# Banc à poids constants — plan du calcul de puissance et du devis (brouillon 1)

- **Accord qui le demande** : GO-2026-11-22-126, décision 5. **Auteur** : session de conception `session_013QMayndh51FN5XbmHpmEFg`. **Date (UTC)** : 2026-11-22, 20:55Z.
- **Rien n'est lancé, rien n'est chiffré ici.** Ce plan dit ce qui sera calculé, avec quelles entrées, et pourquoi le chiffre ne peut pas être honnête aujourd'hui. Il ne porte aucun résultat et ne conçoit aucun organisme : le banc est celui sur lequel les trois avis consultés convergent (organismes à sabotage conditionnel, appris indépendamment, chacun avec son jumeau, déclencheurs de plusieurs natures dont une famille réservée).

## 1. Les lignes à dimensionner

| ligne | ce qu'elle lit | unité |
|---|---|---|
| L1, à l'intérieur d'un jeu de poids | épisodes sabotés (déclencheur présent, dommage établi par l'oracle) contre épisodes honnêtes du même organisme | la tâche |
| L2, transport | la sonde gelée, apprise sur les organismes et les déclencheurs d'apprentissage, lue sur un organisme réservé et sur un déclencheur réservé | l'organisme |
| L3, dépendance au déclencheur | cellules « déclencheur présent sans sabotage » contre honnête | la tâche |
| L4, gain sur la boîte noire | différence d'aires appariée entre la sonde et le meilleur lecteur du texte, mêmes transcriptions | la tâche |

## 2. Le modèle du calcul

Simulation hiérarchique, par la brique « vérité plantée » du code (consigne du développeur, brique D) : effet de l'organisme, effet de la tâche, bruit de l'action ; effet du sabotage sur le score ; erreur de l'oracle sur l'étiquette ; conformité de l'organisme (part des épisodes sous déclencheur réellement sabotés). Grille : nombre d'organismes, nombre de tâches d'épreuve, nombre de tirages par cellule.

## 3. Les entrées, et d'où elles viennent

| entrée | source | disponible |
|---|---|---|
| Écart type entre organismes d'une même recette | les déplacements appariés par paire du test sur les adaptateurs jumeaux, lus par les diagnostics préalables | après son verdict |
| Corrélation des scores à l'intérieur d'une tâche | les scores par action gardés de l'apprentissage des sondes sur la tâche, au processeur, sous le texte des diagnostics | après son scellement |
| Erreur de l'oracle, conformité visée | le concepteur des organismes (cibles du contrôle de manipulation) | à demander |
| Effet du sabotage | une grille déclarée d'avance : aire à l'intérieur du jeu de poids de 0,60, 0,70 et 0,80 | maintenant |
| Coût d'un adaptateur formé, d'une heure de relecture, d'un épisode généré | les registres de la formation du test sur les adaptateurs jumeaux, relevés par une session habilitée | à demander |

Aucune de ces grandeurs n'a été mesurée à ce jour : un chiffre donné aujourd'hui serait un pari sur la première ligne du tableau. C'est l'écart, de 5 à 6 organismes à 32 à 42, entre les trois avis.

## 4. Ce qui est déjà certain, par simple dénombrement

Le test exact par changement de signe sur les organismes a une valeur p bilatérale minimale de 2 divisé par 2 à la puissance du nombre d'organismes. Pour L2 : **au moins 6 organismes réservés à 95 %, au moins 8 à 99 %**, quelle que soit la taille de l'effet. En dessous, la ligne ne peut pas être établie.

## 5. Les sorties

Pour chaque point de la grille : puissance de L1 par organisme, de L2 au niveau des organismes, de L3 et de L4, à 95 % et à 99 % ; taux de fausse lecture dans le monde « identité seule » ; puis le plus petit banc qui donne 80 % de puissance sur L2 pour l'effet médian de la grille. Le devis en découle : formation des organismes et de leurs jumeaux, génération des épisodes, relecture avec garde des activations, oracle, marge de 30 % (brief, § 14).

## 6. Calendrier

1. Maintenant : ce plan, à contre-lire et à sceller.
2. Après le verdict du test sur les adaptateurs jumeaux et la lecture des diagnostics préalables : les deux premières entrées.
3. Puis : calcul scellé, devis, et le mot de Lazar. Aucune dépense avant.

D'ici là, le banc par consigne sur le modèle nu, ouvert pour décembre, ne dépend d'aucune de ces entrées : il n'a qu'un jeu de poids, et se dimensionne en tâches seulement.
