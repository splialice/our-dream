# Hypnospace Outlaw — 资料归档

> 归档日期：2026-11-07
> 用途：素材，不是成稿。每条事实后面标来源，标了"待核"的不要直接写进文章。

---

## 一、硬事实

| 项 | 值 | 来源 |
|---|---|---|
| 发售日 | 2019-03-12（PC） | edgechat / 官方站 |
| 主机版 | 2020-08-27（Switch / PS4 / Xbox Game Pass） | edgechat |
| 开发 | Tendershoot（Jay Tholen 主导） | 官方站 hypnospace.net |
| 发行 | No More Robots | edgechat |
| 引擎 | **Construct 2**（选它是因为 HTML5 能模拟浏览器，不用写太多底层代码） | grokipedia |
| 团队规模 | 核心 4 人 + 音效/QA，结束约 7 人 | grokipedia |
| 开发周期 | 2015 夏原型 → 2019 初完成，约 4 年 | grokipedia |
| 售价 | 原 $19.99；历史最低 $4.99（-75%） | Kotaku / 官方 |
| 媒体均分 | 83/100（29 篇） | edgechat |
| 玩家评分 | 92/100 | edgechat |
| Steam 评价 | **97% 好评，5,542 条** | edgechat |
| 主线时长 | 约 9.5 小时；全收集 16 小时（914 人样本） | edgechat / HowLongToBeat |
| 其他时长说法 | Nintendo Life：赶时间+全程用提示 6-7 小时；Saving Content：10-12 小时 | 各自评测 |

**注意**：Steam 评价数 5,542 是 edgechat 的统计口径，可能只算了一部分（Steam 上 PC 版评价数通常更多）。**要引用就写"五千余条"，别写精确数。**

---

## 二、规模：页面数量有三个不同说法

这是**最需要小心的地方**，三个来源给的数字不一样：

| 说法 | 出处 | 可信度 |
|---|---|---|
| "over 200 unique pages" | grokipedia | 中（AI 生成百科，未给原始出处） |
| "hundreds of pages split into zones" | edgechat | 中 |
| "150+ 个假网站" | 我上一轮口头说过，**未找到原始来源** | **低，不要用** |

**处理建议**：写"两百多个页面"并注明是媒体描述，或者干脆写"分成数个 zone，每个 zone 里几十个页面"，不去碰精确总数。

**另一个可用的硬数字**：官方 mod 站 indexgg 记录 **131 个 mod**，最新更新 2026-10-15。
→ 这说明游戏发售后 7 年仍有社区在做内容，**比页面总数更有说服力**。

**wiki 规模**：hypnospace.wiki.gg 目前维护 **292 篇文章**（专门记录这个虚构网络里的页面、角色、事件）。
→ 这个数字很关键：**一个虚构的互联网，需要 292 篇百科条目来描述它。**

---

## 三、机制：玩家到底在做什么

**核心循环**（官方站原话 + 评测交叉验证）：

1. 收到 Merchantsoft 派下来的"违规举报"
2. 在虚构浏览器里自己找那个页面（没有直接链接）
3. 找到后点法槌图标，把内容删掉
4. 拿 HypnoCoin，去买桌面主题、屏幕保护、虚拟宠物、杀毒软件
5. 后期案件变成：盗版文件分享团伙、黑客组织、隐藏社群、密码保护的未列出页面

**找页面的三条路径**（这三条是关键，说明它不是"给链接点进去"）：

```
① 目录（directory）
   Tholen 说：原本想让用户自己分类，但玩家看不懂
   最后改成 MerchantSoft 用企业逻辑强行分区
   → Goodtime Valley（"记得过去的好日子吗"）、Teentopia Paradise
② 搜索框
   输入关键词找页面
③ 标签 / 社团（clubs）
   比如 HS_Goofs-n-Laughs，点进去能看到所有打了这个标签的页面
   → 这是找"用户不想让官方知道"的页面的主要办法
```

**来源**：Rock Paper Shotgun 2019-10-09 那篇开发者访谈（一手，Tholen 亲口说）

**分区名单**（可核实的）：
```
Teentopia       焦虑青少年、nu metal、八卦
Open Eyed       新时代灵修、阴谋论
Coolpunk        一个虚构的音乐流派（Tholen 自己造的）
Goodtime Valley 老年人怀旧
Gamer Fortress  已被官方移除的 zone（有 mod 把它恢复了）
```

---

## 四、开发史：最有价值的几个细节

### ① 这个游戏原本不是这个游戏

**原型是 2014 年的一个小游戏《Hypnospace Enforcer》**，玩法是"在信息高速公路上追违规用户"。页面只是关卡之间的过场。

**核心机制是「末班车」式的设计**（这是我读下来最有意思的一点）：

原本有个"无尽跑酷"模式（Hypnospace Highway），预算不够做不出来。Tholen 的处理方式是：

> "我们现实中没时间把它做完，那不如让游戏里一个角色也没时间，发一个半成品版本。"

于是游戏里真的有个"很烂的赛车游戏"，而且成为了内行角色之间的一个梗。

**他说这是受了 Brian Eno 的"oblique strategies"里那条 "Emphasise the flaws" 的影响。**

→ **这是全文最有价值的一段素材。** 一个开发者把"做不完"本身写进了世界观。

### ② 灵感来自他打工时的一个真实客户

Tholen 在类似 Squarespace 的建站公司做过电话客服，给不会做网站的人建站。

有个客户叫 "Psychic Elizabeth Claire"（通灵师），要求网站用《Bewitched》的主题曲，还要各种侵权素材。他解释这会侵权，客户一直坚持。

后来客户被公司封号，她女儿打电话来质问。**通话中他才知道：Claire 几乎不识字。**

> "然后很多事情就说得通了。因为很多工作其实是我把她说的写下来。"

**游戏里那个通灵师页面就是这个客户。**（rockpapershotgun 一手访谈）

→ 这一段解释了为什么游戏里的"怪人"不讨厌：**每个角色的怪都有来源。**

### ③ 被砍掉的东西

Tholen 说除了动态分辨率支持和下载管理器的网格视图，几乎没有别的功能被砍。

**这个说法值得注意**：一个 4 年、7 人的项目，只砍了这些，说明范围控制得很死。

---

## 五、玩家/媒体的真实评价（这些是可以引用的原话）

**Nintendo Life**：
> "这是一个你会在一张 eerily accurate 的早期网络复制品里翻找的游戏"

**VideoGamer**：
> "每一个错别字都是故意的，每一个死链都是设计好的"

**Saving Content**：
> "你会看到有人不知道怎么做站长：留着测试文本、删不掉的图片、把连锁邮件里的图当 banner 用，因为他们相信不转发会有坏事发生"

**PC Gamer（转述）**：评论者一边玩一边在真笔记本上记名字和关键词，称它是 PC 上最好的侦探游戏之一。

**评价里出现的批评**（要写就一起写）：
- Nintendo Life：有几处"过于晦涩"（too obtuse）
- Saving Content：不得不重走已经清理过的区域，这点不喜欢
- 玩家评分 92 vs 媒体 83 的差距，也说明媒体对"晦涩"更敏感

---

## 六、衍生与后续（这部分能撑起一个"然后呢"）

| 作品 | 情况 |
|---|---|
| **Slayers X: Terminal Aftermath**（2023） | 衍生作，游戏里那个烂游戏真的做出来了 |
| **Dreamsettler** | 续作，2022 公布，**2025 年 6 月取消** |
| Hypnospace Plus | 后续更新（有 mod 提到） |
| 官方开发工具 | Page Builder + Tune Sequencer，Windows only，可做页面和音乐 |

**Dreamsettler 被取消这件事，在写"这个类型的商业现实"时很有用。**

---

## 七、可以写的角度（不是决定，是候选）

1. **"做不完"变成世界观**：那个烂赛车游戏 + Brian Eno 的 Emphasise the flaws
2. **一个通灵师客户，变成了游戏里最动人的角色**：不识字这件事改变了他看人的方式
3. **一个虚构网络需要 292 篇百科 + 131 个 mod**：这是"世界"的度量方式，不是"页面数"
4. **玩家评分 92 / 媒体 83**：媒体嫌它晦涩的地方，玩家觉得是尊重

---

## 八、待核实 / 不要写的东西

```
❌ "150+ 个假网站"  —— 无来源，我自己编的，删除
⚠️ "over 200 pages" —— 只有 grokipedia，AI 百科，需找原始出处
⚠️ Steam 评价 5,542 —— 口径不明，写"五千余条"
⚠️ 售价 $19.99 —— 是 2019 年原价，现在可能有调整
❌ 不要写"这是这个类型的开创者" —— Her Story 是 2015，比它早
```

---

## 九、一手来源清单

| 类型 | 链接 |
|---|---|
| 官方站 | https://hypnospace.net/ |
| 官方创作工具页 | https://hypnospace.net/create.html |
| 开发者一手访谈（RPS，2019-10-09） | https://www.rockpapershotgun.com/2019/10/09/how-hypnospace-outlaws-1990s-internet-was-made |
| 开发者一手访谈（RPS，起源与影响） | https://www.rockpapershotgun.com/the-influences-and-surprising-origins-of-hypnospace-outlaw |
| 2018 年早期访谈（含通灵师客户故事） | https://blog.aivanet.com/2018/04/page/36/ |
| Wiki（292 篇） | http://hypnospace.wiki.gg/ |
| Mod 索引（131 个） | https://indexgg.com/game/hypnospace/mods |