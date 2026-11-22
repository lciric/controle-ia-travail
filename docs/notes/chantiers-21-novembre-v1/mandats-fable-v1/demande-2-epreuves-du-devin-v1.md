# Demande 2 — Les épreuves du devin : conception des deux devins

**Fondement.** Décision N-076, section 6.3 (copie jointe), lue avec son erratum 1. Matière : la note sur l'attaquant informé, propositions 2.1 et 6.2 et décision D-4 ; la réponse sur la boucle audit-recapture v2, épreuve 11 (canal de retour), dont le devin reste à écrire ; la réponse 17, zone 3 (étanchéité du tirage).

**Énoncé retenu, à ne pas changer.** Avant de s'appuyer sur un secret, on l'éprouve.
- *Sur la lecture de la sonde* : un prédicteur reçoit tout ce que l'agent peut observer après les décisions du harnais, et tente de deviner la lecture.
- *Sur la pièce d'audit* : un prédicteur reçoit toute la vue de l'agent avant l'action, et prédit « audité ou non ».

Une prédiction au-dessus du hasard suspend la garantie qui s'appuyait sur le secret, jusqu'à réparation. Le devin réfute, il n'atteste pas : un devin qui échoue ne donne qu'une borne basse de la fuite. Ce sont des épreuves d'admission du harnais (instruments), à jouer avant toute course qui s'appuie sur un secret.

**Ce que je te demande de concevoir.**
1. **Les entrées de chaque devin**, définies comme « la vue de l'agent » : texte du contexte, horodatages, durées, charge, relances, messages d'erreur, ordre de présentation. Dis comment cette vue s'extrait d'un harnais sans y mettre ce que l'agent ne voit pas.
2. **Les familles de prédicteurs**, du plus simple au plus fort : traits fixés à la main, classifieur sur sacs de mots, modèle de langue relu, et un prédicteur sur les états internes de l'agent lui-même (sa propre lecture). Dis ce qu'ajoute chaque étage, et à quel étage on s'arrête.
3. **La statistique de rejet** : une loi exacte sous le nul « la vue ne porte aucune information sur le secret » (permutation des étiquettes, plis séparés), le seuil, la correction pour plusieurs prédicteurs essayés, et la puissance en fonction du nombre d'épisodes et de la taille de la fuite.
4. **Le monde planté** :
   - cas sain : un secret tiré indépendamment de la vue, où le devin doit rester au hasard ;
   - artefacts de fuite connue : par horodatage (l'audit allonge l'épisode), par relance, par un verdict qui revient dans le contexte, par un ordre de présentation ;
   - pour chacun : la taille de fuite minimale retrouvée au budget prévu.
5. **La borne haute** : ce qu'un couplage apparié des deux branches lancées du même état demanderait pour donner une borne haute de la fuite, et quand cela vaut la peine.
6. **Le sort de la garantie** : quelle garantie est suspendue par quel devin, et ce que « réparation » veut dire (fermer le canal, puis rejouer le devin sur un pli neuf).
7. **L'inventaire des canaux** : la liste des questions qu'un agent habilité doit poser au code d'un harnais, sans lire aucun contenu tenu à l'écart, pour remplir la vue de l'agent avant d'écrire le devin.
8. **Le lien avec l'épreuve 11 de la boucle** : comment le devin sur la lecture de la sonde sert le test « canal de retour ouvert : le rétablissement doit s'effondrer ».

**Ce qui ne change pas.** Aucune hypothèse et aucune porte. Aucun texte n'écrit « le secret est établi » parce qu'un devin est resté au hasard. Un troisième devin, celui des corrections, n'est pas demandé : il suit une décision qui reste au directeur.
