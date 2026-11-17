# 2026-W45 重做：时间窗口与来源证据

最终结果：4篇动态，缺6篇；主题来源组2/1/1。正式会议0篇、预印4篇。历史十篇已独立迁移，过往误补审计另存归档。

本期窗口：2026-10-27 至 2026-11-02（北京时间）。实际回溯检索：2026-11-17。此前用历史基线补数的结论撤销，旧审计记录见 [归档](../archive/2026-W45-superseded-20261117.md)。首次被整理者发现不构成窗口内更新。

## 第一阶段：重新检索

完整读取01及索引、观察清单、14来源池、观点库、本期原周报与inquiry。先处理有到期窗口事件的候选；两个ISSTA缺正文项仍等待W48，长程综述仍W50，不把旧观察记录视为新进展。扫描三组全部21会议，按 CCS→NDSS→USENIX→S&P；ISSTA→FM→其余；ICLR→ICML→其余 轮换。

| 来源 | 实际访问 | 相关链接样例数（最多12个） | 时效门槛处理 |
|---|---|---:|---|
| [CCS](https://www.sigsac.org/ccs/CCS2026/program/accepted-papers.html) | 200 | 0 | 200仅说明入口可读；未取得窗口内版本/出版事件的条目不入选，超时/403/机器人不等于无论文 |
| [NDSS](https://www.ndss-symposium.org/ndss2026/accepted-papers/) | 200 | 12 | 200仅说明入口可读；未取得窗口内版本/出版事件的条目不入选，超时/403/机器人不等于无论文 |
| [USENIX](https://www.usenix.org/conference/usenixsecurity26/technical-sessions) | 200 | 12 | 200仅说明入口可读；未取得窗口内版本/出版事件的条目不入选，超时/403/机器人不等于无论文 |
| [S&P](https://sp2026.ieee-security.org/accepted-papers.html) | 200 | 12 | 200仅说明入口可读；未取得窗口内版本/出版事件的条目不入选，超时/403/机器人不等于无论文 |
| [ISSTA](https://conf.researchr.org/track/issta-2026/issta-2026-research-papers) | 200 | 12 | 200仅说明入口可读；未取得窗口内版本/出版事件的条目不入选，超时/403/机器人不等于无论文 |
| [FM](https://conf.researchr.org/track/fm-2026/fm-2026-research-paper) | 200 | 1 | 200仅说明入口可读；未取得窗口内版本/出版事件的条目不入选，超时/403/机器人不等于无论文 |
| [SOSP](https://sigops.org/s/conferences/sosp/2026/accepted.html) | 200 | 0 | 200仅说明入口可读；未取得窗口内版本/出版事件的条目不入选，超时/403/机器人不等于无论文 |
| [ASE](https://conf.researchr.org/track/ase-2026/ase-2026-research-track) | 200 | 12 | 200仅说明入口可读；未取得窗口内版本/出版事件的条目不入选，超时/403/机器人不等于无论文 |
| [ICSE](https://conf.researchr.org/track/icse-2026/icse-2026-research-track) | 200 | 12 | 200仅说明入口可读；未取得窗口内版本/出版事件的条目不入选，超时/403/机器人不等于无论文 |
| [OOPSLA](https://2026.splashcon.org/track/oopsla-2026) | 200 | 12 | 200仅说明入口可读；未取得窗口内版本/出版事件的条目不入选，超时/403/机器人不等于无论文 |
| [PLDI](https://conf.researchr.org/track/pldi-2026/pldi-2026-papers) | 200 | 5 | 200仅说明入口可读；未取得窗口内版本/出版事件的条目不入选，超时/403/机器人不等于无论文 |
| [POPL](https://conf.researchr.org/track/popl-2026/POPL-2026-popl-research-papers) | 200 | 12 | 200仅说明入口可读；未取得窗口内版本/出版事件的条目不入选，超时/403/机器人不等于无论文 |
| [FSE](https://conf.researchr.org/track/fse-2026/fse-2026-research-papers) | 200 | 12 | 200仅说明入口可读；未取得窗口内版本/出版事件的条目不入选，超时/403/机器人不等于无论文 |
| [OSDI](https://www.usenix.org/conference/osdi26/technical-sessions) | 200 | 5 | 200仅说明入口可读；未取得窗口内版本/出版事件的条目不入选，超时/403/机器人不等于无论文 |
| [ICLR](https://iclr.cc/virtual/2026/papers.html) | 200 | 12 | 200仅说明入口可读；未取得窗口内版本/出版事件的条目不入选，超时/403/机器人不等于无论文 |
| [ICML](https://proceedings.mlr.press/) | 200 | 0 | 200仅说明入口可读；未取得窗口内版本/出版事件的条目不入选，超时/403/机器人不等于无论文 |
| [AAAI](https://ojs.aaai.org/index.php/AAAI/issue/archive) | 200 | 0 | 200仅说明入口可读；未取得窗口内版本/出版事件的条目不入选，超时/403/机器人不等于无论文 |
| [NeurIPS](https://proceedings.neurips.cc/paper_files/paper/2025) | 200 | 1 | 200仅说明入口可读；未取得窗口内版本/出版事件的条目不入选，超时/403/机器人不等于无论文 |
| [ACL](https://aclanthology.org/events/acl-2026/) | curl: (28) Operation timed out after 25001 milliseconds with 3735939 out of 18926839 bytes received  | 0 | 200仅说明入口可读；未取得窗口内版本/出版事件的条目不入选，超时/403/机器人不等于无论文 |
| [CVPR](https://openaccess.thecvf.com/CVPR2026) | 200 | 0 | 200仅说明入口可读；未取得窗口内版本/出版事件的条目不入选，超时/403/机器人不等于无论文 |
| [ICCV](https://openaccess.thecvf.com/ICCV2025) | 200 | 0 | 200仅说明入口可读；未取得窗口内版本/出版事件的条目不入选，超时/403/机器人不等于无论文 |
| [Google Project Zero](https://googleprojectzero.blogspot.com/) | curl: (28) Connection timed out after 25006 milliseconds  | 0 | 200仅说明入口可读；未取得窗口内版本/出版事件的条目不入选，超时/403/机器人不等于无论文 |
| [Google Threat Intelligence / Mandiant](https://cloud.google.com/blog/topics/threat-intelligence) | curl: (28) Connection timed out after 25005 milliseconds  | 0 | 200仅说明入口可读；未取得窗口内版本/出版事件的条目不入选，超时/403/机器人不等于无论文 |
| [Microsoft Security / MSRC](https://www.microsoft.com/security/blog/) | curl: (28) Operation timed out after 25003 milliseconds with 0 bytes received  | 0 | 200仅说明入口可读；未取得窗口内版本/出版事件的条目不入选，超时/403/机器人不等于无论文 |
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

### 候选与决定

- Jailbreak Connectivity，arXiv:2610.38091v1，原始元数据2026-10-28，完整10页PDF；AI安全预印候选，未有正式接收证据。
- RoleFUZZER，arXiv:2610.38438v1，2026-10-28，完整31页PDF；AI角色约束测试预印候选。
- GI-RTL-Fuzz，2610.38489，正文9页可读；仿真器一致性未直接证实安全漏洞，暂缓，不为软件组配额降低安全相关性。
- Adaptive Dynamic Security for OT，2610.41007，正文9页；为示意性模拟场景，原文单位及可复现实验细节不足，暂缓。
- DIFUZZI，2610.38337，仅确认功能相似性测试定位，独立安全贡献不足，未进入精读。
- SEAL 2610.25372、SecureSD 2610.08678、PEV 2610.07125：首次日期早于窗口；未查得窗口内实质更新证据，排除。Atomic Security Concerns为概念假说；不拿未经验证的概念充数。

两篇选中候选均按DOI、arXiv ID、URL、规范标题检查178条索引，无重复。候选全文为逐篇下载的有效PDF，不以搜索摘要代替。

- [x] 全量读取事实输入；完成三组会议及14行业来源尝试。
- [x] 候选去重、状态与正文可用性记录；没有作者模板推断接收。
- [x] 窗口内事件明确，预印保留未同行评审状态。
- [x] 暂缓、缺正文和来源访问缺口均明确，未编造分析。
- [x] 阶段一完成，允许进入正文精读；不足不拿旧论文补数。

## 第二阶段完成

- [x] 最终4篇新增均有窗口内版本/出版事件与完整正文，按14字段顺序和1—5术语整理。
- [x] 同次正文阅读先保存8步推理与Easycatch草稿，再写卡片；摘要仅作一致性校验。
- [x] 原十篇精读与Easycatch迁入独立基础阅读，未改事实字段，旧周报引用保存为previous_weekly_notes。
- [x] 新增按四级去重；预印未写成正式接收，标签受控、主领域唯一。
- [x] 既有行业内容保留正文证据及商业利益边界，未追加未读内容。
- [x] 最终来源组2/1/1，目标4/3/3缺额2/2/2，总缺6。来源按主题归组，正式会议命中与预印分别列出；不宣称来源总量不足。

### 第一阶段补充检索后重新检查

发现JC已有 ICLR2026 GRaM Tiny Paper同作者早期稿（https://openreview.net/attachment?id=lLRjocW97b&name=pdf），早期PDF返回403/验证页，无法完成实质扩展逐项比较，故撤回JC入选，保留精读草稿待版本证据。不能把arXiv新ID自动认定为首次公开。

追加候选：Maven上游安全事件研究2610.36603（10-27，11页）、Silent Blindness2610.36612（10-27，9页）、TADP2610.41642（10-30，19页），原始abs元数据和完整PDF均取得，四级去重无现有命中。三篇分别补充软件供应链、硬件检测器与隐私机制。第一阶段检查重新通过，再进入原文阅读。

## 第二阶段完成

- [x] 最终4篇新增均有窗口内版本/出版事件与完整正文，按14字段顺序和1—5术语整理。
- [x] 同次正文阅读先保存8步推理与Easycatch草稿，再写卡片；摘要仅作一致性校验。
- [x] 原十篇精读与Easycatch迁入独立基础阅读，未改事实字段，旧周报引用保存为previous_weekly_notes。
- [x] 新增按四级去重；预印未写成正式接收，标签受控、主领域唯一。
- [x] 既有行业内容保留正文证据及商业利益边界，未追加未读内容。
- [x] 最终来源组2/1/1，目标4/3/3缺额2/2/2，总缺6。来源按主题归组，正式会议命中与预印分别列出；不宣称来源总量不足。

### 最终候选与配额修正

W45最终4篇：RoleFUZZER、Maven生命周期、Silent Blindness、TADP。组别按主题为安全2/软件系统1/AI1（均为arXiv预印，无正式会议命中），距4/3/3缺2/2/2，总缺6。上方两篇初选及0/0/N为中间审计状态，JC已撤回。

完整正文核对了Maven的832CVE全集、593上游时间子集及1677采用关系子集；HMD保留128/140配置口径冲突，不合并摘要与结论数字；TADP区分单16帧与全视频联合预算。所有Easycatch在相应原文阅读后、卡片写入前保存。

新增Queen’s University、San Francisco State University、Worcester Polytechnic Institute有论文明确地域证据。Queen’s 的Yuan Tian与既有UCLA同名学者分设稳定ID并使用单篇override，不以同名合并。新增Aylin主页来自学校官方页；Feng Xu、Xun Li、Yulei Sui、Dadong Wang、Enrong Pan等中文名暂无一一对应证据，保留原署名。

## 第三阶段：发布前完成检查

近四期W41—W44按当前归属统计：{'security': 16, 'software': 12, 'ai': 12, 'other': 0}，共40篇，已逐会议扫描并优先补充覆盖不足组。历史8项风险记录及新增4项元数据回查未有其他状态升级；既有Not an A11y工作坊及WASP/MCPTox更正保留。

- [x] 完整读取03和列出的事实、构建、发布文件；稳定ID与作者单位映射通过。
- [x] 基础阅读10篇独立归档、W45动态4篇，时效事件全部在窗口内，未混入旧文。
- [x] --check与正式构建通过；182篇及缓存，6领域、73观点、235单位、871学者、423合作边；182篇署名全覆盖，recent_papers≤3。
- [x] 24项Python与5项JS测试通过，包括拒绝缺事件和窗口外日期。
- [x] 本地Chrome实测基础专题、全文搜索、精读、日期、学者/排行/最近论文、返回、单弹层及循环截断，无JS错误。
- [x] 用户原改动保持；仅提交新增功能/规则/数据，构建器用户hunk排除。

推送及Pages的后验核验记入自动化memory及最终报告，发布前不预填成功。
