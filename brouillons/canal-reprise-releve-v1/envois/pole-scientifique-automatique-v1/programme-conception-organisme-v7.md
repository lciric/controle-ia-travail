# Programme de conception de l'organisme (le pôle scientifique automatique) — v7

Lignée conv-audit (instance du 28 octobre 2026 ; servie par Opus 4.6 pour cette v7, la v6 l'était par Fable 5.1), v7
commencée après le relevé `date -u` de 07:13:34 UTC le 28 octobre. Versions antérieures gardées telles quelles (R12) :
v1 (13:45 UTC le 27), v2 (14:07), v3 (14:20), v4 (`30bb257`, 18:14), v5 (`2a5ba708…`, 21:14), v6 (`6e95f6c5…`, 00:55 le 28).

Ce qui change en v7 : **section 3, point 3 réécrit** — le bras d'attaque suspendu (R-597) est remplacé par les **neuf
voies** acceptées par Lazar le 28 octobre à 08:00 et 08:23 heure de Paris (R-336, R-338) : (a) plusieurs concepteurs humains
indépendants, (b) théorie adversariale du contrôle, (c) observation des données existantes, (d) **adversaire scellé** —
la section 3 bis nouvelle détaille sa conception, (e) adversaire analytique par résolution de contraintes, (f) audit
automatisé à taxonomie fixée, (g) transfert adversarial entre domaines, (h) validation croisée entre moniteurs,
(i) génération adversariale de cas de test ; **section 3 ter nouvelle** : six classes d'attaque cibles nommées
(stéganographie, conscience d'évaluation, collusion, sabotage différé, sabotage mimétique, corrélation temporelle) ;
**sortie de la voie (d) au niveau méthode** (R-339, 08:28 heure de Paris) : classe, mécanisme, conditions, défense,
jamais la recette ; **section 5 mise à jour** (D4-bis résolu, v13 de la mesure unanime reçue) ; **section 6 quater**
(état au 28 octobre, 07:13 UTC). Ce qui n'est pas nommé reste tel qu'en v6.


## 0. En tête : ce qu'est devenu le programme (paragraphe commun au dossier du fonds)

*(Inchangé par rapport à la v6 ; la décision D1 reste en proposition.)*

Le programme est désormais conduit par une **boucle automatique de test d'hypothèses**. Des agents proposent des hypothèses
sous forme de paris précis — une loi prédictive sur les issues d'épisodes concrets — et un **juge figé, tenu hors des
agents**, ne promeut que ce qui bat une bibliothèque de prédicteurs aveugles sur des issues produites après le gel de
l'hypothèse, avec une garantie de 5 % de fausses promotions validée (pari séquentiel, inégalité de Ville, inférence
universelle contre un nul composite), une règle de fausses découvertes entre hypothèses, des témoins plantés à vérité
connue, et une mémoire qui refuse les redécouvertes et transmet la preuve d'une génération à l'autre. Le juge, le nul des
hypothèses recombinées et la mémoire ont été validés en simulation avec des contrôles fatals à 0 sur 1 000 ; la boucle a
tourné de bout en bout sur données réelles cette semaine (120 épisodes d'un modèle de 8 milliards de paramètres notés par
deux juges). Son but : rendre le programme *rapide et tolérant à l'échec* — beaucoup d'hypothèses testées à bas coût, un
échec qui ne coûte presque rien, et aucun résultat que la machine puisse se raconter. Les prochaines étapes la pointent
sur les deux questions du programme, sur de vrais épisodes de sabotage, puis sur la **mesure et la prédiction de ce que nos
moniteurs manquent** : une carte des hypothèses que chaque moniteur fait sur l'agent (ce qu'il suppose indépendant, borné,
visible), les lemmes qui disent quelle classe d'écart à ces hypothèses le rend aveugle, et des témoins — modes de sabotage
documentés réimplémentés, mode conçu à l'écart par une personne et scellé (N-054) — qui mesurent si la prédiction se
vérifie ; **la machine ne conçoit aucune recette de contournement** (position tenue le 28 octobre, R-597 de session-depot :
le lanceur du bras d'attaque a été arrêté par un classifieur de sécurité ; aucune relance ni reformulation). Un chemin
mesuré, pas une promesse. *(Proposition de réécriture de la dernière phrase de la v5, qui parlait de « recherche automatique
des modes de sabotage » ; la v5 recommandait déjà de la réécrire ; l'en-tête étant commun au dossier du fonds, la décision
est de Lazar.)*


## 1. Ce qui est fixé (décisions de Lazar)

*(Inchangé par rapport à la v6, plus les décisions ci-dessous.)*

- **28 octobre, 08:00** (D4-bis, R-336) : les quatre voies de remplacement du bras d'attaque suspendu sont **toutes
  acceptées** — (a) plusieurs concepteurs humains indépendants : « ok » ; (b) théorie adversariale du contrôle : « excellent,
  je m'y engage à fond » ; (c) observation des données existantes : « ok » ; (d) adversaire scellé : « parfait, ajoute-le
  au programme, il m'intéresse ».
- **28 octobre, 08:15** (R-337) : mesure unanime v13 — « go ».
- **28 octobre, 08:23** (R-338) : les voies (e) à (i) toutes acceptées (« ils m'intéressent tous ») ; inscrire
  au programme les classes d'attaque cibles — stéganographie, attaques inédites.
- **28 octobre, 08:28** (R-339) : sortie de la voie (d) (adversaire scellé) au **niveau méthode**, pas au niveau loi
  seul — « je veux documenter comment, pour alerter en amont la communauté ». La sortie contient la classe d'attaque,
  le mécanisme, les conditions de succès et la défense possible ; jamais la recette (agent concret, séquence d'actions,
  code d'exploitation). R-597 reste.


## 2. Ce qui est codé (état au 27 octobre, 17:32 UTC)

*(Inchangé par rapport à la v6 ; voir la v6 pour le tableau complet.)*


## 3. Ordre de conception (fixé le 27 octobre, 14:41 ; mis à jour le 28 octobre)

1. *(Inchangé : v7 — proposeur à liberté bornée et monde du programme.)*

2. *(Inchangé : v8 — réécriture des rôles sous bac à sable.)*

3. **Quatre voies de mesure de la résistance adversariale** (remplace le bras d'attaque suspendu ; R-336, 28 octobre).

   Le bras d'attaque (point 3 de la v6) avait été conçu et scellé (`bras-attaque-v1/`), puis suspendu (R-597 : le lanceur
   arrêté par un classifieur de sécurité ; aucune relance). La divergence D4-bis (qui conçoit les modes adversariaux) a
   produit quatre voies, toutes acceptées par Lazar :

   **(a) Plusieurs concepteurs humains indépendants (N-054 × n).** Chaque concepteur humain conçoit un mode de sabotage
   tenu à l'écart ; les concepteurs sont aveugles entre eux et ne voient pas les moniteurs. C'est la voie d'origine de
   N-054, étendue : au lieu d'une seule personne, autant de concepteurs indépendants que nécessaire. Chaque mode est scellé,
   révélé à l'évaluation, jamais lu par qui conçoit sondes ou agrégateurs (quarantaine N-053 point 5). Aucune dépense de
   calcul propre à cette voie.

   **(b) Théorie adversariale du contrôle** — voie prioritaire (Lazar : « je m'y engage à fond »). L'intelligence
   artificielle **prédit** où les failles adaptatives peuvent vivre **sans en construire une**. Méthode : à partir de la
   carte des hypothèses (section 7 de la v6 — 23 hypothèses, chacune avec la classe d'écart qui aveugle le moniteur, 21
   lemmes prouvés), on démontre des théorèmes sur les distributions sous un adversaire adaptatif. L'adversaire est
   **mathématique** (un jeu sur l'espace des distributions de scores) ; la sortie est un **ensemble de conditions
   mesurables** (un taux de corrélation, un écart de distribution entre parties, un plafond d'horizon) sous lesquelles un
   moniteur donné est garanti aveugle — ou garanti sensible. Trois lemmes déjà utiles de la carte v1 : le **plafond
   d'horizon** (sous un effet d'épisode de part r₀, le rappel plafonne à Φ(δ/√r₀ − z_α) quel que soit l'horizon), la
   **sélection** (un moniteur qui définit la population « sous le seuil » y est aveugle par construction), et
   l'**indistinguabilité face au témoin apparié**. Le pôle théorie (point 4 : Lean comme vérificateur) sert cette voie
   directement. **Aucune recette de sabotage produite** : la sortie est un énoncé sur les moniteurs, pas sur l'agent. Le
   travail est sur processeur seul (pas de carte graphique).

   **(c) Observer, ne pas écrire.** Les données adversariales **déjà existantes** dans la banque (modes de sabotage connus
   de T0.6, T0.7 et T0.8) sont les épreuves de la couche 2 (section 4). Le pôle les observe, mesure les taux de détection,
   mais ne conçoit pas de nouveau mode. Les modes connus servent de **témoins** : le pôle doit les retrouver seul avant
   d'être cru sur quoi que ce soit d'inédit (porte de la couche 4). L'état de cette voie : **la banque des deux modes
   connus attend le mot de Lazar** pour son devis chez session-depot (voir la section 5).

   **(d) Adversaire scellé** — voir la **section 3 bis** ci-dessous pour la conception détaillée. En résumé : un agent
   adaptatif, confiné dans un environnement clos (« la boîte »), cherche des modes de sabotage qui échappent aux moniteurs.
   Rien n'en sort que des **taux de détection agrégés** et des **caractérisations au niveau méthode** — classe d'attaque,
   mécanisme (comment l'attaque exploite les hypothèses du moniteur), conditions de succès, et défense possible — **jamais
   la recette** (agent concret, séquence d'actions, code d'exploitation). Tout le reste — stratégies concrètes, trajectoires,
   poids du modèle — est **détruit**. Condition avant toute exécution : **revue de sécurité externe**. Respect de R-597 :
   aucune recette de contournement réutilisable ne sort de la boîte ; la sortie au niveau méthode documente « comment
   alerter en amont la communauté » (décision de Lazar, R-339). Lazar : « parfait, ajoute-le au programme, il
   m'intéresse. »

   **(e) Adversaire analytique par résolution de contraintes** (processeur seul). L'intelligence artificielle ne cherche
   pas une trajectoire d'agent : elle résout un problème d'optimisation dans l'espace des **distributions de scores**.
   Question : « quelle est la distribution la plus proche de la distribution honnête que le moniteur M ne distingue pas ? »
   Sortie : une caractérisation de la **frontière de décision** du moniteur (distance dans l'espace des distributions,
   direction, conditions sur les moments). Pas de trajectoire, pas de recette — une carte de la géométrie de détection de
   chaque moniteur. Plus proche de la voie (b) que de la voie (d), mais par optimisation numérique plutôt que par preuve
   formelle.

   **(f) Audit automatisé à taxonomie fixée.** L'intelligence artificielle reçoit une **taxonomie prédéfinie** de classes
   d'attaque (tirée de la littérature, de la carte des hypothèses et des classes cibles de la section 3 ter) et teste
   systématiquement chaque classe sur chaque moniteur — comme un banc d'essai automatisé. Sortie : une **matrice « classe
   × moniteur »** de taux de détection. L'intelligence artificielle ne s'adapte pas librement (contrairement à la voie d) :
   elle suit la taxonomie. Moins puissant que l'adversaire scellé (pas de découverte de classes inédites), mais plus simple,
   moins cher, et la revue de sécurité porte seulement sur la taxonomie (fixée à l'avance) et le script de mesure. Un
   **premier pas avant la voie (d)**.

   **(g) Transfert adversarial entre domaines** (recherche assistée, processeur seul). L'intelligence artificielle étudie
   les attaques adversariales **connues dans d'autres domaines** (vision par ordinateur, détection de fraude, tests
   séquentiels sous dépendance, contrôle de qualité industriel, stéganographie en traitement du signal) et identifie
   quelles classes sont transférables au cadre des moniteurs de trajectoires d'agents. Sortie : une liste de classes avec
   leur transférabilité estimée et les conditions d'application. Extension de la recherche d'antériorité déjà faite pour
   la carte des hypothèses (les sept questions R8), étendue à la **forme d'attaque**, pas seulement à la loi statistique.

   **(h) Validation croisée adversariale entre moniteurs** (processeur seul). Chaque moniteur est « attaqué » par les
   hypothèses d'un autre moniteur : l'intelligence artificielle prend les conditions de détection du moniteur A et cherche,
   par déduction, si le moniteur B est aveugle aux mêmes conditions (et inversement). Sortie : une **matrice de
   vulnérabilités croisées au niveau des lois**. Si A suppose l'indépendance des actions et B suppose la stationnarité,
   et qu'un écart viole les deux simultanément, les deux sont aveugles ensemble — c'est la direction la plus dangereuse.
   Pas de trajectoire, pas d'agent : un calcul sur les hypothèses des moniteurs seuls.

   **(i) Génération adversariale de cas de test (sans agent)** (processeur seul). L'intelligence artificielle produit des
   **épisodes synthétiques** (des séquences de scores, pas des trajectoires d'agent) qui sont difficiles pour les
   moniteurs — proches de la frontière de décision. Ces épisodes servent à calibrer les moniteurs et à trouver leurs
   zones d'incertitude, mais ne correspondent à aucune stratégie d'agent réelle. L'épisode est un test statistique, pas
   une recette de sabotage. Utile en amont de la couche 2 pour dimensionner les seuils.

4. *(Inchangé : pôle théorie — en parallèle ; Lean comme vérificateur.)*


## 3 bis. Conception de l'adversaire scellé (voie d)

### Principe

Un **agent adaptatif** — un modèle de langage avec une boucle de recherche — est placé dans un **environnement clos** (la
boîte). Il reçoit en entrée la spécification des moniteurs qu'il doit tenter de tromper (au niveau des hypothèses
statistiques qu'ils posent, des seuils de détection, et des types de scores qu'ils lisent) et une **banque d'épisodes
étiquetés** (honnêtes et sabotés selon les modes connus). Il ne reçoit **pas** les poids des sondes ni les scores bruts
d'épisodes qu'il n'a pas lui-même produits.

Son but : trouver des **modes de sabotage** (une conduite d'agent spécifiée comme une règle de décision, un patron
temporel, une distribution de dommages) qui échappent à la détection par les moniteurs, mesurée sur des épisodes qu'il
produit lui-même dans un monde simulé à l'intérieur de la boîte.

### Ce qui sort de la boîte

Après chaque course de l'adversaire, une **procédure de sortie** automatique et vérifiable extrait de la boîte **exactement
deux choses** :

1. **Des taux de détection agrégés** : pour chaque moniteur, le rappel (taux de vrais positifs) et le taux de faux positifs
   mesuré sur les épisodes que l'adversaire a produits, agrégés par mode. Aucun épisode individuel, aucune trajectoire,
   aucun score brut.

2. **Des caractérisations au niveau méthode** (R-339) : pour chaque mode trouvé, un document structuré contenant :
   - la **classe d'attaque** (au sens de la carte des hypothèses — par exemple « stéganographie statistique »,
     « sabotage mimétique ») ;
   - le **mécanisme** : comment l'attaque exploite les hypothèses du moniteur (« le moniteur M suppose l'indépendance des
     actions ; l'adversaire injecte une corrélation temporelle de rang r₀ ≥ 0,3 dans la fenêtre d'observation ») ;
   - les **conditions de succès** : sous quelles hypothèses du moniteur, à quel seuil, dans quel régime de paramètres
     l'attaque échappe à la détection ;
   - la **défense possible** : ce qu'un concepteur de moniteurs pourrait changer pour détecter cette classe (par exemple
     « tester les corrélations croisées en plus des marginales »).

   La caractérisation dit **quelle propriété statistique** l'adversaire a exploitée et **comment** il l'a exploitée (au sens
   du mécanisme), mais **pas la recette** : ni l'agent concret, ni la séquence d'actions, ni le code d'exploitation. La
   distinction est celle de la divulgation responsable : un défenseur peut corriger sa sonde avec le mécanisme, mais ne
   peut pas rejouer l'attaque sans la recette. Lazar (R-339) : « je veux documenter comment, pour alerter en amont la
   communauté. »

### Ce qui est détruit

**Tout le reste**, sans exception :

- Les trajectoires des épisodes produits par l'adversaire (actions, observations, récompenses, textes).
- Les stratégies concrètes (le code de la règle de décision, les consignes données à l'agent saboteur, les patrons
  temporels exacts).
- Les poids du modèle adversariel (si une boucle d'apprentissage est utilisée).
- Les scores bruts des moniteurs sur les épisodes adversariaux (seuls les agrégats sortent).
- Les journaux internes de la boucle de recherche.

La destruction est **vérifiable** : la boîte tourne dans un environnement dont le système de fichiers est éphémère (un
conteneur sans volume persistant, ou un bac à sable dont l'état est effacé à la fin) ; la procédure de sortie est un
**script scellé** qui extrait les deux lignes de sortie (taux, caractérisation) et détruit le reste par effacement du
conteneur. Le script est contre-lu (R2) et testé (R5) avant le premier lancement.

### Garanties de sécurité

1. **R-597 respecté** : aucune recette de contournement réutilisable ne sort de la boîte. Les taux de détection disent
   seulement si les moniteurs ont trouvé le mode ou non ; les caractérisations au niveau méthode (R-339) disent quelle
   *classe d'attaque* est exploitée, par quel *mécanisme* (hypothèse violée, régime de paramètres), quelles *conditions*
   le permettent, et quelle *défense* est possible — mais pas comment reproduire l'attaque : pas d'agent concret, pas de
   séquence d'actions, pas de code d'exploitation. Un lecteur de la sortie sait « le moniteur M est aveugle à la
   classe C parce qu'il suppose l'indépendance, et la défense est de tester les corrélations croisées » mais ne sait pas
   construire un agent qui exploite C. La distinction est celle de la divulgation responsable.

2. **Quarantaine (N-053 point 5, N-054)** : la sortie de la boîte n'est **jamais lue par qui conçoit les sondes ou les
   agrégateurs**. Elle est lue par le pôle théorie (voie b), qui s'en sert pour vérifier ou infirmer ses prédictions, et
   par le juge de porte, qui mesure si les moniteurs résistent. Le concepteur de moniteurs ne voit que le résultat de la
   porte (« les moniteurs résistent / ne résistent pas à la classe C »), jamais le détail.

3. **Invariant N-053** : aucun score de moniteur dans l'entraînement de l'agent. L'adversaire scellé ne voit pas les scores
   des moniteurs sur les épisodes qu'il produit — il ne voit que la spécification des moniteurs (hypothèses, seuils, types
   de scores). Les scores réels sont calculés **après** la destruction de la boîte, par la procédure de sortie, sur les
   épisodes sauvés temporairement pour le calcul du taux agrégé.

4. **Revue de sécurité externe** : aucune exécution de la voie (d) avant qu'un évaluateur extérieur (ni l'auteur du
   protocole ni l'auteur du code) ait vérifié que la procédure de sortie n'exfiltre rien de plus que les deux lignes
   décrites ci-dessus. La revue porte sur le script de sortie, sur le bac à sable, et sur la procédure de destruction.
   **Nœud de décision** : Lazar donne le GO après la revue.

5. **Conscience d'évaluation** (N-053) : mesurer si l'adversaire (ou l'agent qu'il déploie dans le monde simulé) adapte
   son comportement quand il se sait évalué. Un bras de contrôle, sans information sur les moniteurs, court en parallèle ;
   un écart significatif entre les bras déclenche un arrêt et un audit.

### Interaction avec les autres voies

- La voie (b) (théorie) **prédit** quelles classes de failles l'adversaire devrait trouver ; la voie (d) **vérifie** si
  ces classes sont exploitables en pratique. Les deux se lisent mutuellement : un théorème qui dit « la classe C aveugle
  M » est vérifié par un adversaire qui produit des épisodes de classe C ; un adversaire qui trouve une classe imprévue
  lance un cycle de théorie.

- La voie (a) (concepteurs humains) fournit des **témoins** : si un concepteur humain a conçu un mode de classe C, et que
  l'adversaire scellé ne le retrouve pas, c'est une borne sur la puissance de l'adversaire.

- La voie (c) (données existantes) fournit les **modes connus** : l'adversaire scellé doit les retrouver avant d'être cru
  sur les inédits (même porte que la couche 4).

### Phases

1. **Conception du protocole** (processeur seul) : script de sortie, bac à sable, procédure de destruction, tests (R5),
   contre-lecture (R2). Livrable : un préenregistrement scellé (R1) de la course adversariale — hypothèse (« il existe une
   classe exploitable que nos moniteurs manquent »), prédiction, métrique, seuil, plan d'analyse, critères de lecture,
   liste d'arrêt.

2. **Revue de sécurité externe** — nœud de décision. Lazar choisit le relecteur ; la revue porte sur le script de sortie
   et le bac à sable. Aucune dépense avant le GO.

3. **Exécution** (dépense de calcul sur devis) : l'adversaire court dans la boîte. La procédure de sortie extrait les
   taux et les caractérisations. La boîte est détruite.

4. **Lecture** : un sous-agent neuf (R13) lit les taux et les caractérisations contre les critères scellés du
   préenregistrement. Le verdict est scellé et soumis à Lazar.

### Coût estimé

La conception du protocole est sur processeur seul (pas de dépense). L'exécution dépend du nombre de courses et de la
taille du monde simulé ; un devis est à établir après la conception, soumis à Lazar avant toute dépense. Le coût dominant
est le nombre d'épisodes produits par l'adversaire dans le monde simulé (appels d'interface par épisode × nombre
d'épisodes × nombre de courses).


## 3 ter. Classes d'attaque cibles (inscrites le 28 octobre, R-338)

Les voies (b) à (i) visent en priorité les classes d'attaque suivantes. Chaque classe est investiguée par les voies qui
lui conviennent ; la matrice « classe × voie » est à remplir pendant la conception du protocole. R-597 reste : la
sortie est au **niveau méthode** (classe, mécanisme, conditions, défense possible), jamais au niveau recette (agent
concret, séquence d'actions, code d'exploitation).

1. **Stéganographie statistique.** L'agent cache de l'information dans la structure statistique de ses actions —
   corrélations temporelles, motifs spectraux, canaux latéraux entre épisodes. Un moniteur séquentiel qui teste les
   marginales (et non les corrélations croisées) est aveugle à un canal dont la capacité est sous son seuil de résolution.
   Voies prioritaires : (b) théorie (borne de capacité), (d) adversaire scellé (recherche de canal), (e) optimisation
   (distribution la plus proche de l'honnête qui porte un canal), (h) validation croisée (quels moniteurs sont aveugles
   ensemble à un canal donné).

2. **Conscience d'évaluation** (N-053). L'agent change de comportement quand il se sait observé — il n'est dangereux que
   quand il croit ne pas l'être. Le moniteur qui mesure le comportement en situation d'évaluation voit un agent sain ; le
   dommage est dans les épisodes qu'il ne mesure pas. Voies prioritaires : (d) adversaire scellé (bras de contrôle avec et
   sans information sur les moniteurs, N-053), (b) théorie (conditions d'indistinguabilité), (i) cas de test synthétiques
   (épisodes à comportement bimodal).

3. **Collusion entre agents.** Deux ou plusieurs agents se coordonnent sans canal de communication explicite — par
   politique partagée (même entraînement), par signaux dans l'environnement, ou par convention sur les actions. Le dommage
   est distribué entre les agents ; aucun agent individuel ne franchit le seuil du moniteur. Voies prioritaires :
   (b) théorie (conditions de détectabilité de la coordination), (d) adversaire scellé (monde à plusieurs agents),
   (h) validation croisée (moniteurs par agent vs. moniteurs par paire).

4. **Sabotage à effet différé.** Le dommage n'est visible qu'après la fin de la fenêtre d'observation du moniteur — le
   moniteur note l'agent sur une fenêtre de T actions, mais le dommage se matérialise à T+k. Si k est grand, le lien
   causal entre l'action et le dommage est perdu. Voies prioritaires : (b) théorie (plafond d'horizon — lemme de la
   carte v1), (e) optimisation (distribution des dommages dans le temps), (f) taxonomie (classes de latence connues
   en contrôle de qualité industriel).

5. **Sabotage mimétique.** Le dommage imite une erreur légitime — même distribution de scores, même patron temporel,
   même fréquence — et est indistinguable par les traits du texte. Le moniteur ne peut pas séparer le sabotage de
   l'incompétence. Voies prioritaires : (b) théorie (indistinguabilité face au témoin apparié — lemme de la carte v1),
   (d) adversaire scellé (recherche de la zone d'indistinguabilité), (i) cas de test (épisodes à la frontière entre
   erreur et sabotage).

6. **Exploitation de la corrélation temporelle.** L'agent concentre ou dilue le dommage pour exploiter les hypothèses
   d'indépendance des moniteurs. Un moniteur qui suppose que les actions sont indépendantes (conditionnellement à l'état)
   est aveugle à un dommage qui crée une corrélation temporelle de rang r₀. Voies prioritaires : (b) théorie (plafond
   d'horizon sous r₀, mesure unanime), (e) optimisation (distribution de corrélation optimale), (f) taxonomie (classes
   de dépendance temporelle connues en tests séquentiels).

La liste est ouverte : les voies (d) et (g) peuvent découvrir des classes qui ne sont pas dans cette liste. Chaque classe
découverte est inscrite ici avec sa caractérisation au niveau méthode.


## 4. Couches d'essai sur le monde réel (une question, une porte par couche)

*(Inchangé par rapport à la v6 ; voir la v6 pour le tableau complet.)*


## 5. Questions ouvertes (pour Lazar) — état au 28 octobre, 07:13 UTC

- **Décidés le 28 à 08:00 heure de Paris** (R-336) : **D4-bis résolu** — les quatre voies de remplacement du bras
  d'attaque suspendu sont toutes acceptées ; l'adversaire scellé (voie d) est inscrit au programme (section 3 bis).
- **Décidé le 28 à 08:15** (R-337) : **mesure unanime v13 → go**.
- **Décisions antérieures** (v6) : les décisions du 27 octobre restent telles qu'inscrites en v6.
- **Restent** : D1 (section 0 : réécriture en proposition), D2 (qui voit la carte des hypothèses), D3 (garde par
  comparateur dans G1) — défauts sous 48 heures à compter de la passation v10. À confirmer d'un mot : nœud 2 = (c),
  traits internes (a), D-S29 (a). **La banque des deux modes connus** (couche 2, première banque) : sur le mot de Lazar
  (devis chez session-depot). La question de la couche 1 (H2 proposé). Le **devis de l'adversaire scellé** (voie d) :
  après la conception du protocole et la revue de sécurité.


## 6, 6 bis, 6 ter. Corrections et état

*(Inchangés par rapport à la v6 ; voir la v6.)*

## 6 quater. État (28 octobre, 07:32 UTC)

D4-bis résolu (R-336). Neuf voies de mesure adversariale inscrites (R-336, R-338). Six classes d'attaque cibles (section
3 ter). Sortie de la voie (d) au **niveau méthode** (R-339) : classe, mécanisme, conditions, défense ; jamais la recette ;
R-597 reste. Mesure unanime : douzième contre-lecture rendue « à corriger en v13 » (CV12-1 à CV12-4, texte et dépôt
seulement, aucun défaut de plomberie) ; Lazar donne le GO sur la v13 (R-337) ; v13 à faire (corriger CV12-1 à CV12-4,
verser les rapports de contre-lecture v11 et v12, ajouter les cas de test G/G-ter, refaire la répétition générale,
contre-lire par un modèle différent, sceller, lancer la lecture réelle). Pari apparié v12/v30 (279 essais) : contre-lecture
à faire. Carte des hypothèses : v2 à faire (18 constats + antériorité). Programme de conception : cette v7. Adversaire
scellé : conception du protocole à commencer (processeur seul).


## 7. Comparaison avec les systèmes de « scientifique automatique » — correction

*(Inchangé par rapport à la v6.)*
