# Additif 1 à la passation 2026-11-22-1826-dossier-entretien-billets (scellée, non réécrite) — 2026-11-22T18:56:20Z

Tests :
- La suite complète est très longue : environ 8 % après une demi-heure. Je l'ai arrêtée par ses numéros de processus (542, 2009).
- Relancée en mode arrêt au premier échec : 326 réussis, 1 sauté, **1 échec**.
- Le test en échec : `tests/test_amorce_b5f_formation_v1.py::test_texte_plancher_d_essais_egal_au_nombre_d_essais_du_paquet`. Le plancher MIN_ESSAIS vaut 235, alors que les fichiers `tests/test_barreau5_familles_*.py` comptent 814 essais.
- Ce test relève du chantier du barreau 5, non de cette session : rien n'est corrigé ici, c'est signalé à la mère.
- Le reste de la suite, au-delà de ce premier échec, n'a pas été joué.
