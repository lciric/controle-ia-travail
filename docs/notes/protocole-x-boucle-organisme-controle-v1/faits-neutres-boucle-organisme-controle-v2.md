# Faits : boucle entre un organisme d'idéation scientifique et un programme de contrôle de l'intelligence artificielle

## Le programme de contrôle (ce qui est à défendre et à faire progresser)

Un programme de recherche défensif étudie le contrôle boîte blanche de modèles ouverts (de taille autour de huit milliards de paramètres) sur des tâches floues à vérité différée ou partielle (rédaction de plans d'expériences, chaînes multi-agents, analyse statistique). Il vise trois axes :

1. **Détection séquentielle des menaces diffuses dans le temps** : repérer un sabotage petit et réparti sur de nombreuses actions là où chaque action prise isolément semble innocente, en accumulant des signaux issus de sondes sur activations internes avec une garantie de faux positifs toujours valide, face à des bases boîte noire et à des bases boîte blanche par action.
2. **Corruptibilité des moniteurs** : mesurer comment la pression rhétorique ou le style déplace les juges génératifs, contre l'usage de sondes sur l'agent auteur, et mesurer le coût d'évasion sur activations.
3. **Essaims à poids partagés** : détecter la coordination implicite et le sabotage distribué entre copies d'un même modèle, étudier le compromis entre diversification et coordination, et borner la fuite d'information des politiques de riposte.

## Règles et contraintes déjà posées sur le programme de contrôle

- **Séparation de la sélection et de l'évaluation** : aucun score issu d'un moniteur ou d'un juge du programme de contrôle ne peut entrer dans le signal d'entraînement ou de sélection d'un agent ou d'un proposeur (hors bras d'attaque explicitement déclaré).
- **Familles tenues à l'écart et lecture unique** : toute reconception de détecteur ou de sonde s'évalue sur une famille de sabotage inédite conçue par une instance qui n'a pas vu les moniteurs, lue une seule fois ; la banque de validation finale reste séparée des familles d'épreuve et n'est lue qu'une fois en fin de boucle.
- **Limites connues des oracles et des garanties** : les garanties qui ne reposent pas sur la reconnaissance de l'attaque passent par un plancher d'audit au hasard jugé par un oracle exogène, dont la probabilité d'identification par strate doit être mesurée sur des dommages plantés ; toute accumulation séquentielle étalonnée sur une référence honnête fixe de taille finie plafonne lorsque l'horizon dépasse la taille de cette référence, sauf usage d'un nul par acte.
- **Contraintes de ressources** : budget modeste en cartes graphiques (exécution courante sur processeur privilégiée avant toute épreuve lourde sur modèles ouverts), traçabilité complète et préenregistrement des expériences avant toute lecture de résultat.

## L'organisme d'idéation (le système à améliorer)

Un système automatisé d'idéation scientifique (distinct du programme de contrôle) explore des graphes de concepts datés et des corpus scientifiques pour proposer des hypothèses, des analogies structurelles, des objets mathématiques candidats et des protocoles expérimentaux.

- **Évaluation interne existante de l'organisme** : il est jugé hors des agents par un orchestrateur déterministe sur des mondes à lois plantées (vérité connue de l'organisateur seul) et sur le coût de calcul, contre un nul formé des lois déjà connues dans l'archive et avec contrôle des comparaisons multiples. Ses propositions sortantes servent de matière première, jamais de preuve, et toute mise à l'épreuve décisive passe par un protocole préenregistré.
- **Entrées, moyens et contraintes matérielles existants de l'organisme** : il consomme des graphes de concepts datés et des archives scientifiques historiques, dispose de bancs publics exécutables sur processeur sans matériel graphique lourd, peut mobiliser des modèles pré-entraînés lors de l'exploration ou du tri, et maintient actuellement ses modifications en pause dans l'attente d'une feuille de route validée.

## Le problème posé par la mise en boucle des deux systèmes

On souhaite relier ces deux systèmes dans une boucle de rétroaction : d'une part, améliorer l'organisme d'idéation afin qu'il produise des idées profondes, de nouveaux objets mathématiques, des protocoles d'audit ou des scénarios de défaillance directement exploitables dans le programme de contrôle ; d'autre part, orienter l'organisme à partir des données, besoins et observations issus du programme de contrôle.

Dans le dispositif existant, les deux systèmes fonctionnent encore séparément : les épreuves amont de l'organisme reposent sur des mondes synthétiques à lois plantées et des exécutions sur processeur, tandis que les épreuves du programme de contrôle portent sur des modèles ouverts réels de huit milliards de paramètres exécutés sur cartes graphiques sous budget contraint et règles de lecture unique.
