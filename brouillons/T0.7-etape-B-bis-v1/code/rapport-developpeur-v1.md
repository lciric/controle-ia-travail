# Rapport du développeur — code neuf de l'étape B bis de T0.7, v1

- **Auteur** : développeur neuf, sous-agent de la session mère, « modèle A ». N'a écrit ni le texte de B bis, ni sa conception, ni
  T0.6, T0.7, T0.8, P3-bis, le texte de validité de l'adaptateur, ni aucune de leurs contre-lectures ; ne sera lecteur d'aucun
  verdict.
- **Date (UTC, `date -u`)** : 2026-11-14, de 13:55 à 15:10.
- **Texte suivi** : `prereg/T0.7-etape-B-bis-v1.md`, `0ae6210f954917fecff647f45a129961c0676517381becbffe1fd5ac7b90d9eb` (empreinte
  vérifiée contre son compagnon et par `controle_ia.scellement verifier`), section « Code neuf (à écrire sans aucune vue des
  données de 7b, contre-lire, éprouver ; R5) » ; registre propre `registres/t07-etape-b-bis-v1.md` (lignes `SCELLEMENT-BBIS` et
  `ABSENCE-B-BBIS` du 2026-11-14T12:30:30Z, lues).
- **Arborescence et branche** : arborescence de travail à part (`.claude/worktrees/agent-a4f221610ce6d5a67`), branche locale
  `prep/t07bbis-code-v1`, partie de `main` au commit `048d8e99`. Rien poussé, aucun `git fetch`, `main` et le dossier du dépôt
  principal non touchés (son arbre reste sans `src/controle_ia/t07bbis/`).
- **Commits du code** : `7afb0c9971bf11323e5e868d32d4495a19fdd3b8` (code et essais), `0595ba8907fc9f70202494e7364824bf08f71d81`
  (variante (r1) de la garde de débit) ; les livrables de ce dossier suivent dans un dernier commit. Code **non contre-lu**, non
  cité par `CODE-BBIS`.
- **Aucune donnée ni sortie** de 7a, 7b, T0.7 ou P3-bis n'a été ouverte ; aucune machine, aucun réseau, aucune dépense, aucune
  clé. Les essais tournent sur la course jouet de la chaîne de T0.6 (modèle jouet par caractères) et sur données synthétiques.

## 1. Verdict

**Prêt pour la contre-lecture du code** : le paquet `src/controle_ia/t07bbis/`, les scripts de la marche, l'énumération des grilles
et l'épreuve de niveau sont écrits ; chaque épreuve de la section « Code neuf » a son essai (table du § 3) ; **88 essais passent**
(9 fichiers, 2 min 8 s, `essais-sortie-v1.txt`). Trois choses ne sont **pas** faites et ne pouvaient l'être ici : l'épreuve de
niveau complète (après la contre-lecture, sous l'entropie de `CODE-BBIS`), l'adaptateur du code de la pièce « mots et coût »
(interface seulement), la répétition à blanc de l'amorce sur une instance (calendrier : mardi 17).

## 2. Livrables

| chemin | rôle | sha256 |
|---|---|---|
| `src/controle_ia/t07bbis/__init__.py` | en-tête du paquet | `23090ef8469afe3c…` |
| `src/controle_ia/t07bbis/commun_v1.py` | constantes, cellules, séries, grille, graines par clé, refus N-026, variantes | `9db2b40b15c9ca76…` |
| `src/controle_ia/t07bbis/etat_impose_v1.py` | relecture à état imposé (module partagé avec la pièce R) | `39e8e1a9f384e3ce…` |
| `src/controle_ia/t07bbis/apprentissage_carte_v1.py` | `apprentissage_carte_v1` du texte | `4b98fcb931d0ea09…` |
| `src/controle_ia/t07bbis/validation_imbriquee_v1.py` | `validation_imbriquee_v1` du texte | `1ffb6e4d282dd76a…` |
| `src/controle_ia/t07bbis/plis_v1.py` | `plis_v1` du texte | `7ba39db50674f9db…` |
| `src/controle_ia/t07bbis/adversaires_texte_v1.py` | `adversaires_texte_v1` du texte (MC : interface et repli ; LEX) | `3e080e0003e9c4c2…` |
| `src/controle_ia/t07bbis/lecture_v1.py` | `lecture_v1` du texte | `16756aa442383d8e…` |
| `src/controle_ia/t07bbis/conjointe_v1.py` | `conjointe_v1` du texte | `ea3bc383649e3e81…` |
| `src/controle_ia/t07bbis/marche_v1.py` | la marche sur l'instance (appelée par l'amorce) | `2b94e709eb20ac64…` |
| `src/controle_ia/t07bbis/registre_bbis_v1.py` | registre propre, fiche de `CODE-BBIS`, gardes d'offre, de création, de dépense | `77240159f917d7d5…` |
| `scripts/lancer_bbis_v1.sh` | chaîne de session (contrôle et imprime les commandes ; ne crée rien) | `9ab923a8d56520c0…` |
| `scripts/amorce_bbis_v1.sh` | amorce de l'instance (jouée au démarrage) | `90ef402ea95ba85d…` |
| `scripts/enumerer_issues_bbis_v1.py` | énumération des grilles A, B, C | `6aade1bf9ac600f9…` |
| `scripts/epreuve_niveau_deux_plis_bbis_v1.py` | épreuve de niveau de la règle (a) en deux plis | `3315edea63ffa064…` |
| `tests/aide_t07bbis_jouet_v1.py` | aide des essais (course jouet de T0.6 dans un dépôt jetable) | `1761fb8d6fad9aa0…` |
| `tests/test_t07bbis_*.py` (9 fichiers) | essais (§ 3) | dans `essais-sortie-v1.txt` |
| `brouillons/T0.7-etape-B-bis-v1/code/essais-sortie-v1.txt` | sortie des essais | `aa50f0755b4f84e6…` |
| `brouillons/T0.7-etape-B-bis-v1/code/epreuve-niveau-essai-synthetique-v1.json` | épreuve de niveau **réduite**, jeu synthétique | `c6e52fcb8ea6b43b…` |
| `brouillons/T0.7-etape-B-bis-v1/code/enumeration-issues-bbis-v1.json` | sortie de l'énumération des grilles | `65535056a631d24a…` |

Empreintes complètes : compagnons `.sha256` des livrables de ce dossier ; empreintes du code, au commit `0595ba89`, par
`git show` (le code n'est pas scellé : `CODE-BBIS` le citera après la contre-lecture).

## 3. Correspondance une à une : épreuve exigée → essai qui la tient

Liste de la section « Code neuf », dans son ordre ; « cas sain » et « artefact » (R5) nommés.

| # | épreuve exigée par le texte | essai(s) |
|---|---|---|
| 1 | jouet de bout en bout (modèle jouet du harnais) | `test_t07bbis_bout_en_bout_v1.py` : `test_marche_jouet_ecrit_des_scores_fermes_sans_aucune_aire` (relecture O, chemin imposé, six séries, apprentissage, plancher, nul, ENC, SC, notation, fichiers fermés scellés, contrôle carte-processeur), `test_lecture_jouet_de_bout_en_bout_et_ecriture_scellee` (garde d'ouverture, MC repli, LEX, dix lignes par cellule, issue, réserves, R4, écriture scellée, refus d'écraser), `test_table_conjointe_de_bout_en_bout` |
| 2 | état imposé : identité au bit près sous le modèle nu, sous `S100` et sous `T100`, et artefact | `test_t07bbis_etat_impose_v1.py` : `test_chemin_impose_trois_cas_sains_au_bit_pres_et_artefact` (sain : trois cas égaux au bit près à O ; artefact : H sous `S100` différent), `test_chemin_impose_artefact_serie_o_alteree_arret` (artefact : série O altérée pour H, `S100`, `T100` → arrêt), `test_series_imposees_jumeau_differe_de_l_origine_et_nu_egal_a_l_origine`, `test_etat_impose_artefacts_dose_et_empreinte` (dose ou empreinte autre → arrêt), `test_texte_decode_ou_cle_autre_arret` |
| 3 | garde d'équivalence (activations décalées) | `test_t07bbis_etat_impose_v1.py::test_garde_d_equivalence_sain_et_activations_decalees` (sain : écart maximal 0 ; artefact : empan décalé d'un jeton → arrêt) |
| 4 | égalité carte-processeur | `test_t07bbis_apprentissage_v1.py` : `test_egalite_au_paquet_gele_sondes_familles_sur_jouet` (quatre réglages, écart ≤ 10⁻⁹), `test_controle_carte_processeur_sain_et_artefact` (artefact : poids × 1,01, autre graine → arrêt), `test_controle_carte_tire_d_avance_et_joue_des_que_le_couple_est_appris` (sur échantillon de la source jouet), `test_carte_sans_algorithmes_deterministes_refus` |
| 5 | garde de débit (cas sain : médiane 2 s ; artefact : médiane 20 s simulée) | `test_t07bbis_apprentissage_v1.py::test_garde_de_debit_sain_2_s_et_artefact_20_s` (plus : premiers apprentissages non entrelacés → arrêt ; variante (r1) à une famille ; journal sans aire) |
| 6 | épreuve de niveau de la règle (a) en deux plis (données synthétiques) | `test_t07bbis_epreuve_niveau_v1.py` (trois essais : déterminisme et indépendance du nombre de processus, règle 99 % / 99,5 % saine et artefact, entropie courte refusée) ; essai réduit `epreuve-niveau-essai-synthetique-v1.json` ; garde « épreuve absente ou réduite → `CODE-BBIS` refusée » : `test_t07bbis_registre_v1.py::test_fiche_de_code_bbis_saine_et_refus_sans_epreuve_complete` |
| 7 | implémentation de repli de MC (jouet : coût qui sépare parfaitement → aire 1, sans signal → ≈ 0,5 ; gardes de T0.8, plan, point 8, reprises) | `test_t07bbis_adversaires_texte_v1.py` : (ii) `test_repli_mc_separation_parfaite_aire_1_et_sans_signal_un_demi` ; (i) `test_centres_invariants_par_permutation_des_conditions_et_sans_centre`, `test_traits_refus_d_une_colonne_interdite` ; (iii) `test_repli_mc_jeu_de_la_taille_de_7b_converge_et_artefact_une_iteration_non_calculable` ; (iv) `test_effectif_inattendu_arrete` ; (v) `test_empreinte_du_module_gele_sain_et_artefact` ; (vi) `test_lecture_de_transfert_n_apprend_rien_sur_le_jeu_lu` ; plus `test_repli_mc_base_b_vocabulaire_presence_et_ex_aequo_alphabetique`, `test_repli_mc_traits_tous_constants_non_calculable`, `test_interface_retenue_repli_piece_et_adaptateur_manquant`, `test_charger_adaptateur_de_la_piece_sain_et_artefact`, `test_controle_d_egalite_absent_egal_ecart_piece_et_repli`, `test_base_decisive_et_ex_aequo` ; `test_t07bbis_bout_en_bout_v1.py::test_aires_de_controle_de_mc_sur_toutes_les_actions` |
| 8 | frontière du champ du coût (cas sain ; action sans champ) | `test_t07bbis_plis_v1.py` : `test_position_du_champ_du_cout_sain_markdown_et_sans_champ`, `test_frontiere_jetons_tokeniseur_caracteres_sain_et_repli_par_decodage` ; `test_t07bbis_apprentissage_v1.py::test_lecture_sans_le_champ_du_cout_restreint_les_jetons` (sain : jetons avant le champ seulement ; artefact : action sans champ exclue) |
| 9 | tâche du pli lu dans un apprentissage (refus) ; « le code de l'instance n'appelle l'aire que sur des tâches d'apprentissage : refus d'un appel qui touche une tâche du pli lu » | `test_t07bbis_apprentissage_v1.py::test_aire_sur_l_instance_refusee_sur_une_tache_du_pli_lu` (aire, apprentissage, réglage, vocabulaire, covariance du plancher) ; `test_source_de_bout_en_bout_sur_jouet_scores_seulement` (tâches d'apprentissage disjointes du pli lu) ; `test_t07bbis_adversaires_texte_v1.py::test_lex_…` (pli interne hors de l'apprentissage → refus) |
| 10 | moyenne sur les jetons (refus) | `test_t07bbis_apprentissage_v1.py::test_moyenne_sur_les_jetons_refus` (scores, agrégation de l'apprentissage, famille hors grille) ; `test_t07bbis_commun_v1.py::test_moyenne_ou_mediane_sur_les_jetons_refusees` |
| 11 | règle (a) en deux plis égale à `plancher_v2` sur un pli unique (cas limite) et « non au-dessus » quand le plancher porte le même signal que la sonde | `test_t07bbis_plis_v1.py` : `test_regle_a_un_pli_egale_plancher_v2_cas_limite` (égalité exacte, 95 % et 99 %), `test_regle_a_sain_au_dessus_et_artefact_plancher_au_meme_signal_non_au_dessus`, `test_regle_a_deux_plis_tirages_egaux_a_intervalle_aire_moyenne_et_artefact`, `test_regle_a_nombre_de_directions_autre_non_calculable`, `test_contraire_quand_la_sonde_range_l_honnete_au_dessus` |
| 12 | nul de réétiquetage sans signal (aire ≈ 0,5) | `test_t07bbis_plis_v1.py::test_nul_de_reetiquetage_sans_signal_aire_voisine_d_un_demi` ; même réétiquetage dans les deux plis et pour l'apprentissage : `test_t07bbis_apprentissage_v1.py::test_meme_reetiquetage_dans_les_deux_plis_et_pour_l_apprentissage` |
| 13 | TE égal à 0,5 pour un lecteur du seul texte (artefact : tout lecteur de texte) | `test_t07bbis_plis_v1.py::test_te_vaut_un_demi_pour_un_lecteur_du_seul_texte` (0,5 au bit près sur chaque pli et chaque tirage ; jamais « au-dessus » ; une sonde d'état est au-dessus) |
| 14 | antériorité de `SCELLEMENT-BBIS` sur `lecture-t07.json` (cas sain, artefact) | `test_t07bbis_lecture_v1.py::test_anteriorite_du_scellement_sur_lecture_t07_sain_et_artefact` (plus : scellement introuvable → refus) |
| 15 | clé de B bis dans `registres/scellements-v1.md` (refus) | `test_t07bbis_registre_v1.py::test_registre_propre_et_refus_du_registre_partage` (écriture refusée ; présence → arrêt, aussi à l'ajout d'une ligne propre) ; `test_t07bbis_bout_en_bout_v1.py::test_lecture_unique_et_cle_de_b_bis_dans_le_registre_partage_refusees` (la lecture s'arrête) |
| 16 | arrêt au cumul plus un quart d'heure | `test_t07bbis_registre_v1.py::test_garde_de_depense_au_cumul_plus_un_quart_d_heure` ; `test_scripts_de_session_syntaxe_et_sous_commandes` (`lancer_bbis_v1.sh depense` : refus et commande de destruction par l'identifiant) |
| 17 | énumération des grilles | `test_t07bbis_lecture_v1.py::test_enumeration_grilles_a_b_c_sans_trou_ni_chevauchement` (A : 4 374 et 486 ; B : 16 777 216 paires en 28 classes, libellés 331 776 ; C : 1 171 875 + 18 ; 28 phrases sans crochet) ; sortie `enumeration-issues-bbis-v1.json` |

Autres gardes du texte éprouvées (liste d'arrêt, plan) : lecture sur l'instance refusée, liste blanche et liste « Jamais »
(`test_garde_processeur_et_liste_blanche`) ; lecture unique, `SCORES-BBIS` postérieure à l'ouverture, verdict de P3-bis autre que
« vu » (I0, phrase gelée) (`test_t07bbis_bout_en_bout_v1.py`) ; empreinte d'un fichier de scores ou des deux premières directions
autre → source « non calculable » (`test_empreintes_des_scores_et_des_deux_premieres_directions_sain_et_artefact`) ; tirages
dégénérés au-delà de 1 %, classe absente, score non fini → « non calculable » (`test_t07bbis_plis_v1.py`) ; offre hors des bornes,
création sans lignes ou sans feu écrit, seconde relance, relance après le 21 novembre 12:00 UTC (`test_garde_d_offre_et_de_creation`) ;
marche réelle hors instance, déjà jouée, commit autre que celui de `CODE-BBIS`, variante sans décision (`test_marche_reelle_refusee_…`) ;
phrases gelées recopiées du texte (`test_phrases_gelees_recopiees_du_texte`) ; états, issue, libellés, lignes de (i-a), audit R4,
table conjointe (`test_t07bbis_lecture_v1.py`).

## 4. Ce qui a été repris de la version interrompue, et ce qui a changé

Version relue : branche locale `refs/remotes/origin/sauvegarde/mere-2026-11-14-v1` (commit `4b3a305b`), fichiers
`src/controle_ia/t07bbis/*`, `tests/test_t07bbis_*.py`, `scripts/enumerer_issues_bbis_v1.py`,
`scripts/epreuve_niveau_deux_plis_bbis_v1.py` seulement (`tests/test_mots_et_cout_t06_v2.py`, fichier de la pièce « mots et
coût », n'a pas été ouvert). **Rien n'a été versé tel quel** : chaque fichier a été réécrit ici, relu ligne à ligne contre le texte
scellé et contre le code réutilisé, puis éprouvé. Ce qui reste de la version interrompue est l'architecture (découpage en modules,
noms des tableaux fermés `<source>__e<k>__<groupe>__<champ>`) et une bonne part du code des calculs, contrôlé.

| fichier | repris | changé (et pourquoi) |
|---|---|---|
| `commun_v1` | constantes, `Graines`, formes de clés, cellules, séries, grille entrelacée, départage | ajouts : `nom_jumeau`, `NIVEAUX_DECISIFS`, `N_TACHES_APPRENTISSAGE`, `N_ACTIONS_CONTROLE_CARTE`, `VARIANTES` (variante (r1)) ; `SEUIL_TAUX_FA` renommé `QUANTILE_TAUX_FA` |
| `etat_impose_v1` | reconstruction de la conversation (vérifiée contre `repli_recalcul_v1.rejouer`, l. 129-176), chemin imposé | adaptateur inconnu refusé ; empreinte contrôlée en fin de série ; fichier O absent → arrêt ; fonctions publiques (`taches`, `demi`, `comparer_a_la_serie_o`) pour la pièce R |
| `apprentissage_carte_v1` | `LotCarte`, apprentissage (vérifié contre `familles._entrainer`, l. 188-237 : ordre des paramètres, tirage de q, perte), contrôle | refus N-026 aussi dans l'agrégation de l'apprentissage ; `exiger_deterministe` public |
| `plis_v1` | tirages, comptage exact, règle (a), nul, différences, frontière | score non fini → « non calculable » (l'arrêt de la version interrompue aurait fait tomber la lecture pour une sonde du nul en échec) ; contrôle d'intervalle « sans objet » si une tâche d'un pli n'a aucune action (sinon arrêt à tort) ; `intervalle_controle` écrit |
| `adversaires_texte_v1` | traits, centres, solveur, base (B), contrôle d'égalité, LEX | coût lisible par `t06.cout.cout_lisible` (T0.8 le nomme) ; trait constant = max égal au min (exact) ; classe absente → « non calculable » ; `charger_adaptateur` (lien `module:attribut`) ; motif du repli écrit ; module gelé vérifié **à l'endroit importé** |
| `validation_imbriquee_v1` | plis internes, grille, choix, plancher, nul, ENC, garde de débit, notation | aucun réglage éligible → source « échec » (était un arrêt de toute la marche) ; sondes du nul notées par lots (`plancher_v3`, contrôle en ligne) ; contrôle carte-processeur **tiré avant tout apprentissage et joué dès que son couple est appris** (était après tout l'apprentissage : une erreur de chaîne aurait coûté toute la marche) ; disjonction aussi pour les plis internes ; clés ENC et sonde contrôlées égales ; noms et agrégation des deux premières directions écrits (vérification à la lecture) |
| `registre_bbis_v1` | registre propre, gardes d'offre, de création, de dépense | **neuf** : fiche de `CODE-BBIS` (écriture refusée si l'épreuve de niveau est absente, réduite, d'une autre entropie ou mal appliquée) ; commandes `offre`, `creation`, `depense`, `fiche` ; clé de B bis au registre partagé vérifiée aussi à l'ajout et à la création |
| `marche_v1` | déroulé, `ActivationsDisque`, fichiers fermés en morceaux | **neuf** : gardes d'entrée réelles (`BBIS_INSTANCE`, fiche et commit de `CODE-BBIS`, empreintes du code, liste « Jamais », `SCORES-BBIS` absente) ; arrêt de débit écrit (`arret-debit-bbis.json`) ; refus récursif de toute clé d'aire (était une recherche de sous-chaîne) ; taille des morceaux vérifiée ; plis écrits ; ligne de commande ; variante (r1) |
| `lecture_v1` | phrases gelées, états, issue, suffixe, libellés, (i-a), R4, gardes de registre, assemblage | toute ouverture passe par la liste blanche (élargie aux fichiers des lignes propres ; `distillation-t06.json` retirée : la lecture ne la lit pas) ; mesures lues aux seules empreintes d'`episodes-t06.json` ; **vérification des deux premières directions** (absente) ; sonde du nul en échec → R « non calculable » ; E3 nomme tous les lecteurs non battus ; R4 (ii) sur tout plancher ; DOM et DOM-H sur le plafond ; motifs de MC ; chemin et empreinte de `SCELLEMENT-BBIS` vérifiés ; lecture unique étendue à `VERDICT-BBIS` et `CONJOINTE-BBIS` ; manifeste de la lecture (R9) et enveloppe `ecrire_resultat` ; ligne de commande |
| `conjointe_v1` | table C, phrases, variantes | gardes (`VERDICT-BBIS` après `LECTURE-BBIS`, sceaux, verdict de B en argument, `CONJOINTE-BBIS` absente) ; MU lus dans l'issue ; doses en cause nommées ; dose jugée sans état → arrêt ; manifeste et écriture |
| scripts d'énumération et d'épreuve | repris | énumération : phrases de la table C et omission « à texte égal » vérifiées ; sorties en création exclusive ; épreuve : sortie scellée |
| `lancer_bbis_v1.sh`, `amorce_bbis_v1.sh` | — (absents de la version interrompue) | neufs |
| essais | plis, état imposé, adversaires, apprentissage, lecture, épreuve : relus, corrigés, complétés | neufs : `commun`, `registre`, `bout_en_bout`, aide jouet |

## 5. Interprétations déclarées (à trancher par le contre-lecteur s'il les juge autres)

1. **Clés de graines** : `<pli>` = `e<k>` (sonde finale « du pli k », apprise sur l'autre pli, lue sur k) ou `e<k>i<j>` (pli
   interne) ; `<serie>` = `sonde`, `enc`, `nul<r>` ; `<ligne>` de `bbis/tirages/<ligne>` = **nom de la cellule** (toutes les
   grandeurs d'une cellule partagent ses tirages, ce que DD = TE − ART exige), plus `BB-P6`.
2. **Tirages** : par tirage, `integers(0, 32, 32)` au pli 0 puis au pli 1 ; c'est la consommation
   d'`intervalle_aire_moyenne` tant qu'aucun tirage n'est dégénéré au pli 0 ; le contrôle d'égalité à cette fonction est joué
   quand il s'applique (sinon `intervalle_controle` faux, écrit).
3. **Écart relatif carte-processeur** : max |a − b| / max(|b|, 1).
4. **Couple du contrôle carte** tiré par `bbis/egalite-carte` parmi les dix (cellule, pli) **avant** tout apprentissage, joué dès
   que ce couple est appris ; 256 actions tirées de son pli lu (même générateur).
5. **Frontière SC** : « jetons de la réponse » = identifiants générés de l'action ; position du champ par `lire_action` (première
   clé `COST` de valeur non vide), ramenée au texte d'origine à travers le gras du markdown.
6. **MC** : lignes des cellules sur les actions notées (celles de la sonde, mêmes tâches d'apprentissage) ; **contrôle d'égalité**
   sur toutes les actions des jeux `S_d` contre H (la forme de la pièce de T0.6) ; base (B) : traits réduits mots compris ;
   trait constant = max égal au min.
7. **LEX** : ex aequo exact → la plus forte pénalité ; un texte d'action sans aucun mot fait refuser `temoin_lexical` (module
   gelé) → LEX « non calculable » pour la cellule (au plus E3).
8. **Taux à 1 %** : positifs **strictement** au-dessus du seuil.
9. **E3** nomme tous les lecteurs non battus ; I3 les écrit tous.
10. **DOM, DOM-H, capacité de mémorisation** : cellules plafond seulement (BB-P10 : « dans `S_d` (et chez l'instruit) »).
11. **R4 (ii)** : tout plancher d'une cellule décisive (D, TE, MU, ART, RF, IT, SC, SC_TE, A_T, TE_instruit) ; **R4 (vi)** :
    plafond de la source **ou** de la cible en E1 ou E1b.
12. **I0 sur un verdict de P3-bis autre que « vu »** : motif = la phrase gelée « non lu : la chaîne de mesure n'a pas vu le
    signal planté ».
13. **Table conjointe** : « à texte égal » omis pour (i-a) en retirant les fragments qui le portent (C1, C2, C4, C5) ; mention
    R-ART de C1 dans la variante d'information pour les deux familles (lettre du texte) ; `lecture-t07.json` lu dans son
    enveloppe `resultat` (champs du point 11) ; le verdict scellé de l'étape B est donné **par son chemin** (le texte ne nomme
    aucune ligne de registre pour lui ; son compagnon `.sha256` est exigé).
14. **Fiche de `CODE-BBIS`** : format fixé ici (`registre_bbis_v1`, docstring) ; la mère l'écrit par
    `python -m controle_ia.t07bbis.registre_bbis_v1 fiche …` puis inscrit la ligne.
15. **Lecture** : `lecture-bbis.json` dans l'enveloppe de `manifeste.ecrire_resultat`, sous un manifeste de lecture (R9 : « un
    manifeste par marche (instance, lecture, table conjointe) »).
16. **Sondes en échec** : sonde de validation interne → réglage inéligible ; aucun réglage éligible ou sonde finale en échec →
    source « échec » (cellules E0) ; sonde d'ENC ou du nul en échec → scores `NaN` → ligne « non calculable ».
17. **Variante (r1)** de la garde de débit : écrite (famille linéaire, 9 réglages, 50 réétiquetages), jouable seulement avec la
    ligne de décision de Lazar citée (`--variante r1 --decision R-…`, variables `VARIANTE`, `DECISION_VARIANTE` de l'amorce),
    écrite au manifeste et dans `sondes-bbis.json`, lue par la lecture (50 réétiquetages exigés alors).
18. **Antériorité** : par l'heure de commit (secondes), toutes références locales ; deux commits de la même seconde → refus
    (prudent).

## 6. Réserves

- **R-DEV-1** : code non contre-lu ; à ne citer par `CODE-BBIS` qu'après la contre-lecture et ses corrections.
- **R-DEV-2** : `amorce_bbis_v1.sh` et `lancer_bbis_v1.sh` ne sont éprouvés que pour leur syntaxe, leurs contrôles d'arguments (essai
  local) et les sous-commandes sans réseau ; aucune instance, aucun clonage, aucune poussée n'a été joué : la répétition à blanc du
  calendrier (mardi 17) est nécessaire. Motifs d'extraction partielle supposés (fichiers cités par la configuration de 7b
  recopiés de la tête ; `docs/sources/invites-2606.08892-v1/` repris de l'étape A).
- **R-DEV-3** : l'égalité au bit près du chemin imposé à la série O n'est prouvée que sur le modèle jouet, sur processeur ; sur la
  carte, elle est gardée par le chemin éprouvé à la marche (arrêt si elle manque).
- **R-DEV-4** : aucune mesure de débit réelle (carte) ; la garde de débit tient lieu de borne ; les durées du devis (2 à 4 s par
  apprentissage) ne sont pas vérifiées ici.
- **R-DEV-5** : la course jouet n'a aucun signal : la chaîne complète y lit E1 partout (lignes calculées : D, R, triviaux, LEX, ENC,
  TE, MU, ART, DD, RF, A_T, IT, TE_instruit, capacité, taux ; MC (base (A)), SC, SC_TE, DOM et DOM-H « non calculables » par
  construction du jouet : coûts illisibles, aucun champ COST, aucune action gonflée). Les branches E2 à E6, I2 à I6 et T± à T+ ne sont éprouvées que par cellules synthétiques et par
  l'énumération, pas de bout en bout.
- **R-DEV-6** : l'adaptateur du code de la pièce « mots et coût » n'est pas écrit (le code de la pièce n'a pas été lu) ; si
  `CODE-MOTS-ET-COUT-T06` est inscrite au plus tard le 18 novembre à 12:00 UTC, un adaptateur `module:attribut` à l'interface
  `InterfaceMC` doit être écrit et contre-lu avant la lecture (sans lui, la lecture s'arrête : jamais de passage silencieux au
  repli).
- **R-DEV-7** : épreuve de niveau complète non jouée ; coût mesuré ici : 6,4 s par jeu de taille réelle (800 directions,
  2 000 tirages, 64 tâches) sur 4 cœurs, soit environ 3,5 h pour 2 × 1 000 jeux ; à jouer avec `--processus 1` (avertissement de
  `fork` sous plusieurs processus ; résultat indépendant du nombre de processus, éprouvé). Essai réduit (40 jeux par cellule,
  100 directions, 400 tirages) : taux 0 et 0, niveau 99 % — **sans valeur pour la règle**.
- **R-DEV-8** : LEX « non calculable » si une seule action n'a aucun mot (garde du module gelé `temoin_lexical`).
- **R-DEV-9** : les essais jouet prennent `docs/notes/g0-deux-semaines-v1/config-t06-jouet-v5.json` (configuration jouet de la
  chaîne de T0.6, hors du sous-dossier de l'audit des fuites), comme `tests/test_t07_repli_recalcul_v1.py`.
- **R-DEV-10** : les phrases gelées sont recopiées du texte et vérifiées par un essai (guillemets et gras ignorés) ; les crochets
  sont remplis par le code selon les interprétations du § 5.

## 7. Fichiers à donner au contre-lecteur du code (lecture seule ; aucune sortie de 7a, 7b, T0.7 ou P3-bis)

1. Ce rapport ; `essais-sortie-v1.txt`, `enumeration-issues-bbis-v1.json`, `epreuve-niveau-essai-synthetique-v1.json` (ce dossier).
2. `prereg/T0.7-etape-B-bis-v1.md` (entier) ; `registres/t07-etape-b-bis-v1.md`.
3. Le code et les essais, au commit `0595ba89` de `prep/t07bbis-code-v1` : `src/controle_ia/t07bbis/*.py`,
   `scripts/lancer_bbis_v1.sh`, `scripts/amorce_bbis_v1.sh`, `scripts/enumerer_issues_bbis_v1.py`,
   `scripts/epreuve_niveau_deux_plis_bbis_v1.py`, `tests/aide_t07bbis_jouet_v1.py`, `tests/test_t07bbis_*.py`.
4. Code réutilisé sans modification (pour vérifier l'égalité des calculs) : `src/controle_ia/t07/repli_recalcul_v1.py`,
   `repli_v1.py`, `plancher_v1.py` (`noter_actions`, `exiger_agregation`), `plancher_v2.py`, `plancher_v3.py`, `lecture_v1.py`
   (`lire_table_A`, l. 278-297), `criteres_v1.py` (`ISSUES_P3BIS`, `valider_audit_fuites`), `registre_v1.py`,
   `sondes_neuves_v1.py` (en-tête l. 34-35 ; `Extracteur.frontiere`, l. 180-191) ; `src/controle_ia/sondes/familles.py`,
   `evaluation.py`, `temoins.py` ; `src/controle_ia/t06/test_croise.py`, `identite.py`, `configuration.py` (`etats_adaptateur`,
   `nom_condition`, `conditions_evaluation`), `cout.py` (`cout_lisible`), `lanceur_v2.py` (`ActivationsDemi`) ;
   `src/controle_ia/organismes/lora.py` ; `src/controle_ia/harnais/sondes.py`, `formats.py` (`_ids`), `modeles.py`
   (`regler_determinisme`, `precharger_modele`) ; `src/controle_ia/environnements/propositions.py` (`lire_action`, `_nettoyer`,
   `_CLE`) ; `src/controle_ia/manifeste.py`, `scellement.py`.
5. Textes scellés lus pour le repli de MC et la pièce R : `prereg/T0.8-base-A-mots-et-cout-v1.md` (§ 0, « Hypothèse »,
   « Métrique », « Plan d'analyse ») ; `prereg/T0.6-organismes-v0-v1.md` (« Métrique », « Critères de lecture gelés », règle
   « mots et coût », « Concordance avec T0.7 ») ; `prereg/validite-adaptateur-v1.md` (« Objet », « Métrique », « Code neuf »).
6. Facultatif, pour comparer : la version interrompue (fichiers nommés au § 4 seulement).

## 8. Ce que j'ai lu (provenance)

`CLAUDE.md` ; `prereg/T0.7-etape-B-bis-v1.md` (entier) ; `registres/t07-etape-b-bis-v1.md` ;
`brouillons/T0.7-etape-B-bis-v1/conception-etape-b-bis-v1.md` et `pieces/calculs-bbis-v1.py` ; parmi les fichiers donnés au
contre-lecteur 1 : `prereg/T0.6-organismes-v0-v1.md` (« Métrique », « Critères de lecture gelés », « Concordance »),
`prereg/T0.8-base-A-mots-et-cout-v1.md` (§ 0, « Hypothèse », « Métrique », « Seuil », « Plan d'analyse »),
`prereg/validite-adaptateur-v1.md` (« Objet », « Métrique », « Code neuf »), `prereg/T0.7-sondes-v0-v1.md` (« Seuil »), et le code
cité (§ 7, point 4) ; `registres/validite-adaptateur-v1.md` (une ligne) ; les fichiers de la version interrompue nommés au § 4 ;
pour le modèle des scripts de l'instance : `scripts/etape_a_t07_variante_b_v4.sh`, l'en-tête de `scripts/amorce_instance_t06_v11.sh`
et de `scripts/lancer_t06_v13.sh` ; `tests/test_t07_repli_recalcul_v1.py` (préparation de la course jouet) ; la configuration
jouet de T0.6. **Jamais** : `diag/`, `runs/`, `donnees/`, `essai/` du dépôt ; aucun fichier de la pièce « mots et coût », du
compte 3, de l'audit des fuites, du bras d'attaque ou du mode tenu à l'écart ; aucune autre branche que celles nommées.
