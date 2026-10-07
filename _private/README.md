# 私密空间 · 使用手册

这个目录放**不想公开**的 Markdown 文章。目录里的 `*.md` 全部被 `.gitignore` 忽略，**永远不会被推到公开仓库**。

## 一、写一篇私密文章

1. 在本目录新建 `笔记名.md`（文件名随意，会成为网址的一部分），开头可写：

   ```yaml
   ---
   title: 文章标题
   date: 2026-10-07 20:00:00 +0800
   ---
   ```

2. 到项目根目录运行加密脚本（让 AI 代跑也行）：

   ```bash
   python3 scripts/encrypt_private.py 账号 密码
   ```

   脚本会生成两样东西（这两个是**加密后的密文页**，需要提交推送）：
   - `private.md` → 列表页 `/private/`
   - `private-<文件名>.md` → 单篇页 `/private/<文件名>/`

3. 用 GitHub Desktop 提交推送 → 线上更新。

## 二、审批别人申请账号

1. 对方在 `/apply/` 填表 → 得到一段密文 → 发给你
2. 运行：`python3 scripts/audit_apply.py "<密文>"` → 确认后自动写入 `accounts.json`
3. **必须重跑** `python3 scripts/encrypt_private.py`（把新账号的密钥信封包进每篇文章），再推送
4. 告诉对方去 `/private/` 用账号密码登录

> ⚠️ 忘记第 3 步，新账号是登不进去的。

## 三、删账号 / 改密码

编辑根目录 `accounts.json` → 重跑加密脚本 → 推送。

## 四、安全须知

- `accounts.json`（账号密码明文清单）和 `scripts/keys/private_key.pem`（RSA 私钥）**只在你电脑上**，已加入 `.gitignore`
- **不要备份到公开仓库**，也不要把这两个文件发给别人
- 密码忘了没法找回，只能重新加密（所有人密码会一起重置）
