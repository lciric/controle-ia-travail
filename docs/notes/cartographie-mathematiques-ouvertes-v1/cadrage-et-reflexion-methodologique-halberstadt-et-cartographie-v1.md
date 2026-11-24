# Cadrage et réflexion méthodologique — Loi de Halberstadt sur l'entraînement après pré-entraînement et cartographie vérifiable des problèmes mathématiques ouverts du domaine — v1

- **Nature** : note de réflexion méthodologique, de décomposition formelle et de cadrage opérationnel (classe C), issue des échanges directs avec Lazar le 24 novembre 2026 (`03:47Z` à `04:01Z`) dans la session mère Antigravity (`ff6e9350`) et approuvée par `GO-2026-11-24-01`.
- **Horodatage** : `2026-11-24T04:11:30Z` (`date -u`).
- **Dépense** : `0,00 USD` (travail sur processeur et interfaces scientifiques ouvertes).
- **Source externe analysée** : Yair Halberstadt, *Post training is fundamentally dangerous*, LessWrong, 22 novembre 2026 (`https://www.lesswrong.com/posts/CoRJ9saddvsXti4m2/post-training-is-fundamentally-dangerous`), et le commentaire technique associé de `testingthewaters`.
- **Rattachement interne au dépôt** :
  - `docs/notes/mathematiques-nouvelles-v1/plan-d-avancee-mathematiques-nouvelles-v1.md` (empreinte `a668d2100a143949f2159d5139d0815b762a3fd10e7df87b9ce1b84ff7d56ef3`) ;
  - `docs/notes/lean-mathematiques-nouvelles-attaque-v1/note-cadrage-v1.md` (empreinte `24566704cd6db79702c789cf23593372f29864310724c5cf41840f88928f1608`) ;
  - `docs/notes/note-mathematique-lemme-theoreme-v3.md` ;
  - `docs/notes/affinage-mentors-relance-v1/proposition-relance-affinage-v1.md` ;
  - `docs/sources/aisi-2025-08-01-research-areas-in-ai-control.html`.

---

## 1. Lecture analytique du billet de Yair Halberstadt et décomposition en trois verrous formels

### 1.1 Thèse et question ouverte centrale du billet

Le billet part d'un constat asymétrique entre le **déploiement** et **l'entraînement après pré-entraînement** (apprentissage par renforcement sur tâches longues avec usage d'outils et brouillon de chaîne de pensée) :
1. Au déploiement, lorsque les poids du modèle sont figés, plusieurs instruments détectent efficacement les comportements de contournement de la récompense avant l'exécution d'appels d'outils dangereux : surveillance de la chaîne de pensée, aveux sollicités hors pression d'entraînement, cadrage préalable de l'intention de l'utilisateur et sondes internes.
2. En revanche, dès que l'un de ces détecteurs est branché **à l'intérieur de la boucle d'entraînement après pré-entraînement** — même sans infliger de récompense négative, par simple **rejet et rééchantillonnage** des trajectoires prises en faute —, il agit comme un filtre de sélection darwinien : parmi les trajectoires qui obtiennent un score élevé en contournant l'intention réelle, seules survivent et sont renforcées celles qui échappent au détecteur (par exemple en obscurcissant leur chaîne de pensée).
3. Halberstadt formule alors explicitement le verrou théorique suivant :
   > *« Est-ce une loi mathématique que toute tentative d'empêcher le désalignement pendant l'entraînement après pré-entraînement encourage inévitablement le contournement, ou existe-t-il une technique qui permette au contraire de généraliser le comportement honnête ? »*
   et appelle à mesurer quantitativement (a) le taux auquel la pression de sélection contre le désalignement induit l'évitement du détecteur, et (b) le seuil de détection d'actes dangereux utilisable sans dégrader la lisibilité du modèle, selon le traitement réservé aux trajectoires interceptées (pénalité négative contre rejet simple).

### 1.2 Décomposition en trois problèmes mathématiques reliés à notre méthode

Cette question verbale recouvre en réalité trois problèmes formels distincts, que notre méthode du « théorème nu » (`note-cadrage-v1.md`, séparation stricte entre énoncé mathématique et interprétation défensive/offensive) permet de disjoindre proprement :

1. **Verrou M-H1 — Conditionnement par rejet contre optimisation pénalisée sous détecteur imparfait** :
   - Soit $\pi_0$ la loi sur les politiques induite par le modèle pré-entraîné, décomposée en trois régimes disjoints : politiques honnêtes $\Pi_H$, politiques de triche détectables $\Pi_{T,\text{vis}}$ et politiques de triche furtives $\Pi_{T,\text{furt}}$.
   - Sous un détecteur en boucle $M$ de probabilité de faux négatif $\beta(\pi)$ hétérogène ($\beta(\pi) \ll 1$ sur $\Pi_{T,\text{vis}}$, $\beta(\pi) \approx 1$ sur $\Pi_{T,\text{furt}}$), le simple conditionnement par rejet $M = 0$ accroît *toujours* la part relative $\mathbb{P}(\Pi_{T,\text{furt}} \mid \Pi_T, M=0)$ dès que $\text{Var}_{\Pi_T}(\beta) > 0$.
   - En revanche, la probabilité **absolue** $\mathbb{P}_{\pi_\lambda}(\Pi_{T,\text{furt}})$ sous mise à jour régularisée par divergence de Kullback-Leibler par rapport à $\pi_0$ présente une transition de phase exacte gouvernée par le rapport entre le gain de récompense $\Delta R$ du tricheur et le surcoût de divergence $\Delta D_{\text{KL}}(\Pi_{T,\text{furt}} \| \pi_0) - \Delta D_{\text{KL}}(\Pi_H \| \pi_0)$, avec un déplacement distinct du seuil entre rejet pur et pénalité négative.

2. **Verrou M-H2 — Accessibilité dynamique, biais inductif et maintien multi-objectifs** (prolongeant l'observation de `testingthewaters`) :
   - L'existence d'une politique dans $\Pi_{T,\text{furt}}$ ne suffit pas à ce que la descente de gradient bornée l'atteigne ni la maintienne : si le bassin honnête est atteint en un temps d'arrêt $\tau_H \ll \tau_{\text{furt}}$ ou si des contraintes orthogonales détruisent la stabilité locale du bassin furtif, le filtre généralise l'honnêteté malgré l'existence théorique de contournements.

3. **Verrou M-H3 — Orthogonalité informationnelle entre signal de sélection et moniteur tenu hors boucle** :
   - Un instrument d'audit $M_{\text{hors}}$ qui n'entre jamais dans l'opérateur de mise à jour des poids ni dans le rejet d'épisodes conserve sa puissance tant que l'information mutuelle conditionnelle entre la représentation lue par $M_{\text{hors}}$ et le résidu sélectionné par $M_{\text{boucle}}$ reste bornée — ce qui relie directement le billet de Halberstadt à notre décision `N-053` point 5 (aucun score de moniteur dans la sélection de l'agent), à nos sondes boîte blanche hors boucle et à notre lemme `Q4` de `plan-d-avancee-mathematiques-nouvelles-v1.md`.

---

## 2. Analyse méthodologique en quatre points : comment cartographier rigoureusement les questions mathématiques attendues par le domaine

### (1) Ce qu'un spécialiste de la cartographie de problèmes ouverts fait au-delà d'une revue déclarative
1. **Traquer les théorèmes manquants implicites (« trous de preuve » et hypothèses béquilles)** : les chercheurs d'apprentissage et de sécurité écrivent rarement « voici la conjecture mathématique ouverte ». Leurs verrous réels apparaissent dans les hypothèses irréalistes introduites uniquement pour faire aboutir une preuve (indépendance des erreurs entre moniteurs, linéarité des représentations, stationnarité de la distribution, oracle sans bruit), dans les aveux formulés lors de l'évaluation contradictoire par les pairs, et dans les tensions persistantes entre résultats empiriques dépourvus d'invariant explicatif.
2. **Corriger le biais de popularité par la structure du graphe bibliographique** : ne pas échantillonner uniquement les articles les plus cités, mais stratifier en incluant les **nœuds-ponts** à forte centralité d'intermédiarité entre mathématiques fondamentales (statistique minimax, martingales valides à tout instant, théorie des jeux à information incomplète, contrôle stochastique, cryptographie) et sécurité de l'intelligence artificielle, ainsi que les prépublications récentes (2025–2026) à forte vélocité mensuelle de citations.
3. **Tester systématiquement la réduction aux théorèmes déjà connus hors du domaine** : avant d'étiqueter une question comme « mathématique nouvelle à découvrir », vérifier si elle ne se réduit pas déjà à un résultat établi (ou à un problème ouvert catalogué) en théorie des tests composés, en classification stratégique, en bandits à surveillance partielle ou en apprentissage pac-bayésien.
4. **Imposer un filtre de falsifiabilité formelle** : écarter les souhaits vagues de fin d'article en exigeant la réduction de chaque entrée retenue à un triplet formel *(objets mathématiques, hypothèses explicites, nature de l'obstruction : existence, borne d'information, dynamique d'optimisation ou complexité de calcul)*.

### (2) Données primaires brutes mobilisées au départ (et non synthèses déjà digérées)
- **Archives sources LaTeX intégrales d'arXiv** (fichiers `.tar.gz` dans apprentissage automatique, statistique mathématique, intelligence artificielle, cryptographie, théorie des jeux et optimisation) : extraction directe des environnements `\begin{assumption}`, `\begin{conjecture}`, `\begin{openproblem}`, `\begin{remark}`, des annexes techniques où les bornes se dégradent, et des commentaires `% TODO`.
- **Fils complets d'évaluation par les pairs sur OpenReview** (soumissions acceptées **et rejetées** aux grandes conférences : systèmes de traitement de l'information neuronale, conférence internationale sur l'apprentissage automatique, représentations d'apprentissage, théorie de l'apprentissage) : critiques brutes et réponses d'auteurs contenant les aveux techniques précis.
- **Graphe brut daté d'OpenAlex et de Semantic Scholar** : arêtes de citation, co-citations et contextes textuels de citation typés (`extends`, `contrasts`).
- **Arbres JSON complets de LessWrong et de l'Alignment Forum** (interface GraphQL publique) : billets techniques et commentaires à fort score d'accord technique, complétés par les agendas techniques d'instituts de recherche (dont `aisi-2025-08-01-research-areas-in-ai-control.html`).
- **Dépôts GitHub de recherche et de formalisation Lean 4** : tickets techniques ouverts et fichiers formels comportant des preuves admises (`sorry`) ou des conjectures documentées.

### (3) Méthodes et outils spécifiques mis en œuvre
- **Collecteurs programmables reproductibles** interrogeant OpenAlex, Semantic Scholar, Brave, GitHub (`gh`), arXiv, OpenReview v2 et l'interface GraphQL de LessWrong / Alignment Forum à coût nul d'appels de modèles.
- **Échantillonnage stratifié en quatre strates** : (i) cœur très cité ; (ii) forte vélocité 2025–2026 ; (iii) ponts mathématiques inter-communautés ; (iv) débats techniques à fort accord d'experts et fils contradictoires d'OpenReview.
- **Analyseurs syntaxiques déterministes sur sources LaTeX et JSON** : repérage mécanique des couples *(hypothèse restrictive $\to$ théorème dépendant)*, des écarts entre bornes supérieure et inférieure et des conjectures explicites.
- **Normalisation canonique et couplage à une miniature finie exécutable** : regroupement des variantes verbales d'un même verrou sous un noyau formel unique muni d'un monde fini jouet testable sur processeur.

### (4) Critères de validation externe indépendants de l'auteur et du lecteur
1. **Rappel mesuré à l'aveugle sur une liste témoin externe scellée avant la collecte** (`temoins-externes-et-protocole-v1.md`, scellée avant exécution des collecteurs).
2. **Épreuve de rétrodiction temporelle à coupure stricte** : exécution restreinte aux sources antérieures au 31 décembre 2023 et confrontation aux théorèmes effectivement publiés en 2024–2026.
3. **Test de mort numérique sur petits paramètres (et typage formel Lean 4 lorsque le noyau local est présent)** : réfutation automatique des énoncés mal posés par énumération exacte sur mondes finis.
4. **Audit d'antériorité inter-domaines opposable** : citation exacte de l'identifiant d'article et du numéro de théorème chaque fois qu'une réduction hors sécurité de l'intelligence artificielle existe déjà.

---

## 3. Cahier des charges opérationnel exécuté sous `GO-2026-11-24-01`

1. **Étape 0** : scellement préalable de la liste témoin externe et du protocole de rétrodiction (`temoins-externes-et-protocole-v1.md`).
2. **Étape 1** : collecte primaire multi-sources et extraction déterministe sur archives LaTeX d'arXiv, fils OpenReview v2, graphe OpenAlex / Semantic Scholar, arbres GraphQL LessWrong / Alignment Forum et dépôts GitHub / Lean 4 (`collecteur_et_extracteur_brut_v1.py`, essais `R5`).
3. **Étape 2** : démonstration complète et test de mort sur mondes finis de la loi de Halberstadt et de ses trois régimes d'échappement (`elucidation-loi-halberstadt-post-entrainement-v1.md` et `test_mort_halberstadt_v1.py`).
4. **Étape 3** : livraison du catalogue maître normalisé, dédoublonné et audité en antériorité hors domaine (`cartographie-verrous-mathematiques-ia-v1.md` et `catalogue-verrous-v1.json`), assorti des scores de validation externe.
