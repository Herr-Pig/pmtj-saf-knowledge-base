# 03｜Co/Pt/Ru/Co/Pt的反铁磁耦合及Ru厚度效应

主阅读：[SRC-000005](../library/records/SRC-000005.md) → [SRC-000010](../library/records/SRC-000010.md) → [SRC-000003](../library/records/SRC-000003.md)。Ru/W多功能间隔参照[SRC-000001](../library/records/SRC-000001.md)，不可与单Ru直接合并。

## 1. 先保留各论文的实际对照

| 研究 | 相邻磁性结构及变量 | 原文锚点 | 边界 |
|---|---|---|---|
| Li2018 | [Pt0.6/Co0.6]2/Ru(t)/[Co0.6/Pt0.6]4；t=0、0.6、0.9、1.2、1.6nm | Figs.1–2，印刷127502-2至-3 | 是离散厚度组，不足以确定所有振荡峰位置 |
| Ma2025 | [Pt0.6/Co0.6]4/Ru0.8/[Co0.6/Pt0.6]2；SI另测Ru0.6 | Fig.1；SI Note2、Fig.S2 | 上下重复顺序、盖层、测量及激发与Li不同 |
| Cuchet2016 | FeCoB/Ru/FeCoB及Ta/Ru插层 | Figs.1–3 | 相邻材料不同，不能用其Ru最优点替代Co/Pt |
| Chatterjee2018 | Co/Pt/Ru(tx)/W(ty)/FeCoB | Fig.2、SI Fig.S1 | 双间隔层共同改变耦合与结构功能 |

Li2018在其已测样品中见Ru0.6/0.9/1.2的AF特征，Ru1.6与无Ru样品为FM类型。作者明确未制备0–0.6nm之间的样品，因此该区间的行为是原文推测，不作为已测厚度连续曲线。Liu2019 [SRC-000012](../library/records/SRC-000012.md)虽然标题直接相关，但正文未取得，本页不引用摘要里的最大J或峰值作为定量证据。

## 2. Hex、事件场和J不是同一列

Li2018 Fig.1b将Hex定义为minor-loop位移；Ma2025 Results首段给出以下定义，见其Fig.1：

$$
H_{\mathrm{ex}}=\frac{H_{\mathrm{up}}+H_{\mathrm{down}}}{2},\qquad
H_c=\frac{H_{\mathrm{up}}-H_{\mathrm{down}}}{2}.
$$

这里仅将既有定义排为公式，不改变场方向或符号约定。Chatterjee2018 Eq.(1)使用$H_{\mathrm{ex}} M_s t$，p.3说明先用首翻转近似、minor-loop中心更准确。Cuchet2016 Fig.2还说明FM情况下未能提取耦合场而把图中值置零，这个零不等于证明J=0。

此外Li原文tFM写成上下FM总厚度，Chatterjee用PL厚度。把两列J直接排序之前，必须核对归一化磁矩和定义。本库暂保留各自口径，不自动“统一”原文公式或补因子。

## 3. 温度实验与工艺退火分开

Li2018 Figs.3–4为变温测量，Ru0.6与0.9/1.2的温度依赖不同，非单一线性规律。其低温非单调原因作者明确未确定。Devolder2016 [SRC-000011](../library/records/SRC-000011.md)则通过不同退火后FMR拟合研究耦合衰减；二者不能组成同一个“退火温度趋势”。

Ma2025 Fig.3用SQUID及MOKE比较静态升温，与光激发Fig.2的Hc/Hex响应不同。正文提出费米能和陷阱态机制、用计算支持（Figs.4–5）；这仍是作者解释，不是本库独立证明。

## 4. 本轮比较后的认识

可以确认Ru效应必须绑定相邻磁层、厚度范围和热历史；不能宣布一个跨结构通用最佳厚度。补偿改善、有效场增大和交换能增大需要分开检查。Ma SI TableS1改变Co/Pt重复数时报告的Hex变化，也不能单独证明间隔层本征J同比变化。

第二阶段已补读[SRC-000013](../library/records/SRC-000013.md)：电子束蒸发的Co0.35/Pt0.15、6/4 SAF，Ru=0.60–0.80nm、0.05nm步长，330°C/30min退火。原文Fig.4按两支主回线事件场半差提取Hex，不是这里默认的minor-loop中心。p.7、p.10、p.11对退火后0.60/0.80nm最强的说法存在差异，p.8/p.10的J近似式也有μ0写法差异；因此不据此宣布最佳Ru厚度，更不能与Li的变温系列混为对照。实际层序及逐项定位见013。

下一步优先补Liu2019全文及核对013差异，再比较minor-loop、磁矩校准和误差口径。

相关专题：[磁矩与翻转](05-moment-and-reversal.md) · [模型与判据](06-models-and-criteria.md)。

[专题入口](../index.md) · [缺失材料](../gaps/missing-materials.md)
