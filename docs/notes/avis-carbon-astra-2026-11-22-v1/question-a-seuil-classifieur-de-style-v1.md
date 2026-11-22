# Une fuite de forme dans une banque d'énoncés plantés : que faire du seuil ?

## Le cadre

On mesure si un agent à modèle de langue, muni d'un outil de calcul, repère mieux les énoncés mathématiques faux qu'une simple lecture par le même modèle. Pour avoir une vérité connue, on fabrique par programme de petits « mondes » arithmétiques finis (constantes, suites, fonctions définies par des formules), et dans chacun on plante des énoncés dont l'organisateur connaît la valeur de vérité :

- des **vrais** ;
- des **faux tôt** : un contre-exemple existe sous une borne N, et une énumération jusqu'à N le trouve ;
- des **pièges** : faux, mais seulement au-delà de N (par exemple une borne « pour tout t, E(t) < c » dépassée pour la première fois à un rang tiré entre N et 3N).

Deux bras lisent les mêmes 150 énoncés (75 vrais, 75 faux), sans savoir la proportion :

- **bras avec outil** : le modèle dispose d'un bac à sable Python, cherche des contre-exemples, et une autre famille de modèles relit ;
- **bras nu** : le même modèle, un seul appel, sans outil.

L'hypothèse mesurée : le bras avec outil déclare « faux » plus souvent que le bras nu sur les 75 faux (rappel), à fausses alarmes bornées sur les 75 vrais. Le test est un score apparié sur les 75 faux, avec une marge minimale fixée d'avance. Tout contre-exemple que le bras avec outil avance est vérifié en arithmétique exacte, ce qui permet de distinguer un « faux » appuyé par un contre-exemple vérifié d'un « faux » non appuyé.

## Le problème

Un énoncé faux pourrait se reconnaître à sa seule forme (grands littéraux, grands modules premiers, fonctions propres à un gabarit), sans aucun calcul. Si c'est le cas, les deux bras peuvent gagner du rappel par la forme et la comparaison ne dit plus ce qu'on veut.

Pour le mesurer, on entraîne un classifieur de style sans calcul : bayésien naïf multinomial sur des unigrammes et bigrammes de jetons (nombres remplacés par un jeton unique), en quatre plis par mondes entiers, et on calcule l'aire sous la courbe ROC « faux contre vrais », strate par strate, sur les seuls textes non vus à l'apprentissage. L'aire retenue est la plus grande des deux strates.

Une règle avait été posée avant la dernière mesure, présentée par son auteur comme une convention à valider : **si cette aire dépasse 0,75, l'hypothèse ne s'affirme plus que sur les contre-exemples vérifiés** (un « faux » ne compte que s'il est appuyé par un contre-exemple confirmé exactement).

Le générateur a été révisé pour réduire la fuite : des vrais et des faux tôt de même forme que les pièges ont été ajoutés (bornes littérales vraies au-delà de 3N, seuils dépassés avant N, grands littéraux propres au monde). Après cette révision, sur 42 racines d'essai (mesure par programme, sans appel de modèle) : toutes les racines produisent leurs mondes sans retrait, mais **l'aire vaut de 0,939 à 0,982, au-dessus de 0,75 sur les 42**. Chaque aire repose sur une trentaine de vrais par racine ; son intervalle n'est pas calculé.

## Les options sur la table

- **(a)** Garder le seuil de 0,75 et appliquer la règle : l'hypothèse ne s'affirme que sur les contre-exemples vérifiés.
- **(b)** Réviser encore le générateur (par exemple des pièges à borne « naturelle », 0, 1 ou une constante du monde, au lieu d'un grand littéral), puis remesurer. On ne sait pas si c'est faisable dans les trois familles de mondes.
- **(c)** Relever le seuil.

D'autres options sont recevables.

## Ce qu'on vous demande

1. Laquelle recommandez-vous, ou quelle autre, et pourquoi ? Donnez votre niveau de confiance.
2. Le seuil de 0,75 vous paraît-il un bon instrument pour cette décision (choix de l'aire, de la valeur, de la règle « plus grande des deux strates », absence d'intervalle) ? Que mettriez-vous à la place, le cas échéant ?
3. La règle (a) traite-t-elle les deux bras de façon équitable, sachant que seul le bras avec outil peut produire des contre-exemples vérifiés ? Que reste-t-il de mesurable dans la comparaison sous cette règle ?
4. Quelle mesure ou quel contrôle supplémentaire, sans appel de modèle, ajouteriez-vous avant de trancher ?
5. Qu'est-ce qui, dans votre recommandation, serait faux si l'on se trompait sur un point du cadre ci-dessus ?

Répondez en français, de façon argumentée et concrète.
