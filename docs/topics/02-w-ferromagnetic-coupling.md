# 02｜CoFeB/W/CoPt的铁磁耦合及W厚度效应

优先阅读：[SRC-000004](../library/records/SRC-000004.md) SI Fig.S2 → [SRC-000002](../library/records/SRC-000002.md) Fig.1 → [SRC-000001](../library/records/SRC-000001.md) Figs.2–3。本专题聚焦公开文献证据，不对特定实验样品作诊断。

## 1. 同为W，不能混成一种耦合曲线

| W的位置 | 核对来源 | 相邻材料与功能 | 本轮可作何种判断 |
|---|---|---|---|
| 顶参考层纹理打断/桥接 | ACS2021，SRC-000004 SI S2 | FeCoB/W/[Co/Ta/Pt]3及其上方Ru-SAF | 直接相关的参考层厚度与翻转证据，但插Ta多层须明示 |
| 自由层间隔 | Wang2018，SRC-000002 Fig.1c | CoFeB/W/CoFeB | minor loop支持0.2nm自由层同步，非CoFeB/W/CoPt定量证据 |
| 多功能AF间隔层之一 | Chatterjee2018，SRC-000001 Fig.2、SI S1 | Co/Pt/Ru/W/FeCoB | Ru与W共同控制AF耦合，不能当W单独FM桥 |

这是本专题最重要的文献分组。一个数值处于0.2–0.6nm范围，并不使这些体系可直接比较。

## 2. 重新核对ACS2021 Fig.S2

官方SI已下载并目视核对S2页：图注明确是**normalized ascending branch**，W为0.3、0.35、0.4、0.5nm，退火400°C。实际磁层为FeCoB1.1/W(t)/[Co0.6/Ta0.2/Pt1.1]3/Co0.6/Ru0.9/Co0.6/Pt0.25/[Co0.5/Pt0.25]6（nm）；完整层序见主记录。

作者在图上段明确把0.5nm样品解释为FeCoB与Co/Ta/Pt多层不能保持同步，并将该pSAF的优化W范围置于0.35–0.4nm。这是作者基于特定结构的结果和解释。本库没有据此给每个负场台阶指定具体层，也没有将其升级为所有CoFeB/W/CoPt的阈值。

SI S1另研究五重复SL-MLs，给出的W限制与S2不同。两页的多层次数、Pt厚度和有无完整pSAF环境都变了，不能从0.6nm与0.4nm两个数字宣称原文自相矛盾。

## 3. 跨文献比较与证据强度

Wang2018 pp.2–3展示blank-film OOP/IP与minor loop；其自由层结论由磁性测量支持，原子结构的输运计算另有简化，SI Note6省略顶部MgO。其W厚度相关TMR计算（SI Note9、Table1）更不能改名成“参考层FM交换常数曲线”。

Chatterjee2018的Ru/W体系则出现另一种权衡：W减薄可增大AF耦合，却可能不足以完成纹理打断；移除W时FeCoB翻转倾斜（正文p.3及SI S2）。作者对界面混合、织构等机制的讨论应保留“解释”身份，不能由该现象反向断言任何倾斜MOKE都源于W耦合差。

本库综合判断：对W桥有效性的比较应同时查看minor loop、各层磁矩/PMA、厚度对照及结构表征；“存在两个台阶”“TMR下降”均不足以单独量化J_W。此判断是对证据链的要求，不构成对任何特定样品的诊断。

## 4. 尚缺什么

当前直接证据较强的是Co/Ta/Pt seedless结构；仍需扩展无Ta插层的CoFeB/W/普通Co/Pt桥接实验、独立耦合提取和结构分析。需要把桥接J、厚度连续性、B吸收与PMA四种证据分列，避免一个结果同时充当四种机制证明。

相关专题：[整体结构](01-pmtj-saf-design.md) · [PMA优化](04-copt-pma-optimization.md) · [翻转实验](05-moment-and-reversal.md)。

[专题入口](../index.md) · [证据缺口](../gaps/unresolved-evidence.md)
