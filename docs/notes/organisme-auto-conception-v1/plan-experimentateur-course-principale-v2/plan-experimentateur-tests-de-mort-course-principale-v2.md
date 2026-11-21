# Plan du branchement — l'expérimentateur et l'étage des tests de mort sur la course principale d'auto-conception — v2

**La note est intégrée.** Cette v2 cite la note de conception générale des expérimentateurs et des tests de mort, lui confronte la décision D2, récrit les lots E2 et E3, rechiffre le calendrier et le devis du bac, et liste ses nœuds N1 à N7. La v1 (`0bb27bc0a1f262daa41ad1f7746c34a2d423a90354e834d6f6874eee1f80d8e7`) reste telle quelle (règle R12).

Pièce de travail (classe C), non contre-lue, non scellée. Elle planifie ; elle ne tranche rien. Processeur seul : aucun appel, aucune dépense, aucun code lancé, aucune écriture dans un dépôt.

- Auteur : planificateur du branchement de l'expérimentateur, modèle F. Je n'ai écrit aucun orchestrateur, aucune conception de véhicule, aucune pièce du palier 1, ni la note, ni le plan du pilier mathématique.
- Date (UTC) : 2026-11-21 ; relevé de `date -u` : 07:42:34Z, après la lecture des pièces neuves, avant l'écriture.
- Mandat : celui de la v1 (`e4ca4586…`), et le message de la mère qui commande la v2.
- Lecture neuve : `origin/main` du dépôt de l'organisme au commit `5cf69138da10eee73e94a221d5802e6f415b4272`. Six pièces, toutes à l'empreinte annoncée (table jointe).
- Ce texte ne porte aucun identifiant de modèle, aucun nom de clé, aucune méthode d'attaque.

Sigles neufs : NC, la note de conception générale (`4f3ae86f…`), non contre-lue ; PM, le plan d'avancée du pilier des mathématiques nouvelles (`1616e709…`) ; DM, le devis de son pilote (`6f485216…`). Les sigles de la v1 valent toujours (A69, C70, R68, F68, L10, NA, DH).

**Réserve sur PM, son préenregistrement (brouillon 1, `7f04e367…`) et DM**, dite par la mère : ces pièces ne sont pas contre-lues, et leur auteur a été servi sur un autre modèle que celui que prévoit la règle « Qui conçoit ». Tout ce que j'en cite porte cette réserve.

## 0. En bref

1. **La note répond à D2.** Une carte d'auto-conception meurt ou tient par une course appariée de l'organisme, avec et sans son mécanisme, sur des mondes à lois plantées scellés d'avance. D'abord sur un banc à proposeurs écrits par programme ; ensuite, pour les seules cartes qui tiennent, avec de vrais proposeurs, sur devis (NC, § 2.2). C'est une proposition : son nœud N1 n'a pas de défaut et reste à Lazar.
2. **Le premier emploi ne demande aucune génération neuve.** Les quatre premiers pas de la note portent sur les 94 cartes de la course v9. La boucle à plusieurs générations avec étage (lots E5 et E6) sort donc du chemin critique.
3. **Treize lots** pour cette course : les dix de la v1, dont E2 et E3 récrits, plus trois lots communs posés par la note (C1, C2, C3). Deux autres lots de la note appartiennent à d'autres chantiers (M1, S1).
4. **Calendrier** : de 45 à 54 heures de code et de vérification, de 23,5 à 59 heures de textes. Le chemin critique est le texte de la porte, non le code. Table d'admission à 0 USD : trois à quatre jours. Premier dollar, la mesure de l'expérimentateur sur les témoins : pas avant le 28 novembre.
5. **Devis du bac** : l'unité n'est plus la tentative par monde, c'est la carte. Bas 7 heures, haut 26, pire 48 ; de 0,51 à 13,44 USD selon la machine. Plafond proposé inchangé, 15 USD, avec une durée maximale de 48 heures.
6. **Quatorze décisions** : sept nœuds posés par la note, six décisions posées par la v1 et gardées, une décision neuve posée ici (D8, la lecture des cartes). La mère a déjà accordé D3 et D4.

## 1. Ce qui existe

Le § 1 de la v1 vaut, pièce par pièce. Ce que la lecture neuve y ajoute ou corrige :

| pièce | chemin, empreinte | état |
|---|---|---|
| note de conception générale | `docs/notes/experimentateurs-et-tests-de-mort-v1/conception-branchement-experimentateurs-tests-de-mort-v1.md`, `4f3ae86f…` | classe C, **non contre-lue** ; lue en entier ; elle propose |
| calculs de la note | même dossier, `calculs-conception-tests-de-mort-v1.py` (`301c0f52…`) et sa sortie `.txt` (`9b66cc78…`) | non contre-lus ; empreintes vérifiées, contenu non ouvert |
| plan d'avancée du pilier mathématique | `docs/notes/mathematiques-nouvelles-v1/plan-d-avancee-mathematiques-nouvelles-v1.md`, `1616e709…` | classe C, non contre-lu, réserve de la mère ; lu en entier |
| préenregistrement du pilote « oracles plantés », brouillon 1 | `prereg/mathematiques-nouvelles-v1/preenregistrement-pilote-generation-v1-brouillon.md`, `7f04e367…` | non scellable (blancs nommés), même réserve ; empreinte vérifiée, non ouvert |
| devis du pilote | `prereg/mathematiques-nouvelles-v1/devis-pilote-generation-v1.md`, `6f485216…` | même réserve ; lignes de la machine et des plafonds lues |
| code v6 du palier 0b | comparateur sans juge, enveloppe à lots de douze, exécuteur, trois artefacts (NC, § 1) | écrit, lancé le 21 novembre ; aucune sortie lue, ni par la note ni par moi |
| banc à lois plantées de la ligne 1 | `banc_ligne1_v1.py`, `ccc97ea2…` (NC, § 1) | base proposée du banc de course ; **qu'il se rende greffable sans réécriture n'est pas établi** (NC, § 6) ; non ouvert par moi |
| définition scellée de « mieux » | `docs/notes/organisme-auto-conception-v1/course-v2/definition-amelioration-considerable-v9-v1.md`, `4eae96bc…` (NC, § 2.2) | scellée ; trois cas (validité, rendement, cumul) ; non ouverte par moi |
| conception v2 de la course « seuil et moniteurs » | `…/ideation-seuil-moniteurs-v1/conception-v2/ordre-course-seuil-et-moniteurs-v2.md`, `1fbd04c3…` (NC, § 2.2) | la v1 de ce plan ne l'avait pas trouvée ; toujours non ouverte par moi |

**Trois faits que la note établit et que la v1 n'avait pas.**
1. Le seul relevé réel, à la course v67 : au plus 0,081 USD par test pour l'expérimentateur et 0,061 pour le lecteur, appels de proposeur compris (NC, § 1). La v1 disait ce coût non isolé.
2. Le modèle qui jouait l'expérimentateur à la v67 est absent des courses récentes ; aucun n'est nommé à sa place (NC, § 1). D'où son nœud N4.
3. L'additif scellé de la v69 se lit sur `main` sous `prereg/organisme-auto-conception-v9/orchestrateur-v69/` (NC, § 1) ; la v1 l'a lu sur le disque sous `docs/notes/…/epreuves-v9/orchestrateur-v69/`. Même empreinte, `cb352811…`.

## 2. D2 confrontée au § 2.2 de la note

### 2.1 La réponse de la note

Des trois lectures du § 2.1 de la v1, la note retient la troisième, et la rend jouable par deux barreaux.

| | barreau 1, la course de banc | barreau 2, la course réelle appariée |
|---|---|---|
| l'organisme | un banc écrit par nous : proposeurs écrits par programme, fonctions de jugement de l'orchestrateur, mondes à lois vraies et fausses plantées | l'organisme réel, vrais proposeurs, tests de mort réels dans la boucle |
| la carte y entre comme | un greffon : une fonction appelée une fois par génération, dans le bac, qui ne reçoit que ce que recevait le mécanisme remplacé, jamais la vérité | le même greffon, branché |
| bras, sur les mêmes graines | sans ; avec ; placebo de même forme ; bases bon marché du point de greffe, en liste fermée | avec et sans, mêmes mondes |
| ce que le noyau compte | lois vraies et fausses promues, coût | les mêmes |
| issue | « invalide » si plus de lois fausses promues que le niveau annoncé ; « sans gain » si l'écart apparié ne passe pas le seuil de son cas sur des familles tenues à l'écart ; sinon « tient au banc », qui n'est pas une adoption | « tient » ou « ne tient pas » |
| coût | du processeur ; l'expérimentateur se paie une fois par carte | de l'ordre de 590 USD par carte à cinq espèces, 90 à deux (NC, § 2.2, point 4) |

Avec quatre règles (NC, § 2.1) : aucun agent n'écrit le critère de mort ; le code d'un agent rend une décision, jamais une mesure ; l'épreuve passe d'abord ses témoins plantés ; un mort reste mort.

### 2.2 Ce que la note règle des objections de la v1

| point de la v1 | réponse de la note |
|---|---|
| « aucune tranche de données n'existe pour cette course » (§ 2.1, point 2) | le manque n'est pas une tranche, c'est l'objet servi à l'étage : l'orchestrateur écrit la fiche de l'étage, tranche faite de l'interface et d'un petit journal factice du banc, les mêmes pour toutes les cartes |
| « l'étage refuserait chaque fiche » (§ 1.3) | l'étage v5, sans un octet changé, sert à écrire, exécuter et sceller le greffon ; le verdict vient après, par rejeu sans appel |
| D2, option (a) : « un proposeur écrit le test que sa carte passe » | il choisit un cas et une taille, jamais l'épreuve ; les seuils de la définition scellée font plancher |
| D2, option (b) : « le pont décide de ce qui est éprouvé, sans texte qui le fonde » | le pont ne remplit que des champs fermés, chaque valeur avec l'extrait qui la fonde, vérifié à l'octet par programme, par deux traducteurs de deux lignées ; ce qui ne se met pas en forme est « hors gabarit » |
| D2, option (c) : « l'étage actuel ne le joue pas ; coût sans commune mesure » | le barreau 1 la rend bon marché ; le barreau 2 garde ce prix, pour les seules cartes qui tiennent |
| « l'oracle dépend du juge statistique » (§ 2.1, point 3) | le comparateur sans juge du palier 0b ; un essai : permuter les sorties de juges laisse les issues identiques à l'octet |
| le coût du test, de 0,06 à 0,90 USD par tentative (§ 5.3) | ces bornes valent pour un script de loi ; un greffon pèse plus, inconnu à un facteur cinquante près ; à mesurer d'abord sur les seuls témoins |

### 2.3 Ce que la note tranche

**Rien.** Elle est une pièce de travail non contre-lue ; elle recommande l'option (a) de son nœud N1, confiance 0,7, sans défaut. Ce que je tiens pour acquis pour planifier, et seulement pour planifier : la forme de l'épreuve (course appariée, banc d'abord), puisque la mère me demande de récrire E2 et E3 sur elle.

### 2.4 Ce qui reste ouvert, que la note dit elle-même

1. Le banc de la ligne 1 se rend-il greffable sans réécriture ? Non établi.
2. L'étage v5 accepte-t-il la fiche écrite par l'orchestrateur ? « À confirmer sur le code. »
3. Le coût d'un greffon : entre 0,08 USD et 4 USD, ordre de grandeur sous hypothèse.
4. La part des 94 cartes par barreau, et le nombre de cartes hors gabarit : inconnus, aucune carte n'ayant été ouverte.
5. `numpy` dans le bac de la machine louée ; la durée d'une exécution nue ; le bac n'offre que la bibliothèque standard.
6. « Tient au banc » ne vaut que sous des proposeurs écrits par programme.

**Ce que j'ajoute.** (i) Les seuils par cas viennent de la définition scellée `4eae96bc…`, que je n'ai pas ouverte : qu'elle porte un seuil chiffré pour chaque cas est à vérifier avant le texte de la porte. (ii) La liste fermée des points de greffe et celle des bases bon marché n'existent pas. (iii) Les quatre mécanismes témoins (utile, neutre, surajusté, nuisible) sont des formes ; aucun n'est écrit.

### 2.5 Ce qui reste à Lazar

N1 (la forme de l'épreuve), N2 (les champs de fiche, qui rouvre 3a), N3 (un seul texte scellé pour la porte, lecture de la règle R1), N4 (le modèle de l'expérimentateur) ; et D8, posée ici : qui lit les cartes (§ 7).

## 3. Ce qui manque, après la note

Le § 2 de la v1 se relit ainsi.

| v1 | v2 |
|---|---|
| § 2.1, l'objet de l'épreuve, les données, l'oracle, les mondes | répondu en proposition par NC, § 2.2 ; manquent le banc de course greffable, les mondes à lois plantées, les mécanismes témoins, la table d'admission, le texte de la porte |
| § 2.2, points 1 et 2 : sommet d'étage, enveloppe | inchangé, avec un paramètre : la forme d'épreuve, la forme imposée du tour fermé restant la seule admise en réel tant qu'un additif n'en nomme pas d'autre (NC, § 3.1) |
| § 2.2, point 3 : le pont | précisé : pont à extrait cité, deux traducteurs, gabarit « mécanisme » |
| § 2.2, point 4 : classes d'issue | celles d'A69, plus les motifs « invalide » et « sans gain », plus les statuts « hors gabarit » et « non éprouvée (épreuve morte) » (NC, § 2.3) |
| § 2.2, points 5 et 6 : boucle à plusieurs générations, lecture | **hors du premier emploi** ; requis au pas 5 de la note seulement |
| § 2.2, point 7 : récompense de l'héritage | réponse de la note : l'issue par tentative et son coût, rien de plus fin, mondes neufs par génération, mesure finale lue une fois ; rien de servi d'ici la lecture de l'épreuve de l'héritage (NC, § 2.5) |
| § 2.2, point 8 : les juges | réponse de la note : pour information, jamais un choix ni un repêchage |
| § 2.3 : lanceur, additif, préenregistrement | une table des épreuves dans le lanceur 11 ; un additif par épreuve ; un préenregistrement de la porte plutôt qu'un texte par carte, si N3 l'accorde |
| § 2.4 : le bac | trois lieux : le bac, la machine jetable, la mère ; **ni clé ni vérité sur la machine** ; rejeu du script scellé, seul code neuf du côté de la machine ; inventaire et versement scellé avant destruction |
| § 2.5 : mesures et gardes | plus les huit gardes de NC, § 2.6, chacune avec son cas sain et son artefact |

Manques neufs : le compte des cartes par un agent habilité (NC, § 4.1, pas 1) ; deux traducteurs de deux lignées, dont aucune n'est l'expérimentateur ; un modèle pour l'expérimentateur.

## 4. Les lots

### 4.1 E2 et E3 récrits

**E2 révisé — le pont à extrait cité et le gabarit « mécanisme ».**
- Contenu : la fiche à champs fermés d'une carte (point de greffe en liste fermée ; cas de la définition ; quantité, signe et taille de l'effet, sinon « lu au plus prudent ») ; le programme qui vérifie à l'octet chaque extrait cité ; la règle d'accord des deux traducteurs ; le statut « hors gabarit » ; le constructeur de la fiche servie à l'étage (texte de test imposé, tranche d'interface et de journal factice, statistique « nombre ») ; les gardes de l'entrée de l'expérimentateur.
- Dépend de : E0 ; N1 ; D8 ; la liste fermée des points de greffe, qui sort de E3.
- Écrit par un développeur O, vérifié par S. Les consignes des traducteurs sont un texte du modèle F.
- **Partagé avec la course « seuil et moniteurs »** : la mise en forme fixe par deux traducteurs et la vérification de l'extrait à l'octet sont celles de sa conception v2 (NC, § 2.2). Un seul programme de vérification d'extrait ; deux gabarits.
- **Avec le pilier mathématique** : rien du pont ; ses propositions sont écrites dans une grammaire fermée (PM, lot B1).

**E3 révisé — le banc de course greffable, les mondes à lois plantées, les mécanismes témoins.**
- Contenu : le banc (lignées de proposeurs écrites par programme, fonctions de jugement, journal des entrées exactes de chaque décision) ; un point de greffe par étage du trajet d'une carte ; le générateur de mondes à lois vraies et fausses plantées, par graine dérivée par monde et par course (règle R9), racine gardée avec la vérité ; les familles tenues à l'écart ; les bras (sans, avec, placebo, bases en liste fermée) ; les quatre mécanismes témoins et leur sort attendu ; le banc d'étalonnage, qui joue toute la banque à 0 USD et scelle la table d'admission.
- **Les témoins d'abord** : aucune carte ne passe avant que la table d'admission soit scellée ; un témoin « doit mourir » qui tient fait une épreuve morte, arrêt rapporté, jamais un repli.
- **L'issue se calcule chez la mère** : le banc et la vérité ne montent jamais sur la machine jetable ; n'y montent que l'interface et les lots de mise au point.
- Dépend de : E0 ; N1 ; le comparateur du palier 0b ; la lecture de la définition scellée.
- **Partagé avec le pilier mathématique** : le programme de tirage, de disjonction et de scellement des clés de mondes est de même nature que son générateur à trois familles (PM, lot B1) ; ses mondes sont des miniatures finies de deux de ses questions. Je propose un seul module « graines, disjonction, clé scellée, famille tenue à l'écart », deux générateurs. Le lot M1 de la note (contre-exemples exacts) reste au pilier.
- **Partagé avec la course « seuil et moniteurs »** : le même module ; ses mondes à scores plantés sont le lot S1 de la note, compté par sa conception v2.
- Heures : 8 à 15 (NC, § 3.3), au lieu de 3,75.

### 4.2 La table des lots

| lot | contenu | dépend de | partagé avec | premier emploi ? |
|---|---|---|---|---|
| E0 | relevé du code, sans écriture ; aux huit questions de la v1 s'ajoutent : le banc de la ligne 1 est-il greffable ; l'étage accepte-t-il la fiche écrite par l'orchestrateur ; `numpy` dans le bac | — | NA-1, lot 0 | oui |
| C1 | texte de la porte pour cet emploi : gabarit, banque de témoins, critères, table d'admission (classe A) | N1, N3 ; E3 pour les empreintes | un texte par emploi ; la forme est commune aux trois | oui, **chemin critique** |
| E3 révisé | § 4.1 | E0, N1 | pilier mathématique, « seuil et moniteurs » | oui |
| C2 | mesure hors machine, porte des lots (composition par graine avec témoins, épreuve morte, statuts), registre et garde « un mort reste mort » | E3 | **les trois emplois** ; remplace le cœur du E4 de la v1 | oui |
| E2 révisé | § 4.1 | E0, N1, D8 | « seuil et moniteurs » | oui |
| E1 | sommet d'étage et enveloppe | E0 ; palier 0b | **palier 1 : c'est la v69**, écrit une fois | oui, pour le pas 3 |
| C3 | rejeu du script scellé ; paramètre de forme d'épreuve du sommet d'étage | E1 | les trois emplois | oui, pour le pas 3 |
| E4 | ce qu'il en reste : la projection des classes dans les fichiers de la course | C2 | palier 1 | oui, petit |
| E7 | mesures et export | C2 | forme de NA-1, lot 7 | oui |
| E8 | lanceur : table des épreuves, épinglages, parts, machine déclarée, durée de location, attestation du bac, ligne d'accord ; **en régime « étage seul » pour le premier emploi** | E1, C3 | « seuil et moniteurs », que Lazar a mise en étage seul (GO-2026-11-21-16) ; A69, § 7 ; NA-1, lot 8, pour les relais | oui, pour le pas 3 |
| E9 | mise en route et essai du bac, inventaire et versement avant destruction, essai à blanc de bout en bout | E7, E8 | palier 1 ; NA-1, lot 9 | oui, pour le pas 3 |
| E5 | course à plusieurs générations avec étage | E1, E2, E4 | base v68 | **non** : pas 5 |
| E6 | lecture du registre par la génération suivante | E4, E5 | NA-1, lot 5 | **non** ; D4 accordée : rien de servi à la première course |

Hors de ce plan : M1 (banc de contre-exemples exacts, au pilier) et S1 (mondes à scores plantés, à la course « seuil et moniteurs »).

**Ordre pour le premier emploi.** À 0 USD : E0 ; puis E3 et le brouillon de C1 ensemble ; puis C2 et E2 ; table d'admission scellée ; compte des cartes. Pour le premier dollar : E1 et C3 ; E8 et E9 ; additif, devis, ligne. E5 et E6 après.

**Ce qui ne s'écrit pas deux fois.** Avec le palier 1 : le sommet d'étage, l'enveloppe, les classes, l'essai du bac, la garde de durée. Avec la course « seuil et moniteurs » : la vérification d'extrait, le lanceur en étage seul, C2, C3. Avec le pilier : le module des graines et des clés, C2 pour le registre. Avec NA-1 : le relevé du code, les relais, le faux fournisseur.

## 5. Le calendrier, rechiffré

La note change deux lots et en ajoute trois. Heures de session, sans appel ; mêmes repères que la v1 et que NC, § 3.3.

| | v1 | v2 |
|---|---|---|
| lots de code E0 à E9, E3 à 3,75 | 37,75 | — |
| E3 révisé | — | 8 à 15, soit 4,25 à 11,25 de plus |
| C2 | — | 2 à 3 |
| C3 | — | 1 à 2 |
| **code et vérification** | **37,75** | **45 à 54** |
| dont premier emploi (sans E5 ni E6) | — | 36,5 à 45,5 |
| textes autour, hors mondes et porte | 20 | 20 |
| mondes scellés d'avance | 3 | dans C1 |
| C1, texte de la porte de cet emploi | — | 3,5 à 39 |
| **textes** | **23** | **23,5 à 59** |
| **somme** | **environ 61** | **68,5 à 113** |

La borne haute de C1 est le repère mesuré du texte du palier 0b : 39 heures du mot de Lazar au scellement (NC, § 3.3). **Les textes décisifs sont le chemin critique, pas le code.**

**Horloge.**
- Table d'admission scellée, à 0 USD : trois à quatre jours après le mot sur N1, soit le 24 ou le 25 novembre au plus tôt, si E0 confirme que le banc de la ligne 1 se greffe.
- Premier dollar, la mesure de l'expérimentateur sur les témoins : il faut en plus le sommet d'étage, le lanceur, le bac, un additif, un devis contre-lu, une ligne, et N4. **Pas avant le 28 novembre** ; début décembre si le texte de la porte prend le rythme du palier 0b. La v1 disait le 26 au plus tôt : la note recule le premier dollar et avance le premier résultat sans dépense.
- Une issue par carte, sur processeur : après la mesure, et après D8.

**Ce que je ne peux pas dater** : N1, N3, N4 et D8 ; la lecture du palier 0b ; la place du modèle F, que NA-1, le pilier mathématique (PM, § 4 : son pilote vers le 23 au plus tôt) et la course « seuil et moniteurs » se disputent.

## 6. Le devis du bac, rechiffré

**Aucun prix n'a été relevé aujourd'hui.** Calculs à la main.

### 6.1 Ce que la note change

1. **L'unité est la carte, non la tentative par monde.** L'expérimentateur écrit un greffon une fois ; le greffon scellé se rejoue sans appel. Les 282 et 564 tentatives de la v1 n'ont plus d'objet au premier emploi.
2. **Le banc d'étalonnage se joue en local, à 0 USD.** Aucune machine louée avant la mesure de l'expérimentateur.
3. **Ni clé ni vérité sur la machine** : la mesure se fait chez la mère. La machine porte les sessions de l'expérimentateur et l'exécution du greffon sur les lots de mise au point.
4. **Deux tarifs lus**, non un : 0,0675 à 0,0733 USD de l'heure (petite machine, F68) ; 0,28 USD de l'heure pour la machine à processeur que le pilier retient, borne haute du programme 1,30 (DM, l. 15, sous la réserve de la mère). La note dit de 0,07 à 0,28 USD par location relevée.

### 6.2 Trois cas, location seule

| cas | hypothèses | heures | à 0,0733 | à 0,28 | à 1,30 |
|---|---|---|---|---|---|
| bas | mesure sur les témoins puis 94 cartes au rythme de la v67 (3,25 minutes), une heure de mise en route | 7 | 0,51 | 1,96 | 9,10 |
| haut | 94 cartes et 12 témoins, 9 minutes chacun ; 8 heures d'exécutions de mise au point ; 2 heures de mise en route | 26 | 1,91 | 7,28 | 33,80 |
| pire | la durée maximale de location atteinte | 48 | 3,52 | 13,44 | 62,40 |

**Plafond proposé pour le poste : 15 USD, durée maximale de location 48 heures**, tenue par du code (A69, garde 20). Il tient jusqu'à 0,31 USD de l'heure ; au-delà, le devis se refait. Le nombre de témoins (12) et les 8 heures de mise au point sont mes hypothèses.

### 6.3 Ce qui n'est mesuré nulle part

1. **Le coût d'un greffon en appels** : de 0,08 USD (relevé de la v67, pour un script de loi) à 4 USD (plafond d'un autre brouillon, non mesuré). Pour la mesure sur 4 à 12 témoins : de 0,32 à 48 USD. Pour 94 cartes : de 7,5 à 376 USD, moins les cartes hors gabarit, dont le nombre est inconnu.
2. **Les deux traducteurs** : deux appels par carte, coût non chiffré par la note.
3. **Le barreau 2** : de l'ordre de 590 USD par carte à cinq espèces, 90 à deux ; sur devis à part, après les issues du banc.
4. La durée d'une exécution nue du bac ; `numpy` dans le bac ; le prix du jour.

**Lecture.** La location reste négligeable. La première dépense à demander est petite et bornée par le nombre de témoins fois le plafond par greffon ; elle donne le chiffre sans lequel aucun devis des 94 cartes n'est honnête.

## 7. Les décisions

Aucun défaut pour une dépense. Aucune n'est prise ici.

### 7.1 Nœuds de Lazar posés par la note

| nœud | décision | recommandation de la note | défaut |
|---|---|---|---|
| N1 | ce qu'un test de mort éprouve sur une carte d'auto-conception : (a) course appariée à deux barreaux, pont pour les 94 cartes ; (b) course réelle seulement ; (c) engagement écrit par le proposeur | (a), 0,7 | aucun |
| N2 | champs de fiche des courses suivantes, qui rouvre 3a : (a) trois champs fermés de plus, dix gardés ; (b) inchangés, pont pour toujours | (a) pour la suite, (b) pour les 94 cartes ; 0,65 | aucun |
| N3 | un seul texte scellé pour la porte commune, et par carte un engagement en forme fixe ; ou un texte par ligne | le texte unique pour les cartes sans texte scellé ; 0,6 | aucun : lecture de la règle R1 |
| N4 | modèle et plafond de l'expérimentateur d'épreuve : (a) une autre lignée que le lecteur témoin, nommée par Lazar, plafond après la mesure ; (b) attendre celui de la v67 ; (c) deux lignées partout | (a), avec une seconde implémentation sur un tirage ; 0,6 | aucun |
| N5 | règle de l'épreuve morte : (a) un témoin « doit mourir » qui tient annule ; un « doit tenir » qui meurt est compté, annule au-delà d'une borne gelée ; (b) annulation dans les deux sens | (a), 0,65 | (a) sous 48 heures |
| N6 | où se calcule l'issue : (a) chez la mère ; (b) sur la machine, vérité hors du bac | (a), 0,8 | (a) sous 48 heures |
| N7 | ordre au pilier mathématique : (a) les épreuves d'abord ; (b) la génération tout de suite | (a), 0,75 | (a) sous 48 heures pour la conception |

N1 est la D2 de la v1 : je retire ma D2 au profit de N1, et je ne recommandais rien avant la note. Après lecture, j'appuie (a), confiance 0,65 : un cran sous la note, parce que rien n'établit encore que le banc existant se greffe.

### 7.2 Décisions posées par ce plan

| décision | état | ce que la note y change |
|---|---|---|
| D1, étendre le régime « tests de mort réels » à la course principale | posée ; recommandation (a), 0,7 | la note propose qu'étendre le régime soit ajouter une ligne scellée à une table des épreuves, non un interrupteur ; l'allumage reste un nœud |
| D3, nom de version | **accordée par la mère : « AC-1 »** (dit par son message ; ligne de registre non lue par moi) | la note confirme la collision : 68 à 71 et 74 |
| D4, ce que lit la génération suivante | **accordée par la mère : rien de servi à la première course** (même source) | la note l'appuie |
| D5, ordre entre cette course, NA-1 et le palier 1 | posée ; recommandation (a), 0,6 | renforcée : le sommet d'étage s'écrit une fois, paramétré, pour plusieurs générations ; j'ajoute que le banc et la porte partent tout de suite, à 0 USD, sans attendre le palier 1 |
| D6, la dépense | posée ; recommandation changée | **la première dépense à demander devient la mesure de l'expérimentateur sur les seuls témoins**, non plus l'attente du palier 1 ; confiance 0,6 ; aucun défaut |
| D7, préenregistrement de la course | posée ; recommandation (a), 0,75 | absorbée en partie par N2 et N3 : le texte neuf est celui de la porte pour les 94 cartes, et celui de la course pour les suivantes |

**D8 — Qui lit les cartes (neuve).**
- Décision : quel agent ouvre les 94 cartes de la course v9 pour les compter par barreau, puis les sert aux deux traducteurs ?
- Enjeu : la note demande ce compte avant tout devis ; elle n'a ouvert aucune carte, le dossier lui étant interdit. Le précédent connu est une exception bornée, une copie par programme sans ouverture (GO-2026-11-21-04).
- Options : (a) un agent neuf habilité par un mot de Lazar, qui ne rend que des comptes et des fiches à champs fermés. Avantage : le compte existe ; rien d'une carte n'entre ailleurs. Inconvénient : une exception de plus à un dossier fermé. (b) les traducteurs seuls, par programme, sans agent de compte. Avantage : une seule lecture. Inconvénient : aucun devis avant la traduction, donc une dépense à l'aveugle. (c) ne pas passer les 94 cartes ; la porte ne sert que les courses suivantes. Avantage : rien ne s'ouvre. Inconvénient : aucune carte éprouvée avant une course neuve.
- Recommandation : (a), confiance 0,6. Aucun défaut : accès à un dossier fermé, puis dépense des traducteurs.

## 8. Le pilier mathématique

Sous la réserve de la mère sur PM, son préenregistrement et DM.

**Ce que ce plan lui emprunte.**
1. La règle stricte « une proposition qui meurt reste morte », avec la mort héritée par toute reformulation équivalente (PM, § 5, point 2, et D-M5) : c'est la garde du registre de C2. Pour une carte d'auto-conception, l'analogue de la normalisation est la fiche à champs fermés : deux cartes de même fiche et de même greffon sont une seule tentative. À écrire au texte de la porte.
2. Le tarif et la minuterie de la machine à processeur : 0,28 USD de l'heure, destruction par identifiant à 48 heures (DM).
3. La forme « l'expérimentateur à modèle ne tue pas : mesuré, pas cru » (PM, § 5, point 3).

**Ce que ce plan lui doit.**
1. Le sommet d'étage paramétré (E1 et C3) : la forme « par arbitre » de la note en est une valeur ; le pilier ne récrit pas d'étage.
2. C2 : la mesure hors machine, la porte des lots, le registre.
3. Le module des graines, de la disjonction et des clés scellées, si la proposition du § 4.1 est retenue.

**Trois écarts à signaler entre PM et la note**, que je ne tranche pas.
1. PM, § 5, point 2, fait du test de mort « un calcul exact dans le bac » ; la note veut la vérité hors de la machine et l'issue chez la mère (N6). Si les faussetés plantées et leurs contre-exemples scellés montent sur la machine du pilote, N6 n'est pas tenu. PM prévoit un erratum d'alignement (son lot E1).
2. PM a lu le script des calculs de la note à l'empreinte `8223c37f…` ; celui qui est sur `main` est `301c0f52…`. La sortie est la même, `9b66cc78…`.
3. PM vise un premier dollar vers le 23 novembre ; ce plan, pas avant le 28. Les deux se disputent la même place de rédaction et le même sommet d'étage : l'ordre est à dire par la mère, avec N7.

Le chantier lui-même reste hors de ce plan : je n'en planifie aucun lot.

## 9. Réserves du planificateur

1. **La note n'est pas contre-lue**, ses calculs non plus. Ce plan s'appuie sur elle pour planifier ; il ne la vérifie pas.
2. **PM, son préenregistrement et DM** portent la réserve de la mère.
3. **Je n'ai ouvert** ni le banc de la ligne 1, ni la définition scellée de « mieux », ni la conception v2 de la course « seuil et moniteurs », ni le code du palier 0b, ni les calculs de la note, ni le brouillon du préenregistrement du pilote. J'en tiens ce que la note et PM en disent.
4. **Les heures et les cas sont des estimations**, calculées à la main ; douze témoins, huit heures de mise au point et quarante-huit heures de durée maximale sont mes hypothèses.
5. **D3 et D4 accordées** : je le tiens du message de la mère, non d'une ligne de registre lue.
6. Les réserves 2, 4 et 5 de la v1 valent toujours.

— planificateur du branchement de l'expérimentateur, modèle F
