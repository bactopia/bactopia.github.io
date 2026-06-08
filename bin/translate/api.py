"""Claude API integration for translation.

Adapted from the Nextflow Training project's translation system:
https://github.com/nextflow-io/training/tree/master/_scripts/translate
"""

import asyncio
import random
from dataclasses import dataclass

import anthropic

from .config import (
    BASE_DELAY,
    MAX_CONTINUATIONS,
    MAX_RETRIES,
    MAX_TOKENS,
    MODEL,
    REQUEST_TIMEOUT,
    TranslationError,
    validate_api_key,
)


@dataclass
class TranslationResult:
    text: str
    model: str
    input_tokens: int
    output_tokens: int
    stop_reason: str
    continuations: int


def _extract_text(response: anthropic.types.Message) -> str:
    """Extract text from all text content blocks in a response."""
    return "".join(
        block.text for block in response.content if hasattr(block, "text")
    )


async def _call_once(
    client: anthropic.AsyncAnthropic,
    system: str,
    messages: list[dict],
    label: str = "",
    model: str = MODEL,
) -> anthropic.types.Message:
    """Single API call with jittered exponential backoff on transient errors."""
    for attempt in range(MAX_RETRIES):
        try:
            return await client.messages.create(
                model=model,
                max_tokens=MAX_TOKENS,
                system=[{
                    "type": "text",
                    "text": system,
                    "cache_control": {"type": "ephemeral"},
                }],
                messages=messages,
                timeout=REQUEST_TIMEOUT,
            )
        except (
            anthropic.APIConnectionError,
            anthropic.APITimeoutError,
            anthropic.RateLimitError,
            anthropic.InternalServerError,
        ) as e:
            if attempt == MAX_RETRIES - 1:
                raise TranslationError(f"[{label}] API failed after {MAX_RETRIES} retries: {e}")
            delay = BASE_DELAY * (2**attempt) + random.uniform(0, 1)
            await asyncio.sleep(delay)

    raise TranslationError(f"[{label}] Exhausted retries")


async def call_claude_async(
    prompt: str,
    system: str,
    client: anthropic.AsyncAnthropic | None = None,
    label: str = "",
    model: str = MODEL,
) -> TranslationResult:
    """Send a translation prompt to Claude and return the result.

    Handles automatic continuation when responses hit the token limit.
    """
    own_client = client is None
    if own_client:
        client = anthropic.AsyncAnthropic(api_key=validate_api_key())

    try:
        messages = [{"role": "user", "content": prompt}]
        total_input = 0
        total_output = 0
        full_text = ""
        continuations = 0

        response = await _call_once(client, system, messages, label, model)
        full_text += _extract_text(response)
        total_input += response.usage.input_tokens
        total_output += response.usage.output_tokens

        while response.stop_reason == "max_tokens" and continuations < MAX_CONTINUATIONS:
            continuations += 1
            messages.append({"role": "assistant", "content": response.content})
            messages.append({"role": "user", "content": "Continue exactly where you left off."})
            response = await _call_once(client, system, messages, label, model)
            full_text += _extract_text(response)
            total_input += response.usage.input_tokens
            total_output += response.usage.output_tokens

        return TranslationResult(
            text=full_text,
            model=response.model,
            input_tokens=total_input,
            output_tokens=total_output,
            stop_reason=response.stop_reason,
            continuations=continuations,
        )
    finally:
        if own_client:
            await client.close()
