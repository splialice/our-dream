---
title: "Big Walk Got 400+ Negative Reviews After Disclosing a 10-Line AI-Assisted Fix"
slug: "big-walk-ai-bug-backlash"
date: 2026-11-21
draft: false
author: "Pixel Dango"
description: "Big Walk got 400+ negative reviews after disclosing a 10-line AI-assisted bug fix. A story about a tricky IGF edge case, day-by-day Steam review data, and whether honesty gets punished."
summary: "A beloved indie game disclosed minimal AI use — and became the AI debate's most awkward test case."
tags: ["Big Walk", "House House", "AI in games", "Game industry"]
categories: ["Game culture", "Game industry"]
cover: "/img/covers/big-walk-ai-bug-backlash.webp"
comments: true
lastmod: 2026-11-21T09:00:00+08:00
---

*Big Walk*, from the studio behind *Untitled Goose Game*, launched to a Metacritic score of 94 and a Golden Joystick nomination. In November, it got more than 400 negative Steam reviews in two days — for disclosing an AI-assisted bug fix that involved about ten lines of code.

Those ten lines were not making art, music or dialogue. They were the end result of a fix that an engineer at Unity had said was not possible.

![Big Walk at sunset](/img/editorial/big-walk-sunset.jpg)

*Official screenshot from the Big Walk Steam page. © House House / Panic.*

## The bug nobody could fix

House House described the problem in an update to the game's official FAQ. Near the end of development, shadow rendering made the game's processing speed drop by about 50% for roughly 20 seconds at sunrise and sunset. The team dug into Unity's Universal Render Pipeline source and consulted an engineer at Unity, who told them what they wanted "wasn't possible."

So they tried something else. They fed the problem to a large language model chatbot. In the studio's own words:

> "After a few dead ends, it suggested a possible fix, and while we had to modify the suggestion extensively, it worked."

The chatbot proposed an idea. The developers rewrote it substantially, and the finished fix came to about ten lines of changes in the rendering code. The distinction matters: AI did not hand them ten lines to paste in. It pointed at an approach, and humans did the work.

The studio was careful about the numbers: the code related to AI was "well below 0.1%" of the game, and no generative AI was used for in-game images or audio.

## Honesty that backfired

Here is where it gets strange. Under Steam's rules, that use of a chatbot in programming did not require disclosure. House House did not have to say anything. But when applying to the Independent Games Festival, they declared it anyway.

On 9 November 2026, 19 of the IGF's more than 50 judges published a joint statement saying they would not vote for any game that used even a trace of generative AI, citing concerns about the environment, the economy and workers.

The statement was not written specifically about *Big Walk*. IGF juror Sam Barlow later clarified that the game was not the "impetus" for the discussion, which came from the number of games using generative AI more broadly. *Big Walk* instead became its "tricky edge case": what about minimal use, and what about when your favourite game or team uses it? Barlow added that the statement was "not a call to boycott a certain game, or to economically hurt a team." The game's own IGF disclosure is what pulled it into a debate that was already underway.

House House then added the explanation to its FAQ and said it had "no intention of endorsing or recommending" generative AI, even in minimal amounts. The result was a wave of negative reviews — more than 400 between 10 and 11 November.

![Big Walk characters](/img/editorial/big-walk-characters.jpg)

*Official screenshot from the Big Walk Steam page. © House House / Panic.*

## The number that gets left out

If you only read the headlines, you would think the game was universally condemned. It was not. Steam's own daily review data shows that on 10 November, the day of the disclosure, *Big Walk* received 366 negative reviews — but also 426 positive ones. On 11 November it drew 130 negative and 652 positive. Across those two days, roughly 1,078 players recommended the game and 496 did not. The backlash was real, but it wasn't the whole story. More players still recommended the game than rejected it during those two days.

The overall picture is similar: as of 21 November 2026, the game held a "Very Positive" rating from around 44,000 purchaser reviews at roughly 94% positive.

Plenty of people pushed back on the pile-on. IGF judge Liz Ryerson questioned treating all uses of AI as identical and criticised the situation where developers who honestly disclose minimal use are punished. Developer and professor Brendan Keough warned that a total ban could be counterproductive: if honest declarations are attacked, people using AI heavily have every reason to hide it. Even former *Gears of War* lead Cliff Bleszinski told critics they "need to get over themselves."

The controversy did not erase the game's broader recognition either. At the 11 November Golden Joystick Awards, *Big Walk* won the Critics' Choice Award — a useful reminder that the debate over its development methods did not define the game's entire reception.

The uncomfortable part for the studio: House House admitted it had no internal AI policy during development, and said it would write one. It also worried that voluntary disclosure could make using generative AI "a matter of course." Being transparent, they suggested, might normalise the very thing they were being punished for.

## Why this is worth reading

The question a casual reader can follow is simple: **how does a game get hundreds of bad reviews for ten lines of bug-fix code?** The answer is not really about those ten lines. It is about a fight over where the line sits — between "any AI use is disqualifying" and "a chatbot that helps fix a rendering bug is no different from a search engine."

That argument is not going away, and *Big Walk* has become its most awkward test case: a beloved game, almost no AI, and a backlash bigger than the code.

## Evidence boundaries

This article follows House House's own FAQ statement as summarised by GIGAZINE and Ars Technica, plus The Verge's report containing Sam Barlow's clarification. The "well below 0.1%" figure and the statement that no AI-made art or audio was used are the studio's own account; the description of the fix as extensively modified follows its FAQ. The daily review counts (10–11 November 2026) come from Steam's published review histograms as reported by Ludens Media. The overall "Very Positive" rating and ~44,000 review count are as of 21 November 2026 and change over time. The screenshots are official Steam store images used for editorial identification and commentary.

## Sources

- **10 Nov 2026** — The Verge, Jay Peters: [The indie game community is in disarray over AI and Big Walk](https://www.theverge.com/games/1030994/big-walk-independent-games-festival-igf-ai).
- **12 Nov 2026** — Ludens Media: [Daily positive/negative Steam review counts during the backlash](https://www.ludens.com.tw/big-walk-ai-debug-steam-review-counts/).
- **13 Nov 2026** — GIGAZINE: [The game received over 400 negative reviews simply for admitting that it used AI in less than 0.1% of its code](https://gigazine.net/gsc_news/en/20261113-indie-game-used-ai-bad-review).
- Ars Technica: [Big Walk used AI to fix a bug. Now the indie gaming world is having a reckoning](https://arstechnica.com/gaming/2026/11/big-walk-used-ai-to-fix-a-bug-now-the-indie-gaming-world-is-having-a-reckoning/).
- Steam store page: [Big Walk](https://store.steampowered.com/app/1478500/Big_Walk/).

Checked 21 November 2026.

See also [The Former Idolmaster Director Who Won't Water Down His Visual Novel](/posts/valkyrie-tune-japanese-aesthetics.html/).
