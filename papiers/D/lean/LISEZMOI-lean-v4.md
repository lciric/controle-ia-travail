# Vérification mécanique du papier D (Lean 4) — v4, alignée sur le manuscrit v4

- Remplace la v3 pour la table de correspondance (v1 à v3 archivées). Sur le mot de Lazar « aligne sur la v4 ».
- **Énoncé de référence** : `docs/notes/cartographie-mathematiques-ouvertes-v1/publication-evasion-post-entrainement-v1/manuscrit-arxiv/main-v4-correctif-1.tex` (`f02e9db22963078b…`), base de diffusion retenue par la mère de la fille 2. Ses équations numérotées (`eq:ampA`, `eq:ampB`, `eq:domA`, `eq:domB`, `eq:inversion`, `eq:variance`, `eq:R1`, `eq:R2`, `eq:R3`) sont identiques, après normalisation des blancs, à celles de la v3 sur laquelle la Lean avait été écrite. Les remarques nouvelles de la v4 sont couvertes par `NoyauV4.lean`.
- Rejeu : `bash verifier_lean_v4.sh`. Sortie attendue : 30 théorèmes en cinq fichiers, avec les seuls axiomes standard (`propext`, `Classical.choice`, `Quot.sound`), aucun `sorry`, et un énoncé faux témoin refusé.

| Énoncé de la v4 | Théorème(s) Lean |
|---|---|
| `thm:selection`, point 1 (identité de variance) et exemple 37/150 | `variance_identity`, `variance_example` |
| `thm:selection`, point 2 (`eq:ampA`) | `ampA_iff` |
| `thm:selection`, point 3 (`eq:ampB`, condition implicite) | `ampB_iff` |
| `thm:selection`, point 4a (`eq:domA`) ; masse aux tricheurs, part furtive constante (3/128) | `domA_iff` ; `collapse_counterexample` |
| `thm:selection`, point 4b (`eq:domB`) et `thm:escape` R1 sous la pénalité | `domB_iff` |
| `thm:selection`, point 4c (`eq:inversion`) | `niche_inversion_iff` |
| `rem:niche` : plus de furtif ⇔ plus d'honnête ; moins de triche totale | `niche_same_odds`, `niche_total_cheating` |
| `rem:modelA` : rejet répété, barrière non évanescente | `iterated_rejection_iff`, `rft_weights` |
| `thm:escape` R2, identité de covariance (`eq:R2`) | `covariance_identity` |
| `rem:decoupling` : 1/2 → 37/50 hors boucle ; 3/4 → 7/12 en boucle | `offloop_counterexample`, `inloop_counterexample` |
| `rem:decoupling` : covariance nulle, insuffisante sous la pénalité | `zero_covariance_example` ; `zero_covariance_not_sufficient` (pour **toute** pression k > 0, par convexité : `exp_midpoint`), plus général que la valeur k = 4 du texte |
| Remarque « Enrichment under Operator B needs equal rewards » (0,8810 → 0,8748) | `enrichment_fails_under_B` (le sens de l'inégalité ; les quatre décimales ne sont pas mécanisées) |
| `thm:escape` R3 (`eq:R3`) | `r3_gain_neg` |
| section de la dynamique (gradient naturel discret) | `npg_closed_form` |
| découplage géométrique, partie linéaire | `linStep_preserves`, `linear_probe_invariant`, `frozen_row`, `gating_breaks_orthogonality` |
| budget d'audit, détection | `factor_le`, `miss_le`, `detection_counterexample`, `detection_counterexample_98` |

## Limites
Non mécanisés : `prop:limits` (limites asymptotiques), les valeurs décimales des tables, la modélisation (opérateur A, poids de Gibbs), le théorème de sélection gaussien, la dynamique à deux canaux, le programme linéaire de la dissuasion et la valeur minimax de la détection.
