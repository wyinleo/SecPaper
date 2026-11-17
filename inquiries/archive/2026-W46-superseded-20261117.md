# 2026-W46 来源覆盖与核验记录

> 十篇补齐更正：原先三篇编辑范围解释撤回；下方旧记录保留审计，本轮以文末十篇补齐记录为准。W45 已补至十篇并在线验证（14f29403，Pages 43867390020）。

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


## 十篇补齐：第一阶段重新执行

重新全文读取 01-discovery 及全部输入：164 条索引、3 个观察项、14 个行业来源、73 条行业观点、最新 W47 与本期 inquiry。七个用户修改仍保持。W42—W45 共 40 篇，安全16、软件12、AI12，占40%/30%/30%；会议细分为 NDSS5、CCS4、USENIX Security4、S&P3，FSE3、PLDI2、OSDI2、ASE/POPL/OOPSLA/ICSE/ISSTA各1，NeurIPS4、AAAI2、ICML2、ICCV/ACL/CVPR/ICLR各1。

组内轮换从 NDSS、ASE、ACL 开始，仍扫描完全部会议，再补 arXiv。软件入口多项超时、AAAI 反爬，均不当作没有更新；入选改由正式单篇和作者原文核验。

| 来源 | 本轮实际扫描 | 明确候选 / 新增入选 |
| --- | --- | --- |
| NDSS | https://www.ndss-symposium.org/ndss2026/accepted-papers/；200；目录安全主题筛选，已有/未推进全文项不计新候选 | 0 / 0 |
| CCS | https://www.sigsac.org/ccs/CCS2026/program/accepted-papers.html；200；Android Permissions Demystified 单篇及全文核对 | 1 / 1 |
| S&P | https://sp2026.ieee-security.org/accepted-papers.html；200；Angora 单篇及全文核对 | 1 / 1 |
| USENIX | https://www.usenix.org/conference/usenixsecurity26/technical-sessions；200；Terrapin 单篇及全文核对 | 1 / 1 |
| ASE | https://conf.researchr.org/track/ase-2026/ase-2026-research-track；超时；目录安全主题筛选，已有/未推进全文项不计新候选 | 0 / 0 |
| ICSE | https://conf.researchr.org/track/icse-2026/icse-2026-research-track；200；Superion、SAVER 单篇及全文核对 | 2 / 2 |
| ISSTA | https://conf.researchr.org/track/issta-2026/issta-2026-research-papers；超时；目录安全主题筛选，已有/未推进全文项不计新候选 | 0 / 0 |
| FM | https://conf.researchr.org/track/fm-2026/fm-2026-research-paper；200；目录安全主题筛选，已有/未推进全文项不计新候选 | 0 / 0 |
| PLDI | https://conf.researchr.org/track/pldi-2026/pldi-2026-papers；超时；目录安全主题筛选，已有/未推进全文项不计新候选 | 0 / 0 |
| POPL | https://conf.researchr.org/track/popl-2026/POPL-2026-popl-research-papers；200；目录安全主题筛选，已有/未推进全文项不计新候选 | 0 / 0 |
| FSE | https://conf.researchr.org/track/fse-2026/fse-2026-research-papers；超时；目录安全主题筛选，已有/未推进全文项不计新候选 | 0 / 0 |
| SOSP | https://sigops.org/s/conferences/sosp/2026/accepted.html；200；目录安全主题筛选，已有/未推进全文项不计新候选 | 0 / 0 |
| OOPSLA | https://2026.splashcon.org/track/oopsla-2026；超时；目录安全主题筛选，已有/未推进全文项不计新候选 | 0 / 0 |
| OSDI | https://www.usenix.org/conference/osdi26/technical-sessions；200；目录安全主题筛选，已有/未推进全文项不计新候选 | 0 / 0 |
| ACL | https://aclanthology.org/events/acl-2026/；超时；SafeDecoding 单篇及全文核对 | 1 / 1 |
| AAAI | https://ojs.aaai.org/index.php/AAAI/issue/archive；200；FigStep 单篇及全文核对 | 1 / 1 |
| ICLR | https://iclr.cc/virtual/2026/papers.html；200；目录安全主题筛选，已有/未推进全文项不计新候选 | 0 / 0 |
| ICML | https://proceedings.mlr.press/；200；目录安全主题筛选，已有/未推进全文项不计新候选 | 0 / 0 |
| NeurIPS | https://proceedings.neurips.cc/paper_files/paper/2025；200；目录安全主题筛选，已有/未推进全文项不计新候选 | 0 / 0 |
| CVPR | https://openaccess.thecvf.com/CVPR2026；200；目录安全主题筛选，已有/未推进全文项不计新候选 | 0 / 0 |
| ICCV | https://openaccess.thecvf.com/ICCV2025；200；目录安全主题筛选，已有/未推进全文项不计新候选 | 0 / 0 |
| Google Project Zero | https://googleprojectzero.blogspot.com/；超时；目录安全主题筛选，已有/未推进全文项不计新候选 | 0 / 0 |
| Google Threat Intelligence / Mandiant | https://cloud.google.com/blog/topics/threat-intelligence；超时；目录安全主题筛选，已有/未推进全文项不计新候选 | 0 / 0 |
| Microsoft Security / MSRC | https://www.microsoft.com/security/blog/；403；目录安全主题筛选，已有/未推进全文项不计新候选 | 0 / 0 |
| Unit 42 | https://unit42.paloaltonetworks.com/；200；目录安全主题筛选，已有/未推进全文项不计新候选 | 0 / 0 |
| Cisco Talos | https://blog.talosintelligence.com/；403；目录安全主题筛选，已有/未推进全文项不计新候选 | 0 / 0 |
| 腾讯玄武实验室 | https://xlab.tencent.com/cn/；200；目录安全主题筛选，已有/未推进全文项不计新候选 | 0 / 0 |
| 腾讯科恩实验室 | https://keenlab.tencent.com/zh/；200；目录安全主题筛选，已有/未推进全文项不计新候选 | 0 / 0 |
| Anthropic Research / Frontier Red Team | https://www.anthropic.com/research；200；目录安全主题筛选，已有/未推进全文项不计新候选 | 0 / 0 |
| OpenAI Security Research | https://openai.com/research/；403；目录安全主题筛选，已有/未推进全文项不计新候选 | 0 / 0 |
| NIST Cybersecurity | https://www.nist.gov/cybersecurity；200；目录安全主题筛选，已有/未推进全文项不计新候选 | 0 / 0 |
| CISA | https://www.cisa.gov/news-events/cybersecurity-advisories；200；目录安全主题筛选，已有/未推进全文项不计新候选 | 0 / 0 |
| Gartner | https://www.gartner.com/en/cybersecurity；403；目录安全主题筛选，已有/未推进全文项不计新候选 | 0 / 0 |
| Forrester | https://www.forrester.com/security-risk/；超时；目录安全主题筛选，已有/未推进全文项不计新候选 | 0 / 0 |
| IDC Security | https://www.idc.com/；200；目录安全主题筛选，已有/未推进全文项不计新候选 | 0 / 0 |


候选七篇正文已取得：Angora（SP2018 官方程序+UC Davis 作者PDF）、Android Permissions Demystified（CCS2011 DOI+马里兰大学课程保存正式页码627起全文）、Terrapin（USENIX2024 正式PDF）、Superion（ICSE2019 官方程序+作者PDF）、SAVER（ICSE2020 官方程序+作者PDF）、SafeDecoding（ACL2024 Anthology 正式全文）、FigStep（AAAI2025 正式文章 DOI+作者 arXiv 完整扩展版）。FigStep 扩展版独立注明，精读不会把扩展稿当作会议排版稿。Berkeley 撤回的是已被会议稿取代的早期技术报告，本期不读取或引用撤回技术报告的实验。QASan 属 SecDev，排除出本项目软件组配额。

本期既有 Anota、Osprey、AgentHarm 保留，新增3安全+2软件+2AI，合计4/3/3，无软配额偏离。安全四会各1篇，软件2篇ICSE及1篇OSDI，AI分别ICLR/ACL/AAAI。历史基线保留原发表日期，不声称为窗口内首次公开。

按 DOI、arXiv ID、正式URL、规范标题查164条索引，七篇无重复；原三篇不重复写入。观察队列的两个缺正文 ISSTA 项目继续 W48，通用长程综述仍 W50，不倒退观察周。行业五项初筛沿用并复核本期已有来源记录（exposed secrets、制冷系统、CISA KEV、ARTEX、Rust），前三项已收录，后两项分别跨期/重复；本轮无新合格独立正文，不追加营销或重复条目。

- [x] 全部输入完整读取并检查用户改动。
- [x] 四层去重完成。
- [x] 七篇接收身份有正式会议/DOI依据。
- [x] arXiv 仅作作者正文来源，不独立证明接收。
- [x] 七篇正文可读且安全相关性明确。
- [x] 三个暂缓观察项保持原因、检查日期及目标周。
- [x] 七篇进入第二阶段，尚未写正文分析。
- [x] 全会议、行业池、近四期与4/3/3配额均记录。
- [x] 第一阶段无摘要代写。


## 十篇补齐：第二阶段完成检查

- [x] 七篇完整正文已读方法、案例、实验及局限；原三篇字段保留。
- [x] 新增八项中间推理和两段 Easycatch 逐篇先随原文保存，再写十四字段与唯一正文源；skill4、revision1，未从完成卡片反推。
- [x] 十篇均十四字段、必要名词解释、机制与示例完整。
- [x] 实验分母、版本、预算与边界明确：Angora区分已列/未列注入漏洞，Stowaway区分权限告警/应用分母，Terrapin为2023扫描，Superion用所读版34/22/19，SAVER区分96真告警与66误报，SafeDecoding指出先拒后答，FigStep为最多五次任一成功。
- [x] 正式接收与时间线有来源，SAVER仅用已确认年份，未用延期报告日填出版日。
- [x] 单一主领域与受控标签有效，程序修复新标签先定义再使用。
- [x] 作者来自正文；陈鹏据上海科技大学Angora报告记录，陈碧欢据复旦中英简介，段斯斯据清华中英个人页一一对应。其他未证实中文保留英文。
- [x] 四级去重完成，无重复；两个缺全文ISSTA继续等待W48。
- [x] 新增七篇落库并有完整阅读；无正文项未补写。
- [x] 原三项行业观点五个边界字段完整，本轮无合格新增不重复收录。

姓名待核验：Junjie Wang、Lei Wei、Yang Liu、Zhangchen Xu、Fengqing Jiang、Luyao Niu、Jinyuan Jia、Bill Yuchen Lin、Yichen Gong、Delong Ran、Jinyuan Liu、Conglei Wang、Tianshuo Cong、Anyu Wang、Xiaoyun Wang 等保留正式英文，避免同名或拼音猜字。National Financial Cryptography Research Center 的官方中文与独立/联合机构归属尚不足以一一确认，遵照事实表“未核验保留原文”策略记录英文署名，不擅自翻译为国家金融业密码应用研究中心，也不直接归并清华；待后续可靠双语证据。

可靠名称来源：陈鹏 https://sist.shanghaitech.edu.cn/2023/0505/c10970a1077194/page.htm ；陈碧欢 https://datascience.fudan.edu.cn/b4/eb/c13398a439531/page.htm ；段斯斯 https://people.ias.tsinghua.edu.cn/duansisi/zh_CN/jsxx/7088/jsxx/jsxx.htm ；山东区块链研究院 https://www.tsinghua.edu.cn/info/1182/90245.htm 。


## 十篇补齐：第三阶段验证

- [x] 阶段入口重新全文加载03分片及规定事实/构建/发布文件，Git原有七文件补丁逐字节保持。
- [x] 再查八项预印/工作坊的 arXiv comments、journal reference、DOI；未发现此前记录之外的可靠身份升级，原条目保留。
- [x] 新增26个学者规范键与4个单位键；所有署名有稳定实体、重复ID检查无新冲突，归并后822位学者、223单位、362合作记录。
- [x] 171/171论文与精读及单位作者覆盖、6主领域、73行业观点；最近论文均≤3，现行计分下界149篇。
- [x] --check与正式构建通过；README统计先安全同步后重查。
- [x] 七篇关键正文表格页已渲染核对，正文版本差异保留审计。Crossref复核确认Superion与FigStep的身份/日期；其他API失败不取代已有正式来源。
- [x] 本地Chrome作者、排行、最近论文、返回、循环去重、单弹层、日期、名词解释和三入口验证通过，无JS错误。
- [x] Easycatch来源一致性全部通过，无维护阶段补写。
- [x] 仅暂存本期事实与生成物，七个用户改动不入提交；发布前保留原工作流。
- 发布门：实际提交、推送、Pages与线上十篇状态存入本轮发布记录及memory，全部成功后才进入W47。
