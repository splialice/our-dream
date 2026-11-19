# Pixel Dango 站点交接说明

> 生成日期：2026-11-16  
> 仓库：`D:\web\our-dream-preview`（GitHub `splialice/our-dream`，分支 `main`）  
> 线上：https://pixeldango.com  
> 当前 HEAD：`a684457`（空提交，仅用于验证 Cloudflare 构建）

## 0. 一句话

Hugo（Demius 主题）+ Cloudflare Pages 的英文游戏史 / 技术笔记站。文章是 Git 里的 Markdown，推送到 `main` 自动构建；构建时会跑 `scripts/check_site.py`，SEO 或结构有问题会直接让部署失败。

## 1. 站点定位

`content/about.md` 写得很清楚，交接时先读它。核心是两类内容：

- **Game history**：一个主机、一种格式、一家工作室或一类游戏，为什么最后变成那样；重点是谁做了决定、当时看到了什么。
- **Technical notes**：建站过程中实际踩到的坑，写清真正原因和可复现的修法。

三条写作规则：

1. 来源具名；数字必须有出处，不确定就写不确定。
2. 两份材料冲突时，两边都写，不挑顺手的那个。
3. 发现错误就改，必要时标注更正。

明确不写：购买指南、Top 10 榜单、没有实际研究过的题目。宁可少发。

## 2. 仓库与线上

| 项 | 值 |
|---|---|
| 线上域名 | `https://pixeldango.com` |
| GitHub | `splialice/our-dream` |
| 生产分支 | `main` |
| 托管 | Cloudflare Pages，项目名 `our-dream` |
| Build command | `npm install && hugo --gc --minify && python3 scripts/check_site.py --public public` |
| Build output directory | `public` |
| Root directory | `/` |
| Build system | v3，Build cache 关闭 |
| Hugo | 本地 `0.167.0 extended`；Cloudflare 面板用 `HUGO_VERSION` 固定 |
| 统计 | GA4 `G-770Y4W7ZN4`，由 `layouts/_default/baseof.html` 手动输出 |
| 评论 | 关闭（`params.comment.enable = false`） |
| 搜索 | 本地索引，`/index.json` |

注意：Cloudflare 的 Build command 是面板设置，不在仓库里。改它要进 Cloudflare 面板，改完不会自动重新部署，需要下一次 push 或手动 Retry。

## 3. 本地跑起来

前置：Hugo extended 0.167+、Node.js、Python 3。

```powershell
cd D:\web\our-dream-preview
npm install

# 本地预览（含草稿）
hugo server -D

# 干净构建 + 全站检查（推荐，发布前必跑）
npm run build

# 只做独立构建检查，不碰正在预览的 public/
npm run check:site

# 构建 + 探测线上真实 HTTP 状态
npm run check:live
```

`npm run build` 会先 `hugo --cleanDestinationDir`，再跑 `check_site.py`，结果写到 `.seo-check/latest/`。该目录已被 `.gitignore` 忽略，不要提交。

`check:site` / `check:live` 会用独立临时目录构建，不影响你正在开的 `hugo server` 和 `public/`。

## 4. 目录地图

| 路径 | 作用 |
|---|---|
| `content/posts/` | 所有文章；文件名即 slug |
| `content/series/art-direction-changes.md` | 艺术风格系列页 |
| `content/about.md` | 站点定位与写作规则 |
| `content/links.md` | Resources 页，来源说明 |
| `content/questions.md` | Answers 页壳子，数据来自 `data/questions.yaml` |
| `data/questions.yaml` | Answers 的问答数据，手动维护 |
| `data/links.yaml` 等 | 主题页面数据；多个文件是主题示例，不一定在用 |
| `layouts/` | 项目层模板覆盖，优先改这里 |
| `layouts/partials/seo/` | canonical、OG、分页上下文、JSON-LD |
| `scripts/check_site.py` | 构建时 / 线上 SEO 与结构检查 |
| `scripts/merge-css.js` | CSS 合并辅助脚本，当前构建流程未直接调用 |
| `static/404.html` | Cloudflare Pages 顶层 404，必须保留 |
| `static/robots.txt` | 爬虫规则；显式放行搜索引擎，拦截训练爬虫 |
| `static/img/covers/` | 文章封面，WebP 为主 |
| `research/` | 每篇文章的来源归档，不发布 |
| `themes/demius/` | 主题源码，尽量不改 |
| `THEME_CHANGES.md` | 所有对主题的直接改动记录 |
| `.seo-check/` | 检查产物，已忽略，不要提交 |

## 5. 现有内容清单

正式发布 16 篇，另有 2 篇主题演示文不渲染。日期为 front matter 的 `date` 日期部分。

### Art direction / 视觉决策（7 篇）

- `borderlands-art-style.md` — What Is the Borderlands Art Style Called? — 2026-11-10 — `/posts/borderlands-art-style.html/`
- `is-borderlands-cel-shaded.md` — Is Borderlands Cel Shaded? — 2026-11-10 — `/posts/is-borderlands-cel-shaded.html/`
- `borderlands-11th-hour-art-change.md` — How Borderlands Changed Its Art Style at 75 Percent Complete — 2026-11-11 — `/posts/borderlands-11th-hour-art-change.html/`
- `tf2-borderlands-before-the-makeover.md` — TF2, Borderlands and the evidence behind an art makeover — 2026-11-10 — `/posts/tf2-borderlands-before-the-makeover.html/`
- `why-team-fortress-2-stopped-looking-realistic.md` — Why Team Fortress 2 Stopped Looking Realistic — 2026-11-11 — `/posts/why-team-fortress-2-stopped-looking-realistic.html/`
- `why-game-characters-need-distinct-silhouettes.md` — Why Game Characters Need Distinct Silhouettes — 2026-11-11 — `/posts/why-game-characters-need-distinct-silhouettes.html/`
- `what-is-cel-shading.md` — What Is Cel Shading? — 2026-11-12 — `/posts/what-is-cel-shading.html/`

系列页：`content/series/art-direction-changes.md` — `/series/art-direction-changes/`。目前 groups 只有 Borderlands 与 Team Fortress 2。

### Fake OS / 模拟界面（3 篇）

- `what-are-fake-os-games-called.md` — What Are Fake OS Games Called? — 2026-11-12 — `/posts/what-are-fake-os-games-called.html/`
- `why-roottrees-search-was-simple.md` — The Roottrees Are Dead: How a Game Jam Shortcut Became a Research Tool — 2026-11-12 — `/posts/why-roottrees-search-was-simple.html/`
- `why-hypnospace-outlaw-needed-zones.md` — Hypnospace Outlaw: Why a Fake Internet Needed Zones — 2026-11-14 — `/posts/why-hypnospace-outlaw-needed-zones.html/`

### Public record / 证据拆解（2 篇）

- `what-a-steam-page-cant-tell-you.md` — What a Steam page can't tell you — 2026-11-10 — `/posts/what-a-steam-page-cant-tell-you.html/`
- `probably-stolen-28-player-demo.md` — The 28-player demo and Probably Stolen — 2026-11-09 — `/posts/probably-stolen-28-player-demo.html/`

### Site building / 建站技术（3 篇）

- `hugo-site-from-zero-what-broke.md` — Building a Hugo Site from Zero: What Actually Broke — 2026-11-07 — `/posts/hugo-site-from-zero-what-broke.html/`
- `hugo-cloudflare-postcss-not-found.md` — Hugo 部署 Cloudflare 报 PostCSS not found — 2026-11-06 — `/posts/hugo-cloudflare-postcss-not-found.html/`
- `when-git-push-succeeds-and-nothing-ships.md` — When git push succeeds and nothing ships — 2026-11-08 — `/posts/when-git-push-succeeds-and-nothing-ships.html/`

### AI（1 篇）

- `agent-craze-cost-china.md` — Two Hundred Million Tokens Cost Me $2.25 — 2026-11-07 — `/posts/agent-craze-cost-china.html/`

### 不渲染的演示文（2 篇）

- `hello-demius.md` — 主题中文演示 — 2025-11-01 — `render: never`
- `immersive-reading-guide.md` — 沉浸模式演示 — 2025-11-05 — `render: never`，slug 是 `immersive-reading`

这两篇不是丢失，是故意留档。不要因为 sitemap 里没有就以为构建坏了。

## 6. 内容模型与新增文章

### front matter 模板

```yaml
---
title: "文章标题"
slug: "kebab-case-slug"
date: 2026-11-16T10:00:00+08:00
lastmod: 2026-11-16T10:00:00+08:00
draft: false
author: "Pixel Dango"
description: "一句话摘要，必须全站唯一，check_site 会查重。"
summary: "列表卡片用的短摘要。"
tags: ["Topic", "Studio"]
categories: ["Game history"]
cover: "/img/covers/<slug>.webp"
comments: true
---
```

字段注意：

- `date` 不能晚于当前时间。Hugo 对未来文章是静默跳过，不报错，只是不生成。
- `slug` 决定 URL；默认用文件名。已有文章不要随便改 slug，会断外链。
- 实际文章 URL 是 `/posts/<slug>.html/`，带 `.html` 和尾斜杠。站内链接也按这个写。
- `description` 必填且唯一；缺失或重复会让 `check_site.py` 失败。
- `cover` 必须真实存在；建议 1080×606、WebP。
- 正文标题从 `##` 开始，TOC 从 h2 生成。

### 新增一篇的 SOP

1. 在 `content/posts/` 新建 `<slug>.md`，套上面的 front matter。
2. 写正文；需要来源时先建 `research/<topic>-sources.md`，把链接、日期、原话归档。
3. 封面放到 `static/img/covers/`，文件名与 slug 对应。
4. 如需出现在 Answers，手动往 `data/questions.yaml` 加一条：`q`、`a`、`detail`、`url`；`url` 用 `/posts/<slug>.html/`。
5. 如属于艺术风格系列，更新 `content/series/art-direction-changes.md` 的 `groups`、正文和 reading order。
6. `npm run build`，必须 0 错误。
7. `hugo server` 本地点一遍：列表卡片、封面、目录、内链、外链。
8. `git add -A`、`git commit`、`git push origin main`。
9. 等 Cloudflare 部署完成，跑 `npm run check:live`，再点一遍线上新 URL。

## 7. 写作规范

这是这个站和普通游戏博客的主要区别，交接时不要丢：

- **第一方优先**：官方公告、Kickstarter 原文、开发者访谈、会议论文、Steam API 原始字段。
- **二手转述只能当线索**：媒体转述、Wiki、聚合站，必须回到原始出处；回不到就写明「只能找到二手说法」。
- **评价只证明反响，不证明设计决策**：玩家评论、媒体评分可以说明「玩家怎么接收」，不能拿来解释「开发者为什么这么做」。
- **时间要落地**：每个关键说法尽量带日期；同一件事的早期说法和后期回顾分开写。
- **不把可能写成确认**：没有证据的地方直接写「没有找到」「无法确认」。

研究归档在 `research/`，目前有 Fake OS、Probably Stolen、Steam page、visual overhaul 等来源文件。新文章建议沿用 `<topic>-01-sources.md` 的命名。

## 8. SEO 与页面机制

### 分页

- `hugo.toml`：`pagerSize = 12`，`homeColumns = 2`。
- 16 篇文章 → 首页 12 篇，`/page/2/` 4 篇。
- 分页页复用首页 Page 对象，不能直接用 `.Permalink` 当 canonical。统一走 `layouts/partials/seo/page.html`：
  - `canonical.html`、`opengraph.html`、`baseof.html` 都读同一个 `$seo`。
  - `/page/2/` 的 canonical / og:url 自指，标题带 `| Page 2`，description 带页码和条数。
- 如果以后把 `homeColumns` 改成 `3`（瀑布流），`page.html` 目前不会初始化分页上下文，必须重新验证 `/page/2/`。

### 每页元数据

- `description` 必须唯一；`check_site.py` 会检查缺失、重复、OG/Twitter description 不一致。
- `og:url` 必须与 canonical 一致。
- 正常页面不应出现 `noindex`；404 页必须 `noindex, follow`。
- JSON-LD 在 `layouts/partials/seo/schema.html`：文章页输出 `BlogPosting`，其他页保留 `BreadcrumbList`。

### 404

- `static/404.html` 是 Cloudflare Pages 的顶层 404。**不要删。**
- 没有它时，Pages 会把未匹配路径按 SPA fallback 返回首页，形成 soft 404（HTTP 200 + 首页内容）。
- 当前线上已验证：乱输路径、旧 tag 路径都返回真 404。

### robots.txt

- `static/robots.txt` 显式列出 Googlebot、Bingbot、Baiduspider 等并 `Allow: /`。
- Cloudflare 会在文件前注入一段 managed content，批量 Disallow AI 爬虫（含 Baiduspider）；显式 User-agent 组用于覆盖它。
- 不要删这些显式分组，否则可能重新被挡。
- 训练爬虫（GPTBot、ClaudeBot、CCBot 等）是有意拦截的；要放行就删对应段落。

### sitemap / RSS / 搜索

- sitemap 自动生成，当前 75 条 URL；404 不进 sitemap。
- `outputs.home = ["HTML", "RSS", "JSON"]`，`/index.json` 供本地搜索。
- 2 篇 `render: never` 演示文不在 sitemap，是预期。

## 9. 构建、检查、发布

### 本地命令

| 命令 | 作用 |
|---|---|
| `npm run build` | `hugo --cleanDestinationDir` + `check_site.py --public public --record .seo-check/latest` |
| `npm run check:site` | 独立目录构建 + 全站检查，不碰 `public/` |
| `npm run check:live` | 独立构建 + 线上 HTTP 探测 |
| `npm run submit-urls` | 当前不可用，见已知问题 |
| `npm run build:submit` | 当前不可用，见已知问题 |

`check_site.py` 会检查：

- 每个页面 canonical 是否自指且唯一；
- `og:url` 是否与 canonical 一致；
- description 是否缺失、重复、与 OG/Twitter 不一致；
- 正常页面是否意外 `noindex`；
- 404 是否存在且 `noindex`；
- sitemap 目标是否存在、404 是否误入 sitemap；
- 线上 `/`、`/page/2/` 是否 200，已知错误路径是否 404。

### Cloudflare 发布流程

1. `git push origin main`。
2. Cloudflare Pages 自动跑 Build command。
3. `hugo` 成功后跑 `python3 scripts/check_site.py --public public`。
4. 检查非零退出 → 整个部署失败，旧版本继续在线。
5. 成功后在 GitHub commit 上能看到 `Cloudflare Pages` check-run 为 success。

排查部署失败：

- GitHub commit 的 check-run / Cloudflare Deployments 看日志。
- 常见原因：`python3: command not found`（改成 `python`）、description 重复、canonical 不自指、404 被删。
- 不要只看 `git push` 成功就以为上线成功。

## 10. 已知问题（按优先级）

### P0：外链中转页 404

`hugo.toml` 里：

- `params.linkCard.redirectPage = true`
- `params.linkCard.redirect.pagePath = "/go/"`

但 `content/go.md` 被设为 `build: render: never`，线上 `/go/` 返回 404。文章里的外部链接如果走中转页，点击会落到 404。

修法二选一：

1. 恢复 `content/go.md`：删掉 `build: render: never / list: never`，把页面文案英文化；
2. 或把 `params.linkCard.redirectPage` 改为 `false`，外链直接打开，不走 `/go/`。

改完必须点一条文章里的外链验证。

### 已修复：两个菜单死链（2026-11-19）

原来菜单指向两个 `render: never` 的占位页，线上都是 404：

- `Friends > Circle` → `/friends-circle/`
- `Stats > Data` → `/data/`

修法：从 `hugo.toml` 删掉这两个菜单项。Friends 下拉删掉 Circle 后只剩 Links 一项，索性把一级菜单直接指向 `/links/`，去掉下拉层。两个占位 md 文件仍留档（`render: never`），不渲染、不进 sitemap。

验证：`npm run build` 为 0 错误；生成 HTML 已不含 `href="/data/"` 与 `href="/friends-circle/"`；线上重新部署后应确认这两个路径返回 404、导航无死链。

### P1：提交搜索引擎脚本缺失

`package.json` 里：

- `submit-urls`: `python submit_urls_to_search_engine.py`
- `build:submit`: `npm run build && python submit_urls_to_search_engine.py`

但仓库里找不到 `submit_urls_to_search_engine.py`，这两个命令必然失败。修法：补回脚本，或删掉这两个 script 条目。

### P1：分页上下文只覆盖双列首页

`layouts/partials/seo/page.html` 只在 `homeColumns != 3` 时初始化分页。以后改瀑布流或换首页引擎，必须重新验证 `/page/2/` 的 canonical、og:url、title、description。

### P2：其他容易踩的坑

- **未来日期**：`date` 晚于当前时间会被静默跳过，页数不变，不报错。
- **脏 `public/`**：Hugo 默认不清空旧产物。临时跑 `hugo` 要加 `--cleanDestinationDir`；项目 `npm run build` 已有。
- **`--minify` 去引号**：构建产物里属性可能没有引号，grep 时不要带引号匹配。
- **permalink 带 `.html/`**：站内链接写 `/posts/xxx.html/`，不是 `/posts/xxx/`。
- **主题升级**：直接改过 `themes/demius/` 的地方记录在 `THEME_CHANGES.md`；重新拉主题会全部丢失。优先在 `layouts/` 覆盖。
- **首页模板**：不要新建 `layouts/index.html`，主题首页是 `_default/index.html`，会遮掉分发逻辑。
- **演示页**：`content/` 下有 11 个页面，加上 `content/posts/` 下 2 篇演示文，都是 `render: never`（gallery、gear、wishlist、shuoshuo、music-planet、bangumi-planet、booklist、supporters、friends-circle、data、go），不是丢了。
- **主题示例数据**：`data/` 里 bangumi、booklist、gallery、gear、music、wishlist、supporters 多为主题示例，不要误以为都在用。
- **旧 tag 残留**：本地 `public/tags/appdetails` 等旧目录是历史构建残留，干净构建后消失，不是线上真实 tag。

## 11. 后续写作方向

1. **给 Art direction changes 补第三个 case**：现在只有 Borderlands 和 TF2，容易被看成两个特例。优先选有同期第一方材料、同样是「写实转风格化」的案例。
2. **把 Fake OS 三篇升成系列**：先写横向 hub（目录、搜索、聊天记录三种信息架构），再按同一标准加 1–2 个案例。
3. **把这次 SEO / 部署事故写成技术文**：Hugo 分页 `.Permalink` 陷阱、Cloudflare 缺 `404.html` 的 SPA fallback、构建时自动检查。素材是一手的，正好接上现有 3 篇技术笔记。
4. **方法论总纲**：「一条游戏史证据能证明什么」，用 Hypnospace、Borderlands、Probably Stolen 当例子，做全站内链 hub。
5. **Cel shading pillar**：`what-is-cel-shading.md` 搜索需求最大，可以扩成完整指南，再往下挂 Borderlands / TF2 案例。

不建议：追新闻、评测、榜单、购买指南。

## 12. 关键文件速查

| 文件 | 作用 |
|---|---|
| `hugo.toml` | 站点、菜单、分页、主题参数 |
| `content/posts/*.md` | 文章 |
| `content/series/art-direction-changes.md` | 艺术风格系列页 |
| `data/questions.yaml` | Answers 数据 |
| `layouts/partials/seo/page.html` | 统一分页上下文 |
| `layouts/partials/seo/canonical.html` | canonical |
| `layouts/partials/seo/opengraph.html` | OG / Twitter |
| `layouts/partials/seo/schema.html` | JSON-LD |
| `layouts/_default/baseof.html` | 标题、GA |
| `static/404.html` | Cloudflare 顶层 404 |
| `static/robots.txt` | 爬虫规则 |
| `scripts/check_site.py` | 自动检查 |
| `package.json` | 构建与检查命令 |
| `THEME_CHANGES.md` | 主题直接改动记录 |
| `research/` | 来源归档 |
| `static/img/covers/` | 封面 |

## 13. 交接验收清单

- [ ] `hugo version` 为 `0.167.0 extended` 或更高
- [ ] `npm install` 成功
- [ ] `npm run check:site` 输出 `errors: []`
- [ ] `npm run check:live` 输出 `errors: []`
- [ ] Cloudflare 最近一次部署为 success
- [ ] 线上 `/page/2/` 的 canonical 是 `https://pixeldango.com/page/2/`
- [ ] 线上乱输路径返回 404，不是首页
- [ ] `git status --short` 为空
- [ ] 三个已知死链（`/go/`、`/friends-circle/`、`/data/`）已确认是否修复

## 14. 不要做的事

- 不要改已发布文章的 slug。
- 不要删 `static/404.html`。
- 不要从 Cloudflare Build command 里删掉 `python3 scripts/check_site.py --public public`。
- 不要把未来时间写进 `date`。
- 不要直接改 `themes/demius/` 而不记 `THEME_CHANGES.md`。
- 不要新建 `layouts/index.html` 覆盖首页。
- 不要用 `git push` 成功代替部署成功。
- 不要在没有第一方来源的情况下把「可能」写成「确认」。
