BASSIN_MATH: Quorum Byzantin Dolev-Arthur (QBDA)

LOI_PROPOSEE: Une affirmation c est acceptée si et seulement si κ(c) ≥ 2f̂+1 et AM(c) = 1. Le budget suit la règle b_{t+1}(a) ∝ b_t(a)·exp(η·ΔV_a/$_a) · 1[ρ̂_fam(a) < ρ*].

1. **Mécanisme d'auto-organisation hors-poids**
- **Domaines de faute.** Chaque famille de poids (fable, opus, argon) constitue un domaine de faute. Une erreur corrélée (H4') est traitée comme une collusion byzantine. Le nombre de fautes est estimé par f̂ = ⌈n·ρ̂⌉, où ρ̂ est la corrélation d'erreurs inter-agents mesurée gratuitement par jev-1.14.0 sur des canaris.
- **Topologie de Dolev.** Une consigne n'est transmise que par κ ≥ 2f̂+1 chemins sommet-disjoints. Le récepteur garde la version majoritaire, dont l'empreinte est vérifiée par jev. Une divergence révèle une dérive de délégation (H9) et entraîne l'élagage du relais fautif.
- **Spawn.** Si ρ̂_fam > ρ*, l'essaim crée un démolisseur Red-Team issu d'une autre famille : la chimère est forcée. Si ρ̂ est faible et le gain marginal ΔV/$ élevé, il crée un explorateur dans la famille la moins chère : la monoculture est tolérée.
- **Vérification Arthur-Merlin / PCP.** Les agents (Merlin) engagent un hash de leurs preuves. Arthur, c'est-à-dire jev combiné aux API Crossref et Semantic Scholar, tire ensuite des pièces publiques et vérifie k citations au hasard. Toute citation non résolvable invalide l'affirmation, ce qui neutralise la récitation de la mémoire paramétrique.
- **Mémoire évolutive.** L'essaim conserve un registre de topologies et de prompts, muté par la règle de budget ci-dessus.

2. **Fonction objectif et anti-Goodhart**

R = Σ_c 1[c vérifiée sur audit secret] − λ·ρ̂ − μ·Drift_H9 − ν·$/$_max

- L'audit est un sous-ensemble tiré après l'engagement des agents (schéma commit-reveal) et jamais exposé à l'optimisation.
- Le juge alterne entre jev et une famille non productrice de l'affirmation.
- Des canaris faux plantés mesurent la complaisance : si le taux d'acceptation des canaris dépasse α, alors R est mis à 0.

3. **Duel décisif (H_A ⊥ H_B)**
- **Budget constant** : 100 USD Claude et 20 USD Gemini par bras, sur N = 200 tâches bibliographiques de controle-ia, avec 20 % de canaris.
- **Bras A (QBDA)** : la loi proposée.
- **Bras B1** : essaim fixe en monoculture opus.
- **Bras B2** : routage i.i.d. uniforme.
- **Contrôle négatif C** : QBDA avec des scores jev permutés aléatoirement. Il doit retomber au niveau de B2, sinon le gain ne vient pas du signal byzantin.
- **Métrique préenregistrée** : la précision vérifiée sur l'audit secret, mesurée à rappel égal, ainsi que le taux d'acceptation des canaris.
- **Hypothèses** :
  - H_A : A > max(B1, B2, C), avec test de permutation p < 0,01 et correction de Holm.
  - H_B : A ≈ C, ce qui réfuterait QBDA.
- **Falsification structurelle** : si ρ̂ entre familles est indistinguable de ρ̂ intra-famille, la chimère n'apporte rien et la loi est rejetée.
