#!/usr/bin/env python3
"""Fetch papers citing Bactopia from OpenAlex and write data/citations.yml."""
import argparse
import json
import sys
import urllib.request
import urllib.parse
from datetime import date
from pathlib import Path

OPENALEX_WORK_ID = 'W3046929726'
MAILTO = 'robbie.petit@gmail.com'
PER_PAGE = 200
SELECT_FIELDS = 'id,doi,title,authorships,publication_date,primary_location'


def fetch_citations():
    """Fetch all citing works via cursor pagination."""
    works = []
    cursor = '*'

    while cursor:
        params = urllib.parse.urlencode({
            'filter': f'cites:{OPENALEX_WORK_ID}',
            'per_page': PER_PAGE,
            'cursor': cursor,
            'mailto': MAILTO,
            'select': SELECT_FIELDS,
        })
        url = f'https://api.openalex.org/works?{params}'

        req = urllib.request.Request(url, headers={'Accept': 'application/json'})
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read())

        results = data.get('results', [])
        if not results:
            break

        works.extend(results)
        meta = data.get('meta', {})
        cursor = meta.get('next_cursor')
        print(f'  Fetched {len(works)} / {meta.get("count", "?")} citations...', file=sys.stderr)

    return works


def format_authors(authorships):
    """Format OpenAlex authorships into a citation-style author string."""
    names = []
    for a in authorships:
        display = a.get('author', {}).get('display_name', '')
        if display:
            names.append(display)
    if not names:
        return ''
    if len(names) > 10:
        return ', '.join(names[:10]) + ', et al.'
    return ', '.join(names) + '.'


def parse_work(work):
    """Extract citation fields from an OpenAlex work object."""
    authors = format_authors(work.get('authorships', []))
    title = (work.get('title') or '').strip()
    doi = work.get('doi') or ''
    pub_date = work.get('publication_date') or ''

    location = work.get('primary_location') or {}
    source = location.get('source') or {}
    journal = source.get('display_name') or ''

    return {
        'authors': authors,
        'title': title,
        'url': doi,
        'journal': journal,
        'date': pub_date,
    }


def write_yaml(citations, output_path):
    """Write citations as YAML (hand-formatted to avoid PyYAML dependency here)."""
    lines = ['citations:']
    for c in citations:
        title = c['title'].replace('"', '\\"')
        lines.append(f'  - authors: "{c["authors"]}"')
        lines.append(f'    title: "{title}"')
        lines.append(f'    url: {c["url"]}')
        lines.append(f'    journal: "{c["journal"]}"')
        lines.append(f'    date: {c["date"]}')
        lines.append('')

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text('\n'.join(lines) + '\n')


def main():
    parser = argparse.ArgumentParser(description='Fetch Bactopia citations from OpenAlex')
    parser.add_argument('--output', '-o', default='data/citations.yml',
                        help='Output YAML path (default: data/citations.yml)')
    args = parser.parse_args()

    print('Fetching citations from OpenAlex...', file=sys.stderr)
    works = fetch_citations()

    citations = [parse_work(w) for w in works]
    citations = [c for c in citations if c['title']]
    citations.sort(key=lambda c: c['date'], reverse=True)

    seen_titles = set()
    deduped = []
    for c in citations:
        key = c['title'].lower().strip()
        if key not in seen_titles:
            seen_titles.add(key)
            deduped.append(c)
    citations = deduped

    output_path = Path(args.output)
    write_yaml(citations, output_path)
    print(f'Wrote {len(citations)} citations to {output_path}', file=sys.stderr)


if __name__ == '__main__':
    main()
