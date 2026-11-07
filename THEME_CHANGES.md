# 主题改动记录

本文件记录所有对 `themes/demius/` 的直接修改。

**目的**：以后如果更新主题（重新拉一份），下面这些改动会全部丢失，需要对照本文件重做。

**原则**：优先在项目层 `layouts/` 覆盖，不改主题。只有确实无法覆盖时才改主题，并记在这里。

---

## 2026-11-07 主题内删除

### `themes/demius/content/posts/theme-configuration-guide.md` — 已删除

**原因**：Hugo 会把 `themes/<name>/content/` 合并进站点内容。这个文件是主题作者的中文使用文档，会作为一篇文章生成在 `/posts/demius-主题配置指南.html/`。

英文站不需要它，而且它会让首页多出一篇中文文章。

**为什么不用覆盖方式**：可以在 `content/posts/` 建同名文件加 `build: {render: never}` 停用它，但那样仓库里会长期留一份没用的中文文件。直接删除更干净。

**恢复方法**：删除即可，不需要恢复。

**如果要重做**：
```bash
rm themes/demius/content/posts/theme-configuration-guide.md
```

---

## 项目层覆盖的模板（不改主题，仅记录备查）

这些文件在 `layouts/` 下，不涉及修改主题，主题更新不会影响。列出是为了知道哪些模板已被接管。

| 文件 | 改动 |
|---|---|
| `layouts/_default/single.html` | 文章页中文化英文（日期格式/字数/浏览/阅读时长/版权/上下篇）|
| `layouts/_default/baseof.html` | `<html lang>` 改用 `site.Language.LanguageCode` |
| `layouts/partials/post-card.html` | 置顶/加密/阅读时长英文 |
| `layouts/partials/header/header.html` | aria-label 英文 |
| `layouts/partials/footer/footer.html` | 运行时长/加载中英文 |
| `layouts/partials/aside/widgets/announcement.html` | 站点公告 → Announcement |
| `layouts/partials/aside/widgets/social-media.html` | 关注我们 → Follow us |
| `layouts/partials/aside/widgets/toc.html` | 目录 → Contents |
| `layouts/partials/aside/widgets/hitokoto.html` | 一言 → Quote（组件已关）|
| `layouts/partials/aside/widgets/recent-posts.html` | 最新文章 → Latest posts |
| `layouts/partials/seo/schema.html` | 新增：结构化数据（主题原本没有）|
| `layouts/links.html` | 资源库页文案英文 |

**注意**：主题更新后，这些覆盖文件仍然有效（因为它们在项目层）。但如果主题的对应模板有了新功能，覆盖文件不会跟着更新，需要手动对比。

---

## 已被停用的主题页面（front matter 加 `build`）

这些文件保留在 `content/`，加了 `build: {render: never, list: never}`，不生成页面。

删掉 front matter 里那三行即可恢复。

```
content/gallery.md
content/gear.md
content/wishlist.md
content/shuoshuo.md
content/music-planet.md
content/bangumi-planet.md
content/booklist.md
content/supporters.md
content/posts/hello-demius.md
content/posts/immersive-reading-guide.md
```

---

## 踩过的坑（写在这里，免得下次重犯）

1. **`_build` 是废弃写法**，Hugo 0.145+ 要用 `build`，写错了直接构建报错。
2. **改首页不要建 `layouts/index.html`** — 主题真正的首页是 `_default/index.html`，它负责分发到 `main/engine-*.html`。建了 `layouts/index.html` 会把整套分发逻辑遮掉，首页变成空列表。
3. **permalink 带 `.html`** — 实际地址是 `/posts/xxx.html/`，不是 `/posts/xxx/`。
4. **date 写未来时间会被跳过** — 静默跳过，不报错，页数不变。
5. **`--minify` 会去掉属性引号** — grep 构建产物时不要带引号匹配。
6. **SF 封面用 SVG** — 站内显示正常，但社媒 og:image 需要 PNG。