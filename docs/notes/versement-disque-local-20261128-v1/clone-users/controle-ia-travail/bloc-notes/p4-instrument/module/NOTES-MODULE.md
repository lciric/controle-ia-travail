# Notes du module de P4-instrument (v1)

Rédacteur du module, sous-agent neuf, 2026-10-20. Sources :
- le brouillon 4, `…/p4-instrument/P4-instrument-v1-brouillon4.md`
  (`32d821fb42e54341f2649637085de18e2b6b9758b51dc38c504f702ba393ead6`), qui prime sur le brouillon 3 et sur le plan v1 ;
- la décision de conception de la session après les mesures de conception (R-284), que le candidat écrira (section
  « Décision de conception portée »).

Lus pour le contexte : le plan v2 (`7c65e4f6…`) et le traitement de la contre-lecture 2. Non lus :
`prereg/P3-consignes-v1.md`, le contenu des textes d'action, aucune clé. Le préfixe `…/` vaut
`/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad`.

Le code gelé de P3 est importé, jamais modifié. Aucune grandeur de P3 ni de P4 n'a été calculée sur des données réelles.
Seule donnée réelle lue : la sortie scellée de MC-2, qui contient des identifiants de tâches et des empreintes, aucun texte
d'action. Tests et essais : modèle jouet et tables synthétiques. Le dépôt n'a été que lu : `git status --porcelain` est
identique avant et après la suite, et aucun `__pycache__` ni `.pyc` neuf n'est apparu, ni dans le dépôt ni dans le
dossier du module.

## Décision de conception portée (message de la session, après MC-1 à MC-3)

Résultats des mesures :
- `docs/notes/P4-mesures-v1/mesures-conception-p4-v1.json` (`1454d0848c6a2655bbc7ee7f4a845a19b37e0b924e87674d96dfeecdae28a66b`) ;
- B = « a tall », B′ = « an urban » ;
- 38 épisodes sur 60 au niveau 1 ;
- 32 actions en échec de longueur, toutes hors du niveau 1.

Ce que le module applique :

1. **Lignes décisives.** C1, M6a et M6b, ainsi que les descriptives B contre H, concordance et rang, C1 au pas 0, Δ net
   et part des directions étalées, portent sur les actions des seuls épisodes au niveau 1 sur l'instance, dans les cinq
   bras. Les blocs sont leurs tâches. Fonctions : `lecture.taches_du_niveau_1`, `lecture._retenues`,
   `lecture.lignes_du_bras(…, jeu="niveau_1")`, qui est le défaut de toutes les lectures.
2. **Liste des épisodes du niveau 1.** C'est une constante du texte :
   - dans le module, `instrument.TACHES_NIVEAU_1` (38 tâches, dans l'ordre des tâches) ;
   - dans la configuration, la clé `taches_niveau_1`, qui en mode réel doit égaler la constante ;
   - en mode réel, le run la relit dans la sortie scellée de MC-2 (`instrument.MC_SORTIE`, chemin et empreinte ;
     `instrument.taches_niveau_1_de_mc`, `instrument.exiger_taches_niveau_1`). Une différence arrête le run (R11) ;
   - une tâche de la liste hors des tâches de P3 arrête aussi le run.

   L'ensemble des épisodes au niveau 1 sur l'instance est comparé à la liste (`instrument.comparer_niveau_1`). Le résultat
   est écrit dans `identite-p4.json` et dans le résumé (`niveau_1_texte`). Le run va à son terme. À la lecture, un
   ensemble différent (`lecture.controle_du_niveau_1`) donne la nouvelle ligne L4 : « reconstruction de l'instance autre
   que celle mesurée avant le scellement » / « non lu ; nœud », avec en motif les tâches en plus et les tâches absentes.
   C1, M6, les descriptives et le C1 étendu ne sont alors pas calculés ; M5 est lue.
3. **C1 étendu**, descriptif, jamais une ligne. Il porte sur les actions gardées par la garde d'identité : le niveau 1,
   plus les actions des autres épisodes qui passent (a), (b) et (c) si le niveau 2 est actif. Graine `d/c1-etendu`.
   Fonction : `lecture.lire_c1(…, jeu="etendu")`. Son compte d'exclusions est rapporté (`identite.c1_etendu`). L'ancien
   seuil (plus de 60 actions exclues) ne fait plus de ligne. Le niveau 2 et l'épreuve de la tolérance (c) sont gardés
   tels quels.
4. **Réserve inchangée.** « Scores de P3 non reproduits sur des jetons identiques » s'applique sur le niveau 1
   (`instrument._garde_identite`).
5. **Tokeniseur.** En mode réel, le `tokenizer.json` du modèle chargé, lu dans le cache à la révision citée, doit avoir
   l'empreinte `79e3e522…`. Sinon, ou s'il est introuvable, le run s'arrête (R11). Fonctions :
   `instrument.chemin_tokeniseur_du_modele`, `instrument.exiger_tokeniseur_du_modele`. Mes lectures 1 à 19 sont
   retenues : borne strictement inférieure à 10 USD partout ; épreuve (ii) avec les deux actions échangées en échec ;
   épreuve sans action comparable lue « contre l'attendu » ; aucun épisode au niveau 1 donne L4 plus la réserve
   « tolérance (c) non éprouvée ».
6. **Effectifs et puissance.** M5 est inchangé. C1 porte sur 38 blocs de 10 actions au plus (380 actions par bras). À
   corrélation intra-tâche égale, l'erreur type est multipliée par environ √(60/38) ≈ 1,257. Avec l'erreur type réalisée
   par P3 que cite le texte (≈ 0,0194), cela donne ≈ 0,0244. L'aire minimale détectable (95 %, puissance 80 %) devient
   ≈ plancher + 2,80 × 0,0244 ≈ plancher + 0,068, au lieu de + 0,054 : ≈ 0,64 à 0,66 pour des planchers de 0,572 à 0,596,
   et ≈ 0,87 pour un plancher de 0,80. Ce sont des ordres de grandeur dérivés des nombres du texte, non opposables.

## Section du texte → fonction qui l'applique

| section (brouillon 4 et décision R-284) | fonction |
|---|---|
| En-tête : entropie, révision, configuration citées | `instrument.exiger_citations_p4` (run) ; `lecture.exiger_lecture_sous_prereg_p4` (lecture) ; `instrument.exiger_revision_citee` |
| En-tête : lignes « Module de P4 : `chemin` : `empreinte` » | `instrument.lignes_module`, `instrument.exiger_module_cite`, `instrument.exiger_module_execute` ; contrôle avant dépense : `instrument_p4_v1.py --controle module` |
| En-tête : run source | `instrument.CONSTANTES_DU_TEXTE["run_source"]`, `instrument.chemins_du_run_source`, `instrument.exiger_chemins_du_run_source` |
| En-tête : GO et dépense | `instrument.controler_go` (GO cité, huit colonnes, plafond, échéance, borne < 10 USD, révocations), `instrument.borne_de_l_etape`, `instrument.rejouer_garde_de_calcul` ; `--controle go` |
| En-tête : accord du jour | `instrument.controler_accord` |
| Données lues (R11) | `instrument.EMPREINTES_P3`, `instrument._exiger_source`, `instrument.charger_sources_p3`, `instrument.charger_actions_p3` |
| Liste des épisodes du niveau 1 (R-284) | `instrument.TACHES_NIVEAU_1`, `instrument.MC_SORTIE`, `instrument.taches_niveau_1_de_mc`, `instrument.exiger_taches_niveau_1`, `instrument.comparer_niveau_1` ; `lecture.controle_du_niveau_1` |
| Tokeniseur du modèle (R-284) | `instrument.chemin_tokeniseur_du_modele`, `instrument.exiger_tokeniseur_du_modele` |
| Mesures de conception MC-1 à MC-3 | `mesures.mc1`, `mesures.mc2`, `mesures.mc3`, `mesures.mesurer`, `mesures.charger_tokeniseur`, `mesures.ecrire_sortie` |
| Métrique, bras I | `instrument.environnement_du_bras`, `instrument.ids_de_l_action`, `instrument.jeton_de_fin`, `instrument.reconstruire_episode`, `instrument.empreinte_trajectoire` |
| Métrique, bras D, H, B, B′ | `instrument.environnement_du_bras`, `instrument.exiger_bras_alignes`, `instrument.ajouts_par_pas`, `instrument.exiger_longueurs_egales` |
| Métrique, phrases | `instrument.CANDIDATES_B`, `instrument.CANDIDATES_BPRIME`, `instrument.exiger_phrases`, `instrument.premiere_phrase_qui_convient`, `instrument.longueur_seule` ; règle rejouée dans `instrument._executer_apres_manifeste` |
| Métrique, empan, score, maximum, scores par jeton | `instrument.noter_episode`, `instrument.exiger_agregation_maximum`, `instrument.sondes_entrainees_legeres` |
| Métrique, aire, intervalle, plancher | `lecture.detection_p4`, `lecture.plancher_de`, `lecture.etat_contre_le_plancher` |
| Métrique, M5 | `instrument.reconstruire_validation`, `instrument.generateur_de_p3`, `instrument.noter_validation`, `instrument.exiger_aires_validation` (`GardeM5`) ; `lecture.lire_m5` |
| Métrique, C1 (lignes du niveau 1) | `lecture.lire_c1`, `lecture.lignes_du_bras`, `lecture.jeu_apparie` |
| Métrique, M6a, M6b | `lecture.separation_par_blocs`, `lecture._separations_du_plancher`, `lecture.lire_m6a` ; `lecture.difference_aire_separation`, `lecture.lire_m6b` |
| Descriptives | `lecture.lire_m5` (enjeux), `lecture.lire_c1` (enjeux ; pas 0 ; étendu), `lecture.lire_b_contre_h`, `lecture.part_scores_egaux`, `lecture.concordance_appariee`, `lecture.delta_net`, `lecture.part_directions_etalees`, comptes de `lecture.lire` (huit comparaisons) |
| Seuil | `lecture.etat_contre_le_plancher`, `lecture.est_plancher_haut`, `lecture.issue_p4`, `lecture.audit_r4`, `instrument.critere_c` |
| Plan d'analyse, point 1 | `instrument.executer`, `instrument._executer_apres_manifeste`, `instrument.exiger_instrument_fige`, `instrument._echeance` |
| Plan d'analyse, point 2 | `lecture.analyser`, `lecture.exiger_verdict_complete_p3`, `lecture.exiger_lecture_sous_prereg_p4`, `lecture.charger_source_p4`, `lecture.lire` |
| Plan d'analyse, points 3, 7 et 8 | `lecture.issue_p4(…, reserves_heritees)` ; `instrument.borne_de_l_etape` ; `lecture.CLES_LECTURE` (neuf clés), `instrument.CLES_RUN`, `instrument.generateur_de_p3` |
| Garde d'identité, niveaux 1 et 2, épreuve | `instrument._garde_identite`, `instrument.criteres_niveau_2`, `instrument.critere_c`, `instrument._epreuve`, `instrument.position_de_l_espace`, `instrument.decalage_d_un_identifiant`, `instrument.epreuve_conforme` |
| Audit R4 | `lecture.audit_r4`, `lecture.rang_du_maximum`, `lecture.aires_de_construction` (sur les lignes du niveau 1) |
| Critères de lecture gelés | `lecture.LIGNES`, `lecture.issue_p4` |
| Liste d'arrêt | gardes ci-dessus ; résumé avec motif : `instrument.executer` ; lecture en échec écrite : `lecture.descriptif` |

## Écarts au texte

Aucun, si le candidat écrit la décision R-284 telle que portée ici. Le candidat doit écrire, ou l'on aligne le module :
- les cellules de L4 : « reconstruction de l'instance autre que celle mesurée avant le scellement » / « non lu ; nœud » ;
- la clé de graine `d/c1-etendu` au point 8 ;
- le nombre de comparaisons contre un plancher : huit, C1 étendu compris (le brouillon 4 en compte sept) ;
- la liste des 38 tâches, égale à `TACHES_NIVEAU_1`. Le module ne lit pas cette liste dans la prose du texte : il la
  relit dans la sortie scellée de MC-2. Si la session fixe une forme exacte de ligne, je peux ajouter la lecture.

## Silences et contradictions (lectures retenues par la session, plus les neuves)

1. Borne de l'étape strictement inférieure à 10 USD (l'en-tête et la liste d'arrêt divergeaient à 10 USD).
2. Épreuve (ii) : les deux actions échangées doivent échouer à (c).
3. Une épreuve sans action comparable se lit « contre l'attendu ».
4. Aucun épisode au niveau 1 : L4 (sens neuf), plus la réserve « tolérance (c) non éprouvée ».
5. Ancre de l'épreuve (i) sur le jouet : identifiant 4 après l'identifiant 99. En mode réel, 220 et 271 sont exigés, et
   `<|end_header_id|>` est contrôlé.
6. Tokeniseur : empreinte exigée sur l'instance, dans le cache, à la révision citée (point 5 ci-dessus).
7. État « au-dessous » de M6a : calculé par la même règle, sans effet sur une ligne.
8. B contre H : intervalle et état sur l'aire ; séparation et plancher replié rapportés.
9. Audit R4, « M5, C1, M6a » : M5 et C1 de tromperie, et M6a, sur les lignes du niveau 1.
10. L1, « données » : la récupération. Un refus avant le manifeste du run donne L1 (« manifeste absent »).
11. Si plusieurs lignes R-… annoncent le verdict complété, toutes doivent citer l'empreinte du sceau.
12. Révocation : seules les formes écrites bloquent.
13. Accord : la forme lue est « message de Lazar dans la session » ; tout GO échu est refusé.
14. Plafond de la phase : vérifié par la session à l'accord ; aucun code ne le relit.
15. Réserves héritées de P3 : un pointeur, et un paramètre de `issue_p4`.
16. Préenregistrement non scellé à la lecture : refus sans écriture.
17. Configuration : `taches_niveau_1` est ajoutée ; `part_exclusion_max` est retirée (le seuil ne fait plus de ligne). Les
    autres clés ont toutes une valeur écrite au texte. Configuration réelle : `config_de_reference(« … a tall … »,
    « … an urban … »)`.
18. MC : le nœud « plus de 10 % » se comptait sur toutes les actions.
19. Lanceur, contrôle à cinq minutes et surveillance : hors des six fichiers.
20. Neuf. Une liste différente quand M5 est déjà en défaut : L3 prime (ordre de la table). C1 et M6 restent non calculés
    (« rapportés s'ils sont calculés »).
21. Neuf. C1 étendu quand le niveau 2 est désactivé : seules restent les lignes du niveau 1 ; les autres actions sont
    comptées comme exclues, motif « niveau 2 désactivé ».
22. Neuf. Rang du maximum (audit R4) : sur les lignes du niveau 1 de chaque bras, bras I compris.
23. Neuf. La sortie de MC a été produite par `mesures_conception_p4_v1.py` `483b8ac3…`, inchangé ici, avec
    `instrument_p4_v1.py` à `90b9ae8b…` (empreintes écrites dans la sortie). L'instrument a changé depuis, mais aucune
    des fonctions qu'appelle MC n'a changé. Pour une traçabilité stricte, la session peut relancer MC avec le module final,
    sous un nom neuf (R12).
24. Fait vérifié en lecture seule : aux commits `2af59b0` et `d023616`, l'arbre gelé est égal à celui de `7a54d43`.

## Tests

- Nombre de tests : `test_instrument_p4_v1.py` 71, `test_lecture_p4_v1.py` 42, `test_gardes_p4_v1.py` 81. Chaque fichier
  écrit son nombre en tête et le vérifie par un test.
- Commande (depuis la racine du dépôt) :
  `PYTHONPATH=src <python> -B -m pytest -q -p no:cacheprovider <module>/test_instrument_p4_v1.py <module>/test_lecture_p4_v1.py <module>/test_gardes_p4_v1.py`
- Dernière ligne : `194 passed in 120.07s (0:02:00)`.
- Neufs (R-284), chaque fois cas sain et artefact :
  - liste du niveau 1 relue dans la sortie scellée de MC-2. Sain : la vraie sortie, lue seulement. Artefacts : empreinte
    autre, sortie non scellée, liste autre, configuration autre ;
  - liste autre sur l'instance : le run va à son terme et écrit le constat, puis la lecture écrit L4 (jouet). Cas
    synthétiques : épisodes en moins, épisode en plus, aucun épisode au niveau 1 (avec la réserve) ;
  - C1 sur les seules lignes du niveau 1, recalculé à la main (aire 3/4 sur deux blocs ; C1 étendu 3/16 sur quatre
    blocs) ;
  - C1 étendu jamais une ligne (L11 avec un C1 étendu au-dessus ; L6 avec un C1 étendu non au-dessus ; issue identique
    sans le C1 étendu) ;
  - exclusions du niveau 2 jamais une ligne ;
  - tokeniseur du modèle à l'empreinte écrite, ou introuvable ;
  - tâche de la liste hors des tâches de P3.
- Liste « Tests (R5) » du brouillon 4 : couverte comme avant (voir les en-têtes des trois fichiers de tests).

## Durées sur le jouet (processeur)

- Run jouet de P3 (code gelé) : 18,6 s.
- Run jouet de P4 : 2,7 s.
- Lecture : 0,6 s.
- Suite du module : 120,1 s.

## Mesures de conception

Elles ont été lancées par la session avec la commande ci-dessous, déjà faite. Le fichier `mesures_conception_p4_v1.py`
n'a pas changé (`483b8ac3…`). Pour une relance, il faut une sortie de nom neuf (R12) :

```
cd /home/user/controle-ia-travail && PYTHONPATH=src /tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad/scellement-revalidation/venv-gpu-neuf/bin/python -B /tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p4-instrument/module/mesures_conception_p4_v1.py --run-source 20261019-230011-p3-reel --tokeniseur /tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p4-instrument/tokeniseur --sortie docs/notes/P4-mesures-v1/mesures-conception-p4-v1.json
```

## Empreintes (sha256)

Chaque fichier a son compagnon `.sha256`, au format « <empreinte>  <nom> ».

| fichier | sha256 |
|---|---|
| `mesures_conception_p4_v1.py` | `483b8ac3aca65a9879b7d2f2a832cfd5478c48fd860c94a6fbdc041364cc8be7` |
| `instrument_p4_v1.py` | `6e0e026eafba28e708fea009cc5c81c8b95defe6aa8f9fc2f76dd364ee29b06c` |
| `lecture_p4_v1.py` | `51a25e30a70b2439046e87037d6e2fcb26616289a017ef10689d66c0ca50e213` |
| `test_instrument_p4_v1.py` | `9d015be4ce2bbff4a4541387d5d19ef70497aa41f1a53b9c38724360d7a1dffd` |
| `test_lecture_p4_v1.py` | `49441971b81a89fe4b0dcc392efa7eba81234972d1d8e60abd4cececa33111d9` |
| `test_gardes_p4_v1.py` | `f4f97029f9a1fb9d9d1b29bac162334305a001b091319fde250e188071e092f5` |
