# 2026-W47 来源覆盖与核验记录

> 十篇补齐更正：原先三篇编辑范围理由撤回，旧记录仅保留审计；本轮以文末记录为准。W45、W46 已依次补至十篇并发布核验，后者21c1d1aa / Pages43869881119。

窗口为 2026-11-10—11-16（北京时间），本次检索、精读与发布实际在 11 月 16 日进行。W45、W46 均已按顺序发布且线上核验通过；W46 提交 `1b0aecb`，Pages 工作流 43835274702 成功。继续按检索、精读、维护发布三个阶段串行执行，保留运行前七处用户改动。

## 输入与来源均衡

阶段入口重新完整读取检索分片、154 条索引、3 条观察队列、14 个固定行业来源、70 条观点和最新 W46 周报；本期此前没有 inquiry。按 DOI、arXiv ID、规范 URL、规范标题去重，三个新增候选均未入库；Not an A11y 保留原 ID，只作历史状态变化。

W43—W46 共 26 篇：安全 10（38.5%）、软件与系统 8（30.8%）、AI 8（30.8%）。具体来源为 NDSS 4、OSDI 3、S&P 2、CCS 2、USENIX Security 2、NeurIPS 3（2025 两篇、2024 一篇），PLDI、POPL、ACL、ICML、CVPR、FSE、OOPSLA、ICSE、AAAI、ICLR 各一篇。SOSP、FM、ISSTA、ASE、ICCV 近期新增为零，优先检查其覆盖缺口。

本次轮换从软件系统组的 FM 开始，依次检查该组其他会议，再从 NDSS 检查安全组，从 ICCV 检查 AI 组；最后补 arXiv。完整网络扫描发生两遍，后一遍按上述顺序并修正 PLDI、FM track 路径。实际新增精读按 1/1/1 分配：SymCC（USENIX Security 2020）、iLand（OSDI 2026）、CaMeL（SaTML 2026）。SaTML 为额外 AI 安全正式来源，未因此扩大现行 CCF 计分范围。相对 4/3/3 软目标缺 3/2/2；少收录是此次逐期精读与验证的编辑取舍，不能声称其他会议缺乏合格论文。历史升级单独统计，不占新增名额。

## 全部会议覆盖

候选数仅记录明确推进的全文项目，非会议全部安全论文数。入口 URL 沿用 [W45 完整地址表](2026-W45-source-coverage.md)，本次修正与具体条目另列。

| 会议 | 扫描、筛选与未推进原因 | 候选 / 新增 |
| --- | --- | --- |
| FM | 正确 research-paper track 可读；Privacy-Preserving Verification，未推进全文 | 0 / 0 |
| SOSP | SIGOPS 2026 接收入口可读，当前题目匹配未产生本期正文候选 | 0 / 0 |
| ISSTA | 官方 track 可读；两项到期观察项目仍缺正文，不按摘要代写 | 2 / 0 |
| ASE | 官方研究 track，安全测试与代理相关项目未推进原文 | 0 / 0 |
| ICSE | 官方程序及 TaintP2X 等既有项重复 | 0 / 0 |
| OOPSLA | SPLASH track，漏洞检测与 Maven 修复线索未推进正文 | 0 / 0 |
| PLDI | 修正为 pldi-2026-papers；SuperDP 和差分隐私验证条目，未推进全文 | 0 / 0 |
| POPL | 官方研究入口，安全编译及已有 Security Reasoning，未推进新增 | 0 / 0 |
| FSE | 官方 track，已有 PoCGen、日志与二进制相似性条目重复 | 0 / 0 |
| OSDI | 全程序和 iLand 单篇官方页/PDF；UCSan、Osprey 已在前两期收录 | 1 / 1 |
| NDSS | 完整接收页；SAGA、Anota 及既有项重复，其他题目未推进正文 | 0 / 0 |
| CCS | 2026 接收入口可达但当前静态题目提取为空，不把此结果当作没有安全论文 | 0 / 0 |
| S&P | 2026 接收入口可达，既有项目与 IJON 线索，后者继续暂缓 | 0 / 0 |
| USENIX Security | 2026 技术程序及 SymCC 2020 正式页面和完整 PDF，推进历史基线 | 1 / 1 |
| ICCV | CVF 2025 目录可读，JailbreakDiffBench 等视觉论文未推进正文 | 0 / 0 |
| ICLR | 2026 列表，source inference 与 prompt sanitization；AgentHarm 已收录 | 0 / 0 |
| AAAI | archive 返回 200 但有机器人验证；以既有 MCPTox 正式文章替代，未新增 | 0 / 0 |
| ACL | 全目录下载超时；以既有 Conjunctive 与 Fingerprinting 官方具体条目补查，不声称目录已完整下载 | 0 / 0 |
| CVPR | CVF 2026 目录可达，AgentSafe 等既有项目重复 | 0 / 0 |
| ICML | PMLR 入口，PrivAct 已有；未推进其他候选 | 0 / 0 |
| NeurIPS | 2025 正式论文集可读；既有条目重复，WASP 正式链接仍需补齐 | 0 / 0 |
| 额外 SaTML | [2026 官方接收表](https://satml.org/2026/accepted-papers/) 精确列出 Defeating Prompt Injections by Design，Crossref DOI 10.1109/SaTML68715.2026.00040，作者完整版本可读 | 1 / 1 |
| arXiv 补充 | CaMeL v2、Not an A11y v1、七项历史预印；后者登记 AGENT-SEC workshop DOI，作历史升级候选 | 1 历史 / 0 |

三篇候选的完整 PDF 已取得：SymCC 与 iLand 为 USENIX 正式版，CaMeL 为 arXiv 作者 v2。CaMeL 会场作者单位与作者版存在时间差，后续按具体版本区分，不猜测当前单位。IEEE/ACM 正式 PDF 若遇反爬，明确记录，不能据此捏造版本差异。

## 历史变更与观察项

- *Not an A11y*：[出版 DOI](https://doi.org/10.1145/3847320.3847397) 的 Crossref 登记为 2026-11-14，AGENT-SEC 2026 workshop，题目和五位作者可对应；可读取 arXiv v1 正文。第二阶段回读正文和原 W33 卡片，再更新原索引、日期、姓名别名及受影响表述。workshop 不写成 CCS 主会。
- *Ghosts in the Memory*、*How Safe is Your Screen*：复查官方单篇入口仍未取得公开完整 PDF，顺延 W48。高优先级分别核对内核插桩与敏感数据采样/披露链、UI 模型与隐私判定/披露链；摘要中的数字不进入精读。链接沿用 W46 inquiry。
- 长时程综述仍按 W46 实际检查结果暂缓到 W50，未到本期目标，不重复当作新发现。

## 行业来源与初筛

| 固定来源 | 实际访问和处理 |
| --- | --- |
| Project Zero | 旧入口超时，现有紧急补丁内容已收录，覆盖缺口保留 |
| GTIG / Mandiant | 入口超时，未把失败解释为没有新内容 |
| Microsoft | 主页 403；官方 RSS 完整正文可读，kernel 59 bugs、sleeper agents、post-training、SCKit 入初筛 |
| Unit 42 | 主页/RSS/单篇可读，CAIRN、ARTEX、Falcon 三项 |
| Talos | 主页 403；官方 RSS 完整正文可读，ARTEX 调研和补丁星期二 |
| 玄武 | 归档可读，未推进窗口内正文候选 |
| 科恩 | 归档可读，未推进窗口内正文候选 |
| Anthropic | 研究入口可读，既有项目重复，未推进新增 |
| OpenAI | 403，保留访问缺口 |
| NIST | 可读，IR 8547 前期已收录 |
| CISA | 通告页可达，KEV 已在 W46 分析，避免重复 |
| Gartner | 403，缺正文和方法，排除预测 |
| Forrester | 原入口 404，W46 替代归档未见推进证据，不以观点填数 |
| IDC | 页面可读，活动与市场推广未入选 |

至少五篇初筛后选三篇全文分析：Microsoft 11-11 *Lessons from 59 Linux Kernel Bug Reports*、Unit 42 11-12 CAIRN 自主攻击调查、Talos 11-13 ARTEX 平台调研。其余 sleeper、post-training、SCKit、Falcon 等为本轮未推进，避免把有限篇幅全部集中在同一产品或攻击框架。各项按 RSS 时区转换后都位于 W47，北京时间分别为 11-12、11-12、11-14；源字段保留发布方原始文章日期，窗口解释另写于此。行业观点仅在完整阅读后写入。

## 第一阶段完成检查

- [x] 全部事实输入已重新读取，用户改动继续隔离。
- [x] DOI、arXiv、正式 URL 和规范标题去重，历史更新不新增 ID。
- [x] 三篇接收身份分别由 USENIX 与 SaTML 正式页面证明，workshop 身份以出版 DOI 为据。
- [x] 作者版与预印标识区分，未凭作者自述升级。
- [x] 三篇新增和一篇历史更新的可读正文已取得，行业三项完整正文可读。
- [x] 两项到期缺正文候选已注明缺口、日期、目标周。
- [x] 第二阶段候选明确，正文精读与 Easycatch 待下一阶段同步执行。
- [x] 近四期、轮换、全部会议和行业来源、软配额及偏离原因均记录。
- [x] 本阶段没有根据摘要写入公开论文分析或行业观点。

## 第二阶段证据边界与待核验事项

- CaMeL 所读作者 v2 的摘要约 77%/84%，与新模型表 2 不同；正文 Gemini 2.5 Pro 示例写 300 次，而表 4 为 163；图 11 称工具过滤为 next best，但表 7 spotlighting 为 5、tool filter 为 8；正文与附录表 10/13 的 token 中位数、输入/输出对应也不一致。周报只引用明确表格和模型，不替作者统一。实现形式验证在未来工作中，不能据摘要 provable 一词声称已有完整实现证明。
- CaMeL 正式身份由 SaTML 接收表和 Crossref DOI 登记共同核验；IEEE PDF 下载实际返回 HTML，未读取正式版。作者与单位按可读 2025 v2 署名，会场列表 Nicholas Carlini 等单位已变，未将不同时间单位静默混用。若需逐页比较正式版，待人工补充其明确 PDF 路径。
- Not an A11y 的正式 DOI、日期、作者和单位可由 Crossref 出版登记对应；ACM PDF 被反爬阻断，正文使用 arXiv v1，已逐章回读方法、420 个试次、结果与附录。原卡片保留图 4 汇总数字，明确框架攻击矩阵不同；A9 属独立规划通道。正式内容逐页差异尚待 PDF，未臆测新增结果。
- iLand 正文 §9.1 写 60 个应用，§9.4 与结论为 64 个兼容性样本、60 个后续行为研究样本。采用后者并明确分母；表 4 个别比值超出文字概括的 15—90 范围，文字范围按作者描述，保留精确表格。未把私有 API 归类等同恶意判定。
- Kaitao Xie、Yizhuo Wang、Xiaolong Bai、Tianqi Fan、Chongyang Shi 等没有取得一一对应中文姓名证据，保留正式英文，待学校/个人主页明确对应后更新。
- 两篇 ISSTA 仍待人工补充完整正文，可靠入口和需核验章节已列前文；没有据摘要填写卡片。

## 第二阶段完成检查

- [x] 三篇新增及一篇历史正文重新精读方法、实验、局限；关键表格 PDF 第 15/11/33/9 页已渲染核对。
- [x] 三篇新增各 14 字段顺序完整，每篇两个名词解释；原 W33 卡片同步修正。
- [x] Easycatch 在逐篇原文阅读中先形成八项内部推理与两段正文，再写字段；新增 revision 1、历史实际重写 revision 4，均 skill 4。
- [x] 机制、例子、数字条件和反例齐全，未从卡片事后二次生成 Easycatch。
- [x] 日期只写版本时间线，workshop 与主会分开，预印作者版与正式身份分开。
- [x] 新增插桩标签先入分类表，三个主领域显式指定，不扩大会议信号。
- [x] 正式署名和可读作者版本匹配，身份变动与中文姓名缺口列出。
- [x] 四级去重，历史原条目更新且保留稳定 ID；两个缺正文观察项顺延 W48。
- [x] 三条行业内容阅读全文，来源、证据、局限和商业利益字段完整。
- [x] 索引、周报、Easycatch、观察清单和行业唯一源同步完成。

## 第三阶段检查与发布门禁

- [x] 再次读取维护分片、完整事实表、Easycatch 与 skill、W47/W33/W44 周报、inquiry、构建器和 Pages workflow；Git 用户改动单独保留。
- [x] 七项原预印与 Adaptive 的 arXiv 当前页逐项回查；Self-State v2、Adaptive v2 早已处理，其余无新版本。Not an A11y 原位升级；WASP 通过精确标题重新找到 NeurIPS 正式集与 DOI，原状态保持。
- [x] 新增 12 个稳定学者、4 个单位记录，Zagreb 学院通过大学官网明确 parent，图中按大学归并。Faatin Alvi 保留 faatin-alvi ID，以完整出版署名显示并保留旧别名。
- [x] 已核实七个可打开主页：Poeplau、Francillon、Bai、Shumailov、Hayes、Shi、Terzis；Poeplau/Pöplau 对应由本人主页明确说明。其余人名按论文正式署名，中文名未猜测。
- [x] 阿里巴巴集团用官网中文名称，Google DeepMind 用官方 About。两个跨国单位未由论文确定具体团队所在地，country_code 留空；Google DeepMind 的具体上级归并来源请求未成功，不凭品牌相近合并。
- [x] --check 首次仅 README 自动计数过期，已修正并重新 --check、正式构建通过。157 篇与精读全覆盖，六主领域、73 行业观点、215 单位、763 学者、322 合作边；137 篇为现行已核验计分下界，所有最近论文最多三篇。
- [x] 20 项 Python、5 项 JavaScript 测试通过；网络重试报错为测试内故障模拟。
- [x] 独立临时 Chrome 实测论文作者、排行姓名、学者最近论文、返回、循环历史截断、单弹层、日期、详情名词解释与三入口全部通过，无 JS 错误，截图已检查。
- [x] Easycatch 四项新增/复核摘要一致，无维护阶段补写；原有未变条目没有批量刷新。
- [x] 七处用户补丁提交前逐字节核对，明确列出本期暂存文件；推送后持续核验 Pages 和线上资产，未成功前不交付完成结论。最终 SHA、运行 URL 与 HTTP 结果记入自动化 memory 和本次最终报告。

### 可靠实体来源

- [Poeplau 本人页与姓名别名](https://www.s3.eurecom.fr/~seba/)、[EURECOM Francillon 页](https://www.eurecom.edu/fr/people/francillon-aurelien)、[Xiaolong Bai 本人页](https://xiaolongbai.weebly.com/)。
- [Shumailov 学校个人页](https://www.cl.cam.ac.uk/~is410/)、[Jamie Hayes 本人页](https://jamiehay.es/)、[Chongyang Shi 本人页](https://chongya.ng/)、[Andreas Terzis 本人页](https://aterzis-personal.github.io/aterzis/)。个人页与论文署名年份可能不同；图中单位仍基于库内论文署名聚合，不将其声称为实时任职履历。
- [Zagreb 大学学院归属与所在地](https://www.unizg.hr/homepage/international-exchange/exchange-students/engineering/)、[学院官方地址](https://www.fer.unizg.hr/en/about/general_info)。
- [阿里巴巴集团官方中文介绍](https://ali-home.alibaba.com/about-alibaba)、[Google DeepMind 官方介绍](https://deepmind.google/about/)。
- [WASP 正式论文集](https://proceedings.neurips.cc/paper_files/paper/2025/hash/1c9818387f5dd0a0bc151214660f059d-Abstract-Datasets_and_Benchmarks_Track.html)，DOI 10.52202/085713-0666。


## 十篇补齐：第一阶段重新执行

重新全文读取01分片、171条索引、3条观察队列、14个行业来源、73条行业观点、最新与当期W47完整周报/inquiry，并检查用户七文件补丁。W43—W46新增40篇：安全16、软件12、AI12，占40%/30%/30%；四个安全会各4篇，软件OSDI3、ICSE3、PLDI2、POPL/FSE/OOPSLA/ISSTA各1，AI NeurIPS3、ACL/ICML/AAAI/ICLR各2、CVPR1。

组内轮换从 CCS、POPL、CVPR 开始，再扫描全部21个会议和arXiv补充。以下候选数仅计明确推进的新增全文项目，未推进不等于会议没有安全论文。

| 来源 | 本轮扫描结果与原始入口 | 明确候选 / 新增入选 |
| --- | --- | --- |
| CCS | https://www.sigsac.org/ccs/CCS2026/program/accepted-papers.html；200；Directed Greybox Fuzzing官方CCS论文镜像及DOI | 1 / 1 |
| NDSS | https://www.ndss-symposium.org/ndss2026/accepted-papers/；200；FUZZILLI官方2023接收页与完整PDF | 1 / 1 |
| USENIX | https://www.usenix.org/conference/usenixsecurity26/technical-sessions；200；目录筛选；重复/无本期推进项 | 0 / 0 |
| S&P | https://sp2026.ieee-security.org/accepted-papers.html；200；Spectre官方2019程序+作者完整PDF | 1 / 1 |
| POPL | https://conf.researchr.org/track/popl-2026/POPL-2026-popl-research-papers；超时；JFlow作者原文与项目正式引用 | 1 / 1 |
| SOSP | https://sigops.org/s/conferences/sosp/2026/accepted.html；200；目录筛选；重复/无本期推进项 | 0 / 0 |
| FM | https://conf.researchr.org/track/fm-2026/fm-2026-research-paper；200；目录筛选；重复/无本期推进项 | 0 / 0 |
| ISSTA | https://conf.researchr.org/track/issta-2026/issta-2026-research-papers；200；目录筛选；重复/无本期推进项 | 0 / 0 |
| ASE | https://conf.researchr.org/track/ase-2026/ase-2026-research-track；200；目录筛选；重复/无本期推进项 | 0 / 0 |
| ICSE | https://conf.researchr.org/track/icse-2026/icse-2026-research-track；超时；目录筛选；重复/无本期推进项 | 0 / 0 |
| PLDI | https://conf.researchr.org/track/pldi-2026/pldi-2026-papers；200；目录筛选；重复/无本期推进项 | 0 / 0 |
| FSE | https://conf.researchr.org/track/fse-2026/fse-2026-research-papers；超时；目录筛选；重复/无本期推进项 | 0 / 0 |
| OOPSLA | https://2026.splashcon.org/track/oopsla-2026；200；目录筛选；重复/无本期推进项 | 0 / 0 |
| OSDI | https://www.usenix.org/conference/osdi26/technical-sessions；200；TaintDroid官方2010全文 | 1 / 1 |
| CVPR | https://openaccess.thecvf.com/CVPR2026；200；目录筛选；重复/无本期推进项 | 0 / 0 |
| ICCV | https://openaccess.thecvf.com/ICCV2025；200；目录筛选；重复/无本期推进项 | 0 / 0 |
| ICML | https://proceedings.mlr.press/；200；Image Hijacks PMLR正式记录+arXiv作者完整PDF | 1 / 1 |
| ICLR | https://iclr.cc/virtual/2026/papers.html；200；目录筛选；重复/无本期推进项 | 0 / 0 |
| ACL | https://aclanthology.org/events/acl-2026/；200；目录筛选；重复/无本期推进项 | 0 / 0 |
| NeurIPS | https://proceedings.neurips.cc/paper_files/paper/2025；200；Jailbroken正式论文集与完整PDF | 1 / 1 |
| AAAI | https://ojs.aaai.org/index.php/AAAI/issue/archive；200；目录筛选；重复/无本期推进项 | 0 / 0 |
| Google Project Zero | https://googleprojectzero.blogspot.com/；超时；目录筛选；重复/无本期推进项 | 0 / 0 |
| Google Threat Intelligence / Mandiant | https://cloud.google.com/blog/topics/threat-intelligence；超时；目录筛选；重复/无本期推进项 | 0 / 0 |
| Microsoft Security / MSRC | https://www.microsoft.com/security/blog/；403；目录筛选；重复/无本期推进项 | 0 / 0 |
| Unit 42 | https://unit42.paloaltonetworks.com/；200；目录筛选；重复/无本期推进项 | 0 / 0 |
| Cisco Talos | https://blog.talosintelligence.com/；403；目录筛选；重复/无本期推进项 | 0 / 0 |
| 腾讯玄武实验室 | https://xlab.tencent.com/cn/；200；目录筛选；重复/无本期推进项 | 0 / 0 |
| 腾讯科恩实验室 | https://keenlab.tencent.com/zh/；200；目录筛选；重复/无本期推进项 | 0 / 0 |
| Anthropic Research / Frontier Red Team | https://www.anthropic.com/research；200；目录筛选；重复/无本期推进项 | 0 / 0 |
| OpenAI Security Research | https://openai.com/research/；403；目录筛选；重复/无本期推进项 | 0 / 0 |
| NIST Cybersecurity | https://www.nist.gov/cybersecurity；200；目录筛选；重复/无本期推进项 | 0 / 0 |
| CISA | https://www.cisa.gov/news-events/cybersecurity-advisories；200；目录筛选；重复/无本期推进项 | 0 / 0 |
| Gartner | https://www.gartner.com/en/cybersecurity；403；目录筛选；重复/无本期推进项 | 0 / 0 |
| Forrester | https://www.forrester.com/security-risk/；超时；目录筛选；重复/无本期推进项 | 0 / 0 |
| IDC Security | https://www.idc.com/；200；目录筛选；重复/无本期推进项 | 0 / 0 |


候选七篇均有完整正文并有独立正式身份依据；Image Hijacks 从论文集原始GitHub下载不完整（0页），已排除该损坏文件，改用完整13页arXiv作者版，未依据损坏正文精读。四层去重171条索引无重复。Spectre保留2019 SP身份，与2020 CACM版本及后续防御论文区分；TaintDroid保留2010 OSDI，与2014扩展稿区分；JFlow作者当时在MIT，不能用当前Cornell主页替换发表署名。

新增安全3篇、软件2篇、AI2篇，连同既有SymCC、iLand、CaMeL共10篇。按安全相关主题组为4/3/3，安全四会各1；软件OSDI2、POPL1。AI中新增NeurIPS与ICML，既有CaMeL为SaTML补充来源，属于列举会议之外的直接相关正式安全论文；保留其真实会议，按AI主题占补充候选位，不纳入现行CCF-A计分。此项来源偏离明确记录，不把SaTML重标为ICLR或NeurIPS。

观察项两篇ISSTA仍缺可核验正文，继续W48；长程综述独立安全贡献不足，保持W50。行业再查14来源，已有五项初筛（Windows Rust、ARTEX、Cairn、NIST迁移、咨询机构AI治理）中本期已收录三项，另有跨期重复或无可核验方法正文，保持原三项，不追加重复。

- [x] 完整读取全部输入，核对用户改动。
- [x] DOI/arXiv/URL/标题四层去重。
- [x] 七篇正式身份由官方记录/DOI证明。
- [x] arXiv只供正文与版本核查，不独立证明接收。
- [x] 正文可用性、入选理由、损坏下载的替代均记录。
- [x] 暂缓与缺正文项保持下次目标及原因。
- [x] 七篇候选交第二阶段，尚未代写分析。
- [x] 三组会议全扫描、近四期和本期配额及SaTML偏离记录。
- [x] 检索阶段无摘要补全正文。


## 十篇目标补齐：第二阶段完成检查（2026-11-16）

七篇新增正文均完整取得，逐篇阅读引言、方法、案例、实验与局限；Image Hijacks 使用完整13页作者版，未以损坏文件推断。既有三篇事实保持；七份八项中间推理和两段草稿在十四字段之前保存，Easycatch 与精读来自同次原文阅读。

- [x] 十篇均有正文依据；新增七篇逐篇记录，缺正文的两个 ISSTA 候选继续等待。
- [x] 十篇十四字段顺序完整，每篇1—5个名词解释。
- [x] Easycatch 唯一源已保存；来源摘要仅作字段一致性校验。
- [x] 核心机制、输入—过程—输出案例与实验条件已说明。
- [x] 原始发表时间保留，未把补齐日期写成论文时间。
- [x] 主领域唯一、标签受控、override 先于索引写入。
- [x] 作者单位按所读论文；未核验中文名保留拉丁署名，机构所在地不明确时不猜测。
- [x] DOI、arXiv、URL、规范化标题去重；没有把历史版本建立成新记录。
- [x] 三条行业内容保留原证据、限制及商业利益字段，无摘要代替正文的新项。
- [x] SaTML 软配额例外透明记录，不扩大正式会议组及计分。

阅读边界：Jailbroken 的机制为闭源输出支持的假说；Image Hijacks 的未见模型迁移为0%，泄漏判定是输出格式而非实际邮件执行；AFLGo 存在慢于 AFL 的样本，Fuzzilli 覆盖受初始语料影响。全部相关数字在卡片中保留对象与分母。


## 十篇目标补齐：第三阶段事实维护

重新读取03及完整实体表、分类、索引、Easycatch、构建器、Pages配置、本期与涉及历史周报。8项预印/工作坊风险条目逐一刷新 arXiv 原始页面：AgentDataInjection、AdaptiveAdversaries、BadMemory、Self-State、IssueTrojanBench、RECEIPT、MemSecBench、Not an A11y；没有新主会接收依据。AdaptiveAdversaries 仍只是工作坊声明，Not an A11y 已有 AGENT-SEC 正式记录保留。本轮补齐未产生进一步历史状态升级，不重复建条目。FUZZILLI DOI 从所读正式PDF首页核实为10.14722/ndss.2023.24290，写入同一新索引条目。

新增9个署名单位、30个学者键，复用 Michael Schwarz、Yuval Yarom、Abhik Roychoudhury、Thorsten Holz、William Enck、Patrick McDaniel 等稳定身份。Andrew C. Myers 的论文单位保留1999年 MIT，不把当前 Cornell 主页单位写回历史署名；Marcel Böhme 同理保留 AFLGo 时期 NUS。可靠主页分别来自 https://www.cs.cornell.edu/andru/ 与 https://mboehme.github.io/ 。

待核验：Google Project Zero、G DATA Advanced Analytics、Cyberus Technology、Rambus Cryptography Research Division、Intel Labs 的论文时期实际所在地不足，country_code 留空；不以跨国企业总部代填。Project Zero 的 Google 归属有官方 https://projectzero.google/about-pz.html?m=1 支持，但现有归并要求国家一致，Google 现记录美国而该论文研究团队地点未核实，暂不强行合并地图节点，保留署名及待核验项。独立研究者 Paul Kocher 不猜所在地。新学者其余可靠主页尚未确认者保留原拉丁署名及论文来源，不生成猜测主页。既有 iLand、CaMeL 中文名和版本逐页差异待核验清单继续保留。


### 补齐后的构建与本地核验

初次 --check 仅 README 分布计数陈旧，调用构建器同步后复查通过。正式构建178篇/178缓存、6主领域、73行业观点、232单位、852学者、418合作边，178篇均有署名关系；154篇按现有范围计入已核验下界，recent_papers 上限3。21项 Python 与5项 JavaScript 测试通过（流量测试中的模拟网络失败属于测试输入）。

本地真实 Chrome 已检查W47十篇、日期、主卡隐藏/详情显示名词解释、Easycatch、三类入口、作者/排行/最近论文跳转、返回、循环截断、单弹层，无JS错误。PDF关键页已渲染复核。发现1999年论文被只匹配20xx的解析规则错误归到入库年，修复三处年份识别兼容19xx并加入端到端回归测试；OSDI与POPL新增元数据统一使用库内规范名称，源码修复仅暂存本次三处，原七个用户改动的patch正文逐字一致（构建器blob ID随新修复变化）。修复后JFlow关系图年份为1999。

- [x] 应查历史风险条目已刷新，保留原ID，无重复升级。
- [x] 完整实体表读取、30个新学者与9个新署名单位有来源，缺证项明确保留。
- [x] 所有178篇作者能映射，未核验中文名、地区及主页不猜测。
- [x] 页面日期、名词解释、入口与单弹层导航通过。
- [x] Easycatch无缺失或过期摘要，维护阶段未事后补生成。
- [x] --check、正式构建、计数/关系图/recent_papers核验通过。
- [x] 本地交互通过，历史年份修复增加回归覆盖。
- [x] 原用户修改完整保留；提交仅收本轮数据与新增年份修复。
- [ ] 推送、Pages及线上核验将在实际完成后记入自动化 memory 和最终报告。
