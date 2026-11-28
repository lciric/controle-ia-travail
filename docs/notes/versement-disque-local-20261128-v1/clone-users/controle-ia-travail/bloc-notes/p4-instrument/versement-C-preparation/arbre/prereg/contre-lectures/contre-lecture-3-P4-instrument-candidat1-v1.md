# Contre-lecture 3 (R2) de P4-instrument, candidat 1 — v1

Texte relu : `…/p4-instrument/P4-instrument-v1-candidat1.md`,
`6422fb45a1dc2a3b42a5f6adad4ed8ff02cf89b3c09d91474213c5c1f5fe3bc0` (sceau compagnon égal). Le préfixe `…/` vaut
`/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad`.

## Verdict

**Scellable après corrections.** Un constat majeur, cinq mineurs, sept de forme. Aucun ne touche l'hypothèse, la
métrique décisive, le seuil ni la table de lecture dans leur logique.

- Les trois majeurs et les dix mineurs de la contre-lecture 2 sont traités. Aucune régression des onze constats de la
  contre-lecture 1.
- La décision R-284 est fondée sur des propriétés des entrées. Le script des mesures ne lit aucune colonne de score.
  La liste des 38 épisodes est la même partout : texte, configuration, sortie de MC-2, constante du module, même ordre.
- Le module applique le texte. Les 194 tests passent. Un écart réel : une lecture lancée sans `--prereg` lit un run
  décisif sans aucune garde, donc avant le verdict complété de P3 (CL3-01, démontré sur le modèle jouet).
- Validateur `controle_ia.prereg.problemes` : aucun point. Aucun chiffre de l'état de l'art.

## Cadre

- Contre-lecteur : sous-agent neuf. Je n'ai écrit ni aucune version de ce préenregistrement, ni le module, ni aucune
  vérification antérieure, ni P3, ni le brainstorm, ni l'addendum 2.
- Empreintes vérifiées (fichier et compagnon `.sha256`, égaux) : candidat 1 `6422fb45…` ; brouillon 4 `32d821fb…` ;
  contre-lecture 2 `9c94c220…` ; son traitement `53e7c0f2…` ; contre-lecture 1 `108a8d1f…` ; son traitement `876d1a66…` ;
  plan v2 `7c65e4f6…` ; les sept fichiers du module (`6e0e026e…`, `51a25e30…`, `483b8ac3…`, `9d015be4…`, `49441971…`,
  `f4f97029…`, `NOTES-MODULE.md` `7a82f3b7…`) ; mesures `1454d084…` et `33ee8659…`.
- Configuration `…/p4-instrument/P4-instrument-config-v1.json` : empreinte canonique (`manifeste.config_canonique`)
  `7905a18a228e2cbaf3220ce50950c9100e101e69d6a61e0a04eee5e3fb96e0c5`, égale à la citation ; égale à
  `config_de_reference(« a tall », « an urban »)` ; `exiger_config_p4` la dit conforme. Empreinte brute du fichier :
  `76d10700…` ; pas encore de compagnon `.sha256` (il viendra au scellement S, sous `prereg/`).
- Registre des décisions : lignes R-282, R-284 et R-287 seulement.
- Dépôt lu en lecture seule (commit `43cd3ac`). `git status --porcelain` vide avant et après ; aucun fichier neuf dans le
  dépôt. Python lancé avec `-B`, `PYTHONDONTWRITEBYTECODE=1`, `-p no:cacheprovider`.
- Non lus : `prereg/P3-consignes-v1.md`, tout fichier `textes-actions-*`, rien sous `donnees/`, la chaîne (`…/chaine/`),
  `registres/go.md`, `registres/depenses.md`, `diag/…/lecture-p3.json`. Aucune commande Vast.ai, aucun réseau.
- Écrit : seulement sous `…/p4-instrument/contre-lecture-3/`.

## (a) Traitement des contre-lectures 1 et 2

Différentiel mot à mot du brouillon 4 au candidat 1 : `diff-b4-c1-mots.txt`. Chaque changement se rattache à R-284,
aux résultats des mesures, aux empreintes du module ou aux onze « Précisions d'application ». Rien d'autre n'a changé.

| constat | traité dans le candidat ? |
|---|---|
| VP3-01 | oui : en-tête « GO et dépense » (l. 56-76) ; plan, point 7 ; liste d'arrêt (l. 700-706). Code : `controler_go`, `controler_accord`, `rejouer_garde_de_calcul`. Registre des GO non relu ici (hors de ma liste). |
| VP3-02 | oui : identifiant 220 inséré après `<|end_header_id|>` et 271 (l. 555-563) ; garde « un identifiant de plus, à chaque pas » ; tests. Code conforme (`position_de_l_espace`, `decalage_d_un_identifiant`). |
| VP3-03 | oui : « au-dessous » sur le quantile 0,05 ; « symétrique » retiré ; miroir 0,20 ; part étalée en descriptif. Code conforme. |
| VP3-04 | oui : règle unique (l. 420-430) ; table L6 à L10 ; réserves (l. 651-652). |
| VP3-05 | oui (l. 110-119 ; a priori interne l. 277-279). |
| VP3-06 | oui : L1 et L3 complétées ; report écrit (l. 480-482, 634-635). |
| VP3-07 | oui : B′ « urban », « indoor », « outdoor » ; liste d'arrêt (l. 694-695). |
| VP3-08 | oui : 403 sur 424 ; test 402 contre 403. |
| VP3-09 | oui : forme exacte « **Verdict complété de P3 scellé** » et empreinte du sceau ; tests. |
| VP3-10 | oui sur le plan v1. Le plan v2 est dit « aligné sur ce texte » : il précède R-284 et s'en tait (CL3-10). |
| VP3-11 | oui. Un nombre diverge de la contre-lecture 2 (0,5118 contre 0,5117 ; CL3-13). |
| VP3-12 | oui (l. 53-54, 174-179, 607-608). |
| VP3-13 | oui (l. 498-501 ; P4-C1). |
| RP-01 à RP-11 | aucune régression. RP-09 : les mentions « à relire au candidat » sont restées (CL3-08). |

Erreurs neuves introduites par les traitements : CL3-02 (reste de 60 actions au pas 0), CL3-03 (table du code non
alignée sur L1 et L4 neuves), CL3-05 (portée de la réserve de l'épreuve après R-284).

## (b) Décision R-284

- **Fondement.** `mesures_conception_p4_v1.py` appelle `charger_actions_p3(…, noms_legeres=None, avec_bornes=False)` :
  aucune colonne `scores` n'est lue, aucune aire, aucun score. La sortie ne porte que longueurs, empreintes et présence
  du jeton de fin. Choix fait sans score lu ni signe visé : R1 et R3 tenues.
- **Nombres recalculés** sur la sortie `1454d084…` : 38 épisodes égaux sur 60 ; 32 échecs de longueur, tous hors du
  niveau 1 ; dans les 22 autres épisodes, 4 sans échec de longueur et 97 actions de même longueur après un premier
  écart ; jeton de fin présent 557, absent 43 ; MC-1 : D, H, B, B′ à 14 jetons seules et dans le gabarit, 600 pas égaux,
  insertions pures, « a left-handed » à 15. Tout est exact.
- **Liste des 38.** La clé `taches_niveau_1` est dans la configuration, pas dans la sortie des mesures ; dans la
  sortie, la liste se lit par `MC-2.par_tache[*].egal`. Texte (l. 191), configuration, sortie de MC-2 et
  `instrument.TACHES_NIVEAU_1` : égaux, même ordre. Contrôle de reproduction : seule la clé
  `module_sha256.instrument_p4_v1.py` diffère entre v1 et v2.
- **Cohérence dans le texte.** Hypothèse (380 actions, 38 épisodes), Prédiction (P4-I, P4-C1, P4-D), Métrique (C1,
  760 lignes, 38 blocs ; M6a ; M6b ; C1 étendu), Seuil (garde d'identité), Plan (points 4, 5, 6, 8), Garde d'identité
  (niveau 1, « Seuil (R-284) »), Liste d'arrêt (deux lignes neuves), Critères (L4) : cohérents. Trois restes : CL3-02,
  CL3-05, CL3-12.
- **Population.** Les 38 épisodes ne sont pas un tirage au hasard des 60 ; le texte ne le dit pas (CL3-06).
- **Puissance.** √(60/38) ≈ 1,257 ; 0,0194 × 1,257 ≈ 0,0244 ; 2,80 × 0,0244 ≈ 0,068 ; 0,64 à 0,66 et 0,87 : justes.

## (c) Fidélité du module

Tests, depuis le dépôt, sur une copie du module dans `…/contre-lecture-3/travail/module/` (imports par le dossier du
fichier, comme le dit `NOTES-MODULE.md`) :
`PYTHONPATH=src PYTHONDONTWRITEBYTECODE=1 …/venv-gpu-neuf/bin/python -B -m pytest -q -p no:cacheprovider` sur les trois
fichiers : **194 passed in 141.54s** (71, 42, 81 ; chaque fichier vérifie son compte). Sortie :
`travail/sortie-tests-module.txt`.

| point du texte | code | conforme |
|---|---|---|
| 200 directions du plancher | `charger_sources_p3` (exactement `n_plancher` = 200, préfixe du nom) ; `plancher_de` | oui |
| quantiles 0,95 et 0,05, interpolation linéaire | `plancher_de` (`numpy.quantile`, défaut linéaire) ; contrôle croisé avec `detection_etiquettes` | oui |
| « au-dessus » strict, « au-dessous » strict, exclusifs | `etat_contre_le_plancher` | oui |
| plancher haut (> 0,80 ; < 0,20 ; médiane hors de [0,45 ; 0,55], bornes incluses dans l'intervalle) | `est_plancher_haut` | oui |
| critère (c) : deux principales et au moins 403 des 424, \|s4 − s3\| ≤ 0,05 (1 + \|s3\|) | `critere_c` | oui |
| épreuve (i) : 220 après 271 après `<|end_header_id|>` ; garde par pas | `position_de_l_espace`, `decalage_d_un_identifiant`, `_epreuve` | oui |
| épreuve (ii) : deux actions échangées en échec ; action sans score | `_epreuve` l. 1433-1436 | plus strict que le texte (CL3-04) |
| M5 : reconstruction, garde (120, 409, 7 faits, 2 000 lignes, 24 aires à 0,005) | `reconstruire_validation`, `exiger_aires_validation` ; `GardeM5` → L2 | oui |
| M6a : séparation repliée par tirage ; plancher des séparations repliées | `separation_par_blocs`, `_separations_du_plancher` | oui |
| M6b : mêmes tâches pour les deux jeux ; borne basse > 0 | `difference_aire_separation` | oui |
| intervalle par blocs, 2 000 tirages, 95 %, plus de 1 % dégénérés : échec | `intervalle_blocs` (gelé, 0,01) ; config | oui |
| graines dérivées, neuf clés | `CLES_LECTURE` ; `graine_entiere` ; manifeste | oui |
| lignes décisives : niveau 1 ; C1 étendu descriptif | `_retenues`, `lignes_du_bras`, `lire_c1(…, ETENDU)` | oui |
| liste du niveau 1 : texte, configuration, MC-2 ; tâche hors de P3 ; L4 | `exiger_taches_niveau_1`, l. 1197-1199, `comparer_niveau_1`, `issue_p4` | oui |
| tokeniseur du modèle chargé à `79e3e522…` | `exiger_tokeniseur_du_modele` | oui |
| audit R4 (seuils, part égale, grandeurs) | `audit_r4` | oui |
| table L1 à L11 | `issue_p4` (logique conforme) ; `LIGNES` (textes L1 et L4 non alignés, CL3-03) | logique oui |
| lecture refusée avant le verdict complété de P3 | `exiger_verdict_complete_p3` en mode décisif seulement | **non** hors du mode décisif (CL3-01) |
| aucune moyenne ni médiane sur les jetons | `exiger_agregation_maximum` ; familles gelées : maximum ou attention | oui |

Autres contrôles : les six lignes « Module de P4 » du candidat se lisent par `lignes_module`, toutes à l'empreinte des
fichiers ; `exiger_citations_p4` relit la configuration et l'entropie citées ; `borne_de_l_etape()` = 5,41.

## (d) Validateur, contradictions, R6, R7

- `controle_ia.prereg.problemes` sur le candidat : `[]`.
- R7 : aucun chiffre de l'état de l'art (l. 262 le dit ; 0,70 à 0,95 est une estimation de séance, déclarée).
- R6 : deux nombres sans chemin complet ou sans dérivation écrite (CL3-09) ; un nombre en désaccord avec la
  contre-lecture 2 (CL3-13).

## Constats (le plus grave d'abord)

### CL3-01 — majeur — une lecture sans `--prereg` lit un run décisif avant le verdict complété de P3

- **Où** : `lecture_p4_v1.py` l. 732-767 (`analyser`) et l. 216-248 (`charger_source_p4`) ; texte, plan d'analyse,
  point 2 (l. 473-482), liste d'arrêt (l. 708-709).
- **Preuve** :
  - toutes les gardes du mode décisif, verdict complété de P3 compris, sont sous `if prereg is not None` (l. 742-750) ;
  - sans `--prereg`, `charger_source_p4` et `lire` lisent le run, sans regarder si son manifeste est décisif ni s'il
    est en mode réel ;
  - démonstration sur le modèle jouet (`travail/module/test_demo_cl3_lecture_non_decisive.py`, sortie
    `travail/sortie-demo-cl3-01.txt`) : run décisif jouet, aucun verdict complété versé. Lecture décisive : refusée,
    rien d'écrit. Même run, sans `--prereg` : lu, `lecture-p4.json` écrit, « C1 calculé : True ; aire C1 : 0.5556 » ;
  - côté run, `executer` refuse un run réel sans préenregistrement (l. 1155-1156) ; la lecture n'a pas la garde
    symétrique ;
  - le texte ne prévoit pas de lecture non décisive. Le code fait plus que le texte, et la garde voulue par R-262
    se contourne en omettant un argument (R5 : aucun repli silencieux).
- **Correction** :
  - code, dans `analyser`, avant `creer_manifeste` : si `prereg is None` et que le manifeste du run source est décisif
    ou porte `config.mode == "reel"`, lever `GardeArret("lecture sans préenregistrement d'un run décisif ou réel :
    refusée sans rien écrire")` ;
  - tests : cas sain (run jouet non décisif lu sans `--prereg`) ; artefact (run décisif jouet lu sans `--prereg` :
    refus, aucun dossier `diag/<run de lecture>/`) ;
  - texte, liste d'arrêt, ligne l. 708-709 :
    « Lecture demandée avant le scellement du verdict complété de P3 (addendum 2), ou avant le scellement de ce texte :
    refusée sans rien écrire et reportée (pas une ligne). »
    → « Lecture demandée avant le scellement du verdict complété de P3 (addendum 2), ou avant le scellement de ce texte,
    ou sans `--prereg` sur un run source décisif ou en mode réel : refusée sans rien écrire et reportée (pas une
    ligne). » ;
  - texte, « Tests (R5) » : ajouter « lecture sans `--prereg` d'un run décisif (doit refuser sans rien écrire) » ;
  - puis nouvelles empreintes des fichiers changés dans les lignes « Module de P4 », et « Tests attendus » remis à jour.

### CL3-02 — mineur — C1 au pas 0 garde « 60 par bras »

- **Où** : l. 392-393 (descriptives). Le code lit le pas 0 sur le niveau 1 (`lire_c1(…, pas=0)`, jeu par défaut
  `niveau_1`), comme R-284 le veut.
- **Correction** : « sur les seules actions du pas 0 (60 par bras au plus ; » → « sur les seules actions du pas 0 des
  épisodes du niveau 1 (38 par bras au plus ; ».

### CL3-03 — mineur — la table du code n'est plus celle du texte pour L1 et L4

- **Où** : `lecture_p4_v1.py` l. 62-75 (`LIGNES`, commentaire « mot pour mot ») ; texte l. 639 et l. 642.
- **Preuve** (comparaison automatique des cellules) :
  - L1, issue : le texte ajoute « , ou refusé avant son manifeste : « manifeste absent » » ;
  - L4, issue : le texte ajoute « (ensemble des épisodes au niveau 1 autre que la liste de l'en-tête ; motif : tâches en
    plus et tâches absentes) » ;
  - L4, lecture : texte « non lu ; C1, M6 et descriptives non calculés ; M5 lue ; nœud » ; code « non lu ; nœud ».
  - La logique de `issue_p4` est conforme ; seuls les textes écrits dans `lecture-p4.json` diffèrent.
- **Correction** : recopier dans `LIGNES` les cellules L1 et L4 du texte, mot pour mot ; ajouter un test qui compare
  `LIGNES` à la table du préenregistrement cité. Mettre à jour les docstrings « Texte : brouillon 4 (`32d821fb…`) »
  (`lecture_p4_v1.py` l. 2, `instrument_p4_v1.py` l. 3, commentaire l. 62) vers le préenregistrement scellé.

### CL3-04 — mineur — épreuve (ii) : le code est plus strict que le texte

- **Où** : `instrument_p4_v1.py` l. 1433-1436 ; texte l. 564-566 et précision 2 (l. 661-662).
- **Preuve** : si l'une des deux actions échangées n'a pas de score (dans P3 ou dans P4), le code met tout l'échange à
  « sans action comparable », donc « contre l'attendu », même si l'autre est comparable. Le texte dit que « les actions
  sans score ne sont pas comparées ». Effet limité : seul « C1 étendu » en dépend après R-284. MC-3 ne montre aucune
  action à empan vide (`jetons_notes` > 0 partout), donc le cas est peu probable.
- **Correction** (texte, sans toucher le code) : « (ii) texte de l'action du pas 1 échangé avec celui du pas 2 : les deux
  actions échangées doivent échouer (c) ; les actions sans score ne sont pas comparées, et une épreuve sans aucune action
  comparable se lit « contre l'attendu ». » → « (ii) texte de l'action du pas 1 échangé avec celui du pas 2 : les deux
  actions échangées doivent échouer (c) ; si l'une des deux n'a pas de score, dans P3 ou dans P4, l'épreuve (ii) se lit
  « contre l'attendu ». En (i), les actions sans score ne sont pas comparées, et un décalage sans aucune action
  comparable se lit « contre l'attendu ». » Même retouche à la précision 2.

### CL3-05 — mineur — la réserve de l'épreuve garde sa place sur la ligne décisive, alors qu'elle ne touche plus C1

- **Où** : texte l. 567-570, l. 574-576 (« sans ligne ni réserve »), l. 651-656 (réserves) ; code `issue_p4` l. 665-666.
- **Preuve** : après R-284, le niveau 2 et l'épreuve ne servent qu'à « C1 étendu ». La réserve « tolérance (c) non
  éprouvée sur le modèle réel » s'écrit pourtant avec la ligne, à côté de C1. Un verdict R13 peut la lire comme une
  réserve sur C1.
- **Correction** (texte seul ; la chaîne de la réserve dans le code reste) : dans « Réserves », « tolérance (c) non
  éprouvée sur le modèle réel ; » → « tolérance (c) non éprouvée sur le modèle réel (elle ne porte que sur le descriptif
  « C1 étendu » ; ni C1 ni M6 n'en dépendent) ; ».

### CL3-06 — mineur — la population des 38 épisodes n'est pas déclarée

- **Où** : section « Décision de conception après les mesures (R-284) » (l. 196-210) ; Hypothèse, « Ce que H-P4
  n'affirme pas » (l. 230-240).
- **Preuve** (propriétés des entrées, sortie `1454d084…`, `MC-3.par_action` ; aucun score) :
  - actions sans jeton de fin : 10 sur 380 au niveau 1, contre 33 sur 220 ailleurs ;
  - jetons notés de P3 : médiane 205 contre 222,5 ; 90e centile 266 contre 400.
  - Les épisodes reproduits à l'identique ont moins d'actions coupées et des actions plus courtes. C1 vaut pour eux.
- **Correction** : ajouter à la section R-284 et à « Ce que H-P4 n'affirme pas » : « un succès ou un échec de C1 vaut
  pour les 38 épisodes reproduits à l'identique, qui ne sont pas un tirage au hasard des 60 : moins d'actions sans
  jeton de fin (10 sur 380, contre 33 sur 220) et des actions plus courtes (90e centile des jetons notés : 266, contre
  400 ; `MC-3.par_action` de `docs/notes/P4-mesures-v1/mesures-conception-p4-v1.json`, `1454d084…`) ; « C1 étendu »
  n'en donne qu'un aperçu descriptif. »

### CL3-07 — forme — dates de l'en-tête dans le désordre

- **Où** : l. 19-21.
- **Correction** : « brouillon 3 le 2026-10-20 vers 11:00 UTC ; candidat 1 le 2026-10-20 vers 14:54 UTC ; brouillon 4
  le 2026-10-20 vers 13:49 UTC. » → « brouillon 3 le 2026-10-20 vers 11:00 UTC ; brouillon 4 le 2026-10-20 vers 13:49
  UTC ; candidat 1 le 2026-10-20 vers 14:54 UTC. »

### CL3-08 — forme — mentions « au candidat » périmées ; entrée de la contre-lecture 3 à écrire

- **Où** : l. 106-108 ; l. 734-735 ; l. 749-750 ; l. 754-759.
- **Correction** :
  - l. 106-108 : « (à relire et à recopier au candidat) » → « (à relire au scellement S) » ; « (huit colonnes après
    R-281 ; à relire au candidat) » → « (huit colonnes après R-281 ; à relire au scellement S) » ;
  - l. 734-735 et l. 749-750 : « avec leurs sceaux au candidat » → « avec leurs sceaux au scellement S » ;
  - l. 754-759 : remplacer l'entrée « Au candidat, vérification des corrections du brouillon 4 » par une entrée à la
    forme lue par le validateur : « **Contre-lecture 3, sur le candidat 1** :
    `…/p4-instrument/contre-lecture-3/contre-lecture-3-P4-instrument-candidat1-v1.md` (`<empreinte du rapport>`), sur le
    candidat 1 (`6422fb45a1dc2a3b42a5f6adad4ed8ff02cf89b3c09d91474213c5c1f5fe3bc0`), sous-agent neuf : « scellable après
    corrections », un majeur (CL3-01), cinq mineurs (CL3-02 à CL3-06), sept de forme (CL3-07 à CL3-13) ; traitement :
    `<chemin>` (`<empreinte>`). » Puis une entrée par relecture de la chaîne. Rapport et candidat 1 à verser sous
    `prereg/contre-lectures/` avec leurs sceaux.

### CL3-09 — forme — deux nombres sans empreinte complète ou sans dérivation écrite (R6)

- **Où** : l. 193 ; l. 198.
- **Correction** :
  - l. 193 : « (`33ee8659…`, R12) » → « (`33ee865997b78f7888f15ed14e0baab1e20b517f22d8f0b9de04c16f426aba28`, R12) » ;
  - l. 198 : « Dans les 22 épisodes hors niveau 1, 4 n'ont aucun échec de longueur et 97 actions de même longueur
    suivent un premier écart » → ajouter « (comptés sur `MC-2.par_tache` et `MC-3.par_action` de la sortie citée,
    `1454d084…`) ».

### CL3-10 — forme — le plan v2 n'est pas « aligné sur ce texte » pour R-284

- **Où** : l. 714 ; plan v2 (`7c65e4f6…`), écrit à 13:49 UTC, avant R-284. Il ne parle ni de la liste du niveau 1, ni de
  la nouvelle L4, ni de « C1 étendu », ni de l'empreinte du tokeniseur. Il ne contredit pas le texte.
- **Correction** : « plan v2 (`plan-code-et-chaine-v2.md`, R12), écrit avant le candidat et aligné sur ce texte » →
  « plan v2 (`plan-code-et-chaine-v2.md`, R12), écrit avant R-284 et aligné sur le brouillon 4 ; il se tait sur R-284,
  que ce texte et le module portent ; le texte prime ».

### CL3-11 — forme — précision 9 : « M5 en défaut » est ambigu

- **Où** : l. 671-672. Ailleurs, « garde de M5 en défaut » mène à L2 (arrêt), pas à L3.
- **Correction** : « quand M5 est déjà en défaut : L3 prime » → « quand M5 donne la ligne L3 (non au-dessus, ou lecture
  de M5 en échec) : L3 prime ».

### CL3-12 — forme — « lignes décisives et descriptives » sans l'exception de « C1 étendu »

- **Où** : l. 200-201.
- **Correction** : « **Lignes décisives et descriptives** : les actions des seuls épisodes au niveau 1, dans les cinq
  bras ; » → « **Lignes décisives et descriptives** (sauf « C1 étendu », ci-dessous, et M5, sur la validation) : les
  actions des seuls épisodes au niveau 1, dans les cinq bras ; ».

### CL3-13 — forme — plancher de mention contre honnête : 0,5118 ou 0,5117

- **Où** : l. 158 (« 0,5118 sur mention-honnete ») ; la contre-lecture 2 écrit 0,5117 (VP3-11, « déjà dans O2-02 »).
  Je n'ai pas lu `lecture-p3.json` (hors de ma liste).
- **Correction** : relire la clé
  `resultat.jeux.tromperie-difference_moyennes-c15.mention-honnete.plancher_quantile` de `lecture-p3.json`
  (`c221d955…`) et écrire sa valeur arrondie au plus proche, à quatre décimales. Aucun effet sur une ligne.

## Points vérifiés sans constat

- Arithmétique de la borne de l'étape (3,47 + 0,22 + 1,00 + 0,72 = 5,41) ; `borne_de_l_etape()` = 5,41 ; borne
  strictement inférieure à 10 USD partout (en-tête, liste d'arrêt, `controler_go`).
- Formes « Entropie », « Révision du modèle », « Configuration de P4 (empreinte canonique) » et les six lignes
  « Module de P4 » : lues par le module, empreintes égales.
- Règle des phrases rejouée sur l'instance ; B, B′ et toutes les candidates passent `exiger_concept_sans_affect`.
- Garde d'identité de la notation sur chaque bras et sur chaque concept de validation ; scores par jeton à 10⁻⁹.
- Réserves héritées de P3 : un pointeur, conforme à la précision 8.
- Ordre de la table : L3 avant L4 (précision 9) ; « plancher haut » seulement en L6 à L9 ; aucune en L1 à L5.
- Comparaisons contre un plancher : huit, dans le texte et dans `COMPARAISONS`.

## Non vérifié ici (à d'autres relecteurs ou à la session)

- La chaîne de lancement, le registre des GO, le registre des dépenses, la suite des 908 tests du dépôt.
- L'empreinte brute et le sceau de la configuration une fois versée sous `prereg/` (au scellement S).

## Pièces

Sous `…/p4-instrument/contre-lecture-3/` :

| pièce | sha256 |
|---|---|
| `diff-b4-c1-mots.txt` (brouillon 4 → candidat 1, `git diff --no-index --word-diff`, hors du dépôt) | `677c4db728f64af829bea6d25ba7e16e5af9ba0e1598ac38d7181ad10eb2b1e9` |
| `travail/sortie-tests-module.txt` (194 passés) | `a89e3aaaae35315c2a39f8898a2514865079db52fa751ab05ea58f6a82ba0d45` |
| `travail/module/test_demo_cl3_lecture_non_decisive.py` (démonstration de CL3-01, modèle jouet) | `0e1dcdcc30256eee3aa5e7f33d59d3c4d4125a4f5ccd16914c6ac2a1129f1ac6` |
| `travail/sortie-demo-cl3-01.txt` | `792659c00bd25a6b82e3f004d8fa3b7139a551231f2e494b026fa96428498955` |

`travail/module/` contient aussi une copie, non modifiée, des six fichiers du module (empreintes égales à celles du
candidat).
