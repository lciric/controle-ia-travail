# Contrôle du différentiel v2 → v3 — fiche des quatre décisions sur l'orchestrateur v68 — v1

- Auteur : le même contre-lecteur, modèle O (règle de l'allègement), auteur de la contre-lecture de la v1 (`af90dae4…`) et de la vérification de la v2 (`verification-fiche-quatre-decisions-orchestrateur-v68-v2-v1.md`, `349952832f1fe3dd99039915fc4fb88fd5c015d92fcc67b868211524fa04f282`). Je n'ai écrit ni la v3, ni son rapport, ni son mandat. 2026-11-19, vers 23:53Z à 23:58Z (`date -u` : 23:55:11Z).
- Lecture seule. `git fetch origin lot/compte-organisme-v1` puis `git fetch origin main`. La branche est à `7b16f957a`, qui descend de `03f961c7`, et l'arbre est propre. Je n'ai lancé aucun programme, appelé aucun fournisseur, rien écrit dans le dépôt, passé aucun code en ligne à un interpréteur, ni lancé aucune commande sur le dossier d'archives interdit. Aucun refus d'outil.

## Verdict

**Prête après corrections** : une seule correction, de mon fait. Mon texte V6 omettait la condition de R-3209, point 3. Tout le reste est conforme : V1 à V11 sont appliquées à la lettre, la tenue est juste, et rien d'autre ne change.

## 1. Pièces

| pièce | empreinte | état |
|---|---|---|
| fiche v3 | `bff07f805a284bba7cab6e62970bcde2fa10550d620555bc67e6ab1a67daeb7a` | conforme au compagnon ; lue par le différentiel et dans ses zones changées |
| différentiel v2 → v3 | `16ae420586b7458cf2693722428fe5422b5c514e502a1528a73809180144d992` | conforme. Son corps est égal à l'octet à un `diff -u` que j'ai refait entre la v2 et la v3 du dépôt (seul l'en-tête diffère, par les chemins et les heures) |
| remplacements (17) ; journal de l'outil | `18d6a0aa…` ; `d0ce65d1…` | conformes aux compagnons |
| rapport du rédacteur v3 | `dfeed022252408ef999b8e3a46826a514b17260b97a5322ae40566ca633e877c` | conforme ; lu en entier |
| mandat v3 | `127ea2228840b5d3004cac0e2b5a6ea46e9b18e2babc36745e3d904addd089b1` | conforme ; lu en entier |
| `main` à `5e7fc9fc6` : `registres/go.md`, `registres/decisions.md` | `ff9314ae…`, `68958908…` | égales à celles que cite la v3 ; R-3209 porte bien « tant que la correction n'est pas éprouvée » |

## 2. Les corrections V1 à V11

Le différentiel compte treize blocs en `diff` simple (six en `diff -u`, contexte fusionné). J'ai rapporté chacun à une correction ou à la tenue, et je n'ai trouvé aucun changement hors de ces zones.

| n° | appliquée | contrôle |
|---|---|---|
| V1 | verdict, point 3 | texte exact |
| V2 | phrase de la décision 2 | texte exact |
| V3 | enjeu de la décision 2, dernière phrase | texte exact |
| V4 | (a) de la décision 2 : « (7, 8, 9, 12, 20) » | texte exact |
| V5 | (c) de la décision 2, avantage | texte exact |
| V6 | « Ce qui manque » | texte exact ; la condition de R-3209 manque, voir le § 4 |
| V7 | verdict, point 4 | texte exact |
| V8 | décision 4, troisième raison | texte exact |
| V9 | décision 4, titre de (b) | texte exact |
| V10 | décision 4, défaut | texte exact |
| V11 | réserve 5 | texte exact |

**La tenue** comprend le titre, la ligne d'auteur, la ligne du mandat, deux remplacements dans la ligne des sources et une section « Différentiel v2 → v3 ». Les empreintes citées sont justes : version 2, vérification, mandat v3 et registres de `main` à `5e7fc9fc6`. Le statut est dit (« v3 non revérifiée »). Le tableau du différentiel en fin de fiche décrit fidèlement les changements. Les options recommandées, les confiances, le tableau des lignes et les réserves 1 à 4 et 6 sont inchangés.

La question est désormais posée à Lazar, au verdict (point 3) et dans la phrase de la décision 2, au format attendu. La décision 2 garde ses trois options, sa recommandation (a) à 0,5 et un défaut nul justifié.

## 3. Les écarts du rédacteur

1. **La nuance de R-3209, point 3, n'est pas reprise.** C'est mon erreur : la V6 que j'ai écrite résumait un mot de Lazar sans sa condition. La lettre dit : remplacé par un verdict précis « tant que la correction n'est pas éprouvée ». Sans cette condition, la fiche présente comme définitif un remplacement que Lazar a donné comme provisoire. Le rédacteur l'a vu, l'a déclaré et n'a pas dévié du texte exact, ce qui était correct. La règle de symétrie (R4) vaut aussi pour mes propres textes : à corriger (§ 4).
2. **L'en-tête garde « -55 à -93 ».** C'est acceptable : il dit ce que le rédacteur de la v2 a lu à `7d0b0ba9`. La v3 ajoute une phrase exacte sur ce qu'elle a relu à `5e7fc9fc6` (GO-94 à -96, R-3209). Les deux lectures sont datées et empreintées, et rien n'est faux. Ma remarque de la vérification v2 n'était pas une correction numérotée.
3. **Le verdict compte quatre points, plus que les « 1 à 3 lignes » de `CLAUDE.md`.** C'est acceptable pour cette pièce. Le format court vaut pour le message à Lazar, que la mère écrira, alors que la fiche porte quatre nœuds et une divergence. Les points 3 et 4 portent chacun une information que Lazar doit avoir avant de répondre. Les resserrer serait un choix de la mère, non une correction.

## 4. Correction demandée (texte exact ; « remplacer A par B », A copié de la v3, présent une seule fois)

C1. **« Ce qui manque encore », phrase sur R-3209.** Remplacer « (« identique », « portable », « dépendant de la donnée », « confiné ») dans la conception » par « (« identique », « portable », « dépendant de la donnée », « confiné ») « tant que la correction n'est pas éprouvée », dans la conception ».

Aucune autre correction.
