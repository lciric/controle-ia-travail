# Rapport — greffon des échecs connus v2 (auteur, 22 novembre 2026)

Verdict : la liste v2 (14 lignes) et le greffon v2 sont posés et scellés dans l'arbre de travail `/home/user/arbre-main-suite-greffon/` (détaché à `0c16f3cd5`). Les 14 exemptés sont en échec attendu. Chacun des artefacts est rouge comme annoncé. Sur 7 fichiers hors liste, les issues sont identiques avec le v1 et le v2. Rien n'est commité ni poussé.

## Fichiers (arbre de travail) et empreintes SHA-256
| Fichier | Empreinte | État |
|---|---|---|
| `tests/echecs-connus-v2.txt` | `44b298298f70d5c7a76c2d5d83b770ce089f7b4e7b599246dfef3298db78101a` | neuf, scellé (compagnon `.sha256`) |
| `tests/greffon_echecs_connus_v2.py` | `530c2d88e7a343d3156badd4052848898565711132aab583fd88cb85d0816f84` | neuf, scellé (compagnon `.sha256`) |
| `tests/conftest.py` | `5fc78c9e5f487487171327e1f6d7d4db8bf49db138d41b26e827180184a3be12` | une seule ligne changée (l. 5) |
| `tests/echecs-connus-v1.txt`, `tests/greffon_echecs_connus_v1.py` | `c73a3310…`, `53b9b9ee…` | intacts, sceaux vérifiés OK |

`git -C /home/user/arbre-main-suite-greffon status --short` :
```
 M tests/conftest.py
?? tests/echecs-connus-v2.txt
?? tests/echecs-connus-v2.txt.sha256
?? tests/greffon_echecs_connus_v2.py
?? tests/greffon_echecs_connus_v2.py.sha256
```

## Choix
- **Une seule liste v2 qui fusionne les deux** (4 lignes de la v1 recopiées octet pour octet par `ecrire_liste_v2.py`, plus 10 lignes du v11). Le greffon v2 ne lit qu'elle, nommée en dur. Pourquoi : il n'y a qu'un sceau à vérifier et qu'un endroit où chercher. Un même identifiant ne peut pas figurer dans deux listes, et l'ordre de lecture ne compte pas. La v1 reste archivée sans modification, mais la suite ne la lit plus.
- **Ligne de `conftest.py`** : elle importe aussi `pytest_collectreport`, car R-A a besoin de ce second crochet. La ligne change toujours seule, mais elle n'est pas « la même ligne » au mot près, puisqu'elle porte un nom de plus.
- **R-A, refus écrit** plutôt qu'une marque « non jugé ». Si une ligne vise un fichier joué mais sauté en bloc à la collecte (le rapport de collecte est « sauté » et aucun essai n'est collecté), la suite s'arrête en erreur d'usage, code 4, avec le message « fichier joué mais sauté en bloc : aucun essai collecté, exemption non jugeable ». Pourquoi : une exemption invérifiable ne doit pas passer en vert, et une marque se perd dans la sortie. Aucun des 3 fichiers listés ne saute en bloc, donc ce refus ne coûte rien aujourd'hui. Si un fichier listé devait sauter un jour pour une raison d'environnement, sa ligne serait à retirer explicitement. Comme dans la v1, une ligne dont le fichier n'est pas joué dans la passe n'est pas jugée (cas 20).
- **R-B, refus de `--runxfail`** (erreur d'usage, code 4) dès que le greffon est chargé. Ce refus est vérifié dans `pytest_collection_modifyitems`, avant la lecture de la liste, comme les autres refus de la v1. Pourquoi : `--runxfail` désarme le strict. Un exempté qui se mettrait à passer passerait alors en silence, et un simple avertissement en tête de sortie se lit mal.

## Table des cas
Sorties sous `…/auteur-greffon-v2/sorties/`. Les cas 10 à 23 sont joués dans des bacs jetables (`…/auteur-greffon-v2/bacs/<cas>/`). Chaque bac reçoit les greffons et le `conftest.py` de l'arbre, copiés octet pour octet (empreintes vérifiées), trois fichiers d'essais synthétiques et une liste scellée propre au cas. Résumé dans `resume-artefacts.txt`.

| Cas | Attendu | Rendu | Fichier |
|---|---|---|---|
| 3 fichiers listés, arbre réel, v2 | 14 échecs attendus (10 du v11, 4 de la v1), code 0 | 41 réussis, 14 échecs attendus, code 0 | `01-exemptes-v2.txt` |
| Mêmes fichiers, v1 (référence) | les 10 du v11 en échec | 10 échecs, 41 réussis, 4 échecs attendus, code 1 | `03-exemptes-v1-reference.txt` |
| `--runxfail`, arbre réel (R-B) | erreur d'usage | code 4, message R-B | `02-runxfail-reel.txt` |
| bac sain | code 0 | 1 réussi, 1 sauté, 2 échecs attendus, code 0 | `10-sain.txt` |
| ligne fantôme | refus | code 4, « aucun essai collecté de ce nom » | `11-fantome.txt` |
| liste altérée après le sceau | refus | code 4, empreinte différente de celle scellée | `12-liste-alteree.txt` |
| empreinte compagnon absente | refus | code 4, compagnon absent | `13-empreinte-absente.txt` |
| ligne en double | refus | code 4, « en double » | `14-doublon.txt` |
| fichier absent | refus | code 4, « fichier absent » | `15-fichier-absent.txt` |
| exempté qui passe | échec strict | code 1, `FAILED … [XPASS(strict)]` | `16-exempte-qui-passe.txt` |
| module sauté en bloc et listé, v2 (R-A) | refus | code 4, « sauté en bloc » | `17-saute-en-bloc-liste.txt` |
| le même, greffon v1 | (montre le trou) | code 0, passé en silence | `18-saute-en-bloc-liste-v1.txt` |
| module sauté en bloc, non listé | code 0 | code 0 | `19-saute-en-bloc-non-liste.txt` |
| module sauté en bloc et listé, fichier non joué | non jugé (comme la v1) | code 0, 2 échecs attendus | `20-…-fichier-non-joue.txt` |
| `--runxfail`, bac, v2 (R-B) | refus | code 4 | `21-runxfail.txt` |
| `--runxfail`, bac, v1 | (montre le trou) | code 1, xfail désarmé | `22-runxfail-v1.txt` |
| caractère de motif | refus | code 4 | `23-motif.txt` |
| 7 fichiers hors liste, v2 et v1 | mêmes issues | 3 échecs et 202 réussis des deux côtés, 0 différence essai par essai | `30-hors-liste-v2.txt`, `31-hors-liste-v1.txt`, `32-comparaison-v1-v2.txt` |

Les 7 fichiers hors liste : `test_cibles_invisibles_v3.py`, `test_depot_expurge_v7.py`, `test_agregateurs.py`, `test_bases.py`, `test_artefacts_v1.py`, `test_bras_b_v1.py`, `test_comparer_echecs_attendus_v1.py`. Les 3 échecs non listés y restent des échecs. Pour jouer la passe v1, la ligne de `conftest.py` a été remise à son texte de `main` (`git diff` vide vérifié), puis rétablie vers le v2.

## Écarts et réserves
- La ligne de `conftest.py` porte un second nom importé (`pytest_collectreport`), voir Choix.
- R-A ne couvre que le saut de module entier à la collecte. Un essai listé sauté un par un (`skipif`, `pytest.skip` dans l'essai) reste « sauté », comme dans la v1. L'exemption n'y est pas jugée et rien ne le refuse. Ce point n'a pas été traité.
- Le relevé des fichiers sautés vit dans un ensemble au niveau du module, vidé à chaque passage de `pytest_collection_modifyitems`. C'est sûr pour une passe par processus, mais ce n'est pas éprouvé pour des sessions pytest imbriquées dans le même processus qui chargeraient ce `conftest.py`.
- Comparaison hors liste : 204 identifiants distincts relevés pour 205 issues. Un identifiant paramétré apparaît en double ou hors du motif de relevé. Les totaux de pytest sont identiques (3 échecs, 202 réussis).
- La suite entière n'a pas été jouée.

## Chemins lus hors de mon dossier
- Arbre de travail : `tests/greffon_echecs_connus_v1.py`, `tests/echecs-connus-v1.txt` et `.sha256`, `tests/conftest.py`, `pyproject.toml`, la liste de `tests/`, des lignes `skip` et `import` de `tests/test_lancer_course_auto_conception_v11.py`, `tests/test_cibles_invisibles_v1.py` et `tests/test_cibles_invisibles_v2.py`, et les fichiers d'essais joués ci-dessus.
- Dépôt : `registres/essaim/vers-mere/annexe-comparaison-greffon-2026-11-22-v1/echecs-avec.txt` ; `controle_ia.scellement` exécuté depuis `/home/user/controle-ia-travail` (sceller, verifier).

## Outils du système employés
`cat`, `ls`, `grep`, `head`, `tail`, `mkdir`, `sha256sum`, `git` (`status`, `diff`), l'interpréteur `/home/user/controle-ia-travail/.venv/bin/python` (pytest 9.1.1, Python 3.13.18). Scripts du dossier : `ecrire_liste_v2.py`, `epreuve_artefacts.py`, `comparer_issues.py`. Aucun réseau, aucune machine, aucun commit.
