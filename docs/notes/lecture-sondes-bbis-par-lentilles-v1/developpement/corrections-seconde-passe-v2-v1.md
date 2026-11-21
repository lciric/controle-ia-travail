# Corrections de la seconde passe après contre-lecture — table « correction demandée → ce qui est fait → essai » — v1

Développeur neuf des corrections de la seconde passe, 2026-11-21 (UTC). Mandat :
`mandats/mandat-developpeur-seconde-passe-lentilles-v2.md` (`a2132568ad8ce75b32665d2dc004d50914083b7470852506e5651a86cd10aa73`,
vérifié), avec le mandat v1 qu'il cite (`4a3cf535…`) et celui des deux passes (`0a9517ea…`). Contre-lecture corrigée :
`contre-lectures/contre-lecture-code-seconde-passe-v1.md` (`0c90e0f6…`, vérifiée), verdict « pas avant ». Texte de lecture v2 scellé :
`prereg/lecture-sondes-bbis-par-lentilles-v2.md` (`a2bbed7a…`, vérifié), lu aux seules lignes que les corrections touchent
(1462 à 1482, 1990 à 2012, 2068 à 2080, 2098 à 2116, 2212 à 2245), sans sa liste « Jamais ouverts ».

**Mémoire de travail** (à dire au départ, mandat v1) : le travail a tenu d'un seul tenant ; je n'ai pas relu le texte v2 en entier
(la conformité est faite, mandat v2) ni les modules que les corrections ne touchent pas (`statistiques_v4`, `lecture_entree_v1`,
`comparaisons_lentilles_v1`, `audits_v2`, `reproduction_v1` au-delà des noms employés, l'archive de `nos_lentilles_v1`).

## Ce qui est neuf (R12 : aucun fichier existant n'est réécrit)
| fichier | ce que c'est |
|---|---|
| `src/controle_ia/lentilles_sondes_bbis/lanceur_seconde_passe_v2.py` | le lanceur de la seconde passe v1, plus les corrections ; fabriqué par remplacements exacts (outil ci-dessous) ; 11 lignes de la v1 retirées, aucune ligne de calcul |
| `src/controle_ia/lentilles_sondes_bbis/nos_lentilles_v2.py` | complément de `nos_lentilles_v1` : une seule ligne « Lentille nommée : … » par pièce (N5) |
| `src/controle_ia/lentilles_sondes_bbis/phrases_v3.py` | complément de `phrases_v2` : verdict d'ensemble (N2, N2 bis), phrase de tête de la reproduction (N4), tête |
| `tests/lentilles_sondes_bbis_seconde_passe_jouets_v3.py` | jouets de la seconde passe sur le monde des jouets de la version 9 de la première passe (arbre par pages ; arbre du dépôt du modèle qui liste les petits fichiers posés) |
| `tests/test_lentilles_sondes_bbis_seconde_passe_lanceur_v2.py` | copie accordée des essais du lanceur v1 (34 essais) ; l'essai dépendant de l'ordre y est corrigé |
| `tests/test_lentilles_sondes_bbis_seconde_passe_corrections_v1.py` | essais des corrections (55 essais) |
| `developpement/outils/fabrique-lanceur-seconde-passe-v2-v1.py` | fabrique le lanceur v2, les jouets v3 et la copie des essais à partir des v1 ; rejouée par un essai, à l'octet près |
| `developpement/outils/essai-des-essais-corrections-seconde-passe-v1.py` et sa sortie | essai des essais des gardes neuves |
| `developpement/noeuds-et-precisions-seconde-passe-v2.md` | note neuve qui rectifie la ligne 21 de la v1 (N1) et pose les nœuds N-dev-11 à N-dev-15 |

Inchangés : `statistiques_v4` (le mandat le demande), `montage_v2`, `phrases_v2`, `nos_lentilles_v1`, `lanceur_seconde_passe_v1`, tous
les autres modules et tous les fichiers d'essais existants. `MODULES_DIFFERENTS = ("statistiques_v4", "lanceur_seconde_passe_v2")`.
Dans la table, « essais » renvoie à `tests/test_lentilles_sondes_bbis_seconde_passe_corrections_v1.py` sauf mention ; « l'ancien code »
est `lanceur_seconde_passe_v1`, `phrases_v2` ou `nos_lentilles_v1`, joué sur le même monde pour y montrer le défaut.

## Bloquantes

| correction demandée | ce qui est fait | essai sain | essai artefact |
|---|---|---|---|
| **B1** — `corpus_pagine_v1` exécuté par la seconde passe, absent de `MODULES` | `corpus_pagine_v1` dans `MODULES` (lignes 82 à 86) ; les cibles du corpus prises explicitement de `corpus_pagine_v1.cibles_corpus` (ligne 231), comme `lanceur_v8` ; le point de branchement `Reglages.cibles_corpus` retiré ; l'import paresseux de `montage_v2` n'est plus appelé | `test_b1_tout_module_du_paquet_que_le_lanceur_v2_execute_est_dans_sa_liste_…` (fermeture des imports du lanceur, imports paresseux compris, égale à `MODULES`) ; `test_b1_modules_de_la_fiche_du_code_…` ; `test_b1_le_lanceur_v2_prend_les_cibles_du_corpus_de_la_lecture_paginee_…` | le même essai de fermeture, sur le lanceur v1 : il trouve exactement `corpus_pagine_v1` hors de la liste |
| B1 — fiche du code sans l'empreinte du module, ou altérée | `exiger_fiche_code` inchangée : elle exige l'empreinte de chaque module de `MODULES` | `test_b1_fiche_du_code_sans_l_empreinte_d_un_module_neuf_ou_alteree_d_un_octet_rien_ne_part` (cas sain : fiche complète, et fiche aux seuls 27 modules) | même essai, pour chacun des cinq modules neufs (`corpus_pagine_v1`, `cache_tokeniseur_v2`, `nos_lentilles_v2`, `phrases_v3`, le lanceur v2) : empreinte absente, puis altérée d'un caractère : refus de `exiger_fiche_code` et du montage, sans dossier créé |
| B1 — le chemin réel (arbre paginé) n'était éprouvé par aucun essai de la seconde passe | les jouets v3 n'injectent plus de fonction ; le montage suit `corpus_pagine_v1` sur le réseau simulé | `test_b1_bout_en_bout_la_seconde_passe_suit_les_deux_pages_de_l_arbre_du_corpus` (montage et calcul entiers ; arbre d'un jeu de données servi en **deux pages** ; cinq pages lues sans clé, avant tout flux long) | `test_b1_artefact_l_ancien_lanceur_de_la_seconde_passe_sur_le_meme_arbre_en_deux_pages_s_arrete` (l'ancien code : « aucun fichier de données dans l'arbre ») ; `test_b1_artefact_transport_sans_lecture_de_page_arret_…` ; `test_b1_artefact_arbre_du_corpus_sans_fichier_sur_ses_deux_pages_…` |
| **B2** — cache du tokeniseur posé par `montage_v1.poser_cache_tokeniseur`, essayé hors ligne seulement : arrêt 401 du script du corpus | pose par `cache_tokeniseur_v2.poser_cache_tokeniseur` (lignes 239 à 242) ; essai en ligne et sans clé `essayer_tokeniseur_en_ligne` (ligne 247 ; fonction recopiée de `lanceur_v9`, déclaré, lignes 360 à 380) ; `cache_tokeniseur_v2.exiger_cache` (ligne 248) ; les deux champs neufs du rapport `cache_du_tokeniseur` et `essai_du_tokeniseur_en_ligne_sans_cle` ; deux gardes de plus dans la liste du rapport ; `cache_tokeniseur_v2` dans `MODULES` | `test_b2_bout_en_bout_cache_marque_deux_essais_du_tokeniseur_avant_tout_flux_et_deux_champs_neufs` ; `test_b2_les_deux_essais_du_tokeniseur_un_hors_ligne_puis_un_en_ligne_tous_deux_sans_cle` ; `test_b2_la_fonction_de_l_essai_en_ligne_est_celle_du_lanceur_v9_plus_la_relecture_a_l_echec` | `test_b2_artefact_un_fichier_a_marquer_existe_a_la_racine_arret_avant_tout_flux` ; `test_b2_artefact_arbre_du_depot_du_modele_sans_les_petits_fichiers_poses_arret` ; `test_b2_artefact_l_essai_en_ligne_reussit_mais_a_reecrit_la_branche_du_cache_la_relecture_arrete` |
| B2 — **reproduction du refus 401** par la seconde passe | essais par le **vrai chargement** (`AutoTokenizer.from_pretrained`, celui de la copie versée du catalogue du voisin : `test_b2_le_chargement_joue_par_ces_essais_est_celui_de_la_copie_versee_…`) dans un processus enfant en ligne et sans clé, contre une porte simulée locale (127.0.0.1) | `test_b2_sain_le_lanceur_v2_pose_un_cache_que_le_vrai_chargement_lit_en_ligne_et_sans_cle_sans_demander_un_fichier` (les deux essais du lanceur tiennent ; aucun fichier demandé à l'hôte ; jamais la clé) | `test_b2_artefact_l_ancien_lanceur_de_la_seconde_passe_pose_un_cache_que_le_chargement_en_ligne_refuse_par_401` (l'ancien code : `tokenizer.model` demandé, refus 401) ; `test_b2_artefact_le_refus_401_arrete_le_lanceur_v2_avant_tout_flux_quand_le_cache_est_pose_a_l_ancienne` |
| B2 — **en cas d'échec de l'essai en ligne, relire le cache pour nommer la cause** (correction non bloquante 1 de la contre-lecture du correctif du tokeniseur) | à l'échec, `essayer_tokeniseur_en_ligne` relit le cache par `exiger_cache` ; l'arrêt porte « cause relue dans le cache : « … » », ou dit le cache inchangé | `test_b2_artefact_essai_en_ligne_en_echec_arret_avant_tout_flux_et_le_cache_relu_est_dit_inchange` (cache intact : dit inchangé, message exact) | `test_b2_artefact_la_branche_du_depot_a_bouge_l_essai_en_ligne_echoue_et_l_arret_nomme_la_cause` (jouet) ; `test_b2_artefact_la_branche_du_depot_a_bouge_par_le_vrai_chargement_l_arret_du_lanceur_v2_nomme_la_cause` (vrai chargement, porte simulée qui désigne un autre commit) |
| B2 — les jouets listent les petits fichiers posés par l'arbre du dépôt du modèle | jouets v3 sur le monde des jouets de la version 9 | `test_b2_artefact_arbre_du_depot_du_modele_sans_les_petits_fichiers_poses_arret` (première moitié : ils y sont) | même essai (seconde moitié : arbre des seuls poids, arrêt par le témoin) |
| `lanceur_seconde_passe_v2` = v1 plus ces seuls changements | fabrique par remplacements exacts | `test_l_outil_de_fabrique_rejoue_rend_le_lanceur_v2_ses_jouets_et_ses_essais_a_l_octet_pres` ; `test_lignes_du_lanceur_v1_toutes_gardees_hors_onze_lignes` (les 11 lignes retirées, nommées ; 14 fonctions et classes de calcul et de canal d'arrêt égales à la source près) ; les 34 essais de `…seconde_passe_lanceur_v2.py` | — |

## Non bloquantes

| correction demandée | ce qui est fait, ou la raison de ne pas faire | essai sain | essai artefact |
|---|---|---|---|
| **N1** — note des nœuds v1, ligne 21, inexacte (des copies de `lenses.py` et `transport.py` sont versées) | **corrigée** par une note neuve : `noeuds-et-precisions-seconde-passe-v2.md`, « Rectification de la v1 » ; la v1 n'est pas réécrite. L'amélioration « possible, non exigée » (appeler la copie versée dans l'essai) n'est pas faite ; raison écrite dans la note | — | — |
| **N2** — `phrases_v2` lignes 264 à 268 : ligne d'ensemble de la seconde course non recopiée quand une seule lentille est lue au premier palier | **corrigée** : `phrases_v3.lignes_du_verdict_d_ensemble` la recopie après la phrase gelée, avant les réserves (nœud N-dev-11) | `test_n2_une_seule_lentille_au_premier_palier_…` (R seule, S seule ; aucun autre mot ne change) ; `test_n2_bout_en_bout_la_tete_des_tables_porte_la_ligne_de_la_seconde_course` ; `test_n2_deuxieme_palier_inchange_et_cas_d_une_lentille_a_chaque_palier` ; `test_n2_la_tete_de_phrases_v3_est_celle_de_phrases_v2_hors_…` | le même premier essai montre que l'ancien code n'écrivait rien de la seconde course |
| **N2 bis** — `phrases_v2` ligne 258 : ligne recopiée sans vérifier que la lecture est inscrite | **corrigée** : la ligne n'est recopiée que si le lanceur la donne (`_ligne_de_la_seconde_course` : ligne de registre inscrite, seconde course menée en entier, ligne portée par la fiche ; nœud N-dev-12) | `test_n2_bis_nos_deux_lentilles_au_premier_palier_…` (première moitié : lecture inscrite, texte égal à l'ancien à l'octet près) | même essai (seconde moitié : fiche qui porte la ligne, lecture non inscrite ; l'ancien code la recopie, le neuf non) ; `test_n2_bis_bout_en_bout_lecture_non_inscrite_la_ligne_de_la_fiche_n_est_pas_recopiee_par_le_lanceur_v2` |
| **N3** — lanceur ligne 1157 : « non calculable sur vingt » pour le recouvrement des moitiés | **laissée dans la phrase, avec une note** : aucun mot gelé ne change (le texte ne fixe pas ce cas ; retirer ou réécrire la phrase serait un écart au texte scellé) ; `rendre_phrases` ajoute à l'entrée une `note` qui le dit et donne le motif (nœud N-dev-15) | `test_n3_recouvrement_des_moities_non_calculable_…` (seconde moitié : moitiés calculables, aucune note) ; `test_n3_aucune_note_pour_un_libelle_dont_la_phrase_ne_cite_pas_les_moities` ; `test_n3_les_phrases_sans_ce_cas_sont_celles_du_lanceur_v1` | `test_n3_recouvrement_des_moities_non_calculable_…` (première moitié : la note est écrite, la phrase est celle de l'ancien code, qui n'avait pas de note) |
| **N4** — `phrases_v2` ligne 315 avec le lanceur lignes 928 à 936 : phrase de tête fausse « avant le nœud de la v1 » | **corrigée** selon l'option (a) du nœud N-dev-9 : sens sévère gardé (`_premiere_passe_en_vigueur` inchangée), phrase de tête remplacée par une note du code dans les deux cas où l'état a changé depuis le montage (`phrases_v3`, nœud N-dev-13) ; la phrase gelée reste écrite quand rien n'a changé | `test_n4_le_sens_severe_du_lanceur_est_garde_tel_quel` ; `test_n4_phrase_gelee_quand_la_passe_etait_lancee_et_non_achevee_au_montage_et_l_est_encore` ; `test_n4_reproduction_faite_ou_premiere_passe_remplacee_…` | `test_n4_passe_en_cours_au_montage_et_achevee_depuis_…` (l'ancien code écrit la phrase inexacte) ; `test_n4_passe_jamais_lancee_au_montage_et_lancee_depuis_…` ; `test_n4_bout_en_bout_passe_achevee_depuis_le_montage_tete_exacte_et_aucune_phrase_de_la_lentille_publique` |
| **N5** — `nos_lentilles_v1` ligne 343 : exiger une seule ligne « Lentille nommée » | **corrigée** : `nos_lentilles_v2.condition_de_lecture` ; plus d'une ligne de la forme dans la pièce : arrêt, forme mal comprise ; aucune ligne : « non lue », comme avant (nœud N-dev-14) | `test_n5_sain_une_seule_ligne_qui_nomme_…` (R, S, R et S : condition égale à celle de l'ancien code) ; `test_n5_une_piece_sans_ligne_de_la_forme_…` ; `test_n5_la_piece_n_est_jugee_que_si_la_condition_l_a_consultee_…` | `test_n5_artefact_une_citation_de_la_forme_ailleurs_dans_la_piece_arret_…` (l'ancien code ouvrait la lecture de notre S) ; `test_n5_le_lanceur_v2_s_arrete_sur_une_piece_a_deux_lignes_le_lanceur_v1_la_lisait` |

## Les deux nœuds posés à Lazar (défaut (a) à 48 heures, vers le 2026-11-23 18:15Z)
| nœud | ce que le code fait | lignes qui en dépendent |
|---|---|---|
| N-dev-7 — lentille non lue dont le dernier crochet ne se détermine pas | option (a) : le choix du code est gardé, rien n'a changé | `phrases_v2`, lignes 86, 139 à 147, 201 et 202 |
| N-dev-9 — moment où l'état de la première passe est lu | option (a) : sens sévère gardé, phrase de tête corrigée (N4) | `lanceur_seconde_passe_v2`, lignes 990 à 998 et 1040 ; `phrases_v3`, lignes 75 à 97 |

## Point 6 du mandat — l'essai dépendant de l'ordre
- Cause : `from . import corpus_pagine_v1` rend l'attribut du paquet s'il existe déjà, sans consulter la table des modules ; retirer
  la seule entrée de la table ne fait donc pas échouer l'import dès qu'un fichier d'essais chargé avant a importé le module.
  Éprouvé : `test_point_6_l_entree_de_la_table_des_modules_ne_suffit_pas_il_faut_retirer_aussi_l_attribut_du_paquet`.
- Dans la copie neuve (`…seconde_passe_lanceur_v2.py::test_cibles_du_corpus_jamais_celles_de_montage_v1_telles_quelles`), l'attribut
  du paquet est retiré aussi : l'essai passe quel que soit l'ordre (seul, et dans le paquet entier).
- L'ancien fichier `…seconde_passe_lanceur_v1.py` reste tel quel. Son essai du même nom **tombe dans le paquet entier** (les essais
  des lanceurs v8 et v9 et du correctif de la pagination, chargés avant lui, importent `corpus_pagine_v1`) et passe quand le fichier
  est joué seul. L'échec n'a aucun lien avec le code : il éprouve une garde de `montage_v2` que le lanceur v2 n'appelle plus, et que
  la copie neuve éprouve. Pour un paquet entier sans échec, deux voies, au choix de la session : jouer l'ancien fichier dans un
  processus à part, ou écarter ce seul essai (`--deselect`). Comptes des deux façons : voir `sortie-essais-seconde-passe-v2.txt`.

## Essais (comptes seulement)
Voir `sortie-essais-seconde-passe-v2.txt` (scellé) : fichiers neufs, paquet entier, essai des essais. La suite complète du dépôt
n'est pas lancée (plus de deux heures) ; seuls les essais `tests/test_lentilles_sondes_bbis_*.py` l'ont été.

## Ce qui n'est pas fait, dit en clair
- Aucune fiche du code, aucune ligne de registre (hors de mon mandat). La fiche neuve `CODE-LENTILLES-BBIS-V2` doit citer le commit
  neuf et les empreintes de `empreintes-code-seconde-passe-v2.txt` (forme : nœud N-dev-8, complété dans la note des nœuds v2).
- Rien n'a été lancé, loué ni dépensé ; aucun téléchargement de modèle, de lentille, d'ajustement ni de corpus ; aucune requête
  vers la plateforme de modèles ; aucune clé lue.
- Le banc à taille réelle n'est pas rejoué.
