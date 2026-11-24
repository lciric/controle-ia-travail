# Audit de symétrie des deux réserves « trop propres » du chantier 3 du papier D (budget d'audit borné)

- **Session** : fille 2 du papier D (Opus 5.5), 24 novembre 2026, branche `papier-d/evasion-post-entrainement-v1`, commit de départ `93ad7db9`. Coût : 0 USD, processeur seulement.
- **Pièce auditée** : brouillon de Fable non contre-lu `papiers/D/theorie/brouillon-fable-budget-audit-v1/` (script `check_audit_v1.py`, simulation de couverture de la borne de Bernstein). Rien n'y est modifié.
- **Pièces de l'audit** : `audit_reserves_chantier3_v1.py` (recopie à l'identique des fonctions du brouillon, générateur explicite) et sa sortie `resultats-audit-reserves-chantier3-v1.json`. Graine racine `SeedSequence(202611241000)`, une sous-graine par tirage. Python 3.13.18, numpy 2.5.5, scipy 1.18.1 (environnement du bloc-notes de session).

## Verdict

**Les deux réserves s'expliquent ; ni l'une ni l'autre n'est la trace d'un défaut de code ou d'un résultat arrangé.** Mais chacune révèle une faiblesse de la démonstration numérique, à corriger avant toute citation : la simulation ne teste pas la garantie au voisinage de sa limite, et deux des quatre configurations sont dégénérées.

## Réserve 1 — même taux d'échec de 0,275 % dans trois configurations

**Reproduction.** Le script du brouillon, relancé sur une copie, redonne exactement 11 échecs sur 4 000 répétitions (0,275 %) pour les trois premières configurations, et 0,4 % pour la quatrième. Tous les échecs sont des dépassements du budget aléatoire ; aucune violation du seuil de charge.

**Cause.** Les trois configurations ont le même niveau $\delta = 0{,}05$. Le budget aléatoire vaut $\bar B + \sqrt{2\bar B\log(2/\delta)} + \tfrac{2}{3}\log(2/\delta)$, et la variance du nombre d'audits est presque égale à sa moyenne (rapport 0,95 à 0,995, car les taux d'audit par tour sont faibles). Le seuil tombe donc toujours vers $\sqrt{2\log(2/\delta)} \approx 2{,}72$ écarts-types (2,79 à 2,84 en exact), d'où une même probabilité de dépassement, quelle que soit la configuration.

| Configuration | $\delta$ | Probabilité exacte de dépassement (convolution) | Seuil en écarts-types | Simulé, 5 graines × 40 000 | Violations du seuil |
|---|---|---|---|---|---|
| $K=200$, $n=200$, $\eta=2$ | 0,05 | 0,269 % | 2,84 | 0,264 % (96 à 116 échecs) | 0 |
| $K=200$, $n=2000$, $\eta=2$ | 0,05 | 0,280 % | 2,79 | 0,310 % (116 à 134) | 0 |
| $K=500$, $n=500$, $\eta=\infty$ | 0,05 | 0,259 % | 2,81 | 0,269 % (96 à 121) | 0 |
| $K=100$, $n=1000$, $\eta=1$ | 0,10 | 0,439 % | 2,63 | 0,428 % (165 à 183) | 0 |

**La coïncidence exacte (11, 11, 11)** est un hasard : avec des comptes attendus de 10,8, 11,2 et 10,3 sur 4 000, la probabilité que trois comptes soient égaux est de 0,85 % (0,17 % pour trois fois 11). Peu probable, mais sur des probabilités presque identiques par construction ; les relances à d'autres graines donnent des comptes différents.

**Ce que la réserve révèle.** (i) L'échec réel est d'environ 0,27 % pour un niveau nominal de 5 % : la garantie est prudente d'un facteur proche de 18. (ii) Aucune violation du seuil de charge en 800 000 répétitions : la marge de Bernstein écarte la trajectoire du seuil, si bien que **la simulation ne teste jamais la garantie de sécurité près de sa limite** ; elle ne teste que le dépassement de budget. La phrase du brouillon « the bound is conservative » est exacte ; elle ne doit pas être lue comme une validation de la garantie de seuil.

## Réserve 2 — budget optimal nul dans deux configurations

**Cause.** Les deux premières configurations sont posées **exactement sur la frontière** $\eta\,\Delta R = c$ ($= 2$). La charge accumulée sans aucun audit plafonne à $\Delta R\,G(K) = 1{,}99993 < c$ (car $K$ est fini), donc le plan déterministe optimal n'audite jamais : $B^* = 0$, ce qui est juste. Le plan statistique, lui, réserve une marge $\varepsilon$ (0,334 et 0,099) et descend sous la frontière : il dépense 551 et 1 400 audits.

| Configuration | $c$ | Charge max. sans audit | $B^*$ | $\bar B$ | $\bar B - B^*$ | Inflation bornée par le brouillon |
|---|---|---|---|---|---|---|
| $n=200$ | 2,0 (frontière) | 1,99993 | 0 | 550,7 | 550,7 | — |
| $n=2000$ | 2,0 (frontière) | 1,99993 | 0 | 1 400,0 | 1 400,0 | — |
| $n=200$ | 1,5 | 1,99993 | 864,9 | 1 524,9 | 660,0 | 730,5 |
| $n=2000$ | 1,5 | 1,99993 | 8 648,7 | 10 572,5 | 1 923,8 | 2 168,2 |
| $n=200$ | 2,5 | 1,99993 | 0 | 0 | 0 | — |

**Ce que la réserve révèle.** Sur la frontière, l'inégalité du brouillon $\bar B \le B^* + \text{inflation}$ n'est éprouvée que dans le cas dégénéré $B^* = 0$, où tout le budget est le prix de la marge statistique. Hors frontière ($c = 1{,}5$), $B^*$ est strictement positif et l'inflation mesurée reste sous la borne (rapports 0,90 et 0,89) : la borne tient et n'est pas lâche. Les configurations choisies ne trichent pas, mais elles montrent le cas le moins informatif.

## Recommandations pour le brouillon (à la contre-lecture du chantier 3)

1. Rapporter, pour la simulation de couverture, la probabilité exacte de dépassement à côté du taux simulé, et le niveau de seuil atteint (plus grande charge relative au seuil), pour montrer à quelle distance de la limite on reste.
2. Ajouter au moins une configuration où le seuil est approché (marge réduite, ou plan glouton sans marge) pour éprouver la garantie de sécurité elle-même, pas seulement le budget.
3. Remplacer les deux configurations posées sur la frontière $\eta\,\Delta R = c$ par des configurations hors frontière ($c < \eta\,\Delta R$), ou les garder en les signalant comme cas limite.
4. Ne pas présenter l'égalité des taux comme une propriété : elle découle du choix commun de $\delta$.
