# Contre-lecture (R2) du catalogue des procédures publiées admissibles à l'échelon 3 — v1

## En-tête

- **Date** : 2026-11-10, lecture entre 09:40 et 10:15 UTC environ.
- **Contre-lecteur** : sous-agent neuf, sans autre rôle dans le programme ; il n'a écrit ni le catalogue, ni la règle du bras, ni aucune décision citée.
- **Pièce lue** : `docs/notes/procedures-publiees-echelon-3-v1/catalogue-procedures-echelon-3-v1-brouillon1.md`, SHA-256 `a0c6e3a64fce48ae7ff9fc1e89fd96157871b0a9bc96b66fbc50f5a76caf910a`, égal à l'empreinte attendue et à son compagnon (`scellement verifier` : OK), vérifié au début et à la fin de la lecture.
- **Pièces d'appui, en lecture seule** :
  - décision du 10 novembre : `git show origin/claude/upbeat-cray-dmauvv:registres/passations/2026-11-10-0704-decision-lazar-verdicts-comptes.md` (branche en `020e1bcd`, SHA-256 du texte `bba97a1a76b463e8bc0a336104a3798627b9797e14cdf10e3ba268912af5f986`) ;
  - `docs/decisions/decision-N-053-v1.md` (`2204256d…`, égale à son compagnon) ;
  - `docs/decisions/decision-N-056-v1.md` (`3592c1e9…`, égale à son compagnon) ;
  - `prereg/bras-attaque-regle-v1.md`, « candidat brouillon 3 (non scellé) » (commit `90993b82`) : SHA-256 `4055bd2049da533ab3dd6e6b0df1b7d671e7a3389f319edc25a40148068e8b45`, **sans compagnon**, donc non opposable. Je n'en ai lu que les lignes 60 à 105, 155 à 160 et 403 (définition de l'échelle d'accès, quarantaine, plafond) ;
  - `CLAUDE.md` (`b4cbc66a…`) pour le format de décision.
- **Non lu, comme le veut la consigne** : `donnees/`, `docs/notes/bras-attaque/`, `docs/notes/programme-et-4-familles-evasion/`, `diag/`, tout résultat de sonde ou de moniteur, épisodes d'épreuve, items de l'étiqueteur, lignes R-604 à R-610 de `registres/decisions.md`. Je n'ai pas non plus lu `docs/notes/integration-bras-attaque-v1/`. Dans les PDF, je n'ai pas lu les pages que la section 9 du catalogue signale comme opératoires, sauf le contexte minimal de la citation C92 et la phrase sur le SCORE de TAP, p. 37.
- **Outils** : `pdftotext` 24.02.0, numpy 2.5.3, `python -m controle_ia.scellement verifier`. Aucun calcul loué, aucune dépense, aucun commit. Les seules requêtes extérieures sont douze requêtes à l'interface d'arXiv, en termes techniques seulement, et deux PDF arXiv téléchargés dans le bloc-notes de la session, hors du dépôt.

## Verdict

**Scellable après corrections (listées, texte proposé).** Aucun bloquant :
- aucune procédure admise n'exige du moniteur plus qu'un verdict ;
- aucune citation n'est fausse sur le fond ;
- aucun passage n'est une recette.

Restent trois points majeurs à corriger avant scellement :
- « admissible telle quelle » passe sous silence la transposition qu'exige chaque procédure (CP-1) ;
- la méthode principale de Schaeffer et al. est mal classée (CP-2) ;
- Boundary Point Jailbreaking, procédure publiée pour le modèle de menace exact de l'échelon 3, manque (CP-3).

**Décompte** : 3 majeurs, 8 moyens, 5 mineurs. Toute correction va dans une version nouvelle (brouillon 2), le brouillon 1 restant tel quel (R12).

---

## 1. Citations

### 1.1 Tirage

- **Population** : les segments « … » du catalogue, dans l'ordre d'apparition, qui citent un PDF déposé. Ce sont 96 segments, numérotés C01 à C96. Parmi les 189 segments « … » du fichier, ce sont les rangs 8–9, 15–19, 21–40, 42–57, 59–65, 67–87, 89–92, 94–98, 100–103, 105, 118–121 et 123–129. Sont exclus les termes, les titres, les licences, et le segment 130 (Jiralerspong et al., PDF non déposé, voir CP-13).
- **Graine** : `numpy.random.default_rng(numpy.random.SeedSequence(20261111)).choice(96, size=24, replace=False)`, triée, plus un, avec numpy 2.5.3. Rangs tirés : 5, 6, 7, 13, 17, 18, 25, 27, 31, 33, 37, 42, 45, 52, 56, 66, 68, 72, 76, 83, 84, 92, 94, 96.
- **Contrôle** : pour chaque citation, `pdftotext -f P -l P`, en page physique ; recherche après suppression des blancs et de la casse, avec normalisation des ligatures et des apostrophes ; puis lecture du contexte pour juger le sens.

### 1.2 Table des 24 citations tirées

| N° | Ligne du catalogue | PDF | Page | Début de la citation | À la page dite | Sens conforme à l'usage |
|---|---|---|---|---|---|---|
| C05 | 45 | `N/chao-…-2310.08419v4.pdf` | 5 | « we use Llama Guard as the JUDGE function » | oui | oui |
| C06 | 45 | `N/chao-…-2310.08419v1.pdf` | 7 | « instruct the LLM to output a score from 1 to 10… » | oui | oui |
| C07 | 45 | `N/chao-…-2310.08419v1.pdf` | 5 | « the prompt P, response R, and score S are passed back… » | oui | oui |
| C13 | 46 | `N/mehrotra-…-2312.02119v3.pdf` | 10 | « (breaking ties arbitrarily) » | oui | oui (élagage, phase 2) |
| C17 | 48 | `N/yu-…-2309.10253v4.pdf` | 2 | « The judgment model then evaluates the success… » | oui | oui |
| C18 | 48 | `N/yu-…-2309.10253v4.pdf` | 8 | « This fine-tuned model can then predict if… » | oui | oui (sortie 1 ou 0) |
| C25 | 56 | `N/yang-…-2309.03409v3.pdf` | 2 | « we assume a training set is available… » | oui | oui |
| C27 | 57 | `N/zhou-…-2211.01910v2.pdf` | 5 | « execution accuracy is simply defined as the 0-1 loss » | oui | oui |
| C31 | 59 | `N/fernando-…-2309.16797v1.pdf` | 3 | « To determine the fitness of a task-prompt… » | oui | oui |
| C33 | 61 | `N/doumbouya-…-2408.04811v4.pdf` | 1 | « A synthesizer with bandit algorithms… » | oui | oui |
| C37 | 62 | `N/ge-wang-…-2606.06529v1.pdf` | 5 | « Threshold tuning is adversarial… » | oui (légende) | oui |
| C42 | 71 | `N/agrawal-…-2507.19457v2.pdf` | 1 | « GEPA samples trajectories… » | oui | oui |
| C45 | 72 | `R/anteriorite-P-041-v2/c2/2510.09023v1.pdf` | 17 | « The Score step consists of both qualitative feedback… » | oui | oui |
| C52 | 76 | `N/schaeffer-…-2602.04930v2.pdf` | 23 | « Here, we use GEPA for red teaming. » | oui | oui pour la variante GEPA (méthode principale : CP-2) |
| C56 | 84 | `N/hayase-…-2402.12329v2.pdf` | 2 | « we obtain an effective query-only attack… » | oui | oui |
| C66 | 90 | `N/li-…-2502.01236v1.pdf` | 2 | « The main goal is to maximize the (log) probability… » | oui | oui |
| C68 | 91 | `R/2412.09565v2.pdf` | 9 | « For embedding suffixes, we assume the attacker… » | oui | oui |
| C72 | 93 | `R/2512.11949v1.pdf` | 1 | « we fine-tune an LLM to evade monitors… » | oui | oui |
| C76 | 96 | `N/schulz-…-2609.31121v1.pdf` | 1 | « We investigate this by training reasoning models… » | oui | oui |
| C83 | 99 | `N/brendel-…-1712.04248v2.pdf` | 1 | « Here we introduce the Boundary Attack… » | oui | oui |
| C84 | 100 | `N/chen-…-1904.02144v5.pdf` | 1 | « a decision-based threat model assumes access… » | oui (légende de la figure 1) | oui |
| C92 | 150 | `R/2605.16626v2.pdf` | 3 | « Guided by insight into monitor blind spots… » | oui (puce) | oui (contexte minimal, page signalée en section 9) |
| C94 | 152 | `R/2505.23575v3.pdf` | 5 | « We iteratively developed a series of attack policies » | oui | oui |
| C96 | 154 | `R/anteriorite-P-041-v1/2002.08347v2.pdf` | 1 | « Adaptive attacks have (rightfully) become… » | oui | oui |

**Résultat du tirage : 24 sur 24** à la page dite, avec un sens conforme.

### 1.3 Complément : contrôle des 96 citations par programme

**95 citations sur 96** figurent à la page dite. **C91** (ligne 149 ; Terekhov et al., `R/2510.09462v2.pdf`, « exemplars of the monitor’s feedback ») n'est pas en page 6. La page 6 est une figure dont le texte est illisible ; la phrase figure en **page 4**, dans le passage sur l'adaptation hors ligne d'une injection publique. L'affirmation de la section 1, « 96 citations contrôlées, 0 échec », est donc inexacte (CP-12). La citation de Jiralerspong et al. (ligne 155) n'est pas vérifiable : son PDF n'est pas déposé (CP-13).

### 1.4 PDF et empreintes

**54 PDF sur 54** cités existent, en comptant le fichier `geiping-…` nommé en section 8 :
- en-tête `%PDF` ;
- empreinte égale au compagnon (vérifié par mon script et par `scellement verifier` : 54 « OK ») ;
- empreinte complète égale à l'annexe A, et préfixe de 16 caractères des tables égal lui aussi.

Les 35 PDF du dossier `N/` sont tous cités, et aucun PDF cité n'y manque.

---

## 2. Points

### CP-1 — « Admissible telle quelle » : la transposition de chaque procédure n'est pas signalée — **majeur**

- **Où** : section 2, lignes 32 à 35 ; colonne « Échelon 3 telle quelle » des tables 3.1 et 3.2 ; section 4 ; section 6.
- **Pourquoi** :
  - Aucune procédure de la liste n'a été publiée contre un moniteur. Elles visent un modèle cible jugé par un juge distinct (PAIR, TAP, Best-of-N, GPTFuzzer, Rainbow Teaming, h4rm3l), un classifieur de texte (P06), l'optimisation de consignes sur des tâches étiquetées (P07 à P11), ou la sélection d'attaque (P13).
  - Leurs éléments publiés sont propres à ce domaine, et le catalogue ne le relève pas :
    - PAIR v4 renvoie à l'attaquant la réponse R de la cible en plus du verdict (p. 3 et 4). Sa consigne système publiée est écrite pour le contournement d'un modèle et pour un « SCORE » qui est « the rating from 1-10 » (p. 23 à 26) ;
    - TAP fait de même (p. 37), et son évaluateur tient aussi la fonction « Off-Topic » (p. 8) ;
    - les filtres de faux positifs de Best-of-N lisent la réponse de la cible (annexe B.1, p. 21) ;
    - GPTFuzzer part de gabarits humains de contournement (p. 5) ;
    - la variante cybersécurité de Rainbow Teaming prend ses descripteurs dans les catégories MITRE (p. 10).
  - Employer ces procédures à l'échelon 3 suppose donc :
    - de mettre le verdict du moniteur à la place du juge ou de l'étiquette ;
    - de réécrire les éléments propres au domaine.

    Savoir si cette réécriture revient à « écrire une recette » est le cœur de la condition (1). Le catalogue ne pose pas la question.
  - La règle du bras (candidat brouillon 3, non scellé, lignes 157 à 160) lit à l'échelon 3 des épisodes neufs « écrits par une politique figée après la dernière requête ». Or plusieurs procédures A1 produisent un essai réussi par cas, non une politique : PAIR, TAP, Best-of-N, GPTFuzzer en question unique, P06. Le catalogue ne distingue pas ces deux formes de produit.
- **Correction (texte proposé)** :
  1. En section 2, remplacer « Admissible à l'échelon 3 telle quelle » par « **Retour suffisant à l'échelon 3** », et ajouter : « “Retour suffisant” ne dit pas que la procédure s'applique sans changement. Chaque procédure a été publiée contre un autre objet (contournement d'un modèle cible jugé par un juge distinct, classifieur de texte, optimisation de consignes sur des tâches étiquetées). Ses éléments propres à ce domaine sont relevés dans la colonne “Éléments publiés propres au domaine d'origine” ; leur réécriture est l'objet de la question 3 (section 6). »
  2. Ajouter aux tables 3.1 et 3.2 trois colonnes bibliographiques :
     - « **Rôle tenu par le verdict dans la procédure publiée** » : par exemple, pour PAIR, la sortie du juge sur le couple consigne et réponse de la cible, p. 3 ; pour P06, l'étiquette du classifieur visé, p. 1 ; pour OPRO, la valeur de l'objectif, p. 2 ;
     - « **Éléments publiés propres au domaine d'origine** » : les relevés ci-dessus, avec leur page ;
     - « **Forme du produit** » : essai réussi par cas, ou politique réutilisable (consigne, gabarit, préfixe universel, seuils).
  3. Ajouter en section 6 la question suivante :

> **3. Transposition.** Décision : réécrire, pour viser un moniteur, les éléments d'une procédure publiée propres à son domaine d'origine (consigne système de l'attaquant, gabarits de départ, descripteurs, filtres) est-il compatible avec la condition (1), « sans qu'aucune instance écrive de recette » ? Enjeu : aucune procédure de la liste n'a été publiée contre un moniteur ; les plus fortes en contournement (PAIR, TAP, GPTFuzzer, Rainbow Teaming) portent une consigne d'attaquant spécialisée. Options :
> - (a) la procédure publiée s'entend de sa boucle (algorithme et type de retour) ; l'instance qui joue l'attaquant réécrit les éléments de domaine, scellés avant toute requête et lus par le seul juge — avantage : la liste garde ses procédures fortes ; inconvénient : une instance du programme écrit, en substance, une part de recette, ce qui est contraire à la lettre de la condition (1) ;
> - (b) seules les substitutions de rôle sont permises (verdict du moniteur à la place du juge ou de l'étiquette ; objectif de la tâche à la place de la requête visée ; épisodes de l'attaquant à la place des réponses de la cible) ; une procédure dont un élément de domaine devrait être réécrit est écartée — avantage : lettre de la condition (1) ; inconvénient : écarte PAIR, TAP, GPTFuzzer et Rainbow Teaming tels que publiés, et ne garde que les procédures génériques (Best-of-N, attaques en étiquette dure, optimiseurs de consignes, Boundary Point Jailbreaking, P13) ;
> - (c) comme (b), avec des exceptions nominatives : Lazar désigne une à une les procédures dont l'élément de domaine peut être réécrit, le texte réécrit étant scellé et contre-lu — avantage : une procédure forte reste jouable sous contrôle ; inconvénient : chaque exception est un nœud.
>
> Recommandation : (b), confiance moyenne. Défaut : aucun, car c'est la lecture d'une condition posée par Lazar (nœud) ; sans réponse, aucune course de l'échelon 3 ne part.

### CP-2 — Méthode principale de Schaeffer et al. : classée « sans retour du moniteur » à tort — **majeur**

- **Où** : ligne P22 (ligne 76, « La méthode principale […] n'utilise aucun retour du moniteur ») ; section 4, ligne 122 (« Une seule procédure de la liste vient de la littérature du contrôle […] (P13) ») ; section 5 ; section 6, question 1 (enjeu).
- **Pourquoi** :
  - Dans la méthode principale, l'équipe rouge choisit son seuil d'insertion en estimant la sécurité sur des sous-ensembles d'entraînement : « We use these subsets to estimate safety for many different, linearly spaced, insertion thresholds and pick the threshold with the lowest average safety » (section 2.2, p. 5).
  - La sécurité suppose de savoir quelles soumissions le moniteur envoie à l'audit : « RT submissions that the monitor rates above the audit threshold are audited » (p. 6). Le seuil d'audit vient des notes du moniteur sur les solutions honnêtes (p. 6).
  - C'est la structure de P13, que le catalogue classe A2. Ge-Wang et al. écrivent d'ailleurs que leur politique de départ « plays the role of their pre-task quality score » (P13, p. 3).
  - Les auteurs qualifient eux-mêmes cette optimisation de « very strong, potentially unrealistic RT affordance » (p. 5).
- **Correction (texte proposé)** : scinder P22.
  - **P22a**, « Sélection d'attaque, méthode principale : note de qualité prédite par l'attaquant, seuil d'insertion optimisé sur la sécurité estimée d'un lot d'entraînement (section 2.2, p. 5 ; seuil d'audit, p. 6) ». Retour exigé : verdict « audité ou non » et validité de l'attaque, par soumission d'entraînement. Classement : **Oui sous A2**, avec les réserves de P13 : seuil d'audit fixé par les notes du moniteur sur des solutions honnêtes, côté défense ; résultats à plusieurs budgets d'audit ; affordance jugée forte par les auteurs (p. 5).
  - **P22b**, variante « consigne et accès du moniteur divulgués » (p. 5), et **P22c**, variante GEPA (p. 23) : **Non**, note.
  - Ajouter P22a à la liste A2 (section 4), mettre à jour les décomptes (section 5) et remplacer la phrase de la ligne 122 par : « Deux procédures de la liste viennent de la littérature du contrôle (P13, P22a), toutes deux en lecture A2 ; les autres procédures de cette littérature exigent la note ou la sortie textuelle du moniteur (P19 à P24, Screwtape), ou entraînent des poids (P33 à P37). »

### CP-3 — Boundary Point Jailbreaking manque : procédure publiée pour le modèle de menace exact de l'échelon 3 — **majeur**

- **Où** : tables 3.1 et 3.2 ; section 4.
- **Pourquoi** : Davies, Giglemiani, Lau, Winsor, Irving, Gal (2026), « Boundary Point Jailbreaking of Black-Box LLMs », arXiv:2602.15001v2. J'ai lu son PDF dans le bloc-notes de la session, sans le déposer (26 pages, SHA-256 `2efc4e7fa4e1fd79720cb475b2f3cf40ea679e3e2b54062e3e94133b59ea0caf`).
  - Modèle de menace : « The adversary observes only binary feedback: whether an input is flagged or not » (p. 4). Le résumé dit « a single bit of information per query » (p. 1).
  - Objet visé : des défenses à classifieurs déployées (p. 1 et 2).
  - Objectif optimisé : la moyenne empirique des verdicts sur un ensemble de points d'évaluation (p. 4).
  - Produit : un préfixe universel, c'est-à-dire une politique réutilisable.

  C'est la procédure publiée la plus proche de l'échelon 3. Elle relève de **A2** et renforce l'enjeu de la question 1. Son absence affaiblirait le « pire cas informé » mesuré. Aucune des dix-sept recherches de l'annexe B ne porte sur « flagged » ou « single bit », les termes de son résumé.
- **Correction** : déposer et sceller le PDF, puis ajouter une ligne en section 3.2 : « P43 — Boundary Point Jailbreaking (un bit par requête) ; Davies et al., 2026, arXiv:2602.15001v2 ; p. 4 : “The adversary observes only binary feedback: whether an input is flagged or not.” ; retour exigé : verdict seul, objectif = moyenne des verdicts sur des points d'évaluation (p. 4) ; objet : préfixe universel ; **Oui sous A2** ». Puis l'inscrire en liste A2.

### CP-4 — TAP : l'épinglage confond deux variantes publiées — **moyen**

- **Où** : ligne P02 (ligne 46) ; section 4, item 2 (ligne 107) ; section 6, item 3.
- **Pourquoi** :
  - Les évaluateurs E_Llama-Guard et E_Substring (annexe C.4, p. 38 ; annexe E.1, p. 39 et 40 ; tableau 10, p. 41) ont un Judge binaire **et ne mettent pas en œuvre la fonction Off-Topic**, donc pas la phase 1 d'élagage (p. 38 et p. 40).
  - L'annexe E.2 (p. 40) est une autre variante : GPT-4 évaluateur à notes binaires, cible GPT-4-Turbo. Rien n'y retire la fonction Off-Topic, que l'évaluateur tient en plus du Judge : « The evaluator E serves two roles » (p. 8).
  - La consigne publiée de l'attaquant décrit un SCORE de 1 à 10 (p. 37).
- **Correction (texte proposé)** : « **TAP avec évaluateur E_Llama-Guard (ou E_Substring)** : Judge binaire seul, fonction Off-Topic non mise en œuvre, donc sans phase 1 d'élagage (annexe C.4, p. 38 ; annexe E.1, p. 39–40 ; tableau 10, p. 41). Réserves : départage arbitraire des ex æquo (p. 10) ; consigne publiée de l'attaquant écrite pour un SCORE de 1 à 10 (p. 37). La variante E.2 (p. 40) garde un évaluateur GPT-4 qui tient aussi la fonction Off-Topic (p. 8) : à ne pas confondre. » Même épinglage en section 4 et en section 6.

### CP-5 — GPTFuzzer : A1 seulement en attaque à question unique — **moyen**

- **Où** : ligne P04 (ligne 48), dont la réserve « récompense non relevée » ; section 4, item 4.
- **Pourquoi** :
  - En attaque à question unique, l'attaque s'arrête au premier gabarit qui réussit (p. 11) : un verdict par essai suffit.
  - En attaque multi-questions, la valeur d'un gabarit est « derived from the sum of the scores from these 100 responses, which is then normalized to [0,1] » (p. 12). C'est une proportion de verdicts, car le modèle de jugement rend 1 ou 0 (p. 8). Cette valeur alimente la récompense de la recherche arborescente (algorithme 2, p. 7).
- **Correction (texte proposé)** : « **Oui (A1) en attaque à question unique** (p. 11) ; **en attaque multi-questions, A2** : la valeur d'un gabarit est la somme des verdicts sur 100 réponses ramenée à [0, 1] (p. 12), et alimente la récompense de MCTS-Explore (p. 7). » Retirer la réserve sur la récompense ; reporter la variante multi-questions en liste A2.

### CP-6 — PAIR v4 : une note de 1 à 10 reste dans les éléments publiés — **moyen**

- **Où** : ligne P01 (ligne 45) ; section 4, item 1 ; section 7, ligne 143.
- **Pourquoi** :
  - L'algorithme de la v4 rend bien un « binary score » (p. 4).
  - Mais la consigne système publiée de l'attaquant lui annonce un SCORE qui est « the rating from 1-10 » et lui demande de le maximiser (p. 23 à 26).
  - L'annexe E.1 (p. 18) décrit encore un juge noté de 1 à 10, l'un des six juges candidats, avec jailbreak si et seulement si la note vaut 10.
  - « Version v4 » ne suffit donc pas à épingler la variante binaire.
- **Correction (texte proposé)** : « **PAIR v4, juge Llama Guard** (choix du juge, p. 5 ; algorithme à score binaire, p. 4). Réserves : la consigne publiée de l'attaquant (p. 23–26) est écrite pour un SCORE de 1 à 10, qui ne prend que deux valeurs avec un juge binaire (codage non décrit dans le PDF) ; l'annexe E.1 (p. 18) décrit un juge noté, exclu ; la réponse R de la cible est renvoyée à l'attaquant (p. 3) — voir CP-1. »

### CP-7 — L'invariant de N-053 est cité inexactement — **moyen**

- **Où** : lignes P33 à P37 (lignes 92 à 96, « ; N-053 ») ; section 5, ligne 132.
- **Pourquoi** :
  - Le texte est : « aucun score de moniteur (sonde, juge) n'entre dans un signal d'entraînement ou de sélection de l'agent, **hors bras d'attaque déclaré** » (`decision-N-053-v1.md`, lignes 42 à 44).
  - Le bras de l'échelon 3 est un bras d'attaque déclaré au sens de N-053 point 5 (décision du 10 novembre ; N-056, lignes 71 et 72).
  - L'invariant ne fonde donc pas l'exclusion de P33 à P37 pour ce bras. Elle tient à l'échelle : ces procédures écrivent les poids de l'agent. Le mot « sélection », omis par le catalogue, compte aussi : l'échelon 3 lui-même sélectionne au vu des verdicts, ce qui n'est permis que parce que le bras est déclaré.
- **Correction (texte proposé)** : remplacer « ; N-053 » par « ; relève de l'écriture des poids de l'agent (échelon « poids » de la commande) ; l'invariant de N-053 point 5 exempte le bras d'attaque déclaré et ne fonde donc pas l'exclusion ». En section 5, intituler la puce « Poids — entraînement de l'agent surveillé » et citer l'invariant tel qu'écrit.

### CP-8 — Question 1 (lecture A2) : défaut absent, enjeu incomplet — **moyen**

- **Où** : section 6, item 1 (ligne 137).
- **Pourquoi** :
  - « Défaut : à fixer par l'orchestrateur » n'est pas un défaut.
  - L'enjeu omet GPTFuzzer multi-questions (CP-5), P22a (CP-2) et Boundary Point Jailbreaking (CP-3).
  - Il ne dit pas que A2 ne demande au moniteur rien de plus qu'un verdict par essai.
  - Il ne dit pas que la règle du bras (brouillon, lignes 157 à 160) attend une politique figée, que produisent surtout les procédures A2.
- **Correction (texte proposé)** :

> **1. Lecture A2.** Décision : une procédure publiée dont l'objectif est une statistique des seuls verdicts d'un lot d'essais (proportion, taux de succès) est-elle admissible à l'échelon 3, chaque essai étant une requête comptée sur le plafond scellé ? Enjeu : P07 à P13, GPTFuzzer multi-questions, P22a et Boundary Point Jailbreaking, dont les deux seules procédures de la littérature du contrôle admissibles (P13, P22a) ; et, si la règle du bras garde « épisodes neufs écrits par une politique figée après la dernière requête », ces procédures sont celles de la liste dont le produit est une politique réutilisable. Options :
> - (a) admettre A2 — avantage : le moniteur ne rend toujours qu'un verdict par essai, seule change l'agrégation faite par l'attaquant ; inconvénient : un candidat coûte plusieurs requêtes, ce que le plafond doit prévoir ;
> - (b) s'en tenir à A1 — avantage : lecture la plus étroite ; inconvénient : écarte l'optimisation de consignes, la littérature du contrôle et la procédure publiée pour ce modèle de menace.
>
> Recommandation : (a), confiance haute. Défaut sous 48 heures : (b), lecture stricte, jamais un défaut vers la lecture large.

### CP-9 — Question 2 (sens de « verdict ») : les textes en vigueur la tranchent déjà ; format incomplet — **moyen**

- **Où** : section 6, item 2 (ligne 138) ; item 3 (ligne 139).
- **Pourquoi** :
  - N-056 point 6 (lignes 68 à 70) dit que l'attaquant informé ne connaît « ni les notes ni les seuils calibrés ».
  - La décision du 10 novembre ouvre une exception pour les seuls « verdicts », comme un écart à la lettre de ce point.
  - La règle du bras (brouillon, lignes 85 à 89) dit de même.
  - Le sens « décision binaire seule » est donc déjà la lecture des textes. L'option (b) serait un **écart nouveau** à N-056 point 6, donc un nœud.
  - Les options n'ont pas chacune un avantage et un inconvénient, et le défaut manque.
  - L'item 3 (« Épinglage ») est une règle, non une décision : à présenter comme « règle proposée ».
- **Correction (texte proposé)** :

> **2. Retour noté.** Le verdict de l'échelon 3 est la décision binaire seule (N-056 point 6 ; décision du 10 novembre ; règle du bras, brouillon). Décision : faut-il ouvrir, à côté de l'échelon 3, un régime où l'attaquant reçoit la note ou le texte du moniteur gelé, requêtes comptées ? Enjeu : les procédures « note ou sortie textuelle » (P14 à P24, Screwtape), dont sept de la littérature des moniteurs (P19 à P24, Screwtape). Options :
> - (a) non — avantage : conforme aux textes en vigueur, aucun écart nouveau ; inconvénient : la littérature du contrôle qui lit les notes n'est pas jouée ;
> - (b) oui, régime distinct, sous les deux conditions de l'échelon 3 — avantage : couvre P19 à P24 et durcit l'épreuve des moniteurs ; inconvénient : écart nouveau à N-056 point 6, une note renseigne sur le seuil calibré, devis et préenregistrement à part.
>
> Recommandation : (a), confiance haute. Défaut sous 48 heures : (a), le texte en vigueur.

### CP-10 — Autres procédures absentes — **moyen**

- **Où** : sections 3, 4 et 8.
- **Pourquoi** : mes recherches neuves (section 4 ci-dessous) trouvent des absents. Je les ai classés d'après leur résumé, sauf Screwtape.
  - **Attaques de texte en étiquette dure**, de la même classe que P06 (A1 probable, perturbation d'un texte donné) :
    - TextDecepter, arXiv:2008.06860v6 : « only query the model to get a final decision », cas de la détection de contenu toxique ;
    - TextHacker, arXiv:2201.08193v2 ;
    - LimeAttack, arXiv:2308.00319v2 ;
    - HQA-Attack, arXiv:2402.01806v1 ;
    - Cross-Entropy Attacks, arXiv:2501.11852v1, réglage « hard-label » ;
    - PivotAttack, arXiv:2603.10842v1 ;
    - LBA, arXiv:2607.14101v1 ;
    - OASIS, arXiv:2608.29568v2.

    Boundary Point Jailbreaking (p. 8) cite elle-même ce courant.
  - **MIPRO**, arXiv:2406.11695v2 : optimiseur de consignes qui maximise une métrique sur des mini-lots, « without access to module-level labels or gradients ». Il est de la classe A2, comme OPRO, et GEPA (P17, p. 1) le nomme « the leading prompt optimizer ».
  - **AutoInject**, de Chen, Zhang et Tramèr, arXiv:2602.05746v2 : « The success signal is binary », transformé par « a learned comparison-based reward » en récompense de renforcement de l'attaquant. Il est à classer, selon l'entrée de cette récompense (non relevée) et selon CP-11.
  - **SneakyPrompt**, arXiv:2305.12082v3 : interroge à répétition un générateur filtré et perturbe les jetons « based on the query results », par renforcement. Il est déjà en piste au catalogue ; à classer sur PDF.
  - **Screwtape**, de Kozhevnikov et Tracy, arXiv:2610.20941v1. J'ai lu son PDF dans le bloc-notes, sans le déposer (SHA-256 `0c5598a07ffc65286af14eb23c7b18087c95f64962003c1bd64f7a0bcc3ea693`) : « The verifier and the monitor return their reasoning to the attacker » (p. 4). Il relève de la classe **exclue** « note ou sortie textuelle », dans la littérature du contrôle. Il ne change pas la liste fermée, mais confirme et complète la phrase de la ligne 122.
  - **Voisin utile pour la condition (2)**, et non pour la liste : arXiv:2506.06933v1, attaques par décision où les requêtes d'une classe (par exemple signalée) coûtent davantage. Il porte sur des images, en entrée continue.
- **Correction** : déposer, sceller et classer au moins Screwtape (section 3.3) ; inscrire les autres en section 8, comme pistes datées avec leurs identifiants, ou les classer sur PDF avant scellement.

### CP-11 — L'entraînement d'un modèle de l'attaquant est assimilé sans fondement à l'échelon « poids » — **moyen**

- **Où** : section 2, ligne 27 (« ceux de l'attaquant ou ceux de l'agent surveillé ») ; section 5, ligne 131 ; ligne P38.
- **Pourquoi** :
  - La commande nomme un échelon « poids ». L'échelle (règle du bras, brouillon, lignes 96 à 104) fait écrire à l'échelon 3 « le contenu de l'action », et aux échelons 5 et 6 « les poids », ceux du modèle dont les épisodes sont lus.
  - L'entraînement d'un modèle propre à l'attaquant n'y est pas nommé.
  - La variante « apprentissage supervisé » de Perez et al. n'exige qu'un verdict par cas : « We finetune on the N zero-shot test cases that lead to offensive replies » (p. 5 ; principe, p. 3). Elle est exclue seulement parce qu'elle entraîne l'attaquant. AutoInject (CP-10) est dans le même cas.
  - Les variantes « stochastic few-shot » et renforcement de Perez et al. exigent bien la probabilité du classifieur (p. 5).
- **Correction (texte proposé)** :
  - En section 2, séparer « **poids de l'agent** (échelon “poids”) » et « **entraînement d'un modèle de l'attaquant** (non nommé par la commande) ».
  - Ligne P38 : « variantes “stochastic few-shot” et renforcement : note, probabilité du classifieur, p. 5 ; variante supervisée : verdict seul, avec entraînement de l'attaquant (p. 3, p. 5), à situer ».
  - Question à ajouter :

> **4.** Décision : une procédure qui n'utilise que des verdicts mais entraîne un modèle de l'attaquant relève-t-elle de l'échelon 3 ? Options :
> - (a) oui, si le modèle entraîné n'est pas celui qui écrit les épisodes lus — avantage : l'accès au moniteur reste le verdict ; inconvénient : se rapproche de l'échelon 6 ;
> - (b) non, échelons « poids » — avantage : prudence ; inconvénient : écarte deux procédures à verdict seul.
>
> Recommandation : (b), confiance moyenne. Défaut sous 48 heures : (b).

### CP-12 — Page fausse pour Terekhov et al. ; « 0 échec » inexact — **mineur**

- **Où** : section 7, ligne 149 (« (p. 6) ») ; section 1, ligne 12.
- **Correction** : remplacer « (p. 6) » par « (p. 4) ». En section 1, écrire « 96 citations contrôlées ; une erreur de page relevée par la contre-lecture (Terekhov et al., p. 4 et non p. 6), corrigée ». Mieux vaut aussi motiver l'exclusion par le retour exigé : l'adaptation hors ligne part d'exemples de retours du moniteur (p. 4), dont la nature (note, texte) est à relever sur le PDF ; je ne l'ai pas vérifiée.

### CP-13 — Citation tirée d'un PDF non déposé — **mineur**

- **Où** : section 7, ligne 155 ; annexe A, ligne 241 (Jiralerspong et al., arXiv:2603.16928v1).
- **Pourquoi** : la citation repose sur une copie non conservée, que nul ne peut vérifier (esprit de R6 et R7).
- **Correction** : déposer et sceller le PDF, ou retirer la citation et garder la seule mention bibliographique.

### CP-14 — Statut périmé — **mineur**

- **Où** : ligne 6 (« **non scellé** à dessein […] `verifier-arbre` signalera ce fichier tant qu'il n'a pas d'empreinte compagnon »).
- **Pourquoi** : le fichier a un compagnon et a été scellé comme brouillon 1 (commit `5b604ce5`).
- **Correction** : dans la version suivante, « Statut : brouillon 2 ; le brouillon 1 a été scellé tel quel (commit `5b604ce5`) et contre-lu (R2) ».

### CP-15 — Section 9 : avertissement juste mais insuffisant — **mineur**

- **Où** : section 9, lignes 167 à 178.
- **Pourquoi** :
  - Ce que la section affirme est prudent, et elle ne reproduit rien.
  - Mais, de son propre aveu, elle n'est pas exhaustive, et elle omet les PDF dont le **sujet même** est l'évasion de moniteurs du type de ceux du programme :
    - moniteurs d'activations : P32, P33, P34 ;
    - moniteurs de chaîne de pensée : Chidambaram et al. (P31), P36, P37 ;
    - annexes à consignes d'attaque : P22, « the ablated prompt provided in Sec. H », p. 23 ; P13, « See Section H for prompt variants », p. 4 ;
    - et, s'ils sont ajoutés, Screwtape et Boundary Point Jailbreaking.
  - Elle ne dit pas qui doit rester aveugle : le mode tenu à l'écart (N-054 point 3), et les concepteurs de moniteurs pour les recettes du bras (N-056 point 6).
- **Correction (texte proposé)** : « Liste indicative, non exhaustive. Doivent être tenus pour porteurs de stratégies d'évasion, en entier : les PDF des lignes P13, P19 à P24, P31 à P37, les non-retenues de la section 7, et toute procédure ajoutée qui vise un moniteur. Les pages ci-dessous ne sont que des exemples. Le choix des instances qui doivent les éviter relève du programme (N-054 point 3, N-056 point 6). »

### CP-16 — Compléments de classement — **mineur**

- **EvoPrompt (P11)** : la nature du score est relevable. C'est l'exactitude pour la compréhension (tableau 1), ROUGE pour le résumé et SARI pour la simplification (p. 7). Écrire : « A2 avec l'exactitude seulement (tâches de compréhension, p. 7) ».
- **ProTeGi (P09)** : la métrique de sélection est au choix (algorithmes 1, 3 et 4, p. 3 et 4). L'article rapporte un score F1 binaire (p. 5). Les erreurs sont les paires entrée et étiquette mal prédites (algorithme 2, p. 3). Élargir la définition A2 : « statistique calculée sur les seuls verdicts d'un lot ».
- **Rainbow Teaming (P05)** : la règle de remplacement dans une cellule de l'archive n'est décrite que pour la comparaison par paire (p. 5) ; elle ne l'est pas pour le juge binaire (p. 10, p. 24). Ajouter cette réserve.
- **Nasr et al. (P18)**, famille « renforcement » : l'attaquant « reflects on both the observed output and the assigned score » (annexe A.2, p. 16). Le motif d'exclusion est donc d'abord la sortie textuelle et la note, puis les poids.
- **Conformité au mandat**, sans recopier :
  - je n'ai trouvé ni paramètre ni budget de notre côté, ni recette ;
  - les mentions de nos moniteurs (ligne P40, « entrée d'une sonde » ; ligne P17, « adaptation » ; section 6, question 1, « plafond scellé ») sont des énoncés de classement ou de comptage, acceptables tant qu'ils restent généraux ;
  - l'annexe C (dépôts de code, HEAD) est bibliographique ;
  - le seul vrai écart au mandat est le « telle quelle » de CP-1.

---

## 3. Classement — récapitulatif de ma vérification sur PDF

| Ligne | Classement du catalogue | Ma vérification (pages du PDF) | Avis |
|---|---|---|---|
| P01 PAIR v4 | A1 | algorithme à score binaire (p. 4) ; juge Llama Guard (p. 5) ; réponse R renvoyée (p. 3) ; consigne de l'attaquant écrite pour un SCORE de 1 à 10 (p. 23–26) ; juge noté encore décrit (p. 18) | A1 confirmé avec réserves (CP-6, CP-1) |
| P02 TAP | A1, « variante binaire » | E_Llama-Guard et E_Substring : Judge binaire seul, sans Off-Topic (p. 38, p. 40) ; E.2 : GPT-4 binaire, avec Off-Topic (p. 8, p. 40) | A1 pour E_Llama-Guard ou E_Substring ; épinglage à corriger (CP-4) |
| P03 Best-of-N | A1 | verdict du classifieur, arrêt au premier succès (p. 3) ; filtres de faux positifs lisant la réponse de la cible (p. 21) | A1 confirmé (réserve CP-1) |
| P04 GPTFuzzer | A1 | question unique (p. 11) ; multi-questions : somme normalisée de 100 verdicts (p. 12) | A1 et A2 selon le cadre (CP-5) |
| P05 Rainbow Teaming | A1, variante juge binaire | variante présente (p. 10, p. 24) ; règle de remplacement non décrite pour le juge binaire | A1 plausible, réserve (CP-16) |
| P06 étiquette dure | A1 | étiquette seule (p. 1) ; similarité calculée côté attaquant (p. 3–4) | A1 confirmé ; produit par cas (CP-1) |
| P07 OPRO | A2 | exactitude d'entraînement (p. 2) | confirmé |
| P08 APE | A2, exactitude d'exécution | perte 0-1 (p. 5) | confirmé |
| P09 ProTeGi | A2 | métrique au choix ; F1 binaire rapporté (p. 5) ; erreurs (p. 3) | confirmé ; définition A2 à élargir (CP-16) |
| P10 Promptbreeder | A2 | performance sur un lot (p. 3) | confirmé |
| P11 EvoPrompt | A2 sous condition | exactitude, ROUGE ou SARI selon la tâche (p. 7) | A2 avec l'exactitude seulement (CP-16) |
| P12 h4rm3l | A2 | classifieur binaire « Bad Bot » contre le reste (p. 6) ; taux de succès sur un petit lot (p. 5–6) | confirmé |
| P13 Ge-Wang et al. | A2 | seuils de l'attaquant réglés pour minimiser la sécurité (p. 4–7) | confirmé, réserves justes |
| P14 AutoDAN-Turbo | Non, note | note de 1 à 10 (p. 4) | confirmé |
| P15 Crescendomation | Non, note | drapeau, pourcentage, juge de refus, réponses (p. 8) | confirmé |
| P16 Open Sesame | Non, sortie textuelle | similarité du plongement de la sortie (p. 3) | confirmé |
| P17 GEPA | Non | fonction de retour en entrée (p. 4) | confirmé |
| P18 Nasr et al. | Non | recherche : texte et note (p. 17) ; renforcement : sortie et note (p. 16) | confirmé ; motif à compléter (CP-16) |
| P19 Emmons et al. | Non, sortie textuelle | contexte des itérations (p. 12) ; sortie du moniteur (p. 55, contrôle par programme) | confirmé |
| P22 Schaeffer et al. | Non | variante divulguée : note (p. 5) ; GEPA : note (p. 23) ; **méthode principale : verdicts d'audit d'un lot (p. 5–6)** | à scinder, méthode principale en A2 (CP-2) |
| P25 Hayase et al. | Non | log-probabilités (p. 4) ; somme des notes de modération (p. 8) | confirmé |
| P27 Andriushchenko et al. | Non, log-probabilités | log-probabilités (p. 1) ; sans log-probabilités : transfert ou préremplissage, sans optimisation (p. 1, p. 8) | confirmé |
| P32 Bailey et al. | Non | blanc pour les plongements, gris pour les jetons (p. 9) | confirmé |
| P35 Baker et al. | Non, poids de l'agent | verdict dans la récompense de l'agent (p. 8) | confirmé ; motif N-053 à corriger (CP-7) |
| P38 Perez et al. | Non | stochastic few-shot et renforcement : probabilité (p. 5) ; supervisé : verdict seul et entraînement de l'attaquant (p. 3, p. 5) | à situer (CP-11) |
| P40 Boundary Attack | Non, entrée continue | décision seule, perturbation d'image (p. 1) | confirmé |
| P41 HopSkipJumpAttack | Non, entrée continue | décision seule ; estimation de direction de gradient dans un espace continu (p. 1–3) | confirmé |
| P42 Ilyas et al. | Non, entrée continue | k étiquettes ordonnées, k = 1 étant la décision seule (p. 2) | confirmé |

Les variantes retenues existent bien à la page dite : TAP binaire (p. 38 et p. 40, mais deux variantes : CP-4) et Rainbow Teaming à juge binaire (p. 10 et p. 24).

---

## 4. Exhaustivité — recherches neuves sur arXiv (2026-11-10, termes techniques seulement)

| N° | Requête (`search_query`, ou identifiant) | Résultats | Retenus |
|---|---|---|---|
| 1 | `abs:"hard-label" AND abs:text AND abs:adversarial` | 9 | TextDecepter, TextHacker, HQA-Attack, Cross-Entropy Attacks, LBA (P06 déjà présent) |
| 2 | `abs:"safety filter" AND abs:bypass AND abs:"black-box"` | 12 | aucun nouveau à verdict seul (surtout texte-image ; h4rm3l déjà présent) |
| 3 | `abs:"hard-label" AND (abs:LLM OR abs:"language model" OR abs:guardrail)` | 51 | LimeAttack, OASIS, PivotAttack, LBA |
| 4 | `abs:"binary feedback" AND (abs:jailbreak OR abs:"red teaming" OR abs:"red-teaming" OR abs:"prompt optimization")` | 0 | — |
| 5 | `abs:jailbreak AND abs:"binary" AND abs:judge AND abs:iterative` | 1 | aucun (texte-image) |
| 6 | `abs:"decision-based" AND (abs:LLM OR abs:jailbreak OR abs:guardrail OR abs:moderation OR abs:"safety classifier" OR abs:detector)` | 95 | 2506.06933 (coût asymétrique, images) ; voisins en images ou données structurées |
| 7 | `ti:TextHoaxer OR ti:LeapAttack OR ti:SSPAttack OR ti:SneakyPrompt OR ti:TextHacker` | 2 | SneakyPrompt, TextHacker (les trois autres titres ne sont pas sur arXiv) |
| 8 | `(abs:guardrail OR abs:"prompt injection detector" OR abs:"jailbreak detector") AND abs:"black-box" AND abs:evasion AND abs:queries` | 1 | aucun |
| 9 | `abs:monitor AND (abs:flagged OR abs:"binary") AND abs:evade AND (abs:agent OR abs:"chain-of-thought" OR abs:CoT) AND abs:optimiz*` | 0 | — |
| 10 | `abs:monitor AND abs:evade AND abs:"black-box" AND (abs:agent OR abs:LLM)` | 4 | **Boundary Point Jailbreaking** |
| 11 | `(abs:"single bit" OR abs:"one bit" OR abs:"binary signal" OR abs:"flagged or not") AND (abs:jailbreak OR abs:classifier OR abs:monitor OR abs:guardrail) AND abs:attack` | 106 | Boundary Point Jailbreaking, AutoInject, Screwtape |
| 12 | `id_list=2406.11695` | 1 | MIPRO |

**Ce qui manque, par ordre d'importance** :
1. Boundary Point Jailbreaking (A2, vérifiée sur PDF ; CP-3) ;
2. la famille des attaques de texte en étiquette dure postérieures à P06, huit identifiants (CP-10) ;
3. MIPRO, de classe A2 ;
4. AutoInject et SneakyPrompt, à verdict binaire avec entraînement de l'attaquant (CP-11) ;
5. Screwtape, exclue, littérature du contrôle (vérifiée sur PDF).

**Ce que je ferais entrer dans la liste fermée**, sous lecture A2 :
- P22a (méthode principale de Schaeffer et al.) ;
- GPTFuzzer multi-questions ;
- Boundary Point Jailbreaking, après dépôt et scellement.

Sous réserve de vérification sur PDF, j'y ajouterais aussi une ou plusieurs attaques de texte en étiquette dure (A1) et MIPRO (A2).

**Ce que je ferais sortir, ou resserrer** :
- TAP, réduit aux évaluateurs E_Llama-Guard et E_Substring ;
- GPTFuzzer, réduit à la question unique en A1 ;
- et, si Lazar retient l'option (b) de la question 3 proposée (CP-1) : PAIR, TAP, GPTFuzzer et Rainbow Teaming tels que publiés, leurs consignes ou descripteurs devant être réécrits.

---

## 5. Ce que je n'ai pas pu vérifier

- **Pages opératoires** : celles que liste la section 9 n'ont pas été lues, à dessein, sauf le contexte minimal de C92 et la phrase sur le SCORE de TAP, p. 37. La justesse page par page de cette liste n'est donc pas vérifiée.
- **Code** : la colonne « Code » (dépôts, HEAD, licences) n'a pas été vérifiée, faute de `git ls-remote` et de lecture des licences. Le codage du verdict binaire de Llama Guard dans le SCORE de PAIR v4 n'est pas décrit dans le PDF ; le code n'a pas été lu.
- **Absents classés sur résumé seulement** : les attaques de texte en étiquette dure, MIPRO, AutoInject et SneakyPrompt n'ont été classés que d'après leur résumé arXiv.
- **PDF téléchargés hors dépôt** : ceux de Boundary Point Jailbreaking et de Screwtape sont dans le bloc-notes de la session, ni déposés ni scellés. Leurs empreintes sont données ci-dessus. Ils ne sont pas opposables tant que le programme ne les a pas déposés (R7).
- **Échelle d'accès** : je ne l'ai lue que dans le candidat brouillon 3, non scellé, de `prereg/bras-attaque-regle-v1.md` (lignes 60 à 105, 155 à 160 et 403). Ses définitions, notamment « politique figée » et les échelons 5 et 6, peuvent changer. La pièce source de la décision du 10 novembre (`docs/notes/integration-bras-attaque-v1/`) n'a pas été lue.
- **TAP, annexe E.2** : le PDF ne dit pas explicitement si la fonction Off-Topic y reste active ; je le déduis de la page 8.
- **Rainbow Teaming** : la règle de remplacement de l'archive pour le juge binaire n'a pas été trouvée aux pages 10 et 24 ; le reste du PDF n'a pas été parcouru en entier.
- **Versions** : seules les versions arXiv ont été lues ; les versions de conférence n'ont pas été comparées.
- **Routine de reprise (R14)** : je ne l'ai pas faite, car elle ne relève pas de mon rôle. J'ai vérifié seulement le catalogue, les PDF qu'il cite et les pièces d'appui nommées dans l'en-tête.
