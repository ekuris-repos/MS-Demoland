/**
 * Primer Brand – Slide Deck Engine
 * Keyboard, button, and hash-based navigation for course slides.
 */
(function () {
  "use strict";

  let current = 0;
  let slides = [];
  let progressBar, counter, btnPrev, btnNext, tocOverlay;

  /* ---- Initialise ---- */
  function init() {
    slides = Array.from(document.querySelectorAll(".slide"));
    if (!slides.length) return;

    // Inject UI chrome
    injectUI();

    // Read initial slide from hash (#slide-3) or default to 0
    const hash = parseInt(location.hash.replace("#slide-", ""), 10);
    current = hash >= 1 && hash <= slides.length ? hash - 1 : 0;

    show(current);
    bindEvents();
    buildTOC();
  }

  /* ---- Inject navigation elements ---- */
  function injectUI() {
    // Progress bar
    progressBar = el("div", { className: "progress-bar" });
    document.body.prepend(progressBar);

    // Counter
    counter = el("div", { className: "slide-counter" });
    document.body.appendChild(counter);

    // Nav buttons
    const nav = el("div", { className: "slide-nav" });
    const btnHome = el("button", { innerHTML: "&#8962;", title: "Course Navigator (H)" });
    btnPrev = el("button", { innerHTML: "&#8592;", title: "Previous (←)" });
    btnNext = el("button", { innerHTML: "&#8594;", title: "Next (→)" });
    const btnToc = el("button", { innerHTML: "&#9776;", title: "Contents (T)" });
    nav.append(btnHome, btnPrev, btnNext, btnToc);
    document.body.appendChild(nav);

    btnHome.addEventListener("click", goHome);

    // TOC overlay
    tocOverlay = el("div", { className: "toc-overlay" });
    tocOverlay.innerHTML = '<div class="toc-panel"><h2>Contents</h2><ol id="toc-list"></ol></div>';
    document.body.appendChild(tocOverlay);

    btnPrev.addEventListener("click", prev);
    btnNext.addEventListener("click", next);
    btnToc.addEventListener("click", toggleTOC);
    tocOverlay.addEventListener("click", (e) => {
      if (e.target === tocOverlay) toggleTOC();
    });
  }

  /* ---- Show slide ---- */
  function show(index) {
    slides.forEach((s, i) => s.classList.toggle("active", i === index));
    current = index;
    updateUI();
    history.replaceState(null, "", `#slide-${current + 1}`);
  }

  function next() {
    if (current < slides.length - 1) show(current + 1);
  }
  function prev() {
    if (current > 0) show(current - 1);
  }
  function goTo(index) {
    if (index >= 0 && index < slides.length) {
      show(index);
      if (tocOverlay.classList.contains("active")) toggleTOC();
    }
  }

  /* ---- Update chrome ---- */
  function updateUI() {
    const pct = ((current + 1) / slides.length) * 100;
    progressBar.style.width = pct + "%";
    counter.textContent = `${current + 1} / ${slides.length}`;
    btnPrev.disabled = current === 0;
    btnNext.disabled = current === slides.length - 1;
  }

  /* ---- Build table of contents ---- */
  function buildTOC() {
    const list = document.getElementById("toc-list");
    if (!list) return;
    slides.forEach((s, i) => {
      const heading =
        s.querySelector("h1, h2")?.textContent || `Slide ${i + 1}`;
      const li = document.createElement("li");
      const a = document.createElement("a");
      a.href = "#";
      a.textContent = heading;
      a.addEventListener("click", (e) => {
        e.preventDefault();
        goTo(i);
      });
      li.appendChild(a);
      list.appendChild(li);
    });
  }

  function toggleTOC() {
    tocOverlay.classList.toggle("active");
  }

  /* ---- Navigate to course navigator ---- */
  function goHome() {
    // Navigate to the site root (index.html)
    const base = document.querySelector('link[href*="primer-brand.css"]');
    if (base) {
      const cssHref = new URL(base.href);
      window.location.href = cssHref.href.replace(/\/css\/primer-brand\.css.*$/, '/');
    } else {
      window.location.href = '/';
    }
  }

  /* ---- Keyboard ---- */
  function bindEvents() {
    document.addEventListener("keydown", (e) => {
      switch (e.key) {
        case "ArrowRight":
        case " ":
          e.preventDefault();
          next();
          break;
        case "ArrowLeft":
          e.preventDefault();
          prev();
          break;
        case "Home":
          e.preventDefault();
          goTo(0);
          break;
        case "End":
          e.preventDefault();
          goTo(slides.length - 1);
          break;
        case "t":
        case "T":
          if (!e.ctrlKey && !e.metaKey) toggleTOC();
          break;
        case "h":
        case "H":
          if (!e.ctrlKey && !e.metaKey) goHome();
          break;
        case "Escape":
          if (tocOverlay.classList.contains("active")) toggleTOC();
          break;
      }
    });

    // Touch swipe support
    let startX = 0;
    document.addEventListener("touchstart", (e) => {
      startX = e.changedTouches[0].screenX;
    });
    document.addEventListener("touchend", (e) => {
      const diff = e.changedTouches[0].screenX - startX;
      if (Math.abs(diff) > 60) {
        diff < 0 ? next() : prev();
      }
    });
  }

  /* ---- Helper ---- */
  function el(tag, props) {
    const node = document.createElement(tag);
    Object.assign(node, props);
    return node;
  }

  /* ---- Boot ---- */
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
