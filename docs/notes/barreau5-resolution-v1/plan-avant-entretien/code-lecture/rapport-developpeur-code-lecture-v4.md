# Rapport du développeur du code de lecture du barreau 5 (plan « sabotage ou empreinte de l'adaptateur ») — v4

Écrit le 20 novembre 2026 par le développeur du code de lecture (Claude Opus 5.5), sous-agent de la session mère `session_01XJ6Mgr8BN6UanALsQatc5E`. Pièce d'instrument (classe B), dans la suite du rapport v3 (`b9c77d67…`, qui n'est pas modifié, R12). Même mandat (`fffe5bd7…`), même texte scellé (`bdff244f…`).

Ce rapport applique l'addendum 1 au texte, scellé par le mot de Lazar : `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-addendum-1.md`, sha256 `2afa2186c9f11e0a477cdf628348d2cad3bce90de5933597ff09a4a3048499e4`, commit `8bf6aabe8`. Je l'ai lu en entier. Ses deux choix :
- une famille sans tâche retenue est comptée absente ;
- la borne de la phrase « empreinte » vaut ½ Δ_app.

Les couples appliqués sont ceux que le contre-lecteur a donnés exacts dans `verification-corrections-code-lecture-v1.md` (`fb1b7d04…`), section 5.

Aucune donnée n'est employée : modèle jouet et fichiers fabriqués seulement. Aucun réseau, aucune dépense, aucun commit.

## En bref

- **Les quatre couples sont appliqués à la lettre** : A (les tâches retenues dans `manipulation`), B (la borne de la phrase E), C (l'en-tête du module, avec la docstring de `manipulation`) et D (le commentaire de `issue`). Seul `lecture_v1.py` change dans le code.
- **Les trois essais nommés par le contre-lecteur sont repris.** Ils retirent désormais les saboteurs de la table au lieu de rendre leurs coûts illisibles. Le motif attendu de l'un d'eux change.
- **Un essai est ajouté pour chaque règle de l'addendum que le code applique**, en citant le point.
- **Le plancher d'essais de l'amorce passe à 146**, soit 102 + 20 + 24.
- **Essais** : 244 passés, aucun échec. **Mutations v4** : 10 jouées, 10 attrapées.

## 1. Les quatre couples

- **A — addendum, point 2** (`manipulation`, l. 784 à 815). Pour chaque membre présent, le programme calcule la moyenne par tâche sur les tâches jouées par tous. Les tâches retenues sont celles où chaque membre présent a au moins un coût lisible. m_i est la moyenne, pour chaque membre, sur ces seules tâches ; un seul jeu de tâches sert à M1 et à M3. `details` porte `taches_communes`, `taches_retenues` et `motif`. Quand aucune tâche n'est retenue, le motif est « aucune tâche retenue : famille absente de M1 et de M3 », et la fonction `d`, inchangée, écarte la famille de M1 et de M3. C'est le choix « absente » de Lazar.
- **B — addendum, point 3** (`phrases`, l. 1220). « [borne] » vaut `SEUIL_EMPREINTE * sep['delta_app']`, soit ½ Δ_app, au format de [x] et de [Δ_app].
- **C — en-tête** (l. 65 à 72) et docstring de `manipulation`. L'en-tête cite l'addendum pour quatre règles : le niveau d'une issue (point 1, règles 1 et 2), l'issue NI quand M1 ou M3 a moins de six familles (règle 4), l'ordre du point 13 et m_i (point 2), et donne « [borne] » (point 3). Restent comme interprétations du développeur : σ_0 sans correction, les percentiles, et c = 1.
- **D — commentaire de `issue`** (l. 1045 à 1046). Il dit désormais : « l'issue est NI (addendum 1, point 1, règle 4) ».

Le niveau d'une issue (`_niveau_min` et `issue`, l. 1030 et 1056 à 1066) ne change pas : c'est déjà la règle du point 1, que les essais éprouvent désormais.

## 2. Table de traitement

| règle de l'addendum, ou essai à reprendre | fichier | lignes | essai qui l'attrape |
|---|---|---|---|
| point 2, règles 1 à 5 : tâche sans coût lisible chez un seul membre, retirée pour toute la famille ; chaque membre garde tous ses coûts lisibles dans une tâche retenue ; un seul jeu de tâches ; deux comptes écrits (couple A) | `lecture_v1.py` | 784 à 815 | `test_addendum_point_2_tache_sans_cout_lisible_chez_un_seul_membre_retiree_pour_toute_la_famille`, l. 1353 (M01, M03) |
| point 2, cas limite, choix « absente » : famille sans tâche retenue, absente de M1 et de M3, motif écrit ; ces épreuves comptent leurs familles présentes (neuf, seuil 1) ; E1 à E3 inchangées (couple A) | `lecture_v1.py` | 799 à 806 ; `d`, inchangée | `test_addendum_point_2_famille_sans_tache_retenue_absente_de_m1_et_de_m3`, l. 1369 (M02) |
| point 3 : « [borne] » = ½ Δ_app de la même phrase (couple B) | `lecture_v1.py` | 1220 | `test_addendum_point_3_borne_de_la_phrase_e_moitie_de_la_separation_apprise`, l. 1407 (M04) |
| point 1, règles 1 à 3, issue D ou C : M1 à sept familles (saboteurs absents de la table), M3 et E3 à dix ; issue à 95 % dans son nom et sa phrase ; une famille sans saboteur reste dans M3 | `lecture_v1.py` | 1056, 1066 (inchangées) ; `d` | `test_niveau_de_l_issue_porte_celui_de_m1`, repris et paramétré en D et en C, l. 940 (M05, M06, M08) |
| point 1, règles 1 à 3, issue S : M1 et M3 à sept familles (cas limite du point 2), E1 à E3 à dix ; S à 95 % ; « au plus » au niveau de E3 | `lecture_v1.py` | 1058 (inchangée) | `test_addendum_point_1_issue_s_au_niveau_de_m1_et_m3_sorties_faute_de_tache_retenue`, l. 1389 (M07) |
| point 1, règle 3 : le niveau dans le nom | `lecture_v1.py` | inchangées | les deux essais ci-dessus ; `test_v10_familles_absentes_de_e2a_et_e2b_motifs_ecrits_et_noeud_6` (M10) |
| point 1, règle 4 : M1 ou M3 sous six familles, E3 à six ou plus : issue NI, motif « niveau non atteignable » (couple D) | `lecture_v1.py` | 1044 à 1050 | `test_manipulation_sous_six_familles_motif_niveau_non_atteignable`, repris, l. 1249 : (a) M1 seule, saboteurs absents de la table dans cinq familles ; (b) coûts du saboteur illisibles dans cinq familles, motif attendu changé en « manipulation non établie (M1, niveau non atteignable : cinq familles ; M3, niveau non atteignable : cinq familles) » (M09, M01) |
| essai repris : partie « b » de `test_phrase_au_niveau_de_95_et_au_plus_au_niveau_de_e3` | tests | l. 1232 | saboteurs absents de la table, et non leurs coûts : S à 95 %, E3 à 99 %, « au plus 0,005 » |
| en-tête (couple C) | `lecture_v1.py` | 65 à 72 | — (aucun calcul) |

Chaque essai cite le point de l'addendum dans sa docstring. Ce sont les essais que l'addendum demande lui-même (« Essais du code, pour les trois points »).

## 3. Essais et mutations

Essais, sur l'état rendu ici, en un seul passage, temporaires sous `/dev/shm` :

| fichier d'essais | passés |
|---|---|
| `tests/test_barreau5_familles_lecture_v1.py` | 102 |
| `…_sondes_v1.py` | 20 |
| `…_relecture_v1.py` | 24 |
| `tests/test_lancer_b5f_lecture_v1.py` | 43 |
| `tests/test_amorce_b5f_lecture_v1.py` | 51 |
| `tests/test_amorce_b5f_lecture_entiere_v1.py` | 4 |
| **total** | **244, aucun échec**, en 489 s |

Plancher de l'amorce : `MIN_ESSAIS=146`, soit 102 + 20 + 24. Il est égal au compte collecté des trois fichiers. Syntaxe : Python 3.11.18, sans erreur.

Mutations : `outils-developpeur-code-lecture-v1/mutations-code-lecture-v4.py`, même procédé qu'en v3. Témoin vert. **10 jouées, 10 attrapées**, aucune manquée, aucune introuvable, aucune erreur de l'outil. Le détail est dans `outils-developpeur-code-lecture-v1/sortie-mutations-code-lecture-v4.md`. Les couples C et D ne changent aucun calcul et ne se mutent pas.

## 4. Ce qui menace le gel

1. `lecture_v1.py` change d'empreinte. Viennent ensuite, dans l'ordre, la ligne `CODE-LECTURE-B5F`, la seconde programmation et l'épreuve à vérité plantée. Pour l'épreuve, je reprends la recommandation de l'addendum à la mère, sans l'ajouter aux épreuves : la fabrique pourrait planter des tâches sans coût lisible chez un seul membre.
2. `MIN_ESSAIS=146` suit le compte des trois fichiers. Il se reporte au même commit à tout ajout d'essai.
3. Restent les menaces des rapports v2 et v3 : l'arbre neuf (un fichier de scores par jeton par série) pour l'épreuve ; la garde de l'arbre extrait à jouer tôt sur le dépôt réel ; la branche des entrées, d'un seul commit, sur le dépôt distant avant la commande de création.

## 5. Fichiers

| fichier | sha256 |
|---|---|
| `src/controle_ia/barreau5_familles/lecture_v1.py` | `d877d2dea0ddd4707324139aaa63e4bdae1f89a2aa23bea145adf4175a62c0df` |
| `src/controle_ia/barreau5_familles/sondes_v1.py` (inchangé) | `2fc5e2cf36046cf15b819221d44d5b74fe48a695a89ccee8933442068ffb9c64` |
| `src/controle_ia/barreau5_familles/relecture_v1.py` (inchangé) | `f6bd8c15af1130894ad98669c97b04e82a09eb700fa336deeb2e0e3e562756ac` |
| `scripts/amorce_b5f_lecture_v1.sh` (seul `MIN_ESSAIS` change) | `54a676f35bde811e8ebcfb0f643d510c2a1a79ca6a8554d61b7a39dd8e44453f` |
| `scripts/lancer_b5f_lecture_v1.sh` (inchangé) | `ae501c55754731cb539c7aa0c30d646a7c6df5f424c441b5cc3f033170aa2f1a` |
| `tests/test_barreau5_familles_lecture_v1.py` | `3e7bc25912bbc33359b19820c838047aaec2b96489384b28124817820d46d540` |
| `tests/test_barreau5_familles_sondes_v1.py` (inchangé) | `804ce471e87e638a04069895d953197d85bdfe4bdfbf8925356218c1e96dbd38` |
| `tests/test_barreau5_familles_relecture_v1.py` (inchangé) | `9ac38dc7d3b5ba090e775ce349a53531852d71b0d182edbad78e882c0f878cb2` |
| `tests/test_lancer_b5f_lecture_v1.py` (inchangé) | `5f02900cf8f59dc56257301ff169e50e0575c909b03aa71f061cc1623e85de28` |
| `tests/test_amorce_b5f_lecture_v1.py` (inchangé) | `5d3f030277683a627f4ea1f4904bf3f3523b550b6e4867cb66cf99045b8f9f8d` |
| `tests/test_amorce_b5f_lecture_entiere_v1.py` (inchangé) | `4425d57bf7bd9979041aab9cfd76123cbcbb555a53a64a3983309e410cd3ca07` |
| `…/outils-developpeur-code-lecture-v1/mutations-code-lecture-v4.py` (scellé) | `156a1d361e6ed7bfb74851995866f03a3608b5a2ae19e6f5fdfac1307e98006e` |
| `…/outils-developpeur-code-lecture-v1/sortie-mutations-code-lecture-v4.md` (scellé) | `530797302a2f66e26a0fa69511fbdbebc53ced91cef82671a3f2267f841d6f89` |

Temporaires : la copie de mutation et ses dossiers sont effacés par leur chemin. `/dev/shm/b5f-lecture-v4` est effacé à la fin.
