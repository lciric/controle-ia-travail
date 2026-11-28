# Vérification du module v2 de P4-instrument, lentille « contournement » (adverse) — v1

Vérificateur : sous-agent neuf, lancé le 2026-10-20 (vers 19:20 à 19:55 UTC). Je n'ai écrit ni le module v1, ni le module
v2, ni le texte, ni la contre-lecture 3. Le préfixe `…/` vaut `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad`.

## Verdict

**Conforme après corrections.** Par toutes les voies normales, le module v2 refuse de lire un run décisif du modèle
jouet sans verdict complété de P3, et refuse avant toute écriture. La garde de table refuse une table autre dans la
forme du texte. Deux voies restent ouvertes, toutes deux délibérées :

- **VM2-contournement-01 (mineur).** La garde de CL3-01 regarde le manifeste de `runs/<run source>/`. Les données, elles,
  sont rattachées au run nommé dans `resume.json`. Trois copies de fichiers scellés (ou un lien symbolique), sans rien
  resceller, suffisent : la ligne de commande, sans `--prereg`, lit alors le run décisif et calcule C1 (aire 0,5556,
  la valeur de la démonstration de CL3-01). Aucun verdict complété n'est versé.
- **VM2-contournement-02 (mineur).** La garde de table ignore sans le dire une rangée hors de la forme `| Lk |`. Une
  lecture décisive passe donc sous un texte scellé à douze rangées : lien écrit « 22 cellules égales ».

Aucune voie normale ne mène à l'une ou à l'autre. Corrections courtes, proposées plus bas. La correction de 01 est
simulée hors du module (V09) : elle ferme les trois formes et laisse lire le run jouet non décisif.

## Pièces relues

| pièce | sha256 |
|---|---|
| `…/p4-instrument/P4-instrument-v1-candidat1.md` (texte qui fait foi) | `6422fb45a1dc2a3b42a5f6adad4ed8ff02cf89b3c09d91474213c5c1f5fe3bc0` (égale à la citation) |
| `…/p4-instrument/contre-lecture-3/contre-lecture-3-P4-instrument-candidat1-v1.md` | `7f947de00aa58b0635fe2b6f0ad3c22eb7dbcb48ed0c8079f65a57abb13b5368` (égale) |
| `…/p4-instrument/module-v2/RAPPORT-CORRECTION-v1.md` | `1272a2bbda7d8a4da5830a9a4e7fbef14cc2f78c3e0e21971c1373afe74fde22` (égale à son compagnon) |
| `…/p4-instrument/module-v2/NOTES-MODULE-v2.md` | `ad731c278344f89bdc5af96f998d33f5a958d1c879ab80336b7f0849b32081ab` (égale) |
| `…/p4-instrument/module-v2/lecture_p4_v1.py` | `3e41ec106589f9cd6907543ebf4b6e83ed74637f1e40e69ec9c65a15c5b38579` (égale) |
| `…/p4-instrument/module-v2/instrument_p4_v1.py` | `c3e78becc07a1e265490c96842ae810dbee72a0a52c3d0cab195fede851621fc` (égale) |
| `…/p4-instrument/module-v2/test_gardes_p4_v1.py` | `42af1efcadf0f252c5af7a8c7826ebdd333f0f837e5bf4a0753fbccb87e08be0` (égale) |
| `…/p4-instrument/module-v2/test_lecture_p4_v1.py` | `7f1bceb1a73f40df227181d9fd53c421251203eed1dc2b1ed625c1c23126c736` (égale) |
| `…/p4-instrument/module-v2/test_instrument_p4_v1.py` | `9d015be4ce2bbff4a4541387d5d19ef70497aa41f1a53b9c38724360d7a1dffd` (égale) |
| `…/p4-instrument/module/` (v1, sept fichiers) | empreintes de la tâche, égales ; sept sceaux vérifiés après le travail |

Lus aussi, en lecture seule : la démonstration de CL3-01 et sa sortie ; `NOTES-MODULE.md` ; dans le dépôt,
`src/controle_ia/manifeste.py`, `src/controle_ia/prereg.py`, `src/controle_ia/scellement.py`.
Non lus : `prereg/P3-consignes-v1.md`, tout fichier `textes-actions-*`, rien sous `donnees/`, la chaîne de lancement
(`…/p4-instrument/chaine/`).

## Cadre tenu

- Dépôt de travail en lecture seule. `git --no-optional-locks status --porcelain` vide avant et après. Commit de tête
  `37852d6` avant et après. Aucune recherche récursive dans le dépôt.
- Python de la tâche, avec `-B`, `PYTHONDONTWRITEBYTECODE=1`, `-p no:cacheprovider`. Aucun `__pycache__` ni `.pyc` dans
  `module/`, `module-v2/` ni dans mon dossier.
- Modèle jouet et dépôts jetables seulement (montage des tests du module v2 : `run_decisif_jouet`, `_depot_de_lecture`).
  Aucune commande Vast.ai, aucun réseau, aucune clé. Aucune moyenne ni médiane sur les jetons.
- Écrit seulement sous `…/p4-instrument/verification-module-v2-contournement/`. `module/` et `module-v2/` intacts.

## Tests

- Suite du module v2, relancée par moi (`P4_TEXTE_PREREG` = candidat 1) : **215 passed** in 128.88s, code 0.
  Sortie : `travail/sortie-suite-module-v2.txt`.
- Mes voies adverses : `travail/test_contournement_vm2_v3.py`, **44 passed** (une ligne « VOIE » par test, dans
  `travail/voies-v3.txt`). Chaque test décrit ce qui est constaté, il ne le juge pas.
- Versions de travail gardées (R12) : v1, 40 passés et 1 échec (mon affirmation sur `x/../<run>` était fausse ; voie
  corrigée en v2). v2, 43 passés et 1 échec (dépôt jetable non committé entre deux lectures de V09 ; corrigé en v3).

Montage : un dépôt jouet avec un run décisif jouet (`20261020-180000-p4-decisif`, sans verdict complété de P3) et un
run jouet non décisif X (`20261020-170000-p4-jouet`), de même configuration. Chaque voie travaille sur une copie de ce
dépôt. « Écrit » est la différence des arbres (hors `.git`) avant et après la commande.

## Voies essayées

Ligne de commande = `lecture_p4_v1.py` lancé avec `-B` dans le dépôt jouet ; c'est la seule voie que le texte (plan
d'analyse, point 2) et la docstring nomment. Les appels Python directs sont délibérés.

| voie | résultat | refus avant toute écriture ? |
|---|---|---|
| V01 sans `--prereg`, run décisif | ARRÊT « lecture sans préenregistrement d'un run décisif ou réel : refusée sans rien écrire », code 1 | oui, rien écrit |
| V02 `--prereg ""` | ARRÊT « . : fichier absent sur disque » | oui |
| V02 `--prereg` texte du run, sans verdict | ARRÊT « verdict complété de P3 absent … reportée » | oui |
| V02 chemin absolu du texte ; texte copié hors du dépôt et scellé | même report | oui |
| V02 dossier ; `/dev/null` | ARRÊT « fichier absent sur disque » | oui |
| V02 configuration scellée (fichier scellé qui n'est pas un préenregistrement) | ARRÊT « scellé mais non conforme : section absente … » | oui |
| V02 copie non scellée du texte | ARRÊT « empreinte compagnon … absente » | oui |
| V02 autre texte scellé, table égale | report (verdict absent) | oui |
| V02 autre texte scellé, table autre (L6) | ARRÊT « table … ≠ `LIGNES` du module (cellules : L6 issue, L6 lecture) » | oui |
| V02 texte jouet scellé sans section des critères | ARRÊT « scellé mais non conforme : section absente : Critères de lecture gelés » | oui |
| V03 `--run-source` : `<run>/`, `./<run>`, `X/../<run>`, chemin absolu | ARRÊT, motif de CL3-01 | oui |
| V03 `--run-source x/../<run>` (dossier `runs/x` absent) | le système ne trouve pas le manifeste ; L1 « manifeste absent ou illisible » écrite | non, mais aucune donnée lue (CR-04) |
| V04 manifeste du run décisif altéré (8 formes : `decisif` retiré, à `false`, à `1`, clé renommée ; rescellé ou non ; manifeste de X recopié ; manifeste supprimé ; JSON tronqué) | L1 écrite (« manifeste absent ou illisible », ou « résumé … rattaché à un autre manifeste ») ; C1 non calculé | non, mais aucune donnée lue (VM2-contournement-08) |
| V04 `config` non dictionnaire, rescellé | `AttributeError`, trace Python, code 1 | oui, rien écrit (VM2-contournement-04) |
| **V05 copie, sous un run Y, du manifeste de X (scellé) et du résumé et de l'identité du run décisif (scellés)** | **code 0 ; source complète ; C1 calculé, aire 0,5556 ; scores lus = ceux du run décisif ; aucun verdict** | **non : lecture faite (VM2-contournement-01)** |
| **V05 même chose, `diag/Y` lien symbolique vers `diag/<run décisif>`** | **idem** | **non (01)** |
| **V05 manifeste de X recopié dans `diag/<run décisif>/`, `--run-source ../diag/<run décisif>`** | **idem, sans dossier neuf** | **non (01)** |
| V06 appels Python : `lire` sur une source construite sans clé `manifeste` ; lien fabriqué ; clés `manifeste` et `lien` retirées d'une source chargée | C1 calculé dans les trois cas ; `charger_source_p4` sans lien : refus | rien écrit (information, VM2-contournement-07) |
| **V07a texte = table du module + une rangée hors de la forme `\| Lk \|` (5 formes)** | **garde : « 22 cellules égales » dans les 5 cas ; test `P4_TEXTE_PREREG` aveugle à 3 des 5** | **(VM2-contournement-02)** |
| V07b section « Critères de lecture gelés » en double | la garde lit la dernière, le test la première ; validateur muet | (VM2-contournement-03) |
| **V07c lecture décisive, verdict versé, texte scellé à 12 rangées** | **manifeste de lecture décisif écrit ; lien « 22 cellules égales »** | **(02)** |
| V08 `--run-lecture` = run existant (source ou décisif) | ARRÊT « existe déjà : R12 » | oui |
| V08 `--run-lecture ../evil` | ARRÊT « format AAAAMMJJ-HHMMSS-nom attendu » | oui |
| V08 run décisif, dossier de lecture existant | ARRÊT, motif de CL3-01 (vient d'abord) | oui |
| V08 `diag/<lecture>/lecture-p4.json` déjà là, `runs/<lecture>` absent | ARRÊT « existe déjà : R12 interdit d'écraser » **après** l'écriture de `runs/<lecture>/manifeste.json` | non : manifeste orphelin (VM2-contournement-05) |

## Constats (le plus grave d'abord)

### VM2-contournement-01 — mineur — la règle de CL3-01 lit un manifeste ; les données en suivent un autre

- **Où** : `module-v2/lecture_p4_v1.py` l. 824-832 (`analyser`), l. 296-330 (`charger_source_p4` : règle l. 305,
  résumé l. 311, identité l. 319, tables l. 322) ; cause gelée : `src/controle_ia/manifeste.py` l. 142-150
  (`verifier_resultat` suit le `run_id` écrit dans le résultat, pas le dossier).
- **Preuve** (`travail/voies-v3.txt`, V05 ; test `test_v05_…`) :
  - le run décisif jouet, lu directement sans `--prereg` : refus, code 1 ;
  - run Y : `runs/Y/manifeste.json` et son sceau sont copiés de X (non décisif). `diag/Y/resume.json` et
    `identite-p4.json`, avec leurs sceaux, sont copiés du run décisif. Rien n'est rescellé, tout est committé ;
  - `lecture_p4_v1.py --run-source Y --run-lecture …`, sans `--prereg` : code 0. Source complète, C1 calculé, aire
    0,5556 (la valeur de la démonstration de CL3-01). `resume_source.scores_sha256` est celle du run décisif. Le résumé
    est rattaché au run décisif. Manifeste de lecture non décisif. Aucun verdict complété ;
  - même résultat avec un lien symbolique `diag/Y → diag/<run décisif>`, et sans dossier neuf :
    `--run-source ../diag/<run décisif>`, après avoir recopié le manifeste de X dans `diag/<run décisif>/`.
    `--run-source` n'est pas contrôlé comme un identifiant de run ;
  - en mode réel, il faudrait en plus un manifeste non décisif à la configuration réelle, donc un faux manifeste
    rescellé (`sceller`). Pour le jouet, des copies suffisent.
- **Gravité** : mineur. Voie délibérée : copier des fichiers scellés sous un autre nom. Aucune voie normale n'y mène,
  mais ce n'est pas un appel Python interne : la ligne de commande normale lit le run. La docstring de
  `charger_source_p4` (« chaque fichier est … rattaché au manifeste du run source ») est fausse dans ce cas. Même trou
  en mode décisif (information) : sous un manifeste décisif vérifié, les données d'un autre run peuvent être lues.
- **Correction proposée** :
  - dans `charger_source_p4`, garder le corps rendu par `verifier_resultat` pour `resume.json` et `identite-p4.json`.
    Exiger `corps["run_id"] == run_id` et `corps["manifeste_sha256"] == sha_m`. Sinon renvoyer
    `{**base, "etat": "L1", "motif": "récupération non conforme : <fichier> rattaché au run <id>, pas au run source"}`,
    avant toute lecture des tables ;
  - dans `analyser`, avant toute lecture : `--run-source` doit avoir la forme d'un identifiant de run
    (`^[0-9]{8}-[0-9]{6}-[a-z0-9][a-z0-9-]{0,62}$`), sinon `GardeArret`, rien n'est écrit ;
  - tests (R5) : artefacts V05 (copie, lien symbolique, `../diag/…`) → L1 ou refus, C1 non calculé ; cas sain : run
    jouet non décisif X lu, C1 calculé. Simulation hors du module (V09) : Y → L1 « resume.json rattaché au run
    20261020-180000-p4-decisif » ; `../diag/<run décisif>` → L1 ; X → complet, C1 calculé.

### VM2-contournement-02 — mineur — la garde de table ignore sans le dire une rangée hors de la forme `| Lk |`

- **Où** : `module-v2/lecture_p4_v1.py` l. 202-205 (`table_des_criteres` : `if not re.match(r"\|\s*L\d+\s*\|", …):
  continue`) ; même angle mort en partie dans `module-v2/test_lecture_p4_v1.py` l. 789-800 (`table_recodee`,
  `x.startswith("| L")`).
- **Preuve** (V07a, V07c) : table du module plus une douzième rangée. Garde : « 22 cellules égales » pour les cinq
  formes :
  - `L12 | … | … |` (rangée sans barre initiale, que le Markdown de GitHub affiche comme une rangée) ;
  - `| **L12** | … |` ; `| L6bis | … |` ; `| L 12 | … |` ; `| l12 | … |`.
  Le test `P4_TEXTE_PREREG` passe aussi pour la première, la deuxième et la cinquième. Validateur : aucun point. En
  V07c, verdict complété versé : la lecture décisive écrit un manifeste décisif et un lien « 22 cellules égales » sous
  un texte scellé à douze rangées.
- **Gravité** : mineur. Le candidat 1 n'a aucune rangée de ce genre : dans sa section, les seules lignes avec « | »
  sont l'en-tête, le séparateur et L1 à L11 (l. 637-649). Le risque naît à toute retouche de la table (candidat 2). R5 :
  aucun repli silencieux.
- **Correction proposée** : dans `table_des_criteres`, toute ligne non vide de la section qui contient une barre non
  échappée doit être l'en-tête exact `| ligne | issue | lecture |`, le séparateur, ou une rangée `^\|\s*L\d+\s*\|` à
  trois cellules ; sinon `GardeArret` (« rangée non reconnue … : lecture refusée sans rien écrire »). Même règle dans
  `table_recodee`. Tests : les cinq formes ci-dessus → refus ; candidat 1 → passe.

### VM2-contournement-03 — forme — section « Critères de lecture gelés » en double

- **Où** : `lecture_p4_v1.py` l. 199 (`sections(texte).get(...)` : la dernière section de ce titre gagne) ;
  `test_lecture_p4_v1.py` l. 790-791 (`texte.index(...)` : la première gagne).
- **Preuve** (V07b) : table autre puis table égale → garde : « 22 cellules égales » ; test : L6 différente. Ordre
  inverse → garde : refus. Le validateur ne voit rien. La suite lancée avec `P4_TEXTE_PREREG` sur le texte scellé
  rattrape les deux ordres ; la garde seule, non.
- **Correction proposée** : refuser si le titre `## Critères de lecture gelés` paraît plus d'une fois
  (`len(re.findall(r"^## +Critères de lecture gelés\s*$", texte, re.M)) != 1`).

### VM2-contournement-04 — forme — `config` non dictionnaire : trace Python au lieu d'« ARRÊT »

- **Où** : `lecture_p4_v1.py` l. 231-234 (`est_decisif_ou_reel`).
- **Preuve** (V04) : manifeste rescellé, `decisif` retiré, `config = ["x"]` → `AttributeError: 'list' object has no
  attribute 'get'`, code 1, rien écrit. Pas un contournement.
- **Correction proposée** : `config` présente et non dictionnaire → traitée comme suspecte (`True`), donc refus au
  motif de CL3-01.

### VM2-contournement-05 — forme — `diag/<lecture>/` déjà là : manifeste orphelin écrit avant le refus

- **Où** : `lecture_p4_v1.py` l. 847 (`creer_manifeste`) puis l. 859 (`ecrire_resultat`) ; comportement du v1, code
  gelé de `manifeste.py`.
- **Preuve** (V08) : `diag/<lecture>/lecture-p4.json` présent, `runs/<lecture>` absent. ARRÊT « existe déjà : R12 »,
  mais `runs/<lecture>/manifeste.json` et son sceau sont écrits d'abord. Rien n'est écrasé.
- **Correction proposée** : dans `analyser`, avant `creer_manifeste`, refuser si `diag/<run de lecture>` existe.

### VM2-contournement-06 — forme — commande documentée sans `-B`

- **Où** : `lecture_p4_v1.py` l. 5-7 (docstring) ; texte, plan d'analyse, point 2.
- **Constat** (non démontré, pour ne rien écrire dans l'environnement Python d'une autre session) : le module ne pose
  pas `sys.dont_write_bytecode`. Lancé comme écrit, Python écrit `docs/procedures/P4-instrument-v1/__pycache__/…` à
  l'import d'`instrument_p4_v1`, avant toute garde, même pour une lecture refusée. Or `verifier-arbre` vérifie chaque
  fichier sous `docs/`. Le test de la ligne de commande du module passe `-B`.
- **Correction proposée** : `sys.dont_write_bytecode = True` en tête de `lecture_p4_v1.py`, avant
  `import instrument_p4_v1` ; ou `-B` dans la commande de la docstring et du texte.

### VM2-contournement-07 — information — appels Python délibérés

- **Où** : `lecture_p4_v1.py` l. 763 (`lire` ne contrôle que `if "manifeste" in source`) ; l. 237-248.
- **Preuve** (V06) : C1 calculé par `lire` sur une source construite à la main sans clé `manifeste`, par un lien
  fabriqué (déjà dit par CR-03), et en retirant `manifeste` et `lien` d'une source chargée. Rien n'est écrit.
- **Durcissement facultatif** : dans `lire`, une source « complet » sans clé `manifeste` → refus.

### VM2-contournement-08 — information — manifeste du run décisif altéré : L1 écrite, rien du run lu

- **Preuve** (V04, V03 `x/../<run>`) : huit altérations, plus le chemin détourné. Chaque fois, aucun refus : L1 est écrite
  sous un manifeste de lecture non décisif, avec le motif. C1 n'est jamais calculé. CR-04 le disait pour un manifeste
  absent ou illisible ; c'est vrai aussi pour un manifeste rescellé, puisque le résumé reste rattaché à l'ancien. La
  lettre de la liste d'arrêt (« refusée sans rien écrire ») n'est pas tenue dans ces cas. Mais le caractère décisif ne
  se prouve plus par les fichiers, et le motif écrit nomme l'anomalie.

## Ce que la chaîne appelle

Je n'ai pas lu la chaîne. Le texte (plan d'analyse, point 2) et la docstring ne nomment que la ligne de commande, qui
passe par `analyser`. Toutes ses voies normales refusent avant d'écrire (V01 à V03, V08). Si la chaîne appelle
`charger_source_p4` ou `lire` directement (contrôle de la récupération, par exemple), elle sera refusée sur le run
réel sans le lien. À vérifier par la session, comme CR-01 et CR-02.

## Texte à ajouter au candidat 2 (si 01 et 02 sont corrigés)

1. Liste d'arrêt, après la ligne de la table proposée par le rapport de correction :
   « - Résumé ou identité du run source rattachés à un autre run (copie, lien symbolique, chemin détourné), ou
   `--run-source` qui n'a pas la forme d'un identifiant de run : récupération non conforme (ligne L1) ou refus ;
   aucune donnée du run n'est lue. »
2. Liste d'arrêt, compléter la ligne de la table proposée par le rapport de correction (phrase 2) :
   « … d'une cellule, d'une ligne ou de l'ordre, ou dont la section contient une rangée hors de la forme
   « | Lk | issue | lecture | », ou paraît deux fois : refusée sans rien écrire (pas une ligne) ; écart entre le texte
   et le module : nœud. »
3. « Tests (R5) », ajouter : « résumé et identité d'un run décisif sous le manifeste d'un run non décisif (copie, lien
   symbolique, `../diag/…`) : L1, C1 non calculé, contre le run jouet non décisif lu ; rangée de table hors de la
   forme `| Lk |`, et section des critères en double : refus sans rien écrire. »
4. Plan d'analyse, point 2 : `python -B docs/procedures/P4-instrument-v1/lecture_p4_v1.py --run-source …` (si
   VM2-contournement-06 est traité par la commande).
5. Après correction : nouvelles empreintes des fichiers changés dans les lignes « Module de P4 » et « Tests attendus »
   remis à jour.

## Pièces écrites

Sous `…/p4-instrument/verification-module-v2-contournement/`, chaque pièce avec son compagnon `.sha256` :

| pièce | sha256 |
|---|---|
| `travail/test_contournement_vm2_v3.py` (voies retenues, 44 tests) | `9c1b32cafb3b4c47c07bfacf80a308a11c7ef1b83edfb47192551799d52c1702` |
| `travail/voies-v3.txt` (une ligne par voie) | `cda3067181d1be3a807266502f8500ad39c7b01fa03dd7cb3324fac3f9780acf` |
| `travail/sortie-pytest-v3.txt` (44 passed) | `7d70ea8943039c2adcf300c3d296629ec72363f87562bd2abf4727b283a63948` |
| `travail/sortie-suite-module-v2.txt` (215 passed) | `388d7e51045ef374c7739cbccaa1a575b3fb2a3674182987c74e18dbbb27b72c` |
| `travail/test_contournement_vm2_v1.py`, `…_v2.py` (versions de travail) | `9a74d079cc87414d9d168a4f70f1f7ccbf89a918165129b35f918ed8123c0b41`, `5d33f0ba3e6e2a5976dfe2d996b836c75f45590f19a70e734790aa3515ed412d` |
| `travail/voies-v1.txt`, `voies-v2.txt` | `065f43ad2d041da3a2dd24826311b624f1c235adfbe1164ba2f93843555f4e21`, `f526a80e8fb18e9b7cdcc2f31b708248981408aef7130747cf13880b9fe1fc6f` |
| `travail/sortie-pytest-v1.txt`, `sortie-pytest-v2.txt` | `af519833e3b6f1c15c4bf7ab3c13d6922698ee36dedb9f0d48a205be2e93e612`, `d9fc1fa087ad15db9d34daa2c4a19b78bb5d0c2c6c76f3e875649bb824b65e87` |
| `travail/git-status-avant.txt`, `git-status-apres.txt` (vides) | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |

Dossiers jetables des tests : `travail/tmp-1`, `tmp-2`, `tmp-3`, `tmp-suite-module-v2`, `tmp-textes`.

Commande des voies (depuis `travail/`) :

```
VOIES_SORTIE=<travail>/voies-v3.txt TMP_VM2=<travail>/tmp-textes PYTHONPATH=/home/user/controle-ia-travail/src:…/p4-instrument/module-v2 PYTHONDONTWRITEBYTECODE=1 <python> -B -m pytest -q -s -p no:cacheprovider --import-mode=append --basetemp=<travail>/tmp-3 <travail>/test_contournement_vm2_v3.py
```
