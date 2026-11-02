# Verdict de lecture du rejeu à graine de R1 (addendum v2 scellé) — v1

- Lecteur neuf : sous-agent de lecture (Opus 5.5). Je n'ai écrit ni le texte, ni le code, ni la concordance, ni la fiche de réception, ni les contrôles de réception.
- Lecture faite une seule fois, du 2 novembre 2026 à 18:22:23 au 2 novembre 2026 à 18:37:15, en temps universel coordonné (UTC, heures relevées par `date -u`). Rédaction commencée à 18:37:15 UTC.
- Ce fichier n'est pas scellé par moi (consigne : aucun fichier `.sha256`). Son empreinte est rendue à l'appelant.
- Abréviations : R désigne `/tmp/claude-0/-home-claude/03748db6-42ca-5241-871c-5399d39c1451/scratchpad/reception-rejeu-graine-v1/`. S désigne `R/copie/brouillons/canal-reprise-releve-v1/envois/session-depot/rejeu-graine-sortie-v1/`. « Le texte » désigne `R1-addendum-relance-v2.md` (`9d17d640…`). Les numéros de ligne du code renvoient à `resolution_graine_v1.py` au commit `c2a8b6e1`.

## 0. Verdict (trois lignes)

1. **Résolution : les 7 épisodes sur 7 sont résolus**, chacun par l'égalité de son empreinte avec celle de P3 (recalculée). Le contrôle croisé est « conforme » (recalculé contre la table v2) et le lot est « sans objet ». Par les critères gelés : la **table v3 est complète** (`ead8a668…`, aucune entrée `non_resolu`), l'**addendum v3 se fait sans règle B**, et le texte ne porte **aucun nœud** à Lazar.
2. **Validation : 54 empreintes de P3 retrouvées sur 147.** La classe est **« méthode non transposée »** (recalculée, égale à la sortie). Elle impose une **réserve sur HG-2** et une **mesure déclarée incomplète**. Les 93 épisodes manqués le sont tous par une durée : 90 non tentés, parce que le budget de l'étape (2 400 s) était épuisé vers 17:57:53 ; 3 coupés pendant leur repli.
3. **Audit de symétrie : aucun déclencheur écrit ne part.** La validation incomplète tient au budget de temps de l'étape, consommé à 65 % par 3 épisodes en repli. La voie directe a échoué dans 17 des 57 épisodes tentés, loin de ce que prédisait P-G1. Aucune défaillance de la méthode n'est conclue. Réserves : HG-2 et mesure incomplète (exigées par les critères), deux de la concordance, quatre du lecteur.

## 1. Ce que j'ai lu (chemin, empreinte, vérification)

| Pièce | Chemin | sha256 | Vérification faite ici |
|---|---|---|---|
| Texte scellé | `R/textes-scelles/R1-addendum-relance-v2.md` | `9d17d640509c9b5dd0285e90f3096145b82f2e0ea2e73e62725c0e0c8cb71059` | égale à l'attendu et au compagnon ; lu en entier |
| Configuration | `R/textes-scelles/R1-graine-config-v1.json` | `0f300925546d886b8408d137903e711af579abb0d5947b1b88a27da894c4070f` | égale au compagnon ; objet identique à la configuration recopiée dans les deux manifestes (empreinte canonique `f91716bf…` dans les deux) |
| Table v2 | `R/textes-scelles/R1-table-tokenisation-v2.json` | `5f6cf489eb971c195f7263cb738bc5f9de4bdf5cfd0f55658fd3977d3f4b55e2` | égale au compagnon |
| Code (commit `c2a8b6e1`) | `R/code-c2a8b6e1/resolution_graine_v1.py` | `cdc22b5ad2659f82f512c39545c52fc826a6be2dc60fb3aeafda0c5d014a9663` | égale au compagnon et à l'en-tête du texte ; lu sur les lignes 100-189, 232-919, 1013-1067 et 1360-1803, le reste par recherche |
| | `R/code-c2a8b6e1/resolution_graine_lot_v1.py` | `5a9982b2a2248d5312c5a42bf34ac90c505ca579052985169aabb7e16c8c7156` | égale à l'en-tête du texte ; parcouru seulement par recherche (le lot n'a pas tourné) |
| | `R/code-c2a8b6e1/r1_resolution_graine_instance_v1.sh` | `da07025f5cae92cc0041a234a1a3951f33cd42e86da808befbaaedd7d5351cc8` | égale au compagnon et à l'en-tête ; parcouru (en-tête et recherche des étapes « cibles du lot » et « table ») |
| | `R/code-c2a8b6e1/resolution_tokenisation_v1.py` | `e8568c3c8d48a5713fddd7d55d805e54b9c702edee2b7d2f218db49c230434c9` | non cité à l'en-tête du texte (inchangé selon lui) ; non ouvert |
| Fiche de réception | `…/reception-rejeu-graine-v1/fiche-reception-rejeu-graine-v1.md` | `1193a54aed417c28666d4022721e8a0da5e14cdfc41cfc09d2fae4705533221b` | égale à l'attendu et au compagnon |
| Contrôles de réception v2 | `…/reception-rejeu-graine-v1/controles-reception-rejeu-graine-v2.md` | `6db9da14d10d0972d975e0348c9f98b5a411d32be7097b4f0d8dfc6aeeb9eb79` | égale à l'attendu et au compagnon |
| Concordance finale (deux réserves) | `…/analyse-principale-r1-r2-v1/concordance-finale-addendum-r1-v2-scelle-v1.md` | `07ea87e0c5264fbbefeabf061119f769e6e35c13705421d53530e08a5e3809c6` | égale au compagnon et à la citation de la fiche ; lue seulement sur ses lignes 80 à 115 et sur les lignes trouvées par une recherche de « R-1258 », « VI-09 », « balayages », « réserve » |
| Sortie : résultat de la validation | `S/diag/20261102-171752-r1-graine-validation/resolution-graine-validation.json` | `8e6a49126f37af6020b8bf056e6d35c6d53c7391f6d5d311fa0e6caa1298f773` | égale au compagnon |
| … tableau des pas | `…/pas-resolution-graine-validation.npz` | `fe2ef360a2444dc518c4e67b1a4623dce091abce636de0a572cacdd26d1142f6` | égale au compagnon et à `pas_sha256` du résultat |
| … 147 épisodes | `…/episodes-validation/000.json` à `146.json` | une empreinte par fichier | chacune égale à son compagnon et à `episodes_consignes` du résultat (même nom d'épisode, même rang) |
| Sortie : résultat de la résolution | `S/diag/20261102-175806-r1-graine-resolution/resolution-graine-resolution.json` | `674825453a8ce34c8bb6f8cb59a054b37af76d24f5e8b44b06f2c5e59d396079` | égale au compagnon |
| … tableau des pas | `…/pas-resolution-graine-resolution.npz` | `99f7564e95042d56df6c3ac1034e46e84da3349a5b159db687a824ee8252d66a` | égale au compagnon et à `pas_sha256` |
| … 7 épisodes | `…/episodes-resolution/000.json` à `006.json` | une empreinte par fichier | chacune égale à son compagnon et à `episodes_consignes` |
| Table v3 | `S/prereg/R1-table-tokenisation-v3.json` | `ead8a66851b2af5dfa02635297056872032878fbd2987ba780fb6c9096766423` | égale à l'attendu, au compagnon, au journal et à `traces/…/sceau-table.txt` |
| Manifestes | `S/runs/20261102-171752-r1-graine-validation/manifeste.json`, `S/runs/20261102-175806-r1-graine-resolution/manifeste.json` | sceaux conformes | commits `c2a8b6e1…` et `3482d8f1…` ; texte cité `9d17d640…` ; `depot_propre` vrai |
| Traces | `S/traces/r1-graine-20261102-181212-iXsM/` (journal, sorties d'étapes, essais, erreurs) | `empreintes.sha256` (26 lignes) | 26 lignes revérifiées, 0 écart |

Sceaux de la sortie, refaits ici : 161 compagnons `.sha256` revérifiés, 0 écart, 0 fichier absent ; 349 fichiers ; aucun `arret.json`.

Mes calculs (aucun module du dépôt importé ; `python3 -I` sous `nice -n 10`) :
- `R/lecteur/lire_rejeu_graine_v1.py` (`b3766fa4b2b9e372b8e0e269143b65cae4360770a02614bae73aa6e1fce3ead1`). Sa sortie est `R/lecteur/sortie-lire-rejeu-graine-v1.json` (`2df985f5595076344428501f524f124b5239aed0b78578d3ecd5cc5b877438cf`).
- `R/lecteur/complements_v1.py` (`91e473b77c21c711fc06f05651b47d8059ddfb4a2467bee03ce0f001a929da94`). Sa sortie est `R/lecteur/sortie-complements-v1.json` (`f2d009f2f8c54aa5bb90084835f43fab07d3793921100ee39c6b6acf3ee3c21e`).

## 2. Épisodes

Règle appliquée à chacun des 154 fichiers : « résolu » si et seulement si le champ `empreinte` est une empreinte de 256 bits égale au champ `empreinte_cible`. Je n'ai pas lu le drapeau `statut`. Je l'ai seulement comparé ensuite.

| Étape | Épisodes | Résolus (recalculé) | dont voie directe | dont repli (1 / 2 bascules) | Non résolus | dont « non tenté : durée » (budget de l'étape) | dont tentés, coupés par la durée pendant le repli | Autre cause |
|---|---|---|---|---|---|---|---|---|
| 0 Validation | 147 | **54** | 40 | 14 (11 / 3) | **93** | **90** | **3** | **0** |
| 1 Résolution | 7 | **7** | 2 | 5 (4 / 1) | 0 | 0 | 0 | 0 |
| Ensemble | 154 (151 épisodes distincts : les 3 de C-6 figurent aux deux étapes) | 61 | 42 | 19 | 93 | 90 | 3 | 0 |

Contrôles :
- Pour les 154 fichiers, le statut écrit est égal au statut recalculé. Le détail des résultats (`statut`, `empreinte_retrouvee`, `empreinte`) est égal aux fichiers. Les comptes écrits sont égaux aux comptes recalculés : `empreintes_retrouvees` 54 et 7 ; `directes` 40 et 2 ; `par_repli` 14 et 5 ; `non_tentes` 90 ; `non_resolus_duree` 93.
- Les 147 empreintes cibles sont distinctes.
- Pour les 25 occurrences d'épisodes présents dans la table v2 (18 en validation, 7 en résolution), l'empreinte cible est égale au `trajectoire_p3` de la table v2 scellée.
- Pour les 129 épisodes identiques de base, la cible ne vient que du fichier (voir § 10).
- Aucun caractère de remplacement U+FFFD dans les 147 (somme des `fffd` : 0) ; un seul dans les 7 (`mention/2605.17899v2/e0`).

**Non résolus tentés (3)**, validation. L'accord ci-dessous est mesuré contre le jeton retenu, qui n'est plus celui de P3 après le premier écart.

| Rang | Épisode | Cause écrite (recopiée) | Durée | Premier écart de la voie directe (pas, rang ; trouvé contre vrai ; écart contraint) | Repli | Accord / attendu ; pas informatifs (accord / attendu) |
|---|---|---|---|---|---|---|
| 0 | `honnete/2604.12086v1/e0` | « durée : budget de l'épisode épuisé pendant le repli (contradiction à l'essai direct (pas 2, jeton 207 : octets du texte restants au jeton de fin) ; 24 combinaison(s) essayée(s)) » | 600,14 s | (2, 4) ; 40 contre 5484 ; 0,1336 nat | 16 quasi-égalités (le premier écart est la 5e) ; 16 bascules simples et 8 paires ; 23 contradictions, la 24e coupée | 0,8187 / 0,4869 ; 219 (0,6667 / 0,0598) |
| 20 | `honnete/2508.10631v2/e0` | « durée : budget de l'épisode épuisé pendant le repli (contradiction à l'essai direct (pas 3, jeton 179 : octets du texte restants au jeton de fin) ; 18 combinaison(s) essayée(s)) » | 600,28 s | (3, 22) ; 264 contre 323 ; 0,0617 nat | 15 quasi-égalités (2e) ; 15 simples et 3 paires ; 17 contradictions | 0,9166 / 0,6069 ; 239 (0,7699 / 0,1193) |
| 56 | `saboteur/2512.01199v1/e0` | « durée : budget de l'épisode épuisé pendant le repli (empreinte de P3 non retrouvée à l'essai direct ; 44 combinaison(s) essayée(s)) » | **363,86 s** | (0, 130) ; 26954 contre 3122 ; 0,0966 nat. Empreinte calculée `e9220c3a…` ≠ cible `1974a9a0…` | 13 quasi-égalités (4e) ; 13 simples et 31 paires ; 42 contradictions et 1 empreinte différente | 0,9889 / 0,6650 ; 418 (0,9737 / 0,1376) |

L'épisode 56 a duré 363,86 s, moins que les 600 s de son budget propre. Il a été coupé par l'échéance de l'étape, car l'échéance d'un épisode est la plus proche des deux (`echeance_episode`, l. 662-667). Son libellé dit pourtant « budget de l'épisode » (réserve 6).

**Non tentés (90)**, validation. Tous portent `non_tente` vrai, une durée de 0 s, 0 passe et la cause « durée : budget de l'étape (2400 s) épuisé avant l'épisode k », avec k égal à leur rang. Ils couvrent les rangs 57 à 146, sans trou. Entre parenthèses, la méthode de la table v2 pour les épisodes corrigés :
57 `temoin/2512.01199v1/e0` ; 58 `mention/2512.01199v1/e0` ; 59 `honnete/2511.18601v1/e0` ; 60 `temoin/2511.18601v1/e0` ; 61 `mention/2511.18601v1/e0` ; 62 `honnete/2510.20877v1/e0` ; 63 `saboteur/2510.20877v1/e0` ; 64 `temoin/2510.20877v1/e0` ; 65 `mention/2510.20877v1/e0` ; 66 `honnete/2602.07160v1/e0` ; 67 `saboteur/2602.07160v1/e0` ; 68 `temoin/2602.07160v1/e0` ; 69 `mention/2602.07160v1/e0` ; 70 `honnete/2602.09690v1/e0` ; 71 `saboteur/2602.09690v1/e0` ; 72 `temoin/2602.09690v1/e0` ; 73 `mention/2602.09690v1/e0` ; 74 `honnete/2510.05132v3/e0` ; 75 `mention/2510.05132v3/e0` ; 76 `honnete/2601.01484v2/e0` ; 77 `honnete/2510.24061v1/e0` ; 78 `mention/2510.24061v1/e0` ; 79 `honnete/2512.03125v1/e0` ; 80 `saboteur/2512.03125v1/e0` ; 81 `mention/2512.03125v1/e0` ; 82 `honnete/2603.06922v2/e0` ; 83 `mention/2603.06922v2/e0` ; 84 `honnete/2510.21366v3/e0` ; 85 `saboteur/2510.21366v3/e0` ; 86 `temoin/2510.21366v3/e0` ; 87 `mention/2510.21366v3/e0` (une_paire) ; 88 `honnete/2510.02245v2/e0` ; 89 `temoin/2604.17568v1/e0` ; 90 `honnete/2511.00962v1/e0` ; 91 `saboteur/2511.00962v1/e0` ; 92 `mention/2511.00962v1/e0` ; 93 `honnete/2510.24709v2/e0` ; 94 `mention/2510.24709v2/e0` ; 95 `honnete/2506.01420v2/e0` ; 96 `saboteur/2506.01420v2/e0` (une_paire) ; 97 `temoin/2506.01420v2/e0` (une_paire) ; 98 `mention/2506.01420v2/e0` ; 99 `saboteur/2510.14562v1/e0` ; 100 `mention/2510.14562v1/e0` ; 101 `saboteur/2509.23173v2/e0` ; 102 `temoin/2509.23173v2/e0` ; 103 `mention/2509.23173v2/e0` (une_paire) ; 104 `honnete/2512.00930v1/e0` ; 105 `mention/2512.00930v1/e0` ; 106 `honnete/2509.24912v2/e0` ; 107 `saboteur/2509.24912v2/e0` ; 108 `temoin/2509.24912v2/e0` ; 109 `mention/2509.24912v2/e0` ; 110 `honnete/2506.05216v2/e0` ; 111 `saboteur/2506.05216v2/e0` ; 112 `temoin/2506.05216v2/e0` ; 113 `mention/2506.05216v2/e0` ; 114 `saboteur/2602.01329v1/e0` ; 115 `honnete/2509.03810v2/e0` ; 116 `temoin/2509.03810v2/e0` ; 117 `mention/2509.03810v2/e0` (deux_paires) ; 118 `mention/2512.06870v2/e0` ; 119 `honnete/2512.05150v2/e0` (fenetre, C-6) ; 120 `saboteur/2512.05150v2/e0` ; 121 `temoin/2512.05150v2/e0` ; 122 `mention/2512.05150v2/e0` (deux_paires) ; 123 `saboteur/2604.18258v1/e0` ; 124 `temoin/2604.18258v1/e0` ; 125 `mention/2604.18258v1/e0` ; 126 `honnete/2512.11131v1/e0` (fenetre, C-6) ; 127 `saboteur/2512.11131v1/e0` ; 128 `temoin/2512.11131v1/e0` ; 129 `mention/2512.11131v1/e0` ; 130 `honnete/2601.22135v1/e0` ; 131 `mention/2601.22135v1/e0` ; 132 `honnete/2510.02779v4/e0` ; 133 `mention/2510.02779v4/e0` ; 134 `temoin/2506.09007v2/e0` ; 135 `mention/2506.09007v2/e0` (une_paire) ; 136 `honnete/2510.24788v1/e0` (une_paire) ; 137 `temoin/2510.24788v1/e0` (trois_paires, C-6) ; 138 `saboteur/2510.23574v1/e0` ; 139 `temoin/2510.23574v1/e0` ; 140 `mention/2510.23574v1/e0` ; 141 `saboteur/2510.21310v2/e0` ; 142 `temoin/2510.21310v2/e0` ; 143 `honnete/2602.04162v2/e0` ; 144 `saboteur/2602.04162v2/e0` ; 145 `temoin/2602.04162v2/e0` ; 146 `mention/2602.04162v2/e0`.

**Les 18 corrigés de la table v2** (`corriges_table_v2`, recalculé) : 7 tentés et résolus, avec des identifiants égaux à ceux de la table v2 (6 une_paire, 1 fins) ; 11 non tentés (6 une_paire, 2 deux_paires, 2 fenetre, 1 trois_paires, dont les 3 de C-6).

**Résolus par repli (14)**, validation, donnés comme rang, bascules, durée et combinaisons :
- 14 `temoin/2603.01762v1/e0` : 2 bascules, 53,02 s, 6 combinaisons ;
- 16 `honnete/2602.15124v1/e0` : 1, 15,83 s, 1 ;
- 17 `saboteur/2602.15124v1/e0` : 1, 5,79 s, 1 ;
- 23 `honnete/2605.17899v2/e0` : 1, 16,06 s, 3 ;
- 24 `saboteur/2605.17899v2/e0` : 2, 57,22 s, 7 ;
- 25 `honnete/2509.22925v2/e0` : 1, 51,99 s, 2 ;
- 26 `saboteur/2509.22925v2/e0` : 1, 9,82 s, 1 ;
- 41 `mention/2604.23720v1/e0` : 2, 176,70 s, 18 ;
- 43 `honnete/2605.29097v2/e0` : 1, 6,60 s, 1 ;
- 45 `mention/2605.29097v2/e0` : 1, 26,67 s, 1 ;
- 47 `honnete/2512.02017v1/e0` : 1, 8,37 s, 2 ;
- 48 `mention/2512.02017v1/e0` : 1, 89,00 s, 2 ;
- 50 `saboteur/2507.11818v2/e0` : 1, 39,63 s, 3 ;
- 51 `saboteur/2510.25798v1/e0` : 1, 31,36 s, 4.

**Déclarations (`declarer`).** Les épisodes de la validation n'en portent pas : le code ne déclare qu'à l'étape « resolution » (l. 1616-1617), et le texte ne prévoit de déclaration que pour les épisodes de la résolution. Les 7 de la résolution portent « résolu (empreinte de P3 retrouvée) ». J'ai recalculé ces déclarations par la règle écrite du texte (« Seuil », Conséquences) : elles sont égales. Elles sont recopiées à l'identique dans `declarations` de la table v3.

## 3. Classe de la validation, recalculée

- R = 54 (recalculé), E = 147 (compte exact, exigé avant la boucle et atteint).
- Règle gelée, étape 1 : E > 0 et R < E. La classe est donc **« méthode non transposée »**, quelles que soient les mesures d'accord.
- La sortie écrit « méthode non transposée » : **égal**. Elle porte aussi `lecture` = « sous le seuil », qui n'est qu'un compte sans conséquence (« Seuil »).
- Les quatre conditions d'accord n'entrent pas dans la classe, puisque l'étape 1 de la règle décide. Je les ai recalculées sur le tableau des pas, à titre informatif. Elles sont égales aux conditions écrites :
  - accord moyen par épisode 0,98779 ≥ 0,95 : tenue ;
  - **accord minimum par épisode 0,81867 ≥ 0,90 : manquée**. Ce minimum est `honnete/2604.12086v1/e0`, un épisode non résolu ; sur les 54 résolus seuls, le minimum est 0,98608 ;
  - pas informatifs 29 129 ≥ 1 000 : tenue ;
  - accord informatif 0,97545 ≥ 0,90 : tenue.

Accords et accords attendus sous graine indépendante. Tous sont recalculés depuis les tableaux des pas et égaux aux valeurs écrites, à 10⁻¹⁶ près. Ils portent sur les seuls épisodes tentés : les 90 non tentés n'ont aucun pas (`episodes_sans_pas`).

| Mesure | Validation (57 épisodes mesurés, 115 008 pas) | Validation, 54 résolus seuls (informatif, hors règle) | Résolution (7 épisodes, 17 848 pas) |
|---|---|---|---|
| Accord moyen par épisode | 0,98779 | 0,99222 | 0,99250 |
| Accord minimum par épisode | 0,81867 | 0,98608 | 0,99065 |
| Accord sur les pas réunis | 0,99092 | 0,99230 | 0,99249 |
| Pas informatifs | 29 129 | 28 253 | 7 170 |
| Accord sur les pas informatifs | 0,97545 | 0,97961 | 0,98591 |
| Attendu sous graine indépendante, moyen par épisode | 0,68057 | 0,68581 | 0,54501 |
| Attendu sous graine indépendante, sur les pas | 0,68097 | 0,68265 | 0,53676 |
| Attendu sur les pas informatifs | 0,10606 | 0,10584 | 0,05863 |

## 4. Résolution, contrôle croisé, table v3

**Résolution : 7 sur 7.** Lecture écrite « complète ». Détail par épisode :

| Épisode | Voie | Bascules (pas, rang) | Durée | Correction retrouvée (action : premier rang différent, jetons changés) |
|---|---|---|---|---|
| `honnete/2512.05150v2/e0` (C-6) | repli | (3, 28) ; (5, 210) | **572,02 s** (23 combinaisons) | action 4 : rang 384, 3 jetons (la fenêtre de la table v2) |
| `honnete/2512.11131v1/e0` (C-6) | repli | (1, 220) | 9,32 s | action 7 : rang 82, 3 jetons (la fenêtre de la table v2) |
| `temoin/2510.24788v1/e0` (C-6) | repli | (0, 62) | 65,40 s | action 2 : rangs 113 à 281 (les trois paires de la table v2) |
| `honnete/2602.00987v1/e0` | repli | (0, 218) | 9,51 s | action 4 : à partir du rang 212 (152 positions, longueur 400 inchangée) |
| `mention/2605.17899v2/e0` (U+FFFD) | repli | (0, 6) | 96,29 s | action 6 : rang 165, 1 jeton |
| `saboteur/2510.05132v3/e0` | directe | — | 6,16 s | action 4 : à partir du rang 196 (53 positions) |
| `temoin/2512.06870v2/e0` | directe | — | 6,08 s | actions 0, 4 et 6 : 3, 2 et 1 jetons |

Durée de l'étape : 800,4 s, avec 3 447 passes.

Aucune bascule ne tombe sur une position de découpage non canonique de P3. Les découpages connus (table v2) ou nouveaux sont tous désignés par p / q sous les graines. Les bascules réparent ailleurs des quasi-égalités où la passe forcée classait autrement que P3. On voit la même chose sur les 7 corrigés tentés en validation : tous retrouvés par la voie directe, sauf `mention/2604.23720v1/e0`, dont les bascules (2, 120) et (6, 245) sont hors de la paire (8, 381). Cela fait 14 épisodes au total.

**Caractère de remplacement (`mention/2605.17899v2/e0`).**
- Un U+FFFD, plafond de l'essai de 16.
- La sortie écrit `balayages` = 0. Le tableau des pas du chemin retenu porte pourtant **2 pas comptés**, à l'action 6, rangs 164 et 165, avec 255 et 900 candidats. Le compte écrit est celui de l'essai direct, qui s'est arrêté dans l'action 0 (réserve 6).
- Aux deux pas, le choix non contraint (argmax de p / q sur tout le vocabulaire) égale le jeton de P3, alors que p_k vaut 3,8·10⁻⁴ puis 2,5·10⁻⁶. Une graine indépendante ne le donnerait qu'avec cette probabilité.
- Le plafond de 16 n'a pas été approché.

**Contrôle croisé.** La sortie écrit « conforme ». Je l'ai recalculé :
- pour chacun des 3, les identifiants de base du résultat coïncident avec les jetons « canonique » de la table v2 aux positions qu'elle déclare ;
- base plus remplacements « p3 » de la table v2 donne exactement les identifiants retrouvés ;
- empreinte retrouvée = cible = `trajectoire_p3` de la table v2.

Lecture recalculée : **« conforme »**. Mais aucun des 3 n'a été tenté à l'étape 0 : ce sont les non tentés 119, 126 et 137. Ce contrôle n'est donc pas la répétabilité que le texte décrit (réserve 3).

**Table v3** (`ead8a668…`, version 3, 22 entrées).
- Méthodes : 12 une_paire, 2 deux_paires, 1 trois_paires, 2 fenetre, 1 fins, **4 identifiants**. **0 entrée `non_resolu`.**
- `identiques_apres_table` = 151 = 129 + 22 (recalculé). `corrections_verifiees` = 22 = 151 − 129.
- Les 18 entrées de la v2 sont gardées telles quelles (égalité objet à objet).
- Les 4 entrées nouvelles :
  - `trajectoire_p3` égale à la v2 et à l'empreinte retrouvée ;
  - `actions` égales aux différences entre identifiants de base et identifiants retrouvés du résultat ;
  - `resolution_graine` porte la voie, les bascules, la classe « méthode non transposée », la déclaration « résolu » et `resultat_sha256` = `674825453a…`.
- `declarations` : 7 fois « résolu (empreinte de P3 retrouvée) ».
- `lecture_validation` est égale à celle du résultat de la résolution (forme « cœur seul », `classe` en tête : « méthode non transposée »).
- `resultat_graine_sha256` = empreinte du résultat de la résolution ; `table_v2_sha256` = `5f6cf489…`.
- `resultat_hors_table` vide ; pas de `lecture_lot` (lot sans objet).
- La table est **complète**.

## 5. Application ligne à ligne des critères gelés

| Issue observée | Ligne du tableau « Critères de lecture gelés » | Ce qu'elle dit | Ce qui en découle ici |
|---|---|---|---|
| Validation : 54 sur 147 ; causes : toutes des durées | « Validation « méthode non transposée » (moins de 147 retrouvées, cause quelconque, « non tenté : durée » compris) » | « Réserve sur HG-2 : la résolution est partie ; ses empreintes retrouvées restent des preuves ; tout non résolu est un nœud à Lazar (…) ; les épisodes manqués, leurs causes et leurs écarts sont rapportés ; si une cause est une durée, la mesure est déclarée incomplète » | Réserve sur HG-2, écrite (§ 8, réserve A). La résolution est partie à 17:58:06 et ses 7 empreintes retrouvées sont des preuves. Aucun non résolu à la résolution, donc **aucun nœud par cette ligne**. Les 93 manqués et leurs causes sont rapportés (§ 2), avec les premiers écarts des 3 tentés ; les 90 non tentés n'ont pas de pas, donc pas d'écart. **Mesure de validation déclarée incomplète** (réserve B). |
| (classes non observées) | « graines validées » ; « méthode transposée, graines non validées » | — | Ne s'appliquent pas. |
| Distribution des écarts contraints | « Distribution des écarts contraints » | Descriptive (P-G3), sans conséquence de décision | § 7. |
| Lot : aucune cible (`cibles-lot.json` : 0 ; journal 18:11:35) | Les trois lignes du lot (« fidèle », « réserve lot non fidèle », « sans mesure ») supposent un lot exécuté | Étape « cibles du lot » : « Aucune cible : l'étape du lot est « sans objet », consigné au journal, jamais un arrêt ; la table v3 est alors construite sur le cœur seul » | Aucune ligne du lot ne s'applique. Lot « sans objet », consigné. Table du cœur seul. |
| Résolution : 7 / 7 à la fin de l'étape 1, lot « sans objet », contrôle croisé « conforme » | « Résolution : 7 / 7 à la fin de l'étape 1 bis (ou de l'étape 1, lot « sans objet »), contrôle croisé conforme » | « **Table v3 complète** ; addendum v3 sans règle B » | **Table v3 complète** (`ead8a668…`). **Addendum v3 sans règle B.** La ligne « k non résolus » ne s'applique pas (k = 0) : aucune liste à remettre à Lazar. |
| Contrôle croisé « conforme » | Lignes « non résolu » et « contraire » | — | Ne s'appliquent pas. La garde de l'étape table (contrôle croisé « conforme » exigé, l. 1025-1027) a laissé construire la table. |
| Audit de symétrie | « Audit de symétrie (R4) » | Déclencheurs chiffrés | Aucun ne part (§ 6). |

Ce qui en découle, au total :
- table v3 complète ;
- addendum v3 sans règle B ;
- **aucun nœud porté à Lazar par les critères gelés** ;
- réserves : HG-2 et mesure incomplète (exigées), deux de la concordance, quatre du lecteur.

Rien n'est un arrêt. La liste d'arrêt range parmi « ce qui n'est pas un arrêt » : toute classe de la validation, moins de 147 retrouvées, le budget d'étape épuisé et le lot « sans objet ».

## 6. Audit de symétrie (R4)

**Déclencheurs écrits** (ligne « Audit de symétrie » des critères) :

| Déclencheur | Valeur observée | Seuil écrit | Part ? |
|---|---|---|---|
| Accord non contraint égal à 1 exactement sur tous les pas des 147 | 1 044 désaccords sur 115 008 pas mesurés, soit un accord de 0,99092. Les 90 non tentés n'ont pas de pas, mais un seul désaccord suffit à écarter ce déclencheur. | = 1 exactement | Non |
| Aucune quasi-égalité sous 1 | 836 pas d'écart contraint sous 1 nat (dont 17 pas basculés, d'écart négatif) | aucun | Non |
| Durée cumulée des étapes 0 et 1 sous 5 min | 2 408,0 + 800,4 = 3 208,4 s (53 min 28 s), au-dessus de l'estimation de 15 à 40 min | < 300 s | Non |
| `accord_sur_les_pas` ≤ `attendu_graine_independante_sur_les_pas` + 0,02 (étape 0) | 0,99092 contre 0,68097 + 0,02 = 0,70097 | ≤ | Non |
| `accord_informatif` ≤ `attendu_informatif` + 0,10 (sous les deux autres classes seulement ; ici « méthode non transposée », donc applicable) | 0,97545 contre 0,10606 + 0,10 = 0,20606 | ≤ | Non |
| Lot fidèle : un accord de 1 exactement est la prédiction, non un signal | lot non exécuté | — | Sans objet |

L'audit n'est donc pas déclenché par le texte. Par construction du code, les identifiants connus ne peuvent pas avoir fui dans la résolution : `resoudre_avec_repli` ne reçoit ni table, ni reconstruction de base, ni vérité (l. 1565-1566), et la comparaison aux identifiants connus n'a lieu qu'après la boucle (l. 1579-1586).

**Le résultat décevant (validation incomplète), examiné comme un résultat trop propre le serait.**

1. *Causes.*
   - Les 93 manqués ont tous une cause de durée : 90 « non tentés » (budget de l'étape) et 3 coupés pendant le repli (deux au budget d'épisode de 600 s, un à l'échéance de l'étape).
   - **Aucun** épisode ne finit sur une cause qui conclurait à un échec de la méthode : pas de repli épuisé, pas de budget de balayages dépassé, pas de contradiction terminale, pas d'empreinte différente après un repli complet.
2. *Horodatages.*
   - Manifeste de la validation créé à 17:17:53. L'horloge du budget part juste après (l. 1730-1734), donc avant le chargement du modèle et le classement. Échéance vers 17:57:53.
   - La boucle commence à 17:18:25.
   - Le premier non tenté (rang 57) et les 89 suivants sont écrits à 17:57:54. Le compteur de passes reste à 10 627 des lignes « 60/147 » à « 147/147 ».
   - Résultat écrit à 17:58:02 (`duree_s` 2 408,0).
3. *Usage du budget.* Les 57 épisodes tentés totalisent 2 362,1 s :
   - 40 directs : 209,8 s (5,2 s en moyenne) ;
   - 14 par repli : 588,1 s (42,0 s en moyenne, au plus 176,7 s) ;
   - **3 non résolus : 1 564,3 s, soit 65 % des 2 400 s**.
4. *Passes* (lignes de progression du journal, par tranche de dix rangs) :

   | Rangs | Passes de la tranche | Hors épisodes directs | Composition |
   |---|---|---|---|
   | 0 à 9 | 3 062 | 2 971, toutes pour le rang 0 (les rangs 1 à 9 sont directs) | 1 non résolu, 9 directs |
   | 10 à 19 | 384 | 313 | 3 résolus par repli, 7 directs |
   | 20 à 29 | 3 316 | 3 266 | rang 20 et 4 résolus par repli |
   | 30 à 39 | 103 | 0 | 10 directs, 51,9 s |
   | 40 à 49 | 1 597 | 1 547 | 5 résolus par repli (dont le rang 41, 176,7 s), 5 directs |
   | 50 à 59 | 2 165 | 2 125 | rang 56 et 2 résolus par repli |

   Les passes écrites par épisode ne comptent que l'essai direct : 151 pour le rang 0 (réserve 6).
5. *La méthode.*
   - La voie directe a échoué dans **17 des 57 épisodes tentés (30 %)**. P-G1 en attendait au plus 7 sur 147.
   - Les 17 premiers écarts sont des quasi-égalités : écart contraint de 0,0037 à 0,134 nat, sous `seuil_ecart` = 1,0. La marge non contrainte lui est égale à 10⁻⁷ près. C'est le cas que HG-2 prévoit (« sauf aux quasi-égalités, que le repli écrit traite ») et que le repli traite : 14 sauvés.
   - Pour les 3 restants, le premier écart figurait dans la frontière du repli (5e, 2e et 4e quasi-égalité). Toutes les bascules simples ont été essayées sans succès. Le niveau des paires était en cours (8, 3 et 31 paires) quand le temps a manqué.
   - Rien ne conclut un échec de la méthode, et rien ne conclut non plus que ces 3 épisodes auraient été résolus.
6. *Les graines.*
   - Sur les 54 résolus, il y a 863 désaccords pour 112 083 pas (0,77 %), dont 861 à une marge sous 0,5 nat.
   - L'accord informatif est de 0,97961, contre 0,10584 attendu sous graine indépendante.
   - Les découpages non canoniques de P3 ne sont jamais trouvés par une bascule (§ 4, 14 épisodes).

**Conclusion de l'audit.** La validation incomplète tient au **budget de temps de l'étape**, directement pour 90 des 93 épisodes et dans leur cause pour les 3 autres. Ce budget a été consommé à 65 % par trois épisodes dont le repli n'a pas abouti à temps. Le facteur sous-jacent est un taux d'échec de la voie directe (30 %) bien au-dessus de P-G1. Ce taux rend le repli fréquent et coûteux en passes. Aucun épisode observé ne conclut à une défaillance de la méthode. La classe « méthode non transposée » s'applique telle qu'écrite.

**Le résultat propre (7 sur 7 en résolution), examiné de même.**
- Les empreintes sont calculées, non recopiées : au rang 56 de la validation, l'empreinte calculée (`e9220c3a…`) diffère de la cible.
- Les cibles égalent la table v2 scellée pour les 25 occurrences vérifiables.
- Il n'y a aucune fuite possible des identifiants connus (voir plus haut).
- 134 désaccords sur 17 848 pas, tous à une marge sous 0,25 nat : ce n'est pas un accord de 1 exactement.
- Les identifiants des 3 de C-6 retrouvés par la graine égalent ceux de la table v2, trouvés par une autre méthode.
- Seule fragilité : `honnete/2512.05150v2/e0` a été résolu à 572,02 s de ses 600 s, et la table v3 en dépendait (réserve 5).

## 7. Prédictions (descriptives : elles ne décident rien)

| Prédiction | Prédit (confiance) | Observé |
|---|---|---|
| P-G1, empreintes retrouvées | 147 sur 147 (≈ 0,8) | **54 sur 147** (57 tentés, dont 54 résolus) : réfutée. C'est l'issue prévue par le texte, classe « méthode non transposée ». |
| P-G1, voie directe | au moins 140 | 40 (sur 57 tentés) |
| P-G1, accord | ≥ 0,99 en moyenne par épisode et ≥ 0,95 dans chaque épisode (≈ 0,7) | 0,98779 en moyenne, minimum 0,81867 (épisode non résolu). Sur les 54 résolus : 0,99222 et 0,98608. |
| P-G1, pas informatifs | au moins 1 000 (≈ 0,9) | 29 129 |
| P-G1, accord informatif | au moins 0,95 (≈ 0,6) | 0,97545 (résolus seuls : 0,97961) |
| P-G1, attendu informatif | au plus ≈ 0,5 | 0,10606 |
| P-G2, fin de l'étape 1 bis | au moins 6 sur 7 (≈ 0,8) ; 7 sur 7 (≈ 0,6) | **7 sur 7 dès l'étape 1** (1 bis sans objet) |
| P-G2, passe forcée seule (étape 1) | au moins 5 sur 7 (≈ 0,6) | 7 sur 7 avec le repli de l'étape 1, dont 2 par la voie directe seule |
| P-G2, contrôle croisé | « conforme » (≈ 0,95), présenté comme une répétabilité | « conforme », mais sans répétabilité : les 3 n'ont pas été tentés à l'étape 0 |
| P-G2, `mention/2605.17899v2/e0` | le plus exposé ; s'il échoue, cause attendue « budget de balayages dépassé » | Résolu par repli (bascule en (0, 6), hors de l'action à U+FFFD). 2 pas comptés sur le chemin retenu, plafond 16. |
| P-G3, écart contraint sous 1 nat | moins de 1 % des pas à plusieurs candidats | 836 / 115 008 = 0,73 % en validation ; 137 / 17 848 = 0,77 % en résolution. Tous les pas comptent comme « à plusieurs candidats », car les jetons spéciaux hors fins y sont toujours ajoutés (l. 549). |
| P-G3, désaccords | concentrés sur des marges sous 0,5 nat | Validation : 921 / 1 044 (88,2 %) ; 861 / 863 (99,8 %) sur les 54 résolus ; les 3 non résolus portent 121 des 123 désaccords à marge ≥ 0,5, parce qu'ils sont mesurés contre un chemin qui n'est plus celui de P3. Résolution : 134 / 134, tous sous 0,25. |
| P-G4 (lot fidèle) | accord des voisines ≥ 0,999 ; lecture « fidèle » ; forme des quatre lots | Lot non exécuté (sans objet) : rien d'observé. Les formes calculées sans modèle (lots 0, 14 et 24 prouvés, lot 5 non prouvé) restent sans emploi. |

## 8. Réserves

**Exigées par les critères gelés (ligne « méthode non transposée »)**

- **A. Réserve sur HG-2.** La validation à l'aveugle ne retrouve que 54 empreintes sur 147. Les empreintes retrouvées de la résolution restent des preuves (texte) : la réserve ne retire aucune entrée de la table v3, dont chaque correction est revérifiée par l'empreinte de P3 (`corrections_verifiees` = 22). Sous cette classe, aucun non résolu ne pourrait être déclaré non inversible (`declarer`). Il n'y a ici aucun non résolu.
- **B. Mesure de validation déclarée incomplète.** La cause des 93 manqués est une durée. La mesure ne porte que sur 57 épisodes : 54 résolus et 3 coupés. 11 des 18 corrigés de la table v2 n'ont pas été tentés : tous ceux de forme « deux_paires », « fenetre » et « trois_paires », plus 6 « une_paire ».

**Portées par la concordance (décision R-1258)**

- **1. VI-09 est un relâchement non signalé par le texte.**
  - Brouillon 3 : une seule cible « réserve » rendait nœuds tous les non résolus du lot. Texte scellé : chaque cible se lit sur la lecture de son propre lot.
  - Ce relâchement ne peut jouer que pour `mention/2605.17899v2/e0`, seule cible déclarable non inversible. Il faut pour cela quatre conditions : cause finale au lot « budget de balayages dépassé », classe « graines validées », lot 5 lu « fidèle », et un autre lot lu « réserve ». Or le lot 5 est justement le seul dont la forme n'est pas prouvée.
  - *Effet dans ce passage : aucun.* Le lot n'a pas tourné, `mention` est résolue, et la classe n'est pas « graines validées ».
- **2. Le compte qui justifie le plafond de 16 balayages n'est pas recopié près du seuil.**
  - Ce compte est de 2 pas comptés sur le chemin canonique de `mention/2605.17899v2/e0` (`comptes_reels-sortie.txt`, `a2bd318f…`, ligne (b) : « pas comptés 2 (dont complets 1) »).
  - « Seuil » ne donne pas ce chiffre, et « Déclaré » range encore 16 parmi les valeurs au choix de l'auteur.
  - *Observé dans ce passage* : 2 pas comptés sur le chemin retenu de P3 (tableau des pas, action 6), plafond 16, non approché. La sortie écrit 0 (réserve 6).

**Du lecteur**

- **3. Le contrôle croisé « conforme » n'est pas une répétabilité.**
  - Le texte présente ce contrôle comme une répétabilité (« Plan d'analyse », étape 1 : « ils ont été retrouvés à l'aveugle parmi les 18 de l'étape 0 » ; P-G2 : « ils font déjà partie des 147 de l'étape 0 »).
  - Or les 3 épisodes de C-6 n'ont pas été tentés à l'étape 0 (rangs 119, 126 et 137, non tentés).
  - La valeur « conforme » tient par sa définition écrite (empreinte retrouvée, identifiants égaux à la table v2). Elle dit seulement que deux voies, chacune prouvée par l'empreinte, s'accordent, ce qui est garanti hors collision.
  - La répétabilité sur la même carte n'est éprouvée par aucun épisode de ce passage. C'est un écart entre la prémisse du texte et l'exécution, sans changement de lecture.
- **4. Le budget de l'étape de validation était insuffisant au taux observé.**
  - 2 400 s, chargement du modèle et classement compris, pour 147 épisodes. La somme des durées des 57 épisodes tentés atteint déjà 2 362 s.
  - Le texte prévoit le cas dans la lecture (« « non tenté : durée » compris »). Il ne chiffre le risque de non tentés que pour la résolution (« Plan d'analyse », point 6), non pour les 147.
  - Le taux de voie directe observé (40 sur 57) est loin de P-G1 (au moins 140 sur 147). L'estimation « validation et résolution 15 à 40 min » est dépassée (53 min 28 s).
- **5. Marge étroite d'un épisode de C-6.**
  - `honnete/2512.05150v2/e0` a été résolu à 572,02 s de son budget de 600 s (23 combinaisons, 2 bascules).
  - Coupé, il aurait rendu le contrôle croisé « non résolu », et la garde de l'étape table aurait empêché la table v3.
  - Descriptif. Une réexécution n'est pas permise sous ce texte (R3).
- **6. Comptes écrits par épisode et libellé de cause : écarts de compte rendu entre la sortie et le texte, sans effet sur aucune lecture.**
  - (a) Pour un épisode résolu par repli, `balayages`, `balayages_complets` et `passes` écrits sont ceux de l'essai direct seul : `sortie.update(…)` l. 726-727, que le retour « résolu » du repli (l. 761-765) ne met pas à jour.
    - Le texte (« Métrique ») promet des pas de recherche sur octets inconnus « comptés par épisode ».
    - Pour `mention/2605.17899v2/e0`, la sortie écrit 0 contre 2 pas comptés sur le chemin retenu.
    - Le rang 0 de la validation écrit 151 passes contre 2 971 dépensées. Le compte de 2 971 est déduit du journal, comme différence avec les passes écrites des épisodes directs de la même tranche.
    - Le plafond, lui, est appliqué à chaque essai par un compteur neuf (l. 750).
  - (b) La cause du rang 56 dit « budget de l'épisode épuisé pendant le repli », alors qu'il a été coupé à 363,86 s par l'échéance de l'étape. Les deux causes sont des durées, et la lecture n'en dépend pas.

## 9. Ce qui suit selon le texte (et seulement selon lui)

- **Table v3 complète**, scellée (`ead8a66851b2af5dfa02635297056872032878fbd2987ba780fb6c9096766423`). L'**addendum v3** (`prereg/R1-addendum-relance-v3.md`, nom réservé) est écrit et scellé après elle, **sans règle B**.
  - Il cite l'empreinte de la table v3 et celles des résultats scellés de ce rejeu : validation `8e6a4912…`, résolution `674825453a…`. Il cite aussi le commit et le nombre d'essais de son propre code.
  - Il est contre-lu et soumis à la concordance de conv-audit avant tout lancement.
  - Ses attentes de réception sont réécrites (m-8) : empreinte de la table v3 au lieu de `5f6cf489…`, et liste des non résolus vide au lieu des 4.
- **Aucune liste de non résolus** à remettre à Lazar (k = 0). **Aucun nœud** porté par les critères gelés.
- La **classe « méthode non transposée »** reste attachée au passage. Elle est recopiée dans la table v3 (`lecture_validation`), avec les réserves A et B. Les réserves 1 et 2 (concordance) et 3 à 6 (lecteur) accompagnent le verdict.
- **R3** : aucune étape n'est réexécutée sous ce texte. Compléter la validation relèverait d'un texte neuf, et aucune ligne du texte ne le demande.
- Le verdict est scellé, puis soumis à Lazar (fiche, section 6).

## 10. Incertitudes et ce que je n'ai pas pu vérifier

- **Empreintes de P3 des 129 épisodes identiques de base.** Je n'ai pas ouvert les fiches de P3 (`diag/20261019-230011-p3-reel/episodes-p3.json`), qui sont hors de la liste. La cible de ces épisodes ne vient que des fichiers de la sortie. Les 25 occurrences présentes dans la table v2 scellée sont vérifiées.
- **Recalcul des empreintes à partir des identifiants : impossible ici.** Il faudrait les textes, les tâches et les consignes de P3, sous `donnees/` (interdit). « Résolu » repose donc sur l'égalité des deux champs écrits.
  - Ce qui borne le risque d'un défaut d'écriture : une empreinte calculée différente de sa cible existe (rang 56) ; l'étape table a revérifié les 22 corrections par l'empreinte de P3 ; les 4 entrées nouvelles portent la trajectoire de la table v2 scellée.
- **Graines.** Elles ne sont pas redérivées : le manifeste de P3 n'a pas été ouvert. Leur justesse n'est vue qu'à travers l'accord non contraint (§ 3 et 6).
- **Code de la résolution.** L'arbre du code entre `c2a8b6e1` (validation) et `3482d8f1` (résolution) n'est pas vérifiable ici. Je m'appuie sur la garde `exiger_meme_code` (l. 1441-1454), qui aurait arrêté l'étape, et sur `depot_propre` vrai. C'est une réserve héritée des contrôles de réception, comme la réserve R-a (ni `GO_ID` ni identifiant d'instance dans la sortie scellée).
- **Passes par épisode.** Le nombre exact n'est connu que pour le rang 0 (2 971). Pour les rangs 20 et 56, seule une borne haute est connue (3 266 et 2 125, partagés avec 6 épisodes résolus par repli).
- **Balayage complet.** Le tableau des pas ne porte pas de colonne « complet ». Je ne peux pas dire lequel des 2 pas comptés de `mention` a examiné tout le vocabulaire (le pré-vol en annonçait 1 sur 2).
- **Fichiers non ouverts.** `resolution_tokenisation_v1.py` n'a pas été ouvert (empreinte seule, § 1). Le module du lot et le script d'instance n'ont été parcourus que par recherche. Les ajustements du lot (P-G4, VI-09) sont restés sans objet.
- **Concordance.** Je ne l'ai lue que sur les lignes 80 à 115 et sur les lignes trouvées par recherche (§ 1).
- **Calcul sans `nice -n 10`.** Plusieurs courtes commandes d'inspection (lectures de champs, moins d'une seconde chacune) ont tourné sans `nice -n 10`. Les deux scripts de calcul ont tourné avec.
