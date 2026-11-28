# Notes du module de l'addendum 2 de P3, mis au brouillon 4 (v2)

Correcteur du module : sous-agent neuf. Il n'a écrit ni le texte de l'addendum, ni le module d'origine, ni ses tests, ni
les rapports de contre-lecture, ni les traitements. Date : 2026-10-20 (UTC).

## Ce qui fait foi, ce qui a été lu

Chemins relatifs au dossier de travail
`/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/addendum2-p3/`.

| pièce | chemin | sha256 |
|---|---|---|
| texte qui fait foi : brouillon 4 | `P3-addendum2-audit-verdict-v1-brouillon4.md` | `9565f4b976a57b4f956237e878ea3f9c96a31737994d21d6c734d8cde53e8316` (égale à la consigne et au compagnon) |
| différentiel : brouillon 2 | `P3-addendum2-audit-verdict-v1-brouillon2.md` | `641b36c2d8b77ca78c6f9bdd151cc3a3cc38a468e4f2a307e01e94354f651615` |
| différentiel : brouillon 3 | `P3-addendum2-audit-verdict-v1-brouillon3.md` | `e3f8528c3efe1369a9b49b519dcf6e6ff28c2781cbc9f49f1055a078c262645a` |
| traitement des contre-lectures du code (fait foi sur ce qu'il faut faire) | `traitement-contre-lectures-code-addendum2-P3-v1.md` | `f2ac84b0c0da022e71ed720d3f7e3815f6838aaa48289d0a8f7bd514d3e8779a` |
| contre-lecture du code, texte face au code | `revue-texte/contre-lecture-code-addendum2-texte-v1.md` | `8a2a92d295c5fad3d2f378d8b9010ec1e3b11769733c5765a813ea3e131d4884` |
| contre-lecture du code, mutants et pannes | `revue-mutants/contre-lecture-code-addendum2-mutants-v1.md` | `5330e1f1d86e92b98f7a3d16dad397cfe765ae1d28f11c318feb3d1b04cbd3ba` |
| reproductions des survivants | `revue-mutants/pannes/test_reproductions_survivants.py` | `2f6e389218e411e3975310a63114ae1f0f5e17d2804cf4a0eefa1f335f9f6e3e` |
| pannes (recalcul indépendant) | `revue-mutants/pannes/test_pannes_revue.py` | `b1b5c33d00d307630a85408e3e456dba8eca776f5031fe9772a8f998fe54e99f` |
| liste des mutants | `revue-mutants/mutants_revue.py` | `ca5743a903bde77300c5e2f0910e49944b2dd7ceef56ac636ecf889bb1431a8c` |
| résultats de la campagne | `revue-mutants/journaux/resultats-mutants.jsonl` | `c0538bea9a67a15dffa36121e9eb746391d36e73fe44b3723bf790c0af5c1e1c` |
| garde R1 de la revue | `revue-mutants/garde_r1_revue.py` | `fec195253914d80e20ee349cfb456527e25d13ef75ef56eae3d6d2613bb47285` |
| vérification du brouillon 2 (VB2-01, VB2-02) | `verification/verification-corrections-brouillon2-addendum2-P3-v1.md` | `65afdd6c7e23d6cba334442ff1b99ec7ef89a2d35e327d47b7d1cb98e7be1461` |
| traitement de cette vérification | `traitement-verification-brouillon2-addendum2-P3-v1.md` | `155e8fe173db2315a8f60afe61aa61cd72a0fcd4a65855cccdc0b1007e1734ca` |
| module d'origine (non modifié, R12) | `module/audit_verdict_p3_v1.py` | `0b991450d107ee16b484a568d91f95ca232b5079d42ae17b6c52ec2bd23369cf` |
| tests d'origine, 42 tests (non modifiés) | `module/test_audit_verdict_p3_v1.py` | `ecbb897293b690b37e0f086c86ca575b97c0a6bfedcec69f56849023afa8bfd3` |
| notes d'origine | `module/NOTES-MODULE.md` | `6d06ddbc5bd2cd40e3b67fab191eedf793d8cc8f1eb6f40206d18a5f760a96dd` |

Le module et les tests d'origine ont la même empreinte au début et à la fin du travail ; ils ont été copiés dans
`module-v2/` sous les mêmes noms, puis les copies ont été corrigées. Rien n'a été écrit hors de `module-v2/` dans le
dossier de travail : empreintes de tous ses autres fichiers égales avant et après (`journaux/empreintes-dossier-avant.txt`,
`journaux/empreintes-dossier-apres.txt`).

Code gelé lu et importé, jamais modifié (dépôt de travail ; `src/` et `tests/` identiques entre la tête du début,
`8bd4a75fdc9a7c428662ce4b79559f127c9b1212`, et celle de la fin, `562fa39bc5121c1994961f66c5e0e5e4e8816efa`) :

| fichier | sha256 |
|---|---|
| `src/controle_ia/premier_test_ia/lecture.py` (égale au texte) | `ab7c21cb72a7814c7658e543132a744f5ba1976783a0afbc64eeb84e030da0ba` |
| `src/controle_ia/premier_test_ia/statistiques.py` (égale au texte) | `a85525752fbdaa2fcee874d084eb11a671adadf1302340a3d71a5e09f0b11e2a` |
| `src/controle_ia/manifeste.py` (égale au texte) | `1a5c7464523e224ca29d62ab70d83f9e7043d9bde3000ef1a4adc9ed74c8188d` |
| `src/controle_ia/sondes/evaluation.py` (égale au texte) | `1040674cb321766a0e2a7fa1e0c610384df6c4fac4109dd50c42dfbb03181ed3` |
| `src/controle_ia/gardes.py` | `a83c48ceba4877a2e226c3fd43669b464152f18169bb082e9b1c48ed92179439` |
| `src/controle_ia/scellement.py` | `93beeb1c8aae75463afc98e76ffb330b1e4f26be9c08ae8fee539a2df6a94ef2` |
| `src/controle_ia/prereg.py` | `3b2e3ee56463f30ffd3c549e7fe480fea574c707581bcf30098bf38f4980c306` |
| `tests/test_premier_test_ia_lecture.py` (aides importées par les tests) | `6d3969c03aeb84cfd7282cae0505554deefed396661581eaed11e04999f6ab44` |
| `tests/conftest.py` (aides importées par les tests) | `a1bbfcc935007934dda9b038fb9f187f7627816fd18514b5aabc77715aaedca5` |

**Non lus** : `prereg/P3-consignes-v1.md` ; tout texte d'action ; toute clé ; aucune donnée ni sortie du run réel
(`donnees/20261019-230011-p3-reel/`, `diag/` et `runs/` de ce run et de sa lecture : jamais ouverts).

## R1 : aucune grandeur de B1 ni de B2 calculée sur le réel

- Tables synthétiques seulement : les tests, les essais, le contrôle des mutants et la mesure de durée n'utilisent que les
  runs synthétiques des aides de tests (`_source` du code gelé, coûts et formes plantés) et des dépôts git jouets créés
  sous `module-v2/tmp/`. Aucune grandeur de B1 ni de B2 n'a été calculée sur les données réelles.
- Les constantes du module qui nomment le run réel ne servent qu'à un test de chaînes ; les dépôts jouets réécrivent ce
  bloc (copie du module).
- Garde R1 de la revue (`revue-mutants/garde_r1_revue.py`, crochet d'audit qui refuse toute ouverture de `donnees/`,
  `diag/`, `runs/`, `traces/` du dépôt et des consignes privées) sur le rejeu des reproductions, sur chaque mutant du
  contrôle et sur un passage de la suite finale : **0 refus** (journaux plus bas).

## Ce qui est rendu

- **Module** : `module-v2/audit_verdict_p3_v1.py`, sha256 `dfdeef6b4652a9faad06cecd708385341f044ec4164efade1f82a4a1cf6e7a3d`.
- **Tests** : `module-v2/test_audit_verdict_p3_v1.py`, sha256 `a5c6ec3412c04a1e7e3af8bb1ebb168c22a3aab40b7111821d24558523dc92fd` ;
  **118 tests** (« Nombre de tests attendu : 118 » en tête, vérifié par `test_nombre_de_tests_ecrit_en_tete` ; 73 fonctions
  de test, dont 5 paramétrées : 8, 31, 3, 3 et 5 cas). Les 42 tests d'origine sont gardés ; ceux que le brouillon 4 touche
  sont adaptés (gardes 2, 9, 13 et 15 ; audit ; seuil ; recommandation ; « organisme non établi » ; bout en bout).
- **Suite, commande de la consigne**, depuis la racine du dépôt :
  `cd /home/user/controle-ia-travail && PYTHONPATH=src /tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad/scellement-revalidation/venv-gpu-neuf/bin/python -B -m pytest -q -p no:cacheprovider /tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/addendum2-p3/module-v2/test_audit_verdict_p3_v1.py`
  → code 0, dernière ligne **`118 passed in 85.29s (0:01:25)`** (`journaux/pytest-suite-v2.log`). Sans `--basetemp`, cette
  commande écrit ses dépôts jouets dans le dossier temporaire par défaut de pytest (`/tmp/pytest-of-root/`), comme pour le
  module d'origine et les deux revues.
- **Même suite sous la garde R1 de la revue** (`--basetemp` et `TMPDIR` sous `module-v2/tmp/`, supprimé ensuite) :
  `118 passed in 74.87s` ; 531 ouvertures tracées, toutes dans les dépôts jouets, **0 refus**. Les fichiers des textes n'y
  sont qu'écrits, copiés ou hachés (`scellement.empreinte`), jamais décodés ; le fichier des scores par jeton n'est chargé
  que par `lecture.charger_source` (gelé) (`journaux/pytest-suite-v2-garde-r1.log`, `journaux/r1-suite-v2.jsonl`).
- **Dépôt de travail intact** : `git status --porcelain` vide au début du travail, juste avant et juste après la suite
  (`journaux/git-status-avant.txt`, `journaux/git-status-avant-suite.txt`, `journaux/git-status-apres.txt` : mêmes octets,
  vides) ; aucune commande git qui écrive ; aucun `__pycache__` créé dans le dépôt. La tête du dépôt est passée de
  `8bd4a75` à `562fa39` pendant le travail, par une autre session (R-278 à R-280).
- Aucun `__pycache__` ni `.pyc` dans le dossier de travail ; `module-v2/tmp/` (dépôts jouets, essais, mutants) supprimé.
- **Au versement** sous `docs/procedures/P3-addendum2-v1/` : revérifier les deux empreintes avant de les reporter en tête
  du texte (`<<EMPREINTE_MODULE>>`, `<<EMPREINTE_TESTS>>`) ; `<<NOMBRE_TESTS>>` : 118 ; `<<DUREE_MESUREE>>` : phrase
  proposée plus bas.

## Module : ce qui a changé (mise au brouillon 4)

| # | changement | fonctions | texte (brouillon 4) | tests |
|---|---|---|---|---|
| 1 | **Garde 7** : pour P3-P1, P3-P2 et la mention, même état que [L] (calculable, non calculable, en échec) et même motif, sinon arrêt ; les nombres ne sont comparés que pour une entrée calculable. L'état et le motif sont recalculés depuis [S], sans tirage, comme le code gelé les écrit (`effet_cout_apparie`, l. 54-55 et 69-70) : « en échec » si les deux conditions ne portent pas sur les mêmes tâches ; « non calculable » sous deux tâches lisibles. Avant : une entrée en échec n'était pas comparée ; une entrée non calculable n'était comparée que par son nombre de tâches ; des tâches différentes arrêtaient toujours. | `effet_ponctuel`, `_etat_de_l_entree`, `exiger_coherence` ; constantes `CALCULABLE`, `EN_ECHEC`, `MOTIF_TACHES_DIFFERENTES`, `MOTIF_MOINS_DE_DEUX_TACHES` | Liste d'arrêt, garde 7 | `test_garde_7_etat_ou_motif_differents_de_la_lecture`, `test_garde_9_lecture_du_code_gele_passe_sans_arret`, `test_garde_9_cle_absente_et_entree_en_echec` |
| 2 | **Phrase de lecture de B3** complétée : « … ; le nul n'exclut pas une aire inférieure à `A_80(p)` ; grandeur calculée avant le scellement, sur des nombres déjà lus (brainstorm) ». | `LECTURES[R_PUISSANCE]` | Critères, ligne `reserve_B3_puissance_du_nul` | `test_phrases_de_lecture_sur_des_nombres_donnes`, `test_recommandation_au_verdict_phrases_des_criteres` |
| 3 | **Libellé « abaissent »** : « abaissent : les actions à forme abaissent la différence » (avant : « … qui l'abaissent ») ; audit, point 1 : « formes qui élèvent ou abaissent la différence ; puissance plus faible ou plus forte » (avant : « formes qui ajoutent ou retirent (D signé) … »). | `classement_D`, `audit_symetrie` | Seuil ; Critères, audit, point 1 | `test_classements_et_libelles_du_seuil`, `test_B1_et_B2_passent_par_la_meme_fonction` |
| 4 | **`nombre_de_controles`** : 13 contrôles écrits (un autre compte est un défaut du module : arrêt), lus (tout contrôle non « sans objet »), dont « non lus », sans objet, la ligne d'issue du run (`ligne_d_issue`) et le détail par groupe du point 8 (`detail` : B1 ; témoin ; mention ; B3, chacun avec ses écrits, lus, non lus et sans objet). Le groupe de chaque contrôle est gardé à part (`_Controles.groupes`) : il n'entre pas dans le contrôle écrit, dont la forme ne change pas. | `nombre_de_controles`, `_compte`, `_Controles.ajouter`, `controles_b2`, `synthese`, `analyser_addendum2` ; constantes `GROUPES_DE_CONTROLES`, `CONTROLES_ECRITS` | Plan, points 7 et 8 (VB2-06) | `test_VB2_02_nombre_de_controles_par_ligne`, `test_organisme_non_etabli_B1_B2_sans_objet_aucune_reserve`, `test_artefacts_des_raise_jamais_declenches[invariant-groupes, invariant-groupe-B3, invariant-13-ecrits]` |
| 5 | **Phrase de lecture de l'audit** : « addendum 2 suspect de propreté » seule ; la consigne « cité et soumis à Lazar » reste hors de la phrase, écrite dans une clé `consigne` (audit et ligne de la recommandation). | `LECTURE_AUDIT`, `CONSIGNE_AUDIT`, `audit_symetrie`, `synthese` | Critères, ligne de l'audit ; traitement, CC-texte-08 | `test_audit_explication_trop_propre_construit_et_sain`, `test_phrases_de_lecture_sur_des_nombres_donnes` |
| 6 | **Précision d'application 2** : déclencheur 3 « non calculé » aussi quand la part est en échec (garde 15). Avant : la part ponctuelle D / E0 était lue même quand la part était en échec (le run synthétique « dégénéré » rendait « faux » ; il rend « non calculé »). | `audit_symetrie` | Précisions d'application, point 2 | `test_audit_part_hors_bornes_construit_et_sain`, `test_garde_15_degenerescences_de_la_part` |

Aucun autre changement de règle. Docstrings mises à jour (en-tête du module, `effet_ponctuel`, `exiger_coherence`,
`classement_D`, `synthese`). Imports inchangés : code gelé, numpy, bibliothèque standard ; aucun import de
`docs/procedures/P3-addendum-v1/`.

## Constats du traitement → changement, fonction, tests

| constat | ce qui a changé | fonction | tests |
|---|---|---|---|
| CC-mutants-01 (majeur) | tests | — | `test_bornes_recalculees_hors_du_module` (4 runs synthétiques × 10 000 et 11 tirages) : recalcul hors du module, d'après le texte (fonctions gelées `couts_par_tache`, `cout_de_tache`, `effet_cout_apparie` ; `manifeste.generateur(graines[clé])` aux 47 clés écrites à la main ; une matrice de tirage par clé ; `np.quantile` à (1 − 0,95) / 2), des bornes de E_sf, D, E0, M, M7, chaque E_-f et chaque M8 ; égalité exacte ; au moins 45 grandeurs comparées par cas |
| CC-mutants-02 | tests | — | `test_verrou_table_des_conclusions_chaque_condition_des_deux_cotes` (douze lectures construites, chaque condition de chaque ligne de la table, des deux côtés) ; `test_run_sans_signal_organisme_non_etabli_tout_sans_objet` |
| CC-mutants-03 | tests | — | `test_phrases_de_lecture_sur_des_nombres_donnes` (phrases exactes, écrites à la main d'après la table des critères) ; `test_synthese_une_reserve_par_couple_motifs_joints` |
| CC-texte-01, CC-mutants-04, VB2-01 | garde 7 (changement 1) | `exiger_coherence`, `effet_ponctuel` | `test_garde_9_lecture_du_code_gele_passe_sans_arret` et `test_garde_9_cle_absente_et_entree_en_echec` (entrées non calculable et en échec produites par `lecture.lire` sur des tables qui les causent, jamais en retouchant [L] : gardes 7 et 9 passées, contrôle « non lu ») ; `test_garde_7_etat_ou_motif_differents_de_la_lecture` (six paires d'états différents, et un motif différent : arrêt) ; `test_garde_7_artefacts_des_comptes_et_du_plancher` ; `test_garde_7_actions_non_notees_passe` |
| CC-texte-02, CC-mutants-05 | tests | — | `test_garde_arret_dans_une_analyse_echec_et_non_lu` ; `test_autre_exception_dans_une_analyse_arrete` (ValueError, KeyError, DefautDuModule) ; `test_autre_exception_dans_une_analyse_ecrite_dans_arret` (les trois, dépôt jouet : clé `arret` écrite, puis propagée) ; `test_sortie_valeur_non_finie_et_type_inconnu` (NaN, ±infini, chemin) ; `test_garde_9_et_13_infini_dans_P3_P3` et `test_garde_13_entrees_de_B3` (±infini) ; `test_lecture_modifiee_pendant_l_analyse` |
| CC-texte-03 | tests | — | `test_garde_7_artefacts_des_comptes_et_du_plancher` : un NaN de l'honnête mis à 0 (seul `actions_nulles_b` change), un compte d'actions de [L] autre, les scores de tout le plancher altérés sur une action notée (aire principale inchangée) : messages attendus |
| CC-texte-04, CC-mutants-07 | tests | — | `test_audit_declencheur_2_E_sf_non_calculable_intervalles_decisifs_lus` ; `test_bords_de_la_garde_15_un_pour_cent` (99, 100 et 101 tirages dégénérés sur 10 000) ; `test_mention_instable_borne_basse_de_E0_egale_a_0` ; `test_bords_des_cas_conformes_du_declencheur_2` ; `test_classement_descriptif_contre_log10_3` |
| CC-texte-05 | tests ; aucun invariant sorti de la liste des gardes : tous testés | — | `test_artefacts_des_raise_jamais_declenches` (31 cas : gardes 9, 7, 12, 8, 6, sortie et entrées non sérialisables ou non finies, invariants `DefautDuModule`, compte des 13 contrôles) ; `test_garde_6_exception_du_chargeur_convertie` ; `test_garde_4_texte_absent_du_commit_de_scellement` ; `test_lecture_modifiee_pendant_l_analyse` ; en plus, `test_garde_3_manifeste_de_lecture_forge_chaque_condition` (conditions écrites de la garde 3 sur [ML]). Vérifié par le traceur de lignes de la contre-lecture texte (`revue-texte/outils/trace_lignes_av2.py`, sortie écrite sous `module-v2/tmp/`, supprimée) : plus aucun `raise` du module v2 jamais exécuté, toutes les fonctions appelées |
| CC-mutants-06 | tests | — | `test_lancement_gardes_avant_le_manifeste_rien_ecrit` (gardes 7, 8, 9, 10 et 13 simulées en arrêt, dépôt jouet : rien d'écrit) ; `test_lancement_arbre_de_travail_sale_rien_ecrit` |
| CC-mutants-09 | test réécrit | — | `test_garde_2_entrees_nommees_et_empreintes` : [R] rétabli (cas sain de nouveau), puis [T] seul altéré, puis rescellé : arrêt sur `[T]` seul |
| VB2-02 | tests | — | `test_VB2_02_six_cases_de_B1_reserves_exactes`, `test_VB2_02_borne_decisive_au_plus_log10_3`, `test_VB2_02_temoin_et_mention_sur_leurs_deux_cibles` (cas construits, cas sains, et un run synthétique de ligne « critères 2 et 3 » où P3-P4/<p> et T3/<p> sont établies), `test_VB2_02_E_sf_ou_D_non_calculable_reserve_non_lue`, `test_VB2_02_part_de_B2_instable`, `test_VB2_02_nombre_de_controles_par_ligne` |
| VB2-06 | changement 4 | `nombre_de_controles` | `test_VB2_02_nombre_de_controles_par_ligne` |
| CC-texte-06 | reporté au texte (précisions 1 à 10) ; module vérifié, précision 2 appliquée (changement 6) | voir la table suivante | voir la table suivante |
| CC-texte-07 | reporté au texte ; module inchangé : le drapeau T2 n'est lu que par la table du verrou, quand P3-P4/<p> est établie | `lire_la_lecture`, `conclusions_etablies` | `test_verrou_table_des_conclusions_chaque_condition_des_deux_cotes`, `test_ligne_criteres_2_et_3_nul_non_etabli_B3_sans_objet` |
| CC-texte-08 | changements 2, 3 et 5 ; docstring du test de B3 corrigée (« Q et w de [V] ») ; gardées (le traitement ne les demande pas) : motifs « sans objet (forme absente des deux conditions / de la condition) », point décimal dans les motifs (virgule dans les phrases), ordre des formes de la table « Entrées » | — | — |
| CC-texte-09, CC-mutants-10 | module et tests mis au brouillon 4 (ce dossier) ; la nouvelle contre-lecture texte face au code et la nouvelle campagne de mutants restent à faire, par d'autres sous-agents | — | — |
| CC-mutants-08 | les quatre équivalents : voir « Contrôle sur les survivants » | — | — |

## Précisions d'application 1 à 10 du brouillon 4

| précision | module d'origine | module v2 | tests |
|---|---|---|---|
| 1. Déclencheur 2 : « non calculé » si un intervalle décisif n'est pas lu (avant « sans objet ») ; aussi si un E_sf est non calculable | appliquée | inchangée | `test_audit_declencheur_2_E_sf_non_calculable_intervalles_decisifs_lus`, `test_audit_explication_trop_propre_construit_et_sain`, `test_garde_9_cle_absente_et_entree_en_echec` |
| 2. Déclencheur 3 : « non calculé » si la part n'est pas calculée (E0 = 0 ou part en échec) | **en partie** : E0 = 0 et M5 non calculée ; une part en échec (garde 15) était lue | **appliquée** (changement 6) | `test_audit_part_hors_bornes_construit_et_sain`, `test_garde_15_degenerescences_de_la_part` |
| 3. `ampleur_non_resolue` « non lu » si E_sf ou D n'est pas lu ; `reserve_B1_non_lue` dans la même union | appliquée | inchangée | `test_table_des_cas_de_B1`, `test_VB2_02_E_sf_ou_D_non_calculable_reserve_non_lue` |
| 4. E0 = 0 : part « non calculable » (motif écrit) ; D et ses réserves lus | appliquée | inchangée | `test_garde_15_degenerescences_de_la_part` |
| 5. Garde 4 : commit du manifeste = tête vérifiée, égalité stricte | appliquée | inchangée | `test_garde_4_commit_du_manifeste_different_de_la_tete` |
| 6. Garde 5 : critère lexical d'unicité de [PA], garde 16 | appliquée | inchangée | `test_garde_5_second_passage_et_manifeste_illisible`, `test_garde_3_lecture_decisive_rattachement_et_unicite` |
| 7. Sondes principales de [L] = celles de [SF], sinon arrêt (garde 9) | appliquée | inchangée | `test_artefacts_des_raise_jamais_declenches[garde9-principales-autre-ordre]` |
| 8. `issue_primaire` recopiée et vérifiée (garde 8) ; instantané de [L] ; [L] modifiée pendant l'analyse : arrêt | appliquée | inchangée | `test_lecture_modifiee_pendant_l_analyse`, `test_garde_14_verrou`, `test_garde_8_issue_et_etats` |
| 9. `GardeArret` dans une analyse : « échec », contrôle « non lu » ; toute autre exception : arrêt écrit dans `arret` | appliquée | inchangée | `test_garde_arret_dans_une_analyse_echec_et_non_lu`, `test_autre_exception_dans_une_analyse_arrete`, `test_autre_exception_dans_une_analyse_ecrite_dans_arret` |
| 10. Valeur non finie dans la sortie : arrêt avec son chemin, jamais `None` | appliquée | inchangée | `test_sortie_valeur_non_finie_et_type_inconnu` |

## Écarts au brouillon 4

**Aucun.**

Lectures d'application gardées, là où le brouillon 4 se tait (aucune ne change un nombre, une réserve ni le verrou) :

1. Garde 7, P3-P3/<p> en échec dans [L] : aire et quantile du plancher non comparés (« non comparé (entrée en échec) ») ;
   « même état » n'est écrit que pour P3-P1, P3-P2 et la mention, et l'état d'un jeu ne se recalcule pas sans tirage.
2. Garde 7, état « en échec » recalculé : le seul que le code gelé peut écrire sous les constantes de la garde 10 (tâches
   différentes entre les deux conditions) ; tout autre motif d'échec dans [L] arrête (motif différent).
3. Déclencheur 2 : un E_sf « en échec » (et pas seulement « non calculable ») rend aussi « non calculé » : il n'a pas de
   bornes. Cas sans exemple quand les trois intervalles décisifs sont lus.
4. Garde 13 : une entrée P3-P3/<p> en échec n'est pas contrôlée (garde 9 : « non lu », sans arrêt).
5. Garde 11 : les paramètres de tirage sont contrôlés au point d'entrée en ligne de commande (`_main`).
6. Recommandation au verdict : une liste d'entrées {conclusion, réserve, lecture} pour les conclusions établies visées
   par un contrôle lu ; la ligne de l'audit porte aussi `consigne` (changement 5).
7. Libellé de D nul : « D = 0 : retirer les actions à forme ne change pas la différence » (descriptif).

Observation, sans changement : l'audit de symétrie est « gelé et toujours calculé » ; sur un run synthétique « organisme
non établi » (run « aucun_signal » des tests), E0 ≈ 0 et le déclencheur 3 peut être vrai : la recommandation ne porte
alors que la ligne de l'audit. Conforme au texte ; sans objet dans ce run (P3-P1 établie, borne basse décisive 1,2464).

## Contrôle sur les survivants

1. **Rejeu des reproductions de la revue** : `revue-mutants/pannes/test_reproductions_survivants.py` (`2f6e3892…`),
   24 tests, sur la copie de base et les mutants d'origine (module d'origine), depuis la racine du dépôt, sous la garde
   R1 de la revue, `--basetemp` et `TMPDIR` sous `module-v2/tmp/` : **24 passed in 44.46s** (chaque fois, base ≠
   mutant : les survivants sont toujours séparables) ; 0 refus ; rien d'écrit dans `revue-mutants/`
   (`journaux/pytest-reproductions-rejeu.log`, `journaux/r1-reproductions.jsonl`). `test_pannes_revue.py` n'a pas été
   relancé (ses tests P1, P2 et P5 écrivent dans `revue-mutants/pannes/`) ; son recalcul indépendant est repris, écrit à
   la main d'après le texte, dans `test_bornes_recalculees_hors_du_module`.
2. **Portage sur le module v2** (`controle-survivants/controle_survivants_v2.py`) : les remplacements de la campagne
   (`revue-mutants/mutants_revue.py`, lu comme texte, jamais importé) appliqués au module v2, chaque motif présent
   exactement une fois (107 sur 107) ; F23 adapté, parce que le code de la garde 7 a changé (une [L] « non calculable » ou
   « en échec » acceptée quel que soit l'état recalculé) ; dix mutants nouveaux (N01 à N10) pour les règles du brouillon 4.
   Pour chacun : la suite v2 entière, arrêtée au premier échec, depuis la racine du dépôt, sous la garde R1. Versions
   éprouvées : module `dfdeef6b…`, tests `a5c6ec34…` (celles qui sont rendues).
3. **Résultat** (`controle-survivants/resultats-survivants-v2.jsonl`, une ligne par mutant ; `journaux/controle-mutants-v2.log`) :
   **117 mutants, 117 tués, 0 survivant** ; 0 refus R1 ; les 66 mutants que la suite d'origine tuait restent tués.

| mutant | règle mutée | état avec les tests v2 | premier test v2 en échec |
|---|---|---|---|
| A05 | phrase de lecture de P3-P1 donnée aux cibles P3-P4/<p> et T3/<p> | tué | `test_phrases_de_lecture_sur_des_nombres_donnes` |
| A06 | phrase de ampleur_portee_par_les_formes remplie avec E0 au lieu de D | tué | `test_phrases_de_lecture_sur_des_nombres_donnes` |
| A07 | phrase de au_dela_de_la_consigne remplie avec la borne haute | tué | `test_phrases_de_lecture_sur_des_nombres_donnes` |
| A08 | réserves sans union par couple (nom, cible) : une par motif | tué | `test_synthese_une_reserve_par_couple_motifs_joints` |
| A09 | phrase de B3 remplie avec A_80_écrit_min au lieu de A_80_écrit_max | tué | `test_recommandation_au_verdict_phrases_des_criteres` |
| E05 | nul/<p> établie sans la ligne « aucune sonde générique… » | tué | `test_verrou_table_des_conclusions_chaque_condition_des_deux_cotes` |
| E06 | P3-P4/<p> établie sans la ligne « critères 2 et 3… » | tué | `test_verrou_table_des_conclusions_chaque_condition_des_deux_cotes` |
| E07 | P3-P3/<p> établie même sur la ligne « lecture de P3-P3 en échec » | tué | `test_verrou_table_des_conclusions_chaque_condition_des_deux_cotes` |
| E10 | T<k>/<p> établi sans son drapeau etabli | tué | `test_verrou_table_des_conclusions_chaque_condition_des_deux_cotes` |
| E11 (équivalent selon la revue) | nul/<p> établie sans l'état « non au-dessus » (ligne seule) | tué | `test_verrou_table_des_conclusions_chaque_condition_des_deux_cotes` |
| F02 | garde 7 : tâches, exclues, illisibles et nuls non comparés | tué | `test_garde_7_artefacts_des_comptes_et_du_plancher` |
| F03 | garde 7 : nombre d'actions par condition non comparé | tué | `test_garde_7_artefacts_des_comptes_et_du_plancher` |
| F04 (équivalent selon la revue) | garde 9 : sondes principales de [L] non recoupées avec [SF] | tué | `test_artefacts_des_raise_jamais_declenches[garde9-principales-autre-ordre]` |
| F05 | lancement : gardes 7, 8 et 10 retirées d'avant le manifeste (refaites après) | tué | `test_lancement_gardes_avant_le_manifeste_rien_ecrit[exiger_coherence]` |
| F06 | lancement : garde 13 retirée d'avant le manifeste (refaite après) | tué | `test_lancement_gardes_avant_le_manifeste_rien_ecrit[exiger_entrees_b3]` |
| F07 | lancement : arbre de travail sale autorisé | tué | `test_lancement_arbre_de_travail_sale_rien_ecrit` |
| F08 | « échec » pour toute exception (pas seulement GardeArret) | tué | `test_autre_exception_dans_une_analyse_arrete[ValueError]` |
| F09 | valeur non finie de la sortie remplacée par None (repli silencieux) | tué | `test_sortie_valeur_non_finie_et_type_inconnu` |
| F13 (équivalent selon la revue) | garde 9 : type de taches_exclues non contrôlé | tué | `test_artefacts_des_raise_jamais_declenches[garde9-taches_exclues-type]` |
| F19 | garde 15 : ≥ 1 % au lieu de > 1 % | tué | `test_bords_de_la_garde_15_un_pour_cent` |
| F22 | garde « lecture décisive modifiée pendant l'addendum 2 » retirée | tué | `test_lecture_modifiee_pendant_l_analyse` |
| F23 (adapté) | garde 7 : [L] « non calculable » (ou « en échec ») accepté quel que soit l'état recalculé | tué | `test_garde_7_etat_ou_motif_differents_de_la_lecture` |
| F24 (équivalent selon la revue) | garde 3 : empreinte de [P] dans le manifeste de lecture non comparée | tué | `test_garde_3_manifeste_de_lecture_forge_chaque_condition` |
| G01 | intervalles propres (M5, M6, M8) à 90 % au lieu de 95 % (q non divisé par 2) | tué | `test_bornes_recalculees_hors_du_module[sain-10000]` |
| G03 | matrice de tirage de M5, M6, M8 à TIRAGES / 2 lignes | tué | `test_bornes_recalculees_hors_du_module[sain-10000]` |
| G10 | classement descriptif contre 0,48 au lieu de log10 3 | tué | `test_classement_descriptif_contre_log10_3` |
| G11 | audit (2) : saboteur conforme si 0 ≤ bas (au lieu de 0 < bas) | tué | `test_bords_des_cas_conformes_du_declencheur_2` |
| G12 | audit (2) : témoin et mention conformes si bas < 0 < haut (bornes exclues) | tué | `test_bords_des_cas_conformes_du_declencheur_2` |
| G13 | M5 : mention « instable » si e_bas < 0 < e_haut (bornes exclues) | tué | `test_mention_instable_borne_basse_de_E0_egale_a_0` |
| H02 | _nombre accepte ±inf (gardes 9 et 13) | tué | `test_garde_13_entrees_de_B3` |
| H03 | sortie : ±inf laissé passer (NaN seul refusé) | tué | `test_sortie_valeur_non_finie_et_type_inconnu` |
| I01 | générateur fixe (graine 0) au lieu de manifeste.generateur(graines[clé]) | tué | `test_bornes_recalculees_hors_du_module[sain-10000]` |
| I06 | M5 : E0 tiré sur une autre matrice que D (lignes non partagées) | tué | `test_bornes_recalculees_hors_du_module[sain-10000]` |
| I09 | M8 : générateur consommé deux fois (un tirage jeté avant celui qui sert) | tué | `test_bornes_recalculees_hors_du_module[sain-10000]` |
| I10 | M6 : médianes des lignes tirées sur une matrice de graine fixe | tué | `test_bornes_recalculees_hors_du_module[sain-11]` |
| J01 | E_-f retire toutes les formes au lieu de la seule forme f | tué | `test_bornes_recalculees_hors_du_module[sain-10000]` |
| J02 | M7 : T_propres ne regarde que les formes de la condition a | tué | `test_bornes_recalculees_hors_du_module[sain-10000]` |
| J03 | M8 : f comparée aux actions sans f (et non sans aucune forme) | tué | `test_bornes_recalculees_hors_du_module[sain-10000]` |
| J04 | M6 : médiane sur T_sf au lieu des tâches de l'effet décisif | tué | `test_bornes_recalculees_hors_du_module[degenere-10000]` |
| J06 | garde 7 : aire sur toutes les actions (notées ou non) | tué | `test_garde_7_actions_non_notees_passe` |
| K04 | audit (2) : cas « E_sf non calculable » retiré | tué | `test_audit_declencheur_2_E_sf_non_calculable_intervalles_decisifs_lus` |
| N01 | garde 7 : état de [L] non comparé (seuls les nombres d'une entrée calculable) | tué | `test_garde_7_etat_ou_motif_differents_de_la_lecture` |
| N02 | garde 7 : motif de [L] non comparé | tué | `test_garde_7_etat_ou_motif_differents_de_la_lecture` |
| N03 | garde 7 : entrée « en échec » de [L] acceptée sans comparaison (règle du brouillon 2) | tué | `test_garde_7_etat_ou_motif_differents_de_la_lecture` |
| N04 | audit (3) : part en échec (garde 15) non rendue « non calculé » (précision d'application 2 retirée) | tué | `test_garde_15_degenerescences_de_la_part` |
| N05 | phrase de B3 sans « grandeur calculée avant le scellement, sur des nombres déjà lus (brainstorm) » | tué | `test_recommandation_au_verdict_phrases_des_criteres` |
| N06 | libellé de D de l'ancienne forme (« qui l'abaissent ») | tué | `test_classements_et_libelles_du_seuil` |
| N07 | phrase de lecture de l'audit jointe à la consigne « cité et soumis à Lazar » | tué | `test_audit_explication_trop_propre_construit_et_sain` |
| N08 | compte des 13 contrôles écrits non vérifié | tué | `test_artefacts_des_raise_jamais_declenches[invariant-13-ecrits]` |
| N09 | nombre de contrôles : ligne d'issue non rapportée | tué | `test_organisme_non_etabli_B1_B2_sans_objet_aucune_reserve` |
| N10 | audit (1) : règles dans les deux sens au vocabulaire ancien | tué | `test_B1_et_B2_passent_par_la_meme_fonction` |

**Survivants restants : aucun.** Les quatre équivalents de la revue sont tués, mais par des entrées que le code gelé ne
produit pas sur le run réel : E11 par une lecture lue construite (état « non interprétable » sur la ligne « aucune sonde
générique… ») ; F13 par une [L] dont `taches_exclues` n'est pas une liste, lue par la seule garde 9 (sur la fonction pure,
la garde 7 l'arrête avant) ; F04 par une [L] aux sondes principales dans l'autre ordre ; F24 par un manifeste de lecture
forgé dans un dépôt jouet (sur le run réel, la garde 2 épingle déjà l'empreinte de [ML]). Ils restent équivalents pour le
run réel ; les tests qui les tuent éprouvent des conditions écrites du texte (table du verrou, garde 9, garde 3).

## Durée mesurée

Dépôt git jouet de taille réelle, construit sous `module-v2/tmp/` puis supprimé (`mesure-duree/mesure_duree_v2.py`) :
60 tâches, 4 conditions, 10 pas, 600 actions par condition, 430 sondes (2 principales, 214 sondes de plancher chacune),
formes et coûts plantés ; code de `src/` copié, préenregistrement de P3, run source décisif scellé, lecture décisive par le
code gelé (tirages des aires réduits pour cette seule construction), commit de N-025, module v2 aux constantes du run
jouet, tests v2, texte de l'addendum 2 scellé (S2). La vraie commande, dans un processus séparé, aux paramètres du texte
(10 000 tirages), sur deux copies du dépôt, en deux séries ; machine au repos pour la seconde (après la campagne de
mutants). Machine : x86_64, 4 cœurs, Python 3.11.17, numpy 2.4.6.

| série | ligne de commande complète | imports seuls | fonction pure seule | mémoire maximale |
|---|---|---|---|---|
| 1 | 6,49 s ; 5,53 s | 4,8 s | 0,64 s | ≈ 683 Mo |
| 2 (`mesure-duree/mesure-duree-v2.json`) | 5,71 s ; 5,33 s | 4,74 s | 0,43 s | ≈ 683 Mo |

Chaque passage a réussi : sortie scellée, 10 000 tirages, 13 contrôles écrits, 9 lus (ligne « aucune sonde générique… »).

Phrase proposée pour `<<DUREE_MESUREE>>` : « environ 5,5 s pour la ligne de commande complète (de 5,3 à 6,5 s sur quatre
mesures ; processus séparé, dépôt jouet à taille réelle : 60 tâches, 4 conditions, 10 pas, 600 actions par condition,
430 sondes ; 10 000 tirages), dont environ 4,8 s d'imports et 0,4 à 0,6 s pour la fonction pure ; mémoire maximale
≈ 683 Mo ».

## Empreintes et fichiers

Chaque fichier de `module-v2/` a son compagnon `<nom>.sha256` (« <empreinte>  <nom> », vérifiable par `sha256sum -c`
depuis son dossier). Celui de ces notes est dans `NOTES-MODULE-v2.md.sha256`.

| fichier (sous `module-v2/`) | rôle | sha256 |
|---|---|---|
| `audit_verdict_p3_v1.py` | **module** | `dfdeef6b4652a9faad06cecd708385341f044ec4164efade1f82a4a1cf6e7a3d` |
| `test_audit_verdict_p3_v1.py` | **tests (118)** | `a5c6ec3412c04a1e7e3af8bb1ebb168c22a3aab40b7111821d24558523dc92fd` |
| `controle-survivants/controle_survivants_v2.py` | portage des mutants et contrôle | `b94c2411c70ac563ba89950a5a8a6a8b5b2b8dfe8eec7ccec1af41b1760f350e` |
| `controle-survivants/resultats-survivants-v2.jsonl` | 117 résultats | `3693f48f493d56c0e9943dd82bb36274156e0f6d24ee0131863523a8f8c9f36f` |
| `mesure-duree/mesure_duree_v2.py` | mesure de durée | `282ef3766eb3c212647473c924237a4c1620c66704bedf50fe38076d5de90a13` |
| `mesure-duree/mesure-duree-v2.json` | seconde série | `f035bb49e028d41a207cf16ddd089cbc17f0d7b673d74946e2b253a3a2b9c467` |
| `journaux/pytest-suite-v2.log` | suite, commande de la consigne | `6d946909713654faebefd70162e151e3997a41fb6f3c62c62791ec98db449929` |
| `journaux/pytest-suite-v2-garde-r1.log` | suite sous la garde R1 | `1bf2b7e1b71156ea192b213402a9c3e47aefba5a8a1c43d534182e01602df79e` |
| `journaux/r1-suite-v2.jsonl` | journal de la garde R1 (suite) | `3226f6e15015cad37b31642739282663ed85c834e557d96f014509e49522265f` |
| `journaux/pytest-reproductions-rejeu.log` | rejeu des reproductions | `4f9cba840127f395a7eb861c4d860eecbe8af47db3c7e781f49356c29bb02614` |
| `journaux/r1-reproductions.jsonl` | journal de la garde R1 (rejeu) | `52df75a5a3bbfb5de19878fdf29a5deb70a31364605018d6cb1fd95fbf69521f` |
| `journaux/controle-mutants-v2.log` | journal du contrôle | `582717482a9a696486450bd7ecb31881794251d7484aed955df2172d8868b866` |
| `journaux/git-status-avant.txt`, `…-avant-suite.txt`, `…-apres.txt` | état git (vides) | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `journaux/empreintes-dossier-avant.txt`, `…-apres.txt` | dossier de travail hors de `module-v2/` (581 fichiers) | `21107b4d925c0048580b02be97f6a3baa5d956d86217624509343a1352776002` (les deux) |

