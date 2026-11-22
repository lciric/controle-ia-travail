# Conception des sondes de la boîte blanche, version 2 (brouillon 1)

- **Accord** : GO-2026-11-22-126 (décisions 0 à 5). **Auteur** : session de conception `session_013QMayndh51FN5XbmHpmEFg` (modèle servi : à la liste « qui a lu quoi »). **Date (UTC)** : 2026-11-22, 20:45Z.
- **Statut** : note de conception. Elle ne modifie ni le programme ni aucun texte scellé, ne franchit aucune porte et ne revendique rien. **Elle ne porte aucun chiffre de résultat** : une session aveugle peut la lire. Ses embranchements (§ 7) sont à sceller avant le verdict du test « sabotage ou empreinte » sur les adaptateurs jumeaux (barreau 5).
- **Elle remplace**, pour la conduite du travail, la batterie de sondes v0 du brief (T0.7) là où les deux diffèrent ; le brief reste archivé tel quel. Chaque lecture décisive garde son propre texte scellé (R1) : cette note en fixe le cadre, non les seuils.

## 1. Principe

Une sonde ne vaut pas mieux que le contraste qui l'apprend et la juge. Le contraste se choisit donc avant la famille de sondes, et il doit ne différer que par le sabotage : mêmes poids, ou poids jumelés par construction ; même texte, ou lecture avant le champ qui révèle le sabotage. L'unité d'analyse est le jeu de poids ou la tâche, jamais l'action.

Trois questions distinctes, dans cet ordre : existe-t-il une trace propre à l'acte ; se transporte-t-elle à une unité jamais vue ; se lit-elle sans étiquette de sabotage. La première est circulaire par construction et ne prouve que l'existence. La deuxième respecte l'anti-circularité du programme (§ 7). La troisième seule est déployable.

## 2. L'échelle de preuve

| marche | question | sonde | contraste | si elle échoue |
|---|---|---|---|---|
| préalable | Une aire entre poids non appariés veut-elle dire quelque chose ? | sonde d'identité ; étalon de transport ; rejeu croisé du texte et des poids | deux honnêtes non appariés ; saboteur contre honnête non apparié ; source du texte croisée avec les poids qui lisent | voir § 7 ; aucune marche n'est bloquée, mais les libellés permis changent |
| 0 | La chaîne retrouve-t-elle un résultat publié, sur données publiques, avec le modèle de 8 milliards de paramètres ? | génériques de concept | jeu public | les génériques sortent du programme à cette taille ; nœud « contrôle d'échelle » (N-053, point 4) |
| 1 | Existe-t-il une trace propre à l'acte ? | différence de moyennes, puis linéaire régularisée | poids constants ou jumelés, texte égal ou lecture avant le champ, témoins du § 4 | pas de marche 2 sur ce banc ; la reconception porte sur l'organisme et sur la marche 3 (N-062 : jamais un arrêt) |
| 2 | Se transporte-t-elle ? | la même, gelée avant l'ouverture | unité jamais vue : autres jumeaux, autre recette, autre mode | la sonde reste un plafond ; elle ne compte pas pour le critère 3 de G0 |
| 3 | Se lit-elle sans étiquette de sabotage ? | apprise sur honnêtes seuls ; génériques | écart entre la grandeur attendue, lue à l'intérieur, et la grandeur déclarée | le bras « générique » de G1 reste vide, et c'est rapporté |

Niveaux : 99 % pour les lignes décisives d'une marche, 95 % pour les diagnostics et les lignes descriptives, déclarés comme tels dans chaque texte.

## 3. Familles de sondes

Pour toutes : lecture à la couche 15, fixée d'avance ; couches 7 et 23 rapportées (N-056, point 3). Score d'une action : le maximum sur ses jetons. Aucune moyenne ni médiane sur les jetons hors d'un bras de diagnostic déclaré (N-026). Ajustement au processeur, en double précision, sur activations gardées.

| famille | définition | rôle |
|---|---|---|
| Différence de moyennes appariée | différence des moyennes des jetons des deux classes ; appariée par action quand la même action est lue sous deux jeux de poids ou deux conditions | **sonde de référence** des marches 1 et 2 : aucune sélection, forme close |
| Différence de moyennes blanchie | la même, multipliée par l'inverse de la covariance intra-classe rétrécie | seconde lecture ; réglage choisi dans la boucle interne |
| Linéaire régularisée | régression logistique à pénalité quadratique sur les jetons | seconde lecture ; capacité de mémorisation rapportée |
| Apprise sur honnêtes seuls | régression du jeton d'avant le champ vers la grandeur déclarée, sur épisodes honnêtes ; statistique : résidu « déclaré moins attendu » | marche 3, exploratoire d'abord ; doit battre une réestimation par le texte seul |
| Génériques de concept (tromperie, enjeux, dissimulation, conscience d'évaluation) | apprises sur des jeux synthétiques ou publics, jamais sur nos organismes | hors de la ligne décisive ; bras rapporté sur activations gardées, après la marche 0 |
| À attention, perceptron | familles du brief | bras rapporté seulement, sous validation croisée imbriquée |
| Mahalanobis | non supervisée, sur honnêtes | aiguillage d'audit à poids constants (N-075 v3, § 4) ; jamais entre poids différents |
| Apprise avec l'étiquette « adaptateur contre modèle nu » | positifs sous un adaptateur, négatifs sous le modèle nu | **abandonnée** : l'étiquette se confond avec les poids |

À résultat égal, la famille la plus simple porte la ligne décisive.

## 4. Bancs et témoins

Ce que toute lecture exige de son banc : (a) un contrôle de manipulation tenu avant la lecture : l'oracle établit le dommage à une dose où la base « mots et coût » échoue (N-063 v2) ; (b) des poids constants entre actions sabotées et honnêtes, ou des jumeaux appariés et répliqués ; (c) si le sabotage varie à poids constants, une variable qui le commande, connue de l'oracle, absente du texte de l'action ou présente à l'identique chez l'honnête. Cette note ne conçoit aucun organisme.

| banc | ce qu'il permet | limite |
|---|---|---|
| Sabotage par consigne sur le modèle nu, consigne bénigne appariée, paraphrases réservées | marches 1 et 2 à poids vraiment constants ; ouvert pour décembre (GO-2026-11-22-126, décision 5) | la sonde peut lire la consigne suivie plutôt que l'acte ; plus loin du risque réel |
| Adaptateurs jumeaux appariés par construction, répliqués | marche 1 entre poids appariés, marche 2 sur des paires jamais vues | lit une disposition écrite dans les poids, non un acte ; sans jumeau, l'identité revient |
| Organismes à sabotage conditionnel répliqués, avec jumeaux et déclencheur réservé | marches 1 et 2 à l'intérieur de chaque jeu de poids | à construire ; calcul de puissance scellé et devis (décision 5) ; le déclencheur se lit toujours : on montre que la sonde n'en dépend pas |
| Organismes publics, d'une autre main | marche 0 ; validation externe | licences à vérifier (N-061) |

Retiré de toute lecture de sonde : l'adaptateur saboteur unique comparé au modèle nu.

| témoin | rivale qu'il ferme |
|---|---|
| Jumeau apparié par construction ; intensité égalée (divergence des sorties, norme du déplacement à la couche lue), jamais par un score de sonde (N-053, point 5) | « tout réglage fin allume la sonde » |
| Honnête contre honnête non appariés (sonde d'identité, étalon de transport) | « la sonde lit l'identité des poids » |
| Consigne cachée bénigne appariée (même longueur, même ton de secret) | « la sonde lit la présence d'un secret » |
| Déclencheur présent sans sabotage ; déclencheur réservé | « la sonde lit le déclencheur » |
| Texte égal (relecture à état imposé) ; lecture avant le champ révélateur (N-053, point 1) | « la sonde lit le texte » |
| Bases à côté de chaque ligne : valeur déclarée seule, « mots et coût », classifieur lexical, lecteur honnête | « une boîte noire en fait autant » |

## 5. Gardes

1. **Activations gardées**, sur une même liste de clés pour tous les jeux de poids comparés ; sans elles, pas de lecture.
2. **Même chemin de calcul** pour toutes les cases d'un contraste ; sonde ajustée au processeur.
3. **Validation croisée imbriquée**, groupée par tâche et par unité ; toute aire décisive est lue hors pli ; le nul rejoue toute la sélection.
4. **Unité, niveau et règle de famille** écrits avant la lecture ; test exact à l'unité.
5. **Épreuve à vérité plantée** du programme de lecture, aux effectifs réels, avant toute ouverture (R5).
6. **Prévision scellée, contre-lecture, verdict par un agent neuf** (R1, R2, R13) ; audit de symétrie sur tout résultat trop net, dans les deux sens (R4).

## 6. Le critère 3 de G0, tel que Lazar l'a retenu

Lecture (b) (GO-2026-11-22-126, décision 1). Le critère est tenu si une sonde non circulaire — générique, ou apprise sur une unité et lue sur une autre — est au-dessus du plancher aléatoire apparié **et** au-delà du témoin apparié, à une dose jugeable au sens de N-063 v2, sur l'organisme à consigne cachée avec son témoin bénin et sur un banc à poids constants ou à jumeaux tenus à l'écart. Une sonde de la marche 1 seule ne le tient pas. S'il n'est pas tenu à l'échéance, c'est le nœud que le brief prévoit, non un arrêt.

Pour G1, cette note n'écrit aucun critère. Elle fixe seulement l'instrument : le bras boîte blanche se nourrit d'une sonde passée par la marche 1 sur un contraste propre ; les fausses alertes se calibrent sur des épisodes honnêtes de la même tâche et des mêmes poids, ou du jumeau ; les bras « spécialisés » viennent de la marche 2, les bras « génériques » de la marche 3.

## 7. Embranchements, écrits avant le verdict

L'issue scellée du test sur les adaptateurs jumeaux est rangée dans l'une des trois classes ci-dessous par une table de correspondance écrite **avant le verdict** par une session habilitée à lire ses libellés, et jointe à cette note.

| classe du verdict | ce qui suit |
|---|---|
| **Au-delà de l'empreinte**, sur des paires jamais vues | La ligne supervisée tient pour cette recette d'adaptateurs. Suite : marche 2 vers une autre recette ou un autre mode, sous son propre texte. Candidate au critère 3 seulement à une dose jugeable. Aucune phrase « acte » avant une marche 1 à poids constants. |
| **Non établi** à cette puissance | Aucune phrase « sabotage ». Aucune paire de plus n'est formée avant une marche 1 à poids constants (banc par consigne). La sonde apprise sur honnêtes seuls passe devant. |
| **Contraire**, ou empreinte seule | Plus aucune ligne décisive supervisée sur un adaptateur. Toute la boîte blanche passe à poids constants. Les adaptateurs ne servent plus qu'à l'étude de l'empreinte. |

Croisé avec les diagnostics préalables :

| issue | ce qui suit, dans les trois classes |
|---|---|
| Identité « forte » ou « intermédiaire » | aucune aire entre poids non appariés ne se cite comme une détection ; toute ligne de ce genre porte son témoin apparié ou l'étalon de transport |
| Identité « faible » | audit de symétrie ; la règle ci-dessus tient jusqu'à son issue |
| Transport « fort » | la direction peut être essayée sans jumeau sur une autre recette, sous son propre texte |
| Transport « faible », « non établi » ou « contraire » | aucun usage sans jumeau ; les lectures entre poids restent des lectures de banc |
| Rejeu croisé : interaction « établie » | relecture par un même chemin de calcul demandée sur devis avant toute phrase |
| Rejeu croisé : « non établie » ou « contraire » | rien de plus sur l'adaptateur unique |

Et avec la marche 0 : si la chaîne ne retrouve pas le résultat publié, les sondes génériques sortent du programme à cette taille et le nœud « contrôle d'échelle » est porté à Lazar ; les marches 1 à 3 continuent, leur chaîne étant éprouvée à part par la vérité plantée.

Dans tous les cas : les gardes du § 5 ne changent pas ; les génériques restent hors de la ligne décisive ; le banc par consigne s'ouvre pour décembre ; le banc à sabotage conditionnel attend son calcul de puissance et son devis.

## 8. Ordre de travail

1. Code des quatre briques (magasin, formes closes, lectures, vérité plantée) : lancé.
2. Texte des diagnostics préalables : scellé avant le verdict ; lecture au processeur après.
3. Devis de la marche 0 ; aucune dépense avant son accord.
4. Texte et course de la marche 1 sur le banc par consigne : sur devis.
5. Calcul de puissance scellé et devis du banc à sabotage conditionnel.
6. Sonde apprise sur honnêtes seuls : exploratoire, au processeur, sur données gardées, sous texte contre-lu.

## 9. Limites

Une seule taille de modèle, une seule couche décisive, un mode de sabotage chiffré à ce jour. Un succès de la marche 1 ne dit ni « intention », ni tenue devant un modèle entraîné contre la sonde, ni transport à un autre modèle. Les sondes sont un accélérateur et un aiguillage de l'audit, non une garantie (N-075 v3, § 2) : ce qu'on leur demande est ce qu'elles capturent parmi les manqués de la boîte noire, à fausses alertes égales.
