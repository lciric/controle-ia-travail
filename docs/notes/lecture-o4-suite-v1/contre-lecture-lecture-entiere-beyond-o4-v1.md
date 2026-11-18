# Contre-lecture de la lecture entière de BEYOND (Huang et Fan, arXiv 2603.14288 v2) contre O4 — v1

- **Contre-lecteur : modèle J** (J ≠ I ; je n'ai pas écrit la lecture). Pièce contre-lue : `docs/notes/lecture-o4-suite-v1/lecture-entiere-beyond-o4-v1.md` (compagnon `.sha256` vérifié, conforme).
- **Heures (`date -u`, recopiées)** : début 2026-11-18T02:13:16Z (empreintes du PDF et des trois fichiers textuels du clone recalculées, commit relevé) ; rejeu des deux fichiers de l'auteur 2026-11-18T02:13:36Z ; rejeu de mes citations 2026-11-18T02:16:28Z ; écriture de cette note 2026-11-18T02:18:00Z.
- **Fichiers lus** : la lecture et ses quatre fichiers de rejeu et de résultat ; `docs/sources/code/lecture-o4-v1/beyond/provenance-v1.md` ; `lecture-o4-englobement-v3.md` (lignes 19 à 77 et 181 à 199) ; `lecture-pdf-priorite-haute-o4-v2.md` (lignes sur BEYOND, table des composantes, nœuds) ; les deux programmes de rejeu (lus, non modifiés) ; le PDF `docs/sources/pdf/lecture-o4-v1/arxiv-2603.14288/2603.14288v2.pdf` (sha256 `8fe2b21770af074a0e13667048bc40b3eb85fc03ecde8f5d58938e3aa100e301`, recalculé, conforme, 60 pages) ; le clone `code-o4/agentic-factor-investing` au commit `cc8bd7d06c26f39dc379157208482fe0da19623e` (`git rev-parse HEAD`, conforme) : `README.md`, `chart_data.json`, `index.html`.
- **Ma profondeur** : PDF, p. 1 à 47 et 52 à 60 lues en entier (`pdftotext -layout`, page par page) ; bibliographie p. 48 à 51 par recherche de termes seulement ; figures non lues (images). Code : les trois fichiers textuels lus en entier (`index.html`, 507 lignes ; `chart_data.json` par lecture JSON, 502 points) ; l'image non lue. Recherche de 70 termes sur le texte entier, césures recollées.
- **Rejeux** : fichiers de l'auteur, **61 sur 61** citations (code 0, sortie `…-rejeu-citations-pdf.json`) et **14 sur 14** extraits (code 0, sortie `…-rejeu-extraits-code.json`), programmes inchangés. Mes citations : **33 sur 33** (`…-resultat-citations-pdf.json`) et **1 sur 1** (`…-resultat-extraits-code.json`). Entre guillemets français : en anglais, les citations de l'article et du dépôt de la page, toutes dans mes deux fichiers de rejeu ou dans ceux de l'auteur ; en français, les mots de la lecture contre-lue et les formulations proposées, qui ne sont pas des citations de la pièce.
- **Règles** : R7, R8, R4, N-067 (personne ici ne déclare O4 libre ; verdict en vigueur : occupée en partie ; ce qui suit propose des corrections et des nœuds, pas des conclusions).

## 1. Verdict

**Tient avec réserves.** Les six statuts de la table (P voisin, (i) pris, (ii) voisin lointain, (iii) voisin et non trouvé pour l'e-processus, (iv-a) voisin, (iv-b) pris pour la porte écrite) résistent à la relecture du PDF et du dépôt de la page : je n'ai trouvé ni passage ni fichier qui en renverse un. Les absences qui arrangent la revendication (aucun e-processus, aucun nul formé de l'archive, aucun scellement, aucun code du système publié, aucun code annoncé ailleurs) sont confirmées dans ce que j'ai lu, à ma profondeur. La réserve principale porte sur une **formulation** : la lecture attribue l'apport marginal au modèle de langue et propose de retirer « partie de la porte » de la ligne de la note d'englobement ; le texte ne le permet pas, et la correction va dans le sens non flatteur (constat 1). Les autres constats sont des compléments.

## 2. Ce qui est confirmé

- Empreintes : PDF conforme ; `README.md` `2e38d983…`, `chart_data.json` `c87623d8…`, `index.html` `2a5839f1…`, conformes à la provenance ; commit conforme ; clone superficiel, un seul commit (`git log` : 2026-03-14 18:32:09 +0800, message de renommage de fichier).
- Code : le dépôt ne contient **aucun code du système** (quatre fichiers : un titre, les données d'un graphique, une page et son script d'affichage, une image). Ni le PDF (p. 1, p. 47, et les occurrences de `code` et de `github`), ni la page n'annoncent un code publié ailleurs ; la page renvoie au `README.md`, qui ne contient que son titre. Confirmé.
- Recherche de termes de la section 2 de la lecture : refaite, mêmes pages (dont `sequential`, `likelihood`, `spanned`, `incremental`, `marginal`, `benchmark`, `memory`, `pre-commit`) ; zéro occurrence pour `e-value`, `e-process`, `anytime`, `martingale`, `stopping`, `likelihood ratio`, `Bayes factor`, `null`, `Bonferroni`, `Holm`, `hash`, `seal`, et, ajoutés par moi, `p-value`, `bootstrap`, `timestamp`, `posterior`, `betting`, `wealth`, `cutoff`, `repositor`, `temperature`.
- Règle de promotion écrite (p. 13 et 16), seuil de 3,0 non relié à τsig, τecon et τfail sans valeur, nombre de tours et de candidats non donné, modèle de langue du système non nommé, alphas contre CAPM à FF6 hors échantillon et a posteriori (p. 25, 28), sept facteurs sur douze sous 3,0 pour l'alpha FF5 (p. 25, recompté) : confirmés.
- Citations de l'auteur relues dans leur contexte : aucune sortie de son contexte au point de changer un statut.

## 3. Constats

### Constat 1 — majeur. L'attribution de l'apport marginal au modèle de langue est trop forte, et la formulation proposée au nœud 1 retire « partie de la porte » dans le sens flatteur

- **Ce que dit la lecture** : section 3 (P), section 5 (réponse 1 : là où le texte dit qui fait le filtre, il le rend au mécanisme de mémoire, « c'est-à-dire au modèle de langue »), table de la section 6 (P : « attribué à la mémoire de l'agent »), nœud 1 (formulation proposée : règle de promotion hors de l'agent contre aucun effet ; apport marginal « affirmé et attribué à la mémoire de l'agent »). La v2 disait : affirmé **comme partie de la porte**, calcul non montré.
- **Ce que dit le texte.** (a) L'« agent » de l'article est le système entier, porte comprise, non le seul modèle de langue : p. 10, « We design the agent as an autonomous research system for systematic factor investing, rather than as a one-shot language interface. » ; la page le décrit de même, `index.html` l. 381 : « alt="Project framework: Data Layer (CRSP to Standardized Panel), Autonomous Discovery Agent loop (Generator, Factor Recipe, Execution & Gatekeeping, Memory Update), Factor Library to Linear and Tree models to OOS Performance (Net)." ». La phrase de la p. 35 (l'agent s'assure, par un mécanisme de mémoire, de l'information marginale) ne désigne donc pas le modèle de langue comme juge. (b) Le texte range l'apport marginal dans la porte et parmi les obstacles statistiques : p. 35, « Our agent emulates this skepticism by incorporating a multi-objective promotion gate », dont le premier objectif est la redondance d'information ; note 10, p. 35, « Our multi-objective gate acts as a functional heuristic for the Deflated Sharpe Ratio, implicitly accounting for the hidden trials involved in automated factor search by imposing stringent non-performance hurdles. » ; p. 34, sous le titre « 6.2. Strict Statistical Hurdles and Multiple Testing Adjustment », à la première personne des auteurs et non de l'agent : « Furthermore, we evaluate the factor’s contribution to reducing pricing errors ». (c) La porte écrite de l'algorithme est elle-même déclarée incomplète : p. 13, « mf ← [tIC , SRLS , . . . ]⊤ » (vecteur de performance à composantes non nommées) ; p. 17, « new operators, stricter gate criteria, additional risk controls, or richer transaction-cost models can be integrated without changing the core loop ».
- **Portée.** Le texte est ambigu : il met l'apport marginal à la fois dans la porte (p. 34, 35, note 10) et sous un mécanisme de mémoire (p. 35) que l'algorithme place dans le modèle de langue (p. 13, ligne 30). La lecture cite les deux, mais tranche vers le modèle de langue dans sa réponse 1, sa table et son nœud 1. Cette résolution arrange la revendication (un filtre « contre le connu » rendu au modèle n'est pas une statistique calculée hors des agents) ; R4 et R8 demandent l'inverse.
- **Correction proposée** (nœud pour Lazar, pas une conclusion). Ligne de BEYOND : *voisine ; règle de promotion écrite calculée hors du modèle de langue, contre aucun effet (t_IC et Sharpe à seuils) ; apport marginal sur des références établies (par exemple le modèle à cinq facteurs) **affirmé comme partie de la porte de promotion** (p. 34, 35 et note 10), le texte y mêlant le mécanisme de mémoire ; lieu du calcul non tranché par le texte, aucune formule, aucun seuil, aucun résultat ; protocole dit engagé d'avance, non scellé ; code du système non publié*. Dans la table : P reste **voisin**, avec « affirmé comme partie de la porte ; lieu du calcul non tranché » à la place de « attribué à la mémoire de l'agent » ; (iv-b) reste pris pour la porte écrite, « non établi **ni exclu** » pour l'apport marginal. Aucun statut ne change ; le verdict sur O4 n'est pas touché (le principe P est déjà occupé par d'autres pièces de la note d'englobement).

### Constat 2 — mineur. La branche « en attente » de la porte n'a ni règle ni auteur écrits ; (iv-b) « pris » doit le dire

- La porte a trois issues (p. 12, « explicit decisions: promote, hold for review, or retire » ; p. 13, « D(f ) ← Re-evaluate/Hold »). Pour la troisième : p. 16, « Borderline cases are flagged for targeted robustness checks, and clear failures are retired with explicit annotations. » Qui fait la revue (programme, modèle de langue, humain), avec quelle règle, et si un candidat en attente peut être promu ensuite : non écrit dans les 60 pages.
- **Correction proposée** : borner (iv-b) « pris » aux deux branches écrites (promotion, retrait) ; ajouter « sort des candidats en attente non écrit ». Cela borne aussi (iii) : la règle à seuil fixe n'est pas toute la règle de promotion décrite.

### Constat 3 — mineur. La réserve de fiabilité (nœud 3) vaut aussi pour le PDF seul, pas seulement pour l'écart entre la page et le PDF

Incohérences internes au PDF, non relevées par la lecture (constats, sans interprétation) :
- **Noms des facteurs.** Le texte nomme p. 37 « Factor 7 (Delayed Turnover Pressure) and Factor 10 (Medium Horizon Turnover Pressure) », p. 38 « Factor 2 (Friction Adjusted Flow Shock) » et « Flow Volatility Imbalance (Factor 1) and Price Level Persistence (Factor 8) » ; la table des facteurs (exhibit 15, p. 39) donne aux mêmes numéros « Turnover Volatility Risk » (7), « Sustained Liquidity Attention » (10), « Lagged Flow Pressure » (2), « Flow Shock - Winsorized » (1), « Defensive Mean-Reversion Signal » (8). Aucun des cinq noms du texte ne figure p. 39. La phrase de la p. 38 que la lecture cite pour la pénalité de rotation (l'agent apprend à pénaliser les signaux à forte rotation) est attachée à ce facteur 2 dont le nom et la description ne se retrouvent pas dans la table.
- **Rendements cumulés.** P. 42 : « approximately 75% net vs. 139% gross » pour la stratégie composite de janvier 2021 à décembre 2024 ; p. 31 : « The D10-D1 long-short spread yields a cumulative gross return of 465.07% » et, net, « cumulative return of 305.57% ». Le texte n'explique pas l'écart.
- **Rendement annualisé de la combinaison linéaire.** P. 28 : « The strategy delivers a gross annualized return of 54.81% » ; p. 44, pour le portefeuille agentique linéaire sur la même fenêtre : « return of 58.80%, compared with 30.91% for the traditional linear portfolio ».
- **Nombre de facteurs.** P. 41 : « twelve Agentic-AI generated factors » ; p. 58 : « This figure reports univariate portfolio-sort results for Factor 1–Factor 11 ».
- **Correction proposée** : étendre le nœud 3 de la lecture : la réserve de fiabilité repose aussi sur le PDF lui-même. Conséquence pour O4 : les statuts de BEYOND reposent sur des **affirmations** d'un texte peu soigné ; les garder dans le sens non flatteur (ce qui est affirmé compte comme affirmé), sans en tirer davantage.

### Constat 4 — mineur. Une phrase de l'introduction contredit la séparation des échantillons ; non rapportée

- P. 3 : « The agent evaluates factors based on rigorous, out-of-sample statistical properties and structural robustness rather than mere narrative appeal. » Les p. 12 et 14 disent l'inverse pour la promotion (p. 12 : « only in-sample results are allowed to influence promotion decisions »). La lecture cite les secondes, pas la première.
- **Correction proposée** : l'ajouter à (iv-a) comme contradiction interne (la séparation est dite, non scellée, et le texte se contredit une fois) ; le statut voisin ne change pas. Ajouter aussi, dans le sens occupant, le gel déclaré : p. 35, « During the OOS period (2021–2024), the agent’s internal state and », suite p. 36, « factor library are frozen. » (gel dit, sans empreinte ni horodatage).

### Constat 5 — mineur. (ii) : la bibliothèque des admis est une entrée du proposeur ; à dire

- La lecture écrit que la bibliothèque n'est jamais un terme de comparaison écrit, hors la mémoire qui évite les essais redondants (p. 17). Exact, mais incomplet : l'annexe fait de l'état de la bibliothèque l'entrée de la politique, p. 52, « st is the current state of the factor library, and ht is the historical trajectory of previous attempts » ; et p. 12, « This memory-guided diversification is central to reducing search myopia and mitigating factor crowding inside a narrow subspace. » L'archive des admis conditionne donc la **proposition** (diversification par le modèle de langue) ; elle n'est pas un nul ni un terme de la porte écrite.
- **Correction proposée** : ajouter ces deux pages à (ii) ; statut voisin (lointain) inchangé ; le « non trouvé » sur la mise en commun ajustée de l'archive est confirmé dans les pages que j'ai lues.

### Constat 6 — mineur. « L'article ne l'aborde pas » (fuite par l'entraînement du modèle) est un peu trop fort

- La lecture écrit que l'article n'aborde pas la possibilité que le modèle de langue ait vu les données 2021-2024. Il nomme le problème pour un travail cité, p. 9 : « emphasizing chronological consistency to mitigate lookahead bias and training leakage », et ne l'applique pas à son propre système (modèle non nommé, aucune date de fin d'entraînement : `cutoff`, zéro occurrence).
- **Correction proposée** : écrire « l'article nomme ce risque pour un travail cité (p. 9) et ne le traite pas pour son propre système ».

### Constat 7 — mineur. Code : la seule description textuelle du schéma n'est pas rapportée

- `index.html`, l. 381 (attribut `alt` de l'image, cité au constat 1) : seule trace textuelle du contenu de `project-framework.png`. Elle place l'exécution et la porte dans la boucle de l'« agent » et ne nomme aucune comparaison au connu dans cette boucle. À ajouter à la section 4 de la lecture ; elle sert le constat 1 et ne révèle aucune règle, statistique ou engagement que la lecture aurait manqué.
- Rien d'autre dans le dépôt : aucune règle de promotion, aucune statistique, aucun engagement, aucune comparaison au connu réalisés en code ; le script ne fait que tracer deux séries.

### Constat 8 — mineur. Multiplicité : préciser l'origine du seuil

- La lecture dit la multiplicité réalisée par le seul seuil 3,0. Exact ; préciser que ce seuil est emprunté, p. 34 : « we adopt the more stringent significance level recommended by Harvey et al. (2016) for the current research era », sans calcul propre au nombre d'essais du système. La porte écrite est unilatérale (t_IC supérieur ou égal à τsig, p. 13 et 16) alors que le seuil de la p. 34 porte sur la valeur absolue : écart déjà couvert par « lien non écrit », à dire en clair.

## 4. Profondeur déclarée par la lecture

- Les 61 citations de l'auteur couvrent 29 pages distinctes entre la p. 1 et la p. 55 ; la table de termes, refaite, concorde page pour page sur les termes que j'ai recomptés. Je ne peux pas prouver que chaque page a été lue ; je n'ai trouvé, en lisant moi-même les p. 1 à 47 et 52 à 60, aucun contenu décisif absent de la lecture qui change un statut. Les omissions relevées (constats 2 à 7) sont des compléments, dont trois sur des pages que la lecture cite par ailleurs (p. 12, 13, 16).
- Les nombres de l'exhibit 8 (p. 25) et de l'exhibit 9 (p. 27) que la lecture rapporte sans guillemets sont exacts sur la page.

## 5. Ce que je n'ai pas pu vérifier

- Contenu graphique des figures du PDF et de `project-framework.png` (images).
- Bibliographie p. 48 à 51 : par recherche de termes seulement.
- Tout code du système non publié ; page du projet en ligne et historique du dépôt avant le commit lu (aucun accès réseau, clone superficiel) ; version v1 de l'article ; références citées (Harvey et Liu 2021, López de Prado 2018, Harvey, Liu, Zhu 2016).
- Le contrôle strict hors dépôt déclaré par l'auteur (59 sur 61) et son contrôle automatique des passages entre guillemets : non rejoués, leurs programmes n'étant pas au dépôt ; les deux césures qu'il déclare (p. 1, p. 35) sont visibles en fin de ligne dans la mise en page.

## 6. Nœuds pour Lazar (repris de la lecture, amendés)

1. **Formulation de BEYOND dans la prochaine version de la note d'englobement** : (a) la formulation de la lecture (apport marginal attribué à la mémoire de l'agent) ; (b) la formulation du constat 1 (affirmé comme partie de la porte, lieu du calcul non tranché). Recommandation : (b), confiance haute ; elle est la plus proche de la lettre du texte et la moins flatteuse. Statut de la pièce et verdict sur O4 inchangés.
2. **Réserve de fiabilité** : l'étendre au PDF lui-même (constat 3) si BEYOND est citée.
3. Les nœuds 2 et 4 de la lecture (demande du code aux auteurs ; citation obligatoire) : sans objection ; le constat 1 renforce plutôt l'intérêt de citer BEYOND comme voisin du principe affirmé dans la porte.

## 7. Incidents et refus

- Aucun refus de permission, de crochet ou de classifieur. Aucun accès réseau, aucune dépense, aucun programme du clone lancé, aucun fichier de l'auteur modifié.
- Lecture du script de versement avant usage (fichier du dossier de travail, hors dépôt) : la ligne de co-signature qu'il ajoute au commit est fixe et ne dépend pas de l'agent qui verse ; signalé dans la réponse rendue.
