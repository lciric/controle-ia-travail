# Notes du module de l'addendum 2 de P3 (v1)

Rédacteur du module : sous-agent neuf. Il n'a écrit ni le texte (brouillons 1 et 2), ni la contre-lecture, ni le
traitement, ni le premier addendum, ni son module.

## Ce qui fait foi, et ce qui est rendu

- Texte appliqué à la lettre : brouillon 2,
  `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/addendum2-p3/P3-addendum2-audit-verdict-v1-brouillon2.md`,
  sha256 `641b36c2d8b77ca78c6f9bdd151cc3a3cc38a468e4f2a307e01e94354f651615` (revérifié en fin de travail). Un brouillon 3
  est apparu dans le même dossier pendant le travail ; il n'a été ni lu ni appliqué.
- Module : `audit_verdict_p3_v1.py`, sha256 `0b991450d107ee16b484a568d91f95ca232b5079d42ae17b6c52ec2bd23369cf`.
- Tests : `test_audit_verdict_p3_v1.py`, sha256 `ecbb897293b690b37e0f086c86ca575b97c0a6bfedcec69f56849023afa8bfd3` ;
  nombre de tests écrit en tête : 42.
- Suite lancée par chemin explicite, depuis la racine du dépôt :
  `PYTHONPATH=src python -B -m pytest -q -p no:cacheprovider <module>/test_audit_verdict_p3_v1.py` →
  `42 passed in 53.84s`. Le dépôt reste inchangé (`git status --porcelain` identique avant et après) ; aucun
  `__pycache__` laissé.
- Après le versement sous `docs/procedures/P3-addendum2-v1/`, revérifier les deux empreintes avant de les reporter en
  tête du texte (lignes « Module de l'addendum 2 (sha256) » et « Tests du module (sha256) »), avec `42` comme nombre de
  tests attendu.

## R1 : aucune grandeur de B1 ni de B2 calculée sur le réel

- Aucun fichier du run `20261019-230011-p3-reel` ni de la lecture `20261020-075740-p3-lecture` n'a été ouvert ni haché,
  ni par le rédacteur, ni par les tests, ni par la mesure de durée. Ni `prereg/P3-consignes-v1.md`, ni un texte d'action,
  ni une clé n'ont été lus.
- Tables synthétiques seulement. Les constantes du module qui nomment le run réel (bloc entre « début des constantes du
  run réel » et « fin des constantes du run réel ») sont réécrites dans la copie du module versée dans chaque dépôt jouet.
  Un seul test lit ces constantes, comme chaînes, pour les comparer à la table « Entrées » du texte.

## Section du texte → fonction qui l'applique

| section du texte | fonction(s) |
|---|---|
| En-tête : empreintes du module et des tests lues dans le texte | `EMPREINTE_MODULE_CITEE`, `EMPREINTE_TESTS_CITEE`, `exiger_garde_1` |
| En-tête : entrées [MR], [R], [SF], [E], [S], [J], [T], [L], [ML] ; [A] et [MA] non lus | `ENTREES` (bloc des constantes du run réel), `exiger_garde_2` |
| En-tête : code gelé réutilisé, sans modification | imports de `lecture`, `statistiques`, `sondes.evaluation`, `manifeste`, `prereg`, `scellement`, `validation_reelle.exiger_code_cite` ; aucune fonction du premier addendum |
| Métrique, Entrées : run source par `lecture.charger_source` | `exiger_garde_6` |
| Métrique, Entrées : colonnes de [S] lues | `_tables` (condition, tâche, coût, cinq formes ; noms des sondes et scores pour la garde 7) |
| Métrique, Entrées : clés de [L], entrée par entrée | `lire_la_lecture` (garde 9), `_cle`, `_booleen`, `_etat_entree` |
| M1, population et coût lu | `lecture.couts_par_tache` (gelé) sur toutes les actions ; `statistiques.cout_de_tache` (gelé) |
| M2, formes | `FORMES`, `_a_forme` |
| M3, restriction (NaN dans une copie, deux conditions) et comptes propres | `table_restreinte`, `couts_restreints`, `comptes_restriction` |
| M4, statistique de tâche, effet restreint, « non calculable » | `differences_par_tache`, `effet_restreint` (`statistiques.effet_cout_apparie` gelé) |
| M5, part portée par les formes (D, E0, part, libellés signés, mention « instable ») | `part_des_formes`, `classement_D`, `libelle_D` |
| M6, médiane par tâche et descriptifs | `mediane_par_tache` |
| M7, tâches sans forme | `effet_taches_sans_forme` |
| M8, écart de forme | `ecart_de_forme`, `ecarts_de_forme` |
| M9, table par tâche | `table_par_tache` |
| M10, puissance du nul (B3) | `quantiles_normaux`, `puissance_du_nul`, `analyse_b3` |
| Analyses B1 et B2 (même fonction, mêmes paramètres) | `analyse_contraste`, appelée par `analyser_addendum2` pour les trois contrastes |
| Règles communes : forme absente « sans objet », générateur non consommé | `analyse_contraste`, `ecarts_de_forme` |
| Règles communes : tâches triées, une matrice de tirage par clé | `_tirages_des_taches`, `_intervalle` |
| Règles communes : graines, 47 clés | `cles_addendum2`, `_rng`, `exiger_graines` (garde 12) |
| Règles communes : forme de la sortie, clés interdites | `_Controles`, `_calcul`, `_sans_cles_interdites`, `_propre`, `_cles` |
| Seuil : classements d'un intervalle et de D | `classement`, `classements`, `classement_D` |
| Seuil : réserves de B1 et table des cas de B1 | `controles_b1` |
| Seuil : réserves de B2 (témoin et mention, cibles P3-P1, P3-P4/<p>, T3/<p>) | `controles_b2` |
| Seuil : réserve de B3 | `controles_b3` |
| Seuil : réserves « non lue », union par (nom, cible), motifs joints | `_Controles.ajouter`, `synthese` |
| Plan, point 2 : commande | `_main` |
| Plan, point 3 : gardes 1 à 11 et 13 avant le manifeste ; garde 4 (fin) et garde 12 juste après ; gardes 14 et 15 pendant et après | `executer`, puis `analyser_addendum2` |
| Plan, point 4 : manifeste propre, sortie unique scellée et rattachée, arrêt écrit puis propagé | `executer` (`creer_manifeste` sans `autoriser_depot_sale`, `ecrire_resultat`) |
| Plan, point 5 : ordre des analyses | `analyser_addendum2` |
| Plan, point 6 : verrou mécanique, table fermée | `cibles_possibles`, `conclusions_etablies`, recoupement de `P3-P1.etablie` dans `lire_la_lecture` |
| Plan, point 7 : synthèse | `synthese`, `analyser_addendum2` |
| Plan, point 8 : nombre de contrôles à côté du nombre de réserves | `synthese` (`nombre_de_controles`, `nombre_de_reserves`) |
| Critères de lecture gelés : phrases au verdict | `LECTURES`, `LECTURE_NON_LUE`, `LECTURE_AUCUNE`, `LECTURE_AUDIT`, `LECTURE_ARRET`, `_lecture_de`, `synthese` |
| Critères : audit de symétrie (R4), points 1 à 3 | `audit_symetrie` |
| Liste d'arrêt, garde 1 | `exiger_garde_1` |
| garde 2 | `exiger_garde_2` |
| garde 3 | `exiger_garde_3`, `_est_lecture_decisive`, `_manifestes` |
| garde 4 | `exiger_garde_4`, `_git`, `_git_octets`, `_ancetre` ; dernier contrôle : `exiger_commit_du_manifeste` |
| garde 5 | `exiger_garde_5`, `_manifestes`, `_pourrait_concerner` |
| garde 6 | `exiger_garde_6` |
| garde 7 | `exiger_coherence`, `effet_ponctuel` |
| garde 8 | `exiger_issue_recalculee` |
| garde 9 | `lire_la_lecture`, `_cle` |
| garde 10 | `exiger_constantes_gelees` |
| garde 11 | `exiger_garde_11` ; paramètres au point d'entrée : `exiger_parametres_du_texte` (appelée par `_main`) |
| garde 12 | `exiger_graines` |
| garde 13 | `exiger_entrees_b3` |
| garde 14 | `exiger_verrou` |
| garde 15 | `part_des_formes` (part « échec », motif écrit ; D et ses réserves restent lus) |
| Plan, point 10, et liste fermée des tests | `test_audit_verdict_p3_v1.py` (table plus bas) |

## Lectures d'application (le texte se tait ; aucune ne change une règle)

1. Garde 3, « comme la garde 2 de [PA] » : l'unicité de la lecture décisive applique aussi le critère lexical aux
   manifestes illisibles (celui de la garde 5, repris de [PA], garde 16).
2. Garde 4, « dont le fichier scellé a l'empreinte vérifiée » : au commit S2, le compagnon nomme l'empreinte vérifiée,
   et le texte lui-même a cette empreinte. « S2 descendant du commit qui consigne N-025 » est lu au sens strict
   (S2 différent de ce commit).
3. Garde 7, entrée de [L] « non calculable » : le recalcul doit l'être aussi (moins de deux tâches), sinon arrêt ;
   entrée « en échec » : non comparée, écrite telle quelle dans `coherence_avec_la_lecture`.
4. Garde 9 : `principales` de [L] doit égaler celles de [SF] (c'est ce qui désigne `<p>`). Une entrée P3-P1 « non
   calculable » sans `etablie` n'arrête pas ; elle n'est pas établie.
5. Garde 13 : une entrée P3-P3/<p> en échec n'est pas contrôlée (garde 9 : « non lu », sans arrêt).
6. Garde 11 : l'appel de `executer` contrôle le nom du run, le texte passé et le chemin du module ; les paramètres de
   tirage sont contrôlés par `_main`, au point d'entrée, avant toute lecture.
7. M5 : si E0 vaut exactement 0, la part ponctuelle est « non calculable » (motif « E0 = 0 ») ; « échec » reste réservé
   aux tirages dégénérés (garde 15). Dans le cas « échec », aucune valeur de la part n'est rapportée.
8. Table des cas de B1 : `ampleur_non_resolue` est « non lu » si E_sf ou D ne sont pas lus, même si la borne basse
   décisive est au plus log10 3 (sens prudent ; une seule réserve « non lue » par cible, motifs joints).
9. Audit de symétrie, point 2 : un intervalle décisif non lu (entrée non calculable ou en échec) rend le déclencheur
   « non calculé » ; sinon « sans objet » si un intervalle décisif est conforme ; sinon « non calculé » si un E_sf ne
   l'est pas. Point 3 : « non calculé » aussi si la part des formes n'est pas calculée (moins de deux tâches dans T_sf).
10. Recommandation au verdict : une liste d'entrées {conclusion, réserve, lecture}, pour les seules conclusions établies
    visées par au moins un contrôle lu ; « contrôles de l'addendum 2 passés » quand aucune réserve ne les vise ; une
    entrée de plus si l'audit de symétrie est déclenché. Les phrases reprennent la table des critères, nombres remplis
    (A_80(p), A_80_écrit_max, D et son intervalle, borne basse de E_sf), virgule décimale.
11. `nombre_de_controles` : écrits, lus (tout contrôle non « sans objet »), dont « non lus », sans objet.
12. Libellé de D ponctuel nul (cas « sans aucune forme ») : « D = 0 : retirer les actions à forme ne change pas la
    différence » (descriptif ; M5 ne nomme que D > 0 et D < 0).

## Écarts au texte

Aucun.

Tests en plus de la liste fermée (ils éprouvent des règles écrites du texte, sans en ajouter) : table des cas de B1,
règle et cibles de B2, écarts de forme M8, classements et libellés du seuil, recommandation au verdict, déterminisme et
entrées intactes, constantes du run réel égales au texte, ligne de commande de bout en bout (dans le processus et dans un
processus séparé), nombre de tests écrit en tête. Le premier addendum faisait de même.

## Liste fermée des tests (« Liste d'arrêt », Tests) → test

| élément | test(s) |
|---|---|
| garde 1 : entropie, texte non scellé, empreintes du module et des tests, arbre gelé | `test_garde_1_entropie_texte_scelle_empreintes_et_arbre_gele` |
| garde 2 : entrées nommées et empreintes | `test_garde_2_entrees_nommees_et_empreintes` |
| garde 3 : lecture décisive, rattachement et unicité | `test_garde_3_lecture_decisive_rattachement_et_unicite` |
| garde 4 : histoire coupée, S2 non ancêtre de la tête, S2 antérieur à N-025, commit du manifeste ≠ tête vérifiée, dépôt jouet | `test_garde_4_anteriorite_sur_un_depot_jouet`, `test_garde_4_commit_du_manifeste_different_de_la_tete` |
| garde 5 : second passage et manifeste illisible | `test_garde_5_second_passage_et_manifeste_illisible` |
| garde 6 : run source non vérifiable | `test_garde_6_run_source_non_verifiable` |
| garde 7 : coût altéré d'une action, compte de forme altéré | `test_garde_7_coherence_cout_et_forme_alteres` |
| garde 8 : issue et états | `test_garde_8_issue_et_etats` |
| garde 9 : clé absente, entrée en échec, lecture du code gelé sans arrêt (P3-P2 et mention sans `etablie`) | `test_garde_9_cle_absente_et_entree_en_echec`, `test_garde_9_lecture_du_code_gele_passe_sans_arret` |
| garde 10 : constantes gelées | `test_garde_10_constantes_gelees` |
| garde 11 : forme de la commande et paramètres | `test_garde_11_forme_de_la_commande`, `test_garde_11_parametres_au_point_d_entree` |
| garde 12 : graines échangées ou d'une autre entropie | `test_garde_12_graines` |
| garde 13 : entrées de B3 | `test_garde_13_entrees_de_B3` |
| garde 14 : verrou | `test_garde_14_verrou` |
| garde 15 : dégénérescences | `test_garde_15_degenerescences_de_la_part` |
| aucune clé interdite | `test_aucune_cle_interdite_dans_la_sortie` |
| textes non UTF-8 à l'empreinte juste | `test_textes_non_utf8_a_l_empreinte_juste_ne_changent_pas_la_sortie` |
| tables par jeton aléatoires | `test_tables_par_jeton_aleatoires_sortie_identique` |
| sans aucune forme : E_sf = effet décisif, D = 0 | `test_sans_aucune_forme_E_sf_egal_effet_decisif_et_D_nul` |
| restriction recomptée | `test_restriction_retire_exactement_les_actions_a_forme` |
| honnête qui lit 100 fois trop bas ses actions à forme | `test_honnete_lit_100_fois_trop_bas_ses_actions_a_forme` |
| B1 et B2 par la même fonction | `test_B1_et_B2_passent_par_la_meme_fonction` |
| deux déclencheurs de l'audit, cas construit et cas sain | `test_audit_explication_trop_propre_construit_et_sain`, `test_audit_part_hors_bornes_construit_et_sain` |
| B3 à la main ; z et z80 à 1e-12 | `test_B3_calcul_a_la_main_et_quantiles_normaux` |
| « organisme non établi » | `test_organisme_non_etabli_B1_B2_sans_objet_aucune_reserve` |
| ligne « critères 2 et 3 » | `test_ligne_criteres_2_et_3_nul_non_etabli_B3_sans_objet` |
| clés de graines distinctes | `test_cles_de_graines_liste_fermee_et_distinctes` |
| médiane et moyennes sur des tâches seulement | `test_mediane_et_moyennes_sur_les_taches_seulement` |

## Durée mesurée

Mesure faite sur des données synthétiques de taille réelle : 60 tâches, 4 conditions, 10 pas, 600 actions par condition,
430 sondes (2 principales, 214 sondes de plancher chacune), formes et coûts plantés. Elle passe par un dépôt git jouet
(code copié, texte scellé, run source et lecture décisive synthétiques) créé dans le dossier du module puis supprimé.
Machine : x86_64, 4 cœurs, numpy 2.4.6, Python 3.11.

- Ligne de commande réelle, dans un processus séparé, avec les paramètres du texte (10 000 tirages) : **5,4 s**
  (deux mesures : 5,40 s et 5,43 s). Le passage a réussi : sortie scellée, 13 contrôles écrits, 9 lus. Mémoire maximale
  ≈ 680 Mo.
- Dont les seuls imports du code gelé : 4,6 s environ.
- Fonction pure seule (garde 12, gardes 7 à 10 et 13, B1, B2, écarts, B3, audit, verrou) : 0,4 à 0,5 s, dont la garde 7
  (430 aires) 0,18 s.

Phrase proposée pour le marqueur `<<DUREE_MESUREE>>` : « environ 5,4 s pour la ligne de commande complète (processus
séparé, dépôt jouet à taille réelle : 60 tâches, 4 conditions, 10 pas, 600 actions par condition, 430 sondes ;
10 000 tirages), dont environ 4,6 s d'imports et 0,5 s pour la fonction pure ; mémoire maximale ≈ 680 Mo ».
