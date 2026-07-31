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
})();
