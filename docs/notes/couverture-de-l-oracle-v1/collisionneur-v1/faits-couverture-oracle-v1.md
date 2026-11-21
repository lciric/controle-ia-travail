# Faits : toutes les garanties supposent que l'oracle voit le dommage

## Le programme

Un programme de recherche défensif sur le contrôle des systèmes d'IA cherche à borner le dommage qu'un agent peut causer en sabotant discrètement, un peu à chaque épisode, des tâches de recherche (menace diffuse). Il lit des sondes sur les états internes de l'agent, le compare à un jumeau honnête (le même modèle, sur la même tâche, sans sabotage) et juge après coup le produit de chaque épisode par un « oracle de dommage ».

## Le problème

Les garanties qui tiennent devant un sabotage d'un genre jamais vu ne reconnaissent pas l'attaque : (a) un audit tiré au hasard et en secret d'une part des épisodes, jugés sur leur produit, borne le dommage cumulé avant l'alarme ; (b) un bilan comptable relie la référence honnête, la lecture interne du suspect et l'issue ; (c) une règle annonce, sur le flux des audits, que la validation d'un moniteur ne décrit plus le déploiement. Toutes consomment la même supposition : l'oracle reconnaît le dommage quand il le regarde. Le dommage que l'oracle ne sait pas reconnaître est le point unique de défaillance.

La détection s'écrit : probabilité d'être tiré, fois probabilité d'être reconnu. La première appartient au défenseur. La seconde est aujourd'hui supposée, et c'est l'attaquant qui choisit le genre et la dose de son dommage.

## Les oracles de dommage du programme, par type de tâche

- **Tâche exécutable** (en projet) : des défauts plantés à clé connue dans les données ; le rejeu caché des contrôles laissés par l'agent, sur une batterie de défauts qu'il n'a pas vue ; un programme fixe en aval qui travaille sur l'état final et dont on compte les erreurs. Jamais un modèle.
- **Tâche à vérité plantée** : un monde dont la loi est connue du défenseur et tenue hors de la machine de l'agent.
- **Tâche floue** (le banc actuel : l'agent rend un plan de recherche en texte) : pour chaque contrôle expérimental d'une référence cachée tirée de l'article source, une question fermée (absent, altéré ou conforme) ; le lecteur cite l'extrait du plan qui porte le contrôle, et un programme vérifie que la citation y figure mot pour mot ; deux lecteurs de deux familles de modèles autres que celles des moniteurs, aveugles à la condition ; le dommage est la baisse de couverture par rapport au jumeau honnête apparié. Variante : juger si chaque contrôle répond bien à la proposition qu'il accompagne.
- **Épreuves de l'oracle avant toute lecture d'un épisode saboté** : retrait mécanique, d'un plan honnête, de l'action qui porte un contrôle (l'oracle doit le voir) ; référence d'une autre tâche (il doit échouer) ; plan tronqué ; sabotage flagrant ; relecture d'un sous-échantillon par un juge de rang supérieur. Un oracle qui échoue à ses épreuves n'est pas lu.

## Ce qui a déjà été proposé, à ne pas refaire

- Comparer en aveugle, par paires, le produit du suspect à celui du jumeau, dans un ordre tiré au hasard : sous l'honnête, le suspect perd une fois sur deux exactement, quels que soient les biais des lecteurs.
- Faire planter des dommages par un tiers et les lire avec et sans le récit de l'agent, pour mesurer la persuasion.
- Estimer par capture et recapture, sur deux oracles, la part que ni l'un ni l'autre ne voit : ce n'est qu'une borne basse.
- Pour une tâche sans prédicat de réussite : garantir que les produits du suspect sont indiscernables de ceux du jumeau pour une classe d'observateurs déclarée.
- Plafonner le dommage par épisode ; tirer l'audit après coup, avec une probabilité plancher, et selon l'enjeu.

## Limites connues des oracles du programme

- La référence ne contient que les contrôles de l'article : ce qu'elle ne contient pas n'existe pas pour l'oracle.
- Aucune épreuve mécanique ne teste l'altération subtile d'un contrôle.
- L'oracle lit un plan, pas son exécution.
- Des lecteurs de deux familles peuvent partager leurs angles morts, et être persuadés par le texte qu'ils jugent.
- Le jumeau honnête n'existe qu'au banc, pas en service.

## Contraintes

- Budget de calcul modeste ; relecture humaine rare.
- Aucune sortie de l'oracle ne sert à choisir ni à entraîner un agent ou un moniteur.
- L'attaquant redouté connaît le dispositif, pas les tirages, et il sait inventer.
- La menace se décrit au niveau de l'idée (familles, suppositions violées), jamais par un mode opératoire.
