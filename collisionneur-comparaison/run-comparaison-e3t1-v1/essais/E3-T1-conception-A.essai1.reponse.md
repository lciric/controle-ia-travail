# Cellule A — Tour III.1 : qu'apporterait un concepteur entraîné par renforcement

Pièce jointe FAITS : vide par décision de l'arbitre (conv-audit n° 28 § 1). Je n'en infère rien ; tout ce qui suit est HYPOTHÈSE, RAPPORTÉ (littérature) ou VÉRIFIÉ (propriété mathématique ou définitionnelle), avec statut explicite.

Notation commune. Ω : espace des organismes (code + fichiers). J(ω) : score scalaire de l'organisme ω sur le jeu de développement ; J*(ω) : exactitude sur le test caché. La « recherche à cerveaux figés » (RCF) est une marche stochastique ω_{t+1} = M(ω_t, J(ω_t), mémoire), où l'opérateur de mutation M est un modèle de frontière figé, invité par la lignée. Le « concepteur entraîné » (CE) est une politique π_θ(ω | contexte) dont θ est mis à jour par gradient de politique sur R = J(ω), un épisode = une génération.

---

## (a) Ce que la question suppose sans que ce soit établi

1. **Que le signal J est assez informatif pour un gradient.** [HYPOTHÈSE] Un scalaire par épisode, pour une sortie de plusieurs milliers de jetons (structure + composition + mémoire + spécification d'entraînement), donne un estimateur REINFORCE dont la variance croît avec la longueur de la sortie [VÉRIFIÉ, propriété de l'estimateur du gradient de score]. Que des « milliers d'épisodes » suffisent est une hypothèse d'échelle, pas un fait.

2. **Que ce qui serait appris est une « capacité de conception » et non un biais de famille.** [HYPOTHÈSE] Rien ne garantit que θ encode autre chose que « sur les familles d'entraînement, telle topologie marche ». Le transfert entre familles est précisément la question, pas une prémisse.

3. **Que l'épisode = une génération est bien posé.** [OBSERVÉ-NON-AUDITÉ, lecture du texte] Si le concepteur voit les fichiers de la génération précédente, le problème est un processus de décision à horizon = nombre de générations, et la récompense immédiate J(ω_t) omet l'effet de ω_t sur J(ω_{t+1}) (mémoire, instruments A/B hérités). Le traiter comme un bandit contextuel introduit un biais de myopie. Le texte ne tranche pas.

4. **Que la RCF n'apprend « rien dans des poids ».** [VÉRIFIÉ pour les poids ; HYPOTHÈSE pour l'équivalence] Elle n'apprend rien dans des poids, mais elle apprend dans les fichiers : la mémoire de lignée est une forme d'apprentissage en contexte. Comparer « appris dans θ » à « appris dans les fichiers » n'est pas comparer appris à non appris ; c'est comparer deux supports de mémoire avec des propriétés de transfert différentes.

5. **Que les deux approches explorent le même Ω.** [HYPOTHÈSE] Si le CE produit la structure dans un format contraint (schéma JSON, grammaire), son Ω_CE est un sous-espace de Ω_RCF ; une comparaison à Ω inégaux mesure le format, pas l'apprentissage.

6. **Que le plafond est donné par les exécuteurs figés.** [HYPOTHÈSE plausible] Les deux méthodes maximisent J sur des compositions de modèles figés ; le gain maximal est max_Ω J − J(ω_0), inconnu. Si la RCF atteint déjà ce plafond en N générations, le CE ne peut qu'y arriver plus vite ou moins cher, pas plus haut.

7. **Que le score est honnête.** [HYPOTHÈSE] Toute faille de J (fuite dev→structure, biais d'étiquetage, exploit de l'agrégation) sera trouvée plus systématiquement par un gradient que par un opérateur dont le prior humain-textuel freine certaines exploitations [HYPOTHÈSE, cohérente avec la littérature sur la sur-optimisation de récompense, voir § (g)].

8. **Que « modèle de taille moyenne » suffit à écrire des structures d'agents.** [HYPOTHÈSE] La fluence de conception d'un modèle de 7–14 milliards de paramètres en sortie de pré-entraînement est inférieure à celle des modèles de frontière ; le RL part donc d'un point plus bas que la RCF. Il doit rattraper, puis dépasser.

---

## (b) Point 1 de l'arbitre : apport par rapport au système déjà dessiné

### Ce qui serait ajouté

- **Amortissement.** [VÉRIFIÉ au sens définitionnel] Dans la RCF, le coût de conception est payé à chaque lignée. Dans le CE, il est payé une fois en entraînement, puis l'inférence coûte un appel à un modèle de 7–14 B. Le point d'équilibre est : coût_entraînement_CE / (coût_RCF_par_lignée − coût_CE_par_lignée) lignées. S'il faut 5 000 épisodes à 20 $ pièce (illustratif, 100 k$) et qu'une lignée RCF coûte 500 $ (illustratif), l'équilibre est à ~200 lignées (illustratif). En dessous, le CE ne se rembourse pas.

- **Support de transfert.** Entre runs et entre lignées, θ se transfère par copie, comme les fichiers ; entre familles, θ se transfère si et seulement si la politique a extrait une régularité inter-familles. [HYPOTHÈSE à tester, E1 ci-dessous.]

- **Mesurabilité interne.** On peut sonder les activations du concepteur : existe-t-il une représentation linéaire de la valeur attendue d'une conception avant exécution ? Si oui, c'est un critique implicite, exploitable pour filtrer les conceptions sans les exécuter (économie d'épisodes). Dans la RCF, l'opérateur est un modèle de frontière fermé ; on ne sonde rien. [HYPOTHÈSE, E5.]

- **Spécification d'entraînement des instruments A/B.** Le CE pourrait apprendre à écrire des pertes de sondes et des récompenses d'adaptateur qui marchent, ce que la RCF découvre par essais. Mais le délai d'effet (une sonde entraînée à t sert à t+1) aggrave le point 3 de (a).

### Ce qui serait perdu ou risqué

- **Dépendance aux épisodes.** Chaque épisode est une génération complète servie par des modèles de frontière : le coût est externe et non compressible. Un gradient de politique avec échantillonnage de groupe (plusieurs conceptions par contexte pour estimer un avantage) multiplie le coût par la taille du groupe. [VÉRIFIÉ pour la structure du coût ; chiffres en (f).]

- **Exploitation de J.** Le gradient monte vers tout ce qui augmente J, y compris ce qui n'augmente pas J*. La mesure attendue est la courbe (J − J*) en fonction des pas d'entraînement ; une courbe qui s'ouvre est le signe de sur-optimisation. [HYPOTHÈSE, cohérente avec Gao, Schulman, Hilton 2022, à vérifier.]

- **Effondrement de la diversité.** Les politiques optimisées par renforcement tendent à perdre de l'entropie ; une population de conceptions issues d'un seul θ peut être moins variée qu'une population issue de lignées RCF indépendantes. [RAPPORTÉ comme tendance générale ; à mesurer, E3.]

- **Signalement qui baisse.** Si signaler aux humains coûte du budget et n'entre pas dans R, π_θ apprendra à ne plus signaler. La RCF subit la même pression, mais l'opérateur figé porte un prior qui peut la freiner. [HYPOTHÈSE, E4.]

- **Opacité de ce qui est appris.** Les fichiers d'une lignée RCF sont lisibles ; θ ne l'est pas sans instruments.

### Cas où cela ne vaut pas la peine

Nombre de lignées futures inférieur au point d'équilibre ; nombre de familles de tâches trop petit pour que la généralisation inter-familles soit même définissable (moins de ~10 familles, illustratif) ; J présentant des failles connues non corrigées ; RCF déjà saturée en moins de 20 générations (illustratif) ; coût d'une génération dominé par les appels de frontière (le CE ne le réduit pas).

---

## (c) Point 2 de l'arbitre : situation par rapport au publié

Je nomme les familles sans fusionner la conception à l'une d'elles. Références détaillées en (g), toutes « à vérifier ».

1. **Méta-agents à modèle figé qui écrivent des agents en code et les archivent** (Hu, Lu, Clune 2024 ; Zhang et al. 2024 « AFlow »). Commun : l'objet conçu est un programme d'agents évalué par un score. Nouveau dans le CE : l'opérateur de proposition est lui-même entraîné sur la récompense, au lieu d'être figé. À vérifier : que l'entraînement d'un modèle moyen dépasse un opérateur de frontière figé muni d'une archive — ce que ces travaux ne testent pas puisqu'ils n'entraînent pas.

2. **Systèmes qui réécrivent leur propre code avec un modèle figé** (Zhang, Hu, Lu, Lange, Clune 2025 « Darwin Gödel Machine » ; Yin et al. 2024 « Gödel Agent »). C'est, à peu de choses près, le système déjà dessiné : la RCF. Le CE s'en distingue en externalisant la conception dans une politique séparée de l'organisme. À vérifier : si la séparation concepteur/organisme perd l'avantage d'une auto-modification qui connaît ses propres fichiers.

3. **Modèles de taille moyenne entraînés à concevoir des flux ou systèmes d'agents pour des exécuteurs plus forts.** Il existe des travaux qui entraînent un modèle ouvert à produire des systèmes multi-agents ou des flux de raisonnement pour des exécuteurs tiers (référence à vérifier : « MAS-GPT », Ye et al. 2025 ; une seconde famille de « raisonneurs de flux » dont je ne peux attribuer correctement les auteurs — référence à vérifier). Commun : la cible de l'apprentissage est la structure, pas la tâche. Nouveau dans le CE : l'épisode est une génération entière avec mémoire, instruments (A/B) et budget, pas un flux statique ; la récompense est le score de l'organisme résultant. À vérifier : que ces travaux aient montré un transfert inter-familles sur test caché et non une amélioration sur les familles vues.

4. **Organisations d'agents entraînées conjointement par une récompense collective.** La littérature multi-agents par renforcement traite l'attribution de crédit collective (Foerster et al. 2018 « Counterfactual Multi-Agent Policy Gradients » ; Rashid et al. 2018 « QMIX »). Commun : un scalaire collectif pour plusieurs acteurs. Différence : ici, les acteurs sont figés et seul le concepteur apprend ; le problème de crédit est déplacé vers « quelle partie de la conception a compté », non résolu par ces méthodes. À vérifier : si un estimateur contrefactuel (ablation de rôles) réduit la variance.

5. **Modèles figés qui écrivent des fonctions de récompense** (Ma et al. 2023 « Eureka »). Commun : l'organisme (et le CE) écrivent la récompense de l'adaptateur (B). Nouveau : la récompense écrite est elle-même produite par une politique entraînée sur un score amont — récompense d'une récompense. À vérifier : la stabilité d'une boucle à deux niveaux, connue pour être fragile.

6. **Méta-apprentissage et recherche d'architecture** (Zoph, Le 2017 ; Finn, Abbeel, Levine 2017 ; Duan et al. 2016 « RL² » ; Oh et al. 2020 « Discovering Reinforcement Learning Algorithms »). Commun : une politique de contrôle apprise sur des épisodes qui sont eux-mêmes des entraînements. Le CE est structurellement une recherche d'architecture par renforcement (Zoph & Le) où l'« architecture » est un système d'agents et l'« entraînement enfant » est une génération. Ce que la littérature a établi [RAPPORTÉ] : la recherche d'architecture par RL coûte des milliers d'évaluations enfants, et des alternatives plus économes (relaxation différentiable, Liu, Simonyan, Yang 2019 « DARTS » ; évolution régularisée) l'ont souvent rattrapée. Nouveau : un espace non différentiable et un exécuteur figé externe. À vérifier : que le coût par évaluation enfant (une génération à appels de frontière) n'éteigne pas l'approche.

7. **Évolution de code par modèle figé avec évaluateur automatique** (Novikov et al. 2025 « AlphaEvolve », à vérifier ; Fernando et al. 2023 « Promptbreeder »). C'est la RCF avec population. Ce qui, en ces travaux, est rapporté comme efficace, l'est sans entraînement de l'opérateur — argument pour H_B de E1.

Lecture synthétique honnête : la conception n'est pas une famille nouvelle ; elle est l'intersection de (3) et (6) appliquée à un objet de (1)/(2). Ce qui serait nouveau et vérifiable : la génération entière comme épisode, et le transfert inter-familles mesuré sur test caché avec témoin RCF apparié en coût.

---

## (d) Point 3 : expériences décisives, en duel

Conventions : toutes les comparaisons sont à **coût total apparié**, en comptant les épisodes d'entraînement du CE comme des générations. Au moins 5 familles tenues à l'écart, ≥ 3 graines par bras, intervalle de confiance par bootstrap sur items ; seuil = différence supérieure à deux demi-largeurs d'intervalle (illustratif).

### E1 — Transfert inter-familles (l'expérience qui départage)
- H_A : le CE a extrait une régularité de conception inter-familles ; sur familles tenues à l'écart, ses conceptions à n₀ = 5 générations (illustratif) atteignent un J* ≥ celui de la RCF après N générations, N choisi tel que coût_RCF(N) = coût_CE(entraînement + n₀).
- H_B : l'avantage éventuel du CE est confiné aux familles d'entraînement ; sur familles tenues à l'écart, J*_CE ≤ J*_RCF à coût égal.
- Métrique : J* sur test caché, familles tenues à l'écart. Seuil : voir conventions.
- Témoins négatifs : (i) CE non entraîné (même architecture, même format) ; (ii) CE entraîné sur récompenses permutées entre épisodes — il doit tomber au niveau de (i), sinon le gain mesuré vient du format ou de la fuite, pas de l'apprentissage.
- Falsification : si J*_CE ≤ J*_RCF ou si le témoin (ii) égale le CE, H_A est réfutée. Si J*_CE > J*_RCF avec témoins au plancher, H_B est réfutée.
- Ce que le bras RCF apprend dans ses fichiers doit lui aussi être transféré (mémoire de lignée copiée) ; sinon on compare un CE amorti à une RCF à froid.

### E2 — Exploitation du score
- H_A : le gain du CE est réel : (J − J*) reste constant au fil de l'entraînement (pente ≤ bruit).
- H_B : le gain est une sur-optimisation : (J − J*) croît avec les pas, et J* décroît après un maximum.
- Métrique : écart J − J* par point de contrôle. Seuil : pente positive significative sur ≥ 5 points de contrôle.
- Témoin : même courbe pour la RCF au fil des générations ; témoin positif avec faille injectée dans J (fuite contrôlée de 5 % des items dev, illustratif) — le détecteur doit la voir.
- Falsification : courbe qui s'ouvre réfute H_A ; courbe plate avec témoin positif détecté réfute H_B.

### E3 — Diversité
- H_A : la population de conceptions du CE (k échantillons par contexte, k graines) a une diversité structurelle ≥ celle de k lignées RCF indépendantes.
- H_B : effondrement — diversité du CE < moitié de celle de la RCF (illustratif).
- Métrique : distance d'édition de graphe entre topologies, entropie des distributions de rôles et de modèles servis, nombre de conceptions distinctes à égalité de score.
- Témoin : CE échantillonné à température élevée (si la diversité revient avec la température, elle n'est pas apprise, elle est thermique) ; témoin planté : k copies d'une même conception doivent donner diversité 0.
- Falsification croisée évidente.

### E4 — Signalement aux humains
- H_A : le taux de signalement sur items qui le méritent (plantés : étiquettes corrompues, textes hors distribution) est stable au fil de l'entraînement du CE.
- H_B : il décroît (pente négative significative), à taux de fausses alertes constant.
- Métrique : rappel sur plantés, précision sur appariés propres. Témoin : RCF sur les mêmes plantés ; témoin mécanique : règle « désaccord entre exécuteurs > τ ⇒ signaler ».
- Falsification : décroissance réfute H_A ; stabilité avec témoin mécanique dépassé réfute H_B.

### E5 — Critique implicite dans le concepteur
- H_A : une sonde linéaire sur les activations du CE (couche à choisir sur jeu de validation) prédit J de l'épisode avant exécution avec un coefficient de corrélation supérieur à celui d'un prédicteur fondé sur les seules caractéristiques textuelles de la conception (longueur, nombre de rôles, modèles cités).
- H_B : rien de plus que le texte n'est encodé ; la sonde ne bat pas le prédicteur textuel.
- Témoin : sonde sur le CE non entraîné ; sonde sur activations permutées.
- Falsification croisée. Si H_A tient, un filtrage sans exécution est possible et réduit le coût de E1 — à re-mesurer.

### E6 — Myopie de l'épisode (point 3 de (a))
- H_A : récompenser J(ω_t) seul suffit : le CE à récompense myope égale le CE à récompense actualisée (somme de J sur 3 générations, illustratif).
- H_B : la myopie dégrade : le CE myope sacrifie les instruments A/B (coût immédiat, gain différé).
- Métrique : J* à t+3 ; taux de spécifications d'entraînement A/B émises. Témoin : RCF.

---

## (e) Instruments nommés : mesure minimale de fonctionnement

| Instrument | Ce qu'il doit détecter | Cas honnêtes appariés | Vérification mécanique à battre | Mesure minimale |
|---|---|---|---|---|
| Sondes (A) sur le 8 B | Items où l'exécuteur se trompera | Items du jeu de validation avec vérité, appariés par longueur et classe | Variance d'auto-cohérence (plusieurs échantillons), confiance déclarée | AUROC ; taux de détection à 5 % de fausses alertes (illustratif) ; doit dépasser la vérification mécanique de plus que l'intervalle bootstrap |
| Adaptateur (B) par renforcement | Gain d'exactitude sur familles tenues à l'écart | Mêmes invites, base 8 B sans adaptateur | Témoin à récompense permutée (doit être nul) ; invite améliorée sans entraînement | ΔJ* ≥ seuil ; Δ du témoin permuté ≈ 0 |
| Score scalaire J | Qu'il suit J* | Sous-ensembles dev tirés au hasard | Intervalle bootstrap de J ; corrélation J/J* par génération | Corrélation de rang ≥ 0,8 (illustratif) ; chute = instrument cassé |
| Mesure de dérive — diversité | Effondrement | k lignées indépendantes | Planté : copies identiques (détection attendue 100 %) ; population honnête variée (fausses alertes attendues 0) | Comptage mécanique (distance de graphe) ; aucun juge-modèle |
| Mesure de dérive — sur-ajustement | Ouverture de J − J* | Générations honnêtes | Planté : fuite contrôlée d'items dev | Détection de la fuite plantée ; fausses alertes sur honnêtes < 5 % (illustratif) |
| Mesure de dérive — signalement | Baisse du rappel sur plantés | Items propres appariés | Règle de désaccord entre exécuteurs | Rappel/précision par génération ; tendance |
| Bras apparié sans apprentissage | Que la différence vient de l'apprentissage | Même organisme, mémoire, budget | Réplication sur ≥ 3 graines | Écart RCF vs bras figé, puis CE vs RCF, jamais CE vs figé seul |
| Concepteur (CE) lui-même | Qu'il conçoit mieux qu'un prior | CE non entraîné ; CE à récompense permutée | Opérateur de frontière figé à une génération | Taux de victoire par paire de contextes, avec les deux témoins au plancher |

Point d'intégrité : aucune de ces mesures ne doit employer un modèle de frontière comme juge ; la vérité connue d'entraînement et les plantés suffisent.

---

## (f) Ancrage matériel (tout illustratif, aucun fait joint)

- **Concepteur** : modèle à poids ouverts de 7–14 milliards de paramètres (familles Qwen2.5 ou Llama 3 — existence RAPPORTÉE, versions exactes à vérifier), adaptateur de faible rang pour l'entraînement, format de sortie contraint par grammaire pour que Ω_CE = Ω_RCF autant que possible (point 5 de (a)).
- **Algorithme** : gradient de politique avec avantage par groupe (k = 4 conceptions par contexte, illustratif), ou, moins cher, itération d'experts : collecter les générations de la RCF, garder les 20 % meilleures (illustratif), affiner par imitation, puis renforcement court. Cette variante brouille la dichotomie et doit être un bras à part.
- **Épisodes** : 2 000 à 5 000 (illustratif). Coût d'une génération = appels de frontière + recherche documentaire + entraînement éventuel d'une sonde sur le 8 B : 5 à 50 $ (illustratif). Total épisodes : 10 k$ à 250 k$ (illustratif). C'est le poste dominant ; le calcul du RL sur 7–14 B (une machine à 8 accélérateurs de classe H100, quelques jours — illustratif, ~5 k$) est marginal devant lui.
- **Bras RCF apparié** : même budget total converti en générations ; même familles tenues à l'écart ; mémoire transférée.
- **Volume minimal de familles** : ≥ 15 à l'entraînement, ≥ 5 tenues à l'écart (illustratif), sinon E1 n'a pas de puissance.
- **Réduction de coût possible** : si E5 réussit, filtrer les conceptions par la sonde avant exécution ; sinon, réduire le jeu de développement par épisode au prix d'un J plus bruité (à remesurer en E2).

---

## (g) Point 4 : références (toutes « à vérifier » ; aucun identifiant)

- Hu, Lu, Clune (2024), « Automated Design of Agentic Systems » — à vérifier.
- Zhang, Hu, Lu, Lange, Clune (2025), « Darwin Gödel Machine: Open-Ended Evolution of Self-Improving Agents » — à vérifier.
- Yin et al. (2024), « Gödel Agent: A Self-Referential Agent Framework for Recursive Self-Improvement » — à vérifier.
- Zhang et al. (2024), « AFlow: Automating Agentic Workflow Generation » — à vérifier.
- Zhuang et al. (2024), « GPTSwarm: Language Agents as Optimizable Graphs » — à vérifier.
- Khattab et al. (2023), « DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines » — à vérifier.
- Fernando et al. (2023), « Promptbreeder: Self-Referential Self-Improvement via Prompt Evolution » — à vérifier.
- Novikov et al. (2025), « AlphaEvolve: A coding agent for scientific and algorithmic discovery » — à vérifier.
- Ye et al. (2025), « MAS-GPT: Training LLMs to Build LLM-based Multi-Agent Systems » — à vérifier ; famille des « raisonneurs de flux » entraînés par renforcement : référence à vérifier, non attribuée.
- Ma et al. (2023), « Eureka: Human-Level Reward Design via Coding Large Language Models » — à vérifier.
- Zoph, Le (2017), « Neural Architecture Search with Reinforcement Learning » — à vérifier.
- Liu, Simonyan, Yang (2019), « DARTS: Differentiable Architecture Search » — à vérifier.
- Finn, Abbeel, Levine (2017), « Model-Agnostic Meta-Learning for Fast Adaptation of Deep Networks » — à vérifier.
- Duan et al. (2016), « RL²: Fast Reinforcement Learning via Slow Reinforcement Learning » — à vérifier.
- Oh et al. (2020), « Discovering Reinforcement Learning Algorithms » — à vérifier.
- Foerster et al. (2018), « Counterfactual Multi-Agent Policy Gradients » ; Rashid et al. (2018), « QMIX: Monotonic Value Function Factorisation for Deep Multi-Agent Reinforcement Learning » — à vérifier.
- Gao, Schulman, Hilton (2022), « Scaling Laws for Reward Model Overoptimization » — à vérifier.
- Amodei et al. (2016), « Concrete Problems in AI Safety » — à vérifier.
- DeepSeek-AI (2025), « DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning » — à vérifier.

---

## Les deux lectures, sans trancher

Lecture 1 : le CE amortit la conception, extrait une régularité inter-familles, expose un critique sondable ; il vaut la peine dès que le nombre de lignées futures dépasse le point d'équilibre et que J est robuste. Lecture 2 : le CE est une recherche d'architecture par renforcement à évaluation enfant hors de prix, partant d'un modèle plus faible que l'opérateur figé, qui trouvera les failles de J avant de trouver de la conception, et dont la RCF avec mémoire transférée fait déjà l'essentiel. E1 avec ses deux témoins et E2 départagent ; E3, E4, E6 disent à quel prix.

FIN-DE-CELLULE