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
