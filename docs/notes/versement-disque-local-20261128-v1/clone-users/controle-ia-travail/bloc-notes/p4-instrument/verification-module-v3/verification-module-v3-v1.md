# Vérification du module v3 de P4-instrument (vérificateur neuf, adverse) — v1

Vérificateur : sous-agent neuf, lancé le 2026-10-20 (vers 20:37 à 21:10 UTC). Je n'ai écrit ni le texte, ni aucune
version du module, ni aucun rapport de correction ou de vérification. Le préfixe `…/` vaut
`/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p4-instrument`.

## Verdict

**Conforme après corrections.** Les huit décisions sont appliquées dans `…/module-v3/`, chacune avec cas sain et
artefact. Aucune voie normale, et aucune de mes 36 voies, ne lit un run décisif ou réel sans le verdict complété de P3,
hors la fraude délibérée déjà déclarée (CR3-02). Aucune table différente ne passe dans la section lue. Le différentiel
se limite aux décisions. Suite : 258 passés (71, 49, 138), dont les 215 anciens. Empreintes égales aux compagnons.

Une correction, de forme, sur le texte (VM3-01) : deux phrases proposées disent « refusée sans rien écrire » dans un cas
où le module écrit L1 (mode décisif). Paires corrigées plus bas, mêmes ancres, éprouvées. Le module ne change pas.

## Pièces relues

| pièce | sha256 |
|---|---|
| `…/P4-instrument-v1-candidat1.md` (texte qui fait foi) | `6422fb45a1dc2a3b42a5f6adad4ed8ff02cf89b3c09d91474213c5c1f5fe3bc0` (égale à la citation et au compagnon) |
| `…/module-v3/RAPPORT-CORRECTION-v1.md` | `5a2d1626d9abd859c5465f14563d65da80d3f197411de9d3c8172d4db1a45e30` (égale au compagnon) |
| `…/module-v3/NOTES-MODULE-v3.md` | `5435cf177a5fc59a05480281c95bd3ec2cc9bd938ebe7072759455b10b841a32` (égale) |
| `…/module-v3/` six fichiers de code | voir (5) ; tous égaux à leurs compagnons |
| `…/module-v2/` (neuf fichiers, dont `RAPPORT-CORRECTION-v1.md` `1272a2bb…`, `NOTES-MODULE-v2.md` `ad731c27…`) | neuf sceaux vérifiés |
| `…/verification-module-v2-contournement/verification-module-v2-contournement-v1.md` | `2ce3d0af0a36fbb076d494b59619f4f11ed03fb9172f05e3bdde3087500a335d` (égale) |
| `…/verification-module-v2-fidelite/verification-module-v2-fidelite-v1.md` | `ea12d4a2ea780e50e465105c29fb53fbe1e6eace5e3bae1ee177ed17426e7196` (égale) |
| `…/module-v3-travail/paires-texte-module-v3-v3.json` (paires proposées) | `d898bb85bc6cd0c6b6832e4d58c65482fefde076f4d98ad609267ad996cfc243` (égale au compagnon) |
| `…/ecrire_candidat2_v1.py` (paires fixes, T2, T3 ; lu, jamais exécuté) | `9a59358ec3bafa7ba444d2881943ed5be51778e9098dbc7640261417cc7d4480` |
| `…/chaine-v2/paires-candidat2-chaine-v2-v1.json` (pour la simulation) | `2f5a591b8bd7d420509026c6d63e626602648f5d6925a391829ce560b34378fb` (égale) |

Code gelé lu, en lecture seule : `src/controle_ia/manifeste.py`, `prereg.py`, `scellement.py` (début). Lignes de la chaîne
v2 trouvées par `grep` (scripts seulement). Non lus : `prereg/P3-consignes-v1.md`, tout `textes-actions-*`, rien sous
`donnees/` du dépôt.

## Cadre tenu

- Dépôt de travail en lecture seule. `git --no-optional-locks status --porcelain` vide avant et après ; tête `a82dac7`
  avant et après ; `src/controle_ia/__pycache__` : même relevé, mêmes dates.
- **Écart de cadre, déclaré.** Deux fois, `find /home/user/controle-ia-travail/src -newer <marqueur>` (noms seuls, aucun
  contenu lu, rien trouvé), pour prouver qu'aucun cache n'avait été écrit. C'est une recherche récursive dans `src/` du
  dépôt, contraire à la lettre du cadre. Rien sous `donnees/`. À consigner par la session.
- Le test de -06 du module, et mes voies F, copient `src/controle_ia` (code, sans caches) dans un dossier temporaire, comme
  le fait le test du correcteur.
- Python de la tâche, `-B`, `PYTHONDONTWRITEBYTECODE=1`, `-p no:cacheprovider`. Seuls le test de -06 et mes voies F lancent
  Python sans `-B`, par construction. Avant : les 35 modules chargés au démarrage ont un cache valide. Après : aucun fichier
  plus récent que mes marqueurs dans l'environnement Python ni dans `/usr/lib/python3.11`.
- Tests lancés sur des **copies octet pour octet** du v3 (`travail/copie-v3/`, sceaux vérifiés après). `module/` (7 sur 7),
  `module-v2/` (9 sur 9), `module-v3/` (10 sur 10) : intacts, aucun `__pycache__`.
- Dépôts jouets jetables seulement. Aucune commande Vast.ai, aucun réseau, aucune clé. Aucune moyenne ni médiane sur les
  jetons. Écrit seulement sous `…/verification-module-v3/`.

## (1) Décisions, une par une

| décision | où (v3) | cas du module (tests) | mes voies | constat |
|---|---|---|---|---|
| VM2-contournement-01 | `lecture_p4_v1.py` l. 357-369 (`exiger_rattache_au_run`), l. 385-387 (manifeste), l. 392 et 399 (résumé, identité) | `test_donnees_rattachees_au_run_source_cas_sain` ; `…_a_un_autre_run_refusees_sans_rien_ecrire` (6 formes, ligne de commande) ; `test_manifeste_du_run_decisif_rescelle_…` | B : 8 formes (copies, liens physiques, liens de fichiers, liens de dossiers, `../diag/`, manifeste de X sur le run décisif, `runs/<décisif>` → X, `Y/.`) | appliquée : 8 refus, « ARRÊT », code 1, rien écrit |
| -02, -03, VM2-fidelite-01 | l. 89-94, 218-270 (`_cellules_de`, `table_des_criteres`) ; `test_lecture.table_recodee` | 13 artefacts et 3 sains ajoutés ; 2 lectures décisives refusées ; 6 retouches du texte nommé par `P4_TEXTE_PREREG` | épreuve de table : 31 cas sur 31 conformes (4 sains, 27 refus) | appliquée ; voies hors section : VM3-02 |
| -03 (titre en double) | l. 237-241 | 3 formes « section en double » | F6, D1, D2 : refus « présente 2 fois » | appliquée |
| -04 | l. 288-295 (`est_decisif_ou_reel`) ; l. 205-207 (mode décisif) | `test_config_non_dictionnaire_suspecte_…` ; artefact « configuration non dictionnaire » | D : `None`, `"reel"`, `3`, `[]`, `["x"]` rescellés, et sceau rompu : « ARRÊT », motif de CL3-01, code 1, sans trace | appliquée ; en mode décisif : L1 au lieu d'une trace (cohérent avec le texte) |
| -05 | l. 936-938 | `test_diag_de_lecture_existant_refus_r12_…` (sain + 3) | E : fichier ordinaire, lien vers un dossier, lien pendant, dossier avec sous-dossier | appliquée : refus R12, aucun `runs/<lecture>` |
| -06 | `lecture_p4_v1.py` l. 53-55 ; `instrument_p4_v1.py` l. 46-48 ; docstrings avec `-B` | `test_lancement_refuse_sans_option_b_…` (sain et artefact, deux scripts) | F : lecture lue, lecture refusée, contrôle du module refusé, sans `-B` : aucun cache | appliquée ; reste CR3-05 (VM3-05) |
| -07 | l. 848-849 | `test_lire_refuse_une_source_complete_sans_manifeste` | G : absent, `None`, liste : refus ; `{}` ou dictionnaire fabriqué : lu (VM3-06) | appliquée |
| -08 | rien | L1 gardée (manifeste rescellé) | D09 : L1 écrite, rien lu ; C02 : `x/../<run>` : L1 écrite, rien lu | gardée ; une forme passe à refus (manifeste d'un autre run recopié), par -01 |

Run décisif ou réel sans verdict complété, toutes voies normales : A02 (sans `--prereg`) et A04 (mode réel) : « ARRÊT »,
motif de CL3-01 ; A03 (`--prereg`, verdict absent) : report ; rien écrit. Cas sain A01 : run jouet lu, C1 calculé.

## Voies adverses (36, toutes jouées ; une ligne par voie dans `travail/voies-v1.txt`)

| voie | résultat |
|---|---|
| B09 fraude par les fonctions gelées : `creer_manifeste` d'un Y non décisif, résumé et identité du run décisif réécrits sous Y par `ecrire_resultat` | **lu** : code 0, C1 calculé (aire 0,5556, valeur de la démonstration de CL3-01), tables du run décisif (VM3-03 ; CR3-02 confirmé) |
| C01 mode décisif, verdict versé, manifeste de X recopié sur celui du run décisif | **L1 écrite** sous un manifeste de lecture décisif (« run source … non décisif ou hors du mode réel ») ; sans `--prereg`, même montage : refus `AUTRE_RUN` (VM3-01) |
| C02 `--run-source x/../<run décisif>`, `runs/x` absent | L1 écrite, manifeste non lu, aucune donnée lue (comportement -08 gardé) |
| D08 manifeste du run décisif remplacé par un JSON scellé : `[1, 2]`, `"texte"`, `null` | **trace Python** (`TypeError`), code 1, rien écrit (VM3-04 ; CR3-04 confirmé) ; objet sans `config` : L1 écrite |
| D `config = {"a": 1}`, `decisif` retiré, rescellé | L1 écrite (« mode absent », comportement du v2) |
| F04 `mesures_conception_p4_v1.py` sans `-B`, préfixe de cache vers le dossier temporaire | le cache d'`instrument_p4_v1` est décidé sous le dossier du module (VM3-05 ; CR3-05 confirmé) |
| G `lire` sur source fabriquée, `manifeste = {}` ou non décisif fabriqué | lu (VM3-06) |
| les 26 autres (A 4, B 8, D 7 dont D07 et D09, E 4, F 3) | conformes aux décisions (tableau du (1)) |

Épreuve de table (`travail/sortie-epreuve-garde-table-v3-v1.json`), sur le candidat 1 retouché une fois par cas : 31 cas
sains ou à refuser, tous conformes ; neuf voies hors de la section lue (H1 à H8, et H10 : `travail/sortie-h10-…`) passent,
une (H9, titre dans un bloc de code) est refusée. Lecture recodée indépendante du candidat 1 : 22 cellules égales.

## (2) Différentiel `module-v2/` → `module-v3/`

`diff -u` (`travail/diff-*.txt`) et arbre syntaxique (`travail/sortie-differentiel-ast-v2-v3.json`) :

- `mesures_conception_p4_v1.py`, `test_instrument_p4_v1.py`, `NOTES-MODULE.md`, `NOTES-MODULE-v2.md` : identiques ;
- `instrument_p4_v1.py` : docstring et ligne `sys.dont_write_bytecode` ; aucun autre nœud de code (-06) ;
- `lecture_p4_v1.py` : constantes neuves ; `_cellules_de`, `exiger_rattache_au_run` neuves ; changées :
  `exiger_lecture_sous_prereg_p4` (-04), `table_des_criteres` (-02, -03), `est_decisif_ou_reel` (-04),
  `charger_source_p4` (-01), `lire` (-07), `analyser` (-05, docstring) ; `LIGNES`, `issue_p4`, statistiques : inchangés ;
- `test_lecture_p4_v1.py` : `source_synthetique` porte un manifeste jouet (exigé par -07), `table_recodee` réécrite,
  test de la table remanié par une aide (mêmes assertions), un test paramétré neuf (6) ;
- `test_gardes_p4_v1.py` : deux tests paramétrés étendus, 37 tests neufs ; aucune autre fonction changée.

Rien hors des décisions.

## (3) Tests

- Comptes par collecte : v2 71, 43, 101 (215) ; v3 71, 49, 138 (258) ; chaque en-tête égale sa collecte. Les 215
  identifiants du v2 sont tous dans le v3 ; 43 neufs (`travail/ids-*.txt`).
- Suite v3, trois fichiers ensemble, `P4_TEXTE_PREREG` = candidat 1 : **258 passed in 292.45s**, code 0
  (`travail/sortie-suite-v3.txt`, empreintes des fichiers lancés en tête).
- Les sept tests qui lisent `P4_TEXTE_PREREG` (`travail/sortie-tests-variable-v3.txt`) : variable absente, 7 échecs ;
  fichier absent, 7 échecs « (R11) » ; brouillon 4, 7 échecs (L1 issue, L4 issue, L4 lecture) ; candidat 1, 7 passés.
  Jamais un saut.

## (4) Phrases proposées pour le texte

- Chaque ancre des sept paires est trouvée **une seule fois** dans le candidat 1 (lignes 708, 592, 474, 475, 481, 52,
  721), et encore une fois après les paires précédentes (`travail/sortie-comptes-ancres-v1.json`). Aucune ancre ne
  reparaît dans un « nouveau ».
- Simulation indépendante (`scripts/simuler_candidat2_v3_v1.py`, pas un candidat) : paires fixes de l'écrivain, lignes
  « Module de P4 » du v3, T2 avec `1166`, T3, paires de la chaîne v2, paires du v3, dans les deux ordres : 42 ancres
  trouvées une fois chacune, même texte ; table : 22 cellules égales ; validateur : rien ; six lignes « Module de P4 »
  égales au v3 ; « Tests attendus : `1166` » lu une fois ; sept tests de la variable passés sur ce texte.
- Nombres : 908 + 258 = 1 166 ; 71, 49, 138 ; sept tests lisent la variable. Justes.
- Exactitude : phrases 2, 3, 6, 7 exactes. Phrases 1 (troisième tiret) et 5 : inexactes en mode décisif (VM3-01).
  Phrases 1 (deuxième tiret) et 4 : ne disent pas le refus d'une seconde table, que le module fait et que la phrase 2
  teste (VM3-01).
- Le rapport du correcteur coupe la phrase 7 sur deux lignes (renvoi Markdown) : le JSON fait foi, sans effet.

## (5) Empreintes

`sha256sum -c` : `module-v3/` 10 sur 10, `module-v2/` 9 sur 9, `module/` 7 sur 7, `module-v3-travail/` 25 sur 25 (dont
trois sous `simulation/`), candidat 1 et les deux vérifications du v2 : « OK ». Empreintes du v3, égales à celles citées
par le rapport et les notes :

| fichier | sha256 |
|---|---|
| `mesures_conception_p4_v1.py` (inchangé) | `483b8ac3aca65a9879b7d2f2a832cfd5478c48fd860c94a6fbdc041364cc8be7` |
| `instrument_p4_v1.py` | `000281d02c17779937b0033c2e1c724f05548b3f3eaf1ee3cfa94da74afafb8c` |
| `lecture_p4_v1.py` | `0b7a259bc95e8a7fb6c994076d2be72ada47a1d10e9f5d28597afbb14674682a` |
| `test_instrument_p4_v1.py` (inchangé) | `9d015be4ce2bbff4a4541387d5d19ef70497aa41f1a53b9c38724360d7a1dffd` |
| `test_lecture_p4_v1.py` | `305a2e9faf90dd09a48992f76c2ae1a96c8a79d86244b71cd27109698b87f384` |
| `test_gardes_p4_v1.py` | `014a9f85a663602bfeafac809ced04df7ce23ff864a432888822acf9ca397147` |

Seule empreinte citée qui ne tient plus : `controles_avant_depense_p4_v1.sh` de la chaîne v2 (VM3-08).

## Constats (le plus grave d'abord)

### VM3-01 — forme — deux phrases disent « refusée sans rien écrire » là où le module écrit L1

- **Où** : `…/module-v3-travail/paires-texte-module-v3-v3.json`, paire 1 (troisième tiret) et paire 5 ; module :
  `lecture_p4_v1.py` l. 923-935 (gardes du mode décisif avant `charger_source_p4`).
- **Preuve** (voie C01) : mode décisif, verdict complété versé, manifeste du run non décisif X recopié sous
  `runs/<run décisif>/`. La garde « run source décisif, en mode réel » refuse d'abord : **L1 écrite**, sous un manifeste
  de lecture décisif. La règle de -01 n'est pas atteinte. Or la phrase 5 dit « Dans tous les modes, avant toute lecture
  des données du run source : le manifeste lu … porte l'identifiant de ce run … sinon la lecture est refusée sans rien
  écrire », et la paire 1 « Manifeste lu … d'un autre run … : lecture refusée sans rien écrire (pas une ligne) ». Sans
  `--prereg`, même montage : refus, rien écrit. Aucune donnée n'est lue dans les deux cas.
- **Même défaut, plus léger** : le module refuse toute barre non échappée hors du tableau (seconde table) ; la phrase 2
  le teste ; les phrases 1 (deuxième tiret) et 4 ne le disent pas.
- **Gravité** : forme. Voie délibérée seulement ; sûre dans les deux modes. Mais un verdict R13 qui suit le texte verrait
  un écart entre texte et module.
- **Correction recommandée** : changer le texte, pas le module. Paires 1, 4 et 5 corrigées ci-dessous, mêmes ancres.
  Éprouvées : ancres trouvées une fois ; simulation complète conforme ; sept tests de la variable passés
  (`travail/paires-texte-module-v3-corrigees-vm3-v2.json`). Autre voie, plus chère : vérifier le `run_id` du manifeste
  dans `analyser` avant toute garde (module v4, tests, vérification).

### VM3-02 — information — seconde section ou table hors de la section lue : la garde ne la voit pas

- **Preuve** (`travail/sortie-epreuve-garde-table-v3-v1.json`) : une table autre (L1 changée) passe la garde, avec
  « 22 cellules égales », si elle est sous un titre d'apparence identique : espace sans chasse U+200B (H1), espace
  insécable (H2), accent décomposé (H3), titre séparé par des retours chariot seuls (H10). Elle passe aussi sous
  `# Critères…` (H4), `### Critères…` (H5), titre souligné (H6), ou « (suite) » (H8). Une table HTML dans la section passe
  aussi (H7). Le validateur ne voit rien.
- **Gravité** : information. Les décisions portent sur la section de ce titre exact ; tout cela est délibéré et visible
  à la lecture ; rien de tel dans le candidat 1 ni dans les paires (simulation).
- **Durcissement facultatif** : refuser tout titre de tout niveau dont le texte normalisé (NFKC, sans caractères de
  format, espaces réduits) commence par « Critères de lecture gelés », hors la section ; refuser `<table` dans la section.

### VM3-03 — information — CR3-02 confirmé : une fraude par les fonctions gelées lit le run décisif

- **Preuve** (B09) : C1 calculé sur les tables du run décisif, aire 0,5556 ; aucune règle de -01 n'est en défaut.
- **Lecture** : il faut écrire deux résultats scellés neufs. Le durcissement proposé (tables sous
  `donnees/<run source>/`) n'ajoute qu'une copie : les tables `.npz` ne portent pas de `run_id`. Même classe qu'un verdict
  complété fabriqué. Recommandation : ne rien changer, consigner la limite.

### VM3-04 — information — CR3-04 confirmé : manifeste scellé qui n'est pas un objet JSON, trace Python

- **Preuve** (D08) : `[1, 2]`, `"texte"`, `null` : `TypeError` levée par `lire_manifeste` (code gelé), non attrapée par
  `analyser`, code 1, rien écrit. Pas un repli silencieux ; mais une trace, ce que -04 voulait éviter pour la configuration.
- **Correction possible** (hors des décisions) : ajouter `TypeError` aux exceptions attrapées dans `analyser` et
  `charger_source_p4`.

### VM3-05 — information — CR3-05 confirmé ; commande documentée de `mesures_conception_p4_v1.py` sans `-B`

- **Preuve** (F04) : lancé sans `-B`, le cache d'`instrument_p4_v1` est écrit avant que sa ligne s'exécute.
  `mesures_conception_p4_v1.py` l. 21 documente `python …` sans `-B`. Lancée telle quelle à la racine, elle écrirait sous
  `docs/procedures/P4-instrument-v1/__pycache__/`, que `verifier-arbre` refuserait. La chaîne v2 la lance avec `-B`
  (`controles_avant_depense_p4_v1.sh` l. 305).
- **Suite possible** : à une prochaine version, `-B` dans cette docstring, ou la ligne en tête. Hors des décisions.

### VM3-06 — information — `lire` accepte un manifeste fabriqué de forme dictionnaire

- **Preuve** (G) : `manifeste = {}`, ou dictionnaire non décisif fabriqué : la source « complet » est lue. Appel Python
  délibéré, même classe que le lien fabriqué du v2 (CR-03). Aucune voie de la ligne de commande.

### VM3-07 — information — « chemin détourné » sans manifeste lu

- **Preuve** (C02) : `--run-source x/../<run décisif>`, `runs/x` absent : le manifeste n'est pas lu ; L1 « manifeste du
  run source absent ou illisible » est écrite ; aucune donnée lue. Comportement -08, inchangé depuis le v2. La phrase 1
  corrigée parle du manifeste « lu », donc reste exacte.

### VM3-08 — information — chaîne v2 en mouvement

- Le rapport du correcteur cite `controles_avant_depense_p4_v1.sh` à `c881d0c4…` ; le fichier vaut maintenant
  `c44bd6893c3b201ceb9273ce2a8b3a73b99ebf1589e325ee8fab11a61a9ddbeb` (modifié à 20:24:46 UTC, après sa lecture).
- Chaîne actuelle (`grep`) : identifiants exacts (`basename`), motif de CL3-01 attendu, `-B` partout, aucun appel
  direct de `charger_source_p4` ni de `lire`. Paires de la chaîne v2 et du v3 compatibles (simulation). À revérifier
  sur la chaîne retenue.

## Texte à ajouter au candidat (paires exactes ; « \n » = retour à la ligne du texte)

Utiliser `…/verification-module-v3/travail/paires-texte-module-v3-corrigees-vm3-v2.json`
(`324c164fd1cd2d9c654ec8b0ed120ed2cca90a224151652c3467e0640574ba7a`) **à la place de**
`…/module-v3-travail/paires-texte-module-v3-v3.json`, avec `TESTS_ATTENDUS=1166` et `MODULE_DIR=…/module-v3`. Mêmes
ancres ; paires 2, 3, 6 et 7 inchangées ; seules les paires 1, 4 et 5 changent :

1. Paire 1, ancien : « - Lecture demandée avant le scellement du verdict complété de P3 (addendum 2), ou avant le scellement de ce texte :\n  refusée sans rien écrire et reportée (pas une ligne). »
   Nouveau : « - Lecture demandée avant le scellement du verdict complété de P3 (addendum 2), ou avant le scellement de ce texte,\n  ou sans `--prereg` sur un run source décisif ou en mode réel (configuration du manifeste qui n'est pas un\n  dictionnaire comprise) : refusée sans rien écrire et reportée (pas une ligne).\n- Lecture décisive dont la table « Critères de lecture gelés » de ce texte diffère de la table du module (`LIGNES`\n  de `lecture_p4_v1.py`) d'une cellule, d'une rangée ou de l'ordre ; section « Critères de lecture gelés » présente\n  plus d'une fois, ou dont une ligne hors du tableau porte une barre non échappée (seconde table) ; rangée, entre\n  l'en-tête et la fin du tableau, hors de la forme `| Lk | issue | lecture |` : refusée sans rien écrire (pas une\n  ligne) ; écart entre le texte et le module : nœud.\n- Manifeste lu sous `runs/<run source>/`, résumé ou identité du run source dont l'identifiant de run n'est pas\n  celui du dossier (copie, lien symbolique, chemin détourné), vu au chargement des données du run : lecture\n  refusée sans rien écrire (pas une ligne) ; en mode décisif, une autre garde du mode décisif qui refuse avant ce\n  chargement écrit L1 (plan d'analyse, point 2).\n- Dossier `diag/<run de lecture>` déjà présent : lecture refusée sans rien écrire (R12). »
2. Paire 4, ancien : « module à l'empreinte\n   citée (`exiger_module_cite`) ; »
   Nouveau : « module à l'empreinte\n   citée (`exiger_module_cite`) ; table « Critères de lecture gelés » de ce texte égale à celle du module, lue en\n   entier : section présente une seule fois, aucune barre non échappée hors du tableau ; chaque rangée, entre\n   l'en-tête et la fin du tableau, de la forme « `| Lk | issue | lecture |` » ; mêmes rangées, même ordre, mêmes\n   cellules (sinon refus, rien n'est écrit, pas une ligne) ; »
3. Paire 5, ancien : « sans autre table\n   (VP3-06). »
   Nouveau : « sans autre table\n   (VP3-06). Sans `--prereg`, seul un run source ni décisif ni en mode réel se lit (répétition jouet) ; un run\n   source décisif ou en mode réel, ou dont la configuration du manifeste n'est pas un dictionnaire, est refusé sans\n   rien écrire (liste d'arrêt). Dans tous les modes, au chargement des données du run source (en mode décisif, après\n   les gardes ci-dessus, dont les refus restent ceux dits plus haut) : le manifeste lu sous `runs/<run source>/`\n   porte l'identifiant de ce run ; le résumé et l'identité portent ce même identifiant ; sinon la lecture est refusée\n   sans rien écrire (leur rattachement à l'empreinte de ce manifeste reste vérifié : sinon récupération non conforme,\n   ligne L1). Dossier `diag/<run de lecture>` déjà présent : refus (R12), rien n'est écrit. »
4. Inchangé : « Tests attendus : `1166` » (paire T2 de l'écrivain), « les 258 du module de P4 (71, 49 et 138 … sept
   tests … échouent) », « (faits, 194 tests ; module v3 … : 258 tests) », six lignes « Module de P4 » du v3.

## Pièces écrites

Sous `…/verification-module-v3/`, chaque pièce avec son compagnon `.sha256` :

| pièce | sha256 |
|---|---|
| `scripts/test_voies_module_v3_v1.py` (36 voies) | `09ac81ec3b64aeb43c12dfe02569e582daff483bd67d1aa1081f789066fe2963` |
| `scripts/eprouver_garde_table_v3_v1.py` | `410b5ee0f4296756af729be50ad1b21cafcfa3c2756bcf358ba86d6a2f3c133e` |
| `scripts/simuler_candidat2_v3_v1.py` | `51232528a0f5177c6373074f4b8b6b2b03fb5e90e5a54539f1d70c2086df48d4` |
| `scripts/compter_ancres_v1.py` | `cec3206f5c70c74430ffcf7ee8507c6a1ccccf2b903c78f427721352545a2dbe` |
| `scripts/differentiel_ast_v1.py` | `15843f91c36ce968525197ed131339702c0c841e17e3af3b92ca044116e5cb52` |
| `scripts/ecrire_paires_corrigees_vm3_v1.py`, `…_v2.py` (v1 : version de travail) | `76bed018aa94a8957e27bc57f42cb2d1b7e288b20004fa0eb862e1b712fea2ad`, `3721a3b0d4c485901dddc35c24cccd8cb040ab8fc107579f218df89f2f583ea2` |
| `travail/voies-v1.txt` ; `travail/sortie-voies-v1.txt` (36 passed) | `b03fd062e2315b3d60750d516285319246ab3908f3f24fa23adf92b6c74f67ba` ; `c280a60e1483fa02f09ef494ced048f01517f92c6afb02a122659616696c0257` |
| `travail/sortie-suite-v3.txt` (258 passed) | `7e8b442747d6028bcb7cca88837adaac0a7921f62cda3be6132fa0e4da3b032d` |
| `travail/sortie-tests-variable-v3.txt` (quatre réglages) | `744d6643db1b9df3a304a69d40596540b4280b21f1703b2d20972a0fcba2b053` |
| `travail/sortie-epreuve-garde-table-v3-v1.json` ; `travail/sortie-h10-retour-chariot-v1.txt` | `0c61e93eabea11f0cd1e5e7c59ed5a5ac66c81a944ee91838bffbcce0f246358` ; `c404448ce64c98b7abefca8fe147702307dbfd5b489f6aca5777e0fd38a0fb60` |
| `travail/sortie-differentiel-ast-v2-v3.json` | `26e5054b60441b4120c388a7d5c8788b160a9e34015a3b18fe12b03fb4955410` |
| `travail/sortie-comptes-ancres-v1.json` ; `…-corrigees-v2.json` | `79f17e60b134ea8ec798738b50a316255243a2b903df3127ac7b371c40809fb3` ; `e56db6087b0dbbf33811be0a5131f6641c53cee446938c0409eb21fce2220687` |
| `travail/sortie-simulation-candidat2-v3-v1.json` ; `…-corrigees-v2.json` | `2c1369a4db96914867d26c54c62875c3c275589b4cfd9ee95d5271468591ec86` ; `ac99d13ce4e1bd990fbfdee86bc6e2111b408fa6b7ecd12ed124e50e9bd75a91` |
| `travail/paires-texte-module-v3-corrigees-vm3-v2.json` (à utiliser) | `324c164fd1cd2d9c654ec8b0ed120ed2cca90a224151652c3467e0640574ba7a` |
| `travail/sortie-tests-variable-simulation-v1.txt` ; `…-corrigee-v2.txt` (7 passed chacun) | `d16afaab1423f38a7d26cfc086764ca7c1e1e983eb3b48ffb35fbb6a1d591838` ; `8b9fe01f444fda1c0399cec46fda3e59ecd6604dc805a51b35d52b9e268ddb06` |
| `travail/simulation/simulation-candidat2-module-v3-NON-CANDIDAT-v1.md` ; `…-paires-corrigees-NON-CANDIDAT-v2.md` (simulations, pas des candidats) | `77b859d17d78dcdd4604ab57906ce9b96102e3a72d3727035bb5a73293b4ba1e` ; `8f0af6a45364367d696696b2967876140bca5886c3307f67369663792ef36a93` |
| `travail/git-status-avant.txt`, `…-apres.txt` (vides) ; `git-tete-*.txt` (`a82dac7`) ; `pycache-src-*.txt` (égaux) | `e3b0c442…` ; `492002b6…` ; `115163b0…` |

Versions de travail gardées (R12) : `paires-texte-module-v3-corrigees-vm3-v1.json` et ses sorties `…-v1`. Différentiels
`travail/diff-*.txt`, identifiants `travail/ids-*.txt`, copies `travail/copie-v2/`, `travail/copie-v3/` (sceaux
d'origine). Dossiers jetables : `travail/tmp-*`.
