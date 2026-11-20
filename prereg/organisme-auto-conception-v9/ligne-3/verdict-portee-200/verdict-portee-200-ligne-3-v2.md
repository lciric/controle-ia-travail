# Verdict de la mesure « portée à 200 » de la ligne 3 (votes effectifs des juges) — v2

Pièce de classe A, écrite le 2026-11-20 (11:51Z à l'heure relevée) par l'agent qui prononce (règle R13), agent neuf : je n'ai écrit ni le texte de la ligne 3, ni un additif, ni le code, ni le verdict de l'étage 1 ou sa contre-lecture, ni le contrôle du manifeste, et je n'ai pas exécuté la mesure. Mandat : `mandat-verdict-portee-200-v1.md` (`7a1d61fcdf7b88b082b855f09c8bf397f52d3e7f8ea406f201d4b8c3189a9e9f`, égal à son compagnon). À contre-lire par un agent neuf d'un autre modèle, puis à sceller par la mère. **Aucune dépense avant ce scellement.**

Ordre suivi, celui du mandat : faute du banc sans regarder aucune puissance ; puis les comptes ; puis l'audit de symétrie, écrit ici avant la section du verdict ; puis la comparaison à l'aide du code ; puis le verdict.

## Pièces lues et empreintes

Toutes vérifiées par `env -C DOSSIER sha256sum -c F.sha256` (« OK »), sauf mention. R = `/home/user/controle-ia-travail/`. L3 = `R/docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-3-votes-effectifs-juges/`.

| pièce | sha256 | lecture |
|---|---|---|
| additif 3 v3 scellé, `R/prereg/organisme-auto-conception-v9/additif-3-preenregistrement-ligne-3-portee-200-v3.md` | `71b7a876398cdcc133f006c01ff7eb644e8f2c69be79e90be50088bd26492807` | en entier |
| additif 5 v2 scellé (code), même dossier | `581e97e5fb6d390378ce94f32f0057b55afa77ce1831d480f4b317c1c0eaa34c` | en entier |
| texte de la ligne 3 v7 scellé, même dossier | `4e3680d9915ef6e2fa33010fc9b7b2ef5575d74e58e982bfabdbdbcc3e99d5a0` | l. 175 à 244, l. 330 à 347 |
| résultat de la mesure, `L3/execution-portee-200-v1/mesure/resultat-portee-200-ligne-3-v1.json` | `afcb453acbb7dd883f040ce6e4b11cd83d2f86facf17a976621249ab31d2d174` | par mes programmes |
| manifeste de la mesure, même dossier | `da6a9300fb56754e8dd8baad243ab5f5fdab87a51d7fa2ccf08ab8bf51ccfbbd` | lignes `n`, `python`, `numpy`, `executable` |
| manifeste du chronométrage, `L3/execution-portee-200-v1/chronometrage/` | `9819b671c9e495cbb2252f3a56860b4dcdb1351b41b4f42403e8f73b92fe02e6` | empreinte seule |
| compte rendu de l'exécutant, `L3/execution-portee-200-v1/compte-rendu-execution-portee-200-v1.md` | `c0fd3ddc1470514a9bcbff107bf311074b8b7ceded09f4113be850856846a43c` | en entier |
| contrôle du manifeste par la mère, `L3/controle-manifeste-portee-200-par-la-mere-v1.md` | `0dcd2dc72ff0f1db2bce7609a943c45a9848e30d3150329472c873a251d272c4` | en entier |
| verdict de l'étage 1 v3 scellé, `R/prereg/organisme-auto-conception-v9/ligne-3/verdict-etage-1/verdict-etage-1-ligne-3-v3.md` | `1628b4d76d126c1cff9de803a063be0c5a5fc061bc530d5619fd088927d799f3` | l. 1 à 26 ; lignes rendues par recherche bornée (« .json », « 0,160 ») |
| résultat de l'étage 1, `resultat-etage-1-ligne-3-v3.json` (chemin tiré du verdict ; voir écart 2) | `eb7a673bc9612458f4c86cf817ef60e58c8118772934c52fbdba18cc4f3c60ce`, égal à celui du verdict | par mes programmes, section `monde_de_puissance` |
| manifeste de l'étage 1, `manifeste-etage-1-ligne-3-v3.json` (même voie) | `6c64c32c1d0bf7257e5b00277051de26dcedffec6fb0193066164cda9053eb92`, égal à celui du verdict | lignes `n`, `python`, `numpy`, `executable` |
| banc v4, `L3/code-portee-200-v4/banc_juges_scriptes_ligne_3_v4.py` | `79865552…` (additif 5) | parties : `classes`, `indices_moities`, constantes du monde de puissance, `holm` à `cellule_puissance`, `enumerer_cellules_puissance`, `puissance_qui_decide`, `comptes_gagnes`, `criteres_portee_200`, `executer_portee_200` |

## 1. Faute du banc (additif 3, § 6), contrôlée avant toute puissance

Programme `faute_du_banc_portee_200_v1.py`, qui ne lit, n'imprime ni n'écrit aucune puissance ni aucun compte gagné ; sortie `sortie-faute-du-banc-portee-200-v1.json`. Il recalcule lui-même, par ses propres formules et sa propre bissection, `d`, l'écart vrai et la faisabilité de chaque cellule.

| contrôle | attendu | constaté |
|---|---|---|
| nombre de cellules | 210 | 210 ; ordre égal à l'énumération gelée (comparaison, écart, loi, ρ, ρ′), recalculée par moi ; de même pour l'étage 1 |
| répliques par cellule faisable | 2 000 | 2 000 dans les 49 cellules faisables (tous écarts) |
| mondes faisables à l'écart de 0,10 | les treize du § 1, point 5, et eux seuls | treize : unanimité loi 1 ρ = 0 ; 0,15 ; 0,3 ; 0,45 et loi 3 ρ = 0 ; 0,15 ; juge seul loi 1 ρ = 0 ; 0,15 et loi 3 ρ = 0 ; bras R ρ = 0, ρ′ = 0,5 ; 0,9 sous les lois 1 et 3. Comptes (4, 2 ; 2, 1 ; 2, 2) égaux au § 1. Ma faisabilité recalculée : aucun désaccord sur les 210 cellules |
| écart vrai par formule, cellules faisables | égal à l'écart visé à 1e-9 près | plus grand écart 4,2e-17 (champ du résultat) ; 4,2e-17 (mon recalcul) ; mon `d` à 5,6e-17 au plus de celui du résultat |
| a = 0,20 + d, b = 0,20 − d | exact | exact dans chaque cellule faisable |
| `d`, a, b (et faisabilité) égaux à l'étage 1, cellule par cellule | égalité | 372 valeurs comparées, toutes égales à l'octet |

**Aucun manque : pas de faute du banc. L'issue C n'est pas prononcée.**

Autres constats, hors de la liste du § 6 : le manifeste porte n = 200 ; la mesure et l'étage 1 ont tourné sous le même interpréteur (`/usr/local/bin/python3`, Python 3.13.18) et le même numpy (2.5.3), relus sur les deux manifestes (additif 5, § 5, point 3). Le verdict scellé de l'étage 1 dit, l. 11, que la tolérance de l'estimateur tient à n = 200 (additif 3, § 4.2, ligne de l. 233).

## 2. Audit de symétrie (règle R4), écrit avant le prononcé

**Déclencheurs du § 6**, lus sur les comptes (programme `comptes_portee_200_v1.py`, sortie `sortie-comptes-portee-200-v1.json`) :

| déclencheur | valeur | joue ? |
|---|---|---|
| puissance qui décide à 200 sous celle de 100 | 0,3505 contre 0,160 (étage 1 : 320 sur 2 000, unanimité, loi 3, ρ = 0 ; égal au verdict scellé, l. 116) | non |
| au-dessus de 0,90 | 0,3505 | non |
| une cellule faisable à 0 ou 1 exactement | trois cellules faisables à l'écart de 0,05 (rangs 0, 2, 4 : monde de l'unanimité, loi 1, ρ = 0 ; 0,3 ; 0,6) rendent 0 sur 2 000 **pour la comparaison au bras R**, qui n'est pas la comparaison plantée de ces cellules ; aucune comparaison plantée n'est à 0 ou 1 | **oui, à la lettre** |
| hors de l'intervalle prédit (sous 0,30, ou 0,50 et plus) | 0,3505 | non |

Le texte du § 6 dit « une cellule faisable rend une puissance de 0 ou de 1 exactement », sans restreindre à la comparaison plantée. Je le lis à la lettre : l'audit part, entier. (Lecture déclarée, écart 5.)

**Les cinq relectures** (programme `audit_symetrie_portee_200_v1.py`, sortie `sortie-audit-symetrie-portee-200-v1.json`) :

1. **Moitié « lecture » de 50 bons et 50 mauvais.** Le manifeste porte n = 200. Dans le code, `cellule_puissance` prend `n_c = n // 2` = 100 par classe ; `classes(100)` rend 100 bons puis 100 mauvais ; `indices_moities(100)` rend l'étalonnage = 50 bons et 50 mauvais, la lecture = 50 bons et 50 mauvais. Tenu.
2. **Test de l. 179.** Dans le code : valeur de probabilité unilatérale (1 + nombre de tirages où l'écart, bras de comparaison moins agrégation étalonnée, est ≤ 0) / (2 000 + 1) ; Holm sur les quatre colonnes au niveau 0,05 (`NIVEAU_HOLM` = 0,05) ; gagnée si rejetée **et** écart observé ≥ 0,05 (`MARGE_COMPARAISON` = 0,05). Hors de son monde, le bras R est joué à ρ′ = 0 (règle B). Tenu.
3. **Règle choisie par le bras C et replis.** Rapportés dans les 49 cellules faisables ; **aucun repli** aux poids égaux (0 partout). À l'écart de 0,10, « au moins un » est la règle la plus choisie dans chacune des treize cellules (de 1 228 à 1 959 sur 2 000), le reste étant « un juge seul » (unanimité choisie une fois au plus). Plausible : c'est la règle du bras C en population ; l'erreur d'estimation des poids sur 50 par classe fait choisir un juge seul dans le reste. À l'écart de 0,05, dans le monde de l'unanimité (neuf cellules faisables, d de 0,042 à 0,167), « au moins un » n'est choisi qu'environ une fois sur trois aux sept cellules où d vaut 0,076 au plus (de 650 à 768 sur 2 000), puis 939 fois à d = 0,104 (rang 4) et 1 313 fois à d = 0,167 (rang 5) ; aux rangs 0 et 7, un juge seul l'est un peu plus souvent (670 et 686 contre 650 et 660) : d petit, deux juges presque symétriques, poids bruités. Ces cellules ne décident rien. Cela explique aussi que l'unanimité soit la comparaison la plus faible : à 0,10, l'écart observé moyen contre l'unanimité vaut 0,080 dans la cellule qui décide, sous l'écart vrai de 0,10, parce que le bras C n'y choisit « au moins un » que 1 233 fois sur 2 000.
4. **Ordre des cellules.** Égal à l'énumération gelée, recalculée indépendamment (section 1), à 200 comme à l'étage 1. Tenu.
5. **Comparaison cellule par cellule avec 100.** 58 lignes comparées (49 cellules faisables ; comparaisons plantées, deux par cellule « juge seul ») : **aucune ne baisse.** Aux treize mondes de l'écart de 0,10, en répliques gagnées sur 2 000 (à 100 → à 200) : unanimité loi 1 : 330 → 701 ; 341 → 788 ; 450 → 979 ; 654 → 1 297 ; loi 3 : 320 → 724 ; 369 → 792 ; premier juge seul / second juge seul : loi 1 ρ = 0 : 937 → 1 649 / 890 → 1 626 ; ρ = 0,15 : 1 325 → 1 882 / 1 308 → 1 878 ; loi 3 ρ = 0 : 943 → 1 634 / 899 → 1 645 ; bras R : loi 1 ρ′ = 0,5 : 1 029 → 1 726 ; ρ′ = 0,9 : 952 → 1 706 ; loi 3 ρ′ = 0,5 : 1 008 → 1 689 ; ρ′ = 0,9 : 964 → 1 698.

**Les trois zéros, instruits.** Dans ces trois cellules, le bras R est joué à ρ′ = 0 (règle B) ; trois votes indépendants à la majorité y font mieux que « au moins un » : écart vrai, bras R moins « au moins un », par formule, de −0,068, −0,065 et −0,051 ; écart observé moyen contre le bras C de −0,084, −0,079 et −0,067. Une victoire exige un écart observé de +0,05 au moins : 0 sur 2 000 est attendu. Ce n'est pas une faute du banc.

**Conclusion de l'audit.** Aucune anomalie : moitié lue, test, ordre, règle du bras C et comparaison à 100 sont conformes ; les puissances montent toutes de 100 à 200, dans un rapport voisin de 2 aux cellules faibles, ce que le doublement de la moitié « lecture » laisse attendre ; les seuls 0 exacts sont expliqués par la formule. Rien n'est trop beau : la puissance qui décide tombe dans l'intervalle prédit, mais la prédiction était calée sur le 0,160 connu (additif 3, § 1 ; réserve 1 ci-dessous). L'audit, le même dans les deux sens, ne change aucun compte.

## 3. Application du § 3, par moi, aux comptes entiers

Programme `comptes_portee_200_v1.py` (il ne lit pas l'aide du code), sortie `sortie-comptes-portee-200-v1.json`. Chaque puissance du résultat est relue comme un compte entier k sur 2 000 (contrôle k / 2 000 égal à la puissance, exact).

Cellules faisables lues à l'écart de 0,10, lois 1 et 3 : unanimité 6 ; premier juge seul 3 ; second juge seul 3 ; bras R 4. Aucune comparaison sans cellule faisable.

| comparaison | plus bas compte sur 2 000 | puissance | cellule |
|---|---|---|---|
| contre l'unanimité | **701** | **0,3505** | loi 1, ρ = 0 (rang 14) |
| contre le premier juge seul | 1 634 | 0,8170 | loi 3, ρ = 0 (rang 63) |
| contre le second juge seul | 1 626 | 0,8130 | loi 1, ρ = 0 (rang 56) |
| contre le bras R (un juge, trois votes, majorité) | 1 689 | 0,8445 | loi 3, ρ = 0, ρ′ = 0,5 (rang 148) |

**Puissance qui décide : 0,3505**, soit **701 répliques gagnées sur 2 000**, contre l'unanimité, loi 1, ρ = 0 (ρ′ = 0), une seule cellule au minimum. 2 × 701 = 1 402 < 2 000 : **sous 0,5, strictement.** Pas « près du seuil » : 701 est hors de 956 à 1 044 (0,478 à 0,522). Chaque comparaison a au moins une cellule faisable. **Par la table du § 3 : issue B.**

## 4. Comparaison à l'aide du code (`criteres_mecaniques.puissance`)

Programme `comparer_aide_portee_200_v1.py`, sortie `sortie-comparaison-aide-portee-200-v1.json`. Dix-huit champs comparés : issue (B), puissance qui décide (0,3505), compte (701), répliques par cellule, cellule au minimum, minima par comparaison en compte et en puissance (quatre fois deux), cellules faisables lues par comparaison, comparaisons sans cellule faisable, « près du seuil » (faux), écart qui décide, et la lecture du banc v3 sur les mêmes cellules (0,3505, « descriptives avant la dépense »). **Aucun désaccord.** L'aide n'est pas le verdict (R13) : elle confirme ma lecture.

## 5. Verdict

**Issue B : les comparaisons d'agrégations sont descriptives à l'étage 2 à 200 témoins**, par la même règle que l. 240 du texte, déclarées par l'additif 3 scellé (§ 3).

- **Puissance qui décide : 0,3505** — contre l'unanimité, loi 1, ρ = 0 — **701 répliques gagnées sur 2 000**. Sous 0,5 strictement ; pas près du seuil.
- **Minima par comparaison** (écart de 0,10, lois 1 et 3) : unanimité 0,3505 (701) ; premier juge seul 0,8170 (1 634) ; second juge seul 0,8130 (1 626) ; bras R 0,8445 (1 689).
- **Prédiction du § 1** (« sous 0,5 : entre 0,30 et 0,50 ») : **tenue** (0,3505). Sa réfutation (0,5 ou plus) n'est pas atteinte. Réserve : la prédiction était calée sur le chiffre connu de l'étage 1.
- **Audit de symétrie** : déclenché à la lettre par trois puissances nulles du bras R hors de son monde (écart de 0,05) ; les cinq relectures sont tenues, aucune cellule ne baisse de 100 à 200, les zéros sont expliqués par la formule ; aucune anomalie.
- **Faute du banc** : aucune.
- **Ce que l'issue B fait de l'étage 2 à 200** (§ 3, colonne 3) : la clause de l. 343 s'applique. Les rangs 2 et 4 ne peuvent pas être atteints : **aucun « oui » n'est possible**. Le rang 3 garde son « non ». ρ′ − ρ « positif » pour les deux juges se rapporte comme une mesure. Le reste est non concluant. La mesure des votes effectifs et l'écart ρ′ − ρ restent lus selon leur table. Dans les deux issues, la taille de l'étage 2 reste 200 témoins (§ 3). **Ce verdict ne décide rien de la dépense** : elle relève de la ligne de Lazar et de l'ordre des gestes, après la contre-lecture et le scellement de ce verdict.

Ce verdict ne porte aucune revendication et ne tranche aucune carte.

## 6. Écarts et réserves

Écarts :

1. **Premier appel avant la lecture du mandat.** Pour vérifier l'empreinte du mandat, j'ai lancé une commande chaînée (`&&`) qui contenait aussi `ls -la` sur le dossier `additif-3-portee-200-v1/`, `git status --short` et `git log --oneline -3`. Le mandat interdit la liste et le chaînage ; je ne l'avais pas encore lu. Sortie : noms et tailles des fichiers de ce dossier, état et trois derniers commits ; aucune mesure. Ensuite, une commande simple par appel.
2. **Le résultat et le manifeste de l'étage 1 ne sont pas sur le disque de `main`.** Le chemin tiré du verdict (`E/etage-1/…`, E = `docs/notes/…/ligne-3-votes-effectifs-juges/execution-etage-1-v1/`) est absent (contrôle par `stat` sur le chemin, règle R11). Je les ai lus dans la branche distante `origin/lot/compte-organisme-v1`, au même chemin, par `git cat-file blob` redirigé vers mon bloc-notes ; leurs empreintes sont égales à celles du verdict scellé (`eb7a673b…`, `6c64c32c…`). Je n'ai pas vérifié leur compagnon dans cette branche.
3. **Une sortie de 4,6 Mo à l'écran.** Mon premier essai d'extraction (`git show … --output=…`) n'a pas écrit le fichier mais l'a imprimé à l'écran ; l'outil a rangé de lui-même cette sortie sous `/root/.claude/projects/…/tool-results/`. Je n'ai pas ouvert ce fichier. L'aperçu affiché ne montrait que le début de la section « alarme » et des cellules infaisables du monde de puissance de l'étage 1 : aucune valeur de la mesure à 200.
4. **Programmes et sorties** écrits et lancés dans mon bloc-notes (`…/scratchpad/verdict-portee-200/`), puis copiés à l'identique dans ce dossier, chacun avec son compagnon. Quatre programmes au lieu d'un, pour garder l'ordre du mandat (faute du banc sans puissance, comptes sans aide, audit, comparaison à l'aide).
5. **Lecture du déclencheur « 0 ou 1 exactement »** : prise à la lettre, sur toute comparaison d'une cellule faisable, non sur la seule comparaison plantée. Elle fait partir l'audit ; l'autre lecture ne l'aurait pas fait partir. Rien ne change au compte ni à l'issue.
6. J'ai lu une ligne du mandat de l'exécutant (nom de son compte rendu) et des parties du code v4 (liste en tête) qui ne sont pas dans « ce qui fait foi » : pour trouver le compte rendu, connaître les clés du résultat et faire les relectures de l'audit.
7. Recherches bornées à un seul fichier (outil de recherche), jamais sur un dossier.
8. **Versement par une autre session.** Avant que ce verdict soit écrit, le commit `f1b1f95c` (« Travaux en cours versés pour ne rien perdre »), que je n'ai pas fait, a versé mes quatre programmes, leurs quatre sorties et leurs compagnons ; `git status` ne les montre pas modifiés depuis : les octets versés sont ceux de la section 7. Seuls ce verdict et son compagnon restent non versés. Je n'ai fait aucun commit.

Réserves :

1. La prédiction tenue pèse peu : elle était calée sur 0,160 (additif 3, § 1, et sa réserve 3).
2. Le monde de puissance est choisi par nous (réserve 1 du texte ; additif 3, § 8, réserve 1).
3. Mon recalcul de `d`, de l'écart vrai et de la faisabilité reprend les formules du texte (l. 237) écrites par moi ; il est indépendant du code, non du texte.

## 7. Mes pièces

Dossier `L3/verdict-portee-200-v1/`. Chaque fichier a son compagnon `.sha256` (pris par `env -C DOSSIER sha256sum F`).

| fichier | sha256 |
|---|---|
| `faute_du_banc_portee_200_v1.py` | `bffd21380a5a0a8ffb4b63f0ab67732a06571985ead79d4efe2b1cd391972472` |
| `sortie-faute-du-banc-portee-200-v1.json` | `29f6d93c96f5bebd7b19ee5a029809593245cd72d751f633acf8d9bea4db65d4` |
| `comptes_portee_200_v1.py` | `5d2a71d4ac23eb8f2d477256acf146250af299c71156a113182e26d6d43154df` |
| `sortie-comptes-portee-200-v1.json` | `31e0847cf52d9030a06e0c0eef4fb9007d37e4d58e8d1a00ced5a268cfc1370a` |
| `audit_symetrie_portee_200_v1.py` | `2c1c73247b19d5b586996b80251d13a324576132d96180d984427b13246855ae` |
| `sortie-audit-symetrie-portee-200-v1.json` | `c4f3d3db79026c655ca618139dca406c76513a03a8933e0c5303f08a94c265f5` |
| `comparer_aide_portee_200_v1.py` | `4062efe7731fdc0c281e2ea4d1fa837374ceebc9d464b5cc955ceb490b94650b` |
| `sortie-comparaison-aide-portee-200-v1.json` | `9eddc658830b4a1798f82696864606376984ab75d637cbc9adeebc7fc449c771` |

Lancement de chacun : `python3 -B PROGRAMME ARGUMENTS` (arguments en tête de chaque programme ; le résultat de l'étage 1 est la copie du bloc-notes, écart 2). Aucune relance de la mesure, aucune graine, aucun seuil changé ; aucun commit, aucun réseau, aucune dépense ; rien sous `archives-reponses-modeles/`.

Agent qui prononce, modèle O.
