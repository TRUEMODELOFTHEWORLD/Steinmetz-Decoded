import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';
import starlight from '@astrojs/starlight';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';

const SITE_URL = 'https://steinmetz-decoded.vercel.app';
const SITE_DESCRIPTION = 'A source-grounded public research archive for Charles Proteus Steinmetz: primary texts, electrical engineering history, AC theory, hysteresis, transients, equations, diagrams, and careful interpretation.';
const SITE_IMAGE = `${SITE_URL}/og-image.svg`;
const SITE_KEYWORDS = [
  'Charles Proteus Steinmetz',
  'C. P. Steinmetz',
  'Steinmetz Decoded',
  'Steinmetz archive',
  'Steinmetz writings',
  'alternating current theory',
  'AC power engineering',
  'hysteresis law',
  'Steinmetz equation',
  'transient electric phenomena',
  'symbolic method',
  'complex quantities',
  'phasor method',
  'impedance',
  'reactance',
  'admittance',
  'electric waves',
  'radiation light illumination',
  'lightning surges',
  'electrical engineering history',
  'Tesla era electrical science',
  'ether field language',
  'public domain electrical engineering texts'
];
const structuredData = [
  {
    '@context': 'https://schema.org',
    '@type': 'WebSite',
    '@id': `${SITE_URL}/#website`,
    name: 'Steinmetz Decoded',
    url: SITE_URL,
    description: SITE_DESCRIPTION,
    inLanguage: 'en-US',
    isAccessibleForFree: true,
    publisher: { '@id': `${SITE_URL}/#publisher` },
    about: { '@id': `${SITE_URL}/#charles-proteus-steinmetz` },
    keywords: SITE_KEYWORDS
  },
  {
    '@context': 'https://schema.org',
    '@type': 'Organization',
    '@id': `${SITE_URL}/#publisher`,
    name: 'TRUEMODELOFTHEWORLD',
    url: 'https://github.com/TRUEMODELOFTHEWORLD',
    sameAs: [
      'https://github.com/TRUEMODELOFTHEWORLD',
      'https://www.youtube.com/@TRUEMODELOFTHEWORLD',
      'https://pointsource.app/'
    ]
  },
  {
    '@context': 'https://schema.org',
    '@type': 'Person',
    '@id': `${SITE_URL}/#charles-proteus-steinmetz`,
    name: 'Charles Proteus Steinmetz',
    alternateName: ['C. P. Steinmetz', 'Charles P. Steinmetz'],
    birthDate: '1865-04-09',
    deathDate: '1923-10-26',
    jobTitle: 'Electrical engineer and mathematician',
    description: 'Electrical engineer foundational to alternating-current theory, hysteresis, transients, symbolic methods, and power-system engineering.',
    sameAs: [
      'https://en.wikipedia.org/wiki/Charles_Proteus_Steinmetz',
      'https://www.wikidata.org/wiki/Q62494'
    ]
  },
  {
    '@context': 'https://schema.org',
    '@type': 'CollectionPage',
    '@id': `${SITE_URL}/#archive`,
    name: 'Steinmetz Decoded Research Archive',
    url: SITE_URL,
    description: SITE_DESCRIPTION,
    about: { '@id': `${SITE_URL}/#charles-proteus-steinmetz` },
    isAccessibleForFree: true,
    genre: ['Electrical engineering history', 'Public domain text archive', 'Mathematics education', 'Research archive'],
    keywords: SITE_KEYWORDS,
    publisher: { '@id': `${SITE_URL}/#publisher` }
  },
  {
    '@context': 'https://schema.org',
    '@type': 'Dataset',
    '@id': `${SITE_URL}/#corpus`,
    name: 'Steinmetz Decoded Public Research Corpus',
    url: `${SITE_URL}/source-texts/`,
    description: 'A public corpus of processed Charles Proteus Steinmetz source texts, chapter readers, concept dossiers, equation atlases, diagram galleries, and research metadata.',
    about: { '@id': `${SITE_URL}/#charles-proteus-steinmetz` },
    creator: { '@id': `${SITE_URL}/#publisher` },
    isAccessibleForFree: true,
    keywords: SITE_KEYWORDS,
    distribution: [
      {
        '@type': 'DataDownload',
        encodingFormat: 'application/json',
        contentUrl: `${SITE_URL}/data/manifest.json`
      }
    ]
  },
  {
    '@context': 'https://schema.org',
    '@type': 'ItemList',
    '@id': `${SITE_URL}/#research-entrypoints`,
    name: 'Steinmetz Decoded research entry points',
    itemListElement: [
      ['Start Reading', '/start-reading/'],
      ['Steinmetz Research Topic Map', '/steinmetz-research-topics/'],
      ['Who Was Steinmetz?', '/who-was-steinmetz/'],
      ['Source Text Browser', '/source-texts/'],
      ['Book Coverage', '/book-coverage/'],
      ['Concept Encyclopedia', '/concepts/'],
      ['Equation Atlas', '/mathematics/equation-atlas/'],
      ['Visual Topic Galleries', '/diagrams/visual-topic-galleries/'],
      ['Hysteresis', '/concepts/hysteresis/'],
      ['Transient Phenomena', '/concepts/transient-phenomena/'],
      ['Symbolic Method', '/concepts/symbolic-method/'],
      ['Ether References', '/concepts/ether/']
    ].map(([name, url], index) => ({
      '@type': 'ListItem',
      position: index + 1,
      name,
      url: `${SITE_URL}${url}`
    }))
  }
];


export default defineConfig({
  site: SITE_URL,
  integrations: [
    starlight({
      title: 'Steinmetz Decoded',
      description: 'A source-grounded research codex for Charles Proteus Steinmetz.',
      customCss: ['./src/styles/custom.css', 'katex/dist/katex.min.css'],
      head: [
        {
          tag: 'script',
          attrs: {
            src: '/codex-ui.js',
            defer: true
          }
        },
        {
          tag: 'script',
          attrs: {
            src: '/vendor/katex/katex.min.js',
            defer: true
          }
        },
        {
          tag: 'script',
          attrs: {
            src: '/vendor/katex/auto-render.min.js',
            defer: true
          }
        },
        {
          tag: 'script',
          attrs: {
            src: '/math-render.js',
            defer: true
          }
        },
        {
          tag: 'meta',
          attrs: {
            name: 'theme-color',
            content: '#151b1c'
          }
        },
        {
          tag: 'meta',
          attrs: {
            name: 'keywords',
            content: SITE_KEYWORDS.join(', ')
          }
        },
        {
          tag: 'meta',
          attrs: {
            name: 'author',
            content: 'TRUEMODELOFTHEWORLD and open contributors'
          }
        },
        {
          tag: 'meta',
          attrs: {
            name: 'creator',
            content: 'TRUEMODELOFTHEWORLD'
          }
        },
        {
          tag: 'meta',
          attrs: {
            name: 'publisher',
            content: 'TRUEMODELOFTHEWORLD'
          }
        },
        {
          tag: 'meta',
          attrs: {
            name: 'robots',
            content: 'index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1'
          }
        },
        {
          tag: 'meta',
          attrs: {
            name: 'googlebot',
            content: 'index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1'
          }
        },
        {
          tag: 'meta',
          attrs: {
            property: 'og:site_name',
            content: 'Steinmetz Decoded'
          }
        },
        {
          tag: 'meta',
          attrs: {
            property: 'og:type',
            content: 'website'
          }
        },
        {
          tag: 'meta',
          attrs: {
            property: 'og:title',
            content: 'Steinmetz Decoded: Charles Proteus Steinmetz Research Archive'
          }
        },
        {
          tag: 'meta',
          attrs: {
            property: 'og:description',
            content: SITE_DESCRIPTION
          }
        },
        {
          tag: 'meta',
          attrs: {
            property: 'og:url',
            content: SITE_URL
          }
        },
        {
          tag: 'meta',
          attrs: {
            name: 'twitter:card',
            content: 'summary_large_image'
          }
        },
        {
          tag: 'meta',
          attrs: {
            name: 'twitter:title',
            content: 'Steinmetz Decoded'
          }
        },
        {
          tag: 'meta',
          attrs: {
            name: 'twitter:description',
            content: SITE_DESCRIPTION
          }
        },
        {
          tag: 'meta',
          attrs: {
            property: 'og:image',
            content: SITE_IMAGE
          }
        },
        {
          tag: 'meta',
          attrs: {
            name: 'twitter:image',
            content: SITE_IMAGE
          }
        },
        {
          tag: 'link',
          attrs: {
            rel: 'manifest',
            href: '/site.webmanifest'
          }
        },

        {
          tag: 'script',
          attrs: {
            type: 'application/ld+json'
          },
          content: JSON.stringify(structuredData)
        }
      ],
      social: [
        {
          icon: 'github',
          label: 'GitHub',
          href: 'https://github.com/TRUEMODELOFTHEWORLD/Steinmetz-Decoded'
        }
      ],
      sidebar: [
        {
          label: 'Start Reading',
          items: [
            { label: 'Start Reading', slug: 'start-reading' },
            { label: 'Complete Archive Map', slug: 'archive-navigator' },
            { label: 'Who Was Steinmetz?', slug: 'who-was-steinmetz' },
            { label: 'Why He Matters', slug: 'why-steinmetz-matters' },
            { label: 'Guided Routes', slug: 'reading-routes' },
            { label: 'First Source Text', slug: 'source-texts/radiation-light-and-illumination/lecture-01' },
            { label: 'First Deep Decoding', slug: 'sources/radiation-light-and-illumination/lecture-01' },
            { label: 'Research Map', slug: 'research-map' },
            { label: 'Contribute', slug: 'contribute' }
          ]
        },
        {
          label: 'Books And Sources',
          items: [
            { label: 'Browse Books', slug: 'book-coverage' },
            { label: 'Read Source Texts (410)', slug: 'source-texts' },
            { label: 'Section Workbenches (410)', slug: 'chapter-workbench' },
            { label: 'Radiation, Light and Illumination', slug: 'book-coverage/radiation-light-and-illumination' },
            { label: 'Elementary Lectures', slug: 'book-coverage/elementary-lectures-electric-discharges-waves-impulses' },
            { label: 'Electric Discharges 1914', slug: 'book-coverage/electric-discharges-waves-impulses-1914' },
            { label: 'Engineering Mathematics', slug: 'book-coverage/engineering-mathematics' },
            { label: 'Alternating Current Phenomena', slug: 'book-coverage/theory-calculation-alternating-current-phenomena' },
            { label: 'AC Phenomena 1897', slug: 'book-coverage/theory-calculation-alternating-current-phenomena-1897' },
            { label: 'AC Phenomena 1900', slug: 'book-coverage/theory-calculation-alternating-current-phenomena-1900' },
            { label: 'Transient Electric Phenomena', slug: 'book-coverage/theory-calculation-transient-electric-phenomena-oscillations' },
            { label: 'Theoretical Elements', slug: 'book-coverage/theoretical-elements-electrical-engineering' },
            { label: 'General Lectures', slug: 'book-coverage/general-lectures-electrical-engineering' },
            { label: 'Electric Apparatus', slug: 'book-coverage/theory-calculation-electric-apparatus' },
            { label: 'Electric Circuits', slug: 'book-coverage/theory-calculation-electric-circuits' },
            { label: 'America and the New Epoch', slug: 'book-coverage/america-and-new-epoch' },
            { label: 'Relativity and Space', slug: 'book-coverage/four-lectures-relativity-space' },
            { label: 'Commonwealth Edison Trouble', slug: 'book-coverage/commonwealth-edison-generating-system-trouble' },
            { label: 'Source Library', slug: 'source-library' },
            { label: 'Corpus Completion Dossiers', slug: 'source-library/corpus-completion' },
            { label: 'Patent Register', slug: 'sources/steinmetz-patents' }
          ]
        },
        {
          label: 'Core Concepts',
          items: [
            { label: 'Concept Encyclopedia', slug: 'concepts' },
            { label: 'Radiation', slug: 'concepts/radiation' },
            { label: 'Electric Waves', slug: 'concepts/electric-waves' },
            { label: 'Ether', slug: 'concepts/ether' },
            { label: 'Transient Phenomena', slug: 'concepts/transient-phenomena' },
            { label: 'Symbolic Method', slug: 'concepts/symbolic-method' },
            { label: 'Complex Quantities', slug: 'concepts/complex-quantities' },
            { label: 'Hysteresis', slug: 'concepts/hysteresis' },
            { label: 'Impedance', slug: 'concepts/impedance' },
            { label: 'Reactance', slug: 'concepts/reactance' },
            { label: 'Admittance', slug: 'concepts/admittance' },
            { label: 'Lightning And Surges', slug: 'concepts/lightning-surges' },
            { label: 'Illumination', slug: 'concepts/illumination' },
            { label: 'Power Factor', slug: 'concepts/power-factor' },
            { label: 'Dielectric Loss', slug: 'concepts/dielectric-loss' },
            { label: 'Distributed Constants', slug: 'concepts/distributed-constants' },
            { label: 'Dossier Index', slug: 'concepts/dossier-index' },
            { label: 'Concept Concordance (78)', slug: 'concept-concordance' }
          ]
        },
        {
          label: 'Math And Tools',
          items: [
            { label: 'Equation Atlas', slug: 'mathematics/equation-atlas' },
            { label: 'Equation Catalog', slug: 'mathematics' },
            { label: 'First Canonical Set', slug: 'mathematics/canonical-equation-canon' },
            { label: 'Interactive Tools', slug: 'tools' },
            { label: 'Impedance And Reactance', slug: 'mathematics/equations/impedance-reactance' },
            { label: 'Admittance', slug: 'mathematics/equations/admittance-conductance-susceptance' },
            { label: 'Hysteresis Law', slug: 'mathematics/equations/steinmetz-hysteresis-law' },
            { label: 'Transient Term', slug: 'mathematics/equations/transient-term' },
            { label: 'RLC Oscillation', slug: 'mathematics/equations/rlc-oscillation' },
            { label: 'Source Formula Maps (16)', slug: 'mathematics/source-formula-maps' }
          ]
        },
        {
          label: 'Visuals And Diagrams',
          items: [
            { label: 'Visual Topic Galleries', slug: 'diagrams/visual-topic-galleries' },
            { label: 'Diagram Archive', slug: 'diagrams' },
            { label: 'Source Visual Maps (16)', slug: 'diagrams/source-visuals' },
            { label: 'Recreated Visual Index', slug: 'diagrams/recreated-visual-index' },
            { label: 'Original RLI Figures', slug: 'diagrams/original-radiation-light-and-illumination' },
            { label: 'Original AC Figures', slug: 'diagrams/original-alternating-current-phenomena' },
            { label: 'Original Transient Figures', slug: 'diagrams/original-transient-electric-phenomena' },
            { label: 'Extracted Visual Candidates (8)', slug: 'diagrams/extracted-visual-candidates' },
            { label: 'Figure Candidate Atlas', slug: 'diagrams/figure-candidate-atlas' }
          ]
        },
        {
          label: 'Language And Comparisons',
          items: [
            { label: 'Glossary', slug: 'glossary' },
            { label: 'Comparison Index', slug: 'comparisons' },
            { label: 'Steinmetz vs Modern EE', slug: 'comparisons/steinmetz-vs-modern-radiation' },
            { label: 'Modern AC Method', slug: 'comparisons/steinmetz-vs-modern-ac-symbolic-method' },
            { label: 'Tesla-Era Science', slug: 'comparisons/tesla-era-electrical-science' },
            { label: 'Tesla-Era Transients', slug: 'comparisons/transients-tesla-era-high-frequency' },
            { label: 'Ether-Field Reading Guide', slug: 'comparisons/ether-field-reading-guide' },
            { label: 'Hidden Gems', slug: 'hidden-gems' },
            { label: 'Research Questions', slug: 'research-questions' }
          ]
        },
        {
          label: 'Research Operations And Data',
          items: [
            { label: 'Complete Archive Navigator', slug: 'archive-navigator' },
            { label: 'Operations Hub', slug: 'research-operations' },
            { label: 'Source Dashboards', slug: 'source-library/source-research-dashboards' },
            { label: 'Chapter Workbench (410)', slug: 'chapter-workbench' },
            { label: 'Passage Atlas', slug: 'passage-atlas' },
            { label: 'Theme Evidence Atlas', slug: 'theme-evidence' },
            { label: 'Evidence Ledger', slug: 'source-library/evidence-ledger' },
            { label: 'Corpus Completion Matrix', slug: 'source-library/corpus-completion' },
            { label: 'Completion Audit', slug: 'roadmap/completion-audit' },
            { label: 'Canonical Review', slug: 'roadmap/canonical-review-workflow' },
            { label: 'Canonical Verification', slug: 'roadmap/canonical-verification-workbench' },
            { label: 'Citation And Data Export', slug: 'roadmap/citation-and-data-export' },
            { label: 'Publication Roadmap', slug: 'roadmap' },
            { label: 'Research Codex Engine', slug: 'roadmap/research-codex-engine' },
            { label: 'Public Discoverability', slug: 'roadmap/discoverability' }
          ]
        }
      ]
    }),
    mdx()
  ],
  markdown: {
    remarkPlugins: [remarkMath],
    rehypePlugins: [rehypeKatex]
  }
});
