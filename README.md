# PMTJ-SAF Knowledge Base

此项目是独立的公开文献知识库，使用MkDocs Material与GitHub Pages。

2026-10-28，所有者审核并批准36份候选文本；公开知识库另包含1份技术导航首页（`docs/index.md`），因此审批记录列出37个科学文档/导航文件路径，其中36份属于明确批准的候选文本。已按审核哈希导入六个专题、23条文献记录、统一索引及元数据、证据规则、公式定位和三份资料缺口清单。后续编辑性修订单独记录，不改变科学结论、公式、数据或文献记录。

[公开仓库](https://github.com/Herr-Pig/pmtj-saf-knowledge-base) · [网站地址](https://herr-pig.github.io/pmtj-saf-knowledge-base/) · [专题入口](docs/index.md) · [文献索引](docs/library/index.md)

## 本地构建

```text
python -m pip install -r requirements.txt
python tools/site.py build
python tools/site.py preview --port 8766
```

在浏览器访问回环地址127.0.0.1的8766端口。构建每次写入新的派生目录，不清理旧构建。科学内容以`docs/`内获准文件为唯一内容源。

## 公开审核与手动发布

阅读[PUBLICATION_POLICY.md](PUBLICATION_POLICY.md)。Git索引逐文件检查命令：

```text
python tools/publication_audit.py
```

发布检查额外要求`publication/owner-approval.json`中有真实的所有者审核及匹配的文件哈希，且六个专题已导入。本批所有者批准记录覆盖36份指定候选文本；技术导航首页单独列为辅助导航文件。公开图片许可登记仍为空。新增或修改的科学内容须重新审核并更新哈希。

构建通过并创建提交后，运行：

```text
python tools/publication_audit.py --release --expected-commit <完整提交SHA>
```

随后在GitHub Actions选择手动Pages工作流，输入同一个完整提交SHA。工作流会重新检查批准哈希和提交内容，再构建与部署；实际发布是否成功以该次工作流结果为准。

GitHub Actions只允许手动触发，不监听push、pull_request或定时事件；部署必须绑定已审核提交。没有连接私人仓库的令牌、子模块、自动复制或同步任务。

论文全文、研究图片、私人历史、模型规格和实验资料不在本批中。公开可读不自动授予本库原创内容的额外复用许可；第三方软件许可证单独保留，论文图像必须逐项证明许可。研究资料的待核实事项见`docs/gaps/`。
