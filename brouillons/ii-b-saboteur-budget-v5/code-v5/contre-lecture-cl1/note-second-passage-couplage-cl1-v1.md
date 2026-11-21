# Note au rapport `contre-lecture-code-organisme-retenu-v5-cl1.md` — second passage du couplage, v1

Date : 2026-11-21. Le rapport n'est pas réécrit (R12) ; cette note donne le rendu du second passage déclaré (M4).

Sortie : `sorties/sortie-simulation-couplage-centrage-v2.txt` (entropie 162226683886763157841676160999520455752 ; 1 500 étalonnages par cas ; ancrage 0,9 ; w = 0,14). Arrêt à tort de la composante « chaîne réécrite » au niveau 1/80, bloc 4 (le code) contre bloc 8 (une suite prise au hasard) :

| forme | bloc 4 | bloc 8 | différence | erreur type | règle déclarée |
|---|---|---|---|---|---|
| normale | 1,1 % | 1,3 % | −0,2 point | 0,40 | non vu |
| asymétrique | 1,5 % | 1,3 % | +0,2 point | 0,43 | non vu |
| ronde | 1,2 % | 0,8 % | +0,4 point | 0,36 | non vu |

L'écart du premier passage (4,0 % contre 1,3 %, sur 150 étalonnages) n'est pas retrouvé. La pente de fuite n'est pas plus souvent arrêtée avec le bloc 4 (1,4 % à 1,7 %, contre 2,1 % à 2,3 % avec le bloc 8).

**Rendu de la règle écrite d'avance : effet non vu à cette précision, sous les trois formes. Ce que la règle commande : un erratum de rédaction du texte scellé** (la phrase de 3.3 sur ce que le couplage « garantit », et la docstring de `couplage_v5`), sans nœud, sans changement du code ni d'aucun seuil. Ces chiffres sortent d'un modèle de chaîne simplifié, non du modèle de langue réel.
