# Erratum 1 à la consigne du poste Lean v12 (88b5a78b…) — écrit par la mère à 2026-11-22T11:34:51Z (`date -u`)

Sur les deux remarques non bloquantes de la quatrième passe du contre-lecteur (`verification-consigne-v12-v1.md`, c763546c…, verdict « conforme »). Cet erratum prime sur la v12 pour les deux points suivants ; le reste de la v12 est inchangé.

1. **Borne de l'échéance.** La garde « aucune préparation si L1 tombe après le 2026-11-26 à 23:59 UTC » porte aussi sur la création de la machine : aucune machine n'est créée, et aucune n'est encore allumée, après le 2026-11-26 à 23:59 UTC, échéance de GO-2026-11-22-42. Si `T_LIM` (L1 + 6 h) dépasse cette heure, la limite de l'essai devient le 2026-11-26 à 23:59 UTC, et l'arrêt se fait par l'identifiant de la machine. La borne du 30 novembre (GO-2026-11-10-13) reste, plus large.
2. **Étiquette « H12 ».** Dans les réserves, « H12 » se lit en clair : un passage en parallèle compté comme fait alors que l'un des passages a été refusé. Ce cas se lit « non établi ».
