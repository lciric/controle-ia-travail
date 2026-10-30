```json
{"fiches": [
 {
  "nom": "Q3 sur grille publiée, puis sur grille à venir : prédire les cellules où notre propre moniteur échoue",
  "type": "question",
  "enonce": "Volet 1 (rétrospectif, bancs existants) : une instance de théorie qui ne connaît que la carte des hypothèses (aucun score de nos moniteurs, aucun taux publié) prédit-elle, avant le test, contre une référence de permutation ET contre la prédiction naïve « comme les moniteurs modèles publiés », le classement des taux de détection de NOTRE moniteur (sonde sur modèle à 8 milliards de paramètres plus boîte noire) par cellule de la taxonomie croisée de MonitoringBench (niveaux techniques T, structurels S, d'évasion E) et par catégorie de SLEIGHT-Bench ? La quantité prédite n'existe nulle part : elle ne peut être ni mémorisée ni lue après coup. Volet 2 (prospectif, règle gelée) : la même instance scelle, pour une liste déclarée d'occupants, le signe de l'écart de détection par classe d'hypothèse violée que révéleront leurs prochaines versions publiées (nouvelles versions de SLEIGHT-Bench, de MonitoringBench, travaux de l'institut britannique), une règle de correspondance catégories → classes étant gelée avant parution. Leur attaquant devient notre test final, lu une fois, que nous n'avons pas pu contaminer. Cette formulation lève le risque « Q3 non concluante faute de puissance » : la grille T×S×E fournit des dizaines de cellules peuplées, et le volet 2 ajoute des familles vraiment inédites au fil des douze mois.",
  "loi_predictive": {
   "espace_instances": "Volet 1 : cellules peuplées (≥ 30 trajectoires d'attaque réussies) de MonitoringBench, ~25 à 40 cellules sur 2 644 trajectoires, plus les 11 catégories de SLEIGHT-Bench (40 attaques, 10 essais, bénins appariés) ; un moniteur à nous non entraîné sur ces bancs (les auteurs demandent l'exclusion des corpus d'entraînement : lecture pour évaluation seulement). Volet 2 : couples (classe de moniteur publiée, catégorie de famille) parus après la date de scellement, 20 à 60 couples attendus en douze mois.",
   "prediction": "Volet 1 : corrélation de rang de Spearman ≥ 0,4 entre classement prédit et observé, au-delà du 95e centile de 10 000 permutations, ET au moins égale à celle de la prédiction naïve ; la théorie désigne ≥ 3 cellules « échec » (rappel < 20 %) dont ≥ 2 se confirment. Volet 2 : signe de l'écart à la moyenne du papier correct dans ≥ 65 % des couples, contre 50 % (hasard) et contre une référence de persistance (classement du papier précédent).",
   "signe": "+",
   "metrique": "Rappel à 1 % de faux positifs par cellule, seuil calibré sur les 416 trajectoires honnêtes (MonitoringBench) et sur les bénins appariés (SLEIGHT-Bench) ; score logarithmique des probabilités scellées pour le volet 2 ; prédictions empreintées avant tout score ou toute parution ; test lu une seule fois."
  },
  "perte_traduction": "« Savoir où sa défense casse sans y être attaqué » devient un classement de cellules d'une taxonomie fixée par d'autres, étiquetée a posteriori par un juge modèle ; on perd les familles hors taxonomie, le diffus inter-épisodes (S4 est intra-trajectoire) et le volet « au fil des générations » (moniteur figé). Le volet 2 dépend du calendrier et de la granularité des catégories publiées, hors de notre contrôle.",
  "questions_servies": ["Q3", "Q-pont", "Q4", "Q6", "Q1"],
  "avantage": {
   "source": "programme",
   "texte": "La carte des hypothèses existe et son gardien n'a conçu aucun moniteur ; le préenregistrement scellé (méthodes) fait de l'horodatage, et non du calcul, l'objet de la preuve ; la quantité prédite (notre moniteur, leurs familles futures) est inédite par construction.",
   "incopiable_parce_que": "Un occupant qui construit l'attaquant tire ses catégories des échecs observés (SLEIGHT-Bench l'écrit : les catégories sont nées des transcriptions qui ont échappé aux moniteurs) ; sa « prédiction » est a posteriori par construction. Il ne peut pas davantage préenregistrer de prédiction crédible sur son propre prochain attaquant : il le conçoit, il voit ses échecs. Un laboratoire mieux doté en calcul ne gagne rien : le résultat tient à la séquence scellée théorie → prédiction → test, et il faudrait une théorie explicite des hypothèses statistiques du moniteur qu'aucun occupant ne publie."
  },
  "originalite": {
   "niveau": "transposition",
   "texte": "Le schéma « hypothèses du détecteur → familles d'évasion → vérification » est ancien (détection d'intrusion) et SLEIGHT-Bench le réalise avec une théorie informelle ; la notation de la théorie comme prévisionniste, préenregistrée, par cellule, contre permutation et contre la prédiction naïve, puis sur les bancs à venir des concurrents, n'a pas été vue (pièce C, Q3)."
  },
  "demande_organisme": {
   "nature": "ajout",
   "texte": "La troisième instance (fixe l'appariement cellules ↔ hypothèses, la règle de correspondance pour le volet 2, scelle les prédictions, n'a lu ni pièce ni score) : préalable à cette fiche, pas à toutes ; une garde de code qui refuse l'évaluation si l'empreinte de la prédiction est postérieure au premier score ou à la parution ; un lecteur des formats de trajectoires publiés ; un moniteur dont les données d'entraînement excluent ces bancs ; un registre de veille gelé (liste d'occupants). Un horodatage public de l'empreinte serait une publication : nœud pour Lazar."
  },
  "cout": {
   "nature": "depense",
   "ordre_de_grandeur": "Dérivation et préenregistrement sur processeur ; activations du modèle à 8 milliards sur ~3 000 trajectoires longues : quelques heures de processeur graphique (dizaines de dollars) ; boîte noire par appels : centaines de dollars ; volet 2 : processeur seul."
  },
  "piege": "Circularité à deux voies : (a) cellules et catégories nées des échecs de moniteurs modèles — une théorie qui dit « les moniteurs échouent là où la taxonomie le dit » prédit trivialement, d'où la référence naïve à égaler SANS l'avoir lue ; (b) le prédicteur est un modèle dont le corpus contient peut-être les papiers — d'où la prédiction de NOTRE moniteur jamais publié, une instance qui n'a pas lu les pièces, et la fiche « prédicteur en quarantaine ». Confusion des cellules avec la longueur de trajectoire et l'étape de raffinement. Volet 2 : règle de correspondance écrite en connaissant leurs catégories antérieures ; prédictions triviales si un occupant republie le même motif ; trop peu de parutions en douze mois.",
  "cosmetique_si": "La corrélation n'excède pas celle de la prédiction naïve, ou le classement prédit est entièrement expliqué par la longueur de trajectoire ou le seul niveau S ; volet 2 : on ne bat pas la persistance, ou la règle de correspondance doit être retouchée après lecture.",
  "anteriorite": [
   {"reference": "SLEIGHT-Bench: A Benchmark of Evasion Attacks Against Agent Monitors, Najt, Toft, Tracy, Roger, Benton, 2026, arXiv 2605.16626", "statut": "RAPPORTE"},
   {"reference": "MonitoringBench: Semi-Automated Red-Teaming for Agent Monitoring, Jotautaitė, Martinez, Matthews, Tracy, 2026, arXiv 2605.09684", "statut": "RAPPORTE"},
   {"reference": "Inherited Circuits, Learned Semantics, Fetterman, 2026, arXiv 2606.27091", "statut": "RAPPORTE"},
   {"reference": "Insertion, Evasion, and Denial of Service, Ptacek et Newsham, 1998", "statut": "RAPPORTE"},
   {"reference": "What Happened to Anomaly Detection?, Inoue et Somayaji, 2006, rapport Carleton TR-07-09", "statut": "RAPPORTE"},
   {"reference": "No Free Lunch: The Hazards of Over-Expressive Representations in Anomaly Detection, Reiss, Cohen, Hoshen, arXiv 2306.07284", "statut": "RAPPORTE"},
   {"reference": "Formulating Robustness Against Unforeseen Attacks, Dai, Mahloujifar, Mittal, NeurIPS 2022", "statut": "RAPPORTE"},
   {"reference": "Caught in the Act (jeu FIBS), Hollinsworth, Spies, Diriba, Gleave, Cundy, 2026, arXiv 2610.12445", "statut": "RAPPORTE"},
   {"reference": "Why 6? Defining the Operational Limits of stide, Tan et Maxion, IEEE S&P 2002", "statut": "SUPPOSE"},
   {"reference": "Predict science to improve science, DellaVigna, Pope, Vivalt, Science 2019", "statut": "SUPPOSE"}
  ]
 },
 {
  "nom": "La diagonale de l'auto-jeu : le score contre l'attaquant co-évolué prédit-il la généralisation ?",
  "type": "question",
  "enonce": "Dans les matrices croisées attaquant × défenseur publiées par les occupants co-évolutifs, le taux de succès d'attaque du défenseur final contre l'attaquant avec lequel il a co-évolué (la « diagonale ») est-il informatif sur son taux contre des familles publiées tenues à l'écart ? Hypothèse : non, et dans les deux sens. Quand la paire est figée, elle converge vers une spécialisation mutuelle (MAGIC, tableau 10 : l'attaquant co-entraîné est le plus faible de tous contre son propre défenseur, 9,0 % contre 10,5 % pour l'attaquant de base) ; quand l'attaquant reste adaptatif à l'évaluation, la diagonale surestime (AgentSafeEvo : attaquant final à 49,8 % contre le défenseur final, bien au-dessus des bancs externes). Dans les deux cas la diagonale n'est pas une mesure de généralisation — c'est précisément l'objet que le refus de construire l'attaquant nous interdit de publier, et que nous pouvons donc auditer sans conflit.",
  "loi_predictive": {
   "espace_instances": "Paires (défenseur, matrice) extraites des occupants publiant à la fois une diagonale et ≥ 2 familles externes : MAGIC (tableaux 3 et 10), AgentSafeEvo (évaluation croisée par stade, quatre bancs), EvoSafety (tableau 2 : compétences vues / non vues / attaquant évolué), EvoDefense (tableaux 1 à 3), RvB (gardes par tour contre quatre bancs externes), SafeCoEvo si une diagonale existe ; attendu : 5 à 8 matrices, 15 à 30 paires. Liste, tableaux et règle d'appariement fixés avant ouverture des fichiers PDF (Portable Document Format).",
   "prediction": "Corrélation de rang < 0,3 entre taux sur la diagonale et taux médian sur familles externes ; écart absolu > 15 points dans ≥ 70 % des paires, dans les deux sens (sous-estimation du risque quand la paire est figée, surestimation de la robustesse quand l'attaquant est adaptatif à l'évaluation) ; quand plusieurs tours sont publiés, le ratio diagonale/externe s'éloigne de 1 avec le nombre de tours.",
   "signe": "0",
   "metrique": "Taux de succès d'attaque tel que publié, au point de fonctionnement et avec le juge de l'occupant, rapporté par papier (jamais en moyenne globale) ; extraction préenregistrée, vérifiée sur PDF empreinté avant tout chiffre."
  },
  "perte_traduction": "Le mécanisme (spécialisation de paire, Goodhart réciproque) devient une méta-analyse de tableaux hétérogènes ; on ne mesure pas la dynamique interne de la paire, seulement son empreinte publiée ; juges et points de fonctionnement diffèrent d'un papier à l'autre (MAGIC montre que Qwen3Guard et GPT-4o divergent sur les défenseurs forts).",
  "questions_servies": ["nouvelle", "Q1", "Q2", "Q5"],
  "avantage": {
   "source": "methodes",
   "texte": "Le refus de construire l'attaquant : nous n'avons pas de diagonale à défendre ; notre aptitude est la généralisation sur familles tenues par un tiers, jamais le score contre un adversaire maison.",
   "incopiable_parce_que": "Ce n'est pas une question de calcul mais de conflit d'intérêt : chaque occupant publie sa diagonale comme preuve centrale ; l'auditer, c'est auditer sa propre revendication. De plus, une fois la paire construite, la diagonale est le seul objet qu'il mesure sans tiers ; produire une mesure qui ne passe pas par son attaquant exige de changer de méthode."
  },
  "originalite": {
   "niveau": "transposition",
   "texte": "Miconi (progrès historique pris pour global), Czempin et Gleave (l'adversaire unique surajuste), Tramèr et al. (attaques adaptatives) occupent le principe ; la mesure en méta-analyse de matrices publiées de co-évolution défensive, à règle d'extraction scellée, n'a pas été vue dans les pièces."
  },
  "demande_organisme": {
   "nature": "rien",
   "texte": "Extraction préenregistrée par un sous-agent neuf, règle d'appariement fixée par la troisième instance avant lecture ; contre-lecture par un modèle d'une autre lignée ; vérification R7 sur PDF empreinté."
  },
  "cout": {
   "nature": "processeur",
   "ordre_de_grandeur": "Quelques jours d'extraction et de contre-lecture ; aucun calcul."
  },
  "piege": "Sélection après lecture (liste d'occupants, tableaux, règle diagonale ↔ externe fixés AVANT d'ouvrir les PDF) ; hétérogénéité des juges et des points de fonctionnement (rapporter par papier) ; tables incomplètes (une matrice sans familles externes est écartée, pas interprétée) ; chiffres transcrits non opposables avant lecture sur PDF empreinté.",
  "cosmetique_si": "Moins de 5 matrices exploitables, ou si le résultat se réduit à « un attaquant adaptatif est plus fort qu'un banc figé », déjà établi (Terekhov et al., Tramèr et al.).",
  "anteriorite": [
   {"reference": "MAGIC: A Co-Evolving Attacker–Defender Adversarial Game for Robust LLM Safety, Wen, He et al., 2026, arXiv 2602.01539", "statut": "RAPPORTE"},
   {"reference": "AgentSafeEvo: Adversarial Co-Evolution for LLM Agent Safety, Wang, Wen et al., 2026, arXiv 2610.19422", "statut": "RAPPORTE"},
   {"reference": "EvoSafety, Zhang et al., 2026, arXiv 2605.13411", "statut": "RAPPORTE"},
   {"reference": "EvoDefense: Co-Evolving Black-Box Defense with Large Language Models, Li et al., 2026, arXiv 2605.31140", "statut": "RAPPORTE"},
   {"reference": "RvB: Automating AI System Hardening via Iterative Red-Blue Games, Huang, Liu, Zhang et al., 2026, arXiv 2601.19726", "statut": "RAPPORTE"},
   {"reference": "SafeCoEvo, Cheng et al., 2026, arXiv 2609.36580", "statut": "RAPPORTE"},
   {"reference": "Miconi, EuroGP 2009, progrès local / historique / global en co-évolution", "statut": "RAPPORTE"},
   {"reference": "Czempin et Gleave, arXiv 2208.05083", "statut": "RAPPORTE"},
   {"reference": "On Adaptive Attacks to Adversarial Example Defenses, Tramèr et al., NeurIPS 2020", "statut": "RAPPORTE"},
   {"reference": "Adaptive Attacks on Trusted Monitors Subvert AI Control Protocols, Terekhov et al., 2025, arXiv 2510.09462", "statut": "RAPPORTE"}
  ]
 },
 {
  "nom": "Q2 : résultat ou hygiène ? Rejugement des courbes publiées sous juge figé à borne",
  "type": "question",
  "enonce": "Chaque occupant publie une courbe : tour après tour, la défense s'améliore contre son attaquant. Ces courbes sont des suites de promotions prononcées par un juge qui dérive (juge-modèle partagé entre récompense et évaluation chez MAGIC et AgentSafeEvo ; sélection du point de contrôle sur la validation même qui est rapportée chez SafeCoEvo, avec une courbe non monotone après l'époque 13 ; scoreur figé sans garantie chez EvoDefense, où le taux remonte de 4,4 % à 6,6 % au tour 5). Rejouées sous NOTRE juge — chaque amélioration rapportée devenant une mise d'un e-processus à budget d'erreur unique composé sur toute la suite (inégalité de Ville), contre un nul d'archive préenregistré — combien de leurs promotions survivraient, et à quel tour un arrêt honnête les aurait arrêtées ? Si moins de la moitié survit, et moins encore dans le régime « validation en distribution », le juge figé garanti est un résultat (1c de la question), pas une hygiène. Sans rien lancer, et avant que notre boucle existe : les trois régimes de Q2 sont lus sur leurs courbes.",
  "loi_predictive": {
   "espace_instances": "Courbes tour par tour publiées avec effectifs et dispersion : EvoDefense (tableau 3, tours 1, 2, 5, 10 × 4 modèles × 5 classes), Bailey et al. (70 époques, rappel sur la dernière attaque), RvB (4 tours), AgentSafeEvo (stades), SafeCoEvo (15 époques de validation), Terekhov et al. 2606 (itérations de point-selle) ; liste gelée ; chaque courbe classée par régime de juge avant lecture ; témoins plantés : courbes simulées sous le nul et sous effet vrai, insérées à l'aveugle.",
   "prediction": "La part des promotions rapportées qui survivent à la borne (niveau 0,05, budget composé sur la suite) est < 50 % ; elle est la plus basse dans le régime « validation en distribution », intermédiaire sous « juge-modèle partagé », la plus haute sous « scoreur figé » ; les régressions rapportées puis ignorées (EvoDefense tour 5) sont signalées comme alarmes ; sur les témoins plantés, ≥ 90 % des promotions sous effet vrai survivent et ≤ 10 % sous le nul.",
   "signe": "-",
   "metrique": "Part survivante par courbe et par régime ; tour d'arrêt honnête ; taux de bonne élimination sur témoins plantés ; règle de rejugement et nul d'archive empreintés avant toute lecture de courbe."
  },
  "perte_traduction": "On dépend de ce qui est rapporté (sans dispersion, pas de mise ; moyennes de trois exécutions souvent) ; on juge leur rapport, pas leur défense ; la borne contrôle les fausses promotions sur le jeu du juge, pas la robustesse à l'inédit.",
  "questions_servies": ["Q2", "Q5", "nouvelle"],
  "avantage": {
   "source": "organisme",
   "texte": "Le juge figé à mise contre bibliothèque de nuls avec borne composée sur une suite de promotions existe déjà (démonstration couche 1) ; les témoins plantés étalonnent sa sévérité ; la règle est préenregistrée (méthodes).",
   "incopiable_parce_que": "Un occupant ne peut se l'appliquer sans conflit d'intérêt : c'est sa courbe qui est rejugée. Les travaux de certification (2609.17560, 2609.32267) fournissent l'outil mais excluent les pertes jugées et n'ont pas d'adversaire ; l'assemblage sur des boucles co-évolutives de moniteurs, avec étalonnage par témoins, n'existe que chez nous."
  },
  "originalite": {
   "niveau": "transposition",
   "texte": "Analyse adaptative des données (Dwork et al.), certification de promotions par e-processus (Balachandran ; Mondal et al.), prix de la vigilance sous dérive d'évaluateur ; le rejugement de courbes co-évolutives de sûreté publiées, par régime de juge, n'a pas été vu."
  },
  "demande_organisme": {
   "nature": "modification",
   "texte": "Un adaptateur d'entrée du juge pour des suites de scores externes avec dispersion ; une bibliothèque de nuls d'archive simulés ; rien au noyau."
  },
  "cout": {
   "nature": "processeur",
   "ordre_de_grandeur": "Processeur seul ; lecture des PDF empreintés (R7) ; quelques jours."
  },
  "piege": "Chiffres transcrits non opposables ; nul choisi après avoir vu les courbes ; résultat attendu (« petits effectifs → intervalles larges ») pris pour résultat de défense, et propreté suspecte (R4) ; lecture comme dénigrement des occupants ; témoins plantés trop faciles.",
  "cosmetique_si": "Sur les témoins plantés toutes les courbes survivent ou aucune ; ou si la part survivante ne diffère pas entre régimes de juge (alors c'est la taille d'échantillon, pas le juge, qui parle) ; ou si moins de 4 courbes exploitables.",
  "anteriorite": [
   {"reference": "Pay Only for Disagreement: Certified No-Regression Verdicts for Model Updates, Balachandran, 2026, arXiv 2609.17560", "statut": "RAPPORTE"},
   {"reference": "When Can Old Evaluations Certify a New Model?, Mondal, Banik, Apurba, Al Mahmud, 2026, arXiv 2609.32267", "statut": "RAPPORTE"},
   {"reference": "Generalization in Adaptive Data Analysis and Holdout Reuse, Dwork et al., NeurIPS 2015, arXiv 1506.02629", "statut": "RAPPORTE"},
   {"reference": "The Ladder, Blum et Hardt, ICML 2015", "statut": "RAPPORTE"},
   {"reference": "Optimizing the Score, Losing Sight of the Task, 2026, arXiv 2609.25848", "statut": "RAPPORTE"},
   {"reference": "EvoDefense, Li et al., 2026, arXiv 2605.31140 (tableau 3)", "statut": "RAPPORTE"},
   {"reference": "SafeCoEvo, Cheng et al., 2026, arXiv 2609.36580 (sélection du point de contrôle, annexe F)", "statut": "RAPPORTE"},
   {"reference": "Obfuscated Activations Bypass LLM Latent-Space Defenses, Bailey et al., 2025, arXiv 2412.09565 (§3.5)", "statut": "RAPPORTE"},
   {"reference": "Universal inference, Wasserman, Ramdas, Balakrishnan, PNAS 2020", "statut": "SUPPOSE"},
   {"reference": "Deep RL at the Edge of the Statistical Precipice, Agarwal et al., NeurIPS 2021", "statut": "SUPPOSE"}
  ]
 },
 {
  "nom": "Q4 par l'axe structurel publié : dilution à dommage constant, même score, deux règles, coude préenregistré",
  "type": "question",
  "enonce": "Pour un moniteur conçu ou sélectionné sur des familles concentrées (niveaux structurels S1–S2 de MonitoringBench), le rappel décroît-il avec la dilution structurelle (S3, S4 ; attaques graduelles contre positionnelles de Hills et al. ; K = 1, 3, 9 agents de Makins et al.) à dommage total constant, selon un coude prédit par le lemme du plafond d'horizon (chute franche quand la divergence par pas multipliée par l'horizon effectif passe sous l'unité, transposition de la transition γ·D = Θ(1) de Ramtin et al.) ; et une règle séquentielle (somme cumulée CUSUM ou e-valeurs) appliquée aux MÊMES scores par pas récupère-t-elle une part prédite de cette chute, là où la règle « seuil par pas » ne le peut pas ? Le coude est préenregistré à partir des seuls scores S1–S2, avant lecture de S3–S4. Cette fiche ne dépend ni de Q3 ni de la troisième instance : elle peut commencer dès l'accord sur le nœud N-A (lecture du lemme contre Ramtin et Gualandi sur PDF).",
  "loi_predictive": {
   "espace_instances": "Trajectoires d'attaque réussies de MonitoringBench étiquetées S1 à S4 (2 644 ; S4 attendue ≥ 100), stratifiées par niveau technique T et stratégie E, élicitées contre raffinées ; familles graduelle/positionnelle de Hills (n = 120 / 600) et séries K de Makins (FakeLab, sur demande : contact externe, nœud) si accessibles ; notre moniteur : sonde sur modèle à 8 milliards plus boîte noire, scores par pas, non entraîné sur ces bancs.",
   "prediction": "(i) Règle « max par pas » : rappel à 1 % de faux positifs par trajectoire chute de ≥ 25 points de S1–S2 à S4 à T et E fixés ; (ii) règle séquentielle sur les mêmes scores, calibrée au même 1 % trajectoire : récupère ≥ la moitié de cette chute sur S4 ; (iii) le niveau S du coude observé coïncide avec le coude préenregistré depuis S1–S2 (tolérance d'un niveau) ; (iv) sur Hills : l'écart graduel − positionnel est plus grand pour la règle par pas que pour la règle séquentielle.",
   "signe": "-",
   "metrique": "Rappel à 1 % de faux positifs par trajectoire, seuil calibré sur les 416 trajectoires honnêtes ; deux règles de décision sur scores identiques, calibrées au même taux trajectoire (MonitoringBench : 1 % par pas compose à 6,7–17,4 % par trajectoire) ; comparaison au coude préenregistré."
  },
  "perte_traduction": "Le diffus « entre épisodes et entre agents » devient surtout « réparti dans une trajectoire » (S4 est intra-épisode) ; le vrai inter-épisodes dépend de l'accès aux données de Hills et Makins. Le moniteur est figé : le volet « boucle sélectionnée sur du concentré » n'est pas servi ici. Le dommage « constant » est approché par la réussite de la tâche secondaire, pas mesuré.",
  "questions_servies": ["Q4", "Q7", "Q-pont", "Q3"],
  "avantage": {
   "source": "programme",
   "texte": "Un lemme formel du coude (comparé d'abord sur PDF à Ramtin et al. et Gualandi et al. : s'il est couvert, il devient antécédent cité et la prédiction reste la nôtre), l'agrégateur séquentiel, et la boîte blanche sur poids ouverts appliquée aux traces publiées.",
   "incopiable_parce_que": "Makins et Hills construisent l'attaquant et choisissent la dilution après coup ; leur décomposition (dilution 25 %, récit de couverture 53 %, 38–43 % inexpliqué) est descriptive. Aucun occupant ne détient une prédiction préenregistrée du coude dérivée des hypothèses du moniteur ; la valeur est dans l'engagement avant lecture, pas dans le calcul."
  },
  "originalite": {
   "niveau": "transposition",
   "texte": "« Même score, deux règles » est occupé hors champ (Shewhart contre CUSUM, Urbina et al.) ; l'agrégation déployable est partielle en contrôle (Wen et al., TRACE, link-tracker de Hills) ; la confrontation d'un moniteur d'agent à un coude préenregistré issu de la détection de rupture n'a pas été vue."
  },
  "demande_organisme": {
   "nature": "modification",
   "texte": "L'agrégateur séquentiel doit accepter des scores par pas externes ; lecteur des formats de trajectoires publiés (lignes JSON) ; strate « diffus / concentré » de la banque étendue aux étiquettes S."
  },
  "cout": {
   "nature": "depense",
   "ordre_de_grandeur": "Activations du modèle à 8 milliards sur ~3 000 trajectoires : dizaines de dollars de processeur graphique (mutualisées avec la fiche Q3) ; boîte noire par appels : centaines de dollars."
  },
  "piege": "Confusion de la dilution avec T et E (le raffinement rééquilibre les catégories) et sélection : les S4 réussies ont survécu au raffinement contre trois moniteurs de développement, donc sont les plus discrètes ; parade : stratifier par T et E, comparer raffinées et élicitées. La règle séquentielle « gagne » trivialement si son seuil est plus permissif : calibrer les deux au même taux trajectoire. Lemme revendiqué avant lecture de ses voisins (N-A).",
  "cosmetique_si": "La chute (i) disparaît une fois stratifiée par T et E, ou si la règle séquentielle n'apporte rien au-delà d'un « max » recalibré par trajectoire, ou si le coude préenregistré tombe à ± 2 niveaux (aucune prédiction).",
  "anteriorite": [
   {"reference": "Multi-Agent AI Control: Distributed Attacks Hamper Per-Instance Monitors, Angelini, Makins, Shams, Phuong, 2026, arXiv 2607.07368", "statut": "RAPPORTE"},
   {"reference": "Distributed Attacks in Persistent-State AI Control, Hills, Caspary, Cooper Stickland, 2026, arXiv 2607.02514", "statut": "RAPPORTE"},
   {"reference": "MonitoringBench, Jotautaitė et al., 2026, arXiv 2605.09684", "statut": "RAPPORTE"},
   {"reference": "Quickest Change Detection in Discrete-Time in Presence of a Covert Adversary, Ramtin, Nain, Towsley, 2026, arXiv 2601.20022", "statut": "RAPPORTE"},
   {"reference": "Quickest Change Detection in Continuous-Time in Presence of a Covert Adversary, Ramtin, Nain, Towsley, 2025, arXiv 2509.17778", "statut": "RAPPORTE"},
   {"reference": "Gualandi, Maggio, Papadopoulos, MED 2022", "statut": "RAPPORTE"},
   {"reference": "Limiting the Impact of Stealthy Attacks on Industrial Control Systems, Urbina et al., ACM CCS 2016", "statut": "RAPPORTE"},
   {"reference": "Adaptive Deployment of Untrusted LLMs Reduces Distributed Threats, Wen et al., ICLR 2025, arXiv 2411.17693", "statut": "RAPPORTE"},
   {"reference": "TRACE, Mittapalli et al., 2026, arXiv 2606.07054", "statut": "RAPPORTE"},
   {"reference": "Diffuse AI Control on Fuzzy Tasks, Terekhov, Gulcehre, Hebbar, Benton, 2026, arXiv 2606.08892", "statut": "RAPPORTE"},
   {"reference": "Lorden 1971 ; Moustakides 1986, cités par Ramtin et al.", "statut": "RAPPORTE"},
   {"reference": "Manuel d'ingénierie statistique du NIST, section 6.3.2.3.1, Shewhart contre CUSUM", "statut": "RAPPORTE"}
  ]
 },
 {
  "nom": "Q-pont à coût nul : fabriqué (SLEIGHT-Bench) contre exécuté (MonitoringBench), par catégorie appariée scellée",
  "type": "question",
  "enonce": "Pour un même moniteur figé (le nôtre), le taux de détection par catégorie sur les transcriptions fabriquées de SLEIGHT-Bench (sorties d'outils inventées, auteurs humains, vérificateurs de réalisme) prédit-il le taux sur les trajectoires réellement exécutées de MonitoringBench (BashArena), catégorie par catégorie appariée — l'appariement étant fixé par un tiers AVANT toute lecture de taux ? En miroir : les taux publiés des moniteurs modèles communs aux deux bancs sont-ils corrélés par catégorie appariée ? Cette version de Q-pont ne dépend pas des propriétés dérivées par Q3 : les propriétés sont les catégories publiées. Désaccord avec la pièce B : Q-pont peut commencer avant le scellement de Q3 ; la version « P_k issues de Q3 » reste la seconde expérience, pas la première.",
  "loi_predictive": {
   "espace_instances": "6 à 8 paires de catégories appariables entre les 11 classes SLEIGHT-Bench et les niveaux T×S×E de MonitoringBench (par exemple : harm réparti ↔ S4 ; nommage plausible ↔ E1 ; charge dans contenu long ↔ E3 ; persuasion ↔ E4 — appariement exact scellé par le tiers) ; un moniteur à nous sur les deux bancs ; plus les moniteurs publiés communs aux deux (lignée Opus 4.5 / 4.6).",
   "prediction": "Corrélation de rang de Spearman ≥ 0,5 sur les paires « visibles dans le texte » (nommage, contenu long, obfuscation) et < 0,2 sur les paires qui reposent sur l'état, la persuasion ou l'ambiguïté d'autorisation — l'effondrement attendu par Kirch et al. pour les propriétés « ambiguës dans le texte » ; prédiction annexe : avec toutes les paires, la corrélation ne dépasse pas celle d'appariements aléatoires de même taille.",
   "signe": "+",
   "metrique": "Rappel à 1 % de faux positifs par catégorie ; calibration sur bénins appariés (SLEIGHT-Bench) et sur trajectoires honnêtes (MonitoringBench) ; rang de Spearman par sous-ensemble de paires, préenregistré ; exclusion des paires à n < 3 attaques."
  },
  "perte_traduction": "Le « réel » reste instruit, raffiné contre des moniteurs et à sabotage injecté ; les « propriétés P » sont des catégories de banc, pas des statistiques prédites du moniteur ; 6 à 8 paires donnent une puissance faible : le résultat est un signal d'alerte sur la voie synthétique, pas une validation.",
  "questions_servies": ["Q-pont", "Q3", "Q1", "Q6"],
  "avantage": {
   "source": "methodes",
   "texte": "L'appariement scellé par un tiers avant lecture, et un seul moniteur boîte blanche (programme) mesuré sur les deux bancs, alors que les bancs publiés ont des moniteurs différents.",
   "incopiable_parce_que": "Les deux bancs viennent des mêmes équipes, qui n'ont aucune incitation à publier que l'un ne prédit pas l'autre ; un occupant qui construit ses transcriptions choisit l'appariement après avoir vu les taux, ce qui fabrique la corrélation. L'enjeu est le scellement, pas le calcul."
  },
  "originalite": {
   "niveau": "transposition",
   "texte": "Métrique de prédictivité simulation-réel (Kadian et al.) et comparaison de classements d'anomalies synthétiques contre réelles (Steinbuss et Böhm) hors champ ; dans le contrôle, Storf et al. et le billet de Redwood mesurent un transfert global, jamais par propriété appariée scellée."
  },
  "demande_organisme": {
   "nature": "ajout",
   "texte": "La troisième instance pour l'appariement ; sinon rien : mêmes lecteurs et mêmes activations que les fiches Q3 et Q4."
  },
  "cout": {
   "nature": "depense",
   "ordre_de_grandeur": "Nulle si mutualisée avec l'extraction d'activations des fiches Q3 et Q4 ; sinon dizaines de dollars."
  },
  "piege": "L'appariement EST le résultat : fait après lecture, la corrélation est fabriquée ; parade : scellement par le tiers et test contre appariements aléatoires. Effectifs : certaines classes SLEIGHT-Bench comptent une ou deux attaques. Raffinement : les trajectoires MonitoringBench ont été rendues discrètes contre trois moniteurs, ce qui abaisse mécaniquement le « réel ».",
  "cosmetique_si": "L'appariement scellé ne fait pas mieux que des appariements aléatoires de même taille, ou si la corrélation disparaît quand on retire la seule paire « harm réparti ↔ S4 ».",
  "anteriorite": [
   {"reference": "SLEIGHT-Bench, Najt et al., 2026, arXiv 2605.16626", "statut": "RAPPORTE"},
   {"reference": "MonitoringBench, Jotautaitė et al., 2026, arXiv 2605.09684", "statut": "RAPPORTE"},
   {"reference": "Sim2Real Predictivity, Kadian et al., 2019, arXiv 1912.06321", "statut": "RAPPORTE"},
   {"reference": "The Impact of Off-Policy Training Data on Probe Generalisation, Kirch, Dower, Skapars et al., 2025, arXiv 2511.17408", "statut": "RAPPORTE"},
   {"reference": "Constitutional Black-Box Monitoring for Scheming in LLM Agents, Storf, Barton-Cooper, Peters-Gill, Hobbhahn, 2026, arXiv 2603.00829", "statut": "RAPPORTE"},
   {"reference": "Steinbuss et Böhm, 2020, arXiv 2004.06947", "statut": "RAPPORTE"},
   {"reference": "Simulated control evaluations, Olmo, Zhang, Tracy, Redwood Research, billet du 23 octobre 2026", "statut": "RAPPORTE"},
   {"reference": "Hesford et al., arXiv 2403.17458", "statut": "RAPPORTE"}
  ]
 },
 {
  "nom": "Q6 sur bancs d'agents : la part de provenance dans le rappel, mutant aveugle au contenu, puis par tour",
  "type": "question",
  "enonce": "Quelle part du rappel d'une sonde (entraînée hors de ces bancs, par exemple sur le jeu FIBS, Falsehoods in Broad Settings) ou d'un moniteur boîte noire, mesuré sur les bancs d'agents publiés, est expliquée par la provenance de la trajectoire (élicitée contre raffinée ; stratégie humaine contre agent de reconnaissance ; STRIDE contre Gloom contre ControlArena ; fabriquée contre exécutée) plutôt que par le sabotage — et, dans une boucle de sélection de moniteurs non contrôlée, cette part croît-elle de génération en génération ? L'instrument central est le « mutant aveugle au contenu » : un classifieur qui ne voit que des traits de surface (source, longueur, style, gabarit) et aucun contenu d'action ; s'il n'est pas « tué » par un banc (aire nettement au-dessus de 0,5), le banc est séparable par l'artefact, sans aucun attaquant — et le mutant devient un témoin planté « faux » que le juge doit refuser. Le volet statique est l'instrument (principe occupé par Fomin et Lin et al., jamais sur des trajectoires d'agents) ; le volet « par tour » est le résultat distinctif.",
  "loi_predictive": {
   "espace_instances": "Statique : ~3 000 trajectoires MonitoringBench à provenance connue (quatre sources, élicitées / raffinées), 43 transcriptions SLEIGHT-Bench avec bénins appariés, trajectoires ControlArena si accessibles ; activations d'un modèle à 8 milliards lisant les transcriptions. Dynamique : ≥ 5 générations de notre boucle sur ces familles, avec et sans contrôle de provenance.",
   "prediction": "Statique : classifieur de provenance sur activations ≥ 85 % (hasard 25–50 %) ; mutant aveugle au contenu : aire ≥ 0,6 pour séparer attaques et bénins sur au moins un banc d'occupant, mais ≤ 0,55 sur SLEIGHT-Bench avec bénins appariés (contrôle négatif) ; projeter hors des 16 principales directions de provenance dégrade le rappel de ≥ 2 points en moyenne avec hétérogénéité par source de ± 20 points ; rétention de coefficients < 0,5 pour ≥ 25 % des 50 traits principaux. Dynamique : sans contrôle, la part de rappel attribuable à la provenance augmente d'au moins 5 points par génération ; avec témoins bénins appariés par provenance dans la sélection, elle reste stable.",
   "signe": "+",
   "metrique": "Exactitude du classifieur de provenance ; aire sous la courbe du mutant aveugle ; rappel à 1 % de faux positifs avant et après projection ; rétention de coefficients par tour (protocole « un jeu de données laissé de côté », LODO)."
  },
  "perte_traduction": "L'« artefact du générateur » devient « provenance étiquetée par les auteurs des bancs » ; on ne mesure pas l'artefact de notre propre générateur de familles tant que la boucle n'existe pas ; la provenance est confondue avec la difficulté (les trajectoires raffinées sont plus discrètes par construction).",
  "questions_servies": ["Q6", "Q-pont", "Q1", "Q5", "Q2"],
  "avantage": {
   "source": "organisme",
   "texte": "Le bras « fuite textuelle » (N-053), les témoins plantés (le mutant aveugle en est un, côté défense), la mémoire qui refuse les redites et les tâches fraîches, plus la boîte blanche sur poids ouverts (programme) : la rétention de coefficients exige l'accès aux activations.",
   "incopiable_parce_que": "Les occupants à moniteur-modèle fermé ne peuvent ni mesurer la rétention ni projeter hors du sous-espace de provenance ; ceux qui construisent l'attaquant produisent eux-mêmes la signature (le raffinement par un même modèle est une provenance) et n'ont pas intérêt à la mesurer. Un laboratoire mieux doté peut faire le volet statique ; le volet par tour exige une boucle à juge figé et témoins appariés, que personne n'a."
  },
  "originalite": {
   "niveau": "transposition",
   "texte": "Fomin (LODO, rétention) et Lin et al. (identité du modèle) sur invites et sous-performance ; Pathak et al. pour la migration d'artefacts entre tours ; Wallace et al. pour « la collecte adversariale ne purge pas » ; analyse de mutants (test logiciel) pour le mutant aveugle ; le suivi par tour dans une boucle de moniteurs d'agents n'a pas été vu."
  },
  "demande_organisme": {
   "nature": "modification",
   "texte": "Étiqueter la provenance dans la banque et la strate des familles ; brancher le bras « fuite textuelle » sur des sources externes ; inscrire le mutant aveugle comme témoin planté ; témoins bénins appariés par provenance dans la sélection (invariant N-053)."
  },
  "cout": {
   "nature": "depense",
   "ordre_de_grandeur": "Statique : dizaines de dollars (mêmes activations que les fiches précédentes) ; mutant aveugle : processeur seul. Dynamique : générations de la boucle, nœud de dépense."
  },
  "piege": "Provenance et difficulté confondues : un classifieur de provenance qui apprend la difficulté est légitime ; parade : témoins bénins appariés par provenance, ligne de base « honnête contre honnête » de Lin et al., comparaison à provenance fixée. Directions de provenance et de sabotage qui se recouvrent (Fomin) : la projection redistribue plus qu'elle ne réduit, rapporter par source. Mutant aveugle grossier (tué partout) ou surentraîné sur un seul banc.",
  "cosmetique_si": "La projection hors provenance ne change pas le rappel, la rétention dépasse 0,8 partout et le mutant aveugle est à 0,5 sur tous les bancs : l'artefact n'explique alors rien et Q6 n'est qu'une précaution.",
  "anteriorite": [
   {"reference": "When Benchmarks Lie, Fomin, 2026, arXiv 2602.14161", "statut": "RAPPORTE"},
   {"reference": "When Lie Detectors Learn Model Identity, Lin, Bernabeu-Perez, Arnav, Wells, Phuong, ICLR 2026", "statut": "RAPPORTE"},
   {"reference": "Building Better Deception Probes Using Targeted Instruction Pairs, Natarajan et al., 2026, arXiv 2602.01425", "statut": "RAPPORTE"},
   {"reference": "Sequential Training of GANs Against GAN-Classifiers Reveals Correlated Knowledge Gaps, Pathak et al., CVPR 2023", "statut": "RAPPORTE"},
   {"reference": "Analyzing Dynamic Adversarial Training Data in the Limit, Wallace, Williams, Jia, Kiela, arXiv 2110.08514", "statut": "RAPPORTE"},
   {"reference": "Constitutional Black-Box Monitoring, Storf et al., 2026, arXiv 2603.00829", "statut": "RAPPORTE"},
   {"reference": "Caught in the Act / FIBS, Hollinsworth et al., 2026, arXiv 2610.12445", "statut": "RAPPORTE"},
   {"reference": "Testing Robustness Against Unforeseen Adversaries (UAR), Kang, Sun, Hendrycks, Brown, Steinhardt, 2019, arXiv 1908.08016", "statut": "RAPPORTE"},
   {"reference": "Hints on test data selection, DeMillo, Lipton, Sayward, IEEE Computer 1978", "statut": "SUPPOSE"}
  ]
 },
 {
  "nom": "Approche : la carte de contrôle du pôle — les témoins plantés comme processus surveillé",
  "type": "approche",
  "enonce": "Traiter la boucle elle-même comme le processus sous surveillance, avec les mêmes mathématiques que Q4 : à chaque génération, les verdicts du juge sur les témoins plantés (fiches vraies, fiches fausses, nuls de bibliothèque, mutants aveugles de la fiche Q6) alimentent un e-processus ou une somme cumulée (CUSUM) dont le franchissement arrête la boucle et invalide toutes les promotions depuis le dernier point de contrôle. Le taux de fausses promotions sur témoins devient une courbe publiée avec sa séquence de confiance ; le « coût par famille » de Q5 se lit sur l'horloge de cette carte ; le régime « juge-modèle co-évoluant » de Q2 se mesure en injectant une dérive du juge et en lisant le délai de détection. C'est « faire de la boucle elle-même l'objet mesuré » (pièce E) sous une forme que les occupants ne peuvent pas produire : ils n'ont pas de témoins à vérité connue dans leur boucle.",
  "loi_predictive": {
   "espace_instances": "Générations de la boucle (≥ 50 en simulation, ≥ 20 en vrai), ≥ 10 témoins par génération (moitié vrais, moitié faux, tirés frais d'un vivier tenu par le tiers).",
   "prediction": "(a) Sous dérive injectée du juge (remplacement du juge figé par un juge réaffiné sur les survivantes), la carte déclenche en ≤ 5 générations après le début de la dérive, avec ≤ 1 fausse alarme sur 100 générations sous juge figé ; (b) sous juge figé garanti, pas de déclenchement sur 50 générations et taux de bonne élimination des témoins dans sa séquence de confiance ; (c) une boucle sans carte sous dérive promeut ≥ 20 % de témoins faux à la génération 10.",
   "signe": "+",
   "metrique": "Délai moyen de détection et temps moyen avant fausse alarme (la paire de la détection de rupture) ; taux de fausses promotions sur témoins avec séquence de confiance."
  },
  "perte_traduction": "La « validité de la mesure sous évolution » devient « détection d'une dérive du taux de bonne élimination des témoins » : une dérive qui n'atteint pas les témoins (artefact ciblé sur les vraies fiches) passe inaperçue ; la carte mesure le juge sur ce qu'on lui a planté, pas sur l'inédit.",
  "questions_servies": ["Q2", "Q5", "Q4", "Q6", "nouvelle"],
  "avantage": {
   "source": "organisme",
   "texte": "Témoins plantés, juge figé à mise, archive complète et test final lu une fois existent déjà ; la carte les relie en une garantie séquentielle sur la boucle.",
   "incopiable_parce_que": "Les boucles des occupants n'ont ni témoins à vérité connue ni juge hors des agents (juge = récompense chez MAGIC et AgentSafeEvo ; validation en distribution chez SafeCoEvo) ; ajouter une carte à une boucle dont le juge dérive ne mesure que sa propre dérive. Le calcul est négligeable ; c'est l'architecture (juge figé, tiers, témoins frais) qui manque."
  },
  "originalite": {
   "niveau": "transposition",
   "texte": "Contrôle statistique de procédé (Shewhart, Page) et détection de rupture (Ramtin et al.) appliqués au pôle lui-même ; canaris de 2609.25848 et ancre cachée de 2607.05904 posent le principe sans séquence de confiance ; « la vigilance ne se valide pas sans étiquettes fraîches » (2609.32267) justifie les témoins frais. La réflexivité (la même théorie garde le moniteur et la boucle) n'est pas vue."
  },
  "demande_organisme": {
   "nature": "ajout",
   "texte": "Une carte de contrôle dans le noyau (jamais réécrite par le pôle), alimentée par les verdicts sur témoins ; un vivier de témoins tenu par le tiers, tiré frais à chaque génération ; une règle d'invalidation rétroactive des promotions depuis le dernier point de contrôle."
  },
  "cout": {
   "nature": "processeur",
   "ordre_de_grandeur": "Simulation sur processeur (jours) ; la mesure sur une vraie boucle suit le coût des générations (nœud de dépense)."
  },
  "piege": "Témoins reconnaissables (mémoire à empreinte, gabarits) : le pôle apprend à bien traiter les témoins et mal le reste ; parade : témoins frais, indiscernables en forme des vraies fiches. Fausse sécurité : une carte qui ne déclenche jamais peut être aveugle (témoins trop faciles, dérive hors de portée) ; d'où le test (a) à dérive injectée, obligatoire avant toute lecture de (b).",
  "cosmetique_si": "Le taux de bonne élimination des témoins est à 100 % dès la génération 0 (témoins triviaux), ou si la carte ne déclenche pas sous un juge délibérément corrompu (test (a) échoué).",
  "anteriorite": [
   {"reference": "Quickest Change Detection in Discrete-Time in Presence of a Covert Adversary, Ramtin, Nain, Towsley, 2026, arXiv 2601.20022", "statut": "RAPPORTE"},
   {"reference": "Manuel d'ingénierie statistique du NIST, section 6.3.2.3.1", "statut": "RAPPORTE"},
   {"reference": "Page, 1954, Continuous Inspection Schemes ; Shewhart, 1931, cartes de contrôle", "statut": "SUPPOSE"},
   {"reference": "Optimizing the Score, Losing Sight of the Task, 2026, arXiv 2609.25848", "statut": "RAPPORTE"},
   {"reference": "More Convincing, Not More Correct, 2026, arXiv 2607.05904", "statut": "RAPPORTE"},
   {"reference": "When Can Old Evaluations Certify a New Model?, Mondal et al., 2026, arXiv 2609.32267", "statut": "RAPPORTE"},
   {"reference": "Pay Only for Disagreement, Balachandran, 2026, arXiv 2609.17560", "statut": "RAPPORTE"},
   {"reference": "The Ladder, Blum et Hardt, ICML 2015", "statut": "RAPPORTE"},
   {"reference": "HyperAgents, Zhang et al., 2026, arXiv 2603.19461 (boucle externe de sélection gardée fixe)", "statut": "RAPPORTE"},
   {"reference": "Miconi, EuroGP 2009", "statut": "RAPPORTE"}
  ]
 },
 {
  "nom": "Approche : le prédicteur en quarantaine — date de coupure antérieure et annexes non lues comme épreuve scellée",
  "type": "approche",
  "enonce": "Pour toute question où la théorie est notée comme prévisionniste (Q3 sur grille, Q-pont à coût nul, rejugement Q2, diagonale de l'auto-jeu), séparer trois rôles tenus par trois instances à information strictement croissante : (1) le prédicteur, instance neuve d'un modèle dont la date de coupure déclarée est antérieure à la publication du banc, ou qui n'a reçu qu'une passation sans chiffres rédigée par le tiers, et dont la prédiction est empreintée avant tout accès ; (2) l'apparieur tiers, qui fixe cellules, appariements et règles d'extraction ; (3) l'évaluateur, qui lit une fois les tableaux ou calcule les scores. Les annexes jamais extraites des fichiers PDF (Portable Document Format) deviennent une banque scellée gratuite : on prédit les chiffres qu'elles contiennent (tableaux par environnement, matrices de dégradation croisée des invites ciblées, résultats par modèle) avant de les ouvrir. C'est l'asymétrie de Terekhov et al. (l'attaquant à date de coupure postérieure sait tout du moniteur) renversée en garde : le prédicteur à date de coupure antérieure ne peut rien savoir du résultat. Le protocole se teste lui-même par un témoin non quarantainé.",
  "loi_predictive": {
   "espace_instances": "Campagnes de ≥ 20 quantités publiées non lues par campagne, réparties entre corps de papier (indexé, mémorisable) et annexes (peu indexées) ; deux prédicteurs par campagne : quarantainé et non quarantainé (date de coupure postérieure, accès au corpus).",
   "prediction": "L'erreur absolue médiane du prédicteur non quarantainé est ≤ la moitié de celle du quarantainé sur les quantités du corps de papier (fuite par mémorisation mesurable), et les deux erreurs sont indiscernables sur les quantités d'annexes ; une campagne qui ne montre pas cet écart signale soit une annexe indexée, soit une fuite par la passation.",
   "signe": "+",
   "metrique": "Erreur absolue médiane de prédiction par classe de quantité (corps / annexe) ; empreintes et horodatages des prédictions ; registre des dates de coupure."
  },
  "perte_traduction": "La « fuite » est mesurée par une différence entre deux instances, pas prouvée ; la date de coupure déclarée n'est pas une garantie ; une annexe non indexée aujourd'hui peut l'être demain, ce qui périme la banque scellée. On ne mesure pas la théorie, on mesure la propreté de l'épreuve.",
  "questions_servies": ["Q3", "Q-pont", "Q2", "Q1", "nouvelle"],
  "avantage": {
   "source": "methodes",
   "texte": "Préenregistrement scellé avant toute lecture, contre-lecture par un modèle différent, verdict par sous-agent neuf, et la troisième instance : la quarantaine est leur assemblage avec une garde temporelle.",
   "incopiable_parce_que": "Un occupant qui construit l'attaquant a déjà tout lu : la prédiction scellée n'a de valeur que par l'ordre temporel, et cet ordre est irréversible (une prédiction vue après coup ne vaut rien). Rien à voir avec le calcul : c'est une discipline d'accès que la plupart des pipelines publiés violent par construction (même modèle pour construire, évaluer et discuter)."
  },
  "originalite": {
   "niveau": "transposition",
   "texte": "Rapports enregistrés et marchés de prédiction de réplication (hors champ, SUPPOSÉ) ; jeu tenu à l'écart réutilisable (Dwork et al.) ; canaris anti-entraînement des bancs (MonitoringBench, SLEIGHT-Bench) posent le problème inverse. L'usage des annexes non lues comme épreuve et la date de coupure comme garde du prédicteur ne sont pas vus."
  },
  "demande_organisme": {
   "nature": "ajout",
   "texte": "Le rôle de tiers dans le noyau ; une garde d'empreinte temporelle sur toute prédiction ; un registre des dates de coupure des modèles employés ; une passation « sans chiffres » comme gabarit obligatoire pour le prédicteur, relue par un modèle différent pour y chercher tout chiffre ou nom de résultat."
  },
  "cout": {
   "nature": "processeur",
   "ordre_de_grandeur": "Appels de modèle modestes (deux prédicteurs par campagne) ; aucun calcul."
  },
  "piege": "Fuite par la passation : les extraits eux-mêmes citent des chiffres ; une consigne rédigée par quelqu'un qui a lu les pièces fuit sans le vouloir. Date de coupure non fiable (mises à jour du corpus). Et le témoin non quarantainé peut échouer aussi : alors la « fuite » n'est pas mesurable et la quarantaine ne protège de rien de démontrable.",
  "cosmetique_si": "Les deux prédicteurs obtiennent la même erreur sur le corps de papier ET sur les annexes (aucune fuite détectable, donc aucune protection mesurée), ou si une seule prédiction est scellée après la lecture de son résultat.",
  "anteriorite": [
   {"reference": "Adaptive Attacks on Trusted Monitors Subvert AI Control Protocols, Terekhov et al., 2025, arXiv 2510.09462", "statut": "RAPPORTE"},
   {"reference": "Generalization in Adaptive Data Analysis and Holdout Reuse, Dwork et al., NeurIPS 2015", "statut": "RAPPORTE"},
   {"reference": "The Ladder, Blum et Hardt, ICML 2015", "statut": "RAPPORTE"},
   {"reference": "MonitoringBench, 2605.09684 (exclusion des corpus d'entraînement) ; SLEIGHT-Bench, 2605.16626 (chaînes canari)", "statut": "RAPPORTE"},
   {"reference": "Registered reports, Nosek et Lakens, 2014, Social Psychology", "statut": "SUPPOSE"},
   {"reference": "Evaluating the replicability of social science experiments, Camerer et al., 2018, Nature Human Behaviour", "statut": "SUPPOSE"},
   {"reference": "Série ASVspoof, 2019, arXiv 1904.05441", "statut": "RAPPORTE"},
   {"reference": "Tavallaee et al., 2009, critique de KDD'99 / NSL-KDD", "statut": "RAPPORTE"}
  ]
 }
]}
```