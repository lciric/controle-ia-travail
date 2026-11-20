# Sortie du passage de mutations v4 du code de lecture du barreau 5

Jouée le 20 novembre 2026 par le développeur du code de lecture (Claude Opus 5.5), outil `mutations-code-lecture-v4.py` (même dossier), sur une copie de travail du dépôt sous le bloc-notes de la session (une seule), temporaires sous `/dev/shm` ; copie et temporaires effacés par leur chemin. Aucune donnée : modèle jouet et fichiers fabriqués. Objet : défaire une à une les règles de l'addendum 1 au texte (`prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-addendum-1.md`, `2afa2186…`) que le code applique : les couples A et B de la vérification (`fb1b7d04…`), et les règles du point 1 que le code faisait déjà. Les couples C et D (en-tête, commentaire) ne changent aucun calcul : ils ne se mutent pas.

Témoin sans mutation, vert : lecture (102 passés).

**10 jouées, 10 attrapées**, aucune manquée, aucune introuvable, aucune erreur de l'outil.

| id | règle de l'addendum | défaut réintroduit | premier essai en échec |
|---|---|---|---|
| M01 | point 2, règles 2 et 3 | chaque membre sur ses propres tâches à coût lisible (la lecture écartée) | `test_manipulation_sous_six_familles_motif_niveau_non_atteignable` |
| M02 | point 2, cas limite | motif de la famille sans tâche retenue non écrit | `test_addendum_point_2_famille_sans_tache_retenue_absente_de_m1_et_de_m3` |
| M03 | point 2, règle 5 | nombre de tâches retenues non écrit | `test_addendum_point_2_tache_sans_cout_lisible_chez_un_seul_membre_retiree_pour_toute_la_famille` |
| M04 | point 3 | borne de la phrase E au plus grand écart | `test_addendum_point_3_borne_de_la_phrase_e_moitie_de_la_separation_apprise` |
| M05 | point 1, règle 2 | niveau de D sans M1 ni M3 | `test_niveau_de_l_issue_porte_celui_de_m1[effets0-D]` |
| M06 | point 1, règle 2 | niveau de C sans M1 ni M3 | `test_niveau_de_l_issue_porte_celui_de_m1[effets1-C]` |
| M07 | point 1, règle 2 | niveau de S sans M1 ni M3 | `test_addendum_point_1_issue_s_au_niveau_de_m1_et_m3_sorties_faute_de_tache_retenue` |
| M08 | point 1, règle 1 | famille sans saboteur ôtée aussi de M3 | `test_niveau_de_l_issue_porte_celui_de_m1[effets0-D]` |
| M09 | point 1, règle 4 | motif de NI sans « niveau non atteignable » | `test_manipulation_sous_six_familles_motif_niveau_non_atteignable` |
| M10 | point 1, règle 3 | niveau absent du nom de l'issue | `test_v10_familles_absentes_de_e2a_et_e2b_motifs_ecrits_et_noeud_6` |

Tous les essais cités sont dans `tests/test_barreau5_familles_lecture_v1.py`. Les premiers essais en échec sont lus dans le bilan JSON (champ `premier_echec`), gardé dans le bloc-notes de la session (non versé : il ne porte que ces états et durées).
