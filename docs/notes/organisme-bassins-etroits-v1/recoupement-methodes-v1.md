# Recoupement des méthodes suggérées pour atteindre les bassins d'idées étroits et profonds — état après un tour de critique croisée (v1)

## Nature de cette pièce

Compte rendu neutre, écrit le 13 novembre 2026 par un lecteur qui n'a rédigé aucune des propositions. Il recense les méthodes
mathématiques suggérées en réponse à une même question : comment amener un organisme d'idéation à trouver des bassins d'idées
étroits et profonds plutôt qu'à raffiner des bassins larges, à coût égal, sans affaiblir la garde contre les fausses
découvertes et les copies. Les suggestions viennent de deux sources : un tour à cinq participants en trois temps
(conception, critique croisée, réponse aux critiques) et trois avis rendus à part, en une seule fois, sans critique.

**Rien de ce qui suit n'est un résultat.** Aucune méthode n'a été éprouvée. Les « sorts » décrivent l'issue d'une discussion
écrite, pas une mesure. Les chiffres avancés par les propositions étaient illustratifs ; ils sont omis. L'ordre de
présentation suit le lieu d'action de chaque méthode ; il n'exprime aucune préférence.

## Vocabulaire

- **Organisme** : des proposeurs (modèles de langue) rendent des cartes, c'est-à-dire des lois prédictives écrites dans une
  grammaire publique ; un gardien mécanique les contrôle ; un juge statistique, calculé hors de tout agent, les éprouve sur
  des tirages frais ; les cartes retenues entrent dans l'archive de la génération suivante.
- **Vue** : ce qu'un proposeur reçoit (description publique, grammaire, lois de l'archive), sans verdict ni issue.
- **Nul** : la classe des lois déjà connues (archive, lois aveugles, certaines recombinaisons) contre laquelle le juge teste.
  Il tient dans cette classe et cède hors d'elle, notamment devant les recombinaisons par morceaux.
- **Valeur e** : statistique de test d'espérance au plus 1 sous le nul ; les comparaisons multiples sont contrôlées par la
  règle de Benjamini et Hochberg appliquée aux valeurs e.
- **Jeu public** : instances publiques sans issue, qui servent à comparer les cartes entre elles (regroupement des doublons).
- **Bassin étroit** : peu de propositions spontanées y tombent, ou l'idée est invisible en moyenne dans les données.
  **Bassin profond** : le gain est grand une fois l'idée trouvée et complétée.
- **Sorts** : *non critiquée* (personne n'y a répondu) ; *retirée* (critiquée, puis retirée ou sortie des méthodes actives
  par la proposition qui la portait) ; *maintenue* (critiquée, gardée avec la correction dite) ; *survivante* (encore
  défendue au dernier temps du tour, sans objection décisive restée sans réponse) ; *suspendue* (gardée candidate, mais
  différée ou privée d'expérience par la proposition qui la porte).

## 1. Le cadre sur lequel les propositions s'accordent

- **Trois leviers, pas davantage.** La probabilité qu'un bassin reçoive au moins une proposition en k appels vaut
  1 − (1 − p)^k, où p est la probabilité de proposition par appel sous la vue servie. Rien en aval des proposeurs
  (regroupement, juge, sélection) n'augmente cette probabilité ; l'aval peut seulement éviter de perdre une idée déjà
  proposée. Agir revient donc à changer la vue, changer les proposeurs, ou ne pas perdre.
- **Deux étroitesses distinctes.** Une idée peut être rare sous la loi des propositions et pourtant évidente dans les
  données ; une interaction peut être invisible en moyenne et pourtant facile à écrire. La première relève de la vue, la
  seconde du juge et de la distance de regroupement.
- **La largeur d'un bassin sous la loi des modèles ne se règle pas dans le monde** : elle dépend du modèle, de la vue et de
  l'archive, et ne peut qu'être estimée sur des mondes d'étalonnage.
- **La remise à zéro du contexte est déjà en place** : chaque appel se fait en session neuve sans historique.
- **Toute poussée vers les idées conditionnelles pousse vers la classe que le nul ne couvre pas.** La garde est à qualifier
  avant de comparer des méthodes entre elles.
- **Aucune proposition ne sert un score de nouveauté à un agent.**

## 2. Méthodes qui agissent sur la vue servie aux proposeurs

**V1 — Décomposition orthogonale de l'archive, avec la table de ses termes nuls.** Objet : le logit de chaque loi d'archive
est décomposé en effets principaux et interactions par inversion de Möbius sur le treillis des sous-ensembles de traits ;
la décomposition est unique sous une mesure produit. L'archive est servie sous cette forme, les cases d'interaction vides
étant listées. *Sort : retirée.* Motif : dès que les traits sont dépendants, les termes ne sont ni uniques ni orthogonaux,
et des cases annoncées vides peuvent être fausses ; une table fausse détournerait un proposeur d'un bassin réel. Elle se
réduit à V2.

**V2 — Liste des paires de traits que l'archive ne croise pas.** Objet : une paire (i, j) est « non croisée » dans une loi
si la différence mixte de son logit en i et j est identiquement nulle ; c'est une propriété de la fonction, indépendante de
toute mesure. L'archive entière est servie, avec cette table binaire. Quatre suggestions de départ s'y ramènent après
critique : la décomposition V1, un graphe de dépendance entre traits calculé sous les lois de l'archive, une table des
produits de traits absents, et les cavités d'un complexe simplicial des traits en interaction. *Sort : survivante*, sous
cette forme minimale ; elle sert aussi de témoin que toute méthode de vue plus riche devrait dépasser. Objections restées
ouvertes :
- aucun fait n'établit que la loi des propositions d'un modèle change quand on lui montre cette liste ;
- un effet éventuel peut venir de la forme (une table qui appelle à écrire des interactions) et non de l'information ;
- à budget total de jetons égal, des appels supplémentaires sous la vue ordinaire peuvent valoir autant ;
- elle a été pensée pour des mondes dont la structure est celle qu'elle affiche (interaction de deux traits dont l'un est
  déjà archivé) ; devant une interaction de trois traits, un seuil décentré ou un effet non monotone, elle est muette et
  peut détourner l'attention ;
- le nombre de paires croît comme le carré du nombre de traits ; un proposeur peut les remplir mécaniquement ;
- la liste décrit l'archive, non le monde : une paire non croisée n'est pas un indice de présence d'un effet.

**V3 — Plan combinatoire qui répartit des focalisations entre les appels ou entre les cartes d'un appel.** Objet : tableau
couvrant ou orthogonal de force t, plan en blocs, plan factoriel fractionnaire ; chaque combinaison de t facteurs (paires
de traits, questions publiques, blocs de traits) est mise devant au moins un appel. Variantes de contenu : résumés
descriptifs du jeu public par strates définies par les traits de l'archive ; dictionnaire de questions publiques ; une
paire de traits à examiner par emplacement de carte ; blocs de traits pour des interactions clairsemées. Garanties
dites : la couverture porte sur les affectations, pas sur les idées produites ; sous indépendance des réponses, un plan
équilibré ne fait pas moins bien que des blocs tirés indépendamment. *Sort : survivante*, avec corrections : le plan doit
être exhibé et vérifié par programme (le plan d'une proposition s'est révélé inexistant, et sa correction également, voir
la borne 11) ; liste et catalogue fixés avant que le monde soit tiré. Objections restées ouvertes :
- rien ne montre qu'un plan fait mieux que la simple liste V2 servie entière à tous, ni mieux que les mêmes focalisations
  tirées sans remise ;
- rien ne garantit que le proposeur travaille la focalisation reçue ;
- un résumé descriptif de traits sans issue ne rend visible aucun effet sur les issues ;
- sous traits dépendants, certaines configurations du plan sont presque vides ;
- un dictionnaire de questions fixe peut enfermer la recherche ; le nombre de facteurs pertinents est inconnu.

**V4 — Code couvrant sur les sous-ensembles de traits.** Objet : ensemble de sous-ensembles tel que tout sous-ensemble de
traits soit à faible distance de Hamming de l'un d'eux. *Sort : retirée* comme méthode active. Motifs : une idée est une
fonction des traits, non un sous-ensemble ; une borne inférieure sur la taille d'un code ne prouve pas qu'il existe ; deux
sous-ensembles proches peuvent porter des lois opposées.

**V5 — Dictionnaire de directions par moments orthogonaux.** Objet : petites déformations exponentielles d'une loi archivée
par une statistique orthogonale à ses scores ; au second ordre, l'écart en divergence de Kullback-Leibler vaut la moitié du
carré du paramètre fois l'espérance de la variance conditionnelle de la statistique. Les directions, traduites en questions
publiques, fournissent le contenu de V3. *Sort : maintenue*, corrections : variance conditionnelle et non globale ;
orthogonalité revendiquée seulement quand la loi admet une extension paramétrique lisse ; traduction de la direction en
question par une règle déterministe fixée d'avance ; comparaison à un dictionnaire naïf. Objections restées ouvertes :
- la direction donnée en exemple a la forme même de la composante conditionnelle décrite dans les faits : un gain peut
  n'être que la coïncidence de deux constructions ;
- l'orthogonalité est locale et calculée sous les lois de l'archive, non sous celle du monde ;
- une direction qui ne dépend que des traits ne déforme aucune loi ;
- que la question traduite aide un modèle reste une hypothèse.

**V6 — Tirage déterminantal d'un lot de vues.** Objet : processus ponctuel déterminantal sur un catalogue fini de vues ou de
plans publics ; les lots de vues mutuellement dissemblables sont favorisés. Un avis à part en donne une garantie
démontrée : avec un noyau de projection, et sous indépendance et stabilité des réponses, la probabilité de n'obtenir
aucun succès est au plus celle d'un tirage indépendant de mêmes marges. *Sort : maintenue*, corrections : catalogue et
noyau fixés avant que le monde soit tiré ; comparaison à un tirage uniforme sans remise dans le même catalogue et à des
paraphrases neutres. Objections restées ouvertes : la dissemblance est garantie entre descriptions de vues, pas entre les
cartes produites ; si la loi des cartes ne dépend pas de la vue, l'effet est nul ; l'inégalité peut être presque une
égalité.

**V7 — Plan sur des vues équivalentes.** Objet : un groupe fini de transformations publiques inversibles (renommage des
traits, inversion d'un codage) ; chaque vue contient toute l'archive transformée sans perte, chaque sortie subit la
transformation inverse. *Sort : suspendue* à un essai préalable. Objections restées ouvertes : si le modèle est
équivariant, le gain est nul ; une transformation peut au contraire dégrader le raisonnement du modèle ; couvrir des
facteurs de présentation n'est pas couvrir des idées.

**V8 — Acquisition par variance d'un processus gaussien sur l'espace des lois.** Objet : processus gaussien sur une fonction
de gain, avec un noyau entre lois ; suggestion des régions de plus grande incertitude. *Sort : retirée.* Motif : soit le
gain modélisé emploie un verdict, qui ne peut pas être servi ; soit il se réduit à une distance publique, et chercher la
variance maximale revient à récompenser l'éloignement de l'archive.

**V9 — Homologie de l'archive.** Objet, deux variantes : homologie persistante d'un complexe bâti sur les lois archivées et
leurs distances ; cavités d'un complexe simplicial dont les sommets sont les traits et les faces les interactions
archivées. *Sort : retirée* dans ses deux variantes. Motifs : avec peu de lois, aucune classe n'est discernable du bruit ;
avec peu de traits, la construction se ramène à la liste V2 ; une distance globale dilue une différence rare avant tout
calcul topologique.

**V10 — Focalisations tirées des résidus d'une loi de référence.** Objet : résidus des issues par rapport à une loi
publique, projetés sur une base orthonormale de contrastes ; les contrastes à coefficient notable deviennent des
focalisations, servies sans le coefficient. *Sort : non critiquée.* Elle suppose des données publiques d'exploration avec
issues, distinctes des tirages du juge, dont l'existence n'est pas établie. Limites dites par la proposition elle-même :
un résidu peut être du bruit ou un artefact de la loi de référence ; le nombre de contrastes croît vite avec l'ordre ;
rien ne garantit qu'un proposeur en tire parti.

**V11 — Balayage à plusieurs échelles des résidus.** Objet : statistique de balayage standardisée sur un arbre public de
régions ; un effet confiné à une région de masse r y ressort d'un facteur de l'ordre de l'inverse de la racine de r par
rapport à la moyenne globale. *Sort : non critiquée* ; même prérequis que V10. Limites dites : sans assez d'observations
dans la région, rien n'est localisable ; le maximum sur beaucoup de régions retient aussi du bruit ; la focalisation
encourage des lois par morceaux.

**V12 — Méthodes à signal servi (rappel).** Recuit, tempérage, curiosité, bandit sur les vues pendant la course, comité
d'archive, échantillonnage parapluie, recherche de nouveauté : évoquées pour être écartées par celles mêmes des
propositions qui les nomment, parce qu'elles supposent un score ou un verdict rendu à l'agent ou un pilotage par le juge.

## 3. Méthodes qui changent la représentation dans laquelle le proposeur écrit

**I1 — Contrastes orthogonaux compilables.** Objet : une bibliothèque publique de produits de traits codés ±1, orthogonaux
sous mesure produit équilibrée ; le proposeur peut écrire une carte dans ces coordonnées, un compilateur mécanique la
traduit dans la grammaire ; la grammaire d'origine reste ouverte. *Sort : survivante*, corrections : comparaison à un
bras disposant du même compilateur sans la bibliothèque ; copies compilées présentées à la garde ; même borne sur le
nombre de tests dans tous les bras ; mondes non alignés sur la bibliothèque. Objections restées ouvertes :
- une carte compilée est une carte conditionnelle, dans la classe où le nul cède ; un contraste appliqué à une pente
  archivée peut n'être qu'une copie réécrite ;
- la primitive offerte a la forme de la composante décrite dans les faits : avantage possible par construction ;
- une part du gain peut n'être qu'une aide de syntaxe ;
- sur traits continus ou avec un seuil décentré, la bibliothèque est moins puissante qu'une carte libre ;
- si un énumérateur mécanique fait aussi bien que le modèle, l'intérêt est celui du compilateur.

**I2 — Opérateur d'expansion.** Objet : l'orchestrateur complète lui-même une carte additive par le terme croisé
correspondant. *Sort : retirée* ; la proposition qui la portait la signalait dès l'origine comme dangereuse, puisqu'elle
fabrique mécaniquement des cartes dans la classe que le nul ne couvre pas.

**I3 — Carte de déviation dans le groupe des log-cotes.** Objet : les lois conditionnelles strictement positives forment un
groupe abélien pour l'addition des log-cotes ; le proposeur ne rend qu'un écart à une loi de base tirée de l'archive, et
l'orchestrateur compose les deux. Une copie de l'archive devient un écart presque nul ; une idée conditionnelle n'oblige
plus à réécrire l'acquis. *Sort : non critiquée.* Preuve que la proposition dit devoir fournir : que le nul couvre
l'enveloppe log-linéaire de l'archive, faute de quoi un écart qui rejoue une loi connue produirait une composition hors
classe. Hypothèse non éprouvée : qu'un modèle raisonne bien en multiplicateurs de cotes.

## 4. Méthodes qui changent le dessin de la course (recherche en plusieurs pas)

**C1 — Synthèse typée de prolongements.** Objet : un graphe de programmes prédictifs typés ; chaque programme reçoit une
longueur de description préfixe ; une recherche à budgets croissants lui alloue du calcul après un surcoût de l'ordre de
deux puissance sa longueur. Un programme construit la liste des prolongements de l'archive ; les créneaux sont fixés
d'avance. *Sort : suspendue.* Objections reconnues par la proposition : la longueur de description est un a priori sur les
formes, non sur les idées ; elle dépend des primitives choisies par le concepteur ; la borne exponentielle ne donne aucun
avantage pratique à elle seule. Autres objections ouvertes : le grand nombre de candidats durcit le seuil du juge ; le
modèle risque de n'être plus qu'un remplisseur de gabarits.

**C2 — Arbres de continuation sans récompense intermédiaire.** Objet : quelques préfixes (une condition, une
décomposition, une esquisse de loi), chacun prolongé par plusieurs continuations ; tous les préfixes reçoivent le même
traitement, aucun n'est choisi sur une note. La comparaison au tirage indépendant est une inégalité entre taux d'échec par
unité de coût, qui penche d'un côté ou de l'autre selon la rareté des préfixes utiles. *Sort : non critiquée.* Limites
dites : aucune garantie uniforme ; un préfixe partagé peut ancrer toutes les branches dans la même erreur ; choisir les
préfixes sur un « potentiel » noté réintroduirait le signal exclu.

**C3 — Fractionnement à plusieurs niveaux sur un graphe public de prérequis.** Objet : un graphe orienté sans cycle des
éléments publics déjà archivés ; à chaque génération, les appels sont affectés à sa frontière dans un ordre fixe, jamais
selon les valeurs e ; la probabilité de compléter une chaîne est le produit des probabilités de franchir chaque niveau.
*Sort : non critiquée.* Limites dites : le graphe peut devenir trop large ou enfermer dans les raffinements d'un bassin
large ; une étape vraie mais non retenue ferme toute la descente ; il faut au moins autant de générations que de
prérequis.

## 5. Méthodes qui agissent sur le regroupement des doublons et le choix du représentant

**G1 — Jeu public construit par plan.** Objet : les instances publiques sont choisies pour que chaque configuration d'une
paire de signes ou de quantiles de traits apparaisse un nombre minimal de fois, afin qu'une différence confinée à une
région rare ne soit pas effacée dans la distance de regroupement. *Sort : survivante*, correction : la propriété est une
couverture de cellules ; elle ne rend pas les interactions « estimables ». Les strates sont écrites avant que le monde
soit tiré.

**G2 — Représentant par couverture dirigée de strates.** Objet : dans un groupe de doublons, retenir la carte qui s'écarte
de l'archive, au-delà d'un seuil, sur le plus grand nombre de strates publiques. *Sort : maintenue, affaiblie* : ramenée
à une règle de départage, avec un seuil par strate corrigé de la variance. Objections restées ouvertes : c'est un critère
numérique d'écart à l'archive dans une sélection ; rien ne relie les strates aux composantes du monde, de sorte que la
carte choisie peut être la plus bruyante ; dans les strates rares le critère sature ; il peut se surajuster au jeu public.

**G3 — Pivotage de Cholesky sur un noyau de Hellinger par strates.** Objet : chaque carte est représentée par le vecteur de
ses écarts de log-probabilité à l'archive sur le jeu public ; on choisit successivement la carte de plus grand résidu
orthogonal aux précédentes. Le choix est insensible à la multiplication des clones. *Sort : maintenue comme usage
résiduel* (regrouper et choisir le représentant, sans rien transmettre au juge), *suspendue* faute d'expérience ; le
tirage aléatoire déterminantal des représentants est abandonné. Objections restées ouvertes : une carte fausse mais
éloignée de tout est choisie tôt ; une carte utile presque colinéaire aux clones est perdue ; la méthode ne crée aucune
carte ; sa dernière forme n'a reçu aucune critique.

**G4 — Divergences localisées par strates.** Objet : le maximum, sur une famille fixée de strates publiques, de l'écart
d'une carte au nul. *Sort : maintenue comme instrument descriptif*, jamais comme critère de sélection. Limites établies :
le maximum sur beaucoup de strates est optimiste, d'autant plus que les strates sont petites ; si chaque strate choisit
sa propre loi du nul, on obtient un profil d'écarts locaux et non une distance à un nul commun (le maximum des infimums
est au plus l'infimum des maximums).

## 6. Méthodes qui agissent sur le juge statistique

**J1 — Processus de valeurs e à arrêt optionnel.** Objet : la valeur e à taille fixée est remplacée par une surmartingale
de test ; par l'inégalité de Ville, la probabilité qu'elle dépasse un jour l'inverse du niveau est au plus ce niveau,
pour toute règle d'arrêt écrite d'avance. Une carte dont l'effet est confiné à une région rare reçoit plus de tirages.
*Sort : survivante*, corrections : règle d'allocation écrite ; ordre de continuation fixé d'avance, jamais selon les
valeurs e ; dénominateur fait d'un mélange à poids fixés des lois du nul, jamais recalibré sur les issues ; comparaison à
espérance de tirages égale. Limites reconnues : elle améliore la survie d'une idée proposée, pas sa découverte ; elle ne
peut rien quand le produit de la masse de la région, de la profondeur et du budget de tirages reste sous le seuil de
détection ; sa validité sous un nul composite reste à démontrer pas à pas.

**J2 — Tirages du juge stratifiés selon une loi de traits choisie.** Objet : sur-échantillonner les régions rares, la loi
des traits disparaissant du rapport de vraisemblance. *Sort : retirée.* Motifs : la grandeur jugée change (une carte
meilleure dans la région sur-échantillonnée et pire ailleurs serait promue) ; si la partition est celle qui a servi à
construire le monde, il y a fuite ; si la région utile est répartie également entre les strates, le gain disparaît.

**J3 — Valeur e à plusieurs échelles.** Objet : un mélange convexe, à poids fixés d'avance, de valeurs e restreintes aux
cellules d'une hiérarchie de partitions des traits ; valide par linéarité si chaque valeur locale l'est. *Sort :
maintenue, très restreinte.* Une critique a établi que si la carte égale la loi du nul hors d'une région, sa valeur e
globale est déjà sa valeur e locale : localiser n'ajoute rien et coûte une pénalité logarithmique. Il ne reste que le cas
d'une carte utile dans une région et légèrement fausse ailleurs. Objections restées ouvertes : si le nul local contient
les recombinaisons restreintes à la cellule, il absorbe l'effet ; s'il ne les contient pas, la garde cède dans la
cellule ; la validité de chaque facteur local reste à démontrer.

**J4 — Martingale à pari localisé, avec nul ponctuel.** Objet : à chaque épisode, une fraction de mise fonction des seuls
traits, d'autant plus grande que la carte s'écarte localement du nul ; l'écart local est pris contre l'enveloppe convexe,
en chaque point, des lois d'archive. Une carte qui recolle deux lois connues par morceaux obtient alors une valeur e
bloquée à 1. *Sort : non critiquée.* Elle porte le même intitulé que J3 mais un objet différent. Deux bornes de la
section 8 la concernent sans qu'aucune réponse ait été écrite : l'auto-localisation (borne 6) et la fermeture du nul
(borne 7).

**J5 — Poids de multiplicité selon la géométrie des groupes.** Objet : dans la règle de Benjamini et Hochberg, donner plus
de poids aux groupes dont les prédictions sont orthogonales aux autres ou concentrées sur peu d'instances, les poids étant
fixés sur le jeu public avant les issues. *Sort : retirée dans le tour* ; un avis à part la porte encore, non critiqué,
en s'appuyant sur le fait que la garantie formelle tient. L'objection qui a emporté le retrait : pondérer le seuil ou
multiplier la valeur e par un bonus est la même opération ; c'est une priorité numérique donnée à la nouveauté, et le
budget d'erreur se concentre sur les cartes aberrantes mais orthogonales.

**J6 — Valeur e par supremum sur un nul composite explicite.** Objet : le rapport de la carte au supremum des lois du nul ;
valide pour le nul effectivement spécifié. Portée par quatre sources comme garde candidate, non comme moyen de découverte.
*Sort : maintenue sous double condition* : supremum calculé exactement sur une classe finie ou majoré de façon
démontrée ; puissance vérifiée sur une carte réellement additionnelle. Objections restées ouvertes : une grille qui
sous-estime le supremum rompt la validité ; la version par épisode et la version sur l'échantillon entier diffèrent
fortement ; un nul assez fermé absorbe les idées recherchées.

**J7 — Filtre mécanique avant le juge.** Objet : une carte conditionnelle n'est admise que si elle s'écarte, au-delà d'un
seuil, de toute recombinaison de l'archive par morceaux sur une partition publique. *Sort : non critiquée* ; apparue au
dernier temps du tour.

## 7. Méthodes qui agissent sur la composition des proposeurs

**P1 — Portefeuille de proposeurs sous budget.** Objet : choisir le nombre d'appels par famille de proposeurs pour maximiser
la probabilité de couvrir chaque composante, sous contrainte de coût ; la fonction est monotone et sous-modulaire, un
algorithme glouton en approche l'optimum ; les fréquences viennent de l'oracle d'un monde pilote, hors course. *Sort :
suspendue.* Objections : pour un bassin étroit, les fréquences ne se distinguent pas de zéro au budget d'un pilote ; rien
n'assure qu'elles se transportent à un monde de structure différente ; les échecs de deux appels ne sont pas
indépendants.

**P2 — Identification hors ligne du meilleur couple « proposeur × méthode de vue ».** Objet : sur des mondes de
calibration, estimer par l'oracle la fréquence de couverture de chaque couple, avec une borne de concentration uniforme
sur les couples. *Sort : non critiquée.* Limite dite : la garantie vaut pour la distribution des mondes de calibration,
pas pour des mondes futurs.

## 8. Bornes et impossibilités dites

1. **Borne amont.** 1 − (1 − p)^k ; aucun traitement en aval ne crée une carte qui n'a pas été proposée.
2. **Pas de vue uniformément meilleure.** La somme des probabilités de bassins disjoints est au plus 1 : élever l'une
   abaisse les autres. Sans information sur la classe de bassins que le monde contient, aucune méthode ne bat le tirage
   indépendant sur tous les mondes ; si le bon bassin est placé uniformément parmi des candidats indiscernables, le succès
   est borné par la fraction de candidats distincts examinés. Un gain suppose une structure nommable sans l'oracle.
3. **Barrière de parité.** Une composante qui fait interagir k traits et dont toutes les marges d'ordre inférieur sont
   nulles ne laisse aucun palier : sans issue ni résidu dans la vue, la trouver demande de l'ordre du nombre de
   sous-ensembles de k traits en propositions aveugles. Un gain en amont suppose une hiérarchie (un parent détectable,
   déjà archivé).
4. **Chaînes.** Le temps de découverte d'une chaîne est une somme de temps d'attente ; aucun maillon ne se trouve avant le
   précédent ; l'horizon en générations borne la profondeur atteignable.
5. **Détectabilité.** Pour un effet confiné à une région de masse r et de profondeur locale Δ, avec n tirages, une
   puissance 1 − β au niveau α exige que n·r·Δ atteigne la divergence binaire entre 1 − β et α ; avec m tests, l'ordre de
   grandeur est le logarithme de m/α. Aucune stratification, aucun pari localisé ne franchit ce seuil ; l'arrêt optionnel
   ne le déplace qu'en dépensant plus de tirages.
6. **Auto-localisation.** Si une carte est égale à la loi du nul hors d'une région, les rapports de vraisemblance y valent
   1 et la valeur e globale est la valeur e locale. La dilution ne touche que les cartes mal spécifiées hors de leur
   région, et les distances moyennes servant au regroupement.
7. **Fermeture du nul.** Une carte qui appartient au nul a une valeur e au plus égale à 1 ; un nul assez large pour
   contenir toutes les copies peut contenir aussi les découvertes.
8. **Aucune certification empirique absolue.** Aucun nombre de contrôles ne prouve la validité contre toutes les lois hors
   du nul spécifié ; une simulation contrôle un programme, pas une preuve. La validité statistique sous le nul et l'absence
   de fausse découverte au sens de l'oracle sont deux propriétés distinctes.
9. **Copies par morceaux.** Un nul fait de mélanges à poids constants ne couvre pas le recollage de deux lois connues sur
   une partition des traits.
10. **Poids selon la nouveauté.** Pondérer le seuil de multiplicité par un indice de nouveauté équivaut à multiplier la
    valeur e par cet indice.
11. **Tableaux couvrants binaires de force 2.** Avec N appels, on ne peut couvrir toutes les paires que pour un nombre
    borné de facteurs. La formule citée pendant le tour était fausse pour N impair ; une vérification par calcul
    exhaustif, faite après le tour, donne 3 facteurs pour 4 appels, 4 pour 5, 10 pour 6, 15 pour 7.
12. **Sans observation, pas de localisation.** Si aucune donnée ne tombe dans une région, aucun calcul sur ces données ne
    distingue deux mondes qui ne diffèrent que là.
13. **Identité des idées.** Deux cartes proches en prédiction peuvent venir d'idées différentes, et deux étapes d'une même
    idée être éloignées ; la correspondance entre groupe de doublons et idée de fond n'est pas établie. L'équivalence
    fonctionnelle n'est décidable que dans une grammaire bornée.
14. **Orthogonalité.** Les décompositions en contrastes ne sont orthogonales que sous mesure produit ; l'orthogonalité de
    deux contrastes n'implique pas une distance maximale entre les lois correspondantes.

## 9. Objections transversales restées ouvertes

- **La réponse des proposeurs à la vue est inconnue.** Toutes les méthodes des sections 2 à 4 supposent qu'une information
  combinatoire sur l'archive déplace la loi des propositions ; aucun fait ne le montre.
- **Instrument et monde trop assortis.** La plupart des méthodes de vue et de représentation ont la forme de la composante
  conditionnelle décrite dans les faits ; un succès sur un tel monde ne dit rien d'un bassin étroit d'une autre forme.
- **La garde.** Aucune des gardes candidates (J6, J7, le nul ponctuel de J4, l'extension bornée du nul aux recombinaisons
  par morceaux) n'a à la fois une preuve de validité pour la classe visée et une puissance vérifiée. Le contrôle des
  erreurs d'une génération à l'autre n'est écrit nulle part.
- **Découvrir ou survivre.** Les méthodes de juge et de regroupement n'agissent que sur des cartes déjà proposées ; on ne
  sait pas, dans les courses passées, si des idées étroites ont manqué d'être proposées ou ont été proposées puis perdues.
- **La profondeur en chaîne.** Les discussions du tour portent presque toutes sur une seule génération au-dessus d'une
  archive fixée ; seules deux méthodes non critiquées (C2, C3) visent des idées qui demandent plusieurs pas.
- **Ce que vaut la sophistication.** Plusieurs objets mathématiques riches se sont ramenés, après critique, à une liste ou
  à une énumération ; la question de savoir si un objet plus riche fait mieux que cette liste est restée sans réponse.
- **Désaccords non résolus** : faut-il lire l'effet d'une vue sur les propositions brutes ou sur les cartes retenues ; une
  hausse des cartes conditionnelles dans un monde sans effet est-elle une alerte de garde ou une simple description ; un
  monde où l'interaction existe sans parent détectable est-il un contrôle nul ou un cas à part.

## 10. Contrôles que la critique a fait apparaître

- **Vue placebo** : même format, même longueur, archive vraie intacte, table tirée au hasard ; permuter les coefficients
  d'une table fausse l'information au lieu d'en neutraliser la présentation.
- **Coût** : comparaison à budget total de jetons égal, cartes refusées par le gardien comptées ; même borne sur le nombre
  de tests dans tous les bras, pour qu'un bras qui achète plus d'appels ne soit pas jugé plus sévèrement.
- **Unité d'analyse** : le monde, bras appariés par monde ; les cartes d'un même appel ne sont pas indépendantes.
- **Trois lectures** par l'oracle : propositions brutes, représentants, cartes retenues.
- **Deux bancs distincts** : mondes entièrement dans le nul (fausses promotions) ; copies hors de la classe du nul
  (défaillance de la garde contre les copies).
- **Contrôle positif** : une garde qui ne promeut jamais passe tous les contrôles nuls ; une carte réellement
  additionnelle, réservée au banc, doit rester détectable.
- **Mondes hors structure** : interaction de trois traits, seuil décentré, effet non monotone, traits dépendants sans
  interaction.
- **Comparaisons minimales** : énumération simple ; tirage sans remise des mêmes focalisations ; énumérateur mécanique
  sans modèle ; permutation commune des noms de traits pour donner au plan et à son témoin les mêmes lois marginales.
- **Mesure d'exécution** : la carte rendue cite-t-elle la paire ou la condition qui lui était assignée.
- **Ordre des constructions** : listes, partitions, catalogues et noyaux fixés avant que le monde soit tiré ; classement
  « étroit » porté par une famille de mondes, jamais par les mondes où le témoin a échoué ; taille des tirages du juge
  fixée d'avance.

## 11. Limites de ce recoupement

- Les sources ne sont pas indépendantes : plusieurs avis viennent de participants du tour ; une méthode portée par
  plusieurs sources ne compte pas autant de voix.
- Les réponses du dernier temps du tour et les avis rendus à part n'ont pas eu de contradicteur.
- Les garanties annoncées sont des énoncés sous hypothèses, souvent cités de mémoire par leurs auteurs ; une seule a été
  revérifiée par calcul (borne 11).
- Les faits de départ ne précisent pas ce que la vue contient de données ; plusieurs méthodes butent sur ce point.
- La question posée désignait la composante conditionnelle ; les suggestions s'en ressentent.
