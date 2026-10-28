# 04｜Co/Pt厚度、重复次数和PMA优化

阅读：[Chatterjee et al., 2021 · SRC-000004](../library/records/SRC-000004.md) → [Shepley et al., 2015 · SRC-000026](../library/records/SRC-000026.md) → [Ogrodnik et al., 2021 · SRC-000025](../library/records/SRC-000025.md)；重复次数结合[Chatterjee et al., 2018 · SRC-000001](../library/records/SRC-000001.md)、[Muehlenhoff et al., 2021 · SRC-000019](../library/records/SRC-000019.md)，界面磁矩参考[Darwin, 2023 · SRC-000009](../library/records/SRC-000009.md)。

## 1. Co厚度趋势为什么不能脱离结构

Shepley2015的玻璃/Ta/Pt/Co(t)/Pt在t=0.85、0.95、1.0nm范围内，Fig.1b inset的Keff随Co增厚下降；由EHE低场段提取Hk，再结合SQUID的Ms，见Eq.(3)。SI §II、Figs.S3及Eqs.S9–S11说明高场偏离相干旋转并成畴，因此不是将整条曲线简单拟合成单宏自旋。

ACS2021的[Co(t)/Ta0.2/Pt1.1]5 seedless体系却在所测范围显示Keff随Co增厚提高（作者稿Fig.3）。这不是可以直接宣布“哪个趋势正确”的比较：界面插层、厚度区间、生长顺序、热处理和体积归一化不同。该论文计算Keff时考虑Co、Pt及FeCoB总厚度，不能默认等同于仅按Co磁性体积归一化的数据。

## 2. Pt厚度的多重作用

| Pt所处位置 | 来源与锚点 | 作者支持的观察 | 不可直接推广的内容 |
|---|---|---|---|
| SL-ML重复内Pt | SRC-000004 SI Fig.S4，S4页 | 该Co/Ta/Pt系列有从面内到面外及Keff峰值变化 | 不能移植其1.1nm最优值给普通seeded Co/Pt |
| 种子Pt | SRC-000001 Figs.4–5 | 更厚种子伴随HL-PMA、粗糙度及PL翻转变化 | PMA提升与粗糙度代价同时存在，不能只留正向趋势 |
| Co层间Pt楔形spacer | SRC-000025 Figs.1、5–6 | 两层PMA、FM耦合及倾斜区间共同变化 | 不是重复内Pt厚度单独优化，也不是Ru耦合 |

ACS2021把界面混合、织构、退磁能和电子杂化作为解释讨论，不能把磁滞曲线直接改写为这些微观过程均已被独立测量。Ogrodnik2021则联合XRD、静态和FMR模型，仍需保留拟合参数身份。

## 3. 重复数至少有两种

Chatterjee2018 Fig.6改变一个HL的Co/Pt重复数，影响面磁矩与concurrent reversal。Muehlenhoff2020稿Fig.5改变三块SAF中间块Y=8/9，测得不同GMR翻转次序。Böhm体系中的N却是**AF耦合FM块的总数**，块内重复另用X；不能把其N奇偶效应写成单块Co/Pt双层数奇偶效应。

本库综合判断：重复数变化应同时列总磁性厚度、界面数、面磁矩、PMA和读出层位置；仅以“增加重复能提高PMA”概括会丢失这些控制变量。

## 4. 磁矩校准不是附属步骤

Darwin2023 §5.8、Figs.5.14–5.15采用Co/CoB厚度系列研究不同NM界面的moment/area，区分自有实验与前文综述。它提示有效磁厚度和邻近诱导磁矩值得核对，但不能将CoB/Ir/Pt参数直接代给Co/Pt/Ru。该论文与上述研究的比较属于材料边界检查，非用户样品参数估计。

## 5. 覆盖缺口

普通Co/Pt在统一工艺下同时扫描Co、Pt和重复数的原始全文仍需扩展。已定位硕士论文[曾嘉裕 / Tseng, 2011 · SRC-000018](../library/records/SRC-000018.md)的相关章节及2014论文[Lee et al., 2014 · SRC-000006](../library/records/SRC-000006.md)，但未取正文，本页不引用它们的最佳厚度或图级结果。

第二阶段补读的[Aköz et al., 2026 · SRC-000013](../library/records/SRC-000013.md)提供普通Co/Pt在Ta/Ru与Ta/CuN缓冲、重复4/6次及330°C退火的VSM对照（pp.4–6 Fig.2、Table1）。它补充缓冲/重复数证据，未完成Co/Pt厚度二维扫描；PMA与织构解释也不能由方正度或Hc单独定量证明。其单磁块对照和6/4 SAF为不同样品组，不能合并。当前无需为补齐目录而先追完006/018，优先级已降为辅助补充。

相关专题：[Ru耦合](03-ru-antiferromagnetic-coupling.md) · [磁矩读出](05-moment-and-reversal.md)。

[专题入口](../index.md) · [待补材料](../gaps/missing-materials.md)
