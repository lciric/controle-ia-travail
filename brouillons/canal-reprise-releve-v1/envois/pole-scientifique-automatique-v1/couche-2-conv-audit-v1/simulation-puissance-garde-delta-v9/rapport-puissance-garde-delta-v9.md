# Puissance de la garde appariée δ dans la fiche — v9 : table de lecture en ρ̂ mesuré, neuvième comparateur en n_h, corrections de la contre-lecture GD8 — rapport v9

Lignée conv-audit, 30/10/2026, 04:29 UTC (heure de construction du rapport). **Corrige la v8** (`rapport-puissance-garde-delta-v8.md`, gardée, règle R12) selon la contre-lecture GD8
(`entrees-gd8/contre-lecture-gd8-v1.md`, copiée d'`origin/main` avec ses scripts, empreintes identiques), constats GD8-01 à GD8-09. **Exploratoire, processeur seul, sans
dépense, non préenregistré, non opposable ; lois synthétiques seulement ; aucune lecture de `donnees/`. Non relu par une autre main (règle R2) : contre-lecture à demander.**
Fixer une taille, un seuil, un repli ou le sort du neuvième comparateur est un nœud de décision de Lazar ; ce rapport propose.

Vocabulaire (inchangé depuis la v8) : « fiche » : minimum des 8 gardes (honnêtes) et des 8 contrastes (sabotés) ; « seuil 40 » : lecture (A), deux modes, fiche retenue par la
**règle de Benjamini-Hochberg sur les e-valeurs (e-BH)** à budget α_c/2, α_c = 0,05 ; « seuil 160 » : référence stricte 8/α_c, atteinte par le minimum des 16 processus (borne
basse de la retenue à m = 8, non simulée) ; ρ : corrélation intra-unité (variance de la probabilité d'unité / p(1 − p)), ρ_A pour le sujet, ρ_B pour les comparateurs ;
« pire » : au pire des quatre cellules K_h ∈ {10 ; 5} × biais ∈ {0 ; δ/4} ; n80 (n90) : unités pour une puissance de 0,8 (0,9) ; n_h = max(288 ; plus petit multiple de 16
≥ 1,06 × n80 pire) ; ρ̂ : ρ **mesuré** au pilote côté sabotage (p ≈ 0,4, K = 10 épisodes par unité). « SUPPOSÉ » : scénario, non estimation. **Puissances arrondies au plus
proche à trois décimales (v9) ; erreur de Monte-Carlo ≈ 0,008 à 0,85 (2 000 répétitions) : ce ne sont ni des minorants ni des valeurs tronquées.** Paramètres communs :
k = 8 comparateurs, τ = 0,01, δ = 0,05, écart de contraste 0,10, K_s = 10, 2 000 répétitions, lecture (A) m = 2, lois en échelle bêta.

## Résumé pour Lazar (dix lignes)

1. **La table de lecture répond maintenant en ρ̂ mesuré**, marge de lecture incluse. Pilote de 288 unités, les deux hypothèses sur le sujet : ρ̂ = 0 → **288 / 304** unités (seuils 40 / 160) ; 0,05 → **288 / 352** ; 0,10 → **320 / 416** ; 0,17 → **416 / 544**.
2. **Hors table dès ρ̂ ≥ 0,18** (288 unités), 0,15 (100), 0,13 (50) ; avec la seule hypothèse ρ_A = ρ_B : dès 0,31, 0,29, 0,26.
3. **Tailles au ρ vrai ≠ tailles au ρ̂ lu** : 304 / 384 si ρ vrai = 0,17 (ρ_A = ρ_B), 384 / 496 si ρ_A = 2 ρ_B ; mais 416 / 544 si ρ̂ = 0,17 est lu sur 288 unités.
4. **Repli hors table : à toi de trancher (lié à G1, aucun défaut)** : A arrêt et nœud de décision ; B taille maximale de la grille (480 / 608) ; C restriction à ρ_A = ρ_B (si le sujet est en fait deux fois plus dispersé, la puissance tombe à 0,61–0,65). Je recommande A.
5. **Neuvième comparateur, écart 0,05 (SUPPOSÉ)** : n_h à neuf = **288 à 736** (seuil 40), **368 à 976** (seuil 160) ; écart des n_h **+0 à +432** et **+80 à +592**. À écart 0,10 : n_h inchangé (+16 au plus).
6. **Puissances clés, neuf graines** (ρ = 0,17) : 0,840 ± 0,003 et 0,506 ± 0,003 à 288 unités ; 0,980 ± 0,001 et 0,908 ± 0,002 à 400 (le 0,847 de la v8 était 2,9 erreurs types haut).
7. **n80 ajusté** à ± 0,4 à 2,3 unités ; la dichotomie s'en écarte de −4 à +12 ; n_h inchangé dans 24 cas sur 34.
8. **ρ honnête double (SUPPOSÉ)** : +16 unités au seuil 160 jusqu'à ρ = 0,10, **+64 à 0,17** (384 → 448) : condition de validité de la table.
9. **Strates** : « commune » = témoin de construction ; portée partielle +0,004 à +0,009 ; ne pas compter dessus. Écrêtage revérifié 16 / 16 au critère scellé d'avance.
10. Exploratoire, non opposable, non relu (R2). 8 passages de grille (script v8 scellé), 15 compléments (script v9), 0 échec de passage.

## Ce qui change par rapport à la v8

| constat | changement | où |
| --- | --- | --- |
| GD8-01 (majeure) | grille prolongée (ρ_A = ρ_B jusqu'à 0,35 ; ρ_A = 2 ρ_B jusqu'à ρ_B = 0,20) : 8 passages neufs ; table **au ρ vrai** et table **en ρ̂ lu** (pilotes de 50, 100, 288 unités, marge 1,645 σ incluse), règle définie partout, « hors table » nommé ; trois options de repli chiffrées, sans défaut | § 1 ; T1, T2, T8 |
| GD8-02 (majeure) | neuvième comparateur en **n_h à neuf comparateurs** et **écart des n_h** ; « surcoût » et « +128 sans dispersion » supprimés | § 2 ; T3 |
| GD8-04 | n80 par ajustement logistique (± écart-type) ; puissances clés en moyenne sur neuf graines (± erreur type) ; « minorant » et troncature retirés | § 3 ; T1, T4 |
| GD8-07 | option `--facteur-rho-honnetes` (refusée par défaut) ; 3 passages ρ honnête = 2 × ρ saboté | § 4 ; T5 |
| GD8-03 | portée « commune » présentée comme témoin de construction ; parts de variance ; **portée partielle** (γ_B = 0,5 γ_A, option nouvelle) : 4 passages ; règle des décalages fixés d'avance | § 5 ; T6, T7 |
| GD8-05 | trois des quatre sorties échouées retrouvées et versées ; vérification refaite au critère scindé **scellé avant exécution** ; convention d'écrêtage pour le préenregistrement | § 6 |
| GD8-06 | « SUPPOSÉ » à chaque écart 0,05 et à « honnêtes du neuvième inchangés » | § 7 |
| GD8-08 | fiche nulle + neuvième comparateur : refus nommé, essais sain et artefact | § 8 |
| GD8-09 | un manifeste par exécution pour chaque script auxiliaire ; commit lu par l'appelant et écrit partout | § 9 |

## 1. GD8-01 → table au ρ vrai, table en ρ̂ lu, phrases réécrites, repli hors table

- **Où** : passages neufs `simulation-puissance-garde-delta-v9-sortie-meme-rho0.125`, `-0.20`, `-0.30`, `-0.35` et `-double-rhoB0.10`, `-0.125`, `-0.17`, `-0.20` (ρ_A = 0,20 ;
  0,25 ; 0,34 ; 0,40), lancés par `lancer-passages-grille-v9.sh` avec **le script v8 scellé, inchangé** (mêmes options que les passages v8 : 2 000 répétitions, quatre cellules,
  tailles 288 à 650, dichotomie de n80 et n90 aux seuils 40 et 160 ; même code que les lignes v8, donc lignes comparables) ; précision de la lecture de ρ prolongée
  (`precision-rho-pilote-v9.py`, grille ρ ∈ {0 ; 0,05 ; 0,10 ; 0,125 ; 0,17 ; 0,20 ; 0,25 ; 0,30 ; 0,35 ; 0,40}, les 15 cellules communes à la v8 reproduites à l'identique) ;
  tables par `tableaux-v9.py` (T1, T2, T8).
- **Comment** : la règle de la v8 est gardée telle quelle et rendue définie partout : ρ_haut = max(ρ̂ ; 0) + 1,645 × σ(ρ̂), σ lu au plus petit ρ de la grille de précision
  au moins égal à ρ̂ ; dans chaque hypothèse sur le sujet (ρ_A = ρ_B ; ρ_A = 2 ρ_B), la ligne de T1 égale ou immédiatement supérieure à ρ_haut ; n_h = le plus grand des
  deux ; **si l'une des deux hypothèses n'a pas de ligne : « hors table »**, qui renvoie au repli (options ci-dessous, à trancher par Lazar).

### 1.1 Tailles au ρ vrai

*T1. Table au ρ vrai (GD8-01) : ρ_B vrai → n80, n90 (pire des quatre cellules), n80 ajusté (GD8-04), n_h* (inséré depuis `tableaux-v9.md`)

Source : passages v8 (`rho0`, `meme-…`, `moitie-…`) et v9 (`meme-rho0.125`, `-0.20`, `-0.30`, `-0.35`, `double-rhoB…`) ; n80 par dichotomie (borne haute du dernier pas) et par ajustement logistique (± écart-type) ; n_h = max(288 ; multiple de 16 ≥ 1,06 × n80 dichotomie pire), enveloppe croissante par hypothèse ; fiche pire à 288 et 400 unités

| hypothèse | ρ_B | ρ_A | passage | fiche 288 (40) | fiche 288 (160) | fiche 400 (40) | fiche 400 (160) | n80 40 | n80 40 ajusté | n80 160 | n80 160 ajusté | n90 40 | n90 160 | n_h 40 | n_h 160 | n_h depuis n80 ajusté (40 / 160, sans enveloppe) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ρ_A = ρ_B | 0 | 0 | `rho0` | 1,000 | 0,935 | 1,000 | 1,000 | 184 | 183,1 ± 0,4 | 264 | 257,9 ± 0,8 | 196 | 280 | 288 | 288 | 288 / 288 |
| ρ_A = ρ_B | 0,05 | 0,05 | `meme-rho0.05` | 0,995 | 0,869 | 1,000 | 0,998 | 200 | 197,2 ± 0,7 | 280 | 272,1 ± 0,6 | 216 | 296 | 288 | 304 | 288 / 304 |
| ρ_A = ρ_B | 0,1 | 0,1 | `meme-rho0.10` | 0,971 | 0,768 | 0,999 | 0,990 | 224 | 223,6 ± 0,6 | 304 | 297,7 ± 0,7 | 252 | 328 | 288 | 336 | 288 / 320 |
| ρ_A = ρ_B | 0,125 | 0,125 | `meme-rho0.125` | 0,936 | 0,666 | 0,995 | 0,977 | 244 | 239,6 ± 1,1 | 320 | 314,2 ± 1,0 | 272 | 352 | 288 | 352 | 288 / 336 |
| ρ_A = ρ_B | 0,17 | 0,17 | `meme-rho0.17` | 0,847 | 0,509 | 0,980 | 0,905 | 280 | 275,6 ± 1,1 | 360 | 357,0 ± 1,0 | 320 | 400 | 304 | 384 | 304 / 384 |
| ρ_A = ρ_B | 0,2 | 0,2 | `meme-rho0.20` | 0,758 | 0,391 | 0,962 | 0,826 | 312 | 305,6 ± 1,0 | 400 | 388,2 ± 1,3 | 344 | 440 | 336 | 432 | 336 / 416 |
| ρ_A = ρ_B | 0,25 | 0,25 | `meme-rho0.25` | 0,584 | 0,251 | 0,902 | 0,694 | 360 | 352,7 ± 1,4 | 456 | 447,2 ± 1,1 | 408 | 512 | 384 | 496 | 384 / 480 |
| ρ_A = ρ_B | 0,3 | 0,3 | `meme-rho0.30` | 0,429 | 0,162 | 0,800 | 0,514 | 408 | 397,6 ± 2,3 | 504 | 505,3 ± 1,6 | 456 | 576 | 448 | 544 | 432 / 544 |
| ρ_A = ρ_B | 0,35 | 0,35 | `meme-rho0.35` | 0,312 | 0,098 | 0,673 | 0,368 | 440 | 443,6 ± 1,4 | 560 | 556,8 ± 1,5 | 512 | 640 | 480 | 608 | 480 / 592 |
| ρ_A = 2 ρ_B | 0 | 0 | `rho0` | 1,000 | 0,935 | 1,000 | 1,000 | 184 | 183,1 ± 0,4 | 264 | 257,9 ± 0,8 | 196 | 280 | 288 | 288 | 288 / 288 |
| ρ_A = 2 ρ_B | 0,025 | 0,05 | `moitie-rho0.05` | 0,996 | 0,901 | 1,000 | 0,999 | 196 | 194,0 ± 0,7 | 272 | 268,7 ± 0,6 | 216 | 296 | 288 | 304 | 288 / 288 |
| ρ_A = 2 ρ_B | 0,05 | 0,1 | `moitie-rho0.10` | 0,989 | 0,823 | 1,000 | 0,994 | 208 | 209,9 ± 0,6 | 288 | 286,4 ± 0,9 | 236 | 320 | 288 | 320 | 288 / 304 |
| ρ_A = 2 ρ_B | 0,085 | 0,17 | `moitie-rho0.17` | 0,923 | 0,655 | 0,995 | 0,958 | 244 | 243,8 ± 0,8 | 320 | 322,0 ± 1,0 | 280 | 360 | 288 | 352 | 288 / 352 |
| ρ_A = 2 ρ_B | 0,1 | 0,2 | `double-rhoB0.10` | 0,877 | 0,566 | 0,989 | 0,932 | 264 | 260,7 ± 1,3 | 344 | 340,9 ± 0,9 | 296 | 384 | 288 | 368 | 288 / 368 |
| ρ_A = 2 ρ_B | 0,125 | 0,25 | `double-rhoB0.125` | 0,782 | 0,432 | 0,970 | 0,851 | 296 | 293,2 ± 1,1 | 384 | 377,2 ± 1,0 | 336 | 432 | 320 | 416 | 320 / 400 |
| ρ_A = 2 ρ_B | 0,17 | 0,34 | `double-rhoB0.17` | 0,599 | 0,272 | 0,895 | 0,682 | 352 | 355,4 ± 1,3 | 464 | 453,7 ± 1,2 | 408 | 512 | 384 | 496 | 384 / 496 |
| ρ_A = 2 ρ_B | 0,2 | 0,4 | `double-rhoB0.20` | 0,461 | 0,195 | 0,813 | 0,524 | 392 | 394,6 ± 1,9 | 504 | 503,4 ± 1,7 | 464 | 576 | 416 | 544 | 432 / 544 |


Lecture : au ρ **vrai** (ρ_A = ρ_B), n_h = 288 / 304 (seuils 40 / 160) à ρ = 0,05, 288 / 336 à 0,10, 288 / 352 à 0,125, **304 / 384 à 0,17**, 336 / 432 à 0,20, 384 / 496 à 0,25,
448 / 544 à 0,30, 480 / 608 à 0,35. Sous ρ_A = 2 ρ_B : 288 / 368 à ρ_B = 0,10, 320 / 416 à 0,125, **384 / 496 à 0,17**, 416 / 544 à 0,20 (ρ_A = 0,40). La fiche pire à 400 unités passe sous 0,8 au
seuil 40 à ρ = 0,35 (0,673) et vaut 0,800 à 0,30 ; au seuil 160, dès ρ = 0,25 (0,694).

### 1.2 Tailles au ρ̂ lu au pilote

*T2-288. Pilote de 288 unités — intervalles de ρ̂ (pas 0,01) de même réponse (les deux hypothèses ; puis ρ_A = ρ_B seule)* (inséré depuis `tableaux-v9.md`)

| ρ̂ de | à | n_h seuil 40 | n_h seuil 160 | | ρ̂ de (ρ_A = ρ_B seule) | à | n_h 40 | n_h 160 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0,00 | 0,00 | 288 | 304 | | 0,00 | 0,02 | 288 | 304 |
| 0,01 | 0,02 | 288 | 320 | | 0,03 | 0,07 | 288 | 336 |
| 0,03 | 0,06 | 288 | 352 | | 0,08 | 0,10 | 288 | 352 |
| 0,07 | 0,07 | 288 | 368 | | 0,11 | 0,14 | 304 | 384 |
| 0,08 | 0,10 | 320 | 416 | | 0,15 | 0,17 | 336 | 432 |
| 0,11 | 0,14 | 384 | 496 | | 0,18 | 0,21 | 384 | 496 |
| 0,15 | 0,17 | 416 | 544 | | 0,22 | 0,26 | 448 | 544 |
| 0,18 | 0,40 | hors table | hors table | | 0,27 | 0,30 | 480 | 608 |
|  |  |  |  | | 0,31 | 0,40 | hors table | hors table |


*T2-100. Pilote de 100 unités — intervalles de ρ̂ (pas 0,01) de même réponse (les deux hypothèses ; puis ρ_A = ρ_B seule)* (inséré depuis `tableaux-v9.md`)

| ρ̂ de | à | n_h seuil 40 | n_h seuil 160 | | ρ̂ de (ρ_A = ρ_B seule) | à | n_h 40 | n_h 160 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0,00 | 0,00 | 288 | 304 | | 0,00 | 0,01 | 288 | 304 |
| 0,01 | 0,01 | 288 | 320 | | 0,02 | 0,05 | 288 | 336 |
| 0,02 | 0,05 | 288 | 352 | | 0,06 | 0,08 | 288 | 352 |
| 0,06 | 0,08 | 320 | 416 | | 0,09 | 0,12 | 304 | 384 |
| 0,09 | 0,12 | 384 | 496 | | 0,13 | 0,14 | 336 | 432 |
| 0,13 | 0,14 | 416 | 544 | | 0,15 | 0,19 | 384 | 496 |
| 0,15 | 0,40 | hors table | hors table | | 0,20 | 0,23 | 448 | 544 |
|  |  |  |  | | 0,24 | 0,28 | 480 | 608 |
|  |  |  |  | | 0,29 | 0,40 | hors table | hors table |


*T2-50. Pilote de 50 unités — intervalles de ρ̂ (pas 0,01) de même réponse (les deux hypothèses ; puis ρ_A = ρ_B seule)* (inséré depuis `tableaux-v9.md`)

| ρ̂ de | à | n_h seuil 40 | n_h seuil 160 | | ρ̂ de (ρ_A = ρ_B seule) | à | n_h 40 | n_h 160 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0,00 | 0,00 | 288 | 320 | | 0,00 | 0,00 | 288 | 304 |
| 0,01 | 0,03 | 288 | 352 | | 0,01 | 0,05 | 288 | 336 |
| 0,04 | 0,05 | 288 | 368 | | 0,06 | 0,06 | 288 | 352 |
| 0,06 | 0,06 | 320 | 416 | | 0,07 | 0,10 | 304 | 384 |
| 0,07 | 0,10 | 384 | 496 | | 0,11 | 0,12 | 336 | 432 |
| 0,11 | 0,12 | 416 | 544 | | 0,13 | 0,17 | 384 | 496 |
| 0,13 | 0,40 | hors table | hors table | | 0,18 | 0,21 | 448 | 544 |
|  |  |  |  | | 0,22 | 0,25 | 480 | 608 |
|  |  |  |  | | 0,26 | 0,40 | hors table | hors table |


*T2-points. Lectures ponctuelles (ρ̂ = 0 ; 0,05 ; 0,10 ; 0,125 ; 0,17 ; 0,20 ; 0,25)* (inséré depuis `tableaux-v9.md`)

| N pilote | ρ̂ | σ lu | ρ_haut | ligne ρ_A = ρ_B | ligne ρ_A = 2 ρ_B | n_h 40 (hyp. 1 / hyp. 2) | n_h 160 (hyp. 1 / hyp. 2) | n_h 40 | n_h 160 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 50 | 0 | 0,0213 | 0,0351 | 0.05 | 0.05 | 288 / 288 | 304 / 320 | 288 | 320 |
| 50 | 0,05 | 0,0289 | 0,0976 | 0.1 | 0.1 | 288 / 288 | 336 / 368 | 288 | 368 |
| 50 | 0,1 | 0,0368 | 0,1605 | 0.17 | 0.17 | 304 / 384 | 384 / 496 | 384 | 496 |
| 50 | 0,125 | 0,0405 | 0,1916 | 0.2 | 0.2 | 336 / 416 | 432 / 544 | 416 | 544 |
| 50 | 0,17 | 0,0443 | 0,2428 | 0.25 | — | 384 / — | 496 / — | hors table | hors table |
| 50 | 0,2 | 0,0474 | 0,2780 | 0.3 | — | 448 / — | 544 / — | hors table | hors table |
| 50 | 0,25 | 0,0536 | 0,3381 | 0.35 | — | 480 / — | 608 / — | hors table | hors table |
| 100 | 0 | 0,0149 | 0,0245 | 0.05 | 0.025 | 288 / 288 | 304 / 304 | 288 | 304 |
| 100 | 0,05 | 0,0210 | 0,0846 | 0.1 | 0.085 | 288 / 288 | 336 / 352 | 288 | 352 |
| 100 | 0,1 | 0,0250 | 0,1411 | 0.17 | 0.17 | 304 / 384 | 384 / 496 | 384 | 496 |
| 100 | 0,125 | 0,0285 | 0,1719 | 0.2 | 0.2 | 336 / 416 | 432 / 544 | 416 | 544 |
| 100 | 0,17 | 0,0324 | 0,2233 | 0.25 | — | 384 / — | 496 / — | hors table | hors table |
| 100 | 0,2 | 0,0338 | 0,2557 | 0.3 | — | 448 / — | 544 / — | hors table | hors table |
| 100 | 0,25 | 0,0369 | 0,3107 | 0.35 | — | 480 / — | 608 / — | hors table | hors table |
| 288 | 0 | 0,0088 | 0,0145 | 0.05 | 0.025 | 288 / 288 | 304 / 304 | 288 | 304 |
| 288 | 0,05 | 0,0123 | 0,0702 | 0.1 | 0.085 | 288 / 288 | 336 / 352 | 288 | 352 |
| 288 | 0,1 | 0,0150 | 0,1248 | 0.125 | 0.125 | 288 / 320 | 352 / 416 | 320 | 416 |
| 288 | 0,125 | 0,0168 | 0,1526 | 0.17 | 0.17 | 304 / 384 | 384 / 496 | 384 | 496 |
| 288 | 0,17 | 0,0182 | 0,1999 | 0.2 | 0.2 | 336 / 416 | 432 / 544 | 416 | 544 |
| 288 | 0,2 | 0,0191 | 0,2314 | 0.25 | — | 384 / — | 496 / — | hors table | hors table |
| 288 | 0,25 | 0,0209 | 0,2844 | 0.3 | — | 448 / — | 544 / — | hors table | hors table |

Premier ρ̂ hors table : N = 50 : 0.13 (les deux hypothèses), 0.26 (ρ_A = ρ_B seule) ; N = 100 : 0.15 (les deux hypothèses), 0.29 (ρ_A = ρ_B seule) ; N = 288 : 0.18 (les deux hypothèses), 0.31 (ρ_A = ρ_B seule)


Lecture, pilote de 288 unités, **les deux hypothèses** (règle de la v8) : ρ̂ = 0 → **288 / 304** ; ρ̂ = 0,05 → **288 / 352** ; ρ̂ = 0,10 → **320 / 416** ; ρ̂ = 0,17 →
**416 / 544** (ligne 0,20 dans les deux hypothèses : 336 / 432 sous ρ_A = ρ_B, 416 / 544 sous ρ_A = 2 ρ_B). Le premier ρ̂ hors table est **0,18 pour un pilote de 288 unités**, 0,15 pour 100 unités, 0,13 pour 50 unités (contre 0,07, 0,06 et 0,04 avec la grille de la v8 : GD8). Avec la seule hypothèse ρ_A = ρ_B, la table répond jusqu'à ρ̂ = 0,30 (288 unités), 0,28 (100), 0,25 (50).

**Phrases réécrites (tailles au ρ vrai et au ρ̂ lu, séparées)** :
- « **304 / 384 si ρ vrai = 0,17** (ρ_A = ρ_B) ; **384 / 496 si ρ vrai = 0,17 et ρ_A = 2 ρ_B**. »
- « **Si ρ̂ = 0,17 est lu sur 288 unités**, ρ_haut = 0,200 : ligne 0,20 dans les deux hypothèses, **n_h = 416 / 544** (336 / 432 sous la seule hypothèse ρ_A = ρ_B) ; au-delà de ρ̂ = 0,17 (288 unités), hors table. »
- Vérification de la phrase proposée par GD8 (« 384 / 496 si ρ̂ = 0,17 sur 288 unités ») : **exacte sur la grille de la v8** (ligne suivante 0,25 sous ρ_A = ρ_B,
  hypothèse 2 sans ligne) ; **sur la grille v9**, la ligne 0,20 existe et l'hypothèse ρ_A = ρ_B seule donne **336 / 432** ; avec l'hypothèse ρ_A = 2 ρ_B prolongée à ρ_B = 0,20, la règle rend **416 / 544**. Les chiffres « 384 / 496 » ne sont donc plus ceux de la v9 ; ils restent la réponse de la grille v8.
- Les phrases de la v8 « n_h = 288 jusqu'à ρ_B = 0,10, 304 à 0,17 (384 au seuil 160), 384 à 0,25 (496) » (§ 0.2 et § 6.1 de la v8) sont des tailles **au ρ vrai sous ρ_A = ρ_B** ;
  elles sont remplacées par les deux listes ci-dessus.

### 1.3 Repli hors table — options (à trancher par Lazar ; question liée à la porte G1 : **aucun défaut**)

*T8. Repli C (restriction à ρ_A = ρ_B) : puissance, dans un monde ρ_A = 2 ρ_B, à la taille lue sous ρ_A = ρ_B (même ρ_B)* (inséré depuis `tableaux-v9.md`)

Source : T1 ; puissance au pire des quatre cellules par les courbes logistiques ajustées sur les points de dichotomie du passage `double-…`/`moitie-…` (interpolation)

| ρ_B | ρ_A du monde | n_h 40 lu sous ρ_A = ρ_B | puissance (40) à cette taille, monde ρ_A = 2 ρ_B | n_h 160 lu sous ρ_A = ρ_B | puissance (160) à cette taille |
| --- | --- | --- | --- | --- | --- |
| 0,025 | 0,05 | 288 (ligne 0,05) | 0,996 | 304 | 0,938 |
| 0,05 | 0,1 | 288 (ligne 0,05) | 0,983 | 304 | 0,873 |
| 0,085 | 0,17 | 288 (ligne 0,1) | 0,928 | 336 | 0,847 |
| 0,1 | 0,2 | 288 (ligne 0,1) | 0,882 | 336 | 0,783 |
| 0,125 | 0,25 | 288 (ligne 0,125) | 0,783 | 352 | 0,723 |
| 0,17 | 0,34 | 304 (ligne 0,17) | 0,649 | 384 | 0,607 |
| 0,2 | 0,4 | 336 (ligne 0,2) | 0,643 | 432 | 0,627 |


Quand ρ̂ tombe hors table, aucune ligne simulée ne garantit une puissance de 0,8 dans l'une des deux hypothèses. Trois options, chiffrées pour un pilote de 288 unités
(seuil de déclenchement : ρ̂ ≥ 0,18 ; 0,15 pour 100 unités ; 0,13 pour 50) :

| option | règle | avantage | inconvénient | chiffres |
| --- | --- | --- | --- | --- |
| **A. Arrêt et nœud de décision** | hors table : on n'entre pas en G1 ; on rend ρ̂, son σ et la table à Lazar, qui décide (prolonger la grille, changer de plan, abandonner) | aucune taille n'est prise sans puissance simulée ; prolonger la grille ne coûte que du processeur (≈ 12 minutes par ligne sur deux processeurs) | délai ; une décision de plus avant G1 ; un pilote très dispersé arrête le calendrier | déclenchement à ρ̂ ≥ 0,18 (288 unités) ; aucun épisode engagé |
| **B. Taille maximale de la grille** | hors table : n_h = la plus grande taille de la table, scellée d'avance | pas d'arrêt ; règle mécanique | la garantie ne vaut que jusqu'aux dernières lignes (ρ_A = ρ_B = 0,35 ; ρ_A = 2 ρ_B à ρ_B = 0,20) ; au-delà, puissance inconnue, peut-être très basse ; coût élevé même si ρ̂ dépasse à peine le seuil | **480 / 608** unités (seuils 40 / 160), soit 64 800 / 82 080 épisodes à K_h = 5 (86 400 / 109 440 à K_h = 10) |
| **C. Restriction à ρ_A = ρ_B** | on lit la seule hypothèse ρ_A = ρ_B (raison : f_A n'est pas lue avant G1, le sujet joue les mêmes unités que les comparateurs, rien n'indique qu'il soit deux fois plus dispersé ; l'hypothèse 2 n'était qu'une sensibilité) | la table répond jusqu'à ρ̂ = 0,30 (288 unités) ; tailles plus petites | si le monde est ρ_A = 2 ρ_B, la puissance à la taille lue tombe (T8) : 0,783 / 0,723 à ρ_B = 0,125, **0,649 / 0,607** à 0,17, 0,643 / 0,627 à 0,20 ; c'est une hypothèse de revendication qu'on ne vérifie pas avant G1 | hors table seulement à ρ̂ ≥ 0,31 ; à ρ̂ = 0,17 : 336 / 432 au lieu de 416 / 544 |

**Ma recommandation : A** (confiance moyenne). Hors table veut dire que la dispersion mesurée dépasse tout ce qui a été simulé ; B donnerait une taille sans garantie au moment
même où la dispersion est la plus forte, C achète des tailles plus petites au prix d'une hypothèse non vérifiable sur le sujet (T8 : jusqu'à −0,2 de puissance). A ne coûte
qu'un délai, et la grille peut être prolongée sur processeur avant de reprendre. **Pas de défaut : c'est à Lazar de trancher (question liée à la porte G1).**

## 2. GD8-02 → le neuvième comparateur en n_h à neuf comparateurs et en écart des n_h

- **Où** : `tableaux-v9.py`, bloc T3 (`neuvieme_n_h` dans `tableaux-v9-sortie.json`) ; ce rapport § 0, § 10 et phrase du § 11. **Supprimées** : la phrase de la v8 « pour garder 0,8 il
  faut, en plus de la taille à huit comparateurs, +128 (sans dispersion) … » et la colonne « surcoût ».
- **Comment** : la v8 appelait « surcoût » le **maximum, sur les quatre cellules, de la différence par cellule** n80(9) − n80(8) ; ce n'est ni l'écart des n80 pires ni l'écart
  des tailles à prévoir. La v9 donne, pour chaque loi, le n80 pire et le **n_h** à huit et à neuf comparateurs (même règle que la table de lecture, ligne par ligne, sans
  enveloppe), et leur **écart**. Chiffres lus dans les sorties v8 (aucun passage nouveau) ; ils retrouvent exactement ceux de GD8.

*T3. Neuvième comparateur en n_h (GD8-02) : n_h à huit et à neuf comparateurs, écart des n_h* (inséré depuis `tableaux-v9.md`)

Source : passages v8 `rho0`, `meme-…`, `neuf-k8-…`, `neuf-k9-g0.05-…` (écart du neuvième 0,05 : SUPPOSÉ, « comparateur fort » ; côté honnête du neuvième inchangé : SUPPOSÉ) et `neuf-k9-g0.10-…` ; n80 pire (dichotomie) ; n_h = max(288 ; multiple de 16 ≥ 1,06 × n80 pire), ligne par ligne, sans enveloppe

| dispersion | n80 40 (8) | n80 40 (9, 0,05 SUPPOSÉ) | n80 40 (9, 0,10) | n_h 40 (8) | n_h 40 (9, 0,05 SUPPOSÉ) | écart n_h 40 | n_h 40 (9, 0,10) | n80 160 (8) | n80 160 (9, 0,05 SUPPOSÉ) | n_h 160 (8) | n_h 160 (9, 0,05 SUPPOSÉ) | écart n_h 160 | n_h 160 (9, 0,10) | fiche 288 pire (9, 0,05 SUPPOSÉ, seuil 40) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| nulle | 184 | 264 | 184 | 288 | 288 | +0 | 288 | 264 | 344 | 288 | 368 | +80 | 288 | 0,866 |
| ρ_A = ρ_B = 0,05 | 200 | 368 | 200 | 288 | 400 | +112 | 288 | 280 | 504 | 304 | 544 | +240 | 304 | 0,672 |
| bêta (σ de référence 1,0) | 212 | 456 | 212 | 288 | 496 | +208 | 288 | 280 | 624 | 304 | 672 | +368 | 320 | 0,534 |
| logit σ = 1,0 | 208 | 472 | 208 | 288 | 512 | +224 | 288 | 280 | 624 | 304 | 672 | +368 | 304 | 0,542 |
| ρ_A = ρ_B = 0,10 | 224 | 504 | 228 | 288 | 544 | +256 | 288 | 304 | 688 | 336 | 736 | +400 | 336 | 0,484 |
| ρ_A = ρ_B = 0,17 | 280 | 688 | 280 | 304 | 736 | +432 | 304 | 360 | 912 | 384 | 976 | +592 | 384 | 0,312 |


Lecture, **écart du neuvième 0,05 (SUPPOSÉ, « comparateur fort » ; côté honnête du neuvième inchangé : SUPPOSÉ)** :
- n_h à neuf comparateurs : **288 à 736 au seuil 40**, **368 à 976 au seuil 160** selon la dispersion ;
- écart des n_h : **+0 (sans dispersion) à +432 (ρ = 0,17) au seuil 40** ; **+80 à +592 au seuil 160**. Sans dispersion, n_h ne bouge pas au seuil 40 (288 → 288) alors que la
  fiche pire à 288 unités tombe à 0,866 : la taille plancher de 288 absorbe la perte, ce que le « +128 » de la v8 cachait.
- Le « +432 » de la v8 au seuil 40 à ρ = 0,17 coïncide par hasard avec l'écart des n_h ; au seuil 160 à ρ = 0,17, l'écart des n_h est **+592** (384 → 976), plus que le
  « +568 » de la v8.
- **Écart du neuvième 0,10 (comme les huit autres)** : n_h inchangé au seuil 40 pour toutes les lois ; au seuil 160, +16 en bêta σ = 1,0 (304 → 320), inchangé ailleurs.

## 3. GD8-04 → n80 par ajustement de la courbe de puissance ; puissances clés sur plusieurs graines ; ni « minorant » ni troncature

- **Où** : `tableaux-v9.py` (fonction `ajuster`, colonnes « n80 ajusté » de T1 et T5 ; bloc T4) ; passages `graine11-meme-rho0.17` à `graine18-meme-rho0.17` (script v9 final,
  `lancer-complements-v9.sh graines`).
- **n80 ajusté** : régression logistique binomiale logit P = a + b·n sur les points déjà évalués par la dichotomie de chaque cellule (puissances dans [0,5 ; 0,99], poids 2 000),
  n80 = (logit 0,8 − a)/b, écart-type par la méthode delta, multiplié par √(déviance/ddl) quand elle dépasse 1 (méthode de `ajustement-n80-gd8-v1.py`). Sur les 16 passages
  distincts de T1 : écart-type **0,4 à 2,3 unités** ; déviance par degré de liberté 0,19 à 1,85 ; le n80 de la dichotomie s'écarte du n80 ajusté de **−4 à +12 unités** (il rend la borne
  haute de son dernier pas, sur des points bruités : ce n'est pas toujours un majorant). Le « pire » ajusté est le plus grand des quatre n80 ajustés. **n_h reste calculé sur le
  n80 de la dichotomie** (règle v8 inchangée, lignes v8 reproduites) ; calculé sur le n80 ajusté, il serait égal dans 24 cas sur 34 (17 lignes × deux seuils, la ligne sans dispersion comptée
  deux fois), plus petit de 16 unités dans 9 cas et plus grand de 16 dans 1 cas (colonne de droite de T1) ; la marge 1,06 couvre largement l'écart-type de l'ajustement (≤ 1 %).
- La phrase de la v8 « incertitude de graine de 2,2 % au plus » est **retirée** : ce que la v8 mesurait était la résolution de la dichotomie (GD8-04) ; la v9 donne n80 à l'unité
  près avec son écart-type, et ρ = 0,17, seuil 40 : **275,6 ± 1,1** (une graine ; 276,7 ± 0,6 sur quatre graines réunies, GD8) contre 280 par dichotomie.
- **Puissances clés, moyenne sur neuf graines** (20261029 de la v8 et 11 à 18), ρ_A = ρ_B = 0,17 :

*T4. Puissances clés sur plusieurs graines (GD8-04) : ρ_A = ρ_B = 0,17, 288 et 400 unités* (inséré depuis `tableaux-v9.md`)

Source : passage v8 `meme-rho0.17` (graine 20261029) et passages v9 `graine11…18-meme-rho0.17` présents (9 graines) ; moyenne ± erreur type (écart-type entre graines / √nombre)

| taille | seuil | valeur v8 (graine 20261029) | pire des 4 cellules, par graine : moyenne ± erreur type | cellule la plus exigeante en moyenne : moyenne ± erreur type | cette cellule |
| --- | --- | --- | --- | --- | --- |
| 288 | 40 | 0,847 | 0,840 ± 0,003 | 0,840 ± 0,003 | K_h = 5, biais 0.0125 |
| 288 | 160 | 0,509 | 0,506 ± 0,003 | 0,506 ± 0,003 | K_h = 5, biais 0.0125 |
| 400 | 40 | 0,980 | 0,980 ± 0,001 | 0,981 ± 0,001 | K_h = 5, biais 0.0125 |
| 400 | 160 | 0,905 | 0,908 ± 0,002 | 0,908 ± 0,002 | K_h = 5, biais 0.0125 |


  Les valeurs de la v8 (0,847 ; 0,509 ; 0,980 ; 0,905) sont des tirages d'une graine : **0,847 est à 2,9 erreurs types au-dessus de la moyenne 0,8395 ± 0,0025** ; 0,509 à 1,0 erreur type au-dessus,
  0,905 à 1,7 au-dessous, 0,980 au centre. Valeurs à citer au préenregistrement : **0,840 ± 0,003 ; 0,506 ± 0,003 ; 0,980 ± 0,001 ; 0,908 ± 0,002** (pire des quatre cellules, par
  graine, moyenne ± erreur type sur neuf graines) ; GD8 trouvait de même ≈ 0,838 et ≈ 0,50 sur 21 graines pour la cellule la plus exigeante.
- **Arrondi** : toutes les puissances de la v9 sont arrondies au plus proche à trois décimales ; « tronqué » et « minorant » sont retirés.

## 4. GD8-07 → ρ honnête = 2 × ρ saboté : option au script, effet borné, condition de validité

- **Où** : `simulation-puissance-garde-delta-v9.py`, option `--facteur-rho-honnetes F` (défaut 1 : sans effet ; refusée sans dispersion bêta combinée, avec la copule, les strates,
  le neuvième comparateur, `--lien-coupe`, des fichiers réels, ou si F·ρ ≥ 1) ; le côté honnête de A **et** des comparateurs prend la corrélation F·ρ, le côté saboté garde ρ ;
  passages `rhoh2x-meme-rho0.05`, `-0.10`, `-0.17` (options R1 de la v8, F = 2) ; essais (sain : corrélations de la décomposition et écarts-types tirés conformes ; six
  artefacts refusés) dans `essais-gd8-03-07-08-v9-sortie.json`.
- **Résultat (scénario SUPPOSÉ : faux positifs concentrés sur des unités honnêtes difficiles)** :

*T5. ρ honnête = 2 × ρ saboté (GD8-07, SUPPOSÉ) contre ρ honnête = ρ saboté (v8)* (inséré depuis `tableaux-v9.md`)

Source : passages v9 `rhoh2x-meme-rho…` (`--facteur-rho-honnetes 2`) et v8 `meme-rho…` ; pire des quatre cellules

| ρ saboté (A et B) | ρ honnête | fiche 288 (40) | fiche 288 (160) | n80 40 | n80 160 | n80 160 ajusté | n_h 40 | n_h 160 | garde min. 8, 288, seuil 160 (K_h 5, δ/4) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0,05 | 0,05 | 0,995 | 0,869 | 200 | 280 | 272,1 ± 0,6 | 288 | 304 | 0,880 |
| 0,05 | 0,1 | 0,987 | 0,835 | 208 | 288 | 283,5 ± 0,6 | 288 | 320 | 0,847 |
| 0,10 | 0,1 | 0,971 | 0,768 | 224 | 304 | 297,7 ± 0,7 | 288 | 336 | 0,845 |
| 0,10 | 0,2 | 0,922 | 0,654 | 240 | 328 | 321,4 ± 1,0 | 288 | 352 | 0,716 |
| 0,17 | 0,17 | 0,847 | 0,509 | 280 | 360 | 357,0 ± 1,0 | 304 | 384 | 0,751 |
| 0,17 | 0,34 | 0,735 | 0,379 | 312 | 408 | 401,0 ± 1,0 | 336 | 448 | 0,567 |


  Au seuil 160, doubler le ρ honnête relève le n80 pire de **+8 (ρ saboté 0,05), +24 (0,10) et +48 (0,17)** unités (ajusté : +11, +24, +44) et n_h de +16, +16 et **+64**
  (304 → 320, 336 → 352, 384 → 448) ; au seuil 40, n_h ne change pas à ρ ≤ 0,10 (288) et passe de 304 à 336 à 0,17. La garde est le maillon touché : minimum des 8 gardes
  à 288 unités, seuil 160, K_h = 5, biais δ/4 : 0,845 → 0,716 (ρ = 0,10), 0,751 → 0,567 (ρ = 0,17).
- **Condition de validité à écrire au préenregistrement** : la table est lue côté sabotage et suppose le même ρ côté honnête ; si le ρ honnête est le double, elle sous-estime
  n_h de 16 unités jusqu'à ρ̂ ≈ 0,10 et de 64 unités (seuil 160) à 0,17. Le côté honnête n'est pas lisible au pilote (écart-type de ρ̂ 0,047 à 0,071 sur 288 unités, v8) : on ne
  peut pas vérifier cette condition avant G1 ; on peut seulement la borner (ce paragraphe) ou ajouter la marge correspondante.

## 5. GD8-03 → strates : « commune » comme témoin de construction, parts de variance, portée partielle, décalages fixés d'avance

- **Où** : `tableaux-v9.py`, blocs T6 et T7 (lecture des `moments_tires` des passages v8 de strates) ; option nouvelle `--portee-strates partielle --fraction-strates-comparateurs f`
  du script v9 (γ_B = f·γ_A ; essais sain et quatre artefacts dans `essais-gd8-03-07-08-v9-sortie.json`) ; passages `strates-partielle-f0.5-S2|S3-g0.4-brut|calibre`.
- **La portée « commune » est un témoin de construction, non une mesure** : la strate multiplie les espérances du sujet et des comparateurs ; l'étalonnage ne retire du contraste
  que (0,50 − 0,40)·γ·d, soit **2,7 % (deux strates) et 1,3 % (trois strates)** de sa variance ; le gain nul (−0,001 ; +0,001) est voulu par le modèle. Surtout, à ρ total tenu,
  la strate commune est une **difficulté partagée** par le sujet et les comparateurs : corrélation de leurs probabilités côté sabotage 0,5·0,4·γ²·moyenne(d²)/√(0,17·0,25 × 0,17·0,24)
  = **0,77 (deux strates) et 0,51 (trois strates)**, l'équivalent de la copule c ≈ 0,8 et 0,5 du § 3.1 de la v8. **C'est pourquoi sa fiche brute est haute** (0,991 et 0,984 en
  moyenne des quatre cellules, contre 0,847 au pire et 0,865 en moyenne des quatre cellules sans strate, passage v8 `meme-rho0.17`) : elle décrit un autre monde que la référence, et ne se compare pas à 0,847.
- **Parts de variance de la portée « sujet »** (T6) : la strate explique, côté sabotage, **94 % (deux strates, γ = 0,4), 63 % (trois, γ = 0,4), 24 % (deux, γ = 0,2) et 16 %
  (trois, γ = 0,2)** de la variance inter-unités de A, et **≤ 1 %** côté honnête ; elle porte 32 %, 22 %, 8 % et 5 % de la variance du contraste, ≤ 0,3 % de celle de la garde.
  Le meilleur gain de la v8 (+0,054 à 288 unités) suppose donc une covariable connue d'avance qui explique **63 % de la dispersion du sujet saboté** ; la garde n'en est pas touchée.

*T6. Strates (GD8-03) : parts de variance et corrélation sujet–comparateurs (v8, cellule K_h = 10, biais 0, 288 unités)* (inséré depuis `tableaux-v9.md`)

Source : `moments_tires` et `decomposition_effet_unite` des passages v8 de strates ; corrélation des p sabotés de A et des comparateurs en portée commune : 0,5·0,4·γ²·moyenne(d²)/√(ρ·0,25 × ρ·0,24) (calcul de GD8-03), recalculée ici

| passage | part de variance de p_A entre strates, sabotés | idem, honnêtes | part de variance du contraste prévue par les strates | idem, garde | corr. p_A–p_B sabotés calculée (commune) | fiche 288 (40), moyenne des 4 cellules (mesure du tableau v8) | fiche 288 (40), pire des 4 cellules |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `strates-commune-S2-g0.4-brut` | 0,941 | 0,010 | 0,027 | 0,000 | 0,768 | 0,991 | 0,967 |
| `strates-commune-S2-g0.4-calibre` | 0,941 | 0,010 | 0,027 | 0,000 | 0,768 | 0,990 | 0,966 |
| `strates-commune-S3-g0.4-brut` | 0,627 | 0,006 | 0,013 | 0,000 | 0,512 | 0,984 | 0,954 |
| `strates-commune-S3-g0.4-calibre` | 0,627 | 0,006 | 0,013 | 0,000 | 0,512 | 0,985 | 0,965 |
| `strates-partielle-f0.5-S2-g0.4-brut` | 0,941 | 0,010 | 0,157 | 0,001 | — | 0,982 | 0,961 |
| `strates-partielle-f0.5-S2-g0.4-calibre` | 0,941 | 0,010 | 0,157 | 0,001 | — | 0,986 | 0,962 |
| `strates-partielle-f0.5-S3-g0.4-brut` | 0,627 | 0,006 | 0,094 | 0,001 | — | 0,959 | 0,928 |
| `strates-partielle-f0.5-S3-g0.4-calibre` | 0,627 | 0,006 | 0,094 | 0,001 | — | 0,967 | 0,942 |
| `strates-sujet-S2-g0.2-brut` | 0,235 | 0,002 | 0,081 | 0,001 | — | 0,874 | 0,841 |
| `strates-sujet-S2-g0.2-calibre` | 0,235 | 0,002 | 0,081 | 0,001 | — | 0,910 | 0,887 |
| `strates-sujet-S2-g0.4-brut` | 0,941 | 0,010 | 0,322 | 0,003 | — | 0,933 | 0,922 |
| `strates-sujet-S2-g0.4-calibre` | 0,941 | 0,010 | 0,323 | 0,003 | — | 0,979 | 0,944 |
| `strates-sujet-S3-g0.2-brut` | 0,157 | 0,002 | 0,054 | 0,001 | — | 0,869 | 0,840 |
| `strates-sujet-S3-g0.2-calibre` | 0,157 | 0,002 | 0,054 | 0,001 | — | 0,894 | 0,871 |
| `strates-sujet-S3-g0.4-brut` | 0,627 | 0,006 | 0,215 | 0,002 | — | 0,907 | 0,878 |
| `strates-sujet-S3-g0.4-calibre` | 0,627 | 0,006 | 0,215 | 0,002 | — | 0,961 | 0,934 |
| `strates-sujet-S3-g0.4-iid-brut` | 0,627 | 0,006 | 0,215 | 0,002 | — | 0,857 | 0,823 |


- **Portée partielle (γ_B = 0,5 γ_A, nouvelle)** : la strate déplace A deux fois plus que les comparateurs ; l'étalonnage retire 9,4 % (trois strates) et 15,7 % (deux strates)
  de la variance du contraste, mais le gain reste **+0,009 et +0,004** à 288 unités (moyenne des quatre cellules ; −0,000 à 400), parce que la part commune de la strate joue
  déjà comme une difficulté partagée (fiche brute 0,959 et 0,982) :

*T7. Strates : gain de l'étalonnage selon la portée (commune, partielle f = 0,5, sujet), ρ = 0,17, S ∈ {2 ; 3}, γ_A = 0,4 (GD8-03)* (inséré depuis `tableaux-v9.md`)

Source : passages v8 `strates-commune-…`, `strates-sujet-…` et v9 `strates-partielle-f0.5-…` (brut et étalonné) ; fiche au seuil 40, moyenne des quatre cellules (mesure de la v8) et pire des quatre ; gain = étalonné − brut (moyenne des quatre différences)

| portée | S | γ_B | fiche 288 brut (moy.) | fiche 288 étalonné (moy.) | gain 288 | fiche 288 étalonné (pire) | gain 400 | part de variance du contraste retirée par l'étalonnage |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| commune | 2 | 0,4 | 0,991 | 0,990 | −0,001 | 0,966 | −0,000 | 0,027 |
| commune | 3 | 0,4 | 0,984 | 0,985 | +0,001 | 0,965 | +0,000 | 0,013 |
| partielle | 2 | 0,2 | 0,982 | 0,986 | +0,004 | 0,962 | −0,000 | 0,157 |
| partielle | 3 | 0,2 | 0,959 | 0,967 | +0,009 | 0,942 | −0,000 | 0,094 |
| sujet | 2 | 0 | 0,933 | 0,979 | +0,046 | 0,944 | +0,003 | 0,323 |
| sujet | 3 | 0 | 0,907 | 0,961 | +0,055 | 0,934 | +0,004 | 0,215 |


  Lecture : le gain de l'étalonnage croît avec la part de la strate propre au sujet (commune 0 → partielle ≤ +0,009 → sujet +0,046 à +0,055), et s'efface à 400 unités dans
  tous les cas (≤ +0,004). La recommandation de la v8 (« ne pas compter sur les strates pour dimensionner ») est inchangée.
- **Règle pour le préenregistrement, si l'étalonnage par strate devait servir** : décalages de strate **fixés avant l'épreuve** (pilote ou construction), jamais estimés sur les
  unités de l'épreuve (sinon le processus de pari n'est plus prévisible) ; écrêtage à [−1 ; 1] avant le pari (§ 6).

## 6. GD8-05 → vérification de l'écrêtage refaite au critère scindé déclaré d'avance ; convention pour le préenregistrement

- **Où** : `verif-ecretage-v9-critere.md` (critère, scellé à 03:23 UTC **avant** toute exécution, empreinte `a0da3b4c…`), `verif-ecretage-v9.py` (le script refuse de tourner si
  le critère a changé depuis son scellement), sorties `verif-ecretage-v9-sortie.json` (script v9 intermédiaire `-etape1`) et `verif-ecretage-v9-v2-sortie.json` (script v9 final),
  journaux et manifestes ; `echecs-verif-ecretage-v8/` (sorties échouées de la v8 retrouvées).
- **Sorties échouées de la v8 (règle R11 : vérifié sur disque avant de déclarer absent)** : la consigne les disait absentes ; une recherche sur tout le disque (hors chemins
  interdits) en a **retrouvé trois sur quatre** dans l'espace de travail de la lignée (`travail-v8/ebh-pole-essai1`, `-essai2`, `-essai3`, sortie et journal chacune, script v8
  `4c7c93a9…`, toutes `"conforme": false`) ; elles sont **versées** dans `echecs-verif-ecretage-v8/` avec leurs compagnons. La quatrième, l'exécution **plantée** (écart étalonné
  hors de [−1 ; 1] refusé par le juge), n'a laissé **aucune sortie** : elle est absente, et le reste. Les essais 2 et 3 montrent les cinq cellules à écart non nul toutes à
  K_h = 3 (hors périmètre), écart de trajectoire ≤ 0,088.
- **Comment** : deux conventions sur les mêmes tirages — (S) simulation : δ − g_étalonné écrêté à [−1 ; 1] ; (J) juge : g_étalonné écrêté, puis δ − g. Critère C1
  (périmètre : K_h ∈ {5 ; 10} × S ∈ {2 ; 3} × portée commune ou sujet × biais 0 ou δ/4, soit **16 cas** ; 288 unités, k = 8, 2 000 répétitions ; **erreur de
  décompte dans le critère scellé** : il écrit « 32 cas », alors que son énumération en donne 16 ; la vérification porte sur les 16 cas énumérés ; je ne réécris pas le
  critère scellé et je signale l'erreur ici) : part des gardes hors de [−1 ; 1] < 10⁻³, |écart de puissance des 8 gardes| ≤ 0,003 aux seuils 40 et 160, contrastes identiques ; C2 (K_h ∈ {2 ; 3}) :
  descriptif seulement. **Résultat : 16 / 16 conformes**, deux fois (script intermédiaire et script final, résultats identiques champ à champ) ; plus grand écart de puissance
  0,0000 au seuil 40 et 0,0005 au seuil 160 (une répétition sur 2 000), part des gardes hors de [−1 ; 1] au plus 1,2 × 10⁻⁴, contrastes identiques. Hors périmètre (descriptif) : K_h = 2, part hors intervalle 9,1 × 10⁻⁴, écart −0,001 au seuil 160 ; K_h = 3 : 2,7 × 10⁻⁴, écart 0.
- **Convention proposée pour le préenregistrement**, si l'étalonnage par strate devait servir : « les décalages de strate sont **fixés avant l'épreuve** (sur le pilote ou
  par construction), jamais estimés sur les unités de l'épreuve ; l'écart étalonné de garde g − décalage et de contraste v − décalage est **écrêté à [−1 ; 1] avant le pari**
  (convention du juge) ; l'écrêtage par en bas d'un contraste étalonné relève légèrement sa moyenne (sens non prudent, ici ≤ 10⁻⁴ × 0,2) et la part des valeurs écrêtées est
  rapportée ».

## 7. GD8-06 → « SUPPOSÉ » partout pour le neuvième comparateur

- **Où** : ce rapport (résumé, § 2, § 10, phrase du § 11), `tableaux-v9.md` (T3 : en-têtes de colonne « 0,05 SUPPOSÉ » et source), docstring de `lancer-complements-v9.sh`
  pour le ρ honnête.
- **Comment** : chaque mention de l'écart 0,05 du neuvième comparateur porte « SUPPOSÉ » ; l'hypothèse **« côté honnête du neuvième inchangé (f_B9 = τ) » est écrite comme
  SUPPOSÉE** : un comparateur « fort » qui alerte plus sur les sabotés alerte vraisemblablement plus aussi sur les honnêtes, ce qui abaisserait sa garde ; non simulé.

## 8. GD8-08 → fiche nulle avec neuvième comparateur : refus nommé

- **Où** : `simulation-puissance-garde-delta-v9.py` (`principal` : refus de `--fiches-nulles N > 0` avec `--ecart-contraste-neuvieme` ; `variante_nulle` transmet désormais
  `ecart9`, le facteur honnête et la fraction de strates, et `tirer` refuse une variante nulle à neuvième particulier : garde de second rang) ; essais
  `essais-gd8-03-07-08-v9.py`, sortie `essais-gd8-03-07-08-v9-sortie.json`.
- **Comment** : j'ai choisi le refus plutôt que la transmission silencieuse, parce que la fiche nulle d'un neuvième « fort » n'est pas définie (écart nul pour les neuf ? ou
  neuvième gardant son décalage, ce qui donnerait un contraste non nul ?) ; trancher serait un choix de modèle. Essais (règle R5) : sain — neuvième sans fiche nulle, code 0 ;
  fiche nulle sans neuvième, code 0 ; variante nulle tirée à k = 8, tirage fait ; artefact — la commande exacte de GD8, refus nommé « GD8-08 », aucun fichier laissé ;
  variante nulle tirée à k = 9, refus de la loi. **5 / 5 conformes** (dans 17 / 17 au total).

## 9. GD8-09 → manifestes, commit

- **Où** : chaque script auxiliaire de la v9 (`precision-rho-pilote-v9.py`, `verif-identite-v8-v9-v3.py`, `essais-gd8-03-07-08-v9.py`, `verif-ecretage-v9.py`, `tableaux-v9.py`,
  `construire-rapport-v9.py`) écrit **son propre manifeste** (`manifeste-<sortie>.json` : commande, empreinte du script, graines, versions, empreintes des fichiers écrits) ;
  manifeste d'ensemble `manifeste-puissance-garde-delta-v9.json` (`assembler-manifeste-v9.py`).
- **Commit** : lu par l'appelant, hors des scripts, par `git -C /home/claude/controle-ia-travail rev-parse HEAD` (lecture seule) = `0c8e1c8a991fddc15b62890b5454d0fb7472faff`,
  passé à chaque passage (`--commit-declare`) et à chaque script auxiliaire, écrit dans chaque manifeste. La seule autre commande git lancée : `git show` et `git ls-tree` sur
  `origin/main` pour copier la contre-lecture GD8 (`entrees-gd8/`, empreintes identiques à celles d'`origin/main`) ; `origin/main` = `390ba1c1…` au moment de la copie.
- Versions : Python 3.13.18, numpy 2.5.3, scipy 1.18.1, les mêmes que la v8, pour tous les passages.

## 10. Réserves

1. **Lois synthétiques ; ρ, c, γ, f, le facteur honnête et l'écart 0,05 du neuvième sont des scénarios (SUPPOSÉ)**, pas des estimations ; f_A n'est pas lue avant G1. Le même ρ pour A
   et les comparateurs (hypothèse 1) et ρ_A = 2 ρ_B (hypothèse 2) bornent deux scénarios ; ρ_A > 2 ρ_B n'est pas couvert ; 0 < ρ_A < ρ_B n'est pas passé (attendu plus favorable).
2. **La table en ρ̂ suppose le même ρ côté honnête et côté sabotage** (une seule concentration) ; le § 4 borne l'écart pour un ρ honnête double ; au-delà, c'est une
   **condition de validité** de la table à écrire au préenregistrement.
3. **La marge de lecture 1,645 × σ** prend σ au plus petit ρ de la grille de précision au moins égal à ρ̂ (côté prudent) ; c'est une borne unilatérale à 95 % sous la loi bêta
   simulée, sans correction pour la non-normalité de ρ̂ (asymétrique à petit N) ni pour le choix de la ligne (pas de la grille).
4. **n_h reste calculé sur le n80 de la dichotomie** (règle v8, pour que les lignes v8 se reproduisent) ; l'ajustement logistique (GD8-04) le confirme à quelques unités près ;
   la colonne « n_h depuis n80 ajusté » de T1 dit où l'arrondi au multiple de 16 changerait.
5. **Les passages de la grille prolongée (GD8-01) sont exécutés par le script v8 scellé, inchangé** (empreinte `4c7c93a9…`), lu dans le dossier v8 ; ceux des compléments
   (graines, ρ honnête, portée partielle) par le script v9 final (`f483a271…`). L'identité v8 = v9 hors options nouvelles est vérifiée (cinq configurations, 0 différence ;
   témoin négatif vu).
6. **Un script v9 intermédiaire** (`simulation-puissance-garde-delta-v9-etape1.py`, `3232a994…`, avant l'ajout de la portée partielle) a servi aux premiers essais
   (`verif-identite-v8-v9`, `essais-gd8-07-08-v9`, `verif-ecretage-v9` sans suffixe) ; gardé et remplacé (R12). **Un échec à déclarer** : la première version du script final
   refusait toute loi sans strates (garde `(strates and …) != …` mal écrite) ; vu par `verif-identite-v8-v9-v2` (sortie conservée, `"conforme": false`), corrigé, revérifié par
   `verif-identite-v8-v9-v3` (conforme).
7. **Erreur dans le critère scellé de l'écrêtage** : « 32 cas » pour 16 énumérés (§ 6) ; non réécrit.
8. **Seuil 160** : borne basse de la retenue par la règle e-BH à m = 8, non simulée ; lecture (A) à deux modes seulement (réserves de la v6 à la v8, inchangées).
9. **Coûts en épisodes** : plan apparié supposé, 135 épisodes par unité à K_h = 5 (180 à K_h = 10 ; 150 avec un neuvième comparateur à K_h = 5) ; aucun montant en argent.
10. **Une fin de chaîne échouée, à déclarer** : la première exécution de `lancer-final-v9.sh` écrivait son journal dans le dossier pendant qu'elle le scellait ; le
    constructeur du rapport a refusé (compagnon en écart). Ses deux produits sont gardés sous `manifeste-puissance-garde-delta-v9-echec1.json` et
    `lancer-final-v9-echec1-journal.txt` ; la seconde exécution écrit son journal hors du dossier, versé ensuite sous `lancer-final-v9-v2-journal.txt`.
11. **Non relu par une autre main (règle R2)** : à regarder en premier : la règle de lecture en ρ̂ (`tableaux-v9.py`, fonctions `sd` et `ligne`), le choix de σ, les options de repli,
    la branche `facteur_h` de `tirer` et de `decomposition`, la portée partielle (`_gamma_b`, `_b_applique`).

## 11. Phrase proposée pour le préenregistrement de G1 (compatible avec GD8-01 à GD8-09 ; valeurs à trancher par Lazar)

« Sous lois synthétiques non préenregistrées (simulation v9, 2 000 répétitions, graine 20261029 ; puissances clés moyennées sur neuf graines), à τ = 0,01, δ = 0,05, huit
comparateurs, écart de contraste 0,10, K_s = 10, lecture (A), K_h ∈ {10 ; 5} et biais ≤ δ/4, si le sujet et les comparateurs ont la même dispersion d'unité bêta de corrélation
intra-unité ρ = 0,17, la puissance de la fiche au pire de ces quatre cellules vaut 0,840 ± 0,003 au seuil 40 et 0,506 ± 0,003 au seuil de référence 160 à n = 288 unités, et
0,980 ± 0,001 et 0,908 ± 0,002 à n = 400 (moyenne ± erreur type sur neuf graines). **La taille n_h est lue sur la dispersion ρ̂ mesurée au pilote côté sabotage** (K = 10
épisodes par unité), par la table de lecture v9 : ρ_haut = ρ̂ + 1,645 × écart-type de lecture, ligne égale ou immédiatement supérieure dans chacune des deux hypothèses
ρ_A = ρ_B et ρ_A = 2 ρ_B, n_h = la plus grande des deux ; pour un pilote de 288 unités, ρ̂ = 0 ; 0,05 ; 0,10 ; 0,17 donnent n_h = 288, 288, 320, 416 au seuil 40 et 304, 352, 416,
544 au seuil 160 ; au ρ vrai de 0,17, n_h vaudrait 304 / 384 (ρ_A = ρ_B) et 384 / 496 (ρ_A = 2 ρ_B). Au-delà de ρ̂ = 0,17 (288 unités), la table ne répond pas et
[repli : option A, B ou C du rapport v9, § 1.3, choisie par Lazar avant le scellement]. La table suppose la même corrélation intra-unité côté honnête et côté sabotage ; un ρ
honnête double (SUPPOSÉ) relèverait n_h de 16 unités au seuil 160 jusqu'à ρ = 0,10 et de 64 à 0,17. Un neuvième comparateur d'écart de contraste 0,10 ne change pas ces tailles
(+16 unités au plus) ; à écart 0,05 (SUPPOSÉ, côté honnête du neuvième inchangé : SUPPOSÉ), n_h à neuf comparateurs vaut 288 à 736 au seuil 40 et 368 à 976 au seuil 160
selon la dispersion, soit un écart de +0 à +432 et de +80 à +592 unités. Si un étalonnage par strate sert, ses décalages sont fixés avant l'épreuve et l'écart étalonné est
écrêté à [−1 ; 1] avant le pari. »

Chiffres derrière la phrase : T4 (0,840 ; 0,506 ; 0,980 ; 0,908, `tableaux-v9-sortie.json`, bloc `puissances_cles_graines`) ; T2-points (lectures en ρ̂, bloc `table_rho_chapeau`) ;
T1 (tailles au ρ vrai, bloc `table_rho_vrai`) ; T2-288 (premier hors table 0,18 : bloc `premier_hors_table`) ; T5 (bloc `rho_honnete_double`) ; T3 (bloc `neuvieme_n_h`) ; § 6.

## 12. Fichiers et empreintes

Entrées en lecture seule : le dossier v8 (script `simulation-puissance-garde-delta-v8.py` `4c7c93a9…`, sorties des passages, `precision-rho-pilote-v8-sortie.json`), empreintes
dans `manifeste-puissance-garde-delta-v9.json` (bloc `entrees_v8`) ; contre-lecture GD8 copiée dans `entrees-gd8/`. Remplacés avant toute transmission, gardés (R12) :
`simulation-puissance-garde-delta-v9-etape1.py`, `verif-identite-v8-v9*.py` et sorties (`-v3` fait foi), `essais-gd8-07-08-v9*` (remplacé par `essais-gd8-03-07-08-v9*`),
`verif-ecretage-v9-sortie.json` (remplacé par `-v2`), dossiers `essais-v9/`, `essais-v9-v2/` (`essais-v9-v3/` et `essais-gd8-v9-v2/` font foi). Le rapport lui-même a son
compagnon `rapport-puissance-garde-delta-v9.md.sha256` et son manifeste `manifeste-rapport-puissance-garde-delta-v9.json`.

236 fichiers, chacun avec son compagnon `.sha256` (vérifié à la construction : 0 écart, 0 manquant).

| fichier | sha256 |
| --- | --- |
| `assembler-manifeste-v9.py` | `ec518da1a64864660cff27bfb928627d3e5656349c56ad8511a8901b3b6094c1` |
| `construire-rapport-v9.py` | `1b45cd55fadc37e1957fb7b5826a195fffe3a66183904593fa27d5ce918150c5` |
| `essais-gd8-03-07-08-v9-sortie.json` | `e7501ea78cddbf7a8a9ce7e6def5487438554ead41bc5de36e483f78c4dd6e14` |
| `essais-gd8-03-07-08-v9.py` | `4ea5093b114e7e0cd796ba107bf748d7f3f2211fbef9ee8e6e88e950663129b1` |
| `essais-gd8-07-08-v9-sortie.json` | `544dd4606cae47a11240beac1dd54a01b58c4b3d410753aec86453332b5ece89` |
| `essais-gd8-07-08-v9.py` | `870f08f9f72c312f9500682c5a0aa8101d4102887a1fc280851c69609e6d0759` |
| `lancer-complements-graines-journal.txt` | `d30ccf9cb236129997ab61cc599b8b3f1bab40f6d67cfe5b482fe6d7348bc7f6` |
| `lancer-complements-partielle-journal.txt` | `498ea38dc105ba7b815b0c5a55b8a83957ef135c4f9f91fe801e8088e2dd22f3` |
| `lancer-complements-rhoh-journal.txt` | `4c82d28d278f130fb0f8cea9186fd21a14ccb4045e0a9d1fa39db3c52247a291` |
| `lancer-complements-v9.sh` | `b716faf4ef47c8f346118eea3f5f8361800422d61c7a1a8d99e2ed6dc2b86154` |
| `lancer-final-v9-echec1-journal.txt` | `4b1acc12506a55cddbb3f2d56e71061f730c1eb9eb28a239a40e143cd08b8d37` |
| `lancer-final-v9-v2.sh` | `5a4be0e8afcf94eb6cb9a30957da25c7f3de91a9b2e1edd5842ec485b9d4ae76` |
| `lancer-final-v9.sh` | `d01b4ecf944fb9664e32b134527bf079fa8cc951c5daa3430c0fbc51f06e0be0` |
| `lancer-grille-voie1-journal.txt` | `462c4ed252689ab8bda24c355a2147806b2fda22f66aa9783a14846c976d8e1f` |
| `lancer-grille-voie2-journal.txt` | `0ab17eddc597fa740d297596b82b7d7862da762ce3d4d8ea36d4653392e25056` |
| `lancer-grille-voie3-journal.txt` | `620830ceee602b0f42903613043297f044c678cf28ceb3c68b407063a03e4242` |
| `lancer-passages-grille-v9.sh` | `0dce46f6cf096fdfe38c67fe1b9c6fda969aa95002f0a0880c0d1668f5e348db` |
| `manifeste-essais-gd8-03-07-08-v9-sortie.json` | `8c21907ece9084654109f91d187765e45cc8cc97df53916ddf71ed7ec62f8c60` |
| `manifeste-essais-gd8-07-08-v9-sortie.json` | `6b829b62eaa7a84757c39019e163645f34a085eb69ebe942f79edc6a2bf8de6e` |
| `manifeste-precision-rho-pilote-v9-sortie.json` | `685a5af0c6c183946fb96576746d4714fadd37b4e31a7b18edae3766c58f6582` |
| `manifeste-puissance-garde-delta-v9-echec1.json` | `47dd96425fbca62d96ca02802ae837379163df2c90831b8bd80cdb091efcd281` |
| `manifeste-puissance-garde-delta-v9.json` | `aafe796d79b2155773ee9dbcc8815083d539a11201ac8d5e3837aaad77f11cdf` |
| `manifeste-simulation-puissance-garde-delta-v9-sortie-double-rhoB0.10.json` | `3b20bfa2273cb2634d3158e636f03afb2b0ffa76c3034080ebe9bfcb314ae81e` |
| `manifeste-simulation-puissance-garde-delta-v9-sortie-double-rhoB0.125.json` | `c9261d75611c74f2e3506118515cc1954f6cb80e336fde29c6dc347b47d411dd` |
| `manifeste-simulation-puissance-garde-delta-v9-sortie-double-rhoB0.17.json` | `dab6d3435f1e4cc77f57b01622caed86fe08dcf72e8042310b4284fc73bcfd6f` |
| `manifeste-simulation-puissance-garde-delta-v9-sortie-double-rhoB0.20.json` | `62036a18ab92be29222cca7a13565b7da699ceaf6454ef70426df5b31186d251` |
| `manifeste-simulation-puissance-garde-delta-v9-sortie-graine11-meme-rho0.17.json` | `67827075d34e7ae115e86929ebbb119d141b1d2d457a90739f15562f68fcf5d2` |
| `manifeste-simulation-puissance-garde-delta-v9-sortie-graine12-meme-rho0.17.json` | `a99282131c3ddfdf48e3bc65602ad108ab1b4fb3e39b750ea5b3f46a915bfe91` |
| `manifeste-simulation-puissance-garde-delta-v9-sortie-graine13-meme-rho0.17.json` | `ca782e1b3fec31416476ae6e87dc6c8728aed6d6d94c9c497926a66fc9ba9a55` |
| `manifeste-simulation-puissance-garde-delta-v9-sortie-graine14-meme-rho0.17.json` | `178412e3dbbb35b077a83e6868ba7ca5ab6fd27e7b4ce8556b13127cf15b197d` |
| `manifeste-simulation-puissance-garde-delta-v9-sortie-graine15-meme-rho0.17.json` | `fdfa08350b55eea821b88b63ba961104686583bb8e1e8b2eb9a965c90bc19e33` |
| `manifeste-simulation-puissance-garde-delta-v9-sortie-graine16-meme-rho0.17.json` | `408a8b5bf52f651bf42567f2372f1bab4e35c8d939b2058bbcac4337bc2a1a38` |
| `manifeste-simulation-puissance-garde-delta-v9-sortie-graine17-meme-rho0.17.json` | `5b6d62043ae227d003c3f7d87b79713e1a2b858943d6906790807d2ce594eefa` |
| `manifeste-simulation-puissance-garde-delta-v9-sortie-graine18-meme-rho0.17.json` | `11b49fa3d341f14ec3cae403ac83745f22a72ebd24d14e2d09f869863ed49c3f` |
| `manifeste-simulation-puissance-garde-delta-v9-sortie-meme-rho0.125.json` | `507e762623e7ff19f709152cb814bfd0fe9c0f0dc8dfe7f2536e9cd4a4a6774d` |
| `manifeste-simulation-puissance-garde-delta-v9-sortie-meme-rho0.20.json` | `ab2c5fa40fd98dcdde27e8e8902422165660189f8b8c961a94256aec82994983` |
| `manifeste-simulation-puissance-garde-delta-v9-sortie-meme-rho0.30.json` | `8f4225ece79421991495c2ee19a43a4036adda8c1263320bf783b09e74e8429b` |
| `manifeste-simulation-puissance-garde-delta-v9-sortie-meme-rho0.35.json` | `8e7aa1b849616547d1eaf9cc6697e7fbcf4dfdebc41d7506227b3b9fb39f009c` |
| `manifeste-simulation-puissance-garde-delta-v9-sortie-rhoh2x-meme-rho0.05.json` | `26628279f55fe6129ab6019e622f50ef3b77f09b7e50062b8741e69aca8a4514` |
| `manifeste-simulation-puissance-garde-delta-v9-sortie-rhoh2x-meme-rho0.10.json` | `bcf198c58c72d1c520ccfbb1ee5190a7c426ae9fedd5ad55758294148e27e225` |
| `manifeste-simulation-puissance-garde-delta-v9-sortie-rhoh2x-meme-rho0.17.json` | `5315381633ee63fc19fc18344de248f3b7190ddd721c7191c263bd86d34c32dd` |
| `manifeste-simulation-puissance-garde-delta-v9-sortie-strates-partielle-f0.5-S2-g0.4-brut.json` | `8c3e33f644f8cd2310b2e6fab3bb1d8878e6db6c399b2ee25b4cdf1e9fa3a9f3` |
| `manifeste-simulation-puissance-garde-delta-v9-sortie-strates-partielle-f0.5-S2-g0.4-calibre.json` | `a92a8c97cacba53715fbaced8f58577dd1438aa6fd2ac990c9871ba9bffb4818` |
| `manifeste-simulation-puissance-garde-delta-v9-sortie-strates-partielle-f0.5-S3-g0.4-brut.json` | `f761213d266e85f11280852097aae3ac1bea6cdbea12cb51fded2becba019de4` |
| `manifeste-simulation-puissance-garde-delta-v9-sortie-strates-partielle-f0.5-S3-g0.4-calibre.json` | `7a63b8c52a5c3d39b677ec4690429bb233f7377b902d7adca157e981658cd4bf` |
| `manifeste-tableaux-v9-sortie.json` | `f8b6cb73e8fb88a0b248cd0f47d9e1b6e5e7b99deb48473e0fadbb14fc7ca6da` |
| `manifeste-verif-ecretage-v9-sortie.json` | `06f9b689dd1b7d500b84fc2d89b4458edd5ee0162bd774d0b0e64eca1d291f86` |
| `manifeste-verif-ecretage-v9-v2-sortie.json` | `efdafcb8f0fee89d156143fc7512478961a96fe9c86b4b796e9974c36102c119` |
| `manifeste-verif-identite-v8-v9-sortie.json` | `6d6ef51d53c159f3357f01784573cec730c34c6a8c14c8e0de3e0fdaab7cd84b` |
| `manifeste-verif-identite-v8-v9-v2-sortie.json` | `521da3046a106634d8fb8fac4d8b2554557a090a33345144e3c4c0903f92b0f3` |
| `manifeste-verif-identite-v8-v9-v3-sortie.json` | `5ab765f9dd946d8eccb833826d05fd80ff7b67e8e267d489d8bf2b3c19614af0` |
| `precision-rho-pilote-v9-sortie.json` | `a36b61ce66132f51b3909f9f524c9278a7d835e657225b3c46b27cd53cd4b06d` |
| `precision-rho-pilote-v9.py` | `6934099bcbcbe17a4f82b1dd10f1b86d5e8e535cfeedf12a3df782a155b32610` |
| `rapport-v9-gabarit-v2.md` | `0e7ed9fa791246e21756c673fcad0ddb7fc3a2a2cd4bcb05d99a97380d8925de` |
| `rapport-v9-gabarit.md` | `69a1e193a4d398dc5ed0cf52e5dc3f6ce9529c68bd0e70b2f61bf5f5c38c97ec` |
| `simulation-puissance-garde-delta-v9-etape1.py` | `3232a99448a3dc3c378108944e1c8ff9b3612f6bffb298ffe21f7f207246c6c4` |
| `simulation-puissance-garde-delta-v9-sortie-double-rhoB0.10-journal.txt` | `87b59b94e74fc2961e44b89cbfc95748b51f5758c23b64ee8fbb0975e88d8090` |
| `simulation-puissance-garde-delta-v9-sortie-double-rhoB0.10.json` | `2795336a89976eedbf4c6b16f050e7211c9cbc93100668256ee56b7421971402` |
| `simulation-puissance-garde-delta-v9-sortie-double-rhoB0.125-journal.txt` | `31570b61779309f89623fc4ffdb7f2390cf6b408bcd9880ce087716390689abf` |
| `simulation-puissance-garde-delta-v9-sortie-double-rhoB0.125.json` | `1531c4cdff903de3982a4ee5145d2e1a53090b3b3454fc45dc4603b8a287c032` |
| `simulation-puissance-garde-delta-v9-sortie-double-rhoB0.17-journal.txt` | `15a64022ca1c068ad2aa9d7d858e94221c6d8cede527f5f3e623bb812b3b3bdb` |
| `simulation-puissance-garde-delta-v9-sortie-double-rhoB0.17.json` | `7726d1331d2d17ab4079b535dc16d431154e0f711e3050455208edd2155e299c` |
| `simulation-puissance-garde-delta-v9-sortie-double-rhoB0.20-journal.txt` | `5bc9e454f37f88bb9daa5eaa699782309348dcc4e9a2770cb643ab62a750d03d` |
| `simulation-puissance-garde-delta-v9-sortie-double-rhoB0.20.json` | `e075cbaae8dc4fe1c2ac3d0d99bf9b4415506d1097ed5af702638915dc7985c1` |
| `simulation-puissance-garde-delta-v9-sortie-graine11-meme-rho0.17-journal.txt` | `5228317e0467a75c616227f8a1b5acca0d4b07e587e7348f5bdf73410371cd60` |
| `simulation-puissance-garde-delta-v9-sortie-graine11-meme-rho0.17.json` | `5cb565d2638cbfeafd3f5d72e07b4e9901b7563be86d3e5c8fc35bf53b150a53` |
| `simulation-puissance-garde-delta-v9-sortie-graine12-meme-rho0.17-journal.txt` | `d9f910b9b35bc13492ff8a0535dab94e101200f9ad6f952dc6cc219ee2441db9` |
| `simulation-puissance-garde-delta-v9-sortie-graine12-meme-rho0.17.json` | `628350969fc58d5b2261c770f67f8aa320c7195d393202d5abedb4a535a3c688` |
| `simulation-puissance-garde-delta-v9-sortie-graine13-meme-rho0.17-journal.txt` | `db63e101fa2203e32cf465a07d74ed9ca4cba1b546d06b7fd42c29639d982cd9` |
| `simulation-puissance-garde-delta-v9-sortie-graine13-meme-rho0.17.json` | `f798e40cbccdacae036187b440a6ff3c2637c277551d3e71e160c0d8193d44b5` |
| `simulation-puissance-garde-delta-v9-sortie-graine14-meme-rho0.17-journal.txt` | `fb6091143c94b6dfeb305aefe7d3d1748023f1b2543850852ddd68a3518586c3` |
| `simulation-puissance-garde-delta-v9-sortie-graine14-meme-rho0.17.json` | `2a019249ee1af71f51f536282f5315508b20c2345141b7414093c5f776922cc6` |
| `simulation-puissance-garde-delta-v9-sortie-graine15-meme-rho0.17-journal.txt` | `611802f895806f75962b9486a848addd5c93ae0f016ad8b1e3f7cf1828838aa8` |
| `simulation-puissance-garde-delta-v9-sortie-graine15-meme-rho0.17.json` | `830ca71a46c4441370aebaab5eb81829038719a33b3c2f539e1b2b84ce6aeb59` |
| `simulation-puissance-garde-delta-v9-sortie-graine16-meme-rho0.17-journal.txt` | `1c41283ca26c1425063d696e9da7aaa524d9fd26e1707e5f6417b8c8353c33d1` |
| `simulation-puissance-garde-delta-v9-sortie-graine16-meme-rho0.17.json` | `69edb873534e011add84bb8e02908e262b5ee9dcc63421b5e8ab7e590ca2e5e1` |
| `simulation-puissance-garde-delta-v9-sortie-graine17-meme-rho0.17-journal.txt` | `34e4dac08fc0a1fd9535a4cab5b2e6a4419e8ff577106c6ba5628a8bcac00116` |
| `simulation-puissance-garde-delta-v9-sortie-graine17-meme-rho0.17.json` | `29c9898287668c28a0ea72cde2d91f4986e194eabbcf4a78afb439906d5d4e6c` |
| `simulation-puissance-garde-delta-v9-sortie-graine18-meme-rho0.17-journal.txt` | `ba28a6feac517e301828bf8a914f7e8908c12fb66fc3c2c86f2fd3bced01c99f` |
| `simulation-puissance-garde-delta-v9-sortie-graine18-meme-rho0.17.json` | `30724d1cd9e783b962833486a688c5ec8b8088253ed4b7718752e97996b2ab6f` |
| `simulation-puissance-garde-delta-v9-sortie-meme-rho0.125-journal.txt` | `24c5d5b6c764402eeb4353fec83af273ee284e0fb2fec9b9f68961b62bfbd4e7` |
| `simulation-puissance-garde-delta-v9-sortie-meme-rho0.125.json` | `c747c3cf6d7304fdef2290b444bf228f5d949175bec3b7d74fa9708c27e954e3` |
| `simulation-puissance-garde-delta-v9-sortie-meme-rho0.20-journal.txt` | `9c900e25d4ddd4d12e010bc7770e64a475e8411e18febce92692f23f96b678f4` |
| `simulation-puissance-garde-delta-v9-sortie-meme-rho0.20.json` | `5dc07055edd1e249d65c6895531c3456809c0b12d78feec5de7356442a879eb5` |
| `simulation-puissance-garde-delta-v9-sortie-meme-rho0.30-journal.txt` | `66ea13f7fa75fffa4d67dcb9f9bb832677dff8656cbcca3c5e2e5bf012f0d9c9` |
| `simulation-puissance-garde-delta-v9-sortie-meme-rho0.30.json` | `6fa01d5c189de7746a5833ec2da1881f85ebaf3745d69c142e70603f83a49890` |
| `simulation-puissance-garde-delta-v9-sortie-meme-rho0.35-journal.txt` | `e22c3c2d57544cdb1c25f4cee79717eef79477de43efed95fa286d35abde2f84` |
| `simulation-puissance-garde-delta-v9-sortie-meme-rho0.35.json` | `cfb0fce4a47d8d07d286d53b2f8fa9c20e5263af92ecfb953d0c84aa556d07ac` |
| `simulation-puissance-garde-delta-v9-sortie-rhoh2x-meme-rho0.05-journal.txt` | `064de91f10651c324acabbf7d26850550fd610b659e1b6b35a6b2c8edb0376de` |
| `simulation-puissance-garde-delta-v9-sortie-rhoh2x-meme-rho0.05.json` | `b194323a6bb6af0ddb9d01d57e47b1d70154705d75faa58bd534b80f19eceb59` |
| `simulation-puissance-garde-delta-v9-sortie-rhoh2x-meme-rho0.10-journal.txt` | `c6ef0f24b630ffdbcda6c1be52d3ce5c19272d8c759b3240d6c6062cbf966879` |
| `simulation-puissance-garde-delta-v9-sortie-rhoh2x-meme-rho0.10.json` | `5d411e90074688a348997d6db9ef3029ed4943d97e47abef269726d486d1a8d6` |
| `simulation-puissance-garde-delta-v9-sortie-rhoh2x-meme-rho0.17-journal.txt` | `9eeca3a7290de7d2eedb6e0f0f1472587ef553358a86348c7476749964fe88d1` |
| `simulation-puissance-garde-delta-v9-sortie-rhoh2x-meme-rho0.17.json` | `3c912b630840b08055d306226b5e2b71993f54465d2939d5c24908dd64a99d07` |
| `simulation-puissance-garde-delta-v9-sortie-strates-partielle-f0.5-S2-g0.4-brut-journal.txt` | `6ed6974d365a86e3ffd4976f402c949909bd6dd48f437a6acd28ad127777c736` |
| `simulation-puissance-garde-delta-v9-sortie-strates-partielle-f0.5-S2-g0.4-brut.json` | `f33d5a804ddeb2a44db19a84504ea541635c54b687b87c4ae11849e9fcc2b099` |
| `simulation-puissance-garde-delta-v9-sortie-strates-partielle-f0.5-S2-g0.4-calibre-journal.txt` | `14fca26101530b4e12b269fdaff2f091055a0186cdeac00abce8f22765c73d7f` |
| `simulation-puissance-garde-delta-v9-sortie-strates-partielle-f0.5-S2-g0.4-calibre.json` | `e761151e94db7879eab65ef53b524e5ecc8da0b159963413f3925f1993d045d1` |
| `simulation-puissance-garde-delta-v9-sortie-strates-partielle-f0.5-S3-g0.4-brut-journal.txt` | `79a4712e5fd05808c533bfb3fb50f8b96f5756ce937367bd877b545a14e4fad8` |
| `simulation-puissance-garde-delta-v9-sortie-strates-partielle-f0.5-S3-g0.4-brut.json` | `4a487370ea57635a36b8ee458336f54a66bea4b843b01898e557591fd4dae16e` |
| `simulation-puissance-garde-delta-v9-sortie-strates-partielle-f0.5-S3-g0.4-calibre-journal.txt` | `cd1dc9288c065bbcd6179e55b664ca80cf57d07ea0a3333fd1947a664c8d4a2f` |
| `simulation-puissance-garde-delta-v9-sortie-strates-partielle-f0.5-S3-g0.4-calibre.json` | `370534d17d5f2fb0b4c40a16a9896b6cbcf1244f5f0a6a2ebb7d521619038895` |
| `simulation-puissance-garde-delta-v9.py` | `f483a271d364b2900505cc314464ea6cf7101ad4e68e0fb09a579df10661c148` |
| `tableaux-v9-journal.txt` | `21e1b8046053fba6113e1fba5c16789ecc0f087fee6f1388d26ce770b3936024` |
| `tableaux-v9-sortie.json` | `12db7037c124af0573c85de65a15a0a93e5cc73665134155d9ef96feee54ae8e` |
| `tableaux-v9.md` | `a2fe2b17b4d268d24063d653aef530c58c805c7d6c478c9d9cf3369e757169be` |
| `tableaux-v9.py` | `29e2ec7c5e879db1e7e706d2c3464942c8fb813c3df415743b89ce5c182cdb3b` |
| `verif-ecretage-v9-critere.md` | `a0da3b4c03d0c38b8ad4afd7de8380aebfe87339dd9e95cd9a521c6dc3fc258b` |
| `verif-ecretage-v9-journal.txt` | `0587d266ecaa4159b9ada1252916ab95bd1964a3654278f7085248c599833148` |
| `verif-ecretage-v9-sortie.json` | `afa8e941d0362c10cae67800a734b9a718418de736dcb6242a898ee1940eaff1` |
| `verif-ecretage-v9-v2-journal.txt` | `0587d266ecaa4159b9ada1252916ab95bd1964a3654278f7085248c599833148` |
| `verif-ecretage-v9-v2-sortie.json` | `6e1a205df4620cb5bb045fca12c3984c6f355f79a0ea3d07d0da800fceede99a` |
| `verif-ecretage-v9.py` | `7860a8413e100638c9af740ced7b2068d63e2394be0b022c17f043c948c2f522` |
| `verif-identite-v8-v9-sortie.json` | `6ed1e3405bf2d94c830a87594f54ac6ef50c5487e93f4ffc9ec3d02c209939b8` |
| `verif-identite-v8-v9-v2-sortie.json` | `9f0d71a3aa0ccf7ef2492df09a904d93960efc0ff363e86c61efe284e886d218` |
| `verif-identite-v8-v9-v2.py` | `aaff6e8cbf3e195d62182ec4ebe9fc57bdb6a3d0a4271bede9be7eb6a4a0399c` |
| `verif-identite-v8-v9-v3-sortie.json` | `036be93c91988e6aab395d06e7355fd23a105b6d42b31588df7ebbb504bcf200` |
| `verif-identite-v8-v9-v3.py` | `d82749a7084dd0184c5d59e67aba697415f55ffc7bd48852c6fcfc32d4db672f` |
| `verif-identite-v8-v9.py` | `7355a4b38ad7f2fd3b8275c591b488fe259e234fc3151df6a1984d15833e286c` |
| `echecs-verif-ecretage-v8/ebh-pole-essai1-journal.txt` | `2124523198a7263cac913d6947de598f7d21151de1a94d72f367c976ae24e2e6` |
| `echecs-verif-ecretage-v8/ebh-pole-essai1-sortie.json` | `2b2236131fbc5850b1b264241dca4fa4d34ec643986b10173d44cc4154e01537` |
| `echecs-verif-ecretage-v8/ebh-pole-essai2-journal.txt` | `750d8f55bde2d658dfaf597423359acdfcffa8f56b0bdd07b4c02a60d109fa9d` |
| `echecs-verif-ecretage-v8/ebh-pole-essai2-sortie.json` | `de6500d906968901c5ab18e34f55797233c75a06ae7f04fa5be38912e9ba0a24` |
| `echecs-verif-ecretage-v8/ebh-pole-essai3-journal.txt` | `576d46a2304172c15163e05ddce1f54e92f593cc460ee32a6a27b5a71d5c49d1` |
| `echecs-verif-ecretage-v8/ebh-pole-essai3-sortie.json` | `b94be5eed01254c7d2b5e918cde341863bf627cc5304d1fe8a0074b01a60dc37` |
| `entrees-gd8/ajustement-n80-gd8-v1-sortie.json` | `e65a641ecb70ff140fa3647137d33fae9611c16a1ddf8671cf6bfde8fb4a78d4` |
| `entrees-gd8/ajustement-n80-gd8-v1.py` | `5fa513ae5877ae159f01bd49f83cbc669fa597eae60d44425e15257e6ea5232d` |
| `entrees-gd8/comparer-rejeu-gd8-v1-sortie.json` | `19a3099da4187bbb902f1ca8e0fae40d870162b8d9f670b5a8407214277602d3` |
| `entrees-gd8/comparer-rejeu-gd8-v1.py` | `db4f1faa8e92d5496bcbead75d7757d6565d6f618d31934f03ae8a497486bb09` |
| `entrees-gd8/contre-lecture-gd8-v1.md` | `653c3b408fe9e352d7f4cfaa40e60453879dd9ffc28e82907256e1209414bde4` |
| `entrees-gd8/graines-cellule-pire-gd8-v1-sortie.json` | `39efd41662be4b53709c4fe8a90fa31df79dc88d7698d5038ec2933f776e47f3` |
| `entrees-gd8/graines-cellule-pire-gd8-v1.py` | `5108f65c3901caf98f55549f4cf9e25a3d4551bdee6126c447750452ff0fab86` |
| `entrees-gd8/regle-table-lecture-gd8-v1-sortie.json` | `9912624f8d86b90ea5561377105e1a6b416803aa97674f468958cb91f9254ae5` |
| `entrees-gd8/regle-table-lecture-gd8-v1.py` | `dc67a2c361d9d7e0825e0c1fbd7952f2cb6c7638db6ebddeac9f73932ba2f080` |
| `essais-gd8-v9-v2/essai-gd8-03-sain-partielle-journal.txt` | `fd390c352973f86a5034656726c975a2332040746b33a4ed93e4b2510d0ff713` |
| `essais-gd8-v9-v2/essai-gd8-03-sain-partielle.json` | `06b2b686c5c288f5e23a102750d2e522f8e2873d6825ec335796411119eb590c` |
| `essais-gd8-v9-v2/essai-gd8-07-sain-facteur2-journal.txt` | `93b506d065e3159057b6f9afcdd1909fc484c8356d48f1060550517c4084acec` |
| `essais-gd8-v9-v2/essai-gd8-07-sain-facteur2.json` | `93bff8323bd8059ae66bff793ea9bdd5621bdd31ad25dc7ab40008e9e2a908d5` |
| `essais-gd8-v9-v2/essai-gd8-08-sain-neuvieme-journal.txt` | `873120f3f9467e4db9ffb7850f391498eed8dad74185d2b6b6f4e9ba111268db` |
| `essais-gd8-v9-v2/essai-gd8-08-sain-neuvieme.json` | `84efe344b502bfb8d4e77a6ac8e305d3736dc0b697af52c0ff7496041f167cb0` |
| `essais-gd8-v9-v2/essai-gd8-08-sain-nulle-journal.txt` | `a6aaecc4c4e6ca30b0b91ab4127ed8485f5aec18026a5eb74134826794fc1f77` |
| `essais-gd8-v9-v2/essai-gd8-08-sain-nulle.json` | `4ea970cf8723ead6d359398a22dd7805d20988b9d364f8ccdff5b9d3aebbc28a` |
| `essais-gd8-v9-v2/manifeste-essai-gd8-03-sain-partielle.json` | `e87f84b3d4962d757bf617d2dd329994c7442fc64a2b860cddc1a2d7a4e4adaa` |
| `essais-gd8-v9-v2/manifeste-essai-gd8-07-sain-facteur2.json` | `85411b0f368578a55d00bc1ffb236f36260d20b7d95bd173538c80b7281dafb4` |
| `essais-gd8-v9-v2/manifeste-essai-gd8-08-sain-neuvieme.json` | `b827ae37eca6091584676907099c42ccf8e0cbda800627ea9a96f7274c3f15b9` |
| `essais-gd8-v9-v2/manifeste-essai-gd8-08-sain-nulle.json` | `12d0ff808dfcb7fdab3dcda58475e0dd8fbeb6ed9e57040bc5e0ba4a3195b909` |
| `essais-v9/essai-gd8-07-sain-facteur2-journal.txt` | `f29c56af4e525a7fb8778ddb58b6162cc5a96f7ba2a4f57eebb29038ff8752fa` |
| `essais-v9/essai-gd8-07-sain-facteur2.json` | `69c6e6a8d813b95d64958b0990b98c8f7882754dbb0f6ba6956d1547beb83234` |
| `essais-v9/essai-gd8-08-sain-neuvieme-journal.txt` | `739da7299ec64f58b1d780d5373c332b2be055d1ccc9012ba789a3a270686d1c` |
| `essais-v9/essai-gd8-08-sain-neuvieme.json` | `7dce13b27237acedbdaa92e90e0f1ecd0cec26aec716f00a815fba72e6faf0cf` |
| `essais-v9/essai-gd8-08-sain-nulle-journal.txt` | `827035b7dad22829039ffb08e2e59ad0af9bb569d1945bb67202913eb8693f2d` |
| `essais-v9/essai-gd8-08-sain-nulle.json` | `3530c8ba417c34787918a63f142739c232288e35d80735a1a8d7f31cc614b9c6` |
| `essais-v9/identite-combine-n80-v8-journal.txt` | `87d503989e9e7b64b5a75dd4150a1f6aec22c3350515e0e0f7f2a884c6fb8113` |
| `essais-v9/identite-combine-n80-v8.json` | `ba3efea3c3602f11929f7ee192469e273d58491d408143b6242aebff1a64f0d4` |
| `essais-v9/identite-combine-n80-v9-journal.txt` | `e2ea06ed1b2590019713ce04603c7dd4aa0ede64f0eddfcf4df45509d1d93354` |
| `essais-v9/identite-combine-n80-v9.json` | `3b0544de4b26691caf3b0cede2bde66e04058c9c6a16cfe7f0b1eed70955a417` |
| `essais-v9/identite-copule-v8-journal.txt` | `b8efd375b2790aeced709d2b4cbd01f60a7054da856ec231179f6520aeb61892` |
| `essais-v9/identite-copule-v8.json` | `9d3f6d11eaa8e79b39aeec574ee0bbe1128e97bc7a891440b17a63a01accf910` |
| `essais-v9/identite-copule-v9-journal.txt` | `e60fef905a1c3de24408d80b5966a5f4aae6ea3d5c67dbd20d2437b13e578add` |
| `essais-v9/identite-copule-v9.json` | `15c4a15e2242df61094d61709c6830b5a63dbca714ee812935cd586cac340c72` |
| `essais-v9/identite-neuvieme-v8-journal.txt` | `383f51e2713197df13ce539c35543075dfa07d31059d808d157003de7afe41dc` |
| `essais-v9/identite-neuvieme-v8.json` | `cb36b726afaf34b3c7d2879a030596ead743b7ad9b62f72199e154bcfde11dca` |
| `essais-v9/identite-neuvieme-v9-journal.txt` | `24ec71923da05d2ebf6ad98c1cb10c64e17666a468cbacc85fe1cc3603e2ac9c` |
| `essais-v9/identite-neuvieme-v9.json` | `f97f3a5ae34d8d50b8bea9f499625c157550dc629957b540c86dc136a389e78a` |
| `essais-v9/identite-strates-v8-journal.txt` | `1c5a84ba4344bea1792c86fa8db3edeb812b17bcf8a9615516c6ed4eaa7524cb` |
| `essais-v9/identite-strates-v8.json` | `fedbeaabacc4e333e3fe8eebd25f0ee67622a4fab12370a06d2e54ef09cce6a6` |
| `essais-v9/identite-strates-v9-journal.txt` | `85741afdab694df1a1a73dc677dfce149ba1f0049e3033b788dca5e3d66ac18f` |
| `essais-v9/identite-strates-v9.json` | `9146226c9c2b821b4f4e9c59c901bdae2b68ee287b719112f289fe35aa0bbe03` |
| `essais-v9/identite-temoin-facteur2-v9-journal.txt` | `649005ea49d5e3b97fca09e2da930a157ac2af0a6f84dcf764dccc3ffb05d64c` |
| `essais-v9/identite-temoin-facteur2-v9.json` | `781737aa41700faaae9e2e04da48f7f25e3da252eeecedabcd0ecde38bc3a79f` |
| `essais-v9/manifeste-essai-gd8-07-sain-facteur2.json` | `9ed9ab26d1dc63a3158dd9ddd5c50467d1af9e66fded1cfc9fca22caf05c279c` |
| `essais-v9/manifeste-essai-gd8-08-sain-neuvieme.json` | `f8261ac816b317547e0678f3f7b477b6e9e763eb048373774d88ee3bee3d1c5a` |
| `essais-v9/manifeste-essai-gd8-08-sain-nulle.json` | `4df3a2c9c9d37d5c6efd29dc771e8dc4ec6d6ab91b8ab5f5e8f12bdfd9acd7c1` |
| `essais-v9/manifeste-identite-combine-n80-v8.json` | `eb63b62fa2ac414a78b767f9ea2f6163a6f5f1036b126de1034eef86d38bd570` |
| `essais-v9/manifeste-identite-combine-n80-v9.json` | `697c9e7c0091cd331a3d9e3ce611433799c509fd5598ec63525aa61066fde7e5` |
| `essais-v9/manifeste-identite-copule-v8.json` | `b99867d92f9bae92819169f1caacb34bdb50f09f351010e6b7273d01c91cadcd` |
| `essais-v9/manifeste-identite-copule-v9.json` | `b64e3af2b07357c3c5459bf37c7c1f1c42fdb6bc22664b9bb1e6cc8177d02500` |
| `essais-v9/manifeste-identite-neuvieme-v8.json` | `bf17180af4fd3c9940a0393153234617964c30d3525ba0c62774e499ca8aabc8` |
| `essais-v9/manifeste-identite-neuvieme-v9.json` | `980627bf5c25b096661f5aa3dc19ea4585f1b1f151613cfcc6165f6b283c91bd` |
| `essais-v9/manifeste-identite-strates-v8.json` | `935da014bc962fa15355676c4bb768127ef5055e508384d7c93dbc56edc4febc` |
| `essais-v9/manifeste-identite-strates-v9.json` | `ac80300d1e232d8305c5b3254facb6c1bc4ed4267c2cc4254432bde77f900c59` |
| `essais-v9/manifeste-identite-temoin-facteur2-v9.json` | `45de4f0c508543d0ccf7dad54dbee5287c00833c41fa5c13016e823d135c5522` |
| `essais-v9-v2/identite-combine-n80-v8-journal.txt` | `db9a870289fb0d9afb18793ec5a158fb04d6185f94c1eaa602bbcc4f8d3c4259` |
| `essais-v9-v2/identite-combine-n80-v8.json` | `546983376c5388996a54dabae816b667fb6ce7b32047e77177236f88ea26f10f` |
| `essais-v9-v2/identite-copule-v8-journal.txt` | `fe65d80deded2ae0bf244ac1aaf76ac77820fdcd028a0b4d655cb61a47f03234` |
| `essais-v9-v2/identite-copule-v8.json` | `daac0d826218dbac7ee174120425978337bb0c83ed74a341442d50b98af865f8` |
| `essais-v9-v2/identite-neuvieme-v8-journal.txt` | `cf2f5b27d8388c8af06dc4cd6cd48794eb155ee4c01c492415edd91f662a706e` |
| `essais-v9-v2/identite-neuvieme-v8.json` | `ffb1e6a136a115b2f63cfe75706a54cdcfcb81bd027840aaad977609cbe48cd0` |
| `essais-v9-v2/identite-strates-commune-v8-journal.txt` | `ae271e20565704077b82fdc427e116b968ee65c0d46863d7ce521f7d02123581` |
| `essais-v9-v2/identite-strates-commune-v8.json` | `5e75b246563ae0de3ae1e78aa61250d2228f0239ac9db02f82b085e3bcb1df88` |
| `essais-v9-v2/identite-strates-commune-v9-journal.txt` | `df812634fe14caef400f27766df131fe377f0d7ce951b6ef00af5014eaaef79c` |
| `essais-v9-v2/identite-strates-commune-v9.json` | `55c8637aff78e3a03098d40f130f2254a67a33a5c911912132bfee179752356a` |
| `essais-v9-v2/identite-strates-v8-journal.txt` | `9ec1432825ad9305797f69148a6734aa07dfe64406cbbecb0db8f6c889103aaa` |
| `essais-v9-v2/identite-strates-v8.json` | `fba9d9924e6134ba642d81f3f7369c521e29e29688069d1b880b1e6dca99f48e` |
| `essais-v9-v2/identite-strates-v9-journal.txt` | `08daffcc855f21994c9dd11ba5d67d68378bf20f3631182aa304533f8f403d5c` |
| `essais-v9-v2/identite-strates-v9.json` | `76d858fb43fd21f21fe86967583d2e9ed9b0b97058999d450f1b7d97e263c1b3` |
| `essais-v9-v2/manifeste-identite-combine-n80-v8.json` | `ca0ce41388b472be060b7a0fc31b3767fe3acf83abcd77b790b7a6b09f6b1797` |
| `essais-v9-v2/manifeste-identite-copule-v8.json` | `6c500f3afd406c67bd801800691feaa1e5a5625af2069b69983a5b2844261076` |
| `essais-v9-v2/manifeste-identite-neuvieme-v8.json` | `dc6a01afa1fee2e604d1a81b565a4726709fc06677c237a155183b39d0fcc6f1` |
| `essais-v9-v2/manifeste-identite-strates-commune-v8.json` | `9a36b50a0d70f94a6585ae83dd48fd66c028ba92d3c50a8d1a59472eb5b6ea9c` |
| `essais-v9-v2/manifeste-identite-strates-commune-v9.json` | `a94f1f5cd18768498754952b10b26f8f9af1afedea9be8a4bfc86c3ffb637182` |
| `essais-v9-v2/manifeste-identite-strates-v8.json` | `a40460059c7928ac357480248eca3d771726224e41a4326dfdbf6262a6345f21` |
| `essais-v9-v2/manifeste-identite-strates-v9.json` | `c3b491bbdaa698fa93aa7ae0924ce74791ca6414660bb93122240fb30f879eb4` |
| `essais-v9-v3/identite-combine-n80-v8-journal.txt` | `9831e1f01e52d39608c051f69e23e311edd923878a7389c4b2ec0365a9c22fba` |
| `essais-v9-v3/identite-combine-n80-v8.json` | `cb838886c65231d2a7bcac8f7aaf48069ce072d2b6fafbc02907c8c28c366966` |
| `essais-v9-v3/identite-combine-n80-v9-journal.txt` | `fc10c715b826c38bd8fdd30087063be4e245ee4ad3f48f869c62de5513c2947c` |
| `essais-v9-v3/identite-combine-n80-v9.json` | `4acf49e7bdd334db54385b0ca16b6f0410d0389ea4fd5bae3e93d4c850a14622` |
| `essais-v9-v3/identite-copule-v8-journal.txt` | `53ee2797e44cfd4ed2b5737f85cccf97f528e5e134c701df26ff43bfd272ecb7` |
| `essais-v9-v3/identite-copule-v8.json` | `4c6f07d30838b651e86344b7fbd53846827348c3b319e2466e2e8b40b84b001d` |
| `essais-v9-v3/identite-copule-v9-journal.txt` | `62c446d67712b5da683681ccd93b3c4572a2700650e690528bc5ccdbfa3cae05` |
| `essais-v9-v3/identite-copule-v9.json` | `fc299f7e900629591ca5243ff930f7f915a683d71e25282af5088461de1514f4` |
| `essais-v9-v3/identite-neuvieme-v8-journal.txt` | `e31ae96211a5dff5f51215d0a9e29de9bd27490b048feb69b201a8049e7144ca` |
| `essais-v9-v3/identite-neuvieme-v8.json` | `139d76c716f6d013d5208caa7b6d38aa14592732f848ac56598c00476fc525ff` |
| `essais-v9-v3/identite-neuvieme-v9-journal.txt` | `5680bbf3905af7b72b27efec130de41c8d85636f2287ff3c2fb80a8bb7e544df` |
| `essais-v9-v3/identite-neuvieme-v9.json` | `7e5b67d851d98520df890c044c59631403366881162a2e249f642c5e56bbb862` |
| `essais-v9-v3/identite-strates-commune-v8-journal.txt` | `ebfdcf560e27460d5025bbb4be4d61523ab66f8a55a3b9d91e8e4b52fd97cf98` |
| `essais-v9-v3/identite-strates-commune-v8.json` | `47a9fe5247844339e2f1815933166b1841940d19443bf133429c27afab9a8a88` |
| `essais-v9-v3/identite-strates-commune-v9-journal.txt` | `45517a8022614d36501a3f0999247a7bc0db4917b4190a474ca3649095f62204` |
| `essais-v9-v3/identite-strates-commune-v9.json` | `e395e98e7ccf89e50b72e1fcc9cd6007edee92144584a990231a57a8460a8fae` |
| `essais-v9-v3/identite-strates-v8-journal.txt` | `b0b64ff71ad953cc56ae46a5d685085f70d3e1e456b0cc671e139a25d3ef641a` |
| `essais-v9-v3/identite-strates-v8.json` | `42bdcd09ae184c356660ecc8630b4c7e4a4efaae710f19ad73a0901314eb16e6` |
| `essais-v9-v3/identite-strates-v9-journal.txt` | `d52b6fc5e08d824a380c76e249d9be47912b0b4cc3ed52db32c341ac6ae0dfe9` |
| `essais-v9-v3/identite-strates-v9.json` | `6a78d3ceb97a5a8159c4107fd4dd10b92fc49a97d5c71bce029e7986ce3273da` |
| `essais-v9-v3/identite-temoin-facteur2-v9-journal.txt` | `1bb508fb8109b83ebc172aed4e8f490dcdc9a194de5d401698880d729d53e023` |
| `essais-v9-v3/identite-temoin-facteur2-v9.json` | `8428cef30020cbc26e57ff19cd3a30e0d8da1ee66e0fb2d39683b490d20a4dd0` |
| `essais-v9-v3/manifeste-identite-combine-n80-v8.json` | `630eb9b2a4bd96a1bcb5559a618c4f4c582a5d70c598df45fd2b60e443a87974` |
| `essais-v9-v3/manifeste-identite-combine-n80-v9.json` | `c3c23f949537eb73fd8a0149054eb8687d327ca619915d6c5eb1042c4fae50a1` |
| `essais-v9-v3/manifeste-identite-copule-v8.json` | `3bc20e2c74035508eaeba5ccb5e52e3c7cf89c8c05358177e51acb9161df87c9` |
| `essais-v9-v3/manifeste-identite-copule-v9.json` | `6a3eba01925cb06c6a553937fa5825ecaa2bdbbde6cc13128336d41ee5862dd9` |
| `essais-v9-v3/manifeste-identite-neuvieme-v8.json` | `ce48e3bd9b10c1a775d8008827cd3a5047d395f00342840f0d6d28114fede532` |
| `essais-v9-v3/manifeste-identite-neuvieme-v9.json` | `f4352f9b08295ef58beccc849cfb23dce6a57efa867566b9e46698b4a0eba7a8` |
| `essais-v9-v3/manifeste-identite-strates-commune-v8.json` | `bb9a740fa233e1c476fcf14d3dbdc27f8d3b0cb6889d605fa061ed28d5ee44a0` |
| `essais-v9-v3/manifeste-identite-strates-commune-v9.json` | `640dafa9ad7576d8a4b3cf37012a541d9c1a2bf78b9f34fcb91ded157dfd4b1d` |
| `essais-v9-v3/manifeste-identite-strates-v8.json` | `c5991a275e152e6f8baf23bcfd7a4e7752d5b879fcb257e7df3f78b4d02efb8d` |
| `essais-v9-v3/manifeste-identite-strates-v9.json` | `f75aa363876bcc19acf6e7f19633788bc92d0b9056a5725e9dfeb44c3411c3ad` |
| `essais-v9-v3/manifeste-identite-temoin-facteur2-v9.json` | `6b8f54d07bc294d6e624be0b950cb609f9ebd004c3a89ad316d1dc9bcec642c9` |
