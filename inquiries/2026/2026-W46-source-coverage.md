# 2026-W46 来源覆盖与核验记录

窗口为 2026-11-03—11-09（北京时间），实际补刊与回查在 2026-11-16。W45 已先完成推送、Pages 成功和线上数据核验（`c3d5e0b`，工作流 43831479247）。本期仍按检索、原文精读与同步 Easycatch、维护验证与发布三阶段串行执行。

## 输入、近四期分布与配额

重新读取检索分片；完整加载当前 151 条索引、3 条观察队列、14 个固定行业来源、67 条行业记录，检查最新 W45 周报与运行前七个用户改动。用户补丁与运行前相同，继续排除在本期提交外。

W42—W45 新增来源为安全 13、软件与系统 10、AI 10，共 33 篇，占 39.4% / 30.3% / 30.3%。会议分布：CCS 3、NDSS 5、USENIX Security 3、S&P 2、FSE 3、ASE 1、PLDI 1、POPL 1、OSDI 2、OOPSLA 1、ICSE 1、NeurIPS 4、AAAI 2、ICCV 1、ACL 1、ICML 1、CVPR 1。ICLR、SOSP、FM 在这四期未新增；扫描和选题时优先检查这些缺口。

本期继续三篇专题精读，安全 / 软件与系统 / AI 为 1/1/1，各 33.3%；相对十篇软目标缺 3/2/2。入选 Anota（NDSS）、Osprey（OSDI）、AgentHarm（ICLR）。分期处理既定全文候选，避免把未完成原文核对的条目算作精读；这是编辑范围选择，不能解释为其他来源没有可读论文。ICLR 补齐近期来源缺口，OSDI 的隐私计算内存机制补充既有程序分析和加密协作。剩余 SymCC、iLand、CaMeL 留至下一期，IJON 暂缓。

## 三组会议扫描

本期先检查 AI 组，再检查安全与软件系统组；组内优先入口轮换为 ICML、CCS、POPL。目录访问与论文题目筛选分开记录；候选数只统计明确推进项，非整个会议的安全论文数量。

| 会议 | 本次入口、题目筛选与结果 | 候选 / 入选 |
| --- | --- | --- |
| ICML | PMLR 目录与 PrivAct 官方条目；已收录 W43 | 0 / 0 |
| ICLR | 2026 海报列表（harmful prompt sanitization、source inference）；AgentHarm 2025 正式论文集，完整 PDF 已取得 | 1 / 1 |
| AAAI | 归档页返回机器人验证；用 MCPTox 官方具体文章替代，已收录 | 0 / 0 |
| NeurIPS | 2025 论文集及 AgentDojo 正式条目；重复 | 0 / 0 |
| ACL | 完整目录下载超时；改查 Fingerprinting LLMs via Prompt Injection，未推进正文 | 0 / 0 |
| CVPR | 官方 V-Attack、HAM3 条目，未推进视觉攻击精读 | 0 / 0 |
| ICCV | JailbreakDiffBench、Shuffle Inconsistency 官方条目，未推进正文 | 0 / 0 |
| CCS | 2026 接收列表和既有 2025 索引；无本期新增全文候选 | 0 / 0 |
| NDSS | 2026 接收列表、Anota 官方页与 PDF；SAGA 已在 W45 收录 | 1 / 1 |
| USENIX Security | 2026 技术程序；SymCC 官方全文留后续基线 | 1 / 0 |
| IEEE S&P | 2026 接收列表与 IJON 历史 DOI；IJON 暂缓 | 1 / 0 |
| POPL | 官方研究列表，Security Reasoning 已收录 | 0 / 0 |
| PLDI | 自动拼接的 track 路径 404；以官方 Analyzing Bytes 条目替代，已收录 | 0 / 0 |
| FSE | 官方研究列表，PoCGen、Secure Logging 与二进制相似性均已收录 | 0 / 0 |
| SOSP | 2026 接收入口可访问；对照 2025 的 eBPF oracle 与 proof-guided kernel analysis，未推进全文 | 0 / 0 |
| OOPSLA | SPLASH 2026 正确入口，constant-time、Spectre、dynamic release；SEVDF 已收录 | 0 / 0 |
| ASE | 官方研究列表，npm 检测重复，AgentChaos 与 LLM-native IDEs 未推进全文 | 0 / 0 |
| ICSE | 官方程序，TaintP2X 重复；CoBrA 未推进正文 | 0 / 0 |
| ISSTA | 官方列表及两个到期观察项；未获得正文 | 2 / 0 |
| OSDI | 官方技术程序、Osprey 单篇及完整 PDF；UCSan、Acumen 重复，iLand 留后续 | 2 / 1 |
| FM | 猜测 track 404；改用 fm-2026-research-paper 官方列表，Array-Carrying Symbolic Execution 未推进正文 | 0 / 0 |
| arXiv 补充 | 观察队列及 CaMeL；后者须区分 SaTML 身份与现行计分范围 | 1 / 0 |

上述官方入口沿用可直接复核的会议地址，完整 URL 可见 [W45 来源入口表](2026-W45-source-coverage.md)。本次重复扫描的网络结果、HTML 与 RSS 快照保存在临时审计目录。访问失败未计作“没有更新”。三个入选标题、作者、会议与正文已与官方页对应；按 DOI、arXiv ID、规范 URL、规范化标题对全部 151 条索引去重，无重复。

## 观察队列与正文缺口

- *Towards Long-Horizon Agents: A Survey*：GitHub 连接器传输失败后改用项目原始 README；仍引用 Preprints v1，并保留“11 月初计划更新”的旧预告。Crossref 只返回 2026-07-17 posted-content，relation 为空。项目列表有安全主题，但未形成可由更新正文证明的独立安全方法或实证贡献；继续暂缓至 W50，不依据预告认定版本已经发布。
- [Ghosts in the Memory](https://conf.researchr.org/details/issta-2026/issta-2026-research-papers/107/Ghosts-in-the-Memory-Detecting-Unintended-Sensitive-Data-in-Android-Apps)、[How Safe is Your Screen](https://conf.researchr.org/details/issta-2026/issta-2026-research-papers/177/How-Safe-is-Your-Screen-Understanding-and-Detecting-Privacy-Leaks-in-Sensitive-Activ)：同日复查官方入口，仍仅有摘要/报告信息；保留队列并顺延 W47。高优先级人工补充内容分别为插桩与采样/披露链、UI 模型与隐私判定/披露链，不填充摘要数字。

## 行业池与候选

| 固定来源 | 实际结果 |
| --- | --- |
| Project Zero | 旧入口超时，新站既有紧急补丁内容重复 |
| GTIG / Mandiant | 入口超时，保留覆盖缺口，不声称无更新 |
| Microsoft | 主页 403；官方 RSS 可读，取得 exposed secrets、ARTEX、Rust 三项具体正文入口 |
| Unit 42 | 主页与 RSS 可读，取得欧洲制冷系统攻击正文 |
| Talos | 主页 403；官方 RSS 可读，窗口内 it-sa 经验文章进入初筛，未取得足以支撑新增测量结论的证据；10 月研究早于本期窗口 |
| 玄武 | 研究归档可读，未推进窗口内新增 |
| 科恩 | 研究归档可读，未推进窗口内新增 |
| Anthropic | 研究入口可读，已有自评检测重复，未推进新增 |
| OpenAI | 入口 403，已收录训练遏制/PHP 披露，不重复 |
| NIST | 入口可读，IR 8547 已在 W45 收录 |
| CISA | 通告入口和完整 KEV JSON 可读，筛选日期在 11-03、11-04、11-06 的条目 |
| Gartner | 403，未获得报告正文与方法，不采纳付费预测 |
| Forrester | 原入口 404，使用数据安全/安全管理归档；未推进观点型文章 |
| IDC | 页面可读，市场活动不作为技术研究收录 |

行业初筛至少五项：Microsoft exposed secrets、ARTEX、Rust；Unit 42 制冷系统；Talos it-sa；另补 CISA KEV。保留三项进行正文分析：Microsoft exposed secrets、Unit 42 制冷系统、CISA。Rust RSS 时间为 11-09 20:17 UTC，即北京 11-10，留后期；不因为 URL 写 11-09 就纳入本期。CISA 11-09 条目缺精确新增时刻，未将其纳入本期北京时间窗口，选用更早且无跨日边界争议的条目。

## 第一阶段完成检查

- [x] 重新加载全部规定事实输入并核对 Git 用户改动。
- [x] 三篇按四级规则去重。
- [x] 接收身份由 NDSS、USENIX、ICLR 正式页面支撑。
- [x] 没有将纯 arXiv 或计划更新升级为接收。
- [x] 三篇完整 PDF、三项行业正文/结构化原始证据可访问。
- [x] 三个到期观察项已给出原因、实际日期及下一目标。
- [x] 明确第二阶段三篇论文和三项行业内容。
- [x] 近四期、全部会议与固定行业池、本期软配额及偏离原因完整记录。
- [x] 未在检索阶段据摘要代写论文分析。

## 第二阶段完成检查（2026-11-16）

- [x] 三篇正文方法、实验与局限已读；关键证据页已渲染检查（Anota PDF 第 10、Osprey 第 13、AgentHarm 第 18 页）。
- [x] 三篇各 14 字段顺序完整，各有两个必要名词解释。
- [x] Easycatch 在原文阅读期间逐篇先完成，内部八项推理与初稿保存在临时工作文件，随后写入唯一来源；版本 4、revision 1，摘要一致性校验通过。
- [x] 机制、示例输入与过程、实验分母和条件完整，保留 Osprey 反例及 AgentHarm 合成环境边界。
- [x] 状态与日期按正式论文证据；分类标签先于索引写入，主领域显式指定。
- [x] 正式作者名单与单位匹配；未核验中文姓名保留英文并列入下方名单。
- [x] DOI、arXiv、正式 URL、规范标题去重，无重复；观察名单维护完成。
- [x] 缺正文的两篇 ISSTA 未被补写。
- [x] 三条行业内容已读完整正文，五个来源边界字段齐全。
- [x] 索引、周报、Easycatch、观察名单和行业源维护完成。

### 作者姓名待核验

Meng Wang、Liwei Guo、Yicheng Liu、Alice Yeh、Harry Xu 等保留正式英文署名。若后续取得学校主页与论文一一对应的中文姓名，再更新稳定实体；当前不凭拼音转换。

## 第三阶段核验记录

- [x] 重新完整加载实体表、分类表、154 条索引、154 条 Easycatch，读取当前周报、inquiry、构建器和 Pages workflow。
- [x] 重新请求七项预印本和 Adaptive Adversaries 的 arXiv 正文入口，逐项比较版本与正式来源；除窗口后 Not an A11y 信息外未见升级。WASP 尝试正式 NeurIPS 论文集回查，当前入口未匹配精确标题；保留原有已核验身份，不据 arXiv 或本次失败的猜测海报 URL 新增或升级事实。
- [x] 新增电子科技大学与 UCLA 的规范单位，分别由学校官网和 UCLA About 核验。新添 11 个稳定学者，复用其余作者实体；CISPA 猜测个人路径 404，未据此填入主页或中文名。
- [x] --check 首次仅因 README 自动统计过期失败，安全同步统计后 --check 与正式构建通过。
- [x] 154 篇索引与精读全覆盖，六主领域、70 行业观点、212 单位、751 学者、318 合作边，136 篇计入现行计分范围；学者最近论文均不超过三篇。ICLR 与 OSDI 未在当前计分信号内，不扩大既定范围。
- [x] 独立临时 Chrome 本地交互通过：论文作者与排行姓名打开学者、最近论文跳转、返回、循环历史截断、单弹层、日期、详情名词解释与三入口均正确；无 JS 错误。
- [x] Easycatch 一致性校验通过，维护阶段未补写。
- [x] 七处用户改动与运行前补丁逐字节比较，提交前再次检查。
- [x] 按本次授权提交、推送并跟踪 Pages 与线上资产；实际 SHA、工作流和 HTTP 结果统一列入三期最终发布记录，只有成功核验后才进入 W47。
