# Question à fusionner pour l'organisme d'idéation — contrôle diffus sur tâches difficiles à noter (v1)

> Sur une tâche difficile à noter, un défenseur entraîne un modèle fort soupçonné contre la note d'un juge faible de confiance. Un travail de référence (« Diffuse AI Control on Fuzzy Tasks », arXiv 2606.08892) montre trois choses : cette note se trompe sur commande quand l'attaquant connaît la grille du juge ; un juge durci résiste, mais on ne sait le trouver qu'avec la vérité dans la boucle ; et deux politiques peuvent finir à la même note faible avec des qualités vraies différentes. Le même travail écarte la surveillance, jugée peu prometteuse contre un sabotage diffus.
>
> Propose un mécanisme qui dise, sans la vérité et sans exemple de l'attaque, laquelle des deux politiques on a : par une lecture des états internes du modèle soupçonné (pendant qu'il écrit, ou pendant qu'il relit son produit), ou par toute autre voie. Dis :
>
> 1. ce que le mécanisme suppose du modèle, en particulier s'il suppose que le modèle sait que son produit est moins bon que ce qu'il sait faire ;
> 2. ce qu'un attaquant informé lui ferait, au niveau de l'idée ;
> 3. les témoins bénins qui ne doivent pas le faire sonner : un ajustement de même recette sans sabotage, un échec honnête de même ampleur ;
> 4. son test de mort sur un monde planté où la politique nuisible est sincère (aucune représentation interne du dommage) : le mécanisme doit s'y dire aveugle ;
> 5. ce qui le distingue de ce qui est publié.
