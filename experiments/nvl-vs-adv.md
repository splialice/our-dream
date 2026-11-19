---
title: "NVL vs ADV: Two Common Visual Novel Text Layouts"
slug: "nvl-vs-adv"
date: 2026-11-19
---

## Short answer

**ADV** and **NVL** are two common text layouts, not two genres. ADV presents one dialogue or narration unit at a time, usually in a window at the bottom of the screen. NVL shows several units at once in a window that covers most or all of the screen. A game can use both; Ren'Py's documentation explicitly describes mixing the two modes.

## The two layouts

Ren'Py's official NVL-Mode Tutorial gives the clearest definition available in the sources reviewed:

> "There are two main styles of presentation used for visual novels. ADV-style games present dialogue and narration one line at a time, generally in a window at the bottom of the screen. NVL-style games present multiple lines on the screen at a time, in a window that takes up the entire screen."

A caution about wording: "one line at a time" here means one **dialogue or narration unit** at a time, not one physical line of text on screen. A long unit can wrap across two or three visible lines inside an ADV box; it still advances as one unit when the player clicks.

Wikipedia's visual novel article gives the short-form expansion and the same visual rule: "The two most common textbox formats are ADV (short for 'Adventure'), in which the box occupies only a part of the screen, and NVL ('Novel') in which the textbox fills almost the whole screen or the whole screen."

| Layout | What the player sees | Common shorthand |
| :--- | :--- | :--- |
| ADV | One dialogue or narration unit at a time, usually in a bottom text box; the text itself may wrap | Adventure |
| NVL | Several stacked units, usually across most of the screen | Novel |

## Visual examples

These are schematic diagrams showing the layout logic, not screenshots from a specific game.

![ADV-style schematic](/img/diagrams/adv-layout-schematic.png)

*ADV-style: a bottom window advances one dialogue or narration unit at a time. Long units may wrap inside the window.*

![NVL-style schematic](/img/diagrams/nvl-layout-schematic.png)

*NVL-style: a large window keeps multiple units stacked on screen at once.*

## Where the labels come from

The sources reviewed support only a narrow origin: ADV is short for "Adventure"; NVL is short for "Novel." They do not establish who first used the abbreviations or exactly when the distinction became standard in Japanese visual novel development. Community threads discuss the origin, but they are not used here as authority.

That limitation is important. These are practical terms used by engine documentation, players and stores to describe text presentation. They are not a formal genre taxonomy agreed by every developer.

## Can a game use both?

Yes. Ren'Py is explicit about this. Its docs say an alternate NVL menu exists and that it is "useful when mixing NVL-mode and ADV-mode menus in a single game." They also describe `nvl show` and `nvl hide` commands that "can be used in games that use a mix of NVL-mode and ADV-mode windows."

So if you see a game described as "ADV with NVL sections," that is not a contradiction. It means the presentation changes by scene, route or menu context.

## Why players notice

The difference changes reading rhythm. ADV keeps a character scene visible while one line appears at a time. NVL gives narration and dialogue more page-like density, which is why it is often associated with expository or literary passages. These are consequences of the layout definitions above, not claims that one format is better.

This article is the **presentation** guide in a three-part mini-series: [Visual Novel vs Dating Sim](/posts/visual-novel-vs-dating-sim.html/) covers genre and mechanics, and [What Is a Kinetic Novel?](/posts/kinetic-novel-meaning.html/) covers story structure.

## Sources and evidence limits

- [NVL-Mode Tutorial — Ren'Py Documentation](https://www.renpy.org/doc/html/nvl_mode.html), Ren'Py 8.6.2 docs. First-party engine documentation. Used for the ADV/NVL definitions and the statements about mixing modes. No publication date shown.
- [Visual novel — Wikipedia](https://en.wikipedia.org/wiki/Visual_novel), last edited 28 October 2026. Secondary reference used for the "Adventure" / "Novel" expansions and the same textbox distinction.

Evidence limits: this article does not trace the first coinage of ADV or NVL. It also does not evaluate specific games' layouts unless supported by the two sources above. The focus is the current documented meaning.

Checked 19 November 2026.
