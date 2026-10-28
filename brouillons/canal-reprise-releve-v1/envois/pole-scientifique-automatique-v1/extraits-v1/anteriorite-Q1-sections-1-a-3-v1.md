<!-- Extrait scellé (CL31-14) de `anteriorite-sept-questions-v1/anteriorite-Q1-v1.md` : sections 1 à 3. conv-audit, 28 octobre 2026. Contenu copié tel quel, sans modification. -->

## 1. Verdict

**SEMI-OCCUPÉ, avec une confiance moyenne à faible.**

- Les deux branches de la comparaison existent séparément :
  - des défenses entraînées sans attaquant, sur des conditions dérivées d'une spécification ou d'une classe d'hypothèses ;
  - des défenses co-évoluées contre un attaquant empirique, avec évaluation sur des attaques tenues à l'écart.
- En apprentissage automatique classique, l'idée « pire cas sur une classe d'hypothèses plutôt qu'une attaque précise, pour généraliser à l'imprévu » est déjà occupée (Laidlaw et al. ; Casper et al.).
- Je n'ai trouvé AUCUNE comparaison contrôlée, à budget égal, entre l'origine des conditions (dérivées des hypothèses statistiques d'un moniteur ou produites par un attaquant qui tourne). Le critère serait la généralisation à des familles d'attaque tenues à l'écart, pour des moniteurs d'agents.
- La confiance est limitée surtout parce que SafeCoEvo n'a pas été relu.

## 2. Occupants et voisins, du plus proche au plus lointain

**a. « Constitutional Black-Box Monitoring for Scheming in LLM Agents »**
- Identifiant et statut : arXiv 2603.00829, projet du programme MATS (Machine Learning Alignment & Theory Scholars), 2026. Préimpression. RAPPORTÉ.
- Ce qu'il fait :
  - Des moniteurs boîte noire sont optimisés uniquement sur des trajectoires synthétiques générées à partir de spécifications de comportement en langue naturelle. Il y a deux pipelines, STRIDE et Gloom.
  - Ils sont évalués sur 7 500 trajectoires tenues à l'écart (ControlArena) et « peuvent généraliser » à des environnements plus réalistes.
  - Le rendement sature vite, et pousser l'optimisation conduit à du surajustement.
- Ce qu'il ne fait pas :
  - Aucune boucle adverse.
  - Aucune comparaison avec des moniteurs entraînés sur des attaques produites par un attaquant (INFÉRÉ d'après le résumé).
  - La spécification décrit le comportement à détecter, pas les hypothèses du moniteur.
- C'est le voisin le plus proche de la branche « sans attaquant ».

**b. Constitutional Classifiers (Anthropic, billet et préimpression, 2025 ; deuxième génération ensuite)**
- Statut : billet et préimpression. RAPPORTÉ.
- Ce qu'il fait :
  - Les classifieurs sont entraînés sur des données synthétiques dérivées d'une « constitution », sans données d'attaque dans l'entraînement selon le billet.
  - La red-team humaine sert seulement d'évaluation : plus de 3 000 heures, 183 participants, aucune évasion universelle trouvée.
- Ce qu'il ne fait pas :
  - Aucune comparaison avec un classifieur entraîné contre un attaquant.
  - Aucune mesure explicite sur des familles d'attaque absentes du processus.
  - Ce n'est pas un moniteur d'agent.

**c. Casper et al., « Defending Against Unforeseen Failure Modes with Latent Adversarial Training »**
- Identifiant et statut : arXiv 2403.05030, TMLR (Transactions on Machine Learning Research) 2025. Relu par les pairs. RAPPORTÉ.
- Ce qu'il fait :
  - Il défend « sans connaître les vulnérabilités ni utiliser d'entrées qui les déclenchent ».
  - Il compare l'entraînement adversarial latent à l'entraînement adversarial classique (perturbations d'entrée) et à des perturbations latentes aléatoires.
  - L'évaluation porte sur des classes d'attaque tenues à l'écart, dont 18 attaques d'image d'après Kaufmann et al. (= Kang et al. 2019).
- C'est l'analogue méthodologique le plus proche de « condition sans distribution contre attaquant ».
- Ce qu'il ne fait pas : les perturbations ne sont pas dérivées des hypothèses d'un moniteur, et il n'y a pas d'attaquant co-évolué (auto-jeu).

**d. Laidlaw, Singla, Feizi, « Perceptual Adversarial Robustness: Defense Against Unseen Threat Models »**
- Identifiant et statut : arXiv 2006.12655, ICLR (International Conference on Learning Representations) 2021. Relu par les pairs. RAPPORTÉ pour le titre et le lieu.
- Ce qu'il fait : il entraîne contre le pire cas sur une classe définie analytiquement (une boule de distance perceptuelle) et l'évalue sur des modèles de menace non vus. Le détail de la comparaison est À VÉRIFIER.
- Ce qu'il ne fait pas : la recherche du pire cas reste un optimiseur interne, et non une condition prédite sans recherche.
- Voisins de même nature :
  - Stutz et al., CCAT (Confidence-Calibrated Adversarial Training), ICML (International Conference on Machine Learning) 2020, arXiv 1910.06259 : généralisation à des attaques non vues. RAPPORTÉ pour le titre.
  - Tramèr et Boneh 2019 sur les perturbations multiples. De mémoire, À VÉRIFIER.

**e. Co-évolution attaquant-défenseur pour la sûreté des grands modèles de langage**
- EvoSafety (arXiv 2605.13411, préimpression, RAPPORTÉ) :
  - Les entrées adverses du défenseur viennent de l'attaquant co-évolué, et non d'une dérivation analytique.
  - Une bibliothèque de « compétences » d'attaque est tenue à l'écart, et la défense est évaluée sur des méthodes non vues.
  - Le surajustement observé porte sur les artefacts du juge, pas sur la distribution de l'attaquant.
- GPT-Red (arXiv 2607.26115, préimpression, RAPPORTÉ) :
  - Il affirme que l'auto-jeu « généralise mieux que des jeux de données statiques ».
  - Cette affirmation ne s'appuie sur aucune comparaison contrôlée, et l'article ne compare à aucune source spécifiée ou analytique.
- Self-RedTeam (arXiv 2506.07468, RAPPORTÉ) : il donne une garantie conditionnelle à l'équilibre de Nash, mais aucun test contre une source non adverse.
- SafeEvolve (arXiv 2609.02786, RAPPORTÉ) : les conditions viennent de l'expérience de l'agent, sans comparaison d'origine.
- MonitoringBench (2605.09684, RAPPORTÉ) :
  - Les attaques sont optimisées contre trois moniteurs de développement, puis testées sur dix moniteurs tenus à l'écart.
  - La mise à l'écart porte donc sur les moniteurs, pas sur les familles d'attaque.
  - Aucun moniteur n'est entraîné.
- SafeCoEvo (2609.36580) : d'après le cadre commun, il pratique une sélection en distribution. Résumé non lu. À VÉRIFIER.

**f. Détection d'intrusion**
- Sekar et al., CCS (Conference on Computer and Communications Security) 2002, détection d'anomalies fondée sur une spécification. Relu par les pairs. RAPPORTÉ.
  - Le détecteur est dérivé d'une spécification de protocole (machine à états) et non d'attaques collectées.
  - Il détecte les 43 attaques de son périmètre (données Lincoln Lab 1999) avec environ 5,5 fausses alarmes par jour.
  - L'article oppose explicitement cette approche aux signatures, aveugles à l'inédit.
  - C'est une antériorité ancienne et solide de l'intuition « dérivé d'un modèle plutôt qu'appris sur des attaques ». Elle n'a pas de témoin contrôlé moderne.
- Sommer et Paxson, « Outside the Closed World », IEEE S&P (Symposium on Security and Privacy) 2010. RAPPORTÉ pour l'existence. C'est la critique classique des détecteurs appris face à l'inédit.
- Kayacik et al. 2011 : un attaquant évolutionnaire sert à tester des détecteurs. RAPPORTÉ pour le titre.

**g. Prédire les défaillances sans adversaire**
- « Anticipating the Optimism Gap » (arXiv 2606.22054, préimpression, RAPPORTÉ) :
  - Il prédit la chute d'AUC (aire sous la courbe ROC) d'un détecteur sous déplacement de distribution, à partir de ses seules statistiques en distribution.
  - Il sert uniquement à l'évaluation, pas à l'entraînement.
  - Le déplacement est paramétré de l'extérieur et n'est pas dérivé des hypothèses du détecteur.

**h. Critiques de l'auto-jeu et des attaques adaptatives**
- Tramèr et al., NeurIPS (Conference on Neural Information Processing Systems) 2020, « On Adaptive Attacks to Adversarial Example Defenses » : connu, non relu ici, À VÉRIFIER.
- Rice et al., ICML 2020, arXiv 2002.11569 : surajustement robuste au fil des époques. Ce n'est pas un surajustement à l'attaquant. RAPPORTÉ pour le titre.
- Czempin et Gleave, arXiv 2208.05083 : l'entraînement par population réduit l'exploitabilité face à des adversaires tenus à l'écart. RAPPORTÉ pour le titre. C'est la version théorie des jeux de « l'adversaire unique surajuste ».

## 3. Ce qui survit

La formulation la plus étroite qui reste apparemment ouverte (INFÉRÉ) :

> À budget de calcul et de données égal, pour un moniteur d'agent (boîte blanche ou noire) contre des menaces diffuses, on compare deux origines des conditions d'entraînement :
> - (A) des conditions dérivées des hypothèses statistiques du moniteur (indépendance entre étapes, stationnarité, seuil par instant, etc.), sans aucun attaquant ;
> - (B) un attaquant automatique co-évolué.
>
> La question est de savoir laquelle généralise mieux, sous protocole « une famille laissée de côté », à des familles d'attaque tenues à l'écart, avec un juge figé.

Pourquoi cette formulation survit :

- Les travaux sans attaquant (a, b, f) partent d'une spécification du comportement à détecter, pas des hypothèses du détecteur. Aucun d'eux ne fait la comparaison.
- Les travaux co-évolutifs (e) ne testent aucune source non adverse.
- L'analogue en apprentissage automatique classique (c, d) occupe le principe. Les auteurs devront donc le revendiquer comme transfert, non comme idée neuve.
