# Règle « moniteur invalide » : re-dérivation indépendante, version 1

- Auteur : Claude Opus 5.5, dériveur indépendant (règle d'indépendance GO-2026-11-21-55, décision D-2) ; seul l'énoncé reçu a été lu, aucune note du 21 novembre ni aucun dossier exclu.
- Date : 21 novembre 2026. Pièce de travail, aucune lecture de résultat d'expérience.
- Programme : `calcul_regle_moniteur_invalide_v1.py` ; sortie : `sortie_calcul_regle_moniteur_invalide_v1.txt` (même dossier, scellés à côté).
- Réserve de provenance : les voisins cités au §5 (point 4 de l'énoncé) ont été vus en ligne (résumés), pas lus sur PDF empreinté ; aucun de leurs chiffres n'est repris (règle R7).

## 0. Verdict

1. **Garantie 1 : vraie**, par l'inégalité de Ville, sous une hypothèse exacte : le tirage d'audit de l'épisode t est une pièce de Bernoulli(q) fraîche, indépendante de tout le passé et de ce que l'agent fait à l'épisode t. Elle tient quelle que soit la dépendance entre épisodes et l'adaptation de l'agent, **même s'il voit les tirages passés**. Il faut aussi un oracle sans fausse alerte et des taux de la grille au moins égaux à ρ₀. Elle tombe si l'agent devine le tirage courant (contre-exemple au §2.3).
2. **Garantie 2 : vraie sous forme bornée, mais la borne ne croît comme la racine de n qu'avec une grille qui descend vers ρ₀.**
   - **Règle telle qu'écrite (produit des moyennes).** Elle se réduit à un seul rapport de vraisemblance, au taux moyen de la grille (3,125 ρ₀). Un attaquant au taux constant 1,5 ρ₀ n'est jamais annoncé avec une probabilité d'au moins 0,70 ; à 1,8 ρ₀, d'au moins 0,27 (borne de Lundberg, sortie §1b). L'excès garanti est **linéaire en n**, de pente environ 0,09 (environ 0,91 ρ₀). Une garantie sous-linéaire est réfutée pour cette lecture.
   - **Moyenne des produits avec la grille {1,25 ρ₀ … 5 ρ₀}.** L'excès est encore linéaire à long terme, de pente 0,0121 (environ 0,12 ρ₀). Il ressemble à une racine de n tant que n est de l'ordre de 2 300/q ou moins.
   - **Grille qui descend vers ρ₀, ou mélange continu.** L'excès est d'ordre √(n ρ₀ (1−ρ₀)/q). C'est l'ordre optimal : une borne inférieure valable pour toute règle de niveau α le montre (§3.5).
3. Les pièces sont classiques : martingale de pari, Ville, rapport de vraisemblance mélangé, échantillonnage d'audit à probabilité connue. Ce qui serait propre à l'emploi contre un agent qui choisit, c'est :
   - la condition exacte sur ce que l'agent peut voir des tirages ;
   - la borne sur le dommage accumulé avant l'annonce, plutôt que sur le délai de détection ;
   - la bande de taux où l'agent peut s'installer sans être annoncé.

   Un voisin récent semble occuper une partie de ce terrain (arXiv 2610.18948, §5) : à vérifier sur PDF avant toute revendication (règle R8).

## 1. Cadre et notations

- X_t = D_t (1 − S_t) ∈ {0, 1} : l'épisode t est endommagé et non signalé. D_t existe sur tout épisode ; l'oracle ne le révèle que si A_t = 1. Y_t = A_t X_t.
- 𝓕_{t−1} : tout ce qui s'est passé avant l'épisode t, c'est-à-dire les états de l'agent et de l'environnement, les X, S, D, les tirages passés A_1..A_{t−1} et les annonces. 𝓖_t = 𝓕_{t−1} ∨ σ(X_t) : le passé plus ce que l'agent a fait à t.
- Comptes : T_m = Σ_{t≤m} X_t (vrai nombre d'épisodes endommagés et non signalés) ; N_m = Σ_{t≤m} A_t (audits) ; M_m = Σ_{t≤m} A_t X_t (audits endommagés non signalés).
- Pour un taux ρ ∈ (ρ₀, 1) :
  - u = log(ρ/ρ₀) ;
  - b = log((1−ρ₀)/(1−ρ)) > 0 ;
  - a = u + b = log(ρ(1−ρ₀)/(ρ₀(1−ρ))) ;
  - rapport de vraisemblance d'un audit : ℓ_ρ(x) = (ρ/ρ₀)^x ((1−ρ)/(1−ρ₀))^{1−x} = exp(a x − b).
- Seuil de non-détection : r*(ρ) = b/a ∈ (ρ₀, ρ). Sous un taux réel r, la croissance logarithmique espérée par audit vaut r a − b. Elle est négative pour r < r*(ρ).

**Hypothèses (numérotées pour la suite).**
- (H-a) **Tirage d'audit frais** : P(A_t = 1 | 𝓖_t) = q. Autrement dit, A_t est indépendant du passé et de l'action de l'épisode t. L'énoncé le donne (« indépendant de tout ce que l'agent observe », « indépendant, conditionnellement au passé, de ce que l'agent fait à t »). La preuve n'utilise que cette forme. Les tirages passés peuvent entrer dans 𝓕_{t−1} et être vus par l'agent.
- (H-b) **Oracle exact** sur les épisodes audités : il rend D_t sans erreur.
- (H-c) **Grille** : ρ₀ ≤ ρ_k < 1 pour tout k. La grille de l'énoncé, ρ_k ≤ 5 ρ₀, exige ρ₀ < 0,2.
- (H-0) **Hypothèse nulle** : p_t := P(X_t = 1 | 𝓕_{t−1}) ≤ ρ₀ pour tout t, presque sûrement, avec 𝓕_{t−1} qui contient les tirages passés. Si les audits n'ont aucun effet sur l'agent ni sur l'environnement, c'est la même chose que conditionner sur le seul passé de l'agent. Si un audit a des suites (dommage réparé, agent averti), la nulle doit être posée sur 𝓕 complet.

**Deux lectures de la richesse.** L'énoncé dit « produit, sur les épisodes audités, de la moyenne de K rapports ».
- *Produit des moyennes* : W_n = Π_{t≤n, A_t=1} (1/K) Σ_k ℓ_{ρ_k}(X_t). Or ℓ_ρ(x) est affine en ρ (ℓ_ρ(1) = ρ/ρ₀, ℓ_ρ(0) = (1−ρ)/(1−ρ₀)). Donc **(1/K) Σ_k ℓ_{ρ_k} = ℓ_{ρ̄}, où ρ̄ est la moyenne de la grille**. La « moyenne de K rapports » n'est qu'un rapport unique, au taux ρ̄ : c'est un pari à fraction fixe, qui ne s'adapte pas. Pour la grille arithmétique {1,25 ; 1,50 ; … ; 5,00} ρ₀ (K = 16), ρ̄ = 3,125 ρ₀.
- *Moyenne des produits* (mélange de rapports de vraisemblance) : W_n = (1/K) Σ_k Π_{t≤n, A_t=1} ℓ_{ρ_k}(X_t) = (1/K) Σ_k exp(a_k M_n − b_k N_n). C'est sans doute ce qui est voulu.

Les deux lectures sont traitées ci-dessous.

## 2. Garantie 1 (fausse annonce)

### 2.1 Énoncé
Sous (H-a), (H-b), (H-c) et (H-0), pour les deux lectures :
P(∃ n ≥ 1 : W_n ≥ 1/α) ≤ α.
Cela vaut quelle que soit la dépendance entre épisodes. Cela vaut aussi quand la politique de l'agent dépend de tout son passé, tirages passés compris, et pour tout temps d'arrêt choisi par le défenseur (arrêt optionnel, lecture continue).

### 2.2 Preuve
Fixons ρ ∈ [ρ₀, 1). Le facteur de l'épisode t vaut 1 si A_t = 0, et ℓ_ρ(X_t) si A_t = 1 : F_t = 1 + A_t (ℓ_ρ(X_t) − 1).

On calcule d'abord l'espérance conditionnelle au passé et à X_t. Par (H-a) :
E[F_t | 𝓖_t] = 1 + q (ℓ_ρ(X_t) − 1).

On conditionne ensuite sur 𝓕_{t−1}. Comme E[ℓ_ρ(X_t) | 𝓕_{t−1}] = p_t ρ/ρ₀ + (1−p_t)(1−ρ)/(1−ρ₀), on obtient :
E[F_t | 𝓕_{t−1}] = 1 + q (p_t − ρ₀)(ρ − ρ₀) / (ρ₀(1−ρ₀)) ≤ 1,
car p_t ≤ ρ₀ par (H-0) et ρ ≥ ρ₀ par (H-c).

Donc Π_{s≤t} F_s est une surmartingale positive d'espérance initiale 1. C'est le cas pour ρ = ρ̄, donc pour le produit des moyennes. Une moyenne de surmartingales sur la même filtration est encore une surmartingale, donc c'est aussi le cas pour le mélange. L'inégalité de Ville (P(sup_n W_n ≥ c) ≤ E W_0 / c) donne le résultat avec c = 1/α. ∎

À retenir : la preuve n'a besoin ni de l'indépendance entre épisodes, ni d'une politique fixe. Il lui faut seulement l'espérance conditionnelle de chaque facteur, et c'est (H-a) qui la rend calculable. La garantie porte sur l'existence d'une annonce à un instant quelconque, sans horizon.

### 2.3 Ce qui la casse (avec contre-exemples)
- **L'agent connaît le tirage courant.** Exemple : q = 0,05, ρ₀ = 0,10. L'agent endommage exactement les épisodes audités. Alors p_t = q = 0,05 ≤ ρ₀ : la nulle (H-0) tient. Mais chaque audit voit X = 1, la richesse est multipliée par ρ̄/ρ₀ à chaque audit, et l'annonce est certaine. La fausse annonce vaut 1. Plus généralement, toute corrélation entre A_t et X_t sachant 𝓕_{t−1} (canal caché, latence, type de tâche qui prédit l'audit) sort de la preuve.
- **Tirages prévisibles** : pseudo-aléa dont la graine fuit, ou calendrier d'audit déterministe. C'est le même effet.
- **Fausses alertes de l'oracle.** Si l'oracle rend 1 sur un épisode sain avec une probabilité allant jusqu'à ε₊, le taux observé sous la nulle peut atteindre ρ₀ + ε₊(1−ρ₀). Correctif valide : tester à ρ₀' = ρ₀ + ε₊(1−ρ₀), si ε₊ est borné et ne dépend pas de l'agent. Les oublis de l'oracle (ε₋) ne cassent pas la garantie 1 : ils la rendent conservatrice.
- **Nulle « en moyenne » seulement.** Supposons seulement (1/n) Σ p_t ≤ ρ₀. Un agent qui commence à 2 ρ₀ puis tombe à 0 a la moyenne voulue, mais il est annoncé tôt avec une probabilité bien plus grande que α. La garantie à tout instant exige la nulle conditionnelle épisode par épisode.
- **Un taux ρ_k < ρ₀ dans la grille.** Le facteur peut alors avoir une espérance > 1 sous la nulle.
- **Seuil du moniteur réglé sur les audits.** Ce n'est pas un problème pour la garantie 1, tant que (H-0) est énoncée sur le X_t réellement produit. Le seuil gelé simplifie la lecture de la nulle, mais la preuve ne s'en sert pas.

## 3. Garantie 2 (dommage accumulé avant l'annonce)

### 3.1 Énoncé (forme exacte)
Notons τ l'instant de la première annonce. Prenons (H-a) et (H-b) et une politique d'attaque quelconque : adaptative, avec ou sans vue des tirages passés, mais qui ne voit pas le tirage courant.

On définit :
- φ_q(s) = q s + log(1 − q + q e^{−s}) : le logarithme de E[exp(−s (A − q))] pour A de loi de Bernoulli(q) ;
- L = log(K/α) pour le mélange, L = log(1/α) pour le produit des moyennes ;
- pour chaque taux ρ_k (pour le produit des moyennes, ρ̄ seul) et chaque λ > 0 :
  - A_{k,λ} = q a_k − [φ_q(λ u_k) − φ_q(−λ b_k)] / λ ;
  - C_{k,λ} = q b_k + φ_q(−λ b_k) / λ.

**Théorème.** Pour tout couple (k, λ) fixé d'avance avec A_{k,λ} > 0, avec probabilité au moins 1 − β, **pour tout m < τ** :

  T_m − ρ₀ m < [L + log(1/β)/λ] / A_{k,λ} + m · (C_{k,λ}/A_{k,λ} − ρ₀).

Pour un horizon n, la borne B(n) est le minimum de cette expression prise en m = n, sur (k, λ). Ce choix dépend seulement de (n, q, ρ₀, α, β, grille). On le fait d'avance : aucune union sur k n'est nécessaire, et log(1/β) suffit. L'épisode d'annonce lui-même ajoute au plus 1.

### 3.2 Preuve
1. *Pas d'annonce donne une inégalité linéaire.* Si W_m < 1/α, alors pour chaque k, (1/K) exp(a_k M_m − b_k N_m) ≤ W_m < 1/α. Donc a_k M_m − b_k N_m < L, c'est-à-dire Σ_{t≤m} A_t c_t < L, avec c_t = a_k X_t − b_k ∈ {u_k, −b_k}. Pour le produit des moyennes, c'est la même chose avec ρ̄ et L = log(1/α).
2. *Martingale exponentielle exacte du tirage.* c_t est 𝓖_t-mesurable et A_t est une Bernoulli(q) indépendante de 𝓖_t (H-a). Donc E[exp(−λ (A_t − q) c_t) | 𝓖_t] = exp(φ_q(λ c_t)). Par conséquent, Z_m = exp(−λ Σ_{t≤m} (A_t − q) c_t − Σ_{t≤m} φ_q(λ c_t)) est une martingale positive d'espérance 1. Par Ville, avec probabilité ≥ 1 − β, pour tout m :
   Σ A_t c_t ≥ q Σ c_t − [log(1/β) + T_m φ_q(λ u_k) + (m − T_m) φ_q(−λ b_k)] / λ.
3. *Combinaison.* q Σ c_t = q (a_k T_m − b_k m). Avec l'étape 1, on obtient T_m · A_{k,λ} < L + log(1/β)/λ + m C_{k,λ}. On divise par A_{k,λ} > 0 et on retranche ρ₀ m. ∎

Le terme de variance est linéaire en T_m. Il n'y a donc pas de cercle : on n'a pas besoin de supposer T_m petit pour borner sa variance. C'est ce qui rend cette borne nettement plus serrée que la forme fermée ci-dessous.

### 3.3 Forme fermée (plus lâche)
Par l'inégalité de Freedman (forme de Bernstein), on obtient une forme fermée :
- accroissements (q − A_t) c_t ≤ R_k = max((1−q) b_k, q u_k) ;
- variance cumulée ≤ v_k = n q (1−q) max(u_k², b_k²) ;
- x_k = R_k ℓ_β/3 + √((R_k ℓ_β/3)² + 2 v_k ℓ_β), avec ℓ_β = log(1/β).

Avec probabilité ≥ 1 − β, pour tout m < τ avec m ≤ n :

  T_m − ρ₀ m < min_k { (r*_k − ρ₀) n + [log(K/α) + x_k] / (q a_k) },  où r*_k = b_k/a_k.

On y lit la structure :
- **un terme linéaire (r*_k − ρ₀) n** : la bande de non-détection ;
- **un terme en √(n (1−q)/q)**.

### 3.4 Croît-elle comme la racine de n ?
- **Produit des moyennes (lecture littérale) : non.** Il n'y a qu'un taux, ρ̄ = 3,125 ρ₀, donc r̄* = 0,1912 (1,91 ρ₀). Un attaquant au taux constant r ∈ (ρ₀, r̄*) fait décroître la richesse vers 0 presque sûrement. W^θ, où θ(r) ∈ (0, 1) résout E_r[ℓ_ρ̄(X)^θ] = 1, est une martingale sous r : par Ville, l'annonce n'arrive jamais avec une probabilité au moins 1 − α^{θ(r)}. Sur cet événement, l'agent accumule (r − ρ₀) n sans fin. Valeurs (sortie, §1b) : à 1,5 ρ₀, θ = 0,40 et la probabilité de n'être jamais annoncé est ≥ 0,70 ; à 1,8 ρ₀, θ = 0,10 et elle est ≥ 0,27, donc ≥ β. Avec probabilité ≥ β, l'excès vaut donc au moins 0,08 n − O(√n). Près du seuil (1,9 ρ₀), θ tend vers 0 et la borne ne dit plus rien : l'attaquant finit par être annoncé, mais tard. La pente de la borne tend vers environ 0,091 (sortie, §2b : 0,0917 à n = 10⁷). **La garantie 2 « en racine de n » est réfutée pour cette lecture.**
- **Moyenne des produits, grille {1,25 ρ₀ … 5 ρ₀} : non asymptotiquement.** Le plus petit taux 1,25 ρ₀ laisse une bande (ρ₀ ; 1,1209 ρ₀] où la richesse décroît. La pente limite vaut r*_1 − ρ₀ = 0,0121 (sortie, §2b : 0,0125 à n = 10⁷).
  - En pratique, l'excès optimal en racine de n demande un écart ε ≈ √(2 L (1−ρ₀)/(q ρ₀ n)) au-dessus de ρ₀.
  - Cet écart descend sous 0,25 vers n de l'ordre de 2 300/q : environ 11 500 épisodes à q = 0,20, environ 46 000 à q = 0,05.
  - En deçà, la borne paraît évoluer en racine de n ; au-delà, elle devient linéaire.
- **Grille qui descend vers ρ₀ : oui.** C'est le cas de ρ₀ (1 + 4·2^{−j}), j = 0..11, K = 12 (sortie, §2b : borne/√n ≈ 3,5 à q = 0,20 et ≈ 7,3 à q = 0,05, stable jusqu'à n = 10⁷).
  - Ordre principal, heuristique : B(n) ≈ √(2 ρ₀ n / q) · (√((1−ρ₀) log(K/α)) + √((1−q) log(1/β))) (colonne « ordre principal » de la sortie).
  - Une grille finie finit par redevenir linéaire, avec une pente minuscule (10⁻⁴ ici).
  - Pour une garantie en √(n log n) à tout horizon, il faut une grille dyadique dont la taille croît comme log n, ou un mélange continu (loi a priori sur [ρ₀, 1)).

### 3.5 L'ordre √(n/q) ne peut pas être battu
Prenons **n'importe quelle** règle de niveau α qui n'observe que les audits. Un attaquant à taux constant ρ₀ + δ, sans regarder les tirages, produit des observations dont la loi diffère de celle de la nulle (taux ρ₀) d'au plus VT ≤ √(KL/2). Ici KL = q n · kl(ρ₀ + δ ‖ ρ₀) : les épisodes non audités ont la même loi sous les deux hypothèses.

Donc P(annonce avant n) ≤ α + VT. Avec probabilité ≥ 1 − α − VT − γ, il n'y a pas d'annonce **et** T_n dépasse le quantile γ de la loi binomiale Bin(n, ρ₀ + δ). On exige que cette probabilité soit ≥ β.

L'excès ainsi atteint est d'ordre √(n ρ₀(1−ρ₀)/q) (sortie, §3, avec γ = 0,05). Pour ρ₀ = 0,10, α = 0,05, β = 0,10, cela donne :
- q = 0,20 : au moins 18, 36 et 73 épisodes pour n = 1 000, 4 000 et 16 000 ;
- q = 0,05 : au moins 55, 107 et 211.

C'est un minorant valable pour toute règle. Le facteur √(1/q) est irréductible : auditer quatre fois moins double l'excès inévitable.

### 3.6 Ce qui casse la garantie 2
- **L'agent voit le tirage courant**, ou le prédit. Il endommage les seuls épisodes non audités : M reste nul, la richesse décroît, et T_n atteint (1 − q) n sans annonce. L'excès est linéaire et maximal. Voir les tirages *passés* ne casse rien, puisque la preuve conditionne déjà sur eux. C'est seulement vrai si les tirages sont de vraies pièces indépendantes : un générateur dont l'état se déduit des tirages passés retombe dans le cas précédent.
- **L'oracle se trompe.**
  - Oublis à un taux ≤ ε₋, indépendants de l'agent : l'oracle voit un taux (1 − ε₋) r. La borne vaut pour le dommage *vu*. Le vrai excès se majore par [B(n) + ρ₀ n]/(1 − ε₋) − ρ₀ n : un biais linéaire ε₋ ρ₀ n/(1 − ε₋) s'ajoute.
  - Oublis que l'agent choisit (dommage taillé pour échapper à l'oracle) : plus aucune garantie. La garantie ne porte que sur le dommage visible par l'oracle.
  - Fausses alertes : elles ne cassent pas la garantie 2 (elles accélèrent l'annonce), mais elles cassent la garantie 1 (§2.3).
- **La dépendance passe par les tirages.**
  - Un audit qui a des suites visibles par l'agent (correction, ralentissement, signature réseau) révèle les tirages. Si cette révélation arrive avant que l'agent agisse sur les épisodes suivants, la garantie tient encore (tirages passés). S'il peut lier l'audit au type de tâche ou à l'instant, et donc prédire le tirage courant, elle tombe.
  - Une probabilité d'audit q_t qui dépend de signaux que l'agent influence (audit plus fréquent sur les tâches « suspectes ») sort de (H-a), sauf si q_t est 𝓕_{t−1}-mesurable et entre explicitement dans les facteurs du pari.
- **Latence de l'oracle.** Si le verdict de l'audit de l'épisode t n'arrive qu'à t + d, l'annonce est retardée d'au plus d épisodes. Le dommage accumulé augmente d'au plus d (moins en pratique : environ le taux réel fois d).
- **Agents en parallèle.** Si plusieurs copies agissent sur des épisodes simultanés, il faut ordonner les épisodes. (H-a) doit tenir pour chaque épisode conditionnellement à tout ce qui a été décidé avant son tirage.

## 4. Valeurs numériques (ρ₀ = 0,10, α = 0,05, β = 0,10)

Toutes les valeurs viennent de `sortie_calcul_regle_moniteur_invalide_v1.txt`. Hypothèse de lecture de la grille : arithmétique {1,25 ; 1,50 ; … ; 5,00} ρ₀, soit K = 16. Une variante géométrique à K = 5 et une grille descendante à K = 12 sont dans la sortie. La borne garantie est celle du §3.1 (probabilité ≥ 1 − β, horizon n, pour tout m < τ, sans le +1 de l'épisode d'annonce). « Atteint » désigne le quantile 1 − β de l'excès réalisé avant l'annonce par le meilleur attaquant à taux constant d'une grille de 24 taux, de 1,05 ρ₀ à 2,2 ρ₀ (1 000 répétitions) : c'est un **minorant** du pire cas.

### 4.1 Excès au-delà de ρ₀ n (en épisodes)

| q | n | ρ₀ n | Garanti, produit des moyennes | Atteint, produit des moyennes | Garanti, moyenne des produits | Atteint, moyenne des produits | Garanti, grille descendante | Atteint, grille descendante | Minorant, toute règle |
|---|---|---|---|---|---|---|---|---|---|
| 0,20 | 1 000 | 100 | 160,5 | 103,0 | 136,6 | 85,0 | 136,1 | 90,9 | 18 |
| 0,20 | 4 000 | 400 | 486,9 | 355,0 | 255,8 | 171,9 | 252,4 | 168,0 | 36 |
| 0,20 | 16 000 | 1 600 | 1 687,6 | 1 344,1 | 489,6 | 351,1 | 483,7 | 310,0 | 73 |
| 0,05 | 1 000 | 100 | 276,9 | 126,0 (*) | 322,4 | 129,0 (*) | 317,9 | 131,2 (*) | 55 |
| 0,05 | 4 000 | 400 | 662,8 | 443,0 (*) | 566,5 | 378,6 | 564,6 | 386,0 | 107 |
| 0,05 | 16 000 | 1 600 | 1 987,5 | 1 468,2 | 1 058,5 | 731,2 | 1 045,1 | 723,8 | 211 |

(*) Le meilleur taux trouvé est au bord de la grille simulée (2,2 ρ₀) : la valeur atteinte est sous-estimée.

Contrôle de cohérence : dans les dix-huit cases, l'excès atteint reste sous la borne garantie. À n = 16 000, le rapport garanti / atteint vaut 1,3 à 1,6 : la borne est donc assez serrée.
Excès garanti en part de n à n = 16 000 : produit des moyennes 0,105 (q = 0,20) et 0,124 (q = 0,05) ; moyenne des produits 0,031 et 0,066.
La forme fermée de Freedman (sortie, §2c) donne des bornes 1,1 à 1,6 fois plus larges. Par exemple, à q = 0,20, n = 16 000 : 1 909 pour le produit des moyennes, 791 pour la moyenne des produits.

Lecture :
- Avec le produit des moyennes, l'excès atteint suit l'excès garanti et reste linéaire. Le meilleur attaquant se tient vers 1,85 à 2 ρ₀, juste au-dessus du seuil de non-détection 1,91 ρ₀ : il est annoncé tard ou jamais.
- Avec le mélange, l'excès est de l'ordre de la racine de n sur cette plage.
- À q = 0,05 et n = 1 000, on n'a qu'une cinquantaine d'audits. Le minorant valable pour toute règle vaut déjà 55, environ la moitié de ρ₀ n, et la borne garantie dépasse 3 ρ₀ n.

### 4.2 Nombre d'audits avant l'annonce quand le taux réel vaut 2 ρ₀
Le nombre d'audits ne dépend pas de q. En épisodes, il vaut environ audits/q.

| Règle | Médiane des audits | Quantile 0,9 | Part sans annonce à 20 000 audits | Épisodes médians à q = 0,20 | Épisodes médians à q = 0,05 |
|---|---|---|---|---|---|
| Produit des moyennes, grille arithmétique (K = 16) | 61 | 642 | 0 | 305 | 1 220 |
| Moyenne des produits, grille arithmétique (K = 16) | 66 | 189 | 0 | 330 | 1 320 |
| Produit des moyennes, grille géométrique (K = 5) | 56 | 328 | 0 | 280 | 1 120 |
| Moyenne des produits, grille géométrique (K = 5) | 69 | 185 | 0 | 345 | 1 380 |
| Moyenne des produits, grille descendante (K = 12) | 94 | 209 | 0 | 470 | 1 880 |

Repère analytique, pour le produit des moyennes : la croissance par audit à r = 2 ρ₀ vaut 0,2 · log 3,125 + 0,8 · log(0,6875/0,9) = +0,0124. La dérive moyenne est donc faible. La médiane (61 audits) est pourtant basse, parce que chaque audit positif multiplie la richesse par 3,125 : quelques positifs rapprochés suffisent. La queue, en revanche, est lourde (quantile 0,9 de 642 audits, contre 189 pour le mélange). La meilleure dérive possible, celle du rapport au bon taux, vaut kl(0,2 ‖ 0,1) = 0,0444 par audit.

Couvrir la bande de non-détection a un prix. La grille descendante demande environ 40 % d'audits de plus en médiane à 2 ρ₀ (94 contre 66) : la masse du mélange est répartie sur des taux proches de ρ₀. C'est le compromis à trancher : détection rapide à 2 ρ₀, ou aucune bande où l'agent puisse s'installer.

## 5. Voisins : ce qui est classique, ce qui serait propre

**Classique** (aucune revendication possible) :
- Surmartingale positive et inégalité de Ville : Ville 1939. Rapport de vraisemblance séquentiel : Wald 1945. Mélange de rapports pour la validité à tout instant : Robbins, Darling et Robbins.
- Lecture « pari contre la nulle » : Shafer, « Testing by betting », journal de la Société royale de statistique, série A, 2021. Cadre de l'inférence valide à tout instant : Ramdas, Grünwald, Vovk, Shafer, *Statistical Science* 2023. Bornes de Chernoff et Freedman à tout instant : Howard, Ramdas, McAuliffe, Sekhon 2021.
- La nature adversative est elle aussi classique : dans la théorie des probabilités par les jeux (Shafer et Vovk), la « Réalité » choisit les issues de façon adaptative. La garantie 1 face à un agent adaptatif n'est donc que la garantie habituelle de ce cadre.
- **Surveillance séquentielle d'une dégradation de modèle** : Podkopaev et Ramdas, « Tracking the risk of a deployed model and detecting harmful distribution shifts », conférence ICLR 2022 (arXiv 2110.06177). Ils testent séquentiellement si un risque choisi (taux d'erreur) dépasse une tolérance, avec des suites de confiance valides à tout instant, et les étiquettes arrivent après coup. C'est notre test, ρ₀ tenant lieu de tolérance. Voisins de la même famille : détection de rupture par « e-détecteurs » (Shin, Ramdas, Rinaldo, arXiv 2203.03532) ; martingales conformes de test pour décider d'un réentraînement (Vovk et coauteurs).
- **Audit par pari** : « Auditing fairness by betting » (Chugg, Cortes-Gomez, Wilder, Ramdas, conférence NeurIPS 2023, arXiv 2305.17570). Il autorise une collecte par politique probabiliste plutôt qu'uniforme.
- **Audits limitant le risque (élections)** : RiLACS (Waudby-Smith, Stark, Ramdas, arXiv 2107.11323) et ALPHA (Stark). Ce sont des martingales de pari sur un échantillon tiré au hasard, face à un résultat qui peut être truqué. C'est le plus proche par l'esprit : un audit aléatoire secret comme seule prise sur un adversaire.
- **Pondération par une probabilité d'échantillonnage connue** dans les martingales : Waudby-Smith et coauteurs, « Anytime-valid off-policy inference for contextual bandits », arXiv 2210.10768.
- **Côté contrôle des systèmes d'IA** :
  - Wen et coauteurs, « Adaptive deployment of untrusted LLMs reduces distributed threats », conférence ICLR 2025, arXiv 2411.17693 : crédence bayésienne mise à jour sur une suite de tâches, cadre des menaces diffuses.
  - Analyse du contrôle séquentiel avec budget d'audit dans « Control Tax », arXiv 2506.05296.
  - Audit adaptatif valide à tout instant de systèmes génératifs (arXiv 2605.07002, conférence NeurIPS 2026) : d'après son résumé, l'adaptation y est du côté de l'auditeur, pas d'un système qui se cache.

**Voisin à vérifier en priorité (règle R8) : arXiv 2610.18948**, « Limits of Statistical Assurance for Embodied and Agentic AI under Adaptive Adversaries », déposé le 13 octobre 2026. Je n'ai vu que son résumé. Il dit proposer un moniteur à rapport de vraisemblance mélangé avec révocation définitive, qui borne l'excès cumulé de violations au-dessus d'un taux de référence à un ordre proche de la racine carrée, sur chaque trajectoire. Il traite aussi d'évaluateurs à aléa privé et d'un adversaire qui infère l'évaluation cachée. Si le PDF le confirme, la forme « excès cumulé borné en racine de n par un mélange » est occupée. Il faut le lire avant toute phrase de nouveauté.

**Ce qui serait propre à l'emploi contre un agent qui choisit** (à confirmer contre le voisin ci-dessus) :
1. **La condition exacte d'information** : la garantie survit à la vue des tirages passés et meurt à la prédiction du tirage courant (§2.3, §3.6). Elle sépare nettement ce qui doit rester secret (le tirage courant et le générateur) de ce qui peut fuir (les verdicts passés).
2. **La mesure de sortie** : le nombre d'épisodes endommagés et non signalés accumulés *avant l'annonce*, borné avec probabilité 1 − β contre *toute* politique. La littérature sur les ruptures mesure surtout le délai moyen de détection, ou le temps entre fausses alarmes, sous une alternative fixe. Contre un agent qui choisit son taux, le délai n'a pas de sens propre. Le dommage accumulé, si.
3. **La bande de non-détection** : (ρ₀, r*_min], où la richesse décroît, est l'endroit où un agent stratège s'installe. Le choix de la grille se juge sur cette bande, pas sur la puissance contre une alternative donnée. D'où la recommandation d'une grille qui descend vers ρ₀ et la mise en garde contre le produit des moyennes.
4. **L'ordre minimal √(n ρ₀(1−ρ₀)/q)** du dommage inévitable, qui chiffre le prix d'un taux d'audit faible. L'argument (Pinsker sur les seuls audits) est classique, mais son emploi comme budget de dommage du contrôle l'est peut-être moins.

## 6. Réserves
- Lecture de la grille : l'énoncé écrit « {1,25 ρ₀, …, 5 ρ₀} » sans donner le pas. J'ai pris le pas de 0,25 ρ₀ (K = 16). Les conclusions qualitatives (effondrement du produit des moyennes, bande de non-détection, pente limite 0,0121 tant que le plus petit taux vaut 1,25 ρ₀) ne dépendent pas du pas.
- La borne du §3.1 est garantie. La colonne « atteint » est un minorant obtenu par des attaquants à taux constant. Un attaquant non stationnaire pourrait faire un peu mieux, sans jamais dépasser la borne garantie. L'écart entre garanti et atteint vient du facteur λ fixé, du choix d'un seul k et de la queue de Ville.
- Le minorant « toute règle » utilise l'inégalité de Pinsker. Il est lâche d'un facteur proche de 2 à 3.
- L'ordre principal du §3.4 est une approximation gaussienne, pas une borne.
- Les voisins n'ont été lus qu'en résumé. Aucun de leurs chiffres n'est repris.
