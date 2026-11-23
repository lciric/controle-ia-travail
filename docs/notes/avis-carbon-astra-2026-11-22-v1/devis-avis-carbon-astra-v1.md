# Devis — avis de Carbon et d'Astra (2026-11-22)

Aucun appel fait. Accord demandé à la mère (GO-2026-11-22-102 non inscrit).

Prix : gemini-4-carbon 4 / 20 USD par million (entrée / sortie, catalogue du collisionneur v9) ; gpt-6.2-astra 8 / 40 USD par million (R-4905). Réglages : ceux du collisionneur v9 (Carbon : plafond 65 536, réflexion bornée à 32 768, garde Google v3 ; Astra : interface Responses, effort de raisonnement le plus haut, plafond 64 000).

| appel | entrée (≈ jetons) | sortie au pire | pire (USD) | attendu (USD) |
|---|---|---|---|---|
| question A — Carbon | 2 000 | 65 536 | 1,32 | 0,40 |
| question A — Astra | 2 000 | 64 000 | 2,58 | 0,80 |
| question B — Carbon (suspendue, nœud de cloisonnement) | 3 000 | 65 536 | 1,32 | 0,40 |
| **total** | | | **5,22** | **1,60** |

Un appel par modèle et par question ; aucune relance automatique sauf panne technique déclarée (GO-2026-11-22-77), dans le même plafond.
