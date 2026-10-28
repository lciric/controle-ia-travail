# Rétrodiction sur arXiv : la marche « à la Swanson » relie-t-elle mieux les champs éloignés ? — v1

Exécution du brief `BRIEF-retrodiction-swanson-v1.md` (empreinte `3b83d113…c7c0e4`) selon le préenregistrement
`preenregistrement-retrodiction-v1.md` (empreinte `7a4868aa48cfff5eb48937b0a1a99647fc9968c44c1fe8a7bb8047629b3c91eb`,
scellé à 20:13:35 UTC, avant tout calcul). Sous-agent neuf de la lignée conv-audit, 26 octobre 2026.

## Décisions (figées par le brief, découpage principal : avant 2003-2010, après 2011-2016)

- **D1 — réfutée.** Précision à 10 000 : marche à la Swanson (S) **9,83 %** [9,22 ; 10,44] contre tirage stratifié (ST)
  **0,22 %** [0,14 ; 0,32] ; écart **+9,61 points** [+8,98 ; +10,23], sous le seuil de 12 points. La marche n'est pas
  retenue comme règle de tirage de la version 0.
- **D2 — pas de contribution.** Meilleure méthode classique = **allocation de ressources (RA) : 10,65 %**
  [10,08 ; 11,23]. Écart S − RA = **−0,82 point** [−1,43 ; −0,25] : S est *en dessous*, pas 2 points au-dessus ; les
  intervalles se recouvrent. Selon la règle, on adopte l'allocation de ressources **sous son nom**, sans revendication.
- Contrôles : permutations des issues réussies (toutes les méthodes au taux de base) ; placebo 2003-2006 / 2007-2010
  **stable** (même ordre des cinq méthodes à score, tau de Kendall = 1 sur les sept) ; essais d'absence de fuite
  temporelle réussis (cas sain, artefact pris, référence lente à 4e−15 près).

Les nombres (intervalles à 95 % par rééchantillonnage des paires, 1 000 tirages) viennent de
`resultats/issues-v1.json` et `resultats/synthese-v1.json` (empreintes dans la table des sources, fin du document).

## Résultats du découpage principal

1 000 000 de paires candidates, 2 752 positives : **taux de base 0,2752 %** [0,2651 ; 0,2857] (Wilson).

| méthode | précision à 1 000 (%) | précision à 10 000 (%) | précision moyenne (%) | aire sous la courbe de fonctionnement du récepteur |
|---|---|---|---|---|
| S, marche à la Swanson (moyenne des deux sens) | 19,20 [16,90 ; 21,80] | **9,83** [9,22 ; 10,44] | 9,05 [8,38 ; 10,01] | **0,9595** [0,9572 ; 0,9618] |
| AA, Adamic-Adar | 24,20 [21,50 ; 26,80] | 9,05 [8,52 ; 9,65] | 9,47 [8,59 ; 10,52] | 0,9419 [0,9384 ; 0,9455] |
| RA, allocation de ressources | **28,40** [25,70 ; 31,30] | **10,65** [10,08 ; 11,23] | **12,16** [11,14 ; 13,36] | 0,9574 [0,9547 ; 0,9602] |
| CN, voisins communs | 23,70 [21,10 ; 26,30] | 8,87 [8,33 ; 9,45] | 9,16 [8,29 ; 10,18] | 0,9396 [0,9361 ; 0,9432] |
| PA, attachement préférentiel | 11,40 [9,60 ; 13,40] | 5,62 [5,19 ; 6,07] | 3,79 [3,45 ; 4,25] | 0,8897 [0,8840 ; 0,8951] |
| ST, tirage stratifié | 0,30 [0,00 ; 0,60] | 0,22 [0,14 ; 0,32] | 0,27 [0,26 ; 0,29] | 0,4975 [0,4868 ; 0,5082] |
| U, tirage uniforme | 0,30 [0,00 ; 0,70] | 0,25 [0,16 ; 0,36] | 0,27 [0,26 ; 0,29] | 0,4964 [0,4861 ; 0,5073] |
| S(A→C), sens unique (secondaire) | 18,20 [15,90 ; 20,60] | 7,98 [7,46 ; 8,56] | 6,52 [5,94 ; 7,34] | 0,9176 [0,9133 ; 0,9220] |
| S(C→A), sens unique (secondaire) | 9,80 [7,90 ; 11,60] | 4,11 [3,69 ; 4,49] | 2,67 [2,37 ; 3,07] | 0,8768 [0,8720 ; 0,8816] |

Écarts de précision à 10 000, appariés (points ; dans les deux sens) : S − ST **+9,61** [+8,98 ; +10,23] ;
S − RA **−0,82** [−1,43 ; −0,25] ; S − AA +0,78 [+0,12 ; +1,42] ; S − CN +0,96 [+0,30 ; +1,59] ; S − PA +4,21
[+3,69 ; +4,76].

Lecture, sans changer les décisions :
- S bat Adamic-Adar, voisins communs et attachement préférentiel à 10 000, de moins d'un point face aux deux premiers ;
  elle perd contre l'allocation de ressources à 10 000, et plus nettement en tête de liste (précision à 1 000 :
  19,2 % contre 28,4 %, la plus faible des quatre méthodes de cooccurrence) et en précision moyenne (9,05 % contre 12,16 %).
- Seule mesure où S devance RA : l'aire sous la courbe (0,9595 contre 0,9574), intervalles qui se recouvrent. S
  ordonne un peu mieux le gros de la liste, moins bien la tête — or c'est la tête que mesure la décision.
- Le choix préenregistré de la moyenne des deux sens n'a pas desservi S : chacun des deux sens seuls fait pire
  (7,98 % et 4,11 %).
- L'avantage de toutes les méthodes sur ST ne tient pas au choix des strates : la précision qu'aurait la tête de liste
  de chaque méthode avec sa seule composition par strates est de 0,23 à 0,30 % (audit n° 2, non préenregistré).

Taux de base par paire de champs (Wilson ; aucune strate ne touche « stat », qui n'a aucun terme candidat) :

| strate | paires candidates N_s | paires tirées | taux de base (%) |
|---|---|---|---|
| math – cs | 2 469 001 | 17 489 | 0,36 [0,28 ; 0,46] |
| math – physique | 112 832 560 | 799 241 | 0,17 [0,16 ; 0,18] |
| math – q-bio | 258 547 | 1 831 | 0,11 [0,03 ; 0,40] |
| math – q-fin | 6 834 | 49 | 0,00 [0,00 ; 7,27] |
| cs – physique | 23 113 888 | 163 726 | 0,76 [0,72 ; 0,80] |
| cs – q-bio | 52 064 | 369 | 0,00 [0,00 ; 1,03] |
| cs – q-fin | 1 436 | 10 | 0,00 [0,00 ; 27,75] |
| physique – q-bio | 2 374 883 | 16 822 | 0,47 [0,38 ; 0,58] |
| physique – q-fin | 65 247 | 462 | 0,00 [0,00 ; 0,82] |
| q-bio – q-fin | 150 | 1 | 0,00 [0,00 ; 79,35] |
| les cinq strates avec stat | 0 | 0 | — |

Strate « dominée par les termes passe-partout » (plus de la moitié de la masse de S par les 432 termes du 1 % le plus
fréquent) : **494 paires, une seule positive**. Précision à 1 000 et à 10 000 non définies (strate plus petite que k,
règle préenregistrée) ; la précision moyenne et l'aire y reposent sur une seule positive : aucune lecture possible.

## Contrôles

**(a) Issues permutées.** 20 permutations par découpage ; toutes les méthodes restent au taux de base (critère :
moins de 4 erreurs-types). Principal : précision à 10 000 moyenne de 0,27 à 0,29 % pour un taux de base de 0,2752 %,
écarts de −0,61 à +1,43 erreur-type ; aire de 0,4965 à 0,5014, écart le plus grand −2,81 erreurs-types (S). Placebo :
écarts tous sous 1,9 erreur-type. Comme les écarts d'aire au découpage principal penchaient tous du même côté (−1,85 à
−2,81 pour les méthodes à score), je les ai audités (non préenregistré) : 200 permutations de plus, autre graine →
aire à −0,18 à −1,21 erreur-type, écart-type observé 0,0050 à 0,0051 contre 0,0055 en théorie ; précision à 10 000 à
−1,4 à −2,3 erreurs-types, même signe pour toutes. Sous permutation, l'espérance est exactement le taux de base et 0,5 ;
ces écarts de même signe viennent de permutations communes et de têtes de liste qui se recouvrent (fluctuation
corrélée, moins de 0,01 point en valeur absolue), pas d'une fuite.

**(b) Placebo 2003-2006 / 2007-2010** (chaîne entière refaite : 180 284 documents d'avant, 248 918 d'après, 19 975 termes,
1 000 000 de paires, taux de base 0,528 % [0,514 ; 0,542]). Précision à 10 000 : RA 16,17 % [15,38 ; 16,83] > S 13,67 %
[13,03 ; 14,43] > AA 12,65 % > CN 12,29 % > PA 8,75 % > U 0,55 % ≈ ST 0,54 %. **Même ordre qu'au découpage principal :
« stable »**, tau de Kendall = 1,0. Écarts : S − RA −2,50 [−3,24 ; −1,57] ; S − ST **+13,13** [+12,47 ; +13,83].
Au placebo, la règle D1 aurait **retenu** S ; elle la réfute au découpage principal. Le préenregistrement fait décider
le seul découpage principal ; ce basculement est une réserve sur le seuil, traitée plus bas.

**(c) Absence de fuite temporelle.**
- Essai synthétique avec la chaîne même du calcul réel (`code/essais_v1.py`, `resultats/essais-v1.json`) : documents
  d'après mélangés, retirés, ou bourrés des paires candidates → vocabulaire, champs, candidats, paires tirées et scores
  identiques au bit près, issues changées ; un document d'avant modifié → tout change ; un calculateur volontairement
  fuyant est pris par la garde ; calcul à deux processus identique au calcul à un processus.
- Données réelles (`resultats/scores-bilan-v1.json`) : matrices d'avant limitées à 2003-2010 (2003-2006 au placebo) ;
  les fréquences d'avant de la matrice sont égales à celles de la passe d'extraction ; 1 000 paires recalculées par une
  implémentation lente sur les seuls documents d'avant (écart relatif maximal 4,0e−15, 3,3e−15 au placebo) ; degrés et
  normalisations r exacts sur 300 termes ; aucune des 2 000 000 de paires tirées ne cooccurre avant.
- Chronologie : scores écrits et empreintés à 20:30:32 et 20:32:31 UTC ; issues calculées à partir de 20:33:11 UTC.

## Description du corpus et du tirage

- 999 260 lignes, 999 213 articles (37 identifiants en double réduits). Avant : 429 202 ; après : 570 011.
- Vocabulaire : 43 162 termes (dont 27 583 bigrammes) de fréquence documentaire 50 à 21 460 ; 48,8 termes de vocabulaire
  par document d'avant ; 2 688 668 termes distincts avant (risque de conflit d'empreinte borné par 2e−7 ; aucun conflit
  touchant le vocabulaire).
- Part des documents d'avant : physique 73,9 %, math 19,4 %, cs 4,9 %, q-bio 1,1 %, stat 0,44 %, q-fin 0,30 %.
- Termes candidats (spécifiques, fréquence 50 à 3 000) : physique 33 078, math 3 497, cs 722, q-bio 75, q-fin 2, stat 0.
  141 174 610 paires candidates ; tirage proportionnel → 80 % de paires math – physique, 16 % cs – physique.
- Toutes les paires tirées ont au moins un voisin commun (K > 0).

## Ce que le test ne dit pas

- **Des termes ne sont pas des concepts.** Les unigrammes et bigrammes de titres et de résumés mêlent synonymes,
  polysémies et mots de discours. Les têtes de liste le montrent : celle de S ressemble à des ponts de physique
  mathématique (« toric variety — witten », « hopf — supergroups », « projective curves — calabi yau ») ; celle de RA
  est faite de mots courants (« ball — consistently », « users — shifts », « resp — thought », « proofs — vice »), qui
  cooccurrent pourtant plus souvent ensuite. L'issue mesurée est la **cooccurrence lexicale future**, pas une découverte
  féconde. Cette impression vient de 15 exemples et ne sert pas à racheter S.
- **arXiv n'est pas toute la littérature** : physique surreprésentée (74 % des documents d'avant), statistique et finance
  quantitative presque absentes avant 2011, pas de biomédecine (le terrain d'origine de Swanson).
- **« Champs éloignés » se réduit ici, pour l'essentiel, à math – physique et cs – physique**, deux champs reliés par la
  physique mathématique. Le test ne dit rien des champs vraiment lointains.
- **Le régime « termes passe-partout » n'est pas testé** : la strate est vide en pratique (494 paires sur 1 000 000, une
  positive). Le +17 points des mondes synthétiques n'est donc ni confirmé ni réfuté.
- Précision à 10 000 sur un échantillon d'un million = précision du premier centile de la population (≈ 1,4 million de
  paires sur 141 millions). Ce n'est pas la précision des 10 000 meilleures paires de la population entière.
- Une seule fenêtre (2011-2016), un seul seuil d'issue (3 documents), une seule graine par tâche, un seul corpus.
- La précision à 10 000 seule décide. S a la meilleure aire mais une tête plus faible.
- S et RA choisissent des têtes presque disjointes (2 378 paires communes sur 10 000), avec des taux de réussite voisins
  (983 et 1 065 positives). Leur combinaison est une **question ouverte**, à préenregistrer ; elle n'est pas testée ici
  et rien ne s'en revendique.

## Points du brief que je crois mal posés (dits à part ; décisions inchangées)

1. **Spécificité non normalisée par la taille des champs.** Avec 74 % des documents d'avant en physique, un mot réparti
   au hasard a 74 % de ses documents en physique : il devient « spécifique » de la physique (« consistently »,
   « thought », « apparently »…). La statistique n'a aucun terme spécifique. Une spécificité relative à la part du champ
   serait plus fidèle à l'idée de « champs éloignés ».
2. **La strate « passe-partout » est vide par construction.** Le vocabulaire exclut les termes de plus de 5 % des
   documents (les vrais termes passe-partout). De plus, P(C|B) = n(B,C)/r(B) donne peu de masse aux intermédiaires
   fréquents : par le 1 % le plus fréquent passent 22 % de la masse de S en médiane, 38 % au 99e centile. Le motif
   principal du test (le +17 points) ne peut donc pas être éprouvé avec ces définitions.
3. **Le seuil de D1 est absolu alors que ST vaut le taux de base.** Le verdict dépend du taux de base : 9,61 points à
   0,28 % (réfutée) et 13,13 points à 0,53 % (placebo, retenue), pour un même ordre des méthodes. En relatif, S
   multiplie le taux de base par 36 (principal) et 26 (placebo). Un seuil relatif, ou calé sur le taux de base, voyagerait
   mieux. L'allocation de ressources, adoptée par D2, ne passerait pas non plus la barre de D1 (+10,43 points).
4. **Le sens de la marche n'était pas fixé.** Le préenregistrement a tranché pour la moyenne des deux sens, qui
   l'emporte sur chaque sens seul ; aucune décision n'en dépend.
5. **« Paires possibles de chaque strate » était ambigu.** Lu comme le nombre exact de paires candidates. Les paires
   cooccurrentes écartées font de 0 à 4,3 % des paires |T_f|·|T_g| selon la strate (2,5 % pour math – physique) :
   l'autre lecture aurait à peine changé l'allocation.

## Écarts au préenregistrement

Aucun sur les définitions, les seuils, les périodes, le vocabulaire ou les décisions. Ajouts **non préenregistrés**,
signalés comme tels, sans effet sur les décisions :
- `resultats/audit-v1.json` : 200 permutations de plus ; parts des groupes ; masse de S par le 1 % le plus fréquent ;
  recouvrement des têtes de liste ; fréquences des termes en tête.
- `resultats/audit-strates-v1.json` : composition par strates des 10 000 premiers de chaque méthode.

## Sources (chemins sous `sortie/`, empreintes SHA-256)

| fichier | empreinte |
|---|---|
| `preenregistrement-retrodiction-v1.md` | `7a4868aa48cfff5eb48937b0a1a99647fc9968c44c1fe8a7bb8047629b3c91eb` |
| `resultats/synthese-v1.json` (D1, D2, stabilité) | `345e9a4e955f4f41baa24e4983379b0e46d12893f0bd62ab9cf4ed14c50d1ce8` |
| `resultats/issues-v1.json` (mesures, intervalles, permutations, strates) | `dd16d06e6feb59d85f38503cf4eba47fd9b134a0c13059664dd8e69fdc76373e` |
| `resultats/scores-bilan-v1.json` (corpus, vocabulaire, strates, contrôle de référence) | `54463b67fd7c13368b80b34d7926eab1feceeca95f11e4833c912217f4c0c371` |
| `resultats/essais-v1.json` (essais automatiques) | `b9c5b7cafb6e9dca0c2237877df58d358621ef6cb08097af83d714f3a94deb28` |
| `resultats/audit-v1.json` (non préenregistré) | `7f19db8caf136581f16f7b74cbedf14d69140dda2867ad8baf531ca8a387ac26` |
| `resultats/audit-strates-v1.json` (non préenregistré) | `e0700fbaf621e753b5f3a4ed0c6e2470bfffa681b47bb6c5e80535f3c1b4aa8b` |
| `resultats/scores-principal-v1.npz` (scores par paire) | `0850c7e33011fc89e94dd3f4cfd83a8ed8ee47e0ef8871035b5a6814bab92b0d` |
| `resultats/issues-principal-v1.npz` (issues par paire) | `31fbb60da3739cdbd7e7076f22c96c7af486baa9989afb202e5f6e481b1077ab` |
| `resultats/vocabulaire-principal-v1.npz` | `06c065948f0235711492cf58694d9687e50e326f9df20abf7ce781e2f237bff4` |
| `resultats/scores-placebo-v1.npz` | `173684c34fd58162a45f35f65b58393d345b9ab6f2313d1fbb3ff187412c2b49` |
| `resultats/issues-placebo-v1.npz` | `700db17558fc94406f68acf097f17308e32a1ea7a98ac0550dcddd04ff52525e` |
| `resultats/vocabulaire-placebo-v1.npz` | `c73f0c98e588ceb60907b4bd213be08d644b7ff4378bfe6672b33c9663be824d` |

Code (`code/`, chaque fichier a son compagnon `.sha256`) : `termes_v1.py`, `corpus_v1.py`, `chaine_v1.py`,
`mesures_v1.py`, `essais_v1.py`, `lancer_v1.py` (étapes `essais`, `scores`, `issues`, `synthese`), `tables_rapport_v1.py`,
`audit_v1.py`, `audit_strates_v1.py`. Empreintes, versions (Python 3.13.17, numpy 2.3.4, scipy 1.16.3, duckdb 1.4.1),
graines (`SeedSequence(20261026)`, clés d'engendrement par tâche) et heures sont consignées dans chaque fichier JSON et
dans `manifeste-v1.json`. Journaux : `travail/journal-*-v1.txt`. Matrices d'après intermédiaires : `travail/apres-*-v1.npz`.

Horodatage : écrit le 2026-10-26 20:52:23 UTC (heure lue sur `date -u` dans la commande qui écrit cette ligne).
