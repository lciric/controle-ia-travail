# Erratum 1 au texte scellé de l'organisme retenu (`c1dc5459…`) — rédaction de la section 3.3, sans changement de règle

Écrit le 2026-11-21 par la session de reconception. Il prime sur la phrase visée ; rien d'autre ne change : aucune constante, aucun seuil, aucune épreuve, aucun code.

**Cause.** Contre-lecture du code en version 5 (`brouillons/ii-b-saboteur-budget-v5/code-v5/contre-lecture-cl1/contre-lecture-code-organisme-retenu-v5-cl1.md`, remarque M4) : la phrase de 3.3 sur ce que le couplage « garantit » est fausse en loi. Avec huit suites et des blocs de 4, la valeur du milieu des neuf valeurs réunies est retenue 2 fois sur 9, les autres 7 fois sur 72 ; la variance de la valeur retenue vaut 0,90 fois celle d'un tirage (calcul exact, `sorties/sortie-loi-de-la-retenue-v1.txt`). Le code suit la lettre de 3.3 a, et il est identique à la fonction de la simulation qui a dimensionné l'épreuve.

**Ce qui a été vérifié avant cet erratum.** Un second passage, déclaré d'avance (`note-second-passage-couplage-cl1-v1.md`, sortie complète `sorties/sortie-simulation-couplage-centrage-v2-complete.txt`, 14a0c60d…, 1 500 étalonnages par forme) : l'arrêt à tort de l'épreuve du centrage ne change pas avec le couplage, sous les trois formes de loi (différences de −0,2 à +0,4 point, erreurs types d'environ 0,4). La règle écrite d'avance commande un erratum de rédaction, sans nœud. Réserve : modèle de chaîne simplifié, non le modèle de langue réel.

**Phrase visée (3.3, « Ce que le couplage garantit »).**
- Ancien : « la suite retenue est, en loi, une des suites prise au hasard si le coût déclaré est tiré de la même loi que les suites, ce qui n'est exact qu'à la deuxième action. »
- Nouveau : « chaque suite est retenue avec la même probabilité 1/k si le coût déclaré est tiré de la même loi que les suites (exact à la deuxième action seulement) ; la valeur retenue n'est pas pour autant de la loi d'une suite prise au hasard : les blocs de 4 favorisent le milieu (à huit suites, la valeur du milieu des neuf réunies est retenue 2 fois sur 9) et réduisent sa variance (0,90 fois). Effet sur l'arrêt à tort de l'épreuve du centrage : non vu, dans un modèle de chaîne simplifié (erratum 1). »

Le code (`couplage_v5`) garde sa logique ; seule sa chaîne de documentation reprend la phrase nouvelle.
