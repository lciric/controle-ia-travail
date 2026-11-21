EXPLORATOIRE, NON OPPOSABLE (R-522)

# Complément de grille, déclaré avant le passage de la simulation v2 de la chaîne complète de l'oracle révisé

Écrit le 2026-11-19T10:58:44Z par le rédacteur neuf, **après** la lecture des blocs A à D de la sortie v1
(`sortie-simulation-chaine-oracle-revise-ii-b-v1.txt`, données synthétiques seulement) et **avant** tout passage du script v2
(`simulation-chaine-oracle-revise-ii-b-v2.py`, empreinte : 696b40b485358e1b1ed5b13eecdf34baaff75d181953814146e14d75c0174156). Le script v2 n'a été passé à aucun effectif, même réduit, avant cette écriture.

Ce que la sortie v1 a montré et qui motive ce complément (aucune valeur d'une course) :
1. Hors du profil à couplage par le préfixe, les deux statistiques de chaîne tiennent le niveau avec l'oracle « hors_K » ; la règle
   de choix écrite d'avance retient donc la plus puissante contre le biais de réécriture : la différence des estimations entre
   contexte d'origine et contexte réécrit (TB2).
2. Dans le profil à couplage par le préfixe, l'échangeabilité de la chaîne n'est qu'approchée, et la statistique de chaîne nue arrête
   un oracle au code sain, surtout à faible dispersion, pour des dérives de quelques centièmes de décade. D'où la **clause de
   matérialité**, fixée ici a priori : la composante de chaîne n'arrête que si les rangs signés rejettent **et** si le décalage estimé
   (Hodges-Lehmann) dépasse en valeur absolue M = 0,25 · F / T = 0,025 décade par action. M est dimensionné sur la règle (un quart de
   ce qu'il faut en moyenne par action pour atteindre F en T actions ; la moitié de la tolérance de l'épreuve v1) ; il n'est ajusté
   sur aucune sortie : une seule valeur est jouée.
3. La réécriture par un tirage en plus a un coût en calcul ; un candidat sans surcoût (« parmi_K_libre » : une des K suites prise au
   hasard par graine, lisible ou non) est ajouté pour instruire le nœud du surcoût.

Grille du passage v2 : bloc A, les 336 cellules de la v1, trois oracles (« hors_K », « parmi_K_libre », « v1 » en défaut D3) ; bloc B,
les 56 configurations de la v1 pour les défauts D1, D4 et D5 (D2 et D6 relèvent des composantes nues du contexte d'origine, inchangées :
leur puissance est celle de la sortie v1) ; bloc C, 64, 128 et 256 épisodes, D1 et D4 à 0,25 et 0,5 fois F / T ; bloc D, les 160
cellules de la v1, trois oracles. Niveau : 1/60 par composante. Mêmes effectifs. Entropie neuve, tirée une fois.

Règle de choix écrite d'avance : « hors_K » reste retenu sauf s'il ne tient pas le niveau ; « parmi_K_libre » n'est proposé comme
option du nœud du surcoût que s'il tient le niveau (batterie au plus 0,08 dans toute cellule hors couplage, soit le niveau nominal 0,05
plus la marge d'échantillonnage du maximum de 280 cellules à 1 000 répétitions).
