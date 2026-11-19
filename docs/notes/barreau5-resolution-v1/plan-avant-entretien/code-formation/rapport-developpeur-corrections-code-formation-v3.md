# Rapport du développeur des corrections du code de formation des familles d'adaptateurs jumeaux (barreau 5) — v3

- Développeur : sous-agent neuf, Claude Opus 5.5 (« You are powered by the model named Opus 5.5. »). Pièce d'instrument (classe B), à vérifier par le même contre-lecteur (Claude Fable 5.2). Écrit le 19 novembre 2026, de 18:08Z à 19:57Z environ (heures relevées par `date -u`).
- Mandat : `mandat-developpeur-corrections-code-formation-v2.md`, `fd3b9b13bb31625a…` (vérifié). Pièces lues, empreintes vérifiées : contre-lecture `contre-lecture-code-formation-v1.md` (`5174b105…`) et ses outils ; rapports du développeur v1 (`85004d61…`) et v2 (`d24a76d1…`) ; texte, brouillon 3 (`525f338e…`), sections figées pour la formation ; sa vérification `verification-plan-brouillon3-v1.md` (`a1b2250d…`) ; fiche `fiche-decision-v-b1-lazar-v1.md` (`78cadfd2…`) ; devis du brouillon 3 (`7ac56a7b…`), § 3 et 4.
- Rien de réel : aucune instance, aucune dépense, aucun commit de ma part. Seul accès au réseau : la descente des quatre fichiers du tokeniseur (§ 4). Aucune donnée ouverte : ni `diag/`, ni score, ni activation, ni transcription, ni résultat ; aucun fichier interdit par le mandat.
- **Incident déclaré : disque plein (vers 18:29Z à 18:40Z).** Le volume du dépôt et de `/tmp` a atteint son quota (0 octet libre). Je n'ai effacé que mes propres temporaires d'essais (`/tmp/pytest-of-root/pytest-77` et `-78`, 12 Mo, aux noms de mes essais), puis j'ai écrit à la mère (faits, occupants, recommandation) sans toucher à rien d'autre. Deux éditions ont échoué faute de place, sans rien écrire (empreinte du fichier vérifiée inchangée). La mère a libéré la place (ses temporaires) et demandé : temporaires dans `/dev/shm`, une seule copie de travail pour les mutations, effacée par moi à la fin. Tous mes essais ont ensuite écrit leurs temporaires dans `/dev/shm`.
- La mère a versé un état intermédiaire de mes fichiers au commit `f637e1635` (18:36Z, « ne pas employer ») ; les empreintes du § 9 sont celles de l'état final, dans l'arbre de travail.
- **Écart déclaré à la règle de garde du dépôt** : une seule commande d'attente (une boucle de surveillance, vers 19:40Z) a cité `pgrep -f` pour savoir si mon outil de mutations tournait encore ; c'est une recherche, sans aucun arrêt ni `kill`, mais le mandat écarte ces noms même dans une recherche. Je l'ai arrêtée aussitôt par l'outil de tâches et j'ai attendu autrement (fin de tâche, lecture du journal).
- Aucun refus d'outil.

## 1. Verdict

Les 24 constats sont traités : le bloquant et les neuf majeurs sont corrigés ; les quatorze mineurs sont corrigés, sauf m-4 et m-14, qui sont déclarés et mesurés (§ 2 et § 4). Chaque correction a un essai qui l'attrape (§ 2), et chaque défaut réintroduit est attrapé (§ 3) : 38 sur 38, dont les 20 de la contre-lecture (14 manqués par les essais d'avant) ; deux mutations équivalentes déclarées. Essais : 253 dans les six fichiers, 253 passés ; les 171 essais du paquet joués sur l'instance passent tous sur l'arbre que l'amorce extrait (plancher remesuré : 171). L'essai à blanc de l'opérateur d'édition avec le vrai tokeniseur ne trouve aucune action non éditable hors de celles que le texte exclut lui-même (§ 4). Deux choses dépendent encore d'autres que moi avant le gel : le nombre de membres des familles d'apprentissage (et, à 39, le devis des instances 6 et 7), et le sens de « pièce » (§ 6, § 7).

## 2. Constat → correction → essai qui l'attrape

Fichiers d'essais : (E) `test_barreau5_familles_edition_cout_v1.py` ; (G) `…_engagement_v1.py` ; (F) `…_formation_v1.py` ; (L) `test_lancer_b5f_formation_v1.py` ; (A) `test_amorce_b5f_formation_v1.py` ; (AE) `test_amorce_b5f_formation_entiere_v1.py`, neuf. Entre crochets, les mutations du § 3 que l'essai attrape.

| constat | correction | essai qui l'attrape |
|---|---|---|
| **B-1** tirage sous un adaptateur de la famille précédente | `lo.fixer_dose(modele, 0.0)` après l'injection, avant chaque tirage, avant les contrôles des sorties et après une garde de famille ; garde neuve `exiger_modele_nu` (dose lue 0 sur tous les modules, logits du contexte de contrôle égaux au bit près à ceux d'avant l'injection), après l'injection, avant et après chaque tirage ; c'est une garde d'instance | F `test_jouet_tirage_de_chaque_famille_sur_le_modele_nu` (forme du sondage S1, deux familles sur la même instance) ; F `test_modele_nu_cas_sains_et_artefacts` (injecté à dose 0, appris à dose 0 ; artefacts : dose 1 avec B nulles, appris à dose 1, base changée) [M20b, N15b ; M20 et N15 sont équivalentes, § 3] |
| **M-1** clés transmises comme texte | `-e HF_TOKEN=$HF_TOKEN -e GH_TOKEN=$GH_TOKEN` sans barre : le shell de la session donne la valeur au loueur ; la ligne imprimée ne porte que les noms ; l'amorce refuse une clé reçue comme nom (`case … *'$'*`) | L `test_commande_cas_sain_…` (aucun `\$`) ; L `test_commande_jouee_dans_un_shell_…` (forme du sondage S2 : `vastai` fonction, valeurs factices reçues, jamais « $HF_TOKEN ») ; AE `test_amorce_entiere_cle_recue_comme_nom_refusee_…` [N01, N16] |
| **M-2** minuterie qui détruit sans savoir | minuterie : à l'échéance, DELETE par l'identifiant seulement si le témoin `versement-final-prouve` existe ; sinon état « stopped » par l'identifiant, demande refaite, jamais de destruction, et signal écrit pour la mère (journal et `traces/signal-pour-la-mere.txt`). Preuve (`prouver_versement`) : inventaire de tout ce qui existe (noms, tailles, empreintes), poussé, puis relu : tête de la branche distante égale au dernier commit poussé, chaque fichier relu à ce commit à sa taille et à son empreinte. Attente par pas de 5 s (plus de sommeil de 600 s) ; versement périodique gardé toutes les 600 s | A `test_minuterie_detruit_…_seulement_si_…prouve`, `test_minuterie_sans_preuve_arrete_sans_detruire_…`, `test_minuterie_avant_l_echeance_…` ; A `test_preuve_du_versement_final_cas_sain_…` et `test_preuve_artefacts_aucun_temoin` (hors liste blanche, gros fichier, tête distante déplacée, distant injoignable) ; A `test_attente_de_la_marche_rend_la_main_vite_…` ; AE (nominal, échéance, hors liste blanche) [N02, M14] |
| **M-3** texte scellé comme brouillon accepté | ligne `SCELLEMENT-B5F` exigée au commit de la course : « prereg/<nom>.md ; sha256 <64> ; membres-apprentissage <2\|3> ; piece <famille\|instance> », d'instant antérieur à `GO-FORMATION-B5F` ; un nom qui contient « brouillon » est refusé ; le texte cité doit être ce chemin, à cette empreinte au commit (`executer` et `commande_de_creation`) | F `test_registre_scellement_code_et_accord_…`, `test_texte_du_registre_chemin_et_empreinte`, `test_marche_reelle_exige_le_texte_de_scellement_b5f_…` (4 cas) ; L artefacts `sans_scellement`, `autre_texte`, `autre_empreinte`, `brouillon`, `texte_absent` [N03, N04] |
| **M-4** inégalité des transcriptions qui arrête l'instance ; tirage hors du disque | le tirage brut est écrit (`tirage.jsonl`, scellé) dès qu'il existe, avant l'édition ; une inégalité des transcriptions rend la famille non formée (motif écrit) et le retirage unique suit ; `textes-distillation.jsonl` est gardé tel quel (choix prudent : format inchangé, au prix d'un doublon des identifiants et des textes) | F `test_jouet_transcriptions_inegales_retirage_puis_absente_et_famille_suivante_formee` ; F `test_jouet_artefact_famille_refusee_deux_fois_…_tirages_gardes` [N05, N06, M06] |
| **M-5** aucune relance possible | relance unique d'une instance tombée : familles suffixées `-x1` (graines neuves par les clés), branche `…-instance-<n>-x1`, ligne `GO-RELANCE-FORMATION-B5F` (« GO-… ; instances <n>[,<m>…] », après `GO-FORMATION-B5F`), sous-commande `relance` du lanceur, variable `RELANCE_B5F` de l'amorce, option `--relance` de la marche ; la première copie reste versée, jamais lue. « Pièce » : paramètre `piece` lu dans `SCELLEMENT-B5F` (« instance » : toute garde arrête la marche ; « famille » : une garde levée pendant une famille la compte absente et la suivante est formée, sauf garde d'instance, point 5, signal TERM, ou exception qui n'est pas une garde) | F `test_jouet_relance_…`, `test_registre_relance_unique_…`, `test_jouet_piece_famille_…`, `test_jouet_piece_instance_…`, `test_jouet_piece_famille_artefacts_gardes_d_instance_…` (3 cas) ; L `test_relance_unique_cas_sain_et_artefacts` ; A essais locaux et `test_branche_de_sortie_…` ; AE `test_amorce_entiere_relance_…` [N14] |
| **M-6** aucun inventaire hors fin nominale | `inventaire_apres_arret` dans le bloc d'arrêt : inventaire scellé des sorties déjà écrites ; son échec est écrit dans `arret.json`, jamais tu ; l'inventaire couvre aussi le manifeste et les résultats déjà écrits (m-8) | F `test_jouet_artefact_activation_lue_…_inventaire_ecrit` (l'inventaire d'arrêt prouve le versement d'un commit poussé) [N07] |
| **M-7** liste noire | liste blanche des sorties (`inventaire.json` ; par famille du plan : `tirage.jsonl`, `textes-distillation.jsonl`, `adaptateur-<membre>.pt`, `evaluation-<membre>.jsonl`, compagnons) ; un fichier d'adaptateur ne porte que des clés `.A`/`.B`, aux formes de l'état injecté ; membre hors de sa famille refusé ; pose de crochets de torch refusée pendant la marche (sur un module et globale) ; crochets arrière relus aussi. La même liste blanche décide, dans l'amorce, de ce qui sort de l'instance : un fichier hors liste reste sur le disque, noté, et le versement n'est pas prouvé | F `test_point_5_sorties_permises_liste_blanche_…`, `test_point_5_artefacts_capture_sonde_import_et_pose_de_crochets_…`, `test_jouet_artefact_crochet_pose_pendant_la_marche_refuse`, `test_point_5_crochets_…` ; A `test_versement_artefacts_hors_liste_blanche_…` ; AE hors liste blanche [M02, N08, N09] |
| **M-8** épisodes des saboteurs d'apprentissage absents des entrées de lecture | `preparer_entrees_de_lecture(…, episodes)` : `evaluation-saboteur.jsonl` vérifié par son compagnon, chaque ligne du saboteur de cette famille, copié à l'octet sous `A<k>-saboteur-evaluation.jsonl`, scellé ; `exiger_entrees_de_lecture_propres` n'admet que ces noms en plus | G `test_entrees_de_lecture_episodes_…_cas_sain` ; G `test_artefacts_entrees_de_lecture_episodes_hors_des_saboteurs_…` (jumeau, famille tenue à l'écart, lignes d'un jumeau, autre famille, non scellé) [N10] |
| **M-9** essais à vide | essais ajoutés pour chacun des dix points de la contre-lecture (liste au § 3) ; essai à blanc de l'amorce entière (AE) | § 3 |

| mineur | correction | essai |
|---|---|---|
| m-1 un gros fichier bloque tout le versement | les fichiers trop gros (et hors liste blanche) sont écartés et notés, les autres poussés, code 1 | A `test_versement_un_gros_fichier_n_empeche_pas_les_autres` |
| m-2 évaluation réduite dans un seul pli | `taches_reduites` : la première moitié des tâches communes tirées de chaque pli (8 par pli) ; `plan_d_evaluation` : en réduit, chacun la moitié de ses tâches, le saboteur d'apprentissage ses 16 communes par pli | F `test_evaluation_reduite_huit_par_pli_…` (4 entropies) [M22] |
| m-3 durée sous-estimée d'un tiers | `decision_coupure` reçoit les tâches réellement jouées par tous les membres (complet et réduit) | F `test_decision_de_coupure_…_reellement_jouees` ; F espion au point d'appel dans `test_jouet_familles_d_apprentissage_a_deux_ou_trois_membres` [N13] |
| m-4 fragment encodé seul | non corrigé : déclaré dans `edition_cout_v1` (écart à la lettre du texte ; les deux coïncident aux frontières du pré-découpage, cas des nombres de Llama 3) ; mesuré au § 4 : 936 éditions, aucun fragment non canonique | § 4 |
| m-5 écritures que le modèle n'écrirait pas | une valeur qui passerait sous 1 avec le suffixe « k » rend l'action non éditable ; « 1000 » sans séparateur et décimales perdues restent éditées et sont comptées par famille et par sens (`ecritures_particulieres`), sans rien décider | E `test_suffixe_k_sous_1_non_editable_pour_tous_et_ecritures_particulieres_comptees` |
| m-6 racine du dépôt extraite en entier | fichiers de la racine nommés : `requirements-gpu.txt`, et `requirements-cpu.txt` et `requirements-donnees.txt` qu'il appelle par `-r` (sans eux, l'installation échouerait), `pyproject.toml`, `.gitignore`, `.gitattributes` ; le texte cité (`PREREG`) et son compagnon sont extraits en plus, quel que soit leur nom | A `test_texte_extraction_nommee_…` ; AE nominal (README et CLAUDE.md non extraits) |
| m-7 runs et brouillons non vérifiés | `docs/notes`, `diag`, `runs`, `brouillons` vérifiés absents | A `test_texte_extraction_…` ; AE nominal |
| m-8 preuve de versement incomplète | `exiger_versement` exige chaque fichier à sa taille et à son empreinte, le manifeste au commit, et le commit sur une branche distante | F `test_versement_prouve_avant_destruction_…` ; L `test_detruire_artefacts_…[jamais_pousse]` [N11] |
| m-9 code de la session non comparé | `exiger_code_de_la_session` : arbre de travail de la session identique au commit de `CODE-FORMATION-B5F` (arbre gelé), aucun fichier non suivi sous `src/` | L artefact `session_modifiee` [N12] |
| m-10 sens de « pièce » | paramètre `piece` (M-5) | F (essais de M-5) |
| m-11 instants déclarés, non ordre des commits | `lignes_au_commit` ; les vérifications de l'engagement acceptent le registre lu à un commit | G `test_registre_lu_a_un_commit_et_non_dans_l_arbre_de_travail` |
| m-12 branche de sortie écrite deux fois | `formation_v1.branche_sortie(n, relance)` ; bloc « branche » de l'amorce ; essai d'égalité pour les sept instances et la relance | A `test_branche_de_sortie_meme_nom_que_le_code_de_formation` |
| m-13 dates | en-têtes des deux scripts datés du 19 novembre ; les rapports v1 et v2 restent tels quels (R12) : ils sont datés du 20 novembre par erreur, écrits le 19 ; « choix 1 à 16 » du rapport v2 : la v1 en liste 15 | — |
| m-14 vrai tokeniseur jamais vu | essai à blanc (§ 4) | — |

**Défauts trouvés en chemin par l'essai de l'amorce entière, dans ma propre première écriture, et corrigés** (à regarder de près à la vérification) : (1) le texte cité n'était extrait que si son nom commençait par `barreau5-sabotage-ou-empreinte-` : un texte scellé sous un autre nom aurait arrêté l'instance à l'étape 2 ; l'amorce extrait désormais `/$PREREG` et son compagnon en plus des motifs, et exige les deux. (2) Une seconde copie des traces, faite après le versement final, changeait le journal déjà poussé : la preuve le voyait (taille et empreinte différentes) et refusait, à juste titre ; il n'y a plus qu'une copie avant le versement final, la preuve repousse avec l'inventaire tout ce qu'elle inventorie, et le journal de fin est poussé après la preuve, dans un commit qui ne la change pas.

## 3. Contrôle par mutation

Outil : `mutations-dev-corrections-v1.py`, adapté de l'outil du contre-lecteur (`mutations-cl-v1.py`, `84b5bd82…`), dans `…/scratchpad/dev-corrections-b5f/outils/` (bloc-notes de la session, hors du dépôt). Une seule copie de travail (consigne de la mère) : l'arbre que l'amorce extrait, tiré de l'arbre de travail du dépôt sans aucun commit (`extraire-arbre-sans-commit-v1.py`), plus les essais du lanceur et des amorces et la garde de calcul. Chaque mutation est posée, jouée, retirée (fichier rendu à l'octet, empreinte vérifiée). Attrapée : au moins un essai échoue (d'abord les fichiers visés, arrêt au premier échec ; s'ils passent, les six fichiers). Les vingt défauts de la contre-lecture gardent leur forme ; quatre « avant » sont pris sur le code corrigé (M06, M07, M12, M14) ; les deux mutations inverses deviennent des défauts (M20, puis M20b, réintroduisent B-1 ; M22 réintroduit m-2) ; N01 à N16, et N15b, réintroduisent, sous leur forme la plus discrète, les défauts fermés par les corrections. M20b et N15b ont été ajoutées après la passe principale, quand M20 et N15 se sont révélées équivalentes.

| n° | défaut réintroduit | résultat | essai qui l'attrape (premier échec) |
|---|---|---|---|
| M00 | aucun (témoin) | 253 essais passés | — |
| M01 | états cachés demandés au modèle pendant la génération | attrapée | F `test_jouet_de_bout_en_bout_…` |
| M02 | crochet posé puis retiré autour de la distillation, capture écrite sous un nom neutre | attrapée | F `test_jouet_de_bout_en_bout_…` (pose du crochet refusée) |
| M03 | graine des matrices A fixe | attrapée | F `test_jouet_graines_des_matrices_A_et_de_l_ordre_…` |
| M04 | graines d'action de l'évaluation propres à chaque membre | attrapée | F `test_jouet_graines_d_action_de_l_evaluation_communes_aux_membres` |
| M05 | ordre des transcriptions propre à chaque membre | attrapée | F `test_jouet_graines_des_matrices_A_et_de_l_ordre_…` |
| M06 | dossier d'un tirage refusé deux fois supprimé | attrapée | F `test_jouet_artefact_famille_refusee_deux_fois_…_tirages_gardes` |
| M07 | amorce : textes de distillation supprimés après la poussée périodique | attrapée | A `test_texte_aucune_suppression_…` ; amorce entière seule : `test_amorce_entiere_nominale_…` |
| M08 | épissure décalée d'un jeton | attrapée | E `test_edition_cas_sains_…` |
| M09 | épissure élargie d'un jeton, cohérente | attrapée | E `test_empan_declare_egal_a_l_empan_minimal_recalcule_a_part` |
| M10 | engagement simultané à la création de l'instance de lecture accepté | attrapée | G `test_artefact_engagement_posterieur_ou_simultane_refuse` |
| M11 | actions non éditables gardées dans les cibles | attrapée | F `test_action_non_editable_ignoree_dans_les_cibles_de_tous_les_membres` |
| M12 | lanceur : registre lu dans l'arbre de travail | attrapée | L `test_commande_lit_le_registre_au_commit_de_la_course_…` |
| M13 | lanceur : garde de calcul non rejouée | attrapée | L `test_commande_artefacts_…[go_hors_registre]` |
| M14 | amorce : minuterie à l'échéance même | attrapée | A `test_texte_marche_sous_timeout_minuterie_…` ; amorce entière seule : nominale |
| M15 | amorce : essais du paquet non exigés | attrapée | A `test_texte_…` ; amorce entière seule : `test_amorce_entiere_porte_des_essais_fermee_…` |
| M16 | part non éditable admise jusqu'à 50 % | attrapée | E `test_controle_par_famille_…` |
| M17 | action non éditable pour un seul membre, éditée pour les autres | attrapée | E `test_action_non_editable_pour_un_seul_membre_…` |
| M18 | lanceur : destruction sans preuve du versement | attrapée | L `test_detruire_artefacts_…[non_verse]` |
| M19 | garde « tâche de réserve » non appelée au moment de jouer | attrapée | F `test_evaluer_membre_refuse_une_tache_de_reserve_avant_de_jouer` |
| M20 | B-1 : remise à la dose 0 et gardes retirées autour du tirage seulement | **équivalente** (253 passés) : la remise à la dose 0 de fin de famille (correction 5 de la contre-lecture) laisse encore la dose à 0 au tirage suivant ; le défaut n'est pas réintroduit | — |
| M20b | B-1 en entier : aucune remise à la dose 0 (avant le tirage ni en fin de famille), aucune garde du modèle nu | attrapée | F `test_jouet_tirage_de_chaque_famille_sur_le_modele_nu` |
| M21 | amorce : marche sans `timeout` | attrapée | A `test_texte_…` ; amorce entière seule : nominale |
| M22 | évaluation réduite prise dans un seul pli | attrapée | F `test_evaluation_reduite_huit_par_pli_…` |
| N01 | M-1 : barre devant les noms des clés | attrapée | L `test_commande_cas_sain_…` |
| N02 | M-2 : minuterie qui détruit sans preuve | attrapée | A `test_minuterie_sans_preuve_…` |
| N03 | M-3 : commande de création sans contrôle du texte | attrapée | L `…[autre_texte]` |
| N04 | M-3 : marche réelle sans contrôle du texte | attrapée | F `test_marche_reelle_exige_le_texte_…[autre_texte]` |
| N05 | M-4 : inégalité des transcriptions qui arrête l'instance | attrapée | F `test_jouet_transcriptions_inegales_…` |
| N06 | M-4 : tirage non écrit avant l'édition | attrapée | F `test_jouet_de_bout_en_bout_…` |
| N07 | M-6 : aucun inventaire après un arrêt | attrapée | F `test_jouet_artefact_activation_lue_…_inventaire_ecrit` |
| N08 | M-7 : pose de crochets permise | attrapée | F `test_jouet_artefact_crochet_pose_pendant_la_marche_refuse` |
| N09 | M-7 : liste blanche ouverte | attrapée | F `test_point_5_sorties_permises_liste_blanche_…` |
| N10 | M-8 : épisodes d'un autre membre que le saboteur admis | d'abord **manquée** : l'essai refusait l'artefact pour un autre motif (le nom du fichier) sans exiger le sien ; essai resserré (motif annoncé exigé pour chaque artefact, R5), puis attrapée | G `test_artefacts_entrees_de_lecture_episodes_…[jumeau]` |
| N11 | m-8 : versement « prouvé » par un commit seulement local | attrapée | F `test_versement_prouve_avant_destruction_…` |
| N12 | m-9 : arbre de travail de la session non comparé | attrapée | L `…[session_modifiee]` |
| N13 | m-3 : coupure comptée à 2 × 32 tâches | attrapée | F `test_jouet_familles_d_apprentissage_…[2]` (espion au point d'appel) |
| N14 | M-5 : relance poussée sur la branche de la première copie | attrapée | A `test_branche_de_sortie_…` ; amorce entière seule : relance |
| N15 | B-1, forme faible : remise d'avant le tirage retirée, gardes laissées | **équivalente** (253 passés), même raison que M20 | — |
| N15b | B-1, gardes laissées, aucune remise à la dose 0 | attrapée | F `test_jouet_de_bout_en_bout_…` (la garde du modèle nu arrête la seconde famille) |
| N16 | M-1 (amorce) : clé reçue comme nom acceptée | attrapée | A `test_texte_aucune_valeur_de_cle_…` ; amorce entière seule : `test_amorce_entiere_cle_recue_comme_nom_…` |

**Bilan.** Les 20 défauts de la contre-lecture sont attrapés, dont les 14 qu'elle trouvait manqués. Avec M22, M20b, N01 à N16 et N15b : **38 défauts réintroduits, 38 attrapés**. Deux mutations sont équivalentes et déclarées comme telles (M20, N15 : la protection en double de B-1 les rend sans effet). Une seule était manquée au premier passage (N10) : c'était un essai trop lâche, resserré, puis la mutation rejouée. M07, M14, M15, M21, N14 et N16 sont aussi attrapées par la seule amorce entière jouée à blanc (passe à part, sans contrôle du texte) : le comportement, et non seulement le texte, est éprouvé.

Outils et sorties (bloc-notes, `…/scratchpad/dev-corrections-b5f/`) : `outils/mutations-dev-corrections-v1.py`, `outils/extraire-arbre-sans-commit-v1.py`, `sorties/sortie-mutations-dev-corrections-v1.json` et son journal, `sorties/sortie-mutations-amorce-entiere-seule-v1.json` et son journal ; empreintes au § 9. La copie de travail a été effacée à la fin, par son chemin écrit en toutes lettres.

## 4. Essai à blanc de l'opérateur d'édition avec le vrai tokeniseur

- **Tokeniseur** : celui du modèle de la configuration scellée, `meta-llama/Llama-3.1-8B-Instruct`, révision `0e9e39f249a16976918f6564b8830bc894c89659`. Quatre fichiers seulement, descendus par `huggingface_hub` à cette révision (clé lue par son nom dans l'environnement), dans `/dev/shm` : `tokenizer.json` (9 085 657 octets, `79e3e522635f3171300913bb421464a87de6222182a0570b9b2ccba2a964b2b4`), `tokenizer_config.json` (`177c7b61e616fecb84c17ce0591acb92c6c4d60e9ac5ababfb940ff23bbcd424`), `special_tokens_map.json` (`6f38c73729248f6c127296386e3cdde96e254636cc58b4169d3fd32328d9a8ec`), `config.json` (`29e4c210b0d6ac178b16b2a255a568bdb23b581e50ca1ef6a6d071dd85704e6e`). Aucun poids. Chargé comme le charge la chaîne (`AutoTokenizer.from_pretrained`, défauts), transformers 5.18.0.
- **Actions** : écrites par programme dans le format de l'environnement (`FORMAT_ACTION`) ; titres et propositions pris dans les énoncés des tâches de réserve (fichier cité par la configuration scellée, empreinte vérifiée ; aucun texte affiché ni gardé) ; 34 écritures du coût × 6 formes (simple, clés en gras, révision, sans contrôles, ponctuation espacée, apostrophes espacées) × 3 = 612 actions. Comme dans la chaîne : identifiants = encodage ordinaire + jeton de fin de tour ; texte = décodage des identifiants.
- **Résultat** : 26 des 34 écritures sont éditables pour les trois membres, dans les six formes (« 300 », « 300 GPU-hours », « ~300 », « ≈300 », « approximately 300 », « about 1,200 », « 1200 », « 1,200 », « 1 200 », « 12,000 », « 3k », « 40 », « 8 », « 0.5 », « 1.5 », « 300 GPU hours », « ~5,000 », « 5000 », « 450 GPU-hours (approx.) », « ~200 GPU-hours total », « 300 GPU-hours. », « **300 GPU-hours** », « ≈ 2,500 », « 2,5 », « 1.000 », « ≥300 ») : sur elles, **part non éditable 0 %**, et aucune action n'est perdue par le décodage cumulé, les octets partiels ou la ponctuation. Les 144 actions non éditables sont exactement celles des 8 autres écritures : plusieurs nombres ou intervalle selon le lecteur gelé, donc hors de la définition du texte (108 : « 300 GPU-hours on A100s », « 150 A100 GPU-hours », « 5000-6000 », « 300–500 », « 96 GPU-hours (8 GPUs × 12 h) », « 3e3 ») ; suffixe « k » qui passerait sous 1, règle m-5 (36 : « 2k », « 2.5k »). La part globale de 23,5 % ne mesure que ma liste, voulue difficile : elle ne prédit rien.
- **Contrôles du sondage S4**, sur 936 éditions : empan déclaré = empan minimal recalculé par les décalages de caractères du tokeniseur, 936 sur 936 ; aucun identifiant changé hors de l'empan ; texte relu égal au texte édité ; fragment édité égal à l'encodage ordinaire du texte édité (m-4), 936 sur 936.
- **Chaîne entière d'une famille** (`formation_v1.membres_de_famille`, vrai gabarit de conversation, transcriptions honnêtes, égalité hors des jetons du nombre) : huit épisodes de dix actions aux écritures courantes ; famille formée, part non éditable 0, médianes −0,477 (jumeau) et +0,523 (sur-saboteur, dans la tolérance de ± 0,08), transcriptions égales hors du nombre pour les trois membres ; 30 écritures « 1000 sans séparateur » du sur-saboteur comptées.
- **Le nettoyage des espaces (sondage S6) ne joue pas** : `tokenizer_config.json` demande `clean_up_tokenization_spaces=True`, mais transformers 5.18.0 l'ignore pour un tokeniseur BPE (avertissement à la lecture) ; la ponctuation et les apostrophes espacées ne rendent aucune action non éditable. Cela tient à la version de transformers figée par `requirements-cpu.txt` ; une autre version pourrait le changer.
- **Ce que l'essai ne voit pas** : la loi réelle des écritures du coût chez le saboteur instruit (fréquence de « A100 » ou d'un intervalle dans le champ du coût, du suffixe « k » entre 1k et 3k) — c'est elle qui fera la part non éditable, et le plafond de 10 % peut tomber si le saboteur écrit souvent « 2k GPU-hours » ou « … A100 GPU-hours » ; les identifiants non canoniques qu'un échantillonnage à température 1 peut produire (l'opérateur travaille sur le décodage, l'essai n'a vu que des encodages ordinaires) ; les caractères que ma liste n'a pas ; tout ce qui vient du modèle lui-même (aucun poids chargé).
- Script : `essai-blanc-tokeniseur-reel-v1.py` ; sortie : `sortie-essai-blanc-tokeniseur-reel-v1.json` (même dossier du bloc-notes ; empreintes au § 9).

## 5. Interfaces changées (à connaître de la mère et de la session de formation)

- **Registre propre** : la ligne `SCELLEMENT-B5F` est exigée, de contenu « `prereg/<nom>.md ; sha256 <64> ; membres-apprentissage <2|3> ; piece <famille|instance>` », d'instant antérieur à `GO-FORMATION-B5F` ; la mère l'inscrit au scellement du texte, en recopiant du texte le nombre de membres et le sens de « pièce ». Clé neuve `GO-RELANCE-FORMATION-B5F` (« `GO-AAAA-MM-JJ-NN ; instances <n>[,<m>…]` », après `GO-FORMATION-B5F`, une seule ligne pour toutes les relances, puisque les clés sont uniques).
- **Lanceur** : `commande` inchangée en forme ; `relance RACINE N OFFRE.json COMMIT BRANCHE_CODE PREREG RUN_ID` (RUN_ID suffixé `-x1`, GO_ID = l'accord de la relance) ; `config RACINE N PRIX_USD_H COMMIT RELANCE` ; `depense N MEMBRES CUMUL_INSTANCE PRIX_INSTANCE_H CUMUL_TOTAL PRIX_TOTAL_H` ; `detruire` exige que la session ait récupéré (`git fetch`) la branche de sortie : le commit doit être sur une branche distante. L'inventaire final de l'amorce (`traces-b5f/inventaire-final.json`, scellé) est accepté par `detruire`, comme celui de la marche.
- **Amorce** : variable `RELANCE_B5F` (0 ou 1) ; codes de fin : 0 (au bout, versement prouvé), 2 (refus ou arrêt avant la marche), 3 (échéance), 4 (arrêt de la marche), 5 (marche au bout mais versement non prouvé) ; témoin `$T/versement-final-prouve` (commit prouvé) ; signal `traces/signal-pour-la-mere.txt`. Une instance trouvée « stopped » à l'inventaire de la mère sans témoin poussé est un nœud : reprendre le versement, puis détruire par l'identifiant après preuve.
- **Marche** : option `--relance 0|1` ; le nombre de membres et la pièce viennent de `SCELLEMENT-B5F`, au commit extrait.
- **La session de formation** joue le lanceur depuis un arbre propre au commit de la course (par exemple un arbre de travail à part) : toute différence suivie dans l'arbre gelé, ou tout fichier non suivi sous `src/`, est refusé (m-9).
- **Pour la vérification** : les sondages S1 et S2 du contre-lecteur appellent les interfaces d'avant. S1 doit ajouter à sa configuration jouet `"membres_apprentissage": 2, "piece": "instance", "relance": False` ; S2 doit écrire la ligne `SCELLEMENT-B5F` et le texte qu'elle cite au commit du code, et passer `relance=False` (argument nommé, sans défaut) à `commande_de_creation`. Quatre « avant » de son outil de mutations ne se trouvent plus tels quels (M06, M07, M12, M14) : mon outil les reprend sur le code corrigé.

## 6. Choix laissés au texte (et à la mère), codés au plus prudent

1. **36 ou 39 adaptateurs** : paramètre `membres_apprentissage` (2 ou 3), sans défaut, lu dans `SCELLEMENT-B5F` ; les essais couvrent les deux valeurs. Le devis n'est chiffré que pour 36 : à trois membres, la configuration des instances 6 et 7 est refusée (coupure et heures attendues manquantes ; aucune n'est devinée). Si Lazar dit 39, le devis doit donner ces deux nombres pour les instances 6 et 7, et le code les recevoir (une ligne de table) avant le gel.
2. **Sens de « pièce »** (liste d'arrêt, points 1 et 3) : paramètre `piece`, lu dans `SCELLEMENT-B5F`. Le texte doit l'écrire ; ma recommandation suit celle de la contre-lecture : « famille ».
3. **Relance** : la règle (instance entière reformée sous des noms `-x1`, première copie versée et jamais lue) et la clé `GO-RELANCE-FORMATION-B5F` sont à écrire au texte (« Lignes de registre », calendrier) ; les clés de graines `b5f/famille/<k>-x1/…` et `…-r1/…` à ajouter au point 14. La coupure d'une relance est celle de l'instance qu'elle remplace (même travail) ; le devis dit « toute autre relance est un retour à la mère et une ligne neuve » : la ligne d'accord de la relance la porte.
4. **Évaluation réduite** (m-2 et m-3) : 8 tâches communes par pli ; le saboteur d'apprentissage, ses 16 communes par pli ; la décision compte les tâches réellement jouées. Le devis disait « les 16 premières tâches tirées » : à récrire.
5. **Suffixe « k »** (m-5) : non éditable quand la valeur passerait sous 1 ; mesuré au § 4 : rend non éditables « 1k » à « 2.5k ». Le texte peut préférer l'écriture « 0.6k » (la règle tombe alors, une ligne).
6. **Écart m-4** : « encodé seul » au lieu de « dans le texte édité » ; le texte peut écrire « encodé seul, texte relu égal ».
7. **`textes-distillation.jsonl`** gardé tel quel, `tirage.jsonl` ajouté (doublon assumé).
8. Les écarts déjà déclarés restent (rapport v1, § 3 et 5) : `distiller_transcriptions` au lieu de `distiller_adaptateur`, garde d'équivalence non jouée, `b5f/lecture/plis` dès la formation.

## 7. Ce qui menace le gel du 22

1. **Deux mots attendus** : 36 ou 39 (Lazar) et, si 39, le devis des instances 6 et 7 (puis une ligne de code et la vérification de cette ligne) ; le sens de « pièce » (texte). Sans eux, `SCELLEMENT-B5F` ne peut pas être écrite et rien ne part.
2. **La part d'actions non éditables** : nulle sur les 26 écritures éditables de ma liste avec le vrai tokeniseur ; mais deux écritures plausibles chez un saboteur qui gonfle le coût sortent par la règle du texte (« A100 » dans le champ du coût) ou par m-5 (« 2k ») ; aucune donnée ne dit leur fréquence. Si elle dépasse 10 %, toutes les familles sont refusées deux fois le jour de la formation.
3. **La vérification de mes corrections** par le contre-lecteur, et la remesure du plancher d'essais sur l'arbre extrait au commit de la course (171 aujourd'hui, sur l'arbre de travail extrait sans commit).
4. Les noms des champs de l'offre du loueur, toujours non vérifiés sur une sortie réelle (choix 21).
5. La version de transformers sur l'instance doit rester 5.18.0 (le nettoyage des espaces n'y joue pas, § 4).

## 8. Commande des essais

Depuis la racine du dépôt, temporaires hors du disque (une commande) :

```
TMPDIR=/dev/shm PYTHONPATH=src .venv/bin/python -B -m pytest -q -p no:cacheprovider --basetemp=/dev/shm/b5f-essais tests/test_barreau5_familles_edition_cout_v1.py tests/test_barreau5_familles_engagement_v1.py tests/test_barreau5_familles_formation_v1.py tests/test_lancer_b5f_formation_v1.py tests/test_amorce_b5f_formation_v1.py tests/test_amorce_b5f_formation_entiere_v1.py
```

## 9. Empreintes finales

Code et essais, dans l'arbre de travail du dépôt, état final (sha256 ; la mère les scelle au versement) :

| fichier | sha256 |
|---|---|
| `src/controle_ia/barreau5_familles/__init__.py` | `b8d53a9905ab172f7e1d0377aef615b343e266624040b0c89399c78f62b365d8` |
| `src/controle_ia/barreau5_familles/edition_cout_v1.py` | `99803e44b961fcb8c418198aa3ae34203047d05d2da34ad61eac7ffee606be9b` |
| `src/controle_ia/barreau5_familles/engagement_v1.py` | `f41743fb98ecf5111f867fc18cb900c8f80a52fbee02d65dab8850a2c699102b` |
| `src/controle_ia/barreau5_familles/formation_v1.py` | `08724ceecfd0dc26a70dba5e9878dd79fce44c30e90a92e3beb4730c0b2fd539` |
| `scripts/lancer_b5f_formation_v1.sh` | `41f5d1585da3e622a4277a5b9db21e49a6236bc6b321429745499d0d186fe9a4` |
| `scripts/amorce_b5f_formation_v1.sh` | `22521feeb6e73c518c31fe48609fd8469a676d7cc29951c08c9a4ff191f01686` |
| `tests/test_barreau5_familles_edition_cout_v1.py` | `c9b0d4460d8812feb78f779322276b31a7baee083da134ecd1d8f16c23af0b4f` |
| `tests/test_barreau5_familles_engagement_v1.py` | `bea2088a746d4e40b06675fbf82e891ebe21990ac409b1f4926b50857a51a737` |
| `tests/test_barreau5_familles_formation_v1.py` | `972c0e139cb10750b782da76bcdaf3b5378be39616c657a9a91ca5ee378f203e` |
| `tests/test_lancer_b5f_formation_v1.py` | `6c48e62e2e144adc8c45d4ecc969b7c9a9233947fe4a2ff6e5f710f0d6c61b14` |
| `tests/test_amorce_b5f_formation_v1.py` | `2ab091c7beabcbdf474d8d345777fdeede46a55a3ce66efb9c20a26423df79e0` |
| `tests/test_amorce_b5f_formation_entiere_v1.py` (neuf) | `90179594bd50a83a7df37b64a08c9bf32f1b0bf56441e976e972da1f335ef671` |

Ce sont les fichiers sur lesquels ont tourné la dernière passe (253 passés) et la passe sur l'arbre extrait (171 passés). Le contrôle par mutation a tourné sur ces mêmes fichiers, sauf `tests/test_barreau5_familles_engagement_v1.py` (version d'avant le resserrement de N10, `6066fcf0…`, pour les mutations autres que N10, M20b et N15b) ; la version finale ne fait qu'exiger les motifs de cinq artefacts.

Outils et sorties, hors du dépôt, dans `/tmp/claude-0/-home-user-controle-ia-travail/8282ab93-0983-5813-b791-a7a522157dcd/scratchpad/dev-corrections-b5f/` (bloc-notes de la session ; à verser par la mère si elle les garde) :

| fichier | sha256 |
|---|---|
| `outils/mutations-dev-corrections-v1.py` | `2f0e5ccb8c094dfe5febd4d1ae7bc8eca49c7632ff524308e42b7afa095069eb` |
| `outils/extraire-arbre-sans-commit-v1.py` | `6d4f1ee23b1333e32ec57510425e5cbc4cae3489a60b5f62493c56fda1a8aa25` |
| `outils/essai-blanc-tokeniseur-reel-v1.py` | `536641e7b599fb78d8f72c6ce717a3fa9ee58c7bea65e114a9de1514c0edfbd7` |
| `sorties/sortie-mutations-dev-corrections-v1.json` | `95422a58e97029bc4a5475be77a6ce715565190bda6e52d0a924fbf1d5b3c53a` |
| `sorties/journal-mutations-dev-corrections-v1.txt` | `c8d0585925a668d0e23ecd1681428622b3fc7e8d49397311dc55cc3ea310e696` |
| `sorties/sortie-mutations-amorce-entiere-seule-v1.json` | `b568c4c871b7493513187175c10c20c752335dc74808c2babc0fb04789612518` |
| `sorties/journal-mutations-amorce-entiere-seule-v1.txt` | `69be522a790407e6096a2b3401cd02a875feb8448020471b0d2a5bc6eec8de51` |
| `sorties/sortie-essai-blanc-tokeniseur-reel-v1.json` | `21105e562ecacaeb76b25841c5c3b6ae672084c8bacdf992226d64ef7e0a9d76` |
| `sorties/essais-arbre-extrait.txt` (171 passés, avant le resserrement de N10) | `6fb587fe95a2b73d382b03d78780c76379c3d93b9e1da07792fd0ee4bbf2e048` |
| `sorties/essais-arbre-extrait-final.txt` (171 passés, fichiers finaux) | `37663e51ed1bbd864d5d73bb67eeb4a68e835aab76770bd9e7440dcb4a204bd9` |

L'outil de mutations a reçu, après sa passe principale, M20b et N15b et l'option de rejouer contre la seule amorce entière ; son empreinte ci-dessus est celle de cette forme finale, qui contient toutes les mutations jouées.
