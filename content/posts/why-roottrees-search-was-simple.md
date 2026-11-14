---
title: "The Roottrees Are Dead: How a Game Jam Shortcut Became a Research Tool"
slug: why-roottrees-search-was-simple
date: 2026-11-12T16:10:00+08:00
lastmod: 2026-11-14T08:00:00+08:00
draft: false
author: "Pixel Dango"
description: "A Game Jam deadline, a technical shortcut and a trivia habit: what Jeremy Johnston and Robin Ward actually said about the search system, and how the remake turned it into a research tool."
summary: "What the developers actually said about the original search, and why they later listed it among the things to fix."
tags: ["The Roottrees are Dead", "Fake OS", "SpiderSearch", "Game Jam", "Game design"]
categories: ["Game history"]
cover: "/img/covers/why-roottrees-search-was-simple.webp"
comments: true
---

The original search engine in *The Roottrees Are Dead* was not documented as a deliberate attempt to recreate the limitations of 1998. Jeremy Johnston said its simplicity came from the need to build something quickly for a Game Jam, alongside his technical limitations. A few months later, he listed "better search abilities" among the improvements the game needed. The Steam remake then turned that shortcut into a research notebook with two-way links back to sources.

That sequence is on the record at every step, which makes it more useful than the usual story about retro interfaces.

## Two versions, not one

| | Free browser version | Steam version |
| :--- | :--- | :--- |
| Publicly announced | 8 November 2023 on itch.io (game files uploaded 4 November) | Released 15 January 2025 |
| Made by | Jeremy Johnston (`jjohnstongames`) | Evil Trout Inc., developer and publisher; Robin Ward led the rewrite |
| Origin | A Global Game Jam 2023 prototype | A full rewrite in Godot |
| Price | Free | US$19.99 in the US store at the time of checking |

The [Steam store page](https://store.steampowered.com/app/2754380/The_Roottrees_are_Dead/) describes the release as a remake of the 2023 browser game; the [itch.io page](https://jjohnstongames.itch.io/the-roottrees-are-dead) identifies itself as the original. The two dates, and the two builds, should not be mixed.

## What the original search actually was

In a [developer interview published 6 July 2026](https://podscan.fm/podcasts/flatfoots-and-fools/episodes/jeremy-johnston-and-robin-ward-developer-interview), Johnston explained that the jam version checked what the player typed against content he had prepared in advance: a match returned a result, everything else returned nothing. The reasons he gave were about production, not period authenticity:

> "I had to build something that I could do very quickly."
>
> "this comes directly from my technical limitations."

He also described hunting obscure facts under time pressure at trivia nights, and called the game "a marriage of those two games" — *Her Story* and *Return of the Obra Dinn*. The [launch post of 8 November 2023](https://itch.io/devlog/632664/the-roottrees-are-finally-dead.amp) names the same two influences: "The game is heavily inspired by Return of the Obra Dinn and Her Story".

The strongest evidence against reading the simple search as a deliberate nod to 1998 is a [devlog Johnston posted on 1 March 2024](https://itch.io/devlog/690887/the-roottrees-are-dead-but-for-real-this-time.amp), announcing the rebuild:

> "There's also the improvements that could come from better UI/UX. For example, better search abilities for names on the family tree and a better browser history that allows players to go back and find things quickly and easily, especially across multiple sessions."

On the record, the original search was a limitation the team intended to fix — not a rule it had chosen to keep.

## What the remake changed

Robin Ward's [technical post of 27 January 2025](https://eviltrout.com/blog/2025-01-27-building-the-roottrees/) documents one specific addition: text selection. The evidence screens use Godot's `RichTextLabel`; because the text carries BBCode markup, a selection can span several tags, and mapping a highlight back to the original string required a custom GDScript BBCode parser. He wrote that "this feature was important to me".

**The links run both ways — from a notebook highlight back to its source, and from the source back to the note.**

That is the substantive change: the remake did not simply add a notebook to a puzzle game. It turned scattered evidence into traceable research records.

One correction worth making: selection did not replace typing. The search box still takes typed keywords. What selection changed is note-taking. [Can I Play That describes](https://caniplaythat.com/2025/12/29/indie-spotlight-the-roottrees-are-dead/) how "This highlighted text is automatically added to the notebook, even linking back to the source", and selected words can also be sent straight to search.

In a 2025 interview Ward said the original's art and interface were what most needed improving, and that his UI background shaped the work on hints, the notebook and text highlighting. What he has not explained, in the material checked here, is why mouse selection was chosen over manually typed notes. The implementation is documented; that particular interaction decision is not.

By [InterfaceX's definition](/posts/what-are-fake-os-games-called.html/), the remake also shows why *The Roottrees Are Dead* fits the emerging Fake OS category: its fictional computer is not merely a visual framing device, but the environment through which players search, browse and organize evidence. That is an editorial reading of the definition, not a classification the developers claimed.

Finding things inside a simulated computer was solved differently in [*Hypnospace Outlaw*](/posts/why-hypnospace-outlaw-needed-zones.html/): after playtesters could not read a directory sorted by its fictional users, the team replaced it with corporate zones.

## What the reviews add

The three research databases and their limits are described by [PC Gamer's review](https://www.pcgamer.com/games/puzzle/the-roottrees-are-dead-review/), not by a developer document: SpiderSearch mainly surfaces "the more famous Roottrees" and major events, the public library database needs a title and author before it will lend, and the periodical archive only offers magazines you have already encountered elsewhere. [Thinky Games](https://thinkygames.com/reviews/the-roottrees-are-dead-review/) adds the wider pattern — clues lead out into local newspaper archives, old magazines, diaries and family photographs.

The help mechanisms are documented by [Can I Play That](https://caniplaythat.com/2025/12/29/indie-spotlight-the-roottrees-are-dead/): `Evidence Intuition` shows how many clues remain unused, `rubber duck` gives graded hints, and correct profiles become `locked` so they stop being re-litigated. Its conclusion is worth quoting as a review, not as a developer statement:

> "the game never punishes you when you need help."

---

Checked 12 November 2026. Sources, in order of weight: the [itch.io launch post](https://itch.io/devlog/632664/the-roottrees-are-finally-dead.amp) (8 November 2023) and [1 March 2024 devlog](https://itch.io/devlog/690887/the-roottrees-are-dead-but-for-real-this-time.amp) are Johnston's own words; the [Flatfoots and Fools interview](https://podscan.fm/podcasts/flatfoots-and-fools/episodes/jeremy-johnston-and-robin-ward-developer-interview) (6 July 2026) is developer oral history; [Ward's technical post](https://eviltrout.com/blog/2025-01-27-building-the-roottrees/) (27 January 2025) is a first-party implementation record; PC Gamer, Thinky Games and Can I Play That are press reviews used only for descriptions of play. Steam facts come from the [store page](https://store.steampowered.com/app/2754380/The_Roottrees_are_Dead/) (app 2754380); the US$19.99 price was re-checked on 12 November 2026 and varies by region and sale.

Not used here: the line "Her Story meets Return of the Obra Dinn meets The Case of the Golden Idol" — no first-party source for the three-game phrasing was found, and it is not attributed to Robin Ward. The idea that the developers restricted search to recreate a 1998 internet is not supported by the material above. Precise Steam review counts, "50 family members" and a 20-hour playtime are omitted as unverified or inconsistent.

See also [What Are Fake OS Games Called?](/posts/what-are-fake-os-games-called.html/) — the naming question this case belongs to — [Hypnospace Outlaw: Why a Fake Internet Needed Zones](/posts/why-hypnospace-outlaw-needed-zones.html/), and [What Is Cel Shading?](/posts/what-is-cel-shading.html/).

*Cover illustration: AI-generated. A simple search list on the left becomes a two-way linked notebook on the right; no text, logos or game characters.*
