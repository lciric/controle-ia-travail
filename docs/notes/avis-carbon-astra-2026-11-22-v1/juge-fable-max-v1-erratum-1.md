# Erratum 1 au jugement sur le seuil de 0,75 — reproductibilité de la sortie du diagnostic

- Le 2026-11-22, par le juge, après le scellement du jugement (`juge-fable-max-v1.md`, `b1380fe3…`) et avant tout versement. Le jugement n'est pas modifié ; aucun nombre qu'il cite ne change.
- Porte sur la sortie texte du diagnostic, `juge-fable-max-v1-diagnostic-style-sortie.txt` (`f159e02a…`), citée au § 2 du jugement.

## Constat

1. Rejoué après le scellement, le script versé (`juge-fable-max-v1-diagnostic-style.py`, `79c6d862…`) rend le même détail chiffré, identique à l'octet (`juge-fable-max-v1-diagnostic-style-sortie.json`, `b717ae4f…`).
2. La sortie texte, elle, diffère à sa partie 5 (poids du classifieur) : l'ordre des jetons de même poids dépend du tirage de hachage du processus, et donc aussi le dernier jeton retenu quand la liste de douze se coupe au milieu d'ex æquo. Aucun poids ne change. Les quatre poids cités au § 2 du jugement (+3,83 ; −3,04 ; −2,75 ; −2,71) sont les mêmes dans les deux sorties.
3. Les sorties scellées ont été produites par une première rédaction du script, non versée (`9a95ca23…`). Elle ne différait de la version versée que par deux lignes du commentaire d'en-tête (la ligne d'auteur et le nom du fichier dans la ligne d'emploi).

## Conséquence

- La sortie texte n'est pas reproductible à l'octet ; le fichier JSON l'est, et il porte tous les nombres du tableau du § 2.
- Le vérificateur du code qui refera ce diagnostic triera les ex æquo par jeton, pour une sortie texte stable.
