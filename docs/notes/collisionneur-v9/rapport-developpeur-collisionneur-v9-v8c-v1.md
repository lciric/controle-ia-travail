# Rapport du développeur : collisionneur v9 version 8c, v1

21 novembre 2026, vers 20:08Z (`date -u`). Développeur : Claude Opus 5.5 (`claude-opus-5-5`). Pièces d'instrument (classe B), à vérifier par Fable. Base : la v8b (`6cd0209c…`) et la garde v2 (`9d39a749…`), toutes deux laissées intactes (sceaux tenus). Corrections faites selon la décision de la mère sur les réserves du rapport de la v8b (`87f845f2…`). Aucun envoi réel, aucune clé lue ni écrite, aucun commit.

## Verdict

**Les deux décisions de la mère sont portées. Les six essais de reprise et de rejugement passent maintenant sur la vraie table** : la doublure qui prenait Carbon à 4,2 est retirée. La reprise des quatre dossiers passe le tour III.3 de Carbon.

## Corrections

| décision | dans la v8c et la garde v3 | essais |
|---|---|---|
| **(1) K-2, rapport par espèce** | `src/controle_ia/garde_google_v3.py` : la table `JETONS_PAR_MOT_MESURES` donne, pour chaque espèce, le plus haut rapport mesuré pour elle, arrondi au dixième supérieur. Les mesures sont écrites dans le module (`MESURES_JETONS_PAR_MOT`) | `tests/test_garde_google_v3.py::test_v2_rapport_mesure_par_espece` (la table est déduite des mesures), `::test_limite_de_mots_bord` (Carbon : 3 900 mots acceptés, 3 901 refusés) ; `test_v8_garde_reglages_sain_pour_le_catalogue`, `…_limite_de_mots`, `…_mots_des_tours_compatibles` ; `test_v8b_k2_carbon_refuse_au_tour_iii3_sous_5_1` (réécrit : 3 500 mots passent, 4 000 refusés, rien n'est compté) |
| doublure retirée | `carbon_a_son_maximum_mesure` et ses six appels sont supprimés : `test_v3_reprise_declaree_…`, les deux `test_v7_rejugement_…`, les deux tests de copie des dossiers (v7 et v8), `test_v8_ligne_de_reprise_devis_…` | ils passent sur la vraie table |
| **(2) K-1 bis, relance identique** | Quand le plafond de relance égale le premier plafond, ce qui est le cas des trois espèces, la suite des essais devient : premier essai, puis **une relance identique** (même niveau, ou même budget en repli, et même plafond), puis le dernier recours déclaré. La relance identique est déclarée par une ligne propre (`relance_identique_declaree`), par la marque `identique: true` dans la correction de l'essai, et par « RELANCE IDENTIQUE DÉCLARÉE » à l'écran. La fonction `etape_de_relance` lit l'étape sur le journal (premier, identique ou finale). Une reprise part de l'étape suivante, et une relance identique ne bloque pas la cellule. Quand un plafond plus haut existe, la relance relève le plafond sans relance identique, comme dans la v8b | `test_v8c_relance_identique_declaree_puis_ok`, `…_reprise_apres_relance_identique_part_au_dernier_recours`, `…_plafond_releve_sans_relance_identique`, `…_etape_de_relance` ; les essais accordés (trois envois avant le code 9 : `test_v5_max_tokens_…`, `test_v6_defaut_…`, `test_v7_…`, `test_v8_relance_…`, `test_k1_dernier_recours_…`, `test_a2_repli_relance_…`) |
| lieu des déclarations | La relance identique et le dernier recours sont déclarés **après les gardes de dépense** (plafond, ligne) et juste avant l'envoi. Un envoi refusé par le plafond n'est pas déclaré, et la commande suivante ne déclare qu'une fois. C'est un écart au lieu du texte de Fable pour K-1, qui déclarait avant la garde des réglages | `test_v8c_reprise_apres_relance_identique_part_au_dernier_recours` (une seule déclaration de chaque) |

### Table du rapport de jetons par mot (source)

La source est le relevé de Fable, `verification-corrections-collisionneur-v9-v8-fable-v1.md` (`9cf6799f…`), section 4.2 : les jetons de texte par mot de la limite du tour, sur les 43 réponses réelles complètes des journaux versés (branche `runs/collisionneurs-reprise-minuit-v1`).

| espèce | réponses | minimum | médiane | maximum | rapport de la garde v3 |
|---|---|---|---|---|---|
| Argon | 22 | 1,78 | 3,47 | 5,06 | **5,1** |
| Carbon | 21 | 2,40 | 3,41 | 4,11 | **4,2** |
| Neon | 0 (jamais servi) | — | — | — | **5,1** : aucune mesure, je prends par prudence le plus haut mesuré toutes espèces confondues, à remplacer après l'essai réel |

Conséquences, avec 16 384 jetons de texte pour Carbon (65 536 − 49 152) :
- Carbon tient les tours de 3 500 mots (14 700 jetons).
- Carbon refuse le tour de 4 000 mots, qui demande 16 800 jetons : c'est l'E2-T1, étage II, hors de la reprise.
- Argon tient 3 500 mots en flux, à 65 536 (17 850 jetons pour 49 152 de texte).
- Argon les refuse en lot, à 32 768 (17 850 jetons pour 16 384 de texte).

## Essais

Lancés avec `PYTHONPATH=src`, sans clés, sur un `--basetemp` neuf.

| suite | résultat |
|---|---|
| `docs/notes/collisionneur-v9/test_collisionneur_v9_v8c.py` | **359 passés, 1 sauté** (la copie « dopamine », non désignée) |
| `tests/test_garde_google_v3.py` | **44 passés** |
| v8b et garde v2, intactes | 399 passés, 1 sauté |

Les copies des quatre dossiers ont été fabriquées depuis les journaux versés et lancées par les commandes de reprise. Elles passent sur la vraie table : `verifier` tient avant et après, la reprise envoie 5, 5, 10 et 1 cellules (percée, dérive v2, mathématiques, antériorité), et la même commande relancée n'envoie rien.

## Mutations

Chaque mutation est faite sur une copie, avec les deux suites entières et un arrêt au premier échec. Le témoin sans mutation passe : 400 passés, 3 sautés, 1 désélectionné. La série reprend les 52 mutations de la v8b, accordées à la v8c et à la garde v3, et en ajoute 9 sur K-1 bis et sur la table par espèce.

Outil : `/tmp/claude-0/-home-user-controle-ia-travail/2eb82089-3810-5ff8-881f-da5f24b622eb/scratchpad/dev-v8/outils/mutations_v8c.py`.

| n° | pièce mutée | mutation | premier essai en échec | prise |
|---|---|---|---|---|
| 2 | v8c | C-1 : un relevé refusé abandonne le lot | `test_v7_lot_sain_apres_coupure` | oui |
| 3 | v8c | remarque 4 : aucun dernier relevé avant l'annulation | `test_v7_lot_artefact_non_abouti_au_delai_annule_compte_au_pire` | oui |
| 4 | v8c | C-2 : relevé d'un lot échoué jeté | `test_c2_lot_releve_illisible_garde_dans_l_essai_jamais_une_cellule[lot` | oui |
| 5 | v8c | C-2 : ligne de flux illisible jetée | `test_c2_ligne_de_flux_illisible_gardee_dans_l_essai[carbon]` | oui |
| 6 | v8c | C-2 : corps illisible de Kimi jeté | `test_c2_kimi_corps_illisible_garde` | oui |
| 7 | v8c | C-3 : refus de crédit à coût zéro (comme la v9-v7) | `test_v7_refus_de_credit_echec_cout_zero` | oui |
| 8 | v8c | réflexion : budget envoyé au lieu du niveau | `test_garde_a_sain_budget_pose_et_reflexion_dans_la_provision` | oui |
| 9 | v8c | réflexion : niveau le plus haut non exigé à la composition | `test_v7_budget_hors_borne_refuse_a_la_composition[niveau_reflexion-medium-niveau]` | oui |
| 10 | v8c | réflexion : Neon au niveau « high » | `test_v5_neon_au_catalogue_seule_difference_avec_la_v3` | oui |
| 11 | v8c | garde (3) : limite de mots non passée à la garde avant l'envoi | `test_v8_garde_reglages_limite_de_mots_refuse_avant_l_envoi` | oui |
| 12 | v8c | garde : appelée sans le corps de l'essai (aucune garde par essai) | `test_a2_garde_par_essai_controle_le_corps_du_repli` | oui |
| 13 | v8c | (1, retour) : réponse sans pensées admise | `test_v8_reponse_sans_pensees_defaut_code_10_jamais_une_cellule` | oui |
| 14 | v8c | (1, retour) : pensées absentes lues comme zéro | `test_a2_pensees_absentes_jamais_lues_comme_zero_accepte` | oui |
| 15 | v8c | (4) : relance au même niveau, non corrigée | `test_v5_max_tokens_sans_texte_arret_defaut_de_reglage[neon]` | oui |
| 16 | v8c | (4) : reprise après un premier défaut au plus haut niveau | `test_v8_reprise_apres_un_premier_defaut_part_au_reglage_corrige` | oui |
| 17 | v8c | (4) : relance corrigée en défaut renvoyée par une commande suivante | `test_v6_defaut_de_reglage_jamais_renvoye_au_meme_reglage` | oui |
| 18 | v8c | (4) : MAX_TOKENS sans texte arrête sans relance corrigée | `test_v5_max_tokens_sans_texte_arret_defaut_de_reglage[neon]` | oui |
| 19 | v8c | (2) : Argon retiré de la règle du plafond large | `test_v5_max_tokens_sans_texte_arret_defaut_de_reglage[argon]` | oui |
| 20 | v8c | lot : plafonds non ramenés à la limite versée | `test_v7_lot_sain_apres_coupure` | oui |
| 21 | v8c | ajout 2 : aucun repli au budget si le niveau est refusé | `test_a2_repli_declare_au_budget_si_le_niveau_est_refuse` | oui |
| 22 | v8c | ajout 2 : repli silencieux (non journalisé) | `test_a2_repli_declare_au_budget_si_le_niveau_est_refuse` | oui |
| 23 | v8c | ajout 2 : échec d'annulation d'un lot avalé | `test_a2_echec_d_annulation_du_lot_dit_jamais_avale` | oui |
| 24 | v8c | rejugement : pensées non exigées | `test_v8_rejugement_refuse_une_reponse_sans_pensees` | oui |
| 25 | v8c | remarque 3 : empreinte du rejugement non comparée | `test_r3_verifier_compare_l_empreinte_du_rejugement_a_l_essai` | oui |
| 26 | v8c | remarque 4 : nom de lot générique | `test_v7_lot_sain_apres_coupure` | oui |
| 27 | v8c | ligne de reprise : une ligne neuve à chaque relance | `test_v8_ligne_de_reprise_bornee_idempotente_et_refus` | oui |
| 28 | v8c | ligne de reprise : ignorée par la garde par envoi | `test_v8_ligne_de_reprise_bornee_idempotente_et_refus` | oui |
| 29 | garde v3 | garde (1) : thinkingLevel absent non relevé | `test_un_essai_par_reglage_manquant[niveau` | oui |
| 30 | garde v3 | garde (1) : thinkingBudget présent avec un niveau non relevé | `test_un_essai_par_reglage_manquant[budget` | oui |
| 31 | garde v3 | garde (1) : includeThoughts non contrôlé | `test_un_essai_par_reglage_manquant[pensées` | oui |
| 32 | garde v3 | garde (1) : repli au budget, budget différent du prévu admis | `test_repli_declare_au_budget` | oui |
| 33 | garde v3 | garde (1) : réflexion nulle (provision 0) admise | `test_provision_nulle_ou_negative_refusee` | oui |
| 34 | garde v3 | garde (2) : texte sous 16 000 non relevé | `test_un_essai_par_reglage_manquant[texte` | oui |
| 35 | garde v3 | garde (2) : limite versée non contrôlée | `test_un_essai_par_reglage_manquant[plafond` | oui |
| 36 | garde v3 | garde (2) : limite non diffusée de Carbon à 65 536 | `test_limites_versees_par_mode` | oui |
| 37 | garde v3 | garde (3) : limite de mots non contrôlée | `test_limite_de_mots_bord` | oui |
| 38 | garde v3 | motif de fin : RECITATION lu comme une réponse | `test_un_essai_par_motif_de_fin[RECITATION-Texte-100-None-RECITATION]` | oui |
| 39 | garde v3 | motif de fin : zéro pensée admis | `test_un_essai_par_motif_de_fin[STOP-Réponse.-0-None-SANS_PENSEES]` | oui |
| 40 | garde v3 | repli : tout refus vaut refus du niveau | `test_niveau_refuse` | oui |
| 41 | v8c | K-1 : la relance baisse toujours le niveau (comme la v9-v8) | `test_k1_relance_garde_le_niveau_et_releve_le_plafond` | oui |
| 42 | v8c | K-1 : dernier recours non déclaré au journal | `test_v5_max_tokens_sans_texte_arret_defaut_de_reglage[neon]` | oui |
| 43 | v8c | K-1 : dernier recours non affiché | `test_k1_dernier_recours_declare_quand_aucun_plafond_plus_haut` | oui |
| 44 | v8c | K-1 : plafond relevé non journalisé dans la correction | `test_k1_relance_garde_le_niveau_et_releve_le_plafond` | oui |
| 45 | v8c | K-1 : repli, moitié du budget hors du dernier recours | `test_k1_repli_au_budget_relance_au_plafond_releve_budget_garde` | oui |
| 46 | v8c | K-2 : Argon ramené à 32 768 en flux au catalogue | `test_v5_neon_au_catalogue_seule_difference_avec_la_v3` | oui |
| 47 | v8c | garde v2 appelée au lieu de la v3 | `test_v3_reprise_declaree_rejoue_les_tours_2_et_3_sans_le_tour_1` | oui |
| 48 | v8c | témoin de Fable : lot fini lu sur done seul | `test_cl_v8_lot_fini_dit_par_son_etat_seul` | oui |
| 49 | v8c | témoin de Fable : première ligne de reprise lue au lieu de la dernière | `test_cl_v8_deux_lignes_de_reprise_la_derniere_borne` | oui |
| 50 | garde v3 | K-2 : rapport revenu à 1,6 | `test_limite_de_mots_bord` | oui |
| 51 | garde v3 | K-2 : rapport de l'espèce ignoré (constante de la v1) | `test_limite_de_mots_bord` | oui |
| 52 | garde v3 | K-2 : Argon à 32 768 en flux dans la garde | `test_sain_par_espece_et_par_mode[argon-high-65536-16384-flux]` | oui |
| 53 | garde v3 | témoin de Fable : bord exact des 16 000 refusé | `test_cl_v8_bord_exact_des_16000_jetons_de_texte` | oui |
| 54 | v8c | K-1 bis : aucune relance identique avant le dernier recours | `test_v5_max_tokens_sans_texte_arret_defaut_de_reglage[neon]` | oui |
| 55 | v8c | K-1 bis : relance identique non déclarée au journal | `test_v5_max_tokens_sans_texte_arret_defaut_de_reglage[neon]` | oui |
| 56 | v8c | K-1 bis : relance identique non affichée | `test_v8c_relance_identique_declaree_puis_ok` | oui |
| 57 | v8c | K-1 bis : reprise après la relance identique la refait | `test_v8c_reprise_apres_relance_identique_part_au_dernier_recours` | oui |
| 58 | v8c | K-1 bis : relance identique lue comme finale (cellule bloquée) | `test_v8c_reprise_apres_relance_identique_part_au_dernier_recours` | oui |
| 59 | v8c | K-1 bis : relance identique sans la marque « identique » | `test_v5_neon_max_tokens_avec_texte_partiel_relance_comme_la_v3` | oui |
| 60 | v8c | K-1 bis : relance identique du repli à la moitié du budget | `test_a2_repli_relance_corrigee_a_la_moitie_du_budget` | oui |
| 61 | garde v3 | K-2 : Carbon à 5,1 au lieu de son maximum mesuré | `test_limite_de_mots_bord` | oui |
| 62 | garde v3 | K-2 : Neon pris au rapport de Carbon | `test_v2_rapport_mesure_par_espece` | oui |

**61 mutations sur 61 prises** (numéros 2 à 62 ; le 1 est le témoin). Les numéros 2 à 53 reprennent la série de la v8b, accordée à la v8c (trois textes mis à jour : la reprise par étape, le blocage par étape finale, l'étape suivante après MAX_TOKENS sans texte). Les numéros 54 à 62 sont neufs. Les mutations ont tourné en deux passages : 2 à 15, puis 16 à 62, après la mise à jour des trois textes.

## Réserves

1. **Neon n'a aucune mesure** : son rapport de 5,1 est une borne prise par prudence. L'essai réel de la mère la remplacera.
2. **Le rapport vient de trois tours de l'étage III, sous l'ancien réglage.** Il mêle le découpage en jetons et le dépassement de la limite de mots (Fable, « Limites »).
3. **Une cellule de Google peut maintenant recevoir trois envois** : le premier, la relance identique, puis le dernier recours. Le pire cas compté ne change pas par envoi. La garde par envoi (plafond, ligne) refuse chaque envoi qui dépasserait, avant de l'envoyer.
4. **Les déclarations sont faites après les gardes de dépense**, et non avant la garde des réglages comme dans le texte de Fable pour K-1. C'est un écart de lieu, voulu pour qu'un envoi refusé ne soit jamais déclaré.
5. Réserves 3, 4 et 6 du rapport de la v8b : notées par la mère, inchangées.
6. **Les cinq fichiers neufs** sont à verser s'ils sont cachés par `.git/info/exclude` : oui, lignes 114 à 117 de `.git/info/exclude`.
7. **Commandes de reprise** : celles du rapport de la v8 (section 3), avec `S=docs/notes/collisionneur-v9/collisionneur_v9_v8c.py`.

## Pièces écrites

| fichier | empreinte |
|---|---|
| `docs/notes/collisionneur-v9/collisionneur_v9_v8c.py` | `a3fc279ed1754db250016131656671d0639d03749bc62dff88b99a2b72b5b531` |
| `docs/notes/collisionneur-v9/test_collisionneur_v9_v8c.py` | `f7136092c5d76533227dff87c9403eb29f33cb803377497f0f999bf524274f7e` |
| `src/controle_ia/garde_google_v3.py` | `923679b51cfc84b65ff7cfc65296378d08e6d4e64f6b427823d23ba24f4afe91` |
| `tests/test_garde_google_v3.py` | `aceabdb2b35ec62fedf982281b1de76a6a02f651ff5cfa3391831e05825a122a` |

Chaque fichier a son compagnon `.sha256`, fait par `sha256sum F > F.sha256` dans son dossier. Ce rapport aussi.
