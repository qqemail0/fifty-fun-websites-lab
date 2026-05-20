# 50 Fun Websites Lab

50 个功能明显不同的静态互动网站合集，并收录本对话之前生成过的网站链接。

- GitHub Pages: https://qqemail0.github.io/fifty-fun-websites-lab/
- 开源仓库: https://github.com/qqemail0/fifty-fun-websites-lab

## 本次返工重点

上一版过于像同一套模板换文案。本版改成多工具、多版式、多视觉皮肤：

- 50 个网站，至少 38 种不同工具类型。
- 每个子站都有独立交互：转盘、计时器、热力图、矩阵评分、谜题、预算滑杆、文件名重命名器、提示词拼装器、月相日记等。
- 每个子站都有不同视觉皮肤与主题色，不再只有同一种卡片工作台。
- 所有数据保存在浏览器本地，可导出 JSON。

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
node --check assets/site.js
```
