# The Roottrees are Dead — 资料归档

> 归档日期：2026-11-07
> 用途：素材，不是成稿。这个游戏有个特殊之处：**它有两个版本，事实很容易搞混。**
> 2026-11-12 核实更新：补入开发者访谈、两份 itch.io devlog 与 Robin Ward 技术日志，更正四处错误（见下文 ⚠️）。

---

## 一、先分清两个版本（这是最容易写错的地方）

| | 免费版 | Steam 版 |
|---|---|---|
| 时间 | **2023-11-08** 发布公告（itch.io；游戏文件 11-04 上传） | **2025-01-15** 发售（App 2754380） |
| 起因 | Global Game Jam 2023，一周做出原型；之后用了 **11 个月**才完成（作者自述） | 2024-03-01 宣布 **starting over from scratch**，从头重做 |
| 作者 | Jeremy Johnston（`jjohnstongames`） | Robin Ward（aka `eviltrout`）主导程序，用 **Godot** 重写 |
| 美术 | **AI 生成**；作者 2024 年公开承认玩家对 AI 图的批评 | 重画（归档记的是 Henning Ludvigsen，**本轮未独立核实**） |
| 价格 | 免费 | **US$19.99**（2026-11-12 查美国区；首发折扣未核实） |
| 发行 | 自发布 | **Evil Trout Inc.**（开发商与发行商，Steam 页核实） |

**核实后可用的因果**：2024-03-01 的 devlog 里，Jeremy 同时写了三件事——玩家指出 AI 图的问题、UI/UX 需要改进、"The new version of the game will be released on steam, and will not be free"。**可以写「原版因 AI 图与界面挨批，团队决定从头重做并改为付费」，但不要写成「AI 图导致它只能免费」这种单一因果**（那是归档时的归纳，作者没这么说）。

> 这条在做"AI 生成内容的商业后果"这个题目时仍有用，但证据形态变了：作者本人承认问题、宣布重做、宣布收费，三件事都在同一篇 devlog 里。

---

## 二、硬事实

| 项 | 值 | 来源 |
|---|---|---|
| 类型 | 家谱推理 / 档案检索 | edgechat |
| 设定 | 架空 1998 年，56k 拨号猫 | 多来源一致 |
| 平台 | Windows / Mac / Linux，另有 iOS | edgechat |
| 时长 | 含 Roottreemania 扩展约 20 小时，"大约是原版两倍" | edgechat |
| 语言 | 英 / 西 / 德 / 法，2025 年底加**简体中文** | caniplaythat |
| 续篇 | **Roottreemania**（Steam 版附带的第二案） | edgechat |

**注意**：edgechat 说"20 小时含扩展，约为原版两倍"，而 thinkygames 评测的口径是玩法上"目标 50 个家族成员"。两个说法不冲突，但**时长数字建议写"十几个小时到二十小时"，别写精确值。**

---

## 三、剧情设定（写文章当开头用）

```
1998 年 12 月，Carl Roottree（Roottree 糖果公司总裁）与妻子、
三个女儿（Rhayna / Rhose / Rhiley，都是模特）一起死于私人飞机失事。
五人合计身家超过 10 亿美元。

公司创始人 Elias Roottree 在遗嘱里规定：
公司收益在**所有血亲后代**之间平分，不论隔多少代。

于是问题变成：谁还算 Roottree 家的人？

空难两天后，一个匿名客户找上门（玩家），
委托把整个家族树查清楚。
```

**注意名字拼写**：Rhayna / Rhose / Rhiley——三个都 R 开头，是刻意设计（增加混淆难度）。

---

## 四、机制：这是全文最该写细的部分

### ① 你的工具只有三样

```
电脑（拨号上网）     SpiderSearch 搜索引擎
                    —— 只能搜到"有名的"家族成员和重大事件
图书馆（Public Library Database）   必须**先知道书名和作者**才能借
期刊库（Periodical Archive）       **必须先在别处看到这本杂志/报纸的名字**，它才会进库
```

⚠️ **出处更正（2026-11-12）**：这三条边界写得最清楚的是 **PC Gamer 评测**（Tom Sykes, 2025-02-08），不是 thinkygames。thinkygames 只写了一句 "Typing the names of the Roottree sisters into the authentically pre-Google search engine SpiderSearch yields quick results"，以及线索会延伸到地方报纸、旧杂志、日记、家庭照片等。**两篇不要混写成同一段原文。**

**这三条限制是整个游戏设计的核心**（归档时的归纳，保留）：
> 不是"搜不到"，是"你得先知道该搜什么"。

⚠️ 注意层级：以上是**媒体对玩法的描述**，不是开发者对设计意图的说明。见第七节。

### ② 搜索仍要打字；划词用于笔记

⚠️ **更正（2026-11-12）**：归档原来写"不是打字，是划词""不用打字"，**这是错的**。搜索框仍然由玩家输入关键词；划词改的是笔记功能。

```
在网页/书/证据上划一段文字 → 可以
   a) 直接拿去搜
   b) 或者自动存进笔记本，并保留回链到原始出处
```

**一手技术实现**：Robin Ward, *Building The Roottrees are Dead*（2025-01-27）。证据界面用 Godot 的 `RichTextLabel`；因为文本带 BBCode 标签，选区可能跨多个标签，要把高亮映射回原始字符串，他自己写了 GDScript BBCode Parser。原话：`this feature was important to me`。回链是**双向**的：笔记 → 原文，原文 → 高亮 → 笔记。

Can I Play That 的玩家视角原话：
> "This highlighted text is automatically added to the notebook, even linking back to the source"

**证据边界**：Ward 记录了实现过程，也在 2025 年访谈里说过想改进原版的界面 / 笔记本 / 高亮；但**没有找到他解释"为什么选划词而不是手动输入笔记"**。别替他补这个动机。

### ③ 三条帮助机制（这三条是设计亮点）

| 机制 | 英文原名 | 触发 | 作用 |
|---|---|---|---|
| 证据直觉 | `Evidence Intuition` | 每份证据右上角显示一个数字 | 告诉你有几条**还没用上的**线索。可关闭 |
| 锁定 | `locked` / `profiles are locked` | 一次答对 3 个人 | 这 3 条锁定，防止你反复改。**越往后要答对越多才能锁定** |
| 橡皮鸭 | `rubber duck` | 你主动问 | 第一次给全局提示，第二次给更具体的（比如"该搜什么词"）|

**还有一个容易漏的**：`Star-marked notable Roottrees` —— 重要成员带星号，提示你哪些人更容易找到资料，降低开局负担。

**Can I Play That 的评测原话（英文）**：
> "the game never punishes you when you need help."

⚠️ 这是评测作者 Marijn Rongen 的评价，**不是开发者声明**，别写成"开发者说游戏不惩罚求助"。

**这是可访问性设计的一个正面样本**，值得单独写一段。

### ④ 惩罚设计

- **答错不锁**，但正确答案不确认
- 越往后线索越难找，但"剩下的名字和照片能去的地方也越少"——**排除法自然收紧**
- 有些评测提到：错判会**清空你的工作清单**（这一条来自 escapegaming 对 Database Detective 的描述，不是本作，别搞混）

### ⑤ 档案袋与打印机

游戏会自动打印"值得打印"的东西（带照片的文章、杂志封面），摆在桌上，可以一键在"屏幕 / 桌面"之间切换。

**这个设计的作用**：让"两个屏"变成叙事工具，而不是 UI 便利。

---

## 五、那句"三合一"引语：更正（2026-11-12 核实）

❌ **原来归档写"Robin Ward 第一次看到免费版时说：Her Story meets Return of the Obra Dinn meets The Case of the Golden Idol"——这句找不到原始出处，不要引用、不要署名 Robin Ward。**

查过 itch.io 开发者公告、Robin 的技术日志、官方宣传文字和两场开发者访谈，没有找到三款游戏合并成一句的第一方表述。

**有一手证据的是这两条**：

- Jeremy Johnston，itch.io 发布公告，2023-11-08：
  > "The game is heavily inspired by Return of the Obra Dinn and Her Story, two fantastic games that if you haven't played, I'd highly recommend."
- 同一场 2026-07-06 访谈里，Jeremy 把游戏称为 **"a marriage of those two games"**（Her Story + Obra Dinn）。Robin 谈过自己喜爱 Obra Dinn 和 Golden Idol，但那是创作背景，**不是**把三款并列成一句。

下面的坐标系是归档时自己归纳的，**保留作内部参考，不要写成开发者原话**：

```
Her Story      数据库关键词检索
Obra Dinn      从碎片推身份（并且要三条一起确认）
Golden Idol    从场景里凑出句子/关系
```

---

## 六、评价与批评（一起写才站得住）

**正面（thinkygames）**：
> "作为一个谜题，这棵家族树令人极为满足，是一窝互相缠绕的兔子洞：你在一条里挖到不能再挖，过程中发现好几条新的，然后跳进下一条。"

**正面（hard-drive）**：
> "它不像别的游戏那样牵着你的手。被卡住的时候，通常是因为我读太快了，或者没把每个新出现的专有名词都搜一遍。"

**批评（必须写）**：
- **hard-drive**："偶尔依赖 moon logic。第一案里有几处关键，只能靠一个大直觉跳过去——比如一眼判断两个几乎一样的人谁更老。"
- **adventuregamehotspot**："接近结尾时有几处解法特别刁钻，几乎接近不公平。"
- **thinkygames**："作为叙事体验，它的野心不如它的谜题。"
- **caniplaythat**："文字大小只能调一部分，无屏幕阅读器，无手柄支持。"

**thinkygames 还有一句我特别喜欢**（可以当引文）：
> "它主动嘲笑了 Reddit 式网络侦探那套做法，以及那套做法怎么把人带进阴暗又离谱的地方。"

---

## 七、开发史（2026-11-12 补：这一节从"薄"变成最硬的一节）

1. **一周做原型**：Global Game Jam 2023，Jam 的时间压力下他原本想找朋友画图（那时生成式 AI 还不普及）
2. **11 个月扩写**，然后 Robin Ward 发现它、联系、重写
3. **⭐ 2026-07-06 开发者访谈（Flatfoots and Fools，Jeremy + Robin）**：Jeremy 亲自解释了搜索系统为什么这么简单——
   > "I had to build something that I could do very quickly."
   > "this comes directly from my technical limitations."

   原版搜索本质是**预先建好的内容数据库做匹配**：命中就返回结果，否则返回无结果。他还说灵感来自自己参加 **Trivia 比赛**时快速查冷门知识的习惯，以及 Her Story / Obra Dinn。
4. **⭐ 2024-03-01 itch.io devlog（最重要的反证）**：Jeremy 把 **"better search abilities for names on the family tree"** 和 **"a better browser history"** 列为需要改进的 UI/UX 项，并宣布 "starting over from scratch"、Robin Ward 接手。
   → **所以"开发者刻意限制搜索来还原 1998 年互联网"这个判断不成立**。原版搜索是开发条件的产物，而且作者自己把它列为待修的问题。
5. **2025-01-27 Robin Ward 技术日志**：Godot 重写、RichTextLabel、BBCode Parser、双向高亮回链（见第四节 ②）。

**Robin Ward 的背景**：Discourse 论坛软件的开发者，之前做过 Forumwarz（一个 2000 年代恶搞论坛的浏览器游戏）。

> **这条线索有意思**：做论坛软件的人，接手了一个关于"翻旧资料"的游戏。

---

## 八、可以写的角度（候选）

1. **【已废弃】**"你得先知道该搜什么"——1998 年的搜索限制，反而成了最好的谜题设计。⚠️ **这个说法从机制反推了意图，不成立，别再写**。已改写成 2026-11-12 的《The Roottrees Are Dead: How a Game Jam Shortcut Became a Research Tool》，中心是「Game Jam 限制 → 研究工具」。
2. **三条帮助机制**——一个从不惩罚求助的游戏，怎么做到不发水（注意引的是评测，不是开发者）
3. **AI 图 → 重做 → 付费**：只用 2024 devlog 里作者自己承认的三件事，别写单一因果
4. **【已废弃】**Her Story + Obra Dinn + Golden Idol 三条基因。⚠️ 三合一引语无出处；只能分别写开发者承认的两个灵感 + Golden Idol 的背景
5. **新角度（证据最硬）**：*A Search Engine Built Around the Limits of a Game Jam* —— 从预设匹配数据库到双向来源追踪笔记本的演变

---

## 九、待核实 / 不要写

```
❌ 不要写"50 个家族成员"作为确定数字 —— 只有一个评测这么说
⚠️ 20 小时 —— 是含扩展的口径
⚠️ Steam 评价数 —— 本轮没抓到，别写
❌ 不要把 free 版和 Steam 版的剧情当同一件事写 —— 扩展是新增的第二案
❌ 不要写"开发者刻意限制搜索以还原 1998 年互联网" —— 与 2024 devlog 和 2026 访谈直接冲突
❌ 不要引用/署名那句三合一引语 —— 无第一方出处
❌ 不要写"划词代替打字""不用打字" —— 搜索框仍可输入
❌ itch.io 日期不要写 2023-11-07 —— 11-08 是发布公告，11-04 是文件上传，分开写
⚠️ Henning Ludvigsen 手绘、$19.99 首发 -10% —— 本轮未独立核实
```

---

## 十、来源清单（2026-11-12 按证据层级重排）

**A. 官方页面 / 开发者一手（优先）**

| 来源 | 日期 | 链接 |
|---|---|---|
| Steam 商店页（App 2754380）：发售日、开发商 / 发行商、价格、About | 2025-01-15 | https://store.steampowered.com/app/2754380/The_Roottrees_are_Dead/ |
| itch.io 原版游戏页（作者 `jjohnstongames`） | 2023 | https://jjohnstongames.itch.io/the-roottrees-are-dead |
| Jeremy 发布公告 *The Roottrees are (finally) Dead!*：GGJ 起源、Obra Dinn + Her Story 灵感 | 2023-11-08 | https://itch.io/devlog/632664/the-roottrees-are-finally-dead.amp |
| ⭐ Jeremy devlog *But For Real This Time*：AI 图批评、better search / browser history、从头重做、Robin 接手、宣布付费 | 2024-03-01 | https://itch.io/devlog/690887/the-roottrees-are-dead-but-for-real-this-time.amp |
| ⭐ 访谈 *Flatfoots and Fools — Jeremy Johnston and Robin Ward*（05:51–08:28 讲搜索系统） | 2026-07-06 | https://podscan.fm/podcasts/flatfoots-and-fools/episodes/jeremy-johnston-and-robin-ward-developer-interview |
| ⭐ Robin Ward 技术日志 *Building The Roottrees are Dead*：Godot、RichTextLabel、BBCode Parser、双向回链 | 2025-01-27 | https://eviltrout.com/blog/2025-01-27-building-the-roottrees/ |

**B. 媒体评论（只用来描述玩法，不支撑设计意图）**

| 来源 | 链接 | 用途 |
|---|---|---|
| PC Gamer, Tom Sykes | https://www.pcgamer.com/games/puzzle/the-roottrees-are-dead-review/ | **三个检索工具各自的边界**（原归档误记为 thinkygames） |
| Thinky Games, Rick Lane | https://thinkygames.com/reviews/the-roottrees-are-dead-review/ | SpiderSearch 短句、跨媒介线索、批评 |
| Can I Play That, Marijn Rongen | https://caniplaythat.com/2025/12/29/indie-spotlight-the-roottrees-are-dead/ | Evidence Intuition / locked / rubber duck、划词回链、可访问性 |
| adventuregamehotspot 评测 | https://adventuregamehotspot.com/review/3671/the-roottrees-are-dead | 批评 |
| hard-drive 评测（含批评） | https://hard-drive.net/news-games/game-night-unravel-decades-of-family-drama-in-the-roottrees-are-dead | 批评 |

**C. 事实卡（低可信，只作线索，别当硬事实）**

| 来源 | 链接 |
|---|---|
| edgechat 事实卡（版本沿革） | https://www.edgechat.ai/the-roottrees-are-dead |

> 2026-11-12 核实说明：A 组里带 ⭐ 的三条是本轮新补的，直接推翻了原归档「开发者刻意限制搜索」的推断；B 组的三工具描述出处已从 thinkygames 更正为 PC Gamer。
