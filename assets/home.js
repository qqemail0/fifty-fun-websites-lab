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
