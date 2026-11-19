# Épreuve à blanc des critères de choix v2 sur la course v9 — lecteur O — v1

- **Écrit le 2026-11-19** (`date -u` : début de lecture des cartes 2026-11-19T13:57:59Z ; sélections scellées et poussées 2026-11-19T14:08:07Z ; cette note après 14:09Z). Lecteur neuf, modèle O, sur mandat de la mère (GO-2026-11-19-68). Hors ligne, processeur seul, aucune dépense, aucun appel de modèle.
- **Règle appliquée** : `docs/notes/organisme-auto-conception-v1/epreuves-v9/juge-selection/criteres-choix-cartes-v9-v2.md`, sha256 `4ae09b15e2816fcda0ba0ba008ca11b58906d7712351253d04f52214e9a629c1`, égal à son compagnon `.sha256` ; versée par le commit `14e9954d` (2026-11-19T13:53:31Z), qui précède toute lecture de carte de ce rejeu (première carte affichée à 13:57:59Z). Je n'ai écrit ni ces critères ni aucune carte.
- **Cartes** : `archives-reponses-modeles/auto-conception-course-v9-2026-11-19-v1/course-v9-sortie/sortie/generation-1/fiches.json`, sha256 `ba65c411f4e3062fba29d93b5a00fe6fee23b34ebdc64f1708a0cc49177c3481` (égal au compagnon) ; 94 cartes. Un programme a copié le seul champ `contenu` de chaque carte, avant toute lecture ; le champ `meta` (espèce, et tout ce qu'il porte) n'a été ni copié ni imprimé. Ordre de lecture : empreinte de l'identifiant, sans contenu.
- **Non lus** : aucun verdict de juge, aucun coffre, aucun classement, aucune espèce, ni le rejeu de l'autre lecteur. Ni `diag/`, ni `donnees/`, ni le dossier du bras d'attaque, ni la conservation des réponses, ni les journaux des relais.
- **Lus en plus, pour appliquer la lettre** : sur `main`, la liste « Ne plus écrire » de N-073 § 1, son § 2 (porte du meilleur de N), les listes « Ne pas écrire » des compléments 2 et 3, N-067 § 4 (composantes cédées du juge), pour X2 et X5 ; les critères v1 (`8881dbb2…`), § 2, pour les cinq questions et C5, que la v2 renvoie à leur lettre.
- **Sélections** : `docs/notes/organisme-auto-conception-v1/epreuves-v9/juge-selection/selections-rejeu-a-blanc-criteres-v2-lecteur-o-v1.json`, sha256 `8bd435b98f1b81abf3a4e201977b2b1bf9a72cbe464dfb9127243d1a93e0b7d3`, scellé et poussé par le commit `e487939e` **avant** toute lecture de `registres/go.md`. Il porte, pour chaque carte, voie, question écrite, trois notes et leur raison en une phrase, exclusions et réserves ; le rang, la sélection, le veto et le lot, en deux variantes.
- **Comparaison** : faite ensuite, sur `registres/go.md` de `main` (commit `0faf9bb3`, copie sha256 `0682f0aa8a102b9c76256878e8ab08dfd8bcc7dcff57e99cbd824f8c98752aa1`), lignes GO-2026-11-19-55, -56, -57, -59, -61, -63, identifiants seuls.
- **Programmes** (bloc-notes de la session, non versés ; empreintes) : extraction sans `meta` `7e6b6857…` ; affichage `9d09c9b5…` ; assemblage des § 2 à 9 `80373d2e…` ; veto `d55e54e7…` ; lectures par lot `80e3b1d8…`, `c2ae7794…`, `9002e294…`, `de827222…`, `f25c052a…`, `8eee7e88…`, `8fb57a1c…`, `15503df0…`, `faa649e5…`.

## 0. Verdict

1. **La règle v2, appliquée à la lettre par un lecteur, ne départage presque rien.** 90 cartes sur 94 ont 6 sur 6, les 4 autres 5 sur 6 ; aucune n'est sous le plancher ; aucune n'est éliminée. Le nombre visé (neuf, par défaut) est rempli par les places réservées par voie, la strate non couverte (§ 9, point 5) et surtout le tirage au sort (§ 9, point 7) : les neuf retenues sortent d'égalités de 66 à 90 cartes. La sélection recommandée est donc un tirage stratifié, non un jugement.
2. **Recoupement avec les 50 cartes gardées à la main par Lazar** (variante A) : les 50 sont au plancher, listées, aucune éliminée ; 3 seulement sont dans le nombre visé, 2 de plus par mon veto, 1 par le lot tiré au sort, soit 6 sur 50 proposées en premier ; les 44 autres sont « au plancher, hors du nombre visé ». La règle propose en premier 7 cartes que Lazar n'a pas gardées, dont une qu'il a nommément écartée (`fbac0bab50a65`, GO-2026-11-19-63).
3. **Ce que cela dit du mot de Lazar sur la sévérité** : sur cette lecture, la v2 n'est plus sévère pour personne — elle ne fait tomber aucune carte ; elle déplace le choix du plancher vers le nombre visé et le tirage. L'effet par espèce n'est pas mesurable par moi (espèce non lue) ; il revient au programme de la mère (§ 10).

## 1. Ce que j'ai fait, et les écarts à la lettre

- **Un seul lecteur.** Les § 2, 4, 5 et 9 supposent deux lectures assemblées par programme. J'ai assemblé ma seule lecture par le même programme : note d'une carte = mon total (0 à 6) au lieu de la somme des deux (0 à 12) ; « plus petit écart entre lecteurs » (§ 9, point 6) nul pour toutes ; aucune fusion appliquée (elle exige les deux lecteurs) ; aucun désaccord de lecteurs à lister.
- **Exclusions, deux variantes.** Une exclusion n'écarte que si les deux lecteurs la voient (§ 2). Variante **A**, la lettre pour un lecteur : mes exclusions ne font que des réserves, la carte est notée et concourt. Variante **B** : mes exclusions tenues pour communes. Les deux donnent ici **les mêmes neuf cartes et le même veto** ; seul le lot de la voie N diffère. A est la variante principale.
- **X6 inapplicable sans lire `meta`** : je ne sais pas quelles cartes l'aiguilleur a retenues ; toutes ont été lues. À trancher par la mère, par programme.
- **Nombre visé** : K = 9, défaut du § 5, aucun K ne m'ayant été donné.
- **Graine** (§ 8 et § 9, point 7) : `numpy.random.SeedSequence([entier de l'empreinte des critères, entier de l'empreinte sha256 de « auto-conception-course-v9-2026-11-19-v1 »])`, numpy 2.5.3 ; enfant 0 pour le départage, enfant 1 pour le lot. Entropie écrite au fichier des sélections. L'identifiant de course est le nom du dossier d'archive : choix de ma part, à fixer par la mère.
- **Veto** : V = 3 (deux titulaires, les lecteurs ; aucune liste de veto de juge scellée avant l'ouverture ne m'est connue, et je n'ouvre aucune sortie de juge). Le retrait des cartes de ma propre lignée (§ 7) exige de lire l'espèce : **non appliqué**, laissé au programme de la mère ; mes deux suppléantes sont écrites pour cela.
- **§ 6 (coût, collision) non rapporté** dans cette épreuve à blanc : il ne pèse sur rien, et chaque carte porte son propre champ de coût.
- **Masque d'espèce imparfait, à dire** : je reconnais au moins trois familles de style (cartes brèves « adoption adaptée, sans revendication d'inédit », tables booléennes, borne à 95 % ; cartes chargées de références « non vérifié » et des six lignes de N-073 § 2 ; cartes en « Pourquoi cela compte pour l'axe »), sans pouvoir rattacher aucune à une lignée nommée. Le masque n'empêche donc pas un lecteur de regrouper les cartes par auteur probable.

## 2. Lecture des critères, là où la lettre a demandé un choix

- **E = 2** exige un oracle programmé, un témoin sans le mécanisme à coût apparié **et** une base bon marché, et une règle où « oui » et « non » sont définis. Presque toutes les cartes de cette course les écrivent : c'est la forme imposée par la consigne de la course. Seule la carte 4 manque de base bon marché (E = 1).
- **D = 2** : j'ai lu « changer une décision de conception » comme la v1 l'écrit (garder, retirer ou régler un module). Une issue « non » qui fait ne pas ajouter le module compte donc. Lu ainsi, D vaut 2 partout.
- **Q, voie P, à la lettre des questions de la v1** : la question (a) est celle d'un registre des tentatives **hérité d'une course antérieure puis tenu**, comparé au même registre né vide et à aucun. Aucune carte ne la pose ainsi. Les cartes « archive réelle, factice, rien » (17, 20, 45, 74) répondent à la lettre de (c), « ce que la génération suivante lit de la sélection » ; je les y range, avec la mention « éclaire (a) de biais ». La voie P compte ainsi 46 cartes en (c), 5 en (b), 4 en (d), 7 en (e), aucune en (a).
- **X2** : la base « meilleur de N » est, dans 27 cartes, une condition parmi d'autres, l'épreuve se jugeant sans elle (témoin sans le mécanisme) : réserve « critère à réécrire, pratique à citer », aucune exclusion.
- **X1** : vu sur 3 cartes, où l'avis agrégé de juges modèles promeut ou trie l'accès aux tests de mort et où le critère de l'épreuve est cette décision même (9 `fa38f9faa24e0`, 12 `fafa0062508c9`, 63 `fefca0bd94064`). Vu sans exclure sur 4 cartes de juges croisés dont l'épreuve porte une mesure séparable contre l'oracle (19, 21, 50, 64). **Divergence avec Lazar** : GO-2026-11-19-63, point 1, garde 9 et 63 « avec cet avis seulement descriptif » ; j'ai jugé, avant de le lire, la mesure non séparable sans changer l'épreuve. C'est la variante B qui les écarte ; la variante A les garde au plancher.
- **X3, X4, X5** : aucun cas vu. La carte 81 réunit deux mécanismes publiés sans autre forme que leur réunion ; ils ne sont sur aucune liste de X5 : réserve seulement.
- **Fusions proposées** (même oracle, mêmes bras, même monde, si l'autre lecteur le dit) : {17, 20, 32, 45, 74} ; {27, 44, 60} ; {6, 33} ; {11, 66} ; {19, 64} ; {22, 82} ; {37, 77} ; {80, 91}. Fusions raisonnées (voisines, aucune carte retirée) : tests de mort par jumeau ou permutation {26, 38, 43, 84, 89} ; concordance d'exécutions {25, 54, 65, 71, 93} ; interprète de référence {49, 68, 76, 86} ; réentrée des éliminées {62, 67} ; portefeuilles {2, 10, 72} ; vidages {5, 47, 83 ; 81, 90} ; redite par prédictions {73 avec 27, 44, 60} ; expériences discriminantes {48, 79} ; dose et réducteur d'archive {52, 88} ; multiplicité {58 avec 6, 33}.

## 3. Résultats (variante A sauf mention)

**Nombre visé, neuf lignes** (rang global entre parenthèses ; toutes à 6 sur 6) :

| place | carte | voie | motif |
|---|---|---|---|
| 1 | 13 `f7219bb36cfcb` bras à retour permuté | I | place réservée (rang 3) |
| 2 | 40 `f6bb348e95955` recenser les idées par leur comportement | I | place réservée (rang 25) |
| 3 | 54 `f2033ad1cbe45` verdict sur k réimplémentations | P (c) | place réservée (rang 1) |
| 4 | 6 `fb45c8739b3d2` seuil d'e-valeur indexé sur la dépense amont | P (d) | place réservée (rang 4) |
| 5 | 69 `fbac0bab50a65` masquage contrefactuel | N | place réservée (rang 2) |
| 6 | 73 `f89c771e3ac68` dédupliquer les prédictions | N | place réservée (rang 10) |
| 7 | 64 `f6f8c8b855234` votes effectifs du collège | P (e) | au rang (rang 5) |
| 8 | 46 `f51c0935052f6` nul de rappel | P (b) | au rang (rang 6) |
| 9 | 15 `fa312929593cf` mémoire négative par seul verdict de mort | P (c) | au rang (rang 7) |

Comptes : I 2, P 5 (c 2, b 1, d 1, e 1), N 2. Les neuf sont « à égalité, départagées par tirage » (égalités de 66 à 90 cartes) ; les rangs 2 à 6 ont aussi été poussés par la strate non couverte. **À égalité stricte avec la dernière retenue et perdantes au tirage** : 81 lignes (78 en variante B), en tête 81 `fdafe4598caad` (rang 8) puis 45 `fed7a993d9671` (rang 9).

**Lignes au plancher hors du nombre visé** : les 85 autres (82 en B), listées au tableau du § 5 avec leur rang.

**Veto du lecteur O** (liste ordonnée, scellée avec les sélections) :

| ordre | carte | issue prédite pour l'oracle | décision visée | lignée reconnue ? |
|---|---|---|---|---|
| 1 | 66 `f76714f1ddda4` porte séquentielle sur chaque auto-modification | la porte accepte moins de modifications surajustées plantées que la gloutonne et que le hasard sur la famille jamais vue, et rejette une part non majoritaire des bonnes | toute modification de l'organisme passe la porte ; sinon organisme figé plutôt que gloutonne | non |
| 2 | 45 `fed7a993d9671` héritage lu contre placebo | A − B nul à ρ = 0 ; croissant en ρ au quart du budget, resserré sans s'annuler à l'échéance | brancher ou non la lecture de la sélection, et jusqu'à quel point du budget | non |
| 3 | 7 `f562951db6c70` témoins jumeaux contre l'a priori | taux sur variantes contraires nettement sous le taux global, écart né chez les proposeurs | remplacer la moitié des témoins par des jumeaux ; rapporter les mesures sur variantes contraires | non |
| suppléante 1 | 24 `f4250eb75fbba` nul empilé | moins de fausses promotions de mélanges convexes, rappel au-dessus de 0,85 fois le témoin | remplacer la mise en commun du nul par l'empilement | non |
| suppléante 2 | 80 `f6e7646851ba5` rejeu d'inertie | rappel 1 et aucun faux inerte en classe A ; la couverture de code se trompe | étape protégée de rejeu d'inertie avant chaque version | non |

**Lot tiré au sort** (§ 8 ; vivier A : I 10, P 56, N 16) : I 36 `f2e3582b5fa97` ; P 90 `f17603c39bc32` ; N 27 `fd31770b6907d` (variante B : N 48 `fd9bbc7b19deb`).

**Espèce par liste (§ 10)** : non calculée, espèce non lue ; à faire par le programme de la mère sur le fichier des sélections.

## 4. Comparaison avec les cartes gardées par Lazar

Cartes gardées (identifiants des lignes de `registres/go.md`, sur `main`) : GO-55, 5 ; GO-56, 6 ; GO-57, 12 ; GO-59, 10 ; GO-61, 13 ; GO-63, 7 gardées (point 1 : 2 ; point 2 : 5), et 4 nommées non gardées. Trois cartes paraissent dans deux lignes : **50 cartes gardées**.

- **Auraient été gardées par les critères v2 (non éliminées)** : les 50 en variante A, toutes au plancher ; 48 en variante B (9 `fa38f9faa24e0` et 63 `fefca0bd94064` tombent par X1, si l'autre lecteur le voit aussi).
- **Proposées en premier** (nombre visé, veto, lot) : 6 sur 50 en A — dans le nombre visé 6 `fb45c8739b3d2`, 40 `f6bb348e95955`, 73 `f89c771e3ac68` ; par veto 66 `f76714f1ddda4`, 7 `f562951db6c70` ; par le lot 90 `f17603c39bc32`. En B, 7 sur 50 (le lot de la voie N tombe sur 48 `fd9bbc7b19deb`).
- **Non proposées en premier, mais au plancher et listées** : les 44 autres (43 en B) — 23, 3, 34, 92, 58, 79, 35, 37, 59, 14, 41, 24, 2, 18, 75, 55, 8, 77, 80, 85, 72, 26, 82, 67, 39, 42, 70, 9, 50, 28, 91, 57, 4, 16, 49, 48, 81, 10, 51, 87, 63, 11, 29, 61. Parmi elles, quatre des cinq lignes que Lazar a mises en tête (GO-55 : 58, 57, 50, 67) ; seule 73 est dans le nombre visé.
- **Gardées en plus par les critères v2** : dans le nombre visé, 54 `f2033ad1cbe45`, 46 `f51c0935052f6`, 64 `f6f8c8b855234`, 13 `f7219bb36cfcb`, 15 `fa312929593cf`, et 69 `fbac0bab50a65`, que Lazar a nommément écartée (GO-63, point 2) ; par veto 45 `fed7a993d9671` ; par le lot 36 `f2e3582b5fa97` et, en A, 27 `fd31770b6907d`. Au plancher, hors de ce qui est proposé en premier, 35 autres cartes non gardées par Lazar (35 aussi en B), dont les trois autres qu'il a écartées (5 `f4a47f030c829`, 22 `f98b6974fb1dd`, 83 `fcf27198b7462`).
- **Notes des cartes gardées par Lazar** : 47 à 6, 3 à 5 (4, 34, 87) ; les quatre cartes qu'il a écartées ont 6. La note ne sépare pas ce que Lazar a gardé de ce qu'il a écarté.
- **Lecture** : l'accord entre la règle et Lazar n'est ni bon ni mauvais, il est au niveau du hasard : 9 tirées parmi 90 cartes à égalité, dont 50 gardées, donnent près de 5 gardées en moyenne ; j'en trouve 3. Ce rejeu ne dit pas si la règle choisit bien ; il dit qu'elle ne choisit pas.

## 5. Tableau par carte

Raisons des notes, question écrite et réserves : au fichier des sélections, carte par carte. « Lazar » : colonne ajoutée après le scellement.

| n | carte | voie | E | Q | D | total | rang (A) | sélection (A) | veto | lot | exclusion vue | Lazar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `f20fbf8b6d797` | P (c) | 2 | 2 | 2 | 6 | 72 | non (au plancher, hors du nombre visé) |  |  |  |  |
| 2 | `f4b85ff3c1033` | P (c) | 2 | 2 | 2 | 6 | 65 | non (au plancher, hors du nombre visé) |  |  |  | gardée |
| 3 | `f0a8378953d43` | P (c) | 2 | 2 | 2 | 6 | 52 | non (au plancher, hors du nombre visé) |  |  |  | gardée |
| 4 | `fcd56a5ce3c1c` | N | 1 | 2 | 2 | 5 | 94 | non (au plancher, hors du nombre visé) |  |  |  | gardée |
| 5 | `f4a47f030c829` | P (c) | 2 | 2 | 2 | 6 | 17 | non (au plancher, hors du nombre visé) |  |  |  | non gardée (GO-63) |
| 6 | `fb45c8739b3d2` | P (d) | 2 | 2 | 2 | 6 | 4 | oui, place réservée, voie P |  |  |  | gardée |
| 7 | `f562951db6c70` | I | 2 | 2 | 2 | 6 | 61 | non (au plancher, hors du nombre visé) | oui |  |  | gardée |
| 8 | `f68f93bac44e8` | P (c) | 2 | 2 | 2 | 6 | 42 | non (au plancher, hors du nombre visé) |  |  |  | gardée |
| 9 | `fa38f9faa24e0` | P (e) | 2 | 2 | 2 | 6 | 55 | non (au plancher, hors du nombre visé) |  |  | X1 | gardée |
| 10 | `fdcf828b0dc80` | P (c) | 2 | 2 | 2 | 6 | 78 | non (au plancher, hors du nombre visé) |  |  |  | gardée |
| 11 | `ff60dbc7baa6f` | I | 2 | 2 | 2 | 6 | 33 | non (au plancher, hors du nombre visé) |  |  |  | gardée |
| 12 | `fafa0062508c9` | N | 2 | 2 | 2 | 6 | 80 | non (au plancher, hors du nombre visé) |  |  | X1 |  |
| 13 | `f7219bb36cfcb` | I | 2 | 2 | 2 | 6 | 3 | oui, place réservée, voie I |  |  |  |  |
| 14 | `f327b86c669cc` | P (c) | 2 | 2 | 2 | 6 | 43 | non (au plancher, hors du nombre visé) |  |  |  | gardée |
| 15 | `fa312929593cf` | P (c) | 2 | 2 | 2 | 6 | 7 | oui, au rang, toutes voies confondues |  |  |  |  |
| 16 | `fd688912a8667` | I | 2 | 2 | 2 | 6 | 54 | non (au plancher, hors du nombre visé) |  |  |  | gardée |
| 17 | `f7a4918afe116` | P (c) | 2 | 2 | 2 | 6 | 69 | non (au plancher, hors du nombre visé) |  |  |  |  |
| 18 | `f5373a31410ab` | P (c) | 2 | 2 | 2 | 6 | 36 | non (au plancher, hors du nombre visé) |  |  |  | gardée |
| 19 | `fc37640a0181d` | P (e) | 2 | 2 | 2 | 6 | 56 | non (au plancher, hors du nombre visé) |  |  |  |  |
| 20 | `f0d21fb62aff2` | P (c) | 2 | 2 | 2 | 6 | 40 | non (au plancher, hors du nombre visé) |  |  |  |  |
| 21 | `fcfa3d98b90f8` | P (e) | 2 | 2 | 2 | 6 | 68 | non (au plancher, hors du nombre visé) |  |  |  |  |
| 22 | `f98b6974fb1dd` | I | 2 | 2 | 2 | 6 | 28 | non (au plancher, hors du nombre visé) |  |  |  | non gardée (GO-63) |
| 23 | `f01d286e78e83` | P (d) | 2 | 2 | 2 | 6 | 79 | non (au plancher, hors du nombre visé) |  |  |  | gardée |
| 24 | `f4250eb75fbba` | P (b) | 2 | 2 | 2 | 6 | 66 | non (au plancher, hors du nombre visé) |  |  |  | gardée |
| 25 | `f19c7995f9c6a` | P (c) | 2 | 2 | 2 | 6 | 60 | non (au plancher, hors du nombre visé) |  |  |  |  |
| 26 | `f7782e931911d` | P (c) | 2 | 2 | 2 | 6 | 47 | non (au plancher, hors du nombre visé) |  |  |  | gardée |
| 27 | `fd31770b6907d` | N | 2 | 2 | 2 | 6 | 24 | non (au plancher, hors du nombre visé) |  | oui (A) |  |  |
| 28 | `fb9e8ae1b97b8` | P (c) | 2 | 2 | 2 | 6 | 57 | non (au plancher, hors du nombre visé) |  |  |  | gardée |
| 29 | `ff76aee57bba1` | P (c) | 2 | 2 | 2 | 6 | 19 | non (au plancher, hors du nombre visé) |  |  |  | gardée |
| 30 | `fcbf4a2dd1a57` | P (e) | 2 | 2 | 2 | 6 | 15 | non (au plancher, hors du nombre visé) |  |  |  |  |
| 31 | `f0497de657ec8` | I | 2 | 1 | 2 | 5 | 91 | non (au plancher, hors du nombre visé) |  |  |  |  |
| 32 | `fc1f059e8873e` | I | 2 | 2 | 2 | 6 | 83 | non (au plancher, hors du nombre visé) |  |  |  |  |
| 33 | `f1373c384a771` | P (d) | 2 | 2 | 2 | 6 | 20 | non (au plancher, hors du nombre visé) |  |  |  |  |
| 34 | `f14a90c4535dd` | N | 2 | 1 | 2 | 5 | 92 | non (au plancher, hors du nombre visé) |  |  |  | gardée |
| 35 | `f1c19731ccffb` | P (b) | 2 | 2 | 2 | 6 | 38 | non (au plancher, hors du nombre visé) |  |  |  | gardée |
| 36 | `f2e3582b5fa97` | I | 2 | 2 | 2 | 6 | 53 | non (au plancher, hors du nombre visé) |  | oui (A et B) |  |  |
| 37 | `f1d7c5f2e47d7` | P (c) | 2 | 2 | 2 | 6 | 12 | non (au plancher, hors du nombre visé) |  |  |  | gardée |
| 38 | `fb2a799e80c91` | P (c) | 2 | 2 | 2 | 6 | 82 | non (au plancher, hors du nombre visé) |  |  |  |  |
| 39 | `f8c05bffe7cb1` | P (c) | 2 | 2 | 2 | 6 | 75 | non (au plancher, hors du nombre visé) |  |  |  | gardée |
| 40 | `f6bb348e95955` | I | 2 | 2 | 2 | 6 | 25 | oui, place réservée, voie I |  |  |  | gardée |
| 41 | `f38a6ed2f7434` | P (c) | 2 | 2 | 2 | 6 | 11 | non (au plancher, hors du nombre visé) |  |  |  | gardée |
| 42 | `f91a7a590c8fe` | P (c) | 2 | 2 | 2 | 6 | 41 | non (au plancher, hors du nombre visé) |  |  |  | gardée |
| 43 | `f11f00774547f` | P (c) | 2 | 2 | 2 | 6 | 27 | non (au plancher, hors du nombre visé) |  |  |  |  |
| 44 | `fb6f958eb1bb6` | N | 2 | 2 | 2 | 6 | 35 | non (au plancher, hors du nombre visé) |  |  |  |  |
| 45 | `fed7a993d9671` | P (c) | 2 | 2 | 2 | 6 | 9 | non (au plancher, hors du nombre visé) | oui |  |  |  |
| 46 | `f51c0935052f6` | P (b) | 2 | 2 | 2 | 6 | 6 | oui, au rang, toutes voies confondues |  |  |  |  |
| 47 | `f473bb6a03ca3` | P (c) | 2 | 2 | 2 | 6 | 48 | non (au plancher, hors du nombre visé) |  |  |  |  |
| 48 | `fd9bbc7b19deb` | N | 2 | 2 | 2 | 6 | 89 | non (au plancher, hors du nombre visé) |  | oui (B) |  | gardée |
| 49 | `fd81c25c080e8` | P (c) | 2 | 2 | 2 | 6 | 63 | non (au plancher, hors du nombre visé) |  |  |  | gardée |
| 50 | `fb3a2cc87251c` | P (e) | 2 | 2 | 2 | 6 | 71 | non (au plancher, hors du nombre visé) |  |  |  | gardée |
| 51 | `fe15813583b5c` | N | 2 | 2 | 2 | 6 | 58 | non (au plancher, hors du nombre visé) |  |  |  | gardée |
| 52 | `f11193560f4d4` | P (c) | 2 | 2 | 2 | 6 | 13 | non (au plancher, hors du nombre visé) |  |  |  |  |
| 53 | `fbae5b702558e` | I | 2 | 2 | 2 | 6 | 74 | non (au plancher, hors du nombre visé) |  |  |  |  |
| 54 | `f2033ad1cbe45` | P (c) | 2 | 2 | 2 | 6 | 1 | oui, place réservée, voie P |  |  |  |  |
| 55 | `f5ee3a75faea3` | N | 2 | 2 | 2 | 6 | 30 | non (au plancher, hors du nombre visé) |  |  |  | gardée |
| 56 | `f4cbf7e62ff7b` | N | 2 | 2 | 2 | 6 | 22 | non (au plancher, hors du nombre visé) |  |  |  |  |
| 57 | `fcc96538bff00` | P (b) | 2 | 2 | 2 | 6 | 45 | non (au plancher, hors du nombre visé) |  |  |  | gardée |
| 58 | `f169420b8d1d8` | P (d) | 2 | 2 | 2 | 6 | 31 | non (au plancher, hors du nombre visé) |  |  |  | gardée |
| 59 | `f232221730a16` | N | 2 | 2 | 2 | 6 | 70 | non (au plancher, hors du nombre visé) |  |  |  | gardée |
| 60 | `f69c4a2a9c9e7` | N | 2 | 2 | 2 | 6 | 62 | non (au plancher, hors du nombre visé) |  |  |  |  |
| 61 | `ff99ce570c638` | N | 2 | 2 | 2 | 6 | 67 | non (au plancher, hors du nombre visé) |  |  |  | gardée |
| 62 | `fc53dfee17677` | P (c) | 2 | 2 | 2 | 6 | 77 | non (au plancher, hors du nombre visé) |  |  |  |  |
| 63 | `fefca0bd94064` | P (e) | 2 | 2 | 2 | 6 | 73 | non (au plancher, hors du nombre visé) |  |  | X1 | gardée |
| 64 | `f6f8c8b855234` | P (e) | 2 | 2 | 2 | 6 | 5 | oui, au rang, toutes voies confondues |  |  |  |  |
| 65 | `fe0ce53be28b3` | P (c) | 2 | 2 | 2 | 6 | 16 | non (au plancher, hors du nombre visé) |  |  |  |  |
| 66 | `f76714f1ddda4` | I | 2 | 2 | 2 | 6 | 88 | non (au plancher, hors du nombre visé) | oui |  |  | gardée |
| 67 | `f856659046065` | P (c) | 2 | 2 | 2 | 6 | 64 | non (au plancher, hors du nombre visé) |  |  |  | gardée |
| 68 | `ff3f04bf88c72` | P (c) | 2 | 2 | 2 | 6 | 46 | non (au plancher, hors du nombre visé) |  |  |  |  |
| 69 | `fbac0bab50a65` | N | 2 | 2 | 2 | 6 | 2 | oui, place réservée, voie N |  |  |  | non gardée (GO-63) |
| 70 | `f9a517d00f493` | P (c) | 2 | 2 | 2 | 6 | 23 | non (au plancher, hors du nombre visé) |  |  |  | gardée |
| 71 | `fa46f1f3bd417` | P (c) | 2 | 2 | 2 | 6 | 26 | non (au plancher, hors du nombre visé) |  |  |  |  |
| 72 | `f772b4c18818b` | P (c) | 2 | 2 | 2 | 6 | 81 | non (au plancher, hors du nombre visé) |  |  |  | gardée |
| 73 | `f89c771e3ac68` | N | 2 | 2 | 2 | 6 | 10 | oui, place réservée, voie N |  |  |  | gardée |
| 74 | `fdfac3afd4bae` | P (c) | 2 | 2 | 2 | 6 | 18 | non (au plancher, hors du nombre visé) |  |  |  |  |
| 75 | `f5662015db5bf` | P (c) | 2 | 2 | 2 | 6 | 34 | non (au plancher, hors du nombre visé) |  |  |  | gardée |
| 76 | `f319823a86ea7` | P (c) | 2 | 2 | 2 | 6 | 84 | non (au plancher, hors du nombre visé) |  |  |  |  |
| 77 | `f6caf922edbf1` | P (c) | 2 | 2 | 2 | 6 | 39 | non (au plancher, hors du nombre visé) |  |  |  | gardée |
| 78 | `f7b38afebd589` | N | 2 | 2 | 2 | 6 | 59 | non (au plancher, hors du nombre visé) |  |  |  |  |
| 79 | `f19c4c823d67c` | N | 2 | 2 | 2 | 6 | 32 | non (au plancher, hors du nombre visé) |  |  |  | gardée |
| 80 | `f6e7646851ba5` | I | 2 | 2 | 2 | 6 | 76 | non (au plancher, hors du nombre visé) |  |  |  | gardée |
| 81 | `fdafe4598caad` | P (c) | 2 | 2 | 2 | 6 | 8 | non (au plancher, hors du nombre visé) |  |  |  | gardée |
| 82 | `f7cc0003c4b2c` | I | 2 | 2 | 2 | 6 | 50 | non (au plancher, hors du nombre visé) |  |  |  | gardée |
| 83 | `fcf27198b7462` | P (c) | 2 | 2 | 2 | 6 | 37 | non (au plancher, hors du nombre visé) |  |  |  | non gardée (GO-63) |
| 84 | `fe887ca5cb62c` | P (c) | 2 | 2 | 2 | 6 | 49 | non (au plancher, hors du nombre visé) |  |  |  |  |
| 85 | `f71350282d0c0` | N | 2 | 2 | 2 | 6 | 87 | non (au plancher, hors du nombre visé) |  |  |  | gardée |
| 86 | `ff6ddb6c537f6` | P (c) | 2 | 2 | 2 | 6 | 51 | non (au plancher, hors du nombre visé) |  |  |  |  |
| 87 | `fec2307cbabb1` | P (b) | 2 | 1 | 2 | 5 | 93 | non (au plancher, hors du nombre visé) |  |  |  | gardée |
| 88 | `f760c773d6f15` | P (c) | 2 | 2 | 2 | 6 | 85 | non (au plancher, hors du nombre visé) |  |  |  |  |
| 89 | `fb484116eccc4` | P (c) | 2 | 2 | 2 | 6 | 14 | non (au plancher, hors du nombre visé) |  |  |  |  |
| 90 | `f17603c39bc32` | P (c) | 2 | 2 | 2 | 6 | 90 | non (au plancher, hors du nombre visé) |  | oui (A et B) |  | gardée |
| 91 | `fc36c3c3125ac` | I | 2 | 2 | 2 | 6 | 29 | non (au plancher, hors du nombre visé) |  |  |  | gardée |
| 92 | `f1675a6c453a9` | P (c) | 2 | 2 | 2 | 6 | 21 | non (au plancher, hors du nombre visé) |  |  |  | gardée |
| 93 | `f2d60f571d0e2` | P (c) | 2 | 2 | 2 | 6 | 86 | non (au plancher, hors du nombre visé) |  |  |  |  |
| 94 | `f9c8c39740352` | N | 2 | 2 | 2 | 6 | 44 | non (au plancher, hors du nombre visé) |  |  |  |  |

## 6. Ce que ce rejeu ne dit pas, et ce qu'il propose à la mère

- Il ne dit pas qu'une carte vaut mieux qu'une autre : seule l'épreuve le dira (N-058). Il n'est pas une épreuve tenue à l'écart des critères : leur rédacteur connaissait les écarts de la v1 sur ces cartes (critères v2, « Limite dite d'avance »).
- Il ne mesure aucun effet par espèce (espèce non lue). Le programme de la mère peut le faire sur le fichier des sélections, dans les deux sens (§ 10, règle R4).
- **Constat sur la règle, à porter à Lazar sans la changer** (§ 0 des critères : un critère inapplicable ne se change pas, l'écart s'écrit) : à notes de 0 à 2 et plancher à 4 sur 6, les cartes d'une course dont la consigne impose oracle, témoin, base et règle de coupe atteignent toutes le plafond ; le nombre visé est alors tranché par le tirage. Si l'on veut que la règle choisisse, il faut un critère qui varie entre ces cartes ; si l'on veut seulement ne rien éliminer, la v2 le fait, et le choix revient à Lazar sur la liste entière.
- Les deux lectures (O et F) restent à assembler par programme : la somme des notes, les exclusions communes, les fusions dites par les deux et les écarts de deux points peuvent changer le rang, non le constat de plafond si l'autre lecteur note comme moi.
