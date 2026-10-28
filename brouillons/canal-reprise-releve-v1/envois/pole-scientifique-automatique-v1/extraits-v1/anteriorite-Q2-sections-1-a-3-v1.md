<!-- Extrait scellé (CL31-14) de `anteriorite-sept-questions-v1/anteriorite-Q2-v1.md` : sections 1 à 3. conv-audit, 28 octobre 2026. Contenu copié tel quel, sans modification. -->

## 1. Verdict
**SEMI-OCCUPÉ. Confiance moyenne.**
- Les briques sont toutes occupées hors de la sécurité de l'IA, et certaines le sont même dans le contexte des modèles de langage. On a d'un côté la réutilisation adaptative d'un jeu de validation (Dwork et al., Blum et Hardt). On a de l'autre la promotion certifiée de mises à jour par e-processus et inégalité de Ville (2609.17560, 2609.32267, préimpressions de 2026).
- Aucun occupant de la co-évolution attaque/défense ne combine les deux : un juge figé, une borne démontrée et valable à tout instant sur le taux de fausses promotions, et des témoins plantés. Ce constat porte sur SafeCoEvo, AgentSafeEvo, MAGIC, EvoDefense et Auto Mode.
- La nouveauté porterait donc sur l'**assemblage**, appliqué à une boucle de sélection de moniteurs, et sur la **mesure comparative** entre juge figé garanti, juge-modèle co-évoluant et validation en distribution. Elle ne porterait pas sur l'outil statistique.

## 2. Occupants et voisins (du plus proche au plus lointain)

**A. Promotion certifiée et garantie valable à tout instant (les plus proches sur l'outil)**
- **« Pay Only for Disagreement : Certified No-Regression Verdicts for Model Updates »**, arXiv 2609.17560, préimpression 2026. RAPPORTÉ.
  - Ce qu'il fait : il certifie la promotion d'un modèle candidat face au modèle en place par des suites de confiance « anytime-valid » fondées sur le pari et les surmartingales. Selon la page, la validité tient « même avec un juge adversarial ».
  - Point le plus proche de notre question : la Proposition 13 annonce que la garantie se compose sur une suite non bornée de promotions à partir d'un seul budget d'erreur.
  - Ce qu'il NE fait PAS : sa théorie exclut les pertes jugées (juge-modèle, préférences). Il ne traite ni la co-évolution, ni des moniteurs de sécurité, ni des témoins plantés.
  - C'est l'antériorité la plus dangereuse pour la revendication « borne sur les fausses promotions ».
- **« When Can Old Evaluations Certify a New Model? … under Evaluator Drift »**, arXiv 2609.32267, préimpression 2026. RAPPORTÉ.
  - Ce qu'il fait : il certifie une mise à jour par e-processus et Ville quand l'évaluateur bon marché (souvent un juge-modèle) peut dériver. L'historique ne sert qu'à orienter les paris ; il ne touche ni l'hypothèse nulle ni le seuil.
  - Résultat rapporté : changer seulement la grille d'un juge-modèle figé déplace ses scores au-delà de la variance entre exécutions.
  - Ce qu'il NE fait PAS : il ne traite pas la sélection adaptative parmi les candidats d'une boucle évolutive (la page le dit peu clairement), ni l'adversité.
- **CELEUS**, arXiv 2606.20820, préimpression 2026. RAPPORTÉ.
  - Ce qu'il fait : il évalue un seul modèle de langage par e-processus, avec des intervalles valables à tout instant.
  - Ce qu'il NE fait PAS : la sélection parmi plusieurs candidats n'est pas traitée, et la nature de l'évaluateur n'est pas précisée.

**B. Analyse de données adaptative et sélection statistiquement valide (fondations, relues par les pairs)**
- **Dwork, Feldman, Hardt, Pitassi, Reingold, Roth**, « Generalization in Adaptive Data Analysis and Holdout Reuse », NeurIPS 2015, arXiv 1506.02629. RAPPORTÉ.
  - Apport : un jeu tenu à l'écart réutilisable (« reusable holdout ») contre le sur-ajustement adaptatif.
- **Blum et Hardt**, « The Ladder », ICML 2015, arXiv 1502.04585. RAPPORTÉ.
  - Apport : un classement fiable sous soumissions adaptatives.
  - Lien avec notre question : c'est déjà un « juge figé » qui ne divulgue qu'un signal quantifié pour borner l'effet Goodhart.
- **Learn-then-Test** (Angelopoulos, Bates et al., arXiv 2110.01052) et son adaptation **Adaptive LTT** (2409.15844). RAPPORTÉ.
  - Apport : choix d'hyperparamètres par tests multiples, avec contrôle du risque.
- **Wang et Ramdas**, contrôle du taux de fausses découvertes (FDR) par e-valeurs, JRSS-B 2022. RAPPORTÉ.
- **Tests fermés en ligne par e-valeurs**, arXiv 2407.15733. RAPPORTÉ.
- **Jamieson et Jain**, bandits avec contrôle du taux de fausses découvertes, NeurIPS 2018. RAPPORTÉ.
- **Algorithmes Seldoniens / amélioration de politique à haute confiance** (Thomas et al.) et leur extension à l'apprentissage par renforcement à partir de retours humains sous contrainte de sûreté (2506.08266). RAPPORTÉ.
  - Leur schéma « candidat sur une partition, test de sûreté sur une partition intouchée » est structurellement le juge figé.
- **Lacune commune (INFÉRÉ)** : aucun de ces travaux n'est appliqué à une boucle co-évolutive de moniteurs de sécurité.

**C. Goodhart sous sélection contre un juge fixe ou co-adapté**
- **« Optimizing the Score, Losing Sight of the Task »**, arXiv 2609.25848, préimpression 2026. RAPPORTÉ.
  - Ce qu'il fait : il distingue l'adaptation contre un évaluateur fixe de la co-adaptation évaluateur–politique. Il nomme la « concentration induite par la sélection ». Il recommande un jeu final intouché et des canaris (items volontairement invalides), un canari réussi devant déclencher une alarme.
  - Ce qu'il NE fait PAS : aucune correction statistique, aucune expérience juge figé contre juge appris. C'est une synthèse avec une illustration jouet.
  - Il occupe largement le cadrage conceptuel de Q2 et l'idée des témoins plantés.
- **« More Convincing, Not More Correct »**, arXiv 2607.05904, préimpression 2026. RAPPORTÉ.
  - Résultat : une auto-optimisation contre un juge sans référence fait monter le taux d'acceptation du juge sans améliorer l'exactitude. Les erreurs se transfèrent entre familles de juges, et un ensemble de trois juges ne suffit pas.
  - Dispositif : un « ancre cachée » sert d'audit, ce qui est l'analogue d'un témoin planté.
- **Détection de « proxy gaming » par tests de stress de l'évaluateur**, arXiv 2507.05619. RAPPORTÉ par son seul titre, À VÉRIFIER.

**D. Occupants de la co-évolution en sécurité de l'IA, sur le point précis du juge**
- **SafeCoEvo**, arXiv 2609.36580v2, préimpression. RAPPORTÉ.
  - Ce qu'il fait : l'évaluateur officiel est explicitement fixe (« Never change … official outcome, evaluator, dataset »). Les points de contrôle de la garde sont choisis sur une validation de 200 épisodes qui partage six scénarios avec le flux d'entraînement. Le test porte sur quatre scénarios inédits.
  - Ce qu'il NE fait PAS : aucune garantie statistique, aucun intervalle, aucune discussion de Goodhart. La sélection de la meilleure époque se fait sur la même validation qui est rapportée.
  - Conclusion : il a un juge figé, mais un juge **non garanti**.
- **AgentSafeEvo**, arXiv 2610.19422, préimpression. RAPPORTÉ.
  - Ce qu'il fait : un juge-modèle (« Qwen3.8-27B », nom tel quel) attribue à la fois la récompense de sûreté et celle d'utilité. Attaquant et défenseur co-évoluent par GRPO (optimisation de politique relative par groupe). Résultats : moyenne et écart-type sur trois exécutions.
  - Ce qu'il NE fait PAS : aucune analyse du piratage du juge, aucune garantie.
- **MAGIC**, arXiv 2602.01539, préimpression. RAPPORTÉ.
  - Ce qu'il fait : Qwen3Guard est à la fois modèle de récompense **et** juge d'évaluation finale. Ce juge est fixe d'après l'algorithme (INFÉRÉ). La garantie annoncée est théorique (équilibre de jeu idéalisé) et non statistique.
  - Ce qu'il NE fait PAS : il ne discute pas le piratage du juge.
  - Point important : la circularité entraînement/évaluation sur le même juge est exactement le scénario que Q2 veut mesurer.
- **EvoDefense**, arXiv 2605.31140, préimpression. RAPPORTÉ.
  - Ce qu'il fait : un « Scorer » fixe (Deepseek-V3.1) avec un seuil d'arrêt.
  - Ce qu'il NE fait PAS : aucune garantie, aucune variance. Une partie des attaques rapportées pour EvoDefense+ n'est pas tenue à l'écart.
- **Anthropic Auto Mode**. RAPPORTÉ via un billet secondaire (digitalapplied.com), non vérifié sur la source primaire.
  - Ce qu'il fait : il est évalué sur trois jeux, dont 52 actions réelles « trop zélées ». Le taux de faux négatifs de 17 % repose sur « environ neuf échecs », de l'aveu même de la source.
  - Ce qu'il NE fait PAS : rien n'indique un jeu figé, une garantie, ou une co-évolution formelle. Le jeu annoncé est appelé à grossir.

## 3. Ce qui survit
**Formulation étroite apparemment ouverte (INFÉRÉ).**

Dans une boucle de sélection itérée de moniteurs de sécurité (boîte blanche ou noire), contre des familles d'attaque tenues à l'écart, on cherche un juge non apprenant qui :
- contrôle, par e-processus composé sur toute la boucle (budget d'erreur unique, inégalité de Ville), le taux de fausses promotions ;
- est audité en continu par des témoins plantés : contrôles négatifs, et nulles de bibliothèque connues comme non-améliorations.

Il faut en plus une **mesure empirique** de l'écart entre trois régimes sur la même boucle :
- juge figé garanti ;
- juge-modèle co-évoluant ou partagé entre récompense et évaluation (cas de MAGIC et d'AgentSafeEvo) ;
- validation en distribution (cas de SafeCoEvo).

**Pourquoi c'est ouvert.**
- 2609.17560 compose déjà les promotions, mais il exclut les pertes jugées et n'a pas d'adversaire.
- 2609.25848 pose le cadre conceptuel, mais sans garantie ni expérience.
- Les occupants de la co-évolution n'ont pas de garantie.

**Ce qui ne survit pas.**
- « Utiliser des e-valeurs pour certifier une promotion » : occupé.
- « Un évaluateur fixe empêche Goodhart » : occupé, et il est connu que c'est faux sans précaution. Le jeu de validation se sur-ajuste quand même : c'est le résultat de Dwork et al. et de Blum et Hardt.
