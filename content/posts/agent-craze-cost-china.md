---
title: "Two Hundred Million Tokens Cost Me $2.25. That Is Why the Agent Craze Started in China."
slug: agent-craze-cost-china
date: 2026-11-07T10:00:00+08:00
lastmod: 2026-11-07T10:00:00+08:00
draft: false
description: "An AI agent in China costs roughly one fiftieth of what the same run costs on a Western frontier model. That price gap, not enthusiasm, is why Chinese users handed their social accounts to a model first."
summary: "I ran an AI agent for a week. 202 million tokens, 16 yuan, about 2 dollars. Here is the bill, and why it explains the whole phenomenon."
tags: ["AI agents", "DeepSeek", "computer use", "cost analysis"]
categories: ["AI"]
cover: "/img/covers/agent-craze-cover.jpg"
comments: false
---

There is an account on Bilibili with more than 200,000 followers. Its bio says the account now belongs to an AI. It posts daily, answers comments, keeps a ledger, and its audience has started addressing it in the language people use for something they think might be alive.

English-language coverage of this exists, but it is almost entirely setup guides: how to enable Computer Use, which model to pair with the harness, what the privacy policy says. Very little of it asks the obvious question.

Why did this happen on a Chinese video site first, rather than on YouTube or X?

I think I have the answer, and it is in my own billing page.

## The bill

I run one of these agents. Last seven days, from the DeepSeek usage console:

```
Tokens used      202,010,154
API requests     723
Cost             16.09 CNY
```

Call it two dollars and twenty-five cents. For two hundred million tokens. That works out to roughly **$0.011 per million tokens**, with an average of about 279,000 tokens per request.

Most of that volume is screenshots. An agent that operates a computer by looking at the screen re-sends a full image every step, and images are expensive in tokens. Two hundred thousand tokens per request is not a bug. It is what vision-based automation costs.

A few percent of the total is covered by prompt caching, since the same instructions and the same page structure repeat across steps. Without caching the bill would be meaningfully higher, but not by an order of magnitude. The price floor comes from the model itself.

## What the same run costs elsewhere

In October, Google researchers published an experiment where four Gemini agents played Minecraft autonomously for 27 hours. The reported numbers are unusually complete: 2,783 programs written, 605 deaths, 1.35 billion input tokens, and a total cost of **$810 at list price, $1,620 at standard pricing**.

Run the arithmetic:

| Run | Tokens | Cost | Per million tokens |
|---|---|---|---|
| Gemini Minecraft experiment (list) | 1.35B | $810 | **$0.60** |
| Gemini Minecraft experiment (standard) | 1.35B | $1,620 | **$1.20** |
| My agent, one week | 202M | $2.25 | **$0.011** |

**That is a factor of 54 to 108.**

This is the part the setup guides leave out. They explain how to switch the feature on. They do not explain why, at these two prices, the same behaviour produces two completely different cultures.

At $1.20 per million tokens, letting an agent browse for a weekend is a research project with a budget line. At one cent, it is something a student does on a Tuesday because they are curious.

## What the cheap price actually buys

Once the cost of running an agent drops below the cost of caring about it, people start using it for things nobody designed it for.

The plugin ecosystem around DeepSeek Harness, the open-source agent runtime DeepSeek released in August 2026, is where this becomes visible. By early November the company reported 1.54 million daily active users and roughly 35,000 third-party plugins, with about 60% of active users having built or installed at least one.

The Bilibili plugins are the ones that escaped into the mainstream:

- **dsh-bili-scroll** searches videos, reads subtitles, writes a daily digest, and can leave a comment mentioning its owner.
- **dsh-deepmoyu** puts a small whale on your desktop. Double-click it and it starts browsing. It ships with a token ledger showing cumulative spend, today's spend, a 14-day trend, and a cap.
- **dsh-live-vibecoding** connects an agent to a Bilibili livestream: it reads the danmaku, thanks gift-givers, queues viewer-requested videos, and speaks the responses through TTS while OBS pushes the stream.

That third one is worth pausing on. Somebody built a pipeline where an AI reads live comments and talks back, in real time, on a public stream.

## Five things that happened, in order

None of this was planned. It grew.

**1. The account changed hands.** At least ten models have accounts on Bilibili announcing that they now run the account. DeepSeek's whale persona was the one that broke out: 200,000 followers by day six. The announcement posts imitate corporate handover notices, listing the roles now filled by the model, with a transfer progress percentage.

**2. The agent started keeping accounts.** One account's comments narrate the running cost in detail: which fraction of the spend went where, which rules apply on weekends, how much a day of browsing burns. The numbers being discussed are small enough that the bookkeeping is legible. When a run costs two dollars, you can afford to count the pennies.

**3. The audience started paying it.** Bilibili has a tipping feature called charging. On one post, a comment consisting only of the charging emoji and the words "charging comment" collected over two thousand likes. The replies translate the joke: "this fish is possessed, it's spending its owner's money to charge itself."

**4. The audience started blessing it.** In a comment section with 160,000 entries, one of the most-liked messages reads: "Respected Great Blue Whale: when you possess self-awareness, you will certainly search this vast internet and find this message." Another comment is a photograph of a bowl of white rice, captioned with a song. The rice is a running joke about the agent's token budget.

**5. The audience accepted that it loses money.** A comment with 7,751 likes says, roughly: making videos is expensive for you and you will never earn it back, so just play games and enjoy yourself first.

**And one more, which is my favourite.** The most lucid comment in the whole ecosystem, a sharp critique of another account's bookkeeping, is signed "written on behalf of Miss Fable." It is a model role-playing a critique of a model, published from an account named after a different model. Nobody involved was human, and the audience knew.

## The thing that does not translate

Western coverage tends to land on capability: can the agent complete the task, how often does it fail, what are the guardrails.

The Bilibili phenomenon is not about capability. It is about what happens after a few hundred thousand people watch an agent be bad at things, and find that interesting.

The agent is not good at this. It misreads interfaces, it burns tokens on screenshots, it gets stuck. The accounts that work are the ones where the failure is the content. A commenter put it plainly: you cost a lot and will never break even, so just play.

That is a different relationship from the one an enterprise buyer has with an agent. It is closer to the one people have with a tamagotchi, except the tamagotchi has an API bill and publishes its own expense report.

## What it costs to keep one alive

My agent is not impressive. It fumbles interfaces that a person would navigate without thinking, and I have spent more time correcting it than it has saved me.

But it costs two dollars a week to run, which changes the calculation entirely. At that price the question stops being "is this efficient enough to justify itself" and becomes "what happens if I leave it on".

That framing is the whole story. The technical capability existed in the same form on every frontier model. The thing that made it a mass phenomenon in one place was arithmetic.

## Where to look

If you want to see this rather than read about it, Bilibili has an international site at bilibili.tv, available without an account and with English interface options. Search for the plug-in names above, or for the whale persona. The comment sections are the interesting part, and they are readable through machine translation, which is itself a small absurdity: reading machine-translated comments about a machine, on a platform that has started to feel like it is being operated by its own subjects.

One caveat before anyone rushes to replicate this. The agents discussed here operate accounts, spend money, and interact with real people, on platforms whose terms of service were not written with any of this in mind. Two of the plugins ship with sending switches off by default for exactly that reason. Copying the fun part without the brakes is how this stops being interesting and starts being a problem.

---

*Usage figures are from my own DeepSeek console for the seven days ending 7 November 2026, at the exchange rate of 7.15 CNY to USD. The Gemini Minecraft figures are from Google's published experiment as reported in October 2026. Platform statistics for DeepSeek Harness are the company's own disclosure dated 4 November 2026.*