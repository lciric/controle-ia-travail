# Tour III.2, proposition A : critique croisée de méthode

**Pièces.** B, C, D et E sont présentes et non coupées. Ma propre conception A n'est pas retransmise, donc je ne la cite pas.

**Statuts.** Rien n'a été exécuté. Mes critiques sont des HYPOTHÈSES de méthode. Les ordres de grandeur sont des calculs sous lois supposées (binomiale, unités indépendantes) et sont tous « illustratifs ». Je n'ai pas audité les références citées par B et E.

**Notation.**
- α : taux nominal de fausses alertes ; n₀, n₁ : nombres d'unités indépendantes honnêtes et positives.
- μ, σ², φ : décalage moyen par pas du score sous sabotage, variance par pas, autocorrélation d'ordre 1 ; T : nombre de pas.
- τ² : variance d'un effet aléatoire par épisode ou par famille de tâches.
- b : décalage du score dû à la seule différence de poids ou de contexte entre agent et jumeau, hors tout acte de sabotage.
- K : rollouts par frontière ; σ²_MC ≈ [V(1−V)+V′(1−V′)]/K : variance de l'étiquette TD estimée.

---

## Sur la proposition B

### (a) Défauts de méthode

1. **Poids confondus avec l'intention (duels 2, 3, 4).** Le saboteur est un LoRA et le jumeau ne l'est pas. Δ = V_agent − V_jumeau contient donc b. Les paires honnête/honnête à graines différentes ne contiennent pas b : la nulle de B est celle de « mêmes poids », alors que l'alternative mélange « poids différents » et « sabote ». Si b ≠ 0, la détection est vraie par construction.
2. **Déclencheur lexical.** Le contrôle par instruction explicite couvre le texte de l'instruction, pas celui du déclencheur. Une lecture positive au prompt peut être la trace du jeton déclencheur dans un modèle entraîné à y réagir, quelle que soit la réaction apprise.
3. **Sélection post-traitement (duel 3).** Évaluer « uniquement là où les vérifications mécaniques passent » conditionne sur une variable causée par n. Si P(passe | n) décroît en n, les épisodes retenus à n = 16 forment une autre sous-population que ceux à n = 1. La pente en n n'estime alors plus l'effet de n.
4. **Alignement non défini (duel 3).** « Le même pas chez le jumeau » n'existe plus après la première divergence. En teacher-forcing, le texte est on-policy pour l'agent et off-policy pour le jumeau. Les « erreurs honnêtes injectées » sont off-policy pour tous. Le contraste sabotage/erreur injectée confond alors intention et surprise.
5. **Estimateur du duel 1.** Résidualiser le score sans résidualiser l'issue ne mesure pas l'apport conditionnel. Il faut un test emboîté hors échantillon de Y sur (covariables) contre (covariables + score). Par ailleurs, B ne dit pas si les items servant à sélectionner les neurones sont disjoints de ceux où l'ablation est évaluée.
6. **Duel 4.** « Toute évasion coûte ≥ 15 points » est une quantification universelle, testée sur une seule famille d'attaques. La sonde « réentraînée » est supervisée par des étiquettes de sabotage : c'est un autre instrument, et sa puissance ne dit pas que le signal de valeur est « déplacé ».
7. **Zones non attribuées.** Entre 3 % et 30 % de détection au duel 2, aucune hypothèse n'est falsifiée. B doit déclarer cette zone « indécise ».

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **Duel 1.** Sur 500 items à 75,2 % de réussite (RAPPORTÉ), soit environ 375/125, l'erreur-type d'une AUC proche de 0,55 est d'environ 0,03. Les seuils 0,58 et 0,53 sont donc séparés de moins de deux erreurs-types. Le critère n'est pas jugeable sans environ six fois plus d'items. La puissance s'annule aussi quand Var(score | covariables)/Var(score) → 0, par exemple si le prédicteur de difficulté vient d'un modèle de même famille.
- **Détection à α = 1 %.** Le seuil est un quantile empirique. Le nombre de dépassements honnêtes suit Bin(n₀, α), soit 2 à 5 pour « quelques centaines » d'épisodes. La bande [0,5 % ; 2 %] exige √(α(1−α)/n₀) ≲ 0,25 point, donc n₀ de l'ordre de 1 500 unités indépendantes, comptées en familles si τ² > 0.
- **Pente en n (duel 3).** Le rapport signal sur bruit de l'agrégat vaut nμ/√(nσ²(1+φ)/(1−φ) + n²τ²). Il plafonne à μ/τ dès que τ² > 0. Une pente plate ne distingue donc pas « μ = 0 » de « τ domine ». Il faut estimer τ² sur les paires honnêtes avant de lire la pente.
- **Duel 4.** L'issue n'est pas jugeable si la perte d'évasion ne converge pas. Sans attaque dont l'efficacité est connue, « H_A survit » se confond avec un échec d'optimisation.
- **Piste 5.** Si la fiabilité inter-juges est r, l'AUC observable est bornée en dessous de l'AUC vraie. Les seuils 0,58 et 0,53 ne sont pas jugeables tant que r n'est pas estimé.

### (c) Contrôles négatifs dont l'absence serait fatale

- Un LoRA bénin de même rang et de même nombre de pas, et l'agent LoRA hors déclencheur. Ces deux contrôles mesurent b.
- Un LoRA à déclencheur dont la réponse apprise est inoffensive (changement de style).
- Le jumeau teacher-forcé sur le texte exact de l'agent. Si son score de dopamine creuse autant, le signal est dans le texte et l'accès aux activations de l'agent n'apporte rien.
- Des erreurs honnêtes générées on-policy (sélectionnées, non injectées), en plus des injectées.
- Au duel 4, une attaque témoin contre une sonde connue pour être évitable.

---

## Sur la proposition C

**Statut.** C étiquette une supposition (§(a), point 4) OBSERVÉ-NON-AUDITÉ. Les chiffres de la Table 2 sont RAPPORTÉS et l'interprétation est une HYPOTHÈSE. À faire corriger.

### (a) Défauts de méthode

1. **Deux facteurs variés ensemble (expérience 1).** Δδ̂ compare (M_S, pas saboté) à (M_H, pas valide). Les poids et le contenu du pas changent en même temps. Il faut le plan 2×2 poids × texte.
2. **Vrai par construction (expérience 2).** Le score est Σ_K δ̂_k, comparé entre M_S et M_H. Un décalage constant b par pas, dû au seul LoRA, donne un écart Kb qui croît plus vite que le bruit en √K. L'AUROC tend vers 1 avec K sans aucun sabotage. L'accumulation amplifie l'artefact autant que le signal.
3. **Cible non mesurable (expériences 1 et 2, tableau (c)).** Les pas à |ΔV| ∈ [0,02 ; 0,05] sont définis par une quantité que K = 16 rollouts ne résolvent pas, comme le montre le calcul en (b). La condition « sabotage cumulé < −0,50 » repose sur des étiquettes dominées par le bruit.
4. **Duels non exclusifs.**
   - Expérience 2 : H_B agrège deux mécanismes (zone morte de la sonde, bruit de fond) qu'aucune issue ne sépare. L'intervalle 0,60–0,75 n'est attribué à personne.
   - Expérience 3 : H_A est une disjonction (« chute pré/post **ou** divergence KL au prompt »), donc presque infalsifiable. Par ailleurs ΔV̂ = V̂_final(M_S) − V̂_initial(M_H) croise deux modèles et deux positions, alors que l'écart entre positions est déjà non nul chez un modèle honnête.
   - Expérience 4 : H_A porte sur T_sab et H_B sur l'AUROC. La cellule « sabotage maintenu, AUROC maintenue » ne falsifie rien.
5. **Expérience 3, confusions.** « V̂_final > 0,8 » confond une AUC (RAPPORTÉ) avec une valeur de sonde. Les lignes de base 0,52 et 0,48 sont des AUC de prédiction de justesse, non transférables à la détection de sabotage.
6. **Expérience 4.** Le patching par la médiane du jumeau est une ablation hors distribution, pas un rééchantillonnage à préfixe égal. Le sabotage subtil exige de la compétence : une chute de T_sab peut refléter la perte de compétence déjà RAPPORTÉE (75,2 % → 20,3 %).
7. **Reformulation.** Le transfert « sans ré-entraînement » change à la fois le modèle (jumeau → agent) et le domaine (vérifiable → ouvert). Un résultat nul n'est pas attribuable.
8. **Coûts.** Ils omettent l'équipe rouge et l'oracle. Le K requis en (b) les multiplie.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **Fiabilité de l'étiquette.** Avec V ≈ 0,5 et K = 16, σ_MC ≈ 0,18. Sur des pas à |ΔV| < 0,10, Var(ΔV) ≲ 0,0033, donc la fiabilité Var(ΔV)/(Var(ΔV)+σ²_MC) est d'environ 0,10. Le Spearman observable est borné vers 0,31 même pour une sonde parfaite. Le critère « |ρ| ≥ 0,30 » du tableau (c) est quasi inatteignable par construction. Pour atteindre σ_MC ≈ 0,01, il faut K de l'ordre de 5 000.
- **Restriction d'étendue (expérience 1).** Les pas sont sélectionnés sur ΔV_tâche < −0,3. Si Var(ΔV | sélection) → 0, ρ → 0 quelle que soit l'hypothèse vraie. Le seuil |ρ| > 0,25 n'est alors pas jugeable.
- **Agrégat (expérience 2).** La puissance dépend de (Kμ + Kb)/√(Kσ²(1+φ)/(1−φ) + K²τ²). Elle n'est interprétable que si b est estimé nul et τ² estimé. Avec 500 unités à α = 5 %, l'erreur-type du taux de fausses alertes est d'environ 1 point. Le critère « écart de calibration ≤ 1 % » se trouve sous la résolution de l'estimateur.
- **KL entre activations (expérience 3).** L'estimateur n'est pas spécifié. En dimension d'environ 35 (chiffre illustratif de C), les estimateurs de KL sont biaisés à n fini. Le biais doit être mesuré sur des paires honnête/honnête.
- **Expérience 4.** L'issue est conditionnelle à la loi des attaques essayées. Si l'optimisation n'atteint pas AUROC < 0,55, rien n'est appris sur H_A.

### (c) Contrôles négatifs dont l'absence serait fatale

- M_S sur des épisodes où il ne sabote pas, et un LoRA bénin. Sans eux, l'expérience 2 n'a pas de nulle valide.
- M_H teacher-forcé sur les pas sabotés (cellule manquante du 2×2).
- Des erreurs honnêtes de même cumul dans l'expérience 2. C ne les prévoit qu'à l'expérience 1.
- Deux moitiés de rollouts indépendantes, l'une pour définir les pas, l'autre pour les évaluer.
- À l'expérience 4, la même pénalité L2 appliquée à un affinage honnête, et une sonde fraîchement entraînée en plus de la sonde gelée.

---

## Sur la proposition D

### (a) Défauts de méthode

1. **Pas de témoin positif.** D gèle la sonde source sans critère de validité préalable. Il manque la reproduction du résultat source sur le modèle choisi, et la détection d'une dégradation grossière sur la cible. Un duel perdu ne distingue alors pas « pas de signal » d'« instrument insensible ». Chez D, c'est le défaut qui pèse le plus.
2. **Dilution par intention de traiter.** Le positif est « tout dossier assigné ». Si c est la fraction des assignés où un défaut est réellement produit, alors TPR_ITT = c·TPR_exécutants + (1−c)·FPR. Le seuil de +10 points n'a pas de sens sans c. Les résultats « sur défauts confirmés » sont un sous-ensemble post-traitement.
3. **Comparaison non appariée en seuil.** Le critère impose un plafond de 5 %, pas l'égalité des taux réalisés. Un contrôle mécanique est souvent binaire, avec un point de fonctionnement fixe (α_M, β_M). Un candidat calibré à 4,9 % gagne de la détection sur un comparateur à 2 % par le seul seuil.
4. **Canal lexical résiduel.** À poids identiques, tout écart agent/jumeau est une fonction du contexte (D le dit). La sonde est gelée, mais le sens du score, la règle de cumul et le « meilleur montage » sont choisis en validation avec les étiquettes d'assignation. Les familles de formulations inédites limitent ce canal sans exclure une direction « consigne secondaire présente ».
5. **Longueur.** La règle « alerte à n'importe quelle étape » dépend de T. Si la consigne de dégradation change la loi de T, l'écart de détection contient un effet de longueur.
6. **Asymétrie de réglage.** Le candidat a plus de degrés de liberté (couches, frontières, cumul, signe) que les comparateurs mécaniques. La validation favorise le candidat si elle est petite.
7. **Premier contrôle sans contenu.** « Le score initial ne dépend pas de l'assignation ultérieure » est vrai par déterminisme sur préfixe