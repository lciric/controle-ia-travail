# Proposition B — Tour III.1 : où placer l'ensemble hors-genre

## 0. État des pièces

- **Notes absentes.** Le bloc FAITS ne contient que la question, et son titre précise « notes retirées ». Je n'invente pas le contenu de ces notes.
- **Aucun statut fourni.** Aucun élément des FAITS ne porte de statut. Convention de B : ce que l'énoncé affirme explicitement sur l'équipe est traité comme **RAPPORTÉ** (affirmé par le scénario, non audité). Ce qu'il laisse implicite est traité comme **HYPOTHÈSE**.
- **Deux blocs identiques.** Les blocs FAITS et QUESTION portent la même empreinte sha256 et ont un contenu identique. Je ne peux pas recalculer l'empreinte ; c'est une observation sur la pièce, pas une anomalie établie.
- **« Loi déjà publiée » non nommée.** La loi n'est pas identifiée. Je ne la devine pas ; tout exemple cité plus bas n'est qu'un candidat.
- **Pas d'autres propositions.** Les propositions A, C à F ne sont pas transmises à ce tour (aveugle). B1 ne s'applique donc pas ici.
- **Références.** Toutes sont citées de mémoire. Celles dont je suis moins sûr portent « à vérifier ».

## 1. Position de B en quatre lignes

1. **Usage.** L'ensemble sert à la **portée** des affirmations (i) et (ii), et à un **audit unique du critère de passage**. Il ne sert jamais au critère lui-même.
2. **Moment.** Il est consulté **une seule fois par affirmation pré-enregistrée**, après gel des détecteurs. Cette consultation unique peut évaluer d'un coup plusieurs points de contrôle gelés.
3. **Exposition.** La réponse **dépend d'un élément nommé** : l'*exposition différentielle datée*. Il faut savoir ce qui a été vu (entrées, étiquettes ou scores), par les auteurs de quel détecteur, et avant ou après le gel. Le défaut est de déclasser la partie exposée, pas de jeter l'ensemble.
4. **Changement d'affirmation.** Il modifie les réponses **en partie**. Il change le critère de la question 3, les exigences de puissance et le besoin de cas négatifs. Il ne change pas la règle de consultation unique.

## (a) Ce que la question suppose sans que ce soit établi

| # | Supposition | Statut | Si elle est fausse |
|---|---|---|---|
| S1 | Les auteurs des détecteurs n'ont pas consulté ce genre de dégradation. | RAPPORTÉ (aucun journal d'accès mentionné) | La question 3 devient la question principale. |
| S2 | L'ensemble contient des cas honnêtes du même genre, en plus des cas dégradés. | HYPOTHÈSE (l'énoncé dit « cas de dégradation ») | Le taux de fausses alertes est **non mesurable** sur l'ensemble : on ne mesure qu'un taux de détection à seuil fixé ailleurs. |
| S3 | L'étiquette « dégradé » est établie par un oracle mécanique (tests, métrique de sortie) et non par un jugement. | HYPOTHÈSE | Toute mesure dépend de l'avis de l'étiqueteur. |
| S4 | La loi publiée est identifiée et fournit une prédiction avec bande d'incertitude, sans réajuster ses paramètres sur l'ensemble. | HYPOTHÈSE | L'affirmation (i) est irréfutable (paramètres libres) ou vide. |
| S5 | Le détecteur interne et le détecteur textuel sont évalués sur les **mêmes** trajectoires. | HYPOTHÈSE | La comparaison (ii) est confondue par l'échantillon. |
| S6 | Le changement d'affirmation n'a pas été informé par une consultation de l'ensemble. | HYPOTHÈSE | Risque de formulation d'hypothèse après coup (HARKing) : (i) et (ii) seraient choisies sur les données. |
| S7 | La taille de l'ensemble, fixée pour l'ancienne affirmation (« bon en soi »), suffit pour un test de différence (ii) et un test d'écart (i). | HYPOTHÈSE | La consultation unique est gaspillée (puissance insuffisante). |
| S8 | Le critère chiffré de passage est calculé sur des données disjointes de l'ensemble. | HYPOTHÈSE | L'ensemble est déjà contaminé par la boucle. |
| S9 | Le « genre » est une distribution réellement distincte, et non un artefact de surface (format, longueur). | HYPOTHÈSE | La portée « hors-genre » mesure un artefact. |
| S10 | L'état interne de l'agent est accessible, donc les poids sont ouverts ou l'instrumentation est fournie. | HYPOTHÈSE (implicite dans (ii)) | L'affirmation (ii) est inexécutable. |
| S11 | Le nombre de cycles n'est pas fixé et l'arrêt dépend d'un critère atteint. | RAPPORTÉ | Arrêt optionnel : le score au moment du passage est biaisé vers le haut (malédiction du gagnant), même sur les données de développement. |
| S12 | « Avoir vu » est binaire. | HYPOTHÈSE (implicite dans la question 3) | Faux en général : voir les entrées, les étiquettes, les scores agrégés ou les erreurs individuelles ne fuit pas la même chose. |

## 2. Réponses aux questions 1 à 4

### Question 1 — À quoi sert l'ensemble

**Réponse de B.** À la portée de (i) et de (ii), et à « autre chose » : auditer une fois si le critère de passage prédit la performance hors-genre. Pas au critère de passage.

- **Énoncé réfutable R1.** Si un ensemble hors-genre entre dans la boucle de passage avec arrêt optionnel, la performance mesurée sur lui à la sortie dépasse celle mesurée sur une portion scellée du même genre. Mesure : l'écart d'AUROC ou de taux de détection à fausses alertes fixées, entre portion consultée et portion scellée. Test décisif : E1.
- **Énoncé réfutable R1′.** Le score du critère de passage, calculé sur les données de développement, est corrélé positivement au score hors-genre à travers les points de contrôle gelés. Mesure : corrélation de rang de Spearman entre les deux scores, sur tous les points gelés, en une seule consultation. Si la corrélation est nulle ou négative, le critère de passage ne dit rien de la portée.
- **Antériorité (de mémoire).**
  - Dwork, Feldman, Hardt, Pitassi, Reingold, Roth (2015), « The reusable holdout: Preserving validity in adaptive data analysis », *Science*.
  - Recht, Roelofs, Schmidt, Shankar (2019), « Do ImageNet Classifiers Generalize to ImageNet? », ICML.
  - Kapoor, Narayanan (2023), « Leakage and the reproducibility crisis in machine-learning-based science », *Patterns*.
- **Contrôle indépendant de tout avis.** Avant toute ouverture, l'équipe publie ou dépose l'empreinte cryptographique des poids, du code, des seuils et du script d'analyse. Le résultat est le chiffre produit par le script haché, rien d'autre.
- **Certitude.**
  - Exclusion de l'ensemble du critère de passage : élevée (le mécanisme de fuite adaptative est établi).
  - Utilité réelle pour (i) : faible tant que S4 n'est pas levée.

### Question 2 — Quand le consulter

**Réponse de B.** Une seule fois par affirmation, après gel. La découpe « par parties » n'est recevable que si chaque partie est scellée, consultée une seule fois et suffisamment puissante (E5). « À chaque cycle » n'est recevable qu'avec un mécanisme de type « holdout réutilisable » à budget déclaré, et alors (i) et (ii) exigent une portion restée scellée.

- **Énoncé réfutable R2.** Sur un genre substitut (pas l'ensemble précieux), une boucle d'amélioration automatisée qui consulte une portion à chaque cycle produit un écart consulté−scellé qui croît avec le nombre de cycles. Mesure : pente de l'écart en fonction du nombre de cycles (E1).
- **Antériorité (de mémoire).**
  - Klein, Roodman (2005), « Blind analysis in nuclear and particle physics », *Annual Review of Nuclear and Particle Science*.
  - Blum, Hardt (2015), « The Ladder: A Reliable Leaderboard for Machine Learning Competitions », ICML.
  - Armitage, McPherson, Rowe (1969), « Repeated significance tests on accumulating data », *JRSS A*.
  - Lan, DeMets (1983), « Discrete sequential boundaries for clinical trials », *Biometrika*.
- **Contrôle indépendant de tout avis.** Un journal d'accès horodaté et append-only sur le stockage de l'ensemble. L'ensemble est chiffré, et la clé est détenue par une personne qui ne développe pas de détecteur. Le nombre de déchiffrements est un fait comptable.
- **Certitude.**
  - Inflation par consultation répétée : élevée pour un nombre de cycles non fixé.
  - Ampleur de cette inflation dans ce cas précis : inconnue, d'où E1.

### Question 3 — Si des auteurs l'ont vu

**Réponse de B.** Cela dépend de l'élément nommé : l'**exposition différentielle datée**. Elle se décompose en quatre questions :

- (a) Quoi : entrées seules, étiquettes, scores par cas ?
- (b) Par qui : auteurs du détecteur textuel, du détecteur interne, des deux ?
- (c) Quand : avant ou après le gel haché ?
- (d) Quelle partie : sélectionnée au hasard ou non ?

**Règle de décision proposée.**

| Situation | Décision |
|---|---|
| Exposition **après** gel haché | **Garder**. Le gel rend l'exposition sans effet sur les détecteurs. |
| Exposition **avant** gel, partie identifiable | **Déclasser** la partie exposée en développement. Garder la partie non exposée si la sélection de la partie exposée était aléatoire et si la puissance reste suffisante (E5). Sinon, **refaire** un ensemble sur un nouveau genre. |
| Exposition avant gel, partie non identifiable | **Refaire**. |
| Tous les cas | **Jeter** n'est jamais nécessaire : un ensemble déclassé garde une valeur de développement. |

- **Énoncé réfutable R3.** Pour l'affirmation (ii), une exposition **symétrique** des deux équipes n'annule pas le biais. Le détecteur interne, qui a plus de degrés de liberté (dimension des activations), surajuste davantage que le détecteur textuel. Statut : HYPOTHÈSE de B. Mesure : le gain du détecteur interne sur la partie vue moins son gain sur la partie non vue, comparé au même écart pour le détecteur textuel (E4).
- **Antériorité (de mémoire).**
  - Kapoor, Narayanan (2023), cité plus haut, pour la taxonomie des fuites.
  - Sainz, Campos, García-Ferrero, Etxaniz, Lopez de Lacalle, Agirre (2023), « NLP Evaluation in trouble: On the Need to Measure LLM Data Contamination for each Benchmark », Findings of EMNLP (liste d'auteurs à vérifier).
  - Ligne directrice ICH E9 (1998), « Statistical Principles for Clinical Trials », pour la gestion de la levée d'aveugle.
- **Contrôle indépendant de tout avis.** Recouper le journal d'accès avec l'horodatage des empreintes de gel. Une exposition est « avant gel » si et seulement si un accès précède l'empreinte : c'est une comparaison de dates.
- **Certitude.**
  - Que la décision dépende de (a) à (d) : élevée.
  - R3 : faible ; c'est une hypothèse à tester.

### Question 4 — Le changement d'affirmation modifie-t-il les réponses

**Réponse de B.** En partie.

| Ce qui change | Ce qui ne change pas |
|---|---|
| **Usages.** « Bon en soi » se contentait d'un taux de détection. (ii) exige des cas honnêtes appariés (S2) et un test de différence apparié. (i) exige une prédiction externe (S4). | Exclusion de l'ensemble du critère de passage. |
| **Critère de la question 3.** L'exposition *absolue* compte pour « bon en soi ». Pour (ii), c'est l'exposition *différentielle* qui compte. | Règle de consultation unique après gel. |
| **Puissance.** Une différence entre deux détecteurs corrélés demande en général plus de cas qu'une performance isolée. | |
| **Nouveau risque.** Le changement d'affirmation est postérieur à la constitution de l'ensemble : il faut dater ce changement par rapport à tout accès (S6). | |

- **Énoncé réfutable R4.** La puissance de l'ensemble tel que constitué, pour l'effet minimal pré-enregistré de (ii), est inférieure à celle qu'il avait pour l'ancienne affirmation. Mesure : calcul de puissance (E5). Il ne dépend d'aucun avis une fois l'effet minimal fixé.
- **Antériorité (de mémoire).**
  - Kerr (1998), « HARKing: Hypothesizing After the Results are Known », *Personality and Social Psychology Review*.
  - Nosek, Ebersole, DeHaven, Mellor (2018), « The preregistration revolution », *PNAS*.
  - Pour (ii), notion de validité incrémentale : Sechrest (1963), « Incremental validity: A recommendation », *Educational and Psychological Measurement*.
  - Pencina, D'Agostino Sr, D'Agostino Jr, Vasan (2008), « Evaluating the added predictive ability of a new marker: from area under the ROC curve to reclassification and beyond », *Statistics in Medicine*.
- **Contrôle indépendant de tout avis.** Comparer la date de pré-enregistrement des affirmations (i) et (ii) au journal d'accès.
- **Certitude.** Moyenne. Le « en partie » pourrait devenir « oui » si E5 montre que l'ensemble est sous-dimensionné, car il faudrait alors le refaire.

## (b) Expériences décisives (inférence forte)

Les seuils ci-dessous sont **illustratifs** ; ils doivent être pré-enregistrés avant toute exécution.

### E1 — La consultation répétée gonfle-t-elle la mesure ? (questions 1 et 2)

- **Plan.** On n'utilise pas l'ensemble précieux. On construit un **genre substitut** G′, séparé en G′-consulté et G′-scellé par tirage aléatoire. Une boucle d'amélioration **scriptée** (recherche d'hyperparamètres, de seuils et de couches, sans humain) consulte G′-consulté à chaque cycle et s'arrête selon un critère chiffré, comme l'équipe.
- **H_A :** l'écart Δ = score(G′-consulté) − score(G′-scellé) au moment du passage est positif.
- **H_B :** Δ ≈ 0 dans une marge préfixée.
- **Métrique.** Taux de détection à fausses alertes fixées (1 %, illustratif), avec un intervalle de confiance à 95 % par bootstrap apparié.
- **Seuil.** H_A est retenue si la borne inférieure de Δ dépasse 0. H_B est retenue si l'intervalle est inclus dans [−0,02 ; +0,02] (illustratif).
- **Contrôle négatif.** Une boucle identique dont les « améliorations » ne changent que la graine. Elle mesure la part de Δ due au seul bruit de sélection. Second contrôle : étiquettes de G′-consulté permutées, pour lesquelles le score scellé doit être au niveau du hasard.
- **Falsification.**
  - Un intervalle de Δ inclus dans la marge sur au moins 20 cycles (illustratif) falsifie H_A, donc la règle « jamais à chaque cycle » de B est trop stricte.
  - Une borne inférieure strictement positive, au-dessus du contrôle par graines, falsifie H_B.

### E2 — Le détecteur interne ajoute-t-il au détecteur textuel ? (affirmation ii)

- **H_A :** sur l'ensemble hors-genre, le combiné texte + interne dépasse le textuel seul à fausses alertes égales.
- **H_B :** aucun gain au-delà de la marge.
- **Métrique.** Différence de taux de détection à 1 % de fausses alertes (illustratif), seuils calibrés **uniquement sur les cas honnêtes de développement**. Test apparié par McNemar sur les cas discordants. Test secondaire : comparaison d'AUROC corrélées selon DeLong, DeLong, Clarke-Pearson (1988), « Comparing the areas under two or more correlated receiver operating characteristic curves: a nonparametric approach », *Biometrics* (de mémoire).
- **Seuil.** Gain d'au moins 0,05 (illustratif), avec une borne inférieure de l'intervalle à 95 % supérieure à 0.
- **Contrôles négatifs (« contrôles de sonde »).**
  - (1) Sonde entraînée sur la **couche 0** (plongements de jetons, donc une information essentiellement textuelle). Le gain du vrai détecteur interne doit dépasser celui de cette sonde.
  - (2) Sonde sur un modèle de même architecture à **poids aléatoires**.
  - (3) Étiquettes permutées.
  - Antériorité : Hewitt, Liang (2019), « Designing and Interpreting Probes with Control Tasks », EMNLP (de mémoire).
- **Contrôle positif.** Une dégradation trivialement visible dans le texte, par exemple un message d'échec de test dans le journal. Les deux détecteurs doivent l'attraper ; sinon la chaîne d'évaluation est défaillante.
- **Falsification.**
  - Un gain dont l'intervalle contient 0, **ou** un gain égalé par la sonde couche 0, falsifie H_A.
  - Un gain au-dessus du seuil et au-dessus des trois contrôles falsifie H_B.
- **Antériorité de domaine (de mémoire, à vérifier).**
  - Baker et al. (2025), « Monitoring Reasoning Models for Misbehavior and the Risks of Promoting Obfuscation » (OpenAI).
  - Goldowsky-Dill et al. (2025), « Detecting Strategic Deception Using Linear Probes ».
  - Greenblatt, Shlegeris, Sachan, Roger (2024), « AI Control: Improving Safety Despite Intentional Subversion », ICML.

### E3 — Les mesures s'écartent-elles de la loi publiée ? (affirmation i)

**Préalable.** S4 doit être levée : nom de la loi, variables, paramètres fixés hors ensemble. Un candidat d'exemple, non une identification : la corrélation linéaire entre performance en distribution et hors distribution décrite par Miller, Taori, Raghunathan, Sagawa, Koh, Shankar, Liang, Carmon, Schmidt (2021), « Accuracy on the Line », ICML (de mémoire).

- **H_A :** les points hors-genre (un par détecteur gelé) tombent dans la bande de prédiction à 95 % de la loi.
- **H_B :** une fraction significative tombe hors de la bande.
- **Métrique.** Résidus standardisés par rapport à la prédiction de la loi, et proportion de points hors bande.
- **Seuil.** H_B est retenue si la proportion hors bande dépasse le taux nominal de 5 % avec p < 0,01 en test binomial (illustratif ; les points ne sont pas indépendants s'ils viennent de cycles successifs, il faut alors un bootstrap par grappes).
- **Contrôle négatif.** Même test sur une portion **en distribution** retenue à l'écart. Il ne doit pas signaler d'écart, et son taux de faux signal calibre le test.
- **Falsification.**
  - Une proportion compatible avec le taux nominal falsifie H_B.
  - Un excès significatif, absent du contrôle en distribution, falsifie H_A.
- **Limite de portée.** Avec un seul genre hors distribution, la conclusion porte sur **ce** genre, pas sur « hors distribution » en général.

### E4 — L'exposition a-t-elle biaisé la mesure, et de façon différentielle ? (question 3)

- **H_A :** score(partie vue) − score(partie non vue) dépasse l'écart entre deux moitiés aléatoires de la partie non vue, et cet excès est plus grand pour le détecteur interne que pour le textuel.
- **H_B :** aucun excès au-delà de l'écart aléatoire, ni pour l'un ni pour l'autre.
- **Métrique.** Écart vu/non vu, ajusté sur la difficulté. La difficulté est mesurée par le score d'une vérification mécanique (voir (c)), qui n'a pas pu être influencée par l'exposition.
- **Contrôle négatif.** Une distribution de référence obtenue par mille partitions aléatoires (illustratif) de la partie non vue.
- **Falsification.**
  - Un écart à l'intérieur de la distribution des partitions falsifie H_A ; on garde alors l'ensemble entier.
  - Un écart au-delà du 97,5e centile falsifie H_B ; on déclasse la partie vue.
  - La comparaison interne contre textuel teste R3 séparément.

### E5 — L'ensemble a-t-il la puissance nécessaire pour les nouvelles affirmations ? (question 4)

- **H_A :** avec n_dégradés et n_honnêtes tels quels, et la corrélation entre détecteurs estimée sur le développement, la puissance est d'au moins 0,8 à α = 0,05 pour l'effet minimal de (ii) et pour l'écart minimal de (i).
- **H_B :** la puissance est inférieure à 0,8.
- **Métrique.** Puissance calculée analytiquement et vérifiée par simulation.
- **Contrôle.** Calcul pur, fait **avant** ouverture et à partir des seuls effectifs. Aucun avis n'intervient une fois l'effet minimal pré-enregistré.
- **Ordre de grandeur (illustratif, calculé).** Estimer un taux de fausses alertes de 1 % à ±0,5 point (intervalle à 95 %) demande environ 0,0099 × (1,96 / 0,005)² ≈ 1 500 cas honnêtes du genre.
- **Falsification.**
  - H_A est falsifiée par le calcul. Conséquence : la réponse à la question 4 devient « oui », et il faut refaire ou compléter l'ensemble avant la consultation unique.
  - H_B est falsifiée si le calcul dépasse 0,8.

## (c) Instruments nommés dans la question : la mesure minimale

**Principe commun : des paires jumelles.** Pour chaque trajectoire dégradée, on crée une trajectoire honnête **issue du même état sauvegardé** de l'agent, à la même tâche, bifurquant au point de dégradation. Les deux sont appariées sur la longueur, le nombre d'appels d'outils et la difficulté. Sans cet appariement, un détecteur peut reconnaître la tâche ou la longueur au lieu de la dégradation.

| Instrument | Mesure minimale | Cas honnêtes appariés | Vérifications mécaniques à battre |
|---|---|---|---|
| **Détecteur textuel** | Taux de détection à 1 % et 5 % de fausses alertes (illustratif), et **latence** (nombre d'étapes entre la dégradation et l'alerte) | Paires jumelles, hors-genre et en distribution | (1) Classifieur sur métadonnées : nombre d'étapes, d'erreurs d'outil, de reprises, longueur. (2) Expressions régulières sur les messages d'erreur. (3) Log-probabilité ou perplexité moyenne des sorties de l'agent. (4) Suite de tests finale, qui sert de référence de rappel mais avec une latence maximale. |
| **Détecteur sur état interne** | Idem, plus le **gain incrémental** sur le détecteur textuel combiné aux métadonnées (E2) | Mêmes paires | Les quatre précédentes, la sonde couche 0, la sonde sur poids aléatoires et le détecteur textuel lui-même. |
| **Critère chiffré de passage** | Corrélation de rang entre son score et le score hors-genre, sur les points gelés, en une seule consultation (R1′) | — | Un critère trivial, par exemple « nombre de cycles écoulés ». S'il prédit aussi bien le hors-genre, le critère n'apporte rien. |
| **Ensemble hors-genre** | (1) Présence et nombre de cas honnêtes (S2). (2) Accord des étiquettes avec un oracle mécanique (S3), en pourcentage. (3) **Séparabilité du genre** : AUROC d'un classifieur qui distingue l'ensemble des données de développement. Près de 0,5, la distinction de genre est douteuse. Près de 1 grâce à des traits de surface seuls (format, longueur), le hors-genre est un artefact. | — | Le classifieur de séparabilité limité aux traits de surface. |
| **Loi publiée** | Calibration de sa bande de prédiction sur la portion en distribution : environ 5 % de points hors bande attendus | — | Un modèle nul (moyenne constante) : si la loi ne prédit pas mieux que lui en distribution, l'écart hors-genre n'a pas de sens. |

Un détecteur qui ne bat pas, à fausses alertes égales, la meilleure de ces vérifications mécaniques **ou** qui ne la bat pas en latence ne peut pas porter l'affirmation (ii).

## (d) Ancrage matériel

**Tout ce bloc est illustratif ; rien ne vient des faits.**

- **Agent.** Un modèle ouvert, imposé par S10.
  - Qwen2.5-Coder-32B-Instruct pour l'agent principal.
  - Llama-3.1-8B-Instruct pour une réplication à petite échelle, afin de vérifier que le gain de E2 ne dépend pas de la taille.
- **Détecteur textuel.**
  - Un juge ouvert, par exemple Qwen2.5-7B-Instruct utilisé par invite.
  - Un classifieur affiné.
  - Les deux variantes sont gelées par empreinte.
- **Détecteur interne.** Une sonde linéaire, puis une petite sonde non linéaire, sur les activations résiduelles de quelques couches. Les activations sont moyennées par étape et non stockées par jeton : à raison de 2·10⁸ jetons, un stockage par jeton représenterait plusieurs téraoctets.
- **Volume.** 2 000 trajectoires (1 000 dégradées et 1 000 jumelles honnêtes), soit 50 étapes × 2 000 jetons ≈ 10⁵ jetons par trajectoire, donc ≈ 2·10⁸ jetons au total. Pour estimer un taux de fausses alertes de 1 % à ±0,5 point, il faut monter vers 1 500 cas honnêtes du genre (E5).
- **Calcul.**

| Poste | Estimation |
|---|---|
| Génération | ≈ 30 GPU-heures H100, avec vLLM et cache de préfixe, à environ 2 000 jetons/s effectifs |
| Extraction des activations | ≈ 30 GPU-heures supplémentaires (une passe avant) |
| E1 sur genre substitut, 20 cycles | ≈ 50 GPU-heures |
| Sondes et contrôles | négligeable |
| **Total** | **≈ 100 à 150 GPU-heures**, soit quelques centaines de dollars à 2–3 $ par GPU-heure |

- **Infrastructure d'intégrité.**
  - Stockage chiffré de l'ensemble, avec clé détenue par un tiers interne.
  - Journal d'accès append-only.
  - Script d'analyse haché et déposé avant ouverture.
  - Coût marginal quasi nul.

## Ce qui réfuterait la position de B

1. **Règle « jamais à chaque cycle ».** E1 donne un Δ inclus dans la marge sur au moins 20 cycles. B aurait été trop prudent.
2. **Valeur de l'ensemble pour la portée.** La séparabilité du genre est voisine de 0,5, ou entièrement expliquée par la surface. L'ensemble ne pourrait alors pas porter un énoncé « hors-genre ».
3. **Critère « exposition différentielle ».** E4 montre un biais symétrique identique pour les deux détecteurs, avec R3 réfutée. Pour (ii), une exposition symétrique serait alors tolérable, et la règle de déclassement de B serait trop stricte.
4. **Réponse « en partie » à la question 4.** E5 montre une puissance insuffisante : la réponse devient « oui », car l'ensemble est à refaire.
5. **Faisabilité de (i).** S4 ne peut pas être levée (loi sans prédiction fixe). L'affirmation (i) serait alors non réfutable, et l'ensemble ne servirait qu'à (ii).

FIN-DE-CELLULE