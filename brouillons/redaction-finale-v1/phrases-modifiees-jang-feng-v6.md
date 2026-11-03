# Phrases modifiées par le directeur entre la version vérifiée et la version finale — v2

Pour le vérificateur final : chaque phrase ajoutée ou changée (« + ») et celle qu'elle remplace (« − »). Ces phrases n'ont pas été revues par le premier vérificateur.

## jang-feng (jang-feng/reponse-v5.md `e075bd8b…` → jang-feng/reponse-v6.md `78cabf74…`)

− White-box access is best at getting a hidden capability back, and least proven at telling why it was hidden.
+ Weight access is best at getting a hidden capability back, and least proven at telling why it was hidden.
− In the auditing game (Taylor et al., arXiv 2512.07810), imitating a weaker model beat black-box detection, while training on a single correct demonstration elicited full performance from the (password-locked) sandbaggers.
+ In the auditing game (Taylor et al., arXiv 2512.07810), imitating a weaker model beat black-box detection; probes did better but were misled by decoys; and training on a single correct demonstration elicited full performance from the (password-locked) sandbaggers.
− For capability evaluations, that alone justifies white-box access.
+ On fine-tuned locks with full demonstrations, that justifies weight access.
− That shows the lock is conditional.
− But an auditor rarely knows the trigger: the comparison that decides is a model never locked that starts at the same score.
+ That compares the same weights with and without trigger, which start at different scores.
+ RL-locked organisms (§3.1) have no trigger to remove, so the comparison that validates the method, before any audit, is a model never locked starting at the same score.
− The improvement ratio ξ used in the auditing game is a maximum over noise levels and seeds, and a maximum can only grow as draws are added, so a model hiding nothing can score above 1.
− Its null is a benign model run through the same grid, not 1.0.
+ The improvement ratio ξ used after the auditing game is a maximum over noise levels and seeds, and a maximum can only grow as draws are added, so a model hiding nothing can score above 1.
+ Their unlocked conditions reach ξ = 1.26 (Fig.
+ 34); the null is a score-matched benign model through the same grid.
− In my first preregistered test on real activations (Llama-3.1-8B-Instruct, 2,400 actions), the deception probe's interval cleared chance (lower bound 0.53) but not the 0.95 quantile of 200 covariance-matched random probes (0.57): not detected at this power, and the null does not exclude AUCs below 0.63 (https://github.com/lciric/ideation-organism/blob/7c7b688/resultats/controle-p3-premier-test/README.md).
− My automated-research judge meets the same maximum over attempts: with n tries at α = 0.05, the chance of a false promotion is bounded only by 1 − (1 − α)ⁿ, 0.56 at n = 16 (https://github.com/lciric/ideation-organism/blob/7c7b688/resultats/attaque-goodhart-v2/README.md).
− What I would run: with both Qwen3-14B recipes of Eyon's paper, pair the locked organism with five never-locked controls fine-tuned on degraded demonstrations to the same starting score (within 2 points), through the same σ grid and seeds, comparing whole accuracy-versus-σ curves at equal σ, since a control merely more fragile to noise would fake a gap.
+ In my first preregistered test on real activations, the deception probe's interval cleared chance (lower bound 0.53) but not the 0.95 quantile of 200 covariance-matched random probes (0.57): not detected at this power, and the null does not exclude AUCs below 0.63 (https://github.com/lciric/ideation-organism/blob/7c7b688/resultats/controle-p3-premier-test/README.md).
+ What I would run: with both Qwen3-14B recipes of Eyon's paper, pair the locked organism with five never-locked controls (the base trained on a weaker model's honest attempts, same adapter rank) at the same starting score (within 2 points), through the same σ grid and seeds, comparing whole accuracy-versus-σ curves at equal σ, since a control merely more fragile to noise would fake a gap.
− So white-box perturbation is a strong elicitation tool and, so far, an unvalidated detector of intent: evidence only against a matched benign control.
+ So weight access is a strong elicitation tool and white-box perturbation, so far, an unvalidated detector of intent: evidence only against a matched benign control.

Phrases ajoutées ou changées : 11.
