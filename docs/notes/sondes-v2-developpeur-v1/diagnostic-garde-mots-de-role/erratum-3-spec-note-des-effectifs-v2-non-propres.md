# Erratum 3 à la spécification v2 de la note des effectifs : clés communes des séries non propres

- **Porte sur** la spécification v2 (`0ebc790a…`) et ses errata 1 et 2 ; en cas d'écart, cet erratum prime. Classe B. **Décision** : mot de la mère, 2026-11-24, vers 00:00Z (routine sur un instrument), sur le point 5 de l'erratum 2.
- **Écrit par** le développeur des sondes v2, session_016QhUrtqKazbonFiVhXMm3R, le 2026-11-23T23:37Z. **Aucun résultat.**

1. Section `activations` : un champ `"non_propres_aux_cles_communes"` est ajouté. C'est un booléen ; il est vrai si toute série qui n'est pas propre (ancres et « autres » comprises, qu'elles soient nommées ou comptées) porte exactement les clés communes. S'il est faux, une réserve écrite est exigée, et elle désigne les séries publiques par leur catégorie et leur rang (erratum 2, point 2).
2. Chargeur : champ exigé, valeur booléenne, réserve exigée s'il est faux. Essais : un cas sain avec réserve et trois artefacts.
