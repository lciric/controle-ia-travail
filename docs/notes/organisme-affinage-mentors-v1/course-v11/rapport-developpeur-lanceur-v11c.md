# Rapport du développeur — lanceur v11c de la course d'affinage des idées des mentors

Pièce de classe B, écrite hors ligne : aucun appel de modèle, aucune valeur de clé lue, aucun relais lancé, rien de committé.
La v11c répond à la contre-lecture du lanceur v11b (`course-v11/contre-lecture-lanceur-v11b-v1.md`, `cd7e5455…`, commit
`90783a8fc`, verdict « Scellable après corrections »), que j'ai lue en entier, et aux corrections demandées par la mère. Les
fichiers v11 et v11b restent intacts (R12). Les numéros ci-dessous sont ceux des constats de la contre-lecture.

## 1. Fichiers neufs

| fichier | rôle |
|---|---|
| `scripts/lancer_course_affinage_mentors_v11c.py` | lanceur v11c, produit à partir du v11b (`a6f64e79…`) par des remplacements exacts et comptés |
| `tests/test_lancer_course_affinage_mentors_v11c.py` | essais v11b (`673a20d2…`) adaptés, plus les essais propres à v11c |
| `scripts/commande_gemini_flux_v2.py` | commande en flux v2 (constat 12), produite à partir de la v1 (`6aaf235d…`) |
| `tests/test_commande_gemini_flux_v2.py` | essais de la v1 (`e92ff4c9…`) passés aux réglages de production, plus ceux de l'hypothèse |
| `scripts/sonde_astra_courses_v3.py` | sonde commune d'Astra v3 (constat 9), produite à partir de la v2 (`80074c82…`) |
| `tests/test_sonde_astra_courses_v3.py` | essais de la v2 (`742f66be…`) adaptés, plus ceux de la variable de clé |
| `course-v11/configuration-course-affinage-mentors-v11c.json` | configuration v11b (`c69620da…`) ; seul changement : « code 7 » devient le code que le lanceur rend, 5 (constat 15) |
| `course-v11/declaration-relais-gabarit-course-affinage-v11c.json` | gabarit v11 (`b6e09680…`) ; seul changement : chemins de la commande en flux v2 |
| `course-v11/rapport-developpeur-lanceur-v11c.md` | ce rapport |

La sonde d'Astra elle-même (`scripts/sonde_astra_affinage_v3.py`, `32366123…`) ne change pas.

## 2. Corrections, constat par constat

1. **Base de l'écart au devis.** Les prix par appel d'Argon passent à 4 / 20 USD par million. Ce sont deux constantes nommées,
   que Fable recalculera aux réglages réels : `PRIX_ARGON_PROPOSEUR_PAR_APPEL_USD` = 0,276 × 20 / 41,5 = **0,133012** et
   `PRIX_ARGON_JUGE_PAR_APPEL_USD` = 0,0347 × 20 / 41,5 = **0,016723**. Pour obtenir la base du texte à l'arrondi exact, le prix
   d'un appel de Carbon est pris au prix exact du calcul du devis v11b, `PRIX_CARBON_PAR_APPEL_USD` = **0,480472**, au lieu de
   0,4805 arrondi.
   - `devis_estimation` pour cinq espèces = **35,683424**, soit 35,683 au millième. C'est la base du texte, que donne aussi le
     calcul du devis v11b (`calcul-devis-course-affinage-mentors-v11b.py`, rejoué).
   - Pour six espèces : 42,81056.
   - Essai d'égalité au millième, plus un artefact : l'ancienne base de 40,848 est refusée.
2. **Réglages d'Argon.** Rien n'est changé dans le code, comme décidé : provision 24 576, sortie 45 056, en flux. Le texte suit.
3. **Ligne de LUC au relevé des crédits.** L'entrée de LUC est exigée et doit porter `"solde_non_lu": true` et
   `"reference": "GO-2026-11-22-124"`.
   - Champs permis : `solde_non_lu`, `reference`, `source`, `note`.
   - Refus si l'entrée est absente ou n'est pas un objet, si la mention ou la référence manque ou diffère, si un champ porte un
     montant (solde, crédit, reste, couverture, réserve, recharge, plancher, usd, eur, montant), ou si un champ est hors de la
     liste.
   - **Noms des champs à écrire dans le texte et dans le gabarit du relevé** : `solde_non_lu`, `reference`.
   - L'essai `test_v11_releve_sans_ligne_de_luc_part` est renversé (ligne absente : refus, code 2). Onze artefacts sont ajoutés,
     dont la forme du v11b (`non_lisible`), une autre référence et un solde présent.
4. **Libellé de la contre-lecture.** Le libellé « **Opus 5.5, contre-lecteur neuf** » est exigé (`LIBELLE_CONTRE_LECTURE`).
   « modèle K », « Opus 5.5 » seul et « contre-lecteur neuf » seul sont refusés. L'essai à blanc écrit ce même libellé.
5. **Relecture finale.** Après la boucle d'attente, si aucun arrêt n'a été lu, le lanceur appelle
   `SurveillanceCleClaude.lecture_finale()`. Une lecture illisible est refaite, et trois de suite donnent le code 5. Un refus lu à
   ce moment donne le code 5 et l'alerte scellée, avec `moment` = « relecture finale, après l'arrêt de l'orchestrateur ».
   - Essai : faux orchestrateur qui, après la première lecture, écrit un 400 (ou un 402 avec motif) au journal du relais, puis
     sort aussitôt en code 3. Le lanceur rend 5, et non 6.
   - Artefact (mutant sans relecture finale) : le lanceur rend 6, sans alerte.
6. **Journal du run et manifeste de fin.**
   - Chaque lecture, lisible ou non, est écrite dans `journal-part-claude-au-fil-de-l-eau.jsonl`, dans le dossier du run, et
     scellée à la fin. Une ligne contient la date et le moment, l'état lu, la part engagée et les statuts neufs ; jamais un
     contenu.
   - Au manifeste de fin, sous `cle_claude_au_fil_de_l_eau` : `appels_par_statut`, `depassement_max_usd`,
     `appels_au_dessus_de_la_reserve`, `reserve_par_appel_usd`, `dernier_etat_lu` et `journal_du_run` (chemin, empreinte, nombre
     de lignes).
   - Une ligne du journal du relais encore sans fin de ligne est lue à la lecture suivante, au lieu d'être comptée comme
     illisible.
7. **Déclencheurs et cause.** Les déclencheurs larges sont gardés :
   - tout statut de 400 à 499 sauf 429 au journal ;
   - `refus` > 0 dans l'état ;
   - part engagée au plafond ;
   - trois lectures illisibles de suite.

   L'arrêt, l'alerte et le manifeste disent maintenant la **nature**, le **statut** et la **cause** réels :
   - une ligne de refus du relais (401, 402, 403, 404, 413) porte un `motif`, et la cause est ce motif ;
   - pour un appel relayé, la cause est « inconnue : le relais ne garde que le statut… » ;
   - un `refus` compté dans l'état sans ligne lue ne prétend plus « statut 402 ».
8. **Réserve par appel du relais Claude.** Elle est lue au départ dans l'état. Si les arguments lus par PID la donnent
   (`--reserve-par-appel`), elle doit égaler celle de l'état. Elle doit être un nombre dans [0, plafond du relais[, sinon refus.
   Elle est écrite au manifeste de départ, avec sa source et le dépassement possible par appel en vol (plafond de session d'un
   proposeur − réserve = 2,60 USD à 0,40). La constante inutilisée `RESERVE_APPEL_CLAUDE_USD` est retirée.
9. **Sonde commune v3.** La ligne de commande du relais jeté, lue par PID, doit porter `--variable-cle OPENAI_API_KEY_2`, une seule
   fois. Sinon : refus avant tout appel (code 2), rien d'écrit. La variable est écrite au rapport (`relais_jete.variable_cle`). Le
   lanceur v11c exige ce champ et la version `sonde_astra_courses_v3`.
10. **Plafond des juges.** `argon_v11.plafond_session_juge_usd` doit valoir exactement 1,00 (`JUGE_PLAFOND_EXIGE_USD`). Une valeur
    vide est aussi refusée.
11. **Garde Google.** Elle est rejouée sur la plus longue entrée de chaque rôle :
    - proposeur : consigne servie de la case la plus longue, expurgée ;
    - juge : `entree_juge_la_plus_longue`, de la forme que bâtit l'orchestrateur épinglé (`pole/fiches_v54.py`,
      `entree_une_fiche`, l. 59 : consigne, « ## La fiche », fiche JSON indentée), avec une carte de 9 000 caractères et
      1 000 caractères de cadre (SUPPOSÉ).

    Le pire cas d'un juge d'Argon est calculé sur cette même entrée (11 596 caractères, 4 059 jetons gardés) : 0,917356 USD, sous 1,00. La taille de l'entrée de
    chaque rôle est écrite au manifeste (`entree_caracteres`).
12. **Commande en flux v2.** Après chaque réponse lue, elle vérifie `candidatesTokenCount + thoughtsTokenCount ≤ maxOutputTokens`.
    - Le champ `hypothese_sortie_maximale_tenue` (vrai, faux, ou null si l'usage est illisible) est écrit dans toute ligne rendue
      après un envoi.
    - Si l'hypothèse tombe, la commande écrit une ligne `HYPOTHESE_SORTIE_MAXIMALE_TOMBEE` sur sa sortie d'erreur. Le code ne
      change pas ; le coût lu est compté et reste gardé par le plafond de session (code 7 au-delà).
13. **Réglages de production dans les essais.**
    - Commande : Carbon à 4 / 20, provision 28 672, sortie 65 536 ; Argon à 4 / 20 ; juge à 1,00.
    - Lanceur : le monde d'essai met le juge à 1,00, au lieu de 2,00.
14. **Garde Google de main** : voir § 3.
15. **Rédaction.**
    - « code 7 » est corrigé dans la configuration v11c.
    - `PART_CLAUDE_HAUT_USD` est retiré du lanceur et du manifeste.
    - `verifier_go_simplification` lit dans le plafond de GO-2026-11-22-124 le montant « part Claude N USD » et exige N = 45.
      Artefacts : 145, 4500, « 450 USD », « 45 » sans montant.

## 2 bis. Table constat → correction → essai

| constat | correction | essai (cas sain ; artefact) |
|---|---|---|
| 1 | prix par appel d'Argon à 4 / 20 (`PRIX_ARGON_PROPOSEUR_PAR_APPEL_USD` 0,133012, `PRIX_ARGON_JUGE_PAR_APPEL_USD` 0,016723), Carbon exact 0,480472 ; base 35,683 | `test_v11c_base_de_l_ecart_au_devis_egale_au_texte` (35,683 ; 40,848 refusé), `test_v11c_ecart_au_devis_au_manifeste_de_fin_sur_la_base_du_texte`, `test_v7_devis_sur_les_especes_actives` |
| 2 | aucune (réglages d'Argon du code gardés ; le texte suit) | — |
| 3 | `verifier_ligne_luc` : `solde_non_lu` vrai, `reference` GO-2026-11-22-124, aucun montant, champs permis seulement | `test_v11c_ligne_de_luc_saine_au_manifeste` ; `test_v11c_ligne_de_luc_artefacts_refuses` (11 cas), `test_v11_releve_sans_ligne_de_luc_part` (renversé), `test_v11c_verifier_ligne_luc_unitaire` |
| 4 | libellé exigé « Opus 5.5, contre-lecteur neuf » (`LIBELLE_CONTRE_LECTURE`) | `test_v11c_libelle_de_contre_lecture_sain_et_artefacts` (4 artefacts), `test_contre_lecture_sans_modele_k_refusee` (« modèle K » refusé) |
| 5 | `lecture_finale()` après l'arrêt de l'orchestrateur ; refus lu → code 5 et alerte | `test_v11c_refus_ecrit_apres_la_derniere_lecture_vu_a_la_relecture_finale` (400 et 402), `test_v11c_relecture_finale_sans_refus_ne_change_rien` ; `test_v11c_mutation_sans_relecture_finale_rend_6`, `test_v11c_lecture_finale_illisible_refaite_puis_code_5` |
| 6 | journal du run `journal-part-claude-au-fil-de-l-eau.jsonl` scellé ; comptes par statut, dépassement, réserve au manifeste de fin | `test_v11c_journal_du_run_et_comptes_au_manifeste_de_fin`, `test_v11c_ligne_du_relais_en_cours_d_ecriture_lue_la_fois_suivante` |
| 7 | déclencheurs gardés ; nature, statut et cause réels à l'arrêt et à l'alerte | `test_v11c_alerte_dit_la_nature_et_la_cause_reelles` (401, 403 avec motif ; 400 relayé), `test_v11c_refus_compte_a_l_etat_sans_ligne_lue_ne_pretend_pas_402`, `test_v11_premier_4xx_de_l_interface_lu_au_journal_arret_code_5` |
| 8 | réserve par appel lue au départ (état ; arguments par PID s'ils la donnent), écrite au manifeste ; constante morte retirée | `test_v11c_reserve_du_relais_claude_lue_au_depart` ; `test_v11c_reserve_du_relais_claude_artefacts` (5 artefacts) |
| 9 | sonde commune v3 : `--variable-cle OPENAI_API_KEY_2` exigée une fois ; lanceur exige `variable_cle` et la version v3 | `test_v3_cas_sain_variable_ecrite_au_rapport` ; `test_v3_relais_jete_d_une_autre_variable_de_cle_refuse` (4 cas) ; `test_v11c_sonde_commune_v3_saine` ; `test_v11c_sonde_commune_d_une_autre_variable_de_cle_refusee` (3 cas), `test_v11c_sonde_commune_v2_refusee` |
| 10 | plafond des juges exigé égal à 1,00 (`JUGE_PLAFOND_EXIGE_USD`) | `test_v11_argon_emplacement_de_production_1_00` ; `test_v11_argon_plafond_des_juges_au_plus_juste` (0,92, 1,1, 0,6, 2,0 refusés ; vide refusé) |
| 11 | garde Google sur la plus longue entrée de chaque rôle ; entrée de juge de la forme de l'orchestrateur (`entree_juge_la_plus_longue`) | `test_v11c_entree_de_juge_de_la_forme_de_l_orchestrateur`, `test_v11c_garde_google_rejouee_sur_la_plus_longue_entree_de_chaque_role` |
| 12 | commande en flux v2 : `hypothese_sortie_maximale_tenue`, signalement `HYPOTHESE_SORTIE_MAXIMALE_TOMBEE` | `test_v2_hypothese_tenue_au_plafond_exact` ; `test_v2_hypothese_tombee_signalee_et_journalisee`, `test_v2_hypothese_tombee_et_plafond_depasse_code_7`, `test_v2_hypothese_non_ecrite_si_rien_n_est_parti` |
| 13 | essais aux réglages de production (4 / 20 ; Carbon 28 672 / 65 536 ; juge 1,00) | `tests/test_commande_gemini_flux_v2.py` (dont `test_v2_argon_juge_aux_reglages_de_production`), monde d'essai du lanceur au juge 1,00 (`test_v11_argon_juge_servi_au_plafond_de_l_emplacement`) |
| 14 | commande exacte de la garde Google de main écrite au § 3 | extraction vérifiée à l'empreinte `923679b5…` (hors essai) |
| 15 | « code 7 » corrigé dans la configuration v11c ; `PART_CLAUDE_HAUT_USD` retiré ; montant « part Claude 45 USD » lu et égal à 45 (`PART_CLAUDE_GO_124_USD`) | `test_v11c_version_et_pieces` ; `test_v11c_go_124_montant_45_lu_exactement` (2 sains, 4 artefacts), `test_v11_mutation_constante_du_plafond_relevee_refusee` |

## 3. Commande exacte qui fournit la garde Google de main (constat 14)

Le lanceur exige `src/controle_ia/garde_google_v3.py` à l'empreinte `923679b5…` dans le dépôt de travail
`/home/user/controle-ia-travail`. La branche `lot/compte-organisme-v1` ne la porte pas, alors qu'elle porte la commande en flux v2
et la sonde v3. Sur l'arbre de départ (branche `lot/compte-organisme-v1` à jour) :

```
cd /home/user/controle-ia-travail
git fetch origin main
git show origin/main:src/controle_ia/garde_google_v3.py > src/controle_ia/garde_google_v3.py
echo "923679b51cfc84b65ff7cfc65296378d08e6d4e64f6b427823d23ba24f4afe91  src/controle_ia/garde_google_v3.py" | sha256sum -c -
```

J'ai vérifié l'extraction dans mon bloc-notes : `git show origin/main:src/controle_ia/garde_google_v3.py` donne bien `923679b5…`.
Le fichier extrait n'est pas suivi sur cette branche. Le manifeste n'en compte pas moins l'arbre comme propre (`arbre_modifie` lit
`git status --porcelain --untracked-files=no`). La garde est par ailleurs vérifiée à son empreinte par le lanceur et par la
commande.

## 4. Essais (fichiers touchés seulement)

| fichier | compte |
|---|---|
| `tests/test_lancer_course_affinage_mentors_v11c.py` | 323 réussis, 4 sautés (essais hérités qui cherchent l'orchestrateur aux emplacements fixes, absents ici), 0 échec |
| `tests/test_commande_gemini_flux_v2.py` | 32 réussis |
| `tests/test_sonde_astra_courses_v3.py` | 23 réussis |

Orchestrateur épinglé lu dans un clone à `a41b7b50` par `ORCHESTRATEUR_AFFINAGE_ESSAI`.

## 5. Points ouverts

1. **Texte à aligner** : noms des champs de la ligne de LUC (`solde_non_lu`, `reference`) ; libellé « Opus 5.5, contre-lecteur
   neuf » ; déclencheurs plus larges que (a) et (b), et cause écrite ; réglages d'Argon 24 576 / 45 056 en flux (constat 2).
2. **Prix par appel d'Argon et pire cas d'un juge** : les constantes sont les postes du devis v6 ramenés à 4 / 20. Fable les
   recalculera aux réglages réels. Le cadre de fiche de 1 000 caractères reste une hypothèse.
3. **Nom du rapport de la sonde commune** : le chemin du jour garde le suffixe `-v2.json` du v11b (`COMMUNE_DU_JOUR`). La version
   v3 est exigée dans le contenu, pas dans le nom.
4. **Garde de calcul** (`.claude/hooks/garde_calcul.py`) : non touchée. Sur le registre actuel de main, elle bloque tout lancement
   d'instance (ligne 785, GO-2026-11-22-98 ; rapport v11b, § 4).
