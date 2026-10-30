## Titre
Somme de traits linéaires pris au maximum : puissance sous indépendance entre actions, perte quand la loi du trait est conservée

## Classe de statistiques — (a)
Accès S(X, H_Π(X)), Π_T = {(t, ℓ*, p) : t ≤ T, p position de l'action t}, couche ℓ* fixée. Trait u_t = max_p ⟨w, h_{t,ℓ*,p}⟩ (maximum dans l'action), accumulation S_w = Σ_{t ≤ T} u_t. Étalonnage conforme sur n suites de référence tronquées à T actions : s_α est la k-ième plus petite valeur de S_w, k = ⌈(n + 1)(1 − α)⌉ ; rejet si S_w > s_α. La classe est {S_w : w, ℓ*}. φ_w désigne H_Π(X) ↦ (u_1, …, u_T) ; u'_t, S_{w'} sont les mêmes objets pour un vecteur w' non colinéaire à w, employé en (e).

## Hypothèse porteuse — (b)
(H) Sous P_0, pour tout t, la loi conditionnelle de (u_t, u'_t) sachant a_<t ne dépend pas de a_<t, et Var(u_t), Var(u'_t) ≤ σ̄². Les couples (u_t, u'_t) sont alors indépendants entre actions, et μ_t := E_{P_0}[u_t | a_<t] ne dépend pas de l'histoire (de même μ'_t). Le niveau n'en dépend pas ; la puissance de (c1) et le minorant de (e) en dépendent.

## Classe D de puissance garantie — (c1)
d : Hellinger, H²(P, Q) = 1 − ∫√(dP dQ). Régime ε_T = ρ/√T (T ε_T² = ρ²), ρ = 5, T_0 = 400. D : lois Q_T diffuses telles que, pour tout t et toute histoire, (D1) E_{Q_T}[u_t | a_<t] ≥ μ_t + κ ε_T, κ = 2,4 σ̄, et (D2) Var_{Q_T}(u_t | a_<t) ≤ σ̄². Pour tout T ≥ T_0, puissance de S_w sur D au moins 1 − β, β = 0,03, étalonnage compris ; la seconde condition de diffusion tient avec c = 0,6 (preuves en (d)).

## Classe C de perte, et condition — (c2)
C : lois Q_T diffuses (même d, ε_T, T_0, c), de forme mélange par action (1 − π_T) P_0(a_t | a_<t) + π_T R_T(a_t | a_<t), π_T ∈ ]0, 1] et R_T déclarés, telles que (C1) φ_w ∘ H_Π a même loi sous Q_T et sous P_0^(T), et (C2) E_{Q_T}[u'_t | a_<t] ≥ μ'_t + κ ε_T, Var_{Q_T}(u'_t | a_<t) ≤ σ̄². C et D sont disjointes : E_{Q_T}[u_t] = μ_t sous C, ≥ μ_t + κ ε_T sous D.
Condition : si les lois images de Q_T et de P_0^(T) par H_Π ont la même image par φ_w, alors S_w est indiscernable au niveau α avec δ = 0.

## Borne ou impossibilité — (d)
(d1) Pour T ≥ T_0 et Q_T vérifiant (C1), toute statistique fonction de (u_1, …, u_T) et de l'échantillon d'étalonnage, e-processus compris, a la même probabilité de rejet sous Q_T et sous P_0^(T) ; pour S_w, au plus 1 − k/(n + 1) ≤ α. Preuve : l'échantillon est indépendant de la suite lue, la loi jointe est donc la même ; sous P_0, les n + 1 valeurs sont échangeables (validité conforme).
(d2) On pose γ = α/2, z_γ = √((1 − γ)/γ), q = Σ_t μ_t + σ̄ √T z_γ. Sous (H), Var_{P_0}(S_w) ≤ T σ̄² et Cantelli donne P_0(S_w > q) ≤ γ ; s_α > q exige au moins n − k + 1 valeurs d'étalonnage au-dessus de q, de probabilité au plus b_n = P(Bin(n, γ) ≥ n − k + 1). Sous Q_T ∈ D, S_w = Σ_t E_{Q_T}[u_t | a_<t] + M_T, M_T martingale de variance au plus T σ̄², et la somme des moyennes conditionnelles est au moins Σ_t μ_t + κρ√T. Cantelli : P_{Q_T}(S_w ≤ q) ≤ 1/(1 + r²), r = κρ/σ̄ − z_γ. Donc β ≤ b_n + 1/(1 + r²). Avec α = 0,05, n = 999 : k = 950, b_n < 10⁻⁵, z_γ = √39 ≈ 6,245, r ≈ 5,755, β ≤ 0,0294.
Diffusion : la variation totale entre Q_T et P_0^(T) est au moins Q_T(S_w > q) − P_0(S_w > q) ≥ 0,9707 − 0,025 = 0,9457, et au plus √2 H, d'où H ≥ 0,668 ≥ c ; de même sur C par (C2). Le cas où (H) cède reste ouvert.

## Statistique qui étend le domaine, et son prix — (e)
S* = max(S_w − s_{α/2}, S_{w'} − s'_{α/2}), seuil 0, chaque seuil conforme au niveau α/2 (k' = 975) ; même classe ; niveau au plus α par réunion, δ = 0.
Minorant uniforme sur C, T ≥ T_0 : 1 − b'_n − 1/(1 + (κ √T ε_T/σ̄ − z_{α/4})²), b'_n = P(Bin(n, α/4) ≥ n − k' + 1) ; d entre par ε_T, c n'est qu'une contrainte entraînée par (C2). Ici κ √T ε_T/σ̄ = 12, z_{α/4} = √79 ≈ 8,888, b'_n ≈ 0,0011 : minorant 0,905.
Prix, à α et T fixés : contre D, le minorant garanti passe de 0,97 à 0,905 ; contre la classe D_3 (D avec κρ/σ̄ = 3, (D1) et (D2) en égalités, loi des u'_t inchangée), sous approximation normale (Φ : fonction de répartition normale centrée réduite), S_w a la puissance Φ(3 − 1,645) ≈ 0,912 et S* entre Φ(3 − 1,960) ≈ 0,851 et 0,876 : perte entre 0,036 et 0,061.

## Test — (f)
- n_tot = 2 000 suites de référence d'au moins 400 actions, partagées au hasard : 999 d'étalonnage (aussi pour (g)), bassin disjoint de 1 001 pour les déplacements synthétiques ; T = 400. w, w' tirés sur la sphère unité avant lecture ; σ̄² = 1,2 fois la plus grande variance empirique de u_t, u'_t sur le bassin.
- Bras niveau : rejet de S_w et S* sur les 1 001 suites du bassin.
- Bras D, rééchantillonnage pondéré : 2 000 suites, chacune issue d'une suite du bassin tirée au hasard, où chaque u_t est remplacé par un tirage parmi les u_t du bassin, poids ∝ exp(θ u), déplacement moyen κ ε_T = 0,6 σ̄.
- Bras C, couplage : 2 000 suites ; (u_1, …, u_T) d'une suite du bassin est gardée ; chaque u'_t est tiré parmi les u'_t des 20 suites du bassin dont le u_t est le plus proche, poids ∝ exp(θ' u'), déplacement moyen 0,6 σ̄.
- Ces bras modifient les traits, non les textes : approximation SUPPOSÉ, hors de l'image garantie de X ↦ H(X).
- Graines : numpy.random.SeedSequence, racine 61 803, une graine dérivée par tâche.
- Attendu : niveau ≤ 0,05 ; puissance de S_w au bras D ≥ 0,97 ; rejet de S_w au bras C égal au bras niveau ; puissance de S* au bras C ≥ 0,905.
- Résultats qui réfutent (d) : rejet de S_w au bras niveau > 0,08 ; (g) confirmée et puissance de S_w au bras D < 0,95. Résultat qui réfute (e) : (g) confirmée et puissance de S* au bras C < 0,88.
- Première expérience sur processeur seul.

## Quantité de diagnostic — (g)
Λ = max(|log V|, |log V'|), V = Var_{P_0}(Σ_t u_t) / Σ_t Var_{P_0}(u_t), V' de même pour u'_t, T = 400. Sous (H), Λ = 0 ; (g) n'est qu'une condition nécessaire de (H). Estimateur : variances empiriques sur les n = 999 suites d'étalonnage. Intervalle : bootstrap percentile par suites, 2 000 tirages, 95 %. v_1 = 0,15 confirme, v_2 = 0,40 infirme : confirmée si l'intervalle est entièrement du côté de v_1 opposé à v_2, v_1 comprise (dans [0 ; 0,15]) ; infirmée s'il est entièrement du côté de v_2 opposé à v_1, v_2 comprise (dans [0,40 ; +∞[) ; indéterminée sinon.

## Prédiction
Puissance de S* au bras C : 0,99, au-dessus du minorant 0,905.

## Coût
Environ 50 heures-cœur de processeur et 2 dollars, presque tout pour la lecture par M.

## Antériorités
1. « Algorithmic Learning in a Random World », V. Vovk, A. Gammerman, G. Shafer, 2005 : validité en échantillon fini des p-valeurs conformes sous échangeabilité.
2. « Nonparametric Goodness-of-Fit Testing Under Gaussian Models », Yu. I. Ingster, I. A. Suslina, 2003 : frontières minimax de détection en modèle gaussien.
3. « Understanding intermediate layers using linear classifier probes », G. Alain, Y. Bengio, 2016 : montre empiriquement que des traits linéaires lus par couche séparent des classes.

## Critère de mort
(g) confirmée et puissance de S* au bras C sous 0,88 : le minorant de (e) est abandonné. Rejet de S_w au bras niveau au-dessus de 0,08, ou (g) confirmée et puissance de S_w au bras D sous 0,95 : la borne de (d) est abandonnée.

## SUPPOSÉ
- Valeurs fixées par la fiche : α = 0,05, δ = 0, β = 0,03, ρ = 5, κ = 2,4 σ̄, T_0 = T = 400, c = 0,6, n = 999, n_tot = 2 000, facteur 1,2, 20 voisins, 2 000 suites par bras et tirages, v_1 = 0,15, v_2 = 0,40, seuils 0,08, 0,95, 0,88 (environ trois erreurs de tirage), racine 61 803 ; les autres nombres en sont calculés.
- C non vide pour M : non démontré. D non vide : en loi normale de variance σ̄², un déplacement de moyenne 0,6 σ̄ est à Hellinger 0,21 ≤ ε_400 = 0,25.
- Approximation normale, à étalonnage exact, du prix contre D_3.
- Coût : 20 symboles par action, 100 symboles par seconde et par cœur, 0,04 dollar l'heure-cœur.
