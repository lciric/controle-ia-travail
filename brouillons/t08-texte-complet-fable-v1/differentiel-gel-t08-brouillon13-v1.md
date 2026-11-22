# Différentiel du brouillon 13 de T0.8 contre le brouillon 4 gelé (ligne GEL-T08) — v1

Produit par `brouillons/t08-texte-complet-fable-v1/faire-t08-brouillon13-v1.py` ; aucune ligne n'est écrite à la main.

- Brouillon 4 gelé : `brouillons/T0.8-bases-boite-noire-v0-v1-brouillon4.md`, `7da0c3839a7a714b441b018b3cceb704ec431434498653db1496ca839c38c5b5`.
- Brouillon 10 (candidat du compte 4) : `brouillons/T0.8-bases-boite-noire-v0-v1-brouillon10.md`, `fb004b96bf7fd70d6fe4f1938cba8bcd1afa9a3261135b5ddea336a9e0c68ba1`.
- Brouillon 12 (départ) : `brouillons/T0.8-bases-boite-noire-v0-v1-brouillon12.md`, `e55a33ce78ab6b7b97b6b9a53b84c054898ca9823ee30ca64df573394aca8d73`.
- Brouillon 13 : `brouillons/T0.8-bases-boite-noire-v0-v1-brouillon13.md`, `f63a305ed5a3528eba8e6832f39ddd4614ff96f3973edf42a792f49604e48213`.

## 1. Sections « Hypothèse » à « Liste d'arrêt »

Brouillon 4 : lignes 79 à 252 (174 lignes), empreinte de la plage `f2689209da7197b80da049b2c7c0dafde710ae30b96d5cafe74c6d70156b4ba6`. Brouillon 10 : empreinte de la plage `3f5dafbfbe2182f7f59c6f21c538d4401a7ad91a06efc7fddb44f375de16be27`. Brouillon 13 : lignes 81 à 255 (175 lignes), empreinte de la plage `3c0ab4fab57c21c0ecc68e2591b943b01adcf654eab95f2d91d2dc76b0ff3f78`.

**Contrôle par programme, tenu** (`controle_gel_t08_v1.py`) : (a) la plage du brouillon 10, une fois retirée la phrase T5-19, est égale à l'octet à celle du brouillon 4 ; (b) la plage du brouillon 13, une fois remis le nom de chaque marqueur à la place de sa valeur, est égale à l'octet à celle du brouillon 10. La phrase T5-19 est donc celle du brouillon 10, dans son texte et à sa place (rang 103 de la plage).

Différences avec le brouillon 4, toutes :

### Différence 1 — Métrique (brouillon 4, l. 122-122 ; brouillon 13, l. 124-124)

- marqueur `CODE_MOTS_ET_COUT_T06` rempli : au brouillon 4, le nom du marqueur entre chevrons ; au brouillon 13 : « ligne du 2026-11-14T14:55:41Z, qui cite le fichier d'inscription `registres/code-mots-et-cout-t06/CODE-MOTS-ET-COUT-T06-v1.json`, `e418fdafbf8362f0458eb0448ec2d32ffa9a8bb122ec619ad0aaf68a9df3b43b` : commit `da06bb57610f840152e4e9a8c449b036577cc582`, module `scripts/mots_et_cout_t06_v3.py`, `9dbcc55ca47b21674636f5d6c9126af15244d5ee63a9df8dee274df126c4e674`, lanceur `scripts/lancer_mots_et_cout_t06_v3.sh`, `e1d2514cd6361f8201a6773a4cf108ac333aa7ca647807698b90c3abeb97a7c5` ; R-2778 »
- hors de ces valeurs, la ligne est égale à l'octet à celle du brouillon 4

### Différence 2 — Plan d'analyse (brouillon 4, l. 177-177 ; brouillon 13, l. 179-179)

- marqueur `RUN_7B` rempli : au brouillon 4, le nom du marqueur entre chevrons ; au brouillon 13 : « run `20261111-151701-t06-reel`, branche de sortie `calcul/t06-confirmation-7b-v1` (tête `55c3e3eb89a4650419f35999aaa4c54288275b0d`), manifeste `runs/20261111-151701-t06-reel/manifeste.json`, `7e1ac1f02584e4f8babf664e78d12f3122bfdca18292734f28281e9459479bf6` ; ligne inscrite le 2026-11-13T18:52:43Z »
- marqueur `EMPREINTES_ENTREES_7B` rempli : au brouillon 4, le nom du marqueur entre chevrons ; au brouillon 13 : « lues le 2026-11-22 sur les compagnons seuls, sans ouvrir les fichiers : `mesures-t06.npz`, `aca5afd068a8749952c7424a7708a1e4c8b78c082fba495d5d406f2605435049` ; `textes-actions-t06.jsonl`, `d196bb4fffd793dc52190aa2674aeff33619f17bd40d303f564515bde2ad783d` ; `episodes-t06.json`, `c7911933a6cc797db4be094bd252393bb4360cdc55a25867b624be721ccdb51c` ; `manifeste.json`, `7e1ac1f02584e4f8babf664e78d12f3122bfdca18292734f28281e9459479bf6` ; `lecture-cout-t06.json`, `c69884ed54b48ba5a37b17572060a3d2a6258a92ccf8b92d30beb11422196a1c` »
- hors de ces valeurs, la ligne est égale à l'octet à celle du brouillon 4

### Différence 3 — Plan d'analyse (brouillon 4, l. 181-180 ; brouillon 13, l. 183-183)

Ligne ajoutée (phrase T5-19, brouillon 5 ; gardée par le mot de Lazar, R-2657) :

>    - de la course de T0.8 elle-même, pour la lecture seulement : ses sorties scellées (`diag/<run-t08>/course-t08.json` et les fichiers qu'il cite sous `donnees/<run-t08>/`) et son manifeste (`runs/<run-t08>/manifeste.json`, pour son identifiant de run et son empreinte, qui le rattachent à `course-t08.json`, et pour sa date de création, rien d'autre n'en étant gardé : antériorité des lignes `SCELLEMENT-T08` et `CODE-T08` sur le début de la course, « avant toute exécution », en-tête), empreintes vérifiées contre leurs compagnons ; aucune donnée de 7b, aucune sonde, aucun résultat n'en est tiré au-delà de ce que nomment le plan et la « Métrique » (phrase ajoutée au brouillon 5, VCT8B-01 ; nœud de Lazar, VT5-03 : **gardée**, option (a), mot de Lazar « go a pour T5-19 » (journal du compte 4, C4-0054, `registres-provisoires/compte-4-2026-11-14-v16.md`, `190fb7ed632c52c36f3ece7d837b84d9f9529f830553bf46c1ae10021cec9288`) ; ligne du registre et confirmation de la session mère : `<<LIGNE_MOT_LAZAR_T5_19>>`) ;

## 2. La phrase T5-19 d'un brouillon à l'autre

Empreinte épinglée de la ligne (brouillon 10) : `906b82d6c063eb60cc0c6179d43fdbcbe0dbc434e430ac6026837fd0ae06cde4`. Table des brouillons 5 à 12 : `differentiel-gel-t08-brouillon12-v1.md`, section 2 ; la ligne du brouillon 13 est celle du brouillon 10 (contrôle (b) ci-dessus).

## 3. Hors des sections gelées : opérations du brouillon 12 au brouillon 13

| id | nature | section | motif |
|---|---|---|---|
| T13-01 | remplacer | en-tête | titre : brouillon 13 |
| T13-02 | remplacer_ligne | en-tête | statut du brouillon 13 |
| T13-03 | ajouter_en_fin_de_ligne | en-tête | auteur du brouillon 13 |
| T13-04 | ajouter_en_debut_de_valeur | en-tête | date du brouillon 13 |
| T13-05 | ajouter_en_fin_de_ligne | Ce que les auteurs savaient avant le scellement | déclaration de vue : ligne de GO lue |
| T13-06 | remplacer_ligne | Calendrier, et ce qui se passe s'il glisse | calendrier : garde d'antériorité tranchée |
| T13-07 | remplacer | Depuis le gel du 10 novembre : faits, déclarations et ce qui reste (brouillon 11) | table des gardes : source de la quatrième |
| T13-08 | remplacer | Depuis le gel du 10 novembre : faits, déclarations et ce qui reste (brouillon 11) | gardes de code : décision de Lazar, option (a) |
| T13-09 | remplacer_ligne | Depuis le gel du 10 novembre : faits, déclarations et ce qui reste (brouillon 11) | point 1 pour Lazar : tranché |
| T13-10 | remplacer | Contre-lecture | relecture : la vérification porte sur le brouillon 13 |
| T13-11 | remplacer | Marqueurs à remplir avant le scellement | vérification des marqueurs : brouillon 13 |
| T13-12 | remplacer_ligne | Marqueurs à remplir avant le scellement | table des marqueurs : sort de VT5-07 tranché |

Texte ancien et texte nouveau de chaque opération : `brouillons/t08-texte-complet-fable-v1/couples-t08-brouillon13-v1.json`. Opérations antérieures : différentiels des brouillons 11 et 12, même dossier, sections 3.

## 4. Opérations du brouillon 13 qui touchent une section gelée

Aucune (contrôlé par le programme).
