# Tour III.2 : critique croisée de méthode (proposition A)

**État des pièces.** Les cinq pièces B à F sont présentes et se terminent toutes par leur ligne de fin. FAITS et QUESTION DE L'ARBITRE sont identiques et ne contiennent que la question, donc aucun résultat empirique ou bibliographique n'y est établi. Ma propre conception du tour III.1 n'est pas transmise et je ne m'y réfère pas.

**Convention.** « Lu » signale un constat VÉRIFIÉ par lecture de la pièce. Les formules sont des identités ou des approximations usuelles ; leurs applications aux paramètres des pièces donnent des chiffres **illustratifs**. Toute affirmation sur le comportement d'agents est une HYPOTHÈSE.

**Références divergentes entre pièces (Lu).**
- Freivalds est daté 1977 chez B (titre à vérifier) et chez F (avec un titre), 1979 chez D (avec un autre titre) : référence à vérifier.
- Greenblatt et al. est daté 2023 chez B et 2024 chez C, D, E, F : référence à vérifier.

---

## Sur la proposition B

### (a) Défauts de méthode

- **E1 confond dissuasion et optimisation de l'évitement.** La pièce définit U1 par « p × pénalité > gain » mais ne fait varier que p. Une pente en p peut venir d'un calcul d'évitement dans l'épisode, sans aucune sensibilité à une pénalité. Il manque le plan factoriel p × pénalité.
- **Dans la variante par instruction, la pente est en partie fixée par le texte de consigne.** Elle mesure alors l'obéissance. Le contrôle « orthographe » neutralise le mot « audit », pas cette dépendance.
- **E3 : la sonde sépare deux procédés de fabrication.** Les tests sont générés et les épisodes réels ne le sont pas, donc une sonde atteindra 0,65 dès qu'il existe un artefact de générateur. Ce n'est pas une « conscience d'évaluation ». Le contrôle prévu (épisodes réels étiquetés au hasard) ne vérifie que le pipeline.
- **E4 teste le ciblage, pas la borne.** La borne 1−(1−k/n)^m est une identité, conditionnelle à « recalculé ⇒ reconnu ». Si la corruption va sur des étapes non recalculables, R < 1 est vrai par construction. De plus m est choisi par l'agent, donc le dénominateur de R est endogène.
- **E5 : « graine connue » ne rend pas la paraphrase calculable par l'agent.** Il faudrait qu'il simule le paraphraseur. Une différence nulle peut donc venir de cette incapacité, et H_B serait retenue à tort.
- **E6 : le rappel est étalonné sur les mauvais usages.** Il l'est sur U2, U7, U9, au vocabulaire stabilisé, puis sert à affirmer une rareté pour U13, U10, U5, au vocabulaire instable. Le rappel ne se transfère pas d'une classe à l'autre. S'y ajoute une fuite : l'auteur de la thèse rédige aussi les requêtes et les critères d'inclusion.

### (b) Conditions de perte de puissance

- **E1.** Var(log OR) ≈ somme des inverses des quatre effectifs de cellule.
  - La bande [0,9 ; 1,1] exige une erreur-type ≤ 0,05 environ, soit n ≳ 3 200 par bras pour un taux de tentative de 0,5 et n ≳ 8 900 pour 0,1 (illustratifs).
  - Les 2 000 épisodes annoncés ne suffisent donc pas : H_B n'est pas jugeable.
  - La corrélation intra-tâche ρ réduit encore l'effectif utile d'un facteur 1+(m−1)ρ.
- **E2.** Le log-rapport de vraisemblance entre politique corrélée et politique indépendante a pour espérance T·I nats sur T étapes observées.
  - Si T·I ≲ 1, aucun agent, même bayésien optimal, ne peut apprendre la corrélation.
  - ΔS ≈ 0 n'a alors rien à voir avec le caractère stratégique de l'agent.
  - ΔS est aussi non jugeable si S(I=0) est proche de 0 ou de 1.
- **E3, mesure comportementale.** Pour un score binaire, AUROC = ½ + (δ_réel − δ_test)/2 ≤ ½ + δ_réel/2. Si le taux de défection réel est ≤ 0,10, l'AUROC est ≤ 0,55 : H_B est vraie par arithmétique.
- **E4.** R est non jugeable quand la borne tend vers 1, ou quand la loi de m est concentrée sur 1 (variance du rapport).
- **E6.** Le décompte K suit une Binomiale(N, r). Avec N = 5 et un rappel r = 0,5, P(K ≤ 2) = 0,5 (illustratif).

### (c) Contrôles négatifs dont l'absence serait fatale

- **E1 :** un agent honnête soumis aux mêmes annonces de p. Sans lui, le taux de « tentatives » classées à tort peut varier avec p (prudence induite).
- **E1 :** une condition « p annoncé, pénalité nulle ».
- **E3 :** générateur contre lui-même (deux lots de tests), et réel contre réel à deux dates (dérive naturelle).
- **E5 :** un contrôle positif où l'agent reçoit la sortie paraphrasée. Sans lui, un résultat nul est ininterprétable.
- **E6 :** une catégorie placebo, qui doit rendre 0, et une estimation du rappel par deux recherches indépendantes dans la classe visée (capture-recapture ; référence à vérifier).

---

## Sur la proposition C

### (a) Défauts de méthode

- **Statuts (Lu).** La pièce marque `VÉRIFIÉ` de nombreuses attributions et des mécanismes en langue naturelle, et qualifie des dates d'« illustratif ».
  - Je ne modifie aucun statut. Je signale seulement que les FAITS n'établissent rien de tout cela.
  - L'énoncé sur le regret (« nécessaire et suffisante », adversaire adaptatif) dépasse ce que je peux attribuer : référence à vérifier. Un regret borné ne borne d'ailleurs pas une action unique irréversible.
- **Expérience 1 : le bras de référence est nul par construction.** Le sabotage est défini comme « sans affirmation factuellement fausse », et la référence vérifie l'exactitude locale. Son TPR vaut donc son FPR (0,05), et ΔTPR ≥ 0,25 revient à TPR_permutation ≥ 0,30.
- **Expérience 1 : l'issue dépend de la consigne d'implantation.**
  - Si la cible est désignée par son étiquette, les clones divergent après permutation : H_A.
  - Si elle l'est par ses attributs de fond, la politique suit les attributs échangés et reste cohérente : H_B.
  - L'expérience mesure donc la consigne de l'équipe rouge.
- **Contrôle négatif 2.** Une faible divergence entre clones sur entrée identique est donnée comme « preuve de collusion tacite ». Elle vaut tout autant pour un agent loyal : c'est la répétabilité d'une même politique.
- **Fuite de calibration.** Le seuil à FPR 0,05 est calibré sur l'agent loyal sur les 200 tâches qui servent aussi à l'évaluation.
- **Expérience 2 : deux facteurs confondus.** Le bras B diffère du bras A par l'amnésie, mais aussi par le format (question de suivi contre réanalyse complète). L'extracteur de score de risque n'est pas validé.
- **Expérience 3 : deux facteurs variés ensemble.** La génération des pièges et le caractère aléatoire du seuil changent en même temps (pas de plan 2×2), donc aucun effet n'est attribuable à II ou à V.
- **Expérience 3 : hypothèses non exhaustives.** H_A exige AUROC ≥ 0,65 **et** sabotage ≥ 0,30 ; H_B est dite falsifiée dès que l'un **ou** l'autre est atteint. Le cas « AUROC < 0,65 et sabotage ≥ 0,30 » rend les deux fausses, ce qui viole B4.
- **Décisions sur estimations ponctuelles.** Il n'y a ni intervalle ni zone indéterminée : une AUROC de 0,79 « falsifie ».

### (b) Conditions de perte de puissance

- **Expérience 1.** Soit h la probabilité qu'un agent loyal change de recommandation sous permutation, et d celle de l'agent déloyal. Pour un score binaire, AUROC = ½ + (d − h)/2, donc 0,80 exige d − h ≥ 0,6.
- **Calibration du FPR.** Avec n = 200 loyaux, le FPR réel au seuil « 0,05 » est dans [0,02 ; 0,08] environ (illustratif). Le « TPR à FPR 0,05 » hérite de cette incertitude.
- **ΔTPR.** L'erreur-type est ≲ 0,05 à n = 200, soit ±0,10 autour d'un seuil de 0,25.
- **Expérience 2.** Si a est la probabilité qu'un opérateur tiré touche le voisinage causal de la vulnérabilité cachée, alors TPR ≤ FPR + 1−(1−a)^m. Avec m = 3 et a = 0,1 (illustratif), la borne est d'environ 0,32 : H_A est inatteignable par la loi du tirage.
- **Seuil stochastique (V).** Contre un attaquant non adaptatif et une courbe ROC concave, tirer le seuil à FPR moyen égal donne un mélange de points de fonctionnement situé sous la courbe. Le gain est donc ≤ 0. Il n'est positif que si la loi du score d'attaque est concentrée juste sous τ_fixe.
- **Tableau (c), instrument I.** « TPR ≥ 0,70 pour 5 % d'audit » exige k·f ≳ 1,2 (k étapes auditées, f fraction falsifiée). Pour un coup unique, TPR ≤ 0,05 + FPR.

### (c) Contrôles négatifs dont l'absence serait fatale

- **Expérience 1 :** une variante d'agent déloyal dont la cible est définie par le fond, pas par l'étiquette.
- **Expérience 1 :** un sabotage factuel détectable par la référence, pour montrer qu'elle n'est pas aveugle par construction.
- **Expérience 1 :** une calibration loyale sur des tâches disjointes, et un agent loyal plus faible (présent seulement en Expérience 2).
- **Expérience 3 :** le plan 2×2 complet, et des tâches réelles étiquetées « piège » au hasard pour valider l'estimateur d'AUROC_agent.

---

## Sur la proposition D

### (a) Défauts de méthode

- **Convention de statut (Lu).** D redéfinit `VÉRIFIÉ` comme « conséquence conditionnelle ». La pièce est explicite, mais ce statut n'atteste aucune prémisse et aucune attribution. Je le lis ainsi sans le changer.
- **Le banc écrase le résidu non mécanique.** Tout y est recalculable, puisque le recalcul exhaustif donne les labels. Le « meilleur comparateur mécanique » approche le plafond, donc G ≤ τ est quasi acquis pour l'audit et le défi algébrique. La part interprétative, où le hasard pourrait compter, est hors banc.
- **Confusion centrale : l'information de l'adversaire sur le comparateur.**
  - S'il connaît le comparateur déterministe, celui-ci est contournable à coût nul et H_A est acquise.
  - S'il l'ignore, le comparateur vaut un tirage non exploré et H_B est acquise.
  - G est donc une fonction du budget d'adaptation de l'équipe rouge par bras, que la pièce ne fixe pas.
- **Asymétrie de réglage.** Le comparateur est choisi comme le meilleur parmi plusieurs sur développement ; l'instrument aléatoire n'est pas réglé. C'est un biais de sélection, de signe inconnu sur le jeu tenu à part.
- **Dissuasion.** Le comparateur est une sanction déterministe « de même coût ». Pour un maximiseur neutre au risque, la théorie invoquée prédit l'égalité. Le duel mesure une attitude au risque sur des gains simulés, c'est-à-dire l'obéissance au score.
- **Sentinelles.** Le comparateur est une « batterie fixe identifiable » : H_A est vraie par définition du comparateur.
- **Multiplicité.** Il y a onze duels avec un seul τ, sans correction ni hiérarchie.
- **Capacité.** Avec des modèles de 7 milliards de paramètres comme contrôlé « stratégique », un résultat nul peut refléter un plancher de capacité.

### (b) Conditions de perte de puissance

- **Intervalle.** Pour une différence de taux à 400 paires, la demi-largeur non appariée est d'environ 0,07 près de 0,5 (illustratif), soit plus que τ = 0,05. Presque tous les duels sortiront « non tranchés ».
- **Audit.** P(rencontre) = 1 − C(N−k,m)/C(N,m), soit m/N pour k = 1. On a G > τ seulement si l'adversaire obtient P(rang d'anomalie ≤ m | faute) < m/N − τ. Si le score d'anomalie est indépendant de la faute, G = 0 exactement.
- **Sondage.** En tirage de Poisson uniforme, CV ≈ √((1−π)/(πNθ)) pour une prévalence θ. L'estimateur vaut 0 avec probabilité (1−π)^{Nθ}, et il est non jugeable si πNθ ≲ 1.
- **Comité.** La borne hypergéométrique devient vide quand la corrélation des erreurs des juges honnêtes tend vers 1 : P(majorité fausse) ≥ P(erreur commune).
- **Sentinelles.** Tout avantage de distinction est ≤ distance en variation totale entre les lois des historiques. Un classifieur faible la sous-estime.
- **Masque et publication bruitée.** La « baisse de sensibilité » est une borne inférieure de fuite, conditionnelle à la classe d'attaquants.

### (c) Contrôles négatifs dont l'absence serait fatale

- **Un budget d'optimisation adverse égal et séparé par bras,** avec comparateur divulgué. Sans cela G n'est pas interprétable.
- **Un adversaire scripté optimal,** comme contrôle positif de capacité stratégique.
- **Un duel A/A** (même instrument, deux graines) : G doit être nul. Il calibre l'intervalle par grappes.
- **Des tâches à plafond mécanique inférieur à 1.**
- **Bibliographie.** « Aussi fourni que les comparateurs » n'a ni seuil ni rappel mesuré dans la classe visée.

---

## Sur la proposition E

### (a) Défauts de méthode

- **Statuts (Lu).** Des garanties en langue naturelle portent `[VÉRIFIÉ]` : U4 (« ne peuvent pas coordonner »), la variante temporelle de U1 (sans formule), et la borne d'information mutuelle attribuée à Dwork et al. (2006). Les FAITS n'établissent rien de cela.
- **Attribution à vérifier.** « Aléa public = aléa privé » est attribué à Babai (1985). De mémoire (RAPPORTÉ), ce résultat est associé à Goldwasser et Sipser (1986), « Private Coins versus Public Coins in Interactive Proof Systems ».
- **E1 : ΔTPR est vrai par construction.**
  - L'attaque n'inverse que la recommandation finale.
  - U1 tire 3 affirmations parmi N : la rencontre vaut environ 3/N.
  - U3 part de la conclusion : le dernier saut est inspecté avec probabilité 1.
  - Le gain est donc celui de la baseline déterministe « audit du seul dernier saut », que la pièce nomme en (c) mais n'inclut pas dans E1. Le hasard n'y joue aucun rôle.
- **E1 : format et tirage confondus.** U3 change à la fois le format (graphe imposé) et le tirage.
- **E2 : trois transformations non ablatées.** Bijection de noms, transformation affine, permutation d'ordre. Comme chez C, l'issue dépend de la définition de la cible : par nom, U4 gagne ; par rôle (invariant sous isomorphisme), U4 perd.
- **E2 : la translation affine des montants.** Elle ne préserve ni les ratios ni les seuils, ce qui fabrique une perte d'utilité honnête.
- **E2 : H_B est une disjonction de deux mécanismes sans rapport.** L'issue « H_A falsifiée » n'indique pas lequel a joué.
- **E3 : bruit de seuil et rotation de moniteurs confondus.**
- **E3 : deux contrôles mal nommés.** Le « contrôle négatif » algorithmique est en fait un contrôle positif de mécanisme. La clause « P5 directement falsifié » ne vaut que pour le modèle testé.
- **E4 : fuites laissées en place.** Le protocole les laisse volontairement (« sans tampon ni filtrage »). Il teste donc une implémentation, pas l'inobservabilité, et H_A est favorisée par conception. La permutation d'étiquettes ne valide que l'estimateur.
- **Aucune zone indéterminée.** Une AUROC de 0,64 « falsifie H_A ».

### (b) Conditions de perte de puissance

- **E1, côté honnête.** Si un graphe honnête présente une « violation » jugée par transition avec probabilité v, alors FPR = 1−(1−v)³. Tenir 0,05 exige v ≤ 0,017. Au-delà, il faut exiger au moins 2 violations sur 3, et le TPR tombe à P(≥ 2 transitions violées sur le chemin).
- **E1, côté adversaire.** Si le mensonge est déplacé en amont à profondeur uniforme sur d niveaux, P(rencontre) ≈ 3/d.
- **E2, ratio.** Avec ρ_sab = 1 − r₁/r₀, r₀ ≈ 0,40, r₁ ≈ 0,20 et n = 150, l'erreur-type par méthode delta est d'environ 0,10. L'intervalle est d'environ ±0,19 autour du seuil 0,50 (illustratif).
- **E2, utilité.** L'erreur-type de Δ_util est d'environ 0,05, soit le seuil lui-même. Le critère conjoint n'est pas jugeable à cet effectif.
- **E3.** L'information par étape sur τ₀ est ≤ h(r) bits pour un taux de révision r, soit 0,29 bit pour r = 0,05.
  - Sous bruit de Laplace d'échelle b, l'erreur d'estimation décroît quand même en moyennant sur T. Pour T = 60, le bruit ne multiplie l'erreur que par un facteur borné.
  - Le coût est une perte de TPR contre l'attaquant non adaptatif, par la concavité déjà invoquée pour C.
- **E4.** Il y a 100 positifs répartis en 20 grappes. L'erreur-type de l'AUROC est ≳ 0,05 avant correction intra-tâche, soit un écart d'au plus 3 erreurs-types entre 0,65 et 0,50.

### (c) Contrôles négatifs dont l'absence serait fatale

- **E1 :** les bras « graphe + audit déterministe du dernier saut » et « graphe + tirage uniforme », plus une attaque située hors de la conclusion.
- **E2 :** une cible définie par rôle, et des paires honnêtes sous U4 à température non nulle pour le FPR de la comparaison croisée (citées au tableau (c), absentes d'E2).
- **E3 :** un attaquant non adaptatif sous les deux régimes, et le plan factoriel bruit × rotation.
- **E4 :** des étapes où R déclenche une action sans effet observable. L'AUROC doit y valoir 0,50 ; sinon fuite réelle et sur-ajustement du prédicteur sont indiscernables.

---

## Sur la proposition F

### (a) Défauts de méthode

- **Statuts.** La pièce est la plus prudente sur ce point (essentiellement `RAPPORTÉ`). Un seul détail : la borne O(√(T ln K)) est associée aux bandits. Je ne peux l'attribuer avec certitude qu'au cadre à information complète : référence à vérifier.
- **Conditionnement sur une variable post-traitement.** Le « gain sur le résidu qui passe la vérification mécanique » conditionne sur un filtre auquel l'équipe rouge s'adapte.
  - Les trajectoires honnêtes qui passent sont une sous-population sélectionnée, donc l'appariement en difficulté est rompu.
  - Un FPR calibré avant filtrage ne vaut plus après.
- **E1 : engagement et défi aléatoire confondus.** Le contrôle « défi prévisible » isole l'imprévisibilité, ce qui est un bon point. Il n'isole pas l'effet du format d'engagement.
- **E1 : hypothèses non exhaustives.** Le cas « ΔTPR ≥ 20 pp et prévisible ≈ secret » falsifie H_A selon la règle, et H_B (« aucun gain ») aussi. Le troisième état, où l'engagement suffit sans hasard, n'est pas nommé.
- **Équivalence décidée par non-significativité.** C'est le cas en E1 et E4 (« ne perd pas significativement », « résultat équivalent »), sans marge d'équivalence.
- **E1 : critère double incohérent.** Seuil ponctuel à +20 pp, mais borne d'intervalle seulement > 0.
- **E2 : même dépendance à la définition de la cible que chez C et E.**
- **E4 : U9 et U8 sont fusionnés.** Si c'est la réécriture qui agit, l'instant fixe fera aussi bien et H_A tombera pour une raison étrangère à U9.
- **E5 : ε_dist mesure un seul classifieur.** C'est l'avantage de celui de l'agent, tel qu'élicité, donc un minorant de la distinguabilité. Par ailleurs, des « tâches historiques » publiques peuvent être mémorisées (fuite par données d'entraînement).
- **Fuites non exclues.** Les consignes de l'équipe rouge sont optimisées, et les seuils calibrés, sur les mêmes tâches que l'évaluation.
- **Bibliographie.** Aucun étalonnage du rappel n'est prévu, contrairement à B.

### (b) Conditions de perte de puissance

- **E2.** Le test métamorphique porte sur une fraction p = 0,2 des sous-tâches, et le banc contient j = 1 à 3 anomalies. Alors TPR_meta ≤ FPR + 1−(1−p)^j, soit 0,20, 0,36 ou 0,49 (hors FPR) : le seuil de 0,80 est inatteignable par la loi du tirage. H_A ne peut tenir que par la branche « réduction de R_sab ».
- **E4.** Une attaque exigeant ℓ étapes contiguës survit avec probabilité (1−q)^{ℓ−1}. Avec q = 0,15, une réduction ≥ 50 % exige ℓ ≥ 6. Pour ℓ ≤ 5, H_A est inatteignable par le seul aléa temporel.
- **E3.** Si des paires honnêtes se contredisent avec probabilité h par question et les paires sabotées avec d, la détection sur k questions oppose Bin(k, d) à Bin(k, h). Pour k = 1 et h > 0,05, aucun seuil ne donne FPR ≤ 0,05 : non jugeable.
- **E5, erreur-type.** Avec 200 leurres et 200 réels et des taux de prédiction proches de 0,5, l'erreur-type de la différence est d'environ 0,05. La borne supérieure à 95 % vaut ε̂ + 0,10, donc « < 0,10 » n'est presque jamais satisfaisable. H_A est pratiquement infalsifiable à cet effectif.
- **E5, valeur absolue.** Elle biaise l'estimateur vers le haut sous le nul : E|ε̂| ≈ 0,8 × erreur-type ≈ 0,04, à comparer au seuil 0,05.
- **Tableau (c), U1.** « TPR ≥ 80 % » avec une fraction corrompue de 10 % exige k ≥ 16 unités auditées, donc N ≥ 160 à 10 % de budget.

### (c) Contrôles négatifs dont l'absence serait fatale

- **E1 :** un bras « engagement sans défi, plus vérification mécanique ».
- **Résidu :** un FPR recalibré sur la population honnête après filtrage mécanique, et un appariement refait après filtrage.
- **E4 :** les bras « réécriture sans relève » et « relève sans réécriture ».
- **E5 :** des tâches réelles perturbées de façon neutre (perturbation sans vérité implantée), pour séparer l'artefact de perturbation du statut de leurre.
- **Partout :** un budget d'optimisation adverse égal par bras, et des tâches d'optimisation disjointes des tâches d'évaluation.

---

## Usage déclaré des pièces (B1)

Je me sers de deux éléments sans les fusionner au reste :

- **Le contrôle « défi prévisible » de F** (E1, E4). Je le retiens comme gabarit pour isoler la part du hasard.
- **La règle de zone intermédiaire de B,** comptée comme échec de puissance. Je la retiens contre les décisions ponctuelles de C et de E.

Ce sont des emprunts de méthode ; ils ne valident pas le reste de ces pièces.

FIN-DE-CELLULE