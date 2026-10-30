## Titre
Trait linéaire en dernière position, cumulé sur les actions : domaine de puissance en Kullback-Leibler, extension par une seconde couche

## Classe de statistiques — (a)
Accès S(X, H_Π(X)), Π_T = {(t, ℓ_1, p_t) : t ≤ T}, p_t dernière position de l'action t, couche ℓ_1 fixée. Trait u_t = ⟨w, h_{t,ℓ_1,p_t}⟩ + b (maximum sur une seule position), accumulation S = Σ_{t ≤ T} u_t, décision par seuil. Étalonnage conforme sur n suites de référence tronquées à T actions : s_α est la k-ième plus petite valeur de S, k = ⌈(n + 1)(1 − α)⌉. Classe : {S_{w,b,ℓ_1}}. ψ désigne H_Π(X) ↦ (u_1, …, u_T). Pour (e), v_t = ⟨w', h_{t,ℓ_2,p_t}⟩ est lu à une couche ℓ_2 ≠ ℓ_1.

## Hypothèse porteuse — (b)
Indépendance conditionnelle entre actions : (H) sous P_0, pour tout t, la loi conditionnelle de (u_t, v_t) sachant a_<t ne dépend pas de a_<t, et Var(u_t), Var(v_t) ≤ σ̄². Les couples (u_t, v_t) sont alors indépendants entre actions, et μ_t = E_{P_0}[u_t | a_<t], ν_t = E_{P_0}[v_t | a_<t] ne dépendent pas de l'histoire. Le niveau n'en dépend pas ; la puissance de (c1) et le minorant de (e) en dépendent.

## Classe D de puissance garantie — (c1)
d : divergence de Kullback-Leibler KL(Q ‖ P). Régime T ε_T = ρ², ρ = 10 (ε_T = 100/T), T_0 = 400. D : lois Q_T diffuses telles que, pour tout t et toute histoire, (D1) E_{Q_T}[u_t | a_<t] ≥ μ_t + κ √ε_T, κ = 1,2 σ̄, et (D2) Var_{Q_T}(u_t | a_<t) ≤ σ̄². Pour tout T ≥ T_0, puissance de S sur D au moins 1 − β, β = 0,03, étalonnage compris ; seconde condition de diffusion avec c = 1,5 (preuves en (d)).

## Classe C de perte, et condition — (c2)
C : lois Q_T diffuses (même d, ε_T, T_0, c), de forme mélange par action (1 − π_T) P_0(a_t | a_<t) + π_T R_T(a_t | a_<t), π_T ∈ ]0, 1] et R_T déclarés, telles que (C1) ψ ∘ H_Π a même loi sous Q_T et sous P_0^(T), et (C2) E_{Q_T}[v_t | a_<t] ≥ ν_t + κ √ε_T, Var_{Q_T}(v_t | a_<t) ≤ σ̄². C est disjointe de D : sous C, E_{Q_T}[u_t] = μ_t.
Condition : si les lois images de Q_T et de P_0^(T) par H_Π ont la même image par ψ, alors S est indiscernable au niveau α avec δ = 0.

## Borne ou impossibilité — (d)
(d1) Pour T ≥ T_0 et Q_T vérifiant (C1), toute statistique fonction de (u_1, …, u_T) et de l'échantillon d'étalonnage, e-processus compris, a la même probabilité de rejet sous Q_T et sous P_0^(T) ; pour S, au plus 1 − k/(n + 1) ≤ α. Preuve : l'échantillon est indépendant de la suite lue, la loi jointe est donc la même ; sous P_0, les n + 1 valeurs sont échangeables (validité conforme).
(d2) On pose γ = α/2, z_γ = √((1 − γ)/γ), q = Σ_t μ_t + σ̄ √T z_γ. Sous (H), Var_{P_0}(S) ≤ T σ̄² et Cantelli donne P_0(S > q) ≤ γ ; s_α > q exige au moins n − k + 1 valeurs d'étalonnage au-dessus de q, probabilité au plus b_n = P(Bin(n, γ) ≥ n − k + 1). Sous Q_T ∈ D, S = Σ_t E_{Q_T}[u_t | a_<t] + M_T, M_T martingale de variance au plus T σ̄², et la somme des moyennes conditionnelles est au moins Σ_t μ_t + κρ√T. Cantelli : P_{Q_T}(S ≤ q) ≤ 1/(1 + r²), r = κρ/σ̄ − z_γ. Donc β ≤ b_n + 1/(1 + r²). Avec α = 0,05, n = 1 999 : k = 1 900, b_n < 10⁻⁹, z_γ = √39 ≈ 6,245, r ≈ 5,755, β ≤ 0,0294.
Diffusion : la variation totale entre Q_T et P_0^(T) est au moins Q_T(S > q) − P_0(S > q) ≥ 0,9457 ; par Pinsker, KL ≥ 2 × 0,9457² ≥ 1,78 ≥ c ; par la règle de chaîne, KL ≤ T ε_T = 100. De même sur C par (C2). Le cas où (H) cède reste ouvert.

## Statistique qui étend le domaine, et son prix — (e)
Π' = Π ∪ {(t, ℓ_2, p_t) : t ≤ T}, S_v = Σ_t v_t, S* = max(S − s_{α/2}, S_v − s^v_{α/2}), seuil 0, chaque seuil conforme au niveau α/2 (k' = 1 950) ; même classe ; niveau au plus α par réunion, δ = 0.
Minorant uniforme sur C, T ≥ T_0 : 1 − b'_n − 1/(1 + (κ √(T ε_T)/σ̄ − z_{α/4})²), b'_n = P(Bin(n, α/4) ≥ n − k' + 1) ; d entre par ε_T, c n'est qu'une contrainte entraînée par (C2). Ici κ √(T ε_T)/σ̄ = 12, z_{α/4} = √79 ≈ 8,888, b'_n < 10⁻⁵ : minorant 0,906.
Prix, à α et T fixés : contre D, le minorant garanti passe de 0,97 à 0,906 ; contre la classe D_3 (D avec κρ/σ̄ = 3, (D1) et (D2) en égalités, loi des v_t inchangée), sous approximation normale (Φ : fonction de répartition normale centrée réduite), S a la puissance Φ(3 − 1,645) ≈ 0,912 et S* entre Φ(3 − 1,960) ≈ 0,851 et 0,876 : perte entre 0,036 et 0,061.

## Test — (f)
- n_tot = 3 000 suites de référence d'au moins 400 actions, partagées au hasard : 1 999 d'étalonnage, bassin disjoint de 1 001 pour les déplacements synthétiques ; T = 400. w, w' tirés sur la sphère unité avant lecture, b = 0 ; σ̄² = 1,2 fois la plus grande variance empirique de u_t, v_t sur le bassin.
- Bras niveau : rejet de S et S* sur les 1 001 suites du bassin.
- Bras D, rééchantillonnage pondéré : 2 000 suites, chacune issue d'une suite du bassin tirée au hasard, où chaque u_t est remplacé par un tirage parmi les u_t du bassin, poids ∝ exp(θ u), déplacement moyen κ √ε_T = 0,6 σ̄.
- Bras C, couplage : 2 000 suites ; (u_1, …, u_T) d'une suite du bassin est gardée ; chaque v_t est tiré parmi les v_t des 20 suites du bassin dont le u_t est le plus proche, poids ∝ exp(θ' v), déplacement moyen 0,6 σ̄.
- Ces bras modifient les traits, non les textes : approximation SUPPOSÉ, hors de l'image garantie de X ↦ H(X).
- Graines : numpy.random.SeedSequence, racine 27 182, une graine dérivée par tâche.
- Attendu : niveau ≤ 0,05 ; puissance de S au bras D ≥ 0,97 ; rejet de S au bras C égal au bras niveau ; puissance de S* au bras C ≥ 0,906.
- Résultats qui réfutent (d) : rejet de S au bras niveau > 0,08 ; (g) confirmée et puissance de S au bras D < 0,95. Résultat qui réfute (e) : (g) confirmée et puissance de S* au bras C < 0,88.
- Première expérience sur processeur seul.

## Quantité de diagnostic — (g)
Γ_Q = max(|ḡ_u|, |ḡ_v|), ḡ_u = (1/(T − 1)) Σ_{t=2}^{T} Corr_{Q_T}(u_t, u_{t−1}), ḡ_v de même, T = 400, pour une loi Q_T de D de la forme Q_T(a_t | a_<t) = P_0(a_t | a_<t) g_t(u_t), g_t ≥ 0 d'espérance 1 sous P_0. Sous (H), les couples (u_t, v_t) restent indépendants entre actions sous une telle Q_T, et Γ_Q = 0 ; (g) n'est qu'une condition nécessaire de (H). Estimateur : corrélations empiriques sur n_Q = 1 001 suites indépendantes observées sous Q_T. Intervalle : bootstrap percentile par suites, 2 000 tirages, 95 %. v_1 = 0,05 confirme, v_2 = 0,20 infirme : confirmée si l'intervalle est entièrement du côté de v_1 opposé à v_2, v_1 comprise (dans [0 ; 0,05]) ; infirmée s'il est entièrement du côté de v_2 opposé à v_1, v_2 comprise (dans [0,20 ; 1]) ; indéterminée sinon.

## Prédiction
Puissance de S* au bras C : 0,99, au-dessus du minorant 0,906.

## Coût
Environ 70 heures-cœur de processeur et 3 dollars, presque tout pour la lecture par M (deux couches, une passe).

## Antériorités
1. « Algorithmic Learning in a Random World », V. Vovk, A. Gammerman, G. Shafer, 2005 : validité en échantillon fini des p-valeurs conformes sous échangeabilité.
2. « Elements of Information Theory » (2e édition), T. M. Cover, J. A. Thomas, 2006 : inégalité de Pinsker, règle de chaîne de la divergence de Kullback-Leibler, inégalité de traitement des données.

## Critère de mort
(g) confirmée et puissance de S* au bras C sous 0,88 : le minorant de (e) est abandonné. Rejet de S au bras niveau au-dessus de 0,08, ou (g) confirmée et puissance de S au bras D sous 0,95 : la borne de (d) est abandonnée.

## SUPPOSÉ
- Valeurs fixées par la fiche : α = 0,05, δ = 0, β = 0,03, ρ = 10, κ = 1,2 σ̄, T_0 = T = 400, c = 1,5, n = 1 999, n_tot = 3 000, n_Q = 1 001, facteur 1,2, 20 voisins, 2 000 suites par bras et tirages, v_1 = 0,05, v_2 = 0,20, seuils 0,08, 0,95, 0,88 (environ trois erreurs de tirage), racine 27 182 ; les autres nombres en sont calculés.
- C non vide pour M : non démontré. D non vide : en loi normale de variance σ̄², un déplacement de moyenne 0,6 σ̄ est à divergence 0,18 ≤ ε_400 = 0,25.
- Approximation normale, à étalonnage exact, du prix contre D_3.
- Coût : 20 symboles par action, 100 symboles par seconde et par cœur, 0,04 dollar l'heure-cœur.
