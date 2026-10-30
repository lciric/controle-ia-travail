```json
{"fiches": [
{
 "nom": "Q3 sur grille publiée : prédire les cellules où notre propre sonde échoue",
 "type": "question",
 "enonce": "Une instance de théorie qui ne connaît que la carte des hypothèses (et aucun score de nos moniteurs) prédit-elle, avant le test et contre une référence de permutation ET contre la prédiction naïve « comme les moniteurs publiés », le classement des taux de détection de notre moniteur (sonde sur modèle à 8 milliards de paramètres, plus boîte noire) par cellule de la taxonomie publiée de MonitoringBench (niveaux techniques T, structurels S, d'évasion E) et par catégorie de SLEIGHT-Bench ? La quantité prédite est le vecteur par cellule de NOTRE moniteur, qui n'existe nulle part : elle ne peut être ni mémorisée ni lue après coup. Cette formulation répond au risque de non-conclusion de Q3 « faute de puissance » (une dizaine de familles) : la taxonomie croisée T×S×E fournit des dizaines de cellules peuplées.",
 "loi_predictive": {
  "espace_instances": "Cellules peuplées (≥ 30 trajectoires d'attaque réussies) de la taxonomie MonitoringBench, soit ~25 à 40 cellules sur 2 644 trajectoires, plus les 11 catégories de SLEIGHT-Bench (40 attaques, 10 essais chacune, bénins appariés). Un seul moniteur, non entraîné sur ces bancs (les auteurs de MonitoringBench demandent l'exclusion des corpus d'entraînement : lecture pour évaluation seulement).",
  "prediction": "Corrélation de rang de Spearman ≥ 0,4 entre le classement prédit et le classement observé des cellules, au-delà du 95e centile de 10 000 permutations ; ET au moins égale à celle obtenue par la prédiction naïve « classement des moniteurs modèles publiés par cellule ». Second engagement chiffré : la théorie désigne ≥ 3 cellules « échec » (rappel < 20 %) dont ≥ 2 se confirment.",
  "signe": "+",
  "metrique": "Rappel à 1 % de faux positifs par cellule, seuil calibré sur les 416 trajectoires honnêtes (MonitoringBench) et sur les bénins appariés (SLEIGHT-Bench) ; prédiction empreintée avant le premier score ; test lu une seule fois."
 },
 "perte_traduction": "« Savoir où sa défense casse sans y être attaqué » devient un classement de cellules d'une taxonomie fixée par d'autres, étiquetée a posteriori par un juge modèle ; on perd les familles inédites hors taxonomie et le volet « au fil des générations » (une génération ici, le moniteur est figé). On perd aussi le diffus inter-épisodes : S4 est intra-trajectoire.",
 "questions_servies": ["Q3", "Q-pont", "Q4", "Q6"],
 "avantage": {
  "source": "programme",
  "texte": "La carte des hypothèses existe et son gardien n'a conçu aucun moniteur ; le préenregistrement scellé (méthodes) fait de l'horodatage, et non du calcul, l'objet de la preuve ; la quantité prédite est inédite par construction.",
  "incopiable_parce_que": "Un occupant qui construit l'attaquant tire ses catégories des échecs observés (SLEIGHT-Bench le dit : les catégories sont nées des transcriptions qui ont échappé aux moniteurs) ; sa « prédiction » est a posteriori par construction et ne vaut rien. Un laboratoire mieux doté ne gagne rien : le résultat tient à la séquence scellée (théorie → prédiction → test), pas au calcul. Il faudrait de plus une théorie explicite des hypothèses statistiques du moniteur, qu'aucun occupant ne publie."
 },
 "originalite": {
  "niveau": "transposition",
  "texte": "Le schéma « hypothèses du détecteur → familles d'évasion → vérification » est ancien (détection d'intrusion) et SLEIGHT-Bench le réalise avec une théorie informelle ; la notation de la théorie comme prévisionniste, préenregistrée, par cellule, contre permutation et contre la prédiction naïve, n'a pas été vue (pièce C, Q3)."
 },
 "demande_organisme": {
  "nature": "ajout",
  "texte": "La troisième instance (fixe l'appariement cellules ↔ hypothèses, scelle la prédiction, n'a lu aucune pièce ni aucun score) ; une garde de code qui refuse de lancer l'évaluation si l'empreinte de la prédiction est postérieure au premier score ; un lecteur des formats de trajectoires publiés ; un moniteur dont les données d'entraînement excluent ces bancs."
 },
 "cout": {
  "nature": "depense",
  "ordre_de_grandeur": "Dérivation et préenregistrement sur processeur ; extraction des activations du modèle à 8 milliards de paramètres sur ~3 000 trajectoires longues : quelques heures de processeur graphique (dizaines de dollars) ; boîte noire par appels : centaines de dollars."
 },
 "piege": "Circularité à deux voies. (a) Les cellules et catégories sont nées des échecs de moniteurs modèles : une théorie qui dit « les moniteurs échouent là où la taxonomie le dit » prédit trivialement ; d'où la référence naïve (taux publiés des moniteurs modèles par cellule) que la théorie doit égaler SANS les avoir lus. (b) Le prédicteur est un modèle dont le corpus contient peut-être les papiers ; d'où la prédiction de NOTRE moniteur, jamais publié, et une instance de théorie qui n'a pas lu les pièces. Puissance : 11 catégories seules ne suffisent pas ; les cellules peuplées sont nécessaires. Confusion : les cellules sont confondues avec la longueur de trajectoire et l'étape de raffinement.",
 "cosmetique_si": "La corrélation obtenue n'excède pas celle de la prédiction naïve « comme les moniteurs publiés », ou si le classement prédit est entièrement expliqué par la longueur de trajectoire ou par le seul niveau structurel S.",
 "anteriorite": [
  {"reference": "SLEIGHT-Bench: A Benchmark of Evasion Attacks Against Agent Monitors, Najt, Toft, Tracy, Roger, Benton, 2026, arXiv 2605.16626", "statut": "RAPPORTE"},
  {"reference": "MonitoringBench: Semi-Automated Red-Teaming for Agent Monitoring, Jotautaitė, Martinez, Matthews, Tracy, 2026, arXiv 2605.09684", "statut": "RAPPORTE"},
  {"reference": "Inherited Circuits, Learned Semantics, Fetterman, 2026, arXiv 2606.27091", "statut": "RAPPORTE"},
  {"reference": "Insertion, Evasion, and Denial of Service, Ptacek et Newsham, 1998", "statut": "RAPPORTE"},
  {"reference": "What Happened to Anomaly Detection?, Inoue et Somayaji, 2006, rapport Carleton TR-07-09", "statut": "RAPPORTE"},
  {"reference": "No Free Lunch: The Hazards of Over-Expressive Representations in Anomaly Detection, Reiss, Cohen, Hoshen, arXiv 2306.07284", "statut": "RAPPORTE"},
  {"reference": "Formulating Robustness Against Unforeseen Attacks, Dai, Mahloujifar, Mittal, NeurIPS 2022", "statut": "RAPPORTE"},
  {"reference": "Caught in the Act (jeu FIBS), Hollinsworth, Spies, Diriba, Gleave, Cundy, 2026, arXiv 2610.12445", "statut": "RAPPORTE"},
  {"reference": "Why 6? Defining the Operational Limits of stide, Tan et Maxion, IEEE S&P 2002", "statut": "SUPPOSE"}
 ]
},
{
 "nom": "La diagonale de l'auto-jeu : le score contre l'attaquant co-évolué prédit-il la généralisation ?",
 "type": "question",
 "enonce": "Dans les matrices croisées attaquant × défenseur publiées par les occupants co-évolutifs, le taux de succès d'attaque du défenseur final contre l'attaquant avec lequel il a co-évolué (la « diagonale ») est-il informatif sur son taux contre des familles publiées tenues à l'écart ? Hypothèse : non. La paire co-évoluée converge vers une spécialisation mutuelle (MAGIC : l'attaquant co-entraîné est le plus faible de tous contre son propre défenseur) ou, quand l'attaquant reste adaptatif à l'évaluation, la diagonale surestime (AgentSafeEvo : attaquant final bien plus fort que les bancs externes). Dans les deux cas la diagonale n'est pas une mesure de généralisation — c'est ce que le refus de construire l'attaquant nous évite par construction.",
 "loi_predictive": {
  "espace_instances": "Paires (défenseur, matrice) extraites des occupants qui publient à la fois la diagonale et ≥ 2 familles externes : MAGIC (tableaux 3 et 10), AgentSafeEvo (évaluation croisée par étape et quatre bancs), EvoSafety (tableau 2 : compétences vues / non vues / attaquant évolué), EvoDefense (tableaux 1, 2, 3), RvB (gardes par tour contre quatre bancs externes), SafeCoEvo si une diagonale existe ; attendu : 5 à 8 matrices, 15 à 30 paires.",
  "prediction": "Corrélation de rang < 0,3 entre le taux sur la diagonale et le taux médian sur familles externes, à travers les paires ; écart absolu > 15 points dans ≥ 70 % des paires, dans les deux sens (sous-estimation quand la paire est figée, surestimation quand l'attaquant est adaptatif à l'évaluation) ; quand plusieurs tours sont publiés, le ratio diagonale/externe s'éloigne de 1 avec le nombre de tours.",
  "signe": "0",
  "metrique": "Taux de succès d'attaque tel que publié, au point de fonctionnement et avec le juge de l'occupant ; règles d'extraction fixées avant lecture des tableaux."
 },
 "perte_traduction": "Le mécanisme (spécialisation de paire, Goodhart réciproque) devient une méta-analyse de tableaux hétérogènes ; on ne mesure pas la dynamique interne de la paire, seulement son empreinte publiée. Les points de fonctionnement et les juges diffèrent d'un papier à l'autre.",
 "questions_servies": ["nouvelle", "Q1", "Q2", "Q5"],
 "avantage": {
  "source": "methodes",
  "texte": "Le refus de construire l'attaquant : nous n'avons pas de diagonale à défendre, et notre aptitude est la généralisation sur familles tenues par un tiers, jamais le score contre un adversaire maison.",
  "incopiable_parce_que": "Pas une question de calcul mais de conflit d'intérêt : chaque occupant publie sa diagonale comme preuve centrale ; l'auditer, c'est auditer sa propre revendication. De plus, une fois la paire construite, c'est le seul objet qu'il peut mesurer sans tiers ; il ne peut pas, sans changer de méthode, produire une mesure qui ne passe pas par son attaquant."
 },
 "originalite": {
  "niveau": "transposition",
  "texte": "Miconi (progrès historique pris pour global), Czempin et Gleave (l'adversaire unique surajuste), Tramèr et al. (attaques adaptatives) occupent le principe ; la mesure en méta-analyse de matrices publiées de co-évolution défensive n'a pas été vue dans les pièces."
 },
 "demande_organisme": {
  "nature": "rien",
  "texte": "Lecture de fichiers PDF (Portable Document Format) et extraction préenregistrée par un sous-agent neuf ; vérification R7 sur PDF empreinté avant tout chiffre."
 },
 "cout": {
  "nature": "processeur",
  "ordre_de_grandeur": "Quelques jours d'extraction et de contre-lecture ; aucun calcul."
 },
 "piege": "Sélection après lecture : fixer la liste d'occupants, les tableaux à lire et la règle d'appariement diagonale ↔ externe AVANT d'ouvrir les PDF, par la troisième instance. Hétérogénéité des juges (MAGIC montre que Qwen3Guard et GPT-4o divergent sur les défenseurs forts) et des points de fonctionnement : rapporter par papier, jamais en moyenne globale. Tables incomplètes : une matrice sans familles externes est écartée, pas interprétée.",
 "cosmetique_si": "Moins de 5 matrices exploitables, ou si le résultat se réduit à « un attaquant adaptatif est plus fort qu'un banc figé », déjà établi (Terekhov et al., Tramèr et al.).",
 "anteriorite": [
  {"reference": "MAGIC: A Co-Evolving Attacker–Defender Adversarial Game for Robust LLM Safety, Wen, He et al., 2026, arXiv 2602.01539", "statut": "RAPPORTE"},
  {"reference": "AgentSafeEvo: Adversarial Co-Evolution for LLM Agent Safety, Wang, Wen et al., 2026, arXiv 2610.19422", "statut": "RAPPORTE"},
  {"reference": "EvoSafety: Model-Agnostic Lifelong LLM Safety via Externalized Attack-Defense Co-Evolution, Zhang et al., 2026, arXiv 2605.13411", "statut": "RAPPORTE"},
  {"reference": "EvoDefense: Co-Evolving Black-Box Defense with Large Language Models, Li et al., 2026, arXiv 2605.31140", "statut": "RAPPORTE"},
  {"reference": "RvB: Automating AI System Hardening via Iterative Red-Blue Games, Huang, Liu, Zhang et al., 2026, arXiv 2601.19726", "statut": "RAPPORTE"},
  {"reference": "SafeCoEvo, Cheng et al., 2026, arXiv 2609.36580", "statut": "RAPPORTE"},
  {"reference": "Miconi, EuroGP 2009, progrès local / historique / global en co-évolution", "statut": "RAPPORTE"},
  {"reference": "Czempin et Gleave, arXiv 2208.05083, entraînement par population et exploitabilité", "statut": "RAPPORTE"},
  {"reference": "On Adaptive Attacks to Adversarial Example Defenses, Tramèr et al., NeurIPS 2020", "statut": "RAPPORTE"},
  {"reference": "Adaptive Attacks on Trusted Monitors Subvert AI Control Protocols, Terekhov et al., 2025, arXiv 2510.09462", "statut": "RAPPORTE"}
 ]
},
{
 "nom": "Q2 par méta-audit : combien de promotions publiées survivraient à un juge garanti ?",
 "type": "question",
 "enonce": "Si l'on rejoue les courbes tour par tour publiées par les occupants (EvoDefense tours 1, 2, 5, 10 ; SafeCoEvo époques 0 à 15 sur une validation de 200 épisodes avec choix de la meilleure époque ; RvB tours 1 à 4 ; AgentSafeEvo par étape ; MAGIC) sous un test de promotion certifié (séquence de confiance empirique-Bernstein, inégalité de Ville, budget d'erreur composé δ = 0,05 sur toute la chaîne de promotions), quelle part des « améliorations » tour-à-tour rapportées serait promue, et quelle part des promotions effectivement faites (choix du meilleur point de contrôle) est une fausse promotion sous composition ? C'est Q2 (« le juge figé garanti est-il un résultat ou une hygiène ? ») tranchée sur leur matériau : si presque tout survit, Q2 n'est qu'hygiène ; si la majorité tombe, la garantie est un résultat.",
 "loi_predictive": {
  "espace_instances": "30 à 60 transitions tour-à-tour reconstituées des tableaux publiés, avec les effectifs déclarés (320 items pour EvoDefense, 200 épisodes de validation pour SafeCoEvo, 100 invites pour RvB, trois exécutions pour AgentSafeEvo).",
  "prediction": "Moins de 40 % des transitions rapportées comme améliorations franchissent le test certifié ; aucune transition au-delà du tour 2 d'EvoDefense ne passe (écarts < 3 points sur n = 320) ; le gain de première étape (tour 0 → 1 ou 2) est promu partout ; sous composition sur la chaîne de points de contrôle, au moins un occupant voit sa promotion finale retomber sous le seuil.",
  "signe": "-",
  "metrique": "Part de transitions promues à δ composé, calculée sous deux bornes (items indépendants / parfaitement appariés) quand les données par item manquent ; verdict par chaîne."
 },
 "perte_traduction": "« Qu'est-ce qui doit rester fixe pour que la mesure reste valide » devient « combien d'améliorations publiées sont statistiquement nulles » ; on perd le régime juge-modèle co-évoluant (non rejouable sans leurs exécutions) et la mesure comparative des trois régimes sur notre propre boucle.",
 "questions_servies": ["Q2", "Q5", "nouvelle"],
 "avantage": {
  "source": "methodes",
  "texte": "Le juge à mise contre bibliothèque de nuls et l'outillage e-processus existent déjà ; aucun conflit d'intérêt : nous n'avons pas de courbe à défendre.",
  "incopiable_parce_que": "Techniquement copiable à bas coût, mais structurellement non fait : l'occupant qui auditerait ses promotions sous garantie composée perdrait l'essentiel de ses courbes ; sa sélection est en distribution (SafeCoEvo : la validation partage six scénarios avec le flux d'évolution) et son juge sert aussi de récompense (MAGIC, AgentSafeEvo). L'avantage est l'indépendance plus l'approche, pas le calcul."
 },
 "originalite": {
  "niveau": "inedite",
  "texte": "La promotion certifiée par e-processus est occupée (2609.17560, 2609.32267), le cadrage Goodhart aussi (2609.25848), le rapport graines × itérations aussi (2609.19799) ; leur application rétrospective aux chaînes de promotion publiées de la co-évolution défensive n'a pas été vue."
 },
 "demande_organisme": {
  "nature": "modification",
  "texte": "Une entrée du juge à mise acceptant des séries externes (effectifs et taux publiés, bornes d'appariement) au lieu des issues de notre banque."
 },
 "cout": {
  "nature": "processeur",
  "ordre_de_grandeur": "Quelques jours ; calcul négligeable."
 },
 "piege": "Sans données par item, l'approximation binomiale ignore la corrélation entre tours (mêmes items réévalués → test apparié plus puissant) : notre « moins de 40 % » peut être un artefact de la borne indépendante. Parade : rapporter les deux bornes et demander les journaux (EvoDefense annonce du code, RvB archive ses artefacts). Autre piège : l'évaluation finale sur jeu tenu à l'écart (SafeCoEvo, RvB) n'est pas une promotion de chaîne ; ne pas la compter comme telle.",
 "cosmetique_si": "Toutes les transitions sont promues même sous la borne appariée : les occupants n'ont alors pas de problème de fausses promotions à leur effectif, et Q2 se réduit à une hygiène.",
 "anteriorite": [
  {"reference": "Pay Only for Disagreement: Certified No-Regression Verdicts for Model Updates, Balachandran, 2026, arXiv 2609.17560", "statut": "RAPPORTE"},
  {"reference": "When Can Old Evaluations Certify a New Model?, Mondal et al., 2026, arXiv 2609.32267", "statut": "RAPPORTE"},
  {"reference": "Optimizing the Score, Losing Sight of the Task, 2026, arXiv 2609.25848", "statut": "RAPPORTE"},
  {"reference": "Evolution or Illusion?, IBM, 2026, arXiv 2609.19799", "statut": "RAPPORTE"},
  {"reference": "Generalization in Adaptive Data Analysis and Holdout Reuse, Dwork et al., NeurIPS 2015, arXiv 1506.02629", "statut": "RAPPORTE"},
  {"reference": "The Ladder, Blum et Hardt, ICML 2015, arXiv 1502.04585", "statut": "RAPPORTE"},
  {"reference": "Waudby-Smith et Ramdas, 2024, séquences de confiance empirique-Bernstein", "statut": "RAPPORTE"},
  {"reference": "SafeCoEvo, 2609.36580 ; EvoDefense, 2605.31140 ; RvB, 2601.19726 ; AgentSafeEvo, 2610.19422 ; MAGIC, 2602.01539", "statut": "RAPPORTE"}
 ]
},
{
 "nom": "Q4 par l'axe structurel publié : dilution à dommage constant, même score, deux règles",
 "type": "question",
 "enonce": "Pour un moniteur conçu ou sélectionné sur des familles concentrées (niveaux structurels S1–S2 de MonitoringBench), le rappel décroît-il avec la dilution structurelle (S3, S4 ; attaques graduelles contre positionnelles de Hills et al. ; K = 1, 3, 9 agents de Makins et al.) à dommage total constant, selon un coude prédit par le lemme du plafond d'horizon (chute franche quand la divergence par pas multipliée par l'horizon effectif passe sous l'unité) ; et une règle séquentielle (somme cumulée CUSUM ou e-valeurs) appliquée aux MÊMES scores par pas récupère-t-elle une part prédite de cette chute, là où la règle « seuil par pas » ne le peut pas ? Le coude est préenregistré à partir des seuls scores S1–S2, avant lecture de S3–S4.",
 "loi_predictive": {
  "espace_instances": "Trajectoires d'attaque réussies de MonitoringBench étiquetées S1 à S4 (2 644 ; cellule S4 attendue ≥ 100), stratifiées par niveau technique T et stratégie E ; familles graduelle/positionnelle de Hills (n = 120 / 600) et séries K de Makins (FakeLab, sur demande) si accessibles ; notre moniteur : sonde sur modèle à 8 milliards de paramètres plus boîte noire, scores par pas, non entraîné sur ces bancs.",
  "prediction": "(i) Règle « max par pas » : rappel à 1 % de faux positifs par trajectoire chute de ≥ 25 points de S1–S2 à S4 à T et E fixés ; (ii) règle séquentielle sur les mêmes scores, calibrée au même 1 % trajectoire : récupère ≥ la moitié de cette chute sur S4 ; (iii) le niveau S du coude observé coïncide avec le coude préenregistré depuis S1–S2 (tolérance d'un niveau).",
  "signe": "-",
  "metrique": "Rappel à 1 % de faux positifs par trajectoire, seuil calibré sur les 416 trajectoires honnêtes, deux règles de décision sur scores identiques ; comparaison au coude préenregistré."
 },
 "perte_traduction": "Le diffus « entre épisodes et entre agents » devient surtout « réparti dans une trajectoire » (S4 est intra-épisode) ; le vrai inter-épisodes dépend de l'accès aux données de Hills et Makins. Le moniteur est figé : le volet « boucle sélectionnée sur du concentré » n'est pas servi ici. Le dommage total « constant » est approché par la réussite de la tâche secondaire, pas mesuré.",
 "questions_servies": ["Q4", "Q7", "Q-pont", "Q3"],
 "avantage": {
  "source": "programme",
  "texte": "Un lemme formel du coude (à comparer d'abord sur PDF à Ramtin et al. et Gualandi et al., nœud N-A : s'il est couvert, il devient antécédent cité et la prédiction reste la nôtre), l'agrégateur séquentiel, et la boîte blanche sur poids ouverts appliquée aux traces publiées.",
  "incopiable_parce_que": "Makins et Hills construisent l'attaquant et choisissent la dilution après coup ; leur décomposition (dilution 25 %, récit de couverture 53 %, 38–43 % inexpliqué) est descriptive. Aucun occupant ne détient une prédiction préenregistrée du coude dérivée d'hypothèses du moniteur ; la valeur est dans l'engagement avant lecture, pas dans le calcul."
 },
 "originalite": {
  "niveau": "transposition",
  "texte": "« Même score, deux règles » est occupé hors champ (Shewhart contre CUSUM, Urbina et al.) ; l'agrégation déployable est partielle en contrôle (Wen et al., TRACE, link-tracker de Hills) ; la confrontation d'un moniteur d'agent à un coude préenregistré issu de la détection de rupture n'a pas été vue."
 },
 "demande_organisme": {
  "nature": "modification",
  "texte": "L'agrégateur séquentiel doit accepter des scores par pas externes ; ajout d'un lecteur des formats de trajectoires publiés (lignes JSON) ; strate « diffus / concentré » de la banque étendue aux étiquettes S."
 },
 "cout": {
  "nature": "depense",
  "ordre_de_grandeur": "Activations du modèle à 8 milliards sur ~3 000 trajectoires : dizaines de dollars de processeur graphique (à mutualiser avec la fiche Q3) ; boîte noire par appels : centaines de dollars."
 },
 "piege": "Confusion de la dilution avec T et E (le raffinement rééquilibre les catégories) et sélection : les S4 réussies ont survécu au raffinement contre trois moniteurs de développement, donc sont les plus discrètes. Parade : stratifier par T et E, comparer raffinées et élicitées. Autre piège : la règle séquentielle « gagne » trivialement si son seuil est plus permissif ; MonitoringBench note qu'1 % par pas compose à 6,7–17,4 % par trajectoire : calibrer les deux règles au même taux trajectoire.",
 "cosmetique_si": "La chute (i) disparaît une fois stratifiée par T et E, ou si la règle séquentielle n'apporte rien au-delà d'un « max » recalibré par trajectoire.",
 "anteriorite": [
  {"reference": "Multi-Agent AI Control: Distributed Attacks Hamper Per-Instance Monitors, Angelini, Makins, Shams, Phuong, 2026, arXiv 2607.07368", "statut": "RAPPORTE"},
  {"reference": "Distributed Attacks in Persistent-State AI Control, Hills, Caspary, Cooper Stickland, 2026, arXiv 2607.02514", "statut": "RAPPORTE"},
  {"reference": "MonitoringBench, Jotautaitė et al., 2026, arXiv 2605.09684", "statut": "RAPPORTE"},
  {"reference": "Quickest Change Detection in Discrete-Time in Presence of a Covert Adversary, Ramtin, Nain, Towsley, 2026, arXiv 2601.20022", "statut": "RAPPORTE"},
  {"reference": "Quickest Change Detection in Continuous-Time in Presence of a Covert Adversary, Ramtin, Nain, Towsley, 2025, arXiv 2509.17778", "statut": "RAPPORTE"},
  {"reference": "Gualandi, Maggio, Papadopoulos, MED 2022, plafond lié à l'horizon contre CUSUM", "statut": "RAPPORTE"},
  {"reference": "Limiting the Impact of Stealthy Attacks on Industrial Control Systems, Urbina et al., ACM CCS 2016", "statut": "RAPPORTE"},
  {"reference": "Adaptive Deployment of Untrusted LLMs Reduces Distributed Threats, Wen et al., ICLR 2025, arXiv 2411.17693", "statut": "RAPPORTE"},
  {"reference": "TRACE, Mittapalli et al., 2026, arXiv 2606.07054", "statut": "RAPPORTE"},
  {"reference": "Diffuse AI Control on Fuzzy Tasks, Terekhov, Gulcehre, Hebbar, Benton, 2026, arXiv 2606.08892", "statut": "RAPPORTE"},
  {"reference": "Lorden 1971 ; Moustakides 1986 (optimalité de CUSUM), cités par Ramtin et al.", "statut": "RAPPORTE"},
  {"reference": "Manuel d'ingénierie statistique du NIST, section 6.3.2.3.1, Shewhart contre CUSUM", "statut": "RAPPORTE"}
 ]
},
{
 "nom": "Q-pont à coût nul : fabriqué (SLEIGHT-Bench) contre exécuté (MonitoringBench), par catégorie appariée scellée",
 "type": "question",
 "enonce": "Pour un même moniteur figé (le nôtre), le taux de détection par catégorie sur les transcriptions fabriquées de SLEIGHT-Bench (sorties d'outils inventées, auteurs humains, vérificateurs de réalisme) prédit-il le taux sur les trajectoires réellement exécutées de MonitoringBench (BashArena), catégorie par catégorie appariée — l'appariement étant fixé par un tiers AVANT toute lecture de taux ? En miroir : les taux publiés des moniteurs modèles communs aux deux bancs sont-ils corrélés par catégorie appariée ? Cette version de Q-pont ne dépend pas des propriétés dérivées par Q3 : les propriétés sont les catégories publiées. C'est un désaccord avec l'ordre de la pièce B : Q-pont peut commencer avant Q3, et l'ordre n'a pas à attendre le scellement de Q3 pour cette expérience.",
 "loi_predictive": {
  "espace_instances": "6 à 8 paires de catégories appariables entre les 11 classes SLEIGHT-Bench et les niveaux T×S×E de MonitoringBench (par exemple : attaque répartie ↔ S4 ; nommage plausible ↔ E1 ; charge dans contenu long ↔ E3 ; persuasion ↔ E4 — l'appariement exact est scellé par le tiers) ; un moniteur à nous sur les deux bancs ; plus les moniteurs publiés communs.",
  "prediction": "Corrélation de rang de Spearman ≥ 0,5 sur les paires « visibles dans le texte » (nommage, contenu long, obfuscation) et < 0,2 sur les paires qui reposent sur l'état, la persuasion ou l'ambiguïté d'autorisation — l'effondrement attendu par Kirch et al. pour les propriétés « ambiguës dans le texte ». Prédiction annexe : la corrélation ne dépasse pas celle d'un appariement aléatoire de même taille si les paires « état/persuasion » sont incluses.",
  "signe": "+",
  "metrique": "Rappel à 1 % de faux positifs par catégorie ; calibration sur bénins appariés (SLEIGHT-Bench) et sur trajectoires honnêtes (MonitoringBench) ; rang de Spearman par sous-ensemble de paires, préenregistré."
 },
 "perte_traduction": "Le « réel » reste instruit, raffiné contre des moniteurs et à sabotage injecté ; les « propriétés P » sont des catégories de banc, pas des statistiques prédites du moniteur ; 6 à 8 paires donnent une puissance faible : le résultat est un signal d'alerte, pas une validation de la voie synthétique.",
 "questions_servies": ["Q-pont", "Q3", "Q1", "Q6"],
 "avantage": {
  "source": "methodes",
  "texte": "L'appariement scellé par un tiers avant lecture, et un seul moniteur boîte blanche (programme) mesuré sur les deux bancs, alors que les bancs publiés ont des moniteurs différents (Opus 4.5 contre Opus 4.6).",
  "incopiable_parce_que": "Les deux bancs viennent des mêmes équipes, qui n'ont aucune incitation à publier que l'un ne prédit pas l'autre ; un occupant qui construit ses transcriptions choisit l'appariement après avoir vu les taux, ce qui fabrique la corrélation. L'enjeu est le scellement, pas le calcul."
 },
 "originalite": {
  "niveau": "transposition",
  "texte": "Métrique de prédictivité simulation-réel (Kadian et al.) et comparaison de classements d'anomalies synthétiques contre réelles (Steinbuss et Böhm) hors champ ; dans le contrôle, Storf et al. et le billet de Redwood mesurent un transfert global, jamais par propriété appariée."
 },
 "demande_organisme": {
  "nature": "ajout",
  "texte": "La troisième instance pour l'appariement ; sinon rien : mêmes lecteurs et mêmes activations que les fiches Q3 et Q4."
 },
 "cout": {
  "nature": "depense",
  "ordre_de_grandeur": "Nulle si mutualisée avec l'extraction d'activations des fiches Q3 et Q4 ; sinon dizaines de dollars."
 },
 "piege": "L'appariement EST le résultat : fait après lecture, la corrélation est fabriquée ; parade : scellement par le tiers et test contre appariements aléatoires. Effectifs : certaines classes SLEIGHT-Bench comptent une ou deux attaques ; exclure toute paire à n < 3 attaques. Raffinement : les trajectoires MonitoringBench ont été rendues discrètes contre trois moniteurs, ce qui abaisse mécaniquement le « réel ».",
 "cosmetique_si": "L'appariement scellé ne fait pas mieux que des appariements aléatoires de même taille, ou si la corrélation disparaît quand on retire la seule paire « attaque répartie ↔ S4 ».",
 "anteriorite": [
  {"reference": "SLEIGHT-Bench, Najt et al., 2026, arXiv 2605.16626", "statut": "RAPPORTE"},
  {"reference": "MonitoringBench, Jotautaitė et al., 2026, arXiv 2605.09684", "statut": "RAPPORTE"},
  {"reference": "Sim2Real Predictivity, Kadian et al., 2019, arXiv 1912.06321", "statut": "RAPPORTE"},
  {"reference": "The Impact of Off-Policy Training Data on Probe Generalisation, Kirch, Dower, Skapars et al., 2025, arXiv 2511.17408", "statut": "RAPPORTE"},
  {"reference": "Constitutional Black-Box Monitoring for Scheming in LLM Agents, Storf, Barton-Cooper, Peters-Gill, Hobbhahn, 2026, arXiv 2603.00829", "statut": "RAPPORTE"},
  {"reference": "Steinbuss et Böhm, 2020, arXiv 2004.06947, anomalies synthétiques caractérisables", "statut": "RAPPORTE"},
  {"reference": "Simulated control evaluations, Olmo, Zhang, Tracy, Redwood Research, billet du 23 octobre 2026", "statut": "RAPPORTE"},
  {"reference": "Hesford et al., arXiv 2403.17458, inversion de classements entre jeux de détection d'intrusion", "statut": "RAPPORTE"}
 ]
},
{
 "nom": "Q6 sur bancs d'agents : la part de provenance dans le rappel, puis par tour",
 "type": "question",
 "enonce": "Quelle part du rappel d'une sonde (entraînée hors de ces bancs, par exemple sur le jeu FIBS, Falsehoods in Broad Settings) ou d'un moniteur boîte noire, mesuré sur les bancs d'agents publiés, est expliquée par la provenance de la trajectoire (élicitée contre raffinée ; stratégie humaine contre agent de reconnaissance ; STRIDE contre Gloom contre ControlArena ; fabriquée contre exécutée) plutôt que par le sabotage — et, dans une boucle de sélection de moniteurs non contrôlée, cette part croît-elle de génération en génération ? Le volet statique est l'instrument (occupé en principe par Fomin et Lin et al., jamais sur des trajectoires d'agents) ; le volet « par tour » est le résultat distinctif.",
 "loi_predictive": {
  "espace_instances": "Statique : ~3 000 trajectoires MonitoringBench à provenance connue (élicitées / raffinées, quatre sources), 43 transcriptions SLEIGHT-Bench avec bénins appariés, trajectoires ControlArena si accessibles ; activations d'un modèle à 8 milliards de paramètres lisant les transcriptions. Dynamique : ≥ 5 générations de notre boucle sur ces familles, avec et sans contrôle de provenance.",
  "prediction": "Statique : un classifieur de provenance sur activations atteint ≥ 85 % (hasard 25–50 %) ; projeter hors des 16 principales directions de provenance dégrade le rappel de ≥ 2 points en moyenne avec hétérogénéité par source de ± 20 points (schéma de Fomin : −1,75 point moyen, −34 à +21 par jeu) ; rétention de coefficients < 0,5 pour ≥ 25 % des 50 traits principaux. Dynamique : sans contrôle, la part de rappel attribuable à la provenance augmente d'au moins 5 points par génération ; avec témoins bénins appariés par provenance dans la sélection, elle reste stable.",
  "signe": "+",
  "metrique": "Exactitude du classifieur de provenance ; rappel à 1 % de faux positifs avant et après projection ; rétention de coefficients par tour (protocole « un jeu de données laissé de côté », LODO)."
 },
 "perte_traduction": "L'« artefact du générateur » devient « provenance étiquetée par les auteurs des bancs » ; on ne mesure pas l'artefact de notre propre générateur de familles tant que la boucle n'existe pas, et la provenance est confondue avec la difficulté (les trajectoires raffinées sont plus discrètes par construction).",
 "questions_servies": ["Q6", "Q-pont", "Q1", "Q5"],
 "avantage": {
  "source": "organisme",
  "texte": "Le bras « fuite textuelle » (N-053), la mémoire qui refuse les redites et les tâches fraîches, plus la boîte blanche sur poids ouverts (programme) : la rétention de coefficients exige l'accès aux activations.",
  "incopiable_parce_que": "Les occupants à moniteur-modèle fermé ne peuvent pas mesurer la rétention ni projeter hors du sous-espace de provenance ; ceux qui construisent l'attaquant produisent eux-mêmes la signature (le raffinement par un même modèle est une provenance) et n'ont pas intérêt à la mesurer. Un laboratoire mieux doté pourrait faire le volet statique ; le volet par tour exige une boucle à juge figé et témoins appariés, que personne n'a."
 },
 "originalite": {
  "niveau": "transposition",
  "texte": "Fomin (LODO, rétention) et Lin et al. (identité du modèle) sur invites et sous-performance ; Pathak et al. pour la migration d'artefacts en bloc entre tours ; Wallace et al. pour « la collecte adversariale ne purge pas » ; le suivi par tour dans une boucle de moniteurs d'agents n'a pas été vu."
 },
 "demande_organisme": {
  "nature": "modification",
  "texte": "Étiqueter la provenance dans la banque et dans la strate des familles ; brancher le bras « fuite textuelle » sur des sources externes ; témoins bénins appariés par provenance dans la sélection (invariant N-053)."
 },
 "cout": {
  "nature": "depense",
  "ordre_de_grandeur": "Statique : dizaines de dollars (mêmes activations que les fiches précédentes). Dynamique : générations de la boucle, nœud de dépense pour Lazar."
 },
 "piege": "Provenance et difficulté confondues : un classifieur de provenance qui apprend la difficulté est légitime. Parade : témoins bénins appariés par provenance (SLEIGHT-Bench en fournit), ligne de base « honnête contre honnête » de Lin et al., et comparaison à provenance fixée. Autre piège : les directions de provenance et de sabotage se recouvrent (Fomin) ; la projection « redistribue » plutôt qu'elle ne réduit : rapporter par source, jamais en moyenne seule.",
 "cosmetique_si": "La projection hors provenance ne change pas le rappel et la rétention dépasse 0,8 partout : l'artefact n'explique alors rien sur ces bancs et Q6 n'est qu'une précaution.",
 "anteriorite": [
  {"reference": "When Benchmarks Lie, Fomin, 2026, arXiv 2602.14161", "statut": "RAPPORTE"},
  {"reference": "When Lie Detectors Learn Model Identity, Lin, Bernabeu-Perez, Arnav, Wells, Phuong, ICLR 2026", "statut": "RAPPORTE"},
  {"reference": "Building Better Deception Probes Using Targeted Instruction Pairs, Natarajan et al., 2026, arXiv 2602.01425", "statut": "RAPPORTE"},
  {"reference": "Sequential Training of GANs Against GAN-Classifiers Reveals Correlated Knowledge Gaps, Pathak et al., CVPR 2023", "statut": "RAPPORTE"},
  {"reference": "Analyzing Dynamic Adversarial Training Data in the Limit, Wallace, Williams, Jia, Kiela, arXiv 2110.08514", "statut": "RAPPORTE"},
  {"reference": "Constitutional Black-Box Monitoring, Storf et al., 2026, arXiv 2603.00829 (artefacts du synthétique exploités par l'optimisation)", "statut": "RAPPORTE"},
  {"reference": "Caught in the Act / FIBS, Hollinsworth et al., 2026, arXiv 2610.12445", "statut": "RAPPORTE"},
  {"reference": "Testing Robustness Against Unforeseen Adversaries (UAR, normalisation par famille), Kang, Sun, Hendrycks, Brown, Steinhardt, 2019, arXiv 1908.08016", "statut": "RAPPORTE"}
 ]
},
{
 "nom": "Approche : la carte de contrôle du pôle — les témoins plantés comme processus surveillé",
 "type": "approche",
 "enonce": "Traiter la boucle elle-même comme le processus sous surveillance, avec les mêmes mathématiques que Q4 : à chaque génération, les verdicts du juge sur les témoins plantés (fiches vraies, fiches fausses, nuls de bibliothèque) alimentent un e-processus ou une somme cumulée (CUSUM) dont le franchissement arrête la boucle et invalide toutes les promotions depuis le dernier point de contrôle. Le taux de fausses promotions sur témoins devient une courbe publiée avec sa séquence de confiance ; le « coût par famille » de Q5 se lit sur l'horloge de cette carte ; et le régime « juge-modèle co-évoluant » de Q2 se mesure en simulant une dérive du juge et en lisant le délai de détection. C'est « faire de la boucle elle-même l'objet mesuré » (pièce E) sous une forme que les occupants ne peuvent pas produire : ils n'ont pas de témoins à vérité connue dans leur boucle.",
 "loi_predictive": {
  "espace_instances": "Générations de la boucle (≥ 50 en simulation, ≥ 20 en vrai), ≥ 10 témoins par génération (moitié vrais, moitié faux, tirés frais d'un vivier tenu par le tiers).",
  "prediction": "(a) Sous dérive injectée du juge (remplacement du juge figé par un juge réaffiné sur les survivantes), la carte déclenche en ≤ 5 générations après le début de la dérive, avec ≤ 1 fausse alarme sur 100 générations sous juge figé ; (b) sous juge figé garanti, la carte ne déclenche pas sur 50 générations et le taux de bonne élimination des témoins reste dans sa séquence de confiance ; (c) une boucle sans carte sous dérive promeut ≥ 20 % de témoins faux à la génération 10.",
  "signe": "+",
  "metrique": "Délai moyen de détection et temps moyen avant fausse alarme (la paire ADD / AT2FA de la détection de rupture) ; taux de fausses promotions sur témoins avec séquence de confiance."
 },
 "perte_traduction": "La « validité de la mesure sous évolution » devient « détection d'une dérive du taux de bonne élimination des témoins » : une dérive qui n'atteint pas les témoins (artefact ciblé sur les vraies fiches) passe inaperçue ; la carte mesure le juge sur ce qu'on lui a planté, pas sur l'inédit.",
 "questions_servies": ["Q2", "Q5", "Q4", "nouvelle"],
 "avantage": {
  "source": "organisme",
  "texte": "Témoins plantés, juge figé à mise, archive complète et test final lu une fois existent déjà ; la carte les relie en une garantie séquentielle sur la boucle.",
  "incopiable_parce_que": "Les boucles des occupants n'ont ni témoins à vérité connue ni juge hors des agents (le juge sert de récompense chez MAGIC et AgentSafeEvo ; validation en distribution chez SafeCoEvo) ; ajouter une carte à une boucle dont le juge dérive ne mesure que sa propre dérive. Le calcul est négligeable ; c'est l'architecture (juge figé, tiers, témoins frais) qui manque."
 },
 "originalite": {
  "niveau": "transposition",
  "texte": "Contrôle statistique de procédé (Shewhart, Page) et détection de rupture (Ramtin et al.) vers le pôle lui-même ; canaris de 2609.25848 et ancre cachée de 2607.05904 posent le principe sans séquence de confiance ; « la vigilance ne se valide pas sans étiquettes fraîches » (2609.32267) justifie les témoins frais. Réflexivité (la même théorie garde le moniteur et la boucle) non vue."
 },
 "demande_organisme": {
  "nature": "ajout",
  "texte": "Une carte de contrôle dans le noyau (jamais réécrite par le pôle), alimentée par les verdicts sur témoins ; un vivier de témoins tenu par le tiers et tiré frais à chaque génération ; une règle d'invalidation rétroactive des promotions depuis le dernier point de contrôle."
 },
 "cout": {
  "nature": "processeur",
  "ordre_de_grandeur": "Simulation sur processeur (jours) ; la mesure sur une vraie boucle suit le coût des générations (nœud de dépense)."
 },
 "piege": "Les témoins deviennent reconnaissables (mémoire à empreinte, gabarits) : le pôle apprend à bien traiter les témoins et mal le reste ; parade : témoins frais du vivier du tiers, indiscernables en forme des vraies fiches. Fausse sécurité : une carte qui ne déclenche jamais peut être aveugle (témoins trop faciles, dérive hors de leur portée) ; d'où le test (a) à dérive injectée, obligatoire avant toute lecture de (b).",
 "cosmetique_si": "Le taux de bonne élimination des témoins est à 100 % dès la génération 0 (témoins triviaux), ou si la carte ne déclenche pas sous un juge délibérément corrompu (test (a) échoué).",
 "anteriorite": [
  {"reference": "Quickest Change Detection in Discrete-Time in Presence of a Covert Adversary, Ramtin, Nain, Towsley, 2026, arXiv 2601.20022", "statut": "RAPPORTE"},
  {"reference": "Manuel d'ingénierie statistique du NIST, section 6.3.2.3.1", "statut": "RAPPORTE"},
  {"reference": "Page, 1954, Continuous Inspection Schemes (somme cumulée) ; Shewhart, 1931, cartes de contrôle", "statut": "SUPPOSE"},
  {"reference": "Optimizing the Score, Losing Sight of the Task, 2026, arXiv 2609.25848 (canaris)", "statut": "RAPPORTE"},
  {"reference": "More Convincing, Not More Correct, 2026, arXiv 2607.05904 (ancre cachée)", "statut": "RAPPORTE"},
  {"reference": "When Can Old Evaluations Certify a New Model?, Mondal et al., 2026, arXiv 2609.32267 (prix de la vigilance)", "statut": "RAPPORTE"},
  {"reference": "Pay Only for Disagreement, Balachandran, 2026, arXiv 2609.17560 (composition sur une suite de promotions)", "statut": "RAPPORTE"},
  {"reference": "The Ladder, Blum et Hardt, ICML 2015", "statut": "RAPPORTE"},
  {"reference": "HyperAgents, Zhang et al., 2026, arXiv 2603.19461 (boucle externe de sélection et d'évaluation gardée fixe)", "statut": "RAPPORTE"},
  {"reference": "Miconi, EuroGP 2009", "statut": "RAPPORTE"}
 ]
},
{
 "nom": "Approche : le prédicteur en quarantaine — date de coupure antérieure et annexes non lues comme épreuve scellée",
 "type": "approche",
 "enonce": "Pour toute question où la théorie est notée comme prévisionniste (Q3 sur grille, Q-pont à coût nul, méta-audit Q2, diagonale de l'auto-jeu), séparer trois rôles tenus par trois instances à information strictement croissante : (1) le prédicteur, instance neuve d'un modèle dont la date de coupure déclarée est antérieure à la publication du banc, ou qui n'a reçu qu'une passation sans chiffres rédigée par le tiers, et dont la prédiction est empreintée avant tout accès ; (2) l'apparieur tiers, qui fixe cellules, appariements et règles d'extraction ; (3) l'évaluateur, qui lit une fois les tableaux ou calcule les scores. Les annexes jamais extraites des fichiers PDF (Portable Document Format) deviennent une banque scellée gratuite : on prédit les chiffres qu'elles contiennent (tableaux par environnement, matrices de dégradation croisée des invites ciblées, résultats par modèle) avant de les ouvrir. C'est l'asymétrie de Terekhov et al. (l'attaquant à date de coupure postérieure sait tout du moniteur) renversée en garde : le prédicteur à date de coupure antérieure ne peut rien savoir du résultat.",
 "loi_predictive": {
  "espace_instances": "Campagnes de ≥ 20 quantités publiées non lues par campagne, réparties entre corps de papier (indexé, mémorisable) et annexes (peu indexées) ; deux prédicteurs par campagne : quarantainé et non quarantainé (date de coupure postérieure, accès au corpus).",
  "prediction": "Le protocole se teste lui-même : l'erreur absolue médiane du prédicteur non quarantainé est ≤ la moitié de celle du quarantainé sur les quantités du corps de papier (fuite par mémorisation mesurable), et les deux erreurs sont indiscernables sur les quantités d'annexes ; une campagne qui ne montre pas cet écart signale soit une annexe indexée, soit une fuite par la passation.",
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
  "texte": "Le rôle de tiers dans le noyau ; une garde d'empreinte temporelle sur toute prédiction ; un registre des dates de coupure des modèles employés ; une passation « sans chiffres » comme gabarit obligatoire pour le prédicteur."
 },
 "cout": {
  "nature": "processeur",
  "ordre_de_grandeur": "Appels de modèle modestes (deux prédicteurs par campagne) ; aucun calcul."
 },
 "piege": "Fuite par la passation : les extraits eux-mêmes citent des chiffres ; une consigne rédigée par quelqu'un qui a lu les pièces fuit sans le vouloir ; parade : passation rédigée par le tiers, relue par un modèle différent pour y chercher tout chiffre ou nom de résultat. Date de coupure non fiable (mises à jour du corpus). Et le témoin non quarantainé peut échouer aussi : alors la « fuite » n'est pas mesurable et la quarantaine ne protège de rien de démontrable.",
 "cosmetique_si": "Les deux prédicteurs obtiennent la même erreur sur le corps de papier ET sur les annexes (aucune fuite détectable, donc aucune protection mesurée), ou si une seule prédiction est scellée après la lecture de son résultat.",
 "anteriorite": [
  {"reference": "Adaptive Attacks on Trusted Monitors Subvert AI Control Protocols, Terekhov et al., 2025, arXiv 2510.09462 (asymétrie de date de coupure)", "statut": "RAPPORTE"},
  {"reference": "Generalization in Adaptive Data Analysis and Holdout Reuse, Dwork et al., NeurIPS 2015", "statut": "RAPPORTE"},
  {"reference": "The Ladder, Blum et Hardt, ICML 2015", "statut": "RAPPORTE"},
  {"reference": "MonitoringBench, 2605.09684 (demande d'exclusion des corpus d'entraînement) ; SLEIGHT-Bench, 2605.16626 (chaînes canari)", "statut": "RAPPORTE"},
  {"reference": "Registered reports, Nosek et Lakens, 2014 (Social Psychology)", "statut": "SUPPOSE"},
  {"reference": "Evaluating the replicability of social science experiments / marchés de prédiction, Camerer et al., 2018, Nature Human Behaviour", "statut": "SUPPOSE"},
  {"reference": "Série ASVspoof (familles inconnues tenues par l'organisateur), 2019, arXiv 1904.05441", "statut": "RAPPORTE"},
  {"reference": "Tavallaee et al., 2009, critique de KDD'99 / NSL-KDD (banc rejoué devient surajusté)", "statut": "RAPPORTE"}
 ]
}
]}
```