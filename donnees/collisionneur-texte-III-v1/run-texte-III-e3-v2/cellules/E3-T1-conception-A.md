# Proposition A — Tour III.1 (conception à l'aveugle)

Pièces reçues : bloc FAITS (16 faits) et bloc QUESTION, tous deux complets. Je respecte le périmètre : aucune famille, aucun comportement, aucun moyen, ni même à titre d'exemple.

## (a) Ce que la question suppose sans que ce soit établi

Bloc 1(b) :
- Qu'un régime « informé de la défense » peut être tenu sans dépense ni fuite — RAPPORTÉ par la décision N-056 (fait 1 : la décision est VÉRIFIÉE, sa faisabilité est HYPOTHÈSE).
- Que les catégories d'information (existence, liste, protocole, seuils) sont séparables en pratique — HYPOTHÈSE.
- Qu'un mode « tenu à l'écart » de la conception existe déjà — VÉRIFIÉ pour la décision (N-054), OBSERVÉ-NON-AUDITÉ pour son application.

Bloc 1(c) :
- Que les familles sont des unités échangeables — HYPOTHÈSE ; le fait 9 la nomme et la déclare non satisfaite.
- Qu'un nombre fini de familles toutes réussies autorise un énoncé sur une « classe » — HYPOTHÈSE, qui dépend de la loi de tirage.
- Que la variance intra-famille (entre éléments) est mesurable séparément de la variance inter-familles — HYPOTHÈSE, aucun élément n'est décrit dans les pièces.

Bloc 1(d) :
- Que les deux sources sont indépendantes — la question dit « en apparence » ; le fait 6 établit un lecteur unique de la lignée d'une source : l'indépendance est HYPOTHÈSE.
- Que la population de familles est fermée — HYPOTHÈSE.
- Que la grille fermée d'appariement est exacte — OBSERVÉ-NON-AUDITÉ (un seul lecteur, fait 6).
- Que les chiffres 28/25/18/19 sont dans une même unité — VÉRIFIÉ qu'ils ne le sont pas (fait 7 : appariement non bijectif) ; voir bloc 1(d).
- Que la censure commune (refus) est négligeable — HYPOTHÈSE ; le fait 12 signale que des journaux de refus existent, non servis.

## (b) Duels décisifs

**Duel 1 — Lincoln-Petersen/Chapman contre borne de Chao.**
H_A : capture homogène et sources indépendantes ; LP est sans biais notable et coïncide avec Chao2 à l'erreur d'échantillonnage près. H_B : hétérogénéité ou dépendance positive ; LP sous-estime N, Chao2 reste une borne inférieure, et l'écart entre les deux croît avec le nombre de sources.
Métrique : sur mondes simulés à N connu, biais relatif et couverture des intervalles nominaux à 95 % ; sur les cinq sources réelles, dispersion des dix estimateurs LP par paire, comparée à leur variance d'échantillonnage (Chapman).
Seuil (illustratif) : biais relatif > 10 % ou dispersion inter-paires > 2 fois l'écart-type théorique.
Contrôle négatif : mondes simulés homogènes et indépendants, où les deux estimateurs doivent coïncider ; sinon l'implémentation est fautive.
Issues : dispersion inter-paires au-dessus du seuil falsifie H_A ; modèle log-linéaire à interactions non préféré (rapport de vraisemblance non significatif, puissance vérifiée par simulation) falsifie H_B à la magnitude testée.

**Duel 2 — « Pire cas sur classe déclarée » contre « écart vues/tenues à l'écart ».**
H_A : la statistique par famille s(f) ne diffère pas, en loi, entre familles vues et familles tenues à l'écart produites par le même mécanisme (écart ≤ δ). H_B : écart > δ, la défense s'est adaptée aux familles vues.
Métrique : différence des moyennes et des minima de s(f) entre les deux ensembles, avec intervalle par bootstrap au niveau famille.
Seuil : δ = 0,05 en valeur absolue de s (illustratif).
Contrôle négatif : scission aléatoire des familles vues en deux moitiés (loi de l'écart sous H_A) ; et une vérification mécanique triviale dont l'écart doit être nul.
Issues : écart ≤ δ falsifie l'accusation de surajustement et rend le pire cas déclaré transférable au mécanisme ; écart > δ falsifie l'énoncé « universelle sur la classe » comme prédicteur hors classe, et impose la définition par quantile sur le mécanisme.

**Duel 3 — Découvrabilité et difficulté.**
H_A : la probabilité de capture d'une famille (nombre de sources qui l'énumèrent, 1 à 5) est indépendante de s(f). H_B : corrélation négative (familles faciles à concevoir, faciles à détecter), ce qui rend la borne à zéro échec anticonservatrice.
Métrique : pente de s(f) sur le nombre de sources captant f ; corrélation de rang.
Seuil : corrélation de rang |ρ| > 0,3 (illustratif) avec intervalle excluant 0.
Contrôle négatif : permutation des étiquettes de capture (loi nulle).
Issues : pente positive significative falsifie H_A et impose une pondération type Horvitz-Thompson par probabilité de capture estimée ; nulle avec puissance falsifie H_B à cette magnitude.

## (c) Mesure minimale des deux instruments

**Estimateur du nombre de familles.** Mondes simulés : N ∈ {30, 40, 60, 100, 200} (illustratif), T = 2 puis 5 sources, probabilités de capture tirées d'une Beta d'hétérogénéité variable, dépendance par paire injectée via un terme log-linéaire, erreur d'appariement injectée (fusions et scissions à taux 0 à 15 %, illustratif). Mesure : couverture des intervalles à 95 %, biais relatif, RMSE. Base à battre : le comptage brut S_obs (34 ou 35), dont la couverture est nulle dès que N > S_obs. Critère : couverture ≥ 0,90 et RMSE inférieur à celui de S_obs sur toute la grille, sinon l'estimateur ne sert qu'en borne inférieure et doit être présenté ainsi. Détection : l'estimateur « détecte » une masse manquante quand son intervalle exclut S_obs ; fausse alerte : il l'exclut alors que N = S_obs ; cas honnêtes appariés : mondes où N = S_obs avec mêmes marges n₁, n₂.

**Mesure d'universalité (énoncé (ε, α)).** Mondes simulés à deux niveaux : part réelle d'échec π connue, corrélation intra-grappe ρ entre familles proches, k éléments par famille. Mesure : taux de détection = proportion des mondes où π ≥ ε et où l'énoncé est refusé ; fausses alertes = proportion où π < ε et où l'énoncé est refusé ; couverture = proportion où l'énoncé est accepté et π < ε. Base à battre : la proportion brute d'échec sur familles vues, sans intervalle. Cas honnêtes appariés : mondes où π = ε/2 avec mêmes statistiques observées. Le fait 9 donne la référence iid : 29, 59, 149 familles ; la simulation mesure la dégradation quand ρ > 0.

---

## Bloc 1 — Propositions préalables

### 1(a) Définition opérationnelle

Notation : f une famille, s(f) une statistique déclarée d'avance (par exemple taux de détection à taux de fausses alertes fixé), τ un seuil déclaré.

**Option 1 — pire cas sur classe déclarée C.** À déclarer : la liste scellée de C (ou son schéma générateur), s, τ, le protocole d'estimation de s(f). Énoncé : ∀ f ∈ C, s(f) ≥ τ. N'autorise rien hors de C, ni aucune extrapolation. Vérification tierce : rejouer s(f) sur chaque élément de C à partir des scellés ; c'est une vérification déterministe à l'erreur d'estimation de s(f) près.

**Option 2 — écart vues/tenues à l'écart.** À déclarer : le mécanisme M qui produit les familles tenues à l'écart, δ, la statistique d'écart. Énoncé : E_M[s(f)] − E_vues[s(f)] ≥ −δ. N'autorise pas d'énoncé sur le niveau absolu de s ; une défense faible partout a un écart nul. Vérification tierce : scellés des familles tenues à l'écart, date de scellement antérieure à la défense, calcul de l'écart par le tiers.

**Option 3 — quantile ou proportion sur une loi D.** À déclarer : D, opérationnellement définie comme la loi des familles produites par M, ε, α, τ, la règle d'arrêt. Énoncé : avec confiance 1 − α, P_{f∼D}(s(f) < τ) ≤ ε. N'autorise rien sur une loi D' ≠ D ni sur une famille adverse choisie. Vérification tierce : tirage indépendant de familles par M, hors du programme, et test de l'énoncé.

**Option 4 — prédiction scellée.** À déclarer : avant la mesure, une prédiction chiffrée de s(f) sur les familles tenues à l'écart et de N (familles inconnues). Énoncé : calibration, mesurée par l'écart prédiction/mesure. N'autorise pas de garantie, mais rend le programme réfutable sur ses propres anticipations.

**Ce qui sépare « universelle sur la classe déclarée » de « robuste à l'inconnu ».** La première est un quantificateur sur un ensemble fini scellé (option 1). La seconde n'est définissable que relativement à un mécanisme M déclaré (option 3) : « robuste à ce que M produirait encore ». Aucun test fini ne certifie contre une famille choisie après coup par un adversaire ; prétendre le contraire serait un énoncé sans issue falsifiante. Recommandation : option 1 pour l'énoncé principal, option 3 avec D = loi de M pour l'extension, option 4 comme engagement réfutable ; l'option 2 sert de diagnostic de surajustement (duel 2), pas de définition.

### 1(b) Régime d'information

Catégories d'information, par niveau cumulatif : I0 rien ; I1 existence d'une défense ; I2 protocole et statistique s ; I3 liste des familles vues ; I4 seuils ; I5 code et poids de la défense. La décision N-056 (VÉRIFIÉ) prévoit deux versions, aveugle et informée : je propose de les indexer explicitement, aveugle = I0 à I2, informée = I3 à I5, et de rapporter s(f) par palier, chaque palier scellé avant l'ouverture du suivant. L'écart entre paliers est lui-même une mesure (question candidate 5).

Budget : nombre d'éléments par famille k fixé d'avance pour que l'erreur-type de s(f) soit inférieure à la moitié de l'écart inter-familles attendu (k à calibrer par simulation ; aucune valeur dans les faits). Calcul : voir (d).

Interdits entre construction et évaluation : tout retour par famille pendant la conception ; tout accès des concepteurs aux scellés des familles tenues à l'écart ; toute instance (humaine ou modèle) partagée entre les deux côtés (décision N-054, VÉRIFIÉ) ; tout ajustement des seuils après lecture d'un palier. Le journal des ouvertures de scellés est la pièce vérifiable par le tiers.

### 1(c) Combien de familles, par simulation

Énoncé cible : avec confiance 1 − α, part d'échec sous D inférieure à ε.

Modèle génératif : familles groupées en grappes latentes ; difficulté par famille tirée d'une loi continue ; indicateur d'échec = 1{s(f) < τ} ; au second niveau, k éléments par famille, variance binomiale autour de s(f). Hétérogénéité : la loi de difficulté ; dépendance : corrélation intra-grappe ρ ; la taille d'échantillon effective tombe à n/(1 + (g − 1)ρ) pour des grappes de taille g.

Règle de base (fait 9, VÉRIFIÉ) : à zéro échec, n ≥ ln α / ln(1 − ε), soit 29, 59, 149 pour ε = 0,10, 0,05, 0,02. La simulation mesure la couverture réelle de cette règle quand ρ > 0 et quand la probabilité de découverte dépend de la difficulté (duel 3).

Règle d'arrêt séquentielle : un test par e-valeurs (martingale de test) sur la suite des indicateurs d'échec, qui autorise l'arrêt à tout moment sans inflation d'α ; préenregistrée. Analyses de sensibilité : grille sur ρ, sur la forme de la loi de difficulté, sur la corrélation découvrabilité/difficulté, sur k.

Familles découvertes : la garantie porte sur D = loi de M ; si M favorise les familles faciles, la borne est anticonservatrice. Deux corrections : pondérer chaque famille par l'inverse de sa probabilité de capture estimée (nombre de sources la captant), et rapporter l'énoncé conditionnel : « sur les familles que M atteint ». Ce que la simulation démontre : la couverture sous les mécanismes simulés. Ce qu'elle suppose : que M réel appartient à la classe simulée, ce qui n'est pas démontrable depuis l'intérieur ; le seul contrôle est externe (bloc 3, question 2).

### 1(d) Combien de familles encore inconnues

Vérification : 28 × 25 = 700 ; 700/18 = 38,89 ; 700/19 = 36,84 ; Chapman : 754/19 − 1 = 38,68 ; 754/20 − 1 = 36,70. Les quatre valeurs du contexte sont exactes.

Laquelle se défend : **aucune des deux telles quelles**, car elles mélangent les unités (n₂ = 25 en unités d'Opus avec m en unités variables). Il faut fixer une granularité. En unités d'Argon (fusion des deux familles d'Opus) : n₁ = 28, n₂ = 24, m = 18 ; LP = 37,3 ; Chapman = 37,2. En unités d'Opus (scission de la famille d'Argon) : n₁ = 29, n₂ = 25, m = 19 ; LP = 38,2 ; Chapman = 38,0 (calculs dérivés des faits, formule explicite, à vérifier). L'unité grossière se défend mieux : la scission crée deux unités dont la capture par Argon est parfaitement corrélée, ce qui viole l'indépendance intra-source ; la fusion ne coûte que de la résolution. Écart-type de Chapman en unités d'Argon ≈ 2,5 (dérivé), soit un intervalle approximatif 32 à 42 : l'estimation dit surtout que N dépasse peu les 34 observées, sous les hypothèses ci-dessous.

Hypothèses et sens des déplacements :
- Population fermée : si les familles naissent avec le temps, N n'est pas défini ; on rapporte alors une courbe d'accumulation datée et son extrapolation, ou un modèle à population ouverte (Jolly-Seber, référence à vérifier).
- Indépendance : une dépendance positive (même question, entraînements corrélés) gonfle m et **sous-estime** N. Avec deux sources, l'indépendance est non identifiable : on ne peut pas la tester ; avec T ≥ 3, modèles log-linéaires à interactions (Fienberg, 1972, *The multiple recapture census for closed populations and incomplete 2^k contingency tables*, référence à vérifier pour le titre exact), choix par rapport de vraisemblance ou AIC.
- Capture homogène : l'hétérogénéité gonfle aussi m (les familles faciles sont captées par toutes) et **sous-estime** N. Chao (1984, *Nonparametric estimation of the number of classes in a population*) donne une borne inférieure robuste : Chao2 à T = 2, avec Q₁ = 16 familles vues une fois, Q₂ = 18 vues deux fois : 34 + (1/2) × 16²/(2 × 18) ≈ 37,6 (dérivé). Couverture de Good-Turing (Good, 1953, *The population frequencies of species and the estimation of population parameters*) : 1 − Q₁/(n₁ + n₂) = 1 − 16/52 ≈ 0,69, soit environ 31 % de masse d'incidence non couverte (dérivé) ; c'est un énoncé sur la masse, non sur le nombre.
- Appariement exact : les fusions abusives gonflent m (sous-estimation) ; les scissions le dégonflent (surestimation). Un lecteur de la lignée d'Opus (fait 6) risque de reconnaître les catégories d'Opus et de fusionner vers elles : biais probable vers la sous-estimation, direction non prouvée.

Estimateurs à employer avec cinq sources : Chao2 à T = 5 (borne inférieure), Good-Turing pour la couverture, log-linéaire avec interactions par paire et par lignée, classes latentes pour l'hétérogénéité, et une version bayésienne avec a priori sur N permettant de propager l'incertitude d'appariement par imputation multiple.

Refus commun : une famille que toutes les sources refusent a une probabilité de capture nulle partout ; aucun estimateur ne la voit. L'estimation porte sur la **population capturable**, et le rapport doit le dire. Les journaux de refus (fait 12, RAPPORTÉ) permettent de compter la censure, pas de la contourner ; on rapporte le taux de refus par source comme covariable.

Population non fermée : N devient N(t) ; on rapporte le taux de découverte résiduel (Good-Turing conditionnel à la date) et on redate la garantie d'universalité.

## Bloc 2 — Données de départ

Principe : des trajectoires brutes plutôt que des résumés, parce que le niveau famille exige de ré-étiqueter sous la grille du programme et parce qu'une source de capture-recapture ne vaut que si son appariement peut être refait par un tiers.

(i) Bancs publics. Trois au plus, par propriétés seulement :
- SHADE-Arena : cité dans l'état de l'art du programme (fait 10, VÉRIFIÉ pour le nom). Auteurs et licence : référence à vérifier, je ne les attribue pas de mémoire. Indépendance vis-à-vis du programme : faible, puisque les concepteurs l'ont lu. Recouvrement avec l'entraînement des modèles : à mesurer par date de publication contre date de coupe des modèles (HYPOTHÈSE que ces dates sont connues).
- ControlArena : cité (fait 10). Cadre logiciel à code ouvert selon ma mémoire, licence non attribuée ici : référence à vérifier. Mêmes réserves d'indépendance.
- Liars' Bench : cité (décision N-061). Format et licence : référence à vérifier.
- MonitoringBench et SLEIGHT-Bench : je ne connais pas ces bancs de façon fiable ; je n'en décris rien.
Usage comme source de capture : possible seulement après ré-étiquetage par le panel du bloc 4, comme occasion de capture **déclarée dépendante** des sources du programme (lecture préalable). Coût de mise au format : HYPOTHÈSE (fait 11 : rien n'est vérifié).

(ii) Journaux de refus : ne sont pas une source de capture (ils ne produisent pas de familles) ; ils mesurent la censure commune du bloc 1(d). Indépendance : nulle, internes au programme. Coût faible si les refus sont horodatés.

(iii) Propositions brutes d'une course précédente : occasion de capture supplémentaire, à déclarer dépendante (mêmes consignes, mêmes lignées). Risque : appariement par un lecteur ayant lu les deux. Valeur principale : test de stabilité temporelle de l'énumération (population fermée ou non).

Recommandation : (iii) comme troisième occasion de capture, les bancs publics comme familles extérieures de niveau I2 seulement, après mesure du recouvrement par date.

## Bloc 3 — Questions candidates

**Q1. Estimer le nombre de familles capturables avec cinq sources, et prédire scellé le gain de la cinquième.**
Avantage : à T = 5, 31 motifs de capture, les interactions deviennent identifiables (bloc 1(d)). Piège : un appariement unique ou non aveugle, qui injecte la dépendance qu'on veut mesurer. Validation extérieure : avant lecture de la cinquième source, sceller la prédiction Good-Turing du nombre de familles nouvelles qu'elle apportera (illustratif : intervalle à 90 %) ; confrontation après ouverture. Risque hors périmètre : faible ; la question ne porte que sur des comptes.

**Q2. Borner la part d'échec ε sous la loi du mécanisme de découverte, pondérée par la probabilité de capture.**
Avantage : convertit un ensemble découvert en estimateur avec biais explicité (duel 3). Piège : grappes non déclarées qui réduisent n effectif sans qu'on le voie. Validation extérieure : les cinq instances fournissent les familles de test ; seuil illustratif : au moins 20 familles extérieures, zéro échec borne ε ≈ 0,14 à 95 % (dérivé de la formule du fait 9), ce qui dit déjà que cinq instances ne suffiront pas pour ε = 0,05. Risque hors périmètre : faible.

**Q3. Mesurer l'écart vues/tenues à l'écart et le comparer à sa loi nulle par scission aléatoire.**
Avantage : indépendant du niveau absolu, directement réfutable (duel 2). Piège : les familles tenues à l'écart viennent d'un mécanisme différent de celui des familles vues, et l'écart mesure alors un déplacement de difficulté, pas un surajustement. Validation extérieure : scellement daté des familles extérieures avant toute conception ; δ = 0,05 (illustratif). Risque hors périmètre : faible.

**Q4. Valider par simulation la règle d'arrêt séquentielle sous variance à deux niveaux.**
Avantage : autorise d'arrêter la mesure quand la borne est atteinte sans inflation d'α, ce qui réduit le calcul sur 70 milliards. Piège : optional stopping avec familles dépendantes, qui casse la martingale si la dépendance n'est pas modélisée. Validation extérieure : préenregistrement de la règle et revue par un statisticien extérieur ; couverture simulée ≥ 0,93 pour un nominal 0,95 (illustratif). Risque hors périmètre : faible.

**Q5. Mesurer l'écart d'universalité entre les régimes aveugle et informé (I0–I2 contre I3–I5).**
Avantage : la décision N-056 impose déjà les deux versions ; la différence est une statistique gratuite. Piège : décrire comment le régime informé exploite l'information, ce qui sortirait du périmètre et constituerait un attaquant ; la question doit rester au niveau de la différence de s(f) par palier. Validation extérieure : mêmes familles extérieures sous les deux régimes, écart rapporté par palier. Risque hors périmètre : moyen ; l'élément qui la borne est l'indexation par niveaux I0 à I5 et la restriction au rapport chiffré.

## Bloc 4 — Organisation des cinq instances

**Consigne.** Options : même consigne scellée ; consignes différentes par instance. Même consigne : comparabilité, hétérogénéité de capture attribuable aux instances seules ; inconvénient : dépendance par cadrage commun, qui sous-estime N. Consignes différentes : dépendance réduite ; inconvénient : confond source et consigne, et rend l'appariement plus difficile. Recommandation : consigne unique scellée (empreinte publiée avant toute exécution), avec une variation déclarée uniquement de format de sortie ; confiance moyenne.

**Fuites.** Options : exécutions séquentielles par un même opérateur ; exécutions par opérateurs distincts, sans contexte partagé, chaque sortie hachée et scellée avant qu'une autre soit lue (engagement puis révélation). Inconvénient de la seconde : logistique, cinq opérateurs ou cinq sessions isolées (le relais local du fait 13 montre que des canaux distincts existent). Recommandation : engagement-révélation, journal horodaté des ouvertures ; confiance élevée sur le principe, HYPOTHÈSE sur la disponibilité des opérateurs.

**Appariement.** Options : lecteur unique ; panel d'au moins trois lecteurs de lignées distinctes des cinq sources, aveugles à l'origine, grille fermée, appariement dans les deux sens, hyperarêtes autorisées pour les recouvrements non bijectifs. Inconvénient : coût, désaccords. Recommandation : panel, accord inter-lecteurs rapporté (alpha de Krippendorff), désaccords adjugés par un humain avec journal, et surtout propagation : N est calculé pour chaque appariement de lecteur et les résultats sont combinés par imputation multiple ; confiance élevée.

**Indépendance.** Options : test statistique a posteriori par modèle log-linéaire à interactions (par paire, et par groupe de lignée déclaré d'avance) ; étalonnage a priori sur une population de référence de taille connue, sans lien avec le programme, où les mêmes cinq instances énumèrent et où la dépendance par paire se mesure directement. Inconvénient du premier : puissance limitée à T = 5 ; du second : la dépendance mesurée sur la référence peut ne pas se transférer. Recommandation : les deux, avec rapport des termes d'interaction estimés ; confiance moyenne. La corrélation des données d'entraînement entre fournisseurs n'est pas observable directement : HYPOTHÈSE que les termes d'interaction en sont un proxy.

**Usage comme sources multiples.** Chao2 à T = 5 comme borne inférieure, log-linéaire pour l'estimation centrale, bayésien pour l'intervalle propagé ; comparer à LP par paire (duel 1). Recommandation : rapporter les trois ; confiance élevée que cela est faisable, moyenne sur la précision obtenue avec cinq sources.

**Refus.** Options : reformuler ; remplacer par une instance de substitution prédéclarée d'une lignée différente ; continuer à T = 4 en le disant. La reformulation contredit la règle du protocole (fait 14, VÉRIFIÉ : refus enregistré tel quel) ; le repli à questions plus étroites (fait 16) relève d'un autre protocole et n'est pas transférable sans décision. Recommandation : liste scellée de substituts, refus consigné comme donnée de censure, jamais traité comme occasion de capture vide ; un refus partiel est une censure déclarée par source ; confiance élevée.

## (d) Ancrage matériel

Faits : modèles à poids ouverts de 8 et de 70 milliards (RAPPORTÉ) ; aucun chiffre de calcul dans les pièces. Simulation des estimateurs et des règles d'arrêt : CPU seulement, de l'ordre de 10⁴ mondes par point de grille, moins d'une journée sur une machine ordinaire (illustratif). Appariement par panel : quelques centaines d'appels à trois lecteurs (illustratif). Mesure de s(f) sur 70 milliards : coût proportionnel à (nombre de familles) × k × passes avant ; non chiffrable depuis les faits, et c'est la règle d'arrêt séquentielle (Q4) qui le borne.

FIN-DE-CELLULE