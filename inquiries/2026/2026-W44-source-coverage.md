# 论文内容讨论记录｜2026-W44 来源覆盖与正文缺口

- **记录类型**：待正文核验
- **记录状态**：待补充
- **记录来源**：本期自动化要求记录来源均衡、软配额偏离和缺少正文的候选

## 本期检索边界

- **统计窗口**：2026-10-20 至 2026-10-26；2026-10-26 执行与核验。
- **近 4 期新收录**：W40–W43 共 40 篇，其中安全组 16 篇（40%）、软件与系统组 12 篇（30%）、人工智能组 12 篇（30%）。四期均完成 4/3/3，早期单一会议偏差已连续回调。
- **轮换策略**：安全组从 ACM CCS、NDSS、USENIX Security、IEEE S&P 开始；软件与系统组从 FSE、OOPSLA、ICSE 开始并补扫 PLDI、POPL、SOSP、ASE、ISSTA、OSDI、FM；人工智能组从 NeurIPS、AAAI、ICLR 开始并补扫 ACL、CVPR、ICCV、ICML。三组列出的会议均完成扫描。
- **本期软配额**：安全组 4 篇、软件与系统组 3 篇、人工智能组 3 篇。候选池完成 4/3/3；安全组覆盖四个会议，人工智能组因正式身份、正文与主题优先级由 NeurIPS 收录 2 篇，原因在下表说明。

## 会议来源覆盖

“初筛候选”只统计通过安全主题相关性初筛的项目，不代表会议全部论文数量。

| 来源组 | 会议 | 初筛候选 | 入选精读 | 未入选或未继续原因 |
| --- | --- | ---: | ---: | --- |
| 安全 | ACM CCS | 5 | 1 | 保留 CSS 单次渲染窃取加密邮件明文研究；其余候选与近期主题重合或优先级较低 |
| 安全 | NDSS | 6 | 1 | 保留多来源顺序未知场景下的提示注入；其余候选按主题轮换暂缓 |
| 安全 | USENIX Security | 6 | 1 | 保留不可闻近超声语音越狱研究；其余候选与近期智能体主题重合 |
| 安全 | IEEE S&P | 5 | 1 | 保留智能体浏览器进程隔离研究；Camveil 只有正式摘要且公开正文不足，未进入精读 |
| 软件与系统 | FSE | 7 | 1 | 保留二进制相似性用于真实固件漏洞检测的大规模实证；其余候选按主题轮换 |
| 软件与系统 | OOPSLA | 4 | 1 | 保留把路径分段为逻辑单元的漏洞检测研究；其余候选安全贡献较间接 |
| 软件与系统 | ICSE | 6 | 1 | 保留从 LLM 输出到敏感 sink 的静态污点分析；其余候选优先级较低 |
| 软件与系统 | PLDI | 4 | 0 | W43 已收录，主动轮换 |
| 软件与系统 | POPL | 3 | 0 | W43 已收录，主动轮换 |
| 软件与系统 | SOSP | 2 | 0 | 正式计划中的安全候选与近期系统安全主题重合 |
| 软件与系统 | ASE | 5 | 0 | W42 已收录，未发现证据优先级高于入选项的新增候选 |
| 软件与系统 | ISSTA | 5 | 0 | 两篇观察项仍缺公开正文；其余候选的正文或证据完整度较低 |
| 软件与系统 | OSDI | 5 | 0 | W43 已收录，主动轮换 |
| 软件与系统 | FM | 2 | 0 | 安全相关候选缺少本期所需的直接实证贡献 |
| 人工智能 | NeurIPS | 6 | 2 | 保留真实软件安全任务自动基准与 Web 智能体端到端提示注入基准；二者分别覆盖代码安全与网页操作 |
| 人工智能 | AAAI | 5 | 1 | 保留真实 MCP 服务器工具投毒基准；正式正文与数据规模齐备 |
| 人工智能 | ICLR | 4 | 0 | OpenReview 自动访问仍受挑战页限制，无法稳定核验部分候选的接收身份 |
| 人工智能 | ACL | 5 | 0 | W43 已收录，主动轮换 |
| 人工智能 | CVPR | 4 | 0 | W43 已收录，主动轮换 |
| 人工智能 | ICCV | 3 | 0 | W42 已收录，未发现优先级更高的新候选 |
| 人工智能 | ICML | 5 | 0 | W43 已收录，主动轮换 |
| 补充 | arXiv | 8 | 0 | 用于取得作者正文、核对版本和正式身份；没有以预印本身份新增候选 |

## 第二阶段精读候选

| 来源组 | 论文 | 身份证据 | 正文来源 |
| --- | --- | --- | --- |
| 安全 | Site Isolation is Dead: How Site Isolation is Broken in Agentic Browsers and Extensions | IEEE S&P 2026 官方接收页、DOI 10.1109/SP63933.2026.00241 | 作者实验室公开 PDF |
| 安全 | Styled to Steal: The Overlooked Attack Surface in Email Clients | CCS 2025 正式论文、DOI 10.1145/3719027.3765189 | 作者公开 PDF |
| 安全 | ObliInjection: Order-Oblivious Prompt Injection Attack to LLM Agents with Multi-source Data | NDSS 2026 官方论文页、DOI 10.14722/ndss.2026.240702；arXiv 2512.09321 | NDSS/arXiv 公开 PDF |
| 安全 | Sirens' Whisper: Inaudible Near-Ultrasonic Jailbreaks of Speech-Driven LLMs | USENIX Security 2026 官方论文页 | USENIX 官方 PDF |
| 软件与系统 | Understanding Binary Code Similarity for Real-World Vulnerability Detection: A Large-Scale Empirical Study | FSE 2026 Research Papers 官方页；arXiv 2606.28870 | 会议链接的 arXiv 作者正文 |
| 软件与系统 | Reframing Paths as Logic: Semantic Segmentation for Vulnerability Detection | OOPSLA 2026 / PACMPL，DOI 10.1145/3798272 | 南洋理工大学机构仓储中的作者全文 |
| 软件与系统 | TaintP2X: Detecting Taint-Style Prompt-to-Anything Injection Vulnerabilities in LLM-Integrated Applications | ICSE 2026 Research Track，DOI 10.1145/3744916.3773199 | 作者公开 PDF |
| 人工智能 | SEC-bench: Automated Benchmarking of LLM Agents on Real-World Software Security Tasks | NeurIPS 2025 正式论文集、DOI 10.52202/085713-3878；arXiv 2506.11791 | NeurIPS 官方 PDF |
| 人工智能 | MCPTox: A Benchmark for Tool Poisoning on Real-World MCP Servers | AAAI 2026 正式论文、DOI 10.1609/aaai.v40i42.40895；arXiv 2508.14925 | AAAI 官方 PDF |
| 人工智能 | WASP: Benchmarking Web Agent Security Against Prompt Injection Attacks | NeurIPS 2025 正式论文集；arXiv 2504.18575 | arXiv 作者正文与官方工件 |

10 篇均已按 DOI、arXiv ID、正式 URL 和规范化标题与现有索引去重；接收身份来自会议官方页面、正式论文集或 DOI。Camveil 因公开全文门槛未通过而被同会议候选替换；最终 10 篇均已确认存在可完整读取的公开正文，并于第二阶段逐篇核对方法、实验、局限和作者单位后写入 2026-W44 周报。

## 待正文核验

### Ghosts in the Memory: Detecting Unintended Sensitive Data in Android Apps

- **关联论文 ID**：未入库
- **可靠来源**：ISSTA 2026 官方论文页、作者与机构公开入口
- **已核验事实**：官方页面确认题目、作者和 Research Papers 身份；截至 2026-10-26 仍只有摘要与报告入口，没有公开论文 PDF。
- **局限与未决问题**：无法核验 ANDROID-MRI 的内核插桩、RASP 绕过实验、50 个应用的抽样偏差和 17 个披露的验证链。
- **后续处理**：`papers/watchlist.jsonl` 已顺延至 2026-W45。

### How Safe is Your Screen? Understanding and Detecting Privacy Leaks in Sensitive Activities

- **关联论文 ID**：未入库
- **可靠来源**：ISSTA 2026 官方论文页、作者与机构公开入口
- **已核验事实**：官方页面确认题目、作者和 Research Papers 身份；截至 2026-10-26 仍只有摘要与报告入口，没有公开论文 PDF。
- **局限与未决问题**：无法核验 ASSA 的静态分析与 LLM 判定流程、5,667 个应用的样本构造、敏感页面判定误差和披露证据。
- **后续处理**：`papers/watchlist.jsonl` 已顺延至 2026-W45。

## 行业固定来源池扫描

| 来源 | 初筛候选 | 第二阶段保留 | 处理说明 |
| --- | ---: | ---: | --- |
| Google Project Zero | 1 | 1 | 保留紧急漏洞修复通道的工程综述；虽早于本期窗口，方法与实例完整，可作为基线 |
| Google Threat Intelligence / Mandiant | 1 | 1 | 保留 ARMORY CASTLE 利用 BeyondTrust 零日漏洞的事件响应调查 |
| Microsoft Security | 1 | 0 | 10 月 19 日智能体内部人风险条目偏产品叙事，证据优先级低于保留项 |
| Palo Alto Unit 42 | 0 | 0 | 窗口内没有新的完整技术调查，避免重复 W43 三篇同源材料 |
| Cisco Talos | 0 | 0 | 窗口内没有正文与独立证据均足的新报告 |
| 腾讯玄武 | 0 | 0 | 归档页无窗口内新条目 |
| 腾讯科恩 | 0 | 0 | 未找到正文可访问的新技术条目 |
| Anthropic | 1 | 1 | 保留自评式滥用检测研究；随机生产流量评测、误报率和局限说明齐备 |
| OpenAI | 2 | 2 | 保留前沿训练环境隔离红队与 PHP 漏洞全球协同修复两项；主题分别覆盖训练基础设施和开源应急响应 |
| NIST | 0 | 0 | 窗口内没有优于候选的完整方法或数据材料 |
| CISA | 1 | 0 | 以漏洞通告和资源更新为主，缺少适合观点库的完整方法材料 |
| Gartner | 1 | 0 | 摘要与付费材料不足以核验方法和数据 |
| Forrester | 1 | 0 | 可访问内容以活动和摘要为主，无法支持独立核验 |
| IDC | 0 | 0 | 未找到正文可访问且含方法或数据的新条目 |

第二阶段保留 5 篇行业内容：OpenAI《Securing our frontier model training environment》《Patch the Planet: global response coordination as agents uncover critical vulnerabilities》、Anthropic《Scaling Misuse Detection with Self-Assessment》、Google Threat Intelligence / Mandiant《ARMORY CASTLE Exploits BeyondTrust》、Google Project Zero《How to fix a bug in a fix》。OpenAI 占 2 篇；原因是本期窗口内只有这两篇新材料同时提供完整正文、工程方法与可核验行动链，另外三篇用于补足监测、事件响应和紧急修复通道。五篇均已按规范 URL、标题、来源和日期与现有观点库去重。

## 历史状态回查

- 复核范围为索引内 7 篇 `preprint-unreviewed` 与 1 篇 workshop 论文。*Agent Data Injection Attacks are Realistic Threats to AI Agents*、*Bad Memory*、*Self-State Attacks*、*RECEIPT*、*MemSecBench* 与 *Not an A11y* 的作者页面、arXiv 和公开检索仍只支持预印本身份。
- *Adaptive Adversaries* 已由 NeurIPS 2026 官方页面确认 Agents in the Wild workshop 身份，状态无需调整。
- *IssueTrojanBench* 的作者工件仓库给出 ASE 2026 proceedings 引用，但 ASE 2026 Research Papers 官方页面、ACM Digital Library 与 IEEE Xplore 均未找到可核验的论文条目。当前保留 `preprint-unreviewed`，待出现会议正式页面或 DOI 后再更新。

## 实体核验结果

- Site Isolation 论文的机构身份可由论文首页和官方元数据核验；作者中文姓名缺少可一一对应的官方页面，实体表将保留英文署名。
- FSE、OOPSLA、ICSE 与三篇人工智能论文的新作者先按正式论文署名建立稳定实体；仅在存在作者主页、机构页面或可靠出版记录时补充中文名，避免音译猜测。
- USENIX Security 论文首页把 Zijian Ling 与 Man Zhou 同时列于华中科技大学和 State Key Laboratory of Internet Architecture。清华大学官方页面确认其中文全称为“互联网体系结构全国重点实验室”，周报和实体表已据此修正；作者仍保留论文英文署名。
