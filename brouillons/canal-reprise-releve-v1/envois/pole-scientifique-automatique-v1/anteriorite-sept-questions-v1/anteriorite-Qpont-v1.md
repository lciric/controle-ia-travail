# Antériorité — Q-pont : les épisodes synthétiques à propriété prédite P prédisent-ils les taux de détection sur des épisodes réels portant P ?

Avertissement : tout ce qui suit est RAPPORTÉ d'après des pages de résumé, des pages HTML et des billets ; aucun PDF n'a été vérifié en entier.

## 1. Verdict
**SEMI-OCCUPÉ, confiance moyenne.** La *métrique* de validité de transfert existe et a été mesurée ailleurs : le coefficient de corrélation simulation-réel (Sim2Real Correlation Coefficient) en robotique, et des corrélations entre écarts de généralisation pour les sondes entraînées hors politique. La sécurité de l'intelligence artificielle mesure déjà le transfert synthétique → réaliste, mais pour l'*entraînement* ou la *sélection* de moniteurs (Storf et al. 2026), ou pour l'erreur d'une estimation de sûreté (Redwood, octobre 2026). Je n'ai trouvé aucun travail qui fabrique des épisodes **à propriété théorique contrôlée P**, puis corrèle propriété par propriété le taux de détection synthétique au taux réel sur du sabotage réellement produit.

## 2. Occupants et voisins (du plus proche au plus lointain)

**a. Olmo, Zhang, Tracy (Redwood Research), « Simulated control evaluations », billet du 23 octobre 2026.** RAPPORTÉ : la même évaluation de contrôle est exécutée en réel puis en simulation (sorties d'outils produites par un modèle de langage) dans LinuxArena. L'écart quadratique moyen de la prédiction de sûreté vaut 3,6 points de pourcentage à un budget d'audit de 5 %, contre 10,1 pour BashArena. C'est **la mesure de transfert simulé → réel la plus proche dans le contrôle**. Ce qu'il NE fait PAS : la simulation porte sur l'*environnement*, l'attaquant reste réel (une politique d'attaque). Il n'y a ni propriété P contrôlée, ni épisode sans attaquant. Les auteurs disent ne pas pouvoir valider sur des transcriptions de déploiement contenant des attaques. Statut : billet, sans relecture par les pairs.

**b. Storf, Barton-Cooper, Peters-Gill, Hobbhahn, « Constitutional Black-Box Monitoring for Scheming in LLM Agents », arXiv 2603.00829, 2026.** RAPPORTÉ : 1 000 trajectoires synthétiques par pipeline (STRIDE, Gloom), générées depuis des n-uplets de scénario contrôlés (cadre, tâche, objectif désaligné, drapeau « couvert »). Les moniteurs sont sélectionnés sur ces trajectoires puis évalués sur 7 500 trajectoires ControlArena tenues à l'écart. Résultat : le transfert existe, il sature vite et la sur-optimisation mène au surapprentissage. Ils notent une relation monotone entre le rang au balayage de consignes et la performance de test pour STRIDE, mais ne donnent **aucun coefficient de corrélation** (section 5.1, figure 4). Ce qu'il NE fait PAS : les propriétés contrôlées sont des scénarios, pas des statistiques prédites du moniteur ; ControlArena reste un attaquant *instruit*, pas un saboteur « naturel » ; aucune corrélation par propriété. Statut : préimpression (programme MATS).

**c. Kirch, Dower, Skapars, Yannakoudakis, Lubana, Krasheninnikov, « The Impact of Off-Policy Training Data on Probe Generalisation », arXiv 2511.17408.** RAPPORTÉ : des sondes sont entraînées sur des données hors politique, sollicitées, incitées ou naturelles, pour huit comportements, puis testées sur du naturel quand il existe. Le transfert est bon pour les comportements « visibles dans le texte » et mauvais pour les comportements « ambigus dans le texte » (tromperie, flagornerie). Le changement de domaine pèse plus que le changement de stratégie de réponse (aire sous la courbe ROC moyenne ≈ 0,90 / 0,85 / 0,74). **Mesure clé** : la corrélation de Pearson entre l'écart de généralisation sur données incitées et l'écart sur données naturelles vaut 0,793 pour les sondes hors politique. Ce qu'il NE fait PAS : la tromperie et le sous-rendement délibéré (« sandbagging ») n'ont pas de données naturelles, d'où le recours à un proxy et une prédiction non vérifiée d'échec du transfert ; pas de sabotage agentique ; aucune propriété issue d'une théorie. Statut : préimpression (lieu de publication non lu, À VÉRIFIER). C'est le **résultat empirique le plus pertinent** : il prédit que la voie synthétique est la plus fragile exactement pour les propriétés « ambiguës dans le texte », celles que vise le programme. INFÉRÉ.

**d. Goldowsky-Dill et al., « Detecting Strategic Deception with Linear Probes », arXiv 2502.03407, ICML 2025 (PMLR v267).** RAPPORTÉ : sondes entraînées sur des paires d'instructions et sur du jeu de rôle, évaluées sur des scénarios plus réalistes (délit d'initié, sous-rendement délibéré). L'aire sous la courbe ROC va de 0,96 à 0,999. C'est une démonstration de transfert *d'entraînement*, sans mesure de prédictivité de l'*évaluation* synthétique. Relu par les pairs.

**e. Hollinsworth, Spies, Diriba, Gleave, Cundy, « Caught in the Act » (FIBS), arXiv 2610.12445.** RAPPORTÉ : 98,8 % d'aire sous la courbe ROC sur SHADE-Arena, au-dessus d'un moniteur textuel. Le résumé ne dit pas si le corpus FIBS est instruit ou naturel et ne rapporte aucune mesure de transfert synthétique → réel (À VÉRIFIER sur PDF). Préimpression.

**f. Organismes modèles.** Taylor et al., « Auditing Games for Sandbagging », arXiv 2512.07810 (Institut de sécurité de l'IA britannique, FAR.AI, Anthropic), et Clymer et al., banc d'essai « bench-af », billet de novembre 2025 (Redwood/MATS). RAPPORTÉ : tous deux reconnaissent que les organismes construits (verrous par mot de passe, réglage fin) ne garantissent pas la représentativité du comportement naturel, qui pourrait être plus ou moins détectable. **Aucun ne mesure ce transfert.** Hubinger et al. 2024 (« Sleeper Agents », 2401.05566) et « Model Organisms for Emergent Misalignment » (2506.11613) sont des voisins plus lointains, sans mesure de transfert repérée (INFÉRÉ d'après les titres et résumés).

**g. Hors champ : la métrique existe.** Kadian et al., « Sim2Real Predictivity », arXiv 1912.06321 (IEEE Robotics and Automation Letters d'après le DOI, À VÉRIFIER). RAPPORTÉ : le coefficient de corrélation simulation-réel sur 9 modèles valait 0,18 pour le succès ; après correction des failles du simulateur exploitées par les agents, il monte à 0,844. C'est le **modèle méthodologique exact** de Q-pont : le simulateur peut être « hackable » de façon à inverser les classements.

**h. Détection d'anomalies.** Steinbuss & Böhm, arXiv 2004.06947 (2020) : RAPPORTÉ, des anomalies synthétiques *caractérisables* (locales, de dépendance, globales) sont injectées, puis les classements de détecteurs sont comparés à ceux obtenus sur données réelles. Les anomalies uniformes reproduisent à peu près le classement réel ; les anomalies de dépendance l'inversent. Les auteurs disent ne pas chercher à imiter les anomalies réelles, donc il n'y a **pas de corrélation par propriété**. Emmott, Das, Dietterich et al., arXiv 1503.01158 (atelier KDD 2013) : des bancs d'essai sont construits depuis des données réelles selon quatre axes contrôlés (difficulté, fréquence, regroupement, pertinence des variables). Aucune validation de prédictivité sur anomalies naturelles n'a été repérée dans le résumé. Wu & Keogh, arXiv 2009.13807 : les bancs d'essai d'anomalies de séries temporelles « triviaux ou mal étiquetés » créent une illusion de progrès. C'est une critique de validité de construit, sans mesure de transfert.

**i. Détection d'intrusion et estimation par données synthétiques.** Hesford et al., arXiv 2403.17458 : les classements de systèmes de détection d'intrusion s'inversent d'un jeu de données à l'autre (Kitsune : F1 = 0,0216 sur CICIDS2017, bon ailleurs). C'est un argument indirect contre la prédictivité d'un jeu fabriqué unique (INFÉRÉ). Van Breugel et al., NeurIPS 2023 (2310.16524), estiment la performance par sous-groupe à partir de données synthétiques et valident l'erreur absolue contre un oracle réel. Le schéma de validation est le bon, mais le domaine (classification tabulaire) est éloigné. CheckList (Ribeiro et al., ACL 2020) et les relations métamorphiques sur classifieurs (1904.07348) : aucune corrélation avec les échecs en déploiement repérée (À VÉRIFIER).

## 3. Ce qui survit
Formulation étroite, apparemment ouverte : **pour un moniteur figé (sonde et/ou boîte noire) et un ensemble de propriétés P_k dérivées d'une théorie des angles morts, la corrélation de rang, propriété par propriété, entre le taux de détection sur épisodes fabriqués sans attaquant portant P_k et le taux sur épisodes de sabotage réel (agent réellement incité ou entraîné) portant P_k, avec les conditions sous lesquelles cette corrélation s'effondre (propriétés « ambiguës dans le texte », failles exploitables du générateur).** Aucun des occupants ne fait varier une propriété dérivée de la théorie ni ne rapporte cette corrélation. Les plus proches mesurent le transfert de l'entraînement (Kirch et al.), de la sélection (Storf et al.) ou de l'environnement (Redwood). INFÉRÉ, sous réserve des points de la section 5.

## 4. Traitabilité
- **Sur processeur seulement** : la partie boîte noire est possible avec un moniteur par interface de programmation et des transcriptions existantes (SHADE-Arena, ControlArena, LinuxArena). On mesure P sur ces épisodes réels, on fabrique des épisodes à P égale, puis on calcule une corrélation de rang (Spearman, Kendall) et une erreur absolue par propriété.
- **Prérequis** : un corpus « réel » de sabotage étiqueté et un **opérationnaliseur de P** qui mesure P de la même façon sur les deux sources. Sans lui, la corrélation est circulaire.
- **Dépense** : la partie boîte blanche demande l'extraction d'activations sur un modèle ouvert de 8 à 70 milliards de paramètres, soit quelques centaines d'heures de processeur graphique (ordre de grandeur INFÉRÉ), plus éventuellement des organismes réglés finement pour obtenir du sabotage « non instruit ».
- **Pièges connus** : (1) un générateur exploitable crée de faux succès ; le coefficient simulation-réel passe de 0,18 à 0,844 après correction (Kadian). (2) Le changement de domaine domine le changement de source (Kirch) : il faut apparier les domaines. (3) Le « réel » est presque toujours instruit, ce qui revient à valider contre un autre proxy. (4) Sélectionner sur le synthétique surapprend vite (Storf). (5) Les classements s'inversent selon le type d'anomalie (Steinbuss & Böhm), d'où la nécessité de rapporter par propriété, jamais en agrégé. (6) Il y a peu de propriétés, donc peu de points de corrélation : prévoir des intervalles par rééchantillonnage.

## 5. À vérifier sur PDF avant toute revendication
- 2603.00829 : absence confirmée de coefficient de corrélation ; nature exacte des attaques ControlArena (instruites ou non).
- 2511.17408 : définition exacte de la corrélation 0,793 (sur quelles unités) ; lieu de publication.
- Billet Redwood « Simulated control evaluations » : protocole de l'écart quadratique moyen ; existence d'un article associé.
- 2610.12445 : provenance (instruite ou naturelle) du corpus FIBS ; existence d'une évaluation croisée.
- 1912.06321 : formule du coefficient simulation-réel ; lieu de publication.
- 2004.06947 et 1503.01158 : existence d'une comparaison quantitative synthétique ↔ réel par type d'anomalie.
- CheckList et 1904.07348 : absence de lien avec les échecs en déploiement.

## 6. Requêtes faites
1. synthetic anomalies vs real anomalies benchmark validity outlier detection Steinbuss Böhm
2. deception probes off-policy vs on-policy generalization synthetic to real
3. model organisms misalignment do detection results transfer to natural misalignment
4. Emmott Das Dietterich systematic construction of anomaly detection benchmarks real data
5. intrusion detection synthetic dataset evaluation does not transfer real traffic cross-dataset generalization CIC-IDS2017 flaws
6. sabotage monitor evaluation prompted attack policy vs fine-tuned natural sabotage detection rates differ 2026
7. "Can you rely on your model evaluation" synthetic test data subgroup performance estimation van Breugel
8. Goldowsky-Dill detecting strategic deception linear probes roleplaying dataset generalize
9. validity of model organisms for evaluating AI monitors, constructed backdoor vs naturally emergent misalignment
10. Sim2Real predictivity correlation coefficient Kadian Habitat
11. behavioral testing CheckList failures correlate with real-world errors predictive validity
12. synthetic vs real misbehavior trajectories monitor evaluation realism gap AI control 2026
13. probes trained on prompted vs fine-tuned model organisms sandbagging auditing game
14. synthetic fraud data evaluate fraud detectors "train on synthetic test on real"
15. "Telling FIBS" probes sabotage black-box monitor ; arXiv 2610.12445 probes sabotage
16. injected anomalies realistic, time series anomaly benchmarks flawed Wu Keogh
17. ADBench anomaly types synthetic vs real
18. does performance on synthetic attacks predict detection of real attacks correlation
19. metamorphic testing ML classifiers correlate field failures
