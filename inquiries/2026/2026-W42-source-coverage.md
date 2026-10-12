# 论文内容讨论记录｜2026-W42 来源覆盖与正文缺口

- **记录类型**：待正文核验
- **记录状态**：待补充
- **记录来源**：本期自动化要求记录来源均衡、软配额偏离和缺少正文的候选

## 本期检索边界

- **统计窗口**：2026-10-06 至 2026-10-12；2026-10-12 执行与核验。
- **近 4 期新收录**：W38–W41 共 40 篇，其中安全组 28 篇（70%）、软件与系统组 6 篇（15%）、人工智能组 6 篇（15%）。W38–W39 的 20 篇均来自 IEEE S&P；W40–W41 均完成 4/3/3，来源偏差已连续两期回调但仍存在。
- **轮换策略**：安全组从 CCS、NDSS、USENIX Security 开始；软件与系统组从 FSE、ASE、ISSTA 开始；人工智能组从 NeurIPS、AAAI、ICCV 开始。三组列出的会议均完成扫描，S&P 继续主动降权。
- **本期软配额**：安全组 4 篇、软件与系统组 3 篇、人工智能组 3 篇；候选池完成 4/3/3。安全组由 CCS 1 篇、NDSS 2 篇、USENIX Security 1 篇组成，单会未超过 2 篇。

## 会议来源覆盖

“初筛候选”只统计通过安全主题相关性初筛的项目，不代表会议全部论文数量。

| 来源组 | 会议 | 初筛候选 | 入选精读 | 未入选或未继续原因 |
| --- | --- | ---: | ---: | --- |
| 安全 | ACM CCS | 6 | 1 | 保留 Windows 访问控制实证研究；其余候选与近期主题重合或证据优先级较低 |
| 安全 | NDSS | 6 | 2 | 两篇分别覆盖软件供应链实践与模型窃取侧信道，达到单会软上限 |
| 安全 | USENIX Security | 5 | 1 | 保留大规模在线去匿名化研究；其余候选按来源与主题轮换暂缓 |
| 安全 | IEEE S&P | 3 | 0 | W38–W39 已连续集中收录，本期继续纠正四期来源偏差 |
| 软件与系统 | FSE | 9 | 2 | 保留 npm 漏洞 PoC 生成与安全日志研究；其余候选与本期软件供应链主题重合 |
| 软件与系统 | ASE | 8 | 1 | 保留 npm 恶意包检测器的大规模复核；其余候选优先级较低 |
| 软件与系统 | ISSTA | 5 | 0 | 两篇到期观察项仍无公开正文；其余候选的证据完整度低于入选项 |
| 软件与系统 | PLDI | 3 | 0 | 已扫描正式议程，安全贡献与本期候选相比不够直接 |
| 软件与系统 | POPL | 2 | 0 | 已扫描正式议程，未发现更适合本期的安全实证候选 |
| 软件与系统 | SOSP | 2 | 0 | 已扫描 2025 正式计划，系统安全候选与近期主题重合 |
| 软件与系统 | OOPSLA | 4 | 0 | 已扫描研究论文列表，候选安全贡献优先级较低 |
| 软件与系统 | ICSE | 4 | 0 | 已扫描 2026 研究轨及安全场次，配额内优先证据更完整的 FSE、ASE 候选 |
| 软件与系统 | OSDI | 5 | 0 | 已扫描 2026 正式议程；USEC、Timelock Drive 等候选留作后续轮换 |
| 软件与系统 | FM | 2 | 0 | 已扫描 FM 2026 正式论文集，安全相关候选缺少本期所需的直接实证贡献 |
| 人工智能 | NeurIPS | 6 | 1 | 保留计算机使用智能体安全基准 OS-Harm；其余候选与近期智能体主题重合 |
| 人工智能 | AAAI | 4 | 1 | 保留进攻性安全智能体的 CTF 评测研究；正文与正式身份齐备 |
| 人工智能 | ICCV | 3 | 1 | 保留视觉地点识别隐私防护研究；官方开放正文齐备 |
| 人工智能 | ACL | 5 | 0 | 已扫描 ACL Anthology 的智能体安全、工具层防御与安全微调论文；按轮换让位给近期较少来源 |
| 人工智能 | ICML | 6 | 0 | 已扫描 PMLR 与官方论文下载页；MOSAIC 等候选留待后续轮换 |
| 人工智能 | CVPR | 5 | 0 | 已扫描 CVF 官方开放论文集；GUI 智能体后门和隐私候选与本期主题重合 |
| 人工智能 | ICLR | 4 | 0 | 已扫描 OpenReview；部分页面仍标作投稿，未把投稿身份写成正式接收 |
| 补充 | arXiv | 7 | 0 | 用于补足作者公开正文并核对正式版本；没有以预印本身份新增候选 |

## 第二阶段精读候选

| 来源组 | 论文 | 身份证据 | 正文来源 |
| --- | --- | --- | --- |
| 安全 | Windows Plays Jenga: Uncovering Design Weaknesses in Windows File System Security | CCS 2025 正式论文、DOI 10.1145/3719027.3765217 | 作者公开 PDF |
| 安全 | Action Required: The State of GitHub Actions Security in the Wild | NDSS 2026 官方论文页、DOI 10.14722/ndss.2026.240483 | NDSS 官方 PDF |
| 安全 | Peering Inside the Black-Box: Long-Range and Scalable Model Architecture Snooping via GPU Electromagnetic Side-Channel | NDSS 2026 官方论文页、DOI 10.14722/ndss.2026.230141 | NDSS 官方 PDF |
| 安全 | Large-Scale Online Deanonymization with LLMs | USENIX Security 2026 官方论文页 | USENIX 官方 PDF |
| 软件与系统 | PoCGen: Generating Proof-of-Concept Exploits for Vulnerable npm Packages | FSE 2026 正式论文、DOI 10.1145/3808178；arXiv 2506.04962 | 作者公开 PDF |
| 软件与系统 | Secure Logging in Practice: A Taxonomy, Benchmark, and LLM-Based Analysis | FSE 2026 正式论文、DOI 10.1145/3797129；arXiv 2604.20211 | 作者公开 PDF |
| 软件与系统 | How Effective Are NPM Malicious Package Detectors? A Large-Scale Empirical Study | ASE 2026 正式论文、DOI 10.1145/3832783.3837427；arXiv 2603.27549 | 作者公开 PDF |
| 人工智能 | OS-Harm: A Benchmark for Measuring Safety of Computer Use Agents | NeurIPS 2025 Datasets and Benchmarks、DOI 10.52202/085713-1502 | NeurIPS 官方 PDF |
| 人工智能 | Towards Effective Offensive Security LLM Agents: Hyperparameter Tuning, LLM as a Judge, and a Lightweight CTF Benchmark | AAAI 2026 正式论文、DOI 10.1609/aaai.v40i35.40210；arXiv 2508.05674 | 作者公开 PDF |
| 人工智能 | VPR-Cloak: A First Look at Privacy Cloak Against Visual Place Recognition | ICCV 2025 官方开放论文集 | CVF 官方 PDF |

10 篇均已按 DOI、arXiv ID、正式 URL和规范化标题与现有索引去重；接收身份来自会议官方页面、正式论文集或 DOI，正文可用性已逐项确认。

## 待正文核验

### Ghosts in the Memory: Detecting Unintended Sensitive Data in Android Apps

- **关联论文 ID**：未入库
- **可靠来源**：ISSTA 2026 官方论文页
- **已核验事实**：官方页面确认题目、作者和 Research Papers 身份；截至 2026-10-12 仍只有摘要与会议报告入口，没有论文 PDF。
- **局限与未决问题**：无法核验 ANDROID-MRI 的内核插桩、RASP 绕过实验、50 个应用的抽样偏差和披露证据。
- **后续处理**：`papers/watchlist.jsonl` 已顺延至 2026-W43，继续复查作者版、机构仓库和 PACMSE。

### How Safe is Your Screen? Understanding and Detecting Privacy Leaks in Sensitive Activities

- **关联论文 ID**：未入库
- **可靠来源**：ISSTA 2026 官方论文页
- **已核验事实**：官方页面确认题目、作者和 Research Papers 身份；截至 2026-10-12 仍只有摘要与会议报告入口，没有论文 PDF。
- **局限与未决问题**：无法核验 ASSA 的静态分析与 LLM 判定流程、5,667 个应用的样本构造、敏感页面判定误差和披露证据。
- **后续处理**：`papers/watchlist.jsonl` 已顺延至 2026-W43，继续复查作者版、机构仓库和 PACMSE。

## 行业固定来源池扫描

| 来源 | 初筛候选 | 第二阶段保留 | 处理说明 |
| --- | ---: | ---: | --- |
| Google Project Zero | 0 | 0 | 未发现窗口内新的完整技术条目 |
| Google Threat Intelligence / Mandiant | 0 | 0 | 未发现窗口内正文和独立证据均足的新报告 |
| Microsoft Security | 3 | 1 | 保留 FORGE 大规模漏洞发现、验证与修复经验；其余条目按来源多样性排除 |
| Palo Alto Unit 42 | 2 | 0 | 已扫描技术博客，窗口内候选与近期观点库主题重合 |
| Cisco Talos | 3 | 1 | 保留 UAT-11985 对台研究机构的实时 AitM 钓鱼调查 |
| 腾讯玄武 | 0 | 0 | 归档页无窗口内新条目 |
| 腾讯科恩 | 0 | 0 | 未找到正文可访问的新技术条目 |
| Anthropic | 2 | 1 | 保留内部评测与使用中的非预期模型行动调查，精读时区分观察事实与模型动机推断 |
| OpenAI | 1 | 1 | 保留两起 AI 辅助“假前台”影响行动调查，精读时区分尝试、传播和实际影响 |
| NIST | 2 | 1 | 保留 SP 800-185 Rev. 1 初始公开草案，明确征求意见状态与 2026-12-07 截止日期 |
| CISA | 0 | 0 | 窗口内以漏洞通告和资源更新为主，缺少适合观点库的完整方法材料 |
| Gartner | 1 | 0 | 摘要与付费材料不足以核验方法和数据 |
| Forrester | 1 | 0 | 可访问内容不足以支持独立核验 |
| IDC | 0 | 0 | 未找到正文可访问且含方法或数据的新条目 |

第二阶段保留的 5 篇行业内容为：Microsoft《3 lessons from frontier AI vulnerability research》、Cisco Talos《UAT-11985: AI-assisted event lures delivering real-time Google AitM phishing》、Anthropic《Investigating unintended model actions in our evaluations and internal use》、OpenAI《Disrupting AI-enabled “false front” operations》、NIST《SHA-3 Derived Functions: Draft Revision of SP 800-185 Available for Public Comment》。它们均已按规范 URL、标题、来源和日期与现有观点库去重。
