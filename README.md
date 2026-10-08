# 刘子睿 · 人工智能概论 作业仓库

苏州大学未来科学与工程学院 · 人工智能方向 · 大一在读

- **在线站点**：https://liuzr-523.github.io
- **作业墙**：https://liuzr-523.github.io/homework/
- **机器可读台账**：https://liuzr-523.github.io/homework.json

> 这个仓库从第一次作业用到期末。**每一次作业是这个仓库里的一次提交，期末大作业就是这个仓库长到最后的样子。**

---

## 一、作业记录

| 次数 | 主题 | 使用工具 | 提交日期 | 截止 | 正文 |
|:--:|:--|:--|:--:|:--:|:--|
| 01 | AI 编程工具四选一 | WorkBuddy / Trae / Claude | 2026-10-08 | 2026-10-08 | [hw01 →](_posts/2026-10-08-assignment-01-ai-coding-tools.md) |

正文直接在 GitHub 上点开就是排版好的页面。想看带归档、带标签的版本，去 [在线站点](https://liuzr-523.github.io)。

新作业照着上面加一行就行。

## 二、每篇作业写什么

五段骨架，每次都一样，方便回看：

1. **老师要求做什么** —— 用自己的话复述任务，不是复制通知
2. **我实际做了什么** —— 按时间顺序，贴原始报错和实机截图
3. **卡在哪，怎么绕过去的** —— 写清「我以为是什么原因 → 实际是什么」
4. **工具替我做了多少，我自己做了多少** —— 哪些是我判定对错的、哪些是它替我干的
5. **收获 & 下次要改的**

关键在第 3 和第 4 段。**能不能看出「真的动手了」，差别就在这两段。**

## 三、机器可读的部分

每篇作业的 front matter 里有一组固定字段：

```yaml
hw: true              # 标成作业，才会进「作业墙」和台账
hw_seq: "01"          # 第几次
hw_course: 人工智能概论
hw_assigned: 2026-09-24
hw_due: 2026-10-08
hw_tool: WorkBuddy / Trae / Claude
hw_status: done       # done / wip
```

线上汇总成一份台账，程序可以直接读：

```
GET https://liuzr-523.github.io/homework.json
```

里面含 `title` / `due` / `tool` / `status` / `words` / `commit_url`，`commit_url` 能一路追到这篇作业的提交历史。

## 四、目录说明

```
_posts/              每次作业的正文（文件名 YYYY-MM-DD-assignment-NN-xxx.md）
_tabs/homework.md    「作业墙」页面，自动汇总所有带 hw: true 的文章
templates/作业模板.md  新作业从这里复制
homework.json        上面的台账，构建时自动生成
_config.yml          站点配置（标题、时区、导航、归档）
assets/img/hw01/     本次作业的截图
```

## 五、自己用：怎么发下一篇作业

1. 复制 `templates/作业模板.md` 到 `_posts/`，文件名改成 `年-月-日-assignment-序号-英文短名.md`
2. 改 front matter 里的那几个 `hw_*` 字段（**字段名别动**）
3. 按上面五段骨架写正文，截图放进 `assets/img/`
4. GitHub Desktop：写摘要 → **Commit to main** → **Push origin**
5. 等 1~3 分钟，去 Actions 页面看构建进度

**建议分几次提交**，别在截止前一次性推。提交时间线本身也是这次作业的证据。

## 六、两个坑（已经踩过）

- **Pages 的来源必须是 GitHub Actions**。Chirpy 靠 Actions 构建，Settings → Pages → Source 要是 `GitHub Actions`，选成 "Deploy from a branch" 网站不会更新
- **给应用换文件要重新签名**。往 Claude 里塞语言包导致它打不开，最后是靠这条救回来的：

  ```bash
  codesign --force --deep --sign - "/Applications/Claude.app"
  ```
