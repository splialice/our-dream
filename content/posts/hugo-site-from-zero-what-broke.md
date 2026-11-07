---
title: "Building a Hugo Site from Zero: What Actually Broke"
slug: hugo-site-from-zero-what-broke
date: 2026-11-07T10:00:00+08:00
lastmod: 2026-11-07T10:00:00+08:00
draft: false
description: "A real build log: theme setup, Cloudflare Pages, English interface conversion, and the five problems that cost me the most time. No theory, just what happened and how I fixed it."
summary: "I built this site over two days. Five things broke. Here is each one, why it broke, and the fix that actually worked."
tags: ["Hugo", "Cloudflare Pages", "build log", "troubleshooting"]
categories: ["Building this site"]
cover: "/img/covers/default.svg"
comments: true
---

This site was built in about two days. Not because I am fast, but because most of it is copying a theme and changing settings.

What took time was the part nobody writes down: the five things that broke, and why the obvious answer was wrong four times out of five.

This is the log.

## Starting point

I had three things: a domain, a Hugo theme called Demius, and a Cloudflare account. No plan beyond "put something up and see what breaks".

The theme repository is a full source repo, not a packaged theme. That distinction caused the first problem.

```bash
git clone https://github.com/splialice/our-dream.git
cd our-dream
hugo --gc
```

If this is the first command you run, it fails. Expect it.

## Problem 1: POSTCSS binary not found

```
Error building site: POSTCSS: failed to transform "/css/main.css" (text/css).
You need to install PostCSS.
binary with name "postcss" not found in PATH
```

The important half is the last line. It is not a version conflict, not a theme bug. Hugo is trying to run a command called `postcss`, and that command does not exist on this machine.

Why this theme needs it: `assets/css/` contains 76 separate stylesheets, chained through `@import`, merged into 5 output files by a plugin called `postcss-import`. The templates call `resources.PostCSS` in six places.

`postcss` is an npm package. It is not part of Hugo.

The fix is one command locally:

```bash
npm install
```

But this same failure appears again on Cloudflare, and there the fix has to be written into the build configuration, not run by hand. That is Problem 2.

What I got wrong: I searched the error first and found answers recommending `NODE_VERSION=16`, or installing postcss globally, or switching to Hugo extended. All three are real requirements. None of them is the actual fix. Locally I already had Node 22 and Hugo extended, and it still failed, because `npm install` had never been run in the project directory.

## Problem 2: Cloudflare Pages, and where it hides

Two separate annoyances here.

**The build fails the same way.** Cloudflare Pages does not keep `node_modules` between builds. Each build starts from a clean container. Your `package.json` is in the repo, but the dependencies are not installed unless you tell it to install them.

The build command must be:

```
npm install && hugo --gc --minify
```

Not `hugo`, not `hugo --minify`. The `npm install &&` is not optional, no matter how obvious it looks after the fact.

And it is worth pinning the Hugo version, because the build image ships its own:

```
HUGO_VERSION = 0.167.0
```

Hugo deprecated a batch of config keys around 0.158 (`languageCode` → `locale`, among others). If the image updates and you have not pinned, a site that built fine last month starts throwing deprecation errors.

**The entry point is genuinely hard to find.** In the current Cloudflare dashboard, Pages is no longer a top-level product. You go to:

```
Compute → Workers & Pages → Create → (scroll to the bottom) "Continue to Pages"
```

Workers is presented as the primary path. Pages is labelled a legacy workflow, which is accurate: Cloudflare is folding Pages into Workers. If you follow any tutorial written before 2026, you will land on a Workers creation screen and see no Pages option, because there isn't one at the top anymore.

## Problem 3: baseURL and the trailing slash

This one produces no error message at all, which makes it the worst of the five.

```toml
baseURL = 'https://example.com'         # wrong
baseURL = 'https://yourdomain.com'      # also wrong
baseURL = 'https://yourdomain.com/'     # correct
```

Without the trailing slash, Hugo concatenates paths into nonsense like `https://yourdomain.comcss/main.css`. The site loads, the HTML is there, and every stylesheet request 404s. Hugo reports success the whole time.

I spent a while looking at the network tab before realising the URL itself was malformed.

## Problem 4: I broke the homepage by overriding a template

This one is my fault, and it is the most instructive of the five.

I added `layouts/index.html` to translate the homepage heading. Hugo's template lookup order puts the project's `layouts/` above the theme's, so my file did what I wanted.

It also replaced the theme's entire homepage. The theme's real homepage is `_default/index.html`, which dispatches to one of three layout engines (`partials/main/engine-1.html`, `engine-2`, `engine-3`) depending on `homeColumns`. My file had none of that logic. It was an older, simpler structure.

Result: the homepage rendered with zero article cards. The build succeeded. Nothing warned me.

The lesson is not "don't override templates". Overriding is the correct way to modify a theme without editing the theme itself. The lesson is:

**Before copying a template to override it, find out which template is actually rendering the thing you want to change.**

Two ways to check:

```bash
# What does the theme actually have?
find themes/demius/layouts -name "index.html"

# What is the lookup order Hugo is using?
hugo --printPathWarnings
```

`layouts/index.html` and `layouts/_default/index.html` both look like "the homepage". Only one of them is being used.

## Problem 5: Content that lives inside the theme

I deleted two demo posts and the homepage went from three cards to one. Then I noticed a third post still rendering, a Chinese guide to configuring the theme.

It was not in `content/`. It was in `themes/demius/content/posts/theme-configuration-guide.md`.

Hugo merges `themes/<name>/content/` into your site content. Files in your project take priority, but anything without a same-named counterpart gets built as a page.

This is why I could not find the source by searching `content/`:

```bash
find themes/demius/content -type f
# themes/demius/content/_index.md
# themes/demius/content/about.md
# themes/demius/content/posts/theme-configuration-guide.md
```

Two ways to kill it. Either create a same-named file in your `content/` with `build.render: never`, or delete the file from the theme. I used the second, because a repo full of disabled placeholder files is worse than editing a theme you are not going to update.

If you go that route, write down what you changed. The next time you pull a fresh theme, your deletions are gone.

## Two smaller things worth knowing

**Future dates do not build.** I set a post's date to `21:00` while the clock read `20:49`. Hugo skipped it silently. `hugo list all` showed the page as recognised, the build output did not contain it, and the page count did not change. The date was in the future by eleven minutes.

**`--minify` removes attribute quotes.** After minification, `<meta name="author" content="...">` becomes `<meta name=author content="...">`. If you are grepping the build output to verify a tag was rendered, a pattern with quotes in it will match nothing and you will think the tag is missing. It isn't.

## What I would do differently

Not much, but a few things:

1. **Run `hugo --gc` before touching any configuration.** Prove the theme builds clean first. If it does not, you are debugging two things at once.
2. **Fill in `baseURL` with the trailing slash immediately.** Do not wait until deploying.
3. **Check which template renders a page before overriding one.** One `find` command saves an hour.
4. **Search the theme's `content/` directory on day one.** Know what is being built that you did not write.
5. **Write the build command as `npm install && hugo --gc --minify` from the start.** Never type `hugo` alone in a CI field.

## Current state

Two days in:

- Site live on a custom domain, HTTPS working
- Theme interface converted to English, 13 templates overridden in `layouts/`
- 8 theme pages disabled, page count down from 56 to 29
- One real article published (this one is the second)

Still not done: the interface has leftover Chinese in sidebar widgets I have not reached yet, the About page is still the theme author's, and there are exactly two posts.

That last item is the only one that matters. Everything above is setup. A site with two posts is a site with two posts, no matter how clean the build log is.

---

*Environment: Hugo 0.167.0 extended, Node 22, Cloudflare Pages with Git-connected deploys. Everything above was reproduced on Windows 11 with Git Bash.*