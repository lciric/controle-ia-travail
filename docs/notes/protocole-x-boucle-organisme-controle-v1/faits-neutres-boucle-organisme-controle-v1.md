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
- **Pistes déjà inscrites pour le dégel de l'organisme** : séparation entre distance de surface et alignement structurel sans fuite lexicale (graphes typés, signatures de rôle, transport optimal de graphes) ; détection d'obstructions et scission de concepts confondus ; mesure de progrès de compression entre bassins éloignés ; bancs publics datés sur processeur pour étalonner les heuristiques sans coût matériel lourd ; surveillance de la contamination temporelle lorsqu'un modèle pré-entraîné intervient.

## Le problème posé par la boucle de rétroaction

On souhaite relier ces deux systèmes en boucle fermée : améliorer l'organisme d'idéation afin qu'il découvre des idées profondes, de nouveaux objets mathématiques, des protocoles d'audit ou des attaques pertinentes directement exploitables dans le programme de contrôle, et utiliser en retour les problèmes, corpus et échecs du programme de contrôle pour orienter l'organisme.

Les risques identifiés dans la littérature sur les boucles adaptatives et l'évaluation de modèles sont :
- le sur-ajustement adaptatif lorsqu'un système itère sur un banc ou un évaluateur de taille finie ;
- la confusion entre raccourcis propres à un générateur synthétique et invariants réels transférables ;
- la perte d'utilité lorsque l'optimisation porte sur des mondes simplifiés qui manquent des classes d'invariants du domaine cible ;
- le gaspillage du budget de calcul sur cartes graphiques si le filtrage amont laisse passer trop de faux candidats.
