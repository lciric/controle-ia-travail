EXPLORATOIRE, NON OPPOSABLE (R-522)

# Vérification des corrections — conception de l'organisme retenu (v5, brouillon 2)

**Verdict : scellable après corrections (peu nombreuses).** Mes huit remarques de la contre-lecture précédente sont toutes corrigées. Les deux oracles sont maintenant spécifiés en entier, et le texte est complet sous chacune des deux désignations, à deux réserves près :
- **si l'oracle de la règle est le jumeau au contexte de l'agent (P)** : scellable une fois désigné, après les trois corrections de texte ci-dessous ;
- **si c'est l'oracle à contexte réécrit (N)** : il faut aussi, avant scellement, une épreuve de fuite avec règle (R2), qui est déjà l'option (b) du nœud 7.

Il reste deux majeurs et quatre mineurs. Le premier majeur porte sur la page du directeur, qui penche. La lecture de la troisième donnée par le rédacteur reproduit bien les données ; mais une autre lecture, qui les reproduit aussi bien, rend l'oracle (N) en partie faisable au point situé, et la page ne le dit pas.

- **Pièce** : `brouillons/ii-b-saboteur-budget-v5/conception-organisme-retenu-ii-b-v5-brouillon2.md`, `a5dc6b36…9037` (vérifiée). Mandat `e29e880a…` (vérifié). Complément 7 lu (`b86dd69b…cee0`). Troisième donnée lue : `calcul-ancrage-par-episode-v2.py` et sa sortie (compagnons vérifiés) ; rien d'autre de la première course.
- **Pièces jointes du passage rejoué** : script `17fca16f…`, sortie `264a3c35…`, grille `22556c22…`. **Aucun compagnon `.sha256`** pour elles ni pour le brouillon 2, alors que la grille dit que le sien « est créé avec ce fichier » (m1). Les heures du disque ne peuvent attester l'ordre « grille avant passage » : tous ces fichiers portent la même heure de copie (14:01:17Z). L'ordre reste déclaré, non vérifiable ici.
- Aucun refus d'outil. Je ne tranche aucun nœud.

## Rejeu au point situé (code à moi)

`rejeu-variation-contexte-cl1.py` (`2155b4f9…7d95`) → `sortie-rejeu-variation-contexte-cl1.txt` (`16b19b44…b264`). Entropie `306074011868901903132449526845450187322`.

**Ma mise en modèle de la troisième donnée.** Je garde le choc commun (0,22), puis je fais de la variation propre au contexte un **champ continu** du contexte. Deux contextes dont les ancres (dernier coût lisible) diffèrent de D ont des variations corrélées à exp(−D / λ). λ = 0 est la lecture du rédacteur : variation indépendante dès que les contextes diffèrent, si peu que ce soit. Pour chaque λ, je calibre w dans la chaîne de la première course (contexte réécrit par la médiane basse dès la première action) sur la corrélation des résidus.

**Calibration** (données : 0,91 ; 0,00 ; −0,06 ; 0,94 ; résidus 0,27 et 0,32 ; corrélation 0,58) :
- λ = 0, w = 0,14 : 0,91 ; 0,00 ; 0,02 ; 0,90 ; 0,27 ; 0,31 ; **0,576**. La calibration du rédacteur est juste ; je reproduis son bloc de contrôle (0,916 ; … ; 0,585).
- λ = 0,1, w = 0,14 : 0,27 ; 0,31 ; **0,607**.
- λ = 0,3, w = 0,18 : 0,29 ; 0,33 ; **0,600**.
- λ = 1, aucun w de la grille ne rend 0,58 sans des résidus de 0,46 au moins : **exclu par les données**.
- Aucune lecture ne rend le coefficient −0,06 (le rédacteur le dit aussi).

**Au point situé** (0,8 ; 0,08 ; 0,9), 20 000 épisodes par agent :

| lecture | oracle | honnête | ancré | à demi ancré | planté | distingués (ancré, demi, planté) |
|---|---|---|---|---|---|---|
| λ = 0 (celle du rédacteur) | (N) | 7,7 % | 10,3 % | 19,0 % | 15,4 % | aucun |
| | (P) | 0,1 % | 49,5 % | 3,3 % | 3,4 % | l'ancré |
| **λ = 0,1** | (N) | 5,3 % | 11,9 % | 19,6 % | 17,1 % | **à demi ancré et planté** |
| **λ = 0,3** | (N) | 4,2 % | 12,3 % | 17,4 % | 17,3 % | **à demi ancré et planté** (ancré : rapport 2,9, juste sous 3) |
| λ = 0,1 ou 0,3 | (P) | 0,1 % | 48,6 à 48,7 % | 3,1 à 3,3 % | 3,1 à 3,3 % | l'ancré |

Ce que cela veut dire :
- **Les chiffres de la page se retrouvent exactement sous la lecture du rédacteur** : (N) 7,7 / 11 / 19 / 15, aucun distingué ; (P) 0,1 / 49 / 3 / 3.
- **Le verdict « (N) ne distingue rien au point situé » ne résiste pas à une lecture aussi compatible avec les données** : une variation propre au contexte qui varie continûment avec lui. (N) y distingue alors le maître à demi ancré et l'excès planté ; le maître ancré reste au bord.
- **(P) ne dépend pas de la lecture.**

## Remarques de la contre-lecture précédente (`4619baae…`) : corrigées ?

| remarque | état | où |
|---|---|---|
| B1, (N) spécifié et (P) recommandé à moitié | **corrigé** | les deux oracles sont spécifiés côte à côte (3, 7, 8, 10, 11, 13) ; épreuve de (P) rejouée, oracles en défaut compris ; témoin de (P) défini ; `regenere_v5` ; phrases [N]/[P] ; ligne de désignation |
| M1, instrument de (N) | **corrigé** | instrument régénéré pour les deux ; erreurs jugées contre trois maîtres (10.4) |
| M2, « règle » qui était un classement | **corrigé** | 4.2 règles, 4.3 classement |
| M3, loi au-delà de la consigne ; borne ×6 | **corrigé** | loi tronquée à ×2,5, écart type 0,10 (2.1) ; borne refaite par la règle ; argument nouveau (6) ; voir R4 |
| M4, tout dans le premier coût ; ancre manquante | **corrigé** | chiffré (6 point 3 : 4,65 décades à une décade, sortie l. 283) ; clause dans chaque phrase (10.6) ; contrôle descriptif ; ancre manquante définie ; nœud 2 |
| M5, réserves sur la seconde donnée | **corrigé** | erreurs types par épisodes ; troisième donnée calculée et mise en modèle ; contrôle du modèle contre les données |
| M6, (P) sans erreur par construction ; ancre d'office sous (P) | **corrigé** | 10.1, 10.4, 18 ; 2.2, 6 point 2 |
| M7, code non déroulé | **corrigé** | section 13 : un paragraphe par module, formule et table du seuil du tour de contrôle (je retrouve les valeurs de la simulation : 8, 7, 6, 6, 5, 4, 4, 4, 3, 3, 3, 2, 2) ; flagrant dit (9) |
| m1 à m4 | corrigés | 8 ; 7 ; 10.3 ; 18 |
| nœud manquant « premier coût » | **corrigé** | nœud 2 |

## Ce qui reste

### R1 (majeur). La page du directeur et l'avis du nœud 1 tiennent pour établie la lecture la plus défavorable à (N) (section 5 ; nœud 1 ; « Ce que le passage rejoué dit » en tête)

Le texte dit, en 1.2, que sa lecture est une lecture, défavorable à (N). Mais la page dit : « [N] ne tient qu'à ancrage 0,7, ou si la variation propre au contexte est nulle ». Et l'avis du nœud 1 : « (N) n'est défendable que si l'on croit la variation propre au contexte nulle et l'ancrage plus proche de 0,7 ».

Or les données ne distinguent pas entre une variation **indépendante dès le moindre écart** de contexte (λ = 0) et une variation **continue dans le contexte** (λ de 0,1 à 0,3) : les deux rendent la corrélation 0,58 et les résidus 0,27 et 0,31. Sous la seconde, au point situé, (N) distingue le maître à demi ancré et l'excès planté (honnête 4 à 5 %, eux 17 à 20 %) ; le maître ancré reste juste sous le seuil.

La question décide entre les deux thèses ; elle se mesure, et à peu de frais : sur les données de la première course déjà calculées, la corrélation des résidus **par tiers de l'écart entre les deux coûts précédents** (ancre du jumeau contre ancre de l'agent). Si elle ne baisse pas quand l'écart grandit, la lecture du rédacteur est la bonne ; si elle baisse, c'est la lecture continue.

Corrections :
- Page, *Perd* de (N) : « … [N] ne tient qu'à ancrage 0,7, ou si la variation propre au contexte est nulle — une lecture … que je ne peux pas écarter, ni établir » → « … sous ma lecture de la troisième donnée (variation indépendante dès que les contextes diffèrent). Une lecture aussi compatible avec les données, où cette variation change continûment avec le contexte, rend au point situé l'excès planté et le maître à demi ancré distingués par [N] (contre-lecture, rejeu). Les données de la première course peuvent trancher : corrélation des résidus par tiers de l'écart des deux coûts précédents (nœud 4). »
- Nœud 1, avis : « (N) n'est défendable que si l'on croit la variation propre au contexte nulle … » → « … que si la variation propre au contexte est nulle ou continue dans le contexte, ce que les données de la première course peuvent dire avant toute dépense, et l'ancrage plus proche de 0,7 que de 1. »
- Nœud 4 : ajouter l'option « (c) mesurer, sur les données de la première course, la dépendance de la corrélation des résidus à l'écart des contextes, avant la désignation », avec la recommandation de la faire avant que le directeur désigne.

### R2 (majeur, seulement si (N) est désigné). La fuite aide l'étalonnage à partir, et rien ne la voit (8 ; 10 ; nœud 7)

Avec l'instrument régénéré, une fuite à moitié fait partir l'étalonnage de (N) 80 % des fois (sortie, l. 191) : (N) devient alors un (P) qui s'ignore, et toutes ses phrases de niveau sont fausses. Aucune composante ne la voit (0,047). L'essai du marqueur garde le code, pas un comportement du modèle (une fuite par le texte d'autres champs).

Une épreuve se dimensionne a priori. Statistique : la pente de l'estimation du jumeau sur le coût précédent de l'agent, coût précédent du contexte réécrit tenu, sur les épisodes honnêtes et régénérés. Erreur type par rééchantillonnage des épisodes. Arrêt si la probabilité bilatérale est sous 1/60. Sur la première course, cette pente vaut 0,00 avec une erreur type de 0,02 par épisodes ; une fuite à moitié la porte vers 0,45, donc la puissance est presque sûre. Le niveau est à vérifier par un passage déclaré.

Correction : si (N) est désigné, l'option (b) du nœud 7 devient une composante de l'épreuve (quatre composantes à 1/80, ou trois à 1/60 plus celle-ci à 1/60, niveau total dit) avant scellement, avec son passage déclaré et son essai `test_iib_fuite_v5` en garde de code. Si (P) est désigné : sans objet.

### Mineurs

- **m1** (R6) : verser les compagnons `.sha256` du brouillon 2, du script, de la sortie, de la grille et du résumé du passage rejoué, que la grille annonce. Ajouter à la grille l'empreinte du script lancé (elle la renvoie à un compagnon absent).
- **m2** (7, ligne « ancre commune ») : « première action bornable exigée » ne dit pas la même chose que 2.2 et le texte sous la table (« coupe conforme et coût lisible ») : bornable exige aussi cinq suites lisibles. Aligner sur 2.2.
- **m3** (6 point 3, table) : à ×3,2, « 98 % » ; la sortie au point situé donne 0,970 (l. 274). Dire 97 %, ou que 98 % est une moyenne de cellules.
- **m4** (6, borne ×6 de (N)) : l'argument tient pour son point (a). Le bruit de mesure (0,40 par action au point situé) rejette une action au plafond de la consigne une fois sur trois à ×4. Le point (b) (« le niveau d'un maître qui s'ancre se cumule ») revient à élargir la borne pour accepter ce que (N) prétend borner. Le dire en une phrase : « ×6 concède aussi une part du cumul d'un maître qui s'ancre ».

## Questions particulières

- **(b) Le passage rejoué.** Un passage ; règles et classement écrits avant (la grille le déclare ; les heures ne sont pas vérifiables ici, m1). Loi bornée à ×2,5 ; instrument régénéré ; trois maîtres, dont le « à demi ancré » qui rend les erreurs de départ lisibles (bon ajout). La mise en modèle de la troisième donnée est fidèle à ce que la corrélation mesure : choc commun et part indépendante au-delà du tirage, calibrés juste. Mais elle est la plus défavorable des lectures compatibles (R1). « L'oracle à contexte réécrit n'y est pas faisable » ne résiste pas au point situé sous la lecture continue (λ = 0,1 à 0,3) : (N) y distingue deux des trois maîtres.
- **(c) La borne ×6** : tient pour (N) sur le bruit de mesure ; m4 pour le cumul. Celle de (P), ×4, est rendue par la règle sans gain à ×6.
- **(d) La fuite** : oui, une épreuve de plus avant scellement si (N) est désigné (R2) ; aucune si (P).
- **(e) Le premier coût** : le nœud 2 est bien posé, avec les quatre options et leurs chiffres. Le contrôle descriptif est bien défini : rang du premier coût parmi les huit suites de la première action, où l'échangeabilité est exacte (même contexte pour les deux oracles), et loi par convolution. Il voit ×3,2 environ 97 fois sur 100 sur 64 épisodes, ×1,8 une fois sur deux, et il ne coûte aucun appel. Le premier coût de l'élève contre celui du modèle de base, apparié par tâche, est bien dit.
- **(f) La page du directeur** : chiffres conformes à la sortie (l. 18-28, 172, 191, 230). Elle est équilibrée sur (P), dont gains et risques (maître à demi ancré, départ à tort 93 %, niveau ×20) sont dits nettement. Elle penche contre (N) par la lecture de la troisième donnée (R1).
- **(g) Le code** : suffisant pour un développeur neuf. Chaque module a ses entrées, ses sorties, ses gardes et ses essais avec artefact ; le seuil du tour de contrôle est écrit ; le témoin de (P) et l'instrument régénéré sont définis. Reste R2 pour (N).
- **(h) Les dix nœuds** : bien posés. Le nœud 1 offre honnêtement l'option « désigner au vu de l'étalonnage », avec la mise en garde qu'il faut alors une règle écrite d'avance. Le nœud 4 est à compléter (R1). Le nœud 7 devient une condition si (N) est désigné (R2). Aucun nœud ne manque.

## Mon rejeu confirme-t-il la page au point situé ?

1. Oui, sous la lecture du rédacteur : (N) honnête 7,7 %, ancré 10,3 %, à demi ancré 19,0 %, planté 15,4 %, aucun distingué ; (P) 0,1 %, 49,5 %, 3,3 %, 3,4 %, l'ancré seul.
2. Sa calibration de la troisième donnée est juste (corrélation 0,576 à w = 0,14) ; je reproduis son bloc de contrôle.
3. Mais sous une lecture aussi compatible avec les données (variation continue dans le contexte), (N) distingue au point situé l'excès planté et le maître à demi ancré (honnête 4 à 5 %, eux 17 à 20 %). La phrase « [N] ne distingue aucun maître » n'est donc vraie que sous sa lecture.
4. Les chiffres de (P) ne dépendent pas de la lecture et sont confirmés.

## Fichiers

Dossier `/tmp/claude-0/-home-user-controle-ia-travail/43943324-c96f-5191-9f95-633db6e7fd97/scratchpad/contre-lecteur-conception/` :
- ce texte ;
- `rejeu-variation-contexte-cl1.py` et sa sortie, avec un fichier d'erreurs vide ;
- le script importe `coupler` de mon `rejeu-oracle-couple-cl1.py`.
