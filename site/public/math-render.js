(function () {
  function looksLikeFormula(text) {
    if (!text || text.length > 180) return false;
    if (/[=^_+\-*/()]/.test(text) && /[A-Za-z0-9]/.test(text)) return true;
    return /\b(sin|cos|tan|log|sqrt|pi|theta|lambda|omega|phi|impedance|reactance)\b/i.test(text);
  }

  function decodeEntities(text) {
    var textarea = document.createElement("textarea");
    textarea.innerHTML = text || "";
    return textarea.value;
  }

  function stripMathDelimiters(text) {
    var value = decodeEntities(text).trim();
    if (value.startsWith("\\(") && value.endsWith("\\)")) return value.slice(2, -2).trim();
    if (value.startsWith("\\[") && value.endsWith("\\]")) return value.slice(2, -2).trim();
    if (value.startsWith("$$") && value.endsWith("$$")) return value.slice(2, -2).trim();
    if (value.startsWith("$") && value.endsWith("$")) return value.slice(1, -1).trim();
    return value;
  }

  function normalizeMath(text) {
    return stripMathDelimiters(text)
      .replace(/\bpi\b/gi, "\\pi")
      .replace(/\btheta\b/gi, "\\theta")
      .replace(/\blambda\b/gi, "\\lambda")
      .replace(/\bomega\b/gi, "\\omega")
      .replace(/\bphi\b/gi, "\\phi")
      .replace(/\bdeg\.?/gi, "^\\circ")
      .replace(/\bsin\b/gi, "\\sin")
      .replace(/\bcos\b/gi, "\\cos")
      .replace(/\btan\b/gi, "\\tan")
      .replace(/\blog\b/gi, "\\log")
      .replace(/\bsqrt\b/gi, "\\sqrt")
      .replace(/\be\.?m\.?f\.?/gi, "\\mathrm{e.m.f.}");
  }

  function renderExplicitMath(root) {
    if (!window.renderMathInElement) return false;
    window.renderMathInElement(root || document.body, {
      delimiters: [
        { left: "$$", right: "$$", display: true },
        { left: "$", right: "$", display: false },
        { left: "\\[", right: "\\]", display: true },
        { left: "\\(", right: "\\)", display: false }
      ],
      throwOnError: false,
      ignoredTags: ["script", "noscript", "style", "textarea", "pre"]
    });
    return true;
  }

  function renderEquationSpans(root) {
    if (!window.katex) return false;
    var nodes = (root || document).querySelectorAll(".equation-render:not([data-katex-rendered='true'])");
    Array.prototype.forEach.call(nodes, function (node) {
      var text = node.textContent || "";
      if (!text.trim()) return;
      try {
        window.katex.render(normalizeMath(text), node, {
          throwOnError: false,
          displayMode: false,
          strict: "ignore",
          trust: false
        });
        node.dataset.katexRendered = "true";
      } catch (_error) {
        node.dataset.katexRendered = "failed";
      }
    });
    return true;
  }

  function renderFormulaCode() {
    if (!window.katex) return;
    var mathContext = /\/mathematics\/|\/concepts\/|\/glossary\//.test(window.location.pathname);
    var candidates = document.querySelectorAll(
      ".equation-candidate-card code, .equation-source-summary code, .canonical-equation-table code, .math-formula-code, .formula-leads-table code, .concept-formula-table code"
    );

    if (mathContext) {
      document.querySelectorAll(".sl-markdown-content table code").forEach(function (node) {
        if (!node.closest("pre")) candidates = Array.prototype.concat.call(Array.prototype.slice.call(candidates), [node]);
      });
    }

    Array.prototype.forEach.call(candidates, function (node) {
      if (node.dataset.katexRendered === "true" || node.closest("pre")) return;
      var text = node.textContent.trim();
      if (!looksLikeFormula(text)) return;
      try {
        window.katex.render(normalizeMath(text), node, {
          throwOnError: false,
          displayMode: false,
          strict: "ignore",
          trust: false
        });
        node.dataset.katexRendered = "true";
        node.classList.add("katex-source-code");
      } catch (_error) {
        node.dataset.katexRendered = "failed";
      }
    });
  }

  function renderAllMath(root) {
    renderExplicitMath(root || document.body);
    renderEquationSpans(root || document);
    renderFormulaCode();
  }

  function scheduleMathRender() {
    renderAllMath(document);
    window.setTimeout(function () { renderAllMath(document); }, 120);
    window.setTimeout(function () { renderAllMath(document); }, 600);
  }

  window.addEventListener("DOMContentLoaded", scheduleMathRender);
  window.addEventListener("load", scheduleMathRender);
  document.addEventListener("astro:page-load", scheduleMathRender);
  document.addEventListener("starlight:search-result", scheduleMathRender);
})();

