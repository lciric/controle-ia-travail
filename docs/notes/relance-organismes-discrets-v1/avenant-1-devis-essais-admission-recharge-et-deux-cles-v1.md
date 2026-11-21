# Organismes discrets, bras A — avenant 1 au devis des deux essais d'admission : recharge automatique gardée chez Google, et deux clés de Google — note d'écart — v1

- **Objet** : dire ce que deux mots de Lazar changent au devis accepté des deux essais d'admission (`docs/notes/relance-organismes-discrets-v1/devis-essais-admission-mistral-neon-bras-a-v1.md`, sha256 `421ee2e6ec909c8b6261b3be39109aa5e76d6c275e79b4d7ec122816c83dd1bc`, recalculée ici). Le devis n'est pas réécrit : il reste tel quel, et cet avenant se lit avec lui.
- **État** : brouillon, écrit le 2026-11-21 par un rédacteur neuf (Claude Fable 5.2), qui n'a écrit ni le devis ni le programme. **Non scellé, non contre-lu, non accepté.** Il ne change rien tant que Lazar n'a pas tranché les décisions de la section 8.
- **Les deux mots de Lazar**, vers 17:10Z, inscrits sous GO-2026-11-21-66, tels que la session mère me les a relayés (je n'ai pas ouvert le registre) :
  1. « je prefere la garder allumeee pour eviter toute coupure impromptue » : la recharge automatique du crédit prépayé de Google **reste activée** ;
  2. « on va combiner les deux » : le crédit vient de **deux comptes Google, donc deux projets et deux clés**, lues sous `GEMINI_API_KEY` et `GEMINI_API_KEY_2`.
- **Ce que Lazar a vu aux consoles**, relayé de même, en euros : compte A, solde 11,93 €, recharge automatique activée, 0 € d'autres crédits Google Cloud admissibles ; compte B, solde 15,59 €, recharge automatique activée, 0 € d'autres crédits. **Pas encore relevés** : le montant et le seuil de déclenchement des recharges ; quelle clé va avec quel compte. La session mère a vérifié, par l'appel de liste seulement, que les deux clés listent `gemini-4-neon`.
- **Ce que cet avenant ne change pas** : aucun plafond de ligne (0,25 ; 1,50 ; 4,75 ; 8,50 ; 0,25 USD), aucun excès chiffré, aucun critère d'admission (22 sur 24 ; huit sur huit), aucun délai, aucun réglage, rien chez Mistral sauf une clé de devise proposée (section 5). Les seuils de 19,76 et de 16,08 USD gardent leur valeur ; **ce à quoi on les compare est une décision ouverte** (section 8, décision 3).
- Marques : (C) calculé ici ; (S) supposé, sans pièce ; (D) repris du devis.

## 0. En une page

1. **La recharge gardée retire la borne par le solde.** Le devis écrivait que la perte chez Google était bornée par le solde prépayé (23,00 USD). Ce n'est plus vrai : chaque recharge remet du crédit. Ce qui borne désormais la perte, c'est le compteur du programme, sous ses suppositions : **3,68 USD** pour la vérification de la clé, **16,08 USD** pour la file du juge au régime prudent, soit **19,76 USD** chez Google. Dans le seul cas où la file part après une sonde « comprise » et où la borne de sortie se comporte autrement à 32 768 qu'à 256, la perte calculée monte à **72,94 USD** pour la file, **76,62 USD** avec la vérification, au débit déclaré : plus rien de dur ne l'arrête.
2. **Recommandation** : si la console de Google propose un plafond de dépense qui refuse les appels au-delà, Lazar le règle à **23,00 USD** au-dessus de la dépense déjà vue ce mois-ci sur le projet qui joue. Il reprend exactement le rôle que tenait le solde de 23,00 USD, et la recharge continue d'écarter la coupure par un solde à court.
3. **Deux soldes ne s'additionnent que si la file du juge est coupée en deux clés**, et cela change ce qui est jugé (section 4). **Recommandation : une seule clé joue la vérification et la file ; l'autre reste en réserve.**
4. **Aucun des deux soldes vus ne passe seul le seuil de 19,76 USD** à un taux de change plausible : il y faudrait 1,2675 USD par euro pour le compte B, avant toute marge de change (C). Avec la recharge active, la question est de savoir si le seuil se lit sur le solde seul, ou sur le solde et une recharge (décision 3).
5. **Le constat se fait par projet** : offre payante, journaux, partage, devise, crédit, recharge (montant et seuil), plafond de dépense, clé. Treize clés deviennent dix-neuf si un seul projet de Google joue, trente et une si les deux jouent (section 5).
6. **Quatre décisions restent à Lazar** (section 8). Rien ne part avant.

## 1. Les écarts, cités à la lettre

Numéros de ligne du fichier du devis, à l'empreinte ci-dessus. Les citations sont vérifiées par programme (section 9).

### 1.1 Écart 1 : la recharge automatique reste activée

| ligne | section | ce que le devis écrit | ce que le mot de Lazar en fait |
|---|---|---|---|
| 16 | 0, point 4 | « Chez Google, la dépense est bornée par le solde prépayé, plus tout autre crédit Google Cloud admissible du compte de facturation » | faux avec la recharge active : voir section 2 |
| 24 | 0, point 12 | « Chez Google, la perte est bornée par le solde prépayé, plus tout autre crédit Google Cloud admissible du compte ; ce que fait le service au solde nul n'est pas relevé. » | de même |
| 389 | 6.4 | « **Seul le solde prépayé borne alors la perte chez Google** » | plus rien de dur ne borne ce cas, sauf un plafond de dépense réglé à la console |
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
| 422 | 6.5 | « Lazar charge ce qui manque à 23,00 au solde qu'il voit » | non fait ; remplacé par la décision 3 |
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

Les lignes 497 à 499 (offre payante, partage des journaux, durée des journaux) ne changent pas de valeur admise ; elles se constatent **pour chaque projet dont la clé reçoit un texte**, vérification comprise.

## 2. Ce qui remplace la borne par le solde

### 2.1 Ce que le solde faisait, et ce qui en reste

Le solde prépayé tenait deux rôles dans le devis.
- **Borne de la perte**, en dernier recours : si tout le reste manquait, on ne perdait que le solde, sous quatre réserves (ligne 393). **Ce rôle tombe.** Avec la recharge active, la perte possible est le solde, plus autant de recharges que le service en déclenche.
- **Cause de coupure d'une file** : « un solde à court coupe une file partie », et c'est alors la caisse qui décide, non le modèle (ligne 394). **Ce risque baisse**, et c'est ce que Lazar veut ; il ne disparaît pas : rien ne dit qu'une recharge est créditée avant que le solde soit vide (S), ni qu'un seul envoi long ne le vide pas d'un coup.

### 2.2 Perte maximale par ligne, chez Google

Rien n'est recalculé dans les trois premières colonnes : ce sont les chiffres du devis (D). Les sommes sont calculées ici (C).

| ligne de calcul | plafond tenu par la garde 1 (D) | excès possible d'un envoi en cours (6.4, D) | **plafond et excès : ce que le compteur borne** | ce que les recharges ajoutent |
|---|---|---|---|---|
| vérification de la clé de Google (ligne 2), toujours au régime prudent | 1,50 | 2,18 | **3,68** (D, ligne 383) | rien au chiffre ; le filet du solde tombe |
| file du juge (ligne 4), partie sur un mot de Lazar, régime prudent | 8,50 | 7,58 | **16,08** (D, ligne 383) | de même |
| file du juge (ligne 4), partie après une sonde « comprise », régime courant, si la borne se comporte à 32 768 comme à 256 | 8,50 | 7,58 au plus | **16,08** (D, ligne 389) | de même |
| **la même, si cette supposition manque** | 8,50 | jusqu'à neuf envois coupés | **72,77** (D), 72,94 si trois des neuf sont des envois de couverture (D, ligne 389) | **tout** : le devis bornait ce cas par le solde restant, 19,32 à 22,98 USD ; plus rien de dur ne le borne |

Totaux chez Google (C) :
- régime prudent, ou supposition tenue : 3,68 + 16,08 = **19,76 USD** ; c'est le chiffre « à couvrir » du devis, inchangé ;
- supposition manquante au régime courant : 3,68 + 72,94 = **76,62 USD** (76,45 avec 72,77) ;
- **si une seconde vérification de clé est accordée** (clé de réserve, ou ligne nouvelle après un envoi coupé) : 3,68 de plus, soit **23,44 USD** et **80,30 USD**.

Avec les lignes de Mistral, inchangées (1,42 + 1,42 + 5,39 = 8,23, D) : 8,23 + 19,76 = **27,99 USD**, le total « plafonds et excès ensemble » du devis (ligne 563), ce qui recoupe le calcul.

**Tous ces chiffres gardent les trois suppositions du devis** (ligne 384 et suivantes) : pas plus de 200 jetons par seconde ; la coupure d'un envoi arrête la génération et la facturation ; les compteurs d'un envoi fini disent ce qui est facturé. Si la deuxième manque, le devis écrivait déjà que l'excès chiffré « ne borne plus rien » ; il ajoutait « hors le solde prépayé » (ligne 386). **Ce « hors » n'existe plus.**

### 2.3 Ce que les recharges ajoutent, en formule

Soit, pour un projet, S le solde vu, T le seuil de déclenchement, M le montant d'une recharge, dans la même monnaie. Pour payer une dépense D sur ce projet, le service déclenche, si la recharge suit toujours (S) :

`nombre de recharges = 0 si D ≤ S − T ; sinon l'entier supérieur de (D − (S − T)) ÷ M`

- **Dépense attendue** (≈ 0,36 USD chez Google, D) : aucune recharge, sauf si le solde est à moins de 0,36 USD au-dessus du seuil T.
- **Chaque recharge est un paiement de M**, taxe en sus s'il y en a une (S), pris sur le moyen de paiement du compte sans geste de Lazar. Le devis n'en prévoyait aucun (ligne 447). Un crédit rechargé et non consommé n'est pas une dépense de calcul ; il reste une somme sortie.
- **La borne dure de la perte sur un projet devient** : S, plus M fois le nombre de recharges que le service permet. Si la console ne borne ni ce nombre ni la dépense du mois, **il n'y a pas de borne dure**.
- **Autre consommation du même compte de facturation** : si un autre projet ou un autre programme tire sur le même crédit prépayé, il peut déclencher des recharges et abaisser le solde pendant une ligne. À relever (2.4).

### 2.4 Ce qu'il faut relever au constat, pour chaque projet

1. le **montant de chaque recharge** (M), dans la monnaie affichée, et s'il est crédité net ou taxe déduite ;
2. le **seuil de déclenchement** (T) ;
3. **tout plafond de dépense** que la console propose — par projet, par compte de facturation, par mois — : sa valeur s'il est réglé ; s'il **refuse les appels** au-delà, ou s'il ne fait qu'**alerter** ; sur quelle période il compte ;
4. si un plafond compte par mois : la **dépense déjà vue ce mois-ci** sur ce projet ;
5. toute **limite au nombre ou au total des recharges** sur une période, si la console en écrit une ;
6. si la console dit **quand une recharge est créditée** (tout de suite, ou après un délai) : Lazar l'écrit dans son mot, que la pièce porte à la lettre, comme pour le comportement au solde nul (devis, ligne 516) ;
7. si **d'autres projets** sont liés au même compte de facturation.

Je n'ai pas vérifié ce que la console de Google propose : aucun réseau ne m'est permis, et le devis notait déjà que l'existence même de la recharge n'était pas relevée (ligne 445). Les points 3, 5 et 6 peuvent donc rendre « non proposé ».

### 2.5 Faut-il exiger un plafond de dépense côté Google à la place de la recharge coupée ?

**Oui, si la console en propose un qui refuse les appels. C'est un réglage que Lazar fait** ; la session n'a pas accès aux consoles. C'est la décision 1 de la section 8.

- **Pourquoi.** Le devis acceptait qu'une somme finie, 23,00 USD, soit « ce qui peut être perdu si tout va mal » (ligne 438). Un plafond de dépense à la console rend cette somme finie de nouveau, sans couper la recharge : la recharge écarte la coupure par un solde à court ; le plafond borne la perte.
- **Valeur recommandée**, sur le projet qui joue la vérification et la file : la dépense déjà vue ce mois-ci, plus **23,00 USD**. Calcul (C) : plafonds et excès des deux lignes, 19,76 ; avec la marge de 15 % du devis, 19,76 × 1,15 = 22,72 ; arrondi au demi-dollar supérieur, 23,00. C'est le chiffre du devis, à dessein. Si une seconde ligne de vérification est accordée sur le même projet : 23,44 × 1,15 = 26,96, soit **27,00 USD**. Sur un projet de réserve qui ne jouerait qu'une vérification : 3,68 × 1,15 = 4,23, soit **4,50 USD**.
- **En euros**, si la console règle le plafond en euros : la valeur en USD divisée par le taux diminué de la marge de change (décision 4), arrondie au centime supérieur, pour que le plafond ne soit jamais plus bas que voulu.
- **Ce que ce plafond coûte** : comme le solde de 23,00 USD dans le devis, il peut couper une file qui tiendrait, dans le cas à neuf excès (ligne 389). Le devis l'avait accepté ; cet avenant ne l'aggrave pas.
- **Un plafond qui ne fait qu'alerter n'est pas une borne** : il ne compte pas.
- **Si la console n'en propose pas** : Lazar accepte par écrit, à la ligne de calcul de la file du juge, que rien de dur ne borne le cas à 72,94 USD ; ou il impose le régime prudent du compteur à cette file (devis, section 13, point 28), ce qui ramène la borne à 16,08 USD mais arrête la file, sans reprise, sur un seul envoi coupé au délai de 45 minutes.

## 3. Les deux soldes, en dollars : ce qu'on peut dire sans taux

Aucun taux n'est choisi ici. Soit t le taux en USD par euro, et m la marge de change (décision 4). Un solde vu en euros vaut, pour les gardes : `euros × t × (1 − m)`, arrondi au centime inférieur.

| seuil du devis (USD) | ce qu'il couvre | taux t qu'il faut au compte A (11,93 €) | au compte B (15,59 €) | aux deux ensemble (27,52 €) |
|---|---|---|---|---|
| 3,68 | la vérification seule, plafond et excès | 0,3085 | — | — |
| 12,18 | la vérification, et le plafond de la file sans excès | 1,0210 | 0,7813 | — |
| 16,08 | la file du juge, plafond et excès | 1,3479 | 1,0314 | — |
| 19,76 | la vérification et la file, plafonds et excès | 1,6563 | 1,2675 | 0,7180 |

(C : seuil divisé par le solde, avec m nulle. Avec une marge m, diviser encore par 1 − m : pour m de 5 %, 1,0314 devient 1,0857, 1,2675 devient 1,3342, 0,7180 devient 0,7558.)

**Lecture.** Les deux soldes ensemble passent 19,76 USD à tout taux plausible. **Aucun ne le passe seul** sans un euro à plus de 1,2675 USD. Le compte B passe seul 16,08 USD si l'euro vaut plus de 1,0314 USD (1,0857 avec une marge de 5 %). Or un solde ne paie que les appels de la clé de son projet : la somme des deux ne vaut que si les appels sont répartis sur les deux clés.

## 4. Deux clés et deux soldes : comment les gardes comptent

### 4.1 Ce qui s'impose, quelle que soit l'option

- **Une file exige la vérification de sa propre clé** : la garde 10 veut « le relevé scellé de sa vérification », et la règle 3 du texte veut que toutes les réponses portent « le nom servi que la vérification de la clé a relevé » (devis, ligne 460). Une vérification faite sur une clé ne vaut pas pour une file jouée sur l'autre.
- **Les conditions d'envoi se constatent par projet** : offre payante, partage des journaux et durée des journaux sont des réglages de projet. Un projet dont la clé reçoit un seul texte, même à la vérification, a son constat entier.
- **La clé qui joue est écrite à la configuration avant tout appel au modèle.** Le devis pose que « la session ne choisit rien après avoir vu une réponse » (section 4, ligne 88). Choisir la clé de la file après avoir lu deux sondes serait un tel choix.
- **Une clé de réserve ne sert jamais à refaire une sonde dont l'issue a été lue**, ni à rejouer une file partie (règle 4 ; garde 13, qui doit valoir d'une clé à l'autre).

### 4.2 Les options

| option | ce qu'elle fait | avantage | inconvénient |
|---|---|---|---|
| **(a1) une ligne de calcul par clé, file du juge répartie** : quatre lectures sur une clé, quatre sur l'autre, une vérification par clé | deux vérifications, deux demi-files | la seule où les deux soldes s'additionnent vraiment ; aucun complément à charger | **change ce qui est jugé** (4.3) ; écart au texte du préenregistrement, donc nœud ; deux lignes de plus à accorder ; deux excès possibles au lieu d'un sur la file ; plafonds et garantie du compteur à recalculer par moitié ; textes envoyés à deux projets |
| **(a2) une ligne par clé, file entière sur une seule** : les deux clés sont vérifiées d'avance, la file part sur celle que la configuration a nommée d'avance | deux vérifications, une file | la réserve est prête si la première clé est arrêtée avant sa file par une cause qui n'est pas le modèle | 3,68 USD d'exposition de plus (plafond 1,50 et excès 2,18) ; trois envois de plus, à un second projet, donc un second constat entier ; deux sondes lues : la tentation de choisir existe, même écrite d'avance ; les soldes ne s'additionnent pas |
| **(b) une seule clé pour la vérification et la file, l'autre en réserve, non appelée** | les lignes 2 et 4 du devis, sur une variable nommée | aucun écart aux règles d'admission ; un seul projet à constater ; les gardes comptent comme au devis ; la perte calculée reste 19,76 USD | les soldes ne s'additionnent pas : le projet qui joue doit couvrir seul ses seuils, par son solde, par un complément, ou par sa recharge (décision 3) ; la réserve ne sert que sous une ligne nouvelle accordée par Lazar, et doit alors couvrir seule 19,76 USD |

### 4.3 Une file coupée en deux clés change-t-elle ce qui est jugé ? Oui.

Le compte « huit sur huit » resterait calculable sur la réunion des deux moitiés. Mais six choses changent.
1. **L'objet jugé.** La règle 2 juge « ses huit lectures » comme une file, servie par une voie. Deux moitiés sont deux voies : deux projets, deux relevés de vérification, peut-être deux limites de débit. À la course, le juge tournera sur une clé ; quatre lectures seulement l'auront éprouvée.
2. **Le nom servi.** La règle 3 parle de « la vérification de la clé », au singulier. Si les deux relevés portent deux noms servis, la règle n'a plus de lecture.
3. **« Une file n'est jouée qu'une fois »** (règle 4) et « une file coupée par le service après son premier envoi » (règle 3) : avec deux moitiés, on ne sait plus si la seconde moitié est partie quand la première l'est.
4. **L'issue de la sonde peut différer** d'une clé à l'autre : une moitié au régime courant, l'autre au régime prudent, où un envoi coupé arrête sans reprise. Le même modèle serait jugé sous deux règles de compte.
5. **« Une file arrêtée à son plafond ne tient pas »** : le plafond de 8,50 USD devrait être partagé. La garantie du devis — un modèle dont chaque envoi reste sous 32 768 jetons de sortie n'est jamais refusé (ligne 370) — serait à recalculer pour chaque moitié, les huit entrées n'étant pas de même longueur (six d'appariement, deux de couverture). Non recalculé ici.
6. **Deux lignes, deux excès** : 7,58 USD possibles sur chacune.

Le seuil ne bouge pas ; ce qu'il mesure, si. C'est un écart au texte du préenregistrement (brouillon 43, section 3.4), que seul Lazar peut ouvrir, avant le premier envoi.

### 4.4 Recommandation

**Option (b).** La clé qui joue est celle du compte au plus grand solde (le compte B, 15,59 €), une fois que Lazar a dit quelle variable lui correspond. L'autre reste en réserve et n'est appelée que sous une ligne nouvelle. Confiance : assez haute sur le refus de (a1), parce qu'elle touche la règle d'admission ; moyenne entre (a2) et (b), qui ne diffèrent que par le prix d'une réserve prête.

Ce que cela dit du mot « on va combiner les deux » : sous (b), les deux soldes ne s'additionnent pas. Je le signale plutôt que de l'arranger ; la décision 3 dit comment le projet qui joue peut couvrir ses seuils sans cela.

### 4.5 Comment les gardes comptent, sous l'option (b)

- **Garde 1** (plafond avant l'envoi) : inchangée, par ligne. Le compteur ne connaît pas le solde.
- **Garde 7** (clés par leur nom) : le relais de Google lit la variable que la configuration nomme, `GEMINI_API_KEY` ou `GEMINI_API_KEY_2`, et elle seule ; l'autre est absente de son environnement.
- **Garde 8** (ligne de calcul) : la ligne accordée nomme la variable ; une ligne qui nomme l'autre variable ne vaut pas.
- **Garde 9** (constat) : lit les clés du projet de la ligne. Le seuil de crédit se lit sur ce projet seul, converti (section 5).
- **Garde 10** (avant la file) : le crédit du dernier constat **de ce projet**, moins la dépense comptée des lignes de Google jouées **sur ce projet** depuis ce constat, atteint 16,08 USD, selon la lecture que fixe la décision 3.
- **Garde 13** (une file ne se rejoue pas) : un dossier de file du juge déjà parti interdit tout départ de cette file, **sur l'une ou l'autre clé**.
- **Garde 20** (lecture de la console après un envoi coupé) : reste « avant toute autre ligne chez ce fournisseur », les deux projets compris, parce que ce qu'elle éprouve — la coupure arrête-t-elle la facturation — tient au fournisseur. La console lue est celle du projet de l'envoi coupé. La pièce dit de plus **les recharges survenues depuis le constat**, nombre et montant : sans cela, un solde remonté par une recharge ne se compare à rien.

## 5. Les clés du constat à changer ou ajouter

« Projet 1 » est celui de la clé lue sous `GEMINI_API_KEY` ; « projet 2 », celui de `GEMINI_API_KEY_2`. Le lien entre ces numéros et les comptes A et B n'est pas encore connu : c'est Lazar qui le dit, par le **nom** de la variable, jamais par la valeur de la clé. `N` vaut `1` ou `2`. Le tableau ne porte que les clés des projets que la configuration nomme, celui qui joue et, s'il y a lieu, celui de réserve.

| clé du devis | devient | valeur admise, par programme |
|---|---|---|
| `google_offre_payante` | `google_offre_payante_projet_N` | `oui` (inchangée) |
| `google_partage_journaux` | `google_partage_journaux_projet_N` | `désactivé` (inchangée) |
| `google_duree_journaux_jours` | `google_duree_journaux_jours_projet_N` | l'entier `7` (inchangée) |
| `google_cle_du_projet_constate` | `google_cle_du_projet_constate_projet_N` : la clé lue sous la variable du projet N est celle du projet N constaté | `oui` |
| `google_credit_utilisable_usd` | `google_credit_utilisable_usd_projet_N` | un nombre en USD ; seuil selon la décision 3 ; toute chaîne refusée (inchangé) |
| `google_recharge_automatique` | `google_recharge_automatique_projet_N` | `activée`, `désactivée` ou `non proposée` — **écart : `activée` est admise** |
| `google_autres_credits_admissibles` | `google_autres_credits_admissibles_projet_N` | `aucun` (inchangée ; Lazar a vu 0 € sur les deux comptes) |
| — (neuve) | `google_devise_affichee_projet_N` | `USD` ou `EUR` ; toute autre valeur : nœud de Lazar |
| — (neuve) | `google_recharge_montant_usd_projet_N` | un nombre plus grand que zéro si la recharge est `activée` ; `sans objet` sinon |
| — (neuve) | `google_recharge_seuil_usd_projet_N` | un nombre, zéro ou plus, si la recharge est `activée` ; `sans objet` sinon |
| — (neuve) | `google_plafond_depense_usd_projet_N` | selon la décision 1 : un nombre (plafond qui refuse les appels), `alerte seulement`, `aucun` ou `non proposé` |
| — (neuve) | `google_depense_du_mois_usd_projet_N` | un nombre, zéro ou plus, si le plafond est un nombre ; `sans objet` sinon |
| — (neuve) | `mistral_devise_affichee` | `USD` ou `EUR` (demandée par la vérification du programme, section 4, point 1) |

**Compte des clés** (C) : le devis en a treize, dont sept de Google. Avec un seul projet de Google : les sept, renommées, plus cinq neuves, soit douze ; six de Mistral inchangées et une neuve, soit sept ; **dix-neuf**. Avec deux projets de Google : douze fois deux, plus sept, **trente et une**.

**Montants vus en euros.** La valeur inscrite au tableau reste un nombre en USD, comme le veut le devis (« net de toute taxe et de toute conversion de monnaie », ligne 430). Si la devise affichée n'est pas `USD`, la pièce porte, pour **chaque** montant de ce projet — crédit, montant de la recharge, seuil de la recharge, plafond, dépense du mois —, la ligne de conversion que le programme sait déjà lire : montant vu, taux, source, heure du taux. C'est ce que demande la vérification du programme (`verification-corrections-programme-essais-admission-livraison2-v1.md`, section 4), dont je reprends les trois points :
1. la ligne de conversion devient **obligatoire** dès que la devise affichée n'est pas `USD` ;
2. l'heure du taux est au plus **24 heures** avant l'heure de la pièce qui le cite, jamais après ;
3. une **marge de change** s'applique.

**La marge de change, `marge_de_change`**, n'est pas une clé du constat : c'est un nombre de la configuration, fixé par Lazar (décision 4). Je ne choisis pas sa valeur. Son sens, quel que soit le nombre : un crédit, un solde, un montant de recharge compté comme couverture sont convertis au taux **diminué** de la marge, arrondis au centime inférieur ; une dépense vue, un plafond de dépense, un montant de recharge compté comme exposition, au taux **augmenté** de la marge, arrondis au centime supérieur.

## 6. Texte neuf des lignes de calcul de 11.1 touchées

Les lignes 1, 3 et 5 (Mistral) ne changent pas. Les lignes 2 et 4 sont récrites ci-dessous **sous les recommandations de cet avenant** (option (b) ; plafond de dépense réglé s'il est proposé). Ce qui est entre crochets se remplit au constat ou dépend d'une décision de la section 8 ; aucune ligne n'est citée à Lazar avec un crochet ouvert. Les passages inchangés sont repris du devis à la lettre.

2. **Vérification de la clé de Google** : bras A, vérification de la clé de `gemini-4-neon` lue sous [`GEMINI_API_KEY` ou `GEMINI_API_KEY_2` : la variable écrite à la configuration avant tout appel], sur le seul projet constaté de cette clé, trois appels au plus, soit trois envois au plus, sonde de borne et seconde orthographe du niveau de réflexion comprises, délai de 900 secondes par appel, plafond 1,50 USD tenu par compteur si la sortie maximale borne la réflexion, sinon excès possible d'un seul envoi de 2,18 USD au débit déclaré de 200 jetons par seconde, tout envoi sans compteur lisible étant compté à ce débit sur sa durée, ce qui arrête la ligne au premier délai, sous la supposition, non documentée, que la coupure arrête la génération et la facturation, compté à 3 et 15 USD par million, payé sur le crédit prépayé de ce projet, dont la recharge automatique reste activée par décision de Lazar ([montant] par recharge, déclenchée sous [seuil]) ; **le solde prépayé ne borne donc plus la perte** : elle est bornée par le compteur, à 3,68 USD sous les suppositions dites, et, au-delà, par [le plafond de dépense réglé à la console de ce projet, de [valeur] | rien de dur, la console ne proposant aucun plafond de dépense qui refuse les appels] ; aucun autre crédit Google Cloud admissible au constat ; une recharge automatique est un paiement de [montant] sans geste de Lazar ; avant la ligne, le crédit vu de ce projet, converti en USD au taux diminué de la marge de change, [seul | avec une recharge] atteint 19,76 USD ; le crédit de l'autre compte ne compte pas ; une seconde ligne de vérification, après un envoi coupé, exige de nouveau 19,76 USD, lus de même.

4. **File Neon** : bras A, essai d'admission du juge des deux ancres, 8 appels, 16 envois au plus, tous sous la variable et sur le projet de la vérification de la ligne 2, plafond 8,50 USD tenu par compteur si la sortie maximale borne la réflexion, sinon excès possible d'un seul envoi de 7,58 USD au débit déclaré de 200 jetons par seconde : quand la file part sur un mot de Lazar, au régime prudent, où un envoi coupé à 45 minutes arrête la file sans reprise ; et, quand elle part après une sonde « comprise », sous la supposition que la borne se comporte à 32 768 comme à 256, faute de quoi jusqu'à neuf envois peuvent porter un excès (72,77 USD au débit déclaré), **que le solde prépayé ne borne plus, la recharge automatique restant activée par décision de Lazar** ([montant] par recharge, déclenchée sous [seuil]) : ce cas n'est borné que par [le plafond de dépense réglé à la console de ce projet, de [valeur], au risque de couper une file qui tiendrait | rien de dur, ce que Lazar accepte en accordant la ligne] ; aucun autre crédit Google Cloud admissible au constat ; le tout sous la supposition, non documentée, que la coupure arrête la génération et la facturation ; compté à 3 et 15 USD par million, payé sur le crédit prépayé de ce projet ; au départ de la file, le crédit du dernier constat de ce projet, converti au taux diminué de la marge de change, moins la dépense comptée des lignes jouées sur ce projet, [seul | avec une recharge] atteint 16,08 USD, soit le plafond de la file et un excès.

**Avec les lignes, le geste de paiement**, à la place de la ligne 593 du devis : 9,50 USD de crédit utilisable chez Mistral, inchangé ; chez Google, [aucun complément : le crédit vu du projet qui joue et une recharge automatique couvrent 19,76 USD | un complément qui porte le crédit du projet qui joue à 19,76 USD au moins, converti au taux diminué de la marge de change ; à 23,00 USD pour garder la marge de 15 % du devis] ; la recharge automatique peut de plus prélever [montant] chaque fois que le solde passe sous [seuil] ; 20 % de plus si une taxe s'ajoute (S).

**Si Lazar veut une réserve prête** (option (a2)), une ligne de plus, à accorder à part : « **6. Vérification de la clé de Google, clé de réserve** : même texte que la ligne 2, sous l'autre variable et sur son projet, plafond 1,50 USD, excès possible de 2,18 USD ; elle ne sert pas à refaire une sonde dont l'issue a été lue, et la file ne part sur cette clé que sous une ligne nouvelle. » Somme des plafonds avec elle (C) : 15,25 + 1,50 = **16,75 USD** ; excès, 12,74 + 2,18 = **14,92 USD** ; ensemble, **31,67 USD**.

## 7. Ce que le programme doit changer

Pour le rédacteur du code. Rien n'est écrit ni essayé ici.

1. **Configuration** : une entrée qui nomme la variable de la clé de Google de chaque ligne (`GEMINI_API_KEY` ou `GEMINI_API_KEY_2`) et le numéro de son projet ; refus si elle manque, si elle porte un autre nom, ou si la file du juge et sa vérification ne nomment pas la même.
2. **Relais de Google** : lit la variable nommée par la configuration, par son nom ; refuse de partir si l'autre variable de Google est dans son environnement (garde 7 : cas sain, une seule variable ; artefact, les deux présentes, et la variable nommée absente).
3. **Liste fermée des clés du constat** : celle de la section 5, par projet nommé à la configuration ; une clé d'un projet non nommé est une clé de plus, donc refusée (garde 9).
4. **Valeurs admises** : `google_recharge_automatique_projet_N` admet `activée` ; si elle l'est, montant et seuil sont des nombres ; sinon `sans objet`. **Artefacts neufs de la garde 9** : recharge `activée` sans montant ; montant à zéro ; seuil à une chaîne ; devise `GBP` ; devise `EUR` sans ligne de conversion ; plafond de dépense à `alerte seulement` ou `aucun` quand la décision 1 exige un nombre ; plafond en nombre sans dépense du mois ; `google_cle_du_projet_constate_projet_1` à `oui` quand la ligne nomme `GEMINI_API_KEY_2`. L'artefact du devis « `google_recharge_automatique` à `activée` » est retiré et devient un cas sain, **ce qui est un écart à la garde 9 du devis**.
5. **Conversion** : ligne de conversion obligatoire dès que la devise affichée n'est pas `USD`, pour chaque montant du fournisseur — constat, mot sur la sonde, lecture de la console — ; heure du taux au plus 24 heures avant l'heure de la pièce, jamais après ; `marge_de_change` lue à la configuration, refus si elle manque ; sens de la marge selon la section 5. Les artefacts `test_v4_…` et `test_v5_…` de la vérification doivent alors être refusés.
6. **Seuils de crédit** (gardes 9, 10 et 20) : lus sur le projet de la ligne ; selon la décision 3, comparés au crédit seul, ou au crédit plus un montant de recharge. Le choix est un champ de la configuration, sans défaut : refus s'il manque.
7. **Garde 10** : la dépense comptée est celle des lignes de Google jouées **sur le même projet** depuis le constat de ce projet.
8. **Garde 13** : le départ de la file du juge est refusé si un dossier de cette file est déjà parti, sous l'une ou l'autre variable.
9. **Garde 20** : reste par fournisseur ; la pièce de la lecture de la console nomme le projet, et porte le nombre et le montant des recharges vues depuis le constat ; refus si ces deux champs manquent chez Google.
10. **Plafond de dépense** (si la décision 1 l'exige) : la garde 9 refuse un plafond plus bas que la dépense du mois plus la somme des plafonds et des excès des lignes de ce projet, et plus haut que cette somme majorée de la marge de 15 %, arrondie au demi-dollar supérieur (23,00 USD pour les lignes 2 et 4).
11. **Relevés, rapports, manifestes, lignes de dépense** : nomment la variable et le projet, jamais la valeur de la clé ; la relecture « forme d'une clé » de la garde 7 couvre les deux variables.
12. **Gabarit de configuration et note de livraison** : à reprendre sous un nom neuf (R12) ; chaque garde changée garde un cas sain et un artefact (R5).
13. **Essais** : la commande d'essai retire les deux variables de Google de l'environnement (`env -u GEMINI_API_KEY -u GEMINI_API_KEY_2 -u MISTRAL_API_KEY`).

## 8. Décisions restant à Lazar

Chacune change la lecture d'un seuil, d'une garde ou d'une ligne du devis accepté : ce sont des nœuds, sans défaut à 48 heures.

**Décision 1 — Faut-il un plafond de dépense à la console de Google, maintenant que la recharge reste activée ?**
- Enjeu : avec la recharge, plus rien de dur ne borne la perte chez Google ; le cas calculé le plus haut est 76,62 USD, et rien ne borne le cas où la coupure d'un envoi n'arrête pas la facturation.
- Option 1 : Lazar règle, sur le projet qui joue, un plafond qui refuse les appels, à 23,00 USD au-dessus de la dépense du mois. Avantage : rend à la perte la borne que le devis acceptait, sans toucher la recharge. Inconvénient : peut couper une file qui tiendrait dans le cas à neuf excès, comme le solde le faisait ; n'existe peut-être pas à la console.
- Option 2 : aucun plafond ; Lazar accepte par écrit, à la ligne de la file du juge, le cas à 72,94 USD sans borne dure. Avantage : aucune coupure par la caisse. Inconvénient : perte non bornée si une supposition manque.
- Option 3 : aucun plafond, et le régime prudent du compteur imposé à la file du juge. Avantage : borne tenue par le programme, 16,08 USD. Inconvénient : un seul envoi coupé au délai arrête la file sans reprise, et le juge peut échouer pour une règle de compte ; cela va contre le mot « éviter toute coupure impromptue ».
- Recommandation : option 1 si la console la propose, sinon option 2. Confiance : moyenne, parce que je n'ai pas pu vérifier ce que la console propose.

**Décision 2 — Sur quelle clé jouent la vérification et la file du juge ?**
- Enjeu : deux soldes ne s'additionnent que si la file est coupée en deux, ce qui change ce que la règle « huit sur huit » juge.
- Option (a1) : file répartie, quatre et quatre. Avantage : les soldes s'additionnent. Inconvénient : écart au texte des règles d'admission ; deux lignes de plus.
- Option (a2) : les deux clés vérifiées, file entière sur celle nommée d'avance. Avantage : réserve prête. Inconvénient : 3,68 USD d'exposition et un constat de plus ; les soldes ne s'additionnent pas.
- Option (b) : une seule clé joue, l'autre n'est pas appelée. Avantage : aucun écart aux règles, un seul constat. Inconvénient : les soldes ne s'additionnent pas.
- Recommandation : (b), sur la clé du compte B. Confiance : assez haute contre (a1), moyenne entre (a2) et (b).
- À dire avec la décision : quelle variable, `GEMINI_API_KEY` ou `GEMINI_API_KEY_2`, appartient au compte B.

**Décision 3 — Avec la recharge activée, les seuils de 19,76 et de 16,08 USD se lisent-ils sur le solde seul ?**
- Enjeu : aucun des deux soldes ne passe seul 19,76 USD. Le seuil servait à ce que la caisse ne coupe pas une file partie, qui ne se rejoue pas.
- Option 1 : solde seul, comme au devis ; Lazar complète le projet qui joue. Avantage : ne dépend d'aucun comportement non relevé de la recharge ; aucun changement de lecture. Inconvénient : un complément à payer ; le crédit de l'autre compte ne sert pas.
- Option 2 : solde plus **une** recharge, montant relevé au constat. Avantage : aucun complément si le montant suffit. Inconvénient : suppose que la recharge est créditée avant que le solde soit vide, ce qui n'est pas relevé ; si elle tarde, la file est coupée par la caisse et le rôle du juge n'est pas pourvu.
- Option 3 : plus de seuil de solde, la recharge suffit. Avantage : le plus simple. Inconvénient : le même, sans aucun contrôle.
- Recommandation : option 1 ; option 2 seulement si la console écrit que la recharge est créditée tout de suite, et que Lazar le porte dans son mot. Confiance : moyenne. Les valeurs 19,76 et 16,08 ne changent dans aucune option.

**Décision 4 — Quelle marge de change sur les montants vus en euros ?**
- Enjeu : un taux est une parole datée ; un solde converti juste au seuil peut passer dessous avant la file.
- Option 1 : 5 %, la recommandation de la session mère. Avantage : couvre un mouvement de cours de plusieurs jours. Inconvénient : écarte un solde qui passerait de peu.
- Option 2 : 2 %, la proposition du vérificateur du programme. Avantage : moins de crédit immobilisé. Inconvénient : marge mince si le constat précède la file de plusieurs jours.
- Option 3 : aucune. Avantage : aucun. Inconvénient : un seuil lu sans marge sur un taux qui bouge.
- Recommandation : je ne choisis pas la valeur, selon ma consigne ; la session recommande 5 %. J'écarte seulement l'option 3. Confiance sur ce seul point : haute.

**À relever par Lazar, sans décision** : montant et seuil de chaque recharge ; plafond de dépense proposé ou non, et s'il refuse ou alerte ; dépense du mois ; moment où une recharge est créditée ; autres projets sur le même compte de facturation (2.4).

## 9. Réserves

- **Ce que la console de Google propose n'est pas vérifié** : plafond de dépense, limite des recharges, délai de crédit. Tout ce qui en dépend est écrit sous condition.
- **Le lien entre variable et compte repose sur la parole de Lazar** : la session ne lit jamais une clé et ne peut pas le confirmer. Une variable prise pour l'autre ferait valoir le constat d'un projet pour les envois d'un autre. Parade possible, non exigée ici : après la vérification, Lazar regarde sur quel projet la dépense apparaît.
- **Les chiffres en euros sont une parole relayée**, non un constat daté et scellé. Ils ne servent ici qu'aux taux de la section 3.
- **Le chiffre de 72,94 USD** est repris du devis (ligne 389), qui le dit « calculé ici », sans contre-vérification par sa contre-lecture ; 72,77 est le chiffre contre-lu.
- Cet avenant n'a pas été contre-lu (R2).

## 10. Ce que j'ai ouvert

- Le mandat `mandat-redacteur-fable-programme-essais-admission-v1.md` (empreinte recalculée, `d3bc3628…`), en entier, dont la section « Interdits absolus ».
- Le devis accepté (`421ee2e6…`, recalculée) : lignes 11 à 25, 78 à 99, 194 à 204, 299 à 452, 457 à 466, 505 à 594 ; la liste de ses titres ; la ligne 640 par recherche.
- `verification-corrections-programme-essais-admission-livraison2-v1.md` (`557c15da…`, recalculée) : section 4 en entier, et les lignes rendues par une recherche des mots de devise.
- `note-programme-essais-admission-bras-a-v1-livraison2.md` : les seules lignes rendues par la même recherche (section 3, solde en euros).
- `mots-de-lazar-compte-google-prepaye-bras-a-2026-11-21-v1.md`, en entier.
- La liste des noms de fichiers du dossier de la relance qui portent « mots-de-lazar », « constat », « note-programme », « avenant » ou « recharge », et la liste des noms du sous-dossier `constat-conditions-envoi-v1` (noms seulement, aucun contenu, la capture d'écran non ouverte).
- **Non ouverts** : aucun registre, aucun fichier de la liste de cloisonnement, aucune clé, aucun réseau, aucun code du programme. Les deux variables de Google ne sont nommées ici que par leur nom.
- Calculs : un programme jetable, hors du dépôt, pour les quotients et les sommes des sections 2 et 3, et pour confronter chaque citation de la section 1 à sa ligne du devis.
