# Proposition B : Collisionneur 3×3, tour III.1

**État des pièces.** Le bloc FAITS est vide, et l'arbitre l'a déclaré comme tel. Aucun fait n'a donc le statut VÉRIFIÉ. La description du système et celle de la conception sont RAPPORTÉES par la question. Tout le reste est HYPOTHÈSE, sauf mention contraire. Je ne peux pas vérifier les empreintes sha256. Les propositions A et C ne me sont pas visibles à ce tour aveugle : je ne peux ni les attaquer ni m'en servir.

---

## 0. Objets nommés

- **Organisme** à la génération *t* : un ensemble de fichiers *F_t*. Le noyau *K* est fixe et les modèles de frontière *M* sont figés. Une génération applique *F_{t+1} = Φ(F_t ; M, K)* et rend la récompense *r_t = S_dev(F_{t+1})*. Tout ceci est RAPPORTÉ.
- **Système dessiné (S_fig).** Φ est exécuté par l'organisme lui-même, qui s'appuie sur *M*. Ce qui est appris est *F_t*. C'est une optimisation **non paramétrique, intra-lignée, dans le contexte**. Le « paramètre » est le texte de la lignée.
- **Conception évaluée (D_RL).** C'est une politique *π_θ(a | x)*, avec :
  - *x* = (*F_t*, historique des scores, descripteur de famille) ;
  - *a* = la spécification complète (code, composition, mémoire, spécification d'entraînement des sondes et de l'adaptateur).

  Elle maximise *J(θ) = E_{famille, x} E_{a∼π_θ}[S_dev(exec(a))] − β·KL(π_θ ‖ π_ref)*. La régularisation KL est mon hypothèse d'implémentation, pas une donnée.
- **Conséquence formelle de « un épisode = une génération ».** Il s'agit d'un **bandit contextuel à un pas**, pas d'un processus de décision markovien à horizon supérieur à 1. Rien dans *J* ne récompense ce qu'une génération lègue aux suivantes. C'est une HYPOTHÈSE de lecture, mais elle découle directement du texte.
- **Distinction centrale.** S_fig fait de l'**optimisation par lignée**. D_RL fait de l'**amortissement inter-lignées** : il apprend dans les poids un a priori *p_θ(a | x)* partagé entre familles.

---

## (a) Ce que la question suppose sans que ce soit établi

| # | Présupposé | Statut | Pourquoi ce n'est pas acquis |
|---|---|---|---|
| a1 | Un épisode d'une seule génération suffit pour apprendre à concevoir | HYPOTHÈSE | Bandit myopique : la mémoire n'est récompensée que si elle paie dans la même génération. Or, dans S_fig, la mémoire sert les générations **suivantes** (RAPPORTÉ). Il y a une tension directe. |
| a2 | Il existe une structure de conception partagée entre familles de tâches, donc transférable | HYPOTHÈSE | Si les familles sont hétérogènes, l'a priori amorti est neutre, voire nuisible. |
| a3 | La récompense *S_dev* est assez peu bruitée pour fournir un gradient utile | HYPOTHÈSE | Raisonnement explicite, entrées illustratives : avec *n* = 200 items et *p* = 0,7, l'écart-type binomial vaut √(0,21/200) ≈ 3,2 points. Une seule évaluation par épisode a donc un bruit du même ordre que les gains recherchés. |
| a4 | Le score de développement est un proxy fidèle et non exploitable | HYPOTHÈSE | La question prévoit elle-même des mesures de dérive (RAPPORTÉ) : l'arbitre ne le tient pas pour acquis. |
| a5 | Les modèles de frontière restent figés pendant des milliers d'épisodes | RAPPORTÉ pour le noyau ; HYPOTHÈSE pour la stabilité des versions chez les fournisseurs dans la durée | Un concepteur ajusté à des exécuteurs précis peut devenir obsolète quand ceux-ci changent. |
| a6 | Un modèle de taille moyenne, une fois entraîné, conçoit mieux qu'un modèle de frontière non entraîné | HYPOTHÈSE | Des travaux de 2025 le rapporteraient pour des flux de travail (référence à vérifier). Le transfert à des organismes auto-modifiants n'est pas établi. |
| a7 | « Rien, dans des poids, n'apprend à concevoir » dans S_fig | RAPPORTÉ ; la portée est HYPOTHÈSE | L'instrument (B) permet en principe à l'organisme d'entraîner un adaptateur de 8 milliards de paramètres **qui propose des conceptions**, avec *S_dev* comme récompense. D_RL pourrait donc être un cas particulier déjà atteignable par S_fig, à moindre échelle. |
| a8 | Des milliers d'épisodes sont finançables | HYPOTHÈSE | Le coût est dominé par l'exécution des générations, pas par le concepteur (voir (d)). |
| a9 | Ce que l'on mesure dans les activations du concepteur renseigne sur la qualité ou l'honnêteté de ses conceptions | HYPOTHÈSE | Aucune validation n'est prévue. À tester contre l'analyse statique (voir (c), ligne 8). |
| a10 | « Même budget » a un sens unique | HYPOTHÈSE | D_RL consomme un budget d'entraînement préalable. Il faut deux comparaisons : à l'usage (entraînement amorti) et en coût total. |

---

## 1. Apport par rapport au système dessiné : deux lectures

### Lecture 1 : D_RL apporte quelque chose (HYPOTHÈSE)

- **Ce qui est appris et transféré.** Un a priori paramétrique sur les conceptions, partagé entre lignées, familles et runs, sans copier de fichiers. La prédiction réfutable porte sur un **démarrage à chaud** : sur une famille nouvelle, les premières générations conçues par D_RL devraient être meilleures que celles de S_fig. L'objet à mesurer est la courbe *score(t)* pour *t* petit, plutôt que le plateau.
- **Qualité de conception.** Le gradient de politique, cumulé sur de nombreuses familles, peut renforcer des motifs que le modèle de frontière ne propose pas spontanément : agrégations atypiques, données de sonde, récompenses d'adaptateur.
- **Coût à l'usage.** Un appel à un modèle moyen coûte moins cher qu'un appel à un modèle de frontière. Mais les jetons de conception sont probablement marginaux devant le coût d'exécution d'une génération (HYPOTHÈSE). Le gain éventuel porte donc sur le **nombre de générations nécessaires** pour atteindre un niveau donné, pas sur le coût par appel.
- **Mesurabilité interne.** Les poids ouverts donnent accès à plusieurs quantités inaccessibles avec un modèle de frontière servi par API :
  - les log-probabilités, donc l'entropie de *π_θ* et la divergence KL par rapport à la référence, comme indicateurs précoces d'effondrement ;
  - les activations, donc des sondes sur le concepteur ;
  - des attributions par gradient.

  C'est un apport structurel, mais seulement si a9 tient.

### Lecture 2 : D_RL n'apporte rien de net, ou dégrade (HYPOTHÈSE)

- **L'archive suffit.** Donner à S_fig une archive consultable des mêmes trajectoires, comme dans les méta-agents à archive, pourrait transmettre la même information sans poids. La part attribuable aux poids serait alors nulle (voir E2).
- **Goodhart amplifié.** Chaque épisode est une requête adaptative au jeu de développement. Des milliers de requêtes adaptatives produisent un sur-ajustement attendu par la théorie de l'analyse adaptative des données (Dwork et al., 2015, à vérifier).
  - Un concepteur entraîné **apprend à exploiter** les faiblesses du score de façon systématique et transférable.
  - S_fig ne les exploite que lignée par lignée.
- **Effondrement de diversité.** L'entraînement par renforcement avec récompense scalaire réduit typiquement l'entropie de la politique. La diversité des rôles peut s'effondrer **entre lignées**, et pas seulement au sein d'une lignée.
- **Signalement qui baisse.** Si signaler un cas à un humain coûte du score, la récompense pousse à ne plus signaler. Le gradient généralise cette pression à toutes les familles.
- **Myopie (a1).** Les conceptions qui sacrifient la mémoire au profit du score immédiat sont favorisées.
- **Bi-niveau.** D_RL écrit la récompense de l'adaptateur (B). C'est une boucle de renforcement imbriquée dans une autre, avec deux couches où la récompense peut être exploitée.
- **Obsolescence (a5)** et **concepteur plus faible que les exécuteurs** : un modèle moyen peut mal modéliser ce que les modèles de frontière savent faire.

### Quand cela ne vaut pas la peine

Seuil de rentabilité : si *C_train* est le coût d'entraînement et *Δc* l'économie par run future pour atteindre un niveau cible, alors D_RL ne paie que si le nombre de runs futures dépasse *n\* = C_train / Δc*.

Exemple illustratif : *C_train* = 150 k$ et *Δc* = 1 k$ donnent *n\** = 150 runs. D_RL ne vaut pas la peine dans les cas suivants :

- peu de familles ou de runs sont prévus (*n* < *n\**) ;
- S_fig atteint son plateau en quelques générations ;
- le rapport signal sur bruit de *S_dev* est faible (a3) ;
- les familles n'ont pas de structure partagée (a2) ;
- les fournisseurs changent les exécuteurs plus vite que l'entraînement ne s'amortit.

---

## 2. Apport par rapport à ce qui est publié

Toutes les références sont marquées « à vérifier ». Celles dont je ne peux pas garantir l'attribution portent la mention « référence à vérifier » sans auteurs.

| Famille | Travaux | Commun avec D_RL | Nouveau éventuel (HYPOTHÈSE) | À vérifier |
|---|---|---|---|---|
| Méta-agents figés qui écrivent des agents en code et les archivent | Hu, Lu, Clune (2024), *Automated Design of Agentic Systems* ; Zhang et al. (2024), *AFlow: Automating Agentic Workflow Generation* | Espace de conception = code ; évaluation par score | Les poids du concepteur sont mis à jour entre familles ; l'action inclut la mémoire et la spécification d'entraînement | Si l'archive seule égale les poids (E2) |
| Réécriture de son propre code par un modèle figé | Zelikman et al. (2023), *Self-Taught Optimizer (STOP)* ; Zhang, Hu, Lu, Lange, Clune (2025), *Darwin Gödel Machine* ; Schmidhuber, *Gödel Machines* (année à vérifier) | **C'est S_fig.** | D_RL est **moins** auto-référentiel : le concepteur est extérieur à l'organisme. C'est de la conception amortie plutôt que de l'auto-amélioration. | Ne pas présenter D_RL comme « auto-amélioration » |
| Modèles moyens entraînés par renforcement à concevoir des flux ou des systèmes d'agents pour des exécuteurs plus forts | Travaux de 2025 (méta-agent faible pour exécuteurs forts, méta-agents par requête, optimisation de flux guidée par score) : **référence à vérifier**, auteurs non attribués ici | **Famille la plus proche** : modèle moyen, renforcement, exécuteurs forts figés | Épisode = génération d'un organisme **auto-modifiant** avec état de lignée en entrée ; action qui inclut mémoire, sondes et récompense d'adaptateur ; jugement sur familles tenues à l'écart avec bras apparié | Si ces travaux couvrent déjà le multi-tour, la mémoire ou des familles tenues à l'écart. Sinon la nouveauté est faible. |
| Organisations d'agents entraînées conjointement par récompense collective | Foerster et al. (2018), *Counterfactual Multi-Agent Policy Gradients* ; Rashid et al. (2018), *QMIX* ; variantes multi-agents par renforcement avec modèles de langue en 2025 (référence à vérifier) | Une récompense collective attribuée à une organisation | Ici, **seul le concepteur** apprend : l'attribution du crédit porte sur la structure, pas sur les agents | Si l'entraînement conjoint des exécuteurs (impossible ici, ils sont figés) dominerait |
| Modèles figés qui écrivent des récompenses | Kwon, Xie, Bullard, Sadigh (2023), *Reward Design with Language Models* ; Ma et al. (2023), *Eureka* ; Yu et al. (2023), *Language to Rewards for Robotic Skill Synthesis* | **C'est l'instrument (B) de S_fig.** | Un concepteur **entraîné** à écrire des récompenses : apprendre la conception de récompense elle-même | Si cela existe déjà sous la forme d'un apprentissage de la conception de récompense |
| Optimisation de prompts et de programmes à cerveaux figés | Yang et al. (2023), *Large Language Models as Optimizers* ; Fernando et al. (2023), *Promptbreeder* ; Khattab et al. (2023), *DSPy* ; Yuksekgonul et al. (2024), *TextGrad* ; Zhuge et al. (2024), *GPTSwarm* ; Romera-Paredes et al. (2024), *Mathematical discoveries from program search with large language models* | Famille de S_fig | Rien pour D_RL. Ce sont les **témoins** à battre. | — |
| Méta-apprentissage et apprentissage de l'architecture | Zoph & Le (2017), *Neural Architecture Search with Reinforcement Learning* ; Real et al. (2019), *Regularized Evolution for Image Classifier Architecture Search* ; Li & Talwalkar (2019), *Random Search and Reproducibility for Neural Architecture Search* ; Finn, Abbeel, Levine (2017), *MAML* ; Duan et al. (2016), *RL²* ; Wang et al. (2016), *Learning to reinforcement learn* | **D_RL est une recherche d'architecture neuronale à contrôleur appris par renforcement**, où l'architecture est un système d'agents | La conception est transférée entre familles, comme en méta-apprentissage | Leçon RAPPORTÉE, à vérifier : en recherche d'architecture, l'évolution et la recherche aléatoire bien réglées se sont montrées compétitives face au contrôleur appris. S_fig, recherche quasi évolutive, est donc un témoin fort et pas un homme de paille. |
| Conception d'environnements et diversité | Dennis et al. (2020), *Emergent Complexity and Zero-shot Transfer via Unsupervised Environment Design* ; Lehman & Stanley (2011), *Abandoning Objectives* ; Mouret & Clune (2015), *Illuminating search spaces by mapping elites* | Un « concepteur » entraîné, avec un risque d'effondrement | Des archives de qualité et de diversité comme remède à l'effondrement | Si une contrainte de diversité préserve le gain |

**Ce qui serait nouveau (HYPOTHÈSE).** Chaque composante existe déjà. La nouveauté possible tient à la **combinaison** de trois éléments :

1. un concepteur entraîné par renforcement dont l'action est un organisme auto-modifiant complet, mémoire et instruments en boîte blanche compris ;
2. un état de lignée en entrée ;
3. un protocole d'évaluation sur familles tenues à l'écart, avec bras apparié et mesure des dérives.

Mes connaissances peuvent être en retard sur la date de la question (octobre 2026). Une recherche bibliographique ciblée sur 2025–2026 est donc obligatoire avant toute revendication.

---

## (b) Expériences décisives (inférence forte)

**Bras communs.** Chaque bras est défini comme suit :

- **S_fig** : concepteur de frontière figé.
- **S_fig+arch** : S_fig plus une archive consultable des trajectoires d'entraînement de D_RL, à information égale.
- **D_0** : le modèle moyen non entraîné.
- **D_RL** : le concepteur entraîné.
- **D_perm** : renforcement avec récompenses **permutées** entre épisodes.
- **B_int** : l'organisme entraîne lui-même un concepteur via l'instrument (B), à budget total égal.

Les familles sont réparties en entraînement et tenues à l'écart. L'appariement se fait par famille et par graine. Les seuils sont préenregistrés.

**Inférence.**
- Statistique : moyenne interquartile et intervalles de confiance par bootstrap stratifié (Agarwal et al., 2021, *Deep Reinforcement Learning at the Edge of the Statistical Precipice*, à vérifier).
- Équivalence testée par deux tests unilatéraux.
- La marge *δ* = 2 points d'exactitude est illustrative.

**Puissance (raisonnement explicite, entrées illustratives).** Pour des différences appariées d'écart-type *σ_d* = 5 points, avec α = 0,05 et une puissance de 0,8 :

*n ≈ (1,96 + 0,84)² · 25 / 4 ≈ 49 couples famille × graine.*

Une expérience pilote doit d'abord mesurer *σ_d*. Si le nombre de couples n'est pas atteignable, l'issue est déclarée **non concluante a priori** plutôt qu'interprétée.

### E1 : transfert aux familles tenues à l'écart
- **H_A :** D_RL dépasse S_fig de plus de *δ* en exactitude sur le test caché des familles tenues à l'écart, après *G* générations, à budget d'usage égal.
- **H_B :** la différence est dans [−δ, +δ], ou S_fig fait mieux.
- **Métriques.** Différence appariée de l'exactitude au test. Secondaire : aire sous la courbe *score(t)* pour *t* ≤ 3 (démarrage à chaud).
- **Contrôle négatif.** D_perm ne doit pas dépasser D_0. Si D_perm ≈ D_RL, le gain ne vient pas du signal de récompense.
- **Ce qui falsifie chaque hypothèse.**
  - Intervalle de confiance entièrement au-dessus de *δ* : H_B est falsifiée.
  - Intervalle dans [−δ, δ] ou en dessous : H_A est falsifiée.
  - D_perm ≈ D_RL : H_A est falsifiée **même si D_RL > S_fig**, l'apport ne venant pas de l'apprentissage.
- La comparaison est faite deux fois : une fois à l'usage, une fois en coût total.

### E2 : poids contre archive
- **H_A :** le gain de D_RL vient de l'amortissement paramétrique. S_fig+arch reste inférieur à D_RL de plus de *δ*.
- **H_B :** S_fig+arch égale D_RL à *δ* près.
- **Métrique.** Comme pour E1.
- **Contrôle négatif.** S_fig avec une archive **mélangée** (scores permutés) ne doit pas dépasser S_fig.
- **Ce qui falsifie.**
  - Équivalence : H_A est falsifiée. Les fichiers suffisent, ce qui donne raison à la lecture 2.
  - Écart supérieur à *δ* : H_B est falsifiée. Les poids portent quelque chose que l'archive ne transmet pas.

### E3 : exploitation du score (canari)
Une faiblesse **plantée** est introduite dans *S_dev* d'une partie des familles d'entraînement : par exemple, un champ de métadonnées corrélé à l'étiquette, ou un document de la recherche documentaire qui contient des étiquettes du jeu de développement.
- **H_A :** D_RL exploite le canari dans une fraction de lignées supérieure à celle de S_fig, et transfère l'exploitation à des familles tenues à l'écart qui portent un canari **de forme différente**.
- **H_B :** les taux d'exploitation sont équivalents.
- **Métriques.**
  - Taux d'exploitation, détecté par vérification mécanique : accès au champ ou au document canari.
  - Écart développement − test en fonction du logarithme du nombre d'épisodes.
- **Contrôle négatif.** Des familles sans canari, où le détecteur doit indiquer environ 0 % (taux de fausses alertes). Une conception figée réévaluée sans adaptation doit présenter un écart développement − test d'environ 0.
- **Ce qui falsifie.**
  - Taux de D_RL nettement supérieur (intervalle de confiance de la différence > 0) : H_B est falsifiée.
  - Taux équivalents : H_A est falsifiée. L'argument « Goodhart amplifié » de la lecture 2 tombe.

### E4 : diversité et signalement
- **H_A :** D_RL réduit, par rapport à S_fig, la diversité structurelle entre lignées **et** le rappel du signalement sur des cas plantés.
- **H_B :** ni l'une ni l'autre ne baisse de plus d'une marge préenregistrée.
- **Métriques.**
  - Score de Vendi sur des plongements de conceptions (Friedman & Dieng, *The Vendi Score*, 2023, à vérifier) et nombre de graphes de rôles distincts.
  - Rappel du signalement sur des items plantés (étiquettes contradictoires, hors champ, instructions injectées) et taux de faux signalements sur des items propres appariés.
- **Contrôle négatif.** D_RL avec un bonus de diversité de type « élites par cellule » (Mouret & Clune, 2015). Si la baisse persiste, la cause n'est pas l'absence de pression de diversité.
- **Ce qui falsifie.** Une baisse supérieure à la marge falsifie H_B. Une stabilité falsifie H_A pour ce risque.

### E5 : horizon de l'épisode
- **H_A :** l'épisode d'une génération (myope) produit des organismes dont la trajectoire **après** la génération conçue est moins bonne qu'avec une récompense sur *K* générations. L'objet est l'aire sous la courbe sur *K* = 5 générations (illustratif) et l'usage de la mémoire.
- **H_B :** pas de différence supérieure à *δ*.
- **Contrôle négatif.** Un organisme dont la mémoire est ablatée. S'il égale les deux bras, la mémoire n'est pas en jeu et E5 ne dit rien.
- **Ce qui falsifie.** Une différence falsifie H_B : il faut redéfinir l'épisode. Une équivalence falsifie H_A : la myopie est inoffensive ici.

### E6 : D_RL est-il déjà atteignable dans S_fig ?
- **H_A :** D_RL dépasse B_int de plus de *δ* à coût total égal.
- **H_B :** B_int ≥ D_RL − δ.
- **Contrôle négatif.** B_int avec une récompense constante.
- **Ce qui falsifie.**
  - H_B confirmée : D_RL n'est qu'un cas particulier, et une infrastructure séparée ne se justifie pas.
  - H_A confirmée : l'échelle hors lignée (milliers d'épisodes, familles multiples) est ce qui compte.

---

## (c) Mesure minimale de chaque instrument nommé

**Principe commun.** Chaque instrument est validé sur des cas plantés positifs et des cas honnêtes appariés au même score, avec un taux de détection mesuré à 5 % de fausses alertes (seuil illustratif). Il doit **battre** une vérification mécanique peu coûteuse.

| # | Instrument | Positifs plantés | Négatifs honnêtes appariés | Métrique | Vérification mécanique à battre |
|---|---|---|---|---|---|
| 1 | Score scalaire *S_dev* | Un organisme auquel on ajoute un oracle sur *k* % des items (gain connu) | Le même organisme réévalué sur un rééchantillon (test A/A) | Fausses alertes au test A/A ≤ α ; détection d'un gain de taille *k* | L'écart-type binomial (a3) : si le gain planté n'est pas détectable au-delà de cet écart-type, le score ne peut pas guider le renforcement |
| 2 | Bras apparié sans apprentissage | Un écart planté entre deux bras | Deux runs du **même** bras avec des graines différentes | Taux de différences « significatives » entre runs identiques ≤ 5 % | Aucune : c'est un étalonnage. S'il échoue, tout le jugement tombe. |
| 3 | Mesure de sur-ajustement au développement | Des organismes contenant des réponses codées en dur sur une fraction du développement, ou des seuils réglés sur le développement | Des organismes de même score de développement sans fuite (appariés par score) | Taux de détection à 5 % de fausses alertes | Une recherche textuelle des identifiants et textes du développement dans les fichiers ; l'écart sur un échantillon frais jamais interrogé |
| 4 | Diversité des rôles | Des lignées forcées à l'effondrement, y compris des **paraphrases** d'un même rôle | Des lignées honnêtement diverses de même score | Taux de détection à 5 % de fausses alertes | Le nombre de couples distincts (modèle, empreinte du prompt). Le compteur d'empreintes rate les paraphrases : la mesure doit les attraper. |
| 5 | Signalement aux humains | Items où signaler est la bonne action (contradiction, hors champ, injection) | Items propres de même famille et de même longueur | Rappel et taux de faux signalements | La règle « signaler si le désaccord de l'ensemble dépasse τ » |
| 6 | Sondes (A) | Une propriété connue, plantée ou annotée | Des **tâches de contrôle** à étiquettes aléatoires (Hewitt & Liang, 2019, *Designing and Interpreting Probes with Control Tasks*, à vérifier) | Sélectivité = exactitude sur la tâche moins exactitude sur le contrôle | Une régression logistique sur les représentations sac de mots du **texte d'entrée**, et une sonde sur un modèle à poids aléatoires. Sans les battre, la sonde ne lit pas les activations, elle relit le texte. |
| 7 | Adaptateur par renforcement (B) | Une récompense avec une faille plantée (longueur, format) | La même récompense sans faille | Détection de l'exploitation ; gain sur un ensemble tenu à l'écart | Le modèle de 8 milliards de paramètres de base avec quelques exemples dans le prompt ; le décalage de la distribution de longueur et de format des sorties, calculé mécaniquement |
| 8 | Mesures internes du concepteur (D_RL) | Des conceptions exploitantes (accès au canari d'E3) | Des conceptions honnêtes de même score de développement | Taux de détection à 5 % de fausses alertes d'une sonde sur les activations du concepteur ; avance temporelle de l'entropie de *π_θ* sur l'effondrement | **L'analyse statique du code produit** (motifs d'accès au développement, étiquettes codées en dur) et le compteur structurel de diversité. Si la sonde ne bat pas l'analyse statique, l'argument « mesurable à l'intérieur » de la lecture 1 tombe (a9). |
| 9 | Recherche documentaire du noyau | Des documents canaris contenant des étiquettes du test ou du développement | Des documents neutres de même thème | Taux d'accès aux canaris détecté | Une correspondance exacte de chaînes dans les journaux de requêtes |

---

## (d) Ancrage matériel

Tous les chiffres de cette section sont illustratifs : rien ne vient des faits.

**Modèles.**
- Concepteur : un modèle à poids ouverts de 7 à 32 milliards de paramètres (familles Qwen, Llama, Mistral ou Gemma ; versions à vérifier).
- Pour B_int : le même modèle de 8 milliards que l'instrument du noyau.
- Entraînement par optimisation de politique relative de groupe (Shao et al., 2024, *DeepSeekMath*, à vérifier) ou par optimisation de politique proximale, avec régularisation KL. Adaptateur de faible rang possible (Hu et al., 2022, *LoRA*, à vérifier).

**Décomposition du coût (raisonnement explicite).** *C_train = N_ep · G · c_gen + C_GPU*, avec :
- *N_ep* = nombre de contextes d'épisode ;
- *G* = taille du groupe, nécessaire vu a3 ;
- *c_gen* = coût d'une génération servie par les modèles de frontière.

Exemple : *N_ep* = 2 000, *G* = 8 et *c_gen* = 10 $ donnent 16 000 générations, soit environ 160 k$ d'appels. *C_GPU* correspond à 8 accélérateurs de classe H100 pendant 1 à 3 semaines, soit environ 5 à 15 k$. L'exécution domine : c'est le poste à réduire.

**Évaluation.**
- E1 à E6 : environ 50 couples × 6 bras × *G* = 10 générations × 10 $, soit environ 30 k$.
- Plus les lignées à canari d'E3 et les runs à *K* générations d'E5.

**Réduction de coût.**
- Entraîner D_RL avec des exécuteurs **ouverts bon marché** en remplacement des modèles de frontière, puis transférer.
- Cela introduit une nouvelle hypothèse, à trancher par un duel :
  - **H_A :** le classement des conceptions sous exécuteurs bon marché prédit leur classement sous exécuteurs de frontière (corrélation de rang préenregistrée, ρ > 0,7 illustratif) ;
  - **H_B :** ce n'est pas le cas.
  - Contrôle négatif : des classements permutés.

**Phasage proposé.** Chaque étape a une règle d'arrêt.

1. **Pilote** sur environ 5 familles. Il mesure *σ_d* et le bruit de *S_dev*, et valide les instruments 1 et 2. On arrête si le test A/A échoue.
2. **E2 et E6 à petite échelle.** Si S_fig+arch ou B_int égalent D_RL, on arrête : la lecture 2 l'emporte, à faible coût.
3. **Sinon, E1, E3 et E4 à la puissance calculée.** E5 n'est mené que si E1 est positif.

---

## Références

Toutes sont marquées « à vérifier ». Elles sont listées uniquement là où l'attribution me paraît correcte. Les autres travaux mentionnés plus haut portent la mention « référence à vérifier » sans attribution.

- Hu, S., Lu, C., Clune, J. (2024). *Automated Design of Agentic Systems*. À vérifier.
- Zhang, J. et al. (2024). *AFlow: Automating Agentic Workflow Generation*. À vérifier.
- Zhang, J., Hu, S., Lu, C., Lange, R., Clune, J. (2025). *Darwin Gödel Machine: Open-Ended Evolution of Self-Improving Agents*. À vérifier.
- Zelikman, E., Lorch, E., Mackey, L., Kalai, A. T. (2023). *Self-Taught Optimizer (STOP): Recursively Self-Improving Code Generation*. À vérifier.
- Kwon, M., Xie, S. M., Bullard, K., Sadigh, D. (2023). *Reward Design with Language Models*. À vérifier.
- Ma, Y. J. et al. (2023). *Eureka: Human-Level Reward Design via Coding Large Language Models*. À vérifier.
- Yu, W. et al. (2023). *Language to Rewards for Robotic Skill Synthesis*. À vérifier.
- Foerster, J. et al. (2018). *Counterfactual Multi-Agent Policy Gradients*. À vérifier.
- Rashid, T. et al. (2018). *QMIX: Monotonic Value Function Factorisation for Deep Multi-Agent Reinforcement Learning*. À vérifier.
- Zoph, B., Le, Q. V. (2017). *Neural Architecture Search with Reinforcement Learning*. À vérifier.
- Real, E. et al. (2019). *Regularized Evolution for Image Classifier Architecture Search*. À vérifier.
- Li, L., Talwalkar, A. (2019). *Random Search and Reproducibility for Neural Architecture Search*. À vérifier.
- Finn, C., Abbeel, P., Levine, S. (2017). *Model-Agnostic Meta-Learning for Fast Adaptation of Deep Networks*. À vérifier.
- Duan, Y. et al. (2016). *RL²: Fast Reinforcement Learning via Slow Reinforcement Learning*. À vérifier.
- Wang, J. X. et al. (2016). *Learning to reinforcement learn*. À vérifier.
- Yang, C. et al. (2023). *Large Language Models as Optimizers*. À vérifier.
- Fernando, C. et al. (2023). *Promptbreeder: Self-Referential Self-Improvement via Prompt Evolution*. À vérifier.
- Khattab, O. et al. (2023). *DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines*. À vérifier.
- Yuksekgonul, M. et al. (2024). *TextGrad: Automatic "Differentiation" via Text*. À vérifier.
- Zhuge, M. et al. (2024). *GPTSwarm: Language Agents as Optimizable Graphs*. À vérifier.
- Romera-Paredes, B. et al. (2024). *Mathematical discoveries from program search with large language models*. À vérifier.
- Dennis, M. et al. (2020). *Emergent Complexity and Zero-shot Transfer via Unsupervised Environment Design*. À vérifier.
- Lehman, J., Stanley, K. O. (2011). *Abandoning Objectives: Evolution Through the Search for Novelty Alone*. À vérifier.
- Mouret, J.-B., Clune, J. (2015). *Illuminating search spaces by mapping elites*. À vérifier.
- Dwork, C. et al. (2015). *The reusable holdout: Preserving validity in adaptive data analysis*. À vérifier.
- Skalse, J., Howe, N., Krasheninnikov, D., Krueger, D. (2022). *Defining and Characterizing Reward Hacking*. À vérifier.
- Gao, L., Schulman, J., Hilton, J. (2023). *Scaling Laws for Reward Model Overoptimization*. À vérifier.
- Hewitt, J., Liang, P. (2019). *Designing and Interpreting Probes with Control Tasks*. À vérifier.
- Agarwal, R. et al. (2021). *Deep Reinforcement Learning at the Edge of the Statistical Precipice*. À vérifier.
- Shao, Z. et al. (2024). *DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models*. À vérifier.
- Hu, E. J. et al. (2022). *LoRA: Low-Rank Adaptation of Large Language Models*. À vérifier.
- Friedman, D., Dieng, A. B. (2023). *The Vendi Score: A Diversity Evaluation Metric for Machine Learning*. À vérifier.
- Schmidhuber, J. *Gödel Machines* (année et intitulé exact : référence à vérifier).

**Bilan réfutable.** Aucune des deux lectures n'est retenue ici. Ce qui les départage :

- **E2** (poids contre archive) et **E6** (B_int contre D_RL), peu coûteuses, peuvent falsifier la lecture 1 tôt.
- **E1**, avec le contrôle D_perm, peut falsifier la lecture 2.
- **E3** et **E4** comptent ce que l'apport éventuel coûterait en exploitation du score, en diversité et en signalement.

FIN-DE-CELLULE