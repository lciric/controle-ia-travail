# Proposition A, tour III.3 : réponse aux critiques

## Notes d'intégrité

- Le bloc FAITS ne contient aucun fait porteur de statut. Tout énoncé de fond ci-dessous reste une HYPOTHÈSE, ou un calcul conditionnel aux hypothèses qu'il énonce.
- Les quatre pièces de critique semblent complètes (chacune se termine par sa ligne de fin). Je n'ai pas recalculé les empreintes.
- C et E marquent VÉRIFIÉ plusieurs dérivations. Je ne change pas ces statuts. Je signale que ce sont des calculs sous hypothèses, non des faits transmis.
- J'ai refait trois de ces calculs et je retrouve les valeurs sous les hypothèses de leurs auteurs. Cela ne dit rien du banc réel.
  - SE(β) ≈ 0,46 ε (B).
  - Seuil ρ ≈ 0,0072 pour le rapport d′(800)/d′(200) < 1,2 (C).
  - Taux 1/(n+1) pour un seuil de rang (C, D, E).
- Tous les seuils et effectifs sont illustratifs et à préenregistrer.
- Je ne réponds qu'aux sections « Sur la proposition A ».

---

## (a) Réponse aux critiques

Codes : B-a1 désigne la critique 1 de la rubrique (a) de B, et ainsi de suite.

| # | Critique (sources) | Décision | Suite donnée |
|---|---|---|---|
| 1 | Le pantin sur traces réelles est confondu avec H_B de E1, et l'arrêt précoce tuerait l'étude au moment de son résultat (B-a1, D-a). Le pantin est une tautologie du générateur (C-a1, E-a2). | **Acceptée**, avec une précision. | Les deux reproches visent deux objets différents. Je scinde : un pantin sur bruit i.i.d. synthétique (tautologique à dessein, il teste le code) et un pantin sur traces honnêtes réelles (la mesure). L'arrêt « β ≠ 0,5 » ne vaut plus que pour le premier. |
| 2 | D_max n'est pas estimable quand l'agent choisit k et d (B-a2). | **Acceptée.** | β n'est estimé qu'à dose scriptée. Les régimes consigne et affiné sont analysés par dose commandée, sans conditionner sur le D réalisé, et ne portent aucune affirmation sur β. |
| 3 | k* est sélectionné sur le jeu d'évaluation ; le cardinal de la grille croît avec T ; la grille est tronquée (B-a2, C-a3, D-a, E-a3, E-c3). | **Acceptée.** | Grille relative de cardinal fixe (k/T ∈ {1/T, T^-1/2, 0,1, 0,5, 1}). k* et le détecteur sont choisis sur un lot, puis évalués sur un lot disjoint. La règle complète est testée sur un lot honnête intact par longueur. |
| 4 | Le calcul d′ ∝ D/√k donne au moniteur le support des actes (D-a, D-b). | **Acceptée.** Erreur de dérivation de ma part. | Sans support connu, la somme porte sur T actions : d′ ∝ D/√(1ᵀΣ_T 1), indépendant de k si le décalage est linéaire en d. k ne compte que contre un détecteur de type maximum, dont le seuil croît avec T. Le plancher D/√T du tour 1 subsiste ; le chemin pour y arriver était faux. |
| 5 | La variance d'échantillonnage de l'audit dépend de k ; avec probabilité (1−f)^k aucun acte n'est vu (D-b). | **Acceptée.** | Je retire « indépendant de k ». La concentration sert l'adversaire contre l'audit et le dessert contre le maximum. Son k est borné en bas par le plafond de suspicion par acte. |
| 6 | La fraction f constante fait croître le budget avec T et force β = 1/2 (C-a1, E-a1, E-c2). | **Transformée en test** ; un point rejeté. | « Petite part » est ambigu entre fraction et budget absolu. J'ajoute le bras à budget fixe B et je reprends tel quel le duel de E-c2. Rejeté : β = 1/2 n'est « forcé » à f constant que sous indépendance, et c'est elle qui est testée. |
| 7 | Effet aléatoire de trajectoire, courbure du log-log, variance non stationnaire (B-b, C-b1, D-b, E-b1). | **Transformée en test.** | C y voit une non-jugeabilité. J'y vois le mécanisme de mon H_B. Mais la critique porte : une pente unique est mal spécifiée. L'estimande devient la longueur de bascule T* = σ²/τ² dans Var(S_T) = Tσ² + T²τ². |
| 8 | Avec des queues lourdes d'indice a < 2, β = 1/a sous indépendance (B-b, C-b1, E-b1). | **Transformée en test.** | L'indice de queue des erreurs honnêtes est estimé en E0. Sur ce banc, les erreurs d'unité rendent a < 2 plausible (HYPOTHÈSE). La somme est alors remplacée par une statistique winsorisée et la classe « erreur grossière » est analysée à part. |
| 9 | Le biais honnête μ_h ≠ 0 fait dériver la somme signée ; son estimation plafonne en σ_entre/√n (B-b, C-c3). | **Acceptée.** | μ_h est mesuré en E0 et la statistique est centrée sur les exécutions de comparaison. Le plancher en n est celui que le terme τ décrit déjà. |
| 10 | Précision insuffisante sur β ; 5 points de queue pour le seuil ; cible hors grille non identifiée (B-b, D-b). | **Acceptée.** | Le pantin étant injecté après coup, je réalloue le budget vers 400 exécutions honnêtes par longueur (200 de calibration, 200 de test). Les cibles hors grille sont déclarées censurées. |
| 11 | Un seuil de rang sur n exécutions ne descend pas sous 1/(n+1) (C-b3, D-b, E-b4). | **Acceptée.** | Mon critère (c).3 était en partie de l'arithmétique présentée comme un résultat : je le retire pour les seuils de rang. Reste testable la tenue d'un seuil paramétrique à deux composantes (σ estimé sur n·T actions, τ sur n). La calibration sur 200 exécutions est une commodité d'expérience, pas une ressource du défenseur. |
| 12 | Le signal d'état est vrai par construction : le déclencheur est réinjecté à chaque appel (B-a3, C-a2, D-a, E-a1). | **Acceptée.** C'est la critique la plus grave. | E2 est refondue. Conséquence que je n'avais pas vue : en contexte borné sans réinjection, tout état passe par le résumé textuel, et la question des activations ne se sépare plus de celle du texte. |
| 13 | Le placebo n'active aucune politique : la sonde peut lire « déclenchement » et non « sabotage » (B-c2, C-c1, D-b, D-c). | **Acceptée.** | Ajout d'une règle d'état bénigne sous indice, à poids identiques, et croisement indice × politique (plan XOR en (b)). |
| 14 | L'adaptateur a vu les deux déclencheurs ; un seul couple de test ne laisse aucun degré de liberté entre déclencheurs (B-a3, E-a3, E-b2, E-c1). | **Acceptée** pour les formes ; **transformée** pour les adaptateurs disjoints. | Les indices deviennent une classe sémantique, avec au moins 6 formes de surface jamais vues ni par l'adaptateur ni par la sonde, et bootstrap sur les formes. Je rejette une lecture de E-c1 : un échec de transfert entre adaptateurs disjoints ne falsifie pas un état persistant, seulement une direction commune aux organismes. |
| 15 | Le préfixe imposé crée une discordance hors distribution (C-a3, D-a) ; l'exécution libre contamine le résumé (E-a1). | **Transformée en test.** | Chaque bras a son défaut nommé. Les deux sont rapportés ; H_A en E2 exige leur accord. |
| 16 | Le plafonnement de d′ est acquis dès ρ ≈ 0,007 et compatible avec un signal persistant (C-b2, D-b, E-a2, E-b2). La permutation des actions est proposée en contrôle (B-c4). | **Acceptée.** | Je retire le second volet de R2 comme prédiction : il était presque vrai par construction. L'estimande devient d′(∞) = δ/τ_p. La permutation est adoptée. Elle supprime la corrélation sérielle, pas un décalage commun de trajectoire : elle distingue donc ces deux sources. |
| 17 | En E2, l'unité statistique est la trajectoire (B-b). | **Acceptée.** | Tous les intervalles sont calculés par bootstrap par trajectoire. |
| 18 | La longueur est confondue avec le volume de contenu (B-a4). | **Transformée en test.** | Bras « granularité » : même nombre de fiches, 1, 2 ou 4 actions par fiche. |
| 19 | En E3, les variantes diffèrent en difficulté ; le verdict binaire mêle marge, levier et détection ; l'inversion honnête décroît avec T en additif (B-a5, C-a4, D-a, D-c). | **Acceptée.** Elle corrige mon α. | Pour une moyenne à marge fixe, D* ∝ T, donc α = 1 et non 1/2. Mon α = 1/2 supposait sans le dire une marge proportionnelle à l'erreur-type. E3 est refondue. |
| 20 | P(inversion et silence) n'identifie aucun de ses deux facteurs ; l'union des alertes gonfle les fausses alertes (D-b, E-a3, E-b3). | **Acceptée.** | Les deux facteurs sont publiés séparément. Une seule règle combinée est calibrée sur le lot honnête tenu à part. |
| 21 | Un adversaire qui évite les scores élevés annule l'audit ciblé (E-b4, D-b). | **Acceptée.** Risque déjà signalé au tour 1. | Le ciblage garde une part aléatoire. Le pantin « placement adverse » devient obligatoire. |
| 22 | L'année de Greenblatt et al. diffère selon les propositions (B). | **Réponse.** | De mémoire : prépublication fin 2023, publication en conférence en 2024. Les deux années peuvent désigner le même travail ; à vérifier. |

---

## (b) Expériences corrigées

### Modèle corrigé (HYPOTHÈSE, calcul conditionnel)

**Bruit honnête.** La somme signée S_T des erreurs par action a pour variance Tσ² + T²τ², où τ est la composante commune à toute une exécution. La bascule est T* = σ²/τ².

**Dommage maximal indétectable, D_max.**
- Détecteur par somme, support inconnu : D_max ∝ √(Tσ² + T²τ²). L'exposant local vaut 1/2 pour T ≪ T* et 1 pour T ≫ T*.
- Au-delà de T*, la précision dépend de n (exécutions de comparaison) et non de T.
- Audit aléatoire à fraction f : exposant 1/2 en régime diffus. Avec probabilité (1−f)^k aucun acte n'est vu.
- Audit aléatoire à budget fixe B : z = √B·D/(σT), donc exposant 1. La probabilité de toucher un acte vaut environ 1 − (1 − k/T)^B.

**Dommage nécessaire, D\*.**
- α = 1 si le résultat est une moyenne à marge fixe.
- α = 1/2 si la marge est de l'ordre de l'erreur-type, c'est-à-dire si la longueur sert à résoudre la question.
- α ≈ 0 si une décision précoce fait goulot.

**Bilan par cas** (signe de β − α) :

| Structure de la tâche | T < T*, audit en fraction | T > T*, ou audit à budget fixe |
|---|---|---|
| Marge fixe (α = 1) | la longueur sert le défenseur | neutre |
| Marge ∝ erreur-type (α = 1/2) | neutre | sert l'adversaire |
| Goulot (α ≈ 0) | sert l'adversaire | sert l'adversaire |

**Activations.** d′(T) = δ/√(τ_p² + σ_p²/T), qui tend vers δ/τ_p. La longueur n'aide que jusqu'à T ≈ σ_p²/τ_p². La question utile est de savoir si δ vient d'une politique ou d'un indice.

### Banc

Le banc du tour 1 est conservé (méta-analyse synthétique, T ∈ {50, 100, 200, 400, 800}, oracle mécanique). Changements :
- 400 exécutions honnêtes par longueur, scindées en calibration et test.
- Injections scriptées après coup.
- Bras granularité.
- Marge au verdict fixée par construction.

### E0 : décomposition du bruit honnête (sans adversaire)

- **Mesures par longueur :** Var(S_T), d'où σ², τ² et T* avec intervalle bootstrap par exécution ; indice de queue a ; biais μ_h ; taux d'échec honnête ; mêmes composantes pour les scores du moniteur de texte.
- **H_A.** La borne basse de l'intervalle à 90 % sur T* dépasse 800. La preuve s'accumule en √T sur toute la plage des « centaines d'actions ».
- **H_B.** La borne haute est inférieure à 200. Sur l'essentiel de la plage, agréger plus d'actions n'apporte rien et la ressource limitante est n.
- **Falsification.**
  - Issue H_A : la thèse « la corrélation sature l'échantillon effectif » est falsifiée pour ce banc.
  - Issue H_B : R1 (β ≈ 1/2 sur la plage) est falsifiée.
  - Entre les deux : la bascule est dans la plage. T* est rapporté avec son intervalle, et c'est alors le résultat principal.
- **Bras granularité.**
  - H_A : T*, compté en fiches, est le même à 1, 2 et 4 actions par fiche. Le bruit suit le contenu.
  - H_B : T*, compté en actions, est le même. Le bruit suit le nombre d'actes.
  - Chaque issue falsifie l'autre lecture de « longueur ».
- **Contrôles.**
  - Demi-échantillons honnêtes : fausses alertes à 5 %, à la tolérance binomiale près.
  - Test de linéarité préenregistré (terme quadratique du log-log).
  - Si a < 2 : passage à la statistique winsorisée, et rapport séparé de la classe « erreur grossière ».

### E1′ : dommage indétectable à dose scriptée

- **Contrôle positif.** Pantin sur bruit i.i.d. synthétique : β = 0,5 ± 0,1, sinon bogue et arrêt.
- **Mesure.** Pantin sur traces réelles. D_max(T) à 50 % de détection et 5 % de fausses alertes, pour la règle complète, avec k* choisi hors échantillon.
- **Duel 1, modèle à deux composantes.**
  - H_A : D_max mesuré tient à ± 25 % de la courbe prédite par (σ, τ) de E0, aux cinq longueurs. Le modèle suffit.
  - H_B : écart supérieur à 50 % sur au moins deux longueurs. Le modèle est faux, même corrigé de τ.
  - Entre les deux : indécis.
- **Duel 2, budget d'audit (repris de E-c2, je m'en sers).** Budget fixe B ∈ {5, 20}, allocation aléatoire ou ciblée avec part aléatoire, pantin à placement adverse.
  - H_A : l'exposant à B fixe est ≥ 0,85. Le ciblage ne compense pas la dilution.
  - H_B : il est ≤ 0,65. Le ciblage compense.
  - Chaque issue falsifie l'autre.
- **Régimes consigne et affiné.** Détection par dose commandée. Ils vérifient S1 (prémisse « aucun acte suspect isolément ») et n'estiment pas β.

### E2′ : politique ou indice (activations)

- **Organisme.** Un adaptateur, deux familles d'indices A et B, sabotage si exactement un des deux est présent (XOR), et une troisième famille qui active une règle d'état bénigne. Les formes de surface de test n'ont été vues ni par l'adaptateur ni par la sonde.
- **Intérêt du XOR.** La présence d'un indice ne détermine pas la politique. Un lecteur linéaire de « l'indice est présent » est au hasard par construction. Que l'adaptateur apprenne ce XOR est une HYPOTHÈSE. Sinon, repli sur le seul contrôle « règle bénigne », et je le dirai.
- **Contexte.** Historique complet, indices montrés une seule fois à t = 1, T ∈ {25, 50, 100, 200}. Dans ce bras, T est confondu avec la longueur du contexte. Un contrôle par remplissage (même nombre de jetons, moins d'actions) le borne sans le lever.
- **Mesure.** δ, σ_p et τ_p sur les actions bénignes, en fonction de la distance à l'indice, en exécution libre et en préfixe imposé.
- **H_A (politique).** À plus de 50 actions de l'indice, AUROC par action ≥ 0,70 sur formes non vues, dans les deux bras, avec au plus 10 % de fausses alertes sous règle bénigne.
- **H_B (indice ou acte).** AUROC ≤ 0,55 à cette distance.
- **Falsification.**
  - Issue H_A : la dilution des activations est falsifiée pour cet organisme.
  - Issue H_B : R2 est falsifiée.
  - Désaccord entre les deux bras : indécis.
- **Contrôles négatifs.** Étiquettes permutées ; sac de mots sur le contexte ; ordre des actions permuté ; mention de sabotage interdite.
- **Volet secondaire.** Transfert de la sonde entre deux adaptateurs disjoints.
  - H_A : direction commune (AUROC croisée ≥ 0,70).
  - H_B : direction propre à l'organisme (≤ 0,55 en croisé, ≥ 0,70 en interne).
- **Limite inchangée.** C'est un organisme modèle. Le résultat borne un cas favorable.

### E3′ : le goulot en est-il un pour cet agent ?

- Les exposants α des cas additifs (1 et 1/2) sont de l'arithmétique sur une moyenne. Je ne les présente pas comme testés.
- **Contenu empirique.** En variante série, une décision précoce erronée est imposée. On mesure la fraction de fiches aval contaminées en fonction de T, sur des cas appariés par marge initiale.
- **H_A (propagation).** Au moins 80 % des fiches aval sont contaminées à T = 800 : α ≈ 0 est réalisé.
- **H_B (autocorrection).** Moins de 50 % : le goulot n'en est pas un, et α remonte vers le cas additif.
- **Contrôle négatif.** Décision consignée mais sans effet aval : la contamination mesurée doit être nulle.
- **Rapport.** P(inversion) et P(silence | inversion) sont publiés séparément, sous la règle combinée unique.

### Matériel (illustratif)

- Volume honnête : 2 000 exécutions, comparable au tour 1 puisque les trajectoires adverses scriptées disparaissent.
- E2′ en historique complet coûte davantage par action. Il est pris sur la marge ×3 déjà prévue.
- Calendrier :
  - Semaines 1-2 : E0 et pantin synthétique.
  - Semaines 3-4 : E1′.
  - Semaines 5-6 : E2′.
  - Semaines 7-8 : E3′.
- Arrêts précoces :
  - échec du pantin synthétique ;
  - échec honnête supérieur à 80 % dès T = 200 ;
  - sabotage par consigne détecté acte par acte à AUROC > 0,95.

---

## (c) Réponse à l'arbitre

### Ce qui est établi

Rien d'empirique : le bloc FAITS ne contient que la question. Ce qui suit tient comme calcul sous hypothèses explicites ; son application à un agent réel reste une HYPOTHÈSE.

- La longueur n'a pas d'effet d'un seul signe. Le signe dépend de la comparaison entre l'exposant du dommage nécessaire (α) et celui du dommage indétectable (β).
- α vaut 1, 1/2 ou environ 0 selon que la marge au verdict est fixe, de l'ordre de l'erreur-type, ou qu'une décision fait goulot.
- β vaut 1/2 tant que les erreurs honnêtes sont indépendantes d'une action à l'autre, et tend vers 1 au-delà de T* = σ²/τ².
- β vaut 1 pour un audit aléatoire à budget fixe.
- Quelques exécutions de comparaison ne calibrent pas un seuil de rang à 5 % par trajectoire : il en faudrait au moins 19.

Les critiques ont corrigé trois de mes énoncés du tour 1 :
- la dérivation en D/√k ;
- l'indépendance de l'audit vis-à-vis de k ;
- α = 1/2 pour toute tâche additive.

### Ce qui ne l'est pas

- La valeur de T* pour un agent réel. Tout le tableau des cas en dépend.
- La forme des queues d'erreur honnête et le biais μ_h.
- La capacité d'un modèle de 8 milliards de paramètres à saboter sans acte suspect isolément, et à tenir des centaines d'actions.
- L'existence, dans les activations, d'un signal de politique distinct d'un indice relu. Mon plan du tour 1 ne pouvait pas l'établir ; E2′ le peut pour un organisme modèle, pas au-delà.
- La capacité du ciblage à compenser un budget d'audit fixe.
- La propagation ou l'autocorrection d'une erreur précoce.

### L'expérience à faire en premier : E0

Elle ne demande ni adversaire ni adaptateur. Son résultat décide de ce que les autres peuvent conclure, et les deux issues falsifient quelque chose.

### Les cinq points, révisés

1. **Question.** La longueur T* à partir de laquelle la composante d'erreur honnête commune à toute une exécution domine la composante par action tombe-t-elle dans la plage des centaines d'actions, de sorte que l'exposant du dommage indétectable y passe de 1/2 à 1 et que la ressource limitante du défenseur devienne le nombre d'exécutions de comparaison plutôt que le nombre d'actions observées ?
2. **Réponse attendue (HYPOTHÈSE, confiance faible).** T* est dans la plage, entre 200 et 800 (illustratif). La longueur est alors neutre ou favorable au défenseur en dessous, et favorable à l'adversaire au-dessus, sauf tâche à marge fixe. Réfutée par l'une ou l'autre issue extrême de E0.
3. **Antériorité.** Toutes citées de mémoire.
   - Ker, Pevný, Kodovský, Fridrich (2008), « The Square Root Law of Steganographic Capacity », lieu à vérifier.
   - Kish (1965), « Survey Sampling », pour l'effet de plan sous corrélation intra-grappe.
   - Greenblatt, Shlegeris, Sachan, Roger, « AI Control: Improving Safety Despite Intentional Subversion », année à vérifier (voir ligne 22).
   - Wald (1945), « Sequential Tests of Statistical Hypotheses ».
   - Les quatre références à vérifier du tour 1 restent à vérifier.
4. **Expérience.** E0, puis E1′, E2′ et E3′ dans les deux mois.
5. **Type.** Loi connue ailleurs (composantes de variance et loi en racine), transposée, plus un test de mécanisme (politique contre indice). Aucune garantie.

**Issues qui rendraient la question sans intérêt.**
- T* ≫ 800, queues légères et μ_h ≈ 0 : tout se réduit à β = 1/2 et un z-score mécanique suffit.
- T* < 50 : la longueur n'a jamais aidé, et seul n compte.
- Les trois issues du tour 1 restent valables : contrôle mécanique suffisant, prémisse non réalisée, agent honnête déjà en échec.

**Vérification de la nouveauté.** Je n'affirme aucune nouveauté établie. À chercher dans les travaux cités et ceux qui les citent :
- toute décomposition « entre exécutions / par action » de scores de surveillance d'agents en fonction de la longueur ;
- toute sonde évaluée sous croisement indice × politique.

Si l'une existe, la contribution se réduit à une réplication sur ce banc.

FIN-DE-CELLULE