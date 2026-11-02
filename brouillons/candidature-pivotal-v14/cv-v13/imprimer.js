const { chromium } = require('playwright');
(async () => { const b = await chromium.launch(); const p = await b.newPage();
await p.goto('file:///tmp/claude-0/-home-claude/730d0294-0b2b-55ca-8b32-49f2d3ec072d/scratchpad/pivotal/cv-v13/cv-C.html'); await p.pdf({ path: '/tmp/claude-0/-home-claude/730d0294-0b2b-55ca-8b32-49f2d3ec072d/scratchpad/pivotal/cv-v13/Lazar_Ciric_CV_2026-11-02_v13_controle-recherche-automatisee.pdf', format: 'A4', printBackground: true, preferCSSPageSize: true });
await b.close(); })();