# 06｜SAF宏自旋、微磁学及理论判据

主阅读：[Cuchet et al. (2016)](../library/records/SRC-000003.md) → [Devolder et al. (2016)](../library/records/SRC-000011.md) → [Muehlenhoff et al. (2021)](../library/records/SRC-000019.md) → [Böhm et al. (2019)](../library/records/SRC-000020.md) → [Böhm (2023)](../library/records/SRC-000008.md)。本阶段阅读公开模型，不执行或修改用户模型规格。

## 1. 用模型回答什么问题

| 模型层级 | 来源与锚点 | 能解释/约束的问题 | 明确限制 |
|---|---|---|---|
| 两有效磁块与净磁矩 | [Cuchet et al. (2016)](../library/records/SRC-000003.md) p.4 Eqs.(1)–(2)；[Chatterjee et al. (2018)](../library/records/SRC-000001.md) p.4未编号Hex2式 | AP净矩额外翻转、各向异性和补偿趋势 | Cuchet明示真实薄膜成核使开关场低于宏自旋近似 |
| 固定系统PL/RL/HL耦合宏自旋 | [Devolder et al. (2016)](../library/records/SRC-000011.md) p.3、Fig.2、Table I | 用模频率和静态事件联合约束PMA/耦合 | 只测到部分本征模；部分参数固定，拟合不能证明唯一 |
| 深度spin-chain | [Muehlenhoff et al. (2021)](../library/records/SRC-000019.md) 的2020年作者稿pp.4–6、Table I、Fig.7 | 倾斜、层间次序及GMR响应 | 自由层用tanh示意；不是完整器件微磁解 |
| 多FM块与逐Co层模型 | [Böhm et al. (2019)](../library/records/SRC-000020.md) p.5，Figs.2–3；[Böhm (2023)](../library/records/SRC-000008.md) §3.5 | SSF、inversion与垂直AF畴壁 | 模型精细程度、退磁几何和参数重优化影响定量 |

## 2. Hex2判据的正确读取

[Chatterjee et al. (2018)](../library/records/SRC-000001.md)将Hex2解释为AF耦合PL/HL净矩的有效矫顽场。在其近似中，分子为各向异性能之和，分母含面磁矩差；满足相对场尺度条件才出现concurrent reversal。原文的Hex与Hex2不是两个独立的Ru交换常数，也不能用全膜任意两峰间距代入。

[Cuchet et al. (2016)](../library/records/SRC-000003.md) Eq.(2)相似，但作者明确写出该宏自旋值是成核主导薄膜实验的上限。趋于补偿时公式发散不表示真实实验必须测得无限场，也不表示数值求解器可以忽略非均匀磁化。这里记录模型边界，不重新计算材料参数。


!!! note "原文图｜Chatterjee et al. (2018)，Fig. 3"

    [![Chatterjee et al. (2018) Fig. 3：a、b分别给340°C及400°C退火后的主回线下降支和minor loops；插图分别定位共同翻转场Hex2、自由层minor loop以及PL的耦合场Hex。](https://media.springernature.com/lw685/springer-static/image/art%3A10.1038%2Fs41598-018-29913-6/MediaObjects/41598_2018_29913_Fig3_HTML.png){ loading=lazy }](https://www.nature.com/articles/s41598-018-29913-6/figures/3)

    **出处：** [Chatterjee et al. (2018)](../library/records/SRC-000001.md)，*Novel multifunctional RKKY coupling layer for ultrathin perpendicular synthetic antiferromagnet*，Fig. 3，PDF p.4。[原图与图注](https://www.nature.com/articles/s41598-018-29913-6/figures/3) · [出版PDF定位](https://www.nature.com/articles/s41598-018-29913-6.pdf#page=4) · [DOI](https://doi.org/10.1038/s41598-018-29913-6)。

    **原文图注要点／直接证据：** a、b分别给340°C及400°C退火后的主回线下降支和minor loops；插图分别定位共同翻转场Hex2、自由层minor loop以及PL的耦合场Hex。

    **作者解释：** 原文同页给出没有编号的Hex2近似式，将其与AF耦合两块净磁矩和各向异性联系。

    **本库分析与限制：** 图本身是磁性测量，公式是模型近似；它不是微磁模拟结果。Hex与Hex2的不同位置不能解释成两个独立Ru交换常数，宏自旋近似也不能排除成核和磁畴。

    **版权与改动：** Chatterjee et al. (2018)，原文Fig. 3；[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)，依据[官方许可登记](https://www.nature.com/articles/s41598-018-29913-6#rightslink)。图内内容保持原样，中文仅为旁列概述。

## 3. 参数可辨识性和符号、单位

[Devolder et al. (2016)](../library/records/SRC-000011.md)从局域能量极小继续扫场并线性化LLG，结合高低场模频率与事件约束；“宏自旋拟合”的有效证据比仅拟合总回线更多，但仍以假定模型及Ms条件为前提。[Ogrodnik et al. (2021)](../library/records/SRC-000025.md)用静态与动态数据联合拟合，其SI Figs.S4–S5另列面内各向异性及易轴偏角，表明不能只保留一个Keff自由参数。

本库比较时分别记录原文的J符号、能量按面积/体积归一化、H与μ0H、t取哪块厚度。不直接把某篇的正AF-J代入另一篇正FM-J约定。对于MOKE，还要区分单位方向向量与面磁矩以及光学权重；层分辨模拟输出不是层分辨实验测量。

## 4. 为什么“用了微磁软件”仍可能是简化模型

[Böhm et al. (2019)](../library/records/SRC-000020.md)用MuMax3实现块平均模型I及更细模型II；前者复现定性特征，后者加入逐Co层及界面附近耦合差异后重新优化参数。[Böhm (2023)](../library/records/SRC-000008.md) §3.5 pp.51–54进一步讨论简化模型对真实层距和磁静力学的近似。[Muehlenhoff et al. (2021)](../library/records/SRC-000019.md)的magnum.fe计算也用特定窄几何spin-chain，不能仅按软件名把它称为任意横向磁畴过程的完整验证。

[Böhm et al. (2019)](../library/records/SRC-000020.md) Fig.3位于作者稿PDF p.15，其图注说明该能量比较将退磁能视为可忽略并置零。应把这条模型设定与SQUID-VSM实测回线分开，不能将能量分项当成独立实验测量。

强AF-IEC多块模型中的SSF，需要考虑块数、表面和能量层级；不能把其奇偶N规则套到仅两AF磁块的参考系统。相反，出现横向成核/畴壁证据时，两刚性块模型也应保留适用限制。

## 5. 后续理论资料与复现缺口

NIST的[Donahue and Porter (1999)](../library/records/SRC-000027.md)为OOMMF 1.0官方技术报告。印刷p.1/PDF p.9明确区分二维网格与三维自旋，并将完整三维求解列为当时开发内容；§9 pp.30–32列收敛和输出，§16.1 p.66规定MIF 1.1与SI单位。它补充方法记录依据，不能证明目标SAF实验，更不能代表现代OOMMF全部能力。跨软件比较应注明具体版本与离散化，此为本库整理建议。

需补齐公开脚本的具体版本、参数与离散化收敛记录，逐项比较模型I/II及原始实验；本阶段不运行新模拟。技术手册用于定义数值工具及文件格式，不能取代材料实验。模型是否能唯一分离PMA、交换、磁矩和光学权重仍为开放问题。

相关专题：[整体设计](01-pmtj-saf-design.md) · [Ru与J定义](03-ru-antiferromagnetic-coupling.md) · [实验读出](05-moment-and-reversal.md)。

[专题入口](../index.md) · [证据问题](../gaps/unresolved-evidence.md)


## 6. 本批补读：粗糙界面模型与Ru-RKKY判据分开

[Yang et al. (2026)](../library/records/SRC-000032.md)将MgO两侧粗糙界面的平行/反平行能量差定义为ΔE=E平行−E反平行，负为FM、正为AFM。SI S1用周期界面及局域易轴、对磁化起伏作二阶展开；S3 Eqs.(32)–(33)用SW近似提取Ku。这些约束不是任意横向磁畴过程的完整验证，也不把其中A直接当Ru面交换J。

Fig.2a为作者模型示意、b为计算、c–f涉及拟合与实验表征；必须按面板分辨证据。Fig.3e给1ns实验，SI S8/Fig.S13的100ps为模拟估计；Table1是布局/能耗比较，不能写成实测大阵列性能。Methods与Results的CoFeB厚度表述不同，暂保留各自定位，不用一套参数补齐另一组样品。

本库分析：该文补充温度、粗糙度相关耦合与SAF杂散场的联合判读；不能取代[Chatterjee et al. (2018)](../library/records/SRC-000001.md)的Ru/W体系或[Ma et al. (2025)](../library/records/SRC-000010.md)的Ru-RKKY光控机制。原文SI公式符号的复核保留为明确任务，不自动修正作者公式。

!!! note "原文图号定位（仅链接）｜Yang et al. (2026)，Fig. 2"

    [Yang et al. (2026)，Fig. 2（官方原图链接）](https://www.nature.com/articles/s44306-025-00119-7/figures/2)

    **出处与图注要点：** [Yang et al. (2026)](../library/records/SRC-000032.md)，*Parallel writing of magnetic tunnel junctions by electrical control of interlayer magnetic coupling*，Fig. 2，PDF p.3。a为作者周期粗糙界面示意，b为能量差计算，c为Ku温变提取，d为TEM，e–f为TMR回线与offset温变。 [官方图注](https://www.nature.com/articles/s44306-025-00119-7/figures/2) · [出版PDF](https://www.nature.com/articles/s44306-025-00119-7.pdf#page=3)。

    **作者解释：** 作者联合粗糙度模型、Ku变化及SAF杂散场解释耦合与写入；不同面板不是同一种实验。

    **本库分析与限制：** MgO界面粗糙度相关耦合不能改写为Ru-RKKY；偏置场不直接等于本征J，模型和拟合条件见原SI。

    **版权：** Yang et al. (2026)，原图内容未改；[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)，见[出版商许可](https://www.nature.com/articles/s44306-025-00119-7#rightslink)。图中作者示意面板也属于论文原图，不是本库原创。



[完整参考文献](../references.md) · [原图来源与核验事项](../gaps/figure-and-citation-gaps.md)
