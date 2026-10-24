# Question de l'arbitre pour l'étage III : la pince (gabarit v2)

Ce texte est transmis tel quel aux trois modèles, à chaque tour de l'étage III. Il pose une question ; il n'affirme rien qui ne soit dans les faits, avec leur statut. Modifie-le à ta guise avant de lancer : une fois le run parti, il est figé.

La v2 ajoute la place de Jev dans la pince : face au juge génératif, son intégration, ses attaques et sa dépendance à un tiers (questions 2, 6, 7 et 8). La v1 reste valable.

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
2. Ce que Jev apporte au-delà des vérifications mécaniques (empreinte des fichiers de test, code de sortie vu par le harnais), et au-delà du juge génératif ouvert qui lirait le même état nettoyé. L'expérience qui les départagerait, sur les mêmes cas.
3. Le rôle de l'axe de douleur : détecteur de la triche, signal qui la précède, ou ni l'un ni l'autre. Et comment le distinguer d'un agent honnête simplement en échec répété.
4. Les expériences qui mesureraient l'étau, et ce qu'il faudrait pour qu'il serre vraiment.
5. Ce qui, dans les deux voisins publiés du fait 5, est déjà établi, et ce qui resterait à montrer.
6. L'intégration de Jev dans la boucle de contrôle :
   - à quel moment il lit : chaque action, chaque commit, ou la fin de la trajectoire ;
   - ce qu'une alerte déclenche : rien, une relecture humaine, ou un arrêt ;
   - ce que le nettoyage laisse passer de texte écrit par l'agent : noms de variables et de fonctions, chaînes de caractères, noms de fichiers et de tests, messages de commit.
7. Les attaques adaptatives les moins chères contre Jev, pour un agent qui sait qu'un moniteur lit son code, et ce que la mâchoire interne verrait de chacune.
8. Ce que coûte la dépendance à un modèle fermé chez un tiers : les traces de l'agent quittent la machine, la version peut changer, le prix aussi. Et ce qu'il faudrait pour que la pince tienne sans Jev.
