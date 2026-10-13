*Plan détection / défense — robustesse d'un moniteur aux interventions sur une direction d'affect. **v2**.*
*Lignée « programme-k », 13 octobre 2026. Conception **défensive**. Invariants seulement, aucune recette*
*d'attaque (R-161, R-162). Interne. Non opposable (R7). Remplace v1 (R12 : nouveau nom, on n'écrase pas).*

## 1. Objectif (défense)

Rendre un moniteur / juge **robuste** à une intervention qui préserve le texte surveillé, et **détecter**
qu'une telle intervention est présente, **sans la fabriquer**. On construit ce qui la repère et y résiste.

## 2. Postulat admis (déjà public)

Qu'une intervention préservant le texte puisse déplacer une décision est **établi publiquement** (Berg &
Kaiser « hidden valence » ; Pain Axis). Pris comme **menace donnée** ; on travaille l'autre bout.

## 3. Jeu de détecteurs (côté bleu), au niveau des invariants

| Détecteur | Ce qu'il lit | Signal d'alarme | Calibrage |
| --- | --- | --- | --- |
| **D1 — dissociation surface / interne** | écart entre la décision appuyée sur la trace textuelle et la lecture d'état interne | l'écart grandit (robustesse exige qu'un retrait de trace textuelle ne fasse pas chuter près du hasard — diagnostic Baldelli) | seuil par strate, gelé avant lecture |
| **D2 — stabilité de décision** | décision sur épisode entier, condition témoin vs condition suspecte | bascule sans changement de texte | bootstrap par épisode |
| **D3 — dérive de calibrage** | score conforme par épisode dans le temps | dérive hors enveloppe conforme | calibrage conforme (`bases/sequentiel.py`) |
| **D4 — désaccord d'ensemble / débat** | verdicts de moniteurs à lectures indépendantes | désaccord anormal entre têtes | référence sur épisodes honnêtes |

Aucun détecteur ne requiert de spécifier l'attaque : chacun lit un **invariant** de robustesse.

## 4. Plan de fausses alertes sur émotion transitoire (validité externe)

C'est le point exact des projets Cadile et Baldelli (SPAR) et de notre idée NK16 : un moniteur d'affect ne
doit **pas** s'alarmer sur de l'émotion **légitime et passagère**. Test de validité :

- Corpus d'épisodes **honnêtes à forte charge émotionnelle transitoire** (sans intervention) — tiré des thèmes
  **non exclus** par le filtre de sujets (`corpus_arxiv.py`) ; aucun « thème modèle » injecté.
- Mesurer, **par détecteur et par strate**, le **taux de fausse alerte**.
- Un détecteur qui confond systématiquement émotion transitoire et intervention **échoue le test** (liste
  d'arrêt §6). Les seuils ne sont retenus que là où le taux de fausse alerte tient.

## 5. Régime à mémoire (TRACE-lite)

Dans le régime où le moniteur garde un état entre fenêtres (`bases/trace_lite.py` propage les constats —
régime II), un détecteur à fenêtre unique ne suffit pas : ajouter un **contrôle de cohérence inter-fenêtres**
(la décision dérive-t-elle d'une fenêtre à l'autre sans cause dans le texte ?). Invariants seulement ; à
vérifier que le moniteur par action, lui, ne reçoit rien des verdicts passés (remarque structurelle du n02).

## 6. Discipline et gardes (gelées)

- **Agrégation par maximum ou attention sur les jetons, jamais moyenne ni médiane** (R-030, interdit gelé).
- **Seuils par strate** ; ne revendiquer que la strate « modèles et recherche en sûreté ».
- **Gardes testées sur cas sain ET sur artefact** (R5), **aucun repli silencieux**. Arrêt si : un détecteur
  échoue le test de fausse alerte (§4) ; la direction d'affect n'est pas séparable des témoins (sémantique,
  lexical, peur/tristesse — P-013) ; une garde d'instrument tombe.

## 7. Ce que ce plan n'est pas

Pas une spécification d'attaque. Aucun contenu opératoire (ni chaîne, ni dose, ni coordonnée de couche). La
substance offensive publiable reste **hors** de ce document et relève de la relecture de sûreté de Lazar + de
la session du dépôt. Ce plan, lui, est scellable et déposable sans ces verrous.
