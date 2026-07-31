"use strict";

(() => {
  const root = document.documentElement;
  const copyMode = document.getElementById("copy-mode");
  const isOffline = window.location.protocol === "file:";
  const isDevelopment = ["localhost", "127.0.0.1", "::1"].includes(window.location.hostname);
  const runtime = isOffline ? "offline" : isDevelopment ? "development" : "web";

  root.dataset.runtime = runtime;
  if (copyMode) {
    copyMode.textContent =
      runtime === "offline"
        ? "Portable offline copy"
        : runtime === "development"
          ? "Development preview"
          : "Hosted web copy";
  }

  // Navigation remains available as a closed disclosure without JavaScript.
  // With enhancement, keep it expanded on larger screens and compact on phones.
  const contents = document.querySelector(".site-nav details");
  const phoneLayout = window.matchMedia("(max-width: 760px)");
  const syncNavigation = () => {
    if (!contents) return;
    contents.toggleAttribute("open", !phoneLayout.matches);
  };

  syncNavigation();
  phoneLayout.addEventListener("change", syncNavigation);

  // The complete index is generated into each protected handbook page. Search
  // makes no request, sends no query, and remains optional when JavaScript fails.
  const searchBox = document.querySelector(".site-search");
  const searchInput = document.getElementById("site-search-input");
  const searchResults = document.getElementById("search-results");
  const searchIndexElement = document.getElementById("search-index");

  if (!searchBox || !searchInput || !searchResults || !searchIndexElement) return;

  let pages;
  try {
    pages = JSON.parse(searchIndexElement.textContent || "[]");
  } catch {
    return;
  }
  if (!Array.isArray(pages) || pages.length === 0) return;

  const normalize = (value) =>
    String(value || "")
      .toLocaleLowerCase("en")
      .normalize("NFKD")
      .replace(/[\u0300-\u036f]/g, " ")
      .replace(/[^a-z0-9]+/g, " ")
      .trim();

  const searchablePages = pages.map((page) => ({
    ...page,
    normalizedTitle: normalize(`${page.title} ${page.linkTitle}`),
    normalizedDescription: normalize(page.description),
    normalizedContent: normalize(page.content),
  }));

  const clearResults = (message = "") => {
    searchResults.replaceChildren();
    if (message) {
      const status = document.createElement("p");
      status.textContent = message;
      searchResults.append(status);
    }
  };

  const renderResults = () => {
    const query = normalize(searchInput.value);
    if (query.length < 2) {
      clearResults();
      return;
    }

    const terms = query.split(/\s+/).filter(Boolean);
    const matches = searchablePages
      .map((page) => {
        if (!terms.every((term) => page.normalizedContent.includes(term) || page.normalizedTitle.includes(term) || page.normalizedDescription.includes(term))) {
          return null;
        }
        const score = terms.reduce((total, term) => {
          if (page.normalizedTitle.includes(term)) return total + 8;
          if (page.normalizedDescription.includes(term)) return total + 4;
          return total + 1;
        }, 0);
        return { page, score };
      })
      .filter(Boolean)
      .sort((a, b) => b.score - a.score || String(a.page.title).localeCompare(String(b.page.title)))
      .slice(0, 8);

    searchResults.replaceChildren();
    if (matches.length === 0) {
      clearResults("No matching section. Try fewer or broader words.");
      return;
    }

    const list = document.createElement("ul");
    for (const { page } of matches) {
      const item = document.createElement("li");
      const link = document.createElement("a");
      const title = document.createElement("strong");
      const description = document.createElement("span");

      link.className = "search-result";
      link.href = page.permalink;
      title.textContent = page.linkTitle || page.title;
      description.textContent = page.description || "Open this section";
      link.append(title, description);
      item.append(link);
      list.append(item);
    }
    searchResults.append(list);
  };

  searchBox.hidden = false;
  searchInput.addEventListener("input", renderResults);
  searchInput.addEventListener("keydown", (event) => {
    if (event.key === "Escape") {
      searchInput.value = "";
      clearResults();
      searchInput.blur();
    }
  });
})();
