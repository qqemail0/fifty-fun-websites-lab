const data = window.PORTAL_DATA;

const $ = (id) => document.getElementById(id);

document.addEventListener("DOMContentLoaded", () => {
  buildCategories();
  renderStats();
  renderArchive();
  $("searchInput").addEventListener("input", renderArchive);
  $("categoryInput").addEventListener("change", renderArchive);
});

function buildCategories() {
  const categories = [...new Set(data.links.map((item) => item.category))].sort((a, b) => a.localeCompare(b, "zh-CN"));
  for (const category of categories) {
    const option = document.createElement("option");
    option.value = category;
    option.textContent = category;
    $("categoryInput").append(option);
  }
}

function renderStats() {
  $("siteCount").textContent = data.links.length;
  const categories = [...new Set(data.links.map((item) => item.category))];
  $("categoryBadges").replaceChildren(...categories.map((category) => {
    const badge = document.createElement("span");
    badge.textContent = category;
    return badge;
  }));
}

function renderArchive() {
  const query = $("searchInput").value.trim().toLowerCase();
  const category = $("categoryInput").value;
  const links = data.links.filter((item) => {
    const haystack = [item.title, item.category, item.description, item.url, item.repo].join(" ").toLowerCase();
    return (category === "全部" || item.category === category) && haystack.includes(query);
  });
  $("archiveGrid").replaceChildren(...links.map(renderCard));
}

function renderCard(item) {
  const node = document.createElement("article");
  node.className = "archive-card";
  node.innerHTML = `
    <span class="category">${escapeHtml(item.category)}</span>
    <div>
      <h3>${escapeHtml(item.title)}</h3>
      <p>${escapeHtml(item.description)}</p>
    </div>
    <div class="link-lines">
      <span>${escapeHtml(item.url)}</span>
      <span>${escapeHtml(item.repo)}</span>
    </div>
    <div class="card-actions">
      <a class="primary-link" href="${escapeAttr(item.url)}" target="_blank" rel="noreferrer">访问网站</a>
      <a class="secondary-link" href="${escapeAttr(item.repo)}" target="_blank" rel="noreferrer">查看源码</a>
    </div>
  `;
  return node;
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
