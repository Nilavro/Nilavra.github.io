---
---
(function () {
  const container = document.getElementById("external-news");
  if (!container) return;
  fetch("{{ '/data/research_news.json' | relative_url }}")
    .then(r => r.json())
    .then(items => {
      if (!Array.isArray(items) || !items.length) {
        container.innerHTML = "<p class='muted'>No external research-news items are available yet.</p>";
        return;
      }
      container.innerHTML = items.slice(0, 8).map(item => `
        <article class="news-card">
          <time>${item.source || "Research feed"}${item.date ? " · " + item.date : ""}</time>
          <h3><a href="${item.link}" target="_blank" rel="noopener">${item.title}</a></h3>
          <p>${item.summary || ""}</p>
        </article>`).join("");
    })
    .catch(() => {
      container.innerHTML = "<p class='muted'>External feed is not configured yet. Manual updates above still work.</p>";
    });
})();
