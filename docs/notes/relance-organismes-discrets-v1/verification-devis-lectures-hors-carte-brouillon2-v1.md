# Vérification du devis des lectures hors carte du bras A, brouillon 2 — v1

**Verdict : engageable après une correction.** Les sept corrections et les huit mineurs de ma vérification du brouillon 1 sont fermés. Les trois écarts que le rédacteur déclare sont acceptables, et deux d'entre eux corrigent une erreur de ma part. Les chiffres neufs sont justes : je les ai refaits par un programme indépendant. Les plafonds ne bougent pas : 670 USD en huit lignes, 130 au premier engagement. **La seule correction** : le brouillon ignore que la mère a retenu le régime prudent pour toutes les lignes de Google des essais (journal OD-315, R-4682). Le pire cas des essais est donc de 32,97 USD, non plus de 89,67, et l'enjeu de la décision 6 se lit sur 89,11 USD, non sur 145,81.

- **Vérificateur** : le même agent qu'au brouillon 1 (Claude Opus 5.5), le 2026-11-21 vers 20:05Z. Il n'a écrit ni le devis, ni ses programmes, ni les pièces citées. **Rien n'est scellé ni committé.**
- **Objet** : `docs/notes/relance-organismes-discrets-v1/devis-lectures-hors-carte-bras-a-v1-brouillon2.md`. Sa sha256 est `d5e814b40ad3f455d96ae849d8d59306f748c470718ea1e3aa349b0208b08939`, égale à son compagnon. Ses programmes sont dans `devis-hors-carte-programmes-v2/` : les cinq fichiers passent `sha256sum -c` (« OK »). Je ne les ai ni lus ni exécutés ; j'ai fait mes calculs avec mon propre programme.
- **Interdits** : ceux du mandat du rédacteur (`86c98be8…`). Aucun réseau, aucun `git fetch`. Du texte, je n'ai lu que la section 6.11.

## 1. Corrections et mineurs du brouillon 1 : fermés

| remarque | état dans le brouillon 2 |
|---|---|
| C-1 : avenant 2, décision 5, pire cas chez Google | fermée. La décision 5 est refaite, sans défaut, avec la borne déclarée et `outputTokenLimit`. Le 198 656 de l'option (a) est juste (4 × 49 537, porté au multiple de 1 024 supérieur). Voir la correction D-1 pour le régime prudent. |
| C-2 : marge par instrument | fermée, avec l'écart (a) du point 2, accepté |
| C-3 : sortie maximale et maxima | fermée en 3.2, 4.2, 4.4, 5.1, à la garde 3 et aux lignes 4 et 7 ; ses deux précisions sont justes |
| C-4 : ligne 7 et garde 7 | fermée : borne déclarée, `outputTokenLimit`, `CONTINUATION` |
| C-5 : clause de Google aux lignes 9 et 10 | fermée ; 4.5 dit ce que la règle exige d'un moniteur servi par Google, sans en nommer aucun |
| C-6 : lignes, réserve et arrondi | fermée ; les dix lignes font de 223 à 595 signes, comptés par programme, toutes sous 600 |
| C-7 : décision 6 | fermée, sans défaut ; correction D-1 pour son enjeu |
| m-1 à m-8 | fermés ; m-1 et m-3 par un choix du rédacteur, accepté au point 2 ; m-8 « sur la foi de la vérification », ce qui suffit |
| points 4 et 5 | repris en section 10 : qui remplit les cases du premier lecteur ; réponses aux deux questions |

La frontière du mandat tient toujours : aucun nom ni prix de moniteur, plus aucun prix d'exemple. Seules sont nommées les quatre lignes de GO permises, du 21 novembre.

## 2. Les trois écarts déclarés : acceptables

- **(a) Seuil de 24 lectures lu sur l'essai entier.** Le rédacteur a raison. Ma lettre de C-2, « moins de 24 lectures de cet instrument », contredisait ma propre C-6 : l'essai d'admission de Mistral compte 18 lectures d'appariement et 6 de couverture, si bien que la couverture serait restée à la marge 3. Enjeu, recalculé : à la ligne 4, recalculée sur une mesure qui rendrait la supposition, le plafond serait de 40 USD aux marges 2 et 2, contre 45 aux marges 2 et 3. Les deux restent sous le maximum de 55 USD. Le seuil de 1 000 lectures reste lu par instrument, ce qui était le fond de C-2. **Accepté.**
- **(b) 14 994.** C'est juste : à la réserve exacte de 1,05504 USD, la tolérance est de 14 994,17 jetons. Mon 14 990 venait de la réserve arrondie à 1,06 USD, et « environ 15 000 » aurait affirmé six jetons de trop. **Accepté.**
- **(c) Ligne 1 ramenée à 595 signes.** Le rédacteur a raison. Mon compte de 545 portait sur un texte où j'avais retiré la dernière clause ; appliquée à la ligne entière, ma C-6 donne 671 signes (compté par programme). Le texte resserré dit « réserve et arrondi compris », ce qui suffit, puisqu'il renvoie à la règle 5.1. **Accepté.**

## 3. Les deux ajouts

**Huit appels à la fois : l'ajout tient.**
- **Chiffres** : huit envois coupés font 9,94 USD ; les pires cas des lignes 4, 5 et 6 deviennent 64,94, 229,94 et 54,94 USD.
- **Crédits chez Mistral** : 75,00, 264,50, 63,50 et 402,50 USD ; avec une taxe de 20 %, 90,00, 317,40, 76,20 et 483,00.
- **Marge utile de la ligne 4** : le cumul limite est de 50,00 USD, soit 2,796 fois l'attendu, à une sortie maximale de 32 768 ; de 44,25 USD, soit 2,475 fois, à 71 680.
- **Tolérance de sortie** : 3,589 fois la supposition à un appel à la fois, 3,279 fois à huit. Le devis écrit 3,5 et 3,2, des valeurs tronquées, ce qui est cohérent.
- **Ligne 4 si la règle comptait huit réserves** : son maximum passerait à 60 USD.
- **Un point à dire, sans correction** : à huit appels à la fois, la garantie de la règle 5.1 tombe sous sa marge. Exemple : un plafond recalculé de 40 USD à la marge 2, moins huit réserves, ne laisse que 1,96 fois l'attendu. La réserve 15 du devis donne la parade : compter, dans `r`, une réserve par appel en vol. C'est un choix à soumettre à Lazar avec la décision 3, non une erreur.

**Crédit Google selon les avenants : l'ajout tient.** C'est la règle de l'avenant 2, section 3.1 : le solde seul de chaque projet, au taux diminué de 5 %, la dépense retirée.
- **Seuil d'une ligne du juge** : 28,07 USD comptés, soit 26,89 € vus par projet au taux de 1,0990.
- **Manques aux soldes vus avant les essais** : 14,96 € et 11,30 €.
- **Lignes 7 et 8 sans constat entre elles** : 53,78 €.
- **Projets portés à 31,58 €** : ils comptent pour 32,97 USD, ce qui laisse 4,90 USD de marge.
- **Artefact de la garde 12** : 26,88 € comptent pour 28,06 USD, sous le seuil, et la ligne ne part pas.

Tout cela est juste, et cohérent avec le régime prudent retenu par la mère. Au pire des essais, 32,97 USD sont retirés, et tout est à verser de nouveau, comme le devis l'écrit. **Ce qui manque** est seulement la conséquence de ce choix sur le pire cas (D-1).

## 4. Chiffres neufs recalculés

Mon programme est `verif_hc_b2.py` (sha256 `57c18bde…`). Sa sortie (`c89f6056…`) est dans le bloc-notes, `/tmp/claude-0/-home-user-controle-ia-travail/080a2aff-9781-5a4d-8af3-2aae94066157/scratchpad/verif-hc/`. Il complète celui de ma vérification du brouillon 1, dont les chiffres restent valables.

| chiffre neuf | devis | recalcul |
|---|---|---|
| réserve Mistral à 71 680 ; à 131 072 (par la borne en octets ; par la sortie maximale seule) | 1,344, 0,185 ; 2,441, 0,322 | les mêmes |
| Google à 65 536 / 81 920 / 262 144 : réserve ; débit ; majorants pour 80 et 152 appels | 1,056 / 1,301 / 4,005 ; 24,4 / 30,5 / 97,5 ; 253 et 481 / 312 et 593 / 961 et 1 826 | les mêmes |
| maximum observé toléré à l'essai | 17 920 et 20 480 | les mêmes |
| règle de plafond aux sorties maximales les plus hautes | 60 et 25 USD | les mêmes |
| maxima des lignes 5, 6 et 8 | 290 816, 278 528, 206 848 | les mêmes (calculés au brouillon 1) |
| réserve maximale du premier lecteur | 1,40 | 1,403 |
| moniteurs : sortie qui égale l'entrée ; coût par USD de prix de sortie ; réserve de Google | 955, 717, 573 ; 3,20, 12,80, 51,20 ; 0,066 × `ps` | 955,3, 716,5, 573,2 ; les mêmes ; 0,0655 |
| à 160 appels : second lecteur ; premier lecteur | 18,34 et 60 ; 27,79 et 60 | 18,343 et 60 ; 27,79 et 60 |
| juge, 24 appels de couverture parmi 72 | 4,19 | 4,19 (brouillon 1) |
| huit appels à la fois et crédits | point 3 | égaux |
| essais au régime prudent, plus les deux lignes du juge | 89,11 | 89,11, soit 5,05 au-dessus des 84,06 acceptés |

## 5. La question neuve : 128 appels

**La section 6.11 permet de trancher : 128 appels par lecteur.** Trois lectures de la même section concordent :
- « 32 par lecteur et par épreuve », sur quatre épreuves, font 128 ;
- son tableau compte 128 appels par lecteur et 256 lectures ;
- son majorant de 91 272 envois est calculé sur 25 920 lectures, qui comprennent ces 128.

Le devis de course compte de même « 4 × 32 » plans pour les épreuves mécaniques (section 6). « 160 artefacts » est donc un compte d'artefacts fabriqués, non d'appels : 32 de ces artefacts ne sont pas lus sous cette ligne. Ce que sont ces 32 se lit dans la section du texte qui définit les épreuves de l'oracle, du côté de la relance ; la mère peut la lire, pas le rédacteur. C'est **sans effet sur le devis**, qui garde 128. Il suffit d'écrire en section 10 : « réponse : 128, par la lettre de 6.11 ; ce que sont les 160 artefacts reste à dire au texte ».

## 6. Les six décisions

- **Forme** : elles sont bien posées. Chacune a sa décision, son enjeu, deux ou trois options avec avantage et inconvénient, une recommandation et une confiance.
- **Défauts** : quatre décisions sont sans défaut (1, 4, 5 et 6 : une dépense, un choix de Lazar, un mot de Lazar remplacé, un paiement) ; deux ont un défaut sous 48 heures (2 et 3), ce qui est admissible.
- **Un défaut de fond, dans la décision 6** : son enjeu est chiffré sur le pire cas sans borne dure des essais, que la mère a écarté (D-1). Elle doit aussi dire que Lazar ne verse rien de plus avant que les deux pièces soient vérifiées (journal OD-315).
- **Décision 2** : elle peut citer le précédent des essais, où la mère a retenu le régime prudent pour Google. Sa recommandation (a) le prolonge. C'est un mineur.

## 7. Correction

**D-1. Régime prudent retenu par la mère pour Google.**
- En 0, point 7, remplacer « Les deux lignes du juge ajoutent 56,14 USD, au régime prudent, au pire cas des essais, que l'avenant 2 porte à 89,67 USD quand Lazar en a accepté 84,06 (4.4 ; décision 6). » par :

  « Les deux lignes du juge ajoutent 56,14 USD, au régime prudent, au pire cas des essais. Ce pire cas est de 32,97 USD, puisque la mère a retenu le régime prudent pour les lignes de Google (journal OD-315). L'ensemble fait 89,11 USD quand Lazar en a accepté 84,06 (4.4 ; décision 6). »

- En 4.4, dernier point, et en décision 6, enjeu, remplacer « Lazar a accepté 84,06 USD pour les essais ; l'avenant 2 les porte à 89,67 sans borne dure, 32,97 au régime prudent (M). » et la phrase qui suit (« … 145,81 et 89,11 avec les essais » en 4.4 ; « … 145,81 avec le pire cas des essais, 89,11 si tout reste au régime prudent (C) » en décision 6) par :

  « Lazar a accepté 84,06 USD pour les essais. L'avenant 2 les portait à 89,67 sans borne dure ; la mère a retenu le régime prudent pour les lignes de Google, en vérification comme en file (journal OD-315, R-4682), ce qui ramène ce pire cas à 32,97 USD (M). Les deux lignes du juge ajoutent 56,14 USD au régime prudent : 89,11 avec les essais, soit 5,05 USD au-dessus du chiffre accepté (C). »

- En décision 6, ajouter à l'enjeu : « Lazar ne verse rien de plus avant que la version 2 de l'avenant 2 et ce devis soient vérifiés (journal OD-315). »
- En réserve 9, après « 32,97 au régime prudent », ajouter « , régime retenu par la mère (journal OD-315) ».

## 8. Mineurs

- n-1 : section 10, question 3 : y porter la réponse du point 5.
- n-2 : décision 3, option (b) : ajouter « et, si la règle 5.1 compte une réserve par appel en vol, un maximum de 60 USD à la ligne 4 » (réserve 15), pour que Lazar choisisse les deux ensemble.
- n-3 : réserve 9 : la version 2 de l'avenant 2 est en écriture (journal OD-315). Si elle change le taux ou les seuils, la section 6 et la décision 6 se refont, comme le devis le dit déjà.

## 9. Ce que j'ai ouvert

- **Le devis vérifié** (`d5e814b4…`), en entier.
- **Ses programmes** : leurs empreintes seulement.
- **Ma vérification du brouillon 1** (`b0f04bd5…`).
- **Le brouillon 1** du devis (`70adb048…`), pour compter la ligne 1 corrigée par ma C-6.
- **Le journal de la relance**, par `grep` du mot « prudent » seulement, pour l'entrée OD-315.
- **`git log`**, sur le dossier.
- **Rien d'autre** : aucun chemin cloisonné, aucune pièce du côté habilité, aucun réseau.
