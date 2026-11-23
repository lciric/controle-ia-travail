#!/usr/bin/env python3
"""Lanceur v11d (dérivé du lanceur v11c, `fe7358b9…`, par remplacements exacts ; v11, v11b et v11c restent en place, R12).

Seul changement (régression R1 de la vérification des corrections du v11c, `course-v11/contre-lecture-lanceur-v11c-verification-v1.md`,
`525dc158…`) : l'essai à blanc écrit pour la clé LUC la ligne que `verifier_ligne_luc` exige (`solde_non_lu` vrai, `reference`
GO-2026-11-22-124, aucun montant) ; en v11c, il écrivait un solde et une recharge, refusés en moteur simulé aussi.
Configuration v11d (`configuration-course-affinage-mentors-v11d.json`) : notes `changements_v11.carbon` et `.argon` qui citent
`commande_gemini_flux_v2.py` ; `relais_persistants_v4.plafond_relais_claude_usd` (150, lu par personne) retiré.

Texte du lanceur v11c :

Lanceur v11c (dérivé du lanceur v11b, `a6f64e79…`, par remplacements exacts ; v11 et v11b restent en place, R12).

Ce qui change en v11c (contre-lecture du lanceur v11b, `course-v11/contre-lecture-lanceur-v11b-v1.md`, `cd7e5455…`,
« Scellable après corrections » ; corrections demandées par la mère ; numéros des constats de la contre-lecture) :
1. prix par appel d'Argon du devis interne à 4 / 20 USD par million (constantes nommées, que Fable recalculera aux réglages
   réels) et prix d'un appel de Carbon exact (0,480472) : base de l'écart au devis = 35,683 USD pour cinq espèces, celle du
   texte (calcul du devis v11b) ;
3. ligne de la clé LUC au relevé des crédits exigée : `solde_non_lu` vrai et `reference` = GO-2026-11-22-124, aucun champ de
   solde, de crédit, de reste, de couverture, de réserve ni de recharge ; sinon refus ;
4. libellé exigé de la contre-lecture du préenregistrement : « Opus 5.5, contre-lecteur neuf » ;
5. relecture finale de l'état et du journal du relais Claude après l'arrêt de l'orchestrateur : un refus lu alors vaut le
   code 5 et l'alerte ;
6. chaque lecture du relais Claude écrite au journal du run (`journal-part-claude-au-fil-de-l-eau.jsonl`, scellé à la fin) ;
   compte des appels par statut, dépassement et réserve lus dans l'état, au manifeste de fin ;
7. déclencheurs gardés (tout 4xx sauf 429 au journal, `refus` > 0, part engagée au plafond, lectures illisibles), mais
   l'alerte écrit la nature, le statut et la cause réels (motif du relais quand la ligne en porte un) ;
8. réserve par appel du relais Claude lue au départ (arguments par PID, s'ils la donnent, et état) et écrite au manifeste ;
   constante inutilisée retirée ;
9. sonde d'Astra commune v3 (`scripts/sonde_astra_courses_v3.py`) : variable de clé du relais jeté contrôlée ;
10. plafond de session des juges exigé égal à 1,00 USD ;
11. garde Google rejouée sur la plus longue entrée de chaque rôle ; entrée de juge de la forme de l'orchestrateur
    (`fiches_v54.entree_une_fiche` : consigne, « ## La fiche », fiche JSON) ;
12. commande Gemini en flux v2 (`scripts/commande_gemini_flux_v2.py`) : hypothèse « réflexion comprise dans la sortie
    maximale » vérifiée après chaque réponse ;
15. « haut » de la part Claude retiré du manifeste ; GO-2026-11-22-124 : le montant « part Claude 45 USD » lu au plafond, égal à
    45 (plus de sous-chaîne).

Texte du lanceur v11b :

Lanceur v11b (dérivé du lanceur v11, `bdca413c…`, par remplacements exacts ; le v11 reste en place, R12).

Ce qui change en v11b (décision de la mère sur le point ouvert 11 du rapport v11, routine, étage 1) :
1. le GO de la course (`GO_ID`, passé à l'orchestrateur et cité par la commande de lancement) est **GO-2026-11-22-80**,
   prolongation de GO-2026-11-18-14 (calcul, Lazar, 150 USD, échéance 15 décembre) : l'orchestrateur épinglé (`a41b7b50`,
   `configuration_v55.verifier_go_v55`) ne lit que la période de la ligne `GO_ID` ; avec GO-14, il refusait après le 25 ;
2. GO-80 est exigé (refus s'il est absent, révoqué, hors période, s'il n'est pas de Lazar ou ne dit pas prolonger
   GO-2026-11-18-14) ; la ligne de GO-2026-11-18-14 est exigée aussi (calcul, Lazar, non révoquée ; sa propre échéance ne
   borne plus) ; son plafond est lu « 150 USD » (le renvoi entre parenthèses au GO prolongé est admis, sans autre nombre) ;
3. registre dérivé : ligne de GO-80, ligne de GO-14 (traçabilité) et les révocations qui visent l'une ou l'autre ;
4. configuration v11b (`changements_v11.go_course` = GO-2026-11-22-80, exigé égal à `GO_ID`).

Lanceur de la course d'affinage des idées des mentors par l'organisme d'idéation — version 11 (clé Claude LUC et son
plafond propre, Astra gpt-6.2-astra, Carbon en flux sous la garde des appels à Google).

Version 11 (R12). Base : le lanceur **v10** de la branche `prep/affinage-v10-compte-organisme-v1` (`b0829025…`, contre-lu
« Scellable. », jamais joué ; les v7 à v10 vivent sur les branches `prep/affinage-v7…v10-compte-organisme-v1`, et les noms v8
de la branche du compte organisme sont pris : d'où le numéro 11, ordre de la mère du 22 novembre). Accords : GO-2026-11-22-107
(« go luc », exception déclarée à la règle « Claude par l'abonnement », GO-2026-11-22-70), GO-2026-11-22-110 (clé LUC
vérifiée), GO-2026-11-22-111 (recharge automatique au plus 40 euros ; Astra sur `OPENAI_API_KEY_2`), R-4995 (plafond propre
de LUC). Ce que la v11 change, et rien d'autre :
1. **clé Claude** : tous les appels Claude (deux proposeurs, aiguilleur, premier juge) passent par
   `RR_ANTHROPIC_API_KEY_LUC` ; `RR_ANTHROPIC_API_KEY_MINUIT` (sans crédit, R-4833) rejoint Rigaud parmi les clés exclues ;
   la ligne GO-2026-11-22-107 est lue au registre (`verifier_go_exception_cle`) ; configuration **v11** (copie de la v9 : clés,
   notes, plafond de LUC) ;
2. **part Claude sur LUC** (GO-2026-11-22-124, mots de Lazar, qui simplifie GO-2026-11-22-111) : le solde de LUC n'est pas lu
   et n'est pas une condition de départ (recharge automatique) ; aucun plancher ni couverture déclarée ; la règle « Minuit
   compté au prix relevé » est retirée ; **plafond propre de la part Claude : 45 USD** (R-4995), paramètre nommé
   `changements_v11.plafond_part_claude_usd` de la configuration v11, égal à la constante du lanceur (sinon refus : un plafond
   retiré ou relevé ne part pas) ; le relais Claude est lancé à ce plafond exactement ; GO-2026-11-22-124 est lu au registre et
   prolonge l'exception GO-2026-11-22-107 au 15 décembre ;
3. **arrêt au fil de l'eau** : l'état du relais Claude et son journal (statuts seulement, jamais de texte) sont relus toutes
   les `intervalle_surveillance_s` secondes ; au **premier refus de l'interface** (tout statut 4xx autre que 429 au journal :
   un refus faute de crédit est un 400, R-4833), au premier refus du relais (état `refus` > 0, son 402 à 45 USD), à une part
   engagée (dépense + montants réservés des appels en vol) qui atteint 45 USD, ou à un état ou un journal illisible trois fois
   de suite : arrêt propre de l'orchestrateur par son PID, alerte scellée `alerte-arret-part-claude.json` (le statut, pas la
   cause), **code 5**, sans relance ; le plafond d'arrêt de 150 USD ne change pas ;
4. **Astra** : `gpt-6.2-astra`, prix 8 / 40 USD par million (R-4905), clé `OPENAI_API_KEY_2` exigée par son nom ; sonde v3 par
   la sonde commune v2 (rapports du jour sous `course-v11/`) ; modèle servi relu ; entrée la plus longue sous le palier de
   272 000 jetons ;
5. **Carbon en flux** : commande neuve `scripts/commande_gemini_flux_v1.py` (épinglée) par le relais Gemini v3 en flux de
   `main` (`relais_gemini_v3.py`, `2cf6bc6d…`, port 8791) ; niveau de réflexion « high », provision 28 672, sortie 65 536
   (limite en flux ; texte 36 864 ≥ 16 000 et > 2 cartes × 9 000 caractères), délai 1 500 + 60 s ; pire cas d'un appel sous le plafond de
   session (3,00 USD, configuration v9) écrit au manifeste ; relais : `--max-appels` ≥ 40, `--delai-silence-s` ≤ 240,
   `--delai-amont-s` ≥ délai de la commande, tous explicites ; les gardes de la commande par lot (lots, relevés) sont retirées ;
6. **garde des appels à Google** (règle gelée, GO-2026-11-21-71) : chaque commande Google déclarée (Argon, Carbon) est jouée
   hors ligne devant un faux amont local qui capture le corps de génération (rien ne part) ; le corps passe
   `garde_google_v3.verifier_reglages_google` (pièce de `main`, `923679b5…`) et la limite de l'invite d'un proposeur ; tout
   problème refuse le départ réel (écrit au manifeste en moteur simulé) ;
7. devis interne : Carbon à 0,4805 USD par appel (même pensée et réponse que le devis v8, prix 4 / 20 de R-5018, sans remise
   de lot) ; Argon et Carbon déclarés à 4 / 20 USD par million, réflexion comprise (R-5018) ;
8. noms propres à la version (chemins `course-v11/`, sorties, suffixe des runs ; une seule course de v1 à v11).
Codes : 0, 2, 3, 4, 6 comme la v10 ; **5** : arrêt par la garde de crédit d'un relais dispensé (v10) **ou** arrêt propre sur la
part Claude (premier 4xx de l'interface autre que 429 au journal du relais Claude, 402 du relais à 45 USD, part engagée au
plafond, état ou journal illisible), sans relance ; l'alerte scellée dit le statut, pas la cause.
Argon : emplacement `argon_v11.plafond_session_juge_usd` de la configuration (vide : en attente du mot de la mère) ; rempli, il
remplace le plafond de session des juges dans la configuration servie (la garde Google juge ensuite le chemin d'Argon).

Texte de la v10 :

Lanceur de la course d'affinage des idées des mentors par l'organisme d'idéation — version 10.

Version 10 (R12 ; v1 à v9 restent en place, jamais lancées). Contre-lecture de la v9 par le modèle K
(`course-v9/contre-lecture-preenregistrement-course-affinage-mentors-v9.md`, `615ef93b…`, « Scellable après corrections. ») :
un majeur et deux mineurs, **tous de texte** (le lanceur v9 ne porte pas l'erreur). Le préenregistrement v9, le devis v9, le
rapport et les commandes v9 annonçaient un plafond dur de 60 USD qui couperait l'étape « proposition » ; l'orchestrateur épinglé
fixe un plafond dur souple, max(plafond de relais ; 150 − cumul − attendus des étapes restantes) = 130 USD au lancement de la
proposition (`pole/budget_v56.py`, `pole/noyau_v56.py`) ; le risque « non mesuré (budget) » porte sur les juges (cumul > 100) et
l'aiguillage (cumul > 120). Textes corrigés en v10 (préenregistrement, devis, commandes, gabarit de déclaration).
Ce lanceur est le v9 à ces seuls points près :
1. `PREREG` et `PREREG_SHA256` : le préenregistrement v10 ;
2. chemins `course-v10/` : préenregistrement, contre-lecture, déclaration des relais, relevés des crédits et du prix Claude ;
   rapports d'une sonde du jour sous `course-v10/` (ceux faits sous `course-v9/`, `course-v8/`, `course-v7/` restent lus ; un
   seul rapport de sonde commune du jour admis) ; la configuration reste la v9, lue sous `course-v9/` (inchangée) ;
3. sorties `/home/user/sorties-course-affinage-mentors-v10/`, `runs/<id>-course-affinage-mentors-v10/`, alerte de crédit
   `…-v10` ; une seule course de v1 à v10 ;
4. version et cet en-tête.
Aucune garde, aucune constante chiffrée, aucun argument de commande, aucun code de sortie ne change. Plafond d'arrêt 150 USD
(GO-2026-11-18-14). Le reste est la v9.

Texte de la v9 :

Lanceur de la course d'affinage des idées des mentors par l'organisme d'idéation — version 9.

Version 9 (R12 ; v1 à v8 restent en place, jamais lancées ; la v8 ne sera pas contre-lue). La documentation de Google sur la
pensée (lue par la session principale, aistudio.google.com/docs/thinking) dit que la sortie maximale « sets the maximum number
of tokens a response can generate, including thought tokens », coupure dure : la v8 (sortie ramenée à environ 7 000 jetons
sous 1,50 USD, pensée observée jusqu'à 20 696) tronquerait chaque réponse de Carbon (code 5). Décision de la session
principale sous l'autonomie de Lazar (option 1 (c) du rapport du développeur v8) :
1. configuration **v9** : plafond de session des proposeurs porté de 1,50 à **3,00 USD** (comme la course d'auto-conception) ;
   rien d'autre ne change dans la configuration ;
2. Carbon : `--max-sortie-jetons 32768`, `--provision-pensee-jetons 28672` (délais de la v8 : lot 1 620 s, requête 60 s,
   durée maximale 1 770 s sous les 1 800 s de l'orchestrateur) ; sous 3,00 USD la commande garde 32 768 jetons de sortie sur
   l'entrée la plus longue, pire cas d'un appel 2,5715 USD au prix plein ;
3. garde neuve : sortie retenue par la commande sur l'entrée la plus longue ≥ **24 500** jetons (plus forte pensée observée
   20 696 + plus forte réponse observée 3 410, arrondi) ; les gardes de la v8 restent ;
4. parts au pire recalculées par le lanceur sur le plafond de session : Astra 16 × 3,00 = 48 USD (relais d'Astra à 48 USD
   exactement), Carbon 48, clé de Google 150 + 48 = 198 ; Minuit 150 ; Astra sans reprise (aléa accepté, option 3 (a)).
Codes inchangés. Plafond d'arrêt 150 USD (GO-2026-11-18-14). Le reste est la v8.

Texte de la v8 :

Lanceur de la course d'affinage des idées des mentors par l'organisme d'idéation — version 8.

Version 8 (R12 ; v1 à v7 restent en place, jamais lancées). Correctif ciblé après l'échec technique de la course
d'auto-conception v4 (diagnostic `organisme-auto-conception-v1/course-v2/diagnostic-erreurs-carbon-astra-course-v4-v1.md`,
510312b1… : la commande de Carbon refuse par son code 7 quand la pensée dépasse la provision — 8 192 par défaut, observé
17 454 à 20 696 jetons — et par son code 6 au-delà de son délai de 1 500 s). Hypothèse, mesures, seuils, plafond d'arrêt
(150 USD) et composition inchangés. Ce qui change :
1. Carbon : provision de pensée relevée à **28 672** jetons (et non 32 768 : sous le plafond de session d'un proposeur de
   l'affinage, 1,50 USD, la garde avant envoi de la commande refuserait alors **chaque** appel, code 4 — (4 096 + 32 768)
   × 41,5 / 10⁶ = 1,53 USD avant même l'entrée), sortie maximale 16 384, délai 1 620 s, délai de requête 60 s : la commande
   dure au plus 1 620 + 30 + 2 × 60 = 1 770 s, sous le délai de l'adaptateur de commande de l'orchestrateur épinglé
   (1 800 s, écrit en dur : `pole/adaptateurs.py` l. 622, construit sans délai par `demonstrations/ideation_v8.py` l. 74) et
   sous A3 (1 800 s, configuration v6) ; ce délai ne peut pas être relevé sans une version neuve de l'orchestrateur ;
2. gardes neuves (refus, code 2) : options de Carbon exigées une fois chacune et lisibles ; provision ≥ 1,25 × la plus forte
   pensée observée ; chaque appel peut partir (pire cas minimal sous le plafond de session, sur l'entrée la plus longue de la
   course) ; pire cas d'un appel calculé et écrit ; durée maximale de la commande + marge ≤ délai de l'orchestrateur et d'A3 ;
   délai de lot ≥ 1 620 s ; relais de Carbon : « releves » nul et « releves_restants » ≥ 20 lots × (⌈1 620 / 30⌉ + 2) ;
3. devis v8 : prix estimé d'un appel de Carbon 0,4985 USD (pensée 20 000, sortie 3 500, entrée gardée 2 618, prix du lot) ;
   base de l'écart au devis : cinq espèces = 41,136 USD ;
4. Astra : aucune reprise (pas de reprise possible sous le plafond de session de 1,50 USD sans changer la commande épinglée
   ou ce plafond ; proposition au rapport du développeur v8) ; chemins `course-v8/`, sorties `…-v8`.
Codes inchangés (0, 2, 3, 4, 5, 6). Le reste est la v7.

Texte de la v7 :

Lanceur de la course d'affinage des idées des mentors par l'organisme d'idéation — version 7.

Version 7 (R12 ; v1 à v6 restent en place, jamais lancées). Porte la contre-lecture complète de la v6 et des commandes v6b
(modèle K, `course-v6/contre-lecture-complete-course-affinage-v6-v6b.md`, « Scellable après corrections. ») :
1. (majeur 1) bornes basses lues par PID **et** sur `/relais/etat` pour **tous** les relais annoncés au préenregistrement :
   Astra (et Kimi) : `--max-appels` ≥ 16 + 4 = 20, plafond du relais ≥ sa part au pire (Astra : égal, 24 USD = 16 × 1,50) ;
   Carbon : `--max-lots` ≥ 20 et `--max-appels` ≥ 40 ; Argon : inchangé (2 × (16 + 32 × espèces)) ; Claude : plafond 150 ;
   valeurs de l'état égales aux arguments ; un argument de borne absent est un refus (aucun défaut supposé) ;
2. (majeur 2) aucune course d'auto-conception en cours (manifeste de départ sans manifeste de fin) ; relevé des crédits
   postérieur à la fin de toute course d'auto-conception versée ; les commandes v7 disent le reste (ports, clés, sonde) ;
   sonde d'Astra : rapport de la sonde commune du jour exigé et lié au rapport v2 par son empreinte (le rapport du
   18 novembre, `course-v6/sonde-astra-course-affinage-v6.json`, est accepté ce jour-là) ;
3. (mineurs) état de relais vide ou sans « appels » refusé ; écart au devis recalculé sur les espèces actives (cinq : 37,576) ;
   code 6 pour une course partie dont l'orchestrateur rend un code non nul ou dont le lanceur échoue après le départ ; sonde
   commune épinglée ; Kimi refusé tant qu'aucune référence n'est admise par une version du lanceur (liste vide).
Codes : 0 course finie ; 2 refus avant le départ ; 3 alerte de crédit avant le départ ; 4 cumul au-dessus de 150 USD ;
5 arrêt par la garde de crédit ; 6 course partie, orchestrateur à code non nul (arrêt, nœud, signal) ou erreur du lanceur
après le départ (vrai code au manifeste de fin).
Le reste est la v6.

Texte de la v6 :

Lanceur de la course d'affinage des idées des mentors par l'organisme d'idéation — version 6.

Version 6 (R12 ; v1 à v5 restent en place, jamais lancées). Porte la contre-lecture de la v5 (modèle K,
`course-v5/contre-lecture-preenregistrement-course-affinage-mentors-v5.md`, `3da3379a…`) :
1. identifiant de run unique à la microseconde ; acte de gel, configuration et registre dérivé écrits dans un dossier de
   préparation hors dépôt ; `runs/<id>` n'est créé qu'après la porte à blanc (un refus ne laisse rien au dépôt) ;
2. sonde d'Astra : réglages dans les commandes (réserve du relais jeté, sortie bornée par le plafond) ;
3. Kimi non déclaré par défaut : déclaré seulement avec un mot écrit de la mère dans la déclaration
   (`"kimi_autorise_par_la_mere": {"reference": …}`) ;
4. clé faite d'espaces refusée ;
5. garde de crédit v6 : soupçon sur une ligne de limite de débit réglable par la déclaration
   (`"compter_limite_de_debit_comme_soupcon"`, vrai par défaut) ;
6. textes (titre de l'acte de gel) ; 7. part au pire par **nom de variable de clé** : somme des parts des relais qui la
   partagent (Argon et Carbon : 150 + 24), règle de clé par part appliquée à la somme.
Le reste est la v5.

Texte de la v5 :

Lanceur de la course d'affinage des idées des mentors par l'organisme d'idéation — version 5.

Version 5 (R12 ; v1 à v4 restent en place, jamais lancées). Porte :
A. les constats 1 à 5 de la contre-lecture de la v4 (rapportés par la mère) : (1) le dossier de sortie et le dossier des arrêts
   ne sont créés qu'après la vérification de l'orchestrateur et la porte à blanc, et une course ne compte comme lancée que par
   son manifeste de départ ou son journal ; (2) arguments de chaque commande de porte recoupés avec la déclaration et la
   configuration (`--url`, `--modeles-permis`, `--plafond-ligne` = 150) ; modèles permis du relais vivant égaux à ceux de la
   configuration ; (3) garde de crédit v5 (soupçon, arrêt au deuxième soupçon du même relais ; seuls les fichiers
   `arret-credit-*` arrêtent la course) ; (4) relais Gemini d'Argon (et de Carbon) contrôlés avant le départ : PID, programme
   épinglé, port, `--max-appels` suffisant, état neuf, variable de clé effacée ; (5) textes ;
B. Carbon déclaré (R-3274) : commande Gemini par lot épinglée, arguments exacts, relais Gemini v4 contrôlé ;
C. Astra déclaré seulement après une sonde triviale réussie (≤ 0,05 USD, relais jeté ; R-3273), relais de la course neuf ;
D. confidentialité (R-3273) : textes servis expurgés et vérifiés par programme (aucun nom de personne interne, aucun
   identifiant de session, aucun courriel) ; un texte servi où il en reste fait refuser le départ.
Le reste est la v4.

Texte de la v4 :

Lanceur de la course d'affinage des idées des mentors par l'organisme d'idéation — version 4.

Version 4 (R12 ; v1 à v3 restent en place, jamais lancées) : porte les douze constats de la contre-lecture de la v3 (modèle
K, `course-v3/contre-lecture-preenregistrement-course-affinage-mentors-v3.md`, `52e7cc02…`) :
1. porte de plafond des relais persistants = programme épinglé `scripts/porte_plafond_relais_v1.py` (relais de ligne
   entière), en tête de la commande de chaque porte ; **porte à blanc** avant le manifeste de départ ; relais vivant contrôlé
   par PID (programme épinglé par la procédure, variable de clé, port, plafond) ;
2. registre des GO **dérivé** (ligne du GO et révocations qui la visent), écrit et scellé dans le dossier du run, passé à
   l'orchestrateur ; empreinte du registre source au manifeste ;
3. contrôles de l'adaptateur de Kimi repris avant le départ ; 4. garde de crédit v4 ; 5. relevé du jour des prix Claude, scellé,
   comparé au barème du relais épinglé ; 6. relais lancés par le lanceur de relais de la procédure ; 7. variable Minuit vide
   refusée ; 8. pièce de la procédure épinglée ; 9. commandes d'Astra et de Carbon épinglées (table vide en v4 : ces espèces
   sont refusées tant qu'une version ne les épingle pas) ; 10. reste égal à la part refusé ; 11. sorties hors dépôt regardées ;
   12. alerte écrite pour la mère à l'arrêt pour crédit.
Codes : 0, 2, 3, 4, 5 comme la v3.

Texte de la v3 :

Lanceur de la course d'affinage des idées des mentors par l'organisme d'idéation — version 3.

Version 3 (R12 ; v1 `015f5c33…` et v2 `9a85e78d…` restent en place, jamais lancées). Décisions de la mère R-3237 :
(1) **règle de clé par part** : chaque clé est confrontée à sa part au pire (la course ne peut pas dépenser plus sur elle),
non au plafond global ; pour Kimi, part au pire + 11,3 USD (pire cas de la course Kimi de la relance, GO-2026-11-18-17)
≤ 90 % du reste lu, sinon refus (les deux courses se suivent, solde relu avant chacune) ; le plafond d'arrêt de 150 USD est
inchangé ; (2) **dispense écrite** (référence R-3237) pour les clés d'Argon, d'Astra et de Carbon, au solde illisible :
départ permis, chaque appel passe par `scripts/garde_credit_relais_v3.py`, et **la course est arrêtée au premier refus pour
crédit** (SIGTERM à l'orchestrateur par son PID, arrêt propre) ; coût compté au prix des fichiers ; (3) **procédure neutre
des relais persistants** : pièce `course-v3/procedure-relais-persistants-course-affinage-v3.json` (chemin et empreinte de la
procédure versée par la mère) ; moteur réel refusé tant qu'elle n'est pas remplie, scellée, à son empreinte, et citée par
les portes de plafond des relais persistants. Contre-lecture : modèle K, `course-v3/`.
Codes : 0 course finie ; 2 refus avant départ, ou arrêt ou nœud de l'orchestrateur ; 3 alerte de crédit avant le départ ;
4 cumul lu au-dessus de 150 USD ; 5 course arrêtée au premier refus pour crédit d'un relais dispensé.

Texte de la v2 (inchangé sur le reste) :

Lanceur de la course d'affinage des idées des mentors par l'organisme d'idéation — version 2.

Version 2 (R12 ; la v1, `scripts/lancer_course_affinage_mentors_v1.py`, `015f5c33…`, reste en place, jamais lancée).
Ajouts (consigne de la mère, R-3228) : tous les appels Claude passent par la clé `RR_ANTHROPIC_API_KEY_MINUIT` (nom seul) ;
arrêt au départ si cette variable est absente de l'environnement du lanceur (test par le nom, jamais par la valeur) ;
refus de tout relais configuré sur une autre clé de la famille Claude, `RR_ANTHROPIC_API_KEY_RIGAUD` nommément ; crédit
de la clé Minuit compté au prix relevé quand l'interface de facturation ne le rend pas (200 USD déclarés, R-3228, moins
la dépense antérieure déclarée) ; contre-lecture par le modèle K, garde stricte (première ligne du verdict exacte, refus
d'un rapport qui dit n'avoir pas relu) ; nom de la clé écrit pour chaque relais et chaque espèce au manifeste.

Texte de la v1 (inchangé sur le reste) :

Décision N-072 (texte `docs/decisions/decision-matiere-premiere-mentors-v1.md`), GO-2026-11-18-14 (plafond d'arrêt 150 USD,
R-3215), budget des appels d'interface séparé (GO-2026-11-18-13, R-3209 point 2). Préenregistrement :
`docs/notes/organisme-affinage-mentors-v1/course-v1/preenregistrement-course-affinage-mentors-v1.md` (empreinte épinglée
ci-dessous). Modèle : le lanceur de référence `scripts/lancer_course_ideation_organismes_discrets_v7.py` (`3b20b911…`) —
mêmes gardes de GO, d'orchestrateur, de pièces, d'environnement sans clé, de bac à sable, de manifestes scellés ; mais la
course passe par la **course 2** de l'orchestrateur (`demonstrations/ideation_v8.py --course-2`, v56), qui porte
l'aiguilleur, les juges croisés aveugles et la mémoire anti-redite que la voie v2 n'a pas.

Usage, seul et exact (cwd = racine du dépôt de travail) :

    GO_ID=GO-2026-11-22-80 /usr/local/bin/python3 -I -B scripts/lancer_course_affinage_mentors_v11b.py

Essai à blanc (moteur simulé de l'orchestrateur, relais factices, aucune dépense, aucun GO) :

    /usr/local/bin/python3 -I -B scripts/lancer_course_affinage_mentors_v1.py --a-blanc DOSSIER_NEUF

Ce que fait le lanceur, dans cet ordre ; tout refus rend 2 (motif sur la sortie d'erreur), toute alerte de crédit avant le
départ rend 3 ; rien n'est appelé avant le manifeste de départ :
1. course jamais lancée sous ce lanceur (R12 : un dossier de run de cette course existe déjà = refus ; une relance est une
   nouvelle version et un mot de la mère) ; ligne de GO (type calcul, accordée par Lazar, période, non révoquée, plafond
   lu = 150 USD exactement) ;
2. garde (3) : préenregistrement à l'empreinte épinglée et scellé ; contre-lecture scellée, présente, qui cite l'empreinte du
   préenregistrement **et celle de ce lanceur**, au verdict « Scellable » sans réserve (sinon refus) ;
3. pièces épinglées (configuration fixe, liste des fils, consignes, enveloppe et commande d'Argon) ; liste des fils : aucune
   entrée servie dans les retraits, aucun jeton réservé dans un texte servi ;
4. déclaration des relais (écrite et scellée par la session d'exécution : adresses de boucle locale, portes de plafond, noms
   des clés, jamais une valeur) : espèces actives ; Carbon seulement si inscrite (R-3217) **et** relais et clé nommés ;
5. garde (2) : relevé du crédit de chaque clé employée (fichier scellé de la session d'exécution, du jour) : « non lisible »
   refusé sauf dispense écrite de la mère ; reste sous un cinquième du crédit ou sous le plafond d'arrêt : alerte écrite
   pour la mère (fichier et sortie), arrêt avant le départ (code 3) ;
6. orchestrateur : commit et empreintes épinglés, arbre propre (fichiers suivis, non suivis, ignorés) ;
7. garde (1) : configuration d'orchestrateur assemblée (plafond S17 = 150 = GO, portée « course », une génération, plafonds
   de relais des étapes protégées ≤ 150, passe « tableau » et fusions retirées par construction), écrite et scellée avec
   l'acte de gel ; `--verifier-seulement` de l'orchestrateur (aucun appel) exigé à 0, montant requis 150 ;
8. environnement sans clé (noms retirés, jamais une valeur), bac à sable (moteur réel), manifeste de départ scellé (R9) ;
9. course ; manifeste de fin scellé sur tout chemin ; garde (5) coût réel par relais (consommations de l'orchestrateur), écart
   au devis v3, relevé « après » estimé et alerte si un reste estimé passe sous les seuils.

Bibliothèque standard seulement (le lanceur tourne sous `-I`). Ce lanceur nomme des modèles dans la configuration qu'il
passe à l'orchestrateur (comme le lanceur de référence) ; les pièces versées n'en nomment aucun.
"""
from __future__ import annotations

import datetime as _dt
import hashlib
import importlib.util
import shlex
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
import math
import os
import re
import shutil
import signal
import subprocess
import sys
import unicodedata
from dataclasses import dataclass
from pathlib import Path

VERSION = "lancer_course_affinage_mentors_v11d"
GO_ID = "GO-2026-11-22-80"          # v11b : GO de la course (prolongation de GO-2026-11-18-14)
GO_COURSE_INITIAL = "GO-2026-11-18-14"  # v11b : GO prolongé, exigé au registre et gardé au registre dérivé
GO_EXCEPTION_CLE = "GO-2026-11-22-107"  # exception déclarée à la règle « Claude par l'abonnement »
REGLE_ABONNEMENT = "GO-2026-11-22-70"
GO_PRECISIONS_CLE = ("GO-2026-11-22-110", "GO-2026-11-22-111", "R-4995")  # cités au manifeste, non lus
PLAFOND_ARRET_USD = 150.0
INSCRIPTION_CARBON = "R-3217"
DEPOT = Path(__file__).resolve().parents[1]
COURSE_V1 = "docs/notes/organisme-affinage-mentors-v1/course-v1"
COURSE_V2 = "docs/notes/organisme-affinage-mentors-v1/course-v2"
COURSE_V3 = "docs/notes/organisme-affinage-mentors-v1/course-v3"
COURSE_V6 = "docs/notes/organisme-affinage-mentors-v1/course-v6"
COURSE_V7 = "docs/notes/organisme-affinage-mentors-v1/course-v7"
COURSE_V8 = "docs/notes/organisme-affinage-mentors-v1/course-v8"
COURSE_V9 = "docs/notes/organisme-affinage-mentors-v1/course-v9"
COURSE_V10 = "docs/notes/organisme-affinage-mentors-v1/course-v10"
COURSE = "docs/notes/organisme-affinage-mentors-v1/course-v11"
# v8 : réglages de la commande de Carbon (diagnostic 510312b1… de la course d'auto-conception v4, faits techniques seulement).
PENSEE_OBSERVEE_MAX_JETONS = 20696            # plus forte pensée observée en lot (diagnostic, § 2)
MARGE_PENSEE = 1.25                           # provision exigée ≥ 1,25 × la plus forte pensée observée (25 871 jetons)
PROVISION_PENSEE_CARBON = 28672               # v8 ; v9 : inchangée
MAX_SORTIE_CARBON = 65536                     # v11 (flux) : limite en flux ; texte 36 864 au-delà de la provision 28 672
REPONSE_OBSERVEE_MAX_JETONS = 3410            # plus forte réponse observée (diagnostic, § 2)
SORTIE_RETENUE_MIN_CARBON = 24500             # v9 : ≥ pensée observée + réponse observée (24 106), arrondi
SORTIE_MIN_CARBON = 4096
DELAI_CARBON_S = 1500                         # v11 (flux) : délai de la génération ; + 60 s du compte de jetons, sous 1 800
INTERVALLE_CARBON_S = 30
DELAI_REQUETE_CARBON_S = 60                   # 120 par défaut : abaissé pour donner 120 s de plus au lot sous 1 800 s
DELAI_ADAPTATEUR_ORCHESTRATEUR_S = 1800.0     # `pole/adaptateurs.py` l. 622 ; `ideation_v8.py` l. 74 ne le règle pas
MARGE_DELAI_CARBON_S = 30.0                   # démarrage des processus, garde de crédit, horloge de l'orchestrateur
CARACTERES_PAR_JETON_CARBON = 3.0             # défauts de la commande (`--caracteres-par-jeton`, `--marge-entree`), non passés
MARGE_ENTREE_CARBON = 0.05
OPTIONS_CARBON_EXIGEES = ("--prix-entree", "--prix-sortie", "--max-sortie-jetons", "--provision-pensee-jetons", "--delai-s",
                          "--delai-requete-s")  # v11 : options numériques de la commande en flux
NIVEAU_REFLEXION_CARBON = "high"              # v11 : le plus haut admis pour Carbon (garde Google v3)
TEXTE_MIN_GOOGLE = 16000                      # règle gelée : réflexion + 16 000 jetons de texte au moins
CARACTERES_PAR_CARTE_MAX = 9000               # consigne du proposeur, point 6 (une carte, 9 000 caractères au plus)
DELAI_SILENCE_RELAIS_MAX_S = 240.0            # relais v3 : sous la coupure à 300 s des connexions muettes
PORT_CARBON = 8791                            # relais Gemini v3 en flux (procédure neutre, § 2.4)
# v7, majeur 1 : bornes basses des relais. L'orchestrateur épinglé fait un appel d'adaptateur par case et par proposeur, sans
# reprise (`pole/noyau_v56.py`, `appel` ; `pole/course2_v53.py`, `_proposer`) ; la commande d'Astra envoie une requête par
# appel, celle de Carbon un `countTokens` et un `batchGenerateContent` (un lot) par appel. Seize appels suffisent donc à la
# lecture ; la marge de quatre (25 %) couvre ce que la lecture ne peut exclure (un appel refusé par le relais avant l'amont
# compte quand même). Elle ne porte que sur les appels : le plafond en dollars du relais d'Astra reste sa part au pire.
APPELS_PAR_PROPOSEUR = 16
MARGE_APPELS_PROPOSEUR = 4
MIN_APPELS_RELAIS_PROPOSEUR = APPELS_PAR_PROPOSEUR + MARGE_APPELS_PROPOSEUR   # Astra, Kimi : 20
MIN_LOTS_CARBON = APPELS_PAR_PROPOSEUR + MARGE_APPELS_PROPOSEUR              # 20
MIN_APPELS_CARBON = 2 * MIN_LOTS_CARBON                                       # 40 : countTokens + lot, par appel
# v8 : relevés de lot au plus par lot = ⌈délai / intervalle⌉ + 1 (la boucle relève toutes les 30 s jusqu'au délai), + 1 de marge ;
# le relais Gemini v4 les borne à part (`--max-releves`, 2 000 par défaut) : 20 × 56 = 1 120 exigés dans son état.
MIN_RELEVES_CARBON = MIN_LOTS_CARBON * (-(-DELAI_CARBON_S // INTERVALLE_CARBON_S) + 2)
RELAIS_A_DOLLARS = ("claude", "kimi", "astra")
PORTS_DES_COURSES = (8787, 8788, 8789, 8790, 8791, 8792)
# v7, mineur 9 : références écrites de la mère qui autorisent Kimi ; vide : Kimi refusé (R-3279), quelle que soit la déclaration.
REFERENCES_KIMI_ADMISES: tuple = ()
# v7, majeur 2 : l'autre course de l'organisme qui partage ports, clés et sonde.
MOTIF_AUTRE_COURSE = re.compile(r"-course-auto-conception-v\d+$")
REFERENCE_DISPENSE = "R-3237"
FOURNISSEURS_DISPENSABLES = ("argon", "astra", "carbon")
KIMI_COURSE_SUIVANTE_PIRE_USD = 11.3   # R-3237 : pire cas de la course Kimi de la relance (GO-2026-11-18-17)
KIMI_PART_DU_RESTE = 0.9
PROCEDURE_RELAIS = f"{COURSE_V3}/procedure-relais-persistants-course-affinage-v3.json"
RELEVE_PRIX = f"{COURSE}/releve-prix-claude-course-affinage-v11.json"
# v7 : rapport v2 de la sonde (format lu depuis la v5) et rapport de la sonde commune du même appel, cherchés au jour du
# lancement. Le 18 novembre : `course-v6/sonde-astra-course-affinage-v6.json` (d2cacbcf…) et
# `organisme-auto-conception-v1/course-v2/sonde-astra-commune-2026-11-18-v1.json` (802b840e…). Un autre jour : une sonde
# neuve ; v8 : rapports sous `course-v8/` aux noms datés (ceux d'une sonde du jour faite par les commandes v7, sous
# `course-v7/`, restent lus ; un seul rapport de sonde commune du jour est admis parmi tous ces chemins).
# v11 : sonde v3 (gpt-6.2-astra, 8 / 40) jouée par la sonde commune v2, rapports du jour sous `course-v11/` seulement (les
# rapports des versions précédentes sont d'un autre modèle).
SONDE_ASTRA = f"{COURSE}/sonde-astra-course-affinage-v11.json"
SONDES_ASTRA_V2 = (f"{COURSE}/sonde-astra-course-affinage-v11-{{jour}}.json", SONDE_ASTRA)
SONDES_ASTRA_COMMUNES = (f"{COURSE}/sonde-astra-commune-{{jour}}-v2.json",)
VERSION_SONDE_ASTRA = "sonde_astra_affinage_v3"
VERSION_SONDE_COMMUNE = "sonde_astra_courses_v3"
VARIABLE_CLE_SONDE_ASTRA = "OPENAI_API_KEY_2"  # v11c, constat 9 : clé du relais jeté, contrôlée par la sonde commune v3
SONDE_ASTRA_MAX_USD = 0.05
# Barème du relais de clé de la procédure (`pole/relais_reel.py`, 1b90b020…, l. 49-54), USD par million (entrée, sortie).
BAREME_CLAUDE = {"claude-opus-5-5": (4.0, 20.0), "claude-fable-5-1": (10.0, 50.0)}
# Programmes de relais épinglés par la procédure neutre (§ 1) : nom de fichier → empreinte.
PROGRAMMES_RELAIS = {"claude": ("relais_reel.py", "1b90b020287e575b5564508f9ba33b87bbc051c1015f4198e6b6e648d50ee153"),
                     "kimi": ("relais_kimi_v4.py", "67f369518102b3f7408f28dab053a4d6f9bc2b676eadfaa338f55d39af99027e"),
                     "astra": ("relais_kimi_v4.py", "67f369518102b3f7408f28dab053a4d6f9bc2b676eadfaa338f55d39af99027e"),
                     "argon": ("relais_gemini_v3.py", "2cf6bc6df83f8847e75911c8cc0b6153c4467b36ce69273de649b5cbdc7e2378"),  # v11
                     "carbon": ("relais_gemini_v3.py", "2cf6bc6df83f8847e75911c8cc0b6153c4467b36ce69273de649b5cbdc7e2378")}  # v11 : en flux
MODELES_RELAIS = {"kimi": ["kimi-k3.1-pro"], "astra": ["gpt-6.2-astra"], "argon": ["gemini-4-argon"], "carbon": ["gemini-4-carbon"]}
# Astra (R-4905) : USD par million, palier jusqu'à 272 000 jetons d'entrée (16 / 60 au-delà, jamais admis ici).
PRIX_ASTRA = (8.0, 40.0)
PALIER_ASTRA_JETONS = 272000
CLE_ASTRA = "OPENAI_API_KEY_2"  # GO-2026-11-22-111
PORT_ARGON = 8788  # v11 : relais Gemini v3 d'Argon (en flux) ; l'enveloppe v5 n'est plus déclarée
GEMINI = ("argon", "carbon")
# Commandes externes épinglées (constat 9 de la v3 ; B et C de la v5) : nom de fichier → empreinte (copies de main).
COMMANDES_EPINGLEES: dict = {
    "astra": {"commande_astra_v1.py": "986cf71efcac285899e76dd9b1d1c11bccbfd71dd7ae91b8bf3a4372567d7c71"},
    "carbon": {"commande_gemini_flux_v2.py": "13b968eb440279eb77cd9858cefacfb54bc87b11cbf5fc47cf4476044f8e6a50"}}  # v11c : commande en flux v2 (constat 12)  # v11 : commande en flux (dépôt de travail)
GARDE_GOOGLE_PRODUCTION = "/home/user/controle-ia-travail/src/controle_ia/garde_google_v3.py"
COMMANDES_EPINGLEES["argon"] = dict(COMMANDES_EPINGLEES["carbon"])  # v11 : Argon par la même commande en flux
# v11 (décision de la mère) : Argon proposeur et second juge sous la garde Google, par la commande en flux et un relais Gemini v3
# (port 8788, modèle gemini-4-argon). Réglages : niveau « high », provision 24 576, sortie 45 056 (texte 20 480 ≥ 16 000 et
# > 2 × 9 000 caractères) ; prix 4 / 20 USD par million, réflexion comprise (R-5018) ; la commande compte la réflexion dans la
# sortie maximale : pire cas d'un juge = entrée + 45 056 × 20 / 10⁶ ≈ 0,92 USD ; la provision est une HYPOTHÈSE (aucune pensée
# d'Argon au niveau « high » n'est relevée dans les pièces lues).
PROVISION_PENSEE_ARGON = 24576
MAX_SORTIE_ARGON = 45056
# Arguments exacts après « python -I -B <commande> » (B, C). v8 : le délai total de la commande de Carbon (1 620 + 30 + 2 × 60
# = 1 770 s, comme en v7) reste sous le délai de l'adaptateur de l'orchestrateur (1 800 s, non réglable) avec 30 s de marge ;
# provision de pensée 28 672, sortie maximale 16 384 en v8 ; v9 : sortie maximale 32 768, que la garde avant envoi de la
# commande garde entière sous le plafond de session de 3,00 USD (pire cas 2,5715 USD sur le fil le plus long).
ARGUMENTS_COMMANDES = {
    "carbon": ["--espece", "carbon", "--modele", "gemini-4-carbon", "--url-base", f"http://127.0.0.1:{PORT_CARBON}/v1beta",
               "--prix-entree", "4", "--prix-sortie", "20", "--niveau-reflexion", NIVEAU_REFLEXION_CARBON,
               "--provision-pensee-jetons", str(PROVISION_PENSEE_CARBON), "--max-sortie-jetons", str(MAX_SORTIE_CARBON),
               "--delai-s", str(DELAI_CARBON_S), "--delai-requete-s", str(DELAI_REQUETE_CARBON_S), "--roles", "proposeur_ideation",
               "--garde", GARDE_GOOGLE_PRODUCTION],
    "argon": ["--espece", "argon", "--modele", "gemini-4-argon", "--url-base", f"http://127.0.0.1:{PORT_ARGON}/v1beta",
              "--prix-entree", "4", "--prix-sortie", "20", "--niveau-reflexion", "high",
              "--provision-pensee-jetons", str(PROVISION_PENSEE_ARGON), "--max-sortie-jetons", str(MAX_SORTIE_ARGON),
              "--delai-s", str(DELAI_CARBON_S), "--delai-requete-s", str(DELAI_REQUETE_CARBON_S),
              "--roles", "proposeur_ideation,juge_ideation", "--garde", GARDE_GOOGLE_PRODUCTION],
    "astra": ["--url-relais", "http://127.0.0.1:8790", "--modele", "gpt-6.2-astra", "--prix-entree", "8", "--prix-sortie", "40",
              "--max-sortie-jetons", "32768", "--sortie-min-jetons", "4096", "--delai-s", "1500"]}
ETAPE_A_BLANC = "porte-a-blanc"
SORTIES_COURSES = tuple(Path(f"/home/user/sorties-course-affinage-mentors-v{k}") for k in range(1, 12))
MARQUEUR_A_REMPLIR = "À REMPLIR"
CLE_CLAUDE = "RR_ANTHROPIC_API_KEY_LUC"  # GO-2026-11-22-107
CLES_INTERDITES = ("RR_ANTHROPIC_API_KEY_RIGAUD", "RR_ANTHROPIC_API_KEY_MINUIT")  # Minuit : sans crédit (R-4833)
PREFIXE_CLES_CLAUDE = "RR_ANTHROPIC_API_KEY"
# v11 : part Claude estimée (deux proposeurs, aiguilleur, premier juge ; marge comprise) : écrite au manifeste pour information ;
# GO-2026-11-22-124 : aucune condition de départ sur le solde de LUC. v11c (constat 15) : aucun « haut ».
PART_CLAUDE_ESTIMEE_USD = 20.65
PLAFOND_PART_CLAUDE_USD = 45.0   # R-4995 : plafond propre de LUC ; égal à celui de la configuration v11, sinon refus
LIBELLE_CONTRE_LECTURE = "Opus 5.5, contre-lecteur neuf"  # v11c, constat 4 : libellé exigé (le texte écrit le même)
JUGE_PLAFOND_EXIGE_USD = 1.00  # v11c, constat 10 : plafond de session des juges exigé égal à 1,00 USD
PART_CLAUDE_GO_124_USD = 45.0  # v11c, constat 15 : montant écrit au plafond de GO-2026-11-22-124 (« part Claude 45 USD »)
INTERVALLE_SURVEILLANCE_S = 10.0
LECTURES_ILLISIBLES_MAX = 3


PREREG = f"{COURSE}/preenregistrement-course-affinage-mentors-v11.md"
PREREG_SHA256 = ""  # à poser quand le préenregistrement v11 sera écrit et scellé : d'ici là, aucun lancement (refus nommé)
CONTRE_LECTURE = f"{COURSE}/contre-lecture-preenregistrement-course-affinage-mentors-v11.md"
DECLARATION_RELAIS = f"{COURSE}/declaration-relais-course-affinage-mentors-v11.json"
RELEVE_CREDITS = f"{COURSE}/releve-credits-avant-course-affinage-mentors-v11.json"

PIECES = {
    "configuration": (f"{COURSE}/configuration-course-affinage-mentors-v11d.json", "7373818a288b540126c2610fe3715de8a9fad33ae8b0fa9e1d3bb4f47f07b0b1"),  # v11d : notes de la commande v2, plafond inerte retiré  # v9 + LUC + plafond de LUC
    "sonde_astra": ("scripts/sonde_astra_affinage_v3.py", "32366123751ba1d1620cadf4dd4cfda039c0bf35af614a75b49e2d9c04dad7ff"),
    "sonde_commune": ("scripts/sonde_astra_courses_v3.py", "d02971f0cbe6f15e5be1f58a5050ff86ca48bd9b6a059e478285315fda5c729e"),
    "commande_carbon": ("scripts/commande_gemini_flux_v2.py", "13b968eb440279eb77cd9858cefacfb54bc87b11cbf5fc47cf4476044f8e6a50"),
    # garde commune des appels à Google (règle gelée, GO-2026-11-21-71), pièce de `main` : présente dans le dépôt de travail
    "garde_google": ("src/controle_ia/garde_google_v3.py", "923679b51cfc84b65ff7cfc65296378d08e6d4e64f6b427823d23ba24f4afe91"),
    "garde_credit": ("scripts/garde_credit_relais_v6.py", "1d9882f71b01491c3282d24b963d14e8ad4339c855ec969f85b420c463c60fff"),
    "porte_plafond": ("scripts/porte_plafond_relais_v1.py", "fab5fe2e924c47799d968663baddfecb85dd6f74e9f859d9047b185eb36382b1"),
    "procedure_relais": (PROCEDURE_RELAIS, "d97594dbc2263cd4200113d44dd4fd3fc8562bef617d3e182f6a382bf95ec792"),
    "procedure_ecrite": ("docs/procedures/relais-persistants-v1.md", "0ca9cf5daa190135f8f26175f2639e4c9c4b22b01c551ab30ff8f7bb0d085148"),
    "lanceur_relais": ("scripts/lancer_relais_local_v1.py", "d365affcb0303283a71ac7d5e67e24a5b6060e3b13c2a9e83ea592e48d4b3c82"),
    "liste_fils": (f"{COURSE_V1}/fils-servis-et-retraits-course-affinage-mentors-v1.json", "c30928c88feffc16d3aa1119efe2a54ba2d70cf135b8068855190a21470a56bb"),
    "consigne_proposeur": (f"{COURSE_V1}/consigne-proposeur-course-affinage-mentors-v1.md", "d36ba0a01c1c190d55d0ed63b053c951b5a767a9310013321d797e3e203d8c4f"),
    "consigne_aiguilleur": (f"{COURSE_V1}/consigne-aiguilleur-course-affinage-mentors-v1.md", "903318d7659db07819cbe9a7f89cbdbd292f59e14c32bb8811d8f8cb35dd955b"),
    "consigne_juge": (f"{COURSE_V1}/consigne-juge-course-affinage-mentors-v1.md", "a32583b14845343a613514cdcba3c24831a274b48ecc95fe0d884f017d27d346"),
    "consigne_passe_tableau": (f"{COURSE_V1}/consigne-passe-tableau-course-affinage-mentors-v1.md", "1ac9791b6aea1c97f534e32980f1f837cca425806ce8235b1064d98ce261dcbf"),
    "enveloppe_argon": ("rapports/fille-ideation-1-v1/appel-argon-v5.sh",
                        "37c0205e26f83cbdcdf5ad7f1e4094a21c7dcc70afb72d15ef0d260a770a132a"),
    "commande_argon": ("docs/notes/ideation-organisme-v1/argon-recherche-v1/commande_argon_v3d.py",
                       "46c91df41b77a6d4cb7f5141993fda4a894118b5dd4ad1e5ba21a17dc2d67e46"),
}
PIECES_SERVIES = ("consigne_proposeur", "consigne_aiguilleur", "consigne_juge", "consigne_passe_tableau")
DEPOT_ATTENDU_PAR_L_ENVELOPPE = Path("/home/user/controle-ia-travail")

ORCHESTRATEURS_CANDIDATS = (Path("/home/user/ideation-organism/orchestrator"),
                            Path("/home/user/lciric/ideation-organism/orchestrator"))
COMMIT_ORCHESTRATEUR = "a41b7b50f7c64ce488c120bb89ad3d25fb1dd1cb"
LANCEUR_ORCHESTRATEUR = "demonstrations/ideation_v8.py"
EMPREINTES_ORCHESTRATEUR = {
    "demonstrations/ideation_v8.py": "2e2be8d72c548e183b94c14de20c971f241f998f54f64c5281b2427fdd64e9d1",
    "demonstrations/ideation_v7.py": "7b90e65e1308b1c230b3f804743cfc42b9dc571d93b73ed6c5f3f8c9d2b481b2",
    "demonstrations/ideation_v6.py": "4c302e5b97b229d5b3edd9e9a427f1e50796c10f7081f63132165ffeef854ba4",
    "demonstrations/ideation_v5.py": "1894f250264eaaccbf891dfa255e71dc587fe415c8d21e283391203a2fe73444",
    "demonstrations/ideation_v4.py": "4212d4c9d014a265847d4c4ed87a8cd804fdafa73f85fd8947874d63fca1c36d",
    "demonstrations/ideation_v2.py": "bc5e9c98acff41b97487e2345d33768c8cdf41f0ededf8b2eed0bf842c889845",
    "pole/configuration_v53.py": "ef72ffbf6b5ba546fb5e509502b59f0d9ac4f78772dcb9570ef36086639f4a78",
    "pole/configuration_v54.py": "3424ca7fa8911e5c2656cb56632f7d74c958008b9366af0ac45e6a62e4d16d66",
    "pole/configuration_v55.py": "2e6237c0a8b1c823fa17ddd6c680357a59ec4030bfbe9ac6ba970a700a864071",
    "pole/configuration_v56.py": "122405228d6ec550b2120114e87a1e70bcc74c14eee17342605d8402bd015d6b",
    "pole/course2_v53.py": "8f2d035828df913d8fa92e1b7d0c8e41ac73e8416e60f3b674753c27f5c61237",
    "pole/course2_v54.py": "ac1980d04eb88d8fbb9a073902e47146ab9eadd3375a41cd72835fa5acf20342",
    "pole/course2_v55.py": "ee6a861e7f8db32a9545372a51f902389cdbea809b0ba354e621a3681e541a70",
    "pole/course2_v56.py": "14f655696876afc8453ec5237236b3f9daf8d87844c4acc9d5189b3e61b310f1",
    "pole/budget_v56.py": "3a672aceeeee3cf83cd4e46ca461fdbaf3acd0a9552be24d2566627ce6b7c13e",
    "pole/adaptateurs.py": "a1a8ede8d38884a28365ee797dcd3018dbf09ea1baefa3f57cfcb3281c529c99",
    "pole/adaptateurs_v56.py": "d36c79b272af450b8d67313f44068743d80f0204bcedbd30f5d879829c945a17",
    "pole/adaptateur_kimi_v53.py": "09a46515ff30a99f360fcbc7d4c613c35cb511439a5b6c249327e477fdee4ada",
    "pole/aiguilleur_v53.py": "a856cdaa37e8fb1f3b873ef2c0d9aa439ee0a8838f5ee9a2910cb3c0dcf8007f",
    "pole/juges_croises_v53.py": "c4c6ab12dc471eef078c116a4205a22d9b498da720ce71e37a0a6edae6c4239b",
    "pole/memoire_v53.py": "43b01b43b1ec347ff02b456975d74c17e7a0e974e9b95e9ba4935bdb895f31a0",
    "pole/noyau_v56.py": "eb5a003e8f23b0882e5588fe537e8b65b890f0d7d19560896be4e85a0731543b",
    "pole/gardes_e0_v56.py": "921e59f23753666d6367678447edf4ee2964dc6ec3d382aefa8582b996e123b9",
    "pole/simulation_v56.py": "bcafca44c5117dfd30262ee520a67944d051208f1b1deac6fac016e8cb95dc76",
    "pole/relais_reel_v2.py": "98c3e79e2c795a69345ffcf9aa742e31dde4a578a15f7c610f1ec7fd535ac8d7",
}

# Devis v6 et v6b (`devis-course-affinage-mentors-v6.md`, `…-v6b.md`, mêmes prix par appel que la v3 et la v5 ; noms des
# constantes gardés), estimation par appel, USD : sert à l'écart au devis (garde 5).
# v8 (devis v8, `devis-course-affinage-mentors-v8.md`) : prix estimé d'un appel de Carbon 0,4985 USD au lieu de 0,276 — pensée
# 20 000 jetons (plus forte pensée observée, arrondie), sortie 3 500, entrée gardée 2 618 (fil le plus long), au prix plein
# 8,3 / 41,5 USD par million × facteur du lot 0,5 ; les autres prix sont ceux du devis v6.
# v11c (constat 1) : Argon ramené de 8,3 / 41,5 à 4 / 20 USD par million (postes mesurés du devis v6 × 20 / 41,5, comme le
# calcul du devis v11b, `calcul-devis-course-affinage-mentors-v11b.py`) ; constantes nommées, que Fable recalculera aux réglages
# réels ; Carbon au prix exact d'un appel estimé (2 618 × 4 + 23 500 × 20, par million = 0,480472) : base 35,683 (cinq espèces).
PRIX_ARGON_PROPOSEUR_PAR_APPEL_USD = round(0.276 * 20 / 41.5, 6)   # 0,133012
PRIX_ARGON_JUGE_PAR_APPEL_USD = round(0.0347 * 20 / 41.5, 6)       # 0,016723
PRIX_CARBON_PAR_APPEL_USD = round((2618 * 4 + (20000 + 3500) * 20) / 1e6, 6)  # 0,480472
DEVIS_V5_PAR_APPEL = {"prop-opus": 0.141, "prop-fable": 0.3525, "prop-argon": PRIX_ARGON_PROPOSEUR_PAR_APPEL_USD, "prop-kimi": 0.276,
                      "prop-astra": 0.276, "prop-carbon": PRIX_CARBON_PAR_APPEL_USD, "aiguilleur": 0.031, "juge-opus": 0.037,
                      "juge-argon": PRIX_ARGON_JUGE_PAR_APPEL_USD}
# v11 : Carbon en flux, sans remise de lot : 2 618 × 8,3 + (20 000 + 3 500) × 41,5, par million = 0,996979, arrondi 0,997 ;
# R-5018 (4 / 20 USD par million, réflexion comprise) : un appel estimé 2 618 × 4 + (20 000 + 3 500) × 20, par million =
# 0,480472, arrondi 0,4805 ; pire cas : 2 618 × 4 + 65 536 × 20, par million = 1,321192 USD (la commande compte la réflexion
# dans la sortie maximale) ; 1,894632 si la réflexion était facturée en plus de la sortie maximale ; sous 3,00 dans les deux cas.
# v7, mineur 4 : base du devis recalculée sur les espèces actives (16 appels par espèce ; 2 cartes × 16 cases par espèce pour
# l'aiguilleur et chacun des deux juges) ; ces deux totaux ne servent plus qu'aux essais. v8 : cinq espèces déclarées (Carbon
# comprise) 37,576 + 16 × (0,4985 − 0,276) = 41,136 ; six (Kimi en plus) 45,2784 + 3,56 = 48,8384.
DEVIS_V5_TOTAL = {"cinq_especes": 35.683424, "six_especes": 42.81056}  # v11c : base du texte (35,683 pour cinq espèces)

DOSSIER_SORTIES = Path("/home/user/sorties-course-affinage-mentors-v11")
SUFFIXE_RUN = "-course-affinage-mentors-v11"
SUFFIXES_DEJA_LANCEE = tuple(f"-course-affinage-mentors-v{k}" for k in range(1, 12))  # une seule course, quelle que soit la version
NOMS_PERMIS = ("PATH", "LANG", "LC_ALL", "TZ", "TMPDIR")
NOMS_DE_CLE = ("ANTHROPIC_API_KEY", "ANTHROPIC_AUTH_TOKEN", "CLAUDE_CODE_OAUTH_TOKEN", "OPENAI_API_KEY", "GOOGLE_API_KEY",
               "GEMINI_API_KEY", "KIMI_API_KEY", "AWS_SECRET_ACCESS_KEY", "AWS_SESSION_TOKEN", "GITHUB_TOKEN", "GH_TOKEN", "HF_TOKEN")
MOTIF_NOM_DE_CLE = re.compile(r"(API_?KEY|TOKEN|SECRET|PASSWORD|PASSWD|CREDENTIAL)", re.I)
MOTIF_VALEUR_DE_CLE = re.compile(r"(sk-ant-[A-Za-z0-9]|sk-[A-Za-z0-9]{20,}|ghp_[A-Za-z0-9]{20,}|hf_[A-Za-z0-9]{20,}|AKIA[A-Z0-9]{12}|"
                                 r"AIza[0-9A-Za-z_-]{20,}|Bearer\s+[A-Za-z0-9._-]{16,})")
NOM_DE_VARIABLE = re.compile(r"^[A-Z][A-Z0-9_]{1,63}$")
URL_LOCALE = re.compile(r"^http://(127\.0\.0\.1|localhost|\[::1\]):\d{2,5}(/.*)?$")
MODELES_CLAUDE = ("claude-opus-5-5", "claude-fable-5-1")
TYPES_PERMIS = {"claude": "claude_sdk", "argon": "commande_externe", "kimi": "kimi_protocole", "astra": "commande_externe",
                "carbon": "commande_externe"}
CLES_PERMISES = {"claude_sdk": {"type", "url_relais", "porte_plafond"},
                 "commande_externe": {"type", "commande", "modeles_servis_permis", "porte_plafond"},
                 "kimi_protocole": {"type", "url_relais", "modele", "prix_entree", "prix_sortie", "max_sortie_jetons",
                                    "sortie_min_jetons", "delai_s", "porte_plafond"}}
CLES_META = {"nom_cle", "modele_propose", "inscription", "pid_relais"}

SONDE_BAC_A_SABLE = (
    "import json, sys\n"
    "sys.path.insert(0, sys.argv[1])\n"
    "from pole.adaptateurs import etat_bac_a_sable_detaille\n"
    "print(json.dumps(etat_bac_a_sable_detaille()))\n"
)


class Refus(RuntimeError):
    """Garde du lanceur : rien n'est lancé (code 2)."""


class AlerteCredit(RuntimeError):
    """Garde (2) : un reste est sous un seuil ; alerte écrite, arrêt avant le départ (code 3)."""


def sha256_fichier(chemin: Path) -> str:
    h = hashlib.sha256()
    with open(chemin, "rb") as f:
        for bloc in iter(lambda: f.read(1 << 20), b""):
            h.update(bloc)
    return h.hexdigest()


def date_u() -> str:
    r = subprocess.run(["date", "-u"], capture_output=True, text=True, timeout=10)
    if r.returncode != 0 or not r.stdout.strip():
        raise Refus("`date -u` illisible")
    return r.stdout.strip()


def _normaliser(texte: str) -> str:
    return unicodedata.normalize("NFKD", texte.lower()).encode("ascii", "ignore").decode()


def scelle(chemin: Path) -> bool:
    """Compagnon `.sha256` présent, une ligne « empreinte  nom », égal à l'empreinte du fichier."""
    c = Path(str(chemin) + ".sha256")
    if not chemin.is_file() or not c.is_file():
        return False
    lignes = [x for x in c.read_text(encoding="utf-8").splitlines() if x.strip()]
    if len(lignes) != 1:
        return False
    m = re.match(r"^([0-9a-f]{64})  (\S.*)$", lignes[0])
    return bool(m) and m.group(2) == chemin.name and m.group(1) == sha256_fichier(chemin)


def ecrire_scelle(chemin: Path, contenu) -> str:
    if chemin.exists():
        raise Refus(f"{chemin} existe déjà (R12)")
    if isinstance(contenu, (bytes, str)):
        donnees = contenu.encode("utf-8") if isinstance(contenu, str) else contenu
    else:
        donnees = (json.dumps(contenu, ensure_ascii=False, indent=1, sort_keys=True) + "\n").encode("utf-8")
    with open(chemin, "xb") as f:
        f.write(donnees)
    h = hashlib.sha256(donnees).hexdigest()
    with open(str(chemin) + ".sha256", "x", encoding="utf-8") as f:
        f.write(f"{h}  {chemin.name}\n")
    return h


@dataclass
class Reglages:
    depot: Path
    orchestrateurs: tuple
    commit_orchestrateur: str
    empreintes_orchestrateur: dict
    pieces: dict
    prereg: tuple
    contre_lecture: Path
    declaration: Path
    releve: Path
    registre_go: Path
    procedure_relais: Path
    releve_prix: Path
    dossier_runs: Path
    dossier_sorties: Path
    depot_attendu_par_l_enveloppe: Path
    python: str
    lanceur: Path
    moteur: str = "reel"
    environnement: dict | None = None
    aujourd_hui: _dt.date | None = None
    horodatage: object = date_u
    exiger_bac_a_sable: bool = True
    sorties_courses: tuple = SORTIES_COURSES
    programmes_relais: dict | None = None
    lire_cmdline: object = None
    lire_etat_relais: object = None
    ref_registre: str | None = "origin/main"
    verifier_go: bool = True
    sondes_astra_v2: tuple = SONDES_ASTRA_V2               # v7 : chemins relatifs au dépôt, « {jour} » = jour du lancement
    sondes_astra_communes: tuple = SONDES_ASTRA_COMMUNES
    references_kimi_admises: tuple = REFERENCES_KIMI_ADMISES
    controler_google: object = None          # v11 : None = la garde réelle (commandes jouées hors ligne devant un faux amont)
    intervalle_surveillance_s: float = INTERVALLE_SURVEILLANCE_S

    @classmethod
    def production(cls) -> "Reglages":
        return cls(depot=DEPOT, orchestrateurs=ORCHESTRATEURS_CANDIDATS, commit_orchestrateur=COMMIT_ORCHESTRATEUR,
                   empreintes_orchestrateur=dict(EMPREINTES_ORCHESTRATEUR), pieces=dict(PIECES),
                   prereg=(DEPOT / PREREG, PREREG_SHA256), contre_lecture=DEPOT / CONTRE_LECTURE,
                   declaration=DEPOT / DECLARATION_RELAIS, releve=DEPOT / RELEVE_CREDITS,
                   registre_go=DEPOT / "registres" / "go.md", procedure_relais=DEPOT / PROCEDURE_RELAIS, releve_prix=DEPOT / RELEVE_PRIX, dossier_runs=DEPOT / "runs", dossier_sorties=DOSSIER_SORTIES,
                   depot_attendu_par_l_enveloppe=DEPOT_ATTENDU_PAR_L_ENVELOPPE, python=sys.executable,
                   lanceur=Path(__file__).resolve())


# --- (1) GO, une seule course -------------------------------------------------------------------------------------------------


def _est_revocation(cellules: list, go_id: str) -> bool:
    return any(_normaliser(c).startswith("revoc") for c in cellules) and any(go_id in c for c in cellules)


def verifier_go(registre: Path, aujourd_hui: _dt.date, go_id: str = GO_ID, prolongation: str | None = None) -> dict:
    """Même lecture que le lanceur de référence ; plafond lu exactement égal au plafond d'arrêt (150 USD)."""
    if not registre.is_file():
        raise Refus(f"registre des GO absent : {registre}")
    ligne_go = re.compile(r"^\|\s*(GO-\d{4}-\d{2}-\d{2}-\d{2,3})\s*\|")
    trouvees, revocations = [], []
    for ligne in registre.read_text(encoding="utf-8").splitlines():
        m = ligne_go.match(ligne)
        if not m:
            continue
        cellules = [c.strip() for c in ligne.strip().strip("|").split("|")]
        if m.group(1) == go_id:
            trouvees.append(cellules)
        elif _est_revocation(cellules, go_id):
            revocations.append(m.group(1))
    principales = [c for c in trouvees if not (len(c) == 8 and c[3].lower().startswith("extension"))]
    if len(principales) != 1:
        raise Refus(f"{go_id} : {len(principales)} ligne(s) principale(s) dans {registre.name} (une exigée)")
    c = principales[0]
    if len(c) != 8:
        raise Refus(f"{go_id} : ligne mal formée ({len(c)} colonnes, 8 attendues)")
    ident, accorde, typ, perimetre, plafond, echeance, par, _ref = c
    if typ != "calcul":
        raise Refus(f"{go_id} : type {typ!r}, « calcul » exigé")
    if par != "Lazar":
        raise Refus(f"{go_id} : accordé par {par!r}, Lazar exigé")
    try:
        d_acc, d_ech = _dt.date.fromisoformat(accorde), _dt.date.fromisoformat(echeance)
    except ValueError:
        raise Refus(f"{go_id} : dates illisibles ({accorde!r}, {echeance!r})") from None
    fin = max(d_ech, _dt.date.fromisoformat(prolongation)) if prolongation else d_ech  # v11 : prolongée par GO-2026-11-22-80
    if not d_acc <= aujourd_hui <= fin:
        raise Refus(f"{go_id} hors de sa période de validité ({d_acc} → {fin}, aujourd'hui {aujourd_hui}) ; prolongation "
                    f"valide : {prolongation or 'aucune'}")
    if revocations:
        raise Refus(f"{go_id} révoqué par {', '.join(sorted(revocations))}")
    p = _normaliser(perimetre)
    if "mentors" not in p and "affinage" not in p:
        raise Refus(f"{go_id} : périmètre sans « mentors » ni « affinage » — ce n'est pas le GO de cette course")
    m_plafond = re.match(r"^\s*(\d+(?:[.,]\d+)?)\s*(?:USD|usd)\s*(?:\([^()0-9]*\))?\s*$",
                         re.sub(r"GO-\d{4}-\d{2}-\d{2}-\d{2,3}", "GO", plafond))  # v11b : renvoi au GO prolongé admis
    if not m_plafond:
        raise Refus(f"{go_id} : plafond illisible {plafond!r} (un nombre + USD attendu)")
    plafond_lu = float(m_plafond.group(1).replace(",", "."))
    if plafond_lu != PLAFOND_ARRET_USD:
        raise Refus(f"{go_id} : plafond lu {plafond_lu} USD != plafond d'arrêt {PLAFOND_ARRET_USD} USD")
    return {"id": ident, "accorde": accorde, "echeance": echeance, "plafond": plafond, "plafond_lu": plafond_lu, "par": par,
            "ligne_sha256": hashlib.sha256(("|".join(c)).encode("utf-8")).hexdigest()}


def verifier_go_exception_cle(registre: Path, aujourd_hui: _dt.date, go_id: str = GO_EXCEPTION_CLE,
                              prolongation: str | None = None) -> dict:
    """v11 : la ligne de l'exception déclarée (GO-2026-11-22-107) : une seule ligne, type « calcul », accordée par Lazar, en
    période, non révoquée, dont le périmètre nomme la clé Claude de la course, la règle « Claude par l'abonnement »
    (GO-2026-11-22-70) et la course (« mentors » ou « affinage ») ; son plafond, en mots, renvoie au GO de la course."""
    if not registre.is_file():
        raise Refus(f"registre des GO absent : {registre}")
    ligne_go = re.compile(r"^\|\s*(GO-\d{4}-\d{2}-\d{2}-\d{2,3})\s*\|")
    trouvees, revocations = [], []
    for ligne in registre.read_text(encoding="utf-8").splitlines():
        m = ligne_go.match(ligne)
        if not m:
            continue
        cellules = [c.strip() for c in ligne.strip().strip("|").split("|")]
        if m.group(1) == go_id:
            trouvees.append(cellules)
        elif _est_revocation(cellules, go_id):
            revocations.append(m.group(1))
    if len(trouvees) != 1 or len(trouvees[0]) != 8:
        raise Refus(f"{go_id} : {len(trouvees)} ligne(s) dans {registre.name} (une ligne de 8 colonnes exigée) — exception de clé "
                    f"non trouvée : aucun appel Claude par l'interface")
    ident, accorde, typ, perimetre, plafond, echeance, par, _ref = trouvees[0]
    if typ != "calcul" or par != "Lazar":
        raise Refus(f"{go_id} : type {typ!r} accordé par {par!r} (« calcul », Lazar exigés)")
    try:
        d_acc, d_ech = _dt.date.fromisoformat(accorde), _dt.date.fromisoformat(echeance)
    except ValueError:
        raise Refus(f"{go_id} : dates illisibles ({accorde!r}, {echeance!r})") from None
    fin = max(d_ech, _dt.date.fromisoformat(prolongation)) if prolongation else d_ech  # v11 : prolongée par GO-2026-11-22-124
    if not d_acc <= aujourd_hui <= fin:
        raise Refus(f"{go_id} hors de sa période de validité ({d_acc} → {fin}, aujourd'hui {aujourd_hui})")
    if revocations:
        raise Refus(f"{go_id} révoqué par {', '.join(sorted(revocations))}")
    p = _normaliser(perimetre)
    if CLE_CLAUDE not in perimetre or REGLE_ABONNEMENT not in perimetre or not ("mentors" in p or "affinage" in p):
        raise Refus(f"{go_id} : le périmètre doit nommer {CLE_CLAUDE}, la règle {REGLE_ABONNEMENT} et la course d'affinage")
    if GO_COURSE_INITIAL not in plafond:
        raise Refus(f"{go_id} : le plafond doit renvoyer au plafond d'arrêt de {GO_COURSE_INITIAL}")
    return {"id": ident, "accorde": accorde, "echeance": echeance, "par": par, "regle_exceptee": REGLE_ABONNEMENT,
            "precisions_citees": list(GO_PRECISIONS_CLE),
            "ligne_sha256": hashlib.sha256(("|".join(trouvees[0])).encode("utf-8")).hexdigest()}


GO_SIMPLIFICATION_CLE = "GO-2026-11-22-124"


def verifier_go_simplification(registre: Path, aujourd_hui: _dt.date, go_id: str = GO_SIMPLIFICATION_CLE) -> dict:
    """v11 : la ligne GO-2026-11-22-124 (mots de Lazar) : une ligne, accordée par Lazar, en période, non révoquée, qui nomme
    GO-2026-11-22-107 (prolongée) ; rend son échéance (prolongation de l'exception de clé)."""
    if not registre.is_file():
        raise Refus(f"registre des GO absent : {registre}")
    ligne_go = re.compile(r"^\|\s*(GO-\d{4}-\d{2}-\d{2}-\d{2,3})\s*\|")
    trouvees, revocations = [], []
    for ligne in registre.read_text(encoding="utf-8").splitlines():
        m = ligne_go.match(ligne)
        if not m:
            continue
        cellules = [c.strip() for c in ligne.strip().strip("|").split("|")]
        if m.group(1) == go_id:
            trouvees.append(cellules)
        elif _est_revocation(cellules, go_id):
            revocations.append(m.group(1))
    if len(trouvees) != 1 or len(trouvees[0]) != 8:
        raise Refus(f"{go_id} : {len(trouvees)} ligne(s) (une ligne de 8 colonnes exigée) : règle de la clé Claude non trouvée")
    ident, accorde, typ, perimetre, plafond, echeance, par, _ref = trouvees[0]
    if par != "Lazar" or typ not in ("calcul", "décision"):
        raise Refus(f"{go_id} : type {typ!r} accordé par {par!r} (Lazar exigé)")
    try:
        d_acc, d_ech = _dt.date.fromisoformat(accorde), _dt.date.fromisoformat(echeance)
    except ValueError:
        raise Refus(f"{go_id} : dates illisibles ({accorde!r}, {echeance!r})") from None
    if not d_acc <= aujourd_hui <= d_ech:
        raise Refus(f"{go_id} hors de sa période de validité ({d_acc} → {d_ech}, aujourd'hui {aujourd_hui})")
    if revocations:
        raise Refus(f"{go_id} révoqué par {', '.join(sorted(revocations))}")
    m45 = re.search(r"part Claude\s+(\d+(?:[.,]\d+)?)\s*USD", plafond)  # v11c, constat 15 : le montant lu, pas une sous-chaîne
    if GO_EXCEPTION_CLE not in perimetre or not m45 or float(m45.group(1).replace(",", ".")) != PART_CLAUDE_GO_124_USD:
        raise Refus(f"{go_id} : le périmètre doit nommer {GO_EXCEPTION_CLE} (prolongée) et le plafond, « part Claude 45 USD » "
                    f"(lu : {m45.group(0) if m45 else 'aucun montant'!r})")
    return {"id": ident, "accorde": accorde, "echeance": echeance, "par": par,
            "ligne_sha256": hashlib.sha256(("|".join(trouvees[0])).encode("utf-8")).hexdigest()}


GO_PROLONGATION_COURSE = "GO-2026-11-22-80"   # prolonge GO-2026-11-18-14 au 15 décembre
assert GO_PROLONGATION_COURSE == GO_ID          # v11b : la prolongation est le GO de la course


def verifier_go_initial(registre: Path) -> dict:
    """v11b : la ligne de GO-2026-11-18-14 (prolongé par GO-80) est exigée : une seule, de type « calcul », accordée par Lazar,
    non révoquée ; sa propre échéance ne borne plus (la période est celle de GO-80)."""
    c, rev = lire_ligne_go(registre, GO_COURSE_INITIAL)
    if c is None:
        raise Refus(f"{GO_COURSE_INITIAL} (GO prolongé par {GO_ID}) : ligne absente ou mal formée")
    ident, accorde, typ, _perimetre, _plafond, echeance, par, _ref = c
    if typ != "calcul" or par != "Lazar":
        raise Refus(f"{GO_COURSE_INITIAL} : type {typ!r} accordé par {par!r} (« calcul », Lazar exigés)")
    if rev:
        raise Refus(f"{GO_COURSE_INITIAL} (prolongé par {GO_ID}) révoqué par {', '.join(sorted(rev))}")
    return {"id": ident, "accorde": accorde, "echeance": echeance, "par": par,
            "ligne_sha256": hashlib.sha256(("|".join(c)).encode("utf-8")).hexdigest()}


def lire_ligne_go(registre: Path, go_id: str) -> tuple:
    """(cellules de la ligne unique de `go_id` ou None, révocations qui la visent)."""
    ligne_go = re.compile(r"^\|\s*(GO-\d{4}-\d{2}-\d{2}-\d{2,3})\s*\|")
    trouvees, revocations = [], []
    for ligne in registre.read_text(encoding="utf-8").splitlines():
        m = ligne_go.match(ligne)
        if not m:
            continue
        cellules = [c.strip() for c in ligne.strip().strip("|").split("|")]
        if m.group(1) == go_id:
            trouvees.append(cellules)
        elif _est_revocation(cellules, go_id):
            revocations.append(m.group(1))
    return (trouvees[0] if len(trouvees) == 1 and len(trouvees[0]) == 8 else None), revocations


def lire_prolongation(registre: Path, aujourd_hui: _dt.date, go_id: str, go_vise: str, mot: str = "prolong") -> dict:
    """Une ligne de prolongation : accordée par Lazar, non révoquée, en période, qui nomme le GO visé et dit « prolong… ».
    Rend {valide, echeance, motif} ; une ligne absente ou invalide n'est jamais tue : le motif est écrit au manifeste, et le GO
    visé garde sa propre échéance (au-delà, refus)."""
    c, rev = lire_ligne_go(registre, go_id) if registre.is_file() else (None, [])
    if c is None:
        return {"id": go_id, "valide": False, "motif": "ligne absente ou mal formée"}
    ident, accorde, typ, perimetre, plafond, echeance, par, _ref = c
    try:
        d_acc, d_ech = _dt.date.fromisoformat(accorde), _dt.date.fromisoformat(echeance)
    except ValueError:
        return {"id": go_id, "valide": False, "motif": "dates illisibles"}
    motifs = []
    if par != "Lazar":
        motifs.append(f"accordée par {par!r}")
    if rev:
        motifs.append(f"révoquée par {', '.join(sorted(rev))}")
    if go_vise not in perimetre or mot not in _normaliser(perimetre):
        motifs.append(f"ne dit pas prolonger {go_vise}")
    if not d_acc <= aujourd_hui <= d_ech:
        motifs.append(f"hors période ({d_acc} → {d_ech})")
    if motifs:
        return {"id": go_id, "valide": False, "motif": " ; ".join(motifs)}
    return {"id": ident, "valide": True, "echeance": echeance, "go_vise": go_vise,
            "ligne_sha256": hashlib.sha256(("|".join(c)).encode("utf-8")).hexdigest()}


def verifier_confirmation_107(registre: Path, aujourd_hui: _dt.date, fixe: dict) -> dict:
    """GO-2026-11-22-124 dit la prolongation de GO-2026-11-22-107 « à confirmer par Lazar » : elle ne vaut que si la ligne de
    confirmation est **nommée** dans la configuration (`changements_v11.confirmation_prolongation_go_107`) et **inscrite** au
    registre (Lazar, non révoquée, en période, qui nomme GO-2026-11-22-107). Non nommée : aucune prolongation (au-delà du
    25 novembre, refus). Nommée mais absente ou invalide : refus."""
    nom = (fixe.get("changements_v11") or {}).get("confirmation_prolongation_go_107", "absente")
    if nom == "absente":
        raise Refus("configuration : emplacement changements_v11.confirmation_prolongation_go_107 absent (null s'il n'y a pas "
                    "de confirmation)")
    if nom is None:
        return {"nommee": None, "valide": False, "motif": "aucune confirmation nommée dans la configuration"}
    if not isinstance(nom, str) or not re.fullmatch(r"GO-\d{4}-\d{2}-\d{2}-\d{2,3}", nom):
        raise Refus(f"configuration : confirmation_prolongation_go_107 = {nom!r} : identifiant de GO exigé")
    o = lire_prolongation(registre, aujourd_hui, nom, GO_EXCEPTION_CLE, mot="")
    if not o["valide"]:
        raise Refus(f"confirmation de la prolongation de {GO_EXCEPTION_CLE} nommée ({nom}) mais non valide au registre : {o['motif']}")
    return dict(o, nommee=nom)


def verifier_les_go(registre: Path, aujourd_hui: _dt.date, fixe: dict) -> dict:
    """v11 : GO de la course (GO-2026-11-18-14, prolongé par GO-2026-11-22-80 s'il est valide), règle de la clé
    (GO-2026-11-22-124), exception de clé (GO-2026-11-22-107, prolongée à l'échéance de GO-124 seulement sous confirmation)."""
    go_conf = (fixe.get("changements_v11") or {}).get("go_course")
    if go_conf != GO_ID:
        raise Refus(f"configuration : changements_v11.go_course = {go_conf!r}, {GO_ID} exigé (GO de la course, v11b)")
    if not registre.is_file():
        raise Refus(f"registre des GO absent : {registre}")
    p80 = lire_prolongation(registre, aujourd_hui, GO_PROLONGATION_COURSE, GO_COURSE_INITIAL)
    if not p80["valide"]:  # v11b : GO-80 est le GO de la course ; absent ou invalide, la course ne part pas
        raise Refus(f"{GO_PROLONGATION_COURSE} (GO de la course, prolongation de {GO_COURSE_INITIAL}) non valide : {p80['motif']}")
    go = verifier_go(registre, aujourd_hui)
    p80 = dict(p80, go_initial=verifier_go_initial(registre))
    simpl = verifier_go_simplification(registre, aujourd_hui)
    conf = verifier_confirmation_107(registre, aujourd_hui, fixe)
    cle = verifier_go_exception_cle(registre, aujourd_hui, prolongation=simpl["echeance"] if conf["valide"] else None)
    return {"go": go, "prolongation_course": p80, "simplification": simpl, "confirmation_107": conf, "exception_cle": cle}


def verifier_plafond_luc(fixe: dict) -> float:
    """v11 (R-4995) : plafond propre de LUC lu dans la configuration et égal à la constante du lanceur ; ni retiré, ni relevé,
    au plus le plafond d'arrêt de la course."""
    bloc = fixe.get("changements_v11") or {}
    lu, part = bloc.get("plafond_part_claude_usd"), bloc.get("part_de_la_couverture")
    if not _nombre(lu) or float(lu) != PLAFOND_PART_CLAUDE_USD or not 0 < PLAFOND_PART_CLAUDE_USD <= PLAFOND_ARRET_USD:
        raise Refus(f"plafond propre de {CLE_CLAUDE} : configuration {lu!r}, lanceur {PLAFOND_PART_CLAUDE_USD!r} ; 45 USD exigés "
                    "aux deux (R-4995) : un plafond retiré ou relevé ne part pas")
    if part is not None:  # GO-2026-11-22-124 : plus de part de la couverture ; sa présence est un reste d'une règle retirée
        raise Refus("configuration : changements_v11.part_de_la_couverture présent alors que GO-2026-11-22-124 l'a retiré")
    return float(lu)


def appliquer_emplacement_argon(fixe: dict) -> dict:
    """v11 (brouillon 1 du préenregistrement v11, point 4) : `argon_v11.plafond_session_juge_usd` de la configuration ; vide
    (null) : en attente du mot de la mère, plafond des juges inchangé ; rempli : réel dans ]0 ; 3,00] qui remplace
    `plafonds_session.juge` (les deux juges : l'orchestrateur n'a qu'un plafond par rôle) ; toute autre valeur : refus."""
    bloc = fixe.get("argon_v11")
    if not isinstance(bloc, dict) or "plafond_session_juge_usd" not in bloc:
        raise Refus("configuration : emplacement argon_v11.plafond_session_juge_usd absent (v11)")
    v = bloc["plafond_session_juge_usd"]
    avant = fixe["plafonds_session"]["juge"]
    if not _nombre(v) or float(v) != JUGE_PLAFOND_EXIGE_USD:  # v11c, constat 10 : égalité exigée (vide compris : refus)
        raise Refus(f"configuration : argon_v11.plafond_session_juge_usd = {v!r} : {JUGE_PLAFOND_EXIGE_USD:.2f} USD exactement "
                    "exigé (devis v11, texte v11)")
    fixe["plafonds_session"]["juge"] = float(v)
    return {"plafond_session_juge_usd": float(v), "emplacement": float(v), "avant": avant, "statut": "rempli"}


def verifier_course_jamais_lancee(r: Reglages) -> None:
    """Une course est « lancée » dès que son manifeste de départ existe ; un essai refusé avant lui ne bloque rien."""
    if r.dossier_runs.is_dir():
        deja = sorted(p.name for p in r.dossier_runs.iterdir()
                      if p.name.endswith(SUFFIXES_DEJA_LANCEE) and (p / "manifeste-lanceur-depart.json").exists())
        if deja:
            raise Refus(f"course déjà lancée sous ce lanceur ({deja}) : une relance est une nouvelle version et un mot de la mère")
    for d in r.sorties_courses:  # v4, constat 11 ; v5, constat 1 : seul un journal de course compte, pas un dossier laissé par un refus
        lancees = sorted(x.name for x in d.iterdir() if (x / "course.stdout.txt").exists()) if d.is_dir() else []
        if lancees:
            raise Refus(f"course d'affinage déjà lancée (journal hors dépôt) : {d} {lancees} — une seule course")


# --- (3) préenregistrement, contre-lecture, liste des retraits ----------------------------------------------------------------


def verifier_preenregistrement(r: Reglages) -> dict:
    chemin, attendu = r.prereg
    if not re.fullmatch(r"[0-9a-f]{64}", attendu or ""):
        raise Refus("empreinte du préenregistrement non posée dans le lanceur : aucun lancement")
    if not chemin.is_file():
        raise Refus(f"préenregistrement absent : {chemin}")
    lu = sha256_fichier(chemin)
    if lu != attendu:
        raise Refus(f"préenregistrement d'empreinte {lu}, {attendu} épinglée")
    if not scelle(chemin):
        raise Refus("préenregistrement non scellé (compagnon .sha256 absent ou faux)")
    return {"chemin": str(chemin.relative_to(r.depot)) if chemin.is_relative_to(r.depot) else str(chemin), "sha256": lu}


def lire_verdict(texte: str) -> str | None:
    lignes = texte.splitlines()
    for i, l in enumerate(lignes):
        if re.match(r"^#{1,3}\s*Verdict\b", l.strip()):
            for suite in lignes[i + 1:]:
                if suite.strip():
                    return suite.strip()
    return None


VERDICTS_EXACTS = ("Scellable.", "**Scellable.**")
AVEUX_NON_RELU = re.compile(r"(n'ai pas (re)?lu|pas (ete )?relu|non relu|sans (la )?relire|sans relecture|n'a pas (ete )?(re)?lu|"
                            r"lecture partielle du (preenregistrement|lanceur)|pas pu (re)?lire)")


def verdict_favorable(verdict: str | None) -> bool:
    """v2 (garde stricte) : la première ligne du verdict est exactement « Scellable. » (en gras ou non), rien d'autre."""
    return isinstance(verdict, str) and verdict.strip() in VERDICTS_EXACTS


def verifier_contre_lecture(r: Reglages, prereg_sha: str, lanceur_sha: str) -> dict:
    c = r.contre_lecture
    if not c.is_file():
        raise Refus(f"contre-lecture absente : {c} (R2 : aucun lancement sans contre-lecture scellée)")
    if not scelle(c):
        raise Refus("contre-lecture non scellée (compagnon .sha256 absent ou faux)")
    texte = c.read_text(encoding="utf-8")
    if prereg_sha not in texte:
        raise Refus("la contre-lecture ne cite pas l'empreinte du préenregistrement épinglé")
    if lanceur_sha not in texte:
        raise Refus("la contre-lecture ne cite pas l'empreinte de ce lanceur (elle n'a pas lu cette version)")
    v = lire_verdict(texte)
    if not verdict_favorable(v):
        raise Refus(f"verdict de la contre-lecture défavorable, illisible ou inexact : {v!r} (première ligne exacte « Scellable. » exigée)")
    if _normaliser(LIBELLE_CONTRE_LECTURE) not in _normaliser(texte):  # v11c, constat 4
        raise Refus(f"la contre-lecture ne porte pas le libellé « {LIBELLE_CONTRE_LECTURE} » (contre-lecteur attendu, v11)")
    aveu = AVEUX_NON_RELU.search(_normaliser(texte).replace("’", "'"))
    if aveu:
        raise Refus(f"la contre-lecture dit n'avoir pas relu ({aveu.group(0)!r}) : refusée")
    return {"chemin": str(c), "sha256": sha256_fichier(c), "verdict": v}


def verifier_pieces(r: Reglages) -> dict:
    if r.moteur == "reel" and r.depot.resolve() != r.depot_attendu_par_l_enveloppe.resolve():
        raise Refus(f"dépôt de travail en {r.depot}, l'enveloppe d'Argon v5 attend {r.depot_attendu_par_l_enveloppe}")
    lues, ecarts = {}, {}
    for nom, (rel, attendu) in sorted(r.pieces.items()):
        p = r.depot / rel
        lu = sha256_fichier(p) if p.is_file() else None
        if lu != attendu:
            ecarts[nom] = {"chemin": rel, "attendu": attendu, "lu": lu}
        lues[nom] = {"chemin": rel, "absolu": str(p), "sha256": lu}
    if ecarts:
        raise Refus("pièces absentes ou d'empreinte différente (R11) : " + json.dumps(ecarts, ensure_ascii=False))
    return lues


def verifier_liste(liste: dict) -> dict:
    """Garde (3), dernier point : aucune entrée servie dans la liste des retraits ; aucun jeton réservé servi."""
    retirees = {x["numero"] for x in liste["retraits"]["idees_de_la_table"]}
    jetons = sorted({f for x in liste["retraits"]["reserves_de_cloisonnement"] for f in x["fiches"]})
    servies = [s["numero"] for f in liste["fils"] for s in f["idees_servies"]]
    croisement = sorted(set(servies) & retirees)
    if croisement:
        raise Refus(f"entrée servie figurant dans la liste des retraits : {croisement}")
    textes = "\n".join(s["texte_servi"] for f in liste["fils"] for s in f["idees_servies"])
    for j in jetons:
        if j in textes:
            raise Refus(f"jeton d'une entrée réservée dans un texte servi : {j}")
    if len(liste["fils"]) != 16:
        raise Refus(f"liste des fils : {len(liste['fils'])} fils, 16 attendus")
    return {"fils": len(liste["fils"]), "idees_servies_distinctes": len(set(servies)), "idees_retirees": sorted(retirees),
            "jetons_reserves": jetons}


def texte_de_case(fil: dict) -> str:
    lignes = [f"Fil commun n° {fil['rang']} : {fil['titre']}",
              "Idées regroupées sous ce fil (avis de proposeurs d'une course passée, jamais des faits ni des preuves) :"]
    lignes += [f"- [{s['numero']}] {s['texte_servi']}" for s in fil["idees_servies"]]
    return "\n".join(lignes)


# --- (4) déclaration des relais -----------------------------------------------------------------------------------------------


def lire_json_scelle(chemin: Path, quoi: str) -> tuple:
    if not chemin.is_file():
        raise Refus(f"{quoi} absent : {chemin}")
    if not scelle(chemin):
        raise Refus(f"{quoi} non scellé (compagnon .sha256 absent ou faux) : {chemin}")
    brut = chemin.read_text(encoding="utf-8")
    if MOTIF_VALEUR_DE_CLE.search(brut):
        raise Refus(f"{quoi} : une chaîne de la forme d'une valeur de clé y figure — refus, rien n'est lu ni recopié")
    try:
        return json.loads(brut), sha256_fichier(chemin)
    except ValueError:
        raise Refus(f"{quoi} : JSON illisible") from None


def verifier_declaration(decl: dict, fixe: dict, r: Reglages) -> dict:
    """Rend {fournisseurs (blocs de l'orchestrateur), especes_actives, cles {fournisseur: nom}, absentes, carbon}."""
    f_decl = decl.get("fournisseurs")
    if not isinstance(f_decl, dict):
        raise Refus("déclaration des relais : « fournisseurs » (objet) exigé")
    inconnus = sorted(set(f_decl) - set(TYPES_PERMIS))
    if inconnus:
        raise Refus(f"déclaration des relais : fournisseurs inconnus {inconnus}")
    for requis in ("claude", "argon"):
        if requis not in f_decl:
            raise Refus(f"déclaration des relais : « {requis} » exigé (proposeurs Claude d'abord ; juge et lecteur Argon)")
    metas: dict = {}
    blocs, cles, modeles, carbon = {}, {}, {}, {"inscrite": INSCRIPTION_CARBON, "active": False, "motif": None}
    for nom, b in sorted(f_decl.items()):
        if not isinstance(b, dict):
            raise Refus(f"fournisseurs.{nom} : objet attendu")
        t = TYPES_PERMIS[nom]
        if b.get("type") != t:
            raise Refus(f"fournisseurs.{nom}.type : {t!r} exigé (reçu {b.get('type')!r})")
        en_trop = sorted(set(b) - CLES_PERMISES[t] - CLES_META)
        if en_trop:
            raise Refus(f"fournisseurs.{nom} : clés non permises {en_trop}")
        nom_cle = b.get("nom_cle")
        if not isinstance(nom_cle, str) or not NOM_DE_VARIABLE.match(nom_cle):
            raise Refus(f"fournisseurs.{nom}.nom_cle : nom de variable exigé (le nom seul, jamais la valeur)")
        if nom_cle in CLES_INTERDITES:
            raise Refus(f"fournisseurs.{nom}.nom_cle = {nom_cle} : clé exclue de cette course (Rigaud garde son reste ; Minuit "
                        f"est sans crédit, R-4833)")
        if nom == "claude" and nom_cle != CLE_CLAUDE:
            raise Refus(f"fournisseurs.claude.nom_cle = {nom_cle} : tous les appels Claude passent par {CLE_CLAUDE} ({GO_EXCEPTION_CLE})")
        if nom == "astra" and nom_cle != CLE_ASTRA:
            raise Refus(f"fournisseurs.astra.nom_cle = {nom_cle} : Astra passe par {CLE_ASTRA} (GO-2026-11-22-111)")
        if nom != "claude" and nom_cle.startswith(PREFIXE_CLES_CLAUDE):
            raise Refus(f"fournisseurs.{nom}.nom_cle = {nom_cle} : une clé de la famille Claude sur un autre relais est refusée")
        pp = b.get("porte_plafond")
        if not isinstance(pp, dict) or pp.get("type") not in ("commande", "environnement"):
            raise Refus(f"fournisseurs.{nom}.porte_plafond : {{type: commande|environnement}} exigé (A15, brouillon 10)")
        if t == "commande_externe" and pp["type"] != "environnement":
            raise Refus(f"fournisseurs.{nom}.porte_plafond : « environnement » exigé pour une commande externe")
        if t != "commande_externe":
            if pp["type"] != "commande" or not isinstance(pp.get("commande"), list) or not pp["commande"] \
                    or not all(isinstance(x, str) and x for x in pp["commande"]):
                raise Refus(f"fournisseurs.{nom}.porte_plafond : commande (liste non vide) exigée pour un relais persistant")
            if not isinstance(pp.get("delai_s"), (int, float)) or isinstance(pp.get("delai_s"), bool) or pp["delai_s"] <= 0:
                raise Refus(f"fournisseurs.{nom}.porte_plafond.delai_s : nombre > 0 exigé")
            if not isinstance(b.get("url_relais"), str) or not URL_LOCALE.match(b["url_relais"]):
                raise Refus(f"fournisseurs.{nom}.url_relais : adresse de boucle locale exigée (http://127.0.0.1:PORT)")
        if nom == "argon":  # v11 : la commande en flux épinglée, aux arguments épinglés (garde Google) ; l'enveloppe v5 est refusée
            c = b.get("commande") if isinstance(b.get("commande"), list) else []
            ep = COMMANDES_EPINGLEES["argon"]
            if len(c) < 4 or not os.path.isabs(c[0]) or c[1:3] != ["-I", "-B"] or os.path.basename(c[3]) not in ep \
                    or not os.path.isfile(c[3]) or sha256_fichier(Path(c[3])) != ep[os.path.basename(c[3])]:
                raise Refus(f"fournisseurs.argon.commande : « python -I -B <commande en flux épinglée> » exigé ({sorted(ep)}) ; "
                            "l'enveloppe v5 (commande_argon_v3d, hors garde Google) est refusée")
            if c[4:] != ARGUMENTS_COMMANDES["argon"]:
                raise Refus(f"fournisseurs.argon.commande : arguments différents des arguments épinglés {ARGUMENTS_COMMANDES['argon']}")
        if nom in ("astra", "carbon"):
            m = b.get("modele_propose")
            motif = next(e.get("motif_modele") for e in fixe["especes"] if e["fournisseur"] == nom)
            if not isinstance(m, str) or motif not in m.lower() or "claude" in m.lower() or not re.fullmatch(r"[a-z0-9.\-]+", m):
                raise Refus(f"fournisseurs.{nom}.modele_propose : identifiant de modèle qui contient « {motif} » exigé")
            if not isinstance(b.get("commande"), list) or not b["commande"]:
                raise Refus(f"fournisseurs.{nom}.commande : liste non vide exigée")
            c = b["commande"]
            epingles = COMMANDES_EPINGLEES.get(nom) or {}
            if len(c) < 4 or not os.path.isabs(c[0]) or c[1:3] != ["-I", "-B"] or os.path.basename(c[3]) not in epingles \
                    or not os.path.isfile(c[3]) or sha256_fichier(Path(c[3])) != epingles[os.path.basename(c[3])]:
                raise Refus(f"fournisseurs.{nom}.commande : « python -I -B <commande épinglée> » exigé, à l'empreinte épinglée "
                            f"({sorted(epingles)})")
            if nom == "carbon":  # v8 : options exigées lues d'abord (motif précis), puis l'égalité aux arguments épinglés
                controler_delai_carbon(lire_reglages_carbon(c[4:]), fixe)
                if _valeur_arg(c[4:], "--niveau-reflexion") != NIVEAU_REFLEXION_CARBON:  # v11 : réflexion explicite, la plus haute
                    raise Refus(f"fournisseurs.carbon.commande : --niveau-reflexion {_valeur_arg(c[4:], '--niveau-reflexion')!r}, "
                                f"{NIVEAU_REFLEXION_CARBON!r} exigé (règle des appels à Google)")
            if c[4:] != ARGUMENTS_COMMANDES[nom]:
                raise Refus(f"fournisseurs.{nom}.commande : arguments différents des arguments épinglés {ARGUMENTS_COMMANDES[nom]}")
            if m != MODELES_RELAIS[nom][0]:
                raise Refus(f"fournisseurs.{nom}.modele_propose : {MODELES_RELAIS[nom][0]} exigé")
            modeles[nom] = m
        if nom == "kimi" and b.get("modele") != "kimi-k3.1-pro":
            raise Refus("fournisseurs.kimi.modele : « kimi-k3.1-pro » exigé (configuration fixe)")
        if nom == "kimi":
            controler_kimi(b)
            mot = decl.get("kimi_autorise_par_la_mere")
            if not (isinstance(mot, dict) and isinstance(mot.get("reference"), str) and re.fullmatch(r"R-\d{3,5}", mot["reference"])):
                raise Refus("fournisseurs.kimi : Kimi n'est pas déclaré par défaut (A14 : 6 appels inexploitables sur 16 rendent "
                            "l'étape « non mesurée (technique) ») ; il faut le mot écrit de la mère dans la déclaration : "
                            "\"kimi_autorise_par_la_mere\": {\"reference\": \"R-NNNN\"}")
            if mot["reference"] not in tuple(r.references_kimi_admises):  # v7, mineur 9 : la forme ne suffit plus
                raise Refus(f"fournisseurs.kimi : référence {mot['reference']} non admise par ce lanceur (admises : "
                            f"{list(r.references_kimi_admises) or 'aucune'} ; R-3279 : Kimi non déclaré) ; une autorisation de "
                            "la mère s'inscrit dans une version suivante du lanceur")
        if nom == "carbon":
            if b.get("inscription") != INSCRIPTION_CARBON:
                carbon["motif"] = f"inscription {b.get('inscription')!r} : {INSCRIPTION_CARBON} exigée ; Carbon non active"
                continue
            carbon.update(active=True, motif="inscrite (R-3217), relais et clé nommés dans la déclaration")
        elif "inscription" in b:
            raise Refus(f"fournisseurs.{nom}.inscription : clé réservée à Carbon")
        blocs[nom] = {k: v for k, v in b.items() if k not in CLES_META}
        metas[nom] = {k: v for k, v in b.items() if k in CLES_META}
        cles[nom] = nom_cle
    if "carbon" not in f_decl:
        carbon["motif"] = "relais et clé non nommés dans la déclaration : course sans Carbon"
    actives, absentes = [], []
    for e in sorted(fixe["especes"], key=lambda x: x["ordre"]):
        if e["fournisseur"] in blocs:
            actives.append(dict(e, modele=e["modele"] or modeles[e["fournisseur"]]))
        else:
            absentes.append({"etiquette": e["etiquette"], "motif": "relais non déclaré" if e["fournisseur"] != "carbon" else carbon["motif"]})
    return {"fournisseurs": blocs, "especes_actives": actives, "especes_absentes": absentes, "cles": cles, "carbon": carbon, "metas": metas,
            "absences": decl.get("absences") if isinstance(decl.get("absences"), dict) else None,
            "kimi_autorise_par_la_mere": decl.get("kimi_autorise_par_la_mere"),
            "compter_limite_de_debit_comme_soupcon": verifier_choix_limite(decl)}


# --- (2) relevé du crédit de chaque clé ---------------------------------------------------------------------------------------


def _reel_positif(v) -> bool:
    return isinstance(v, (int, float)) and not isinstance(v, bool) and v >= 0


def verifier_choix_limite(decl: dict) -> bool:
    """5 : choix de la mère sur la limite de débit dans la garde de crédit ; vrai par défaut (lettre de la v5)."""
    v = decl.get("compter_limite_de_debit_comme_soupcon", True)
    if not isinstance(v, bool):
        raise Refus("compter_limite_de_debit_comme_soupcon : booléen exigé (vrai par défaut)")
    return v


def controler_kimi(bloc: dict) -> None:
    """Constat 3 : les contrôles de l'adaptateur `adaptateur_kimi_v53` (l. 62-69), repris avant le départ."""
    for k in ("prix_entree", "prix_sortie", "delai_s"):
        v = bloc.get(k)
        if not (isinstance(v, (int, float)) and not isinstance(v, bool) and v > 0):
            raise Refus(f"fournisseurs.kimi.{k} : réel > 0 exigé, comme l'adaptateur de Kimi")
    for k in ("max_sortie_jetons", "sortie_min_jetons"):
        v = bloc.get(k)
        if not (isinstance(v, int) and not isinstance(v, bool) and v >= 1):
            raise Refus(f"fournisseurs.kimi.{k} : entier ≥ 1 exigé, comme l'adaptateur de Kimi")
    if bloc["sortie_min_jetons"] > bloc["max_sortie_jetons"]:
        raise Refus("fournisseurs.kimi : sortie_min_jetons > max_sortie_jetons")


def borne_appel_kimi(bloc: dict, octets_entree_max: int, plafond_session: float) -> float:
    """Pire coût d'un appel de Kimi (formule de l'adaptateur `adaptateur_kimi_v53`) : (octets du corps + 1024) × prix d'entrée
    + max_tokens × prix de sortie, borné par le plafond de session ; prix en USD par million de jetons."""
    for k in ("prix_entree", "prix_sortie", "max_sortie_jetons"):
        if not _reel_positif(bloc.get(k)):
            raise Refus(f"fournisseurs.kimi.{k} : nombre ≥ 0 exigé pour la part au pire")
    brut = ((octets_entree_max + 1024) * bloc["prix_entree"] + bloc["max_sortie_jetons"] * bloc["prix_sortie"]) / 1e6
    return round(min(brut, plafond_session), 6)


# --- v8 : réglages de la commande de Carbon (pensée, sortie, délai) -------------------------------------------------------------


def lire_reglages_carbon(args: list) -> dict:
    """v8 : options de la commande de Carbon lues sur ses arguments déclarés. Chaque option exigée figure **une fois** (argparse
    garderait la dernière), avec une valeur réelle finie strictement positive ; une option absente est un refus : le défaut de
    la commande reprendrait la provision de 8 192 jetons et le délai de 1 500 s qui ont fait échouer la course d'auto-conception
    v4 (codes 7 et 6 ; diagnostic 510312b1…)."""
    manquantes = [o for o in OPTIONS_CARBON_EXIGEES if o not in args]
    if manquantes:
        raise Refus(f"fournisseurs.carbon.commande : options {manquantes} absentes (provision de pensée, sortie, délais exigés "
                    "explicitement)")
    doubles = [o for o in OPTIONS_CARBON_EXIGEES if args.count(o) != 1]
    if doubles:
        raise Refus(f"fournisseurs.carbon.commande : options {doubles} données plusieurs fois (une seule exigée)")
    lues = {}
    for o in OPTIONS_CARBON_EXIGEES:
        v = _valeur_arg(args, o)
        try:
            x = float(v)
        except (TypeError, ValueError):
            raise Refus(f"fournisseurs.carbon.commande : {o} illisible ({v!r})") from None
        if not (_nombre(x) and x > 0):
            raise Refus(f"fournisseurs.carbon.commande : {o} = {v!r} (réel fini strictement positif exigé)")
        lues[o] = x
    return lues


def controler_delai_carbon(lues: dict, fixe: dict) -> dict:
    """v8 : la commande dure au plus délai + intervalle + 2 × délai de requête (docstring de la commande) ; avec la marge de
    30 s, cette durée doit tenir sous le délai de l'adaptateur de commande de l'orchestrateur épinglé (1 800 s, non réglable :
    au-delà, il tue le groupe de processus, le lot n'est pas annulé et le plafond de session est compté) et sous le délai A3
    de la configuration pour Carbon (au-delà, l'appel est compté coupé, jamais lu). Le délai de lot doit être au moins celui
    de la v8 (1 620 s ; 1 500 en v7) ; la provision de pensée au moins 1,25 × la plus forte pensée observée."""
    a3 = (fixe.get("arrets") or {}).get("a3_delai_s") or {}
    try:
        delai_a3 = float(a3.get("carbon", a3["*"]))
    except (KeyError, TypeError, ValueError):
        raise Refus("configuration : arrets.a3_delai_s (« * » ou « carbon ») illisible : délai de Carbon non contrôlable") from None
    borne = min(DELAI_ADAPTATEUR_ORCHESTRATEUR_S, delai_a3)
    duree_max = lues["--delai-s"] + lues["--delai-requete-s"]  # v11 (flux) : compte de jetons, puis une génération
    if duree_max + MARGE_DELAI_CARBON_S > borne:
        raise Refus(f"fournisseurs.carbon.commande : durée maximale {duree_max:g} s + marge {MARGE_DELAI_CARBON_S:g} s > {borne:g} s "
                    "(délai de l'adaptateur de l'orchestrateur épinglé, 1 800 s non réglable, et A3) : l'orchestrateur tuerait la "
                    "commande avant l'annulation du lot")
    if lues["--delai-s"] < DELAI_CARBON_S:
        raise Refus(f"fournisseurs.carbon.commande : --delai-s {lues['--delai-s']:g} < {DELAI_CARBON_S} (v11 : délai de la "
                    "génération en flux)")
    minimum = math.ceil(MARGE_PENSEE * PENSEE_OBSERVEE_MAX_JETONS)
    if lues["--provision-pensee-jetons"] < minimum:
        raise Refus(f"fournisseurs.carbon.commande : --provision-pensee-jetons {lues['--provision-pensee-jetons']:g} < {minimum} "
                    f"(1,25 × {PENSEE_OBSERVEE_MAX_JETONS}, plus forte pensée observée : la garde après coup de la commande, code 7, "
                    "refuserait la réponse)")
    return {"duree_max_s": duree_max, "marge_s": MARGE_DELAI_CARBON_S, "borne_s": borne, "delai_a3_s": delai_a3,
            "delai_adaptateur_s": DELAI_ADAPTATEUR_ORCHESTRATEUR_S, "provision_minimale_jetons": minimum}


def consigne_servie_proposeur(consigne: str, case: str, bras: str = "affinage") -> str:
    """La consigne qu'un proposeur reçoit en passe 1, sans héritage (une seule génération) : `pole/course2_v53.py`, `_proposer`,
    l. 228-229 de l'orchestrateur épinglé."""
    return consigne.rstrip() + f"\n\n## Case\nTexte : {case} ; bras : {bras}\n"


def controler_pire_cas_carbon(decl: dict, fixe: dict, liste: dict, pieces: dict) -> dict | None:
    """v11 (flux, `commande_gemini_flux_v1.py`) : la commande ne baisse jamais sa sortie ; elle refuse (code 4) si l'entrée
    gardée × prix d'entrée + sortie maximale × prix de sortie dépasse le plafond de session. Sur l'entrée **la plus longue** de
    la course (consigne servie et fil expurgé, caractères / 3 × 1,05) et l'entrée la plus courte : pire cas d'un appel ≤ plafond
    de session (sinon Carbon serait absente de fait) ; texte = sortie − provision ≥ 16 000 (règle gelée) et > cartes × 9 000
    caractères (limite de l'invite, un jeton au plus par caractère) ; sortie ≥ pensée et réponse observées (24 500). Rend None si
    Carbon n'est pas active."""
    if "carbon" not in decl["fournisseurs"]:
        return None
    c = decl["fournisseurs"]["carbon"]["commande"]
    lues = lire_reglages_carbon(c[4:])
    delai = controler_delai_carbon(lues, fixe)
    plafond = float(fixe["plafonds_session"]["proposeur"])
    consigne = Path(pieces["consigne_proposeur"]["absolu"]).read_text(encoding="utf-8")
    caracteres = [len(consigne_servie_proposeur(consigne, expurger(texte_de_case(f))[0])) for f in liste["fils"]]
    pe, ps = lues["--prix-entree"] / 1e6, lues["--prix-sortie"] / 1e6
    p, smax = lues["--provision-pensee-jetons"], lues["--max-sortie-jetons"]
    texte = smax - p
    limite_invite = int(fixe.get("cartes_par_appel") or 1) * CARACTERES_PAR_CARTE_MAX
    if texte < TEXTE_MIN_GOOGLE or texte <= limite_invite:
        raise Refus(f"fournisseurs.carbon.commande : texte {texte:g} jetons (sortie {smax:g} − provision {p:g}) : au moins "
                    f"{TEXTE_MIN_GOOGLE} et plus que la limite de l'invite ({limite_invite} caractères) exigés (règle des appels à Google)")
    if smax < SORTIE_RETENUE_MIN_CARBON:
        raise Refus(f"fournisseurs.carbon.commande : sortie {smax:g} < {SORTIE_RETENUE_MIN_CARBON} (pensée et réponse observées)")
    sortie = {}
    for nom_cas, n in (("entree_la_plus_longue", max(caracteres)), ("entree_la_plus_courte", min(caracteres))):
        e = math.ceil(n / CARACTERES_PAR_JETON_CARBON * (1 + MARGE_ENTREE_CARBON))
        pire = e * pe + smax * ps
        if pire > plafond + 1e-12:
            raise Refus(f"fournisseurs.carbon.commande : pire cas d'un appel {pire:.6f} USD (entrée gardée {e}, sortie {smax:g}) > "
                        f"plafond de session {plafond} USD : la commande refuserait chaque appel (code 4, rien envoyé)")
        sortie[nom_cas] = {"caracteres": n, "entree_gardee_jetons": e, "sortie_demandee_jetons": int(smax),
                           "pire_cas_appel_usd": round(pire, 6), "marge_sous_le_plafond_usd": round(plafond - pire, 6)}
    return {"reglages": {k: lues[k] for k in OPTIONS_CARBON_EXIGEES}, "niveau_reflexion": NIVEAU_REFLEXION_CARBON,
            "texte_jetons": texte, "limite_invite_caracteres": limite_invite, "plafond_session_usd": plafond, "delai": delai,
            "cas": sortie, "part_au_pire_usd": round(len(liste["fils"]) * plafond, 6),
            "note": "flux, prix plein, aucune remise ; la sortie maximale compte la pensée ; une sortie coupée (MAX_TOKENS) ou "
                    "sans pensée est un défaut de la commande (garde Google après réponse), jamais une réponse"}


def entree_juge_la_plus_longue(consigne_juge: str) -> str:
    """v11c (constat 11) : entrée d'un juge de la forme que bâtit l'orchestrateur épinglé (`pole/fiches_v54.py`,
    `entree_une_fiche`, l. 59 : consigne figée, « ## La fiche », fiche JSON indentée), pour la carte la plus longue que la consigne
    du proposeur permet (9 000 caractères) et 1 000 caractères de cadre de fiche (SUPPOSÉ : identifiant servi, champs) ;
    caractères non ASCII, comme le texte des cartes."""
    fiche = {"identifiant": "F" + "x" * 5, "carte": "é" * CARACTERES_PAR_CARTE_MAX, "cadre": "é" * 1000}
    corps = json.dumps(fiche, ensure_ascii=False, indent=1)
    return consigne_juge.rstrip() + "\n\n## La fiche\n```json\n" + corps + "\n```\n"


def controler_pire_cas_argon(decl: dict, fixe: dict, liste: dict, pieces: dict) -> dict | None:
    """v11 : Argon sous la garde Google (commande en flux, sortie jamais abaissée) : pour chaque rôle (proposeur, juge), pire cas
    d'un appel = entrée gardée (caractères / 3 × 1,05) × prix d'entrée + sortie × prix de sortie ≤ plafond de session du rôle ;
    sinon refus, avec le plafond minimal qui le paierait (à fixer par le devis v11 dans `argon_v11.plafond_session_juge_usd`).
    Entrée d'un juge : consigne du juge + une carte de 9 000 caractères au plus + 1 000 caractères de marge (SUPPOSÉ)."""
    b = decl["fournisseurs"].get("argon")
    if b is None or (b.get("commande") or [None])[0] == "bash":
        return None
    a = b["commande"][4:]
    pe, ps = float(_valeur_arg(a, "--prix-entree")) / 1e6, float(_valeur_arg(a, "--prix-sortie")) / 1e6
    p, smax = float(_valeur_arg(a, "--provision-pensee-jetons")), float(_valeur_arg(a, "--max-sortie-jetons"))
    texte = smax - p
    limite_invite = int(fixe.get("cartes_par_appel") or 1) * CARACTERES_PAR_CARTE_MAX
    if texte < TEXTE_MIN_GOOGLE or texte <= limite_invite:
        raise Refus(f"fournisseurs.argon.commande : texte {texte:g} jetons : au moins {TEXTE_MIN_GOOGLE} et plus que {limite_invite} exigés")
    consigne_p = Path(pieces["consigne_proposeur"]["absolu"]).read_text(encoding="utf-8")
    consigne_j = Path(pieces["consigne_juge"]["absolu"]).read_text(encoding="utf-8")
    caracteres = {"proposeur": max(len(consigne_servie_proposeur(consigne_p, expurger(texte_de_case(f))[0])) for f in liste["fils"]),
                  "juge": len(entree_juge_la_plus_longue(consigne_j))}  # v11c : forme de l'orchestrateur
    out = {}
    for role, n in caracteres.items():
        e = math.ceil(n / CARACTERES_PAR_JETON_CARBON * (1 + MARGE_ENTREE_CARBON))
        pire = e * pe + smax * ps
        plafond = float(fixe["plafonds_session"][role])
        minimal = math.ceil(pire * 100) / 100
        if pire > plafond + 1e-12:
            raise Refus(f"fournisseurs.argon.commande : pire cas d'un appel de {role} {pire:.6f} USD > plafond de session {plafond} "
                        f"USD : la commande refuserait chaque appel (code 4) ; plafond minimal {minimal} USD "
                        "(argon_v11.plafond_session_juge_usd pour les juges, fixé par le devis v11)")
        out[role] = {"caracteres": n, "entree_gardee_jetons": e, "sortie_jetons": int(smax), "pire_cas_appel_usd": round(pire, 6),
                     "plafond_session_usd": plafond, "plafond_minimal_usd": minimal}
    return {"roles": out, "texte_jetons": texte, "provision_jetons": p, "note": "provision d'Argon SUPPOSÉE (devis v11)"}


def parts_au_pire(fixe: dict, liste: dict, pieces: dict, decl: dict) -> dict:
    """Part au pire de chaque relais (donc de chaque clé) dans cette course, en USD (R-3237, point 1) :
    - relais qui tient l'aiguilleur ou un juge (Claude, Argon) : le nombre de cartes n'est borné par aucun programme, la seule
      borne dure est le plafond d'arrêt : 150 USD ;
    - relais de proposeur seulement : 16 appels × pire coût d'un appel (plafond de session ; pour Kimi, la formule de son
      adaptateur sur l'entrée la plus longue de la course, si elle est plus basse)."""
    actives = decl["especes_actives"]
    ps = fixe["plafonds_session"]
    internes = {fixe["aiguilleur"]["fournisseur"]} | {j["fournisseur"] for j in fixe["juges"]}
    consigne = Path(pieces["consigne_proposeur"]["absolu"]).read_bytes()
    entree_max = len(consigne) + max(len(texte_de_case(f).encode("utf-8")) for f in liste["fils"]) + 200
    parts = {}
    for f in sorted({e["fournisseur"] for e in actives} | internes):
        if f in internes:
            parts[f] = {"part_au_pire_usd": PLAFOND_ARRET_USD, "regle": "aiguilleur ou juge : cartes non bornées, plafond d'arrêt"}
            continue
        n = len(liste["fils"]) * sum(1 for e in actives if e["fournisseur"] == f)
        par_appel = float(ps["proposeur"])
        regle = f"{n} appels × plafond de session {par_appel}"
        if f == "kimi":
            par_appel = borne_appel_kimi(decl["fournisseurs"]["kimi"], entree_max, float(ps["proposeur"]))
            regle = f"{n} appels × pire coût d'un appel de Kimi (formule de son adaptateur, entrée ≤ {entree_max} octets)"
        parts[f] = {"part_au_pire_usd": round(min(n * par_appel, PLAFOND_ARRET_USD), 6), "par_appel_usd": par_appel, "regle": regle}
    return parts


REFERENCE_LUC_SANS_SOLDE = "GO-2026-11-22-124"
CHAMPS_LUC_PERMIS = ("solde_non_lu", "reference", "source", "note")
MOTS_DE_MONTANT = ("solde", "credit", "reste", "couverture", "reserve", "recharge", "plancher", "usd", "eur", "montant")


def verifier_ligne_luc(x) -> dict:
    """v11c (constat 3 ; brouillon 3, « Règle des clés », point 1) : l'entrée de la clé LUC au relevé des crédits est exigée ;
    elle porte `solde_non_lu` = vrai et `reference` = GO-2026-11-22-124 ; elle ne porte aucun montant (aucun champ de solde, de
    crédit, de reste, de couverture, de réserve, de recharge ni de plancher) ; champs permis : `solde_non_lu`, `reference`,
    `source`, `note`. Toute autre forme : refus (aucun repli)."""
    if not isinstance(x, dict):
        raise Refus(f"relevé des crédits : entrée de la clé {CLE_CLAUDE} absente — « solde non lu » avec "
                    f"{REFERENCE_LUC_SANS_SOLDE} s'écrit, il ne s'omet pas")
    if x.get("solde_non_lu") is not True or x.get("reference") != REFERENCE_LUC_SANS_SOLDE:
        raise Refus(f"relevé des crédits : clé {CLE_CLAUDE} : « solde_non_lu » vrai et « reference » = {REFERENCE_LUC_SANS_SOLDE} "
                    f"exigés (lus : {x.get('solde_non_lu')!r}, {x.get('reference')!r})")
    montants = sorted(k for k in x if k != "solde_non_lu" and any(m in _normaliser(k) for m in MOTS_DE_MONTANT))
    autres = sorted(k for k in x if k not in CHAMPS_LUC_PERMIS)
    if montants or autres:
        raise Refus(f"relevé des crédits : clé {CLE_CLAUDE} : champ(s) {sorted(set(montants) | set(autres))} refusé(s) : la ligne ne "
                    "porte ni solde, ni crédit, ni reste, ni couverture, ni réserve (GO-2026-11-22-124)")
    return x


def verifier_credits(releve: dict, cles: dict, aujourd_hui: _dt.date, dossier_alerte: Path, parts: dict | None = None) -> dict:
    """v3 (R-3237). Rend {nom_cle: {...}}.
    - Relevé du jour exigé ; chaque clé employée y figure (« non lisible » s'écrit).
    - v11 (GO-2026-11-22-124) : clé Claude (LUC) : aucune condition (solde non lu, recharge automatique) ; la ligne du relevé,
      si elle est écrite, est recopiée pour information ; la part Claude est tenue par le plafond propre et l'arrêt au premier
      refus de l'interface (`SurveillanceCleClaude`).
    - Non lisible : Argon, Astra, Carbon seulement sous la dispense écrite de la mère
      citant R-3237 (départ permis, arrêt au premier refus pour crédit) ; toute autre clé : refus.
    - Lisible : alerte et arrêt avant le départ (code 3) si reste < sa part au pire, ou reste < un cinquième du crédit ;
      Kimi : part au pire + 11,3 USD > 90 % du reste → refus (les deux courses se suivent)."""
    parts = parts or {}
    quand = str(releve.get("releve_utc") or "")
    if not quand.startswith(aujourd_hui.isoformat()):
        raise Refus(f"relevé des crédits du {quand!r} : un relevé du jour ({aujourd_hui}) est exigé")
    instant_du_releve(releve)  # v7 : heure lisible exigée (comparée à la fin d'une autre course de l'organisme)
    lignes = releve.get("cles")
    if not isinstance(lignes, dict):
        raise Refus("relevé des crédits : « cles » (objet) exigé")
    dispense = releve.get("dispense") or {}
    dispensees = set(dispense.get("cles") or []) if dispense.get("par") == "mère" and dispense.get("reference") == REFERENCE_DISPENSE else set()
    sortie, alertes = {}, []
    groupes: dict = {}
    for f, n in sorted(cles.items()):
        groupes.setdefault(n, []).append(f)
    for nom, fours in sorted(groupes.items()):
        fournisseur = "+".join(fours)  # 7 : une clé partagée (Argon et Carbon) porte la somme des parts au pire
        x = lignes.get(nom)
        parts_k = [(parts.get(f) or {}).get("part_au_pire_usd") for f in fours]
        part = None if any(q is None for q in parts_k) else round(sum(parts_k), 6)
        if nom == CLE_CLAUDE:  # v11 (GO-2026-11-22-124) : solde non lu, aucune condition de départ sur la clé Claude
            verifier_ligne_luc(x)  # v11c, constat 3 : l'entrée « solde non lu, GO-2026-11-22-124 » est exigée, sans montant
            sortie[nom] = {"fournisseur": fournisseur, "relais": fours, "parts_par_relais": dict(zip(fours, parts_k)),
                           "lisible": False, "condition_de_depart": None, "ligne_du_releve": x if isinstance(x, dict) else None,
                           "part_au_pire_usd": part, "plafond_part_claude_usd": PLAFOND_PART_CLAUDE_USD,
                           "regle": "GO-2026-11-22-124 : solde non lu (recharge automatique) ; plafond propre de la part Claude "
                                    f"{PLAFOND_PART_CLAUDE_USD} USD (relais Claude lancé à ce plafond) ; arrêt propre au premier "
                                    "refus de l'interface ou du relais (code 5)"}
            continue
        if not isinstance(x, dict):
            raise Refus(f"relevé des crédits : clé {nom} ({fournisseur}) absente — « non lisible » s'écrit, il ne s'omet pas")
        if x.get("non_lisible") is True:
            if any(f not in FOURNISSEURS_DISPENSABLES for f in fours):
                raise Refus(f"crédit de la clé {nom} ({fournisseur}) non lisible : seules les clés d'Argon, d'Astra et de Carbon "
                            "peuvent partir sous dispense (R-3237)")
            if nom not in dispensees:
                raise Refus(f"crédit de la clé {nom} ({fournisseur}) non lisible et sans dispense écrite de la mère citant "
                            f"{REFERENCE_DISPENSE} : aucun départ")
            sortie[nom] = {"fournisseur": fournisseur, "relais": fours, "parts_par_relais": dict(zip(fours, parts_k)),
                           "lisible": False, "motif": x.get("motif"), "dispense": dispense, "part_au_pire_usd": part, "regle": "arrêt de la course au premier refus pour crédit (R-3237)"}
            continue
        credit, reste = x.get("credit_usd"), x.get("reste_usd")
        if not (_reel_positif(credit) and _reel_positif(reste)) or reste > credit:
            raise Refus(f"relevé des crédits : clé {nom} : credit_usd et reste_usd (nombres ≥ 0, reste ≤ crédit) exigés")
        if part is None:
            raise Refus(f"part au pire du relais {fournisseur} inconnue : aucun départ")
        d = {"fournisseur": fournisseur, "relais": fours, "parts_par_relais": dict(zip(fours, parts_k)), "lisible": True,
             "credit_usd": credit, "reste_usd": reste, "source": x.get("source"), "part_au_pire_usd": part, "cinquieme_usd": credit / 5.0}
        motifs = []
        if reste <= part:
            motifs.append(f"reste {reste} ≤ part au pire {part} (à l'égalité, le pire cas laisse zéro)")
        if reste < credit / 5.0:
            motifs.append(f"reste {reste} < un cinquième du crédit {credit / 5.0}")
        if "kimi" in fours and part + KIMI_COURSE_SUIVANTE_PIRE_USD > KIMI_PART_DU_RESTE * reste:
            motifs.append(f"part au pire {part} + {KIMI_COURSE_SUIVANTE_PIRE_USD} (course Kimi de la relance) > 90 % du reste "
                          f"({round(KIMI_PART_DU_RESTE * reste, 6)}) : les deux courses doivent se suivre, solde relu avant chacune")
        d["motifs_d_arret"] = motifs
        sortie[nom] = d
        if motifs:
            alertes.append({"cle": nom, "fournisseur": fournisseur, "reste_usd": reste, "credit_usd": credit, "part_au_pire_usd": part,
                            "motifs": motifs})
    if alertes:
        texte = {"alerte": "crédit insuffisant pour la part au pire d'une clé, avant la course d'affinage des idées des mentors : "
                           "départ refusé",
                 "regle": "R-3237 : chaque clé confrontée à sa part au pire ; un cinquième du crédit ; Kimi : part + 11,3 USD ≤ 90 % "
                          "du reste, sinon les deux courses se suivent et le solde est relu avant chacune ; Lazar à prévenir "
                          "avant qu'une clé n'atteigne zéro",
                 "cles": alertes, "pour": "la mère (à transmettre à Lazar)"}
        dossier_alerte.mkdir(parents=True, exist_ok=True)
        chemin = dossier_alerte / "alerte-credits-avant.json"
        if not chemin.exists():
            ecrire_scelle(chemin, texte)
        raise AlerteCredit(json.dumps(dict(texte, fichier=str(chemin)), ensure_ascii=False))
    return sortie


def instant_du_releve(releve: dict) -> _dt.datetime:
    """v7 : heure du relevé (« AAAA-MM-JJTHH:MM:SSZ », celle de `date -u +%FT%TZ`), en UTC ; illisible : refus."""
    m = re.match(r"^(\d{4}-\d{2}-\d{2})T(\d{2}):(\d{2}):(\d{2})Z", str(releve.get("releve_utc") or ""))
    if not m:
        raise Refus(f"relevé des crédits : releve_utc {releve.get('releve_utc')!r} illisible (« AAAA-MM-JJTHH:MM:SSZ » exigé, "
                    "date -u +%FT%TZ)")
    try:
        return _dt.datetime.fromisoformat(f"{m.group(1)}T{m.group(2)}:{m.group(3)}:{m.group(4)}+00:00")
    except ValueError:
        raise Refus(f"relevé des crédits : releve_utc {releve.get('releve_utc')!r} illisible") from None


def verifier_autres_courses(r: "Reglages", releve: dict) -> dict:
    """v7, majeur 2 : la course d'auto-conception partage les ports 8787 à 8793, la clé Minuit (et celles de Google et
    d'OpenAI) et la sonde d'Astra. Refus si l'une de ses courses a un manifeste de départ sans manifeste de fin (en cours, ou
    interrompue sans fin écrite : à éclaircir avant tout départ), ou si le relevé des crédits n'est pas postérieur à la fin
    (date du manifeste de fin) de chacune de ses courses versées : il faut le refaire après elle, avec sa dépense réelle."""
    vues = []
    if not r.dossier_runs.is_dir():
        return {"autres_courses": vues}
    quand = instant_du_releve(releve)
    for p in sorted(r.dossier_runs.iterdir()):
        if not (p.is_dir() and MOTIF_AUTRE_COURSE.search(p.name) and (p / "manifeste-lanceur-depart.json").exists()):
            continue
        fin = p / "manifeste-lanceur-fin.json"
        if not fin.exists():
            raise Refus(f"course d'auto-conception {p.name} partie sans manifeste de fin : les deux courses ne tournent jamais en "
                        "même temps (ports 8787 à 8793, clés et sonde communs) ; attendre sa fin, arrêter ses relais par leur "
                        "PID, refaire le relevé des crédits")
        fini = _dt.datetime.fromtimestamp(fin.stat().st_mtime, _dt.timezone.utc)
        if quand <= fini:
            raise Refus(f"relevé des crédits du {quand.isoformat()} antérieur à la fin de la course d'auto-conception {p.name} "
                        f"({fini.isoformat()}) : relevé à refaire après elle, avec sa dépense réelle (clé Minuit comprise)")
        vues.append({"run": p.name, "fin_utc": fini.isoformat()})
    return {"autres_courses": vues, "releve_utc": quand.isoformat()}


# --- (R-3237, 3) procédure neutre des relais persistants ; (R-3237, 2) garde de crédit des relais dispensés ----------------


def modeles_du_fournisseur(fixe: dict, nom: str) -> list:
    if nom == "claude":
        return sorted(e["modele"] for e in fixe["especes"] if e["famille"] == "claude")
    return list(MODELES_RELAIS[nom])


def verifier_procedure_relais(r: "Reglages", decl: dict, pieces: dict, fixe: dict | None = None, parts: dict | None = None) -> dict:
    """Moteur réel : pièce de la procédure épinglée ; commande de chaque porte « commande » = « python -I -B porte » et ses
    arguments recoupés avec la déclaration et la configuration (v5, constat 2) ; **chaque** relais déclaré vivant contrôlé
    par son PID et par `/relais/etat` (v5, constat 4 ; B ; C)."""
    fixe = fixe or {"especes": []}
    o = json.loads(Path(pieces["procedure_relais"]["absolu"]).read_text(encoding="utf-8"))
    for cle_chemin, cle_sha, piece in (("chemin", "sha256", "lanceur_relais"), ("procedure_ecrite", "procedure_ecrite_sha256", "procedure_ecrite")):
        if o.get(cle_sha) != pieces[piece]["sha256"]:
            raise Refus(f"pièce de la procédure : {cle_chemin} d'une autre empreinte que la pièce épinglée {piece}")
    porte = pieces["porte_plafond"]["absolu"]
    relais = {}
    n_especes = len(decl["especes_actives"])
    for nom, b in sorted(decl["fournisseurs"].items()):
        pp = b.get("porte_plafond") or {}
        meta = decl.get("metas", {}).get(nom, {})
        if pp.get("type") == "commande":
            c = pp.get("commande") or []
            if len(c) < 4 or not os.path.isabs(c[0]) or c[1:3] != ["-I", "-B"] or c[3] != porte:
                raise Refus(f"fournisseurs.{nom}.porte_plafond : la commande doit commencer par « python -I -B {porte} » (constat 1)")
            reste = c[4:]
            try:
                plafond_ligne = float(_valeur_arg(reste, "--plafond-ligne"))
            except (TypeError, ValueError):
                plafond_ligne = None
            if _valeur_arg(reste, "--url") != b.get("url_relais"):
                raise Refus(f"fournisseurs.{nom}.porte_plafond : --url différent de l'adresse déclarée du relais (v5, constat 2)")
            mp = sorted(x for x in (_valeur_arg(reste, "--modeles-permis") or "").split(",") if x)
            if mp != modeles_du_fournisseur(fixe, nom):
                raise Refus(f"fournisseurs.{nom}.porte_plafond : --modeles-permis différents des modèles de la configuration (v5, constat 2)")
            if plafond_ligne != PLAFOND_ARRET_USD:
                raise Refus(f"fournisseurs.{nom}.porte_plafond : --plafond-ligne doit valoir {PLAFOND_ARRET_USD} (v5, constat 2)")
        relais[nom] = controler_relais_vivant(r, nom, dict(b, **meta), fixe, n_especes, parts)
    return {"procedure": o.get("procedure_ecrite"), "lanceur_relais": o.get("chemin"), "porte": porte, "relais_vivants": relais,
            "note": "la note de la pièce v3 (« chaque porte lance le lanceur de relais ») est périmée depuis la v4 : la porte "
                    "épinglée ouvre chaque commande de porte"}


def _cmdline(pid: int) -> list:
    with open(f"/proc/{int(pid)}/cmdline", "rb") as f:
        return [x.decode("utf-8", "replace") for x in f.read().split(b"\0") if x]


def _valeur_arg(args: list, nom: str):
    return args[args.index(nom) + 1] if nom in args and args.index(nom) + 1 < len(args) else None


def _valeurs_arg(args: list, nom: str) -> list:
    return [args[k + 1] for k, a in enumerate(args) if a == nom and k + 1 < len(args)]


def _etat_relais(url: str) -> dict:
    import urllib.request
    ouvreur = urllib.request.build_opener(urllib.request.ProxyHandler({}))
    with ouvreur.open(url.rstrip("/") + "/relais/etat", timeout=5) as rep:
        return json.loads(rep.read().decode("utf-8"))


def _port_du_fournisseur(nom: str, b: dict):
    if nom == "argon":
        return str(PORT_ARGON)
    if nom in ("astra", "carbon"):
        url = ARGUMENTS_COMMANDES[nom][ARGUMENTS_COMMANDES[nom].index("--url-relais" if nom == "astra" else "--url-base") + 1]
    else:
        url = b.get("url_relais") or ""
    m = re.search(r":(\d+)", url)
    return m.group(1) if m else None


def _entier_arg(args: list, option: str, nom: str) -> int:
    """v7 : borne lue sur la ligne de commande ; absente ou illisible : refus (aucun défaut du relais n'est supposé)."""
    v = _valeur_arg(args, option)
    if v is None:
        raise Refus(f"relais {nom} : {option} absent des arguments lus par PID (borne basse exigée, aucun défaut supposé)")
    try:
        return int(v)
    except ValueError:
        raise Refus(f"relais {nom} : {option} illisible ({v!r})") from None


def _nombre(v) -> bool:
    return isinstance(v, (int, float)) and not isinstance(v, bool) and v == v and v not in (float("inf"), float("-inf"))


def controler_relais_vivant(r: "Reglages", nom: str, b: dict, fixe: dict | None = None, n_especes: int = 6,
                            parts: dict | None = None) -> dict:
    """Arguments du relais lus par PID (jamais son environnement) et état lu sur `/relais/etat` : programme épinglé par la
    procédure, variable de la clé déclarée, port attendu, modèles permis égaux à ceux de la configuration ; v7 (majeur 1) :
    bornes basses de **tous** les relais — Claude : plafond 150 ; Astra, Kimi : `--max-appels` ≥ 20, plafond ≥ la part au pire
    (Astra : égal), réserve par appel ≤ plafond de session d'un proposeur, prix de l'état égaux à ceux de la commande ; Argon :
    `--max-appels` ≥ 2 × (16 + 32 × espèces) ; Carbon : `--max-lots` ≥ 20, `--max-appels` ≥ 40 ; bornes de l'état égales aux
    arguments ; variable de clé effacée (relais Gemini, Astra, Kimi) ; v7 (mineur 3) : état neuf **lu** — « appels » présent et
    nul ; « depense_usd » et « engage_usd » présents et nuls pour les relais à plafond en dollars ; « lots_crees » nul pour
    Carbon ; un état vide est refusé."""
    fixe = fixe or {"especes": []}
    pid = b.get("pid_relais")
    if not isinstance(pid, int) or isinstance(pid, bool) or pid <= 1:
        raise Refus(f"fournisseurs.{nom}.pid_relais : PID du relais vivant exigé (lancé par le lanceur de relais)")
    try:
        args = (r.lire_cmdline or _cmdline)(pid)
    except (OSError, KeyError):
        raise Refus(f"relais {nom} : PID {pid} absent") from None
    nom_prog, attendu = (r.programmes_relais or PROGRAMMES_RELAIS)[nom]
    progs = [a for a in args if os.path.basename(a) == nom_prog]
    if len(progs) != 1 or not os.path.isfile(progs[0]) or sha256_fichier(Path(progs[0])) != attendu:
        raise Refus(f"relais {nom} : programme {nom_prog} absent des arguments ou d'une autre empreinte que celle de la procédure")
    variable = _valeur_arg(args, "--variable-cle") or ("GEMINI_API_KEY" if nom in GEMINI else None)
    if variable != b["nom_cle"]:
        raise Refus(f"relais {nom} : lancé sur la variable {variable!r}, {b['nom_cle']} déclarée")
    port = _port_du_fournisseur(nom, b)
    if not port or _valeur_arg(args, "--port") != port:
        raise Refus(f"relais {nom} : port des arguments ({_valeur_arg(args, '--port')!r}) différent du port attendu ({port})")
    modeles_attendus = modeles_du_fournisseur(fixe, nom)
    if nom in GEMINI:
        modeles_args = sorted(_valeurs_arg(args, "--modele"))
    else:
        modeles_args = sorted(x for x in (_valeur_arg(args, "--modeles-permis") or "").split(",") if x)
    if modeles_args != modeles_attendus:
        raise Refus(f"relais {nom} : modèles permis des arguments {modeles_args} différents de la configuration (v5, constat 2)")
    out = {"pid": pid, "programme": progs[0], "programme_sha256": attendu, "variable_cle": variable, "port": port,
           "modeles": modeles_args}
    if nom == "claude":  # v11 (GO-2026-11-22-124) : le journal du relais dit chaque statut de l'interface (jamais le texte)
        journal = _valeur_arg(args, "--journal")
        if not journal or not os.path.isabs(journal):
            raise Refus("relais claude : --journal (chemin absolu) exigé : l'arrêt au premier refus de l'interface le lit")
        out["journal"] = journal
    egal_a_l_etat: dict = {}
    if nom == "claude" and _valeur_arg(args, "--reserve-par-appel") is not None:  # v11c, constat 8 : lue par PID si donnée
        try:
            egal_a_l_etat["reserve_par_appel_usd"] = float(_valeur_arg(args, "--reserve-par-appel"))
        except ValueError:
            raise Refus("relais claude : --reserve-par-appel illisible") from None  # bornes que /relais/etat doit rendre à l'identique des arguments (v7)
    if nom in GEMINI:
        max_appels = _entier_arg(args, "--max-appels", nom)
        minimum = 2 * (16 + 32 * n_especes) if nom == "argon" else MIN_APPELS_CARBON
        if max_appels < minimum:
            raise Refus(f"relais {nom} : --max-appels {max_appels} < {minimum} (comptes de jetons compris ; v7 : marge de "
                        f"{MARGE_APPELS_PROPOSEUR} lots pour Carbon)")
        out["max_appels"] = egal_a_l_etat["max_appels"] = max_appels
        if nom in GEMINI:  # v11 : relais Gemini v3 en flux (Carbon et Argon) ; délais explicites (aucun défaut supposé)
            for option in ("--delai-silence-s", "--delai-amont-s"):
                if _valeur_arg(args, option) is None:
                    raise Refus(f"relais {nom} : {option} absent des arguments lus par PID (explicite exigé)")
            try:
                silence, amont = float(_valeur_arg(args, "--delai-silence-s")), float(_valeur_arg(args, "--delai-amont-s"))
            except ValueError:
                raise Refus(f"relais {nom} : --delai-silence-s ou --delai-amont-s illisible") from None
            if not 0 < silence <= DELAI_SILENCE_RELAIS_MAX_S:
                raise Refus(f"relais {nom} : --delai-silence-s {silence:g} hors de ]0, {DELAI_SILENCE_RELAIS_MAX_S:g}] (coupure à 300 s)")
            if amont < DELAI_CARBON_S:
                raise Refus(f"relais {nom} : --delai-amont-s {amont:g} < délai de la commande {DELAI_CARBON_S} (relais ≥ commande)")
            if "--sans-pensees-amont" in args:
                raise Refus(f"relais {nom} : --sans-pensees-amont refusé (les pensées doivent être demandées à l'amont)")
            out["delai_silence_s"], out["delai_amont_s"] = silence, amont
    else:
        try:
            plafond = float(_valeur_arg(args, "--plafond-usd"))
        except (TypeError, ValueError):
            raise Refus(f"relais {nom} : --plafond-usd absent des arguments") from None
        exige_claude = ((parts or {}).get("claude") or {}).get("plafond_relais_exige_usd", PLAFOND_PART_CLAUDE_USD)  # v11 : 45
        if not _nombre(plafond) or plafond <= 0 or plafond > PLAFOND_ARRET_USD or (nom == "claude" and abs(plafond - exige_claude) > 1e-9):
            raise Refus(f"relais {nom} : plafond {plafond} hors règle (≤ 150 ; Claude : égal au plafond de la part Claude du relevé, "
                        f"{exige_claude} USD, v11)")
        out["plafond_usd"] = egal_a_l_etat["plafond_usd"] = plafond
        if nom in ("kimi", "astra"):
            part = ((parts or {}).get(nom) or {}).get("part_au_pire_usd")
            if not _nombre(part) or part <= 0:
                raise Refus(f"relais {nom} : part au pire inconnue : borne basse du plafond non contrôlable")
            if plafond < part - 1e-9:
                raise Refus(f"relais {nom} : plafond {plafond} < part au pire {part} USD : les derniers appels seraient refusés "
                            "(402) et l'étape « proposition » perdue (v7, majeur 1)")
            if nom == "astra" and plafond > part + 1e-9:
                raise Refus(f"relais astra : plafond {plafond} > part au pire {part} USD : la barrière du relais doit égaler la "
                            "part de la clé (16 × plafond de session)")
            max_appels = _entier_arg(args, "--max-appels", nom)
            if max_appels < MIN_APPELS_RELAIS_PROPOSEUR:
                raise Refus(f"relais {nom} : --max-appels {max_appels} < {MIN_APPELS_RELAIS_PROPOSEUR} ({APPELS_PAR_PROPOSEUR} "
                            f"cases + marge de {MARGE_APPELS_PROPOSEUR}) (v7, majeur 1)")
            out["max_appels"] = egal_a_l_etat["max_appels"] = max_appels
            out["part_au_pire_usd"] = part
    try:
        etat = (r.lire_etat_relais or _etat_relais)(f"http://127.0.0.1:{port}")
    except Exception as e:  # noqa: BLE001
        raise Refus(f"relais {nom} : /relais/etat illisible ({type(e).__name__})") from None
    if not isinstance(etat, dict):
        raise Refus(f"relais {nom} : /relais/etat n'est pas un objet")
    champs = ("appels",) + (("depense_usd", "engage_usd") if nom in RELAIS_A_DOLLARS else ())  # v11 : plus de lots pour Carbon
    absents = [k for k in champs if k not in etat]
    if absents:
        raise Refus(f"relais {nom} : /relais/etat sans {absents} : état non reconnu (autre service, réponse tronquée ?) — "
                    "un relais neuf lisible est exigé (v7, mineur 3)")
    if any(not _nombre(etat[k]) or etat[k] != 0 for k in champs):
        raise Refus(f"relais {nom} : relais déjà employé ({ {k: etat[k] for k in champs} }) : un relais neuf est exigé")
    if "pid" in etat and etat["pid"] != pid:
        raise Refus(f"relais {nom} : /relais/etat rend le PID {etat['pid']!r}, {pid} déclaré")
    for k, v in sorted(egal_a_l_etat.items()):
        lu = etat.get(k)
        if not _nombre(lu) or abs(float(lu) - float(v)) > 1e-9:
            raise Refus(f"relais {nom} : /relais/etat rend {k} = {lu!r}, les arguments lus par PID {v!r} (v7)")
    if nom in GEMINI + ("kimi", "astra") and etat.get("variable_cle_encore_presente") is not False:
        raise Refus(f"relais {nom} : variable de clé non effacée de son environnement (variable_cle_encore_presente "
                    f"{etat.get('variable_cle_encore_presente')!r})")
    if nom in ("kimi", "astra"):
        session = ((fixe or {}).get("plafonds_session") or {}).get("proposeur")
        reserve = etat.get("reserve_par_appel_usd")
        if not (_nombre(session) and _nombre(reserve) and 0 <= reserve <= session):
            raise Refus(f"relais {nom} : réserve par appel {reserve!r} USD hors de [0, plafond de session {session!r}] : "
                        "les derniers appels seraient refusés (402)")
        if nom == "astra":  # Kimi : refusé à la déclaration en v7 (liste des références admises vide) ; prix non recoupés
            a = ARGUMENTS_COMMANDES["astra"]
            prix = (float(a[a.index("--prix-entree") + 1]), float(a[a.index("--prix-sortie") + 1]))
            lus = (etat.get("prix_entree_usd_par_million"), etat.get("prix_sortie_usd_par_million"))
            if not all(_nombre(x) for x in lus) or tuple(float(x) for x in lus) != prix:
                raise Refus(f"relais {nom} : prix de l'état {lus!r} différents de ceux de la commande {prix!r} (la barrière en "
                            "dollars du relais compterait faux)")
        out["reserve_par_appel_usd"] = reserve
    if nom == "claude":  # v11c, constat 8 : réserve par appel lue dans l'état au départ, écrite au manifeste
        reserve = etat.get("reserve_par_appel_usd")
        if not (_nombre(reserve) and 0 <= reserve < float(out.get("plafond_usd") or 0)):
            raise Refus(f"relais claude : réserve par appel {reserve!r} USD illisible ou hors de [0, plafond du relais[ ; elle "
                        "borne le dépassement possible du plafond de la part Claude")
        out["reserve_par_appel_usd"] = reserve
        out["reserve_par_appel_source"] = "arguments lus par PID et état" if "reserve_par_appel_usd" in egal_a_l_etat \
            else "état (défaut du programme épinglé, absent des arguments)"
        out["depassement_possible_par_appel_en_vol_usd"] = round(float(fixe["plafonds_session"]["proposeur"]) - reserve, 6) \
            if fixe and _nombre((fixe.get("plafonds_session") or {}).get("proposeur")) else None
    out["etat_neuf"] = True
    return out


def porte_a_blanc(decl: dict) -> dict:
    """Constat 1 : chaque porte « commande » est jouée une fois avant le manifeste de départ, avec l'environnement minimal du
    contrat (`PortePlafondCommande`) et l'étape « porte-a-blanc » ; aucun appel au fournisseur ; accusé exigé au centime."""
    sortie = {}
    for nom, b in sorted(decl["fournisseurs"].items()):
        pp = b.get("porte_plafond") or {}
        if pp.get("type") != "commande":
            continue
        env = {"PATH": os.environ.get("PATH", os.defpath), "LANG": "C.UTF-8", "ETAPE_POLE": ETAPE_A_BLANC,
               "PLAFOND_ETAPE_USD": "1.00"}
        try:
            p = subprocess.run(pp["commande"], env=env, capture_output=True, text=True, timeout=float(pp["delai_s"]),
                               stdin=subprocess.DEVNULL)
        except (OSError, subprocess.SubprocessError) as e:
            raise Refus(f"porte à blanc de {nom} non jouée ({type(e).__name__})") from None
        lignes = [x for x in p.stdout.splitlines() if x.strip()]
        try:
            accuse = json.loads(lignes[-1]) if lignes else None
        except ValueError:
            accuse = None
        if p.returncode != 0 or not isinstance(accuse, dict) or accuse.get("etape") != ETAPE_A_BLANC \
                or round(float(accuse.get("plafond_usd") or -1), 2) != 1.00:
            raise Refus(f"porte à blanc de {nom} refusée (code {p.returncode}) : {(p.stderr or p.stdout).strip()[-300:]!r}")
        sortie[nom] = {"accuse": accuse, "code": 0}
    return sortie


# --- constat 2 : registre des GO dérivé ; constat 5 : prix Claude du jour -------------------------------------------------------


def verifier_registre_main(r: "Reglages") -> str | None:
    """v5, constat 5 (R-3249) : le registre lu est celui de `main` (le dépôt de travail mis à jour sur `origin/main`, récupérée
    avant) ; rend le commit source, cité par le registre dérivé. Sans référence (essais) : None."""
    if not r.ref_registre:
        return None
    commit = _git(r.depot, "rev-parse", r.ref_registre).strip()
    p = subprocess.run(["git", "-C", str(r.depot), "show", f"{r.ref_registre}:registres/go.md"], capture_output=True, timeout=60)
    if p.returncode != 0 or not r.registre_go.is_file() or p.stdout != r.registre_go.read_bytes():
        raise Refus(f"registre des GO du dépôt différent de celui de {r.ref_registre} ({commit[:8]}) : se mettre à jour sur main")
    return commit


def ecrire_registre_derive(registre: Path, chemin: Path, go_id: str = GO_ID, commit: str | None = None,
                           go_traces: tuple = (GO_COURSE_INITIAL,)) -> dict:
    """Lit le registre source par lignes nommées seulement (la ligne du GO et les révocations qui la visent) et écrit, scellé,
    un registre dérivé que la lecture de l'orchestrateur accepte (aucun identifiant en double)."""
    gardees = []
    for ligne in registre.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^\|\s*(GO-\d{4}-\d{2}-\d{2}-\d{2,3})\s*\|", ligne)
        if not m:
            continue
        cellules = [c.strip() for c in ligne.strip().strip("|").split("|")]
        vises = (go_id,) + tuple(go_traces)  # v11b : GO de la course et GO prolongé (traçabilité)
        if m.group(1) in vises and not (len(cellules) == 8 and cellules[3].lower().startswith("extension")):
            gardees.append(ligne)
        elif len(cellules) == 8 and cellules[2] == "révocation" and any(g in (cellules[3] + cellules[7]) for g in vises):
            gardees.append(ligne)
    texte = ("# Registre des GO dérivé (course d'affinage, lanceur v5) — lignes nommées seulement\n\n"
             f"Source : `registres/go.md` de main au commit {commit or 'non cité (essai)'} (R-3249).\n\n"
             "| id | accordé le | type | périmètre | plafond | échéance | accordé par | référence |\n"
             "|---|---|---|---|---|---|---|---|\n" + "\n".join(gardees) + "\n")
    h = ecrire_scelle(chemin, texte)
    return {"source": str(registre), "source_sha256": sha256_fichier(registre), "commit_source": commit, "derive": str(chemin),
            "derive_sha256": h,
            "lignes": [hashlib.sha256(l.encode("utf-8")).hexdigest() for l in gardees], "nombre_de_lignes": len(gardees)}


def verifier_releve_prix(chemin: Path, fixe: dict, aujourd_hui: _dt.date) -> dict:
    """Constat 5 (condition de GO-2026-11-18-14 : « prix Claude relevé avant le départ ») : fichier du jour, scellé, prix des
    deux espèces Claude (par leur rang dans la configuration) égaux au barème du relais épinglé ; source et heure exigées."""
    o, h = lire_json_scelle(chemin, "relevé des prix Claude")
    if not str(o.get("releve_utc") or "").startswith(aujourd_hui.isoformat()):
        raise Refus(f"relevé des prix Claude : du jour ({aujourd_hui}) exigé")
    if not isinstance(o.get("source"), str) or not o["source"].strip():
        raise Refus("relevé des prix Claude : source exigée")
    claude = [e for e in fixe["especes"] if e["famille"] == "claude"]
    prix = o.get("prix") or {}
    for k, e in enumerate(claude, 1):
        lu = prix.get(f"espece_claude_{k}")
        if not (isinstance(lu, dict) and [lu.get("entree"), lu.get("sortie")] == list(BAREME_CLAUDE[e["modele"]])):
            raise Refus(f"relevé des prix Claude : espèce Claude {k} lue {lu!r}, différente du barème du relais : arrêt, nouveau devis")
    return {"chemin": str(chemin), "sha256": h, "source": o["source"], "releve_utc": o["releve_utc"], "egal_au_bareme": True}


def verifier_sonde_astra(r: "Reglages", decl: dict, aujourd_hui: _dt.date) -> dict:
    """C (R-3273) : Astra n'est déclarée qu'après un appel trivial réussi par sa commande épinglée, par un relais jeté, pour
    0,05 USD au plus ; le relais de la course est neuf (contrôlé par `controler_relais_vivant`)."""
    if "astra" not in decl["fournisseurs"]:
        return {"astra": "non déclarée", "motif": (decl.get("absences") or {}).get("astra")}
    # v7 (mineur 8, majeur 2) : le rapport v2 n'est accepté que lié, par son empreinte, au rapport de la sonde commune du jour
    # (`scripts/sonde_astra_courses_v1.py`, épinglée), qui a contrôlé le relais jeté avant l'appel.
    jour = aujourd_hui.isoformat()
    communes = [(m.format(jour=jour), r.depot / m.format(jour=jour)) for m in r.sondes_astra_communes]
    trouvees = [(rel, p) for rel, p in communes if p.exists()]
    if len(trouvees) != 1:
        raise Refus(f"sonde d'Astra : {len(trouvees)} rapport(s) de la sonde commune du jour parmi {[x for x, _ in communes]} "
                    "(un seul exigé, R-3273) ; un autre jour : sonde neuve, rapports sous course-v11/")
    rel_c, chemin_c = trouvees[0]
    c, h_c = lire_json_scelle(chemin_c, "rapport de la sonde commune d'Astra")
    rj = c.get("relais_jete") if isinstance(c.get("relais_jete"), dict) else {}
    v2c = c.get("rapport_v2") if isinstance(c.get("rapport_v2"), dict) else {}
    ecarts = []
    if c.get("version") != VERSION_SONDE_COMMUNE:
        ecarts.append(f"version {c.get('version')!r}")
    if c.get("ok") is not True or c.get("echec_de_configuration") is not False or c.get("appel_envoye") is not True:
        ecarts.append("sonde commune non réussie")
    if c.get("jour") != jour or not str(c.get("horodatage_utc") or "").startswith(jour):
        ecarts.append(f"jour {c.get('jour')!r}")
    if (c.get("sonde_v2") or {}).get("sha256") != PIECES["sonde_astra"][1]:
        ecarts.append("sonde v2 d'une autre empreinte")
    sha_commande = sha256_fichier(Path(decl["fournisseurs"]["astra"]["commande"][3]))  # épinglée par verifier_declaration
    if (c.get("commande") or {}).get("sha256") != sha_commande:
        ecarts.append("commande d'une autre empreinte que la commande déclarée")
    if rj.get("variable_cle") != VARIABLE_CLE_SONDE_ASTRA:  # v11c, constat 9
        ecarts.append(f"variable de clé du relais jeté {rj.get('variable_cle')!r}, {VARIABLE_CLE_SONDE_ASTRA} exigée")
    if rj.get("programme_sha256") != PROGRAMMES_RELAIS["astra"][1] or rj.get("max_appels") != 1 \
            or rj.get("plafond_usd") != SONDE_ASTRA_MAX_USD or rj.get("port") in PORTS_DES_COURSES:
        ecarts.append("relais jeté hors règle (programme, un appel, 0,05 USD, port hors des courses)")
    dep = c.get("depense_relais_usd")
    if not _nombre(dep) or dep > SONDE_ASTRA_MAX_USD:
        ecarts.append(f"dépense lue au relais jeté {dep!r}")
    if ecarts:
        raise Refus(f"sonde d'Astra : rapport de la sonde commune {rel_c} refusé ({'; '.join(ecarts)})")
    permis = {m.format(jour=jour) for m in r.sondes_astra_v2}
    permis |= {str(r.depot / x) for x in permis}
    if v2c.get("chemin") not in permis:
        raise Refus(f"sonde d'Astra : la sonde commune cite le rapport v2 {v2c.get('chemin')!r}, hors des chemins lus par ce "
                    f"lanceur {sorted(m.format(jour=jour) for m in r.sondes_astra_v2)}")
    chemin_v2 = Path(v2c["chemin"]) if os.path.isabs(v2c["chemin"]) else r.depot / v2c["chemin"]
    o, h = lire_json_scelle(chemin_v2, "sonde d'Astra")
    if h != v2c.get("sha256"):
        raise Refus("sonde d'Astra : rapport v2 d'une autre empreinte que celle citée par la sonde commune")
    if o.get("relais_pid") != rj.get("pid"):
        raise Refus("sonde d'Astra : rapport v2 et sonde commune d'un autre relais jeté")
    if not str(o.get("horodatage_utc") or "").startswith(aujourd_hui.isoformat()):
        raise Refus("sonde d'Astra : du jour exigée")
    cout = o.get("cout_usd")
    if o.get("code") != 0 or o.get("ok") is not True or not isinstance(cout, (int, float)) or cout > SONDE_ASTRA_MAX_USD:
        raise Refus(f"sonde d'Astra échouée ou trop chère ({o.get('code')!r}, {cout!r} USD) : Astra ne se déclare pas")
    if o.get("version") != VERSION_SONDE_ASTRA:
        raise Refus("sonde d'Astra : fichier non écrit par la sonde épinglée (scripts/sonde_astra_affinage_v3.py)")
    servi = o.get("modele_servi")
    attendu = MODELES_RELAIS["astra"][0]
    if not (isinstance(servi, str) and re.fullmatch(re.escape(attendu) + r"(-\d{4}-?\d{2}-?\d{2})?", servi)):
        raise Refus(f"sonde d'Astra : modèle servi {servi!r}, {attendu} exigé")
    if o.get("commande_sha256") != sha256_fichier(Path(decl["fournisseurs"]["astra"]["commande"][3])):
        raise Refus("sonde d'Astra faite par une autre commande que la commande épinglée")
    if o.get("relais_pid") == (decl.get("metas", {}).get("astra") or {}).get("pid_relais"):
        raise Refus("sonde d'Astra faite par le relais de la course : un relais jeté est exigé")
    return {"chemin": str(chemin_v2), "sha256": h, "cout_usd": cout, "modele_servi": o.get("modele_servi"),
            "sonde_commune": {"chemin": rel_c, "sha256": h_c, "relais_jete_pid": rj.get("pid"),
                              "depense_relais_usd": dep},
            "relais_jete_a_arreter": f"PID {rj.get('pid')} : arrêt par son PID (R10), consigné dans registres/arrets.md"}


# D (R-3273) : aucun nom de personne interne, aucun identifiant de session, aucun courriel dans un texte servi. Les noms
# d'auteurs de travaux publiés cités par les idées (Berkson, Petri, Gu, Krenn…) restent.
MOTIFS_CONFIDENTIELS = (
    ("courriel", re.compile(r"[\w.+-]+@[\w-]+(?:\.[\w-]+)+")),
    ("identifiant de session", re.compile(r"session_[A-Za-z0-9]{6,}|claude\.ai/\S+|\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b")),
    ("nom de variable de clé", re.compile(r"\bRR_[A-Z0-9_]+\b")),
    ("nom de personne interne", re.compile(r"\b(Lazar|Ciric|lciric|Rigaud|Minuit|Luc|Heimersheim|Kirchner|Ibrahim|Scheurer|Colognese|"
                                          r"Ward|Jang|Feng)\b")),
)


def expurger(texte: str) -> tuple:
    """Rend (texte expurgé, liste des expurgations {motif, empreinte de l'extrait}) ; jamais l'extrait lui-même."""
    faites = []
    for motif, rx in MOTIFS_CONFIDENTIELS:
        for m in rx.finditer(texte):
            faites.append({"motif": motif, "extrait_sha256": hashlib.sha256(m.group(0).encode("utf-8")).hexdigest()})
        texte = rx.sub("[retiré]", texte)
    return texte, faites


def verifier_confidentialite(textes: dict) -> None:
    """Refus si un texte servi porte encore un motif confidentiel (D, R-3273)."""
    for nom, t in textes.items():
        for motif, rx in MOTIFS_CONFIDENTIELS:
            if rx.search(t):
                raise Refus(f"texte servi « {nom} » : {motif} présent (R-3273) : départ refusé")


def envelopper_commandes(decl: dict, python: str, garde: Path, dossier_arrets: Path) -> dict:
    """Met la garde de crédit devant la commande de chaque relais dispensable actif (Argon, Astra, Carbon)."""
    option = [] if decl.get("compter_limite_de_debit_comme_soupcon", True) else ["--limite-de-debit-pas-soupcon"]
    for nom in FOURNISSEURS_DISPENSABLES:
        b = decl["fournisseurs"].get(nom)
        if b is not None:
            b["commande"] = [python, "-I", "-B", str(garde), str(dossier_arrets), nom] + option + ["--"] + list(b["commande"])
    return decl


# --- v11 : garde des appels à Google (règle gelée de CLAUDE.md, GO-2026-11-21-71) -----------------------------------------------


ROLES_GOOGLE = {"carbon": (("proposeur_ideation", "proposeur", "consigne_proposeur"),),
                "argon": (("proposeur_ideation", "proposeur", "consigne_proposeur"), ("juge_ideation", "juge", "consigne_juge"))}
MOTIF_CAPTURE = "capture du lanceur v11 : rien n'est envoyé"


class FauxAmontGoogle:
    """Faux amont local de l'interface de Google : `countTokens` rend un compte (octets / 4), toute génération
    (`generateContent`, `streamGenerateContent`, `batchGenerateContent`) est **capturée** et reçoit un 503. Aucun réseau."""

    def __init__(self):
        self.captures = []
        moi = self

        class H(BaseHTTPRequestHandler):
            def do_POST(self):
                n = int(self.headers.get("Content-Length") or 0)
                brut = self.rfile.read(n)
                try:
                    objet = json.loads(brut or b"{}")
                except ValueError:
                    objet = None
                if self.path.split("?")[0].endswith(":countTokens"):
                    code, rep = 200, {"totalTokens": max(1, len(brut) // 4)}
                else:
                    moi.captures.append({"chemin": self.path, "corps": objet})
                    code, rep = 503, {"error": {"code": 503, "message": MOTIF_CAPTURE}}
                donnees = json.dumps(rep).encode("utf-8")
                self.send_response(code)
                self.send_header("Content-Type", "application/json")
                self.send_header("Content-Length", str(len(donnees)))
                self.end_headers()
                self.wfile.write(donnees)

            def do_GET(self):
                self.send_response(404)
                self.end_headers()

            def log_message(self, *a):
                pass

        self.serveur = ThreadingHTTPServer(("127.0.0.1", 0), H)
        self.serveur.daemon_threads = True
        threading.Thread(target=self.serveur.serve_forever, daemon=True).start()
        self.url = f"http://127.0.0.1:{self.serveur.server_address[1]}"

    def fermer(self):
        self.serveur.shutdown()
        self.serveur.server_close()


def charger_garde_google(chemin: Path, attendu: str):
    if not chemin.is_file() or sha256_fichier(chemin) != attendu:
        raise Refus(f"garde des appels à Google absente ou d'une autre empreinte que {attendu[:12]}… ({chemin})")
    spec = importlib.util.spec_from_file_location("garde_google_pour_lanceur_affinage_v11", chemin)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def arguments_enveloppe_argon(enveloppe: Path) -> list:
    """Arguments que l'enveloppe d'Argon (épinglée) passe à sa commande : ceux de sa ligne `exec` (lignes continuées
    jointes), après `"$COMMANDE"`, `"$@"` retiré (l'orchestrateur n'en passe aucun)."""
    texte = enveloppe.read_text(encoding="utf-8").replace("\\\n", " ")
    lignes = [l for l in texte.splitlines() if l.strip().startswith("exec ")]
    if len(lignes) != 1:
        raise Refus(f"enveloppe d'Argon : {len(lignes)} ligne(s) « exec » (une exigée)")
    jetons = shlex.split(lignes[0])
    if "$COMMANDE" not in jetons:
        raise Refus("enveloppe d'Argon : « $COMMANDE » absent de la ligne exec")
    return [j for j in jetons[jetons.index("$COMMANDE") + 1:] if j != "$@"]


def _remplacer_option(args: list, option: str, valeur: str) -> list:
    if option not in args:
        return list(args) + [option, valeur]
    out = list(args)
    for k, a in enumerate(out[:-1]):
        if a == option:
            out[k + 1] = valeur
    return out


def capturer_corps_google(python: str, commande: Path, args: list, env_plus: dict, consigne: str) -> dict:
    """Joue la commande épinglée hors ligne devant le faux amont ; rend {code, captures}."""
    amont = FauxAmontGoogle()
    try:
        env = {"PATH": os.environ.get("PATH", os.defpath), "LANG": "C.UTF-8", **env_plus}
        p = subprocess.run([python, "-I", "-B", str(commande)] + _remplacer_option(args, "--url-base", amont.url + "/v1beta"),
                           input=consigne.encode("utf-8"), env=env, capture_output=True, timeout=180)
    except (OSError, subprocess.SubprocessError) as e:
        raise Refus(f"garde Google : commande {commande.name} non jouée hors ligne ({type(e).__name__})") from None
    finally:
        amont.fermer()
    return {"code": p.returncode, "captures": amont.captures}


def corps_de_generation(capture: dict) -> tuple:
    """(corps de génération, mode de la garde) : lot → la requête unique du lot ; flux ou synchrone → le corps lui-même. Le
    relais v3 passe un `generateContent` à l'amont en flux : une commande qui parle au port de Carbon est en mode « flux »."""
    chemin, corps = capture["chemin"].split("?")[0], capture["corps"]
    if not isinstance(corps, dict):
        return None, None
    if chemin.endswith(":batchGenerateContent"):
        try:
            return corps["batch"]["input_config"]["requests"]["requests"][0]["request"], "non_diffuse"
        except (KeyError, IndexError, TypeError):
            return None, "non_diffuse"
    return corps, ("flux" if chemin.endswith(":streamGenerateContent") else "non_diffuse")


def _provision(args: list, corps: dict):
    v = _valeur_arg(args, "--provision-pensee-jetons")
    if v is not None:
        try:
            return int(float(v))
        except ValueError:
            return None
    pensee = ((corps or {}).get("generationConfig") or {}).get("thinkingConfig") or {}
    return pensee.get("thinkingBudget")


def controler_chemins_google(r: "Reglages", decl: dict, pieces: dict, fixe: dict, liste: dict) -> dict:
    """Pour chaque commande Google déclarée (Argon, Carbon) et chaque rôle qu'elle tient : corps réel capturé hors ligne,
    `verifier_reglages_google` de la garde épinglée (mode « flux » pour Carbon, que le relais v3 sert en flux ; « non diffusé »
    pour Argon et le lot), limite de l'invite d'un proposeur (cartes × 9 000 caractères, un jeton au plus par caractère) sous
    le plafond de texte. Rend {espèce: {conforme, roles}} ; aucune consigne n'y est écrite."""
    garde_chemin = Path(pieces["garde_google"]["absolu"])
    garde = charger_garde_google(garde_chemin, pieces["garde_google"]["sha256"])
    consigne_p_texte = Path(pieces["consigne_proposeur"]["absolu"]).read_text(encoding="utf-8")
    consigne_j_texte = Path(pieces["consigne_juge"]["absolu"]).read_text(encoding="utf-8")
    # v11c (constat 11) : la plus longue entrée de chaque rôle : proposeur, consigne servie de la case la plus longue ; juge,
    # entrée de la forme de l'orchestrateur pour la carte la plus longue permise
    plus_longue = {"consigne_proposeur": max((consigne_servie_proposeur(consigne_p_texte, expurger(texte_de_case(f))[0])
                                              for f in liste["fils"]), key=len),
                   "consigne_juge": entree_juge_la_plus_longue(consigne_j_texte)}
    out = {"garde": {"chemin": pieces["garde_google"]["chemin"], "sha256": pieces["garde_google"]["sha256"],
                     "version": getattr(garde, "VERSION_GARDE", None)}}
    for nom in ("argon", "carbon"):
        b = decl["fournisseurs"].get(nom)
        if b is None:
            continue
        c = b.get("commande") or []
        if len(c) >= 4 and c[0] != "bash":  # v11 : commande déclarée (en flux) ; --garde remplacé par la pièce vérifiée
            commande, args, env_cle = Path(c[3]), (_remplacer_option(list(c[4:]), "--garde", str(garde_chemin)) if "--garde" in c[4:] else list(c[4:])), {}
        else:  # enveloppe v5 d'Argon (hors garde) : jouée telle quelle pour dire ce qu'elle enverrait
            commande = Path(pieces["commande_argon"]["absolu"])
            args = arguments_enveloppe_argon(Path(pieces["enveloppe_argon"]["absolu"]))
            env_cle = {"GEMINI_API_KEY": "factice-relais"}  # comme l'enveloppe : jeton factice, la vraie clé reste au relais
        roles = []
        for role_pole, role_plafond, consigne_piece in ROLES_GOOGLE[nom]:
            consigne = plus_longue[consigne_piece]
            env = dict(env_cle, PLAFOND_SESSION_USD=str(fixe["plafonds_session"][role_plafond]), ROLE_POLE=role_pole)
            jeu = capturer_corps_google(r.python, commande, args, env, consigne)
            problemes, reglages = [], None
            gens = [corps_de_generation(x) for x in jeu["captures"]]
            if len(gens) != 1 or gens[0][0] is None:
                problemes.append(f"aucun corps de génération capturé (code {jeu['code']}, {len(gens)} capture(s)) : la "
                                 "commande n'a pas atteint l'envoi, rien ne peut être vérifié")
            else:
                corps, mode = gens[0]
                if "--niveau-reflexion" in args:  # commande en flux (relais v3 : amont lu en flux)
                    mode = "flux"
                provision = _provision(args, corps)
                problemes += list(garde.verifier_reglages_google(nom, corps, provision=provision, mots=None, mode=mode))
                config = corps.get("generationConfig") if isinstance(corps.get("generationConfig"), dict) else {}
                reglages = {"mode": mode, "provision": provision, "maxOutputTokens": config.get("maxOutputTokens"),
                            "thinkingConfig": config.get("thinkingConfig")}
                plafond = config.get("maxOutputTokens")
                if role_plafond == "proposeur" and isinstance(plafond, int) and isinstance(provision, int):
                    limite = int(fixe.get("cartes_par_appel") or 1) * CARACTERES_PAR_CARTE_MAX
                    if limite >= plafond - provision:
                        problemes.append(f"limite de l'invite : {limite} caractères (≤ {limite} jetons) ≥ plafond de texte "
                                         f"{plafond - provision}")
            roles.append({"role": role_pole, "plafond_session_usd": fixe["plafonds_session"][role_plafond],
                          "entree_caracteres": len(consigne),
                          "code_commande": jeu["code"], "reglages_captures": reglages, "problemes": problemes})
        out[nom] = {"commande": str(commande), "commande_sha256": sha256_fichier(commande), "roles": roles,
                    "conforme": all(not x["problemes"] for x in roles)}
    return out


def verifier_palier_astra(pieces: dict, liste: dict) -> dict:
    """v11 : prix d'Astra à palier (R-4905) : l'entrée la plus longue servie (consigne servie en octets, plus les 1 024 octets
    de marge de la commande d'Astra ; un jeton au plus par octet) reste sous 272 000 jetons."""
    consigne = Path(pieces["consigne_proposeur"]["absolu"]).read_text(encoding="utf-8")
    borne = max(len(consigne_servie_proposeur(consigne, expurger(texte_de_case(f))[0]).encode("utf-8")) for f in liste["fils"]) + 1024
    if borne >= PALIER_ASTRA_JETONS:
        raise Refus(f"Astra : entrée bornée à {borne} jetons ≥ palier {PALIER_ASTRA_JETONS} : prix 16 / 60, hors devis")
    return {"borne_entree_jetons": borne, "palier_jetons": PALIER_ASTRA_JETONS, "prix_usd_par_million": list(PRIX_ASTRA)}


# --- v11 : part Claude sur LUC, comptée au fil de l'eau (GO-2026-11-22-124 ; plafond propre, R-4995) -------------------------


STATUT_NON_REFUS = 429  # v11 : tout statut 4xx de l'interface autre que 429 (limite de débit) est un refus (crédit : 400, R-4833)


def est_refus_interface(statut) -> bool:
    return isinstance(statut, int) and not isinstance(statut, bool) and 400 <= statut < 500 and statut != STATUT_NON_REFUS


JOURNAL_PART_CLAUDE = "journal-part-claude-au-fil-de-l-eau.jsonl"  # v11c, constat 6 : une ligne par lecture, scellé à la fin
CHAMPS_ETAT_CLAUDE = ("plafond_usd", "reserve_par_appel_usd", "depense_usd", "engage_usd", "appels", "refus", "refus_modele",
                      "restant_usd", "appels_au_dessus_de_la_reserve", "depassement_max_usd")


class SurveillanceCleClaude:
    """GO-2026-11-22-124. Relit l'état du relais Claude et son journal (statuts seulement, jamais un contenu) ; `depasse()` rend
    {code: 5, nature, statut, cause, motif} ou None.
    Déclencheurs (v11c, constat 7 : gardés plus larges que le texte, écrits comme tels) : premier statut de 400 à 499 hors 429 au
    journal — appel relayé (refus de l'interface d'Anthropic) ou refus propre du relais (401 jeton, 402 plafond, 403 modèle,
    404 chemin, 413 corps : sa ligne porte un `motif`) ; `refus` > 0 dans l'état (refus du relais dont la ligne n'est pas encore
    lue) ; part engagée (dépense + réservé des appels en vol) au plafond propre ; état ou journal illisible trois fois de suite.
    L'arrêt écrit la nature, le statut et la cause réels : le motif du relais quand sa ligne en porte un ; « inconnue » pour un
    appel relayé, dont le relais ne garde que le statut.
    v11c, constat 6 : chaque lecture (lisible ou non) est écrite au journal du run (montants, comptes, statuts) ; compte des appels
    par statut et dernier état lu (dépassement, réserve) au bilan. Constat 5 : `lecture_finale()` après l'arrêt de
    l'orchestrateur. Une ligne du journal du relais encore sans fin de ligne est lue à la lecture suivante ; une lecture manquée
    isolée est comptée, jamais tue."""

    def __init__(self, r: "Reglages", url: str, plafond_part: float, journal: str | None = None, journal_run: Path | None = None):
        self.r, self.url, self.plafond_part, self.journal = r, url, plafond_part, journal
        self.journal_run = Path(journal_run) if journal_run is not None else None
        self.illisibles, self.lectures, self.derniere, self.refus, self.vu = 0, 0, None, None, 0
        self.par_statut: dict = {}
        self.etat: dict = {}
        self.lignes_ecrites = 0

    def _ecrire(self, ligne: dict) -> None:
        self.lignes_ecrites += 1
        if self.journal_run is not None:
            with open(self.journal_run, "a", encoding="utf-8") as f:
                f.write(json.dumps(ligne, ensure_ascii=False, sort_keys=True) + "\n")

    def _lignes_du_relais(self) -> tuple:
        """(nombre de lignes complètes, lignes neuves lues) ; une ligne illisible lève (lecture manquée, rien n'est compté)."""
        if not self.journal:
            return self.vu, []
        p = Path(self.journal)
        if not p.exists():
            return self.vu, []  # aucun appel encore : le relais crée son journal au premier appel
        texte = p.read_text(encoding="utf-8", errors="replace")
        lignes = texte[: texte.rfind("\n") + 1].splitlines()
        return len(lignes), [json.loads(x) for x in lignes[self.vu:] if x.strip()]

    def _arret(self, nature: str, statut, cause: str) -> dict:
        return {"code": 5, "nature": nature, "statut": statut, "cause": cause,
                "motif": f"{nature} : statut {statut if statut is not None else 'sans objet'} ; cause : {cause} ; part engagée "
                         f"{self.derniere} USD (plafond de la part Claude {self.plafond_part} USD)"}

    def depasse(self, moment: str = "au fil de l'eau"):
        quand = _dt.datetime.now(_dt.timezone.utc).isoformat()
        try:
            etat = (self.r.lire_etat_relais or _etat_relais)(self.url)
            engagee = float(etat.get("depense_usd") or 0.0) + float(etat.get("engage_usd") or 0.0)
            refus = etat.get("refus", 0) or 0
            if not (math.isfinite(engagee) and _nombre(refus)):
                raise ValueError("non fini")
            n_lignes, neuves = self._lignes_du_relais()
        except Exception as e:  # noqa: BLE001
            self.illisibles += 1
            self._ecrire({"quand": quand, "moment": moment, "lisible": False, "erreur": type(e).__name__,
                          "illisibles_de_suite": self.illisibles})
            if self.illisibles >= LECTURES_ILLISIBLES_MAX:
                return self._arret("part Claude non comptable", None, f"état ou journal du relais Claude illisible "
                                   f"{self.illisibles} fois de suite ({type(e).__name__})")
            return None
        self.vu = n_lignes
        statuts_neufs: dict = {}
        premier = None
        for o in neuves:
            s = o.get("statut")
            statuts_neufs[str(s)] = statuts_neufs.get(str(s), 0) + 1
            if premier is None and est_refus_interface(s):
                premier = o
        for k, n in statuts_neufs.items():
            self.par_statut[k] = self.par_statut.get(k, 0) + n
        self.illisibles, self.lectures = 0, self.lectures + 1
        self.derniere, self.refus = round(engagee, 6), refus
        self.etat = {k: etat.get(k) for k in CHAMPS_ETAT_CLAUDE if k in etat}
        self._ecrire({"quand": quand, "moment": moment, "lisible": True, "lecture": self.lectures, "etat": self.etat,
                      "part_engagee_usd": self.derniere, "statuts_neufs": statuts_neufs})
        if premier is not None:
            s = premier.get("statut")
            if premier.get("motif") is not None:  # refus propre du relais : sa ligne dit la cause
                return self._arret("refus du relais Claude", s, str(premier.get("motif")))
            return self._arret("refus de l'interface d'Anthropic, relayé", s,
                               "inconnue : le relais ne garde que le statut d'un appel relayé (un statut 400 peut être un crédit "
                               "insuffisant, R-4833, ou une requête refusée)")
        if refus > 0:
            return self._arret("refus du relais Claude", None,
                               f"{refus} refus comptés dans l'état du relais, ligne non encore lue à son journal (401 jeton, 402 "
                               "plafond, 403 modèle, 404 chemin ou 413 corps : la ligne du journal dit lequel)")
        if engagee >= self.plafond_part - 1e-9:
            return self._arret("part engagée au plafond", None,
                               f"part Claude engagée {self.derniere} USD ≥ plafond de la part Claude {self.plafond_part} USD "
                               "(déclencheur du lanceur, avant le refus du relais)")
        return None

    def lecture_finale(self):
        """v11c, constat 5 : relecture après l'arrêt de l'orchestrateur ; une lecture illisible est refaite, jusqu'à
        LECTURES_ILLISIBLES_MAX lectures manquées de suite (alors code 5, part non comptable)."""
        for _ in range(LECTURES_ILLISIBLES_MAX):
            a = self.depasse(moment="relecture finale")
            if a is not None or self.illisibles == 0:
                return a
        return self._arret("part Claude non comptable", None, "relecture finale illisible")

    def sceller_journal(self) -> dict | None:
        """Compagnon `.sha256` du journal du run (écrit une fois, à la fin)."""
        if self.journal_run is None or not self.journal_run.is_file():
            return {"chemin": None, "lignes": self.lignes_ecrites}
        h = sha256_fichier(self.journal_run)
        with open(str(self.journal_run) + ".sha256", "x", encoding="utf-8") as f:
            f.write(f"{h}  {self.journal_run.name}\n")
        return {"chemin": str(self.journal_run), "sha256": h, "lignes": self.lignes_ecrites}

    def bilan(self) -> dict:
        return {"plafond_part_claude_usd": self.plafond_part, "lectures": self.lectures, "derniere_part_engagee_usd": self.derniere,
                "refus_du_relais": self.refus, "illisibles_de_suite": self.illisibles, "journal": self.journal,
                "appels_par_statut": dict(sorted(self.par_statut.items())), "dernier_etat_lu": dict(self.etat),
                "depassement_max_usd": self.etat.get("depassement_max_usd"),
                "appels_au_dessus_de_la_reserve": self.etat.get("appels_au_dessus_de_la_reserve"),
                "reserve_par_appel_usd": self.etat.get("reserve_par_appel_usd"), "lectures_ecrites_au_journal_du_run": self.lignes_ecrites}

# --- (6) orchestrateur --------------------------------------------------------------------------------------------------------


def _git(dossier: Path, *args: str) -> str:
    p = subprocess.run(["git", "-C", str(dossier), *args], capture_output=True, text=True, timeout=60)
    if p.returncode != 0:
        raise Refus(f"git {' '.join(args)} dans {dossier} : code {p.returncode} ({p.stderr.strip()[:200]})")
    return p.stdout


def verifier_orchestrateur(r: Reglages) -> dict:
    presents = [o for o in r.orchestrateurs if (o / LANCEUR_ORCHESTRATEUR).is_file()]
    if len(presents) != 1:
        raise Refus(f"orchestrateur : {len(presents)} copie(s) trouvée(s) parmi {[str(o) for o in r.orchestrateurs]} (une exigée)")
    o = presents[0]
    tete = _git(o, "rev-parse", "HEAD").strip()
    if tete != r.commit_orchestrateur:
        raise Refus(f"orchestrateur au commit {tete}, {r.commit_orchestrateur} exigé")
    porcelaine = _git(o, "status", "--porcelain", "--untracked-files=all", "--ignored=matching").strip()
    if porcelaine:
        raise Refus(f"orchestrateur modifié, fichiers non suivis ou ignorés : {porcelaine[:200]!r}")
    ecarts = {rel: (sha256_fichier(o / rel) if (o / rel).is_file() else None) for rel in r.empreintes_orchestrateur}
    ecarts = {k: v for k, v in ecarts.items() if v != r.empreintes_orchestrateur[k]}
    if ecarts:
        raise Refus(f"orchestrateur : empreintes différentes ou fichiers absents : {ecarts}")
    return {"chemin": str(o), "commit": tete, "empreintes": dict(r.empreintes_orchestrateur)}


# --- (1) configuration de l'orchestrateur, acte de gel ------------------------------------------------------------------------


def assembler_configuration(fixe: dict, liste: dict, pieces: dict, decl: dict, specification: dict | None) -> dict:
    garde_configuration_fixe(fixe)
    garde_cles_configuration(fixe)
    actives = decl["especes_actives"]
    if not any(e["famille"] == "claude" for e in actives):
        raise Refus("aucune espèce Claude active : Claude d'abord (R-3209, point 2)")
    interdites = list(fixe["etiquettes_interdites_fixes"]) + [x["numero"] for x in liste["retraits"]["idees_de_la_table"]] \
        + sorted({f for x in liste["retraits"]["reserves_de_cloisonnement"] for f in x["fiches"]})
    conf = {k: v for k, v in fixe.items() if k not in ("version", "statut", "orchestrateur", "generations", "cartes_par_appel",
                                                       "especes", "etiquettes_interdites_fixes", "cles",
                                                       "cles_interdites", "credit_declare_usd", "regle_cles_v3",
                                                       "relais_persistants_v4", "carbon_v5", "confidentialite_v5",
                                                       "risques_v6", "changements_v11", "argon_v11")}
    conf["proposeurs"] = [{"etiquette": e["etiquette"], "modele": e["modele"], "fournisseur": e["fournisseur"],
                           "consigne": "consigne_proposeur"} for e in actives]
    cases, expurgations = [], []
    for f in liste["fils"]:
        t, faites = expurger(texte_de_case(f))
        expurgations += [dict(x, fil=f["rang"]) for x in faites]
        cases.append([t, "affinage"])
    verifier_confidentialite({f"fil {k + 1}": c[0] for k, c in enumerate(cases)})
    conf["cases"] = cases
    conf["_expurgations"] = expurgations
    conf["pieces"] = {n: {"chemin": pieces[n]["absolu"], "sha256": pieces[n]["sha256"]} for n in PIECES_SERVIES}
    conf["etiquettes_interdites"] = interdites
    conf["fournisseurs"] = decl["fournisseurs"]
    if specification is not None:
        conf["specification"] = specification
    for e in actives:
        if e["fournisseur"] not in conf["fournisseurs"]:
            raise Refus(f"espèce {e['etiquette']} active sans relais")
    utilises = {conf["aiguilleur"]["fournisseur"]} | {j["fournisseur"] for j in conf["juges"]} | \
        {x["fournisseur"] for x in conf["lecteurs_etiquettes"]}
    manquants = sorted(utilises - set(conf["fournisseurs"]))
    if manquants:
        raise Refus(f"relais absents pour l'aiguilleur, un juge ou un lecteur : {manquants}")
    return conf


def garde_cles_configuration(fixe: dict) -> None:
    """v11 : la configuration fixe nomme LUC pour Claude, exclut Rigaud et Minuit, et chaque espèce Claude porte LUC."""
    if (fixe.get("cles") or {}).get("claude") != CLE_CLAUDE:
        raise Refus(f"configuration : cles.claude doit être {CLE_CLAUDE}")
    if any(c not in (fixe.get("cles_interdites") or []) for c in CLES_INTERDITES):
        raise Refus(f"configuration : les clés {list(CLES_INTERDITES)} doivent figurer dans cles_interdites")
    for e in fixe.get("especes") or []:
        if e.get("famille") == "claude" and e.get("cle") != CLE_CLAUDE:
            raise Refus(f"configuration : espèce {e.get('etiquette')} sur une autre clé que {CLE_CLAUDE}")


def garde_configuration_fixe(fixe: dict) -> None:
    """Garde (1) sur la partie fixe : S17 = plafond d'arrêt, portée « course », une génération, étapes retirées par
    construction, plafonds de relais des étapes protégées ≤ S17, aucune étape de tests de mort."""
    b = fixe.get("budget") or {}
    if b.get("plafond_usd") != PLAFOND_ARRET_USD:
        raise Refus(f"configuration : budget.plafond_usd {b.get('plafond_usd')!r} != plafond d'arrêt {PLAFOND_ARRET_USD}")
    if b.get("portee_plafond") != "course" or fixe.get("generations") != 1:
        raise Refus("configuration : portée « course » et une seule génération exigées")
    etapes = {e["nom"]: e for e in b.get("etapes") or []}
    for nom in ("passe_tableau", "fusions"):
        e = etapes.get(nom) or {}
        if e.get("role") != "sacrifiable" or not e.get("plafond_relais_usd", 0) > PLAFOND_ARRET_USD or e.get("attendu_usd") != 0:
            raise Refus(f"configuration : l'étape {nom} doit être retirée par construction (sacrifiable, plafond de relais > S17, attendu 0)")
    protegees = sum(e["plafond_relais_usd"] for e in etapes.values() if e.get("role") == "protegee")
    if protegees > PLAFOND_ARRET_USD:
        raise Refus(f"configuration : somme des plafonds de relais des étapes protégées {protegees} > {PLAFOND_ARRET_USD}")
    if "etage_tests_de_mort" in fixe:
        raise Refus("configuration : pas de tests de mort dans cette course")
    if fixe.get("bisociateur", {}).get("bras") != [] or fixe.get("bisociateur", {}).get("k_paires") != 0:
        raise Refus("configuration : aucun bras du bisociateur, aucune fusion")


def acte_de_gel(prereg: dict, cl: dict, lanceur_sha: str, horodatage: str) -> str:
    return (f"# Acte de gel — course d'affinage des idées des mentors, lanceur {VERSION}\n\n"
            f"Écrit par le lanceur `{VERSION}` (sha256 {lanceur_sha}) le {horodatage}, après vérification.\n\n"
            f"- Préenregistrement : `{prereg['chemin']}`, sha256 {prereg['sha256']}, scellé.\n"
            f"- Contre-lecture : `{cl['chemin']}`, sha256 {cl['sha256']}, scellée ; verdict lu : {cl['verdict']}\n"
            "- Cet acte est la spécification servie à l'orchestrateur (`specification.preenregistrement`) ; il ne change rien au "
            "préenregistrement.\n")


# --- (8) environnement, bac à sable -------------------------------------------------------------------------------------------


def environnement_filtre(env: dict, dossier_maison: Path) -> tuple:
    retires = sorted(n for n in env if n in NOMS_DE_CLE or MOTIF_NOM_DE_CLE.search(n))
    hors_liste = sorted(n for n in env if n not in NOMS_PERMIS and n not in retires)
    garde = {n: env[n] for n in env if n in NOMS_PERMIS}
    garde["GO_ID"] = GO_ID
    garde["HOME"] = str(dossier_maison)
    garde["PYTHONPYCACHEPREFIX"] = str(dossier_maison / "pycache")
    return garde, retires, hors_liste


def sonder_bac_a_sable(r: Reglages, orchestrateur: Path, env: dict) -> dict:
    try:
        p = subprocess.run([r.python, "-I", "-B", "-c", SONDE_BAC_A_SABLE, str(orchestrateur)], cwd=str(orchestrateur), env=env,
                           capture_output=True, text=True, timeout=120)
    except (OSError, subprocess.SubprocessError) as e:
        raise Refus(f"sonde du bac à sable non exécutée ({type(e).__name__})") from None
    lignes = [x for x in p.stdout.splitlines() if x.strip()]
    try:
        etat = json.loads(lignes[-1]) if p.returncode == 0 and lignes else None
    except json.JSONDecodeError:
        etat = None
    if not (isinstance(etat, dict) and isinstance(etat.get("actif"), bool)):
        raise Refus(f"sonde du bac à sable illisible (code {p.returncode})")
    if r.exiger_bac_a_sable and not (etat["actif"] and etat.get("proc_neuf")):
        raise Refus("bac à sable inactif ou sans /proc neuf : " + str(etat.get("motif")))
    return etat


# --- (5) coût réel, écart, relevé après ---------------------------------------------------------------------------------------


def couts_reels(sortie: Path) -> dict:
    chemin = sortie / "generation-1" / "consommations.json"
    if not chemin.is_file():
        return {"lisible": False, "motif": f"{chemin} absent"}
    donnees = json.loads(chemin.read_text(encoding="utf-8")).get("consommations") or []
    par_relais, par_role, appels, coupures, inconnus = {}, {}, {}, [], {}
    for x in donnees:
        role = x.get("role")
        if role == "plafond-relais":
            continue
        if role == "coupure" or x.get("coupure"):
            coupures.append(str(x.get("etape")))
            continue
        f, role, c = str(x.get("fournisseur") or "(sans relais)"), str(role or "(sans rôle)"), float(x.get("cout_usd") or 0.0)
        par_relais[f] = round(par_relais.get(f, 0.0) + c, 6)
        par_role[role] = round(par_role.get(role, 0.0) + c, 6)
        appels[role] = appels.get(role, 0) + 1
        if x.get("cout_inconnu"):
            inconnus[f] = inconnus.get(f, 0) + 1
    return {"lisible": True, "fichier_sha256": sha256_fichier(chemin), "par_relais_usd": par_relais, "par_role_usd": par_role,
            "appels_par_role": appels, "total_usd": round(sum(par_relais.values()), 6), "coupures": coupures,
            "appels_a_cout_inconnu_par_relais": inconnus}


def devis_estimation(etiquettes_actives: list) -> float:
    """v7, mineur 4 : estimation sans marge du devis pour les espèces **actives** : 16 appels par espèce de proposeurs, et
    2 cartes × 16 cases par espèce pour l'aiguilleur et pour chacun des deux juges (prix par appel du devis v6)."""
    inconnues = [e for e in etiquettes_actives if e not in DEVIS_V5_PAR_APPEL]
    if inconnues:
        raise Refus(f"devis : espèces sans prix par appel {inconnues}")
    n = len(etiquettes_actives)
    proposeurs = sum(APPELS_PAR_PROPOSEUR * DEVIS_V5_PAR_APPEL[e] for e in etiquettes_actives)
    internes = 2 * APPELS_PAR_PROPOSEUR * n * sum(DEVIS_V5_PAR_APPEL[k] for k in ("aiguilleur", "juge-opus", "juge-argon"))
    return round(proposeurs + internes, 6)


def ecart_au_devis(couts: dict, etiquettes_actives: list) -> dict:
    if not couts.get("lisible"):
        return {"lisible": False}
    lignes = {}
    for role, n in sorted(couts["appels_par_role"].items()):
        attendu = DEVIS_V5_PAR_APPEL.get(role)
        reel = couts["par_role_usd"][role]
        lignes[role] = {"appels": n, "reel_usd": reel, "devis_usd": round(n * attendu, 6) if attendu is not None else None,
                        "ecart_usd": round(reel - n * attendu, 6) if attendu is not None else None}
    total_devis = devis_estimation(etiquettes_actives)
    return {"lisible": True, "par_role": lignes, "total_reel_usd": couts["total_usd"], "devis_estimation_sans_marge_usd": total_devis,
            "base_du_devis": {"especes_actives": list(etiquettes_actives), "nombre": len(etiquettes_actives),
                              "regle": "recalculée sur les espèces actives (v7, mineur 4)"},
            "ecart_total_usd": round(couts["total_usd"] - total_devis, 6)}


def releve_apres(credits: dict, couts: dict, cles: dict) -> tuple:
    """Reste estimé = reste avant − coût compté des relais de la clé (consommations de l'orchestrateur, au prix des fichiers ;
    à confirmer par l'interface de facturation). Alerte sous un cinquième du crédit, et pour Kimi sous ce qu'exige la course
    Kimi de la relance (11,3 / 0,9 USD). Rend (relevé, alertes)."""
    apres, alertes = {}, []
    for nom, avant in sorted(credits.items()):
        fournisseurs = [f for f, n in cles.items() if n == nom]
        depense = round(sum((couts.get("par_relais_usd") or {}).get(f, 0.0) for f in fournisseurs), 6) if couts.get("lisible") else None
        if not avant.get("lisible") or depense is None:
            apres[nom] = {"lisible": False, "depense_comptee_usd": depense, "a_relever": "par l'interface de facturation si elle le permet"}
            continue
        reste = round(avant["reste_usd"] - depense, 6)
        seuil = avant["credit_usd"] / 5.0
        if "kimi" in fournisseurs:
            seuil = max(seuil, KIMI_COURSE_SUIVANTE_PIRE_USD / KIMI_PART_DU_RESTE)
        apres[nom] = {"lisible": "estimé", "reste_estime_usd": reste, "depense_comptee_usd": depense, "seuil_usd": seuil,
                      "a_relever": "par l'interface de facturation (confirmation)"}
        if reste < seuil:
            alertes.append({"cle": nom, "reste_estime_usd": reste, "seuil_usd": seuil})
    return apres, alertes


def lire_resume_course(sortie: Path) -> dict:
    """Ce qui a été fait, sans lire aucun verdict : étapes, nœud, arrêt, cumul, nombre de cartes."""
    out = {}
    m = sortie / "generation-1" / "manifeste-fin.json"
    if m.is_file():
        d = json.loads(m.read_text(encoding="utf-8"))
        out.update(etapes=d.get("etapes"), noeud=d.get("noeud"), arret=d.get("arret"), roles_arretes=d.get("roles_arretes"),
                   exclues_a4=d.get("exclues_a4"), cumul_usd=(d.get("budget") or {}).get("cumul_usd"),
                   depassement_s17_usd=(d.get("budget") or {}).get("depassement_s17_usd"))
    f = sortie / "generation-1" / "fiches.json"
    if f.is_file():
        out["cartes_a_passeport"] = len(json.loads(f.read_text(encoding="utf-8")))
    b = sortie / "bilan-course.json"
    if b.is_file():
        out["bilan_sha256"] = sha256_fichier(b)
    return out


# --- exécution ----------------------------------------------------------------------------------------------------------------


def _depot_git(r: Reglages) -> dict:
    try:
        return {"commit": _git(r.depot, "rev-parse", "HEAD").strip(),
                "arbre_modifie": bool(_git(r.depot, "status", "--porcelain", "--untracked-files=no").strip())}
    except Refus as e:
        return {"commit": None, "erreur": str(e)}


def _versions(r: Reglages, orch: Path, env: dict) -> dict:
    p = subprocess.run([r.python, "-I", "-B", "-c", "import numpy, platform; print(numpy.__version__, platform.python_version())"],
                       cwd=str(orch), env=env, capture_output=True, text=True, timeout=60)
    morceaux = p.stdout.split()
    return {"python": morceaux[1] if len(morceaux) == 2 else None, "numpy": morceaux[0] if len(morceaux) == 2 else None,
            "executable": r.python}


def executer(r: Reglages) -> int:
    env_lu = dict(os.environ) if r.environnement is None else dict(r.environnement)
    aujourd_hui = r.aujourd_hui or _dt.datetime.now(_dt.timezone.utc).date()
    reel = r.moteur == "reel"

    verifier_course_jamais_lancee(r)
    cle_presente = bool((env_lu.get(CLE_CLAUDE) or "").strip())  # nom présent, valeur non vide ni faite d'espaces ; jamais écrite
    if reel and not cle_presente:
        raise Refus(f"variable {CLE_CLAUDE} absente ou vide dans l'environnement du lanceur : arrêt au départ ({GO_EXCEPTION_CLE})")
    commit_registre = verifier_registre_main(r) if (reel and r.verifier_go) else None
    go = go_simpl = go_cle = {"go": "sans objet (moteur simulé, aucune dépense)"}  # v11 : lus après la configuration
    lanceur_sha = sha256_fichier(r.lanceur)
    prereg = verifier_preenregistrement(r)
    cl = verifier_contre_lecture(r, prereg["sha256"], lanceur_sha)
    pieces = verifier_pieces(r)
    fixe = json.loads(Path(pieces["configuration"]["absolu"]).read_text(encoding="utf-8"))
    argon_v11 = appliquer_emplacement_argon(fixe)  # v11 : plafond de session des juges (devis v11)
    if reel and r.verifier_go:  # v11 : prolongations (GO-80, GO-124 sous confirmation) ; la confirmation est nommée en configuration
        les_go = verifier_les_go(r.registre_go, aujourd_hui, fixe)
        go, go_simpl, go_cle = dict(les_go["go"], prolongation=les_go["prolongation_course"]), les_go["simplification"], \
            dict(les_go["exception_cle"], confirmation=les_go["confirmation_107"])
    liste = json.loads(Path(pieces["liste_fils"]["absolu"]).read_text(encoding="utf-8"))
    controle_liste = verifier_liste(liste)
    decl_brute, decl_sha = lire_json_scelle(r.declaration, "déclaration des relais")
    decl = verifier_declaration(decl_brute, fixe, r)
    plafond_luc = verifier_plafond_luc(fixe)
    google = (r.controler_google or controler_chemins_google)(r, decl, pieces, fixe, liste)
    non_conformes = {n: [p for x in v["roles"] for p in x["problemes"]] for n, v in google.items()
                     if isinstance(v, dict) and v.get("conforme") is False}
    if non_conformes:
        if reel:
            raise Refus("garde des appels à Google (règle gelée, GO-2026-11-21-71) : " + json.dumps(non_conformes, ensure_ascii=False)
                        + " — retirer l'espèce de la déclaration (motif dans « absences ») ou lui donner un chemin conforme")
        print(json.dumps({"avertissement_garde_google": non_conformes, "moteur": "simulé : refus en moteur réel"},
                         ensure_ascii=False), file=sys.stderr)
        google["refus_en_moteur_reel"] = sorted(non_conformes)
    palier_astra = verifier_palier_astra(pieces, liste) if "astra" in decl["fournisseurs"] else {"astra": "non déclarée"}
    releve_brut, releve_sha = lire_json_scelle(r.releve, "relevé des crédits")
    horodatage = r.horodatage()
    ident = _dt.datetime.now(_dt.timezone.utc).strftime("%Y%m%d-%H%M%S-%f") + SUFFIXE_RUN  # 1 : unique à la microseconde
    dossier_run = r.dossier_runs / ident
    parts = parts_au_pire(fixe, liste, pieces, decl)
    reglages_carbon = controler_pire_cas_carbon(decl, fixe, liste, pieces)  # v8 : chaque appel peut partir, pire cas écrit
    reglages_argon = controler_pire_cas_argon(decl, fixe, liste, pieces)  # v11 : Argon sous la garde Google
    autres_courses = verifier_autres_courses(r, releve_brut)  # v7, majeur 2
    credits = verifier_credits(releve_brut, decl["cles"], aujourd_hui,
                               r.dossier_runs / (ident.replace(SUFFIXE_RUN, "") + "-alerte-credits-affinage-mentors-v11"), parts)
    # v11 : le relais Claude doit être lancé au plafond de la part Claude, calculé sur le relevé (le relevé précède le relais)
    parts["claude"] = dict(parts.get("claude") or {}, plafond_relais_exige_usd=plafond_luc)  # GO-124 : 45 USD exactement
    verifier_confidentialite({n: Path(pieces[n]["absolu"]).read_text(encoding="utf-8") for n in PIECES_SERVIES})
    procedure = verifier_procedure_relais(r, decl, pieces, fixe, parts) if reel else {"exigee": False, "motif": "moteur simulé : aucun relais réel"}
    sonde = verifier_sonde_astra(r, decl, aujourd_hui) if reel else {"exige": False, "motif": "moteur simulé"}
    prix = verifier_releve_prix(r.releve_prix, fixe, aujourd_hui) if reel else {"exige": False, "motif": "moteur simulé"}
    orch = verifier_orchestrateur(r)
    orch_dir = Path(orch["chemin"])

    dossier_sortie = r.dossier_sorties / ident
    sortie = dossier_sortie / "sortie"
    prepa = r.dossier_sorties / (ident + "-preparation")  # 1 : hors dépôt ; runs/<id> n'est créé qu'après la porte à blanc
    if dossier_run.exists() or dossier_sortie.exists() or prepa.exists():
        raise Refus(f"{dossier_run}, {dossier_sortie} ou {prepa} existe déjà (R12)")
    env, retires, hors_liste = environnement_filtre(env_lu, dossier_sortie)
    bac = sonder_bac_a_sable(r, orch_dir, env) if reel else {"exige": False, "motif": "moteur simulé : aucun agent réel"}

    prepa.mkdir(parents=True)
    dossier_arrets = dossier_sortie / "arrets-credit"  # v5, constat 1 : créé seulement après la porte à blanc
    decl = envelopper_commandes(decl, r.python, Path(pieces["garde_credit"]["absolu"]), dossier_arrets)
    h_acte = ecrire_scelle(prepa / "acte-de-gel.md", acte_de_gel(prereg, cl, lanceur_sha, horodatage))
    spec = {"preenregistrement": {"chemin": str(prepa / "acte-de-gel.md"), "sha256": h_acte},
            "contre_lecture": {"chemin": cl["chemin"], "sha256": cl["sha256"]}}
    conf = assembler_configuration(fixe, liste, pieces, decl, spec)
    chemin_conf = prepa / "configuration-orchestrateur.json"
    expurgations = conf.pop("_expurgations")
    h_conf = ecrire_scelle(chemin_conf, conf)
    base = [r.python, "-I", "-B", LANCEUR_ORCHESTRATEUR, "--course-2", str(chemin_conf), str(sortie), "--generations", "1"]
    registre = ecrire_registre_derive(r.registre_go, prepa / "registre-go-derive.md", commit=commit_registre) if reel else {"motif": "moteur simulé"}
    moteur = ["--moteur", "reel", "--confirmer-moteur-reel", "--registre-go", registre["derive"]] if reel else ["--moteur", "simule"]
    verif = subprocess.run(base + ["--verifier-seulement"] + (moteur if reel else []),
                           cwd=str(orch_dir), env=env, capture_output=True, text=True, timeout=600)
    try:
        verif_json = json.loads(verif.stdout) if verif.returncode == 0 else None
    except ValueError:
        verif_json = None
    if verif_json is None or verif_json.get("montant_requis_go_usd") != PLAFOND_ARRET_USD:
        raise Refus(f"vérification de l'orchestrateur refusée (code {verif.returncode}) : "
                    f"{(verif.stderr or verif.stdout).strip()[-800:]!r}")
    if verif_json.get("specification", {}).get("conforme") is not True:
        raise Refus(f"spécification refusée par l'orchestrateur : {verif_json.get('specification')}")
    portes = porte_a_blanc(decl) if reel else {"exige": False, "motif": "moteur simulé : portes tenues par le noyau"}
    dossier_run.mkdir(parents=True)  # 1 : seulement après la porte à blanc
    for f in sorted(prepa.iterdir()):  # copie au dépôt, pour mémoire ; l'orchestrateur lit les pièces de la préparation
        shutil.copy2(f, dossier_run / f.name)
    dossier_sortie.mkdir(parents=True)
    dossier_arrets.mkdir()
    argv = base + moteur
    etiquettes_actives = [e["etiquette"] for e in decl["especes_actives"]]
    depart = {
        "lanceur": {"version": VERSION, "chemin": str(r.lanceur), "sha256": lanceur_sha}, "moteur": r.moteur,
        "horodatage_canonique": horodatage, "id": ident, "go": go, "plafond_arret_usd": PLAFOND_ARRET_USD,
        "preenregistrement": prereg, "contre_lecture": cl, "acte_de_gel_sha256": h_acte, "pieces": pieces,
        "liste_fils": controle_liste, "declaration_relais": {"chemin": str(r.declaration), "sha256": decl_sha},
        "especes_actives": [e["etiquette"] for e in decl["especes_actives"]], "especes_absentes": decl["especes_absentes"],
        "carbon": decl["carbon"], "cles_employees": decl["cles"], "go_exception_cle": go_cle, "go_simplification_cle": go_simpl, "garde_google": google,
        "palier_astra": palier_astra,
        "cle_par_espece": {e["etiquette"]: decl["cles"][e["fournisseur"]] for e in decl["especes_actives"]},
        "cle_par_role_interne": {"aiguilleur": decl["cles"][fixe["aiguilleur"]["fournisseur"]],
                                 **{j["etiquette"]: decl["cles"][j["fournisseur"]] for j in fixe["juges"]}},
        "parts_au_pire": parts, "procedure_relais_persistants": procedure, "porte_a_blanc": portes,
        "registre_go_derive": registre, "releve_prix_claude": prix, "sonde_astra": sonde, "preparation": str(prepa),
        "kimi_autorise_par_la_mere": decl.get("kimi_autorise_par_la_mere"),
        "compter_limite_de_debit_comme_soupcon": decl.get("compter_limite_de_debit_comme_soupcon", True),
        "confidentialite": {"regle": "R-3273", "expurgations": expurgations, "textes_verifies": list(PIECES_SERVIES) + ["16 fils"]}, "dossier_arrets_credit": str(dossier_arrets),
        "cle_claude": {"nom": CLE_CLAUDE, "presente_dans_l_environnement_du_lanceur": cle_presente, "valeur": "jamais lue",
                       "cles_exclues": list(CLES_INTERDITES), "exception": GO_EXCEPTION_CLE,
                       "regle": "GO-2026-11-22-124", "plafond_propre_usd": plafond_luc,
                       "part_estimee_usd": PART_CLAUDE_ESTIMEE_USD,
                       "surveillance": ("au fil de l'eau, toutes les " + str(r.intervalle_surveillance_s) + " s") if reel else "moteur simulé : aucune",
                       "plafond_part_claude_usd": plafond_luc},
        "argon_v11": argon_v11, "reglages_argon_v11_flux": reglages_argon,
        "releve_credits_avant": {"chemin": str(r.releve), "sha256": releve_sha, "cles": credits},
        "orchestrateur": orch, "configuration": {"chemin": str(chemin_conf), "sha256": h_conf},
        "verification_orchestrateur": {k: verif_json.get(k) for k in ("configuration_sha256", "montant_requis_go_usd",
                                                                      "specification", "go", "generations")},
        "commande": argv, "cwd": str(orch_dir), "sortie": str(sortie), "bac_a_sable": bac,
        "environnement": {"noms_retires": retires, "noms_exclus": hors_liste, "valeurs": "jamais lues"},
        "graines": {"racine": conf["racine_graines"], "prefixe": conf["graines"]["prefixe"],
                    "regle": "numpy.random.SeedSequence(racine, spawn_key=(cle_de_tache(tache),)) dans l'orchestrateur (R9)"},
        "versions": _versions(r, orch_dir, env), "depot_travail": _depot_git(r),
        "devis_estimation_sans_marge_usd": devis_estimation(etiquettes_actives),
        "base_du_devis": {"especes_actives": etiquettes_actives, "regle": "recalculée sur les espèces actives (v7, mineur 4)"},
        "autres_courses_de_l_organisme": autres_courses,
        "reglages_carbon_v11_flux": reglages_carbon if reglages_carbon is not None else {"carbon": "non active"},
        "codes_de_sortie": {"0": "course finie", "2": "refus avant le départ", "3": "alerte de crédit avant le départ",
                            "4": "cumul au-dessus de 150 USD", "5": "arrêt par la garde de crédit",
                            "6": "course partie : orchestrateur à code non nul ou erreur du lanceur après le départ",
                            "5 (v11)": "ou arrêt propre sur la part Claude : premier refus de l'interface (4xx sauf 429) ou du "
                                       "relais (402, plafond de 45 USD), part engagée au plafond, état ou journal illisible "
                                       "(alerte-arret-part-claude.json)"},
        "journaux": {"stdout": str(dossier_sortie / "course.stdout.txt"), "stderr": str(dossier_sortie / "course.stderr.txt")},
    }
    h_depart = ecrire_scelle(dossier_run / "manifeste-lanceur-depart.json", depart)
    print(json.dumps({"manifeste_depart": str(dossier_run / "manifeste-lanceur-depart.json"), "sha256": h_depart}, ensure_ascii=False),
          flush=True)

    code, pid, echec, arret_credit = None, None, None, []
    surveillance, arret_luc = None, None
    if reel:
        journal_claude = ((procedure.get("relais_vivants") or {}).get("claude") or {}).get("journal")
        surveillance = SurveillanceCleClaude(r, decl["fournisseurs"]["claude"]["url_relais"], plafond_luc, journal_claude,
                                             journal_run=dossier_run / JOURNAL_PART_CLAUDE)
    debut = _dt.datetime.now(_dt.timezone.utc)
    try:
        with open(dossier_sortie / "course.stdout.txt", "xb") as fo, open(dossier_sortie / "course.stderr.txt", "xb") as fe:
            enfant = subprocess.Popen(argv, cwd=str(orch_dir), env=env, stdout=fo, stderr=fe)
            pid = enfant.pid

            def relayer(num, _cadre):
                try:
                    enfant.send_signal(num)
                except ProcessLookupError:
                    pass
            anciens = {s: signal.signal(s, relayer) for s in (signal.SIGTERM, signal.SIGINT, signal.SIGHUP)}
            try:
                prochaine = 0.0
                while True:
                    if surveillance is not None and arret_luc is None and time.monotonic() >= prochaine:
                        prochaine = time.monotonic() + float(r.intervalle_surveillance_s)
                        arret_luc = surveillance.depasse()
                        if arret_luc:  # R-4995 et GO-2026-11-22-111 : arrêt propre par PID (R10), message écrit, jamais muet
                            print(json.dumps({"arret_cle_claude": arret_luc, "pid": enfant.pid}, ensure_ascii=False),
                                  file=sys.stderr, flush=True)
                            try:
                                enfant.send_signal(signal.SIGTERM)
                            except ProcessLookupError:
                                pass
                    try:
                        code = enfant.wait(timeout=min(1.0, float(r.intervalle_surveillance_s)))
                        break
                    except subprocess.TimeoutExpired:
                        if not arret_credit and any(dossier_arrets.glob("arret-credit-*.json")):
                            arret_credit = sorted(x.name for x in dossier_arrets.glob("arret-credit-*.json"))
                            enfant.send_signal(signal.SIGTERM)  # R-3237 : arrêt au premier refus pour crédit (par PID, R10)
            finally:
                for s, a in anciens.items():
                    signal.signal(s, a)
    except BaseException as exc:  # noqa: BLE001 — le manifeste de fin est écrit sur tout chemin
        echec = f"{type(exc).__name__}: {exc}"
    if surveillance is not None and arret_luc is None:  # v11c, constat 5 : relecture finale, après l'arrêt de l'orchestrateur
        try:
            arret_luc = surveillance.lecture_finale()
        except Exception as exc:  # noqa: BLE001 — jamais tu
            arret_luc = {"code": 5, "nature": "relecture finale impossible", "statut": None,
                         "cause": f"{type(exc).__name__}: {exc}", "motif": f"relecture finale du relais Claude impossible ({type(exc).__name__})"}
        if arret_luc:
            arret_luc = dict(arret_luc, moment="relecture finale, après l'arrêt de l'orchestrateur")
            print(json.dumps({"arret_cle_claude": arret_luc, "pid": pid}, ensure_ascii=False), file=sys.stderr, flush=True)
    journal_part = surveillance.sceller_journal() if surveillance is not None else None
    fin = _dt.datetime.now(_dt.timezone.utc)
    bilan = {"id": ident, "manifeste_depart_sha256": h_depart, "pid_orchestrateur": pid, "code": code, "echec_lanceur": echec,
             "debut_utc": debut.isoformat(), "fin_utc": fin.isoformat(),
             "arret_au_premier_refus_pour_credit": [json.loads(x.read_text(encoding="utf-8"))
                                                    for x in sorted(dossier_arrets.glob("arret-credit-*.json"))],
             "soupcons_de_refus_pour_credit": [json.loads(x.read_text(encoding="utf-8"))
                                               for x in sorted(dossier_arrets.glob("soupcon-credit-*.json"))],
             "cle_claude_au_fil_de_l_eau": dict(surveillance.bilan(), arret=arret_luc, journal_du_run=journal_part)
             if surveillance else {"moteur": "simulé"}}
    alertes_apres, depasse = [], False
    try:
        couts = couts_reels(sortie)
        cumul = (lire_resume_course(sortie).get("cumul_usd") or 0.0)
        apres, alertes_apres = releve_apres(credits, couts, decl["cles"])
        depasse = bool(couts.get("lisible") and couts["total_usd"] > PLAFOND_ARRET_USD + 1e-9) or cumul > PLAFOND_ARRET_USD + 1e-9
        bilan.update({"ce_qui_a_ete_fait": lire_resume_course(sortie), "cout_reel": couts,
                      "ecart_au_devis": ecart_au_devis(couts, etiquettes_actives),
                      "plafond_arret": {"usd": PLAFOND_ARRET_USD, "depasse": depasse},
                      "releve_credits_apres": apres, "alertes_apres": alertes_apres})
    except Exception as exc:  # noqa: BLE001 — le manifeste de fin est écrit quand même, l'erreur y est dite
        bilan["erreur_bilan"] = f"{type(exc).__name__}: {exc}"
        echec = echec or bilan["erreur_bilan"]
    bilan["journaux_sha256"] = {n: sha256_fichier(dossier_sortie / n) for n in ("course.stdout.txt", "course.stderr.txt")
                                if (dossier_sortie / n).is_file()}
    if bilan.get("arret_au_premier_refus_pour_credit"):
        ecrire_scelle(dossier_run / "alerte-arret-credit.json",
                      {"alerte": "course arrêtée par la garde de crédit (refus pour crédit, ou deuxième soupçon du même relais ; R-3237)",
                       "relais": bilan["arret_au_premier_refus_pour_credit"], "pour": "la mère, qui prévient Lazar"})
    if arret_luc:
        ecrire_scelle(dossier_run / "alerte-arret-part-claude.json",
                      {"alerte": f"course arrêtée proprement sur la part Claude ({CLE_CLAUDE}) : {arret_luc.get('nature')} ; "
                                 "sans relance",
                       "nature": arret_luc.get("nature"), "statut": arret_luc.get("statut"), "cause": arret_luc.get("cause"),
                       "moment": arret_luc.get("moment", "au fil de l'eau"),
                       "code": arret_luc["code"], "motif": arret_luc["motif"], "bilan": surveillance.bilan(),
                       "relance": "aucune (une relance est une nouvelle version et un mot de la mère)",
                       "pour": "la mère, qui prévient Lazar"})
    if alertes_apres or depasse:
        ecrire_scelle(dossier_run / "alerte-credits-apres.json",
                      {"alerte": "après la course : reste estimé sous le seuil ou plafond d'arrêt dépassé", "cles": alertes_apres,
                       "plafond_depasse": bool(depasse), "pour": "la mère (à transmettre à Lazar avant qu'une clé n'atteigne zéro)"})
    sortie_lanceur = code_de_sortie(depasse, bool(bilan.get("arret_au_premier_refus_pour_credit")), echec, code,
                                    arret_luc["code"] if arret_luc else None)
    bilan["code_orchestrateur"] = code
    bilan["code_du_lanceur"] = sortie_lanceur
    h_fin = ecrire_scelle(dossier_run / "manifeste-lanceur-fin.json", bilan)
    print(json.dumps({"manifeste_fin": str(dossier_run / "manifeste-lanceur-fin.json"), "sha256": h_fin, "code": code,
                      "code_du_lanceur": sortie_lanceur, "cout_reel_usd": (bilan.get("cout_reel") or {}).get("total_usd"),
                      "alertes_apres": alertes_apres}, ensure_ascii=False), flush=True)
    if echec:
        print(json.dumps({"erreur_apres_depart": echec}, ensure_ascii=False), file=sys.stderr)
    return sortie_lanceur


def code_de_sortie(depasse: bool, arret_credit: bool, echec, code_orchestrateur, arret_luc: int | None = None) -> int:
    """v7, mineur 5 : codes du lanceur distincts de ceux de l'orchestrateur. 4 (plafond) prime, puis 5 (garde de crédit) ;
    toute autre issue non nette d'une course partie — code non nul ou absent de l'orchestrateur, signal, erreur du lanceur
    après le manifeste de départ — rend 6 (le vrai code est au manifeste de fin) ; 0 seulement pour un code 0 sans erreur."""
    if depasse:
        return 4
    if arret_luc == 5:  # v11 : arrêt propre au premier refus de l'interface (4xx sauf 429) ou du relais Claude (402)
        return 5
    if arret_credit:
        return 5
    if echec or code_orchestrateur != 0:
        return 6
    return 0


# --- essai à blanc ------------------------------------------------------------------------------------------------------------


CHEMINS_MAIN_COMMANDES = {
    "astra": "docs/notes/ideation-organisme-v1/relais-kimi-v1/commande_astra_v1.py"}  # v11 : Carbon par la commande du dépôt


def extraire_de_main(depot: Path, chemin: str, attendu: str, destination: Path) -> Path:
    """Extraction hors dépôt, depuis `origin/main` (récupérée avant par un `git fetch` ciblé), vérifiée à son empreinte."""
    p = subprocess.run(["git", "-C", str(depot), "show", "origin/main:" + chemin], capture_output=True, timeout=60)
    if p.returncode != 0 or hashlib.sha256(p.stdout).hexdigest() != attendu:
        raise Refus(f"extraction de {chemin} depuis origin/main : absente ou d'une autre empreinte que {attendu[:12]}…")
    if destination.exists():
        raise Refus(f"{destination} existe déjà (R12)")
    destination.write_bytes(p.stdout)
    return destination


def reglages_a_blanc(dossier: Path) -> Reglages:
    """Moteur simulé, relais factices (adresses locales sans serveur, portes « commande » factices jamais appelées par le moteur
    simulé), contre-lecture et relevé d'essai écrits dans le dossier, aucun GO. Rien n'est lu dans `registres/`."""
    if dossier.exists():
        raise Refus(f"{dossier} existe déjà (R12)")
    dossier.mkdir(parents=True)
    essai = dossier / "pieces-d-essai"
    essai.mkdir()
    r = Reglages.production()
    lanceur_sha = sha256_fichier(r.lanceur)
    prereg_sha = r.prereg[1] if re.fullmatch(r"[0-9a-f]{64}", r.prereg[1]) else sha256_fichier(r.prereg[0])
    cl = essai / "contre-lecture-d-essai.md"
    ecrire_scelle(cl, f"# Contre-lecture d'ESSAI, {LIBELLE_CONTRE_LECTURE} (aucune valeur réelle)\n\nPréenregistrement lu : {prereg_sha}\n"
                      f"Lanceur lu : {lanceur_sha}\n\n## Verdict\n\nScellable.\n\nEssai à blanc seulement.\n")
    porte = ["/bin/false"]
    cmd = {n: extraire_de_main(r.depot, CHEMINS_MAIN_COMMANDES[n], next(iter(COMMANDES_EPINGLEES[n].values())),
                               essai / os.path.basename(CHEMINS_MAIN_COMMANDES[n])) for n in ("astra",)}
    cmd["carbon"] = r.depot / PIECES["commande_carbon"][0]
    decl = {"version": "declaration-relais-essai-a-blanc", "fournisseurs": {
        "carbon": {"type": "commande_externe", "commande": [sys.executable, "-I", "-B", str(cmd["carbon"])] + ARGUMENTS_COMMANDES["carbon"],
                   "modele_propose": "gemini-4-carbon", "nom_cle": "CLE_FACTICE_ARGON", "inscription": INSCRIPTION_CARBON,  # 7 : clé partagée
                   "porte_plafond": {"type": "environnement"}},
        "astra": {"type": "commande_externe", "commande": [sys.executable, "-I", "-B", str(cmd["astra"])] + ARGUMENTS_COMMANDES["astra"],
                  "modele_propose": "gpt-6.2-astra", "nom_cle": CLE_ASTRA, "porte_plafond": {"type": "environnement"}},
        "claude": {"type": "claude_sdk", "url_relais": "http://127.0.0.1:18999", "nom_cle": CLE_CLAUDE,
                   "porte_plafond": {"type": "commande", "commande": porte, "delai_s": 5}},
        "argon": {"type": "commande_externe", "commande": [sys.executable, "-I", "-B", str(cmd["carbon"])] + ARGUMENTS_COMMANDES["argon"],
                  "nom_cle": "CLE_FACTICE_ARGON", "porte_plafond": {"type": "environnement"}}}}
    chemin_decl = essai / "declaration-relais-d-essai.json"
    ecrire_scelle(chemin_decl, decl)
    maintenant = _dt.datetime.now(_dt.timezone.utc)
    releve = {"version": "releve-credits-essai-a-blanc", "releve_utc": maintenant.strftime("%Y-%m-%dT%H:%M:%SZ"),
              "note": "essai à blanc : aucune valeur réelle",
              "cles": dict({n: {"non_lisible": True, "motif": "essai à blanc : solde illisible, sous dispense"}
                            for n in ("CLE_FACTICE_ARGON", CLE_ASTRA)},
                           **{CLE_CLAUDE: {"solde_non_lu": True, "reference": REFERENCE_LUC_SANS_SOLDE,  # v11d, R1
                                           "source": "essai à blanc"}}),
              "dispense": {"par": "mère", "reference": REFERENCE_DISPENSE,
                           "cles": ["CLE_FACTICE_ARGON", CLE_ASTRA]}}
    chemin_releve = essai / "releve-credits-d-essai.json"
    ecrire_scelle(chemin_releve, releve)
    r.prereg = (r.prereg[0], prereg_sha)
    r.contre_lecture, r.declaration, r.releve = cl, chemin_decl, chemin_releve
    r.dossier_runs, r.dossier_sorties = dossier / "runs", dossier / "sorties"
    r.moteur, r.exiger_bac_a_sable, r.verifier_go = "simule", False, False
    r.ref_registre = None
    return r


def principal(argv: list | None = None, reglages: Reglages | None = None) -> int:
    argv = sys.argv[1:] if argv is None else list(argv)
    try:
        if argv and argv[0] == "--a-blanc" and len(argv) == 2:
            reglages = reglages or reglages_a_blanc(Path(argv[1]).resolve())
        elif argv:
            print(json.dumps({"refus": f"arguments non admis (reçu {argv!r}) ; seul « --a-blanc DOSSIER »"}, ensure_ascii=False),
                  file=sys.stderr)
            return 2
        return executer(reglages or Reglages.production())
    except AlerteCredit as e:
        print(json.dumps({"alerte_credit": str(e)}, ensure_ascii=False), file=sys.stderr)
        return 3
    except Refus as e:
        print(json.dumps({"refus": str(e)}, ensure_ascii=False), file=sys.stderr)
        return 2
    except Exception as e:  # noqa: BLE001
        print(json.dumps({"erreur": f"{type(e).__name__}: {e}"}, ensure_ascii=False), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(principal())
