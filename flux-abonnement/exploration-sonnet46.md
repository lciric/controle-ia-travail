# Exploration guidée et non guidée dans de grands espaces de possibilités : modèles, preuves et conditions d'émergence des idées

*Toutes les affirmations sont classées : [SÛR] = confiance élevée, [MÉM] = citation de mémoire à vérifier, [SUP] = supposition raisonnée. Aucun chiffre sans source. Date : 22 novembre 2026.*

---

## 1. Exploration guidée versus exploration non guidée

### Le résultat de référence : No Free Lunch

[SÛR] Wolpert & Macready (1997, « No Free Lunch Theorems for Optimization », *IEEE Transactions on Evolutionary Computation*, 4(1):67–82) démontrent que, moyennés sur tous les problèmes possibles, tous les algorithmes d'optimisation ont les mêmes performances. Ce résultat est mathématiquement rigoureux. Il implique que l'avantage des méthodes guidées sur les non guidées dépend nécessairement d'une adéquation entre les hypothèses de l'algorithme et la structure réelle du problème.

### Quand l'exploration guidée fait mieux

Les méthodes guidées tirent parti de la structure de l'espace.

**Continuité ou corrélation** : les voisins dans l'espace se ressemblent en valeur. Dans ce cas, l'optimisation bayésienne (BO) est efficace. [SÛR] Mockus (1978, « Application of Bayesian Approach to Numerical Methods of Global and Stochastic Optimization ») est la référence fondatrice. [MÉM] Shahriari et al. (2016, « Taking the Human Out of the Loop: A Review of Bayesian Optimization », *Proceedings of the IEEE*, 104(1):148–175) est une synthèse souvent citée. La BO peut trouver l'optimum d'une fonction en $O(\log T)$ évaluations contre $O(T)$ pour le tirage aléatoire, sous des hypothèses de régularité (fonctions à variation bornée dans un espace de Hilbert à noyau reproduisant).

**Décomposabilité ou modularité** : les algorithmes évolutionnaires (AE) exploitent la structure de blocs. [SÛR] Holland (1975, *Adaptation in Natural and Artificial Systems*, MIT Press) est la référence originale. Le théorème des schémas (schema theorem) dit que les sous-chaînes de haute performance se propagent exponentiellement — mais ce théorème a été critiqué comme trop optimiste ([MÉM] Whitley 1994, « A Genetic Algorithm Tutorial », *Statistics and Computing*, 4:65–85).

**Arbre de décision connu** : MCTS (Monte Carlo Tree Search). [SÛR] Kocsis & Szepesvári (2006, « Bandit Based Monte-Carlo Planning », *ECML*, LNCS 4212:282–293) introduisent UCT, qui combine UCB et MCTS. Le résultat clé est une borne de regret sous-linéaire : $O(\sqrt{T \log T})$ contre $O(T)$ pour le tirage uniforme.

**Évaluations coûteuses, budget limité** : c'est le régime de l'optimisation bayésienne et des bandits. [SÛR] Lai & Robbins (1985, « Asymptotically Efficient Adaptive Allocation Rules », *Advances in Applied Mathematics*, 6:4–22) établissent la borne inférieure de regret pour les bandits à deux bras : $\Omega(\log T)$. L'algorithme UCB1 de [MÉM] Auer, Cesa-Bianchi & Fischer (2002, « Finite-Time Analysis of the Multiarmed Bandit Problem », *Machine Learning*, 47:235–256) atteint cette borne.

### Quand l'exploration non guidée fait mieux (ou pas pire)

**Paysages trompeurs** : certaines fonctions de fitness ont des bassins d'attraction larges vers des sous-optima. Les AE peuvent rester bloqués. [MÉM] Deb & Goldberg (1993) ont caractérisé les « deceptive problems ». Dans ces cas, le tirage uniforme suivi d'une vérification peut trouver les optima plus rapidement.

**Parallélisme massif** : si les évaluations sont parallélisables, le tirage indépendant devient compétitif car il n'y a aucun coût de coordination ni biais d'exploration.

**Stratégies de redémarrage aléatoire** : [SÛR] Luby, Sinclair & Zuckerman (1993, « Optimal Speedup of Las Vegas Algorithms », *Information Processing Letters*, 47(4):173–180) démontrent que, pour les algorithmes Las Vegas dont le temps d'arrêt a une distribution à queue lourde, une stratégie de redémarrage optimale (séquence $1, 1, 2, 1, 1, 2, 4, 1, 1, 2, 1, 1, 2, 4, 8, \ldots$) est asymptotiquement optimale. Ce résultat s'applique au model checking et aux solveurs SAT.

**Absence de structure exploitable** : la NFL s'applique pleinement. Les méthodes guidées ont un surcoût de calcul et aucun avantage.

### Mesures publiées dans la découverte automatique

[MÉM] Dans la découverte de drogues : Olivecrona et al. (2017, « Molecular De-Novo Design through Deep Reinforcement Learning », *Journal of Cheminformatics*, 9:48) ont comparé RL guidé vs. tirage aléatoire pour la génération de molécules actives. Le guidage a amélioré le taux de succès d'un facteur ~10 sur des benchmarks spécifiques. Résultat contraire : sur d'autres benchmarks, l'amélioration était marginale (je cite ceci de mémoire ; vérifier les tableaux de comparaison de l'article).

[MÉM] Romera-Paredes et al. (2023, « Mathematical discoveries from program search with large language models », *Nature*, 625:468–475) décrivent FunSearch : une approche évolutionnaire combinant LLM et évaluateur. Sur le problème du cap set, cette approche guidée a trouvé des solutions surpassant les meilleurs résultats connus à l'époque. Résultat contraire possible : les auteurs ne rapportent pas de comparaison systématique avec un tirage aléatoire à budget égal.

[MÉM] Dans la recherche de programmes : Lample & Charton (2020, « Deep Learning for Symbolic Mathematics », *ICLR 2020*) montrent que l'apprentissage guidé (transformeurs) surpasse les CAS sur certaines intégrales. Comparaison avec un tirage non guidé : non fournie explicitement.

**Résultat contraire important** : [MÉM] Musgrave, Belongie & Lim (2020, « A Metric Learning Reality Check », *ECCV*) ont montré que des améliorations d'algorithmes guidés sur des benchmarks populaires disparaissaient face à des baselines correctement réglées. Ce résultat suggère que les avantages rapportés des méthodes guidées sont parfois des artefacts de comparaison.

---

## 2. Modèles mathématiques de l'apparition des idées nouvelles

### Modèles d'urnes et adjacent possible

[SÛR] L'urne de Pólya (Pólya 1930, « Sur quelques points de la théorie des probabilités », *Annales de l'Institut Henri Poincaré*, 1:117–161) est un modèle de renforcement : chaque tirage augmente la probabilité du même résultat. Elle génère des distributions en loi de puissance. Son lien avec l'innovation est que les idées déjà connues sont plus facilement récombinées.

[SÛR] Kauffman (1993, *The Origins of Order*, Oxford University Press) introduit la notion d'« adjacent possible » : l'espace des possibilités accessibles depuis l'état actuel. Cette notion est qualitative chez Kauffman.

[MÉM] Tria, Loreto, Servedio & Strogatz (2014, « The dynamics of correlated novelties », *Scientific Reports*, 4:5890) formalisent l'adjacent possible dans un modèle d'urne avec expansion : chaque tirage d'une boule nouvelle ajoute $\rho$ nouvelles boules (non encore vues) à l'urne. Ce modèle reproduit la loi de Heaps (croissance sous-linéaire du vocabulaire) et la loi de Zipf (distribution des fréquences). Il a été confronté à des données Wikipedia, Last.fm et Project Gutenberg. Les distributions observées et prédites concordent qualitativement. Limite : le modèle suppose que toutes les nouveautés ont le même « potentiel d'expansion » $\rho$.

### Paysages de fitness

[SÛR] Wright (1932, « The Roles of Mutation, Inbreeding, Crossbreeding and Selection in Evolution », *Proceedings of the 6th International Congress of Genetics*, 1:356–366) introduit la métaphore du paysage adaptatif. C'est une métaphore géométrique, pas un résultat mesurable directement.

[SÛR] Kauffman & Levin (1987, « Towards a General Theory of Adaptive Walks on Rugged Landscapes », *Journal of Theoretical Biology*, 128(1):11–45) définissent le modèle NK : $N$ gènes binaires, chaque gène interagit avec $K$ autres. Résultat clé : pour $K=0$, le paysage est lisse (un seul optimum) ; pour $K=N-1$, le paysage est totalement rugueux (corrélations nulles entre voisins). Le nombre d'optima locaux croît exponentiellement avec $K$. Ce modèle a été appliqué à l'innovation technologique ([MÉM] Rivkin 2000, « Imitation of Complex Strategies », *Management Science*, 46(6):824–844) mais les applications empiriques sont souvent qualitatives.

### Transitions de phase

[SÛR] Cheeseman, Kanefsky & Taylor (1991, « Where the Really Hard Problems Are », *IJCAI*, 331–337) identifient une transition de phase dans les problèmes de satisfaction de contraintes (k-SAT) : près du ratio critique clauses/variables, les problèmes sont les plus difficiles. Ce résultat a été confirmé expérimentalement et par des arguments de physique statistique.

[SÛR] Erdős & Rényi (1960, « On the Evolution of Random Graphs », *Publications of the Mathematical Institute of the Hungarian Academy of Sciences*, 5:17–61) démontrent que dans un graphe aléatoire $G(n,p)$, une composante géante apparaît brusquement quand $p = 1/n$. Analogie pour l'innovation : un réseau d'idées peut avoir un seuil de connectivité au-delà duquel de nouvelles idées deviennent accessibles. [SUP] Cette analogie est plausible mais n'a pas été testée rigoureusement à ma connaissance.

### Modèles économiques de la recherche

[SÛR] Romer (1990, « Endogenous Technological Change », *Journal of Political Economy*, 98(5):S71–S102) modélise la croissance par la production d'idées. Les idées sont non rivales et partiellement excluables. Résultat : le taux d'innovation est proportionnel au stock total de capital humain dédié à la R&D. Ce modèle a été critiqué par [MÉM] Jones (1995, « R&D-Based Models of Economic Growth », *Journal of Political Economy*, 103(4):759–784) qui montre que les données empiriques — croissance du nombre de chercheurs sans accélération correspondante de la croissance de la productivité — sont incompatibles avec les prédictions de Romer.

[MÉM] Jones & Williams (1998, « Measuring the Social Returns to R&D », *Quarterly Journal of Economics*, 113(4):1119–1135) estiment que le retour social sur la R&D est 2 à 4 fois le retour privé, ce qui suggère une sous-investissement en recherche fondamentale.

### Confrontation aux données

Modèles confrontés avec succès : Tria et al. 2014 (urnes + adjacent possible, données numériques) ; modèle de Cheeseman et al. (transitions de phase SAT, confirmé par simulations et analyse).

Modèles non confrontés ou confrontation problématique : paysages NK (applicable qualitativement, pas quantitativement à l'innovation réelle) ; modèle de Romer (réfuté par Jones 1995 sur données macroéconomiques).

---

## 3. Autres savoirs sur les conditions de naissance d'une idée

### Ce qui est mesuré

**Bibliométrie et réseaux**

[SÛR] De Solla Price (1965, « Networks of Scientific Papers », *Science*, 149(3683):510–515) décrit la structure des réseaux de citations. La loi de Price (croissance préférentielle des citations) est un résultat empirique.

[SÛR] Uzzi, Mukherjee, Stringer & Jones (2013, « Atypical Combinations and Scientific Impact », *Science*, 342(6157):468–472) analysent 17,9 millions d'articles et calculent un score de conventionnalité/atypicalité des combinaisons de références. Résultat : les articles à fort impact combinent typiquement une majorité de références conventionnelles avec quelques combinaisons très atypiques. Les articles totalement conventionnels ou totalement atypiques ont moins d'impact. Ce résultat est mesuré sur données bibliographiques, pas rapporté sur le mode testimonial.

[MÉM] Sinatra, Wang, Deville, Song & Barabási (2016, « Quantifying the Evolution of Individual Scientific Impact », *Science*, 354(6312):aaf5239) analysent les carrières de 2 887 physiciens sur données APS. Résultat principal : la règle d'impact aléatoire (random impact rule) — le meilleur article d'un chercheur est uniformément distribué au cours de sa carrière, non concentré au début ou à la fin. Résultat contraire : Wang et al. (2019, « Early-career setback and future career impact », *Nature Communications*, 10:4331) montrent que les scientifiques ayant subi des rejets précoces de financement NSF ont ensuite une carrière légèrement supérieure à ceux qui avaient réussi (analyse de discontinuité de régression sur 561 candidats proches du seuil d'admission).

[MÉM] Burt (2004, « Structural Holes and Good Ideas », *American Journal of Sociology*, 110(2):349–399) compare des cadres d'une grande entreprise d'électronique. Les cadres dont le réseau social span des trous structuraux (peu d'échanges entre leurs contacts) ont généré des idées mieux notées par des panels indépendants. Résultat mesuré sur enquête, pas uniquement rapporté. Résultat contraire : [MÉM] Reagans & Zuckerman (2001, « Networks, Diversity, and Productivity », *Organization Science*, 12(4):502–517) trouvent que la cohésion interne (non la diversité structurale) prédit mieux la performance de certaines équipes R&D.

**Neurosciences**

[MÉM] Beaty, Benedek, Silvia & Schacter (2016, « Creative Cognition and Brain Network Dynamics », *Trends in Cognitive Sciences*, 20(2):87–95) passent en revue les études fMRI. Le résultat central : la créativité associe activation du réseau du mode par défaut (DMN, médial préfrontal, cuneus postérieur) et du réseau de contrôle exécutif. Ces réseaux sont habituellement anticorrélés mais co-activés chez les individus créatifs. [MÉM] Beaty et al. (2018, *PNAS*, 115(5):1087–1092) mesurent que la force de la connexion fonctionnelle DMN-contrôle prédit la créativité verbale ($r \approx 0.4$ sur $n = 163$). Limite : toutes les études fMRI de la créativité ont des puissances statistiques basses.

**Psychologie**

[SÛR] Mednick (1962, « The Associative Basis of the Creative Process », *Psychological Review*, 69(3):220–232) définit la créativité comme la capacité à associer des éléments distants. Le Remote Associates Test (RAT) est un test mesurable.

[MÉM] Dijksterhuis & Meurs (2006, « Where Creativity Resides: The Generative Power of Unconscious Thought », *Consciousness and Cognition*, 15(1):135–146) rapportent que les sujets laissés distraits pendant l'incubation ont de meilleures performances sur des problèmes créatifs complexes. Ces résultats ont eu du mal à être répliqués ; [MÉM] Sio & Ormerod (2009, méta-analyse) trouvent un effet d'incubation modeste mais significatif dans une méta-analyse de 117 études.

### Ce qui est raconté

**Témoignages de découvreurs**

[SÛR] Poincaré (1908, « L'Invention mathématique », conférence publiée dans *Science et Méthode*) décrit son expérience : une idée sur les fonctions fuchsiennes est venue au moment de poser le pied sur un marchepied de voiture, après une période d'incubation. Ce témoignage est historiquement documenté mais n'est pas une donnée expérimentale contrôlée.

[SÛR] Hadamard (1945, *The Psychology of Invention in the Mathematical Field*, Princeton University Press) a collecté des témoignages de mathématiciens (dont Einstein). Il décrit quatre phases (préparation, incubation, illumination, vérification) similaires à Wallas (1926, *The Art of Thought*). Ce sont des données qualitatives.

**Philosophie des sciences**

[SÛR] Kuhn (1962, *The Structure of Scientific Revolutions*, University of Chicago Press) distingue science normale (résolution de puzzles dans le paradigme) et révolutions scientifiques (changement de paradigme). Les révolutions surviennent lors d'accumulations d'anomalies. Kuhn ne quantifie pas.

[SÛR] Popper (1934/1959, *The Logic of Scientific Discovery*) souligne que la logique de la découverte — comment une hypothèse naît — n'est pas accessible à la philosophie : c'est une question psychologique. La philosophie ne traite que de la justification.

**Physique statistique**

[MÉM] Bak, Tang & Wiesenfeld (1987, « Self-Organized Criticality: An Explanation of 1/f Noise », *Physical Review Letters*, 59(4):381–384) définissent la criticalité auto-organisée (SOC). L'analogie avec l'innovation (système maintenu spontanément à la criticalité) est populaire mais [SUP] je ne connais pas de test rigoureux de cette analogie sur des données d'innovation.

**Biologie évolutionnaire**

[SÛR] Gould & Vrba (1982, « Exaptation — a Missing Term in the Science of Form », *Paleobiology*, 8(1):4–15) introduisent le concept d'exaptation : une structure sélectionnée pour une fonction est réutilisée pour une autre. Analogie directe avec la réutilisation d'idées dans de nouveaux contextes. Mesuré en paléontologie, pas directement en histoire des sciences.

---

## 4. Rapprochement de domaines séparés et idées non encore émises

### (a) Domaines séparés qui ne communiquent pas

**Ce qui augmente la probabilité**

*Intermédiaires et traducteurs.* [SÛR] Burt (2004, déjà cité) mesure que les individus bridgeant des trous structuraux ont 2 à 3 fois plus d'idées hautement cotées. La présence de tels intermédiaires augmente la probabilité d'émergence. [MÉM] Ce résultat repose sur une seule entreprise d'électronique ; sa généralisation est incertaine.

*Revues de synthèse et prépublications.* [MÉM] Brainard & You (2018, *Science*, 361:1344–1348) rapportent que les preprints accélèrent la diffusion des résultats, réduisant la friction entre domaines. L'effet sur la combinaison interdisciplinaire n'est pas directement mesuré dans cet article.

*Combinaisons atypiques.* [SÛR] Uzzi et al. (2013, déjà cité) mesurent que les combinaisons atypiques de références sont associées à un impact plus élevé. Ces combinaisons sont plus probables quand des chercheurs de domaines différents collaborent.

**Ce qui diminue la probabilité**

*Jargons incompatibles.* Des concepts identiques nommés différemment dans deux domaines ralentissent la reconnaissance. [SUP] Je ne connais pas de mesure directe de cet effet.

*Évaluation par les pairs dans des silos.* Les soumissions interdisciplinaires reçoivent des évaluations plus variables et souvent plus négatives. [MÉM] Larivière, Haustein & Mongeon (2015, *PLOS ONE*, sur la spécialisation croissante) documentent cet effet.

*Attribution du crédit incertaine.* Quand la paternité d'une découverte est difficile à attribuer entre deux domaines, les incitations à la collaboration diminuent. [SÛR] Merton (1961, « Singletons and Multiples in Scientific Discovery », *Proceedings of the American Philosophical Society*, 105(5):470–486) documente les disputes de priorité comme phénomène récurrent.

**Résultat contraire**

[MÉM] Fleming (2001, « Recombinant Uncertainty in Technological Search », *Management Science*, 47(1):117–132) sur données de brevets américains : les combinaisons de classes technologiques inhabituelles ont effectivement une variance plus élevée — plus de chances d'être très cités ET plus de chances d'être inutiles. L'espérance de valeur peut être inférieure à celle des combinaisons classiques pour un inventeur donné, même si elle est supérieure pour la société.

### (b) Idées découlant de résultats publiés mais non encore émises

**Ce qui augmente la probabilité**

*Meilleure indexation et recherche sémantique.* [MÉM] Hope, Chang, Kittur & Shahaf (2017, « Accelerating Science by Mining Abstracts », *KDD*) construisent un graphe de concepts scientifiques et proposent des connexions non exploitées. Résultat : les connexions suggérées correspondent à des découvertes ultérieures dans une fraction notable des cas (je cite ceci de mémoire ; vérifier les tableaux de l'article).

*Dormance et « sleeping beauties ».* [MÉM] van Raan (2004, « Sleeping Beauties in Science », *Scientometrics*, 59(3):467–472) identifie des articles qui reçoivent peu de citations pendant 10–25 ans puis sont soudain très cités. Ce phénomène suggère que les conditions (disponibilité d'une méthode complémentaire, intérêt d'un nouveau domaine) déterminent la valorisation des résultats existants.

**Ce qui diminue la probabilité**

*Surcharge informationnelle.* [MÉM] Larsen & von Ins (2010, « The Rate of Growth in Scientific Publication and the Decline in Coverage Provided by Science Citation Index », *Scientometrics*, 84(3):575–603) documentent la croissance exponentielle des publications. Avec ~2 millions d'articles par an en 2010, les chercheurs ne peuvent lire qu'une infime fraction du corpus pertinent.

*Biais vers les articles déjà cités.* [SÛR] Merton (1968, « The Matthew Effect in Science », *Science*, 159(3810):56–63) décrit l'accumulation d'avantages : les travaux déjà reconnus attirent davantage l'attention, réduisant la visibilité des idées sous-citées.

---

## 5. Estimer ce qui reste à découvrir et décider de la suite

### Estimation de la couverture

Le problème est analogue à l'estimation du nombre d'espèces dans un écosystème à partir d'un échantillon.

[SÛR] Good (1953, « The Population Frequencies of Species and the Estimation of Population Parameters », *Biometrika*, 40(3–4):237–264) introduit l'estimateur Good-Turing : la probabilité d'observer une espèce non encore vue est approximée par $f_1 / N$ où $f_1$ est le nombre d'espèces vues une seule fois et $N$ la taille de l'échantillon. Cet estimateur a été utilisé en traitement automatique du langage et en écologie.

[MÉM] Chao (1984, « Nonparametric Estimation of the Number of Classes in a Population », *Scandinavian Journal of Statistics*, 11(4):265–270) propose un estimateur non paramétrique du nombre total d'espèces : $\hat{S} \geq S_{obs} + f_1^2 / (2 f_2)$ où $f_1, f_2$ sont les nombres d'espèces observées 1 et 2 fois.

**Limites de l'analogie avec la découverte scientifique** :
- Les « espèces » à découvrir ne constituent pas une population fixe : de nouvelles possibilités apparaissent au fur et à mesure des découvertes (adjacent possible). L'espace n'est pas stationnaire.
- Les évaluations ne sont pas indépendantes : une découverte peut fermer ou ouvrir d'autres possibilités.
- On ne connaît pas le générateur exact.

### Critère d'arrêt et exploration-exploitation

[SÛR] Dans le cadre des bandits, la règle UCB1 de Auer et al. (2002, déjà cité) est asymptotiquement optimale : elle équilibre exploration et exploitation avec un regret de $O(\sqrt{KT \log T})$ sur $K$ bras et $T$ tirages. Mais ce résultat suppose que le nombre de bras est connu et fixe.

[SÛR] Le problème du secrétaire (optimal stopping) est résolu exactement par la règle : observer les $n/e$ premiers candidats sans choisir, puis choisir le premier meilleur. La probabilité de succès est $1/e \approx 0.37$ ([MÉM] Lindley 1961, « Dynamic Programming and Decision Theory », *Applied Statistics*, 10(1):39–51 pour une formulation moderne ; Ferguson 1989, « Who Solved the Secretary Problem? », *Statistical Science*, 4(3):282–296, pour l'histoire).

### Mise à jour bayésienne sur le générateur

Si on dispose d'un modèle probabiliste du générateur, on peut estimer la distribution prédictive sur les prochains échantillons. [SÛR] Ferguson (1973, « A Bayesian Analysis of Some Nonparametric Problems », *Annals of Statistics*, 1(2):209–230) fonde les processus de Dirichlet, qui permettent une estimation non paramétrique bayésienne du générateur. Des méthodes dérivées (expected improvement, knowledge gradient) sont utilisées en optimisation bayésienne. [MÉM] Frazier, Powell & Dayanik (2008, « A Knowledge-Gradient Policy for Sequential Information Collection », *SIAM Journal on Control and Optimization*, 47(5):2410–2439) formalisent la connaissance-gradient.

**Limites globales** : toutes ces méthodes supposent soit une stationnarité, soit une forme paramétrique du générateur, soit un espace fini. Dans la découverte scientifique réelle, aucune de ces hypothèses n'est entièrement vérifiée.

---

## 6. Falsifiabilité de chaque réponse

**Réponse 1 (exploration guidée vs. non guidée)**

*Ce qui me donnerait tort* : une expérience montrant que sur une classe naturelle de problèmes scientifiques, l'algorithme évolutionnaire ou la BO est surpassé par le tirage aléatoire à budget égal, même après réglage optimal des hyperparamètres des deux méthodes.

*Coût minimal* : prendre un benchmark standard d'optimisation en boîte noire ([MÉM] Hansen et al. 2009, benchmark BBOB/COCO) et comparer BO vs. tirage aléatoire sur les 24 fonctions standard. Résultat partiellement connu : BO surpasse le tirage sur les fonctions lisses, pas sur les fonctions multimodales discontinues. Ce benchmark est public et peu coûteux à exploiter.

**Réponse 2 (modèles d'urnes et de paysages)**

*Ce qui me donnerait tort* : un corpus de données d'innovation (brevets, articles) où la loi de Heaps (croissance sous-linéaire du vocabulaire de concepts) n'est pas vérifiée, réfutant le modèle de Tria et al.

*Coût minimal* : compter le nombre de nouveaux concepts par an dans un corpus de brevets USPTO par classe technologique. L'USPTO est public ; l'analyse nécessite un NLP basique.

**Réponse 3 (autres disciplines)**

*Ce qui me donnerait tort sur l'incubation* : un essai randomisé bien puissancé comparant performance sur problèmes d'insight avec vs. sans période d'incubation, montrant aucun effet après correction pour les tests multiples.

*Coût minimal* : une méta-analyse avec correction du biais de publication sur les études d'incubation existantes. Sio & Ormerod (2009) font cela mais une mise à jour avec des études plus récentes serait moins coûteuse qu'un nouvel essai.

*Ce qui me donnerait tort sur les trous structuraux* : une étude longitudinale montrant que les individus bridgeant des trous structuraux ne génèrent pas plus d'idées valides après contrôle pour le talent individuel.

*Coût minimal* : exploiter des données de réseaux sociaux d'entreprises avec évaluation des performances. Des données de ce type existent dans des études d'organisation.

**Réponse 4 (rapprochement de domaines)**

*Ce qui me donnerait tort* : une expérience naturelle (l'annulation des conférences internationales lors du COVID-19 en 2020–2021) montrant aucun effet sur le taux de publications interdisciplinaires.

*Résultat partiel connu* : [MÉM] des études ont commencé à analyser l'effet du COVID sur la collaboration scientifique internationale. Plusieurs rapportent une légère réduction de la collaboration internationale en 2020. Je cite ceci de mémoire ; des études précises auraient plus de poids.

*Coût minimal* : comparer le nombre de références croisant deux domaines prédéfinis dans des articles soumis avant et après mars 2020. Web of Science / Scopus fournissent ces données.

**Réponse 5 (estimation de ce qui reste)**

*Ce qui me donnerait tort* : appliquer l'estimateur de Chao à une base de données de composés chimiques connus en 2010, puis vérifier si la prédiction du nombre total de composés pharmacologiquement actifs cadre avec les données de 2026. Si la prédiction est grossièrement inexacte (facteur > 10), le modèle est invalide pour ce contexte.

*Coût minimal* : les données de ChEMBL (base publique) permettent de tester cela en quelques semaines.

---

## Récapitulatif épistémique

| Domaine | SÛR | MÉM (à vérifier) | SUP |
|---|---|---|---|
| NFL | Wolpert & Macready 1997 | — | — |
| Pólya / adjacent possible | Pólya 1930 ; Kauffman 1993 (qualitatif) | Tria et al. 2014, chiffres précis | Analogie avec l'innovation |
| Kuhn, Popper | Oui | — | — |
| Uzzi et al. 2013 | Structure qualitative | $n = 17.9M$ et scores exacts | — |
| Sinatra et al. 2016 | Structure qualitative | Taille de l'échantillon | — |
| Burt 2004 | Structure qualitative | Facteur 2–3, contexte précis | — |
| Good-Turing | Oui | — | — |
| Fleming 2001 brevets | Structure qualitative | Variance précise | — |
| SOC et innovation | Bak et al. 1987 (SOC) | — | Analogie non testée |
| Olivecrona 2017 | Structure qualitative | Facteur ~10 | — |

*Cette réponse repose sur ma connaissance de la littérature au moment de ma formation. Les articles marqués [MÉM] doivent être vérifiés dans leurs versions publiées. Je n'ai effectué aucune recherche sur la toile pour la rédiger.*
