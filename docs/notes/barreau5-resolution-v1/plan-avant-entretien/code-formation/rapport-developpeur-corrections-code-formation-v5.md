# Rapport du développeur des corrections du code de formation des familles d'adaptateurs jumeaux (barreau 5) — v5 (troisième tour)

- Développeur : le sous-agent des rapports v3 et v4, Claude Opus 5.5 (« You are powered by the model named Opus 5.5. »). Pièce d'instrument (classe B), à vérifier par le même contre-lecteur (Claude Fable 5.2). Écrit dans la nuit du 19 au 20 novembre 2026, de 22:55Z à 23:43Z environ (heures relevées par `date -u`).
- Demande : message de la mère, troisième tour « sur les choix du texte », puis son second message : l'erratum 1 au brouillon 5 fixe les règles du texte et prime. Pièces lues, empreintes vérifiées : le texte, brouillon 5 (`6f7e20418c84…`), aux sections qui touchent le code ; la table des corrections du brouillon 4 (`bf129b01d730…`), son § 1 « Choix qui touchent le code » ; la vérification du brouillon 4 (`a091eed230a1…`), constat W-m3 ; **l'erratum 1 au brouillon 5** (`8c3451a2e768…`), en entier ; le rangement des treize points (g) de mon rapport v4 (`76e0e27efe4a…`) ; le devis du brouillon 5 (`9ba5db06f207…`, § 3 et 4) ; la table des corrections du brouillon 5 (`8be817c6d69d…`).
- Mots de Lazar rapportés par la mère : 39 adaptateurs, voie (iii), départ au plus tôt (`GO-2026-11-19-79` et `-82`) ; accord de calcul, plafond commun de 200 USD (`GO-86`) ; enveloppe de relance à part, 56 USD au plus (`GO-87`).
- Rien de réel : aucune instance, aucune dépense, aucun commit. Réseau : PyPI et l'index de PyTorch pour processeur, pour refaire l'environnement Python 3.11 seulement. Aucune donnée, aucun résultat, aucune transcription, aucun énoncé de tâche.
- Garde du dépôt tenue : aucun nom de commande d'arrêt ni de recherche de processus dans aucune commande ; attentes par l'outil de tâches et la lecture des journaux. Aucun refus d'outil. Fichiers du dépôt écrits par les outils d'écriture et d'édition ; temporaires dans `/dev/shm`, effacés à la fin par leurs chemins écrits en toutes lettres (§ 8).

## 1. Verdict

Les quatre points que le texte demande au code sont codés, chaque garde avec cas sain et artefact : **(a)** deux paliers de la part non éditable (25 % et 10 %), le marqueur « part non éditable haute » au résultat de la famille, la part par motif en six classes et la classe de chaque action non éditable ; **(c)** la relance hors du plafond commun : à l'inscription, deux instances au plus et 56 USD de coupures au plus ; en cours de marche, deux compteurs, la relance ne comptant que sa coupure ; **(d)** le nom de carte, à la lettre de la définition de « collé » de l'erratum, le lecteur gelé n'étant pas touché ; **(f)** la table à trois membres des instances 6 et 7 (28 USD, 9,61 à 10,99 heures ; 17 USD, 5,71 à 6,40 heures). Rien n'est codé pour (b) (code de lecture), (e) (refusé par le texte) ni (g) (l'erratum aligne le texte sur le code : modèle nu, base de temps de la coupure ; aucun point de (g) ne demande de code). Plancher d'essais de l'amorce : 191 → **235**, remesuré sur l'arbre extrait : 235 passés sous Python 3.13 et sous Python 3.11 (refait : le paquet a changé). Essais : **325** dans les six fichiers, **325 passés**. Mutations : **32 défauts réintroduits, 32 attrapés** (les 20 de ce tour, et 12 des tours précédents dont le code visé a changé) ; aucune équivalente, aucune manquée.

## 2. Choix du texte → correction → essai qui l'attrape

Fichiers d'essais : (E) `test_barreau5_familles_edition_cout_v1.py` ; (G) `…_engagement_v1.py` ; (F) `…_formation_v1.py` ; (L) `test_lancer_b5f_formation_v1.py` ; (A) `test_amorce_b5f_formation_v1.py` ; (AE) `test_amorce_b5f_formation_entiere_v1.py`. Entre crochets, les mutations du § 3 que l'essai attrape.

| choix du texte | correction | essai qui l'attrape |
|---|---|---|
| **(a) Deux paliers** (texte, plan, point 3 ; erratum 1, couple E-2a) : part ≤ 25 %, sinon famille non formée et retirage ; au-dessus de 10 %, famille formée et marquée « part non éditable haute », marqueur écrit au résultat de la famille | `edition_cout_v1` : `PART_NON_EDITABLE_MAX = 0.25`, `PART_NON_EDITABLE_HAUTE = 0.10` (l. 51-52) ; `controler_famille` (l. 331-365) rend `part_non_editable_haute` (10 % < part ≤ 25 %) et `part_par_motif`. `formation_v1._former_une_famille` recopie le marqueur au statut de la famille (l. 1277), donc à `diag/<marche>/famille-<k>.json`. Le repli à quatre familles refusées reste à la session : rien d'automatique | E `test_deux_paliers_de_la_part_non_editable_marqueur_et_part_par_motif` (six cas : 0 et 10 % juste, formée non marquée ; 20 % et 25 % juste, formée marquée ; 33 % et 50 %, non formée) ; F `test_jouet_part_non_editable_haute_famille_formee_marquee_part_par_motif_et_classe_ecrite` (chaîne jouet, 2 actions sur 12 : formée, marquée au résultat de la famille ; sans action non éditable : non marquée) [R01, R02, R03, R05] |
| **(a) Six classes** (erratum 1, E-2a) : plusieurs nombres ; intervalle ; multiplication ; suffixe « k » ; action non valide, coût illisible ou absent ; contrôle manqué (épissure, contrôle par action, nombre du champ différent du coût lu) | `CLASSES_NON_EDITABLE` (l. 56-57) ; chaque refus de `action_editable`, `localiser_nombre_du_cout` et `editer_action` porte sa classe ; `editer_tirage` écrit, par action non éditable, la classe du premier membre qui l'a refusée (celui de son motif, l. 315). Correspondance : « action non valide », « coût illisible », « champ du coût absent ou vide » → action non valide, coût illisible ou absent ; « N nombre(s) dans le champ brut », « nombre brut ≠ coût lu », épissure, contrôles par action → contrôle manqué. La clé `classe` entre au contenu borné des lignes d'édition (`formation_v1`, l. 162 et 333-334 : nulle pour une action éditable, l'une des six sinon) | E `test_classes_des_actions_non_editables` (six cas) et `test_classes_action_non_valide_et_controle_manque` ; F `test_point_5_contenu_borne_des_sorties_de_texte_…` (deux artefacts neufs : classe sur une action éditable, classe illisible) [R04, R19] |
| **(c) Relance, à l'inscription** (texte, « Calendrier », borne de la relance ; erratum 1, couples E-4a et E-7a) : la ligne `GO-RELANCE-FORMATION-B5F` cite deux instances au plus, et leurs coupures ne dépassent pas 56 USD ; sinon refus, nœud | `formation_v1` : `RELANCES_MAX = 2`, `ENVELOPPE_RELANCE_USD = 56.0` (l. 111-112) ; `lire_code_et_accord` (l. 1053-1059) refuse la ligne, avec la coupure de chaque instance selon le nombre de membres de `SCELLEMENT-B5F`. Toute lecture du registre propre passe par là : la marche, et toutes les commandes du lanceur | F `test_registre_relance_bornee_deux_instances_et_enveloppe_de_56_usd` (sains : 6 et 1, 54 USD ; 1 et 7 ; 6 et 7 ; une seule ; artefacts isolés : trois instances sous l'enveloppe, la table retouchée à 10 USD ; deux instances au-delà, la table retouchée à 30 USD) ; L `test_commande_artefacts_…[relance_trois_instances]` [R11, R12] |
| **(c) Relance, en cours de marche** (liste d'arrêt, point 14 ; erratum 1, couples E-4a et E-8a) : deux compteurs. Par instance, sa coupure (une relance : celle de l'instance remplacée) ; en commun, les pièces du devis contre 200 USD, sans la dépense d'une relance ; pas de troisième compteur ; le plafond atteint n'arrête pas une relance en cours | `depense_session(…, *, relance)` (l. 1520-1536) : la coupure toujours ; le plafond commun seulement pour une pièce du devis ; `relance` exigé, booléen, sans défaut. Sous-commande `depense` du lanceur : un argument de plus, `RELANCE` (0 ou 1), sans défaut | F `test_depense_deux_compteurs_la_relance_hors_du_plafond_commun` ; L `test_depense_cas_sain_et_artefacts_coupure_et_plafond` et `test_depense_d_une_relance_hors_du_plafond_commun_sa_seule_coupure` [R13, R14, R20] |
| **(d) Nom de carte** (texte, plan, point 3 ; erratum 1, couple E-1a) : un nombre collé à une lettre n'est pas compté, pourvu que le premier nombre du champ ne le soit pas ; « collé » : une lettre touche le nombre, juste avant ou juste après, sans espace ni signe ; le suffixe « k » lu fait partie du nombre ; un tiret sépare ; si le premier est collé, tous comptent | `edition_cout_v1` : `_colle_a_une_lettre` et `nombres_comptes` (l. 135-153) remplacent le drapeau « plusieurs nombres » du lecteur gelé aux trois endroits : `action_editable` (l. 184-197), `localiser_nombre_du_cout` (l. 156-181), `controler_edition` (l. 246). `t06/cout.py` n'est pas touché ; son drapeau reste levé, le même pour tous les membres | E `test_nom_de_carte_nombres_comptes_a_la_lettre_de_l_erratum` (quatorze champs) ; `test_nom_de_carte_cas_sains_edites_carte_inchangee_lecteur_gele_non_touche` (quatre écritures, deux tokeniseurs) ; `test_nom_de_carte_artefacts_non_editables_pour_tous_classe_plusieurs_nombres` (six écritures) ; `test_controle_par_action_le_nom_de_carte_ne_desserre_pas_le_compte_de_l_action_editee` [R06 à R10, R18] |
| **(f) Table à trois membres** (devis du brouillon 5, § 3 ; erratum 1, couple E-6a) : instance 6, 28 USD, 9,61 à 10,99 heures ; instance 7, 17 USD, 5,71 à 6,40 heures ; deux entrées par instance, choisies par le nombre de membres | `COUPURES_TROIS_MEMBRES_USD`, `HEURES_TROIS_MEMBRES` (l. 104-105) ; `_trois_membres`, `coupure_usd`, `heures_attendues` (l. 464-477) : le refus « devis non chiffré » est retiré ; `plan` imprime les deux entrées. Échéance d'arrêt au prix plafond : 21,3 et 12,8 heures, au-dessus des heures attendues | F `test_table_du_devis_a_trois_membres_instances_6_et_7` (somme de la formation : 175 USD) ; F `test_echeance_d_arret_…`, `test_configuration_de_chaque_instance_…[3]`, artefact de configuration (24 USD à trois membres refusé) ; L `test_plan_…`, `test_config_reelle_…`, `test_commande_a_trois_membres_instance_6_echeance_a_la_coupure_de_28_usd` [R15, R16, R17] |
| **(b) Copie `-x1`** | non codé : relève du code de lecture (erratum 1, couple E-3a) | — |
| **(e) « 2k » écrit « 600 »** | non codé : refusé par le texte ; « 2k » reste non éditable, classe « suffixe « k » » | E (essai m-5 inchangé ; classe vérifiée) |
| **(g) Treize points** | non codé : neuf pris par le texte ou le devis (erratum 1, couples G-1a à G-12a), les autres renvoyés à (a), (b), (c) ou conformes (rangement `points-g-rapport-v4-ranges-v1.md`) ; en particulier, le modèle nu en fin de famille et la base de temps de la règle de coupure restent tels qu'au deuxième tour, le texte s'alignant sur eux | — |
| **Plancher** | `MIN_ESSAIS` 191 → 235 (quarante-quatre essais de plus dans le paquet) | A `test_texte_plancher_d_essais_egal_au_nombre_d_essais_du_paquet` ; arbre extrait : 235 passés (§ 7) |

Ce que je n'ai pas ajouté, et pourquoi : un refus d'une ligne de relance qui citerait l'accord de la formation au lieu de celui de l'enveloppe. Le texte dit que la ligne « cite cet accord » (`GO-87`), mais ne demande pas au code de le vérifier ; la garde de calcul rejoue déjà l'accord cité par la commande. Une ligne de code si le texte le veut.

## 3. Contrôle par mutation

Outil : `mutations-dev-corrections-v5.py`, dans `outils-developpeur-corrections-code-formation-v5/` (scellé). Il importe tels quels l'outil du premier tour (`…-v3/outils/mutations-dev-corrections-v1.py`, `2f0e5ccb…`, sa logique de jeu), la liste du vérificateur et celle du deuxième tour, et joue : les vingt mutations neuves de ce tour (R01 à R20), et les douze mutations des tours précédents dont le code visé a changé à ce tour. Une seule copie de travail, dans `/dev/shm` : l'arbre que l'amorce extrait, tiré de l'arbre de travail sans commit, plus les essais du lanceur et des amorces et la garde de calcul ; effacée à la fin. Chaque mutation posée, jouée (fichiers visés d'abord, arrêt au premier échec ; s'ils passent, les six fichiers), retirée, fichier rendu à l'octet.

| n° | défaut réintroduit | résultat | essai qui l'attrape (premier échec) |
|---|---|---|---|
| R01 | (a) part non éditable admise jusqu'à 50 % | attrapée | E `test_controle_par_famille_cas_sain_et_artefacts` |
| R02 | (a) marqueur jamais levé | attrapée | E `test_deux_paliers_…[2-10-True-True]` |
| R03 | (a) marqueur levé dès 10 % juste | attrapée | E `test_deux_paliers_…[1-10-True-False]` |
| R04 | (a) classe non écrite dans la table d'édition | attrapée | E `test_classes_action_non_valide_et_controle_manque` |
| R05 | (a) marqueur non recopié au résultat de la famille | attrapée | F `test_jouet_part_non_editable_haute_…` |
| R19 | (a) contenu borné : classe des lignes d'édition non relue | attrapée | F `test_point_5_contenu_borne_des_sorties_de_texte_…[…textes-distillation…]` |
| R06 | (d) règle du nom de carte retirée | attrapée | E `test_nom_de_carte_nombres_comptes_…[150…]` |
| R07 | (d) réserve retirée (la règle joue quand le premier nombre est collé) | attrapée | E `test_nom_de_carte_nombres_comptes_…[120h on A100s]` |
| R08 | (d) « collé » ne regarde que la lettre d'avant | attrapée | E `test_nom_de_carte_nombres_comptes_…[300 GPU-hours on 8x A100s]` |
| R09 | (d) contrôle par action : drapeau du lecteur gelé | attrapée | E `test_nom_de_carte_cas_sains_…[150…]` |
| R10 | (d) localisation : tous les nombres du champ brut comptent | attrapée | même essai |
| R18 | (d) action d'origine : drapeau du lecteur gelé | attrapée | même essai |
| R11 | (c) plus de deux instances admises dans la ligne de relance | attrapée | F `test_registre_relance_bornee_…` |
| R12 | (c) coupures au-delà de l'enveloppe admises | attrapée | même essai |
| R13 | (c) une relance comptée contre le plafond commun | attrapée | F `test_depense_deux_compteurs_…` |
| R14 | (c) coupure de l'instance non gardée | attrapée | même essai |
| R20 | (c) le lanceur ne passe pas « relance » à la garde de dépense | attrapée | L `test_depense_cas_sain_et_artefacts_coupure_et_plafond` |
| R15 | (f) instance 6 à trois membres : 24 USD | attrapée | F `test_configuration_artefacts_…[membres_apprentissage-3-coupure]` |
| R16 | (f) instance 6 à trois membres : heures de deux membres | attrapée | F `test_table_du_devis_a_trois_membres_instances_6_et_7` |
| R17 | (f) entrée du devis choisie à l'envers | attrapée | F `test_configuration_reelle_cas_sain_…` |
| M08, M09, M17 | épissure décalée, épissure élargie, action non éditable pour un seul membre (premier tour) | attrapées | E (essais du premier tour) |
| M11 | actions non éditables gardées dans les cibles (premier tour) | attrapée | F `test_action_non_editable_ignoree_…` |
| V04, V06 | contenu d'adaptateur non relu ; activation glissée dans l'évaluation (vérificateur) | attrapées | F `test_point_5_sorties_permises_…` ; F `test_jouet_de_bout_en_bout_…` |
| P07, P08, P09, P15, P16, P17 | contenu borné (deuxième tour) | attrapées | F (essais du contenu borné) |

**Bilan. 32 défauts réintroduits, 32 attrapés** : les 20 de ce tour, et les 12 des tours précédents dont le code visé a changé. Aucune mutation équivalente, aucune manquée. M16 (« part admise jusqu'à 50 % ») n'a plus son « avant » : R01 la remplace. Journal et sortie dans le bloc-notes, aux empreintes du § 8.

## 4. Interfaces changées, et consignes pour la session

- **Sous-commande `depense`** du lanceur : `depense N MEMBRES CUMUL_INSTANCE PRIX_INSTANCE_H CUMUL_COMMUN PRIX_COMMUN_H RELANCE` (sept arguments au lieu de six). `CUMUL_COMMUN` est le cumul de toutes les pièces du devis, **sans** la dépense d'aucune relance (celle de la première marche d'une instance tombée y reste) ; pour une relance (`RELANCE=1`), il n'est pas lu, et seule la coupure de l'instance remplacée est gardée.
- **`depense_session(n, membres, cumul_instance, prix_instance, cumul_commun, prix_commun, *, relance)`** : `relance` sans défaut.
- **Ligne `GO-RELANCE-FORMATION-B5F`** : deux instances au plus, 56 USD de coupures au plus ; sinon toute lecture du registre propre est refusée (la marche, et chaque commande du lanceur) : la mère doit donc relire la ligne avant de l'inscrire.
- **À 39 adaptateurs** (`SCELLEMENT-B5F` : « membres-apprentissage 3 ; piece famille ») : les instances 6 et 7 sont acceptées, à 28 et 17 USD ; `plan` imprime les deux entrées.
- **Sorties** : chaque ligne de la table d'édition porte une clé `classe` ; le contrôle de chaque tirage porte `part_non_editable_haute` et `part_par_motif` ; le statut d'une famille formée porte `part_non_editable_haute`. Le lecteur de l'audit lit le marqueur au résultat de la famille.
- **Nom de carte** : dans les lignes d'évaluation, le drapeau « plusieurs nombres » du lecteur gelé reste levé sur les actions qui nomment une carte, pour tous les membres à la fois.

## 5. Python 3.11

Refait : le paquet joué sur l'instance a changé, et l'environnement du deuxième tour avait été perdu avec `/dev/shm`. Python 3.11.18, torch 2.14.1+cpu, `requirements-gpu.txt` (transformers 5.18.0, tokenizers 0.23.2) : **235 passés en 84 s**, sortie d'erreur vide, sur l'arbre que l'amorce extrait (sortie : `sortie-essais-paquet-python311-v5.txt`, dossier des outils). Ce que l'essai ne montre pas reste ce que disait le rapport v4 (la carte, torch pour CUDA).

## 6. Ce qui reste, et ce qui menace le gel

1. La vérification de ce tour par le contre-lecteur.
2. Le plancher, à remesurer au commit de la course (235 aujourd'hui, sur l'arbre de travail extrait sans commit).
3. Les mutations des tours précédents n'ont pas toutes été rejouées : seules les douze dont le code visé a changé à ce tour (§ 3) ; les 325 essais passent.
4. La part d'actions non éditables, inconnue chez le saboteur instruit : le nom de carte et les paliers la réduisent ; « 2k » et les intervalles sortent toujours.

## 7. Essais : commande, compte, plancher

Depuis la racine du dépôt, temporaires hors du disque (une commande) :

```
TMPDIR=/dev/shm PYTHONPATH=src .venv/bin/python -B -m pytest -q -p no:cacheprovider --basetemp=/dev/shm/b5f-essais tests/test_barreau5_familles_edition_cout_v1.py tests/test_barreau5_familles_engagement_v1.py tests/test_barreau5_familles_formation_v1.py tests/test_lancer_b5f_formation_v1.py tests/test_amorce_b5f_formation_v1.py tests/test_amorce_b5f_formation_entiere_v1.py
```

- Six fichiers, état final : **325 essais** (E 124, G 23, F 88, L 36, A 45, AE 9), **325 passés**, joués par fichier sur leur état final (E : 124 en 3 s ; G et F : 111 en 80 s ; L : 36 en 163 s ; A et AE : 54 en 217 s, la passe de mutations tournant en même temps). Au deuxième tour : 279 ; quarante-six essais de plus (E + 38, F + 6, L + 2), et des essais existants retournés là où le texte a changé (instances 6 et 7 à trois membres, sous-commande `depense`).
- Paquet joué sur l'instance (`tests/test_barreau5_familles_*.py`) : 235 essais ; sur l'arbre que l'amorce extrait, tiré de l'arbre de travail sans commit, par la commande de l'étape 4 : **235 passés** sous Python 3.13.18 (79 s) et sous Python 3.11.18 (84 s). Plancher : **235**.

## 8. Empreintes finales

Code et essais, dans l'arbre de travail du dépôt, état final (sha256 ; la mère les scelle au versement). Ce sont les fichiers des 325 essais passés (§ 7), de la passe de mutations (même contenu) et, pour le paquet, de l'essai sous Python 3.11.

| fichier | sha256 | ce tour |
|---|---|---|
| `src/controle_ia/barreau5_familles/__init__.py` | `b8d53a9905ab172f7e1d0377aef615b343e266624040b0c89399c78f62b365d8` | inchangé |
| `src/controle_ia/barreau5_familles/edition_cout_v1.py` | `23002f43a02e057a5efd2ed160f21e372a754bbad8e951ee6cbe3ed34566cf9a` | (a), (d) |
| `src/controle_ia/barreau5_familles/engagement_v1.py` | `565d4e51eccd82562f3f00e7bd020beba525ac09b782905151a38e72ca536396` | inchangé |
| `src/controle_ia/barreau5_familles/formation_v1.py` | `a56602c3a488f5775ca0f1ce63afb19e8a7ae2e30a5e762b7f25e4af0075c183` | (a), (c), (f) |
| `scripts/lancer_b5f_formation_v1.sh` | `5cc9023aa44a1ede2ae876f6bb950b1ea8976cf2a7f1eb60c47bd012c0e9385a` | (c) |
| `scripts/amorce_b5f_formation_v1.sh` | `5bd91c1c3d0cbb2bcecbdf18ca60fb3ae60da9366074b376ef97e3b89569193a` | plancher |
| `tests/test_barreau5_familles_edition_cout_v1.py` | `e83f45a3a0c77cb9695c47a1f04e18d5fce6b105662b230bdf4fe097637551df` | trente-huit essais |
| `tests/test_barreau5_familles_engagement_v1.py` | `fd72d1db00916a06404e37e6c213536b914820a43b435dd8abe5381c42384874` | inchangé |
| `tests/test_barreau5_familles_formation_v1.py` | `2fad8862eefb505e1e8611f8a76a2ab8425766f47d097421bba49028a17c7def` | six essais, quatre retournés |
| `tests/test_lancer_b5f_formation_v1.py` | `af33ad2096563955e455f7aef2a0619b8aa25d80a5d13ee84368332319d1b047` | deux essais, quatre retournés |
| `tests/test_amorce_b5f_formation_v1.py` | `5e913a944300606970e6c08fde0cdad2d5d41d3308efab682a3048c54d364a42` | inchangé |
| `tests/test_amorce_b5f_formation_entiere_v1.py` | `77f1841b9179a220209192405e407a2533ef9af1459fe1ea2eb33d5a0d0be687` | inchangé |

Outils et sorties, dans `outils-developpeur-corrections-code-formation-v5/` (compagnons scellés) : `mutations-dev-corrections-v5.py` (`ff086bae279fbf4d9e618b3cca99a9f95349a32baac8c94c4259b62e7a1d6bf0`), `sortie-essais-paquet-python311-v5.txt` (`c9e50c9e03599108317826895e86f39e793b23f7e4d5159bde3be3e4cf8a0fc7`).

Dans le bloc-notes de la session, à verser par la mère si elle les garde : `/tmp/claude-0/-home-user-controle-ia-travail/8282ab93-0983-5813-b791-a7a522157dcd/scratchpad/dev-corrections-b5f-v5/journal-mutations-dev-corrections-v5.txt` (`8e0185321cc74d8125568cc3f99c23d39517ad2ce166fdc0ee5f82a1477a6a63`) et `/tmp/claude-0/-home-user-controle-ia-travail/8282ab93-0983-5813-b791-a7a522157dcd/scratchpad/dev-corrections-b5f-v5/sortie-mutations-dev-corrections-v5.json` (`df293f96949e65d269dc0cf1091438992222b2658b00b68733961307603570da`).

Temporaires effacés par leurs chemins écrits en toutes lettres : `/dev/shm/b5f-mut-v5`, `/dev/shm/b5f-py311-t3`, `/dev/shm/b5f-arbre-extrait-t3` et son dossier de temporaires, les temporaires d'essais `/dev/shm/b5f-f3`, `/dev/shm/b5f-l3`, `/dev/shm/b5f-a3`, et le dossier vide `/dev/shm/torchinductor_root` que torch y a créé pendant mes essais.
