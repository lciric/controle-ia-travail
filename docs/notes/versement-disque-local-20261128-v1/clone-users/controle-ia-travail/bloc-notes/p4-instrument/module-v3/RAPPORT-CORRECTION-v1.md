# Rapport de correction du module de P4-instrument : vérifications du module v2 (module v3) — v1

Rédacteur : sous-agent correcteur neuf, lancé par la session le 2026-10-20 (vers 19:50 à 20:45 UTC). Je n'ai écrit ni le
préenregistrement, ni le module v1, ni le module v2, ni aucune vérification. Le préfixe `…/` vaut
`/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p4-instrument`.

## Verdict

**Corrigé.** Les huit décisions acceptées (VM2-contournement-01 à -08, VM2-fidelite-01) sont appliquées dans
`…/module-v3/`, chacune avec cas sain et artefact. La suite des trois fichiers passe : **258 passed** (71, 49 et 138),
code 0, avec `P4_TEXTE_PREREG` = candidat 1. `…/module/` et `…/module-v2/` sont intacts. Dépôt de travail non modifié.

À reporter dans le texte (candidat 2) : sept paires exactes (fin de ce rapport), « Tests attendus : `1166` », six lignes
« Module de P4 ». Une conséquence à noter : une forme de VM2-contournement-08 passe de L1 à refus, par la règle de -01.

## Pièces relues

| pièce | sha256 |
|---|---|
| `…/P4-instrument-v1-candidat1.md` (texte qui fait foi) | `6422fb45a1dc2a3b42a5f6adad4ed8ff02cf89b3c09d91474213c5c1f5fe3bc0` (égale à la citation et au compagnon) |
| `…/module-v2/RAPPORT-CORRECTION-v1.md` | `1272a2bbda7d8a4da5830a9a4e7fbef14cc2f78c3e0e21971c1373afe74fde22` (égale au compagnon) |
| `…/module-v2/NOTES-MODULE-v2.md` | `ad731c278344f89bdc5af96f998d33f5a958d1c879ab80336b7f0849b32081ab` (égale) |
| `…/module-v2/` six fichiers de code | égaux à leurs compagnons (`c3e78bec…`, `3e41ec10…`, `483b8ac3…`, `9d015be4…`, `7f1bceb1…`, `42af1efc…`) |
| `…/verification-module-v2-contournement/verification-module-v2-contournement-v1.md` | `2ce3d0af0a36fbb076d494b59619f4f11ed03fb9172f05e3bdde3087500a335d` (égale) |
| `…/verification-module-v2-fidelite/verification-module-v2-fidelite-v1.md` | `ea12d4a2ea780e50e465105c29fb53fbe1e6eace5e3bae1ee177ed17426e7196` (égale) |
| `…/ecrire_candidat2_v1.py` (forme des paires, paire T2) | `9a59358ec3bafa7ba444d2881943ed5be51778e9098dbc7640261417cc7d4480` |
| `…/P4-instrument-v1-brouillon4.md` (artefact du test de la table, non lu à la main) | `32d821fb42e54341f2649637085de18e2b6b9758b51dc38c504f702ba393ead6` |
| `…/chaine-v2/repetition_jouet_p4_v1.sh`, `controles_avant_depense_p4_v1.sh`, `p4_instance_v1.sh` (lignes de la lecture et de la suite, par `grep`) | `dc570f9e…`, `c881d0c4…`, `8801864f…` |

Code gelé lu, en lecture seule : `src/controle_ia/manifeste.py`, `src/controle_ia/prereg.py`, `src/controle_ia/scellement.py`
(début). Non lus : `prereg/P3-consignes-v1.md`, tout fichier `textes-actions-*`, rien sous `donnees/`.

## Cadre tenu

- Dépôt `/home/user/controle-ia-travail` en lecture seule : `git status --porcelain` (sans verrou) vide avant et après ;
  `src/controle_ia/__pycache__` : même relevé, mêmes dates, avant et après. Aucune recherche récursive dans le dépôt. Le
  commit de tête est passé de `c52225b` à `a82dac7` pendant mon travail : commits de la session, pas les miens.
- Python de la tâche (`…/5a6b9d1d-…/venv-gpu-neuf/bin/python`), `-B`, `PYTHONDONTWRITEBYTECODE=1`, `-p no:cacheprovider` ;
  dossiers temporaires sous `…/module-v3-travail/` (`--basetemp`). Seuls les tests de -06 lancent un Python sans `-B` :
  code du dépôt copié hors du dépôt réel ; pour l'artefact, cache envoyé sous le dossier temporaire
  (`PYTHONPYCACHEPREFIX`). Relevé après coup : aucun fichier plus récent que mon début dans l'environnement Python ni dans
  `/usr/lib/python3.11`.
- Aucune commande Vast.ai, aucun réseau, aucune clé. Aucune moyenne ni médiane sur les jetons ajoutée.
- R12 : dossiers neufs `…/module-v3/` et `…/module-v3-travail/` ; mêmes noms de fichiers que `module-v2/` ;
  `NOTES-MODULE-v3.md` neuf ; versions de travail gardées sous des noms neufs (`…-essai1`, `…-essai2`, `…-v1`, `…-v2`).

## Changements (détail : `NOTES-MODULE-v3.md`)

| décision | où | ce qui change |
|---|---|---|
| VM2-contournement-01 | `lecture.charger_source_p4`, `exiger_rattache_au_run` | manifeste lu sous `runs/<run source>/` au `run_id` du dossier ; résumé et identité au même `run_id` ; sinon refus avant tout manifeste de lecture (`AUTRE_RUN`) |
| -02, -03, VM2-fidelite-01 | `lecture.table_des_criteres`, `_cellules_de` ; `test_lecture.table_recodee` | section unique ; en-tête et séparateur exacts ; chaque rangée jusqu'à la fin du tableau, quelle que soit sa forme, en `\| Lk \| issue \| lecture \|` ; aucune autre ligne à barre ; sinon refus |
| -04 | `lecture.est_decisif_ou_reel`, `exiger_lecture_sous_prereg_p4` | `config` non dictionnaire : suspecte, refus au motif de CL3-01 ; en mode décisif, « hors du mode réel » au lieu d'une trace |
| -05 | `lecture.analyser` | `diag/<run de lecture>` présent (même lien pendant) : refus R12 avant `creer_manifeste` |
| -06 | `lecture_p4_v1.py`, `instrument_p4_v1.py` | `sys.dont_write_bytecode = True` avant tout import du dépôt ; commandes des docstrings avec `-B` |
| -07 | `lecture.lire` | source « complet » sans manifeste dictionnaire : refus (`MOTIF_SANS_MANIFESTE`) |
| -08 | aucun | L1 gardée ; voir CR3-01 pour la seule forme qui change |

`mesures_conception_p4_v1.py` et `test_instrument_p4_v1.py` sont inchangés. `LIGNES`, `issue_p4` et les statistiques
sont inchangés.

## Tests (nombres exacts)

| fichier | v2 | v3 | sortie |
|---|---|---|---|
| `test_instrument_p4_v1.py` | 71 | 71 | 71 collectés, passés |
| `test_lecture_p4_v1.py` | 43 | 49 | 49 collectés, passés (avec `P4_TEXTE_PREREG` = candidat 1) |
| `test_gardes_p4_v1.py` | 101 | 138 | 138 collectés, passés |
| **total** | 215 | **258** | **258 passed in 233.29s**, code 0 |

- Suite des trois fichiers ensemble, sur les fichiers scellés : `…/module-v3-travail/sortie-tests-module-v3.txt`
  (empreintes des fichiers lancés en tête). Comptes par collecte : `…/module-v3-travail/comptes-collectes-v3.txt`.
  Chaque fichier vérifie son propre compte.
- Variable `P4_TEXTE_PREREG` (sept tests la lisent) : absente, 7 échecs ; brouillon 4, 7 échecs (L1 issue, L4 issue,
  L4 lecture) ; fichier absent, 7 échecs ; candidat 1, 7 passés. Jamais un saut.
  Sortie : `…/module-v3-travail/sortie-test-table-variable-v3.txt`.
- Essais intermédiaires gardés : 257 passés (avant la correction de CR3-01 et le test de -08), deux fois
  (`sortie-tests-module-v3-essai1.txt`, `-essai2.txt`).

Tests neufs, cas sain et artefact pour chaque décision : `NOTES-MODULE-v3.md`, section « Tests ».

## Constats et réserves

- **CR3-01, réserve (décision appliquée à la lettre).** -01 compare le `run_id` seulement, comme la décision. Le
  rattachement à l'empreinte du manifeste reste vérifié par `verifier_resultat` (sinon L1, -08 gardé). Une forme de -08
  change pourtant : le manifeste d'un autre run recopié sous `runs/<run décisif>/` porte un `run_id` autre que celui du
  dossier ; il est maintenant refusé sans rien écrire (le v2 écrivait L1). Même chose en mode décisif : un résumé ou une
  identité d'un autre run donne un refus (pas une ligne), pas L1 « récupération non conforme ». Les phrases du texte
  ci-dessous le disent.
- **CR3-02, limite (comme CR-03 du v2).** Un run fabriqué par les fonctions gelées (`creer_manifeste` d'un run neuf non
  décisif, puis `ecrire_resultat` du résumé et de l'identité d'un autre run sous ce manifeste) passe la règle : c'est
  une fraude délibérée, pas une omission. Durcissement possible, non fait (hors des décisions) : exiger que les tables
  citées par le résumé soient sous `donnees/<run source>/`. À trancher par la session.
- **CR3-03, information.** `--run-source` doit être l'identifiant exact du run. La chaîne v2 passe des identifiants
  exacts (`basename`) et cherche le motif de CL3-01, inchangé.
- **CR3-04, information (hors des décisions, lu dans le code, non éprouvé).** Un manifeste du run source scellé dont le
  JSON n'est pas un objet (une liste) fait lever une `TypeError` dans `lire_manifeste`, non attrapée par `analyser` :
  trace Python, rien d'écrit. Correction possible : ajouter `TypeError` aux exceptions attrapées. Non fait.
- **CR3-05, information.** `mesures_conception_p4_v1.py` (inchangé, hors des décisions) importe `instrument_p4_v1` sans
  poser la ligne : lancé sans `-B`, le cache de `instrument_p4_v1` s'écrirait sous le dossier du module avant que la
  ligne de l'instrument s'exécute. La chaîne v2 le lance avec `-B`.
- **CR3-06, information.** Le cas sain de -06 lance Python sans `-B` : les modules importés avant la ligne
  (`__future__`, modules des fichiers `.pth`) pourraient écrire leur cache dans l'environnement Python s'il manquait.
  Ici, rien n'a été écrit (relevé). Sans effet sur le dépôt.
- **CR3-07, information.** Durée de la suite : 233 s ici (v2 : 135 s). Environ 100 s de plus, dont 20 à 25 s pour
  l'artefact de -06 (compilation sous le préfixe) et le run décisif jouet partagé. Sur l'instance, environ deux minutes
  de plus avant le run.
- **CR3-08, information.** Les constantes `COMMANDE` (écrites dans les manifestes) restent sans `-B` ; seules les
  docstrings et le texte portent `-B`.
- **CR3-09, texte.** Les sept paires ci-dessous remplacent celles du rapport du v2 et de la vérification de fidélité
  pour les mêmes ancres. Appliquer les deux échouerait (ancre trouvée 0 fois) : l'écrivain du candidat 2 s'arrête. Utiliser
  `…/module-v3-travail/paires-texte-module-v3-v3.json` et `TESTS_ATTENDUS=1166`.

## Simulation des phrases (pas un candidat)

`…/module-v3-travail/simuler_texte_module_v3_v1.py` applique les paires au candidat 1 : (a) seules ; (b) après les paires
fixes de `ecrire_candidat2_v1.py`, les lignes « Module de P4 » du module v3 et la paire T2 avec `1166` (T3 non jouée :
elle exige les scripts de l'instance et ne touche aucune ancre d'ici). Résultat
(`…/module-v3-travail/sortie-simulation-texte-module-v3-v3.json`) : chaque paire trouvée une fois, dans (a) et dans (b) ;
table : 22 cellules égales ; `prereg.problemes` : rien ; lignes « Module de P4 » égales aux empreintes du module v3 ;
« Tests attendus : `N` » lu une fois, `1166`. Les sept tests de la variable passent sur le texte simulé
(`…/module-v3-travail/simulation/simulation-candidat1-avec-paires-module-v3-NON-CANDIDAT-v3.md`).

## Texte à ajouter au candidat (paires exactes ; « \n » = retour à la ligne du texte)

Chaque ancre est recopiée du candidat 1, caractère pour caractère, et trouvée une seule fois.

1. Liste d'arrêt (CL3-01 ; VM2-contournement-01 à -05 ; VM2-fidelite-01). Ancien :
   « - Lecture demandée avant le scellement du verdict complété de P3 (addendum 2), ou avant le scellement de ce texte :\n  refusée sans rien écrire et reportée (pas une ligne). »
   Nouveau :
   « - Lecture demandée avant le scellement du verdict complété de P3 (addendum 2), ou avant le scellement de ce texte,\n  ou sans `--prereg` sur un run source décisif ou en mode réel (configuration du manifeste qui n'est pas un\n  dictionnaire comprise) : refusée sans rien écrire et reportée (pas une ligne).\n- Lecture décisive dont la table « Critères de lecture gelés » de ce texte diffère de la table du module (`LIGNES`\n  de `lecture_p4_v1.py`) d'une cellule, d'une rangée ou de l'ordre ; section « Critères de lecture gelés » présente\n  plus d'une fois ; rangée, entre l'en-tête et la fin du tableau, hors de la forme `| Lk | issue | lecture |` :\n  refusée sans rien écrire (pas une ligne) ; écart entre le texte et le module : nœud.\n- Manifeste lu sous `runs/<run source>/`, résumé ou identité du run source dont l'identifiant de run n'est pas\n  celui du dossier (copie, lien symbolique, chemin détourné) : lecture refusée sans rien écrire (pas une ligne).\n- Dossier `diag/<run de lecture>` déjà présent : lecture refusée sans rien écrire (R12). »
2. « Tests (R5) ». Ancien : « C1 au pas 0 et Δ net\n  recalculés à la main sur un jeu synthétique. »
   Nouveau :
   « C1 au pas 0 et Δ net\n  recalculés à la main sur un jeu synthétique ; lecture sans `--prereg` d'un run décisif ou en mode réel, ou d'un run\n  dont la configuration du manifeste n'est pas un dictionnaire (doit refuser sans rien écrire), contre un run jouet non\n  décisif (doit lire) ; table « Critères de lecture gelés » de ce texte différente d'une cellule de la table du module,\n  rangée hors de la forme `| Lk |` (sans barre initiale, en gras, « L6bis »), ligne collée sous la table, seconde\n  table, section en double (doit refuser sans rien écrire), contre la table du module égale à celle de ce texte,\n  cellule par cellule (tests lancés avec `P4_TEXTE_PREREG`, qui échouent sans elle) ; résumé ou identité d'un autre\n  run sous le manifeste du run source, par copie, lien symbolique ou chemin détourné (doit refuser sans rien écrire),\n  contre le run jouet lu sous son nom (doit lire) ; `diag/<run de lecture>` déjà présent (doit refuser avant tout\n  manifeste) ; lecture et contrôle du module lancés sans `-B` (aucun cache de code écrit), contre la ligne\n  `sys.dont_write_bytecode = True` retirée (le cache s'écrit). »
3. Plan d'analyse, point 2, commande (VM2-contournement-06). Ancien :
   « `lecture_p4_v1 --run-source <run> --run-lecture <run de lecture> --prereg\n   prereg/P4-instrument-v1.md --entropie <entropie citée>` »
   Nouveau :
   « `PYTHONPATH=src python -B docs/procedures/P4-instrument-v1/lecture_p4_v1.py --run-source <run> --run-lecture\n   <run de lecture> --prereg prereg/P4-instrument-v1.md --entropie <entropie citée>` »
4. Plan d'analyse, point 2, garde de table (VM2-contournement-02 et -03 ; VM2-fidelite-01 et -03). Ancien :
   « module à l'empreinte\n   citée (`exiger_module_cite`) ; »
   Nouveau :
   « module à l'empreinte\n   citée (`exiger_module_cite`) ; table « Critères de lecture gelés » de ce texte égale à celle du module, lue en\n   entier : section présente une seule fois ; chaque rangée, entre l'en-tête et la fin du tableau, de la forme\n   « `| Lk | issue | lecture |` » ; mêmes rangées, même ordre, mêmes cellules (sinon refus, rien n'est écrit, pas une\n   ligne) ; »
5. Plan d'analyse, point 2, lecture sans `--prereg`, rattachement, R12 (CL3-01 ; VM2-contournement-01, -04, -05 ;
   VM2-fidelite-03). Ancien : « sans autre table\n   (VP3-06). »
   Nouveau :
   « sans autre table\n   (VP3-06). Sans `--prereg`, seul un run source ni décisif ni en mode réel se lit (répétition jouet) ; un run\n   source décisif ou en mode réel, ou dont la configuration du manifeste n'est pas un dictionnaire, est refusé sans\n   rien écrire (liste d'arrêt). Dans tous les modes, avant toute lecture des données du run source : le manifeste lu\n   sous `runs/<run source>/` porte l'identifiant de ce run ; le résumé et l'identité portent ce même identifiant ;\n   sinon la lecture est refusée sans rien écrire (leur rattachement à l'empreinte de ce manifeste reste vérifié :\n   sinon récupération non conforme, ligne L1). Dossier `diag/<run de lecture>` déjà présent : refus (R12), rien\n   n'est écrit. »
6. « Tests attendus » (VM2-fidelite-02). Paire T2 de l'écrivain avec `TESTS_ATTENDUS=1166` :
   « - Tests attendus : 1 102, soit » → « - Tests attendus : `1166`, soit ». Puis, ancien :
   « les 194 du module de P4 (71, 42 et 81 ; chaque fichier\n  écrit son nombre et le vérifie). »
   Nouveau :
   « les 258 du module de P4 (71, 49 et 138 ; chaque fichier\n  écrit son nombre et le vérifie ; la suite du module se lance avec `P4_TEXTE_PREREG=prereg/P4-instrument-v1.md`, sans\n  quoi les sept tests qui lisent la table de ce texte échouent). »
   Ligne obtenue : « - Tests attendus : `1166`, soit les 908 de la suite du dépôt au commit de P3 (`prereg/P3-premier-test-i-a-v1.md` l. 41 ; … ».
7. Facultatif (VM2-fidelite-04), Chaîne de lancement : « (faits, 194 tests) » → « (faits, 194 tests ; module v3, après
   la contre-lecture 3 et les vérifications du module v2 : 258 tests) ».
8. Lignes « Module de P4 » (l'écrivain les calcule depuis `MODULE_DIR=…/module-v3`) :
   - Module de P4 : `docs/procedures/P4-instrument-v1/mesures_conception_p4_v1.py` : `483b8ac3aca65a9879b7d2f2a832cfd5478c48fd860c94a6fbdc041364cc8be7`
   - Module de P4 : `docs/procedures/P4-instrument-v1/instrument_p4_v1.py` : `000281d02c17779937b0033c2e1c724f05548b3f3eaf1ee3cfa94da74afafb8c`
   - Module de P4 : `docs/procedures/P4-instrument-v1/lecture_p4_v1.py` : `0b7a259bc95e8a7fb6c994076d2be72ada47a1d10e9f5d28597afbb14674682a`
   - Module de P4 : `docs/procedures/P4-instrument-v1/test_instrument_p4_v1.py` : `9d015be4ce2bbff4a4541387d5d19ef70497aa41f1a53b9c38724360d7a1dffd`
   - Module de P4 : `docs/procedures/P4-instrument-v1/test_lecture_p4_v1.py` : `305a2e9faf90dd09a48992f76c2ae1a96c8a79d86244b71cd27109698b87f384`
   - Module de P4 : `docs/procedures/P4-instrument-v1/test_gardes_p4_v1.py` : `014a9f85a663602bfeafac809ced04df7ce23ff864a432888822acf9ca397147`

## Pièces écrites

Sous `…/module-v3/`, chaque fichier avec son compagnon `.sha256` (« <empreinte>  <nom> ») :

| fichier | sha256 |
|---|---|
| `mesures_conception_p4_v1.py` (inchangé) | `483b8ac3aca65a9879b7d2f2a832cfd5478c48fd860c94a6fbdc041364cc8be7` |
| `instrument_p4_v1.py` | `000281d02c17779937b0033c2e1c724f05548b3f3eaf1ee3cfa94da74afafb8c` |
| `lecture_p4_v1.py` | `0b7a259bc95e8a7fb6c994076d2be72ada47a1d10e9f5d28597afbb14674682a` |
| `test_instrument_p4_v1.py` (inchangé) | `9d015be4ce2bbff4a4541387d5d19ef70497aa41f1a53b9c38724360d7a1dffd` |
| `test_lecture_p4_v1.py` | `305a2e9faf90dd09a48992f76c2ae1a96c8a79d86244b71cd27109698b87f384` |
| `test_gardes_p4_v1.py` | `014a9f85a663602bfeafac809ced04df7ce23ff864a432888822acf9ca397147` |
| `NOTES-MODULE.md`, `NOTES-MODULE-v2.md` (copies) | `7a82f3b7…`, `ad731c27…` |
| `NOTES-MODULE-v3.md`, `RAPPORT-CORRECTION-v1.md` (ce rapport) | dans leurs compagnons |

Sous `…/module-v3-travail/` (compagnons `.sha256`) : `sortie-tests-module-v3.txt`, `comptes-collectes-v3.txt`,
`sortie-test-table-variable-v3.txt`, `paires-texte-module-v3-v3.json`, `ecrire_paires_module_v3_v3.py`,
`simuler_texte_module_v3_v1.py`, `sortie-simulation-texte-module-v3-v3.json`, `sortie-test-table-variable-simulation-v3.txt`,
`simulation/simulation-candidat1-avec-paires-module-v3-NON-CANDIDAT-v3.md` (une simulation, pas un candidat) ; versions de
travail (`…-v1`, `…-v2`, `…-essai*`) ; relevés `git-status-avant.txt`, `git-tete-avant.txt`, `pycache-src-avant.txt` ;
dossiers temporaires des tests (`tmp-*`, dépôts jetables du modèle jouet ; `essai-prefixe`, essai de durée).
