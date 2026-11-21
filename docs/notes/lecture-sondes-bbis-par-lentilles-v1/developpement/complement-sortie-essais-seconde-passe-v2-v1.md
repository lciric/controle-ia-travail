# Complément à la sortie des essais de la seconde passe v2 — v1

Session des lentilles, 2026-11-21T21:29:50Z. Répond aux remarques a et b de la contre-lecture
`contre-lectures/contre-lecture-corrections-seconde-passe-v2-v1.md` (93833229…), sans réécrire la table des corrections ni la sortie
scellée (`sortie-essais-seconde-passe-v2.txt`, 939a6674…).

- **a.** `tests/test_lentilles_sondes_bbis_seconde_passe_corrections_v1.py` compte **54 essais**, non 55 comme le dit
  `corrections-seconde-passe-v2-v1.md` (compte recueilli par la contre-lecture : 54 réussis).
- **b.** L'ancien fichier `tests/test_lentilles_sondes_bbis_seconde_passe_lanceur_v1.py`, joué à part (commande :
  `PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src python -m pytest -q -p no:cacheprovider tests/test_lentilles_sondes_bbis_seconde_passe_lanceur_v1.py`,
  code au commit 0690d639a) : **34 passed**, code 0. Avec le paquet entier (3 226 réussis, 1 échec : un essai de ce fichier, dépendant
  de l'ordre), tous les essais du paquet passent quand ce fichier est joué dans un processus à part.
