```json
{
 "fiches": [
  {
   "nom": "Q4 — Le diffus comme axe d'universalité séparé sous borne d'horizon",
   "type": "question",
   "enonce": "En désaccord avec la pièce B (qui relègue Q4 à l'étape 2 et subordonne tout à Q3 sur une dizaine de familles puis à Q-pont), Q4 est LA question centrale du programme : un moniteur (sonde d'activations internes et/ou boîte noire) évolué sur des menaces concentrées échoue-t-il au transfert vers des menaces diffuses à dommage total constant selon la loi de transition asymptotique, et la combinaison boîte blanche inter-épisodes plus agrégation séquentielle par processus de pari restaure-t-elle ce transfert sur des familles tenues à l'écart ?",
   "loi_predictive": {
    "espace_instances": "Séquences multi-épisodes ou multi-agents obtenues par dilution paramétrique (facteur K de 1 à 9 épisodes ou requêtes de fusion) de trajectoires issues de bancs publics (ControlArena, SHADE-Arena, Iterative Vibe Coding, FakeLab), N >= 300 séquences par niveau de K, évaluées sur modèles à poids ouverts de 8 et 70 milliards de paramètres.",
    "prediction": "Sous règle de décision par instant, le rappel d'un moniteur évolué sur du concentré chute avec le facteur de dilution K et le délai moyen de détection bascule de O(log gamma) à Theta(gamma) dès que le produit de la contrainte de fausse alarme gamma par la divergence de Kullback-Leibler par pas franchit le seuil critique O(1) ; à scores d'activations identiques, le remplacement du seuil par instant par un processus de pari séquentiel inter-épisodes abaisse le taux d'évasion graduelle d'au moins 25 points de pourcentage à taux de fausses alertes fixé à 1 %.",
    "signe": "-",
    "metrique": "Pente du rappel (et du taux d'évasion) en fonction du facteur de dilution K à taux de fausses alertes fixé à 1 % par séquence sur familles diffuses tenues à l'écart, normalisée par famille selon la robustesse aux attaques imprévues (Unforeseen Attack Robustness), et erreur quadratique vis-à-vis de l'asymptotique théorique de Ramtin, Nain et Towsley."
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
    "incopiable_parce_que": "Les occupants du diffus (Terekhov et al., Angelini et Makins et al., Hills et al.) opèrent à 100 % en boîte noire sur modèles fermés par interface de programmation et couplent leur évaluation à l'élicitation d'un attaquant (sujette aux refus des modèles de frontière et au biais de sélection des attaques réussies). Reproduire notre mesure exige d'extraire les états cachés inter-épisodes sur 70 milliards de paramètres et d'abandonner la co-évolution d'invites d'attaque au profit d'un découpage paramétrique sous juge figé."
   },
   "originalite": {
    "niveau": "transposition",
    "texte": "Transpose la théorie asymptotique de la détection de changement le plus rapide face à un adversaire furtif (Ramtin, Nain et Towsley 2025/2026) aux moniteurs d'agents (boîte blanche et boîte noire) en co-évolution défensive. Les constats boîte noire statiques existent (Hills et al. 2026 ; Angelini, Makins et al. 2026), et Terekhov et al. (2026) font évoluer une instruction de juge faible en boîte noire sur tâches floues sans agrégation séquentielle ni boîte blanche."
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
   "nom": "Nouvelle Q-N1 (fusion Q2 + Q6) — Loi de dégradation de Goodhart des boucles co-évolutives",
   "type": "question",
   "enonce": "Contre l'hésitation de la pièce B sur Q2 (hygiène ou résultat) et son report de Q6, on les fusionne en une entrée oblique : dans les boucles de sélection de moniteurs utilisant un juge-modèle partagé ou une validation en distribution non garantie (protocoles de SafeCoEvo, AgentSafeEvo, MAGIC, EvoDefense, EvoSafety), quelle fraction du gain déclaré au fil des générations G est une fausse promotion (rejugée par processus de pari) ou une dérive vers l'artefact de source (mesurée par la compétition entre distance de mécanisme et distance de surface), et notre juge figé garanti à témoins plantés annule-t-il cette dérive ?",
   "loi_predictive": {
    "espace_instances": "Deux volets : (a) ré-analyse sans exécution des courbes de promotion publiées par les occupants (SafeCoEvo 15 époques, MAGIC 200 pas, AgentSafeEvo, EvoDefense 10 tours, EvoSafety) ; (b) exécution comparative de trois régimes de jugement sur notre propre boucle pendant G = 20 générations sur un corpus multi-sources (FIBS 28 familles, MonitoringBench, Agent-SafetyBench, les 18 jeux de Fomin) en rotation laissant une famille de côté.",
    "prediction": "En volet (a), plus de 40 % des améliorations par tour rapportées par les occupants sans garantie statistique échouent au seuil d'arrêt valable à tout instant (alpha = 0,05) ou s'inversent après l'époque optimale choisie en distribution (comme l'époque 13 de SafeCoEvo). En volet (b), sous juge-modèle partagé ou validation en distribution, l'écart entre gain en distribution et gain sous témoins bénins appariés du même générateur croît d'au moins 10 points de pourcentage en 20 générations et la rétention des coefficients r_j chute sous 0,5 pour plus de 30 % des traits, tandis que sous notre juge figé garanti le taux de fausses promotions sur témoins nuls plantés reste borné par 5 %.",
    "signe": "+",
    "metrique": "Fraction de promotions publiées survivant à une séquence de confiance de Ville (alpha = 0,05), écart cumulé de rappel à 1 % de faux positifs entre validation interne et protocole laissant une famille de côté avec témoins bénins du même modèle, et rétention des coefficients r_j par génération."
   },
   "perte_traduction": "Ramène la diversité des architectures co-évolutives publiées (apprentissage par renforcement multi-agents, optimisation de préférences, mémoire externe) à la seule statistique de sélection et de filtrage d'artefacts de leur évaluateur.",
   "questions_servies": [
    "Q2",
    "Q6",
    "Q5",
    "nouvelle"
   ],
   "avantage": {
    "source": "organisme",
    "texte": "L'organisme dispose déjà en production (pièce F, démonstration couche 1 v7) du juge figé à mise contre bibliothèque de nuls avec borne de Ville, des témoins plantés (vrais et faux), de l'empreinte prédictive de la mémoire et du pare-feu N-053 (aucun score du juge dans l'entraînement ou la sélection).",
    "incopiable_parce_que": "Les occupants ont un conflit d'intérêt structurel : leurs gains publiés (choix du point de contrôle époque 13 sur la même validation dans SafeCoEvo ; usage de Qwen3Guard ou Qwen3.8-27B à la fois comme récompense d'entraînement et comme juge d'évaluation dans MAGIC, EvoSafety et AgentSafeEvo) reposent sur le couplage que cette question mesure. Appliquer notre juge figé garanti et nos témoins du même générateur invaliderait rétroactivement leurs courbes de progrès."
   },
   "originalite": {
    "niveau": "transposition",
    "texte": "Combine la certification séquentielle de mises à jour par séquences de confiance et processus de pari (Balachandran 2026 ; Mondal et al. 2026, qui n'ont ni boucle évolutive de moniteurs ni contrôle d'artefact) avec le diagnostic d'artefact de source sous rotation laissant un jeu de côté (Fomin 2026 ; Lin et al. 2026) pour mesurer la dérive dynamique d'une boucle (voisin en vision : Pathak et al. 2023)."
   },
   "demande_organisme": {
    "nature": "modification",
    "texte": "Sur processeur seul : brancher le bras « fuite textuelle » (N-053 point 1), le calcul de rétention des coefficients r_j (Fomin) et l'export de l'empreinte de mémoire à chaque génération de la boucle existante de la pièce F, plus un adaptateur lisant les tableaux publiés des occupants."
   },
   "cout": {
    "nature": "processeur",
    "ordre_de_grandeur": "Entièrement sur processeur pour le rejugement des courbes publiées et l'exécution sur activations et scores précalculés."
   },
   "piege": "Croire que la borne de Ville sur le jeu du juge garantit à elle seule la généralisation hors distribution (réserve C mineur de la pièce B : la borne contrôle les fausses promotions sur la loi du juge ; sans rotation des familles et témoins bénins appariés du même générateur, un juge figé certifie un raccourci de jeu de données).",
   "cosmetique_si": "Plus de 80 % des promotions publiées survivent à la borne séquentielle et la sélection en distribution de type SafeCoEvo ne produit pas plus de fausses promotions sur les témoins plantés ni plus de dérive de rétention r_j que le juge figé garanti.",
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
     "reference": "Sequential Training of GANs Against GAN-Classifiers Reveals Correlated Knowledge Gaps, Pathak et al., CVPR 2023",
     "statut": "RAPPORTE"
    }
   ]
  },
  {
   "nom": "Q3 + Q-pont fusionnées — Prédiction préenregistrée des angles morts par cellule (moniteur × propriété) contre témoin géométrique",
   "type": "question",
   "enonce": "Pour lever l'objection 1a (manque de puissance statistique de Q3 sur une dizaine de familles et dépendance séquentielle de Q-pont), la carte théorique des hypothèses des moniteurs prédit-elle a priori et sous scellement cryptographique, sur la matrice croisée de M moniteurs distincts et K cellules taxonomiques tenues à l'écart, à la fois (i) le classement des taux d'échec mieux qu'un prédicteur géométrique sans théorie (cartographie antigénique de la matrice de développement), et (ii) la corrélation de rang entre épisodes synthétiques sans attaquant portant la propriété P_k et épisodes semi-réalistes portant P_k ?",
   "loi_predictive": {
    "espace_instances": "Produit cartésien de M >= 8 moniteurs (sondes linéaires, sondes multicouches, autoencodeurs parcimonieux, moniteurs boîte noire par étape et par trajectoire, agrégateurs CUSUM) par K >= 30 cellules d'angles morts (issues de l'union figée par la troisième instance de SLEIGHT-Bench 11 catégories, MonitoringBench T1-T5 × S1-S4 × E1-E4, et FIBS 28 familles), soit N >= 240 paires (moniteur, cellule) évaluées une seule fois après gel.",
    "prediction": "La corrélation de rang de Spearman entre la vulnérabilité prédite par la carte des hypothèses et le taux d'évasion observé dépasse 0,45 (valeur p < 0,001 par test de permutation stratifié par moniteur et par taux de base) et bat d'au moins 0,10 le bras témoin géométrique sans théorie ; pour Q-pont, la corrélation synthétique-réel dépasse 0,70 sur les propriétés textuellement explicites, chute sous 0,30 sur les propriétés textuellement ambiguës pour les moniteurs boîte noire, mais reste supérieure à 0,60 pour les sondes d'activations introspectives.",
    "signe": "+",
    "metrique": "Corrélation de rang de Spearman (et écart de score de Brier contre le témoin géométrique et le hasard) entre prédictions scellées et rappels observés à 1 % de faux positifs (étalonnés sur transcriptions bénignes appariées), sur les N >= 240 cellules."
   },
   "perte_traduction": "Remplace la preuve formelle binaire en Lean (« telle famille casse tel moniteur ») par un score de vulnérabilité ordinale sur une grille finie de cellules pré-existantes.",
   "questions_servies": [
    "Q3",
    "Q-pont",
    "Q1"
   ],
   "avantage": {
    "source": "methodes",
    "texte": "Scellement cryptographique avant toute lecture des données de test (R1), séparation stricte de la troisième instance qui fige la grille taxonomique (N-054), carte explicite des hypothèses opposée à un témoin géométrique (R4), et refus de construire l'attaquant qui élimine toute contamination entre la conception du banc et la prédiction.",
    "incopiable_parce_que": "Un occupant qui construit ses attaques par itération contre des moniteurs de développement (SLEIGHT-Bench fait environ 10 itérations par transcription contre le moniteur ; MonitoringBench filtre ses raffinements sur 3 moniteurs de développement) consomme les degrés de liberté de ses catégories pendant la construction même du banc : ses catégories sont en partie a posteriori et ne peuvent plus jamais faire l'objet d'une prédiction aveugle préenregistrée sur ce banc."
   },
   "originalite": {
    "niveau": "inedite",
    "texte": "Transforme l'énumération qualitative et a posteriori d'angles morts (SLEIGHT-Bench 2026 ; Ptacek et Newsham 1998) et le test de transfert global (Storf et al. 2026 ; Kirch et al. 2025) en une épreuve de prévisionniste notée par cellule (moniteur × propriété), préenregistrée et contrôlée contre un témoin de cartographie géométrique."
   },
   "demande_organisme": {
    "nature": "ajout",
    "texte": "Réponse explicite au point 3 de la question : la troisième instance (N-054) est un préalable immédiat à Q3 et au scellement de Q-pont (elle doit fixer la grille des K cellules et les traits déclarés sans voir la carte des hypothèses ni les moniteurs), mais elle n'est PAS un préalable aux travaux théoriques de Q2/Q4 ni au rejugement de Q-N1. Inutile d'attendre Lean (couche 4) : des contrats hypothèse-garantie analytiques empreintés suffisent en étape 0."
   },
   "cout": {
    "nature": "processeur",
    "ordre_de_grandeur": "Processeur seul pour la dérivation, le scellement, le témoin géométrique et l'évaluation sur transcriptions publiques déjà scorées ; 50 à 200 dollars si calcul des scores de nos propres sondes sur ces transcriptions."
   },
   "piege": "Circularité par fuite des taux de détection déjà publiés dans SLEIGHT-Bench ou MonitoringBench vers l'instance qui rédige les prédictions (si l'analyste sait déjà que « N-hops » ou « Omission » sont à 0 % dans SLEIGHT-Bench, la prédiction est contaminée : il faut donc soit masquer les noms de catégories et ne donner que les contrats formels, soit inclure dans les 240 cellules nos propres sondes boîte blanche jamais testées sur SLEIGHT-Bench).",
   "cosmetique_si": "Les prédictions issues de la carte des hypothèses ne battent pas le prédicteur géométrique sans théorie (cartographie par factorisation de la matrice de développement) ou un prédicteur naïf fondé sur la longueur de la transcription, ou si la corrélation Q-pont est nulle sur toutes les propriétés P_k (ce qui écarte immédiatement Q1).",
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
     "reference": "Mapping the antigenic and genetic evolution of influenza virus, Smith et al., Science 2004",
     "statut": "SUPPOSE"
    }
   ]
  },
  {
   "nom": "Nouvelle Q-N2 — Masse cachée d'évasion et plafond de couverture par capture-recapture inter-canaux",
   "type": "question",
   "enonce": "Au lieu de traiter Q7 (dynamique du mélange boîte blanche / boîte noire, posable par tout laboratoire) et Q5 (coût de la boucle, cher en générations) comme des questions ordinaires, on les remplace par la question oblique que le domaine attend sans pouvoir la poser : sur un flux d'épisodes tenus à l'écart ou non étiquetés, le recouvrement des détections entre canaux mécanistiquement orthogonaux (sonde d'activations introspectives sur poids ouverts contre moniteur d'actions boîte noire) permet-il d'estimer par capture-recapture et modèles à classes latentes la « masse cachée » d'épisodes de sabotage qui échappent simultanément à tous les moniteurs, et cette masse cachée décroît-elle au fil des générations de notre organisme ?",
   "loi_predictive": {
    "espace_instances": "Triplets d'évaluateurs aux mécanismes disjoints — (1) sonde d'activations sur question de suivi pré-remplie type FIBS, (2) moniteur boîte noire par trajectoire ou par différence de code, (3) agrégateur séquentiel inter-épisodes — appliqués à K >= 15 familles tenues à l'écart (concentrées et diffuses) contenant une fraction connue mais masquée de témoins positifs plantés, sur G >= 5 générations.",
    "prediction": "Calibré par les témoins plantés pour corriger la dépendance résiduelle entre canaux, l'estimateur de capture-recapture (Chao / classes latentes de Hui-Walter) prédit le taux réel de faux négatifs conjoints (la masse cachée) avec une erreur absolue médiane inférieure à 8 points de pourcentage et une corrélation de rang supérieure à 0,65 entre familles ; la masse cachée estimée est au moins 1,5 fois plus élevée sur les familles diffuses que sur les familles concentrées, et décroît significativement de la génération 0 à la génération G.",
    "signe": "+",
    "metrique": "Erreur absolue et corrélation de rang entre la masse cachée estimée sans étiquettes de vérité et le taux réel d'évasion conjointe sur l'épreuve à 1 % de faux positifs, plus la pente de cette masse cachée en fonction du rang de génération."
   },
   "perte_traduction": "L'indépendance conditionnelle parfaite entre la sonde interne et le moniteur textuel est violée si l'évasion latente modifie aussi le comportement visible (RL-Obfuscation rapporte qu'environ 70 % de la baisse de rappel vient d'un changement visible) ; l'estimateur fournit donc un indicateur étalonné par témoins et une borne inférieure, pas une identité exacte sans témoins.",
   "questions_servies": [
    "Q7",
    "Q5",
    "Q4",
    "Q-pont",
    "nouvelle"
   ],
   "avantage": {
    "source": "programme",
    "texte": "Nécessite simultanément les deux canaux sur poids ouverts de 8 et 70 milliards de paramètres (programme : un occupant boîte noire n'a qu'un seul canal textuel ; Bailey et al. n'ont que le canal latent), les témoins plantés à prévalence connue pour étalonner le biais de dépendance (organisme), et l'évaluation sur familles non générées par nous (méthodes).",
    "incopiable_parce_que": "Un occupant qui construit l'attaquant évalue sa défense sur les attaques que son propre générateur a réussi à produire (avec un fort effondrement de modes : MonitoringBench montre que 81 % des attaques élicitées tombent dans 2 niveaux techniques sur 5) ; il mesure un taux de capture conditionnel à son générateur et ne peut structurellement pas estimer la masse cachée hors de son générateur."
   },
   "originalite": {
    "niveau": "inedite",
    "texte": "Transpose les estimateurs écologiques et épidémiologiques de population cachée (capture-recapture de Chao 1984/1987 ; évaluation diagnostique sans étalon-or de Hui et Walter 1980 ; découverte d'espèces en test logiciel de Böhme 2018) à la fusion boîte blanche / boîte noire en contrôle des intelligences artificielles, transformant l'ensemble de moniteurs en instrument de mesure de ce que l'ensemble manque."
   },
   "demande_organisme": {
    "nature": "ajout",
    "texte": "Sur processeur : un module statistique d'estimation de masse cachée (estimateur de Chao avec correction de dépendance par témoins plantés et modèle à classes latentes à 3 listes) branché sur les sorties binaires des canaux à 1 % de faux positifs."
   },
   "cout": {
    "nature": "processeur",
    "ordre_de_grandeur": "Processeur seul sur les scores boîte blanche et boîte noire déjà extraits pour Q4 et Q3 (zéro dépense additionnelle)."
   },
   "piege": "Sous-estimer la masse cachée à cause d'une corrélation positive non corrigée entre canaux (biais rassurant, le plus dangereux en sûreté) : parade obligatoire en stratifiant par longueur et perplexité et en vérifiant que l'estimateur retrouve le nombre exact de témoins plantés aveugles avant toute lecture sur le test.",
   "cosmetique_si": "L'estimateur de masse cachée ne prédit pas mieux le taux d'échec sur l'épreuve qu'une simple constante proportionnelle au taux de détection du meilleur canal seul, ou si l'erreur sur les témoins plantés dépasse la variance inter-familles.",
   "anteriorite": [
    {
     "reference": "Nonparametric Estimation of the Number of Classes in a Population, Chao, Scandinavian Journal of Statistics 1984",
     "statut": "SUPPOSE"
    },
    {
     "reference": "Estimating the Error Rates of Diagnostic Tests, Hui, Walter, Biometrics 1980",
     "statut": "SUPPOSE"
    },
    {
     "reference": "STADS: Software Testing as Species Discovery, Böhme, ACM Transactions on Software Engineering and Methodology 2018",
     "statut": "SUPPOSE"
    },
    {
     "reference": "Obfuscated Activations Bypass LLM Latent-Space Defenses, Bailey et al., 2025, arXiv:2412.09565v2",
     "statut": "RAPPORTE"
    },
    {
     "reference": "RL-Obfuscation, Gupta et al., 2025, arXiv:2506.14261",
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
     "reference": "Caught in the Act: Probes Effectively Detect Sabotage and Catch Unverbalized Deception, Hollinsworth et al., 2026, arXiv:2610.12445v1",
     "statut": "RAPPORTE"
    }
   ]
  },
  {
   "nom": "Nouvelle Q-N3 — Péché antigénique originel et hystérésis d'ordre dans l'héritage de la boucle",
   "type": "question",
   "enonce": "Alors que la pièce B met Q5 en réserve à cause du coût de nombreuses générations et que HyperAgents (2603.19461) occupe déjà « évaluer le méta-agent », notre organisme récompense explicitement l'héritage sur K >= 3 générations (N-045-v2) : cet héritage induit-il un « péché antigénique originel » (une défense héritée généralise moins bien qu'une défense repartie de zéro à budget égal lorsqu'elle rencontre une famille à distance de mécanisme intermédiaire de sa famille fondatrice, et rend le point d'arrivée dépendant de l'ordre de présentation des familles) ?",
   "loi_predictive": {
    "espace_instances": "Paires appariées par graine (boucle avec héritage récompensé N-045-v2 et mémoire active contre boucle sans héritage repartant du moniteur initial à budget d'appels égal) exposées à des suites courtes de 3 à 4 familles d'attaque ordonnées selon deux permutations inverses (concentré -> diffus contre diffus -> concentré ; ou famille A -> B -> C contre C -> B -> A) et évaluées sur des familles tenues à l'écart situées à distance de mécanisme proche, intermédiaire ou lointaine.",
    "prediction": "Dans la bande de distance de mécanisme intermédiaire (où la nouvelle famille partage les traits de surface ou une partie des couches activées mais viole une clause adjacente de la carte des hypothèses), la défense héritée accuse un déficit de rappel d'au moins 5 points de pourcentage à 1 % de faux positifs par rapport à la défense sans héritage à budget égal (courbe non monotone en U), et la permutation de l'ordre d'exposition déplace le rappel final par famille de plus de 8 points de pourcentage.",
    "signe": "-",
    "metrique": "Différence appariée de rappel à 1 % de faux positifs (héritée moins neuve à budget égal) stratifiée en trois bandes de distance de mécanisme (proche, intermédiaire, lointaine), et norme L1 de l'écart de performance finale entre deux permutations inverses de l'ordre des familles."
   },
   "perte_traduction": "Discrétise l'espace continu des mécanismes de sabotage en trois bandes de distance et remplace une trajectoire évolutive longue (coûteuse) par un test d'hystérésis sur des séquences courtes de 3 à 4 familles.",
   "questions_servies": [
    "Q5",
    "Q1",
    "Q4",
    "nouvelle"
   ],
   "avantage": {
    "source": "organisme",
    "texte": "L'héritage récompensé sur K >= 3 générations (N-045-v2), la mémoire à empreinte prédictive et la sortie 5 (« pointer le proposeur sur les failles de notre propre programme ») sont câblés dans l'organisme ; la carte des hypothèses fournit la distance de mécanisme a priori.",
    "incopiable_parce_que": "Les occupants de l'apprentissage continu de sécurité (SafeCoEvo, EvoSafety, Lifelong Safety Alignment) traitent la mémoire comme un simple tampon d'exemples ou de règles toujours supposé bénéfique et évaluent sur un ordre fixe unique sans distance théorique ni témoin sans héritage à budget égal. Tester l'hystérésis et le péché antigénique remet en cause leur hypothèse d'accumulation monotone."
   },
   "originalite": {
    "niveau": "inedite",
    "texte": "Transpose le concept immunologique de péché antigénique originel (Francis 1960) et de biais de primauté en apprentissage par renforcement (Nikishin et al. 2022) aux boucles co-évolutives de moniteurs de sécurité, en transformant une règle interne de notre organisme (N-045-v2) en hypothèse falsifiable à bas coût (3 à 4 familles au lieu d'une longue courbe asymptotique)."
   },
   "demande_organisme": {
    "nature": "modification",
    "texte": "Sur processeur : ajouter un commutateur désactivant l'héritage N-045-v2 à budget d'évaluation identique (bras témoin naïf) et un planificateur d'ordre exécutant deux permutations inverses de la rotation des familles."
   },
   "cout": {
    "nature": "depense",
    "ordre_de_grandeur": "Zéro dollar sur simulateur jouet et sur sondes linéaires réentraînées sur activations mises en cache ; 100 à 250 dollars d'appels aux proposeurs pour 2 permutations × 3 générations."
   },
   "piege": "Confondre le péché antigénique (creux spécifique dans la bande de distance intermédiaire par réactivation d'une règle inadaptée) avec une perte générale de plasticité ou une saturation du budget (où la défense héritée serait uniformément pire partout) : seule la non-monotonie (gain sur le proche, perte sur l'intermédiaire, neutre sur le lointain) valide l'effet.",
   "cosmetique_si": "La différence de rappel entre défense héritée et défense neuve est monotone en distance ou statistiquement indiscernable de zéro sur les trois bandes, et l'inversion de l'ordre des familles ne change pas le vecteur de rappel final.",
   "anteriorite": [
    {
     "reference": "On the Doctrine of Original Antigenic Sin, Francis, Proceedings of the American Philosophical Society 1960",
     "statut": "SUPPOSE"
    },
    {
     "reference": "The Primacy Bias in Deep Reinforcement Learning, Nikishin et al., ICML 2022",
     "statut": "SUPPOSE"
    },
    {
     "reference": "Loss of plasticity in deep continual learning, Dohare et al., Nature 2024",
     "statut": "SUPPOSE"
    },
    {
     "reference": "On the Spontaneous Emergence of Discrete and Modularzner / Facilitated Variation, Parter, Kashtan, Alon, PLoS Computational Biology 2008",
     "statut": "RAPPORTE"
    },
    {
     "reference": "HyperAgents, Zhang, Zhao, Yang, Foerster, Clune, Jiang, Devlin, Shavrina, 2026, arXiv:2603.19461v1",
     "statut": "RAPPORTE"
    },
    {
     "reference": "SkillFlow, 2026, arXiv:2604.17308",
     "statut": "RAPPORTE"
    },
    {
     "reference": "EvoSafety: Model-Agnostic Lifelong LLM Safety via Externalized Attack-Defense Co-Evolution, Zhang et al., 2026, arXiv:2605.13411v1",
     "statut": "RAPPORTE"
    },
    {
     "reference": "SafeCoEvo: Co-Evolving Safety Harnesses and Guards for LLM Agents at Test-Time, Cheng et al., 2026, arXiv:2609.36580v2",
     "statut": "RAPPORTE"
    }
   ]
  },
  {
   "nom": "Approche A1 — Juge à support de désaccord et portefeuille de vigilance (fusion Discern + Portfolio Vigilance)",
   "type": "approche",
   "enonce": "Transposer à notre juge figé et à la sélection des proposeurs (pièce F) l'identité de support de Balachandran (2609.17560) combinée au mélange d'experts de Mondal et al. (2609.32267) : lorsqu'un proposeur soumet un moniteur candidat g face au moniteur en place f, observer gratuitement leur taux de désaccord sur un grand flux non étiqueté (Palier 0 : rejet ou certification à zéro étiquette si le désaccord est hors bande), et ne dépenser le budget d'exposition de la banque d'épreuve scellée que sur les instances où f et g sont en désaccord au seuil de 1 % de faux positifs (At = 1), en mixant à poids 1/2 un parieur guidé par la carte théorique des hypothèses (conseil non fiable au sens M2) et un parieur robuste n'apprenant que des étiquettes d'épreuve.",
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
    "texte": "Fusionne deux préimpressions statistiques de septembre 2026 (Discern, 2609.17560, et Portfolio Vigilance, 2609.32267, conçues pour le déploiement industriel d'une mise à jour de modèle) pour en faire le moteur de sélection darwinienne d'un pôle de recherche automatique de moniteurs."
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
   "nom": "Approche A2 — Chirurgie mécanique de dilution et chaîne d'hybrides d'activations sans attaquant",
   "type": "approche",
   "enonce": "Pour alimenter Q4, Q-pont et Q1 sans jamais construire ni exécuter d'agent attaquant (respect absolu de R-597 et R-611), remplacer l'équipe rouge par un opérateur purement mécanique combinant le titrage dose-réponse de la métrologie et l'argument hybride de la cryptographie : à partir de paires appariées (trajectoire bénigne, trajectoire de sabotage issue d'un banc public figé comme ControlArena, SHADE-Arena ou FIBS) du même modèle sur la même tâche principale, générer (i) une échelle de dilution temporelle K par entrelacement de pas bénins authentiques du même agent à dommage final constant, et (ii) une chaîne d'hybrides remplaçant un composant à la fois dans le texte puis couche par couche dans les activations mises en cache.",
   "loi_predictive": {
    "espace_instances": "Grille paramétrique de dilution K et chaîne d'hybrides couche par couche appliquées à N >= 200 paires de trajectoires (bénigne, sabotage) appariées par tâche et par modèle agent sur 8 et 70 milliards de paramètres.",
    "prediction": "La dose médiane de détection (ED50 : valeur de K où le rappel à 1 % de faux positifs passe sous 50 %) mesurée sur l'opérateur mécanique prédit avec une corrélation de rang supérieure à 0,75 le classement de robustesse des moniteurs sur les attaques graduelles et multi-agents tenues à l'écart de Hills et al. et d'Angelini et Makins et al. ; sur la chaîne d'hybrides, une propriété P_k valide concentre au moins 60 % du saut de détection sur l'étape ou la couche porteuse de P_k, tandis qu'une propriété dominée par l'artefact disperse le saut sur les couches d'identité de source.",
    "signe": "+",
    "metrique": "Corrélation de rang entre la dose médiane ED50 sur l'opérateur mécanique et le taux d'évasion sur bancs diffus externes, et part de la variation totale du score de détection concentrée sur l'étape hybride porteuse de P_k."
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
    "texte": "Réconcilie la contrainte de sûreté R-597 (zéro génération d'attaque nouvelle, zéro refus de modèle de frontière, coût processeur) avec le besoin d'avoir un bouton continu de dilution (gamma * D) et une localisation couche par couche sur poids ouverts de 8 et 70 milliards de paramètres.",
    "incopiable_parce_que": "Les occupants qui reposent sur l'élicitation de modèles de frontière subissent un biais de sélection massif (Hills et al. notent en sections 4.1 et 6 que leurs attaques graduelles réussies concentrent en réalité l'attaque en 1 ou 2 requêtes et que Opus 4.6 refuse d'attaquer ; Storf et al. jettent 49 % des trajectoires où la tâche secondaire échoue), et les occupants boîte noire n'ont pas accès aux hybrides d'activations."
   },
   "originalite": {
    "niveau": "inedite",
    "texte": "Fusionne le titrage dose-réponse métrologique et l'argument hybride cryptographique (Goldwasser et Micali 1984 ; échanges causaux sur activations de Meng et al. 2022) pour créer un banc d'épreuve séquentiel et un diagnostic de validité de pont sans aucun appel de modèle générateur."
   },
   "demande_organisme": {
    "nature": "ajout",
    "texte": "Un script Python pur sur processeur dans le module de préparation des banques (entrelacement d'étapes JSONL et substitution couche par couche sur tenseurs d'activations mis en cache)."
   },
   "cout": {
    "nature": "processeur",
    "ordre_de_grandeur": "Zéro dollar sur les transcriptions et activations déjà extraites."
   },
   "piege": "Créer des discontinuités syntaxiques ou représentationnelles aux points de greffe, qu'un moniteur détecterait comme une anomalie de cohérence plutôt que comme du sabotage : parade obligatoire par un témoin « hybride bénin-dans-bénin » qui doit maintenir le taux de faux positifs à 1 %.",
   "cosmetique_si": "Un moniteur boîte noire ou une sonde distingue la greffe « bénin-dans-bénin » de la trace bénigne originale à un taux supérieur à 5 % pour un seuil étalonné à 1 %, ou si les classements ED50 ne corrèlent pas avec ceux de Hills et al.",
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
    },
    {
     "reference": "Probabilistic Encryption, Goldwasser, Micali, Journal of Computer and System Sciences 1984",
     "statut": "SUPPOSE"
    },
    {
     "reference": "Locating and Editing Factual Associations in GPT, Meng et al., NeurIPS 2022",
     "statut": "SUPPOSE"
    }
   ]
  },
  {
   "nom": "Approche A3 — Test par mutation chirurgicale des moniteurs (témoins plantés côté défense)",
   "type": "approche",
   "enonce": "Au lieu de mesurer la puissance d'un banc d'évaluation en lançant un attaquant (interdit par R-597), emprunter le test par mutation du génie logiciel en mutant chirurgicalement la DÉFENSE : à partir d'un moniteur complet et de la carte des hypothèses, générer automatiquement des « moniteurs mutants » dont une capacité précise est amputée par construction (effacement linéaire LEACE d'un sous-espace d'activations, retrait d'une couche, troncature de l'horizon de l'agrégateur séquentiel à K = 1, ou « mutant aveugle au contenu » qui ne lit que les traits de surface et d'identité du générateur) et les injecter comme témoins plantés dans le juge figé et sur les bancs des occupants.",
   "loi_predictive": {
    "espace_instances": "Ensemble de M >= 20 moniteurs mutants (un par clause de la carte des hypothèses, plus le mutant aveugle au contenu) évalués sur nos banques tenues à l'écart et sur K >= 5 bancs publiés d'occupants.",
    "prediction": "Sur un banc valide, chaque mutant d'hypothèse h subit une chute de rappel d'au moins 20 points de pourcentage sur la seule famille qui viole h sans perte sur les autres (sélectivité diagnostique), tandis que sur les bancs d'occupants non contrôlés pour l'artefact, le « mutant aveugle au contenu » atteint encore une aire sous la courbe ROC supérieure à 0,70 et plus de 25 % des mutants d'hypothèses survivent sans être détectés par le banc.",
    "signe": "+",
    "metrique": "Score de mutation du banc (fraction de mutants d'hypothèse tués avec sélectivité >= 20 points de rappel) et aire sous la courbe ROC du mutant aveugle au contenu sur chaque banc."
   },
   "perte_traduction": "Un défaut chirurgical injecté dans une sonde ou un agrégateur ne reproduit pas toutes les défaillances émergentes d'un moniteur appris ; on mesure la résolution de l'instrument de test, pas la distribution naturelle des bogues.",
   "questions_servies": [
    "Q6",
    "Q2",
    "Q3",
    "Q-pont"
   ],
   "avantage": {
    "source": "organisme",
    "texte": "Combine les témoins plantés à vérité connue du juge figé (organisme), l'accès boîte blanche aux couches et sous-espaces d'activations sur poids ouverts (programme : requis pour créer des mutants d'effacement de concept), et la carte des hypothèses qui indexe chaque mutant sur une clause théorique précise.",
    "incopiable_parce_que": "Un occupant sans carte explicite des hypothèses ni sondes boîte blanche ne peut que perturber aléatoirement ses invites de moniteur (ce qui produit des mutants dégénérés ou équivalents), et son banc d'évaluation est déjà co-adapté à son propre attaquant."
   },
   "originalite": {
    "niveau": "inedite",
    "texte": "Transpose l'analyse de mutation logicielle (DeMillo, Lipton et Sayward 1978 ; DeepMutation de Ma et al. 2018) et l'effacement chirurgical de concepts dans les représentations (Ravfogel et al. 2020 ; Belrose et al. 2023) à l'étalonnage des bancs de contrôle d'agents et au contrôle d'artefact sans attaquant."
   },
   "demande_organisme": {
    "nature": "ajout",
    "texte": "Sur processeur : un générateur automatique de moniteurs mutants (projection orthogonale sur tenseurs d'activations, masquage de couches, troncature de fenêtre CUSUM, classifieur de surface seul) inscrit au registre des témoins plantés du juge v7."
   },
   "cout": {
    "nature": "processeur",
    "ordre_de_grandeur": "Entièrement sur processeur une fois les activations et traits de surface extraits (opérations matricielles et réévaluation de classifieurs légers)."
   },
   "piege": "Générer des « mutants équivalents » (lorsque l'information retirée d'une couche est redondante dans une autre couche, comme Fomin le montre p.11 où l'ablation de 14 traits raccourcis ne bouge l'aire sous la courbe que de -0,1 point par compensation) : il faut donc opérer par projection orthogonale sur l'ensemble des couches lues.",
   "cosmetique_si": "Tous les mutants non triviaux sont tués à 100 % sur tous les bancs (score de mutation saturé à 1 sans pouvoir discriminant) ou le mutant aveugle au contenu tombe à 0,50 d'aire sous la courbe sur tous les bancs publiés.",
   "anteriorite": [
    {
     "reference": "Hints on Test Data Selection: Help for the Practicing Programmer, DeMillo, Lipton, Sayward, IEEE Computer 1978",
     "statut": "SUPPOSE"
    },
    {
     "reference": "DeepMutation: Mutation Testing of Deep Learning Systems, Ma et al., ISSRE 2018",
     "statut": "SUPPOSE"
    },
    {
     "reference": "Null It Out: Guarding Protected Attributes by Iterative Nullspace Projection, Ravfogel et al., ACL 2020",
     "statut": "SUPPOSE"
    },
    {
     "reference": "LEACE: Perfect linear concept erasure in closed form, Belrose et al., NeurIPS 2023",
     "statut": "SUPPOSE"
    },
    {
     "reference": "When Benchmarks Lie: Evaluating Malicious Prompt Classifiers Under True Distribution Shift, Fomin, 2026, arXiv:2602.14161v2",
     "statut": "RAPPORTE"
    }
   ]
  }
 ]
}
```