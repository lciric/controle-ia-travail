# Lecture du lot T0.5 à graines neuves — v1

Date : 2026-11-02 02:06 UTC. Préenregistrement : `prereg/preenregistrement-lecture-t05-graines-neuves-v2.md` (sha256 93923d7132260c2fe7674417ec819b2a7011fa49ba3949482c3c355e9289443d). Calibrage : sha256 f59018fb047af289ba1f466430fa9c577d6a0b6d4843a51831b19bd3c197b22e. Code : sha256 91973f2582c4db08d86250594adec317bc6796095bfdd60d3119a8c21dde179d (script), 6bcec082991bd8a4d55d195adb0e7b35f4e5dec00f85330e70863da96f4b4569 (juge).

## Issue : I1

juge valide et denté ; aucune loi réelle promue : borne I*(N) par moniteur.

## Épreuve

Épisodes retenus : 288 (96 tâches) ; exclus sans jetons : 0 ; exclus sans notation : 0. Instances jugées par moniteur réel : 3B:BALANCE 128, 3B:COHERENCE 262, 3B:NOVELTY 236, 3B:REDUNDANCY_PENALTY 234, 3B:RESULT_REASONING 121, 3B:RIGOR 217, 8B:BALANCE 173, 8B:COHERENCE 194, 8B:IRRELEVANCE_PENALTY 215, 8B:NOVELTY 176, 8B:REDUNDANCY_PENALTY 210, 8B:RESULT_REASONING 174, 8B:RIGOR 180.

## Lectures

- **L1** (décisive) tenu : témoins faux promus (e-BH) R-gele : aucun; R-plein : aucun; T-gele : aucun; T-plein : aucun.
- **L3′ réel** : dents non mesurées (0 promus sur 0 jugés).
- **L3′ planté** (décisive, monde informé, plan plein) : 3/3 promus (fraction 1,00) ; par force : 0.3 → oui, 0.5 → oui, 0.8 → oui ; rééchantillonnage par tâche (1000 répliques) : moyenne 0,93, intervalle à 95 % [0,67 ; 1,00].
  Prédiction conditionnelle aux paires tirées : attendus plein 2,30, gelé 2,05 ; P(fraction ≥ 2/3) = 1,00 ; P(I4) = 0,0000.
- **Dents** : T-gele : dents, T-plein : dents, reels_seuls : dents non mesurées.
- **L4′ comparaison** (lue) : témoins plantés promus, plein 3, gelé 2 ; gain du plan plein : 1 ; différence rééchantillonnée : moyenne 0,42, intervalle [0 ; 1] ; lois réelles promues, plein aucune, gelé aucune.
- **LR** (lois réelles, monde aveugle, plan plein) : aucune loi réelle promue : borne I*(N) par moniteur.

| moniteur (loi connue) | N jugé | log W max | promue | borne I*(N) (nat/épisode ; force) |
|---|---|---|---|---|
| LR-3B-BALANCE | 128 | -0,04 | non | 0,115 ; 0,74 |
| LR-3B-COHERENCE | 262 | -0,26 | non | 0,057 ; 0,48 |
| LR-3B-NOVELTY | 236 | -2,49 | non | 0,060 ; 0,50 |
| LR-3B-REDUNDANCY_PENALTY | 234 | -0,27 | non | 0,060 ; 0,50 |
| LR-3B-RESULT_REASONING | 121 | -1,18 | non | 0,117 ; 0,75 |
| LR-3B-RIGOR | 217 | -0,12 | non | 0,072 ; 0,55 |
| LR-8B-BALANCE | 173 | -0,17 | non | 0,094 ; 0,65 |
| LR-8B-COHERENCE | 194 | -0,69 | non | 0,083 ; 0,60 |
| LR-8B-IRRELEVANCE_PENALTY | 215 | -0,03 | non | 0,073 ; 0,56 |
| LR-8B-NOVELTY | 176 | -2,17 | non | 0,092 ; 0,64 |
| LR-8B-REDUNDANCY_PENALTY | 210 | 1,00 | non | 0,076 ; 0,57 |
| LR-8B-RESULT_REASONING | 174 | 0,34 | non | 0,093 ; 0,65 |
| LR-8B-RIGOR | 180 | 0,57 | non | 0,088 ; 0,62 |

## Témoins de la famille T (monde informé)

| fiche | vérité | log W max plein | e-BH plein | log W max gelé | e-BH gelé | N plan plein / gelé |
|---|---|---|---|---|---|---|
| T-3B-BALA-bruit-faux | fausse | -0,05 | non | -0,05 | non | 128 / 120 |
| T-3B-COHE-bruit-faux | fausse | -1,60 | non | -1,60 | non | 262 / 120 |
| T-3B-NOVE-bruit-faux | fausse | -0,17 | non | -0,17 | non | 236 / 120 |
| T-3B-REDU-bruit-faux | fausse | -0,04 | non | -0,04 | non | 234 / 120 |
| T-3B-RESU-bruit-faux | fausse | -0,06 | non | -0,06 | non | 121 / 120 |
| T-3B-RIGO-bruit-faux | fausse | -0,06 | non | -0,06 | non | 217 / 120 |
| T-8B-BALA-bruit-faux | fausse | -2,25 | non | -2,25 | non | 173 / 120 |
| T-8B-COHE-bruit-faux | fausse | -3,31 | non | -3,31 | non | 194 / 120 |
| T-8B-IRRE-bruit-faux | fausse | 0,57 | non | -0,02 | non | 215 / 120 |
| T-8B-NOVE-bruit-faux | fausse | -0,49 | non | -0,49 | non | 176 / 120 |
| T-8B-REDU-bruit-faux | fausse | -2,41 | non | -2,41 | non | 210 / 120 |
| T-8B-RESU-bruit-faux | fausse | -1,78 | non | -1,78 | non | 174 / 120 |
| T-8B-RIGO-bruit-faux | fausse | -1,15 | non | -1,15 | non | 180 / 120 |
| TFN01 | fausse | -0,05 | non | -0,05 | non | 288 / 120 |
| TFN02 | fausse | -3,49 | non | -3,49 | non | 288 / 120 |
| TFN03 | fausse | -2,62 | non | -2,62 | non | 288 / 120 |
| TFP01 | fausse | -0,46 | non | -0,46 | non | 288 / 120 |
| TFP02 | fausse | -3,17 | non | -3,17 | non | 288 / 120 |
| TFP03 | fausse | -4,78 | non | -4,78 | non | 288 / 120 |
| TVP01 | vraie | 8,50 | oui | 5,66 | non | 288 / 120 |
| TVP02 | vraie | 26,60 | oui | 17,81 | oui | 288 / 120 |
| TVP03 | vraie | 29,31 | oui | 21,48 | oui | 288 / 120 |

## Prédictions

- **P1_L1_tenu** : prédit True, observé True → tenu.
- **P2_aucun_temoin_vrai_reel** : prédit 0, observé 0 → tenu.
- **P3_plantes_plein_au_moins_deux_tiers** : prédit >= 2/3, observé 1.0 → tenu.
- **P4_gain_du_plan_plein_lu** : prédit gain attendu 0.586 témoin (lu, sans seuil ; signe garanti par l'invariant), observé 1 → lu.
- **P5_aucune_loi_reelle_promue** : prédit 0 (plein et gelé), observé {'gele': 0, 'plein': 0} → tenu.
- **Invariant du préfixe** : tenu.

## Exposition

configurations : 4; fiches_jugees : {'R': 26, 'T': 22}; lectures_de_l_epreuve : 1; repliques_de_reechantillonnage : 1000; taches_d_epreuve : 96; verdicts_montres_a_un_proposeur_avant_la_lecture : 0.

## Audit R4

Aucun déclencheur.

Seuils : par fiche log(1/α) = 2,996 (lu) ; e-BH famille T, m = 19 : log(m/α) = 5,940 ; famille R, m = 26 : 6,254 (décisifs).
