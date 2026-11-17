# 2026-W47 重做：时间窗口与来源证据

扩大覆盖后最终结果：10篇动态，缺0篇；来源组4/3/3。正式会议2篇CCS、预印8篇。以下旧2篇结果保留为过程记录。历史十篇已独立迁移，过往误补审计另存归档。

本期窗口：2026-11-10 至 2026-11-16（北京时间）。实际回溯检索：2026-11-17。此前用历史基线补数的结论撤销，旧审计记录见 [归档](../archive/2026-W47-superseded-20261117.md)。首次被整理者发现不构成窗口内更新。

## 第一阶段：重新检索

完整读取01及索引、观察清单、14来源池、观点库、本期原周报与inquiry。先处理有到期窗口事件的候选；两个ISSTA缺正文项仍等待W48，长程综述仍W50，不把旧观察记录视为新进展。扫描三组全部21会议，按 USENIX→其余安全；SOSP→其余软件系统；AAAI→其余AI 轮换。

| 来源 | 实际访问 | 相关链接样例数（最多12个） | 时效门槛处理 |
|---|---|---:|---|
| [USENIX](https://www.usenix.org/conference/usenixsecurity26/technical-sessions) | 200 | 12 | 200仅说明入口可读；未取得窗口内版本/出版事件的条目不入选，超时/403/机器人不等于无论文 |
| [S&P](https://sp2026.ieee-security.org/accepted-papers.html) | 200 | 12 | 200仅说明入口可读；未取得窗口内版本/出版事件的条目不入选，超时/403/机器人不等于无论文 |
| [CCS](https://www.sigsac.org/ccs/CCS2026/program/accepted-papers.html) | 200 | 0 | 200仅说明入口可读；未取得窗口内版本/出版事件的条目不入选，超时/403/机器人不等于无论文 |
| [NDSS](https://www.ndss-symposium.org/ndss2026/accepted-papers/) | 200 | 12 | 200仅说明入口可读；未取得窗口内版本/出版事件的条目不入选，超时/403/机器人不等于无论文 |
| [SOSP](https://sigops.org/s/conferences/sosp/2026/accepted.html) | 200 | 0 | 200仅说明入口可读；未取得窗口内版本/出版事件的条目不入选，超时/403/机器人不等于无论文 |
| [FM](https://conf.researchr.org/track/fm-2026/fm-2026-research-paper) | 200 | 1 | 200仅说明入口可读；未取得窗口内版本/出版事件的条目不入选，超时/403/机器人不等于无论文 |
| [ISSTA](https://conf.researchr.org/track/issta-2026/issta-2026-research-papers) | 200 | 12 | 200仅说明入口可读；未取得窗口内版本/出版事件的条目不入选，超时/403/机器人不等于无论文 |
| [ASE](https://conf.researchr.org/track/ase-2026/ase-2026-research-track) | curl: (28) Operation timed out after 25003 milliseconds with 1513083 bytes received  | 0 | 200仅说明入口可读；未取得窗口内版本/出版事件的条目不入选，超时/403/机器人不等于无论文 |
| [ICSE](https://conf.researchr.org/track/icse-2026/icse-2026-research-track) | 200 | 12 | 200仅说明入口可读；未取得窗口内版本/出版事件的条目不入选，超时/403/机器人不等于无论文 |
| [OOPSLA](https://2026.splashcon.org/track/oopsla-2026) | 200 | 12 | 200仅说明入口可读；未取得窗口内版本/出版事件的条目不入选，超时/403/机器人不等于无论文 |
| [PLDI](https://conf.researchr.org/track/pldi-2026/pldi-2026-papers) | 200 | 5 | 200仅说明入口可读；未取得窗口内版本/出版事件的条目不入选，超时/403/机器人不等于无论文 |
| [POPL](https://conf.researchr.org/track/popl-2026/POPL-2026-popl-research-papers) | 200 | 12 | 200仅说明入口可读；未取得窗口内版本/出版事件的条目不入选，超时/403/机器人不等于无论文 |
| [FSE](https://conf.researchr.org/track/fse-2026/fse-2026-research-papers) | curl: (28) Operation timed out after 25010 milliseconds with 917187 bytes received  | 0 | 200仅说明入口可读；未取得窗口内版本/出版事件的条目不入选，超时/403/机器人不等于无论文 |
| [OSDI](https://www.usenix.org/conference/osdi26/technical-sessions) | 200 | 5 | 200仅说明入口可读；未取得窗口内版本/出版事件的条目不入选，超时/403/机器人不等于无论文 |
| [ICLR](https://iclr.cc/virtual/2026/papers.html) | 200 | 12 | 200仅说明入口可读；未取得窗口内版本/出版事件的条目不入选，超时/403/机器人不等于无论文 |
| [ICML](https://proceedings.mlr.press/) | 200 | 0 | 200仅说明入口可读；未取得窗口内版本/出版事件的条目不入选，超时/403/机器人不等于无论文 |
| [AAAI](https://ojs.aaai.org/index.php/AAAI/issue/archive) | 200 | 0 | 200仅说明入口可读；未取得窗口内版本/出版事件的条目不入选，超时/403/机器人不等于无论文 |
| [NeurIPS](https://proceedings.neurips.cc/paper_files/paper/2026) | 404 | 0 | 200仅说明入口可读；未取得窗口内版本/出版事件的条目不入选，超时/403/机器人不等于无论文 |
| [ACL](https://aclanthology.org/events/acl-2026/) | curl: (28) Operation timed out after 25002 milliseconds with 991939 out of 18926839 bytes received  | 0 | 200仅说明入口可读；未取得窗口内版本/出版事件的条目不入选，超时/403/机器人不等于无论文 |
| [CVPR](https://openaccess.thecvf.com/CVPR2026) | 200 | 0 | 200仅说明入口可读；未取得窗口内版本/出版事件的条目不入选，超时/403/机器人不等于无论文 |
| [ICCV](https://openaccess.thecvf.com/ICCV2025) | 200 | 0 | 200仅说明入口可读；未取得窗口内版本/出版事件的条目不入选，超时/403/机器人不等于无论文 |
| [Google Project Zero](https://googleprojectzero.blogspot.com/) | curl: (28) Connection timed out after 25003 milliseconds  | 0 | 200仅说明入口可读；未取得窗口内版本/出版事件的条目不入选，超时/403/机器人不等于无论文 |
| [Google Threat Intelligence / Mandiant](https://cloud.google.com/blog/topics/threat-intelligence) | curl: (28) Connection timed out after 25009 milliseconds  | 0 | 200仅说明入口可读；未取得窗口内版本/出版事件的条目不入选，超时/403/机器人不等于无论文 |
| [Microsoft Security / MSRC](https://www.microsoft.com/security/blog/) | 403 | 0 | 200仅说明入口可读；未取得窗口内版本/出版事件的条目不入选，超时/403/机器人不等于无论文 |
| [Unit 42](https://unit42.paloaltonetworks.com/) | 200 | 12 | 200仅说明入口可读；未取得窗口内版本/出版事件的条目不入选，超时/403/机器人不等于无论文 |
| [Cisco Talos](https://blog.talosintelligence.com/) | 403 | 0 | 200仅说明入口可读；未取得窗口内版本/出版事件的条目不入选，超时/403/机器人不等于无论文 |
| [腾讯玄武实验室](https://xlab.tencent.com/cn/) | 200 | 1 | 200仅说明入口可读；未取得窗口内版本/出版事件的条目不入选，超时/403/机器人不等于无论文 |
| [腾讯科恩实验室](https://keenlab.tencent.com/zh/) | 200 | 2 | 200仅说明入口可读；未取得窗口内版本/出版事件的条目不入选，超时/403/机器人不等于无论文 |
| [Anthropic Research / Frontier Red Team](https://www.anthropic.com/research) | 200 | 1 | 200仅说明入口可读；未取得窗口内版本/出版事件的条目不入选，超时/403/机器人不等于无论文 |
| [OpenAI Security Research](https://openai.com/research/) | 403 | 0 | 200仅说明入口可读；未取得窗口内版本/出版事件的条目不入选，超时/403/机器人不等于无论文 |
| [NIST Cybersecurity](https://www.nist.gov/cybersecurity) | 200 | 12 | 200仅说明入口可读；未取得窗口内版本/出版事件的条目不入选，超时/403/机器人不等于无论文 |
| [CISA](https://www.cisa.gov/news-events/cybersecurity-advisories) | 200 | 12 | 200仅说明入口可读；未取得窗口内版本/出版事件的条目不入选，超时/403/机器人不等于无论文 |
| [Gartner](https://www.gartner.com/en/cybersecurity) | 403 | 0 | 200仅说明入口可读；未取得窗口内版本/出版事件的条目不入选，超时/403/机器人不等于无论文 |
| [Forrester](https://www.forrester.com/security-risk/) | 404 | 0 | 200仅说明入口可读；未取得窗口内版本/出版事件的条目不入选，超时/403/机器人不等于无论文 |
| [IDC Security](https://www.idc.com/) | 200 | 2 | 200仅说明入口可读；未取得窗口内版本/出版事件的条目不入选，超时/403/机器人不等于无论文 |

会议首页、静态接收表、模板年份和页面修改日期均未作为入选日期。NeurIPS入口若指向2025旧论文集，只作存量回查，额外检查2026官方/作者新版本；ARXIV批量API返回429，月份列表404，已使用精确检索与逐篇原始abs/PDF核对。检索受限不代表近期没有论文。

近四期分布以索引当前归属统计，基础阅读不计入周报新增；本期缺额在二阶段实际落库后记录。安全/软件系统/AI的4/3/3是软配额，时效与正文先行。行业池全部尝试；原有符合窗口的内容保留，不把跨期文章重复追加，也不从标题或摘要生成新观点。

- [x] 全量读取事实输入；完成三组会议及14行业来源尝试。
- [x] 候选去重、状态与正文可用性记录；没有作者模板推断接收。
- [x] 窗口内事件明确，预印保留未同行评审状态。
- [x] 暂缓、缺正文和来源访问缺口均明确，未编造分析。
- [x] 阶段一完成，允许进入正文精读；不足不拿旧论文补数。

W47最终候选进入阅读：
- Meme Coin Factories，正式CCS2026接收表可匹配；Crossref精确DOI10.1145/3830454.3846641登记online为2026-11-14、print为11-15；15页作者版已取得。窗口内依据是正式出版事件，未把会议开幕日或作者版首次日期当新公开。
- Anonymous in Name Only，2611.17012v1，原始arXiv元数据2026-11-12，完整32页PDF；预印候选，法律评价只作为作者主张。

The Devil in Context为11月3日，已回W46完成精读/发布，不计本期。Indirect Prompt Injection in the Wild（2604.27202）的Crossref搜索第一项实际是另一篇题目、6月发表，禁止拿模糊命中作时效证据；无本期事件，排除。CCS开幕11月15日仅是活动日期，不自动让全部旧稿符合窗口；正式会议入选目前仅这一篇有精确出版证据。11月10/11/12/13/16多组安全、隐私、程序分析和代理查询未取得其他可核验候选，API429及搜索覆盖限制保留。两篇与186条索引四级去重无重复。

行业五项初筛为Windows Rust、Cairn、ARTEX（本期已有）、NIST迁移（跨期）、咨询AI预测（正文方法不足）；保留现有三条，不补未读观点。

## 第二阶段完成

- [x] 最终2篇新增均有窗口内版本/出版事件与完整正文，按14字段顺序和1—5术语整理。
- [x] 同次正文阅读先保存8步推理与Easycatch草稿，再写卡片；摘要仅作一致性校验。
- [x] 原十篇精读与Easycatch迁入独立基础阅读，未改事实字段，旧周报引用保存为previous_weekly_notes。
- [x] 新增按四级去重；预印未写成正式接收，标签受控、主领域唯一。
- [x] 既有行业内容保留正文证据及商业利益边界，未追加未读内容。
- [x] 最终来源组2/0/0，目标4/3/3缺额2/3/3，总缺8。来源按主题归组，正式会议命中与预印分别列出；不宣称来源总量不足。

## 第三阶段及最终配额核对

近四期W43—W46按修正后的动态归属统计：{'security': 10, 'software': 9, 'ai': 9}，共28篇，不计基础专题。W47最终安全2/软件系统0/AI0，缺2/3/3，总缺8；会议实际1篇CCS，另1篇arXiv，不把主题分组当作正式会议命中。三期主题合计4/3/3，但会议来源目标仍有缺口；9篇预印不升级为主会论文。

Meme Coin Factories核对正式DOI在线11月14日、印刷11月15日及15页作者稿；隐私预印核对32页原文，特别保留前100条经排序选择样本不能外推总体识别率，正文million单位与表1数量不一致不擅自订正，不复制身份查询。作者法律评价未作为官方裁决。全文和关键表格已复核。

新增Fullstack的NYC、URV的Tarragona、ENS/PSL的Paris均有论文明确地点，新增8学者、复用既有标识。Nicolas Christin的CMU官方个人页和Mathias Payer本人页已核实。Enze Liu中文名未得一一对应证据，保留英文；其他前期未核验姓名及跨国团队地区见各期记录。历史风险回查未发现进一步正式身份升级，原Not an A11y工作坊、MCPTox/WASP更正保持。

- [x] 完整读取03及全部事实、构建和发布输入；作者、单位和稳定ID可映射。
- [x] 30篇基础专题（包括指定21篇和其余9篇）与4/4/2动态明确隔离，逐ID核对迁移且旧Easycatch未丢失。
- [x] 188篇/188缓存、6领域、73观点、249单位、911学者、459合作边，188篇关系覆盖，recent_papers≤3。
- [x] --check及正式构建通过，26项Python和5项JS测试通过；缺日期、窗口外日期、无具体变更的更新均拒绝。
- [x] 七个用户修改的原始hunk保留，构建器仅暂存本次功能差异。

本地交互和发布后验结果将按实际检查写入memory与最终报告。

最终规则固化：01独占时效规则，列出weekly_windows与discovery_events字段；构建从W45起拒绝未声明窗口的后续周报，并要求实质更新有版本和具体变化。补齐UTC晚间稿件的北京时间事件日期，保留原文版本日期。新增回归测试通过；全文内容与页面交互不变。

## 本次扩大覆盖：检索阶段复核

近四期（W43—W46）共40篇：W43/W44各10篇已核准会议论文，W45为1篇NeurIPS与9预印，W46为10预印；三组配额统计约13/12/15，安全与软件相对AI偏少。按CCS、ISSTA、NeurIPS为各组起点扫描全部21会议及14行业来源，无命中数量截断。CCS为无链接表格，另解析全部论文行，修正旧脚本0链接被误读为无候选的问题。全部记录见[来源审计](2026-W47-expanded-sources.json)。

八篇候选均取得原始abs及完整PDF，arXiv v1日期在11月12—13日；On the Same Track在作者页已有更早线索，改用Crossref正式在线出版11月14日事件，CCS官方列表核准接收。其余七篇按预印初筛。DOI/arXiv/URL/规范化标题四级去重通过。

作者主页沿Konrad Rieck实验室论文表继续追踪；个人主页及三方聚合日期不直接当首次公开事件。Weakest Agent的Workshop接收目前只有作者自述，保持预印待官方核准。既有两个ISSTA候选仍缺全文，不入本期。行业池现有窗口内观点保留，跨期/重复不追加。

- [x] 本阶段所有规则及输入重读，观察清单处理。
- [x] 三组与行业池全部尝试；访问缺口记录；不把链接数量当逐篇日期核验。
- [x] 八篇候选明确版本与全文，预印和正式接收分开；原两篇保留。
- [x] 4/3/3为目标，实际分布待正文核准；历史基础阅读计数为0。
- [x] 检索阶段通过，进入原文精读。

## 扩大覆盖后的精读与维护结果

八篇新增均核对完整正文，先保存8步推理与两段Easycatch，再写14字段卡片；每篇保留1—2个必要术语，去重、作者对应及受控主题通过。ReA-Bench v1/v2逐行比较仅增加数据集入口，沿用首次公开事件，不把v2重复计数；数据集入口本轮访问失败，不宣称下载数据或复现实验。Rail论文使用正式出版日期，未把新arXiv ID误当首次公开。

| 新增 | 窗口事件（北京时间） | 正文与处理 |
|---|---|---|
| [CANTraj: Recovering Vehicle Trajectories from CAN Signals in Naturalistic Driving](https://arxiv.org/abs/2611.18442v1) | 2026-11-14 first-public | 完整PDF；预印 |
| [On the Same Track: Privacy Leaks in Electric Rail Transport via Magnetic Fields](https://arxiv.org/abs/2611.18312v1) | 2026-11-14 published | 完整PDF；CCS正式出版 |
| [PrivacyPR: A Dataset of Real-World Privacy Fixes for Benchmarking Privacy-Aware Code Review](https://arxiv.org/abs/2611.18293v1) | 2026-11-13 first-public | 完整PDF；预印 |
| [Preserve the Vulnerability, Break the Alert: Testing the Robustness of CodeQL Taint Tracking with Natural Rewrites](https://arxiv.org/abs/2611.17123v1) | 2026-11-13 first-public | 完整PDF；预印 |
| [Forget the Lineage: Forward-Secure, Lineage-Complete Cryptographic Erasure for LLM-Agent Memory](https://arxiv.org/abs/2611.18133v1) | 2026-11-13 first-public | 完整PDF；预印 |
| [CapLite: Prompt-Injection Defense for Small Language Model Agents without Model-Written Security Artifacts](https://arxiv.org/abs/2611.17115v1) | 2026-11-13 first-public | 完整PDF；预印 |
| [Only as Safe as the Weakest Agent: A Break That Appears Only When the System Is Multi-Agent](https://arxiv.org/abs/2611.17520v1) | 2026-11-13 first-public | 完整PDF；预印 |
| [ReA-Bench: Benchmarking Responsible Agent Auditing](https://arxiv.org/abs/2611.16493v1) | 2026-11-12 first-public | 完整PDF；预印 |

### 配额与未入选原因

- 安全4、软件系统3、AI3。LinEra按研究对象为记忆存储与删除系统归软件系统来源组；主领域仍为系统与硬件安全。两个CCS命中符合单会通常不超过2篇，其余8篇预印。S&P、USENIX、NDSS没有本轮核准的窗口新事件，三组目标达到不代表正式会议分布已均衡。
- CCS全部486行已保存，其他会议保存全量关键词相关链接。静态论文表缺精确窗口事件，尚未逐篇追到日期的条目均为未核准。ASE及ACL正文列表本轮超时；CVF等页面零锚点命中仅为解析结果。各源完整URL和状态见JSON，未声称穷尽所有新论文。
- 候选DeCompCert（2611.18055）为反编译语义验证，尚缺独立安全贡献核验，本轮不因软件配额补入；Bytes to Behavior（2611.18272）需进一步确认GPU读权限与攻击者能力，列下期正文重点。两者只作后续候选，未生成精读。
- Weakest Agent仅作者声明Meta-Agents workshop接收，官网未列逐篇名单；保留预印，不计NeurIPS主会。两个ISSTA待正文项目继续W48，旧GRaM Tiny版本仍需实质差异比对。
- 行业池复查未追加符合窗口且已读、未重复的观点；本次0新增，原有73条保留。

### 实体与待核验清单

- AAIG中文名称与集团归属来自[阿里安全官方发布](https://s.alibaba.com/mobile/news/detail/1173/security)；BIFOLD依据[官方署名](https://www.bifold.berlin/imprint)归并TU Berlin；CEDRIC依据[实验室官网](https://cedric.cnam.fr/)归并Cnam；Efrei依据[母体大学页面](https://www.assas-universite.fr/fr/frederic-meunier-directeur-general-lefrei)归并Université Paris-Panthéon-Assas。跨国企业及独立研究者地区没有猜填。
- [Bowen Xu](https://www.bowenxu.me/)、[Yulliwas Ameur](https://yulliwasameur.github.io/about/)及铁路论文作者主页已登记；Zimo Xu与Hideki Nakayama依据东京大学成员页对应。Shidong Pan按原文保留Independent Researcher，未由邮箱推断为ANU现职。
- 中文姓名尚待一一核准：CANTraj的六位作者；PrivacyPR的Hua Yang、Shidong Pan、Bowen Xu；CodeQL的Zhezhen Cao、Weiyuan Ding；CapLite的Zimo Xu、Wenzhuo Liu；ReA-Bench全部九位作者。名单以本期卡片原署名为准，不猜汉字。
- 历史预印与待核准条目全量元数据回查，无新增状态升级。Not an A11y由Crossref确认11月14日已登记出版，与既有accepted-workshop一致；TADP仍缺WACV官方逐篇接收证据。

- [x] 第二阶段全部完成检查通过，正文/两段解释/14字段/身份/去重/行业证据核对完成。
- [x] 第三阶段规则与全部输入重读，Git原有7文件保持未暂存；新实体及上级归属有来源，历史状态保持一致。
- [x] 构建及check通过：208篇/208精读缓存，6领域、73观点、271单位、993学者、501合作边，recent_papers均≤3。26项Python与5项JS通过；本地Chrome核验日期、术语、三个入口及所有要求的单弹层导航，无页面错误。原7文件用户差异逐字节一致。
- 推送及线上状态以发布工作流和最终报告的实际核验为准。

此前逐期发布证据：W45 `26b8da9e97807affa3cbf0afbf5c492ddce5b6a6`，Pages 44046500096成功；W46 `37b3bd159a305340fb6d89bf069af09e49848efc`，Pages 44048558268成功。每期线上10篇及基础30篇详情、关系图均返回200，Chrome关键交互通过。
