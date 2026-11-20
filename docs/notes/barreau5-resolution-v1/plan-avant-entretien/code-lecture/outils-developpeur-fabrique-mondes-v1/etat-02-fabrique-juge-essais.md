# État 02 — fabrique, juge et essais écrits ; 116 essais passent

20 novembre 2026 vers 04:55Z (horloge du conteneur). Pièce de travail du développeur de la fabrique (Claude Opus 5.5).

| fichier | sha256 |
|---|---|
| `src/controle_ia/barreau5_familles/epreuve_verite_plantee_v1.py` | `e2eb98b9f9c2d20ac194c7dfc2a5dc6565cc27824a465af27d6e4c05e46524e5` |
| `src/controle_ia/barreau5_familles/juge_verite_plantee_v1.py` | `c7089d17dcf7c09a8661de474a2a9a7548f979103c35128e34cfd5b5a4be97a1` |
| `tests/test_barreau5_familles_epreuve_verite_plantee_v1.py` | `835e9c1bf05c820af2c98d34bfa32ad9ad5054d4571a99ed6a8ac09a3e25373a` |

Essais : `PYTHONPATH=src .venv/bin/python -B -m pytest -q -p no:cacheprovider tests/test_barreau5_familles_epreuve_verite_plantee_v1.py`
→ 116 passés en 89 s. Premier passage : 2 échecs, tous deux dans une aide d'essai (division par un produit planté
exactement nul en V10) ; l'aide est corrigée, la fabrique n'a pas changé.

Fumée (bloc-notes) : vérités de tous les mondes en 8 s, 24 Mo après resserrement (66 Mo au premier jet, refusé) ;
un monde par groupe en 0,2 à 0,6 s, 143 à 180 fichiers d'arbre ; issues plantées conformes au tableau du point 11.

Ces fichiers changent encore (passage de mutations à venir) : seuls leurs états finals seront scellés par compagnon.
