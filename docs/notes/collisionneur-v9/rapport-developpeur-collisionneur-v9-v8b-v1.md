# Rapport du développeur : collisionneur v9 version 8b, v1

21 novembre 2026, vers 19:20Z (`date -u`). Développeur : Claude Opus 5.5 (`claude-opus-5-5`). Pièces d'instrument (classe B), à vérifier de nouveau par Fable. La base est la v8 (`b8569031…`) et la garde v1 (`04d233bd…`), toutes deux laissées intactes. Les corrections suivent la vérification de Fable, `verification-corrections-collisionneur-v9-v8-fable-v1.md` (`9cf6799f…`), lue en entier, et les décisions de la mère. Je n'ai fait aucun envoi réel, je n'ai lu ni écrit aucune clé, et je n'ai fait aucun commit.

## Verdict

K-1 est portée au texte exact de Fable, et K-2 selon la décision de la mère. Les essais demandés y sont : les 16 essais qui lisent les tables sont accordés, avec les 3 essais de K-1 et les 3 essais témoins. **Une conséquence de K-2 bloque la reprise des dossiers**, voir la réserve 1.

## Corrections

| point | dans la v8b et la garde v2 | essais |
|---|---|---|
| **K-1** : la relance garde le niveau et relève le plafond ; dernier recours déclaré | `reglage_de_relance`, et le bloc de la relance dans `executer_cellule`, au texte exact de Fable. Quand le plafond de relance est au-dessus du premier plafond, la relance garde le niveau et relève le plafond. Sinon, c'est le dernier recours : le niveau baisse d'un cran, ou le budget du repli est divisé par deux. Ce dernier recours est déclaré **avant l'envoi**, par la ligne propre `dernier_recours_reflexion_declare` au journal et par « DERNIER RECOURS DÉCLARÉ » à l'écran. Avec les tables actuelles (premier plafond égal au plafond de relance pour les trois espèces), toute relance passe par le dernier recours déclaré | les trois essais de Fable (`test_k1_…`), plus `test_k1_dernier_recours_au_repli_moitie_du_budget_declaree` et `test_k1_repli_au_budget_relance_au_plafond_releve_budget_garde` |
| **K-2** : rapport de jetons par mot mesuré (décision de la mère) | `src/controle_ia/garde_google_v2.py` : `JETONS_PAR_MOT_MESURES` vaut 5,1 pour Argon, Carbon et Neon. C'est **le plus haut rapport relevé sur les 43 réponses réelles complètes d'Argon et de Carbon (5,06), arrondi à 5,1** : la table de Fable, section 4.2, donne de 1,78 à 5,06 pour Argon et de 2,40 à 4,11 pour Carbon. La garde prend le rapport de l'espèce, sauf si l'appelant en donne un autre | `tests/test_garde_google_v2.py::test_v2_rapport_mesure_par_espece`, `::test_limite_de_mots_bord` (bord : 3 212 mots acceptés, 3 213 refusés) ; `test_v8_garde_reglages_limite_de_mots` ; `test_v8_garde_reglages_mots_des_tours_compatibles` ; `test_v8b_k2_carbon_refuse_au_tour_iii3_sous_5_1` |
| **Argon à 65 536 en flux dès le premier envoi** | catalogue d'Argon à 65 536 pour le premier envoi comme pour la relance ; `LIMITES_SORTIE["argon"]["flux"]` à 65 536. Source : page versée `docs/sources/google-gemini-reflexion-v1/gemini-thinking-generate-content-2026-11-21-v1.md.txt` (`fe0b8d88…`, sceau tenu), ligne 931. Jamais servi : à confirmer par l'essai réel. En lot, Argon reste à 32 768 (liste versée, ligne 594) | `test_k2_argon_a_65536_des_le_premier_envoi` ; `tests/…::test_limites_egales_a_la_liste_versee` (lit la ligne 931 de la page) |
| Les 16 essais qui lisent les tables | accordés (marque « v9-v8b ») : les deux `test_b4_…`, `test_v5_neon_au_catalogue_…`, `test_v7_budget_envoye_…[argon]`, `test_v7_argon_reglages_prix_et_sources`, `test_v7_argon_pire_cas_et_cout_reel`, `test_v8_garde_reglages_sain_pour_le_catalogue`, `…_limite_de_mots`, `…_mots_des_tours_compatibles` ; dans la garde, `test_sain_par_espece_et_par_mode` (quatre cas), `test_limites_versees_par_mode`, `test_limites_egales_a_la_liste_versee`, `test_limite_de_mots_bord` | — |
| Trois essais témoins de Fable (remarque 1) | `test_cl_v8_bord_exact_des_16000_jetons_de_texte` (garde) ; `test_cl_v8_lot_fini_dit_par_son_etat_seul` ; `test_cl_v8_deux_lignes_de_reprise_la_derniere_borne` | ils passent ; chacun prend sa mutation (section suivante) |

Sous 5,1, six essais de reprise et de rejugement feraient échouer Carbon au tour III.3 : la réponse à 3 500 mots y est refusée. Ce sont `test_v3_reprise_declaree_…`, les deux `test_v7_rejugement_…`, les deux tests de copie des dossiers (v7 et v8) et `test_v8_ligne_de_reprise_devis_…`. Ils prennent pour Carbon son maximum relevé, 4,2, par la doublure `carbon_a_son_maximum_mesure` (déclarée dans sa docstring). Le refus à 5,1 a son essai propre.

## Essais

Lancés avec `PYTHONPATH=src`, sans clés, chacun sur un `--basetemp` neuf :

| suite | résultat |
|---|---|
| `docs/notes/collisionneur-v9/test_collisionneur_v9_v8b.py` | **355 passés, 1 sauté** (la copie « dopamine », non désignée) |
| témoins : la v8 et la garde v1, intactes | 388 passés, 1 sauté |
| `tests/test_garde_google_v2.py` | **44 passés** |

## Mutations

Chaque mutation est faite sur une copie dans mon bloc-notes, les deux suites entières, arrêt au premier échec. Le témoin sans mutation passe : 395 passés, 3 sautés, 1 désélectionné. La série reprend les 39 mutations de la v8, et en ajoute 13 sur K-1, K-2 et les trois essais témoins de Fable. Le témoin passe à 395 avant l'ajout d'un essai, à 396 après. Outil : `/tmp/claude-0/-home-user-controle-ia-travail/2eb82089-3810-5ff8-881f-da5f24b622eb/scratchpad/dev-v8/outils/mutations_v8b.py`. Sorties : `/tmp/claude-0/-home-user-controle-ia-travail/2eb82089-3810-5ff8-881f-da5f24b622eb/scratchpad/dev-v8/mutations-v8b-pairs.txt` et `…/mutations-v8b-impairs.txt`.

| n° | pièce mutée | mutation | premier essai en échec | prise |
|---|---|---|---|---|
| 2 | v8b | C-1 : un relevé refusé abandonne le lot | `test_v7_lot_sain_apres_coupure` | oui |
| 3 | v8b | remarque 4 : aucun dernier relevé avant l'annulation | `test_v7_lot_artefact_non_abouti_au_delai_annule_compte_au_pire` | oui |
| 4 | v8b | C-2 : relevé d'un lot échoué jeté | `test_c2_lot_releve_illisible_garde_dans_l_essai_jamais_une_cellule[lot` | oui |
| 5 | v8b | C-2 : ligne de flux illisible jetée | `test_c2_ligne_de_flux_illisible_gardee_dans_l_essai[carbon]` | oui |
| 6 | v8b | C-2 : corps illisible de Kimi jeté | `test_c2_kimi_corps_illisible_garde` | oui |
| 7 | v8b | C-3 : refus de crédit à coût zéro (comme la v9-v7) | `test_v7_refus_de_credit_echec_cout_zero` | oui |
| 8 | v8b | réflexion : budget envoyé au lieu du niveau | `test_garde_a_sain_budget_pose_et_reflexion_dans_la_provision` | oui |
| 9 | v8b | réflexion : niveau le plus haut non exigé à la composition | `test_v7_budget_hors_borne_refuse_a_la_composition[niveau_reflexion-medium-niveau]` | oui |
| 10 | v8b | réflexion : Neon au niveau « high » | `test_v5_neon_au_catalogue_seule_difference_avec_la_v3` | oui |
| 11 | v8b | garde (3) : limite de mots non passée à la garde avant l'envoi | `test_v8_garde_reglages_limite_de_mots_refuse_avant_l_envoi` | oui |
| 12 | v8b | garde : appelée sans le corps de l'essai (aucune garde par essai) | `test_a2_garde_par_essai_controle_le_corps_du_repli` | oui |
| 13 | v8b | (1, retour) : réponse sans pensées admise | `test_v8_reponse_sans_pensees_defaut_code_10_jamais_une_cellule` | oui |
| 14 | v8b | (1, retour) : pensées absentes lues comme zéro | `test_a2_pensees_absentes_jamais_lues_comme_zero_accepte` | oui |
| 15 | v8b | (4) : relance au même niveau, non corrigée | `test_v5_max_tokens_sans_texte_arret_defaut_de_reglage[neon]` | oui |
| 16 | v8b | (4) : reprise après un premier défaut au plus haut niveau | `test_v8_reprise_apres_un_premier_defaut_part_au_reglage_corrige` | oui |
| 17 | v8b | (4) : relance corrigée en défaut renvoyée par une commande suivante | `test_v6_defaut_de_reglage_jamais_renvoye_au_meme_reglage` | oui |
| 18 | v8b | (4) : MAX_TOKENS sans texte arrête sans relance corrigée | `test_v5_max_tokens_sans_texte_arret_defaut_de_reglage[neon]` | oui |
| 19 | v8b | (2) : Argon retiré de la règle du plafond large | `test_v5_max_tokens_sans_texte_arret_defaut_de_reglage[argon]` | oui |
| 20 | v8b | lot : plafonds non ramenés à la limite versée | `test_v7_lot_sain_apres_coupure` | oui |
| 21 | v8b | ajout 2 : aucun repli au budget si le niveau est refusé | `test_a2_repli_declare_au_budget_si_le_niveau_est_refuse` | oui |
| 22 | v8b | ajout 2 : repli silencieux (non journalisé) | `test_a2_repli_declare_au_budget_si_le_niveau_est_refuse` | oui |
| 23 | v8b | ajout 2 : échec d'annulation d'un lot avalé | `test_a2_echec_d_annulation_du_lot_dit_jamais_avale` | oui |
| 24 | v8b | rejugement : pensées non exigées | `test_v8_rejugement_refuse_une_reponse_sans_pensees` | oui |
| 25 | v8b | remarque 3 : empreinte du rejugement non comparée | `test_r3_verifier_compare_l_empreinte_du_rejugement_a_l_essai` | oui |
| 26 | v8b | remarque 4 : nom de lot générique | `test_v7_lot_sain_apres_coupure` | oui |
| 27 | v8b | ligne de reprise : une ligne neuve à chaque relance | `test_v8_ligne_de_reprise_bornee_idempotente_et_refus` | oui |
| 28 | v8b | ligne de reprise : ignorée par la garde par envoi | `test_v8_ligne_de_reprise_bornee_idempotente_et_refus` | oui |
| 29 | garde v2 | garde (1) : thinkingLevel absent non relevé | `test_un_essai_par_reglage_manquant[niveau` | oui |
| 30 | garde v2 | garde (1) : thinkingBudget présent avec un niveau non relevé | `test_un_essai_par_reglage_manquant[budget` | oui |
| 31 | garde v2 | garde (1) : includeThoughts non contrôlé | `test_un_essai_par_reglage_manquant[pensées` | oui |
| 32 | garde v2 | garde (1) : repli au budget, budget différent du prévu admis | `test_repli_declare_au_budget` | oui |
| 33 | garde v2 | garde (1) : réflexion nulle (provision 0) admise | `test_provision_nulle_ou_negative_refusee` | oui |
| 34 | garde v2 | garde (2) : texte sous 16 000 non relevé | `test_un_essai_par_reglage_manquant[texte` | oui |
| 35 | garde v2 | garde (2) : limite versée non contrôlée | `test_un_essai_par_reglage_manquant[plafond` | oui |
| 36 | garde v2 | garde (2) : limite non diffusée de Carbon à 65 536 | `test_limites_versees_par_mode` | oui |
| 37 | garde v2 | garde (3) : limite de mots non contrôlée | `test_limite_de_mots_bord` | oui |
| 38 | garde v2 | motif de fin : RECITATION lu comme une réponse | `test_un_essai_par_motif_de_fin[RECITATION-Texte-100-None-RECITATION]` | oui |
| 39 | garde v2 | motif de fin : zéro pensée admis | `test_un_essai_par_motif_de_fin[STOP-Réponse.-0-None-SANS_PENSEES]` | oui |
| 40 | garde v2 | repli : tout refus vaut refus du niveau | `test_niveau_refuse` | oui |
| 41 | v8b | K-1 : la relance baisse toujours le niveau (comme la v9-v8) | `test_k1_relance_garde_le_niveau_et_releve_le_plafond` | oui |
| 42 | v8b | K-1 : dernier recours non déclaré au journal | `test_k1_dernier_recours_declare_quand_aucun_plafond_plus_haut` | oui |
| 43 | v8b | K-1 : dernier recours non affiché | `test_k1_dernier_recours_declare_quand_aucun_plafond_plus_haut` | oui |
| 44 | v8b | K-1 : plafond relevé non journalisé dans la correction | `test_k1_relance_garde_le_niveau_et_releve_le_plafond` | oui |
| 45 | v8b | K-1 : repli, moitié du budget hors du dernier recours | `test_k1_repli_au_budget_relance_au_plafond_releve_budget_garde` | oui |
| 46 | v8b | K-2 : Argon ramené à 32 768 en flux au catalogue | `test_v5_neon_au_catalogue_seule_difference_avec_la_v3` | oui |
| 47 | v8b | garde v1 appelée au lieu de la v2 | `test_garde_a_artefact_sortie_au_dela_de_la_sortie_comptee` | oui |
| 48 | v8b | témoin de Fable : lot fini lu sur done seul | `test_cl_v8_lot_fini_dit_par_son_etat_seul` | oui |
| 49 | v8b | témoin de Fable : première ligne de reprise lue au lieu de la dernière | `test_cl_v8_deux_lignes_de_reprise_la_derniere_borne` | oui |
| 50 | garde v2 | K-2 : rapport revenu à 1,6 | `test_limite_de_mots_bord` | oui |
| 51 | garde v2 | K-2 : rapport de l'espèce ignoré (constante de la v1) | `test_limite_de_mots_bord` | oui |
| 52 | garde v2 | K-2 : Argon à 32 768 en flux dans la garde | `test_sain_par_espece_et_par_mode[argon-high-65536-16384-flux]` | oui |
| 53 | garde v2 | témoin de Fable : bord exact des 16 000 refusé | `test_cl_v8_bord_exact_des_16000_jetons_de_texte` | oui |

**52 mutations sur 52 prises** (numéros 2 à 53 ; le 1 est le témoin). Les numéros 2 à 40 reprennent la série de la v8, et 41 à 53 sont neufs : K-1, K-2, garde v2 et les trois essais témoins de Fable. La mutation 45 (la relance du repli divise le budget par deux même quand le plafond est relevé) n'était pas prise au premier passage. J'ai ajouté `test_k1_repli_au_budget_relance_au_plafond_releve_budget_garde`, puis je l'ai rejouée : elle est prise. Le témoin, rejoué, donne 396 passés.

## Réserves

1. **K-2 bloque la reprise des quatre dossiers au tour III.3 de Carbon.** À 5,1 jetons par mot, la réponse de Carbon au tour III.3 (3 500 mots) demande 17 850 jetons, au-delà des 16 384 jetons de texte de Carbon (65 536 − 49 152). Elle est donc refusée avant l'envoi : code 1, rien n'est compté ni envoyé (`test_v8b_k2_carbon_refuse_au_tour_iii3_sous_5_1`). Les tours de 3 000 mots passent. Trois issues sont possibles, toutes à trancher par la mère :
   - (a) Carbon à 4,2, son maximum relevé : une ligne de `JETONS_PAR_MOT_MESURES`, comme le proposait Fable ; la reprise passe alors, éprouvée sur les copies ;
   - (b) une provision de Carbon d'au plus 47 685 jetons, ce qui donne plus de 17 850 jetons de texte ;
   - (c) garder le refus.
2. **K-1 a peu d'effet avec les tables actuelles.** Les trois espèces ont un premier plafond égal à leur plafond de relance (Argon à 65 536 dès le premier envoi, sur la décision de la mère). Toute relance est donc le dernier recours déclaré, au niveau plus bas. Le relèvement du plafond n'est éprouvé que sur une copie des tables (Argon à 32 768 puis 65 536).
3. **Les pires cas d'Argon montent à 65 536 + 16 384 jetons de sortie comptés**, soit environ 1,64 USD par cellule au lieu de 0,98. Les copies des dossiers tiennent sous leurs lignes ; `devis-reprise` en tient compte.
4. **Il faut l'essai réel par modèle de la mère avant toute reprise** : Argon à 65 536 au niveau « high » (pensées non nulles ?), Neon au niveau « xhigh ».
5. **Le rapport de 5,1 est relevé sous l'ancien réglage**, sur trois tours de l'étage III. Il mêle le découpage en jetons et le dépassement de la limite de mots par les modèles (Fable, section « Limites »).
6. **Les cinq fichiers neufs sont cachés par `.git/info/exclude`** (lignes 104 à 107), comme ceux de la v8 : à verser par la mère.
7. **Les commandes de reprise restent celles du rapport de la v8** (section 3), avec `S=docs/notes/collisionneur-v9/collisionneur_v9_v8b.py`. Elles ne passent pas le tour III.3 de Carbon tant que la réserve 1 n'est pas tranchée. Le dossier fusionné est `collisionneur-question-de-recherche-fusionnee-v1-20261121-153256` (nom trouvé par Fable). Ses cellules d'Argon écrites sans pensées sont `E3-T1-conception-C` et `E3-T2-critique-croisee-C`.

## Pièces écrites

| fichier | empreinte |
|---|---|
| `docs/notes/collisionneur-v9/collisionneur_v9_v8b.py` | `6cd0209c10118ff58d5ad3b6e2cc3e3c52c33aa155db2df96f53b9d5786f4c9b` |
| `docs/notes/collisionneur-v9/test_collisionneur_v9_v8b.py` | `e27561406bd50c55255d155dbca9e0b77b206986bfdcaf1f0740245531765287` |
| `src/controle_ia/garde_google_v2.py` | `9d39a7496d0a7b36197e369d12fe1e72d1d878abca2d9d8d764c4750ed91473b` |
| `tests/test_garde_google_v2.py` | `6adad2604f010b1f7bb003d86b55da1fcc391e9147d7915625940e2f7af9803d` |

Chaque fichier a son compagnon `.sha256`, fait par `sha256sum F > F.sha256` dans son dossier. Ce rapport aussi.
