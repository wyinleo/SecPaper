# 2026-W48 来源覆盖与阶段核验

检索窗口：2026-11-17 至 2026-11-23（北京时间）。执行于11月23日，覆盖执行时点之前可得材料；当天后续内容留待下期回查。

## 第一阶段：检索

已完整读取01规则、现有论文索引、观察队列、行业来源及观点库，并读取最新W47周报。运行前7个用户修改已保存二进制差异快照。近4期W44—W47共40篇，安全/软件系统/AI分别13/12/15（32.5%/30%/37.5%）；按正式会议优先、预印主题归组。正式会议13篇，预印27篇。

轮换起点为NDSS、OSDI、ACL，每组起点先访问，再扫描组内全部余下会议。完整相关链接与无链接表格保存于[机器可读来源记录](2026-W48-sources.json)。数量表示解析后的相关入口，尚未逐篇核准的日期明确为空；入口访问成功只证明取得列表。

|来源|访问结果|相关链接/表行数|筛选处理|
|---|---|---:|---|
|[NDSS](https://www.ndss-symposium.org/ndss2026/accepted-papers/)|200|141/0|按具体候选追原文与版本；未核准窗口事件不计入选|
|[S&P](https://sp2026.ieee-security.org/accepted-papers.html)|200|137/0|按具体候选追原文与版本；未核准窗口事件不计入选|
|[USENIX](https://www.usenix.org/conference/usenixsecurity26/technical-sessions)|200|203/0|按具体候选追原文与版本；未核准窗口事件不计入选|
|[CCS](https://www.sigsac.org/ccs/CCS2026/program/accepted-papers.html)|200|0/273|按具体候选追原文与版本；未核准窗口事件不计入选|
|[OSDI](https://www.usenix.org/conference/osdi26/technical-sessions)|200|9/0|按具体候选追原文与版本；未核准窗口事件不计入选|
|[SOSP](https://sigops.org/s/conferences/sosp/2026/accepted.html)|200|0/0|按具体候选追原文与版本；未核准窗口事件不计入选|
|[FM](https://conf.researchr.org/track/fm-2026/fm-2026-research-paper)|200|17/21|按具体候选追原文与版本；未核准窗口事件不计入选|
|[OOPSLA](https://2026.splashcon.org/track/oopsla-2026)|200|52/55|按具体候选追原文与版本；未核准窗口事件不计入选|
|[PLDI](https://conf.researchr.org/track/pldi-2026/pldi-2026-papers)|200|41/46|按具体候选追原文与版本；未核准窗口事件不计入选|
|[POPL](https://conf.researchr.org/track/popl-2026/POPL-2026-popl-research-papers)|200|45/42|按具体候选追原文与版本；未核准窗口事件不计入选|
|[ISSTA](https://conf.researchr.org/track/issta-2026/issta-2026-research-papers)|200|148/152|按具体候选追原文与版本；未核准窗口事件不计入选|
|[ASE](https://conf.researchr.org/track/ase-2026/ase-2026-research-track)|200|263/282|按具体候选追原文与版本；未核准窗口事件不计入选|
|[ICSE](https://conf.researchr.org/track/icse-2026/icse-2026-research-track)|200|253/264|按具体候选追原文与版本；未核准窗口事件不计入选|
|[FSE](https://conf.researchr.org/track/fse-2026/fse-2026-research-papers)|200|158/177|按具体候选追原文与版本；未核准窗口事件不计入选|
|[ACL](https://aclanthology.org/events/acl-2026/)|200|1120/0|按具体候选追原文与版本；未核准窗口事件不计入选|
|[CVPR](https://openaccess.thecvf.com/CVPR2026)|200|0/0|按具体候选追原文与版本；未核准窗口事件不计入选|
|[ICCV](https://openaccess.thecvf.com/ICCV2025)|200|0/0|按具体候选追原文与版本；未核准窗口事件不计入选|
|[AAAI](https://ojs.aaai.org/index.php/AAAI/issue/archive)|200|0/0|按具体候选追原文与版本；未核准窗口事件不计入选|
|[ICLR](https://iclr.cc/virtual/2026/papers.html)|200|600/1|按具体候选追原文与版本；未核准窗口事件不计入选|
|[ICML](https://proceedings.mlr.press/)|200|0/0|按具体候选追原文与版本；未核准窗口事件不计入选|
|[NeurIPS](https://neurips.cc/Downloads/2026)|200|1189/1|按具体候选追原文与版本；未核准窗口事件不计入选|
|[Google Project Zero](https://googleprojectzero.blogspot.com/)|error|0/0|访问缺口已保留；未据此判断无候选|
|[Google Threat Intelligence / Mandiant](https://cloud.google.com/blog/topics/threat-intelligence)|200|10/0|按具体候选追原文与版本；未核准窗口事件不计入选|
|[Microsoft Security / MSRC](https://www.microsoft.com/security/blog/)|error|0/0|访问缺口已保留；未据此判断无候选|
|[Unit 42](https://unit42.paloaltonetworks.com/)|200|62/0|按具体候选追原文与版本；未核准窗口事件不计入选|
|[Cisco Talos](https://blog.talosintelligence.com/)|error|0/0|访问缺口已保留；未据此判断无候选|
|[腾讯玄武实验室](https://xlab.tencent.com/cn/)|200|4/0|按具体候选追原文与版本；未核准窗口事件不计入选|
|[腾讯科恩实验室](https://keenlab.tencent.com/zh/)|200|7/0|按具体候选追原文与版本；未核准窗口事件不计入选|
|[Anthropic Research / Frontier Red Team](https://www.anthropic.com/research)|200|5/0|按具体候选追原文与版本；未核准窗口事件不计入选|
|[OpenAI Security Research](https://openai.com/research/)|200|2/0|按具体候选追原文与版本；未核准窗口事件不计入选|
|[NIST Cybersecurity](https://www.nist.gov/cybersecurity)|200|30/0|按具体候选追原文与版本；未核准窗口事件不计入选|
|[CISA](https://www.cisa.gov/news-events/cybersecurity-advisories)|200|35/0|按具体候选追原文与版本；未核准窗口事件不计入选|
|[Gartner](https://www.gartner.com/en/cybersecurity)|error|0/0|访问缺口已保留；未据此判断无候选|
|[Forrester](https://www.forrester.com/security-risk/)|error|0/0|访问缺口已保留；未据此判断无候选|
|[IDC Security](https://www.idc.com/)|200|7/0|按具体候选追原文与版本；未核准窗口事件不计入选|

CVPR/ICCV额外访问day=all完整论文表；ICML额外读取v306整卷，相关链接均保存。AAAI入口返回HTTP200但未解析到论文，仍有覆盖缺口。SOSP页面零相关命中也仅为解析结果。NeurIPS使用官方Downloads/2026，CCS额外保存无链接表行。

arXiv补充cs.CR及cs.SE完整recent列表；cs.CR共253条含跨类记录。列表发布日期仅为入口标签，入选以v1原始UTC时刻换算北京时间。未逐篇核准的入口未充当无论文证据。

### 本期精读候选

|论文|事件（北京时间）|来源组|全文与状态|
|---|---|---|---|
|[ToolPulse: Side-Channel Eavesdropping on Tool-Using LLM Agents](https://arxiv.org/abs/2611.25470v1)|2026-11-19 v1首次公开|security|完整PDF已取得；预印，尚未同行评审|
|[Network-Exposed Configuration Attacks on LLM-Controlled Social Robots](https://arxiv.org/abs/2611.22761v1)|2026-11-17 v1首次公开|security|完整PDF已取得；预印，尚未同行评审|
|[When Tool Names Are Not Identities: Measuring Provider Misbinding in MCP-Based AI Agents](https://arxiv.org/abs/2611.21577v1)|2026-11-17 v1首次公开|security|完整PDF已取得；预印，尚未同行评审|
|[Slice Isolation-as-a-Service: An Isolation Mechanism to Proactively Defend Cross-Slice Attacks in 5G-Advanced and Beyond](https://arxiv.org/abs/2611.23826v1)|2026-11-18 v1首次公开|security|完整PDF已取得；预印，尚未同行评审|
|[Missing Security-Fix Backporting for GitHub Actions Workflows](https://arxiv.org/abs/2611.22519v1)|2026-11-17 v1首次公开|software|完整PDF已取得；预印，尚未同行评审|
|[On the Reliability of CyberGym Evaluation: Task Material Consistency and Reference-Target Identity](https://arxiv.org/abs/2611.25790v1)|2026-11-19 v1首次公开|software|完整PDF已取得；预印，尚未同行评审|
|[ChainAgent: Automated Chainable Vulnerability Discovery in PHP Web Applications](https://arxiv.org/abs/2611.25412v1)|2026-11-19 v1首次公开|software|完整PDF已取得；预印，尚未同行评审|
|[Tether: Verified Stateful Policy Engine for System-Level Monitoring of Agents](https://arxiv.org/abs/2611.25599v1)|2026-11-19 v1首次公开|ai|完整PDF已取得；预印，尚未同行评审|
|[PIPETTE: Prompt Injection Purple-Teaming for Robust LLM Agents](https://arxiv.org/abs/2611.24362v1)|2026-11-18 v1首次公开|ai|完整PDF已取得；预印，尚未同行评审|
|[GapLeak: When Privacy-Preserving LLM-based Web Agents Become a Privacy Risk](https://arxiv.org/abs/2611.22223v1)|2026-11-17 v1首次公开|ai|完整PDF已取得；预印，尚未同行评审|

10项均与208条现有记录按DOI→arXiv→正式URL→规范化标题核对，无重复。当前没有足够官方逐篇接收证据，全部保持预印。4/3/3软配额在候选层满足；正式会议新增0篇，偏离原因是本轮核准的窗口事件均为预印首次公开，会议静态表未提供可用于本窗口的逐篇日期。第二阶段逐篇确认质量后再锁定最终数量。

### 暂缓与缺证据

- Stargate和Memory Safety Isn’t All You Need的arXiv v1均为11月13日，虽出现在11月17日列表，仍属W47；未计入本期。DeCompCert与Bytes to Behavior保持旧首次事件，后续可回补W47或作为基础阅读。
- 两篇ISSTA观察项仍缺完整正文。Ghost原页可见的一个PDF实际属于另一篇Android恶意软件复现论文，已排除混用。Screen得DOI线索10.1145/3832268，待原始记录与全文核验。
- JC旧版比较与ADS-OT实验缺口保持；所有到期候选均更新last_checked=2026-11-23、target_week=W49及具体原因。安全范围暂缓项仍保持W50。

### 行业候选

固定14来源均已尝试。Microsoft主页及RSS、Talos主页及RSS访问失败，公开搜索回退亦有网络故障，明确保留缺口。正文与日期均已取得的5项：

|候选|日期证据|入选理由|
|---|---|---|
|GTIG ARMORY CASTLE/vSphere|正文可见11月20日；JSON-LD为11月19日，均在窗内|事件响应、样本和补丁证据|
|Unit42 OPTIMJACK|2026-11-17发布，UTC发布时间换算为11月18日|供应链入侵技术复盘|
|Unit42 Com电话钓鱼|2026-11-20发布，UTC时刻换算11月21日|事件调查与攻击链|
|NIST移动驾驶证项目|2026-11-19带时区发布时间|可核验草案与工程实践|
|CISA Java4Shell公告|2026-11-17官方正文|具体漏洞与修补指南|

正文均可访问且与73项观点库按URL、标题及来源日期去重，无重复；第二阶段才写入公开观点。NIST solopreneur、Anthropic披露政策与GTIG代理威胁文均为11月16日或更早，未计本期。咨询入口无可核验方法全文的内容不选。

### 第一阶段完成检查

- [x] 所有规定事实输入已读取；候选完成去重。
- [x] 预印标记、窗口事件、全文可用性和入选理由均有记录；无未经证实的接收判断。
- [x] 到期观察项已处理，缺正文与证据缺口已列明。
- [x] 三组全扫描、近4期分布、轮换与4/3/3软配额及正式来源偏离已记录。
- [x] 已形成10篇论文与5项行业精读候选；本阶段未生成正文分析。

第一阶段通过，进入第二阶段。

## 第二阶段：精读与落库

- [x] 十篇候选均阅读完整正文，结合方法图和结果表核对机制与数字；完整PDF及SHA-256见机器记录。
- [x] 十篇十四字段完整，顺序及1—5条名词解释通过程序检查；数字保留对象、分母和条件。
- [x] Easycatch随正文精读保存八步推理后生成，十篇两段正文写入唯一源文件；五项事实摘要逐项校验通过。
- [x] 三组4/3/3软配额最终保留；按主领域实际分为AI4、软件3、移动1、网络1、隐私1，来源组与主领域分别记录。
- [x] 索引按标识符和规范化标题去重；本期均为未同行评审预印，不把PDF模板当作接收证据。
- [x] 五条行业观点读取完整正文，记录证据、限制与商业利益；底层厂商公告/草案未全文复核的部分明确留空。
- [x] 作者署名和单位与正文匹配。Tether p1的Google与Google DeepMind已分开；参考arXiv反序作者元数据后统一为正文顺序。

第二阶段通过。第三阶段回查发现TADP正式接收证据后，返回第二阶段重读规则、正文方法/预算表/局限和Easycatch；修订限制与两段解释后再次校验，再进入维护。ReA-Bench v1/v2全文差异仅为数据入口，原卡已有v2说明，此次仅同步索引日期。

## 第三阶段：历史与实体维护

遍历208条历史索引；95条带arXiv记录均取得当前版本历史、Comments、期刊引用与DOI字段，包括全部33条预印、1条workshop及1条accepted-workshop状态。其余历史已接收条目结合本次官方列表扫描作题名比对，未把解析未命中当作撤销接收证据。详情与未核验清单见[历史核验记录](2026-W48-history.json)。

- TADP由WACV 2027官方接收列表核验题名及六位作者，在原W45条目升级，无精确日期时仅用会议年份显示。WACV不计现行三类CCF-A分数。
- Weakest Agent仅有arXiv作者的Meta-Agents Workshop接收说明，官网无逐篇记录，继续待核验。
- ReA-Bench原W47卡已有v2时间线与公开数据入口；索引last_updated纠正为11月16日。

新增作者实体均保存稳定ID及论文证据。已核实Shinan Liu/劉詩楠（HKU Scholars Hub）、Yun Chen/陈韵（HKUST(GZ)师资页）、Yeting Li/李页霆（本人主页）。新核实的英文主页另含Sajjad Dadkhah、Meghana Aparna Sistla、Alaia Solko-Breslin与N. Asokan。其他作者保留英文署名，待核验中文对应逐人在JSON列出。

单位核验按正文所在地维护；南方电网公司中文名由官方采购公告确认。CyberGym审计两作者单位未披露，暂列“论文未注明单位”，国家为空，该节点为待核验分组，不代表已知机构。Google和DeepMind未凭总部所在地填国家。

### 待人工补充全文与身份

|对象|优先级|可靠入口|需要补充|
|---|---|---|---|
|Ghosts in Memory|高|原ISSTA链接保存在watchlist|完整正文及实验表，现有PDF为其他论文|
|How Safe Is Your Screen?|高|原ISSTA链接保存在watchlist|正文及10.1145/3832268原始DOI核验|
|Yule Ding、Hongzhen Wu|中|https://arxiv.org/pdf/2611.25790v1|作者单位、本人主页及一一对应|
|英文署名的中文对应|低|逐人清单见history.json|有明确论文、单位对应的官方个人页|


公司中文全称核实后再回第二阶段复核ChainAgent原文披露和动态验证条件，移除卡片里已过期的待核验说明；同步复核Easycatch，补入发现后验证步骤并升至revision2。

### 构建与本地交互验证

- [x] 完整读取本阶段事实文件与构建/发布流程；119/208条历史题名在本次官方列表解析中命中，其余未命中保持原证据，不作否定推断。
- [x] --check、正式构建及构建后--check通过。218篇论文全部有精读及Easycatch，20期、6主领域、78条行业观点。
- [x] 218篇均有作者映射，1043位学者、514条单位合作边、278个单位分组；其中“论文未注明单位”为1个临时未知分组。每位学者最近论文不超过3条。已核验三类顶会计分保持157篇。
- [x] 独立Chrome本地静态页面在1440px及390px验证作者/排行进入学者、最近论文进入论文、返回恢复、同论文循环截断历史；单弹层、日期、名词解释及三入口正常。全文搜索Flush命中ToolPulse，无页面异常、手机横向溢出或公开配额说明。
- [x] 26项Python、5项JavaScript检查通过。旧测试把未来期固定W48，本期已成为真实窗口；改为从最新已声明窗口推算下一周，恢复对未声明窗口的实际检查。
- [x] 合并远端7次仅流量图自动更新；运行前7个用户修改的二进制差异与初始快照逐字节一致，保持不暂存。
- [x] 首页数据资源版本由v7升v8，避免普通URL继续使用旧目录。内容哈希数据由构建器生成且不入Git。

浏览器控制接口两次连接超时，改用临时独立配置的Chrome通过本地文件URL检查；HTTP本地服务本身返回200。详细检查记录保存在运行临时目录，最终发布状态以推送后工作流及普通公开URL核验为准。

### 资源变更

更新周报、事实索引及5条行业观点，新增来源和历史核验记录；维护关系图与公开数据目录，修复1条随周次老化的测试。未创建服务器、订阅或付费API任务，使用既有GitHub Pages流程。临时目录保存PDF与解析/浏览器检查输出，Python解析依赖仅装入临时目录。模型/工具实际资费未提供，无法核算金额。

待提交树已独立导出，在不带用户未提交构建器改动的环境下再次通过--check、正式构建和26项Python测试。周报末尾追踪说明使用模板列表格式，确认未被解析为最后一篇论文的推荐理由。
