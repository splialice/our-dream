# Art-style 类页面模板 v2.1（从 Cuphead 与两轮审查修订）

用途：一个游戏回答一个具体问题（「这个画风叫什么、怎么做出来的」）。结构固定，证据和结论每篇独立。模板约束研究流程，不替代研究。

v2 相对 v1：收紧否定性结论；固定六节改为五个核心区块 + 可选模块；拆分 `source_type` 与 `claim_usage`；去掉强制制造误解；增加「是否值得独立建页」门槛。

v2.1 相对 v2：`statement` 与逐字引语分离，新增 `supporting_quote`；无命名判断改用 `reviewed_source_ids` 多来源声明；Short answer 改为 2–4 句、不超过 100 英文词；末节标题统一为 `## Sources and evidence limits`。

## 一、建页前的发布门槛（三问全过才建 URL）

| 检查 | 通过条件 |
|---|---|
| 搜索问题独立吗？ | 用户有一个不能被现有文章直接完整回答的问题 |
| 答案独立吗？ | 有自己的核心结论，不是其他文章的局部改写 |
| 证据独立吗？ | 至少有一条与该问题直接相关的独特证据或解释 |

目的：防止关键词蚕食和高度相似页面。`cuphead art style` 与 `cuphead rubber hose animation` 可能由同一篇覆盖；`cuphead art style` 与 `how cuphead was animated` 是否拆开，要看 SERP 和实际内容深度。

不要因为搜索词不同就建多个 URL。**一个页面覆盖一个问题簇。**

## 二、Front matter 固定字段

```yaml
---
title: "What Is the <Game> Art Style? <核心区分点>"
slug: "<game>-art-style"
date: YYYY-MM-DD
type: "art-style"
primary_keyword: "<game> art style"
primary_question: "What is the <Game> art style called, and how was it made?"
answer: "2–4 句、不超过 100 个英文词。只陈述来源支持的内容：有官方名称就写名称；没有找到就写「在查阅的这些来源里，团队描述的是技法与参考，未呈现独家命名」。"
evidence_status: "verified | partial | contested"
primary_sources:
  - id: "source-1"
    title: "..."
    author: "...（含采访者）"
    published: "YYYY-MM-DD"
    source_type: "developer_interview"
    url: "..."
claims:
  - statement: "想证明的事实（可以是概括，不是逐字引语）"
    source_id: "source-1"
    claim_usage: "paraphrase"
    supporting_quote: "来源中的实际原文；claim_usage 为 direct_quote / paraphrase / reporter_paraphrase_plus_direct_quote 时必填"
  - statement: "在查阅的来源里没有找到独家命名"
    claim_usage: "absence_in_reviewed_sources"
    reviewed_source_ids: ["source-1", "source-2", "source-3"]
last_verified: YYYY-MM-DD
---
```

字段说明：

- `answer` 第一屏给结论，同时供以后生成 Q&A / FAQ 结构化数据。**2–4 句、不超过 100 个英文词**：句数太少装不下必要边界，太长会把正文塞进摘要。
- `statement` 是**你想证明的事实**，允许是概括，不要求逐字出现在来源里。
- `supporting_quote` 是**来源中的实际原文**。凡 `claim_usage` 为 `direct_quote`、`paraphrase`、`reporter_paraphrase_plus_direct_quote`、`developer_written_description` 都必须填；脚本应检查它确实能在对应来源中定位到。这样 `statement` 是概括也不会被误判成逐字引语。
- `source_type` 标准化取值：`developer_document`、`developer_interview`、`official_store`、`contemporary_reporting`、`retrospective_reporting`。描述**材料本身是什么**。
- `claim_usage` 标准化取值：`direct_quote`、`paraphrase`、`reporter_paraphrase`、`reporter_paraphrase_plus_direct_quote`、`developer_written_description`、`absence_in_reviewed_sources`。描述**文章怎么使用这份材料**。
- 两个维度分开，避免把「采访里有开发者引语」和「独立取得的开发者原始文档」混为一谈。
- `evidence_status: contested` 的页面不能用 `verified` 的语气发布。

**否定性结论的写法**：不要写「工作室从没给画风起名」这类绝对命题，除非有来源直接证明。改写为「在本文查阅的这些来源里，团队描述的是技法与参考，未呈现独家命名」，并说明这份调查的范围边界。

**无命名判断的证据结构**：`absence_in_reviewed_sources` 用 `reviewed_source_ids` 列出**这次调查实际看过的全部来源**，不挂单一 `source_id`。因为「没找到」是跨来源的调查结论，不是某篇采访单独证明的。正文必须写出调查范围。这与「开发者明确否认存在名称」是两种不同强度的证据，不能混用。

## 三、正文：五个核心区块（顺序固定）+ 可选模块

| # | 区块 | 回答的问题 | 最低要求 |
|---|---|---|---|
| 1 | `## Short answer` | 叫什么？怎么做？ | 2–4 句、不超过 100 英文词，只用来源支持的话；给出最重要的区分点 |
| 2 | `## What it looks like` | 可观察特征是什么？ | 至少 3 个具体特征，配开发者原话或同期材料 |
| 3 | `## What the developers said` | 开发者自己怎么描述？ | 原话 + 日期 + 直达原文链接；区分「来源里没找到命名」与「证明不存在命名」 |
| 4 | 流程标题（见下） | 制作流程、开发决策或参考来源 | 按证据类型选标题，至少 1 个反直觉细节作为信息增量 |
| 5 | `## Sources and evidence limits` | 引文来自哪里、哪些不能确定 | 按日期列来源，标一手/二手、原话/转述；写清证据边界 |

流程标题按证据类型选，不强行统一：

- `## How it was made` — 有具体制作流程和技术资料（Cuphead）
- `## How the look was developed` — 资料主要是开发决策、时间线、回顾性访谈（Wind Waker）
- `## How the visual direction was developed` — 资料主要是参考来源与概念设计，没有单一技术（Dishonored）

不要为了填这个章节编写没有来源的渲染细节。材料里有什么就写什么，标题跟材料走。

**可选模块**（有证据才加，不为填空而写）：`Common confusions`、`Timeline`、`Visual comparison`、`Who designed it`。

关于 `Common confusions`：只写**确实有证据或真实搜索需求**的混淆。不要把作者自己的技术对比包装成「社区误传」。Cuphead 样稿里的「不是 a filter」已明确标注为编辑比较，不是 documented community claim——照这个标准写。

## 四、每篇放行条件

1. **直接回答**：第一屏能回答 `primary_question`。
2. **一手材料 ≥1**：开发者访谈、官方技术文章、会议论文、开发者写的商店描述——至少一份真正相关。
3. **非平凡事实 ≥2**：不是百科级描述，而是有来源的具体细节（如 Cuphead 的 cel test、boss 先于动画）。
4. **信息增量 ≥1**：现有搜索结果没说清、而这篇能说清的点。
5. **视觉证据**（如有）：原始截图、幻灯片、自制对照图；纯装饰不算。
6. **来源可追溯**：每条关键断言有 source_id + 日期 + 类型；转述不冒充原话。
7. **内链 2–4 条**：只链真正相关的，不堆链接。
8. **不重复**：不是「换个游戏名」的同义复写。

任一不满足 → 不建独立页，把事实并入已有文章或放弃。

## 五、什么能固定、什么绝不能固定

**能固定**：结构、字段、检查规则、发布流程。

**绝不能固定**：事实、引语、结论、参考对象。每篇必须重新研究、重新填 `primary_sources` 和 `claims`。如果两篇的 claims 高度相似，说明模板被用成了内容农场——砍掉其中一篇。

不要把模板套成「X art style → 灵感来自 Y 年代 → 手绘 → 影响了很多游戏」的填空题。Cuphead 样稿站得住，因为有具体的人（Chad / Jared）、具体的片子（*Swing You Sinners*）、具体的制作顺序（boss 先于动画）、具体的物理证据（扫描的灰尘和毛发），并明确告诉读者它与 cel shading 的关系。

## 六、质量检查分两层

### 第一层：自动结构校验（`validate_article.py`）

运行：`pip install -r requirements.txt` 然后 `python validate_article.py --all`。

脚本内置 schema，**不读取模板文字**——改模板措辞不会意外改变校验规则。它检查：

- front matter 必填字段、`evidence_status` 合法取值、日期格式。
- 每条来源的 `id` / `title` / `author` / `published` / `source_type` / `url` 齐全，URL 格式合法，日期已排序，id 不重复。
- `claim_usage` 必须是允许枚举中的值；不允许的值会被拒绝。
- 普通 claim 的 `source_id` 必须存在；`claim_usage` 需要引语时，`supporting_quote` 必须是非空字符串。
- `absence_in_reviewed_sources` 用 `reviewed_source_ids`，不挂单一 `source_id`。
- 正文五个核心区块：`## Short answer` / `## What it looks like` / `## What the developers said` / 一个流程标题（`How it was made` 或 `How the look was developed` 或 `How the visual direction was developed`）/ `## Sources and evidence limits`。
- `Short answer` 2–4 句、不超过 100 英文词；`answer` 字段不超过 100 词。

**脚本只查结构，不证明引语是真的。** 它无法知道 `supporting_quote` 是否真的出现在来源里、归属是否正确、回顾性访谈是否被当成同期记录。

### 第二层：人工史实核查

每篇发布前必须人工做：

1. 打开每条来源原文，确认 `supporting_quote` 确实存在且归属正确。
2. 确认 `statement` 没有超出引语能支持的范围。
3. 确认回顾性 / 同期 / 发行前的证据类型没有混用。
4. 确认 `absence_in_reviewed_sources` 的调查范围与正文陈述一致。

### 生成页面检查（`check_site.py`，复用主站检查器）

canonical / og:url / description 唯一性、内链、404、sitemap——在站点构建后运行，与上面的文章级校验分开。

**来源重复不是硬性拒绝条件**。同一 GDC 演讲支持画风名称、技术实现、设计决策多个不同问题是正常的。要检测的是「同一证据被重复包装为没有独立信息增量的页面」，不是 URL 重复本身。

## 七、技术注意

Hugo 中 `type: art-style` 会改变页面查找和渲染模板选择，实验站需要确认有对应 layout 或明确回退行为。`claims`、`evidence_status` 等自定义字段必须在构建脚本里真实读取和校验，不能只存在于 Markdown 文本里。

## 八、下一批关键词（重新分级后）

| 关键词 | SV | 研究准备 | 决定 |
|---|---|---|---|
| `wind waker art style` | 150 | 有 Nintendo Iwata Asks 一手访谈 | 下一篇，样板 2 |
| `dishonored art style` | 30 | 待找 Arkane 一手访谈 | 样板 3 候选，先研究 |
| `okami art style` | 90 | 开发者访谈待找；美术职责需按具体人核实 | 待研究 |
| `jet set radio art style` | 150 | 只有 Sega Retro 年代记录 | 暂缓——年代记录证明不了「叫什么、怎么做」 |

SV / KD 来自 2026-11-17 的 Ahrefs 记录，未独立重新测量。

## 九、验证节奏

先做 3 篇样板，不急着铺 10 篇：

1. **Cuphead** — 传统动画技术、开发者原话、术语混淆
2. **The Wind Waker** — 开发者决策、视觉转型时间线、后来的美术解释
3. **Dishonored** — 没有简单技术标签时，模板能否靠开发者访谈解释美术方向

三篇代表三种史料结构。若能在不强迫章节、不补无来源结论的情况下完成，模板才算通过测试，再考虑扩到 10 篇、30 篇。
