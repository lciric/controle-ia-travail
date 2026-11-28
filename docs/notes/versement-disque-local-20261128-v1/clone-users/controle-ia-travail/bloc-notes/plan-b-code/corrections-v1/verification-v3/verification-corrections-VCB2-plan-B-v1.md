# Vérification des corrections VCB2 du code du plan B des juges (T0.5) et du brouillon 6 — v1

## Verdict : prêt pour la chaîne de lancement

- Les corrections de VCB2-01 à VCB2-05 sont faites et justes, au code, aux tests et au texte. La garde de VCB-b et la garde « une seule valeur par intitulé » aussi. Aucune lecture ne change. Aucun test n'est retiré ni affaibli. Les modules gelés sont intacts.
- Les 423 tests du plan B passent sur le clone. L'annexe A du brouillon 6 est `RS1.txt`, octet pour octet (`b1e3e003…`). Les lignes de citation et la table « Configuration » passent les gardes du lanceur et du lecteur, sur une copie aux six marqueurs remplis de valeurs factices de bonne forme.
- Les 38 mutants nommés sont rejoués : 37 sont tués, 1 est introuvable (VCB-M01, dont le port VCB-M01p est tué) ; aucun ne survit. VCB2-M01 à VCB2-M04 meurent sur les tests neufs, pour la raison écrite. RQ-17 meurt sur l'espion, dans ma rejoue et dans quatre ordres.
- J'ai écrit 12 mutants neufs : 10 sont tués, 2 survivent. Les deux survivants sont équivalents au réel (VCB3-01, VCB3-02).
- Six constats, tous d'information. Aucun ne bloque, aucun ne demande d'action avant le commit du code. Les plus utiles : un test du plafond `max_nouveaux_juge` réellement employé, symétrique de VCB2-02 (VCB3-01) ; une phrase de l'échéance globale et une mesure aux bancs (VCB3-03).

## Ce qui a été lu et fait

- Je suis un vérificateur neuf (R2). Je n'ai écrit ni le texte, ni le code, ni les tests, ni aucune correction, ni aucune relecture ou vérification précédente.
- J'ai lu en entier :
  - le rapport de la vérification précédente (`verification-v2/verification-corrections-VCB-plan-B-v1.md`, `95926f9c…`) ;
  - les notes des corrections VCB2 (`NOTES-CORRECTIONS-VCB2-plan-b-v1.md`, `8a8cd0a9…`) ;
  - la section « VCB2 » du traitement et ses points ouverts (`traitement-R2-code-plan-B-v1.md`, `324c56ca…`). Depuis `a4a243d0…`, seule cette section est ajoutée (l. 109-150) ; rien n'est retiré ;
  - la différence ligne à ligne entre les brouillons 5 et 6 (23 blocs, tous lus) ;
  - les différences du code et des tests avec `corrections-v1/originaux-vcb2/`.
- J'ai aussi lu, dans le brouillon 6 : en-tête et citations, « Ordre des phases », « Dépassement », « Chaîne des limites de temps », « Lecture », « Configuration », « Avant le scellement », « Liste d'arrêt », « Code à écrire et tests », « Transparence », « Contre-lecture », annexe A. Au lanceur : `executer`, `_avant` et ses sept appels, `_requalifier`, `_rejouer`, `_temoins`, `exiger_config_planb`, `exiger_citations_planb`. Au lecteur : `exiger_config_de_l_etape`, `lire_requalification`, `lots_du_rejeu`, `exiger_lots_du_rejeu`, `relire_notations_rs1`.
- Empreintes recalculées. Elles sont égales à celles des notes VCB2 :
  - brouillon 5 : `1d6f1932…`, intact ; brouillon 6 : `4a4184c0…`, 669 lignes ;
  - `lire_requalification.py` : `f104805e…` (avant : `4ee817c6…`) ; `requalifier_juges.py` `a0b1d15f…`, `rubrique_simplifiee.py` `beeb1017…`, `juges_simplifies.py` `01a4e0c4…` : inchangés ;
  - tests : requalifier `620d8f4d…`, lecteur `485687bd…` ; rubrique `c04c1735…`, juges `403e1461…`, intégration `0c1ea90f…` : inchangés ;
  - `RS1.txt` `b1e3e003…`, `index.json` `c61df3db…`, `LISEZMOI.md` `00e6011e…` ; `travail-b6/` : construction `629e9915…`, contrôles `a3b572f8…`, sortie `6bd3097b…`.
- Aucun test n'est retiré. J'ai comparé les fonctions de module par `ast` : aucune ne disparaît ; aucune fonction existante ne change de corps (docstrings exclues). Sont ajoutés : deux aides et trois tests au module du lanceur, deux tests au module du lecteur (423 tests, 413 + 10). Lignes retirées des tests : deux lignes de docstring de module, réécrites. Au lecteur, seul le corps de `exiger_config_de_l_etape` change (trois lignes) ; la ligne `plafond = …` reste, avec un commentaire. Toutes les lignes neuves ont 120 caractères au plus.
- Le clone n'a reçu aucune écriture : hors `.git`, aucun fichier n'y est plus récent que mon fichier de départ (07:25:58 UTC). Les tests, les mutants, les contrôles et l'essai du témoin ont tourné sous `nice -n 19`, avec `-B` ; pytest avec `-p no:cacheprovider`, `--basetemp` et `TMPDIR` dans `verification-v3/`. Quatre petits scripts d'édition de mes propres fichiers ont tourné avec `python3`, sans `nice` ; aucun `__pycache__` n'est laissé.
- Les copies de mutants sont effacées après usage. `rm -r` n'efface que les liens, jamais leurs cibles : le clone garde ses 502 entrées de profondeur 2.
- Je n'ai ouvert aucune donnée scellée, sauf pour les contrôles mécaniques : des empreintes de fichiers, la configuration du manifeste du pilote et `prereg/T0.5-pilote-config-v1.json`. Aucun contenu n'est affiché. L'essai du témoin n'emploie que le modèle jouet.

## Résultats mécaniques

| contrôle | résultat | pièce |
|---|---|---|
| tests du plan B, clone | `423 passed in 269.06s (0:04:29)`, code 0 ; aucun `__pycache__` | `pytest-plan-b-v3.txt` |
| témoin des mutants (copie non mutée) | `423 passed in 278.28s (0:04:38)` | `mutants/journal-temoin.txt` |
| annexe A, extraction indépendante (octets) | une ligne de début (l. 590) et une ligne de fin (l. 647), seules de leur forme dans le texte ; 3 966 octets ; égale à `RS1.txt`, octet pour octet ; bloc égal à celui du brouillon 5 ; dans la section « Annexe A », seule l'introduction change | `controle_brouillon6_v3.py`, `sortie-controle-brouillon6-v3.txt` |
| annexe A, commande de `LISEZMOI.md` | extraite du fichier, jouée telle qu'écrite par `bash` (`python3` du système, 3.13.16), puis avec le Python du venv, sur une copie nommée `T0.5-plan-B-juges-v1.md` (empreinte égale au brouillon 6) : `b1e3e003daf2c64bb317fe5623495f73ec25e7a703c5d799ceb1ab8c1eb042e7` les deux fois | `travail/lisezmoi/` |
| annexe A, `exiger_annexe_a_egale_a_rs1` | cas sain : `b1e3e003…`. Neuf artefacts : un caractère changé, une espace de fin, une ligne vide en plus, une en moins, un retrait de trois espaces, une seconde ligne de fin après l'annexe B, une seconde ligne de début, la ligne de fin retirée, la ligne de début retirée. Sur chacun, la garde arrête et la commande ne rend pas `RS1.txt`. Fins de ligne CRLF : la garde et la commande passent toutes deux (VCB3-06) | idem |
| table « Configuration » | 50 clés (l. 333-382), dans l'ordre de `rq.CLES`. `exiger_config_planb` l'accepte. Aucun écart à `lr.CONSTANTES_CONFIG`. `exiger_config_de_l_etape` l'accepte et rend `lot_juge` = 8. `exiger_egal_au_pilote_planb` l'accepte face au manifeste du pilote (versions non comparées) ; clés égales au pilote = `prereg/T0.5-pilote-config-v1.json`. `exiger_invites_planb` l'accepte. Empreinte canonique `8ff777cf…`, inchangée. `_config_reelle()` des tests égale la table, sauf `manifeste_pilote_sha256` (factice dans les tests) | idem |
| artefacts de la table | `lot_juge` et `max_nouveaux_juge` absents, 0, négatifs, texte, flottants, booléens (12 formes) : arrêt au lecteur et au lanceur. `tolerance_simple` 0.004 : arrêt au lecteur | idem |
| lignes de citation, texte tel quel | refusé par `exiger_code_cite` (« ne cite pas le commit ») et par `exiger_citations_planb` (« configuration cité(e) nulle part »). Les valeurs citées égalent les fichiers du clone | idem |
| marqueurs (VCB2-03) | `<<COMMIT_CODE>>`, `<<EMPREINTE_CONFIG>>` ou `<<ENTROPIE>>` laissé seul : refusé. Les trois marqueurs de la chaîne laissés seuls : les deux gardes du lanceur passent | idem |
| lignes de citation, copie aux six marqueurs remplis | commit = tête du clone ; empreinte canonique ; entropie, tests attendus et empreintes des scripts : factices de bonne forme. Chaque intitulé apparaît une fois, commit compris ; notations : 8B et 3B une fois chacune. `exiger_code_cite`, `exiger_citations_planb` et `exiger_annexe_a_egale_a_rs1` passent, dans l'ordre d'`executer` | idem |
| lignes de citation, artefacts | 14 intitulés × (absent, répété avec deux valeurs, différent) ; le commit avec deux autres valeurs (racine du dépôt, commit inexistant) ; l'entropie absente ou répétée : 43 formes, toutes arrêtées, chacune par la garde de sa citation. Même valeur répétée : acceptée (une seule valeur). Commit répété en fin de texte avec une autre valeur : `exiger_code_cite` passe (première occurrence), `exiger_citations_planb` arrête. Copie remplie effacée (`215e8c0b…`) | idem |
| clone à la fin | `git status --short` : les 10 entrées non suivies ; `git diff --stat HEAD` : vide ; hors `.git`, aucun fichier plus récent que mon départ ; aucun `__pycache__` ; empreintes du code et des tests inchangées (08:16 UTC) | — |

## Mutants

Le pilote `mutants/muter_vcb3.py` reprend la méthode des rondes précédentes, réécrite. La base est le clone, jamais écrit. Chaque module muté est restauré depuis le clone, puis comparé octet pour octet. Chaque mutant exige une seule occurrence de son ancien texte. Les tests sont ciblés (`-x`), comme dans les listes. La liste `liste_mutants_vcb3.py` importe telles quelles les copies exactes de `liste_mutants_vcb2.py` (`99d3dbcb…`), `liste_mutants_v3.py` (`615df4b2…`) et `liste_mutants_verification.py` (`5747332534241b99…`), puis ajoute mes 12 mutants. Quatre passes : A (les mutants visés par VCB2 et les miens, deux travailleurs), B1 et B2 (les autres mutants nommés), et les ordres de RQ-17.

**Mutants nommés (38, liste des corrections VCB2).**

| mutant | ce qu'il simule | résultat | premier échec | fin |
|---|---|---|---|---|
| RQ-17 | témoin sans graine | tué | `tests/test_plan_b_requalifier.py::test_temoin_graine_posee_avant_chaque_appel` | 1 failed, 128 passed in 197.36s (0:03:17) |
| VCB-M01 | lecteur : lot_juge absent de la configuration du run accepté (8 par défaut) | ancien texte trouvé 0 fois | — |  |
| VCB-M02 | lecteur : cadre recalculé sans la condition du plafond | tué | `tests/test_plan_b_lecteur.py::test_cadre_du_rejeu_plafond_et_dernier_lot_incomplet` | 1 failed, 135 passed in 76.78s (0:01:16) |
| VCB-M03 | lecteur : cadre recalculé avec le dernier lot incomplet | tué | `tests/test_plan_b_lecteur.py::test_cadre_du_rejeu_plafond_et_dernier_lot_incomplet` | 1 failed, 135 passed in 74.75s (0:01:14) |
| VCB-M04 | lecteur : clés des rangées comparées sans leur ordre | tué | `tests/test_plan_b_lecteur.py::test_tirage_des_lots_recalcule_cas_sain_et_artefacts` | 1 failed, 134 passed in 108.90s (0:01:48) |
| VCB-M05 | lecteur : décalage de D1 non exigé | tué | `tests/test_plan_b_lecteur.py::test_decalages_passes_exiges_au_chemin_et_a_d1[d1-valeur3-décalages réellement passés]` | 1 failed, 131 passed in 119.88s (0:01:59) |
| VCB-M06 | lecteur : R_S illisible non classé | tué | `tests/test_plan_b_lecteur.py::test_classer_depassement_valeurs_illisibles` | 1 failed, 20 passed in 72.60s (0:01:12) |
| VCB-M07 | lecteur : grandeur illisible en réserve, non en contrôle (palier lu jusqu'à « fidèle ») | tué | `tests/test_plan_b_lecteur.py::test_grandeur_illisible_au_palier_du_chemin_cas_sain_et_artefacts[g_s]` | 1 failed, 21 passed in 26.99s |
| VCB-M08 | descriptif D-5 : tout caractère de mot compté comme un chiffre | tué | `tests/test_plan_b_rubrique_simplifiee.py::test_descriptifs_lues_suite_avec_chiffre_et_suivies_de_texte[3 (competent)-0-1]` | 1 failed, 128 passed in 8.83s |
| VCB-M09 | repère : passes en demi-précision gardées dans les rangées (D-13) | tué | `tests/test_plan_b_requalifier.py::test_repere_et_rapports_sur_le_jouet` | 1 failed, 117 passed in 115.72s (0:01:55) |
| VCB-M10 | palier de production rejoué avec D1, décalage consigné 0 | tué | `tests/test_plan_b_requalifier.py::test_rejeu_effectif_lots_graines_decalages` | 1 failed, 118 passed in 117.69s (0:01:57) |
| VCB-M11 | annexe A : fin contrôlée sur la première ligne de fin (sans effet ici) | tué | `tests/test_plan_b_rubrique_simplifiee.py::test_annexe_a_premiere_ligne_de_debut_derniere_ligne_de_fin` | 1 failed, 7 passed in 8.90s |
| VCB-M12 | annexe A : bloc arrêté à la première ligne de fin, non à la dernière | tué | `tests/test_plan_b_rubrique_simplifiee.py::test_annexe_a_premiere_ligne_de_debut_derniere_ligne_de_fin` | 1 failed, 7 passed in 6.99s |
| VCB-M13 | annexe A : dernière ligne de début, non la première | tué | `tests/test_plan_b_rubrique_simplifiee.py::test_annexe_a_premiere_ligne_de_debut_derniere_ligne_de_fin` | 1 failed, 7 passed in 7.13s |
| VCB-M14 | citation « Épisodes du pilote requalifié » présente mais jamais comparée | tué | `tests/test_plan_b_requalifier.py::test_chaque_intitule_de_citation_absent_repete_ou_different[épisodes du pilote]` | 1 failed, 72 passed in 48.11s |
| VCB-M15 | citation « Tâches du pilote » présente mais jamais comparée | tué | `tests/test_plan_b_requalifier.py::test_chaque_intitule_de_citation_absent_repete_ou_different[tâches]` | 1 failed, 73 passed in 57.01s |
| VCB-M16 | citation « Manifeste des notations rejoué » présente mais jamais comparée | tué | `tests/test_plan_b_requalifier.py::test_chaque_intitule_de_citation_absent_repete_ou_different[manifeste des notations]` | 1 failed, 75 passed in 50.97s |
| VCB-M17 | citation « Run du pilote requalifié » présente mais jamais comparée | tué | `tests/test_plan_b_requalifier.py::test_chaque_intitule_de_citation_absent_repete_ou_different[run du pilote]` | 1 failed, 70 passed in 64.89s (0:01:04) |
| VCB-M01p | lecteur : lot_juge absent accepté (8 par défaut) (porté, comme les notes VCB) | tué | `tests/test_plan_b_lecteur.py::test_lot_juge_exige_par_le_lecteur_cas_sain_et_artefacts[absent]` | 1 failed, 112 passed in 55.25s |
| VCB-M18 | lanceur : commit cité deux fois, deux valeurs, accepté | tué | `tests/test_plan_b_requalifier.py::test_chaque_intitule_de_citation_absent_repete_ou_different[commit du code d'analyse]` | 1 failed, 68 passed in 55.74s |
| VCB-M19 | lecteur : lot_juge non entier positif accepté | tué | `tests/test_plan_b_lecteur.py::test_lot_juge_exige_par_le_lecteur_cas_sain_et_artefacts[nul]` | 1 failed, 113 passed in 53.05s |
| VCB2-M01 | lanceur : aucun contrôle d'échéance avant la conversion et le repère | tué | `tests/test_plan_b_requalifier.py::test_echeance_avant_la_conversion_et_le_repere` | 1 failed, 123 passed in 142.17s (0:02:22) |
| VCB2-M02 | lanceur : aucun contrôle d'échéance avant l'ancrage | tué | `tests/test_plan_b_requalifier.py::test_echeance_avant_l_ancrage` | 1 failed, 124 passed in 153.89s (0:02:33) |
| VCB2-M03 | lanceur : aucun contrôle d'échéance avant le rechargement pour le témoin | tué | `tests/test_plan_b_requalifier.py::test_echeance_avant_le_rechargement_pour_le_temoin` | 1 failed, 125 passed in 173.92s (0:02:53) |
| VCB2-M04 | lecteur : lot_juge exigé mais non employé (8 écrit en dur) | tué | `tests/test_plan_b_lecteur.py::test_lot_juge_de_la_configuration_sert_au_tirage_des_lots` | 1 failed, 119 passed in 62.37s (0:01:02) |
| VCB2-M12 | lecteur : lot_juge nul accepté | tué | `tests/test_plan_b_lecteur.py::test_lot_juge_exige_par_le_lecteur_cas_sain_et_artefacts[nul]` | 1 failed, 113 passed in 56.18s |
| VCB2-M05 | citation « Configuration du plan B » présente mais jamais comparée | tué | `tests/test_plan_b_requalifier.py::test_gardes_de_citation_cas_sain_et_artefacts` | 1 failed, 67 passed in 72.33s (0:01:12) |
| VCB2-M06 | citation « Run des notations rejoué » présente mais jamais comparée | tué | `tests/test_plan_b_requalifier.py::test_chaque_intitule_de_citation_absent_repete_ou_different[run des notations]` | 1 failed, 74 passed in 52.53s |
| VCB2-M07 | citation « Résumé des notations rejoué » jamais comparée | tué | `tests/test_plan_b_requalifier.py::test_gardes_de_citation_cas_sain_et_artefacts` | 1 failed, 67 passed in 69.47s (0:01:09) |
| VCB2-M08 | citation « Invite RS1 » jamais comparée | tué | `tests/test_plan_b_requalifier.py::test_gardes_de_citation_cas_sain_et_artefacts` | 1 failed, 67 passed in 68.94s (0:01:08) |
| VCB2-M09 | citation « Index de l'invite RS1 » jamais comparée | tué | `tests/test_plan_b_requalifier.py::test_chaque_intitule_de_citation_absent_repete_ou_different[index de l'invite RS1]` | 1 failed, 80 passed in 52.34s |
| VCB2-M10 | citation des notations de chaque juge jamais comparée | tué | `tests/test_plan_b_requalifier.py::test_gardes_de_citation_cas_sain_et_artefacts` | 1 failed, 67 passed in 67.05s (0:01:07) |
| VCB2-M11 | citations : seule la première occurrence lue (répétition acceptée) | tué | `tests/test_plan_b_requalifier.py::test_gardes_de_citation_cas_sain_et_artefacts` | 1 failed, 67 passed in 65.51s (0:01:05) |
| VCB2-M13 | témoin : graine posée après l'appel | tué | `tests/test_plan_b_requalifier.py::test_temoin_graine_posee_avant_chaque_appel` | 1 failed, 128 passed in 192.93s (0:03:12) |
| VCB2-M14 | témoin : graine constante, la même pour tous les appels | tué | `tests/test_plan_b_requalifier.py::test_temoin_graine_posee_avant_chaque_appel` | 1 failed, 128 passed in 188.66s (0:03:08) |
| VCBb-M01 | lecteur : max_nouveaux_juge absent accepté (garde de présence retirée) | tué | `tests/test_plan_b_lecteur.py::test_max_nouveaux_juge_exige_par_le_lecteur_cas_sain_et_artefacts[absent]` | 1 failed, 120 passed in 65.97s (0:01:05) |
| VCBb-M02 | lecteur : max_nouveaux_juge nul accepté | tué | `tests/test_plan_b_lecteur.py::test_max_nouveaux_juge_exige_par_le_lecteur_cas_sain_et_artefacts[nul]` | 1 failed, 121 passed in 70.92s (0:01:10) |
| VCBb-M03 | lecteur : max_nouveaux_juge d'une autre forme qu'un entier accepté | tué | `tests/test_plan_b_lecteur.py::test_max_nouveaux_juge_exige_par_le_lecteur_cas_sain_et_artefacts[nul]` | 1 failed, 121 passed in 64.78s (0:01:04) |

- VCB-M01 tel quel : son ancien texte n'existe plus (0 occurrence), comme aux rondes précédentes ; son port VCB-M01p est tué.
- RQ-17 : tué par l'espion de `test_temoin_graine_posee_avant_chaque_appel` (`[('generate',)] == [('manual_seed', 12), ('generate',)]` échoue). Dans ma rejoue, l'égalité de deux appels de `test_temoin_configuration_remplacee_cas_sain_et_artefact` a tenu : c'est l'espion qui tue, et non ce test comme dans la rejoue des corrections. Rejoué contre l'espion dans quatre ordres, ordre réel affiché par `pytest -v` : seul ; après les trois autres tests du témoin ; avant eux ; après les trois tests neufs des échéances, puis le témoin dans l'ordre du fichier. Il meurt chaque fois, sur l'espion ; l'égalité tient dans les trois ordres où elle tourne. Sans mutant, les quatre ordres passent (`resultats-ordre-v.jsonl` ; première passe, sans l'ordre affiché : `resultats-ordre.jsonl`, mêmes issues).

**Mutants neufs de ce vérificateur (12), écrits contre les corrections VCB2 et le brouillon 6.**

| mutant | ce qu'il simule | résultat | raison de la mort |
|---|---|---|---|
| VCB3-M01 | contrôle d'avant la conversion déplacé après elle (avant le repère) | tué | conversions `['jouet-3B', 'jouet-8B']` pour `['jouet-8B']` |
| VCB3-M02 | avant la conversion, échéance de la phase seule (ni signal TERM, ni échéance globale) | tué | artefact TERM : arrêt relevé « avant le lot L1 du palier de production de jouet-8B », non avant la conversion du 3B |
| VCB3-M03 | avant l'ancrage, échéance de la phase seule | tué | artefact global : arrêt « avant le lot L1 du palier du chemin », non avant l'ancrage |
| VCB3-M04 | avant le rechargement pour le témoin, échéance de la phase seule | tué | artefact TERM : arrêt relevé « avant l'appel L1 du témoin de jouet-3B » |
| VCB3-M05 | avant la conversion, signal TERM seul (aucune échéance) | tué | conversion du 3B faite |
| VCB3-M06 | contrôle d'avant le rechargement pour le témoin déplacé après lui | tué | rechargements aux témoins `['jouet-8B', 'jouet-3B']` |
| VCB3-M07 | contrôle d'avant l'ancrage déplacé après lui | tué | ancrages `['jouet-3B', 'jouet-8B']` |
| VCB3-M08 | `exiger_config_de_l_etape` rend 8, non `lot_juge` | tué | « tirage consigné … ≠ tirage recalculé » au cas sain de VCB2-02 |
| VCB3-M09 | `max_nouveaux_juge` booléen accepté | tué (`[booleen]`) | arrêt plus loin, « cadre de 0 lot(s) » |
| VCB3-M10 | lecteur : `max_nouveaux_juge` exigé, mais 3 072 écrit en dur (cadre du rejeu et lecture RS1) | **survit** (`145 passed`) ; équivalent au réel | VCB3-01 |
| VCB3-M11 | lecteur : configuration exigée après l'issue et les fichiers du run | **survit** (`145 passed`) ; sans effet sur l'issue | VCB3-02 |
| VCB3-M12 | `max_nouveaux_juge` absent lu `None` (refusé par la forme, sans le message « absent ») | tué (`[absent]`) | message « max_nouveaux_juge None, un entier positif attendu » |

## Constats (le plus grave d'abord)

| id | gravité | où | problème | correction |
|---|---|---|---|---|
| VCB3-01 | information (R5 ; équivalent au réel ; symétrique de VCB2-02) | `lire_requalification.py`, l. 1027 (`plafond = …`), l. 1035 (`relire_notations_rs1(…, plafond)`) et l. 1059 (`lots_du_rejeu(…, lot_juge, plafond)`) ; `tests/test_plan_b_lecteur.py`, `_config` (l. 289 : `max_nouveaux_juge` 3072) | VCB-b exige `max_nouveaux_juge` entier positif. Le lecteur l'emploie pour le cadre du rejeu et pour la part au plafond de la lecture RS1. Mais toutes les lectures de test emploient 3 072. Si l'on écrit 3 072 en dur à la place de la valeur de la configuration (VCB3-M10), les 145 tests ciblés passent. Au réel, c'est sans effet : le lanceur exige `max_nouveaux_juge` égal au pilote (3 072), et la table l'écrit. C'est la situation de `lot_juge` avant VCB2-02, que la session a fait éprouver. | Facultatif, par symétrie avec VCB2-02 : une lecture synthétique avec un autre plafond (par exemple 4 096), et un espion sur `lots_du_rejeu` et `relire_notations_rs1` qui exige la valeur de la configuration. La lecture peut s'arrêter ensuite, comme au test de VCB2-02. Tuer VCB3-M10 et le noter. |
| VCB3-02 | information (texte face aux tests) | texte l. 302, 339, 340, 504 et 518 (« avant toute lecture des fichiers du run ») ; `lire_requalification.py`, l. 1014 (appel) et l. 1017-1018 (issue, fichiers) | Le code exige `lot_juge` et `max_nouveaux_juge` avant `issue_du_run` et `charger_fichiers` : c'est juste. Mais aucun test ne tient cet ordre. Si l'on déplace l'appel de `exiger_config_de_l_etape` après l'issue et les fichiers (VCB3-M11), les 145 tests ciblés passent : chaque garde arrête encore, plus tard, avec son message. Sans effet sur l'issue : un arrêt n'écrit rien ; seul le message change. | Facultatif : un test où `lot_juge` est absent et l'issue absente (ou double), qui exige le message de `lot_juge`. Tuer VCB3-M11. |
| VCB3-03 | information (texte ; chaîne des limites) | texte l. 273 (« échéance globale … contrôlée avant chaque lot ») et l. 274 (délai externe = échéance globale + un lot de dépassement de 900 s + 120 s) ; `requalifier_juges.py`, `_rejouer` (rechargement l. 826, premier contrôle l. 835) et `_apres_manifeste` (chargement du 3B, l. 562) | Depuis VCB-06, l'échéance globale se contrôle aux cinq points du « Dépassement » (l. 264), pas seulement avant chaque lot : la l. 273 est incomplète, sans contredire le code. Et aucun point de contrôle ne précède le rechargement du 8B au début de son rejeu (le texte n'en écrit pas, le code n'en a pas). Entre le contrôle d'avant le lot L3 du rejeu du 3B et celui d'avant le lot L1 du rejeu du 8B, il y a donc deux étapes : le lot D1 du 3B (600 s estimés) et ce rechargement (non mesuré). De même, entre le dernier lot de la requalification du 8B (500 s) et le premier du 3B, il y a le chargement du 3B ; il est compté dans les 300 s de chargements hors phase, donc cette paire reste sous 900 s. Le dépassement de l'échéance globale peut couvrir ces deux étapes. Il reste sous le lot de dépassement de 900 s si le rechargement du 8B dure moins de 300 s. Au-delà, il entame les 120 s de consignation, puis le signal TERM du délai externe arrêterait le run avant la garde : arrêt consigné aussi, sous un autre motif ; aucune lecture ne change. | Écrire à la l. 273 : « contrôlée aux points du « Dépassement » ». Mesurer aux bancs, avec VCB-a, le rechargement du 8B pour son rejeu et le chargement du 3B, face à cette marge. Ou ajouter un contrôle avant le rechargement du rejeu (code neuf ; à décider). |
| VCB3-04 | information (rédaction) | texte l. 572 (« Transparence », du brouillon 5 au brouillon 6) | La phrase dit : « le lanceur exige déjà `max_nouveaux_juge` entier positif et égal au pilote (liste d'arrêt, « Avant le manifeste ») ». C'est vrai du code : `exiger_config_planb` (entier positif) et `exiger_egal_au_pilote_planb` (égal au pilote). Mais la liste d'arrêt « Avant le manifeste » (l. 501) ne nomme que « configuration incomplète » et « paramètres des juges différents de ceux du pilote ». « Entier positif » est écrit à la table « Configuration » (l. 329, « égale à ce qu'exigent … `exiger_config_planb` ») et aux tests (l. 533). | Écrire « (`exiger_config_planb` ; liste d'arrêt, « Avant le manifeste ») ». |
| VCB3-05 | information (docstrings des tests) | `tests/test_plan_b_lecteur.py`, l. 1345 ; `tests/test_plan_b_requalifier.py`, l. 1817 | (a) La docstring de `test_lot_juge_exige_par_le_lecteur_cas_sain_et_artefacts` dit encore « exigé avant toute lecture » : la formule que VCB2-04 a corrigée ailleurs. (b) La docstring de `test_temoin_graine_posee_avant_chaque_appel` dit : « chaque appel rend [(6, True), (6, True)], avec ou sans graine ». Sans graine, c'est faux : sur 40 états du générateur global, 34 rendent [(6, True), (6, True)] ; 6 rendent autre chose, sous 4 formes (`rq17/sortie-essai-sans-graine.txt`). Avec la graine 12 : 40 sur 40. C'est le point ouvert « RQ-17, observation » du traitement, que je confirme. La conclusion du test tient. | (a) « avant toute lecture des fichiers du run ». (b) « le plus souvent, sans graine ». |
| VCB3-06 | information (annexe A ; aucune action requise) | `rubrique_simplifiee.py`, `exiger_annexe_a_egale_a_rs1` (`read_text`) ; commande de `LISEZMOI.md` (`open(…).read()`) ; texte l. 588 (« un seul caractère changé dans cette annexe arrête le lanceur et le lecteur ») | La garde et la commande lisent le texte en mode texte : `\r\n` y devient `\n`. Une annexe aux fins de ligne CRLF passe donc la garde et la commande, qui rendent toutes deux `b1e3e003…` (artefact écrit tel quel, octets `\r` présents). Les deux s'accordent, et l'invite employée reste `RS1.txt` : c'est sans effet. Mais la phrase de la l. 588 ne tient pas pour un retour chariot ajouté en fin de ligne. `.gitattributes` (`* -text`) ne convertit rien ; l'empreinte du texte scellé le fixe. | Aucune action requise. Facultatif : « hors fins de ligne » à la l. 588. |

## Corrections VCB2-01 à VCB2-05 et VCB-b : faites et justes ?

| constat | code et tests | texte (brouillon 6) | preuve | jugement |
|---|---|---|---|---|
| VCB2-01 (points de contrôle d'échéance) | code inchangé (`_avant`, l. 871, 876, 1040). Espion commun `_espions_des_points_de_controle` (l. 1533). `test_echeance_avant_la_conversion_et_le_repere` (l. 1598), `test_echeance_avant_l_ancrage` (l. 1635), `test_echeance_avant_le_rechargement_pour_le_temoin` (l. 1667). Chaque point : un cas sain (l'autre juge, ou une échéance large) et deux artefacts (l'échéance de la phase ; un signal TERM au premier et au troisième point, l'échéance globale au deuxième) | l. 532 | VCB2-M01 à M03 tués par leur test, pour la raison écrite : conversion, ancrage ou rechargement du 3B en trop. Mes VCB3-M01 à M07 tués : contrôle déplacé après l'étape, contrôle partiel, signal seul. J'ai refait à la main les calendriers des trois docstrings (horloge, échéances, lots de 100 s) : ils sont justes | fait, juste |
| VCB2-02 (`lot_juge` employé au tirage) | `test_lot_juge_de_la_configuration_sert_au_tirage_des_lots` (l. 1376) : `lot_juge` 4, tirage fait par les fonctions du lanceur ; cas sain : la garde du tirage passe, puis arrêt sur 8 rangées pour 16 ; artefact : tirage à lots de 8, arrêt ; rien n'est écrit | l. 534 | VCB2-M04 et VCB3-M08 tués, pour la raison écrite (« tirage consigné … ≠ tirage recalculé ») | fait, juste ; même question pour `max_nouveaux_juge` (VCB3-01) |
| VCB2-03 (marqueurs) | — | l. 10, 386, 519 | chacun des trois marqueurs du lanceur, laissé seul : refusé (`exiger_code_cite` pour le commit, `exiger_citations_planb` pour les deux autres). Les trois marqueurs de la chaîne laissés seuls : les deux gardes passent | fait, juste |
| VCB2-04 (« avant toute lecture ») | docstring de `exiger_config_de_l_etape` (l. 211-215) | l. 302, 339, 340, 504, 518 | code relu : appel après le pilote, l'analyse, les notations H.4, le manifeste du run et l'annexe A ; avant les modules, l'issue et les fichiers du run | fait ; reste une docstring de test (VCB3-05) ; ordre non tenu par un test (VCB3-02) |
| VCB2-05 (renvois périmés) | — | l. 37 (« des brouillons 4, 5 et 6 »), l. 264 (« VCB-a »), l. 580 (« transcrite par le brouillon 4 ») | différence ligne à ligne | fait, juste ; l'adaptation « 4, 5 et 6 » est la bonne, le texte étant le brouillon 6 |
| VCB-b (`max_nouveaux_juge` au lecteur) | `exiger_config_de_l_etape` (l. 232-234) : présent (`_champ`), entier, booléen refusé, au moins 1. Lecture du plafond (l. 1027) gardée, commentée. `test_max_nouveaux_juge_exige_par_le_lecteur_cas_sain_et_artefacts` (l. 1412-1436) : cas sain et six artefacts | l. 302, 340, 504, 518, 534 ; l. 572 | VCBb-M01 à M03, VCB3-M09 et VCB3-M12 tués. Artefacts sur la table du texte : arrêt au lecteur et au lanceur. Empreinte canonique inchangée | fait, juste ; voir VCB3-01 et VCB3-04 |
| garde « une seule valeur par intitulé » | code inchangé (`exiger_citations_planb`, l. 366-389 ; commit lu l. 372) | l. 501 | commit répété en fin de texte, autre valeur : `exiger_code_cite` passe, `exiger_citations_planb` arrête. Même valeur répétée : acceptée, pour chacun des 14 intitulés | fait, juste |

## Texte face au code : changements du brouillon 6

Les 23 blocs de différence entre les brouillons 5 et 6 sont ceux que listent les notes VCB2 (section 4). Le bloc de l'annexe A est identique, octet pour octet. Chaque phrase normative neuve a sa ligne de code :

| phrase du brouillon 6 | code |
|---|---|
| trois marqueurs refusés par les gardes du lanceur ; trois laissés à la chaîne (l. 10, 519) | `COMMIT_CITE`, `CITATIONS["configuration"]`, `ENTROPIE_CITEE` ; aucun motif du lanceur ne lit « Tests attendus » ni les empreintes des scripts |
| cinq points de contrôle, dépassement d'au plus l'étape commencée, VCB-a (l. 264) | `_avant` et ses appels (l. 635, 835, 871, 876, 885, 1040, 1047) ; tests de VCB2-01 ; pour l'échéance globale, voir VCB3-03 |
| `lot_juge` et `max_nouveaux_juge` entiers positifs, exigés avant toute lecture des fichiers du run (l. 302, 339, 340, 504, 518) | `exiger_config_de_l_etape`, l. 229-234 ; appel l. 1014, avant l. 1017-1018 |
| une seule valeur par intitulé, commit compris (l. 501) | `exiger_citations_planb`, l. 372-376 |
| tests listés (l. 532, 534) | présents ; chacun tue ses mutants |
| « le lanceur exige déjà … » (l. 572) | vrai du code ; renvoi imprécis (VCB3-04) |

Inversement, le code des corrections VCB2 n'ajoute qu'une règle : la garde de forme de `max_nouveaux_juge` au lecteur. Le texte l'écrit (l. 302, 340, 504, 518).

## Points ouverts du traitement (VCB2)

- VCB-a : d'accord pour mesurer ces durées aux bancs. J'y ajouterais le rechargement du 8B pour son rejeu et le chargement du 3B pour sa requalification, face au lot de dépassement de 900 s (VCB3-03).
- VCB2-03 (suite) : d'accord. Mon essai confirme que les gardes du lanceur ne lisent pas les trois marqueurs de la chaîne.
- Garde « une seule valeur par intitulé » : le numéro de registre est à citer par la session ; hors de mon champ.
- VCB2-05 (a), adaptation : juste.
- RQ-17, observation : confirmée. Sans graine, le témoin jouet rend [(6, True), (6, True)] dans 34 états sur 40 : l'égalité de deux appels est un détecteur de hasard. L'espion, lui, tue RQ-17 dans tous mes essais. La proposition de docstring est juste (VCB3-05).
- VCB2-02, constat : d'accord. `RANGEES_REJEU` (16) et `RANGEES_D1` (8) supposent des lots de 8 ; le lanceur exige `lot_juge` égal au pilote.
- VCB-d : c'est l'objet de ce rapport.

## Pièces (sous `corrections-v1/verification-v3/`)

| fichier | sha256 |
|---|---|
| `pytest-plan-b-v3.txt` | `1a45e596a7d9921dfa3504b71c23742a93191dfb19118e1f73924fa37fda6847` |
| `controle_brouillon6_v3.py` | `ed72a06a67f647938db52d9a8198a5cfdc8898d7e34c65453c54ec2f53db92bf` |
| `sortie-controle-brouillon6-v3.txt` | `90796fe2543ce2ca411594dc532f4bd9a34a1bc9a6713c658e7fe26cf8072e7a` |
| `travail/lisezmoi/T0.5-plan-B-juges-v1.md` (copie exacte du brouillon 6) | `4a4184c0d62bb44213106b9f86ca078f15eb9c89c7b65a6a4010969af022ee33` |
| `rq17/essai_sans_graine.py`, `rq17/sortie-essai-sans-graine.txt` | `4dd9b4a8…`, `f6b7b82e…` |
| `mutants/liste_mutants_vcb3.py` | `7a018a45ed588998187f6a897d66305d372a79f41cb086d159737babcbf5f8ea` |
| `mutants/liste_mutants_vcb2.py`, `liste_mutants_v3.py`, `liste_mutants_verification.py` (copies exactes) | `99d3dbcb…`, `615df4b2…`, `5747332534241b99…` |
| `mutants/muter_vcb3.py` | `62af47c868ea79c712c69eb6d4f12b5334535bea5a8ab3386bef428396a1fab2` |
| `mutants/resultats-w0.jsonl`, `resultats-w1.jsonl` (passe A) | `862788a3…`, `c37eea5e…` |
| `mutants/resultats-w0b1.jsonl`, `resultats-w0b2.jsonl` (passes B1 et B2) | `a7c4f900…`, `fb9f988f…` |
| `mutants/resultats-ordre.jsonl`, `resultats-ordre-v.jsonl` (RQ-17, ordres) | `13d143aa…`, `4878dbe0…` |
| `mutants/journal-temoin.txt`, `journal-run-temoin.txt` | `1c2904f4…`, `2dfbf0be…` |
| `mutants/tableau_nommes.py`, `tableau-nommes.md` | `a436416e…`, `350cab01…` |
| `mutants/resume_mutants.py`, `suivre_resultats.py` | `c9bdb063…`, `7c8a20f3…` |

Les journaux `journal-w0-a.txt`, `journal-w1-a.txt`, `journal-w0-b1.txt`, `journal-w0-b2.txt`, `journal-ordre.txt` et `journal-ordre-v.txt` sont les copies des résultats (mêmes empreintes). Les dossiers des travailleurs (`w0`, `w1`, `w0b1`, `w0b2`, `wT`, `wO-*`) et les dossiers temporaires (`mutants/tmp`, `clone-tmp`) sont effacés.

Je n'ai fait aucun commit ni aucune poussée. Je n'ai lancé aucune commande Vast.ai, utilisé aucun service payant ni chargé aucun modèle réel.
