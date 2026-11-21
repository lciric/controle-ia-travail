# Rapport du développeur : collisionneur v9 version 8d, v1

21 novembre 2026, vers 21:20Z (`date -u`). Développeur : Claude Opus 5.5 (`claude-opus-5-5`). Pièce d'instrument (classe B). La v8d est une copie de la v8c (`a3fc279e…`, laissée intacte), corrigée selon la vérification d'Opus `verification-collisionneur-v9-v8c-opus-v1.md` (`a0ff6a76…`, lue en entière). La garde v3 (`923679b5…`) est intacte : C-2 ne la touche pas, il n'y a donc pas de garde v4. Je n'ai fait aucun envoi réel, je n'ai lu ni écrit aucune clé, je n'ai fait aucun commit.

## Corrections, aux textes exacts de la section 8 de la vérification

| point | où | essai |
|---|---|---|
| **C-1** : le devis de reprise sous-comptait le pire cas « avec relances » | `pire_tours_2_3` compte deux relances pour une cellule de Google à plafonds égaux (la relance identique, puis le dernier recours) et une pour les autres espèces. Chaque cellule porte le nombre de ses relances (`relances`). Deux phrases sont corrigées : celle de `devis_reprise` (« si chaque cellule épuisait ses relances… ») et celle de `devis` (la phrase « jusqu'au double » est remplacée) | `test_opus_c1_devis_avec_relances_compte_deux_relances_chez_google` |
| **C-2** : essai témoin du plancher de 16 000 jetons de texte en appel non diffusé | essais seulement | `test_opus_m2_plancher_de_texte_en_appel_non_diffuse` |

En dehors de ces points, seuls changent l'en-tête, `VERSION`, les lignes d'emploi, le chemin des essais et l'essai qui lit la version.

## Remarques non bloquantes : laissées en réserve

La vérification ne donne de texte exact pour aucune d'elles, je n'en porte donc aucune.
1. Des commentaires sont restés anciens :
   - ligne 408 : « × 1,6 » ;
   - ligne 1090 : « garde_google_v1.py » ;
   - lignes 1803 et 1804 : « relancés une seule fois » ;
   - ligne 1809 : « l'unique relance » ;
   - ligne 1908 : « Au plus deux essais » ;
   - ligne 2035 : l'écran dit « relance corrigée » pour une relance identique.
2. Une déclaration peut être écrite en double, jamais tue : refus du niveau à l'étape identique ou au dernier recours, ou commande morte entre la déclaration et l'envoi.
3. La reprise lit l'étape sans lire le plafond de l'essai précédent. Le cas est sans objet avec les tables actuelles.
4. `mots=None` coupe le contrôle de la limite de mots dans la garde : une garde future devrait exiger la limite.
5. Le rapport de Neon (5,1 jetons par mot) attend la mesure de l'essai réel.
6. Carbon refuse le tour de 4 000 mots de l'étage II : sa provision pour ce tour reste à revoir.
7. La v8b, ses essais et son rapport, la garde v2 et ses essais ne sont pas versés.
8. `countTokens` est une requête sans génération : aucune règle de réflexion ne s'y applique.
9. Sous un niveau de réflexion, rien ne borne la pensée hors du plafond de sortie.

## Essais

Lancés avec `PYTHONPATH=src`, sous `env -u` des sept clés, sur un `--basetemp` neuf :

| suites | résultat |
|---|---|
| `docs/notes/collisionneur-v9/test_collisionneur_v9_v8d.py` et `tests/test_garde_google_v3.py` | **405 passés, 1 sauté** (361 et 44 ; le sauté est la copie « dopamine », non désignée) |

## Mutations

Chaque mutation est faite sur une copie, les deux suites entières, arrêt au premier échec. Le témoin sans mutation passe : 402 passés, 3 sautés, 1 désélectionné. La série reprend les 61 mutations de la v8c et en ajoute trois : deux sur C-1, et la mutation M2 de la vérification, qui contrôle le plancher de 16 000 en flux seulement.

En cours de travail, le disque du conteneur s'est rempli à 100 % (5,7 Mo libres). J'ai supprimé mes propres copies de mutations des versions 8 à 8c, dans mon bloc-notes ; leurs sorties texte sont gardées. L'outil n'emploie plus qu'un dossier temporaire par partie, que pytest vide à chaque course.

Outil : `/tmp/claude-0/-home-user-controle-ia-travail/2eb82089-3810-5ff8-881f-da5f24b622eb/scratchpad/dev-v8/outils/mutations_v8d.py`.

| n° | pièce mutée | mutation | premier essai en échec | prise |
|---|---|---|---|---|
| 2 | v8d | C-1 : un relevé refusé abandonne le lot | `test_v7_lot_sain_apres_coupure` | oui |
| 3 | v8d | remarque 4 : aucun dernier relevé avant l'annulation | `test_v7_lot_artefact_non_abouti_au_delai_annule_compte_au_pire` | oui |
| 4 | v8d | C-2 : relevé d'un lot échoué jeté | `test_c2_lot_releve_illisible_garde_dans_l_essai_jamais_une_cellule[lot` | oui |
| 5 | v8d | C-2 : ligne de flux illisible jetée | `test_c2_ligne_de_flux_illisible_gardee_dans_l_essai[carbon]` | oui |
| 6 | v8d | C-2 : corps illisible de Kimi jeté | `test_c2_kimi_corps_illisible_garde` | oui |
| 7 | v8d | C-3 : refus de crédit à coût zéro (comme la v9-v7) | `test_v7_refus_de_credit_echec_cout_zero` | oui |
| 8 | v8d | réflexion : budget envoyé au lieu du niveau | `test_garde_a_sain_budget_pose_et_reflexion_dans_la_provision` | oui |
| 9 | v8d | réflexion : niveau le plus haut non exigé à la composition | `test_v7_budget_hors_borne_refuse_a_la_composition[niveau_reflexion-medium-niveau]` | oui |
| 10 | v8d | réflexion : Neon au niveau « high » | `test_v5_neon_au_catalogue_seule_difference_avec_la_v3` | oui |
| 11 | v8d | garde (3) : limite de mots non passée à la garde avant l'envoi | `test_v8_garde_reglages_limite_de_mots_refuse_avant_l_envoi` | oui |
| 12 | v8d | garde : appelée sans le corps de l'essai (aucune garde par essai) | `test_a2_garde_par_essai_controle_le_corps_du_repli` | oui |
| 13 | v8d | (1, retour) : réponse sans pensées admise | `test_v8_reponse_sans_pensees_defaut_code_10_jamais_une_cellule` | oui |
| 14 | v8d | (1, retour) : pensées absentes lues comme zéro | `test_a2_pensees_absentes_jamais_lues_comme_zero_accepte` | oui |
| 15 | v8d | (4) : relance au même niveau, non corrigée | `test_v5_max_tokens_sans_texte_arret_defaut_de_reglage[neon]` | oui |
| 16 | v8d | (4) : reprise après un premier défaut au plus haut niveau | `test_v8_reprise_apres_un_premier_defaut_part_au_reglage_corrige` | oui |
| 17 | v8d | (4) : relance corrigée en défaut renvoyée par une commande suivante | `test_v6_defaut_de_reglage_jamais_renvoye_au_meme_reglage` | oui |
| 18 | v8d | (4) : MAX_TOKENS sans texte arrête sans relance corrigée | `test_v5_max_tokens_sans_texte_arret_defaut_de_reglage[neon]` | oui |
| 19 | v8d | (2) : Argon retiré de la règle du plafond large | `test_v5_max_tokens_sans_texte_arret_defaut_de_reglage[argon]` | oui |
| 20 | v8d | lot : plafonds non ramenés à la limite versée | `test_v7_lot_sain_apres_coupure` | oui |
| 21 | v8d | ajout 2 : aucun repli au budget si le niveau est refusé | `test_a2_repli_declare_au_budget_si_le_niveau_est_refuse` | oui |
| 22 | v8d | ajout 2 : repli silencieux (non journalisé) | `test_a2_repli_declare_au_budget_si_le_niveau_est_refuse` | oui |
| 23 | v8d | ajout 2 : échec d'annulation d'un lot avalé | `test_a2_echec_d_annulation_du_lot_dit_jamais_avale` | oui |
| 24 | v8d | rejugement : pensées non exigées | `test_v8_rejugement_refuse_une_reponse_sans_pensees` | oui |
| 25 | v8d | remarque 3 : empreinte du rejugement non comparée | `test_r3_verifier_compare_l_empreinte_du_rejugement_a_l_essai` | oui |
| 26 | v8d | remarque 4 : nom de lot générique | `test_v7_lot_sain_apres_coupure` | oui |
| 27 | v8d | ligne de reprise : une ligne neuve à chaque relance | `test_v8_ligne_de_reprise_bornee_idempotente_et_refus` | oui |
| 28 | v8d | ligne de reprise : ignorée par la garde par envoi | `test_v8_ligne_de_reprise_bornee_idempotente_et_refus` | oui |
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
| 41 | v8d | K-1 : la relance baisse toujours le niveau (comme la v9-v8) | `test_k1_relance_garde_le_niveau_et_releve_le_plafond` | oui |
| 42 | v8d | K-1 : dernier recours non déclaré au journal | `test_v5_max_tokens_sans_texte_arret_defaut_de_reglage[neon]` | oui |
| 43 | v8d | K-1 : dernier recours non affiché | `test_k1_dernier_recours_declare_quand_aucun_plafond_plus_haut` | oui |
| 44 | v8d | K-1 : plafond relevé non journalisé dans la correction | `test_k1_relance_garde_le_niveau_et_releve_le_plafond` | oui |
| 45 | v8d | K-1 : repli, moitié du budget hors du dernier recours | `test_k1_repli_au_budget_relance_au_plafond_releve_budget_garde` | oui |
| 46 | v8d | K-2 : Argon ramené à 32 768 en flux au catalogue | `test_v5_neon_au_catalogue_seule_difference_avec_la_v3` | oui |
| 47 | v8d | garde v2 appelée au lieu de la v3 | `test_v3_reprise_declaree_rejoue_les_tours_2_et_3_sans_le_tour_1` | oui |
| 48 | v8d | témoin de Fable : lot fini lu sur done seul | `test_cl_v8_lot_fini_dit_par_son_etat_seul` | oui |
| 49 | v8d | témoin de Fable : première ligne de reprise lue au lieu de la dernière | `test_cl_v8_deux_lignes_de_reprise_la_derniere_borne` | oui |
| 50 | garde v3 | K-2 : rapport revenu à 1,6 | `test_limite_de_mots_bord` | oui |
| 51 | garde v3 | K-2 : rapport de l'espèce ignoré (constante de la v1) | `test_limite_de_mots_bord` | oui |
| 52 | garde v3 | K-2 : Argon à 32 768 en flux dans la garde | `test_sain_par_espece_et_par_mode[argon-high-65536-16384-flux]` | oui |
| 53 | garde v3 | témoin de Fable : bord exact des 16 000 refusé | `test_cl_v8_bord_exact_des_16000_jetons_de_texte` | oui |
| 54 | v8d | K-1 bis : aucune relance identique avant le dernier recours | `test_v5_max_tokens_sans_texte_arret_defaut_de_reglage[neon]` | oui |
| 55 | v8d | K-1 bis : relance identique non déclarée au journal | `test_v5_max_tokens_sans_texte_arret_defaut_de_reglage[neon]` | oui |
| 56 | v8d | K-1 bis : relance identique non affichée | `test_v8c_relance_identique_declaree_puis_ok` | oui |
| 57 | v8d | K-1 bis : reprise après la relance identique la refait | `test_v8c_reprise_apres_relance_identique_part_au_dernier_recours` | oui |
| 58 | v8d | K-1 bis : relance identique lue comme finale (cellule bloquée) | `test_v8c_reprise_apres_relance_identique_part_au_dernier_recours` | oui |
| 59 | v8d | K-1 bis : relance identique sans la marque « identique » | `test_v5_neon_max_tokens_avec_texte_partiel_relance_comme_la_v3` | oui |
| 60 | v8d | K-1 bis : relance identique du repli à la moitié du budget | `test_a2_repli_relance_corrigee_a_la_moitie_du_budget` | oui |
| 61 | garde v3 | K-2 : Carbon à 5,1 au lieu de son maximum mesuré | `test_limite_de_mots_bord` | oui |
| 62 | v8d | C-1 : une seule relance comptée chez Google (comme la v9-v8c) | `test_opus_c1_devis_avec_relances_compte_deux_relances_chez_google` | oui |
| 63 | v8d | C-1 : relances comptées mais non ajoutées au total | `test_opus_c1_devis_avec_relances_compte_deux_relances_chez_google` | oui |
| 64 | garde v3 | C-2 (M2 d'Opus) : plancher de 16 000 contrôlé en flux seulement | `test_opus_m2_plancher_de_texte_en_appel_non_diffuse` | oui |
| 65 | garde v3 | K-2 : Neon pris au rapport de Carbon | `test_v2_rapport_mesure_par_espece` | oui |

**64 mutations sur 64 prises** (numéros 2 à 65 ; le 1 est le témoin). Chaque mutation est prise par l'échec d'un essai, jamais par une erreur. Un premier passage, gêné par le disque plein, a été écarté et versé dans mon bloc-notes (`essai-1/`) ; la série entière a été rejouée après le retour de la place.

## Pièces écrites

| fichier | empreinte |
|---|---|
| `docs/notes/collisionneur-v9/collisionneur_v9_v8d.py` | `b780383874598f12b24c79e4087d335c8e01cda685e295f5116898fa3b1715ac` |
| `docs/notes/collisionneur-v9/test_collisionneur_v9_v8d.py` | `6c2204f1c5c5126a23a57ee41160a6932f87f627c35eef1aac115de270230841` |

Chaque fichier a son compagnon `.sha256`, fait par `sha256sum F > F.sha256` dans son dossier. Ce rapport aussi.
