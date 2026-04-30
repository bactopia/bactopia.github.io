---
title: Bactopia v4 Updates and Improvements
authors: [rpetit3]
tags: [community, release]
date: 2026-04-29
slug: bactopia-v4-updates
description: Learn about the new features and improvements in Bactopia version 4.
---

Howdy folks! Robert here, developer of Bactopia! It’s been a while, huh? Well it's finally
here! I’m super excited to announce the [release of Bactopia version 4](https://github.com/bactopia/bactopia/releases/tag/v4.0.0)!

You might be wondering what’s new in Bactopia? And the answer is **_a lot_**, but
also… **_not a lot_**, but in a good way! How can that be? Well, about that…

## Bactopia is all Strict, Static and Records now!

Over the last year [Nextflow](https://nextflow.io/) (the engine that Bactopia is based on)
has undergone a significant metamorphosis, with the [introduction of Strict Syntax and Static Types in v25](https://seqera.io/blog/nextflow-25-10-plugin-registry/),
and [now Record Types in v26](https://github.com/nextflow-io/nextflow/releases/tag/v26.04.0). Haha
if you’ve ever looked at the Bactopia code base, you would have quickly seen that it was
the least strict thing. Bactopia took advantage of many things in Nextflow that weren’t really
the intended purpose (e.g. [launching 60+ workflows from a single workflow…](https://github.com/bactopia/bactopia/blob/4b075af96da522222bb075d4b65927d1ba3de9c2/workflows/bactopia-tools.nf)). 

So, to answer your first question: _how did Bactopia change a lot, without changing a lot?_

Well, in order to implement strict syntax, static types, and record types, I had to essentially rewrite the
code base, almost from scratch (_which again is not necessarily a bad thing!_). As you can see in the
image below, v4 of Bactopia changed 2,641 files, with 140k additional lines of code and 55k
removed lines of code. It's true! Check out the [CHANGELOG](https://github.com/bactopia/bactopia/blob/master/CHANGELOG.md#v400-bactopiabactopia-cream-puff-20260429)!

![Bactopia v4 Changes](./img/image1.png)

In version 4 of Bactopia, I’m happy to report that I’m now compliant with the future of Nextflow! Which as a side-effect, means Bactopia should now play much nicer both locally and in the cloud.

While Strict Syntax, Static Types, and Record Types aren’t exactly “required”, I think their
adoption has put Bactopia in a much better place than it was before. Cheers to the folks at
[Seqera](https://seqera.io/) (_who maintain Nextflow_) for getting that implemented!

## Co-development with AI

[can you write a message about the usage of llms in Bactopia] Haha, just kidding, it's still me
writing this post! But, on a more serious note, **_going forward Bactopia will be utilizing AI in
the future developments and maintenance_**. I’m the only developer and maintainer of Bactopia, so I
have to balance what I can, to avoid burnout going forward. However, my usage of AI is not without a
lot of thought. There won’t be any AI agents getting unrestricted access to do what it wants with
Bactopia. Trust me, Bactopia is something I care about deeply, and I plan to continue maintaining ownership of it.

I’ve made extensive efforts to ensure there are specific guardrails for AI to follow, as well as
ways for me to verify those guardrails are being followed. With the introduction of strict syntax, static types, and
record types, I was able to incorporate numerous patterns that are well suited to LLMs and these
guardrails I’ve set up. At the end of the day, I will still be very much involved in reviewing any changes
made by LLMs and pushing Bactopia forward. I just wanted to briefly state my stance on the usage of AI and LLMs to help co-develop Bactopia.

![Bactopia's AI Feedback Loop](./img/image2.png)

I feel a more lengthy post is still needed to demonstrate my process when using LLMs for
Bactopia. _I’ll be sure to get that out soon!_

## Bactopia is easier to support now

With that out of the way, I mentioned I spent a lot of time rewriting Bactopia, and turns out the
rewrite didn’t move the dial much, but that’s a good thing. You might be wondering, _how is all this
effort to end up where you started a good thing?!?_ Well, when you get the opportunity to rewrite
something, you get to rewrite it based on your current experience and abilities. I’m not the same
bioinformatician I was over 7 years ago, when Tim and I first released Bactopia. I sometimes wonder:
_'why did 2017 Robert do it this way?'_ and _'why is 2026 Robert so much more gray?!'_

But, to me at
least, this rewrite provided the opportunity to unload a lot of technical debt past Robert built up
over the years. I was able to standardize many pieces of Bactopia, so a module is a module is a
module is a module, etc…. I also got to move a lot of the non-Nextflow pieces out of the Bactopia Nextflow
pipeline and into [bactopia-py](https://github.com/bactopia/bactopia-py) and
[nf-bactopia](https://github.com/bactopia/nf-bactopia).

While pytest still worked, I was able to transition to [nf-test](https://www.nf-test.com/) for
all Nextflow files, not just the subworkflows. With this transition, at the moment, Bactopia
now includes 246 tests, which test everything (modules, subworkflows, and workflows) using
real data from the revamped [bactopia-tests](https://github.com/bactopia/bactopia-tests)
repo.

![Bactopia's Test Suite in Action](./img/image3.png)

I was also able to make the documentation built from of in-line
GroovyDoc. Not only that, I moved from [MkDocs Material to Docusaurus](https://github.com/bactopia/bactopia.github.io/pull/9),
and even got this new fancy address! I personally think it will be much easier to maintain,
and am very curious to get your opinions and feedback!

All this, to say:

_If you are a user of Bactopia, what you need to take away is, I now find Bactopia much easier
to build and maintain. Tim and I are in the kitchen cooking up some fun things for the future
of Bactopia. So keep an eye out!_

P.S. As with all major releases, there will be bumps in the road, and I’m sure I may have
missed something. If you find bugs or a feature I missed, just let me know! Maybe even find
me on the [Bactopia Slack workspace](https://bactopia.io/slack/)
 (_haha which I actually created ages ago!_)

To get started with Bactopia version 4, check out the [installation guide](/installation/) and the [tutorial](/tutorial/).
