# 2026-W45 来源覆盖与核验记录

> 2026-11-16 补齐修订：原先每期三篇的编辑范围理由已撤回；本次在既有三篇上补七篇，按约十篇目标重新执行三阶段。下方原记录保留作审计历史，当前进度与结论以文末“十篇补齐”记录为准。

原窗口为 2026-10-27—11-02；实际补刊与外部回查日期为 2026-11-16。以下记录不表示这些论文在该窗口首次发表。执行计划依次为检索、正文精读与同步 Easycatch、维护验证与发布；本期线上核验通过后才处理 W46。

## 用户改动保护

运行前已有七个修改文件：`docs/automation/02-reading.md`、`docs/automation/03-maintenance.md`、`docs/automation/README.md`、`docs/data-architecture.md`、`docs/paper-reading-guide.md`、`scripts/build_site.py`、`skills/secpaper-easycatch/SKILL.md`。原补丁保存在 `/private/tmp/secpaper-user-changes-20261116.patch`；这些文件不进入本次内容提交。已安全快进至 `d28628b`。远端为 `wyinleo/SecPaper`。

## 配额与选题

W41—W44 各为安全 / 软件与系统 / AI 的 4/3/3，合计 16/12/12，占 40%/30%/30%。本期采用三篇专题精读，分别为 NDSS 的 SAGA、OSDI 的 UCSan 和 NeurIPS 的 AgentDojo，实际为 1/1/1，各 33.3%。相对 4/3/3 软目标缺 3/2/2 篇。

偏离原因是补刊分期组织问题链：本期连接通信权限、组件执行与注入评测；Anota、Osprey、AgentHarm 留给下一期，SymCC、iLand、CaMeL 留作后续核验候选。三组均有候选，并非声称其余会议没有合格论文。IJON 与后续 SymCC 的历史执行分析主题接近，暂缓精读。没有为达到十篇把摘要候选写成正文分析。历史基线保留真实年份；历史状态更新独立计数。

## 会议扫描

扫描从软件与系统组起，随后 AI、安全，最后 arXiv；组内起点分别为 OSDI、ICLR、NDSS。候选数指进入本轮明确候选清单的数量，不是整个会议相关论文总量。官方目录进行题目筛选，已有标题与全部索引按 DOI、arXiv ID、规范 URL、规范标题去重。

| 会议 | 官方入口与论文级检查 | 候选 / 入选 | 去向或排除原因 |
| --- | --- | --- | --- |
| OSDI | [技术程序](https://www.usenix.org/conference/osdi26/technical-sessions)，UCSan、Osprey、iLand | 3 / 1 | 后两篇跨期精读 |
| PLDI | [Analyzing Bytes](https://pldi26.sigplan.org/details/pldi-2026-papers/49/Analyzing-Bytes-Pre-Disassembly-Static-Binary-Analysis) | 0 / 0 | 已收录 W43；最初猜测的 track 路径 404，改用论文入口 |
| POPL | [研究论文](https://conf.researchr.org/track/POPL-2026/POPL-2026-popl-research-papers)，Security Reasoning | 0 / 0 | W43 重复 |
| FSE | [研究论文](https://conf.researchr.org/track/fse-2026/fse-2026-research-papers)，PoCGen、Secure Logging | 0 / 0 | W42 重复 |
| SOSP | [2026 接收页](https://sigops.org/s/conferences/sosp/2026/accepted.html)，另查 [2025 接收页](https://sigops.org/s/conferences/sosp/2025/accepted.html) 的 eBPF oracle、Proof-Guided Abstraction | 0 / 0 | 接收页可达；本期未推进其正文，不将主页访问当作精读 |
| OOPSLA | [SPLASH 正确入口](https://2026.splashcon.org/track/oopsla-2026)，SEVDF、Spectre、constant-time、dynamic release | 0 / 0 | SEVDF 已收录；其他主题留作候选方向 |
| ASE | [研究论文](https://conf.researchr.org/track/ase-2026/ase-2026-research-track)，npm detectors、LLM-native IDEs、AgentChaos | 0 / 0 | npm 为重复；其余未推进正文 |
| ICSE | [研究程序](https://conf.researchr.org/program/icse-2026/program-icse-2026/Detailed-Table)，TaintP2X、CoBrA | 0 / 0 | TaintP2X 重复；CoBrA 未推进正文 |
| ISSTA | [研究论文](https://conf.researchr.org/track/issta-2026/issta-2026-research-papers)，两篇观察项 | 2 / 0 | 正文缺口见下文 |
| FM | [正确研究入口](https://conf.researchr.org/track/fm-2026/fm-2026-research-paper)，Array-Carrying Symbolic Execution | 0 / 0 | 原猜测路径 404，已修正；未推进全文 |
| ICLR | [正式 AgentHarm 论文集](https://proceedings.iclr.cc/paper_files/paper/2025/hash/c493d23af93118975cdbc32cbe7323f5-Abstract-Conference.html)；2026 列表的 harmful prompt sanitization | 1 / 0 | AgentHarm 留待后续精读 |
| AAAI | [MCPTox](https://ojs.aaai.org/index.php/AAAI/article/view/40895) | 0 / 0 | 归档页有机器人拦截，以官方文章补查；重复项。发现正式日期应为 2026-03-14，交维护阶段修正 |
| NeurIPS | [AgentDojo 正式页](https://proceedings.neurips.cc/paper_files/paper/2024/hash/97091a5177d8dc64b1da8bf3e1f6fb54-Abstract-Datasets_and_Benchmarks_Track.html)，2025 论文集 | 1 / 1 | 补齐已有注入基准所依赖的历史基线 |
| ACL | [Fingerprinting LLMs](https://aclanthology.org/2026.acl-long.541/)；完整目录下载超时后查具体官方条目 | 0 / 0 | 本期聚焦可执行工具环境，未推进模型指纹正文 |
| CVPR | [V-Attack](https://openaccess.thecvf.com/content/CVPR2026/html/Nie_V-Attack_Targeting_Disentangled_Value_Features_for_Controllable_Adversarial_Attacks_on_CVPR_2026_paper.html)、HAM3 | 0 / 0 | 可见正文入口，未推进视觉攻击精读 |
| ICCV | [JailbreakDiffBench](https://openaccess.thecvf.com/content/ICCV2025/html/Jin_JailbreakDiffBench_A_Comprehensive_Benchmark_for_Jailbreaking_Diffusion_Models_ICCV_2025_paper.html)、Shuffle Inconsistency | 0 / 0 | 同上；不据此声称无更新 |
| ICML | [PrivAct](https://proceedings.mlr.press/v306/cheng26o.html) 与 PMLR 目录 | 0 / 0 | PrivAct 已在 W43 收录 |
| NDSS | [2026 接收列表](https://www.ndss-symposium.org/ndss2026/accepted-papers/)，SAGA、Anota | 2 / 1 | SAGA 官方正文和 DOI 齐备；Anota 后续精读 |
| IEEE S&P | [2026 接收页](https://sp2026.ieee-security.org/accepted-papers.html)，IJON DOI / 作者正文 | 1 / 0 | 历史 IJON 暂缓，未重复加入已收录的 2026 论文 |
| CCS | [2026 接收列表](https://www.sigsac.org/ccs/CCS2026/program/accepted-papers.html)，既有 2025 条目对照 | 0 / 0 | 不把会后日期写为 W45 已正式发表；未推进新增全文 |
| USENIX Security | [技术程序](https://www.usenix.org/conference/usenixsecurity26/technical-sessions)，SymCC 2020 官方页 | 1 / 0 | 现有 2026 标题去重；SymCC 留后续基线 |
| arXiv / SaTML 补充 | [CaMeL](https://arxiv.org/abs/2503.18813) 与 DOI 10.1109/SaTML68715.2026.00040 | 1 / 0 | 后续核验；SaTML 不加入现行三类计分范围 |

SAGA、UCSan、AgentDojo 均有官方会议身份和 PDF；与 148 条原索引四级去重无重复。正文候选的详细入口见对应官方页；本阶段不提前落库分析。

## 固定行业池 14 来源

所有入口均已尝试；访问异常只说明证据缺口，不代表该周无更新。

| 来源 | 扫描与筛选结果 |
| --- | --- |
| Project Zero | 旧 Blogspot 超时；[新官方站](https://projectzero.google/) 检索到紧急补丁文章，已在 W44 收录 |
| GTIG / Mandiant | 入口曾可读，本轮 curl 超时；既有 BeyondTrust 与季度 AI 报告去重，未选新增 |
| Microsoft | 入口超时或 403，改查官方 10 月文章；未形成窗口内新增候选 |
| Unit 42 | 入口和 [10-29 PHP2Shell 正文](https://unit42.paloaltonetworks.com/cve-2026-109618-cve-2026-109619/) 可读，入选 |
| Talos | 入口 403；官方文章检索返回既有 10 月报告，未选新增 |
| 玄武 | 入口可读，浏览器安全文章与研究目录；未推进窗口内新增 |
| 科恩 | 入口可读，BinAbsInspector 与既有移动漏洞归档；未推进窗口内新增 |
| Anthropic | 研究入口可读，自评式检测已收录；未选新增 |
| OpenAI | 入口 403；已收录训练遏制和 PHP 协调披露，未重复 |
| NIST | 入口及 [10-27 PQC 新闻](https://www.nist.gov/news-events/news/2026/10/nist-report-provides-guidelines-transition-post-quantum-cryptography) 与 IR 8547 final 可读，入选 |
| CISA | 通告入口可读，导航和通用指南不直接作为原创研究入库 |
| Gartner | 403，未取得足够正文与方法证据，不收录付费预测 |
| Forrester | 原入口错误或不完整，改查 [数据安全归档](https://www.forrester.com/blogs/category/data-security/) 与 [安全管理归档](https://www.forrester.com/blogs/category/security-management/)；AI Agents Aren't Waiting、eMudhra、PHP2Shell、Endpoint 四篇进入初筛但排除：观点或二手事件综述，未取得新增独立方法和底层数据 |
| IDC | 入口可读，活动和市场推广未形成可复核研究候选 |

行业初筛至少五项：NIST、Unit 42、Forrester 的三篇相关观点；正文精读保留前两项。两项来源类型分别为公共标准和商业事件响应，保留商业利益与遥测局限。

## 待人工补充正文与身份

- 高优先级：[Ghosts in the Memory](https://conf.researchr.org/details/issta-2026/issta-2026-research-papers/107/Ghosts-in-the-Memory-Detecting-Unintended-Sensitive-Data-in-Android-Apps)。2026-11-16 回查官方页和精确标题公开搜索仍只取得摘要，需正文核对内核插桩、50 应用采样、RASP 与披露链。
- 高优先级：[How Safe is Your Screen](https://conf.researchr.org/details/issta-2026/issta-2026-research-papers/177/How-Safe-is-Your-Screen-Understanding-and-Detecting-Privacy-Leaks-in-Sensitive-Activ)。同日回查仍无可核验全文，需核对 UI 模型、样本构造、隐私泄露判定与披露。两者继续保留 watchlist，目标 W46；不把摘要数字写成精读结论。
- UCSan 中国作者、AgentDojo 的 Jie Zhang 暂用正式英文署名，未核实一一对应的官方中文姓名。

## 第一阶段检查

- [x] 已加载索引、观察清单、行业池与观点事实库，检查最新周报和本期工作记录。
- [x] 候选四级去重，无正式版重复新建。
- [x] 三篇接收身份由官方论文集或 DOI 支持。
- [x] 未把 arXiv 自述升级为会议接收。
- [x] 三篇正文 PDF 可用，行业两项有完整正文入口及入选理由。
- [x] 缺正文项目继续保留，更新实际核验日期、目标周与原因。
- [x] 第二阶段明确处理 SAGA、UCSan、AgentDojo 与两篇行业内容。
- [x] 三组、全部会议、近四期分布、软配额偏离与固定行业池均已记录。
- [x] 未把候选摘要加工成未经阅读的正文分析。

## 第二阶段检查与证据定位

- [x] 三篇完整正文的引言、方法、实验、局限和补充材料已核对；核心结果页分别为 SAGA PDF 第 12 页、UCSan 第 13 页、AgentDojo 第 20 页，并渲染检查表格。
- [x] 三篇 14 字段完整且顺序一致；各有两个名词解释。
- [x] Easycatch 在阅读原文时先形成中间推理和两段草稿，再写精读与一致性摘要；三条 skill_version 为 4。
- [x] 方法解释输入、关键处理与结果；实验带对象、预算和分母；未把模拟数据写成真实用户数据。
- [x] 正式身份、版本时间和原文链接可核验；没有预印本升级推断。
- [x] 完整受控词表已检查，三条 override 指向唯一主领域，未新增无定义标签。
- [x] 单位和作者采用论文署名，中文姓名歧义保留英文。
- [x] 索引四级去重通过，观察项保留；两个行业条目包含所有证据、限制与利益字段。
- [x] 两个行业条目只根据可访问正文分析，IR 8547 的实施细节没有被冒充为完整条款审计。
- [x] AgentDojo 数字差异明确保存：正文工具数 74、表 1 和数据卡写 70（表内求和为 74）；主文工具过滤约 7.5%，附录表 5 为 6.84%；主文部分旧版效用描述与附录新版模型表不一致。精读采用指定表格，不混用不同配置或自行修订原文。

## 历史回查与维护

2026-11-16 逐项复核 ADI（2607.05120）、Bad Memory（2607.14611）、Self-State（2607.17986）、IssueTrojanBench（2607.20759）、RECEIPT（2607.18575）、MemSecBench（2607.27080）、Not an A11y（2608.08939）、Adaptive Adversaries（2607.18063），并检查仅依赖 arXiv/项目链接的 WASP。Self-State v2 与 Adaptive Adversaries v2 已在原卡片体现；未见其他应在 W45 截止线内升级的可靠正式记录。IssueTrojanBench 的 arXiv 入口在工具中不可达，精确标题检索未获得对应官方 ASE 记录，保持预印；未把这次访问失败写成没有更新的证明。

Not an A11y 的 arXiv 新增 AGENT-SEC 2026 参考文献和 DOI；Crossref 原始登记返回标题一致、published-online 为 **2026-11-14**（DOI 10.1145/3847320.3847397），超出 W45、W46 窗口，留至 W47 处理。DOI 页面当前工具不可达，还需取得正式全文核对作者和实验。此处只记录实际发现时间，不提前更改 W45 的历史身份。

MCPTox 官方 AAAI 文章页显示 Published 2026-03-14；已修正 W44 原卡片并给原索引增加官方链接。没有改动五个 Easycatch 事实字段，其摘要保持有效。

实体表增加 Invariant Labs（瑞士政府 UID 登记支持所在地），复用 Northeastern、UCR、ETH 的既有 ID；新增 11 位缺失学者，保持正式英文署名，Chengyu Song 的主页由 UCR 官方个人站支持。未获得其他作者可靠中文姓名或主页时不猜测。生成关系图覆盖 151/151 篇、740 位学者、211 个单位、311 条合作边，135 篇计入现行顶会已核验下界；OSDI 沿用现行不计分口径。每位学者最近论文不超过三条，全部学者有稳定 ID。

首次 `--check` 只因 README 自动统计过期失败；已由构建器同步该生成区块，再次 `--check` 和正式构建通过：151 篇、151 缓存、6 主领域、67 行业观点。20 项 Python 测试、5 项 JavaScript 测试通过；测试中的模拟网络错误属于重试单测输出。内置浏览器两次连接超时，已切换到使用独立临时配置的本地无头 Chrome 进行实际交互检查。

无头 Chrome 实际交互通过：W45 三条主卡公开日期、主卡不显示名词解释、详情显示名词解释与 Easycatch、论文作者到学者、排行姓名到学者、最近论文回到同一论文、返回恢复、循环截断与单一弹层、三类顶部入口；页面没有 JavaScript 错误。截图留在本次临时 QA 目录，不作为站点素材发布。七个用户修改文件的二进制 diff 与运行前逐字一致。

第三阶段发布前检查：历史逐项回查、实体登记、稳定学者 ID、日期与名词解释边界、Easycatch 来源摘要、构建与检查、计数与关系覆盖、实际交互、用户改动保护九项均通过。发布 SHA、推送结果、Pages 工作流和线上核验在本次自动化最终报告及 memory 中记录，以实际结果为准。

首次推送被远端 `c232be0` 拒绝；核对该提交只改流量历史和流量图后，安全 rebase 并恢复用户改动，二进制补丁仍一致。随后按最新流量历史重建并再次通过检查，不覆盖远端统计。

## 十篇补齐：第一阶段重新执行

本轮开始保留七处用户改动，完整二进制补丁快照为临时工作文件；未修改或暂存这些文件。执行计划为 W45、W46、W47，每期严格依次完成检索、原文精读与 Easycatch、维护验证及发布；当前只开始 W45，后两期尚未进入正式阶段。

重新读取 01-discovery、157 条索引、3 条观察清单、14 行业来源、73 条行业记录、当前最新 W47 周报与本期原 inquiry。按原期次统计 W41—W44，安全 16（40%）、软件与系统 12（30%）、AI 12（30%）；会议为 CCS 4、NDSS 6、USENIX Security 4、S&P 2，ISSTA 2、ASE 2、FSE 3、PLDI/POPL/OSDI/OOPSLA/ICSE 各 1，ACL/ICML/CVPR/AAAI 各 2、NeurIPS 3、ICCV 1。优先补 CCS/S&P、软件与 AI 细分来源。

本轮从 CCS 开始安全组、ISSTA 开始软件组、ICLR 开始 AI 组，扫描全部 21 个会议与 arXiv；行业 14 个入口全部尝试。当前目标为已有 SAGA/UCSan/AgentDojo 加七篇，下表完成后合计安全 4、软件系统 3、AI 3；安全组四个会议各一篇，无调剂缺额。七篇均为明确标识的历史基线，保留文献原时间，不称近期首次发表。

| 本轮推进项 | 来源、正文与选择原因 | 候选/新增目标 |
| --- | --- | --- |
| IJON | IEEE S&P 2020，DOI 10.1109/SP40000.2020.00117，CISPA 正式研究记录与作者完整 16 页 PDF；补人工引导模糊测试 | 1/1 |
| Path ORAM | CCS 2013，DOI 10.1145/2508859.2516660；ACM 正式集与完整 12 页论文，补访问模式隐私 | 1/1 |
| QSYM | USENIX Security 2018 官方页与 18 页正式 PDF，补混合符号执行执行组件 | 1/1 |
| FlowDroid | PLDI 2014，DOI 10.1145/2594291.2594299；大学研究库及作者 11 页论文，补生命周期感知污点分析 | 1/1 |
| DroidRA | ISSTA 2016，DOI 10.1145/2931037.2931044；University of Luxembourg 机构库及 12 页作者版，补反射静态分析；与 2016 ASE 工具演示、2021 TOSEM 扩展版区分 | 1/1 |
| AutoDAN | ICLR 2024 正式论文集及 21 页 PDF，精确题目 Generating Stealthy Jailbreak Prompts；与同名 Automatic and Interpretable 论文分开 | 1/1 |
| HarmBench | ICML 2024 PMLR 235 正式记录与 arXiv 作者完整 44 页正文；补统一红队评测及拒绝能力，PMLR PDF 被验证页阻断不等于无正文 | 1/1 |

其余会议继续扫描，不因达到七篇停止：NDSS/OSDI、FSE/POPL/OOPSLA/ICSE、AAAI/NeurIPS/ACL/CVPR/ICCV/ICML 目录或具体条目可达；SOSP/FM 可达但未推进其他正文；PLDI、ISSTA、ASE、FSE 大页面此次超时，以对应正式单篇与机构原文作替代；CCS 当前页静态标题提取为空，以 ACM 原论文集核验。未推进的项目仍为原记录的候选或重复项，不能将“未选”写成“没有论文”。

行业池仍为原表 14 源：Project Zero、GTIG 超时，Microsoft/Talos/OpenAI/Gartner 403，Forrester 超时；Unit 42、玄武、科恩、Anthropic、NIST、CISA、IDC 可达；Microsoft/Talos 官方 RSS 为替代入口。复查原记录的至少五项初筛候选（NIST 后量子、Unit 42 PHP2Shell，以及 Forrester 的 AI Agents、eMudhra、Endpoint 等文章）与当期日期、URL 去重；此次不为增加论文数而重复增加行业观点，W45 两项既有全文分析保留，2 条已符合行业 2—5 条范围。未出现能够新增且已经完成正文分析的行业记录。

四级去重对全部 157 条索引检查：七篇 DOI、arXiv ID、正式 URL、规范题目均无命中。两项 ISSTA 2026 未公开正文项目在本轮实际日期已查过、下一目标 W48，W45 补齐不倒改它们为到期或编写摘要事实；综述 W50 同理。

可靠入口：[IJON](https://cispa.de/en/research/publications/68621-ijon-exploring-deep-state-spaces-via-fuzzing)、[QSYM](https://www.usenix.org/conference/usenixsecurity18/presentation/yun)、[Path ORAM](https://doi.org/10.1145/2508859.2516660)、[FlowDroid](https://ris.uni-paderborn.de/record/5189)、[DroidRA](https://orbilu.uni.lu/handle/10993/27761)、[AutoDAN](https://proceedings.iclr.cc/paper_files/paper/2024/hash/f83cb637e159e789f5576ff6848874de-Abstract-Conference.html)、[HarmBench](https://proceedings.mlr.press/v235/mazeika24a.html)。

第一阶段完成检查：九项全部通过——事实输入重读、四级去重、正式身份、预印边界、七篇完整正文、观察清单原因与目标、候选明确、近四期/轮换/完整来源覆盖与配额、未据摘要写分析。进入第二阶段。


### 十篇补齐：第二阶段检查

新增精读：IJON、Path ORAM、QSYM、FlowDroid、DroidRA、AutoDAN、HarmBench。依次阅读对应全文的引言、方法、算法/案例、实验及局限，在临时阅读记录先完成八项推理和两段 Easycatch，随后写入周报与唯一源文件；未从卡片反推 Easycatch。

- [x] 七篇均有完整正文，分别使用会议、作者或机构保存的论文；DroidRA 作者稿页脚占位 DOI 不作为身份依据，正式身份以卢森堡大学记录及 DOI 为准。
- [x] 十篇均有顺序一致的十四字段，每篇 1—5 条名词解释。
- [x] 新增七篇 Easycatch 已与原文同步写入，修订号 1、skill version 4，一致性摘要在精读完成后计算。
- [x] 方法解释输入、步骤与输出，示例注明论文案例或整理者归纳。
- [x] 数字附样本与条件：Path ORAM 区分证明和外推，QSYM 不混用摘要/表格和跨机器倍数，FlowDroid 不把流报告视为恶意，AutoDAN 明示未加系统提示，HarmBench 明示尝试行为标准。
- [x] 仅使用正式会议接收状态，时间线保留真实发表时间。
- [x] 主领域显式映射；先登记四个受控标签，再写入论文索引。
- [x] 署名与单位据正文。刘晓耕中文由本人主页 https://xiaogeng-liu.com/ 明确对应；其他未核实中文保持英文。
- [x] DOI / arXiv / URL / 标题去重，七篇无重复。两篇缺正文观察项继续在 W48 队列。
- [x] 原有两条行业观点证据字段完整，本轮不增加没有独立正文证据的行业条目。

待核验姓名：Li Li、Ling Ren、Xiangyao Yu、Meng Xu、Nan Xu、Muhao Chen、Chaowei Xiao、Long Phan、Xuwang Yin、Zifan Wang、Norman Mu、Nathaniel Li、Bo Li 等暂保留论文拉丁署名。Li Li 的作者主页与 DroidRA 作品已对应，但搜索到的中文线索尚不足以据此统一中文姓名；不能凭拼音选择汉字。主页与论文发表时单位分开处理。

正文差异：QSYM 摘要 LAVA 总数与表 6 加总相差 1，CGC 平局文字与其他项加总不一致；精读不引用这些冲突合计。DroidRA 真实应用段落出现 100 / 91 样本量差异，故不引用统一耗时结论。HarmBench 当前可读完整文本是作者 arXiv v2，接收身份由 PMLR 正式页独立证明，未将后续在线榜单混入该版本。


### 十篇补齐：第三阶段验证

2026-11-16 再次全量加载实体、分类、索引、Easycatch、本期周报、inquiry、构建器与 Pages 工作流。八个预印/工作坊风险条目的 arXiv 正文入口、comments、journal reference 和 DOI 已逐项回查；除此前已经记录的 Not an A11y 工作坊出版外，未发现可确认的新身份升级，不重复建项。Adaptive Adversaries 仍是 workshop，不能计入主会。

- [x] 历史风险清单逐项回查，既有状态保留，无新增状态修正。
- [x] 实体表完整读取；新增 34 个稳定学者实体、4 个已核验大学。论文签名与单位按发表时正文，主页不替换历史单位。
- [x] 164/164 论文有单位作者覆盖；关系图 797 位学者、219 家归并单位、342 条合作记录，recent_papers 均不超过三条。
- [x] 十篇均含十四字段与有效 Easycatch；无缺失、过期摘要或事后由卡片生成。
- [x] 分类表 1.10.4、实体表 1.12.4，十篇单一主领域且来源配额 4/3/3。
- [x] 构建 --check 与正式构建通过；164 篇论文及精读、6 主领域、73 行业观点。
- [x] 20 项 Python、5 项 JavaScript 验证通过。
- [x] 本地 Chrome 验证论文作者、学者最近论文、排名、返回、单弹层循环、日期、详情名词解释与三入口；无页面 JS 错误。
- [x] 七个运行前用户修改文件的 binary diff 与快照逐字节一致，提交按文件白名单暂存。
- 发布门：仅在本地验证完成后提交推送；实际 SHA、Pages run 和线上十篇检查另由本次发布记录与自动化 memory 保存，成功核验后才进入 W46。
