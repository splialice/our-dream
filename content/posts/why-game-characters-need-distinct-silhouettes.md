---
title: "Why Game Characters Need Distinct Silhouettes: What Valve and Riot Wrote Down"
slug: why-game-characters-need-distinct-silhouettes
date: 2026-11-11T17:20:00+08:00
lastmod: 2026-11-11T17:54:00+08:00
draft: false
author: "Pixel Dango"
description: "Valve built a three-level read hierarchy into Team Fortress 2; Riot made silhouette the anchor of champion recognition in League of Legends. Two related answers to the same multiplayer problem, and the products each changed to enforce them."
summary: "A reading order built into TF2, a skin policy written for League, and a ponytail cut off and then put back."
tags: ["Team Fortress 2", "League of Legends", "Valve", "Riot Games", "Art direction", "Silhouettes"]
categories: ["Game history"]
cover: "/img/covers/why-game-characters-need-distinct-silhouettes.webp"
comments: true
---

"Why do game characters need distinct silhouettes?" is usually answered with a drawing lesson. Search for the question and you get sketch exercises, generators, videos about shape language and long forum threads about whether a design is "readable". Those answer a different question: how to draw one.

The historical answer is written down, and the clearest single piece of it is not in a conference paper or a retrospective interview. It is inside Team Fortress 2 itself. In the game's own developer commentary, Valve's Ariel Diaz says:

> "We developed a read hierarchy for player models, prioritizing the information that players needed to be able to read merely by looking at the model. Our hierarchy was this: first, what team they're on, second, what class they're playing, and third, what weapon they're wielding."

Note the order. Colour answers the first question. The silhouette answers the second. Texture contrast at the chest answers the third. Valve did not make silhouette the first thing a player reads; it made silhouette the thing that identifies a class.

In [a developer article published on 12 March 2021](https://www.leagueoflegends.com/en-gb/news/dev/clarity-in-league/), Riot Games framed it differently for League of Legends:

> "Silhouettes are the single most important thing for champion recognition in League. This is basically a champion's shadow: What do they look like shrouded in darkness?"

There, silhouette is the primary anchor of a character's identity, because the problem was keeping more than 150 champions readable across more than 1,000 skins.

This page is about two related answers to one underlying problem: in a multiplayer match a player has a fraction of a second to work out who is in front of them, which side they are on and what they can do. The frameworks are not the same, and flattening them into one rule loses what is interesting about both. What follows is the written evidence, the differences between the two frameworks, and the cases where each studio enforced its own. It is not a guide to designing characters.

For what Valve gave up to arrive at this look, see [Why Team Fortress 2 Stopped Looking Realistic](/posts/why-team-fortress-2-stopped-looking-realistic.html/).

## The rule in the game's own words

TF2's developer commentary is unusual evidence. It is not an interview given years later, or a slide shown at a conference. It is a set of audio nodes built into the shipped game in October 2007, triggered by pointing at markers in a map, and the [Official TF2 Wiki preserves the transcript](https://wiki.teamfortress.com/wiki/Well_developer_commentary/Transcript).

In the node titled "Functional Character Design", Diaz assigns a technique to each of his three levels. Team comes from the palette: warm colours for RED, cool for BLU. Class comes from the silhouette:

> "Unique silhouette and animation shapes are more identifiable at far distances, and across a broader range of light levels, than any amount of other visual detail on the model."

Weapon comes from texture contrast. The highest-contrast areas sit around the chest, where the weapon is held, and a gradient from dark feet to a bright chest pulls the eye upward. That is a specification, not an aesthetic preference: it says which information wins when a character can only be seen for an instant, and names the part of the model responsible for each piece.

A second node, "Lightwarp and Rimlight", is spoken by Jason Mitchell, one of the authors of Valve's technical paper on the game's rendering. He explains that the team altered diffuse lighting to match early twentieth-century commercial illustration, then adds:

> "Another facet of illustrative shading is the use of rim highlights to accentuate the silhouettes of characters. Without the rim lighting, the characters tend to blend into the scenery."

The shading exists to protect the silhouette. That ordering matters. The illustrated look is often discussed as a style choice; in Valve's own account it is downstream of a readability requirement.

## On paper, and in a talk a year later

The same reasoning appears in the [NPAR 2007 paper, *Illustrative Rendering in Team Fortress 2*](https://steamcdn-a.akamaihd.net/apps/valve/2007/NPAR07_IllustrativeRenderingInTeamFortress2.pdf), by Jason Mitchell, Moby Francke and Dhabih Eng. Its abstract says the techniques were designed "so that game players are consistently able to visually 'read' the scene and identify other players in a variety of lighting conditions". The introduction says the team "sought to explicitly differentiate ourselves from other multiplayer deathmatch games which typically embrace a modern photorealistic look", and credits the commercial illustrators J. C. Leyendecker, Dean Cornwell and Norman Rockwell for the strong silhouettes, the clothing folds and the use of rim highlights rather than dark outlines.

The read hierarchy is also on slide 22 of [Valve's 82-slide GDC 2008 deck, *Stylization with a Purpose*](https://steamcdn-a.akamaihd.net/apps/valve/2008/GDC2008_StylizationWithAPurpose_TF2.pdf). Both documents were downloaded and read in full for [our earlier article on TF2's art direction](/posts/why-team-fortress-2-stopped-looking-realistic.html/), which also sets out what the paper does and does not establish.

The fullest public account of how the hierarchy was arrived at came a year after release. At the Montreal International Game Summit in November 2008, Mitchell gave a talk about Left 4 Dead's visual style that opened with the work on TF2. [Mathew Kumar's report for Game Developer, published 19 November 2008](https://www.gamedeveloper.com/pc/migs-valve-s-mitchell-on-creating-i-left-4-dead-i-s-filmic-visual-style), records the sequence:

> "After a disastrous attempt to create a 'realistic' visual style for that title, they realized the 'visual hierarchy' that defines the way in which a player observes the characters within the world."

The three tiers are the same ones in the commentary. "The first level is their color — are they on my team, or another team?" came from a defined set of mirroring red and blue swatches. Class was carried by silhouettes, with the team going as far as differentiating clothing folds. Weapon was handled by keeping the eye at chest height; Mitchell pointed to the Pyro's blackened, scorched legs as the clearest example of the dark-to-light gradient. He said characters were modelled in character-specific poses rather than a "generic T-shape", and that the world around them was desaturated so they would "pop off" the background, even when a red team member stood in a red base.

The report also gives the technical origin of the rim lighting. Leyendecker's illustrations used highlights that made figures look lit from behind; after a few tests overlaying hand-drawn rim highlights on renders, Mitchell said the team "immediately knew this was what we wanted, and began writing shader code".

One evidentiary caution: the commentary and the paper are Valve-authored and date to the release. The MIGS talk is a journalist's report of a talk given thirteen months later. It is strong evidence for the shape of the reasoning and for the abandoned realistic version, but it is a recollection, not a project log, and it does not date the decision to drop realism. No source in this set does.

## Riot in 2021: a different problem at a different scale

Riot published [*Clarity in League*](https://www.leagueoflegends.com/en-gb/news/dev/clarity-in-league/) on 12 March 2021 under the byline bananaband1t. It opens with a scale Valve never had to manage: "over 150 champs and 1000 skins — not to mention items, runes, and neutral objectives".

Riot frames the goal as three "Unbreakable Vows": gameplay should be clearly conveyed, hierarchy should always be preserved, and noise should be kept minimal. Hierarchy here means that the most important thing at a given moment, such as a major ultimate, draws the most attention. Valve used the same word for the order in which a player reads a model. The usages are not identical, though both treat attention as a limited resource that the art has to allocate.

The article then breaks a silhouette into primary, secondary and tertiary features, and sets the rule for skins:

> "A champion's primary feature should never be removed or significantly altered in any skin."

Senna's gun, Diana's moon weapon and Yuumi being a cat are given as examples. Senna can change her body outline because the gun still identifies her; a skin cannot give her a pea-shooter. A silhouette should also indicate a champion's source of power, their size and playstyle, and even the direction they are facing. The article names the failure case: Lee Sin "has a fairly generic shape, so a lot of his silhouette is carried by his animations", which makes legendary skins hard to design because changing the animations changes the silhouette.

## Two frameworks, not one

| | Valve, Team Fortress 2 (2007) | Riot, League of Legends (2021) |
| :--- | :--- | :--- |
| What silhouette does | Identifies the class — the **second** of three levels | The **primary** anchor of champion identity |
| What comes before it | Team colour | Nothing; it is the top recognition signal |
| What "hierarchy" means | The order in which a player reads a model | Which visual element deserves attention at a given moment |
| What the rule governs | Designing nine classes from nothing | Keeping 150+ champions readable across 1,000+ skins |
| What it costs to enforce | Discarding a realistic art direction | Restricting or altering skins, then redesigning a base model |

Both documents organise visual information by importance so that players can identify characters quickly. That is the shared constraint. It is not the same rule: Valve built a reading order for a fixed cast, Riot built a preservation policy for an expanding catalogue. Neither studio claims the other's framing, and no source in this set connects them.

## The rule enforced

A policy document only shows what a studio says. Riot published a second document a month later that shows what it does. [*Ask Riot: Let's Talk Clarity*](https://www.leagueoflegends.com/en-gb/news/dev/ask-riot-let-s-talk-clarity/), dated 9 April 2021 and credited to Meddler, MechaHawk, OCRAM818, Riot Bellissimoh and Riot Zimberfly, answers player questions about skins that were changed or restricted.

The sharpest case is Blitzcrank. A player asked why the 2017 Lancer skin could not have a new walk animation when the later Space Groove skin did. MechaHawk, Riot's Skins Art Director, answered that the standards had not been clearly defined in 2017, then applied them retroactively:

> "One of the things we now view as key for champion recognition in 2021 is their silhouette, which is basically their shadow. So when we were working on Space Groove Blitz+Crank, we put a lot of effort into making sure the silhouette was still quickly and easily recognizable at Blitz — if you were to give him the 'who's-this-champ?' test, his large hands read similarly to base, as do his head and shoulder pads."

![Abstract diagram: three block figures showing that changing interior detail leaves the shadow unchanged, while changing the outline changes it.](/img/silhouette-diagrams/outline-change.png)

*Diagram: original illustration for this article, drawn with plain geometric shapes. It visualises the distinction Riot describes in [Ask Riot: Let's Talk Clarity](https://www.leagueoflegends.com/en-gb/news/dev/ask-riot-let-s-talk-clarity/) (9 April 2021). No game assets are used.*

Because the hands, head and shoulder pads still read correctly, the team could give Space Groove a floaty walk without putting clarity at risk. Lancer Blitzcrank failed the same test:

> "Lancer Blitzcrank's silhouette is harder to read than Space Groove's, particularly because he has pointy drills instead of 'hands.' This muddies his silhouette when he's standing in lane, running around, and when his Q is coming at you."

![Abstract diagram: four figures sharing one outline but different interiors, compared with four clearly different outlines.](/img/silhouette-diagrams/shadow-test.png)

*Diagram: original illustration for this article, drawn with plain geometric shapes. It illustrates the "who's-this-champ?" shadow test described in [Ask Riot: Let's Talk Clarity](https://www.leagueoflegends.com/en-gb/news/dev/ask-riot-let-s-talk-clarity/) (9 April 2021). No game assets are used.*

The exchange also shows that the rule was not fully formed from the start. MechaHawk says Riot was "mostly going off of intuition" when Lancer Blitzcrank was made in 2017, and that the standards were solidified later. A design principle became an explicit, documented policy as the catalogue grew and player feedback accumulated.

The second case is smaller and more revealing. Storm Dragon Lee Sin was reported as hard to recognise on the public test server, and Bellissimoh, Director of Production, confirmed that "we decided to make some changes before he went live, including cutting his ponytail". The answer then concedes the broader problem: "Lee doesn't really have a distinct character model silhouette. Most of his character recognition is carried through animation" — the same weakness the March article had named, now attached to a specific skin that had to be trimmed because of it.

Valve's equivalent is much larger in scope and much thinner in documentation: an entire realistic art direction was attempted and abandoned. The MIGS report calls it disastrous and describes the hierarchy that replaced it, but no dated meeting or internal document marks the switch. What the two studios have in common is that their respective rules cost something. Riot cut a ponytail and withheld a walk animation; Valve discarded a visual direction for a game already years into development.

## From a skin back to the base model

The Lee Sin story did not end with a trimmed ponytail. On 8 April 2024 Riot published [/dev: Modernizing the Monk](https://www.leagueoflegends.com/en-us/news/dev/dev-modernizing-the-monk/), an account of Lee Sin's Art and Sustainability Update credited to The ASU Team. Its "Preparing the Ponytail" section explains the decision:

> "Adding in a more dynamic ponytail adds an interesting animation and silhouette element to Lee Sin's design. On an additional note, there were some gameplay clarity issues that caused Lee to read as Ezreal or other human champions, so giving him a more unique silhouette should help Lee be more clearly Lee to players."

The article notes that Lee Sin had "always" had a ponytail, but it was wrapped around his shoulders and "essentially glued in place". Making it dynamic was what turned it into a silhouette element, and Riot adds: "for future skins, we plan for the ponytail to be an integral part of his silhouette." Not every skin received it — God Fist, Dragon Fist and Knockout kept their original hair because a ponytail would break their themes.

The detail that closes the loop sits in the 3D art section:

> "Storm Dragon Lee Sin's model was a lot more recent, so there wasn't as much of a need for a big change but you'll notice he's now rocking his beautiful ponytail."

The same skin whose ponytail was cut in 2021 for clarity reasons got it back in 2024, now as part of a redesigned base silhouette rather than an obstacle to readability. This is not a reversal. The 2021 cut removed a static, hard-to-read feature from one skin; the 2024 update rebuilt the feature as a dynamic identification cue across the whole champion. What the record shows is a documented sequence: a skin constraint exposed a base-model problem, and the base model was redesigned to fix it.

## Still being articulated in 2026

The principle was still being articulated by Riot's art leadership in 2026. In an [interview published by Sheep Esports on 10 April 2026](https://www.sheepesports.com/en/articles/creating-league-of-legends-skins-the-hidden-rules-shaping-champions-cosmetics-an-interview-with/en), Cecilia Ciocchetti asked Thomas Randby, Associate Art Director at Riot, how a skin keeps a character recognisable. He described "the visual identity of the character, which is always tantamount", with the test being that a player can look "at a glance" and know who they are seeing. His concrete example is the same kind of primary feature the 2021 article defined:

> "A good example is Kai'Sa with her cannons: the cannons are absolutely a must. It's not necessarily a must that we keep the length of her hair, but just making sure that those certain aspects of the silhouette that are really primary for gameplay are maintained."

Five years after the clarity article and nineteen after TF2's commentary, the distinction is unchanged: keep the outline that carries gameplay information, let the rest move. A single interview shows that a senior art director still describes the work this way; it does not establish that every team follows a single formal policy.

## What the record does and does not show

| Source | Date | Kind | What it supports |
| :--- | :--- | :--- | :--- |
| [TF2 developer commentary transcript](https://wiki.teamfortress.com/wiki/Well_developer_commentary/Transcript), "Functional Character Design" (Ariel Diaz) and "Lightwarp and Rimlight" (Jason Mitchell) | Shipped with the game, Oct 2007 | Primary, Valve-authored | The three-level read hierarchy, team palette, class silhouette, chest-level contrast, rim highlights protecting the outline |
| [NPAR 2007 paper](https://steamcdn-a.akamaihd.net/apps/valve/2007/NPAR07_IllustrativeRenderingInTeamFortress2.pdf), Mitchell / Francke / Eng | 2007 | Primary, Valve-authored | Reading the scene as a stated goal; the three illustrators; rim highlights instead of dark outlines |
| [GDC 2008 deck, *Stylization with a Purpose*](https://steamcdn-a.akamaihd.net/apps/valve/2008/GDC2008_StylizationWithAPurpose_TF2.pdf), 82 slides | 2008 | Primary, Valve-authored | The read hierarchy on slide 22; the visual history on slides 3–5 |
| [Game Developer, MIGS report](https://www.gamedeveloper.com/pc/migs-valve-s-mitchell-on-creating-i-left-4-dead-i-s-filmic-visual-style), Mathew Kumar | 19 Nov 2008 | Reported talk, retrospective | The failed realistic version; the three tiers in Mitchell's own words; desaturated backgrounds; the shader decision |
| [Riot, *Clarity in League*](https://www.leagueoflegends.com/en-gb/news/dev/clarity-in-league/), bananaband1t | 12 Mar 2021 (UTC) | Primary, Riot-authored | Silhouettes as the top recognition signal; the three vows; primary/secondary/tertiary; Lee Sin; facing direction |
| [Riot, *Ask Riot: Let's Talk Clarity*](https://www.leagueoflegends.com/en-gb/news/dev/ask-riot-let-s-talk-clarity/) | 9 Apr 2021 (UTC) | Primary, Riot-authored | The "who's-this-champ?" test; Lancer and Space Groove Blitzcrank; Storm Dragon Lee Sin's ponytail; standards solidified after 2017 |
| [Riot, */dev: Modernizing the Monk*](https://www.leagueoflegends.com/en-us/news/dev/dev-modernizing-the-monk/), The ASU Team | 8 Apr 2024 | Primary, Riot-authored | Lee Sin read as Ezreal; dynamic ponytail added to the base silhouette; Storm Dragon's ponytail restored; skins exempted |
| [Sheep Esports interview with Thomas Randby](https://www.sheepesports.com/en/articles/creating-league-of-legends-skins-the-hidden-rules-shaping-champions-cosmetics-an-interview-with/en), Cecilia Ciocchetti | 10 Apr 2026 | Primary interview | Riot art leadership still describing the principle in 2026; Kai'Sa's cannons as a primary feature |

Six limits are worth stating plainly.

One: there is no evidence of a line of influence between the two studios. Neither Riot article cites Valve, and nothing here suggests Riot borrowed the framework. Similar wording in similar documents is consistent with the same constraint — fast recognition in a multiplayer match — and that is all it establishes. "Valve invented silhouette design" would be as wrong as "Riot copied TF2"; the idea is older than both, and the MIGS report itself credits Leyendecker's commercial illustration.

Two: the frameworks are related, not identical. Valve's silhouette identifies a class after team colour; Riot's silhouette is the top-level identity anchor for a champion. The word "hierarchy" means a reading order at Valve and an attention budget at Riot.

Three: Valve's commentary and paper describe a finished style. They do not date the decision to abandon realism, and the MIGS anecdote is a recollection from a year after release. [Our TF2 article](/posts/why-team-fortress-2-stopped-looking-realistic.html/) sets out how thin the chronology is.

Four: Riot's articles are statements of studio policy and project rationale, not measurements of whether the policy works. The Blitzcrank, Lee Sin and ASU examples show decisions being made; they do not show player reaction times or win rates. The 2024 post explains why the team made a change, not what the measured effect was.

Five: the MIGS piece is a reporter's account of a talk, not a transcript. Its quotations are as published by Game Developer, not audio we have checked.

Six: a [GameSpy report of a GDC session on TF2's art direction](http://pc.gamespy.com/pc/team-fortress-2/855121p1.html) describes the same read hierarchy and the same three illustrators, but the page could not be opened during research. It was visible only as a search excerpt, so nothing in this article is taken from it. Valve's own commentary covers the same ground more directly.

## Where this sits beside the other case files

The [art-direction case files](/series/art-direction-changes/) are about games that changed how they looked and what each studio left behind as evidence. This page is about something slightly different: not a makeover, but two related sets of rules that a makeover and a catalogue of cosmetics had to obey.

It also explains why the TF2 and Borderlands records read so differently. [Borderlands](/posts/borderlands-11th-hour-art-change.html/) has a dated decision, a development timeline and a percentage of completion. TF2 has a specification. The comparison is set out in [TF2, Borderlands and the evidence behind an art makeover](/posts/tf2-borderlands-before-the-makeover.html/): one record lets you reconstruct a sequence of events, the other lets you reconstruct an argument. The developer commentary quoted at the top of this page is the clearest surviving piece of that argument.

---

### Sources

Checked 11 November 2026. The TF2 developer commentary transcript, both 2021 Riot developer articles, the 2024 ASU article, the Game Developer MIGS report, the Sheep Esports interview and the NPAR 2007 paper were opened and read in full. The GDC 2008 slide deck was downloaded from Valve's Steam CDN and read in full for [the earlier TF2 article](/posts/why-team-fortress-2-stopped-looking-realistic.html/).

Dates are given in UTC, taken from each Riot page's `datePublished` metadata: `2021-03-12T16:00:00.000Z` for *Clarity in League* and `2021-04-09T18:00:00.000Z` for *Ask Riot*. The en-gb article pages display `13/03/2021` and `09/04/2021` respectively, so a one-day difference from the UK-facing display date is expected for the first article.

- [Official TF2 Wiki: Well developer commentary / Transcript](https://wiki.teamfortress.com/wiki/Well_developer_commentary/Transcript) — "Functional Character Design" (Ariel Diaz), "Lightwarp and Rimlight" (Jason Mitchell), with links to the original audio nodes.
- [NPAR 2007: Illustrative Rendering in Team Fortress 2 (PDF)](https://steamcdn-a.akamaihd.net/apps/valve/2007/NPAR07_IllustrativeRenderingInTeamFortress2.pdf) — Jason Mitchell, Moby Francke, Dhabih Eng, Valve.
- [Valve, GDC 2008: Stylization with a Purpose (PDF, 82 slides)](https://steamcdn-a.akamaihd.net/apps/valve/2008/GDC2008_StylizationWithAPurpose_TF2.pdf) — Jason Mitchell.
- [Game Developer, 19 Nov 2008: MIGS — Valve's Mitchell On Creating Left 4 Dead's 'Filmic' Visual Style](https://www.gamedeveloper.com/pc/migs-valve-s-mitchell-on-creating-i-left-4-dead-i-s-filmic-visual-style) — Mathew Kumar.
- [Riot Games, 12 Mar 2021: Clarity in League](https://www.leagueoflegends.com/en-gb/news/dev/clarity-in-league/) — bananaband1t.
- [Riot Games, 9 Apr 2021: Ask Riot: Let's Talk Clarity](https://www.leagueoflegends.com/en-gb/news/dev/ask-riot-let-s-talk-clarity/) — Meddler, MechaHawk, OCRAM818, Riot Bellissimoh, Riot Zimberfly.
- [Riot Games, 8 Apr 2024: /dev: Modernizing the Monk](https://www.leagueoflegends.com/en-us/news/dev/dev-modernizing-the-monk/) — The ASU Team.
- [Sheep Esports, 10 Apr 2026: Creating League of Legends' skins, an interview with Riot's Associate Art Director](https://www.sheepesports.com/en/articles/creating-league-of-legends-skins-the-hidden-rules-shaping-champions-cosmetics-an-interview-with/en) — Cecilia Ciocchetti, with Thomas Randby.
- [GameSpy: The Artistic Stylings of Team Fortress 2](http://pc.gamespy.com/pc/team-fortress-2/855121p1.html) — cited only as a note; the page could not be opened and nothing in this article is taken from it.

*Cover illustration: AI-generated for this article on 11 November 2026. The generator's on-image label was removed by cropping so the artwork can run at full width; the AI disclosure is kept here instead. It is an abstract arrangement of shapes — no game assets, logos, lettering or brand marks appear in it. The two in-article diagrams are original drawings made for this article with plain geometric shapes; they are neither AI-generated nor reproductions of any game asset. Quotations from Riot's developer articles are cited inline with links to the originals.*
