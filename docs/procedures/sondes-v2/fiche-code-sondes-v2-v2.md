# Fiche de code — sondes de la boîte blanche, version 2 (v2)

- **Remplace** la fiche v1 (`docs/procedures/sondes-v2/fiche-code-sondes-v2-v1.md`, `725387ef…`, gardée telle quelle, R12), après la contre-lecture de Sonnet (branche `contre-lecture/sondes-v2-code-v1`, commit `d4abb3e94`, note `docs/notes/sondes-v2-contre-lecture-v1/contre-lecture-code-sondes-v2-v1.md`). **Écrite par** le développeur session_013QMaykMZAR8jYKempS4coQ (Opus 5.5), le 2026-11-23T05:04:18Z (`date -u`). **Aucun résultat** : données fabriquées seulement.
- **Code** au commit `831d1cfb8a59e1e7654036133719db175fadb861` de la branche `sondes-v2/code-v1` (cette fiche vient dans le commit suivant).
- **Essais** : `PYTHONPATH=src python -m pytest -q tests/test_sondes_v2_*.py` → 127 passés, 1 sauté (l'essai lent), en 32 s sur ce conteneur (jusqu'à 2 min sous charge, mesure du contre-lecteur) ; essai lent (`SONDES_V2_LENT=1`) passé. Le paquet ne charge pas torch (essai).

## Corrections, défaut par défaut

| défaut | correction |
|---|---|
| 1, majeur (R9) | le rapport du programme porte le commit, l'état du dépôt et la configuration complète empreintée ; dépôt sale refusé sauf `--autoriser-depot-sale`, alors consigné en réserve ; essais |
| 2, majeur | paires lues sur la structure du jeu (`paires_structurelles`), quelle que soit la famille ; étiquette du jeu de poids sans paires : permutation des séries d'un bloc ; unité échangeable inconnue sur un jeu à unités : arrêt nommé ; trois essais |
| 3 | monde « fuite de pli » : cas sain jumeau (unité et tâche tenues à l'écart) joué avant l'artefact |
| 4 | critère engagé jamais lu ou manquant dans une réplique : arrêt (essai) |
| 5 | sonde d'identité : nombre de tirages où un pli manque (et non de plis manquants) |
| 6 | nul de la sonde d'identité : 200 par défaut, séparé du nul de réétiquetage (`--nul-identite`, écrit au manifeste ; abaissé dans les seuls essais) |
| 7 | ligne : nombre de plis d'épreuve sans les deux classes rapporté ; prédicteur trivial manquant : « prédicteur non évalué » |
| 8 | lignes : effectifs de plan et nombre de plis produits ; garde du résumé sans accents et élargie (testable, fort, faible, insuffisant) ; clés du résumé tirées d'une liste fermée |
| 9 | magasin : les octets vérifiés sont ceux chargés (`io.BytesIO`) |
| 10 | magasin : garde « même source de textes », diagnostic nommé pour l'exception (essai) |
| 11 | LISEZ-MOI et en-tête de `lecture_v1` corrigés ; cette fiche v2 |
| 12 | copies fidèles sans torch dans `reemploi_v1.py` ; essai d'égalité octet pour octet aux originaux ; essai « torch non chargé » |
| 13 | contrôle du chemin marqué « provisoire (E-8) » ; essai d'équivalence du Holm de `etalon_familles` avec `holm()` |

## Fichiers et empreintes (sha256)

| fichier | sha256 |
|---|---|
| `src/controle_ia/sondes_v2/LISEZ-MOI.md` | `df2493bbf2ffba36ed25cc42776b96fec36192292e38540c0f8d158865112d5e` |
| `src/controle_ia/sondes_v2/__init__.py` | `618b032dc7a1aa6fe384234352bab0f3d000292b3d776e942aa4adf75e338b06` |
| `src/controle_ia/sondes_v2/formes_closes_v1.py` | `a284a936abef3eb1c1b27abc200d961d5699f67e557997e3e9a4012158573ce4` |
| `src/controle_ia/sondes_v2/lecture_v1.py` | `9abdabdfc7e2ddf999e40a493e77dad704c954bd1e3ac352cddadd7f55b25263` |
| `src/controle_ia/sondes_v2/magasin_v1.py` | `9bb3cc48918c7e1855da1b2f82ffe3529030ffb3fb3bb7f0072236020dddee32` |
| `src/controle_ia/sondes_v2/monde_plante_v3.py` | `0381e42955a94f8ef717850b77d7f8581063b0c02bc6ffa81eab18ac002ceb6c` |
| `src/controle_ia/sondes_v2/programme_monde_plante_v3.py` | `db1679a3766d371da7ed0e8e34bb8db6860c7a3ac2adde5030437a194b456561` |
| `src/controle_ia/sondes_v2/reemploi_v1.py` | `5bb27d36f1fd96773eda99dda8bb5c9f115bbe7d1b0e4aa18e66de73c9cb8ac3` |
| `src/controle_ia/sondes_v2/statistiques_v1.py` | `c498147816094592fdb75fa8513a76e93f4e7a675a70f50a3d2a92a5931404a8` |
| `tests/test_sondes_v2_formes_closes.py` | `d3d9113ca4592fe27f2a9c6783d3056e96673f7139a68940d9abc670f3ef168a` |
| `tests/test_sondes_v2_lecture.py` | `5df61a925fd08d767d7c273faf4c6c46a64e62c4ada35f4c34002ec5f172c71a` |
| `tests/test_sondes_v2_magasin.py` | `845a5006744662493f977702c6b738fff6d7ff5380e70647f41e3c1392305e56` |
| `tests/test_sondes_v2_monde_plante_v3.py` | `26d4e97b924fe5c7471ccd7da23e27b24961090dfacbb3165b97a4854744af1e` |
| `tests/test_sondes_v2_reemploi.py` | `99bcd09ec44dec9b89f07200f6d27ca4b2fe49747de2b87997ecb203aac0ed9a` |
| `tests/test_sondes_v2_statistiques.py` | `f99a388dba6b8f8b14e9cf1d629ecccddaaa6b8fc2ec449c3b986cea438e80b9` |
| `src/controle_ia/sondes_v2/verites_mondes_plantes_v1.json` | `e5755cc34284d0ec24ec07aa15ec6e66de18d8462726c3be715c074830b7e285` |
| `src/controle_ia/sondes_v2/verites_mondes_plantes_v2.json` | `af87e981755b91ab9bf28127af1021384503e2db3b736fae167c3a6ae67d36de` |
| `src/controle_ia/sondes_v2/verites_mondes_plantes_v3.json` | `a214fe771dcba10d9485511ab2267a039158bf408eec0967278ae241deeecf40` |

Compagnons `.sha256` des fichiers modifiés renouvelés (l'ancienne empreinte reste dans l'historique git et dans la fiche v1). Fichiers de vérités inchangés.
