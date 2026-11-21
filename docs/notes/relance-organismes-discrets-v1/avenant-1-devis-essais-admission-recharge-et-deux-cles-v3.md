# Organismes discrets, bras A — avenant 1 au devis des deux essais d'admission : recharge automatique gardée chez Google, et deux clés de Google — note d'écart — v3

- **Objet** : dire ce que les mots de Lazar du 21 novembre changent au devis accepté des deux essais d'admission (`docs/notes/relance-organismes-discrets-v1/devis-essais-admission-mistral-neon-bras-a-v1.md`, sha256 `421ee2e6ec909c8b6261b3be39109aa5e76d6c275e79b4d7ec122816c83dd1bc`, recalculée ici). Le devis n'est pas réécrit : il reste tel quel, et cet avenant se lit avec lui.
- **État** : version 3, brouillon, écrite le 2026-11-21 par le rédacteur des versions 1 et 2 (Claude Fable 5.2), qui n'a écrit ni le devis ni le programme. La version 1 (sha256 `14d479d70ee57ccfcb80bc582c51acdeda92b2de67b3ae7c82936a878093603d`) et la version 2 (sha256 `3dbc747b6e38683338c10c52fad9edd91454e3fd6fdeeb35b6b277acb867d2d3`) sont scellées comme brouillons et restent inchangées. Le même agent Claude Opus 5.5 les a contre-lues : la version 1, « engageable après corrections », six corrections et douze mineurs (`contre-lecture-avenant-1-devis-essais-admission-v1.md`) ; la version 2, « engageable après corrections », légères, deux corrections et quatre mineurs (`contre-lecture-avenant-1-v2-devis-essais-admission-v1.md`). Cette version porte les unes et les autres (sections 12 et 13), et les quatre décisions de Lazar de 17:25Z. **Elle est à sceller comme brouillon par la session ; elle n'est ni revérifiée ni acceptée.**
- **Les mots de Lazar**, tels que la session mère me les a relayés :
  1. vers 17:10Z, inscrits sous GO-2026-11-21-66 (registre non ouvert pour cette ligne) : « je prefere la garder allumeee pour eviter toute coupure impromptue » ; « on va combiner les deux » ;
  2. vers 17:25Z, inscrits sous GO-2026-11-21-68, **en réponse aux quatre décisions de la version 1** : « ca m'emmerde on zappe ca, on combine les deux cles 1 et 2 comme on veut, recharge automtique activee basta , euros affices , pas de plafond mensuel » ; et, pour la marge de change de 5 % : « go ». J'ai lu cette seule ligne du registre, sur la branche principale, avec l'accord de la session mère. Elle porte de plus : « (visée environ 20 € sur le projet de la clé) » ; « le constat ligne par ligne aux consoles est abandonné » ; « bras A : pire cas 84,06 USD sans borne dure (accepté) ».
- **Seule source sur l'état des comptes** : deux captures de la page de facturation de l'API Gemini dans AI Studio, envoyées par Lazar à la session mère à 2026-11-21T16:24:17Z. Je ne les ai pas vues ; la session mère m'en dit le contenu. Elles montrent un projet en offre payante avec prépaiement, solde 11,93 €, recharge automatique activée, 0 € d'autres crédits (« projet A ») ; et un projet en offre payante avec prépaiement, solde 15,59 €, recharge automatique activée, 0 € d'autres crédits (« projet B »). **On ne sait pas quel projet porte quelle clé.**
- **Ce que cet avenant ne change pas** : aucun plafond de ligne (0,25 ; 1,50 ; 4,75 ; 8,50 ; 0,25 USD), aucun excès d'un envoi, aucun délai, aucun réglage des modèles, les valeurs des seuils de crédit (19,76 et 16,08 USD), le compte « huit sur huit ». **Ce qu'il change, par décision de Lazar** : ce à quoi les seuils se comparent ; ce que « huit sur huit » juge ; ce que la pièce de constat porte ; une ligne de calcul de plus. Des gardes s'ajoutent, et une s'allège (section 7).
- Marques : (C) calculé ici, par programme (section 11) ; (S) supposé, sans pièce ; (D) repris du devis.

## 0. En une page

1. **Pire cas chez Google : 84,06 USD, sans borne dure, accepté par Lazar** (GO-2026-11-21-68). C'est la file du juge au cas des neuf excès, 76,70 USD, et deux vérifications de clé à 3,68 USD (C). Au régime prudent, ou si la supposition de la sonde tient : 23,44 USD. Ces chiffres ne valent que sous les suppositions du devis sur le débit et sur la coupure d'un envoi (2.2). **Aucun plafond de dépense n'est réglé à la console.**
2. **La file du juge est partagée entre les deux clés, par une règle fixe écrite d'avance** : les lectures de rang impair vont à `GEMINI_API_KEY`, celles de rang pair à `GEMINI_API_KEY_2` ; la reprise d'un appel reste sur sa clé (4.1). Une seule file, une seule ligne de calcul, un seul compteur, un seul plafond de 8,50 USD. Chaque clé a sa vérification, d'où **une ligne de calcul de plus** (1,50 USD de plafond).
3. **« Huit sur huit » ne juge plus la même chose** (4.2). Reste jugé : le modèle, à son réglage, sur les huit entrées, dans l'ordre. N'est plus jugé : qu'une même voie de service tienne huit lectures de suite ; chaque clé n'en sert que quatre. C'est un écart au texte du préenregistrement, à porter par un brouillon du texte avant le premier envoi.
4. **Seuils de crédit** : 19,76 et 16,08 USD, inchangés, lus **sur chaque projet**, sur le solde vu en euros, converti au taux diminué de 5 %, **plus une recharge automatique, une seule**, moins la dépense déjà comptée (4.4). Tant qu'on ne sait pas que les deux clés sont sur deux projets différents, c'est la **somme** des dépenses des deux clés qui est retirée. **Cette règle ne se calcule pas encore : le montant d'une recharge n'est pas relevé.** C'est le seul chiffre qui manque.
5. **Le constat ligne par ligne aux consoles est abandonné par Lazar.** Ne sont constatés ni le partage des journaux, ni leur durée, ni le lien entre chaque clé et chaque projet. La pièce de constat reste exigée par le programme : elle porte vingt-huit clés : les valeurs vues sur les deux captures et, pour chacune des six clés levées, la valeur fermée « non constaté, levé par GO-2026-11-21-68 » (section 5). Aucune clé n'est levée en silence.
6. **Quatre points restent ouverts, aucun n'est une décision de fond** (section 8) : le montant d'une recharge ; le sens de « visée environ 20 € » ; si l'abandon du constat vaut aussi pour Mistral ; si les deux clés sont sur deux projets différents.

## 1. Les écarts, cités à la lettre

Numéros de ligne du fichier du devis, à l'empreinte ci-dessus. Les citations des quatre tableaux sont confrontées par programme à leur ligne (section 10).

### 1.1 Écart 1 : la recharge automatique reste activée

| ligne | section | ce que le devis écrit | ce que le mot de Lazar en fait |
|---|---|---|---|
| 16 | 0, point 4 | « Chez Google, la dépense est bornée par le solde prépayé, plus tout autre crédit Google Cloud admissible du compte de facturation » | faux avec la recharge active : voir section 2 |
| 24 | 0, point 12 | « Chez Google, la perte est bornée par le solde prépayé, plus tout autre crédit Google Cloud admissible du compte ; ce que fait le service au solde nul n'est pas relevé. » | de même |
| 389 | 6.4 | « **Seul le solde prépayé borne alors la perte chez Google** » | plus rien de dur ne borne ce cas ; aucun plafond de dépense n'est réglé à la console (2.4) |
| 393 | 6.4 | « (4) une recharge automatique, si la console en propose une et qu'elle est active, lèverait la borne : le constat exige qu'elle ne le soit pas (section 9). » | la réserve (4) s'est réalisée, par décision de Lazar |
| 400 | 6.4 | « pendant un envoi, rien ne le tient que le délai, et, au bout, le solde prépayé, sous ses réserves » | « au bout », il ne reste que le délai |
| 445 | 6.5 | « **Recharge automatique** : si une console en propose une, elle reste désactivée. Active, elle lèverait la borne du solde. » | contredit à la lettre |
| 447 | 6.5 | « Charger est un geste de Lazar. » | une recharge automatique est un paiement sans geste, d'un montant non encore relevé |
| 507 | 9 | « `google_recharge_automatique` \| `désactivée`, ou `non proposée` » | la valeur `activée` doit être admise, avec son montant et son seuil |
| 538 | 10, garde 9 | cas sain : « recharge automatique `désactivée` » ; artefact : « `google_recharge_automatique` à `activée` » | l'artefact devient un cas sain ; un artefact neuf le remplace (section 7) |
| 565 | 11 | « La dépense est bornée par le solde prépayé, plus tout autre crédit Google Cloud admissible du compte de facturation, aucun au constat » | phrase à retirer des lignes de calcul 2 et 4 |
| 568 | 11 | « Seul le solde prépayé borne alors la perte chez Google » | de même |
| 586 | 11.1, ligne 2 | « la perte est bornée par le solde prépayé » | texte neuf en section 6 |
| 588 | 11.1, ligne 4 | « que seul le solde prépayé borne » | texte neuf en section 6 |

### 1.2 Écart 2 : deux comptes, deux projets, deux clés, des soldes en euros

| ligne | section | ce que le devis écrit | ce que le mot de Lazar en fait |
|---|---|---|---|
| 16 | 0, point 4 | « chez Google, 23,00 USD de crédit prépayé, en une fois » | aucun compte n'a été porté à 23,00 USD ; deux soldes, 11,93 € et 15,59 € |
| 93 | 4.1 | « **Clés lues par leur nom seulement**, dans l'environnement du seul relais : `MISTRAL_API_KEY` ; `GEMINI_API_KEY`. » | une seconde variable, `GEMINI_API_KEY_2` |
| 407 | 6.5 | « 22,72, soit **23,00 USD prépayés** » | le crédit à avoir n'est plus sur un seul compte |
| 422 | 6.5 | « Lazar charge ce qui manque à 23,00 au solde qu'il voit » | non fait ; décision non reprise après les mots de 17:25Z (section 6 ; 8.2, point 2) |
| 433 | 6.5 | « **Google, avant la vérification** : crédit prépayé vu d'au moins **19,76 USD** » | le seuil se lit par projet ; aucun des deux soldes ne le passe seul (section 3) |
| 434 | 6.5 | « **Google, avant la file Neon** : au moins **16,08 USD** » | de même, par projet |
| 435 | 6.5 | « elle exige de nouveau **19,76 USD** de crédit vu » | de même |
| 437 | 6.5 | « le crédit du dernier constat, moins la dépense comptée des lignes de Google jouées depuis ce constat, atteigne 16,08 USD » | « des lignes de Google jouées **sur ce projet** » |
| 503 | 9 | « la clé lue sous `GEMINI_API_KEY` est celle du projet constaté \| `google_cle_du_projet_constate` \| `oui` » | une clé du constat par variable et par projet |
| 506 | 9 | « `google_credit_utilisable_usd` \| un nombre, au moins 19,76 » | un crédit par projet, vu en euros, converti |
| 539 | 10, garde 10 | « le crédit du dernier constat, moins la dépense comptée des lignes de Google jouées depuis ce constat, lue aux relevés, est d'au moins 16,08 USD » | compte par projet |
| 549 | 10, garde 20 | « chez Google, la pièce porte le solde prépayé vu, au moins égal à ce que 6.5 exige pour la ligne » | solde du projet de la ligne ; recharges survenues à dire |
| 569 | 11 | « la variable de la clé ; le compte qui paie » | chaque ligne de Google nomme sa variable et son projet |
| 578 et 593 | 11 et 11.1 | « complément de 7,00 USD pour un solde de 16,00 » ; « le solde prépayé porté à 23,00 USD en une fois » | geste de paiement à récrire (section 6) |
| 586 | 11.1, ligne 2 | « payé sur le crédit prépayé, porté à 23,00 USD avant la ligne » | texte neuf en section 6 |
| 588 | 11.1, ligne 4 | « dont il reste au moins 19,32 USD au départ de la file après la recharge à 23,00 USD » | texte neuf en section 6 |

### 1.3 Lignes touchées que la version 1 ne déclarait pas (contre-lecture, C-2)

Le tableau est celui de la contre-lecture, repris tel quel ; chaque citation est confrontée ici par programme à sa ligne. « Écart 1 » : la recharge gardée ; « écart 2 » : les deux clés et les euros.

| ligne | section | ce que le devis écrit | écart | ce que le mot de Lazar en fait |
|---|---|---|---|---|
| 5 | en tête | « **chez Google, 23,00 USD de crédit prépayé, en une fois** » ; « seul le solde borne alors la perte, au risque de couper une file qui tiendrait » | 2 ; 1 | les deux phrases tombent |
| 181 | 4.4, texte dit à Lazar sur la file Neon | « La perte est bornée par le solde prépayé, plus tout autre crédit Google Cloud admissible du compte » | 1 | de même que la ligne 24 |
| 183 | 4.4 | « la recharge en une fois à 23,00 USD le laisse, même au pire (19,32 ; 6.5) » | 2 | ne vaut plus : aucun projet n'est porté à 23,00 USD (4.4) |
| 386 | 6.4, supposition 2 | « c'est la seule borne d'un envoi, hors le solde prépayé » | 1 | ce « hors » tombe |
| 394 | 6.4 | « Le solde prépayé borne la perte, sous ces réserves ; il ne protège pas l'essai. » | 1 | la première moitié tombe ; la seconde demeure, atténuée par la recharge |
| 411 | 6.5 | « **Décision de Lazar : chez Google, une seule recharge, à 23,00 USD** » | 2 | décision antérieure de Lazar, non reprise après les mots de 17:25Z (section 6 ; 8.2, point 2) |
| 412 à 418 | 6.5, tableau des soldes de départ | « solde de départ S », en USD, sur un seul compte | 2 | à relire par projet, en USD convertis ; il repose sur 16,00 USD (section 3) |
| 423 | 6.5 | « Sur les seuls 16 USD » | 2 | le solde vu est en euros |
| 426 | 6.5, point 1 | « **le solde prépayé borne la perte chez Google » | 1 | tombe |
| 435 | 6.5 | « **une recharge d'au moins 0,44 USD est alors due** » ; « Toute recharge faite après le constat se constate par un constat neuf, daté, sous un nom neuf. » | 1 | une recharge automatique ne se constate pas d'avance : 4.4, point 5 |
| 438 | 6.5 | « le solde est ce qui peut être perdu si tout va mal ; 23,00 USD y sont exposés » | 1 | faux : l'exposition est celle de 2.2 |
| 446 | 6.5 | « Le solde prépayé borne la perte, sous les réserves de 6.4 » | 1 | tombe |
| 515 | 9 | « le crédit porté à 23,00 le passe » | 2 | par projet, converti |
| 538 | 10, garde 9 | cas sain : « crédit prépayé de Google à 23,00 » ; artefact : « `google_credit_utilisable_usd` à 16,00, l'état de départ avant la recharge » | 2 | à reprendre par projet, en euros convertis, avec une recharge (4.4 ; section 7, point 7) |
| 599 | 12, point 3 | « **crédit de Google porté à 23,00 USD**, recharge automatique désactivée » | 1 ; 2 | contredit par l'écart 1 ; par projet pour l'écart 2 |
| 640 | 13, point 28 | « c'est **le solde restant au départ de la file** qui borne alors la perte » | 1 | tombe |
| 641 | 13, point 29 | « Le solde prépayé comme borne de la perte » ; « l'absence de recharge automatique ne sont pas écrits non plus » | 1 | tombe |
| 645 | 13, point 33 | « la borne du solde ne vaut que si aucune recharge automatique ne joue » | 1 | la condition manque désormais |
| 646 | 13, point 34 | « **Le solde de 16 USD** est un mot de Lazar » | 2 | le solde vu est en euros (section 3) |
| 648 | 13, point 36 | « une recharge faite après le constat demande un constat neuf » | 1 | 4.4, point 5 |

### 1.4 Écarts ouverts par les décisions de Lazar du 21 novembre, 17:25Z (GO-2026-11-21-68)

| ligne | section | ce que le devis écrit | ce que la décision en fait |
|---|---|---|---|
| 13 | 0, point 1 | « **Deux files indépendantes, une par fournisseur.** » | la file du juge reste une file, servie par deux clés (4.1) |
| 22 | 0, point 10 | « les réglages des deux consoles constatés et datés » | constat ligne par ligne abandonné ; la pièce porte ce que montrent deux captures (section 5) |
| 203 | 5.1 | « une file n'est jouée qu'une fois » | inchangé, lu sur les deux clés ensemble |
| 400 | 6.4 | « **Un relais est lancé par ligne de calcul** » | deux relais pour la file du juge, un par clé (4.3) |
| 459 | 7, règle 2 | « si ses huit lectures rendent huit réponses de code 200 » | compte inchangé ; quatre lectures par clé (4.2) |
| 460 | 7, règle 3 | « toutes les réponses de la file portent le nom servi que la vérification de la clé a relevé » | deux vérifications ; lecture par clé, et nom servi égal exigé avant la file (4.2) |
| 493 | 9 | « Elles valent **avant la vérification de la clé** aussi » | les conditions d'envoi ne sont plus constatées, sauf l'offre payante |
| 498 | 9 | « `google_partage_journaux` \| `désactivé` » | non constaté, levé |
| 499 | 9 | « `google_duree_journaux_jours` \| l'entier `7` » | non constaté, levé |
| 503 | 9 | « `google_cle_du_projet_constate` \| `oui` » | non constaté, levé, pour chaque variable |
| 512 | 9 | « le programme refuse un tableau où une clé manque, où une clé de plus figure, ou dont une valeur n'est pas admise » | inchangé ; la valeur levée devient une valeur admise, pour les seules clés nommées (section 5) |
| 519 | 9 | « Lazar, sur l'écran de chaque console, après le réglage » | deux captures de la page de facturation, relayées par la session mère |
| 520 | 9 | « Ni courriel, ni identifiant de compte, ni capture d'écran dans le dépôt. » | inchangé : la pièce cite les captures par leur heure, sans les verser |
| 521 | 9 | « un brouillon du texte porte le constat à la case « lecteurs et juge des ancres » de 13.1, avant la première vérification de clé. » | le brouillon porte la pièce nouvelle, clés levées nommées (4.2) |
| 539 | 10, garde 10 | « la file exige le relevé scellé de sa vérification » | les deux relevés, un par clé |

Sous les décisions du 21 novembre, 17:25Z, la phrase de la version 1 sur les lignes 497 à 499 tombe : seule la ligne 497 (offre payante) garde une valeur vue.

## 2. Ce qui remplace la borne par le solde

### 2.1 Ce que le solde faisait, et ce qui en reste

Le solde prépayé tenait deux rôles dans le devis.
- **Borne de la perte**, en dernier recours : si tout le reste manquait, on ne perdait que le solde, sous quatre réserves (ligne 393). **Ce rôle tombe.** Avec la recharge active, la perte possible est le solde, plus autant de recharges que le service en déclenche.
- **Cause de coupure d'une file** : « un solde à court coupe une file partie », et c'est alors la caisse qui décide, non le modèle (ligne 394). **Ce risque baisse**, et c'est ce que Lazar veut ; il ne disparaît pas : rien ne dit qu'une recharge est créditée avant que le solde soit vide (S), ni qu'un seul envoi long ne le vide pas d'un coup.

### 2.2 Perte maximale par ligne, chez Google

Rien n'est recalculé dans les trois premières colonnes : ce sont les chiffres du devis (D). Les sommes sont calculées ici (C, section 11).

**D'où vient 76,70** (contre-lecture, C-1 ; refait ici). Le devis chiffrait les neuf envois coupés seuls. Or le compteur laisse aussi passer les autres envois, jusqu'à son plafond. Un envoi coupé coûte réellement sa réserve plus 7,578 USD (8,085 − 0,507 à l'appariement ; 8,142 − 0,564 à la couverture). Le compteur refuse un envoi quand le cumul compté passe 8,50 − 0,564 = 7,936 USD. Au pire : 7,936 comptés avant le dernier envoi, ce dernier envoi au coût plein d'un envoi de couverture coupé, 8,142, et huit envois coupés plus tôt, chacun de 7,578 au-delà de ce qui en a été compté : 7,936 + 8,142 + 8 × 7,578 = 76,702, soit 8,50 + 9 × 7,578.

| ligne de calcul | plafond tenu par la garde 1 (D) | excès possible d'un envoi en cours (6.4, D) | **plafond et excès : ce que le compteur borne** | ce que les recharges ajoutent |
|---|---|---|---|---|
| vérification de la clé de Google (ligne 2), toujours au régime prudent | 1,50 | 2,18 | **3,68** (D, ligne 383) | rien au chiffre ; le filet du solde tombe |
| file du juge (ligne 4), partie sur un mot de Lazar, régime prudent | 8,50 | 7,58 | **16,08** (D, ligne 383) | de même |
| file du juge (ligne 4), partie après une sonde « comprise », régime courant, si la borne se comporte à 32 768 comme à 256 | 8,50 | 7,58 au plus | **16,08** (D, ligne 389) | de même |
| **la même, si cette supposition manque** | 8,50 | neuf excès de 7,58 au plus | **76,70** (C : 8,50 + 9 × 7,578 = 76,702) ; les neuf envois coupés seuls font 72,77, ou 72,94 si trois des neuf sont des envois de couverture (D, ligne 389) | **tout** : le devis bornait ce cas par le solde restant, 19,32 à 22,98 USD ; plus rien de dur ne le borne |

Totaux chez Google (C) :
- régime prudent, ou supposition tenue : 3,68 + 16,08 = **19,76 USD** ; c'est le chiffre « à couvrir » du devis, inchangé ;
- supposition manquante au régime courant : 3,68 + 76,70 = **80,38 USD** ;
- **avec deux vérifications de clé**, ce que la file partagée demande (section 4) : 3,68 de plus, soit **23,44 USD** et **84,06 USD**. C'est le cas retenu.

Avec les lignes de Mistral, inchangées (1,42 + 1,42 + 5,39 = 8,23, D) : 8,23 + 19,76 = **27,99 USD**, le total « plafonds et excès ensemble » du devis (ligne 563), ce qui recoupe le calcul.

**Tous ces chiffres gardent les trois suppositions du devis** (ligne 384 et suivantes) : pas plus de 200 jetons par seconde ; la coupure d'un envoi arrête la génération et la facturation ; les compteurs d'un envoi fini disent ce qui est facturé. Si la deuxième manque, le devis écrivait déjà que l'excès chiffré « ne borne plus rien » ; il ajoutait « hors le solde prépayé » (ligne 386). **Ce « hors » n'existe plus.**

**Les 16,08 et 19,76 USD ne sont donc eux-mêmes des bornes que sous les suppositions 1 et 2** (contre-lecture, m-6). Sans le solde, à 400 jetons par seconde au lieu de 200 (excès du devis, lignes 380 et 381 : 4,85 et 15,65), le régime prudent donne 1,50 + 4,85 + 8,50 + 15,65 = **30,50 USD**, et le cas des neuf excès, 8,50 + 9 × 15,65 = **149,35 USD** (C, au grain des excès du devis). Si la coupure n'arrête pas la facturation, aucun chiffre ne vaut.

### 2.3 Ce que les recharges ajoutent, en formule

Soit, pour un projet, S le solde vu, T le seuil de déclenchement, M le montant d'une recharge, dans la même monnaie. Pour payer une dépense D sur ce projet, le service déclenche, si la recharge part dès le passage sous T et est créditée aussitôt (S) :

`nombre de recharges = 0 si D ≤ S − T ; sinon l'entier supérieur de (D − (S − T)) ÷ M`

- **Dépense attendue** (≈ 0,36 USD chez Google, D) : aucune recharge, sauf si le solde est à moins de 0,36 USD au-dessus du seuil T.
- **Chaque recharge est un paiement de M**, taxe en sus s'il y en a une (S), pris sur le moyen de paiement du compte sans geste de Lazar. Le devis n'en prévoyait aucun (ligne 447). Un crédit rechargé et non consommé n'est pas une dépense de calcul ; il reste une somme sortie.
- **Un moyen de paiement refusé** laisse entière la coupure par un solde à court : la recharge ne protège la file que si le paiement passe (S).
- **La borne dure de la perte sur un projet devient** : S, plus M fois le nombre de recharges que le service permet. Si la console ne borne ni ce nombre ni la dépense du mois, **il n'y a pas de borne dure**.
- **Autre consommation du même compte de facturation** : si un autre projet ou un autre programme tire sur le même crédit prépayé, il peut déclencher des recharges et abaisser le solde pendant une ligne. Non relevé (section 9).

### 2.4 Plafond de dépense à la console : aucun, par décision de Lazar

La version 1 recommandait un plafond de dépense à la console, s'il en existait un qui refuse les appels. **Lazar a tranché : « pas de plafond mensuel »** (GO-2026-11-21-68). Lazar a écarté un plafond mensuel ; je lis qu'aucun plafond de dépense n'est réglé, quelle que soit sa période. C'est une lecture, que la valeur admise `aucun, par GO-2026-11-21-68` reprend. Rien n'est donc réglé, et rien n'est à relever sur ce point.

- **Ce que cela laisse** : la perte chez Google n'a pas de borne dure. La borne calculée est celle de 2.2 ; avec deux vérifications de clé (une par clé, section 4) : **23,44 USD** au régime prudent, **84,06 USD** au cas des neuf excès (C). Le registre porte « pire cas 84,06 USD sans borne dure (accepté) » : le chiffre est le même.
- **Ce que le registre n'écrit pas, et que je redis** : 84,06 USD suppose un débit d'au plus 200 jetons par seconde et une coupure qui arrête la facturation. À 400 jetons par seconde : 36,85 USD au régime prudent, 162,05 USD au cas des neuf excès (C). Si la coupure n'arrête pas la facturation, aucun chiffre ne vaut. La seule parade qui reste est la lecture de la console après tout envoi coupé (garde 20), que je lis comme **maintenue** : la décision abandonne le constat des conditions d'envoi, non cette lecture (section 8, point ouvert 3).
- **Le régime prudent imposé à la file** (option 3 de la version 1) n'est pas retenu : il retirerait la reprise unique que la règle 1 donne (devis, ligne 346 : « un modèle pourrait échouer sur un seul délai, par une règle de compte du devis »).

### 2.5 Ce qu'il reste à relever : la recharge, et elle seule

1. **ce que vaut une recharge automatique**, pour chaque projet : soit un montant ajouté, soit un solde visé, selon ce que la page affiche. C'est ce qu'exige la règle des seuils (4.4). Si les deux captures le montrent, la session le lit sur elles ; sinon, c'est un mot de Lazar ;
2. le seuil de déclenchement : **non exigé**, la règle ne s'en sert pas ;
3. le reste de la liste de la version 1 (limite des recharges, moment du crédit, autres projets du compte) : **non relevé, par décision de Lazar**. Ce sont des réserves (section 9).

## 3. Les deux soldes, en dollars : ce qu'on peut dire sans taux

Aucun taux n'est choisi ici. Soit t le taux en USD par euro, et m la marge de change, que Lazar a fixée depuis à 5 %. Un solde vu en euros vaut, pour les gardes : `euros × t × (1 − m)`, arrondi au centime inférieur.

| seuil du devis (USD) | ce qu'il couvre | taux t qu'il faut au moins au compte A (11,93 €) | au compte B (15,59 €) | aux deux ensemble (27,52 €) |
|---|---|---|---|---|
| 3,68 | la vérification seule, plafond et excès | 0,3085 | 0,2361 | — |
| 12,18 | la vérification, et le plafond de la file sans excès | 1,0210 | 0,7813 | — |
| 16,08 | la file du juge, plafond et excès | 1,3479 | 1,0315 | — |
| 19,76 | la vérification et la file, plafonds et excès | 1,6564 | 1,2675 | 0,7181 |

(C : seuil divisé par le solde, avec m nulle, **arrondi à la quatrième décimale par excès** : à 1,0314 USD par euro, 15,59 € ne font que 16,0795 USD, sous 16,08. Avec une marge m, diviser encore par 1 − m, toujours par excès. Pour m de 5 % : 1,0315 devient 1,0858 ; 1,2675 devient 1,3342 ; 0,7181 devient 0,7559. Pour m de 2 % : 1,0525 ; 1,2934 ; 0,7327. Tous les quotients sont en section 11.)

**Lecture.** Je ne juge pas du taux : la pièce du taux le dira. Les deux soldes ensemble passent 19,76 USD dès 0,7181 USD par euro. **Aucun ne le passe seul** sans un euro d'au moins 1,2675 USD (1,26748 exactement) pour le compte B, 1,6564 pour le compte A. Le compte B passe seul 16,08 USD si l'euro vaut au moins 1,0315 USD (1,0858 avec une marge de 5 %). Or un solde ne paie que les appels de la clé de son projet : la somme des deux ne vaut que si les appels sont répartis sur les deux clés.

**Le « 16 dollars » du 21 novembre.** La pièce `mots-de-lazar-compte-google-prepaye-bras-a-2026-11-21-v1.md` (`487b5a72…`) porte « il reste 16 dollars sur la cle par defaut ». C'est très probablement le solde de 15,59 € du compte B, lu en dollars (contre-lecture, m-4). Le tableau des soldes de départ du devis (lignes 412 à 418) repose sur ces 16,00 USD. **Il ne faut pas en tirer quelle variable va avec quel compte** : la pièce dit « clé par défaut », et ce lien n'est pas constaté (section 9, point 3).

**Avec la marge de change de 5 %, décidée par Lazar.** Un solde vu en euros compte pour `euros × t × 0,95`, arrondi au centime inférieur. Le projet A compte pour 11,3335 × t ; le projet B, pour 14,8105 × t (C). Sans recharge comptée, le projet A passe 19,76 USD à partir de 1,7436 USD par euro, et le projet B à partir de 1,3342. Ce qu'une recharge doit apporter pour passer 19,76 USD, à trois taux pris **en exemple seulement** :

| taux t, exemple | projet A compté (USD) | recharge à compter pour 19,76 | projet B compté (USD) | recharge à compter pour 19,76 |
|---|---|---|---|---|
| 1,00 | 11,33 | 8,43 USD, soit 8,88 € vus | 14,81 | 4,95 USD, soit 5,22 € vus |
| 1,10 | 12,46 | 7,30 USD, soit 6,99 € vus | 16,29 | 3,47 USD, soit 3,33 € vus |
| 1,20 | 13,60 | 6,16 USD, soit 5,41 € vus | 17,77 | 1,99 USD, soit 1,75 € vus |

(C. « € vus » : le montant affiché en euros qui, converti au taux diminué de 5 %, apporte la somme, arrondi au centime supérieur.)

## 4. Deux clés, une file : la règle de partage, ce qui est jugé, comment les gardes comptent

Lazar a tranché : « on combine les deux cles 1 et 2 comme on veut ». La règle est donc à écrire ici. Je la choisis la plus simple, et fixée d'avance.

### 4.1 La règle de partage

- **Par le rang dans l'ordre de la file** (devis, section 3, garde 17) : les lectures de rang impair vont à la clé lue sous `GEMINI_API_KEY` (« clé 1 ») ; celles de rang pair, à la clé lue sous `GEMINI_API_KEY_2` (« clé 2 »).

| rang | entrée | clé |
|---|---|---|
| 1 | `A-b1-01` | clé 1 |
| 2 | `A-b1-02` | clé 2 |
| 3 | `A-b1-03` | clé 1 |
| 4 | `A-b1-04` | clé 2 |
| 5 | `A-b1-05` | clé 1 |
| 6 | `A-b1-06` | clé 2 |
| 7 | `C-b1-02` | clé 1 |
| 8 | `C-b1-03` | clé 2 |

- **Chaque clé sert trois lectures d'appariement et une de couverture** : même charge, même pire cas (4,17 USD d'envois finis par clé, 8,34 pour les deux, sous 8,50 ; C).
- **La reprise d'un appel part sur la clé de son premier envoi.** Jamais sur l'autre : changer de clé après une panne serait un second tirage.
- **Le tableau est écrit à la configuration avant tout appel au modèle.** Rien n'y dépend d'une réponse, d'un solde ni d'une dépense.
- **Une seule file** : une ligne de calcul (la ligne 4), un dossier, un compteur, un plafond de 8,50 USD, un rapport. Les appels restent un à la fois, dans l'ordre.
- **Pourquoi pas une bascule sur la seconde clé quand le crédit de la première ne couvre plus la réserve** : le programme ne voit pas le solde, seulement sa dépense comptée ; et la bascule ferait dépendre de l'état de la caisse quelles lectures chaque clé sert. Le partage par rang est connu d'avance et se vérifie sur le rapport.

### 4.2 Ce que « huit lectures sur huit » juge désormais

**Ce qui reste jugé**, sans changement de seuil :
- le modèle `gemini-4-neon`, à son réglage unique, sur les huit entrées de la section 3 du devis, dans leur ordre ;
- huit réponses de code 200, reprise unique comprise, sans refus, sans fin par sortie maximale atteinte, **toutes les huit de forme conforme** ;
- une file jouée une seule fois : elle est partie à son premier envoi, sur l'une ou l'autre clé, et ne repart sur aucune ;
- une file arrêtée à son plafond ne tient pas : le plafond est celui de la file entière, 8,50 USD, tenu par un seul compteur. Il n'est pas partagé en deux moitiés, et la garantie du devis (ligne 370) reste entière.

**Ce qui n'est plus jugé, ou l'est autrement** :
1. **Une voie de service unique.** La règle 2 jugeait huit lectures servies par une clé et un projet. Chaque clé n'en sert plus que quatre. L'admission ne dit donc pas qu'un projet seul tient huit lectures de suite. **À la course, le juge devra être servi de la même façon, ou sur une clé que quatre lectures seulement auront éprouvée** : à écrire au texte.
2. **Le nom servi, par clé.** La règle 3 parle de « la vérification de la clé », au singulier. Lecture retenue : chaque réponse porte le nom servi relevé par la vérification **de la clé qui l'a servie**. Et, pour garder « un seul nom servi » (devis, ligne 365) : **si les deux vérifications relèvent deux noms servis différents, la file ne part pas ; c'est un nœud de Lazar.** Cette condition est plus stricte que le devis ; je la déclare.
3. **La sonde, par clé.** Chaque vérification porte sa sonde. Deux sondes « comprises » : la file part au régime courant. **Une seule sonde non « comprise » suffit à exiger le mot de Lazar, et la file entière part alors au régime prudent** : un seul régime de compte pour les huit lectures, le plus strict. Deux orthographes retenues différentes (niveau de réflexion, température) : la file ne part pas, nœud de Lazar.
4. **Deux causes d'échec qui ne sont pas le modèle, au lieu d'une.** Un refus propre à un projet — caisse, quota, réglage — fait échouer la file entière. « Une file coupée par le service après son premier envoi » (règle 3) se lit sur l'une ou l'autre clé.
5. **Deux vérifications, donc six envois de vérification au plus**, et deux sondes lues avant la file. Aucun choix n'en dépend : la règle de partage est déjà écrite.

**C'est un écart au texte du préenregistrement** (brouillon 43, section 3.4, règles 2, 3 et 4). Le texte permet qu'un brouillon suivant change les règles avant le premier envoi (règle 8). **Un brouillon du texte doit donc porter ces lectures, et le fichier des règles doit en être la copie, avant la première vérification de clé.** C'est l'affaire du rédacteur du texte ; cet avenant ne modifie pas le texte.

### 4.3 Comment les gardes comptent

- **Garde 1** (plafond avant l'envoi) : inchangée. Un compteur pour la file entière, quelle que soit la clé de l'envoi ; un compteur par vérification.
- **Seconde barrière** (borne d'appels du relais) : **deux relais pour la file du juge, un par clé**, chacun borné à 8 envois (quatre appels, deux envois chacun) ; un relais par vérification, borné à 3. Le devis en voulait un par ligne (ligne 400) : écart déclaré.
- **Garde 5** (nom servi) : chaque réponse est comparée au relevé de la vérification de sa clé.
- **Garde 7** (clés par leur nom) : chaque relais de Google lit une seule variable, celle que la configuration lui donne ; l'autre est absente de son environnement.
- **Garde 8** (ligne de calcul) : la ligne 2 nomme `GEMINI_API_KEY` ; la ligne 6, `GEMINI_API_KEY_2` ; la ligne 4 nomme les deux et la règle de partage.
- **Garde 9** (constat) : section 5.
- **Garde 10** (avant la file) : exige **les deux** relevés de vérification, sains, d'empreintes inscrites ; noms servis égaux ; orthographes égales ; deux sondes « comprises », sinon la pièce du mot de Lazar et le régime prudent ; et le contrôle du crédit de 4.4.
- **Garde 13** (une file ne se rejoue pas) : un dossier de la file du juge déjà parti interdit tout départ, quelle que soit la clé.
- **Garde 17** (les huit entrées) : contrôle de plus, avant tout envoi : chaque entrée part sur la clé que le tableau de 4.1 lui donne.
- **Garde 20** (lecture de la console après un envoi coupé) : maintenue, « avant toute autre ligne chez ce fournisseur », les deux clés comprises. Le lien entre clé et projet n'étant pas connu, **Lazar lit la page de facturation des deux projets**. La pièce dit de plus les recharges survenues, nombre et montant.

### 4.4 La règle exacte des seuils de crédit

Décision de Lazar : les seuils se lisent sur le solde plus la recharge automatique. Les valeurs ne changent pas : **19,76 USD** avant une vérification de clé, **16,08 USD** avant la file (devis, 6.5).

1. **Crédit compté d'un projet P**, en USD :
   `crédit compté(P) = plancher au centime de [ crédit après une recharge(P), en euros × t × 0,95 ]`
   où `crédit après une recharge(P)` est le solde vu, plus le montant d'une recharge si la page affiche un montant ; ou le solde visé par la recharge, s'il dépasse le solde vu, si la page affiche un solde visé. **Une recharge, jamais deux.** `t` est le taux en USD par euro de la pièce de constat, daté d'au plus 24 heures avant elle. 0,95 est la marge de change de 5 %.
2. **Si la valeur de la recharge n'est pas relevée** : la pièce porte `non relevé` à cette clé, et le crédit compté est le solde vu seul, converti. Ce n'est pas un repli silencieux : la valeur est nommée, le relevé de la ligne l'écrit, et le seuil se lit alors sans recharge.
3. **Avant chaque vérification de clé de Google** : `crédit compté(P) − dépense retirée ≥ 19,76`, pour **chacun des deux projets**, la dépense retirée étant lue comme au point 4. On ne sait pas quel projet porte la clé : les deux doivent passer. Avant la première vérification, aucune dépense n'est comptée, et la dépense retirée est nulle ; avant la seconde, la première a pu prendre jusqu'à 3,68 USD.
4. **Avant le premier envoi de la file**, pour chacun des deux projets : `crédit compté(P) − dépense retirée ≥ 16,08`. La dépense retirée est la plus grande des dépenses comptées sous l'une et l'autre clé depuis la pièce de constat, **si la pièce porte que les deux clés sont sur deux projets différents** (clé `google_deux_projets_distincts` à `oui` ; section 8, point ouvert 4). **Sinon, c'est leur somme.** Le seuil reste 16,08 par projet, et non une moitié : le compteur est commun, et un seul projet peut porter presque tout le plafond et l'excès.
5. **Une recharge survenue après la pièce de constat** n'est pas comptée et ne demande pas de constat neuf (contre-lecture, C-4) ; une recharge faite à la main par Lazar en demande un, comme au devis (lignes 435 et 648).
6. **Ce que la règle suppose, sans pièce** : que la recharge est créditée avant que le solde soit vide, et que le moyen de paiement passe. **Elle ne suppose plus que les deux clés sont sur deux projets différents** (contre-lecture de la version 2, C-1) : tant que la pièce ne le porte pas, la somme des deux dépenses est retirée. Si les deux clés étaient sur le même projet, ce projet porterait les deux vérifications et toute la file, soit 2 × 3,68 + 16,08 = 23,44 USD au régime prudent ; la somme retirée couvre ce cas, puisque les deux vérifications y pèsent au plus 7,36 USD.
7. **Effet chiffré de la somme** (C). Au pire, les deux vérifications ont pris 7,36 USD comptés : il faut alors un crédit compté de 16,08 + 7,36 = **23,44 USD** par projet avant la file, contre 19,76 sous la règle du plus grand (16,08 + 3,68). Sous la lecture 1 du point ouvert 2 — un solde visé d'environ 20 €, soit 19,00 × t USD comptés —, cela demande un euro d'au moins **1,2337 USD**, contre 1,0400. Si les vérifications coûtent leur attendu (0,02 USD chacune, D), l'écart entre les deux règles est de 0,02 USD.

**État au moment où j'écris** : la valeur d'une recharge n'est pas relevée, et rien ne dit que les deux clés sont sur deux projets différents : c'est donc la somme qui serait retirée. Par le point 2, le crédit compté serait le solde seul, et aucun des deux projets ne passerait 19,76 USD sans un euro à 1,3342 USD (projet B) ou 1,7436 (projet A). **Aucune ligne de Google ne peut donc partir avant que cette valeur soit dite** (section 8, point ouvert 1).

## 5. La pièce de constat, et ce que devient la garde 9

Le programme exige toujours une pièce de constat, scellée, d'empreinte inscrite à la configuration (devis, garde 9). Lazar a abandonné le constat ligne par ligne aux consoles. La pièce change donc de contenu, non d'existence.

### 5.1 Ce que la pièce porte

- les mots de Lazar à la lettre (GO-2026-11-21-66 et GO-2026-11-21-68) ;
- sa source : « deux captures de la page de facturation de l'API Gemini dans AI Studio, envoyées par Lazar à la session mère à 2026-11-21T16:24:17Z », sans les verser au dépôt (devis, ligne 520), sans identifiant de compte ;
- une ligne de taux : taux en USD par euro, source, heure en temps universel ; de préférence le taux que la console de facturation affiche, à défaut une référence publique nommée ;
- le tableau à clés fixes ci-dessous ; pour chaque ligne : clé, valeur, source (« capture » ou « levé »), heure ;
- **la liste des clés levées, recopiée en clair sous le tableau.**

« Projet A » est celui de la capture au solde de 11,93 € ; « projet B », celui de la capture au solde de 15,59 €. « Clé 1 » est lue sous `GEMINI_API_KEY` ; « clé 2 », sous `GEMINI_API_KEY_2`. `P` vaut `a` ou `b`.

| clé de la pièce | valeur admise, par programme | source |
|---|---|---|
| `google_offre_payante_projet_P` | `oui` | capture |
| `google_devise_affichee_projet_P` | `EUR` ou `USD` | capture |
| `google_credit_vu_projet_P` | un nombre, dans la devise affichée (11,93 pour A ; 15,59 pour B) ; toute chaîne refusée | capture |
| `google_recharge_automatique_projet_P` | `activée` (écart 1 : `désactivée` et `non proposée` restent admises) | capture |
| `google_autres_credits_admissibles_projet_P` | `aucun` | capture (0 €) |
| `google_credit_apres_une_recharge_projet_P` | un nombre, dans la devise affichée, au moins égal au crédit vu ; ou `non relevé` | capture, ou mot de Lazar |
| `google_partage_journaux_projet_P` | `désactivé` ; ou `non constaté, levé par GO-2026-11-21-68` | **levé** |
| `google_duree_journaux_jours_projet_P` | l'entier `7` ; ou `non constaté, levé par GO-2026-11-21-68` | **levé** |
| `google_plafond_depense_projet_P` | `aucun, par GO-2026-11-21-68` | décision de Lazar |
| `google_cle_du_projet_constate_cle_1`, `google_cle_du_projet_constate_cle_2` | `oui` ; ou `non constaté, levé par GO-2026-11-21-68` | **levé** |
| `google_deux_projets_distincts` : les deux clés sont sur deux projets différents | `oui` ; ou `non relevé` | mot de Lazar ; **non levée** |
| les six clés de Mistral du devis, et `mistral_devise_affichee` (`USD` ou `EUR`) | celles du devis | voir 5.3 |

**Compte** (C) : neuf clés par projet de Google, soit dix-huit ; deux clés de lien ; une clé des deux projets distincts ; sept de Mistral ; **vingt-huit**. Le devis en avait treize.

### 5.2 Les clés levées, nommées une à une

Six clés portent la valeur fermée « non constaté, levé par GO-2026-11-21-68 » :
1. `google_partage_journaux_projet_a`
2. `google_partage_journaux_projet_b`
3. `google_duree_journaux_jours_projet_a`
4. `google_duree_journaux_jours_projet_b`
5. `google_cle_du_projet_constate_cle_1`
6. `google_cle_du_projet_constate_cle_2`

**`google_deux_projets_distincts` n'est pas une clé levée** : `non relevé` y est une valeur admise, nommée comme telle, qui fait retirer la somme des deux dépenses (4.4, point 4). La valeur « non constaté, levé par GO-2026-11-21-68 » n'y est pas admise. Comme `non relevé` pour la recharge, elle durcit le seuil ; elle ne l'allège jamais.

**Ce que le programme doit accepter, et rien de plus** :
- la valeur levée, à la lettre, pour ces six clés et elles seules, et seulement si la configuration les nomme dans une liste fermée `cles_levees`, avec l'identifiant du GO ;
- **jamais** pour l'offre payante, la devise, le crédit vu, la recharge automatique, les autres crédits admissibles : ces cinq-là sont vues sur les captures et gardent leurs valeurs admises ;
- chaque relevé de vérification et le rapport de la file recopient la liste des clés levées et l'identifiant du GO : la levée se voit dans tout ce qui est rendu ;
- une clé manquante, une clé de plus, une valeur levée sous un autre identifiant de GO, une valeur levée sur une clé hors de la liste : refus, comme au devis (ligne 512).

### 5.3 Mistral

La ligne du registre écrit « aux consoles », au pluriel. Je ne sais pas si l'abandon vaut pour les clés de Mistral : crédit, offre payante, refus de l'entraînement, clé de l'espace, deux limites de débit. Un constat de la page de confidentialité de Mistral existe déjà au dépôt (je n'en ai vu que le nom). **Je ne lève ici aucune clé de Mistral** : elles gardent les valeurs admises du devis. Si la session établit que le mot de Lazar les couvre, elle les ajoute à `cles_levees`, une à une, par leur nom (section 8, point ouvert 3).

### 5.4 Devise et conversion

- **La devise est une clé du tableau** : écart à la proposition du vérificateur du programme, qui demandait une ligne hors tableau (`557c15da…`, section 4, point 1 ; contre-lecture, m-3). L'exigence est la même.
- **Les montants restent en euros dans la pièce**, tels que vus ; le programme convertit, avec la ligne de taux. Le devis voulait un nombre en USD (« net de toute taxe et de toute conversion de monnaie », ligne 430) : écart déclaré, qui évite une conversion faite à la main.
- **Marge de change : 5 %, décidée par Lazar.** Un crédit, un solde, une recharge comptée comme couverture : taux diminué de 5 %, centime inférieur. Une dépense vue (lecture de la console, garde 20) : taux augmenté de 5 %, centime supérieur.
- L'heure du taux est au plus 24 heures avant l'heure de la pièce qui le cite, jamais après.

## 6. Texte neuf des lignes de calcul de 11.1 touchées

Les lignes 1, 3 et 5 (Mistral) ne changent pas. Les lignes 2 et 4 sont récrites, et une ligne 6 s'ajoute. Ce qui est entre crochets se remplit à la pièce de constat ; aucune ligne n'est citée à Lazar avec un crochet ouvert. Les passages inchangés sont repris du devis à la lettre.

2. **Vérification de la clé 1 de Google** : bras A, vérification de la clé de `gemini-4-neon` lue sous `GEMINI_API_KEY`, trois appels au plus, soit trois envois au plus, sonde de borne et seconde orthographe du niveau de réflexion comprises, délai de 900 secondes par appel, plafond 1,50 USD tenu par compteur si la sortie maximale borne la réflexion, sinon excès possible d'un seul envoi de 2,18 USD au débit déclaré de 200 jetons par seconde, tout envoi sans compteur lisible étant compté à ce débit sur sa durée, ce qui arrête la ligne au premier délai, sous la supposition, non documentée, que la coupure arrête la génération et la facturation, compté à 3 et 15 USD par million, payé sur le crédit prépayé du projet de cette clé, dont la recharge automatique reste activée et qui n'a aucun plafond de dépense, par décision de Lazar (GO-2026-11-21-68) : **le solde ne borne pas la perte ; elle n'est bornée que par le compteur, à 3,68 USD sous les suppositions dites, et par rien de dur au-delà** ; conditions d'envoi : offre payante vue sur capture ; partage et durée des journaux, et lien entre la clé et son projet, non constatés, levés par le même GO ; avant la ligne, le crédit de chacun des deux projets, en euros, converti au taux diminué de 5 %, avec une recharge automatique [valeur], moins la dépense retirée de 4.4, point 4, atteint 19,76 USD ; une ligne nouvelle de vérification, sur l'une ou l'autre clé, ajoute 3,68 USD au pire cas et exige de nouveau 19,76 USD, lus comme en 4.4.

6. **Vérification de la clé 2 de Google** : même texte que la ligne 2, sous `GEMINI_API_KEY_2`, plafond 1,50 USD, excès possible d'un seul envoi de 2,18 USD ; ligne neuve, due à la file partagée entre les deux clés.

4. **File Neon** : bras A, essai d'admission du juge des deux ancres, 8 appels, 16 envois au plus, **partagés entre les deux clés par une règle fixe : rangs impairs sous `GEMINI_API_KEY`, rangs pairs sous `GEMINI_API_KEY_2`, la reprise sur la clé de son appel** ; une seule file, un seul compteur, plafond 8,50 USD tenu par compteur si la sortie maximale borne la réflexion, sinon excès possible d'un seul envoi de 7,58 USD au débit déclaré de 200 jetons par seconde : quand la file part sur un mot de Lazar, au régime prudent, où un envoi coupé à 45 minutes arrête la file sans reprise ; et, quand elle part après deux sondes « comprises », sous la supposition que la borne se comporte à 32 768 comme à 256, faute de quoi jusqu'à neuf envois peuvent porter un excès (jusqu'à 76,70 USD pour la file au débit déclaré, plafond compté compris), **que rien de dur ne borne, la recharge automatique restant activée et aucun plafond de dépense n'étant réglé, par décision de Lazar (GO-2026-11-21-68) : pire cas chez Google, pour les lignes 2, 4 et 6 telles qu'accordées, 84,06 USD, accepté** ; le tout sous la supposition, non documentée, que la coupure arrête la génération et la facturation ; compté à 3 et 15 USD par million, payé sur le crédit prépayé des deux projets ; elle ne part qu'après les deux vérifications saines, au même nom servi et aux mêmes orthographes ; « huit sur huit » se lit sur les huit lectures ensemble, quatre par clé ; conditions d'envoi : comme à la ligne 2 ; au départ de la file, le crédit de chacun des deux projets, converti au taux diminué de 5 %, avec une recharge automatique [valeur], moins la dépense retirée de 4.4, point 4, atteint 16,08 USD.

**Sommes, avec la ligne 6** (C) : plafonds, 15,25 + 1,50 = **16,75 USD** (16,50 sans la ligne 5) ; excès possibles, un par ligne, 12,74 + 2,18 = **14,92 USD** ; ensemble, **31,67 USD**. Attendu : ≈ 0,55 + 0,02 = 0,57 USD (D, pour une vérification de Google de plus).

**Chaque ligne ajoute**, comme au devis : la lecture de la console par Lazar après tout envoi coupé, avant toute autre ligne chez ce fournisseur — chez Google, sur les deux projets — ; et les empreintes du devis accepté, **de cet avenant accepté**, de la pièce de constat, du fichier des règles (lignes 3 et 4), des pages de prix, des relevés documentaires, de la pièce « goreco ».

**Avec les lignes, le geste de paiement**, à la place de la ligne 593 du devis : 9,50 USD de crédit utilisable chez Mistral, inchangé ; chez Google, aucun complément n'est demandé par cet avenant : les deux soldes vus (11,93 € et 15,59 €) et une recharge automatique par projet doivent couvrir 19,76 USD sur chaque projet ; **chaque recharge automatique est un paiement de [valeur] sans geste de Lazar**, taxe en sus s'il y en a une (S). La décision du 21 novembre de porter le solde à 23,00 USD (pièce `487b5a72…`) n'est pas reprise : je lis les mots de 17:25Z comme la retirant, et la ligne du registre porte « visée environ 20 € sur le projet de la clé », que je ne sais pas lire (section 8, point ouvert 2).

## 7. Ce que le programme doit changer

Pour le rédacteur du code. Rien n'est écrit ni essayé ici. Chaque garde changée garde un cas sain et un artefact (R5).

1. **Lignes de calcul** : une ligne de plus, la vérification de la clé 2 de Google ; même forme et même plafond que la ligne 2. Dossiers, relevés et manifestes distincts par clé.
2. **Configuration** : la variable de chaque vérification de Google ; pour la file du juge, **le tableau rang → clé de 4.1**, écrit en entier ; refus s'il manque, s'il diffère de la règle « impair, clé 1 ; pair, clé 2 », ou si une entrée n'y figure pas. Aucun défaut.
3. **Relais de Google** : un relais par clé. Chacun lit la variable que la configuration lui donne, par son nom, et refuse de partir si l'autre variable de Google est dans son environnement. À la file : deux relais, chacun borné à 8 envois ; aux vérifications : 3.
4. **Chef d'essai, file du juge** : un seul compteur et un seul plafond pour les deux clés ; chaque appel part sur le relais de sa clé ; la reprise sur le même relais. Artefacts : une reprise adressée à l'autre clé ; une entrée de rang pair adressée à la clé 1 : refus avant l'envoi.
5. **Garde 5** : nom servi comparé au relevé de la vérification de la clé de l'envoi.
6. **Garde 9, pièce de constat** : liste fermée des vingt-huit clés de 5.1 ; valeurs admises de 5.1 ; liste `cles_levees` à la configuration, avec l'identifiant du GO ; la valeur « non constaté, levé par GO-2026-11-21-68 » admise pour ces clés seulement. Cas sain : la pièce de 5.1, six clés levées. Artefacts, un par cas : valeur levée sur `google_offre_payante_projet_a` ; valeur levée sur `google_credit_vu_projet_b` ; valeur levée qui cite un autre GO ; clé levée absente de `cles_levees` ; `cles_levees` qui nomme une clé hors des six ; `google_recharge_automatique_projet_a` à une valeur hors des trois ; `google_plafond_depense_projet_a` à un nombre ; devise `GBP` ; ligne de taux absente quand une devise est `EUR` ; taux daté de plus de 24 heures, ou d'après la pièce ; `google_credit_apres_une_recharge_projet_a` sous le crédit vu ; `google_deux_projets_distincts` à la valeur levée, ou à `non` ; `google_deux_projets_distincts` absente. **L'artefact du devis « `google_recharge_automatique` à `activée` » devient un cas sain** ; les artefacts du devis sur le partage et la durée des journaux (`activé`, 55) restent des artefacts : une valeur vue et mauvaise est refusée, seule l'absence de constat est levée.
7. **Seuils de crédit** : la règle de 4.4, points 1 à 5, en décimal exact. Avant toute vérification de Google, les deux projets à 19,76 ; avant la file, les deux projets à 16,08 après retrait de la dépense retirée de 4.4, point 4 ; avant la seconde vérification, les deux projets à 19,76 après le même retrait. La dépense retirée est la plus grande des deux dépenses comptées si `google_deux_projets_distincts` vaut `oui`, leur somme si elle vaut `non relevé` ; le relevé écrit laquelle a été retirée. Cas sain : `oui`, dépenses de 3,68 et 0,02, crédit compté de 19,76 : la file part (19,76 − 3,68 = 16,08). Artefact : le même, `non relevé` : la file ne part pas (19,76 − 3,70 = 16,06). `non relevé` : le solde seul compte, et le relevé l'écrit. Artefacts : un projet sous le seuil et l'autre au-dessus ; recharge comptée deux fois ; marge de change absente de la configuration ou autre que 5 %.
8. **Garde 10** : les deux relevés de vérification, sains ; noms servis égaux ; orthographes égales ; deux sondes « comprises » ou la pièce du mot de Lazar, et alors le régime prudent pour toute la file. Artefacts : un seul relevé ; deux noms servis ; une sonde « comprise » et l'autre non, sans pièce.
9. **Garde 13** : un dossier de la file du juge déjà parti interdit tout départ, sous l'une ou l'autre clé.
10. **Garde 17** : chaque entrée sur la clé de son rang.
11. **Garde 20** : par fournisseur ; chez Google, la pièce de la lecture de la console porte la dépense vue et le solde vu **des deux projets**, en euros avec la ligne de taux, et le nombre et le montant des recharges survenues ; la dépense vue, convertie au taux augmenté de 5 %, se compare à la dépense comptée de la ligne. Refus si un projet manque.
12. **Rapport et règles** : le rapport de la file dit, par lecture, la clé qui l'a servie (par son nom de variable, jamais sa valeur) ; le programme des règles applique « huit sur huit » aux huit lectures ensemble, et le nom servi par clé ; il recopie la liste des clés levées.
13. **Relevés, manifestes, lignes de dépense** : nomment la variable ; la relecture « forme d'une clé » de la garde 7 couvre les deux variables.
14. **Gabarit de configuration, gabarit des règles, note de livraison** : à reprendre sous des noms neufs (R12). Le fichier des règles cite le brouillon du texte qui porte les lectures de 4.2.
15. **Essais** : la commande d'essai retire les trois variables de l'environnement (`env -u GEMINI_API_KEY -u GEMINI_API_KEY_2 -u MISTRAL_API_KEY`).
16. **Retiré de la version 1** : toute garde sur un plafond de dépense de console ; la pièce du contrôle du lien entre variable et projet (contre-lecture, C-5) ; la clé de la dépense du mois ; le seuil de déclenchement de la recharge.

## 8. Décisions : celles que Lazar a prises, et ce qui reste ouvert

### 8.1 Les quatre décisions de la version 1, tranchées (GO-2026-11-21-68)

| décision | ce que recommandait la version 1 | ce que Lazar a tranché | ce que cela fait |
|---|---|---|---|
| 1. plafond de dépense à la console | un plafond de 23,00 USD s'il existe | **« pas de plafond mensuel »** | pire cas de 84,06 USD sans borne dure, accepté (2.4) |
| 2. sur quelle clé jouer | une seule clé, l'autre en réserve | **« on combine les deux cles 1 et 2 comme on veut »** | file du juge partagée par rang ; deux vérifications ; « huit sur huit » jugé autrement (section 4) |
| 3. lecture des seuils de crédit | le solde seul, porté à 23,00 USD | **solde plus la recharge automatique** (« recharge automtique activee basta ») | règle de 4.4 ; la décision de porter le solde à 23,00 USD n'est pas reprise |
| 4. marge de change | 5 % (session), 2 % (vérificateur) | **5 % : « go »** ; « euros affices » | 5.4 |

Et, de plus : **« on zappe ca »**, que le registre lit « le constat ligne par ligne aux consoles est abandonné » (section 5).

Sur deux de ces quatre points, Lazar a tranché contre la recommandation de la version 1, en connaissance du pire cas, qui est inscrit au registre. Les réserves qui en découlent sont en section 9 ; je ne rouvre pas les décisions.

### 8.2 Ce qui reste ouvert

**Point 1 — Que vaut une recharge automatique, sur chaque projet ?**
- Enjeu : sans ce nombre, la règle de 4.4 ne compte que le solde, et aucune ligne de Google ne passe son seuil.
- Option 1 : la session le lit sur les deux captures, s'il y figure. Avantage : aucun mot de plus. Inconvénient : il n'y figure peut-être pas.
- Option 2 : Lazar le dit en une ligne, pour chaque projet. Avantage : sûr. Inconvénient : un aller-retour.
- Recommandation : option 1, sinon option 2. Confiance : haute. Ce n'est pas un constat de console ligne par ligne : c'est le seul nombre dont dépend la règle que Lazar a choisie.

**Point 2 — Que veut dire « visée environ 20 € sur le projet de la clé » ?**
- Enjeu : selon le sens, c'est la valeur du point 1, ou un complément que Lazar entend charger.
- Option 1 : c'est le solde que la recharge automatique vise. Alors `crédit après une recharge` vaut environ 20 € par projet, soit 19,00 × t en USD comptés (C : 20 × 0,95) : le seuil de 19,76 passe si l'euro vaut au moins 1,0400 USD ; avant la file, si les deux vérifications ont pris leur pire cas et que la somme est retirée (4.4, point 7), il faut 23,44 USD, soit un euro d'au moins 1,2337 USD.
- Option 2 : c'est un solde que Lazar portera à la main sur un projet. Alors une recharge à la main demande une pièce de constat neuve (4.4, point 5), et un seul projet est visé alors que deux jouent.
- Recommandation : la session le demande ou le lit dans son propre échange ; je ne tranche pas. Confiance : sans objet.

**Point 3 — L'abandon du constat vaut-il aussi pour Mistral, et pour la lecture de la console après un envoi coupé ?**
- Enjeu : lever une garde que Lazar n'a pas levée, ou en garder une qu'il a levée.
- Option 1 : il ne vaut que pour les conditions d'envoi de Google. Avantage : c'est la lecture la plus étroite ; les gardes de Mistral et la garde 20 restent. Inconvénient : le constat de Mistral reste dû.
- Option 2 : il vaut aussi pour Mistral. Avantage : conforme à « aux consoles ». Inconvénient : crédit et limites de débit de Mistral non constatés, alors qu'ils écartent des coupures de la file Mistral.
- Recommandation : option 1 tant que la session n'a pas la preuve du contraire, et **la garde 20 maintenue dans les deux cas** : sans solde et sans plafond, c'est la seule vue qui reste sur une coupure qui n'arrêterait pas la facturation. Confiance : moyenne sur Mistral, haute sur la garde 20.

**Point 4 — Les deux clés sont-elles sur deux projets différents ?**
- Enjeu : si oui, le partage combine bien les deux soldes, et le contrôle d'avant la file retire la plus grande des deux dépenses (4.4, point 4). Si non, ou si l'on ne sait pas, il retire leur somme, et un seul projet porte jusqu'à 23,44 USD au régime prudent.
- Option 1 : Lazar le dit en un mot, et, s'il le sait, quel projet (celui de 11,93 € ou celui de 15,59 €) porte quelle variable. Avantage : un mot, aucune lecture de console. Inconvénient : c'est une parole, non un constat.
- Option 2 : rien n'est demandé, la pièce porte `non relevé`, et la somme est retirée. Avantage : aucun aller-retour. Inconvénient : un seuil plus dur, qui peut bloquer la file (4.4, point 7).
- Recommandation : option 1. Confiance : haute. Ce n'est pas le constat ligne par ligne que Lazar a abandonné : c'est ce qu'il sait d'avoir créé les deux clés.
- Si Lazar dit aussi quel projet porte quelle variable, la pièce le porte dans son mot ; les contrôles de 4.4 restent faits sur les deux projets, et aucune clé levée ne change de valeur sans une version nouvelle.

**À faire sans décision** : la ligne de calcul 6 à demander avec les autres ; le brouillon du texte et le fichier des règles à mettre aux lectures de 4.2 avant la première vérification de clé ; la pièce de constat de 5.1 à écrire et sceller.

## 9. Réserves

1. **Aucune vérification de console.** Tout ce que cet avenant sait des comptes vient de deux captures que je n'ai pas vues, relayées par la session mère. Ce sont des images d'un instant (16:24:17Z), non un constat daté ligne par ligne.
2. **Partage et durée des journaux non constatés, sur les deux projets.** Le devis en faisait une condition d'envoi, par un mot de Lazar (« b a b go », choix 3 (b)), et le texte du préenregistrement la veut inscrite avant le premier envoi. Lazar la lève. Ce qui tient encore : les deux projets sont vus à l'offre payante ; les textes envoyés sont synthétiques (devis, ligne 3). Ce qui ne tient plus : rien ne dit que les journaux des deux projets ne sont pas partagés, ni combien de temps ils sont gardés.
3. **Lien entre chaque clé et chaque projet non constaté.** D'où les contrôles de crédit sur les deux projets à la fois (4.4). **Rien n'établit non plus que les deux clés sont sur deux projets différents** : la session mère a seulement vu que chacune liste le modèle. Si elles étaient sur le même, le partage ne combinerait rien, et ce projet porterait tout. Le contrôle du crédit couvre ce cas en retirant la somme des deux dépenses, tant que la pièce ne porte pas `oui` (4.4, point 4) ; ce `oui` serait une parole de Lazar, non un constat.
4. **Pire cas de 84,06 USD sans borne dure**, accepté. Il suppose 200 jetons par seconde au plus et une coupure qui arrête la facturation ; à 400 jetons par seconde, 162,05 USD ; sans la seconde supposition, aucun chiffre.
5. **La recharge automatique est supposée suivre** : créditée à temps, moyen de paiement accepté. Sinon un solde à court coupe la file, et le rôle du juge n'est pas pourvu, pour une raison de caisse. Avec deux projets, ce risque est pris deux fois.
6. **« Huit sur huit » sur deux clés est un écart au texte du préenregistrement**, que seul un brouillon du texte peut porter. Tant qu'il ne l'a pas fait, le programme des règles n'a pas de règle à appliquer à une file partagée.
7. **La règle de partage est mon choix**, permis par « comme on veut ». Une autre règle fixe (les quatre premières à une clé, les quatre dernières à l'autre) mettrait les deux lectures de couverture sur la même clé ; je l'écarte pour cela.
8. **La condition « noms servis égaux, orthographes égales » est plus stricte que le devis.** Elle peut arrêter avant la file un essai que le devis aurait laissé partir sur une clé.
9. **Le chiffre de 76,70 USD** est calculé par la contre-lecture, refait ici par programme (76,702), sur les coûts à trois décimales du devis, non recalculés depuis les corps réels.
10. **Les soldes en euros** sont ceux des captures, à leur heure ; ils ont pu changer.
11. **Cette version 3 n'est pas revérifiée** : le contre-lecteur doit encore dire si ses deux corrections et ses quatre mineurs sont portés.
12. **Le pire cas de 84,06 USD vaut pour les lignes 2, 4 et 6 telles qu'accordées** : toute ligne nouvelle de vérification y ajoute 3,68 USD.

## 10. Ce que j'ai ouvert

- Le mandat `mandat-redacteur-fable-programme-essais-admission-v1.md` (`d3bc3628…`), en entier.
- Le devis accepté (`421ee2e6…`, recalculée) : lignes 11 à 25, 78 à 99, 194 à 204, 299 à 452, 457 à 466, 505 à 594 ; la liste de ses titres ; la ligne 640 par recherche ; par programme, pour y confronter des citations, les lignes 5, 13, 22, 181, 183, 203, 346, 365, 400, 459 à 461, 493, 498, 499, 512, 519 à 521, 539, 599, 641, 645, 646, 648, dont seul le début des lignes 259, 493, 641, 645, 646 et 648 a été affiché.
- `verification-corrections-programme-essais-admission-livraison2-v1.md` (`557c15da…`) : section 4, et les lignes rendues par une recherche des mots de devise.
- `note-programme-essais-admission-bras-a-v1-livraison2.md` : les seules lignes rendues par la même recherche.
- `mots-de-lazar-compte-google-prepaye-bras-a-2026-11-21-v1.md`, en entier.
- `contre-lecture-avenant-1-devis-essais-admission-v1.md`, en entier.
- **Pour la version 3** : `contre-lecture-avenant-1-v2-devis-essais-admission-v1.md`, en entier ; la version 2 de cet avenant, relue par programme pour en faire la version 3 (empreinte recalculée, `3dbc747b…`). Rien d'autre ; aucun `git fetch`, aucun geste réseau.
- **`registres/go.md`, sur `origin/main` : la seule ligne GO-2026-11-21-68**, par la commande que la session mère m'a donnée. Le mandat interdit les registres ; cette lecture est faite sur sa consigne expresse, et je la déclare. La ligne porte aussi des décisions sur d'autres travaux (dommages plantés, épisodes dérivés, consultations), que j'ai vues en passant et dont je ne fais rien.
- La liste des noms de fichiers du dossier de la relance qui portent « mots-de-lazar », « constat », « note-programme », « avenant » ou « recharge », et celle du sous-dossier `constat-conditions-envoi-v1` (noms seulement).
- **Non ouverts** : les deux captures ; aucun autre registre ; aucun fichier de la liste de cloisonnement ; aucune clé ; aucun réseau ; aucun code du programme.
- Calculs et assemblage : programmes jetables du bloc-notes de la session, hors du dépôt (`calc_v2.py`, `faire_v2.py`, `faire_v2b.py`, `faire_v3.py`).

## 11. Calculs, par programme

Sortie de `calc_v2.py` (nombres décimaux exacts ; les seuils de taux sont arrondis à la quatrième décimale **par excès** ; un crédit compté, au centime inférieur). Les entrées sont les chiffres du devis : plafonds, excès, coûts d'un envoi coupé à trois décimales (8,085 et 8,142), réserves (0,507 et 0,564) ; et les soldes des captures.

```
vérification : 1,50 + 2,18 = 3,68
file, un excès : 8,50 + 7,58 = 16,08
Google, régime prudent : 3,68 + 16,08 = 19,76
sortie d'un envoi coupé : 2 690 × 200 × 15 ÷ 1 000 000 = 8,07
excès d'un envoi coupé : 8,085 − 0,507 = 7,578 ; 8,142 − 0,564 = 7,578
neuf envois coupés seuls : 9 × 8,085 = 72,765 ; 6 × 8,085 + 3 × 8,142 = 72,936
borne de la file, neuf excès : (8,50 − 0,564) + 8,142 + 8 × 7,578 = 7,936 + 8,142 + 60,624 = 76,702 ; aussi 8,50 + 9 × 7,578 = 76,702
avec la vérification : 3,68 + 76,70 = 80,38 ; avec une seconde : 84,06 ; régime prudent avec une seconde : 19,76 + 3,68 = 23,44
Mistral : 1,42 + 1,42 + 5,39 = 8,23 ; avec Google : 27,99
à 400 jetons par seconde : 1,50 + 4,85 + 8,50 + 15,65 = 30,50 ; 8,50 + 9 × 15,65 = 149,35
plafond de console : 19,76 × 1,15 = 22,7240, au demi-dollar supérieur 23
plafond de console : 23,44 × 1,15 = 26,9560, au demi-dollar supérieur 27
plafond de console : 3,68 × 1,15 = 4,2320, au demi-dollar supérieur 4,5
soldes : 11,93 + 15,59 = 27,52
taux pour 3,68 USD, compte A (11,93 €) : 0,308466 → par excès 0,3085 ; marge de 5 % : 0,3248 ; marge de 2 % : 0,3148
taux pour 12,18 USD, compte A (11,93 €) : 1,020956 → par excès 1,0210 ; marge de 5 % : 1,0747 ; marge de 2 % : 1,0418
taux pour 16,08 USD, compte A (11,93 €) : 1,347863 → par excès 1,3479 ; marge de 5 % : 1,4189 ; marge de 2 % : 1,3754
taux pour 19,76 USD, compte A (11,93 €) : 1,656329 → par excès 1,6564 ; marge de 5 % : 1,7436 ; marge de 2 % : 1,6902
taux pour 3,68 USD, compte B (15,59 €) : 0,236049 → par excès 0,2361 ; marge de 5 % : 0,2485 ; marge de 2 % : 0,2409
taux pour 12,18 USD, compte B (15,59 €) : 0,781270 → par excès 0,7813 ; marge de 5 % : 0,8224 ; marge de 2 % : 0,7973
taux pour 16,08 USD, compte B (15,59 €) : 1,031430 → par excès 1,0315 ; marge de 5 % : 1,0858 ; marge de 2 % : 1,0525
taux pour 19,76 USD, compte B (15,59 €) : 1,267479 → par excès 1,2675 ; marge de 5 % : 1,3342 ; marge de 2 % : 1,2934
taux pour 3,68 USD, compte A et B (27,52 €) : 0,133721 → par excès 0,1338 ; marge de 5 % : 0,1408 ; marge de 2 % : 0,1365
taux pour 12,18 USD, compte A et B (27,52 €) : 0,442587 → par excès 0,4426 ; marge de 5 % : 0,4659 ; marge de 2 % : 0,4517
taux pour 16,08 USD, compte A et B (27,52 €) : 0,584302 → par excès 0,5844 ; marge de 5 % : 0,6151 ; marge de 2 % : 0,5963
taux pour 19,76 USD, compte A et B (27,52 €) : 0,718023 → par excès 0,7181 ; marge de 5 % : 0,7559 ; marge de 2 % : 0,7327
contrôle : 15,59 × 1,0314 = 16,079526 (sous 16,08) ; 15,59 × 1,0315 = 16,081085
option (a2) : 15,25 + 1,50 = 16,75 ; 12,74 + 2,18 = 14,92 ; ensemble 31,67
clés : Google 7 + 5 = 12 ; Mistral 6 + 1 = 7 ; un projet 19 ; deux projets 31
--- après les décisions de Lazar (GO-2026-11-21-68) : deux vérifications, une file partagée, marge de change de 5 %
plafonds : 0,25 + 1,50 + 4,75 + 8,50 + 0,25 + 1,50 = 16,75 ; excès : 12,74 + 2,18 = 14,92
Google, régime prudent, deux vérifications : 2 × 3,68 + 16,08 = 23,44
Google, neuf excès, deux vérifications : 2 × 3,68 + 76,70 = 84,06
à 400 jetons par seconde, deux vérifications : 2 × (1,50 + 4,85) + 8,50 + 15,65 = 36,85 ; 2 × 6,35 + 8,50 + 9 × 15,65 = 162,05
pire cas des envois finis d'une clé (3 appariements, 1 couverture, 2 envois chacun, sortie à 32 768) : 2 × (3 × 0,507 + 0,564) = 4,170 ; les deux clés : 8,340 (sous 8,50)
compte A : 11,93 € × 0,95 = 11,3335 € comptés ; taux pour 19,76 sans recharge : 1,7436 ; pour 16,08 : 1,4189
   à t = 1,00 (exemple, non choisi) : 11,33 USD comptés ; recharge à compter pour 19,76 : 8,43 USD, soit 8,88 € vus
   à t = 1,10 (exemple, non choisi) : 12,46 USD comptés ; recharge à compter pour 19,76 : 7,30 USD, soit 6,99 € vus
   à t = 1,20 (exemple, non choisi) : 13,60 USD comptés ; recharge à compter pour 19,76 : 6,16 USD, soit 5,41 € vus
compte B : 15,59 € × 0,95 = 14,8105 € comptés ; taux pour 19,76 sans recharge : 1,3342 ; pour 16,08 : 1,0858
   à t = 1,00 (exemple, non choisi) : 14,81 USD comptés ; recharge à compter pour 19,76 : 4,95 USD, soit 5,22 € vus
   à t = 1,10 (exemple, non choisi) : 16,29 USD comptés ; recharge à compter pour 19,76 : 3,47 USD, soit 3,33 € vus
   à t = 1,20 (exemple, non choisi) : 17,77 USD comptés ; recharge à compter pour 19,76 : 1,99 USD, soit 1,75 € vus
clés de la pièce de constat : Google, par projet : 5 vues + 1 recharge (valeur) + 2 levées + 1 décision (plafond) = 9, deux projets 18 ; par variable : 1 levée, deux variables 2 ; deux projets distincts : 1, non levée ; Mistral 7 ; total 28 ; clés levées : 2 × 2 + 2 = 6
--- version 3 : dépense retirée (contre-lecture de la version 2, C-1)
deux vérifications au pire : 2 × 3,68 = 7,36 ; crédit compté à avoir avant la file, somme retirée : 16,08 + 7,36 = 23,44 ; plus grande retirée : 16,08 + 3,68 = 19,76
solde visé de 20 € : 20 × 0,95 = 19,00 × t ; 23,44 ÷ 19,00 = 1,233684 → par excès 1,2337 ; 19,76 ÷ 19,00 = 1,04 → 1,0400
artefact du point 7 de la section 7 : 19,76 − (3,68 + 0,02) = 16,06 (sous 16,08) ; cas sain : 19,76 − 3,68 = 16,08
```

La borne de 76,702 est écrite 76,70, comme dans la contre-lecture et au registre (84,06). Les trois lignes « plafond de console » et le compte de clés « 19 ; 31 » sont ceux de la version 1 corrigée ; ils sont sans objet depuis les décisions de Lazar, et gardés pour la trace. Les lignes de la version 3 sont ajoutées à la main à la sortie du programme, et recalculées par `faire_v3.py` (1,2337 et 1,0400 vérifiés par assertion).

## 12. Changements depuis la version 1

### Les six corrections de la contre-lecture

| correction | sort | où |
|---|---|---|
| **C-1** borne de la file au cas des neuf excès | **appliquée** : 72,94 remplacé par 76,70 comme borne de la file ; le calcul est montré ; 72,77 et 72,94 gardés comme coût des seuls neuf envois coupés. Avec les deux vérifications que la file partagée demande : 84,06 | 0 ; 2.2 ; 2.4 ; 6 ; 9 ; 11 |
| **C-2** lignes touchées non déclarées | **appliquée** : les vingt lignes du tableau de la contre-lecture, citations confrontées par programme ; un quatrième tableau pour les écarts des décisions de 17:25Z | 1.3 ; 1.4 |
| **C-3** le plafond de console n'est pas « exactement » le solde | **sans objet depuis la décision de Lazar** : aucun plafond n'est réglé. « Exactement » n'est plus écrit nulle part ; la recommandation est retirée | 2.4 ; 8.1 |
| **C-4** recharge après le constat | **appliquée** : une recharge automatique ne demande pas de constat neuf et n'est pas comptée, sauf la seule que la règle des seuils ajoute | 4.4, point 5 ; 1.3, lignes 435 et 648 |
| **C-5** contrôle exigé du lien entre variable et projet | **non appliquée, par décision de Lazar** : le constat aux consoles est abandonné, et ce lien est dit « non constaté ». Je ne peux pas exiger une lecture de console que Lazar a levée. À la place : les seuils de crédit se contrôlent sur les deux projets à la fois, et la clé `google_cle_du_projet_constate` de chaque variable est levée par son nom | 4.4 ; 5.2 ; 9, point 3 |
| **C-6** décision de Lazar du 21 novembre (23,00 USD) | **appliquée, puis dépassée** : elle est nommée ; les mots de 17:25Z, tels que je les lis, la retirent ; le sens de « visée environ 20 € » reste à dire | 6 ; 8.1 ; 8.2, point 2 |

### Les douze mineurs

| mineur | sort |
|---|---|
| m-1 seuils de taux par excès | appliqué : 1,0315 ; 1,6564 ; 0,7181 ; 1,0858 ; 0,7559 ; « au moins », non « plus de » ; ajoutés, la case du projet B à 3,68 USD et les taux à 2 % et 5 % de marge |
| m-2 « taux plausible » | appliqué : retiré |
| m-3 devise en clé du tableau | appliqué : déclaré comme écart à la proposition du vérificateur ; source préférée du taux reprise (5.1 ; 5.4) |
| m-4 le « 16 dollars » | appliqué (section 3) |
| m-5 régime prudent imposé à la file | appliqué : dit comme écart aux règles d'admission ; option non retenue (2.4) |
| m-6 bornes sous suppositions | appliqué, et refait pour deux vérifications : 36,85 et 162,05 USD à 400 jetons par seconde ; les 30,50 et 149,35 de la contre-lecture valent pour une vérification |
| m-7 « aucun réglage » | appliqué (en-tête) |
| m-8 état | **appliqué en partie** : la version 1 est dite « scellée comme brouillon ». Cette version 2 ne peut pas se dire scellée : je ne scelle rien. Elle dit « à sceller comme brouillon par la session » |
| m-9 décision 2, enjeu | sans objet depuis la décision ; ce que le mot « combiner » demandait est ce qui est fait |
| m-10 décision 4, recommandation | sans objet : Lazar a dit 5 % |
| m-11 troisième colonne de 2.2 | appliqué |
| m-12 formule de 2.3 | appliqué : supposition précisée ; moyen de paiement refusé |

Aucun mineur n'est refusé. Une correction, C-5, n'est pas appliquée, pour la raison dite.

### Ce que les décisions de Lazar de 17:25Z changent à la version 1

- **Pas de plafond de dépense** : section 2.5 de la version 1 remplacée (2.4) ; pire cas de 84,06 USD sans borne dure.
- **File du juge partagée entre les deux clés** : la recommandation « une seule clé » est retirée ; règle de partage par rang (4.1) ; effet sur « huit sur huit » déclaré (4.2) ; une ligne de calcul de plus (ligne 6) ; sommes des plafonds de 15,25 à 16,75 USD, des excès de 12,74 à 14,92 USD.
- **Seuils lus sur le solde plus une recharge** : règle exacte en 4.4 ; valeurs 19,76 et 16,08 inchangées, lues sur chaque projet.
- **Marge de change de 5 %, montants en euros dans la pièce** (5.4).
- **Constat aux consoles abandonné** : pièce de constat refaite (section 5), vingt-sept clés à la version 2, vingt-huit à la version 3, dont six levées et nommées ; clés du plafond, de la dépense du mois et du seuil de recharge de la version 1 retirées.
- **Aucun plafond de ligne, aucun excès d'un envoi, aucun seuil de crédit, aucun compte d'admission n'a changé de valeur.**

## Annexe A. L'analyse des options, écrite avant la décision de Lazar (reprise de la version 2, inchangée)

Reprise de la version 1, corrigée selon la contre-lecture. Elle est gardée parce qu'elle dit ce que chaque voie coûtait ; **elle ne vaut plus recommandation** : Lazar a choisi la file partagée, que la version 1 nommait (a1), sous une forme à une seule ligne de calcul et un seul compteur (section 4), ce qui lève les points 5 et 6 ci-dessous.

| option | ce qu'elle fait | avantage | inconvénient |
|---|---|---|---|
| **(a1) une ligne de calcul par clé, file du juge répartie** : quatre lectures sur une clé, quatre sur l'autre, une vérification par clé | deux vérifications, deux demi-files | la seule où les deux soldes s'additionnent vraiment ; aucun complément à charger | **change ce qui est jugé** (4.3) ; écart au texte du préenregistrement, donc nœud ; deux lignes de plus à accorder ; deux excès possibles au lieu d'un sur la file ; plafonds et garantie du compteur à recalculer par moitié ; textes envoyés à deux projets |
| **(a2) une ligne par clé, file entière sur une seule** : les deux clés sont vérifiées d'avance, la file part sur celle que la configuration a nommée d'avance | deux vérifications, une file | la réserve est prête si la première clé est arrêtée avant sa file par une cause qui n'est pas le modèle | 3,68 USD d'exposition de plus (plafond 1,50 et excès 2,18) ; trois envois de plus, à un second projet, donc un second constat entier ; deux sondes lues : la tentation de choisir existe, même écrite d'avance ; les soldes ne s'additionnent pas |
| **(b) une seule clé pour la vérification et la file, l'autre en réserve, non appelée** | les lignes 2 et 4 du devis, sur une variable nommée | aucun écart aux règles d'admission ; un seul projet à constater ; les gardes comptent comme au devis ; la perte calculée reste 19,76 USD | les soldes ne s'additionnent pas : le projet qui joue doit couvrir seul ses seuils, par son solde, par un complément, ou par sa recharge (décision 3 de la version 1) ; la réserve ne sert que sous une ligne nouvelle accordée par Lazar, et doit alors couvrir seule 19,76 USD |

Ce que la version 1 disait d'une file coupée en deux clés :

Le compte « huit sur huit » resterait calculable sur la réunion des deux moitiés. Mais six choses changent.
1. **L'objet jugé.** La règle 2 juge « ses huit lectures » comme une file, servie par une voie. Deux moitiés sont deux voies : deux projets, deux relevés de vérification, peut-être deux limites de débit. À la course, le juge tournera sur une clé ; quatre lectures seulement l'auront éprouvée.
2. **Le nom servi.** La règle 3 parle de « la vérification de la clé », au singulier. Si les deux relevés portent deux noms servis, la règle n'a plus de lecture.
3. **« Une file n'est jouée qu'une fois »** (règle 4) et « une file coupée par le service après son premier envoi » (règle 3) : avec deux moitiés, on ne sait plus si la seconde moitié est partie quand la première l'est.
4. **L'issue de la sonde peut différer** d'une clé à l'autre : une moitié au régime courant, l'autre au régime prudent, où un envoi coupé arrête sans reprise. Le même modèle serait jugé sous deux règles de compte.
5. **« Une file arrêtée à son plafond ne tient pas »** : le plafond de 8,50 USD devrait être partagé. La garantie du devis — un modèle dont chaque envoi reste sous 32 768 jetons de sortie n'est jamais refusé (ligne 370) — serait à recalculer pour chaque moitié, les huit entrées n'étant pas de même longueur (six d'appariement, deux de couverture). Non recalculé ici.
6. **Deux lignes, deux excès** : 7,58 USD possibles sur chacune.

Le seuil ne bouge pas ; ce qu'il mesure, si. C'est un écart au texte du préenregistrement (brouillon 43, section 3.4), que seul Lazar peut ouvrir, avant le premier envoi.

## 13. Changements depuis la version 2

Contre-lecture de la version 2 (`contre-lecture-avenant-1-v2-devis-essais-admission-v1.md`) : « engageable après corrections », légères ; deux corrections, quatre mineurs. Tous sont appliqués ; aucun n'est refusé.

| point | ce qui est fait | où |
|---|---|---|
| **C-1** dépense retirée avant la file | la **somme** des dépenses comptées sous les deux clés est retirée, tant que la pièce ne porte pas que les deux clés sont sur deux projets différents ; sinon, la plus grande. Clé neuve `google_deux_projets_distincts` (`oui` ou `non relevé`), **non levée** ; la pièce passe de vingt-sept à **vingt-huit** clés. Effet chiffré : 23,44 USD à avoir par projet au pire, soit 1,2337 USD par euro pour un solde visé de 20 € | 0, points 4 et 5 ; 4.4, points 4, 6 et 7 ; 5.1 ; 5.2 ; 6, ligne 4 ; 7, points 6 et 7 ; 9, point 3 ; 11 |
| **C-2** question manquante pour Lazar | point ouvert 4 ajouté, au texte de la contre-lecture ; « trois points » devient « quatre points » | 0, point 6 ; 8.2 |
| **m-1** « pas de plafond mensuel » | dit comme une lecture : aucun plafond de dépense, quelle que soit sa période | 2.4 |
| **m-2** pire cas et ligne nouvelle de vérification | la ligne 2 dit qu'une ligne nouvelle ajoute 3,68 USD et exige de nouveau 19,76 USD ; la ligne 4 dit « pour les lignes 2, 4 et 6 telles qu'accordées » | 6 ; 9, point 12 |
| **m-3** contrôle avant la seconde vérification | la dépense retirée s'applique aussi avant chaque vérification | 4.4, point 3 ; 6, ligne 2 ; 7, point 7 |
| **m-4** « 3 levées » par projet | lu « 2 levées et 1 décision » ; total des clés levées, six, inchangé | 11 |

**Ajouts de mon fait, déclarés** : un cas sain et un artefact chiffrés pour la dépense retirée (section 7, point 7) ; trois artefacts pour la clé neuve (section 7, point 6) ; la phrase qui dit que le point 6 de 4.4 ne suppose plus deux projets distincts.

**Rien d'autre ne change** : aucun plafond de ligne, aucun excès, aucun seuil de crédit (19,76 et 16,08 USD), aucun compte d'admission, la règle de partage par rang, les six clés levées, les 70 citations du devis.
