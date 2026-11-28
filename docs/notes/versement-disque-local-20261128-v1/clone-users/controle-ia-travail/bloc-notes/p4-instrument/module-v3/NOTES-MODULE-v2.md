# Notes du module de P4-instrument (v2) : corrections de CL3-01 et de CL3-03

Rédacteur de la correction : sous-agent lancé par la session le 2026-10-20 (vers 19:00 à 19:20 UTC). Je n'ai écrit ni le
préenregistrement, ni le module v1, ni la contre-lecture 3. Le préfixe `…/` vaut
`/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad`.

Sources :
- texte qui fait foi : `…/p4-instrument/P4-instrument-v1-candidat1.md`
  (`6422fb45a1dc2a3b42a5f6adad4ed8ff02cf89b3c09d91474213c5c1f5fe3bc0`), table « Critères de lecture gelés » et « Liste
  d'arrêt » ;
- contre-lecture 3 : `…/p4-instrument/contre-lecture-3/contre-lecture-3-P4-instrument-candidat1-v1.md`
  (`7f947de00aa58b0635fe2b6f0ad3c22eb7dbcb48ed0c8079f65a57abb13b5368`), constats CL3-01 (majeur) et CL3-03 (mineur) ;
- module v1 : `…/p4-instrument/module/` (intact ; ses sept sceaux vérifiés après le travail). Ses notes,
  `NOTES-MODULE.md` (`7a82f3b7…`), sont copiées ici sans changement et restent valables pour tout ce que ces notes-ci
  ne changent pas.

Rien d'autre n'a changé : ni la logique de `issue_p4`, ni les statistiques, ni le run, ni les mesures de conception.

## Ce qui change, et pourquoi

### CL3-01 : une lecture sans `--prereg` lisait un run décisif, avant le verdict complété de P3

Dans le v1, toutes les gardes du mode décisif étaient sous `if prereg is not None`. Sans `--prereg`, `analyser` lisait un
run décisif et écrivait C1 (démonstration de la contre-lecture 3). La garde voulue par R-262 se contournait en omettant
un argument.

Dans `lecture_p4_v1.py` :
- `analyser` : sans `--prereg`, avant `creer_manifeste` et avant toute écriture, un run source dont le manifeste est
  décisif ou porte `config.mode == "reel"` est refusé : `GardeArret("lecture sans préenregistrement d'un run décisif ou
  réel : refusée sans rien écrire")` (constante `MOTIF_SANS_PREREG`). Le manifeste compte s'il est vérifié ; s'il est
  présent mais que son sceau ne tient plus, son contenu brut compte aussi (`_manifeste_brut`).
- Règle commune : `exiger_lecture_permise(manifeste, lien)`. Un run ni décisif ni réel se lit sans rien. Un run décisif
  ou réel exige le lien écrit par `analyser` quand toutes les gardes du mode décisif ont passé
  (`gardes_decisives_passees` : aucun refus, run source vérifié, verdict complété de P3, table des critères égale).
- Autres voies :
  - `charger_source_p4(racine, run_id, lien=None)` applique la règle dès le manifeste lu, avant toute autre lecture, et
    garde le lien dans la source chargée ;
  - `lire(source, …)` applique la règle à toute source chargée qui porte un manifeste ;
  - la ligne de commande passe par `analyser` (refus : « ARRÊT : … », code 1).
- Un run jouet non décisif reste lisible sans `--prereg` : c'est la répétition jouet de la chaîne, en mode non décisif.
- Manifeste absent, ou illisible et non analysable : comme avant, rien du run n'est lu, et la lecture écrit L1
  (« manifeste absent ou illisible »). En mode non décisif, cette L1 s'écrit sous un manifeste de lecture non décisif.

### CL3-03 : la table du code n'était plus celle du texte pour L1 et L4

- `LIGNES` : les cellules L1 (issue) et L4 (issue et lecture) sont recopiées du candidat 1, mot pour mot. Les onze
  lignes ont été comparées, cellule par cellule, à la table du candidat. Avant : trois cellules différentes (L1 issue,
  L4 issue, L4 lecture), exactement celles de CL3-03. Après : vingt-deux cellules égales, aucune différente.
- Garde neuve de la lecture décisive, `exiger_table_des_criteres(texte)` : elle relit la table « Critères de lecture
  gelés » du préenregistrement passé par `--prereg` (`table_des_criteres` : section lue par `controle_ia.prereg.sections`,
  cellules séparées par les « | » non échappés, « \| » rendu « | »). Mêmes lignes, même ordre, mêmes issues, mêmes
  lectures, sinon refus. Elle est appelée juste après `exiger_prereg_scelle`, avant le verdict complété et avant tout
  manifeste de lecture : rien n'est écrit. Son résultat est écrit dans le lien (`table_des_criteres`).
- Docstrings et commentaires : « brouillon 4 (`32d821fb…`) » devient « le préenregistrement scellé
  (`prereg/P4-instrument-v1.md`) ». Fichiers touchés : `lecture_p4_v1.py` (en-tête, commentaire de `LIGNES`),
  `test_lecture_p4_v1.py` et `test_gardes_p4_v1.py` (en-têtes), `instrument_p4_v1.py` (en-tête, lignes 3 et 4 :
  docstring seule, aucun code changé).

## Fichiers

| fichier | changement |
|---|---|
| `mesures_conception_p4_v1.py` | aucun (`483b8ac3…`, sceau v1 copié) |
| `instrument_p4_v1.py` | docstring seule, lignes 3 et 4 (CL3-03) |
| `lecture_p4_v1.py` | CL3-01 et CL3-03 (ci-dessus) |
| `test_instrument_p4_v1.py` | aucun (`9d015be4…`, sceau v1 copié ; 71 tests) |
| `test_lecture_p4_v1.py` | en-tête ; compte 42 → 43 ; un test neuf (table du texte, variable d'environnement) |
| `test_gardes_p4_v1.py` | en-tête ; compte 81 → 101 ; la table de `LIGNES` dans le préenregistrement synthétique (`table_markdown`) ; vingt tests neufs |
| `NOTES-MODULE.md` | aucun (copie du v1, `7a82f3b7…`) |
| `NOTES-MODULE-v2.md` | neuf (ces notes) |

## Section du texte → fonction (ajouts au tableau de `NOTES-MODULE.md`)

| section | fonction |
|---|---|
| Plan d'analyse, point 2 ; Liste d'arrêt (lecture sans `--prereg` d'un run décisif ou réel) | `lecture.analyser`, `lecture.exiger_lecture_permise`, `lecture.est_decisif_ou_reel`, `lecture.gardes_decisives_passees`, `lecture.charger_source_p4(…, lien)`, `lecture.lire` |
| Critères de lecture gelés (table relue au texte) | `lecture.LIGNES`, `lecture.table_des_criteres`, `lecture.exiger_table_des_criteres` |

## Tests

- Comptes : `test_instrument_p4_v1.py` 71, `test_lecture_p4_v1.py` 43, `test_gardes_p4_v1.py` 101 ; total 215. Chaque
  fichier écrit son nombre en tête et le vérifie par un test.
- Neufs, chaque fois cas sain et artefact (R5) :
  - CL3-01 (`test_gardes_p4_v1.py`) :
    - sain : run jouet non décisif lu sans `--prereg`, `lecture-p4.json` écrit sous un manifeste non décisif ;
    - artefacts, chaque fois refus au motif exact, aucun dossier `runs/<lecture>` ni `diag/<lecture>`, arbre propre :
      run décisif jouet (reprise de la démonstration : la lecture décisive attend le verdict complété, puis la lecture
      sans `--prereg` est refusée) ; run en mode réel (manifeste réécrit, cohérent et rescellé, sans modèle réel) ;
      manifeste décisif dont le sceau ne tient plus ;
    - ligne de commande : « ARRÊT » avec le motif, code 1, rien d'écrit, aucun `__pycache__` ;
    - autres voies : `charger_source_p4` et `lire` sans lien, ou avec un lien incomplet, refusent ; avec un lien de la
      forme écrite par `analyser`, elles chargent et lisent ;
    - règle `exiger_lecture_permise` : trois cas permis sans lien (pas de manifeste, jouet, mode absent), quatre permis
      avec le lien complet ; trois manifestes décisifs ou réels refusés contre sept liens absents ou incomplets ;
    - voie décisive saine : toutes les gardes passées, le run décisif est lu sous un manifeste de lecture décisif. Le
      jouet ne peut pas passer la garde « mode réel » : `exiger_lecture_sous_prereg_p4`, éprouvée par ses propres tests,
      y est remplacée par un lien de sa forme.
  - CL3-03 :
    - `test_gardes_p4_v1.py` : table saine (barres de L11 échappées) ; dix artefacts refusés (issue de L1 et lecture de
      L4 du module v1, signe moins devenu tiret dans L11, ligne absente, en trop, en double, ordre autre, barre non
      échappée, section sans table, section absente) ; à la lecture décisive, préenregistrement scellé à la table autre :
      refus, rien d'écrit (cas sain sur le même dépôt : la garde passe et son résultat est écrit) ;
    - `test_lecture_p4_v1.py` : `LIGNES` contre la table du texte nommé par la variable d'environnement
      `P4_TEXTE_PREREG` (lecture recodée hors du module, puis la garde). Variable absente ou fichier absent : le test
      ÉCHOUE avec un message clair ; il ne saute jamais. Éprouvé ici : candidat 1, passé ; brouillon 4, échec sur
      exactement L1 issue, L4 issue, L4 lecture ; variable absente, échec ; fichier absent, échec.
- Le préenregistrement synthétique des tests porte maintenant la table de `LIGNES`. Sans elle, la garde neuve aurait
  refusé les lectures décisives des tests existants.

### Commande exacte de la suite

Depuis la racine du dépôt, une fois le module versé sous `docs/procedures/P4-instrument-v1/` et le texte scellé (S) :

```
P4_TEXTE_PREREG=prereg/P4-instrument-v1.md PYTHONPATH=src python -B -m pytest -q -p no:cacheprovider docs/procedures/P4-instrument-v1/test_instrument_p4_v1.py docs/procedures/P4-instrument-v1/test_lecture_p4_v1.py docs/procedures/P4-instrument-v1/test_gardes_p4_v1.py
```

Avant S, `P4_TEXTE_PREREG` nomme le candidat relu. Commande lancée ici (dépôt lu seulement, commit `bbc4e49` puis
`37852d6`, ce dernier écrit par la session pendant mes essais : une ligne de `registres/decisions.md`) :

```
cd /home/user/controle-ia-travail && P4_TEXTE_PREREG=…/p4-instrument/P4-instrument-v1-candidat1.md PYTHONPATH=src PYTHONDONTWRITEBYTECODE=1 /tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad/scellement-revalidation/venv-gpu-neuf/bin/python -B -m pytest -q -p no:cacheprovider --basetemp=…/p4-instrument/module-v2-travail/tmp-suite …/p4-instrument/module-v2/test_instrument_p4_v1.py …/p4-instrument/module-v2/test_lecture_p4_v1.py …/p4-instrument/module-v2/test_gardes_p4_v1.py
```

Dernière ligne : `215 passed in 134.92s (0:02:14)`, code 0. Sortie : `…/p4-instrument/module-v2-travail/sortie-tests-module-v2.txt`
(`f5e8deece1ee9b31b2da9dfb9cae08b637d3dba99eacd55ea55f91100c1a74e7`).

### La démonstration de la contre-lecture 3, rejouée contre le v2

Fichier inchangé (`…/contre-lecture-3/travail/module/test_demo_cl3_lecture_non_decisive.py`, `0e1dcdcc…`), importé
contre le v2 par `--import-mode=append` et `PYTHONPATH=src:…/p4-instrument/module-v2` :
- la lecture décisive est refusée comme avant (verdict complété absent) ;
- la lecture sans `--prereg`, qui lisait le run et écrivait C1 dans le v1, lève maintenant
  `GardeArret: lecture sans préenregistrement d'un run décisif ou réel : refusée sans rien écrire`
  (`module-v2/lecture_p4_v1.py`) ;
- la démonstration échoue donc (`1 failed`), comme attendu ; son dépôt jetable n'a aucun run ni diag de lecture.

Sortie : `…/p4-instrument/module-v2-travail/sortie-demo-cl3-01-module-v2.txt`
(`9fad94a779a0295757c61ebf38e0e95dcc8e9b643dac2637a3d5ad1e4f9cd243`).

## À reporter dans le texte et dans la chaîne

- Lignes « Module de P4 » du texte : nouvelles empreintes (ci-dessous) pour `instrument_p4_v1.py`, `lecture_p4_v1.py`,
  `test_lecture_p4_v1.py` et `test_gardes_p4_v1.py` ; les deux autres sont inchangées.
- « Tests attendus » : 1 123 (908 + 215 ; 71, 43 et 101).
- Liste d'arrêt et « Tests (R5) » : phrases données dans `RAPPORT-CORRECTION-v1.md`.
- Chaîne : toute exécution de la suite du module, sur la machine de la session comme sur l'instance, doit passer
  `P4_TEXTE_PREREG`, sinon un test échoue. La répétition jouet ne peut plus lire sans `--prereg` un run décisif jouet ;
  elle lit un run jouet non décisif, ou lit le run décisif jouet en mode décisif (L1, « hors du mode réel »). Je n'ai pas
  lu la chaîne : à vérifier par la session.

## Empreintes (sha256)

Chaque fichier a son compagnon `.sha256`, au format « <empreinte>  <nom> ».

| fichier | sha256 | état |
|---|---|---|
| `mesures_conception_p4_v1.py` | `483b8ac3aca65a9879b7d2f2a832cfd5478c48fd860c94a6fbdc041364cc8be7` | inchangé |
| `instrument_p4_v1.py` | `c3e78becc07a1e265490c96842ae810dbee72a0a52c3d0cab195fede851621fc` | docstring seule (v1 : `6e0e026e…`) |
| `lecture_p4_v1.py` | `3e41ec106589f9cd6907543ebf4b6e83ed74637f1e40e69ec9c65a15c5b38579` | changé (v1 : `51a25e30…`) |
| `test_instrument_p4_v1.py` | `9d015be4ce2bbff4a4541387d5d19ef70497aa41f1a53b9c38724360d7a1dffd` | inchangé |
| `test_lecture_p4_v1.py` | `7f1bceb1a73f40df227181d9fd53c421251203eed1dc2b1ed625c1c23126c736` | changé (v1 : `49441971…`) |
| `test_gardes_p4_v1.py` | `42af1efcadf0f252c5af7a8c7826ebdd333f0f837e5bf4a0753fbccb87e08be0` | changé (v1 : `f4f97029…`) |
| `NOTES-MODULE.md` | `7a82f3b7770c36a15afbf8065e3f1f92424e533ac0ffa02bb066eabfedc958cc` | copie du v1 |
