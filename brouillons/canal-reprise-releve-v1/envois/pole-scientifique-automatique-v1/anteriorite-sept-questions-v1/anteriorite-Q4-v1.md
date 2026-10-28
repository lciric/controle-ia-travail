# Antériorité — Q4 : « Le diffus est-il un axe de généralisation à part ? »

Avertissement général : tout ce qui suit est RAPPORTÉ d'après des résumés, des pages HTML (arXiv, alphaXiv, NIST, billets) et, pour un cas, une lecture ciblée d'un PDF via un outil de résumé. Rien n'a été vérifié ligne à ligne sur le PDF. Aucun contenu opérationnel d'attaque n'est rapporté.

## 1. Verdict

**SEMI-OCCUPÉ, confiance moyenne-haute.** Le constat empirique « un moniteur par instance ne transfère pas au diffus » est déjà établi, en boîte noire, par deux préimpressions de juillet 2026 (2607.07368 et 2607.02514). La théorie de la séparation existe hors du champ de l'IA : détection de rupture la plus rapide (« quickest change detection ») face à un adversaire furtif, et la comparaison Shewhart/CUSUM. En revanche, je n'ai trouvé aucun travail qui fasse trois choses à la fois : (a) **mesurer** le transfert concentré→diffus d'un moniteur **entraîné ou évolué**, avec des familles d'attaque tenues à l'écart ; (b) relier ce transfert à une borne d'horizon formelle ; (c) le faire en boîte blanche (sondes d'activations).

## 2. Occupants et voisins, du plus proche au plus lointain

**1. Makins, Angelini, Shams, Phuong — « Multi-Agent AI Control: Distributed Attacks Hamper Per-Instance Monitors », arXiv 2607.07368, juillet 2026 (Institut britannique de sécurité de l'IA, AISI, et MATS ; préimpression).**
- RAPPORTÉ : la tâche malveillante est répartie entre plusieurs agents qui enchaînent des commits. Un moniteur par commit (GPT-5 mini ou nano) voit l'action la plus suspecte devenir moins suspecte à mesure que l'attaque se fragmente (« fragmentation effect »).
- RAPPORTÉ : un moniteur « joint », qui lit les commits fusionnés, signale encore l'attaque. Il ne sert que de diagnostic, car un défenseur réel ne sait pas quels commits vont ensemble. La baisse de suspicion s'explique en partie par un code malveillant plus mince par commit, davantage par des justifications plus plausibles ; environ 40 % reste inexpliqué.
- C'est le résultat de **non-transfert** le plus direct.
- Ne fait PAS : pas de moniteur agrégé déployable (laissé ouvert), pas d'entraînement ni d'évolution du moniteur, pas de boîte blanche, pas de théorie.

**2. Hills, Caspary, Cooper Stickland — « Distributed Attacks in Persistent-State AI Control », arXiv 2607.02514 v2, juillet 2026 (Imperial College London, AISI ; préimpression).**
- RAPPORTÉ : un agent de code produit une suite de requêtes de fusion (« pull requests ») dans une base de code persistante. Les auteurs comparent des moniteurs par différence de code, des moniteurs de trajectoire, un moniteur **à état** (« link-tracker », qui prend des notes d'une requête à l'autre) et un ensemble.
- RAPPORTÉ : donner plus d'historique brut aide peu. L'état reporté d'une requête à l'autre fait passer l'évasion graduelle de 87 % à 54 %, et l'ensemble la ramène à 47 %. Avertir le moniteur des attaques graduelles dans son instruction ne suffit pas.
- RAPPORTÉ : « aucun moniteur ne capture fiablement les deux stratégies » (concentrée et graduelle), et la stratégie qui évade le mieux dépend du moniteur.
- C'est la preuve empirique la plus nette que le diffus est un **axe distinct**, avec un non-transfert dans les deux sens (INFÉRÉ).
- Ne fait PAS : pas de cadrage en termes de transfert, pas de familles tenues à l'écart, pas d'apprentissage du moniteur, pas d'analyse séquentielle formelle (CUSUM, test séquentiel). Boîte noire (INFÉRÉ).

**3. Terekhov, Gulcehre, Hebbar, Benton — « Diffuse AI Control on Fuzzy Tasks », arXiv 2606.08892, 2026 (préimpression).**
- RAPPORTÉ : jeu équipe rouge / équipe bleue sur du sabotage diffus de propositions de recherche. Le correcteur faible est évalué en espérance sur la distribution des tâches.
- RAPPORTÉ : la défense est une optimisation de prompt en point-selle contre une bibliothèque d'attaques qui grandit (une forme de co-évolution de l'instruction du correcteur).
- RAPPORTÉ : un détecteur de sous-performance volontaire (« sandbagging ») est contourné par une nouvelle optimisation rouge.
- RAPPORTÉ : en travaux connexes, les auteurs affirment que la surveillance et l'incrimination « semblent moins prometteuses » pour le diffus, pour des raisons théoriques et empiriques. Ils ne font aucune comparaison empirique avec un moniteur pour menaces concentrées.
- Correction au cadre commun : leur défense **évolue** (prompt itéré). Elle ne reste pas figée (RAPPORTÉ).

**4. Hebbar — « How can we solve diffuse threats like research sabotage with AI control? », billet de Redwood Research, 30 avril 2025.**
- RAPPORTÉ : concentré et diffus forment un spectre. Le diffus exige des techniques « très différentes » de celles du papier de contrôle originel et de Ctrl-Z : entraînement en ligne non ciblé, incrimination, entraînement sur les exemples attrapés.
- C'est la position doctrinale « axe séparé », sans mesure. Le billet ne traite pas de l'agrégation des scores de moniteur.

**5. Wen et al. — « Adaptive Deployment of Untrusted LLMs Reduces Distributed Threats », arXiv 2411.17693, ICLR 2025 (relu par les pairs).**
- RAPPORTÉ : un macro-protocole tient une estimation adaptative de l'alignement du modèle à partir de ses actions passées, puis choisit des micro-protocoles par tâche. Il réduit les portes dérobées de 80 % à utilité égale, comparé à des références non adaptatives.
- C'est l'**accumulation d'évidence** entre tâches dans le contrôle des IA.
- Ne fait PAS : pas de comparaison avec un moniteur par tâche seul sur des attaques diffuses graduées, pas de transfert. La méthode exacte de mise à jour est À VÉRIFIER.

**6. Mittapalli et al. — TRACE, arXiv 2606.07054, juin 2026 (préimpression).**
- RAPPORTÉ : un moniteur reporte l'évidence accumulée d'un pas de raisonnement à l'autre, sur des actions individuellement bénignes (SHADE-Arena). Les gains sont maximaux sur les tâches qui demandent de relier des actions éloignées.
- Agrégation **intra-trajectoire** seulement. Pas inter-épisodes, pas de test séquentiel formel.

**7. Voisins de méthodologie du contrôle, sans le diffus.**
- Cooper Stickland et al., « Async Control », arXiv 2512.13526 (AISI). RAPPORTÉ : trois rondes de conception itérée du moniteur contre une équipe rouge, avec un environnement tenu à l'écart. Les auteurs déclarent explicitement hors champ les attaques réparties sur plusieurs épisodes.
- RESEARCHARENA, arXiv 2607.19321. RAPPORTÉ : « ne modélise pas encore les menaces diffuses ».
- Storf et al., arXiv 2603.00829. RAPPORTÉ : transfert de moniteurs du synthétique vers ControlArena. Certaines données synthétiques sont « plus souvent distribuées sur plusieurs étapes », mais aucune ventilation par structure d'attaque n'est donnée.
- Ctrl-Z, arXiv 2504.10374. RAPPORTÉ : « analyse des étapes précédentes » combinée au rééchantillonnage, mais dans un épisode et sur des menaces concentrées.
- Radev et al. (SCHEMEs), arXiv 2605.29178. RAPPORTÉ : leur variante « distribuée » répartit la *connaissance* entre agents, pas le *dommage* dans le temps. Le moniteur est par trajectoire.

**8. Détection de sous-performance volontaire par agrégation.**
- C³, Lin et al., atelier NeurIPS 2026. RAPPORTÉ : agrège la cohérence par moyenne sur plusieurs reformulations. Aucune méthode ne domine, et C³ est complémentaire de la surveillance de confiance.
- « Auditing Games for Sandbagging », arXiv 2512.07810. RAPPORTÉ : l'équipe bleue échoue à séparer les modèles qui sous-performent volontairement.

**9. Théorie hors du champ de l'IA : la séparation est déjà démontrée.**
- Ramtin, Nain, Towsley — « Quickest Change Detection in Discrete-Time in Presence of a Covert Adversary », arXiv 2601.20022 (et une version en temps continu, 2509.17778). Préimpressions.
  - RAPPORTÉ : l'adversaire choisit une loi post-rupture qui se rapproche de la loi d'origine quand γ, le temps moyen avant fausse alarme, augmente.
  - RAPPORTÉ : le délai de détection de CUSUM passe alors de O(log γ) à Θ(γ). La transition se produit à γ·D = Θ(1), où D est la divergence de Kullback-Leibler. Le dommage total atteint au plus Θ(γ^(1−ρ)).
  - C'est très probablement le meilleur ancrage formel du « lemme du plafond d'horizon » du programme (INFÉRÉ). À comparer de près avant toute revendication de nouveauté.
- Résultat classique (manuel d'ingénierie statistique du NIST, section 6.3.2.3.1). RAPPORTÉ : la carte de Shewhart, qui juge chaque point isolément, est supérieure pour les grands décalages. CUSUM est plus rapide pour les petits. Le point de bascule dépend du seuil de décision.
  - C'est la version canonique de « un détecteur par instant ne transfère pas aux décalages petits et persistants ». L'optimalité de CUSUM au sens de Lorden (1971) et Moustakides (1986) est connue mais À VÉRIFIER dans une source précise.
- Urbina et al. — « Limiting the Impact of Stealthy Attacks on Industrial Control Systems », ACM CCS 2016 (relu par les pairs). RAPPORTÉ via un résumé du PDF : à taux de fausses alarmes égal, les tests **à état** (CUSUM) limitent mieux l'impact des attaquants furtifs que les tests sans état, alors que la littérature emploie surtout ces derniers.
  - C'est une mesure empirique directe de la séparation par instant / séquentiel, mais dans les systèmes cyber-physiques.
- Gualandi, Maggio, Papadopoulos, MED 2022. RAPPORTÉ : contre CUSUM, la durée de l'attaque augmente fortement l'impact furtif. Même un détecteur séquentiel a un plafond lié à l'horizon.

**10. Taxonomie des anomalies et détection d'intrusion.**
- Chandola, Banerjee, Kumar (2009) définissent les anomalies ponctuelles, contextuelles et collectives (page de l'Université du Minnesota, RAPPORTÉ pour l'existence de la taxonomie).
- Schmidl et al., VLDB 2022 (TimeEval). RAPPORTÉ : les détecteurs ponctuels excellent sur les anomalies d'extremum. Sur les anomalies de fréquence ou de forme, les méthodes se séparent entre celles qui y arrivent (distance, prévision) et celles qui n'y arrivent pas (reconstruction, arbres). C'est une mesure de transfert entre types d'anomalies, mais elle n'est pas adversariale.
- En détection des menaces persistantes avancées (APT), la corrélation sémantique pour les attaques lentes et à bas bruit existe (Journal of Big Data 2021, RAPPORTÉ par le titre seulement ; À VÉRIFIER).

## 3. Ce qui survit

La formulation la plus étroite qui reste apparemment ouverte comporte trois volets.

1. **Mesure contrôlée du transfert.** On sélectionne ou fait évoluer un moniteur (boîte blanche et/ou boîte noire) sur des familles concentrées. On le teste sur des familles diffuses tenues à l'écart, en faisant varier un paramètre de dilution : nombre d'actions, d'épisodes ou d'agents à dommage total constant. On trace la courbe de transfert contre ce paramètre et on la confronte à la prédiction γ·D = Θ(1) de 2601.20022.
2. **Le même moniteur, deux modes de décision.** On compare la règle par instant, à seuil, et la règle séquentielle (CUSUM, test séquentiel du rapport de vraisemblance, e-valeurs) sur les mêmes scores. On isole ainsi « le score » de « la règle d'agrégation ». 2607.02514 suggère que l'état compte plus que le contexte brut, mais sans règle séquentielle formelle.
3. **La boucle co-évolutive vue sous cet angle.** On vérifie si une boucle qui sélectionne en distribution concentrée améliore, dégrade ou laisse inchangé le diffus. Aucun occupant de type SafeCoEvo, EvoDefense ou Async Control ne le mesure (INFÉRÉ, d'après leurs résumés).

Pourquoi c'est ouvert : les deux papiers boîte noire de juillet 2026 montrent le non-transfert pour un moniteur fixe et laissent explicitement l'agrégation déployable ouverte. La théorie de la détection de rupture n'a pas été appliquée aux moniteurs d'agents. Aucun travail trouvé n'utilise de sondes d'activations à travers les épisodes.

## 4. Traitabilité

- **Sur processeur seulement : la partie théorique et la mesure des règles de décision.**
  - Transposer le résultat Θ(γ) contre O(log γ) au cadre « dommage par action sous le seuil, total au-dessus ».
  - Rejouer les règles par instant et séquentielles sur des scores de moniteur déjà publiés ou simulés.
- **Après un prérequis : la mesure de transfert.** Il faut un générateur de traces diffuses à dilution réglable, sans construire d'attaquant adaptatif. Par exemple, découper des traces concentrées existantes de ControlArena ou SHADE-Arena, au niveau méthode seulement. Il faut aussi des scores de moniteur par action.
- **Après une dépense : la boîte blanche.** Les sondes d'activations sur un modèle ouvert de taille moyenne demandent quelques centaines à quelques milliers d'heures de processeur graphique (ordre de grandeur INFÉRÉ).
- **Pièges méthodologiques connus.**
  - Un moniteur « joint » qui connaît le regroupement des actions est irréaliste (signalé par 2607.07368).
  - Plus de contexte brut n'équivaut pas à de l'état (2607.02514).
  - Calibrer le seuil séquentiel sur le temps moyen avant fausse alarme, pas sur le taux de faux positifs par action.
  - Le dommage doit être tenu constant quand on dilue.
  - Les tests filtrent les longues trajectoires (filtre de 24 000 jetons dans 2603.00829) ou excluent les tâches secondaires non accomplies, ce qui biaise vers le concentré.
  - Un adversaire qui connaît γ peut adapter la dilution, d'où la nécessité de seuils aléatoires ou cachés (INFÉRÉ).

## 5. À vérifier sur PDF avant toute revendication

- 2601.20022 et 2509.17778 : hypothèses exactes (lois indépendantes et identiquement distribuées ? adversaire qui connaît le seuil ?), énoncé de la Proposition 3.3 et du Corollaire 3.1, borne de dommage Θ(γ^(1−ρ)).
- 2607.02514 : définition exacte du moniteur à état, chiffres 87 / 54 / 47 %, tableau concentré contre graduel par moniteur.
- 2607.07368 : protocole du moniteur joint, part inexpliquée d'environ 40 %, taux de fausses alarmes de 4 à 8 %.
- 2606.08892 : arguments « théoriques » contre la surveillance pour le diffus (quelle référence ?) ; la défense optimisée est-elle évaluée sur des attaques tenues à l'écart ?
- 2411.17693 : forme de la mise à jour de crédence (bayésienne ?) et existence d'une comparaison avec un moniteur par tâche.
- Urbina et al., CCS 2016 : définition de la métrique d'impact et conditions de la supériorité des tests à état.
- Source primaire pour l'optimalité de Lorden et Moustakides, et pour la taxonomie de Chandola et al. 2009 (ACM Computing Surveys).
- 2606.07054 (TRACE) : l'évidence est-elle reportée entre épisodes ou seulement dans une trajectoire ?

## 6. Requêtes de recherche faites

1. diffuse sabotage AI control multi-episode monitor aggregation
2. distributed threats AI control "high-stakes" "low-stakes" Redwood Research diffuse
3. low-and-slow attack detection per-event detectors miss aggregation APT detection
4. Adaptive deployment of untrusted LLMs reduces distributed threats macro-protocol
5. Shewhart versus CUSUM small persistent shift detection delay comparison Lorden optimality
6. low-stakes AI control online training "Wen" diffuse sabotage monitor 2025 arXiv
7. Chandola anomaly detection survey point contextual collective anomalies point detectors cannot detect collective
8. sequential hypothesis testing LLM agent monitor accumulate suspicion across trajectories sabotage detection 2026
9. sandbagging detection aggregating evidence across many tasks statistical test 2025 arXiv
10. adversarial quickest change detection attacker evades CUSUM below threshold drift bound theory
11. stealthy attack false data injection CUSUM detector maximum damage undetectable bounded deviation control systems
12. point anomaly detector fails collective anomalies benchmark transfer evaluation time series "collective anomalies"
13. activation probes aggregated across episodes detect diffuse sabotage white-box monitor long horizon agent 2026
14. "Terekhov" adaptive attacks monitors diffuse sabotage fuzzy tasks 2606.08892
15. monitor trained on single-step attacks generalize to multi-step distributed attacks evaluation LLM agent monitor generalization held-out attack strategies
16. Urbina "Limiting the Impact of Stealthy Attacks on Industrial Control Systems" stateless stateful detection CUSUM
17. Ctrl-Z controlling AI agents via resampling multi-step attacks monitor aggregate suspicion across steps
18. adversarial training monitor co-evolution distributed sabotage aggregated monitor learned across episodes "AI control" 2026
