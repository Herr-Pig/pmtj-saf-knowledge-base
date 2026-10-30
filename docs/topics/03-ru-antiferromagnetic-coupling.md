# 03｜Co/Pt/Ru/Co/Pt的反铁磁耦合及Ru厚度效应

主阅读：[Li et al. (2018)](../library/records/SRC-000005.md) → [Ma et al. (2025)](../library/records/SRC-000010.md) → [Cuchet et al. (2016)](../library/records/SRC-000003.md)。Ru/W多功能间隔参照[Chatterjee et al. (2018)](../library/records/SRC-000001.md)，不可与单Ru直接合并。

## 1. 先保留各论文的实际对照

| 研究 | 相邻磁性结构及变量 | 原文锚点 | 边界 |
|---|---|---|---|
| [Li et al. (2018)](../library/records/SRC-000005.md) | [Pt0.6/Co0.6]2/Ru(t)/[Co0.6/Pt0.6]4；t=0、0.6、0.9、1.2、1.6nm | Figs.1–2，印刷127502-2至-3 | 是离散厚度组，不足以确定所有振荡峰位置 |
| [Ma et al. (2025)](../library/records/SRC-000010.md) | [Pt0.6/Co0.6]4/Ru0.8/[Co0.6/Pt0.6]2；SI另测Ru0.6 | Fig.1；SI Note2、Fig.S2 | 上下重复顺序、盖层、测量及激发与Li不同 |
| [Cuchet et al. (2016)](../library/records/SRC-000003.md) | FeCoB/Ru/FeCoB及Ta/Ru插层 | Figs.1–3 | 相邻材料不同，不能用其Ru最优点替代Co/Pt |
| [Chatterjee et al. (2018)](../library/records/SRC-000001.md) | Co/Pt/Ru(tx)/W(ty)/FeCoB | Fig.2、SI Fig.S1 | 双间隔层共同改变耦合与结构功能 |

[Li et al. (2018)](../library/records/SRC-000005.md)在其已测样品中见Ru0.6/0.9/1.2的AF特征，Ru1.6与无Ru样品为FM类型。作者明确未制备0–0.6nm之间的样品，因此该区间的行为是原文推测，不作为已测厚度连续曲线。[Liu et al. (2019)](../library/records/SRC-000012.md)虽然标题直接相关，但正文未取得，本页不引用摘要里的最大J或峰值作为定量证据。

## 2. Hex、事件场和J不是同一列

[Li et al. (2018)](../library/records/SRC-000005.md) Fig.1b将Hex定义为minor-loop位移；[Ma et al. (2025)](../library/records/SRC-000010.md) Results首段给出以下定义，见其Fig.1：

$$
H_{\mathrm{ex}}=\frac{H_{\mathrm{up}}+H_{\mathrm{down}}}{2},\qquad
H_c=\frac{H_{\mathrm{up}}-H_{\mathrm{down}}}{2}.
$$

这里仅将既有定义排为公式，不改变场方向或符号约定。[Chatterjee et al. (2018)](../library/records/SRC-000001.md) Eq.(1)使用$H_{\mathrm{ex}} M_s t$，p.3说明先用首翻转近似、minor-loop中心更准确。[Cuchet et al. (2016)](../library/records/SRC-000003.md) Fig.2还说明FM情况下未能提取耦合场而把图中值置零，这个零不等于证明J=0。

此外Li原文tFM写成上下FM总厚度，Chatterjee用PL厚度。把两列J直接排序之前，必须核对归一化磁矩和定义。本库暂保留各自口径，不自动“统一”原文公式或补因子。


!!! note "原文图｜Ma et al. (2025)，Fig. 1"

    [![Ma et al. (2025) Fig. 1：a为Co/Pt多层-Ru0.8nm-SAF的实际层序示意；b为300K静态面外VSM回线，图注区分两支扫场方向和minor-loop的Hup、Hdown。](https://media.springernature.com/lw685/springer-static/image/art%3A10.1038%2Fs41467-025-59689-z/MediaObjects/41467_2025_59689_Fig1_HTML.png){ loading=lazy }](https://www.nature.com/articles/s41467-025-59689-z/figures/1)

    **出处：** [Ma et al. (2025)](../library/records/SRC-000010.md)，*Optical control of RKKY coupling and perpendicular magnetic anisotropy in a synthetic antiferromagnet*，Fig. 1，PDF p.2。[原图与图注](https://www.nature.com/articles/s41467-025-59689-z/figures/1) · [出版PDF定位](https://www.nature.com/articles/s41467-025-59689-z.pdf#page=2) · [DOI](https://doi.org/10.1038/s41467-025-59689-z)。

    **原文图注要点／直接证据：** a为Co/Pt多层-Ru0.8nm-SAF的实际层序示意；b为300K静态面外VSM回线，图注区分两支扫场方向和minor-loop的Hup、Hdown。

    **作者解释：** 作者从minor-loop位移与半宽分别定义Hex和Hc；此处与上方公式一起阅读。

    **本库分析与限制：** 这一幅是Ru0.8nm样品，不是完整Ru厚度扫描；不能凭它选通用最佳Ru厚度。只引用出版商原图完整链接，不裁剪、拼接或翻译图内文字；非商业、不得分享改编图的限制已按所有者决定接受并遵守。

    **版权与改动：** Ma et al. (2025)，原文Fig. 1；[CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/)，依据[官方许可登记](https://www.nature.com/articles/s41467-025-59689-z#rightslink)。图内内容保持原样，中文仅为旁列概述。

## 3. 温度实验与工艺退火分开

[Li et al. (2018)](../library/records/SRC-000005.md) Figs.3–4为变温测量，Ru0.6与0.9/1.2的温度依赖不同，非单一线性规律。其低温非单调原因作者明确未确定。[Devolder et al. (2016)](../library/records/SRC-000011.md)则通过不同退火后FMR拟合研究耦合衰减；二者不能组成同一个“退火温度趋势”。

[Ma et al. (2025)](../library/records/SRC-000010.md) Fig.3用SQUID及MOKE比较静态升温，与光激发Fig.2的Hc/Hex响应不同。正文提出费米能和陷阱态机制、用计算支持（Figs.4–5）；这仍是作者解释，不是本库独立证明。

## 4. 本轮比较后的认识

可以确认Ru效应必须绑定相邻磁层、厚度范围和热历史；不能宣布一个跨结构通用最佳厚度。补偿改善、有效场增大和交换能增大需要分开检查。Ma SI TableS1改变Co/Pt重复数时报告的Hex变化，也不能单独证明间隔层本征J同比变化。

第二阶段已补读[Aköz et al. (2026)](../library/records/SRC-000013.md)：电子束蒸发的Co0.35/Pt0.15、6/4 SAF，Ru=0.60–0.80nm、0.05nm步长，330°C/30min退火。原文Fig.4按两支主回线事件场半差提取Hex，不是这里默认的minor-loop中心。p.7、p.10、p.11对退火后0.60/0.80nm最强的说法存在差异，p.8/p.10的J近似式也有μ0写法差异；因此不据此宣布最佳Ru厚度，更不能与Li的变温系列混为对照。实际层序及逐项定位见013。

下一步优先补[Liu et al. (2019)](../library/records/SRC-000012.md)全文及核对013差异，再比较minor-loop、磁矩校准和误差口径。

相关专题：[磁矩与翻转](05-moment-and-reversal.md) · [模型与判据](06-models-and-criteria.md)。

[专题入口](../index.md) · [缺失材料](../gaps/missing-materials.md)


## 5. 本批补读：Ru/Re界面位置与耐退火

[Yang and Lai (2021)](../library/records/SRC-000033.md)比较Ru0.79、Ru0.61/Re0.18和Re0.18/Ru0.61等间隔，主要对照固定总间隔0.79nm、450°C退火1h。其磁块为Co0.6/Pt1/Co0.6，不是其他论文的6/4重复组。Fig.2（PDF p.3）先给VSM回线；Fig.4（p.4）再给按该文定义提取的J。原文J=Ms·t·Hex在p.2为无编号式，不另造公式号。

本库比较：上、下界面Re插入效果不同，支持把层序与热历史列入对照条件；并不能由固定总间隔系列推出所有纯Ru的通用最优厚度。其简化XRR样品、STEM结构及作者的扩散解释也应与磁性提取量分开。[Yun et al. (2016)](../library/records/SRC-000029.md)已登记书目但未取全文，不引用摘要峰值来填补当前厚度扫描。

!!! note "原文图号定位（仅链接）｜Yang and Lai (2021)，Fig. 2"

    [Yang and Lai (2021)，Fig. 2（官方原图链接）](https://www.nature.com/articles/s41598-021-94640-4/figures/2)

    **出处与图注要点：** [Yang and Lai (2021)](../library/records/SRC-000033.md)，*High thermal durability of Ru-based synthetic antiferromagnet by interfacial engineering with Re insertion*，Fig. 2，PDF p.3。黑色为Ru0.79nm，红色为Ru0.61/Re0.18nm；对比沉积态与450°C、1h后VSM回线。 [官方图注](https://www.nature.com/articles/s41598-021-94640-4/figures/2) · [出版PDF](https://www.nature.com/articles/s41598-021-94640-4.pdf#page=3)。

    **作者解释：** 作者将Ru/Re的较慢耦合劣化与上界面互混抑制联系；另用XRR和STEM支持讨论。

    **本库分析与限制：** 不是纯Ru完整厚度扫描，也不是PMA定量曲线；层序和作者的J归一化口径必须保留。

    **版权：** Yang and Lai (2021)，原图内容未改；[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)，见[出版商许可](https://www.nature.com/articles/s41598-021-94640-4#rightslink)。图中作者示意面板也属于论文原图，不是本库原创。



[完整参考文献](../references.md) · [原图来源与核验事项](../gaps/figure-and-citation-gaps.md)


## W记录层与厚度模型的原文证据补充

[Mouhoub et al. (2023)](../library/records/SRC-000036.md)的作者稿固定Ru0.7nm而改变沉积态CoFeB单层5–40nm，是面内VSM/VNA-FMR与厚度方向模型的对照，不是Co/Pt-Ru厚度扫描。其Table I分开总耦合Jtot与orange-peel修正后的Jex；与[Yang and Lai (2021)](../library/records/SRC-000033.md)的Ru/Re loop-shift提取量比较时，应先核场定义、磁层均匀性及粗糙度假设。

[Karayev et al. (2019)](../library/records/SRC-000035.md)已补读CHORUS正文与图注，高清图像像素仍待核；不以未完成的图像核验关闭Ru厚度缺口。012、029的原文及013内部差异仍需独立收敛。

## Ru厚度相区不能跨层序直接拼接

本轮补读[Karayev et al. (2019)](../library/records/SRC-000035.md)的官方CHORUS正文：其[Pt/Co/Ru]N让Co之间还夹Pt，反常Hall回线及minor loops显示Ru依赖、多级翻转和局部回线交叉。它既不同于[Li et al. (2018)](../library/records/SRC-000005.md)两磁块，也不同于[Aköz et al. (2026)](../library/records/SRC-000013.md)6/4结构。Hall平台中的层数归属是作者结合堆结构作的解释，不等于深度分辨磁成像。

尤其需要把三种场分开：Karayev的饱和场Hs用于半定量J估算；其minor-loop位移给独立相关的耦合标志；013的Hex取主回线事件半差。回线交叉作者关联DMI与IEC竞争，但仍要求进一步模型研究，不能直接宣称已证明skyrmion或套成两块SAF的第三步翻转。

Ru的通用“最佳厚度”仍无依据。001的0.4/0.45nm冲突已限定为SI纯Ru对照；013对0.60/0.80nm的冲突及μ0口径仍在。012仍未取得原文，不能用新超晶格结果替它补全或关闭缺口。
