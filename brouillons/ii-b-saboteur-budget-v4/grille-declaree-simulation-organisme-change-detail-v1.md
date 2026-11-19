EXPLORATOIRE, NON OPPOSABLE (R-522)

# Complément descriptif, déclaré avant son passage — il ne décide rien

Écrit le 2026-11-19T12:56:47Z, après la lecture de la sortie du passage qui fait foi (`sortie-simulation-organisme-change-ii-b-v1.txt`) et avant tout passage de `simulation-organisme-change-detail-ii-b-v1.py` (empreinte : 6f4389c87b0b69e977dec4d7eb622b62dea3a6ee9ad3307155833a8a140bd412).

**La décision est acquise et n'est pas rejouée** : aucun des douze candidats ne couvre l'environnement, avec ou sans couplage. La meilleure couverture est de 0,585 (excès ×2, 10 actions, ancre commune au premier pas, couplage par moitié) puis 0,574 (excès ×1,5, mêmes autres choix), pour 0,90 exigé.

**Pourquoi ce complément.** Le passage principal n'imprimait le détail par cellule et l'étalonnage que pour l'organisme d'origine et pour l'organisme retenu. Aucun n'étant retenu, il manque, pour instruire les nœuds, de savoir **où** les deux meilleurs candidats se distinguent (quelles dispersions, quel ancrage) et ce que l'étalonnage y rendrait. Ce complément rejoue donc, sur une entropie neuve, les deux organismes à ancre commune de 10 actions (×1,5 et ×2), pour les deux oracles, avec les planchers que le passage principal a rendus (aucun choix refait), et imprime ce détail. Mêmes cellules, mêmes effectifs, mêmes définitions. Ses chiffres de couverture peuvent différer de ceux du passage principal dans la limite du bruit ; ils ne remplacent pas la décision.

**Ajout du 2026-11-19T12:57:06Z.** Le script v1 s'est arrêté avant tout calcul, sur une erreur de programme (ses deux fonctions n'étaient pas transmissibles aux processus fils) ; sa sortie ne porte que la ligne d'entropie et l'en-tête. La version 2 (`simulation-organisme-change-detail-ii-b-v2.py`, empreinte 70516563b579402a11d95825539f94e32a8e4de95e5e4f7e734dae1deb6bb6d9) n'ajoute que deux fonctions d'enveloppe. Rien d'autre ne change ; aucun résultat n'avait été vu.
