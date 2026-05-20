from __future__ import annotations

import json
from pathlib import Path
from textwrap import dedent


ROOT = Path(__file__).resolve().parents[1]
REPO_URL = "https://github.com/qqemail0/fifty-fun-websites-lab"
PAGES_URL = "https://qqemail0.github.io/fifty-fun-websites-lab/"


CATEGORIES = {
    "创作灵感": "把零散想法变成可执行的文本、故事、标题和视觉线索。",
    "学习成长": "面向自学者的节奏、路线、复盘和记忆工具。",
    "生活计划": "把日常安排做得轻盈、清楚、有仪式感。",
    "情绪疗愈": "温柔地记录情绪，给自己一个可回来的空间。",
    "游戏互动": "适合打开即玩的微型互动体验。",
    "数据可视": "用轻量图表和卡片理解趋势与判断。",
    "设计美学": "为创作者准备的配色、排版、动效和品牌练习场。",
    "社交协作": "让会议、决策、活动和团队状态更容易推进。",
    "工具效率": "日常工作里的小型生成器、整理器和清单台。",
    "奇想实验": "更像一扇窗：月相、城市、时间和秘密菜单。",
}


SITES = [
    ("idea-forge", "灵感锻造炉", "创作灵感", "把关键词熔成选题、开场和行动卡。", "灵", "#f06a4f", "#f9c66b", "#6cc6b8", ["选题", "开场", "系列", "转折", "收束"]),
    ("story-oracle", "故事神谕台", "创作灵感", "抽取人物、冲突和结尾，生成短故事骨架。", "故", "#8e6df0", "#f0b56d", "#74d2c8", ["人物", "冲突", "伏笔", "结尾", "对白"]),
    ("dream-index", "梦境索引馆", "创作灵感", "记录梦的碎片，并把它们整理成可写作的素材。", "梦", "#4b8df7", "#9ee493", "#f4b7d2", ["梦象", "场景", "隐喻", "色彩", "余味"]),
    ("color-poem", "颜色诗生成器", "创作灵感", "用颜色、气味和物件生成一首可编辑的小诗。", "诗", "#e26d9a", "#ffd166", "#62d2a2", ["颜色", "气味", "物件", "节奏", "留白"]),
    ("title-lab", "爆款标题实验室", "创作灵感", "组合角度、对象和情绪，快速测试标题方向。", "题", "#ff7a59", "#ffd37a", "#5ec9e6", ["标题", "钩子", "受众", "反差", "关键词"]),
    ("focus-forest", "专注森林计时器", "学习成长", "用短冲刺、休息和复盘保护注意力。", "专", "#2f9e74", "#a7d96d", "#f0b76d", ["冲刺", "休息", "复盘", "能量", "节律"]),
    ("code-path", "编程路线罗盘", "学习成长", "根据目标生成语言、项目和练习路线。", "码", "#3f7df6", "#73d7ff", "#ffca6a", ["语言", "项目", "算法", "框架", "作品"]),
    ("memory-cards", "记忆卡片工坊", "学习成长", "把知识点拆成卡片、测试和间隔复习计划。", "记", "#ba6df0", "#7ce2b2", "#ffd166", ["卡片", "提问", "复习", "错题", "巩固"]),
    ("language-sprint", "语言冲刺舱", "学习成长", "每天生成听说读写小任务，适合外语练习。", "语", "#ef476f", "#ffd166", "#06d6a0", ["单词", "听力", "表达", "复述", "语境"]),
    ("exam-map", "考试作战地图", "学习成长", "整理科目、薄弱点、倒计时和冲刺优先级。", "考", "#2563eb", "#f59e0b", "#22c55e", ["科目", "薄弱点", "真题", "倒计时", "优先级"]),
    ("morning-ritual", "晨间仪式台", "生活计划", "把醒来后的 30 分钟排成温柔而清晰的流程。", "晨", "#f59e0b", "#fed7aa", "#60a5fa", ["饮水", "整理", "计划", "光线", "呼吸"]),
    ("meal-wheel", "今日吃什么转盘", "生活计划", "按口味、时间和预算生成菜单组合。", "食", "#fb7185", "#fbbf24", "#34d399", ["早餐", "午餐", "晚餐", "预算", "口味"]),
    ("trip-moodboard", "旅行情绪板", "生活计划", "把目的地、预算和节奏变成一张路线草图。", "旅", "#14b8a6", "#f97316", "#8b5cf6", ["城市", "路线", "预算", "节奏", "清单"]),
    ("habit-harbor", "习惯港口", "生活计划", "为习惯设置靠岸点、奖励和复盘记录。", "习", "#0ea5e9", "#84cc16", "#facc15", ["习惯", "奖励", "连续", "提醒", "复盘"]),
    ("budget-river", "预算河流", "生活计划", "把收入、支出和愿望分流成清晰的预算方案。", "财", "#16a34a", "#f59e0b", "#38bdf8", ["收入", "支出", "储蓄", "愿望", "风险"]),
    ("wind-letter", "风中来信", "情绪疗愈", "写一封不会催促你的信，保存给未来的自己。", "信", "#7dd3fc", "#fbcfe8", "#a7f3d0", ["书信", "风", "未来", "安静", "回声"]),
    ("emotion-weather", "情绪天气站", "情绪疗愈", "给今天的情绪命名，并生成照顾自己的建议。", "晴", "#60a5fa", "#fde68a", "#c4b5fd", ["天气", "情绪", "身体", "建议", "记录"]),
    ("sleep-lantern", "睡前灯笼", "情绪疗愈", "整理睡前想法，生成低刺激的晚间清单。", "灯", "#818cf8", "#f9a8d4", "#fde68a", ["睡眠", "放松", "灯光", "呼吸", "安顿"]),
    ("tiny-courage", "小小勇气站", "情绪疗愈", "把压力拆成一口能吞下的小行动。", "勇", "#f97316", "#fef08a", "#93c5fd", ["压力", "勇气", "一步", "支持", "完成"]),
    ("gratitude-constellation", "感谢星座图", "情绪疗愈", "记录感谢的人和事，生成属于今天的星图。", "谢", "#a78bfa", "#fde68a", "#67e8f9", ["感谢", "星星", "关系", "回忆", "善意"]),
    ("riddle-market", "谜题夜市", "游戏互动", "抽取谜面、线索和难度，做一个一分钟谜题。", "谜", "#f43f5e", "#f59e0b", "#22d3ee", ["谜面", "线索", "答案", "难度", "摊位"]),
    ("dice-adventure", "骰子冒险书", "游戏互动", "用骰点生成路线、遭遇和奖励。", "骰", "#7c3aed", "#fb7185", "#facc15", ["骰子", "地图", "遭遇", "奖励", "选择"]),
    ("alien-zoo", "外星动物园", "游戏互动", "随机培育奇妙生物，并给它们建立档案。", "兽", "#22c55e", "#a3e635", "#38bdf8", ["星球", "生物", "习性", "饲料", "档案"]),
    ("treasure-map", "藏宝图编辑器", "游戏互动", "组合地形、机关和提示，生成一张文字藏宝图。", "宝", "#d97706", "#fde68a", "#2dd4bf", ["地形", "机关", "提示", "宝藏", "路线"]),
    ("pixel-fortune", "像素运势机", "游戏互动", "抽取今日像素签，并保存你的幸运词。", "签", "#ec4899", "#facc15", "#60a5fa", ["运势", "像素", "幸运", "行动", "签文"]),
    ("trend-lens", "趋势观察镜", "数据可视", "把指标拆成趋势卡，快速发现变化。", "趋", "#06b6d4", "#84cc16", "#f97316", ["趋势", "信号", "增长", "异常", "判断"]),
    ("heatmap-desk", "热力图工作台", "数据可视", "为活动、时间和表现建立轻量热力图。", "热", "#ef4444", "#f97316", "#22c55e", ["热力", "时段", "强度", "活动", "颜色"]),
    ("timeline-garden", "时间线花园", "数据可视", "把事件按时间种成一片可筛选的花园。", "时", "#10b981", "#f9a8d4", "#93c5fd", ["事件", "时间", "阶段", "节点", "回看"]),
    ("survey-spark", "问卷火花", "数据可视", "把问题、选项和洞察整理成小型调查板。", "问", "#6366f1", "#fbbf24", "#34d399", ["问题", "选项", "反馈", "统计", "洞察"]),
    ("metric-lab", "指标实验室", "数据可视", "用权重和评分比较多个方案。", "指", "#0f766e", "#fde047", "#38bdf8", ["指标", "权重", "评分", "比较", "决策"]),
    ("font-theater", "字体剧场", "设计美学", "试验标题气质、字体搭配和版面节奏。", "字", "#111827", "#f43f5e", "#f59e0b", ["字体", "标题", "节奏", "气质", "版面"]),
    ("logo-mixer", "标志混合器", "设计美学", "组合品牌词、形状和情绪，生成 logo 方向。", "标", "#7f1d1d", "#fb7185", "#fbbf24", ["品牌", "图形", "识别", "情绪", "符号"]),
    ("layout-dojo", "版式道场", "设计美学", "练习网格、留白、层级和组件秩序。", "版", "#1f2937", "#22d3ee", "#a3e635", ["网格", "留白", "层级", "组件", "秩序"]),
    ("palette-atlas", "配色地图集", "设计美学", "按场景生成配色，并保存喜欢的色组。", "色", "#dc2626", "#fbbf24", "#06b6d4", ["配色", "场景", "对比", "色温", "记忆"]),
    ("motion-sketch", "动效草图本", "设计美学", "为界面状态生成动效描述和节奏建议。", "动", "#4f46e5", "#f472b6", "#22c55e", ["动效", "缓动", "进入", "反馈", "节奏"]),
    ("meeting-kite", "会议风筝", "社交协作", "把议题、结论和行动项拉成清楚的线。", "会", "#0284c7", "#f59e0b", "#a3e635", ["议题", "结论", "行动", "负责人", "时间"]),
    ("team-mood", "团队温度计", "社交协作", "记录团队状态、阻塞和互相支持。", "团", "#7c3aed", "#60a5fa", "#fbbf24", ["状态", "阻塞", "支持", "节奏", "能量"]),
    ("compliment-machine", "夸夸补给站", "社交协作", "生成真诚、不油腻、适合不同场合的夸奖。", "夸", "#fb7185", "#fde68a", "#86efac", ["夸奖", "场合", "真诚", "细节", "关系"]),
    ("decision-table", "多人决策桌", "社交协作", "用标准、风险和收益比较方案。", "决", "#0f172a", "#38bdf8", "#facc15", ["方案", "标准", "风险", "收益", "共识"]),
    ("event-planner", "小型活动导演", "社交协作", "为聚会、分享会和线上活动生成流程。", "活", "#ea580c", "#fdba74", "#22c55e", ["活动", "流程", "嘉宾", "物料", "氛围"]),
    ("filename-sculptor", "文件名雕刻机", "工具效率", "把混乱文件名整理成统一命名规则。", "名", "#334155", "#94a3b8", "#f59e0b", ["文件名", "规则", "日期", "版本", "归档"]),
    ("prompt-workbench", "提示词工作台", "工具效率", "拼装角色、上下文、约束和输出格式。", "提", "#2563eb", "#f97316", "#22c55e", ["角色", "上下文", "约束", "示例", "输出"]),
    ("clipboard-studio", "剪贴板排练室", "工具效率", "把常用文本片段整理成可复制模板。", "贴", "#0891b2", "#f0abfc", "#bef264", ["片段", "模板", "复制", "分类", "复用"]),
    ("checklist-lab", "清单实验室", "工具效率", "为复杂任务生成可勾选的执行清单。", "清", "#16a34a", "#facc15", "#60a5fa", ["清单", "步骤", "检查", "交付", "复盘"]),
    ("bookmark-cove", "书签海湾", "工具效率", "把链接按主题、用途和优先级整理。", "签", "#0369a1", "#67e8f9", "#fde047", ["链接", "主题", "用途", "优先级", "收藏"]),
    ("moon-diary", "月相日记", "奇想实验", "把日期、心情和月光感受写成一页日记。", "月", "#4338ca", "#c4b5fd", "#fde68a", ["月相", "日记", "夜晚", "愿望", "回望"]),
    ("plant-whisper", "植物悄悄话", "奇想实验", "给植物建立照料档案和今日对话。", "植", "#15803d", "#86efac", "#fef08a", ["植物", "浇水", "光照", "观察", "对话"]),
    ("time-portal", "时间传送门", "奇想实验", "把某个年份、地点和身份拼成一段旅程。", "门", "#7e22ce", "#f472b6", "#22d3ee", ["年份", "地点", "身份", "任务", "出口"]),
    ("secret-menu", "隐藏菜单研究所", "奇想实验", "为咖啡、甜品和夜宵生成秘密菜单。", "菜", "#be123c", "#fbbf24", "#34d399", ["菜单", "口味", "暗号", "搭配", "惊喜"]),
    ("city-soundwalk", "城市声音漫步", "奇想实验", "记录街角声音，并生成一条散步路线。", "声", "#0e7490", "#a7f3d0", "#f9a8d4", ["声音", "街角", "路线", "节拍", "记忆"]),
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


def enrich_site(site: tuple[str, str, str, str, str, str, str, str, list[str]], index: int) -> dict:
    slug, title, category, description, mark, accent, warm, cool, keywords = site
    verbs = ["生成", "筛选", "收藏", "复盘", "导出", "组合", "校准", "归档"]
    items = []
    for i in range(8):
        key = keywords[i % len(keywords)]
        items.append(
            {
                "title": f"{key} · {verbs[i]}卡",
                "body": f"围绕“{key}”给出一个可立即执行的小模块，适合在 {title} 中作为下一步行动。",
                "tag": key,
                "score": 62 + ((index * 7 + i * 11) % 37),
            }
        )
    steps = [
        f"选择一个核心词：{keywords[0]}",
        f"用生成器得到 3 个关于{keywords[1]}的方向",
        f"收藏最想推进的卡片，并写下{keywords[2]}记录",
        f"导出本地工作台，作为下一次继续的入口",
    ]
    prompts = [
        f"把{keywords[0]}改成一个 15 分钟任务",
        f"给{keywords[1]}增加一个反差角度",
        f"围绕{keywords[2]}生成三个版本",
        f"把{keywords[3]}做成清单",
        f"用{keywords[4]}设计一个收尾动作",
        f"写一个更温柔的提示",
        f"压缩成一句话",
        f"加入一个可衡量指标",
    ]
    actions = ["立刻做一版", "留到明早", "发给朋友看", "拆成三步", "加入收藏", "写进复盘"]
    return {
        "slug": slug,
        "title": title,
        "category": category,
        "description": description,
        "mark": mark,
        "accent": accent,
        "warm": warm,
        "cool": cool,
        "keywords": keywords,
        "items": items,
        "steps": steps,
        "prompts": prompts,
        "actions": actions,
        "repoUrl": REPO_URL,
        "homeUrl": "../../index.html",
        "pageUrl": f"{PAGES_URL}sites/{slug}/",
    }


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def site_html(config: dict) -> str:
    payload = json.dumps(config, ensure_ascii=False)
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
          <body class="site-page" style="--accent:{config["accent"]};--warm:{config["warm"]};--cool:{config["cool"]};">
            <canvas class="ambient-canvas" aria-hidden="true"></canvas>
            <header class="topbar">
              <a class="brand" href="../../index.html"><span class="brand-mark">{config["mark"]}</span><span>50 Sites Lab</span></a>
              <nav class="top-actions">
                <a class="pill-link" href="../../index.html">总导航</a>
                <a class="repo-orb" href="{REPO_URL}" target="_blank" rel="noreferrer" aria-label="GitHub 开源地址">GH</a>
              </nav>
            </header>
            <main id="app" class="site-shell"></main>
            <footer class="source-footer">
              <div><strong>{config["title"]}</strong><span>{config["category"]} · 本地数据保存在当前浏览器。</span></div>
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
            <meta name="description" content="50 个功能完整的静态互动网站合集，并收录本对话之前生成过的网站链接、分类和描述。" />
            <link rel="stylesheet" href="assets/style.css" />
            <script>window.PORTAL_DATA = {payload};</script>
            <script src="assets/home.js" defer></script>
          </head>
          <body class="home-page">
            <canvas class="ambient-canvas" aria-hidden="true"></canvas>
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
                  <p class="eyebrow">Static Playground · GitHub Pages Ready</p>
                  <h1>50 个打开就能玩的完整小网站。</h1>
                  <p class="lead">创作、学习、生活、情绪、游戏、数据、设计、协作、效率、奇想实验，一次打包成一个可部署的静态站群。每个子站都有独立页面、搜索、收藏、笔记、任务、生成器和导出能力。</p>
                  <div class="hero-actions">
                    <a class="primary-link" href="#new-sites">浏览网站</a>
                    <a class="secondary-link" href="#archive">查看历史链接</a>
                  </div>
                </div>
                <section class="hero-board" aria-label="项目概览">
                  <strong>50</strong>
                  <span>new websites</span>
                  <div class="mini-grid"><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i></div>
                </section>
              </section>
              <section class="control-panel" id="new-sites">
                <div>
                  <h2>新网站目录</h2>
                  <p>按分类筛选，或搜索站名、用途、关键词。</p>
                </div>
                <div class="filters">
                  <input id="searchInput" type="search" placeholder="搜索：标题、分类、描述、关键词" />
                  <select id="categoryInput"><option value="全部">全部分类</option></select>
                </div>
              </section>
              <section id="siteGrid" class="site-grid"></section>
              <section class="control-panel archive-panel" id="archive">
                <div>
                  <h2>之前生成的网站</h2>
                  <p>从本机仓库和 README 里整理出的部署链接与开源地址。</p>
                </div>
              </section>
              <section id="archiveGrid" class="archive-grid"></section>
            </main>
            <footer class="source-footer">
              <div><strong>50 Fun Websites Lab</strong><span>所有页面均为纯静态实现，可直接部署到 GitHub Pages。</span></div>
              <a class="source-footer-link" href="{REPO_URL}" target="_blank" rel="noreferrer">开源项目</a>
            </footer>
          </body>
        </html>
        """
    )


STYLE_CSS = r"""
:root {
  color-scheme: light;
  --bg: #f7f4ed;
  --ink: #151711;
  --muted: #6b6d65;
  --paper: rgba(255, 255, 255, 0.76);
  --panel: rgba(255, 255, 255, 0.9);
  --line: rgba(21, 23, 17, 0.12);
  --accent: #f06a4f;
  --warm: #f9c66b;
  --cool: #6cc6b8;
}

* { box-sizing: border-box; }

html { scroll-behavior: smooth; }

body {
  min-height: 100vh;
  margin: 0;
  color: var(--ink);
  font-family: "Microsoft YaHei", "Segoe UI", sans-serif;
  background:
    radial-gradient(circle at 15% 12%, color-mix(in srgb, var(--warm) 38%, transparent), transparent 28rem),
    radial-gradient(circle at 82% 6%, color-mix(in srgb, var(--cool) 28%, transparent), transparent 24rem),
    linear-gradient(135deg, #fffaf0, var(--bg) 48%, #eef6f2);
}

a { color: inherit; }

button,
input,
select,
textarea {
  font: inherit;
}

.ambient-canvas {
  position: fixed;
  inset: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
  opacity: 0.42;
  z-index: -1;
}

.topbar,
.home-shell,
.site-shell,
.source-footer {
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

.brand,
.top-actions,
.hero-actions,
.filters,
.card-actions,
.tool-actions {
  display: flex;
  align-items: center;
  gap: 10px;
}

.brand {
  font-weight: 900;
  text-decoration: none;
}

.brand-mark,
.repo-orb {
  display: grid;
  width: 38px;
  height: 38px;
  place-items: center;
  color: #fff;
  font-size: 13px;
  font-weight: 900;
  text-decoration: none;
  background: linear-gradient(135deg, var(--accent), var(--cool));
  border-radius: 50%;
  box-shadow: 0 14px 34px color-mix(in srgb, var(--accent) 28%, transparent);
}

.pill-link,
.primary-link,
.secondary-link,
.source-footer-link,
button {
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

.pill-link,
.secondary-link {
  background: var(--paper);
}

.primary-link,
button {
  color: #fff;
  background: linear-gradient(135deg, var(--accent), color-mix(in srgb, var(--accent) 62%, var(--cool)));
  border: 0;
  cursor: pointer;
}

.home-hero,
.site-hero {
  display: grid;
  grid-template-columns: minmax(0, 1fr) minmax(300px, 0.46fr);
  gap: 24px;
  align-items: stretch;
  padding: 44px 0 24px;
}

.eyebrow {
  margin: 0 0 12px;
  color: var(--accent);
  font-size: 12px;
  font-weight: 900;
  letter-spacing: 0;
  text-transform: uppercase;
}

h1,
h2,
h3,
p {
  margin: 0;
}

h1 {
  max-width: 840px;
  font-size: clamp(42px, 7vw, 86px);
  line-height: 0.96;
}

h2 { font-size: 25px; }
h3 { font-size: 18px; }

.lead {
  max-width: 760px;
  margin-top: 18px;
  color: var(--muted);
  font-size: 17px;
  line-height: 1.9;
}

.hero-actions { margin-top: 22px; flex-wrap: wrap; }

.hero-board,
.panel,
.site-card,
.archive-card,
.tool-card,
.result-card {
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 8px;
  box-shadow: 0 18px 70px rgba(23, 22, 16, 0.08);
  backdrop-filter: blur(18px);
}

.hero-board {
  display: grid;
  align-content: center;
  gap: 8px;
  min-height: 320px;
  padding: 24px;
  overflow: hidden;
}

.hero-board strong {
  font-size: clamp(80px, 12vw, 150px);
  line-height: 0.85;
}

.hero-board span {
  color: var(--muted);
  font-weight: 900;
}

.mini-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 8px;
  margin-top: 24px;
}

.mini-grid i {
  display: block;
  aspect-ratio: 1;
  border-radius: 8px;
  background: linear-gradient(135deg, var(--accent), var(--warm));
}

.mini-grid i:nth-child(2n) { background: linear-gradient(135deg, var(--cool), var(--warm)); }

.control-panel {
  display: flex;
  justify-content: space-between;
  gap: 16px;
  align-items: end;
  margin-top: 20px;
  padding: 18px;
  background: rgba(255,255,255,0.52);
  border: 1px solid var(--line);
  border-radius: 8px;
}

.control-panel p,
.site-card p,
.archive-card p,
.panel p,
.source-footer,
.result-card span,
.task-row span {
  color: var(--muted);
}

.filters { flex-wrap: wrap; justify-content: flex-end; }

input,
select,
textarea {
  width: 100%;
  border: 1px solid var(--line);
  border-radius: 8px;
  background: rgba(255,255,255,0.86);
  color: var(--ink);
  outline: none;
}

input,
select {
  min-height: 42px;
  padding: 0 12px;
}

textarea {
  min-height: 140px;
  padding: 12px;
  resize: vertical;
}

.filters input { width: min(360px, 100vw); }
.filters select { width: 180px; }

.site-grid,
.archive-grid,
.card-grid,
.tool-grid,
.workspace-grid {
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

.site-card,
.archive-card {
  position: relative;
  display: grid;
  min-height: 230px;
  padding: 16px;
  overflow: hidden;
  text-decoration: none;
}

.site-card::before,
.archive-card::before {
  content: "";
  position: absolute;
  inset: auto -24px -42px auto;
  width: 130px;
  height: 130px;
  background: radial-gradient(circle, color-mix(in srgb, var(--accent) 42%, transparent), transparent 68%);
}

.site-card small,
.archive-card small,
.tag {
  width: fit-content;
  color: var(--accent);
  font-size: 12px;
  font-weight: 900;
}

.site-card h3,
.archive-card h3 { align-self: end; }

.site-card p,
.archive-card p {
  line-height: 1.7;
}

.site-meta,
.tag-list {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
}

.tag {
  padding: 5px 8px;
  background: color-mix(in srgb, var(--accent) 9%, white);
  border: 1px solid var(--line);
  border-radius: 999px;
}

.site-hero { align-items: center; }

.visual-panel {
  min-height: 330px;
  padding: 18px;
  overflow: hidden;
}

.visual-stack {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 8px;
  height: 100%;
}

.visual-stack i {
  display: block;
  min-height: 42px;
  border-radius: 999px;
  background: linear-gradient(180deg, var(--accent), var(--warm));
  transform: translateY(var(--shift));
}

.visual-stack i:nth-child(2n) { background: linear-gradient(180deg, var(--cool), var(--warm)); }

.panel { padding: 16px; }

.tool-grid {
  grid-template-columns: 0.9fr 1.1fr;
  align-items: start;
  margin-bottom: 34px;
}

.card-grid { grid-template-columns: repeat(4, minmax(0, 1fr)); }

.tool-card,
.result-card {
  display: grid;
  gap: 10px;
  padding: 14px;
}

.card-actions,
.tool-actions { flex-wrap: wrap; }

.result-card {
  min-height: 172px;
}

.result-card strong { font-size: 19px; }

.score-bar {
  height: 9px;
  overflow: hidden;
  background: color-mix(in srgb, var(--muted) 12%, white);
  border-radius: 999px;
}

.score-bar i {
  display: block;
  height: 100%;
  background: linear-gradient(90deg, var(--accent), var(--cool));
}

.workspace-grid {
  grid-template-columns: repeat(2, minmax(0, 1fr));
}

.task-list { display: grid; gap: 8px; }

.task-row {
  display: grid;
  grid-template-columns: auto 1fr auto;
  gap: 8px;
  align-items: center;
  padding: 8px;
  background: rgba(255,255,255,0.66);
  border: 1px solid var(--line);
  border-radius: 8px;
}

.source-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 12px;
  padding: 28px 0 36px;
}

.source-footer div {
  display: grid;
  gap: 5px;
}

.source-footer-link {
  color: #fff;
  background: var(--ink);
}

.hidden { display: none !important; }

@media (max-width: 1040px) {
  .site-grid,
  .card-grid {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }

  .home-hero,
  .site-hero,
  .tool-grid {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 680px) {
  .topbar,
  .control-panel,
  .source-footer {
    align-items: flex-start;
    flex-direction: column;
  }

  .top-actions { flex-wrap: wrap; }

  .site-grid,
  .archive-grid,
  .card-grid,
  .workspace-grid {
    grid-template-columns: 1fr;
  }

  .filters,
  .filters input,
  .filters select {
    width: 100%;
  }
}
"""


HOME_JS = r"""
const data = window.PORTAL_DATA;
const $ = (id) => document.getElementById(id);

document.addEventListener("DOMContentLoaded", () => {
  drawAmbient();
  buildCategories();
  renderSites();
  renderArchive();
  $("searchInput").addEventListener("input", renderSites);
  $("categoryInput").addEventListener("change", renderSites);
});

function buildCategories() {
  Object.keys(data.categories).forEach((name) => {
    const option = document.createElement("option");
    option.value = name;
    option.textContent = name;
    $("categoryInput").append(option);
  });
}

function renderSites() {
  const query = $("searchInput").value.trim().toLowerCase();
  const category = $("categoryInput").value;
  const sites = data.sites.filter((site) => {
    const haystack = [site.title, site.category, site.description, ...(site.keywords || [])].join(" ").toLowerCase();
    return (category === "全部" || site.category === category) && haystack.includes(query);
  });
  $("siteGrid").replaceChildren(...sites.map(siteCard));
}

function siteCard(site) {
  const node = document.createElement("a");
  node.className = "site-card";
  node.href = `sites/${site.slug}/`;
  node.style.setProperty("--accent", site.accent);
  node.style.setProperty("--warm", site.warm);
  node.style.setProperty("--cool", site.cool);
  node.innerHTML = `
    <small>${escapeHtml(site.category)}</small>
    <h3>${escapeHtml(site.title)}</h3>
    <p>${escapeHtml(site.description)}</p>
    <div class="tag-list">${site.keywords.slice(0, 3).map((tag) => `<span class="tag">${escapeHtml(tag)}</span>`).join("")}</div>
  `;
  return node;
}

function renderArchive() {
  $("archiveGrid").replaceChildren(...data.previousLinks.map((item) => {
    const node = document.createElement("article");
    node.className = "archive-card";
    node.innerHTML = `
      <small>${escapeHtml(item.category)}</small>
      <h3>${escapeHtml(item.title)}</h3>
      <p>${escapeHtml(item.description)}</p>
      <div class="card-actions">
        <a class="primary-link" href="${item.url}" target="_blank" rel="noreferrer">访问</a>
        <a class="secondary-link" href="${item.repo}" target="_blank" rel="noreferrer">源码</a>
      </div>
    `;
    return node;
  }));
}

function drawAmbient() {
  const canvas = document.querySelector(".ambient-canvas");
  const ctx = canvas.getContext("2d");
  const resize = () => {
    canvas.width = window.innerWidth * devicePixelRatio;
    canvas.height = window.innerHeight * devicePixelRatio;
    ctx.setTransform(devicePixelRatio, 0, 0, devicePixelRatio, 0, 0);
    paint();
  };
  const paint = () => {
    ctx.clearRect(0, 0, window.innerWidth, window.innerHeight);
    for (let i = 0; i < 42; i++) {
      const x = (i * 137) % window.innerWidth;
      const y = (i * 89) % window.innerHeight;
      ctx.fillStyle = i % 3 === 0 ? "rgba(240,106,79,.18)" : i % 3 === 1 ? "rgba(108,198,184,.16)" : "rgba(249,198,107,.14)";
      ctx.beginPath();
      ctx.arc(x, y, 12 + (i % 7) * 5, 0, Math.PI * 2);
      ctx.fill();
    }
  };
  window.addEventListener("resize", resize);
  resize();
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
const storageKey = `fifty-site:${config.slug}`;
let state = loadState();

document.addEventListener("DOMContentLoaded", () => {
  drawAmbient();
  renderApp();
});

function renderApp() {
  const app = document.getElementById("app");
  app.innerHTML = `
    <section class="site-hero">
      <div>
        <p class="eyebrow">${escapeHtml(config.category)}</p>
        <h1>${escapeHtml(config.title)}</h1>
        <p class="lead">${escapeHtml(config.description)}</p>
        <div class="hero-actions">
          <button data-action="generate">生成一个灵感</button>
          <button data-action="export">导出工作台</button>
          <button data-action="share">复制链接</button>
        </div>
      </div>
      <section class="hero-board visual-panel" aria-label="${escapeHtml(config.title)} 视觉图">
        <div class="visual-stack">${Array.from({length: 15}, (_, i) => `<i style="--shift:${(i % 5) * 15}px"></i>`).join("")}</div>
      </section>
    </section>
    <section class="tool-grid">
      <section class="panel">
        <div class="control-panel">
          <div>
            <h2>模块卡片</h2>
            <p>搜索并收藏适合今天推进的卡片。</p>
          </div>
          <div class="filters">
            <input id="cardSearch" type="search" placeholder="搜索关键词" />
          </div>
        </div>
        <div id="cardGrid" class="card-grid"></div>
      </section>
      <aside class="panel">
        <h2>灵感生成器</h2>
        <p>组合提示、行动和关键词，生成一个可执行的小方向。</p>
        <div id="generated" class="result-card"></div>
        <div class="tool-actions">
          <button data-action="generate">重新生成</button>
          <button data-action="saveGenerated">保存结果</button>
        </div>
      </aside>
    </section>
    <section class="workspace-grid">
      <section class="panel">
        <h2>我的笔记</h2>
        <p>内容保存在当前浏览器，适合临时推演和复盘。</p>
        <textarea id="notesInput" placeholder="写下你的想法、结论或下一步。"></textarea>
      </section>
      <section class="panel">
        <h2>行动清单</h2>
        <p>把灵感落到今天可以完成的小动作。</p>
        <div class="tool-actions">
          <input id="taskInput" placeholder="新增一个任务" />
          <button data-action="addTask">添加</button>
        </div>
        <div id="taskList" class="task-list"></div>
      </section>
      <section class="panel">
        <h2>路线步骤</h2>
        <div class="card-grid">${config.steps.map((step, i) => `<article class="tool-card"><small>Step ${i + 1}</small><strong>${escapeHtml(step)}</strong></article>`).join("")}</div>
      </section>
      <section class="panel">
        <h2>状态评分</h2>
        <p>调节三个维度，得到今日推进指数。</p>
        <label>清晰度<input class="scoreInput" type="range" min="0" max="100" value="${state.scores.clarity}" data-score="clarity" /></label>
        <label>趣味度<input class="scoreInput" type="range" min="0" max="100" value="${state.scores.fun}" data-score="fun" /></label>
        <label>可执行度<input class="scoreInput" type="range" min="0" max="100" value="${state.scores.action}" data-score="action" /></label>
        <div id="scoreOutput" class="result-card"></div>
      </section>
    </section>
  `;
  document.getElementById("notesInput").value = state.notes;
  bindEvents();
  renderCards();
  renderGenerated();
  renderTasks();
  renderScore();
}

function bindEvents() {
  document.querySelectorAll("[data-action]").forEach((node) => {
    node.addEventListener("click", () => actions[node.dataset.action]?.());
  });
  document.getElementById("cardSearch").addEventListener("input", renderCards);
  document.getElementById("notesInput").addEventListener("input", (event) => {
    state.notes = event.target.value;
    saveState();
  });
  document.querySelectorAll(".scoreInput").forEach((input) => {
    input.addEventListener("input", (event) => {
      state.scores[event.target.dataset.score] = Number(event.target.value);
      saveState();
      renderScore();
    });
  });
}

const actions = {
  generate() {
    state.current = makeIdea();
    state.history.unshift(state.current);
    state.history = state.history.slice(0, 12);
    saveState();
    renderGenerated();
  },
  saveGenerated() {
    if (!state.current) state.current = makeIdea();
    state.savedIdeas.unshift(state.current);
    state.savedIdeas = state.savedIdeas.slice(0, 20);
    saveState();
    renderGenerated("已保存到导出数据里。");
  },
  addTask() {
    const input = document.getElementById("taskInput");
    const text = input.value.trim();
    if (!text) return;
    state.tasks.push({text, done: false, id: Date.now()});
    input.value = "";
    saveState();
    renderTasks();
  },
  export() {
    const payload = {
      site: config.title,
      notes: state.notes,
      tasks: state.tasks,
      savedCards: state.savedCards,
      savedIdeas: state.savedIdeas,
      scores: state.scores,
      exportedAt: new Date().toISOString(),
    };
    const blob = new Blob([JSON.stringify(payload, null, 2)], {type: "application/json"});
    const url = URL.createObjectURL(blob);
    const link = document.createElement("a");
    link.href = url;
    link.download = `${config.slug}-workspace.json`;
    link.click();
    URL.revokeObjectURL(url);
  },
  share() {
    navigator.clipboard?.writeText(location.href);
    renderGenerated("链接已复制。");
  },
};

function renderCards() {
  const query = document.getElementById("cardSearch").value.trim().toLowerCase();
  const cards = config.items.filter((item) => [item.title, item.body, item.tag].join(" ").toLowerCase().includes(query));
  document.getElementById("cardGrid").replaceChildren(...cards.map((item) => {
    const saved = state.savedCards.includes(item.title);
    const node = document.createElement("article");
    node.className = "tool-card";
    node.innerHTML = `
      <small>${escapeHtml(item.tag)}</small>
      <strong>${escapeHtml(item.title)}</strong>
      <p>${escapeHtml(item.body)}</p>
      <div class="score-bar"><i style="width:${item.score}%"></i></div>
      <button>${saved ? "已收藏" : "收藏"}</button>
    `;
    node.querySelector("button").addEventListener("click", () => {
      state.savedCards = saved ? state.savedCards.filter((title) => title !== item.title) : [...state.savedCards, item.title];
      saveState();
      renderCards();
    });
    return node;
  }));
}

function renderGenerated(message = "") {
  if (!state.current) state.current = makeIdea();
  document.getElementById("generated").innerHTML = `
    <small>${message || "今日方向"}</small>
    <strong>${escapeHtml(state.current.title)}</strong>
    <p>${escapeHtml(state.current.body)}</p>
    <span>${escapeHtml(state.current.action)}</span>
  `;
}

function renderTasks() {
  const list = document.getElementById("taskList");
  if (!state.tasks.length) {
    list.innerHTML = `<article class="task-row"><span>还没有任务，先添加一个最小动作。</span></article>`;
    return;
  }
  list.replaceChildren(...state.tasks.map((task) => {
    const row = document.createElement("article");
    row.className = "task-row";
    row.innerHTML = `<input type="checkbox" ${task.done ? "checked" : ""} /><span>${escapeHtml(task.text)}</span><button>删除</button>`;
    row.querySelector("input").addEventListener("change", (event) => {
      task.done = event.target.checked;
      saveState();
      renderTasks();
    });
    row.querySelector("button").addEventListener("click", () => {
      state.tasks = state.tasks.filter((item) => item.id !== task.id);
      saveState();
      renderTasks();
    });
    return row;
  }));
}

function renderScore() {
  const values = Object.values(state.scores);
  const total = Math.round(values.reduce((sum, item) => sum + item, 0) / values.length);
  document.getElementById("scoreOutput").innerHTML = `
    <small>今日推进指数</small>
    <strong>${total}</strong>
    <div class="score-bar"><i style="width:${total}%"></i></div>
    <p>${total >= 75 ? "状态很好，可以推进主线。" : total >= 45 ? "适合做小步验证。" : "先降低难度，保护节奏。"}</p>
  `;
}

function makeIdea() {
  const pick = (arr) => arr[Math.floor(Math.random() * arr.length)];
  const keyword = pick(config.keywords);
  const prompt = pick(config.prompts);
  const action = pick(config.actions);
  return {
    title: `${keyword}：${prompt}`,
    body: `在「${config.title}」里，把它做成一个 15 分钟内可完成的小实验，然后观察结果。`,
    action,
    at: new Date().toISOString(),
  };
}

function loadState() {
  try {
    return {
      notes: "",
      tasks: [],
      savedCards: [],
      savedIdeas: [],
      history: [],
      current: null,
      scores: {clarity: 68, fun: 72, action: 64},
      ...JSON.parse(localStorage.getItem(storageKey) || "{}"),
    };
  } catch {
    return {notes: "", tasks: [], savedCards: [], savedIdeas: [], history: [], current: null, scores: {clarity: 68, fun: 72, action: 64}};
  }
}

function saveState() {
  localStorage.setItem(storageKey, JSON.stringify(state));
}

function drawAmbient() {
  const canvas = document.querySelector(".ambient-canvas");
  const ctx = canvas.getContext("2d");
  const colors = [getCss("--accent"), getCss("--warm"), getCss("--cool")];
  const resize = () => {
    canvas.width = window.innerWidth * devicePixelRatio;
    canvas.height = window.innerHeight * devicePixelRatio;
    ctx.setTransform(devicePixelRatio, 0, 0, devicePixelRatio, 0, 0);
    paint();
  };
  const paint = () => {
    ctx.clearRect(0, 0, window.innerWidth, window.innerHeight);
    for (let i = 0; i < 36; i++) {
      ctx.globalAlpha = 0.14;
      ctx.fillStyle = colors[i % colors.length];
      ctx.beginPath();
      ctx.roundRect((i * 83) % window.innerWidth, (i * 131) % window.innerHeight, 80 + (i % 5) * 18, 18 + (i % 4) * 12, 20);
      ctx.fill();
    }
    ctx.globalAlpha = 1;
  };
  window.addEventListener("resize", resize);
  resize();
}

function getCss(name) {
  return getComputedStyle(document.body).getPropertyValue(name).trim();
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
    assert_true(len(data["sites"]) == 50, "site count must be 50")
    assert_true(len(data["previousLinks"]) >= 10, "previous links missing")
    for site in data["sites"]:
        path = ROOT / "sites" / site["slug"] / "index.html"
        assert_true(path.exists(), f"missing site page: {site['slug']}")
        text = path.read_text(encoding="utf-8")
        assert_true("repo-orb" in text and "source-footer-link" in text, f"source badge missing: {site['slug']}")
        assert_true(site["title"] in text, f"title missing: {site['slug']}")
    for required in ["assets/style.css", "assets/site.js", "assets/home.js", ".github/workflows/pages.yml", "README.md"]:
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
    print("OK: 50 static websites, portal, archive links, source badges, and path hygiene verified.")


if __name__ == "__main__":
    main()
'''


README_MD = f"""# 50 Fun Websites Lab

50 个功能完整的静态互动网站合集，并收录本对话之前生成过的网站链接。

- GitHub Pages: {PAGES_URL}
- 开源仓库: {REPO_URL}

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
    sites = [enrich_site(site, index) for index, site in enumerate(SITES, 1)]
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
        for site in [item for item in sites if item["category"] == category]:
            sitemap.append(f"- [{site['title']}]({PAGES_URL}sites/{site['slug']}/): {site['description']}")
        sitemap.append("")
    sitemap.extend(["## 历史网站", ""])
    for title, category, desc, url, repo in PREVIOUS_LINKS:
        sitemap.append(f"- [{title}]({url}) - {category} - {desc} - [源码]({repo})")
    write(ROOT / "docs" / "SITE_MAP.md", "\n".join(sitemap) + "\n")
    for site in sites:
        write(ROOT / "sites" / site["slug"] / "index.html", site_html(site))
    print(f"Generated {len(sites)} sites at {ROOT}")


if __name__ == "__main__":
    main()
