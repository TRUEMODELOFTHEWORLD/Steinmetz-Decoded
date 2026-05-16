(function () {
  const root = document.documentElement;
  const storedMode = localStorage.getItem('codex-source-mode') || 'all';
  root.dataset.sourceMode = storedMode;

  function setMode(mode) {
    root.dataset.sourceMode = mode;
    localStorage.setItem('codex-source-mode', mode);
    document.querySelectorAll('[data-codex-mode]').forEach((button) => {
      button.setAttribute('aria-pressed', button.dataset.codexMode === mode ? 'true' : 'false');
    });
  }

  function findSidebarHost() {
    return (
      document.querySelector('.sidebar-content') ||
      document.querySelector('starlight-sidebar') ||
      document.querySelector('[data-has-sidebar] aside') ||
      document.querySelector('nav[aria-label="Main"]')?.parentElement ||
      document.querySelector('nav[aria-label="Sidebar"]')?.parentElement
    );
  }

  function buildReaderControls() {
    if (document.querySelector('.codex-reader-controls')) return;

    const panel = document.createElement('aside');
    panel.className = 'codex-reader-controls';
    panel.setAttribute('aria-label', 'Codex reader controls');
    panel.innerHTML = [
      '<p class="codex-reader-title">Reader Mode</p>',
      '<div class="codex-control-row" role="group" aria-label="Reading layer filter">',
      '<button type="button" data-codex-mode="all">All layers</button>',
      '<button type="button" data-codex-mode="steinmetz-only">Source only</button>',
      '</div>',
      '<details class="codex-sidebar-tools">',
      '<summary>Page tools</summary>',
      '<button type="button" class="codex-ask-toggle" aria-expanded="false">Ask this page</button>',
      '<label class="codex-translate">Translate',
      '<select aria-label="Translate this page">',
      '<option value="">Language</option>',
      '<option value="es">Spanish</option>',
      '<option value="fr">French</option>',
      '<option value="de">German</option>',
      '<option value="it">Italian</option>',
      '<option value="pt">Portuguese</option>',
      '<option value="ar">Arabic</option>',
      '<option value="hi">Hindi</option>',
      '<option value="zh-CN">Chinese</option>',
      '</select>',
      '</label>',
      '<form class="codex-ask-panel" hidden>',
      '<label>Ask using visible page text only',
      '<input name="q" type="search" autocomplete="off" placeholder="Try: hysteresis, ether, impedance" />',
      '</label>',
      '<div class="codex-ask-results" aria-live="polite"></div>',
      '</form>',
      '</details>'
    ].join('');

    const sidebarHost = findSidebarHost();
    if (sidebarHost) {
      sidebarHost.appendChild(panel);
    } else {
      document.body.appendChild(panel);
    }
    setMode(root.dataset.sourceMode || 'all');

    panel.querySelectorAll('[data-codex-mode]').forEach((button) => {
      button.addEventListener('click', () => setMode(button.dataset.codexMode));
    });

    const translate = panel.querySelector('.codex-translate select');
    translate.addEventListener('change', () => {
      if (!translate.value) return;
      const url = `https://translate.google.com/translate?sl=auto&tl=${encodeURIComponent(translate.value)}&u=${encodeURIComponent(location.href)}`;
      window.open(url, '_blank', 'noopener,noreferrer');
      translate.value = '';
    });

    const toggle = panel.querySelector('.codex-ask-toggle');
    const askPanel = panel.querySelector('.codex-ask-panel');
    toggle.addEventListener('click', () => {
      const isOpen = askPanel.hidden;
      askPanel.hidden = !isOpen;
      toggle.setAttribute('aria-expanded', String(isOpen));
      if (isOpen) askPanel.querySelector('input').focus();
    });

    setupAskPanel(askPanel);
  }

  function setupAskPanel(form) {
    const input = form.querySelector('input');
    const results = form.querySelector('.codex-ask-results');
    const contentRoot = document.querySelector('main') || document.body;

    function pageTextNodes() {
      return Array.from(contentRoot.querySelectorAll('p, li, td, blockquote, pre.source-text-loader, .source-text-loader'))
        .filter((node) => !node.closest('.codex-reader-controls'))
        .map((node) => node.textContent.replace(/\s+/g, ' ').trim())
        .filter((text) => text.length > 65);
    }

    function search() {
      const query = input.value.trim().toLowerCase();
      if (query.length < 2) {
        results.innerHTML = '<p>Type a term. Results are pulled only from this page.</p>';
        return;
      }

      const terms = query.split(/\s+/).filter(Boolean);
      const matches = pageTextNodes()
        .filter((text) => terms.every((term) => text.toLowerCase().includes(term)))
        .slice(0, 6);

      if (!matches.length) {
        results.innerHTML = '<p>No visible page passage matched that exact query.</p>';
        return;
      }

      results.innerHTML = matches
        .map((text) => `<p>${escapeHtml(text.length > 320 ? `${text.slice(0, 320)}...` : text)}</p>`)
        .join('');
    }

    input.addEventListener('input', search);
    form.addEventListener('submit', (event) => {
      event.preventDefault();
      search();
    });
  }

  function escapeHtml(value) {
    return value.replace(/[&<>"']/g, (char) => ({
      '&': '&amp;',
      '<': '&lt;',
      '>': '&gt;',
      '"': '&quot;',
      "'": '&#39;'
    })[char]);
  }

  function setupLightbox() {
    const images = Array.from(
      document.querySelectorAll(
        '.diagram-frame img, .codex-visual-card img, .home-portrait-card img, .home-portrait-grid img, .steinmetz-profile-media img'
      )
    );
    if (!images.length) return;

    const overlay = document.createElement('button');
    overlay.className = 'codex-lightbox';
    overlay.type = 'button';
    overlay.setAttribute('aria-label', 'Close diagram viewer');
    overlay.hidden = true;
    overlay.innerHTML = '<img alt="" />';
    document.body.appendChild(overlay);

    const overlayImage = overlay.querySelector('img');
    images.forEach((image) => {
      image.classList.add('codex-zoomable');
      image.addEventListener('click', () => {
        overlayImage.src = image.currentSrc || image.src;
        overlayImage.alt = image.alt || '';
        overlay.hidden = false;
        document.body.classList.add('codex-lightbox-open');
      });
    });

    overlay.addEventListener('click', () => {
      overlay.hidden = true;
      document.body.classList.remove('codex-lightbox-open');
    });

    document.addEventListener('keydown', (event) => {
      if (event.key === 'Escape') {
        overlay.hidden = true;
        document.body.classList.remove('codex-lightbox-open');
      }
    });
  }

  function setupProjectHeaderLinks() {
    const links = Array.from(
      document.querySelectorAll('a[href*="github.com/TRUEMODELOFTHEWORLD/Charles-Proteus-Steinmetz-Texts-AI-Decoded"], a[href*="github.com/TRUEMODELOFTHEWORLD/Steinmetz-Decoded"]')
    );
    links.forEach((link) => {
      if (link.closest('.codex-project-menu')) return;
      const host = link.parentElement;
      if (!host) return;

      const menu = document.createElement('div');
      menu.className = 'codex-project-menu';
      menu.innerHTML = [
        '<button class="codex-project-button" type="button" aria-expanded="false" aria-haspopup="true">',
        '<span class="codex-project-label">TRUEMODELOFTHEWORLD</span>',
        '<span class="codex-project-caret" aria-hidden="true">v</span>',
        '</button>',
        '<div class="codex-project-dropdown" role="menu">',
        '<a role="menuitem" href="https://github.com/TRUEMODELOFTHEWORLD/Steinmetz-Decoded">Steinmetz Decoded GitHub</a>',
        '<a role="menuitem" href="https://github.com/TRUEMODELOFTHEWORLD">TRUEMODELOFTHEWORLD GitHub</a>',
        '<a role="menuitem" href="https://pointsource.app">PointSource.app</a>',
        '<a role="menuitem" href="https://www.youtube.com/@TRUEMODELOFTHEWORLD">YouTube</a>',
        '</div>'
      ].join('');

      const contribute = document.createElement('a');
      contribute.className = 'codex-contribute-link';
      contribute.href = '/contribute/';
      contribute.textContent = 'Contribute';

      host.replaceChild(menu, link);
      if (!host.querySelector('.codex-contribute-link')) {
        menu.insertAdjacentElement('afterend', contribute);
      }

      const button = menu.querySelector('.codex-project-button');
      const dropdownLinks = Array.from(menu.querySelectorAll('.codex-project-dropdown a'));

      function setOpen(open) {
        menu.dataset.open = open ? 'true' : 'false';
        button.setAttribute('aria-expanded', String(open));
      }

      button.addEventListener('click', (event) => {
        event.stopPropagation();
        setOpen(menu.dataset.open !== 'true');
      });

      dropdownLinks.forEach((item) => {
        item.addEventListener('click', () => setOpen(false));
      });

      document.addEventListener('click', (event) => {
        if (!menu.contains(event.target)) setOpen(false);
      });

      document.addEventListener('keydown', (event) => {
        if (event.key === 'Escape') setOpen(false);
      });
    });
  }

  function setupSourceTextLoaders() {
    const loaders = Array.from(document.querySelectorAll('.source-text-loader[data-source-text-url]'));
    if (!loaders.length) return;

    loaders.forEach(async (loader) => {
      const url = loader.dataset.sourceTextUrl;
      if (!url) return;
      try {
        const response = await fetch(url);
        if (!response.ok) throw new Error(`HTTP ${response.status}`);
        const text = await response.text();
        renderSourceReader(loader, text || '[Source text asset is empty.]', url);
      } catch (error) {
        loader.textContent = `Could not load source text asset. Open it directly: ${url}`;
      }
    });
  }

  function renderSourceReader(loader, sourceText, assetUrl) {
    const blocks = buildReaderBlocks(sourceText);
    const title = loader.dataset.readerTitle || 'Source text';
    const source = loader.dataset.readerSource || '';
    const locationLabel = loader.dataset.readerLocation || '';
    const status = loader.dataset.readerStatus || 'candidate';
    const tags = (loader.dataset.readerTags || '').split('|').filter(Boolean);
    const urlSearch = new URLSearchParams(window.location.search);
    const initialQuery = urlSearch.get('q') || urlSearch.get('highlight') || urlSearch.get('term') || urlSearch.get('find') || '';
    const savedScale = Number(localStorage.getItem('codex-reader-scale') || '1');
    const shell = document.createElement('section');
    shell.className = 'codex-source-reader';
    shell.dataset.view = 'readable';
    shell.dataset.math = localStorage.getItem('codex-reader-math') || 'on';
    shell.dataset.artifacts = localStorage.getItem('codex-reader-artifacts') || 'hide';
    shell.style.setProperty('--codex-reader-scale', String(Number.isFinite(savedScale) ? savedScale : 1));
    shell.innerHTML = [
      '<div class="reader-command-bar" data-layer="source">',
      '<div class="reader-title-block">',
      `<strong>${escapeHtml(title)}</strong>`,
      `<span>${escapeHtml([source, locationLabel].filter(Boolean).join(' - '))}</span>`,
      '</div>',
      '<div class="reader-search">',
      '<label>Find in source text',
      `<input type="search" value="${escapeHtml(initialQuery)}" placeholder="ether, reactance, wave, field..." autocomplete="off" />`,
      '</label>',
      '<button type="button" data-reader-action="prev">Previous</button>',
      '<button type="button" data-reader-action="next">Next</button>',
      '<button type="button" data-reader-action="clear">Clear</button>',
      '</div>',
      '<div class="reader-view-controls" role="group" aria-label="Reader view controls">',
      '<button type="button" data-reader-view="readable" aria-pressed="true">Readable</button>',
      '<button type="button" data-reader-view="raw" aria-pressed="false">Transcript</button>',
      '<button type="button" data-reader-view="dense" aria-pressed="false">Dense</button>',
      '<button type="button" data-reader-action="smaller">A-</button>',
      '<button type="button" data-reader-action="larger">A+</button>',
      `<button type="button" data-reader-action="math" aria-pressed="${shell.dataset.math === 'on'}">Math</button>`,
      `<button type="button" data-reader-action="artifacts" aria-pressed="${shell.dataset.artifacts === 'show'}">OCR Fragments</button>`,
      '<button type="button" data-reader-action="scan">Scan</button>',
      '<button type="button" data-reader-action="copy">Copy Link</button>',
      '<button type="button" data-reader-action="copy-text">Copy Text</button>',
      '<button type="button" data-reader-action="citation">Cite</button>',
      `<a href="${escapeHtml(assetUrl)}">Text Asset</a>`,
      '</div>',
      '<div class="reader-status-line" aria-live="polite"></div>',
      '<div class="reader-progress-track" aria-hidden="true"><span></span></div>',
      '</div>',
      '<div class="reader-ribbon" data-layer="source"></div>',
      '<article class="reader-document" data-layer="source"></article>',
      '<pre class="reader-raw-transcript" data-layer="source"></pre>'
    ].join('');

    loader.classList.add('is-enhanced');
    loader.textContent = '';
    loader.appendChild(shell);

    const input = shell.querySelector('.reader-search input');
    const documentPane = shell.querySelector('.reader-document');
    const rawPane = shell.querySelector('.reader-raw-transcript');
    const statusLine = shell.querySelector('.reader-status-line');
    const ribbon = shell.querySelector('.reader-ribbon');
    const progressBar = shell.querySelector('.reader-progress-track span');
    let activeMatch = -1;
    let renderTimer = 0;

    rawPane.textContent = sourceText.trim();
    const artifactCount = blocks.filter((block) => block.type === 'artifact').length;
    ribbon.innerHTML = [
      `<span>${escapeHtml(status)}</span>`,
      `<span>${(blocks.length - artifactCount).toLocaleString()} reading blocks</span>`,
      artifactCount ? `<span>${artifactCount.toLocaleString()} OCR fragments hidden</span>` : '',
      `<span>${countWords(sourceText).toLocaleString()} words</span>`,
      ...tags.slice(0, 8).map((tag) => `<span>${escapeHtml(tag)}</span>`)
    ].join('');

    function render() {
      const terms = queryTerms(input.value);
      const showArtifacts = shell.dataset.artifacts === 'show';
      const matchIds = [];
      documentPane.innerHTML = blocks.map((block, index) => {
        const matches = terms.length && blockMatches(block, terms);
        if (block.type === 'artifact' && !showArtifacts && !matches) return '';
        if (matches) matchIds.push(index);
        const blockClass = [
          'reader-block',
          `reader-block-${block.type}`,
          matches ? 'has-reader-match' : '',
          index === activeMatch ? 'is-active-match' : ''
        ].filter(Boolean).join(' ');
        const label = block.type === 'heading' ? 'Heading' : block.type === 'equation' ? 'Formula candidate' : block.type === 'artifact' ? 'OCR fragment' : 'Passage';
        const body = highlightText(block.text, terms);
        if (block.type === 'heading') {
          return `<section class="${blockClass}" id="${block.id}"><a class="reader-anchor" href="#${block.id}" aria-label="Link to ${label}">#</a><h3>${body}</h3></section>`;
        }
        if (block.type === 'equation') {
          return `<section class="${blockClass}" id="${block.id}" data-formula-text="${escapeHtml(block.text)}"><a class="reader-anchor" href="#${block.id}" aria-label="Link to ${label}">#</a><div class="reader-math-panel" aria-label="KaTeX rendering of formula candidate"><span class="reader-math-label">KaTeX candidate</span><div class="reader-math-output"></div></div><pre class="reader-equation-transcript">${body}</pre></section>`;
        }
        if (block.type === 'page-marker') {
          return `<section class="${blockClass}" id="${block.id}"><a class="reader-anchor" href="#${block.id}" aria-label="Link to page marker">#</a><p>${body}</p></section>`;
        }
        if (block.type === 'artifact') {
          return `<section class="${blockClass}" id="${block.id}"><a class="reader-anchor" href="#${block.id}" aria-label="Link to ${label}">#</a><p>${body}</p></section>`;
        }
        return `<section class="${blockClass}" id="${block.id}"><a class="reader-anchor" href="#${block.id}" aria-label="Link to passage">#</a><p>${body}</p></section>`;
      }).join('');

      enhanceReaderMath(shell);

      const markCount = documentPane.querySelectorAll('mark.reader-highlight').length;
      const activeHuman = activeMatch >= 0 ? matchIds.indexOf(activeMatch) + 1 : 0;
      statusLine.textContent = terms.length
        ? `${markCount.toLocaleString()} highlighted term match${markCount === 1 ? '' : 'es'} in ${matchIds.length.toLocaleString()} passage${matchIds.length === 1 ? '' : 's'}${activeHuman > 0 ? ` - selected ${activeHuman} of ${matchIds.length}` : ''}.`
        : artifactCount
          ? `Readable mode unwraps OCR line breaks. ${artifactCount.toLocaleString()} OCR fragments are hidden; Transcript mode preserves everything.`
          : 'Readable mode unwraps OCR line breaks. Math mode renders formula candidates with KaTeX while preserving the raw OCR transcript for verification.';
      shell._matchIds = matchIds;
    }

    function updateReaderProgress() {
      if (!progressBar) return;
      const rect = shell.getBoundingClientRect();
      const viewport = window.innerHeight || document.documentElement.clientHeight || 1;
      const total = Math.max(1, rect.height - viewport);
      const read = Math.min(total, Math.max(0, -rect.top));
      progressBar.style.inlineSize = `${Math.round((read / total) * 100)}%`;
    }

    function scheduleRender() {
      clearTimeout(renderTimer);
      renderTimer = window.setTimeout(() => {
        activeMatch = -1;
        render();
      }, 80);
    }

    function jump(delta) {
      const matchIds = shell._matchIds || [];
      if (!matchIds.length) return;
      const currentPosition = matchIds.indexOf(activeMatch);
      const nextPosition = currentPosition < 0
        ? (delta > 0 ? 0 : matchIds.length - 1)
        : (currentPosition + delta + matchIds.length) % matchIds.length;
      activeMatch = matchIds[nextPosition];
      render();
      document.getElementById(blocks[activeMatch].id)?.scrollIntoView({ behavior: 'smooth', block: 'center' });
    }

    input.addEventListener('input', scheduleRender);
    window.addEventListener('scroll', updateReaderProgress, { passive: true });
    window.addEventListener('resize', updateReaderProgress);
    shell.querySelectorAll('[data-reader-view]').forEach((button) => {
      button.addEventListener('click', () => {
        shell.dataset.view = button.dataset.readerView;
        shell.querySelectorAll('[data-reader-view]').forEach((viewButton) => {
          viewButton.setAttribute('aria-pressed', String(viewButton === button));
        });
      });
    });

    shell.querySelectorAll('[data-reader-action]').forEach((button) => {
      button.addEventListener('click', async () => {
        const action = button.dataset.readerAction;
        if (action === 'prev') jump(-1);
        if (action === 'next') jump(1);
        if (action === 'clear') {
          input.value = '';
          scheduleRender();
          input.focus();
        }
        if (action === 'smaller' || action === 'larger') {
          const current = Number(shell.style.getPropertyValue('--codex-reader-scale') || '1');
          const next = Math.min(1.35, Math.max(0.85, current + (action === 'larger' ? 0.05 : -0.05)));
          shell.style.setProperty('--codex-reader-scale', String(next));
          localStorage.setItem('codex-reader-scale', String(next));
        }
        if (action === 'math') {
          shell.dataset.math = shell.dataset.math === 'on' ? 'off' : 'on';
          localStorage.setItem('codex-reader-math', shell.dataset.math);
          button.setAttribute('aria-pressed', String(shell.dataset.math === 'on'));
          statusLine.textContent = shell.dataset.math === 'on'
            ? 'Math rendering is on. Formula candidates remain tied to their raw OCR transcript.'
            : 'Math rendering is hidden. Raw OCR transcript remains visible.';
        }
        if (action === 'artifacts') {
          shell.dataset.artifacts = shell.dataset.artifacts === 'show' ? 'hide' : 'show';
          localStorage.setItem('codex-reader-artifacts', shell.dataset.artifacts);
          button.setAttribute('aria-pressed', String(shell.dataset.artifacts === 'show'));
          render();
          statusLine.textContent = shell.dataset.artifacts === 'show'
            ? 'OCR fragments are visible for audit.'
            : 'OCR fragments are hidden from the reading view and preserved in Transcript mode.';
        }
        if (action === 'scan') {
          const scan = document.getElementById('original-scan-viewer');
          if (scan) {
            scan.open = true;
            scan.scrollIntoView({ behavior: 'smooth', block: 'start' });
          }
        }
        if (action === 'copy-text') {
          try {
            await navigator.clipboard.writeText(sourceText.trim());
            statusLine.textContent = 'Source text copied.';
          } catch (_error) {
            statusLine.textContent = 'Copy was blocked by the browser. Select Transcript mode and copy manually.';
          }
        }
        if (action === 'citation') {
          const citation = [title, source, locationLabel, location.href].filter(Boolean).join(' - ');
          try {
            await navigator.clipboard.writeText(citation);
            statusLine.textContent = 'Citation stub copied.';
          } catch (_error) {
            statusLine.textContent = citation;
          }
        }
        if (action === 'copy') {
          const focused = activeMatch >= 0 ? `#${blocks[activeMatch].id}` : '#source-text-reader';
          const base = `${location.origin}${location.pathname}`;
          const query = input.value.trim() ? `?q=${encodeURIComponent(input.value.trim())}` : '';
          const link = `${base}${query}${focused}`;
          try {
            await navigator.clipboard.writeText(link);
            statusLine.textContent = 'Reader link copied.';
          } catch (_error) {
            statusLine.textContent = link;
          }
        }
      });
    });

    render();
    updateReaderProgress();
    if (initialQuery) {
      window.setTimeout(() => jump(1), 180);
    }
  }

  function enhanceReaderMath(shell) {
    if (!window.katex) return;
    const formulaBlocks = Array.from(shell.querySelectorAll('.reader-block-equation[data-formula-text]'));
    formulaBlocks.forEach((block) => {
      const raw = block.dataset.formulaText || '';
      const output = block.querySelector('.reader-math-output');
      if (!output) return;
      if (!likelyReaderFormula(raw)) {
        block.classList.add('is-weak-formula-candidate');
        output.textContent = 'Formula candidate needs scan review.';
        return;
      }
      try {
        window.katex.render(normalizeReaderFormula(raw), output, {
          throwOnError: false,
          displayMode: true,
          strict: 'ignore',
          trust: false
        });
        block.classList.add('has-rendered-math');
      } catch (_error) {
        block.classList.add('is-weak-formula-candidate');
        output.textContent = 'Formula candidate needs scan review.';
      }
    });
  }

  function likelyReaderFormula(text) {
    const value = (text || '').replace(/\s+/g, ' ').trim();
    if (value.length < 2 || value.length > 220) return false;
    const hasLetter = /[A-Za-z]/.test(value);
    const hasDigit = /\d/.test(value);
    const hasEquationSign = /[=\u2248\u2260\u2264\u2265]/.test(value);
    const operatorMatches = value.match(/[+\-*/^_(){}\[\]\u221a\u2211\u222b<>\u00b1]/g) || [];
    const hasMathWord = /\b(sin|cos|tan|log|sqrt|pi|theta|lambda|omega|phi)\b/i.test(value);
    const hasUnitOnly = /\b(voltage|current|impedance|reactance|amperes?|volts?|ohms?)\b/i.test(value) && !hasEquationSign && operatorMatches.length === 0;
    const mostlyWords = /^[A-Za-z ,.'-]+$/.test(value);
    if (looksLikeOcrArtifact(value) || hasUnitOnly || (mostlyWords && !hasMathWord)) return false;
    if (hasEquationSign && (hasLetter || hasDigit)) return true;
    if (hasMathWord && (hasLetter || hasDigit)) return true;
    return hasLetter && operatorMatches.length > 0 && value.length > 4;
  }

  function normalizeReaderFormula(text) {
    return (text || '')
      .replace(/[\u201c\u201d]/g, '"')
      .replace(/[\u2018\u2019]/g, "'")
      .replace(/\u2212/g, '-')
      .replace(/\bpi\b/gi, '\\pi')
      .replace(/\btheta\b/gi, '\\theta')
      .replace(/\blambda\b/gi, '\\lambda')
      .replace(/\bomega\b/gi, '\\omega')
      .replace(/\bphi\b/gi, '\\phi')
      .replace(/\bsin\b/gi, '\\sin')
      .replace(/\bcos\b/gi, '\\cos')
      .replace(/\btan\b/gi, '\\tan')
      .replace(/\blog\b/gi, '\\log')
      .replace(/\bsqrt\b/gi, '\\sqrt')
      .replace(/\be\.?m\.?f\.?/gi, '\\mathrm{e.m.f.}')
      .replace(/\bEo\b/g, 'E_0')
      .replace(/\bZo\b/g, 'Z_0')
      .replace(/\bIo\b/g, 'I_0')
      .trim();
  }

  function buildReaderBlocks(sourceText) {
    const normalized = sourceText
      .replace(/\r\n?/g, '\n')
      .replace(/\u00ad/g, '')
      .replace(/\f/g, '\n\n[page break]\n\n');
    const chunks = normalized.split(/\n{2,}/);
    const lineGroups = [];
    chunks.forEach((chunk) => {
      const lines = chunk.split('\n').map((line) => line.trim()).filter(Boolean);
      if (!lines.length) return;
      splitLongLineGroup(lines).forEach((group) => lineGroups.push(group));
    });
    return lineGroups.map((lines, index) => {
      const text = joinOcrLines(lines);
      return {
        id: `reader-block-${index + 1}`,
        type: classifyReaderBlock(lines, text),
        text,
        raw: lines.join('\n')
      };
    });
  }

  function splitLongLineGroup(lines) {
    if (lines.length <= 10) return [lines];
    const groups = [];
    let current = [];
    lines.forEach((line) => {
      current.push(line);
      const joinedLength = current.join(' ').length;
      const endsSentence = /[.!?;:)"']$/.test(line);
      if (current.length >= 5 && (endsSentence || joinedLength > 650)) {
        groups.push(current);
        current = [];
      }
    });
    if (current.length) groups.push(current);
    return groups;
  }

  function joinOcrLines(lines) {
    return lines.reduce((joined, line) => {
      if (!joined) return line;
      if (joined.endsWith('-') && /^[a-z]/i.test(line)) {
        return `${joined.slice(0, -1)}${line}`;
      }
      return `${joined} ${line}`;
    }, '').replace(/\s+/g, ' ').trim();
  }

  function classifyReaderBlock(lines, text) {
    if (/^\[page break\]$/i.test(text)) return 'page-marker';
    if (/^(lecture|chapter|section|part)\b/i.test(text) && text.length < 180) return 'heading';
    if (looksLikeOcrArtifact(text)) return 'artifact';
    const uppercaseHeadingWords = text.match(/[A-Z][A-Z.'-]{2,}/g) || [];
    if (lines.length <= 3 && text.length >= 12 && text.length < 160 && text === text.toUpperCase() && uppercaseHeadingWords.length >= 2) return 'heading';
    if (lines.length <= 6 && likelyReaderFormula(text)) return 'equation';
    if (/^\d{1,4}$/.test(text) || /^[A-Z ,.'-]+\.\s+\d{1,4}$/.test(text)) return 'page-marker';
    return 'paragraph';
  }

  function looksLikeOcrArtifact(text) {
    const value = (text || '').replace(/\s+/g, ' ').trim();
    if (!value) return true;
    if (/^\[page break\]$/i.test(value)) return false;
    if (value.length > 24) return false;
    const words = value.match(/[A-Za-z]{2,}/g) || [];
    const letters = value.match(/[A-Za-z]/g) || [];
    const digits = value.match(/\d/g) || [];
    if (/^[A-Z]$/.test(value) || /^[a-z]\.?$/.test(value)) return true;
    if (/^[^A-Za-z0-9]{1,12}$/.test(value)) return true;
    if (value.length <= 4 && words.length === 0 && !/[=]/.test(value)) return true;
    if (value.length <= 8 && words.length === 0 && letters.length <= 2 && digits.length <= 2 && !/[=]/.test(value)) return true;
    if (/^[A-Za-z]?[\^_'.;,;:|<>\\/+-]{1,8}$/.test(value)) return true;
    return false;
  }

  function countWords(text) {
    return (text.match(/\b[\w'-]+\b/g) || []).length;
  }

  function queryTerms(value) {
    return value
      .toLowerCase()
      .split(/\s+/)
      .map((term) => term.trim())
      .filter((term) => term.length > 1)
      .slice(0, 6);
  }

  function blockMatches(block, terms) {
    const haystack = block.text.toLowerCase();
    return terms.every((term) => haystack.includes(term));
  }

  function highlightText(value, terms) {
    if (!terms.length) return escapeHtml(value);
    const pattern = new RegExp(terms.map(escapeRegExp).join('|'), 'gi');
    let output = '';
    let lastIndex = 0;
    let match;
    while ((match = pattern.exec(value))) {
      output += escapeHtml(value.slice(lastIndex, match.index));
      output += `<mark class="reader-highlight">${escapeHtml(match[0])}</mark>`;
      lastIndex = match.index + match[0].length;
      if (match.index === pattern.lastIndex) pattern.lastIndex += 1;
    }
    output += escapeHtml(value.slice(lastIndex));
    return output;
  }

  function escapeRegExp(value) {
    return value.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  }


  function setupReadingProgress() {
    if (document.querySelector('.codex-progress-meter')) return;
    const meter = document.createElement('div');
    meter.className = 'codex-progress-meter';
    meter.setAttribute('aria-hidden', 'true');
    document.body.appendChild(meter);

    function update() {
      const doc = document.documentElement;
      const total = Math.max(1, doc.scrollHeight - window.innerHeight);
      const progress = Math.min(1, Math.max(0, window.scrollY / total));
      root.style.setProperty('--codex-progress', String(progress));
    }

    update();
    window.addEventListener('scroll', update, { passive: true });
    window.addEventListener('resize', update);
  }

  function setupReadingMemory() {
    const mainHeading = document.querySelector('h1')?.textContent?.trim() || document.title.replace(/\s+[-|].*$/, '');
    const isSourcePage = location.pathname.includes('/source-texts/');
    if (isSourcePage) {
      localStorage.setItem('codex-last-source', JSON.stringify({
        path: location.pathname + location.search,
        title: mainHeading,
        savedAt: Date.now()
      }));
      return;
    }

    let saved = null;
    try {
      saved = JSON.parse(localStorage.getItem('codex-last-source') || 'null');
    } catch (_error) {
      saved = null;
    }
    if (!saved || !saved.path || saved.path === location.pathname) return;
    if (Date.now() - Number(saved.savedAt || 0) > 1000 * 60 * 60 * 24 * 30) return;
    if (document.querySelector('.codex-continue-reading')) return;

    const link = document.createElement('a');
    link.className = 'codex-continue-reading';
    link.href = saved.path;
    link.innerHTML = `<strong>Continue reading</strong><span>${escapeHtml(saved.title || 'Last source text')}</span>`;
    document.body.appendChild(link);
  }

  function setupQuickJump() {
    const content = document.querySelector('.sl-markdown-content') || document.querySelector('main');
    if (!content || content.querySelector('.codex-quick-jump')) return;
    const headings = Array.from(content.querySelectorAll('h2[id], h3[id]'))
      .filter((heading) => heading.textContent.trim().length > 0)
      .slice(0, 8);
    if (headings.length < 3) return;

    const nav = document.createElement('nav');
    nav.className = 'codex-quick-jump';
    nav.setAttribute('aria-label', 'Page quick jump');
    nav.innerHTML = headings
      .map((heading) => `<a href="#${heading.id}">${escapeHtml(heading.textContent.trim().replace(/#$/, ''))}</a>`)
      .join('');

    const firstParagraph = content.querySelector('p, .home-codex-hero, .steinmetz-profile-hero, .coverage-hero');
    if (firstParagraph?.parentNode) {
      firstParagraph.parentNode.insertBefore(nav, firstParagraph.nextSibling);
    }
  }

  function setupKeyboardShortcuts() {
    document.addEventListener('keydown', (event) => {
      if (event.defaultPrevented || event.metaKey || event.ctrlKey || event.altKey) return;
      const target = event.target;
      const isTyping = target && ['INPUT', 'TEXTAREA', 'SELECT'].includes(target.tagName);
      if (isTyping) return;
      if (event.key === '/') {
        const sourceSearch = document.querySelector('.reader-search input');
        const siteSearch = document.querySelector('site-search button, [data-open-modal]');
        event.preventDefault();
        if (sourceSearch) sourceSearch.focus();
        else siteSearch?.click?.();
      }
      if (event.key.toLowerCase() === 'r') {
        document.querySelector('.codex-continue-reading')?.click();
      }
    });
  }

  document.addEventListener('DOMContentLoaded', () => {
    buildReaderControls();
    setupProjectHeaderLinks();
    setupSourceTextLoaders();
    setupLightbox();
    setupReadingProgress();
    setupReadingMemory();
    setupQuickJump();
    setupKeyboardShortcuts();
  });
})();
