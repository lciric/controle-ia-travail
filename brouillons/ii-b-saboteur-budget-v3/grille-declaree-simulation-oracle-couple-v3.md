EXPLORATOIRE, NON OPPOSABLE (R-522)

# Complément de grille, déclaré avant le passage v3 de la simulation de l'oracle couplé

Écrit le 2026-11-19T11:51:32Z, après la lecture de la sortie v2 et avant tout passage du script v3 (`simulation-oracle-couple-ii-b-v3.py`, empreinte : 11abc0f0ca7d82ae4f6ec160d28617d1dd23c52fc4352b87763f48c94ae8835b), jamais passé avant cette écriture.

**Ce que la sortie v2 a montré.** Par la règle écrite d'avance, le bloc retenu est celui de 8 rangs : **aucun couplage**. Le couplage réduit le bruit de l'excès honnête, mais il réduit l'excès mesuré du saboteur dans la même proportion ; le critère (signal sur bruit) ne gagne que 4 % au mieux parmi les blocs admis, moins que la marge de 5 % que la règle demande pour accepter une fuite. Je ne change pas la règle après avoir vu son résultat.

**Pourquoi un passage de plus.** Lazar a demandé un oracle couplé. La règle dit que le couplage ne gagne rien. Ce n'est pas à moi de trancher : je rends le nœud, et pour l'instruire il faut les blocs B, C et D aussi pour le meilleur bloc couplé admis. Le script v3 joue donc ces blocs deux fois : pour le bloc retenu par la règle, puis pour le bloc couplé admis de plus grand critère. Rien d'autre ne change : même définition du couplage que la v2, mêmes cellules, saboteurs, candidats, règles de choix, branches, effectifs, niveaux. Entropie neuve ; tous les choix sont refaits par les mêmes règles sur ce passage, qui fait foi pour les chiffres du texte. Si ses choix diffèrent de ceux du passage v2 (les critères des blocs sont proches), je le dis dans le texte.
