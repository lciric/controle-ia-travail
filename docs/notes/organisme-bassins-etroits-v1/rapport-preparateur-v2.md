# Rapport du préparateur — lanceur v2 de l'atelier d'idées sur les bassins étroits — v2

Préparateur (Claude Opus 5.5), repris avec son contexte, 13 novembre 2026, de 13:57 à 14:30 UTC (heures relevées par
`date -u`). Consigne de corrections `consigne-preparateur-organisme-bassins-etroits-corrections-v1.md`
(`e9bef58685d6c0f52abd63373be4ae90055f6c28af2f3d33aa07afc4af3099aa`, vérifiée) ; contre-lecture
`contre-lecture-lanceur-bassins-etroits-v1.md` (`3aaf9981a3fc03ee5510e3b9a136c6360217ba9ab021d7ca851dd6e9454d57ab`, vérifiée) ;
interdits d'origine appliqués (aucune dépense, aucun appel de modèle, aucun réseau, aucune opération git, ni
`.claude/settings.json` ni `.claude/hooks/` lus ou touchés, noms neufs). **Le bras n'a été exécuté ni contre l'orchestrateur
réel ni en simulation** ; seul l'analyseur d'arguments réel l'a lu (sans appel). Aucun refus de permission ni de classifieur
dans cette reprise.

## Verdict

**Lanceur v2 prêt pour une vérification courte.** Le bloquant et les neuf majeurs sont corrigés, chacun avec un cas sain et
un artefact ; dix mineurs corrigés ou écrits, deux refusés avec raison. Essais : **122 passés** (dont trois sans appel contre
l'orchestrateur réel). Mutations : **22 tués sur 22** (les douze du contre-lecteur, dont ses six survivants, et dix sur les gardes neuves), contrôle de l'outil : tous passés.

## Pièces (scellées)

| Pièce | Empreinte SHA-256 |
|---|---|
| `scripts/lancer_course_ideation_bassins_etroits_v2.py` | `c6d82d8c9439a2f7fbc0f2d41228d56cb8327d1d3b27e7ca0b15f846e474bb00` |
| `tests/test_lancer_course_ideation_bassins_etroits_v2.py` | `4038ca4e4d39f7dbdcdefb3da5a319fb1f2c78803edda608f34dfc1e22a6a4fb` |
| `docs/notes/organisme-bassins-etroits-v1/conception-trois-generations-v2.md` | `b6c7035ee8a6d72cf28901f98b6d756b733131a97b93e1800b37dd8a33af8926` |
| `docs/notes/organisme-bassins-etroits-v1/temoins-bassins-etroits-v2.json` | `f1ddcef9748d63e8884176c6e846bb65ef9df0b4e261e486b0656a5344687631` |
| `docs/notes/organisme-bassins-etroits-v1/devis-organisme-bassins-etroits-v2.md` | `23077e8bed04fd9f796fdba792f24081d4c7d8a8b2c6f30eadf8696d41cb5a71` |
| `…/preparateur-outils-v2/differentiel-lanceur-v1-v2.diff` | `1c818120366b27a765f24942a7e14db2e1dedfe0ff24046c740d7ba680e3e1bd` |
| `…/preparateur-outils-v2/mutations_lanceur_v2.py` | `8a440185fbbad72512a00c11eb452dddb4fd2112b7ad19682cef70e70bc6dc0d` |
| `…/preparateur-outils-v2/resultat-mutations-lanceur-v2.json` | `4ddf4512c2b206742b798e0b879f15ea5aed69d518a0a1e2fbd80cf8f250cba2` |

Inchangés : question `c188fa9a…`, faits `d19b5400…`, lanceur v1 `a10420cc…`, témoins v1 `748f391e…`.

## Constat par constat

| Constat | Issue | Où (lanceur v2, sauf mention) | Essai qui le prouve |
|---|---|---|---|
| **B1** compagnon de la liste blanche recréé | corrigé : le compagnon écrit par l'orchestrateur est **lu et vérifié** (`lire_json_scelle`), jamais recréé ; le faux orchestrateur l'écrit comme le vrai | `construire_liste_blanche` | `test_b1_compagnon_ecrit_par_l_orchestrateur_verifie` ; artefacts `test_b1_artefacts_liste_blanche` (sans sceau, liste différente) ; **sans appel, orchestrateur réel** : `test_b1_liste_blanche_et_mesure_contre_l_orchestrateur_reel`, `test_analyseur_reel_accepte_les_trois_commandes` ; mutant N10 |
| **M1** dépense illisible comptée 0 | corrigé : aucun chemin ne rend 0 par défaut ; 0 seulement si le superviseur a fini proprement et que rien n'est parti ; tout dossier `tentative-N` ou `tentative-N-externe-*` sans `tentative-N.json` scellé, tout fichier inattendu, tout processus mort sans fin propre → plafond entier, génération verrouillée | `depense_course`, `depense_run`, `etat_generation` | `test_m1_controle_d_argon_interrompu_compte_le_plafond`, `test_depense_course_cas`, `test_cout_mal_type_compte_le_plafond` (−1, texte, booléen, nul, infini, NaN), `test_m7_mort_sans_fin_propre` ; mutants M2, N1, N2 |
| **M2** refus « rien envoyé » verrouillant ; marge mince | corrigé : une tentative à dépense relevée ≤ 10⁻⁵ USD (coût plancher 10⁻⁶ d'un refus sans envoi) ne verrouille pas ; contrôle externe 1,5 → **1,7** ; gardes de la commande d'Argon **à 3 caractères par jeton** (contrôle, passes, juge, contrôle court) ; somme externe 7,6 < 8 ; pire cas avec bras 8,0 ≤ 8 ; génération 17,9 ≤ 20 ; trois 53,7 ≤ 60 | `SEUIL_SANS_DEPENSE_USD`, `CONTROLE_EXTERNE_USD`, `gardes_de_taille`, `garder_bras` | `test_m2_refus_rien_envoye_ne_verrouille_pas`, `test_tailles_sain_mesure_gabarit`, `test_tailles_artefact_commande_argon_a_3_caracteres`, `test_sommes_sain_production`, `test_sommes_artefacts` |
| **M3** bras relancé après dépense | corrigé : un bras ne se relance que si chaque bras précédent a fini proprement en « non joué, rien envoyé » ; jamais après un manifeste du bras, une tentative payée ou un refus de taille ; trois au plus ; l'essai qui consacrait la relance est retiré | `bras_relancable`, `etat_generation` | `test_m3_bras_paye_pas_de_relance`, `test_m3_bras_joue_illisible_verrouille`, `test_m3_bras_non_joue_relancable_trois_fois_au_plus`, `test_m3_bras_non_joue_puis_reussi` ; mutants M9, N3 |
| **M4** règle de passage : appariement, repli, mesure réservée | corrigé : plus aucune mesure de l'orchestrateur ; doublons sur le seul signalement explicite d'un juge ; une fiche de passe 2 n'est plus sautée pour être la version d'une fiche prise ; donnée manquante ou mal formée → arrêt (code 2, motif) ; texte et code d'accord | `choisir_fiches_recues` ; conception v2 § 3 | `test_regle_de_passage` (passe 2 prise, doublon sauté), `test_regle_de_passage_n_emploie_pas_les_mesures_de_convergence`, `test_regle_de_passage_artefacts` (5 cas), `test_regle_de_passage_sceau_faux` ; mutants M11, N4 |
| **M5** lecture d'N-053 non confirmée | corrigé : générations 2 et 3 refusées sans `attestations/confirmation-regle-de-passage-v1.md` scellé ; la génération 1 n'en dépend pas ; ce que la confirmation couvre est écrit (conception v2 § 3.6) | `etat_generation` | `test_m5_generation_2_sans_confirmation` ; mutant N6 |
| **M6** qui lit | corrigé : la mère lit (Lazar peut s'y substituer) ; l'attestation dit qui (`lecteur` non vide), quoi (empreintes des fiches et de la consigne en attente, égales à celles de la course), quand (`lu_le`) ; versions `-v<N>`, la plus haute lue ; conséquence (enchaînement sans geste humain hors la confirmation) écrite | `lire_attestation`, `derniere_attestation` ; conception v2 § 6 | `test_attestation_artefacts` (5 cas), `test_attestation_version_la_plus_haute`, `test_attestation_non_scellee` ; mutant M8 |
| **M7** durée contre la borne de l'outil | corrigé : lancement **détaché** sous un superviseur (session neuve, sorties en fichiers, PID et heure de départ au manifeste de départ scellé, signaux relayés par PID, code scellé) ; la même commande : en marche → code 3 ; finie → clôture ; morte → plafond et verrou ; rien ne part tant qu'un superviseur vit | `SUPERVISEUR`, `lancer_detache`, `superviseur_vivant`, `cloturer`, `executer` | `test_m7_en_marche_rien_ne_part`, `test_m7_mort_sans_fin_propre`, `test_m7_arret_par_pid_relaye`, `test_m7_superviseur_vivant_pid_reutilise`, `test_trois_generations_bout_en_bout` (session distincte) ; mutant N5 |
| **M8** recoupement ni épinglé ni relu | corrigé : compagnon **et** attestation scellée de relecture par la mère (`attestation-relecture-recoupement-v1.json` : lecteur, lu_le, `recoupement_sha256`, aucune recette ni secret, témoin vrai absent) ; les deux empreintes au manifeste | `piece_generation_1` | `test_m8_recoupement_artefacts` (9 cas) ; mutant N7 |
| **M9** témoins | corrigé pour (a) : témoin vrai réécrit (estimateur de Chao des bassins non vus), et règle : la mère certifie qu'aucune pièce servie aux juges ne l'énonce (relecture du recoupement ; attestation de g − 1) ; (b) écrit comme réserve au devis et à la conception ; (c), (d) refusés : durcir les témoins faux ferait échouer la chaîne sur un juge sain, ils visent les fautes grossières (dit) | `temoins-bassins-etroits-v2.json` ; `etat_generation`, `piece_generation_1` | chargés par le chargeur réel (sans appel) ; `test_m9_temoin_vrai_present_dans_les_fiches`, cas « temoin » de `test_m8_recoupement_artefacts` ; mutant N8 |
| m1 révocation mal formée ignorée | corrigé : toute ligne qui cite le GO doit avoir 8 colonnes ; type « révocation » lu sans accent ni casse | `verifier_go` | `test_m1_go_revoque_ou_ligne_mal_formee` (3 cas), `test_go_ligne_qui_cite_bien_formee_admise` ; mutant N9 |
| m2 bras joué hors du lanceur | corrigé : les traces du bras sont lues dans la sortie, avec ou sans manifeste du lanceur | `traces_bras`, `depense_bras` | `test_m2_bras_joue_hors_du_lanceur_compte` |
| m3 plafond sur la somme des fiches | corrigé : le plafond porte sur la pièce entière | `choisir_fiches_recues` | `test_regle_de_passage_plafond_de_la_piece_entiere` |
| m4 doublons sans fermeture | écrit dans la règle (union, sans fermeture transitive) | conception v2 § 3.3 ; docstring | `test_regle_de_passage` |
| m5 étiquettes à allure ordinale | **refusé en partie** : l'étiquette `G<g>-R<i>` est celle que la question scellée (`c188fa9a…`) nomme ; la changer demanderait une question neuve. La tête de la pièce dit que le numéro n'est pas un rang et qu'un « raffine G…-R… » reçu renvoie à une génération invisible | `_texte_piece` | `test_regle_de_passage` (« n'est pas un rang ») |
| m6 bras sans `--moteur claude-sdk` | corrigé : `--moteur claude-sdk --confirmer-moteur-reel` ajoutés ; accepté par l'analyseur réel | `commande_bras` | `test_analyseur_reel_accepte_les_trois_commandes`, `test_trois_generations_bout_en_bout` |
| m7 gardes sans artefact | corrigé : les six survivants (M6 tentatives, M7 borne 60, M8 consigne à l'attestation, M9 trois bras, M10 manifeste du bras, M12 plancher du contrôle court) et préfixe du cache, liste blanche différente, mesure illisible, run sans manifeste, version incohérente, attestation mal formée, aucune fiche éligible | essais | `test_m6_trois_tentatives_au_plus`, `test_m7_borne_du_cumul_jamais_au_dela_de_60`, `test_attestation_artefacts`, `test_m3_bras_non_joue_relancable_trois_fois_au_plus`, `test_m10_generation_jouee_exige_le_manifeste_du_bras`, `test_m12_plancher_du_controle_court`, `test_prefixe_du_cache_artefact`, `test_b1_artefacts_liste_blanche`, `test_mesure_illisible`, `test_run_sans_manifeste`, `test_run_version_incoherente`, `test_regle_de_passage_artefacts` |
| m8 exception hors `Refus` | corrigé : toute exception après la création du dossier de run écrit un manifeste de refus scellé ; la relance reste permise si rien n'est parti | `executer` | `test_m8_toute_exception_ecrit_un_manifeste_de_refus` |
| m9 garde lexicale de l'orchestrateur | écrit aux limites (conception v2 § 8) ; à compter par motif après la course | conception | — |
| m10 devis | écrit (Fable sans précédent, sonde de la garde refus-question, bras impossible au-delà de ≈ 14 400 caractères par fiche) | devis v2 § 5 | — |
| m11 crochet sans `-I -B` | proposé dans le texte de règle ci-dessous (la mère l'écrit) | — | — |
| m12 question et commit | **refusé** pour la question : scellée et épinglée, son cœur est mot pour mot celui du collisionneur ; « Q1 … Q7, Q-pont » est le texte du gabarit de l'orchestrateur, qu'on ne change pas ; commit `f39a7f4a` / `be6b5af9` hors des neuf fichiers : réserve écrite (conception v2 § 8) | — | — |

## Mutations (outil du contre-lecteur adapté au v2)

| Mutant | Garde affaiblie | Issue | Essais en échec (extrait) |
|---|---|---|---|
| base | aucune (contrôle de l'outil) | contrôle : tous passés |  |
| M1-cumul-sans-plafond-suivant | garde de cumul : plafond suivant non compté | tué | `test_cumul_depasse`, `test_m7_borne_du_cumul_jamais_au_dela_de_60` |
| M2-depense-illisible-comptee-zero | manifeste de fin illisible compté 0 | tué | `test_cout_mal_type_compte_le_plafond[-1]`, `test_cout_mal_type_compte_le_plafond[None]` |
| M3-relance-apres-depense | relance d'une course après dépense | tué | `test_m1_controle_d_argon_interrompu_compte_le_plafond`, `test_pas_de_relance_apres_depense` |
| M4-generation-suivante-sans-bras | génération g+1 sans bras de g | tué | `test_m10_generation_jouee_exige_le_manifeste_du_bras`, `test_m3_bras_joue_illisible_verrouille[illisible]` |
| M5-argument-non-ferme | arguments en plus admis | tué | `test_argument_artefacts[argv3]` |
| M6-tentatives-de-course-non-bornees | trois tentatives de course | tué | `test_m6_trois_tentatives_au_plus` |
| M7-borne-du-cumul-egale-au-go | borne 60 cède au plafond du GO | tué | `test_m7_borne_du_cumul_jamais_au_dela_de_60` |
| M8-attestation-sans-consigne-du-juge | consigne en attente non exigée | tué | `test_attestation_artefacts[modif1-consigne en attente]`, `test_attestation_artefacts[modif2-consigne en attente]` |
| M9-bras-non-bornes | trois bras | tué | `test_m3_bras_non_joue_relancable_trois_fois_au_plus` |
| M10-bras-reussi-sans-manifeste-du-bras | manifeste du bras non exigé | tué | `test_m10_generation_jouee_exige_le_manifeste_du_bras` |
| M11-classement-illisible-transmis | classement illisible transmis | tué | `test_regle_de_passage_artefacts[classement.json-contenu3-illisible]` |
| M12-plancher-du-controle-court-non-garde | plancher du contrôle court | tué | `test_m12_plancher_du_controle_court` |
| N1-controle-externe-interrompu-zero | M1 : dossier de contrôle externe sans tentative | tué | `test_depense_course_cas`, `test_m1_controle_d_argon_interrompu_compte_le_plafond` |
| N2-mort-sans-fin-compte-zero | M7 : processus mort sans fin propre compté 0 | tué | `test_depense_course_cas`, `test_m7_mort_sans_fin_propre` |
| N3-bras-relance-apres-paiement | M3 : bras relancé après paiement | tué | `test_m3_bras_paye_pas_de_relance` |
| N4-doublons-ignores | M4 : doublons des juges ignorés | tué | `test_regle_de_passage` |
| N5-en-marche-ignore | M7 : processus en marche ignoré | tué | `test_m7_en_marche_rien_ne_part` |
| N6-confirmation-non-exigee | M5 : confirmation non exigée | tué | `test_m5_generation_2_sans_confirmation` |
| N7-relecture-recoupement-non-exigee | M8 : relecture du recoupement non exigée | tué | `test_m8_recoupement_artefacts[autre_empreinte-empreinte]`, `test_m8_recoupement_artefacts[recette-aucune recette]` |
| N8-temoin-vrai-non-garde | M9 : témoin vrai présent admis | tué | `test_m9_temoin_vrai_present_dans_les_fiches` |
| N9-revocation-mal-formee-ignoree | m1 : ligne mal formée ignorée | tué | `test_m1_go_revoque_ou_ligne_mal_formee[| GO-2026-11-14-01 | 2026-11-14 | r\xe9vocation | r\xe9voque GO-2026-11-13-03 | \u2014 | \u2014 | Lazar | x | y |-mal form\xe9e]` |
| N10-liste-blanche-sans-sceau | B1 : compagnon non vérifié | tué | `test_b1_artefacts_liste_blanche[FAUX_LB_SANS_SCEAU-compagnon]` |

## Différentiel v1 → v2, pour une vérification courte

`preparateur-outils-v2/differentiel-lanceur-v1-v2.diff` (`diff -u`). Repris tels quels du v1 : interpréteur, git et
orchestrateur, caches d'octets, préfixe, pièces, drapeaux, sommes, environnement sans clés, sonde, `ecrire_scelle`. Changés :
en-tête et constantes (version, témoins v2, contrôle externe 1,7, dossiers `…-v2`, superviseur) ; `verifier_go` (m1) ;
`gardes_de_taille` (garde à 3 caractères par jeton). Neufs ou réécrits : processus détachés ; `runs_du_lanceur` ;
`depense_course`, `traces_bras`, `depense_bras`, `depense_run` ; `bras_relancable` ; attestations ; `etat_generation` ;
`choisir_fiches_recues` et `_texte_piece` ; `construire_liste_blanche` ; `piece_generation_1` ; `garder_bras` ; `cloturer` ;
`executer`, `executer_bras` ; `commande_bras` (moteur armé).

## Règle de permission et épingle proposées pour la version 2 (non écrites ; la mère les écrit et les dit à Lazar)

Une règle par commande exacte — **trois** commandes, et non « la seule commande » du mot de Lazar :

```json
"allow": [
  "Bash(/usr/local/bin/python3 -I -B scripts/lancer_course_ideation_bassins_etroits_v2.py 1)",
  "Bash(/usr/local/bin/python3 -I -B scripts/lancer_course_ideation_bassins_etroits_v2.py 2)",
  "Bash(/usr/local/bin/python3 -I -B scripts/lancer_course_ideation_bassins_etroits_v2.py 3)"
],
"deny": [
  "Edit(//home/user/controle-ia-travail/scripts/lancer_course_ideation_bassins_etroits_v2.py)",
  "Edit(//home/user/controle-ia-travail/scripts/lancer_course_ideation_bassins_etroits_v2.py.sha256)",
  "Edit(//home/user/controle-ia-travail/.claude/hooks/garde_calcul.py)"
]
```

Épingle au crochet `.claude/hooks/garde_calcul.py`, de la forme de `garder_lanceur_v3` : toute commande qui cite
`lancer_course_ideation_bassins_etroits_v2` est bloquée sauf si elle est exactement l'une des trois ci-dessus, lancée depuis
`/home/user/controle-ia-travail`, fichier présent et non lien, empreinte égale à la constante `c6d82d8c9439a2f7fbc0f2d41228d56cb8327d1d3b27e7ca0b15f846e474bb00` **et** au compagnon
`.sha256`. Essais du crochet : un cas sain par génération ; octet changé ; compagnon faux ; argument `4` ; deux arguments ;
autre interpréteur ; autre dossier. Et (m11) la commande du crochet dans `.claude/settings.json` passée à
`python3 -I -B "$CLAUDE_PROJECT_DIR/.claude/hooks/garde_calcul.py"`. Ne jamais lancer en `bypassPermissions`. Le v1
(`a10420cc…`) ne doit recevoir aucune règle.

## Ce qui reste avant la génération 1

Vérification courte du v2 (autre modèle) ; règle et épingle ; recoupement et son attestation de relecture (mère) ; relais
Claude et Gemini ; sonde de la garde refus-question (≈ 0,003 USD, à part, recommandée, m10). Pour la génération 2 : la
confirmation de la règle de passage (mot de Lazar) et le programme des mesures entre générations (non écrit).
