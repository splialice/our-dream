---
title: "Hugo 部署 Cloudflare 报 PostCSS not found"
slug: hugo-cloudflare-postcss-not-found
date: 2026-11-06T20:45:00+08:00
lastmod: 2026-11-06T20:45:00+08:00
draft: false
description: "本地 hugo 构建正常，推到 Cloudflare 就报 postcss binary not found。这是长期存在的坑，社区答案大多不完整。本文给出可复现的三步配置与验证方法。"
summary: "本地能构建、线上报 POSTCSS not found，原因不在主题也不在 Hugo 版本，而在 Cloudflare 构建环境没跑 npm install。"
tags: ["Hugo", "Cloudflare Pages", "PostCSS", "部署排错"]
cover: "/img/covers/postcss-not-found.svg"
categories: ["建站折腾"]
comments: true
---

在本地跑 `hugo` 一切正常，推到 Cloudflare Pages 就红了一片：

```
Error building site: POSTCSS: failed to transform "/css/main.css" (text/css).
You need to install PostCSS.
See https://gohugo.io/functions/css/postcss/:
binary with name "postcss" not found in PATH
```

关键信息在最末尾那半句：**binary with name "postcss" not found in PATH**。

这不是主题坏了，也不是 Hugo 版本不对。**是构建环境里根本没有 postcss 这个可执行文件。**

## 先搞清楚：为什么这个主题非要 PostCSS

不是所有 Hugo 主题都会遇到这个报错。只有当主题用 `resources.PostCSS` 处理样式时才会。

我这次用的主题，`assets/css/` 下有 **76 个 CSS 源文件**：

```
_advertisement.css
_announcement.css
_archive.css
_article-cards.css
_aside.css
_author.css
...（共 76 个）
```

它们靠 `@import` 互相引用，最后由 `postcss-import` 插件合并成 **5 个输出文件**。

模板里的调用长这样，一共 6 处：

```go
{{ with resources.Get "css/main.css" | postCSS | minify | fingerprint }}
  <link rel="stylesheet" href="{{ .RelPermalink }}">
{{ end }}
```

看到 `| postCSS` 这一节，就意味着 **构建时必须能调用到 postcss 命令行工具**。

而 `postcss` 不是 Hugo 自带的，它是 npm 包。

## 三种流传的解法，前两种都不完整

我搜了一圈，这类帖子从 2021 年一直排到 2022 年，Hugo 官方论坛和 Cloudflare 社区都有。给出的答案大致三类。

### 第一种：设 NODE_VERSION=16

> "Is this with Cloudflare Pages? Do you have a NODE_VERSION env var set to something more modern such as 16?"

**这个解法方向对了一半。** Cloudflare 早期默认 Node 12，确实太老，装不上新版 postcss。

**但它只是前提条件，不是解决办法。**

我这次的 Node 版本是 v22.22.2，早就够了，照样报同样的错。

### 第二种：全局安装 postcss

> "install postcss and postcss-cli AND all used plugins either locally in your site or globally"

`npm install -g postcss postcss-cli` —— 有人在本地这么干，然后推上去，仍然失败。

**原因很简单：Cloudflare 的构建容器是干净的。** 你在自己电脑上全局装的东西，线上一个都没有。

而且就算线上能全局装，**下一步还会踩到 `postcss-import` 找不到的坑**——因为这个主题的 `postcss.config.js` 显式依赖了它。

### 第三种：装 Hugo extended

> "Hugo itself needs to be either compiled with postcss/pipes support or you install one of the extended precompiled versions"

**这条是对的，但不解决当前问题。**

`postCSS` 这个 pipe 需要 Hugo extended 版本才有。Cloudflare 在你指定 `HUGO_VERSION` 时下载的**默认就是 extended 版**，所以这一步通常已经满足。

真正的缺口在 Node 侧。

## 正确做法：三步，缺一不可

### 第一步：构建命令里必须带 npm install

这是最关键的一条。

```
Build command:  npm install && hugo --gc --minify
```

**不是 `hugo`，也不是 `hugo --minify`，前面必须有 `npm install &&`。**

原因：Cloudflare Pages 每次构建都是全新容器，**不会保留上一次的 `node_modules`**。你仓库里就算提交了 `package.json`，不跑 `npm install` 就没有 `node_modules`，Hugo 自然找不到 postcss 可执行文件。

我一开始填的就是裸的 `hugo`，报错一模一样。

### 第二步：显式指定 Hugo 版本

```
环境变量:  HUGO_VERSION = 0.167.0
```

不指定的话，Cloudflare 用构建镜像里内置的那个版本。**这个版本会随镜像更新漂移**，今天是 0.14x，明年可能是别的。

而 Hugo 在 0.158 之后改过一批配置键名（比如 `languageCode` → `locale`），版本漂移会让本来能构建的站突然报弃用错误甚至失败。

**填你自己本地跑通的那个版本号。**

### 第三步：构建输出目录填 public

```
Build output directory:  public
```

这条容易漏。Hugo 默认输出到 `public/`，但 Cloudflare 的输入框是空的，不填就等于没指定。

## 三处填完的样子

| 字段 | 值 |
|---|---|
| Build command | `npm install && hugo --gc --minify` |
| Build output directory | `public` |
| HUGO_VERSION（环境变量） | `0.167.0` |

**注意 `--gc` 和 `--minify` 不是必须的**，但建议加：前者清理无用的缓存资源，后者压缩输出。真正不能少的是 `npm install &&`。

## 怎么验证真的修好了

构建日志里看这两行：

```
Install dependencies:  npm install        ← 出现这行说明在装依赖
...
Total in 3.5 seconds                       ← 构建通过
```

然后打开线上页面，**按 F12 看 Network 面板**：

- **CSS 请求返回 200** → 修好了
- **CSS 请求 404** → 是 baseURL 的问题，不是 PostCSS
- **页面完全没有 `<link rel="stylesheet">`** → 模板里的 postCSS 那段被跳过了（可能 `resources.Get` 路径不对）

**这三种失败长得完全不一样，别混。**

## 一个容易踩的连带问题：baseURL

PostCSS 修好之后，很多人紧接着遇到页面裸奔——HTML 出来了，但样式没生效。

**十有八九是 `baseURL` 写错了。**

```toml
baseURL = 'https://example.com'        ← 错，上线后所有绝对链接都指向 example.com
baseURL = 'https://yourdomain.com'     ← 也错，少了结尾斜杠
baseURL = 'https://yourdomain.com/'    ← 对
```

**结尾那个斜杠必须有。** 少了它，Hugo 生成的资源路径会拼成 `https://yourdomain.comcss/main.css` 这种残缺形式，而 **Hugo 不会报任何错**。

这个坑我今晚也踩了——排查了半天，最后发现是一个字符的问题。

## 补充：这个报错还有第四种可能

如果上面三步都做了还是报同样的错，检查一处：

```toml
[security]
  [security.exec]
    allow = ['^postcss$']
```

Hugo 从某个版本开始对「执行外部命令」加了白名单。如果你的配置里限制了 `security.exec.allow`，`postcss` 不在名单里，**即使装了也调不动**。

不过这个情况很少见，大多数默认配置没开这个限制。

## 小结

报错原文里 `binary with name "postcss" not found in PATH` 已经把答案写清楚了：**找不到这个命令**。

所以解法也只有一句话：

> **在构建命令前面加 `npm install &&`，让它在构建时被装上。**

NODE_VERSION、全局安装、extended 版本，这些都是必要条件，但都不是充分条件。**缺 `npm install` 这一步，前面做多少都没用。**

---

*本文的配置在 Hugo 0.167.0 + Cloudflare Pages（Git 连接自动部署）+ Node 22 环境下验证通过。主题文件结构因主题而异，判断依据是模板里有没有 `| postCSS` 这一节。*