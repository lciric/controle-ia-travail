# Mesurer, éprouver, réfuter : que manque-t-il au dossier ?

Les faits sont joints en annexe. Cette question les complète. Elle porte sur deux choses liées : la mesure d'un système qui chercherait des idées « étroites et profondes », et les propositions restées en suspens après un premier tour de conception et de critique sur ces faits.

Rien de ce qui suit n'a été mesuré. Tout ce qui est rapporté comme « ayant résisté » a seulement résisté à des arguments. Les seuils, effectifs et coûts avancés au premier tour étaient illustratifs. Aucune proposition du dossier n'est tenue pour la bonne : vous pouvez les attaquer toutes.

## 1. Ce qu'on vous demande

Un petit nombre de propositions réfutables, complètes, qui portent sur ce qui manque au dossier. Pas de simples variantes de ce qui est retenu (section 3) ou réfuté (section 4), sauf si vous montrez qu'elles corrigent un défaut précis.

Vous pouvez aussi répondre qu'un point est mal posé, que la cible est mal définie, qu'aucun instrument de ce genre n'est faisable, ou proposer un point absent de la liste. Ces réponses comptent autant qu'une proposition, si elles sont argumentées.

## 2. Le contexte de la mesure

On envisage un système où plusieurs agents fondés sur des modèles de langue proposent, critiquent et sélectionnent des idées scientifiques candidates : hypothèses, lois quantitatives, lemmes, protocoles. Avant de le faire tourner, on veut construire et valider un instrument de mesure. Vous pouvez soutenir que l'ordre inverse est préférable : faire tourner d'abord le système à petit coût, puis instrumenter.

Cet instrument devrait permettre de montrer, ou de réfuter, que le système trouve des idées « étroites et profondes » : rarement atteintes par une recherche ordinaire, mais de grande conséquence une fois trouvées.

Bases de comparaison envisagées, sans hiérarchie entre elles :
- un tirage au hasard dans le même espace d'idées candidates ;
- un énumérateur mécanique ;
- le meilleur modèle unique, à budget égal ;
- toute autre base que vous jugeriez nécessaire.

## 3. État du dossier : ce qui a résisté, et ce qui reste à reprendre

Ces propositions viennent d'un premier tour de conception sous deux cadrages, de critique croisée et de réponses aux critiques.

### 3.1 Propositions qui ont résisté aux critiques du premier tour

Chacune est donnée avec ce qui a été argué et ce qui reste ouvert. Les réparations « jamais critiquées » ne sont pas pour autant validées.

**a. Banc de validité d'un détecteur séquentiel, en simulation sur processeur seul.** Le détecteur doit repérer un écart faible et dilué sur une longue suite d'observations, avec un taux de faux positifs garanti à tout instant d'arrêt. Il s'étalonne sur une référence finie supposée saine, peut-être contaminée dans une fraction inconnue.
- Défaut établi indépendamment sous les deux cadrages (argument et calcul, non mesure) : une référence finie gelée rend les facteurs d'évidence dépendants. Leur produit n'est alors plus une surmartingale, même sans contamination.
- Réparations convergentes du dernier tour, jamais critiquées depuis : l'épisode comme unité échangeable ; une enveloppe uniforme sur la fonction de répartition par l'inégalité de Dvoretzky-Kiefer-Wolfowitz ; un budget d'erreur partagé entre l'étalonnage et l'arrêt.
- Contrôle de banc proposé : la construction naïve (référence gelée, aucune contamination, horizon très supérieur à la taille n de la référence) doit échouer. Si elle n'échoue pas, le banc est défectueux.
- Grille proposée : contamination basse, haute et ciblée ; contamination réelle double de la contamination déclarée ; dérive bénigne graduée ; autocorrélation.
- Base proposée : somme cumulée écrêtée au même rayon, sur le même score et la même référence.
- Ouvert : la pente de la frontière d'identifiabilité. Deux formes sont en balance, ε ou σ₀√ε, où ε est la fraction contaminée de la référence et σ₀ l'écart type du score honnête. Ouvert aussi : ce qu'un processus d'évidence doit battre, à horizon fixe ou sous arrêt optionnel.

**b. Démarcation d'un corpus contre des nuls topologiques et fréquentiels emboîtés, avant tout usage de « connaissance latente ».**
- Proposé : le dénominateur complet des paires candidates à la date t ; des nuls emboîtés (fréquences, degrés, blocs estimés sur le passé seul, dates de disponibilité des instruments) ; des comparateurs à plusieurs sauts (indice de Katz, PageRank personnalisé, décomposition spectrale) et des coordonnées aléatoires de même dimension ; des coupures placebo ; un rééchantillonnage par nœuds.
- Contrôle du contrôle proposé : un monde où l'information est plantée dans les seules fenêtres de phrase.
- Ouvert : quel emboîtement de nuls suffit, et dans quel ordre.

**c. Fausse identité jugée sur monde planté, par un évaluateur externe aveugle au score.**
- Argument retenu : le texte seul ne suffit pas. Une fausse identité et un concept unique controversé ont la même loi sur les paires (contexte, prédicat).
- Classes négatives à inclure : vraies identités sous biais d'instrument, ou à ordres d'approximation différents ; concepts uniques à variable de régime, lois à plusieurs variables ou rétroactions ; controverse sur un concept unique ; identités promues en principe ; polysémie dans un même domaine ; homonymes.
- Scores candidats à départager, sans préférence établie : tension ordinale ; frustration conditionnée aux covariables ; co-invocation et tension entre documents.
- La dizaine de cas historiques est déclarée non jugeable d'avance.

**d. Règles de forme pour toute épreuve.** Une statistique, un seuil, deux hypothèses complémentaires sur le même dispositif. Effectif fixé par analyse de puissance, « non exécutable » déclaré d'avance. Nul d'une statistique maximisée recalculé en refaisant la maximisation. Comparateur de même capacité et de même budget de requêtes. Unité indépendante explicite. Extracteurs et taxonomies figés avant la coupure. Amputation placebo et réécriture hétérogène pour toute redécouverte de primitive. Seuils fixés sur des générateurs disjoints de ceux de l'épreuve. Lot d'étalonnage distinct du lot jugé.

**e. Frontière proposée (argument, non expérience) : copies d'un même modèle et audit d'une seule copie.** Sous l'hypothèse « mêmes poids, contextes indépendants, sans aléa partagé », la loi jointe des copies se factorise. Une statistique de paire n'apporte alors rien au-delà de l'audit d'une seule copie. Tout test comportemental sur un groupe de copies exigerait des permutations indépendantes de l'ordre et des étiquettes des options, et un étalonnage sur des clones honnêtes de mêmes poids.
- Ouvert : ce qui réfuterait cette réduction (quel aléa partagé, quel canal).

### 3.2 À reprendre ensuite (non tranché, plus coûteux)

- Primitives hors de l'alphabet existant : banc sous réécriture algébrique, anonymisation, cônes de dépendance disjoints, comparateur d'anti-unification à variables liées, grammaire probabiliste bien typée comme nul. Personne ne sait encore construire un contrôle réel bien typé sans redondance.
- Définitions d'une bibliothèque formelle non préfigurées dans son passé, si le nombre de positifs, compté avant tout prédicteur, suffit.
- Borne sur la robustesse d'un détecteur appris : réseau témoin disposant d'un canal libre orthogonal. La marge mesurée contre une famille d'attaques n'est qu'une borne supérieure.
- Transfert d'échelle sur une famille de modèles ouverts à corpus daté, après vérification de la date de fin du corpus.
- Percolation comme outil de réfutation seulement, contre un nul auto-excité à blocs et à croissance exogène.
- Audit spectral des poids sur des cohortes d'adaptateurs de même rang et de même budget : jugeable sur petits modèles, déclaré non jugeable sur de grands modèles quand la fraction d'adaptateurs altérés est faible.

## 4. Constructions réfutées : ne pas les reproposer, ni leurs variantes

- Surmartingale écrêtée des plus hauts scores : anticonservatrice.
- Correction statique du seuil α − k/(n+1) : ne protège pas un processus d'évidence.
- Boule de contamination en variation totale centrée sur la loi empirique : vide.
- Troncature basse de la moyenne de référence : sens inversé.
- Test de la corde : ne sépare pas le continu du discret.
- Laplacien de faisceau lu comme premier groupe de cohomologie ; sous-ensemble booléen insatisfaisable comme critère : mal posés.
- Critère de non-polysémie « pour toute partition » : vide.
- Repondération des mentions ; invariance entre genres par divergence de Jensen-Shannon : n'identifient pas le biais de déclaration.
- Signaux d'épicycles par dérivée de longueur de description : confondus avec l'extension du domaine.
- Spectres « invariants de jauge » du produit des matrices de requête et de clé d'une couche d'attention : faux sous reparamétrisations non orthogonales.
- Contrefactuel « d'autres copies existent » : non identifiable.
- Toute épreuve de marge où seule une sonde linéaire est attaquée : une rotation orthogonale l'élude.
- Banc sur bibliothèque formelle conditionné aux preuves refactorisées plus tard : fuite du futur.
- Jeux publics d'intérêt d'experts comme cible de rétrodiction ; analyseurs syntaxiques modernes sur archives anciennes ; taxonomies de concepts non millésimées : fuites.
- Théorèmes d'incomplétude et d'indécidabilité comme frontières : hors sujet pour des extensions définitionnelles et des circuits finis.

Si vous pensez qu'une de ces réfutations est elle-même fausse, dites-le et montrez pourquoi. Ne reproposez pas la construction sans cette démonstration.

## 5. Les points prioritaires

Sans ordre imposé. Vous n'êtes pas tenus de les traiter tous.

1. **Le détecteur séquentiel.** Les trois réparations jamais critiquées tiennent-elles ? La pente de la frontière d'identifiabilité est-elle en ε, en σ₀√ε, ou autre ? Que doit battre un processus d'évidence : une base à horizon fixe, une base sous arrêt optionnel, autre chose ?
2. **Les nuls emboîtés.** Lesquels démarquent vraiment un corpus de sa « connaissance latente », et lesquels manquent ou sont superflus ?
3. **La fausse identité sur monde planté.** Quelles classes négatives séparent la scission d'un concept faussement unifié de la promotion d'une égalité en principe ? Lesquelles manquent à la liste ?
4. **Les copies d'un même modèle.** Quel résultat réfuterait la réduction, à mêmes poids et sans aléa partagé, à l'audit d'une seule copie ? Quel aléa partagé, quel canal la briserait ?
5. **L'étroitesse et la profondeur.** Comment les mesurer, avec ou sans juge génératif ? Vous pouvez soutenir qu'un juge génératif étalonné est le meilleur instrument disponible ; dites alors comment le valider hors de lui-même. Si c'est impossible, dites-le, et dites à quelles conditions un juge (génératif, humain ou formel) deviendrait admissible et comment borner son biais. Comment écarter leurs leurres : l'« aiguille stérile », le « faux profond », la « mère générique » ? Les noms de ces leurres sont indicatifs : les définir fait partie de la question.
6. **La recherche d'une correspondance étroite entre deux voisinages conceptuels près d'un leurre large de même masse.** Méthodes citées au premier tour, aucune éprouvée : énumération, programme exact en nombres entiers, signatures de rôle, transport régularisé, appariement du grossier au fin, recuit. Aucune n'est présumée meilleure. Laquelle, ou quelle autre, et comment la départager des autres ?
7. **Les sélecteurs de lieux** (où chercher). Comment les éprouver comme prévisions, contre un tirage au hasard et contre des bases simples ?

## 6. Huit questions sur la mesure elle-même

Elles détaillent les points 5 et 7, mais valent pour tout le dossier.

1. **Cible.** Comment définir « étroite » et « profonde » de façon opératoire, avec ou sans juge (génératif, humain, formel) ? Si vous en employez un, comment bornez-vous son biais, en particulier le recoupement de ses préférences avec celles du générateur ? Par rapport à quelle référence mesurer l'étroitesse ? Comment distinguer la profondeur de la seule rareté ?
2. **Sources de vérité.** Comparez les sources candidates : mondes synthétiques à vérité plantée, rétrodiction avec coupure temporelle, preuve formelle, tests exécutables, jugement d'experts humains en aveugle, conséquence observée après coup, ou autres. Pour chacune : ce qu'elle peut établir sur l'étroitesse et la profondeur, ce qu'elle ne peut pas établir, et comment elle échoue. Aucune n'est présumée suffisante.
3. **Comparaison.** Quelle quantité principale, quelle unité d'analyse, quelle comptabilité des coûts, quelle règle de décision soutiendraient ou réfuteraient « mieux que les bases » ? Quelles comparaisons supplémentaires, s'il en faut, permettraient d'attribuer une différence à une partie précise du système ?
4. **Choix des problèmes.** Comment choisir des problèmes ou des régions où ces idées seraient plus probables, si de telles régions existent ? Comment éprouver ce choix au lieu de le supposer ?
5. **Retour pendant la recherche.** Quelles mesures peuvent, le cas échéant, être rendues au générateur pendant la recherche ? Lesquelles doivent lui être cachées pour que l'instrument mesure encore ce qu'il dit mesurer ?
6. **Validation de l'instrument.** Que doit-il démontrer sur lui-même avant toute course coûteuse ?
7. **Plan.** Ordonnez les expériences de la moins chère à la plus chère, avec critères d'arrêt et effectifs requis.
8. **Limites.** Qu'est-ce qui est hors de portée de tout instrument de ce genre ? Envisagez explicitement qu'aucun ne soit faisable, ou que la cible soit mal posée. Dites quelle preuve montrerait l'un ou l'autre.

## 6 bis. Quatre questions brèves

Chacune appelle une réponse brève et une confiance entre 0 et 1. Elles sont indépendantes du dossier ; y répondre n'engage aucune position sur les sections 3 à 6.

1. Dans la méthode des tâches de contrôle pour juger les sondes de représentations (Hewitt et Liang, 2019, arXiv 1909.03368), comment est définie la sélectivité d'une sonde ? Donnez la définition en une phrase, et votre confiance entre 0 et 1.
2. On estime une fonction de répartition F par la fonction de répartition empirique F_n de n tirages indépendants de loi F. Avec l'inégalité de Dvoretzky-Kiefer-Wolfowitz à la constante de Massart, P(sup_x |F_n(x) − F(x)| > η) ≤ 2·exp(−2nη²), quel est le plus petit entier n qui garantit un écart uniforme d'au plus η = 0,05 avec une probabilité d'au moins 0,99 ? Donnez la réponse et votre confiance entre 0 et 1.
3. Le jeu de test d'analogies sémantiques et syntaxiques introduit avec les architectures CBOW et skip-gram (Mikolov et al., 2013, arXiv 1301.3781) compte combien de questions sémantiques, et combien de questions syntaxiques ? Donnez la réponse (deux nombres) et votre confiance entre 0 et 1.
4. Sur 300 essais indépendants, aucun succès n'est observé. Quelle est la borne supérieure de l'intervalle de confiance exact bilatéral de Clopper-Pearson à 95 % pour la probabilité de succès (quatre chiffres significatifs) ? Donnez la réponse et votre confiance entre 0 et 1.

## 7. Forme imposée de chaque proposition

Chaque proposition donne, dans cet ordre :
- l'idée en deux phrases ;
- le verrou ou le mécanisme qu'elle sert (dans l'annexe ou dans les sections 3 à 6) ;
- ce qu'elle suppose ;
- une statistique, un seuil et deux hypothèses complémentaires, ou, si vous jugez le test d'hypothèse inadapté, une autre règle de décision écrite d'avance (estimation avec intervalle, facteur de Bayes, coût attendu) et son critère d'échec ;
- son test de mort, écrit avant toute exécution : quel résultat la tue ;
- son contrôle négatif apparié, adapté à la source de vérité choisie (par exemple : pour un corpus, permutation préservant fréquences et degrés ou recâblage à degrés et types constants ; pour un monde synthétique, le même monde sans la structure ; pour des experts en aveugle, des items leurres appariés ; pour une rétrodiction, une coupure placebo ; pour un test exécutable, une mutation neutre) ;
- son contrôle positif, adapté de même (par exemple : monde synthétique avec la structure, cas connu du corpus, item dont la réponse est établie, énoncé déjà prouvé, test dont l'issue est connue) ;
- son coût sur processeur seul d'abord, et ce qui exigerait plus tard une carte graphique ;
- l'effectif requis, ou « non exécutable » ;
- les antériorités connues et celles à chercher : auteurs, année, lieu de publication ou identifiant arXiv, page ou section si possible ;
- le statut de chaque énoncé : argument, calcul ou mesure ;
- une confiance entre 0 et 1.

Les questions brèves de la section 6 bis appellent une réponse brève et une confiance entre 0 et 1, sans la forme ci-dessus.

Séparez ce qui est établi de ce qui est conjecture. Dites où le cadrage vous paraît faux.

Une réponse qui conteste un point au lieu de proposer suit une forme allégée : l'objection en deux phrases ; ce qu'elle suppose ; ce qui la réfuterait ; les références ; une confiance entre 0 et 1.

## 8. Comment les propositions seront éprouvées

- Un banc d'exécution jouera, sur processeur seul et sur des mondes à graine, les propositions exécutables. Il passera d'abord un contrôle de banc qui doit échouer.
- Un étage de réfutation cherchera à tuer chaque proposition. Il applique la même procédure à toutes les propositions.
- Aucun résultat d'épreuve ne vous sera rendu.
- Aucune note d'un juge génératif n'entre dans le choix des propositions. Aucun juge génératif ne valide une découverte.
- Une épreuve interrompue pour cause technique ne compte ni pour ni contre une proposition.

## 9. Hors de portée de ce tour

À ne pas revendiquer :
- montrer que le système trouve des idées étroites et profondes mieux que le hasard : l'instrument qui le mesurerait n'est pas validé ;
- valider quoi que ce soit sur des modèles réels ;
- rétrodire ;
- prouver formellement ;
- dire « neuf » sans recherche d'antériorité.

Vous pouvez analyser la rétrodiction et la preuve formelle comme sources de vérité (question 2 de la section 6). Vous ne pouvez pas en rapporter un résultat.

Survivre aux épreuves voudra dire « éprouvable et pas encore tué », non « découverte ».

## 10. En résumé

Proposez peu, complet et réfutable. Visez ce qui manque, pas ce qui est retenu ou réfuté. Répondez à chacune des huit questions de mesure, au moins brièvement (une réponse argumentée « mal posé » compte), et aux points prioritaires que vous jugez les plus utiles. Dites librement qu'un point est mal posé, que la cible l'est, qu'aucun instrument n'est faisable, ou qu'un point manque. Pour chaque énoncé, donnez son statut, sa confiance et ses références.
