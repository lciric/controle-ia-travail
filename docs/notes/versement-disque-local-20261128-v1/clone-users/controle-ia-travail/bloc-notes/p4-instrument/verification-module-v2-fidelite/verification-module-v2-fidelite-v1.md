# Vérification du module v2 de P4-instrument — lentille « fidélité et non-régression » — v1

Vérificateur : sous-agent neuf, lancé le 2026-10-20 (vers 19:30 à 20:15 UTC). Je n'ai écrit ni le module v1, ni le
module v2, ni le texte, ni la contre-lecture 3. Le préfixe `…/` vaut
`/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p4-instrument`.

## Verdict

**Conforme après corrections.** Le module v2 ne change que ce qui était demandé (CL3-01, CL3-03, comptes, docstrings).
Sa table `LIGNES` égale celle du candidat 1, 22 cellules sur 22. Les 194 anciens tests sont tous là, inchangés, et
passent avec les 21 neufs : 215 passés. Les empreintes égalent les compagnons.

Deux mineurs touchent le module ou les phrases : la garde de la table laisse passer certaines rangées en plus
(VM2-fidelite-01) ; la phrase « Tests attendus » n'a pas la forme lue par la chaîne (VM2-fidelite-02). Un mineur et deux
de forme : phrases à compléter (VM2-fidelite-03 à 05).

## Pièces relues

| pièce | sha256 |
|---|---|
| `…/P4-instrument-v1-candidat1.md` (texte qui fait foi) | `6422fb45a1dc2a3b42a5f6adad4ed8ff02cf89b3c09d91474213c5c1f5fe3bc0` (égale à la citation et au compagnon) |
| `…/contre-lecture-3/contre-lecture-3-P4-instrument-candidat1-v1.md` | `7f947de00aa58b0635fe2b6f0ad3c22eb7dbcb48ed0c8079f65a57abb13b5368` (égale) |
| `…/contre-lecture-3/travail/module/test_demo_cl3_lecture_non_decisive.py` | `0e1dcdcc30256eee3aa5e7f33d59d3c4d4125a4f5ccd16914c6ac2a1129f1ac6` |
| `…/contre-lecture-3/travail/sortie-demo-cl3-01.txt` | `792659c00bd25a6b82e3f004d8fa3b7139a551231f2e494b026fa96428498955` |
| `…/module/` (sept fichiers) | `6e0e026e…`, `51a25e30…`, `483b8ac3…`, `9d015be4…`, `49441971…`, `f4f97029…`, `NOTES-MODULE.md` `7a82f3b7…` : égales à la tâche ; sept sceaux vérifiés |
| `…/module-v2/` (neuf fichiers) | sceaux vérifiés, voir (6) |
| `…/module-v2/RAPPORT-CORRECTION-v1.md` | `1272a2bbda7d8a4da5830a9a4e7fbef14cc2f78c3e0e21971c1373afe74fde22` (égale au compagnon) |
| `…/module-v2/NOTES-MODULE-v2.md` | `ad731c278344f89bdc5af96f998d33f5a958d1c879ab80336b7f0849b32081ab` (égale) |

Lus en plus, pour le seul point (5), parce que la chaîne lit la ligne « Tests attendus » : `…/traitement-CL3-et-relectures-chaine-P4-v1.md`
(`4678a01b07bd8885169b8a77ac12381ab21763632bed48758da94a00f001b5d8`, ligne RC-fidelite-01),
`…/ecrire_candidat2_v1.py` (l. 100-140), et quatre lignes de la chaîne trouvées par `grep` dans `…/chaine/` (scripts
seulement). Lu dans le dépôt : `src/controle_ia/prereg.py` (fonction `sections`), nommé, sans recherche récursive.

Non lus : `prereg/P3-consignes-v1.md`, tout `textes-actions-*`, rien sous `donnees/`.

## Cadre tenu

- Dépôt en lecture seule. `git status --porcelain` vide avant et après (lu avec `GIT_OPTIONAL_LOCKS=0`, sans écriture
  de l'index). Commit `37852d6` avant et après. `src/controle_ia/__pycache__` : même relevé avant et après.
- Python `…/5a6b9d1d-…/venv-gpu-neuf/bin/python`, `-B`, `PYTHONDONTWRITEBYTECODE=1`, `-p no:cacheprovider`, `PYTHONPATH=src`.
- Les tests ont tourné sur des **copies octet pour octet** (empreintes vérifiées avant et après), sous
  `…/verification-module-v2-fidelite/travail/` : `module/` et `module-v2/` n'ont pas été touchés ; aucun `__pycache__`
  nulle part.
- Aucune commande Vast.ai, aucun réseau, aucune clé. Aucune moyenne ni médiane sur les jetons.

## (1) Différentiel complet `module/` → `module-v2/`

Deux lectures : `diff -u` (fichiers `diff-*.txt`) et un différentiel par l'arbre syntaxique, sans rien exécuter
(`travail/differentiel_ast_v1.py`, sortie `sortie-differentiel-ast-v1.json`).

| fichier | changement constaté | demandé ? |
|---|---|---|
| `mesures_conception_p4_v1.py` | aucun | — |
| `test_instrument_p4_v1.py` | aucun | — |
| `NOTES-MODULE.md` | aucun (copie) | — |
| `instrument_p4_v1.py` | docstring seule, lignes 3 et 4 ; aucun nœud de code changé | oui (CL3-03, docstring) |
| `lecture_p4_v1.py` | docstring ; import de `sections` ; `MOTIF_SANS_PREREG`, `TITRE_CRITERES` ; `LIGNES` (L1 issue, L4 issue et lecture, rien d'autre) ; six fonctions neuves (`table_des_criteres`, `exiger_table_des_criteres`, `est_decisif_ou_reel`, `gardes_decisives_passees`, `exiger_lecture_permise`, `_manifeste_brut`) ; trois fonctions changées (`charger_source_p4`, `lire`, `analyser`) | oui : CL3-01 et CL3-03 (garde de lecture contre le texte : décision de la session, traitement, ligne CL3-03) |
| `test_lecture_p4_v1.py` | docstring ; compte 42 → 43 ; un test neuf et son lecteur recodé | oui |
| `test_gardes_p4_v1.py` | docstring ; compte 81 → 101 ; imports (`hashlib`, `depot_p4`, `config_canonique`, `graines`) ; aide `texte_prereg` (table de `LIGNES` dans la section) ; neuf fonctions de test neuves (20 tests) | oui (l'aide est nécessaire : voir (4)) |

Aucune autre fonction de `lecture_p4_v1.py` n'a changé ; l'ordre des nœuds communs est gardé. La voie décisive réelle
reste la même, plus la garde de table : `exiger_lecture_sous_prereg_p4` (l. 167-191) met `run_source_verifie` à vrai
après toutes ses gardes ; `analyser` ajoute `verdict_p3` et `table_des_criteres` (l. 843-844) ; le lien passe donc
`gardes_decisives_passees` (l. 237-241). Un manifeste absent ou illisible donne L1 comme au v1. Sortie : le lien écrit
porte une clé de plus (`table_des_criteres`), rien d'autre.

## (2) `LIGNES` du v2 contre la table du candidat 1, cellule par cellule

Script indépendant, sans import du module (`LIGNES` lue par `ast.literal_eval`) et sans `prereg.sections`
(`travail/comparer_table_independant_v1.py`, sortie `sortie-comparaison-table-v1.json`) :

- texte : section l. 632, en-tête `ligne | issue | lecture`, 11 rangées de trois cellules, L1 à L11 dans l'ordre ;
  aucune ligne à barre hors des rangées ; aucune espace insécable (seuls non-ASCII : lettres accentuées, guillemets,
  Δ, −, ≤) ;
- module v2 : même ordre, **22 cellules égales, aucune différente** ;
- module v1 (contrôle) : 19 égales, 3 différentes, exactement L1 issue, L4 issue, L4 lecture (CL3-03).

## (3) Garde « table du texte » (`exiger_table_des_criteres`)

- Elle lit la table du texte passé par `--prereg` : `analyser` relit `racine / prereg` (l. 836), juste après
  `exiger_prereg_scelle` et avant le verdict complété et tout manifeste. Le test neuf du correcteur
  (`test_analyser_decisif_table_des_criteres_autre_refus_sans_rien_ecrire`) le montre au niveau d'`analyser`.
- Épreuve indépendante, 49 cas (`travail/eprouver_garde_table_v1.py`, sortie `sortie-epreuve-garde-table-v1.json`) :
  - sain : candidat 1 tel quel, passe (`cellules_egales` 22) ; espaces de fin de ligne, passe ;
  - **refusés, comme il faut** : chacune des 22 cellules changée d'un signe (motif nommant la cellule) ; chacune des
    11 lignes retirée ; « | L12 | » en plus ; L3 et L4 échangées ; double espace ; espace insécable ; barre échappée
    rendue nue ; signe moins devenu tiret ; brouillon 4 (L1 issue, L4 issue, L4 lecture) ; section en double dont la
    seconde est changée ;
  - **passent à tort (6)** : rangée en plus « | L4bis | », « | L3b | » entre L3 et L4, « | **L12** | », « | M1 | »,
    « L12 | … | » sans barre initiale (rangée valide en Markdown), section « Critères de lecture gelés » en double dont
    la première est changée (`sections` garde la dernière). Voir VM2-fidelite-01.
- Rien de tel dans le candidat 1 : la garde y donne le bon résultat.

## (4) Tests

- Comptes par collecte (`travail/comptes-collectes-v1.txt`) : v1 71, 42, 81 (194) ; v2 71, 43, 101 (215). Chaque en-tête
  « Nombre de tests attendu » égale la collecte de son fichier.
- Identifiants : les 194 du v1 sont tous dans le v2 ; 21 neufs (`travail/ids-*.txt`). Par l'arbre syntaxique, aucune
  fonction de test du v1 n'est changée ; seule l'aide `texte_prereg` l'est.
- Suite v2 complète, trois fichiers ensemble, `P4_TEXTE_PREREG` = candidat 1 : **215 passed in 152.42s**, code 0
  (`travail/sortie-suite-v2.txt`, `2ef5df8a…`).
- Croisé (non-régression) : les trois fichiers de tests **du v1, inchangés**, contre le code du v2 : 191 passés,
  3 échecs (`travail/sortie-croise-anciens-tests-code-v2.txt`). Les trois échecs ont la même cause : le
  préenregistrement synthétique du v1 n'a pas de table, et la garde neuve refuse (« lignes [] ≠ lignes du module »).
  Aucun échec ne vient de CL3-01 ni d'un autre changement. Le v2 règle ce point par l'aide `texte_prereg`.
- Test de la table du texte, seul, selon `P4_TEXTE_PREREG` (`travail/sortie-test-table-variable-v1.txt`) : candidat 1,
  passe ; variable absente, échec au message clair ; brouillon 4, échec sur `[('L1', 'issue'), ('L4', 'issue'),
  ('L4', 'lecture')]` ; fichier absent, échec « (R11) ». Jamais un saut.
- Démonstration de CL3-01, fichier inchangé, rejouée contre une copie du v2 (`--import-mode=append`) : **1 failed**,
  comme attendu ; la lecture décisive attend (verdict absent), puis la lecture sans `--prereg` lève
  « lecture sans préenregistrement d'un run décisif ou réel : refusée sans rien écrire » depuis `v2/lecture_p4_v1.py`
  l. 248 ; aucun run ni diag de lecture dans le dépôt jetable (`travail/sortie-demo-cl3-01-contre-v2.txt`).

## (5) Phrases proposées pour le texte

Simulation : les phrases appliquées au candidat 1 par paires exactes, chacune trouvée une fois
(`travail/simuler_phrases_v1.py`, sortie `sortie-simulation-phrases-v1.json` ; texte simulé
`travail/simulation-candidat1-avec-phrases-NON-CANDIDAT-v1.md`, une simulation, pas un candidat). Résultat : 13 paires
trouvées une fois ; la table n'est pas touchée (garde : 22 cellules égales) ; validateur `prereg.problemes` : rien ;
les six lignes « Module de P4 » relues par `lignes_module`, toutes à l'empreinte des fichiers du v2 ; « Tests attendus »
lu comme la chaîne : `1123` ; test de la table avec ce texte : passé.

| phrase du correcteur | exacte ? | suffisante ? |
|---|---|---|
| 1. Liste d'arrêt, l. 708-709 | oui : ancre unique ; dit ce que fait le module | oui |
| 2. Liste d'arrêt, ligne neuve (table) | oui, au défaut de VM2-fidelite-01 près | oui |
| 3. « Tests (R5) » | oui ; l'ancre a un retour à la ligne (VM2-fidelite-05) | oui |
| 4. « Tests attendus » | nombre juste (908 + 215 = 1 123 ; 71, 43, 101) ; **forme non lue par la chaîne** | VM2-fidelite-02 |
| 5. Lignes « Module de P4 » | oui : six empreintes égales aux fichiers du v2 | oui |
| CR-07 (plan, point 2), dite facultative | ancre avec retour à la ligne | **nécessaire** (VM2-fidelite-03) |
| — | l. 721 « (faits, 194 tests) » non traitée | VM2-fidelite-04 |

## (6) Empreintes

`sha256sum -c` sur chaque compagnon : `module/` 7 sur 7, `module-v2/` 9 sur 9, `module-v2-travail/` 3 sur 3,
candidat 1 et contre-lecture 3 : tous « OK ». Forme « <64 signes>  <nom> » partout dans `module-v2/`. Empreintes du v2 :
`instrument_p4_v1.py` `c3e78bec…`, `lecture_p4_v1.py` `3e41ec10…`, `test_lecture_p4_v1.py` `7f1bceb1…`,
`test_gardes_p4_v1.py` `42af1efc…` ; inchangés : `mesures_conception_p4_v1.py` `483b8ac3…`,
`test_instrument_p4_v1.py` `9d015be4…`, `NOTES-MODULE.md` `7a82f3b7…`. Les empreintes citées par le rapport du
correcteur pour ses sorties (`f5e8deec…`, `9fad94a7…`, `8d5cedca…`) sont justes.

## Constats (le plus grave d'abord)

### VM2-fidelite-01 — mineur — la garde de table ignore, sans le dire, certaines rangées en plus

- **Où** : `…/module-v2/lecture_p4_v1.py` l. 195-213 (`table_des_criteres`, filtre l. 204 :
  `re.match(r"\|\s*L\d+\s*\|", …)`) ; `src/controle_ia/prereg.py` l. 32-34 (`sections` garde la dernière section d'un
  titre répété).
- **Preuve** : `sortie-epreuve-garde-table-v1.json`, 43 cas conformes sur 49. Passent à tort : « | L4bis | … »,
  « | L3b | … » entre L3 et L4, « | **L12** | … », « | M1 | … », « L12 | … | » (sans barre initiale), et une
  première section « Critères de lecture gelés » changée suivie de la vraie. Une rangée de critère que le module ne
  connaît pas passerait donc la garde, sans motif (R5 : aucun repli silencieux). Sans effet sur le candidat 1.
- **Correction** (recommandée) : dans `table_des_criteres`, refuser toute ligne de la section qui porte une barre non
  échappée et qui n'est ni l'en-tête `| ligne | issue | lecture |`, ni le séparateur, ni une rangée « | Lk | » ;
  refuser si `len(re.findall(r"^## +Critères de lecture gelés\s*$", texte, re.M)) != 1`. Ajouter ces six artefacts à
  `test_table_des_criteres_artefacts_refuses` (101 → 107 ; total 221 ; « Tests attendus » `1129`), nouvelles
  empreintes, nouvelle vérification. À défaut : écrire la limite dans la phrase 2 (« la garde ne lit que les rangées
  « | Lk | » de la seule section de ce titre ») — moins bon.

### VM2-fidelite-02 — mineur — « Tests attendus » : forme non lue par la chaîne, paire qui ne s'appliquerait pas

- **Où** : `…/module-v2/RAPPORT-CORRECTION-v1.md`, « Texte à ajouter », point 4 ; `NOTES-MODULE-v2.md`, « À reporter ».
- **Preuve** : la session a accepté la forme « Tests attendus : `N` » (traitement, ligne RC-fidelite-01 ; NOTES-CHAINE
  T2). La chaîne la lit ainsi : `…/chaine/p4_instance_v1.sh` l. 85-86 et `…/chaine/controle_cinq_minutes_p4_v1.sh`
  l. 51-53 (motif « Tests attendus : \`[0-9]+\` », une seule fois). La phrase 4 écrit « Tests attendus : 1 123, soit » :
  ni accents graves, ni chiffres collés ; la chaîne ne trouverait pas le nombre. De plus, `…/ecrire_candidat2_v1.py`
  l. 116 remplace d'abord « - Tests attendus : 1 102, soit » ; une paire qui part de la ligne entière du candidat 1 ne
  se trouverait plus.
- **Correction** : lancer `ecrire_candidat2_v1.py` avec `TESTS_ATTENDUS=1123` (ou `1129` si VM2-fidelite-01 est
  corrigé), et ne donner en paire que le reste de la ligne (texte exact ci-dessous, trouvé une fois). Montré par la
  simulation : « Tests attendus » lu `1123`.

### VM2-fidelite-03 — mineur — plan d'analyse, point 2 : la garde de table et la lecture sans `--prereg` n'y sont pas

- **Où** : candidat 1, l. 473-482 ; rapport du correcteur, CR-07 (« suggestion facultative »).
- **Preuve** : le point 2 énumère les gardes du mode décisif (entropie, module, run source, configuration, verdict
  complété), sans la garde de table, et dit qu'une lecture refusée par « une autre garde du mode décisif » écrit L1. La
  garde de table refuse **sans rien écrire**. Rien n'y dit que la lecture sans `--prereg` d'un run décisif ou réel est
  refusée. Le module ferait plus que le plan : le défaut même que CL3-01 relevait. Un verdict R13 qui suit le plan
  pourrait attendre une L1.
- **Correction** : rendre CR-07 obligatoire et ajouter une phrase sur la lecture sans `--prereg` (deux paires exactes
  ci-dessous).

### VM2-fidelite-04 — forme — « Chaîne de lancement » garde « 194 tests »

- **Où** : candidat 1, l. 721 : « module et tests alignés (faits, 194 tests) ». Aucune phrase du correcteur ne la touche.
- **Preuve** : le texte dirait 194 ici et 215 dans « Tests attendus ».
- **Correction** : « (faits, 194 tests) » → « (faits, 194 tests ; module v2 après la contre-lecture 3 : 215 tests) ».

### VM2-fidelite-05 — forme — deux ancres citées sans leurs retours à la ligne

- **Où** : rapport du correcteur, point 3 (« C1 au pas 0 et Δ net recalculés à la main sur un jeu synthétique » : l.
  593-594) et CR-07 (« module à l'empreinte citée (`exiger_module_cite`) ; » : l. 475-476).
- **Preuve** : le script du candidat 2 applique des paires exactes, chacune trouvée une seule fois (`une`). Sans le
  retour à la ligne, l'ancre de CR-07 est trouvée 0 fois (compté).
- **Correction** : utiliser les ancres exactes ci-dessous (chacune comptée une fois).

## Texte à ajouter au candidat (paires exactes ; « \n » = retour à la ligne du texte)

1. Liste d'arrêt (phrases 1 et 2 du correcteur, inchangées) : ancien
   « - Lecture demandée avant le scellement du verdict complété de P3 (addendum 2), ou avant le scellement de ce texte :\n  refusée sans rien écrire et reportée (pas une ligne). »
   → nouveau « - Lecture demandée avant le scellement du verdict complété de P3 (addendum 2), ou avant le scellement de ce texte,\n  ou sans `--prereg` sur un run source décisif ou en mode réel : refusée sans rien écrire et reportée (pas une ligne).\n- Lecture décisive dont la table « Critères de lecture gelés » de ce texte diffère de la table du module (`LIGNES`\n  de `lecture_p4_v1.py`) d'une cellule, d'une ligne ou de l'ordre : refusée sans rien écrire (pas une ligne) ; écart\n  entre le texte et le module : nœud. »
2. « Tests (R5) » (phrase 3 du correcteur) : ancien « C1 au pas 0 et Δ net\n  recalculés à la main sur un jeu synthétique. »
   → nouveau « C1 au pas 0 et Δ net\n  recalculés à la main sur un jeu synthétique ; lecture sans `--prereg` d'un run décisif ou en mode réel (doit refuser\n  sans rien écrire), contre un run jouet non décisif (doit lire) ; table « Critères de lecture gelés » de ce texte\n  différente d'une cellule de la table du module (doit refuser sans rien écrire), et table du module égale à celle de\n  ce texte, cellule par cellule (test lancé avec `P4_TEXTE_PREREG`, qui échoue sans elle). »
3. « Tests attendus » (VM2-fidelite-02) : `TESTS_ATTENDUS=1123` pour la paire T2 (« - Tests attendus : `1123`, soit ») ;
   puis ancien « les 194 du module de P4 (71, 42 et 81 ; chaque fichier\n  écrit son nombre et le vérifie). »
   → nouveau « les 215 du module de P4 (71, 43 et 101 ; chaque fichier\n  écrit son nombre et le vérifie ; la suite du module se lance avec `P4_TEXTE_PREREG=prereg/P4-instrument-v1.md`, sans\n  quoi le test qui compare la table du module à celle de ce texte échoue). »
4. Plan d'analyse, point 2 (VM2-fidelite-03) :
   - ancien « module à l'empreinte\n   citée (`exiger_module_cite`) ; » → nouveau « module à l'empreinte\n   citée (`exiger_module_cite`) ; table « Critères de lecture gelés » de ce texte égale à celle du module, cellule par\n   cellule (sinon refus, rien n'est écrit, pas une ligne) ; » ;
   - ancien « sans autre table\n   (VP3-06). » → nouveau « sans autre table\n   (VP3-06). Sans `--prereg`, seul un run source ni décisif ni en mode réel se lit (répétition jouet) ; un run\n   source décisif ou en mode réel est refusé sans rien écrire (liste d'arrêt). »
5. Chaîne de lancement (VM2-fidelite-04) : ancien « (faits, 194 tests) » → nouveau « (faits, 194 tests ; module v2 après
   la contre-lecture 3 : 215 tests) ».
6. Lignes « Module de P4 » : les six empreintes du dossier `module-v2/` (point 5 du correcteur, justes) ; le script du
   candidat 2 les calcule lui-même depuis `MODULE_DIR`.

Si VM2-fidelite-01 est corrigé : 107 au lieu de 101, 221 au lieu de 215, `1129` au lieu de `1123`, et les empreintes
du nouveau module.

## Hors de ma lentille (information, sans constat)

- La chaîne lance la suite du module sans `P4_TEXTE_PREREG` (`controles_avant_depense_p4_v1.sh` l. 313,
  `p4_instance_v1.sh` l. 213) : avec le v2, un test y échouerait. Cela confirme la réserve CR-01 du correcteur ; la
  chaîne v2 doit exporter la variable.
- La répétition jouet lit `runs/*-p4-jouet` sans `--prereg` (`repetition_jouet_p4_v1.sh` l. 329-333). Si ce run est
  décisif, le v2 le refuse (réserve CR-02). Non vérifié ici.
- Le correcteur dit avoir lancé une fois un `find` par nom dans l'arbre du dépôt, `donnees/` compris (compte seul,
  aucun contenu). Écart de cadre déclaré ; à consigner par la session.

## Artefacts (sous `…/verification-module-v2-fidelite/`)

| fichier | sha256 |
|---|---|
| `diff-instrument_p4_v1.py.txt` | `ab44c44853b1b3ceb7671336a7a7623925f6c84b34789b1f2fa01f28e5f1efb5` |
| `diff-lecture_p4_v1.py.txt` | `8a16a922c0715a6d6fdacab9e4f94855bafb0ca66357e14ef9753cd4252305f2` |
| `diff-test_lecture_p4_v1.py.txt` | `044c2d8f1509d03f965ccbc69fa0a86d41bfce45a8e82177fbe323b44f4bfe01` |
| `diff-test_gardes_p4_v1.py.txt` | `81592903a1abe10840cac329f39694c036a00dcb9139ea1768ce3d4aa57f5c33` |
| `diff-mesures…`, `diff-test_instrument…`, `diff-NOTES-MODULE.md.txt` (vides) | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `sortie-differentiel-ast-v1.json` | `a489ecbe91fc350d2ee71b886affeba77ef64e195394b9d45a458cb68cfd3c2b` |
| `sortie-comparaison-table-v1.json` | `a894652f015ee344391664ff13d39e154dd5631b06c185aa8b0678be88f52e3c` |
| `sortie-epreuve-garde-table-v1.json` | `963f58601808ffceb218afb3e42ff2c73505d4058e4e4dfd0dd078cf3bd6018f` |
| `sortie-simulation-phrases-v1.json` | `44f5f679e8b816eec231b84d0553449211b4f79463b2c7136770aa6bbf2b71d5` |
| `travail/sortie-suite-v2.txt` (215 passés) | `2ef5df8afe4f5cff5d3a34efbb27d231431d59b70ad106042546c4d801d8f579` |
| `travail/sortie-croise-anciens-tests-code-v2.txt` (191 passés, 3 échecs expliqués) | `921b98a6eedb7fd608bd5822bb716174cb66d78eb48c2dca06f5e4adf5f23443` |
| `travail/sortie-demo-cl3-01-contre-v2.txt` (1 failed, attendu) | `dad825ad89b8619010ce0e5463508806932505daf3a6f1ac75cb77ea867325a0` |
| `travail/sortie-test-table-variable-v1.txt` (quatre cas) | `6a6a24a5a738f5c74e2fff4f3b426916fe79b42b20967110e875557639297412` |
| `travail/sortie-test-table-variable-simulation-v1.txt` | `a5a2fa614ca168a9127701b7aacca63972e4f23c6f60d92709c1372f49a6bc5a` |
| `travail/comptes-collectes-v1.txt` | `ea9e646ad2629bb34ca276212f799912c3108faad72eb07a358f674a55177aa8` |
| `travail/ids-anciens.txt`, `ids-v2.txt`, `ids-neufs.txt` | `63a4358c…`, `52182541…`, `47e147eb…` |
| `travail/simulation-candidat1-avec-phrases-NON-CANDIDAT-v1.md` (simulation) | `91d53338c350bbfefd4daf47f12ceff51568020f3629f38f2b66e7fc9edb1cb6` |
| scripts : `comparer_table_independant_v1.py`, `eprouver_garde_table_v1.py`, `differentiel_ast_v1.py`, `simuler_phrases_v1.py` | `5a86e3fc…`, `2653b9a9…`, `227ee1b8…`, `6397e271…` |

Copies de travail (`travail/v2/`, `travail/croise/`, `travail/demo/`) : empreintes dans `travail/empreintes-copies-v1.txt`,
vérifiées après les tests (13 sur 13).
