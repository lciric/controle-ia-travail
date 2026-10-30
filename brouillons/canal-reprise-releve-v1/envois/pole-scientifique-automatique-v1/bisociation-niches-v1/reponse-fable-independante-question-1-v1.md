# Réponse indépendante à la question 1 — distance entre chapelles — v1

- Répondant : sous-agent neuf, indépendant (n'a lu que `question-1-chapelles-v1.md`).
- Modèle : Claude Fable 5.1 (`claude-fable-5-1`).
- Date : Fri Oct 30 16:19:50 UTC 2026.
- Niveau : méthode. Aucune décision prise. Références marquées SUPPOSÉ quand non vérifiées ; les deux références marquées « vérifiée (existence) » ont été confirmées par recherche web sur le titre, l'année et la revue seulement, pas sur le contenu ni sur la page.

## 1. Ce qu'un expert ferait ici et que la demande ne formule pas

Trois experts sont concernés, et chacun commencerait par une étape que la demande saute.

**Le sociologue ou historien des sciences** (Fleck 1935, « collectifs de pensée » ; Kuhn 1962 ; Collins 1998, réseaux de rivalité intellectuelle ; SUPPOSÉ) exigerait une **définition opérationnelle falsifiable** : à quel signe observable reconnaît-on que deux groupes « ne se parlent pas » ? Il séparerait quatre relations que la demande mêle : (a) ne pas se citer, (b) vocabulaires disjoints, (c) objets ou échelles disjoints, (d) prémisses incompatibles. Elles ne coïncident pas : deux chapelles cosmologiques se citent abondamment pour se contredire. La non-communication est une **relation asymétrique et multi-couches**, pas une métrique ; il faut dire quelle couche la bisociation veut combler.

**Le scientométricien** (Small 1973 ; Fortunato et collègues 2018 ; SUPPOSÉ) exigerait un **étalon** : des paires de chapelles dont l'éloignement est connu par l'histoire (interprétations de la mécanique quantique, neurosciences dynamiques contre neurosciences par régions), étiquetées par des humains du domaine *avant* toute mesure ; sans étalon, toute distance s'auto-valide. Plus un **témoin négatif** : des sous-domaines qui se parlent bien, que la mesure doit placer près.

**Le mathématicien** demanderait si la distance doit être une **métrique** (symétrie, inégalité triangulaire) ou une **divergence** ; la divergence de Kullback-Leibler est asymétrique, et c'est utile : A peut lire B sans que B lise A. Il préciserait que « mêmes objets mathématiques sans s'en rendre compte » est une relation de **structure partagée** (isomorphisme partiel entre modèles), à détecter sur des équations et des symétries, pas sur des mots.

Tous trois noteraient que la « lecture exhaustive sur la genèse des idées » est un **autre travail**, à **borner** : exhaustivité impossible ; corpus de départ, critères d'inclusion, règle d'arrêt.

## 2. Données brutes de départ

Les classifications disciplinaires de revues et les codes de sujets des bases bibliographiques sont à éviter : elles figent le niveau « domaine » que Lazar veut dépasser. Données brutes :

1. **Graphe de citations complet** au niveau article, horodaté (OpenAlex ; SUPPOSÉ pour la couverture actuelle) : références brutes, pas catégories calculées.
2. **Sections de méthode** en texte intégral (arXiv, bioRxiv, PubMed Central) : la chapelle se lit dans l'instrument, l'échelle et le formalisme plus que dans le résumé.
3. **Co-signatures et affiliations**, pour les communautés d'auteurs (ce qu'utilisent Sourati et Evans 2023, *Nature Human Behaviour*, vérifiée (existence)).
4. **Traces de rencontre** : programmes de conférences, comités éditoriaux ; données rarement exploitées et directement liées à « ne se parlent pas ».
5. **Formules** extraites du LaTeX d'arXiv, pour la couche « mêmes objets mathématiques ».
6. **Évaluations par les pairs ouvertes** (OpenReview, eLife ; SUPPOSÉ) : là où une chapelle refuse les prémisses de l'autre.
7. Pour l'historique : **sources primaires** (correspondances, actes d'époque) plutôt que récits secondaires de « révolution », déjà interprétés.

La coupure temporelle s'applique à ces données brutes, pas aux récits a posteriori.

## 3. Méthodes et outils spécifiques

**Définir une chapelle** : non pas une partition unique, mais une partition par couche, puis mesure de leur accord.

- Couche sociale : détection de communautés sur co-signature et citation (Leiden ; Traag et collègues 2019, SUPPOSÉ), stabilité testée par rééchantillonnage.
- Couche lexicale : modèles de sujets (Blei et collègues 2003, SUPPOSÉ) ou plongements ; une chapelle est un sujet dont les termes sont **absents** des documents voisins.
- Couche méthodologique : extraction des **instruments, échelles et formalismes** déclarés dans les méthodes.
- Couche des prémisses, la plus dure : extraire les énoncés tenus pour acquis (« il est bien établi que… », hypothèses non citées) ; prémisses incompatibles quand l'acquis de l'une est la controverse de l'autre.
- Couche structurale : comparaison de graphes d'équations ou de signatures de modèles ; isomorphisme partiel, pas similarité de mots.

**Définir la distance** : candidats à confronter à l'étalon de la section 1.

- Distance de citation (plus court chemin, temps de diffusion), asymétrique si l'on distingue A cite B de B cite A.
- Divergences entre distributions de références ou de vocabulaire (Kullback-Leibler, Jensen-Shannon).
- Transport optimal (Wasserstein) entre nuages de plongements, qui respecte la structure interne des groupes.
- La règle « loin en domaine, proche en concept » devient un **vecteur de distances par couche** ; niche prometteuse = **grande distance sociale et lexicale, faible distance structurale ou méthodologique**, soit exactement « mêmes objets mathématiques sans s'en rendre compte ». Shi et Evans 2023, *Nature Communications*, vérifiée (existence), séparent déjà contenus et contextes ; Uzzi et collègues 2013 (*Science*, SUPPOSÉ) mesurent l'atypicité par paires de revues co-citées. Le programme doit se situer par rapport à ces deux mesures.

**Outils** : déchargements OpenAlex ; igraph, networkx, leidenalg ; POT pour le transport optimal ; extraction de LaTeX ; un modèle de langage comme extracteur de prémisses, **jamais comme juge de la distance** (il réintroduirait le découpage disciplinaire appris).

**Revue historique** : revue systématique bornée (critères d'inclusion écrits avant la recherche, journal des exclusions) sur trois corpus : philosophie et sociologie des sciences (Fleck, Kuhn, Lakatos, Galison 1997 sur les « zones d'échange » ; SUPPOSÉ), psychologie de la créativité (Koestler 1964 pour la bisociation, Simonton ; SUPPOSÉ), science de la science (Fortunato 2018, Wang et Barabási 2021 ; SUPPOSÉ). Livrable : un **inventaire de mécanismes** (migration d'un chercheur, importation d'un instrument, analogie formelle, controverse forcée), chacun traduisible en règle de choix de paires.

## 4. Ce qui, hors de nous, vérifierait le résultat

1. **Rétrodiction historique sous coupure temporelle** : à une date T, la mesure classe des paires de chapelles ; on vérifie, sur les données postérieures à T, si les paires que la mesure déclare « loin socialement, proches structuralement » ont produit plus de ponts (articles citant les deux, auteurs migrant) que les paires témoins. Le critère est fixé avant la lecture.
2. **Accord avec des experts du domaine** étiquetant à l'aveugle des paires de sous-domaines (cosmologie, neurosciences) : accord mesuré par une statistique d'accord inter-juges, sur un échantillon non vu pendant la construction.
3. **Reproduction indépendante** sur un autre jeu de données (Semantic Scholar contre OpenAlex, SUPPOSÉ pour l'accès) et sur un autre champ, avec code et graines publiés.
4. **Comparaison contre les mesures publiées** (Sourati et Evans 2023 ; Shi et Evans 2023 ; Uzzi 2013) : la nouvelle distance doit prédire quelque chose qu'elles ne prédisent pas, sinon elle n'apporte rien.
5. **Témoins négatifs et artefacts** : paires construites artificiellement proches ou lointaines, pour vérifier que la mesure ne répond pas à la taille des groupes ou à l'âge des articles.

## Reformulation de la demande

« Construire et tester une définition opérationnelle des chapelles scientifiques et une mesure de leur éloignement, en remplacement de la distance entre domaines.

1. Produire, avant toute mesure, un étalon : au moins trente paires de sous-domaines (cosmologie, neurosciences, un troisième champ témoin), étiquetées par des personnes du domaine sur quatre relations distinctes, non-citation mutuelle, vocabulaires disjoints, objets ou échelles disjoints, prémisses incompatibles, et dix paires de sous-domaines qui communiquent bien.
2. À partir des données brutes (graphe de citations horodaté, textes de méthodes, co-signatures, programmes de conférences, formules extraites), calculer pour chaque paire un vecteur de distances par couche : sociale, lexicale, méthodologique, de prémisses, structurale. Retenir les mesures asymétriques là où la relation l'est.
3. Formaliser la règle "loin en domaine, proche en concept" comme une condition sur ce vecteur, et la situer explicitement par rapport à Sourati et Evans 2023, Shi et Evans 2023 et Uzzi 2013.
4. Préenregistrer, puis tester par rétrodiction sous coupure temporelle, si les paires sélectionnées par cette condition produisent plus de ponts ultérieurs que des paires témoins ; critère d'accord avec l'étalon fixé à l'avance ; artefacts de taille et d'âge contrôlés.
5. En parallèle et séparément, mener une revue bornée (critères d'inclusion écrits avant la recherche) de la littérature sur la genèse des idées et des révolutions scientifiques, dans trois corpus (philosophie et sociologie des sciences, psychologie de la créativité, science de la science), avec pour livrable un inventaire de mécanismes de rapprochement entre chapelles, chacun traduit en règle candidate pour le bisociateur, chaque référence vérifiée sur document empreinté avant citation. »

Réserve finale : le point le plus fragile est la couche des prémisses ; si elle ne peut être extraite de façon reproductible, le programme doit le dire et s'en tenir aux quatre autres couches plutôt que de la remplacer par un jugement de modèle de langage.
