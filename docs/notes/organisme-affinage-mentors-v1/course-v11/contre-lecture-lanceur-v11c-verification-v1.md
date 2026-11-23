# Vérification des corrections — lanceur v11c de la course d'affinage (pièce de classe B)

- Même contre-lecteur que la contre-lecture du v11b (`contre-lecture-lanceur-v11b-v1.md`, `cd7e5455…`), Opus 5.5. Hors ligne : aucun appel payant, aucune valeur de clé, aucune poussée, aucune pièce modifiée. Fichier écrit, non committé.
- Branche `prep/lanceur-affinage-v11c-interrompu-v1`, commit `1ed883749`, dans `/home/user/wt-organisme`.
- Empreintes vérifiées (compagnon `.sha256` égal au fichier) : lanceur v11c `fe7358b9…`, ses essais `88a61acd…`, commande en flux v2 `13b968eb…` et ses essais `35e874ef…`, sonde commune v3 `d02971f0…` et ses essais `49142a34…`, configuration v11c `7615a31c…`, gabarit de déclaration v11c `1c0f8f9a…`, rapport du développeur v11c `a56faf45…`.
- Hors périmètre par consigne : constat 2 (le texte suit le code) ; ligne 785 du registre.

## Verdict

Scellable après corrections.

Les corrections des constats 1 et 3 à 15 sont faites ou, pour deux d'entre elles, faites en partie sans risque. Une régression est apparue : l'essai à blanc du lanceur écrit une ligne de LUC que la nouvelle garde refuse (R1 ci-dessous). Une fois cette ligne corrigée, la pièce est scellable.

## Essais (fichiers v11c seulement ; `.venv`, `PYTHONPATH=src`, orchestrateur épinglé lu dans un clone à `a41b7b50`)

| fichier | compte |
|---|---|
| `tests/test_commande_gemini_flux_v2.py` | 32 réussis |
| `tests/test_sonde_astra_courses_v3.py` | 23 réussis |
| `tests/test_lancer_course_affinage_mentors_v11c.py` | 323 réussis, 4 sautés (essais hérités qui cherchent l'orchestrateur aux emplacements fixes), 0 échec, 19 min 08 s |

## Constats du v11b

| n° | état | preuve |
|---|---|---|
| 1 base de l'écart au devis | **corrigé** | l. 537-550 : Argon à 0,133012 et 0,016723, `DEVIS_V5_TOTAL` cinq espèces 35,683424 ; `test_v11c_base_de_l_ecart_au_devis_egale_au_texte`, `test_v11c_ecart_au_devis_au_manifeste_de_fin_sur_la_base_du_texte` |
| 3 ligne de LUC au relevé | **corrigé**, avec la régression R1 | `verifier_ligne_luc` l. 1412-1428, appelée l. 1461 : entrée exigée, `solde_non_lu` vrai, `reference` GO-2026-11-22-124, aucun champ de montant, champs permis seulement ; `test_v11c_ligne_de_luc_saine_au_manifeste`, `test_v11c_ligne_de_luc_artefacts_refuses` (11 cas), `test_v11_releve_sans_ligne_de_luc_part` renversé |
| 4 libellé de la contre-lecture | **corrigé** | l. 459 et 1014 : « Opus 5.5, contre-lecteur neuf » exigé ; `test_v11c_libelle_de_contre_lecture_sain_et_artefacts`, « modèle K » refusé. Le texte doit porter le même libellé (à vérifier au scellement du préenregistrement). |
| 5 relecture finale | **corrigé** | l. 2287-2295 (`lecture_finale`, lecture illisible refaite jusqu'à trois fois) et l. 2757-2767 (appelée après la boucle, même après une exception, jamais tue) ; `test_v11c_refus_ecrit_apres_la_derniere_lecture_vu_a_la_relecture_finale` (400 et 402), mutation `test_v11c_mutation_sans_relecture_finale_rend_6` |
| 6 journal du run, comptes | **corrigé** | `JOURNAL_PART_CLAUDE` l. 2189, une ligne par lecture (`_ecrire`), scellé par `sceller_journal` ; `bilan` l. 2305-2311 : comptes par statut, `depassement_max_usd`, `appels_au_dessus_de_la_reserve`, réserve ; ligne en cours d'écriture lue la fois suivante (l. 2253) ; `test_v11c_journal_du_run_et_comptes_au_manifeste_de_fin`, `test_v11c_ligne_du_relais_en_cours_d_ecriture_lue_la_fois_suivante` |
| 7 déclencheurs plus larges | **corrigé** (option « écrire l'écart ») | déclencheurs gardés et dits dans la docstring de la classe ; l'arrêt écrit la nature, le statut et la cause réels (motif du relais, ou « inconnue » pour un appel relayé) ; le faux « 402 » pour tout `refus` > 0 a disparu (l. 2277-2280) ; `test_v11c_alerte_dit_la_nature_et_la_cause_reelles`, `test_v11c_refus_compte_a_l_etat_sans_ligne_lue_ne_pretend_pas_402`. Le texte doit nommer ces déclencheurs. |
| 8 réserve du relais Claude | **corrigé** | l. 1688-1691 (lue par le numéro de processus si donnée, égale à l'état) et l. 1777-1785 (lue dans l'état, refus hors de [0, plafond[, écrite au manifeste avec le dépassement possible par appel en vol) ; constante morte retirée ; `test_v11c_reserve_du_relais_claude_lue_au_depart`, `…_artefacts` (5) |
| 9 clé du relais jeté de la sonde | **corrigé** | sonde commune v3 : `--variable-cle OPENAI_API_KEY_2` exigée ; lanceur l. 401-402 et 1893-1905 (version v3 et `variable_cle` exigées) ; `test_v3_relais_jete_d_une_autre_variable_de_cle_refuse` (4), `test_v11c_sonde_commune_d_une_autre_variable_de_cle_refusee` (3), `test_v11c_sonde_commune_v2_refusee` |
| 10 plafond des juges | **corrigé** | l. 460 et 943 : 1,00 exigé exactement, vide refusé ; `test_v11_argon_plafond_des_juges_au_plus_juste` |
| 11 garde Google, entrées | **partiellement corrigé** | entrée de juge de la forme de l'orchestrateur (`entree_juge_la_plus_longue` l. 1337, d'après `pole/fiches_v54.py`), utilisée au pire cas (l. 1365) et à la capture (l. 2122) ; plus longue entrée de chaque rôle. Restent : pas de capture sur l'entrée la plus courte (le texte la demande ; les réglages capturés ne dépendent pas de l'entrée, risque nul) ; 1 000 caractères de cadre toujours SUPPOSÉS (marge large). À accorder au texte. |
| 12 hypothèse de sortie maximale | **corrigé** | commande v2 : `hypothese_sortie_maximale_tenue` dans chaque ligne après un envoi, signalement `HYPOTHESE_SORTIE_MAXIMALE_TOMBEE` sur la sortie d'erreur, code inchangé, code 7 au-delà du plafond ; `test_v2_hypothese_tenue_au_plafond_exact`, `test_v2_hypothese_tombee_signalee_et_journalisee`, `…_et_plafond_depasse_code_7` |
| 13 essais aux réglages de production | **corrigé** | `tests/test_commande_gemini_flux_v2.py` l. 31 (Carbon 4 / 20, 28 672 / 65 536) et l. 209-222 (Argon, juge à 1,00) ; `test_v2_argon_juge_aux_reglages_de_production` |
| 14 précondition de lieu | **corrigé** (texte) | rapport v11c, § 3 : commande exacte d'extraction de la garde de `main`, vérifiée à `923679b5…` ; refus nommé inchangé dans le lanceur |
| 15 rédaction | **corrigé** | « code 7 » absent de la configuration v11c ; `PART_CLAUDE_HAUT_USD` retiré ; GO-124 : montant « part Claude … USD » lu et égal à 45 (l. 813-814) ; `test_v11c_go_124_montant_45_lu_exactement` (2 sains, 4 artefacts) |

## Régression nouvelle

**R1 — Majeur (correction d'une ligne) : l'essai à blanc est refusé par la nouvelle garde de LUC.** `reglages_a_blanc`, l. 2889-2890, écrit pour la clé LUC `{"solde_console_usd": 0.0, "source": …, "recharge_declaree_usd": 100.0, "recharge_source": …}`. `verifier_credits` est appelée aussi en moteur simulé, et `verifier_ligne_luc` refuse cette ligne (rejoué : « « solde_non_lu » vrai et « reference » = GO-2026-11-22-124 exigés (lus : None, None) »). L'essai à blanc, condition de départ (GO-2026-11-22-107 ; brouillon 3, § K), rendrait donc le code 2. Aucun essai ne joue `reglages_a_blanc`, d'où des essais verts. Correction : ligne `{"solde_non_lu": true, "reference": "GO-2026-11-22-124", "source": "essai à blanc"}` ; ajouter un essai qui construit les réglages à blanc et passe leur relevé à `verifier_credits`. (L'essai à blanc reste aussi bloqué tant que le préenregistrement v11 n'existe pas, puisque `reglages_a_blanc` en lit l'empreinte : c'est attendu.)

Aucune autre régression vue dans les parties relues : boucle d'attente, relecture finale, contrôles du relais Claude, lecture des GO, commande v2 (seul ajout : le champ d'hypothèse et son signalement).
