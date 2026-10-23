BASSIN_MATH: Médiateur Swap-Regret à Équilibre Corrélé Bayésien (MSR-ECB)

LOI_PROPOSEE: π* = argmax_π Σ_θ μ_t(θ) Σ_a π(a|θ)·W(a,θ), sous la contrainte d'obéissance ∀i, ∀a_i, ∀a_i′ : Σ_{θ,a₋ᵢ} μ_t(θ)·π(a|θ)·[u_i(a,θ) − u_i(a_i′,a₋ᵢ,θ)] ≥ 0, et sous la contrainte budgétaire Σ_a π(a|θ)·c_f(a) ≤ B_f pour f ∈ {Claude, Gemini}.

Ici, θ désigne l'état latent de la tâche, μ_t la croyance a posteriori et a le profil des rôles.

**1. Mécanisme d'auto-organisation hors-poids**

Un médiateur non génératif, qui est la mémoire externe de l'essaim, observe un signal de tâche θ̂. Il recommande ensuite en privé à chaque agent son rôle a_i parmi les suivants : explorateur, démolisseur Red-Team, vérificateur bibliographique ou silence.

La recommandation porte aussi sur la famille de poids : fable-5-1, opus-5-5 ou argon. La topologie « qui parle à qui » est le support de π. Une arête i→j n'existe que si leurs rôles sont corrélés positivement dans π.

Chaque agent ne garde en contexte que sa recommandation et un tableau de regrets. Il exécute un algorithme de minimisation du regret d'échange (Blum-Mansour). La distribution empirique des profils converge alors vers un équilibre corrélé bayésien (Bergemann-Morris). C'est ainsi que l'essaim apprend sans modifier ses poids.

Le choix entre monoculture et chimère est endogène. Le médiateur ne recommande une paire de même famille que si W y reste supérieur après la pénalité de corrélation κ·ρ̂, ce qui traite le risque H4′.

Un démolisseur est généré lorsque l'obéissance de l'explorateur devient presque saturée, c'est-à-dire lorsque la confiance est trop élevée pour l'information disponible.

**2. Fonction objectif et anti-Goodhart**

R_i = (𝟙[audit]/q)·(1 − ‖p_i − y‖²) − κ·Σ_j ρ̂(e_i,e_j) − λ_f·c_i − η·D_jev(consigne_k, consigne_0)

- **Score de Brier propre (q tiré secrètement)** : il est calculé sur des vérités vérifiables, à savoir des DOI et identifiants arXiv résolus via Crossref et Semantic Scholar. Il ne repose jamais sur un juge LLM. La réponse sincère p_i reste ainsi optimale, ce qui contrecarre la loi de Goodhart sur le juge.
- **Pénalité de récitation** : toute affirmation sans DOI résolu vaut y = 0, ce qui neutralise la récitation de la mémoire paramétrique.
- **Pénalité de dérive (H9)** : D_jev est la divergence de consigne mesurée à chaque délégation par jev-1.14.0, à coût nul.

**3. Duel décisif (H_A ⊥ H_B) à budget constant**

Trois bras disposent chacun de 100 USD Claude et 20 USD Gemini, sur N = 200 tâches de revue pré-enregistrées :

| Bras | Configuration |
|---|---|
| A | MSR-ECB |
| B | Topologie fixe, pipeline explorateur→critique |
| C (contrôle négatif) | Rôles i.i.d., tirés indépendamment selon les marginales exactes de π* apprises en A |

Les deux hypothèses rivales sont :
- **H_A** : le gain provient de la corrélation des rôles, ce qui prédit A > C ≈ B.
- **H_B** : le gain provient seulement des marginales, ce qui prédit A ≈ C > B.

Le critère principal est le nombre d'hypothèses nouvelles vérifiées par dollar. Les critères secondaires sont ρ̂ inter-agents et D_jev cumulée.

L'analyse repose sur un test de permutation stratifié par tâche, avec α = 0,01.

MSR-ECB est validée seulement si A dépasse C avec une taille d'effet d ≥ 0,3 et si C ne dépasse pas significativement B.
