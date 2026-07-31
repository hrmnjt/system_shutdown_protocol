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

  // Keep the full navigation visible without JavaScript, but collapse it on
  // phone-sized screens once enhancement is available.
  const contents = document.querySelector(".site-nav details");
  if (contents && window.matchMedia("(max-width: 760px)").matches) {
    contents.removeAttribute("open");
  }
})();
