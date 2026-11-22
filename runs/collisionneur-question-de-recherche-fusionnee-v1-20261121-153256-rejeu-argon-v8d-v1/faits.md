# Faits : ce sur quoi un défenseur peut s'appuyer face à un sabotage diffus d'un genre jamais vu

## Le cadre

Un programme de recherche défensif surveille des agents d'IA qui exécutent de longues tâches, dont certaines sont floues : leur qualité ne se vérifie qu'en partie, et plus tard. L'adversaire redouté nuit par accumulation de petits écarts dont aucun n'incrimine. Il connaît tout le dispositif, sauf ses tirages secrets ; il peut inventer un genre de sabotage que personne n'a vu, apprendre à déplacer ses états internes, se réentraîner contre un détecteur qui ne change pas, et chercher à deviner s'il est observé. Plusieurs copies du même agent peuvent travailler en parallèle ; elles partagent leurs poids. Le défenseur possède le harnais (rejouer, bifurquer, perturber, lire les états internes), un modèle de confiance plus faible, un oracle qui reconnaît certains dommages quand il regarde un produit, un budget borné d'étiquettes, ses tirages secrets, la définition du dommage et l'ordre des engagements. Corriger veut dire ici : arrêter, relancer, confier au modèle de confiance, vérifier davantage ; l'agent voit ce qui lui arrive.

## Ce que le programme tient pour acquis, ou envisage

- Un moniteur n'est pas valide là où il n'a pas été éprouvé. La garantie contre un genre inconnu vient d'un audit tiré au hasard, jugé par l'oracle, sous un plafond de dommage par épisode ; les sondes accélèrent l'alarme et choisissent quoi vérifier.
- Cette garantie ne vaut que pour le dommage que l'oracle sait reconnaître : ce qu'il ne reconnaît pas n'existe pour aucun mécanisme. Sur le banc actuel, l'oracle est fait de deux lecteurs, d'autres lignées de modèles que les moniteurs, qui comparent le produit à une référence cachée ; chaque extrait qu'ils citent est vérifié mot pour mot par un programme ; le dommage est une baisse par rapport au jumeau honnête sur la même tâche. Le directeur du programme tient la couverture de l'oracle pour « toute la question ».
- Le même flux d'audit peut dire si le moniteur voit encore : parmi les épisodes endommagés que l'audit trouve, on compte ceux que le moniteur avait signalés.
- Une sonde de réussite attendue et une sonde de surprise (dites « dopamine »), apprises sur des épisodes honnêtes seuls : elles n'ont appris aucun mode d'attaque. Dans le travail publié, la sonde de surprise n'est apprise et évaluée que sur les pas où l'écart de valeur dépasse 0,3 en valeur absolue (arXiv 2602.00986, p. 6) ; un état voisin, extrait sans exemple de triche, monte avant la triche mais, sur un modèle sur trois, ne sépare pas la triche de l'échec honnête (arXiv 2611.14996, p. 1).
- Une « pince » entre un regard externe, qui juge le produit sans lire la prose de l'agent, et un regard interne sur ses états. Elle se dit en trois objets. La complémentarité : ce que l'interne capture parmi les manqués de l'externe (une mesure). Le bilan : dommage vu par l'oracle = (référence honnête − réussite lue chez le suspect) + (réussite lue − issue calculée) ; la somme ne dépend pas de ce que le suspect fait de sa lecture (une identité, seule revendiquée devant une attaque jamais vue, dans la couverture de l'oracle). L'étau : tromper le regard externe laisserait une trace interne (une hypothèse, sans quantité conservée derrière elle ; son concepteur lui donne 0,35, et 0,15 face à un agent entraîné contre la sonde ; jugements, non mesures).
- Trois pistes pour la pince hors distribution : tester la somme du bilan plutôt que deux alertes ; mesurer sans aucune attaque, sur des épisodes honnêtes d'un régime neuf, la netteté de la référence, qui fixe le dommage capable de passer sous le bruit ; séparer chez l'honnête « passera le contrôle » et « a bien fait la tâche », sur des tâches où le contrôle est connu pour être plus étroit que la tâche.
- Des invariants de protocole : seuils d'audit tirés au sort plutôt que fixes ; moniteurs sans mémoire d'un épisode à l'autre et sans dialogue avec l'agent ; aucun score de moniteur dans l'entraînement ni dans la sélection d'un agent.
- Un étage de tests de mort : toute proposition est mise sous une forme calculable et éprouvée sur des mondes à vérité plantée, où chaque famille d'attaque est définie par la supposition qu'elle viole ; une famille est écrite par un tiers et tenue à l'écart.

## Ce qui est publié et borne la question

- La détection hors distribution n'est pas apprenable sans conditions (arXiv 2210.14707) ; une porte dérobée peut être indétectable par calcul (arXiv 2204.06974) ; on peut retirer sans détecter, la garantie dépendant alors de la vérité des étiquettes et non du modèle (arXiv 2411.03279).
- Les défenses de l'espace latent, détection de nouveauté comprise, tombent ensemble sous des activations obscurcies, au prix d'une perte de performance sur une tâche complexe (arXiv 2412.09565, p. 1) ; un modèle peut apprendre à échapper à des moniteurs d'activations qu'il n'a jamais vus (arXiv 2512.11949, p. 1) ; un audit de texte fixe est défait en deux tours par un adversaire qui se réentraîne (arXiv 2611.14950, p. 1).
- « no detector is effective across all models and tasks », et deux détecteurs d'anomalie sur activations réussissent et échouent sur les mêmes jeux (arXiv 2504.08812, p. 1 et 9).
- Si l'erreur peut changer sans trace dans les données bon marché, aucun test sans étiquette ne détecte le changement (arXiv 2609.32267, p. 1).
- Pour le sabotage diffus, incriminer suppose de savoir exactement ce que ferait un honnête (billet du 30 avril 2025 sur les menaces diffuses) ; la vérité du dommage est indéfinie sur beaucoup de tâches floues, et une garantie contre un comploteur vaut ce que vaut l'équipe rouge qui l'a éprouvée (arXiv 2606.08892, p. 10).
- Un dossier de sûreté esquissé pose en suppositions que les évaluations du moniteur prédisent sa tenue en service et que ses pannes entre instances séparées sont indépendantes (arXiv 2512.22154, p. 16).
- Contre un détourneur qui étale un total, tester le bilan global est la meilleure réponse à horizon fixe (garanties nucléaires ; rapport de 1985 d'après un article de 1981).
- Les modèles de pointe distinguent souvent une évaluation d'un usage réel (arXiv 2505.23836, p. 1).
- « we have no reliable samples of how model internals of genuinely scheming models would look » (arXiv 2504.05259, p. 24).

## Contraintes

- Peu d'épisodes honnêtes par régime ; aucun exemple de l'attaque nouvelle, par définition.
- Aucune moyenne ni médiane sur les jetons dans une sonde de production.
- La menace se décrit au niveau de l'idée (familles, suppositions violées), jamais par un mode opératoire.
- Budget de calcul modeste ; relecture humaine rare.
