(function () {
  function looksLikeFormula(text) {
    if (!text || text.length > 180) return false;
    if (/[=^_+\-*/()]/.test(text) && /[A-Za-z0-9]/.test(text)) return true;
    return /\b(sin|cos|tan|log|sqrt|pi|theta|lambda|omega|phi|impedance|reactance)\b/i.test(text);
  }

  function normalizeMath(text) {
    return text
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

  function renderExplicitMath() {
    if (!window.renderMathInElement) return;
    window.renderMathInElement(document.body, {
      delimiters: [
        { left: "$$", right: "$$", display: true },
        { left: "\\[", right: "\\]", display: true },
        { left: "\\(", right: "\\)", display: false }
      ],
      throwOnError: false,
      ignoredTags: ["script", "noscript", "style", "textarea", "pre"]
    });
  }

  function renderFormulaCode() {
    if (!window.katex) return;
    var mathContext = /\/mathematics\/|\/concepts\/|\/glossary\//.test(window.location.pathname);
    var candidates = document.querySelectorAll(
      ".equation-candidate-card code, .equation-source-summary code, .canonical-equation-table code, .math-formula-code"
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

  window.addEventListener("DOMContentLoaded", function () {
    renderExplicitMath();
    renderFormulaCode();
  });
})();
