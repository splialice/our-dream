---
title: "TF2, Borderlands and the evidence behind an art makeover"
slug: tf2-borderlands-before-the-makeover
date: 2026-11-10T09:40:00+08:00
lastmod: 2026-11-11T11:28:00+08:00
draft: false
author: "Pixel Dango"
description: "Two older games changed how they looked on the way to release. Both left conference material and dated accounts. That is the part missing from the 2026 Probably Stolen story."
summary: "What a 2007 paper and a 2010 GDC slide deck leave behind that a one-sentence social post does not."
tags: ["Team Fortress 2", "Borderlands", "Valve", "Gearbox"]
categories: ["Game history"]
cover: "/img/covers/tf2-borderlands-before-the-makeover.webp"
comments: true
series: "borderlands-art-style"
series_order: 4
series_note: "A wider look at what an art-makeover claim needs as evidence, set beside TF2 and Probably Stolen."
---

When Rock Paper Shotgun wrote about [`Probably Stolen`](/posts/probably-stolen-28-player-demo.html/) in November 2026, it reached for two precedents: Team Fortress 2 and Borderlands. Both, the argument went, had looked radically different before release. Both are real cases. What is less often noticed is how differently they are documented.

One left a conference paper, a developer commentary track and dated screenshots. The other left a GDC talk with its slide deck, on-the-record quotes from its CEO, and a reported account of that same session. The 2026 game left one sentence on X and a press release full of numbers. None of this tells us whether the art change caused any of the three outcomes. It tells us how much evidence a claim about an art change would need.

## The one with a paper

Valve announced `Team Fortress 2: Brotherhood of Arms` in 1998. When it was shown at E3 the following year, it looked like a contemporary military shooter: realistic visuals, a command hierarchy with a Commander class, parachute drops, networked voice chat. Six years of public silence followed, a second delay, several scrapped versions, and regular appearances on Wired's vaporware list. Valve reintroduced the game in July 2006 with the stylised look it shipped with on 10 October 2007 as part of The Orange Box.

That much is a development timeline. The more useful artefact is what Valve published about the decision. In 2007, Jason Mitchell, Moby Francke and Dhabih Eng presented `Illustrative Rendering in Team Fortress 2` at the fifth International Symposium on Non-Photorealistic Animation and Rendering (NPAR 2007, pp. 71–76, DOI `10.1145/1274871.1274883`), with a related SIGGRAPH 2007 course. The abstract's opening is unambiguous about the intent:

> "In Team Fortress 2, we chose to employ an art style inspired by the early to mid 20th century commercial illustrators J. C. Leyendecker, Dean Cornwell and Norman Rockwell."

The official TF2 wiki preserves the accompanying video's transcript, released on 13 August 2007. In it Mitchell explains that the shading, the strong silhouettes and the rim highlights were not decoration: they let players identify classes and assess threats quickly in a fast-moving game.

Wikipedia's account of the game's developer commentary offers another explanation for abandoning the realistic look: it was hard to reconcile with deliberately unrealistic gameplay, in which two teams maintain elaborate bases next to each other. That is a secondary account of an in-game commentary track, not a statement in the paper above, so it sits one step further from the source.

So for TF2 there is a published design rationale, a technical paper describing how it was implemented, and a date for each. The original Valve-hosted PDF is now a 404 (checked 9 November 2026); the paper survives through its DOI and the official transcript. That is a separate lesson about links, but the documentary chain itself is intact.

## The quotes, and the talk behind them

Borderlands was unveiled in 2007 as "Diablo meets Mad Max" and was originally expected for Christmas 2008. By April 2009, screenshots from a magazine preview had started a debate about its new look. The paper trail for what happened next runs through contemporaneous reporting, a June interview, a post-launch technical article and a conference talk the following March. Those layers are worth keeping separate: the 2009 material records the decision and the naming dispute while they were happening, and the 2010 material is Gearbox describing the work in its own slides.

On 9 April, Kotaku published Randy Pitchford's email response under the headline `Gearbox: "Borderlands Is Not Cel-Shaded"`:

> "No, Borderlands is not cel-shaded — it's a gritty and serious world after all."

On 14 April, Kotaku transcribed a longer statement from the official Gearbox forum, in which Pitchford said that since the game was first unveiled the team had "made big advancements with the art direction and the technology to support the art, and have produced some pretty impressive, even shocking results." New techniques and methods let the game render its concept art in real time, but the team had no settled name for the result: "We don't know what to call the result. You can use whatever term you like." Gearbox itself settled on `Concept Art Style`. That is a choice of its own label, not a demand that everyone else stop saying cel-shaded. Eurogamer covered the same exchange on 14 April; it is contemporaneous reporting of those statements, not the original source for them.

This is worth pausing on. "Borderlands went cel-shaded" became a common shorthand, but it does not reflect how Gearbox described the work at the time. `Concept Art Style` is the studio's own name for its art direction; cel shading is a rendering technique, and the family resemblance is a visual classification rather than an official label. Keeping the two apart is more useful than declaring one side wrong. For the short answer to the question itself, with the four dated sources, see [Is Borderlands Cel Shaded?](/posts/is-borderlands-cel-shaded.html/).

A June 2009 Kotaku interview provides a clearer account of how the change happened. Pitchford said that four artists prototyped a new visual direction after growing frustrated that many games looked alike. He initially expected to reject the proposal, but changed his mind after seeing the prototype in motion. The new direction subsequently gained support from Gearbox management and publisher 2K.

A post-launch article on Unreal Engine's own site, dated 27 October 2009, supplies the technical half of the chain. It says the extended development cycle gave Gearbox's art team an important opportunity, and quotes Pitchford directly: "From a small group of artists came an initiative to render the concept art style in the game." The prototype impressed Gearbox's management and publisher 2K, and Gearbox engineers then extended Unreal Engine 3's rendering, adjusted lighting and shading for the new look, added new rendering techniques alongside the artists, and kept the work compatible with the UE3 codebase. That is an engine vendor's technical write-up carrying one direct quote, not a full development interview: it does not list which art assets were changed, and on its own it cannot settle the cel-shading label either way. The page returned 403 from this machine, so the details above were checked against the original during review.

In March 2010 Gearbox took the change to GDC. The session was titled `Borderlands & The 11th Hour Art Style Change (Don't Try This at Home)`. Randy Pitchford dropped out at short notice, so co-founder and chief creative officer Brian Martel presented with creative director Mikey Neumann and VP of product development Aaron Thibault. [GameSpot's report of the session](https://www.gamespot.com/articles/behind-borderlands-11th-hour-style-change/1100-6253257/), published 15 March 2010, says the game was already 75 percent finished. The studio's own [132-slide deck](https://media.gdcvault.com/gdc10/slides/Martel_Brian_Borderlands_and_the_11th_Hour_Art_Change.pdf) is still hosted by GDC Vault. Slide 7 places `art style change` inside the final phase of the project (Oct 08 – Oct 09), alongside a doubled team size and a finalised story and design. Slide 49 says of the prototype, "That is why we hid in a closet and did a secret prototype." Slide 53 labels the comparison `FAKE CEL SHADING` versus `BORDERLANDS SHADING (Concept Art Style)`. Slide 60 gives four reasons for the change: embrace fun, stand out from the crowd, break the plausibility shackles, make a beautiful game.

That is a different kind of source from a CEO quote. It is a studio presenting its own process, with a dated timeline, at a conference — the same broad category as TF2's paper, though a slide deck is not peer-reviewed and does not document the renderer in the same detail. A 2025 [Game Informer interview](https://gameinformer.com/2025/09/01/the-behind-the-scenes-story-of-the-art-style-swap-that-saved-borderlands-1) adds the view from sixteen years later: Pitchford recalls giving "five guys" two weeks to try, and lead level designer Graeme Timmins remembers that almost every level was rebuilt. Useful colour, but recollection rather than a contemporaneous record.

What matters here is not which label is correct. It is that Gearbox documented the change twice: in 2009 through on-the-record quotes and interviews while it was happening, and in 2010 at a conference through its own slides and timeline. The naming dispute is the loudest part of that record, not the whole of it.

## What a makeover claim needs

Set the three cases side by side and the difference is not the outcome. It is the record.

| | TF2 (1999–2007) | Borderlands (2007–2009) | Probably Stolen (2025–2026) |
| :--- | :--- | :--- | :--- |
| What changed | Realistic military look → commercial-illustration style | Gritty realistic look → `Concept Art Style` | Visuals reworked; name and publisher changed |
| What documents it | Conference paper, video transcript, in-game commentary, dated reveals | GDC 2010 talk and slide deck, dated CEO quotes, a June 2009 interview, a UE3 technical write-up, a reported GDC session | One X post; a launch press release with wishlist and player figures |
| Stated design reason | Realism clashed with unrealistic gameplay (via developer commentary) | Realism clashed with exaggerated gameplay and resembled Fallout 3 and Rage (GDC 2010, GameSpot report) | "focus on what works design wise" — no further detail found |

For `Probably Stolen`, tinyBuild's own launch release of 28 October 2026 gives 500,000+ wishlists, 660,000+ demo players and a near-40,000 Next Fest peak. Those are useful numbers about reach. They are not an account of which design decisions were made. Rock Paper Shotgun's caveat on the whole episode was blunt: "The situation is almost certainly more complicated than Nichiporchik makes it sound."

None of this means the visual work was irrelevant in any of the three cases. It means the evidence available to a reader is wildly uneven — just not along the line the comparison first suggests. TF2 and Borderlands both left conference material and contemporaneous accounts: one a technical paper with a published rationale, the other a slide deck with a timeline and a reported session. Both let you reconstruct an argument, at different resolutions. A one-sentence post lets you reconstruct a claim, and a press release lets you count an audience. Treating those as the same kind of source is how "they changed the art and it went viral" becomes a fact rather than a summary.

It is also worth resisting the obvious induction. These are three projects from 1999, 2009 and 2026, on different platforms, with different publishers and different markets. Putting them in a list proves that visual overhauls happen. It does not prove why any of them worked.

Even the dates need the same caution: [Steam's own metadata](/posts/what-a-steam-page-cant-tell-you.html/) lists a 2023 date for a Borderlands package, which says more about the listing than about the 2009 release. The older cases survive as history partly because people wrote down their reasoning at the time. The 2026 case is being written mostly in numbers. In another twenty years, the difference between a store page, a press release and a conference paper may be the only thing left to read.

---

### Sources

Checked 9–11 November 2026. The GDC 2010 slide deck was downloaded and read in full on 11 November 2026; the GameSpot report and the 2025 Game Informer interview were read in full the same day.

- [Official TF2 Wiki: Illustrative Rendering in Team Fortress 2](https://wiki.teamfortress.com/wiki/Illustrative_Rendering_in_Team_Fortress_2) — video transcript, 13 Aug 2007; influences and stated gameplay purpose.
- [Wikipedia: Team Fortress 2, Development](https://en.wikipedia.org/wiki/Team_Fortress_2) — 1998 announcement, E3 1999 realistic look, July 2006 reveal, 10 Oct 2007 release, secondary account of the developer commentary.
- [NPAR 2007 paper DOI](https://doi.org/10.1145/1274871.1274883) — Mitchell, Francke, Eng, pp. 71–76. The ACM page returned 403 during research; the original Valve-hosted PDF now returns 404.
- [Kotaku, 9 Apr 2009: Gearbox: "Borderlands Is Not Cel-Shaded"](https://kotaku.com/gearbox-borderlands-is-not-cel-shaded-5206042) — Brian Ashcraft; Pitchford's email response. Original article directly verified, 10 November 2026.
- [Kotaku, 14 Apr 2009: Gearbox Explain Cel-Shaded Borderlands](https://kotaku.com/gearbox-explain-cel-shaded-borderlands-5210855) — Luke Plunkett; Kotaku's transcription of the official Gearbox forum statement and the `Concept Art Style` naming. Original article directly verified, 10 November 2026; the Gearbox forum post itself was not independently checked.
- [Eurogamer, 14 Apr 2009](https://www.eurogamer.net/pitchford-borderlands-will-not-be-cel-shaded) — contemporaneous reporting of the same exchange, not the original source of the quotes.
- [Kotaku, 12 Jun 2009: The New Borderlands Look That Almost Wasn't](https://kotaku.com/the-new-borderlands-look-that-almost-wasnt-5288292/) — Brian Crecente; interview on the four-artist prototype and how the change nearly did not happen. Original article directly verified, 10 November 2026.
- [Unreal Engine, 27 Oct 2009: Gearbox Software's Borderlands More Awesome Than Ever with Unreal Engine 3](https://www.unrealengine.com/blog/borderlands?lang=en) — the engine vendor's technical account of the UE3 rendering work, with a direct Pitchford quote; a technical write-up rather than a full studio interview. The page returned 403 from this machine and was checked against the original during review.
- [GDC Vault: Borderlands & The 11th Hour Art Style Change](https://media.gdcvault.com/gdc10/slides/Martel_Brian_Borderlands_and_the_11th_Hour_Art_Change.pdf) — Brian Martel, GDC 2010, 132 slides. Timeline on slide 7, secret prototype on slide 49, `FAKE CEL SHADING` / `Concept Art Style` on slide 53, stated reasons on slide 60. PDF downloaded and read in full, 11 November 2026.
- [GameSpot, 15 Mar 2010: Behind Borderlands' 11th-hour style change](https://www.gamespot.com/articles/behind-borderlands-11th-hour-style-change/1100-6253257/) — Tor Thorsen; report from the GDC session. 75 percent complete, Truth Team review, "Brown Period", jump height as trigger, Martel's closet prototype, staff departure, reused assets and shortcuts. Read in full, 11 November 2026.
- [Game Informer, 1 Sep 2025: The Behind-The-Scenes Story Of The Art-Style Swap That Saved Borderlands 1](https://gameinformer.com/2025/09/01/the-behind-the-scenes-story-of-the-art-style-swap-that-saved-borderlands-1) — Brian Shea; interviews with Pitchford, Adam May and Graeme Timmins. Retrospective testimony, sixteen years after the fact. Read in full, 11 November 2026.
- [tinyBuild launch press release, 28 Oct 2026](https://www.gamespress.com/ja-JP/TINYBUILD-SMUGGLES-PROBABLY-STOLEN-THE-GRITTY-PIXEL-ART-CYBERPUNK-SHOP) and [Alex Nichiporchik on X, 29 Oct 2026](https://x.com/aNichiporchik/status/2115777936527901098) — the 2026 comparison.
- [Rock Paper Shotgun, 4 Nov 2026](https://www.rockpapershotgun.com/smash-hit-cyberpunk-storekeeper-probably-stolen-was-originally-a-different-non-cyberpunk-game-that-seemed-destined-to-sink-without-trace/) — the two precedents and its caveat.

*Cover illustration: AI-generated with Doubao. The on-image label was removed by cropping so the artwork can run at full width; the AI disclosure is kept here instead.*
