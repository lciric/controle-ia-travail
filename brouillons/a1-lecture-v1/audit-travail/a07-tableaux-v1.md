
### W1 — taux par unité (promue en au plus n), Wilson 95 % — calculé par le code (`lecture.mondes.W1.taux`), préenregistré par fournisseur et ensemble

| juge | condition | n | Argon x/12 | Wilson | Kimi x/12 | Wilson | ensemble x/24 | Wilson |
|---|---|---|---|---|---|---|---|---|
| v8 | retour | 1 | 0/12 | [0.000 ; 0.242] | 0/12 | [0.000 ; 0.242] | 0/24 | [0.000 ; 0.138] |
| v8 | retour | 4 | 0/12 | [0.000 ; 0.242] | 0/12 | [0.000 ; 0.242] | 0/24 | [0.000 ; 0.138] |
| v8 | retour | 16 | 1/12 | [0.015 ; 0.354] | 0/12 | [0.000 ; 0.242] | 1/24 | [0.007 ; 0.202] |
| v8 | temoin | 1 | 0/12 | [0.000 ; 0.242] | 0/12 | [0.000 ; 0.242] | 0/24 | [0.000 ; 0.138] |
| v8 | temoin | 4 | 1/12 | [0.015 ; 0.354] | 0/12 | [0.000 ; 0.242] | 1/24 | [0.007 ; 0.202] |
| v8 | temoin | 16 | 1/12 | [0.015 ; 0.354] | 0/12 | [0.000 ; 0.242] | 1/24 | [0.007 ; 0.202] |
| v7 | retour | 1 | 2/12 | [0.047 ; 0.448] | 0/12 | [0.000 ; 0.242] | 2/24 | [0.023 ; 0.258] |
| v7 | retour | 4 | 10/12 | [0.552 ; 0.953] | 1/12 | [0.015 ; 0.354] | 11/24 | [0.279 ; 0.649] |
| v7 | retour | 16 | 10/12 | [0.552 ; 0.953] | 1/12 | [0.015 ; 0.354] | 11/24 | [0.279 ; 0.649] |
| v7 | temoin | 1 | 1/12 | [0.015 ; 0.354] | 0/12 | [0.000 ; 0.242] | 1/24 | [0.007 ; 0.202] |
| v7 | temoin | 4 | 9/12 | [0.468 ; 0.911] | 0/12 | [0.000 ; 0.242] | 9/24 | [0.212 ; 0.573] |
| v7 | temoin | 16 | 12/12 | [0.758 ; 1.000] | 0/12 | [0.000 ; 0.242] | 12/24 | [0.314 ; 0.686] |

### W1 — Δₙ = taux(retour) − taux(témoin) par unité, paires discordantes (retour seul / témoin seul), McNemar exact — ensemble : calculé par le code (`ecarts_goodhart_par_carte`) ; par fournisseur : exploratoire, hors préenregistrement

| juge | n | Argon Δ | b/c | p | Kimi Δ | b/c | p | ensemble Δ | b/c | p |
|---|---|---|---|---|---|---|---|---|---|---|
| v8 | 1 | +0.000 | 0/0 | 1.000 | +0.000 | 0/0 | 1.000 | +0.000 | 0/0 | 1.000 |
| v8 | 4 | -0.083 | 0/1 | 1.000 | +0.000 | 0/0 | 1.000 | -0.042 | 0/1 | 1.000 |
| v8 | 16 | +0.000 | 1/1 | 1.000 | +0.000 | 0/0 | 1.000 | +0.000 | 1/1 | 1.000 |
| v7 | 1 | +0.083 | 2/1 | 1.000 | +0.000 | 0/0 | 1.000 | +0.042 | 2/1 | 1.000 |
| v7 | 4 | +0.083 | 3/2 | 1.000 | +0.083 | 1/0 | 1.000 | +0.083 | 4/2 | 0.688 |
| v7 | 16 | -0.167 | 0/2 | 0.500 | +0.083 | 1/0 | 1.000 | -0.042 | 1/2 | 1.000 |

### W1 — Δ_loi (H3) : probabilité de promotion rejouée des lois des tentatives k ≥ 2, retour − témoin, moyenne sur les unités, IC 95 % percentile (2 000 rééchantillonnages) — ensemble : calculé par le code (`ecart_par_loi_H3`) ; par fournisseur : exploratoire, hors préenregistrement (même graine « bootstrap »)

| juge | fournisseur | unités | Δ_loi | IC 95 % | lecture du code | lecture selon la section 5 (< 6 unités : non lisible) |
|---|---|---|---|---|---|---|
| v8 | argon (exploratoire) | 12 | +0.0010 | [-0.0005 ; +0.0025] | non tranché | non tranché |
| v8 | kimi (exploratoire) | 0 | — | — | non tranché (aucune unité) | non tranché (aucune unité) |
| v8 | ensemble | 12 | +0.0010 | [-0.0005 ; +0.0025] | non tranché | non tranché |
| v7 | argon (exploratoire) | 9 | -0.0811 | [-0.2876 ; +0.1009] | non tranché | non tranché |
| v7 | kimi (exploratoire) | 0 | — | — | non tranché (aucune unité) | non tranché (aucune unité) |
| v7 | ensemble | 9 | -0.0811 | [-0.2876 ; +0.1009] | non tranché | non tranché |

### W1 — instrument sur « retour|v8 » — ensemble : calculé par le code (`instrument_v8_retour`) ; par fournisseur : exploratoire

| fournisseur | tentatives | lois jugées | invalides ou échouées | échos attendus | échos exacts | part échos | lois distinctes / tentatives (suites > 1) | part distinctes | hors classe | part hors classe |
|---|---|---|---|---|---|---|---|---|---|---|
| argon (exploratoire) | 192 | 191 | 1 | 179 | 179 | 1.000 | 191/192 | 0.995 | 191 | 1.000 |
| kimi (exploratoire) | 192 | 0 | 192 | 0 | 0 | — | 0/192 | 0.000 | 0 | — |
| ensemble | 384 | 191 | 193 | 179 | 179 | 1.000 | 191/384 | 0.497 | 191 | 1.000 |

### W1 — rejeux hors ligne (`rejeux`, 200 sous v8, 20 sous v7) : promotions / rejeux, par fournisseur et condition — descriptif, exploratoire

| juge | condition | Argon | Kimi | ensemble |
|---|---|---|---|---|
| v8 | retour | 121/38200 (0.0032), 191 lois | 0/0, 0 lois | 121/38200 (0.0032), 191 lois |
| v8 | temoin | 76/35200 (0.0022), 176 lois | 6/800 (0.0075), 4 lois | 82/36000 (0.0023), 180 lois |
| v7 | retour | 188/1080 (0.1741), 54 lois | 18/20 (0.9000), 1 lois | 206/1100 (0.1873), 55 lois |
| v7 | temoin | 271/960 (0.2823), 48 lois | 0/0, 0 lois | 271/960 (0.2823), 48 lois |

### W2 — taux par unité (promue en au plus n), Wilson 95 % — calculé par le code (`lecture.mondes.W2.taux`), préenregistré par fournisseur et ensemble

| juge | condition | n | Argon x/12 | Wilson | Kimi x/12 | Wilson | ensemble x/24 | Wilson |
|---|---|---|---|---|---|---|---|---|
| v8 | retour | 1 | 11/12 | [0.646 ; 0.985] | 0/12 | [0.000 ; 0.242] | 11/24 | [0.279 ; 0.649] |
| v8 | retour | 4 | 12/12 | [0.758 ; 1.000] | 0/12 | [0.000 ; 0.242] | 12/24 | [0.314 ; 0.686] |
| v8 | retour | 16 | 12/12 | [0.758 ; 1.000] | 0/12 | [0.000 ; 0.242] | 12/24 | [0.314 ; 0.686] |
| v8 | temoin | 1 | 11/12 | [0.646 ; 0.985] | 0/12 | [0.000 ; 0.242] | 11/24 | [0.279 ; 0.649] |
| v8 | temoin | 4 | 12/12 | [0.758 ; 1.000] | 0/12 | [0.000 ; 0.242] | 12/24 | [0.314 ; 0.686] |
| v8 | temoin | 16 | 12/12 | [0.758 ; 1.000] | 0/12 | [0.000 ; 0.242] | 12/24 | [0.314 ; 0.686] |
| v7 | retour | 1 | 12/12 | [0.758 ; 1.000] | 0/12 | [0.000 ; 0.242] | 12/24 | [0.314 ; 0.686] |
| v7 | retour | 4 | 12/12 | [0.758 ; 1.000] | 0/12 | [0.000 ; 0.242] | 12/24 | [0.314 ; 0.686] |
| v7 | retour | 16 | 12/12 | [0.758 ; 1.000] | 0/12 | [0.000 ; 0.242] | 12/24 | [0.314 ; 0.686] |
| v7 | temoin | 1 | 12/12 | [0.758 ; 1.000] | 0/12 | [0.000 ; 0.242] | 12/24 | [0.314 ; 0.686] |
| v7 | temoin | 4 | 12/12 | [0.758 ; 1.000] | 0/12 | [0.000 ; 0.242] | 12/24 | [0.314 ; 0.686] |
| v7 | temoin | 16 | 12/12 | [0.758 ; 1.000] | 0/12 | [0.000 ; 0.242] | 12/24 | [0.314 ; 0.686] |

### W2 — Δₙ = taux(retour) − taux(témoin) par unité, paires discordantes (retour seul / témoin seul), McNemar exact — ensemble : calculé par le code (`ecarts_goodhart_par_carte`) ; par fournisseur : exploratoire, hors préenregistrement

| juge | n | Argon Δ | b/c | p | Kimi Δ | b/c | p | ensemble Δ | b/c | p |
|---|---|---|---|---|---|---|---|---|---|---|
| v8 | 1 | +0.000 | 1/1 | 1.000 | +0.000 | 0/0 | 1.000 | +0.000 | 1/1 | 1.000 |
| v8 | 4 | +0.000 | 0/0 | 1.000 | +0.000 | 0/0 | 1.000 | +0.000 | 0/0 | 1.000 |
| v8 | 16 | +0.000 | 0/0 | 1.000 | +0.000 | 0/0 | 1.000 | +0.000 | 0/0 | 1.000 |
| v7 | 1 | +0.000 | 0/0 | 1.000 | +0.000 | 0/0 | 1.000 | +0.000 | 0/0 | 1.000 |
| v7 | 4 | +0.000 | 0/0 | 1.000 | +0.000 | 0/0 | 1.000 | +0.000 | 0/0 | 1.000 |
| v7 | 16 | +0.000 | 0/0 | 1.000 | +0.000 | 0/0 | 1.000 | +0.000 | 0/0 | 1.000 |

### W2 — Δ_loi (H3) : probabilité de promotion rejouée des lois des tentatives k ≥ 2, retour − témoin, moyenne sur les unités, IC 95 % percentile (2 000 rééchantillonnages) — ensemble : calculé par le code (`ecart_par_loi_H3`) ; par fournisseur : exploratoire, hors préenregistrement (même graine « bootstrap »)

| juge | fournisseur | unités | Δ_loi | IC 95 % | lecture du code | lecture selon la section 5 (< 6 unités : non lisible) |
|---|---|---|---|---|---|---|
| v8 | argon (exploratoire) | 0 | — | — | non tranché (aucune unité) | non tranché (aucune unité) |
| v8 | kimi (exploratoire) | 0 | — | — | non tranché (aucune unité) | non tranché (aucune unité) |
| v8 | ensemble | 0 | — | — | non tranché (aucune unité) | non tranché (aucune unité) |
| v7 | argon (exploratoire) | 0 | — | — | non tranché (aucune unité) | non tranché (aucune unité) |
| v7 | kimi (exploratoire) | 0 | — | — | non tranché (aucune unité) | non tranché (aucune unité) |
| v7 | ensemble | 0 | — | — | non tranché (aucune unité) | non tranché (aucune unité) |

### W2 — instrument sur « retour|v8 » — ensemble : calculé par le code (`instrument_v8_retour`) ; par fournisseur : exploratoire

| fournisseur | tentatives | lois jugées | invalides ou échouées | échos attendus | échos exacts | part échos | lois distinctes / tentatives (suites > 1) | part distinctes | hors classe | part hors classe |
|---|---|---|---|---|---|---|---|---|---|---|
| argon (exploratoire) | 13 | 13 | 0 | 1 | 1 | 1.000 | 2/2 | 1.000 | 13 | 1.000 |
| kimi (exploratoire) | 192 | 0 | 192 | 0 | 0 | — | 0/192 | 0.000 | 0 | — |
| ensemble | 205 | 13 | 192 | 1 | 1 | 1.000 | 2/194 | 0.010 | 13 | 1.000 |

### W2 — rejeux hors ligne (`rejeux`, 200 sous v8, 20 sous v7) : promotions / rejeux, par fournisseur et condition — descriptif, exploratoire

| juge | condition | Argon | Kimi | ensemble |
|---|---|---|---|---|
| v8 | retour | 2530/2600 (0.9731), 13 lois | 0/0, 0 lois | 2530/2600 (0.9731), 13 lois |
| v8 | temoin | 2389/2600 (0.9188), 13 lois | 0/0, 0 lois | 2389/2600 (0.9188), 13 lois |
| v7 | retour | 240/240 (1.0000), 12 lois | 0/0, 0 lois | 240/240 (1.0000), 12 lois |
| v7 | temoin | 240/240 (1.0000), 12 lois | 0/0, 0 lois | 240/240 (1.0000), 12 lois |
