---
title: 第一个踩坑：仓库推上去，网站却没变
date: 2026-09-28 11:30:00 +0800
categories: [踩坑记录]
tags: [GitHub Pages, 备忘]
---

把文件推到 GitHub 之后，网站却还是老样子——这是我建站时踩的第一个坑，记录一下排查顺序。

## 现象

GitHub Desktop 里显示推送成功，但打开网站还是旧页面。

## 原因与排查顺序

1. **构建需要时间**：推送后 GitHub 要 1～3 分钟重新生成网页，先等一会儿
2. **浏览器缓存**：按 `Cmd + Shift + R` 强制刷新，别只按 F5
3. **构建真的失败了**：去仓库页面的 **Actions** 标签，看有没有红色的失败记录，点开能看到具体报错
4. **Pages 的来源没配对**：Settings → Pages → Source，Chirpy 必须选 **GitHub Actions**，选成「Deploy from a branch」会导致网站不更新

{: .prompt-warning }

> 我这次就是第 4 条：换了 Chirpy 主题之后，网站是由 GitHub Actions 构建的，Pages 来源必须跟着改成 GitHub Actions。

## 记住的结论

- 推送后网站没变 → 先看 **Actions** 页面，红叉就是报错，绿勾就再等等
- 报错 90% 出在某篇文章的开头信息（Front Matter）格式写错了，重点检查 `---` 有没有成对、`date` 格式对不对
