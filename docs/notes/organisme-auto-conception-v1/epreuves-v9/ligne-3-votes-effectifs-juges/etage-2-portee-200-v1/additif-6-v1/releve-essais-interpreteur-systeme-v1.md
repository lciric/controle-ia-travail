# Relevé — suites d'essais de l'étage 2 rejouées sous l'interpréteur du mode réel — v1

Pièce de travail (classe C), session du compte organisme, 2026-11-20, sur la demande de la mère (16:27Z : « rejoue toutes les suites d'essais de l'étage 2 sous /usr/local/bin/python3 -I -B (numpy 2.5.3) avant mon scellement, avec les comptes au rapport »).

Interpréteur : `/usr/local/bin/python3 -I -B`, Python 3.13.18, numpy 2.5.3, pytest 9.1.1. Chaque suite est jouée sur une copie du dossier versé (bloc-notes de la session), par `env -C COPIE /usr/local/bin/python3 -I -B -m pytest -q -p no:cacheprovider F`. Aucun appel, aucune clé, aucun réseau, rien sous `archives-reponses-modeles/`.

| suite | dossier versé | essais | résultat |
|---|---|---|---|
| code d'appel v4 | `code-appel-v4/essais_epreuve_juges_reels_ligne_3_v4.py` (`072439a0…`) | 98 | 98 passés (113,01 s) |
| générateur v3 | `generateur-v3/essais_generer_temoins_ligne_3_v3.py` (`7e064c90…`) | 101 | 101 passés (10,30 s) |
| étalonnage et lecture v3 | `etalonnage-lecture-v3/essais_etalonnage_lecture_ligne_3_v3.py` (`7833acb3…`) | 49 | 49 passés (57,13 s) |

Total : 248 passés, 0 échec, 0 saut. Mêmes comptes que sous `.venv` (numpy 2.4.6). Sorties brutes : `sortie-code-appel-v4.txt`, `sortie-generateur-v3.txt`, `sortie-etalonnage-lecture-v3.txt`, au même dossier.
