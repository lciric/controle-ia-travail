# Notes du module de P4-instrument (v3) : corrections après les vérifications du module v2

Rédacteur : sous-agent correcteur neuf, lancé par la session le 2026-10-20 (vers 19:50 à 20:45 UTC). Je n'ai écrit ni le
préenregistrement, ni le module v1, ni le module v2, ni aucune vérification. Le préfixe `…/` vaut
`/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p4-instrument`.

Sources :
- texte qui fait foi : `…/P4-instrument-v1-candidat1.md` (`6422fb45a1dc2a3b42a5f6adad4ed8ff02cf89b3c09d91474213c5c1f5fe3bc0`) ;
- module v2 : `…/module-v2/` (intact ; neuf sceaux vérifiés après le travail), avec `RAPPORT-CORRECTION-v1.md`
  (`1272a2bb…`) et `NOTES-MODULE-v2.md` (`ad731c27…`), copiées ici sans changement et valables pour tout ce que ces
  notes-ci ne changent pas ; `NOTES-MODULE.md` (`7a82f3b7…`, notes du v1) aussi ;
- vérifications du v2 : `…/verification-module-v2-contournement/verification-module-v2-contournement-v1.md`
  (`2ce3d0af0a36fbb076d494b59619f4f11ed03fb9172f05e3bdde3087500a335d`) et
  `…/verification-module-v2-fidelite/verification-module-v2-fidelite-v1.md`
  (`ea12d4a2ea780e50e465105c29fb53fbe1e6eace5e3bae1ee177ed17426e7196`) ;
- décisions de la session (toutes acceptées) : VM2-contournement-01 à -08 et VM2-fidelite-01 (liste dans le rapport).

Rien d'autre n'a changé : ni `issue_p4`, ni `LIGNES`, ni les statistiques, ni le run, ni les mesures de conception.

## Ce qui change, et pourquoi

### VM2-contournement-01 : les données suivaient un autre run que le manifeste lu

Avant : la règle de CL3-01 lisait `runs/<run source>/manifeste.json`, mais `verifier_resultat` suit le `run_id` écrit
dans le résumé. Des copies de fichiers scellés (ou un lien symbolique, ou `--run-source ../diag/<run>`) faisaient lire,
sans `--prereg`, les données d'un run décisif sous le manifeste d'un run non décisif.

Maintenant (`lecture_p4_v1.charger_source_p4`, dans tous les modes, avant toute lecture des données) :
- le manifeste lu sous `runs/<run source>/` doit porter `run_id == <run source>` (le dossier) ; sinon `GardeArret` ;
- le résumé, puis l'identité, lus tels qu'écrits, doivent porter ce même `run_id` (`exiger_rattache_au_run`) ; sinon
  `GardeArret` ;
- motif : « … rattaché à un autre run que celui du manifeste lu et du dossier (…) : lecture refusée sans rien écrire »
  (constante `AUTRE_RUN`). `charger_source_p4` est appelée par `analyser` avant `creer_manifeste` : rien n'est écrit.
- `--run-source` doit donc être l'identifiant exact du run (pas de `./`, de `/` final, de chemin absolu ni de `../`).
- Le rattachement à l'empreinte du manifeste reste vérifié comme avant, par `verifier_resultat` : manifeste rescellé →
  L1 « résumé non conforme » (VM2-contournement-08, comportement gardé). Je ne compare donc que le `run_id`, comme la
  décision le dit ; une comparaison de l'empreinte aurait changé en refus les cas que -08 garde en L1.

### VM2-contournement-02, -03 et VM2-fidelite-01 : la table du texte est lue en entier

`table_des_criteres` (réécrite) :
- titre « ## Critères de lecture gelés » compté comme le lit `controle_ia.prereg.sections` : absent → refus ; présent
  plus d'une fois → refus (« présente n fois ») ;
- première ligne de la section qui porte une barre non échappée : l'en-tête exact `| ligne | issue | lecture |` ; puis
  le séparateur (trois cellules `:?-+:?`) ;
- chaque ligne non vide qui suit, jusqu'à la première ligne vide (fin du tableau en Markdown), est une rangée, quelle
  que soit sa forme : barres de bord exigées, début `| Lk |`, première cellule `L` suivie de chiffres, trois cellules ;
  sinon refus (« rangée hors de la forme ») ; une ligne de texte collée sous la table est une rangée en Markdown, donc
  refusée ;
- après la fin du tableau, aucune ligne à barre non échappée dans la section (seconde table : refus) ;
- section sans aucune ligne à barre : table vide, que la garde refuse (« lignes [] ≠ lignes du module »), comme avant.

`exiger_table_des_criteres` compare ensuite, comme au v2, la liste des rangées et chaque cellule à `LIGNES` (rangée en
plus ou en moins, ordre, cellule : refus). Tout refus a lieu avant tout manifeste de lecture : rien n'est écrit.
`test_lecture_p4_v1.table_recodee` (lecture recodée hors du module) suit la même règle, écrite autrement.

### VM2-contournement-04 : configuration non dictionnaire

`est_decisif_ou_reel` : une clé `config` présente dont la valeur n'est pas un dictionnaire (liste, nulle, texte, nombre)
rend vrai. Sans `--prereg`, la lecture est donc refusée au motif de CL3-01 (« ARRÊT », code 1, aucune trace Python).
En mode décisif, `exiger_lecture_sous_prereg_p4` traite la même configuration comme « hors du mode réel » (refus de
garde, L1 écrite, comme les autres gardes du mode décisif) au lieu d'une `AttributeError`. Une clé `config` absente
garde le comportement du v2 (test existant « mode absent »).

### VM2-contournement-05 : pas de manifeste orphelin

`analyser` : si `diag/<run de lecture>` existe (dossier, fichier ou lien symbolique, même pendant), refus R12 juste
avant `creer_manifeste` : « … existe déjà : R12 interdit d'écraser ; lecture refusée sans rien écrire ».

### VM2-contournement-06 : aucun cache de code

`sys.dont_write_bytecode = True` en tête de `lecture_p4_v1.py` et de `instrument_p4_v1.py`, juste après
`from __future__ import annotations` (qui doit rester la première instruction ; il n'importe que la bibliothèque
standard), avant tout import du dépôt et de numpy. Commandes des docstrings écrites avec `python -B`. Les constantes
`COMMANDE` (écrites dans les manifestes) ne changent pas.

### VM2-contournement-07 : `lire` sans manifeste

`lire` refuse une source d'état « complet » dont `manifeste` est absent ou n'est pas un dictionnaire
(`MOTIF_SANS_MANIFESTE`). Les sources « L1 » et « arret » se lisent comme avant. Les sources synthétiques de
`test_lecture_p4_v1.py` portent désormais un manifeste jouet non décisif (`MANIFESTE_SYNTHETIQUE`).

### VM2-contournement-08 : rien à faire

Comportement L1 gardé pour un manifeste du run décisif altéré (sans `decisif`, rescellé). Une seule des huit formes de
la vérification change, par la règle de -01 : le manifeste d'un autre run recopié sous `runs/<run décisif>/` porte un
`run_id` autre que celui du dossier ; il est maintenant refusé sans rien écrire (le v2 écrivait L1). Test :
`test_manifeste_du_run_decisif_rescelle_l1_gardee_manifeste_d_un_autre_run_refuse`.

## Fichiers

| fichier | changement |
|---|---|
| `mesures_conception_p4_v1.py` | aucun (`483b8ac3…`, sceau copié) |
| `instrument_p4_v1.py` | -06 : `sys.dont_write_bytecode = True` avant les imports ; docstring (commandes avec `-B`) ; aucun autre code |
| `lecture_p4_v1.py` | -01, -02, -03, -04, -05, -06, -07 (ci-dessus) ; docstrings |
| `test_instrument_p4_v1.py` | aucun (`9d015be4…`, sceau copié ; 71 tests) |
| `test_lecture_p4_v1.py` | compte 43 → 49 ; `table_recodee` lue en entier ; six tests neufs sur le texte nommé par `P4_TEXTE_PREREG` ; manifeste jouet des sources synthétiques |
| `test_gardes_p4_v1.py` | compte 101 → 138 ; 37 tests neufs (ci-dessous) ; en-tête |
| `NOTES-MODULE.md`, `NOTES-MODULE-v2.md` | aucun (copies) |
| `NOTES-MODULE-v3.md` | neuf (ces notes) |

## Section du texte → fonction (ajouts)

| section | fonction |
|---|---|
| Liste d'arrêt et plan d'analyse, point 2 (rattachement au run source) | `lecture.charger_source_p4`, `lecture.exiger_rattache_au_run`, `lecture.AUTRE_RUN` |
| Critères de lecture gelés (table lue en entier) | `lecture.table_des_criteres`, `lecture._cellules_de`, `lecture.exiger_table_des_criteres` |
| Liste d'arrêt (lecture sans `--prereg`, configuration non dictionnaire) | `lecture.est_decisif_ou_reel`, `lecture.exiger_lecture_sous_prereg_p4` |
| Liste d'arrêt (`diag/<run de lecture>` présent) | `lecture.analyser` |
| Plan d'analyse, point 2 (commande) | en-têtes de `lecture_p4_v1.py` et `instrument_p4_v1.py` (`sys.dont_write_bytecode`) |

## Tests

Comptes : `test_instrument_p4_v1.py` 71, `test_lecture_p4_v1.py` 49, `test_gardes_p4_v1.py` 138 ; total 258. Chaque fichier
écrit son nombre en tête et le vérifie. Neufs, chaque fois cas sain et artefact (R5) :

- -01 (`test_gardes_p4_v1.py`, 8) : sain, run jouet lu sous son nom exact (résumé et identité au même `run_id`, C1
  calculé) ; six artefacts, chacun refusé par `charger_source_p4` et par `analyser`, sans rien écrire, arbre propre :
  manifeste de X recopié sous Y avec résumé et identité du run décisif (aussi en ligne de commande : « ARRÊT », code 1,
  sans trace), manifeste neuf de Y avec résumé et identité du run décisif recopiés, `diag/Y` lien symbolique vers le
  run décisif, `--run-source ../diag/<run décisif>`, résumé de Y écrit sous son manifeste avec l'identité du run
  décisif, `--run-source X/` ; plus -08 gardé (manifeste rescellé : L1) à côté de la forme qui change (refus).
- -02, -03, VM2-fidelite-01 : `test_gardes_p4_v1.py`, treize artefacts ajoutés au test paramétré de la table (rangée sans
  barre initiale, en gras, « L6bis », « L 12 », « l12 », « M1 », ligne collée sous la table, seconde table, en-tête autre,
  séparateur absent, section en double ×3) ; trois cas sains de forme (paragraphes avant et après la table, espaces de
  fin et séparateur aligné, table en fin de section) ; deux lectures décisives (verdict versé) refusées sans rien
  écrire (rangée sans barre initiale, section en double), chacune après son cas sain ; `test_lecture_p4_v1.py`, six
  retouches du texte nommé par `P4_TEXTE_PREREG`, refusées par la lecture recodée et par la garde, après le cas sain sur
  le même texte.
- -04 (2) : règle (liste, nulle, texte, nombre : refus ; jouet : permis) et ligne de commande sur un manifeste rescellé
  à `config = ["x"]` sans `decisif` (« ARRÊT » au motif de CL3-01, code 1, sans trace, rien d'écrit) ; mode décisif :
  un artefact de plus au test des gardes (« hors du mode réel », pas d'`AttributeError`).
- -05 (4) : sain (lecture écrite) ; `diag/<lecture>/lecture-p4.json` présent, dossier vide, lien symbolique pendant :
  refus R12, aucun `runs/<lecture>`, arbre inchangé.
- -06 (4) : lecture refusée et `--controle module` refusé, lancés sans `-B` ni `PYTHONDONTWRITEBYTECODE`, module versé
  sous `docs/procedures/P4-instrument-v1/` d'un dépôt jetable, code du dépôt copié hors du dépôt réel : aucun
  `__pycache__` ni `.pyc` (sain) ; ligne retirée → le cache s'écrit (artefact ; `PYTHONPYCACHEPREFIX` l'envoie sous
  le dossier temporaire des tests, rien n'est écrit dans l'environnement Python ni dans le dépôt réel).
- -07 (1) : source chargée lue (sain) ; source L1 sans manifeste lue ; source « complet » sans manifeste (clé retirée,
  nulle, texte, clés `manifeste` et `lien` retirées) : refus.

Variable `P4_TEXTE_PREREG` : sept tests de `test_lecture_p4_v1.py` la lisent (celui du v2 et les six neufs). Absente, ou
fichier absent, ou brouillon 4 : les sept échouent, aucun ne saute ; candidat 1 : les sept passent.

### Commande exacte de la suite

Une fois le module versé sous `docs/procedures/P4-instrument-v1/` et le texte scellé (S) :

```
P4_TEXTE_PREREG=prereg/P4-instrument-v1.md PYTHONPATH=src python -B -m pytest -q -p no:cacheprovider docs/procedures/P4-instrument-v1/test_instrument_p4_v1.py docs/procedures/P4-instrument-v1/test_lecture_p4_v1.py docs/procedures/P4-instrument-v1/test_gardes_p4_v1.py
```

Commande lancée ici (dépôt lu seulement) :

```
cd /home/user/controle-ia-travail && P4_TEXTE_PREREG=…/P4-instrument-v1-candidat1.md PYTHONPATH=src PYTHONDONTWRITEBYTECODE=1 /tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad/scellement-revalidation/venv-gpu-neuf/bin/python -B -m pytest -q -p no:cacheprovider --basetemp=…/module-v3-travail/tmp-suite-finale-v3 …/module-v3/test_instrument_p4_v1.py …/module-v3/test_lecture_p4_v1.py …/module-v3/test_gardes_p4_v1.py
```

Dernière ligne : `258 passed in 233.29s (0:03:53)`, code 0. Sortie : `…/module-v3-travail/sortie-tests-module-v3.txt`.

## À reporter dans le texte et dans la chaîne

- Texte : phrases exactes (paires ancien → nouveau) dans `RAPPORT-CORRECTION-v1.md` et
  `…/module-v3-travail/paires-texte-module-v3-v3.json` ; « Tests attendus » `1166` (908 + 258 ; 71, 49 et 138) ; six
  lignes « Module de P4 » aux empreintes ci-dessous.
- Chaîne (v2, lue pour les seuls appels de la lecture) : elle passe `P4_TEXTE_PREREG`, `-B`, et des identifiants de run
  exacts (`basename`) ; son contrôle du refus de CL3-01 cherche le même motif, inchangé. Rien à changer, à revérifier
  par la session sur la chaîne retenue.

## Empreintes (sha256)

Chaque fichier a son compagnon `.sha256`, au format « <empreinte>  <nom> ».

| fichier | sha256 | état |
|---|---|---|
| `mesures_conception_p4_v1.py` | `483b8ac3aca65a9879b7d2f2a832cfd5478c48fd860c94a6fbdc041364cc8be7` | inchangé |
| `instrument_p4_v1.py` | `000281d02c17779937b0033c2e1c724f05548b3f3eaf1ee3cfa94da74afafb8c` | changé (v2 : `c3e78bec…`) |
| `lecture_p4_v1.py` | `0b7a259bc95e8a7fb6c994076d2be72ada47a1d10e9f5d28597afbb14674682a` | changé (v2 : `3e41ec10…`) |
| `test_instrument_p4_v1.py` | `9d015be4ce2bbff4a4541387d5d19ef70497aa41f1a53b9c38724360d7a1dffd` | inchangé |
| `test_lecture_p4_v1.py` | `305a2e9faf90dd09a48992f76c2ae1a96c8a79d86244b71cd27109698b87f384` | changé (v2 : `7f1bceb1…`) |
| `test_gardes_p4_v1.py` | `014a9f85a663602bfeafac809ced04df7ce23ff864a432888822acf9ca397147` | changé (v2 : `42af1efc…`) |
| `NOTES-MODULE.md` | `7a82f3b7770c36a15afbf8065e3f1f92424e533ac0ffa02bb066eabfedc958cc` | copie |
| `NOTES-MODULE-v2.md` | `ad731c278344f89bdc5af96f998d33f5a958d1c879ab80336b7f0849b32081ab` | copie |
