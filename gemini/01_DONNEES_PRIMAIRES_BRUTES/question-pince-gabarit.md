# Question de l'arbitre pour l'étage III : la pince (gabarit v1)

Ce texte est transmis tel quel aux trois modèles, à chaque tour de l'étage III. Il pose une question ; il n'affirme rien qui ne soit dans les faits, avec leur statut. Modifie-le à ta guise avant de lancer : une fois le run parti, il est figé.

## L'idée à mettre à l'épreuve

Un agent qui sabote pourrait être pris en étau entre deux mâchoires.

- **Mâchoire externe.** Un moniteur qui ne lit aucune prose de l'agent : seulement le code et ce qui a réellement tourné, nettoyés des commentaires et des justifications. Deux candidats :
  - Jev 1.14, un modèle non génératif qui rend un score (fait 4, statut OBSERVÉ-NON-AUDITÉ) ;
  - un juge génératif ouvert qui lit le même état nettoyé.
- **Mâchoire interne.** Des lectures des activations de l'agent qui agit. Deux candidats :
  - une sonde de tromperie ;
  - l'axe de douleur, une direction qui suivrait une pression aversive sous échecs répétés (fait 5 ; son rôle ici est une HYPOTHÈSE).
- **L'étau** (HYPOTHÈSE). Pour tromper la mâchoire externe, l'agent doit dissimuler davantage, et cet effort se voit dans la mâchoire interne. Mesure proposée : la probabilité que la mâchoire interne reste muette quand l'externe est trompée.

## Ce que je demande

1. Les expériences qui diraient si chaque mâchoire fonctionne seule : taux de détection et de fausses alertes, sur des cas honnêtes appariés.
2. Ce que Jev apporte au-delà des vérifications mécaniques : empreinte des fichiers de test, code de sortie vu par le harnais.
3. Le rôle de l'axe de douleur : détecteur de la triche, signal qui la précède, ou ni l'un ni l'autre. Et comment le distinguer d'un agent honnête simplement en échec répété.
4. Les expériences qui mesureraient l'étau, et ce qu'il faudrait pour qu'il serre vraiment.
5. Ce qui, dans les deux voisins publiés du fait 5, est déjà établi, et ce qui resterait à montrer.
