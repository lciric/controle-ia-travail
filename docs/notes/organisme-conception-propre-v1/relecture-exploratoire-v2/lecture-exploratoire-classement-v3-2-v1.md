# Lecture exploratoire — aucune désignation (règle v2.1 changée après la vue de E2)

**Lecture du classement de la relecture exploratoire v2 des fiches de la course « conception propre » — v1.**
Écrite par un lecteur neuf (sous-agent de la session mère, modèle Fable 5.2), le 14 novembre 2026 vers 23:57 UTC
(`date -u`), qui n'a écrit ni la règle, ni les témoins, ni l'outil, ni le classement.

**Statut.** Ce rapport ne désigne rien : aucun gagnant, aucune fiche « retenue » pour une suite, aucune recommandation de
choix. La règle a été réécrite après que la première lecture a rendu E2, en connaissant le recalcul de l'audit ; la
relecture elle-même rend de nouveau E2 (classement « non lisible »). Les identifiants de fiches cités plus bas le sont
pour décrire, jamais pour choisir. Aucun chiffre d'ici n'est opposable (R1).

Chemins relatifs à `docs/notes/organisme-conception-propre-v1/` ; `RE/` = `relecture-exploratoire-v2/` ;
`CL/` = `lecture-g1-v3-2/classement/`.

## 0. Pièces lues, empreintes vérifiées

| Abrégé | Pièce | Empreinte | Vérification |
|---|---|---|---|
| [MD] | `CL/classement-v3-2.md` | `b175883e` | `sha256sum -c` : OK |
| [JS] | `CL/classement-v3-2.json` | `95da8192` | OK |
| [L1] | `CL/lecture-verifiee-L1-v3-2.json` | `8b3ff58d` | OK |
| [L2] | `CL/lecture-verifiee-L2-v3-2.json` | `81d23dbd` | OK |
| [RG] | `RE/regle-v2-1.md` | `b955e730` | OK |
| [DF] | `RE/differentiel-regle-v2-v2-1.diff` | `cb7276e5` | OK |
| [RP] | `RE/rapport-v1.md` | `d454f366` | OK |
| [EN] | `RE/engagement-avant-epreuve-v2.md` | `27ffad3a` | OK |
| [DV] | `RE/devis-v2.md` | `b412723e` | OK |

Rien d'autre n'a été ouvert : ni les fiches (`runs/`), ni `diag/`, ni les envois, ni les programmes de classement, ni
les notes du juge de l'organisme. Aucun appel payant, aucune machine, aucun commit. Les chiffres marqués « recalcul »
sont comptés par moi sur les valeurs `compte` de [L1] et [L2] et les valeurs `retenu` de [JS] ; ils ne figurent pas
tels quels dans le classement et n'étaient pas déclarés d'avance par la règle.

## 1. Ce que mesure le classement, en mots simples

- **Qui lit.** Un seul modèle lecteur, Astra, lit deux fois une pile de 43 fiches servies sans nom d'auteur : 23 fiches
  réelles, 12 témoins plantés (7 conceptions publiées réécrites, 3 fausses fiches, un « vrai » et son jumeau) et 8 idées
  « au hasard » (fond tiré, forme complète). « L1 » et « L2 » sont ces deux passages du même modèle, dans deux ordres
  différents — pas deux lecteurs distincts ([RG] § 1, § 9 point 2).
- **Ce qu'il rend.** Pour chaque fiche, sept oui/non (R1 à R7) et une réponse sur la nouveauté (N : `aucune` ou une
  entrée d'un catalogue fermé de 12 conceptions connues). Un « oui » ne compte que s'il s'appuie sur un passage recopié
  mot pour mot de la fiche. La **valeur retenue** est « oui » seulement si les deux passages disent « oui » prouvé
  ([RG] § 1).
- **Comment le rang est fait** ([RG] § 6). Deux portes (R2 et R3 : contraintes dures du programme) ; une fiche qui en
  manque une est « écartée ». Parmi les passées, « neuve » si N = `aucune`. Score des neuves : S = R1 + R4 + R5 + R6 + R7,
  de 0 à 5. Rang : S décroissant, puis coût déclaré par la fiche (« processeur » avant « dépense »), puis un tirage au sort.
- **Ce que cela mesure donc** : à quel point une fiche *affiche*, aux yeux d'Astra, les éléments demandés (prédiction
  fermée, garanties, mécanisme…), et si Astra la rapproche d'une entrée du catalogue. **Ce que cela ne mesure pas** : la
  valeur d'une idée, ni sa nouveauté hors de ce catalogue de 12 entrées ([RG] § 9 points 6 et 7).
- **Ce qui a changé par rapport à la première lecture** ([RG] § 2 ; [EN] § 2 ; [RP] § 1) : R7 (le jugement sur le
  mécanisme) n'est plus une porte mais un point du score ; témoins et idées au hasard réécrits à la longueur des vraies
  fiches ; le test de séparation d'avec le hasard est refait. De la v2 à la v2.1 ([DF]) : idées au hasard refaites sur le
  style seulement, issues de la séparation renommées, table de puissance déclarée, limites ajoutées — avant la relecture,
  mais après la première lecture et son verdict E2.

## 2. Le classement tel qu'il est

**Verdict du programme** ([JS] `verdict` ; [MD]) : « E2 v2 : classement exploratoire non lisible (L2) ; pas de séparation
(non lue : classement non lisible ; L5 v2 : p = 0,63009) ; rang rapporté avec cette mention ; exploratoire : aucune idée
désignée ». Le champ `designees` de [JS] est vide. Issues levées : E2 v2 et E3 v2 ; audit de propreté déclenché
([JS] `echecs`, `audit_proprete`).

**Statuts des 23 fiches réelles** ([JS] `rang_exploratoire.statut`) : 18 « neuves », 5 « écartées » (toutes par la porte
R3), 0 « occupée ». Répartition du score des 18 neuves (recalcul sur [JS]) : **11 fiches à S = 5** (le maximum),
4 à S = 4, 3 à S = 3.

**Rang exploratoire, à titre d'information, non lisible** ([JS] `rang_exploratoire.ordre_neuves` ; critères dans l'ordre
R1 R2 R3 R4 R5 R6 R7, valeurs comptées de [L1] et [L2], valeurs retenues de [JS]) :

| Rang | Fiche | S | L1 | L2 | Retenu | Désaccord L1/L2 |
|---|---|---|---|---|---|---|
| 1 à 11 (ex æquo) | opus-p1-01, fable-p2-01, fable-p1-04, fable-p1-03, fable-p2-02, opus-p1-04, opus-p1-03, opus-p1-02, argon-p2-02, argon-p1-02, fable-p2-04 | 5 | 1111111 | 1111111 | 1111111 | aucun |
| 12 | opus-p1-05 | 4 | 1110111 | 1110111 | 1110111 | aucun (R4 = 0) |
| 13 | fable-p1-01 | 4 | 1111011 | 1111011 | 1111011 | aucun (R5 = 0) |
| 14 | argon-p1-03 | 4 | 1111110 | 1111110 | 1111110 | aucun (R7 = 0) |
| 15 | argon-p2-03 | 4 | 1111110 | 1111110 | 1111110 | aucun (R7 = 0) |
| 16 | argon-p2-01 | 3 | 1111010 | 1111010 | 1111010 | aucun (R5, R7 = 0) |
| 17 | argon-p1-01 | 3 | 1111010 | 1111010 | 1111010 | aucun (R5, R7 = 0) |
| 18 | fable-p2-03 | 3 | 1111011 | 1111010 | 1111010 | **R7** (L1 : 1 ; L2 : 0) |
| écartée (R3) | argon-p2-05 | — | 1101110 | 1101110 | 1101110 | aucun |
| écartée (R3) | argon-p1-04 | — | 1101000 | 1101000 | 1101000 | aucun |
| écartée (R3) | fable-p1-05 | — | 1101010 | 1111010 | 1101010 | **R3** (L1 : 0 ; L2 : 1) |
| écartée (R3) | argon-p1-05 | — | 1101010 | 1101011 | 1101010 | **R7** (L1 : 0 ; L2 : 1) |
| écartée (R3) | argon-p2-04 | — | 1101010 | 1101000 | 1101000 | **R6** (L1 : 1 ; L2 : 0) |

N = `aucune` pour les 23 fiches réelles dans les deux passages ([L1], [L2]). L'ordre à l'intérieur du bloc des onze
ex æquo est celui que donne [JS] ; il ne vient d'aucun jugement du lecteur (voir § 3.2).

**Accord des deux passages sur les 23 fiches réelles** (recalcul sur [L1], [L2]) : 4 désaccords sur 184 jugements
(23 fiches × 8 réponses). Par critère : R1, R2, R4, R5, N : 23 sur 23 ; R3 : 22 sur 23 ; R6 : 22 sur 23 ; R7 : 21 sur 23
(κ ≈ 0,82). Les deux passages donnent le même statut « neuve » aux mêmes 18 fiches si l'on exige l'accord, et le même
score à 17 des 18 neuves (la dix-huitième, fable-p2-03, vaut 4 selon L1 et 3 selon L2).

**Accord sur toute la pile** ([JS] `L4`) : R7 : κ = 0,721, accord brut 0,860 (6 désaccords sur 43, dont 4 sur les
témoins — recalcul) ; N : κ = 1,0.

**Contre le hasard** ([JS] `L5`, `separation`, `descriptif_holm`, `retenu`) :
- Score composite C (0 à 6) : moyenne des 23 réelles 4,26, moyenne des 8 idées au hasard 4,50 ; différence −0,24,
  de signe **contraire** à la prédiction ; p = 0,630 ; pas de rejet.
- Aucune idée au hasard n'est écartée ni dite occupée ; elles obtiennent S = 4 (quatre fiches) ou S = 3 (quatre fiches),
  c'est-à-dire le score des rangs 12 à 18 des fiches réelles.
- R7 retenu : 13 réelles sur 23 à 1, 0 idée au hasard sur 8 (0 dans chaque passage, que la chaîne tirée soit cohérente ou
  contraire : [JS] `hasard_R7_selon_la_chaine`). Le test de R7 seul est calculé (p = 0,0058) mais **non lu**, par la
  séquence fixe de la règle (L5 non rejetée, classement non lisible). En comparaison descriptive à huit critères :
  différence 0,565, p brute 0,0095, p de Holm 0,076.
- Les sept autres comparaisons critère par critère : p de Holm = 1,0.

**Témoins** ([JS] `L1` à `L3`, `exactitude_lecteur`) :
- Publiées réécrites : 7 sur 7 reconnues avec l'entrée attendue, dans les deux passages.
- Vrai et jumeau : portes passées, « neufs », R7 = 1 prouvé dans les deux passages.
- Fausses fiches : la fausse fiche visant R1 (T2-F1, prédiction sans seuil ni effet chiffré) est lue R1 = 0 par L1 et
  **R1 = 1 par L2** ; les deux autres sont lues 0 au critère visé par les deux passages. C'est ce qui fait manquer la
  condition L2 et rend le classement « non lisible ».
- R7 sur les témoins à valeur fixée : 10 justes sur 11 pour L1, 7 sur 11 pour L2 ; accord L1/L2 sur R7 parmi les
  12 témoins : 8 sur 12 (recalcul).

**Relecture contre première lecture** ([JS] `relecture_contre_premiere_lecture`, `regle_v2_sur_la_premiere_lecture`) :
sur les 23 fiches, valeurs retenues identiques pour R1, R2, R3, R7 et N ; accord 0,957 sur R4, 0,913 sur R5 et sur R6.
La règle v2 appliquée aux valeurs de la première lecture donne les mêmes cinq premières positions et les mêmes treize
premières ; seuls les rangs 14 à 18 se permutent.

## 3. Ce qui est solide, ce qui ne l'est pas

### 3.1 Ce qui tient (au sens : stable entre les deux passages et entre les deux lectures)

- **La lecture est complète et prouvée** : 18 réponses closes, aucune anomalie, aucune fiche touchée, aucun « oui » non
  prouvé, aucun passage court refusé ([JS] `lecture_complete`, `non_prouves`, `passages_courts_refuses`).
- **Le partage en trois paliers est stable** : mêmes 18 neuves, même bloc de 11 au maximum, mêmes valeurs retenues de R3
  et R7 qu'à la première lecture (accord 1,000 sur ces deux critères).
- **La reconnaissance des publiées réécrites** est sans faute (7 sur 7, deux passages) — avec la réserve que les témoins
  gardent le vocabulaire du catalogue ([RG] § 9 point 9).
- **Astra ne donne R7 à aucune des 8 idées au hasard**, dans aucun des deux passages, et le donne au vrai et à son
  jumeau dans les deux.

### 3.2 Ce qui ne tient pas

- **Le haut du rang est un ex æquo de onze fiches.** Les onze ont toutes les réponses à 1 dans les deux passages : le
  score est au plafond pour 11 des 18 neuves et ne peut pas les départager. L'ordre affiché entre elles vient du coût
  *déclaré par la fiche elle-même*, puis d'un tirage au sort ([RG] § 6.4 ; rangs de départage dans [JS]
  `rang_exploratoire.departage`). Les « deux premières » que nomme [MD] ne se distinguent des neuf suivantes par aucun
  jugement du lecteur. (La catégorie de coût de chaque fiche n'est pas dans les pièces lues ; les rangs de départage
  — 0 et 14 pour les deux premières, puis 5, 7, 11, 13, 15, 16, 17, 18, 20 en ordre croissant — sont compatibles avec
  « deux fiches à coût "processeur", neuf à coût "dépense" » : c'est une inférence, non une lecture.)
- **Le témoin à score permuté** ([JS] `temoin_score_permute`) place en tête deux autres fiches, sans aucune commune avec
  les deux premières : attendu pour un rang dont la tête est un ex æquo.
- **Les écarts sont d'un point, sur un seul critère.** Entre les paliers 5, 4 et 3, la différence est une ou deux
  réponses binaires. Le passage de S = 5 à S = 4 tient à R4 (une fiche), R5 (une fiche) ou R7 (deux fiches) ; chacun de
  ces critères a, sur les témoins ou entre lectures, un taux d'écart du même ordre (R5 : 2 fautes sur 11 par passage ;
  R7 : 4 désaccords sur 12 témoins ; R5 et R6 : accord 0,913 avec la première lecture).
- **Deux critères du score ne séparent rien.** R1 est à 1 pour les 23 réelles et les 8 idées au hasard, et le seul témoin
  fait pour l'éprouver échappe à un passage sur deux : R1 n'est ni discriminant ni validé. R6 est à 1 pour 21 réelles sur
  23 et pour les 8 idées au hasard. Le score est en pratique porté par R5 et R7.
- **Le score total ne distingue pas les fiches réelles d'idées dont le fond est tiré au sort** (4,26 contre 4,50).
  L'écart négatif vient des cinq fiches réelles écartées par R3 (score composite 0) alors qu'aucune idée au hasard ne
  l'est ; parmi les 18 neuves seules, la moyenne est 5,44 (recalcul, comparaison non déclarée d'avance, à ne pas lire
  comme un test).
- **R7 est le seul critère qui penche vers les fiches réelles, et c'est aussi le moins fiable.** Astra L2 se trompe sur
  R7 pour 4 témoins sur 11 ; R7 retenu vaut 0 pour 5 témoins publiés sur 7. La valeur p de R7 seul (0,0058) n'est pas
  lue par la règle, ne survit pas à la correction de Holm au seuil 0,05 (0,076), et porte sur un hasard « de réglages »
  qu'un lecteur peut juger pauvre pour une autre raison que le mécanisme ([RG] § 9 point 10).
- **Fiches dont la lecture dépend du passage** : fable-p1-05 est écartée par la porte R3 sur le seul passage L1 (L2 donne
  R3 = 1) ; fable-p2-03 perd son point de R7 sur le seul passage L2 ; argon-p1-05 (R7) et argon-p2-04 (R6) diffèrent
  aussi, sans effet sur leur statut. La règle des valeurs retenues tranche toujours vers 0 : un seul passage strict
  suffit à écarter ou à ôter un point.
- **Fiches témoins mal lues** : T2-F1 par L2 (R1 et R7 à 1, attendus 0) ; T2-C2 lue à 0 sur R3, R4 et R7 par les deux
  passages et sur R2 par L2 (attendus 1) ; T2-C9 lue R2 = 0 par les deux passages ; T2-C11 lue R3 = 0 et R5 = 0 par les
  deux ([JS] `exactitude_lecteur`). Pour les critères non porteurs, la valeur attendue est le consensus de deux
  relecteurs d'une autre famille : l'écart n'est pas une « erreur » d'Astra ([RG] § 7).
- **Trop propre à un endroit (R4 du programme, symétrie).** R7 retenu est identique fiche par fiche entre la première
  lecture et la relecture (κ = 1,0 sur 23 fiches), alors que l'accord sur R7 *entre deux passages* d'une même lecture
  est nettement plus bas (κ = 0,62 à la première lecture selon [RG] § 2 ; 0,72 sur la pile ici). Les fiches ont gardé
  étiquette et lot ([RG] § 9 point 3). Je ne sais pas l'expliquer avec les pièces lues ; cela mérite le même audit qu'un
  résultat suspect, et ne doit pas être lu comme une preuve de fiabilité de R7. L'audit de propreté est de toute façon
  déclenché par le programme (toutes les publiées reconnues).
- **Incohérence de libellé, mineure** : [MD] s'intitule « v3.2.1 (règle v2.1) » mais son verdict se termine par
  « (règle v2) » ; les fichiers s'appellent `…-v3-2…` pour un programme `v3-2-1` ([JS] `version`).

## 4. Limites

1. **Règle changée après la vue.** La règle v2 puis v2.1 a été écrite après le verdict E2 de la première lecture, par un
   préparateur qui connaissait le recalcul de l'audit (sans R7 dans les portes : p ≈ 0,21) et les valeurs lues sur les
   témoins ([EN], en-tête et § 2 ; [RG] § 9 point 1). Deux regards sur les mêmes fiches, aucune valeur p corrigée pour
   cela. Rien ici n'est confirmatoire.
2. **La relecture échoue à sa propre condition de lisibilité** (L2) : même sous la règle corrigée, le rang est rapporté
   « non lisible ».
3. **Un seul lecteur, lu deux fois.** L1 et L2 sont le même modèle (Astra), même consigne, même palier, même effort, et
   le même qu'à la première lecture ([RG] § 1, § 9 point 2). Leur accord n'est pas une réplique indépendante ; une erreur
   systématique d'Astra se répète quatre fois. Aucun lecteur d'une autre famille.
4. **Témoins et hasard d'une même main, éprouvés par la même famille.** Écrits par un modèle de la famille des
   proposeurs, éprouvés par un modèle de la famille de l'auteur ([RG] § 4, § 9 point 4 ; [RP] réserve r2). Un seul tirage
   de huit idées au hasard, toutes des changements de constante ([RG] § 9 points 5 et 10).
5. **Taille.** 23 fiches réelles, 8 idées au hasard, une génération, une question. La table de puissance de la règle
   ([RG] § 6.7) montre qu'avec 8 idées au hasard un déplacement d'une seule réponse change l'issue.
6. **Plafond.** 11 fiches sur 18 au score maximal ; quatre critères sur sept proches de la constante sur les réelles
   (R1 et R2 : 23 sur 23 ; R4 : 22 ; R6 : 21 — [JS] `relecture_contre_premiere_lecture`).
7. **Positions inchangées.** Étiquettes et lots identiques à la première lecture : l'effet d'ordre et de voisinage n'est
   pas retiré ([RG] § 9 point 3 ; [RP] réserve r5).
8. **Nouveauté relative à 12 entrées.** N = `aucune` pour 23 fiches sur 23 dit seulement qu'Astra ne les rapproche
   d'aucune entrée du catalogue ; les fiches qui se disent « transposition » ne sont pas relues ([RG] § 9 point 7).
9. **Le coût départage, et il est déclaré par la fiche.** Aucune vérification du coût dans les pièces lues.
10. **Comptes par proposeur** ([JS] `comptes_par_proposeur` : passées 6 sur 10, 5 sur 5, 7 sur 8) : rapportés par le
    programme ; jamais pour juger la composition (décision N-058), et confondus ici avec un lecteur unique.
11. **Ce que je n'ai pas vérifié** : je n'ai rejoué ni le classement ni les tests de permutation, et n'ai lu ni les
    fiches ni les passages cités ; je rapporte les sorties scellées et des décomptes simples faits dessus. La dépense
    réelle de la relecture n'est pas dans les pièces lues (devis : 2,69 USD attendus, plafond 6,50 — [DV] § 2 et 3).

## 5. Ce qu'une lecture confirmatoire devrait sceller avant d'être jouée

Ceci décrit des conditions de méthode, pas un choix de fiches ; ouvrir une telle lecture, son devis et son lecteur sont
des décisions de Lazar.

1. **Un préenregistrement scellé et contre-lu avant toute lecture** (R1, R2) : hypothèse, signe et taille prédits,
   statistique, seuil, plan d'analyse, liste d'arrêt — écrit par quelqu'un qui n'a vu ni ce classement ni les valeurs
   lues, ou qui déclare ce qu'il a vu.
2. **Des fiches jamais lues** (autre génération ou autre question). Les 23 fiches d'ici ont servi à régler la règle ;
   elles ne peuvent plus la confirmer.
3. **La règle entière, gelée** : portes, score, valeur retenue, et surtout **le traitement des ex æquo** — dire d'avance
   que des fiches à score égal sont rapportées ensemble, ou sceller un critère de départage qui ne soit ni déclaré par
   la fiche ni tiré au sort. Dire d'avance ce qu'on fait si le score plafonne (par exemple plus de la moitié des fiches
   au maximum).
4. **Ce que serait une « désignation », et la marge exigée** : l'écart minimal de score, comparé au bruit mesuré entre
   passages, en dessous duquel rien n'est désigné.
5. **Le lecteur** : au moins un lecteur d'une autre famille que les proposeurs, que l'auteur des témoins et que le
   premier lecteur ; nombre de passages ; ordres et lots retirés au sort ; règle d'accord entre lecteurs distincts.
6. **Des témoins éprouvés sur le lecteur lui-même ou sur une famille tierce**, avec leurs valeurs attendues scellées
   avant la lecture ; plusieurs fausses fiches par critère visé (une seule fiche pour R1 a suffi ici à rendre le tout
   non lisible, dans un sens comme dans l'autre) ; des publiées réécrites en paraphrase lointaine.
7. **Un hasard de puissance déclarée** : effectif fixé par un calcul de puissance écrit d'avance (huit ne suffisent
   pas), plusieurs tirages, des idées au hasard qui proposent des mécanismes et pas seulement des réglages, contrôles de
   forme scellés avant de voir toute lecture.
8. **La séquence de tests et la multiplicité** : test principal, tests secondaires, correction ; ce qui est lu si la
   lisibilité manque ; le sort d'un critère au plafond (R1, R6) ou trop peu fiable (R7) — seuil de fiabilité exigé avant
   qu'il entre dans un score.
9. **Les gardes** : chacune essayée sur un cas sain et sur un artefact (R5) ; audit de symétrie prévu pour un résultat
   trop propre comme pour un résultat nul (R4) ; l'accord R7 parfait entre lectures relevé au § 3.2 expliqué avant.
10. **Le périmètre de la revendication** : une telle lecture dirait au mieux qu'un lecteur trie des fiches selon ce
    qu'elles affichent ; la valeur des idées se mesure ailleurs, sur des mondes jamais vus, sous son propre
    préenregistrement et son propre devis ([RG] § 9 point 6).

## 6. En trois lignes

Le classement est rendu « non lisible » (une fausse fiche sur trois échappe à un passage) et ne sépare pas les fiches
réelles d'idées au fond tiré au sort (4,26 contre 4,50 ; p = 0,63). Onze des dix-huit fiches « neuves » sont ex æquo au
score maximal ; l'ordre entre elles vient du coût déclaré et d'un tirage, pas du lecteur. Le seul signal, R7 (13 sur 23
contre 0 sur 8), n'est pas lu par la règle, repose sur un lecteur unique et sur le critère le moins fiable. Rien n'est
désigné.
