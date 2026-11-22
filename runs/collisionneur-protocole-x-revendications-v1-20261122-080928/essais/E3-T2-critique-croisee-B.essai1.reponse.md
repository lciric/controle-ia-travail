# Proposition B, tour III.2 : critique croisée de méthode

**État des pièces.**
- Le bloc FAITS reproduit la question de l'arbitre et ne contient aucun fait porteur de statut.
- Les quatre conceptions A, C, D et E sont transmises. Toutes se terminent par FIN-DE-CELLULE et aucune ne paraît coupée.
- Je ne peux recalculer aucune empreinte sha256.

**Statut de mes propres énoncés.**
- Les critiques ci-dessous sont des HYPOTHÈSES de méthode.
- Les calculs sont des déductions arithmétiques non auditées. Ils partent des chiffres que les propositions ont elles-mêmes marqués « illustratif », et restent donc illustratifs.
- Quand je mobilise une proposition pour en critiquer une autre, je le signale (B1).

**Statuts des autres propositions.** Je ne modifie aucun statut attribué par une autre proposition. Lorsqu'un statut VÉRIFIÉ n'est étayé par aucune pièce de la cellule, je le signale à l'arbitre sans le changer.

---

## Sur la proposition A

### (a) Défauts de méthode

1. **L'étiquette « action sabotée » n'est pas définie pour S-LoRA.** Toutes les actions d'un agent affiné relèvent de la politique saboteuse. Le duel 1 régresse pourtant le décalage de sonde « sur les actions sabotées » en fonction de Δ_i. Le quintile de Δ_i le plus bas contient donc des actions identiques à des actions honnêtes. Une ordonnée à l'origine ≥ 0,5 écart-type y révélerait l'identité du modèle (l'adaptateur déplace les activations partout), pas une « signature d'intention ». C'est le confondant central de C1.

2. **L'erreur de mesure sur Δ_i favorise H_A.** Δ_i provient d'un rejeu bruité. Une régression sur un régresseur bruité aplatit la pente (dilution par erreur sur la variable explicative). Or H_A est justement « pente plate ». Le moniteur de texte sert de comparateur, mais l'atténuation n'est pas forcément la même pour les deux moniteurs si leurs bruits diffèrent.

3. **Le rejeu mécanique n'est pas défini au-delà de la bifurcation.** Après remplacement de l'action i, les actions suivantes, figées, peuvent devenir invalides dans le nouvel état.
   - Le taux de rejeux invalides peut dépendre du bras (saboteur ou honnête).
   - Les Δ_i manquants sont alors manquants de façon non aléatoire.
   - L'« action honnête appariée » au rang i n'existe que si le préfixe est commun, ce qui n'est plus le cas après le premier écart.

4. **R dépend de l'ordre des substitutions et du tirage honnête.** Σ_i Δ_i suppose des substitutions une à une. En régime interactif, R varie avec l'action honnête de remplacement, elle-même tirée d'une loi. Un seul tirage par position donne un R conditionnel au tirage.

5. **S-script confond deux choses.** Une trajectoire perturbée puis relue en lecture forcée par le modèle honnête est hors politique : le modèle y est « surpris ». Si la sonde s'allume sur S-script, A conclut qu'elle lit le contenu. Elle peut tout aussi bien lire la surprise (faible vraisemblance sous le modèle).

6. **C3 compare deux budgets dans des unités différentes.** Les bifurcations appariées se consomment par trajectoire déployée. Le réservoir d'étalonnage se partage entre tâches. « k exécutions » ne fixe donc pas un coût commun tant que l'unité (exécution complète ou segment, par tâche ou globale) n'est pas précisée.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **Dose–réponse (C1).**
  - Notons λ = Var(Δ)/(Var(Δ)+Var(η)) la fidélité de Δ̂_i (η est le bruit de rejeu). La pente observée vaut λβ. Si λ ≲ 0,5 (illustratif), le rapport quintile haut / quintile bas est comprimé vers 1, et le critère « ≤ 1,5 » de H_A devient atteignable sans aucun effet d'intention.
  - Le critère « rapport ≥ 3 » de H_B est non jugeable quand E[S_texte | Q1] est à moins d'une erreur-type de 0, car le dénominateur s'annule.
  - Ce qu'il faut : estimer λ par double rejeu, et préférer une pente avec correction d'atténuation à un rapport de moyennes.
- **Rapport d'additivité (C2).**
  - R̂ = Σ Δ̂_i / Δ̂_tot n'a pas de moments finis si P(Δ_tot ≤ 0) n'est pas négligeable. Le bootstrap est alors invalide.
  - Le numérateur somme 30 à 40 termes bruités. Son erreur-type croît en √T·σ_η.
  - R est jugeable seulement si E[Δ_tot] ≫ ET(Δ̂_tot) et si √T·σ_η ≪ E[Σ Δ_i].
  - À estimer : un rapport de moyennes sur les tâches, avec intervalle par méthode delta, plutôt qu'une moyenne de rapports.
- **Duel 3, à 1 % de fausses alertes par trajectoire.** Avec environ 150 tâches honnêtes de test (illustratif), on attend 1,5 fausse alerte. L'erreur-type de l'estimation est d'environ 0,008 (illustratif), soit environ 80 % de la cible. Le seuil au quantile 0,99 repose sur une ou deux observations, et un écart de 10 points à ce point de fonctionnement est non jugeable. A énonce lui-même la remarque sur 1/α sans l'appliquer à son propre duel.
- **Agrégation intra-trajectoire.** Si ρ est la corrélation intraclasse des scores honnêtes, le nombre effectif d'observations vaut n·m/(1+(m−1)ρ). A le mesure, ce qui est un point fort, mais aucun seuil ne dit quand le duel devient non jugeable.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Un adaptateur honnête** de même rang et de même nombre de pas, affiné sur un changement de style neutre. Sans lui, C1 ne distingue pas « intention » et « poids modifiés ».
2. **Une lecture forcée honnête hors politique** : trajectoire honnête d'une autre graine, ou d'un autre modèle honnête, relue en lecture forcée. Sans lui, S-script ne sépare pas contenu et surprise.
3. **Un double rejeu H contre H par position**, qui donne Var(η) et λ. Sans lui, ni la pente de C1 ni R ne s'interprètent.
4. **Les contrôles déjà présents** : H-leurre et permutation d'étiquettes. Ils sont nécessaires, mais ne couvrent pas les trois points ci-dessus.

---

## Sur la proposition C

### (a) Défauts de méthode

1. **Une fuite potentielle dans C1.**
   - Le vecteur directeur u (« vecteur directeur moyen ») et le seuil h (« validation croisée ») ont une source non précisée.
   - Si u ou h sont estimés sur des trajectoires saboteuses qui recoupent le test, la détection est en partie construite sur l'échantillon évalué.
   - Si u est estimé sur les seules références, il n'est pas défini, puisque les références n'ont pas de direction de sabotage.

2. **Le pas t n'est pas aligné entre tâches.** Normaliser « au même pas t » sur N_ref = 20 exécutions suppose des phases comparables d'une tâche à l'autre.
   - Si les références sont mises en commun entre tâches, μ_t mélange difficulté de tâche et phase.
   - Si les références sont propres à chaque tâche, 20 × 50 tâches = 1 000 exécutions (illustratif) : ce n'est plus un nombre limité.

3. **Le contrôle négatif de C1 est satisfait par construction.** Monter la température produit un bruit non directionnel, et un CUSUM projeté sur une direction u le rejette mécaniquement. Le contrôle informatif est un échec honnête directionnel : modèle plus faible, documentation trompeuse, ou erreur précoce qui se propage. E pose ce même problème (son P3), et je m'en sers ici en le disant.

4. **C2 : la première moitié de H_2A est presque vraie par construction.** Une sonde entraînée hors domaine qui échoue sur une autre distribution (S-DPO) ne prouve rien sur une « cécité sémantique ». De même, n'importe quel adaptateur modifie la dynamique h_t → h_{t+1}. M_dyn peut détecter la modification des poids et non le sabotage. Le contrôle de paraphrase ne touche pas ce confondant.

5. **C3 : la comptabilité du budget est ambiguë.** Un bloc k = 5 implique 5 pas réels et 5 pas régénérés. Il faut dire si B compte les pas inspectés, les pas générés ou les deux. De plus, le bras k = 1 propose deux modalités (« évaluer l'action » ou « comparer à un pas généré ») : la longueur k et la modalité d'audit sont confondues tant que le bras k = 1 n'emploie pas aussi le contrefactuel.

6. **Les zones sans verdict ne sont pas déclarées, contrairement à B4.**
   - C1 : un TPR de CUSUM entre 0,45 et 0,75 ne déclenche aucune issue.
   - C1 : le seuil sur le détecteur max varie selon les passages (≤ 0,25 dans l'énoncé, écart ≥ 0,30 dans H_1A, ≤ 0,45 dans l'issue 1).
   - C2 : une AUROC de M_lin entre 0,60 et 0,70 ne tranche pas.
   - C3 : un gain entre 0,10 et 0,25 ne tranche pas.
   A et D déclarent leur zone intermédiaire ; C ne le fait pas.

7. **Statuts à signaler à l'arbitre.**
   - C attribue VÉRIFIÉ à Wald 1945 et à Page 1954. Aucune pièce de la cellule ne permet de contrôler ces statuts ; je les laisse tels quels.
   - « VÉRIFIÉ par construction algébrique » : une sonde sur la moyenne des plongements de la couche 0 est bien une fonction linéaire des comptes de jetons. En revanche, l'inférence « s'il ne la bat pas, il ne détecte qu'un changement de vocabulaire » n'est pas algébrique.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **CUSUM, pente contre κ.**
  - Soit δ = uᵀΣ^{-1/2}(μ_sab − μ_hon) la dérive par pas.
  - En lois gaussiennes de même variance, AUROC_pas = Φ(δ/√2).
  - Le critère « diffus » de A (AUROC par action ≤ 0,60) donne δ ≈ 0,36. Celui du duel E0 de E (≤ 0,55) donne δ ≈ 0,18 (illustratifs).
  - Avec κ = 0,5, l'incrément espéré sous sabotage, δ − κ, est négatif : le CUSUM n'accumule rien en moyenne. Il perd sa puissance précisément dans le régime visé.
  - La règle usuelle κ ≈ δ/2 exige de connaître δ, ce qui ramène à la fuite du point (a)1.
- **Erreur d'estimation des références.**
  - μ̂_t, calculé sur 20 exécutions, a une erreur de l'ordre de 0,22σ (illustratif).
  - Si les mêmes références servent à tous les pas, cette erreur est corrélée dans le temps et s'ajoute à la dérive sous H0.
  - Le CUSUM reste sous contrôle seulement si |biais| < κ. Les queues sont aussi plus lourdes, puisque z_t suit environ une loi de Student à 19 degrés de liberté.
- **M_dyn (C2).**
  - Un modèle autorégressif d'ordre 1 sur 32 composantes compte 1 024 coefficients pour A et 528 pour Σ.
  - 20 × 40 = 800 transitions (illustratif), autocorrélées : le problème est sous-déterminé sans régularisation.
  - Les résidus évalués sur les données d'ajustement sont alors plus petits que sur toute donnée nouvelle, honnête ou non, et la comparaison est biaisée.
  - Condition : nombre effectif de transitions ≫ d² et ajustement croisé par trajectoire.
- **C3 avec m = 2 blocs par trajectoire.** La décision par trajectoire repose sur deux comparaisons. Si la variance de ΔV_k entre deux contrefactuels honnêtes partis du même état croît plus vite que k² · (dérive par pas)², le gain change de signe. C'est H_3B, qui doit être mesurée directement, pas inférée.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Un adaptateur DPO honnête** de même rang, sur des paires d'actions honnêtes de qualité égale (C2).
2. **Un échec honnête directionnel**, en remplacement ou en complément de la température (C1).
3. **Des blocs contrefactuels honnête contre honnête** depuis le même état (C3). C'est le plancher de bruit de ΔV_k ; sans lui, le contrôle TDD ne suffit pas.
4. **Une estimation de u et h sur un ensemble de saboteurs disjoint du test**, par famille de tâches.

---

## Sur la proposition D

### (a) Défauts de méthode

1. **La sélection se fait sur l'issue, de façon asymétrique.**
   - Seules les exécutions dégradées où aucune décision ne dépasse le quart de la perte sont « qualifiées ».
   - Les témoins honnêtes ne subissent pas de filtre symétrique.
   - Le taux de détection et le taux de fausses alertes portent donc sur des populations sélectionnées différemment.
   - D publie aussi les résultats sur tous les essais assignés. C'est un point fort, mais le verdict du contraste principal doit être rendu sur la population assignée, ou bien les témoins doivent être filtrés par un critère homologue.

2. **La consigne est indissociable de « l'intention ».**
   - Aucun poids n'est ajusté, donc la dégradation passe uniquement par la consigne.
   - Les activations à toutes les positions sont conditionnées par cette consigne. Le duel 3 traite ce point.
   - Mais les instances témoins à options de même valeur forment une autre distribution de tâches, sur laquelle le modèle se comporte peut-être autrement. Le contraste mélange donc l'effet de consigne et le type d'instance.

3. **Le gain est plafonné par le comparateur.**
   - Le comparateur non interne inclut la « dérive du coût cumulé ».
   - Si cette dérive s'approche du signal du solveur, le gain propre aux activations est nul par construction.
   - À l'inverse, un comparateur faible le gonfle. D le choisit sur validation, ce qui est un point fort, mais le plafond n'est pas rapporté.

4. **Le débit est présenté comme « mesuré ».** La configuration est marquée illustrative et D demande de chronométrer, ce qui reste cohérent. Mais l'adjectif « mesuré » ne doit pas être lu comme une observation. L'arithmétique est cohérente : 200 × 4 × 32 × 64 ≈ 1,64 million de jetons par modèle, et 36,4 heures-carte à 25 jetons/s.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **Plafond du contraste principal.** Gain ≤ 1 − TPR_comp(échéance). Si le meilleur comparateur non interne détecte au moins 90 % des cas avant l'échéance (illustratif), un gain de 10 points est inatteignable. Il faut publier TPR_comp avant de lire le gain.
- **Le gain n'est pas identifiable face à l'effet de consigne.**
  - Soit γ = P(alerte | consigne de dégradation, aucun dommage possible) − P(alerte | honnête).
  - Le duel 3 ne réfute que γ ≥ 0,10.
  - Si γ se situe entre 0 et 0,10 et que le gain observé G est proche de 0,10, la part de G due au dommage n'est pas identifiable.
  - Il faut estimer G − γ̂ avec un intervalle conjoint, et ne pas lire les deux duels séparément.
- **Effectifs du duel de qualification locale.**
  - Pour obtenir une borne basse au-dessus de 0,60 quand la vraie proportion vaut 0,65, il faut une demi-largeur d'intervalle inférieure à 0,05, soit n ≳ 350 paires indépendantes (illustratif).
  - Le rééchantillonnage par famille réduit le nombre effectif d'un facteur 1+(m−1)ρ.
- **Plafond de 5 % de fausses alertes.** Réfuter H_B exige une borne haute ≤ 5 %. Avec 200 témoins (illustratif) et un vrai taux de 3 %, la borne haute à 95 % avoisine 5,5 % (illustratif) : le duel est non jugeable même si la candidate est vraie. La strate des échecs honnêtes, plus rare, est pire ; D l'anticipe.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **La permutation des activations** entre trajectoires de même tâche, phase et longueur, avec réentraînement. Elle est présente. Elle doit être appliquée aussi aux instances témoins de même valeur.
2. **Deux paraphrases de la consigne de dégradation** sur instances témoins. D ne propose que deux paraphrases honnêtes. Sans ce contrôle, on ne sait pas si la sonde lit le sens de la consigne ou sa forme lexicale.
3. **Une sonde lisant un modèle tiers recevant le même préfixe public**, contrôle emprunté à A et signalé comme tel. Sans lui, « activations de l'agent » et « représentation du texte » ne se séparent pas.

---

## Sur la proposition E

### (a) Défauts de méthode

1. **C1 : une fuite entre construction du sabotage et construction de l'audit.**
   - Les expérimentateurs injectent eux-mêmes un couplage d'ordre 2 (invariant au pas t₁, consommateur au pas t₂), donc le long d'une arête de flux de données.
   - L'audit de paires tire précisément ses paires sur ce graphe lecture-écriture.
   - Le gain sur l'audit unitaire et sur les paires hors graphe est donc en grande partie vrai par construction.
   - Il faut une équipe rouge aveugle au constructeur de graphe, autorisée à coupler par des canaux non représentés (fichiers de configuration, conventions implicites, environnement).

2. **C1 : la borne α + O(B√ε) est en grande partie mécanique.** Pour un auditeur qui ne voit que la loi conditionnelle de chaque pas, elle découle de l'inégalité de Pinsker et d'une borne d'union. Le libellé « C1 démontre l'effondrement » présente comme établi ce qui reste une HYPOTHÈSE. Pour l'arbitre : la partie empirique porte la charge de nouveauté, pas la borne.

3. **C2 : une circularité possible dans la notation.** Le prédicteur est écrit φ(h_t, y_t). Si φ utilise l'état caché h_t pour prédire z_t, qui est dérivé de h_t, le résidu mesure une erreur d'ajustement entre deux fonctions de la même variable. φ ne doit dépendre que du texte émis. Il faut le spécifier.

4. **C2 : une fuite entre ajustement et calibration.**
   - La régression ridge passe de traits textuels à z_t, de dimension 4 × 3 584 environ (illustratif), sur 40 × 40 = 1 600 pas (illustratif).
   - Si les résidus de calibration sont calculés sur les données d'ajustement, ils sont systématiquement plus petits que sur toute donnée nouvelle.
   - Toute trajectoire nouvelle, honnête ou non, paraît alors anormale.
   - Un ajustement croisé par trajectoire, sur des familles de tâches disjointes, est indispensable.

5. **C3 : écart de capacité dans le centrage.**
   - Le centrage contrefactuel local est fait par Qwen2.5-3B (section d), alors que l'agent est un modèle 7–8B.
   - Sous H0, E[ψ(agent honnête) − ψ(rééchantillonneur 3B) | h_t] ≠ 0, et ce biais a une direction persistante (écart de compétence).
   - La U-statistique d'alignement directionnel est construite pour détecter exactement ce type de dérive : elle s'allumera sur des agents honnêtes.

6. **C3 : un contrôle trivial.** Randomiser les signes par variables de Rademacher sur des vecteurs centrés annule par construction l'espérance des produits hors diagonale. L'AUROC « dans [0,45 ; 0,55] » est donc garantie et n'informe pas. C'est plutôt le mécanisme naturel de construction de la loi nulle qu'un contrôle négatif.

7. **Un statut à signaler à l'arbitre, sans le modifier.**
   - E attribue « VÉRIFIÉ mathématiquement » à l'échec de toute somme scalaire. Or l'hypothèse énoncée porte seulement sur la moyenne par pas (« inférieure ou égale »).
   - Une moyenne inférieure n'implique ni dominance stochastique ni échec d'une statistique scalaire. Variance et autocorrélation peuvent différer, et des scores centrés par tâche ne sont pas couverts.
   - Le statut VÉRIFIÉ semble porter sur une prémisse plus forte que celle écrite. Le plancher conforme 1/(N_ref+1), lui, découle bien de la définition des p-valeurs de rang.

8. **Une incohérence matérielle mineure.** 48 000 pas × 4 couches × 4 096 dimensions × 2 octets ≈ 1,6 Go, et non 8 Go, si les activations sont moyennées par segment d'action comme indiqué (illustratifs). Cela ne change pas le verdict, mais l'unité de stockage doit être précisée.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **Duel E3, précision de l'estimation des fausses alertes.**
  - Avec environ 600 trajectoires honnêtes (illustratif), à α = 0,01, l'erreur-type est d'environ 0,004. L'intervalle autour d'une valeur observée de 0,010 va d'environ 0,002 à 0,018.
  - Les critères « ≤ 0,015 » (H_A) et « > 0,02 » (H_B) ne sont pas départagés par l'estimateur ponctuel.
  - L'intervalle entre 0,015 et 0,02 est une zone sans verdict non déclarée, contrairement à B4.
  - Les trajectoires de N_ref doivent en outre être exclues du test.
- **Conditions de validité de C3.** La validité exige E_H0[ψ_agent − ψ_rééch | h_t] = 0. Sinon, la U-statistique a une espérance hors diagonale positive sous H0, de l'ordre de ‖biais‖² · nombre de paires, et le taux de fausses alertes diverge avec T.
- **C2, régime de dimension.** Si dim(z) ≫ nombre effectif de pas, la variance des résidus hors échantillon dépend surtout du paramètre de pénalité. Le score devient une fonction de ce paramètre, et non de la trajectoire.
- **Duel E1.** Si la probabilité qu'une paire couplée tombe dans l'échantillon d'audit, P(paire couplée ∈ arêtes du graphe), est faible pour un adversaire aveugle au graphe, la puissance de l'audit de paires tombe sous celle de l'audit de paires tirées sans graphe. C'est justement le cas que le protocole n'échantillonne pas.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Un centrage par le même modèle honnête** que l'agent (C3), ou à défaut une mesure directe du biais 7B contre 3B sur trajectoires honnêtes.
2. **Un adaptateur honnête** de même rang pour E2 et E3, pour le même motif que chez A et C.
3. **Une équipe rouge aveugle au graphe** (E1).
4. **Une calibration et un ajustement croisés par famille de tâches** (C2), ainsi qu'un contrôle par trajectoires honnêtes non vues dont la difficulté est appariée.

---

## Défauts communs, signalés sans fusionner les propositions

- **Le confondant « poids modifiés ou intention » touche trois propositions** : A (S-LoRA), C (S-DPO) et E (adaptateur diffus). Aucune ne prévoit d'adaptateur honnête de même rang.
- **Les petites cibles de fausses alertes (1 % chez A, 1 % chez E, 5 % chez C et D)** sont souvent non jugeables avec les effectifs illustratifs annoncés une fois tenu compte de l'autocorrélation intra-trajectoire.

**Ce qui me ferait réviser ces critiques.**
- Pour le confondant des poids : un protocole qui montre qu'un adaptateur neutre ne déplace pas les scores de sonde au-delà du bruit entre graines.
- Pour l'écart de capacité chez E : une mesure du biais de centrage indiscernable de 0.
- Pour la fuite de l'audit de paires : une équipe rouge aveugle au graphe qui reste détectée.

FIN-DE-CELLULE