# Théorèmes sur les vallées, les seuils et les pics étroits — rapport de lecture (22 novembre 2026)

Dossier des sources : `/tmp/claude-0/-home-user-controle-ia-travail/7225ef84-cf06-5367-97a0-6c2a4e600e2b/scratchpad/sources/theoremes-vallees/`. Les pages sont celles du fichier PDF ; le numéro imprimé est donné entre crochets quand il diffère.

## Empreintes

| Fichier | Source | sha256 (16 premiers) |
|---|---|---|
| oliveto2018.pdf | eprints.whiterose.ac.uk/id/eprint/122143 (Algorithmica, CC-BY) | 50ffb2cfc0f009d2 |
| 1703.03334.pdf | arxiv.org/pdf/1703.03334 | ef55e3212005db12 |
| 1801.10087.pdf | arxiv.org/pdf/1801.10087 | a435e762a510b119 |
| dang2018.pdf | eprints.whiterose.ac.uk/118392/7/08019856.pdf | 022b182ee0d9a3a8 |
| wilke2005.pdf | authors.library.caltech.edu/records/v037b-7ye38 | b990f2d057dcf2c2 |
| 2109.14409.pdf | arxiv.org/pdf/2109.14409 | 6b0d4e58899b5ef6 |
| 1511.02476.pdf | arxiv.org/pdf/1511.02476 | d096e3391b537ed5 |
| 1810.05129.pdf | arxiv.org/pdf/1810.05129 (v3) | 3aeeab11c85b5aad |
| math_0701741.pdf | arxiv.org/pdf/math/0701741 (v2, tiré à part des Annals of Applied Probability) | 26d04e6a5a79ee1e |
| 1605.06444.pdf | arxiv.org/pdf/1605.06444 | 3e8f05bb54d45b4c |
| weissman2009_pmc.xml | PubMed Central PMC2992471 (texte intégral du manuscrit d'auteur, XML) | 11b30e10252f6512 |
| vannimwegen2000.pdf | arxiv.org/pdf/adap-org/9907002 | ddde6c757f9b89ec |
| woodard2009.pdf | maths.tcd.ie/EMIS/journals/EJP-ECP/article/download/638/870.pdf | eb59a71e9226bab1 |

Les empreintes complètes sont dans le message final.

---

## 1. Oliveto, Paixão, Pérez Heredia, Sudholt, Trubenová 2018, Algorithmica 80(5):1604–1633 — lu sur PDF

- **Montage.** La fonction « Valley » est bâtie sur un « long k-path ». La pente descend sur une longueur ℓ1, d'une profondeur d1, puis remonte sur une longueur ℓ2, d'une hauteur d2, avec d2 > d1 (p. 7–9).
- **Théorème 3 (p. 9).** « Assume ℓ1+ℓ2 ≤ √n/4 and d1 ≤ d2. The expected time for the (1+1) EA starting in P0 to cross the fitness valley is Θ(n^ℓ*) where ℓ* = ℓ1 + d1ℓ2/d2. » L'algorithme élitiste dépend donc de la **longueur effective** : la distance jusqu'au premier point de fitness au moins égale.
- **Théorème 11 (p. 16).** Régime de sélection forte et mutation faible (SSWM), mutations locales : E(T) = O(n·e^{2Nβd1(ℓ1+1)/ℓ1}) + Θ(n·ℓ2), et la borne inférieure correspondante Ω(n·e^{2(N−1)βd1(ℓ1−1)/ℓ1}) + Θ(n·ℓ2). Hypothèses : « provided βd1/ℓ1, βd2/ℓ2 = Ω(1) and N being a large enough constant ». Le texte dit : « for the SSWM the growth is exponential in the depth of the valley. »
- **Théorème 13 (p. 19).** Metropolis : E(T) = O(n·e^{αd1(1+1/ℓ1)}) + Θ(n·ℓ2), et Ω(n·e^{αd1(1−1/ℓ1)}) + Θ(n·ℓ2), sous αd1/ℓ1, αd2/ℓ2 = Ω(1).
- **Théorèmes 17 et 18 (p. 24).** Sur une suite de m vallées (« ValleyPath »), les deux algorithmes non élitistes ont un temps de O(m·n·e^{…}) + Θ(ℓ2) si 2β(N−1)(d2−d1) ≥ c (SSWM), ou α(d2−d1) ≥ c (Metropolis).
- **Ce que ça ne dit pas.** Les analyses ne portent que sur des chemins de dimension un plongés dans l'hypercube, sur une seule trajectoire, sans population ni recombinaison. Les bornes sont asymptotiques. Le résultat ne dit rien d'une vallée où le chemin n'est pas imposé. Ta formule de mémoire est juste, à une précision près : pour l'élitiste, c'est la longueur **effective** ℓ*, qui dépend aussi du rapport d1/d2.

## 2. Doerr, Le, Makhmara, Nguyen 2017, « Fast Genetic Algorithms », arXiv 1703.03334 — lu sur PDF

- **Résumé (p. 1).** « For the Jump_{m,n} function, any mutation rate between 2/n and m/n leads to a speed-up at least exponential in m compared to the standard choice. » Et : « Any deviation by a small (1 ± ε) factor leads to a slow-down exponential in m. »
- **Théorème 1 (p. 10).** Pour p ≤ m/n : (1/2)·1/(p^m(1−p)^{n−m}) ≤ T_p(m,n) ≤ 3·1/(p^m(1−p)^{n−m}). Pour p ∈ [2/n, m/n] : T_p ≤ O(2^{−m}·T_{1/n}).
- **Lemme ou théorème p. 13.** Tout taux hors de [(1−ε)m/n, (1+ε)m/n] est plus lent que l'optimum « by a factor of at least (1/6)exp(mε²/5) ».
- **Théorème 6 (p. 21).** « Let n ∈ N and β > 1. For all m ∈ [2..n/2] with m > β − 1, the expected optimization time T_β(m,n) of the (1+1) EA with mutation operator fmut_β is T_β(m,n) = O(C^β_{n/2} m^{β−0.5} T_opt(m,n)). » Le taux de mutation est α/n, et α suit une loi de puissance d'exposant β.
- **Théorème 5 (p. 20).** Le pire cas sur toute fonction est O(C^β_{n/2} 2^n n^β), contre n^n pour la mutation standard.
- **Ce que ça ne dit pas.** Le gain est un facteur polynomial en m, soit m^{β−0.5}, au-dessus du meilleur taux fixe connu à l'avance. Le temps reste de l'ordre de (en/m)^m environ, donc exponentiel en m : la vallée reste chère, on évite seulement de mal choisir le taux. Le résultat vaut pour le (1+1) EA, sans population.

## 3. Jansen et Wegener 2005, « Real royal road functions », Discrete Applied Mathematics 149 — non lu sur l'original

L'article original n'a pas été trouvé en accès libre. Ce qui suit est lu dans la synthèse de Sudholt (1801.10087.pdf, p. 18–20).

- **Énoncé rapporté (p. 18).** « a simple genetic algorithm (GA) with crossover takes expected polynomial time, whereas all (µ+λ) evolutionary algorithms using only standard bit mutation need exponential time with overwhelming probability. »
- **Théorème 15 de la synthèse (p. 19), simplifié du Théorème 3 de l'article.** Si pc ≤ 1−ε et µ ≥ 2n/3+1, le (µ+1) GA qui départage les ex aequo en faveur des génotypes les moins dupliqués a un temps O(µn³ + (µ log µ)n + µ²/pc) sur R_n, donc O(n⁴).
- **Hypothèses.** La fonction est construite pour l'occasion, avec une vallée de fitness 0. Un mécanisme anti-doublons est indispensable à la preuve (p. 20).
- **Statut :** de la synthèse seulement ; l'énoncé original est à vérifier sur le PDF.

## 4. Dang, Friedrich, Kötzing, Krejca, Lehre, Oliveto, Sudholt, Sutton 2018, IEEE Transactions on Evolutionary Computation 22(3) — lu sur PDF (manuscrit d'auteur)

- **Théorème 6 (p. 7–9 du fichier ; Théorème 21 de la synthèse, p. 24).** Le (µ+1) GA avec pc = 1 et µ ≤ κn, sur Jump_k avec 3 ≤ k = o(n), a un temps O(n^k/µ + n^{k−1} log µ). Pour µ = κn, cela donne O(n^{k−1} log n), soit un gain Ω(n/log n) sur le Θ(n^k) du (1+1) EA.
- **Théorème 10 (p. 9).** « The (µ+1) GA with mutation rate (1+δ)/n, for a constant δ > 0, and population size µ ≥ ck ln(n) … has for k = o(n) expected optimisation time O(n√k µ log(µ) + µ² + n^{k−1}) on Jump_k. »
- **Tableau 2 de la synthèse (p. 25).** Pour les mécanismes de diversité (îles, partage de fitness, distance de Hamming maximisée), le temps tombe à O(n log n + kn + 4^k) avec les meilleurs réglages.
- **Ce que ça ne dit pas.** Le gain reste en n^{k−1}, donc exponentiel en k, sauf avec un mécanisme explicite où l'on atteint 4^k. Ces résultats ne valent que pour Jump : tous les optima locaux sont à la même distance k de l'optimum, et la recombinaison exploite cette symétrie.

## 5. Lässig et Sudholt 2010 (GECCO) et 2013 (Soft Computing 17:1121–1144) — non lu sur l'original

Aucun des deux originaux n'a été lu. Il n'y a pas de dépôt ouvert trouvé, seulement une copie sur un domaine miroir non officiel, que je n'ai pas prise. Ce qui suit est lu dans la synthèse de Sudholt (1801.10087.pdf, p. 14–16).

- **Énoncé rapporté (p. 14).** « a simple island model, all islands running (1+1) EAs, finds the optimum in polynomial time, with high probability. This holds for a proper choice of the migration interval and any migration topology that is not too sparse. Contrarily, both a single, large population as in the (µ+1) EA as well as independent islands … need exponential time, with high probability. »
- **Théorème 11 de la synthèse (p. 15).** Le (µ+1) EA avec µ ≤ cn/log n, sur LOLZ_{n,z,b,ℓ} avec z = ω(log b), bℓ ≤ n et z < ℓ, ne trouve pas l'optimum en n^{z/3} générations, avec une probabilité d'au moins 1 − e^{−Ω(z)} − 2^{−b}. Pour s îles indépendantes, la probabilité est d'au moins 1 − s·e^{−Ω(z)} − s·2^{−b}.
- **Théorème 12 de la synthèse (p. 15–16).** Topologie « well-expanding », τ = n^{5/3}, µ = n^{Θ(1)} îles, ℓ = 2n^{2/3}, z = n^{2/3}/2, b ≤ n^{1/6}/16, compteur de migration démarré à τ/2 : l'optimum est trouvé en O(bℓn) = O(n²) générations, avec une probabilité écrasante.
- **Rôle de l'intervalle de migration (p. 15–16).** Il faut migrer après la rupture de symétrie sur un bloc, sinon des îles parties vers les zéros envahissent celles parties vers les uns. Il faut aussi laisser une période d'évolution indépendante après chaque migration, pour que les blocs futurs redeviennent indépendants : « The island model is only successful because it can use both migration and periods of independent evolution. »
- **Contre-exemple sur le même thème (p. 18).** Sur les cycles eulériens, si τ·diam(T)·λ = O(m²), le temps est Ω(m⁴/log λ). Le gain est alors au mieux logarithmique : selon l'intervalle, on passe d'un gain exponentiel à un gain logarithmique.

## 6. Sudholt 2020, synthèse, arXiv 1801.10087 — lu sur PDF

Ses énoncés utiles sont repris aux points 3, 4 et 5.

- Synthèse sur les vallées de Jump (p. 23) : « mutation-only algorithms such as the (1+1) EA require expected time Θ(n^k) ».
- Le (µ+1) GA de Jansen et Wegener met O(µn²k³ + 4^k/pc), mais « requires an unrealistically small crossover probability pc ≤ 1/(ckn) ».
- Paysage mobile « Maze » (p. 29) : le (1+λ) EA avec λ = O(n^{1−ε}) perd l'optimum avec forte probabilité (Théorème 30). Un modèle à c·log n îles, avec une migration alignée sur la période de changement, le suit en temps polynomial (Théorème 31).

## 7. Wilke, Wang, Ofria, Lenski, Adami 2001, Nature 412:331–333 — résumé seulement

L'article est sous mur payant ; je ne l'ai pas contourné. Le résumé a été lu par PubMed (identifiant 11460163) :

- « Forty pairs of populations were derived from 40 different ancestors in identical selective environments, except that one of each pair experienced a 4-fold higher mutation rate. In 12 cases, the dominant genotype that evolved at the lower mutation rate achieved a replication rate >1.5-fold faster than its counterpart. … In each case, as mutation rate was increased, the outcome of competition switched to favour the genotype with the lower replication rate. These genotypes, although they occupied lower fitness peaks, were located in flatter regions of the fitness surface and were therefore more robust with respect to mutations. »
- **Nature du résultat.** C'est un résultat expérimental sur des organismes numériques (le logiciel Avida), pas un théorème. Il porte sur 12 paires sur 40. Le texte ne dit pas que la stratégie plate l'emporte en général. Il montre une inversion de l'issue de la compétition quand la mutation croît, dans ces 12 cas.
- **Le même effet dans Wilke 2005 (wilke2005.pdf, p. 4).** « sequences with high fitness can lose out against sequences with lower fitness that have better support from their mutational neighbors … survival of the flattest. »

## 8. Seuil d'erreur d'Eigen — Wilke 2005, BMC Evolutionary Biology 5:44 — lu sur PDF

- **P. 5.** « Eigen described the error threshold in his 1971 paper as a limit to the amount of information a genome can store at a given mutation rate. » Plus loin : « it is a deterministic effect … the position of the error threshold depends only weakly on the population size, and … even in an infinite population the error threshold occurs at a finite mutation rate. »
- **P. 6.** « Wagner and Krall have proven mathematically that the condition for the existence of an error threshold is precisely the complete absense of lethal genotypes. »
- **P. 6, toujours.** L'existence et la position du seuil « depend on the choice of the fitness landscape ». La plupart des travaux ne considèrent que le paysage à pic unique.
- **P. 6, sur la survie du plus plat.** Elle est présentée comme cas particulier de la « error cascade » de Tannenbaum et Shakhnovich.
- **Forme du seuil dans van Nimwegen et Crutchfield (vannimwegen2000.pdf, p. 14).** Sur un pic d'avantage σ et un génome de longueur L, l'instabilité survient près de σ(1−µ)^L = 1, soit log σ ≈ Lµ.
- **Ce que ça ne dit pas.** Ce n'est pas une loi universelle. En présence de génotypes létaux, il n'y a pas de seuil au sens d'Eigen.

## 9. Gamarnik 2021, « The overlap gap property », PNAS 118 ; arXiv 2109.14409 — lu sur PDF

- **Définition (p. 9).** « the optimization problem min_σ L(σ,ξ) exhibits the OGP with values µ > 0, 0 ≤ ν1 < ν2 if for every two solutions σ, τ which are µ-optimal … it is the case that either ρ_N(σ,τ) ≤ ν1 or ρ_N(σ,τ) ≥ ν2. »
- **Mécanisme d'exclusion (p. 12).** On suppose la propriété vérifiée en ensemble sur une famille interpolée ξ_t, deux conditions remplies — (a) les extrémités ont des solutions éloignées, (b) κ < ν2 − ν1 — et un algorithme κ-stable, c'est-à-dire dont la sortie bouge peu quand l'instance bouge peu. Alors « any κ-stable algorithm fails to produce a µ-optimal solution ».
- **Classes d'algorithmes exclues (p. 16–18).** Polynômes de bas degré, passage de messages approché (AMP), algorithmes locaux, et la dynamique de Langevin sur une échelle de temps linéaire en N. Le texte reste prudent sur ce dernier point : « It is a very plausible conjecture, though, that the Langevin dynamics indeed still fails unless it is ran for exponentially long … We leave this conjecture as an interesting open problem. »
- **Exemples (p. 15–18).** Clique maximale, ensemble indépendant (le m-OGP règle le cas au-delà de α = 1), partition de nombres, verres de spin p-spin. Pour ces derniers, les algorithmes de Montanari atteignent l'optimum exactement là où la propriété est absente (p. 18).
- **Ce que ça ne dit pas (p. 19).** Ce n'est pas une preuve de difficulté au sens de NP. Il existe un modèle à faible regroupement en grappes réduites à des singletons — le perceptron symétrique —, des « aiguilles dans une botte de foin », qui serait pourtant soluble en temps polynomial (à condition que l'algorithme de Kim et Roche s'étende). Un paysage d'aiguilles isolées n'implique donc pas à lui seul la difficulté algorithmique.

## 10. Zdeborová et Krzakala 2016, Advances in Physics 65 ; arXiv 1511.02476 — lu sur PDF

- **Objectif (p. 12).** « Determine the threshold αc between the inference-impossible and inference-possible region, and the threshold αs between the inference-hard and inference-easy region. » Et : « In many problems the intermediate hard phase is missing and αc = αs. »
- **Quatre phases, coloriage planté à 5 couleurs (p. 37–38).** Elles sont définies par le propagateur de croyances lancé depuis une **initialisation au hasard** et depuis une **initialisation plantée** :
  - indétectable paramagnétique, c < cd : « belief propagation converges to the uniform fixed point both from random and planted initialization » ;
  - indétectable en grappes, cd < c < cc ;
  - **difficile détectable**, cc < c < cs : « The Bayes optimal marginals are correlated to the planted configuration, however, there is a metastable paramagnetic phase to which belief propagation converges from a random initialization » ;
  - facile détectable, c > cs.
  - La figure 6 (p. 38) trace les deux courbes de recouvrement, initialisation plantée et au hasard : elles divergent entre cc et cs.
- **Pas de phase difficile en transition du second ordre (p. 23 et p. 36).** « Inference is either impossible, or possible and tractable. The hard phase … is absent. » La phase difficile demande une transition discontinue, du premier ordre.
- **Statut de la barrière (p. 41).** Dans la phase difficile, la méthode de Monte-Carlo et le propagateur de croyances « fail and get blocked in the metastable paramagnetic phase ». Le seuil cs est une barrière pour toutes les méthodes spectrales connues. Mais la conjecture d'une barrière pour tous les algorithmes polynomiaux est fausse en général : le XOR-SAT planté se résout par élimination de Gauss. Les auteurs posent ouvertement la question : « In which exact sense is the hard phase hard? »
- **Ordres de grandeur, grand nombre de groupes q (p. 52).** γd ≈ 2q log q, γc ≈ 4q log q, γs = q² : la phase difficile est très large.
- **Contournement par couplage spatial (p. 42–43).** Une nucléation fait disparaître la région spinodale quand la structure peut être dessinée, ce qui n'est possible que si l'on conçoit l'instance.
- **Ce que ça ne dit pas.** Une grande partie relève des prédictions de la physique, non démontrées. Le texte sépare les parties prouvées, par exemple p. 22 sur la transition du second ordre.

## 11. Addario-Berry et Maillard 2020, arXiv 1810.05129 — lu sur PDF

- **Modèle (p. 2).** Processus gaussien sur l'arbre binaire de profondeur N, avec E[X_v X_w] = N·A(R_N(v,w)). L'algorithme est une suite de requêtes adaptées à la filtration : modèle de requêtes en boîte noire.
- **Théorème 1.1 (p. 2–3).** « Suppose that there exists a Riemann-integrable function a … such that A(t) = ∫0^t a(s)ds. » Soit x* = √(2 log 2) ∫0^1 √a(t) dt. Alors :
  - (1) pour tout x < x*, un algorithme en temps linéaire trouve v avec X_v ≥ xN, avec forte probabilité ;
  - (2) pour tout x > x*, il existe γ > 0 tel que, pour tout algorithme, le nombre de requêtes « is stochastically bounded from below by a geometric random variable with parameter exp(−γN) ».
- **P. 4.** On a x* ≤ x_s, l'énergie du fondamental, avec égalité si et seulement si A est concave. « The concavity of A is therefore a necessary and sufficient condition for the existence of efficient algorithms for finding a node whose energy is within a (1 − o(1)) factor of the ground state energy. »
- **Ce que ça ne dit pas.** Le modèle est jouet : arbre hiérarchique gaussien. La borne inférieure vaut contre **tout** algorithme de requêtes, mais seulement dans ce modèle.

## 12. Pemantle 2009, Annals of Applied Probability 19(4):1273–1291 — lu sur PDF

- **Résumé (p. 1 [1273]).** Arbre binaire avec des variables de Bernoulli de moyenne p ≤ 1/2. Pour s'approcher du chemin optimal à un facteur 1−ε : « In the case p = 1/2 … it is shown to take Θ(ε^{−1}n) steps. In the case p < 1/2, the number of steps is shown to be at least n·exp(const ε^{−1/2}). »
- **Théorème 3.3 (p. 10).** Cas p = 1/2. Pour tout algorithme et tout κ < 1/2, la probabilité de trouver un chemin avec au moins (1−ε)n uns avant le temps κε^{−1}n est O(1/n).
- **Théorème 3.4 (p. 10).** Cas p < 1/2. La borne est exprimée par ρ(p, sε, ε^{−3/2}). Avec la Proposition 2.6 (p. 8), on obtient la borne en exp(const·ε^{−1/2}). La borne supérieure correspondante (recherche en profondeur itérée) n'est démontrée que dans le sous-cas c(p) − ε = 1/2 ; ailleurs, elle dépend d'une conjecture (Conjecture 1, p. 10).
- **Ce que ça ne dit pas.** Le coût reste linéaire en n pour un ε fixé, mais explose quand ε → 0. C'est la quasi-optimalité qui coûte, pas la bonne qualité.

## 13. Baldassi, Borgs, Chayes, Ingrosso, Lucibello, Saglietti, Zecchina 2016, PNAS 113 ; arXiv 1605.06444 — lu sur PDF

- **Résumé (p. 1).** « theoretical and numerical evidence of the existence of rare—but extremely dense and accessible—regions of configurations ».
- **P. 3.** Dans les problèmes de contraintes, il n'existe pas d'algorithme efficace connu quand toutes les solutions sont « frozen ». Dans la limite où presque toutes les variables sont fixées, « the clusters are isolated point-like regions ». Pour l'apprentissage à poids discrets, la description à l'équilibre prédit que toutes les solutions sont « locked », « in spite of the fact that efficient algorithms seem to exist ».
- **P. 4.** « in a high-dimensional space the isolated global minima can be exponentially more numerous and thus dominate the equilibrium measure ». Les algorithmes efficaces « invariably find solutions belonging to high-density regions when these regions exist, and fail otherwise ».
- **Ce que ça ne dit pas.** Ce sont des calculs de physique, sans théorème de temps de calcul, et des expériences numériques. Le passage aux réseaux profonds est une conjecture des auteurs (p. 1).

## 14. Weissman, Desai, Fisher, Feldman 2009, Theoretical Population Biology 75(4):286–300 — lu sur la page HTML

La source est le texte intégral XML de PubMed Central, PMC2992471 ; il n'y a pas de pagination.

- **Résumé.** « We calculate the rate at which a population crosses a fitness valley or plateau of arbitrary width, as a function of the mutation rates, the population size, and the fitnesses of the intermediates. We find that when intermediates are close to neutral, a large population can cross even wide fitness valleys remarkably quickly … In smaller populations … below a threshold size which depends on the width of the fitness valley and the strength of selection against intermediate genotypes, valley-crossing is much less likely. »
- **Régimes nommés.** « sequential fixation », pour les petites populations, contre « stochastic tunneling », pour les grandes, et des régimes « semi-deterministic » et « deterministic » quand N est très grand. Pour des intermédiaires neutres, p1 ∼ √(µ1 s) en tunnel, et ∼ 1/N si N < 1/√(µ1 s).
- **Méthode.** Une analyse formelle (« rigorously derive », section IV, par transformées de Laplace) avec des approximations, complétée par des simulations pour K = 2 et 3. Ce n'est pas un théorème au sens de l'informatique théorique.

## 15. van Nimwegen et Crutchfield 2000, Bulletin of Mathematical Biology 62 ; arXiv adap-org/9907002 — lu sur PDF

- **Résumé (p. 1).** « the waiting times to reach higher fitness depend strongly on the width of a fitness barrier and much less on its height. … crossing entropy barriers is faster by orders of magnitude than fitness barrier crossing. … If no such escape route along a neutral path exists, a population is most likely to cross a fitness barrier where the barrier is narrowest, rather than where the barrier is shallowest. »
- **Équation 33 (p. 14).** ⟨t⟩ ∝ (1/(w!·Mµ))·(log σ/µ)^{w−1}. Et : « high barriers can be passed relatively easily, as long as they are narrow; while wide barriers take a very long time to cross, even if they are shallow. »
- **Méthode.** Analytique avec approximations (p. 9 : « we made several approximations »), comparée aux simulations (figure 3, p. 11).
- **Contradiction apparente avec le point 1, à noter.** Ici, population de Wright-Fisher avec mutation par site : la largeur domine. Chez Oliveto et al., trajectoire unique non élitiste à mutations locales : la profondeur domine. Les deux sont cohérents. Une population à mutation multi-sites franchit la vallée par saut, comme l'élitiste ; un marcheur local doit la descendre.

## 16. Woodard, Schmidler, Huber 2009, Electronic Journal of Probability 14:780–804 — lu sur PDF

- **Persistance, équation 4 (p. 8 [787]).** γ(A,φ) = min{1, φ[A]/π[A]}.
- **Corollaire 3.2 (p. 11 [790]).** S'il existe β* < β** tels que :
  - (1) la conductance de A soit exponentiellement décroissante sur [β**, 1] ;
  - (2) la persistance soit exponentiellement décroissante sur [β*, β**) ;
  - (3) β* = inf B, ou le recouvrement soit exponentiellement décroissant,
  - « Then parallel and simulated tempering are torpidly mixing ». Torpide veut dire un trou spectral exponentiellement petit.
- **Exemple 4.1 (p. 12 [791]).** Mélange à poids égaux ½ N(−1_M, σ1²I) + ½ N(1_M, σ2²I) avec σ1 > σ2. Le pic étroit est A2, et « parallel and simulated tempering are also torpidly mixing for this target distribution for any choice of temperatures ». Avec σ1 = σ2, le mélange est rapide (Woodard et al. [22]).
- **Résumé (p. 1 [780]).** « anytime a multimodal distribution includes both very narrow and very wide peaks of comparable probability mass, parallel and simulated tempering are shown to mix slowly ». Ce mélange lent « commonly used convergence diagnostics will fail to detect ».
- **Conclusion (p. 20 [799]).** Initialisée dans un pic large, la chaîne « will take a very large number of iterations to discover the narrow peaks ».
- **Ce que ça ne dit pas.** La section 5 (p. 19–20) est une interprétation (« informally speaking », « slow mixing in a relative sense »). Le théorème porte sur des masses **comparables**, pas sur un pic étroit de faible masse. Il concerne l'échantillonnage, c'est-à-dire l'équilibre, pas l'optimisation.

---

## Synthèse (dix lignes)

1. **Vallée étroite, de largeur k, à la position fixée.** Mutation à queue lourde, sans réglage : à un facteur m^{β−0.5} de l'optimal (Doerr et al., Théorème 6). Recombinaison avec diversité : n^{k−1} ou 4^k (Dang et al.). Le coût reste exponentiel en k.
2. **Vallée longue mais peu profonde.** Les procédés qui acceptent de descendre (Metropolis, sélection forte et mutation faible) paient e^{profondeur}. L'élitiste paie n^{longueur effective} (Oliveto et al., Théorèmes 3, 11, 13).
3. **Populations à mutation multi-sites.** La largeur domine la hauteur. Les chemins neutres sont plus rapides de plusieurs ordres de grandeur (van Nimwegen et Crutchfield, p. 1 et 14). Une grande population traverse vite des vallées presque neutres (Weissman et al.).
4. **Décisions successives irréversibles.** Des îles avec un intervalle de migration réglé sont polynomiales, là où une population unique et des courses indépendantes sont exponentielles (Lässig et Sudholt, d'après la synthèse ; original non lu).
5. **Cible plantée.** Une transition du second ordre donne seulement « impossible » ou « facile ». Une transition du premier ordre ouvre une phase difficile où le propagateur de croyances parti du hasard reste bloqué et celui parti de la cible la garde. Elle n'est pas démontrée difficile pour tous les algorithmes : le XOR-SAT planté en est le contre-exemple (Zdeborová et Krzakala, p. 37–41).
6. **Recouvrement à trou.** Il exclut les algorithmes stables : polynômes de bas degré, passage de messages approché, Langevin en temps linéaire. Les solutions isolées seules ne suffisent pas à prouver la difficulté (Gamarnik, p. 12, 18, 19).
7. **Bornes contre tout algorithme de requêtes, en modèles jouets.** Au-delà de x*, le coût est exponentiel (Addario-Berry et Maillard, Théorème 1.1). La quasi-optimalité à ε près coûte n·exp(c·ε^{−1/2}) (Pemantle, Théorème 3.4).
8. **Pic étroit contre plateau large, à masse comparable.** Les tempérages parallèle et simulé mélangent torpidement, et les diagnostics ne le voient pas (Woodard et al., Corollaire 3.2 et exemple 4.1).
9. **Mutation forte.** Le plateau large l'emporte sur le pic haut, sur 12 paires d'organismes numériques sur 40 (Wilke et al. 2001, résumé seulement). Le seuil d'erreur dépend du paysage et n'existe pas s'il y a des génotypes létaux (Wilke 2005, p. 6). Les algorithmes efficaces trouvent les régions denses, non les solutions isolées (Baldassi et al., p. 4 ; physique, non démontré).
10. **Là où rien d'efficace n'est connu.** Au-delà de x* dans le modèle d'énergie aléatoire continu, en tout algorithme. Dans les phases à recouvrement à trou, pour les classes stables seulement. Dans la phase difficile des cibles plantées, conjecturalement.

## Non vérifié

- Jansen et Wegener 2005 : PDF original non trouvé en accès libre ; énoncé lu par la synthèse de Sudholt seulement.
- Lässig et Sudholt 2010 et 2013 : originaux non lus (pas de dépôt ouvert trouvé ; copie sur un domaine miroir non officiel non prise) ; énoncés par la synthèse de Sudholt seulement.
- Dang et al. 2016 (GECCO) : non lu ; seule la version de la revue, 2018, a été lue.
- Wilke et al. 2001 (Nature) : texte intégral sous mur payant ; résumé de PubMed seulement.
- Weissman et al. 2009 : lu sur le XML de PubMed Central, sans numéro de page de la revue ; aucun PDF obtenu (le PDF d'Europe PMC a renvoyé du HTML).
- Gamarnik : la version arXiv a été lue, pas la pagination de PNAS. Zdeborová et Krzakala, Baldassi : idem pour la pagination des revues.
- Oliveto et al. : le numéro imprimé de la revue n'est pas porté dans le fichier ; seules les pages du fichier sont données.
- La correspondance entre les numéros de théorème de la synthèse de Sudholt et ceux des articles originaux est rapportée telle que la synthèse la donne.
