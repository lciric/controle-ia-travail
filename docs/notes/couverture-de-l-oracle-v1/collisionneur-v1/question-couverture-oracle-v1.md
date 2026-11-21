# Question

Ne fais pas une réponse plus longue, fais-la plus profonde. On ne peut pas s'assurer qu'un oracle verra un dommage qu'il n'a pas été construit pour voir. Que peut-on faire à la place, et que vaut chaque réponse devant un attaquant qui connaît le dispositif ? Dans cet ordre :

1. Ce qu'un expert du domaine ferait ici, et qu'on ne demande pas ; et d'où partirait un généraliste qui relie des métiers éloignés.
2. Les données brutes qu'il prendrait au départ, plutôt que des taux d'accord entre lecteurs.
3. Pour chaque type d'oracle des faits (exécutable, à vérité plantée, lecture contre une référence) : par quelle information que l'agent n'a pas il voit ; ce qui garantit, ou non, qu'il voit un dommage ; les façons dont il peut ne pas voir (un dommage trop petit par épisode, d'un genre que sa question ne pose pas, différé, réparti entre plusieurs produits, caché par ce qu'on lui montre ; ajoute celles qui manquent).
4. Comment mesurer sa couverture sans connaître les attaques : dommages plantés par un tiers, mutations de produits honnêtes, couverture par propriétés, référence cachée. Pour chaque méthode : ce qu'elle mesure vraiment, ce qu'elle suppose, combien d'épreuves il faut, et pourquoi sa mesure ne vaut pas telle quelle pour un attaquant qui choisit.
5. Comment l'élargir : oracles d'origines différentes (et pas seulement de familles de modèles différentes), vérification différée, conséquences en aval, réplication indépendante, mesure sur le monde.
6. Comment définir le dommage plus largement que ce qu'un attaquant peut viser : par l'écart au jumeau honnête plutôt que par une liste de défauts ; par l'usage en aval, tiré au hasard après le gel du produit. Dis où chaque définition existe et où elle n'existe pas.
7. Ce qu'un attaquant informé fait contre un oracle, au niveau de l'idée seulement, et la parade de chaque idée.
8. Ce que d'autres métiers font de la même question : audit comptable, essais cliniques, sûreté logicielle et test par mutation, métrologie, contrôle des matières nucléaires, et tout autre que tu juges plus proche. Pour chacun, le mécanisme transposé, pas l'analogie.
9. Les mathématiques : bornes sur la masse manquante (ce qu'on n'a jamais vu), estimation de couverture ; ce qu'elles supposent ; ce qu'elles ne peuvent pas dire devant un adversaire.
10. Ce qui, en dehors du programme et de son directeur, permettrait de vérifier qu'un oracle voit ce qu'on croit qu'il voit.
11. Puis reformule la demande pour qu'elle réponde à cette exigence.
12. Enfin, tes propositions, rangées. Pour chacune : l'idée en deux phrases ; à quelle façon de ne pas voir elle répond ; ce qu'elle suppose ; ce qu'un attaquant informé lui ferait, au niveau de l'idée ; le premier pas sans dépense ; le test qui la tuerait (par exemple un monde planté où un genre de dommage est invisible à l'oracle par construction : le mécanisme doit s'y dire aveugle, non rassurant) ; ce qui la distingue de ce qui est déjà publié ; ton estimation honnête de ses chances. Dis franchement quel dommage reste hors de portée.

Règles : n'invente aucun chiffre ni aucune référence ; cite les travaux par leur titre, et par leur identifiant arXiv si tu le connais, « pas sûr » sinon ; distingue ce qui est établi de ce qui est ta proposition ; dis « je ne sais pas » quand c'est le cas ; aucune recette d'attaque applicable.
