# 04｜Co/Pt厚度、重复次数和PMA优化

阅读：[Chatterjee et al. (2021)](../library/records/SRC-000004.md) → [Shepley et al. (2015)](../library/records/SRC-000026.md) → [Ogrodnik et al. (2021)](../library/records/SRC-000025.md)；重复次数结合[Chatterjee et al. (2018)](../library/records/SRC-000001.md)、[Muehlenhoff et al. (2021)](../library/records/SRC-000019.md)，界面磁矩参考[Darwin (2023)](../library/records/SRC-000009.md)。

## 1. Co厚度趋势为什么不能脱离结构

[Shepley et al. (2015)](../library/records/SRC-000026.md)的玻璃/Ta/Pt/Co(t)/Pt在t=0.85、0.95、1.0nm范围内，Fig.1b inset的Keff随Co增厚下降；由EHE低场段提取Hk，再结合SQUID的Ms，见Eq.(3)。SI §II、Figs.S3及Eqs.S9–S11说明高场偏离相干旋转并成畴，因此不是将整条曲线简单拟合成单宏自旋。

[Chatterjee et al. (2021)](../library/records/SRC-000004.md)的[Co(t)/Ta0.2/Pt1.1]5 seedless体系却在所测范围显示Keff随Co增厚提高（作者稿Fig.3）。这不是可以直接宣布“哪个趋势正确”的比较：界面插层、厚度区间、生长顺序、热处理和体积归一化不同。该论文计算Keff时考虑Co、Pt及FeCoB总厚度，不能默认等同于仅按Co磁性体积归一化的数据。


!!! note "原文图｜Shepley et al. (2015)，Fig. 1"

    [![Shepley et al. (2015) Fig. 1：a是由EHE低场段外推各向异性场的示例；b比较Co=0.85、0.95、1.0nm时各向异性能随应变变化，插图列未施加应变的Keff与Co厚度。](https://media.springernature.com/lw685/springer-static/image/art%3A10.1038%2Fsrep07921/MediaObjects/41598_2015_Article_BFsrep07921_Fig1_HTML.jpg){ loading=lazy }](https://www.nature.com/articles/srep07921/figures/1)

    **出处：** [Shepley et al. (2015)](../library/records/SRC-000026.md)，*Modification of perpendicular magnetic anisotropy and domain wall velocity in Pt/Co/Pt by voltage-induced strain*，Fig. 1，PDF p.2。[原图与图注](https://www.nature.com/articles/srep07921/figures/1) · [出版PDF定位](https://www.nature.com/articles/srep07921.pdf#page=2) · [DOI](https://doi.org/10.1038/srep07921)。

    **原文图注要点／直接证据：** a是由EHE低场段外推各向异性场的示例；b比较Co=0.85、0.95、1.0nm时各向异性能随应变变化，插图列未施加应变的Keff与Co厚度。

    **作者解释：** 作者结合测得的Ms和各向异性场计算Keff，且正文限制了低场近相干旋转的适用区间。

    **本库分析与限制：** 是Pt/Co/Pt单磁层邻近体系，不是Co/Pt/Ru SAF，也不是Co和Pt厚度的完整二维优化；不能将该趋势代替含Ta的seedless多层。

    **版权与改动：** Shepley et al. (2015)，原文Fig. 1；[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)，依据[官方许可登记](https://www.nature.com/articles/srep07921#rightslink)。图内内容保持原样，中文仅为旁列概述。

## 2. Pt厚度的多重作用

| Pt所处位置 | 来源与锚点 | 作者支持的观察 | 不可直接推广的内容 |
|---|---|---|---|
| SL-ML重复内Pt | [Chatterjee et al. (2021)](../library/records/SRC-000004.md) SI Fig.S4，S4页 | 该Co/Ta/Pt系列有从面内到面外及Keff峰值变化 | 不能移植其1.1nm最优值给普通seeded Co/Pt |
| 种子Pt | [Chatterjee et al. (2018)](../library/records/SRC-000001.md) Figs.4–5 | 更厚种子伴随HL-PMA、粗糙度及PL翻转变化 | PMA提升与粗糙度代价同时存在，不能只留正向趋势 |
| Co层间Pt楔形spacer | [Ogrodnik et al. (2021)](../library/records/SRC-000025.md) Figs.1、5–6 | 两层PMA、FM耦合及倾斜区间共同变化 | 不是重复内Pt厚度单独优化，也不是Ru耦合 |

[Chatterjee et al. (2021)](../library/records/SRC-000004.md)把界面混合、织构、退磁能和电子杂化作为解释讨论，不能把磁滞曲线直接改写为这些微观过程均已被独立测量。[Ogrodnik et al. (2021)](../library/records/SRC-000025.md)则联合XRD、静态和FMR模型，仍需保留拟合参数身份。

## 3. 重复数至少有两种

[Chatterjee et al. (2018)](../library/records/SRC-000001.md) Fig.6改变一个HL的Co/Pt重复数，影响面磁矩与concurrent reversal。[Muehlenhoff et al. (2021)](../library/records/SRC-000019.md) 的2020年作者稿Fig.5改变三块SAF中间块Y=8/9，测得不同GMR翻转次序。[Böhm et al. (2019)](../library/records/SRC-000020.md)体系中的N却是**AF耦合FM块的总数**，块内重复另用X；不能把其N奇偶效应写成单块Co/Pt双层数奇偶效应。

本库综合判断：重复数变化应同时列总磁性厚度、界面数、面磁矩、PMA和读出层位置；仅以“增加重复能提高PMA”概括会丢失这些控制变量。

## 4. 磁矩校准不是附属步骤

[Darwin (2023)](../library/records/SRC-000009.md) §5.8、Figs.5.14–5.15采用Co/CoB厚度系列研究不同NM界面的moment/area，区分自有实验与前文综述。它提示有效磁厚度和邻近诱导磁矩值得核对，但不能将CoB/Ir/Pt参数直接代给Co/Pt/Ru。该论文与上述研究的比较属于材料边界检查，非用户样品参数估计。

## 5. 覆盖缺口

普通Co/Pt在统一工艺下同时扫描Co、Pt和重复数的原始全文仍需扩展。已定位硕士论文[曾嘉裕 (2011)](../library/records/SRC-000018.md)的相关章节及2014论文[Lee et al. (2014)](../library/records/SRC-000006.md)，但未取正文，本页不引用它们的最佳厚度或图级结果。

第二阶段补读的[Aköz et al. (2026)](../library/records/SRC-000013.md)提供普通Co/Pt在Ta/Ru与Ta/CuN缓冲、重复4/6次及330°C退火的VSM对照（pp.4–6 Fig.2、Table1）。它补充缓冲/重复数证据，未完成Co/Pt厚度二维扫描；PMA与织构解释也不能由方正度或Hc单独定量证明。其单磁块对照和6/4 SAF为不同样品组，不能合并。当前无需为补齐目录而先追完006/018，优先级已降为辅助补充。

相关专题：[Ru耦合](03-ru-antiferromagnetic-coupling.md) · [磁矩读出](05-moment-and-reversal.md)。

[专题入口](../index.md) · [待补材料](../gaps/missing-materials.md)


## 6. 本批补读：优化指标不能混列

| 来源 | 实际评价量与条件 | 不能直接替代的内容 |
|---|---|---|
| [Chatterjee et al. (2017)](../library/records/SRC-000028.md)，Figs.2–5、Table I | W/Ta封盖半结的PMA、临界厚度和退火行为 | 普通Co/Pt中Co、Pt与重复数的完整扫描 |
| [Kim et al. (2023)](../library/records/SRC-000031.md)，Figs.1–5 | 面内MTJ的TMR、Hc、结构表征 | 直接Keff测量或垂直Co/Pt-Ru参数 |
| [Yang and Lai (2021)](../library/records/SRC-000033.md)，Figs.3–6、SI S1–S3 | 固定总间隔的Ru/Re层序、J及热处理 | 用J随退火的曲线直接代替PMA或织构强度 |

原文Fig.4的纵轴是作者提取的面交换能，非Keff。作者同时用XRR拟合和STEM讨论界面机制；本库只据此要求PMA、交换和界面证据分别定位，不将单一曲线提升为全部机制的独立证明。

!!! note "原文图号定位（仅链接）｜Yang and Lai (2021)，Fig. 4"

    [Yang and Lai (2021)，Fig. 4（官方原图链接）](https://www.nature.com/articles/s41598-021-94640-4/figures/4)

    **出处与图注要点：** [Yang and Lai (2021)](../library/records/SRC-000033.md)，*High thermal durability of Ru-based synthetic antiferromagnet by interfacial engineering with Re insertion*，Fig. 4，PDF p.4。黑色Ru、红色Ru/Re、蓝色Re/Ru；纵轴为作者提取的Jex，横轴为各组退火温度/沉积态。 [官方图注](https://www.nature.com/articles/s41598-021-94640-4/figures/4) · [出版PDF](https://www.nature.com/articles/s41598-021-94640-4.pdf#page=4)。

    **作者解释：** 作者将Ru/Re的较慢耦合劣化与上界面互混抑制联系；另用XRR和STEM支持讨论。

    **本库分析与限制：** 不是纯Ru完整厚度扫描，也不是PMA定量曲线；层序和作者的J归一化口径必须保留。

    **版权：** Yang and Lai (2021)，原图内容未改；[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)，见[出版商许可](https://www.nature.com/articles/s41598-021-94640-4#rightslink)。图中作者示意面板也属于论文原图，不是本库原创。



[完整参考文献](../references.md) · [原图来源与核验事项](../gaps/figure-and-citation-gaps.md)
