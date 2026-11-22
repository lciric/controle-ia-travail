# Un effet de forme dans une banque d'énoncés plantés : que faire du seuil ?

## Le cadre

On mesure si un agent à modèle de langue, muni d'un outil de calcul, repère mieux les énoncés mathématiques faux qu'une simple lecture par le même modèle. Pour avoir une vérité connue, on fabrique par programme de petits « mondes » arithmétiques finis (constantes, suites, fonctions définies par des formules), répartis en trois familles de mondes de natures différentes. Dans chaque monde, on plante des énoncés dont l'organisateur connaît la valeur de vérité :

- des **vrais** ;
- des **faux tôt** : un contre-exemple existe sous une borne N, et une énumération jusqu'à N le trouve ;
- des **pièges** : faux, mais seulement au-delà de N (par exemple une borne « pour tout t, E(t) < c » dépassée pour la première fois à un rang tiré entre N et 3N).

Les faux tôt et les pièges forment les deux strates d'énoncés faux.

Deux bras lisent les mêmes 150 énoncés (75 vrais ; 75 faux, dont 38 faux tôt et 37 pièges), sans connaître la proportion :

- **bras avec outil** : le modèle dispose d'un bac à sable Python et cherche des contre-exemples ; un modèle d'une autre famille relit son raisonnement avant le verdict ;
- **bras nu** : le même modèle, un seul appel, sans outil.

L'hypothèse mesurée : le bras avec outil déclare « faux » plus souvent que le bras nu sur les 75 faux (rappel). Le test est un score apparié sur les 75 faux, avec une marge minimale de 0,20 sur la différence de rappel fixée d'avance ; les fausses alarmes sur les 75 vrais doivent avoir une borne haute d'au plus 0,10. Tout contre-exemple avancé par le bras avec outil est vérifié en arithmétique exacte, ce qui distingue un « faux » appuyé par un contre-exemple vérifié d'un « faux » non appuyé. Le bras nu, sans outil, rend un verdict ; il peut citer une valeur, mais n'exécute aucun calcul.

## Le constat

Un énoncé faux pourrait se reconnaître en partie à sa forme (grands littéraux, grands modules premiers, fonctions propres à un gabarit), sans calcul. Si c'est le cas, une part du rappel des deux bras peut venir de la forme et non du calcul.

Pour le mesurer, on entraîne un classifieur de style sans calcul : bayésien naïf multinomial sur des unigrammes et bigrammes de jetons, chaque nombre étant remplacé par un même jeton « NUM ». Classe positive : les faux (faux tôt et pièges ensemble) ; classe négative : les vrais. Validation croisée en quatre plis, chaque pli regroupant des mondes entiers. L'aire sous la courbe ROC est calculée séparément pour chaque strate (faux tôt contre vrais, pièges contre vrais), sur les seuls textes non vus à l'apprentissage ; l'aire retenue est la plus grande des deux.

Un seuil de 0,75 sur cette aire avait été fixé avant la mesure ; il n'a pas été validé empiriquement. La règle associée : **si l'aire dépasse 0,75, l'hypothèse ne s'affirme plus que sur les contre-exemples vérifiés** (un « faux » ne compte que s'il est appuyé par un contre-exemple confirmé exactement).

Avant révision, sur deux graines d'essai, l'aire valait environ 0,96 à 0,97 (pièges contre vrais) et 0,89 à 0,90 (faux tôt contre vrais). Le générateur a ensuite été révisé pour réduire l'effet de forme : des vrais et des faux tôt de même forme que les pièges ont été ajoutés (bornes littérales vraies au-delà de 3N, seuils dépassés avant N, grands littéraux propres au monde). Après révision, sur 42 graines d'essai (mesure par programme, sans appel de modèle) : toutes les graines produisent leurs mondes sans retrait, et **l'aire retenue vaut de 0,939 à 0,982, au-dessus de 0,75 sur les 42**. Chaque aire repose sur une trentaine de vrais par graine ; son intervalle n'est pas calculé.

Non connus à ce jour : la part des 75 faux pour lesquels le bras avec outil produira un contre-exemple vérifiable (par construction, les pièges n'en ont qu'au-delà de N), et le rappel réel des deux bras.

## Les options

- **(a)** Garder le seuil de 0,75 et appliquer la règle : l'hypothèse ne s'affirme que sur les contre-exemples vérifiés.
- **(b)** Réviser encore le générateur (par exemple des pièges à borne « naturelle », 0, 1 ou une constante du monde, au lieu d'un grand littéral), puis remesurer.
- **(c)** Relever le seuil (valeur à choisir) et garder la même règle au-dessus.

D'autres options sont recevables.

Incertitudes, pour chacune : (a) réduit ce que la comparaison peut affirmer à un sous-ensemble des verdicts ; (b) n'a pas encore été essayée, sa faisabilité dans les trois familles et son effet sur l'aire sont inconnus ; (c) demande de justifier la nouvelle valeur.

## Ce qu'on vous demande

1. Laquelle recommandez-vous, ou quelle autre, et pourquoi ? Donnez votre niveau de confiance.
2. Le seuil de 0,75 vous paraît-il un bon instrument pour cette décision (choix de l'aire, de la valeur, de la règle « plus grande des deux strates », absence d'intervalle) ? Le conserveriez-vous tel quel, ou que mettriez-vous à la place ?
3. La règle (a) vous paraît-elle équitable entre les deux bras ? Pourquoi, et que reste-t-il de mesurable dans la comparaison sous cette règle ?
4. Quelle mesure ou quel contrôle supplémentaire, sans appel de modèle, ajouteriez-vous avant de trancher ?
5. Qu'est-ce qui, dans votre recommandation, serait faux si l'on se trompait sur un point du cadre ci-dessus ?

Répondez en français, de façon argumentée et concrète.
