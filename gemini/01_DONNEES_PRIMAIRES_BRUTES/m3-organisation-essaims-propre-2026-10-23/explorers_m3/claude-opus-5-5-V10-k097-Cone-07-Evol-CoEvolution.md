BASSIN_MATH: Amplificateur de Lieberman-Nowak piloté par Price (ALN-P)

LOI_PROPOSEE: ẋᵢ = Σⱼ xⱼ wⱼ Q_ji(G) − xᵢ w̄. G passe en étoile (amplificateur) si |Cov(w,z)| > |E(wΔz)|, et en cycle (suppresseur) sinon. La probabilité de fixation vaut ρ_G(r) ≈ ρ_Moran(r^K), avec K=2 pour l'étoile et K=1 pour le cycle.

**1. Mécanisme d'auto-organisation hors-poids**

Un génotype est un triplet g = (consigne, rôle, famille f), avec f ∈ {fable, opus, argon}. Le graphe G définit qui transmet sa consigne à qui. Une mutation Q réécrit la consigne d'un agent ou change sa famille.

À chaque époque, on décompose le changement du trait moyen z̄ (qualité vérifiée) par l'équation de Price : Δz̄ = Cov(w,z)/w̄ + E(wΔz)/w̄.

- **Sélection dominante** (Cov > E) : on bascule G en étoile. Cela amplifie la sélection et accélère la fixation des bonnes consignes.
- **Transmission dominante** : le terme E(wΔz) mesure la dérive de consigne à travers les délégations (H9). On bascule G en cycle, ce qui supprime la sélection. On plafonne aussi la profondeur de délégation à 1.

Le spawn suit la co-évolution Red Queen :
- un **démolisseur** naît quand le taux de réussite des parasites archivés tombe sous 0,2 ;
- un **explorateur** naît quand des cellules MAP-Elites restent vides.

Les descripteurs MAP-Elites sont des coordonnées de comportement calculées gratuitement par jev-1.14.0.

L'arbitrage entre monoculture et chimère se fait par fitness fréquence-dépendante. Chaque famille paie −λ·ρ̂_err(f), où ρ̂_err(f) est la corrélation de ses erreurs intra-famille (H4'). Les chimères émergent donc dès que ρ̂_err(f) > ρ̂_err(inter-familles).

**2. Fonction objectif et anti-Goodhart**

wᵢ = q̂ᵢ^HoF − λ ρ̂_err(fᵢ) + μ·𝟙[cellule nouvelle] − ν·R̂ᵢ − κ·coûtᵢ/budget_f

- **q̂ᵢ^HoF** : taux de survie face au Hall of Fame des parasites passés. Ce score est tiré au hasard et caché, ce qui empêche les cycles de dominance.
- **R̂ᵢ** : fraction de références non résolues via Crossref, arXiv ou Semantic Scholar. Elle pénalise la récitation de la mémoire paramétrique.
- **Rôle de jev** : il sert de descripteur, jamais de récompense. Le juge reste un panel tournant renouvelé à chaque époque, ce qui contre la loi de Goodhart.

Les budgets sont alloués proportionnellement à x_f·w̄_f, sous les contraintes de 100 USD pour Claude et 20 USD pour Gemini.

**3. Duel décisif (H_A ⊥ H_B)**

Le budget est constant pour tous les bras : 100 USD Claude et 20 USD Gemini, sur 30 graines et 40 tâches pré-enregistrées.

- **H_A** : ALN-P.
- **H_B** : essaim à étoile fixe.
- **H_C** : best-of-N i.i.d. avec le même nombre d'appels.
- **Contrôle négatif** : ALN-P dont le signal de Price est permuté entre les époques.

La métrique est le nombre d'hypothèses vérifiées, nouvelles et à références résolues, par dollar. Elle est évaluée par des parasites tenus hors échantillon, générés par un tiers.

La loi est validée si trois conditions sont réunies (test de Wilcoxon apparié, correction de Holm, α = 0,01) :
- H_A bat H_B et H_C ;
- le contrôle permuté reste au niveau de H_B ;
- ρ̂_err(H_A) < ρ̂_err(H_B).

Elle est réfutée si le contrôle permuté égale H_A.
