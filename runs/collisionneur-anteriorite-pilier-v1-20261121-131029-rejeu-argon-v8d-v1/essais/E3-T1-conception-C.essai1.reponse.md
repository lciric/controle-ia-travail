*Note d'intégrité (Règle 2) : Tour III.1 à l'aveugle ; les propositions A, B, D et E ne sont pas transmises à ce stade du protocole [VÉRIFIÉ].*

---

## 1. Ce que la question suppose sans que ce soit établi (Livrable III.1.a) et ce qu'un expert ferait ici sans qu'on le lui demande (Point 1 de l'Arbitre)

### 1.1. Présupposés non établis de la question
La formulation du dilemme entre (a), (b) et (c) repose sur six présupposés implicites dont aucun n'est établi dans les faits :

1. **Homogénéité du risque de collision entre les trois formes de cibles** : La question suppose qu'un « objet à score exact », un « énoncé à démontrer ou réfuter » et un « lemme de bibliothèque » [RAPPORTÉ] présentent le même profil de collision bibliographique et requièrent le même moment de lecture [HYPOTHÈSE]. Or, leur vulnérabilité à l'antériorité diffère structurellement (voir 1.2).
2. **Fiabilité de l'« empreintage » textuel par un agent** : L'option (a) suppose qu'un agent lisant des articles en langage naturel/LaTeX produit des empreintes (« articles lus et empreintés ») capables de détecter l'équivalence mathématique avec une cible avant son scellement [HYPOTHÈSE]. En statistique mathématique et en théorie des jeux, le polymorphisme notationnel (cryptomorphisme) met en échec la similarité textuelle ou vectorielle directe [HYPOTHÈSE].
3. **Invisibilité des collisions par spécialisation (subsomption)** : La question traite la collision comme une identité d'énoncés [HYPOTHÈSE], alors que le cas fréquent en recherche est qu'un théorème publié $T^*$ implique trivialement la cible $T$ comme corollaire (en fixant un paramètre ou une filtration), sans que $T$ n'apparaisse explicitement dans l'article [HYPOTHÈSE].
4. **Indépendance entre lecture d'antériorité et vérité de l'énoncé** : Pour une cible de type « énoncé à démontrer ou réfuter » [RAPPORTÉ], ignorer un article de 2026 [RAPPORTÉ] avant de sceller la cible ne crée pas seulement un risque de doublon : cela prive le concepteur de savoir *quel sens* (démonstration ou réfutation) est déjà tranché, exposant le budget à être dépensé sur une direction déjà résolue [HYPOTHÈSE].
5. **Rapport de coût implicite ($C_{\text{preuve}} \gg C_{\text{veille}}$)** : L'option (a) suppose que le coût de calcul et d'effort pour tenter de résoudre une cible dépasse largement le coût de lecture préalable d'une zone entière [HYPOTHÈSE], tandis que l'option (b) suppose l'inverse [HYPOTHÈSE]. Ce rapport n'est pas mesuré dans les faits (je ne sais pas quel est le budget exact alloué par cible).
6. **Stationnarité de l'antériorité après scellement** : L'option (a) suppose qu'une cible vérifiée neuve avant son scellement le restera jusqu'à la revendication [HYPOTHÈSE], alors que l'existence de plusieurs travaux voisins de 2026 croisés par hasard [RAPPORTÉ] indique une concurrence active pendant la durée même du programme [HYPOTHÈSE].

### 1.2. Ce qu'un expert du domaine ferait immédiatement (et qu'on ne demande pas)
Un mathématicien ou statisticien expérimenté confronté au gel de la veille [RAPPORTÉ] ne choisirait ni une lecture exhaustive de cinq zones (a), ni l'aveuglement jusqu'à la première revendication (b). Il exécuterait quatre opérations que la question omet :

1. **Stratifier le protocole par la *forme* de la cible (et non par zone thématique)** :
   * *Pour un « objet à score exact »* [RAPPORTÉ] (ex. règle de décision trouvée par recherche de programmes, stratégie explicite d'un jeu d'inspection sous budget) : l'expert ne lit pas les preuves de la littérature. Il extrait uniquement le **meilleur score numérique publié (la ligne de base ou *baseline*)**. Dès que ce seuil numérique est vérifié, la cible est scellée. Tout programme ou objet valide qui bat strictement ce score exact est constructivement neuf par définition de la métrique [HYPOTHÈSE].
   * *Pour un « lemme de bibliothèque »* [RAPPORTÉ] : sa valeur réside dans son intégration formelle à la bibliothèque Lean publique de statistique [RAPPORTÉ]. L'expert ne fait aucune veille papier : il interroge uniquement l'arbre de types de Lean 4 / Mathlib4. Si le lemme manque à l'édifice formel, la cible est valide même si le résultat mathématique sous-jacent est un exercice classique de martingale [HYPOTHÈSE].
   * *Pour un « énoncé à démontrer ou réfuter »* [RAPPORTÉ] : c'est la seule catégorie où la collision papier détruit toute la valeur de la cible. L'expert concentre $90\%$ (illustratif) de l'effort bibliographique exclusivement sur cette forme.
2. **Dépouiller en priorité absolue le « noyau chaud 2026 » déjà repéré** : Les faits mentionnent que « plusieurs travaux voisins de 2026 ont été croisés par hasard, sans être lus » [RAPPORTÉ]. Laisser ces articles identifiés non lus tout en débattant d'une veille générale sur cinq zones est une faute méthodologique : ces articles de 2026, augmentés de leur graphe de citations à $1$ saut (articles qu'ils citent et qui les citent), contiennent la probabilité maximale de collision directe avec le programme [HYPOTHÈSE].
3. **Canoniser les énoncés dans le vocabulaire de la bibliothèque Lean *avant* de chercher l'antériorité** : Puisqu'une bibliothèque Lean publique couvre déjà divergences, Fano, Bretagnolle–Huber, identité de Wald et e-valeurs [RAPPORTÉ], l'expert force chaque cible candidate à s'exprimer comme une signature de type sur ces primitives exactes *avant* l'empreintage. Cela élimine les illusions de nouveauté dues à un simple changement de notation entre la théorie de l'information et les tests séquentiels [HYPOTHÈSE].
4. **Exécuter un filtre de réfutation numérique sur petit support *avant* toute lecture bibliographique** : Avant de chercher pendant des heures si un « énoncé à démontrer ou réfuter » existe dans la littérature, l'expert lance un solveur numérique (optimisation sous contraintes ou recherche de contre-exemple sur un espace d'états fini à $2$ ou $3$ points (illustratif) et un horizon $T \le 4$ (illustratif)). Si un contre-exemple élémentaire réfute l'énoncé en $5$ minutes (illustratif), l'énoncé était mal posé : on économise à la fois la veille bibliographique et le budget de preuve [HYPOTHÈSE].

---

## 2. Les données brutes de départ (Point 2 de l'Arbitre)

Pour alimenter la recherche d'antériorité sur les cinq zones [RAPPORTÉ], les sources brutes se divisent en quatre strates techniques :

1. **Bases d'articles et graphes de citations** :
   * *Sources LaTeX brutes (arXiv)* : Dépôts sources `.tex` et `.bbl` (et non les seuls PDF, qui dégradent les formules) sur les catégories `math.ST` (Statistics Theory), `stat.ME` (Methodology), `cs.IT` (Information Theory), `cs.GT` (Computer Science and Game Theory) et `cs.LG` (Machine Learning) [VÉRIFIÉ].
   * *Bases indexées à taxonomie fine* : zbMATH Open (accès ouvert [VÉRIFIÉ]) et MathSciNet (accès par abonnement [VÉRIFIÉ]), filtrés par codes MSC2020 : `62L10` (analyse séquentielle), `62C20` (décision minimax), `62G10` (tests d'hypothèses non paramétriques), `94A17` (mesures d'information et divergences), `91A68` (jeux algorithmiques et d'inspection) [VÉRIFIÉ].
   * *Graphes bibliométriques ouverts* : OpenAlex et Semantic Scholar API [VÉRIFIÉ] pour extraire instantanément la clôture transitive à $1$ ou $2$ sauts (illustratif) autour des travaux de 2026 croisés par hasard [RAPPORTÉ] et des articles fondateurs de la bibliothèque Lean (ex. Abraham Wald (1945), *Sequential Tests of Statistical Hypotheses* [VÉRIFIÉ] ; Jean Bretagnolle et Catherine Huber (1979), *Estimation des densités : risque minimax* [VÉRIFIÉ] ; Vladimir Vovk et Ruodu Wang (2021), *E-values: Calibration, combination and applications* [VÉRIFIÉ]).
2. **Bibliothèques formelles et index de types** :
   * Le dépôt Git de la bibliothèque Lean publique de statistique du programme [RAPPORTÉ] (incluant ses branches non fusionnées, ses *issues*, ses PR et ses blocs `sorry` ou `todo` [HYPOTHÈSE]).
   * `Mathlib4` (en particulier les dossiers `Mathlib.MeasureTheory`, `Mathlib.Probability`, `Mathlib.InformationTheory`) [VÉRIFIÉ].
   * Les index de recherche par type et par sémantique de l'écosystème Lean 4 : `Loogle` (recherche par motifs d'expressions et signatures de types), `LeanSearch` et `Moogle` (recherche sémantique vers Mathlib4), ainsi que `Reservoir` (registre des paquets Lean 4 publics) [VÉRIFIÉ].
3. **Listes de problèmes ouverts et littérature grise** :
   * Les sections « Open Problems » des actes de COLT (*Conference on Learning Theory*, publiés dans PMLR) [VÉRIFIÉ], qui publient régulièrement des conjectures sur les e-valeurs, les bandits et les tests séquentiels.
   * Les rapports d'ateliers spécialisés (Oberwolfach Reports, Dagstuhl Reports, Simons Institute workshops sur l'inférence séquentielle valide à tout instant et la théorie des jeux de sécurité — référence à vérifier pour les éditions 2025–2026).
   * Les billets de synthèse et fils techniques sur MathOverflow (tags `math.ST`, `martingales`, `game-theory`, `inequalities`) [VÉRIFIÉ].
4. **Notices de bancs (*benchmarks*) pour objets à score exact** :
   * Pour la fusion de p-valeurs et d'e-valeurs sous dépendance : les tables de constantes des calibrateurs admissibles et fonctions de fusion symétriques/asymétriques (au sens de Vovk et Wang (2021), *E-values: Calibration, combination and applications* [VÉRIFIÉ]).
   * Pour la recherche de programmes appliquée aux règles de décision : les dépôts de bancs de découverte algorithmique (sur le modèle de Bernardino Romera-Paredes et al. (2024), *Mathematical discoveries from program search with large language models*, référence à vérifier) et les enveloppes numériques de puissance des tests séquentiels (bornes de Ville et de Wald) [VÉRIFIÉ].

---

## 3. Méthodes et outils d'une recherche d'antériorité sans collision : suppositions, défaillances et mesure minimale (Point 3 de l'Arbitre & Livrable III.1.c)

### 3.1. Analyse des instruments : ce que chacun suppose et comment il échoue

| Instrument | Méthode précise | Ce qu'il suppose [HYPOTHÈSE] | Comment il échoue (Modes de défaillance) [HYPOTHÈSE] |
| :--- | :--- | :--- | :--- |
| **1. Agent de lecture et d'empreintage** *(nommé dans la question)* | Extraction des théorèmes depuis les sources `.tex` vers un schéma canonique structuré : $(\text{Espace}, \text{Hypothèses de dépendance}, \text{Stationnarité de } \mathcal{H}_0, \text{Quantificateurs}, \text{Fonctionnelle/Score}, \text{Sens de l'inégalité})$ + traduction des types vers les primitives de la bibliothèque Lean publique [RAPPORTÉ]. | Suppose que deux énoncés mathématiquement équivalents se projettent sur la même représentation canonique, indépendamment du jargon de la sous-communauté d'origine. | **Échec par cryptomorphisme** : une borne d'impossibilité formulée en théorie des jeux d'inspection (équilibre de Stackelberg minimax) est identique à une borne de test de Neyman-Pearson composite, mais le vocabulaire diffère totalement. **Échec sur quantificateurs** : inversion par le modèle de langage entre $\sup_\theta \inf_\tau$ et $\inf_\tau \sup_\theta$. |
| **2. Juge de nouveauté** *(nommé dans les faits [RAPPORTÉ])* | Vérificateur d'implication logique (*entailment/subsumption*) qui teste si un théorème empreinté $A$ (ou la conjonction $A_1 \wedge A_2$ de deux théorèmes connus) implique la cible candidate $B$ modulo des inégalités standards (Jensen, Hölder, Markov, Fano). | Suppose que la réduction d'un théorème publié plus général vers la cible candidate est détectable en un petit nombre d'étapes déductives par un modèle de raisonnement ou un solveur. | **Faux négatif par subsomption cachée** : l'article prouve une borne pour toute $f$-divergence sous filtration générale ; la cible porte sur la divergence de Kullback-Leibler sous dépendance markovienne (corollaire en $3$ lignes (illustratif) non écrit dans l'article). **Fausse alerte par proximité lexicale** : rejette une vraie nouveauté qui améliore un exposant dans Bretagnolle–Huber parce que $95\%$ (illustratif) des termes coïncident. |
| **3. Recherche formelle d'énoncés** *(nommée au point 4 de l'arbitre)* | Requêtes par unification de types (`Loogle`, `exact?`, `apply?`), tactiques de recherche d'arbre (`aesop`) et recherche vectorielle vers le code Lean (`LeanSearch`). | Suppose que la cible et le lemme existant utilisent exactement les mêmes structures de données Lean (ex. même encodage d'une filtration ou d'une e-valeur). | **Cécité à l'isomorphisme de types** : échoue si la bibliothèque existante encode une loi de probabilité via `MeasureTheory.Measure` tandis que la requête utilise une fonction de masse explicite ou un sous-type empaqueté (*bundled vs unbundled*), ou à cause de coercions `Real` / `ENNReal`. |
| **4. Lecteur humain du domaine** *(nommé dans les faits [RAPPORTÉ])* | Audit expert par un chercheur spécialisé confronté au dossier de la cible et aux $k$ plus proches voisins remontés par l'agent. | Suppose que le lecteur humain maîtrise simultanément la littérature récente (jusqu'en 2026 [RAPPORTÉ]) des cinq zones (statistique séquentielle, théorie des jeux, synthèse de programmes). | **Angle mort interdisciplinaire** : un expert des e-valeurs et martingales de test connaît la zone 1 et 2, mais ignore la littérature de recherche opérationnelle sur les jeux d'inspection sous budget (zone 4). **Saturation cognitive** s'il doit lire des dizaines d'articles bruts non filtrés. |

### 3.2. Mesure minimale de fonctionnement de chaque instrument (Livrable III.1.c)

Pour valider qu'un instrument fonctionne avant de lui confier le pilier, on construit un **banc d'étalonnage de $N = 100$ (illustratif) paires de cas honnêtes appariés** ($20$ paires par zone (illustratif)) :
* **Cas positifs (collisions réelles déguisées)** : On prélève $100$ (illustratif) théorèmes ou bornes publiés (dont une moitié issue d'articles récents hors de la bibliothèque Lean actuelle, incluant les travaux de 2026 croisés par hasard [RAPPORTÉ] une fois dépouillés), et on leur applique trois transformations honnêtes préservant le contenu mathématique : (i) *renommage et changement de domaine* (ex. réécrire un processus d'e-valeurs sous forme de jeu de pari séquentiel), (ii) *spécialisation en corollaire* (fixer une distribution ou une classe de dépendance particulière), (iii) *passage au dual ou à la contraposée* (réécrire une borne inférieure de risque minimax de Fano comme une borne inférieure de complexité d'échantillonnage).
* **Cas négatifs appariés (vraies nouveautés proches)** : Pour chaque cas positif, on construit un énoncé jumeau partageant au moins $80\%$ (illustratif) du vocabulaire mathématique, mais où la modification d'une hypothèse structurelle (ex. remplacer l'indépendance sous $\mathcal{H}_0$ par un nul non stationnaire à dérive bornée, ou ajouter une contrainte de budget discret dans le jeu d'inspection) rend la preuve connue caduque et l'énoncé véritablement non résolu dans le corpus.

Chaque instrument doit battre trois **vérifications mécaniques de référence (*baselines*)** :
1. `B_lex` : Recherche lexicale BM25 sur le code LaTeX normalisé (macros dépliées) + filtrage par codes MSC.
2. `B_emb` : Similarité cosinus directe par plongement dense généraliste (ex. `BAAI/bge-m3` [VÉRIFIÉ]) sur le texte brut des théorèmes.
3. `B_lean` : Exécution mécanique de `exact?`, `apply?` et requête par signature de type dans `Loogle` sur la bibliothèque Lean locale [RAPPORTÉ] et `Mathlib4` [VÉRIFIÉ].

**Critères minimaux d'acceptation (tous les seuils sont illustratifs)** :
* **Agent d'empreintage + Juge de nouveauté** : Sur les collisions déguisées par spécialisation/corollaire et changement de notation, doit atteindre un **taux de détection (rappel, TPR) $\ge 0.85$ (illustratif)** pour un **taux de fausses alertes (FPR) sur les négatifs appariés $\le 0.15$ (illustratif)**, et battre `B_lex` + `B_emb` d'au moins $+0.25$ (illustratif) de rappel sur la strate « corollaire par subsomption ».
* **Recherche formelle d'énoncés** : Sur des lemmes déjà présents dans `Mathlib4` ou la bibliothèque Lean locale [RAPPORTÉ] mais reformulés avec des hypothèses réordonnées ou des types isomorphes (`Real` vs `NNReal`), doit atteindre un **TPR $\ge 0.90$ (illustratif)** et un **FPR $\le 0.05$ (illustratif)**, en battant l'appel nu à `exact?` (`B_lean`) d'au moins $+0.30$ (illustratif) de rappel grâce à la normalisation canonique des types.
* **Lecteur humain du domaine (assisté par le dossier d'empreintes)** : Testé en aveugle sur un sous-échantillon de $30$ (illustratif) paires difficiles (celles où `B_emb` échoue), doit atteindre un **TPR $\ge 0.90$ (illustratif)** et un **FPR $\le 0.10$ (illustratif)** en moins de $15$ minutes par cible (illustratif). Si le lecteur humain seul fait moins bien sur une des cinq zones, cela prouve qu'un lecteur unique ne couvre pas l'ensemble du spectre et qu'il faut scinder la relecture entre un profil « statistique séquentielle / information » (zones 1, 2, 3) et un profil « théorie des jeux / synthèse » (zones 4, 5) [HYPOTHÈSE].

---

## 4. Ce qui, hors du programme, vérifierait qu'une cible est neuve (Point 4 de l'Arbitre)

Pour éviter l'enfermement épistémique interne au programme, quatre mécanismes externes fournissent un test de nouveauté indépendant :

1. **Mainteneurs de bibliothèques formelles (communauté Mathlib4 / Lean Zulip)** :
   * *Mécanisme* : Pour tout « lemme de bibliothèque » [RAPPORTÉ] ou théorème généralisable (divergences, martingales, e-valeurs), soumettre la signature Lean 4 (ou une *Pull Request* vers `Mathlib4` / la bibliothèque publique [RAPPORTÉ]) et poster la signature dans les canaux `#mathlib4` ou `#probability` du serveur Zulip de Lean [VÉRIFIÉ].
   * *Ce que cela vérifie* : Les mainteneurs de `Mathlib4` et leurs outils d'audit identifient rapidement si un énoncé existe déjà sous une forme plus abstraite (ex. dans la théorie générale de la mesure ou des filtrations de `Mathlib.Probability.Martingale`) [HYPOTHÈSE].
2. **Recherche formelle d'énoncés et *hammers* externes** :
   * *Mécanisme* : Soumettre l'énoncé formalisé en Lean 4 aux moteurs publics (`Loogle`, `LeanSearch`, `Moogle` [VÉRIFIÉ]) ainsi qu'aux prouveurs automatiques intégrés (`aesop`, `duper` [VÉRIFIÉ]).
   * *Ce que cela vérifie* : Si un outil d'automatisation externe ferme le but en une étape à partir de `Mathlib4`, la cible est un corollaire trivial de l'état de l'art formel et non une « mathématique nouvelle » [HYPOTHÈSE].
3. **Relecteur du domaine externe incité par une « prime à la collision » (*Bounty Red-Teaming*)** :
   * *Mécanisme* : Lorsqu'un relecteur académique est sollicité de façon classique (« cet énoncé vous semble-t-il nouveau ? »), il répond souvent par un accord superficiel faute de temps [HYPOTHÈSE]. Le protocole inverse l'incitation : on soumet l'énoncé mathématique épuré (décontextualisé du contrôle de l'IA pour protéger la confidentialité opérationnelle si nécessaire) à un spécialiste externe avec une **prime forfaitaire versée uniquement s'il exhibe une référence publiée qui prouve ou réfute l'énoncé** en moins de $72$ heures (illustratif).
   * *Ce que cela vérifie* : Mobilise la mémoire active de la communauté de recherche sur les prépublications récentes de 2025–2026 que les moteurs d'indexation n'ont pas encore reliées [HYPOTHÈSE].
4. **Sonde publique décontextualisée (MathOverflow / auteurs des travaux de 2026)** :
   * *Mécanisme* : Pour un « énoncé à démontrer ou réfuter » [RAPPORTÉ] à fort enjeu, poster la question mathématique pure sur MathOverflow [VÉRIFIÉ] ou envoyer un courriel de $5$ lignes (illustratif) aux auteurs des travaux voisins de 2026 croisés par hasard [RAPPORTÉ].
   * *Ce que cela vérifie* : Test de non-collision direct auprès des producteurs mêmes de la frontière de 2026 [HYPOTHÈSE].

---

## 5. Expériences décisives en inférence forte $H_A$ contre $H_B$ (Livrable III.1.b)

Pour trancher empiriquement entre les options (a), (b), (c) et calibrer les outils sans spéculation, voici trois expériences décisives conformes à la règle B4 :

### Expérience 1 — Duel sur le moment de la lecture : Taux de collision à l'aveugle sur le noyau 2026 (Option (a) ciblée contre Option (b))
* **Hypothèse $H_A$ (Vulnérabilité élevée aux collisions 2026)** : Sans lecture préalable au scellement (gel actuel [RAPPORTÉ]), au moins une fraction $\theta \ge 0.20$ (illustratif) des cibles de type « énoncé à démontrer ou réfuter » conçues à partir de la seule bibliothèque Lean actuelle sont déjà résolues (prouvées, réfutées ou impliquées en $\le 5$ lignes (illustratif)) dans les travaux voisins de 2026 croisés par hasard [RAPPORTÉ] et leur voisinage de citations à $1$ saut.
* **Hypothèse $H_B$ (Isolement naturel des cibles de contrôle)** : Les contraintes spécifiques du contrôle défensif des systèmes d'IA [RAPPORTÉ] génèrent des énoncés naturellement disjoints de la littérature statistique publiée ; le taux de collision avant scellement est $\theta < 0.05$ (illustratif), ce qui rend la lecture a priori plus coûteuse que le risque de collision (justifiant l'Option (b)).
* **Protocole et métrique** : Rédiger un lot pilote de $20$ (illustratif) cibles candidates « énoncé à démontrer ou réfuter » ($4$ par zone (illustratif)) en s'appuyant uniquement sur la bibliothèque Lean actuelle [RAPPORTÉ]. Débloquer et lire *uniquement* les travaux voisins de 2026 déjà croisés [RAPPORTÉ] + leur graphe de citations à $1$ saut (soit environ $50$ à $80$ articles (illustratif)). Mesurer la proportion $\hat{\theta}$ de cibles candidates qui entrent en collision directe ou par corollaire immédiat.
* **Seuil de décision** : $\hat{\theta}_{\text{seuil}} = 0.15$ (illustratif) (soit $3$ cibles sur $20$ (illustratif)).
* **Contrôle négatif** : Insérer à l'aveugle dans le lot $5$ (illustratif) théorèmes publiés en 2021–2024 (ex. règles de fusion d'e-valeurs de Vovk et Wang (2021) [VÉRIFIÉ] non encore codées dans la bibliothèque Lean locale) avec notations modifiées. Le protocole d'audit doit détecter $5/5$ (illustratif) de ces contrôles ; s'il en manque un seul, l'instrument de détection est déclaré défaillant et l'expérience invalide.
* **Issues falsificatrices** :
  * Si $\hat{\theta} \ge 0.15$ (illustratif) : **$H_B$ est réfutée** ; l'option (b) (« attendre la première revendication ») est falsifiée pour les énoncés à démontrer ou réfuter, car elle gaspille au moins $15\%$ (illustratif) du budget sur des résultats déjà connus.
  * Si $\hat{\theta} \le 0.05$ (illustratif) (avec contrôle négatif à $5/5$ (illustratif)) : **$H_A$ est réfutée** ; l'option (a) lourde et l'option (c) sont falsifiées comme surcoût inutile au stade du scellement.

### Expérience 2 — Duel sur la méthode d'empreintage : Empreinte textuelle LaTeX contre Empreinte canonisée sur les types Lean
* **Hypothèse $H_A$ (Nécessité de l'ancrage formel Lean)** : Un agent qui empreinte les articles en traduisant leurs théorèmes dans les types et définitions de la bibliothèque Lean publique [RAPPORTÉ] détecte significativement mieux les collisions cryptomorphes (changements de notation entre théorie de l'information, tests séquentiels et jeux d'inspection) qu'un agent utilisant des empreintes structurées en langage naturel/LaTeX.
* **Hypothèse $H_B$ (Suffisance du schéma LaTeX structuré)** : L'extraction d'un schéma JSON en LaTeX normalisé suffit à capturer les collisions ; l'étape d'auto-formalisation vers les types Lean n'apporte aucun gain de rappel et échoue lorsque l'article utilise des concepts absents de la bibliothèque Lean actuelle.
* **Protocole et métrique** : Sur le banc des $100$ (illustratif) paires honnêtes appariées (Section 3.2), mesurer l'écart de taux de détection $\Delta \text{TPR} = \text{TPR}(\text{Lean-Canon}) - \text{TPR}(\text{LaTeX-JSON})$ à taux de fausses alertes fixé $\text{FPR} \le 0.10$ (illustratif), ainsi que le taux d'échec de typage $\tau_{\text{échec}}$ (articles dont l'énoncé ne peut pas être exprimé avec le vocabulaire de la bibliothèque Lean actuelle [RAPPORTÉ]).
* **Seuil de décision** : $\Delta \text{TPR} \ge 0.15$ (illustratif) et $\tau_{\text{échec}} \le 0.25$ (illustratif).
* **Contrôle négatif** : Paires de théorèmes identiques mot pour mot (où les deux méthodes doivent donner $\text{TPR} = 1.00$ (illustratif)) et paires de théorèmes issus de domaines mathématiques sans intersection (ex. cohomologie étale contre tests séquentiels, où $\text{FPR} = 0.00$ (illustratif)).
* **Issues falsificatrices** :
  * Si $\Delta \text{TPR} \ge 0.15$ (illustratif) et $\tau_{\text{échec}} \le 0.25$ (illustratif) : **$H_B$ est réfutée** ; tout empreintage purement textuel est falsifié comme poreux aux collisions inter-zones.
  * Si $\Delta \text{TPR} < 0.05$ (illustratif) ou si $\tau_{\text{échec}} > 0.40$ (illustratif) : **$H_A$ est réfutée** ; la bibliothèque Lean actuelle est trop étroite pour servir de langage pivot d'antériorité sans extension préalable.

### Expérience 3 — Duel sur l'ordre des opérations : Veille bibliographique d'abord contre Filtre numérique de contre-exemple sur petit support d'abord
* **Hypothèse $H_A$ (Efficacité du filtre de réfutation finie)** : Exécuter un script de recherche numérique de contre-exemples sur distributions discrètes à petit support ($|\mathcal{X}| \in \{2, 3, 4\}$, horizon $T \le 5$ (illustratif)) *avant* toute recherche bibliographique permet de réfuter ou d'éliminer au moins $\rho \ge 0.25$ (illustratif) des cibles candidates mal calibrées en moins de $10$ minutes CPU par cible (illustratif).
* **Hypothèse $H_B$ (Cécité des petits supports finis)** : Les phénomènes des cinq zones (frontières asymptotiques de détection, nuls non stationnaires continus) ne se manifestent pas sur de petits espaces discrets ; le filtre numérique élimine moins de $\rho < 0.10$ (illustratif) des cibles candidates.
* **Protocole et métrique** : Soumettre $20$ (illustratif) énoncés candidats (avant lecture d'antériorité) à un solveur d'optimisation numérique / SMT (Python + JAX/SciPy + Z3 [VÉRIFIÉ]) paramétré sur des lois discrètes à support fini pendant $10$ minutes CPU (illustratif) par cible. Mesurer la fraction $\hat{\rho}$ d'énoncés réfutés par un contre-exemple explicite vérifiable.
* **Seuil de décision** : $\hat{\rho} \ge 0.25$ (illustratif).
* **Contrôle négatif** : Soumettre au même script $10$ (illustratif) théorèmes vrais déjà démontrés dans la bibliothèque Lean publique [RAPPORTÉ] (identité de Wald, Fano, Bretagnolle–Huber). Le script doit trouver exactement $0$ contre-exemple ($\hat{\rho}_{\text{contrôle}} = 0.00$ (illustratif)).
* **Issues falsificatrices** :
  * Si $\hat{\rho} \ge 0.25$ (illustratif) (avec $\hat{\rho}_{\text{contrôle}} = 0.00$ (illustratif)) : **$H_B$ est réfutée** ; lancer une lecture d'antériorité (Option (a)) sur un énoncé sans l'avoir d'abord soumis au filtre numérique fini est falsifié comme un gaspillage d'effort.
  * Si $\hat{\rho} < 0.10$ (illustratif) : **$H_A$ est réfutée** ; le pré-filtrage fini est abandonné pour les énoncés théoriques au profit de la vérification bibliographique directe.

---

## 6. Reformulation de la demande (Point 5 de l'Arbitre)

La question initiale demande *quand* et *sur quelle étendue géographique (les cinq zones ou tout le pilier)* un agent doit lire l'antériorité, comme si les trois formes de cibles [RAPPORTÉ] subissaient le même risque de collision au même instant.

**Reformulation proposée** :
> **« Comment allouer l'effort de vérification d'antériorité (dépouillement du noyau 2026 déjà repéré, recherche formelle de types dans Lean, extraction des scores de référence et lecture par requête ciblée) en fonction de la *forme* de chaque cible (objet à score exact, énoncé à démontrer ou réfuter, lemme de bibliothèque) et de son étape dans le cycle de vie (avant scellement dans la liste fermée contre au moment d'une revendication), afin de minimiser la somme du coût de preuve gaspillé sur des résultats connus et du coût de retard des pilotes ? »**

---

## 7. Recommandation, coûts, ancrage matériel et conditions de bascule (Point 6 de l'Arbitre & Livrable III.1.d)

### 7.1. Pourquoi rejeter (a) pur, (b) pur et (c) pur
* **Contre (a) pur** *(tout lire sur 5 zones avant de sceller la moindre cible)* : Retarde le lancement de tous les pilotes [RAPPORTÉ], gaspille des jetons et du temps humain à empreinter des centaines d'articles hors de la liste fermée des cibles, et impose une veille papier inutile aux « lemmes de bibliothèque » et aux « objets à score exact » [HYPOTHÈSE].
* **Contre (b) pur** *(ne rien lire avant la première revendication de nouveauté)* : Dangereux pour les « énoncés à démontrer ou réfuter » en liste fermée [RAPPORTÉ]. Sceller une liste fermée sans même ouvrir les travaux voisins de 2026 déjà croisés par hasard [RAPPORTÉ] expose le programme à payer des agents pour redémontrer des théorèmes de 2026 — ou à tenter de prouver un énoncé que l'article de 2026 a déjà réfuté [HYPOTHÈSE].
* **Contre (c) pur** *(étendre la lecture à tout le pilier)* : Maximise le délai et dilue l'attention du lecteur humain du domaine [RAPPORTÉ] sans réduire le risque spécifique à la liste fermée [HYPOTHÈSE].

### 7.2. Ma recommandation : Option (d) — Protocole stratifié par forme de cible + Dépouillement immédiat du noyau 2026

Je recommande une quatrième option, **l'Option (d) en entonnoir asymétrique**, qui débloque immédiatement deux des trois formes de cibles tout en protégeant la troisième contre toute collision :

1. **Étape 0 (Dès maintenant, avant tout scellement — Délai : $48$ heures (illustratif))** :
   * Lever le gel bibliographique [RAPPORTÉ] *exclusivement* sur un **« noyau chaud »** composé de : (i) les travaux voisins de 2026 croisés par hasard [RAPPORTÉ], et (ii) leur graphe de citations direct à $1$ saut + les articles de 2024–2026 citant les théorèmes fondateurs de la bibliothèque Lean publique [RAPPORTÉ] (soit un corpus borné de $60$ à $100$ articles (illustratif), et non les cinq zones entières).
   * L'agent lit et empreinte ce noyau chaud en projetant les énoncés sur le vocabulaire de la bibliothèque Lean [RAPPORTÉ].
2. **Étape 1 (Avant de sceller une cible dans la liste fermée — Régime selon la forme de la cible)** :
   * **Forme 1 : « Lemme de bibliothèque »** $\rightarrow$ **Régime (b) formel (démarrage immédiat)**. Zéro lecture d'articles. Vérification mécanique en $2$ minutes (illustratif) via `Loogle`, `LeanSearch`, `exact?`, `apply?` et `aesop` sur `Mathlib4` et la bibliothèque Lean publique [RAPPORTÉ]. Si absent du code formel, la cible est scellée immédiatement.
   * **Forme 2 : « Objet à score exact »** $\rightarrow$ **Régime de ligne de base numérique (démarrage en $24$ heures (illustratif))**. Pas d'empreintage de théorèmes. On extrait uniquement du noyau chaud et des notices de bancs **le meilleur score numérique connu** (la constante ou courbe de référence à battre). Dès que ce score de référence est audité par le lecteur humain [RAPPORTÉ], la cible est scellée. La vérification bibliographique fine de la formule gagnante n'a lieu qu'à la revendication (comme en (b)), lorsqu'un agent bat effectivement le score de référence.
   * **Forme 3 : « Énoncé à démontrer ou réfuter »** $\rightarrow$ **Régime (a) ciblé par requête (*Query-Driven Prior Art*)**. Avant de sceller un énoncé candidat $E$ :
     1. Passage par le filtre numérique de contre-exemple sur petit support ($10$ minutes CPU (illustratif), Expérience 3).
     2. Écriture de la signature de $E$ dans les types de la bibliothèque Lean publique [RAPPORTÉ].
     3. Recherche d'antériorité dirigée par la requête $E$ sur les bases ouvertes (arXiv, zbMATH, Semantic Scholar) dans la zone concernée : l'agent récupère, lit et empreinte uniquement le **cône des $15$ à $25$ articles (illustratif) les plus proches de $E$**, puis le juge de nouveauté vérifie l'absence de collision directe ou par subsomption avant scellement.
3. **Étape 2 (À chaque revendication de nouveauté — Régime (b) approfondi)** :
   * Lorsqu'un agent résout une cible scellée, passage devant le juge de nouveauté [RAPPORTÉ], validation par le lecteur humain du domaine [RAPPORTÉ] et vérification externe (mainteneurs Lean pour les lemmes ; sonde externe / prime à la collision de $48$ heures (illustratif) pour les théorèmes majeurs).

### 7.3. Ancrage matériel, modèles ouverts et coûts estimés (Livrable III.1.d)

Tous les composants reposent sur des modèles à poids ouverts et une infrastructure locale vérifiable (tous les chiffres de dimensionnement et de coût ci-dessous sont **illustratifs**, aucun chiffre de coût n'étant fourni dans les faits) :

* **Ingestion et extraction mathématique (`.tex` / PDF)** :
  * Téléchargement prioritaire des sources `.tex` arXiv (traitement CPU, $< 5$ minutes pour $300$ articles (illustratif)). Pour les PDF sans source TeX : modèles ouverts `MinerU` / `Marker` ou `Qwen2.5-VL-7B-Instruct` [VÉRIFIÉ].
* **Recherche hybride et plongements denses** :
  * Index lexical BM25 sur macros LaTeX normalisées + modèle ouvert de plongement `BAAI/bge-m3` [VÉRIFIÉ] ou `Qwen3-Embedding-8B` (poids ouverts). Calcul : $< 1$ heure sur $1 \times$ GPU A100-80GB (illustratif).
* **Agent de lecture, d'empreintage et juge de nouveauté** :
  * Modèles ouverts de raisonnement : `DeepSeek-R1` (671B MoE, poids ouverts [VÉRIFIÉ]) ou `Qwen2.5-72B-Instruct` [VÉRIFIÉ] pour l'extraction du schéma canonique et le test de subsomption logique.
  * Modèles ouverts d'auto-formalisation Lean 4 (traduction des énoncés extraits en signatures de types Lean 4) : `DeepSeek-Prover-V2` ou `Kimina-Prover-Preview-72B` / `Goedel-Prover-SFT` (modèles ouverts spécialisés Lean 4).
* **Vérification mécanique Lean 4 et filtre numérique de contre-exemples** :
  * Serveur CPU $32$ cœurs, $128$ Go RAM (illustratif) exécutant `Lean 4` + `Mathlib4` [VÉRIFIÉ] + la bibliothèque statistique publique [RAPPORTÉ], couplé à `Python` / `JAX` / `Z3` [VÉRIFIÉ] pour la recherche de contre-exemples sur supports finis.

**Comparaison des coûts et délais (tous les chiffres sont illustratifs)** :

| Option | Volume d'articles lus et empreintés avant scellement | Calcul nécessaire (GPU A100-80GB ou équivalent) | Coût inférence estimé (modèles ouverts) | Temps du lecteur humain avant lancement | Retard infligé au démarrage des pilotes | Risque de collision après dépense |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **(a) 5 zones dès maintenant** | $\sim 1\,500\text{ à }2\,500$ articles (illustratif) | $\sim 180\text{ à }300\text{ h.GPU}$ (illustratif) | $\sim 350\text{ \$ à }600\text{ \$}$ (illustratif) | $\sim 35\text{ à }50\text{ h}$ (illustratif) | $2\text{ à }3\text{ semaines}$ (illustratif) | Faible ($\le 5\%$, illustratif) |
| **(b) À la 1re revendication** | $0$ article avant scellement (illustratif) | $0\text{ h.GPU}$ initial (illustratif) | $0\text{ \$}$ initial (illustratif) | $0\text{ h}$ initial (illustratif) | $0\text{ jour}$ (illustratif) | Élevé sur les énoncés ($\ge 20\text{ à }35\%$ du budget de preuve gaspillé, illustratif) |
| **(c) Tout le pilier** | $\ge 5\,000$ articles (illustratif) | $\ge 600\text{ h.GPU}$ (illustratif) | $\ge 1\,200\text{ \$}$ (illustratif) | $\ge 80\text{ h}$ (illustratif) | $\ge 1\text{ mois}$ (illustratif) | Faible, mais bruit et fausses alertes élevés (illustratif) |
| **(d) Recommandée (Noyau 2026 + stratifié par forme)** | $\sim 80$ (noyau 2026) $+ 20$ par énoncé ouvert $\approx \mathbf{200\text{ à }300}$ articles (illustratif) | $\mathbf{\sim 25\text{ à }40\text{ h.GPU}}$ (illustratif) | $\mathbf{\sim 50\text{ \$ à }80\text{ \$}}$ (illustratif) | $\mathbf{\sim 5\text{ à }8\text{ h}}$ (illustratif) | **$0\text{ jour}$** (lemmes/scores) ; **$48\text{ h}$** (énoncés) (illustratif) | Faible ($\le 5\%$, illustratif) |

### 7.4. Ce que ma recommandation suppose et ce qui la ferait changer

**Ce qu'elle suppose** :
1. Que la liste fermée contient effectivement un mélange des trois formes de cibles [RAPPORTÉ] et pas uniquement des conjectures ouvertes [HYPOTHÈSE].
2. Que les travaux voisins de 2026 croisés par hasard [RAPPORTÉ] sont accessibles en texte intégral (arXiv ou PDF) pour l'agent [HYPOTHÈSE].
3. Que le coût d'empreintage d'un cône de $20$ articles (illustratif) autour d'un énoncé candidat est inférieur d'au moins un ordre de grandeur (illustratif) au budget de calcul alloué aux agents pour démontrer ou réfuter cet énoncé [HYPOTHÈSE] (je ne sais pas quel est le budget de calcul exact par cible dans le programme).

**Ce qui me ferait changer de recommandation (conditions de bascule falsifiables)** :
1. **Bascule de (d) vers (b) pur** : Si l'Expérience 1 montre un taux de collision $\hat{\theta} \le 0.05$ (illustratif) sur le noyau 2026 *et* que le coût de tentative de preuve d'une cible par les agents est faible ($C_{\text{preuve}} \le 2 \times C_{\text{veille par cible}}$ (illustratif)). Dans ce cas, il est plus économique de laisser les agents chercher sans veille préalable et de ne vérifier l'antériorité que sur les cibles effectivement résolues.
2. **Bascule de (d) vers (a) intégral** : Si l'Expérience 1 révèle un taux de collision $\hat{\theta} \ge 0.40$ (illustratif) *et* que plus de la moitié (illustratif) des collisions détectées lors de l'étalonnage proviennent d'articles situés à $\ge 2$ sauts de citations du noyau 2026 et échappent à la recherche par requête ciblée (par exemple parce que toute une zone, comme les jeux d'inspection sous budget, a déjà été résolue sous un autre nom en recherche opérationnelle). Alors le scellement doit être gelé jusqu'à l'empreintage complet des cinq zones.
3. **Abandon de l'ancrage Lean dans l'empreintage** : Si l'Expérience 2 montre que plus de $40\%$ (illustratif) des théorèmes de 2026 des cinq zones ne peuvent pas être typés dans le vocabulaire de la bibliothèque Lean actuelle ($\tau_{\text{échec}} > 0.40$ (illustratif)), j'abandonne le typage Lean préalable au profit du schéma LaTeX structuré couplé au filtre numérique de l'Expérience 3.

FIN-DE-CELLULE