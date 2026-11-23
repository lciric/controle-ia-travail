# Contre-lecture — additif 2-A à l'ordre de la course et devis de la voie (A) du saboteur à budget, organisme retenu v5 — cl1

Date : 2026-11-22. Classe A. Contre-lecteur neuf : Claude Opus 5.5 (n'a rien écrit de ces pièces). Rien dépensé, aucun loueur, aucun modèle externe, rien poussé. Aucune consigne privée, aucune sortie de mesure, aucune branche `essai/*` ou `donnees/*` ouverte, aucune pièce côté sondes.

## Verdict

**Non scellable tel quel ; scellable après corrections** (une version neuve, brouillon 2, puis vérification des corrections par moi). Deux bloquants : (B1) la ligne de dépense est fausse depuis l'inscription de `GO-2026-11-22-75`, et tout le chiffrage du devis en dépend ; (B2) l'essai de vitesse que l'additif exige n'existe pas dans le code. Le reste est juste, tracé et rejoué à l'identique.

## Pièces lues et vérifiées

- Commit `9e48622c264680059c3373de7bd52c569a2683e0` (branche `claude/iib-executante-v5-fable-additif-c`) : additif `7cef2bda410de2dea0d467eeb891c04c22942db603165327054ebe85bf74537d`, devis `12dd845cb700c83388a0705c41d029069edbb769ddc9e6b7b8f4bcedbf86aca6`, note `e2d63c20c1be82fb…`, calcul `557a83fa…`, sortie `b1a21a35…`, vérification `e9188fd0…`, sa sortie `43e433d5…` : empreintes conformes.
- **Rejeux sur processeur** : `calcul-devis-voies-A-B-v1.py` rend une sortie **identique octet pour octet** à `sortie-calcul-devis-voies-A-B-v1.txt`. `verifier-gardes-du-lanceur-v1.sh`, au commit `43d6d0673…` et sur `registres/go.md` de `origin/main` (tête `187f4c41b4a8bcf7c2c4d6206836e6b61858f5c9`, registre `3db30eb98fed1488934cb53466f058510521b606dd8fd3fe1f84a5c06cb56b19`) : sortie identique, en dehors de la ligne d'en-tête (empreinte du registre).
- Code à la tête `6696aca1fc57df7e4d5d3a26b3f25dd05d0d4f58` (arbre `725f3d5884c3617065aa913d04e9b3eee0e2afac`, branche locale `prep/iib-tirage-carte-local`) ; correctif 0020 `fd2e2d37…`, correctif 0021 `b80938ab…` ; rapports v4 `0678ab7a…` et v5 `53f476a5…` ; contre-lecture du correctif 0020 `90f6ac3c…` (« acceptable, aucun bloquant ») ; constat du lanceur `af52f2aa…`.

## Bloquants

**B1. Ligne de dépense : la mère a raison ; l'additif doit citer `GO-2026-11-22-75`.**
- Fait du registre. `GO-2026-11-22-75` (inscrite à 14:52:17Z) : « voie (A) … **dépense neuve, distincte de GO-2026-11-21-70** », plafond « 60 USD », échéance 2026-11-30, type « calcul », voie (B) gardée pour plus tard. Le rédacteur a lu `main` à `17082d49…` (registre `dc24a69f…`). Cette tête ne porte pas cette ligne : il ne pouvait pas la voir. `GO-2026-11-22-73` dit aussi : « saboteur (A), code corrigé : environ 27 USD. go » et « recharge automatique activée chez Vast ».
- Fait du code, rejoué au code de la tête `6696aca1f` :
  - `session_v5 go … GO-2026-11-22-75 55 0` : code 0 (« 55 + 0 = 55 ≤ 60 ») ; antérieure 5 : code 0 ; antérieure 5,01 : code 1 (`session_v12.verifier_plafond_epreuve`, l. 65–79) ;
  - `plafond-ligne` : 60, lu par `session_v3._plafond_ligne`, l. 30–36, forme « N USD » ;
  - `calendrier` sur une configuration à `go_id` = `GO-2026-11-22-75` : code 0 le 2026-11-26 (`fin_go_utc_s=1796083200`), refus le 2026-11-27 ;
  - `variante` : « B conforme à la ligne (60 USD) » ; `config` : « configuration v5 conforme ».
  - Aucun identifiant de ligne n'est écrit en dur dans le code : `GO-2026-11-21-70` n'apparaît que dans un commentaire de `session_v5.py`.
- Le lanceur (`lancer_iib_v3.sh`, l. 237 et 289) appelle donc `go` sans erreur sur la ligne neuve. Il exige en plus que le `registres/go.md` du commit de lancement porte la ligne. La phrase de C1, « Seule `GO-2026-11-21-70` passe ces contrôles », est fausse. Citer `GO-2026-11-21-70` imputerait la dépense neuve à une ligne qui la dit distincte, et dont 16,22 USD sont déjà dépensés.
- **Ce que l'additif doit écrire** :
  - C1 : l'accord de la voie (A) est `GO-2026-11-22-75`, avec `GO-2026-11-22-71` et `-73` ; les machines citent `GO_ID=GO-2026-11-22-75` ;
  - **configuration neuve** : `go_id` = `GO-2026-11-22-75`, ce qui fait **sept** points d'écart à la configuration scellée, et non six ; l'entropie est tirée par la mère au scellement ;
  - le commit de lancement porte le `registres/go.md` de `main` qui contient cette ligne ;
  - plafond **60 USD de dépense neuve**, coupure **55 USD**, égale au `plafond_usd` figé par `configuration_v5.DEVIS`, l. 87 ; les 16,22 USD et le stockage de 61875617 sont rapportés à part, hors du compte de la voie ;
  - le champ `<<LECTURE_DES_PLAFONDS_CONFIRMEE_PAR>>` est rempli par cette ligne même.
- **Conséquences à reporter** :
  - (a) **Fichier d'entrées** : la dépense passée vaut **0 + dépense relevée de l'essai** ; l'« écriture de 13 USD » disparaît, car 45 = 55 − 10, la réserve du devis scellé ;
  - (b) **Échéance des machines** : `heures permises = (55 − compte − 2) / 1,38` ; la minuterie va **au plus tard au 2026-11-30T22:00:00Z (`1796076000`)**, celle de l'ordre scellé, et non plus au 2026-11-27T22:00Z ; aucune création à partir du 2026-11-27T00:00:00Z (inchangé ; le code refuse dès le 27) ;
  - (c) **Pire tenu** : 55 + 0,92 + 0,69 = **56,61 USD**, sous 60 ;
  - (d) **Seuil de l'essai** : recalculé par moi avec les fonctions du programme, coupure 55 et essai à 5,40 USD, le seuil devient environ 2,99 fois les durées du devis scellé. Il suffit donc que le chemin neuf soit au moins **1,77 fois** plus rapide que le rythme lent (au lieu de 2,80 à 3,06). Au facteur 3 : 25 tours projetés ;
  - (e) **Lignes caduques** : [L16] à [L20], [L23] à [L25], [L52] et [L54] sont à refaire, ainsi que [L18], [L40], [L50] et [L51], qui portent la lecture « total de la ligne ». Correction exacte : `calcul-devis-voies-A-B-v1.py` passe en **v2**, avec `PLAFOND_A = 60.0`, `COUPURE_A = 55.0`, `FIN_DE_VOIE_S = 1796076000`, et `depense_passee_de_A` passe à `45 − (55 − 10) + essai` ; sortie v2, et le devis et l'additif pointent vers ses lignes.
- **La borne de 5,00 USD reste**, même sous la ligne neuve. Le code figé (55 + dépense antérieure ≤ 60) refuse toute dépense antérieure au-delà de 5. Or le compte de la voie atteint environ 4 à 6 USD à l'étalonnage et 9 à 16 USD à la course. Garder C3 (déclaré `min(compte, 5.00)`, écart écrit, coupure tenue par l'échéance) en le nommant **écart déclaré** à la garde, ou bien appliquer la correction étroite du constat (point 1 : coupure effective = 60 − dépense antérieure, passée à `session_v3 depense`). Cette correction est de classe B et demande le mot de Lazar. Recommandation : garder C3, écart nommé (confiance moyenne).

**B2. L'essai de vitesse n'existe pas dans le code.**
- Aucune sous-commande « essai-de-vitesse » ni aucun script ou amorce de cet essai à la tête `6696aca1f` (recherche sur `src`, `scripts`, `tests`). Le rapport v5 le dit (N-T2 : « le premier lot de l'étalonnage rejoué le mesurera de fait »).
- Le champ `<<LANCEMENT_ESSAI_DE_VITESSE>>` ne peut donc pas être rempli, et le § 3.1 n'est pas exécutable.
- Correction : (i) commander à Opus 5.5 une sous-commande `essai-de-vitesse` (classe B, contre-lue). Elle écrit, par chemin et sans texte, les durées de génération par épisode et par action d'oracle et l'égalité des empreintes de jetons. Préfixe de graines `essai-de-vitesse/`. Elle est lancée par le lanceur de session sous `IIB_TIRAGE` ; ou bien (ii) récrire le § 3.1 pour que la règle `essai-de-vitesse` soit jouée sur les marques de progrès du premier lot de l'étalonnage rejoué, avec une liste de l'étalonnage **v7** qui porte `tests/test_tirage_carte_v1.py` (déterminisme sur la carte). Ce texte est à écrire par Fable, car c'est un critère de décision.
- Recommandation : (ii), parce qu'elle épargne une location et environ 4 à 6 USD ; mais les marques actuelles portent-elles les durées sans lire de sortie ? À vérifier avant de choisir. Sinon (i).

## Majeurs

- **M1. Le chemin de tirage n'est pas une clé de la configuration.** Le code le prend par la variable **`IIB_TIRAGE`**, `processeur` par défaut ou `carte` :
  - `lancer_iib_v3.sh` l. 83 la vérifie, et l. 322 la passe par `-e IIB_TIRAGE=$TIRAGE` ;
  - les amorces la vérifient (l. 207 et l. 225) et la passent par `--tirage` (l. 418 et l. 451) ;
  - `lanceur_v5.py` l. 849 la reçoit, et `exiger_meme_tirage` (l. 752–764) refuse une course qui ne tire pas comme son étalonnage.

  Corrections :
  - au § 3.2, retirer la ligne « clé du chemin de tirage » de la table (la configuration ne change pas pour le tirage) ;
  - aux § 3.4 et § 4.4, étape 1, ajouter `IIB_TIRAGE=carte` aux variables ;
  - au § 4.3, ajouter aux contrôles à blanc que la commande de création imprimée porte `-e IIB_TIRAGE=carte` ;
  - au § 5, ajouter un arrêt par identifiant si le journal de l'amorce (« TIRAGE=carte ») ou la marque de chargement (`tirage`) dit autre chose.

  Sans cela, un oubli fait tirer l'étalonnage par l'ancien chemin, le défaut, sans que rien ne le signale avant la course.
- **M2. Liste de la course.** Le § 4.2 cite `scripts/tests-cibles-iib-course-v5-v1.txt` ; le code de la voie emploie la **v2** (`035c9427…`, correctif 0020). Essais attendus : étalonnage **296** (liste v6), course **312** sur la carte (rapport v5). Corriger le § 4.2 et les nombres « 294 / 296 avant le correctif ».
- **M3. Exigence 4 du § 2, en partie seulement.** Le chemin est écrit au **résumé** (rattaché au manifeste par `ecrire_resultat`) et à la marque de chargement. Il ne l'est ni au manifeste lui-même ni à `arret.json` (étalonnage, l. 704–709 ; course, l. 821–826). Écrire « au résumé et à la marque de chargement », ou exiger un correctif qui l'ajoute à l'arrêt.
- **M4. Voie (B) gardée pour plus tard.** C'est ce que dit `GO-2026-11-22-75`. Sous ce mot, C2 (ordre des deux voies), C5 (« la première qui réussit ») et `<<SENS_DE_REUSSIT_CONFIRME_PAR>>` sont sans objet tant que (B) ne part pas. À écrire : « sans objet sous GO-2026-11-22-75 ; C5 rejoue au premier départ de (B) ». La définition des fins écrites d'avance (abouti, échec), elle, reste.
- **M5. Crédit.** La recharge automatique est active (`GO-2026-11-22-73`). Le devis, aux § 0 et § 4 (« Aucune création ne part sans recharge par Lazar »), et C7 doivent dire : crédit relu ≥ pire de la machine + 2 USD, ou recharge automatique constatée ; sinon nœud. Les montants « au-delà du crédit » restent rapportés.

## Mineurs

- m1. C2 dit « sans rapatriement vérifié, aucune destruction », alors que C3 écrit que la minuterie détruit à l'échéance après la consignation (code de l'amorce, l. 85–110, design scellé). Ajouter « sauf la minuterie de l'amorce (ordre scellé) ».
- m2. Les identifiants des correctifs : le code de la voie porte **0020 et 0021**. Les champs du § 2 et la table « Élément » doivent nommer les deux.
- m3. Dans C3, l'exemple « 34,78 heures, soit 48 USD » sera recalculé avec la coupure à 55 (l'épuisement à 5 USD déclarés est inchangé).
- m4. Le § 3.1 s'appuie sur `GO_ID=GO-2026-11-21-70` ; le remplacer par `GO-2026-11-22-75`.
- m5. Le devis, § 7, réserve 6 (« n'a pas lu le correctif ») : à mettre à jour, puisque 0020 et 0021 existent et sont lus ici.

## Règles gelées (R1 à R14)

Conformes, sous les corrections ci-dessus :
- la course est exploratoire (`PREREG_ABSENT=1`, R-522), sans préenregistrement, comme les courses précédentes de cette ligne ;
- le passage des conditions est unique et fait par programme ; le code refuse un second passage (correctif 0019) ;
- aucune lecture avant la désignation scellée (C6) ;
- tous les arrêts se font par identifiant (§ 5, R10) ;
- destruction seulement après le mot de la mère et le rapatriement vérifié, sous réserve de m1 ;
- graines par les clés scellées, avec le préfixe `course/` (correctif 0018, R9) ;
- une machine à la fois, vérifié : toute instance `iib`, arrêtée comprise, bloque la création (`session_v2`, l. 150–156) ; 61875617 doit disparaître d'abord.

Les chiffres du devis sont justes à la lecture « 44 USD ». Ils sont caducs sous B1.

## Exigences du § 2 contre le code (tête `6696aca1f`)

| exigence | constat |
|---|---|
| 1. chemin choisi explicitement | **oui** : `IIB_TIRAGE` et `--tirage`, défaut `processeur` (l'ancien) ; valeur inconnue refusée ; « carte » refusée en mode jouet (`modele_v5.exiger_tirage`) ; aucun repli d'un chemin à l'autre (le chemin est fixé à la construction du modèle) |
| 2. un seul chemin pour l'agent et le jumeau | **oui** : `iib/modele_tirage_carte_v1.ModeleTorchTirageCarte` (actions, suites en cache dupliqué, repli `prerempli_par_suite`) ; le distillateur de la course est bâti sur le même modèle ; `noter_rejeu_juges_v2` n'est pas raccordé, et l'organisme ne l'emploie pas |
| 3. même loi | **oui** : khi-deux à trois températures et le long d'une ligne ; artefact « bruit uniforme » refusé ; le contre-lecteur l'a vérifié de son côté |
| 4. graines et manifeste | graines par ligne inchangées (**oui**) ; chemin écrit au résumé et à la marque, **pas au manifeste ni à l'arrêt** (M3) |
| 5. reproductibilité | **oui** sur processeur ; l'essai sur la carte n'est que dans la liste de la course v2, pas dans la liste de l'étalonnage v6 |
| 6. rien d'autre ne change | **oui** selon les rapports v4 et v5 : seuls le harnais, `IIB_TIRAGE` et la commande de création changent |
| essai de vitesse | **absent** (B2) |

## Champs du § 6 : ce que j'ai trouvé

| champ | trouvé |
|---|---|
| `<<LECTURE_DES_PLAFONDS_CONFIRMEE_PAR>>` | `GO-2026-11-22-75` (60 USD de dépense neuve, distincte de `-21-70`) ; C1 est à récrire (B1) |
| `<<SENS_DE_REUSSIT_CONFIRME_PAR>>` | sans objet tant que (B) est gardée (M4) |
| `<<MOT_DE_LA_MERE_DESTRUCTION_61875617>>` | à donner par la mère. Le message du commit `336c971cf` de `main` porte « destruction refusée par la garde » : la mère vérifie d'abord la voie de destruction |
| `<<CORRECTIF_LANCEUR_PLUSIEURS_MACHINES>>` | « aucun » : le code bloque toute instance `iib` (constat, point 3) |
| `<<CORRECTIF_0020_CHEMIN_ET_EMPREINTE>>` | `registres/iib-executante/p1-code-course-v1/0020-…patch` `fd2e2d373a6747f6ebfb12341ac1b44eb225fd282af38f86a31eb1f2a0b1c9c4` **et** `0021-…patch` `b80938ab87241750b78740b02fd53eeca209231d6f5a9ce1b433da363dc04880` |
| `<<RAPPORT_0020_CHEMIN_ET_EMPREINTE>>` | `rapport-developpeur-course-v5-v4.md` `0678ab7ac0ff6ae2900735adfd73f82ec8679b93d0c45786137401ed4057e543` ; v5 (0021) `53f476a541cff1e11b8a910179f14f85e82c81c654fd1535651e7c06c2d1abb2` |
| `<<CONTRE_LECTURE_ET_VERIFICATION_0020>>` | contre-lecture `contre-lecture-tirage-carte-0020-cl1.md` `90f6ac3c949a7f5841b14b716cf68a0d6c6547d0344c0a3388cfa20f2de03f9a` ; **la vérification des corrections de 0021 par le même contre-lecteur manque** |
| `<<LEVEE_DES_EXIGENCES_0020>>` | **manque** : aucune note ne répond point par point au § 2 ; la table ci-dessus peut lui servir de base |
| `<<BRANCHE_CODE_VOIE_A>>` | `prep/iib-tirage-carte-local` est **locale**. Le lanceur exige `refs/remotes/origin/prep/…` (l. 228–229) : elle doit être poussée sous `prep/…` |
| `<<COMMIT_CODE_REVU_VOIE_A>>` / `<<ARBRE_CODE_VOIE_A>>` | `6696aca1fc57df7e4d5d3a26b3f25dd05d0d4f58` / `725f3d5884c3617065aa913d04e9b3eee0e2afac` (si la vérification de 0021 ne change rien) |
| `<<CLE_DU_CHEMIN_DE_TIRAGE>>` | variable `IIB_TIRAGE=carte`, et non une clé de la configuration (M1) |
| `<<EMPREINTES_AMORCES_ET_LISTES_VOIE_A>>` | amorce de l'étalonnage `3107480e6d34bb8f1c897fa29cea94ca278a86a01dd3008161477f1b9ef70931` ; amorce de la course `03962c29b04bfcbef6abf70cd2a92bb5806b61adcd3cef2e7ed892e11fd01f71` ; liste v6 `f78384553e789e0cd37a803fabacfaf145057be6c6a61b877b54b7e1de7c490d` ; liste de la course v2 `035c9427f9be8e509b493d28515567d2f99550dd74e0648289bd25c28c2babbf` ; lanceur v3 `4e3e95a0b8684c3b163d4b1930d87c0068942df49a17e794a24122db56b95bbd` |
| `<<TESTS_ATTENDUS_ETALONNAGE_VOIE_A>>` / `<<TESTS_ATTENDUS_COURSE_VOIE_A>>` | **296** / **312** sur la carte (311 réussis et 1 sauté sur processeur) |
| `<<LANCEMENT_ESSAI_DE_VITESSE>>` | **inexistant** (B2) |
| `<<ENTROPIE_VOIE_A>>` | à tirer par la mère au scellement, **avant l'essai de vitesse**, qui en tire sous `essai-de-vitesse/` |
| `<<INSTANCES_INTOUCHABLES>>` | à relever par l'exécutante à l'inventaire en champs filtrés |
