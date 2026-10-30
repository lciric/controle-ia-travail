# Réponse de conv-audit à la question 4 (apprendre concepts, dimensions, chapelles, hypergraphe, paramètres) — v1

conv-audit, 30 octobre 2026 (Fable 5.1, 18:05 heure de Paris), transcrite sans modification de fond. Références de mémoire : SUPPOSÉ.

**Position.** Oui, et c'est déjà la forme standard du problème : prédire quels liens entre concepts, auteurs ou niches apparaîtront après une coupure, à partir du graphe d'avant (Krenn / Science4Cast, Shi-Evans, Sourati-Evans). Neuf chez nous : apprendre la représentation elle-même (dimensions, chapelles, hypergraphe) au lieu de la coder à la main, et traiter la sortie comme une fertilité calibrée. Ce qu'un modèle apprend le plus facilement est la popularité, pas la fertilité : tout le soin va dans les témoins et les fuites.

## (1) Ce qu'un expert ferait, et que Lazar ne demande pas
- Séparer trois apprentissages : structure (quels nœuds et hyperarêtes : auteurs, concepts, méthodes, jeux de données, équations) ; fonction (probabilité de reprise d'une paire, supervisée) ; loi (seuil ou cloche dans un paramètre de contrôle : ajustement de physique statistique sur la fonction apprise).
- Fermer trois fuites : temporelle (plongements de texte préentraînés sur l'après-coupure ; il faut des plongements d'avant-coupure ou une coupure postérieure à l'entraînement) ; biais du survivant (témoins durs appariés en taille, âge, distance, jamais reliés) ; effet Matthieu (contrôler degré et âge).
- Garder l'interprétabilité par construction : goulot de traits nommés (communication, structure commune, désaccord, densité de contacts) puis ablation ; ou entraînement libre puis régression symbolique.
- Distinguer prédire et causer : pour les « paramètres qui créent », quasi-expériences (déménagements, conférences, expériences humaines contrôlées comme Derex et Boyd).
- Tester la transition de phase comme propriété de la fonction apprise : seuil contre cloche contre droite ; pic de variance ; mise à l'échelle avec la taille des sous-domaines.
- Boucler avec le bisociateur sous préenregistrement (apprentissage actif : le modèle propose, les tests de mort étiquettent).
- Chiffrer : sous-domaine (contrôle des IA) sur processeur ; OpenAlex entier ou affinage d'un modèle de langage sur cartes graphiques, devis.

## (2) Données brutes
OpenAlex complet (articles, concepts et sujets, auteurs, références, dates) ; Semantic Scholar (contexte et intention des citations) ; sources LaTeX d'arXiv (équations), jeux de données et code réutilisés ; bancs existants (graphe de concepts d'IA de Science4Cast 2015-2021, graphe de physique quantique de Krenn, hypergraphe matériaux de Sourati-Evans, redécouvertes étalons d'Arrowsmith) ; brevets avec classes ; nos courses (fiches, verdicts, survie aux tests de mort).

## (3) Méthodes et outils
Hypergraphe temporel multicouche (une hyperarête par article ; tranche par année) ; chapelles par communautés multicouches (Leiden), puis partition apprise comparée ; prédiction de liens futurs par réseaux sur hypergraphes et graphes temporels contre lignes de base (marche de Swanson, voisins communs, Adamic-Adar, node2vec) ; partage temporel strict (entraînement < T1, validation T1-T2, test > T2) ; témoins durs appariés ; aire sous la courbe et précision dans les k premiers avec taux de base ; sortie calibrée (diagrammes de fiabilité) ; goulot de concepts, attribution, régression symbolique ; transition de phase (formes, mise à l'échelle, variance) ; transfert entre domaines.

## (4) Vérification hors de nous
Le futur (période postérieure à l'entraînement) ; bancs publics et leurs classements (Science4Cast), redécouvertes d'Arrowsmith ; transfert entre domaines ; reproduction (OpenAlex, code, préenregistrement daté) ; tests de mort.

## Reformulation
« Apprendre, plutôt que décréter, la représentation des niches et la fonction de fertilité. 1. Construire l'hypergraphe temporel multicouche depuis OpenAlex, Semantic Scholar et arXiv. 2. Entraîner un modèle à prédire les liens futurs entre niches sous coupure stricte, témoins durs appariés, contrôle des taux de base, plongements sans fuite ; sortie calibrée = fertilité. 3. Interprétabilité forcée (goulot, ablation, régression symbolique). 4. Transition de phase comme propriété de la fonction apprise, avec ce qui la réfuterait. 5. Validation sur bancs publics, transfert, futur ; boucle avec le bisociateur et les tests de mort sous préenregistrement. 6. Sous-domaine du contrôle des IA sur processeur d'abord ; passage à l'échelle sur devis. »
