EXPLORATOIRE, NON OPPOSABLE (R-522)

# Complément de grille, déclaré avant le passage v4 de la simulation de l'oracle couplé

Écrit le 2026-11-19T11:56:57Z, après la lecture de la sortie v3 et avant tout passage du script v4 (`simulation-oracle-couple-ii-b-v4.py`, empreinte : b5893fc050c2a0976207e9823df6f6564091a66491bbf82f6aafa27640d93f94), jamais passé avant cette écriture.

**Un défaut de programme trouvé à la lecture de la sortie v3.** Pour le bloc de 8, les blocs C et D appelaient la chaîne avec la liste de blocs (8, 8) : le contexte réécrit était mis à jour deux fois par pas. Signe visible : l'épreuve du centrage y arrêtait un oracle sain 100 % des fois à faible dispersion. **Les chiffres des blocs C et D du bloc de 8 sont faux dans les sorties v2 et v3** ; je ne m'en sers pas. Les blocs A et B (liste sans doublon) et les blocs C et D du bloc de 2 ne sont pas touchés.

**Deux corrections, aucune autre.** (1) La liste des blocs est dédoublonnée. (2) Les blocs B, C et D sont joués pour le bloc de 8 et pour le meilleur bloc couplé admis, quel que soit celui que la règle retient : dans les passages v2 et v3, la règle retient le bloc de 8 de très peu (son critère est à 4,0 % puis 4,5 % sous le meilleur admis, pour une marge de 5 %), et un troisième tirage peut basculer. Mêmes cellules, saboteurs, candidats, règles, branches, effectifs, niveaux. Entropie neuve. Ce passage fait foi pour les chiffres du texte ; les choix des trois passages sont rapportés côte à côte.
