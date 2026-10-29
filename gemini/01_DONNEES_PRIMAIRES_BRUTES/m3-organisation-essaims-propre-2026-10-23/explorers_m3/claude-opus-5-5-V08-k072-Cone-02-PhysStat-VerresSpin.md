BASSIN_MATH: Fission Hopfield-AGS à Capacité Critique (FHAGS-αc)

LOI_PROPOSEE: Un sous-essaim de N agents stocke P stratégies ξ^μ (explorer, démolir, vérifier, sourcer). Sa capacité effective est N_eff = N/[1+(N−1)ρ̄], où ρ̄ est la corrélation d'erreurs mesurée par jev. La charge vaut α = P/N_eff. Si α > α_c(T) ≈ 0,138·(1−T²) (ligne Amit-Gutfreund-Sompolinsky), l'essaim fissionne. Sinon, il récupère les stratégies via TAP.

**1. Mécanisme d'auto-organisation et d'entraînement hors-poids**

- **Mémoire de l'essaim.** L'« entraînement » est une mémoire de Hopfield externe, sans modification des poids : J_ij = (1/N) Σ_μ r_μ ξ_i^μ ξ_j^μ, où r_μ est la récompense validée de la stratégie μ.
- **Division des tâches.** Pour chaque sous-tâche, on résout TAP : m_i = tanh(β Σ_j J_ij m_j − β²α(1−q)/[1−β(1−q)] · m_i). Le terme d'Onsager retire l'auto-écho, c'est-à-dire la réaffirmation de l'agent par lui-même. La stratégie assignée est argmax_μ m_μ.
- **Détection des états parasites.** Un recouvrement mixte (plusieurs m_μ ≈ 1/√3) signale une récitation paramétrique ou une dérive de consigne (H9). Il déclenche le spawn d'un démolisseur Red-Team, et non d'un explorateur.
- **Fission.** Quand α > α_c, on évite la catastrophe de confusion du verre. On scinde l'essaim en recrutant l'agent de la famille qui minimise ρ avec le noyau, souvent Gemini, ce qui produit une chimère. Ou bien on applique un désapprentissage de Hopfield-Feinstein-Palmer aux stratégies de r_μ minimal.
- **Choix monoculture ou chimère.** On garde la monoculture tant que α < α_c, car elle est moins chère. On passe à la chimère seulement quand c'est nécessaire.
- **Topologie.** Seules les arêtes vérifiant |J_ij| > 1/√N communiquent.
- **Budget.** La température d'inférence T est réglée par le budget restant : T = 1 − B_restant/B₀, avec 100 USD Claude et 20 USD Gemini. Le refroidissement réduit α_c et force la parcimonie.

**2. Fonction objectif et anti-Goodhart**

R = V_ext − λ·ρ̄ − κ·Coût − ν·|S_jev − S_audit|

- V_ext : validité sur des canaris scellés, vérifiée par Crossref ou Semantic Scholar (existence et contenu des citations).
- S_audit : audit croisé d'une autre famille sur un échantillon aléatoire de 10 %.
- Anti-Goodhart : le dernier terme pénalise l'écart entre le juge jev et l'audit. En complément, le seuil de jev est randomisé à chaque époque, et r_μ n'est jamais calculé à partir de jev seul.

**3. Duel décisif (H_A ⊥ H_B), budget constant de 120 USD**

- **H_A (capacité).** Le gain provient de la fission déclenchée à α_c.
- **H_B (diversité brute).** Le gain provient seulement du mélange des familles.

Bras expérimentaux, chacun sur 40 tâches à P croissant :

| Bras | Description |
|---|---|
| A | FHAGS-αc |
| B | Topologie fixe chimérique |
| C | Contrôle négatif i.i.d. : même nombre de fissions, mais à des instants tirés au hasard, ρ̄ étant permuté |
| D | Monoculture fixe |

Prédictions discriminantes :

- **Sous H_A**, la précision des bras B et D chute brutalement (transition du premier ordre) à P/N_eff ≈ 0,14, tandis que le bras A reste plat. Le bras C affiche le même nombre de fissions que A mais conserve la chute.
- **Sous H_B**, le déclin est lisse et l'on observe A ≈ C ≈ B.

Statistiques : on ajuste un modèle segmenté au point de rupture α*. H_A est réfutée si l'intervalle de confiance à 95 % de α* exclut [0,10 ; 0,18], ou si A − C ≤ 0 selon un test de permutation (p > 0,05).
