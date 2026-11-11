# Revérification du barreau 6 sur T0.7 scellé — v1

**En cours** (livrable écrit tôt ; verdict non encore prononcé). Vérificateur neuf, Claude Fable 5.2 (`claude-fable-5-2`), 2026-11-11.

## Notes au fil de l'eau (provisoires, remplacées par le compte rendu final)

- 07:50 UTC : empreintes des pièces vérifiées (candidat 3 `d48fb8a3…`, T0.7 scellé `d7d180ec…`, configuration v8 `e31c7a79…`, brouillon 22 `8b84cba5…`, contre-lecture du code `67614af4…`).
- Constat 1 (bloquant, provisoire) : `lecture_v4.noter` (C7) écrit `plancher_<k>` à `n_plancher` = 800 directions en mode réel ; le barreau 6 exige 200 (`etats_v1.N_DIRECTIONS = 200`, `lecture_v1.ouvrir_e1` l. 205-206 : arrêt, code 3, après le manifeste, donc sans relance possible) ; texte : « 200 directions » (Métrique, B6-D5, plan E1, liste d'arrêt).
- Constat 2 (provisoire) : « au-dessus de son plancher … (même règle que T0.7, « Seuil ») » : T0.7 scellé a changé de règle (différence appariée).
- 08:20 UTC : essai ciblé joué (trois cas, 3 passés) dans le bac à sable : sorties jouets de `lecture_v4` (C7) passées à `accumulation_b6.lecture_v1.lire` (`6c98ea20`). À 200 directions : lecture écrite, champs lus sans faute. À 800 directions : `ArretAccb6` « 800 directions de plancher, 200 attendues », `arret-accb6.json` écrit, relance refusée. Bras arrêté : figées en E. Constat 3 (provisoire) : la réserve du palier « carte » du plancher neuf (dans `resultat.reserves`, chaînes) n'est pas recopiée par le barreau 6 (il ne lit que `reserves_identifiees`).
