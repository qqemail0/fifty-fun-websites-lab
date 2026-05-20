# 50 Fun Websites Lab

50 个功能完整的静态互动网站合集，并收录本对话之前生成过的网站链接。

- GitHub Pages: https://qqemail0.github.io/fifty-fun-websites-lab/
- 开源仓库: https://github.com/qqemail0/fifty-fun-websites-lab

## 内容

- 50 个新网站，覆盖创作灵感、学习成长、生活计划、情绪疗愈、游戏互动、数据可视、设计美学、社交协作、工具效率、奇想实验。
- 根目录 `index.html` 是总导航页，包含分类、搜索、描述和历史网站链接。
- 每个子站都有独立 URL，并支持搜索、收藏、笔记、任务、评分、灵感生成和 JSON 导出。
- 所有数据存在浏览器本地，不依赖后端服务。

## 本地预览

```bash
python -m http.server 8795
```

打开：

```text
http://127.0.0.1:8795/
```

## 验证

```bash
python tests/verify.py
```
