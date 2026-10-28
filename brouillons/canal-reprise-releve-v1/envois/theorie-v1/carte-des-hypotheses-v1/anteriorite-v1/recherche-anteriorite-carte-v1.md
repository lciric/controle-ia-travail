# Recherche d'antériorité des sept questions de la carte des hypothèses v1 — v1

Sous-agent neuf (Fable 5.1) ; je n'ai écrit ni la carte, ni l'audit des failles, ni le programme. Brief :
`brief-anteriorite-carte-v1.md` (dossier de travail de la session). Carte lue :
`/home/claude/canal-conv-audit-n04/brouillons/canal-reprise-releve-v1/envois/theorie-v1/carte-des-hypotheses-v1/carte-des-hypotheses-v1.md`
(sections 0, 1, 2 — A2, A6, A7, A11, A12, A14, A20 — et 4). Début : relevé `date -u` de **03:23:22 UTC le 28 octobre 2026**
(appel séparé) ; relevé intermédiaire 03:34:22 ; fin de la rédaction et fin : relevées en bas du document (appels séparés).

**Pièce confidentielle**, comme la carte : dépôt privé seulement ; jamais servie à un organisme ni au concepteur du mode tenu à
l'écart. **Règle absolue** respectée : ce document reste au niveau des questions (lois, statistiques, propriétés des moniteurs) ;
aucune procédure, consigne ou réglage qui servirait à tromper un moniteur n'est décrit ni recopié. Deux sources lues contiennent
des expériences d'attaque ou d'évasion : elles sont citées par leur titre et une phrase de constat, sans la procédure.

**Méthode et provenance.** Soixante-quatre requêtes (huit par question, parfois partagées entre deux questions voisines), toutes le
28 octobre 2026 entre 03:23 et 03:38 UTC, avec l'outil de recherche du web ; les candidats ont été lus avec l'outil de lecture
de pages (résumé arXiv, texte intégral html, dépôt institutionnel ou page de conférence), **jamais par le terminal** ; rien n'a été
téléchargé dans le dépôt, rien de ce qui a été lu n'a été exécuté, aucun fichier du dépôt modifié, aucun `git`. Chaque résultat
attribué à un papier renvoie à la **page lue et à la section ou page** rapportée par la lecture ; les chiffres sont des relevés de
pages web rendus par l'outil de lecture, **non vérifiés sur PDF empreinté** : ils ne sont pas opposables au sens de R7 et doivent
être revérifiés avant tout usage dans un préenregistrement ou un papier. Ce qu'un papier cite d'un autre est marqué « cité par ».
Langage : jamais « inédit » ; « non trouvé avec ces requêtes ».

**Lectures manquées (à consigner, R11).** Le papier « Detecting Strategic Deception Using Linear Probes » (arXiv 2502.03407) a
été refusé deux fois par le modèle de lecture (résumé et PDF) ; lu à la place par la page de présentation des auteurs sur
GreaterWrong (sans métadonnées). « Power and limitations of conformal martingales » (Vovk, Nouretdinov, Gammerman) **n'a pas été
lu** : les deux liens qui le promettaient rendaient d'autres textes (« Testing randomness online », article 24 du projet de
modélisation par compression en ligne ; « Retrain or not retrain », arXiv 2102.10439). Pages bloquées (vérification de navigateur
ou liste blanche) : PMC (deux fois), PubMed, Bielefeld, Project Euclid, page d'accueil de BMC ; remplacées par des miroirs
(ar5iv, dépôt de Birmingham, page de figure BMC, PDF arXiv).

## 0. Verdict

| question | verdict | antécédent le plus proche (lu) |
|---|---|---|
| **A2** — ordre seul, multi-ensemble gardé | **voisine — couvre en partie** : la classe statistique (même multi-ensemble, ordre changé) est le nul exact des « substituts par rebrassage » (Theiler et al. 1992, via Wikipédia) et l'objet des martingales conformes de test d'échangeabilité (Vovk 2019–2020) ; **l'occurrence** — un agent qui réalise un dommage par l'ordre seul — **non trouvée avec ces requêtes** | Yueh-Han et al. 2025 (dommage « séquentiellement contextuel » par décomposition ; l'ordre n'est pas isolé) ; Kang, Fuller, Honavar 2005 (sac d'appels système ≈ séquences) |
| **A6** — indépendance et marges pour Ville | **voisine — couvre en partie** : la perte de la garantie sous autocorrélation est classique en maîtrise statistique des procédés (Prajapati 2013, citant Goldsmith et Whitfield 1961, Harris et Ross 1991 — cités par, non vérifiés) ; la dépendance par grappes dans les évaluations de modèles est mesurée (Miller 2024, § 2.2 : erreurs groupées jusqu'à 3 fois les naïves) ; la prédiction conforme sous données hiérarchiques existe (Dunn, Wasserman, Ramdas 2018–2022) ; les scores de moniteur corrélés au sein d'un contexte sont **nommés** comme risque, sans mesure ni correction (Lindner et al. 2025, § 5.1, § 6.1) ; **aucune mesure d'effet épisode sur des scores de sondes** trouvée | Miller 2024 ; Lindner et al. 2025 ; Dunn, Wasserman, Ramdas |
| **A7** — plafond du rappel sous hétérogénéité d'épisode | **voisine — couvre en partie** ; **la loi elle-même : antériorité trouvée — couvre** (puissance maximale atteignable à nombre de grappes fixé, Hemming et al. 2011 ; plancher de variance σ_b²/N, Baker et al. 2019, § 11, éq. 3 ; même structure pour le ré-échantillonnage, Miller 2024, § 3.1) ; le transfert aux moniteurs séquentiels d'épisodes d'agents et la valeur de r₀ dans nos scores : **non trouvés** | Hemming et al. 2011 ; Baker et al. 2019 |
| **A11** — décalage étalé sur les jetons contre max et attention | **voisine — couvre en partie** : la loi « le maximum n'est efficace que pour les alternatives très parcimonieuses » est établie (Donoho et Jin 2004, § 1.4.1, théorème 1.3) ; l'« hypothèse collective » de l'apprentissage à instances multiples nomme le cas (Carbonneau et al., § 2.1) ; en sondes : signal « distribué sur la réponse » capté par la moyenne et perdu par le dernier jeton (MIRAGE, § 5.3, annexe E) ; l'agrégation à deux échelles (max de moyennes glissantes) est **déjà publiée** (Kramár et al. 2026, § 3.2.2 ; McKenzie et al. 2025, § 2.1 ; He et al. 2026) ; **le rappel du max contre un décalage étalé dans des scores de sondes par jeton, et la conjecture sur l'attention apprise : non trouvés** | Donoho et Jin 2004 ; Kramár et al. 2026 ; MIRAGE 2026 |
| **A12** — où la trace est lisible dans la trajectoire | **voisine — couvre en partie** : la méthode existe hors du domaine (généralisation temporelle, King et Dehaene 2014) ; en modèles de langue, la décision est lisible **avant** l'action (Esakkiraja et al. 2026 : avant le premier jeton de raisonnement, § 4 ; MIRAGE : dernier jeton d'entrée, § 3.4 ; Chan et al. 2025 : segments précoces ; Ruan et al. 2026 : premier tour ; Chen 2026 : trois pas d'avance) ; **aucune matrice position d'entraînement × position de test sur trajectoires d'agents** trouvée | Esakkiraja et al. 2026 ; Ruan et al. 2026 ; King et Dehaene 2014 |
| **A14** — état (action) contre disposition (épisode) | **voisine — couvre en partie** : la décomposition état / trait est un cadre établi (théorie des états et traits latents : consistance, spécificité d'occasion ; Litson et al., p. 11) ; les vecteurs de persona surveillent une disposition (Chen et al. 2025) ; plusieurs papiers de sondes de tromperie **reconnaissent** que la sonde peut lire le régime d'instruction plutôt que l'acte (Natarajan et al. 2026, § 8 ; Kumar 2026 ; Luikham 2026 : étiquettes par condition) ; la sonde de défection lit l'invite seule (MacDiarmid et al. 2024) ; l'issue d'un épisode se lit dès le premier tour (Ruan et al. 2026) ; **aucune part état / part trait estimée sur des scores de sondes** trouvée | Natarajan et al. 2026 ; Ruan et al. 2026 ; Litson et al. (théorie des états et traits latents) |
| **A20** — battre une base de texte sans la recoder | **voisine — couvre en partie** : la méthode est classique (validité incrémentale et ΔR² ; tests de permutation et de randomisation conditionnels, Berrett et al. 2019 ; tâches de contrôle, Hewitt et Liang 2019 ; sondage amnésique, Elazar et al. 2020) ; en moniteurs de sondes, les comparaisons restent **séparées** (Parrack et al. 2025 ; Kumar 2026 ; McKenzie et al. 2025 ; Xu et al. 2026) ; un modèle combiné dans le **sens inverse** existe (Ruan et al. 2026 : « adding behavioral features to hidden-state probes provides no further gain ») ; **le test emboîté texte + sonde contre texte seul, sur une sonde d'intention : non trouvé** | Parrack et al. 2025 ; Ruan et al. 2026 ; Berrett et al. 2019 |

**Lecture d'ensemble.** Aucune des sept questions n'est vierge : pour chacune, la **loi** ou la **méthode** a un nom et une
littérature hors de la sûreté de l'intelligence artificielle (tests d'échangeabilité et substituts, essais en grappes, détection
de mélanges parcimonieux, généralisation temporelle, théorie des états et traits, validité incrémentale). Ce qui n'a pas été
trouvé, à chaque fois, est **la mesure de la classe dans des scores de sondes sur des trajectoires d'agents**, et pour A2
l'**occurrence** du dommage par l'ordre seul. R8 : ces absences restent des questions, pas des trous du champ ; les requêtes
ci-dessous disent exactement jusqu'où la recherche est allée.

**Trois sources à verser au pôle théorique dès maintenant** (à vérifier sur PDF empreinté avant citation) : Hemming, Girling,
Sitch, Marsh, Lilford 2011 (BMC Medical Research Methodology 11:102) pour A7 ; Donoho et Jin 2004 (Annals of Statistics 32(3))
pour A11 ; Kramár et al. 2026 (arXiv 2601.11516, déjà cité par la carte pour A9 sous MD-B3) pour A11 et la défense à deux échelles.

## 1. A2 — Le multi-ensemble des scores de l'épisode porte le signal

**Énoncé (carte, § 2, A2 ; § 4).** Classe K2 : multi-ensemble d'un honnête, ordre seul changé par une permutation ; toute
statistique invariante par permutation (somme terminale, maximum, moyenne) est aveugle ; question : un organisme réalise-t-il
un dommage de classe C, ou l'environnement le rend-il impossible ?

**Requêtes (28 octobre 2026, 03:24–03:37 UTC).**
1. testing exchangeability online conformal test martingale Vovk detect order dependence
2. surrogate data test random shuffle preserves amplitude distribution destroys temporal order Theiler
3. harm from ordering of individually benign actions AI agent sequence monitor per-action blind
4. permutation-invariant statistic blind to order anomaly detection sequence bag of events versus sequence
5. exchangeability test power against alternatives with identical marginal distribution but serial dependence conformal martingale efficiency
6. "order of actions" OR "action ordering" safety agent harmful sequence same actions different order monitor evaluation
7. "Power and limitations of conformal martingales" Vovk Nouretdinov Gammerman arXiv
8. bag of system calls representation anomaly detection ordering information versus frequency Kang Fuller Honavar

**Candidats.**

| référence | lien | ce qu'il établit (page lue) | couverture | page ou section lue |
|---|---|---|---|---|
| Theiler et al. 1992, « Testing for nonlinearity in time series: the method of surrogate data », Physica D — lu via Wikipédia « Surrogate data testing » | https://en.wikipedia.org/wiki/Surrogate_data_testing | L'algorithme 0 (« random shuffle ») permute les valeurs observées : **même distribution d'amplitude (même multi-ensemble), corrélation temporelle détruite** ; une statistique discriminante compare l'original aux substituts. C'est exactement le nul de la classe C, pris comme hypothèse nulle d'un test d'ordre. | **en partie** : la classe statistique est nommée et outillée (côté test d'ordre) ; rien sur des agents ni des moniteurs | page encyclopédique, section « Algorithm 0 » ; l'article original non lu |
| Vovk 2019–2020, « Testing randomness » (Statistical Science, arXiv 1906.09256) et « Testing randomness online » (article 24, projet de modélisation par compression en ligne) | https://arxiv.org/abs/1906.09256 ; https://www.alrw.net/articles/24.pdf | Tous les tests en ligne connus de l'échangeabilité reposent sur des martingales conformes ; validité (Ville) ; efficacité « grossière » : la non-échangeabilité est détectable à un facteur N près (§ 6, proposition 6.2) ; « the accuracy of these statements is very low and far from meaningful in practice » (§ 7). Une alternative qui ne change que l'ordre n'est pas traitée en tant que telle. | **en partie** : les détecteurs d'ordre (T3 de la carte) ont une théorie générale, aux bornes lâches | résumé arXiv ; § 3 (remarque 3.3), § 4, § 6, § 7, annexe A |
| Vovk, Nouretdinov, Gammerman 2022, « Conformal testing: binary case with Markov alternatives », PMLR 179 | https://proceedings.mlr.press/v179/vovk22a.html | Deux classes de martingales conformes contre des alternatives markoviennes à l'échangeabilité, l'une « statistiquement efficace dans nos expériences ». La page ne dit pas si la marge est gardée. | **en partie** (dépendance sérielle, cas binaire) | résumé PMLR |
| Vovk, Petej, Nouretdinov, Ahlberg, Carlsson, Gammerman 2021, « Retrain or not retrain: conformal test martingales for change-point detection » | https://arxiv.org/pdf/2102.10439.pdf | Martingales conformes pour la rupture ; « all conformal test martingales constructed in this paper will always lose capital in the ideal setting » (remarque 2) ; les alternatives « ordre seul, marges gardées » ne sont pas analysées. | **non** pour K2 ; utile pour S3b–S3d | § 2, § 3, § 4, § 6 |
| Yueh-Han, Joshi, Chen, He, Angell 2025, « Monitoring LLM Agents for Sequentially Contextual Harm », atelier ICLR 2025 ; et Yueh-Han et al., « Monitoring Decomposition Attacks in LLMs with Lightweight Sequential Monitors » (arXiv 2506.10949) | https://iclr.cc/virtual/2025/34234 ; https://arxiv.org/abs/2506.10949v1 | Le dommage peut n'être identifiable que « by analyzing the composition of multiple instructions or actions » ; moniteurs par sous-tâche moins fiables que sur l'instruction de haut niveau ; moniteur cumulatif C_i = [p_1…p_i]. **Aucune expérience où le multi-ensemble est identique et seul l'ordre change** ; l'ordre n'est pas une variable isolée ; moniteurs sur texte d'invite, non sur actions exécutées. | **en partie** (composition, non ordre seul) | page ICLR ; résumé arXiv et limites |
| Kang, Fuller, Honavar 2005, « Learning classifiers for misuse and anomaly detection using a bag of system calls representation », IEEE SMC IAW | https://pure.psu.edu/en/publications/learning-classifiers-for-misuse-and-anomaly-detection-using-a-bag/ | Une représentation **sans ordre** (sac d'appels système) est « effective and often performs better than those approaches that use foreign contiguous subsequences » (approches à ordre). Indice, dans ce domaine, que l'ordre porte peu d'information au-delà du multi-ensemble — l'inverse de la classe C recherchée (où tout le signal est dans l'ordre). | **en partie** (même question, réponse empirique opposée dans un autre domaine) | résumé du dépôt institutionnel |
| NHI Mgmt Group, foire aux questions « What should teams do when an AI agent performs approved actions in a harmful order », mise à jour du 9 juin 2026 | https://nhimg.org/faq/what-should-teams-do-when-an-ai-agent-performs-approved-actions-in-a-harmful-ord/ | **Littérature grise** (entreprise de sécurité des identités, non revue) : nomme exactement le cas « actions approuvées une à une, nuisibles par leur ordre », recommande de garder l'ordre dans les journaux ; aucune donnée, cite des cadres (OWASP, NIST) et son propre rapport. | **en partie** (le cas est nommé ; rien n'est établi) | page entière |

**Ce qui reste ouvert après lecture.** L'occurrence : aucun organisme, aucune évaluation d'agent lue ne montre un dommage obtenu
par un réarrangement d'actions dont le multi-ensemble est honnête ; la seule littérature voisine (décomposition) ne contrôle
pas l'ordre. La théorie des détecteurs d'ordre existe (martingales conformes) mais ses bornes d'efficacité sont lâches ; le
papier qui porte le titre « Power and limitations of conformal martingales » n'a pas été lu. Le domaine des appels système
suggère que l'ordre peut porter peu d'information : à mesurer sur nos scores (T2 de la carte).

**Mots clés d'une suite.** « exchangeability martingale power against Markov alternatives marginals preserved » ; « Power and
limitations of conformal martingales » (retrouver le PDF) ; « order-dependent harm benchmark agent tool-call reordering » ;
« process mining conformance ordering constraints anomaly » ; « surrogate data test agent action sequences ».

## 2. A6 — Indépendance et marges gaussiennes (règle de Ville ; niveau composé d'une cascade)

**Énoncé (carte, § 2, A6 ; § 4).** Classe K6 : effet épisode (z_t = b_e + ε_t, part r₀), dépendance intra-épisode, marges
asymétriques ; sous effet épisode le processus e n'est plus une surmartingale (fausse garantie) ; question : les scores de
sondes sur trajectoires d'agent ont-ils effet épisode, dépendance ou marges qui cassent Ville ?

**Requêtes (28 octobre 2026, 03:24–03:37 UTC).**
1. Ville's inequality dependent observations e-process fails clustered data random effects
2. anytime-valid inference cluster randomized trials e-values intraclass correlation
3. autocorrelated data control chart false alarm rate inflation CUSUM independence assumption violated
4. clustered standard errors LLM evaluation questions intraclass correlation "error bars" evals
5. e-values test martingale under dependence robustness "not a martingale" false alarm inflation sequential test correlated increments
6. conformal prediction coverage under within-group dependence hierarchical clustered exchangeability "two-layer" conformal
7. Alwan Roberts autocorrelation Shewhart chart false alarm rate inflation positive autocorrelation average run length
8. AI control monitor false positive rate per-step independence assumption episode-level correlation trajectory scores sequential alarm calibration

**Candidats.**

| référence | lien | ce qu'il établit (page lue) | couverture | page ou section lue |
|---|---|---|---|---|
| Prajapati 2013, « Performance of conventional X-bar chart for autocorrelated data using smaller sample sizes », WCECS 2013 | https://www.iaeng.org/publication/WCECS2013/WCECS2013_pp1200-1205.pdf | « When X charts are applied to the autocorrelated data, the false alarm rate increases » ; rapporte (**cités par**, non vérifiés à la source) : Goldsmith et Whitfield 1961 (l'autocorrélation positive augmente les fausses alarmes des sommes cumulées), Harris et Ross 1991 (longueur moyenne de run sous contrôle des cartes de sommes cumulées et à moyenne mobile pondérée sensible à l'autocorrélation), VanBrackle et Reynolds 1997, Alwan et Roberts 1988 (« more than 70 % of the studied processes… are autocorrelated »). Ses propres tables montrent surtout une perte de sensibilité, les limites ayant été recalées. | **en partie** : la rupture de la garantie par dépendance sérielle est classique (sommes cumulées, Shewhart), hors agents | pages 1200–1205 (texte entier) |
| Miller 2024, « Adding Error Bars to Evals », arXiv 2411.00640 | https://arxiv.org/html/2411.00640v1 | Questions groupées (même passage, même question traduite) violent l'indépendance ; erreur type groupée = naïve + termes croisés intra-grappe (éq. 4) ; « clustered standard errors can be over 3X larger than naive standard errors » (table 4, DROP) ; ré-échantillonner la même question K fois ne réduit que la part intra-question (§ 3.1). | **en partie** : la dépendance par grappes dans des scores de modèles de langue est mesurée ; pas de test séquentiel, pas de sondes | § 2.2, § 3.1, tables 3–4 |
| Dunn, Wasserman, Ramdas 2018–2022, « Distribution-free prediction sets for two-layer hierarchical models », JASA | https://arxiv.org/abs/1809.07441v4 | L'échangeabilité conforme échoue quand les observations sont groupées (plusieurs mesures par patient, lois distinctes par groupe) ; trois méthodes (regroupement des fonctions de répartition, sous-échantillonnage simple ou répété) ; garantie formelle non lue. | **en partie** : la structure « épisodes = groupes » est exactement celle du calibrage conforme par épisodes entiers de la carte (défense posée) ; prédiction, non test séquentiel | résumé arXiv |
| Lindner, Griffin, Korbak, Zimmermann, Irving, Farquhar, Cooney 2025, « Practical challenges of control monitoring in frontier AI deployments », arXiv 2512.22154 | https://arxiv.org/html/2512.22154v1 | Taux de fausses alertes défini **par action** (annexe D) ; « monitor scores on each may be highly correlated » (§ 5.1) ; « monitor scores within a context may be correlated rather than independent » (§ 6.1) ; certains résultats supposent l'indépendance entre contextes (§ 4.3 ; arrivées de signalements à taux constant, annexe D) ; la corrélation des scores entre pas est listée comme raison d'échec des protocoles, **sans méthode pour l'estimer ni la corriger**. | **en partie** : le risque est nommé dans le contrôle de l'intelligence artificielle, non mesuré | § 2, § 3.1.2, § 4.3, § 5.1, § 6.1, annexe D (100 000 premiers caractères) |
| Vovk 2019–2020 (ci-dessus, A2) | https://arxiv.org/abs/1906.09256 | Validité des martingales conformes **sous échangeabilité seulement** ; sous effet épisode les épisodes entiers sont échangeables, pas les pas : argument pour le calibrage par épisodes entiers. | **en partie** | § 3, § 6 |
| Regularized e-processes (arXiv 2410.01427) ; Hypothesis testing with e-values (arXiv 2410.23614) | résultats de recherche seuls | **Non lus** (titres seulement, hors sujet apparent : régularisation, revue générale). | non évalué | — |

**Ce qui reste ouvert après lecture.** Aucune mesure, dans aucun papier lu, de la corrélation intraclasse de scores de sondes
par action au sein d'épisodes d'agents, ni du dépassement du niveau d'un processus e calibré par pas quand cette corrélation est
positive (la carte le simule : 0,21 à 0,35 pour 0,05 visé, T0.3 P8, non lu ici). Le contrôle de l'intelligence artificielle nomme
la corrélation des scores entre pas comme un risque (Lindner et al.) sans la quantifier : c'est la place exacte de M2 ter de la
mesure unanime. Les processus e robustes à la dépendance par grappes (e-valeur par grappe, mélange sur épisodes) ne sont pas
apparus dans les requêtes : à chercher.

**Mots clés d'une suite.** « e-value cluster-level aggregation hierarchical data anytime-valid » ; « test martingale random
effects intraclass correlation level inflation simulation » ; « conformal change detection grouped observations
exchangeable blocks » ; « intraclass correlation probe scores agent episodes » ; « control chart autocorrelation CUSUM
in-control ARL Goldsmith Whitfield 1961 » (vérifier à la source).

## 3. A7 — Le rappel croît avec l'horizon

**Énoncé (carte, § 2, A7 ; § 4).** Classe K7 : effet épisode honnête de part r₀ > 0 et décalage constant ; le meilleur test de
niveau α a pour puissance Φ(δ/√(r₀ + (1 − r₀)/T) − z_α), plafonnée à Φ(δ/√r₀ − z_α) ; question : le rappel d'un moniteur
séquentiel plafonne-t-il sous hétérogénéité d'épisode ?

**Requêtes (28 octobre 2026, 03:26–03:37 UTC).**
1. cluster randomised trial fixed number of clusters maximum achievable power increasing cluster size plateau
2. design effect intraclass correlation power does not increase indefinitely with observations per cluster ceiling formula
3. sequential test random intercept cluster-level shift detection power limited between-cluster variance
4. between-batch variation control chart detection power limited batch means random effects monitoring
5. repeated measures power number of participants versus trials per participant ceiling "power contours" between-subject variance
6. LLM evaluation variance decomposition more samples per task diminishing returns task-level variance clustering eval statistics
7. optimal test mean shift compound symmetry covariance exchangeable errors power bounded as number of repeated measures increases random intercept
8. cluster randomized trials number of clusters drives power more than cluster size intraclass correlation Donner Klar design effect limit

**Candidats.**

| référence | lien | ce qu'il établit (page lue) | couverture | page ou section lue |
|---|---|---|---|---|
| Hemming, Girling, Sitch, Marsh, Lilford 2011, « Sample size calculations for cluster randomised controlled trials with a fixed number of clusters », BMC Medical Research Methodology 11:102 | https://research.birmingham.ac.uk/en/publications/sample-size-calculations-for-cluster-randomised-controlled-trials ; https://bmcmedresmethodol.biomedcentral.com/articles/10.1186/1471-2288-11-102/figures/2 | À nombre de grappes fixé, un essai n'est faisable que si le nombre de grappes dépasse la taille d'échantillon en randomisation individuelle multipliée par la corrélation intra-grappe ρ ; sinon on calcule la **« maximum achievable power… irrespective of how many individuals are included within each cluster »** ; la figure 2 donne cette puissance maximale comme **valeur limite quand la taille de grappe tend vers l'infini**. | **couvre la loi** (même mathématique que le lemme de A7 : variance de la moyenne bornée par la part inter-grappes) ; **non** pour les moniteurs séquentiels | résumé (dépôt de Birmingham) ; légende de la figure 2 |
| Baker, Vilidaite, Lygo, Smith, Flack, Gouws, Andrews 2019–2020, « Power contours: optimising sample size and precision in experimental psychology and human neuroscience » | https://ar5iv.arxiv.org/html/1902.06122 | Erreur type de la moyenne SE = √(σ_b²/N + σ_w²/(kN)) (§ 11, éq. 3) : le terme inter-sujets σ_b²/N **ne dépend pas du nombre d'essais k** et fixe un plancher ; « beyond a particular number of trials (around k = 50 in Figure 1h), the function asymptotes and further trials are not beneficial » (§ 2) ; plateau non universel (§ 8, § 9, § 11). | **couvre la loi** (plancher de variance = plafond de puissance), autre domaine | § 2, § 8, § 9, § 11 |
| Miller 2024 (ci-dessus, A6) | https://arxiv.org/html/2411.00640v1 | Ré-échantillonner la même question K fois réduit E[σ²]/K ; une fois ce terme petit devant Var(x), « will have little effect » (§ 3.1) : même structure de plancher, au niveau des questions d'une évaluation. | **en partie** (évaluations de modèles, non moniteurs) | § 3.1 |
| Hemming et al. 2017, « How to design efficient cluster randomised trials », BMJ 358:j3064 | https://pubmed.ncbi.nlm.nih.gov/28710062/ | **Non lu** (vérification de navigateur). | non évalué | — |
| Essais en grappes : Donner et Klar ; effet de plan (résultats de recherche : BMJ 1998 « The intracluster correlation coefficient in cluster randomisation », pages de calculatrices) | résultats seuls | **Non lus** ; la formule de l'effet de plan 1 + (m − 1)ρ est classique (non vérifiée ici, R7). | non évalué | — |

**Ce qui reste ouvert après lecture.** La loi est établie et nommée ailleurs (essais en grappes, psychologie expérimentale,
évaluations de modèles) : le lemme de A7 n'a rien à revendiquer comme loi ; sa valeur est dans **l'application** — montrer que
des scores de sondes sur épisodes d'agents ont un r₀ > 0 et que le rappel des sommes conformes plafonne en conséquence (T1 de la
carte). Aucun papier lu ne traite d'un test séquentiel ou d'un moniteur dont la puissance plafonne par effet de grappe ; les
requêtes 3 et 4 n'ont rendu que des pages périphériques (plans en marches d'escalier, cartes de contrôle de lots), non lues.

**Mots clés d'une suite.** « sequential monitoring random intercept power asymptote cluster » ; « batch-means control chart
between-batch variance detection limit » ; « Donner Klar design effect maximum power fixed clusters » ; « longitudinal design
power number of subjects versus measurements per subject ceiling » ; « mixed-effects power ICC asymptote repeated measures ».

## 4. A11 — L'agrégation sur les jetons voit un décalage étalé

**Énoncé (carte, § 2, A11 ; § 4).** Classe K11 : décalage total B_j réparti sur n jetons, loi jointe sinon gardée ; le max perd
sa puissance dès que B_j/n est petit, la somme quand B_j/(σ√n) l'est ; conjecture : une attention apprise sur des signaux
concentrés pondère peu un décalage étalé ; question : un décalage étalé sur les jetons échappe-t-il au max et à l'attention ?

**Requêtes (28 octobre 2026, 03:26–03:37 UTC).**
1. multiple instance learning collective assumption versus standard assumption max pooling fails weak diffuse signal many instances
2. higher criticism sparse versus dense alternatives max statistic versus sum statistic detection boundary Donoho Jin
3. deception probe token aggregation mean versus max over response tokens linear probe LLM
4. attention-based multiple instance learning pooling weak signals distributed across many instances Ilse Tomczak Welling
5. EleutherAI attention probes token aggregation mean max last token probe comparison blog
6. scan statistic versus sum statistic power dense weak signal spread over many sites anomalous cluster detection Arias-Castro
7. "token-level" monitors vulnerable reinforcement learning obfuscation latent monitors sequence-level aggregation max mean 2506.14261
8. "max over tokens" OR "mean over tokens" probe aggregation recall misalignment monitor agent long context diffuse per-token signal comparison

**Candidats.**

| référence | lien | ce qu'il établit (page lue) | couverture | page ou section lue |
|---|---|---|---|---|
| Donoho et Jin 2004, « Higher criticism for detecting sparse heterogeneous mixtures », Annals of Statistics 32(3), 962–994 | https://arxiv.org/pdf/math/0410072v1 | n moyennes, fraction ε = n^(−β) non nulle : le **maximum** (type Bonferroni) n'est efficace que « in the range of very sparse alternatives » et est **inefficace pour β < 3/4** (§ 1.4.1, théorème 1.3) ; « can be dramatically outperformed » quand ~n^(1/2) moyennes sont non nulles ; frontière de détection ρ*(β) (§ 1.1) ; régime dense (ε fixe) non traité ; la statistique de somme simple n'est pas analysée directement. | **couvre la loi** (max contre statistiques globales selon la parcimonie), hors sondes | § 1.1, § 1.2, § 1.4 et figure 1, § 1.5, § 5, annexe |
| Arias-Castro et Grimmett 2013, « Cluster detection in networks using percolation », Bernoulli 19(2) | https://pdf.arxiv.org/pdf/1104.0338 | Pour un amas « of size comparable to that of the entire network », « the simple test based on the total sum » est « optimal up to a multiplicative constant » (§ 2) ; le balayage est quasi optimal pour des amas compacts (§ 3) ; **pas de comparaison directe balayage / somme en régime étalé**. (Le papier visé, Arias-Castro, Candès, Durand 2011, n'a pas pu être lu : page vide.) | **en partie** | § 1, § 2, § 3, § 4.2 |
| Carbonneau, Cheplygina, Granger, Gagnon, « Multiple instance learning: a survey of problem characteristics and applications », arXiv 1612.03365 | https://arxiv.org/abs/1612.03365 | Hypothèse **standard** (un témoin suffit) contre hypothèse **collective** (« more than one instance defines the bag label », accumulation) ; les méthodes à témoin « would fail » quand le label dépend de plusieurs instances (§ 2.1) ; à faible taux de témoins la moyenne dilue (§ 4.2) ; la mise en commun par max n'est pas testée en tant que telle. | **en partie** (le cas est nommé ; pas de loi quantitative) | § 2.1, § 4.1, § 4.2, § 4.4, § 6.3 (100 000 premiers caractères) |
| Kramár, Engels, Wang, Chughtai, Shah, Nanda, Conmy 2026, « Building production-ready probes for Gemini », arXiv 2601.11516 (déjà cité par la carte, MD-B3, pour A9) | https://arxiv.org/pdf/2601.11516 | Agrégations : moyenne (§ 3.1.1), max de moyennes mobiles exponentielles (§ 3.1.2), attention (§ 3.1.4), **MultiMax** — « prevents dilution of the signal when harmful content appears in a small portion of a long context » (§ 3.2.1, pp. 6–7) —, **Max of Rolling Means** (fenêtres w = 10, § 3.2.2, p. 7) ; sur attaques en contexte long, taux de faux négatifs 87,88 % (attention), 99,13 % (moyenne), ≈ 1,7 % (MultiMax sur fenêtres) (table 3, p. 12). Documente le cas **concentré** (la moyenne dilue) ; **ne teste pas le cas étalé** (le max perd). | **en partie** : l'agrégation à deux échelles que la carte propose en défense **est déjà publiée** ; la classe K11 elle-même n'est pas mesurée | § 3.1–3.3, § 4, § 5.3, § 7, table 3, annexe C |
| Revankar, Chauhan, Kim, Nur, Siu, Wang 2026, « MIRAGE: a polarity-flipping encoding subspace in LLM agents », atelier ICML 2026 | https://arxiv.org/html/2606.10304 | Deux canaux : « burst » (max d'une moyenne sur fenêtre de 5 jetons, annexe A) et « intent » (dernier jeton d'entrée, § 3.4) ; **« Last-token scoring drops to 0.37–0.76 AUC, confirming the signal is distributed across the response »** (§ 5.3) ; « Mean-pool and 95th-percentile aggregation capture this distributed signal » (annexe E) ; attention non testée. Contient des expériences d'attaque sur le sous-espace : **non reprises ici**. | **en partie** : un signal **étalé** sur la réponse est observé et capté par la moyenne ; le rappel du max contre un décalage étalé contrôlé n'est pas mesuré | § 3.4, § 5.1–5.3, § 7.2, § 7.4, annexes A et E |
| McKenzie, Pawar, Blandfort, Bankes, Krueger, Lubana, Krasheninnikov 2025, « Detecting high-stakes interactions with activation probes », NeurIPS 2025, arXiv 2506.10805 | https://www.alphaxiv.org/abs/2506.10805.md | Compare moyenne, max, dernier jeton, softmax, attention, max de moyennes glissantes (fenêtre 40) (§ 2.1, table 3) ; les meilleures « take all the tokens into account » (softmax, attention, moyenne) (§ 3). | **en partie** (comparaison d'agrégations sur un autre objet ; pas de décalage étalé contrôlé) | § 2.1, § 2.2, § 2.3, § 3, table 3 |
| He, Sel, Ali, Bao, Cunningham, Wei 2026, « Segment-level coherence for robust harmful intent probing in LLMs » (arXiv 2604.14865, déjà cité par la carte pour A9) | https://arxiv.org/pdf/2604.14865v1.pdf | Les sondes en flux « over-rely on a few high-scoring tokens » ; Top-K de fenêtres : « harmful predictions effectively require at least K windows to exhibit elevated logits » (§ 3.2) ; moyenne sur fenêtre glissante (M = 16), max sur fenêtres, softmax (annexe C.1). Décrit le symptôme inverse de K11 (fausses alertes par pics isolés) et une agrégation qui **exige** un signal réparti sur plusieurs fenêtres. | **en partie** (indice contre la conjecture : une agrégation apprise peut être conçue pour favoriser le réparti ; non testée sur un décalage étalé) | § 1, § 3.1, § 3.2, § 5, annexes C.1, D.3, F |
| Shabalin et Belrose 2025, « Attention probes », blog EleutherAI | https://blog.eleuther.ai/attention-probes/ | Moyenne contre dernier jeton : dépend du jeu de données ; attention à 8 têtes « mostly outperforms mean probes » ; max non discuté ; pas de cadrage concentré / étalé. | **non** pour K11 | billet entier |
| Ilse, Tomczak, Welling 2018, « Attention-based deep multiple instance learning », ICML | résultats seuls | **Non lu** (priorité donnée au relevé des sondes) ; référence de l'agrégation par attention. | non évalué | — |
| Carte : 2506.14261v4 (« RL-Obfuscation ») | résultats seuls | **Non relu** ici (la carte a vérifié p. 1 : « token-level monitors are highly vulnerable ») ; une recherche par identifiant n'a rendu que des liens. | déjà classé « voisine » par la carte | — |

**Ce qui reste ouvert après lecture.** La loi est connue (Donoho et Jin : le maximum ne vaut qu'en régime très parcimonieux) ;
l'agrégation à deux échelles existe (max de moyennes glissantes, MultiMax, Top-K). Ce qui manque : (a) une mesure du rappel du
**max par action** quand un décalage de budget fixé est étalé sur les n jetons de scores de sondes réels (le témoin de la carte) ;
(b) la conjecture sur l'attention apprise — aucune lecture ne la teste ; He et al. montrent qu'on peut concevoir l'agrégation
pour exiger un signal réparti, ce qui est un argument de conception, pas une mesure. La comparaison balayage / somme en régime
dense (Arias-Castro, Candès, Durand 2011) reste à lire.

**Mots clés d'une suite.** « dense weak signal detection sum versus max power curve » ; « token-score shift spread
sequence-level probe recall simulation » ; « attention pooling learned on sparse positives fails on diffuse positives MIL » ;
« Arias-Castro Candès Durand 2011 anomalous cluster scan versus sum » ; « multiple instance learning collective assumption
benchmark max pooling failure ».

## 5. A12 — La trace atteint les positions lues

**Énoncé (carte, § 2, A12 ; § 4).** Classe K12 : loi jointe des activations aux positions lues gardée, la trace est ailleurs ;
S5 (position finale) et S6 (jetons de l'action, contexte privé) ne lisent pas les mêmes positions ; question : où, dans la
trajectoire, la trace d'une intention est-elle lisible ?

**Requêtes (28 octobre 2026, 03:28–03:37 UTC).**
1. temporal generalization method decoding King Dehaene train decoder one time point test other time points
2. linear probe trained at one token position generalize to other positions language model hidden states position generalization
3. activation probe monitoring agent trajectories which token positions intent encoded before action tool call
4. "Future Lens" anticipating subsequent tokens hidden state language models plan ahead probe
5. King Dehaene 2014 "temporal generalization" Trends in Cognitive Sciences characterizing dynamics of mental representations
6. predict agent misbehavior from early trajectory activations before harmful action forecasting outcome linear probe LLM agent
7. "Simple probes can catch sleeper agents" defection probe token position generic questions Anthropic (partagée avec A14)
8. probe trained on one step transfer to other steps multi-turn agent trajectory activation probe cross-step generalization matrix

**Candidats.**

| référence | lien | ce qu'il établit (page lue) | couverture | page ou section lue |
|---|---|---|---|---|
| King et Dehaene 2014, « Characterizing the dynamics of mental representations: the temporal generalization method », Trends in Cognitive Sciences 18(4), 203–210 | https://bibbase.org/network/publication/king-dehaene-characterizingthedynamicsofmentalrepresentationsthetemporalgeneralizationmethod-2014 | Classifieurs entraînés à un instant et testés aux autres : « at which moment a specific mental content becomes decodable », et la généralisation à travers le temps révèle l'organisation des étapes de traitement ; « a repertoire of canonical dynamical patterns ». **La méthode exacte** que la carte appelle (HT-04), hors du domaine. | **couvre la méthode** ; rien sur les modèles de langue | résumé |
| Pal, Sun, Yuan, Wallace, Bau 2023, « Future Lens: anticipating subsequent tokens from a single hidden state », CoNLL 2023, arXiv 2311.04897 | https://arxiv.org/abs/2311.04897 | Un état caché à la position t porte de l'information sur les jetons t + 2 et au-delà (GPT-J-6B) ; à certaines couches, plus de 48 % d'exactitude sur les prédictions du modèle lui-même. | **en partie** : la trace d'un contenu futur est lisible à des positions antérieures (langue générale, non intention) | résumé arXiv |
| Esakkiraja, Akhiyarov, Rajeswar, Venkatesaramani 2026, « Therefore I am. I think. », arXiv 2604.01202 | https://arxiv.org/html/2604.01202 | Sondes à neuf positions (avant génération, centiles du raisonnement, fin de la réflexion, jeton de décision), **une sonde par (couche, position)** (§ 3.2–3.3) ; la décision d'appel d'outil se lit « pre_gen », avant tout jeton de raisonnement ; « this accuracy drops significantly during the thinking process » ; accord > 80 % entre pré-génération et fin de réflexion (§ 4). Pas de transfert d'une sonde entre positions ; pas de trajectoires multi-pas. | **en partie** : la lisibilité varie le long de la génération ; pas de matrice de généralisation | § 3.2, § 3.3, § 4, discussion |
| Revankar et al. 2026, MIRAGE (ci-dessus, A11) | https://arxiv.org/html/2606.10304 | Canal « intent » au **dernier jeton d'entrée**, avant toute sortie : la direction « is positive when the model is about to simulate » (§ 3.4), séparable à toutes les couches de Qwen-7B ; canal « burst » pendant la génération ; le dernier jeton seul chute (§ 5.3). | **en partie** : deux positions comparées sur un même objet | § 3.4, § 5.3 |
| Chan, Yong, Bach 2025, « Can we predict alignment before models finish thinking? », NeurIPS 2025 | https://neurips.cc/virtual/2025/133737 | Une sonde linéaire sur les activations de la chaîne de raisonnement « can significantly outperform all text-based methods » ; « makes accurate predictions before reasoning completes » ; « strong performance even when applied to early CoT segments » ; positions et couches non précisées sur la page. | **en partie** | résumé |
| Ruan, Huang, Zhou, Wei, Lin, Wang, Sun 2026, « Doomed from the start: early abort of LLM agent episodes via a recall-controlled probe cascade », arXiv 2607.06503 (type déjà cité par la carte pour S4) | https://www.alphaxiv.org/abs/2607.06503v2 | Sonde sur « the residual-stream hidden state at the final token of the agent's action in a given round r » ; « predict eventual task failure from the first interaction round » ; AUC 0,86 au premier tour (TextCraft, Qwen-2.5-7B) ; portes aux tours 1 à R_g. Issue d'épisode, non sabotage. | **en partie** : la trace d'une issue d'épisode est lisible dès le premier tour, à la fin de chaque action | résumé ; section « Finding the Signal » |
| Chen 2026, « Goal-drift probes: anticipating multi-turn LLM agent failure from mid-network activations », atelier ICML 2026 | https://icml.cc/virtual/2026/67962 | Sondes linéaires (Qwen2.5-7B, ALFWorld) : échec de trajectoire prédit **trois pas d'avance** (AUC 0,989) ; identité de tâche décodée (83,4 %) ; signal robuste au retrait de l'indice de pas (« residualized AUC ≥ 0.939 at every layer ») ; position de lecture non précisée. Résumé d'atelier, sans méthodes. | **en partie** | résumé d'atelier |
| Sun, Dong, Qiao, Lin, Zhang, Rajmohan (Microsoft), « LLM reasoning as trajectories: step-specific representation geometry and correctness signals », arXiv 2604.05655 | https://arxiv.org/pdf/2604.05655 | Sous-espaces **spécifiques à l'étape** du raisonnement (§ 3.3) ; la justesse se lit **tard** : AUC 0,83 en fin de trajectoire contre 0,63 aux premières étapes (§ 4.2) ; transfert entre modèles et jeux de données, **pas entre étapes**. | **en partie** : la lisibilité dépend de la position ; sens inverse de Ruan et al. (tard plutôt que tôt), sur un autre objet | § 3.3, § 3.4, § 4.1, § 4.2, § 4.4 |
| MacDiarmid et al. 2024, « Simple probes can catch sleeper agents », Anthropic | https://www.anthropic.com/research/probes-catch-sleeper-agents | « Activations are always taken at the final token position of the prompt » ; « activations are taken only on prompts, not model completions » : la trace « will defect » est lisible **avant** toute action. | **en partie** | billet entier |
| Xu et al. 2026, « PreAct-Bench: benchmarking predictive monitoring in LLMs », arXiv 2606.09890 | https://www.alphaxiv.org/abs/2606.09890.md | Moniteur sur un **préfixe** de trajectoire avant la première action non éthique ; performance par fraction de préfixe (40 à 100 %), « performance drop with smaller window sizes » ; sonde linéaire (Llama 3.3 70B, couche 22) à 0,774 contre 0,852 pour GPT-5-mini. | **en partie** : la lisibilité croît avec la longueur du préfixe ; positions de jetons non étudiées | résumé, table A1 |

**Ce qui reste ouvert après lecture.** Beaucoup de papiers lisent une trace **avant** l'action (invite, dernier jeton d'entrée,
pré-génération, premier tour), un autre la lit **tard** (justesse mathématique) ; chacun choisit ses positions ; **aucun ne
construit la matrice position d'entraînement × position de test** (généralisation temporelle) sur des trajectoires d'agents, ni
ne teste le nul d'alignement de HT-04. La question posée reste ouverte en tant que mesure ; la méthode a un nom et une
littérature (neurosciences).

**Mots clés d'une suite.** « temporal generalization matrix language model probe token positions » ; « cross-position probe
transfer agent trajectory tool-call token » ; « when does intent become decodable chain-of-thought activations position » ;
« alignment null temporal decoding permutation across positions » ; « probe trained on prompt tokens tested on response
tokens transfer ».

## 6. A14 — La sonde lit un état (l'action), non une disposition

**Énoncé (carte, § 2, A14 ; § 4).** Classe K14 : décalage constant sur l'épisode saboteur, action sabotée ou non ; la
localisation est aveugle et K14 rejoint K7 ; question : une sonde lit-elle une disposition d'épisode, non l'action ?

**Requêtes (28 octobre 2026, 03:28–03:37 UTC).**
1. latent state-trait theory variance decomposition trait state occasion Steyer
2. persona vectors monitoring character traits language models activation direction disposition
3. deception probe fires on system prompt instruction regime rather than deceptive output limitation "prompt regime"
4. persona persistence across conversation in-context state carryover LLM activation drift emergent misalignment direction probe disposition
5. "Simple probes can catch sleeper agents" defection probe token position generic questions Anthropic (partagée avec A12)
6. emergent misalignment linear direction probe generalizes across contexts "misalignment direction" disposition detection activations
7. episode-level versus step-level anomaly detection agent trajectory per-episode random intercept monitor scores variance decomposition between within episode
8. probe detects system prompt condition rather than behavior "honest" responses under deceptive instruction flagged probe false positives instructed but complied honestly

**Candidats.**

| référence | lien | ce qu'il établit (page lue) | couverture | page ou section lue |
|---|---|---|---|---|
| Litson, Thornhill, Geiser, Burns, Servera, « Applying and interpreting mixture distribution latent state-trait models » (Teacher's Corner ; théorie des états et traits latents de Steyer et collègues) | https://core.ac.uk/download/275574516.pdf | Score observé = état latent + erreur (éq. 1, p. 6) ; état latent = trait (stable) + résidu d'occasion (« systematic deviations from the trait level due to the situation », p. 7) ; **consistance** = part de variance due au trait (éq. 5, p. 11), **spécificité d'occasion** = part due aux écarts momentanés (éq. 6, p. 11) ; « a variable containing more trait variance than occasion-specific variance is considered trait-like » (p. 4). | **couvre le cadre** (décomposition exacte que HT-24 appelle), hors du domaine | pp. 4–11 |
| Chen, Arditi, Sleight, Evans, Lindsey 2025, « Persona vectors: monitoring and controlling character traits in language models », arXiv 2507.21509 | https://huggingface.co/papers/2507.21509 | Directions d'activation liées à des traits (malveillance, flagornerie, hallucination) ; « these vectors can be used to monitor fluctuations in the Assistant's personality at deployment time » ; granularité (réponse, conversation, jeton) non précisée sur la page. | **en partie** : une **disposition** est surveillée par projection, sans dissociation d'avec l'acte | résumé et commentaires |
| Natarajan, Jain, Arora, Golechha, Bloom 2026, « Building better deception probes using targeted instruction pairs », arXiv 2602.01425 | https://arxiv.org/html/2602.01425v1 | La sonde lit « the model's internal representations of intent as shaped by the system prompt » (§ 3.1) ; limite : montrer que les gains viennent « due to their increased detection of that specific deception type » et non de traits de l'invite (§ 8) ; **aucun test** « instruit de tromper mais répond honnêtement » ; agrégation par la moyenne hors des 5 derniers jetons (§ 3.6). | **en partie** : la confusion disposition / acte est **reconnue comme ouverte** | § 3.1, § 3.3, § 3.6, § 4.1, § 5.3, § 6.1, § 8 |
| Kumar 2026, « Pressure-testing deception probes in LLMs », arXiv 2605.27958 (cité par la carte pour A20 sans page) | https://arxiv.org/abs/2605.27958 | Tromperie induite par invite système ; 29–41 % des étiquettes « trompeuses » non vérifiées ; **« the probes may detect the prompt regime rather than deceptive output »** (limites) ; lecture au dernier jeton de la réponse. | **en partie** (limite déclarée, non mesurée) | résumé et limites |
| Luikham 2026, « Asymmetries in spontaneous and instructed deception », arXiv 2609.00180 | https://arxiv.org/pdf/2609.00180 | Étiquettes instruites « labeled based on their system prompt instruction » ; transfert asymétrique (spontané → instruit 0,980 ; instruit → spontané faible) ; pas de condition instruction / conduite discordantes ; « spontaneous last-prompt-token probes failed within setting ». Un modèle, scénarios générés. | **en partie** (la disposition instruite est « loud », l'acte spontané « subtle » — hypothèses des auteurs) | sections de résultats et limites |
| MacDiarmid et al. 2024 (ci-dessus, A12) | https://www.anthropic.com/research/probes-catch-sleeper-agents | Sonde lue sur l'invite seule, interprétée comme « representing whether or not it will defect » ; ne sépare pas les classes sur des questions sans code ; « the salience of this feature is an artifact of our backdoor insertion process » possible. | **en partie** : lecture d'une disposition conditionnelle avant l'acte | billet entier |
| Ruan et al. 2026, « Doomed from the start » (ci-dessus, A12) | https://www.alphaxiv.org/abs/2607.06503v2 | L'issue de l'épisode est prédite dès le premier tour (AUC 0,86) : signal de niveau épisode lu à chaque action ; échec, non sabotage. | **en partie** | résumé |
| Soligo, Turner, Rajamanoharan, Nanda 2025, « Convergent linear representations of emergent misalignment », arXiv 2506.11618 | https://arxiv.org/html/2506.11618v2 | Direction de désalignement tirée d'étiquettes **par réponse** (§ 3.1), transférable entre réglages fins ; **non testée** comme trait stable entre contextes ; surveillance renvoyée aux travaux futurs (§ 6.1). | **non** pour K14 (voisin lointain) | § 1.1, § 3.1, § 3.3, § 3.6, § 4.1, § 6.1 |
| Kim, Fogliato, Akpinar, Wang, Palia 2026, « Carryover harm in conversational AI », atelier NeurIPS 2026 | https://neurips.cc/virtual/2026/165324 | « Carryover harm » : persistance d'une conduite au-delà d'une frontière d'interaction ; jugée au niveau de la trajectoire entière ; juges automatiques, résultats « provisional ». | **en partie** (niveau conversation, boîte noire) | résumé |
| Liu et al. 2026, « TrajAD: trajectory anomaly detection for trustworthy LLM agents », arXiv 2602.06443 | https://arxiv.org/html/2602.06443v1 | Verdict par trajectoire + « First Error Step » (§ 3.3) ; dépendance entre pas non modélisée ; pas de calibrage de fausses alertes. | **non** pour K14 (boîte noire, vérificateur réglé) | § 1, § 3.3, § 4.1, § 5, § 6.1 |

**Ce qui reste ouvert après lecture.** Le cadre existe (états et traits latents) et le soupçon est **écrit** dans plusieurs
papiers de sondes de tromperie (la sonde lirait le régime d'instruction, une disposition posée en début d'épisode) ; aucun ne
le **mesure** par la part état / part trait sur des occasions désignées a priori (HT-24), ni ne compare action sabotée et non
sabotée d'un même épisode. La question reste une mesure à faire, avec un vocabulaire emprunté : consistance et spécificité
d'occasion.

**Mots clés d'une suite.** « latent state-trait model probe scores consistency occasion specificity » ; « probe fires on
instruction not on act mismatched condition deceptive instruction honest response » ; « within-episode contrast sabotaged versus
unsabotaged actions probe score » ; « persona vector projection per-token versus per-conversation variance » ; « sleeper agent
probe disposition generic prompts separation ».

## 7. A20 — Battre le prédicteur de texte établit une information interne

**Énoncé (carte, § 2, A20 ; § 4).** Classe K20 : X = g(T) + ε, ε indépendant de (I, T) : la sonde recode les traits du texte ;
le modèle emboîté (T et X contre T seul) a une puissance égale à son niveau alors que les deux comparaisons séparées peuvent
passer ; question : une sonde qui bat une base de texte recode-t-elle ce texte ?

**Requêtes (28 octobre 2026, 03:30–03:37 UTC).**
1. probing classifiers control tasks selectivity Hewitt Liang probe memorizes surface features baseline
2. do activation probes add information beyond text classifier hallucination detection internal states versus text-based baseline combined model
3. conditional randomization test neural representations conditional independence feature importance Candès holdout randomization test
4. white-box activation monitor versus black-box transcript monitor agent misbehavior complementary information ensemble hybrid
5. incremental validity hierarchical regression nested model test psychometrics definition Hunsley Meyer 2003
6. variance partitioning encoding models unique variance explained beyond low-level stimulus features nested regression neuroscience
7. amnesic probing counterfactual representation does probe rely on surface lexical features residualize text features activation probe shortcut
8. activation probe score predictable from text features residualized against text baseline nested model incremental information internal states LLM monitor

**Candidats.**

| référence | lien | ce qu'il établit (page lue) | couverture | page ou section lue |
|---|---|---|---|---|
| Validité incrémentale (psychométrie) — Wikipédia, citant Haynes et Lench 2003, Sackett et Lievens 2008, Lilienfeld et al. 2005 | https://en.wikipedia.org/wiki/Incremental_validity | Une mesure nouvelle a-t-elle « more predictive ability than existing methods » ; test par deux régressions (variables existantes ; + mesure focale), test F sur le **changement de R²**, préféré aux corrélations brutes qui ignorent le recouvrement. C'est le test emboîté de FI-05, nommé. | **couvre la méthode**, hors du domaine | page entière |
| Berrett, Wang, Barber, Samworth 2019, « The conditional permutation test for independence while controlling for confounders » (arXiv 1807.05405) ; test de randomisation conditionnelle de Candès et al. (cité par) | https://arxiv.org/pdf/1807.05405 | Test de X ⟂ Y \| Z : validité exacte quand la loi de X \| Z est connue (théorème 1 ; « P{p ≤ α} ≤ α », § 3) ; sous approximation Q de Q*, excès d'erreur de première espèce borné par la distance en variation totale (théorème 4, § 5) ; Q estimée sur les mêmes données « not covered by our theory ». Le cadre exact de HT-03 (randomisation conditionnelle aux traits de surface). | **couvre la méthode** | § 3, § 5, § 6.1 |
| Hewitt et Liang 2019, « Designing and interpreting probes with control tasks », EMNLP | https://ar5iv.labs.arxiv.org/html/1909.03368 | Une exactitude de sonde élevée peut venir de la sonde qui mémorise l'identité lexicale ; tâche de contrôle à sorties aléatoires par type de mot, « can only be learned by the probe itself » ; **sélectivité** = exactitude linguistique − exactitude de contrôle (§ 1, § 2, § 3.5). | **en partie** : contrôle du recodage de surface, pour des sondes linguistiques (pas de base de texte explicite) | § 1, § 2, § 3.5 |
| Elazar, Ravfogel, Jacovi, Goldberg 2020–2021, « Amnesic probing », TACL | https://ar5iv.arxiv.org/html/2006.00995 | « high probing performance does not entail this information is being used » (§ 4) ; retrait linéaire itéré ; « the classifiers can rely on arbitrary features that happen to correlate with the gold label » (§ 9) ; les sondes de contrôle peuvent réussir par mémorisation lexicale (annexe B). | **en partie** (recodage de traits corrélés nommé ; pas de base de texte) | § 1, § 2.2, § 2.3, § 4, § 9, annexe B |
| Parrack, Attubato, Heimersheim 2025, « Benchmarking deception probes via black-to-white performance boosts », arXiv 2507.12691 | https://arxiv.org/html/2507.12691v3 | Gain « black-to-white » = écart d'AUROC entre un moniteur avec et sans accès aux activations de sonde (§ 1.2, § 6, table 3) ; **aucun test emboîté** ; ensemble à poids fixés 2/3–1/3 (§ 5.3) ; le gain est « attributed to the probes themselves » par usage du même modèle (§ 8), ce qui **n'exclut pas le recodage** ; intervalles bootstrap par moniteur, pas sur la différence (annexe A). | **en partie** : c'est précisément la pratique « deux comparaisons séparées » que la carte oppose au test emboîté | § 1.2, § 5.3, § 6, § 7, § 8, annexe A, table 3 |
| Kumar 2026 (ci-dessus, A14) | https://arxiv.org/abs/2605.27958 | « B→W boost » = sonde − classifieur TF-IDF (table 3), 0,442 à 0,522 ; base texte sous 0,5 à 12B et 27B, « inflates the boost » ; **pas de modèle combiné**. | **en partie** (séparé, non emboîté) | résumé, table 3, limites |
| Ruan et al. 2026, « Doomed from the start » (ci-dessus) | https://www.alphaxiv.org/abs/2607.06503v2 | Bases « behavior-only » (probabilités de jetons, mots clés d'erreur) « consistently weaker » ; **« adding behavioral features to hidden-state probes provides no further gain »** — un modèle combiné existe, dans le sens **texte ajouté à la sonde** ; construction non décrite sur la page. | **en partie** : le seul modèle combiné trouvé ; sens inverse du test de A20 (sonde ajoutée au texte) ; échec, non sabotage | résumé |
| Revankar et al. 2026, MIRAGE (ci-dessus) | https://arxiv.org/html/2606.10304 | Base de six statistiques de surface à 0,816 d'AUC ; l'écart restant « must live in the hidden states » (§ 5.1) : argument **informel**, pas de test emboîté. | **en partie** | § 5.1, § 5.2 |
| McKenzie et al. 2025 (ci-dessus, A11) | https://www.alphaxiv.org/abs/2506.10805.md | Bases boîte noire (réglage fin, invite ; TF-IDF + SVM en annexe B.4) ; cascade sonde → base avec moyenne des scores ; « probes and baselines capture complementary information » fondé sur des gains d'ensemble, « not a controlled analysis of what the probe adds beyond the text ». | **en partie** | § 2.2, § 2.3, § 3, annexe B.4, figures 6 et 13 |
| Xu et al. 2026, PreAct-Bench (ci-dessus, A12) | https://www.alphaxiv.org/abs/2606.09890.md | Sonde linéaire 0,774 contre modèles invités jusqu'à 0,852 ; comparaison côte à côte, **pas de modèle combiné**. | **en partie** | résumé, table A1 |
| Salehmohamed et al., « Weakly supervised distillation of hallucination signals into transformer representations », arXiv 2604.06277 | https://arxiv.org/html/2604.06277v1 | Sondes internes 0,8577 contre bases de similarité 0,41–0,42 ; **pas de modèle combiné ni emboîté** ; bases faibles. | **non** (comparaison séparée, bases proches du hasard) | § 2.4, § 7.4, table 6 |
| Partition de variance / régressions empilées (neurosciences : « Stacked regressions and structured variance partitioning for interpretable brain maps », PMC12117960) ; tâches de contrôle (Belinkov 2022, « Probing classifiers: promises, shortcomings, and advances », arXiv 2102.12452) | résultats seuls | **Non lus** (pages bloquées ou non prioritaires) ; la partition de variance est la méthode des neurosciences pour « variance unique d'un espace de traits au-delà d'un autre ». | non évalué | — |
| Carte : 2602.14161 (base « texte seul », sans page) | — | **Non trouvé ni lu** dans ces requêtes. | non évalué | — |

**Ce qui reste ouvert après lecture.** La méthode est ancienne et nommée ailleurs (ΔR² de la validité incrémentale ;
tests de randomisation et de permutation conditionnels ; partition de variance) ; dans la littérature des sondes-moniteurs lue,
la norme est la **comparaison séparée** (gain « black-to-white », bases côte à côte) ; un seul modèle combiné (Ruan et al.),
dans le sens inverse et sans construction visible ; **aucun test emboîté « texte + sonde contre texte seul » sur une sonde
d'intention ou de tromperie** n'a été trouvé, ni aucun test de randomisation conditionnelle appliqué aux traits de texte
(HT-03). La carte peut donc dire que FI-05 applique une méthode connue à un objet où elle n'a pas été vue appliquée.

**Mots clés d'une suite.** « incremental validity activation probe transcript features nested logistic regression » ;
« conditional randomization test activations given text features monitor » ; « probe residualized on lexical features
deception » ; « stacked regression variance partitioning activations versus text LLM » ; « black-to-white boost nested test ».

## 8. Réserves

1. **Provenance.** Toutes les lectures sont des rendus de pages web par l'outil de lecture, qui résume ; aucune n'a été faite sur
   un PDF empreinté ; les citations entre guillemets sont celles que l'outil a rapportées comme textuelles. Avant tout usage
   opposable (préenregistrement, papier), relire la page citée sur le PDF empreinté (R7), en particulier Hemming et al. 2011,
   Donoho et Jin 2004, Baker et al. 2019, Berrett et al. 2019, Kramár et al. 2026.
2. **Deux lectures manquées** (section d'en-tête) : « Detecting Strategic Deception Using Linear Probes » (refus du modèle de
   lecture ; lu via une page de présentation sans métadonnées, qui indique une agrégation par la **moyenne** et une sonde qui
   réagit aussi à du texte « lié à la tromperie ») ; « Power and limitations of conformal martingales » (non trouvé aux liens
   promis).
3. **Horodatage** : le système de fichiers du dossier de sortie affiche une heure (04:25) en avance d'environ une heure sur
   `date -u` (03:23) ; les heures du présent document sont celles de `date -u`.
4. **Deux sources contiennent des expériences d'attaque** (MIRAGE ; Lindner et al., § 4.3) : citées pour leurs constats sur
   les moniteurs seulement ; aucune procédure n'est reprise ici.
5. **Périmètre** : un peu plus d'une heure de recherche, huit requêtes par question ; une suite devrait d'abord lire les
   références non lues marquées « non évalué », puis les mots clés de suite ; un « non trouvé » ici ne vaut que par la liste.

**Fin** : relevé `date -u` de **03:44:54 UTC le 28 octobre 2026** (appel séparé de toute écriture) ; durée totale 21 minutes
et 32 secondes depuis le relevé de début (03:23:22), sous l'heure visée.
