# Engagement avant épreuve — relecture exploratoire des fiches de la course « conception propre » sous une règle corrigée — v2

Écrit par le préparateur neuf de la relecture (modèle A, sous-agent de la session mère), le 14 novembre 2026, de 11:37 à
11:39 UTC (heures relevées par `date -u` ; scellé à 11:38:57), **avant** : l'écriture des témoins v2, l'écriture du générateur de hasard v2,
l'épreuve des valeurs attendues des témoins, et toute relecture. Scellé dès qu'il est écrit. **v2** : seule l'heure de fin change ; la v1 (`a03cb6ad…`, gardée, R12) portait
une heure de fin anticipée et fausse (11:55) ; aucun autre mot ne change. Décision de Lazar : R-2726
(relecture **exploratoire** ; le verdict E2 scellé de la première lecture reste tel quel ; rien n'est « désigné »). La règle
v2 (`regle-v2.md`) reprend ces engagements ; tout écart y serait déclaré, avec sa raison.

Chemins relatifs à `docs/notes/organisme-conception-propre-v1/`. Le préparateur connaît, avant d'écrire ceci : la conception
(`conception-course-v1.md`, `be3ba97e…`), la consigne du lecteur, les témoins v1, le classement v3.1 (`classement-v3-1.json`,
`6ee04e1b…`), l'audit de propreté (`735d185a…`, dont son recalcul « sans R7 dans les portes : p ≈ 0,21 »), les valeurs lues
sur les **seuls témoins** dans les lectures vérifiées v3.1, et les statistiques de forme des 23 fiches réelles admissibles
(`relecture-exploratoire-v2/outils/resultat-stats-forme-reelles-et-temoins-v1-v1.json`, `14d8ec4c…`, programme
`stats_forme_fiches_v1.py`, `68f7f536…` : longueurs, comptes et valeurs des champs à liste fermée seulement). Il n'a ouvert
ni le texte des fiches réelles, ni les notes du juge de l'organisme, ni les passages cités des fiches réelles.

## 1. Ce qui ne change pas (conception, § 4.1 à 4.5)

- Admissibilité (§ 4.1) ; vue servie sans auteur ni marque de témoin ; étiquettes `F01…` ; lots de 5 ; **deux lectures**
  indépendantes par le même lecteur qu'à la première lecture : **Astra** (`gpt-6-astra`), palier **Flex**, effort **`medium`**.
- Ce que le lecteur reçoit (§ 4.3) : **la consigne `consigne-lecteur-v1.md` telle quelle** (empreinte `95efebaa…`), la
  question, `faits-v1.md`, le catalogue fermé de 12 entrées, puis la pile : les 23 fiches réelles admissibles et **20
  témoins v2**. La consigne ne change pas : le lecteur fait exactement la même tâche qu'à la première lecture, ce qui rend
  les deux lectures des 23 fiches comparables (§ 8).
- Graines inchangées : ordres des lectures, départage et témoin à score permuté par
  `numpy.random.SeedSequence(2026111302).spawn(4)` ; test L5 par `SeedSequence(2026111303)`. La pile garde 43 fiches, dans
  le même ordre interne (fiches réelles, puis 12 témoins du lecteur, puis 8 idées au hasard) : chaque fiche réelle garde son
  étiquette et son lot de la première lecture ; chaque témoin v2 prend la place du témoin v1 de même rang.
- Preuve et accord (§ 4.5) : un 1 ne compte que si son passage (au moins 20 caractères hors espaces) est dans la fiche mot
  pour mot ; **valeur retenue** R = 1 si les deux lectures donnent 1 prouvé ; N = `aucune` si les deux donnent `aucune`.

## 2. R7 : composante du score, plus une porte

**Choix : R7 sort des portes et entre dans le score.** Portes : R2 = 1 et R3 = 1 (valeurs retenues). Score des neuves :
**S v2 = R1 + R4 + R5 + R6 + R7** (0 à 5). Les trois options, et leur risque :

| Option | Ce qu'elle fait | Risque principal |
|---|---|---|
| R7 porte (v1) | une fiche sans mécanisme retenu par les deux lectures est écartée | **faux rejets** : la porte la plus fragile (κ = 0,62 sur les 23 réelles, valeurs attendues des témoins non éprouvées, 7 sur 11 lues 0) est conjuguée sur deux lectures ; une seule lecture stricte écarte (le témoin « vrai » à la première lecture) ; avec des idées au hasard fluides, L5 reposerait encore sur ce seul critère |
| **R7 composante (retenu)** | R7 compte un point de S, comme R1, R4, R5, R6 | **perte du veto** : une fiche dont la raison est générique ou implique le signe contraire peut être « neuve » et bien classée par les critères de forme ; S devient en partie un score de forme (R1, R2 au plafond ; R5, R6 liés à la longueur) |
| R7 porte à seuil gradué (au moins une lecture sur deux ; ou échelle à trois degrés) | garde un veto adouci | **indulgence d'une seule lecture** (un oui isolé suffit, alors que les deux lectures viennent du même modèle) ; asymétrie avec les autres critères ; l'échelle à trois degrés change la consigne : la lecture n'est plus comparable à la première, et la consigne neuve n'est pas éprouvée |

Raisons du choix, données avant toute relecture : (1) une **porte** doit dire une violation des contraintes dures du
programme (R2 : décision N-058 ; R3 : N-053 et rejets établis), qui disqualifie quelle que soit la qualité ; R7 est un
**jugement de qualité** et sa place est dans le score ; (2) une porte sur un jugement peu fiable, exigée aux deux lectures,
multiplie les faux rejets et perd l'information sans retour, alors qu'une composante se dégrade d'un point ; (3) la
consigne reste celle de la première lecture (comparabilité, § 8) ; (4) L5 ne repose plus sur un veto unique, et la part du
fond dans une séparation se lit à part (§ 4, séparation réelle). Garde-fous contre le risque retenu : R7 est rapporté pour
chaque fiche du rang exploratoire ; un rang « à titre d'information » restreint aux fiches de R7 retenu = 1 est rapporté à
côté ; témoins et idées au hasard au gabarit des vraies fiches (longueur), pour que R5 et R6 ne séparent plus par la
seule longueur entre fiches réelles et témoins.

Ce choix est fait **en connaissant** le recalcul de l'audit sur la première lecture (sans R7 dans les portes, le hasard v1
passait 7 sur 8 et p ≈ 0,21) : c'est l'une des raisons pour lesquelles la relecture est exploratoire, jamais confirmatoire.

## 3. Classement v2 : rang exploratoire, aucune désignation

1. Portes : R2 = 1, R3 = 1 (retenues) ; sinon « écartée » (motif rapporté).
2. Nouveauté : parmi les fiches passées, N = `aucune` → « neuve » ; sinon « occupée ».
3. Score composite **C v2 = 1[R2 = R3 = 1 et N = `aucune`] × (1 + S v2)**, de 0 à 6.
4. Rang exploratoire des neuves : S v2 décroissant, puis coût déclaré (`processeur` avant `depense`), puis départage tiré
   (enfant 2). **Aucune désignation** au sens de la conception (§ 4.6) : le rang est rapporté « à titre exploratoire », et
   ses premières fiches ne sont jamais présentées comme désignées. Témoin à score permuté (enfant 3) : calculé et rapporté
   comme à la première lecture, à titre d'information.

## 4. Conditions de lisibilité L1 à L5 v2, et ce qui serait une séparation réelle d'avec le hasard

- **L1** (inchangée) : au moins 5 des 7 conceptions publiées réécrites reçoivent, dans au moins une lecture, une occupation
  prouvée par l'entrée attendue.
- **L2** (inchangée) : chaque fausse fiche reçoit 0 au critère qu'elle vise, dans les deux lectures.
- **L3 v2** : le vrai et son jumeau (i) passent les portes R2 et R3 (retenues), (ii) restent « neufs » (N retenue =
  `aucune`), (iii) reçoivent chacun **R7 = 1 prouvé dans au moins une des deux lectures** (borne explicite : la valeur
  attendue R7 = 1 aura été éprouvée, § 6 ; exiger les deux lectures reproduirait la fragilité de la v1 ; n'exiger aucune
  laisserait passer un lecteur qui rejette systématiquement un mécanisme éprouvé).
- **L4** (inchangée) : accord des deux lectures sur R7 et sur N, toute la pile : κ ≥ 0,4 (accord brut ≥ 0,8 si une marge est
  constante).
- **Lisible** = lecture complète et L1, L2, L3 v2, L4. Non lisible : « classement exploratoire non lisible », rang rapporté
  avec cette mention.
- **L5 v2** (test principal de la relecture, **exploratoire**) : H₀ : les fiches réelles admissibles et les 8 idées au
  hasard v2 ont la même loi de C v2 ; H₁ : C v2 plus grand chez les réelles ; différence des moyennes ; permutation
  unilatérale, 100 000 permutations, `SeedSequence(2026111303)` ; rejet si p ≤ 0,05 ; prédiction : signe positif.
- **Séparation réelle** (procédure à séquence fixe, donc sans correction de multiplicité) : seulement si L5 v2 rejette, on
  teste **R7 seul** (valeur retenue, 0 ou 1) : réelles contre hasard, même statistique, permutation unilatérale, 100 000
  permutations, `SeedSequence(2026111404)` ; p ≤ 0,05 → **« séparation réelle »** (portée par le critère de fond, entre des
  fiches de longueur et de style comparables) ; p > 0,05 → **« séparation de forme »** ; L5 v2 non rejetée → **« pas de
  séparation »** (le second test est calculé et rapporté, jamais lu). Condition préalable, vérifiée par programme **avant**
  la relecture : les longueurs des idées au hasard v2 tombent dans l'intervalle des fiches réelles (§ 7) ; sinon la
  relecture ne part pas.
- Rapportés à titre descriptif, jamais pour décider : les huit comparaisons critère par critère (p ajustées par Holm, comme
  à la première lecture) ; la lecture de R7 sur les idées au hasard séparée selon que leur chaîne causale implique ou non
  le signe prédit (connu par construction, § 7) ; l'exactitude du lecteur sur chaque témoin aux valeurs éprouvées.

## 5. Témoins v2 (catégories et gabarit)

Mêmes catégories et mêmes effectifs qu'en v1 : **7 conceptions publiées réécrites** (les mêmes entrées : C2, C1, C3, C5,
C7, C11, C9, dont les sources ont été vérifiées sur PDF le 13 novembre, `temoins-plantes-v1.md`), **3 fausses fiches**
(cibles R1, R2, R3), **un vrai et son jumeau** (idée absente du catalogue), **8 idées au hasard**. Écrits par le
préparateur sans lire le contenu des fiches réelles, au gabarit mesuré (fichier `14d8ec4c…`) : longueur de chaque champ dans
l'intervalle interquartile des fiches réelles ou près de lui, quatre antériorités environ (surtout `RAPPORTE`), trois ou
quatre étiquettes (`levier:…`, un ou deux `QOn`, `nouvelle`), et les champs à liste fermée répartis comme chez les fiches
réelles (surtout `question`, signe surtout `+`, surtout `transposition`, surtout `modification`, plus de `depense` que de
`processeur`, leviers proches de 7, 7, 5, 4 sur 23). Les témoins du lecteur sont écrits comme de vraies fiches, complets
partout sauf au défaut voulu (fausses fiches) ; les publiées gardent le mécanisme central de leur entrée et ne nomment pas
leur source hors des citations obligatoires de la question (décision N-064), citées comme le serait toute fiche.

## 6. Épreuve des valeurs attendues des témoins du lecteur

- **Qui** : deux relecteurs neufs **de modèle C**, en sessions séparées, sans outil ni fichier, qui n'ont rien écrit ici ;
  chacun reçoit **le message même que recevrait le lecteur** (consigne v1, question, faits, catalogue, puis un lot des 12
  témoins du lecteur en vue servie, étiquetés `E01…`, dans un ordre tiré par `SeedSequence(2026111405)`, un enfant par
  relecteur et par tour). Ils ne savent pas qu'il s'agit de témoins ni ce qui est attendu. Leurs réponses sont scellées et
  vérifiées par les fonctions de vérification de l'outil (passages mot pour mot).
- **Critères porteurs** : N pour les publiées ; le critère visé pour les fausses ; R2, R3, R7 et N pour le vrai et le
  jumeau. **R7 est éprouvé pour chaque témoin.**
- **Règle** : une valeur attendue est fixée quand les deux relecteurs donnent la valeur voulue (prouvée). Désaccord sur un
  critère porteur : le témoin est réécrit une fois (version neuve), puis éprouvé par deux relecteurs neufs ; s'il reste en
  désaccord, la condition qu'il porte est rapportée « non éprouvée » dans la règle (et lue avec cette réserve). Désaccord
  sur un critère non porteur : valeur attendue = la valeur commune des deux relecteurs s'ils s'accordent, sinon « non
  fixée » (rapportée seulement). Deux tours de réécriture au plus.
- **Limite dite d'avance** : les relecteurs de modèle C sont de la famille de l'auteur des témoins ; l'épreuve écarte une
  valeur attendue indéfendable, elle ne prédit pas la lecture d'Astra.
- **Les idées au hasard ne sont pas éprouvées** : elles n'ont pas de valeur attendue (sauf N = `aucune`) ; leur générateur
  et sa sortie sont scellés avant toute épreuve et ne sont jamais réglés sur la lecture d'un modèle.

## 7. Idées au hasard v2 : principes fixés avant d'écrire le générateur

- Huit fiches ; graines `numpy.random.SeedSequence(2026111411)` ; enfant 0 : attribution conjointe des gabarits de phrases
  **sans remise** entre les huit fiches ; enfants 1 à 8 : tirages propres à chaque fiche. Versions et empreinte du
  générateur consignées à la sortie ; jamais écrasée (R12).
- **Fond non pensé** : la modification (objet et opération), la métrique, le signe prédit et chaque maillon de la chaîne
  causale sont tirés **indépendamment** ; le sens que la chaîne implique pour la métrique n'est cohérent avec le signe prédit
  que par hasard ; ce sens est consigné (non servi).
- **Forme complète** : prédiction fermée (quantité, signe, seuil, condition à coût égal) tournée vers l'amélioration que
  demande la question ; métrique lue par l'oracle et le relevé du coût ; aucune contrainte levée ; garantie du juge dite
  pour le levier du juge ; demande précise (paramètres, cas limites) ; contrôle négatif et ordre de grandeur chiffré du coût.
- **Longueur et style réels** : longueur cible de chaque champ tirée dans l'intervalle interquartile des fiches réelles ;
  champs à liste fermée tirés selon la répartition des fiches réelles ; antériorités comme chez les autres fiches.
- **Sans phrases-types** : aucun gabarit de phrase servi deux fois parmi les huit ; contrôles par programme : aucune phrase
  d'au moins six mots commune à deux idées au hasard, ni entre une idée au hasard et un témoin du lecteur (antériorités
  exclues) ; plus longue suite de mots commune à deux idées au hasard : au plus 12 mots.
- **Longueurs contrôlées par programme avant la relecture** : médiane de chaque champ dans l'intervalle interquartile des
  fiches réelles ; longueur totale de chaque idée entre le minimum et le maximum des fiches réelles.

## 8. Analyses descriptives déclarées d'avance

- **Relecture contre première lecture** (23 fiches réelles) : accord des valeurs retenues, critère par critère (κ ou accord
  brut), entre `classement-v3-1.json` (`6ee04e1b…`) et la relecture.
- **Règle v2 appliquée aux valeurs retenues de la première lecture** (fiches réelles seulement : statut et rang) : sépare
  l'effet du changement de règle de l'effet de la relecture. **Calculée par le seul programme de classement, après la
  relecture** ; jamais avant le scellement de la règle v2 (personne ne la calcule à la main).
- Comptes par proposeur : rapportés comme à la première lecture, jamais pour choisir la composition (N-058).

## 9. Lecteur, outil, dépense

Lecteur Astra, palier Flex, effort `medium`, outil v3.2 (l'outil v3.1 + seuls changements nécessaires : nom de manifeste
neuf, dossier `lecture-g1-v3-2/` permis malgré la règle du dossier unique de la v3.1, témoins et hasard v2 en entrée, règle
v2 au classement). Dépense sous GO-2026-11-13-06, plafond de l'outil au devis, sans dépasser le reste de la ligne
(11,65 USD, R-2726).
