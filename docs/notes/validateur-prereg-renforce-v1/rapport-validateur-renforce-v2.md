# Validateur renforcé des préenregistrements — rapport v2

- **Pièce** : instrument (classe B), version 2, écrite par Opus 5.5 le 28 novembre 2026, à faire vérifier par le même contre-lecteur que la v1. Non commise par l'auteur.
- **Fichiers neufs** : `src/controle_ia/prereg_renforce_v2.py`, `tests/test_prereg_renforce_v2.py` (158 essais). La v1 (`src/controle_ia/prereg_renforce_v1.py`, `tests/test_prereg_renforce_v1.py`, `docs/notes/validateur-prereg-renforce-v1/rapport-validateur-renforce-v1.md`) reste telle quelle (R12).
- **Pourquoi** : la contre-lecture de classe B de la v1 (Claude Sonnet 5.5, agent neuf ; rapport dans le bloc-notes de la session, `contre-lecture-classe-b-validateur-renforce-v1.md`, `c5c775b1caf9581d5f2b025d1e25977d48facecba89ba428cda907adcd8f84b4`) a conclu « à corriger », avec 4 remarques majeures et 9 mineures.
- **Emploi** : `PYTHONPATH=src python -m controle_ia.prereg_renforce_v2 [--racine R] [--mots-min N] [--mots-min-contre-lecture N] [--permettre-hors-racine] FICHIER…` ; code de sortie 1 si un fichier a un problème ou est refusé. **Ordre d'emploi** : d'abord sceller (compagnon) ou suivre par git le rapport de contre-lecture et tout fichier cité, puis valider ; sinon (a) refuse leurs empreintes.

## 1. Remarque, correction, essai qui la prouve

| remarque de la contre-lecture | correction dans la v2 | essais qui la prouvent (`tests/test_prereg_renforce_v2.py`) |
|---|---|---|
| **1 (majeure)** Une empreinte d'un autre fichier passe à côté d'un chemin | `paires` : une empreinte s'apparie au dernier chemin qui la précède sur la ligne, si l'intervalle ne contient que des séparateurs, au plus un accent grave et, au plus, « empreinte » ou « sha256 » ; ligne à k ≥ 2 chemins tous avant les empreintes : appariement par rang (k et k), aucun si les nombres diffèrent. Vérification dans l'ordre : compagnon du chemin cité, empreinte sur disque, historique git (`PLAFOND_HISTORIQUE` = 50 révisions, plus la révision citée après « commit ») en avertissement. Sinon problème, avec le fichier que l'empreinte désigne. Non appariée : contrôle de la v1, plus un avertissement qui compte les empreintes non appariées | `test_appariement_empreinte_d_un_autre_fichier`, `…_rapport_croise_dans_la_contre_lecture`, `…_par_disque_sans_compagnon`, `…_fichier_garde_par_compagnon_sans_ouverture`, `…_fichier_garde_sans_compagnon`, `…_ligne_de_table_par_rang`, `…_table_nombres_differents_rien_n_est_apparie`, `…_strict_libelle_intercale`, `…_version_ancienne_dans_l_historique`, `…_historique_plafonne_et_commit_cite`, `…_chemin_absent` |
| **2 (majeure)** Garde contournée par `..` et par les liens symboliques | `est_garde` normalise (`posixpath.normpath`), sans tenir compte de la casse, avec des motifs testés à toute profondeur. `Index.refus` refuse les liens symboliques, ce qui sort de la racine passée ou du dépôt (chemin réel), et tout chemin gardé, lexical ou réel. Il est appelé avant chaque hachage, chaque comptage de lignes et chaque lecture de compagnon (compagnon lien : non lu). Un refus donne un avertissement, jamais une ouverture | `test_est_garde` (27 cas, dont `docs/../…/iib/…`, `src//controle_ia//iib/…`, majuscules, dossier `P3-consignes-v1-…/`), `test_garde_lien_symbolique_suivi_non_hache`, `…_lien_symbolique_cite_avec_lignes`, `…_lien_symbolique_apparie`, `…_compagnon_lien_symbolique_non_lu`, `…_point_point_cite_vers_un_fichier_garde`, `…_dossier_parent_lien_vers_l_exterieur`, `…_dossier_parent_lien_vers_un_dossier_garde`, `…_chemin_garde_qui_mene_ailleurs`, `test_c_point_point_qui_sort_de_la_racine` ; toutes avec un crochet d'audit (`sys.addaudithook`) qui enregistre chaque ouverture en lecture |
| **3 (majeure)** Garde ancrée à la racine passée | Motifs sans ancrage de tête (`controle_ia/iib`, `ii-b-saboteur-budget-*`, `g0-criteres-2-3-v1/consignes-privees-*`, `p3-consignes-v1*`). Racine du dépôt = `git rev-parse --show-toplevel`, sinon le premier parent qui contient `CLAUDE.md`, sinon la racine passée ; un fichier hors de cette racine n'est jamais ouvert. Préenregistrement gardé (chemin absolu, réel ou relatif au dépôt) ou lien : `GardeArret` ; hors de la racine : `GardeArret`, sauf `--permettre-hors-racine` (la garde s'applique alors quand même) | `test_garde_racine_sous_dossier`, `test_garde_preenregistrement_garde_ou_lien_refuse`, `test_garde_preenregistrement_hors_racine`, `test_garde_relatif_depuis_un_sous_dossier`, `test_racine_du_depot`, `test_garde_aucun_fichier_garde_ouvert_par_l_index` |
| **4 (majeure)** Empreintes de 63 ou 65 caractères, ou en majuscules, ignorées | Toute suite de 32 caractères hexadécimaux ou plus (au moins une lettre, non collée à une lettre ou à un chiffre, non suivie d'une ellipse) est classée. 64 minuscules : (a) ; 64 avec majuscules : problème ; 40 : avertissement si ce n'est pas un commit du dépôt ; 32 ou 128 : avertissement ; toute autre longueur : problème | `test_a_longueur_invalide` (33, 63, 65, 72), `test_a_empreinte_de_65_caracteres_issue_d_une_vraie`, `test_a_majuscules` (vraie et inventée `AB`×32), `test_a_quarante_caracteres`, `test_a_longueurs_md5_sha512`, `test_a_suite_collee_a_une_lettre_ignoree` (63, 64, 65) |
| 5 Faux positifs de (c) | `::…` et `#…` coupés ; `:Ln`, `:Ln-Lm`, `:n–m`, `:n,m` acceptés, chaque ligne vérifiée ; `:nom` après une extension : le fichier seul ; gabarits `AAAA`, `JJ`, `HHMM`, `XXX`, `NNN` ignorés ; contenu entier essayé avant le premier mot (noms avec espaces) | `test_c_formes_legitimes` (10 formes), `test_c_lignes_hors_du_fichier` (7 formes), `test_c_motifs_ignores` (11 motifs), `test_c_nom_avec_espaces`, `test_c_commande_entre_accents_graves` |
| 6 (d) refuse une contre-lecture saine et brève | Seuil distinct pour « Contre-lecture » (`mots_min_contre_lecture`, défaut 12) ; ailleurs, au moins `mots_min // 2` mots distincts (trente mots creux ne passent plus) | `test_d_contre_lecture_courte_et_saine`, `test_d_section_repetitive`, `test_d_ponctuation_ne_compte_pas`, `test_d_seuil_parametre`, `test_mutation_q4_sections_reduites_a_un_mot` |
| 7 (b) : dates, préfixes nus, autres ellipses, commits | Dates de 8 à 14 chiffres ignorées ; ellipses `...`, `..`, `‥`, `⋯` ; préfixe nu entre accents graves (8 à 31 caractères, un chiffre et une lettre) ; un préfixe qui n'est le début d'aucune empreinte connue est accepté s'il désigne un commit du dépôt (`git cat-file -e`) | `test_b_formes_d_ellipse`, `test_b_prefixe_nu_entre_accents_graves`, `test_b_prefixe_de_commit_accepte`, `test_b_ignores_date_trop_court_sans_chiffre_colle` |
| 8 Pas d'issue pour une empreinte hors dépôt | Marque « hors dépôt » ou « hors du dépôt » sur la ligne : une empreinte non appariée et inconnue devient un avertissement visible | `test_non_appariee_marque_hors_depot` |
| 9 Robustesse | Lecture en octets : un fichier non UTF-8 ou absent donne un problème « (lecture) », sans planter, et la ligne de commande passe au fichier suivant ; octet d'ordre (BOM) signalé ; git indisponible : avertissement ; fichier suivi illisible : compté en avertissement ; `_nb_lignes` lit en flux | `test_ligne_de_commande`, `test_lecture_latin1_absent_bom`, `test_a_hors_depot_git_avertissement`, `test_a_fichier_suivi_illisible`, `test_nb_lignes_en_flux` |
| 10 `resoudre` cache le fichier courant | `connue(h)` (compagnons, puis fichiers suivis) pour accepter ; `chemins(h)` (réunion des deux) pour dire quel fichier une empreinte désigne | `test_appariement_empreinte_d_un_autre_fichier` (message « elle désigne … ») |
| 11 Limites sémantiques de (a) et (e) | Compagnon périmé : avertissement ; empreinte du fichier vide : avertissement ; une entrée exige une puce, un titre ou du gras (une phrase du corps n'ouvre plus d'entrée) ; noms de modèle avec leur majuscule (« une fable » ne compte plus) ou identifiant `claude-…`, `gemini-…`, `gpt-…` ; un nom précédé de « écrit par », « rédigé par » ou « auteur » ne compte pas | `test_appariement_compagnon_perime`, `test_empreinte_du_fichier_vide`, `test_e_phrase_du_corps_n_ouvre_pas_d_entree`, `test_e_faux_modeles` (6 cas), `test_e_auteur_et_relecteur_nommes`, `test_e_modele_dans_un_identifiant` |
| 12 Mutants survivants de la v1 | Essais ajoutés pour chaque survivant : M01/M54 (longueur, collé à une lettre), M02 (compagnon d'une ligne au nom ancien), M03 (`hash *nom`), M04 (compagnons des fichiers gardés lus), M05/M06/M09 (dossier `P3-consignes-v1-…/`), M08 (compagnon suivi non compté comme fichier), M10 (`.sha256` sous `.git` ignoré), M15 à M18 (`[`, `$`, `?`, `{`), M22 (fichier sans saut final), M23 (ponctuation), M28/M29 (`Operator`, `GPTq`), M41 (préfixe collé), M43/M44 (`runs/`, `livrables/`), M50 (`gardes_sautes`), M51 (dédoublonnage de (c)) | `test_a_suite_collee_a_une_lettre_ignoree`, `test_a_compagnon_d_une_ligne_au_nom_ancien`, `test_a_liste_sha256sum_et_marqueur_binaire`, `test_garde_aucun_fichier_garde_ouvert_par_l_index`, `test_est_garde`, `test_a_compagnon_suivi_n_est_pas_un_fichier_designe`, `test_a_compagnon_sous_git_ignore`, `test_c_motifs_ignores`, `test_c_fichier_sans_saut_final`, `test_d_ponctuation_ne_compte_pas`, `test_e_faux_modeles`, `test_b_ignores_date_trop_court_sans_chiffre_colle`, `test_c_toutes_les_racines`, `test_c_dedoublonnage` |
| 13 Rapport v1 : exemple faux | Corrigé ici : `3b2e3ee5…` **est** l'empreinte du `src/controle_ia/prereg.py` courant (la contre-lecture a raison). La v2 apparie cette empreinte à ce chemin et la vérifie sur disque ; la limite 1 de la v1 est prouvée par l'essai `test_appariement_empreinte_d_un_autre_fichier`, pas par un cas du dépôt | — |

**Épreuve des essais par mutants (v2).** 57 mutants du module (22 sur la garde, 12 sur l'appariement, 23 sur les autres contrôles), joués contre `tests/test_prereg_renforce_v2.py` sur une copie du module hors du dépôt : **57 tués**, aucun survivant ; le mutant d'identité passe. Script : `mut2/run.py` dans le bloc-notes de la session, non versé. Les trois mutants de garde qui survivaient d'abord (refus « hors de la racine », garde du chemin réel, garde lexicale) sont tués par les trois essais à dossier parent lien.

## 2. Remarques non traitées, ou traitées en partie

- 7, « exiger une lettre à partir de 12 caractères » : non retenu ; la règle des dates suffit pour les faux positifs mesurés, et elle n'écarte pas les préfixes entièrement chiffrés plus longs, qui restent plausibles.
- 8, marques « externe » et « machine : » : non retenues, ce sont des mots trop courants dans le dépôt ; seule « hors dépôt » ou « hors du dépôt » est lue.
- 9, octet d'ordre : il est signalé, mais pas retiré avant le contrôle de structure. `prereg.problemes` lit le fichier lui-même, et la consigne interdit de modifier `prereg.py`.
- 9, archives `.tar` et `.zip` suivies : toujours hachées comme des octets, jamais décompressées. Faut-il les sauter parce qu'elles peuvent contenir des fichiers gardés ? C'est une question de politique, à trancher par la mère.
- 11, forme imposée « Relecteur : <modèle> » : non retenue, elle refuserait toutes les pièces actuelles. L'exclusion des tournures d'auteur la remplace en partie : un nom de modèle cité dans une autre phrase passe encore.
- 11, ordre d'emploi (sceller avant de valider) : documenté, en tête de ce rapport et dans la docstring.

## 3. Relevé informatif (aucun fichier relevé n'est modifié)

### 3.1 Les deux brouillons du 28 novembre

| brouillon | v1 | v2 |
|---|---|---|
| `brouillons/prereg-v4-c-furtif-g1/G0-critere-3-additif-c-furtif-v1-brouillon-gemini-1.md` (`94913179…`) | 12 problèmes | 12 problèmes (les mêmes : 10 empreintes sans fichier, 2 contre-lectures sans modèle) ; 2 avertissements : un identifiant de 40 caractères qui n'est pas un commit du dépôt (`0e9e39f2…`, ligne 17), 22 empreintes non appariées |
| `brouillons/prereg-v4-c-furtif-g1/G1-architecture-h1-h2-v1-brouillon-gemini-1.md` (`887795c4…`) | 9 problèmes | **10 problèmes** : les 9 de la v1, plus une empreinte de **65 caractères** à la ligne 14 (celle donnée à `taches-evaluation.json`, `76cdeace…` suivie d'un caractère de trop), que la v1 ignorait ; 2 avertissements (le même identifiant de 40 caractères, 21 empreintes non appariées) |

Les empreintes appariées des deux brouillons (16 pour G0, 8 pour G1) sont toutes vérifiées contre leur chemin. Leurs fautes sont donc des empreintes inventées ou mal recopiées, pas des empreintes d'un autre fichier. Sur les 13 mutations du lecteur B, la v2 en voit 7 sur chaque brouillon, comme la v1 (p5, p6, p7, q1, q2, q3, q4). Elle voit en plus, pour p5 et q3, l'empreinte appariée au chemin disparu. Durée : environ 11 secondes pour les deux.

### 3.2 Préenregistrements scellés de `prereg/`

Même champ que la v1 : 183 fichiers `prereg/*.md` scellés ; `prereg/P3-consignes-v1.md`, gardé, n'est pas ouvert.

| contrôle | 183 scellés, v1 → v2 : fichiers (problèmes) | 66 conformes au validateur de base, v1 → v2 : fichiers (problèmes) |
|---|---|---|
| (a) | 135 (2 458) → 132 (2 549) | 55 (1 181) → 53 (1 273) |
| (b) | 93 (641) → 111 (843) | 35 (326) → 42 (452) |
| (c) | 115 (1 831) → 115 (1 831) | 39 (929) → 39 (929) |
| (d) | 19 (26) → 14 (20) | 0 → 0 |
| (e) | 102 (263) → 103 (265) | 34 (120) → 35 (122) |
| un contrôle renforcé au moins | 174 → 178 | 65 → 66 |

Les problèmes de (a) se répartissent ainsi :
- 1 239 empreintes non appariées sans fichier (128 pièces) ;
- 1 286 empreintes appariées à un chemin absent (43 pièces) ; ce sont les mêmes lieux que (c), vus du côté de l'empreinte ;
- 24 empreintes appariées qui ne sont celles ni du fichier, ni de ses 50 dernières versions (14 pièces). Ce sont surtout des registres vivants à l'historique très long : `registres/decisions.md`, `go.md`, `depenses.md`, `arrets.md`, dans `prereg/P3-bis-addendum-2-telechargement-controle-v1.md` et `prereg/P3-bis-addendum-3-relance-credit-v1.md`. Leurs versions sont plus anciennes que le plafond.

Avertissements :
- 673 identifiants de 40 caractères absents des commits. Le clone de travail est superficiel (`git rev-parse --is-shallow-repository` : `true`), et les commits d'autres dépôts entrent dans le compte ;
- des versions anciennes retrouvées dans l'historique ;
- 8 empreintes du fichier vide ;
- 7 empreintes déclarées hors dépôt.

`prereg/diagnostics-prealables-sondes-v1.md`, seule pièce que la v1 acceptait entièrement, échoue maintenant à (e). Sa contre-lecture ne nomme aucun modèle : la v1 la croyait conforme à cause du mot « fable » dans un nom de dossier (`conception-sondes-boite-blanche-fable-v1`).

Durée du relevé : 2 min 49 s pour les 183 pièces, surtout pour les recherches dans l'historique git ; une pièce neuve prend quelques secondes.

## 4. Limites connues

1. L'appariement ne lit que les formes `chemin` puis `empreinte` sur une même ligne. Une empreinte citée avant son chemin, ou sur la ligne suivante, reste non appariée (avertissement compté), et seul le contrôle d'existence de la v1 s'applique.
2. Historique plafonné à 50 révisions par chemin. Les registres vivants plus anciens sont refusés, sauf si la ligne cite le commit (« commit `X` »).
3. Clone superficiel : des commits réels du dépôt distant peuvent manquer. Les avertissements à 40 caractères et les préfixes de commit en dépendent.
4. (a) appariée à un chemin absent double le message de (c), à dessein (l'un parle du chemin, l'autre de l'empreinte).
5. (e) ne sait toujours pas qui est le relecteur : un nom de modèle cité hors d'une tournure d'auteur passe.
6. Le hachage suit le contenu sur disque, pas celui du dernier commit.
7. Hors champ, comme en v1 : neuvième titre, niveau des sous-sections, mots imposés, seuil contradictoire.

## 5. Rejouer

```
cd /home/user/controle-ia-travail
PYTHONPATH=src python -m pytest -q tests/test_prereg_renforce_v2.py tests/test_prereg*.py      # 224 réussis
PYTHONPATH=src python -m controle_ia.prereg_renforce_v2 brouillons/prereg-v4-c-furtif-g1/*gemini-1.md
```
