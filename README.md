# 历史网站导航

这个项目现在只保留本对话之前生成过的网站导航功能，已经删除此前批量生成的 50 个新网站子目录。

- GitHub Pages: https://qqemail0.github.io/fifty-fun-websites-lab/
- 开源仓库: https://github.com/qqemail0/fifty-fun-websites-lab

## 当前功能

- 展示之前生成过的网站链接
- 按分类筛选
- 搜索标题、分类、描述、访问链接和源码地址
- 每个网站展示描述、访问入口和 GitHub 源码入口
- 顶部和底部保留开源项目标注

## 已移除

- `sites/` 目录下的 50 个新生成子网站
- 子站运行脚本 `assets/site.js`
- 50 站批量生成脚本

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
node --check assets/home.js
```
