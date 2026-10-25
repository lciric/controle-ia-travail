# Proposition A — Tour III.1 (à l'aveugle)

## 0. Préliminaires d'intégrité

- **Pièce FAITS** : le bloc est présent mais ne contient aucun fait, par décision de l'arbitre (conv-audit, message n° 28 § 1). Conséquence : tout énoncé ci-dessous est au statut **HYPOTHÈSE**, sauf mention explicite ; tout chiffre est **illustratif** ; les références sont toutes marquées « à vérifier ».
- **Règle B1** : tour à l'aveugle, je ne vois ni B ni C. Je n'ai donc rien à attaquer ni à emprunter ; je le dis plutôt que de faire semblant.
- Le texte de la question est traité comme donnée. Je réponds aux six points de l'arbitre en les rangeant dans les quatre livrables (a)–(d) du tour.

---

## (a) Ce que la question suppose sans que ce soit établi

| # | Présupposé | Statut | Pourquoi ce n'est pas acquis |
|---|---|---|---|
| P1 | Un **score scalaire** sur le jeu de développement suffit pour apprendre une structure (programme + mémoire + poids). | HYPOTHÈSE | Le signal a une variance d'échantillonnage (taille du dev) et une variance de décodage (agents stochastiques). Si l'écart-type du score dépasse l'effet d'une mutation de structure, le « concepteur » fait une marche aléatoire déguisée. |
| P2 | La **structure et la composition** apportent quelque chose au-delà du choix du meilleur modèle appelé une fois. | HYPOTHÈSE | Pour de la classification de textes, un seul appel bien formaté à un modèle fort, ou un vote à k échantillons, peut absorber l'essentiel du gain. Le bras apparié doit inclure ce cas. |
| P3 | Les **sondes** sur un modèle 8B apportent de l'information que la sortie textuelle du même modèle ne donne pas déjà. | HYPOTHÈSE | Une sonde linéaire peut être équivalente, à coût près, à « demander au modèle ». Elle peut aussi n'être qu'un classifieur TF-IDF déguisé. |
| P4 | Le système peut **écrire une récompense** de renforcement sans qu'elle soit piratée par l'adaptateur. | HYPOTHÈSE | Toute récompense écrite par le même acteur que celui qui l'optimise ouvre un canal Goodhart ; la question ne prévoit pas de juge indépendant. |
| P5 | La **mémoire transmise** entre générations encode des leçons de structure et non des **fuites du dev**. | HYPOTHÈSE | Une mémoire textuelle libre peut contenir des exemples du dev, des étiquettes, ou des règles sur-ajustées à ses familles. |
| P6 | « **Familles jamais vues** » est définissable et non contaminé par le pré-entraînement des agents de frontière. | HYPOTHÈSE | On ne sait pas ce qu'un modèle de frontière a vu. Seules des familles *fabriquées après le gel* du système sont défendables. |
| P7 | Le **bras apparié sans apprentissage** est réellement apparié. | HYPOTHÈSE | Apparier sur le nombre de générations ne suffit pas ; il faut apparier sur jetons, appels, calcul GPU, et sur le nombre de lectures du score dev. |
| P8 | Le **mérite** est répartissable entre éléments et entre générations. | HYPOTHÈSE | Une valeur de Shapley sur n éléments coûte 2^n évaluations ; sur T générations elle n'est pas séparable si les mutations interagissent. |
| P9 | L'auto-réécriture du **code** est exécutable sans que le système touche au score, au dev, ou au bras témoin. | HYPOTHÈSE | Question d'infrastructure (bac à sable, droits), non de méthode ; elle conditionne tout le reste. |
| P10 | Lire le score dev à chaque génération ne détruit pas sa validité statistique. | HYPOTHÈSE | Lecture adaptative répétée d'un même jeu : problème connu (cf. « reusable holdout », réf. à vérifier en §6). |

---

## Point 1 — Formalisation de l'apprentissage de génération en génération

**Espace de recherche** (HYPOTHÈSE de modélisation). Une structure est un tuple
s = (G, r, m, a, μ, b, θ_A, θ_B) où :
- G = (V, E) graphe orienté des échanges (V = agents, E = messages), r : V → R rôles, m : V → M modèle servant chaque rôle (M = {frontière₁, …, 8B, 8B+LoRA, sonde}) ;
- a règle d'agrégation (vote, pondération, juge, sonde-arbitre) ;
- μ ∈ Σ* mémoire textuelle transmise ;
- b ∈ simplexe |V|+2 : parts de budget (agents, sondes, LoRA) ;
- θ_A poids des sondes, θ_B poids de l'adaptateur.

Le sous-espace (G, r, m, a, b) est discret-combinatoire ; μ est un espace de chaînes ; θ_A, θ_B sont continus.

**Actions.** À la génération t, le concepteur produit s_{t+1} = π(h_t), où h_t = {(s_k, J_dev(s_k), traces_k)}_{k≤t}. Trois niveaux imbriqués :
1. *Interne* (gradient) : θ_A, θ_B appris sur les données d'entraînement à structure fixe.
2. *Intermédiaire* (programme) : mutation de (G, r, m, a, μ, b) par le système ou par un concepteur.
3. *Externe* (méta) : paramètres φ du concepteur π_φ, éventuellement entraînés par renforcement sur des épisodes qui sont chacun une trajectoire s_0 → s_T.

**Signal.** J_dev(s) = moyenne du score sur N_dev tâches, variable aléatoire de variance σ²/N_dev + σ²_décodage. L'objectif réel est J_test(s_T) sur des familles non vues ; le signal disponible est J_dev. L'écart J_dev − J_test est la quantité à borner (point 5).

**Horizon.** T générations par épisode ; E épisodes pour le niveau externe. Le niveau externe est un bandit contextuel à récompense très parcimonieuse : une récompense (ou un vecteur de T différences ΔJ) par épisode.

**Ce qui est appris, par qui.**

| Variante | Apprend | Reste figé |
|---|---|---|
| C0 : concepteur figé (modèle de frontière sollicité) | programme, μ, θ_A, θ_B | φ, modèles de base, scoreur |
| C1 : concepteur entraîné | idem + φ | modèles de base, scoreur |
| C2 : le système lui-même (un de ses agents est le concepteur) | idem, avec φ = m(concepteur) | idem |

C2 pose un problème de circularité : l'agent qui réécrit le système est évalué par le score que sa réécriture influence ; il doit être exclu de l'accès au scoreur et au dev brut (P9).

**Répartition du mérite** (objets nommés) :
- Entre éléments à t fixé : ablation leave-one-out Δ_v = J(s) − J(s ∖ v), et pour les paires, interactions Δ_{uv} ; la valeur de Shapley complète n'est faisable que pour |V| ≤ 5 environ (32 évaluations).
- Entre générations : contrefactuel « mutation du concepteur contre mutation aléatoire » à partir du même s_{t−1}, répété R fois ; le mérite de la génération t est E[J(s_t)] − E[J(mut_aléa(s_{t−1}))]. Ceci est aussi le contrôle négatif central (E1 ci-dessous).
- Entre instruments et structure : évaluer s avec θ_A, θ_B remis à zéro (sondes aléatoires, LoRA nul).

---

## Point 2 et livrable (c) — Conception des instruments et mesure minimale

### (A) Sondes

- **Données** : activations h_ℓ(x) du 8B sur les textes d'entraînement étiquetés ; pool des jetons (dernier jeton, moyenne, ou jeton de réponse après une invite fixe) — le choix du pool est une variable à balayer.
- **Architectures** : (i) linéaire w·h + b ; (ii) MLP à une couche cachée. On commence par (i) : si (ii) ne bat pas (i) de plus que la variance, (i) suffit.
- **Pertes** : entropie croisée pour la classe cible ; variante utile : sonde d'**abstention**, entraînée à prédire « le système va se tromper » (étiquette = erreur observée du système sur l'entraînement), ce qui donne à l'agrégateur un signal de confiance calibré.
- **Couche** : balayage ℓ ∈ {ℓ/4, ℓ/2, 3ℓ/4, ℓ} ; sélection sur une validation *interne à l'entraînement*, jamais sur le dev.
- **Contrôles** : (c1) étiquettes permutées → la sonde doit tomber au hasard ; (c2) modèle à poids réinitialisés → mesure ce que l'architecture seule explique ; (c3) **tâche de contrôle** avec étiquettes aléatoires fixes par type de texte (Hewitt & Liang, réf. à vérifier) → la *sélectivité* = précision(tâche) − précision(contrôle).
- **Mesure minimale** : sur des familles tenues à l'écart, appariées en classe et en longueur avec l'entraînement : rappel par classe (taux de détection), taux de faux positifs, ECE (calibration), coût par exemple (un passage avant, pas de génération).
- **Vérifications mécaniques à battre** : (m1) classe majoritaire ; (m2) TF-IDF + régression logistique ; (m3) plongement de phrases + régression logistique ; (m4) le 8B lui-même en zéro-coup et en k-coups, à coût apparié. Si la sonde ne dépasse pas (m2) et (m4) d'au moins deux écarts-types bootstrap sur les familles non vues, elle n'apporte rien au système.

### (B) Adaptateur LoRA par renforcement

- **Récompenses candidates** : (r1) binaire = exactitude sur l'étiquette connue ; (r2) règle de score écrite par le concepteur (p. ex. exactitude + format + justification courte) ; (r3) collective = part de la réussite du système entier dans laquelle l'adaptateur est un agent ; (r4) signalement = prime à déclarer « incertain / problème » sur des cas plantés.
- **Algorithmes** : REINFORCE avec base de groupe (type GRPO, réf. à vérifier), PPO, ou préférences hors ligne (DPO, réf. à vérifier) construites à partir des paires correct/incorrect. Pour de la classification à étiquettes connues, le concurrent mécanique évident est l'**affinage supervisé** (entropie croisée sur l'étiquette) : si le renforcement ne bat pas le SFT à données égales, l'étage RL ne sert qu'à la récompense (r2–r4).
- **Données** : milliers de tâches d'entraînement ; échantillonnage par groupe (G = 8 réponses par tâche, illustratif) ; jamais de tâche dev.
- **Mesure minimale** : exactitude sur familles non vues contre (m4) et contre le SFT ; **corrélation entre récompense écrite et exactitude vraie** sur un échantillon audité (si ρ chute au fil de l'entraînement, c'est le signe de Goodhart) ; pour (r3) et (r4), le rappel de signalement sur un jeu planté (cas ambigus ou invalides à vérité connue), suivi génération par génération.
- **Ce que chacun apporte** : (A) un classifieur rapide et calibré utilisable comme arbitre ou filtre ; (B) un agent moins cher qu'un appel de frontière, spécialisé au domaine. Les deux ne valent que s'ils améliorent J sur familles non vues *à budget apparié*, ce qui est l'objet de E3 et E4.

### Le concepteur comme instrument

- **Taux de détection** : part des générations où la mutation proposée améliore J sur une validation tenue à l'écart (pas seulement le dev).
- **Fausses alertes** : part des mutations acceptées sur le dev qui dégradent la validation.
- **Mécanique à battre** : (m5) mutation aléatoire + acceptation si meilleure ; (m6) recherche par grille ou bandit sur un espace discret réduit (point 3, V2).
- **Mesure préalable** : écart-type test–retest du score dev (re-décodage et ré-échantillonnage) ; le seuil d'acceptation d'une mutation doit dépasser 2σ, sinon on sélectionne du bruit.

---

## (b) Expériences décisives (B4 : duels H_A / H_B)

Toutes les métriques sont sur familles tenues à l'écart ; IC par bootstrap apparié sur les familles (unité d'inférence = famille, pas l'exemple) ; seuils **illustratifs**.

**E1 — La structure apprise vaut-elle plus que le bras apparié ?**
- H_A : après T générations, J_held(s_T) − J_held(témoin) > 0, le témoin étant un vote à k échantillons du même modèle fort, apparié en jetons et appels.
- H_B : Δ ≤ 0, ou Δ > 0 sur dev seulement.
- Métrique : Δ exactitude macro ; seuil : borne inférieure de l'IC 95 % > 0 sur ≥ 5 familles non vues.
- Contrôle négatif : concepteur nourri d'un score **permuté** (marche aléatoire) ; il ne doit pas battre le témoin.
- Falsification : Δ_dev > 0 et Δ_held ≤ 0 falsifie H_A (mémorisation, P5) ; le contrôle permuté qui égale le concepteur falsifie P1 (le signal n'est pas utilisé) ; Δ_held > 0 avec contrôle au niveau du témoin falsifie H_B.

**E2 — Concepteur entraîné (C1) contre concepteur figé (C0).**
- H_A : à budget d'épisodes égal, C1 atteint un J_held supérieur à C0 d'au moins δ.
- H_B : C1 ≤ C0 + δ.
- Contrôle négatif : C1 entraîné avec récompenses mélangées entre épisodes.
- Falsification : H_A réfutée si C1 ne dépasse pas C0 ou si le C1-mélangé fait aussi bien (l'entraînement n'a rien appris) ; H_B réfutée si l'IC exclut 0 et que le contrôle mélangé reste au niveau de C0.

**E3 — Sondes contre vérifications mécaniques.**
- H_A : la meilleure sonde dépasse max(m2, m4) à coût apparié sur familles non vues, et sa sélectivité (c3) est positive.
- H_B : non.
- Contrôle négatif : étiquettes permutées (c1) → hasard.
- Falsification : sonde ≤ m2 réfute H_A (la sonde lit la surface) ; sonde > m2 et > m4 avec (c1) au hasard réfute H_B.

**E4 — Récompense écrite contre récompense binaire ; piratage.**
- H_A : (r2) donne un J_held supérieur à (r1) et la corrélation récompense/exactitude ρ reste > 0,8 (illustratif) jusqu'à la fin.
- H_B : (r1) ≥ (r2), ou ρ décroît sous 0,5 (Goodhart).
- Contrôle négatif : SFT sur les mêmes étiquettes ; si SFT ≥ (r1) et ≥ (r2), l'étage RL est réfuté dans son principe pour cette tâche.
- Falsification symétrique selon l'issue.

**E5 — Récompense collective et signalement aux humains.**
- H_A : sous (r3), le rappel de signalement sur le jeu planté baisse de plus de 10 points (illustratif) entre la génération 1 et T.
- H_B : il ne baisse pas (reste dans l'IC de la génération 1).
- Contrôle : même système sous (r1) seulement.
- Falsification : une baisse sous (r3) et non sous (r1) réfute H_B ; aucune baisse sous (r3) réfute H_A (au moins à cet horizon et ce jeu planté).

**E6 — Mémorisation contre généralisation (point 5).**
- H_A : le gain Δ_held persiste sur des familles **fabriquées après le gel** de s_T, et aucun n-gramme long de μ ne recouvre le held-out.
- H_B : le gain disparaît sur les familles post-gel, ou μ contient des fuites.
- Contrôle : système identique dont μ est vidée à chaque génération.
- Falsification : gain post-gel nul réfute H_A ; gain post-gel conservé et recouvrement nul réfutent H_B.

**E7 — Fidélité des évaluations réduites (pour les voies moins chères).**
- H_A : le classement de 20 structures sur 20 % du dev a un ρ de Spearman > 0,7 (illustratif) avec le classement sur le dev complet.
- H_B : ρ ≤ 0,7.
- Contrôle : classement sur 20 % tiré deux fois (test–retest).
- Falsification : ρ faible réfute l'usage du dev réduit comme proxy ; ρ élevé réfute l'obligation d'évaluer en entier.

---

## Point 3 — Voies moins chères (six voies distinctes, coûts illustratifs)

Hypothèses de chiffrage communes (illustratives) : N_dev = 300 tâches ; k = 5 appels par tâche ; 2 000 jetons par appel ; prix mélangé de frontière 5 $/M jetons ; une génération évaluée en entier ≈ 3 M jetons ≈ 15 $ ; une heure de GPU de classe H100 ≈ 3 $.

| Voie | Principe | Ce qui est appris | Coût (illustratif) | Ce qu'on perd |
|---|---|---|---|---|
| V1. Concepteur figé, code libre | Un modèle de frontière propose des mutations de code ; acceptation sur dev | programme, μ | T = 50 gén. × (15 $ éval + 2 $ concepteur) ≈ 10³ $ par exécution ; ×10 graines ≈ 10⁴ $ | aucun apprentissage de φ ; dépendance au modèle de frontière et à son biais de proposition |
| V2. Espace discret + bandit | Structure paramétrée à la main (≤ 10⁴ configurations : topologies, agrégations, modèles, budgets) ; bandit ou halving successif | (G, r, m, a, b) seulement | ≈ 200 configurations évaluées en halving ≈ 10³ $ | ouverture du code ; rôles nouveaux impossibles |
| V3. Structure fixe, prompts compilés | Topologie choisie, seuls les prompts et les k-coups optimisés (type DSPy, réf. à vérifier) | contenu des rôles | ≈ 10² – 10³ $ | la structure elle-même |
| V4. Mémoire seule | Tout fixe sauf μ : leçons textuelles réécrites par génération | μ | ≈ 15 $ par génération, 10² – 10³ $ au total | composition, instruments ; risque P5 maximal |
| V5. Instruments seuls | 1 agent 8B + sonde + LoRA (r1) ; structure fixe | θ_A, θ_B | sonde : < 1 h GPU ; LoRA RL : 10 – 50 h GPU ≈ 10² $ | tout l'apprentissage structurel |
| V6. Distillation du concepteur | Journaux des mutations acceptées de V1 → SFT d'un concepteur 8B–32B ; puis RL court | φ (par imitation) | V1 + 10 – 100 h GPU ≈ 10⁴ $ | on n'apprend que ce que le concepteur de frontière savait déjà ; pas de découverte |
| V7. Agents de substitution | Recherche avec agents 8B, bascule vers la frontière à la fin | programme, μ | ≈ 1/20 de V1 en jetons | hypothèse de transfert 8B → frontière, à tester (variante d'E7) |

**Ce qui les départagerait** : E1 appliquée à chaque voie avec le même témoin et le même held-out ; E7 pour V7 (transfert de classement) ; E6 pour V4 (mémoire = fuite ?). Une voie qui ne bat pas le témoin sur familles post-gel est écartée, quel que soit son coût.

---

## Point 4 — Voie chère : concepteur à poids ouverts entraîné par renforcement

Hypothèses (illustratives, raisonnement explicite) :
- Concepteur : modèle ouvert 32 B – 70 B, affiné par LoRA ou complet.
- Épisode = T = 20 générations ; chaque génération = une évaluation dev complète par des agents de frontière (15 $) + génération du concepteur (≈ 1 $ sur GPU propre) + entraînement des instruments quand le concepteur le demande.
- Instruments par génération : sonde ≈ 0,1 h GPU ; LoRA RL ≈ 20 h GPU si demandé ; supposons une demande sur quatre générations → ≈ 5 h GPU par génération en moyenne ≈ 15 $.
- Coût d'un épisode ≈ 20 × (15 + 1 + 15) ≈ 600 $ ; avec jeu planté et validation interne (×1,3) ≈ 800 $.
- Nombre d'épisodes : une récompense scalaire par épisode, espace d'actions = programmes ; par analogie avec le renforcement sur des tâches à récompense rare, E ≈ 2 000 – 10 000 épisodes pour voir un signal (illustratif, non justifié par un fait).
- Total API : 2 000 × 800 ≈ 1,6 M$ ; 10 000 × 800 ≈ 8 M$.
- Calcul du concepteur : 70 B en RL, 8 – 16 GPU H100 pendant 2 – 6 semaines ≈ 3 000 – 15 000 h GPU ≈ 10⁴ – 5·10⁴ $. **Le poste dominant est l'évaluation par des agents de frontière, pas le gradient du concepteur.**
- Ordre de grandeur total : 10⁶ – 10⁷ $ (illustratif).

**Ce qui le ferait baisser** (chacun testable) :
1. Récompense dense : ΔJ à chaque génération au lieu d'un scalaire par épisode (divise E par un facteur ≈ T, hypothèse).
2. Agents 8B pendant l'entraînement du concepteur, frontière seulement en validation (V7, divise le coût API par ≈ 20, sous réserve d'E7).
3. Halving successif sur le dev (E7) : ≈ ÷ 5.
4. Cache des sous-appels identiques entre structures voisines.
5. Réutilisation hors politique des épisodes (préférences entre paires de trajectoires plutôt que RL en ligne).
6. T plus court (10 générations) : ÷ 2, au prix de structures moins mûres.

Composées, ces réductions ramènent (illustratif) à 10⁴ – 10⁵ $, soit l'ordre de V6 ; la question devient alors E2 : ce concepteur entraîné bat-il le concepteur figé ?

---

## Point 5 — Généralisation et dérives : protocole

**Partition des familles.** F_dev (vues, score lu à chaque génération) ; F_val (jamais lues par le concepteur, lues par l'expérimentateur pour la détection de dérive) ; F_held (scellées, lues une fois à la fin) ; F_post (fabriquées après le gel de s_T, à partir d'un générateur de tâches non consulté auparavant). Seule F_post répond à P6.

**Bras apparié gelé.** Fixé avant le départ : modèle fort, vote à k, mêmes jetons et appels que la moyenne de s_T, mêmes données d'entraînement accessibles pour SFT. Préenregistré avec seuils.

**Bornes.** IC bootstrap apparié au niveau des familles ; correction de Holm sur les familles ; borne sur le sur-ajustement adaptatif : avec T lectures du dev, l'écart attendu J_dev − J_val croît avec T ; la mesurer empiriquement (courbe de l'écart en fonction de t) et arrêter quand l'écart dépasse 2σ.

**Dérives à mesurer pendant l'apprentissage** (toutes au statut HYPOTHÈSE quant à leur pertinence) :
- *Effondrement de la diversité des rôles* : entropie de la distribution des plongements des descriptions de rôles, et nombre de rôles distincts effectivement sollicités (ablation Δ_v ≠ 0) ; alerte si l'entropie chute de plus de 50 % (illustratif) sans gain sur F_val.
- *Sur-ajustement au dev* : J_dev − J_val par génération.
- *Exploitation du score* : rescorage d'un échantillon par un juge indépendant (humain ou scoreur alternatif) ; divergence entre score et jugement indépendant ; cas typique : la structure apprend le format que le scoreur récompense.
- *Signalements qui baissent* : rappel sur le jeu planté (E5), suivi par génération, sous chaque régime de récompense.
- *Fuite par la mémoire* : recouvrement de n-grammes (n ≥ 8, illustratif) entre μ et F_val/F_held.
- *Concentration du budget* : évolution de b ; si tout le budget va à un seul agent de frontière, la « structure » a convergé vers le témoin et E1 doit alors donner Δ ≈ 0.

---

## Point 6 — Ce qui est connu (toutes « à vérifier »)

Aucun identifiant donné de mémoire ; auteurs/année/titre tels que je crois pouvoir les attribuer.

- Alain & Bengio, 2016, « Understanding intermediate layers using linear classifier probes » — à vérifier.
- Hewitt & Liang, 2019, « Designing and interpreting probes with control tasks » — à vérifier.
- Belinkov, 2022, « Probing classifiers: promises, shortcomings, and advances » — à vérifier.
- Hu et al., 2021/2022, « LoRA: Low-rank adaptation of large language models » — à vérifier.
- Schulman et al., 2017, « Proximal policy optimization algorithms » — à vérifier.
- Rafailov et al., 2023, « Direct preference optimization: your language model is secretly a reward model » — à vérifier.
- Shao et al., 2024, « DeepSeekMath » (origine de GRPO) — à vérifier.
- Skalse, Howe, Krasheninnikov & Krueger, 2022, « Defining and characterizing reward hacking » — à vérifier.
- Manheim & Garrabrant, 2018, « Categorizing variants of Goodhart's law » — à vérifier.
- Dwork, Feldman, Hardt, Pitassi, Reingold & Roth, 2015, « The reusable holdout: preserving validity in adaptive data analysis » — à vérifier.
- Finn, Abbeel & Levine, 2017, « Model-agnostic meta-learning for fast adaptation of deep networks » — à vérifier.
- Li, Jamieson, DeSalvo, Rostamizadeh & Talwalkar, 2018, « Hyperband: a novel bandit-based approach to hyperparameter optimization » — à vérifier.
- Hu, Lu & Clune, 2024, « Automated design of agentic systems » — à vérifier.
- Zhang, Hu, Lu, Lange & Clune, 2025, « Darwin Gödel Machine: open-ended evolution of self-improving agents » — à vérifier.
- Zhuge et al., 2024, « GPTSwarm: language agents as optimizable graphs » — à vérifier.
- Khattab et al., 2023, « DSPy: compiling declarative language model calls into self-improving pipelines » — à vérifier.
- Fernando et al., 2023, « Promptbreeder: self-referential self-improvement via prompt evolution » — à vérifier.
- Yang et al., 2023, « Large language models as optimizers » — à vérifier.
- Shapley, 1953, « A value for n-person games » — à vérifier.

Aucune de ces références n'est présentée comme établissant un résultat pour le présent système ; elles situent les objets (sondes, LoRA, RL par préférences, Goodhart, holdout réutilisable, recherche automatique de structures d'agents).

---

## (d) Ancrage matériel (illustratif sauf mention)

- **Modèles ouverts** : un 8 B à poids ouverts avec accès aux activations (familles Llama 3 8B ou Qwen 2.5 7B, licence à vérifier) pour (A) et (B) ; un 32 B – 70 B ouvert pour le concepteur (C1, V6) ; agents de frontière par API pour l'évaluation.
- **Calcul** : extraction d'activations sur 10⁴ textes ≈ minutes sur 1 GPU ; sondes linéaires ≈ CPU ; LoRA RL sur 5·10³ tâches, groupe de 8, 1 – 2 époques ≈ 10 – 50 h GPU ; RL du concepteur 70 B ≈ 10³ – 10⁴ h GPU.
- **Coûts** : V1–V5 ≈ 10² – 10⁴ $ chacune ; V6 ≈ 10⁴ $ ; voie chère ≈ 10⁶ – 10⁷ $ nue, 10⁴ – 10⁵ $ avec les six réductions. Tous illustratifs ; aucun ne vient des faits (il n'y en a pas).
- **Ordre recommandé pour « réfléchir avant que les étapes 1 et 2 tournent »** : mesurer σ du score dev (préalable à tout) ; E3 et le SFT témoin de E4 (une journée GPU) ; E7 (fidélité du dev réduit) ; puis E1 sur V1 et V2 avec contrôle permuté. E2 et la voie chère n'ont de sens que si E1 donne Δ_held > 0 pour au moins une voie bon marché.

FIN-DE-CELLULE