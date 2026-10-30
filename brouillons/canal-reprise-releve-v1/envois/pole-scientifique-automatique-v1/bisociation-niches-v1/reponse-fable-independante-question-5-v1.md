# Réponse indépendante — question 5 : identifier par apprentissage profond les paramètres qui *créent* la fertilité — v1

- Répondant : sous-agent neuf et indépendant (n'a lu que `question-5-causes-v1.md` et, pour le contexte, les questions 1 à 4 ; aucune réponse, relecture ni revue lue ; rien lu sous `donnees/`).
- Modèle : Claude Fable 5.1 (`claude-fable-5-1`).
- Date : 2026-10-30 17:20 UTC (`date -u`).
- Statut : niveau méthode ; aucune décision prise. Références : « vérifiée (existence) » = titre et lieu de publication retrouvés par recherche web ce jour, contenu non vérifié sur PDF empreinté (R7 : aucun chiffre opposable) ; « SUPPOSÉ » = citée de mémoire.

## Verdict court

Oui, à une condition qui n'est pas d'apprentissage profond : un réseau peut *estimer* des effets causaux, il ne peut pas *fournir* ce qui les identifie. Sans intervention, expérience naturelle ou hypothèse d'invariance explicite, le modèle le plus profond apprend les paramètres qui accompagnent la fertilité (sélection, mode, prestige, survivants), jamais ceux qui la créent. La question « peut-on ? » devient donc « quelle source de variation exogène possédons-nous ? » ; l'apprentissage profond intervient ensuite, pour absorber les variables de confusion à haute dimension (texte, réseau) et estimer des effets hétérogènes et non linéaires — ce qui est précisément la forme d'une « transition de phase ».

## (1) Ce qu'un expert ferait, et que la question ne demande pas

1. **Écrire l'estimande avant le modèle** : le « traitement » (mettre deux niches en présence : comment, à quelle dose, à quelle date), l'« unité » (paire de niches, chercheur, papier), le « résultat » (fertilité, définie en question 3, mesurée sans savoir si la paire a réussi), la quantité visée (effet moyen, effet au seuil, dose-réponse). Sans cela, « les paramètres qui créent » n'est pas estimable.
2. **Dessiner le graphe causal et nommer les confondeurs**, observés (prestige, financement, mode, proximité, langue) et *non observés* : ce sont eux qui décident la stratégie d'identification, pas la taille du modèle.
3. **Traiter l'interférence** : un pont entre A et B change C ; l'hypothèse d'unités indépendantes (SUPPOSÉ : Rubin) est violée ; estimateurs sous interférence de réseau (SUPPOSÉ : Aronow et Samii 2017 ; Hudgens et Halloran 2008).
4. **Distinguer trois sens de « peut-on »** : (a) effet d'un paramètre manipulable — oui, si variation exogène ; (b) structure causale entre paramètres — seulement jusqu'à une classe d'équivalence ; (c) paramètres latents « qui créent » appris de bout en bout — apprentissage de représentations causales, avec résultats d'impossibilité sans interventions ni environnements multiples (Schölkopf et al. 2021, « Toward causal representation learning », vérifiée (existence)).
5. **Mesurer la fertilité par un canal que le traitement ne touche pas autrement** : des citations futures sont aussi causées par la visibilité des auteurs ; préférer, par exemple, la réutilisation d'un objet mathématique précis dans une troisième niche.
6. **Analyse de sensibilité** à la confusion non mesurée (SUPPOSÉ : bornes de Rosenbaum ; « E-value », VanderWeele et Ding 2017), publiée avec l'estimation.
7. **Contrôle négatif** : un résultat que le traitement ne peut pas causer (fertilité *antérieure* à la rencontre) ; un effet trouvé là mesure la sélection.

## (2) Données brutes qu'il prendrait au départ

Pas les distances déjà calculées (Sourati-Evans, cité en question 1), ni les scores de nouveauté déjà agrégés, mais :

- **Trajectoires d'affiliation par auteur et par année** (OpenAlex ou Microsoft Academic Graph, données brutes auteur–institution–date), pour reconstruire les *déplacements* de chercheurs entre laboratoires et les *décès* ou départs forcés : le matériau des expériences naturelles.
- **Texte intégral et historique de versions** (arXiv, PubMed Central, bioRxiv) : le texte sert de proxy des confondeurs latents (ce qu'un auteur savait, suivait, imitait), condition pour que l'apprentissage profond serve à la causalité (SUPPOSÉ : Veitch, Sridhar, Blei 2020 ; Keith, Jensen, O'Connor 2020 « Text and causal inference »).
- **Programmes et listes de participants de conférences ou d'écoles d'été**, avec dates d'annulation, de déplacement ou de fusion de sessions (variation exogène de « mise en présence »).
- **Dossiers de financement avec score d'évaluation et seuil de financement** (NIH RePORTER, ERC, ANR si accessible) : permet une discontinuité de régression sur « projet interdisciplinaire financé de justesse ou refusé de justesse ».
- **Plans d'étage et déménagements de bâtiments universitaires** (Catalini 2018, « Microgeography and the direction of inventive activity », vérifiée (existence) : colocalisation quasi aléatoire après travaux).
- **Événements historiques datés** : mort prématurée de chercheurs centraux (Azoulay, Graff Zivin, Wang 2010, « Superstar Extinction », vérifiée (existence)) ; effondrement de l'URSS et arrivée de mathématiciens soviétiques (Borjas et Doran 2012, vérifiée (existence)) ; expulsions sous le nazisme (SUPPOSÉ : Waldinger 2010, 2012).
- **Journaux d'exécution de l'organisme lui-même** : chaque paire proposée, par quel proposeur, sous quel juge figé, à quelle date, avec le résultat du test de mort — données brutes d'une expérience *randomisable*, la seule dont nous contrôlons le mécanisme d'affectation.
- **Mondes inventés avec loi génératrice connue** (déjà dans le programme) : les seules données où « créer » a une vérité terrain.

## (3) Méthodes et outils

**A. Interventions (le seul « créer » sans hypothèse).**
- Expérience randomisée dans l'organisme : affecter au hasard les paires de niches entre bras (règle « loin en domaine, proche en concept » contre tirage aléatoire contre règle inverse), juges figés, fertilité mesurée par un juge *autre* que celui qui a servi à choisir. C'est un essai contrôlé dont le programme est propriétaire ; il isole l'effet de la *règle*, pas celui de la fertilité dans la science humaine.
- Expériences humaines de terrain : Boudreau et al. 2017, symposium où la proximité des participants est tirée au sort (« A Field Experiment on Search Costs and the Formation of Scientific Collaborations », *Review of Economics and Statistics*, vérifiée (existence)) ; expérience de laboratoire sur la connectivité partielle des groupes (Derex et Boyd 2016, *PNAS*, vérifiée (existence)). Les répliquer avec des niches réelles est coûteux mais faisable à petite échelle (une école d'été dont on randomise les binômes).

**B. Expériences naturelles (quasi-expériences).**
- Différences de différences et événements échelonnés (déménagements, décès, arrivées) avec estimateurs robustes à l'hétérogénéité des dates (SUPPOSÉ : Callaway et Sant'Anna 2021 ; de Chaisemartin et D'Haultfœuille 2020).
- Discontinuité de régression au seuil de financement ; discontinuité géographique (étage, bâtiment).
- Variables instrumentales : l'arrivée d'un chercheur d'une niche B dans un laboratoire de niche A, instrumentée par un choc extérieur (fermeture d'un institut, politique de visas).
- Appariement et contrôle synthétique (SUPPOSÉ : Abadie) pour les paires de niches « témoins » évoquées en question 4 : il faut des témoins *avant la date*, choisis par une règle gelée.
- Ce que l'apprentissage profond ajoute ici : **apprentissage automatique double et orthogonalisé** (Chernozhukov et al. 2018, *Econometrics Journal*, vérifiée (existence)) — le réseau prédit le traitement et le résultat à partir du texte et du réseau de citations, et l'effet est estimé sur les résidus, ce qui neutralise le surajustement ; **forêts causales** pour l'hétérogénéité de l'effet (SUPPOSÉ : Wager et Athey 2018) ; réseaux à deux têtes pour l'effet individuel sous confusion observée (SUPPOSÉ : TARNet, Shalit, Johansson, Sontag 2017 ; DragonNet, Shi, Blei, Veitch 2019). Ces outils estiment une **courbe dose-réponse** (effet en fonction de la distance ou de la densité de canal) ; une « transition de phase » y apparaît comme une non-linéarité à seuil, testable par un seuil préenregistré.

**C. Invariance (quand on n'a ni intervention ni choc).**
- Prédiction causale invariante (Peters, Bühlmann, Meinshausen 2016, *Journal of the Royal Statistical Society B*, vérifiée (existence)) : on découpe les données en « environnements » (disciplines, pays, décennies, régimes de publication) ; les paramètres dont la relation avec la fertilité reste la même dans tous les environnements sont candidats causaux ; les autres sont des accompagnateurs. Variantes profondes : SUPPOSÉ « Invariant Risk Minimization » (Arjovsky et al. 2019), avec des résultats négatifs connus quand les environnements sont trop semblables (SUPPOSÉ : Rosenfeld et al. 2021).
- Hypothèse à expliciter et à discuter : les mécanismes de confusion changent d'un environnement à l'autre, le mécanisme causal non. En science des sciences, cette hypothèse est fragile (les normes de citation changent par discipline *et* la fertilité aussi) ; l'expert la testerait par un environnement tenu à l'écart, choisi avant l'analyse.
- Découverte de structure (SUPPOSÉ : PC, FCI, NOTEARS) : utile pour proposer des hypothèses, jamais pour conclure ; sort une classe d'équivalence, pas un graphe.

**D. Régression symbolique ou petits traits nommés (les deux pistes de Lazar).** Elles produisent une *loi descriptive* lisible, pas une loi causale ; elles deviennent causales seulement si la loi est ajustée sur des données où la variation est exogène (A ou B) ou validée par invariance (C). Le bon protocole : apprendre la loi sur les données observationnelles, puis la *mettre à l'épreuve* sur les expériences naturelles (prédit-elle le sens et l'ordre de grandeur de l'effet d'un choc qu'elle n'a pas vu ?).

**Antériorités en science des sciences à relever** (toutes observationnelles sauf celles de A et B) : SUPPOSÉ Fortunato et al. 2018 (*Science*, revue de champ) ; Uzzi et al. 2013 et Wang, Veugelers, Stephan 2017 (nouveauté et citations) ; Rzhetsky, Foster, Evans 2015 (modèle de choix d'expériences, simulation) ; Jaffe, Trajtenberg, Henderson 1993 et la critique de Thompson et Fox-Kean 2005 (localisation des citations : exemple canonique d'un résultat qui change avec le groupe témoin) ; Myers 2020 (élasticité des sujets de recherche aux incitations). Point d'antériorité : la question « les ponts créent-ils ou accompagnent-ils ? » est ouverte dans cette littérature ; aucune des études citées ne randomise la *distance conceptuelle* elle-même.

## (4) Ce qui permettrait de vérifier, hors de Lazar et hors de nous

1. **Vérité terrain plantée** : dans les mondes inventés, planter un paramètre qui *cause* la fertilité et un paramètre qui *l'accompagne* (corrélé par un confondeur commun) ; l'estimateur doit retenir le premier et rejeter le second, avec taux d'erreur préenregistrés (R5 : testé sur un cas sain et sur un artefact).
2. **Tests placebo** : date de traitement fictive, résultat antérieur au traitement, niche jumelle non exposée ; un effet trouvé là est un échec, consigné.
3. **Recalibrage sur un résultat publié** : à partir des données brutes, retrouver le *signe* d'un effet connu (Azoulay 2010 ; Borjas-Doran 2012) ; si notre chaîne ne le retrouve pas, elle n'est pas prête.
4. **Prédiction hors environnement, scellée** : les paramètres déclarés causaux doivent prédire la fertilité dans un environnement (discipline, période) jamais vu, après la coupure temporelle déjà prévue dans le programme ; prédiction chiffrée et signée avant lecture (R1).
5. **Intervention prospective dans l'organisme** : si un paramètre est déclaré causal, le manipuler dans le bisociateur et observer la fertilité sous juge figé indépendant ; c'est la seule vérification qui ne dépend d'aucune hypothèse d'observation.
6. **Réanalyse indépendante** : données brutes, code et préenregistrement empreintés (R6), remis à un analyste extérieur qui applique le plan gelé ; convergence ou divergence consignée.
7. **Bornes de sensibilité publiées** : la force de confusion nécessaire pour annuler l'effet, comparée à celle des confondeurs mesurés.

## Reformulation de la demande

« Déterminer si l'apprentissage profond peut identifier les paramètres qui *créent* la fertilité d'un croisement entre niches, en séparant trois étapes : (i) définir l'estimande (unité, traitement, dose, résultat mesuré indépendamment du traitement, hypothèse d'interférence) et le graphe causal avec ses confondeurs observés et non observés ; (ii) inventorier les sources d'identification disponibles — interventions randomisées dans l'organisme et expériences humaines (Boudreau 2017, Derex-Boyd 2016), expériences naturelles datées sur données brutes d'affiliation, de conférences, de financement et de localisation (Azoulay 2010, Borjas-Doran 2012, Catalini 2018), hypothèses d'invariance entre environnements (Peters-Bühlmann-Meinshausen 2016) — et dire pour chacune quel paramètre elle permet d'identifier et à quel prix ; (iii) n'utiliser l'apprentissage profond que comme estimateur sous identification donnée (apprentissage double orthogonalisé, forêts causales, réseaux à deux têtes, prédiction invariante), avec courbe dose-réponse et seuil préenregistré pour la « transition de phase », les deux pistes « traits nommés puis ablation » et « régression symbolique » étant mises à l'épreuve sur les chocs exogènes qu'elles n'ont pas vus. Livrer : tableau estimande × source d'identification × estimateur × hypothèse à défendre ; revue d'antériorité en inférence causale et en science des sciences marquant ce qui est vérifié sur PDF ; protocole de validation en sept points (vérité plantée, placebos, recalibrage, prédiction hors environnement scellée, intervention prospective, réanalyse externe, bornes de sensibilité), avant tout calcul. »
