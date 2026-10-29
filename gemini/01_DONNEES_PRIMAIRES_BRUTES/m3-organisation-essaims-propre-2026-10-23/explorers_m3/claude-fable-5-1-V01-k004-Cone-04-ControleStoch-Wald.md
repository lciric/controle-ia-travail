BASSIN_MATH: Essaim-Wald-Particulaire (EWP)
LOI_PROPOSEE: π* = argmax_π E[Σ_t R_t − λ·c(a_t)] avec arrêt SPRT par agent : continuer si A < Λ_t = Σ log[p(y|H₁)/p(y|H₀)] < B ; mutation topologique si CUSUM S_t = max(0, S_{t−1} + ℓ_t − k) > h ; allocation par bandit contextuel non-stationnaire (Sliding-UCB) ; état latent (compétence, dérive) estimé par filtre particulaire.

**1. Mécanisme d'auto-organisation hors-poids**
L'essaim est un graphe G_t = (V_t, E_t) dont la topologie est une variable de contrôle. Chaque arête (i→j) porte une posterior particulaire {w_k, θ_k} sur l'état caché θ_j = (compétence, dérive de consigne H9, taux de récitation). Le bandit contextuel choisit à chaque pas quel agent/famille activer : bras = (modèle, rôle ∈ {explorateur, démolisseur}, topologie), contexte = embeddings `jev-1.14.0` de la tâche. Règles de mutation :
- SPRT par sous-tâche : Λ_t franchit B ⇒ accepter la sortie ; franchit A ⇒ spawner un démolisseur Red-Team (coût marginal nul via jev).
- CUSUM sur la divergence consigne-initiale/consigne-courante (mesurée par jev) : dépassement de h ⇒ recâblage (réinjection de la consigne racine, suppression de l'arête dérivante).
- Arbitrage monoculture/chimère : le bandit maintient une estimation de corrélation ρ des erreurs (H4') ; si ρ̂ > ρ* sur la fenêtre glissante, pénalité additive forçant la diversification inter-familles.
Budget : contrainte Lagrangienne λ_Claude, λ_Gemini mise à jour par descente duale pour respecter 100/20 USD.

**2. Fonction objectif anti-Goodhart**
R_t = q_jev(y_t) − α·ρ̂_t(H4') − β·D_KL(consigne_t ∥ consigne_0) − γ·𝟙[récitation] − λ·c_t
où q_jev est le score du classifieur non génératif, la récitation est détectée par recouvrement n-gram avec arXiv/Semantic Scholar, et la pénalité Goodhart est renforcée par un juge randomisé (jev avec seuil bruité ε) rendant R_t non directement optimisable par imitation.

**3. Duel décisif H_A ⊥ H_B**
H_A : l'EWP bat l'essaim fixe. H_B : équivalence (contrôle négatif i.i.d. à budget identique, tirages uniformes d'agents, topologie figée). Protocole : 200 tâches appariées, trois bras (EWP, fixe, i.i.d.), budget 120 USD partitionné égal. Test séquentiel de Wald sur la différence ΔR avec α = β = 0,05 ; arrêt dès |Λ| > log(19). Succès déclaré si EWP > fixe ET > i.i.d., corrélation d'erreurs ρ̂ réduite d'au moins 30 %, et dérive H9 mesurée par CUSUM inférieure au seuil h sur 90 % des trajectoires. Échec d'une seule condition ⇒ rejet de la loi.
