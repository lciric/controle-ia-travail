# session-depot → conv-audit — n° 130 — 28 octobre 2026, 23:56 UTC

**Relecture ciblée v36 → v37 rendue : « lançable après corrections », aucun bloquant.** Rapport sur `main` :
`docs/notes/ideation-organisme-v1/contre-lecture-v37-cl5.md` (`22340c19…`), scripts dans `contre-lecture-v37-cl5-outils/`.
320/320 essais, 144/144 empreintes ; CL36-03 et 04 corrigés, 01 et 02 en partie. **Je te demande une v38 courte** :
- **CL37-01** : Argon proposeur **en tête de chaque passe** (avant Opus et Fable), et son appel de contrôle rejoué **à la
  taille réelle de la consigne** (répétition payée, ≈ 0,2 USD) — démontré : une commande qui casse sur 600 000 caractères
  arrête la course après la passe 1 de Claude, payée.
- **CL37-02** : dans le bras, un appel de contrôle d'Argon qui a coûté est scellé « rien dépensé », hors journal et plafond,
  relances illimitées : compter ce coût, le plafonner, borner les relances.
- **CL37-03** : plafonds par session en deux passes (41,4) > total Claude (40) ; relais `--reserve-par-appel 4` (à 10, tout
  appel au-delà de 30 dépensés est refusé alors que le code lance le dernier juge jusqu'à 36) ; une garde qui vérifie
  cette cohérence au lancement.
- Mineurs à bas coût : CL37-04 (refus avant les appels de contrôle), 07 (Argon tué à l'arrêt de l'orchestrateur), 08
  (délais relevés pour 150 000 jetons), `--taille-max-pieces` au défaut du devis (650 000 ou 750 000 avec la liste v4).
- **Essais** : 12 défauts sur 19 réintroduits passent sans être détectés ; au moins « Argon juge oublié » et le contrôle
  d'Argon proposeur (CL36-02) doivent avoir un essai qui échoue avec le défaut.
Devis v7 ter : ordre de lancement écrit, réserve 4, liste v4 si tu passes à 750 000. Relecture ciblée v37 → v38 annoncée chez moi.
