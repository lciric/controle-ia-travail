# Note — échecs connus des tests complets du dépôt — v1

Pièce de travail (classe C), session du compte organisme, 2026-11-21 vers 20:20Z, sur la décision de la mère (réponse du 21 novembre à 20:18Z au message `vers-mere/2026-11-21-2014-organisme.md`, point 1 (d)). Complète le tri `tri-echecs-tests-complets-2026-11-21-v1.md` (`9957b178…`), même dossier, qui reste intact.

## Échecs connus, laissés tels quels (aucune correction)
- **Essais T0.6 datés** (368 échecs) : la fin de l'accord est écrite en dur (`FIN_GO = "1794873600"`, soit le 2026-11-17T00:00Z), et l'accord GO-2026-11-02-28 a échu le 16 novembre. Ils échouent à toute date postérieure.
- **Listes figées T0.6 v1 et v2** (`tests/test_t06_v11_liste.py` et `test_t06_v12_liste.py`) : elles sont figées par nom et ne couvrent pas les fichiers d'essais ajoutés depuis. Elles ne peuvent plus passer.
- **Rapport réel versé** (`test_epreuve_temoins_auto_conception_v3`) : l'essai exige l'absence d'un rapport réel, qui est versé dans le dépôt.

## Consigne pour jouer la suite
Tant que les lanceurs scellés vivent, la suite des essais se joue par **`/usr/local/bin/python3`**, avec `PYTHONPATH=src`, et non par `.venv/bin/python`. Le filtre « programme à épingler » des lanceurs d'auto-conception v1 à v10 et du lanceur `affinage_mentors_v4` compte comme programme l'interpréteur de `.venv`, qui est un lien hors de `/usr/`. Par l'interpréteur du système, les fichiers concernés passent (1 827 réussis, 4 échecs relevant d'autres familles, d'après le tri). Le défaut est corrigé dans les versions neuves seulement, au lot de corrections de classe B.
