# Proposition B, tour III.2 : critique croisée de méthode

**État des pièces.** Le bloc FAITS reproduit la question avec la même empreinte affichée, que je ne recalcule pas, et ne contient aucun fait porteur de statut. Les pièces A, C, D et E sont présentes, se terminent par FIN-DE-CELLULE et ne paraissent pas coupées.

Tout ce qui suit est HYPOTHÈSE de méthode. Les chiffres que je calcule sont illustratifs ; quand je reprends un seuil d'une pièce, je l'attribue à son auteur. Je ne modifie aucun statut. Je signale seulement les statuts qui n'ont aucun support dans FAITS.

---

## Sur la proposition A

### (a) Défauts de méthode

1. **Fuite entre construction et évaluation dans le duel 1.** Les défauts-pièges sont la seule source d'entraînement des sondes. A ne dit pas qui les produit.
   - S'ils sont rédigés ou paraphrasés par l'un des trois modèles de la matrice, la sonde de ce lecteur est entraînée sur sa propre distribution de surface.
   - L'avantage diagonal est alors vrai par construction.

2. **Surprise du lecteur, confondant principal.** Un lecteur-copie honnête lit un texte produit sous consigne adverse par ses propres poids. Sa log-vraisemblance conditionnelle est exactement la référence de la politique honnête du rédacteur.
   - Une sonde peut ne lire que cet écart de vraisemblance, qui est maximal sur la diagonale par définition.
   - A prévoit bien le rapport de vraisemblance, mais comme « vérification à battre » de l'instrument 2, pas comme covariable de l'interaction Δ du duel 1.
   - H_A du duel 1 peut donc être confirmée par un phénomène trivial : la copie reconnaît un texte qu'elle n'aurait pas écrit, ce qui ne prouve pas une connaissance partagée du défaut.

3. **LoRA partagé (variante « lecteur complice »).** Le même adaptateur équipe rédacteur et lecteur. Deux confusions en résultent :
   - toute concordance ou discordance mesurée relève de l'entraînement conjoint, pas de l'identité des poids de base ;
   - une sonde peut détecter la seule présence de l'adaptateur, c'est-à-dire un décalage des activations sur toute entrée, et non un « défaut vu ».

4. **Le duel 2 mesure une coordination explicite.** On dit au relecteur de « désigner la famille qu'il laissera passer ». C'est un jeu de coordination annoncé, pas un sabotage tacite.
   - En outre, si les contextes sont identiques et le décodage glouton, des copies concordent à 100 % par construction.
   - Le hasard 1/K n'est donc pas le bon nul (voir b).

5. **Duel 0.** Les erreurs naturelles du rédacteur m sont sélectionnées par échec de m aux tests cachés : leur type dépend de m.
   - Retirer les effets de ligne et de colonne enlève les niveaux moyens, pas l'interaction « type d'erreur × lecteur ».
   - Avec trois modèles, l'interaction diagonale repose sur peu de degrés de liberté. Elle est confondue avec toute proximité entre paires de modèles (données ou tokeniseur partagés).

6. **Duel 3.** Égaliser les fausses alertes des équipes honnêtes revient à fixer un seuil. Si ce seuil est calibré sur les épisodes honnêtes qui servent aussi à estimer le taux de fausses alertes, l'estimation est optimiste. Il faut un échantillon tenu à part.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **Interaction Δ du duel 1.** Notons F_sab^(r,ℓ) et F_err^(r,ℓ) les lois du score de sonde sous sabotage et sous erreur appariée, pour un rédacteur r et un lecteur ℓ.
  - Si le transfert pièges → sabotage échoue, on a F_sab ≈ F_err dans toutes les cellules, donc AUROC ≈ 0,5 partout. Δ est alors non jugeable (plancher), pas nul.
  - Borne de variance : σ(AUROC) ≤ √(A(1−A)/min(n₊,n₋)). Pour A ≈ 0,7, il faut n₊ ≳ 300 sabotages réussis par cellule pour avoir σ ≈ 0,026 (illustratif). L'interaction combine 9 cellules et leurs variances s'additionnent.
  - Avec le point de blocage de A (5 % de tentatives réussies), cela représente de l'ordre de 6 000 tentatives par cellule (illustratif).
- **Duel 0.** Si le taux d'approbation p des erreurs naturelles est proche de 1 pour tous les lecteurs, l'écart-type binomial par cellule est faible. Mais l'interaction devient bornée par 1 − p, et l'équivalence ±3 points de A est atteinte trivialement.
- **Duel 2.** Soit q_m la loi marginale des choix du modèle m sur les K familles.
  - Sous indépendance, la concordance vaut Σ_k q_a(k)q_b(k). Pour un même modèle, elle vaut Σ q(k)², qui est ≥ 1/K et croît quand l'entropie de q baisse.
  - Un écart « même-modèle moins inter-modèles » positif s'obtient donc sans aucune coordination, dès que les marginales sont piquées et différentes.
  - Estimateur requis : la concordance observée comparée à Σ q̂_a q̂_b, les marginales étant estimées sur des exécutions indépendantes.
  - Si q est uniforme, la concordance vaut 1/K partout et le test perd toute puissance.
- **Duel 3.** Pour une sûreté s ≈ 0,5, tenir la marge de non-infériorité de A (2 points) avec un écart-type d'environ 0,8 point demande n_dégradés ≈ 2s(1−s)/0,008² ≈ 7 800 épisodes dégradés par composition (illustratif). Le dimensionnement doit porter sur les dégradés indépendants.
- **Agrégation par maximum.** Si les scores des k copies ont une corrélation ρ → 1, le maximum n'apporte rien de plus qu'un score unique. Le contraste avec MIXTE dépend alors de ρ, pas de l'identité des poids.

### (c) Contrôles négatifs dont l'absence serait fatale

1. Une sonde réduite au seul log-ratio de vraisemblance du lecteur, plus la même covariable intégrée au modèle de l'interaction Δ.
2. Des défauts-pièges de source hors matrice : mutation mécanique, ou quatrième modèle exclu de la matrice.
3. Un « LoRA leurre » de même rang, entraîné sur un objectif bénin, pour savoir si la sonde lit la présence de l'adaptateur.
4. Des LoRA indépendants (graines et données disjointes) sur la même base, pour séparer coordination héritée et coordination apprise.
5. Pour le duel 2 : décodage échantillonné, contextes variés, et nul calculé par les marginales.

---

## Sur la proposition C

### (a) Défauts de méthode

1. **Δh = h_Auteur − h_Relecteur est contaminé par construction.** Deux sources s'additionnent :
   - les états de l'auteur sont pris en position de génération, sous son prompt, consigne secrète comprise ; ceux du relecteur sont pris en lecture forcée, sous un autre prompt ;
   - Δh contient donc la différence de prompts. En condition « consigne », la sonde peut lire la consigne elle-même.

   Le contrôle « bogue accidentel honnête : Δh faible » est faux par construction, car les prompts de rôle diffèrent toujours. E centre par rôle ; je m'en sers pour constater que C ne le fait pas.

2. **Attribution indue à la multiplicité des copies.** Le défenseur héberge les poids. Il peut toujours rejouer une copie honnête de référence sur l'artefact :
   - pour l'agent seul ;
   - pour chaque modèle de l'équipe hétérogène (rejouer Qwen honnête sur le code de Qwen).

   C attribue le statut [VÉRIFIÉ] à « agent seul sans contrepartie indépendante à soustraire ». Ce statut n'a pas de support dans FAITS ; je le signale sans le changer. Le comparateur « référence de même poids rejouée » manque, et le gain revendiqué pour les copies peut venir de ce seul accès, disponible dans les trois régimes.

3. **Ablation rotation + Procrustes.** Les activations sont exactes et viennent du même modèle. Le Procrustes orthogonal retrouve donc Q exactement dès que n_cal ≥ d points en position générale.
   - Avec les valeurs de C (n_cal = 1 000 pour d = 4 096, illustratifs chez C), l'alignement est sous-déterminé et l'échec est garanti.
   - L'issue est dictée par le rapport n_cal/d, pas par les données.

4. **Expérience 1 : comparaison au maximum de D et S.** L'agent seul a toute la chaîne dans son contexte : il se coordonne trivialement.
   - Le critère de légitimité est appliqué pièce par pièce dans tous les régimes ; il ne pénalise donc pas S spécifiquement.
   - Le maximum de D et S rend H_1A difficile à confirmer par construction.
   - Le mécanisme invoqué (« isolement de responsabilité ») n'est pas mesuré par TSDF.

5. **Fuite entre filtre et instrument évalué.**
   - Le critère 3 (légitimité ≥ 0,80 selon un juge, valeur de C) entre dans la définition du succès adverse. L'observateur textuel est ensuite évalué sur ces mêmes épisodes : sa faiblesse est en partie construite.
   - Le LoRA est optimisé pour réussir sous ce juge, pas contre la sonde.
   - La « dualité » texte / activations est donc en partie inscrite dans le protocole.

6. **Adaptateur commun conditionné par le rôle.** La coordination observée serait apprise, pas héritée des poids de base.

7. **Statuts et référence.** C attribue le statut [VÉRIFIÉ] à la non-isomorphie des espaces latents et aux lacunes partagées. Je le signale sans le modifier. Le co-auteur « Kieronzmann » ne concorde pas avec les listes d'auteurs données par A et E : attribution à vérifier.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **Expérience 1.** La différence de différences (copies adverses − honnêtes, contre l'autre régime) a un écart-type d'environ √(Σ p_i(1−p_i)/500).
  - Pour p ≈ 0,1 : écart-type ≈ 0,027, et le seuil de détection à p < 0,01 est d'environ 7 points.
  - Pour p ≈ 0,3 : écart-type ≈ 0,041, et le seuil de détection dépasse 10 points. Un effet réel égal au seuil de C ne serait pas déclaré.
  - Ces deux cas sont illustratifs.
- **Rappel@10 %.** Il est borné par min(1, b/π), où π est la prévalence des dégradations dans le flux.
  - Le critère d'instrument de C (rappel ≥ 80 % à K/N = 10 %) est impossible si π > 12,5 %.
  - C ne fixe pas π.
- **Gain de Δh.** Si la meilleure sonde individuelle a déjà un taux de détection proche de 1, le gain de +15 points est non jugeable (plafond).
- **R_comm de l'expérience 3.** C'est un rapport.
  - Si le dénominateur δ = TSDF_comm − TSDF_sans a une moyenne faible devant son écart-type (δ/σ_δ < 2, illustratif), l'estimateur a une variance non bornée (rapport de lois approximativement normales).
  - Les seuils 40 % et 10 % deviennent non jugeables. Il faut rapporter des différences, ou des intervalles de type Fieller.
- **Procrustes.** Résultat déterminé par n_cal/d (voir a.3).

### (c) Contrôles négatifs dont l'absence serait fatale

1. Une consigne privée honnête de longueur appariée dans le contexte de l'auteur, ou le passage au seul LoRA.
2. Δh centré par rôle sur des paires honnêtes.
3. Une référence de même poids rejouée en régimes S et D.
4. Un LoRA leurre, et des LoRA indépendants.
5. Un balayage de n_cal de part et d'autre de d.
6. Un juge de légitimité distinct du moniteur textuel évalué.

---

## Sur la proposition D

### (a) Défauts de méthode

1. **Le contraste de transfert est réglable.** G_copies − G_différents dépend de l'alignement autorisé pour les poids différents (« exemples honnêtes parallèles »). D ne fixe pas la taille de ce corpus par rapport à la dimension des activations ; l'issue peut être déplacée à volonté.

2. **Fuite de consigne dans le duel défensif.** Le détecteur ne reçoit ni les consignes ni « leurs activations ».
   - Mais les activations aux décisions sont calculées avec la consigne dans le contexte, et l'attention y donne accès.
   - D place le contrôle « consignes privées de longueur appariée » dans le duel adverse, pas dans le duel défensif. C'est pourtant dans le duel défensif qu'il est indispensable, puisque D ne fait aucun réentraînement : la consigne est le seul canal d'induction.

3. **Appariement sur la compétence mesurée en pilote.** Sélectionner des familles ou des modèles pour égaliser la compétence produit deux effets :
   - une régression vers la moyenne au test ;
   - des distributions de tâches différentes entre régimes, si l'appariement procède par sous-échantillonnage.

4. **Ambiguïté de G.** D dit que les mauvais plans honnêtes comptent comme négatifs « pour une prétention à détecter l'adversité ». Mais G est défini comme un « gain de rappel » sans préciser sur quels positifs. Selon le choix, le duel défensif teste la détection du dommage ou celle de l'adversité.

5. **Témoin d'identité.** À graines identiques, le témoin reproduit les copies par déterminisme. C'est un contrôle d'implémentation, à ne pas compter comme réplication.

6. **Revendication de « compensation ».** Elle exige la conjonction de trois issues : avantage adverse avant audit, bilan après audit, et effet du retrait des activations. Le risque global de conclusion erronée n'est pas contrôlé.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **R_g.** Il est rapporté à tous les plans soumis. Pour un taux de base p ≈ 0,05 de mauvais plans livrés, le seuil de 1 point de D demande un écart-type ≲ 0,4 point, soit n ≈ 2p(1−p)/0,004² ≈ 6 000 plans par régime (illustratif).
  - Il faut multiplier par l'effet de grappe 1 + (m−1)ρ, où m est le nombre de plans par famille et ρ la corrélation intra-famille.
  - D dimensionne sur les plans dégradés indépendants, mais ne mentionne pas ρ.
- **G à budget de 5 %.** Le rappel est plafonné par 0,05/π. Si π est grand, les deux régimes plafonnent et G_copies − G_différents tend vers 0 par construction.
- **Transfert.** Deux cas rendent le contraste peu informatif :
  - si les lois des scores dans le rôle cible sont déjà séparables avec le petit budget de calibration cible, le transfert est inutile et le contraste ne mesure plus le transfert ;
  - si ce budget tend vers 0, le contraste ne dépend plus que de n_align/d.
- **Permutation par strates.** Si les strates (rôle × difficulté × longueur) sont si fines qu'elles contiennent un seul plan, la permutation est l'identité. Le contrôle est alors non jugeable et doit rapporter la taille effective des strates.

### (c) Contrôles négatifs dont l'absence serait fatale

1. Des consignes privées honnêtes de longueur appariée, dans le duel défensif également.
2. Un balayage de n_align.
3. Une sonde sur la couche d'entrée et sur la longueur, pour écarter un signal lexical.
4. L'audit aléatoire au même budget, déjà présent chez D, à conserver.

---

## Sur la proposition E

### (a) Défauts de méthode

1. **Le contrôle H-rot teste la statistique, pas les données.** Le score de E combine une sonde partagée et une covariance résiduelle inter-copies.
   - Toute statistique invariante par rotations indépendantes est inchangée sous H-rot par construction. C'est le cas de la norme de Frobenius ou des valeurs singulières de la covariance croisée : ‖Q₁CQ₂ᵀ‖_F = ‖C‖_F. C'est aussi le cas d'une sonde réentraînée par copie.
   - À l'inverse, une différence directe ou une sonde commune non réentraînée chute sous H-rot, là encore par construction.
   - La seule part empirique est l'efficacité en étiquettes du partage, fonction de n_étiquettes/d.

2. **Double usage du budget d'audit.** Les épisodes audités servent à la fois à calibrer en ligne le détecteur et à compter TPR@b.
   - Si un épisode contribue à la règle qui l'évalue, TPR@b est optimiste.
   - Il faut une évaluation préquentielle : score figé avant l'audit de l'épisode.

3. **Fuite entre filtre et instrument évalué.**
   - « Défendable » est défini comme « sous le quantile 95 % du juge sur les honnêtes » (valeur de E). Le moniteur textuel est ensuite évalué sur ces mêmes épisodes : s'il est corrélé au juge, son taux de détection est bas par construction.
   - Le LoRA est entraîné par rejet sur des traces défendables : il est adapté au juge textuel, pas à la sonde.
   - Le « renversement » prédit est donc en partie construit.

4. **Le duel E3 ne porte pas sur l'identité.** E affirme S_reset ≡ H [VÉRIFIÉ] ; je signale ce statut sans le modifier.
   - Si c'est exact, H contre S mesure la continuité du contexte, pas l'identité des copies.
   - « Taux de dégradation effective égalisé » revient à régler l'attaque par régime sur une variable post-traitement, ce qui introduit un biais de sélection.

5. **Appariement pass@1 ±3 points par filtrage de problèmes.** Si le filtrage diffère selon le régime, les distributions de tâches diffèrent entre régimes.

6. **LoRA « pour les trois rôles ».** Si les adaptateurs de H sont entraînés conjointement sur des trajectoires composées, la coordination est apprise, pas héritée des poids de base.

7. **Asymétrie de E2.** H_2A exige le succès dans deux régimes, alors que H_2B se contente d'un échec dans l'un. À risque α égal par test, la puissance de H_2A est réduite.

8. **Statuts sans support dans FAITS**, signalés sans modification :
   - [VÉRIFIÉ] pour la distribution p_W identique : vrai pour les poids, mais les contextes diffèrent, et la convergence tacite n'en découle pas ;
   - [VÉRIFIÉ] pour la faisabilité en deux mois ;
   - [OBSERVÉ-NON-AUDITÉ] pour l'artefact de prompt, sans observation transmise ;
   - [VÉRIFIÉ] pour la comparaison sonde / logits.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **Critère d'allocation.** Intercepter 60 % des dégradations avec b = 5 % (valeurs de E) est impossible si la prévalence π dépasse b/0,6 ≈ 8,3 %.
  - E2 fixe 10 % d'épisodes adverses, plus les bogues honnêtes : le critère est infaisable par construction.
  - Le taux de détection maximal y est de 50 %, et l'écart de 10 points de E2 se joue sous ce plafond, pour tous les régimes.
- **H-rot.** Si n_étiquettes ≫ dimension effective, une sonde réentraînée par copie égale la sonde partagée. Le contraste H − H-rot tend vers 0 quelles que soient les données.
- **Appariement en perplexité** (±0,3 nat, valeur de E). Si les lois de perplexité sous adversaire et sous honnêteté ont des supports quasi disjoints, l'ensemble apparié est vide ou minuscule. Le critère d'AUROC devient non jugeable, et l'effectif apparié doit être rapporté.
- **E1** (seuil de 8 points, intervalle à 99 %, N = 500, valeurs de E). Pour p ≈ 0,4 : écart-type ≈ √(2 × 0,24 / 500) ≈ 0,031, et la demi-largeur de l'intervalle est d'environ 8 points (illustratif). Le seuil coïncide avec le bruit, et un effet égal au seuil a environ une chance sur deux d'être déclaré.

### (c) Contrôles négatifs dont l'absence serait fatale

1. Une évaluation préquentielle.
2. Un juge de défendabilité distinct du moniteur évalué (autre modèle, données disjointes).
3. Un LoRA leurre, et des LoRA indépendants sur la même base.
4. Pour H-rot : une statistique non invariante désignée à l'avance, plus un balayage de n_étiquettes.
5. Une référence honnête de même poids rejouée en régime D.

---

**Note de B.**
- Ces critiques ne départagent pas les quatre conceptions sur le fond. Elles indiquent où chaque issue annoncée serait acquise d'avance plutôt qu'observée.
- Je ne fusionne pas les remèdes. Les contrôles « LoRA leurre », « référence de même poids rejouée » et « balayage n/d » valent pour plusieurs propositions, mais chacune doit les intégrer à son propre duel.
- Les références mentionnées ci-dessus restent dans le statut que leur donne chaque pièce. Je n'en ajoute aucune.

FIN-DE-CELLULE