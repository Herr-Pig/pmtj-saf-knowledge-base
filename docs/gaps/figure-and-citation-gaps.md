# 原图与引用核验缺口

图片许可与科学阅读状态分别记录。两张旧SVG已按所有者决定撤出MkDocs目录，源文件保存在忽略的本地批次档案；不再追查其许可，也不作为待批准的图。

## 六个专题的原图选择

| 专题 | 原文定位 | 使用方式与许可 | 支持与边界 |
|---|---|---|---|
| 01 | [Current-induced magnetization switching in atom-thick tungsten engineered perpendicular magnetic tunnel junctions with large tunnel magnetoresistance](https://www.nature.com/articles/s41467-018-03140-z/figures/1)，Fig. 1，PDF p.2 | 链接出版商原图；CC BY 4.0，按批次许可登记 | 本库将其用于区分器件层序及证据归属，不把自由层minor loop当成参考侧W桥的独立交换常数测量；正文与SI的stack A/B差异仍保留。 |
| 02 | [Unconventional Seedless Multilayers with Large Perpendicular Anisotropy for Back-End-of-Line Compatible Spintronic Devices](https://acs.figshare.com/articles/journal_contribution/Unconventional_Seedless_Multilayers_with_Large_Perpendicular_Anisotropy_for_Back-End-of-Line_Compatible_Spintronic_Devices/16934265)，Fig. S2，PDF p.2 | 提取原始嵌入JPEG；CC BY-NC 4.0，按批次许可登记 | 不将这个范围推广到所有无Ta的CoFeB/W/CoPt，也不凭负场台阶给每层强行归属。仅从PDF提取该嵌入JPEG，未重绘或修改图内像素；原文图注另以中文概述。 |
| 02 | [Novel multifunctional RKKY coupling layer for ultrathin perpendicular synthetic antiferromagnet](https://www.nature.com/articles/s41598-018-29913-6/figures/2)，Fig. 2，PDF p.3 | 链接出版商原图；CC BY 4.0，按批次许可登记 | 这是Ru/W多功能AF间隔，不能与上面的FM桥接Fig. S2合并为一条W厚度曲线；J提取依赖原文Ms、磁层厚度和场定义。 |
| 03 | [Optical control of RKKY coupling and perpendicular magnetic anisotropy in a synthetic antiferromagnet](https://www.nature.com/articles/s41467-025-59689-z/figures/1)，Fig. 1，PDF p.2 | 链接出版商原图；CC BY-NC-ND 4.0，按批次许可登记 | 这一幅是Ru0.8nm样品，不是完整Ru厚度扫描；不能凭它选通用最佳Ru厚度。只引用出版商原图完整链接，不裁剪、拼接或翻译图内文字；非商业、不得分享改编图的限制已按所有者决定接受并遵守。 |
| 04 | [Modification of perpendicular magnetic anisotropy and domain wall velocity in Pt/Co/Pt by voltage-induced strain](https://www.nature.com/articles/srep07921/figures/1)，Fig. 1，PDF p.2 | 链接出版商原图；CC BY 4.0，按批次许可登记 | 是Pt/Co/Pt单磁层邻近体系，不是Co/Pt/Ru SAF，也不是Co和Pt厚度的完整二维优化；不能将该趋势代替含Ta的seedless多层。 |
| 05 | [Perpendicular magnetic tunnel junctions with a synthetic storage or reference layer: A new route towards Pt- and Pd-free junctions](https://www.nature.com/articles/srep21246/figures/5)，Fig. 5，PDF p.5 | 链接出版商原图；CC BY 4.0，按批次许可登记 | 点是实验提取量，线是模型或经验拟合；不能把拟合线当成另一项独立实验。该图为FeCoB/Ru/FeCoB，不能据此直接赋值Co/Pt磁矩或MOKE光学权重。 |
| 06 | [Novel multifunctional RKKY coupling layer for ultrathin perpendicular synthetic antiferromagnet](https://www.nature.com/articles/s41598-018-29913-6/figures/3)，Fig. 3，PDF p.4 | 链接出版商原图；CC BY 4.0，按批次许可登记 | 图本身是磁性测量，公式是模型近似；它不是微磁模拟结果。Hex与Hex2的不同位置不能解释成两个独立Ru交换常数，宏自旋近似也不能排除成核和磁畴。 |

## 高优先级待办

- ACS Fig. S2来源、图注、页码及Figshare CC BY-NC 4.0已经核实；所有者已批准本批非商业、保留署名的原图使用。原SI的全文不进入Git。
- Ma (2025) Fig. 1使用CC BY-NC-ND 4.0，必须保持完整原图且限非商业用途；使用须遵守相应限制。用途或呈现改变时重新审核。
- 普通无Ta插层CoFeB/W/CoPt的直接W厚度系列仍缺，不能用Ru/W-AF曲线或自由层W-spacer代替。
- Li (2018)的Co/Pt/Ru厚度系列、Böhm (2019)微磁学Fig. 3及Muehlenhoff的SQUID/MOKE Fig. 6尚未完成图像转载许可核验，本轮保留记录与官方来源，不复制其图。宏自旋专题所嵌Fig. 3明确标为实验图，未冒充微磁学结果。
- 013内部Ru最佳值与J式μ0口径差异、012全文缺口、001/002原文差异继续保留；本轮排版不解决这些科学问题。

## 书目核验边界

五篇Nature/Springer文章直接核对出版商citation元标签、全文和出版PDF；ACS (2021)核对出版商条目、官方SI与Figshare；其余DOI使用出版商登记的Crossref作字段对照。Crossref不替代原文阅读。完整逐条状态见`publication/bibliography-verification.json`（仓库元数据，不打包进站点）。

期刊条目保留完整作者、年、题名、期刊、卷期、页码/文章号和DOI。011期号17、020期号14来自明确登记字段；不填不存在或未确认的期号。讲座频道与讲者分开，NIST两位作者采用Donahue and Porter (1999)。无DOI资料明确注明未提供，学位论文/讲义总PDF页数不冒充期刊页码。

未完成出版社或机构字段逐项复核的条目保持待核实；本轮请求返回403、429或挑战页时，不能写成核验成功。来源可访问也不等于版权可转载。

视频021的官方页面当前时长元数据为PT75M9S，与旧目录75:08差1秒，保留原记录并列为待播放器人工核对；不生成科学时间戳。006/012/013/018本轮分别遇到验证页、403或连接限制，未将这些请求计为新的原文核验成功。


## B20261029增量与统一审核

本批新增6条去重资料，4条完成正文关键证据阅读，2条仅书目/官方预览；目录共29条。已准备的10幅均为**论文原图**。本批正式嵌入并登记所有者批准的七幅；Yang and Lai (2021) Figs.2/4、Yang et al. (2026) Fig.2保留图号、页码、科学解释及官方链接，仅链接、不嵌入，其图像使用留入后续资料批次。三张旧本地图中的两张就是已撤下SVG，另一张是ACS Fig.S2；没有额外三张新图，也没有七幅原创示意图。无需生成新示意图凑数。

- [Chatterjee et al. (2017)](../library/records/SRC-000028.md)：HAL出版PDF已读，封盖/完整器件和底电极分组明确；原图转载许可未核，不提取图，仅链接PDF图页。独立SI未确认。
- [Yun et al. (2016)](../library/records/SRC-000029.md)、[Yang et al. (2021)](../library/records/SRC-000030.md)：身份与DOI已核，全文请求403。不给摘要峰值或缺页补图号；优先保留为核心候选。
- [Kim et al. (2023)](../library/records/SRC-000031.md)：正文已读，面内IrMn-MTJ辅助证据；正文封盖5nm与Fig.3/4图注4nm差异不修造。XRD为独立增厚样品；官方SI只定位、未取得。
- [Yang et al. (2026)](../library/records/SRC-000032.md)：发表年按2026，不按DOI字符串2025；1ns实验、100ps模拟、Table1电路/布局模拟分开。Methods/Results的CoFeB厚度和SI S3公式符号复核仍保留。
- [Yang and Lai (2021)](../library/records/SRC-000033.md)：Ru/Re总间隔、上/下界面、退火与简化表征样品分列；p.5样品数量文字及主文/SI S3层序称呼差异保留。

旧012全文、013原文内部差异、无Ta桥接系列缺口并未因新增文献自动关闭。后续按publication/BATCH_WORKFLOW.md积累工作分支或待整理区，统一生成变更/哈希再审核。发布遵循批次约定，阅读及版权的未决项继续保留。


## 2026-10-30新增原图证据索引

新增10条去重图证据定位，4幅合法原图嵌入本地候选，其余6条仅官方来源链接。035的两图目前核到正文和图注，高清像素未核，不列为视觉核验通过。本站本批未部署，原七幅批准保持；新图owner字段仍待批。

| 文献/原图 | 版本页码 | 物理含义及边界 | 许可/方式 |
|---|---|---|---|
| [Kim et al. (2015) Fig. 4](https://www.nature.com/articles/srep16903/figures/4) | source as linked p.4 | W厚度系列M–H与Hk/Hex分列；双CoFeB记录层，不是Co/Pt参考桥；RKKY起源未定 | CC BY 4.0；official image embed in local candidate |
| [Karayev et al. (2019) Fig. 3](https://link.aps.org/accepted/10.1103/PhysRevMaterials.3.041401#page=16) | CHORUS accepted manuscript, 17 PDF pages p.16 | Ru楔形超晶格主回线、minor loop和回线交叉；CHORUS正文/图注已读，原图像素待核；不是两磁块MOKE | 转载许可未核；official source link only |
| [Karayev et al. (2019) Fig. 4](https://link.aps.org/accepted/10.1103/PhysRevMaterials.3.041401#page=17) | CHORUS accepted manuscript, 17 PDF pages p.17 | Ru/Pt/Ir厚度相区及饱和场；Hs半定量J口径不等于单层minor-loop提取 | 转载许可未核；official source link only |
| [Mouhoub et al. (2023) Fig. 5](https://arxiv.org/pdf/2211.02497v1#page=5) | arXiv v1 p.5 | 模式实测点、模型曲线与厚度分辨本征模；实测符号与模拟曲线分开；不是Co/Pt-Ru厚度扫描 | 转载许可未核；official source link only |
| [Lee et al. (2016) Fig. 1](https://www.nature.com/articles/am2016162/figures/1) | source as linked p.2 | 完整堆结构及封盖厚度—TMR；top free不是top reference；TMR曲线横轴是cap | CC BY 4.0；official image embed in local candidate |
| [Lee et al. (2016) Fig. 2](https://www.nature.com/articles/am2016162/figures/2) | source as linked p.2 | 400°C后完整pMTJ主回线和minor-loop；作者层归属非层分辨实验；不是同一样品退火前后对照 | CC BY 4.0；official image embed in local candidate |
| [Lee et al. (2016) Supplementary 2](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fam.2016.162/MediaObjects/41427_2016_BFam2016162_MOESM3_ESM.pdf) | official single-page supplementary PDF p.1 | W桥厚度—CIPT TMR峰约0.24nm；不是交换能或PMA厚度曲线；不重绘或数字化数据 | CC BY 4.0；official source link only |
| [Chi et al. (2024) Fig. 2](https://arxiv.org/pdf/2102.01283v3#page=3) | arXiv v3 p.3 | 磁矩/厚度、Keff·teff及线性拟合；总Keff与去退磁项MCA不同；作者稿页码未映射正式版 | 正式版CC BY 4.0；作者稿转载范围未另核；official source link only |
| [Das et al. (2014) Fig. 1](https://www.nature.com/articles/srep05328/figures/1) | source as linked p.2 | Co/Pt退火前后M–H及厚度/结构信息；350°C/1h特定三重复组，非一般退火规律 | CC BY-NC-ND 4.0；official image embed in local candidate |
| [Das et al. (2014) Fig. 3](https://www.nature.com/articles/srep05328/figures/3) | source as linked p.4 | EDX及HAADF推定Co/Pt剖面；元素剖面含纯Pt端层/楔形模型；机理仍为作者解释 | CC BY-NC-ND 4.0；official source link only |

不将论文原图称为原创示意图；不新增AI图、论文全文附件、数字化实验数据或未经核实的许可。图库中的模型面板也保留模型身份。
