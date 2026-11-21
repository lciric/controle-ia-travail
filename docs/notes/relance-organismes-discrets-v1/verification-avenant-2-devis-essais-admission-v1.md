# Vérification de l'avenant 2 au devis des deux essais d'admission du bras A (plafond de sortie de Google à 65 536) — v1

- **Vérificateur** : Claude Opus 5.5, neuf, le 2026-11-21 vers 19:12, temps universel (`date -u`). Je n'ai écrit ni le devis, ni les avenants, ni le programme, ni leurs contre-lectures.
- **Objet** : `docs/notes/relance-organismes-discrets-v1/avenant-2-devis-essais-admission-plafond-google-65536-v1.md`, sha256 `5f84642a896da2440c76c2c51aecb027224b644dde98ee0bcd3c63e4fd53f497`, égale à son compagnon ; ses programmes `avenant-2-programmes-v1/` (`calc_av2.py` `83d296ef…`, `faire_av2.py` `b3d1952d…`, `verif_av2.py` `5422548f…`, chacun égal à son compagnon ; l'empreinte de `calc_av2.py` est celle que l'avenant cite). **Je ne les ai pas exécutés** : tous les chiffres ci-dessous viennent de mon propre programme (section 7).
- **Interdits tenus** : ceux du mandat du rédacteur (`mandat-redacteur-fable-avenant-2-plafond-65536-v1.md`, `55a08330…`, égale à son compagnon). Aucun réseau, aucun `git fetch`, aucune clé, aucun appel, rien scellé, rien committé.
- **Non scellée** : à sceller par la session.

## Verdict

**Engageable après corrections.** Les chiffres sont justes : plafonds, excès, pire cas, seuils et manques, recalculés indépendamment, tombent tous au centime ; les 98 citations des tableaux d'écarts sont exactes à la lettre, et « goreco » n'est remplacé que pour Google. Mais l'avenant est écrit sur la livraison 4 du programme et ignore la livraison 5 et la ligne GO-2026-11-21-74. Trois corrections de fond suivent :
1. il dit d'une réflexion au-delà de la borne « la lecture vaut », alors que le programme en fait un défaut qui arrête la file (correction 2) ;
2. il chiffre le versement sans tenir compte des 17,28 € déjà accordés par Lazar (correction 3) ;
3. il signale le dépassement du pire cas accepté, mais ne le pose pas en nœud de Lazar et ne donne aucun levier (correction 1).

**Aucune ligne de Google ne part avant le mot de Lazar sur le pire cas (décision 1) et sur le versement (décision 2).**

## 1. Chiffres recalculés (question 1)

Calcul indépendant en décimal exact (section 7). Entrées : prix de 3 et 15 USD par million de jetons, bornes d'entrée de 5 000 et 24 000 octets, corps de vérification de 160 octets (supposé), délais de relais de 2 690 et 890 secondes, débit déclaré de 200 jetons par seconde, taux lu dans le fichier XML du relevé (1.0990, fixage du 2026-11-20).

| grandeur | avenant 2 | recalcul | accord |
|---|---|---|---|
| réserve d'un envoi : file (appariement ; couverture) ; vérification | 0,999 ; 1,056 ; 0,984 | 0,99804 ; 1,05504 ; 0,98352 | oui |
| pire cas des 16 envois ; des 3 envois de vérification | 16,20 ; 2,96 | 16,19664 ; 2,95056 | oui |
| **plafond de la file du juge ; d'une vérification** | **16,50 ; 3,00** | 16,50 ; 3,00 (demi-dollar supérieur) | oui |
| excès d'un envoi : file ; vérification | 7,09 ; 1,69 | 7,08696 ; 1,68696 | oui |
| plafond et excès : vérification ; file | 4,69 ; 23,59 | 4,69 ; 23,59 | oui |
| file, neuf excès | 80,29 | 80,28264 | oui |
| **pire cas chez Google, deux vérifications, sans borne dure** | **89,67** | 89,67 au grain des lignes (2 × 4,69 + 80,29) ; 89,66 en valeur exacte (89,65656) | oui |
| régime prudent, ou supposition de la sonde tenue | 32,97 | 32,97 | oui |
| **seuil avant chaque vérification ; avant la file** | **28,28 ; 23,59** | 28,28 ; 23,59 | oui |
| taux diminué de 5 % | 1,04405 | 1,04405 | oui |
| crédit compté aujourd'hui (11,93 € ; 15,59 €) | 12,45 ; 16,27 | 12,45 ; 16,27 | oui |
| **solde à voir au pire, par projet ; manque** | **31,58 € ; 19,65 € et 15,99 €** | 31,58 € (qui comptent 32,97 USD ; 31,57 € n'en comptent que 32,96) ; 19,65 et 15,99 | oui |
| au plus juste (première vérification à 0,02) | 27,11 € ; 15,18 et 11,52 | 27,11 € ; 15,18 et 11,52 | oui |
| débit requis à 65 536 | 24,4 | 24,363 | oui |

Contrôle de mon programme : à 32 768, il redonne 8,50, 1,50, 7,58, 2,18, 16,08, 19,76 et 23,44. Un écart ancien apparaît. Le pire cas accepté de 84,06 venait d'un excès arrondi à 7,578. Arrondi vers le haut comme le veut la règle, il valait 84,07 (84,06328 en valeur exacte). Ce n'est pas un défaut de l'avenant 2, qui le dit (section 12, partie 1), mais la base de comparaison est inférieure d'un centime à sa propre règle.

**Pourquoi les seuils « des deux projets » diffèrent-ils ?** Ils ne diffèrent pas d'un projet à l'autre. 28,28 et 23,59 USD sont deux moments, appliqués **chacun aux deux projets** :
- 28,28 USD avant chaque vérification : une vérification (4,69) plus la file (23,59) ;
- 23,59 USD avant la file : son plafond plus un excès.

Ce qui diffère d'un projet à l'autre, c'est **le manque** : les soldes vus diffèrent de 3,66 €, et les manques aussi (19,65 et 15,99). Le seuil est exigé sur chaque projet, et la somme des deux dépenses est retirée de chaque solde, pour une raison : on ne sait pas quelle clé paie quel projet, ni si un seul projet les paie toutes les deux. Avant la seconde vérification et avant la file, le crédit requis vaut alors le seuil plus la dépense déjà retirée. Au pire, c'est 32,97 USD aux deux moments.

**Pourquoi OD-301 chiffre-t-il 22,40 € par projet (sous 32 768) ?** Deux différences, que l'avenant (3.4) décrit justement :
1. **La formule.** Le journal multiplie le besoin par 1,05 puis divise par le taux : 23,44 × 1,05 ÷ 1,0990 = 22,3949, soit 22,40 €. La règle de l'avenant 1, que le programme applique (`marge_de_change_note` du gabarit : montant × taux × (1 − marge), au centime inférieur), divise par 1,0990 × 0,95 : 23,44 ÷ 1,04405 = 22,4510, soit **22,46 €**. Diviser par 0,95, c'est multiplier par 1,0526, et non par 1,05.
2. **Le seuil d'une vérification.** Le journal compte 3,68 USD (3,52 €). La règle exige, avant chaque vérification, de couvrir aussi la file : 19,76 USD, soit 18,93 €.

**La règle du programme est la juste**, puisque c'est elle qui décide si une ligne part. **L'écart est de 0,06 € par projet** : 22,40 € ne comptent que 23,38 USD, sous les 23,44 exigés au pire. Même au plafond de 32 768, le versement chiffré par OD-301 laissait refuser la file au pire.

## 2. Le pire cas au-dessus des 84,06 USD acceptés (question 2)

**Ce que dit l'avenant.** Le dépassement est écrit en tête (point 2 de la section 0, « c'est à lui dire »), à la section 10 (point 1) et dans le texte de la ligne 4 (« les 84,06 USD acceptés sous ce GO sont dépassés de 5,61 USD »). **Il ne le nomme ni écart au GO-2026-11-21-68, ni nœud de Lazar.** Il ne propose aucun levier ; il signale seulement le régime prudent comme « fait neuf, que je signale sans rien proposer » (2.4). Or le texte de la ligne 4 serait alors accordé avec un dépassement connu d'un chiffre que Lazar a accepté nommément. Une dépense sans borne dure au-delà de ce que Lazar a accepté est un nœud. Le « go dépenses sur devis » de GO-2026-11-21-69 ne le couvre pas : GO-2026-11-21-68 fixe le chiffre (correction 1).

**Les leviers, sans changer le niveau de réflexion.** Cible : 84,06 USD. Formule : 2 × 4,69 + 16,50 + k × 7,08696, où k est le nombre d'envois de la file qui peuvent porter un excès.

| levier | ce qui change | pire cas chez Google | ce qu'il coûte | code |
|---|---|---|---|---|
| (a) **régime prudent imposé à la file** | tout envoi sans compteur lisible compté à 200 jetons par seconde de sa durée | **32,97** | la file s'arrête au second envoi coupé à 45 minutes, sur deux appels différents (aujourd'hui, sur un même appel seulement). À 16,50, la reprise après un premier envoi coupé part, si le cumul compté avant lui ne passe pas 7,30 USD : la raison qui faisait écarter ce régime (devis, ligne 346 ; avenant 1, ligne 163) tombe | changement de règle : le choix du régime dans le chef, essais sain et artefact (R5) |
| (b) **ordre et condition des lignes** | la file ne part que si la dépense comptée des deux vérifications ne passe pas **3,77 USD** (84,06 − 80,28264 = 3,77736) | ≤ 84,06 (au plus 84,05) | rien dans le cas attendu (0,04 USD). Une vérification avec un envoi coupé (2,68 comptés) passe encore ; deux bloquent la file, cas où la lecture de la console par Lazar est due de toute façon (garde 20) | une garde neuve d'avant la file, éprouvée |
| (c) **nombre d'excès borné** | la file s'arrête à son 8e envoi coupé (k = 8) ; à son 2e (k = 2) | 82,58 ; 40,06 | k = 8 : seule une file à huit envois coupés, tous repris, cesse de tenir, cas sans portée pratique. k = 2 : comme (a), sans le compte au débit | règle du compteur, éprouvée |
| (d) **délai de la file** | relais de 2 690 à **2 481 secondes** (délai total de 2 491 secondes) ; excès de 6,46 USD | 84,02 | débit requis de 26,5 jetons par seconde au lieu de 24,4 ; une lecture pleine plus lente est coupée plus tôt ; délai global de 45 336 secondes | **aucun** : valeurs `delais.total_s` et `delais.relais_total_s` de `lignes.file-neon` |
| délai des vérifications, seul | relais à 600 secondes ; même nul | 87,93 ; 86,29 | — | **insuffisant seul** |
| plafond de la file abaissé | 10,87 au plus | ≤ 84,06 | la garantie du devis (16,20 < plafond) tombe ; des lectures longues seraient refusées pour une raison de caisse | non recommandé |

Le levier (a) ramène le pire cas au chiffre sur lequel les seuils de crédit sont déjà calculés (23,59 et 28,28 couvrent le régime prudent) : la part « sans borne dure » disparaît, sous les suppositions du devis. Le levier (d) est le seul qui ne demande aucun code.

## 3. La borne de réflexion de 49 536, « supposée » (question 3)

**Le choix de la valeur est justifié ; le fait qu'elle affirme ne l'est pas.** 49 536 est la plus haute valeur que la garde admet (`chef_essais_admission_bras_a_v4.py`, `controler_la_configuration_de_google`, ligne 1434), donc l'affirmation la plus faible. La vérification de la livraison 5 la recommande pour cette raison (section 1 : « la borne doit être choisie haute »). Aucune pièce lue ne dit que la réflexion de `gemini-4-neon` au niveau `xhigh` reste sous 49 536 jetons : le « (S) » est honnête.

**Ce que l'avenant ne voit pas : la livraison 5 (C-2) éprouve la borne après chaque réponse.** `borne_dementie` (chef v4, lignes 1506 à 1512) compare `thoughtsTokenCount` à la borne :
- dans la file : défaut journalisé, l'envoi n'est ni jugé ni compté, la file s'arrête et ne tient pas (lignes 2608 à 2611) ;
- à une vérification : ligne 13 du classement, non saine, nœud de Lazar (lignes 2090 à 2092) ;
- à la sonde : une mesure.

La garde n'est donc pas « une soustraction » seule (section 4 de l'avenant). Son prix : un juge qui réfléchirait plus de 49 536 jetons échouerait pour un chiffre de configuration. Le paragraphe de l'avenant qui dit le contraire est à remplacer (correction 2).

**Ce qu'il faut relever, et où, sans appel payant :**
1. **Pièces déjà au dépôt, que l'avenant n'a pas ouvertes** (non opposables, provenance par transcription) :
   - `releve-api-mistral-gemini-essais-admission-v1.md` (`291341e2…`), ligne 18 : `maxOutputTokens` « caps combined thinking and output tokens for a response » ; mais « ces phrases visent `max_output_tokens` de l'API Interactions ; pour `generateContent`, confirmation directe non trouvée ». Si la pensée est comprise dans le plafond, 65 536 borne tout envoi, mais rien ne réserve 16 000 jetons au texte.
   - `juge-des-ancres-identifiant-gemini-v1.md`, ligne 15 : quatre niveaux, `xhigh` le plus haut, aucune borne en jetons.
2. **Pages à verser en PDF empreinté, page citée (R7)**, par un agent de lecture, sans clé ni dépense : `aistudio.google.com/docs/thinking`, `…/docs/whats-new-gemini-4-neon`, `…/docs/models/gemini-4-neon`, `…/api-reference/generate-content`. Quatre choses à y lire :
   - un maximum de jetons de pensée par niveau ;
   - si `thinkingBudget` est admis avec Neon, et son maximum : c'est l'option (a) de la confrontation, la seule vérifiable avant l'envoi ;
   - la limite de sortie du modèle ;
   - si `maxOutputTokens` de `generateContent` comprend la pensée.
3. **Premier constat de la ligne 2, gratuit** : `outputTokenLimit` rendu par l'appel de liste. S'il est sous 65 536, rien ne part.
4. **Aucune mesure au niveau `xhigh` n'existe** (devis, ligne 215). Sans appel payant, le relevé ne peut pas aller plus loin.

## 4. Citations et « goreco » (question 4)

- **98 citations** des tableaux 1.1 à 1.3 ont été confrontées par mon programme à la ligne citée : **aucun défaut**. J'ai aussi relu à la main les citations de 1.5, 3.4, 4 et 6 (devis 17, 95, 101, 162, 163, 215, 219, 346 ; confrontation 43, 45, 50, 77 ; avenant 1, 8, 163, 259, 327 ; note v3, 36, 51, 57, 64, 65, 89) : toutes exactes.
- **Listes de 1.4** : pour les 54 listes, les lignes listées portent bien le nombre. Les seules lignes qui portent le nombre sans être listées sont celles que l'avenant écarte en le déclarant (histoire : 315, 321, 424 ; Mistral : 169, 192, 200, 336, 350, 352, 353, 359, 368, 369, 545, 548, 585 ; corps de Mistral : 206).
- **« goreco »** (devis, lignes 34 à 37) est remplacé **pour Google seulement**. Mistral garde 32 768 jetons, ses bornes en octets, ses trois plafonds et la phrase de la ligne 3. La garde 3 fait de 65 536 un artefact chez Mistral. Conforme.

## 5. Texte des lignes et configuration (question 5)

**Le texte des lignes n'est pas citable tel quel.**
- Il porte un dépassement connu du GO-2026-11-21-68 (correction 1).
- Il ne dit pas l'arrêt sur une borne de réflexion démentie (correction 2).
- Son geste de paiement ignore le versement de GO-2026-11-21-74 (correction 3).
- Il lit la dépense retirée selon la règle de la livraison 4 (correction 4).

**La configuration est presque cohérente avec la livraison 5, mais le tableau de la section 9 ne nomme pas les champs réels du gabarit v4** (`configuration-essais-admission-bras-a-v4-gabarit.json`, `63a53802…`) et en omet plusieurs (correction 5). Deux points demandent du code, contrairement à « sans code neuf » de la vérification de la livraison 5 :
- **la garde 8 ne vérifie qu'un avenant** : `config["avenant"]`, chef lignes 491 et 1110 à 1118. Pour citer l'avenant 2 sans perdre l'avenant 1, il faut un champ de plus et sa garde ;
- **la forme neuve de la ligne de taux** (section 7 de l'avenant) n'est pas lue : `MOTIF_TAUX`, ligne 507, ne connaît que « heure du taux ».

**Deux questions que l'avenant laisse ouvertes, et que le programme tranche déjà :**
- **Limite de mots à la sonde** : `garde_google_avant_envoi` rend la main, pour le corps exact de la sonde, avant les contrôles (2) et (3) (lignes 1486 à 1497). L'exemption couvre donc les deux.
- **Échéance du GO de l'exemption** : seule la forme de `exemption_de_la_sonde_go` est contrôlée (ligne 1441), non son échéance. L'échéance contrôlée est celle du GO de chaque ligne de calcul (garde 8, ligne 479).

Des fichiers `_v5` du programme sont présents, non suivis (`git status`). Je ne les ai pas ouverts : la référence est la livraison 5 (fichiers `_v4`).

## 6. Corrections, avec le texte de remplacement exact

**Correction 1 — le pire cas, écart et nœud.**
- Section 0, point 2. Remplacer « Le chiffre accepté est dépassé de 5,61 USD : c'est à lui dire. » par : « Le chiffre accepté est dépassé de 5,61 USD : **c'est un écart au GO-2026-11-21-68 et un nœud de Lazar. Aucune ligne de Google ne part sur ce chiffre sans son mot, ou sans un levier qui le ramène sous 84,06 (section 10).** »
- Section 10, point 1. Remplacer « En valeurs exactes, l'écart est de 5,60 USD. » par : « Au grain des lignes, l'écart est de 5,61 USD (5,60 en valeurs exactes). C'est un nœud : décision, enjeu, options et leviers chiffrés à la vérification de cet avenant (`verification-avenant-2-devis-essais-admission-v1.md`, section 2 et décision 1). »
- Texte de la ligne 4. Remplacer « pire cas chez Google, pour les lignes 2, 4 et 6 telles qu'accordées, 89,67 USD ; les 84,06 USD acceptés sous ce GO sont dépassés de 5,61 USD ; » par l'une de deux formes :
  - si Lazar accepte le chiffre : « pire cas chez Google, pour les lignes 2, 4 et 6 telles qu'accordées, 89,67 USD, accepté par Lazar sous [identifiant du GO] ; » ;
  - sous le levier (a) : « la file est comptée au régime prudent, quelle que soit l'issue des sondes ; pire cas chez Google, pour les lignes 2, 4 et 6 telles qu'accordées, 32,97 USD, sous le chiffre accepté (GO-2026-11-21-68) ; ». Retirer alors de la même ligne : « et, quand elle part après deux sondes « comprises », sous la supposition que la borne se comporte à 65 536 comme à 256, faute de quoi jusqu'à neuf envois peuvent porter un excès (jusqu'à 80,29 USD pour la file au débit déclaré, plafond compté compris), que rien de dur ne borne, ».

**Correction 2 — la borne démentie.**
- Section 4. Remplacer tout le paragraphe qui commence par « **Si un envoi dépasse la borne et finit normalement** » par : « **Si un envoi dépasse la borne** — plus de 49 536 jetons de pensée facturés —, le programme de la livraison 5 en fait un défaut (C-2, `borne_dementie`). Dans la file : défaut journalisé, l'envoi n'est ni jugé ni compté parmi les réponses, la file s'arrête et ne tient pas. À une vérification : ligne 13 du classement, non saine, nœud de Lazar. À la sonde : une mesure. La borne est donc une déclaration éprouvée après chaque réponse. Son prix est qu'un juge qui réfléchit plus longtemps échoue pour un chiffre de configuration : c'est pourquoi elle est déclarée à la plus haute valeur admise. »
- Même section. Remplacer « elle n'arrête pas une réflexion plus longue que la borne. » par « elle n'empêche pas une réflexion plus longue que la borne ; le programme la constate après la réponse (C-2) et arrête la ligne. »
- Textes des lignes 2 et 4. Après « supposée et non relevée », insérer : « , éprouvée après chaque réponse : une réflexion facturée au-delà est un défaut, qui arrête la file sans qu'elle tienne, et rend une vérification non saine (nœud de Lazar) ».
- Section 9, point 8 (« Relevés et rapport »). Remplacer par : « 8. **Relevés et rapport** : déjà au programme (livraison 5, C-2 : `borne_de_reflexion_dementie` à la fiche, `bornes_de_reflexion_dementies` au relevé) ; rien à changer. »

**Correction 3 — le versement déjà accordé (GO-2026-11-21-74).**
- Section 3.3. Après le paragraphe « **Le manque dépend du taux** », ajouter : « **Le versement déjà accordé.** Lazar a accordé sous GO-2026-11-21-74 le versement de 10,47 € et de 6,81 € (17,28 €), chiffré par le journal (OD-301) pour le plafond de 32 768. S'il est fait, chaque projet montre 22,40 €. Il en faut 31,58 : il reste **9,18 € à verser sur chaque projet, 18,36 € en tout**, ce qui demande un mot de paiement de plus. Même à 32 768, 22,40 € ne comptaient que 23,38 USD, sous les 23,44 exigés au pire. Les soldes qui comptent sont ceux de la pièce de constat neuve qui suivra le versement. »
- Section 8, geste de paiement. Remplacer « Il manque 19,65 € au projet à 11,93 € et 15,99 € au projet à 15,59 €. » par : « Chaque projet doit montrer au moins 31,58 € à la pièce de constat. Aux soldes du 21 novembre (11,93 € et 15,59 €), il manque 19,65 € et 15,99 € ; après le versement accordé sous GO-2026-11-21-74 (10,47 € et 6,81 €), il manque 9,18 € sur chacun. »
- Section 0, point 4 et section 10, point 2 : ajouter la même phrase sur les 9,18 € par projet.

**Correction 4 — la règle de la dépense retirée (livraison 5, C-1).** Section 3.1, troisième point. Remplacer « tant que cette pièce ne porte pas `oui` à `google_deux_projets_distincts` » par : « sauf si la pièce porte `oui` à `google_deux_projets_distincts` **et** constate, sans levée, les deux clés `google_cle_du_projet_constate_cle_1` et `google_cle_du_projet_constate_cle_2` (livraison 5, C-1). Sous le constat que GO-2026-11-21-68 permet, ces deux clés sont levées, et la somme est toujours retirée ». Même changement à la ligne `google_deux_projets_distincts` du tableau de la section 9.

**Correction 5 — la configuration, par les champs du gabarit v4.** Remplacer, dans le tableau de la section 9, les lignes « plafonds des six lignes », « seuils de crédit de Google », « relais de Google, `--borne-reflexion` », « relais de Google, `--plafond-exempte` » et « réserve de sortie » par :

| champ | valeur définitive | état |
|---|---|---|
| `fournisseurs.google.sortie_max` | `65536` | décidé |
| `fournisseurs.google.reflexion` | `{"forme": "niveau", "borne_declaree": 49536}` | borne supposée, éprouvée par C-2 |
| `fournisseurs.google.exemption_de_la_sonde` ; `_go` | `true` ; `"GO-2026-11-21-69"` (forme seule contrôlée) | décidé ; à consigner (section 10, point 3) |
| `fournisseurs.google.credit_min_avant_verification_usd` ; `credit_min_avant_file_usd` | `28.28` ; `23.59` | à changer (gabarit : 19.76 et 16.08) |
| `fournisseurs.google.credit_a_avoir_usd` | `32.97`, pour ne pas dire faux | non lu par le chef v4 ; gabarit : 23.0, valeur du schéma de recharge retiré |
| `lignes.verification-google-cle-1` et `-cle-2` : `plafond_usd` ; `plafond_registre` ; `exces_possible_d_un_envoi_usd` | `3.0` ; `"3,00 USD"` ; `1.69` | à changer (1.5 ; « 1,50 USD » ; 2.18) |
| `lignes.file-neon` : `plafond_usd` ; `plafond_registre` ; `exces_possible_d_un_envoi_usd` | `16.5` ; `"16,50 USD"` ; `7.09` | à changer (8.5 ; « 8,50 USD » ; 7.58) |
| `lignes.<ligne de Google>.reserve_sortie_jetons` | `null` ou `65536` (le chef la déduit de `sortie_max`) | rien à inscrire |
| `lignes.file-neon.delais` | inchangé (2 700 et 2 690), ou 2 491 et 2 481 sous le levier (d) | selon la décision 1 |
| arguments `--borne-reflexion` et `--plafond-exempte` | passés par le chef (lignes 3025 à 3027), non à la main | rien à passer |
| `avenant` | la garde 8 n'en lit qu'un : code neuf, un second champ pour l'avenant 2, vérifié sur disque et cité par la ligne du registre | **à coder** |

Et, dans la liste « Ce que le programme doit changer » de la section 9 :
- au point 2, citer les champs `credit_min_avant_*_usd` ;
- remplacer le point 9 par : « 9. **Limite de mots à la sonde** : déjà tranchée par le programme ; l'exemption couvre les contrôles (2) et (3) pour le corps exact de la sonde (chef v4, lignes 1486 à 1497). »

**Correction 6 — la ligne de taux, sans code neuf.** À la fin de « Forme proposée » (section 7), ajouter : « Le chef v4 ne lit que « - taux : T USD par EUR ; source : … ; heure du taux (UTC) : … » (`MOTIF_TAUX`). Sans code neuf, la pièce de constat écrit : « - taux : 1.0990 USD par EUR ; source : Banque centrale européenne, fixage du 2026-11-20, fichier a234540a78d0bccccc3642bfe604b138310a03741361434907aa4cf3e7622e8a ; heure du taux (UTC) : 2026-11-21T17:49Z ». L'heure du taux y est l'heure du relevé, que bornent les contrôles de la livraison 5 (m-5). Les contrôles 2 et 4 sont alors faits par le vérificateur de la pièce, non par le programme ; les coder est une livraison de plus. »

**Correction 7 — réserve 10.** Remplacer la réserve 10 par : « 10. **L'échéance de GO-2026-11-21-69 (2026-11-22) n'est pas contrôlée pour l'exemption** : le chef ne contrôle que la forme de `exemption_de_la_sonde_go` (ligne 1441). L'échéance contrôlée est celle du GO de chaque ligne de calcul (garde 8). »

**Mineurs.**
- m-1. Le texte de la ligne 4 dit « sa reprise part si le cumul compté avant lui ne passe pas 7,30 USD ». C'est une condition suffisante (7,41 pour un envoi d'appariement) : écrire « au plus 7,30 USD (7,41 pour un envoi d'appariement) ».
- m-2. Point 3 de la section 4 : citer les deux relevés de la section 3 ci-dessus, déjà au dépôt.
- m-3. La règle des cinq jours (section 7, contrôle 4) est une supposition sur le calendrier de la Banque centrale européenne : à relever avec la page de ce calendrier, ou à retirer si le contrôle n'est pas codé.

## 7. Décisions pour Lazar

**Décision 1 — le pire cas chez Google.**
- **Décision** : accepter 89,67 USD sans borne dure, ou adopter un levier qui ramène le pire cas sous les 84,06 USD acceptés.
- **Enjeu** : le relèvement du plafond à 65 536 fait passer le pire cas de 84,06 à 89,67 USD (+ 5,61), sans rien de dur pour le borner.
- **Options** :
  - (A) accepter 89,67 USD. Aucun code ; mais une perte possible plus haute.
  - (B) régime prudent imposé à la file : 32,97 USD, égal à ce que couvrent déjà les seuils de crédit. Prix : la file s'arrête au second envoi coupé à 45 minutes, même sur deux appels différents. Code et essais.
  - (C) délai de la file réduit à 2 481 secondes : 84,02 USD. Aucun code. Prix : débit requis de 26,5 jetons par seconde au lieu de 24,4.
- **Recommandation** : (B), confiance moyenne. La raison qui l'écartait (une file arrêtée sur un seul délai) ne vaut plus à 16,50. Elle retire la part « sans borne dure » sous les suppositions du devis. Si aucun code ne doit être ajouté avant ce soir : (C).
- **Défaut** : aucun, c'est un nœud. Sans mot, aucune ligne de Google ne part.

**Décision 2 — le versement.**
- **Décision** : verser 9,18 € de plus sur chaque projet, après les 10,47 € et 6,81 € accordés sous GO-2026-11-21-74. Sans ce premier versement : 19,65 € et 15,99 €.
- **Enjeu** : sans versement, aucune ligne de Google ne part, pas même une vérification.
- **Options** :
  - (A) 31,58 € vus sur chaque projet : aucune ligne bloquée en route.
  - (B) 27,11 € sur chaque projet : la seconde vérification ne part que si la première coûte au plus 0,02 USD.
- **Recommandation** : (A), confiance moyenne. C'est la seule qui ne puisse pas bloquer une ligne en route. Le solde non consommé reste au compte.
- **Défaut** : aucun, c'est un paiement.

**Décision 3 — consigner la décision de la mère.** Le plafond, le niveau gardé, l'exemption de la sonde et l'âge du taux ne sont nommés par aucune ligne du registre. Je recommande, comme l'avenant (section 10, point 3), une ligne ou une pièce qui nomme ces quatre parts, citée par `exemption_de_la_sonde_go`. Ce n'est pas un paiement : la mère peut l'écrire.

## 8. Ce que j'ai ouvert

- **Lus en entier** :
  - le mandat ;
  - l'avenant 2 ;
  - la note de la livraison 5 (`note-programme-essais-admission-bras-a-v4.md`, `7fbb61e7…`) ;
  - la vérification de la livraison 5 (`2ad643a0…`).
- **Lus en partie** :
  - le devis (`421ee2e6…`) : lignes 17, 34 à 37, 95, 101, 162, 163, 195 à 400, 433 et 434 ;
  - l'avenant 1 v3 (`5e255c5f…`) : lignes 1 à 20, 120 à 165, 250 à 270, 327 ;
  - la contre-lecture de la livraison 4 (`25cda460…`) : lignes 1 à 40 ;
  - la confrontation (`b49688eb…`) : lignes 43, 45, 50, 77 ;
  - la note v3 : lignes 36, 51, 57, 64, 65, 89.
- **Empreintes** : vérification de l'avenant 1 v3 (`8232e22e…`), empreinte seule, non lue au-delà. Toutes les empreintes sont égales à leurs compagnons.
- **Journal** : OD-301 et OD-302, par `grep -E '^- OD-30[12] '`.
- **Registre** : GO-2026-11-21-68, -69, -74 et -75, par `git show origin/main:registres/go.md | grep`.
- **Hors de la liste de la mission, non interdits par le mandat** :
  - le gabarit de configuration v4 (`63a53802…`), lu par programme. Il cite un chemin sous `essai-mesure-lecteurs-bras-a-v1/`, que je n'ai pas suivi ;
  - le chef `scripts/chef_essais_admission_bras_a_v4.py` : lignes 455 à 505, 536 à 575, 715 à 735, 1100 à 1130, 1400 à 1550 et 3240 à 3250, plus des recherches de noms de champs ;
  - le relais de Google v4 : recherches de lignes seulement ;
  - le fichier XML du taux (`a234540a…`), lu par programme ;
  - `releve-api-mistral-gemini-essais-admission-v1.md` (lignes 10 à 25) et `juge-des-ancres-identifiant-gemini-v1.md` (lignes 1 à 30) ;
  - une recherche de mots sur `releve-api-mistral-gemini-essais-admission-complement-v1.md`, sans résultat.
- **Git** : `git status --short` a montré, outre ce fichier, des fichiers `_v5` non suivis du programme et deux fichiers modifiés hors du périmètre (m-7 de la livraison 5). Non ouverts.
- **Cloisonnement** : aucun chemin de la liste du mandat ouvert, listé, cherché ni empreinté. La première commande (`ls` du dossier de la relance) a affiché les noms de ce dossier. Aucun ne porte un motif interdit, sauf le nom du dossier `essai-mesure-lecteurs-bras-a-v1`, affiché par la liste et non ouvert.
- **Mes programmes**, au bloc-notes, hors du dépôt (`/tmp/claude-0/-home-user-controle-ia-travail/080a2aff-9781-5a4d-8af3-2aae94066157/scratchpad/verif-av2/`) :
  - `recalc.py` (`c72a2400…`) : les chiffres ;
  - `cit.py` (`069ffc22…`) : les citations ;
  - `listes.py` (`fe8f1079…`) : les listes de 1.4.

## Annexe — sortie de `recalc.py` (extraits)

```
taux lu 1.0990 fixage 2026-11-20 ; 2026-11-21 : Saturday
== sortie 32768 : Pf 8.5 Pv 1.5 Ef 7.578480 Ev 2.178480 ; 3.68 ; 16.08 ; neuf excès 76.70632 -> 76.71 ; prudent 23.44 ; pire 84.07
== sortie 65536 : ra 0.998040 rc 1.055040 rv 0.983520 ; pire16 16.196640 ; pire3 2.950560 ; Pf 16.5 Pv 3
   Ef 7.086960 Ev 1.686960 ; 4.69 ; 23.59 ; neuf excès 80.282640 -> 80.29 ; prudent 32.97 ; pire 89.67 (exact 89.65656 -> 89.66)
   seuils 28.28 ; 23.59 ; taux net 1.044050 ; crédit compté 12.45 16.27
   avant vérif 1 : 27.09 EUR (15.16 ; 11.50) ; au pire : 31.58 EUR (19.65 ; 15.99 ; 35.64) ; première à 0,02 : 27.11 (15.18 ; 11.52)
   OD-301 : 23.44 -> 22.40 (journal) / 22.46 (programme) ; 22,40 EUR comptent 23.38
   après versement GO-74 (22.40 et 22.40) : à verser 9.18 et 9.18 (18.36)
leviers : k=1 32.97 ; k=2 40.06 ; k=8 82.58 ; k=9 89.67 ; relais de la file max 2481 s -> 84.02 (débit 26.5) ;
   vérif 600 s -> 87.93 ; vérif 0 -> 86.29 ; file conditionnée à 3.77 USD de vérifications ; plafond de file ≤ 10.87
```
