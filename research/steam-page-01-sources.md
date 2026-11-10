# Steam 商店页作为史料 — 资料归档

> 归档日期：2026-11-09；审稿修订：2026-11-10
> **选它的理由**：接 `probably-stolen-28-player-demo` 结尾那张「比游戏活得久」的旧商店页，把归因谨慎落成一篇可复现的技术笔记。
> **本稿论点**：商店页是**某一刻的元数据快照**，不是开发史。`appdetails` 能证明页面当下写了什么，不能证明两版共用代码、谁做的决定、页面为什么消失。
> **可复现性**：全部数字来自本机对 Steam 官方 API 的实测，命令写进正文，`last_checked = 2026-11-09`。

---

## 一、实测结果（`appdetails`，2026-11-09）

请求：`https://store.steampowered.com/api/appdetails?appids=<ID>&l=english&cc=us`，**一次一个 AppID**；一次带多个 ID 的请求返回 400。表里六行是把同一请求换 `$id` 分别跑六次得到的，不是一段脚本的输出。

| AppID | name | release_date.coming_soon | release_date.date | developers | publishers | 备注 |
|---|---|---|---|---|---|---|
| 3334540 | Deepspace Emporium | **true** | `2026` | Questing Goose Studio | Questing Goose Studio | 仍挂「未发售」，无评价 |
| 4348910 | Probably Stolen - Cyberpunk Shopkeeper Sim | false | `Oct 28, 2026` | Questing Goose Studio | tinyBuild | 已发售 |
| 3469870 | **no data** | — | — | — | — | 旧 demo，`success: false`，商店 URL 现在解析到 Steam 首页 |
| 440 | Team Fortress 2 | false | `Oct 10, 2007` | Valve | — | `is_free = true` |
| 10 | Counter-Strike | false | `Nov 1, 2000` | Valve | — | — |
| 8980 | Borderlands Game of the Year | false | `Aug 31, 2023` | Gearbox Software | — | **当前列表的日期，不是 2009 原作首发日** |

浏览器侧补充实测：

- `https://store.steampowered.com/app/3334540/` → 页面仍写 `This game is not yet available on Steam`、Planned release 2026、No user reviews，且留有一句 demo 版说明。
- `https://store.steampowered.com/app/3469870/` → 重定向到 Steam 首页（2026-11-09）。
- `https://pixeldango.com/posts/probably-stolen-28-player-demo.html` → 308 跳到带尾斜杠版本（站点既有行为）。

---

## 二、能证明什么 / 不能证明什么

| 字段 | 能说明 | 不能说明 |
|---|---|---|
| `name` | 页面此刻显示的名字 | 两版是不是同一个项目、谁改的名 |
| `coming_soon` + `date` | 平台当前标注的发售状态 | 真实发售计划、延期原因 |
| `developers` / `publishers` | 当前署名的公司 | 谁做了设计决策、有没有换团队 |
| `success: false` | 这个 ID 此刻没返回数据 | 缺数据的**原因**（响应本身没有说明）；不能据此写「已下架」 |
| 商店页正文 | 页面此刻的文案 | 文案何时写的、是否被沿用、代码是否复用 |

**核心结论**：`Deepspace Emporium` 页与 `Probably Stolen` 页描述高度相似，只能说明两段商店文案相似；不能证明两版共用代码或开发史。这正是上一篇里用「RPS identified…」而不写「became」的原因。

---

## 三、冲突点

| # | 冲突 | 处理 |
|---|---|---|
| 1 | app 8980 显示 2023-08-31，而 2K 官网写 2009-10-20（北美主机版，PC 当月稍后） | 只写「当前 Steam 列表的日期字段不必等于原作首次发行日期」；**不再概括成商店页会重命名／重新打包／改日期**，那三个动作都无法由这一行单独证明 |
| 2 | 旧 demo 页返回 `success: false` | 响应**没有说明原因**；地区限制、访问控制、配置变化等都只是需要另行调查的可能方向。正文只写「该 URL 此刻不再指向商品页 / API 返回 no data」，不写「已下架」 |
| 3 | 中文媒体称旧 demo 2025 年 4 月上线，Steam/SteamDB 是 2025-02-13 | 沿用上一篇口径，用 Steam 日期 |
| 4 | `release_date.date` 为字符串 `2026` 而非完整日期 | 说明它是「计划年份」，不是承诺日期 |

---

## 四、验证算例

**正例**：`coming_soon=true` + `date=2026` + 页面「No user reviews」三处一致 → 可确认「截至 11-09，这个页面仍被标成未发售」。

**反例**：拿 `appdetails` 的 `developers` 相同就推出「两款游戏是同一个项目改名」——字段只说明署名相同，不说明资产、代码或团队连续。这也是「换皮爆红」稿最常见的跳跃。

---

## 五、链接会死（本篇的可维护部分）

- Valve 2007 论文原 PDF 链接实测 **404**：`http://www.valvesoftware.com/publications/2007/NPAR07_IllustrativeRenderingInTeamFortress2.pdf`；论文仍可由 DOI 10.1145/1274871.1274883 与官方维基转录佐证。
- `Deepspace Emporium Demo` 页不再返回商品页数据。
- 因此档案表必须带 `last_checked`，死了标 `no data` 保留记录，不删行——「哪些链接死了」本身是内容。

---

## 六、未验证 / 不要写进正文

- 未核到 Steam 官方对 `appdetails` 字段语义的公开文档，正文只描述**实测到的行为**，不宣称官方定义。
- `success:false` 的具体原因未知，不推断、不列确定为成因。
- 不写「Steam 永久保留所有商店页」这类全称判断。

---

## 七、来源清单

| 源 | URL | 性质 |
|---|---|---|
| Steam Web API（appdetails） | https://store.steampowered.com/api/appdetails?appids=3334540&l=english&cc=us | 一手，本机实测，单 AppID 请求 |
| Steam：Deepspace Emporium | https://store.steampowered.com/app/3334540/ | 一手 |
| Steam：Probably Stolen | https://store.steampowered.com/app/4348910/ | 一手 |
| 2K 官方 Borderlands 页 | https://borderlands.2k.com/zh-CN/borderlands/ | 一手发售日；**2009-10-20 为北美主机版，PC 版当月稍后** |
| 官方 TF2 维基论文转录 | https://wiki.teamfortress.com/wiki/Illustrative_Rendering_in_Team_Fortress_2 | 一手转录 |

---

## 八、正文口径声明

所有 API 结果标注 `checked 2026-11-09`；把 `appdetails` 明确写成「未公开的公共接口，字段行为以实测为准」；结论只到「页面能证明什么」，不越过到「项目之间是什么关系」。标题不改，标签精简为 `Steam` / `Steam API` / `Borderlands`，互链 `probably-stolen-28-player-demo` 与 `tf2-borderlands-before-the-makeover`。审稿修订完成前保持 `draft: true`。

---

## 九、审稿修订记录（2026-11-10）

- 代码示例明确为「单 AppID 可复现示例」，说明其余五行是同参数换 ID 分别查询，并记下多 ID 请求返回 400。
- `success: false` 的原因推测收弱，改为「响应未说明，需另行调查」。
- app 8980 段落重写：只证明当前列表日期 ≠ 原作首发日，不证明重命名／重打包／改日期。
- 2K 的 2009-10-20 加北美主机版限定，PC 版另列。
- 标签、互链、Sources 同步更新。
