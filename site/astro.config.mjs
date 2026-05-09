import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';
import starlight from '@astrojs/starlight';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';

export default defineConfig({
  site: 'https://truemodeloftheworld.github.io',
  base: '/Charles-Proteus-Steinmetz-Texts-AI-Decoded',
  integrations: [
    starlight({
      title: 'Steinmetz Decoded',
      description: 'A source-grounded research codex for Charles Proteus Steinmetz.',
      customCss: ['./src/styles/custom.css', 'katex/dist/katex.min.css'],
      head: [
        {
          tag: 'script',
          attrs: {
            src: '/Charles-Proteus-Steinmetz-Texts-AI-Decoded/codex-ui.js',
            defer: true
          }
        },
        {
          tag: 'meta',
          attrs: {
            name: 'theme-color',
            content: '#151b1c'
          }
        }
      ],
      social: [
        {
          icon: 'github',
          label: 'GitHub',
          href: 'https://github.com/TRUEMODELOFTHEWORLD/Charles-Proteus-Steinmetz-Texts-AI-Decoded'
        }
      ],
      sidebar: [
        {
          label: 'Start Here',
          items: [
            { label: 'Start Reading', slug: 'start-reading' },
            { label: 'Research Map', slug: 'research-map' },
            { label: 'Source Library', slug: 'source-library' },
            { label: 'Browse Books', slug: 'book-coverage' },
            { label: 'Visual Topic Galleries', slug: 'diagrams/visual-topic-galleries' },
            { label: 'Equation Atlas', slug: 'mathematics/equation-atlas' },
            { label: 'Interactive Tools', slug: 'tools' },
            { label: 'Study Curriculum', slug: 'research-map/study-curriculum' },
            { label: 'Who Was Steinmetz?', slug: 'who-was-steinmetz' },
            { label: 'Why Steinmetz Matters', slug: 'why-steinmetz-matters' },
            { label: 'Project Tracker', slug: 'project-tracker' }
          ]
        },
        {
          label: 'Read The Corpus',
          items: [
            { label: 'Source Library', slug: 'source-library' },
            { label: 'Source Dashboards', slug: 'source-library/source-research-dashboards' },
            { label: 'Browse Books', slug: 'book-coverage' },
            { label: 'Guided Reading Routes', slug: 'reading-routes' },
            { label: 'Source Text Browser', slug: 'source-texts' },
            { label: 'Chapter Workbench', slug: 'chapter-workbench' },
            { label: 'Passage Atlas', slug: 'passage-atlas' },
            { label: 'Concept Concordance', slug: 'concept-concordance' },
            { label: 'Theme Evidence Atlas', slug: 'theme-evidence' },
            { label: 'Source Formula Maps', slug: 'mathematics/source-formula-maps' },
            { label: 'Source Visual Maps', slug: 'diagrams/source-visuals' },
            { label: 'Evidence Ledger', slug: 'source-library/evidence-ledger' },
            { label: 'Chapter Atlas', slug: 'source-library/chapter-atlas' },
            { label: 'Corpus Completion Matrix', slug: 'source-library/corpus-completion' },
            { label: 'Critical Source Frontier', slug: 'source-library/corpus-completion/critical-frontier' },
            { label: 'Processing Dashboard', slug: 'research-status' },
            { label: 'Bibliography Intake', slug: 'source-library/bibliography-intake' },
            { label: 'Official Source Expansion', slug: 'source-library/official-source-expansion' },
            {
              label: 'Steinmetz Patents',
              items: [
                { label: 'Patent Register', slug: 'sources/steinmetz-patents' },
                { label: 'Seeded Patent Dossiers', slug: 'sources/steinmetz-patents/seeded-patent-dossiers' }
              ]
            }
          ]
        },
        {
          label: 'Books: Browse And Read',
          items: [
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
            { label: 'Commonwealth Edison Trouble', slug: 'book-coverage/commonwealth-edison-generating-system-trouble' }
          ]
        },
        {
          label: 'Deep Decoding Paths',
          items: [
            { label: 'RLI Lecture I', slug: 'sources/radiation-light-and-illumination/lecture-01' },
            { label: 'The Electric Field', slug: 'sources/elementary-lectures-electric-discharges-waves-impulses/electric-field' },
            { label: 'General Number', slug: 'sources/engineering-mathematics/general-number' },
            { label: 'Symbolic Method', slug: 'sources/theory-calculation-alternating-current-phenomena/symbolic-method' },
            { label: 'Impedance And Reactance', slug: 'sources/theory-calculation-alternating-current-phenomena/impedance-reactance' },
            { label: 'Admittance', slug: 'sources/theory-calculation-alternating-current-phenomena/admittance-conductance-susceptance' },
            { label: 'Transient Terms', slug: 'sources/theory-calculation-transient-electric-phenomena-oscillations/transient-terms' },
            { label: 'Condenser Charge', slug: 'sources/theory-calculation-transient-electric-phenomena-oscillations/condenser-charge-discharge' },
            { label: 'Standing And Traveling Waves', slug: 'sources/theory-calculation-transient-electric-phenomena-oscillations/standing-traveling-waves' },
            { label: 'Fields of Force', slug: 'sources/theoretical-elements-electrical-engineering/fields-of-force' },
            { label: 'Hysteresis And Effective Resistance', slug: 'sources/theoretical-elements-electrical-engineering/hysteresis-effective-resistance' },
            { label: 'High-Frequency Surges', slug: 'sources/general-lectures-electrical-engineering/high-frequency-oscillations-surges' },
            { label: 'Hysteresis Motor', slug: 'sources/theory-calculation-electric-apparatus/hysteresis-motor' },
            { label: 'Industrial Government', slug: 'sources/america-and-new-epoch/industrial-government' },
            { label: 'Gravitational Field', slug: 'sources/four-lectures-relativity-space/gravitational-field' },
            { label: 'Reactors And Synchronism', slug: 'sources/commonwealth-edison-generating-system-trouble/power-limiting-reactors-synchronism' }
          ]
        },
        {
          label: 'Concept Encyclopedia',
          items: [
            { label: 'Concept Index', slug: 'concepts' },
            { label: 'Dossier Index', slug: 'concepts/dossier-index' },
            { label: 'Radiation', slug: 'concepts/radiation' },
            { label: 'Electric Waves', slug: 'concepts/electric-waves' },
            { label: 'Lightning And Surges', slug: 'concepts/lightning-surges' },
            { label: 'Ether', slug: 'concepts/ether' },
            { label: 'Illumination', slug: 'concepts/illumination' },
            { label: 'Transient Phenomena', slug: 'concepts/transient-phenomena' },
            { label: 'Symbolic Method', slug: 'concepts/symbolic-method' },
            { label: 'Complex Quantities', slug: 'concepts/complex-quantities' },
            { label: 'Hysteresis', slug: 'concepts/hysteresis' },
            { label: 'Harmonics And Wave Shape', slug: 'concepts/harmonics-wave-shape' },
            { label: 'Impedance', slug: 'concepts/impedance' },
            { label: 'Reactance', slug: 'concepts/reactance' },
            { label: 'Admittance', slug: 'concepts/admittance' },
            { label: 'Conductance', slug: 'concepts/conductance' },
            { label: 'Susceptance', slug: 'concepts/susceptance' },
            { label: 'Power Factor', slug: 'concepts/power-factor' },
            { label: 'Dielectric Loss', slug: 'concepts/dielectric-loss' },
            { label: 'Distributed Constants', slug: 'concepts/distributed-constants' },
            { label: 'Oscillation And Damping', slug: 'concepts/oscillation-damping' },
            { label: 'Inductance And Capacity', slug: 'concepts/inductance-capacity' },
            { label: 'Power-Limiting Reactors', slug: 'concepts/power-limiting-reactors' },
            { label: 'Synchronizing Power', slug: 'concepts/synchronizing-power' }
          ]
        },
        {
          label: 'Mathematics And Tools',
          items: [
            { label: 'Equation Catalog', slug: 'mathematics' },
            { label: 'Equation Atlas', slug: 'mathematics/equation-atlas' },
            { label: 'Source Formula Maps', slug: 'mathematics/source-formula-maps' },
            { label: 'First Canonical Set', slug: 'mathematics/canonical-equation-canon' },
            { label: 'Velocity, Frequency, Wavelength', slug: 'mathematics/equations/velocity-frequency-wavelength' },
            { label: 'Symbolic Components', slug: 'mathematics/equations/symbolic-rectangular-components' },
            { label: 'Operator j', slug: 'mathematics/equations/symbolic-operator-j' },
            { label: 'Reactance Forms', slug: 'mathematics/equations/reactance-forms' },
            { label: 'Impedance And Reactance', slug: 'mathematics/equations/impedance-reactance' },
            { label: 'Admittance', slug: 'mathematics/equations/admittance-conductance-susceptance' },
            { label: 'Power And Effective Resistance', slug: 'mathematics/equations/power-effective-resistance' },
            { label: 'Capacity Susceptance', slug: 'mathematics/equations/capacity-susceptance' },
            { label: 'Hysteresis Law', slug: 'mathematics/equations/steinmetz-hysteresis-law' },
            { label: 'Transient Term', slug: 'mathematics/equations/transient-term' },
            { label: 'RLC Oscillation', slug: 'mathematics/equations/rlc-oscillation' },
            { label: 'Condenser Oscillation', slug: 'mathematics/equations/condenser-oscillation-decrement' },
            { label: 'Synchronizing Power', slug: 'mathematics/equations/synchronizing-power-commonwealth' },
            { label: 'Interactive Tools', slug: 'tools' }
          ]
        },
        {
          label: 'Visual And Language Archive',
          items: [
            { label: 'Diagram Archive', slug: 'diagrams' },
            { label: 'Visual Topic Galleries', slug: 'diagrams/visual-topic-galleries' },
            { label: 'Figure Candidate Atlas', slug: 'diagrams/figure-candidate-atlas' },
            { label: 'Source Visual Maps', slug: 'diagrams/source-visuals' },
            { label: 'Recreated Visual Index', slug: 'diagrams/recreated-visual-index' },
            { label: 'Original RLI Figures', slug: 'diagrams/original-radiation-light-and-illumination' },
            { label: 'Original AC Figures', slug: 'diagrams/original-alternating-current-phenomena' },
            { label: 'Original Transient Figures', slug: 'diagrams/original-transient-electric-phenomena' },
            { label: 'Glossary', slug: 'glossary' },
            { label: 'Condensive Reactance', slug: 'glossary/condensive-reactance' },
            { label: 'Wattless Component', slug: 'glossary/wattless-component' },
            { label: 'Imaginary Unit j', slug: 'glossary/imaginary-unit-j' },
            { label: 'Electrostatic Capacity', slug: 'glossary/electrostatic-capacity' },
            { label: 'Counter EMF', slug: 'glossary/counter-electromotive-force' },
            { label: 'Effective Resistance', slug: 'glossary/effective-resistance' },
            { label: 'Hidden Gems', slug: 'hidden-gems' },
            { label: 'Research Questions', slug: 'research-questions' }
          ]
        },
        {
          label: 'Comparisons And Interpretation',
          items: [
            { label: 'Comparison Index', slug: 'comparisons' },
            { label: 'Steinmetz vs Modern EE', slug: 'comparisons/steinmetz-vs-modern-radiation' },
            { label: 'Modern AC Method', slug: 'comparisons/steinmetz-vs-modern-ac-symbolic-method' },
            { label: 'Tesla-Era Science', slug: 'comparisons/tesla-era-electrical-science' },
            { label: 'Tesla-Era Transients', slug: 'comparisons/transients-tesla-era-high-frequency' },
            { label: 'Ether-Field Reading Guide', slug: 'comparisons/ether-field-reading-guide' }
          ]
        },
        {
          label: 'Review And Publication',
          items: [
            { label: 'Publication Roadmap', slug: 'roadmap' },
            { label: 'Completion Audit', slug: 'roadmap/completion-audit' },
            { label: 'Final Completion Pass', slug: 'roadmap/final-completion-pass' },
            { label: 'Deep Decoding Queue', slug: 'roadmap/deep-decoding-promotion-queue' },
            { label: 'World-Class Criteria', slug: 'roadmap/world-class-completion-criteria' },
            { label: 'Citation And Data Export', slug: 'roadmap/citation-and-data-export' },
            { label: 'Editorial Policy', slug: 'roadmap/editorial-policy' },
            { label: 'Canonical Review', slug: 'roadmap/canonical-review-workflow' },
            { label: 'Canonical Verification', slug: 'roadmap/canonical-verification-workbench' },
            { label: 'Equation Verification', slug: 'roadmap/equation-verification-queue' },
            { label: 'Figure Verification', slug: 'roadmap/figure-verification-queue' },
            { label: 'Patent Verification', slug: 'roadmap/patent-verification-queue' },
            { label: 'Claim Attribution', slug: 'roadmap/claim-attribution-ledger' },
            { label: 'Notation Ledger', slug: 'roadmap/notation-ledger' },
            { label: 'Diagram Provenance', slug: 'roadmap/diagram-provenance-ledger' },
            { label: 'Schema Reference', slug: 'roadmap/schema-reference' },
            { label: 'Expert Review Packets', slug: 'roadmap/expert-review-packets' },
            { label: 'Release Levels', slug: 'roadmap/release-levels' },
            { label: 'Accessibility Audit', slug: 'roadmap/accessibility-audit' },
            { label: 'Mobile Readiness', slug: 'roadmap/mobile-readiness-audit' },
            { label: 'Edition Comparison', slug: 'roadmap/edition-comparison-layer' },
            { label: 'Patent Theory Bridge', slug: 'roadmap/patent-to-theory-bridge' },
            { label: 'Future Codex Architecture', slug: 'roadmap/future-codex-architecture' },
            { label: 'Research Codex Engine', slug: 'roadmap/research-codex-engine' },
            { label: 'Clone This Codex', slug: 'roadmap/clone-this-codex' }
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
