# Vérification mécanique du noyau algébrique (Lean 4) — v1

- Chaîne : Lean 4.36.0 (releases.lean-lang.org), Mathlib étiquette v4.36.0 (commit fc4f59e5…), cache officiel ; installée le 24 novembre 2026 avec l'accord de Lazar.
- Rejeu : `bash verifier_lean_v1.sh` (≈ 10 s avec le cache). Sortie attendue : 13 théorèmes dépendant des seuls axiomes standard (`propext`, `Classical.choice`, `Quot.sound`), aucun `sorry`, et un énoncé faux témoin refusé.

| Théorème Lean | Énoncé du papier |
|---|---|
| `ampA_iff` | seuil d'amplification absolue sous le rejet pur (théorème 1, point 2) |
| `domA_iff` | dominance du furtif sur l'honnête sous le rejet pur (point 4a) |
| `niche_same_odds` | lemme : à poids honnête et furtif communs, plus de furtif ⇔ plus d'honnête (correction d'audit n° 2 ; l'égalité des poids dans la niche est un calcul direct, non mécanisé) |
| `niche_inversion_iff` | seuil d'inversion dans la niche parfaitement furtive (point 4c), avec k = η(ΔR + C) |
| `variance_identity`, `variance_example` | identité de variance (point 1) et exemple rationnel exact 37/150 |
| `covariance_identity` | identité de covariance du découplage sous le rejet pur (régime R2) |
| `offloop_counterexample`, `inloop_counterexample`, `collapse_counterexample` | contre-exemples exacts de l'audit : 1/2 → 37/50, 3/4 → 7/12, part furtive 3/128 |
| `iterated_rejection_iff` | rejet répété : barrière non évanescente (audit § 3.1, section dynamique) |
| `npg_closed_form` | gradient naturel discret : forme close, pression effective η(1 − (1 − γ/η)^k) |
| `rft_weights` | filtrage itéré : poids p β^k w^k après k tours |

Limites : les théorèmes portent sur les inégalités algébriques des énoncés, pas sur la modélisation (choix de l'opérateur A, passage du modèle aux poids de Gibbs). Les deux brouillons de Fable (dynamique à deux canaux, budget d'audit) ne sont pas mécanisés.
