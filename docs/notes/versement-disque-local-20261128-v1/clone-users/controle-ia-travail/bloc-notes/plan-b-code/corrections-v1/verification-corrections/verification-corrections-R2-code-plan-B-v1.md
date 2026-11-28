# Vérification des corrections du code du plan B des juges (T0.5) et du brouillon 4 — v1

## Verdict : prêt après corrections

- Les corrections D-1 à D-15 sont faites et justes, au code et au texte. Les 27 constats des trois relectures R2 sont traités. Aucun défaut de lecture n'a été trouvé : aucune issue ne peut plus lire « défaut » sur une grandeur illisible, et chaque garde neuve arrête sur son artefact.
- Les 389 tests du plan B passent. L'annexe A du brouillon 4 est `RS1.txt`, octet pour octet (`b1e3e003…`). Les lignes de citation et la table « Configuration » du brouillon 4 passent les gardes du lanceur et du lecteur.
- Mutants de la relecture 3 rejoués : 61, dont 60 tués. Les 21 survivants de la relecture 3 sont tous tués. Un seul survit : RQ-17 (témoin sans graine). Il était tué en relecture 3, mais par hasard (VCB-01).
- Restent cinq corrections mineures, sans effet sur la lecture : quatre trous de tests au sens de R5 (VCB-01 à VCB-04) et une phrase de texte (VCB-05). Ce sont surtout des tests à ajouter ; une seule garde change de place (VCB-02). Aucune n'est bloquante, mais R5 est une règle gelée : elles sont à faire avant le commit du code.

## Ce qui a été lu et fait

- Vérificateur neuf (R2). Je n'ai écrit ni le texte, ni le code, ni les tests, ni les corrections, ni les relectures.
- Lus en entier : le brouillon 4 (`528a2386…`, 663 lignes) ; le traitement ; les notes des corrections ; les trois rapports R2 (`1ef2d27f…`, `5f21fc37…`, `d413cfdd…`) ; les quatre modules neufs ; les différences des cinq fichiers de tests avec `corrections-v1/originaux/` ; les sondes de la relecture 3. Différence mot à mot entre les brouillons 3 et 4 : `diff-mots-b3-b4.txt`.
- Empreintes recalculées, égales à la section 7 des notes des corrections : `rubrique_simplifiee.py` `beeb1017…`, `juges_simplifies.py` `01a4e0c4…`, `requalifier_juges.py` `75346dc0…`, `lire_requalification.py` `440a9778…`, `RS1.txt` `b1e3e003…`, `index.json` `c61df3db…`, `LISEZMOI.md` `00e6011e…`. Tests : `f925fbfc…`, `403e1461…`, `fa39c2c3…`, `a9cac945…`, `0c1ea90f…`.
- Modules gelés égaux à `c63d4f1` (`git diff --quiet`, code 0). Aucun test retiré : la seule fonction disparue est renommée (`test_limite_constatee_…` devient `test_limite_ecrite_…`, cinq formes gardées, vingt ajoutées). Les lignes retirées des tests sont des docstrings, des signatures mises à jour (D-13) et l'assertion d'écart connu de D-1, devenue une égalité.
- Tous mes essais sont sous `corrections-v1/verification-corrections/`. Le clone n'a reçu aucune écriture. Lancements avec `python -B`, `-p no:cacheprovider` et `--basetemp` dans mon dossier. Les dossiers de travail des mutants (copies de `src/` et `tests/`) ont été effacés après usage ; leurs résultats restent.
- Base des mutants : `rsync` n'existe pas dans ce conteneur. `relecture-R2-3/base/src` et `base/tests` ont été rafraîchis par effacement puis `cp -a` depuis le clone, ce qui a le même effet que `rsync --delete`. `diff -r` donne une égalité exacte avec le clone. Aucune copie neuve de la base n'a été faite.

## Résultats mécaniques

| contrôle | résultat | pièce |
|---|---|---|
| tests du plan B, clone | `389 passed in 179.11s` (code 0), aucun `__pycache__` laissé | `pytest-plan-b-verification.txt` |
| témoin des mutants (base rafraîchie, non mutée) | `389 passed in 284.08s` | `mutants/journal-temoin.txt` |
| annexe A du brouillon 4 : commande de `LISEZMOI.md` sur une copie nommée `T0.5-plan-B-juges-v1.md` | `b1e3e003daf2c64bb317fe5623495f73ec25e7a703c5d799ceb1ab8c1eb042e7` | `lisezmoi/` |
| annexe A, extraction indépendante (octets) | une seule ligne de début (l. 584), une seule ligne de fin (l. 641) ; 3 966 octets ; égal octet pour octet à `RS1.txt` ; ASCII, sans retour chariot ni espace de fin | `annexe_a_brouillon4.py`, `sortie-annexe-a-brouillon4.txt` |
| annexe A, `exiger_annexe_a_egale_a_rs1` | cas sain `b1e3e003…` ; artefacts : un caractère, retrait manquant, ligne vide de plus : arrêt | idem |
| annexe A, brouillon 3 et brouillon 4 | blocs identiques (même sha256) | — |
| table « Configuration » | 50 clés, ordre de `rq.CLES` ; `exiger_config_planb` l'accepte ; aucun écart à `lr.CONSTANTES_CONFIG` ; `lr.exiger_config_de_l_etape` l'accepte ; clés égales au pilote ; empreinte canonique `8ff777cf…`, égale à celle du traitement | `controle_citations_config_b4.py`, `sortie-citations-config-b4.txt` |
| lignes de citation | texte tel quel : refusé par les deux gardes (marqueurs). Copie aux marqueurs remplis : chaque intitulé une seule fois ; `exiger_citations_planb` et `exiger_code_cite` passent, valeurs recalculées sur les fichiers du clone ; artefacts « résumé cité deux fois » et « invite autre » : arrêt. Copie effacée après l'essai | idem |
| sondes originales de la relecture 3, sur le code corrigé | `16 passed, 1 failed` : l'échec est la signature de `repere_demi_simple` changée par D-13 ; la substance est versée (`test_roles_du_repere_et_de_l_ancrage_et_gardes_du_repere`) | `mutants/sortie-sondes-originales-sur-code-corrige.txt` |
| clone à la fin | `git status --short` : les 10 entrées non suivies ; `git diff --stat HEAD` : vide ; aucun `__pycache__` | — |

## Mutants

Pilotes copiés dans `mutants/`. Seuls trois points diffèrent des originaux : le chemin de la base (absolu), `--basetemp` par travailleur et `TMPDIR` dans mon dossier. La liste est celle de la relecture 3, plus deux blocs ajoutés à la fin : six mutants « portés » et les mutants neufs du vérificateur. Tests ciblés et `-x`, comme dans la relecture 3. Résultats : `mutants/lot-principal/` et `mutants/lot-vcb/`.

**Liste de la relecture 3 (62 entrées).**
- LR-13 est sans objet, comme en relecture 3.
- 55 mutants s'appliquent tels quels.
- 6 ne trouvent plus leur ancien texte, car le code a changé : RS-01, RQ-10, RQ-12, RQ-13, RQ-15, RQ-23. Ils sont portés à l'identique sur le code corrigé (`-p` : même défaut, même module, mêmes tests).
- Bilan : **61 rejoués, 60 tués, 1 survivant (RQ-17)**.
- Les 21 survivants de la relecture 3 sont tous tués : RQ-01 à RQ-09, RQ-10b, RQ-11, RQ-12p, RQ-13p, RQ-15p, RQ-21, RQ-23b, RQ-24, LR-01 à LR-04.
- RQ-17 (`torch.manual_seed` retiré du témoin) survit : `246 passed`. Sa mise à mort en relecture 3 tenait au hasard (VCB-01).

**Mutants neufs du vérificateur, écrits contre les corrections (17).**
- 6 tués : VCB-M04 (clés comparées sans leur ordre), VCB-M05 (décalage de D1 non exigé), VCB-M06 (R_S illisible non classé), VCB-M07 (grandeur illisible mise en réserve), VCB-M08 (descriptif D-5 sur `\w`), VCB-M09 (passes en demi-précision gardées) et VCB-M10 (D1 au palier de production, décalage consigné 0).
- 11 survivent : VCB-M01 (VCB-02) ; VCB-M02 et VCB-M03 (VCB-04) ; VCB-M14 à VCB-M17 (VCB-03) ; VCB-M11 à VCB-M13 (VCB-07, équivalents sur le brouillon 4).

## Constats (le plus grave d'abord)

| id | gravité | où | problème | correction |
|---|---|---|---|---|
| VCB-01 | mineur (R5, R9) | `tests/test_plan_b_requalifier.py`, `test_temoin_configuration_remplacee_cas_sain_et_artefact`, l. 1529 ; `requalifier_juges.py`, `appel_temoin`, l. 1003 | La « graine par appel » du témoin (texte, l. 151) n'est tenue par aucun test. La seule assertion, `appel == rq.appel_temoin(…)`, compare des rangées réduites à la longueur et aux drapeaux. Sur le jouet du témoin, chaque appel rend `[(6, True), (6, True)]`, avec ou sans graine. Le mutant RQ-17 survit (`246 passed`). Rejoué seul, il passe aussi (`1 passed`). Il était tué en relecture 3 par l'état du générateur laissé par les tests précédents ; les tests ajoutés ont changé cet état. Reproduction : `mutants/rejouer_rq17.py`, sortie `mutants/sortie-rq17.txt` (quatre appels sans graine, rangées identiques). | Tester la graine elle-même. Deux voies : un espion sur `torch.manual_seed` qui exige l'appel avec la graine de la clé, avant `generate` ; ou la comparaison des jetons générés, capturés en enveloppant `modele.generate`, entre deux appels (égaux) et avec une autre graine (différents). Tuer RQ-17 et le noter. |
| VCB-02 | mineur (R5 ; texte face au code) | `lire_requalification.py`, l. 1042-1044 ; texte l. 302, l. 339, l. 504 | Le texte fait de « `lot_juge` absent » un arrêt de la lecture, sans condition. Le code ne lit `lot_juge` que si un fichier du rejeu de J est écrit. De plus, aucun test n'éprouve l'artefact. Le mutant VCB-M01 (`m_b["config"].get("lot_juge", 8)`) survit : `130 passed`. Sans conséquence au réel, car le lanceur exige `lot_juge` égal au pilote (`CLES_EGALES_AU_PILOTE`), et la configuration est scellée dans le manifeste. | Exiger `lot_juge` (entier positif) dans `exiger_config_de_l_etape`, avant toute lecture, puis le passer à `lots_du_rejeu`. Ajouter un test d'artefact : configuration du run sans `lot_juge`, arrêt, rien n'est écrit. Le cas sain est la lecture d'équivalence. |
| VCB-03 | mineur (R5 ; texte face aux tests) | `tests/test_plan_b_requalifier.py`, `test_gardes_de_citation_cas_sain_et_artefacts` ; `requalifier_juges.py`, `executer`, l. 426-431 ; texte l. 533 | Le texte annonce, pour les lignes de citation, un artefact par intitulé : « chaque intitulé absent, répété avec deux valeurs, ou différent ». Le test en éprouve cinq. Si l'on retire de `attendus` « épisodes du pilote », « tâches », « manifeste des notations » ou « run du pilote », la citation reste exigée mais n'est plus comparée, et les mutants survivent : VCB-M14 à M17, `246 passed` chacun. Le code est juste : sur une copie remplie du brouillon 4, toutes les valeurs ont été comparées (`sortie-citations-config-b4.txt`). | Ajouter une ligne de paramètre « valeur différente » pour chaque intitulé de `CITATIONS` (les dix et les notations par juge), plus l'entropie absente. Sinon, écrire au texte ce que le test couvre vraiment. |
| VCB-04 | mineur (R5) | `lire_requalification.py`, `lots_du_rejeu`, l. 740-741 ; `tests/test_plan_b_lecteur.py`, `_h4` et `test_tirage_des_lots_recalcule_cas_sain_et_artefacts` | D-14 veut un recalcul du cadre « sans le code du lanceur », mais les deux règles propres au lecteur n'ont pas d'artefact. Dans les données du lecteur, toute réponse tronquée est au plafond, et le dernier lot incomplet n'en porte pas. Deux mutants survivent (`130 passed` chacun) : VCB-M02 (cadre sans la condition du plafond) et VCB-M03 (cadre avec le dernier lot incomplet). Au réel, M02 est équivalent (une réponse ne se tronque qu'au plafond). M03 ferait arrêter la lecture à tort (le dernier lot du 8B, de 4 rangées, va au plafond) ; ce n'est jamais une acceptation silencieuse. | Ajouter deux artefacts au test du tirage : une notation H.4 « tronquée » sous le plafond, hors du cadre ; un dernier lot incomplet porteur d'une tronquée, exclu. Comparer au cadre attendu écrit en clair, et au cadre du lanceur (`rq.cadre_du_rejeu`). |
| VCB-05 | mineur (texte ; point ouvert 1 du traitement) | texte l. 144 (et l. 259) ; `requalifier_juges.py`, `ancrage_noyaux`, l. 740-747 ; `test_roles_du_repere_et_de_l_ancrage_et_gardes_du_repere` | Le code et un test fixent les rôles de l'ancrage : numérateur ‖a_défaut − a_math‖, dénominateur ‖a_math‖, la passe au noyau « math » servant de référence. Le texte dit seulement « entre cette passe et sa passe … au noyau par défaut ». R_S entre dans le seuil (1e-3 et 1e-2/3) : c'est une définition de métrique, qui doit figurer au préenregistrement (R1), comme les rôles du repère (R2-03). | Écrire les rôles à la l. 144, comme au repère. Cela change une phrase de métrique : décision de la session (point ouvert 1), avant le scellement. |
| VCB-06 | information (point ouvert 2) | texte « Dépassement », l. 264 ; `requalifier_juges.py`, l. 25, l. 869, l. 874, l. 1038 | Le code contrôle aussi l'échéance avant la conversion et le repère, avant l'ancrage et avant chaque rechargement du témoin. Le texte ne nomme que « avant chaque lot et avant chaque appel du témoin ». La docstring du lanceur (l. 25) omet le rechargement. C'est plus strict, sans effet sur la borne de dépassement. | Écrire ces points de contrôle au « Dépassement » ; compléter la docstring. |
| VCB-07 | information | `rubrique_simplifiee.py`, `annexe_a_du_texte`, l. 108-114 | La règle « première ligne de début, dernière ligne de fin » n'est éprouvée par aucun texte qui porterait deux lignes de début ou de fin. Les mutants VCB-M11, M12 et M13 survivent. Ils sont équivalents sur le brouillon 4 : une seule ligne de chaque forme, vérifiée, et le texte l'écrit (l. 582). La règle du code est la plus stricte : avec une fin en double, l'extraction diffère de `RS1.txt`, donc arrêt. | Facultatif : un artefact avec une seconde ligne de fin après l'annexe (arrêt attendu). |
| VCB-08 | information (rédaction) | `lire_requalification.py`, docstring l. 9-12 et `bilan_chemin` l. 725-728 ; `tests/test_plan_b_rubrique_simplifiee.py`, docstring de `annexe_a_comme_au_texte` | (a) La docstring du lecteur ne liste pas, dans « ce qu'il calcule lui-même », le tirage des lots, l'extraction de l'annexe A et l'exigence des décalages. Le texte (l. 301) les liste, et les gardes de la docstring (l. 20-27) aussi. (b) Un R_S illisible à une couche sans dépassement donne la réserve « ancrage au-dessus de 1e-3 ». La lecture est juste, conforme à D-1 : « fidèle », réserve, et l'audit NaN suspend la lecture ; mais le libellé dit « au-dessus » pour un NaN. (c) La docstring de l'aide de test cite les lignes du brouillon 3. | Retouches de libellé, sans effet. Pour (b), écrire par exemple « ancrage au-dessus de 1e-3 ou illisible ». |

## Constats des trois relectures : correction faite et juste ?

| constat | code | texte (brouillon 4) | test ou contrôle qui le prouve | jugement |
|---|---|---|---|---|
| R2-01 (D-1) | `lr.classer_depassement` et `_illisible` ; `bilan_chemin` (motif, « non concluant (contrôles) ») ; `rq.lire_palier_chemin` aligné | l. 99, 178, 197, 437, 473, 534 | grille NaN : égalité des deux calculs ; artefacts G_S, maximum de zone, R_S ; de bout en bout : lecture combinée « non concluant », PB8 « non concluant », RS1 retenue, audit NaN gardé ; VCB-M06 et VCB-M07 tués | fait, juste |
| R2-02 (D-9) | — | l. 528-534 | huit gardes avec artefact ; RQ-06, RQ-07, RQ-08 et LR-01 à LR-04 tués | fait |
| R2-03 (D-15) | inchangé (juste : `ecarts_par_jeton(a_demi, a32)` = ‖a_demi − a_simple‖ / ‖a_simple‖) | l. 143, 259, 386, 517 ; VC-15 clos | rôles à 0,5 ; RQ-12p tué | fait |
| R2-04 | inchangé (déjà exigé) | l. 9-31, 329-382, 388, 406, 519 | mon essai : citations et configuration (ci-dessus) | fait ; voir VCB-03 pour les tests |
| R2-05 (D-13) | ancrage choisi avant le repère ; passes rendues | l. 259, 294, 531 | test de mémoire ; VCB-M09 tué | fait, juste |
| R2-06 (D-3) | `lr.table_a`, ligne « sonde d'audit fausse » | l. 133, 195, 418 | ligne « sonde-fausse » de la table A | fait, juste |
| R2-07 (D-14) | `lots_du_rejeu`, `exiger_lots_du_rejeu` | l. 297, 301-306, 339, 504 | artefacts du tirage ; VCB-M04 tué | fait ; voir VCB-02 et VCB-04 |
| R2-08 (D-2) | en-tête l. 1065 ; docstring l. 33-47, divergences nommées | l. 517 | égalité des deux calculs (intégration) | fait |
| R2-09 (D-5) | docstring de `rs` ; `_suite_avec_chiffre` | l. 111, 121, 126 | 25 formes de la limite ; descriptif dans les deux sens | fait, juste |
| R2-10 | — | l. 282, 294 (2 × 13 Go + 32 Go ; arithmétique vérifiée) | — | fait ; pic à mesurer aux bancs (chaîne) |
| R2-11 | — | — | — | sans objet |
| R2-2-01 (R-225) | inchangé | l. 36, 111, 121, 126, 200, 382, 522, 568, 576, annexe B | `test_seconds_nombres_invalides_r225` | fait |
| R2-2-02 (D-4) | `_suite` : `[+\-−]?` | l. 111, 200, 522, annexe B | « 3 to -4 », « 3 to −4 », « 3 - +4 », « 3, -1 », « 3, −1 », « 3 and +4 » ; motif direct ; RS-01p tué | fait, juste |
| R2-2-03 (D-5) | `lues_suite_avec_chiffre`, compté et rapporté par le lecteur | l. 111, 126, 269, 306 | tests de la limite et du descriptif ; recalcul au lecteur (compte altéré : arrêt) | fait, juste |
| R2-2-04 (D-6) | `annexe_a_du_texte`, `exiger_annexe_a_egale_a_rs1` ; lanceur avant le manifeste ; lecteur | l. 201, 255, 302, 501, 504, 515, 523, 582 | cas sain et artefacts (T-rs, T-rq, T-lr) ; mon essai sur le brouillon 4 | fait, juste |
| R2-2-05 | `index.json` inchangé (`c61df3db…`) | l. 26, 392 | — | fait |
| R2-2-06 (D-7) | docstring de `_a_une_suite` | l. 121, 126 | colonne « suivie de texte » | fait |
| R2-2-07 (D-8) | — | l. 522 | `test_motif_de_ligne_lie_au_motif_gele_de_h4` | fait |
| R3-01 (D-10) | `decalages_passes` consignés ; le lecteur exige 0 au chemin et `decalage_d1` à D1 | l. 138, 145, 149, 269, 304, 504, 535 | espion du rejeu ; reproduction 4 sur 4 ; lectures attendues du run jouet ; RQ-09, RQ-10b, RQ-10p, RQ-23b, RQ-23p, RQ-24 et VCB-M10 tués | fait, juste |
| R3-02 (D-11) | — | l. 528 | espion sur `noyau` ; rôles ; RQ-11, RQ-12p, RQ-13p tués | fait ; voir VCB-05 pour le texte |
| R3-03 (D-9) | — | l. 533 | sondes versées ; docstring corrigée et cas ajouté ; RQ-01, RQ-04 à RQ-08 tués | fait |
| R3-04 (D-9) | — | l. 302, 534 | LR-01 à LR-04 tués | fait |
| R3-05 (D-12) | — | l. 528 | RQ-15p tué | fait |
| R3-06 (D-9) | — | l. 529, 533 | une ligne par sous-garde (liste relue, complète) ; RQ-02, RQ-03, RQ-21 tués | fait |
| R3-07 | (a) D-5 ; (b) D-4 | l. 111, 121, 382 | idem | fait |
| R3-08 | fermé par D-1 | l. 437 | égalité | fait |
| R3-09 | — | — | — | sans objet ; RQ-17 n'est plus tué (VCB-01) |

## Texte face au code : phrases normatives neuves ou changées du brouillon 4

Chaque phrase normative neuve ou changée a sa ligne de code. Les seuls écarts sont VCB-02 (`lot_juge` exigé seulement sous condition), VCB-05 (rôles de l'ancrage absents du texte) et VCB-06 (contrôles d'échéance du code non écrits).

| phrase du brouillon 4 | code |
|---|---|
| citations sur une ligne, une valeur, marqueurs refusés (l. 9-31) | `rq.CITATIONS`, `NOTATIONS_CITEES`, `exiger_citations_planb` ; `COMMIT_CITE`, `TACHES_CITEES`, `ENTROPIE_CITEE` (gelés) |
| étape 5 : séparateurs, chiffre éventuellement signé, limite (b) (l. 111) | `rs._suite`, `controle_suite`, docstring l. 30-40 |
| « ne choisit jamais entre deux nombres reliés par l'un des séparateurs listés » (l. 121) | `rs` docstring l. 39-40 ; test de la limite |
| descriptifs `lues_suivies_de_texte` et `lues_suite_avec_chiffre` (l. 126) | `rs._a_une_suite` (`\w`), `rs._suite_avec_chiffre` (`\d`), `lire_notes_rs1` ; `lr.relire_notations_rs1` |
| sonde fausse de la garde en ligne lue à la table A (l. 133, 195, 418) | `lr.table_a`, l. 505-507 |
| production : décalage consigné, rapporté, non exigé (l. 138) | `rq._rejouer`, l. 836-852 ; `lr._rapportes(demi, …)` |
| repère : fonctions gelées, agrégation, rôles (l. 143, 259) | `rq.repere_demi_simple` ; lignes gelées citées vérifiées (`activations.py`, l. 99 et 124 ; `validation_reelle.py`, l. 526-541) |
| ancrage : plus longue rangée de L1, choisie avant le repère (l. 144, 259) | `rq._rejouer`, l. 866-867 |
| chemin et D1 : décalages consignés et exigés (l. 145, 149, 304, 504) | `rq._rejouer`, l. 878-900 ; `lr.bilan_chemin`, l. 636-641 |
| NaN : classe « illisible », jamais « défaut » (l. 99, 178, 197, 433, 437, 473) | `lr.classer_depassement`, `bilan_chemin` l. 703-706 ; `rq.classer_depassement`, `lire_palier_chemin` |
| annexe A : garde au lanceur et au lecteur (l. 201, 255, 302, 501, 504, 582) | `rs.annexe_a_du_texte`, `exiger_annexe_a_egale_a_rs1` ; `rq.executer` l. 434 ; `lr.lire_requalification` l. 998 |
| tirage des lots recalculé, comparé dans l'ordre ; cadre de moins de 3 lots (l. 297, 301, 304, 504) | `lr.lots_du_rejeu`, `exiger_lots_du_rejeu`, l. 1041-1045 |
| `lot_juge` lu par le lecteur ; absent : arrêt (l. 302, 339, 504) | l. 1043, seulement si un fichier du rejeu est écrit (VCB-02) |
| champs des fichiers (l. 269, 306) | `decalages_passes` (l. 852, 897, 899) ; `annexe_a` (état, résumé, partiel d'`arret.json` ; `lecture-planb.json`) ; `rejeu.<J>.tirage` ; `lues_suite_avec_chiffre` |
| mémoire du repère (l. 294) | `repere_demi_simple` (`pop`, seule passe de l'ancrage gardée) |
| liste d'arrêt « Pendant le run » : rangée d'ancrage absente ou en double, passe absente (l. 502) | `repere_demi_simple`, l. 715-721 |
| point 4 : second calcul gardé, divergences nommées (l. 517) | docstring de `rq`, l. 33-47 ; en-tête l. 1065 |
| tests listés (l. 521-535) | présents, sauf la couverture « chaque intitulé » des citations (VCB-03) |

Inversement, le code corrigé ne porte aucune règle neuve absente du texte, sauf les rôles de l'ancrage (VCB-05) et les contrôles d'échéance supplémentaires (VCB-06). Deux retraits n'en sont pas : l'étiquette `palier` des lignes de progression et le retrait du `tirage` des champs rapportés sont de forme.

## Points ouverts du traitement

- Point 1 (rôles de l'ancrage) : je recommande de les écrire (VCB-05).
- Point 2 (échéances) : je recommande de les écrire (VCB-06).
- Point 3 (décalage du palier de production non exigé) : le texte l'écrit tel quel (l. 138). Le lanceur est tenu par l'espion (VCB-M10 tué). Aucune garde de plus n'est nécessaire.
- Points 4 à 8 : chaîne de lancement, bancs, devis et versement, hors de cette vérification.

## Pièces (sous `corrections-v1/verification-corrections/`)

| fichier | sha256 |
|---|---|
| `pytest-plan-b-verification.txt` | `9dad74b9d66a5fa6edebb609955c375cc50a4d0b216274722510fb07b754dff1` |
| `annexe_a_brouillon4.py` | `d094777baf672b55e114d22f67c7054383bb0fac9f5651a69b1e586a78bcdb33` |
| `sortie-annexe-a-brouillon4.txt` | `3bcb82926f96cff2cf5c908fcc7ad549f48cce5f1a5d917be8fcf29d4675f2c2` |
| `controle_citations_config_b4.py` | `53ab69e494cc50728890f4f5d038d9e8e9ea851764d053fa1684f3eb1078f530` |
| `sortie-citations-config-b4.txt` | `0ae11704582e3649b8759a4175d62367f929160b9b3b984de62010e7da5f4875` |
| `diff-mots-b3-b4.txt` | `93eb78fae8646560c515bfe833f2a3319679b06509d7ec1f398522779f3f6941` |
| `lisezmoi/T0.5-plan-B-juges-v1.md` (copie exacte du brouillon 4) | `528a238667a7a5220a207982487682f677a1687f2ecbea1beac6ae247e2225b1` |
| `mutants/liste_mutants.py` (liste de la relecture 3, plus les blocs portés et VCB) | `5747332534241b99c553757fb823b28f622111724b34f727346b98703ef7b0e9` |
| `mutants/muter.py` | `6b6886fad127a96312515364b1d236b4c0620858e0b827ca12006f1d8a9f2b31` |
| `mutants/muter_sondes.py` (chemins seulement) | `513904a63a142741faf1e9debc3a894576d731063e972f321a85c461670cb5fb` |
| `mutants/temoin.py`, `journal-temoin.txt` | `78fa7d4b…`, `8ab9d790…` |
| `mutants/rejouer_rq17.py`, `sortie-rq17.txt` | `968eebbb…`, `9a3e8ee3…` |
| `mutants/sortie-sondes-originales-sur-code-corrige.txt` | `99f4f1d7…` |
| `mutants/lot-principal/resultats-w0…w3.jsonl` | `d8b38d7a…`, `7af63c7c…`, `cf99ab98…`, `e056d153…` |
| `mutants/lot-vcb/resultats-w0…w3.jsonl` | `3a66c51c…`, `b05a8182…`, `94ef0374…`, `6a20bfa4…` |

Aucun commit, aucune poussée, aucun service payant, aucune commande Vast.ai, aucun modèle réel.
