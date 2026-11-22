# Exploration, découverte et émergence des idées nouvelles

## Préambule méthodologique

Ce texte répond à six questions sur la recherche d'objets rares et précieux dans un grand espace de possibilités. Je sépare systématiquement : (a) ce que je **sais** (résultats que j'ai vus dans des sources primaires et dont je suis raisonnablement certain), (b) ce que je **suppose** (inférences raisonnables mais non directement vérifiées), et (c) ce que je **cite de mémoire** (références dont je suis assez sûr mais que je n'ai pas sous les yeux — les détails bibliographiques pourraient être légèrement inexacts). Les chiffres sont toujours attribués à une source.

---

## 1. Procédés guidés contre procédés non guidés

### 1.1 Cadre

Les procédés **guidés** (recherche évolutionnaire, recherche arborescente Monte-Carlo — MCTS —, bandits multi-bras, optimisation bayésienne) exploitent l'information accumulée pour orienter la suite de la recherche. Les procédés **non guidés** (tirages i.i.d., marche aléatoire, reprises à zéro — *random restarts*) ne le font pas, ou très peu.

### 1.2 Résultats théoriques

**Théorèmes « No Free Lunch » (NFL).** Wolpert et Macready (1997, « No Free Lunch Theorems for Optimization », *IEEE Transactions on Evolutionary Computation*, 1(1), 67–82) montrent que, moyennés sur *toutes* les fonctions possibles, tous les algorithmes d'optimisation à boîte noire ont la même performance. **Ce que cela implique** : la supériorité des méthodes guidées repose entièrement sur des hypothèses de structure de l'espace (corrélation spatiale, régularité, décomposabilité). **Ce que cela n'implique pas** : que sur un problème réel donné, guidé et non guidé se valent.

**Bandits multi-bras.** Le regret cumulé d'UCB (Auer, Cesa-Bianchi et Fischer, 2002, « Finite-time Analysis of the Multiarmed Bandit Problem », *Machine Learning*, 47(2–3), 235–256) est en O(ln n) pour n tirages, contre Ω(n) pour l'exploration uniforme — un avantage exponentiel en termes de regret. Cela suppose des récompenses bornées et un nombre fini de bras.

**Optimisation bayésienne.** Bull (2011, « Convergence Rates of Efficient Global Optimization Algorithms », *Journal of Machine Learning Research*, 12, 2879–2904) démontre que l'algorithme EGO (Expected Improvement sur processus gaussien) converge à taux optimal au sens minimax sur les fonctions dans un espace de Hilbert à noyau reproduisant (RKHS) — ce que je cite de mémoire. La supériorité sur le tirage aléatoire est d'autant plus marquée que la dimension est faible et la fonction régulière.

**MCTS.** Kocsis et Szepesvári (2006, « Bandit Based Monte-Carlo Planning », *ECML 2006*) montrent que UCT (Upper Confidence bounds for Trees) converge vers le minimax. Silver et al. (2016, « Mastering the game of Go with deep neural networks and tree search », *Nature*, 529, 484–489) fournissent la démonstration empirique la plus spectaculaire : AlphaGo bat le champion du monde de go, ce qui aurait été hors de portée d'une recherche non guidée dans l'arbre de jeu (espace de ~10^170 positions possibles, chiffre de mémoire).

**Algorithmes évolutionnaires.** Droste, Jansen et Wegener (2002, « On the Analysis of the (1+1) Evolutionary Algorithm », *Theoretical Computer Science*, 276(1–2), 51–81) analysent le temps d'optimisation du (1+1)-EA sur des fonctions de test classiques. Sur OneMax (fonction linéaire), le temps attendu est Θ(n ln n), identique à l'algorithme glouton optimal. Sur des fonctions à tromperie (*deceptive*), la recherche guidée peut être piégée : le paysage de fitness guide vers un optimum local. Je cite de mémoire.

### 1.3 Quand le non guidé fait mieux

1. **Espaces sans corrélation spatiale (paysage « aiguille dans une botte de foin »).** Si la valeur d'un point ne donne aucune information sur les points voisins, aucun guidage ne peut surpasser le tirage uniforme. C'est la conséquence directe de NFL.

2. **Fonctions fortement multimodales avec bassins étroits.** Les reprises à zéro (*random restarts*) battent régulièrement les méthodes locales pures. Je suppose que c'est mesuré dans la communauté d'optimisation continue (voir les benchmarks BBOB/COCO, Hansen et al., 2021, « COCO: A Platform for Comparing Continuous Optimizers in a Black-Box Setting », *Optimization Methods and Software*, 36(1), 114–144), mais je n'ai pas de chiffre comparatif précis sous les yeux.

3. **Découverte de nouveauté pure.** Lehman et Stanley (2011, « Abandoning Objectives: Evolution Through the Search for Novelty Alone », *Evolutionary Computation*, 19(2), 189–223) montrent que la recherche de *nouveauté* (sans fonction objectif) surpasse la recherche guidée par fitness dans des labyrinthes trompeurs. L'explication : le guidage par objectif converge vers un optimum local, tandis que l'exploration sans objectif couvre mieux l'espace.

4. **Exploration chimique / découverte de matériaux.** Les campagnes de criblage à haut débit (*high-throughput screening* — HTS) reposent sur un tirage quasi aléatoire d'une bibliothèque de composés. Walters, Stahl et Murcko (1998, « Virtual screening — an overview », *Drug Discovery Today*, 3(4), 160–178) rapportent que le HTS restait compétitif face aux méthodes de *docking* guidé de l'époque, mais les résultats récents en optimisation bayésienne appliquée à la chimie (Shields et al., 2021, « Bayesian reaction optimization as a tool for chemical synthesis », *Nature*, 590, 89–96) montrent une supériorité mesurée du guidé : typiquement 3 à 5 fois moins d'expériences pour trouver des conditions optimales, d'après leur article. Je cite de mémoire pour les chiffres exacts.

### 1.4 Quand le guidé fait mieux — mesures publiées

- **AlphaFold** (Jumper et al., 2021, « Highly accurate protein structure prediction with AlphaFold », *Nature*, 596, 583–589). Recherche guidée par réseau de neurones. GDT (Global Distance Test) médian > 92 sur CASP14, contre ~60 pour les meilleures méthodes ab initio antérieures — ce que je cite de mémoire pour le chiffre comparatif.

- **Synthèse de programmes (program synthesis).** Gulwani (2011, « Automating string processing in spreadsheets using input-output examples », *POPL 2011*) : FlashFill trouve le programme correct en quelques secondes par recherche guidée dans un espace de ~10^20 programmes possibles (chiffre de mémoire). Un tirage uniforme dans cet espace serait sans espoir.

- **Optimisation de réactions chimiques.** Shields et al. (2021, op. cit.) : l'optimisation bayésienne trouve les meilleures conditions en ~20 expériences contre ~100 pour un *design of experiments* factoriel (non guidé). Chiffres de mémoire.

- **Résultat contraire notable.** Recht et al. (2019, « A Tour of Reinforcement Learning: The View from Continuous Control », *Annual Review of Control, Robotics, and Autonomous Systems*, 2, 253–279) et Mania, Guy et Recht (2018, « Simple random search provides a competitive approach to reinforcement learning », *NeurIPS 2018*) montrent que la recherche aléatoire (*Augmented Random Search*) rivalise avec les méthodes d'apprentissage par renforcement guidées (PPO, TRPO) sur des problèmes de contrôle MuJoCo. L'explication proposée : dans des espaces de dimension modérée avec des gradients bruités, le guidage n'apporte pas autant qu'attendu.

### 1.5 Synthèse

**Je sais** : le guidage est d'autant plus avantageux que l'espace est structuré (corrélation spatiale, régularité, décomposabilité) et de haute dimension. Le non guidé est compétitif quand l'espace est peu structuré, quand l'objectif est trompeur, ou quand l'espace est de dimension suffisamment basse pour qu'un échantillonnage dense soit abordable. **Je suppose** : pour la découverte scientifique, l'espace des idées possibles est très structuré mais la structure est mal connue, ce qui place la situation entre les deux régimes.

---

## 2. Modèles mathématiques de l'apparition des idées nouvelles

### 2.1 Modèles d'urnes : l'adjacent possible

**Urne de Pólya généralisée et adjacent possible.** Tria, Loreto, Servedio et Strogatz (2014, « The dynamics of correlated novelties », *Scientific Reports*, 4, 5890) proposent un modèle d'urne où chaque tirage d'une couleur nouvelle ajoute de nouvelles couleurs possibles (l'« adjacent possible » au sens de Kauffman). Le modèle reproduit la loi de Heaps (croissance sous-linéaire du vocabulaire avec le corpus), la loi de Zipf, et la statistique des premières occurrences. **Confrontation aux données** : les auteurs comparent leur modèle à des données de Wikipedia, Last.fm, Gutenberg et brevets — l'accord est raisonnable sur les lois de puissance observées. Je cite de mémoire pour les détails statistiques.

**Loi de Heaps.** Heaps (1978, *Information Retrieval*) : le nombre de mots distincts V(n) dans un texte de n mots croît comme V(n) ~ n^β avec β ∈ (0,4 ; 0,6) pour l'anglais. C'est un résultat empirique robuste, vérifié sur de nombreux corpus (chiffre de mémoire pour l'intervalle de β).

### 2.2 Paysages de fitness et transitions de phase

**Modèle NK de Kauffman.** Kauffman (1993, *The Origins of Order*, Oxford University Press). Un paysage de fitness sur {0,1}^N avec K interactions par locus. Pour K = 0, le paysage est lisse (un seul pic) ; pour K = N-1, il est aléatoire. La transition de « cherchable » à « incherchable » se produit pour K de l'ordre de quelques unités (je suppose, sur la base du comportement connu). Ce modèle n'a pas été directement confronté à des données de découverte scientifique, **à ma connaissance**. Il a été confronté à des données d'évolution moléculaire (Weinreich et al., 2006, « Darwinian Evolution Can Follow Only Very Few Mutational Paths to Fitter Proteins », *Science*, 312, 111–114 : sur 5 mutations de la β-lactamase, seules 18 des 120 chemins possibles sont monotones en fitness, ce qui est compatible avec un K modéré).

**Transitions de phase en satisfiabilité (SAT).** Cheeseman, Kanefsky et Taylor (1991, « Where the Really Hard Problems Are », *IJCAI 1991*). Pour le SAT aléatoire à k littéraux (k-SAT), il existe un ratio critique clauses/variables α_c au-delà duquel le problème passe de satisfiable à insatisfiable. Pour 3-SAT, α_c ≈ 4,267 (Mézard, Parisi et Zecchina, 2002, « Analytic and Algorithmic Solution of Random Satisfiability Problems », *Science*, 297, 812–815 — résultat rigoureux par la suite confirmé à ce seuil, je cite de mémoire). Les instances les plus dures pour la recherche se situent près de la transition. **Analogie supposée** : la difficulté de la découverte serait maximale dans une zone critique de densité de contraintes.

### 2.3 Modèles économiques de la recherche

**Modèle de Weitzman (1979, « Optimal Search for the Best Alternative », *Econometrica*, 47(3), 641–654).** Résultat central : la règle de recherche optimale (séquentielle, avec coûts de vérification et distributions connues) est un index de réservation — on fouille par ordre décroissant de cet index, et on s'arrête quand la meilleure trouvaille dépasse l'index du prochain candidat. **Confrontation aux données** : peu de tests empiriques directs à ma connaissance (le modèle est surtout normatif). Caplin, Dean et Martin (2011, « Search and Satisficing », *American Economic Review*, 101(7), 2899–2922) montrent que les sujets humains dévient systématiquement de l'optimum de Weitzman (arrêt trop précoce).

**Modèle de Jones (1995, « R&D-Based Models of Economic Growth », *Journal of Political Economy*, 103(4), 759–784).** L'hypothèse du « fishing out » : les idées les plus faciles sont trouvées en premier, et la productivité marginale de la recherche décline. Jones montre empiriquement que le nombre de chercheurs aux États-Unis a été multiplié par ~5 entre 1950 et 1990 (chiffre de mémoire) tandis que la croissance de la productivité totale des facteurs n'a pas augmenté. Bloom, Jones, Van Reenen et Webb (2020, « Are Ideas Getting Harder to Find? », *American Economic Review*, 110(4), 1104–1144) confirment : la productivité de la recherche (mesurée comme croissance TFP par chercheur) décline d'environ 4 % par an aux États-Unis sur la période 1930–2000.

### 2.4 Processus de branchement

**Modèle de Galton-Watson appliqué à la recherche.** Une idée en engendre d'autres avec une certaine probabilité. Si la moyenne de descendance m > 1, le processus survit avec probabilité positive ; si m ≤ 1, il s'éteint presque sûrement. **Je suppose** que cela modélise la « fécondité » d'un programme de recherche. Je ne connais pas de confrontation directe à des données de découverte scientifique. En revanche, les cascades de citations ont été analysées par ce prisme : Golosovsky et Solomon (2017, « Growing complex network of citations of scientific papers: Modeling and measurements », *Physical Review E*, 95, 012324) modélisent les citations comme un processus de Hawkes (apparenté au branchement) et obtiennent un bon accord avec les données Web of Science. Je cite de mémoire.

### 2.5 Réseaux

**Uzzi, Mukherjee, Stringer et Jones (2013, « Atypical Combinations and Scientific Impact in Science », *Science*, 342, 468–472).** Les articles de *Science* et *Nature* les plus cités combinent des paires de journaux cités qui sont « atypiques » (rarement co-citées) avec une majorité de paires conventionnelles. Les auteurs analysent 17,9 millions d'articles (1945–2005) du Web of Science. **C'est une mesure.** Résultat : les articles dans le top 5 % des citations sont 2 fois plus susceptibles de contenir des combinaisons atypiques (je cite de mémoire pour le facteur exact). **Résultat contraire** : Lee, Walsh et Wang (2015, « Creativity in scientific teams: Unpacking novelty and impact », *Research Policy*, 44(3), 684–697) nuancent : la nouveauté combinatoire augmente l'impact moyen mais aussi la variance — les articles très nouveaux ont plus de chances d'être soit un succès, soit un échec.

---

## 3. Autres savoirs sur les conditions de la découverte

### 3.1 Philosophie des sciences

**Kuhn (1962, *The Structure of Scientific Revolutions*, University of Chicago Press).** Les découvertes naissent typiquement dans les périodes de « crise » d'un paradigme, quand les anomalies s'accumulent. **C'est un cadre interprétatif, pas une mesure.** Kuhn s'appuie sur des études de cas (la révolution copernicienne, la chimie de Lavoisier, la relativité).

**Popper (1959, *The Logic of Scientific Discovery*, Hutchinson).** L'accent est sur la réfutabilité, pas sur l'origine des conjectures. Popper reconnaît explicitement que le « contexte de découverte » échappe à la logique.

**Lakatos (1978, *The Methodology of Scientific Research Programmes*, Cambridge University Press).** Les programmes de recherche « progressifs » (qui prédisent des faits nouveaux) survivent ; les « dégénératifs » (qui ne font que des accommodations post hoc) finissent par être abandonnés. **Cadre interprétatif**, illustré par l'histoire de la physique.

### 3.2 Ce qui est mesuré

**Incubation en psychologie.** Sio et Ormerod (2009, « Does Incubation Enhance Problem Solving? A Meta-Analytic Review », *Psychological Bulletin*, 135(1), 94–120). Méta-analyse de 117 études. L'incubation (pause dans la résolution) a un effet positif petit mais significatif (d de Cohen ≈ 0,3, je cite de mémoire). L'effet est plus fort pour les problèmes divergents que convergents.

**Sérendipité mesurée.** Yaqub (2018, « Serendipity: Towards a Taxonomy and a Theory », *Research Policy*, 47(1), 169–179) propose une taxonomie de la sérendipité. Mais les *mesures* directes de la fréquence de la sérendipité sont rares. Campanario (1996, « Using Citation Classics to study the incidence of serendipity in scientific discovery », *Scientometrics*, 37(1), 3–24) analyse les « Citation Classics » de Current Contents et trouve qu'environ 30–50 % des auteurs mentionnent un élément inattendu dans leur récit de découverte (chiffre de mémoire). **Ce qui est raconté, pas mesuré** : le biais de rappel et de narration rend ce chiffre peu fiable.

**Diversité des équipes.** Shi et Evans (2023, « Surprising combinations of research contents and contexts are related to impact and emerging topics in science », *Nature Human Behaviour*, 7, 1024–1039 — je cite de mémoire pour l'année et le titre exact). Les équipes qui combinent des chercheurs issus de disciplines éloignées produisent des articles plus novateurs mais aussi plus risqués.

### 3.3 Ce qui est raconté (témoignages, non mesuré)

**Poincaré (1908, *Science et Méthode*).** Décrit l'illumination comme survenant après une période de travail intense suivie de repos. Le célèbre épisode du marchepied de l'omnibus et des fonctions fuchsiennes. **Témoignage, non mesure.**

**Hadamard (1945, *The Psychology of Invention in the Mathematical Field*, Princeton University Press).** Enquête auprès de mathématiciens sur leur processus créatif. Modèle en quatre phases : préparation, incubation, illumination, vérification (emprunté à Wallas, 1926). **Recueil de témoignages, biais de sélection évident.**

**Kekulé (1890).** Raconte avoir rêvé de la structure en anneau du benzène — un serpent se mordant la queue. **Témoignage tardif et contesté.** Wotiz (1993, *The Kekulé Riddle*, Cache River Press) met en doute son authenticité.

**McClintock (sur les transposons).** Décrit des années d'isolement intellectuel avant la reconnaissance. **Témoignage de découvreur**, corroboré par l'historique des publications et du prix Nobel (1983).

### 3.4 Neurosciences

**Beeman et al. (2004, « Neural Activity When People Solve Verbal Problems with Insight », *PLoS Biology*, 2(4), e97).** Une bouffée d'activité gamma dans le gyrus temporal supérieur droit précède la résolution « insight » de problèmes de mots composés (Compound Remote Associates). **Mesure (EEG/fMRI, N = 44 — de mémoire).** Mais le lien entre ce phénomène de laboratoire et la découverte scientifique réelle est **supposé**, pas démontré.

### 3.5 Physique statistique

**Analogie avec les transitions de phase.** Certains auteurs (par exemple Solé et al., 2013, « The evolutionary ecology of technological innovations », *Complexity*, 18(4), 15–27 — je cite de mémoire) proposent que l'innovation se comporte comme un phénomène critique. **L'analogie est suggestive mais les preuves quantitatives d'une véritable transition de phase dans la découverte scientifique sont faibles**, à ma connaissance.

### 3.6 Biologie évolutive

**Exaptation (Gould et Vrba, 1982, « Exaptation — A Missing Term in the Science of Form », *Paleobiology*, 8(1), 4–15).** Un trait évolué pour une fonction est « coopté » pour une autre. L'analogie avec la découverte scientifique (un résultat développé dans un contexte est appliqué dans un autre) est **supposée** mais non mesurée.

---

## 4. Deux situations

### 4.1 (a) Domaines séparés dont le rapprochement ferait naître une idée

**Ce qui augmente la probabilité :**

- **Mobilité des chercheurs entre disciplines.** Mesuré : Uzzi et al. (2013, op. cit.) montrent que les combinaisons atypiques de références augmentent l'impact. Fleming (2001, « Recombinant Uncertainty in Technological Search », *Management Science*, 47(1), 117–132) montre que les inventeurs qui combinent des sous-classes de brevets éloignées produisent des brevets d'impact moyen plus élevé mais de variance plus grande.

- **Structures institutionnelles favorisant les interactions.** L'exemple du MIT Media Lab ou des Bell Labs est souvent cité — **témoignage et narration historique**, pas mesure contrôlée. Gertner (2012, *The Idea Factory: Bell Labs and the Great Age of American Innovation*, Penguin). Cependant, les études contrôlées sont rares.

- **Outils et langages communs.** L'adoption des mathématiques dans la biologie (Fisher, 1930 ; Wright, 1931) a permis la synthèse évolutive. L'adoption de l'apprentissage profond dans de nombreuses disciplines (physique, biologie, chimie) depuis ~2015 crée un langage commun. **Observation historique, pas mesure.**

**Ce qui diminue la probabilité :**

- **Spécialisation croissante.** Jones (2009, « The Burden of Knowledge and the 'Death of the Renaissance Man': Is Innovation Getting Harder? », *Review of Economic Studies*, 76(1), 283–317). L'âge moyen de la première contribution des inventeurs augmente au cours du XXe siècle (mesure sur données de brevets et de prix Nobel). La spécialisation rend les ponts entre domaines plus coûteux en temps de formation.

- **Silos institutionnels et disciplinaires.** Les systèmes de financement et de publication favorisent les contributions dans un domaine établi. **Je suppose** que cela décourage les travaux transdisciplinaires, mais les mesures directes de cet effet sont rares.

- **Incompréhension mutuelle des vocabulaires.** Deux domaines peuvent étudier le même phénomène sous des noms différents sans le savoir. **Observation courante mais non mesurée systématiquement.**

### 4.2 (b) Idées non encore émises qui découlent de résultats publiés

**Ce qui augmente la probabilité :**

- **Accessibilité de la littérature.** L'accès ouvert (*open access*) augmente les citations (mesure : Piwowar et al., 2018, « The state of OA: a large-scale analysis of the prevalence and impact of Open Access articles », *PeerJ*, 6, e4375 — les articles en accès ouvert reçoivent environ 18 % de citations de plus, je cite de mémoire pour le chiffre).

- **Outils de recherche sémantique.** Les outils comme Semantic Scholar (Allen Institute for AI, lancé 2015) et Elicit facilitent la découverte de liens entre articles. **Je suppose** que cela augmente la probabilité de dériver une idée nouvelle de la littérature existante, mais je ne connais pas de mesure directe de cet effet sur la découverte.

- **Prépublications (preprints).** L'accélération de la circulation des idées par arXiv (depuis 1991) et bioRxiv (depuis 2013). Effet mesuré sur la vitesse de citation, pas directement sur la découverte.

**Ce qui diminue la probabilité :**

- **Surcharge informationnelle.** Le nombre d'articles publiés croît exponentiellement (Bornmann et Mutz, 2015, « Growth rates of modern science: A bibliometric analysis based on the number of publications and cited references », *Journal of the Association for Information Science and Technology*, 66(11), 2215–2222 : croissance d'environ 4 % par an, doublement tous les 17–18 ans). La probabilité qu'un article pertinent soit lu décroît.

- **Biais de publication.** Les résultats négatifs et les réplications sont sous-publiés, ce qui cache des informations nécessaires pour compléter un raisonnement.

- **Effet Ortega (ou sa contestation).** L'hypothèse Ortega (Ortega y Gasset, 1930, *La rebelión de las masas*) suggère que la masse des chercheurs ordinaires contribue essentiellement au bruit. Cole et Cole (1972, « The Ortega Hypothesis », *Science*, 178, 368–375) montrent que la majorité des citations vont à un petit nombre d'articles. **Résultat contraire** : Bornmann, Mutz et Daniel (2010, « The h index research output measurement: Two approaches to enhance its accuracy », *Journal of Informetrics*, 4(3), 407–414 — je cite de mémoire et le titre peut ne pas être le bon pour ce résultat spécifique) : certaines études contestent cette concentration extrême, montrant que les articles moyennement cités contribuent de manière significative au progrès incrémental.

---

## 5. Estimer ce qui reste à découvrir et décider de la suite

### 5.1 Estimateurs de richesse non observée

**Capture-recapture.** Le problème est analogue à l'estimation du nombre d'espèces dans un écosystème. L'estimateur de Chao (Chao, 1984, « Nonparametric Estimation of the Number of Classes in a Population », *Scandinavian Journal of Statistics*, 11(4), 265–270) donne une borne inférieure du nombre d'espèces non observées à partir du nombre d'espèces observées une seule fois (singletons) et deux fois (doubletons) :

N̂ ≥ N_obs + f₁² / (2 f₂)

où f₁ est le nombre de singletons et f₂ le nombre de doubletons. **Hypothèse** : les objets sont tirés indépendamment d'une population finie selon des probabilités inégales. **Limite** : l'estimateur est une borne inférieure et peut être très conservateur si de nombreuses « espèces » ont une probabilité extrêmement faible.

**Good-Turing.** Good (1953, « The Population Frequencies of Species and the Estimation of Population Parameters », *Biometrika*, 40(3–4), 237–264) estime la probabilité totale de toutes les espèces non encore observées comme ≈ f₁ / n, où f₁ est le nombre de singletons et n le nombre total de tirages. **Ce résultat est élégant et bien fondé**, sous l'hypothèse de tirages i.i.d.

**Application à la découverte scientifique.** Clauset, Larremore et Sinatra (2017, « Data-driven predictions in the science of science », *Science*, 355, 477–480) — je cite de mémoire — discutent la prédictibilité des carrières scientifiques et de l'impact, mais pas directement l'estimation du nombre de découvertes restantes. **Je ne connais pas d'application directe de Chao ou Good-Turing à l'estimation du nombre de théorèmes ou d'idées scientifiques restantes.** Je suppose que l'obstacle principal est que l'espace des idées n'est pas une population finie au sens classique — il croît par « adjacent possible ».

### 5.2 Courbes de découverte

**Loi de rendements décroissants.** Bloom et al. (2020, op. cit.) : la productivité de la recherche décline. Si l'on suppose un « stock d'idées » fini (ou croissant mais plus lentement que l'effort), on peut estimer la fraction restante par extrapolation de la courbe de rendement. **Très sensible aux hypothèses** : un modèle à stock fini prédit l'épuisement ; un modèle à stock croissant (adjacent possible) ne le fait pas.

### 5.3 Critères d'arrêt

**Règle d'arrêt optimale de Weitzman** (1979, op. cit.) : s'arrêter quand la valeur marginale espérée du prochain tirage tombe en dessous du coût. Nécessite de connaître la distribution des valeurs et le coût.

**Regret budgété.** Dans le cadre des bandits, on peut définir un regret cumulé maximal acceptable et arrêter quand il est atteint. Bubeck et Cesa-Bianchi (2012, « Regret Analysis of Stochastic and Nonstochastic Multi-Armed Bandit Problems », *Foundations and Trends in Machine Learning*, 5(1), 1–122) donnent un traitement complet.

**Critère d'information bayésien pour l'arrêt.** Dans le cadre de l'optimisation bayésienne, on peut définir un seuil de probabilité d'amélioration (EI < ε) pour arrêter. **Hypothèse** : le modèle de substitution (processus gaussien) est bien calibré. **Limite** : si le modèle est mal spécifié, l'arrêt peut être prématuré.

### 5.4 Limites fondamentales

**Le problème de l'induction.** On ne peut jamais être certain qu'il ne reste rien à découvrir. L'estimateur de Chao donne une borne inférieure, pas une borne supérieure. L'analogie avec le problème du cygne noir (Taleb, 2007, *The Black Swan*, Random House) est pertinente : les découvertes les plus importantes sont précisément celles qu'on ne peut pas anticiper.

**Incomplétude de Gödel (1931).** Dans tout système formel assez puissant, il existe des énoncés vrais mais indémontrables. Cela pose une limite théorique à l'exploration par déduction dans les mathématiques. **Ce que cela implique pour la recherche d'idées nouvelles** : certaines idées mathématiques ne peuvent pas être atteintes par la dérivation systématique à partir des axiomes connus. **Je suppose** que cette limite est rarement atteinte en pratique dans les sciences empiriques.

---

## 6. Qu'est-ce qui me donnerait tort ?

Pour chaque section, je propose une observation falsificatrice et son coût estimé.

### 6.1 Section 1 (guidé vs non guidé)

**Ce qui me donnerait tort** : une expérience montrant que sur un espace structuré et de haute dimension (par exemple la conception de protéines), le tirage uniforme fait aussi bien que l'optimisation bayésienne à budget égal.

**Coût minimal** : un benchmark computationnel sur un problème standard (ex. : optimisation de protéines in silico), reproductible en quelques jours de calcul sur un cluster modeste. Coût estimé : quelques milliers de dollars de calcul.

### 6.2 Section 2 (modèles mathématiques)

**Ce qui me donnerait tort** : des données de découverte scientifique réelle montrant que la loi de Heaps *ne s'applique pas* à l'apparition de nouveaux concepts (par exemple, si le nombre de concepts nouveaux par an accélérait au lieu de ralentir).

**Coût minimal** : une analyse bibliométrique sur un corpus existant (ex. : MeSH terms dans PubMed). Faisable par un doctorant en quelques semaines.

### 6.3 Section 3 (autres savoirs)

**Ce qui me donnerait tort sur l'incubation** : une méta-analyse actualisée montrant que l'effet d'incubation est un artefact méthodologique (par exemple, biais de publication).

**Coût minimal** : une analyse de la littérature existante avec correction pour le biais de publication (*p-curve* ou *z-curve*). Réalisable sans nouvelle collecte de données.

### 6.4 Section 4a (domaines séparés)

**Ce qui me donnerait tort** : une étude contrôlée montrant que la mobilité interdisciplinaire des chercheurs *diminue* la probabilité de découvertes de haut impact (par exemple, parce que l'expertise superficielle dans deux domaines est moins productive que l'expertise profonde dans un seul).

**Coût minimal** : une analyse causale (différence-en-différences ou variable instrumentale) sur des données de carrières de chercheurs. Données disponibles via OpenAlex ou Web of Science. Faisable en quelques mois.

### 6.5 Section 4b (idées non encore émises)

**Ce qui me donnerait tort** : une démonstration que l'accès ouvert n'augmente *pas* les découvertes dérivées (par exemple, en montrant que les articles en accès ouvert ne sont pas plus souvent les prémisses d'articles ultérieurs que les articles fermés).

**Coût minimal** : une analyse de chaînes de citations sur un corpus existant. Faisable avec les données de Semantic Scholar (accès API gratuit).

### 6.6 Section 5 (estimer ce qui reste)

**Ce qui me donnerait tort** : une application directe de l'estimateur de Chao à un domaine scientifique bien délimité (par exemple les espèces chimiques naturelles, les particules élémentaires, les protéines humaines) donnant une estimation précise et vérifiable du nombre d'objets restants, contredisant l'idée que l'espace des idées échappe à cette estimation.

**Coût minimal** : l'appliquer aux nouvelles espèces chimiques découvertes par an (données disponibles dans CAS Registry). Faisable en quelques jours.

**L'observation la moins coûteuse de toutes** : pour la section 6.2, l'analyse bibliométrique des MeSH terms dans PubMed. Les données sont publiques, les outils existent, et un analyste compétent pourrait obtenir un résultat en une semaine.

---

## Références consolidées

(Par ordre d'apparition, avec les informations que j'ai ou que je reconstitue de mémoire.)

1. Wolpert, D. H. et Macready, W. G. (1997). « No Free Lunch Theorems for Optimization ». *IEEE Transactions on Evolutionary Computation*, 1(1), 67–82.
2. Auer, P., Cesa-Bianchi, N. et Fischer, P. (2002). « Finite-time Analysis of the Multiarmed Bandit Problem ». *Machine Learning*, 47(2–3), 235–256.
3. Bull, A. D. (2011). « Convergence Rates of Efficient Global Optimization Algorithms ». *JMLR*, 12, 2879–2904. [De mémoire.]
4. Kocsis, L. et Szepesvári, C. (2006). « Bandit Based Monte-Carlo Planning ». *ECML 2006*.
5. Silver, D. et al. (2016). « Mastering the game of Go with deep neural networks and tree search ». *Nature*, 529, 484–489.
6. Droste, S., Jansen, T. et Wegener, I. (2002). « On the Analysis of the (1+1) Evolutionary Algorithm ». *Theoretical Computer Science*, 276(1–2), 51–81. [De mémoire.]
7. Hansen, N. et al. (2021). « COCO: A Platform for Comparing Continuous Optimizers in a Black-Box Setting ». *Optimization Methods and Software*, 36(1), 114–144.
8. Lehman, J. et Stanley, K. O. (2011). « Abandoning Objectives: Evolution Through the Search for Novelty Alone ». *Evolutionary Computation*, 19(2), 189–223.
9. Walters, W. P., Stahl, M. T. et Murcko, M. A. (1998). « Virtual screening — an overview ». *Drug Discovery Today*, 3(4), 160–178.
10. Shields, B. J. et al. (2021). « Bayesian reaction optimization as a tool for chemical synthesis ». *Nature*, 590, 89–96.
11. Jumper, J. et al. (2021). « Highly accurate protein structure prediction with AlphaFold ». *Nature*, 596, 583–589.
12. Gulwani, S. (2011). « Automating string processing in spreadsheets using input-output examples ». *POPL 2011*.
13. Mania, H., Guy, A. et Recht, B. (2018). « Simple random search provides a competitive approach to reinforcement learning ». *NeurIPS 2018*.
14. Tria, F., Loreto, V., Servedio, V. D. P. et Strogatz, S. H. (2014). « The dynamics of correlated novelties ». *Scientific Reports*, 4, 5890.
15. Heaps, H. S. (1978). *Information Retrieval*. Academic Press.
16. Kauffman, S. A. (1993). *The Origins of Order*. Oxford University Press.
17. Weinreich, D. M. et al. (2006). « Darwinian Evolution Can Follow Only Very Few Mutational Paths to Fitter Proteins ». *Science*, 312, 111–114.
18. Cheeseman, P., Kanefsky, B. et Taylor, W. (1991). « Where the Really Hard Problems Are ». *IJCAI 1991*.
19. Mézard, M., Parisi, G. et Zecchina, R. (2002). « Analytic and Algorithmic Solution of Random Satisfiability Problems ». *Science*, 297, 812–815.
20. Weitzman, M. L. (1979). « Optimal Search for the Best Alternative ». *Econometrica*, 47(3), 641–654.
21. Caplin, A., Dean, M. et Martin, D. (2011). « Search and Satisficing ». *American Economic Review*, 101(7), 2899–2922.
22. Jones, C. I. (1995). « R&D-Based Models of Economic Growth ». *Journal of Political Economy*, 103(4), 759–784.
23. Bloom, N., Jones, C. I., Van Reenen, J. et Webb, M. (2020). « Are Ideas Getting Harder to Find? ». *American Economic Review*, 110(4), 1104–1144.
24. Golosovsky, M. et Solomon, S. (2017). « Growing complex network of citations of scientific papers: Modeling and measurements ». *Physical Review E*, 95, 012324. [De mémoire.]
25. Uzzi, B., Mukherjee, S., Stringer, M. et Jones, B. F. (2013). « Atypical Combinations and Scientific Impact in Science ». *Science*, 342, 468–472.
26. Lee, Y.-N., Walsh, J. P. et Wang, J. (2015). « Creativity in scientific teams: Unpacking novelty and impact ». *Research Policy*, 44(3), 684–697.
27. Kuhn, T. S. (1962). *The Structure of Scientific Revolutions*. University of Chicago Press.
28. Popper, K. R. (1959). *The Logic of Scientific Discovery*. Hutchinson.
29. Lakatos, I. (1978). *The Methodology of Scientific Research Programmes*. Cambridge University Press.
30. Sio, U. N. et Ormerod, T. C. (2009). « Does Incubation Enhance Problem Solving? A Meta-Analytic Review ». *Psychological Bulletin*, 135(1), 94–120.
31. Yaqub, O. (2018). « Serendipity: Towards a Taxonomy and a Theory ». *Research Policy*, 47(1), 169–179.
32. Campanario, J. M. (1996). « Using Citation Classics to study the incidence of serendipity in scientific discovery ». *Scientometrics*, 37(1), 3–24.
33. Poincaré, H. (1908). *Science et Méthode*. Flammarion.
34. Hadamard, J. (1945). *The Psychology of Invention in the Mathematical Field*. Princeton University Press.
35. Beeman, M. J. et al. (2004). « Neural Activity When People Solve Verbal Problems with Insight ». *PLoS Biology*, 2(4), e97.
36. Fleming, L. (2001). « Recombinant Uncertainty in Technological Search ». *Management Science*, 47(1), 117–132.
37. Jones, B. F. (2009). « The Burden of Knowledge and the 'Death of the Renaissance Man' ». *Review of Economic Studies*, 76(1), 283–317.
38. Piwowar, H. et al. (2018). « The state of OA: a large-scale analysis of the prevalence and impact of Open Access articles ». *PeerJ*, 6, e4375.
39. Bornmann, L. et Mutz, R. (2015). « Growth rates of modern science ». *JASIST*, 66(11), 2215–2222.
40. Cole, J. R. et Cole, S. (1972). « The Ortega Hypothesis ». *Science*, 178, 368–375.
41. Chao, A. (1984). « Nonparametric Estimation of the Number of Classes in a Population ». *Scandinavian Journal of Statistics*, 11(4), 265–270.
42. Good, I. J. (1953). « The Population Frequencies of Species and the Estimation of Population Parameters ». *Biometrika*, 40(3–4), 237–264.
43. Bubeck, S. et Cesa-Bianchi, N. (2012). « Regret Analysis of Stochastic and Nonstochastic Multi-Armed Bandit Problems ». *Foundations and Trends in Machine Learning*, 5(1), 1–122.
44. Gould, S. J. et Vrba, E. S. (1982). « Exaptation — A Missing Term in the Science of Form ». *Paleobiology*, 8(1), 4–15.
45. Shi, F. et Evans, J. A. (2023). « Surprising combinations of research contents and contexts are related to impact and emerging topics in science ». *Nature Human Behaviour*, 7, 1024–1039. [De mémoire pour année et titre.]
46. Gödel, K. (1931). « Über formal unentscheidbare Sätze der Principia Mathematica und verwandter Systeme I ». *Monatshefte für Mathematik und Physik*, 38, 173–198.
47. Taleb, N. N. (2007). *The Black Swan*. Random House.
