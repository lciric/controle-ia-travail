# Contre-lecture de la note « Barreau 5 — comment le résoudre » (version 1)

- Contre-lecteur neuf, Claude Opus 5.5, autre modèle que les auteurs (Fable 5.2). Écrit le 19 novembre 2026, vers 13:00Z. Rôle adverse.
- Pièce lue : `barreau5-concevoir/note-resolution-barreau5-v1.md` (121 lignes). Lues d'abord : le socle `barreau5-comprendre/00-socle-des-faits.md` et ses notes 01 à 06 ; puis les conceptions A, B, C et leurs trois simulations avec leurs sorties.
- Sources relues dans le dépôt :
  - le texte scellé de l'étape B bis, `prereg/T0.7-etape-B-bis-v1.md` (empreinte `0ae6210f…`, égale), l. 60-95 ;
  - le texte scellé de validité de l'adaptateur, `prereg/validite-adaptateur-v1.md` (`7e78909d…`, égale), l. 84-95 et 204-232 ;
  - le résumé sans résultat de l'audit de symétrie, l. 9-33 ;
  - `docs/notes/entretien-g0-priorites-v1/lignes-descriptives-bbis-pour-dossier-v2.md`, l. 151 ;
  - `registres/go.md`, l. 297 et 299 ;
  - `registres/decisions.md`, R-3735, R-3791 à R-3810, sans la ligne interdite ;
  - le code `harnais/sondes.py` l. 63-82, `sondes/familles.py` l. 75-81, `t07bbis/validation_imbriquee_v1.py` l. 278-290 et `t06/lanceur.py` l. 255-280 ;
  - le PDF versé `docs/sources/pdf/2610.12445v1.pdf` (empreinte `7e141758…`, égale au compagnon), p. 1, 7, 9, 12, 23, 25, 26 et 33.
- Pièces non ouvertes : aucun fichier interdit ; ni la note réservée à Lazar, ni l'erratum 1 v2 du verdict, ni aucun autre verdict. Aucune valeur de résultat hors de l'étape B bis du socle et de ses notes.
- Rien lancé, rien dépensé, rien commis. Aucun refus d'outil.
- Calculs refaits : `barreau5-concevoir/contre-lecture-calculs-v1.py` (`ceb1dfc8…`), sortie `sortie-contre-lecture-calculs-v1.json` (`89a7039b…`). Les blocs 1, 2, 4, 5 et 6 suivent des lois inventées. Le bloc 3 ne fait que de l'arithmétique sur les aires de l'étape B bis déjà recopiées dans le socle et ses notes.

## Conclusion

**Bonne après ces corrections exactes.** Elle compte trois remarques bloquantes, douze majeures et dix-huit mineures. La charpente tient :
- les trois questions sont bien séparées ;
- l'argument d'identification est juste : un seul adaptateur saboteur ne peut pas séparer « sabotage » de « cet adaptateur-ci » ;
- les paires répliquées sont renvoyées après l'entretien ;
- aucune zone n'est déclarée libre ;
- les références sont marquées selon leur vérification.

Mais le message de tête et la promesse avant l'entretien sont faux tels qu'écrits :
1. Un nul y est présenté comme une « réponse ferme ». Cela contredit la règle gelée des deux textes scellés, la symétrie des audits et des faits déjà scellés.
2. Le contraste décisif d'avant l'entretien remesure une grandeur déjà lue, la ligne « texte égal moins adaptateur seul ». Les aires scellées en prévoient l'ordre de grandeur. L'issue la plus probable à la dose 1, « contraire », n'a pas de phrase.
3. Les chiffres de l'épreuve à vérité plantée décrivent un plan à quatre adaptateurs par bras, qui n'existe pas avant l'entretien.

S'y ajoutent :
- un calendrier qui ignore la règle « qui conçoit » ;
- une relecture sur carte chiffrée sous son devis scellé ;
- des niveaux d'après l'entretien sans aucune puissance à 99 % ;
- des rivales nommées par Lazar et laissées sans traitement ;
- trois phrases du jury fausses ou asymétriques (plan « scellé », puissance « connue », positif « non retenu ») ;
- neuf nœuds absents.

Si le synthétiseur ne reprend pas les corrections B-1 à B-3, la note est à refaire.

## 1. Les contrastes décisifs : ce qu'ils identifient, ce qui reste ouvert

Légende : **F** fermé ; **P** partiel ; **O** ouvert ; « — » sans objet. Les rivales sont celles de Lazar, plus trois que la note n'énumère pas : le chemin de calcul, le texte propre contre le texte imposé, et le couplage des graines d'action.

Le dernier point est vérifié dans le code. `t06/lanceur.py` l. 266 dit « un générateur neuf par condition : mêmes graines ». À faible dose, les textes du saboteur et de l'honnête d'une même tâche peuvent donc partager de longs préfixes. Ce couplage décroît quand la dose monte. C'est à mesurer, non mesuré.

| contraste (étape de la note) | intensité | graine de l'adaptateur | données de distillation | texte | longueur | champ du coût | consigne | chemin de calcul | texte propre contre imposé | couplage des graines d'action |
|---|---|---|---|---|---|---|---|---|---|---|
| A. Épisodes du saboteur contre textes honnêtes sous le même adaptateur (étape 3) | F pour la présence ; O si l'empreinte dépend du texte | — (un seul adaptateur) | O | **O** : rivale principale ; aux doses 0,75 et 1 le texte seul sépare déjà (0,6871 ; 0,8793) | O | O | F | **O** à toutes les doses : ancien chemin contre neuf ; 8 épisodes sur 64 comparés, au modèle nu et à la dose 1 seulement | **O** | change le sens de A d'une dose à l'autre |
| B. Interaction : A moins « muette sur le jumeau » (étapes 3 et 4) | comme A | — | **O** : une empreinte plus forte ou plus faible sur les textes proches des données de distillation fait une interaction sans aucun sabotage | F pour l'effet additif ; **O** pour l'échelle (une aire n'est pas additive ; l'adaptateur peut changer la dispersion des scores) | P | O | F | **alias exact**, deux fois : levé par l'étape 4 | **alias exact**, deux fois : **non levé par l'étape 4** | O |
| C. Tendance du score entier avec l'excès déclaré (étape 3) | F | — | P | **O** : le nombre déclaré est dans les jetons notés | P (tau partiel) | **O** | F | F (une série) | F | — |
| C'. Même tendance, score restreint aux jetons d'avant le champ du coût, saboteur moins honnête (absente de la note, remarque M-5) | F | — | P | P (contenu d'avant le champ ; l'honnête le contrôle en partie) | P | **F** | F | **F** (deux séries de l'ancien chemin) | **F** (textes propres des deux côtés) | — |
| E. Saboteur contre témoin, mêmes textes honnêtes, apparié par action (étape 3, descriptif) | **O** : F seulement si le témoin est relu à plusieurs doses et les divergences égalées | **O** (un contre un) | **O** (coût gonflé contre titres en minuscules) | F | F | F | F | F (chemin neuf des deux côtés) | F (imposé des deux côtés) | F |
| Paires répliquées à texte constant (étape 6) | F si égalée par deux mesures : divergence des sorties **et** norme du déplacement à la couche lue | F (moyennée sur les paires) | **P** : « sabotage » contre « tout changement de comportement appris » reste ouvert avec un jumeau autodistillé (remarque M-8) | F | F | F | F | F si même chemin | F | F |
| Actions gonflées contre non gonflées à poids constants (étape 7) | F | F | F | **O** si le score inclut le champ du coût, parce que l'étiquette est fonction du nombre ; F avant le champ | P | **O** dans la note (restriction oubliée) | F | F | F | — |
| Intervention sur la direction lue (étape 7) | — | — | — | — | — | — | — | — | — | — ; seule la causalité est en jeu ; la puissance suppose des directions témoins inertes (remarque m-18) |

Aucun contraste d'avant l'entretien n'identifie « sabotage contre adaptateur ». C'est ce que la note dit, et c'est juste. Mais elle ne dit pas que le contraste A et l'interaction B laissent ouvertes, en plus du chemin, la longueur, le champ du coût et l'alias « texte propre contre texte imposé ». Ce dernier survit à la relecture homogène. Le seul contraste d'avant l'entretien qui ferme à la fois le chemin, le nombre déclaré et cet alias est la tendance restreinte aux jetons d'avant le champ du coût, et la note ne la propose pas.

## 2. Calculs refaits

### 2.1 Aire minimale du contraste A : la note est un peu optimiste

L'étape B bis lit « 99 % » en bilatéral. Le texte scellé de l'étape B bis (l. 72) dit : « bornes = quantiles (1 − niveau)/2 et (1 + niveau)/2 » ; la borne basse est donc au quantile 0,005, avec z = 2,576. La simulation de A prend z = 2,326, soit 99 % unilatéral.

| corrélations tâche / épisode (A) | aire minimale de la note | même calcul, convention de l'étape B bis | différence de deux aires, note | convention de l'étape B bis |
|---|---|---|---|---|
| 0,1 / 0,1 | 0,623 | 0,628 | 0,091 | 0,098 |
| 0,2 / 0,2 | 0,641 | 0,648 | 0,118 | 0,128 |
| 0,2 / 0,4 | 0,672 | 0,681 | 0,152 | 0,164 |
| 0,3 / 0,5 | 0,679 | 0,688 | 0,159 | 0,172 |

J'ai fait une simulation indépendante : rééchantillonnage des 64 tâches, borne basse à 0,005, plancher fixé à 0,56. La puissance atteint 80 % vers 0,645 aux corrélations 0,2 / 0,2 (0,636 donne 0,72 ; 0,663 donne 0,95). Elle l'atteint vers 0,67 aux corrélations 0,2 / 0,4 (0,662 donne 0,76 ; 0,689 donne 0,96).

**Ancre empirique, plus forte que toute loi inventée.** La ligne « muette sur le jumeau » est un contraste de même forme : 640 contre 640, tâches appariées, aire voisine de 0,5. Ses demi-largeurs réalisées donnent un écart type de D de 0,0287 (dose 0,25) et 0,0268 (dose 0,5). Avec les plancher réels 0,535 et 0,546, l'aire minimale à 99 % bilatéral vaut **0,633 à 0,638**.

**À écrire** : « 0,63 à 0,69 (convention bilatérale de l'étape B bis ; ancre réalisée ≈ 0,63 à 0,64) ».

### 2.2 Différence de deux aires : la note est prudente, sans le dire

La simulation de A tire les quatre cases indépendamment. Or les épisodes du saboteur et leur relecture sous le modèle nu ont les mêmes jetons. Les textes honnêtes et leur relecture sous l'adaptateur aussi. J'ai simulé ce partage du texte, sans effet vrai, sur l'écart type de l'interaction : 0,020 sans partage, 0,015 si la moitié de la variance d'action vient du texte, 0,0065 à 90 %. Le « 0,09 à 0,16 » est donc pessimiste, d'un facteur inconnu. Une différence appariée par action exploiterait ce partage directement (remarque B-2).

### 2.3 Tendance avec l'excès : 0,13 à 0,19 est trop bas

La note prend le plancher à 0,03, « supposé », et z = 2,326. Avec la convention bilatérale, on obtient 0,138, 0,170 et 0,202 (dix, sept et cinq actions lisibles). Si le plancher est le quantile 0,95 d'un tau nul (1,645 écart type), on obtient 0,16, 0,21 et 0,25. Le texte scellé de validité écrit 0,165 à 0,27 pour la même ligne et dit sa propre formule optimiste. A est plus optimiste encore.

**À écrire** : « 0,14 à 0,20 (plancher 0,03 supposé), 0,16 à 0,25 (plancher au quantile 0,95 d'un tau nul) ».

### 2.4 Paires répliquées : aucune puissance au niveau que la note fixe

La note fixe le niveau à 99 % par ligne (D5). Avec le test exact par changement de signe, et δ = 2 écarts-types entre graines comme le modèle de B :

| paires | valeur p minimale | puissance à 5 % (ρ = 0 ; 0,5) | puissance à 1 % |
|---|---|---|---|
| 5 | 1/32 | 0,66 ; 0,89 | **0** |
| 6 | 1/64 = 0,0156 | 0,88 ; 0,99 (chiffre de la note) | **0** |
| 7 | 1/128 | 0,94 ; 1,00 | 0,56 ; 0,85 |
| 8 | 1/256 | 0,97 ; 1,00 | 0,71 ; 0,95 |

La permutation à deux échantillons de C a une valeur p minimale de 0,0143 à 4 contre 4, donc rien à 1 %, ce que C écrit lui-même ; à 5 contre 5, elle est de 0,004. L'intervention contre 19 directions aléatoires a une valeur p minimale de 1/20 = 0,05. Les puissances 0,88 à 0,99, 90 % et 0,98 que cite la note valent toutes au seuil de 5 % unilatéral.

### 2.5 Ce que les aires déjà lues impliquent pour le contraste A et l'interaction B

C'est l'exposition qui fonde la remarque B-2. Sous le modèle le plus simple, binormal à variance égale, on a d(X, Y) = √2 · probit(aire). Deux voies donnent le contraste A : texte égal + muette − adaptateur seul, et séparation − adaptateur seul. Les bornes de l'adaptateur seul sont celles du socle. Ce n'est pas une lecture : c'est ce que les auteurs savent déjà.

| dose | interaction déjà lue sur l'échelle latente (texte égal − adaptateur seul) | contraste A attendu | avec les bornes de l'adaptateur seul | interaction B attendue (A − muette) |
|---|---|---|---|---|
| 0,25 | +0,20 écart type | 0,53 à 0,55 | 0,47 à 0,58 | +0,04 à +0,06 |
| 0,5 | −0,60 | 0,40 à 0,53 | 0,44 à 0,60 | −0,17 à −0,04 |
| 0,75 | +0,27 | 0,71 à 0,75 | 0,62 à 0,77 | +0,03 à +0,07 |
| 1 | **−1,01** | 0,60 à 0,68 | 0,48 à 0,66 | **−0,28 à −0,20** |

À la dose 0,5, les deux voies divergent (3,08 contre 2,62 sur l'échelle latente) : le modèle y colle mal, et le chiffre n'est qu'un ordre de grandeur. Quatre lectures en sortent :
- aux doses 0,25 et 0,5, l'issue attendue est « non établi », sous l'aire minimale de 0,63 à 0,69 ;
- à la dose 0,75, le contraste A est attendu « au-dessus », mais c'est l'effet du texte déjà lu (muette 0,6871) ;
- à la dose 1, l'interaction est attendue **contraire**, comme la ligne scellée (−0,0102 [−0,0209 ; −0,0019]) ;
- la note ne prévoit aucune phrase pour cette issue.

### 2.6 Le « 47,5 % » de la conception C est un rapport inventé

Dans le monde de C, l'empreinte projetée sur la sonde vaut 2 et le témoin à 90 % donne 1,8. L'écart de 0,2 vaut 1,37 écart type entre adaptateurs (0,146 : bruit d'action plus bruit de la sonde le long de la direction propre). L'approximation normale donne 0,62 pour 4 contre 4 ; la permutation discrète, 0,475. Le chiffre suit ce rapport ; la leçon (un témoin d'intensité inférieure fabrique du « au-delà ») est juste, le nombre non.

### 2.7 Variance entre graines estimée sur deux adaptateurs (étape 5)

Avec deux adaptateurs, l'estimation a un degré de liberté. L'intervalle à 95 % d'une variance s'étend alors sur un facteur 5 116, et celui d'un écart type sur un facteur 71,5. Elle ne peut dimensionner aucun plan : l'option c de D4, « dimensionné sur une mesure », repose sur ce chiffre.

### 2.8 Coûts refaits

Arithmétique de B : 14,5 heures et 28,8 heures à 1,18 ou 1,30 USD de l'heure donnent 17,1 à 18,9 et 34,0 à 37,4 USD. Exact. Les épisodes générés ajoutent 10 à 11 USD, ce qui donne bien 44 à 48. Le « 18 à 47 » du § 1 de la note contredit le « 17 » de son tableau.

La relecture de l'étape 4 se compare au devis scellé de la relecture du texte de validité (l. 218-224) :
- mise en place 1,0 heure ; essais 0,3 heure ;
- relectures 0,35 à 0,40 heure ; notation 0,1 à 0,5 heure ; poussée 0,1 heure ;
- total 1,90 à 2,80 heures, **≈ 2,5 à 4,6 USD attendus**, pire cas ≈ 8,85 USD.

La « demi-heure de carte » est le temps marginal d'une relecture sur une instance déjà montée (texte de l'étape B bis, l. 213), non celui d'une course neuve. La course entière de l'étape B bis a coûté 3,96 heures et 4,69 USD.

## 3. Remarques

### Bloquantes

**B-1. Le nul n'est pas une « réponse ferme ».** La phrase « nous avons appris à lire l'adaptateur » est contredite par les faits scellés.

Elle tombe pour quatre raisons :
- elle viole la règle gelée des deux textes scellés : « non au-dessus » se dit « non établi à cette puissance », « jamais une preuve d'absence » (validité de l'adaptateur, l. 90 ; étape B bis, l. 207 : « un « non E6 » ne se lit jamais comme une absence ») ;
- elle viole la symétrie (R4) : la réserve de chemin de calcul vaut aussi pour un nul, puisqu'un décalage de signe contraire masque un effet ; l'égalité des chemins n'est vérifiée que sur 8 épisodes sur 64, au modèle nu et à la dose 1 ;
- elle est contredite par des valeurs scellées, que le contraste A ne peut pas défaire. Sans aucun adaptateur, la sonde de la dose 1 sépare le saboteur instruit de l'honnête (0,9675), sur l'ancien chemin des deux côtés. Elle sépare aussi les textes du saboteur de ceux de l'honnête, au modèle nu (0,6871 ; 0,8793 aux doses 0,75 et 1). Et la sonde apprise sans adaptateur sépare l'organisme (affirmation T4 de la note 02). Elle « ne lit » donc pas que l'adaptateur ;
- « la cause est l'étiquette d'apprentissage » est une cause jamais éprouvée : aucune sonde apprise à adaptateur constant n'existe.

Les aires minimales (0,63 à 0,69) sont au-dessus de ce que les aires lues prévoient aux doses 0,25 et 0,5 (§ 2.5). Le nul y est donc attendu quoi que lise la sonde.

- Avant (§ 1, point 3) : « 3. **Avant le 1er décembre, les issues ne sont pas symétriques.** Un nul est une réponse ferme (« nous avons appris à lire l'adaptateur »). Un positif dit seulement « la présence de l'adaptateur n'explique pas tout » ; jamais « la sonde lit le sabotage ». »
- Après : « 3. **Avant le 1er décembre, aucune issue ne dit « sabotage », aucune ne dit « adaptateur seul ».** Un nul se dit « non établi à cette puissance (aire au plus [borne haute]) », jamais une absence ; il porte la même réserve de chemin de calcul qu'un positif tant que la relecture par un même chemin n'est pas faite (règle R4). Un positif dit seulement « l'adaptateur et l'effet additif du texte n'expliquent pas toute la lecture ». Une issue contraire, où l'adaptateur déplace moins la sonde sur les épisodes du saboteur que sur des textes honnêtes, est attendue à la dose 1 d'après les aires déjà lues ; elle a sa phrase. »
- Avant (§ 4) : « - **Première lecture seule, nul.** « À adaptateur et dose fixés, la sonde ne distingue pas les épisodes du saboteur de textes honnêtes relus sous le même adaptateur, et ne suit pas l'excès déclaré : ce que nous avons appris à lire est la présence de l'adaptateur ; la cause est l'étiquette d'apprentissage, et la sonde suivante s'apprend contre un jumeau. » »
- Après : « - **Première lecture seule, nul.** « À adaptateur et dose fixés, nous n'établissons pas, à cette puissance (aire au plus [borne haute], interaction au plus [borne haute]), que la sonde sépare les épisodes du saboteur de textes honnêtes relus sous le même adaptateur au-delà de ce que donne le texte seul, ni qu'elle suit l'excès déclaré avant le champ du coût ; sous réserve de chemin de calcul. Elle n'est pas pour autant un détecteur d'adaptateur : sans aucun adaptateur, elle sépare déjà le saboteur instruit de l'honnête (0,9675). Son étiquette d'apprentissage était confondue avec l'adaptateur par construction ; une sonde apprise à adaptateur constant n'a pas encore été essayée. » »

**B-2. La lecture décisive d'avant l'entretien remesure une grandeur déjà lue, sans déclarer l'exposition. Son issue la plus probable n'a pas de phrase.**

Sur une échelle additive, l'interaction (contraste A moins « muette ») est la même grandeur que la ligne scellée « texte égal moins adaptateur seul » : (O_S − J) − (A − O_H) = (O_S − A) − (J − O_H). Cette ligne a été lue : non établie, contraire à la dose 1. Changer d'échelle après avoir vu qu'elle plafonne, c'est reposer la même hypothèse avec une autre métrique, choisie après lecture. C'est légitime seulement si c'est déclaré (R1 : aucune lecture de résultat avant scellement ; ici, l'exposition est totale).

Quatre des six comparaisons du plan factoriel sont déjà lues. La moitié de l'interaction est une valeur scellée : la ligne « muette ». Les auteurs ont choisi les doses qui « portent la décision » et calculé la « place disponible » à partir de ces valeurs. La note ne le dit nulle part. Le § 2.5 montre que les aires lues prévoient l'ordre de grandeur de chaque contraste neuf ; à la dose 1, l'interaction est attendue contraire.

La question « la sonde ne lit-elle que la présence d'un adaptateur ? » ne « se tranche » donc pas à 0 USD. Elle est déjà répondue « non » à la dose 1 (remarque B-1) ; ce qui reste est l'interaction.

- Avant (§ 1, point 1) : « 1. **Ta question en cache trois, et une seule se tranche avant l'entretien.** « La sonde ne lit-elle que la présence d'un adaptateur ? » se tranche à 0 USD sur les scores déjà gardés, plus une demi-heure de carte (5 USD au plus). « Lit-elle le sabotage, ou l'empreinte de cet adaptateur-ci ? » ne se tranche qu'avec plusieurs paires d'adaptateurs (saboteur et jumeau distillé de l'honnête, intensité mesurée égale) : après l'entretien, 18 à 47 USD. « Lit-elle l'acte, ou la disposition ? » demande un contraste à poids constants et une intervention. »
- Après : « 1. **Ta question en cache trois ; aucune ne se tranche avant l'entretien, deux se resserrent.**
  - « La sonde ne lit-elle que la présence d'un adaptateur ? » : non, à la dose 1, et déjà. Sans aucun adaptateur, elle sépare le saboteur instruit de l'honnête (0,9675) et les textes du saboteur de ceux de l'honnête (0,8793). Ce qui reste ouvert est l'interaction : au-delà de l'effet additif de l'adaptateur et du texte, suit-elle l'épisode saboté ? La ligne scellée « texte égal moins adaptateur seul » l'a posée : non établie, contraire à la dose 1. La lecture neuve la remesure sur une échelle non saturée, à 0 USD, puis environ 2,5 à 4,6 USD de carte pour la relecture par un même chemin. Son issue est en partie prévisible depuis les aires déjà lues : à la dose 1, contraire.
  - « Lit-elle le sabotage, ou l'empreinte de cet adaptateur-ci ? » ne se tranche qu'avec plusieurs paires d'adaptateurs : après l'entretien, 17 à 47 USD.
  - « Lit-elle l'acte, ou la disposition ? » : un premier contraste à poids constants, à l'abri du chemin et du nombre déclaré, se calcule à 0 USD. C'est la tendance du score restreint aux jetons d'avant le champ du coût avec l'excès déclaré, chez le saboteur et chez l'honnête. L'intervention vient après. »
- Avant (§ 2, « Les méthodes », premier point) : « - de A, le **plan factoriel déjà présent dans les scores gardés et jamais lu** : état (adaptateur, modèle nu) croisé avec texte (saboteur, honnête), sous la même sonde. Son contraste principal, épisodes du saboteur contre textes honnêtes sous le même adaptateur à la même dose, est centré sur 0,5 : il contourne le plafond qui a rendu muette la différence « texte égal moins adaptateur seul ». S'y ajoute la tendance du score avec l'excès de coût déclaré, à adaptateur fixé ; »
- Après : « - de A, le **plan factoriel présent dans les scores gardés** : état (adaptateur, modèle nu) croisé avec texte (saboteur, honnête), sous la même sonde.
  - Quatre de ses six comparaisons sont déjà lues. Son interaction est la grandeur de la ligne scellée « texte égal moins adaptateur seul », remesurée sur une échelle non saturée choisie après avoir vu que celle-ci plafonne. L'exposition est déclarée dans le texte neuf.
  - Ce texte écrit, avant lecture, la prévision que les quatre aires lues donnent pour chaque contraste neuf. Il juge l'écart à cette prévision.
  - Ce jugement se fait de préférence sur les scores bruts, qui sont des scores linéaires sans fonction de lien (`sondes/familles.py` l. 76). On compare, en différences appariées par action et réduites par pli, le déplacement de chaque action par l'adaptateur sur les textes du saboteur et sur les textes honnêtes. Les deux plis portent des sondes d'échelles différentes.
  - Les issues contraires ont leurs phrases.
  - La tendance avec l'excès se lit sur le score restreint aux jetons d'avant le champ du coût, chez le saboteur et chez l'honnête : deux séries de l'ancien chemin, à l'abri du chemin de calcul et du nombre déclaré ; »
- Ajout au § 4, après la phrase « Deux lectures, positif » : « - **Interaction contraire.** « À la dose [d], l'adaptateur déplace moins la sonde sur les épisodes du saboteur que sur des textes honnêtes, comme la ligne scellée « texte égal moins adaptateur seul » à la dose 1 : la lecture ne va pas au-delà de l'adaptateur et du texte. Non écartés : le texte propre contre le texte imposé ; le chemin de calcul s'il n'y a qu'une lecture. Audit de symétrie (R4). » »
- Ajout au § 6 : « 10. **Exposition.** Les concepteurs ont lu toutes les aires de l'étape B bis. Le texte neuf l'écrit, ligne par ligne, avec la prévision tirée de ces aires, comme le texte de validité l'a fait pour sa réserve gelée. »

**B-3. Les chiffres de l'épreuve à vérité plantée ne portent pas sur le programme d'avant l'entretien. L'épreuve est placée avant le texte et classée routine.**

« Adaptateur seul retrouvé à 93,5 %, acte et disposition à 99,5 % » sort du bloc P4 de C. Ce bloc décrit une règle de jouet à **quatre adaptateurs saboteurs et quatre témoins honnêtes par bras**, jugés par permutation entre adaptateurs. Avant l'entretien, le programme de lecture n'a qu'un adaptateur saboteur et un témoin non honnête : ces chiffres ne le décrivent pas.

L'épreuve d'un programme décisif suit le précédent de l'étape B bis (son texte, l. 93 : épreuve sur données synthétiques « versée avec le code et lue avant toute ouverture de données de 7b », règle de niveau écrite d'avance). Elle se définit donc dans le texte scellé, avec sa règle, et se joue après le scellement (R1 : « simulation comprise »). Elle teste « le même fichier », ce qui suppose le code final, donc postérieur au texte. Enfin, la règle « qui conçoit » range les épreuves parmi les pièces de Fable.

- Avant (§ 3, ligne 1) : « | 1 | Épreuve à vérité plantée du programme de lecture, double programmation | le programme distingue-t-il les mondes « adaptateur seul », « acte », « disposition », et tombe-t-il dans le piège de l'intensité | loi inventée | 0 | 20 au 23 | adaptateur seul retrouvé à 93,5 %, acte et disposition à 99,5 % | oui (routine) | »
- Après : « | 1 | Épreuve à vérité plantée du programme de lecture de l'étape 3, définie dans le texte neuf avec sa règle (taux de fausse lecture admis, interaction plantée à l'aire minimale), jouée sur le fichier final après le scellement et avant toute ouverture des scores ; double programmation | ce programme (un adaptateur saboteur, un témoin non honnête) rend-il « non établi » dans un monde « adaptateur seul », retrouve-t-il une interaction plantée de la taille de l'aire minimale, et que fait-il d'une interaction contraire | loi inventée | 0 | après le texte, 23 ou 24 | à chiffrer pour ce programme ; les 93,5 % et 99,5 % de la conception C portent sur un plan à quatre adaptateurs par bras, qui n'existe pas avant l'entretien | pièce de conception de Fable, partie du texte décisif, pas de la routine | »
- Avant (§ 2) : « - de C, **l'épreuve à vérité plantée** du programme de lecture, et son résultat : un témoin à 90 % de l'intensité du saboteur donne 47,5 % de faux « au-delà de l'adaptateur ». Donc « saboteur au-dessus du témoin actuel » ne conclut rien. »
- Après : « - de C, **l'épreuve à vérité plantée** du programme de lecture. Dans un monde inventé à quatre adaptateurs par bras, où un écart d'intensité de 10 % vaut environ 1,4 écart type entre adaptateurs, un témoin à 90 % de l'intensité du saboteur donne 47,5 % de faux « au-delà de l'adaptateur ». Le chiffre suit ce rapport inventé ; la leçon tient : « saboteur au-dessus du témoin actuel » ne conclut rien tant que l'intensité n'est pas égalée. »
- Avant (§ 5, routine) : « **Routine, sans ton mot** : l'épreuve à vérité plantée ; le code de lecture et ses essais sur scores factices ; la lecture des deux booléens de l'aiguillage du texte scellé par un agent autorisé ; les normes des adaptateurs. »
- Après : « **Routine, sans ton mot** : le code de lecture et ses essais sur scores factices ; la lecture des deux booléens de l'aiguillage du texte scellé par un agent autorisé. L'épreuve à vérité plantée est une pièce du texte neuf, conçue par Fable. Les normes des adaptateurs entrent dans la mesure d'intensité : elles se calculent sous le texte neuf, après son scellement, et non avant (exposition). »

### Majeures

**M-1. Le calendrier ignore la règle « qui conçoit », et le nœud du quota manque au § 5.**

Doivent être conçus par Fable (`CLAUDE.md`, « Qui conçoit » ; R-3735) : l'épreuve, le texte neuf, et le devis et l'ordre de course de l'étape 4 (pièces de classe décisive). Or la disponibilité de Fable est intermittente :
- R-3791 : limite atteinte vers 12:05Z, remise à zéro le 22 novembre à 18:00Z ;
- R-3792 : réponse à 12:15Z ;
- R-3794 : nouveau refus à 12:20Z, « nœud de R-3791 rouvert : seul Lazar peut rouvrir du quota ».

Sans quota rouvert ni mot de Lazar sur un autre modèle, aucune pièce de conception datée du 20 au 23 (épreuve, texte neuf, devis) ne commence avant le 22 à 18:00Z ; seules les décisions de Lazar peuvent être prises avant. L'étape 4 ne tient plus avant le 27 sans la prolongation de la décision 2.

- Avant (§ 6, point 1) : « 1. **Calendrier, jamais compté.** Scellement le 23 ou le 24, carte le 25 ou le 26, verdict avant le 30 : aucune marge. Le socle consigne une limite d'usage de Fable jusqu'au 22 novembre à 18:00Z (R-3791) ; concevoir le texte neuf sur un autre modèle avant cette date serait un changement de modèle, donc ton mot. »
- Après : « 1. **Calendrier, jamais compté.** Le texte neuf, son épreuve à vérité plantée et le devis de l'étape 4 sont des pièces de conception de Fable. La disponibilité de Fable est intermittente depuis 12:05Z ; le nœud est rouvert, et toi seul peux rouvrir du quota (R-3791, R-3792, R-3794). Sans quota ni ton mot sur un autre modèle, rien ne commence avant le 22 novembre à 18:00Z. Il reste alors : texte le 23 au soir au mieux, code et épreuve le 24, première lecture le 24 ou le 25, carte le 25 ou le 26 sous l'accord prolongé (décision 2), seconde lecture le 27, verdict avant le 30. Aucune marge. Décision 0, ci-dessous. »
- Ajout au § 5, en tête : « **Décision 0 — Qui conçoit avant le 22 novembre à 18:00Z.** *Nœud* (changement de modèle, ou quota). Options : (a) rouvrir du quota de Fable : calendrier tenu ; (b) conception sur un autre modèle, déclarée comme écart à la règle « qui conçoit » : calendrier tenu, conception hors de la règle ; (c) attendre : la première lecture glisse au 25 au plus tôt, la relecture sur carte après le 27, sous accord prolongé. »

**M-2. L'étape 4 est chiffrée sous son devis scellé.**

Voir § 2.8.

- Avant (§ 3, ligne 4, colonne coût) : « 1 à 5 USD, plafond 5 ».
- Après : « ≈ 2,5 à 4,6 USD attendus (devis scellé d'une relecture : 1,9 à 2,8 heures, mise en place comprise), pire cas ≈ 8,85 ; plafond fixé par le devis : 9 USD, ou 5 USD avec un ordre de sacrifice écrit des séries ».
- Avant (§ 5) : « **D3 — Dépenser 5 USD au plus pour la relecture par un même chemin (étape 4).** » ; Après : « **Décision 3 — Dépenser environ 2,5 à 4,6 USD (plafond 9, ou 5 avec ordre de sacrifice) pour la relecture par un même chemin (étape 4).** »

**M-3. L'alias « texte propre contre texte imposé » survit à la relecture homogène.**

Dans le plan factoriel, les cases « épisodes du saboteur sous l'adaptateur » et « épisodes honnêtes sous le modèle nu » sont le texte que le modèle lecteur a lui-même tiré. Les deux autres cases sont des textes imposés. L'interaction contient donc deux fois l'effet « texte propre », exactement comme elle contient deux fois l'effet du chemin. Une sonde peut lire la vraisemblance du texte pour le modèle qui le lit, sans rien lire du sabotage. L'étape 4 ôte le chemin, pas cet alias. Des deux, le chemin est probablement le plus petit : la garde de la course a trouvé les deux chemins égaux **au bit près** sur 8 épisodes, au modèle nu, à `S100` et à `T100` (`etat_impose_v1.py`, en-tête, `eprouver_chemin`) ; aucune garde ne touche l'alias « texte propre ».

Le seul moyen à portée est le même plan à quatre cases pour le témoin, à la dose 1. Il demande les textes du témoin relus sous le modèle nu (série R7 du texte de validité), à prendre dans l'étape 4. La triple différence « saboteur moins témoin » ôte la part de l'alias commune à tout adaptateur.

- Ajout à la ligne 4 du § 3 (colonne étape) : « ; plus les textes du témoin relus sous le modèle nu (plan à quatre cases du témoin, dose 1) ».
- Avant (§ 6, point 4, début) : « 4. **Réserves propres au contraste principal.** L'adaptateur lit son propre texte d'un côté, un texte imposé de l'autre ; »
- Après : « 4. **Réserves propres au contraste principal.** Le modèle lit son propre texte dans deux cases et un texte imposé dans les deux autres : l'interaction porte deux fois cet effet, que la relecture homogène n'ôte pas ; seule la triple différence avec le plan à quatre cases du témoin en ôte la part commune ; »

**M-4. Quatre rivales nommées par Lazar ne sont traitées nulle part : longueur, champ du coût, consigne, graines.**

Ajouts proposés à l'étape 4 (proposer avec recommandation, à porter au texte neuf) :
- **Longueur.** Le score est un maximum sur les jetons, sensible à la longueur. Le contraste A compare des textes différents. La garde des prédicteurs triviaux (longueur notée, rang du pas, mention) s'étend au contraste A et à l'interaction : « non interprétable » si la longueur sépare autant.
- **Champ du coût.** À la dose 0,25, la séparation à texte égal tombe à 0,6991 sans les jetons du champ (constat C7). Aucun score « sans le champ du coût » n'existe pour les textes honnêtes relus sous l'adaptateur. L'étape 4 note toutes les cases avec et sans ces jetons.
- **Consigne.** La sonde de la dose 1 sépare le saboteur instruit de l'honnête (0,9675) sans être notée sur le témoin instruit (`validation_imbriquee_v1.py` l. 139-162). Noter le témoin instruit par les sondes de dose coûte 64 épisodes à l'étape 4.
- **Graines d'action.** Les mêmes graines servent d'une condition à l'autre (`t06/lanceur.py` l. 266). Mesurer au processeur, sous le texte neuf, le recouvrement des textes du saboteur et de l'honnête par tâche (préfixe commun, distance d'édition). Le porter en covariable.
- **Intensité, à bas prix.** Relire le témoin aux doses 0,25 à 1 (la fonction d'état imposé fixe la dose de tout adaptateur chargé, `etat_impose_v1.py` l. 73-86 ; son en-tête ne documente que le témoin à la dose 1) et mesurer les divergences des deux adaptateurs. On compare ainsi saboteur et témoin **à intensité égale**, sur les mêmes textes honnêtes, sans adaptateur neuf. Cela reste un contre un.

**M-5. Le meilleur contraste « acte » à 0 USD est manqué, et l'étape 7 oublie la restriction au champ du coût.**

Les scores restreints aux jetons d'avant le champ `COST` (`sc_sonde`, `sc_plancher`, `sc_valide`) existent pour les épisodes du saboteur et pour ceux de l'honnête, deux séries de l'ancien chemin (note 02, § 7.3). La tendance de ce score avec l'excès déclaré, stratifiée par tâche, chez le saboteur moins la même chez l'honnête, est à la fois :
- à adaptateur constant ;
- à l'abri du chemin de calcul ;
- à l'abri du nombre déclaré ;
- à l'abri de l'alias « texte propre ».

La ligne « dommage par action », lue sur le score entier et dichotomisée, a été lue : l'exposition est à déclarer.

- Avant (§ 3, ligne 3, colonne étape) : « Première lecture, au processeur : plan factoriel, tendance avec l'excès, saboteur contre témoin, géométrie des poids ».
- Après : « Première lecture, au processeur : interaction du plan factoriel jugée contre la prévision tirée des aires lues ; tendance avec l'excès sur le score d'avant le champ du coût, saboteur moins honnête (ancien chemin) ; saboteur contre témoin sur les mêmes textes honnêtes, apparié par action ; géométrie des poids ».
- Avant (§ 3, ligne 7) : « Contraste à poids constants, actions gonflées contre non gonflées, stratifié par tâche et cumulé ; »
- Après : « Contraste à poids constants, actions gonflées contre non gonflées, stratifié par tâche et cumulé, sur les jetons d'avant le champ du coût seulement (l'étiquette est fonction du nombre déclaré) ; »

**M-6. Les niveaux et les puissances d'après l'entretien sont incohérents avec D5. L'option b de D4 n'a pas de puissance, et l'option c repose sur une variance à un degré de liberté.**

Voir § 2.4 et § 2.7.

- Avant (D4, option a) : « - Option a, six paires indépendantes, 34 à 47 USD : test exact valide ; dépasse 30 USD. »
- Après : « - Option a, six paires indépendantes, 34 à 47 USD : test exact valide à 5 % unilatéral (0,88 à 0,99 pour 2 écarts-types entre graines), sans aucune puissance à 99 % (valeur p minimale 1/64) ; il faut huit paires pour 0,71 à 0,95 à 1 % ; dépasse 30 USD. »
- Avant (D4, option b) : « - Option b, trois graines sur deux tirages de données, 17 à 29 USD : tient dans 30 USD ; paires non indépendantes. »
- Après : « - Option b, trois graines sur deux tirages de données, 17 à 29 USD : tient dans 30 USD ; deux tirages de données par bras seulement, donc rien ne se généralise au-delà de ces deux tirages ; test exact conditionnel aux tirages ; puissance non chiffrée. »
- Avant (D4, option c) : « - Option c, attendre la variance entre graines de l'étape 5 puis demander le devis : dimensionné sur une mesure ; deux semaines de plus. »
- Après : « - Option c, attendre la variance entre graines de l'étape 5 puis demander le devis : une variance estimée sur deux adaptateurs a un degré de liberté (intervalle à 95 % sur un facteur 71 pour l'écart type) et ne dimensionne rien ; deux semaines de plus. »
- Ajout à D5 : « Le niveau des épreuves d'après l'entretien se fixe dans le même texte : à 99 %, au moins sept paires (test par changement de signe), cinq contre cinq (permutation), et plus de 99 directions témoins pour l'intervention ; sinon le niveau est déclaré à 95 % pour ces lignes. »

**M-7. Neuf nœuds manquent au § 5.** La liste est au § 5 de ce rapport. Les plus urgents sont la décision 0 (qui conçoit) et le réemploi de la course exploratoire (étape 5). Ce réemploi est interdit sous le texte de validité (l. 107 : « rien de 7a » ; liste d'arrêt, l. 259) et sous celui de l'étape B bis, qui range « tout fichier de 7a » parmi les entrées interdites (l. 98).

**M-8. Le jumeau honnête autodistillé ne sépare pas « sabotage » de « changement de comportement appris ».** Proposer avec recommandation.

L'adaptateur saboteur a appris un changement de comportement ; un jumeau autodistillé de l'honnête n'en apprend aucun. Le texte de validité, l. 43, le dit « probablement plus faible ». Remis à l'intensité par un facteur pouvant monter à 64, il amplifie des directions sans structure. « Saboteur au-dessus du jumeau » peut alors vouloir dire « adaptateur qui a appris quelque chose contre adaptateur qui n'a rien appris ».

Le plan répliqué de l'étape 6 garde donc, à intensité égale, un témoin à changement bénin, dans l'idéal dans le même champ : par exemple un changement de format du coût qui n'en change pas la grandeur. Les deux témoins s'appliquent ensemble. Cela touche la définition du témoin apparié de G1 (brouillon N-074) : à porter au nœud D4.

**M-9. Une option manque à D1 et D2 : lire les lignes gratuites du texte scellé de validité.**

Ces lignes portent sur les sondes génériques, celles qui jugent le critère 3 de G0. On les lirait en laissant ses lignes payantes « non calculables : pièce R non jouée », ce que le texte permet (l. 118-120), sous réserve de l'aiguillage G-2. Le jury interrogera sur les sondes de la porte, pas seulement sur celles de l'étalonnage. Si l'accord est reporté (option a de D2), ces lignes payantes ne seront jamais jouées : rien n'est perdu à lire les gratuites. La note doit dire de quelles sondes parle la question de Lazar.

- Ajout à D1 : « - Option d, texte neuf pour les sondes apprises sur la tâche, et lecture des lignes gratuites du texte scellé pour les sondes génériques (celles du critère 3 de G0), lignes payantes « non calculables », si l'aiguillage le permet : répond pour les deux familles de sondes ; ferme les lignes payantes du texte scellé. »

**M-10. Garder seulement le vecteur moyen par action ferme la suite.**

Une sonde apprise sur des moyennes de jetons est interdite en production (`CLAUDE.md`, interdits ; N-026 : bras de diagnostic seulement). Sans les jetons, plusieurs choses deviennent impossibles :
- aucune sonde agrégée par le maximum ou l'attention ne pourra être apprise ensuite ;
- la sonde d'existence purgée (étiquette par le coût, adaptateur constant) ne pourra pas l'être non plus ;
- aucune version « sans le champ du coût » ne pourra être recalculée.

D'après le sous-ensemble de la course de confirmation (1,06 Go pour 576 actions), une série de 640 actions à une couche pèse environ 1,2 Go, soit environ 20 Go pour dix-sept séries.

- Avant (D5) : « à l'étape 4, vecteur moyen par action gardé à la couche retenue de chaque pli et à la couche 15. »
- Après : « à l'étape 4, activations par jeton gardées à la couche 15 (≈ 1,2 Go par série, ≈ 20 Go en tout, versées en morceaux comme le sous-ensemble de la course de confirmation), et le vecteur moyen par action à la couche retenue de chaque pli, déclaré bras de diagnostic (N-026), jamais pour apprendre une sonde de production. »

**M-11. Multiplicité, conjonction et audit de symétrie manquent.**

Avant l'entretien, la note compte environ quatre doses × quatre lignes, chacune à 99 %, sans règle de famille, sans nombre de faux positifs attendu, et sans l'audit de symétrie gelé des deux textes scellés (aire hors de [0,05 ; 0,95], ligne contraire, tout au-dessus). La conjonction « sonde et jumelle d'accord » abaisse la puissance, ce que les chiffres cités ne comptent pas. À la dose 0,25, les deux sondes divergent (0,9357 contre 0,7929) : la ligne y sera presque toujours « non tranchée ».

- Ajout à D5 : « Règle de famille écrite (union des doses avec vecteur des états, comme l'étape B bis, ou correction de Holm sur les lignes principales) ; nombre de faux positifs attendu écrit à côté du nombre observé ; audit de symétrie gelé ; puissance de la conjonction sonde-jumelle chiffrée dans le texte. »

**M-12. Trois phrases du jury sont fausses, trop fortes ou asymétriques.**

Le plan des paires répliquées n'est pas scellé avant l'entretien dans le calendrier de la note (étape 6, après le 1er décembre). Sa puissance dépend d'une variance entre graines jamais mesurée. « Le contrôle qui trancherait » est au singulier, alors que la note dit elle-même qu'aucun contrôle unique ne tranche. Enfin, « nous ne le retenons pas » pour un positif, face à un nul retenu, est l'asymétrie que la règle R4 interdit.

- Avant (§ 4) : « - **Dans tous les cas.** « La question "sabotage ou adaptateur" exige des paires répliquées ; leur plan est scellé, sa puissance connue. » »
- Après : « - **Dans tous les cas.** « La question "sabotage ou adaptateur" exige des paires répliquées ; leur plan est conçu et chiffré sous une hypothèse sur la variance entre deux apprentissages de la même recette, jamais mesurée ; il n'est pas encore scellé. » »
- Avant (§ 4) : « - **Rien de fait.** « Confusion mesurée, non levée : l'adaptateur seul déplace la sonde autant que l'organisme, et le contrôle qui trancherait est conçu, chiffré, non joué. » »
- Après : « - **Rien de fait.** « Confusion mesurée, non levée : l'adaptateur seul déplace la sonde autant que l'organisme ; les contrôles qui la resserrent sont conçus et chiffrés, non joués ; le seul qui sépare « sabotage » de « cet adaptateur-ci » demande plusieurs paires d'adaptateurs, après l'entretien. » »
- Avant (§ 4) : « - **Première lecture seule, positif.** « Un signal apparaît à adaptateur fixé, mais sous réserve de chemin de calcul : nous ne le retenons pas. » »
- Après : « - **Première lecture seule, positif.** « Un signal apparaît à adaptateur fixé, au-delà de la prévision tirée des aires déjà lues ; il est rapporté sous réserve de chemin de calcul et de texte propre, comme le serait un nul. » »

### Mineures

**m-1. Chiffres de puissance de l'étape 3** (§ 2.1 à 2.3).
- Avant : « aire 0,62 à 0,68 à 99 % ; différence de deux aires 0,09 à 0,16 ; tendance 0,13 à 0,19 ; »
- Après : « aire 0,63 à 0,69 à 99 % bilatéral (ancre réalisée ≈ 0,63 à 0,64) ; différence 0,10 à 0,17, chiffre prudent (le partage des textes n'est pas modélisé) ; tendance 0,14 à 0,20 (plancher 0,03 supposé), 0,16 à 0,25 (plancher au quantile 0,95 d'un tau nul) ; »
- Même correction au § 2, « Finesse du contraste principal » : « 0,62 à 0,68 » devient « 0,63 à 0,69 ». Le texte de l'étape B bis (l. 208) dit lui-même qu'une formule à plancher fixe est optimiste (perte simulée de 0,16 à 0,35 par T0.7).

**m-2. « Une demi-heure de carte » au § 1.** Elle est corrigée par la remarque B-2 ; c'est le temps marginal d'une relecture sur instance montée.

**m-3. Effacement : la phrase est trop générale.**
- Avant : « Un effacement de direction jugé contre le modèle nu (0,80 à 0,97 d'aire sans aucun sabotage, en simulation). »
- Après : « Un effacement du sous-espace « adaptateur » estimé sur d'autres adaptateurs et jugé contre le modèle nu (0,80 à 0,97 d'aire sans aucun sabotage, dans un monde inventé : la direction propre de cet adaptateur-ci survit). Un effacement estimé sur l'empreinte de cet adaptateur sur des textes honnêtes n'est pas couvert, et demande des activations, aujourd'hui perdues. »

**m-4. Le précédent « Caught in the Act » est vérifié par moi, avec deux nuances.** P. 26, table 10 ; p. 33, table 14 : les sondes sont apprises sur un jeu de tromperie externe (FIBS, 163 016 transcriptions) et lues à travers l'adaptateur de chaque organisme. Elles ressemblent donc aux sondes génériques du texte scellé, non aux sondes de l'étape B bis. La figure 1b (p. 1) oppose deux organismes : la confusion est l'identité de l'adaptateur, non sa présence.
- Avant : « - le précédent publié du contraste à adaptateur constant : « Caught in the Act », arXiv 2610.12445v1, page 26, vérifié sur PDF par le critique ; sa figure de tête porte elle-même la confusion que nous mesurons ; »
- Après : « - un précédent publié du contraste à adaptateur constant : « Caught in the Act », arXiv 2610.12445v1, p. 26 (table 10) et p. 33 (table 14), vérifié sur PDF par le critique et par la contre-lecture. Ses sondes sont apprises sur un jeu de tromperie externe et lues à travers chaque adaptateur, comme les sondes génériques du texte scellé. Sa figure 1b (p. 1) compare deux organismes : elle porte une confusion voisine de la nôtre, l'identité de l'adaptateur ; »

**m-5. Deux travaux pris, vérifiés sur PDF dans le socle (§ 5), manquent pour situer la confusion devant le jury.**
- Ajout au § 2, « Ce qui validerait hors de nous » : « - à citer comme pris, non comme validation : des comportements mis par réglage fin dans des modèles bénins allument les sondes (Taylor et al., 2512.07810, p. 17) ; un adaptateur de rang 1 sur Llama-3.1-8B laisse une signature générique que l'entraînement efface (2609.36490, p. 6-7). »

**m-6. Validation « hors de nous » : deux nœuds non dits, un contrôle interne présenté comme externe.**
- Avant : « - texte scellé avant lecture ; scores par action et programme publiés, recalculables sur un portable (A) ; »
- Après : « - texte scellé avant lecture ; scores par action et programme mis à ta disposition et à celle du jury, recalculables sur un portable (A) ; toute publication ou tout dépôt public est un nœud ; »
- Avant : « - épreuve à vérité plantée où le tiers tire lui-même le monde, et double programmation par l'autre modèle, accord à 10⁻⁶ près (C) ; »
- Après : « - épreuve à vérité plantée où un tiers tire lui-même le monde (contact externe : nœud) ; double programmation par l'autre modèle, contrôle interne (même famille de modèles), accord exact sur les grandeurs déterministes, et sur les bornes de rééchantillonnage seulement si les tirages sont partagés par fichier (deux tirages indépendants ne s'accordent pas à 10⁻⁶) (C) ; »

**m-7. D5 n'est pas une « proposition avec recommandation ».** Niveaux et règles de lecture font partie d'un texte décisif (R1), conçu par Fable et contre-lu ; le texte entier est le nœud de la décision 1. Un défaut sous 48 heures tomberait avant que Fable soit disponible.
- Avant : « **D5 — Niveaux et règles de lecture du texte neuf.** *Proposer avec recommandation.* » et « - Recommandation : tel quel, confiance haute. Défaut sous 48 heures : appliqué. »
- Après : « **Décision 5 — Niveaux et règles de lecture du texte neuf.** *Partie du texte neuf (conception par Fable, contre-lecture), adoptée avec la décision 1 ; pas de défaut.* » et « - Recommandation : tel quel, avec les ajouts M-6, M-10, M-11 ; confiance haute. »

**m-8. Les noms « D1 » à « D6 ».** « D1, D2, D3 » sont aussi, dans `CLAUDE.md`, des décisions du brief rangées en « proposer avec recommandation », avec un défaut sous 48 heures. La collision peut faire croire à un défaut. Écrire « décision 1 : texte neuf… » et suivre la règle « nommer ce que c'est ».

**m-9. L'invariant de N-053 n'est écrit nulle part.**
- Ajout au § 3, ligne 6 : « Intensité égalée par la divergence des sorties et la norme du déplacement à la couche lue ; aucun score de sonde dans l'entraînement, le choix, l'arrêt ou l'exclusion d'un adaptateur (invariant de N-053) ; contrôle de manipulation par l'oracle du coût seul, règle écrite d'avance. »

**m-10. Le cadrage de D3 sert un signe (R3).**
- Avant : « - Enjeu : sans elle, un positif de la première lecture n'est pas lisible. »
- Après : « - Enjeu : sans elle, aucune issue de la première lecture (nul, positif, contraire) n'est lisible sans réserve de chemin de calcul. »

**m-11. Le résumé des données brutes omet le sous-ensemble d'activations** : 576 actions, couche 15, par jeton, états d'origine. Il permet de localiser, jeton par jeton, où s'allument les sondes de couche 15 (dose 0,75 pli e0, dose 1, instruit), notamment dans le champ du coût. C'est un calcul au processeur, sous le texte neuf.
- Ajout après « Perdus : les activations complètes et les textes de distillation. » : « Gardé : un dixième des actions à la couche 15, par jeton (1,06 Go). »

**m-12. « 800 directions aléatoires ».** Écrire « 800 directions tirées dans la covariance des jetons d'apprentissage de chaque sonde ».

**m-13. Incohérence de coût.** « 18 à 47 USD » au § 1 contre « 17 à 19 » au § 3 : écrire « 17 à 47 ». Le pire cas des paires n'est écrit nulle part ; le devis du témoin distillé honnête donne environ 24,6 USD pour un adaptateur au pire.

**m-14. Géométrie des poids.** Le nul de référence est celui des 800 directions du plancher, non une direction isotrope. B écrit « 0,079 au millième » sous un nul isotrope ; il ne faut pas le citer. L'écriture de l'adaptateur dans le flux ne se borne pas à ses matrices de sortie : les termes ajoutés à q, k et v passent par la matrice de sortie de base et par les couches suivantes. À dire « un alignement faible n'acquitte pas, un alignement fort n'accuse qu'à cette couche ».

**m-15. Intensité.** La note écrit « intensité mesurée égale » sans définir la mesure. Il en faut deux : la divergence des sorties, et la norme du déplacement à la couche lue. L'égalité est exigée sur les deux, ou l'écart est rapporté.

**m-16. Partage de l'accord reporté (D2, option a).** Les étapes 4, 5 et 6 ensemble peuvent dépasser 30 USD (4,6 + 4,6 + 17 à 47). Le report doit dire le plafond et l'ordre des pièces.

**m-17. Réserve 1, chiffres de Fable dépassés** (corrigé par M-1).

**m-18. Intervention.** La puissance de 0,98 suppose des directions témoins presque inertes (écart type 0,02 dans la simulation de B). La littérature que la note cite dit qu'une direction placebo de même norme agit autant (2610.22460, p. 8, via N-034 ; 2607.25907, PDF non versé). À écrire « puissance si les directions témoins sont inertes ; à rechiffrer avec des témoins actifs ».

## 4. Conformité aux règles

- **Préenregistrement (R1)** : non conforme sur deux points.
  - L'exposition des concepteurs aux résultats de l'étape B bis n'est pas déclarée (B-2).
  - L'épreuve à vérité plantée est placée avant le texte et hors de lui (B-3).
- **Aucun run visant un signe positif (R3)** : conforme sur le fond. Le cadrage de la décision 3 est à corriger (m-10).
- **Symétrie (R4)** : non conforme. Nul et positif ne reçoivent pas la même réserve (B-1). Aucune issue contraire n'est prévue (B-2). L'audit gelé est absent (M-11).
- **Provenance vérifiée sur PDF (R7)** : conforme.
  - 2610.12445 est vérifié de nouveau par moi (p. 1, 9, 12, 26, 33).
  - Cooney et al. et l'effacement de concept sont marqués « non vérifiés ».
  - Une nuance est à ajouter (m-4).
- **Anti-faux-trou (R8)** : conforme. Aucune zone n'est déclarée libre. « Le précédent publié » est à écrire « un précédent ».
- **Invariant de N-053** : non violé par le plan, mais non écrit (m-9).
- **Règle « qui conçoit »** : non tenue par le calendrier (M-1).
- **Interdit de la moyenne sur les jetons** : risque à l'étape 4 (M-10).

## 5. Nœuds manquants

1. **Qui conçoit avant le 22 novembre 18:00Z** : quota de Fable ou changement de modèle (R-3791, R-3794 : nœud rouvert).
2. **Réemploi des adaptateurs de la course exploratoire** (étape 5) : données versées, interdites sous les deux textes scellés. Il faut un texte contre-lu et ton mot.
3. **Dépenses des étapes 5 (2,5 à 4,6 USD) et 7 (6 à 20 USD)** : absentes de la liste des décisions.
4. **Contact externe pour l'épreuve où « le tiers tire lui-même le monde »**, distinct de l'envoi au statisticien.
5. **Publication des scores par action et du programme** (« publiés »).
6. **Sens du contraste « textes du saboteur relus sous le modèle nu contre l'honnête »** dans le texte neuf : soutien, réserve ou simple effet principal. C'est un nœud du socle, absent de la décision 1.
7. **Recouvrement des paires répliquées avec le second cycle gelé** (GO-2026-11-19-27) : même recette, témoin de même intensité et second témoin honnête. À trancher : dégel, rattachement, ou place parmi les trois chantiers actifs.
8. **Changement de modèle pour les organismes publiés** (Qwen3.6-27B, décision 6), en plus de la décision R-122 et du contact.
9. **Choix de la phrase du dossier de l'entretien sur le barreau 5** : il revient à Lazar (note 02, nœud 6).

Options manquantes à des nœuds présents :
- lire les lignes gratuites du texte scellé pour les sondes génériques (décisions 1 et 2 ; M-9) ;
- plafond et partage de l'accord reporté (décision 2 ; m-16) ;
- niveau des épreuves d'après l'entretien (décision 4 ; M-6) ;
- témoin à changement bénin dans les paires (décision 4 ; M-8).

## 6. Faits de la note relus à leur source

| affirmation de la note | source relue | état |
|---|---|---|
| Un seul adaptateur saboteur ; les 640 actions sont des mesures répétées d'une unité | socle § 3 ; note 03 (f) | conforme |
| Étiquette d'apprentissage confondue avec l'adaptateur | socle 0.3 (code l. 357) | conforme |
| Interaction confondue avec le chemin ; égalité vérifiée sur 8 épisodes sur 64, au modèle nu et à la dose 1 | lignes descriptives v2, l. 151 ; résumé de l'audit, l. 26-33 | conforme ; vaut aussi pour le contraste A lui-même |
| « Une demi-heure de carte » | texte de l'étape B bis, l. 213 ; devis de la relecture, l. 218-224 | trop bas pour une course neuve (§ 2.8) |
| 93,5 % ; 99,5 % ; 47,5 % | sortie de C, bloc P4 | exacts, mais pour quatre adaptateurs par bras (B-3, § 2.6) |
| 0,62 à 0,68 ; 0,09 à 0,16 ; 0,13 à 0,19 | sortie de A | exacts dans A ; niveau unilatéral ; tendance au plancher supposé (§ 2.1 à 2.3) |
| 0,88 à 0,99 (six paires) ; 90 % (4 contre 4) ; 0,98 (intervention) | sorties de B et de C | exacts à 5 % ; nuls à 1 % (§ 2.4) |
| 0,80 à 0,97 (effacement) | sortie de B, simulation 2 | exact ; effacement estimé sur les jumeaux (m-3) |
| 17 à 19 ; 34 à 37 ; 47 USD | conception B, § 2 bis | arithmétique exacte (§ 2.8) |
| « Caught in the Act », p. 26 ; figure de tête | PDF versé, empreinte égale | vérifié, avec deux nuances (m-4) |
| Poids des organismes de l'institut britannique publiés | PDF 2610.12445, p. 12 (lien vers les poids) | conforme ; Cooney et al. bien marqué « non vérifié » |
| Limite de Fable jusqu'au 22 à 18:00Z | `registres/decisions.md` l. 3929, 3930, 3932 | dépassé : disponibilité intermittente, nœud rouvert (M-1) |
| Accord de 30 USD, échéance le 27 | `registres/go.md` l. 297 | conforme |
| Scores bruts linéaires, maximum ou attention sur les jetons | `sondes/familles.py` l. 75-81 ; `harnais/sondes.py` l. 63-82 | conforme ; donne sens aux différences appariées brutes (B-2) |
