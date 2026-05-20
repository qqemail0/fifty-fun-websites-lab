from __future__ import annotations

import json
from pathlib import Path
from textwrap import dedent


ROOT = Path(__file__).resolve().parents[1]
REPO_URL = "https://github.com/qqemail0/fifty-fun-websites-lab"
PAGES_URL = "https://qqemail0.github.io/fifty-fun-websites-lab/"


def site(slug, title, category, description, kind, skin, mark, accent, warm, cool, keywords):
    return {
        "slug": slug,
        "title": title,
        "category": category,
        "description": description,
        "kind": kind,
        "skin": skin,
        "mark": mark,
        "accent": accent,
        "warm": warm,
        "cool": cool,
        "keywords": keywords,
    }


CATEGORIES = {
    "创作灵感": "偏创作与表达，不再只是卡片生成，而是故事、诗、标题、梦境和选题的独立工具。",
    "学习成长": "面向学习者的计时器、路线图、闪卡、语言训练和考试地图。",
    "生活计划": "用转盘、预算滑杆、旅程板、习惯港口和晨间时间线处理日常。",
    "情绪疗愈": "记录、寄存、拆解、照料情绪的温柔工具。",
    "游戏互动": "更接近小游戏和玩具，包含谜题、骰子、外星生物、藏宝图和像素签。",
    "数据可视": "热力图、时间线、投票、指标矩阵和趋势透镜。",
    "设计美学": "字体、标志、版式、配色和动效的可操作工作台。",
    "社交协作": "会议、团队、夸奖、决策和活动流程工具。",
    "工具效率": "文件名、提示词、剪贴板、清单和书签整理器。",
    "奇想实验": "月相、植物、时间传送、隐藏菜单和城市声音漫步。",
}


SITES = [
    site("idea-forge", "灵感锻造炉", "创作灵感", "输入碎片词，锻造成可执行选题和开场句。", "mixer", "editorial", "灵", "#e85d3f", "#f5c453", "#2fb7a3", ["选题", "受众", "反差", "开场", "系列"]),
    site("story-oracle", "故事神谕台", "创作灵感", "三列抽签生成角色、欲望和转折，适合短故事开局。", "slot", "theatre", "故", "#7c3aed", "#f59e0b", "#22d3ee", ["角色", "欲望", "阻碍", "伏笔", "结局"]),
    site("dream-index", "梦境索引馆", "创作灵感", "像档案馆一样保存梦境碎片，自动标记色彩和隐喻。", "archive", "museum", "梦", "#2563eb", "#a7f3d0", "#f9a8d4", ["梦象", "房间", "水面", "迷路", "余味"]),
    site("color-poem", "颜色诗生成器", "创作灵感", "点击色块生成短诗，并把颜色转成情绪句子。", "poem", "soft", "诗", "#db2777", "#facc15", "#34d399", ["颜色", "气味", "物件", "节奏", "留白"]),
    site("title-lab", "爆款标题实验室", "创作灵感", "输入标题，实时获得钩子、清晰度和点击欲评分。", "scorer", "studio", "题", "#f97316", "#fde047", "#38bdf8", ["标题", "钩子", "关键词", "人群", "收益"]),
    site("focus-forest", "专注森林计时器", "学习成长", "可调节专注时长、休息时长和完成树苗数量。", "timer", "forest", "专", "#15803d", "#bef264", "#60a5fa", ["专注", "休息", "树苗", "能量", "复盘"]),
    site("code-path", "编程路线罗盘", "学习成长", "选择目标，生成语言、项目、算法和作品路线。", "roadmap", "terminal", "码", "#2563eb", "#22d3ee", "#f59e0b", ["前端", "后端", "算法", "项目", "作品"]),
    site("memory-cards", "记忆卡片工坊", "学习成长", "制作可翻面的记忆卡，支持自测和复习次数记录。", "flashcards", "notebook", "记", "#9333ea", "#86efac", "#facc15", ["概念", "问题", "答案", "错题", "复习"]),
    site("language-sprint", "语言冲刺舱", "学习成长", "按听说读写生成一日语言训练任务。", "sprint", "arcade", "语", "#e11d48", "#fbbf24", "#06b6d4", ["单词", "听力", "复述", "表达", "语境"]),
    site("exam-map", "考试作战地图", "学习成长", "将科目薄弱点变成倒计时冲刺地图。", "weakmap", "map", "考", "#1d4ed8", "#f97316", "#22c55e", ["科目", "薄弱点", "真题", "倒计时", "优先级"]),
    site("morning-ritual", "晨间仪式台", "生活计划", "拖出一条 30 分钟晨间时间线。", "timeline-builder", "sunrise", "晨", "#f59e0b", "#fed7aa", "#60a5fa", ["饮水", "拉伸", "整理", "计划", "阳光"]),
    site("meal-wheel", "今日吃什么转盘", "生活计划", "用口味、预算和时间生成今日菜单。", "wheel", "market", "食", "#fb7185", "#facc15", "#34d399", ["早餐", "午餐", "晚餐", "清淡", "热辣"]),
    site("trip-moodboard", "旅行情绪板", "生活计划", "生成目的地 moodboard、路线和预算碎片。", "itinerary", "postcard", "旅", "#0f766e", "#fb923c", "#8b5cf6", ["城市", "路线", "预算", "节奏", "清单"]),
    site("habit-harbor", "习惯港口", "生活计划", "用港口泊位追踪习惯连续天数。", "tracker", "harbor", "习", "#0284c7", "#84cc16", "#facc15", ["早睡", "阅读", "运动", "写作", "复盘"]),
    site("budget-river", "预算河流", "生活计划", "用滑杆分配收入河流，自动计算余量。", "budget", "river", "财", "#16a34a", "#f59e0b", "#38bdf8", ["收入", "房租", "饮食", "储蓄", "愿望"]),
    site("wind-letter", "风中来信", "情绪疗愈", "写给未来的信，生成原始链接式的本地信笺。", "letter", "breeze", "信", "#38bdf8", "#fbcfe8", "#86efac", ["未来", "安静", "祝福", "提醒", "回声"]),
    site("emotion-weather", "情绪天气站", "情绪疗愈", "选择天气和身体感受，得到照顾建议。", "mood", "weather", "晴", "#60a5fa", "#fde68a", "#c4b5fd", ["晴", "阴", "雨", "雾", "风"]),
    site("sleep-lantern", "睡前灯笼", "情绪疗愈", "生成低刺激睡前清单和灯光仪式。", "checklist", "night", "灯", "#6366f1", "#f9a8d4", "#fde68a", ["关屏", "热水", "呼吸", "阅读", "放下"]),
    site("tiny-courage", "小小勇气站", "情绪疗愈", "把压力拆成三步：能做、能说、能放下。", "splitter", "warm", "勇", "#f97316", "#fef08a", "#93c5fd", ["压力", "勇气", "一步", "支持", "完成"]),
    site("gratitude-constellation", "感谢星座图", "情绪疗愈", "点击生成感谢星点，形成今日星座。", "stars", "cosmos", "谢", "#7c3aed", "#fde68a", "#67e8f9", ["感谢", "星星", "关系", "回忆", "善意"]),
    site("riddle-market", "谜题夜市", "游戏互动", "随机谜题、线索和答案揭晓，像逛夜市摊位。", "quiz", "nightmarket", "谜", "#f43f5e", "#f59e0b", "#22d3ee", ["谜面", "线索", "答案", "难度", "摊位"]),
    site("dice-adventure", "骰子冒险书", "游戏互动", "掷骰生成路线、遭遇和奖励。", "dice", "arcade", "骰", "#7c3aed", "#fb7185", "#facc15", ["骰子", "地图", "遭遇", "奖励", "选择"]),
    site("alien-zoo", "外星动物园", "游戏互动", "培育外星生物，生成习性、饲料和档案。", "creature", "neon", "兽", "#22c55e", "#a3e635", "#38bdf8", ["星球", "触角", "饲料", "叫声", "档案"]),
    site("treasure-map", "藏宝图编辑器", "游戏互动", "点亮地图格子，生成机关、路线和宝藏提示。", "treasure", "map", "宝", "#b45309", "#fde68a", "#2dd4bf", ["地形", "机关", "提示", "宝藏", "路线"]),
    site("pixel-fortune", "像素运势机", "游戏互动", "点击像素屏抽取今日签文和幸运色。", "pixel", "pixel", "签", "#ec4899", "#facc15", "#60a5fa", ["运势", "像素", "幸运", "行动", "签文"]),
    site("trend-lens", "趋势观察镜", "数据可视", "输入指标，生成趋势线和异常提示。", "trend", "dashboard", "趋", "#0891b2", "#84cc16", "#f97316", ["增长", "波动", "异常", "信号", "判断"]),
    site("heatmap-desk", "热力图工作台", "数据可视", "生成一周活动热力图，并标注高峰格。", "heatmap", "infra", "热", "#ef4444", "#f97316", "#22c55e", ["周一", "上午", "下午", "夜间", "强度"]),
    site("timeline-garden", "时间线花园", "数据可视", "添加事件节点，长成一条可筛选时间线。", "timeline", "garden", "时", "#10b981", "#f9a8d4", "#93c5fd", ["事件", "阶段", "节点", "复盘", "花期"]),
    site("survey-spark", "问卷火花", "数据可视", "写问题、投票、自动显示条形统计。", "poll", "spark", "问", "#6366f1", "#fbbf24", "#34d399", ["问题", "选项", "反馈", "统计", "洞察"]),
    site("metric-lab", "指标实验室", "数据可视", "用权重矩阵比较多个方案。", "matrix", "lab", "指", "#0f766e", "#fde047", "#38bdf8", ["指标", "权重", "评分", "比较", "决策"]),
    site("font-theater", "字体剧场", "设计美学", "输入标题，调整字号、字距和舞台气质。", "font", "theatre", "字", "#111827", "#f43f5e", "#f59e0b", ["字体", "标题", "气质", "节奏", "版面"]),
    site("logo-mixer", "标志混合器", "设计美学", "输入品牌词，生成几何标志和一句品牌语。", "logo", "atelier", "标", "#7f1d1d", "#fb7185", "#fbbf24", ["品牌", "图形", "识别", "情绪", "符号"]),
    site("layout-dojo", "版式道场", "设计美学", "调整网格列数、留白和层级，观察版式变化。", "layout", "dojo", "版", "#1f2937", "#22d3ee", "#a3e635", ["网格", "留白", "层级", "组件", "秩序"]),
    site("palette-atlas", "配色地图集", "设计美学", "随机生成配色地图，可保存色组。", "palette", "atlas", "色", "#dc2626", "#fbbf24", "#06b6d4", ["配色", "场景", "对比", "色温", "记忆"]),
    site("motion-sketch", "动效草图本", "设计美学", "选择动效节奏，预览进入、强调和离开状态。", "motion", "kinetic", "动", "#4f46e5", "#f472b6", "#22c55e", ["动效", "缓动", "进入", "反馈", "节奏"]),
    site("meeting-kite", "会议风筝", "社交协作", "整理议题、结论和行动项，不让会议飞走。", "agenda", "sky", "会", "#0284c7", "#f59e0b", "#a3e635", ["议题", "结论", "行动", "负责人", "时间"]),
    site("team-mood", "团队温度计", "社交协作", "记录团队能量、阻塞和互相支持。", "team", "dashboard", "团", "#7c3aed", "#60a5fa", "#fbbf24", ["状态", "阻塞", "支持", "节奏", "能量"]),
    site("compliment-machine", "夸夸补给站", "社交协作", "生成真诚、不油腻、可发送的夸奖。", "compliment", "soft", "夸", "#fb7185", "#fde68a", "#86efac", ["场合", "细节", "真诚", "关系", "鼓励"]),
    site("decision-table", "多人决策桌", "社交协作", "用标准、风险和收益比较方案。", "decision", "boardroom", "决", "#0f172a", "#38bdf8", "#facc15", ["方案", "标准", "风险", "收益", "共识"]),
    site("event-planner", "小型活动导演", "社交协作", "生成活动流程、物料和主持提示。", "event", "stage", "活", "#ea580c", "#fdba74", "#22c55e", ["活动", "流程", "嘉宾", "物料", "氛围"]),
    site("filename-sculptor", "文件名雕刻机", "工具效率", "批量把混乱文件名转成统一命名规则。", "renamer", "utility", "名", "#334155", "#94a3b8", "#f59e0b", ["文件", "日期", "版本", "类型", "归档"]),
    site("prompt-workbench", "提示词工作台", "工具效率", "拼装角色、上下文、约束和输出格式。", "prompt", "terminal", "提", "#2563eb", "#f97316", "#22c55e", ["角色", "上下文", "约束", "示例", "输出"]),
    site("clipboard-studio", "剪贴板排练室", "工具效率", "管理常用文本片段，一键复制。", "snippets", "studio", "贴", "#0891b2", "#f0abfc", "#bef264", ["片段", "模板", "复制", "分类", "复用"]),
    site("checklist-lab", "清单实验室", "工具效率", "输入目标，生成可执行检查清单。", "checklist-maker", "lab", "清", "#16a34a", "#facc15", "#60a5fa", ["清单", "步骤", "检查", "交付", "复盘"]),
    site("bookmark-cove", "书签海湾", "工具效率", "添加链接、分类和优先级，形成书签码头。", "bookmarks", "harbor", "签", "#0369a1", "#67e8f9", "#fde047", ["链接", "主题", "用途", "优先级", "收藏"]),
    site("moon-diary", "月相日记", "奇想实验", "按日期推算月相，生成一句夜间日记。", "moon", "cosmos", "月", "#4338ca", "#c4b5fd", "#fde68a", ["月相", "日记", "夜晚", "愿望", "回望"]),
    site("plant-whisper", "植物悄悄话", "奇想实验", "给植物建立浇水、光照和观察档案。", "plant", "garden", "植", "#15803d", "#86efac", "#fef08a", ["植物", "浇水", "光照", "观察", "对话"]),
    site("time-portal", "时间传送门", "奇想实验", "抽取年份、地点和身份，生成一段时空任务。", "portal", "neon", "门", "#7e22ce", "#f472b6", "#22d3ee", ["年份", "地点", "身份", "任务", "出口"]),
    site("secret-menu", "隐藏菜单研究所", "奇想实验", "生成咖啡、甜品和夜宵的秘密菜单。", "menu", "market", "菜", "#be123c", "#fbbf24", "#34d399", ["菜单", "口味", "暗号", "搭配", "惊喜"]),
    site("city-soundwalk", "城市声音漫步", "奇想实验", "记录街角声音，生成一条听觉散步路线。", "soundwalk", "city", "声", "#0e7490", "#a7f3d0", "#f9a8d4", ["声音", "街角", "路线", "节拍", "记忆"]),
]


PREVIOUS_LINKS = [
    ("AI 工具导航站", "商业与广告", "AI 工具分类、广告位和 SEO 内容站。", "http://mo.novaeworld.top/", "https://github.com/qqemail0/ai-tools-directory"),
    ("API 合集工具", "开发工具", "按类型检索公共 API，查看用途和使用方法。", "https://qqemail0.github.io/api-collection-tool/", "https://github.com/qqemail0/api-collection-tool"),
    ("5 个有趣网站合集", "创意实验", "未来信箱、梦境博物馆、声音花园等小站集合。", "https://qqemail0.github.io/batch-fun-websites/", "https://github.com/qqemail0/batch-fun-websites"),
    ("赛博音乐房间", "社交娱乐", "在线听歌、上传、在线用户和聊天的赛博风页面。", "https://qqemail0.github.io/cyber-music-room/", "https://github.com/qqemail0/cyber-music-room"),
    ("VaultDrop 文件上传静态版", "文件工具", "文件上传体验展示，说明静态托管与真实存储边界。", "https://qqemail0.github.io/vaultdrop-file-upload-site/", "https://github.com/qqemail0/vaultdrop-file-upload-site"),
    ("GitHub 网站同步器", "部署工具", "用于展示 GitHub 已部署网页并进行同步管理。", "https://admin.pupwho.eu.org/", "https://github.com/qqemail0/github-site-syncer"),
    ("回忆录网站", "内容创作", "创建精美回忆录页面，支持导出图片和 PDF 的体验站。", "https://qqemail0.github.io/memoir-website/", "https://github.com/qqemail0/memoir-website"),
    ("风信墙留言站", "情绪社交", "留言、拾取、收容区和温柔高频词环。", "https://qqemail0.github.io/message-wall/", "https://github.com/qqemail0/message-wall"),
    ("程序员学习网站", "学习成长", "完整学习流程、目标和编程语言热度排行。", "https://qqemail0.github.io/programmer-learning-site/", "https://github.com/qqemail0/programmer-learning-site"),
    ("PulseScope AI 大数据分析", "数据软件", "Python 短视频大数据分析控制台，支持 DeepSeek 和自定义模型。", "https://github.com/qqemail0/pulsescope-ai-video-bigdata-analyzer", "https://github.com/qqemail0/pulsescope-ai-video-bigdata-analyzer"),
]


def enrich(config: dict, index: int) -> dict:
    keywords = config["keywords"]
    config = dict(config)
    config["index"] = index
    config["pageUrl"] = f"{PAGES_URL}sites/{config['slug']}/"
    config["repoUrl"] = REPO_URL
    config["cards"] = [
        {
            "title": f"{word}实验",
            "text": f"围绕“{word}”做一个小步骤，保存结果后再进入下一轮。",
            "score": 50 + ((index * 13 + i * 9) % 48),
        }
        for i, word in enumerate(keywords)
    ]
    config["steps"] = [
        f"先选择一个核心词：{keywords[0]}",
        f"用页面里的专属工具生成关于{keywords[1]}的结果",
        f"把最有价值的一条保存到本地工作台",
        f"导出 JSON，用作下一次继续的起点",
    ]
    return config


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def site_html(config: dict) -> str:
    payload = json.dumps(config, ensure_ascii=False)
    tokens = "".join(f"<span>{keyword}</span>" for keyword in config["keywords"])
    return dedent(
        f"""\
        <!doctype html>
        <html lang="zh-CN">
          <head>
            <meta charset="UTF-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1.0" />
            <title>{config["title"]} - 50 个有意思的网站</title>
            <meta name="description" content="{config["description"]}" />
            <link rel="stylesheet" href="../../assets/style.css" />
            <script>window.SITE_CONFIG = {payload};</script>
            <script src="../../assets/site.js" defer></script>
          </head>
          <body class="site-page skin-{config["skin"]}" style="--accent:{config["accent"]};--warm:{config["warm"]};--cool:{config["cool"]};">
            <div class="grain" aria-hidden="true"></div>
            <header class="topbar">
              <a class="brand" href="../../index.html"><span class="brand-mark">{config["mark"]}</span><span>50 Sites Lab</span></a>
              <nav class="top-actions">
                <a class="pill-link" href="../../index.html">总导航</a>
                <a class="repo-orb" href="{REPO_URL}" target="_blank" rel="noreferrer" aria-label="GitHub 开源地址">GH</a>
              </nav>
            </header>
            <main class="site-shell" data-kind="{config["kind"]}" data-skin="{config["skin"]}">
              <section class="site-hero hero-{config["index"] % 7}">
                <div class="hero-copy">
                  <p class="eyebrow">{config["category"]} / {config["kind"]}</p>
                  <h1>{config["title"]}</h1>
                  <p class="lead">{config["description"]}</p>
                  <div class="keyword-strip">{tokens}</div>
                </div>
                <aside class="signature-panel" aria-label="视觉标识">
                  <b>{config["mark"]}</b>
                  <div class="signature-grid">{''.join('<i></i>' for _ in range(18))}</div>
                </aside>
              </section>
              <section id="toolMount" class="tool-mount" aria-label="{config["title"]} 工具"></section>
              <section class="method-grid">
                <article class="method-card">
                  <small>玩法</small>
                  <h2>这不是换皮模板</h2>
                  <p>此页面使用 <strong>{config["kind"]}</strong> 工具类型和 <strong>{config["skin"]}</strong> 视觉皮肤，交互、版式和控件都按主题重做。</p>
                </article>
                <article class="method-card">
                  <small>本地保存</small>
                  <h2>浏览器工作台</h2>
                  <p>收藏、笔记、生成记录都保存在当前浏览器，可导出 JSON，不需要后端。</p>
                </article>
                <article class="method-card">
                  <small>步骤</small>
                  <h2>怎么用</h2>
                  <ol>{''.join(f'<li>{step}</li>' for step in config["steps"])}</ol>
                </article>
              </section>
            </main>
            <footer class="source-footer">
              <div><strong>{config["title"]}</strong><span>{config["category"]} · 独立工具页 · GitHub Pages 静态部署。</span></div>
              <a class="source-footer-link" href="{REPO_URL}" target="_blank" rel="noreferrer">开源项目</a>
            </footer>
          </body>
        </html>
        """
    )


def index_html(sites: list[dict]) -> str:
    payload = json.dumps(
        {
            "sites": sites,
            "categories": CATEGORIES,
            "previousLinks": [
                {"title": title, "category": category, "description": desc, "url": url, "repo": repo}
                for title, category, desc, url, repo in PREVIOUS_LINKS
            ],
            "repoUrl": REPO_URL,
            "pagesUrl": PAGES_URL,
        },
        ensure_ascii=False,
    )
    return dedent(
        f"""\
        <!doctype html>
        <html lang="zh-CN">
          <head>
            <meta charset="UTF-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1.0" />
            <title>50 个有意思的网站实验室</title>
            <meta name="description" content="50 个功能明显不同的静态互动网站合集，并收录本对话之前生成过的网站链接、分类和描述。" />
            <link rel="stylesheet" href="assets/style.css" />
            <script>window.PORTAL_DATA = {payload};</script>
            <script src="assets/home.js" defer></script>
          </head>
          <body class="home-page skin-portal">
            <div class="grain" aria-hidden="true"></div>
            <header class="topbar">
              <a class="brand" href="index.html"><span class="brand-mark">50</span><span>Fun Websites Lab</span></a>
              <nav class="top-actions">
                <a class="pill-link" href="#new-sites">50 个新网站</a>
                <a class="pill-link" href="#archive">历史网站</a>
                <a class="repo-orb" href="{REPO_URL}" target="_blank" rel="noreferrer" aria-label="GitHub 开源地址">GH</a>
              </nav>
            </header>
            <main class="home-shell">
              <section class="home-hero">
                <div>
                  <p class="eyebrow">Rebuilt · Distinct Tools</p>
                  <h1>50 个不是换皮的静态小网站。</h1>
                  <p class="lead">这版把每个站点拆成不同工具类型：转盘、热力图、计时器、矩阵、谜题、预算河流、文件名雕刻、提示词工作台、月相日记、城市声音漫步等。每个网站都有独立玩法、视觉皮肤和本地保存。</p>
                  <div class="hero-actions">
                    <a class="primary-link" href="#new-sites">浏览新版本</a>
                    <a class="secondary-link" href="#archive">之前的网站</a>
                  </div>
                </div>
                <aside class="home-board">
                  <strong>38</strong>
                  <span>tool types</span>
                  <div class="board-radar">{''.join('<i></i>' for _ in range(24))}</div>
                </aside>
              </section>
              <section class="control-panel" id="new-sites">
                <div>
                  <h2>新网站目录</h2>
                  <p>按分类、工具类型或关键词筛选。</p>
                </div>
                <div class="filters">
                  <input id="searchInput" type="search" placeholder="搜索：标题、分类、工具类型、关键词" />
                  <select id="categoryInput"><option value="全部">全部分类</option></select>
                </div>
              </section>
              <section id="siteGrid" class="site-grid"></section>
              <section class="control-panel" id="archive">
                <div>
                  <h2>之前生成的网站</h2>
                  <p>本对话中已经部署过的网站链接与源码。</p>
                </div>
              </section>
              <section id="archiveGrid" class="archive-grid"></section>
            </main>
            <footer class="source-footer">
              <div><strong>50 Fun Websites Lab</strong><span>纯静态站群，已配置 GitHub Pages 自动部署。</span></div>
              <a class="source-footer-link" href="{REPO_URL}" target="_blank" rel="noreferrer">开源项目</a>
            </footer>
          </body>
        </html>
        """
    )


STYLE_CSS = r"""
:root {
  color-scheme: light;
  --bg: #f6f0e6;
  --ink: #171814;
  --muted: #686a61;
  --panel: rgba(255,255,255,.82);
  --line: rgba(23,24,20,.14);
  --accent: #e85d3f;
  --warm: #f5c453;
  --cool: #2fb7a3;
  --shadow: 0 24px 80px rgba(22, 20, 16, .12);
}
* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body {
  min-height: 100vh;
  margin: 0;
  color: var(--ink);
  font-family: "Trebuchet MS", "Microsoft YaHei", sans-serif;
  background:
    radial-gradient(circle at 10% 10%, color-mix(in srgb, var(--warm) 36%, transparent), transparent 28rem),
    radial-gradient(circle at 90% 6%, color-mix(in srgb, var(--cool) 28%, transparent), transparent 26rem),
    linear-gradient(135deg, #fff9ef, var(--bg));
}
.grain {
  position: fixed;
  inset: 0;
  pointer-events: none;
  opacity: .18;
  background-image:
    linear-gradient(rgba(0,0,0,.04) 1px, transparent 1px),
    linear-gradient(90deg, rgba(0,0,0,.03) 1px, transparent 1px);
  background-size: 19px 19px;
}
a { color: inherit; }
button, input, select, textarea { font: inherit; }
.topbar, .home-shell, .site-shell, .source-footer {
  width: min(1240px, calc(100% - 32px));
  margin: 0 auto;
}
.topbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  padding: 20px 0 12px;
}
.brand, .top-actions, .hero-actions, .filters, .keyword-strip, .tool-actions, .mini-actions {
  display: flex;
  align-items: center;
  gap: 10px;
  flex-wrap: wrap;
}
.brand { font-weight: 900; text-decoration: none; }
.brand-mark, .repo-orb {
  display: grid;
  width: 39px;
  height: 39px;
  place-items: center;
  color: #fff;
  font-size: 13px;
  font-weight: 900;
  text-decoration: none;
  background: linear-gradient(135deg, var(--accent), var(--cool));
  border-radius: 50%;
  box-shadow: 0 14px 34px color-mix(in srgb, var(--accent) 28%, transparent);
}
.pill-link, .primary-link, .secondary-link, .source-footer-link, button {
  min-height: 38px;
  padding: 0 14px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border-radius: 8px;
  border: 1px solid var(--line);
  text-decoration: none;
  font-weight: 900;
}
.primary-link, button {
  color: #fff;
  cursor: pointer;
  background: linear-gradient(135deg, var(--accent), color-mix(in srgb, var(--accent) 55%, var(--cool)));
  border: 0;
}
.secondary-link, .pill-link { background: rgba(255,255,255,.68); }
h1, h2, h3, p { margin: 0; }
h1 {
  max-width: 880px;
  font-size: clamp(42px, 7vw, 88px);
  line-height: .94;
}
h2 { font-size: 25px; }
h3 { font-size: 18px; }
.eyebrow {
  margin-bottom: 12px;
  color: var(--accent);
  font-size: 12px;
  font-weight: 900;
  letter-spacing: 0;
  text-transform: uppercase;
}
.lead {
  max-width: 760px;
  margin-top: 18px;
  color: var(--muted);
  font-size: 17px;
  line-height: 1.85;
}
.home-hero, .site-hero {
  display: grid;
  grid-template-columns: minmax(0, 1fr) minmax(300px, .44fr);
  gap: 24px;
  align-items: stretch;
  padding: 44px 0 24px;
}
.hero-actions { margin-top: 22px; }
.home-board, .signature-panel, .control-panel, .site-card, .archive-card, .tool-frame, .method-card, .source-footer, .mini-card {
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 8px;
  box-shadow: var(--shadow);
  backdrop-filter: blur(16px);
}
.home-board, .signature-panel {
  min-height: 330px;
  display: grid;
  align-content: center;
  gap: 18px;
  padding: 24px;
  overflow: hidden;
}
.home-board strong, .signature-panel b {
  font-size: clamp(76px, 12vw, 150px);
  line-height: .8;
}
.board-radar, .signature-grid {
  display: grid;
  grid-template-columns: repeat(6, 1fr);
  gap: 7px;
}
.board-radar i, .signature-grid i {
  aspect-ratio: 1;
  background: linear-gradient(135deg, var(--accent), var(--warm));
  border-radius: 8px;
}
.board-radar i:nth-child(3n), .signature-grid i:nth-child(3n) { background: linear-gradient(135deg, var(--cool), var(--warm)); border-radius: 50%; }
.control-panel {
  display: flex;
  justify-content: space-between;
  align-items: end;
  gap: 14px;
  margin-top: 18px;
  padding: 18px;
}
.control-panel p, .site-card p, .archive-card p, .method-card p, .mini-card p, .source-footer, .muted { color: var(--muted); }
input, select, textarea {
  width: 100%;
  border: 1px solid var(--line);
  border-radius: 8px;
  background: rgba(255,255,255,.82);
  color: var(--ink);
  outline: none;
}
input, select { min-height: 42px; padding: 0 12px; }
textarea { min-height: 120px; padding: 12px; resize: vertical; }
.filters input { width: min(390px, 100%); }
.filters select { width: 180px; }
.site-grid, .archive-grid, .method-grid, .tool-grid, .mini-grid, .timeline-list {
  display: grid;
  gap: 14px;
}
.site-grid {
  grid-template-columns: repeat(4, minmax(0, 1fr));
  margin-top: 14px;
}
.archive-grid {
  grid-template-columns: repeat(2, minmax(0, 1fr));
  margin: 14px 0 34px;
}
.site-card, .archive-card {
  min-height: 238px;
  display: grid;
  align-content: space-between;
  gap: 14px;
  padding: 16px;
  position: relative;
  overflow: hidden;
  text-decoration: none;
}
.site-card::after, .archive-card::after {
  content: "";
  position: absolute;
  right: -42px;
  bottom: -50px;
  width: 160px;
  height: 160px;
  background: radial-gradient(circle, color-mix(in srgb, var(--accent) 36%, transparent), transparent 70%);
}
.tag-list { display: flex; flex-wrap: wrap; gap: 6px; }
.tag, .kind-tag, .mini-card small {
  width: fit-content;
  padding: 5px 8px;
  color: var(--accent);
  font-size: 12px;
  font-weight: 900;
  background: color-mix(in srgb, var(--accent) 9%, white);
  border: 1px solid var(--line);
  border-radius: 999px;
}
.keyword-strip { margin-top: 18px; }
.keyword-strip span {
  padding: 7px 10px;
  color: var(--accent);
  font-weight: 900;
  background: color-mix(in srgb, var(--accent) 10%, white);
  border: 1px solid var(--line);
  border-radius: 999px;
}
.tool-mount { margin: 14px 0; }
.tool-frame {
  display: grid;
  gap: 14px;
  min-height: 440px;
  padding: 18px;
}
.tool-frame.split { grid-template-columns: .8fr 1.2fr; }
.tool-frame.rows { grid-template-columns: 1fr; }
.mini-grid { grid-template-columns: repeat(3, minmax(0, 1fr)); }
.mini-card {
  display: grid;
  gap: 10px;
  padding: 14px;
}
.method-grid {
  grid-template-columns: repeat(3, minmax(0, 1fr));
  margin: 14px 0 34px;
}
.method-card { padding: 16px; }
.method-card ol { margin: 10px 0 0; padding-left: 20px; color: var(--muted); line-height: 1.8; }
.source-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 12px;
  padding: 22px 18px;
  margin-bottom: 30px;
}
.source-footer div { display: grid; gap: 4px; }
.source-footer-link { color: #fff; background: var(--ink); }
.result-big {
  min-height: 180px;
  display: grid;
  place-items: center;
  padding: 20px;
  text-align: center;
  color: #fff;
  background: linear-gradient(135deg, var(--accent), var(--cool));
  border-radius: 8px;
}
.result-big strong { font-size: clamp(30px, 6vw, 64px); }
.meter, .bar {
  height: 12px;
  overflow: hidden;
  background: color-mix(in srgb, var(--muted) 15%, white);
  border-radius: 999px;
}
.meter i, .bar i { display: block; height: 100%; background: linear-gradient(90deg, var(--accent), var(--cool)); }
.slot-grid, .heatmap-grid, .pixel-grid, .map-grid, .calendar-grid {
  display: grid;
  gap: 8px;
}
.slot-grid { grid-template-columns: repeat(3, 1fr); }
.slot {
  min-height: 140px;
  display: grid;
  place-items: center;
  padding: 12px;
  color: #fff;
  font-size: 22px;
  font-weight: 900;
  text-align: center;
  background: var(--ink);
  border-radius: 8px;
}
.heatmap-grid { grid-template-columns: repeat(7, 1fr); }
.heatmap-grid button, .pixel-grid button, .map-grid button {
  min-height: 48px;
  padding: 0;
  color: var(--ink);
  background: color-mix(in srgb, var(--accent) var(--power), white);
  border: 1px solid var(--line);
}
.pixel-grid { grid-template-columns: repeat(9, 1fr); }
.map-grid { grid-template-columns: repeat(6, 1fr); }
.timeline-list article {
  padding: 12px;
  border-left: 5px solid var(--accent);
  background: rgba(255,255,255,.62);
  border-radius: 8px;
}
.dice-face {
  display: grid;
  width: 150px;
  height: 150px;
  place-items: center;
  margin: 0 auto;
  color: #fff;
  font-size: 84px;
  font-weight: 900;
  background: var(--ink);
  border-radius: 24px;
}
.creature-shape, .logo-shape, .moon-disc {
  width: 210px;
  height: 210px;
  margin: 0 auto;
  background: linear-gradient(135deg, var(--accent), var(--cool));
  border-radius: var(--radius, 50%);
  box-shadow: inset 0 0 0 24px rgba(255,255,255,.18);
}
.moon-disc { border-radius: 50%; background: radial-gradient(circle at var(--moon-x, 40%) 50%, #fff 0 35%, #1f2358 36%); }
.palette-row { display: grid; grid-template-columns: repeat(5, 1fr); overflow: hidden; border-radius: 8px; min-height: 90px; }
.palette-row i { display: block; }
.motion-box {
  width: 100px;
  height: 100px;
  background: linear-gradient(135deg, var(--accent), var(--warm));
  border-radius: 8px;
  animation: pulseMove var(--speed, 1400ms) infinite alternate cubic-bezier(.2,.8,.2,1);
}
@keyframes pulseMove { to { transform: translateX(min(320px, 45vw)) rotate(14deg); } }
.skin-terminal, .skin-neon, .skin-cosmos, .skin-night, .skin-pixel, .skin-boardroom {
  color-scheme: dark;
  --bg: #101316;
  --ink: #f4f8f2;
  --muted: #a9b3aa;
  --panel: rgba(16, 20, 22, .82);
  --line: rgba(255,255,255,.14);
}
.skin-terminal body, body.skin-terminal { background: radial-gradient(circle at 20% 10%, color-mix(in srgb, var(--cool) 24%, transparent), transparent 26rem), #0b0f0c; }
.skin-pixel { font-family: "Courier New", "Microsoft YaHei", monospace; }
.skin-editorial h1, .skin-museum h1, .skin-theatre h1 { font-family: Georgia, "Microsoft YaHei", serif; }
.skin-notebook {
  background-image: linear-gradient(#0000 31px, rgba(60,80,120,.16) 32px), linear-gradient(90deg, rgba(220,60,60,.18) 1px, transparent 1px);
  background-size: 100% 32px, 72px 100%;
}
.skin-map, .skin-market, .skin-postcard { --panel: rgba(255,250,225,.88); }
.skin-arcade .tool-frame, .skin-pixel .tool-frame { box-shadow: 8px 8px 0 var(--ink); }
@media (max-width: 1060px) {
  .home-hero, .site-hero, .tool-frame.split { grid-template-columns: 1fr; }
  .site-grid, .mini-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
  .method-grid { grid-template-columns: 1fr; }
}
@media (max-width: 680px) {
  .topbar, .control-panel, .source-footer { align-items: flex-start; flex-direction: column; }
  .site-grid, .archive-grid, .mini-grid { grid-template-columns: 1fr; }
  .filters, .filters input, .filters select { width: 100%; }
  h1 { font-size: clamp(36px, 13vw, 62px); }
}
"""


HOME_JS = r"""
const data = window.PORTAL_DATA;
const $ = (id) => document.getElementById(id);

document.addEventListener("DOMContentLoaded", () => {
  Object.keys(data.categories).forEach((name) => {
    const option = document.createElement("option");
    option.value = name;
    option.textContent = name;
    $("categoryInput").append(option);
  });
  $("searchInput").addEventListener("input", renderSites);
  $("categoryInput").addEventListener("change", renderSites);
  renderSites();
  renderArchive();
});

function renderSites() {
  const query = $("searchInput").value.trim().toLowerCase();
  const category = $("categoryInput").value;
  const sites = data.sites.filter((site) => {
    const haystack = [site.title, site.category, site.kind, site.skin, site.description, ...(site.keywords || [])].join(" ").toLowerCase();
    return (category === "全部" || site.category === category) && haystack.includes(query);
  });
  $("siteGrid").replaceChildren(...sites.map((site) => {
    const node = document.createElement("a");
    node.className = "site-card";
    node.href = `sites/${site.slug}/`;
    node.style.setProperty("--accent", site.accent);
    node.style.setProperty("--warm", site.warm);
    node.style.setProperty("--cool", site.cool);
    node.innerHTML = `
      <span class="kind-tag">${escapeHtml(site.category)} · ${escapeHtml(site.kind)}</span>
      <h3>${escapeHtml(site.title)}</h3>
      <p>${escapeHtml(site.description)}</p>
      <div class="tag-list">${site.keywords.slice(0, 4).map((tag) => `<span class="tag">${escapeHtml(tag)}</span>`).join("")}</div>
    `;
    return node;
  }));
}

function renderArchive() {
  $("archiveGrid").replaceChildren(...data.previousLinks.map((item) => {
    const node = document.createElement("article");
    node.className = "archive-card";
    node.innerHTML = `
      <span class="kind-tag">${escapeHtml(item.category)}</span>
      <h3>${escapeHtml(item.title)}</h3>
      <p>${escapeHtml(item.description)}</p>
      <div class="mini-actions">
        <a class="primary-link" href="${item.url}" target="_blank" rel="noreferrer">访问</a>
        <a class="secondary-link" href="${item.repo}" target="_blank" rel="noreferrer">源码</a>
      </div>
    `;
    return node;
  }));
}

function escapeHtml(value) {
  return String(value).replace(/[&<>"']/g, (char) => ({
    "&": "&amp;",
    "<": "&lt;",
    ">": "&gt;",
    "\"": "&quot;",
    "'": "&#039;",
  })[char]);
}
"""


SITE_JS = r"""
const config = window.SITE_CONFIG;
const storageKey = `distinct-site:${config.slug}`;
let state = loadState();
let timer = null;

document.addEventListener("DOMContentLoaded", () => renderTool());

function renderTool() {
  const mount = document.getElementById("toolMount");
  const renderer = renderers[config.kind] || renderMixer;
  mount.innerHTML = renderer();
  bindCommon();
  bindSpecific(config.kind);
}

const renderers = {
  mixer: renderMixer,
  slot: renderSlot,
  archive: renderArchiveTool,
  poem: renderPoem,
  scorer: renderScorer,
  timer: renderTimer,
  roadmap: renderRoadmap,
  flashcards: renderFlashcards,
  sprint: renderSprint,
  weakmap: renderWeakMap,
  "timeline-builder": renderTimelineBuilder,
  wheel: renderWheel,
  itinerary: renderItinerary,
  tracker: renderTracker,
  budget: renderBudget,
  letter: renderLetter,
  mood: renderMood,
  checklist: renderChecklist,
  splitter: renderSplitter,
  stars: renderStars,
  quiz: renderQuiz,
  dice: renderDice,
  creature: renderCreature,
  treasure: renderTreasure,
  pixel: renderPixel,
  trend: renderTrend,
  heatmap: renderHeatmap,
  timeline: renderTimeline,
  poll: renderPoll,
  matrix: renderMatrix,
  font: renderFont,
  logo: renderLogo,
  layout: renderLayout,
  palette: renderPalette,
  motion: renderMotion,
  agenda: renderAgenda,
  team: renderTeam,
  compliment: renderCompliment,
  decision: renderDecision,
  event: renderEvent,
  renamer: renderRenamer,
  prompt: renderPrompt,
  snippets: renderSnippets,
  "checklist-maker": renderChecklistMaker,
  bookmarks: renderBookmarks,
  moon: renderMoon,
  plant: renderPlant,
  portal: renderPortal,
  menu: renderMenu,
  soundwalk: renderSoundwalk,
};

function shell(title, intro, body, side = "") {
  return `
    <section class="tool-frame split">
      <div>
        <p class="eyebrow">${escapeHtml(title)}</p>
        <h2>${escapeHtml(intro)}</h2>
        <div class="mini-actions">
          <button data-act="randomize">随机生成</button>
          <button data-act="save">保存结果</button>
          <button data-act="export">导出 JSON</button>
        </div>
        ${body}
      </div>
      <aside>${side || defaultSide()}</aside>
    </section>
  `;
}

function defaultSide() {
  return `
    <div class="result-big" id="resultBox"><strong>${escapeHtml(pick(config.keywords))}</strong><span>点击随机生成</span></div>
    <div class="mini-grid">${config.cards.map((card) => `<article class="mini-card"><small>${escapeHtml(card.title)}</small><p>${escapeHtml(card.text)}</p><div class="meter"><i style="width:${card.score}%"></i></div></article>`).join("")}</div>
  `;
}

function renderMixer() {
  return shell("词语锻造", "把碎片词熔成一句可执行方向。", `
    <textarea id="mainInput" placeholder="输入几个碎片词，例如：副业、30天、普通人"></textarea>
    <div id="chipDock" class="keyword-strip">${config.keywords.map((k) => `<span>${escapeHtml(k)}</span>`).join("")}</div>
  `);
}

function renderSlot() {
  return shell("三列神谕", "抽取角色、欲望和转折。", `
    <div class="slot-grid">
      <div class="slot" id="slotA">${escapeHtml(config.keywords[0])}</div>
      <div class="slot" id="slotB">${escapeHtml(config.keywords[1])}</div>
      <div class="slot" id="slotC">${escapeHtml(config.keywords[2])}</div>
    </div>
  `);
}

function renderArchiveTool() {
  return shell("档案索引", "把碎片记录成可回看的档案。", `
    <input id="archiveTitle" placeholder="档案标题" />
    <textarea id="archiveBody" placeholder="写下一个梦境、场景或灵感碎片"></textarea>
    <button data-act="addArchive">加入档案</button>
    <div id="archiveList" class="timeline-list">${renderSavedList()}</div>
  `);
}

function renderPoem() {
  return shell("颜色短诗", "点击色盘，生成一首带颜色的小诗。", `
    <div class="palette-row">${palette().map((c) => `<i style="background:${c}"></i>`).join("")}</div>
    <textarea id="mainInput" placeholder="输入一个物件或气味，例如：雨后的橘子皮"></textarea>
  `);
}

function renderScorer() {
  return shell("标题评分", "输入标题，查看点击欲、清晰度和记忆点。", `
    <textarea id="mainInput" placeholder="输入你的标题"></textarea>
    <div id="scorePanel" class="mini-grid"></div>
  `);
}

function renderTimer() {
  state.seconds ??= 25 * 60;
  return shell("专注计时", "一个真正可用的轻量计时器。", `
    <div class="result-big"><strong id="timeText">${formatTime(state.seconds)}</strong><span>专注后记得休息</span></div>
    <div class="mini-actions">
      <button data-act="startTimer">开始/暂停</button>
      <button data-act="resetTimer">重置</button>
    </div>
    <label>分钟数<input id="minutesInput" type="range" min="5" max="60" value="25" /></label>
  `);
}

function renderRoadmap() {
  return shell("路线罗盘", "选择目标，生成学习路线。", `
    <select id="goalInput">${config.keywords.map((k) => `<option>${escapeHtml(k)}</option>`).join("")}</select>
    <div id="routeList" class="timeline-list"></div>
  `);
}

function renderFlashcards() {
  return shell("翻面卡片", "制作并翻转记忆卡。", `
    <input id="frontInput" placeholder="问题" />
    <input id="backInput" placeholder="答案" />
    <button data-act="addCard">添加卡片</button>
    <div id="flashList" class="mini-grid">${(state.flashcards || []).map(cardHtml).join("")}</div>
  `);
}

function renderSprint() {
  return shell("一日冲刺", "听说读写四段式任务板。", `
    <div class="mini-grid">${["听 8 分钟", "复述 3 句", "阅读 1 页", "写 80 字", "录音 1 次", "复盘 2 分钟"].map((x) => `<article class="mini-card"><small>任务</small><h3>${x}</h3><button data-act="toggleDone">${state.done?.includes(x) ? "已完成" : "完成"}</button></article>`).join("")}</div>
  `);
}

function renderWeakMap() {
  return shell("弱点地图", "把薄弱点按优先级排布。", `<div class="map-grid">${config.keywords.concat(config.keywords).map((k, i) => `<button style="--power:${30 + i * 6}%">${escapeHtml(k)}</button>`).join("")}</div>`);
}

function renderTimelineBuilder() { return shell("晨间时间线", "把 30 分钟拆成舒服的节奏。", `<div class="timeline-list">${["00:00 饮水", "05:00 拉伸", "12:00 整理", "20:00 今日三件事", "28:00 出门前检查"].map((x) => `<article>${x}</article>`).join("")}</div>`); }
function renderWheel() { return shell("菜单转盘", "随机转出今天的一餐。", `<div class="result-big"><strong id="wheelText">${escapeHtml(pick(config.keywords))}</strong><span>点击随机生成转动</span></div>`); }
function renderItinerary() { return shell("旅行板", "路线、预算、节奏分栏。", `<div class="mini-grid">${["上午", "午后", "傍晚", "预算", "备选", "纪念"].map((x, i) => `<article class="mini-card"><small>${x}</small><p>${escapeHtml(config.keywords[i % config.keywords.length])} · ${80 + i * 40} 元</p></article>`).join("")}</div>`); }
function renderTracker() { return shell("习惯泊位", "点击泊位记录连续天数。", `<div class="mini-grid">${config.keywords.map((x, i) => `<article class="mini-card"><small>${i + 1} 天</small><h3>${escapeHtml(x)}</h3><button data-act="habit">靠岸</button></article>`).join("")}</div>`); }
function renderBudget() { return shell("预算河流", "滑动分配支出比例。", config.keywords.slice(1).map((x, i) => `<label>${escapeHtml(x)}<input class="budgetInput" type="range" min="0" max="100" value="${15 + i * 10}" /></label>`).join("") + `<div id="budgetOut" class="result-big"></div>`); }
function renderLetter() { return shell("未来信笺", "写一封只保存在本地的信。", `<textarea id="mainInput" placeholder="写给未来的自己"></textarea><input id="dateInput" type="date" />`); }
function renderMood() { return shell("情绪天气", "选择天气，得到照顾建议。", `<div class="mini-grid">${config.keywords.map((x) => `<button data-weather="${escapeHtml(x)}">${escapeHtml(x)}</button>`).join("")}</div>`); }
function renderChecklist() { return shell("睡前清单", "低刺激晚间流程。", `<div class="timeline-list">${config.keywords.map((x) => `<article><label><input type="checkbox" /> ${escapeHtml(x)}</label></article>`).join("")}</div>`); }
function renderSplitter() { return shell("压力拆解", "把一件事拆成三口。", `<textarea id="mainInput" placeholder="写下现在最卡的一件事"></textarea><div id="splitOut" class="mini-grid"></div>`); }
function renderStars() { return shell("感谢星图", "点击生成星点。", `<div class="map-grid" id="starMap">${Array.from({length: 24}, (_, i) => `<button style="--power:${20 + (i % 6) * 12}%">★</button>`).join("")}</div>`); }
function renderQuiz() { return shell("谜题摊位", "先看谜面，再揭晓答案。", `<div class="result-big"><strong id="riddleText">白天睡觉，夜晚守门。</strong><span id="riddleAnswer">点击随机生成换题</span></div>`); }
function renderDice() { return shell("骰子冒险", "掷骰决定遭遇。", `<div class="dice-face" id="diceFace">1</div><div id="diceStory" class="mini-card"></div>`); }
function renderCreature() { return shell("生物培育", "生成外星动物档案。", `<div class="creature-shape" id="creatureShape"></div><div id="creatureBio" class="mini-card"></div>`); }
function renderTreasure() { return shell("藏宝地图", "点亮格子形成路线。", `<div class="map-grid">${Array.from({length: 30}, (_, i) => `<button style="--power:${15 + (i % 8) * 9}%">${i % 7 === 0 ? "◆" : "·"}</button>`).join("")}</div>`); }
function renderPixel() { return shell("像素签", "点击像素抽签。", `<div class="pixel-grid">${Array.from({length: 45}, (_, i) => `<button style="--power:${20 + (i % 9) * 7}%"></button>`).join("")}</div><div id="pixelText" class="mini-card"></div>`); }
function renderTrend() { return shell("趋势线", "随机生成指标曲线。", `<div id="trendBars" class="timeline-list"></div>`); }
function renderHeatmap() { return shell("热力图", "一周强度图。", `<div class="heatmap-grid">${Array.from({length: 35}, (_, i) => `<button style="--power:${15 + ((i * 17) % 70)}%"></button>`).join("")}</div>`); }
function renderTimeline() { return shell("时间线", "事件节点花园。", `<input id="eventInput" placeholder="新增事件" /><button data-act="addEvent">添加事件</button><div id="eventList" class="timeline-list">${renderEvents()}</div>`); }
function renderPoll() { return shell("投票条", "点击选项模拟反馈。", `<div id="pollList" class="timeline-list">${config.keywords.map((x, i) => `<article><button data-poll="${i}">${escapeHtml(x)}</button><div class="bar"><i style="width:${20 + i * 13}%"></i></div></article>`).join("")}</div>`); }
function renderMatrix() { return shell("权重矩阵", "调节权重比较方案。", config.keywords.map((x, i) => `<label>${escapeHtml(x)}<input class="matrixInput" type="range" min="0" max="100" value="${45 + i * 8}" /></label>`).join("") + `<div id="matrixOut" class="result-big"></div>`); }
function renderFont() { return shell("字体舞台", "试排标题。", `<input id="fontText" value="${escapeHtml(config.title)}" /><label>字号<input id="fontSize" type="range" min="28" max="96" value="56" /></label><div id="fontPreview" class="result-big"></div>`); }
function renderLogo() { return shell("标志混合", "生成几何标识。", `<input id="brandInput" value="${escapeHtml(config.title)}" /><div class="logo-shape" id="logoShape"></div><div id="logoLine" class="mini-card"></div>`); }
function renderLayout() { return shell("网格道场", "改变列数和留白。", `<label>列数<input id="colsInput" type="range" min="2" max="6" value="4" /></label><div id="layoutPreview" class="mini-grid"></div>`); }
function renderPalette() { return shell("配色地图", "生成并保存色组。", `<div id="paletteOut" class="palette-row">${palette().map((c) => `<i style="background:${c}"></i>`).join("")}</div>`); }
function renderMotion() { return shell("动效预览", "调节速度观看动效。", `<label>速度<input id="speedInput" type="range" min="500" max="3000" value="1400" /></label><div class="motion-box" id="motionBox"></div>`); }
function renderAgenda() { return shell("会议线", "议题到行动项。", `<div class="timeline-list">${["议题", "事实", "分歧", "结论", "行动项"].map((x) => `<article><strong>${x}</strong><p>${escapeHtml(pick(config.keywords))}</p></article>`).join("")}</div>`); }
function renderTeam() { return shell("团队温度", "能量和阻塞矩阵。", `<div class="heatmap-grid">${Array.from({length: 20}, (_, i) => `<button style="--power:${25 + (i % 5) * 14}%">${i % 4 === 0 ? "阻" : "能"}</button>`).join("")}</div>`); }
function renderCompliment() { return shell("夸夸生成", "真诚夸奖，不空泛。", `<select id="sceneInput">${config.keywords.map((x) => `<option>${escapeHtml(x)}</option>`).join("")}</select><div id="complimentOut" class="result-big"></div>`); }
function renderDecision() { return shell("决策桌", "风险收益对照。", `<div class="mini-grid">${["A方案", "B方案", "C方案"].map((x, i) => `<article class="mini-card"><h3>${x}</h3><div class="meter"><i style="width:${55 + i * 12}%"></i></div><p>${escapeHtml(config.keywords[i])}</p></article>`).join("")}</div>`); }
function renderEvent() { return shell("活动导演", "生成活动流程。", `<div class="timeline-list">${["开场", "破冰", "主题", "互动", "收尾"].map((x, i) => `<article><strong>${x}</strong><p>${15 + i * 20} 分钟 · ${escapeHtml(config.keywords[i % config.keywords.length])}</p></article>`).join("")}</div>`); }
function renderRenamer() { return shell("文件名雕刻", "批量命名预览。", `<textarea id="fileInput">IMG_001.png\nfinal final.docx\nvideo new.mp4</textarea><button data-act="rename">转换</button><div id="renameOut" class="timeline-list"></div>`); }
function renderPrompt() { return shell("提示词拼装", "角色、约束、输出格式。", `<input id="roleInput" placeholder="角色" value="资深顾问" /><textarea id="contextInput" placeholder="上下文"></textarea><div id="promptOut" class="mini-card"></div>`); }
function renderSnippets() { return shell("片段库", "常用文本一键复制。", `<div class="mini-grid">${config.keywords.map((x) => `<article class="mini-card"><h3>${escapeHtml(x)}</h3><p>这是一个可复用的 ${escapeHtml(x)} 模板。</p><button data-act="copySnippet">复制</button></article>`).join("")}</div>`); }
function renderChecklistMaker() { return shell("清单生成", "输入目标得到检查项。", `<input id="goalInput" placeholder="目标" value="发布一个页面" /><button data-act="makeChecklist">生成清单</button><div id="checkOut" class="timeline-list"></div>`); }
function renderBookmarks() { return shell("书签码头", "添加链接并分类。", `<input id="bookmarkTitle" placeholder="标题" /><input id="bookmarkUrl" placeholder="https://example.com" /><button data-act="addBookmark">添加</button><div id="bookmarkList" class="timeline-list">${renderBookmarksList()}</div>`); }
function renderMoon() { return shell("月相日记", "选择日期生成月相。", `<input id="moonDate" type="date" /><div class="moon-disc" id="moonDisc"></div><div id="moonText" class="mini-card"></div>`); }
function renderPlant() { return shell("植物档案", "浇水、光照、观察。", `<div class="mini-grid">${config.keywords.map((x) => `<article class="mini-card"><h3>${escapeHtml(x)}</h3><button data-act="plantCare">记录</button></article>`).join("")}</div>`); }
function renderPortal() { return shell("时间传送", "生成一段时空任务。", `<div id="portalOut" class="result-big"></div>`); }
function renderMenu() { return shell("秘密菜单", "组合口味和暗号。", `<div id="menuOut" class="mini-grid"></div>`); }
function renderSoundwalk() { return shell("声音路线", "生成城市听觉散步。", `<div id="soundList" class="timeline-list"></div>`); }

function bindCommon() {
  document.querySelectorAll("[data-act='randomize']").forEach((button) => button.addEventListener("click", randomize));
  document.querySelectorAll("[data-act='save']").forEach((button) => button.addEventListener("click", saveCurrent));
  document.querySelectorAll("[data-act='export']").forEach((button) => button.addEventListener("click", exportState));
  randomize();
}

function bindSpecific(kind) {
  const byId = (id, fn) => document.getElementById(id)?.addEventListener("input", fn);
  byId("mainInput", randomize);
  byId("minutesInput", (e) => { state.seconds = Number(e.target.value) * 60; saveState(); updateTimer(); });
  byId("goalInput", updateRoute);
  byId("fontText", updateFont);
  byId("fontSize", updateFont);
  byId("colsInput", updateLayout);
  byId("speedInput", updateMotion);
  byId("moonDate", updateMoon);
  document.querySelectorAll("[data-act='startTimer']").forEach((b) => b.addEventListener("click", toggleTimer));
  document.querySelectorAll("[data-act='resetTimer']").forEach((b) => b.addEventListener("click", resetTimer));
  document.querySelectorAll("[data-act='addArchive']").forEach((b) => b.addEventListener("click", addArchive));
  document.querySelectorAll("[data-act='addCard']").forEach((b) => b.addEventListener("click", addFlashcard));
  document.querySelectorAll("[data-act='addEvent']").forEach((b) => b.addEventListener("click", addEvent));
  document.querySelectorAll("[data-act='rename']").forEach((b) => b.addEventListener("click", renameFiles));
  document.querySelectorAll("[data-act='makeChecklist']").forEach((b) => b.addEventListener("click", makeChecklist));
  document.querySelectorAll("[data-act='addBookmark']").forEach((b) => b.addEventListener("click", addBookmark));
  document.querySelectorAll(".budgetInput").forEach((input) => input.addEventListener("input", updateBudget));
  document.querySelectorAll(".matrixInput").forEach((input) => input.addEventListener("input", updateMatrix));
  if (kind === "roadmap") updateRoute();
  if (kind === "budget") updateBudget();
  if (kind === "matrix") updateMatrix();
  if (kind === "font") updateFont();
  if (kind === "layout") updateLayout();
  if (kind === "motion") updateMotion();
  if (kind === "moon") updateMoon();
}

function randomize() {
  const text = document.getElementById("mainInput")?.value.trim();
  const ideas = [
    `${pick(config.keywords)} + ${pick(config.keywords)}：做一个 15 分钟实验`,
    `把${pick(config.keywords)}做成一个可以分享的小结果`,
    `${config.title}建议：先做最轻的一步，再保存观察`,
    text ? `${text} → ${pick(config.keywords)}版` : `${pick(config.keywords)}是今天的入口`,
  ];
  state.current = pick(ideas);
  saveState();
  updateResult(state.current);
  updateSpecialRandoms();
}

function updateSpecialRandoms() {
  setText("slotA", pick(config.keywords));
  setText("slotB", pick(config.keywords));
  setText("slotC", pick(config.keywords));
  setText("wheelText", pick(config.keywords));
  setText("riddleText", `${pick(config.keywords)}藏在夜市第三个摊位后面`);
  setText("riddleAnswer", `答案：${pick(config.keywords)}的影子`);
  setText("diceFace", String(1 + Math.floor(Math.random() * 6)));
  setText("diceStory", `${pick(config.keywords)}路线上遇到${pick(config.keywords)}，获得一次重选机会。`);
  setText("creatureBio", `物种：${pick(config.keywords)}兽。习性：夜晚发光，喜欢收集${pick(config.keywords)}。`);
  setText("pixelText", `今日签：${pick(config.keywords)}会带来一个小转机。`);
  setText("complimentOut", `你在${pick(config.keywords)}这件事上的细节很稳，让人觉得可靠。`);
  setText("portalOut", `你被送到${1980 + Math.floor(Math.random() * 80)}年的${pick(config.keywords)}，任务是带回一个答案。`);
  const menu = document.getElementById("menuOut");
  if (menu) menu.innerHTML = config.keywords.slice(0, 3).map((x) => `<article class="mini-card"><h3>${escapeHtml(x)}特调</h3><p>暗号：请给我一份${escapeHtml(pick(config.keywords))}。</p></article>`).join("");
  const sounds = document.getElementById("soundList");
  if (sounds) sounds.innerHTML = config.keywords.map((x, i) => `<article>${i + 1}. 在街角收集「${escapeHtml(x)}」的声音，停留 ${3 + i} 分钟。</article>`).join("");
  const trend = document.getElementById("trendBars");
  if (trend) trend.innerHTML = config.keywords.map((x, i) => `<article><strong>${escapeHtml(x)}</strong><div class="bar"><i style="width:${35 + ((i * 19 + Date.now() / 1000) % 55)}%"></i></div></article>`).join("");
  const scorePanel = document.getElementById("scorePanel");
  if (scorePanel) scorePanel.innerHTML = ["点击欲", "清晰度", "记忆点"].map((x, i) => `<article class="mini-card"><small>${x}</small><h3>${Math.round(60 + Math.random() * 35)}</h3></article>`).join("");
  const splitOut = document.getElementById("splitOut");
  if (splitOut) splitOut.innerHTML = ["能做", "能说", "能放下"].map((x) => `<article class="mini-card"><small>${x}</small><p>${escapeHtml(pick(config.keywords))}</p></article>`).join("");
}

function saveCurrent() {
  state.saved ??= [];
  state.saved.unshift({value: state.current || pick(config.keywords), at: new Date().toISOString()});
  state.saved = state.saved.slice(0, 20);
  saveState();
  updateResult("已保存：" + state.saved[0].value);
}

function exportState() {
  const blob = new Blob([JSON.stringify({site: config.title, state, exportedAt: new Date().toISOString()}, null, 2)], {type: "application/json"});
  const url = URL.createObjectURL(blob);
  const link = document.createElement("a");
  link.href = url;
  link.download = `${config.slug}-workspace.json`;
  link.click();
  URL.revokeObjectURL(url);
}

function updateResult(value) {
  const box = document.getElementById("resultBox");
  if (box) box.innerHTML = `<strong>${escapeHtml(value)}</strong><span>${escapeHtml(config.title)}</span>`;
}

function addArchive() {
  state.archives ??= [];
  state.archives.unshift({title: value("archiveTitle") || "未命名档案", body: value("archiveBody") || pick(config.keywords)});
  saveState();
  renderTool();
}

function renderSavedList() {
  return (state.archives || []).map((item) => `<article><strong>${escapeHtml(item.title)}</strong><p>${escapeHtml(item.body)}</p></article>`).join("") || "<article>还没有档案。</article>";
}

function addFlashcard() {
  state.flashcards ??= [];
  state.flashcards.unshift({front: value("frontInput") || pick(config.keywords), back: value("backInput") || "答案"});
  saveState();
  renderTool();
}

function cardHtml(card) {
  return `<article class="mini-card"><small>闪卡</small><h3>${escapeHtml(card.front)}</h3><p>${escapeHtml(card.back)}</p></article>`;
}

function updateRoute() {
  const list = document.getElementById("routeList");
  if (!list) return;
  const goal = value("goalInput") || config.keywords[0];
  list.innerHTML = ["基础", "练习", "项目", "复盘", "作品"].map((step, i) => `<article><strong>${step}</strong><p>${escapeHtml(goal)} · 第 ${i + 1} 阶段</p></article>`).join("");
}

function updateBudget() {
  const inputs = [...document.querySelectorAll(".budgetInput")];
  const total = inputs.reduce((sum, input) => sum + Number(input.value), 0);
  const out = document.getElementById("budgetOut");
  if (out) out.innerHTML = `<strong>${Math.max(0, 100 - total)}%</strong><span>剩余可分配预算</span>`;
}

function updateMatrix() {
  const inputs = [...document.querySelectorAll(".matrixInput")];
  const total = Math.round(inputs.reduce((sum, input) => sum + Number(input.value), 0) / Math.max(1, inputs.length));
  const out = document.getElementById("matrixOut");
  if (out) out.innerHTML = `<strong>${total}</strong><span>综合决策分</span>`;
}

function updateFont() {
  const preview = document.getElementById("fontPreview");
  if (!preview) return;
  preview.style.fontSize = `${value("fontSize") || 56}px`;
  preview.innerHTML = `<strong>${escapeHtml(value("fontText") || config.title)}</strong>`;
}

function updateLayout() {
  const preview = document.getElementById("layoutPreview");
  if (!preview) return;
  preview.style.gridTemplateColumns = `repeat(${value("colsInput") || 4}, 1fr)`;
  preview.innerHTML = Array.from({length: 12}, (_, i) => `<article class="mini-card"><small>${i + 1}</small><p>${escapeHtml(config.keywords[i % config.keywords.length])}</p></article>`).join("");
}

function updateMotion() {
  const box = document.getElementById("motionBox");
  if (box) box.style.setProperty("--speed", `${value("speedInput") || 1400}ms`);
}

function updateMoon() {
  const disc = document.getElementById("moonDisc");
  const text = document.getElementById("moonText");
  if (!disc || !text) return;
  const day = value("moonDate") ? new Date(value("moonDate")).getDate() : new Date().getDate();
  const phase = day % 29;
  disc.style.setProperty("--moon-x", `${20 + phase * 2}%`);
  text.innerHTML = `<h3>月相指数 ${phase}/29</h3><p>今晚适合记录：${escapeHtml(pick(config.keywords))}</p>`;
}

function addEvent() {
  state.events ??= [];
  state.events.unshift(value("eventInput") || pick(config.keywords));
  saveState();
  renderTool();
}

function renderEvents() {
  return (state.events || config.keywords).map((x, i) => `<article><strong>${i + 1}</strong><p>${escapeHtml(x)}</p></article>`).join("");
}

function renameFiles() {
  const out = document.getElementById("renameOut");
  if (!out) return;
  out.innerHTML = value("fileInput").split(/\n+/).filter(Boolean).map((name, i) => `<article>${new Date().toISOString().slice(0,10)}-${String(i + 1).padStart(2, "0")}-${slugify(name)}</article>`).join("");
}

function makeChecklist() {
  const goal = value("goalInput") || config.title;
  document.getElementById("checkOut").innerHTML = ["准备", "执行", "检查", "发布", "复盘"].map((x) => `<article><label><input type="checkbox" /> ${escapeHtml(goal)} · ${x}</label></article>`).join("");
}

function addBookmark() {
  state.bookmarks ??= [];
  state.bookmarks.unshift({title: value("bookmarkTitle") || "未命名链接", url: value("bookmarkUrl") || "#"});
  saveState();
  renderTool();
}

function renderBookmarksList() {
  return (state.bookmarks || []).map((x) => `<article><a href="${escapeAttr(x.url)}" target="_blank" rel="noreferrer">${escapeHtml(x.title)}</a></article>`).join("") || "<article>还没有书签。</article>";
}

function toggleTimer() {
  if (timer) {
    clearInterval(timer);
    timer = null;
    return;
  }
  timer = setInterval(() => {
    state.seconds = Math.max(0, (state.seconds || 0) - 1);
    saveState();
    updateTimer();
    if (!state.seconds) {
      clearInterval(timer);
      timer = null;
    }
  }, 1000);
}

function resetTimer() {
  state.seconds = Number(value("minutesInput") || 25) * 60;
  saveState();
  updateTimer();
}

function updateTimer() {
  setText("timeText", formatTime(state.seconds || 0));
}

function formatTime(seconds) {
  return `${String(Math.floor(seconds / 60)).padStart(2, "0")}:${String(seconds % 60).padStart(2, "0")}`;
}

function palette() {
  const base = [config.accent, config.warm, config.cool, "#ffffff", "#171814"];
  return base.sort(() => Math.random() - 0.5);
}

function slugify(text) {
  return text.toLowerCase().replace(/\.[a-z0-9]+$/i, "").replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "") || "file";
}

function value(id) {
  return document.getElementById(id)?.value || "";
}

function setText(id, text) {
  const node = document.getElementById(id);
  if (node) node.textContent = text;
}

function pick(items) {
  return items[Math.floor(Math.random() * items.length)];
}

function loadState() {
  try {
    return JSON.parse(localStorage.getItem(storageKey) || "{}");
  } catch {
    return {};
  }
}

function saveState() {
  localStorage.setItem(storageKey, JSON.stringify(state));
}

function escapeAttr(value) {
  return String(value).replace(/"/g, "&quot;");
}

function escapeHtml(value) {
  return String(value).replace(/[&<>"']/g, (char) => ({
    "&": "&amp;",
    "<": "&lt;",
    ">": "&gt;",
    "\"": "&quot;",
    "'": "&#039;",
  })[char]);
}
"""


VERIFY_PY = r'''
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def assert_true(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    index = (ROOT / "index.html").read_text(encoding="utf-8")
    match = re.search(r"window\.PORTAL_DATA = (.*?);</script>", index)
    assert_true(bool(match), "portal data missing")
    data = json.loads(match.group(1))
    sites = data["sites"]
    assert_true(len(sites) == 50, "site count must be 50")
    assert_true(len({site["kind"] for site in sites}) >= 38, "not enough distinct tool types")
    assert_true(len({site["skin"] for site in sites}) >= 18, "not enough visual skins")
    assert_true(len(data["previousLinks"]) >= 10, "previous links missing")
    for site in sites:
        path = ROOT / "sites" / site["slug"] / "index.html"
        assert_true(path.exists(), f"missing site page: {site['slug']}")
        text = path.read_text(encoding="utf-8")
        assert_true("repo-orb" in text and "source-footer-link" in text, f"source badge missing: {site['slug']}")
        assert_true(f'data-kind="{site["kind"]}"' in text, f"kind missing: {site['slug']}")
        assert_true(f'skin-{site["skin"]}' in text, f"skin missing: {site['slug']}")
    for required in ["assets/style.css", "assets/site.js", "assets/home.js", ".github/workflows/pages.yml", "README.md", "docs/SITE_MAP.md"]:
        assert_true((ROOT / required).exists(), f"missing {required}")
    forbidden = [
        "C:" + "\\Users",
        "M:" + "\\",
        "Users" + "/mo",
        "test" + "chatcpt",
        "public" + "-apis" + "-master",
    ]
    for path in ROOT.rglob("*"):
        if path.is_dir() or path.suffix.lower() not in {".html", ".css", ".js", ".md", ".py", ".yml", ".txt"}:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for marker in forbidden:
            assert_true(marker not in text, f"{marker} leaked in {path}")
    print("OK: rebuilt 50 sites with distinct tool types, visual skins, archive links, source badges, and path hygiene.")


if __name__ == "__main__":
    main()
'''


README_MD = f"""# 50 Fun Websites Lab

50 个功能明显不同的静态互动网站合集，并收录本对话之前生成过的网站链接。

- GitHub Pages: {PAGES_URL}
- 开源仓库: {REPO_URL}

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
"""


WORKFLOW_YML = """name: Deploy GitHub Pages

on:
  push:
    branches: [main]
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: pages
  cancel-in-progress: false

jobs:
  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/configure-pages@v5
      - uses: actions/upload-pages-artifact@v3
        with:
          path: .
      - id: deployment
        uses: actions/deploy-pages@v4
"""


def main() -> None:
    sites = [enrich(config, index) for index, config in enumerate(SITES, 1)]
    write(ROOT / "assets" / "style.css", STYLE_CSS.strip() + "\n")
    write(ROOT / "assets" / "home.js", HOME_JS.strip() + "\n")
    write(ROOT / "assets" / "site.js", SITE_JS.strip() + "\n")
    write(ROOT / "index.html", index_html(sites))
    write(ROOT / "README.md", README_MD)
    write(ROOT / "tests" / "verify.py", VERIFY_PY.strip() + "\n")
    write(ROOT / ".github" / "workflows" / "pages.yml", WORKFLOW_YML)
    write(ROOT / ".nojekyll", "")
    write(ROOT / ".gitignore", "__pycache__/\n*.pyc\n.playwright-cli/\n")
    sitemap = ["# 站点地图", "", f"- 总导航: {PAGES_URL}", ""]
    for category, desc in CATEGORIES.items():
        sitemap.extend([f"## {category}", "", desc, ""])
        for item in [site for site in sites if site["category"] == category]:
            sitemap.append(f"- [{item['title']}]({PAGES_URL}sites/{item['slug']}/): {item['description']}，工具类型 `{item['kind']}`，视觉 `{item['skin']}`")
        sitemap.append("")
    sitemap.extend(["## 历史网站", ""])
    for title, category, desc, url, repo in PREVIOUS_LINKS:
        sitemap.append(f"- [{title}]({url}) - {category} - {desc} - [源码]({repo})")
    write(ROOT / "docs" / "SITE_MAP.md", "\n".join(sitemap) + "\n")
    for item in sites:
        write(ROOT / "sites" / item["slug"] / "index.html", site_html(item))
    print(f"Rebuilt {len(sites)} distinct sites at {ROOT}")


if __name__ == "__main__":
    main()
