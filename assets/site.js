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
