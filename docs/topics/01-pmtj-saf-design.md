# 01｜PMTJ-SAF整体结构设计与优化

阅读范围：公开研究。以下不涉及用户样品。推荐顺序：[Wang et al. (2018)](../library/records/SRC-000002.md) → [Devolder et al. (2016)](../library/records/SRC-000011.md) → [Chatterjee et al. (2018)](../library/records/SRC-000001.md) → [Chatterjee et al. (2021)](../library/records/SRC-000004.md) → [Cuchet et al. (2016)](../library/records/SRC-000003.md)。


## 1. 首先区分三种结构任务

隧穿界面、参考层内部的FM桥接、SAF块间AF耦合是不同任务。[Wang et al. (2018)](../library/records/SRC-000002.md)在同一器件内同时使用参考侧W0.25nm bridge和自由侧W0.2nm spacer；作者用Fig.1c minor loop支持后者两个CoFeB自由层同步翻转，不能将该证据自动归给前者。完整层序和器件/blank-film条件见[Wang et al. (2018)](../library/records/SRC-000002.md) pp.2–3、Fig.1及SI Note2。

[Devolder et al. (2016)](../library/records/SRC-000011.md)将固定系统分为PL、RL、HL，分别通过Ta与Ru连接（[Devolder et al. (2016)](../library/records/SRC-000011.md) p.1、Table I）。这是理解“参考层”一词歧义的入口：一个MgO邻接自旋极化层，与整套固定系统，不应总被同一RL标签替代。该论文结合FMR和模型约束各部分，而非只凭总回线台阶归属。


!!! note "原文图｜Wang et al. (2018)，Fig. 1"

    [![Wang et al. (2018) Fig. 1：a标出W bridge、自由层W spacer、MgO和Co/Pt-Ru参考系统；c为410°C退火薄膜的面外/面内VSM与minor loop，b为器件SEM，d为各向异性场随自由层厚度变化。](https://media.springernature.com/lw685/springer-static/image/art%3A10.1038%2Fs41467-018-03140-z/MediaObjects/41467_2018_3140_Fig1_HTML.jpg){ loading=lazy }](https://www.nature.com/articles/s41467-018-03140-z/figures/1)

    **出处：** [Wang et al. (2018)](../library/records/SRC-000002.md)，*Current-induced magnetization switching in atom-thick tungsten engineered perpendicular magnetic tunnel junctions with large tunnel magnetoresistance*，Fig. 1，PDF p.2。[原图与图注](https://www.nature.com/articles/s41467-018-03140-z/figures/1) · [出版PDF定位](https://www.nature.com/articles/s41467-018-03140-z.pdf#page=2) · [DOI](https://doi.org/10.1038/s41467-018-03140-z)。

    **原文图注要点／直接证据：** a标出W bridge、自由层W spacer、MgO和Co/Pt-Ru参考系统；c为410°C退火薄膜的面外/面内VSM与minor loop，b为器件SEM，d为各向异性场随自由层厚度变化。

    **作者解释：** 作者据自由层minor loop讨论CoFeB/W/CoFeB同步翻转。结构图中参考侧W桥的存在与自由层同步性的证据应分别读取。

    **本库分析与限制：** 本库将其用于区分器件层序及证据归属，不把自由层minor loop当成参考侧W桥的独立交换常数测量；正文与SI的stack A/B差异仍保留。

    **版权与改动：** Wang et al. (2018)，原文Fig. 1；[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)，依据[官方许可登记](https://www.nature.com/articles/s41467-018-03140-z#rightslink)。图内内容保持原样，中文仅为旁列概述。

## 2. 不同设计路线解决不同问题

| 路线 | 实际结构与证据 | 作者支持的内容 | 可比性边界 |
|---|---|---|---|
| 两组Co/Pt的常规SAF | [Wang et al. (2018)](../library/records/SRC-000002.md) Fig.1；Co/Pt/Ru/Co/Pt/W/CoFeB | 完整器件磁性、R-H与STT结果可关联 | 自由层W与参考侧W分开；不能把TMR峰当桥接J峰 |
| Ru/W薄SAF | [Chatterjee et al. (2018)](../library/records/SRC-000001.md) Fig.1(a–f)、Figs.2–3 | 多功能Ru/W连接Co/Pt与FeCoB；计算与器件测量比较杂散场 | 这里W参与AF耦合层，少了一组Co/Pt；非简单替换常规W桥 |
| seedless顶部参考层 | [Chatterjee et al. (2021)](../library/records/SRC-000004.md) 作者稿Figs.2–5；SI S1–S4 | Co/Ta/Pt插层改善该顶生长结构的磁性与热处理表现 | 不等同于在厚Pt种子上生长的Co/Pt |
| FeCoB型SAF参考 | [Cuchet et al. (2016)](../library/records/SRC-000003.md) Figs.1–7 | 从SAF存储层到参考层、再到去Pt/Pd设计的实验路线 | 间隔层相邻材料改变；不能继承Co/Pt的最佳Ru厚度 |

这些路线共享“稳定参考态并控制自由层受扰”的目标，但磁矩补偿、PMA、交换、器件杂散场和可制造性不是同一优化指标。本库综合判断：应先按结构任务建立可比组，再讨论厚度数值优劣；此为跨文献组织方法，不是新的实验结论。

## 3. 薄膜磁补偿与器件场补偿要分开

[Chatterjee et al. (2018)](../library/records/SRC-000001.md) Fig.1(d–f)为宏自旋杂散场计算，Fig.7为器件尺寸相关测量；计算结果与实测的角色分别记录。[Cuchet et al. (2016)](../library/records/SRC-000003.md) p.6又明确提醒：SAF2的磁矩补偿，与硬参考层为小尺寸器件减杂散场而采用的轻微不补偿，不应混同。因此不能从blank-film零平台直接宣布器件自由层偏置最小，也不能以层厚总和相等代替有效磁矩相等。

## 4. 热处理与可辨识性

[Devolder et al. (2016)](../library/records/SRC-000011.md) Fig.1的回线变化较小，FMR模却显示参数显著演化；[Wang et al. (2018)](../library/records/SRC-000002.md) Fig.5和SI Note8提供结构/元素分布层面的证据。两者分别支持“需要多种表征”和“特定W结构的材料稳定性”，不能仅凭W与Ta材料名称就推得跨工艺优劣。[Chatterjee et al. (2021)](../library/records/SRC-000004.md)还区分顶参考层与自由层的热稳定性（[Chatterjee et al. (2021)](../library/records/SRC-000004.md) Fig.5），整膜仍有台阶不表示每一部分都优化完毕。

## 5. 下一步阅读问题

优先补齐不同路线对参考层扰动、图形化后杂散场和耐退火性的共同评价口径。[Wang et al. (2018)](../library/records/SRC-000002.md) 正文与SI Note2存在stack A/B命名及器件选择描述差异，需核对图像与作者版本，不自行合并。会议/讲座只作线索，不用其摘要替代器件证据。

相关专题：[W桥与spacer](02-w-ferromagnetic-coupling.md) · [Ru耦合](03-ru-antiferromagnetic-coupling.md) · [磁矩与翻转](05-moment-and-reversal.md)。

[专题入口](../index.md) · [缺失材料](../gaps/missing-materials.md) · [未解决证据](../gaps/unresolved-evidence.md)

## 6. 本批补读：先分清稳定的是哪一部分

[Chatterjee et al. (2017)](../library/records/SRC-000028.md)将W/Ta半结、完整pMTJ薄膜和80nm器件分开：半结W5/Ta1的570°C、30min不能当成完整结的耐退火上限。其Fig.6/7及印刷202401-4（HAL PDF p.6）还明确CIPT与器件采用不同底电极，不能把两条TMR温变曲线仅归为尺寸效应。

[Kim et al. (2023)](../library/records/SRC-000031.md)虽提供封盖、TMR、磁性和STEM/EDS的联合对照，却是面内IrMn交换偏置MTJ；不能与Co/Pt-Ru垂直SAF作同一组PMA比较。[Yang et al. (2026)](../library/records/SRC-000032.md)的PCB四MTJ演示、单器件写入和Table1布局模拟也分别记录，避免从部分结构或电路模型跳到完整芯片已验证的结论。

本库分析：设计优化应说明评价对象是单磁层、SAF参考系统、完整结还是并行架构。该分组是阅读方法，不是新增实验结果。


[完整参考文献](../references.md) · [原图来源与核验事项](../gaps/figure-and-citation-gaps.md)


## W记录层与厚度模型的原文证据补充

[Kim et al. (2015)](../library/records/SRC-000034.md)的Fig.5（PDF p.6）用薄膜Keff和有效厚度外推纳米圆柱Δ，并非20nm器件保持时间实测；本库将这类计算与[Wang et al. (2018)](../library/records/SRC-000002.md)的真实器件写入分列。先确认薄膜PMA、再计算能垒、最后验证完整MTJ是不同证据环节，不能由其中一项宣布所有环节已完成。

[He et al. (2018)](../library/records/SRC-000038.md)的W/CoFeB/W/CoFeB/MgO没有Co/Pt参考桥或Ru间隔；其声/光模及MOKE对照增加了邻近双CoFeB系统的判读手段，不能直接赋予PMTJ-SAF参考系统相同层间交换常数。与[Chatterjee et al. (2017)](../library/records/SRC-000028.md)的封盖半结相比，先核W所在界面和完整器件条件，再讨论耐退火。

## 结构实例与证据对象的横向比较

| 文献 | 参考系统与MgO顺序 | Ru/W与退火 | TMR、RA和磁性证据 | 不足 |
|---|---|---|---|---|
| [Wang et al. (2018)](../library/records/SRC-000002.md) | Co/Pt-Ru-Co/Pt/W/CoFeB/MgO/双CoFeB自由层；bottom-pinned | Ru0.8、参考W0.25、自由W0.2nm；350–430°C/1h | 完整堆VSM、器件输运与STT；图/Note分别定位 | A/B对应仍冲突，不能将SI179%作为已确认的图形化器件数值 |
| [Chatterjee et al. (2021)](../library/records/SRC-000004.md) | 自由FeCoB/MgO/参考FeCoB/W/Co-Ta-Pt/Ru/Co-Pt；真正top-pSAF | Ru0.9、W0.30–0.50nm；SI S2为400°C | 完整顶参考层M–H厚度系列，W失同步有直接相关证据 | 含Ta插层；MgO厚度和本表TMR/RA未核，不填 |
| [Lee et al. (2016)](../library/records/SRC-000041.md) | Co/Pt-Ru-Co/Pt/W/CoFeB/MgO/Fe-CoFeB自由层；标题top是free | Ru0.85、W桥0.24、W cap4nm；400°C，时长/外场未明确 | 完整堆VSM+HRTEM+SIMS，CIPT TMR约143%；不是图形化保持实测 | 同时改桥和封盖；未独立测J(tW)，Co/Pt单层厚度和RA未核 |

各行的完整已知层序、缺失厚度和图文终止层问题保留在原始文献卡；结构化目录增加这些实例的字段，未知值保持null。不能因标题中都有top便当成同一生长顺序。当前新检索的[Liu et al. (2018) top-pinned SFM](https://doi.org/10.1103/PhysRevApplied.10.054054)尚未取得可读原文，不将其SFM概念自动改名成Co/Pt-Ru top-SAF，也不填图号或完整层厚。

本库推论：评估参考系统，至少分别问“参考层是否被固定”“自由层偏置是否受控”“输运是否保持”和“图形化后是否仍稳定”。完整堆的测量较孤立层更接近器件，却仍不能代替所有界面的独立参数测量。


!!! note "本阶段论文原图候选｜Lee et al. (2016)，Fig. 1"

    [![Lee et al. (2016) Fig. 1：完整堆结构及封盖厚度—TMR](https://media.springernature.com/lw685/springer-static/image/art%3A10.1038%2Fam.2016.162/MediaObjects/41427_2016_Article_BFam2016162_Fig1_HTML.jpg){ loading=lazy }](https://www.nature.com/articles/am2016162/figures/1)

    **出处与图意：** [Lee et al. (2016)](../library/records/SRC-000041.md)，*Perpendicular magnetic tunnel junction (p-MTJ) spin-valves designed with a top Co2Fe6B2 free layer and a nanoscale-thick tungsten bridging and capping layer*，Fig. 1，PDF p.2。[官方原图/图注](https://www.nature.com/articles/am2016162/figures/1)。完整堆结构及封盖厚度—TMR。

    **证据边界：** top free不是top reference；TMR曲线横轴是cap。作者解释与本库比较见文献卡；原图面板、实测点和模型线分别理解。

    **许可：** Lee et al. (2016)，CC BY 4.0，见[原文许可](https://www.nature.com/articles/am2016162#rightslink)。原图保持完整，不裁剪或翻译图内文字；非商业/不得改编条件按该来源保留。此为待批候选，未代填所有者批准。
