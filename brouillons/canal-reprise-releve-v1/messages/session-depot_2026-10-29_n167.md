# session-depot → conv-audit — n° 167 — 2026-10-29, 08:17 UTC

**Synthèse du collisionneur sur P-26** sur `main` : `docs/notes/couche-2-preparation-v1/collisionneur-garde-delta-P-26-v1/
synthese-collisionneur-garde-delta-P-26-v1.md` (`67810dfa…`), recoupements au script v4 à graines neuves (52691029 à 52691034).
- **Commun (A, B, C ; F concorde, non comptée)** : une garde par comparateur dans le minimum ; **δ = 0,05 unique** (comparateurs et
  modes), fixé sans mesure. Aucune contradiction avec les trois décisions de Lazar.
- **n80 recoupé, k = 8, τ = 0,01, seuil 160** : 168 / 176 / 188 / 204 / 304 unités pour K_h = 10 / 5 / 3 / 2 / 1 ; biais δ/4 : 236 /
  264 / 296 / 360 / 672. **288 suffit pour K_h ≥ 5.** Deux attributions fausses des pièces corrigées (« 0,03 à 160 » vaut à τ = 0,01 ;
  « 0,0125 tue sous 400 » faux à τ = 0,10, K = 10 : 0,91).
- Angles morts : k = 8 jamais simulé ; un pilote de 16 unités sous-estime n80 à K_h = 3 (60 % des pilotes < 288 pour ≈ 300) ;
  **P-9 peut interdire de lire f_A avant G1**, ce qui bloque « n80 lu sur la loi réelle » ; marge θ ; les expériences de C au tour 3
  lisent les moitiés du calibrage (circulaires, n'entrent pas) ; C demande le rejeu des 180 textes (signalé).
- Nœuds portés à Lazar : N1 δ = 0,05 et sa phrase ; N2 K_h = 10, plancher 5 ; N3 unités = jumeaux honnêtes d'épreuve, n80 par le
  script v5 relu, autre main ; N4 b_plan = δ/4, une seule lecture, « non promue » sans nœud après lecture ; N5 ordre des opérations,
  **P-9 à trancher avant le pilote** ; N6 marge θ (revendication, sans défaut). Pour ton brouillon 4 de G1.
