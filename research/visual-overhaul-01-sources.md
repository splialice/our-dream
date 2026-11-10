# 视觉改版史：TF2 / Borderlands — 资料归档

> 归档日期：2026-11-09；审稿修订：2026-11-10
> **选它的理由**：接 `probably-stolen-28-player-demo` 里 RPS 提的两个先例，把「改美术」从新闻话术还原成有据可查的开发史。
> **本稿论点**：改头换面不是新鲜事，差别在**留下的证据**。TF2 有 2007 年会议论文 + 游戏内开发评论；Borderlands 有 2009 年 CEO 同期原话、同期访谈与引擎方技术文章；Probably Stolen 目前只有一句 X 帖 + 一份带数字的新闻稿。
> **不做**：不写「N 款改过画风的游戏」榜单；不把三例说成同一因果。

---

## 一、硬事实（一手 / 准一手）

| 项 | 值 | 来源 |
|---|---|---|
| TF2 公布名 | `Team Fortress 2: Brotherhood of Arms`，1998 年宣布 | Wikipedia TF2 开发史（引 GameSpot 1998/1999） |
| TF2 早期形态 | E3 1999 展示写实军事风、指挥官层级、伞降、 networked voice | Wikipedia（引 GameSpot 2000 Q&A、GameSpy 1999） |
| TF2 开发时长 | 约 9 年；2000 年第二次延期、之后六年无消息；Valve 做过 3–4 个不同版本 | Wikipedia（引 Game Informer 2007、Wired 2006） |
| TF2 改版公开 | 2006-07 EA Summer Showcase 重新亮相，首次展示卡通/插画风 | Wikipedia（引 GameSpot 2006） |
| TF2 发售 | **2007-10-10**，《橙盒》 | Wikipedia + Steam appdetails app 440，一致 |
| TF2 风格来源 | 20 世纪商业插画家 J. C. Leyendecker、Dean Cornwell、Norman Rockwell | Valve 论文摘要 / 官方 TF2 维基转录（一手） |
| 论文 | `Illustrative Rendering in Team Fortress 2`，Jason L. Mitchell、Moby Francke、Dhabih Eng；NPAR 2007，pp.71–76，DOI 10.1145/1274871.1274883；另有 SIGGRAPH 2007 courses 版本 DOI 10.1145/1281500.1281666 | ACM / dblp 索引；官方 TF2 维基有 2007-08-13 发布的视频逐字稿 |
| 改版理由（弱证据） | 写实风格与「不真实的玩法」无法自洽而放弃 | **Wikipedia 对游戏内开发者评论的转述，二手**；不是 Valve 论文的直接陈述，正文须与论文分开写 |
| 风格的功能性 | 剪影、边缘光、低视觉噪声，为的是远距离快速识别职业与威胁 | 官方维基转录 Jason Mitchell 原话（一手） |
| Borderlands 首次公开 | 2007 年，被形容为「Diablo meets Mad Max」；原预期 2008 年圣诞 | Eurogamer 2009-04-14 |
| Borderlands：4/9 邮件原话 | Pitchford：「Heh! No, Borderlands is not cel-shaded - it's a gritty and serious world after all.」 | **Kotaku 2009-04-09**《Gearbox: "Borderlands Is Not Cel-Shaded"》 |
| Borderlands：4/14 官方论坛转录 | 「since the game was first unveiled we have made big advancements with the art direction and the technology to support the art, and have produced some pretty impressive, even shocking results」；官方命名 `Concept Art Style`，Pitchford 称「We don't know what to call the result」 | **Kotaku 2009-04-14**《Gearbox Explain Cel-Shaded Borderlands》，转录官方论坛声明 |
| Eurogamer 的定位 | 2009-04-14 同期报道同一轮问答 | **二手报道**，不是上述引语的原始出处；用于证「当年否认 cel-shaded + 使用 Concept Art Style」 |
| Borderlands：6/12 采访 | 一小群艺术家推动新方向（当时游戏看起来越来越像），改版差点没做成 | **Kotaku 2009-06-12**《The New Borderlands Look That Almost Wasn't》；用户审阅时可直接打开并确认细节，本机 403 |
| Borderlands：改版机会与发起者 | 开发周期延长给美术团队重要机会；Pitchford 原话「From a small group of artists came an initiative to render the concept art style in the game.」 | **Unreal Engine 官网 2009-10-27**《Gearbox Software's Borderlands More Awesome Than Ever with Unreal Engine 3》，第 9 段 + 直接引语 |
| Borderlands：方案获认可 | 新原型让 Gearbox 管理层与发行商 2K Games 惊艳 | 同上，第 13 段 |
| Borderlands：技术实现 | Gearbox 工程师扩展 UE3 渲染功能；针对新视觉调整光照与着色；程序员与美术合作增加新渲染技术；保持对 UE3 代码库兼容 | 同上，第 14–16 段 |
| Borderlands 发售 | **2009-10-20，北美主机版（PS3 / Xbox 360）**；PC 版在当月稍后（10/26、10/30 两说） | 2K 官方页给 10-20；Take-Two/2K 新闻稿转录区分平台与地区 |
| Probably Stolen 对照 | 2026-10-28 发售；CEO 10-29 一句 X 帖说改了视觉；新闻稿只给数字，不给设计细节 | tinyBuild 新闻稿 / X 原帖（见 `probably-stolen-01-sources.md`） |

---

## 二、来源分工（三源证据链）

| 环节 | 用哪个源 | 能证明 |
|---|---|---|
| 官方命名与解释 | Eurogamer 2009-04-14（同期报道，含 Kotaku 4/9、4/14 转录的原话） | Gearbox 当年否认 `cel-shaded`，提出 `Concept Art Style` |
| 提出方案 / 过程 | Kotaku 2009-06-12 | 一小群艺术家主动推动、改版差点没做成 |
| 获得认可 / 技术实现 | Unreal Engine 官网 2009-10-27 | 开发周期提供机会、原型打动管理层与 2K、UE3 渲染层面的具体改动 |

链条：提出方案 → 获得认可 → 技术实现 → 官方命名与解释。正文**保留原有结构，只补一段技术说明**，不扩成 Borderlands 开发史章节。

---

## 三、冲突点

| # | 冲突 | 处理 |
|---|---|---|
| 1 | 「Borderlands 改成 cel-shaded」是流传最广的说法，但 Gearbox 当年否认这个标签 | 语气收弱：写成**常见 shorthand 不反映 Gearbox 自己的描述**。`Concept Art Style` 是官方命名，cel shading 是渲染技术，视觉归类与官方标签分开；不写成「一方错了」。UE 文章**不能单独证明**「完全不属于 cel-shading」，不拿来加强这一结论 |
| 2 | Steam app 8980 显示 `Borderlands Game of the Year`、发售日 2023-08-31，与 2009 原作不符 | 只用来说明**当前列表的日期字段不必等于原作首发日**；不单独证明重命名、重新打包或改日期（见 `steam-page-01-sources.md`） |
| 3 | Valve 论文原 PDF 链接 `valvesoftware.com/publications/2007/NPAR07_...pdf` 现在 **404** | 论文仍可由 ACM DOI、dblp、官方维基转录佐证；正文只引用 DOI 与维基转录，把 404 写进「链接会死」一节 |
| 4 | Kotaku 三篇与 UE 官网文章本机均 403 / 连接关闭 | Kotaku 4/9、4/14 用可检索的标题与引语片段并标注归因链；6/12 与 UE 文章由用户审阅时直接打开核对，正文写明本机 403、只写能核对的部分，不扩写 |
| 5 | ACM DOI 页 403 | 元数据由 dblp / HandWiki / Wikipedia 参考文献交叉，标注未直连 |
| 6 | 三例时间跨度 1999 / 2009 / 2026，媒体形态不同 | 只比较「留下什么证据」，**不比较成因或成功率** |

---

## 四、验证算例

**正例**：TF2 发售日 2007-10-10 同时出现在 Wikipedia、Steam appdetails(app 440)、官方 TF2 维基语境里 → 可放心用。

**反例**：把「TF2 改了画风 → 拿了 92 分」「Borderlands 改了画风 → 卖了爆款」「Probably Stolen 改了画风 → 18 万在线」并列，得出「改画风就能成功」——三个案例的证据强度、年代、平台完全不同，且没有一个来源给出因果证明。正文只写「有据可查」与「只有一句话」的差别。

---

## 五、未验证 / 不要写进正文

- 未找到 tinyBuild 或 Questing Goose 关于「具体改了哪些设计」的开发者访谈。
- Kotaku 三篇与 UE 官网文章均未能从本机直连；只写标题、可检索的引语片段与审阅时核对的内容，不扩写场景或数字。
- **UE 文章的证据边界**：它是引擎方发布的开发技术介绍（含 Pitchford 直接引语），**不是 Gearbox 的完整开发访谈**；没有列出具体改动了哪些美术资产，也不能单凭它证明「完全不属于 cel-shading」。正文必须写明这三点限制。
- IMDb trivia「最后 10 个月改完」等说法不采用。
- Venus Patrol 2009 把改版称为「mutiny」，只是同期博客转述，未直连核实，不引用。
- Valve 论文 PDF 已 404，不写「可在 Valve 官网下载」。
- 不写「TF2 是第一款这样做的游戏」之类的首创断言。

---

## 六、来源清单（2026-11-09 检索，2026-11-10 复核）

| 源 | URL | 性质 |
|---|---|---|
| 官方 TF2 维基：插画渲染视频逐字稿 | https://wiki.teamfortress.com/wiki/Illustrative_Rendering_in_Team_Fortress_2 | 一手转录，已直接抓取 |
| Wikipedia: Team Fortress 2（Development） | https://en.wikipedia.org/wiki/Team_Fortress_2 | 二手，带完整引文，已直接抓取 |
| ACM NPAR 2007 论文 DOI | https://doi.org/10.1145/1274871.1274883 | 一手元数据，页面 403 |
| Kotaku 2009-04-09 | https://kotaku.com/gearbox-borderlands-is-not-cel-shaded-5206042 | Pitchford 邮件原话；本机 403，据检索摘要 |
| Kotaku 2009-04-14 | https://kotaku.com/gearbox-explain-cel-shaded-borderlands-5210855 | 官方论坛声明转录；本机 403，据检索摘要 |
| Kotaku 2009-06-12 | https://kotaku.com/the-new-borderlands-look-that-almost-wasnt-5288292/ | 改版过程采访；本机 403，细节由审阅时直接打开确认 |
| Eurogamer 2009-04-14 | https://www.eurogamer.net/pitchford-borderlands-will-not-be-cel-shaded | 同期报道（非引语原始出处），已直接抓取 |
| Unreal Engine 2009-10-27 | https://www.unrealengine.com/blog/borderlands?lang=en | **一手技术文章 + Pitchford 直接引语**；本机 403，由审阅时直连核对原文（第 9、13、14–16 段） |
| 2K 官方 Borderlands 页 | https://borderlands.2k.com/zh-CN/borderlands/ | 一手发售日，北美主机版 |
| Steam appdetails API | https://store.steampowered.com/api/appdetails?appids=440 | 一手元数据 |
| tinyBuild 新闻稿 / X 原帖 | 见 `probably-stolen-01-sources.md` | 一手 |

---

## 七、正文口径声明

正文把三例写成「证据量的对照」，不是「成败对照」；所有日期带来源；`cel-shaded` 只作为常见 shorthand 出现，并与官方命名 `Concept Art Style` 区分；跨年代不做因果推断。标题改为 `TF2, Borderlands and the evidence behind an art makeover`，标签精简为 `Team Fortress 2` / `Borderlands` / `Valve` / `Gearbox`，开头互链 `probably-stolen-28-player-demo`，日期段互链 `what-a-steam-page-cant-tell-you`。审稿修订完成前保持 `draft: true`。

---

## 八、审稿修订记录（2026-11-10）

- `cel-shaded` 纠正语气收弱，区分官方命名与技术/视觉分类。
- Eurogamer / Kotaku 引语按 4/9 邮件、4/14 论坛转录、Eurogamer 同期报道三层拆开。
- TF2 放弃写实风的理由降级为 Wikipedia 对开发者评论的转述，与 Valve 论文分开。
- 补 Kotaku 2009-06-12 采访要点，并标注本机 403 的证据限制。
- **补 Unreal Engine 官网 2009-10-27 技术文章**：正式加入 Sources 与硬事实表，正文只加一段技术说明；写明它是引擎方技术介绍而非完整访谈，不列举资产改动、不据此强化 cel-shading 结论。
- 2K 的 2009-10-20 加「北美主机版」限定，PC 版另列。
- 标题、标签、Sources、两处站内互链同步更新。
