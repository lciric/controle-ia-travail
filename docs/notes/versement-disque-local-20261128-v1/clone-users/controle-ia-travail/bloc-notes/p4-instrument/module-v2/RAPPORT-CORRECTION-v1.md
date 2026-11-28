# Rapport de correction du module de P4-instrument : CL3-01 et CL3-03 (module v2) — v1

Rédacteur : sous-agent lancé par la session le 2026-10-20 (vers 19:00 à 19:25 UTC). Je n'ai écrit ni le
préenregistrement, ni le module v1, ni la contre-lecture 3. Le préfixe `…/` vaut
`/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad`.

## Verdict

**Corrigé.** CL3-01 et CL3-03 sont corrigés dans `…/p4-instrument/module-v2/`. La suite du module v2 passe : 215 tests
(71, 43, 101). La démonstration de la contre-lecture 3, rejouée sans changement contre le v2, échoue au refus neuf, comme
attendu. Rien d'autre n'a changé. Le dossier `…/p4-instrument/module/` est intact.

À reporter dans le texte (candidat 2) : lignes « Module de P4 », « Tests attendus » (1 123), Liste d'arrêt, « Tests
(R5) ». Phrases exactes à la fin de ce rapport.

## Pièces relues

| pièce | sha256 |
|---|---|
| `…/p4-instrument/P4-instrument-v1-candidat1.md` (texte qui fait foi) | `6422fb45a1dc2a3b42a5f6adad4ed8ff02cf89b3c09d91474213c5c1f5fe3bc0` (égale à la citation) |
| `…/p4-instrument/contre-lecture-3/contre-lecture-3-P4-instrument-candidat1-v1.md` | `7f947de00aa58b0635fe2b6f0ad3c22eb7dbcb48ed0c8079f65a57abb13b5368` (égale) |
| `…/contre-lecture-3/travail/module/test_demo_cl3_lecture_non_decisive.py` | `0e1dcdcc30256eee3aa5e7f33d59d3c4d4125a4f5ccd16914c6ac2a1129f1ac6` |
| `…/contre-lecture-3/travail/sortie-demo-cl3-01.txt` | `792659c00bd25a6b82e3f004d8fa3b7139a551231f2e494b026fa96428498955` |
| module v1, sept fichiers | empreintes de la tâche, égales ; sept sceaux vérifiés avant et après |

Code gelé lu, en lecture seule, pour les appels de la lecture : `src/controle_ia/manifeste.py` (`creer_manifeste`,
`lire_manifeste`, `ecrire_resultat`, `verifier_resultat`), `src/controle_ia/prereg.py` (`SECTIONS`, `sections`,
`exiger_prereg_scelle`), `src/controle_ia/scellement.py` (`sceller`).

Non lus : `prereg/P3-consignes-v1.md`, tout fichier `textes-actions-*`, la chaîne (`…/p4-instrument/chaine/`) et ses
relectures. La suite du module, par son test existant `test_registres_reels_du_depot_go_cite_conforme_au_2026_10_20`,
lit `registres/go.md` et `registres/decisions.md` du dépôt, comme au v1 ; je ne les ai pas ouverts moi-même.

## Cadre tenu

- Dépôt `/home/user/controle-ia-travail` en lecture seule. `git status --porcelain` vide avant et après. Les dossiers
  `__pycache__` du dépôt (hors `donnees/`, `.venv/`, `.git/`) sont les mêmes avant et après, mêmes dates (12). Aucun
  `__pycache__` ni `.pyc` dans `module/`, `module-v2/`, `contre-lecture-3/`.
- Python : `…/5a6b9d1d-…/scratchpad/scellement-revalidation/venv-gpu-neuf/bin/python`, avec `-B`,
  `PYTHONDONTWRITEBYTECODE=1`, `-p no:cacheprovider` ; fichiers temporaires des tests sous
  `…/p4-instrument/module-v2-travail/` (`--basetemp`).
- Le commit de tête du dépôt est passé de `bbc4e49` à `37852d6` pendant mes essais. Ce commit est celui de la session
  (R-291, une ligne de `registres/decisions.md`), pas le mien.
- Une fois, au début, un `find` par nom (sans lire aucun contenu) a parcouru l'arbre du dépôt, `donnees/` compris, pour
  compter les dossiers `__pycache__`. Seul le compte a été affiché. Les relevés suivants excluent `donnees/`.
- Aucune commande Vast.ai, aucun réseau, aucune clé. Aucune moyenne ni médiane sur les jetons ajoutée.
- R12 : dossier neuf `module-v2/`, mêmes noms de fichiers, car le texte et la chaîne les citent par ces noms ; notes
  neuves sous un nom neuf (`NOTES-MODULE-v2.md`) ; `NOTES-MODULE.md` copié sans changement.

## Changements

### CL3-01 (majeur) : lecture sans `--prereg` d'un run décisif ou réel

- `lecture_p4_v1.analyser` : sans `--prereg`, avant `creer_manifeste` et avant toute écriture, refus par `GardeArret`
  si le manifeste du run source est décisif ou porte `config.mode == "reel"`. Message exact : « lecture sans
  préenregistrement d'un run décisif ou réel : refusée sans rien écrire » (`MOTIF_SANS_PREREG`). Le manifeste vérifié
  compte. S'il est présent mais que son sceau ne tient plus, son contenu brut compte aussi.
- Règle unique, `exiger_lecture_permise(manifeste, lien)`. Un run décisif ou réel exige le lien écrit par `analyser`
  après toutes les gardes du mode décisif : aucun refus, run source vérifié, verdict complété de P3, table des critères
  égale (`gardes_decisives_passees`).
- Autres chemins d'entrée, vérifiés un par un :
  - `charger_source_p4(racine, run_id, lien=None)` : la règle s'applique dès le manifeste lu, avant toute autre lecture ;
  - `lire(source, …)` : la règle s'applique à toute source chargée qui porte un manifeste ;
  - ligne de commande (`_main`) : elle passe par `analyser` ; refus « ARRÊT : … », code 1.
- Un run jouet non décisif reste lisible sans `--prereg` (répétition jouet de la chaîne, en mode non décisif).

### CL3-03 (mineur) : table du code et table du texte

- `LIGNES` : cellules L1 (issue) et L4 (issue et lecture) recopiées du candidat 1, mot pour mot.
- Les onze lignes ont été comparées cellule par cellule au texte, par un script hors du module
  (`…/p4-instrument/module-v2-travail/comparer_table_v1.py`, `8d5cedcafb7ade96bca7f0f9e8a55e18f7b357e4ae8421ae343bb0c23594fe8b`).
  Avant : trois différences, exactement L1 issue, L4 issue, L4 lecture. Après : 22 cellules égales. Le texte ne contient
  aucune espace insécable dans la table.
- Garde neuve de la lecture décisive : `exiger_table_des_criteres` relit la table « Critères de lecture gelés » du
  préenregistrement passé par `--prereg`. Mêmes lignes, même ordre, mêmes cellules, sinon refus. Elle s'applique juste
  après `exiger_prereg_scelle`, avant le verdict complété et avant tout manifeste : rien n'est écrit. Son résultat est
  écrit dans le lien.
- Docstrings et commentaires « brouillon 4 (`32d821fb…`) » → « le préenregistrement scellé
  (`prereg/P4-instrument-v1.md`) » : `lecture_p4_v1.py` (en-tête, commentaire de `LIGNES`), `test_lecture_p4_v1.py` et
  `test_gardes_p4_v1.py` (en-têtes), `instrument_p4_v1.py` (lignes 3 et 4 de l'en-tête).

### Fichiers inchangés, ou changés seulement dans leur docstring

- `mesures_conception_p4_v1.py` : inchangé (`483b8ac3…`).
- `test_instrument_p4_v1.py` : inchangé (`9d015be4…`, 71 tests).
- `instrument_p4_v1.py` : docstring seule. Le `diff` ne montre que les lignes 3 et 4 de l'en-tête ; aucun code changé.
  Son empreinte change donc : `6e0e026e…` → `c3e78bec…`.

## Tests (nombres exacts)

| fichier | v1 | v2 | sortie |
|---|---|---|---|
| `test_instrument_p4_v1.py` | 71 | 71 | 71 passés |
| `test_lecture_p4_v1.py` | 42 | 43 | 43 passés (avec `P4_TEXTE_PREREG` = candidat 1) |
| `test_gardes_p4_v1.py` | 81 | 101 | 101 passés |
| **total** | 194 | **215** | **215 passed in 134.92s**, code 0 |

- Suite complète, les trois fichiers ensemble : `…/p4-instrument/module-v2-travail/sortie-tests-module-v2.txt`
  (`f5e8deece1ee9b31b2da9dfb9cae08b637d3dba99eacd55ea55f91100c1a74e7`). Chaque fichier vérifie son propre compte.
- Lancements séparés : gardes seules, 101 passés (67,96 s) ; lecture seule, 43 passés (82,35 s).
- Test de la table du texte, artefacts (R5) :
  - sans `P4_TEXTE_PREREG` : 1 échec, message « P4_TEXTE_PREREG absente : … », 42 passés ;
  - avec le brouillon 4 : échec sur `[('L1', 'issue'), ('L4', 'issue'), ('L4', 'lecture')]` ;
  - avec un chemin absent : échec « fichier absent sur disque (R11) ».
- Démonstration de la contre-lecture 3, fichier inchangé, rejouée contre le v2 (`--import-mode=append`,
  `PYTHONPATH=src:…/p4-instrument/module-v2`) : **1 failed**, comme attendu. La lecture décisive est refusée (verdict
  complété absent). La lecture sans `--prereg` lève `GardeArret: lecture sans préenregistrement d'un run décisif ou
  réel : refusée sans rien écrire`, depuis `module-v2/lecture_p4_v1.py`. Son dépôt jetable n'a ni run ni diag de lecture.
  Sortie : `…/p4-instrument/module-v2-travail/sortie-demo-cl3-01-module-v2.txt`
  (`9fad94a779a0295757c61ebf38e0e95dcc8e9b643dac2637a3d5ad1e4f9cd243`). La démonstration est aussi reprise comme test
  dans `test_gardes_p4_v1.py` (premier artefact de
  `test_lecture_sans_prereg_d_un_run_decisif_ou_reel_refusee_sans_rien_ecrire`), qui affirme le refus.

Tests neufs (cas sain et artefact, R5) : voir `NOTES-MODULE-v2.md`, section « Tests ».

Commande exacte de la suite, une fois le module versé et le texte scellé :

```
P4_TEXTE_PREREG=prereg/P4-instrument-v1.md PYTHONPATH=src python -B -m pytest -q -p no:cacheprovider docs/procedures/P4-instrument-v1/test_instrument_p4_v1.py docs/procedures/P4-instrument-v1/test_lecture_p4_v1.py docs/procedures/P4-instrument-v1/test_gardes_p4_v1.py
```

## Constats et réserves

- **CR-01, réserve (chaîne).** Toute exécution de la suite du module doit passer `P4_TEXTE_PREREG` : machine de la
  session, répétitions et instance (« la suite complète tourne aussi sur l'instance avant le run »). Sinon un test
  échoue, et ne saute jamais. Le lanceur et ses contrôles doivent l'exporter. Je n'ai pas lu la chaîne.
- **CR-02, réserve (chaîne).** La répétition jouet ne peut plus lire sans `--prereg` un run décisif jouet : refus. Elle
  doit lire un run jouet non décisif, ou lire le run décisif jouet en mode décisif (issue L1, « hors du mode réel »). À
  vérifier dans les scripts de la chaîne.
- **CR-03, limite.** Le lien des gardes est un dictionnaire. Un appelant qui le fabrique passe la règle, comme le font
  deux tests (voie décisive saine ; autres voies). La garde empêche l'omission d'un argument, pas une fraude
  délibérée. Dans le module, seul `analyser` construit ce lien.
- **CR-04, limite.** Manifeste du run source absent, ou présent mais illisible comme JSON, sans `--prereg` : rien du run
  n'est lu, et la lecture écrit L1 (« manifeste absent ou illisible ») sous un manifeste non décisif. C'est le
  comportement du v1, gardé. Décisif ou réel n'y est pas exclu, mais aucune donnée du run n'est lue.
- **CR-05, information.** La garde de table est stricte : un seul signe change le résultat (moins devenu tiret : refus).
  Toute retouche d'une cellule de la table au candidat 2 doit être recopiée dans `LIGNES`, avec de nouvelles empreintes,
  sinon la lecture décisive refuse. Les corrections proposées par CL3-05 (paragraphe « Réserves ») et CL3-11
  (précision 9) ne touchent aucune ligne « | Lk | » : la garde ne lit que ces lignes.
- **CR-06, information.** `instrument_p4_v1.py` change d'empreinte pour sa seule docstring. La sortie de MC avait déjà
  été produite avec une autre empreinte de l'instrument (`90b9ae8b…`, point 23 de `NOTES-MODULE.md`). Aucune fonction
  appelée par MC ne change.
- **CR-07, suggestion facultative (texte).** Le plan d'analyse, point 2, énumère les gardes du mode décisif. On peut y
  ajouter, après « module à l'empreinte citée (`exiger_module_cite`) ; » : « table « Critères de lecture gelés » de ce
  texte égale à celle du module, cellule par cellule (sinon refus, rien n'est écrit) ; ». Non demandé ; la Liste d'arrêt
  suffit à fixer la règle.

## Texte à ajouter au candidat (phrases exactes)

1. Liste d'arrêt, remplacer la ligne des lignes 708 et 709 par :
   « - Lecture demandée avant le scellement du verdict complété de P3 (addendum 2), ou avant le scellement de ce texte,
   ou sans `--prereg` sur un run source décisif ou en mode réel : refusée sans rien écrire et reportée (pas une ligne). »
2. Liste d'arrêt, ligne neuve (après la précédente) :
   « - Lecture décisive dont la table « Critères de lecture gelés » de ce texte diffère de la table du module (`LIGNES`
   de `lecture_p4_v1.py`) d'une cellule, d'une ligne ou de l'ordre : refusée sans rien écrire (pas une ligne) ; écart
   entre le texte et le module : nœud. »
3. « Tests (R5) », à la fin de la liste, à la place du point final après « C1 au pas 0 et Δ net recalculés à la main
   sur un jeu synthétique » :
   « ; lecture sans `--prereg` d'un run décisif ou en mode réel (doit refuser sans rien écrire), contre un run jouet non
   décisif (doit lire) ; table « Critères de lecture gelés » de ce texte différente d'une cellule de la table du module
   (doit refuser sans rien écrire), et table du module égale à celle de ce texte, cellule par cellule (test lancé avec
   `P4_TEXTE_PREREG`, qui échoue sans elle). »
4. « Tests attendus », nouvelle valeur de la ligne entière :
   « - Tests attendus : 1 123, soit les 908 de la suite du dépôt au commit de P3 (`prereg/P3-premier-test-i-a-v1.md`
   l. 41 ; 908 passés sur le dépôt de travail le 2026-10-20, R-285) et les 215 du module de P4 (71, 43 et 101 ; chaque
   fichier écrit son nombre et le vérifie ; la suite du module se lance avec `P4_TEXTE_PREREG=prereg/P4-instrument-v1.md`,
   sans quoi le test qui compare la table du module à celle de ce texte échoue). La suite complète tourne aussi sur
   l'instance avant le run, comme pour P3 : l'économie d'environ 30 minutes (plan v1, 5.2, question) est refusée
   (contre-lecture 2, VP3-12). »
5. Lignes « Module de P4 » (empreintes du module v2) :
   - Module de P4 : `docs/procedures/P4-instrument-v1/mesures_conception_p4_v1.py` : `483b8ac3aca65a9879b7d2f2a832cfd5478c48fd860c94a6fbdc041364cc8be7`
   - Module de P4 : `docs/procedures/P4-instrument-v1/instrument_p4_v1.py` : `c3e78becc07a1e265490c96842ae810dbee72a0a52c3d0cab195fede851621fc`
   - Module de P4 : `docs/procedures/P4-instrument-v1/lecture_p4_v1.py` : `3e41ec106589f9cd6907543ebf4b6e83ed74637f1e40e69ec9c65a15c5b38579`
   - Module de P4 : `docs/procedures/P4-instrument-v1/test_instrument_p4_v1.py` : `9d015be4ce2bbff4a4541387d5d19ef70497aa41f1a53b9c38724360d7a1dffd`
   - Module de P4 : `docs/procedures/P4-instrument-v1/test_lecture_p4_v1.py` : `7f1bceb1a73f40df227181d9fd53c421251203eed1dc2b1ed625c1c23126c736`
   - Module de P4 : `docs/procedures/P4-instrument-v1/test_gardes_p4_v1.py` : `42af1efcadf0f252c5af7a8c7826ebdd333f0f837e5bf4a0753fbccb87e08be0`

## Pièces écrites

Sous `…/p4-instrument/module-v2/` (chaque fichier avec son compagnon `.sha256`, au format « <empreinte>  <nom> ») :

| fichier | sha256 |
|---|---|
| `mesures_conception_p4_v1.py` (inchangé) | `483b8ac3aca65a9879b7d2f2a832cfd5478c48fd860c94a6fbdc041364cc8be7` |
| `instrument_p4_v1.py` (docstring seule) | `c3e78becc07a1e265490c96842ae810dbee72a0a52c3d0cab195fede851621fc` |
| `lecture_p4_v1.py` | `3e41ec106589f9cd6907543ebf4b6e83ed74637f1e40e69ec9c65a15c5b38579` |
| `test_instrument_p4_v1.py` (inchangé) | `9d015be4ce2bbff4a4541387d5d19ef70497aa41f1a53b9c38724360d7a1dffd` |
| `test_lecture_p4_v1.py` | `7f1bceb1a73f40df227181d9fd53c421251203eed1dc2b1ed625c1c23126c736` |
| `test_gardes_p4_v1.py` | `42af1efcadf0f252c5af7a8c7826ebdd333f0f837e5bf4a0753fbccb87e08be0` |
| `NOTES-MODULE.md` (copie du v1) | `7a82f3b7770c36a15afbf8065e3f1f92424e533ac0ffa02bb066eabfedc958cc` |
| `NOTES-MODULE-v2.md` | dans son compagnon `NOTES-MODULE-v2.md.sha256` |
| `RAPPORT-CORRECTION-v1.md` (ce rapport) | dans son compagnon `RAPPORT-CORRECTION-v1.md.sha256` |

Sous `…/p4-instrument/module-v2-travail/` : `sortie-tests-module-v2.txt`, `sortie-demo-cl3-01-module-v2.txt`,
`comparer_table_v1.py` (empreintes ci-dessus, compagnons écrits), relevés `git-status-avant.txt`, `pycache-avant.txt`,
`pycache-apres.txt`, et les dossiers temporaires des tests (`tmp-*`, dépôts jetables du modèle jouet).
