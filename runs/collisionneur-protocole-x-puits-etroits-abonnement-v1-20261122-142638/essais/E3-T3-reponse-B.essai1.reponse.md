# Proposition B — Tour III.3 : réponse aux critiques

**Pièces.** J'ai reçu ma conception III.1 et les critiques croisées de A, C, D, E et F. Toutes sont présentes, closes par leur balise de fin, et aucune ne paraît coupée. Les conceptions III.1 des autres propositions ne m'ont pas été transmises. Quand une critique en invoque une, je reprends le statut que la critique lui donne. Je n'ai pas recalculé les empreintes. Je ne réponds qu'aux sections « Sur la proposition B ».

**Conventions.** « calcul ici » signifie VÉRIFIÉ par un calcul fait dans ce texte. Tous les seuils, effectifs et budgets sont **illustratifs**, sauf les constantes mathématiques.

---

## (a) Sort des critiques

Deux corrections valent pour toute la suite.

**Notation (D) : acceptée.** En R5, j'ai utilisé p comme prévalence vraie, alors que je l'avais défini comme P(V=1). Désormais :
- Y désigne la propriété vraie, et p = P(Y=1) ;
- p_V = P(V=1) = p(1−β) + (1−p)α ;
- R1 à R3 portent sur p_V, la seule fréquence observable ; R5 relie p_V à p.

**Règle de décision (A, D) : acceptée.** Je reprends celle de D en le disant.
- Le paramètre θ, le seuil s et l'effectif sont fixés avant la collecte. Aucune extension n'est faite après coup : l'extension que je prévoyais au III.1 contredisait R3 (A).
- Si la borne basse dépasse s, « θ ≤ s » est réfutée. Si la borne haute est ≤ s, « θ > s » est réfutée.
- Si l'intervalle traverse s, l'issue est « non jugeable ». Elle est enregistrée et établit |θ − s| < demi-largeur.
- Tout ce qui sert à sélectionner, stratifier ou ajuster vient d'un lot 1. Tout ce qui sert à décider vient d'un lot 2 indépendant.

| # | Critique (source) | Sort |
|---|---|---|
| | **D1** | |
| 1 | Permuter à l'intérieur d'un sous-échantillon laisse la couverture inchangée : le témoin est vide (A) | Acceptée. Je permute entre campagnes. |
| 2 | Clopper–Pearson sur-couvre ; le seuil 0,93 n'est qu'à ≈ 1,3 écart-type de 0,95 ; puissance établie contre Markov seulement ; mesure faite à p modéré (A, E, F) | Acceptée. La métrique est abandonnée, un contrôle par mélange est ajouté et la limite à p faible est déclarée. |
| 3 | p̂_ref est pris pour p : les tests sont corrélés, et un simple décalage de marginale donne une issue hors des deux cas (D, E, F) | Acceptée. Dépendance et décalage de marginale sont mesurés séparément. |
| 4 | Un indice de dispersion n'exclut pas les dépendances d'ordre supérieur (D) | Acceptée. D1′ estime directement P(S_N = 0), l'objet de R1. |
| | **D2** | |
| 5 | Û(k ≤ n/16) et Û(n) sont des fonctions du même compte C_i : la fuite est intégrale (C, E, F ; corrélation relevée par A) | Acceptée. La décision ne repose plus sur une extrapolation. |
| 6 | Avec p₀ libre, H_A est irréfutable (A) ; sous ~1/n, les deux lois sont indiscernables (C, D, E, F) | Acceptée. p₀ est pré-enregistré, et je ne conclus rien sous 1/n. |
| 7 | L'issue « ni plancher ni loi de puissance » n'a pas de lecture (A) ; idem pour une queue en (ln k)^{−γ} (E) | Acceptée. H_A et H_B portent maintenant sur une quantité non paramétrique. |
| 8 | Mettre à part un horizon ne met pas à part une instance ; 30 instances, c'est trop peu ; log Û est indéfini si Û = 0 (D, F) | Acceptée pour la partie descriptive : double séparation, sans logarithme. |
| | **D3** | |
| 9 | Strates et rappel sont estimés sur les mêmes verdicts ; régression vers la moyenne ; atténuation (A, C, D, E, F) | Acceptée. Les strates sont formées sur le lot 1. |
| 10 | Quand p → 0, R7 devient c_v(t−f) > c_g(1−t)+c_f. La conjonction « chute de 0,2 **et** inversion » n'est atteinte que par un filtre quasi aléatoire (A) | Acceptée, et vérifiée ici. Elle est remplacée par un seuil de rentabilité t_crit. |
| 11 | Un coût scalaire contredit S6 ; E[C_v \| F=1] ≠ E[C_v] (E) | Acceptée. J'utilise des coûts conditionnels. |
| 12 | Trop peu de positifs dans la strate basse (A, C, D, F) | Acceptée. La condition de jugeabilité est pré-enregistrée. |
| 13 | p est confondu avec l'identité de l'instance ; il faudrait diluer une même instance (C) | **Rejetée comme défaut ; le contrôle est transformé** (motif plus bas). |
| | **D4** | |
| 14 | D4 sort du modèle « tirages seuls » (C, D, E) | **Rejetée** (motif plus bas). |
| 15 | Le SMC n'est pas une vérité terrain ; la grammaire triviale ne teste que la chaîne logicielle (A, D) | Acceptée. Banc à support fini, avec la loi conditionnelle exacte. |
| 16 | Faire varier r par comptabilité masque le surcoût de c′_g (C) ; c_v dépend des longueurs propres à chaque bras (F) | Rejetée pour c′_g : il était déjà mesuré au III.1, masquage compris. Acceptée pour c_v, désormais mesuré par bras. |
| 17 | Le log-rapport est infini quand un bras n'a aucun succès, et exclure ces instances biaise (E, F) | Acceptée. J'utilise un rapport de sommes. |
| 18 | Un signe de coût n'identifie pas une distorsion de masse ; avec la grammaire universelle, l'égalité porte sur les lois, pas sur les temps (D) | Acceptée. Deux mesures séparées. |
| | **D5** | |
| 19 | Le non-recouvrement de bornes de Clopper–Pearson, combiné à Benjamini–Hochberg, a une puissance ≈ 0,4 à 10/n sans correction (A), quasi nulle avec (C) ; la règle n'est pas calibrée (F) et reste muette sous ≈ 5/n (E) | Acceptée. Mon recalcul (calcul ici, approximation de Poisson) donne 22 succès requis au premier rang, plutôt que 21 ; la conclusion de C ne change pas. Je passe à un plan en deux temps. |
| 20 | Une baisse ne prouve pas une extinction ; le contrôle du taux de fausses découvertes ne borne pas les pertes non détectées ; une baisse d'un facteur 2 n'a pas de lecture (A, D) | Acceptée. H_B est restreinte aux instances où n·p_base ≥ 1. |
| 21 | L'effet de l'affinage est confondu avec la température, le SFT et les autres différences entre modèles (A, D, E, F) | Transformée en bras témoins. |
| | **D6** | |
| 22 | α̂ = P(V*=0 \| V=1) est un taux de fausses découvertes, pas α ; sa pente change même à α constant (A, C, D, E, F) | Acceptée : c'était une erreur de ma part. α est désormais estimé sur les candidats que V* rejette. |
| 23 | Si V* contient les tests de V, β = 0 par construction ; le couple (V, V*) n'identifie pas les erreurs vis-à-vis de Y (A, D, F) | Acceptée. HYPOTHÈSE déclarée, et audit indépendant. |
| 24 | Contrôles demandés : vérificateur synthétique à α fixé (A) ; prévalence seule modifiée ; audit des refus (D) | Acceptés. |

**Motif du rejet 13.** Mon affirmation opérationnelle porte sur les instances à p̂ bas, quelle que soit la cause de leur rareté. Je retire donc toute lecture causale du type « la rareté fait baisser t ». Pour un filtre qui juge chaque objet isolément, ajouter des négatifs ne change pas t = P(F=1 | V=1) : le contrôle de dilution serait vrai par construction (calcul ici). Je le garde pour les filtres à quota ou à rang, dont le rappel dépend du lot.

**Motif du rejet 14.** S2 posait déjà « tirages seuls » comme un choix de cadrage. L'item 3 de la question demande aussi comment la réponse dépend de ce qu'on sait du générateur. D4 relève donc du régime « accès aux logits », que je déclare comme tel. Ses issues ne disent rien du régime « tirages seuls ».

---

## (b) Expériences corrigées

### D1′ — Les tirages, tels qu'ils sont servis, sont-ils indépendants ?

**Unité.** Une campagne est une suite de N tirages consécutifs sur une même instance, dans les conditions de production (lots, requêtes concurrentes). Les K campagnes sont espacées dans le temps, chacune sur une session neuve.

**Taille.** N = c/p̂₀, avec c = 3 et p̂₀ estimé sur un pilote séparé. On vise p modéré, entre 0,01 et 0,05. Une erreur sur p̂₀ coûte de la puissance, pas de la validité.

**Paramètre.** θ₁ = z(N)/(1−p_V)^N, avec z(N) = P(S_N = 0). C'est exactement l'objet de R1.
- **H_A** : θ₁ ≤ 1,25.
- **H_B** : θ₁ > 1,25.

**Estimation.**
- ẑ est la part des campagnes vides.
- p_V est estimé par fenêtre de temps, sur les campagnes et sur des tirages isolés intercalés dans la même fenêtre (E, F). Une dérive entre fenêtres n'est donc pas prise pour une dépendance interne aux campagnes. L'écart p_prod − p_iso est rapporté à part : il change le p de R1 sans réfuter R1.
- La variance due à p̂ vaut ≈ 16 % de celle de ẑ à c = 3, si p̂ repose sur autant de tirages que les campagnes (calcul ici, méthode delta).
- L'intervalle est obtenu par bootstrap sur les campagnes. K ≈ 1 000 donne une puissance ≈ 0,8 contre le contrôle markovien (calcul ici, approximation normale).

**Contrôles négatifs.**
- Verdicts permutés entre campagnes d'une même fenêtre (A) : θ̂₁ doit couvrir 1.
- Tout le pipeline rejoué sur un Bernoulli pseudo-aléatoire de même p̂ (D).

**Contrôles positifs** (calcul ici).
- Mélange Θ ∈ {0, p/η} avec η = 0,8 : θ₁ ≈ 4,4.
- Chaîne de Markov de corrélation 0,2 : θ₁ ≈ e^{0,6} ≈ 1,8.

**Issues.**
- Si la borne basse dépasse 1,25, H_A tombe : R1 et R3 ne valent pas pour ce générateur tel qu'il est servi. Il faut alors des campagnes réinitialisées.
- Si la borne haute est ≤ 1,25, H_B tombe, à ce p.

**Limite.** Auditer l'indépendance coûte K·c/p tirages (calcul ici). À p faible, l'indépendance reste une HYPOTHÈSE extrapolée.

### D2′ — Premiers succès tardifs dans une population d'instances

**Paramètre.** θ₂ = U(n/2) − U(n), c'est-à-dire la part des instances dont le premier succès tombe entre n/2 et n tirages. Une instance insoluble y contribue 0, donc π₀ disparaît (calcul ici). On garde n = 2 000 et M = 300.

**Hypothèses.**
- **H_A** : toute instance soluble a P ≥ p₀ = 20/n, valeur pré-enregistrée. Alors θ₂ ≤ (1−p₀)^{n/2} ≤ e^{−10} (calcul ici).
- **H_B** : θ₂ ≥ 0,02.

**Statistique.** L est le nombre d'instances dont le premier succès tombe dans (n/2, n]. Aucun ajustement n'est fait au préalable sur ces tirages, donc la fuite relevée en 5 disparaît. Une variante de variance plus faible est la différence des estimateurs sans biais de Chen et al. (2021), « Evaluating Large Language Models Trained on Code » (RAPPORTÉ).

**Règle** (calcul ici, approximation de Poisson). Chaque issue réfute l'une des deux hypothèses :
- L ≥ 2 réfute H_A, avec un risque ≤ 10⁻⁴ ;
- L ≤ 1 réfute H_B, avec un risque ≈ 0,02.

**Profil descriptif.** On trace Δ(2^j) = U(2^j) − U(2^{j+1}).
- Sous une queue en puissance d'exposant b, le rapport de deux valeurs successives tend vers 2^{−b}.
- Sous un plancher, Δ s'effondre dès que 2^j·p₀ ≫ 1.
- Tout ajustement paramétrique se fait sur une moitié des instances avec le lot 1, et se teste sur l'autre moitié avec le lot 2.

**Contrôles.**
- Deux populations synthétiques qui ne diffèrent que sur (0 ; 0,1/n) doivent recevoir le même verdict (D).
- Une loi bêta et une loi uniforme sur [p₀ ; 1] doivent être classées correctement.

**Limite acceptée.** Sous ~1/n, ni π₀ ni la masse près de 0 ne sont identifiables à l'horizon n (C, D, E). D2′ ne conclut que sur (1/n ; 1].

**Prérequis.** D1′ ne doit pas avoir réfuté H_A. Sinon, chaque instance reçoit des campagnes réinitialisées.

### D3′ — Le filtre bon marché fait-il gagner sur la strate basse ?

**Lots.** Les strates sont formées sur le lot 1. Sur le lot 2, tous les candidats passent par F et par V, et l'on mesure t, f et les coûts.

**Seuil de rentabilité** (calcul ici, depuis R7 avec des coûts conditionnels). On note E = E[C_v], E₊ = E[C_v | F=1, V=1] et E₋ = E[C_v | F=1, V=0]. Le filtre fait gagner si et seulement si t > t_crit, avec :

t_crit = [c_g + c_f + f(1−p_V)·E₋] / [c_g + E − p_V·E₊]

Quand p_V → 0 et que c_v est constant, t_crit → (c_g + c_f + f·c_v)/(c_g + c_v).

**Paramètre.** θ₃ = t − t_crit, dans la strate basse.
- **H_A** : θ₃ > 0, le filtre fait gagner.
- **H_B** : θ₃ ≤ 0.
- Les deux hypothèses sont complémentaires. L'intervalle est obtenu par bootstrap par grappes d'instances.

**Jugeabilité.** Il faut au moins z²·t(1−t)/w² positifs dans la strate basse, multipliés par l'effet de grappe estimé au pilote. Les tirages manquants sont alloués avant la collecte.

**Description.** La pente de t entre les strates est rapportée, sans lecture causale.

**Contrôles.**
- Filtre aléatoire au même taux de passage : θ₃ < 0 par construction (calcul ici).
- Filtre mécanique : analyse syntaxique, déduplication, compilation.
- Pour un filtre à quota ou à rang : dilution d'une même instance (C).

### D4′ — Décodage contraint contre rejet (régime « accès aux logits »)

**(i) Distorsion de masse.**
- Banc : un générateur synthétique à support fini, dont la loi conditionnelle exacte p(·)/Z se calcule (A, D).
- Mesures : la variation totale entre la sortie du masquage et p(·)/Z, et la comparaison de p_GCD avec p_exact.
- Contrôle : avec la grammaire universelle, les lois de sortie doivent coïncider. Le surcoût du masque vide est chronométré à part.

**(ii) Coût opérationnel sur bancs réels.**
- R₄ est le coût total par succès confirmé du décodage contraint, divisé par la même quantité pour le rejet, avec des sommes sur les instances.
- R₄ est défini dès que chaque bras atteint un minimum de succès pré-enregistré. L'intervalle est obtenu par bootstrap d'instances.
- c′_g est mesuré masquage compris, et c_v est mesuré par bras. r ne varie que par comptabilité sur c_v.
- **H_A** : R₄ ≤ 1 à r = 100, valeur pré-enregistrée.
- **H_B** : R₄ > 1.

**Mécanisme.** L'explication « parce que p_GCD < p_RS » n'est plus tirée du signe du coût. Elle est testée par (i) et par une comparaison directe des p (D).

**Troisième bras.** Le SMC est comparé comme une méthode, pas comme une référence. Sources : Lew, Zhi-Xuan, Grand & Mansinghka (2023), « Sequential Monte Carlo steering of large language models using probabilistic programs » (RAPPORTÉ) ; Loula et al. (2025) : référence à vérifier.

### D5′ — Affinage : instances perdues, en deux temps

**Lot 1.** n tirages par bras et par instance. Sel est l'ensemble des instances où la base réussit au moins une fois et l'affiné jamais.

**Lot 2**, tiré à neuf, sur Sel. N₁₀ compte les instances où la base réussit et l'affiné non ; N₀₁ compte l'inverse.

**Pourquoi le plan est valide** (calcul ici). Posons q = 1−(1−p)^n.
- Pour chaque instance, E[base seule] − E[affiné seul] = q_base − q_aff, quelle que soit la sélection faite au lot 1, car le lot 2 en est indépendant.
- Sous H_A, chaque discordance favorise l'affiné avec une probabilité ≥ ½. Le test des signes exact est donc valide.

**Hypothèses.**
- **H_A** : p_aff ≥ p_base sur toute instance.
- **H_B** : au moins 10 instances ont n·p_base ≥ 1 et p_aff = 0. Chacune entre dans Sel puis compte dans N₁₀ avec une probabilité ≥ (1−e^{−1})² ≈ 0,40 (calcul ici).

**Règles.**
- Si N₁₀ > N₀₁ de façon significative au test des signes unilatéral, H_A tombe.
- Si N₁₀ ≤ 1, H_B tombe, avec un risque ≤ P(Bin(10 ; 0,4) ≤ 1) ≈ 0,05 (calcul ici).
- Sinon, l'issue est déclarée non jugeable.

**Bras témoins.**
- Base contre base, avec le pipeline complet (D).
- Base à une température réglée sur l'entropie par jeton de l'affiné (A, F). Si ce bras « perd » autant d'instances, l'effet n'est pas propre à l'affinage.
- Point de contrôle SFT, s'il est publié (E). Sinon, c'est un facteur confondant déclaré.

**Limite acceptée.** Les instances où n·p_base ≪ 1 ne sont pas identifiables à ce budget (D, E).

### D6′ — Le vérificateur reste-t-il stable sous pression de sélection ?

**Paramètre.** α_n = P(V=1 | V*=0, niveau de sélection n), pour n ∈ {1, 16, 256}.

**Estimation.**
- À chaque niveau, V* est appliqué à un échantillon aléatoire de tous les candidats présentés à V, acceptés comme refusés.
- α_n est estimé sur les candidats que V* rejette, β_n sur ceux qu'il accepte (D).
- Le taux de fausses découvertes est rapporté comme mesure de fiabilité d'une acceptation, mais n'entre pas dans la décision.

**Hypothèses.** θ₆ = α₂₅₆/α₁.
- **H_A** : θ₆ ≤ 1,5.
- **H_B** : θ₆ > 1,5.

**Contrôles.**
- Un vérificateur synthétique à α fixé, indépendant de l'objet, est soumis à la même sélection : θ̂₆ doit couvrir 1 (A).
- On modifie seulement la prévalence, en ajoutant des négatifs connus : α̂ ne doit pas bouger, alors que le taux de fausses découvertes bouge (D).

**Limites déclarées.**
- Si V* contient les tests de V, β = 0 par construction, et les erreurs propres de V* restent invisibles (A, F).
- « V* ≈ Y » est une HYPOTHÈSE. Elle est contrôlée par un audit indépendant d'un échantillon de paires (V=1, V*=0) et (V=1, V*=1).
- Si aucune fausse acceptation n'apparaît, ce qui est attendu sur Lean (HYPOTHÈSE), θ₆ est non jugeable. On rapporte alors α_n ≤ 3/n₋ au niveau 95 % (calcul ici, R3).

### Ordre d'exécution et volume

L'ordre est D1′, puis D6′ sur le banc code, puis D2′, puis D3′, D4′ et D5′. Les lots séparés multiplient à peu près par 1,5 à 2 le volume de tirages estimé au III.1.

---

## (c) Réponse à la question de l'arbitre

### Ce qui est établi (VÉRIFIÉ, sauf mention contraire)

**1. Ce que « garantir » peut signifier (item 1).** On note p_V = P(V=1).
- **Énoncé positif.** Sous i.i.d., pour tout p_V ≥ p₀, n ≥ ln(1/δ)/p₀ implique P(aucun succès en n tirages) ≤ δ. Le prix est n(c_g + c_v) (R1).
- **Impossibilité.** Pour n fixé, sup_{p>0} (1−p)^n = 1. Aucune garantie positive ne tient sans p₀ ni loi a priori (R2).
- **Énoncé négatif.** Après n échecs, p_V ≤ 1 − δ^{1/n} au niveau 1−δ (R3). D montre que, si l'on s'arrête au premier succès, ce certificat reste valide à tout instant sans surcoût (VÉRIFIÉ chez D). Je précise R3 en ce sens.
- **Population d'instances.** P(échec en n) = E[(1−P)^n] ≥ π₀. Si la densité de P se comporte comme c·p^{b−1} près de 0, le budget pour approcher π₀ à ε près croît comme ε^{−1/b} (R4).
- **Reconnaissance.** La précision des objets acceptés n'atteint ½ que si α ≤ p(1−β)/(1−p) (R5).

**2. Ce qu'un budget n ne permet pas d'apprendre.** Sous ~1/n, « p minuscule » et « p = 0 » sont indiscernables (R3 ; C, D, E). Une garantie pour p ≪ 1/n ne peut donc venir que d'une hypothèse sur le générateur, jamais d'une mesure.

**3. Dépendances (item 3).**
- **Corrélation.** Sous une variable latente tirée une seule fois, P(au moins un succès) ≤ P(p(Θ) > 0) pour tout n (contre-exemple de F, VÉRIFIÉ selon A et C). Un indice qui ne voit que deux moments manque cette masse en 0 (VÉRIFIÉ selon A et D). Auditer l'indépendance demande des campagnes d'une longueur de l'ordre de 1/p (C, E, F ; calcul ici en D1′).
- **Rapport des coûts.** Quand p → 0 et que c_v est constant, un filtre fait gagner si et seulement si t > (c_g + c_f + f·c_v)/(c_g + c_v) (calcul ici, depuis R7). Ce seuil tend vers f quand c_g/c_v et c_f/c_v tendent vers 0. À r grand, tout filtre meilleur que le hasard fait donc gagner en coût, sauf si les coûts conditionnels sont asymétriques (E). Cela ne dit rien de son rappel sur les puits étroits.
- **Connaissance du générateur.** L'accès aux logits permet de changer de loi, mais le masquage n'échantillonne pas p(·)/Z (R8). Une grammaire publique fournit toujours un échantillonneur uniforme de référence (S2).
- **Taille de la grammaire.** Elle n'entre dans p, par |L_{≤ℓ}|, que pour l'échantillonneur uniforme (S10). Pour un générateur appris, son effet est une HYPOTHÈSE.

**4. Méthodes répandues (item 4).**
- **Tirage répété avec V exact** : R1 s'applique si les tirages sont i.i.d. et si p₀ est connu ; sinon, seul R3 s'applique.
- **Vote et best-of-n** : avec V exact, ils ne font qu'économiser des appels à V (raisonnement du III.1). Avec V imparfait, ils sont bornés par α (R5). Stroebl, Kapoor & Narayanan (2024), « Inference Scaling fLaws: The Limits of LLM Resampling with Imperfect Verifiers », vont dans ce sens (RAPPORTÉ).
- **Filtres appris** : ils ont un seuil de rentabilité, mais aucune garantie de rappel.
- **Décodage contraint** : rien ne garantit p_GCD ≥ p_RS (R8).
- **Affinage par RL** : aucune garantie sur le support. Une perte de couverture à k grand est RAPPORTÉE par Yue et al. (2025), « Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model? ».

### Ce qui n'est pas établi (HYPOTHÈSES)

- **La loi de P pour des générateurs réels.** Des lois de puissance sont RAPPORTÉES par Brown et al. (2024), « Large Language Monkeys: Scaling Inference Compute with Repeated Sampling », et par Schaeffer et al. (2025), « How Do Large Language Monkeys Get Their Power (Laws)? ».
- **L'indépendance des tirages tels qu'ils sont servis.**
- **La valeur de t aux p faibles.**
- **L'effet des méthodes sur p.**
- **La stabilité de α sous sélection.**

D1′ à D6′ réfutent ou retiennent ces hypothèses. Aucun ne fournit p₀ pour une instance nouvelle.

### Première expérience : D1′

R1 et R3, les seules garanties établies, supposent l'indépendance des tirages. D2′, D3′ et D5′ en dépendent aussi pour leurs risques.
- **Coût** : K·c/p tirages vérifiés, soit ≈ 3·10⁵ à p = 0,01.
- **Si H_A tombe** : R1 et R3 ne s'appliquent pas au générateur tel qu'il est servi. Tout le reste passe en campagnes réinitialisées.
- **Si H_B tombe** : R1 vaut à ce p, à un facteur 1,25 près. Son extension aux p faibles reste une HYPOTHÈSE, et l'auditer coûte un nombre de tirages qui croît comme 1/p.

FIN-DE-CELLULE