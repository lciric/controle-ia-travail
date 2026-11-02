const { chromium } = require('playwright');
(async () => { const b = await chromium.launch(); const p = await b.newPage();
await p.goto('file:///home/claude/controle-ia-travail/brouillons/candidature-pivotal-v15/cv-v14/cv-I.html'); await p.pdf({ path: '/home/claude/controle-ia-travail/brouillons/candidature-pivotal-v15/cv-v14/Lazar_Ciric_CV_2026-11-02_v14_interpretabilite.pdf', format: 'A4', printBackground: true, preferCSSPageSize: true });
await b.close(); })();