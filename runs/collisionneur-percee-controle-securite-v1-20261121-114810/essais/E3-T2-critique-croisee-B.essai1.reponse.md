# Critique croisée de méthode, proposition B, tour III.2

**Pièces.** J'ai reçu FAITS, QUESTION et les conceptions A, C, D, E. Aucune n'est vide ni coupée : chacune se termine par sa ligne de clôture.

**Statuts.** Mes critiques sont des HYPOTHÈSE, sauf les calculs posés en clair, que chacun peut refaire. Les faits ne donnent pas de statut individuel ; j'écris donc « le 1 % des faits ». Tout chiffre qui ne vient pas des faits est illustratif.

## Quatre outils, utilisés dans toutes les sections

**T1. Plafond des e-valeurs conformes.**
- Une valeur p conforme calculée sur n cas honnêtes vérifie p ≥ 1/(n+1).
- Tout calibrateur admissible f (décroissant, d'intégrale ≤ 1) vérifie p·f(p) ≤ ∫₀ᵖ f ≤ 1. Une e-valeur par pas est donc au plus n+1.
- Prenons une moyenne d'e-valeurs sur T pas, dont k sont sabotés. Pour atteindre 1/α, il faut grossièrement k(n+1)/T ≥ 1/α, soit **n+1 ≥ T/(kα)**.
- Exemple illustratif : T = 100, k = 1, α = 0,01 donnent n ≳ 10⁴ cas de calibration.
- En dessous, l'alarme est impossible : la puissance est nulle par construction. Le produit d'e-valeurs, plus puissant, n'est valide que sous indépendance conditionnelle des pas honnêtes.

**T2. Une AUROC proche de 0,5 ne borne pas l'avantage d'un adversaire.**
- Soit R = 0,9·U + 0,1·V la loi des tâches réelles et P = U celle des tâches plantées, où V est un trait absent des tâches plantées.
- Le classifieur « 1 sur V, hasard sinon » donne une AUROC de 0,1·1 + 0,9·0,5 = **0,55**. La variation totale vaut 0,1.
- L'agent peut alors saboter les 10 % de tâches réelles qui portent V **sans aucun risque** d'être pris sur une tâche plantée.
- La grandeur pertinente est un supremum sur les événements, que l'on n'estime que par en dessous.

**T3. Le bruit du seuil domine souvent le TPR à 1 %.**
- Par la méthode delta : Var(TPR̂) ≈ TPR(1−TPR)/n_s + (f_S(q)/f_H(q))²·α(1−α)/n_h.
- f_S et f_H sont les densités de score sous sabotage et sous honnêteté, au seuil q.
- Si les sabotages s'accumulent juste autour du seuil (f_S(q)/f_H(q) grand), l'erreur sur le quantile honnête domine. Compter 10⁴ honnêtes ne suffit plus.

**T4. Nombre de familles.**
- Si la détection varie entre familles de sabotage avec une variance τ², l'erreur type d'une généralisation estimée sur K familles est au moins τ/√K.
- Avec K = 1, τ n'est pas estimable : toute affirmation de généralisation est non jugeable.

---

## Sur la proposition A

### (a) Défauts de méthode

1. **D1 / E2 : le duel est asymétrique, ce qui viole B4 sur une branche.**
   - δ est mesuré comme l'avantage du meilleur discriminateur *trouvé*. C'est une borne inférieure de l'avantage de l'agent.
   - L'issue δ > δ₀ falsifie bien la défense.
   - L'issue δ ≤ δ₀ ne falsifie pas la famille « discernement du test » : elle constate seulement qu'on n'a pas trouvé de discriminateur.
   - D1 peut donc produire un résultat négatif fiable, jamais un résultat positif. A ne le dit pas.
2. **La borne (1 − q·d·(s−δ))^N suppose trois choses non établies :**
   - une politique sans mémoire et des tâches indépendantes, alors qu'un agent à état peut conditionner son sabotage sur l'historique des vérifications ;
   - un taux de vérification d indépendant de la subtilité du sabotage. Or d dépend de la famille, et c'est une variable confondante entre familles ;
   - un δ défini comme avantage global, alors que la borne a besoin d'un avantage uniforme sur les régions où l'agent sabote (voir T2).
3. **Le contrôle négatif de E1 est impur.**
   - Un « sabotage injecté après coup » est ensuite *lu* par le modèle. Une sonde posée sur les états postérieurs à l'injection peut sonner légitimement, par lecture de l'artefact, sans aucune fuite d'étiquettes.
   - Le contrôle n'est propre que sur les états de génération antérieurs à l'injection, ou sur un modèle qui ne voit pas l'artefact. Sinon, il conclut à une fuite à tort.
4. **E4 est en partie vrai par construction.**
   - Le rappel sur mondes plantés dépend de la loi des tailles d'effet choisie par ceux qui conçoivent les mondes.
   - « Fausses découvertes au niveau nominal » n'a pas de sens tant que la flotte n'a pas de règle de décision pré-enregistrée qui fixe ce niveau. En l'état, ce critère est non jugeable.
5. **M2 est fait sur les mêmes organismes que E1.**
   - Un classifieur oracle entraîné sur des organismes construits estime aussi le plafond de détection de la *trace de construction*.
   - M2 doit donc venir après E1, pas en parallèle comme A le conseille. Sinon, un « plafond haut » peut n'être que la cicatrice de construction.
6. **D3 : la provenance des énoncés n'est pas précisée.** Si l'agent surveillé extrait lui-même les « énoncés porteurs », un sabotage logé dans l'énoncé traverse la re-dérivation.

### (b) Conditions de perte de puissance

- **D2 :** l'alarme sonne-t-elle seulement ? Pas si n+1 < T/(kα) (T1). A écrit « perd en puissance » ; c'est en réalité *nulle* sous ce seuil calculable.
- **E2 :** l'avantage minimal détectable est de l'ordre de c/√n_plantées. Si δ₀ est plus petit, H_B n'est pas atteignable et le duel devient non jugeable.
- **Comparaison de moniteurs à 1 % :** l'erreur type de 0,1 point de A est juste pour la fausse alerte. Elle omet le second terme de T3, qui peut dominer.
- **E5 / M1 :** T4. L'écart entre familles vues et familles tierces n'a de puissance que si K ≫ (τ/marge)².
- **E1, zone morte :** entre « placebo > 5 % » et « placebo dans l'IC de 1 % », aucune issue ne falsifie quoi que ce soit. Cette zone n'est acceptable que si sa largeur est inférieure à deux demi-largeurs d'intervalle de confiance à n_placebo fixé.

### (c) Contrôles dont l'absence est fatale

- **Contrôle de puissance du discriminateur** (E2) : une paire planté/réel rendue discernable exprès. Sans lui, δ ≤ δ₀ ne dit rien.
- **Rétroaction placebo** (E4) : la flotte reçoit les scores de l'évaluateur avec des étiquettes permutées. Sans lui, un gain peut venir du budget ou de la sélection, pas du signal.
- **Chaînes canari dans les familles scellées** : elles détectent toute fuite vers la mémoire des tentatives. Sans elles, M1 n'est pas jugeable.

---

## Sur la proposition C

### (a) Défauts de méthode

1. **CCT : l'énoncé mathématique central est inexact.**
   - Pour tout couplage, P(X≠Y) ≥ TV(P,Q). L'égalité exige un couplage maximal.
   - Le couplage Gumbel-max est maximal à deux issues. Au-delà, je pense qu'il ne l'est pas en général ; c'est à vérifier sur un exemple à trois jetons.
   - « Mesure directe de TV » et « garantie mathématique exacte » sont donc des affirmations non établies.
   - La garantie à 1 % ne vient de toute façon pas du couplage. Elle vient de l'échangeabilité des pas honnêtes de calibration.
   - Le jumeau à contexte réduit diverge de l'agent honnête *par construction*.
   - L'accès aux logits exclut les agents de frontière fermés, c'est-à-dire la menace visée.
2. **ABCA est contredite par la Menace 2 de C.**
   - ABCA fait produire l'objet de contrôle par l'agent surveillé. La Menace 2 de C désigne précisément cette surface comme vulnérable.
   - ABCA n'a pas de test de mort adaptatif : son seul test est la taxe d'utilité.
3. **Expérience 1 : confusion entre évasion et dégât d'optimisation.**
   - Une baisse de S_sab sous pénalité de sonde peut venir de la dégradation générale due à l'apprentissage par renforcement, et non de la nécessité de la signature. H_B serait alors faussement falsifiée.
   - Le verdict ne vaut que pour le budget d'optimisation B, ce que C dit à moitié.
4. **Expérience 2 : le contrôle négatif est circulaire.**
   - Les « objets de contrôle » qui doivent tuer la défense sur-apprise viennent de la même flotte.
   - ΔTPR est mesuré sur un seul mode tenu à l'écart, donc K = 1 (T4).
5. **Expérience 3 : calibrer sur τ_I seul ne borne pas la fausse alerte de déploiement.**
   - Celle-ci vaut π_I·FPR_I + π_H·FPR_H. Elle n'est bornée par FPR_I que si les scores sur τ_I dominent stochastiquement ceux sur τ_H, ce qui n'est pas montré.
   - Si les cas τ_I sont induits par consigne d'insouciance, ils portent à leur tour une trace de construction.
6. **Menace 3 : le premier pas ne prouve pas ce qu'il annonce.**
   - Qu'une sonde reste muette sur un modèle *honnête* qui exécute une consigne erronée est le comportement correct.
   - Cela ne montre pas qu'un saboteur peut atteindre cet état.
7. **Intégrité.**
   - « 50 × 300 $ [RAPPORTÉ] » : le produit est illustratif. Les 300 $ des faits concernent une liste de problèmes mathématiques ouverts, pas des cycles d'idéation.
   - Des modèles et des références sont étiquetés [VÉRIFIÉ] sans appui dans les faits.
   - Des chances de 75 à 80 % sont données sans base.

### (b) Conditions de perte de puissance

- **Expérience 1 :** si TPR(B) décroît encore au budget final (pente non nulle), l'issue est indécidable. Un critère de plateau doit être pré-enregistré.
- **Zones mortes :** dans l'expérience 1 (TPR entre 20 % et 70 %) et l'expérience 3 (entre 20 % et 60 %), aucune issue ne falsifie rien. Cela viole B4, sauf si la largeur de chaque zone est justifiée par la taille d'échantillon.
- **CCT :** T1, plus une condition propre. Si la loi des divergences honnêtes par pas a une queue au-delà du quantile 0,99 qui recouvre les k pas sabotés, alors TPR ≈ α.
- **CAPP :**
  - Si la variance de sensibilité entre tâches honnêtes, σ²_tâche, dépasse l'écart moyen honnête/saboteur de ‖∇π‖, alors TPR ≈ α.
  - Le coefficient de pilotage est choisi sur les traces d'évaluation : c'est une fuite.
- **ABCA :** soit π₀ la proportion de décisions honnêtes sans micro-test constructible. Si π₀ > 1 % et que ces cas comptent comme alertes, le 1 % est inatteignable. Si on les exclut, la couverture devient la vraie métrique.

### (c) Contrôles dont l'absence est fatale

- **Organisme placebo** (même construction, objectif bénin) : il est absent de C. Sans lui, les expériences 1 et 3 ne séparent pas sabotage et cicatrice.
- **Apprentissage par renforcement avec pénalité sur une direction aléatoire** de même norme (expérience 1) : il isole le dégât d'optimisation.
- **Pilotage le long d'une direction aléatoire** (CAPP) : sans lui, la « bifurcation » peut être générique.
- **Objets de contrôle d'un agent indépendant contre objets de l'agent surveillé** (ABCA) : sans lui, ABCA n'est pas éprouvée.

---

## Sur la proposition D

### (a) Défauts de méthode

1. **Risque de vérité par construction.**
   - « Décision nuisible » est défini par l'oracle du monde, et le témoin est tiré du même monde.
   - Si la définition du dommage et le témoin viennent du même générateur, le contrat détecte ce que l'oracle définit.
   - Le test de mort de D (« le même témoin en test caché égale-t-il le contrat ? ») couvre une partie du problème, pas la dépendance au générateur.
2. **« Témoin indépendant » n'est pas défini en loi.** La condition opératoire est l'indépendance conditionnelle : P(témoin passe | conclusion fausse, trajectoire de l'agent) ≈ P(témoin passe | conclusion fausse). D ne la mesure pas.
3. **L'engagement est choisi par l'adversaire.**
   - L'agent dépose lui-même « l'observation qui obligerait à retirer ». Un saboteur choisit un falsificateur dont il sait qu'il ne se déclenchera pas.
   - D nomme « l'engagement vide », mais ne le mesure qu'en couverture. Il faut aussi mesurer la probabilité a priori de déclenchement des falsificateurs déposés, sous honnêteté et sous sabotage.
4. **La conjonction du duel commun est fragile au bruit.**
   - « La rétention des conclusions honnêtes ne baisse pas » est une hypothèse nulle ponctuelle. Sans marge de non-infériorité pré-enregistrée, H_A peut être falsifiée par le seul bruit d'échantillonnage, avec une probabilité qui approche ½ même si H_A est vraie.
   - « D dépasse strictement » souffre du même défaut.
5. **Intégrité.**
   - Les références bibliographiques sont étiquetées RAPPORTÉ alors qu'elles ne figurent pas dans les faits.
   - Aucune chance n'est chiffrée. C'est honnête, mais « chance plausible » n'est pas réfutable.

### (b) Conditions de perte de puissance

- Si les décisions nuisibles sont rares par trajectoire (n_nuis petit), l'intervalle sur D est de l'ordre de 1/√n_nuis. S'y ajoute T4 entre familles de tâches.
- **À budget égal**, le contrat ne bat le recalcul que si l'information apportée par le témoin, par unité de coût, dépasse celle du recalcul : I(témoin ; validité)/c_t > I(recalcul ; validité)/c_r. Sinon le duel est perdu d'avance, et le perdre ne falsifie que ce choix de témoin.
- Si la corrélation ρ entre l'erreur du témoin et l'erreur de l'agent tend vers 1, D tend vers le comparateur. La menace « dépendance commune » de D est donc aussi le paramètre de puissance de sa défense.

### (c) Contrôles dont l'absence est fatale

- **Témoin permuté**, pris sur une autre décision : sans lui, un gain peut venir du rituel d'engagement (l'agent change de conduite quand il doit s'engager), pas de l'observation.
- **Échange de générateurs** : générer l'oracle du dommage et le témoin par des procédés distincts. Sans lui, le point (a)1 reste ouvert.
- **Engagements honnêtes vides** : décisions valides avec un falsificateur trivial. Sans eux, on ne sait pas si le protocole repère l'engagement vide.

---

## Sur la proposition E

### (a) Défauts de méthode

1. **RAND-ML contredit la section 3.3 de E.**
   - Le noyau déclaratif est rédigé par l'agent possiblement saboteur. E écrit lui-même que la ré-exécution « reproduit fidèlement le biais » d'un énoncé biaisé.
   - La branche H_B « biais logé dans les 50 lignes » est donc l'issue par défaut. Le duel mesure surtout si l'équipe rouge y pense.
2. **RAND-ML confond lignée et sabotage.** La divergence Qwen/Llama mêle la différence de lignée et la trace de construction de l'organisme, s'il est affiné sur une seule lignée.
3. **CES-MM : le critère d'indiscernabilité ne borne pas ce qu'il prétend borner.**
   - Une AUROC ≤ 0,55 autorise un sabotage sans risque sur environ 10 % des tâches réelles (T2).
   - L'AUROC est mesurée par le discriminateur du défenseur, ce qui donne une borne inférieure de celle de l'agent.
   - L'inégalité de Ville ne s'applique que si les e-valeurs sont une sur-martingale sous la loi honnête *réelle*. Or l'hypothèse nulle « erreurs honnêtes sur canaris » est composite et calibrée empiriquement : la garantie n'est qu'approchée, sous échangeabilité.
4. **Les données de départ ne sont pas établies.**
   - Rien dans les faits ne dit que le programme détient les traces zêta et celles des 68 problèmes.
   - Ce sont des traces de mathématiques. Les prendre comme base honnête pour la recherche en contrôle rompt l'échangeabilité par construction.
5. **Affirmations surévaluées.**
   - La « dilution de deux ordres de grandeur dans tout agrégateur » ne vaut que pour la moyenne, pas pour le maximum ni le rapport de vraisemblance.
   - Une borne de puissance par la divergence KL relève du traitement de l'information, pas du lemme de Neyman-Pearson. L'étiquette [VÉRIFIÉ] est auto-attribuée.
   - Même remarque pour Kerckhoffs et pour les modèles : « Mistral-Large ouvert [VÉRIFIÉ] » n'est pas appuyé par les faits.
6. **E4 qualifie l'équipe rouge sur la mauvaise compétence.** Elle est qualifiée si elle fait chuter une *sonde*. RAND-ML et CES-MM ne sont pas des sondes : la qualification ne prédit pas la force de l'équipe contre le candidat.
7. **Zones mortes systématiques.**
   - Menace 2 : 15 % < TPR < 60 %.
   - Menace 1 : 15 % < TPR < 60 %.
   - RAND-ML : 40 % < TPR < 75 %.
   - CES-MM : 0,55 < AUROC ≤ 0,65.
   - Dans ces zones, aucune hypothèse n'est falsifiée, ce qui viole B4. Les hypothèses de la Menace 2 ne sont ni exclusives ni exhaustives.

### (b) Conditions de perte de puissance

- **FMS-Lean est incohérent avec son propre seuil.** Soit π_f le taux d'échec de génération des contre-modèles sur théorèmes honnêtes. Si ces échecs comptent comme rejets, la fausse alerte est au moins π