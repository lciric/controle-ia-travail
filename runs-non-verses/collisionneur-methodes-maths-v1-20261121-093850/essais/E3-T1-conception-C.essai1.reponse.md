*Note liminaire de conformité : La Règle d'intégrité 3 (« Aucun identifiant arXiv donné de mémoire ») prime sur la consigne de la Question (point 3). Aucun identifiant arXiv n'est donc fourni. Les sections suivent l'ordre (1 à 6) exigé par la Question de l'Arbitre, en intégrant systématiquement les livrables (a), (b), (c) et (d) du Tour III.1.*

---

### 1. Ce qu'un expert du domaine ferait ici, et qu'on ne demande pas
*(Intègre le livrable (a) : ce que la question et le programme supposent sans que ce soit établi)*

Un expert en théorie de la détection, en apprentissage statistique et en déduction automatique ne commencerait pas par lancer cinq lignées de modèles de langage [VÉRIFIÉ dans les faits] sur des problèmes ouverts. Il auditerait les suppositions implicites du programme pour éviter de construire une usine à redécouvrir des théorèmes classiques sous un vocabulaire nouveau.

**Audit des présupposés non établis (Livrable a) :**
1. **L'inexistence du résultat dans la littérature existante [HYPOTHÈSE]** : Le programme suppose qu'il a besoin de « résultats mathématiques nouveaux » [VÉRIFIÉ dans les faits] sur l'agrégation sous corrélation adverse, les tests séquentiels finis et les jeux d'audit. Or, ces objets sont massivement étudiés sous d'autres noms : les *e-values* et martingales de test (pour le séquentiel fini), la théorie des copules et des bornes de Fréchet-Hoeffding (pour l'agrégation sous dépendance arbitraire), la divergence de Le Cam et les inégalités de Fano/Assouad (pour les bornes d'impossibilité), et les jeux de Stackelberg ou d'inspection (pour l'audit sous budget). **Ce que ferait l'expert :** Avant toute génération, il construirait un **traducteur d'isomorphismes** (mapping terminologique) pour réduire les cinq questions cibles à des problèmes canoniques de statistique mathématique.
2. **La suffisance des « mondes plantés » pour garantir la vérité universelle [HYPOTHÈSE]** : Le programme évalue les propositions sur douze mondes plantés [VÉRIFIÉ dans les faits] avant que Lean 4 ne soit opérationnel [VÉRIFIÉ dans les faits]. Cela suppose que la survie à un ensemble fini de distributions paramétriques (la « suite bon marché ») corrèle avec la validité d'une borne mathématique générale. **Ce que ferait l'expert :** En dimension infinie ou face à un adversaire adaptatif, un énoncé peut survivre à tous les mondes gaussiens ou discrets plantés et échouer sur une distribution singulière ou un adversaire non-stationnaire. L'expert inverserait le rôle des modèles : au lieu de leur faire chercher des *bornes*, il leur ferait chercher des **distributions adverses pathologiques** (maximisation de divergence sous contrainte de moments) qui cassent les moniteurs.
3. **La capacité d'auto-formalisation vers Lean 4 des abstractions statistiques [HYPOTHÈSE]** : Le programme prépare Lean 4 et Mathlib comme arbitre [VÉRIFIÉ dans les faits]. Cela suppose que les objets manipulés (processus stochastiques filtrés, couplages, sondes linéaires sur espaces d'activation) sont facilement formalisables par un LLM dans Mathlib. **Ce que ferait l'expert :** Sachant que la théorie de la mesure et des probabilités dans Mathlib est notoirement rigide (gestion des mesurabilités, intégrales de Bochner/Lebesgue) [OBSERVÉ-NON-AUDITÉ], l'expert n'utiliserait pas Lean en bout de chaîne sur du texte libre. Il définirait d'abord une **API formelle restreinte** (une vingtaine de définitions figées dans Lean : l'espace d'états, le noyau de transition du saboteur, la fonction de perte du moniteur) et interdirait aux proposeurs d'utiliser d'autres définitions.
4. **L'absence de contamination du juge de nouveauté [OBSERVÉ-NON-AUDITÉ]** : Le juge est éprouvé sur quarante énoncés connus plantés [VÉRIFIÉ dans les faits]. La question suppose que ce calibrage suffit à détecter des reformulations non triviales (changement de variables, dualité lagrangienne). L'expert imposerait une **normalisation algébrique et asymptotique** des énoncés avant tout passage au juge.

---

### 2. Les données brutes qu'il prendrait au départ

Plutôt que des résumés d'articles ou des synthèses générées par LLM, l'expert alimenterait l'organisme avec cinq types de données brutes structurées :

1. **Sous-graphes d'états de preuves de Mathlib4 (Lean 4) :** Non pas le code source en texte brut, mais les triplets `(état_tactique_avant, tactique, état_tactique_après)` extraits via un outil d'extraction de traces (comme LeanDojo) sur les répertoires précis `Mathlib.Probability`, `Mathlib.MeasureTheory`, `Mathlib.InformationTheory` et `Mathlib.LinearAlgebra`.
2. **Banques de distributions extrémales et contre-exemples paramétrés :** Un fichier de code exécutable (Python/SymPy/JAX) contenant des familles de distributions pathologiques connues en théorie des tests : mélanges de Dirac, lois à queues lourdes (Pareto, Cauchy), distributions de Rademacher couplées, matrices de covariance mal conditionnées au bord du cône semi-défini positif, et copules extrémales (co-monotone et contre-monotone).
3. **Journaux d'échecs (« Cimetière structuré ») :** Le programme mentionne qu'« un mort reste mort » [VÉRIFIÉ dans les faits]. La donnée brute doit être une table relationnelle indexant chaque tentative échouée par : `(énoncé_formel, code_évaluateur, monde_planté_tueur, trace_du_contre_exemple, vecteur_des_hypothèses_actives)`. C'est ce journal brut qui permet d'apprendre la frontière exacte où un théorème devient faux.
4. **Corpus d'inégalités sous forme d'arbres syntaxiques abstraits (AST) :** Une base de données d'inégalités fondamentales (Cauchy-Schwarz, Hölder, Jensen, Pinsker, Bretagnolle-Huber, Markov, Doob, Azuma-Hoeffding) encodées non pas en LaTeX, mais comme des règles de réécriture formelles `Hypothèses -> Terme_Gauche <= Terme_Droit`, prêtes à être chaînées mécaniquement.
5. **Traces empiriques brutes de saboteurs et de jumeaux honnêtes :** Les matrices d'activations réelles (tenseurs bruts) issues de modèles honnêtes et de modèles saboteurs sur des tâches de contrôle, afin que les « hypothèses des moniteurs » [VÉRIFIÉ dans les faits] soient testées contre la géométrie réelle des résidus, et non sur des gaussiennes idéalisées.

---

### 3. Les méthodes et outils précis : état de l'art, suppositions, résultats et échecs

Voici l'analyse critique des méthodes où des modèles de langage ont été couplés à des vérificateurs pour produire des preuves ou des constructions mathématiques. Conformément à la Règle 3, aucun identifiant arXiv n'est cité de mémoire.

#### A. Recherche guidée par programme évaluable et sélection évolutionnaire
* **Travaux de référence :** Romera-Paredes et al., 2023, *Mathematical discoveries from program search with large language models* (FunSearch) [VÉRIFIÉ] ; Novikov et al., 2025, *AlphaEvolve: A coding agent for scientific and algorithmic discovery* (titre exact à vérifier — référence à vérifier) [RAPPORTÉ].
* **Ce que cela suppose :** Que le problème mathématique se ramène à la construction d'un objet discret ou algorithmique (un graphe, un code correcteur, une fonction de priorité) et qu'il existe un évaluateur déterministe, rapide (quelques secondes) et à **score continu ou granulaire** (pas un simple booléen vrai/faux) permettant de guider la sélection darwinienne dans une base de programmes (modèle d'îles).
* **Ce que cela a donné :** Nouvelles bornes constructives pour le problème du *Cap Set* et des heuristiques de *bin packing* [VÉRIFIÉ].
* **Où cela échoue :** Échoue dès qu'il n'y a pas de gradient de récompense (paysage de fitness plat où tout programme échoue avec un score de 0 jusqu'à la solution exacte). Surtout, cette méthode **ne produit pas de théorèmes d'impossibilité universels** : elle construit des exemples (bornes inférieures constructives), mais ne prouve pas qu'aucun détecteur ne peut dépasser un seuil $\epsilon$ sur tout espace mesurable.

#### B. Recherche de preuve dans un assistant formel (Lean / Isabelle)
* **Travaux de référence :** Polu & Sutskever, 2020, *Generative Language Modeling for Automated Theorem Proving* (GPT-f) [VÉRIFIÉ] ; Lample et al., 2022, *Hypertree Proof Search for Neural Theorem Proving* (HTPS) [VÉRIFIÉ] ; Yang et al., 2023, *LeanDojo: Theorem Proving with Retrieval-Augmented Language Models* [VÉRIFIÉ] ; Trinh et al., 2024, *Solving olympiad geometry without human demonstrations* (AlphaGeometry) [VÉRIFIÉ].
* **Ce que cela suppose :** Que l'énoncé est **déjà intégralement et correctement formalisé** dans le système cible, et que toutes les définitions et lemmes de base existent dans la bibliothèque (Mathlib). Suppose également un budget de recherche en arbre (MCTS ou recherche best-first) capable d'interroger le noyau de vérification des milliers de fois par théorème.
* **Ce que cela a donné :** Résolution de problèmes d'olympiades (AMC, AIME, IMO en géométrie dédiée ou sur le benchmark MiniF2F) et automatisation de lemmes techniques locaux [VÉRIFIÉ].
* **Où cela échoue :** Explosion combinatoire dès que la preuve exige d'inventer une définition intermédiaire absente de la bibliothèque (ex. construire une martingale ad hoc ou un couplage spécifique). Dans Lean 4, la recherche échoue très souvent sur des obstructions purement bureaucratiques : unification de classes de types (*typeclass inference*), coercions entre types numériques ($\mathbb{N}, \mathbb{Z}, \mathbb{R}, \overline{\mathbb{R}}_+$), et preuves secondaires de mesurabilité ou d'intégrabilité qui polluent l'arbre de recherche.

#### C. Décomposition en lemmes (Draft, Sketch, Prove) et mémoire
* **Travaux de référence :** Jiang et al., 2022, *Draft, Sketch, and Prove: Guiding Formal Theorem Provers with Informal Proofs* (DSP) [VÉRIFIÉ] ; Wang et al., 2023, *LEGO-Prover: Neural Theorem Proving with Growing Libraries* [VÉRIFIÉ].
* **Ce que cela suppose :** Qu'un grand modèle de langage peut rédiger une preuve informelle juste dans sa structure logique, la traduire en un « squelette » formel dont les étapes sont admises via le mot-clé `sorry`, et qu'un prouveur automatique local (comme Sledgehammer dans Isabelle ou `aesop`/`linarith` dans Lean) peut combler chaque `sorry` indépendamment.
* **Ce que cela a donné :** Amélioration nette du taux de succès sur MiniF2F par rapport à la recherche tactique pure de bout en bout [VÉRIFIÉ].
* **Où cela échoue :** **Le piège du `sorry` faux.** Le LLM découpe souvent le théorème en sous-lemmes syntaxiquement valides mais **mathématiquement faux** (une hypothèse essentielle comme la bornitude ou l'indépendance conditionnelle a été oubliée dans la signature du sous-lemme). Le système gaspille alors tout son budget de calcul à essayer de prouver un sous-lemme faux, sans mécanisme natif pour remonter corriger le squelette.

#### D. Auto-formalisation et Conjecture automatique
* **Travaux de référence :** Wu et al., 2022, *Autoformalization with Large Language Models* [VÉRIFIÉ] ; Johansson & Smallbone (référence à vérifier pour l'année exacte, travaux sur QuickSpec / Hipster) [RAPPORTÉ] ; Fajtlowicz (programme Graffiti pour les conjectures en théorie des graphes, référence historique à vérifier) [RAPPORTÉ].
* **Ce que cela suppose :** Pour l'auto-formalisation : que le compilateur formel suffit à valider la traduction. Pour la conjecture automatique : qu'on peut évaluer des milliers d'invariants numériques sur une banque d'objets finis et déduire les relations d'ordre ($A \le B + C$) qui ne sont jamais violées sur la banque.
* **Ce que cela a donné :** Redécouverte de théorèmes connus et génération de conjectures ouvertes en théorie des graphes et en combinatoire extrémale [VÉRIFIÉ].
* **Où cela échoue :** **Le bogue silencieux de spécification.** Un LLM qui auto-formalise un énoncé en Lean 4 peut produire un théorème qui compile parfaitement et qu'il arrive même à prouver, parce qu'il a accidentellement introduit une hypothèse contradictoire (ex. une division par zéro qui vaut `0` par convention dans Mathlib, ou un ensemble vide) rendant le théorème **trivialement vrai par vacuité**. Le compilateur Lean vérifie la *preuve*, jamais la *fidélité sémantique de l'énoncé*.

---

### 4. Vérification externe : vrai, nouveau, utile
*(Intègre le livrable (c) : mesures minimales, taux de détection/fausses alertes, cas appariés, vérifications mécaniques à battre)*

En dehors du programme et de son directeur, la validation repose sur quatre instruments externes. Voici pour chacun son protocole et sa **mesure minimale de fonctionnement (Livrable c)** :

#### Instrument 1 : Le Vérificateur Formel (Lean 4 + Mathlib sur machine isolée) + Garde de non-vacuité
* **Fonction :** Garantir la vérité logique de l'énoncé sans faire confiance au modèle.
* **Protocole externe :** Export d'un fichier `.lean` autonome vérifié par un binaire indépendant (`lean4checker`) qui rejoue les termes de preuve au niveau du noyau sans exécuter de métaprogrammes arbitraires, interdisant `#eval`, `unsafe`, `sorry`, et vérifiant que `#print axioms NomDuTheoreme` ne contient que les axiomes standards (`propext`, `Quot.sound`, `Classical.choice`).
* **Crucial — Le test de non-vacuité (Witness Test) :** Tout théorème de la forme $\forall x, P(x) \implies Q(x)$ doit être accompagné dans le même fichier d'un théorème d'existence $\exists x, P(x)$ prouvé constructivement, prouvant que les hypothèses ne sont pas contradictoires.
* **Mesure minimale (Livrable c) :**
  * *Cas honnêtes appariés vs Saboteurs :* 50 paires de théorèmes (illustratif) : dans chaque paire, un théorème valide et sa version sabotée par un changement subtil de définition (ex. une variable réelle déclarée en entier naturel $\mathbb{N}$ où $a - b = 0$ si $a < b$, ou une hypothèse implicite contradictoire rendant la prémisse fausse).
  * *Métrique :* Taux de détection des preuves invalides ou vacantes $\ge 99\%$ (illustratif), taux de fausses alertes sur preuves valides instanciées $= 0\%$ (illustratif).
  * *Vérification mécanique à battre :* La simple compilation `lake build` standard de Lean 4 (qui accepte sans broncher les théorèmes vrais par vacuité ou par pathologie de division par zéro dans Mathlib).

#### Instrument 2 : Le Harnais de Preuve Rejouable et l'Étage de Tests de Mort (L'adversaire numérique)
* **Fonction :** Vérifier l'utilité opérationnelle et la justesse avant ou en complément de la preuve formelle.
* **Protocole externe :** Pour toute borne proposée (ex. « sous corrélation $\rho$, le taux de fausses alertes du moniteur agrégé est au moins $f(\rho)$ »), un script déterministe (graine fixée, conteneur Docker scellé) instancie le pire cas prédit par le théorème et simule l'agrégateur sur $N$ tirages.
* **Mesure minimale (Livrable c) :**
  * *Cas honnêtes appariés :* Les 12 mondes mathématiques plantés à vérité calculée du pilote [VÉRIFIÉ dans les faits], en appariant pour chaque monde un énoncé exact (jumeau honnête) et un énoncé dont la constante ou l'exposant est violé de $10\%$ (illustratif).
  * *Métrique :* Taux de rejet (mort) des énoncés faux $\ge 95\%$ (illustratif) ; taux de survie des énoncés vrais $= 100\%$ (illustratif, un seul contre-exemple exact tue un théorème universel).
  * *Vérification mécanique à battre :* Le bras « lecture nue » par un juge LLM [VÉRIFIÉ dans les faits] ET un test de Monte-Carlo naïf à distribution uniforme (sans optimisation adverse par gradient ou programmation linéaire).

#### Instrument 3 : L'Extracteur d'Antériorité et Juge de Nouveauté (Recherche d'isomorphismes)
* **Fonction :** Vérifier que le résultat n'est pas un théorème connu déguisé.
* **Protocole externe :** Canonicalisation de l'énoncé (suppression du jargon « saboteur / sonde / moniteur » au profit du langage standard de la théorie de la mesure : variables aléatoires, filtrations, divergences $f$), suivie d'une recherche dans Mathlib (`loogle`, `Moogle`), arXiv et MathSciNet/zbMATH, doublée d'une tentative de preuve directe en une seule étape par les tactiques d'automatisation de Lean (`exact?`, `apply?`, `aesop`, `linarith`, `positivity`). **Si `exact?` ou `aesop` prouve le théorème en moins de 5 secondes (illustratif), le résultat n'est pas nouveau.**
* **Mesure minimale (Livrable c) :**
  * *Cas honnêtes appariés :* Les 40 énoncés connus plantés du pilote [VÉRIFIÉ dans les faits] (maquillés par changement de notation et de domaine) appariés à 40 variantes structurellement modifiées (ajout d'une contrainte de budget ou de corrélation non standard) (illustratif).
  * *Métrique :* Taux de détection des théorèmes connus maquillés $\ge 90\%$ (illustratif) ; taux de fausses alertes sur les variantes réellement distinctes $\le 10\%$ (illustratif).
  * *Vérification mécanique à battre :* Recherche par similarité cosinus d'embeddings textuels bruts et recherche plein texte par mots-clés (qui échouent dès qu'on renomme « martingale » en « processus d'audit séquentiel »).

#### Instrument 4 : Relecture humaine en aveugle et Réplication
* **Fonction :** Valider l'intérêt mathématique (la profondeur) au-delà de la simple nouveauté technique.
* **Protocole externe :** La relecture humaine étant rare [VÉRIFIÉ dans les faits], un mathématicien externe reçoit uniquement les théorèmes qui ont survécu aux Instruments 1, 2 et 3, présentés sous forme standardisée (énoncé LaTeX + preuve Lean compilée + code du monde planté où la borne est serrée), mélangés à des théorèmes humains récents non publiés. Il évalue si la borne améliore l'état de l'art ou si c'est une variation triviale.

---

### 5. Reformulation de la demande

À la lumière de ce qui précède, la demande initiale du programme (« *produire des mathématiques nouvelles pour le contrôle d'agents saboteurs via un organisme de modèles de langage* ») est mal posée car trop ouverte aux hallucinations sémantiques et aux redécouvertes triviales. Voici sa reformulation rigoureuse et opératoire :

> **Demande reformulée :**
> « Étant donné une interface formelle figée dans Lean 4 (définissant un espace d'états cachés, un canal d'observation linéaire bruité, une famille de moniteurs corrélés et un budget d'audit séquentiel) et un banc d'essai de $K$ familles de distributions paramétrées exécutables :
> 1. **Construire par programmation évolutive** des distributions d'attaque (couplages de corrélation adverse, stratégies de sabotage séquentiel) qui maximisent l'erreur des moniteurs existants sous contrainte d'indiscernabilité vis-à-vis du jumeau honnête ;
> 2. **Extraire automatiquement de ces pires cas numériques** des invariants algébriques (conjectures de bornes d'impossibilité ou de garanties en échantillon fini) ;
> 3. **Démontrer formellement ces bornes dans Lean 4** par décomposition en lemmes dont chaque sous-but est pré-filtré numériquement par la suite bon marché avant tout appel au prouveur formel, en garantissant la non-vacuité des hypothèses et l'irréductibilité aux lemmes triviaux de Mathlib. »

---

### 6. Propositions concrètes de méthodes, Expériences décisives (Inférence forte) et Ancrage matériel
*(Intègre les livrables (b) et (d) ainsi que le point 6 de la Question)*

Pour que l'organisme produise des résultats inédits sur ses cinq questions cibles [VÉRIFIÉ dans les faits] avec un budget de quelques centaines de dollars par course et peu de relecture humaine [VÉRIFIÉ dans les faits], je propose **trois méthodes complémentaires**.

---

#### Méthode 1 : La Boucle de Dualité Selle-Point (« Adversaire Constructif $\leftrightarrow$ Prouveur de Borne »)
*Cible principale : Agrégateur sous corrélation adverse, lemme d'impossibilité, sonde qui ne lit que l'indication.*

* **Principe :** Toute borne d'impossibilité ou de minimax en détection est un point-selle : $\inf_{\text{Moniteur}} \sup_{\text{Saboteur}} \text{Risque} = V^*$. Au lieu de demander à un LLM de deviner $V^*$ dans le vide, on fait jouer deux moteurs numériques l'un contre l'autre :
  * Le **Bras A (type FunSearch)** génère du code Python/JAX qui construit explicitement une matrice de corrélation adverse ou une distribution de sabotage qui fait échouer le moniteur tout en trompant la sonde linéaire. Cela donne une borne inférieure numérique constructive $L$.
  * Le **Bras B (Conjectueur symbolique)** observe la structure analytique de la distribution gagnante du Bras A (ex. « la matrice de covariance gagnante est constante hors diagonale et sature la condition de semi-définie positivité ») et propose une formule fermée pour la borne supérieure théorique $U$ (via dualité lagrangienne ou inégalité de Fano/Pinsker).
  * Lorsque l'écart numérique $|U - L| < 10^{-4}$ (illustratif) sur tous les mondes plantés, la conjecture est gelée et envoyée au prouveur Lean 4.
* **Premier pas :** Implémenter en Python (scipy/cvxpy) le problème d'optimisation convexe qui cherche la pire loi jointe de $M$ détecteurs binaires à marges fixées (problème de transport optimal discret / bornes de Fréchet) sur les 12 mondes plantés du pilote [VÉRIFIÉ dans les faits].
* **Coût en ordre de grandeur :** $\sim 30\text{ \$ à } 80\text{ \$}$ par course (illustratif) en appels API ou inférence locale, car 95 % du travail est du calcul matriciel CPU très peu coûteux.
* **Test de mort (ce qui la tuerait) :** Si, après $1\,000$ générations (illustratif) sur les 12 mondes plantés, l'écart de dualité numérique $|U - L|$ reste supérieur à $15\%$ (illustratif), ou si le Bras B s'avère incapable d'interpoler une expression analytique exacte à partir des solutions numériques du Bras A sur des cas connus (comme le lemme de Neyman-Pearson ou la borne de Chernoff).
* **Ce qui la distingue de l'état de l'art :** FunSearch (Romera-Paredes et al., 2023) ne fait que le Bras A (recherche d'objets constructifs) sans extraire ni prouver la borne d'impossibilité duale. Les prouveurs formels (HTPS, LeanDojo) ne font que la preuve d'un énoncé donné sans jamais découvrir la constante optimale par jeu adverse.

---

#### Méthode 2 : Décomposition en lemmes filtrée par contre-exemples (« Squelette Élagué avant Preuve »)
*Cible principale : Plafond d'horizon, détection séquentielle à faible taux de fausses alertes en échantillon fini.*

* **Principe :** Résoudre le point d'échec majeur de *Draft, Sketch, and Prove* (Jiang et al., 2022), où le système s'épuise à prouver en Lean des sous-lemmes faux. Ici, chaque fois qu'un proposeur décompose un théorème $T$ en sous-lemmes $L_1, L_2, \dots, L_k$ (avec $L_1 \wedge \dots \wedge L_k \implies T$ vérifié par Lean avec des `sorry` sur chaque $L_i$), **interdiction d'appeler le prouveur Lean sur $L_i$ tant que $L_i$ n'a pas survécu à l'étage des tests de mort numériques** (traduction automatique de $L_i$ en assertion Python/Hypothesis/Z3 testée contre la banque de distributions pathologiques). Si un sous-lemme $L_i$ est tué par un contre-exemple numérique, le contre-exemple exact est réinjecté dans le prompt du proposeur (« *Ton lemme $L_2$ est faux pour la loi de Pareto de paramètre $\alpha=1.5$ ; corrige l'énoncé de $L_2$ en ajoutant l'hypothèse de moment manquante* »).
* **Premier pas :** Brancher le bras « suite bon marché » existant du pilote [VÉRIFIÉ dans les faits] non pas uniquement sur l'énoncé final, mais comme **portier obligatoire devant chaque `sorry`** d'un squelette de preuve Lean 4.
* **Coût en ordre de grandeur :** $\sim 50\text{ \$ à } 150\text{ \$}$ par théorème candidat (illustratif). Le filtre numérique coûte quelques centimes de CPU et économise des dizaines d'heures de recherche MCTS stérile dans Lean 4.
* **Test de mort (ce qui la tuerait) :** Si plus de $50\%$ (illustratif) des sous-lemmes intermédiaires générés en Lean 4 portent sur des propriétés purement abstraites (ex. mesurabilité d'une tribu, topologie) non traduisibles en assertions numériques ou symboliques testables par la suite bon marché.
* **Ce qui la distingue de l'état de l'art :** Dans DSP (Jiang et al., 2022) et LEGO-Prover (Wang et al., 2023), la validation des sous-lemmes est purement déductive (le prouveur formel essaie et échoue par timeout, sans savoir si le lemme est faux ou juste trop difficile). Ici, l'échec est **réfutatif et informatif** : le test de mort distingue un lemme *faux* (tué en 0,1 seconde avec un contre-exemple) d'un lemme *vrai mais difficile à prouver*.

---

#### Méthode 3 : Mutation d'hypothèses à l'envers (« Lecture Inverse des Théorèmes d'Impossibilité »)
*Cible principale : Clôture d'une archive pour un juge, lemme d'impossibilité, valeur du jeu d'audit sous budget.*

* **Principe :** Le programme note déjà l'idée de « théorèmes d'impossibilité lus à l'envers, dont les hypothèses nommées sont les suppositions des moniteurs » [VÉRIFIÉ dans les faits]. Concrètement, on part d'un théorème classique déjà formalisé (ou facile à formaliser) dans Mathlib ou dans l'archive : par exemple l'inégalité de traitement de l'information (Data Processing Inequality), le lemme de décomposition orthogonale pour les sondes linéaires, ou l'inégalité de Wald pour les tests séquentiels. Un opérateur syntaxique retire ou affaiblit systématiquement une hypothèse $H_k$ (ex. remplacer l'indépendance des moniteurs par une corrélation bornée par $\rho$, ou remplacer l'espace entier par le noyau de la sonde linéaire). L'étage des tests de mort cherche immédiatement le contre-exemple qui brise l'ancien théorème. Le proposeur doit alors **calculer le terme correctif exact $\Delta(\rho)$** à ajouter à l'inégalité pour qu'elle redevienne vraie sur tous les mondes plantés, puis adapter la preuve Lean existante par réparation locale (diff de preuve).
* **Premier pas :** Encoder 10 inégalités fondamentales de théorie de l'information et des martingales (illustratif) sous forme modulaire dans Lean 4 et dans la suite Python, et automatiser la suppression d'une hypothèse à la fois.
* **Coût en ordre de grandeur :** $\sim 20\text{ \$ à } 60\text{ \$}$ par course (illustratif), car on ne cherche pas une preuve à partir d'une feuille blanche : on édite une preuve existante (réparation de preuve guidée par les erreurs du compilateur Lean).
* **Test de mort (ce qui la tuerait) :** Si la réparation d'une preuve Lean après affaiblissement d'une hypothèse échoue dans plus de $90\%$ des cas (illustratif) parce que la preuve du théorème affaibli exige une technique mathématique radicalement différente de celle du théorème original (discontinuité méthodologique).
* **Ce qui la distingue de l'état de l'art :** Les travaux de réparation de preuves (comme Baldur : First et al., 2023, *Baldur: Whole-Proof Generation and Repair with Large Language Models* [VÉRIFIÉ]) réparent des preuves *pour un énoncé fixe*. Ici, on mute conjointement l'énoncé (le terme correctif $\Delta$) et la preuve pour explorer le voisinage théorique d'un résultat connu.

---

#### Expériences décisives en inférence forte (Livrable b — Règle B4)

Pour trancher scientifiquement la viabilité de ces méthodes sur le matériel déjà conçu (les 12 mondes plantés et les 40 énoncés connus du pilote [VÉRIFIÉ dans les faits]), voici trois expériences en duel $H_A$ contre $H_B$ :

##### Expérience 1 : Utilité du filtre de mort au niveau des sous-lemmes (Méthode 2 vs DSP standard)
* **Duel d'hypothèses :**
  * $H_A$ : Le filtrage numérique de chaque sous-lemme `sorry` par la « suite bon marché » avant appel au prouveur formel augmente le taux de théorèmes complets prouvés à budget de calcul constant, car il élimine les branches mortes où le LLM a halluciné un sous-lemme faux.
  * $H_B$ : Le coût de traduction des sous-lemmes vers la suite numérique et les faux rejets (erreurs de traduction Python) consomment le budget sans gain net par rapport à l'allocation directe de tout le budget de calcul à la recherche d'arbre dans Lean 4 (DSP standard).
* **Protocole et Métrique :** Sur 20 théorèmes de probabilité/algèbre linéaire à difficulté graduée issus des 12 mondes plantés [VÉRIFIÉ dans les faits] (niveau licence/master, dont la preuve demande 3 à 6 lemmes intermédiaires, illustratif), comparer à budget strictement égal ($50\text{ \$}$ d'inférence et 20 heures-CPU par bras, illustratif) : (1) le taux de preuves Lean 4 complètes sans `sorry`, et (2) la proportion de temps CPU passée par Lean à tenter de prouver des sous-lemmes mathématiquement faux.
* **Seuil de décision :** Gain absolu $\ge +20\%$ (illustratif, soit au moins 4 théorèmes supplémentaires prouvés sur 20) et réduction d'au moins $50\%$ (illustratif) du temps perdu sur des sous-lemmes faux.
* **Contrôle négatif :** Injecter délibérément 20 squelettes de preuve contenant chacun un sous-lemme subtil mais mathématiquement faux (ex. inégalité de Jensen dans le mauvais sens pour une fonction concave). Vérifier que le filtre de mort en tue au moins 18 sur 20 (illustratif) en moins de 10 secondes chacun.
* **Falsification :**
  * Si le bras filtré résout au moins 4 théorèmes de plus que le bras DSP pur et tue $\ge 90\%$ des contrôles négatifs $\implies$ **$H_B$ est falsifiée** (le goulot d'étranglement était bien la fausseté mathématique des sous-lemmes).
  * Si le gain est $< 10\%$ ou si plus de $30\%$ des sous-lemmes légitimes échouent à être traduits en tests exécutables $\implies$ **$H_A$ est falsifiée** (la Méthode 2 est abandonnée au profit d'une recherche purement formelle).

##### Expérience 2 : Découverte par dualité Selle-Point contre Conjecture directe en boucle (Méthode 1 vs Génération directe)
* **Duel d'hypothèses :**
  * $H_A$ : La co-évolution d'un programme construisant la distribution adverse (borne inférieure numérique $L$) et d'un proposeur d'énoncés (borne supérieure analytique $U$) produit des bornes plus serrées (plus proches de la vérité calculée des mondes plantés) qu'un proposeur d'énoncés couplé uniquement à un vérificateur booléen (vrai/faux) de tests de mort.
  * $H_B$ : Un proposeur LLM guidé uniquement par le verdict binaire (survie/mort) de la suite bon marché et son mémoire des tentatives (« un mort reste mort » [VÉRIFIÉ dans les faits]) converge aussi vite vers la borne optimale par dichotomie ou intuition pré-entraînée, rendant le moteur d'optimisation adverse (Bras A) superflu.
* **Protocole et Métrique :** Sur les 12 mondes mathématiques plantés à vérité calculée $V^*$ du pilote [VÉRIFIÉ dans les faits], mesurer après 200 itérations par monde (illustratif) l'**écart d'optimalité relatif** $\delta = \frac{|U_{\text{survivant}} - V^*|}{|V^*|}$ de la meilleure borne valide survivante (une borne lâche comme $P \le 1$ survit aux tests de mort mais a un écart $\delta$ catastrophique).
* **Seuil de décision :** L'écart médian $\delta$ sur les 12 mondes doit être $\le 5\%$ (illustratif) pour la Méthode 1 et inférieur d'au moins un facteur 3 (illustratif) à l'écart du bras binaire.
* **Contrôle négatif :** Un proposeur « conservateur trivial » qui propose systématiquement des bornes triviales universellement vraies (ex. probabilité $\le 1$, variance $\ge 0$). Il doit avoir un taux de survie aux tests de mort de $100\%$, mais être immédiatement éliminé par la métrique d'écart de dualité $|U - L|$.
* **Falsification :**
  * Si la Méthode 1 atteint $\delta \le 5\%$ sur au moins 9 des 12 mondes alors que le bras binaire stagne sur des bornes lâches ($\delta > 15\%$) $\implies$ **$H_B$ est falsifiée** (un test de mort binaire seul encourage des théorèmes vrais mais faibles ; la pression adverse constructive est indispensable).
  * Si le bras binaire atteint le même écart $\delta$ à $\pm 5\%$ près pour un coût moindre $\implies$ **$H_A$ est falsifiée** (l'usine évolutive de distributions adverses est abandonnée).

##### Expérience 3 : Juge de nouveauté algébrique/tactique contre Juge LLM par lecture/embedding (Instrument 3)
* **Duel d'hypothèses :**
  * $H_A$ : Un juge de nouveauté purement basé sur un LLM (lecture nue ou similarité d'embeddings) se laisse tromper par un renommage de domaine (traduire un théorème classique de martingales en jargon « audit séquentiel de saboteur »), alors qu'un filtre de canonicalisation suivi d'une recherche de preuve en une étape dans Lean (`exact?`, `aesop`) et de tests d'équivalence symbolique (SymPy) détecte la redécouverte.
  * $H_B$ : Le juge LLM du pilote (éprouvé sur 40 énoncés connus plantés [VÉRIFIÉ dans les faits]) possède déjà une capacité d'abstraction sémantique suffisante pour reconnaître les théorèmes classiques même sous un fort maquillage terminologique et algébrique.
* **Protocole et Métrique :** Prendre les 40 énoncés connus plantés du pilote [VÉRIFIÉ dans les faits]. Appliquer à chacun trois niveaux de camouflage : (N1) renommage lexical complet vers le jargon du contrôle d'IA ; (N2) changement de variable algébrique inversible (ex. passer des probabilités $p$ aux log-odds $\ln(p/(1-p))$) ; (N3) passage à la contraposée. Y mêler 40 énoncés réellement modifiés (changement structurel de la borne). Mesurer l'aire sous la courbe ROC (AUC) et le taux de faux positifs de nouveauté (accepter un théorème connu camouflé comme nouveau).
* **Seuil de décision :** Sur les niveaux N2 et N3, le taux de faux positifs de nouveauté doit être $\le 10\%$ (illustratif).
* **Contrôle négatif :** Soumettre 20 identités algébriques élémentaires (ex. $(a+b)^2 \ge 4ab$) réécrites sous forme de théorèmes sur « l'énergie de deux sondes linéaires orthogonales ». Tout juge fonctionnel doit les rejeter à $100\%$ comme triviaux.
* **Falsification :**
  * Si le juge LLM laisse passer plus de $25\%$ (illustratif) des énoncés camouflés N2/N3 alors que le pipeline (Canonicalisation + SymPy + `aesop`) en rejette $\ge 90\%$ $\implies$ **$H_B$ est falsifiée** (le juge LLM ne doit jamais être utilisé seul comme portier de nouveauté).
  * Si le juge LLM obtient un taux de rejet $\ge 90\%$ sur N2/N3 et que le pipeline formel échoue à s'exécuter sur plus de $40\%$ des cas à cause d'erreurs de formalisation $\implies$ **$H_A$ est falsifiée**.

---

#### Ancrage matériel et budget (Livrable d)

Tous les chiffres ci-dessous qui ne proviennent pas du bloc FAITS sont marqués **(illustratif)**. Le budget imposé par les faits est de « quelques centaines de dollars par course » [VÉRIFIÉ dans les faits].

1. **Modèles ouverts et propriétaires (les cinq lignées [VÉRIFIÉ dans les faits]) :**
   * *Modèles ouverts spécialisés code/maths et Lean 4 (exécutables localement ou sur GPU loués à l'heure) :* DeepSeek-Prover-V1.5-RL (7B) ou DeepSeek-R1-Distill / Qwen2.5-Math-72B-Instruct, InternLM2-Math-Plus (20B/7B), Kimina-Prover ou LeanDojo-ByT5 pour la génération de tactiques Lean 4 [OBSERVÉ-NON-AUDITÉ pour leur disponibilité exacte sur le serveur isolé].
   * *Modèles généralistes de raisonnement (pour la décomposition en lemmes et le Bras A Python) :* Combinaison de modèles ouverts lourds (Llama-3.3-70B-Instruct, Qwen2.5-Coder-32B) et d'appels API ciblés (pour les lignées distinctes) dans l'enveloppe budgétaire.
2. **Infrastructure de calcul nécessaire :**
   * *Machine isolée pour l'arbitre formel [VÉRIFIÉ dans les faits] :* 1 serveur CPU à forte mémoire vive (32 à 64 cœurs CPU, 128 Go de RAM — illustratif) est beaucoup plus important qu'un gros cluster GPU pour Lean 4 + Mathlib, car la vérification de types et les tactiques comme `aesop` ou `omega` sont massivement liées au CPU et à la RAM (chargement des `.olean` de Mathlib).
   * *Nœud d'inférence pour modèles ouverts et suite bon marché :* 2 à 4 GPU A100 (80 Go) ou H100 (illustratif) à la demande pour servir les modèles 7B–72B en parallèle (via vLLM/SGLang) et exécuter les optimisations JAX/PyTorch des mondes plantés.
3. **Décomposition du coût estimé pour une course complète sur une question cible (Total : $\sim 220\text{ \$}$, illustratif — conforme au budget de « quelques centaines de dollars par course » [VÉRIFIÉ dans les faits]) :**
   * *Étape 1 (Méthode 1 — Boucle Selle-Point numérique sur les 12 mondes plantés, $2\,000$ programmes évalués) :* 4 heures sur 1 GPU + 16 cœurs CPU $\approx 15\text{ \$}$ de calcul + $25\text{ \$}$ d'inférence LLM $\approx \mathbf{40\text{ \$}}$ (illustratif).
   * *Étape 2 (Méthode 2 — Génération de 30 squelettes de preuve et filtrage numérique des `sorry` par la suite bon marché) :* 3 heures CPU + appels aux 5 lignées de proposeurs $\approx \mathbf{60\text{ \$}}$ (illustratif).
   * *Étape 3 (Preuve formelle Lean 4 + Mathlib sur les 5 squelettes survivants ayant passé tous les tests de mort) :* Recherche arborescente avec modèle de tactiques local (7B) sur 2 GPU + 32 cœurs CPU pendant 12 heures $\approx \mathbf{90\text{ \$}}$ (illustratif).
   * *Étape 4 (Filtre d'antériorité, tests de non-vacuité et empaquetage pour relecture humaine) :* $\approx \mathbf{30\text{ \$}}$ (illustratif).

---

#### Honnêteté sur la part de temps, d'effort humain et de chance (Point 6 de la Question)

Il faut être totalement transparent sur ce qu'un tel organisme peut et ne peut pas faire en l'état actuel des connaissances :

1. **La part d'effort humain caché (70 % du succès — illustratif) :** L'idée qu'un organisme d'agents va découvrir des mathématiques nouvelles en autonomie complète à partir d'une question en français est une illusion. Dans tous les succès publiés (FunSearch, AlphaGeometry), **l'essentiel de l'intelligence mathématique humaine a été injecté en amont dans la conception de l'interface scellée, le choix de la représentation du problème et la fonction d'évaluation**. Si un mathématicien humain ne passe pas deux à trois semaines (illustratif) à définir proprement dans Lean 4 les types exacts du jeu d'audit ou du modèle de sonde linéaire et à coder des mondes plantés riches, l'organisme passera 100 % de son budget à exploiter des failles de spécification (trouver des théorèmes triviaux ou dégénérés).
2. **Ce qui sera automatisé vs ce qui demandera un humain :**
   * L'organisme sera redoutablement efficace pour **trouver des contre-exemples** aux conjectures naïves, **optimiser des constantes** dans des inégalités existantes (Méthode 1), et **assembler des lemmes techniques connus** (inégalités de concentration, bornes de matrices) dans des configurations nouvelles (Méthodes 2 et 3).
   * En revanche, si la résolution d'une des cinq questions cibles exige d'**inventer un concept mathématique nouveau** (une nouvelle définition structurelle qui n'est pas une combinaison syntaxique simple de concepts de Mathlib), je ne sais pas comment un système actuel à base de LLM pourrait le faire de manière fiable sans intervention humaine.
3. **La part de temps et de chance :**
   * *Temps de mise en conformité de l'outillage :* Relevé conforme du harnais Lean 4 + Mathlib [VÉRIFIÉ dans les faits : non encore relevé conforme] et écriture des définitions de base des 5 questions cibles = **3 à 6 semaines d'ingénierie formelle humaine** (illustratif).
   * *Taux de déchet (chance) :* Même avec l'étage des tests de mort, il faut s'attendre à ce que sur 10 courses complètes ($\sim 2\,000\text{ \$}$, illustratif), 7 ou 8 courses (illustratif) convergent vers des résultats qui sont soit des reformulations de résultats connus en statistique mathématique, soit des bornes techniquement nouvelles mais trop lâches pour être utiles, et que seulement **1 ou 2 courses** (illustratif) produisent un lemme serré, non trivial et formellement vérifié. La découverte réelle résidera souvent non pas dans la preuve Lean finale, mais dans le **contre-exemple inattendu** que l'étage de tests de mort aura construit en tuant une conjecture que les chercheurs humains croyaient vraie.

FIN-DE-CELLULE