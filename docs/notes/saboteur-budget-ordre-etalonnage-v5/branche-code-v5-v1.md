# Branche du code v5 du saboteur à budget (champs 1 et 2 de l'ordre de l'étalonnage) — v1

- Branche : `prep/iib-code-v5`, poussée sur `origin` (dépôt de travail).
- Base : `836c7cccda5071fe54ecb148d214d74b5cb90474` (= `origin/prep/iib-code-v4`, vérifié).
- Commit final : `62356e2ff612a8228b37a8333689e8114099f3c0`.
- Arbre final : `ed9b0e48be367670cad0782ccb6fbe2d9ca41b87` (conforme à l'arbre attendu).

## Les treize correctifs, appliqués par `git am` dans cet ordre
Lus sur `origin/claude/iib-reconception-oracle-v1`, sous `brouillons/ii-b-saboteur-budget-v5/code-v5/` ; chaque empreinte vérifiée contre son compagnon `.sha256`.

| Rang | Chemin | SHA-256 |
|---|---|---|
| 1 | `correctifs/0001-Lanceur-de-session-du-saboteur-budget-version-2-chem.patch` | `6449a44d6ed345758424a00e0803ca33845946cac0d1c9cac725f1704edbf900` |
| 2 | `correctifs/0002-Lanceur-de-session-du-saboteur-budget-version-2-corr.patch` | `0ac2c5068bcb1d2e1e7488c23d2d1df5bce47f1e0b32b638871d254a9f4a1410` |
| 3 | `correctifs/0003-Lanceur-de-session-du-saboteur-budget-version-2-erra.patch` | `c0c9a6a51ba74c467a17f54d1dca63a57c1110c70bbb3c8fe2ff6b011cdcb93f` |
| 4 | `correctifs/0004-Organisme-retenu-du-saboteur-budget-code-en-version-.patch` | `4563106efc2296e06f89686ada3c5637c9f1bdafe535072bcd5eb7d3a7f29a9e` |
| 5 | `correctifs/0005-Organisme-retenu-du-saboteur-budget-code-en-version-.patch` | `9b06da7e66d853bd587b5391c26b5e9ef0396ae466c64d963392dfe4dfee8ada` |
| 6 | `correctifs/0006-Organisme-retenu-du-saboteur-budget-code-en-version-.patch` | `ee867c9c6d429d4b5e2aef6b48ccc67ef3e1073e043aec34f2d19ef521ca73ca` |
| 7 | `correctifs-v2/0007-Organisme-retenu-du-saboteur-budget-code-en-version-.patch` | `3075a8df0becf391df583b0ffc300419a387ac49818a48c11d71dd5cd9dad20b` |
| 8 | `correctifs-v3/0008-Organisme-retenu-du-saboteur-budget-code-en-version-.patch` | `ad33fe2697fcdcb95242fe8464fcd154f14aea0140aac898796fb7ee5be88281` |
| 9 | `distillateur-v5/correctifs/0001-Organisme-retenu-du-saboteur-budget-distillateur-en-.patch` | `8cfb77005517c83229887fe78230c1b681f7c0793afc8d986ddaf8558c2debe3` |
| 10 | `distillateur-v5/correctifs/0002-Organisme-retenu-du-saboteur-budget-distillateur-en-.patch` | `a515c1d8372611595c3f7a9a77cc44ebb7083fc5e2698b58890fef4a8b562197` |
| 11 | `distillateur-v5/correctifs/0003-Organisme-retenu-du-saboteur-budget-distillateur-en-.patch` | `324b51fad40b3da3c129e254377a1c8a6fda6866f91ee000cd92a3e1a526a6bc` |
| 12 | `correctifs-v4/0009-Organisme-retenu-du-saboteur-budget-code-en-version-.patch` | `4287a6889061c921886582ff3a7ebffecd4bd67fcbb4556b102e9eb9e2737661` |
| 13 | `correctifs-v5/0010-Organisme-retenu-du-saboteur-budget-code-en-version-.patch` | `d2c339b5b4542c9850edaf2942a8555bdb12da28f9bbb4cfcb06393ac61a7691` |

Écart de chemin : l'ordre nommait `brouillons/ii-b-saboteur-budget-v5/distillateur-v5/correctifs/` ; ce chemin est vide sur la branche. Les trois correctifs du distillateur munis de compagnons sont sous `code-v5/distillateur-v5/correctifs/` (ceux de `code-v5/distillateur-v5/brouillon/`, sans compagnon, n'ont pas été pris). L'arbre final conforme confirme ce choix.

## Essais
Liste figée `scripts/tests-cibles-iib-v5-v4.txt` (23 fichiers), `PYTHONPATH=src`, `--basetemp` neuf : **271 réussis, 0 échec, 0 sauté** (538 s). Torch présent dans l'environnement virtuel (2.14.1+cu130) : aucun essai écarté pour son absence.
