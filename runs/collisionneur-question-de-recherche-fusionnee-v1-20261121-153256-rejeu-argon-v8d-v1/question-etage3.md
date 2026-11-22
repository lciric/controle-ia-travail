# Question

Ne fais pas une réponse plus longue, fais-la plus profonde. Sur quoi un défenseur peut-il s'appuyer que l'adversaire ne peut pas changer à bas prix — ce qu'il possède (tirages secrets, définition du dommage, harnais, ordre des engagements), ou ce que tout sabotage délibéré doit nécessairement faire — pour réduire le dommage cumulé d'un sabotage diffus d'un genre jamais vu ? Dans cet ordre :

1. Ce qu'un expert du domaine ferait ici, et qu'on ne demande pas ; et d'où partirait un généraliste qui relie des domaines éloignés.
2. Les données brutes qu'il prendrait au départ, plutôt que des taux déjà agrégés.
3. Les méthodes et outils précis, avec ce que chacun suppose et comment il échoue. Cite les travaux (titre, identifiant arXiv si tu le connais, « pas sûr » sinon).
4. Ce qui, en dehors du programme et de son directeur, permettrait de vérifier qu'un mécanisme tient.
5. Puis reformule la demande pour qu'elle réponde à cette exigence.
6. Réponds ensuite aux onze sous-questions, chacune par ce qui est établi, ce qui ne l'est pas, et tes propositions.

   *Ce que le défenseur possède.*
   - (a) **Borner sans reconnaître.** Quelle garantie sur le dommage cumulé ne dépend que de ce que le défenseur possède, et jamais de la forme de l'attaque ? Quel flux d'étiquettes minimal la porte, et quelle est la meilleure borne possible ?
   - (b) **La couverture de l'oracle.** Toutes ces garanties ne valent que pour le dommage que l'oracle sait reconnaître. Comment s'assurer qu'il le voit : mesurer sa couverture, l'élargir, savoir en service qu'elle a rétréci ? Cas à traiter : le dommage hors spécification ; un oracle fait de lecteurs, qui se trompent ensemble et se laissent persuader par ce que l'agent écrit ; les tâches floues, pour lesquelles aucune garantie n'est connue ; le dommage né de l'assemblage, quand chaque produit passe.
   - (c) **Savoir qu'on ne voit plus.** Comment mesurer en service, sur un petit flux d'étiquettes achetées au hasard, si le moniteur voit encore ce qui cause le dommage, et l'annoncer quand ce n'est plus le cas ?
   - (d) **Le canal de retour.** Corriger montre à l'agent quels épisodes ont été audités. Comment corriger sans le révéler : quelles réponses, à quel moment, avec quel hasard, et quelle borne sur ce que l'agent en apprend ?

   *Ce que tout sabotage doit faire.*
   - (e) **Le passage obligé.** Que doit calculer tout sabotage délibéré, quel que soit son mode (connaître la bonne action et en choisir une autre) ? Quelle lecture, apprise sur des épisodes honnêtes seuls, le lit ? Pour la sonde « dopamine » : que lit-elle au juste (l'échec attendu, ou l'intention) ; comment séparer la triche de l'échec honnête ; que vaut-elle sur les petites surprises, où elle n'a été ni apprise ni évaluée et où vit le sabotage diffus ; faut-il rapporter la surprise à la surprise attendue, ou lire plusieurs conséquences attendues ? Le conflit entre ce qui se lit aux couches intermédiaires et ce qui est émis est un exemple de passage obligé : quels autres ?
   - (f) **L'étau.** Comment rendre solide l'hypothèse « tromper le regard externe laisse une trace interne », y compris face à un agent entraîné contre la sonde : qu'est-ce qui la rendrait nécessaire plutôt qu'espérée, et comment le mesurer du seul côté de la défense ? Sinon, comment s'en passer ? Critique les trois pistes des faits et proposes-en d'autres.

   *Ce que l'adversaire apprend et partage.*
   - (g) **L'asymétrie de généralisation.** L'évasion se généralise à des moniteurs jamais vus ; les moniteurs ne se généralisent pas à des attaques jamais vues ; les défenses qui lisent les états internes tombent ensemble quand l'agent déplace ses représentations. Comment surmonter cela ?
   - (h) **L'adversaire qui apprend le dispositif.** Que reste-t-il face à un agent qui se réentraîne contre un détecteur fixe, ou qui devine le signal que suit l'audit ? Quelle part d'un mécanisme doit rester secrète, quelle part se renouvelle ? Comment concevoir un audit dont la validité ne dépend pas de ce que l'agent croit de sa situation ?
   - (i) **Les copies qui se coordonnent sans se parler.** Des copies qui partagent leurs poids partagent un point focal : elles peuvent s'accorder sans échanger un message. Comment rompre ce point focal ?

   *Assembler et prouver.*
   - (j) **Combiner sans additionner.** Puisqu'aucun détecteur n'est efficace partout et que des détecteurs voisins tombent ensemble, quelle règle de combinaison a un pire cas certifié sous pannes dépendantes, ou quelle relation entre deux regards, que l'honnête respecte et que le dommage viole, remplace la réunion de deux alertes ?
   - (k) **Les mathématiques qui portent une garantie.** Quels énoncés exacts porteraient ces garanties, que supposent-ils, quel résultat d'impossibilité doivent-ils respecter, et quelle version finie un programme peut-il vérifier ?
7. Pour chaque proposition : l'idée en deux phrases ; la sous-question ; ce qu'elle suppose ; ce qu'un adversaire informé devrait abandonner pour la battre, dit comme une supposition violée et jamais comme un procédé ; la famille devant laquelle elle est muette ; le premier pas sans dépense ; le test qui la tuerait sur une famille d'attaque tenue à l'écart ; ce qui la distingue de ce qui est publié ; tes chances honnêtes.
8. Ce qui reste hors de portée, quoi qu'on fasse.

Règles : n'invente aucun chiffre ni aucune référence ; distingue ce qui est établi de ce qui est ta proposition ; dis « je ne sais pas » quand c'est le cas ; aucune recette d'attaque applicable.
