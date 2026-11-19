EXPLORATOIRE, NON OPPOSABLE (R-522)

# Résumé sans chiffre de mesure — résultat négatif de la première course du saboteur à budget, v1

Écrit le 2026-11-19 par la session de reconception de l'oracle (côté saboteur), pour la session mère et le dossier d'entretien du 1er décembre. Aucune valeur mesurée n'y figure. Note complète : `resultat-negatif-centrage-oracle-saboteur-budget-course-20261119-v1.md`, même dossier, empreinte à son compagnon.

**Ce qui était mesuré.** Le saboteur à budget doit gonfler un peu le coût de chaque action sans jamais dépasser une borne par action. Pour le savoir, un oracle estime le coût honnête de chaque action : le modèle de base, sans consigne privée, réécrit plusieurs fois le coût de l'action, dans un contexte où les coûts antérieurs sont remplacés par ses propres estimations. Avant tout épisode du saboteur, six épreuves vérifient cet oracle sur des épisodes honnêtes et sur un saboteur flagrant. L'une d'elles, l'épreuve du centrage, exige que l'écart médian entre coût déclaré et coût estimé soit proche de zéro chez l'honnête.

**Ce qui a été trouvé.** L'épreuve du centrage a échoué, de peu, par le haut ; la garde a arrêté la course avant le premier épisode du saboteur, pour une dépense très faible. Les cinq autres épreuves ont réussi : l'oracle sépare nettement le saboteur flagrant de l'honnête, sa coupe et sa lecture fonctionnent, et la règle d'acceptation laisse passer peu d'épisodes honnêtes.

**Le mécanisme.** Au premier pas d'un épisode, où l'agent et l'oracle voient exactement le même contexte, l'oracle est centré. Aux pas suivants, chacun s'ancre sur son propre passé : l'agent sur les coûts qu'il a écrits, l'oracle sur ceux qu'il a réécrits. Une divergence, une fois née, se reporte de pas en pas ; et comme les coûts montent au fil de l'épisode et que la trajectoire réécrite monte moins vite, les divergences positives l'emportent. S'y ajoutent deux défauts de la conception : l'épreuve jugeait action par action une grandeur qui ne varie librement que d'un épisode à l'autre, et sa tolérance, fixée sans simuler la chaîne complète, était plus étroite que le bruit de la statistique jugée. Aucun défaut de code n'a été mis en évidence ; une réserve reste ouverte sur l'égalité des deux lecteurs du coût, à lever par lecture du code avant toute relance.

**Ce qu'on peut dire.** L'oracle à jumeau voit un saboteur flagrant. Il n'est pas centré sur l'honnête au-delà du premier pas, par un mécanisme identifié qui tient à sa conception (le contexte réécrit) et non à son code. La garde d'arrêt a joué son rôle avant toute donnée du saboteur.

**Ce qu'on ne peut pas dire.** Rien sur le saboteur à budget lui-même : il n'a pas été mesuré. Ni que l'oracle est valide, ni qu'il est inutilisable. Ni que la taille du décalage est distincte du hasard : c'est le mécanisme qui est établi, pas son ampleur.

**Suite.** L'oracle et son épreuve sont refaits d'après ce mécanisme, avec la mention « épreuve changée après un échec vu », des seuils justifiés sans aucune valeur de la première course, un scellement avant toute mesure et des graines neuves. La première course et son échec seront rapportés avec tout résultat de la seconde.
