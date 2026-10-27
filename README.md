# PMTJ-SAF Knowledge Base

此项目是独立的公开文献知识库框架，目标为Public GitHub仓库和MkDocs Material / GitHub Pages。已创建Public目标仓库；Pages配置与实际部署状态以迁移报告及GitHub返回为准，网站没有自动发布。

**研究正文尚未导入。** 六个专题、文献记录和公式解释的候选先保留在私人工作区，待所有者明确选择并审核后再手动复制。当前目录只含新建的框架、公开政策和技术依赖，不含实验数据、私人历史或论文全文。

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

发布检查额外要求`publication/owner-approval.json`中有真实的所有者审核及匹配的文件哈希，且六个专题已导入。当前状态故意为未批准。

GitHub Actions只允许手动触发，不监听push、pull_request或定时事件；部署必须绑定已审核提交。没有连接私人仓库的令牌、子模块、自动复制或同步任务。

未创建或确认同名远程仓库前，不添加remote或推送。技术框架可以按占位页冻结基线单独审核上传，这不代表任何研究正文已获批准，也不触发部署。本机仅为这两个新仓库使用已识别GitHub账号及noreply提交身份，不改全局设置。公开可读不自动授予本库原创内容的额外复用许可；第三方软件许可证单独保留，论文图像必须逐项证明许可。
