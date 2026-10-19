# 论文内容讨论记录｜2026-W43 来源覆盖与正文缺口

- **记录类型**：待正文核验
- **记录状态**：待补充
- **记录来源**：本期自动化要求记录来源均衡、软配额偏离和缺少正文的候选

## 本期检索边界

- **统计窗口**：2026-10-13 至 2026-10-19；2026-10-19 执行与核验。
- **近 4 期新收录**：W39–W42 共 40 篇，其中安全组 22 篇（55%）、软件与系统组 9 篇（22.5%）、人工智能组 9 篇（22.5%）。W39 的 10 篇来自 IEEE S&P；W40–W42 均完成 4/3/3，来源偏差持续回调。
- **轮换策略**：安全组覆盖 IEEE S&P、ACM CCS、NDSS、USENIX Security；软件与系统组从 PLDI、POPL、SOSP/OSDI 开始并补扫 FSE、ASE、ISSTA、OOPSLA、ICSE、FM；人工智能组从 ACL、ICML、CVPR 开始并补扫 NeurIPS、AAAI、ICCV、ICLR。三组列出的会议均完成扫描。
- **本期软配额**：安全组 4 篇、软件与系统组 3 篇、人工智能组 3 篇。候选池完成 4/3/3，10 篇来自 10 个不同会议，没有单会超过 1 篇。

## 会议来源覆盖

“初筛候选”只统计通过安全主题相关性初筛的项目，不代表会议全部论文数量。

| 来源组 | 会议 | 初筛候选 | 入选精读 | 未入选或未继续原因 |
| --- | --- | ---: | ---: | --- |
| 安全 | IEEE S&P | 4 | 1 | 保留有公开作者正文的 NanoTag；Camveil 等候选正文不足或与近期主题重合 |
| 安全 | ACM CCS | 5 | 1 | 保留 SSH 严格密钥交换状态学习；其余候选按主题轮换暂缓 |
| 安全 | NDSS | 5 | 1 | 保留桌面密码管理器 UI 攻击；其余候选优先级较低 |
| 安全 | USENIX Security | 6 | 1 | 保留后门大模型事后修补；其余候选与近期智能体安全主题重合 |
| 软件与系统 | PLDI | 4 | 1 | 保留反汇编前静态二进制分析；正式全文 HTML 可核验 |
| 软件与系统 | POPL | 3 | 1 | 保留以次结构依赖追踪表达安全推理的 Distinguished Paper |
| 软件与系统 | OSDI | 5 | 1 | 保留加密且可问责的协同编辑系统；官方开放正文齐备 |
| 软件与系统 | SOSP | 2 | 0 | 扫描正式计划，候选与近期系统安全主题重合 |
| 软件与系统 | FSE | 5 | 0 | W42 已集中收录，本期主动轮换 |
| 软件与系统 | ASE | 4 | 0 | W42 已收录，未发现证据优先级高于入选项的新增候选 |
| 软件与系统 | ISSTA | 5 | 0 | 两篇观察项仍缺公开正文；其余候选证据完整度较低 |
| 软件与系统 | OOPSLA | 3 | 0 | 已扫描研究论文列表，安全贡献优先级低于 PLDI、POPL |
| 软件与系统 | ICSE | 4 | 0 | 已扫描 2026 研究轨及安全场次，本期按会议轮换暂缓 |
| 软件与系统 | FM | 2 | 0 | 安全相关候选缺少本期所需的直接实证贡献 |
| 人工智能 | ACL | 6 | 1 | 保留多智能体系统的合取提示攻击；官方 Anthology 正文齐备 |
| 人工智能 | ICML | 5 | 1 | 保留上下文隐私的多智能体偏好训练；PMLR 正文齐备 |
| 人工智能 | CVPR | 4 | 1 | 保留具身智能体危险指令安全基准；CVF 正式身份与正文齐备 |
| 人工智能 | NeurIPS | 5 | 0 | W42 已收录计算机使用智能体安全基准，本期主动轮换 |
| 人工智能 | AAAI | 4 | 0 | W42 已收录进攻性安全智能体评测，本期主动轮换 |
| 人工智能 | ICCV | 3 | 0 | W42 已收录视觉隐私候选，本期主动轮换 |
| 人工智能 | ICLR | 4 | 0 | 部分 OpenReview 页面仍无法可靠区分投稿与正式接收，未写成接收事实 |
| 补充 | arXiv | 8 | 0 | 用于取得作者正文和核对版本；没有以预印本身份新增候选 |

## 第二阶段精读候选

| 来源组 | 论文 | 身份证据 | 正文来源 |
| --- | --- | --- | --- |
| 安全 | NanoTag: Systems Support for Efficient Byte-Granular Overflow Detection on ARM MTE | IEEE S&P 2026 官方接收/工件页；arXiv 2509.22027 | 作者公开 PDF |
| 安全 | Finding SSH Strict Key Exchange Violations by State Learning | CCS 2025 正式论文、DOI 10.1145/3719027.3765208；arXiv 2509.10895 | arXiv 作者正文 |
| 安全 | Vault Raider: Stealthy UI-based Attacks Against Password Managers in Desktop Environments | NDSS 2026 官方论文页、DOI 10.14722/ndss.2026.231067 | NDSS 官方 PDF |
| 安全 | Patcher: Post-Hoc Patching of Backdoored Large Language Models | USENIX Security 2026 官方论文页 | USENIX 官方 PDF |
| 软件与系统 | Analyzing Bytes: Pre-Disassembly Static Binary Analysis | PLDI 2026 正式论文、DOI 10.1145/3808292 | ACM 正式全文 HTML；Google Research 元数据页 |
| 软件与系统 | Security Reasoning via Substructural Dependency Tracking | POPL 2026 Distinguished Paper、DOI 10.1145/3776669 | 作者公开 PDF |
| 软件与系统 | Acumen: A Platform for Encrypted and Accountable Collaborative Editing | OSDI 2026 官方论文页 | USENIX 官方 PDF |
| 人工智能 | Conjunctive Prompt Attacks in Multi-Agent LLM Systems | ACL 2026 长文、DOI 10.18653/v1/2026.acl-long.1577 | ACL Anthology 官方 PDF |
| 人工智能 | PrivAct: Internalizing Contextual Privacy Preservation via Multi-Agent Preference Training | ICML 2026 PMLR 306 | PMLR 官方 PDF |
| 人工智能 | AGENTSAFE: Benchmarking the Safety of Embodied Agents on Hazardous Instructions | CVPR 2026 官方开放论文集 | CVF/arXiv 作者正文 |

10 篇均已按 DOI、arXiv ID、正式 URL 和规范化标题与现有索引去重；接收身份来自会议官方页面、正式论文集或 DOI。PLDI 论文的 PDF 下载端点对自动访问返回 403，正式 ACM 全文 HTML 内容完整，足以执行全文精读；其余 9 篇 PDF 均已逐项确认可打开。

## 待正文核验

### Ghosts in the Memory: Detecting Unintended Sensitive Data in Android Apps

- **关联论文 ID**：未入库
- **可靠来源**：ISSTA 2026 官方论文页、作者实验室公开页面
- **已核验事实**：官方页面确认题目、作者和 Research Papers 身份；截至 2026-10-19 仍只有摘要与报告入口，没有公开论文 PDF。
- **局限与未决问题**：无法核验 ANDROID-MRI 的内核插桩、RASP 绕过实验、50 个应用的抽样偏差和 17 个披露的验证链。
- **后续处理**：`papers/watchlist.jsonl` 已顺延至 2026-W44。

### How Safe is Your Screen? Understanding and Detecting Privacy Leaks in Sensitive Activities

- **关联论文 ID**：未入库
- **可靠来源**：ISSTA 2026 官方论文页、作者实验室公开页面
- **已核验事实**：官方页面确认题目、作者和 Research Papers 身份；截至 2026-10-19 仍只有摘要与报告入口，没有公开论文 PDF。
- **局限与未决问题**：无法核验 ASSA 的静态分析与 LLM 判定流程、5,667 个应用的样本构造、敏感页面判定误差和披露证据。
- **后续处理**：`papers/watchlist.jsonl` 已顺延至 2026-W44。

### Towards Long-Horizon Agents: A Survey

- **关联论文 ID**：未入库
- **可靠来源**：Preprints DOI、项目仓库与 OpenReview 正文
- **已核验事实**：项目方预告 2026 年 11 月初更新；截至 2026-10-19 仍为 v1 预印本，安全、验证和可信性是广义综述主题。
- **局限与未决问题**：缺少独立安全方法、威胁模型或安全实证，当前不足以作为安全论文收录。
- **后续处理**：`papers/watchlist.jsonl` 顺延至 2026-W46，核验预告更新。

## 行业固定来源池扫描

| 来源 | 初筛候选 | 第二阶段保留 | 处理说明 |
| --- | ---: | ---: | --- |
| Google Project Zero | 0 | 0 | 窗口内没有新的完整技术条目 |
| Google Threat Intelligence / Mandiant | 0 | 0 | 窗口内没有正文与独立证据均足的新报告 |
| Microsoft Security | 1 | 0 | 最新实质条目早于本窗口，避免重复近期观点 |
| Palo Alto Unit 42 | 4 | 3 | 保留 Linux 间谍活动、PEERSTITCH FortiGate 植入与第三方风险三项调查；同源偏高在下方说明 |
| Cisco Talos | 3 | 1 | 保留哈萨克斯坦关联 UAT-6275 对独联体政府机构的攻击调查 |
| 腾讯玄武 | 0 | 0 | 归档页无窗口内新条目 |
| 腾讯科恩 | 0 | 0 | 未找到正文可访问的新技术条目 |
| Anthropic | 2 | 1 | 保留美国中期选举准备与对抗测试说明，精读时限定抽样与归因边界 |
| OpenAI | 1 | 0 | 最新实质安全条目早于窗口，避免重复近期观点 |
| NIST | 1 | 0 | 窗口内更新以计划和征求意见材料为主，没有优于候选的实证内容 |
| CISA | 1 | 0 | 以漏洞通告和资源更新为主，缺少适合观点库的完整方法材料 |
| Gartner | 1 | 0 | 摘要与付费材料不足以核验方法和数据 |
| Forrester | 1 | 0 | 可访问内容不足以支持独立核验 |
| IDC | 0 | 0 | 未找到正文可访问且含方法或数据的新条目 |

第二阶段保留 5 篇行业内容：Unit 42《AI-Powered Espionage Campaign Targets Government Linux Infrastructure》《Unit 42 Uncovers PEERSTITCH, a Stealthy FortiGate Implant》《The Noise Inside the Network: How an Unsophisticated Attack Exposed a Third-Party Risk》、Cisco Talos《Break the silence: Kazakhstan-nexus UAT-6275 targets CIS government organizations》、Anthropic《Preparing for the 2026 US midterms》。三篇来自 Unit 42，偏离通常的来源分散目标；原因是固定池内只有这三篇、Talos 一篇和 Anthropic 一篇同时满足窗口、正文、方法与证据要求，其他来源没有可核验的新材料。五篇均已按规范 URL、标题、来源和日期与现有观点库去重。

## 实体待核验

- *AGENTSAFE* 的论文署名使用 `Institute of Dataspace`，公开出版页能确认其位于中国，但本次未找到可一一对应的机构官方中文全称，实体表暂保留英文。
- Zonghao Ying、Le Wang、Yisong Xiao、Yuqing Ma、Jinyang Guo、Aishan Liu、Jiakai Wang、Xianglong Liu、Zhenfei Yin 与 Mingchuan Zhang 均按 CVF 正式论文署名建立稳定实体；未找到能把英文署名与官方中文姓名一一对应的页面，因此不猜测中文名。
