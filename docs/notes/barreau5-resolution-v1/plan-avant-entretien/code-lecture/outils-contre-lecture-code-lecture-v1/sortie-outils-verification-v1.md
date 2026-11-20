# Sorties des outils du contre-lecteur à la vérification des corrections du code de lecture — v1

Jouées le 20 novembre 2026 sur le code du commit `eda8c395` (`lecture_v1.py` : `d08591d1…`). Aucune donnée : mondes fabriqués, dépôts git jetables. Temporaires sous `/dev/shm/b5f-contre-lecture/`, copie de travail sous le bloc-notes ; effacés.

## Essais, sans mutation

Les six fichiers de la lecture : **233 passés, aucun échec** — lecture 95, sondes 18, relecture 24, blocs de l'amorce 50 (témoins de l'outil de mutations), lanceur et amorce entière à blanc 46 (un passage à part, 297 s).

## Mutations (`mutations-verification-v1.py`)

**Premier passage nul, non compté.** Le témoin de l'amorce échouait dans ma copie de travail : j'avais omis d'y copier `requirements-gpu.txt`, que lit un essai de l'amorce. Les 50 essais passent sur le dépôt. Outil corrigé, copie neuve.

**Second passage** : quatre témoins verts ; **14 jouées, 14 attrapées**.

| id | fichier | défaut réintroduit | essai qui l'attrape |
|---|---|---|---|
| C1 | lecture | probabilité rapportée prise sur la mauvaise somme | `test_probabilites_rapportees_exactes_sur_un_cas_ecrit_a_la_main` |
| C2 | lecture | issue E sans séparation apprise établie | `test_petits_ecarts_sans_separation_apprise_etablie_issue_n` |
| C3 | lecture | issue E sans valeur absolue | `test_grand_ecart_negatif_sans_contraire_issue_n` |
| C4 | lecture | épreuve non exigée avant les scores | `test_epreuve_inscrite_apres_les_scores_refus` |
| C5 | lecture | table non comparée à `OUVERTURE-B5F` | `test_ouverture_d_une_autre_table_que_l_engagement_refus` |
| C6 | lecture | E2b : rapport des poussées inversé | `test_monde_force_seule_issue_d_force_non_ecartee` |
| C7 | lecture | tâches de M1 et M3 en réunion | `test_manipulation_sur_les_seules_taches_communes` |
| C8 | sondes | la sonde d'un pli note l'autre pli | `test_sonde_d_un_pli_ne_note_que_les_taches_de_son_pli` (essai rapide) |
| N1 | lecture | correction M-3 : contenu d'un compagnon non vérifié | `test_compagnon_orphelin_ou_faux_dans_l_arbre_de_lecture_refus` |
| N2 | lecture | correction M-1 : descriptifs avec les notations sous NI | `test_non_interpretable_rien_n_est_lu_des_sondes` |
| N3 | relecture | métadonnées admises dans un fichier d'adaptateur | `test_entrees_reduites_aux_seuls_tenseurs` |
| N4 | relecture | noms opaques non contigus admis | `test_entrees_noms_opaques_contigus` |
| N5 | amorce | témoin final sans les activations gardées versées | `test_preuve_cas_sain_puis_temoin_final_seulement_si_tout_tient` |
| N6 | amorce | entrées admises hors d'un seul commit | `test_entrees_artefacts[en_deux-un seul commit]` |

## Sondages (`sondages-contre-lecture-v1.py`, rejoué tel quel)

| sondage | à la contre-lecture | sur le code corrigé |
|---|---|---|
| S1, sondes lues sous « non interprétable » | oui | **non** : ni séparation apprise, ni épreuve, ni comparaison, ni couches ; diagnostic « non lu » |
| S2, famille sans sur-saboteur dans M1 | oui (dix familles) | **non** : M1, M3 et E1 à neuf familles, somme admise 1 |
| S3, table sous un nom en `.sha256` | ouverture faite | **refus**, pour les deux noms (« n'est le compagnon d'aucun fichier inventorié ») |
| S4, garde du code au commit | juste | juste : trois cas sains acceptés, quatre artefacts refusés |
| S5, dénombrement et seuils | égaux | égaux |
| S6, borne de la phrase E | peut valoir un millionième | inchangé : attend l'addendum |
