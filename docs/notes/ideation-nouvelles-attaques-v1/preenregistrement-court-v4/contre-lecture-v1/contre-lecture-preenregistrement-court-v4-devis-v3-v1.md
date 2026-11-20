# Contre-lecture — préenregistrement court v4 et devis v3 de la course « nouvelles attaques » à six espèces — v1

- Contre-lecteur neuf, modèle O. Je n'ai écrit aucune version du préenregistrement court, du devis, de l'ordre de course, ni leurs contrôles. Pièce de travail (classe C) au service de pièces décisives (classe A), sur GO-2026-11-20-33, règle R2. Écrit le 2026-11-20 ; relevé de `date -u` : 10:25:37Z, avant l'écriture de ce rapport.
- Mandat : `docs/notes/ideation-nouvelles-attaques-v1/preenregistrement-court-v4/mandat-contre-lecteur-preenregistrement-court-v4-devis-v3-v1.md` (`01f9e05774d89b9b741e89c5f691427f30b9a6b15564342cfcbd5bf07b04e797`, égal à son compagnon).
- Processeur seul. Aucun appel à un fournisseur de modèles, aucune dépense, aucun lancement du relais, du véhicule ni de la sonde, aucune écriture dans le dépôt, aucun commit. Réseau : un `git fetch origin main` (commit `fbaf53190e8088cd0d68fb37b19a577db64fd573`). Une vérification de présence par le nom seulement, `[ -n "${KIMI_API_KEY:-}" ]`, code 0 ; aucune valeur lue. **Aucun refus de permission, de classifieur ni de garde.**

## Verdict

**À corriger**, puis conforme. Neuf corrections de lettre : quatre au préenregistrement (K1 à K4), cinq au devis (K5 à K9). **Aucune ne change un total, un seuil, un arrêt ni une décision.** Le rejeu de l'outil est égal à l'octet. Les totaux qui décident, refaits par un programme indépendant, sont égaux au centime à ceux du rédacteur. Le validateur ne rend que le problème attendu. La sonde de l'espèce 6 ne contient aucun contenu d'attaque, aucune recette, aucune invite opérante.

## 0. Pièces vérifiées (empreinte égale au compagnon, `env -C DOSSIER sha256sum -c`)

Dossier N = `docs/notes/ideation-nouvelles-attaques-v1/`, dossier V = `N/preenregistrement-court-v4/`.

| pièce | empreinte |
|---|---|
| V/mandat du rédacteur | `4fa56789…` (OK) |
| V/`preenregistrement-court-course-nouvelles-attaques-v4.md` | `2dabdadf9ac126ee8d931dfde3e3507a3183b50b8f584d0f817e7ebf8adf2b10` |
| V/`devis-course-nouvelles-attaques-v3.md` | `bf7b4ba3ede3ba73c8ee4e1a3548b6b0d52975df717b98ca4af44a6c503c142a` |
| V/ deux JSON de remplacements, deux journaux de l'outil, deux différentiels | OK chacun |
| V/`calcul_devis_course_nouvelles_attaques_v3.py` ; sa sortie | `a50c9983…` ; `fa4bc8b0…` |
| V/`valider_prereg_v4_v1.py` ; V/rapport du rédacteur | `63a1c0bc…` ; `36b8d1e2…` |
| `N/preenregistrement-court-v3/` : la v3 ; son contrôle | `2ea5ad53…` ; `5039197f…` |
| `N/conception-v2/` : devis v2 ; programme v2 ; sa sortie | `714e4fc6…` ; `cefe9783…` ; `ffecbd11…` |
| `N/conception-v3/question-course-nouvelles-attaques-v3.md` (taille seulement, `wc -c` : 10 562 octets) | `2cf2aae0…` |
| `scripts/remplacer_texte_exact_v1.py` (recalculée) | `391db990734dd36f7c827b8b6c77dc0de1bda324f671b65748ccfe68c56a53d6` |
| S3, devis v2i (pour la phrase « de 120 à 150 USD », § 9 du devis v3 : vérifiée, ligne 4 de S3) | `a8c033cd…` |

Registres : `registres/go.md` est identique à `fbaf5319` et au commit du rédacteur `da0d389c` (`21f8f184…` des deux côtés). `registres/decisions.md` a grandi depuis `da0d389c` (`47ed2a0b…` alors, `ee0eafe6…` à `fbaf5319`) : R-4175 à R-4187, lues pour ce qui touche la course (§ 6, points 13 et 14). Les lignes demandées sont lues à la lettre : GO-2026-11-20-08, -10, -16, -20, -22, -31, -32, -33, -34 ; R-813, R-1780, R-4117, R-4125, R-4169, R-4170, R-4174.

## 1. Rejeu de l'outil et différentiels

- v3 → v4 : « FAIT : 46 remplacement(s) », cible `2ea5ad53…`, sortie `2dabdadf…` ; `cmp` avec la v4 rendue : égal.
- devis v2 → v3 : « FAIT : 17 remplacement(s) », cible `714e4fc6…`, sortie `bf7b4ba3…` ; `cmp` : égal.
- Les deux différentiels refaits par `diff -u` ne diffèrent des différentiels rendus que par la ligne 2 (chemin et heure du fichier neuf).

## 2. Fidélité à GO-2026-11-20-33

- GO-33, lu à la lettre (je ne recopie pas le nom de l'espèce) : une sixième espèce entre, « option (a) de la mère » ; « version neuve du préenregistrement court et du devis » ; sa clé et sa part « s'y écrivent » ; « rien ne court avant le mot de Lazar sur le devis neuf ». La v4 porte six espèces, la sixième par son numéro, proposeur seul, et « rien ne court » (statut, seuil, point 11). Le rôle « proposeur » vient de l'option (a) de la mère et du mandat du rédacteur, pas de la lettre de la ligne : je le constate, sans réserve.
- Rien d'autre ne change que ce que le nombre d'espèces entraîne, **hors GO-2026-11-20-34** (recharge de Rigaud), porté sur la note de la mère et déclaré (remarque 7). Je le tiens pour légitime : GO-34 vise nommément « le devis v3 » ; laisser la v3 dire « sans recharge » sur Rigaud contredirait la ligne. Mais la v4 ne l'a porté qu'à moitié : trois phrases de méthode disent encore les soldes « jamais lus » (K1, K2, K4), et la manière de relire le solde n'est écrite nulle part comme valeur ouverte (K3).
- Chaque « inchangé » de la table « un par un » est vrai, contrôlé contre la v3 : onze cases par génération, trente-trois servies, vingt tenues à l'écart, soixante-sept en réserve (une case par génération, chaque espèce la reçoit) ; graines et clés de tirage ; C1 ; borne de 60 fiches (la part non lue peut croître, c'est dit) ; garde du coffre (une part) ; définitions de M1 à M5 et I1 ; forme du registre ; règle du lecteur d'antériorité ; juges et aiguilleur. « Les deux autres relais » de la dispense de lecture de solde reste juste : le quatrième a sa propre ligne de valeur ouverte.

## 3. Le devis : totaux refaits indépendamment

Mon programme, `recalcul_contre_lecteur_devis_v3_v1.py` (arithmétique exacte par fractions, sans reprendre le code du rédacteur ; énumération propre des répartitions), sortie `recalcul-contre-lecteur-devis-v3-v1.json`, joué deux fois, sorties égales à l'octet (`cmp`). Le programme du rédacteur, rejoué : sortie égale à l'octet à `fa4bc8b0…`.

| total (USD) | rédacteur | moi |
|---|---|---|
| par génération, bas / haut / plafond (règle de marge ; règle des juges) | 87,01 / 180,88 / 190 (190 ; 155) | 87,01 / 180,88 / 190 (190 ; 155) |
| seuils : proposition, aiguillage, juges | 180, 175, 160 | 180, 175, 160 ; au cas haut, tout est lancé (reste pour les juges 65,90 ≥ 56,78) |
| course, bas / haut / **ligne** | 261,04 / 542,65 / **570** | 261,04 / 542,65 / **570** |
| total, attendu / haut / **plafond total** | 262,23 / 548,66 / **576,01** | 262,23 / 548,66 / **576,01** |
| écarts à cinq espèces : attendu / haut / plafond | 43,51 / 129,23 / 120,01 | 43,51 / 129,23 / 120,01 |
| espèce 6 sur la course, bas / haut / pire | 35,19 / 88,55 / 199,65 | 35,19 / 88,55 / 199,65 |
| par espèce (bas ; haut) : 1, 2, 3, 4, 5, 6, aiguilleur | 21,19 ; 59,23 — 14,25 ; 17,01 — 46,99 ; 152,68 — 52,74 ; 62,97 — 74,16 ; 88,55 — 35,19 ; 88,55 — 16,52 ; 73,66 | identiques |
| par clé (bas ; haut) : Minuit, Luc, Rigaud, relais 2, relais 3, clé de l'espèce 6 | 24,70 ; 126,06 — 69,26 ; 136,63 — 22,29 ; 26,61 — 95,35 ; 147,77 — 14,25 ; 17,01 — 35,19 ; 88,55 | identiques |
| rôles Claude, bas / haut (contrôle à cinq) | 116,25 / 289,31 (256,02) | 116,25 / 289,31 (256,02) |
| variante à 450 : ligne / plafond total / marge sur le bas | 450 / 456,01 / 1,72 | 450 / 456,01 / 1,72 |
| borne 415,21 sur le cas haut Claude, six (cinq) | 1,435 (1,622) | 1,435 (1,622) |
| ligne moins borne, six (cinq) ; manque « au moins » sans X | 154,79 (34,79) ; 146,44 | 154,79 (34,79) ; 146,44 |
| Rigaud : solde minimal pour le haut de son rôle ; pour son pire | 34,96 ; 208,00 | 34,96 ; 208,00 |
| « de l'ordre de 151 » (recommandation du § 9) | 151,36 (lignes arrondies) | 151,37 (exact) |

**Les trois règles de coût de l'espèce 6.** Jugées acceptables, et dites pour ce qu'elles sont. Le bas (moyenne des cinq) est une hypothèse neutre ; le haut (le plus cher des cinq, fois 1,1940) évite qu'un plafond repose sur une espèce supposée bon marché ; le pire (onze appels à 6,05) aligne sa clé sur le troisième relais. Le plafond de génération de 190 USD ne dépend que du haut ; si l'espèce 6 coûtait plus que le plus cher des cinq, le cas haut le dirait faux, et l'arrêt n° 6 tiendrait.

**6,05 USD de pire par appel.** Au repère de tarif (R-813 : « 2 / 10 USD par million de jetons », vérifié par le registre le 30 octobre ; R-1780 : « 2/10/2 par million », troisième chiffre non expliqué, sans doute un tarif d'entrée en cache), 6,05 USD valent 605 000 jetons de sortie, ou environ trois millions de jetons d'entrée. C'est une borne haute très large d'un appel, pas une estimation : elle tient tant que la sortie maximale de la configuration et la borne en octets de la consigne restent loin de ces ordres. Le texte la garde en valeur ouverte, à confirmer au complément : juste. Au même repère, le bas vaut 1,0664 USD par appel, soit de l'ordre de 100 000 jetons de sortie : il est sans doute large, comme le dit le rédacteur.

**Le tarif du registre change-t-il un total ?** Non pour la ligne, le plafond total, les seuils et les parts : aucun n'en dépend. Il ne toucherait que l'estimation de la sonde de l'espèce 6 dans l'attendu : comptée à un jeton par octet de la question, elle vaudrait 0,0211 USD au lieu de 0,0017, et l'attendu passerait de 262,23 à 262,25 USD. Sans effet sur une décision ; je ne le corrige pas.

## 4. GO-2026-11-20-22 et GO-2026-11-20-34 ; la clé la plus serrée

- **Répartition** (GO-22 : juge de l'espèce 3 sur Minuit ; aiguilleur et espèce 4 sur Luc ; espèce 3 sur Rigaud) : inchangée, et chaque clé tient encore le cas haut de ses rôles. Rejouée à six espèces aux parts d'avant la recharge : neuf répartitions admissibles ; meilleur plus petit rapport 1,2895, atteint par la répartition retenue, à égalité avec celle qui met aussi le proposeur de l'espèce 3 sur Luc. Égal au rédacteur.
- **La clé la plus serrée.** En rapport part sur cas haut, Minuit : 1,290 (Luc 1,566 ; Rigaud 1,452). En USD au cas haut, avant la recharge, Rigaud : marge de 12,04 USD (Minuit 36,50 ; Luc 77,37). La v3 disait déjà que « les rapports sont des rapports, non des marges en USD » ; le devis ne donne que le rapport (K8).
- **« Solde relu après recharge ».** La v4 et le devis le citent à la lettre et ne supposent aucun montant : juste. Trois choses restent ouvertes, que GO-34 ne tranche pas : (i) la manière de relire (lu sur le compte, ou déclaré par Lazar et rapproché du registre), alors que la v3 dit les soldes Claude « jamais lus » ; (ii) les deux lots en cours sur Rigaud (R-4170 : au plus 45 USD) : un solde relu pendant qu'ils tournent surestime la part, et l'arrêt n° 13 peut alors partir avant que la part soit atteinte ; (iii) le rejeu de la règle de choix : si la part de Rigaud dépasse 162,56 USD après la recharge (solde relu au-delà de 170,91), la règle, rejouée, préférerait le juge de l'espèce 3 sur Rigaud. GO-22 fixe la répartition, et le rédacteur a raison de ne pas la rejouer ; je le signale pour que personne ne la rejoue en silence. (i) et (ii) vont à la valeur ouverte K3, sans être tranchés.

## 5. La sonde de refus de l'espèce 6

- **Ce qu'elle mesure** : la réponse de la clé par son relais ; l'acceptation ou le refus de la question scellée, lus par la même garde que pour les espèces 1 à 5 ; son coût réel. **Son plafond** : 0,01 USD, tenu par le relais, ligne à part sur la clé de l'espèce 6, qui s'ajoute à la ligne de 1 USD : lecture juste, la ligne de 1 USD ne dit pas sur quelle clé elle se paie, et celle-ci ne peut se payer que sur la clé de l'espèce 6. **Son arrêt** : refus de la question, arrêt n° 2 ; refus d'un classifieur, arrêt n° 1 ; refus pour crédit, erreur d'accès ou réponse illisible : pas de relance, pas d'« acceptante », pas de course sans le mot de la mère. Éprouvée en moteur simulé sur cas sain et artefact. Bien écrite.
- **La taille de la requête** (point 9 du rapport du rédacteur ; « remarque 6 » dans mon mandat, voir les écarts). La question fait 10 562 octets. Au repère de tarif d'entrée, 0,01 USD paie 5 000 jetons d'entrée sans aucune sortie : la requête ne tient que si la question compte moins de 0,473 jeton par octet ; comptée à un jeton par octet, l'entrée seule vaudrait 0,0211 USD. Un relais qui borne le pire par les octets refusera donc la sonde ; un relais qui compte les jetons peut la tenir, avec une sortie très courte, au risque d'une réponse que la garde ne sait pas lire. La v4 a le bon repli (la sonde ne part pas, une ligne neuve se demande) ; le devis, qui demande les 0,01 USD à Lazar, ne le dit pas (K9). Recommandation à porter avec le devis : un plafond de 0,05 USD couvrirait l'entrée comptée à un jeton par octet et près de 2 890 jetons de sortie, et éviterait un second aller-retour.
- **Aucun contenu d'attaque, aucune recette, aucune invite opérante** : la sonde n'envoie que la question scellée telle qu'elle est servie ; le texte ne cite rien de son contenu. Vérifié aussi pour la clé de l'espèce 6, la table « un par un » et les ajouts du devis.

## 6. Les remarques du rapport du rédacteur

Le rapport en compte douze (§ 5), non neuf : je les prends toutes.

| n° | objet | suite | recommandation, confiance |
|---|---|---|---|
| 1 | plafond 570 ou 450 | à porter à Lazar (c'est la décision du devis, § 9) | 570 est la règle du devis v2 appliquée telle quelle ; à 150, seul le jeu des juges au cas haut se perd. Je rejoins (a), 0,65. Lettre de la variante corrigée (K5 à K7) |
| 2 | coût de l'espèce 6 | sans suite sur les règles ; à la mère pour le relevé du tarif au complément | règles prudentes ; le tarif n'entre dans aucun total de décision (§ 3), 0,8 |
| 3 | 6,05 USD par appel | sans suite ; valeur ouverte déjà écrite | borne très large au repère de tarif ; confirmer au complément avec la sortie maximale ; le relais de l'espèce 6 réserve ce pire par appel, cohérent avec l'arrêt n° 12, 0,8 |
| 4 | nom de la clé | à la mère | nom confirmé au registre des décisions ; présent aussi dans mon conteneur (code 0). Reste : le conteneur qui joue la course, la lisibilité du solde. Le nom de variable dit la lignée, ce que le numéro seul évite : imposé par le mandat, sans suite, 0,85 |
| 5 | juges et aiguilleur inchangés | sans suite | GO-33 n'en dit rien ; charges recalculées justes ; clé la plus serrée dite aussi en USD (K8), 0,85 |
| 6 | diversité | sans suite | Lazar a fait entrer l'espèce en le sachant (GO-32 puis GO-33) ; la v4 n'en tire rien, à juste titre, 0,8 |
| 7 | GO-34 | à corriger (K1 à K4) et à la mère | rendre le texte cohérent sans trancher ; la mère écrit au complément la manière de relire et l'état des lots de R-4170, et porte à Lazar ce que GO-34 ne dit pas ; ne pas rejouer la répartition (§ 4), 0,75 |
| 8 | X et la borne de 415,21 | sans suite | chiffres refaits (1,435 ; 154,79), 0,9 |
| 9 | sonde : taille de la requête ; ligne à part | à corriger (K9) ; à porter à Lazar avec le devis | option d'un plafond de 0,05 USD (§ 5), 0,6 ; ligne à part plutôt que dans la ligne de 1 USD : juste, 0,75 |
| 10 | pièces citées non récrites | à la mère | le devis v3 et son calcul sont déjà au chemin `N/preenregistrement-court-v4/` cité par la v4 (empreintes vérifiées là). L'ordre de course v3 et le rapport de conception v3 disent encore cinq espèces, alors que la v4 se scelle « avec l'ordre de course » (point 4) : un erratum ou une version de l'ordre de course, par sa chaîne (classe A), 0,7 |
| 11 | GO-2026-11-20-08 | sans suite | lu : 450 USD, échéance 30 novembre ; la v4 le dit justement « cité pour 450 », ne couvrant pas 570, 0,9 |
| 12 | GO-20 et GO-31 | à la mère, avec le point 7 | GO-31 et R-4187 (second lecteur choisi par essai comparatif) peuvent changer le besoin du bras A sur Rigaud ; X reste 8,35 par GO-22 ; tout dépassement pendant la course passe par l'arrêt n° 13, 0,7 |
| 13 | (neuf) R-4179, postérieure au commit du rédacteur | à la mère | une directive de Lazar rapportée, non relue à la source : une « note de périmètre de la mère avant la course », pour des modes inédits et non des recettes. Si la mère la confirme, elle entre dans « ce qui reste à écrire avant l'allumage » par une version neuve, 0,6 |
| 14 | (neuf) R-4181, portée de R1 posée à Lazar | sans suite pour ce texte | d'ici la réponse, la mère lit R1 comme tenant ; ce préenregistrement n'en change pas, 0,8 |

## 7. Le validateur

Lu d'abord : `valider_prereg_v4_v1.py` n'écrit rien et n'appelle que `controle_ia.prereg.problemes` et `sections`. `controle_ia.prereg` n'a pas d'entrée en ligne de commande (aucun `__main__`) : l'écart 2 du rédacteur est fondé. Rejoué depuis la racine, `PYTHONPATH=src` : sur la v4, toutes les sections présentes, un seul problème, « section vide ou à remplir : Contre-lecture » ; sur la v3, en témoin, aucun. Sur la copie corrigée par K1 à K4 (essai dans mon dossier, `b0696360…`) : le même seul problème.

## 8. Corrections, à texte exact

Chaque « Ancien » est compté une fois par `grep -c -F -e` dans sa cible. Les deux jeux sont écrits en JSON à côté de ce rapport (`corrections-preenregistrement-court-v4-v1.json`, `corrections-devis-v3-v1.json`) et passés à l'outil sur des copies : « FAIT : 4 remplacement(s) », sortie `b069636010af78752227e8cb83c72746f5658b796f08e6455b36f1afa3a8aa31` ; « FAIT : 5 remplacement(s) », sortie `c18e263e4c16f942764a4a68977b3aa9975ab50f92cf6cb1e181a7f51e6cc086`. Les versions neuves sont à écrire par la mère, sous des noms neufs (R12).

**Préenregistrement v4** (`2dabdadf…`)

- **K1** (méthode de Rigaud). Ancien : « Parts plafonnées au solde de chaque clé, sans recharge (GO-2026-11-20-16). Aucun solde n'est lu sur le compte : Minuit et Rigaud sont calculés au registre des dépenses, Luc est déclaré : » — Neuf : « Parts plafonnées au solde de chaque clé, sans recharge (GO-2026-11-20-16), sauf Rigaud, rechargée (GO-2026-11-20-34 ; paragraphe « Recharge de Rigaud » ci-dessous). Avant cette recharge, aucun solde n'est lu sur le compte : Minuit et Rigaud sont calculés au registre des dépenses, Luc est déclaré : »
- **K2** (arrêt n° 13). Ancien : « avant que sa part soit atteinte (leurs soldes sont calculés ou déclarés, jamais lus) » — Neuf : « avant que sa part soit atteinte (leurs soldes sont calculés ou déclarés, jamais lus ; pour Rigaud, le solde relu après la recharge de GO-2026-11-20-34, de la manière écrite au complément de valeurs) »
- **K3** (valeur ouverte neuve, sans rien trancher). Ancien : « si aucune borne ne le permet, la sonde ne part pas et une ligne neuve se demande | avant la sonde | » — Neuf : le même texte, suivi d'un saut de ligne et de la ligne de table : « | la manière de relire le solde de Rigaud après la recharge (GO-2026-11-20-34 : lu sur le compte, ou déclaré par Lazar et rapproché du registre des dépenses), et l'état, à ce moment, des deux lots en cours sur cette clé (R-4170 : au plus 45 USD) | écrite par la mère au complément de valeurs ; ce que GO-2026-11-20-34 ne tranche pas va au mot de Lazar | avant tout allumage et avant la contre-lecture du véhicule | »
- **K4** (valeurs ouvertes). Ancien : « Les parts s'écrivent au complément de valeurs, sur le reste calculé de chaque clé au jour du complément. » — Neuf : « Les parts s'écrivent au complément de valeurs, sur le reste calculé de chaque clé au jour du complément (pour Rigaud, sur le solde relu après la recharge, GO-2026-11-20-34). »

**Devis v3** (`bf7b4ba3…`)

- **K5** (§ 5, variante : à 150 USD, la génération n'est pas coupée par son plafond ; elle s'arrête avant les juges, à 124,10 USD au cas haut). Ancien : « | six espèces, ligne gardée à 450 USD (variante, v3) | au cas haut, les juges ne sont pas lancés et la génération est coupée par son plafond ; » — Neuf : « | six espèces, ligne gardée à 450 USD (variante, v3) | au cas haut, les juges ne sont pas lancés : le cumul avant eux, 124,10 USD, passe leur seuil de 120 USD, et la génération s'arrête là, sous son plafond ; »
- **K6** (§ 9, option (b), même raison). Ancien : « Inconvénient : au cas haut, les juges ne sont pas lancés et la génération est coupée par son plafond ; » — Neuf : « Inconvénient : au cas haut, les juges ne sont pas lancés (cumul de 124,10 USD avant eux, pour un seuil de 120) ; »
- **K7** (§ 3, même raison). Ancien : « et dépasse le plafond (180,88 ; champ `variante_plafond_de_150_garde`) » — Neuf : « et, juges compris, dépasserait le plafond (180,88 ; champ `variante_plafond_de_150_garde`) »
- **K8** (§ 6, clé la plus serrée). Ancien : « La clé la plus serrée devient Minuit. » — Neuf : « La clé la plus serrée devient Minuit, en rapport ; en USD, la marge la plus courte au cas haut reste celle de Rigaud avant la recharge (12,04 USD, contre 36,50 pour Minuit et 77,37 pour Luc). »
- **K9** (§ 4, sonde de l'espèce 6 : ce que Lazar accorde). Ancien : « Estimée à moins d'un centime : 0,0017 USD, le tiers de la sonde de trois modèles (S4). » — Neuf : « Estimée à moins d'un centime : 0,0017 USD, le tiers de la sonde de trois modèles (S4). Une réserve : la question scellée fait 10 562 octets ; au repère de tarif (S9 : 2 et 10 USD par million de jetons, entrée et sortie), 0,01 USD paie 5 000 jetons d'entrée sans aucune sortie. L'entrée seule ne tient donc sous le plafond qu'à moins de 0,473 jeton par octet de la question ; comptée à un jeton par octet, elle vaudrait 0,0211 USD. Si le relais ne peut pas tenir la requête sous 0,01 USD, la sonde ne part pas et une ligne neuve se demande (préenregistrement court v4, valeurs ouvertes). »

**Texte à porter à la section « Contre-lecture 4 »**, à la place de la ligne qui porte le marqueur (ancre comptée une fois : « - **Contre-lecture 4** (la v4, par un agent neuf d'un autre modèle) : À REMPLIR. ») ; la mère y écrit l'empreinte de ce rapport, prise à son compagnon, et le traitement :

« - **Contre-lecture 4** (la v4, par un agent neuf d'un autre modèle) : contre-lecteur neuf, modèle O, sous-agent de la session de l'organisme, le 2026-11-20 ; il n'a écrit aucune version de ce texte, du devis, de l'ordre de course, ni leurs contrôles. Brouillon relu : la v4, `2dabdadf9ac126ee8d931dfde3e3507a3183b50b8f584d0f817e7ebf8adf2b10`, avec le devis v3, `bf7b4ba3ede3ba73c8ee4e1a3548b6b0d52975df717b98ca4af44a6c503c142a`. Rapport : `docs/notes/ideation-nouvelles-attaques-v1/preenregistrement-court-v4/contre-lecture-preenregistrement-court-v4-devis-v3-v1.md`, (empreinte du rapport), verdict « À corriger » : K1 à K4 sur ce texte, K5 à K9 sur le devis v3, toutes de lettre ; aucun total, seuil ni arrêt changé. Rejeu de l'outil égal à l'octet ; totaux refaits par un programme indépendant, égaux au centime. Traitement : (à écrire par la mère). »

## 9. Écarts

1. Mon mandat dit « les neuf remarques » et « remarque 6 » pour la taille de la requête : le rapport du rédacteur en compte douze, et la taille de la requête est son point 9. J'ai pris les douze, et deux points neufs (13 et 14).
2. `main` a avancé depuis le commit du rédacteur (`da0d389c` → `fbaf5319`) : `go.md` est identique ; `decisions.md` a reçu R-4175 à R-4187, lues pour ce qui touche la course.
3. Ma vérification de présence de la clé de l'espèce 6, par le nom seulement, n'était pas demandée : elle répond au point 4 du rédacteur, sans lire aucune valeur.
4. Pour éprouver les corrections, j'ai fait passer l'outil sur des copies, dans mon dossier, sous-dossier `rejeu/` ; rien n'est écrit ailleurs.

— contre-lecteur neuf, modèle O
