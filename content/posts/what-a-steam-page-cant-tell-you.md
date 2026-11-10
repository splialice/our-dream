---
title: "What a Steam page can't tell you"
slug: what-a-steam-page-cant-tell-you
date: 2026-11-10T09:40:00+08:00
lastmod: 2026-11-10T09:40:00+08:00
draft: false
author: "Pixel Dango"
description: "A store page is a dated snapshot of metadata, not a development record. Six Steam apps checked against the public appdetails endpoint, and what those fields can and cannot prove."
summary: "Reading Steam appdetails as a historical document, and why a live storefront cannot prove two games share a development history."
tags: ["Steam", "Steam API", "Borderlands"]
categories: ["Technical notes"]
cover: "/img/covers/what-a-steam-page-cant-tell-you.webp"
comments: true
---

A Steam store page is one of the more durable objects in games. It can sit there, unchanged, long after the thing it describes has shipped under another name, been cancelled, or quietly disappeared. That makes it a tempting source for game history. It is also easy to overread.

The page is a record of what Steam was serving on the day you looked at it. It is not a record of what happened inside a studio.

## The check

Steam exposes a public JSON endpoint for store metadata. I could not find public documentation of its field semantics during research, so the descriptions below are observed behaviour, not official definitions. Here is the request for one AppID, run on 9 November 2026:

```powershell
$id = '3334540'
$u  = "https://store.steampowered.com/api/appdetails?appids=$id&l=english&cc=us"
$r  = Invoke-WebRequest -Uri $u -UseBasicParsing
($r.Content | ConvertFrom-Json).$id.data |
    Select-Object name, type, developers, publishers, release_date
```

The endpoint takes one AppID at a time; a request containing several IDs returned 400. The other five rows below come from the same request repeated with `$id` changed, using the same `l=english&cc=us` parameters on the same day. This snippet is a reproducible example, not a script that produces the whole table.

Six apps, queried through the same endpoint with the same parameters, on the same day:

| AppID | name | `coming_soon` | `date` | developers | publishers |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 3334540 | Deepspace Emporium | `true` | `2026` | Questing Goose Studio | Questing Goose Studio |
| 4348910 | Probably Stolen - Cyberpunk Shopkeeper Sim | `false` | `Oct 28, 2026` | Questing Goose Studio | tinyBuild |
| 3469870 | *(no data)* | — | — | — | — |
| 440 | Team Fortress 2 | `false` | `Oct 10, 2007` | Valve | — |
| 10 | Counter-Strike | `false` | `Nov 1, 2000` | Valve | — |
| 8980 | Borderlands Game of the Year | `false` | `Aug 31, 2023` | Gearbox Software | — |

Checked 9 November 2026. The `release_date.date` value is a string, not a typed date; `2026` means a planned year, not a promise.

## Three shapes of a page

**Unreleased but alive.** `Deepspace Emporium` (3334540) still returns `coming_soon: true` and a planned 2026 release. Its store page says "This game is not yet available on Steam" and has no user reviews. It also carries a leftover line — "This is the demo version of the game and does not include Save and Loading" — which suggests demo copy was carried over. That is an observation about the text, not proof of how the page was assembled or maintained.

**Shipped.** `Probably Stolen` (4348910) returns `coming_soon: false`, a full date, the same developer and a different publisher. Both fields are current metadata. Neither says when the publisher came on board.

**No data.** The old demo's ID (3469870) returns `success: false`, and its store URL now resolves to Steam's home page. It would be easy to write "the demo has been delisted". The response does not identify why the data is missing. Region restrictions, access controls and configuration changes are all possible, and would need separate investigation. All that is defensible is: as of 9 November 2026, this ID returns no product data and its URL no longer resolves to a product page.

The fourth row is the trap. App 8980 is listed as *Borderlands Game of the Year* and reports `Aug 31, 2023`. 2K's own site gives 20 October 2009 for the original Borderlands — specifically the North American console release, with PC versions following later that month. What this row shows is that the date on a current listing need not equal the underlying game's first release date. It does not, on its own, prove that the package was renamed, re-bundled or re-dated, and I have not found evidence here for any of those three actions.

## What the fields cannot carry

The two pages that matter for [the recent `Probably Stolen` story](/posts/probably-stolen-28-player-demo.html/) are 3334540 and 4348910. Their descriptions outline much the same loop: a former scavenger with a loan, a shop on the Lower Levels, goods of questionable legality, rising rent, factions watching. The developer field is identical. It is tempting to stop there and call one the renamed version of the other.

None of those fields establishes it. `developers` records a credit, not a team's continuity. `name` records a label, not a decision. Similar prose records similar prose. A store page cannot tell you whether code, assets or design documents carried over, who made the call to change the name, or why an earlier demo vanished. That gap is why reporting on the 2026 game has to say things like "Rock Paper Shotgun identified the earlier game as..." instead of "the game became...".

The same limit applies in reverse. A page that says "coming in 2026" does not tell you the project is alive. A page that returns no data does not tell you it is dead. A page with no reviews does not tell you nobody played it — a demo can have a very low peak-concurrency figure and still leave dozens of positive reviews.

## Keeping the record honestly

Treat each check as a dated observation:

- Record the AppID, the fields you used, and `last_checked`. Quote the API response, not a screenshot of the store.
- When a row dies, mark it `no data` and keep the row. Which links have stopped working is itself part of the archive.
- Note the failure mode. 403, 404 and `success: false` are different outcomes, and none of them is a verdict about the game.
- Expect link rot. The original Valve-hosted PDF for `Illustrative Rendering in Team Fortress 2` now returns 404, while the paper survives through its DOI and an official transcript; [the development-history note](/posts/tf2-borderlands-before-the-makeover.html/) leans on that distinction. A citation that worked in 2007 may not resolve in 2026.

The practical habit is small but changes what you can claim later: append the date to every number, and separate "the page said" from "the studio did". A storefront is excellent evidence of the first. It is very weak evidence of the second.

---

### Sources

Checked 9–10 November 2026.

- [Steam appdetails endpoint](https://store.steampowered.com/api/appdetails?appids=3334540&l=english&cc=us) — public JSON, one AppID per request; field meanings above are observed behaviour, not official documentation.
- [Steam: Deepspace Emporium (3334540)](https://store.steampowered.com/app/3334540/) — unreleased page and its leftover demo copy.
- [Steam: Probably Stolen (4348910)](https://store.steampowered.com/app/4348910/) — release date, developer and publisher.
- [2K: Borderlands](https://borderlands.2k.com/zh-CN/borderlands/) — 20 Oct 2009, the North American console release; PC versions followed later that month, contrasted with the GOTY listing.
- [Official TF2 Wiki: Illustrative Rendering in Team Fortress 2](https://wiki.teamfortress.com/wiki/Illustrative_Rendering_in_Team_Fortress_2) — example of a surviving transcript.
- [Rock Paper Shotgun, 4 Nov 2026](https://www.rockpapershotgun.com/smash-hit-cyberpunk-storekeeper-probably-stolen-was-originally-a-different-non-cyberpunk-game-that-seemed-destined-to-sink-without-trace/) — the identification of the earlier game.

*Cover illustration: AI-generated. Generated text embedded in the image was removed by cropping so the artwork can run at full width; the AI disclosure is kept here instead.*
