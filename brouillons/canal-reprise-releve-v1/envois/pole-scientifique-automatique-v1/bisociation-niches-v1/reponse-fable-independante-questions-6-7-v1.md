# Réponse indépendante aux questions 6 et 7 — v1

- Répondant : sous-agent neuf et indépendant (n'a lu que `question-1` à `question-7` ; aucune réponse, relecture, revue ni construction ; rien sous `donnees/`).
- Modèle : Claude Fable 5.1 (`claude-fable-5-1`).
- Date (`date -u`) : Fri Oct 30 22:34:51 UTC 2026.
- Niveau méthode ; aucune décision. Les références de mémoire sont marquées SUPPOSÉ ; deux recherches en ligne ont seulement confirmé l'existence de titres (marqué « titre vu »), jamais le contenu.

---

## Question 6 — l'apprentissage profond peut-il identifier à lui seul les paramètres qui créent la fertilité ?

### (1) Ce qu'un expert ferait et que la question ne demande pas

Un expert en apprentissage de représentations causales commencerait par séparer trois objets que la question fond en un seul : **estimer** (prédire la fertilité à partir de traits observés), **identifier une représentation** (retrouver, à une permutation et une renormalisation près, les variables latentes qui engendrent les données) et **identifier un effet causal** (dire ce que changerait la fertilité si l'on modifiait un paramètre). Les théorèmes d'identifiabilité répondent au deuxième objet ; la question de Lazar porte sur le troisième. Retrouver les latentes ne dit pas lesquelles sont causes de la fertilité : il faut encore un argument d'intervention ou d'invariance. L'expert écrirait donc d'abord le **graphe de génération supposé** (quelles variables latentes, quelles non-stationnarités, quel mécanisme de sélection des paires observées), puis demanderait quel théorème s'y applique, au lieu de partir de l'algorithme.

Il poserait aussi la question du **biais de sélection** : dans la littérature réelle, on n'observe que les croisements tentés, puis parmi eux ceux qui sont publiés, puis cités. Aucun théorème de démêlage n'est robuste à un échantillonnage dépendant de la sortie ; c'est le point que le non supervisé ne voit pas, car il n'a pas d'étiquette, mais le mécanisme de sélection déforme la distribution qu'il apprend.

### (2) Données brutes

- Pour les théorèmes : la liste des hypothèses exactes de chacun, recopiée du papier (pas d'un résumé), avec page.
- Pour les données scientométriques : graphe de citations horodaté au niveau du papier, avec affiliations, pays, langue, revue, dates de soumission et de publication ; textes intégraux ou résumés ; historique des affiliations des auteurs (déménagements) ; programmes de conférences (coprésence de niches). Toujours avant la date de coupure.
- Pour les courses de l'organisme automatique : le journal complet des affectations (quelle paire de fiches à quel proposeur, avec quelle dose de contact, par tirage de graine consignée), et non le seul résultat agrégé. C'est la seule source où l'affectation est **vraiment randomisée** ; tout le reste est observationnel.
- Mondes inventés : les paramètres générateurs stockés avec le run (manifeste, graines), scellés avant toute lecture de résultat (règle R1).

### (3) Méthodes et outils, avec les théorèmes et leurs hypothèses

(a) **Ce que disent les théorèmes.**
- Impossibilité de base : sans hypothèse inductive ni information auxiliaire, le démêlage non supervisé est non identifiable (Locatello et al., 2019, « Challenging common assumptions in the unsupervised learning of disentangled representations », SUPPOSÉ ; résultat de fond : Hyvärinen et Pajunen 1999 sur l'analyse en composantes indépendantes non linéaire, SUPPOSÉ). Tout ce qui suit est une façon d'acheter l'identifiabilité avec une hypothèse supplémentaire.
- Variable auxiliaire et non-stationnarité : analyse en composantes indépendantes non linéaire par contraste temporel (Hyvärinen et Morioka 2016, 2017, SUPPOSÉ) et auto-encodeur variationnel identifiable, iVAE (Khemakhem, Kingma, Monti, Hyvärinen 2020, « Variational autoencoders and nonlinear ICA: a unifying framework », SUPPOSÉ ; arXiv 1907.04809, titre vu). Hypothèses : les latentes sont conditionnellement indépendantes sachant une variable auxiliaire u (temps, segment, environnement) ; leur densité conditionnelle appartient à une famille exponentielle dont les paramètres naturels varient « assez » avec u (condition de rang : au moins 2k+1 valeurs distinctes de u pour k latentes, selon la version) ; le mélange est injectif. Résultat : identification à permutation et transformation élément par élément près.
- Parcimonie des mécanismes : Lachapelle et al. 2022, « Disentanglement via mechanism sparsity regularization » (titre vu) ; Zheng, Ng, Zhang 2022, « On the identifiability of nonlinear ICA: sparsity and beyond » (titre vu). Hypothèses : chaque intervention ou transition temporelle ne touche qu'un petit nombre de latentes, et le graphe de dépendance est suffisamment varié. Cadre général : « sparse mechanism shift » (Schölkopf et al. 2021, « Toward causal representation learning », SUPPOSÉ).
- Non-gaussianité et modèles linéaires : LiNGAM (Shimizu et al. 2006, SUPPOSÉ) identifie l'ordre causal si le modèle est linéaire, non gaussien et sans confusion cachée ; les extensions à variables latentes exigent des contraintes fortes (pureté des mesures, etc.).
- Séries temporelles : causalité au sens de Granger et modèles de transfert d'information ; identifiabilité de la direction sous hypothèses de bruit additif ou de non-stationnarité (Zhang, Hyvärinen, Schölkopf et al., SUPPOSÉ). Hypothèse décisive : pas de variable commune non observée et pas d'échantillonnage dépendant de la sortie.
- Apprentissage de représentations causales avec interventions : identification des latentes et de leur graphe quand on dispose d'interventions sur des latentes individuelles, parfois une seule par latente (von Kügelgen et al. 2023, SUPPOSÉ ; Squires et al. 2023, SUPPOSÉ ; Buchholz et al. 2023, SUPPOSÉ). Hypothèse : les interventions sont **sur les latentes**, pas sur les observations, et l'on sait quelles données viennent de quel régime.

Bilan théorique : il n'existe aucun théorème où l'identification des **causes** sort du seul non supervisé. Chaque résultat suppose une source exogène de variation (étiquette de régime, intervention, temps) et des hypothèses structurelles (indépendance conditionnelle, parcimonie, famille de distribution). Le non supervisé est un **amplificateur** : il transforme une information d'identification faible mais exogène en une représentation complète, il ne la crée pas.

(b) **Hypothèses satisfaites « gratuitement » par nos données.**
- Ordre temporel des citations : fournit la variable auxiliaire u = décennie et la direction du temps (utile pour le contraste temporel). Mais l'hypothèse « les latentes sont indépendantes sachant u » est fausse par construction : taille, prestige et âge d'un domaine co-évoluent.
- Sous-domaines, pays, décennies comme environnements : donnent une variable u à valeurs multiples (condition de rang plausible). Mais les environnements ne sont pas des interventions : un pays ne modifie pas une seule latente. Le décalage parcimonieux de mécanisme est une hypothèse à tester, pas une donnée.
- Courses de l'organisme automatique : affectation randomisée et dose de contact contrôlée. Ici, et ici seulement, les hypothèses d'intervention sont vraies et connues. Les latentes « fertilité » restent cependant définies par nos propres juges figés ; le théorème identifie ce que les juges mesurent, pas la fertilité au sens de la littérature réelle.

(c) **Ce qu'un modèle non supervisé apprend en pratique sur des citations.** Les axes de plus grande variance : taille du domaine, âge, prestige des revues, langue, régime de citation disciplinaire (biomédecine contre mathématiques). Détection : corréler chaque latente apprise avec ces covariables de nuisance ; mesurer la prédiction de la fertilité après résidualisation ; vérifier que la latente « survit » à une permutation des étiquettes de domaine (test de permutation) ; comparer sur deux fenêtres temporelles disjointes (stabilité). Outils : iVAE ou analyse en composantes indépendantes par contraste temporel comme encodeur ; sondes linéaires de nuisance ; scores de démêlage (MCC, DCI — SUPPOSÉ pour les noms exacts) ; régression symbolique sur les latentes retenues.

(d) **Épreuve empirique qui tranche.**
1. Mondes inventés à causes connues : générateur scellé avec k latentes vraies dont certaines causent la fertilité et d'autres seulement la prédisent (corrélées via une variable de sélection). Bras A : non supervisé seul. Bras B : non supervisé plus variable auxiliaire (régime). Bras C : non supervisé plus interventions randomisées (courses). Métrique 1 : recouvrement des latentes vraies (coefficient de corrélation moyen après appariement). Métrique 2, la seule qui compte : **erreur de prédiction de l'effet d'une intervention jamais vue** sur un paramètre, comparée à l'effet vrai du générateur.
2. Littérature réelle : coupure temporelle ; prédire l'effet d'une « intervention naturelle » postérieure (déménagement de chercheur, création d'une conférence conjointe), enregistrée après la coupure, à partir de latentes apprises avant.

(e) **Critères de mort chiffrés** (seuils à geler dans un préenregistrement, les valeurs ci-dessous sont des propositions à discuter, pas des chiffres opposables) :
- Voie « non supervisé seul » morte si, sur mondes inventés, l'erreur sur l'effet d'intervention jamais vue n'est pas meilleure qu'une ligne de base qui prédit l'effet moyen, sur 3 mondes sur 3, avec intervalle de confiance bootstrap à 95 % recouvrant la ligne de base.
- Voie « non supervisé plus environnements » morte si le recouvrement des latentes causales vraies est inférieur à 0,5 alors que celui des latentes de nuisance dépasse 0,8 : le modèle a appris la taille et le prestige.
- Voie « non supervisé plus courses randomisées » morte si l'effet de dose estimé par le modèle diffère de plus d'un facteur 2 de l'effet mesuré par simple différence de moyennes entre bras randomisés : le modèle n'apporte rien au randomisé.

### (4) Vérification hors de nous

- Les théorèmes sont vérifiables sur les papiers (énoncé, hypothèses, page).
- Le générateur de mondes inventés, les graines et les seuils sont scellés avant lecture ; un tiers peut rejouer.
- Sur littérature réelle, l'épreuve post-coupure est falsifiable par quiconque dispose du même graphe de citations.
- Un relecteur extérieur du domaine de l'apprentissage causal peut juger si les hypothèses revendiquées « gratuites » le sont.

### Reformulation

« Construire trois mondes inventés scellés où k latentes connues engendrent des paires de niches et leur fertilité, certaines latentes causales, d'autres seulement corrélées par sélection. Y comparer trois voies : non supervisé seul, non supervisé avec environnements, non supervisé avec affectations randomisées. Juger chaque voie sur l'erreur de prédiction de l'effet d'une intervention jamais vue, avec seuils de mort gelés. Transposer ensuite la voie survivante à la littérature réelle avec coupure temporelle et interventions naturelles postérieures. Énoncer pour chaque théorème invoqué ses hypothèses exactes et lesquelles nos données ne satisfont pas. »

(≈ 1 180 mots)

---

## Question 7 — l'allumage comme ensemble autocatalytique de fiches

### (1) Ce qu'un expert ferait et que la question ne demande pas

Un expert des ensembles autocatalytiques (théorie RAF : « reflexively autocatalytic and food-generated », Hordijk et Steel 2004, « Detecting autocatalytic, self-sustaining sets in chemical reaction systems », SUPPOSÉ) demanderait d'abord ce qui joue le rôle de l'**ensemble nourricier** (food set) et ce qui joue le rôle de **catalyse** : dans une réaction chimique, un catalyseur n'est pas consommé et n'est pas un réactif ; dans le bisociateur, une fiche est réactif de sa fusion. Sans distinction réactif/catalyseur, le formalisme RAF dégénère en simple fermeture de graphe (ce qui est atteignable depuis le corpus), et le seuil de transition disparaît. Il demanderait aussi si les fiches ont une **dégradation** (sans dégradation, tout lot « s'entretient » trivialement puisque rien ne meurt) et si le corpus est fini (l'entretien sans apport extérieur est alors une question de combinatoire, pas de dynamique).

Il distinguerait enfin **existence** d'un ensemble autocatalytique (propriété statique du graphe de réactions, calculable en temps polynomial par l'algorithme RAF) et **dynamique** (concentration, cinétique) : la question de Lazar mêle les deux via « génération après génération ».

### (2) Données brutes

Le journal complet d'une course, par génération : identifiant de chaque fiche, ses parents (fusion de quelles fiches), le proposeur et la graine, la décision de chaque juge figé (avec score brut, pas seulement accepté/refusé), la dose de contact (titres du tableau minimal, nombre de fusions tentées), les fiches « mortes » au test de mort et pourquoi, et les fiches nourricières (importées du corpus) marquées comme telles. Sans la marque nourricière, le food set n'est pas reconstructible.

### (3) Méthodes et outils

(a) **Où l'analogie tient et où elle casse.**
- Tient : la structure « ensemble d'objets, ensemble de réactions, chaque réaction produite par des objets de l'ensemble, fermeture par rapport à un ensemble nourricier » est exactement l'hypergraphe fiches → fusions → fiches. L'algorithme RAF (élagage itératif) s'applique tel quel pour trouver le plus grand sous-ensemble fermé ; la condition « chaque réaction catalysée par un élément de l'ensemble » devient « chaque fusion rendue possible par une fiche du lot », si l'on définit une relation de catalyse.
- Casse 1 : pas de consommation. Une fiche reste disponible après fusion ; il n'y a donc pas de compétition pour le substrat ni de seuil de concentration. Correctif possible : introduire une dégradation (une fiche non réutilisée pendant g générations sort du lot) et un budget (nombre de fusions par génération) qui crée la rareté.
- Casse 2 : pas de stœchiométrie. Une fusion est un choix combinatoire, pas une conservation de masse ; la « production » d'une fiche par une fusion est une décision d'un juge. Le graphe est donc **sélectionné**, pas chimique : la fermeture autocatalytique dépend du juge.
- Casse 3 : le substrat est le corpus, qui est immense. Si le food set est tout le corpus, tout est « généré depuis le food set » et la condition F est vide. Il faut restreindre le food set au tableau minimal effectivement fourni à la course.
- Casse 4 : catalyse. Il faut nommer explicitement ce qui « catalyse » une fusion : par exemple, une fiche-pont (concept partagé) qui rend la fusion de deux autres fiches recevable par le juge. Sans cette relation, l'autocatalyse n'est pas définie.

(b) **Définition opérationnelle.** Soit G_t le graphe à la génération t : fiches F_t, fusions R_t, food set F_0 (tableau minimal). Relation de catalyse C ⊂ F_t × R_t définie par « la fusion r a été proposée en citant la fiche f comme pont » (à journaliser). Un **lot allumé** à la génération t est un sous-ensemble RAF de G_t : chaque fusion du lot est catalysée par une fiche du lot, et chaque fiche du lot est atteignable depuis F_0 par des fusions du lot. **Allumage** : existence d'un RAF non vide hors F_0 qui persiste sur g générations consécutives malgré la dégradation. **Fertilité d'une paire** (f1, f2) : variation de la taille du plus grand RAF quand on retire la fusion de (f1, f2) du graphe (contribution par ablation), ou nombre de fusions aval que cette fusion rend catalysables. Cela donne une fertilité mesurable, comparable entre lots, sans juge supplémentaire.

(c) **Prédiction chiffrée et critère de mort pour la génération 2** (propositions à geler, non opposables). Prédiction si l'analogie tient : la taille du plus grand RAF hors F_0 a un comportement de seuil en fonction de la dose (nombre de fusions par génération) : nulle sous une dose d_c, croissante au-dessus, avec une pente à la transition plus forte que celle d'un modèle nul où les fusions sont acceptées au hasard à taux égal. Critère de mort : si, sur toutes les doses testées (au moins 5 niveaux, 3 graines chacun), aucun lot ne contient un RAF non vide hors F_0 à la génération 2, ou si la taille du RAF n'est pas distinguable (test de permutation, p > 0,05) de celle obtenue en permutant aléatoirement les parents des fusions, l'hypothèse « allumage autocatalytique » est morte pour cette génération. Réserve de symétrie (R4) : un RAF qui couvre presque tout le lot dès la génération 2 est suspect de fermeture triviale (catalyse trop lâche).

(d) **Antériorités.**
- Kauffman 1986, « Autocatalytic sets of proteins », SUPPOSÉ ; Kauffman 1993, *The Origins of Order*, SUPPOSÉ.
- Hordijk et Steel 2004 (algorithme RAF), SUPPOSÉ ; Hordijk 2012 (synthèse, arXiv 1205.0584, titre vu).
- Technologie et économie : Hordijk et Steel, modèle d'autocatalyse en technologie (« Emergence of autocatalytic sets in a simple model of technological evolution », 2022, titre vu, SUPPOSÉ pour les auteurs exacts) ; Cazzolla Gatti, Koppl, Fath, Kauffman, Hordijk 2020, « On the emergence of ecological and economic niches », SUPPOSÉ ; Arthur 2009, *The Nature of Technology*, combinaison de technologies existantes, SUPPOSÉ ; Kauffman, « economic webs » et « adjacent possible », SUPPOSÉ.
- Idées et culture : Gabora et Steel, « Modeling a cognitive transition at the origin of cultural evolution using autocatalytic networks » (arXiv 2007.06442, titre vu) ; Gabora et Steel 2022 (arXiv 2204.01059, titre vu, contenu non lu).
- Possible adjacent et innovation : Loreto, Tria, Servedio, Strogatz 2014, « The dynamics of correlated novelties », SUPPOSÉ ; Loreto et al. sur urnes de Pólya à déclenchement, SUPPOSÉ.
- Cascades d'idées entre générations : Fleming 2001 (recombinaison), Uzzi 2013 (combinaisons atypiques), déjà relevés ; modèles de percolation de l'innovation (Silverberg et Verspagen 2005, SUPPOSÉ).
Zone à vérifier plus durement (R8) : il est probable que « RAF appliqué à des agents génératifs ou à un organisme de recherche automatique » soit vierge ; ce vide est séduisant, donc à chercher avec plus d'acharnement avant d'être revendiqué.

(e) **À journaliser dès la génération 1** (sinon la génération 2 ne pourra pas être lue) : pour chaque fusion, parents, fiche-pont citée (relation de catalyse), proposeur, graine, dose au moment de la fusion, décision brute de chaque juge ; pour chaque fiche, génération de naissance, marque nourricière ou non, nombre de réutilisations par génération, génération de mort et motif ; pour chaque génération, dose (fusions tentées, titres du tableau), taille du plus grand RAF, nombre de composantes fermées, proportion de fiches atteignables depuis F_0 ; le code de calcul du RAF et son empreinte ; un test de la garde sur un cas sain et sur un artefact (R5) : un graphe où le RAF est connu par construction.

### (4) Vérification hors de nous

- L'algorithme RAF est publié ; un tiers peut le rejouer sur le journal scellé.
- Le modèle nul par permutation des parents est reproductible.
- La définition de catalyse est publique et falsifiable : si une autre relation de catalyse donne un RAF très différent, l'allumage est un artefact de définition.
- Un expert de la théorie RAF peut juger si l'absence de consommation invalide l'usage du formalisme.

### Reformulation

« Définir l'allumage comme l'existence persistante d'un ensemble RAF non vide, hors du tableau nourricier, dans l'hypergraphe journalisé fiches → fusions → fiches, avec une relation de catalyse explicitement journalisée (fiche-pont) et une dégradation des fiches inutilisées. Définir la fertilité d'une paire comme sa contribution au RAF par ablation. Prédire un seuil de dose ; geler avant la génération 2 un critère de mort (aucun RAF à aucune dose, ou RAF indistinguable du modèle nul par permutation des parents) et une réserve de fermeture triviale. Vérifier d'abord les antériorités technologie, économie, culture avant toute revendication de zone vierge. »

(≈ 1 150 mots)
