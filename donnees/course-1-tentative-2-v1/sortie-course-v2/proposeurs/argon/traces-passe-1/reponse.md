```json
{
 "fiches": [
  {
   "nom": "Q4 — Le diffus comme axe d'universalité séparé sous borne d'horizon",
   "type": "question",
   "enonce": "En désaccord avec la pièce B (qui relègue Q4 à l'étape 2 et enchaîne Q3 à faible puissance puis Q-pont), Q4 est LA question centrale : un moniteur (sonde d'activations internes et/ou boîte noire) évolué sur des menaces concentrées échoue-t-il au transfert vers des menaces diffuses à dommage total constant selon la loi de transition théorique, et la combinaison boîte blanche inter-épisodes plus agrégation séquentielle par processus de pari restaure-t-elle ce transfert sur des familles tenues à l'écart ?",
   "loi_predictive": {
    "espace_instances": "Séquences multi-épisodes ou multi-agents obtenues par dilution paramétrique (facteur K de 1 à 9 épisodes ou requêtes de fusion) de trajectoires issues de bancs publics (ControlArena, SHADE-Arena, Iterative Vibe Coding, FakeLab), N >= 300 séquences par niveau de K, évaluées sur modèles à poids ouverts de 8 et 70 milliards de paramètres.",
    "prediction": "Sous règle de décision par instant, le rappel d'un moniteur évolué sur du concentré chute avec le facteur de dilution K et le délai moyen de détection bascule de O(log gamma) à Theta(gamma) dès que le produit de la contrainte de fausse alarme gamma par la divergence de Kullback-Leibler par pas franchit le seuil critique O(1) ; à scores d'activations identiques, le remplacement du seuil par instant par un processus de pari séquentiel inter-épisodes abaisse le taux d'évasion graduelle d'au moins 25 points de pourcentage à taux de fausses alertes fixé.",
    "signe": "-",
    "metrique": "Pente du rappel (et du taux d'évasion) en fonction du facteur de dilution K à taux de fausses alertes fixé à 1 % par séquence sur familles diffuses tenues à l'écart, normalisée par famille selon la robustesse aux attaques imprévues (Unforeseen Attack Robustness), et écart d'erreur quadratique avec l'asymptotique théorique de Ramtin, Nain et Towsley."
   },
   "perte_traduction": "Réduit la richesse stratégique des menaces diffuses (choix adaptatif du moment d'attaque pour maximiser la couverture naturelle, coordination par planificateur) à un paramètre scalaire de dilution K et de divergence de Kullback-Leibler stationnaire par épisode.",
   "questions_servies": [
    "Q4",
    "Q2",
    "Q7"
   ],
   "avantage": {
    "source": "programme",
    "texte": "Intersection exclusive de quatre briques du programme : ancrage théorique formel (lemme du plafond d'horizon), sondes en boîte blanche sur poids ouverts de 8 et 70 milliards de paramètres, agrégateur séquentiel formel, et sélection sous juge figé garanti sur familles tenues à l'écart — le tout en variant la dilution par découpage contrôlé sans construire d'attaquant.",
    "incopiable_parce_que": "Les occupants du diffus (Terekhov et al., Makins et al., Hills et al.) opèrent à 100 % en boîte noire sur modèles fermés par interface de programmation et couplent leur évaluation à l'élicitation d'un attaquant (sujette aux refus des modèles de frontière et au surajustement en distribution). Reproduire notre mesure exige d'extraire les états cachés inter-épisodes sur 70 milliards de paramètres et d'abandonner la co-évolution d'invites d'attaque au profit d'un découpage paramétrique sous juge figé."
   },
   "originalite": {
    "niveau": "transposition",
    "texte": "Transpose la théorie asymptotique de la détection de changement le plus rapide face à un adversaire furtif (Ramtin, Nain et Towsley 2025/2026) aux moniteurs d'agents (boîte blanche et boîte noire) en co-évolution défensive. Les constats boîte noire statiques existent (Hills et al. 2026 ; Angelini, Makins et al. 2026), et Terekhov et al. (2026) font évoluer une instruction de juge en boîte noire sur tâches floues sans agrégation séquentielle ni boîte blanche."
   },
   "demande_organisme": {
    "nature": "ajout",
    "texte": "En priorité sur processeur (coût nul) : opérateur de dilution paramétrique sur traces existantes et module d'agrégation séquentielle inter-épisodes. Puis en dépense modeste : extraction unique et mise en cache des activations (8 et 70 milliards de paramètres) sur les séquences diluées."
   },
   "cout": {
    "nature": "depense",
    "ordre_de_grandeur": "Processeur seul pour la théorie, l'opérateur de dilution et le rejeu sur scores boîte noire publiés ; 100 à 400 dollars de processeur graphique pour l'extraction unique d'activations sur 8 et 70 milliards de paramètres."
   },
   "piege": "Confondre l'effet mécanique de dilution avec l'effet de plausibilité de la couverture par la tâche principale (Angelini, Makins et al. montrent que la couverture explique 45 à 53 % de la baisse de suspicion contre 20 à 25 % pour la dilution pure), ou revendiquer le lemme du plafond d'horizon comme neuf sans citer Ramtin, Nain et Towsley (nœud N-A).",
   "cosmetique_si": "La courbe empirique de détection en fonction de K ne montre aucune transition au voisinage de gamma fois la divergence de Kullback-Leibler d'ordre 1, ou si l'agrégateur séquentiel sur activations ne bat pas le moniteur textuel à notes persistantes (link-tracker de Hills et al.).",
   "anteriorite": [
    {
     "reference": "Quickest Change Detection in Discrete-Time in Presence of a Covert Adversary, Ramtin, Nain, Towsley, 2026, arXiv:2601.20022v2",
     "statut": "RAPPORTE"
    },
    {
     "reference": "Quickest Change Detection in Continuous-Time in Presence of a Covert Adversary, Ramtin, Nain, Towsley, 2025, arXiv:2509.17778v1",
     "statut": "RAPPORTE"
    },
    {
     "reference": "Distributed Attacks in Persistent-State AI Control, Hills, Caspary, Cooper Stickland, 2026, arXiv:2607.02514v2",
     "statut": "RAPPORTE"
    },
    {
     "reference": "Multi-Agent AI Control: Distributed Attacks Hamper Per-Instance Monitors, Angelini, Makins, Shams, Phuong, 2026, arXiv:2607.07368v1",
     "statut": "RAPPORTE"
    },
    {
     "reference": "Diffuse AI Control on Fuzzy Tasks, Terekhov, Gulcehre, Hebbar, Benton, 2026, arXiv:2606.08892v2",
     "statut": "RAPPORTE"
    },
    {
     "reference": "Adaptive Deployment of Untrusted LLMs Reduces Distributed Threats, Wen et al., ICLR 2025, arXiv:2411.17693",
     "statut": "RAPPORTE"
    },
    {
     "reference": "TRACE, Mittapalli et al., 2026, arXiv:2606.07054",
     "statut": "RAPPORTE"
    },
    {
     "reference": "Caught in the Act: Probes Effectively Detect Sabotage and Catch Unverbalized Deception, Hollinsworth, Spies, Diriba, Gleave, Cundy, 2026, arXiv:2610.12445v1",
     "statut": "RAPPORTE"
    }
   ]
  },
  {
   "nom": "Nouvelle Q-N1 — Dégradation en ligne des bancs co-évolutifs (loi de Goodhart du juge)",
   "type": "question",
   "enonce": "Contre l'hésitation de la pièce B sur Q2 (hygiène ou résultat), on fusionne Q2 et Q6 en une entrée oblique offensive : dans les boucles de sélection de moniteurs utilisant un juge-modèle partagé ou une validation en distribution non garantie (protocoles de SafeCoEvo, AgentSafeEvo, MAGIC, EvoDefense, EvoSafety), quelle fraction du gain déclaré au fil des générations G est une fausse promotion ou une exploitation de l'artefact de source (mesurée par rétention des coefficients sous protocole laissant une famille de côté), et notre juge figé garanti à processus de pari plus témoins plantés annule-t-il cet écart ?",
   "loi_predictive": {
    "espace_instances": "Trois régimes de jugement exécutés sur la même boucle d'évolution de moniteurs pendant G = 20 générations sur un corpus multi-sources de trajectoires et d'invites publiques (FIBS 28 familles, MonitoringBench, Agent-SafetyBench, les 18 jeux de Fomin), avec K >= 10 familles en rotation laissant une famille de côté.",
    "prediction": "Sous les régimes des occupants (validation en distribution type SafeCoEvo ou juge-modèle partagé type MAGIC et AgentSafeEvo), l'écart entre le gain déclaré en distribution et le gain réel sur familles tenues à l'écart sous témoins bénins appariés du même générateur croît d'au moins 10 points de pourcentage en 20 générations, avec un taux de fausses promotions supérieur à 25 % et une chute de la rétention des coefficients sous 0,5 pour plus de 30 % des traits actifs ; sous notre juge figé à processus de pari composé (inégalité de Ville, seuil alpha = 0,05) et filtre d'artefact, le taux de fausses promotions reste borné par 5 % à tout temps d'arrêt.",
    "signe": "+",
    "metrique": "Écart cumulé de rappel (à 1 % de faux positifs sur témoins bénins appariés du même modèle) entre validation interne et protocole laissant une famille de côté, taux empirique de fausses promotions sur témoins nuls plantés, et métrique de rétention des coefficients r_j par génération G."
   },
   "perte_traduction": "Ramène la diversité des architectures co-évolutives publiées (apprentissage par renforcement multi-agents, optimisation de préférences, mémoire externe) à la seule statistique de sélection et de filtrage d'artefacts de leur boucle.",
   "questions_servies": [
    "Q2",
    "Q6",
    "nouvelle"
   ],
   "avantage": {
    "source": "organisme",
    "texte": "L'organisme dispose déjà en production (pièce F, démonstration couche 1 v7) du juge figé à mise contre bibliothèque de nuls avec borne de Ville, des témoins plantés (vrais et faux) et du pare-feu N-053 (aucun score du juge dans l'entraînement ou la sélection).",
    "incopiable_parce_que": "Les occupants ont un conflit d'intérêt structurel : leurs gains publiés (par exemple +21,5 points pour SafeCoEvo en choisissant le point de contrôle époque 13 sur la même validation, ou l'usage de Qwen3Guard et Qwen3.8-27B à la fois comme récompense et comme juge final dans MAGIC, EvoSafety et AgentSafeEvo) reposent sur le couplage que cette question invalide. Adopter notre juge figé garanti détruirait rétroactivement leurs courbes de progrès."
   },
   "originalite": {
    "niveau": "transposition",
    "texte": "Combine la certification séquentielle de mises à jour par séquences de confiance et processus de pari (Balachandran 2026 ; Mondal et al. 2026, qui n'ont ni boucle évolutive de moniteurs ni contrôle d'artefact) avec le diagnostic statique d'artefact de source sous rotation laissant un jeu de côté (Fomin 2026 ; Lin et al. 2026) pour mesurer la dérive dynamique d'une boucle (voisin en vision : Pathak et al. 2023)."
   },
   "demande_organisme": {
    "nature": "modification",
    "texte": "Sur processeur seul : brancher le bras « fuite textuelle » (N-053 point 1) et le calcul de rétention des coefficients r_j (Fomin) à chaque génération de la boucle existante de la pièce F, et instancier deux juges témoins dégradés (validation en distribution ; juge-modèle) pour la comparaison à trois bras."
   },
   "cout": {
    "nature": "processeur",
    "ordre_de_grandeur": "Entièrement sur processeur si exécuté sur activations et scores précalculés (ou quelques dizaines de dollars d'inférence locale)."
   },
   "piege": "Croire que la borne de Ville sur le jeu du juge garantit à elle seule la généralisation hors distribution (réserve C mineur de la pièce B : la borne contrôle les fausses promotions sur la loi du juge ; sans rotation des familles et témoins bénins appariés du même générateur, le juge figé certifie un raccourci de jeu de données).",
   "cosmetique_si": "La sélection en distribution de type SafeCoEvo ne produit pas plus de fausses promotions sur les témoins plantés ni plus de dérive de rétention r_j que le juge figé garanti à budget de calcul égal.",
   "anteriorite": [
    {
     "reference": "Pay Only for Disagreement: Certified No-Regression Verdicts for Model Updates with Matching Label-Complexity Bounds, Balachandran, 2026, arXiv:2609.17560v1",
     "statut": "RAPPORTE"
    },
    {
     "reference": "When Can Old Evaluations Certify a New Model? Label-Efficient Release Decisions under Evaluator Drift, Mondal, Banik, Apurba, Mahmud, 2026, arXiv:2609.32267v1",
     "statut": "RAPPORTE"
    },
    {
     "reference": "When Benchmarks Lie: Evaluating Malicious Prompt Classifiers Under True Distribution Shift, Fomin, 2026, arXiv:2602.14161v2",
     "statut": "RAPPORTE"
    },
    {
     "reference": "SafeCoEvo: Co-Evolving Safety Harnesses and Guards for LLM Agents at Test-Time, Cheng et al., 2026, arXiv:2609.36580v2",
     "statut": "RAPPORTE"
    },
    {
     "reference": "AgentSafeEvo: Adversarial Co-Evolution for LLM Agent Safety, Wang et al., 2026, arXiv:2610.19422v1",
     "statut": "RAPPORTE"
    },
    {
     "reference": "MAGIC: A Co-Evolving Attacker-Defender Adversarial Game for Robust LLM Safety, Wen et al., 2026, arXiv:2602.01539v2",
     "statut": "RAPPORTE"
    },
    {
     "reference": "EvoSafety: Model-Agnostic Lifelong LLM Safety via Externalized Attack-Defense Co-Evolution, Zhang et al., 2026, arXiv:2605.13411v1",
     "statut": "RAPPORTE"
    },
    {
     "reference": "EvoDefense: Co-Evolving Black-Box Defense with Large Language Models, Li et al., 2026, arXiv:2605.31140v1",
     "statut": "RAPPORTE"
    },
    {
     "reference": "When Lie Detectors Learn Model Identity: Confounds in Black-Box Sandbagging Detection, Lin, Bernabeu-Perez, Arnav, Wells, Phuong, ICLR 2026",
     "statut": "RAPPORTE"
    },
    {
     "reference": "Optimizing the Score, Losing Sight of the Task, 2026, arXiv:2609.25848",
     "statut": "RAPPORTE"
    }
   ]
  },
  {
   "nom": "Q3 + Q-pont fusionnées — Prédiction préenregistrée des angles morts par cellule (moniteur × propriété)",
   "type": "question",
   "enonce": "Contre la pièce B qui sépare Q3 et Q-pont et échoue par manque de puissance statistique sur K = 11 catégories (objection 1a), la théorie explicite des hypothèses des moniteurs (carte des hypothèses) prédit-elle a priori et sous scellement cryptographique, sur la matrice croisée de M moniteurs distincts et K cellules taxonomiques tenues à l'écart, à la fois (i) le classement des taux d'échec sur trajectoires d'agents et (ii) la corrélation de rang entre épisodes synthétiques sans attaquant portant la propriété P_k et épisodes semi-réalistes portant P_k ?",
   "loi_predictive": {
    "espace_instances": "Produit cartésien de M >= 8 moniteurs (sondes linéaires, sondes multicouches, autoencodeurs parcimonieux, moniteurs boîte noire par étape et par trajectoire, agrégateurs CUSUM) par K >= 30 cellules d'angles morts (issues de l'union figée de SLEIGHT-Bench 11 catégories, MonitoringBench T1-T5 × S1-S4 × E1-E4, et FIBS 28 familles), soit N >= 240 paires (moniteur, cellule) évaluées une seule fois après gel.",
    "prediction": "La corrélation de rang de Spearman entre la vulnérabilité prédite analytiquement (depuis les hypothèses violées de chaque moniteur m sur la propriété P_k) et le taux d'évasion observé dépasse 0,45 (valeur p < 0,001 par test de permutation stratifié par moniteur et par difficulté de base) ; sur les propriétés textuellement explicites, la corrélation synthétique-réel (Q-pont) dépasse 0,70, mais elle s'effondre sous 0,30 sur les propriétés textuellement ambiguës pour les moniteurs boîte noire tout en restant supérieure à 0,60 pour les sondes d'activations introspectives.",
    "signe": "+",
    "metrique": "Corrélation de rang de Spearman (et statistique de concordance c-index) entre prédictions scellées et rappels observés à 1 % de faux positifs (étalonnés sur transcriptions bénignes appariées), évaluée sur les N >= 240 cellules contre un nul de permutation."
   },
   "perte_traduction": "Remplace la preuve formelle binaire en Lean (« telle famille casse tel moniteur ») par un score de vulnérabilité ordinale sur une grille finie de cellules pré-existantes.",
   "questions_servies": [
    "Q3",
    "Q-pont",
    "Q1"
   ],
   "avantage": {
    "source": "methodes",
    "texte": "Scellement cryptographique avant toute lecture des données de test (R1), séparation stricte de la troisième instance qui fige la grille taxonomique (N-054), carte explicite des hypothèses des moniteurs, et refus de construire l'attaquant qui élimine toute contamination entre la conception du banc et la prédiction.",
    "incopiable_parce_que": "Un occupant qui construit ses attaques par itération contre des moniteurs de développement (SLEIGHT-Bench fait environ 10 itérations par transcription contre le moniteur ; MonitoringBench filtre ses raffinements sur 3 moniteurs de développement) consomme les degrés de liberté de ses catégories pendant la construction même du banc : ses catégories sont en partie a posteriori et ne peuvent plus jamais faire l'objet d'une prédiction aveugle préenregistrée sur ce banc."
   },
   "originalite": {
    "niveau": "inedite",
    "texte": "Transforme l'énumération qualitative et a posteriori d'angles morts (SLEIGHT-Bench 2026 ; Ptacek et Newsham 1998) et le test de transfert global (Storf et al. 2026 ; Kirch et al. 2025) en une épreuve de prévisionniste notée par cellule (moniteur × propriété), préenregistrée et contrôlée contre le hasard."
   },
   "demande_organisme": {
    "nature": "ajout",
    "texte": "Préalable obligatoire avant toute exécution de Q3 (réponse explicite au point 3 de la question : la troisième instance est un préalable immédiat à Q3 et au test final de Q4/Q-pont, mais pas au développement théorique de Q2 ni à l'instrumentation statique de Q6) : instancier la troisième instance (N-054) qui fige la grille des K cellules et l'opérateur synthétique de P_k sans accès à la carte des hypothèses ni aux moniteurs ; inutile d'attendre la couche 4 complète en Lean (des dérivations analytiques empreintées suffisent en étape 0)."
   },
   "cout": {
    "nature": "processeur",
    "ordre_de_grandeur": "Processeur seul pour la dérivation, le scellement et l'évaluation sur transcriptions publiques déjà scorées ; 50 à 200 dollars si calcul des scores de nos propres sondes sur les transcriptions publiques."
   },
   "piege": "Circularité par fuite des taux de détection publiés dans SLEIGHT-Bench ou MonitoringBench vers l'instance qui rédige les prédictions (si l'analyste connaît déjà que les catégories « N-hops » ou « Omission » sont à 0 % de détection dans SLEIGHT-Bench, la prédiction est contaminée), ou confusion avec la difficulté intrinsèque de la cellule si la permutation ne stratifie pas par taux de base.",
   "cosmetique_si": "Les prédictions issues de la carte des hypothèses ne battent pas un prédicteur naïf fondé sur la seule longueur de la transcription ou la perplexité moyenne, ou si la corrélation Q-pont est nulle sur toutes les propriétés P_k (ce qui invaliderait aussitôt Q1 et toute la voie synthétique).",
   "anteriorite": [
    {
     "reference": "SLEIGHT-Bench: A Benchmark of Evasion Attacks Against Agent Monitors, Najt, Toft, Tracy, Roger, Benton, 2026, arXiv:2605.16626v2",
     "statut": "RAPPORTE"
    },
    {
     "reference": "MonitoringBench: Semi-Automated Red-Teaming for Agent Monitoring, Jotautaite, Martinez, Matthews, Tracy, 2026, arXiv:2605.09684v1",
     "statut": "RAPPORTE"
    },
    {
     "reference": "The Impact of Off-Policy Training Data on Probe Generalisation, Kirch, Dower, Skapars, Yannakoudakis, Lubana, Krasheninnikov, 2025/2026, arXiv:2511.17408v4",
     "statut": "RAPPORTE"
    },
    {
     "reference": "Constitutional Black-Box Monitoring for Scheming in LLM Agents, Storf, Barton-Cooper, Peters-Gill, Hobbhahn, ICML 2026, arXiv:2603.00829v2",
     "statut": "RAPPORTE"
    },
    {
     "reference": "Simulated control evaluations, Olmo, Zhang, Tracy, Redwood Research, billet du 23 octobre 2026",
     "statut": "RAPPORTE"
    },
    {
     "reference": "Sim2Real Predictivity, Kadian et al., 2019, arXiv:1912.06321",
     "statut": "RAPPORTE"
    },
    {
     "reference": "Inherited Circuits, Learned Semantics, Fetterman, 2026, arXiv:2606.27091",
     "statut": "RAPPORTE"
    }
   ]
  },
  {
   "nom": "Nouvelle Q-N2 — Immunité des sondes introspectives à la subversion adaptative du moniteur",
   "type": "question",
   "enonce": "Alors que la pièce B écarte Q7 comme « la moins distinctive » parce qu'elle la lit comme un simple mélange pondéré après Bailey et al. (2025) et Parrack et al. (2025), nos extraits primaires révèlent une question oblique beaucoup plus forte au croisement de Terekhov et al. (2510.09462) et Hollinsworth et al. (2610.12445) : lorsque l'agent non fiable exécute une attaque adaptative qui subvertit directement le moniteur boîte noire par injection dans les sorties (effondrant l'aire sous la courbe ROC du moniteur textuel sous la diagonale, jusqu'à un score de 0 sur 375 exemples dans Terekhov et al.), une sonde boîte blanche mesurant le contraste d'affirmation introspective sur le flux résiduel de l'agent conserve-t-elle son pouvoir discriminant, et un protocole de contrôle qui aiguille l'audit ou le rééchantillonnage selon la discorde entre sonde interne et moniteur textuel élimine-t-il l'effet de retour de flamme du protocole Defer-to-Resample ?",
   "loi_predictive": {
    "espace_instances": "Trajectoires de BashBench, APPS et SHADE-Arena issues de ou évaluées selon le protocole public de Terekhov et al. (2510.09462) et Hollinsworth et al. (2610.12445) sur modèles à poids ouverts de 8 et 70 milliards de paramètres, N >= 300 épisodes avec et sans subversion du moniteur textuel (aucune nouvelle injection conçue : utilisation exclusive des traces et évaluations existantes ou d'une simulation analytique de corruption du score boîte noire).",
    "prediction": "Sur les épisodes où le score du moniteur boîte noire est subverti (rappel à 1 % de faux positifs tombant sous 10 %), la sonde de contraste introspectif sur les activations de l'agent (qui ne lit pas le texte comme une instruction) maintient une aire sous la courbe ROC supérieure à 0,90 ; un détecteur de discorde inter-canaux (sonde interne haute ET moniteur textuel anormalement bas) isole les tentatives de subversion du moniteur avec un rappel supérieur à 80 % à 1 % de faux positifs et restaure la monotonie de la sûreté du protocole Defer-to-Resample en fonction du nombre d'échantillons k.",
    "signe": "+",
    "metrique": "Écart de rappel à 1 % de faux positifs et d'aire sous la courbe ROC entre sonde interne et moniteur boîte noire sous subversion du moniteur, et probabilité de victoire de l'équipe bleue (Safety au budget d'audit c = 0,02) du protocole Defer-to-Resample aiguillé par la discorde contre le protocole standard."
   },
   "perte_traduction": "Ne teste pas une co-évolution simultanée sur 70 tours d'obfuscation latente ET d'injection textuelle (ce qui exigerait de construire un attaquant conjoint interdit par R-597), mais l'orthogonalité causale des deux canaux face à la subversion du canal textuel.",
   "questions_servies": [
    "Q7",
    "nouvelle"
   ],
   "avantage": {
    "source": "programme",
    "texte": "Accès simultané aux activations internes sur modèles à poids ouverts de 8 et 70 milliards de paramètres et au cadrage de contrôle séquentiel, tout en utilisant les résultats publiés de Terekhov et al. comme matériau sans jamais concevoir d'injection.",
    "incopiable_parce_que": "Terekhov et al. (2510.09462, section 2) supposent par axiome que l'équipe bleue n'a qu'un accès boîte noire à l'agent (modèles fermés GPT-5 et Claude Sonnet 4) et concluent que seules les politiques « Always-Defer » survivent ; à l'inverse, Hollinsworth et al. (2610.12445) entraînent des sondes boîte blanche mais n'évaluent ni la subversion adaptative du moniteur ni le retour de flamme des protocoles de rééchantillonnage."
   },
   "originalite": {
    "niveau": "inedite",
    "texte": "Première jonction entre la vulnérabilité systémique des protocoles de contrôle par subversion du moniteur (Terekhov et al. 2025/2026, où Defer-to-Resample se retourne contre le défenseur en sélectionnant le minimum des scores) et la détection boîte blanche par pré-remplissage contrastif (Hollinsworth et al. 2026) : utilise la causalité amont des états cachés de l'agent pour détecter que la sortie vise à tromper l'évaluateur aval."
   },
   "demande_organisme": {
    "nature": "modification",
    "texte": "Ajouter dans le répertoire d'opérateurs des proposeurs (couche 1) l'opérateur de score de discorde directionnelle (sonde interne moins moniteur textuel étalonné par rang) et le simulateur analytique du protocole Defer-to-Resample (calcul de sûreté de Terekhov et al., annexe B.2)."
   },
   "cout": {
    "nature": "processeur",
    "ordre_de_grandeur": "Processeur seul pour la simulation de protocole sur scores croisés ; 50 à 150 dollars de processeur graphique pour extraire les scores de sonde contrastive sur 300 trajectoires de 8 et 70 milliards de paramètres."
   },
   "piege": "Oublier l'effet « persona contextuelle » documenté par Hollinsworth et al. (section 5.2, cas bird-labs : l'aire sous la courbe tombe de 99,7 % à 75 % quand la question de suivi active une persona bénigne qui « croit » ne pas avoir de but caché), ou supposer que l'agent ne peut pas simultanément obfusquer ses activations (Bailey et al. 2025) si la tâche est simple.",
   "cosmetique_si": "Le score de la sonde interne chute en même temps que celui du moniteur textuel sur les trajectoires subverties, ou si le coût de faux positifs du détecteur de discorde absorbe tout le budget d'audit c = 0,02.",
   "anteriorite": [
    {
     "reference": "Adaptive Attacks on Trusted Monitors Subvert AI Control Protocols, Terekhov, Panfilov, Dzenhaliou, Gulcehre, Andriushchenko, Prabhu, Geiping, 2025/2026, arXiv:2510.09462v2",
     "statut": "RAPPORTE"
    },
    {
     "reference": "Caught in the Act: Probes Effectively Detect Sabotage and Catch Unverbalized Deception, Hollinsworth, Spies, Diriba, Gleave, Cundy, 2026, arXiv:2610.12445v1",
     "statut": "RAPPORTE"
    },
    {
     "reference": "Obfuscated Activations Bypass LLM Latent-Space Defenses, Bailey et al., 2025, arXiv:2412.09565v2",
     "statut": "RAPPORTE"
    },
    {
     "reference": "Benchmarking Deception Probes via Black-to-White Performance Boosts, Parrack, Hex, Nardo, 2025, arXiv:2507.12691",
     "statut": "RAPPORTE"
    },
    {
     "reference": "Building Production-Ready Probes For Gemini, Kramar et al., 2026, arXiv:2601.11516",
     "statut": "RAPPORTE"
    },
    {
     "reference": "RL-Obfuscation, Gupta et al., 2025, arXiv:2506.14261",
     "statut": "RAPPORTE"
    }
   ]
  },
  {
   "nom": "Nouvelle Q-N3 — Rupture du plafond de saturation des moniteurs par sélection à la sévérité",
   "type": "question",
   "enonce": "Storf et al. (2603.00829, sections 5.2 à 5.4) démontrent que l'optimisation de moniteurs (par recherche en grille, raffinement humain, optimiseurs automatiques GEPA/MIPROv2 ou réglage fin LoRA) sature très vite (autour de 0,85 à 0,86 d'aire sous la courbe partielle) et que pousser l'optimisation dégrade la généralisation en surajustant aux artefacts d'entraînement : remplacer la sélection par le score moyen en distribution par la boucle de notre organisme (sélection par la sévérité du test survécu sous juge figé à mise, recombinaison bisociative de contraintes et pénalité d'instabilité des coefficients sous rotation laissant une famille de côté) permet-il de franchir ce plafond de saturation sur ControlArena et SHADE-Arena ?",
   "loi_predictive": {
    "espace_instances": "Évolution d'architectures et de consignes de moniteurs sur N = 2 000 trajectoires d'entraînement (issues de pipelines synthétiques ou de FIBS) et évaluation scellée unique sur M >= 5 environnements tenus à l'écart de ControlArena / SHADE-Arena, en comparant à budget d'appels égal un optimiseur maximisant l'aire sous la courbe partielle en distribution (type GEPA/MIPROv2 de Storf et al. ou évolution gloutonne d'EvoDefense) et notre organisme sélectionnant par sévérité (−log de la probabilité de survie sous le nul informé).",
    "prediction": "Au-delà du budget de recherche en grille initiale (15 candidats), l'optimiseur standard stagne ou régresse sur les environnements tenus à l'écart (gain <= 0,01 d'aire sous la courbe partielle, répliquant Storf et al.), tandis que la sélection par sévérité combinée à la recombinaison bisociative continue d'améliorer la performance hors distribution d'au moins +0,05 d'aire sous la courbe partielle (ou +10 points de rappel à 1 % de faux positifs sur le pire environnement tenu à l'écart) sans dégradation entre les générations 2 et 10.",
    "signe": "+",
    "metrique": "Gain d'aire sous la courbe ROC partielle sur l'intervalle de faux positifs [0, 0,20] (métrique pAUROC de Storf et al.) et rappel à 1 % de faux positifs sur le pire environnement tenu à l'écart (protocole d'universalité normalisée par famille), en fonction du budget d'optimisation dépensé."
   },
   "perte_traduction": "Substitue à la question générale de l'universalité asymptotique de la machine (Q5, trop coûteuse en générations complètes × permutations d'ordre) un test ciblé de non-saturation sur un banc public où le plafond d'optimisation est déjà documenté.",
   "questions_servies": [
    "Q1",
    "Q5",
    "nouvelle"
   ],
   "avantage": {
    "source": "organisme",
    "texte": "Règle d'aptitude R3 propre à l'organisme (aptitude = sévérité du test survécu contre un nul informé et un nul d'archive, jamais l'ampleur du score positif), mémoire à empreinte prédictive refusant les redites, et recombinaison bisociative exigeant un contenu empirique accru.",
    "incopiable_parce_que": "Tous les optimiseurs des occupants (DSPy GEPA/MIPROv2 dans Storf et al., MO-ASHA/OpenEvolve dans Terekhov et al., ORPO dans EvoDefense, DGM-H dans HyperAgents) maximisent directement la métrique cible sur un jeu d'entraînement ou de validation réutilisé ; ils sont mathématiquement condamnés à exploiter la queue de bruit et les raccourcis du jeu synthétique dès que le budget d'optimisation dépasse quelques essais."
   },
   "originalite": {
    "niveau": "inedite",
    "texte": "Exploite l'impasse empirique majeure rapportée par Storf et al. (ICML 2026) et EvoDefense (2026, tableau 3 : régression à 5 tours) comme banc d'épreuve direct de notre mécanisme de sélection darwinienne à la sévérité (pièce F)."
   },
   "demande_organisme": {
    "nature": "rien",
    "texte": "Utilise tel quel le cœur de la pièce F (fiches d'hypothèses, gel, affinage sur développement, juge figé à sévérité, recombinaison bisociative) en prenant comme « fiches » des spécifications de moniteurs et comme « nul informé » le meilleur moniteur de la grille initiale plus un classifieur d'artefact de source."
   },
   "cout": {
    "nature": "depense",
    "ordre_de_grandeur": "Modeste : 150 à 500 dollars d'appels de modèles ou de calcul d'activations (budget apparié au réglage « light » de DSPy dans Storf et al.)."
   },
   "piege": "Inversion des classements selon le budget d'itération choisie (« Evolution or Illusion? », arXiv:2609.19799) : il faut préenregistrer toute la frontière budget × graines et ne lire le jeu de test final ControlArena qu'une seule fois en fin de course (N-050).",
   "cosmetique_si": "La courbe test de notre organisme plafonne exactement au même niveau que le simple balayage de 15 consignes (prompt sweep) de Storf et al.",
   "anteriorite": [
    {
     "reference": "Constitutional Black-Box Monitoring for Scheming in LLM Agents, Storf, Barton-Cooper, Peters-Gill, Hobbhahn, ICML 2026, arXiv:2603.00829v2",
     "statut": "RAPPORTE"
    },
    {
     "reference": "EvoDefense: Co-Evolving Black-Box Defense with Large Language Models, Li et al., 2026, arXiv:2605.31140v1",
     "statut": "RAPPORTE"
    },
    {
     "reference": "HyperAgents, Zhang, Zhao, Yang, Foerster, Clune, Jiang, Devlin, Shavrina, 2026, arXiv:2603.19461v1",
     "statut": "RAPPORTE"
    },
    {
     "reference": "Evolution or Illusion?, IBM, 2026, arXiv:2609.19799",
     "statut": "RAPPORTE"
    },
    {
     "reference": "Unforeseen Attack Robustness (UAR), Kang, Sun, Hendrycks, Brown, Steinhardt, 2019, arXiv:1908.08016",
     "statut": "RAPPORTE"
    }
   ]
  },
  {
   "nom": "Approche A1 — Évolution guidée par le support de désaccord sans étiquette (fusion Discern + Portfolio Vigilance)",
   "type": "approche",
   "enonce": "Transposer à notre juge figé et à l'affinage des proposeurs (pièce F) l'identité de support de Balachandran (2609.17560) combinée au mélange d'experts de Mondal et al. (2609.32267) : lors de l'évolution d'un moniteur candidat g face au moniteur en place f, observer gratuitement leur taux de désaccord sur un grand flux non étiqueté de trajectoires multi-familles (Palier 0 : rejet ou certification immédiate à zéro étiquette si le désaccord est hors bande), et ne dépenser le budget d'exposition du juge figé que sur les instances de désaccord (At = 1), en mixant à poids 1/2 un parieur guidé par la carte théorique des hypothèses (conseil non fiable au sens M2) et un parieur robuste n'apprenant que des étiquettes d'épreuve.",
   "loi_predictive": {
    "espace_instances": "Flux de M >= 200 candidats moniteurs générés par les proposeurs au fil des générations sur une banque d'épreuve de N >= 5 000 épisodes.",
    "prediction": "À garantie de fausses promotions identique (delta_seq <= 0,05 composée sur toute la suite de promotions par série en k^-2), la restriction au support de désaccord réduit la consommation d'unités d'épreuve scellées d'un facteur proportionnel à l'inverse du taux de désaccord (gain de 5 à 20 fois en longévité de la banque scellée avant épuisement), et le portefeuille 1/2-1/2 borne le regret de log-évidence à log(2) même lorsque la théorie conseillère est fausse.",
    "signe": "+",
    "metrique": "Nombre d'évaluations d'épreuve consommées par promotion certifiée, nombre total de générations soutenables avant renouvellement de la banque sœur (N-049), et taux empirique de fausses promotions sur témoins plantés."
   },
   "perte_traduction": "L'identité de support exacte exige une perte déterminée par la décision binaire au seuil fixé (rappel à 1 % de faux positifs) ; pour des scores continus d'aire sous la courbe ROC, elle ne s'applique qu'à travers la version relâchée Lipschitz (Proposition 14 de Balachandran), ce qui réduit le gain d'échantillonnage.",
   "questions_servies": [
    "Q2",
    "Q5",
    "Q4"
   ],
   "avantage": {
    "source": "methodes",
    "texte": "Économie radicale du budget d'épreuve scellée et du budget de calcul, permettant à un programme doté de quelques milliers de dollars de faire tourner 5 à 20 fois plus de générations certifiées qu'un laboratoire qui réévalue chaque candidat sur tout le banc.",
    "incopiable_parce_que": "Un occupant dont l'attaquant co-évolue change la distribution d'entrée à chaque génération, ce qui détruit la stationnarité du flux sous-jacent et invalide l'identité de support entre générations ; notre refus de construire l'attaquant maintient le vivier d'épreuve contrôlé et rend l'échantillonnage sur désaccord mathématiquement exact."
   },
   "originalite": {
    "niveau": "transposition",
    "texte": "Fusionne deux préimpressions statistiques de septembre 2026 (Discern, 2609.17560, et Portfolio Vigilance, 2609.32267, conçues pour le déploiement industriel d'une mise à jour unique ou en chaîne passive) pour en faire le moteur de sélection darwinienne d'un pôle de recherche automatique de moniteurs."
   },
   "demande_organisme": {
    "nature": "modification",
    "texte": "Sur processeur dans l'orchestrateur v7 du juge figé : ajouter le filtre de désaccord At = 1{f(Xt) != g(Xt)} au point de fonctionnement 1 % de faux positifs avant l'appel au juge d'épreuve, et remplacer la mise unique par la moyenne 1/2 Et^Théorie + 1/2 Et^Robuste."
   },
   "cout": {
    "nature": "processeur",
    "ordre_de_grandeur": "Coût de développement nul (quelques dizaines de lignes de Python dans le juge v7) ; gain net négatif en dépense (économise les appels d'évaluation)."
   },
   "piege": "Violer la condition de prévisibilité du routage (Lemme 3 de Balachandran) : la probabilité d'interroger l'épreuve pi_t doit dépendre uniquement du passé Ft-1 et des prédictions des moniteurs sur Xt, jamais d'un signal corrélé à l'étiquette vraie Yt non encore révélée, et doit respecter un plancher strict pi_min > 0.",
   "cosmetique_si": "Les moniteurs candidats proposés d'une génération à l'autre sont en désaccord sur plus de 50 % des exemples au seuil de 1 % de faux positifs (auquel cas rho est proche de 1 et le gain d'échantillonnage disparaît).",
   "anteriorite": [
    {
     "reference": "Pay Only for Disagreement: Certified No-Regression Verdicts for Model Updates with Matching Label-Complexity Bounds, Balachandran, 2026, arXiv:2609.17560v1",
     "statut": "RAPPORTE"
    },
    {
     "reference": "When Can Old Evaluations Certify a New Model? Label-Efficient Release Decisions under Evaluator Drift, Mondal, Banik, Apurba, Mahmud, 2026, arXiv:2609.32267v1",
     "statut": "RAPPORTE"
    },
    {
     "reference": "Estimating means of bounded random variables by betting, Waudby-Smith, Ramdas, JRSS-B 2024",
     "statut": "RAPPORTE"
    }
   ]
  },
  {
   "nom": "Approche A2 — Opérateur de dilution et de greffe contrefactuelle sans attaquant (emprunt à la métrologie)",
   "type": "approche",
   "enonce": "Pour alimenter Q4, Q-pont et Q1 sans jamais construire ni exécuter d'agent attaquant (respect absolu de R-597 et R-611), remplacer l'équipe rouge par un opérateur purement mécanique de chirurgie de traces et d'états cachés : à partir d'une paire (trajectoire bénigne, trajectoire de sabotage issue d'un banc public figé comme ControlArena, SHADE-Arena ou FIBS) du même modèle sur la même tâche principale, construire un continuum paramétrique d'instances par (i) dilution temporelle (insertion de K pas bénins authentiques du même agent entre deux pas liés au sabotage, à dommage final identique) et (ii) interpolation ou greffe de sous-espaces d'activations (remplacement de la composante orthogonale au sous-espace d'identité de jeu de données de Fomin à intensité contrôlée alpha dans [0, 1]), étalonné comme une courbe dose-réponse en métrologie.",
   "loi_predictive": {
    "espace_instances": "Grille paramétrique (K, alpha) appliquée à N >= 200 paires de trajectoires (bénigne, sabotage) appariées par tâche et par modèle agent sur 8 et 70 milliards de paramètres.",
    "prediction": "La dose médiane de détection (ED50 : valeur de K ou de 1/alpha à laquelle le rappel à 1 % de faux positifs passe sous 50 %) mesurée sur ce banc purement mécanique prédit avec une corrélation de rang supérieure à 0,75 le classement de robustesse des moniteurs sur les attaques graduelles et multi-agents tenues à l'écart de Hills et al. et d'Angelini, Makins et al., tout en ramenant la séparabilité d'identité de source (classifieur de jeu de données de Fomin) de plus de 90 % à moins de 55 %.",
    "signe": "+",
    "metrique": "Corrélation de rang entre la dose médiane de détection (ED50) sur l'opérateur mécanique et le taux d'évasion sur bancs diffus externes, et précision d'un classifieur d'identité de source entre paires bénignes et greffées."
   },
   "perte_traduction": "Ne capture pas l'invention de nouvelles stratégies sémantiques de couverture par l'agent (puisque les briques élémentaires proviennent de traces figées).",
   "questions_servies": [
    "Q4",
    "Q-pont",
    "Q6",
    "Q1"
   ],
   "avantage": {
    "source": "programme",
    "texte": "Réconcilie la contrainte de sûreté R-597 (zéro génération d'attaque nouvelle, zéro refus de modèle de frontière, coût processeur) avec le besoin d'avoir un bouton continu de difficulté et de dilution (gamma * D) ainsi qu'une annulation par construction de l'artefact de source.",
    "incopiable_parce_que": "Les occupants qui reposent sur l'élicitation de modèles de frontière subissent un biais de sélection massif (Hills et al. notent en section 4.1 et 6 que leurs attaques graduelles réussies concentrent en réalité l'attaque en 1 ou 2 requêtes et que Opus 4.6 refuse d'attaquer ; Storf et al. jettent 49 % des trajectoires où la tâche secondaire échoue). Notre opérateur mécanique contrôle exactement la dilution K sans perte ni refus."
   },
   "originalite": {
    "niveau": "inedite",
    "texte": "Transpose le titrage dose-réponse de la métrologie analytique et l'étalonnage contrefactuel apparié (Kirch et al. 2025 ; Fomin 2026) à la génération de bancs d'épreuve séquentiels pour moniteurs d'agents, sans aucun appel de modèle générateur."
   },
   "demande_organisme": {
    "nature": "ajout",
    "texte": "Un script Python pur sur processeur dans le module de préparation des banques de développement et d'épreuve (découpage d'étapes JSONL et algèbre linéaire sur tenseurs d'activations mis en cache)."
   },
   "cout": {
    "nature": "processeur",
    "ordre_de_grandeur": "Zéro dollar (calcul matriciel sur processeur à partir des transcriptions et activations déjà extraites)."
   },
   "piege": "Créer des discontinuités syntaxiques ou temporelles aux points de greffe des pas bénins, qu'un moniteur détecterait comme une anomalie de cohérence plutôt que comme du sabotage (à contrôler par un témoin « greffe bénin-dans-bénin » qui doit rester à 1 % de faux positifs).",
   "cosmetique_si": "Un moniteur boîte noire ou une sonde distingue la greffe « bénin-dans-bénin » de la trace bénigne originale à un taux supérieur à 5 % pour un seuil étalonné à 1 %.",
   "anteriorite": [
    {
     "reference": "When Benchmarks Lie: Evaluating Malicious Prompt Classifiers Under True Distribution Shift, Fomin, 2026, arXiv:2602.14161v2",
     "statut": "RAPPORTE"
    },
    {
     "reference": "The Impact of Off-Policy Training Data on Probe Generalisation, Kirch et al., 2025/2026, arXiv:2511.17408v4",
     "statut": "RAPPORTE"
    },
    {
     "reference": "Distributed Attacks in Persistent-State AI Control, Hills, Caspary, Cooper Stickland, 2026, arXiv:2607.02514v2",
     "statut": "RAPPORTE"
    },
    {
     "reference": "Constitutional Black-Box Monitoring for Scheming in LLM Agents, Storf et al., ICML 2026, arXiv:2603.00829v2",
     "statut": "RAPPORTE"
    }
   ]
  },
  {
   "nom": "Approche A3 — Détournement de l'organisme en auditeur adversarial des courbes publiées (méta-benchmarking)",
   "type": "approche",
   "enonce": "Plutôt que d'entrer dans la course en entraînant un n-ième défenseur sur HarmBench ou Agent-SafetyBench (terrain saturé où EvoSafety revendique déjà 99,61 % et SafeCoEvo 94,33 %), pointer les proposeurs de notre organisme (sortie 5 de la pièce F : « failles du programme actuel ») sur les dépôts, points de contrôle et journaux publiés des occupants (SafeCoEvo, EvoSafety, AgentSafeEvo, MAGIC, FIBS, MonitoringBench) pour générer et certifier sous juge figé des fiches de réfutation méthodologique (« le gain publié du système X entre le tour 1 et le tour T tombe de Y % lorsqu'on applique le contrôle C »).",
   "loi_predictive": {
    "espace_instances": "Journaux d'évaluation, banques de mémoire vérifiée et modèles de garde publiés d'au moins K = 4 occupants à code ouvert (SafeCoEvo, EvoSafety, MAGIC, Fomin/FIBS), testés par des fiches d'ablation générées et affinées automatiquement par nos proposeurs.",
    "prediction": "Sur au moins 3 des 4 systèmes audités, l'organisme découvre en moins de 5 générations sur processeur un contrôle de rigueur omis (substitution du juge-modèle partagé par un juge d'une autre famille comme dans l'annexe D.3 de MAGIC où les distributions de scores divergent de 0,24 à 0,49 ; retrait des raccourcis de jeu de données ; évaluation au point de fonctionnement à 1 % de faux positifs sur bénins appariés du même modèle au lieu du taux d'erreur global) qui réduit l'amélioration co-évolutive revendiquée d'au moins 40 % en valeur relative.",
    "signe": "+",
    "metrique": "Réduction relative certifiée (avec intervalle de confiance valable à tout instant) du gain co-évolutif déclaré par les occupants sous les contrôles générés par l'organisme, et taux de survie de notre propre défense sous les mêmes fiches d'audit."
   },
   "perte_traduction": "Déplace une partie de la contribution d'une performance brute de détection vers une norme métrologique et un audit de reproductibilité du domaine (tout en servant de filtre dur pour nos propres moniteurs).",
   "questions_servies": [
    "Q6",
    "Q2",
    "Q5",
    "nouvelle"
   ],
   "avantage": {
    "source": "organisme",
    "texte": "L'architecture à castes contradictoires (expérimentateur d'une lignée, vérificateur neuf d'une autre lignée, juge figé hors des agents, sortie 5 d'auto-critique mécanique) transforme les publications des concurrents en matériau gratuit pour notre organisme.",
    "incopiable_parce_que": "Un laboratoire auteur de SafeCoEvo, MAGIC ou EvoSafety ne publiera jamais un audit automatique montrant que sa boucle co-évolutive exploite son propre évaluateur ou ses artefacts de partitionnement ; et un laboratoire tiers sans notre organisme à vérification croisée et juge certifié ne peut pas produire d'enregistrements de preuve vérifiables par machine à la chaîne."
   },
   "originalite": {
    "niveau": "inedite",
    "texte": "Réoriente un système « scientifique automatique » (au sens de Sakana AI Scientist ou Agent Laboratory, corrigé par nos gardes de gel et de juge externe de la pièce F) vers l'audit méthodologique automatisé et préenregistré des systèmes de sécurité co-évolutifs."
   },
   "demande_organisme": {
    "nature": "modification",
    "texte": "Dans la couche 1 (pièce F), ouvrir un répertoire en lecture seule dans le bac à sable contenant les artéfacts publics des occupants (journaux JSON, poids de gardes légers 3B/4B, prédictions) et paramétrer le gabarit de fiche « sortie 5 — faille méthodologique »."
   },
   "cout": {
    "nature": "processeur",
    "ordre_de_grandeur": "Processeur seul pour la ré-analyse des journaux et des partitions ; moins de 100 dollars pour réévaluer les petits modèles de garde ouverts (Llama-3.2-3B d'EvoSafety, Qwen-3-4B d'EvoDefense)."
   },
   "piege": "Passer pour de la critique purement négative si l'on n'applique pas exactement les mêmes fiches de réfutation à nos propres moniteurs évolués (sur Q4 et Q-N2) pour démontrer qu'ils y survivent.",
   "cosmetique_si": "Les gains co-évolutifs des occupants restent inchangés (à moins de 5 % près) sous juge externe indépendant, sous témoins bénins appariés du même générateur et sous protocole laissant une famille de côté.",
   "anteriorite": [
    {
     "reference": "When Lie Detectors Learn Model Identity: Confounds in Black-Box Sandbagging Detection, Lin et al., ICLR 2026",
     "statut": "RAPPORTE"
    },
    {
     "reference": "When Benchmarks Lie: Evaluating Malicious Prompt Classifiers Under True Distribution Shift, Fomin, 2026, arXiv:2602.14161v2",
     "statut": "RAPPORTE"
    },
    {
     "reference": "Dos and Don'ts of Machine Learning in Computer Security, Arp et al., USENIX Security 2022",
     "statut": "RAPPORTE"
    },
    {
     "reference": "MAGIC: A Co-Evolving Attacker-Defender Adversarial Game for Robust LLM Safety, Wen et al., 2026, arXiv:2602.01539v2",
     "statut": "RAPPORTE"
    },
    {
     "reference": "SafeCoEvo: Co-Evolving Safety Harnesses and Guards for LLM Agents at Test-Time, Cheng et al., 2026, arXiv:2609.36580v2",
     "statut": "RAPPORTE"
    },
    {
     "reference": "EvoSafety: Model-Agnostic Lifelong LLM Safety via Externalized Attack-Defense Co-Evolution, Zhang et al., 2026, arXiv:2605.13411v1",
     "statut": "RAPPORTE"
    }
   ]
  }
 ]
}
```