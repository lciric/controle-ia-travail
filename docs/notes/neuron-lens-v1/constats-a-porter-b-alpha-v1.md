# Constats à porter dans une version suivante du lanceur B-α — v1

Relevé par le lecteur du verdict de B-α (`docs/notes/neuron-lens-v1/lecture-b-alpha/verdict-b-alpha-v1.md` sur `main`, `ca06acb1…`,
R-2915), transmis par la mère le 2026-11-15 ; **sans effet sur ce verdict** (le lecteur a vérifié la condition sur pièces).

1. **`essais_ok=True` écrit en dur** dans `etape_verdicts` de `src/controle_ia/neuron_lens/b_alpha_lancer_v3.py` (appel de
   `verdicts_b_alpha_v3.verdict`) : la condition (d) de la chaîne (« essai ou fumée en échec ») n'est pas relue par le code des
   verdicts, elle n'est tenue que par l'ordre des étapes (B0 et fumée doivent être faits pour atteindre `verdicts`). À la prochaine
   version : `essais_ok` calculé depuis les résultats scellés `b-alpha-b0.json` (cinq essais au bilan « passed » sans « skipped »,
   lentilles sans arrêt) et `b-alpha-fumee.json` (code 0), avec un essai qui le rend faux sur un résultat altéré (R5).
2. Rappel des mineurs encore ouverts : `pytest` à épingler dans les exigences ; défaut `calcul/neuron-lens-b-alpha-v1` codé dans
   l'amorce (sans effet, la commande passe `BRANCHE_RESULTATS`) ; `test_cibles_invisibles_v4` avant toute fusion dans `main`.
