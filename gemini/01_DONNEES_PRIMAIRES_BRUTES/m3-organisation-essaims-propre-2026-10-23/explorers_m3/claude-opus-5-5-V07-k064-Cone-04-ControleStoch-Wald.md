BASSIN_MATH: Jeu de Dynkin à Frontières de Wald Couplées (JDFWC)

LOI_PROPOSEE: Pour chaque thèse k, on a Λ_k(t) = Σ log[p₁(x)/p₀(x)] et une valeur de jeu V_k = sup_τ inf_σ E[R_k(τ∧σ) − λ_t·$(τ∧σ)]. Les frontières sont A_t = log((1−β)/α) + λ_t et B_t = log(β/(1−α)) − λ_t, où λ_t est le prix dual du dollar issu de l'équation HJB budgétaire. On spawne un démolisseur si Λ_k ≥ A_t − δ, un explorateur si Λ_k ≤ B_t + δ, et on arrête la thèse sinon.

**1. Mécanisme d'auto-organisation et d'entraînement hors-poids**

- **Rôles en jeu de Dynkin.** Chaque thèse est un jeu d'arrêt à deux joueurs. L'explorateur veut stopper en « acceptation », le démolisseur Red-Team veut stopper en « réfutation ». Une thèse proche de l'acceptation attire donc automatiquement l'adversaire, ce qui produit un équilibre point-selle sans topologie fixe.
- **Arbitrage monoculture/chimère.** Un filtre particulaire Rao-Blackwellisé estime les corrélations d'erreurs ρ̂_ij entre familles (fable, opus, argon) à partir des désaccords notés par jev-1.14.0. Une arête i→j n'existe que si ρ̂_ij < ρ*. Le démolisseur est tiré dans une famille différente de l'explorateur si ρ̂_mono > ρ*, ce qui traite H4'.
- **Allocation du budget.** Un bandit contextuel à fenêtre glissante (SW-UCB) choisit le couple (famille, rôle). Son contexte est (Λ_k, ρ̂, budget restant Claude/Gemini, λ_t), et sa récompense est l'incrément d'information par dollar.
- **Dérive de consigne (H9).** Un CUSUM S_t = max(0, S_{t−1} + log q₁/q₀) est calculé sur la fidélité jev entre consigne racine et consigne déléguée. Si S_t > h, la branche est élaguée et re-spawnée depuis la consigne racine.
- **Apprentissage sans réentraînement.** La mémoire évolutive se limite aux paramètres (ρ̂, posteriors du bandit, h, δ) ; les poids ne sont jamais modifiés.

**2. Fonction objectif et anti-Goodhart**

J = E[ Σ_k 𝟙{V_ext(k)} · (1 − ρ̂_k) − λ·$ − η·|jev_k − V_ext(k)| − κ·N_rec ]

- **V_ext(k)** est une vérification externe via arXiv, Semantic Scholar et Crossref : DOI existant et non contredit.
- **Rôle limité de jev.** Le juge jev ne sert qu'aux vraisemblances, jamais seul à la récompense. L'écart jev/externe est pénalisé, ce qui contre Goodhart.
- **N_rec** compte les affirmations sans référence récupérable, c'est-à-dire la récitation de mémoire paramétrique.

**3. Duel décisif de validation M3 (H_A ⊥ H_B)**

- **Conditions.** Budget identique (100 USD Claude / 20 USD Gemini) et même corpus de 200 questions. Il contient 20 % de pièges plantés : articles rétractés et citations inventées.
- **H_A** : essaim JDFWC.
- **H_B** : topologie fixe à rôles tirés i.i.d., monoculture opus.
- **Contrôle négatif** : JDFWC avec les Λ_k permutés aléatoirement entre thèses. Les frontières sont alors vides d'information et l'avantage doit disparaître.
- **Métriques** : thèses vérifiées par dollar, taux de fausses acceptations sur les pièges, délai moyen de détection de dérive.
- **Décision** : SPRT apparié sur la différence par question, avec α = β = 0,05.
- **Critère de réfutation.** H_A est réfutée si elle ne domine pas H_B, ou si le contrôle permuté égale H_A. Dans ce second cas, le gain viendrait du budget et non de la loi.
