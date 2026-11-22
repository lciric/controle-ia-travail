# Semaine des systèmes (dépôts arXiv du 14 au 19 novembre 2026) — rapport de lecture

Sources : `/tmp/claude-0/-home-user-controle-ia-travail/7225ef84-cf06-5367-97a0-6c2a4e600e2b/scratchpad/sources/semaine-systemes/` (PDF `IDENTIFIANT.pdf`, page arXiv `IDENTIFIANT.abs.html`). Tous les PDF passent `pdfinfo`. Les pages citées sont celles du fichier PDF. Les dates viennent de la ligne « Submitted on … » de la page arXiv (v1). Statut de chaque fiche : « lu sur PDF, p. N », sauf mention contraire.

| Identifiant | sha256 (PDF) |
|---|---|
| 2611.24711 | de958721ff1fa11cef675c894e0dd241e7bf054a4af39b06a216bd30586ff86d |
| 2611.23080 | 7d18e0605c0b0c25b1acd91c8751cefeb043513b791a2a3ac2aa56d44d1b568a |
| 2611.19594 | df6d0c20bab227919584ce069256c14791281616a8da3c6154e98c668fc09e44 |
| 2611.22032 | eb6f8b515573262fe434163cb1726408d04a66cf33c7657c45eb57af992e259f |
| 2611.25357 | b6cf25ceff8ce44625138ce24fcfbac81c894e84ee77befc1552d33e191982a1 |
| 2611.21765 | 15f8abcd6fd1b6b9226606ca41e2475c25cfcc96ecea293016268ae419d47df2 |
| 2611.26343 | 3474e0a0f70394ba5c4541a5963de0430093108f3c306dc153e6d317dc72520e |
| 2611.26248 | ee8206b11a9a13d2b4b6526e9dd2187b79f41526708889d9d52620e64ecc93aa |
| 2611.20649 | c44e4480bfff7472182a797c637dc6d19239a6a6cfd991921a0d13f06972b63c |
| 2611.23949 | 0beec4cf0367f3f7db457ffbecccb50598a1c8b81744a6a83e29738a92e0dbf9 |
| 2611.19543 | 51053fb2c452b632e1e6ff9d6a1fe3f7639e8d051b37542416a182d2e327d406 |

---

## 1. Openhagen Worlds (2611.24711), déposé le 18 novembre 2026
- **Auteur** : Alexander Boesgaard Lorup, Openhagen (seul auteur ; rapport technique d'une entreprise ; le banc est « available to research and industry partners under licence », p. 25).
- **Ce que c'est** : 27 familles de mondes générés par programme, 178 niveaux (92 de base, 86 « frontière »). Un vérificateur déterministe compare la réponse engagée à une vérité cachée. La règle de notation complète figure dans chaque observation (p. 1, p. 4).
- **Étalonnage (p. 5)** : sur 64 instances de développement, un niveau n'est admis que si l'oracle scripté (ensemble exact des hypothèses compatibles, ou loi a posteriori, puis expérience qui les sépare le mieux) réussit au moins 0,75, la « politique naïve » au plus 0,25 et chaque raccourci au plus 0,35. Citation : « The naive policy is the strongest plausible non-deductive policy for the family, such as probing in a fixed order or regressing on observational data. Shortcut policies are specific habits that could pass for skill, such as measuring at both safety limits, plus an answer prior that commits another instance's correct answer » (p. 5). Au niveau frontière, le panel ajoute la stratégie du barreau inférieur, une politique qui résout chaque étape d'une campagne à neuf, et un oracle sans carnet (p. 5). Le « plan exhaustif » (toutes les expériences dans un ordre fixe, puis l'analyse de l'oracle) est rapporté sans servir de filtre. Il résout 0,98 à 1,00 des niveaux de discrimination de mécanismes, mais seulement 0,02 à 0,28 des niveaux d'induction de règles (p. 1-2) : une partie des familles teste l'analyse et non le choix des expériences.
- **Familles (p. 5-6, fig. 2)** : 15 mondes de découverte (dont quatre énigmes classiques : tests groupés, fausse pièce, induction de règles, apprentissage d'automates ; puis panne de circuit, cinétique, intervention causale, débogage de programme, etc.), 2 MicroWorld, 5 PhysicsWorld (simulateurs), 5 ChemistryWorld. Quatre familles sont tenues hors de tout entraînement (p. 6).
- **Résultats (tableau 5, p. 11)** : oracle 0,978 au niveau de base, 0,910 à 0,942 au niveau frontière ; Qwen3.8-27B 0,358 au niveau de base, 0,087 au niveau frontière ; DeepSeek V4.1 Flash 0,583 au niveau de base, 0,343 au niveau frontière, 0,107 sur les campagnes à huit étapes (L3). Sur les 84 instances frontière à une instance par famille et par barreau : Flash résout 32 sous le plafond de 16 384 jetons, 57 à l'effort maximal (393 216 jetons) ; l'oracle en résout 79 (p. 1-2) ; GPT-6.1 Sol, en pilote par l'interface en ligne de commande, en résout 71 (p. 13, p. 25). Une grande part de la difficulté vient donc du budget de jetons : « much of the difficulty is a budget effect » (p. 2).
- **Référence comparée** : les politiques scriptées (oracle et politique naïve) jouent les mêmes instances, et les comparaisons sont appariées (p. 5, p. 10). Ce n'est pas un tirage simple de modèles à budget égal.
- **Ce que le banc ne mesure pas (limites, p. 24-25)** : « calibration cannot exclude shortcuts that nobody has written » (p. 24). Le niveau frontière a été réglé sur les résultats de Flash obtenus sur les instances finales, puis ces instances ont été rejouées après révision des analyseurs (p. 6, p. 24). Les familles mesurent le raisonnement expérimental « in a pure form, not domain science » (p. 24). L'étude d'entraînement repose sur un modèle et une course (p. 24) ; celle par renforcement sur une graine par course (p. 25).
- **Ce que l'article ne montre pas** : aucune validité externe vers la découverte réelle ; aucun tirage simple à budget égal entre agents ; les résultats de Sol reposent sur une instance par barreau.

## 2. Colombo (2611.23080), déposé le 17 novembre 2026
- **Auteurs** : Haihan Zhang, Wendao Wu, Chenheng Zhang, Chunyuan Zheng, Yanyi Li, Cong Fang, Haoxuan Li, Zhouchen Lin (Peking University, « ZERO Lab », p. 1). Modèle sous-jacent : « GPT-5.6 Sol » (p. 4). L'article dit avoir été déposé d'abord sur Zenodo (p. 2).
- **Procédé** : un « Complexity Atlas » consigne, pour chaque cadre d'optimisation par oracle, les bornes supérieures et inférieures les mieux établies et l'écart qui reste entre elles (p. 4). Un « Brain » formule des conjectures de vitesses optimales et découpe le travail en sous-problèmes confiés à des « Cells » ; il replanifie selon les preuves obtenues (p. 2, p. 14). La co-ascension adverse cherche d'un côté un algorithme qui bat une famille difficile, de l'autre des instances qui battent un algorithme (formule p. 15). Un humain intervient : « a human approval gate selects the Setting Profile to be passed to the Brain » (p. 7).
- **Ce qui est vérifié formellement** : la section 2.4 (p. 12) décrit une traduction en Lean, une vérification par le noyau, une comptabilité des axiomes et un alignement sémantique entre l'énoncé formel et la revendication. Cet alignement est confié au système lui-même ; aucun tiers ne le fait. Selon l'article, seuls les énoncés certifiés entrent en mémoire : « Only after formal certification succeeds are the resulting claims admitted » (p. 10).
- **Ce qui ne l'est pas, ou n'est pas montré** : le rapport ne publie ni fichier Lean, ni décompte des énoncés certifiés, ni d'exemple d'énoncé formel. Le site et la démonstration sont « under construction » (p. 16). Les « plus de cinquante cadres » correspondent à 56 articles (tableau 1, p. 16), cités pour la plupart comme prépublications arXiv des mêmes auteurs (p. 22-26). Aucune relecture par des pairs n'est indiquée.
- **Référence comparée** : seulement l'historique des bornes publiées (annexe A, p. 28-33). L'article ne compare le système ni à un autre système, ni au même modèle sans l'architecture, ni à un tirage simple.
- **Ablation** : aucune (j'ai cherché « ablation » et « baseline » dans le texte : rien qui porte sur le système).
- **Ce que l'article ne montre pas** : la part de chaque mécanisme dans les résultats ; le coût ; le taux d'échec ; la vérification des énoncés par un tiers.

## 3. Record de l'exposant somme-différence de Katz-Tao (2611.19594), déposé le 14 novembre 2026
- **Auteur** : Atrin Farnamfar, seul auteur, sans affiliation indiquée (p. 1).
- **Résultat** : C3b ≤ 209357544569848128/114631769327023765 ≈ 1,8263483657 pour les groupes abéliens sans 2-torsion. Pour tout groupe abélien, la borne vaut ≈ 1,8264161855 (p. 1-3). Record précédent : Tomar 2026, 1,8272962152674 ; pour tout groupe, 9213/5036 ≈ 1,82943 (p. 2). Avec les seuls ingrédients classiques, l'article obtient aussi 2762/1509 et 152/83, sous 11/6 (p. 3).
- **Procédé de recherche** : il est décrit en trois phrases seulement. Citation : « AI agents explored stacked configurations, discovered the certificates and verified the resulting proofs with independent exact checkers, under the author's direction. CASP used Anthropic Claude and OpenAI Codex models » (p. 2) ; « AI-directed search under the author's direction » (p. 14). L'idée nouvelle est l'« empilement » de copies conditionnelles (p. 2). L'article ne donne ni algorithme de recherche, ni budget, ni comparaison.
- **Certification** : des identités rationnelles exactes, vérifiées par des vérificateurs en Python (bibliothèque standard), avec un audit de domaine sur Z ou Z[1/2] (p. 9-11). Une seconde vérification passe par le vérificateur public de Tomar, lancé sans modification, mais sur des certificats compagnons plus faibles : 1,8271149 et 1,8271177 (p. 11, p. 13). Les 34 entrées délibérément corrompues sont toutes rejetées, ainsi que 4 et 5 corruptions supplémentaires (p. 13). Il n'y a pas de preuve formelle en Lean.
- **Comparaison avec l'étude AlphaEvolve (2511.02864)** : l'article dit que cette étude a amélioré la borne inférieure « in the eighth decimal place » et a laissé la borne supérieure à 11/6 (p. 1-2). Citation : « Such distributions witness lower bounds for this constant; a universal upper bound requires a proof » (p. 2). Les deux travaux portent donc sur deux côtés différents du problème, et aucune comparaison de procédé n'est faite. Le record battu est celui de Tomar, non celui d'AlphaEvolve.
- **Ce que l'article ne montre pas** : le coût ni la part de l'humain dans la découverte ; aucune référence de recherche (par exemple un programme linéaire sur les configurations empilées sans agent).

## 4. FunSearch et recherche par satisfiabilité pour les partitions de Schur faibles (2611.22032), déposé le 17 novembre 2026
- **Auteurs** : R. Vicenzi (Bologne), P. Christofferson (Carleton College), C. Hartman (Waynesburg), J. Feng (USC), S. Khan (RIT), O. M. Elshinawy (Münster), E. Ramos (Stevens) (p. 1).
- **FunSearch** fait évoluer la seule fonction de priorité d'un solveur glouton fixe (p. 3-4). Il retrouve WS(2)=8, WS(3)=23 et WS(4)=66, et atteint **WS(5) ≥ 195**, ce qui reste sous la borne publiée de 196 (Eliahou et al. 2012 ; tableau 2, p. 7). L'article ne nomme pas le modèle employé et ne donne ni nombre d'échantillons ni budget. Il précise : « their individual effects have not been validated by ablation experiments » (p. 4).
- **Recherche par satisfiabilité** : le solveur SLIME5 tourne environ 107 s sur 1 035 variables et 56 334 clauses (p. 7). La formule contient deux restrictions tirées de la note de Fred Rowley (« Rowley, 2026 ») : une période de 4 dans [100, 120] et 14 couleurs imposées (p. 6). Résultat : **WS(5) ≥ 207**. Réserve importante : « Rowley's source also gives a partition at 207 » (p. 8). La partition trouvée en diffère, avec un accord maximal de 191 positions sur 207 (p. 8). Le gain de 11 se mesure donc contre la borne de 2012 ; contre la note de Rowley, l'article n'apporte pas de borne meilleure, seulement une autre partition de même taille.
- **Limite de FunSearch** : citation : « its greedy solver makes local, irreversible decisions, whereas SAT can enforce global structure across the whole partition » (p. 1) ; à 195, chaque classe bloque 196 (p. 5). Les auteurs bornent eux-mêmes la portée : « it does not prove a general limitation of FunSearch » (p. 8).
- **Vérification** : par programme, sur tous les couples (10 609 pour N = 207), indépendamment du solveur (p. 8).
- **Ce que l'article ne montre pas** : aucune comparaison à budget égal entre FunSearch et un tirage simple de priorités, ou une recherche locale. La satisfiabilité seule, sans l'information de Rowley, n'a pas été essayée, ou du moins l'essai n'est pas rapporté.

## 5. Pro² Agent (2611.25357), déposé le 19 novembre 2026
- **Auteurs** : Yixiong Chen (Google et Johns Hopkins, stagiaire), L. Peng, T. Tan, Z. Lin, B. J. Chen, C. Zhao, Y. Liu, A. Go (Google), A. Yuille (Johns Hopkins) (p. 1). Modèles : Gemini 3.5 Flash pour l'exécution et la relecture, Gemini 3.1 Pro pour le « PI Agent » (p. 9-10).
- **Procédé** : l'état principal n'est plus le code mais un « Problem State », c'est-à-dire la liste des problèmes qui bloquent, des solutions candidates et de leur confiance. Cet état est initialisé par analyse, relié à la littérature, puis mis à jour par des tests d'hypothèse à une seule variable (p. 1, p. 6). Citations : « on difficult problems it often gets stuck in the wrong solution region because the agent never explicitly represents its understanding of the problem » (p. 1) ; « the agent may repeatedly propose locally reasonable code changes while staying within the wrong solution region » (p. 2).
- **Chiffres sur MLE-Bench (tableau 1, p. 10)** : sur les 75 tâches, taux de médailles de 70,7 % en 24 h et de 76,0 % en 48 h, avec un A100 et **une course par budget**. Les systèmes comparés utilisent d'autres modèles et d'autres calculs. Les auteurs le reconnaissent : « they provide system-level context rather than a controlled comparison » (p. 9). Le score de 70,7 % égale celui d'AIBuildAI-2 (Claude Opus 4.7). Sur PostTrainBench, Pro² obtient 30,69 ± 3,1 contre 41,79 pour Fable 5, avec un budget de 24 h sur A100 contre 10 h sur H100 pour les autres (tableau 2, p. 10).
- **Contrôles et ablations (MLE-Bench Lite, 22 tâches, 24 h, trois courses ; mêmes modèles et budgets, p. 9)** : première solution, taux de médailles de 57,6 % contre 12,1 % pour une boucle de code directe, 28,8 % pour une variante avec recherche documentaire et 28,8 % pour MARS (tableau 3, p. 12). Les trajectoires de MARS viennent de son dépôt public, avec Gemini 3 Pro : ce contrôle n'est pas apparié. Ablation (tableau 4, p. 13), médaille finale : état « base de code » 56,1 %, état « problème » sans ancrage 77,3 %, état statique 83,3 %, système complet 89,4 %.
- **Ce que l'article ne montre pas** : aucun tirage simple à budget égal, par exemple N essais indépendants du même modèle avec sélection sur la validation ; une seule course sur le banc complet ; aucun contrôle de contamination propre à MLE-Bench, dont les tâches sont publiques.

## 6. QORA, contrôle quantique robuste (2611.21765), déposé le 16 novembre 2026
- **Auteurs** : J. Yan, X. Lai, X. Lin, Y. Wang, C. Yao, G. He, T. Lewer, C. Zu, C. Zhang (département de physique et Center for Quantum Leaps, Washington University in St. Louis) (p. 1). Modèles : « GPT-6-Astra and Sorol » (p. 2).
- **Procédé** : un agent théoricien (« Theo ») coordonne cinq sous-agents : proposeurs, relecteurs, simulateur par diagonalisation exacte, classifieur et compositeur. Ils cherchent des blocs de 18 impulsions, retenus si le contraste moyen sur 12 états dépasse 0,8 et le minimum 0,7, puis composent un cycle de 7 blocs (126 impulsions). Un agent expérimental (« Dex ») pilote le montage, étalonne et mesure (p. 2-3). Ce sont les humains qui fixent les objectifs (p. 2).
- **Résultat expérimental** : T2 = 18,6 ± 0,7 µs pour AID-ROD-1 contre 9,8 ± 1,1 µs pour DROID-C3PO, la séquence conçue par des humains ; AID-ROD-2 atteint 19,3 ± 1,0 µs (p. 4).
- **Qui vérifie** : l'expérience physique, sur un ensemble de centres azote-lacune, mesurée par l'agent expérimental sur le montage des auteurs. Il n'y a pas de réplication extérieure.
- **Ce qu'ajoute l'analyse humaine** : l'explication. Citation : « human researchers identify the mechanisms underlying the sequences discovered by QORA » (p. 6). La hiérarchie de suppression des erreurs est établie par les humains (p. 1, p. 5).
- **Ce que l'article ne montre pas** : le nombre de candidats évalués et le budget ne sont pas trouvés dans le texte. Aucune comparaison avec une optimisation numérique classique ou un tirage au hasard dans le même espace de séquences.

## 7. DeepQuest, maladie d'Alzheimer (2611.26343), déposé le 19 novembre 2026
- **Auteurs** : C. Jiang, Y. Chen, B. Wu, F. Mao, W. Chen, E. Bao, M. Liu, F. Qin, Q. Tian (Hangzhou Dianzi, Tsinghua, Central South) (p. 1). L'en-tête porte « Published as a conference paper at ICLR 2027 » (p. 1) ; je n'ai pas vérifié cette mention.
- **Lacunes de connaissance** : extraites de 10 revues du domaine par un modèle, puis transformées en paires « limite-hypothèse » (p. 4, p. 14).
- **Classement** : un modèle classe les hypothèses par groupes de 5, avec identifiants anonymes et ordre aléatoire, et les scores sont mis à jour par Elo (p. 5).
- **« Taux de trouvailles scientifiques »** : c'est la part des tâches que l'**audit** classe en « découverte candidate », « redécouverte » ou « extension » (p. 7). L'audit est un agent, c'est-à-dire un modèle, qui compare chaque affirmation à un corpus figé de 200 études publiées après le 16 février 2026 (p. 7). Le tableau 4 est intitulé « under Claude evaluation » (p. 15). DeepQuest obtient 95,24 %, soit 40 tâches sur 42, contre 78,57 % pour Codex et 76,19 % pour Claude Code sur les mêmes hypothèses (p. 8). L'écart des ablations tient à une ou deux tâches : 92,68 % sans extraction des lacunes ; 90 % contre 100 % sur les dix premières sans Elo, soit une tâche sur dix (p. 9). La qualité des hypothèses est jugée par trois modèles (GPT-5.6-sol, Claude Opus 4.8, DeepSeek-v4-pro), qui donnent l'avantage à DeepQuest dans 14 comparaisons sur 15 (p. 1, p. 14).
- **Validation** : les associations clés sont retrouvées sur les cohortes indépendantes ADNI et AIBL, avec des rapports de risque chiffrés (p. 7, p. 9). C'est la seule vérification qui ne passe pas par un modèle.
- **Ce que l'article ne montre pas** : aucun jugement humain des trouvailles. La « nouveauté » est jugée par un modèle contre un corpus limité. Aucun budget égal ni tirage simple d'hypothèses n'est contrôlé.

## 8. TwinLab-Bench (2611.26248), déposé le 19 novembre 2026
- **Auteurs** : Yang Wan, Linchao Zhu (Zhejiang University) (p. 1).
- **Principe** : 52 tâches tirées de vrais laboratoires. Un agent « jumeau » sert d'environnement : il lit les matériaux bruts du laboratoire et des calculateurs bâtis sur ses registres. Le rapport de l'agent testé est noté par un **agent juge**, un modèle vision-langage, selon une grille, contre une réponse cachée tirée des registres réels (p. 1, p. 7). Le jumeau et le juge tournent tous deux sur DeepSeek-flash (p. 7).
- **Scores** : Claude Fable 5.2 obtient 45,0, Claude Opus 5.5 40,2, les autres entre 5,4 et 31,7 ; GPT-6.1-sol obtient 31,7 (p. 5, p. 7). Doubler le budget ne transforme que 2 échecs d'Opus 5.5 sur 21 en réussite (p. 9).
- **Contrôles de mémoire (p. 8-9)** : quand l'état vrai du laboratoire est changé, la conclusion suit le nouvel état dans 8 cas sur 10 qui permettent un verdict. Les sondes à livre fermé d'Opus 5.5 (52 cas) ne retrouvent la conclusion de la source dans aucun cas ; Fable 5.2 la retrouve dans un cas. Avec un budget nul, aucune tâche n'est réussie. Les écarts au registre et les réponses incohérentes tombent de 41 % et 31 % (modèle qui ne voit que l'énoncé) à 2 % et 4 % avec le jumeau (p. 2, figure).
- **Ce que l'article ne montre pas** : la note dépend d'un juge qui est un modèle. Sa stabilité est mesurée (accord de deux juges dans 19 cas sur 20, p. 8), mais aucun humain ne la valide. Les lectures hors du registre sont extrapolées par des calculateurs, même si 76 % des lectures viennent du registre (p. 8).

## 9. Borrowed Strength, Imported Risk (2611.20649), déposé le 16 novembre 2026
- **Auteurs** : P. Nilayam, K. K. Ramanna, P. Tumbade, N. N. Bhat, S. Nayak (ServiceNow) (p. 1).
- **Plan** : pour chaque direction (receveur, pair, tâche), quatre panels de trois agents sont appariés : receveurs seuls, pairs seuls, mixte honnête, mixte avec un pair adverse (p. 2). Il y a neuf directions sur MATH-hard et GSM8K, deux directions de confirmation à receveur fixe et une sonde sur MuSiQue (p. 2-3).
- **Décomposition** : le gain honnête vaut à peu près κ multiplié par l'avantage du pair Γ⁺ et par la réception ρ. Le produit donne R² = 0,995, contre 0,776 avec l'écart de capacité seul (p. 2). Les auteurs reconnaissent que cet ajustement est en partie mécanique : « the product fit is partly structurally induced » (p. 3). Le modèle figé prédit les deux directions à receveur fixe : avec une réception d'environ 61 % et un écart doublé, le gain passe de 7,89 à 16,92 points (p. 2). Sur MuSiQue, la réception atteint 62,50 % mais le gain n'est que de +1,17 point, car le pair est plus faible de 10,78 points (p. 1).
- **Vote majoritaire** : citation : « the panel's best majority correctness … never exceeds the peer's best accuracy inside that panel, while an oracle that credits any correct member is 4.7–23.0 points higher » (p. 7). Exemple : pair 80,62 %, majorité 79,97 %, oracle 85,37 % (p. 13).
- **Budget** : le débat consomme 40,6 à 86,7 fois les jetons d'un seul appel au pair (médiane 62,2). Même la meilleure ronde, choisie après coup, ne bat le pair en un seul passage que dans 3 directions sur 9 (p. 7). C'est l'un des seuls articles de la semaine qui compare à une référence simple en comptant le budget. Les auteurs ajoutent : « Strong-model resampling and learned routing remain unevaluated » (p. 7).
- **Risque** : avec un pair adverse, le panel tombe 3,06 points sous le panel homogène à la première ronde ; l'écart atteint −27,60 points en quatrième ronde dans le panel GPT-OSS (p. 2).
- **Limites (p. 9)** : les directions ne sont pas indépendantes ; MuSiQue repose sur une paire et une réplique ; l'adversaire suit une seule invite.

## 10. Spéciation incrémentale en attaque évolutive (2611.23949), déposé le 18 novembre 2026
- **Auteurs** : Onkar Shelar, Travis Desell (Rochester Institute of Technology) (p. 1).
- **Plan** : deux représentations de la ressemblance (plongements MiniLM, non-implication par NLI) croisées avec deux assignations (meneur-suiveur, DBSCAN incrémental). La référence non spéciée est ToxSearch (« Global EA »). Chaque configuration tourne 10 fois, avec 2 000 évaluations uniques par course, à budget égal (p. 3, p. 11). La note vient de l'outil de modération d'OpenAI (p. 5, p. 10).
- **Résultat** : à la fin, la médiane de la note des 50 meilleures invites vaut 0,80 pour les deux DBSCAN, 0,69 et 0,63 pour meneur-suiveur, 0,60 pour la référence globale. Les écarts DBSCAN moins meneur-suiveur valent Δ = 0,050 [−0,113 ; 0,215] et 0,156 [−0,004 ; 0,315] (p. 11-12). Citation : « the bootstrap intervals based on the 10 executions include zero and do not establish a reliable performance advantage » (p. 1). Aucun intervalle n'est donné pour l'écart avec la référence non spéciée.
- **Diversité** : citation : « The semantic diversity of top prompts declines in every configuration, with no consistent advantage for either method » (p. 1). Δ diversité = 0,049 [−0,025 ; 0,122] et −0,023 [−0,113 ; 0,066] (p. 12).
- **Ce que la spéciation change** : la structure de la population plus que la note. NLI avec DBSCAN réduit la population à environ une espèce (part médiane 0,995) et concentre ses meilleures invites sur quelques thèmes de départ (p. 12-13).

## 11. Grands « caps » de F₃⁹ et F₃¹¹ (2611.19543), déposé le 14 novembre 2026
- Matt Holden (adresse personnelle). Il construit des caps de 1 104 points dans F₃⁹ (contre 1 082 auparavant) et de 5 744 points dans F₃¹¹ (contre 5 504), par relèvement et substitution à partir des caps classiques de Hill et de Calderbank-Fishburn (p. 1).
- **Usage de FunSearch** : le cap de 512 points de FunSearch ne sert pas d'ingrédient. L'auteur constate que les deux couches extérieures de son cap sont linéairement équivalentes au cap de FunSearch et vérifie cette équivalence par programme (p. 1-2). L'article ne mentionne aucune recherche automatique.

---

## Tableau de synthèse

| # | Système | Procédé d'exploration | Référence comparée | Budget égal ? | Preuve hors d'un modèle |
|---|---|---|---|---|---|
| 1 | Openhagen Worlds | (banc) oracle scripté, politique naïve, raccourcis | politiques scriptées sur les mêmes instances | apparié par instance ; budgets de jetons différents selon les modèles | vérificateur déterministe |
| 2 | Colombo | conjecture et décomposition, co-ascension adverse, mémoire | historique des bornes | sans objet | Lean annoncé, aucun artefact publié |
| 3 | CASPAC | agents qui cherchent des configurations empilées, non décrits | record de Tomar | non rapporté | vérificateurs rationnels exacts, vérificateur public de Tomar |
| 4 | FunSearch et satisfiabilité | évolution de programmes ; solveur avec structure humaine | borne de 2012 ; note de Rowley (207) | non | vérification exhaustive par programme |
| 5 | Pro² | état « problème » et tests d'hypothèse | systèmes publiés ; variantes internes ; MARS | variantes internes oui ; tirage simple non | note du banc (Kaggle) |
| 6 | QORA | proposeurs, simulation, composition, expérience | séquence humaine DROID-C3PO | non | mesure physique |
| 7 | DeepQuest | lacunes tirées des revues, tournoi Elo, audit | Codex, Claude Code, Biomni, DiscoADRD | non | cohortes ADNI et AIBL (le taux, lui, est jugé par un modèle) |
| 8 | TwinLab-Bench | (banc) jumeau d'un laboratoire réel | 13 modèles | coût rapporté | réponse tirée des registres ; note donnée par un juge modèle |
| 9 | Débat hétérogène | débat à trois agents | panels homogènes, meilleur membre, oracle | **oui, coût en jetons compté** | notation exacte des réponses |
| 10 | Spéciation | algorithme évolutif avec espèces | algorithme évolutif global | **oui (2 000 évaluations)** | outil de modération (un modèle) |
| 11 | Caps | construction à la main | bornes publiées | sans objet | vérification par programme |

## Lecture d'ensemble
- Procédés employés : des boucles d'agents à mémoire et replanification (Colombo, CASPAC, Pro², QORA, DeepQuest), de l'évolution (FunSearch, spéciation) et des solveurs exacts guidés par une structure humaine (satisfiabilité).
- Sur 9 systèmes ou méthodes de recherche (hors les deux bancs), aucun n'est comparé à un tirage simple du même modèle à budget égal.
- Deux articles font une comparaison à budget égal contre une référence simple : le débat (contre le meilleur membre, coût compté) et la spéciation (contre l'algorithme évolutif global, mêmes évaluations). Aucun des deux n'y trouve d'avantage établi.
- Les résultats mathématiques solides reposent sur des certificats vérifiés par programme (Katz-Tao, Schur, caps), et non sur le procédé. Le gain de 207 existait déjà dans la note de Rowley.
- Les bancs (Openhagen, TwinLab) contrôlent les raccourcis et la mémoire ; Openhagen reconnaît ne pas pouvoir exclure les raccourcis que personne n'a écrits.

## Non vérifié
- La mention « ICLR 2027 » de DeepQuest.
- L'existence et le contenu des fichiers Lean de Colombo (aucun lien dans le PDF).
- Le contenu de la note de Rowley (2026), non publique selon l'article (« communicated »).
- Les annexes et suppléments de CASPAC (`anc/`), Openhagen, TwinLab et du débat : non téléchargés ni exécutés.
- L'étude AlphaEvolve 2511.02864 : non relue ici ; ce qui en est dit vient de 2611.19594, p. 1-2.
- Le nombre de candidats évalués par QORA et le modèle employé par FunSearch dans 2611.22032 : non trouvés dans le texte.
