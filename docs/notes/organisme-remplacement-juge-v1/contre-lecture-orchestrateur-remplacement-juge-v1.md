# Contre-lecture — orchestrateur de l'organisme d'idéation, version neuve : remplacement déclaré du modèle d'un juge externe différé — v1

- **Date** (temps universel, `date -u`) : 2026-11-18T17:09:45Z (début de la contre-lecture 2026-11-18T16:25Z environ, fin de la dernière suite 2026-11-18T17:09:01Z).
- **Contre-lecteur : modèle K**, agent neuf. Je n'ai écrit aucune des pièces relues (module, essais, banc de mutations, rapport du développeur, écrit par le modèle L'), ni la demande, ni `pole/ideation_v2.py`.
- **Objet** : branche `prep/orchestrateur-remplacement-juge-compte-organisme-v1`, commit `50a6f1a4aa121078da427d1d4159d8eabb7138cb` (20 ajouts sur `da55b2a13f88ead4ed03a4cb3776bb571bfd1052`, aucune ligne M ni D ; `da55b2a1` est un ancêtre de `lot/compte-organisme-v1`), dossier `docs/notes/organisme-remplacement-juge-v1/`.
- **Hors ligne** : aucune dépense, aucun appel réseau, aucun relais, aucun lanceur en mode réel ; rien installé ; rien écrit dans `/home/user/ideation-organism` (tête restée `a41b7b50f7c64ce488c120bb89ad3d25fb1dd1cb`, arbre de travail propre, vérifié) ; deux clones locaux neufs à poussée neutralisée (`/home/user/orch-relecture-remplacement-juge-v1`, `/home/user/orch-relecture-base-a41b7b50`), jamais poussés.

## 1. Empreintes vérifiées

Toutes les pièces du dossier ont leur compagnon `.sha256` ; `sha256sum -c` sur les dix compagnons : tous justes. Les empreintes ci-dessous sont celles que j'ai calculées moi-même ; elles sont égales à celles du rapport du développeur et du bloc gelé provisoire.

| pièce | sha256 |
|---|---|
| paquet `orchestrateur-remplacement-juge-v1.bundle` | `5701775c1e6ea591664169ae837dcbb6f77ba2600716aeb1b0aa51554740ef9c` |
| différentiel `orchestrateur-remplacement-juge-v1-contre-a41b7b50.diff` | `b45a0b8758675071dd04e291130aa117450b20dfccabb7b43948b8cc8dc0486e` |
| écarts de la copie `ecarts-copie-contre-v2-remplacement-juge-v1.diff` | `efbc0c0047527dc3605bdefcbf84e8a21330e64785ec89275b6fc051b34cf5f9` |
| spécification `docs/notes/relance-organismes-discrets-v1/demande-orchestrateur-remplacement-modele-juge-v1.md` (branche `claude/pensive-bardeen-1fv7hw`, `df8af8da401e9f090e10949dbd0a530ba9e54ee1`, lue par `git show`) | `2ddb1117e77820ebfaa6a84133cc03c140d262b3765c5960fcbdb8bc091fe136` |
| `rapport-developpeur-remplacement-juge-v1.md` | `bd3e442c838ca4cfef5020048d76931e1e416836153ecca16ed9a02f65becde5` |
| `empreintes-orchestrateur-remplacement-juge-v1.txt` | `b437bd6bac436cf4324cc2c3aaf6a20fee6301c8cd3f628a4422f85bcfb204c2` |
| `essais-remplacement-juge-v1.txt` | `921d3b95a55b158d912bf07717f023eed35138c649e8d75cfd6b4be90ad8e2e0` |
| `mutations-remplacement-juge-v1.json` / `.txt` | `5eee259cf0a231f7df4f824217bce497e47cd098ddfe051075cc055bed68b6a6` / `ef6efd39fa54b0b39f3f945deb58b93ada8061099a032e93852cf1572917d3ac` |
| `suite-orchestrateur-remplacement-juge-v1.txt` / `suite-base-a41b7b50-remplacement-juge-v1.txt` | `1aa2c966b154ac5b29123043707159f86c6d0f21a8d64da0f06ea3f370feec0b` / `ac978929d30f47a90664c18e921e65c4e4af10f7cf7d98afaf953de8eca6672f` |

Orchestrateur, dans mon clone neuf :

| objet | valeur |
|---|---|
| base déclarée : commit `a41b7b50f7c64ce488c120bb89ad3d25fb1dd1cb` = `origin/main` de la copie en lecture seule | arbre `orchestrator/` **`ee84d6eca7a4c9b25f4e297ca29c6d9f24af5d70`**, l'« arbre actuel `ee84d6ec…` » de la spécification (`git cat-file -t` : `tree`) ; `orchestrator/pole` `0d2fefff4ed8f7fa17e58042af413a86373c0396` |
| `git bundle verify` | « is okay » ; une référence `refs/heads/prep-remplacement-juge-v1` → `0861800260e33224a71f48b111e72ac04288d3cb` ; prérequis `a41b7b50…` |
| tête du paquet (après `git fetch` du paquet) | `08618002…`, parent `a41b7b50…` ; arbre `orchestrator/` `3c6cff30671bb5bdf6b7f461c167db48e32c5d6d` ; `orchestrator/pole` `55cae9e0effc76e5201ad47c5f8b3bd9d055609a` |
| `git diff --name-status a41b7b50 08618002` | exactement trois lignes **A** : `orchestrator/pole/bras_remplacement_juge_v1.py`, `orchestrator/essais/test_bras_remplacement_juge_v1.py`, `orchestrator/essais/mutations_bras_remplacement_juge_v1.py` ; aucune M, aucune D |
| `git diff a41b7b50 08618002` recalculé | sha256 `b45a0b87…`, identique octet pour octet au différentiel livré |
| `orchestrator/pole/bras_remplacement_juge_v1.py` (577 lignes) | `2efd6b0874e8bbfa58a0c53a5099f46da51318c6807c90909b8cf58dfe90866a` |
| `orchestrator/essais/test_bras_remplacement_juge_v1.py` (412 lignes) | `1e5f39d8705b77216829d27da181c929b988b0502509609eb37b16f2efbc34e2` |
| `orchestrator/essais/mutations_bras_remplacement_juge_v1.py` (75 lignes) | `cdd021c6d7f49473ca074f72aa7cdda1d99c31b12401f4dbf32481c92358cbb9` |
| `orchestrator/pole/ideation_v2.py`, base et tête | `67d2ad3591b21601ece4101154138f532ba519024761beb8c9738181f8f3fefc` (inchangé) |

Écarts de la copie : j'ai extrait moi-même `ideation_v2.executer_bras_differe` (lignes 2754-3162) et `_executer_bras_avec_remplacement` (lignes 185-577) et fait le `diff -u` : mêmes lignes ajoutées et retirées que le fichier livré (seule différence : ma fenêtre inclut la ligne d'alias finale de la v2, hors du corps). Six morceaux de différence hors signature et docstring, tous marqués « remplacement-juge-v1 » : garde CL35-04 → `verifier_remplacements_contre_course` et mention dans `lecture_course` (l. 254-261) ; `remplacements_juges_externes` dans le journal (l. 301) ; dans le manifeste du bras avec `mention_remplacement` (l. 310-311) ; dans le manifeste de refus de taille (l. 405) ; modèle joué pour l'auto-préférence et famille (l. 488-492) ; `auto_preference_par_famille` dans la lecture (l. 498-499). Tout le reste du corps est identique à la v2.

## 2. Décomptes des essais (rejoués par moi, interpréteur `/usr/local/bin/python3`, `-B`, `PYTHONDONTWRITEBYTECODE=1`, `-p no:cacheprovider`, `-q -rs`)

| essai | résultat |
|---|---|
| `essais/test_bras_remplacement_juge_v1.py` seul, tête `08618002` | **19 passed, 18 subtests passed in 1.87s** (égal au développeur : 19 passed, 18 subtests passed) |
| banc `essais/mutations_bras_remplacement_juge_v1.py --processus 4` | **18 tuées pour la raison attendue sur 18 mutations**, code 0 ; mêmes décomptes par mutation que le fichier livré (R01, garde CL35-04 neuve retirée : 2 failed dont `test_artefacts_contre_la_course`) |
| suite complète `essais/`, tête, première passe (`--continue-on-collection-errors`) | 8 failed, 1374 passed, 5 skipped, 14 errors, 1231 subtests passed in 691.48s |
| suite complète, tête, deuxième passe | **7 failed, 1374 passed, 5 skipped, 14 errors, 1232 subtests passed in 663.31s** (égal au développeur) |
| suite complète, base `a41b7b50`, jouée **seule** (second clone, aucune concurrence) | **7 failed, 1355 passed, 5 skipped, 14 errors, 1214 subtests passed in 677.84s** |
| première passe sans `--continue-on-collection-errors` | interrompue à la collecte : 14 errors in 3.46s (sans objet, relancée avec l'option) |

- 1374 − 1355 = 19 : les essais du module neuf ; 1232 − 1214 = 18 : ses sous-essais.
- **Les 7 échecs communs** (tête, deuxième passe ; base) : `TestV51.test_v51_10_modele_commande_externe_refuse_sans_attestation`, `TestV51.test_v51_15_r12_la_v50_reste_telle_quelle_et_provenance_de_la_v51`, `TestR12.test_aucun_fichier_de_la_v52b_modifie`, `TestR12.test_aucun_fichier_de_la_v53_modifie`, `TestR12V55.test_aucun_fichier_de_la_v54_modifie`, `TestV49.test_v49_18_provenance_du_code_modifie_dit_au_lisezmoi`, `TestV50.test_v50_17_provenance_du_code_modifie_dit_au_lisezmoi` — fichiers d'archive absents de l'arbre public (`LISEZMOI-…-v49/v50/v51.md`, `EMPREINTES-…-v50/v53/v54.txt`, liste v52b) ; aucun ne touche le bras ; aucun échec neuf.
- **Le 8ᵉ échec de ma première passe** : `LanceurCheminReel.test_artefacts_du_chemin_reel`, sous-cas « budget par appel sous deux fois le prix de plan » (`essais/test_juges_idees_v2.py:1719` : refus « devis de juge-b … au-dessus de sa part » rendu à la place de « plafonds_session.juge »). Rejoué seul : passe à la tête (1 passed, 25 subtests) et à la base (idem) ; passe à la deuxième passe complète. Aucune référence au module neuf dans `test_juges_idees_v2.py`, `demonstrations/validation_juges_idees_v2.py` ni `pole/juges_idees_v2.py` (0 occurrence). Échec transitoire, hors du périmètre de la livraison (constat 8).
- **14 erreurs de collecte** (tête comme base) : `ModuleNotFoundError: No module named 'scipy'` dans quatorze fichiers (`test_boucle_reelle_v65/66/67`, `test_gardes_tour_ferme_v63/64`, `test_lecture_boucle_reelle_v65/66`, `test_tour_ferme_v62/63/64`, `test_v60_lecture_tour_ferme`, `test_v60_oracle_tour_ferme`, `test_v61_lecture_tour_ferme`, `test_v61_tour_ferme`) ; rien installé.
- **5 sautés** avec leur motif : `test_lecture_epreuve_w2g_dose_v1.py:432` sorties exploratoires absentes ; `test_nul_v9.py:199` scipy absent ; `test_v54_annexe.py:265` brouillon 1 hors de la livraison ; `test_v54_corrections.py:314` brouillon 7 hors de la livraison ; `test_v56_corrections.py:893` liste v55 absente de l'arbre.
- Les 18 échecs de la base rapportés par le développeur (deux suites en même temps) ne se reproduisent pas seule : 7. Ses 11 échecs de plus étaient bien la concurrence sur l'utilisateur dédié du bac, comme il le disait ; `bwrap` présent (`/usr/bin/bwrap`) pendant toutes mes passes.

## 3. Exigences de la spécification, une à une

| point | exigence | tenue | preuve |
|---|---|---|---|
| 1 | option explicite par étiquette (modèle de la course, modèle joué, référence de GO, mot verbatim) ; sans elle, comportement inchangé, CL35-04 comprise | oui | `executer_bras_differe` l. 172-178 : `None` → `_v2.executer_bras_differe(sortie, **reglages)` elle-même ; essais `test_sans_option_appelle_la_v2_elle_meme` (espion : mêmes arguments), `test_sans_option_meme_sortie_que_la_v2_cas_fixe` (sept fichiers neufs identiques, quatre lectures octet pour octet), `test_artefact_modele_change_sans_option` (même message CL35-04 que la v2, rien écrit) ; mutation R10 tuée |
| 2 | étiquettes identiques ; modèle donné = course ou remplacement déclaré ; étiquette absente ou modèle de la course discordant → refus | oui | `verifier_remplacements_contre_course` l. 112-146 (et concordance ajoutée avec `noyau/modeles.json["par_juge"]`, l. 130, cohérente : `par_juge` porte bien les juges externes, `ideation_v2.py` l. 2577 et 2584) ; `test_artefacts_contre_la_course`, `TestGardePure.test_sain_et_artefacts` ; mutations R01-R05 tuées ; mes sondes (section 4) |
| 3 | manifeste du bras : deux modèles, référence de GO, mot ; lecture écrite avec la mention visible | oui | journal l. 301 (donc manifestes non joué, tentative payée, repli impossible), manifeste du bras l. 310-311, refus de taille l. 405 ; `lecture.json` et `lecture-sans-bras.json` portent `juge_externe_remplace = {mention, remplacements}` l. 149-151, 260-261 ; essais `test_sain_remplacement_declare_admis`, `test_panne_apres_envoi_repli_sans_bras_avec_mention`, `test_refus_de_taille_porte_le_remplacement` ; mutations R07, R09, R13, R16 tuées |
| 4 | auto-préférence au modèle joué ; lecture par famille à côté, descriptive | oui | l. 488-499 ; `lecture_auto_preference_par_famille` l. 154-169 (`descriptive: True`, motif) ; essai sain : `n_propre_modele = 0` au modèle joué, fiches du proposeur de la lignée « propres » par famille ; `test_famille_temoins_exclus` ; mutations R08, R14 tuées ; réserve sur le sens de « famille » (constat 4) |
| 5 | verrous inchangés : attestation scellée (fiches validées, consignes en attente), jamais rejoué après dépense, témoins relus chez le juge externe, plafond externe, aucun repli silencieux | oui | diff de la copie : attestation l. 233-239 et 282-289, verrou `manifeste-bras-rapporte.json` et `reponse.md` l. 209-212 et 290-291, trois tentatives au plus l. 230-232, plafond externe avant tout appel l. 409-411, témoins l. 493-496 et 504, repli marqué illisible l. 313-333 — tous identiques à la v2 ; `TestVerrousInchanges` (quatre essais) ; CL35-04 « course réelle : seule une commande externe » l. 264-269 inchangée |
| 6 | essais : cas sain ; modèle changé sans option ; option pour une autre étiquette ; modèle de la course faux ; référence de GO vide | oui | `test_sain_remplacement_declare_admis`, `test_sain_option_donnee_modele_de_la_course_joue`, `test_artefact_modele_change_sans_option`, `test_artefacts_contre_la_course`, `test_artefact_reference_de_go_vide` (sept formes) ; plus dix-huit formes mal formées, secret jamais recopié, correspondance entière des motifs |
| 7 | contre-lecture par un agent neuf, puis épinglage | cette pièce ; l'épinglage revient à la relance | — |

Garde CL35-04 hors remplacement déclaré : conservée deux fois — sans option, c'est la v2 elle-même ; avec option, tout modèle donné qui n'est ni celui de la course ni le modèle joué déclaré pour cette étiquette est refusé avec le message CL35-04 (l. 144-145 ; essai : modèle non déclaré refusé ; sonde : modèle joué donné sur une autre étiquette que celle déclarée → refus).

Aucune dépense possible par le module : il n'ouvre aucune connexion ; les adaptateurs sont donnés par le lanceur ; les essais n'utilisent qu'une commande Python locale scriptée à environnement vide ; le banc de mutations copie l'arbre dans un dossier temporaire et joue `pytest` localement.

## 4. Sondes du contre-lecteur (R5, cas sain et artefacts, hors du fichier d'essais ; script dans mon bloc-notes, non livré)

| sonde | issue |
|---|---|
| cas sain aux noms de la demande (modèle de la course → modèle joué de la section « Pourquoi », `GO-2026-11-18-01`) | admis par `valider_remplacements_juges_externes` |
| valeur aux clés mixtes entier et chaîne | **`TypeError`** (dans `_vu(sorted(r))`), pas `CourseInterrompue` ; refus tout de même, rien lu ni écrit (constat 1) |
| étiquette `None` | refus, message caviardé |
| mot avec tabulation (catégorie Cc) | refus |
| mot avec U+200B (catégorie Cf, invisible) | **admis** (constat 2) |
| référence de GO à trois chiffres ; date impossible `GO-2026-99-99-01` | admises (forme seulement, constat 3) |
| deux remplacements, l'un pour une étiquette absente de la course | refus CL35-04 |
| modèle joué donné sur une autre étiquette que celle déclarée | refus CL35-04 |
| `noyau/modeles.json` sans `par_juge` | refus (« la course n'est pas cohérente ») |
| course sans juge externe, remplacement déclaré | refus |
| option `{}` | refus (« non vide attendu ») |
| alias `executer_bras_rapporte` | même objet que `executer_bras_differe`, dans le module neuf comme dans la v2 |
| `lecture_auto_preference_par_famille` avec un juge absent de la table | `KeyError`, comme `lecture_auto_preference` de la v2 (`modele_par_juge[j]`) — même contrat (constat 9) |

## 5. Table des constats

| n° | gravité | fichier | lignes | constat et preuve | correction proposée |
|---|---|---|---|---|---|
| 1 | mineur | `orchestrator/pole/bras_remplacement_juge_v1.py` | 83-85 | Valeur de l'option aux clés non comparables (entier et chaîne) : `_vu(sorted(r))` lève `TypeError` au lieu de `CourseInterrompue`. Refus quand même, avant toute lecture ; un lanceur qui n'attrape que les exceptions de `pole.ideation_v2` verrait une exception brute. Sonde section 4. | Version neuve (R12) : `sorted(map(repr, r))` ou `list(r)` dans le message. Aucun effet sur le cas d'usage (clés chaînes). |
| 2 | mineur | idem | 104-107 | Le mot verbatim refuse les caractères de contrôle (Cc) mais admet les caractères de format (Cf : U+200B, U+200E…), invisibles dans les manifestes. Le mot est une consigne recopiée, pas une garde : aucun effet sur les verrous. | Version neuve : refuser aussi la catégorie `Cf` (et `Cs`, `Co`). |
| 3 | mineur (information) | idem | 54, 101-103 | La référence de GO est vérifiée dans sa forme seulement (`GO-\d{4}-\d{2}-\d{2}-\d{2,}`) : date non vérifiée, registre `registres/go.md` non lu — l'orchestrateur ne connaît pas le dépôt de travail, le développeur le dit (rapport, 6.5). | À la charge du lanceur de la relance : vérifier la ligne de GO contre le registre avant l'appel, et la citer dans son propre manifeste. |
| 4 | mineur (écart documenté) | idem | 58-60, 154-169, 490-492 | « Famille » n'est pas la famille de fournisseur de la demande (point 4) : c'est la paire (modèle de la course, modèle joué) pour un juge remplacé, le seul modèle pour les autres ; aucune famille devinée d'après les noms. Pour le cas visé (proposeur de la lignée resté au modèle de la course) la lecture est celle voulue ; pour les juges internes, elle est égale à la lecture par modèle. Marquée descriptive. | Acceptable pour ce lancement. Si la relance veut des familles de fournisseur pour tous les juges : table déclarée, version neuve. À dire dans la lecture du bras. |
| 5 | mineur (méthode) | `rapport-developpeur-remplacement-juge-v1.md` | §1, §6.1 | Le développeur ne s'est pas arrêté quand `ee84d6ec…` s'est révélé un arbre ; il a pris `a41b7b50` pour base. Vérifié par moi : `ee84d6ec…` est bien l'arbre `orchestrator/` de `a41b7b50` = `origin/main` de la copie, résolution unique ; le paquet n'ajoute que des fichiers et s'applique à tout commit de même arbre `orchestrator/`. Déclaré par lui. | Aucune ; la base est la bonne. |
| 6 | mineur (méthode) | idem | en-tête, §1 | Un heredoc a servi une fois à passer un script qui écrivait un brouillon (règle « jamais de heredoc pour écrire un fichier ») ; premier commit local modifié sur place avant livraison, jamais poussé ; quatre commandes git et un `sleep` refusés par la garde d'isolement, découpés comme elle le demandait. Déclarés ; sans effet sur le livrable, vérifié par le différentiel recalculé. | Aucune sur le livrable. |
| 7 | mineur (information) | `suite-base-a41b7b50-remplacement-juge-v1.txt` | dernière ligne | 18 échecs à la base chez le développeur, dus aux deux suites jouées en même temps (bac). Rejouée seule par moi : **7 failed, 1355 passed** ; les 7 sont ceux de la tête. Le compte livré n'est pas faux mais pas probant seul ; le mien l'est. | Aucune ; cette pièce fait foi pour la base seule. |
| 8 | mineur (information, hors périmètre) | `orchestrator/essais/test_juges_idees_v2.py` | 1719 | Échec transitoire d'un sous-cas de `LanceurCheminReel.test_artefacts_du_chemin_reel` dans ma première passe complète à la tête ; passe seul (tête et base) et à la deuxième passe. Aucun lien avec les fichiers neufs (0 référence). Essai existant dépendant de l'ordre ou d'un état. | Hors de cette livraison ; à signaler au compte de l'organisme (essai à rendre indépendant de l'ordre). |
| 9 | mineur (information) | `orchestrator/pole/bras_remplacement_juge_v1.py` | 159 | `famille_par_juge[j]` lève `KeyError` pour un juge absent de la table : même contrat que `lecture_auto_preference` de la v2 (l. 926) ; la table est construite à partir de `noyau/modeles.json["par_juge"]`, qui porte tous les juges d'une course saine. | Aucune. |
| 10 | mineur (information) | `orchestrator/pole/outils.py` | 157-165 | Tout manifeste écrit depuis l'arbre `3c6cff30…` porte une entrée de plus dans `code_sha256` (`bras_remplacement_juge_v1.py`), avec ou sans option : effet de tout fichier neuf dans `pole/`, déclaré par le développeur (rapport 6.8) ; l'identité « sans option » est bien éprouvée dans le même arbre. | Aucune ; à savoir pour comparer des manifestes de la course et du bras. |
| 11 | mineur (information) | `orchestrator/pole/bras_remplacement_juge_v1.py` | 260-261, 323-331 | Quand le juge remplacé échoue après envoi, `lecture-sans-bras.json` porte la mention « juge externe joué avec un autre modèle » bien qu'aucune note du juge ne soit agrégée : le remplacement a été joué (dépense), la mention est juste ; `remplacements[].applique` et le manifeste disent le reste. | Aucune. |
| 12 | mineur (information) | `orchestrator/demonstrations/ideation_v2.py` | — | Le lanceur de démonstration ne transmet pas l'option (inchangé, R12) : la relance doit appeler `pole.bras_remplacement_juge_v1.executer_bras_differe` directement, plafond par session donné au **modèle joué**, exceptions de `pole.ideation_v2` attrapées ; rien n'a tourné avec une vraie commande ni le modèle joué. Déclaré (rapport §7). | Lanceur de la relance (à sa charge, spécification « Pièces neuves côté relance ») : exiger que la commande rende `modele_servi` égal au modèle joué. |

Aucun constat bloquant, aucun constat majeur.

## 6. Ce que la relance peut épingler (après ce verdict)

- Commit de l'orchestrateur `0861800260e33224a71f48b111e72ac04288d3cb` sur la base `a41b7b50f7c64ce488c120bb89ad3d25fb1dd1cb` ; arbre `orchestrator/` `3c6cff30671bb5bdf6b7f461c167db48e32c5d6d` ; `orchestrator/pole` `55cae9e0effc76e5201ad47c5f8b3bd9d055609a`.
- `pole/bras_remplacement_juge_v1.py` `2efd6b0874e8bbfa58a0c53a5099f46da51318c6807c90909b8cf58dfe90866a` ; `pole/ideation_v2.py` `67d2ad3591b21601ece4101154138f532ba519024761beb8c9738181f8f3fefc` (inchangé).
- Le bloc gelé provisoire de `empreintes-orchestrateur-remplacement-juge-v1.txt` peut être figé tel quel ; les constats 1 et 2 ne l'imposent pas (ils ne touchent ni un verrou ni le cas d'usage) et se prendraient dans une version neuve ultérieure si elle a lieu.

## Verdict

Conforme.

La version neuve fait ce que la spécification demande aux points 1 à 6, sous des noms neufs seulement (trois ajouts, aucun fichier existant modifié), sur la base déclarée ; sans option elle appelle la v2 elle-même ; les verrous sont la copie exacte de la v2 ; la garde CL35-04 est conservée hors remplacement déclaré ; essais et banc de mutations rejoués par moi aux mêmes décomptes ; aucun échec neuf dans la suite complète (base rejouée seule) ; aucune dépense possible. Les douze constats sont mineurs ou informatifs ; aucun n'exige de correction avant l'épinglage. La ligne de GO et la vérification de la référence de GO contre le registre reviennent à la mère et au lanceur de la relance.
