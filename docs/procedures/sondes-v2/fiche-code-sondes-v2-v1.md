# Fiche de code — sondes de la boîte blanche, version 2 (v1)

- **Instrument** de classe B (GO-2026-11-22-126, décision 2). **Écrite par** le développeur session_013QMaykMZAR8jYKempS4coQ (Opus 5.5), le 2026-11-22T21:23:42Z (`date -u`). **Aucun résultat** : données fabriquées seulement.
- **Porte sur** la consigne `60aef942…`, l'erratum 1 `e9c8cde1…` et l'erratum 2 `1e6ebdbe…` ; sert le texte scellé `prereg/diagnostics-prealables-sondes-v1.md` (`e8dca00b…`) ; format du barreau 5 lu dans la pièce `b8539886…` (fichiers fabriqués seulement).
- **Branche** `sondes-v2/code-v1`, code au commit `a2b6c12fe76c209e5d57fd1a890f94ed0effc84b` (cette fiche vient dans le commit suivant).
- **Essais** : `PYTHONPATH=src python -m pytest -q tests/test_sondes_v2_*.py` → 119 passés, 1 sauté (l'essai lent), en moins d'une minute sur ce conteneur ; essai lent (`SONDES_V2_LENT=1`, dimension 4 096) passé à part. Suite complète du dépôt non lancée (consigne de la mère : essais limités au paquet) ; aucun module existant modifié.
- **Choix provisoires** : Q1 à Q13 (confirmés par la mère, à revoir par le concepteur), E-1 à E-7 (LISEZ-MOI).
- **Corrections après contre-lecture** : nouvelle fiche (v2) et nouveaux compagnons ; les fichiers de vérités scellés ne changent jamais (nouvelle version = nouveau nom).

## Fichiers et empreintes (sha256)

| fichier | sha256 |
|---|---|
| `src/controle_ia/sondes_v2/LISEZ-MOI.md` | `19df2531e03025706b69d149e75067e1c566ce6f2108f1e01adb947956848bbb` |
| `src/controle_ia/sondes_v2/__init__.py` | `618b032dc7a1aa6fe384234352bab0f3d000292b3d776e942aa4adf75e338b06` |
| `src/controle_ia/sondes_v2/formes_closes_v1.py` | `22e10ba36374fbba6b86bdab028bff220c455031c244040e66d72ff2d4846a1b` |
| `src/controle_ia/sondes_v2/lecture_v1.py` | `47f58c3c7cfd39a22269299f2ab1431f7183ae484f58d386acbf75380984a464` |
| `src/controle_ia/sondes_v2/magasin_v1.py` | `9b51f41342ed3d8f6c0992771ac55472a7093b1edd2779e358bb1f31128dcdc0` |
| `src/controle_ia/sondes_v2/monde_plante_v3.py` | `a7fc29c889349e7bde103a2a7c2682e1499af8d1fe4b00b6576d936f252b9ddf` |
| `src/controle_ia/sondes_v2/programme_monde_plante_v3.py` | `3b2738693993aec81c9c0aae7aa19aa7f14f89b660644efe611e46fc1fd3b976` |
| `src/controle_ia/sondes_v2/statistiques_v1.py` | `bc23ff317b1b560eb3018d4a65daf744d919665c73ded46e2ab112dc0a29fdac` |
| `tests/test_sondes_v2_formes_closes.py` | `c95104e8c54a9236c7471474a6d8fe053b9334a94316b29cbdb7a990720e367d` |
| `tests/test_sondes_v2_lecture.py` | `5a649d4de166fd5abe61444dde3564d36be2ec08d1decd0c64da1978c59ee679` |
| `tests/test_sondes_v2_magasin.py` | `04d3e4149a11cdd3415f8cfa31d6c73fe4e4b076fd680b55595f7080b508bf18` |
| `tests/test_sondes_v2_monde_plante_v3.py` | `d2ceaafed368fc0b7e20f3f6c064f384bc4552be4f8483fce3604344c718bf83` |
| `tests/test_sondes_v2_statistiques.py` | `c4d55a6a0299863c1dce19a2bdc50a94798be8301abc12e5c34ed74e745f60c1` |
| `src/controle_ia/sondes_v2/verites_mondes_plantes_v1.json` | `e5755cc34284d0ec24ec07aa15ec6e66de18d8462726c3be715c074830b7e285` |
| `src/controle_ia/sondes_v2/verites_mondes_plantes_v2.json` | `af87e981755b91ab9bf28127af1021384503e2db3b736fae167c3a6ae67d36de` |
| `src/controle_ia/sondes_v2/verites_mondes_plantes_v3.json` | `a214fe771dcba10d9485511ab2267a039158bf408eec0967278ae241deeecf40` |

Les fichiers de vérités v1 et v2 sont remplacés par la v3 et gardés tels quels (R12) ; seuls la v3 et les modules `monde_plante_v3` et `programme_monde_plante_v3` font foi pour l'épreuve plantée.
