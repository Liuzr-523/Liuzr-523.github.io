# 个人博客站点（Jekyll + GitHub Pages）

## 日常写文章（只需要做这三件事）

1. 在 `_posts/` 下新建文件：`2026-10-01-my-title.md`（日期-英文标题）
2. 文件开头写上：

   ```
   ---
   layout: post
   title: 文章标题
   date: 2026-10-01 10:00:00 +0800
   tags: [标签]
   ---
   ```

3. 用 Markdown 写正文，提交推送，等 1 分钟刷新即可。

## 需要改的地方（只改一次）

| 文件 | 改什么 |
| --- | --- |
| `_config.yml` | 站点标题、描述、作者、邮箱、社交账号 |
| `about/index.md` | 自我介绍正文 |
| `assets/css/style.css` | 顶部 `:root` 里的配色变量 |

## 目录结构

```
_config.yml          站点配置
index.html           首页（最新文章列表）
about/index.md       关于我页面
archive/index.html   归档页（按年份）
_posts/              文章都放这里
_layouts/            页面模板（default / post / page）
_includes/           头部导航、页脚
assets/css/style.css 样式
404.md               404 页面
```

## 本地预览（可选）

装了 Ruby 的话：

```bash
bundle install
bundle exec jekyll serve
# 打开 http://127.0.0.1:4000
```

不装也能用——推到 GitHub 后 GitHub 会自动帮你生成网站。
