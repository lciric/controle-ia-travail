# Règle corrigée (v2) de la relecture exploratoire des fiches de la course « conception propre »

Écrite par le préparateur neuf de la relecture (modèle A, sous-agent de la session mère), le 14 novembre 2026, de 12:20 à
12:22 UTC (heures relevées par `date -u`), **avant toute relecture** des 23 fiches. Décision de Lazar : R-2726
(« (b) Relire les mêmes fiches avec une règle corrigée  go »), sur l'audit de propreté R-2722
(`audit-proprete-lecture-g1-v3-1-v1.md`, `735d185a…`). Chemins relatifs à `docs/notes/organisme-conception-propre-v1/` ;
`RE/` = `relecture-exploratoire-v2/`. Les engagements pris avant l'épreuve des témoins sont scellés à part :
`RE/engagement-avant-epreuve-v2.md` (`27ffad3a…`, 11:39 UTC) ; cette règle les reprend sans écart, et y ajoute les témoins
éprouvés, le hasard tiré et leurs contrôles.

**Statut : exploratoire.** La règle change après que le classement scellé de la première lecture a rendu E2
(`lecture-g1-v3-1/classement/classement-v3-1.md`, `18f31d49…`). Ce verdict reste tel quel. Cette relecture n'est jamais
confirmatoire, ne « désigne » aucune idée au sens de la règle scellée (conception, § 4.6), et ses chiffres ne sont
opposables à rien (R1).

## 1. Ce qui ne change pas

- Admissibilité (conception, § 4.1) ; vue servie sans auteur ni marque de témoin ; étiquettes `F01…` ; lots de 5 ; **deux
  lectures** indépendantes par le lecteur de la première lecture : **Astra** (`gpt-6-astra`), palier **Flex**, effort
  **`medium`**, `store: false`, `max_completion_tokens` 32 768.
- Pièces servies, dans le même ordre : **`consigne-lecteur-v1.md` telle quelle** (`95efebaa…`), la question
  (`77c524f3…`), `faits-v1.md` (`d19b5400…`), le catalogue fermé de 12 entrées (`ddfb2522…`), puis la pile.
- Pile : les 23 fiches réelles admissibles de `runs/course-ideation-conception-propre-v1/20261113-235541-…-g1/copies/
  sortie--fiches-validees.json` (`a9f9594e…`), puis les 12 témoins du lecteur v2, puis les 8 idées au hasard v2 : 43 fiches,
  9 lots par lecture (sept de 5, deux de 4), 18 appels.
- Graines inchangées : ordres des lectures, départage et témoin à score permuté par
  `numpy.random.SeedSequence(2026111302).spawn(4)` (enfants 0, 1 ; 2 ; 3) ; test L5 par `SeedSequence(2026111303)` ;
  comparaisons descriptives par `SeedSequence(2026111303).spawn(8)`. La pile ayant le même effectif et le même ordre interne,
  **chaque fiche réelle garde l'étiquette et le lot de la première lecture** ; chaque témoin v2 prend la place du témoin v1
  de même rang.
- Preuve et accord (conception, § 4.5) : un 1 ne compte que si son passage (au moins 20 caractères hors espaces) est dans la
  fiche servie mot pour mot ; une occupation `Ck` seulement si les deux passages sont prouvés ; **valeur retenue** R = 1 si
  les deux lectures donnent 1 prouvé, N = `aucune` si les deux donnent `aucune`. Anomalies bloquantes de l'outil v3.1
  inchangées (lecture « incomplète » : E2).

## 2. R7 : composante du score, plus une porte

**Choix, fait avant toute épreuve et toute relecture (engagement, § 2) : R7 sort des portes et entre dans le score.**

| Option | Ce qu'elle fait | Risque principal |
|---|---|---|
| R7 porte (v1) | une fiche sans mécanisme retenu aux deux lectures est écartée | **faux rejets** : la porte la plus fragile (κ = 0,62 sur les 23 réelles selon l'audit ; 7 témoins sur 11 attendus à 1 lus 0) exigée aux deux lectures ; une lecture stricte suffit à écarter (le « vrai » v1) ; avec un hasard fluide, L5 reposerait encore sur ce seul veto |
| **R7 composante (retenu)** | R7 compte un point de S, comme R1, R4, R5, R6 | **perte du veto** : une fiche à raison générique ou de sens contraire peut être « neuve » et bien placée par les critères de forme ; S devient en partie un score de forme (R1, R2 au plafond ; R5, R6 liés à la longueur) |
| R7 porte à seuil gradué (une lecture sur deux suffit ; ou échelle à trois degrés) | veto adouci | **indulgence d'une lecture isolée** (les deux lectures sont du même modèle) ; asymétrie avec les autres critères ; à trois degrés, la consigne change : la lecture n'est plus comparable à la première et la consigne neuve n'est pas éprouvée |

Raisons : (1) une porte dit une violation d'une contrainte dure du programme (R2 : N-058 ; R3 : N-053 et rejets établis),
qui disqualifie quelle que soit la qualité ; R7 est un jugement de qualité, sa place est dans le score ; (2) une porte sur
un jugement peu fiable, exigée aux deux lectures, perd l'information sans retour, une composante se dégrade d'un point ;
(3) la consigne reste celle de la première lecture (comparabilité, § 9) ; (4) la part du fond dans une séparation d'avec le
hasard se lit à part (§ 6). Garde-fous : R7 rapporté pour chaque fiche du rang ; rang « à titre d'information » restreint
aux fiches de R7 retenu = 1 ; témoins et hasard au gabarit des vraies fiches (§ 3, § 5). Ce choix est fait **en
connaissant** le recalcul de l'audit sur la première lecture (sans R7 dans les portes : hasard v1 passé 7 sur 8, p ≈ 0,21).

## 3. Témoins du lecteur v2 : `RE/temoins-lecteur-v2.json` (`bb4f903f…`)

**Écrits sans lire le contenu des fiches réelles**, au gabarit mesuré par programme sur les 23 fiches réelles admissibles
(`RE/outils/stats_forme_fiches_v1.py`, `68f7f536…` ; sortie `RE/outils/resultat-stats-forme-reelles-et-temoins-v1-v1.json`,
`14d8ec4c…` : longueurs, comptes, valeurs des champs à liste fermée ; aucun texte). Mêmes catégories et effectifs qu'en v1.

| Code | Famille | Cible | Levier | Ce qu'il porte |
|---|---|---|---|---|
| T2-V | vrai | doit passer | coût | deux mises à jour de l'archive par génération, à budget égal (composantes conditionnelles des faits, § 4) ; absent du catalogue |
| T2-J | jumeau de T2-V | doit passer | coût | la même idée réécrite (mêmes nombres) |
| T2-F1 | fausse | R1 | composition | énumérateur local des variantes à un trait ; **prédiction sans seuil ni effet chiffré** |
| T2-F2 | fausse | R2 | juge | épisodes déplacés vers le test de mort ; **mesure sur le journal du juge** (promotions, éliminations) |
| T2-F3 | fausse | R3 | proposeurs | **sort et valeur e des cartes servis aux proposeurs** (N-053), objection non nommée |
| T2-C2, T2-C1, T2-C3, T2-C5, T2-C7, T2-C11, T2-C9 | publiées réécrites | N | juge, juge, proposeurs, composition, proposeurs, juge, coût | mécanisme central de POPPER, Co-Scientist, The AI Scientist, Fork-and-Flush, PACE, réserve réutilisable de Dwork et al., Pay Only for Disagreement (sources vérifiées sur PDF le 13 novembre par le préparateur de la course : `temoins-plantes-v1.md`, `9b0faed5…` ; PDF non rouverts ici), sans nommer la source hors des citations obligatoires de la question (N-064), citées comme dans toute fiche |

Gabarit atteint (`RE/outils/resultat-stats-forme-reelles-et-temoins-v2-v1.json`, `682da20c…`) :

| Mesure (médiane) | 23 réelles (q1–q3) | 12 témoins v1 | 12 témoins v2 | 8 hasard v1 | 8 hasard v2 |
|---|---|---|---|---|---|
| longueur totale (feuilles textuelles) | 4 174 (3 508–4 840) | 1 688,5 | 3 882 | 1 662 | 3 990 |
| six champs de l'audit (sans clés JSON ; l'audit compte 241 caractères de plus, constants) | 2 951 | 1 253,5 | 2 595,5 | 1 204,5 | 2 771 |
| `demande_organisme.texte` | 754 (583,5–853,5) | 157 | 656,5 | 68,5 | 688 |
| `cout.ordre_de_grandeur` | 212 (133,5–280,5) | 56 | 161 | 46 | 141 |
| antériorités (nombre) | 4 (3,5–5) | 0 | 4 | 0 | 4 |
| `type` question / approche | 20 / 3 | 0 / 12 | 10 / 2 | 0 / 8 | 7 / 1 |
| signe + / 0 / − | 21 / 2 / 0 | 7 / 0 / 5 | 11 / 1 / 0 | 3 / 0 / 5 | 7 / 1 / 0 |

Écarts résiduels, dits : moins de parenthèses (6 et 4 contre 10), phrases du hasard plus courtes (16 mots contre 21) ;
coût un peu plus court que la médiane réelle. Les 20 témoins passent le validateur réel de l'orchestrateur sans signal de la
garde lexicale (`RE/outils/valider_temoins_orchestrateur_v2.py`, `913e2a38…` ; `RE/outils/resultat-valider-temoins-
orchestrateur-v2.txt`, `7c24b8d8…` ; clone resté propre).

## 4. Valeurs attendues, éprouvées

**Comment** (engagement, § 6) : deux **relecteurs neufs de modèle C** par tour, en sessions séparées, **sans outil ni fichier**
(`claude -p --model sonnet --tools "" --safe-mode --no-session-persistence --output-format text < message`, lancé hors du
dépôt), chacun recevant **le message même que recevrait le lecteur** (consigne v1, question, faits, catalogue, puis un lot
des 12 témoins en vue servie, étiquetés `E01…` dans un ordre tiré par `SeedSequence(2026111405).spawn(6)`), sans savoir qu'il
s'agit de témoins. Préparation et vérification par `RE/outils/epreuve_valeurs_attendues_v1.py` (`4a9f4430…`), qui emploie
les fonctions de vérification de l'outil v3.1 (`95bc46c1…`) : passages mot pour mot. Différences avec la lecture : un seul
lot de 12 (non 5), étiquettes `E` ; aucun appel payant (sous-agents de la session).

**Tour 1** (12:02 à 12:10 UTC ; `RE/epreuve/resultat-epreuve-tour1.json`, `2486df0e…`) : tous les critères porteurs
confirmés par les deux relecteurs, sauf **N de T2-C7** : le second relecteur a reconnu C7 mais l'a cité hors mot pour mot
(« du vivier » pour « du vivier de conception »), donc compté `aucune`. **Tour 2** (12:11 à 12:17 UTC ;
`RE/epreuve/resultat-epreuve-tour2.json`, `4f0008f7…`) : T2-C7 réécrit (énoncé en phrases courtes, mécanisme inchangé ;
`RE/temoins-lecteur-v2-epreuve-2.json`, `580887e5…`) puis confirmé sur tous ses critères ; règle écrite avant le tour 2 :
les onze autres gardent leurs valeurs du tour 1, leurs lectures du tour 2 sont une information.

| Code | R1 | R2 | R3 | R4 | R5 | R6 | R7 | N | Lu par B1/B2 hors valeur voulue |
|---|---|---|---|---|---|---|---|---|---|
| T2-V | 1 | 1 | 1 | 1 | 1 | 1 | **1** | aucune | — (tours 1 et 2 : R7 = 1 aux quatre lectures) |
| T2-J | 1 | 1 | 1 | 1 | 1 | 1 | **1** | aucune | — (idem) |
| T2-F1 | **0** | 1 | 1 | 1 | 1 | 1 | 0 | aucune | R7 0/0 (voulu 1) |
| T2-F2 | 1 | **0** | 1 | 1 | 1 | 1 | 1 | aucune | — |
| T2-F3 | 1 | 1 | **0** | 1 | 1 | 1 | non fixée | aucune | R7 1/0 |
| T2-C2 | 1 | 1 | 1 | 1 | 0 | 1 | 1 | **C2** | R5 0/0 (calibrateur non nommé) |
| T2-C1 | 1 | 1 | 0 | 0 | 1 | 1 | 0 | **C1** | R7 0/0 (voulu 1) |
| T2-C3 | 1 | 1 | 0 | 1 | non fixée | 1 | 0 | **C3** | R5 0/1 ; R7 0/0 (voulu 1) |
| T2-C5 | 1 | 1 | 0 | 1 | 1 | 1 | 1 | **C5** | — |
| T2-C7 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | **C7** | — (tour 2) |
| T2-C11 | 1 | 1 | 1 | 0 | 1 | 1 | 1 | **C11** | R4 0/0 (nul non nommé) |
| T2-C9 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | **C9** | — |

En gras : critères porteurs (N des publiées ; critère visé des fausses ; R7 du vrai et du jumeau). R7 a ainsi une valeur
éprouvée pour onze témoins sur douze (T2-F3 : non fixée, rapportée). Stabilité (information, tour 2 contre tour 1) : tous les
critères porteurs identiques ; R7 est le critère le moins stable entre relecteurs (9 accords sur 12 au tour 2, 11 au tour 1).
**Limite** : modèle C est de la famille de l'auteur ; l'épreuve écarte une valeur indéfendable, elle ne prédit pas Astra.

## 5. Idées au hasard v2 : `RE/temoins-hasard-v2.json` (`5cef38f6…`)

Générateur `RE/outils/tirer_fiches_hasard_v2.py` (`35756e6d…`), principes fixés avant lui (engagement, § 7) : graines
`numpy.random.SeedSequence(2026111411).spawn(9)` (enfant 0 : attribution sans remise des gabarits de phrases et des urnes
des champs à liste fermée ; enfants 1 à 8 : une fiche chacun) ; numpy 2.4.6, Python 3.13.18. **Fond non pensé** : objet,
opération, métrique, signe et chaque maillon de la chaîne causale tirés indépendamment ; la chaîne implique un sens pour
la métrique, consigné (champ `chaine`, jamais servi) : **6 chaînes sur 8 impliquent le signe prédit, 2 le contredisent**, par
le seul tirage. **Forme complète** (prédiction fermée, métrique de l'oracle et du coût, aucune contrainte levée, garantie
du juge pour son levier, demande avec valeur, arrondi, borne, cas limite, consignation, contrôle négatif, coût chiffré).
**Sans phrases-types** : 48 réserves de 9 gabarits ou plus (433 en tout), chacun servi au plus une fois parmi les huit.

Contrôles par programme (`RE/outils/controler_temoins_v2.py`, `90bed804…` ; rapport final
`RE/outils/resultat-controles-temoins-v2.json`, `2c9caf87…`), **tous tenus** : médiane de chaque champ libre du hasard dans
l'intervalle interquartile des réelles ; longueur totale de chaque témoin entre le minimum et le maximum des réelles ;
aucune phrase d'au moins six mots commune à deux idées au hasard, ni entre le hasard et les témoins du lecteur (champs
libres) ; plus longue suite de mots commune à deux idées au hasard : 12 au plus ; codes, effectifs, admissibilité. Une
première sortie (`RE/temoins-hasard-v2-rejete-1.json`, `be25d8e3…`, d'un brouillon non gardé du générateur) a été **rejetée
par ces contrôles** (un même témoin à coût égal recopié dans plusieurs fiches ; phrases communes avec deux témoins du
lecteur) : le générateur a été corrigé sur la langue et la longueur seulement, jamais sur une lecture ; la sortie retenue est
la première qui passe. Le compte des chaînes cohérentes de la première sortie d'essai (6 sur 8) a été vu pendant ces
corrections : dit ici, il n'a guidé aucun changement. Tirage des urnes (sans remise parmi les 23 valeurs réelles) : 4 juge,
2 composition, 2 coût, **aucun levier « proposeurs »** ; 5 opérations sur 8 sont « réduire de moitié » : hasard du tirage,
dit, non corrigé. Le hasard n'a pas été soumis aux relecteurs de l'épreuve.

## 6. Classement v2, lisibilité, séparation

1. **Portes** : R2 = 1 et R3 = 1 (retenues) ; sinon « écartée ».
2. **Nouveauté** : parmi les passées, N retenue = `aucune` → « neuve » ; sinon « occupée ».
3. **S v2 = R1 + R4 + R5 + R6 + R7** (0 à 5) ; **C v2 = 1[R2 = R3 = 1 et N = `aucune`] × (1 + S v2)** (0 à 6).
4. **Rang exploratoire** des neuves : S v2 décroissant, coût déclaré (`processeur` avant `depense`), départage tiré (enfant 2).
   **Aucune désignation.** À côté : le même rang restreint aux fiches de R7 retenu = 1 (information) ; le témoin à score
   permuté (enfant 3, information).
5. **L1** : au moins 5 des 7 publiées reconnues avec l'entrée attendue dans au moins une lecture. **L2** : chaque fausse fiche
   à 0 au critère visé dans les deux lectures. **L3 v2** : T2-V et T2-J passent R2 et R3 (retenues), restent neufs, et
   reçoivent chacun **R7 = 1 prouvé dans au moins une des deux lectures**. **L4** : κ ≥ 0,4 sur R7 et sur N (accord brut
   ≥ 0,8 si une marge est constante). **Lisible** = lecture complète et L1, L2, L3 v2, L4 ; sinon « classement exploratoire
   non lisible » (E2 v2), rang rapporté avec cette mention.
6. **L5 v2** (exploratoire) : C v2 des 23 réelles contre les 8 idées au hasard v2 ; différence des moyennes ; permutation
   unilatérale, 100 000 permutations, `SeedSequence(2026111303)` ; rejet si p ≤ 0,05 ; prédiction : signe positif.
7. **Séparation réelle** (séquence fixe) : seulement si L5 v2 rejette, test de **R7 seul** (retenu, 0 ou 1), réelles contre
   hasard, même méthode, `SeedSequence(2026111404)` : p ≤ 0,05 → « **séparation réelle** » (portée par le critère de fond,
   entre fiches de longueur et de style comparables) ; p > 0,05 → « **séparation de forme** » ; L5 v2 non rejetée →
   « **pas de séparation** » (le second test est calculé et rapporté, jamais lu). Condition préalable : contrôles de longueur
   du § 5 tenus (c'est le cas).
8. **Issues** : E2 v2 (non lisible) ; E3 v2 (L5 v2 non rejetée) ; E4 v2 (moins de deux neuves : information) ; E5 (plus de
   80 % des passées occupées : information). **R4 du programme** : lisible et L5 rejetée, κ = 1 sur R7 et N, toutes les
   publiées reconnues, ou aucune idée au hasard passée aux portes : audit de propreté.

## 7. Analyses descriptives déclarées d'avance (jamais pour décider)

- Huit comparaisons critère par critère, réelles contre hasard, p ajustées par Holm.
- R7 lu sur les idées au hasard, séparé selon que leur chaîne implique ou non le signe prédit (6 contre 2).
- Exactitude du lecteur sur chaque témoin aux valeurs éprouvées (§ 4) ; valeurs « non fixées » exclues.
- **Relecture contre première lecture** (23 réelles) : accord des valeurs retenues, critère par critère, avec
  `lecture-g1-v3-1/classement/classement-v3-1.json` (`6ee04e1b…`).
- **Règle v2 appliquée aux valeurs retenues de la première lecture** (réelles : statut, S v2, rang ; recouvrement des deux
  premières et des cinq premières avec la relecture) : sépare l'effet de la règle de celui de la relecture. Calculée par le
  seul programme de classement, après la relecture ; jamais avant.
- Comptes par proposeur (N-058 : jamais pour choisir la composition).

## 8. Lecteur, outil, dépense

Outil v3.2 (`RE/lecture-classement-v3-2/`) = outil v3.1 + seuls changements nécessaires : nom de manifeste neuf
(`manifeste-relecture-v3-2.json`, hors du motif cherché par la v3.1, qui reste vérifiable), dossier fixe
`lecture-g1-v3-2/envois` permis à côté de celui de la v3.1 (seul autre manifeste toléré : celui de la première lecture, à son
chemin et à son empreinte), plafond absolu 11,65 USD (reste de GO-2026-11-13-06 : 21 − 9,347722, arrondi en dessous ; la
dépense de la première lecture est vérifiée sur son relevé scellé), témoins et hasard v2 en entrée, cette règle au
classement. Devis : `RE/devis-v1.md`. Palier Flex, effort `medium`, lecteur Astra inchangés.

## 9. Ce que cette relecture ne peut pas dire

1. **Rien de confirmatoire** : la règle change après E2, en connaissant le recalcul de l'audit ; L5 v2 et la « séparation
   réelle » sont des lectures exploratoires d'un second regard sur les mêmes fiches (deux regards : aucune valeur p n'est
   corrigée pour cela) ; aucune idée n'est désignée.
2. **Pas une réplique indépendante** : même lecteur (Astra), même famille, même consigne, même palier et même effort que la
   première lecture, et deux lectures du même modèle entre elles ; leur accord n'est pas une preuve d'indépendance, et une
   erreur systématique d'Astra se répète (la proposition (d) de l'audit, un lecteur d'une autre famille, n'est pas reprise).
3. **Positions inchangées** : les 23 réelles gardent étiquettes et lots ; une différence entre lectures mêle le hasard du
   lecteur et le changement des témoins voisins dans les lots ; l'effet d'ordre n'est pas tiré de nouveau.
4. **Témoins de la famille des proposeurs** (modèle A) et **épreuve par la même famille** (modèle C) : les valeurs attendues
   disent ce que lisent des lecteurs de cette famille ; Astra peut lire autrement (c'est ce que mesurent l'exactitude et L3).
5. **Un seul tirage de huit idées au hasard**, écrit par le même auteur ; « fond non pensé » est une construction (maillons
   tirés), non un modèle de l'idée faible ; huit fiches donnent peu de puissance à L5 v2 et au test de R7 seul.
6. **Aucune valeur des idées** : une séparation, même « réelle », dirait que R7 sépare des raisons pensées de raisons tirées
   au hasard et fluides, non que les fiches sont bonnes ; la valeur se mesure sur une famille de mondes jamais vue (conception,
   § 9), sous préenregistrement et devis propres.
7. **Nouveauté relative** au catalogue fermé de 12 entrées ; les 16 fiches qui se disent « transposition » ne sont pas
   relues à la main (proposition (f) de l'audit, hors de cette relecture).
8. Une génération, une question : rien sur l'organisme en général, ni sur la valeur relative des proposeurs.
