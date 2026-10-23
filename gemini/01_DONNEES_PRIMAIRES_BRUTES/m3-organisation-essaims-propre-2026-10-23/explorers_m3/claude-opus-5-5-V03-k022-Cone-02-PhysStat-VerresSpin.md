BASSIN_MATH: Loi du Potentiel de Franz-Parisi à Couplage Épistémique (FP-ε)

LOI_PROPOSEE: Chaque agent a produit des verdicts σ_a ∈ {±1}^N sur N affirmations, notés par jev. On définit le recouvrement q_ab = N⁻¹Σ_i σ_a^i σ_b^i et le potentiel V_ε(q̃) = −(βN)⁻¹ ln Σ_σ e^{−βH(σ)} δ(q(σ,σ_ref) − q̃). La règle de spawn est : si ∂²V/∂q̃² < 0 et ΔV = V(q_min,2) − V(q_ref) < θ·c_appel, alors on lance un explorateur ancré en q_min,2. Si la variance Var_P(q) intra-famille dépasse la variance inter-familles, alors on lance un démolisseur chimérique.

1. **Auto-organisation hors-poids**
Chaque cycle produit un consensus σ_ref. On estime V_ε empiriquement en relançant des agents sous une pénalité textuelle ε·(1 − q) qui les force à rester proches de σ_ref, avec ε décroissant.
- **Minimum unique (phase RS)** : le paysage est simple. On contracte l'essaim vers une monoculture bon marché, Gemini en priorité.
- **Second minimum métastable (transition dynamique T_d, 1RSB)** : un explorateur est envoyé dans cette vallée.
- **Distribution P(q) bimodale intra-famille (H4')** : un Red-Team d'une autre famille de poids est spawné.

La topologie de communication J_ab suit l'équation TAP avec réaction d'Onsager : m_a = tanh(β Σ_b J_ab m_b − β² m_a Σ_b J_ab²(1 − m_b²)). Le terme d'Onsager soustrait l'écho de l'agent lui-même dans ses délégués, ce qui borne la dérive de consigne (H9). On ne garde un lien a→b que si |J_ab| survit au seuil d'Almeida-Thouless. L'apprentissage est entièrement externe : les J_ab, θ et l'historique de V sont stockés en mémoire et ne modifient aucun poids.

2. **Objectif et anti-Goodhart**
R = Acc_jev(canaris cachés et tournants) − λ₁·(q̄_intra − q̄_inter)₊ − λ₂·Rec − λ₃·$/$_budget.
- **Rec** est la fraction d'affirmations sans DOI vérifiable via Crossref ou Semantic Scholar, ce qui pénalise la récitation de la mémoire paramétrique.
- **Les canaris** forment un ensemble invisible pour les agents, renouvelé à chaque cycle.
- **Le juge jev** n'est jamais exposé au gradient de prompt, ce qui limite l'effet Goodhart.
- **Le budget** est réparti à proportion de ∂R/∂$ par famille, sous les plafonds 100 USD (Claude) et 20 USD (Gemini).

3. **Duel décisif (H_A ⊥ H_B)**
Le budget est constant à 120 USD et réparti entre quatre bras pré-enregistrés de même coût :
- **(A)** FP-ε adaptatif ;
- **(B)** topologie fixe chimérique ;
- **(C)** échantillonnage i.i.d. avec vote majoritaire ;
- **(D)** contrôle négatif : FP-ε avec matrice q_ab permutée aléatoirement, donc des spawns sans structure.

Le corpus compte 300 questions bibliographiques à vérité jev cachée.

Hypothèses :
- **H_A** : Acc(A) > max(B, C, D) et la corrélation des erreurs ρ_err(A) est inférieure de 30 %.
- **H_B** : le gain disparaît en D, ce qui prouve que la structure du paysage, et non la seule chimère, est causale.

Le test est un bootstrap apparié avec α = 0,01. La réfutation est acquise si D ≈ A.
