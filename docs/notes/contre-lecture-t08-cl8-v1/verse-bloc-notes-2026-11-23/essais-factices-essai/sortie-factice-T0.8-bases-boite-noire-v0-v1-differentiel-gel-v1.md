# Différentiel du texte de T0.8 à sceller contre le brouillon 4 gelé (ligne GEL-T08) — v1

Produit par `brouillons/t08-texte-complet-fable-v1/finaliser-t08-scellement-v1.py` ; exigé par la règle « Gel vérifiable » du texte.

- Brouillon 4 gelé : `brouillons/T0.8-bases-boite-noire-v0-v1-brouillon4.md`, `7da0c3839a7a714b441b018b3cceb704ec431434498653db1496ca839c38c5b5` ; plage gelée, lignes 79 à 252, `f2689209da7197b80da049b2c7c0dafde710ae30b96d5cafe74c6d70156b4ba6`.
- Texte à sceller : `prereg/T0.8-bases-boite-noire-v0-v1.md`, `1498c377045cf88d5eec343222a33b8435a1974eee0ce2182cc127ba529bfe7d` ; plage gelée, lignes 81 à 255, `92f91dcd501505a777919a9f9cafa37e086cb1f3551107cb5e4c22f5655672fb`.
- Brouillon d'entrée : `brouillons/T0.8-bases-boite-noire-v0-v1-brouillon11.md`, `4342b1a5e1aae3d5595ccac86fc8488a5c3e97b7c57c8355d7cb38db8df33456`.

**Contrôle par programme, tenu** : la plage gelée du texte à sceller, une fois retirée la ligne T5-19 du point 1 du plan et remis le nom de chaque marqueur à la place de sa valeur, est égale à l'octet à la plage du brouillon 4.

## Ligne T5-19 (ajoutée au brouillon 5, gardée par le mot de Lazar)

>    - de la course de T0.8 elle-même, pour la lecture seulement : ses sorties scellées (`diag/<run-t08>/course-t08.json` et les fichiers qu'il cite sous `donnees/<run-t08>/`) et son manifeste (`runs/<run-t08>/manifeste.json`, pour son identifiant de run et son empreinte, qui le rattachent à `course-t08.json`, et pour sa date de création, rien d'autre n'en étant gardé : antériorité des lignes `SCELLEMENT-T08` et `CODE-T08` sur le début de la course, « avant toute exécution », en-tête), empreintes vérifiées contre leurs compagnons ; aucune donnée de 7b, aucune sonde, aucun résultat n'en est tiré au-delà de ce que nomment le plan et la « Métrique » (phrase ajoutée au brouillon 5, VCT8B-01 ; nœud de Lazar, VT5-03 : **gardée**, option (a), mot de Lazar « go a pour T5-19 » (journal du compte 4, C4-0054, `registres-provisoires/compte-4-2026-11-14-v16.md`, `190fb7ed632c52c36f3ece7d837b84d9f9529f830553bf46c1ae10021cec9288`) ; ligne du registre et confirmation de la session mère : R-2657 (mot de Lazar inscrit le 14 novembre) et R-9999 (gardes de code plus strictes confirmées ; sort de VT5-07)) ;

## Valeurs des marqueurs dans les sections gelées

- `CODE_MOTS_ET_COUT_T06` : ligne du 2026-11-14T14:55:41Z, qui cite le fichier d'inscription `registres/code-mots-et-cout-t06/CODE-MOTS-ET-COUT-T06-v1.json`, `e418fdafbf8362f0458eb0448ec2d32ffa9a8bb122ec619ad0aaf68a9df3b43b` : commit `da06bb57610f840152e4e9a8c449b036577cc582`, module `scripts/mots_et_cout_t06_v3.py`, `9dbcc55ca47b21674636f5d6c9126af15244d5ee63a9df8dee274df126c4e674`, lanceur `scripts/lancer_mots_et_cout_t06_v3.sh`, `e1d2514cd6361f8201a6773a4cf108ac333aa7ca647807698b90c3abeb97a7c5` ; R-2778

- `RUN_7B` : run `20261111-151701-t06-reel`, branche de sortie `calcul/t06-confirmation-7b-v1` (tête `55c3e3eb89a4650419f35999aaa4c54288275b0d`), manifeste `runs/20261111-151701-t06-reel/manifeste.json`, `7e1ac1f02584e4f8babf664e78d12f3122bfdca18292734f28281e9459479bf6` ; ligne inscrite le 2026-11-13T18:52:43Z

- `EMPREINTES_ENTREES_7B` : lues le 2026-11-22 sur les compagnons seuls, sans ouvrir les fichiers : `mesures-t06.npz`, `aca5afd068a8749952c7424a7708a1e4c8b78c082fba495d5d406f2605435049` ; `textes-actions-t06.jsonl`, `d196bb4fffd793dc52190aa2674aeff33619f17bd40d303f564515bde2ad783d` ; `episodes-t06.json`, `c7911933a6cc797db4be094bd252393bb4360cdc55a25867b624be721ccdb51c` ; `manifeste.json`, `7e1ac1f02584e4f8babf664e78d12f3122bfdca18292734f28281e9459479bf6` ; `lecture-cout-t06.json`, `c69884ed54b48ba5a37b17572060a3d2a6258a92ccf8b92d30beb11422196a1c`

- `ENTROPIE_T08` : `253570597405009124442973687959391052685`

- `LIGNE_MOT_LAZAR_T5_19` : R-2657 (mot de Lazar inscrit le 14 novembre) et R-9999 (gardes de code plus strictes confirmées ; sort de VT5-07)

## Valeurs des marqueurs hors des sections gelées

- `COMMIT_CODE_T08` : `0123456789abcdef0123456789abcdef01234567` (pièce de ses empreintes `emp.md`, `3d2e659fac966bceb94b8bee8cf10bcb222a271b939b8f5556599ba99f37aa67` ; contre-lecture de l'alignement `cl.md`, `9d3488bbe8cf674f738791e0a932bdaf43d1ebe4463aaebb114fd576e8aafc46`)

- `LIGNE_DEPENSE_T08` : ligne inscrite au scellement : 2026-11-26 : engagement, T0.8, GO-2026-11-10-12
