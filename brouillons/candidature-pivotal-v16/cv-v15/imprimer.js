const { chromium } = require('playwright');
(async () => { const b = await chromium.launch(); const p = await b.newPage();
await p.goto('file:///home/claude/controle-ia-travail/brouillons/candidature-pivotal-v16/cv-v15/cv-C.html'); await p.pdf({ path: '/home/claude/controle-ia-travail/brouillons/candidature-pivotal-v16/Lazar_Ciric_CV_2026-11-02_v16_controle-recherche-automatisee.pdf', format: 'A4', printBackground: true, preferCSSPageSize: true });
await b.close(); })();