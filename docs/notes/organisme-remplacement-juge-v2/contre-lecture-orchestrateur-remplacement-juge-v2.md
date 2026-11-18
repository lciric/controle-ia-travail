# Contre-lecture — orchestrateur de l'organisme d'idéation, version 2 du remplacement déclaré du modèle d'un juge externe (étiquette répétée refusée)

- **Date** (temps universel, `date -u`) : 2026-11-18T18:21:25Z (début de la contre-lecture 2026-11-18T17:50:06Z ; fin de la dernière suite 18:20:45Z).
- **Contre-lecteur : modèle K**, agent neuf. Je n'ai écrit aucune des pièces relues (module v2, essais, banc de mutations, lanceurs neufs, rapport du développeur, écrits par le modèle L'), ni la version 1, ni sa contre-lecture, ni la demande de la relance, ni `pole/ideation_v2.py`.
- **Objet** : branche `prep/orchestrateur-remplacement-juge-compte-organisme-v1`, commit `3218f4605ac64b634cdab8bd03a1029758b0566b` (parent `3b283d48819229418e9f97b9d7c5688452a924f6`), dossier `docs/notes/organisme-remplacement-juge-v2/` : `git diff --name-status 3b283d48 3218f460` donne **20 lignes A** (10 pièces et leurs compagnons `.sha256`), aucune M, aucune D ; garde des secrets sur ce différentiel : 0.
- **Hors ligne** : aucune dépense, aucun appel réseau, aucun relais, aucun lanceur en mode réel ; rien installé ; aucune variable d'environnement lue ni affichée (les lanceurs joués par la ligne de commande reçoivent l'environnement explicite `{"PATH": "/usr/bin:/bin"}`) ; rien lu ni écrit sous `diag/`, `runs/`, `donnees/`, `registres/`, `docs/notes/bras-attaque/` ; rien écrit dans `/home/user/ideation-organism` (tête restée `a41b7b50f7c64ce488c120bb89ad3d25fb1dd1cb`, arbre propre, vérifié avant et après) ; deux clones locaux neufs à poussée neutralisée (`git remote set-url --push origin DISABLED-no-push`, vérifié par `git remote -v`) : `/home/user/orch-relecture-remplacement-juge-v2` (tête du paquet) et `/home/user/orch-relecture-base-0861800-v2` (détaché sur la base `0861800`), jamais poussés ; rien vers `lciric/ideation-organism`.
- **Refus rapportés** : la garde d'isolement de l'arbre de travail a refusé trois commandes de ma part (deux commandes composées enchaînant `cd` et `git`, un `git clone` lancé depuis `/home/user`) en demandant des commandes simples lancées depuis mon arbre ; je les ai découpées sans en changer l'effet. Aucun refus de permission ni de classifieur. Aucun heredoc : mes scripts (sondes, mutations, suites) sont des fichiers écrits par l'outil d'écriture dans mon bloc-notes, non livrés.

## 1. Empreintes vérifiées (calculées par moi ; égales à celles du rapport du développeur et du bloc gelé provisoire)

Les dix pièces du dossier ont leur compagnon `.sha256` ; `controle_ia.scellement verifier` sur les dix : toutes `OK`.

| pièce | sha256 |
|---|---|
| **paquet** `orchestrateur-remplacement-juge-v2.bundle` | `1c5a5bd2e97c26c515927f8c1d4519e1b1c94367ee03abb4186eb7aa697d5262` |
| **module v2** `orchestrator/pole/bras_remplacement_juge_v2.py` (86 lignes, lu dans la tête du paquet) | `83a08aeeeba694f72e0aceb004c9432c4c57427072ed37208181903f30433ee2` |
| **différentiel** `orchestrateur-remplacement-juge-v2-contre-0861800.diff` (recalculé par `git diff 0861800 8a2a6ac` : identique octet pour octet) | `095fe1cbe2c2e29b19b718c0d89b17677d0e62d5e20bced54dad2b3d927f059c` |
| **spécification** `docs/notes/relance-organismes-discrets-v1/demande-orchestrateur-remplacement-modele-juge-v1.md` (branche `claude/pensive-bardeen-1fv7hw`, tête `630c6c74`, lue par `git show`) | `2ddb1117e77820ebfaa6a84133cc03c140d262b3765c5960fcbdb8bc091fe136` |
| `rapport-developpeur-remplacement-juge-v2.md` | `6ac2e13f45621d098bfe570ceaf89daef63fac682635a13ca65768f3e10bac96` |
| `empreintes-orchestrateur-remplacement-juge-v2.txt` (bloc gelé provisoire) | `3108dac01deea3d655f723923cd9f5378b5fa138da178359aa73955c22061efe` |
| `ecarts-portage-essais-et-banc-v1-v2.diff` (recalculé par `diff -u` des essais v1/v2 et des bancs v1/v2 : mêmes lignes ajoutées et retirées, 431 ; seuls les en-têtes de `diff` différent) | `6fa4fd3584c987b0bc569ef3d82d69d7ef50946484348fe8a8a0c7ed812bb7b3` |
| `essais-remplacement-juge-v2.txt` | `453e90c4288e8a6ba682527fc218bc6eb90f505b01d472d4047dc2977f87dc19` |
| `mutations-remplacement-juge-v2.json` / `.txt` | `4d226f0bccc41d968b358c0d49a7235d27b74621e6707a5b7437671210cfa2a2` / `9f42795007cbfae7a964f3199b77555be2c8c99f0d6629cf3376b692b10d8401` |
| `suite-orchestrateur-remplacement-juge-v2.txt` / `suite-base-0861800-remplacement-juge-v2.txt` | `43c8182978655dfb8d266c44cbe92325712d6bce555f0473167d43d648928582` / `b0ac4b4950a4d3367848cb7683b137245ecba60ca9dad5ca78c8ef548154c5c6` |

Orchestrateur, dans mon clone neuf de la copie en lecture seule :

| objet | valeur |
|---|---|
| `git bundle verify` | « is okay » ; une référence `refs/heads/prep-remplacement-juge-v2 → 8a2a6ac9d3feb52e6771edca52f440dd780fb373` ; prérequis `a41b7b50f7c64ce488c120bb89ad3d25fb1dd1cb` (= `origin/main` de la copie, arbre `orchestrator/` `ee84d6eca7a4c9b25f4e297ca29c6d9f24af5d70`) |
| tête du paquet | `8a2a6ac9…`, parent `0861800260e33224a71f48b111e72ac04288d3cb` (v1), lui-même fils de `a41b7b50…` : le paquet porte bien les deux commits |
| arbres à la tête | `orchestrator/` **`71417ad17d816af07a6a57e9dc28bbfac07faac5`** ; `orchestrator/pole` **`bfd8585661fdcce6157bc5287f86e2371ea254b3`** |
| `git diff --name-status 0861800 8a2a6ac` | exactement **cinq lignes A** : `pole/bras_remplacement_juge_v2.py`, `essais/test_bras_remplacement_juge_v2.py`, `essais/mutations_bras_remplacement_juge_v2.py`, `demonstrations/ideation_v2_juges_externes_uniques_v1.py`, `demonstrations/ideation_v1_juges_externes_uniques_v1.py` ; aucune M, aucune D |
| `git diff --name-status a41b7b50 8a2a6ac` | **huit lignes A** (les trois de la v1, les cinq de la v2) ; `git diff a41b7b50 0861800` recalculé : `b45a0b87…`, le différentiel de la livraison v1, inchangé |
| garde des secrets sur `git diff 0861800 8a2a6ac` | 0 |
| fichiers neufs | `test_bras_remplacement_juge_v2.py` (729 l.) `d0ae81de887f1bbd13918c3210ac12113126f6ea7c6f69ca5e392dbc0e8a10be` ; `mutations_bras_remplacement_juge_v2.py` (115 l.) `57f427a5c661190dd769210addea8fc8b31c3f67907dbfd147cced1c3b5e2499` ; `ideation_v2_juges_externes_uniques_v1.py` (50 l.) `1fbe2be3cab8e843daaecd8547beee05e2948f0e11bdbb9dc1ffacdce4ee7682` ; `ideation_v1_juges_externes_uniques_v1.py` (49 l.) `3b471029171dc1e86f700aa55c3058179fbe93b45357e26d06efb903ac08d00d` |
| fichiers existants, même empreinte à `0861800` et à `8a2a6ac` (`git diff --stat` vide) | `pole/bras_remplacement_juge_v1.py` `2efd6b0874e8bbfa58a0c53a5099f46da51318c6807c90909b8cf58dfe90866a` ; `pole/ideation_v2.py` `67d2ad3591b21601ece4101154138f532ba519024761beb8c9738181f8f3fefc` ; `pole/ideation.py` `4ee70d25567a9b3ac90911cc5ebee8cebba0537d541e7a0ebc1fa3ed170abdc2` ; `demonstrations/ideation_v2.py` `bc5e9c98acff41b97487e2345d33768c8cdf41f0ededf8b2eed0bf842c889845` ; `demonstrations/ideation_v1.py` `855a1139f5fb8463699fad22c3725fc0f630488186add94f1da909b12bccf17e` ; essais et banc de la v1 `1e5f39d8…`, `cdd021c6…` |

Les deux lanceurs neufs ne différent entre eux que par la cible chargée (`ideation_v2.py` / `ideation_v1.py`), le nom du module et la docstring (`diff` lu ligne à ligne) ; le module v2 réexporte l'API de la v1 (mêmes objets, essai `test_api_de_la_version_1_reexportee`).

## 2. Décomptes (rejoués par moi ; interpréteur `/usr/local/bin/python3` 3.13.18, pytest 9.1.1, `-B`, `PYTHONDONTWRITEBYTECODE=1`, `-p no:cacheprovider`)

| essai | mon résultat | développeur |
|---|---|---|
| `essais/test_bras_remplacement_juge_v2.py` seul, tête `8a2a6ac` (`-q -rs`) | **34 passed, 43 subtests passed in 3.12s** | 34 passed, 43 subtests passed in 3.65s — égal |
| banc `essais/mutations_bras_remplacement_juge_v2.py --processus 4` (17:53:59Z → 17:54:34Z) | **28 tuées pour la raison attendue sur 28**, code 0 ; par origine : v1 porté 17/17, porté sur la v2 1/1, neuves 10/10 ; décomptes `failed/passed/subtests` **identiques mutation par mutation** à `mutations-remplacement-juge-v2.txt` (durées à part) | 28/28 — égal |
| suite complète `essais/`, tête `8a2a6ac` (`-q -rfEs --continue-on-collection-errors`), clone de relecture, 17:59:22Z → 18:10:17Z | **7 failed, 1408 passed, 5 skipped, 14 errors, 1275 subtests passed in 653.87s** | 7 failed, 1408 passed, 5 skipped, 14 errors, 1275 subtests passed — égal |
| suite complète, base `0861800`, second clone, jouée **après** la tête (18:10:17Z → 18:20:45Z), jamais en même temps | **7 failed, 1374 passed, 5 skipped, 14 errors, 1232 subtests passed in 627.51s** | 7 failed, 1374 passed, 5 skipped, 14 errors, 1232 subtests passed — égal |

1408 − 1374 = 34 essais et 1275 − 1232 = 43 sous-essais : exactement ceux de `test_bras_remplacement_juge_v2.py`. Mes listes `FAILED`, `ERROR` et `SKIPPED` (26 lignes) sont identiques entre la tête et la base, et identiques à celles des deux sorties livrées (comparées ligne à ligne après retrait des messages, `diff` vide) : **aucun échec neuf**, aucune erreur neuve, aucun saut neuf. Aucune passe n'a montré l'échec transitoire de `test_juges_idees_v2.py` vu une fois à la contre-lecture v1.

Les listes `FAILED`, `ERROR` et `SKIPPED` des deux sorties livrées par le développeur sont identiques entre elles (comparées ligne à ligne, `diff` vide) : les 7 échecs sont ceux déjà vus à la contre-lecture v1 (`TestV51.test_v51_10`, `test_v51_15`, `TestR12` v52b et v53, `TestR12V55` v54, `TestV49.test_v49_18`, `TestV50.test_v50_17` : fichiers d'archive absents de l'arbre public), les 14 erreurs sont `scipy` absent à la collecte (mêmes quatorze fichiers), les 5 sautés ont les mêmes motifs. Aucun ne touche le bras, le module v2 ni les lanceurs.

## 3. Mutations propres au contre-lecteur (machinerie du banc v66 chargée telle quelle, liste neuve de huit ; jugées par `essais/test_bras_remplacement_juge_v2.py` ; 17:58:51Z → 17:59:06Z, code 0)

| mutation | fichier muté | issue |
|---|---|---|
| K01 égalité remplacée par l'identité (`e == v` → `e is v`) | module v2 l. 58 | **tuée**, 7 échecs — **tous dans `TestLanceursNeufs`** (constat 1) |
| K02 mauvaise clé de réglages (`"juges_externes"` → `"juges_externe"` : garde muette) | module v2 l. 80 | tuée, 19 échecs |
| K03 refus seulement si deux étiquettes différentes sont répétées (`if repetees` → `if len(repetees) > 1`) | module v2 l. 69 | tuée, 20 échecs |
| K04 option perdue à la délégation (v1 appelée sans `remplacements_juges_externes`) | module v2 l. 83 | tuée, 33 échecs (`test_sain_remplacement_declare_admis` compris) |
| K05 seules les entrées voisines comparées (`e == vues[-1]`) | module v2 l. 58 | tuée, 2 échecs (cas à trois entrées `lx-juge, autre-juge, lx-juge`) |
| K06 lanceur v1 neuf : garde sur les modèles au lieu des étiquettes | lanceur v1 neuf l. 34 | tuée, 6 échecs |
| K07 lanceur v2 neuf : `return 2` à la place de `a.error(...)` | lanceur v2 neuf l. 43 | tuée, 5 échecs |
| K08 garde jouée **après** la délégation sans option (v2 appelée d'abord) | module v2 l. 80-82 | tuée, 9 échecs |

**8 tuées pour la raison attendue sur 8.** Chaque texte d'origine était présent une seule fois ; les essais sains passent sur la copie non mutée (vérification du banc).

## 4. Sondes du contre-lecteur (R5 : cas sains et artefacts, hors du fichier d'essais ; 13 sondes, toutes passées, 17:58:35Z → 17:58:39Z)

Au cœur (`pole.bras_remplacement_juge_v2.executer_bras_differe`, course simulée de `test_v7_ideation_v2.TestCourse`, adaptateur « espion » qui lève à **tout** accès d'attribut) :

| sonde | issue |
|---|---|
| k01 : sans option, `[(lx-juge, non déclaré, a), (lx-juge, course, b)]`, **attestation absente** | `CourseInterrompue` « étiquettes de juges externes en double » ; aucun accès à `a` ni `b` ; contenu du dossier de la course identique octet pour octet avant et après ; aucun manifeste du bras ni de tentative. Si le bras avait lu quoi que ce soit, l'erreur aurait été celle de l'attestation. |
| k02 : avec option (bien formée, référence de GO vide, `{"x": 1}`, chaîne), attestation absente | même refus pour les quatre formes ; rien lu, rien appelé, rien écrit |
| k03 : sans option, étiquettes **distinctes** mais l'une absente de la course | le module et `ideation_v2` lèvent la **même** exception CL35-04 (texte identique), sans mot « en double » : la v2 décide seule |
| k04 : témoin du défaut dans `ideation_v2.executer_bras_differe` gardée telle quelle | les deux juges joués ; le modèle **non déclaré** reçoit **deux** appels `juge_ideation` (contrôle puis juge) ; `EcrasementInterdit` ; `manifeste-bras-rapporte.json` écrit (verrou posé) |
| k05 : espion sur `ideation_v2.executer_bras_differe` | mêmes arguments reçus, avec `remplacements_juges_externes` absent ou `None` explicite |
| k06 : garde pure | étiquette répétée trois fois citée une fois ; `None` répété refusé ; `"a"` et `"a "` distincts (le cœur ne retire pas les blancs, le lanceur si) ; dictionnaire, chaîne : formes non inspectées (`[]`) ; étiquette de 500 caractères répétée : message tronqué |
| k07 : sans option, `juges_externes` donné en dictionnaire | la v2 échoue au dépaquetage (`ValueError`/`TypeError`) ; aucun accès à l'adaptateur ; rien écrit |
| k08 : lignes du défaut | `pole/ideation.py` l. 2847, `pole/ideation_v2.py` l. 2852, `pole/bras_remplacement_juge_v1.py` l. 255 : `donnes = {e: m for e, m, _ in juges_externes}` présent dans les trois |

Par la ligne de commande (`python -I -B`, environnement `{"PATH": "/usr/bin:/bin"}`, `--commande-externe /bin/false`, attestation absente, dossier de sortie absent) :

| sonde | issue |
|---|---|
| k10 : `ideation_v2_juges_externes_uniques_v1.py` et `ideation_v1_juges_externes_uniques_v1.py`, `--bras-rapporte-differe`, trois listes répétées (`astra-juge=…` deux fois ; `m1` puis `externe-1=m2` : étiquette par défaut ; blancs autour) | **code 2**, « error: --juge-externe : étiquettes de juges externes en double ["'astra-juge'"] … » (ou `'externe-1'`) sur la sortie d'erreur, sortie standard vide, dossier de sortie non créé — six cas |
| k11 : les deux lanceurs neufs en mode **course** (`--moteur simule`, sans bras), `a=m` et `a=m2` | code 2, même message, rien écrit : la garde vaut dans tous les modes |
| k12 : lanceurs **d'origine** `ideation_v2.py` et `ideation_v1.py`, même liste répétée | aucun mot « en double » : ils passent la lecture des arguments et échouent plus loin (`{"arret": "FileNotFoundError …"}`, code 2) — le défaut passait par là |
| k13 : lanceurs neufs, étiquettes **distinctes** | ils passent la main au lanceur d'origine : même code, même dernière ligne d'erreur, même sortie standard que le lanceur d'origine appelé directement |
| k14 : `ideation_v3.py` (juges seulement) | `pole/juges_seulement_v1.py` l. 185-186 : « étiquettes de juges en double » déjà refusé |

Autres lanceurs : seuls `demonstrations/ideation_v1.py`, `ideation_v2.py` et `ideation_v3.py` ont l'option `--juge-externe` (`grep` sur `demonstrations/`). La course elle-même refuse « étiquettes en double » pour tous les juges, externes compris (`ideation_v2.valider_etiquettes` l. 984-992, appelée l. 1489 et 1941 avec `tous_juges = juges + juges_externes`) : aucune course valide n'a deux juges externes de même étiquette, donc le refus neuf n'écarte aucun bras légitime (cela confirme la raison donnée au § 3 du rapport).

## 5. Ce que la relance demandait, point par point

| point | tenu | preuve |
|---|---|---|
| étiquette répétée refusée **avant toute lecture et tout appel**, **avec et sans option**, au cœur | oui | module v2 l. 80 : première instruction d'`executer_bras_differe`, avant les deux branches ; essais `TestEtiquetteRepeteeRefusee` (neuf essais, 0 appel compté), sondes k01, k02 (adaptateur espion : aucun accès ; attestation absente : l'erreur est celle de l'étiquette) ; mutations V01-V07 (développeur), K01-K03, K05, K08 (moi) tuées |
| … par toute ligne de commande concernée | oui | lanceurs neufs : sondes k10, k11 (code 2, rien écrit, tous modes) ; essais `TestLanceursNeufs` ; mutations V08-V10, K06, K07 tuées ; `ideation_v3` refusait déjà ; aucun autre lanceur n'a l'option |
| aucun autre changement de comportement sans option | oui | module v2 l. 81-82 : `ideation_v2.executer_bras_differe(sortie, **reglages)` elle-même ; sonde k05 (mêmes arguments), k03 (même exception CL35-04), essais v1 portés `test_sans_option_*` (sortie identique octet pour octet sur le cas fixe) ; mutation R10 portée tuée. **Seul écart** : la liste à étiquette répétée, refusée au lieu d'être jouée deux fois (le défaut même), déclaré par le développeur et sans bras légitime écarté (section 4) |
| remplacement déclaré dans **tous** les manifestes de tentative (`bras-tentative-N`, `manifeste-bras-non-joue-N`, `manifeste-bras-refus-taille-N`) | oui | v1 inchangée (journal l. 301, manifestes) ; essais neufs `TestManifestesDeTentative` (trois essais, passés chez moi) et essai v1 porté `test_refus_de_taille_porte_le_remplacement` ; mutations R09, R13, R16 tuées |
| auto-préférence au **modèle joué**, lecture par famille descriptive à côté | oui | v1 inchangée l. 488-499 ; essai v1 porté `test_sain_remplacement_declare_admis` (`n_propre_modele = 0` au modèle joué) ; mutations R08, R14 tuées |
| verrous inchangés (attestation scellée, jamais rejoué après dépense, témoins, plafond externe, aucun repli silencieux) | oui | `pole/ideation_v2.py` et `pole/bras_remplacement_juge_v1.py` ont la même empreinte qu'à la v1 contre-lue ; le module v2 n'ajoute aucun chemin autour d'eux (86 lignes lues entièrement) ; `TestVerrousInchanges` porté (quatre essais passés) |
| différentiel = ajouts seuls | oui | cinq A contre `0861800`, huit A contre `a41b7b50` ; aucun M ni D ; commit du dépôt de travail : 20 A |
| essais rejoués, décomptes exacts | oui | section 2 |
| au moins deux mutations à moi | oui | huit, section 3 |
| suite de l'orchestrateur sans échec neuf | oui | section 2 : tête et base aux décomptes du développeur, mêmes 7 échecs, 14 erreurs de collecte et 5 sautés, tous antérieurs à la v1 |

## 6. Table des constats

| n° | gravité | fichier | lignes | constat et preuve | correction proposée |
|---|---|---|---|---|---|
| 1 | mineur (couverture d'essai) | `orchestrator/essais/test_bras_remplacement_juge_v2.py` | 446-623 (`TestEtiquetteRepeteeRefusee`, `TestGardeEtiquettesPure`) | Les essais du cœur répètent toujours le **même objet** chaîne (`ETIQ`, `"a"`) : une garde qui comparerait par identité (`is`) au lieu de l'égalité (`==`) y passerait. Ma mutation K01 n'est tuée que par `TestLanceursNeufs` (7 échecs, tous dans cette classe : les blancs retirés et l'étiquette par défaut `externe-N` produisent des chaînes neuves). Le code livré compare bien par `==` (l. 58-59, lu). | Si un cycle a lieu (R12, fichier neuf) : un sous-cas du cœur avec deux objets égaux et distincts (par exemple `"".join(["lx-", "juge"])`). Aucun effet sur le livrable. |
| 2 | mineur (information) | `orchestrator/demonstrations/ideation_v2_juges_externes_uniques_v1.py` ; `demonstrations/ideation_v2.py` | 43 ; 1105-1160 | Le code 2 de la garde neuve (erreur d'argument `argparse`) est aussi celui des « arrêts » du lanceur d'origine (`{"arret": …}`, code 2) : seul le message distingue les deux (sortie d'erreur « error: --juge-externe … en double » contre un JSON `arret`). Sondes k12, k13. | Aucune ; le lanceur de la relance lit le message, pas le seul code. |
| 3 | mineur (information) | `orchestrator/pole/bras_remplacement_juge_v2.py` | 48-56 | Formes non inspectées par la garde (itérateur, objet non itérable, entrée qui n'est pas un tuple ou une liste de trois éléments, dictionnaire) : passées telles quelles à la v2, qui échoue avant tout appel (`TypeError` sur `len`, échec du dépaquetage) ; vérifié par l'essai `test_formes_non_inspectees_suivent_la_v2_sans_appel` et ma sonde k07 (aucun accès à l'adaptateur, rien écrit). Un lanceur ne passe jamais ces formes. Déclaré par le développeur. | Aucune. |
| 4 | mineur (information) | `orchestrator/pole/bras_remplacement_juge_v2.py` | 58 | Au cœur, les étiquettes sont comparées telles quelles (`"a"` ≠ `"a "`) ; le lanceur retire les blancs avant la garde (`paire`). Au cœur, une étiquette à blanc ne passe de toute façon pas CL35-04 (étiquettes ≠ celles de la course). Sonde k06. | Aucune. |
| 5 | mineur (information) | `orchestrator/pole/ideation_v2.py`, `pole/ideation.py`, `pole/bras_remplacement_juge_v1.py`, `demonstrations/ideation_v2.py`, `ideation_v1.py` | 2852, 2847, 255, — | Le défaut **demeure** dans les fichiers gardés tels quels (R12) : ma sonde k04 montre que, par `ideation_v2.executer_bras_differe`, le modèle non déclaré reçoit **deux** appels (contrôle puis juge) avant le verrou. Déclaré par le développeur (§ 7). | La relance n'épingle que le module v2 et, en ligne de commande, `ideation_v2_juges_externes_uniques_v1.py` ; jamais la v1 ni `ideation_v2` seuls comme point d'entrée. |
| 6 | mineur (information) | `orchestrator/pole/bras_remplacement_juge_v1.py` | 83-85, 104-107 | Les constats 1 et 2 de la contre-lecture v1 (`TypeError` sur une option aux clés non comparables ; caractères de format `Cf` admis dans le mot) demeurent dans la v1, inchangée, donc dans le chemin **avec option** de la v2. Hors de la demande de la relance (étiquette répétée seule). | Version neuve ultérieure si voulue ; aucun verrou touché. |
| 7 | mineur (information) | `orchestrator/pole/outils.py` | 157-165 | Tout manifeste écrit depuis l'arbre `71417ad1…` porte une entrée de plus dans `code_sha256` (`bras_remplacement_juge_v2.py`) qu'à `3c6cff30…`, avec ou sans option : effet de tout fichier neuf dans `pole/`, déclaré. | Aucune ; à savoir pour comparer des manifestes. |
| 8 | mineur (information) | `orchestrator/demonstrations/ideation_v2_juges_externes_uniques_v1.py` | 46 | Le lanceur neuf ne transmet toujours pas l'option de remplacement (il appelle le lanceur d'origine, qui appelle `pole.ideation_v2`) : la relance doit appeler `pole.bras_remplacement_juge_v2.executer_bras_differe` directement pour jouer le remplacement déclaré. Déclaré (§ 4, § 7). | Lanceur de la relance (spécification, « Pièces neuves côté relance »). |
| 9 | mineur (méthode, déclaré) | `rapport-developpeur-remplacement-juge-v2.md` | en-tête | Refus de la garde d'isolement (commande composée découpée) et un `git commit -F /dev/stdin <<< ""` refusé par git (message vide, rien commis). Sans effet sur le livrable : différentiel recalculé identique, arbre de la tête recalculé identique. | Aucune. |

Aucun constat bloquant, aucun constat majeur.

## 7. Ce que la relance peut épingler (après ce verdict)

- Commit de l'orchestrateur **`8a2a6ac9d3feb52e6771edca52f440dd780fb373`** (parent `0861800260e33224a71f48b111e72ac04288d3cb`, base `a41b7b50f7c64ce488c120bb89ad3d25fb1dd1cb`) ; arbre `orchestrator/` **`71417ad17d816af07a6a57e9dc28bbfac07faac5`** ; `orchestrator/pole` `bfd8585661fdcce6157bc5287f86e2371ea254b3` ; paquet `orchestrateur-remplacement-juge-v2.bundle` `1c5a5bd2…` (prérequis `a41b7b50`, s'applique seul sur la copie en lecture seule).
- Point d'entrée **`pole.bras_remplacement_juge_v2.executer_bras_differe`** (`83a08aee…`), épinglé avec `pole/bras_remplacement_juge_v1.py` `2efd6b08…` et `pole/ideation_v2.py` `67d2ad35…` ; **une seule entrée par étiquette** dans `juges_externes`.
- En ligne de commande, uniquement `demonstrations/ideation_v2_juges_externes_uniques_v1.py` (`1fbe2be3…`, qui charge `demonstrations/ideation_v2.py` `bc5e9c98…`) ; il n'offre pas l'option de remplacement (constat 8).
- Le bloc gelé provisoire de `empreintes-orchestrateur-remplacement-juge-v2.txt` peut être figé tel quel : aucun constat ne l'impose à changer.

## Verdict

Conforme.

La version 2 fait ce que la relance demandait : toute liste `juges_externes` dont une étiquette apparaît plus d'une fois est refusée par la première instruction du bras, avec et sans option, sans lecture, sans appel, sans écriture (rejoué par moi au cœur avec un adaptateur qui interdit tout accès, et par les deux lignes de commande concernées, dans tous les modes) ; sans option, tout le reste est `ideation_v2.executer_bras_differe` elle-même ; avec option, la version 1 contre-lue, intacte ; les manifestes de toutes les tentatives et l'auto-préférence au modèle joué sont tenus et éprouvés ; les verrous sont inchangés (mêmes empreintes) ; le différentiel ne contient que des ajouts ; essais et banc de mutations rejoués aux mêmes décomptes ; huit mutations à moi, toutes tuées ; la suite complète de l'orchestrateur, tête puis base, ne montre aucun échec neuf. Les neuf constats sont mineurs ou informatifs ; aucun n'exige de correction avant l'épinglage. La ligne de GO revient à la mère.
