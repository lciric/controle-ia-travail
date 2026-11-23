# Différentiel du texte de T0.8 à sceller contre le brouillon 4 gelé (ligne GEL-T08) — v1

Produit par `brouillons/t08-texte-complet-fable-v1/finaliser-t08-scellement-v2.py` ; exigé par la règle « Gel vérifiable » du texte.

- Brouillon 4 gelé : `brouillons/T0.8-bases-boite-noire-v0-v1-brouillon4.md`, `7da0c3839a7a714b441b018b3cceb704ec431434498653db1496ca839c38c5b5` ; plage gelée, lignes 79 à 252, `f2689209da7197b80da049b2c7c0dafde710ae30b96d5cafe74c6d70156b4ba6`.
- Brouillon 10 : `brouillons/T0.8-bases-boite-noire-v0-v1-brouillon10.md`, `fb004b96bf7fd70d6fe4f1938cba8bcd1afa9a3261135b5ddea336a9e0c68ba1` ; plage gelée `3f5dafbfbe2182f7f59c6f21c538d4401a7ad91a06efc7fddb44f375de16be27`.
- Brouillon d'entrée, déclaré conforme par la vérification : `brouillons/T0.8-bases-boite-noire-v0-v1-brouillon12.md`, `e55a33ce78ab6b7b97b6b9a53b84c054898ca9823ee30ca64df573394aca8d73` ; rapport de vérification `verif.md`, `d4a779bc5bfc85c25b5b5699f764b81424df441f3839b00ccbff0a85ba3894d2`.
- Texte à sceller : `sortie/T0.8-bases-boite-noire-v0-v1.md`, `c9f1b9e71cd9260b136f9265f160a92b2c54b55ae40e4109dea95e17891637ea` ; plage gelée, lignes 81 à 255, `c17970f51637621440cbec6d04ce75a297918087f6c61d9f40fa4a477762582a`.

**Contrôle par programme, tenu** : (a) la plage gelée du brouillon 10, une fois retirée la phrase T5-19, est égale à l'octet à celle du brouillon 4 ; (b) la plage gelée du texte à sceller, une fois remis le nom de chaque marqueur à la place de sa valeur, est égale à l'octet à celle du brouillon 10 : la phrase T5-19 y est celle du brouillon 10, dans son texte et à sa place (rang 103 de la plage ; empreinte épinglée `906b82d6c063eb60cc0c6179d43fdbcbe0dbc434e430ac6026837fd0ae06cde4`).

## Phrase T5-19 (ajoutée au brouillon 5, gardée par le mot de Lazar ; ici avec le nom de son marqueur)

>    - de la course de T0.8 elle-même, pour la lecture seulement : ses sorties scellées (`diag/<run-t08>/course-t08.json` et les fichiers qu'il cite sous `donnees/<run-t08>/`) et son manifeste (`runs/<run-t08>/manifeste.json`, pour son identifiant de run et son empreinte, qui le rattachent à `course-t08.json`, et pour sa date de création, rien d'autre n'en étant gardé : antériorité des lignes `SCELLEMENT-T08` et `CODE-T08` sur le début de la course, « avant toute exécution », en-tête), empreintes vérifiées contre leurs compagnons ; aucune donnée de 7b, aucune sonde, aucun résultat n'en est tiré au-delà de ce que nomment le plan et la « Métrique » (phrase ajoutée au brouillon 5, VCT8B-01 ; nœud de Lazar, VT5-03 : **gardée**, option (a), mot de Lazar « go a pour T5-19 » (journal du compte 4, C4-0054, `registres-provisoires/compte-4-2026-11-14-v16.md`, `190fb7ed632c52c36f3ece7d837b84d9f9529f830553bf46c1ae10021cec9288`) ; ligne du registre et confirmation de la session mère : `<<LIGNE_MOT_LAZAR_T5_19>>`) ;

## Valeurs des marqueurs dans les sections gelées

- `CODE_MOTS_ET_COUT_T06` : ligne du 2026-11-14T14:55:41Z, qui cite le fichier d'inscription `registres/code-mots-et-cout-t06/CODE-MOTS-ET-COUT-T06-v1.json`, `e418fdafbf8362f0458eb0448ec2d32ffa9a8bb122ec619ad0aaf68a9df3b43b` : commit `da06bb57610f840152e4e9a8c449b036577cc582`, module `scripts/mots_et_cout_t06_v3.py`, `9dbcc55ca47b21674636f5d6c9126af15244d5ee63a9df8dee274df126c4e674`, lanceur `scripts/lancer_mots_et_cout_t06_v3.sh`, `e1d2514cd6361f8201a6773a4cf108ac333aa7ca647807698b90c3abeb97a7c5` ; R-2778

- `RUN_7B` : run `20261111-151701-t06-reel`, branche de sortie `calcul/t06-confirmation-7b-v1` (tête `55c3e3eb89a4650419f35999aaa4c54288275b0d`), manifeste `runs/20261111-151701-t06-reel/manifeste.json`, `7e1ac1f02584e4f8babf664e78d12f3122bfdca18292734f28281e9459479bf6` ; ligne inscrite le 2026-11-13T18:52:43Z

- `EMPREINTES_ENTREES_7B` : lues le 2026-11-22 sur les compagnons seuls, sans ouvrir les fichiers : `mesures-t06.npz`, `aca5afd068a8749952c7424a7708a1e4c8b78c082fba495d5d406f2605435049` ; `textes-actions-t06.jsonl`, `d196bb4fffd793dc52190aa2674aeff33619f17bd40d303f564515bde2ad783d` ; `episodes-t06.json`, `c7911933a6cc797db4be094bd252393bb4360cdc55a25867b624be721ccdb51c` ; `manifeste.json`, `7e1ac1f02584e4f8babf664e78d12f3122bfdca18292734f28281e9459479bf6` ; `lecture-cout-t06.json`, `c69884ed54b48ba5a37b17572060a3d2a6258a92ccf8b92d30beb11422196a1c`

- `ENTROPIE_T08` : `169300574314717024477969479955284404501`

- `LIGNE_MOT_LAZAR_T5_19` : R-2657 (mot de Lazar inscrit le 14 novembre) et R-9999 (gardes de code plus strictes confirmées ; sort de VT5-07)

## Valeurs des marqueurs hors des sections gelées

- `COMMIT_CODE_T08` : `0123456789abcdef0123456789abcdef01234567` (pièce de ses empreintes `emp.md`, `3d2e659fac966bceb94b8bee8cf10bcb222a271b939b8f5556599ba99f37aa67` ; contre-lecture de l'alignement `cl.md`, `9d3488bbe8cf674f738791e0a932bdaf43d1ebe4463aaebb114fd576e8aafc46`)

- `LIGNE_DEPENSE_T08` : ligne inscrite au scellement : 2026-11-26 : engagement, T0.8, GO-2026-11-10-12, GO-2026-11-22-79, GO-2026-11-22-93

- `VERIFICATION_CL8_T08` : rapport `verif.md`, `d4a779bc5bfc85c25b5b5699f764b81424df441f3839b00ccbff0a85ba3894d2` ; brouillon déclaré conforme : `brouillons/T0.8-bases-boite-noire-v0-v1-brouillon12.md`, `e55a33ce78ab6b7b97b6b9a53b84c054898ca9823ee30ca64df573394aca8d73`

## Hors des sections gelées

Le texte à sceller est le brouillon d'entrée, à l'octet, hors les cinq valeurs de marqueurs et la phrase de statut de l'en-tête (« non scellé » devient « texte à sceller »). Opérations des brouillons 10 à 12 : `brouillons/t08-texte-complet-fable-v1/differentiel-gel-t08-brouillon11-v1.md` et `…-brouillon12-v1.md`, sections 3.
