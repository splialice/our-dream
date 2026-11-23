---
title: "What Is Cel Shading? A Guide to the Technique, Its Limits, and Borderlands"
slug: what-is-cel-shading
date: 2026-11-12T11:38:25+08:00
lastmod: 2026-11-18T10:00:00+08:00
draft: false
author: "Pixel Dango"
description: "Cel shading is a rendering technique, not an art style. Learn how it works, why outlines are separate, and why Gearbox and Valve rejected the label."
summary: "A technique with two meanings, five dated reference points, and two studios that argued about the word on the record."
tags: ["Cel shading", "Toon shading", "Borderlands", "Non-photorealistic rendering", "Game art direction"]
categories: ["Game design"]
cover: "/img/covers/what-is-cel-shading.webp"
comments: true
---

Cel shading, often called toon shading, is a form of non-photorealistic rendering that makes 3D objects look as if they were painted with the flat, stepped colours of traditional animation. It does this by replacing smooth lighting gradients with a small number of discrete bands. Ink outlines are often added to complete the cartoon look, but they are a separate rendering step, not part of the shader itself. The name comes from the celluloid *cels* used in hand-drawn animation.

That distinction — between what the shader does and what the finished picture looks like — explains most of the arguments about the word. This guide separates the two, then shows how one studio, Gearbox, handled the label in 2009.

## What the shader actually does

Start with an ordinary lit 3D model. A renderer normally calculates a smooth value for how much light reaches each pixel, producing a continuous gradient from highlight to shadow. A cel shader takes that same value and quantizes it: anything in one range becomes colour A, the next range colour B, and so on. The result is a handful of flat bands instead of a gradient.

That is the core operation of cel shading: it changes how lighting values are mapped to visible colours. It does not, by itself, prescribe the model design, texture style, or broader art direction.

The black ink outline popularly associated with the look is normally produced by a different pass:

- render an enlarged, inverted-back-face copy of the mesh so only the silhouette shows; or
- detect edges from the depth and surface-normal buffers after the main render.

Because the two passes are usually shipped together, the word drifted. [Wikipedia's entry](https://en.wikipedia.org/wiki/Cel_shading) records that drift explicitly:

> The term "cel-shading" is popularly used to refer to the application of this "ink" outlining process in animation and games, although originally the term referred to the flat shading technique regardless of whether the outline was applied.

Wikipedia is used here only for the history of the label, not as the technical definition.

## Is cel shading the same as toon shading?

In practice the two names are used interchangeably, and this site uses them that way. If a distinction is being drawn, *toon shading* leans towards the whole cartoon presentation — flat bands, outlines, exaggerated colour — while *cel shading* names the stepped-lighting render more narrowly. There is no standards body that enforces one meaning over the other.

What matters more than the choice between those two words is the boundary on the other side: a **rendering technique** is not the same thing as an **art direction**. Cel shading describes how lighting is rendered. An art direction is the decision about what a game should look like, and it can be reached with a mix of shaders, hand-painted textures, model work, lighting choices and post-processing. Asking "is this game cel shaded?" can therefore get a technically honest yes and a studio-level no at the same time.

## Does cel shading need outlines?

No. Stepped lighting works without any outline pass at all, and outline passes can be applied to renders that are not cel shaded. They are two tools that happen to ship together because the combination reads as "cartoon" very quickly.

This is why a visual classification and a technical audit can disagree. A game can look like the popular idea of cel shading while its renderer does something else, and a renderer can use stepped lighting as one ingredient in a look the studio names differently.

## A short history in five reference points

| Game | Year | Why it matters | Source |
| :--- | :--- | :--- | :--- |
| Jet Set Radio | 2000 | One of the earliest commercial 3D games to draw press attention for cel shading | [Sega Retro](https://segaretro.org/Jet_Set_Radio) |
| Cel Damage | 2001 | Comic-book visuals applied to a competitive driving game | [Wikipedia](https://en.wikipedia.org/wiki/Cel_Damage) |
| The Wind Waker | 2002 | Linked stylized rendering to how clearly game information reads | [Iwata Asks](https://iwataasks.nintendo.com/interviews/wiiu/wind-waker/0/0/) (retrospective) |
| Ōkami | 2006 | Brought Japanese ink-painting traditions into real-time 3D | [Wikipedia](https://en.wikipedia.org/wiki/%C5%8Ckami) |
| Team Fortress 2 | 2007 | Valve called the approach illustrative rendering, used rim highlights instead of dark outlines, and rejected the cel-shaded route | [NPAR 2007 paper](https://steamcdn-a.akamaihd.net/apps/valve/2007/NPAR07_IllustrativeRenderingInTeamFortress2.pdf) |

Jet Set Radio was shown at the 1999 Tokyo Game Show and released for the Dreamcast in 2000; the reveal and the release are not the same date. Both appear in [Sega Retro's record](https://segaretro.org/Jet_Set_Radio). It is often called the first cel-shaded game, and that claim is not made here.

A particularly clear retrospective explanation comes from Nintendo's [*Iwata Asks* interview on *The Wind Waker HD*](https://iwataasks.nintendo.com/interviews/wiiu/wind-waker/0/0/). Satoru Takizawa said the style let the team "represent the mechanisms and objects for puzzles ... in a more easy-to-understand way", while photorealistic graphics would have "had the adverse effect of making information difficult to represent game-wise". His point was that players could no longer tell which objects could be moved or used. This is a developer looking back on the decision, not a document from 2002 — but it is first-party, and it makes the readability argument plainly. In that case the shader was a readability decision, not just a look.

## Why Borderlands is often called cel shaded — and why that label needs qualification

Borderlands is the most common example of the technique-versus-art-direction problem, and the studio left an unusually dated paper trail.

On 9 April 2009, before release, Randy Pitchford answered an email question, [published by Kotaku](https://kotaku.com/gearbox-borderlands-is-not-cel-shaded-5206042), with:

> "No, Borderlands is not cel-shaded — it's a gritty and serious world after all."

Five days later, [Kotaku transcribed a statement posted on Gearbox's official forums](https://kotaku.com/gearbox-explain-cel-shaded-borderlands-5210855). The studio said it did not know what to call the result, invited readers to use whatever term they liked, and explained that Gearbox had chosen `Concept Art Style` as its own name for the approach. It did not ask anyone else to stop saying cel-shaded. That 14 April item is Kotaku's transcription of a forum statement, not an archived copy of the original post. On 16 April, [Destructoid reported Gearbox's explanation](https://www.destructoid.com/borderlands-explains-its-not-cel-shaded-actually-art-style/) of what it had actually built:

> "The new technique uses hand-drawn textures, scanned in and colored in Photoshop, combined with software that draws graphic novel-style outlines around characters and objects, sharpens shadows to look more like something an artist might create, and even draws lines on hills and inclines."
>
> "Finally the character models were all revamped with more exaggerated proportions, creating the appearance of a detailed comic book in motion."

That is a rendering pipeline made of several parts, not one toon shader — which is the basis for the studio's objection. A slide from Brian Martel's GDC 2010 presentation, [preserved as a PDF by GDC Vault](https://media.gdcvault.com/gdc10/slides/Martel_Brian_Borderlands_and_the_11th_Hour_Art_Change.pdf), labels two versions of one character model "FAKE CEL SHADING" and "BORDERLANDS SHADING (Concept Art Style)"; it is also reproduced in [How Borderlands Changed Its Art Style at 75 Percent Complete](/posts/borderlands-11th-hour-art-change.html/).

The boundary that matters: the 9 April quote is a denial of a **label**, not a technical audit of the shipped renderer. It tells us how Gearbox named and defended its work in 2009. It does not, on its own, prove that no part of the final game resembles cel shading.

For the short yes-or-no answer with all four dated 2009 sources, see [Is Borderlands Cel Shaded?](/posts/is-borderlands-cel-shaded.html/). For what the studio actually called the look, see [What Is the Borderlands Art Style Called?](/posts/borderlands-art-style.html/). For the wider evidence comparison with Team Fortress 2, see [TF2, Borderlands and the evidence behind an art makeover](/posts/tf2-borderlands-before-the-makeover.html/).

## Team Fortress 2: the other false friend

TF2 is often pulled into the same argument because it has bold shapes and readable shadows, but Valve's own account points in a different direction. The 2007 NPAR paper calls the approach *Illustrative Rendering in Team Fortress 2*, names early 20th-century commercial illustrators as references, and records the rule: "Silhouettes are often emphasized with rim highlights rather than dark outlines." A 2008 report of Moby Francke's Gamefest talk is blunter: "We didn't want to go the cel-shaded route, we wanted to go more true to the way that lighting occurs."

That is the same distinction as Borderlands, with different evidence. Gearbox described hand-drawn textures plus graphic-novel outlines and chose `Concept Art Style`; Valve described illustrative shading with rim highlights and warm-to-cool hue shifts. Neither statement is a technical audit of every shader in the game. Both tell you what the studios said they were building. The dedicated [Team Fortress 2 art style](/posts/tf2-art-style.html/) article lays out the full paper trail.

## Frequently asked questions

**What is cel shading in simple terms?**
It is a way of lighting a 3D model so the shadows appear as flat bands of colour instead of smooth gradients, like a hand-drawn cartoon.

**Is cel shading the same as toon shading?**
In everyday use, yes. The two names are used interchangeably. If a writer distinguishes them, *toon shading* usually means the whole cartoon presentation and *cel shading* the stepped-lighting render specifically.

**Does cel shading always need black outlines?**
No. Outlines are a separate rendering pass. Cel shading changes the lighting; the ink contour is an addition that often ships with it.

**Is cel shading an art style?**
It is a rendering technique. An art style or art direction is the broader decision about how a game looks, and can combine cel shading with hand-painted textures, outlines, exaggerated proportions and other choices.

**Why is Borderlands called cel shaded if Gearbox said no?**
The look reads as cel shaded to many viewers, but Gearbox used a different name, `Concept Art Style`, and described a multi-part pipeline. The visual shorthand and the studio's own label answer different questions. Both are documented in the section above.

**Is Team Fortress 2 cel shaded?**
Not by Valve's own account. The 2007 paper calls the approach illustrative rendering, and Moby Francke said in 2008 that the team did not want the cel-shaded route. Players still use the term as visual shorthand because the result reads as cartoon-like; the studio-level answer and the visual shorthand are different claims.

**Why does cel shading matter for readability?**
Flat bands of colour can separate interactive objects from the background more clearly than realistic lighting. Nintendo's *Iwata Asks* interview on The Wind Waker gives a concrete example: puzzle mechanisms became harder to read under photorealistic rendering.

## So which word should you use?

If you are describing the renderer, cel shading is a legitimate technical term. If you are quoting the studio, use `Concept Art Style` and attribute it to Gearbox in April 2009. One names a technique; the other names a decision about how a game should look. Keep them apart and the apparent contradiction disappears.

For related art-direction questions, see [What Is the Team Fortress 2 Art Style?](/posts/tf2-art-style.html/), [Why Game Characters Need Distinct Silhouettes](/posts/why-game-characters-need-distinct-silhouettes.html/) and [Why Team Fortress 2 Stopped Looking Realistic](/posts/why-team-fortress-2-stopped-looking-realistic.html/).

---

Checked 12 November 2026; guide expanded 16 November and 18 November 2026. The 9 and 14 April quotations were verified against the original Kotaku articles on 10 November 2026; the 14 April item verifies Kotaku's transcription of a Gearbox forum statement, not the original forum page. The 16 April description is quoted from James Stephanie Sterling's Destructoid report of 16 April 2009; Gearbox's original release was not independently checked. The 1999 Tokyo Game Show reveal (TGS '99 Autumn ran 17–19 September 1999, per Sega Retro) and the 2000 release are separate events. The GDC slide is reproduced in [How Borderlands Changed Its Art Style at 75 Percent Complete](/posts/borderlands-11th-hour-art-change.html/).

Further reading: [Wikipedia, "Cel shading"](https://en.wikipedia.org/wiki/Cel_shading) — used here only for the term's drift, not as the technical definition.

*Cover: programmatically generated editorial graphic, 18 November 2026. The three stepped bands are a schematic motif, not a shader screenshot.*
