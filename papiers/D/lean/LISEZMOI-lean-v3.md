# Vérification mécanique du papier D (Lean 4) — v3

- Remplace la v2 pour la table de correspondance (v1 et v2 restent archivées). Chaîne : Lean 4.36.0 (releases.lean-lang.org), Mathlib étiquette v4.36.0 (fc4f59e5…), cache officiel ; installée hors du dépôt avec l'accord de Lazar.
- Rejeu : `bash verifier_lean_v3.sh`. Sortie attendue : 25 théorèmes répartis en quatre fichiers, dépendant des seuls axiomes standard (`propext`, `Classical.choice`, `Quot.sound`), aucun `sorry`, et un énoncé faux témoin refusé.
- Les énoncés suivent le manuscrit v3 (`docs/notes/cartographie-mathematiques-ouvertes-v1/publication-evasion-post-entrainement-v1/manuscrit-arxiv/main-v3.tex`) et le découplage v2 (`papiers/D/theorie/decouplage-geometrique-v2.tex`). L'alignement sur la v4 et sur la v3 du découplage de la fille 2 reste à faire, sur sa réponse.

| Fichier | Théorème Lean | Énoncé du papier |
|---|---|---|
| `Noyau.lean` | `ampA_iff`, `domA_iff` | rejet pur : seuil d'amplification absolue ; dominance du furtif |
| | `niche_same_odds`, `niche_inversion_iff` | niche parfaitement furtive : plus de furtif ⇔ plus d'honnête ; seuil d'inversion |
| | `variance_identity`, `variance_example`, `covariance_identity` | identités de variance (37/150) et de covariance du découplage |
| | `offloop_counterexample`, `inloop_counterexample`, `collapse_counterexample` | contre-exemples exacts de l'audit |
| | `iterated_rejection_iff`, `npg_closed_form`, `rft_weights` | rejet répété ; forme close du gradient naturel discret ; filtrage itéré |
| `NoyauPenalite.lean` | `ampB_iff` | pénalité : condition implicite d'amplification absolue (théorème 1, point 3), énoncée exactement comme dans le manuscrit |
| | `domB_iff` | pénalité : dominance du furtif (point 4b, et R1 sous la pénalité) |
| | `r3_gain_neg` | pièges plantés (R3) : gain négatif dès que C > C*, pour tout τ ≥ τmin > δ |
| `Decouplage.lean` | `linStep_preserves`, `linear_probe_invariant` | découplage, partie 2 : réseau linéaire, `W w = 0` et `Uᵀ w = 0` ⇒ score de la sonde invariant pour tout pas, tout lot et toute entrée |
| | `frozen_row` | découplage, partie 1 : la récurrence qui gèle une ligne de paramètres dont le gradient s'annule à sa valeur initiale |
| | `gating_breaks_orthogonality` | découplage, partie 3 : l'exemple élémentaire où le déclenchement ReLU détruit l'orthogonalité |
| `Detection.lean` | `factor_le`, `miss_le` | budget d'audit, détection : un audit uniforme de B épisodes sur T manque toute triche (k épisodes) avec probabilité binom(T−k,B)/binom(T,B) ≤ (1 − k/T)^B |
| | `detection_counterexample`, `detection_counterexample_98` | contre-exemple relevé par Fable à la borne inférieure de la consigne : T = 100, k = 1, δ = 1/100, budget minimal exactement 99 (manque 1/100 à 99 audits, 1/50 à 98) |

## Limites
- Seules les inégalités et récurrences algébriques sont mécanisées. Restent sur papier : la modélisation (opérateur A, passage aux poids de Gibbs) ; pour le découplage, le calcul du gradient d'un réseau ReLU (`frozen_row` prend en hypothèse que le gradient s'annule à l'initialisation) ; la condition d'indépendance linéaire des noyaux (partie 3) ; le théorème de sélection gaussien (Stein, corrélation maximale).
- Les brouillons de Fable (dynamique à deux canaux, budget d'audit) ne sont pas mécanisés, hormis la borne de détection ci-dessus ; la valeur minimax (principe de Yao) et le programme linéaire de la dissuasion restent sur papier.
