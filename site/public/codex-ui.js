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

  function labelGithubLink() {
    const links = Array.from(
      document.querySelectorAll('a[href*="github.com/TRUEMODELOFTHEWORLD/Charles-Proteus-Steinmetz-Texts-AI-Decoded"]')
    );
    links.forEach((link) => {
      if (link.querySelector('.codex-github-text')) return;
      link.classList.add('codex-github-label');
      const span = document.createElement('span');
      span.className = 'codex-github-text';
      span.textContent = 'TRUEMODELOFTHEWORLD';
      link.appendChild(span);
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
    shell.style.setProperty('--codex-reader-scale', String(Number.isFinite(savedScale) ? savedScale : 1));
    shell.innerHTML = [
      '<div class="reader-command-bar" data-layer="source">',
      '<div class="reader-title-block">',
      `<strong>${escapeHtml(title)}</strong>`,
      `<span>${escapeHtml([source, locationLabel].filter(Boolean).join(' · '))}</span>`,
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
      '<button type="button" data-reader-action="scan">Scan</button>',
      '<button type="button" data-reader-action="copy">Copy Link</button>',
      `<a href="${escapeHtml(assetUrl)}">Text Asset</a>`,
      '</div>',
      '<div class="reader-status-line" aria-live="polite"></div>',
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
    let activeMatch = -1;
    let renderTimer = 0;

    rawPane.textContent = sourceText.trim();
    ribbon.innerHTML = [
      `<span>${escapeHtml(status)}</span>`,
      `<span>${blocks.length.toLocaleString()} reading blocks</span>`,
      `<span>${countWords(sourceText).toLocaleString()} words</span>`,
      ...tags.slice(0, 8).map((tag) => `<span>${escapeHtml(tag)}</span>`)
    ].join('');

    function render() {
      const terms = queryTerms(input.value);
      const matchIds = [];
      documentPane.innerHTML = blocks.map((block, index) => {
        const matches = terms.length && blockMatches(block, terms);
        if (matches) matchIds.push(index);
        const blockClass = [
          'reader-block',
          `reader-block-${block.type}`,
          matches ? 'has-reader-match' : '',
          index === activeMatch ? 'is-active-match' : ''
        ].filter(Boolean).join(' ');
        const label = block.type === 'heading' ? 'Heading' : block.type === 'equation' ? 'Formula candidate' : 'Passage';
        const body = highlightText(block.text, terms);
        if (block.type === 'heading') {
          return `<section class="${blockClass}" id="${block.id}"><a class="reader-anchor" href="#${block.id}" aria-label="Link to ${label}">#</a><h3>${body}</h3></section>`;
        }
        if (block.type === 'equation') {
          return `<section class="${blockClass}" id="${block.id}"><a class="reader-anchor" href="#${block.id}" aria-label="Link to ${label}">#</a><pre>${body}</pre></section>`;
        }
        if (block.type === 'page-marker') {
          return `<section class="${blockClass}" id="${block.id}"><a class="reader-anchor" href="#${block.id}" aria-label="Link to page marker">#</a><p>${body}</p></section>`;
        }
        return `<section class="${blockClass}" id="${block.id}"><a class="reader-anchor" href="#${block.id}" aria-label="Link to passage">#</a><p>${body}</p></section>`;
      }).join('');

      const markCount = documentPane.querySelectorAll('mark.reader-highlight').length;
      const activeHuman = activeMatch >= 0 ? matchIds.indexOf(activeMatch) + 1 : 0;
      statusLine.textContent = terms.length
        ? `${markCount.toLocaleString()} highlighted term match${markCount === 1 ? '' : 'es'} in ${matchIds.length.toLocaleString()} passage${matchIds.length === 1 ? '' : 's'}${activeHuman > 0 ? ` · selected ${activeHuman} of ${matchIds.length}` : ''}.`
        : 'Readable mode gently unwraps OCR line breaks; Transcript mode preserves the raw candidate text.';
      shell._matchIds = matchIds;
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
        if (action === 'scan') {
          const scan = document.getElementById('original-scan-viewer');
          if (scan) {
            scan.open = true;
            scan.scrollIntoView({ behavior: 'smooth', block: 'start' });
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
    if (initialQuery) {
      window.setTimeout(() => jump(1), 180);
    }
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
    if (lines.length <= 3 && text.length < 160 && text === text.toUpperCase() && /[A-Z]/.test(text)) return 'heading';
    if (lines.length <= 6 && /[=≈≠≤≥+\-*/^√∑∫<>]| sin | cos | log | volts?| amperes?| ohms?/i.test(` ${text} `)) return 'equation';
    if (/^\d{1,4}$/.test(text) || /^[A-Z ,.'-]+\.\s+\d{1,4}$/.test(text)) return 'page-marker';
    return 'paragraph';
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

  document.addEventListener('DOMContentLoaded', () => {
    buildReaderControls();
    labelGithubLink();
    setupSourceTextLoaders();
    setupLightbox();
  });
})();
