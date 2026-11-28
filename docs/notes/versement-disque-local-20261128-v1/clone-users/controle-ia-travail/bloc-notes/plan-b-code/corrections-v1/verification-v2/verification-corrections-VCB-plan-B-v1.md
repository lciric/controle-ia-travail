# Vérification des corrections VCB du code du plan B des juges (T0.5) et du brouillon 5 — v1

## Verdict : prêt après corrections

- Les corrections de VCB-01 à VCB-08 sont faites et justes, au code et au texte. Aucune lecture ne change. Aucun test n'est retiré ni affaibli. Les modules gelés sont intacts.
- Les 413 tests du plan B passent. L'annexe A du brouillon 5 est `RS1.txt`, octet pour octet (`b1e3e003…`). Les lignes de citation et la table « Configuration » passent les gardes du lanceur et du lecteur, sur une copie aux marqueurs remplis de valeurs factices de bonne forme.
- Les 20 mutants nommés sont rejoués : RQ-17, VCB-M01 porté, VCB-M02 à VCB-M19. Les 20 sont tués. RQ-17 meurt pour la raison écrite (l'espion), seul et dans les deux ordres.
- J'ai écrit 14 mutants neufs : 10 sont tués et 4 survivent. Trois survivants viennent de VCB-06 : les points de contrôle d'échéance que le brouillon 5 écrit au « Dépassement » n'ont aucun artefact (VCB2-01). Le quatrième est équivalent au réel (VCB2-02).
- Il reste une correction mineure, qui ne demande que des tests : VCB2-01, au sens de R5. Le reste est de l'information : une phrase sur les marqueurs, deux formulations, deux renvois périmés. Rien n'est bloquant pour la lecture. Mais R5 est une règle gelée : VCB2-01 est à faire avant le commit du code.

## Ce qui a été lu et fait

- Je suis un vérificateur neuf (R2). Je n'ai écrit ni le texte, ni le code, ni les tests, ni aucune correction, ni aucune relecture ou vérification précédente.
- J'ai lu en entier :
  - le rapport de vérification précédent (`a751e43c…`) ;
  - les notes des corrections VCB (`aaac2688…`) ;
  - la section « Vérification des corrections (VCB) » et les points ouverts du traitement (`a4a243d0…`) ;
  - la différence mot à mot entre les brouillons 4 et 5 (`diff-mots-b4-b5.txt`, 23 blocs, tous lus) ;
  - les différences de code et de tests avec `corrections-v1/originaux-vcb/`.
- J'ai aussi lu, dans le brouillon 5, les sections touchées : en-tête et citations, « Métrique », « Ordre des phases », « Dépassement », « Lecture », « Configuration », « Avant le scellement », « Liste d'arrêt », « Code à écrire et tests », « Transparence », « Contre-lecture », annexe A.
- Empreintes recalculées. Elles sont égales à celles des notes VCB :
  - brouillon 4 : `528a2386…` ; brouillon 5 : `1d6f1932…`, 666 lignes ;
  - `requalifier_juges.py` : `a0b1d15f…` ; `lire_requalification.py` : `4ee817c6…` ;
  - `rubrique_simplifiee.py` : `beeb1017…`, inchangé ; `juges_simplifies.py` : `01a4e0c4…`, inchangé ;
  - tests : requalifier `1b8aa9be…`, lecteur `1693cbe1…`, rubrique `c04c1735…`, juges `403e1461…` (inchangé), intégration `0c1ea90f…` (inchangé) ;
  - `RS1.txt` : `b1e3e003…` ; `index.json` : `c61df3db…` ; `LISEZMOI.md` : `00e6011e…`.
- Aucun test n'est retiré. J'ai comparé les noms de fonctions par `ast` : aucune fonction de test ne disparaît, 24 tests sont ajoutés (389 → 413). Les seules lignes retirées des tests sont des docstrings (3, 1 et 5 lignes), réécrites. Aucune assertion n'est retirée. Toutes les lignes neuves ont 120 caractères au plus.
- Le clone n'a reçu aucune écriture. Aucun fichier n'y a été modifié depuis le début de ma vérification. Tous les lancements ont tourné sous `nice -n 19`, avec `-B`, `-p no:cacheprovider`, `--basetemp` et `TMPDIR` dans `verification-v2/`.
- Les copies de mutants (`w0`, `w1`, `wT`, `wR`) sont effacées après usage. `rm -r` n'efface que les liens, jamais leurs cibles. Les dossiers temporaires sont effacés aussi.
- Je n'ai ouvert aucune donnée scellée, sauf pour les contrôles mécaniques : des empreintes de fichiers et la configuration du manifeste du pilote. Aucun contenu n'est affiché.

## Résultats mécaniques

| contrôle | résultat | pièce |
|---|---|---|
| tests du plan B, clone | `413 passed in 198.92s` (code 0), aucun `__pycache__` | `pytest-plan-b-v2.txt` |
| témoin des mutants (copie non mutée) | `413 passed in 660.64s` | `mutants/journal-temoin.txt` |
| annexe A, extraction indépendante (octets) | une ligne de début (l. 587) et une ligne de fin (l. 644) ; 3 966 octets ; égale à `RS1.txt`, octet pour octet ; ASCII, sans retour chariot, sans espace de fin, une seule fin de ligne finale | `controle_brouillon5.py`, `sortie-controle-brouillon5.txt` |
| annexe A, commande de `LISEZMOI.md` | extraite du fichier et jouée telle qu'écrite, sur une copie nommée `T0.5-plan-B-juges-v1.md` (empreinte égale à celle du brouillon 5). Avec le Python du venv : `b1e3e003daf2c64bb317fe5623495f73ec25e7a703c5d799ceb1ab8c1eb042e7`. Avec `python3` du système (3.13.16) : la même empreinte | `travail/lisezmoi/` |
| annexe A, `exiger_annexe_a_egale_a_rs1` | cas sain : `b1e3e003…`. Six artefacts arrêtent : un caractère changé, une ligne vide de plus, un retrait manquant, une seconde ligne de fin après l'annexe B, une seconde ligne de début avant l'annexe, la ligne de fin retirée. Sur chacun, la commande de `LISEZMOI.md` rend `RS1.txt` exactement quand la garde passe | idem |
| table « Configuration » | 50 clés, dans l'ordre de `rq.CLES`, aucune en plus ni en moins. `exiger_config_planb` l'accepte. Aucun écart à `lr.CONSTANTES_CONFIG`. `lr.exiger_config_de_l_etape` l'accepte et rend `lot_juge` = 8. `exiger_egal_au_pilote_planb` l'accepte face au manifeste du pilote (versions non comparées). `exiger_invites_planb` l'accepte. `manifeste_pilote_sha256` est l'empreinte du manifeste ; `couverture_jetons` = `SEUILS_COUVERTURE`. Empreinte canonique `8ff777cf…`, inchangée. Artefacts « `lot_juge` absent, 0, `"8"` » : arrêt au lanceur et au lecteur | idem |
| lignes de citation, texte tel quel | refusé par `exiger_code_cite` (« ne cite pas le commit ») et par `exiger_citations_planb` (« configuration cité(e) nulle part ») | idem |
| lignes de citation, copie aux six marqueurs remplis | commit = tête du clone ; empreinte canonique ; entropie, tests attendus et empreintes des scripts : factices de bonne forme. Chaque intitulé apparaît une fois, commit compris ; notations : 8B et 3B une fois chacune. `exiger_code_cite`, `exiger_citations_planb` et `exiger_annexe_a_egale_a_rs1` passent dans l'ordre d'`executer`. Les valeurs citées égalent les fichiers du clone et la section « Pièces scellées » | idem |
| lignes de citation, artefacts sur la copie remplie | 14 intitulés (commit, les dix, l'entropie, les notations 8B et 3B) × trois formes : absent, répété avec deux valeurs, différent (l'entropie : absente ou répétée). Les 41 formes arrêtent, chacune par la garde de sa citation. La copie remplie est effacée (`abe5c94c…`) | idem |
| clone à la fin | `git status --short` : les 10 entrées non suivies ; `git diff --stat HEAD` : vide ; aucun `__pycache__` | — |

## Mutants

Le pilote `mutants/muter_v3.py` reprend celui des notes VCB. La base est le clone, jamais écrit. Chaque module muté est restauré depuis le clone puis comparé octet pour octet. Chaque mutant exige une seule occurrence de son ancien texte. Les tests sont ciblés (`-x`), comme dans la vérification précédente. Deux travailleurs et le témoin ont tourné en parallèle. Résultats : `mutants/resultats-w0.jsonl` et `mutants/resultats-w1.jsonl` (35 lignes).

**Mutants nommés (liste de la vérification recopiée, `5747332534241b99…`).**
- VCB-M01 tel quel : son ancien texte n'existe plus (0 occurrence). Je l'ai porté avec la même substitution que les notes (VCB-M01p) : il est tué par `test_lot_juge_exige_par_le_lecteur_cas_sain_et_artefacts[absent]`.
- RQ-17 : tué par `test_temoin_graine_posee_avant_chaque_appel`, sur l'espion : `[('generate',)] == [('manual_seed', 12), ('generate',)]` échoue. Rejoué seul, après les deux autres tests du témoin, puis avant eux : il échoue chaque fois, pour la même raison. Sur le code non muté, les trois ordres passent (`mutants/sortie-rq17-v3.txt`).
- VCB-M02 et VCB-M03 : tués par `test_cadre_du_rejeu_plafond_et_dernier_lot_incomplet`.
- VCB-M04 à VCB-M10 : tués, comme dans la vérification précédente.
- VCB-M11 à VCB-M13 : tués par `test_annexe_a_premiere_ligne_de_debut_derniere_ligne_de_fin`.
- VCB-M14 à VCB-M17 : tués par `test_chaque_intitule_de_citation_absent_repete_ou_different`, avec le paramètre attendu.
- VCB-M18 : tué par le paramètre « commit du code d'analyse ». VCB-M19 : tué par le paramètre « nul ».
- **Bilan : 20 rejoués, 20 tués.**

**Mutants neufs de ce vérificateur (14), écrits contre les corrections VCB et le brouillon 5.**

| mutant | ce qu'il simule | résultat |
|---|---|---|
| VCB2-M01 | aucun contrôle d'échéance avant la conversion et le repère | **survit** (`269 passed`) |
| VCB2-M02 | aucun contrôle d'échéance avant l'ancrage | **survit** (`269 passed`) |
| VCB2-M03 | aucun contrôle d'échéance avant le rechargement pour le témoin | **survit** (`269 passed`) |
| VCB2-M04 | lecteur : `lot_juge` exigé, mais 8 écrit en dur dans l'appel de `lots_du_rejeu` | **survit** (`138 passed`) ; équivalent au réel |
| VCB2-M05 | citation « Configuration » jamais comparée | tué |
| VCB2-M06 | citation « Run des notations » jamais comparée | tué |
| VCB2-M07 | citation « Résumé des notations » jamais comparée | tué |
| VCB2-M08 | citation « Invite RS1 » jamais comparée | tué |
| VCB2-M09 | citation « Index de l'invite RS1 » jamais comparée | tué |
| VCB2-M10 | notations de chaque juge jamais comparées | tué |
| VCB2-M11 | citations : seule la première occurrence lue | tué |
| VCB2-M12 | lecteur : `lot_juge` nul accepté | tué (`[nul]`) |
| VCB2-M13 | témoin : graine posée après `generate` | tué (espion) |
| VCB2-M14 | témoin : graine constante pour tous les appels | tué (espion) |

## Constats (le plus grave d'abord)

| id | gravité | où | problème | correction |
|---|---|---|---|---|
| VCB2-01 | mineur (R5 ; texte face aux tests) | `requalifier_juges.py`, `_avant` appelé l. 871 (avant la conversion et le repère), l. 876 (avant l'ancrage) et l. 1040 (avant le rechargement pour le témoin) ; texte, « Dépassement » (l. 264) et tests, « échéances » (l. 532) ; `tests/test_plan_b_requalifier.py`, `test_ancrages_et_depassement_d_au_plus_un_lot` (l. 912) et `test_echeance_avant_les_lots_en_simple_precision` (l. 1503) | VCB-06 rend normatifs ces trois points de contrôle. Le texte écrit : « chaque échéance se contrôle avant chaque lot, avant la conversion et le repère, avant l'ancrage, avant chaque rechargement d'un juge pour le témoin et avant chaque appel du témoin ». Mais aucun test ne les éprouve sur un artefact. Si on retire l'un des trois, les 269 tests ciblés passent encore : VCB2-M01, M02 et M03 survivent. Pourquoi : dans les tests, l'échéance tombe toujours avant un lot ou un appel, jamais entre la production et la conversion, ni entre le repère et l'ancrage, ni entre les appels du 8B et le rechargement du 3B. Or `_avant` porte aussi deux gardes d'arrêt, l'échéance globale et le signal TERM. Sans ces contrôles, le dépassement pourrait couvrir plusieurs étapes, par exemple la conversion, le repère, l'ancrage puis un lot. Il dépasserait alors la borne d'une étape écrite au « Dépassement », sur laquelle reposent le délai externe et la somme des maxima. Le code est juste aujourd'hui ; ce sont les tests qui manquent. Enfin, la liste des tests (l. 532) dit encore « dépassement d'au plus un lot », alors que le « Dépassement » dit maintenant « d'au plus l'étape commencée ». | Ajouter un test par point de contrôle, avec l'`Horloge` des tests : (a) échéance du rejeu atteinte pendant le lot L2 de production : `convertir_en_simple` n'est jamais appelé (espion), `rejeu-…-simple` est « échu », `rejeu-…-demi` est écrit ; (b) échéance atteinte pendant le repère (l'horloge avance dans `repere_demi_simple`) : `ancrage_noyaux` n'est jamais appelé ; (c) échéance des témoins atteinte pendant le second appel du 8B : le 3B n'est pas rechargé (compte des appels de `_charger_pour_le_rejeu`). Au moins un cas doit porter l'échéance globale (arrêt consigné) ou un signal TERM au même point. Écrire ces cas à la ligne « échéances » des tests (l. 532), et y remplacer « au plus un lot » par « au plus l'étape commencée ». Tuer VCB2-M01 à M03 et le noter. |
| VCB2-02 | information (R5 ; équivalent au réel) | `lire_requalification.py`, l. 1008 et l. 1053 ; `tests/test_plan_b_lecteur.py` (config `lot_juge` 8, l. 287) | VCB-02 exige `lot_juge` et le passe à `lots_du_rejeu`. Mais aucune lecture de test n'emploie une autre valeur que 8. Si on écrit 8 en dur à la place de la valeur exigée, tout passe : VCB2-M04 survit. Au réel, c'est sans effet : le lanceur exige `lot_juge` égal au pilote (8, `CLES_EGALES_AU_PILOTE`), et la table l'écrit. | Facultatif : une lecture synthétique avec `lot_juge` 4 et un tirage cohérent, ou un espion sur `lots_du_rejeu` qui exige la valeur de la configuration. |
| VCB2-03 | information (texte ; inchangé depuis le brouillon 4) | texte l. 10 (« Marqueurs à remplir au candidat ») | Le texte dit : « Tant qu'il en reste un, les gardes de citation refusent le texte ». C'est vrai pour `<<COMMIT_CODE>>`, `<<EMPREINTE_CONFIG>>` et `<<ENTROPIE>>`. C'est faux, au lanceur, pour les trois marqueurs de la chaîne. Une copie où seuls `<<TESTS_ATTENDUS>>`, `<<SHA256_AMORCE>>` et `<<SHA256_SCRIPT_INSTANCE>>` restent passe `exiger_code_cite` et `exiger_citations_planb` (essai : `sortie-controle-brouillon5.txt`). Leur refus dépend de la chaîne, qui n'est pas encore écrite (point 6). | Écrire que les trois premiers marqueurs sont refusés par les gardes du lanceur, et les trois autres par la chaîne (script de l'instance : « Tests attendus », empreintes des scripts). Porter ce refus, avec un artefact, à la relecture R2 de la chaîne. |
| VCB2-04 | information (rédaction) | texte l. 302, l. 339, l. 504, l. 518 ; docstring de `exiger_config_de_l_etape` | Le texte dit « exigé avant toute lecture ». Le code exige `lot_juge` après avoir lu le pilote, l'analyse, les notations H.4 (seuils de couverture), le manifeste du run et l'annexe A. Il l'exige avant l'issue et les fichiers du run. Le sens est juste, car rien n'est lu des résultats de l'étape ; c'est le mot qui est trop large. | Écrire « avant toute lecture des fichiers du run ». |
| VCB2-05 | information (renvois périmés) | texte l. 37 ; l. 264 | (a) La ligne 37 dit encore « ce qu'elle retient de ce brouillon 4 ». Mais le texte est le brouillon 5, et la ligne 399 dit maintenant « les brouillons 4 et 5 ». (b) La ligne 264 renvoie au « point ouvert du traitement, VCB-06 ». Le traitement nomme ce point ouvert VCB-a. | (a) Écrire « des brouillons 4 et 5 ». (b) Écrire « VCB-a ». |

## Corrections VCB-01 à VCB-08 : faites et justes ?

| constat | code et tests | texte (brouillon 5) | preuve | jugement |
|---|---|---|---|---|
| VCB-01 (graine du témoin) | `test_temoin_graine_posee_avant_chaque_appel` (l. 1636) : l'espion exige `[("manual_seed", graine), ("generate",)]` à chaque appel ; jetons égaux à graine égale depuis deux états du générateur global, différents sous une autre graine ; code inchangé (`appel_temoin`, l. 1005) | tests, témoin (l. 529) | RQ-17 tué, seul et dans les deux ordres ; VCB2-M13 (graine après l'appel) et VCB2-M14 (graine constante) tués | fait, juste |
| VCB-02 (`lot_juge` au lecteur) | `exiger_config_de_l_etape` (l. 209-229) exige `lot_juge` (`_champ`, entier, booléen refusé, ≥ 1) et le rend ; `lire_requalification` le passe à `lots_du_rejeu` (l. 1008, l. 1053) ; plus de lecture sous condition ; tests l. 1341 (6 artefacts) et l. 1356 (sans fichier du rejeu : cas sain et artefact) | l. 302, 339, 504, 518, 534 | VCB-M01p, VCB-M19 et VCB2-M12 tués ; artefacts sur la table du texte : arrêt | fait, juste ; voir VCB2-02 et VCB2-04 |
| VCB-03 (chaque intitulé) | test paramétré l. 630 (14 intitulés × 3 formes, l'entropie × 2), avec un cas sain par paramètre ; trou du commit répété comblé dans le module neuf (`exiger_citations_planb`, l. 372 : `COMMIT_CITE` lu, une seule valeur) ; aucun module gelé touché | l. 9, 517, 533 | VCB-M14 à M18 tués ; VCB2-M05 à M11 tués ; mes 41 artefacts sur la copie remplie du brouillon 5 arrêtent | fait, juste |
| VCB-04 (cadre du lecteur) | `test_cadre_du_rejeu_plafond_et_dernier_lot_incomplet` (l. 1483) : données écrites en clair ; cadre [0, 3, 4] égal à `rq.cadre_du_rejeu` ; tirage égal à celui de `rq.tirer_lots` ; cadres fautifs [0, 1, 3, 4] et [0, 3, 4, 5] : arrêt | l. 534 | VCB-M02 et VCB-M03 tués | fait, juste |
| VCB-05 (rôles de l'ancrage) | code inchangé : `ancrage_noyaux` (l. 742-749) fait `ecarts_par_jeton(a_defaut[c], a_math[c])` ; la fonction gelée calcule ‖g − p‖ / ‖p‖ (`activations.py`, l. 124-130), donc le dénominateur est a_math | l. 144 et l. 259 : numérateur ‖a_défaut − a_math‖, dénominateur ‖a_math‖, la passe au noyau « math » en référence | relu face au code gelé ; test des rôles existant (passe) | fait, juste |
| VCB-06 (échéances) | docstrings du module (l. 25-26) et de `_avant` (l. 483-484) ; appels l. 635, 835, 871, 876, 885, 1040, 1047 : conformes au texte | l. 264 : les cinq points, dépassement d'au plus l'étape commencée, durées non mesurées comptées sous la borne d'un lot ou d'un appel | relu face au code | fait, juste ; mais trois points sans artefact (VCB2-01) ; renvoi « VCB-06 » au lieu de « VCB-a » (VCB2-05) |
| VCB-07 (annexe A) | `test_annexe_a_premiere_ligne_de_debut_derniere_ligne_de_fin` (rubrique, l. 130) : 4 artefacts et un cas sain de la règle ; la commande de `LISEZMOI.md`, extraite du fichier, est jouée sur chaque texte ; code inchangé | l. 523 | VCB-M11, M12 et M13 tués ; mes artefacts sur le brouillon 5 : la garde et la commande s'accordent | fait, juste |
| VCB-08 (rédaction) | (a) docstring du lecteur (l. 11-15, 23-24) ; (b) réserve « ancrage au-dessus de 1e-3 ou illisible » (l. 734-737) ; (c) docstring de `annexe_a_comme_au_texte` sans numéros de ligne | inchangé (l. 301 listait déjà ces calculs) | tests existants de la réserve : passent | fait |

## Texte face au code : changements du brouillon 5

Les 23 blocs de différence entre les brouillons 4 et 5 sont ceux que listent les notes VCB (section 4). Le bloc de l'annexe A est identique. Chaque phrase normative neuve a sa ligne de code :

| phrase du brouillon 5 | code |
|---|---|
| commit à valeur unique, exigé par `exiger_citations_planb` (l. 9, l. 517) | `rq.exiger_citations_planb`, l. 372 |
| rôles de l'ancrage (l. 144, l. 259) | `rq.ancrage_noyaux`, l. 749 ; `activations.ecarts_par_jeton` |
| cinq points de contrôle d'échéance (l. 264) | `rq._avant` et ses appels (l. 635, 835, 871, 876, 885, 1040, 1047) ; tests incomplets (VCB2-01) |
| `lot_juge` entier positif, exigé sans condition (l. 302, 339, 504, 518) | `lr.exiger_config_de_l_etape`, l. 226-229 ; l. 1008 ; voir VCB2-04 pour « avant toute lecture » |
| tests listés : VCB-07 (l. 523), VCB-01 (l. 529), VCB-03 (l. 533), VCB-02 et VCB-04 (l. 534) | présents, et chacun tue ses mutants |

Inversement, le code des corrections VCB n'ajoute aucune règle absente du texte. Sa seule règle neuve est l'unicité du commit, et le texte l'écrit (l. 9 ; liste d'arrêt, « Avant le manifeste », l. 501).

## Points ouverts du traitement (VCB)

- VCB-a (durées non mesurées de la conversion, du repère, de l'ancrage et d'un rechargement) : d'accord pour les mesurer aux bancs. Le texte doit renvoyer à VCB-a (VCB2-05).
- VCB-b (`max_nouveaux_juge` lu sans garde de forme, l. 1021) : je le confirme. Sans la clé, le lecteur lève une `KeyError`, pas une `GardeArret`. L'arrêt a donc lieu, rien n'est écrit, mais sans message de garde. Le texte n'écrit pas de garde pour cette clé : ce n'est pas un écart. Je recommande de l'aligner sur `lot_juge`, avec trois lignes et un test, pour qu'aucun arrêt ne passe sans message.
- VCB-c : c'est l'objet de ce rapport.

## Pièces (sous `corrections-v1/verification-v2/`)

| fichier | sha256 |
|---|---|
| `pytest-plan-b-v2.txt` | `2e2c7d868af81c2fb9339d8b9f11b91e431887cc51e5e3c17067db2cce644cc0` |
| `diff-mots-b4-b5.txt` | `4a34ded3000b6f8c6b4d1e022b68a984380d1dccbe1030c54b5aaf6bca669c03` |
| `controle_brouillon5.py` | `7eaff065b78f1b6bd5101d41a925e116641e91a95e4b39c85ba216be9a31de7e` |
| `sortie-controle-brouillon5.txt` | `49e27d4581f4d66aba0b97bb4173bcf0fe1f33a85023634545aed6037e4c7116` |
| `travail/lisezmoi/T0.5-plan-B-juges-v1.md` (copie exacte du brouillon 5) | `1d6f1932d8597421caeedeff16e7d0175003921c40bc0173c133cbdb3ef768f2` |
| `mutants/liste_mutants_verification.py` (copie exacte) | `5747332534241b99c553757fb823b28f622111724b34f727346b98703ef7b0e9` |
| `mutants/liste_mutants_v3.py` | `615df4b2e7e057217b3dca9432c038f799f6ba879a895b8055cfaa1c8f00d8d2` |
| `mutants/muter_v3.py` | `076af5ad830186d064b025f4b280fb92991634871bfd59e3ebec6d337a336eb4` |
| `mutants/resultats-w0.jsonl`, `resultats-w1.jsonl` | `989c2f27…`, `76d2aef9…` |
| `mutants/journal-temoin.txt`, `journal-run-temoin.txt` | `7f2e6f1a…`, `8bd028a5…` |
| `mutants/rejouer_rq17_v3.py`, `sortie-rq17-v3.txt` | `31283b08…`, `ee4cd9ec…` |

Je n'ai fait aucun commit ni aucune poussée. Je n'ai lancé aucune commande Vast.ai, utilisé aucun service payant ni chargé aucun modèle réel.
