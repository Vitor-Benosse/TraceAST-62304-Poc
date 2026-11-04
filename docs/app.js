document.addEventListener("DOMContentLoaded", function () {
  // 1. Mobile sidebar toggle
  const menuBtn = document.getElementById("mobile-menu-btn");
  const sidebar = document.getElementById("sidebar");
  if (menuBtn && sidebar) {
    menuBtn.addEventListener("click", function () {
      sidebar.classList.toggle("open");
    });
  }

  // Close mobile sidebar when clicking a nav link
  const navLinks = document.querySelectorAll(".nav-item a");
  navLinks.forEach(function (link) {
    link.addEventListener("click", function () {
      if (window.innerWidth <= 980 && sidebar) {
        sidebar.classList.remove("open");
      }
    });
  });

  // 2. Reading progress bar & active section spy
  const progressBar = document.getElementById("progress-bar");
  const sections = document.querySelectorAll(".doc-section");

  function updateScrollState() {
    const scrollTop = window.scrollY || document.documentElement.scrollTop;
    const docHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
    if (progressBar && docHeight > 0) {
      const pct = Math.min(100, Math.max(0, (scrollTop / docHeight) * 100));
      progressBar.style.width = pct + "%";
    }

    let currentId = "";
    sections.forEach(function (sec) {
      const top = sec.offsetTop - 130;
      if (scrollTop >= top) {
        currentId = sec.getAttribute("id");
      }
    });

    if (currentId) {
      navLinks.forEach(function (link) {
        const href = link.getAttribute("href");
        if (href === "#" + currentId) {
          link.classList.add("active");
        } else {
          link.classList.remove("active");
        }
      });
    }
  }

  window.addEventListener("scroll", updateScrollState);
  updateScrollState();

  // 3. Global documentation search (filters sections and nav items)
  const globalSearch = document.getElementById("global-search");
  const searchStats = document.getElementById("search-stats");
  if (globalSearch) {
    globalSearch.addEventListener("input", function () {
      const q = globalSearch.value.trim().toLowerCase();
      let visibleCount = 0;

      sections.forEach(function (sec) {
        if (!q) {
          sec.style.display = "";
          visibleCount++;
          return;
        }
        const text = sec.textContent.toLowerCase();
        if (text.indexOf(q) !== -1) {
          sec.style.display = "";
          visibleCount++;
        } else {
          sec.style.display = "none";
        }
      });

      if (searchStats) {
        if (!q) {
          searchStats.textContent = "Exibindo todas as 20 seções";
        } else {
          searchStats.textContent = visibleCount + " de 20 seções contêm \"" + globalSearch.value.trim() + "\"";
        }
      }
    });
  }

  // 4. Variable dictionary search (Section 5)
  const varSearch = document.getElementById("var-search");
  const varRows = document.querySelectorAll(".var-table-row");
  const varCountLabel = document.getElementById("var-count-label");
  if (varSearch && varRows.length > 0) {
    varSearch.addEventListener("input", function () {
      const q = varSearch.value.trim().toLowerCase();
      let shown = 0;
      varRows.forEach(function (row) {
        if (!q || row.textContent.toLowerCase().indexOf(q) !== -1) {
          row.style.display = "";
          shown++;
        } else {
          row.style.display = "none";
        }
      });
      if (varCountLabel) {
        varCountLabel.textContent = "Exibindo " + shown + " de " + varRows.length + " variáveis documentadas";
      }
    });
  }

  // 5. Searchable Glossary (Section 16)
  const glossarySearch = document.getElementById("glossary-search");
  const glossaryCards = document.querySelectorAll(".glossary-card");
  const glossaryCount = document.getElementById("glossary-count");
  if (glossarySearch && glossaryCards.length > 0) {
    glossarySearch.addEventListener("input", function () {
      const q = glossarySearch.value.trim().toLowerCase();
      let count = 0;
      glossaryCards.forEach(function (card) {
        if (!q || card.textContent.toLowerCase().indexOf(q) !== -1) {
          card.style.display = "";
          count++;
        } else {
          card.style.display = "none";
        }
      });
      if (glossaryCount) {
        glossaryCount.textContent = count + " de " + glossaryCards.length + " termos exibidos";
      }
    });
  }

  // 6. Add Copy button to all <pre> blocks
  const preBlocks = document.querySelectorAll("pre");
  preBlocks.forEach(function (pre) {
    const btn = document.createElement("button");
    btn.className = "copy-btn";
    btn.type = "button";
    btn.textContent = "Copiar";
    btn.addEventListener("click", function () {
      const codeEl = pre.querySelector("code");
      const rawText = codeEl ? codeEl.innerText : pre.innerText;
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(rawText).then(function () {
          btn.textContent = "Copiado!";
          setTimeout(function () {
            btn.textContent = "Copiar";
          }, 1800);
        });
      }
    });
    pre.appendChild(btn);
  });
});

