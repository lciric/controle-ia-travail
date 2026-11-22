# Rapport du développeur — véhicule NA-1, lot 6 v4 (registre des tentatives alimenté, comptes de M6 et des replis, garde du coffre avec repli, code chargé) — v1

- Développeur du lot 6 v4 du véhicule NA-1 (modèle O). Je n'ai écrit ni les lots 1 à 5, 10 a, 6 v1 à v3, ni la conception, ni l'additif, ni l'interface.
- Date (UTC) : 2026-11-22.
- Processeur seul : aucun appel de modèle, aucun réseau, aucune clé, aucune dépense, aucune écriture dans un dépôt, aucun commit. Aucune variable d'environnement affichée. Écritures sous mon seul dossier `vehicule-na-lot-6-v4/`.
- Lectures : les seuls fichiers du mandat, par chemin complet (§ 2). **Aucun refus d'outil ni de classifieur.** Une sortie trop longue (lignes 121 à 240 du projet d'additif v2) a été rangée d'office par l'outil comme sortie enregistrée : **je ne l'ai pas ouverte** ; j'ai relu ces lignes par tranches plus courtes dans le fichier même. **Écart à la règle de lecture, déclaré** : pour écrire les compagnons et la table d'empreintes, j'ai lancé une fois `find` **sur mon seul dossier d'écriture** (`vehicule-na-lot-6-v4/`, hors `tmp/`). Le mandat interdit `find` sans exception. Rien hors de mon dossier n'a été listé ni lu. Les compagnons et la table ont ensuite été réécrits par un programme qui nomme chaque fichier un à un, sans liste.

## 1. Verdict

- **Le lot 6 v4 porte ce que le mandat demande, contre l'interface**, dans un module neuf `paquet/orchestrator/pole/course_na_v4.py` (noté C4), à côté du v3, qui n'est pas modifié (empreintes du v3 vérifiées contre leurs compagnons : OK).
- **Essais : 68 passés, 0 échec** (`journal-essais-na-lot-6-v4.txt`).
- **Mutations : 31 tuées sur 31**, témoin non muté et témoin inerte survivants, aucune invalide (`journal-mutations-na-lot-6-v4.json`). Le brouillon (premier passage) en avait laissé deux vivantes (V07, V27) : deux essais neufs les tuent (`brouillon-mutations-1-na-lot-6-v4.json`).
- **Ce qui n'est pas fait, faute de pièces que je n'ai pas le droit de lire** : le branchement dans `GenerationNA` du v3 et la chaîne entière sur copie neuve (v68, lots 2 à 5, 10 a). Voir § 6, « Besoins ».
- **L'interface ne se tient pas entière** en quatre points (§ 5) ; je ne l'ai pas changée : j'ai isolé chaque écart dans une constante nommée et je le dis ici.

## 2. Pièces lues (empreintes recalculées)

| pièce (C = `docs/notes/ideation-nouvelles-attaques-v1/`) | sha256 |
|---|---|
| C/interface-lots-5-6-7-repli-v1.md | `497419021b18f1906e4967d49649632a86d38a1ec13ee5a20031a81dca2aca2f` |
| C/mandat-developpeur-vehicule-na-lot-6-v1.md | `b59766267b5b285ad12395a86bb388fc12af48ebe6ded630a3062c2bac6f6b1d` |
| C/mandat-developpeur-vehicule-na-lot-6-v2-reprise-v1.md | `89b2a38d1b38d3a925afa8c40fa59415abd7935e09f429a2fd0ec1686abe7b1a` |
| C/erratum-1-…-v1.md ; C/erratum-1-…-v2.md | `1b08d873…667e` ; `24d37f85…1730` |
| C/lot-5-vehicule-na-v1/…/registre_na_v1.py | `a2a359852e23bc2728d9ad32a525137c1282cffa02dab27388833a2f62451744` |
| C/lot-4-vehicule-na-v1/…/appel_garde_na_v1.py ; adaptateur_claude_na_v1.py | `d16d07bf…1428` ; `38baa206…a763` |
| C/conception-vehicule-v5/…-v5.md (§ 2.6, 2.8, 2.13, 7, par extraits) | `1b7f6822af20417e997b80290f05e7a4d70aa69c3d65f4139b5b3673cd98a863` |
| C/additif-vehicule-na-projet-v2/additif-vehicule-na-projet-v2.md | `6e9bb88e680211b10646f147611a6a4c90a7b9cc6b03be97f8b39fafd4cfa6ba` |
| C/noeuds-et-part-luc-v2/noeuds-ouverts-vehicule-na-v2.md (§ 3, § 5.2) | `79b9d423f662a3759a0f36037af1d0faae5e6757223d6c40c672d5e973c53032` |
| V9 scellée (l. 88-102, 145-162, 366-380) | `864f39a7ecd41a613f8892efbf66607c14da34252d643a4fd40032b5d2b500c2` |
| C/lot-6-vehicule-na-v3/rapport-developpeur-lot-6-na-v3.md | `4992e4bf3011300e878ea1f35c7276720f1472883f7c87342f0759720ec45b63` |
| C/lot-6-vehicule-na-v3/reserve-modele-de-menace-lot-6-v3-v1.md | `a92d3d4a9ef862bbced8f81121b2bb8389bccd4c6c11f68fb65490ab82791de4` |
| C/lot-6-vehicule-na-v3/verification-v1/verification-lot-6-na-v3-v1.md | `0eedf5f9cfd73a320a8b64b281d5498eed3458b2a7a4bbdecff4732a9f96abba` |
| course_na_v3.py (par extraits : en-tête, l. 104-120, 339-475, 578-664) | `7c154a8987a34d75cee13ecf27d1d580e65afbeba051a3b34ef6798a56e87614` |
| configuration_course_na_v1.py (l. 1-40, 255-290) | `0264479234576b3b66e7fd1af35475c3a7858a9a1ef3c5cf949c2f753aaf5c18` |
| mutations_na_lot6_v3.py (l. 1-60, pour la manière) | compagnon du v3 |

## 3. Ce que la v4 porte, et où

| exigence | source | code (C4 = `pole/course_na_v4.py`) | essais |
|---|---|---|---|
| chaque tentative écrite au registre, champs de l'interface (`generation`, `filiation`, `espece`, `case`, `rang_repli`, `modele_demande`, `modele_servi`, `raison_arret`, `categorie_refus`, `cout_compte_usd`, `classe_issue`) | interface, « Registre » | `AlimentationRegistreNA.consigner_chaine` C4:369 ; écriture après toutes les vérifications C4:413 | `TestRegistre` (13) |
| une ligne par fiche rendue, qui porte la tentative **servie** (rang, modèle servi), coût à zéro (le coût vit à la ligne de tentative) | P7, P8 ; interface | C4:393, C4:397 | `test_fiches_servies_par_repli_portent_la_tentative_servie` ; V13, V14 |
| filiation : identifiant de la fiche mère ou nulle (« aucune » → nulle) | interface | `_filiation` C4:346 | idem ; V30 |
| classe de la chaîne à l'espèce demandée (P12) ; classe neuve « refus par classifieur, servi par repli » | P7-bis, P12 ; R-4812 | `classe_de_la_chaine` C4:316, `classe_de_la_tentative` C4:328 | V01, V26, V27, V29 |
| lecture de la chaîne de l'appel (rangs 0, 1, 2 ; suite fermée modèle du rôle, premier, second repli ; repli seulement après « refusal », A6 ; repli seulement sur une espèce à clé Claude, P1) | P1, A6 ; nœuds § 5.2 | `tentatives_de_l_appel` C4:262, C4:311 | `TestLectureChaine` ; V08, V09, V10 |
| n° 31 : modèle servi absent ou autre que le modèle demandé **de la tentative** | additif § 10 ; P16 | C4:299 et la ligne qui précède | V06, V07 |
| coût au pire si l'usage manque, jamais moins | A3 ; P4 ; interface | dans `tentatives_de_l_appel` | V11 |
| catégorie jamais devinée (seulement avec un refus) | interface ; A5 | idem | V12 |
| n° 34 : un (espèce, modèle) sans pire | additif § 10 | `ConfigurationReplisNA.verifier_pires` C4:226 | V25 |
| champ « modèles de repli » distinct de `a11_modeles` (qui reste `[]`, non lu ici) | P16 ; nœuds § 5.2, point 6 | `ConfigurationReplisNA` C4:184 | `TestConfiguration` |
| **M6** par génération, par rôle, par espèce demandée, par case, par (case, espèce) ; sous-compte « cause non établie, en repli » ; tentatives de rang 0 des proposeurs seules (une chaîne = un appel) | V9 l. 160 ; P7-quater ; interface | `comptes_m6` C4:461 | `TestComptes` ; V02, V24, V28 |
| **replis** par espèce demandée et modèle servi (nombre, coût) ; par modèle demandé ; servies par repli, à part, au nom du modèle servi (tentatives par classe, fiches par classe) | P10 (3) ; interface | `comptes_replis` C4:485 | V17 |
| **M3** lecture scellée (fiches de repli comprises) et lecture « espèces seules » ; fiches de repli à part par modèle servi | P8, P10 | `comptes_m3` C4:517 | V16 |
| **M4** : première tentative seule à l'espèce ; ligne « replis » (coût par modèle demandé, fiches passées servies par repli) | P9 ; interface | `comptes_m4` C4:535 | V15 ; somme des coûts égale au total |
| **n° 5** sur les lignes de fiche de la génération, servies par repli comprises ; un quart exactement part ; dernière génération consignée | V9 l. 376 ; P8 ; D-22.3 | `garde_du_coffre_v4` C4:570, C4:582 | `TestGardeDuCoffre` ; V03, V04, V05 |
| **C-1** contrôle d'empreinte du code chargé (n° 33) ; **C-3** réserve déclarée ; C-4 constat | additif § 3 ; N3 | `lire_table_empreintes` C4:620, `verifier_code_charge` C4:640, `RESERVE_C3` | `TestCodeCharge` (10) ; V18 à V22 |
| comptes écrits en fichier neuf avec compagnon (R6, R12) | — | `ecrire_comptes` C4:607 | `test_comptes_serialisables_et_ecrits` |
| course simulée de trois générations, graines par `SeedSequence` dérivée par (génération, case, espèce) (R9) | mandat | `pole/simulation_na_v4.py` ; `demonstrations/lancer_course_simulee_na_v4.py` | `TestCourseSimulee` |

**C-1, ce qui est vérifié.** Pour chaque module de `sys.modules` dont le fichier vit sous la racine du paquet, ou dont le nom est dans un espace protégé (`pole` par défaut) : refus si aucun fichier `.py` lisible, si le fichier est hors de la racine, hors table, ou d'une autre empreinte ; un paquet d'espace de noms est admis si tous ses dossiers sont sous la racine. La table est lue à son empreinte. **C-3 éprouvé comme limite, non comme refus** : un `__code__` échangé passe le contrôle (`test_limite_c3_modification_en_memoire_non_vue`). **C-4** : le contrôle ne lit aucun texte rendu par un modèle ; ce module n'exécute aucun texte rendu (constat de lecture du code, non une preuve).

## 4. Formats pour le lot 7 (et le lot 5 v2)

- **Registre** : une ligne par tentative (`classe` nulle ; `identifiant` = `<identifiant de chaîne>.t<rang>` ; `filiation` nulle) et une ligne par fiche rendue (`classe` ∈ « passée », « au coffre », « hors case » ; `identifiant` et `nom` = identifiant de la fiche ; pour « passée », les trois champs fermés et `enonce` sur une ligne ; `classe_issue` = « fiches rendues » ; champs de la tentative servie ; `cout_compte_usd` = `"0"`). Les montants sont des **chaînes décimales** (`"0.25"`), pour garder l'exactitude du type « décimal ».
- **Compter les appels** : lignes de tentative de rang 0. **Compter les fiches rendues** : lignes dont `classe` n'est pas nulle. **Sommer les coûts** : toutes les lignes (les lignes de fiche valent zéro).
- **Comptes** (`comptes-tentatives-et-replis-na-v4.json` + `.sha256`, `course_na_v4.NOM_COMPTES`) : `{"version": "course-na-v4", "m6": {g: {par_role, par_espece, par_case, par_case_et_espece, sous_comptes}}, "replis": {g: {par_espece_et_modele_servi: {espece: {modele_servi: {nombre, cout_usd}}}, par_modele_demande, servies_par_repli: {modele_servi: {tentatives, fiches}}}}, "m3": {g: {scellee, especes_seules, servies_par_repli}}, "m4": {g: {par_espece: {espece: {cout_usd, fiches_passees}}, replis: {cout_usd, par_modele_demande, fiches_passees}}}}`. Le lot 7 peut tout recalculer depuis le registre par `comptes_v4(lignes, config)`.
- **Ligne de la génération** (au branchement) : proposer deux clés neuves, `comptes_lot_6_v4` (= `comptes_v4` de la génération) et `coffre_v4` (= `ConstatCoffreV4`, avec `dont_repli_rendues`, `dont_repli_au_coffre`), sans toucher aux clés du v3.

## 5. Où je ne tiens pas l'interface (dit, non changé)

1. **`classe_issue` d'une chaîne qui finit sur un refus** (trois refus, ou chaîne coupée par un arrêt de budget) : aucune des cinq classes ne convient (P12 : « aucune classe de M6, mais le n° 1 »). J'écris `CLASSE_ARRET_1` = « arrêt n° 1, consigné, non relancé » (C4:71), hors liste. À trancher.
2. **`classe_issue` d'une tentative servie d'un rôle non proposeur** (aiguilleur, portier, juges, passe X) : les classes de la V9 sont des classes d'appel de proposeur. J'écris `CLASSE_HORS_M6` (C4:72), hors liste. Une chaîne non proposeuse servie par repli prend bien « refus par classifieur, servi par repli ». À trancher.
3. **`modele_servi` d'une tentative sans réponse** (erreur : crédit, accès, coupure) : l'interface veut une chaîne « lue dans la réponse » ; il n'y en a pas. J'écris `SANS_REPONSE` = « sans réponse » (C4:80).
4. **Lignes de tentative et lignes de fiche dans un même registre** : l'interface ne dit pas comment les distinguer. Je les distingue par `classe` nulle, sans champ neuf. **Conséquence pour le lot 5 v2** : `registre_na_v1.garde_du_coffre` compte **toutes** les lignes de la génération comme fiches rendues (l. 216 : `rendues = len(de_g)`) ; avec des lignes de tentative, la part au coffre serait diluée et l'arrêt n° 5 ne se lèverait pas (épreuve : `test_les_lignes_de_tentative_ne_diluent_pas`, où 2 sur 4 fiches au coffre font 2 sur 9 lignes). La garde du v4 lit les seules lignes de fiche ; **le lot 5 v2 doit faire de même**, ainsi que `fabriquer_registre_servi` (une ligne de classe nulle y lève « classe inconnue »).
5. Forme attendue du **lot 4 v2** (en écriture) : `a["tentatives_na"]`, liste de `{rang_repli, modele_demande, modele_servi, raison_arret, categorie_refus, cout_compte_usd, usage_manquant}`. Un dictionnaire du lot 4 v1 est refusé (aucune lecture sans la chaîne). Si le lot 4 v2 rend autre chose, seule `tentatives_de_l_appel` change.
6. La conception v5, § 2.6, disait du registre des tentatives : « rien du coût, rien de l'espèce ». L'interface y met l'un et l'autre ; je suis l'interface (écart à la conception, à confirmer par la mère).

## 6. Essais, mutations, différentiel, besoins

**Commandes** (`TMPDIR` posé dans mon dossier) : `…/.venv/bin/python -B -m pytest -v -p no:cacheprovider essais` (68 passés) ; `…/python -B essais/mutations_na_lot6_v4.py --racine . --journal …/journal-mutations-na-lot-6-v4.json` (33 jouées : T0, T1 survivent ; V01 à V31 tuées) ; `…/python -B demonstrations/lancer_course_simulee_na_v4.py --sortie …/demonstration-course-simulee` (276 lignes ; coffre 0/12, 1/16, 1/17 ; aucune génération arrêtée).

**Différentiel avec le v3.** (a) Aucun fichier du v3 n'est touché ; la v4 ajoute `course_na_v4.py`, `simulation_na_v4.py`, le lanceur simulé, l'essai et les mutations. (b) `TestDifferentielV3` : l'oracle est `_classer_retour_proposeur` du v3 (C3:415-445), recopié pour ses issues. Sans repli, les comptes du v4 au rang 0 égalent ceux du v3 (texte rendu ; illisible, cause non établie). Avec repli, l'écart est celui de P12 et rien d'autre : le v3 compte « arrêt n° 1 », le v4 compte « refus par classifieur, servi par repli ».

**Objets hors paquet** : `orchestrator/conftest.py` et `pole/__init__.py` (vide). Ils ne servent qu'à faire tourner les essais hors de l'orchestrateur. Ils ne sont pas à appliquer.

**Besoins (fichiers hors de ma liste, non cherchés)** :
- pour brancher et éprouver dans `GenerationNA` : `portier_na_v1.py` (forme de `IssueFiche` et classes des réponses sans fiche), `contrat_fiche_na_v1.py` (`CHAMPS_FERMES`), la v68 et l'orchestrateur `a41b7b50…`, les lots 2 v5 à 5 v1, 10 a, et le programme d'application du v3 ;
- l'interface du lot 5 v2 (noms des méthodes du registre au-delà de `ajouter`) et la forme rendue par le lot 4 v2 ;
- la table d'empreintes du paquet assemblé, pour C-1 en course. Elle est du ressort du lot 8 (nœuds § 5.2, point 8).

## 7. Réserves

- R-1. Le branchement se fera au lot 8, à l'assemblage, ou dans un v5 du lot 6 qui aura le droit de lire les pièces du § 6. Il se ferait en quatre lieux du v3. (1) `_classer_retour_proposeur` : garder la chaîne. (2) `etape_aiguillage` : consigner la chaîne quand le portier a classé la réponse ; consigner tout de suite une chaîne sans réponse servie. (3) La garde du coffre (C3:774) : la remplacer par `garde_du_coffre_v4`. (4) `ligne_de_generation` : y ajouter les deux clés du § 4. Un refus écrit ou un appel non lancé n'écrit aucune ligne : ce n'est pas un appel (§ 2.13 de la conception).
- R-2. C-1 regarde les fichiers sur disque. Il ne voit ni une modification en mémoire (C-3), ni un fichier modifié puis rétabli entre deux contrôles.
- R-3. Le faux fournisseur et le registre factice sont à moi. Ils ne prouvent pas que les lots 4 v2 et 5 v2 tiendront la même forme.

## 8. Relevé de méthode

**Chaîne de raisonnement.**
1. L'interface (`49741902…`) demande cinq choses au lot 6 v4 : champs par tentative ; M6 par case et par espèce ; replis par espèce et modèle servi ; fiche de repli au modèle servi, dans M3 et le n° 5 ; M4 au rang 0, plus une ligne « replis ».
2. Le projet d'additif v2 (`6e9bb88e…`), P7 à P12, donne les règles de classe et de compte. C-1 à C-3 donnent le contrôle du code chargé.
3. Le mandat interdit de lire les lots 1 à 5, 10 a et la v68 au-delà de trois fichiers. Donc le v3 ne peut pas être importé ici (il les importe, C3:71-90 lu). Donc la v4 est un module autonome contre l'interface (pas 1, pas 2).
4. Le registre du lot 5 v1 (`a2a35985…`) compte toutes ses lignes comme fiches rendues (l. 216). Si on y ajoute des lignes de tentative, le n° 5 est dilué. Calcul rejoué : l'essai de dilution (2/4 contre 2/9).
5. P12 (« aucune classe de M6, mais le n° 1 ») et la liste fermée de l'interface ne couvrent pas tous les cas : § 5, points 1 à 3.
6. Les essais et les mutations sont rejoués (§ 6).
7. Supposé : la forme rendue par le lot 4 v2 (§ 5, point 5).

**Objets de contrôle.** Chaque garde, avec son cas sain et son artefact, ce que j'attendais, puis ce qui est rendu :
- n° 5 : un quart exactement, attendu « part », rendu « part » ; une fiche de repli au coffre en plus, attendu arrêt avec `dont_repli = 1`, rendu arrêt ; dilution par les lignes de tentative, attendu arrêt (la lecture du v1 ne lèverait pas), rendu arrêt ; génération 3, attendu « consigné », rendu « consigné ».
- n° 31 : même modèle, attendu « lu », rendu « lu » ; modèle absent, puis modèle autre, attendu arrêt n° 31 avec sa cause, rendu arrêt.
- A6 : repli après un refus, attendu « lu », rendu « lu » ; repli après une réponse servie ou une raison inconnue, attendu arrêt, rendu arrêt ; repli sur une espèce sans repli, attendu arrêt, rendu arrêt ; modèle hors de la suite, attendu arrêt, rendu arrêt.
- n° 34 : tous les pires, attendu départ, rendu départ ; un pire de repli manquant, attendu n° 34, rendu n° 34.
- n° 33 : table égale, attendu « vérifié », rendu « vérifié » (vrai `sys.modules` compris). Quatre artefacts, attendu refus, rendu refus : module planté, fichier modifié, module protégé hors racine, source absente. Table d'une autre empreinte, et espace de noms hors racine : attendu refus, rendu refus.
- C-3 : `__code__` échangé, attendu « non vu » (limite déclarée), rendu « non vu ».
- Atomicité : une fiche hors forme dans une chaîne, attendu aucune ligne écrite, rendu aucune ligne écrite (V31 tuée).
- Juge des mutations : le témoin non muté et le témoin inerte survivent.

**Premier pas non justifié.** Le pas 7 : la forme de la chaîne rendue par le lot 4 v2 est supposée. Le justifierait l'interface figée du lot 4 v2. Ensuite le pas 5 : les valeurs hors liste sont de moi. Les justifierait un mot de la coordination.

**Mode d'échec affecté.** Sans objet : je suis développeur, non relecteur.

**Dérivation de l'énoncé seul.** Sans objet : je suis développeur, non agent de re-dérivation.

**Trouvaille de côté.** La garde du coffre du lot 5 v1 compterait les lignes de tentative comme des fiches rendues (§ 5, point 4). C'est un point pour le développeur du lot 5 v2, non poursuivi ici.

**Évaluateur et conseil.** Ce qui juge mon produit, ce sont mes essais et mes mutations ; le juge des mutations est admis sur deux témoins. Les cas sont écrits par moi, contre mon propre registre factice et mon propre faux fournisseur. Mon produit pourrait donc être bien jugé sans le mériter : si les lots 4 v2 et 5 v2 rendent d'autres formes, tout passe ici et casse à l'assemblage (R-3). Le remède est un essai d'assemblage sur les vrais lots.

## 9. Fichiers et empreintes

Table complète : `table-empreintes-dossier-na-lot-6-v4.txt` (avec son compagnon), écrite après ce rapport. Chaque fichier a son compagnon `.sha256`. Sont hors table : `tmp/`, et les sorties de `demonstration-course-simulee/`, qui ont déjà leurs propres compagnons.

— développeur du lot 6 v4 du véhicule NA-1, modèle O
