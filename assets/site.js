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
