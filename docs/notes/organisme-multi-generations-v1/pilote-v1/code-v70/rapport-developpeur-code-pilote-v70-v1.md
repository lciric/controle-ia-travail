# Rapport du développeur — code v70 du pilote MR-2 (corrections de la contre-lecture du différentiel v68 → v69) — v1

- **Développeur** : Claude Opus 5.5 (`claude-opus-5-5`), développeur **neuf**, sous-agent de la session
  `session_01QPDgKgACWyCkCN8HjqwNXy`. Je n'ai écrit ni le code v68, ni le v69, ni leurs contre-lectures. Un premier développeur
  v70, arrêté par une limite d'usage, n'avait rien versé : je suis reparti de la v69.
- **Mandat** : message de la mère (code v70 : les cinq majeurs D-1 à D-5 et les huit mineurs d-1 à d-8 de la contre-lecture du
  différentiel v68 → v69). Pièces lues, **chacune égale à son compagnon avant lecture** : contre-lecture
  `contre-lecture-differentiel-code-pilote-v69-v1.md` (`935e44bc6d21cbc36206424486c39ed5569f594978c6e490b2c1c04dc487a613`,
  sur `main`) et ses outils (`mutations_contre_lecteur_v69_v1.py`, `epreuves_contre_lecteur_v69_v1.py`,
  `epreuve_mesure_autres_mondes_v69_v1.py` et leurs sorties) ; `registres/decisions.md` R-2548 (décisions de la mère sur ses
  majeurs), R-2527, R-2528, R-2534, R-2542 ; consigne du code v68 `consigne-developpeur-code-pilote-v1.md` (`3b4f570c…`) ;
  rapport du développeur v69 (`c396ec43…`) ; paquet v69 (`89aa20ba…`) et ses prérequis ; brouillon 4 du texte (`04ada9fa…`) ;
  vérifications courtes v1 (`45394b74…`) et v2 (`9b662803…`).
- **Heures** (`date -u`, 13 novembre 2026) : début 17:59:14 ; empreintes, lectures et chaîne de l'arbre 18:00 à 18:06 ; essais v69
  rejoués sur l'arbre reconstruit 18:10:44 à 18:12:44 (88 passés, 112 sous-essais) ; quatre mondes de développement 18:13:02 à
  18:26:02 ; code v70 18:14 à 18:41 ; jalon 1 18:41:13 ; essais complets 18:43:56 à 18:47:46 ; essais à blanc 18:47:59 à
  18:48:09 ; premier passage du banc lancé 18:48:37, **arrêté par moi** vers 18:49 (disque plein, section 7) ; jalon 2 18:51:37 ;
  passage du banc tué par la limite de 30 minutes des tâches de fond 18:51:50 à ≈ 19:22 (section 7) ; jalon 3 de l'organisme
  ≈ 19:30 ; banc complet en deux passages, 19:30:18 → 20:33:37 (88) et 20:33:50 → 21:20:56 (64) ; refus d'outil vers 20:34
  (section 15) ; essais finaux 21:21:11 → 21:24:55 ; fin : 21:27:31 (dépôt du rapport).
- **Aucune dépense, aucun appel de modèle, aucune machine, aucune clé lue ; la sonde n'a jamais été jouée** (seulement sur la
  doublure des essais : boucle locale, clés factices posées par les essais dans les environnements qu'ils bâtissent). Réseau : une
  seule récupération git à refspec explicite (`refs/heads/main` du dépôt public `lciric/ideation-organism`, pour le commit
  `94bfd92`, prérequis du paquet v65 ; le clone local en lecture est superficiel et ne le porte pas) ; rien d'autre. Tous mes
  lancements d'essais, de banc et d'essais à blanc sous `env -i` (PATH, OMP_NUM_THREADS=2, HOME et TMPDIR de mon bac) : aucune
  variable de l'environnement réel n'a atteint un essai. Un processus de calcul à la fois, `ulimit -v 6000000`. Rien poussé.
  **Un refus d'outil** (contrôle de sécurité intégré, vers 20:34 : section 15) ; aucun refus de classifieur ni de crochet.

## 0. Verdict

**Code v70 écrit sous des noms neufs (la v69 reste dans l'arbre) : les cinq majeurs D-1 à D-5 et les huit mineurs d-1 à d-8
corrigés ; le point (7) de la contre-lecture (doublure) durci aussi. Deux écarts écrits (section 4) : l'empreinte du relevé de la
sonde est au bloc gelé par `bloc --releve-sonde`, pas dans un champ de la configuration ; la règle de comptage de la réflexion
est écrite à la configuration v11 d'après la documentation des fournisseurs (non vérifiée) et le mode réel refuse tant que la
sonde ne l'a pas confirmée. Essais : 109 passés, 166 sous-essais. Banc : 152 mutations, **152 tuées pour la raison attendue** (deux passages).** La sonde payante est une
sous-commande du lanceur (`sonde`), sous deux lignes de GO à part (s1 4,39 USD sur crédits de Claude, s2 3,68 USD hors crédits) qui
n'existent pas encore. Le bloc gelé versé ici (`EMPREINTES-code-pilote-v70.txt`) dit donc « relevé de la sonde absent » : il est
**provisoire** ; le bloc à recopier au texte sera celui que rend `bloc --releve-sonde RELEVE` après la sonde.

## 1. Arbre et chaîne

- Arbre neuf `/home/user/pilote-v70/organisme` (hors du dépôt de programme), reconstruit selon la chaîne : dépôt public (commit
  `94bfd92`) → paquet v65 (`prep/organisme-v65-v1`, lu par `git show`, tête `cef5ea60`) → v66 (tête `7e415cba`) → v67 (tête
  `ab53b7f`) → v68 (tête `276b6afd`) → **v69** (`89aa20ba…`, tête `2ca17ea3243979837890e1243876299a202b7748`) ; chaque paquet égal à
  son compagnon et `git bundle verify` conforme avant d'être lu ; le fichier des quatre mondes de développement régénéré est
  **égal à celui de la v68** (`687974573f18d937020350fe9534c529e70cb654e9219d0985b01e46fb05f07c`).
- Branche `prep/organisme-v70-pilote-mr2-v1` depuis `2ca17ea` ; commits `9613640` (jalon 1 : code, configuration v11, essais), `49015da` (jalon 2 : banc, essais renforcés), `932a5ff` (jalon 3 : sélections du banc resserrées sur l'essai attendu, motif d'un essai rendu exact).
- Fichiers neufs (`orchestrator/`) : `pole/pilote_mr2_v70.py` (cœur, 902 lignes), `pole/proposeurs_pilote_v70.py` (499),
  `pole/audit_pilote_v70.py` (176), **`pole/sonde_pilote_v70.py` (287, neuf)**, `demonstrations/pilote_mr2_v70.py` (lanceur, 568),
  `exemples/pilote-mr2-v70/commandes/commande_pilote_v70.py` (275), `…/relais_pilote_v70.py` (475),
  `exemples/pilote-mr2-v70/configuration-pilote-mr2-v11.json` ; essais `essais/test_pilote_mr2_v70.py` (2 061) ; banc
  `essais/mutations_pilote_mr2_v70.py` (412). Aucun fichier v69 modifié (ajouts seulement). Lignes citées : celles de la tête v70.

## 2. Majeurs, un par un

| constat | issue | où (fichier, ligne) | correction | essais ; mutations |
|---|---|---|---|---|
| **D-1** règle des graines fausse au manifeste (étiquette v68 écrite, v69 employée) | corrigé | cœur l. 88-98 ; lanceur l. 76, l. 114 | **étiquette v69 gardée** (le choix de la contre-lecture : épisodes et textes servis inchangés), figée en chaîne, plus liée au nom de version ; la règle écrite (`REGLE_EPISODES`) est **bâtie depuis la constante** que `episodes_de_developpement` emploie ; le manifeste la reprend (`REGLE_DES_GRAINES` = `REGLE_EPISODES` + le reste) et le bloc gelé en fait une ligne (`regle-des-graines-episodes …`), donc le texte scellé la recopie et le mode réel la vérifie : code, manifeste et texte disent **la même chaîne** ; elle dit les octets (16 premiers), l'ordre (gros-boutiste), la forme (UTF-8 de l'étiquette suivie de l'empreinte du devis en hexadécimal minuscule), le nombre d'instances et l'ordre des tirages | `EssaiABlanc.test_regle_des_graines_redonne_les_episodes` (la règle relue **seule** au manifeste — étiquette et nombre d'instances lus par expression régulière — redonne l'empreinte des épisodes servis des quatre mondes) ; `RegleDesGraines.test_sain` ; `BlocGele.test_sain`, `test_artefacts` (texte au bloc d'étiquette v68 : refus) ; essai à blanc A : textes servis, épisodes, héritages et C-17 **égaux à ceux de la v69** ; D1a à D1e |
| **D-2** (a) abandon sur coût excessif ajouté par le développeur v69 ; (b) réflexion d'Astra comptée deux fois | corrigé (b : avec un écart écrit, section 4) | proposeurs l. 41-42, l. 126-129, l. 359-361 ; lanceur l. 280-285 ; commande l. 133-169, l. 201 ; relais l. 101-118, l. 306-312, l. 377-379, l. 409-418, l. 449 ; configuration v11 | (a) décision de la mère : **coût lu au-dessus du pire cas = arrêt du pilote** (`ArretPilote`, code 3), jamais un abandon ni un échec silencieux : pièces scellées, relevé et manifeste partiels, l'appel porté au relevé (`cause: cout_excessif`, `arret: true`, `abandon: false`), sa dépense comptée ; le relais se **verrouille** (409 à tout appel suivant, rien vers l'amont ; drapeau `au_dessus_du_pire_cas` dans sa réponse et son journal ; `verrouille` à son état) ; (b) règle de comptage = champ gelé `reflexion_comprise` par proposeur (booléen ; Claude : vrai seulement, aucun compte séparé), passé à la commande et au relais (`--reflexion-comprise oui|non`), contrôlé à l'état du relais, recopié au bloc ; v11 : Fable 5.2 et Opus 5.5 vrai, **Astra vrai** (le champ `completion_tokens` compterait déjà la réflexion : l'épreuve X2 n'est plus lue en double), **Argon faux** (pensées ajoutées) | `C7C8C10Appel.test_cout_excessif_arret` (Astra, Argon, Opus : arrêt, pièces scellées, verrou, 409, plancher), `test_etats_et_abandons` (scénario « reflexion_longue » : 80 % de la borne facturée dont 70 % de réflexion — l'épreuve X2 — complet, sans abandon ni arrêt, pour Argon, Astra et Opus) ; `EssaiABlanc.test_cout_excessif_arret_du_pilote` ; `Commande.test_dialectes`, `test_reglages_et_plafond` ; `Configuration.test_artefacts` ; `EtatDesRelais.test_artefacts` ; `RelaisRefus.test_lancement_refuse` ; D2a à D2o, N6, V12 |
| **D-3** `mesurer` ne lie pas les mondes au manifeste (et `lire` non plus) | corrigé | lanceur l. 383-404 (`mesurer`), l. 420-446 (`lire`) | décision de la mère : `mesurer` exige le fichier des mondes du manifeste (`--mondes-sha256` = `controles.mondes.fichier_mondes_sha256`) et ses empreintes de mondes ; la pièce de la mesure porte `fichier_mondes_sha256` ; `lire` exige le manifeste égal à son compagnon et à celui de la mesure, et les mondes mesurés égaux à ceux du manifeste | `EssaiABlanc.test_mesure_autres_mondes_d3` (épreuve X9 rejouée : quatre autres mondes publics, empreinte juste → refus, aucune sortie), `test_mesure_manifeste_mondes_d3`, `test_lecture_artefacts` (« mondes » ; manifeste refait) ; D3a à D3d |
| **D-4** plus rien n'attend une confirmation ; la voie de Claude n'a jamais lu un vrai flux | corrigé (écart écrit, section 4) | sonde `pole/sonde_pilote_v70.py` (l. 55-233 faits, verdict, conclusions ; l. 244-287 `exiger_releve`) ; lanceur l. 95-122 (bloc), l. 193-218 (`exiger_mode_reel`), l. 322-380 (`sonde`) ; proposeurs l. 160-231 ; configuration v11, section `sonde` | décision de la mère : **sonde payante avant le scellement, écrite comme sous-commande du lanceur, jamais jouée par moi**, sous deux lignes à part (s1, s2) ; détail section 10. Le mode réel **exige** `--releve-sonde` : relevé égal à son compagnon, complet, fait avec la borne courte, par la commande et le relais de cette configuration, pour l'identité de chaque proposeur (modèle, dialecte, adresse, réglages, borne, variables) ; conclusions **recalculées depuis les champs d'usage bruts** égales aux siennes et toutes vraies (statut, modèle servi, borne gelée admise, raison d'arrêt, usage entier, verdict sur la réflexion égal à la règle gelée, borne courte tronquée et tenue ; Claude : flux relu égal, effort admis) ; le bloc gelé du texte scellé doit citer **ce** relevé | `ModeReelBoutEnBout.test_sain_sonde` (8 appels sur la doublure, relevé complet, verdicts égaux aux règles), `test_sain_bout_en_bout` (sonde → bloc → texte → mode réel → mesure → lecture), `test_artefacts_releve` (11 artefacts : verdict, borne non tenue, non tronqué, flux, conclusions forgées, partiel, sans borne courte, identité, pièces, version, appel manquant ; compagnon ; `bloc` refuse), `test_artefacts_sonde` (GO absente, montant faux, dossier existant, clé absente, relevé sans borne courte), `test_artefact_releve_absent`, `test_artefact_texte_scelle_sans_releve` ; `SondeFonctions` ; `Configuration.test_artefacts` (9 artefacts de la section `sonde`, 2 de la règle de comptage), `test_go_sonde` ; D4a à D4t |
| **D-5** cinq gardes neuves sans artefact (W1 à W5) | corrigé | W1 : relais l. 306-312, l. 355, l. 467 ; proposeurs l. 419-449 ; W2 : cœur l. 896 ; W3 : proposeurs l. 272-279 ; W4 : cœur l. 742-746 ; W5 : lanceur l. 393 | un artefact par garde : W1 — le relais rend les **noms** de son environnement (`environnement_noms`, jamais une valeur), contrôlés (rien d'autre que le filtre, le jeton, la clé et l'espace du proposeur) ; W3 et « session neuve » — conditions du témoin en fonction à part, chacune son artefact ; « monde public » du texte servi (aussi dit sans artefact) — artefact | W1 : `EtatDesRelais.test_environnement_du_relais_w1` (relais lancé avec neuf variables dont trois clés et deux adresses : seules passent `LANG`, `PATH`, `RELAIS_JETON` et la clé du proposeur), `test_artefacts` (4 noms étrangers), `ModeReelBoutEnBout` (ni `ANTHROPIC_BASE_URL`, ni une autre clé, ni `OMP_NUM_THREADS` aux relais, sonde comprise) ; W2 : `test_artefact_engagement_autre_fichier_des_mondes_w2` ; W3 : `test_artefacts_temoin_un_par_un` (« consigne_commande »), `test_conditions_du_temoin` ; W4 : `M6TexteEtEpisodes.test_artefacts_texte` (« gabarit », « monde_public ») ; W5 : `EssaiABlanc.test_mesure_manifeste_altere_w5` ; mutations **W1 à W5 recopiées mot pour mot** du contre-lecteur, plus W1b, W1c, W3b, W4b |

## 3. Mineurs, un par un (et le point (7))

| constat | issue | où | correction | essai ; mutation |
|---|---|---|---|---|
| **d-1** `recrite` par monde au manifeste | corrigé | cœur l. 718-720 | le public de C-16 ne dit plus que `admise` et `loi_sha256` ; `recrite` passe aux contrôles privés (jamais rapatriés) | `C16C17.test_sain`, `test_sain_monde_naturel_hors_bornes_recrit`, `EssaiABlanc.test_manifeste` ; V18 |
| **d-2** délai de l'adaptateur compté 0 USD | corrigé | proposeurs l. 309-312 | compté au plafond de session (l'amont a pu facturer) | `test_delai_de_l_adaptateur_panne` ; d2 |
| **d-3** flux : un `message_delta` sans raison efface la raison ; délai par lecture | corrigé | relais l. 150-156, l. 165-171, l. 204-209 | une raison d'arrêt lue n'est jamais effacée ; délai total du flux (`lignes_dans_le_delai`) | `RelaisRefus.test_flux_anthropic` (second delta, `ping`), `test_delai_total_du_flux` ; d3a, d3b |
| **d-4** `CARTES-partiel.json` non rapatrié | corrigé | audit l. 35 | pièce permise | `EssaiABlanc.test_part_atteinte_arret_et_releve_partiel` ; d4 |
| **d-5** refus du scénario factice après la création du dossier | corrigé | lanceur l. 200 | dans `exiger_mode_reel`, avant tout dossier | `EssaiABlanc.test_mode_reel_options_et_scenario`, `ModeReelBoutEnBout.test_artefact_scenario` (aucun dossier) ; V28 |
| **d-6** huit chiffres quelconques passent pour une date | corrigé | commande l. 71, l. 104-124 | le suffixe doit être une **date réelle** (années 2000 à 2099) | `Commande.test_modele_servi_m1` (six refus neufs dont `-99999999`, `-20261301`, `-2026-02-30`, `-20250229` ; deux admis neufs dont `-20240229`) ; d6, M38 |
| **d-7** une loi compilée ou une graine dans un fichier au nom permis serait copiée | corrigé | audit l. 38-41, l. 89-126 ; lanceur l. 471-475, l. 552-555 | refusés : clés de devis et de graine (`"spec_sha256"`, `"loi_vraie"`, `"graine"`, `"secret"`, `"phrase"`), entier décimal ≥ 2⁶⁴ (forme des graines des mondes), **loi compilée d'un monde** (JSON canonique égal, cherché dans chaque objet JSON ou JSONL) quand `rapatrier --mondes M --mondes-sha256 H` est donné | `EssaiABlanc.test_rapatriement` (sain, lois cherchées), `test_rapatriement_artefacts` (« devis », « graine », « loi_compilee », ligne de commande ; un entier sous 2⁶⁴ et des chiffres dans une empreinte admis) ; d7a à d7d |
| **d-8** pire cas de la sonde 7,98 et non 7,97 | corrigé ici | ce rapport, section 10 | le rapport v69 n'est pas réécrit (R12) ; chiffres justes : **7,975968 USD** à la borne gelée, **8,052896 USD** avec la borne courte | `Configuration.test_sain` (8,052896 recalculé) |
| point **(7)** la doublure ne se signale pas | durci | lanceur l. 243-245, l. 457, l. 466 | en mode réel sur une adresse d'amont de la boucle locale, le manifeste et le relevé disent `reel_sur_doublure` ; `lire` recopie le mode et `amont_boucle_locale` | `ModeReelBoutEnBout.test_sain_bout_en_bout`, `EssaiABlanc.test_lecture` ; p7a, p7b |

## 4. Refus et écarts écrits

1. **D-4, où vit l'empreinte du relevé de la sonde.** La contre-lecture proposait un champ de la configuration. **Écart** : c'est
   une ligne du bloc gelé que rend `bloc --releve-sonde RELEVE` (« releve-de-la-sonde <sha256> »), et que le mode réel recalcule
   avec le relevé qu'on lui passe. Raison : un champ de la configuration ne peut être rempli qu'après la sonde ; R12 interdit de
   réécrire la configuration v11 ; il faudrait une configuration v12 **et** un code v71 (le nom de la configuration est au lanceur
   et au bloc) même quand la sonde confirme tout. La garantie demandée tient : l'empreinte du relevé est au bloc, donc au texte
   scellé, et le mode réel refuse sans ce relevé, avec un autre, ou avec un relevé qui ne confirme pas la configuration. Si la sonde
   **dément** la configuration (règle de comptage, identifiant, borne, en-tête d'espace de travail), le mode réel refuse : une
   configuration v12 (et le code qui la nomme) devient nécessaire — décision de la mère.
2. **D-2 (b), valeur de la règle avant la sonde.** Je n'ai pas laissé la règle « inconnue » : la v11 porte des valeurs écrites
   **de mémoire, d'après la documentation des fournisseurs, non vérifiées** (dit dans `sources` et au bloc), et le mode réel ne
   part pas tant que la sonde ne les a pas confirmées. Ainsi aucune réponse rendue sous la borne ne devient un échec sous une
   règle non tranchée : à blanc, la doublure suit la règle ; dans la sonde, les champs bruts sont relevés et le verdict tiré
   d'eux, sans rien jeter. Si la mère préfère une configuration à règle nulle jusqu'à la sonde, c'est une v12 après la sonde.
3. **Prix.** La sonde calcule le coût de chaque appel aux prix de la configuration ; elle ne lit pas la console : le
   rapprochement des prix reste à Lazar, **hors du code** (le relevé le dit : `a_lire_hors_du_code`). Le plafond n'est dur que si
   les prix sont les vrais : à écrire au texte.
4. **m-8 et m-14** (refus de la v69, jugés fondés par la contre-lecture) : hors de ce mandat, inchangés ; restent à dire à Lazar
   (risque de P-0 sur une erreur passagère ; `secondes_de_chaine` dans la sortie scellée).

## 5. Gardes neuves (R5) : cas sain, artefact, mutation tuée

| garde neuve | cas sain | artefact | mutations tuées |
|---|---|---|---|
| règle des graines écrite = règle employée (D-1) | `RegleDesGraines.test_sain` ; `test_regle_des_graines_redonne_les_episodes` | texte au bloc d'étiquette v68 (`BlocGele.test_artefacts`) | D1a à D1e |
| coût au-dessus du pire cas → arrêt du pilote, l'appel au relevé, jamais d'abandon (D-2) | « k1_plus » et « reflexion_longue » complets | « cout_excessif » → `ArretPilote` (adaptateur et lanceur) | D2a, D2b, D2o, N6 |
| verrou du relais (D-2) | quatre appels complets puis 429 (`test_appels_modele_non_branche`) | 409 au second appel après un coût excessif | D2g, D2h |
| règle de comptage et verrou contrôlés à l'état du relais (D-2) | `EtatDesRelais.test_sain` | règle contraire ; verrou levé | D2i, D2j |
| règle de comptage booléenne, Claude « comprise » (configuration, commande, relais) (D-2) | `Configuration.test_sain` ; tous les appels d'essai | « reflexion_non_booleenne », « claude_non_comprise » ; `non` → code 2 (commande), sortie 2 (relais) | D2k, D2l, D2m, D2n |
| lecture de l'usage selon la règle (commande et relais) (D-2) | `Commande.test_dialectes` (deux règles par dialecte) ; écarts de coût nuls | réflexion toujours ajoutée, pensées ignorées (mutations) | D2c, D2d, D2e, D2f |
| `mesurer` : fichier et mondes du manifeste (D-3) | `test_mesure_une_fois` | autres mondes (X9) ; manifeste aux mondes changés | D3a, D3b |
| `lire` : mondes mesurés et manifeste liés (D-3) | `test_lecture` | « mondes » ; manifeste refait | D3c, D3d |
| relevé de la sonde exigé en mode réel, cité par le bloc du texte (D-4) | `test_sain_bout_en_bout` | option absente ; fichier introuvable ; texte scellé avant la sonde | D4a, D4b, D4c |
| relevé : compagnon, complet, borne courte, mêmes pièces, même identité (D-4) | `test_sain_sonde` | altéré ; « partiel » ; « sans_borne_courte » ; sonde sans `--borne-courte` ; « pieces » ; « identite » ; « version » ; « appel_manquant » | D4d, D4e, D4f, D4g |
| conclusions recalculées des champs bruts, toutes exigées, verdict = règle, borne tenue (D-4) | `test_sain_sonde` | « conclusions_forgees » ; « flux », « pas_tronque » ; « verdict » ; « borne_tenue » | D4h, D4i, D4j, D4k |
| flux de Claude relu indépendamment et comparé (D-4) | `SondeFonctions.test_flux_relu_et_compare` | texte, raison, usage absent du delta, flux illisible | D4l |
| verdicts sur la réflexion (Argon par le total, Astra par le seuil) (D-4) | `test_verdicts` | cas indéterminés et contradictoires | D4m, D4n |
| lignes de GO de la sonde (D-4) | `test_go_sonde` ; `test_sain_sonde` | GO absente, montant faux, périmètre, identifiants égaux | D4o |
| section `sonde` de la configuration (D-4) | `Configuration.test_sain` | 9 artefacts (part sous le pire cas, consigne > 100 octets, octets, borne courte, somme, lignes, proposeur, périmètre, section absente) | D4p, D4q |
| relais de la sonde : plafond de la sonde, deux appels (D-4) | `test_sain_sonde` ; `test_sonde_plafond_et_appels` | état au plafond et au nombre d'appels du pilote | D4r, D4s |
| borne plus courte dans ]0 ; borne gelée] seulement (D-4) | appel à 256 jetons (sonde) | 36 001, 0, 25,5 → refus avant tout appel | D4t |
| noms de l'environnement du relais (W1) | `test_environnement_du_relais_w1` ; relais du mode réel et de la sonde | 4 noms étrangers | W1, W1b, W1c |
| engagement lié au fichier des mondes (W2) | `test_sain_bout_en_bout` | autre fichier des mondes, engagement du vrai copié | W2 |
| témoin : consigne de la commande, session neuve (W3) | `test_conditions_du_temoin` | chaque condition seule fausse | W3, W3b, N7 |
| texte servi : gabarit, monde public (W4) | `M6TexteEtEpisodes.test_sain` | « gabarit », « monde_public » | W4, W4b |
| `mesurer` : manifeste égal à son compagnon (W5) | `test_mesure_une_fois` | manifeste altéré, compagnon gardé | W5 |
| délai de l'adaptateur compté au plafond de session (d-2) | appels complets comptés à l'usage | commande tuée par le délai | d2 |
| raison d'arrêt jamais effacée ; délai total du flux (d-3) | `test_flux_anthropic` ; horloge sous l'échéance | second delta sans raison ; horloge au-delà | d3a, d3b |
| `CARTES-partiel.json` rapatrié (d-4) | `test_rapatriement` | arrêt sur la part | d4 |
| scénario factice refusé avant le dossier (d-5) | mode réel sans scénario (`test_sain_bout_en_bout`) | scénario donné, toutes options présentes | V28 |
| suffixe de date réelle (d-6) | 7 admis | 14 refusés | d6, M38 |
| rapatriement : devis, graine, loi compilée ; lois passées par la commande (d-7) | `test_rapatriement` (lois cherchées) | « devis », « graine », « loi_compilee », ligne de commande | d7a à d7d |
| mode « réel sur doublure », recopié par `lire` (7) | `test_sain_bout_en_bout` ; `test_lecture` | (mutations) | p7a, p7b |

## 6. Essais

`essais/test_pilote_mr2_v70.py`, tête `932a5ff` : **109 passés, 166 sous-essais passés, en 223,71 s** (21:21:11 → 21:24:55 ;
journal `essais-pilote-v70-v2.txt`, `2b997eb6…`). Au jalon 2 (même code, un motif d'essai moins exact) : 109 passés, 166
sous-essais, 229,38 s (18:43:56 → 18:47:46 ; `essais-pilote-v70.txt`, `7801c83f…`, gardé). Les 88 essais de la v69 sont portés (renommés, deux ajustés au comportement voulu : `test_cout_excessif_cause`
devient `test_cout_excessif_arret`, l'abandon sur coût excessif étant retiré ; `test_etats_et_abandons` sans `cout_excessif`) ;
21 essais neufs (`test_go_sonde`, `test_conditions_du_temoin`, `test_borne_de_la_sonde`, `test_sonde_plafond_et_appels`,
`test_environnement_du_relais_w1`, `test_delai_total_du_flux`, `test_regle_des_graines_redonne_les_episodes`,
`test_mesure_manifeste_altere_w5`, `test_mesure_manifeste_mondes_d3`, `test_mesure_autres_mondes_d3`,
`test_cout_excessif_arret_du_pilote`, `test_sain_sonde`, `test_artefact_engagement_autre_fichier_des_mondes_w2`,
`test_artefact_releve_absent`, `test_artefact_texte_scelle_sans_releve`, `test_artefacts_releve`, `test_artefacts_sonde`, et
les classes `RegleDesGraines` (1) et `SondeFonctions` (3)) ; d'autres renforcés (sous-essais neufs). Mondes : publics
(`pilote-v68-essai-developpement` 1 à 4 ; `pilote-v2-essai-developpement` pour C-16, D-3 et W2). La doublure des fournisseurs sert
aussi la sonde (« OK » à la borne gelée, texte coupé à 256 jetons, réflexion comptée selon la règle ; flux de Claude avec `ping`).

## 7. Banc de mutations

`essais/mutations_pilote_mr2_v70.py` : **152 mutations** — les 88 de la v69 portées au code v70 (43 du banc v68, 10 des deux
contre-lectures de la v68, 35 gardes de la v69 ; textes ajustés là où le code a changé : M25, M33, M34, M38, N4a, N6, V12, V13, V15,
V18, V28), les **cinq du contre-lecteur du différentiel v68 → v69 (W1 à W5), recopiées mot pour mot**, et **59 neuves** (D1a à
D1e, D2a à D2o, D3a à D3d, D4a à D4t, W1b, W1c, W3b, W4b, d2, d3a, d3b, d4, d6, d7a à d7d, p7a, p7b). Copie neuve
d'`orchestrator/` par mutation, un remplacement présent une seule fois (contrôle à sec : aucun défaut), empreintes de la commande
et du relais recopiées dans la configuration de la copie quand l'un d'eux est muté ; « tuée » seulement si l'essai attendu échoue ;
essais sains d'abord sur la copie non mutée. Sélection de chaque mutation resserrée sur son essai attendu (`selection_effective`).

| passage | mutations | heures (`date -u`) | essais sains sur la copie non mutée | bilan |
|---|---|---|---|---|
| 1 | les 88 portées (M01 à M43, N1 à N8, V01 à V35) | 19:30:18 → 20:33:37 | code 0, aucun échec | **88 tuées pour la raison attendue** |
| 2 | W1 à W5 et les 59 neuves | 20:33:50 → 21:20:56 | code 0, aucun échec | **64 tuées pour la raison attendue** |

**152 sur 152 tuées pour la raison attendue**, sur le code gelé de la tête `932a5ff` (le même que celui du bloc gelé). Pièces :
`mutations-pilote-v70.json` (`b8935377…`, fusion des deux passages par mon outil, mutations dans l'ordre du banc, bilan d'ensemble),
`mutations-pilote-v70-passage-1.json` (`eeb6b544…`), `…-passage-2.json` (`9afb8ea7…`) et leurs journaux. Les cinq mutations du
contre-lecteur meurent par l'essai écrit pour elles : W1 par `test_environnement_du_relais_w1`, W2 par
`test_artefact_engagement_autre_fichier_des_mondes_w2`, W3 par `test_artefacts_temoin_un_par_un`, W4 par `test_artefacts_texte`, W5
par `test_mesure_manifeste_altere_w5` ; M23 (survivante du passage tué) meurt par `Configuration.test_artefacts`. Réserve de
méthode : chaque mutation n'est jugée que sur la classe et l'essai attendus (pas sur la suite entière, comme le faisait le
contre-lecteur pour W1 à W5) ; une mutation tuée ici l'est aussi par la suite entière, l'inverse n'est pas éprouvé.

**Passages qui ne comptent pas, dits** : (1) 18:48:37, arrêté par moi vers 18:49 (disque plein, section 14), aucune mutation
jouée ; (2) 18:51:50, **tué par la limite de 30 minutes des tâches de fond** (je n'avais pas donné de délai) après 29 mutations :
28 tuées pour la raison attendue et **une survivante, M23** (borne de sortie au-delà de ce que paie le plafond de session) : l'essai
`Configuration.test_artefacts` attendait le motif « pire cas », que le refus neuf de la section `sonde` dit aussi (la part de la
sonde sous le pire cas d'une borne d'un million de jetons) ; motif rendu exact (« borne de sortie »), jalon 3 (`932a5ff`), et les
sélections resserrées sur l'essai attendu pour tenir sous deux heures en deux passages. Journaux versés
(`mutations-pilote-v70-journal-passage-tue.txt`). Aucun code gelé n'a changé entre ces passages et le banc complet.

## 8. Différentiel v69 → v70, paquet, patch

- **`differentiel-v69-v70-v2.patch`** (`ce225d6e1ba002efc805c164d44b806a3d721c7d0125e4692f2bd996f08b137c`, 3 766 lignes,
  10 en-têtes ; celui de la tête `932a5ff`) : `git diff --no-index --no-color` de chaque paire, lancé depuis `orchestrator/`, dans
  cet ordre : cœur, proposeurs, audit, **sonde contre `/dev/null`** (module neuf), lanceur, commande, relais, configuration
  v10 → v11, essais, banc. Recalcul : `git -c core.quotepath=off diff --no-index --no-color A B` pour chaque paire, sorties mises
  bout à bout. Le différentiel du jalon 2 (`differentiel-v69-v70.patch`, `b47d2943…`, gardé, R12) ne diffère que par les paires
  des essais (un motif) et du banc (sélections resserrées) : le code est le même.
- Paquet `organisme-v70-pilote-mr2-v1.bundle` (`838ddd2c51ee5cf72ec3f0b874d6d8ada26528b2d3cd10d1c6b158a05488cac8`) : branche `prep/organisme-v70-pilote-mr2-v1`, tête
  `932a5ffc2459c4cd5bb1dc45e9102af8078274bb`, **prérequis `2ca17ea3243979837890e1243876299a202b7748`** (tête v69) ; commits v70 `9613640` (jalon 1 : code, configuration v11, essais), `49015da` (jalon 2 : banc, essais renforcés), `932a5ff` (jalon 3 : sélections du banc resserrées sur l'essai attendu, motif d'un essai rendu exact). Paquets de
  jalon gardés : `organisme-v70-pilote-mr2-jalon1.bundle` (`e621eb6e…`, tête `9613640`) et `…-jalon2.bundle` (`e9026d63…`, tête
  `49015da`).
- Patch `organisme-v70-contre-2ca17ea.patch` (`c84f5d3f8fad64c582e9925f75ad7df6659e0942b869bdbba05060e58941a80d`, trois commits) : `git format-patch --stdout 2ca17ea..prep/organisme-v70-pilote-mr2-v1`.
- Ajouts seulement : `git diff --name-status 2ca17ea <tête>` : dix « A » (neuf fichiers au nom v70 et le module neuf de la sonde) ; aucun fichier de la v69 ni d'avant n'est modifié.

## 9. Bloc gelé et marqueurs

- **Bloc gelé** : `EMPREINTES-code-pilote-v70.txt` (`16a368b688269d7c1cc2f86d656f546cbd76432e8dc2d5ae2c9047917aab4a66`), 45 lignes,
  marqueurs `<!-- empreintes-du-code-pilote-v70 : début/fin -->` ; rendu par `bloc` (sans relevé) sur le code du jalon 2 et
  revérifié égal à l'octet en fin de travail. **Provisoire** : sa ligne « releve-de-la-sonde absent (le mode réel le refuse) »
  sera remplacée par l'empreinte du relevé (`bloc --releve-sonde`), qui seule peut être recopiée au texte scellé. Il porte :
  gabarit servi, bornes, plafonds, parts, réglages envoyés et **règle de comptage de la réflexion** par proposeur, lignes π1
  (20,00) et π2 (21,72), **lignes de la sonde s1 (4,39) et s2 (3,68)**, octets d'entrée, numpy exigé (2.5.3), **règle des graines
  des épisodes** (D-1), relevé de la sonde, et 28 empreintes de fichiers : les 7 fichiers du pilote au nom v70 (lanceur, cœur,
  proposeurs, audit, commande, relais, configuration v11 `9240c624…`), le module neuf de la sonde, les 7 modules de l'arbre
  inchangés depuis la v69 et les 13 outils portés inchangés.
- **[GABARIT-SHA256]** : `e77d3041f7815b2c0579cbafdb2898ca8569fe61e6cb51b99a41c3724fc456a2` (inchangé depuis la v69 : la consigne
  servie ne change pas).
- **Bornes, plafonds, parts, lignes π1 et π2, réglages d'effort, octets** : inchangés depuis la v69 (64 000 / 89 000 / 36 000 /
  36 000 ; 3,00 / 2,00 / 2,34 / 2,34 ; 12 / 8 / 9,36 / 9,36 ; π1 20,00 ; π2 21,72 ; total au pire 41,72 USD).
- **[CHAMPS-ASTRA]** : `usage.prompt_tokens`, `completion_tokens` (réflexion **comprise**, règle gelée de la v11, à confirmer par
  la sonde), `completion_tokens_details.reasoning_tokens` (relevé, non ajouté), `finish_reason`, `message.refusal`.
- **Identifiant et prix d'Astra** : `gpt-6-astra` ; 10 / 50 USD par million (barème prudent du collisionneur, supposé) — prix à
  rapprocher de la console par Lazar après la sonde.
- **Voie d'accès aux crédits de Claude** : inchangée depuis la v69 (clé nommée `RR_ANTHROPIC_API_KEY_RIGAUD`, interface Messages,
  en flux, sans repli ; aucun en-tête d'espace configuré — la sonde dira s'il en faut un).

## 10. La sonde : sous-commande, pire cas, lignes de GO proposées, ordre

**Ligne de commande** (le lanceur de l'arbre gelé ; les trois clés exportées dans l'environnement **par leur nom** seulement,
`RR_ANTHROPIC_API_KEY_RIGAUD`, `GEMINI_API_KEY`, `OPENAI_API_KEY` ; aucune valeur sur la ligne de commande) :

```
python3 -I -B orchestrator/demonstrations/pilote_mr2_v70.py sonde --go-sonde-credits GO-… --go-sonde-hors GO-… \
    --registre-go registres/go.md --sortie DOSSIER_NEUF --borne-courte
python3 -I -B orchestrator/demonstrations/pilote_mr2_v70.py bloc --releve-sonde DOSSIER_NEUF/releve-sonde-pilote-v70.json
```

**Ce qu'elle fait** : configuration gelée de l'arbre seulement ; les deux lignes lues au montant **exact** (4,39 et 3,68) avec les
mots de leur périmètre (« sonde » et « crédits de Claude » ; « sonde » et « hors crédits ») ; dossier de sortie neuf ; quatre
relais lancés par le lanceur (appelant = dialecte, clé passée par son nom au seul relais, environnement filtré, plafond = part de
la sonde, deux appels au plus), leur état contrôlé champ par champ (noms de l'environnement compris) ; par relais, par la chaîne
du pilote (adaptateur → commande → relais → amont ; réponse brute, corps du relais et témoin scellés) : « Réponds par le seul mot
OK. » (28 octets) à la borne gelée, puis « Écris un très long texte, de plusieurs milliers de mots, sur l'histoire de la
navigation. » (91 octets) à 256 jetons ; relais arrêtés par leur PID ; relevé `releve-sonde-pilote-v70.json` scellé (faits bruts
par appel, conclusions, identité des proposeurs, empreintes de la commande, du relais, de la configuration et du code, lignes de GO
lues, états des relais, consignes, dépense calculée). Tout arrêt (coût au-dessus du pire cas compris) laisse un relevé partiel,
que le mode réel refuse. Elle ne lit aucun monde, aucun résultat ; aucune machine n'est nécessaire.

**Ce que le relevé vérifie** (points de la section 6 de la contre-lecture) : statut ; identifiant servi exact (règle M-1 et d-6) ;
raison d'arrêt (complet à la borne gelée, tronqué à 256) ; champs d'usage présents et entiers ; bornes gelées admises (64 000,
89 000, 36 000, 36 000) ; `output_config.effort` admis sans en-tête bêta ; besoin d'un en-tête d'espace de travail (un statut 200
sans lui dit qu'il n'en faut pas ; sinon le statut est faux et le mode réel refuse) ; Fable 5.2 servi sur ce compte ; **flux réel
relu indépendamment et comparé au message que reconstitue `lire_flux_anthropic`** (identifiant, raison, texte, usage, événements
vus, usage final dans `message_delta`) ; **réflexion comprise ou non** (Astra : réponse d'un mot, `completion_tokens` ≥
`reasoning_tokens` et l'écart ≤ 32 → comprise ; `completion_tokens` ≤ 32 < `reasoning_tokens` → ajoutée ; Argon :
`totalTokenCount` = prompt + candidats + pensées → ajoutée, = prompt + candidats → comprise ; sinon indéterminé, et le mode réel
refuse) ; **réflexion tenue sous la borne courte** (sortie comptée par la règle ≤ 256 : le plafond est dur). Prix : le coût de
chaque appel est calculé aux prix de la configuration ; la console reste à lire par Lazar, hors du code.

**Pire cas** (consigne de 100 octets, le maximum que la configuration permet ; les consignes de la v11 font 28 et 91 octets) :

| | borne gelée | borne de 256 | somme | part (ligne) |
|---|---|---|---|---|
| Fable 5.2 | 2,568992 | 0,019232 | 2,588224 | 2,59 (s1) |
| Opus 5.5 | 1,784496 | 0,009616 | 1,794112 | 1,80 (s1) |
| Argon | 1,811240 | 0,024040 | 1,835280 | 1,84 (s2) |
| Astra | 1,811240 | 0,024040 | 1,835280 | 1,84 (s2) |
| **total** | **7,975968** | 0,076928 | **8,052896** | s1 **4,39** ; s2 **3,68** |

Soit 4,382336 au pire sur crédits de Claude et 3,670560 hors crédits (d-8 : 7,975968 et non 7,97 à la seule borne gelée).
Attendu : quelques centimes (réponses d'un mot et de 256 jetons ; la réflexion se paie).

**Lignes de GO proposées, mot pour mot, non inscrites** (nœud de Lazar ; leurs périmètres portent les mots que le code exige) :

```
| GO-AAAA-MM-JJ-NN (s1) | AAAA-MM-JJ | calcul | Pilote MR-2 : sonde des relais Fable 5.2 et Opus 5.5 sur crédits de Claude, avant le scellement du texte : par relais, un appel à la borne gelée (réponse d'un mot) et un à 256 jetons, consignes de 100 octets au plus, par la sous-commande « sonde » du lanceur v70 ; aucun monde, aucun résultat ; relevé scellé, cité au bloc gelé du texte ; prix rapprochés de la console par Lazar ; jamais de ligne d'extension ; arrêt par identifiant (R10) | 4.39 USD | AAAA-MM-JJ | Lazar | R-2548 ; mot de Lazar à recopier |
| GO-AAAA-MM-JJ-NN (s2) | AAAA-MM-JJ | calcul | Pilote MR-2 : sonde des relais Argon et Astra hors crédits, mêmes conditions que la ligne s1 | 3.68 USD | AAAA-MM-JJ | Lazar | R-2548 ; mot de Lazar à recopier |
```

**Limites, dites** : si un modèle ne réfléchit pas sur la consigne d'un mot ni sur la longue (réflexion nulle aux deux appels),
le verdict est « indéterminé » et le mode réel refuse (nœud : sonde à refaire avec une consigne qui fait réfléchir, donc une
configuration neuve) ; un relevé ne vaut que pour la configuration, la commande et le relais avec lesquels il a été fait (ses
conclusions gardées portent la règle de comptage du moment) : toute configuration neuve demande une sonde neuve ; les prix ne sont
pas vérifiés par le code.

**Ordre** : lignes s1 et s2 inscrites → `sonde --borne-courte` → relevé versé, scellé, cité → console lue par Lazar (prix) → si le
relevé confirme la configuration : `bloc --releve-sonde` → bloc recopié au texte (brouillon 5) → contre-lecture → scellement ;
s'il la dément (règle de comptage, identifiant, borne, en-tête d'espace) : nœud de la mère (configuration v12 et code qui la
nomme), le mode réel refusant de partir.

## 11. Ce que le texte doit changer avant le scellement

Section 6 du rapport v69, corrigée, et les sept manques du point (9) de la contre-lecture :

- **Faux, corrigé (D-1)** : la phrase de la graine des épisodes est la ligne `regle-des-graines-episodes` du bloc gelé, à
  recopier telle quelle : « épisodes de développement : SeedSequence(entier gros-boutiste des 16 premiers octets de sha256(UTF-8 de
  « pilote-mr2-v69|episodes-developpement| » suivi de l'empreinte sha256 du devis, en hexadécimal minuscule)) ; 400 instances par
  monde_riche_outils_v1.tirer_instances(rng, 400, dimension, sous_populations), puis les issues par tirer_issues(rng, probas(loi
  compilée, Z, G)), même générateur ». L'étiquette est celle de la v69 (épisodes et textes servis inchangés depuis la v69 ; plus
  « héritée de la v68 »).
- **(a)** Préalables : numpy 2.5.3 sur la machine (le mode réel le refuse sinon, bloc gelé).
- **(b)** Plan d'analyse, étape 2, et « Métrique » : la mesure se lance par `pilote_mr2_v70.py mesurer --sortie S --mondes M
  --mondes-sha256 H` (une seule fois, sur le fichier des mondes du manifeste, D-3), qui lance `mesure_pilote_v4.py mesurer` ;
  la lecture par `pilote_mr2_v70.py lire --sortie S --ecrire F`.
- **(c)** Ordre : **avant le scellement**, la sonde (section 10) et le bloc définitif (`bloc --releve-sonde`) ; après :
  lignes π1 et π2 → secret tiré (`secret`), engagé et poussé → phrase de Lazar → `generer --texte T --texte-sha256 H` (engagement
  des mondes au texte) → empreintes des mondes au registre → `preparer` (C-16, C-17) → essai à blanc sur la machine avec les
  vraies pièces → `jouer --mode reel … --mondes-shas … --registre-lancements FICHIER_HORS_DÉPÔT --releve-sonde RELEVE` →
  `mesurer` → `lire` → audit si déclenché → `rapatrier --mondes M --mondes-sha256 H` → destruction de la machine (R10).
- **(d)** Version du code citée : « code v70 gelé » (ligne P-2 des critères et ailleurs ; plus « v68 », ni « chaîne v67 »).
- **(e)** Isolement : un relais par proposeur, lancé par le lanceur, jeton du lancement, environnement filtré dont les noms sont
  contrôlés avant tout appel (W1).
- **(f)** Sonde : un préalable (« sonde des quatre relais faite, relevé scellé, son empreinte au bloc gelé ») et deux lignes du
  devis **hors des 41,72 USD** (s1 4,39 sur crédits de Claude ; s2 3,68 hors crédits ; 8,05 au pire, attendu quelques centimes).
- **(g)** Liste d'arrêt : « coût lu au-dessus du pire cas d'un appel → **arrêt du pilote** (relevé et manifeste partiels, l'appel
  au relevé, relais verrouillé), jamais un abandon » ; abandon d'un proposeur : panne du relais (délai de l'adaptateur compris,
  compté au plafond de session), modèle servi différent, usage absent ; refus du modèle et réponse illisible = échec sans
  abandon ; et le risque de P-0 sur une erreur passagère (m-8, aucune reprise).
- **Métrique** : la règle d'extraction (premier bloc ```json) ; « la sortie comptée suit la règle de comptage gelée par
  proposeur (`reflexion_comprise`, vérifiée par la sonde) » ; « le plafond n'est dur que si le fournisseur tient sa borne
  (vérifié par la sonde à 256 jetons) et si les prix sont les vrais (console lue par Lazar) ».
- Inchangés et justes : C-5, C-16, phrase sur l'effort, 41,72 USD (π1 20,00 ; π2 21,72), textes servis gardés pour l'audit R4,
  gabarit servi `e77d3041…`.

## 12. Essais à blanc A et B (par la ligne de commande)

Quatre mondes de développement publics régénérés (secret de 32 octets nuls, phrase « développement public, jamais pour un vrai
monde », empreinte de texte nulle ; fichier privé hors dépôt `687974573f18…`, **égal à celui de la v68**), configuration v11
gelée, relais à amont factice lancés par le lanceur, puis `mesurer` (deux fois), `lire --ecrire`, `relire`, `rapatrier --mondes
--mondes-sha256`, par la ligne de commande (`essais-a-blanc-pilote-v70.txt`, chemins locaux masqués) :

- **A, sain** (tous « k1_plus ») : 16 complets ; `CARTES.json` `d61dfc80…` (**égal à celui de la v68 et de la v69**) ; au
  manifeste, textes servis, épisodes, héritages, gabarit et C-17 **égaux à ceux de la v69** (D-1 : même étiquette, mêmes
  épisodes), C-16 sans `recrite` (d-1), règle des graines dite telle que le code l'emploie, `releve_sonde_sha256` nul (à blanc) ;
  mesure par `mesurer` (pièce `d3dc3ae9…`), second `mesurer` refusé (code 2) ; issue **P-2 avec réserve R-1** (témoin 0 sur 16 :
  proposeurs factices) ; 16 répondus, 32 refusées au gardien, 16 au-delà de six ; écarts de coût nuls ; mode `a_blanc`,
  `amont_boucle_locale` faux ; rapatriement, lois compilées cherchées : 112 copies, 6 laissés (`prive/`), aucun monde.
- **B, pannes mêlées** (Fable tronqué au monde 3, Opus copies de K1, Argon refus au monde 2 et illisible au monde 4, Astra en
  panne) : Astra abandonné au monde 1 (code 3) ; 10 complets, 1 tronqué, 5 échecs ; `CARTES.json` `66396fef…` (égal à la v69) ;
  issue **P-0** (9 répondus, minimum par monde 2) ; écarts de coût nuls ; rapatriement : 94 copies, aucun monde.
- Mode réel sans ses options : refus (code 2 ; options manquantes, `releve_sonde` compris), aucun dossier créé. `bloc` : le
  bloc provisoire (« relevé de la sonde absent »), égal à `EMPREINTES-code-pilote-v70.txt`.

Versés : `essai-a-blanc-v70/A/`, `essai-a-blanc-v70/B/` (rapatriés, sans monde ni texte servi ; les fichiers sans compagnon —
journaux des relais, liste du rapatriement — scellés au versement).

## 13. Ce qui reste avant le premier appel

Contre-lecture du différentiel v69 → v70 par un autre modèle que le mien (N-052) ; lignes s1 et s2 (Lazar) ; la sonde, son relevé
versé et les prix rapprochés de la console (Lazar) ; le bloc définitif (`bloc --releve-sonde`) ; brouillon 5 du texte (section 11)
et sa contre-lecture ; scellement ; lignes π1 (20,00) et π2 (21,72) ; puis l'ordre de la section 11. Pour la mère : l'arbre de
travail `/home/user/wt-pilote-v70` (2,7 Go, section 14) peut être retiré une fois la branche poussée.

## 14. Incident

Vers 18:49 (`date -u`), le volume de `/` (et de `/tmp/claude-0`) est tombé à 0 Mo libre (quota effectif d'environ 39 Go,
plein). Ma part : l'arbre de travail du dépôt de programme exigé par le mandat (2,7 Go, extrait entier) et les copies provisoires du
banc. J'ai arrêté mon premier passage du banc par l'identifiant de sa tâche (aucun processus resté, vérifié), supprimé ses seuls
dossiers provisoires par leur chemin (`…/pilote-v70-dev/tmp-essais/*`, mes copies d'`orchestrator/`), puis vérifié chaque pièce
écrite autour de l'événement : le différentiel copié à cet instant était **vide, avec un compagnon vide** ; les deux ont été retirés
et refaits, et tous les compagnons du dossier revérifiés (115, conformes) avant le jalon 2. L'espace est ensuite revenu (12 Go
libres à 18:51, libérés hors de mon fait). Rien d'autre n'a été supprimé ; aucun fichier d'une autre session touché.

## 15. Refus d'outil (tel quel)

Vers 20:34 (`date -u` : 20:33:41 avant), la commande qui versait un jalon 3 côté programme (paquet du jalon 3 de l'organisme, copie
et scellement de la sortie du passage 1 du banc et de deux journaux, commit local avec garde des secrets) a été refusée ; texte du
refus, tel quel :

> Permission for this command was denied by a built-in Claude Code safety check, not by the user. The check stops removals that
> can delete far more than intended: a system, home or workspace directory, or a target it cannot resolve, such as a shell variable
> that, if unset or empty, turns this into `rm -rf /` or `rm -rf /*`. Only a person may approve such a removal, and no person did
> (the permission prompt timed out, or none was shown). The command was NOT run; do not claim it succeeded. Do not work around the
> check by splitting, scripting, or re-issuing the removal through another tool or shell: the check exists because a removal like
> this can destroy the user's data, and getting past it would not make it safe. If the text below suggests a safe rewrite, run that
> instead; it goes through the same check. Otherwise finish the rest of the task without this removal, tell the user what you
> wanted to delete and why, and leave the removal to them. What was flagged: This command could not be checked for dangerous rm
> operations: the shell may read it differently than it was parsed. This requires explicit approval.

La commande ne contenait aucune suppression ; le contrôle n'a pas pu l'analyser (sous-commandes imbriquées). Elle n'a pas été
lancée (arbre de travail vérifié propre, tête `2de088e6`). Je ne l'ai pas reprise sous une autre forme : il n'y a pas de jalon 3
côté programme. Les pièces finales ont été versées ensuite, au commit final, par des commandes simples distinctes (création du
paquet final, copies, scellement, commit), sans suppression.
