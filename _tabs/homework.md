---
icon: fas fa-clipboard-check
order: 0
---

## 作业墙

这门课的每次作业，对应这个站里的一篇文章。归档页按时间保留全部提交痕迹，[`/homework.json`](/homework.json) 是给机器读的作业台账。

{% assign hw_posts = site.posts | where: "hw", true | sort: "hw_seq" %}
{% assign hw_done = hw_posts | where: "hw_status", "done" %}
{% assign hw_all = site.posts | where: "hw", true %}

> 已完成 **{{ hw_done.size }} / {{ hw_all.size }}** 次作业 · 最近更新 {{ site.time | date: "%Y-%m-%d" }}

| # | 作业 | 发布日期 | 截止 | 主要工具 | 状态 |
|:--:|:-----|:---------|:-----|:---------|:----:|
{% for p in hw_posts -%}
| {{ forloop.rindex }} | [{{ p.title }}]({{ p.url | relative_url }}) | {{ p.date | date: "%Y-%m-%d" }} | {{ p.hw_due }} | {{ p.hw_tool }} | {% if p.hw_status == "done" %}完成{% elsif p.hw_status == "wip" %}进行中{% else %}待补{% endif %} |
{% endfor %}

记录在下面这张表，下面是每次作业怎么发。

---

## 交一次作业只要 4 步

1. 复制仓库里的 `templates/作业模板.md` 到 `_posts/`，文件名改成 `YYYY-MM-DD-assignment-0N-<英文短名>.md`
2. 改 front matter 里的 `hw_seq` / `hw_due` / `hw_tool`（这一段是机器读的，**不要动字段名**）
3. 按正文小标题填：任务 → 我实际做了什么 → 卡在哪 → 工具帮了什么忙 → 我自己的收获
4. Git 提交推送。建议**分几次提交**，别 deadline 前一次性 push —— 提交记录本身就是过程证据

## 每篇作业要有「可验证的东西」

能证明自己真的动手了，而不是抄一段：

- **原始报错全文**（不是「我遇到了一个 bug」）
- **截图**：终端输出、软件界面、版本号页面
- **自己的话复述**：工具是怎么解决问题的，下一步我打算改什么
- **给复现者的说明**：让别人照着做能跑通

## 最近一次作业

{% assign latest = hw_posts | last %}
- [{{ latest.title }}]({{ latest.url | relative_url }}) —— {{ latest.date | date: "%Y-%m-%d" }}，用 {{ latest.hw_tool }} 完成
