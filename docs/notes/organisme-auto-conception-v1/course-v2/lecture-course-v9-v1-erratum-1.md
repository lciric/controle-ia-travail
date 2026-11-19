# Erratum 1 de la lecture descriptive de la course d'auto-conception v9 de l'organisme d'idéation

- **Auteur** : relecteur neuf, Claude Fable 5.2, sur le mot de Lazar « go relis par fable » (GO-2026-11-19-54, R-3810) et le mandat de la mère (R-3814). Écrit le 2026-11-19, vers 12:59Z. Processeur seul, aucune dépense.
- **Pièce corrigée** : `lecture-course-v9-v1.md`, sha256 `0306adf74d321cfa933e047adff28324092787f870a2bf97bafd9d52bd5ffddb`. **La v1 n'est pas réécrite** (règle R12) : elle se lit désormais avec cet erratum, qui prime là où il parle.
- **Ce que l'erratum corrige** : une phrase fausse de l'en-tête ; la présentation de l'audit de symétrie (sens du mot « lot », nombre qui répond à la question, bloc de l'espèce Astra non relevé) ; trois phrases de la lecture des cartes et des nœuds.
- **Ce qu'il ne change pas** : la bonne fin (§ 1) ; aucun compte de la « Métrique » (§ 3) — le programme de comptes, rejoué sur le commit `8029ae7f`, rend les deux sorties à l'octet près (`85d8e8b8…`, `a9c90c34…`) ; la conclusion sur la case « originalité » (compatible avec le hasard) ; les regroupements du § 4, sauf deux phrases ; le § 5. Aucun choix de carte, aucune promotion, aucun verdict.
- **Source** : `docs/notes/relecture-fable-ecarts-qui-concoit-v1.md`, sha256 `0f7e3473c99d929e9b2545f075fd4e77a9b78081f12ee1b51d1fe29a3deb3283`, § 1.5, repris tel quel.

## Pièces d'appui (règle R6), dans ce dossier, chacune avec son compagnon

Programmes joués par `python3 -I -B` sur un arbre extrait du commit `8029ae7f` de `lot/compte-organisme-v1` (sortie de la course, sans `conservation-reponses-v1/` ni `.claude/projects/`). Ils ne lisent que des champs, des longueurs et des motifs ; aucune carte n'a été lue par le relecteur.

| ce que la pièce établit | programme | sortie |
|---|---|---|
| probabilités de l'audit : case désignée, au moins une case sur onze (200 000 permutations, graine `SeedSequence(2026111954)`), bloc par espèce, notables par juge et par espèce, longueurs | `lecture-course-v9-v1-erratum-1-verif-probabilites-v1.py` `39264eea8b09fd73781e069948d9a250e9cff1a3e69f3a260513380860073026` | `…-verif-probabilites-v1-sortie.txt` `3cea377a66ec93e7eb1fc694a652d7c880c0b104e5a87ffe97c4d3d03b135ee4` |
| marques de citation et de réserve par espèce | `lecture-course-v9-v1-erratum-1-verif-citations-par-espece-v1.py` `50ad93a57368de0c7940b8808d2758283816b6edaba4752ac4160aef64e4dea2` | `…-verif-citations-par-espece-v1-sortie.txt` `aaadd4c1822273ea8535f819a7fb6190afcd2ab165c5d26cd3706a117ebb84df` |
| identifiants et espèces cités au § 4 de la v1 | `lecture-course-v9-v1-erratum-1-verif-identifiants-v1.py` `4ce81dd684e1906b4bafc115751c7b8659559be8b1c546da24dd2f4fddcc9246` | `…-verif-identifiants-v1-sortie.txt` `d9360b317c78c014e09385197e006e0936abf04fde548e7f5adcbe3c20a9945e` |
| effectifs et notables par regroupement, carte non rangée | `lecture-course-v9-v1-erratum-1-verif-regroupements-v1.py` `ad28996c8509356c4e915c10718eee34c0eab00c16bf806546074137402b32ef` | `…-verif-regroupements-v1-sortie.txt` `550eaf80e2d10c8493b68af18eff1870ec9db95327bccb5e6c35faba8495af39` |

Les 414 et 322 chemins de la reprise 1 se recomptent par `git ls-tree -r --name-only 8029ae7f`, filtré sur `conservation-reponses-v1` et sur `.claude/projects`.

## Les six reprises

**Reprise 1 — en-tête, « Non lus ».**
- Avant : « Non lus : `conservation-reponses-v1/` et `.claude/projects/` (absents du commit), tout fichier « consigne-privee »… »
- Après : « Non lus : `conservation-reponses-v1/` et `.claude/projects/` (présents au commit `8029ae7f`, 414 et 322 chemins, non ouverts), tout fichier « consigne-privee »… »

**Reprise 2 — § 2, titre et deuxième puce.**
- Avant : « issue : **une case « trop propre », aucune « trop sale » ; rien d'artefactuel sur les champs** » et « **Par case du catalogue** (lecture plus stricte, onze cases) »
- Après : « issue : **une case et une espèce « trop propres », aucune « trop sale » ; la case est compatible avec le hasard, l'espèce ne l'est pas et s'explique par un mécanisme de l'item qui trie** » et « **Par case du catalogue** (c'est le « lot » du texte : onze cases) »

**Reprise 3 — § 2, puce « Audit déclenché », la probabilité.**
- Avant : « probabilité qu'une case de 6 cartes tirées sans remise parmi 94 (67 notables) soit entièrement notable 0,1226 ; espérance du nombre de cases entièrement notables sous répartition au hasard 0,617 sur 11 »
- Après : « probabilité qu'une case de 6 désignée d'avance soit entièrement notable 0,1226 ; la case ayant été désignée parce qu'elle l'est, la grandeur qui compte est la probabilité qu'au moins une des onze cases le soit : 0,50 sous échange libre des notables, 0,40 sous échange à l'intérieur de chaque espèce (200 000 permutations, relecture par Fable) ; espérance 0,617 sur 11 »

**Reprise 4 — § 2, puce ajoutée après « Par case du catalogue ».**
- Avant : (rien)
- Après : « **Par espèce** (seconde marge de la « Métrique », non découpée par l'audit d'origine ; ajoutée par la relecture de Fable, après la lecture des cartes par l'agent, donc hors de l'ordre du texte) : l'espèce Astra est **trop propre** (20 cartes, toutes à passeport, tous items vrais chez les deux juges, aucune redite) ; probabilité d'un bloc de 20 désigné tout notable 4,3 × 10⁻⁴ ; aucune espèce trop sale. Mêmes contrôles de champs : rien d'anormal. Compte par programme, sans lecture : aucune des 20 cartes d'Astra ne porte de marque de citation d'un travail publié (« et al. », « arXiv », année), contre 20 sur 21 pour Argon, 15 sur 16 pour Carbon, 9 sur 15 pour Fable, 11 sur 22 pour Opus ; l'item `reserves_tenues`, qui porte le tri, n'a rien à y sanctionner. « Notable » mesure en bonne part l'absence de citation : aucune comparaison d'espèces n'en est tirée, dans aucun sens. »

**Reprise 5 — § 4, tête et regroupements 7 et 13.**
- Avant : « une carte peut relever de plusieurs. »
- Après : « chaque carte est rangée une seule fois ; les effectifs sont exacts ; 93 cartes sur 94 sont rangées, la carte `f9a517d00f493` (Carbon, case « mémoire ») ne l'est pas dans cette v1. »
- Avant : « C'est le regroupement le plus large, et le moins notable (plusieurs cartes reprennent « battre le meilleur de N à budget égal » comme critère, voir § 6). »
- Après : « C'est le regroupement le plus large (plusieurs cartes reprennent « battre le meilleur de N à budget égal » comme critère, voir § 6). »

**Reprise 6 — § 6, nœuds 3 et 7.**
- Avant (nœud 3) : « Pour une course suivante : soit la consigne du proposeur dit que ces citations portent « non vérifié », soit le juge les accepte. Rien n'est à changer pour cette course. »
- Après : « Question remise à qui concevra la consigne d'une course suivante (règle « qui conçoit ») ; aucune option n'est proposée ici. Rien n'est à changer pour cette course. »
- Avant (nœud 7) : « **Réserve R4** sur la case « originalité », entièrement notable : consignée, compatible avec le hasard (probabilité 0,12) ; aucune suite proposée. »
- Après : « **Réserves R4** : la case « originalité », entièrement notable, compatible avec le hasard (une case au moins sur onze : 0,40 à 0,50) ; l'espèce Astra, entièrement notable, non compatible avec le hasard, expliquée sur les champs par l'absence de toute citation. L'ordre « audit avant toute lecture des cartes » est déclaré par l'agent et n'est daté par aucun commit séparé. Aucune suite proposée ; « notable » ne sert à comparer ni des espèces ni des regroupements. »

## Constat sur l'espèce Astra — constat fait après coup, non une épreuve préenregistrée

Ce constat a été conçu et calculé par le relecteur après qu'il a vu les marges par espèce, et après la lecture des cartes par l'agent d'origine. Il n'est donc pas dans l'ordre du texte (« avant toute lecture des cartes ») et ne vaut pas épreuve. Les définitions ont été fixées avant l'exécution du programme : marque de citation = « et al. », « arXiv » ou une année de 1900 à 2099 en mot entier ; marque de réserve = « non vérifi… ».

1. **Le bloc.** Astra : 20 cartes, 20 à passeport, 20 à tous items vrais chez les deux juges, aucune redite. C'est la définition de « trop propre » du texte, appliquée à la seconde marge de la « Métrique » (« par lot et par espèce »), que l'audit d'origine n'avait pas découpée.
2. **Le hasard ne l'explique pas.** Sous échange libre des 67 notables entre les 94 cartes, la probabilité qu'un bloc de 20 désigné soit tout notable est C(67,20)/C(94,20) = 4,3 × 10⁻⁴.
3. **Les champs montrent un mécanisme.**

| espèce | cartes | cartes avec une marque de citation | cartes notables |
|---|---|---|---|
| Argon | 21 | 20 | 12 |
| Astra | 20 | **0** | **20** |
| Carbon | 16 | 15 | 13 |
| Fable | 15 | 9 | 11 |
| Opus | 22 | 11 | 11 |

   Toutes espèces confondues : cartes sans marque de citation, 33 notables sur 39 ; cartes avec, 34 sur 55. L'item qui porte le tri, `reserves_tenues`, sanctionne un travail publié cité sans « non vérifié » ; les cartes d'Astra n'en citent aucun ; l'item n'a rien à y mordre.
4. **Contrôles de champs, les mêmes que pour la case** : aucune note vide ; longueurs des notes des juges dans l'étendue des autres espèces ; cartes d'Astra les plus courtes (médiane 3 997 signes, contre 4 517 à 5 760). Aucun juge n'est de la famille d'Astra ; le juge Opus est le plus sévère pour les cartes d'Opus (11 notables sur 22).
5. **Ce que cela dit, et ne dit pas.** « Notable » mesure en bonne part l'absence de citation d'un travail publié. Cela renforce la limite déjà écrite au § 5 de la v1 (les juges n'ont éprouvé qu'un plancher de lecture de forme) et interdit toute comparaison d'espèces ou de regroupements sur ce compte. Cela ne dit rien de la valeur des cartes d'Astra, dans aucun sens, et ne change aucun compte de la « Métrique ».
6. **Limites du constat.** Les marques sont des motifs de texte : une année peut ne pas être une citation, un travail peut être cité sans année. Le lien entre absence de citation et item vrai est une association sur 94 cartes, non une cause établie. Les critères de choix des cartes (`criteres-choix-cartes-v9-v1.md`) écartent déjà le verdict des juges et l'espèce : ce constat n'y change rien.
