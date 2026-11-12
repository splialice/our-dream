---
title: "What Is Cel Shading?"
slug: what-is-cel-shading
date: 2026-11-12T11:38:25+08:00
lastmod: 2026-11-12T11:56:07+08:00
draft: false
author: "Pixel Dango"
description: "Cel shading is a rendering technique, not an art style. What the term originally meant, when the meaning drifted, and why Gearbox publicly rejected the label in 2009."
summary: "A technique with two meanings, four dated games, and one studio that said no to the word on the record."
tags: ["Cel shading", "Toon shading", "Borderlands", "Non-photorealistic rendering", "Game art direction"]
categories: ["Game history"]
cover: "/img/covers/what-is-cel-shading.webp"
comments: true
---

Cel shading, often referred to as toon shading, is a form of non-photorealistic rendering (NPR) that makes 3D objects appear to have the flat, stepped shading associated with traditional animation. It does this by replacing smooth lighting gradients with discrete bands of colour. Outlines are often added to reinforce the cartoon look, but they are a separate rendering technique — not an essential part of cel shading itself. The name comes from the celluloid *cels* painted on for traditional 2D animation.

## What the shader does

A cel shader starts with an ordinary 3D model and quantizes per-pixel lighting into a small number of discrete shades, so shadows and highlights become blocks of colour. The ink outline is a separate step: it can be drawn by rendering an enlarged, inverted-back-face silhouette, or by edge-detecting the depth and surface-normal buffers. Because the two usually ship together, the word drifted. As [Wikipedia notes](https://en.wikipedia.org/wiki/Cel_shading):

> The term "cel-shading" is popularly used to refer to the application of this "ink" outlining process in animation and games, although originally the term referred to the flat shading technique regardless of whether the outline was applied.

## A short history in four games

| Game | Year | Why it matters |
| :--- | :--- | :--- |
| Jet Set Radio | 2000 | One of the earliest commercial 3D games to draw press attention for cel shading |
| Cel Damage | 2001 | Comic-book visuals applied to a competitive driving game |
| The Wind Waker | 2002 | Linked stylized rendering to how clearly game information reads |
| Ōkami | 2006 | Brought Japanese ink-painting traditions into real-time 3D |

Jet Set Radio was shown at the 1999 Tokyo Game Show and released for the Dreamcast in 2000; the reveal and the release are not the same date. It is often called the first cel-shaded game, and that claim is not made here.

The strongest document in this group is Nintendo's. Satoru Takizawa told *Iwata Asks* that the style let the team "represent the mechanisms and objects for puzzles ... in a more easy-to-understand way", while photorealistic graphics would have "had the adverse effect of making information difficult to represent game-wise". His point was that players could no longer tell which objects could be moved or used. The shader was a readability decision, not just a look.

## The Label Gearbox Rejected

A rendering technique and a studio's own name for its work are not the same thing. On 9 April 2009 Randy Pitchford answered an email question with:

> "No, Borderlands is not cel-shaded — it's a gritty and serious world after all."

Five days later Gearbox said it had no settled name for the new look, adopted `Concept Art Style` for itself, and added "You can use whatever term you like." It did not ask anyone else to stop saying cel-shaded. On 16 April, two days after that report, [Destructoid quoted Gearbox](https://www.destructoid.com?p=44099/) explaining what it had actually built:

> "The new technique uses hand-drawn textures, scanned in and colored in Photoshop, combined with software that draws graphic novel-style outlines around characters and objects, sharpens shadows to look more like something an artist might create, and even draws lines on hills and inclines."
>
> "Finally the character models were all revamped with more exaggerated proportions, creating the appearance of a detailed comic book in motion."

That is a rendering pipeline, not a single toon shader — which is why the studio resisted the label. A slide from Brian Martel's GDC 2010 presentation labels two versions of one character model "FAKE CEL SHADING" and "BORDERLANDS SHADING (Concept Art Style)".

## So which word should you use?

If you are describing the renderer, cel shading is a legitimate technical term. If you are quoting the studio, use `Concept Art Style`. One names a technique; the other names a decision about how a game should look.

---

Checked 12 November 2026. The 9 and 14 April quotations were verified against the original Kotaku articles on 10 November 2026; the 14 April item verifies Kotaku's transcription of a Gearbox forum statement, not the original forum page. The 16 April description is quoted from James Stephanie Sterling's Destructoid report of 16 April 2009; Gearbox's original release was not independently checked. The 1999 Tokyo Game Show reveal (TGS '99 Autumn ran 17–19 September 1999, per Sega Retro) and the 2000 release are separate events. The GDC slide is reproduced in [How Borderlands Changed Its Art Style at 75 Percent Complete](/posts/borderlands-11th-hour-art-change.html/).

Further reading: [Wikipedia, "Cel shading"](https://en.wikipedia.org/wiki/Cel_shading) — used here only for the term's drift, not as the technical definition.

See also [Is Borderlands Cel Shaded?](/posts/is-borderlands-cel-shaded.html/), [What Is the Borderlands Art Style Called?](/posts/borderlands-art-style.html/) and [Why Game Characters Need Distinct Silhouettes](/posts/why-game-characters-need-distinct-silhouettes.html/).

*Cover illustration: AI-generated with Doubao. The three panels show the same object under smooth lighting, quantized shading without outlines, and quantized shading with ink outlines.*
