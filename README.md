# 刘子睿的小站（Jekyll + Chirpy 主题）

主题：[Chirpy](https://github.com/cotes2020/jekyll-theme-chirpy)
网址：https://liuzr-523.github.io

## 日常：发一篇文章

1. 在 `_posts/` 下新建 `年-月-日-英文标题.md`
2. 开头写上：

   ```
   ---
   title: 文章标题
   date: 2026-10-01 10:00:00 +0800
   categories: [课程笔记]
   tags: [标签1, 标签2]
   ---
   ```

3. 用 Markdown 写正文
4. GitHub Desktop：写摘要 → **Commit to main** → **推送 origin**
5. 等 1～3 分钟，网站自动更新（去仓库的 Actions 页面可以看构建进度）

常用分类：`课程笔记` `项目` `踩坑记录` `随想` `教程`

## 想改站点信息

| 想改什么 | 去哪儿改 |
| --- | --- |
| 站点标题、一句话简介、作者名、邮箱 | `_config.yml` 顶部 |
| 头像 | 替换 `assets/img/avatar.jpg`（正方形，建议 400×400 以上） |
| 自我介绍 | `_tabs/about.md` |
| 深浅色模式 | `_config.yml` 里的 `theme_mode`（留空＝跟随系统） |

## 目录说明

```
_config.yml        站点配置
_posts/            文章（文件名必须是 日期-英文标题.md）
_tabs/             左侧导航页：about.md（关于）、archives（归档）、categories（分类）、tags（标签）
assets/img/        图片，头像放这里
.github/workflows/ 自动构建部署流程（不用改）
_data/contact.yml  侧栏联系方式图标
```

## 重要：Pages 的来源必须是 GitHub Actions

Chirpy 由 GitHub Actions 构建，所以仓库 **Settings → Pages → Source** 要选 **GitHub Actions**。
如果选了 "Deploy from a branch"，网站不会更新。

## 本地预览（可选，需要装 Ruby）

```bash
bundle install
bundle exec jekyll serve
# 打开 http://127.0.0.1:4000
```
