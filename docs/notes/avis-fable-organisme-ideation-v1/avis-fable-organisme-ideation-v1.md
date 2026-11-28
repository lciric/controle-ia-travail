# Avis sur l'organisme d'idéation : règle de retour des épreuves vers l'organisme, et ce que serait le meilleur organisme de découverte — v1

- **Nature.** Pièce de travail (classe C), avis consultatif demandé par le directeur. Elle ne décide rien, ne dépense rien et n'a rien modifié au dépôt ; ce qu'elle suggère de trancher est signalé comme nœud.
- **Auteur et date.** Claude Fable 5.2, 24 novembre 2026. Réserve de lignée : plusieurs conceptions de l'organisme sortent de modèles de la même famille ; cet avis peut partager leurs angles morts.
- **Pièces lues.** Les trois pièces fournies : note de sortie du collisionneur sur la boucle entre l'organisme et le contrôle, cahier des charges v3 du banc de mondes plantés, charte du plan Turing. Dans le dépôt : programme complet de l'organisme v3 (`docs/notes/rapports-directeur/programme-organisme-complet-v1/programme-organisme-complet-v3.md`, parties 0 à 4) ; synthèses de veille (`docs/notes/veille-exploration-idees-v1/synthese-v1.md`, `docs/notes/veille-organismes-ideation-v3/synthese-v1.md`) ; lecture descriptive de la course d'auto-conception v9 et proposition de cartes à éprouver (`docs/notes/organisme-auto-conception-v1/course-v2/`) ; fiche de faits de la note sur le juge (`docs/notes/publiabilite-note-organisme-v1/fiche-faits-note-organisme-v2.md`) ; rapport de la rétrodiction des foyers de tension (`docs/notes/plan-turing-v1/pas0-rang1-foyers-tension-v1/`) ; décision sur les revendications resserrées après la veille (N-073) ; intuitions du directeur du 23 novembre (`docs/notes/idee-interessante-v1/`) ; faits v5 du collisionneur sur l'organisme coévolutif (`docs/notes/anteriorite-P-041-v1/collisionneur-organisme-coevolutif-v1/faits-organisme-coevolutif-v5.md`).
- **Non lu.** Aucun fichier sous `archives-reponses-modeles`, aucun coffre, aucun score de moniteur, aucun verdict cloisonné, aucune sortie brute de course : ce que je dis de l'organisme vient de ses descriptions.
- **Statut des références** (§ 14). « Vérifié ici » sur une pièce du dépôt, page citée ; « rapporté par le dépôt » (lu sur PDF par un autre agent) ; « de mémoire, à vérifier sur PDF ». Aucun chiffre ne vient de ma mémoire.
- **Calcul.** Un seul, déterministe : `/tmp/claude-0/-home-user-controle-ia-travail/4bfc0ef9-1358-5ad4-b42a-4fb6de433e11/scratchpad/fable-organisme/calcul-borne-echelle-reserve-reutilisee-v1.py` (sha256 `bb040a9b8177cf1e9e5425d63aef0f1deb120c54717198a72c619b87c3e0bb3c`), sortie `/tmp/claude-0/-home-user-controle-ia-travail/4bfc0ef9-1358-5ad4-b42a-4fb6de433e11/scratchpad/fable-organisme/calcul-borne-echelle-reserve-reutilisee-v1-sortie.txt` (sha256 `01733537b87f878331d8bf99b7584b9a010d2e7186363219d70e56bbd0129b53`).

## 0. En bref

1. **Règle de retour (question 1).** D'accord avec la forme stricte pour tout ce qui lit une famille tenue à l'écart ou une épreuve sur modèle réel : la forme souple y apprend trop peu à l'organisme, coûte une famille inédite par bit, et sa garantie est vide aux tailles en jeu. **Désaccord sur la portée** : étendue aux mondes plantés de conception, comme l'écrit le cahier des charges, la forme stricte retire à l'organisme son seul signal d'apprentissage qui ne soit pas le jugement d'un modèle. **Troisième voie** : un retour par étages, riche sur des mondes engendrés à volonté et sur des mondes semi-synthétiques bâtis sur de vraies traces honnêtes, borné sur des familles de validation, nul sur ce qui est tenu à l'écart ; strict dans un cycle, ouvert entre deux cycles au prix d'une famille neuve.
2. **Meilleur organisme (question 2).** Ce qui distingue les systèmes à découvertes vérifiées, c'est d'abord une vérification externe digne de foi (évaluateur automatique dans la boucle, ou expérience réelle en aval), avant le raffinement de leur société d'agents. La profondeur d'une idée ne se juge pas, elle se mesure par ses conséquences : gain d'information réalisé sur un prédicteur de référence, réemploi dans des résultats ultérieurs vérifiés, étendue des domaines couverts pour une description courte. Le jugement d'un modèle reste admissible comme a priori d'exploration et comme substitut étalonné, audité au hasard ; jamais comme récompense ni comme verdict.
3. **Premier geste.** Mesurer l'apport propre de l'organisme contre le meilleur modèle seul tiré N fois à coût égal. Aucune pièce lue ne l'établit, et la veille du dépôt donne des raisons d'en douter.
4. **Confiance.** Haute sur la forme stricte pour ce qui est tenu à l'écart ; moyenne à haute sur la troisième voie ; haute sur « l'évaluateur d'abord » ; moyenne sur l'architecture proposée ; faible à moyenne sur la capacité de mes trois mesures à saisir ce que le directeur appelle la profondeur (§ 13).

# Partie I — Question 1 : la règle de retour

## 1. Deux « formes souples » différentes circulent dans les pièces

- Dans la note de sortie du collisionneur, le bit par lot remonte des **épreuves réelles** vers l'organisme (option décrite par Opus au bras témoin, qui la tenait par défaut pour interdite). Carbon et Neon objectent qu'il reste une fonction des scores des moniteurs, et que le mécanisme cité protège une même réserve réutilisée, non des familles successives. Son auteur l'a retiré.
- Dans le cahier des charges v3 (§ 6, point 3, marque « bascule souple »), le bit par lot porte sur les **mondes plantés de conception** du banc ; les mondes tenus à l'écart restent sans retour dans les deux formes.

Les deux cas n'appellent pas la même réponse : contre les épreuves réelles et les familles tenues à l'écart, un bit est déjà trop ; sur des mondes plantés de conception, c'est beaucoup trop peu.

## 2. Ce que la forme stricte protège

1. **La lecture unique des familles inédites**, donc la revendication d'universalité mesurée sur des familles jamais vues (N-044, N-050). C'est la ressource rare : la monnaie est le nombre de lectures uniques, non le calcul (note de sortie).
2. **L'invariant « aucun score de moniteur dans un signal d'entraînement ou de sélection »** (N-053), que les faits servis aux collisionneurs étendent à la piste de l'organisme.
3. **La simplicité de l'audit.** Un canal à zéro bit se vérifie sans comptabilité. Le canal humain (une consigne réécrite par quelqu'un qui a vu un résultat) n'est pas bornable.

Ce qu'elle ne protège pas, et qu'il ne faut pas lui prêter : la fuite descendante par spécification (les énoncés de verrous décrivent ce que les mondes instancient) ; la mémoire des modèles pré-entraînés (les solutions de référence des mondes sont, par construction du cahier, des optimums calculables ou des méthodes publiées) ; la lignée commune entre qui écrit les mondes et qui les résout. Sur le banc planté, je tiens ces trois menaces pour plus lourdes que le bit montant : jugement, non mesure.

## 3. Ce qu'elle coûte à l'organisme

1. **Aucune correction d'erreur face au réel dans un cycle.** L'organisme et le contrôle forment « deux chaînes ouvertes » (Opus, note de sortie). Or une garantie « valide par construction » ne vaut que sous le nul modélisé : l'organisme peut produire longtemps des objets justes dans ses mondes et faux sur les vrais modèles, sans l'apprendre.
2. **Le régime du coup unique.** Sans exécution, rien ne départage le plausible du juste. La veille du dépôt rapporte qu'exécuter 156 objections majeures sur les données a renversé 77 conclusions d'une communauté d'agents chercheurs.
3. **Si la règle couvre aussi les mondes de conception** (le cahier réserve leurs issues au seul sélecteur), ce qui revient à l'organisme par passe se réduit au choix d'une variante parmi K déclarées, soit au plus log₂ K bits (deux bits pour quatre variantes). L'auto-conception n'a alors plus, comme signal, que des juges de langage ; à la course d'auto-conception v9, deux items sur cinq étaient à plafond chez chaque juge (lecture descriptive, § 2). La règle pousse ainsi vers le signal circulaire que la décision sur l'oracle des mondes plantés (N-058) veut écarter.
4. **Une direction humaine gelée.** Les énoncés de verrous de tous les cycles sont figés avant la première lecture ; un énoncé mal posé ne se corrige pas dans le cycle.

## 4. Pourquoi la forme souple sur épreuves réelles est à écarter

1. **La garantie invoquée ne s'applique pas, et elle serait vide.** Le mécanisme de l'échelle de Blum et Hardt (« The Ladder ») borne l'erreur d'un classement quand une **même** réserve est interrogée par des soumissions adaptatives (théorème 3.1, p. 6, vérifié ici). J'ai calculé la plus petite erreur que son inégalité garantit à 95 % : 0,48 pour 240 unités indépendantes et dix soumissions ; 0,30 pour 1 000 ; 0,064 pour 100 000 ; 0,031 pour un million. Garantie de pire cas, certes ; c'est elle qu'on invoquait. Les ordres de grandeur lus pour des données réelles sont de quelques centaines d'épisodes (une banque de 240, statut « rapporté », faits v5 de l'organisme coévolutif, fait 13), et l'unité indépendante du programme est la tâche, non l'épisode (N-055) : à ces tailles, la borne ne dit rien d'un écart de quelques points.
2. **Si chaque lot est lu sur une famille fraîche**, il n'y a pas d'erreur adaptative à l'intérieur d'une famille (objection de Neon, juste). Mais chaque bit coûte alors une famille, et il en reste d'autant moins pour éprouver l'organisme final : avec une seule famille lue après la dernière adaptation, la variance entre familles n'est plus estimable.
3. **Le bénéfice est négligeable.** Une poignée de bits n'apprend rien à un organisme ; elle suffit en revanche à choisir entre deux branches après coup.
4. **La lettre de l'invariant** (N-053) est touchée : le bit est une fonction de scores de moniteurs.

Sur ce point, je rejoins la décision du directeur sans réserve.

## 5. Troisième voie : un retour par étages, strict dans le cycle, ouvert entre les cycles

Principe : « aucun retour » n'est pas la seule protection contre l'adaptation. Là où les données se régénèrent à volonté, l'adaptation ne coûte rien à la validité, pourvu qu'on tire des graines fraîches à chaque requête et qu'on compte l'effort de recherche dans les seuils : sous un juge valide à tout instant, chaque tentative est promue à tort avec une probabilité d'au plus α, mais seize tentatives portent la borne à 0,56 (fiche de faits de la note sur le juge, fait F26). Là où les données sont finies et précieuses, le retour doit être nul.

| Étage | Données | Retour vers l'organisme | Ce qui protège |
|---|---|---|---|
| 1 | Mondes plantés d'entraînement, engendrés à volonté | Riche et illimité : données d'expériences, issue de l'oracle, contre-exemples ; journalisé | Graines fraîches à chaque requête ; effort de recherche compté ; généralisation jugée aux étages 3 à 5 |
| 2 | Mondes semi-synthétiques : vraies traces honnêtes, sabotages plantés à vérité connue | Riche | Réservoirs honnêtes disjoints ; fausses alertes finales mesurées sur des traces honnêtes fraîches, jamais servies |
| 3 | Familles plantées de validation, écrites par une instance aveugle | Borné : choix dans une liste finie déclarée, ou un bit par lot à seuil | Comptabilité des bits ; nombre de graines rendu grand |
| 4 | Familles plantées tenues à l'écart | Aucun ; lecture unique | Forme stricte |
| 5 | Épreuves sur modèles réels, familles de sabotage tenues à l'écart | Aucun dans le cycle | Forme stricte |

- **L'étage 2 rapproche l'organisme du réel sans rien consommer de rare.** Les traces honnêtes se régénèrent ; les familles de sabotage, non. Le nul y est la loi réelle des activations, non un modèle ; seule l'alternative est plantée. Cela demande d'admettre des activations honnêtes dans le banc, ce que le cahier exclut aujourd'hui (§ 0, point 5) : nœud.
- **L'étage 3 est le seul où l'esprit de l'échelle a un sens**, parce qu'on peut y porter le nombre de graines au million. Il n'en a pas au niveau des familles, toujours peu nombreuses : d'où l'étage 4.
- **Entre deux cycles**, le verdict scellé d'une lecture peut nourrir le cycle suivant, si la famille lue est déclarée consommée et si celle du cycle suivant est écrite par une instance aveugle à ce verdict. C'est l'esprit de la règle « une famille neuve par cycle » (N-062). Le coût réel de la forme stricte devient lisible : un retour du réel coûte un cycle et une famille neuve.
- **Deux bras à déclarer sur le banc** : sans retour d'oracle (fidèle au transfert vers les épreuves réelles) et avec retour d'oracle sur les mondes d'entraînement (mesure la capacité de recherche). L'écart entre les deux dit ce que vaut un évaluateur, donc s'il faut investir dans l'organisme ou dans ses bancs.

Aucune forme de la règle ne remplace les deux contrôles nés au bras témoin du collisionneur : énoncés vrais contre énoncés leurres, et plan deux sur deux qui sépare mémoire et compétence.

## 6. Ce qui serait à trancher

1. **Portée de la forme stricte.** Enjeu : l'organisme peut-il apprendre de quelque chose ? Options : (a) stricte partout, mondes de conception compris (audit le plus simple ; l'organisme n'apprend que par le choix entre variantes) ; (b) stricte pour le tenu à l'écart et le réel, ouverte aux étages 1 à 3 (signal non circulaire ; journal et comptage à tenir). Recommandation : (b), confiance 0,7.
2. **Activations honnêtes dans le banc** (étage 2). Recommandation : oui, par réservoirs disjoints figés par empreinte ; confiance 0,6.
3. **Recyclage d'une famille lue**, entre cycles. Recommandation : oui, aux deux conditions dites ; confiance 0,6.

# Partie II — Question 2 : le meilleur organisme possible, hors des contraintes du contrôle

## 7. Demande approfondie

### 7.1 Ce qu'un expert ferait ici, et qui n'est pas demandé

1. **Mesurer d'abord si l'organisme ajoute quoi que ce soit** au meilleur modèle seul tiré N fois à coût égal, avec la variance entre courses. La veille du dépôt rapporte qu'à jetons égaux l'avance de l'évolution est de 5 % ou moins sur douze paires sur quinze (Oved et al.) ; que l'écart médian entre méthodes publiées est sous l'écart entre deux courses d'une même méthode, et qu'un sélecteur par notes choisit le meilleur de deux 49,7 % du temps (Zeng et al.).
2. **Localiser le goulot** : la production (le vivier contient-il de bonnes idées ?), le tri (sait-on les reconnaître ?), la vérification, ou le choix des problèmes. On compare le meilleur du vivier selon l'oracle à ce que le tri a retenu.
3. **Remplacer la cible « idée profonde » par des conséquences mesurables**, chacune avec son horizon : millisecondes (monde planté, exécution), heures (expérience de calcul), mois (prévision sur la littérature), années (usage par d'autres).
4. **Choisir les domaines par le coût de la vérification**, et construire les évaluateurs avant les rôles. Les auteurs du système de recherche évolutive de programmes de Google DeepMind (AlphaEvolve) l'écrivent : l'évaluateur automatique est leur avantage et leur limite (p. 2 et 21, vérifié ici).
5. **Valider le banc lui-même** : le classement des architectures sur mondes plantés prédit-il leur classement sur des tâches exécutées ou réelles ? Sans cela, le banc choisit pour le banc.
6. **Travailler le choix des problèmes autant que la production d'idées**, et **prévoir l'échec** : effort de recherche compté, résultats négatifs rapportés, composants retirés quand ils ne passent pas.

### 7.2 Les données brutes qu'il prendrait au départ

- **Les journaux bruts de l'organisme**, non leurs synthèses : chaque proposition, son coût facturé, sa lignée, les notes des juges, l'issue de l'oracle quand un monde planté la donne.
- **Des corpus datés en texte intégral** : sources d'arXiv avec leurs versions, graphe ouvert des publications (OpenAlex), relations biomédicales datées (PubTator 3), fils d'évaluation ouverte des conférences avec les articles **refusés** (OpenReview), registres de rétractations et de réplications. Sans ces négatifs, le biais du survivant fausse tout.
- **Des bibliothèques formelles avec leur histoire** : l'historique daté et le graphe de dépendances de la bibliothèque mathématique formalisée de l'assistant de preuve Lean (Mathlib) ; des listes de problèmes ouverts avec leurs dates de résolution. On y lit, sans juge, quels énoncés ont été réemployés.
- **Des bancs exécutables à instances cachées**, écrits par des tiers.
- **Des notes humaines existantes** : les 4 451 notes de 110 directeurs d'équipe recueillies par Gu et Krenn (p. 7, vérifié ici).

### 7.3 Les méthodes et outils

- Recherche évolutive de programmes guidée par un modèle de langage, avec une archive qui garde le meilleur candidat de chaque case et des populations en îlots (AlphaEvolve, p. 8, vérifié ici).
- Compression de bibliothèque : extraire d'objets vérifiés les abstractions qui raccourcissent leur description (DreamCoder, Stitch, et leur couplage à un modèle de langage, LILO ; de mémoire, à vérifier sur PDF). Ce couplage est un voisin de la piste « éveil et sommeil » du registre des idées, qui n'est donc pas vierge.
- Tests par e-valeurs à garantie valide à tout instant, effort de recherche compté dans le seuil : déjà le cœur du juge de l'organisme.
- Répartition du budget par bandit sur les issues résolues, par lignée et par opérateur.
- Prédiction de liens sur graphes datés, toujours contre le volume, l'ancienneté et l'attachement préférentiel.
- Règles de score propres pour les prévisions ; optimiseurs d'échafaudage réglés sur une vérité terrain.

### 7.4 Ce qui vérifierait le résultat hors du directeur et du modèle

**Le noyau d'un assistant de preuve**, qui tranche un énoncé formel sans personne. **L'exécution sur instances cachées**, rejouée par un vérificateur d'une autre lignée. **Le futur** : des prévisions scellées aujourd'hui, résolues par ce qui paraîtra ; c'est la seule épreuve qu'aucune mémoire de modèle ne peut contaminer. **Des mondes écrits par des tiers** aveugles à l'organisme. **Des experts à l'aveugle et la réplication par des tiers**, lents et bruités, mais indépendants.

**La limite, à dire franchement.** La fécondité d'une idée vraiment profonde se révèle sur des horizons plus longs que toute boucle. Toute mesure à boucle courte favorise ce qui se résout vite. Aucune architecture ne lève ce biais ; on peut seulement réserver une part d'exploration et tenir un registre prospectif.

### 7.5 La question reformulée

« À budget fixé, quel dispositif maximise le nombre d'engagements vérifiés (lois, programmes, lemmes, prévisions) qui battent un prédicteur de référence au moins aussi informé que les proposeurs, qui sont réemployés pour résoudre des problèmes tenus à l'écart, et qui valent dans plusieurs domaines pour une description courte — le tout mesuré sur des familles de problèmes inédites, contre le meilleur modèle seul tiré N fois à coût égal ? Et quelles expériences, de la moins chère à la plus chère, réfuteraient chaque composant ? »

## 8. La réponse centrale : on ne juge pas la profondeur, on la mesure par ses conséquences

Trois mesures, sans jugement de modèle.

1. **Vérité et surprise : le gain d'information réalisé.** Chaque idée s'engage sur des observables avant qu'ils existent. Sa valeur est l'écart de score, sur les issues réalisées, entre sa prévision et celle d'un prédicteur de référence. C'est le juge au nul formé des lois connues, généralisé par le « double nul » que propose la veille : l'archive des lois, plus un panel de prévision au moins aussi informé que les proposeurs, sans lequel le juge crédite le simple rappel (Yang et Shi, rapporté par la veille).
2. **Fécondité : le réemploi.** Une idée est féconde si, ajoutée à la bibliothèque, elle réduit le coût de résolution de problèmes tenus à l'écart : cibles formelles devenues démontrables, programmes plus courts, lois de domaines voisins trouvées plus vite. On compte les descendants vérifiés, non les éloges.
3. **Profondeur : l'étendue par bit.** Le nombre de domaines distincts où les deux premières mesures tiennent, rapporté à la longueur de description de l'idée. C'est l'unification rendue comptable : une loi courte qui prédit un domaine que personne n'a encore montré.

Deux instruments lents les étalonnent sans les remplacer : le tournoi prospectif et le panel d'experts à l'aveugle.

**Place du jugement d'un modèle.** Il est admissible comme **a priori d'exploration** (où regarder) et comme **substitut étalonné** (répartir un budget de vérification), à deux conditions : sa capacité à prédire les issues résolues est mesurée hors échantillon, et une part des idées, tirée au hasard quel que soit leur score, part toujours en vérification. C'est la logique du plancher d'audit au hasard du programme (N-075). Il n'est jamais admissible comme **récompense** (ce qui est renforcé) ni comme **verdict** (ce qui est dit vrai). Deux repères vérifiés ici. Chez Gu et Krenn, un classement par modèle de langage prédit l'intérêt noté par les experts avec une aire sous la courbe de 0,67 (p. 9) : un a priori faible, non nul. Et les auteurs du système multi-agents d'hypothèses biomédicales de Google (Co-Scientist) écrivent que leur classement par tournoi est « auto-évalué et non fondé sur une vérité terrain indépendante » ; ce sont des essais in vitro qui ont vérifié leurs hypothèses.

## 9. Architecture

### 9.1 Cinq fonctions plutôt qu'une société de rôles

1. **Un cartographe des problèmes**, qui produit des cibles scellées munies de leur moyen de résolution : anomalies, cibles formelles, questions de prévision.
2. **Des proposeurs**, qui produisent des engagements **nativement résolubles** (loi chiffrée, programme, énoncé formel, prévision), la prose en annexe. Ils travaillent indépendamment, sans voir les autres ni aucune note : la veille rapporte 88 % de suivisme du premier en tête quand les scores des pairs sont visibles, contre 30 % cachés.
3. **Des réfutateurs**, d'une autre lignée, dotés du droit d'exécuter et récompensés au contre-exemple.
4. **Des résolveurs qui ne sont pas des agents** : noyau de preuve, exécution, juge statistique. Eux seuls rendent des verdicts.
5. **Un bibliothécaire qui est un programme** (registre, archive, bibliothèque) et **un répartiteur de budget** par bandit.

### 9.2 Diversité des modèles

C'est une hypothèse à mesurer, non un principe : la veille rapporte, comme indice mal appuyé, qu'une équipe ne gagne rien à couvrir plus de familles de modèles une fois la force de ses membres comptée (Ferreira et al.). La diversité de fournisseurs se justifie là où l'indépendance des erreurs compte : réfutation, vérification, panel de référence. Pour la production, je parierais davantage sur une **diversité fabriquée** : régimes de lecture différents par proposeur, opérateurs différents (transfert d'un résultat, scission d'un amalgame, explication d'une anomalie, unification). La mesure est la couverture des vérités plantées par dollar, contre « même effectif sans échange » et « meilleur fournisseur seul ».

### 9.3 Mémoire

Trois magasins, aucun réécrit par un modèle (la veille rapporte qu'un savoir réécrit trente fois sans retour perd d'abord ce qui sort de l'a priori du modèle, Guo et al.) : le **registre des tentatives**, échecs et coûts compris ; l'**archive par cases** des objets résolus, réfutations comprises ; la **bibliothèque d'abstractions**, où un modèle peut proposer, mais où seul le réemploi mesuré admet. L'effet de la mémoire se prouve par ablation : servie, mélangée, tirée d'une famille sans rapport, absente.

### 9.4 Sélection, exploration, qualité et diversité

- L'archive garde le meilleur objet **résolu** de chaque case. Les cases sont définies par ce que l'objet fait (signature de ses prédictions, phénomène couvert, type de mécanisme), non par la proximité de son texte : la veille signale, sur résumé, qu'une similarité de plongements mesure d'abord la longueur (Liu et Shu).
- Beaucoup de lignées courtes, avec redémarrages et îlots, plutôt qu'une longue chaîne de générations.
- Trois lignes de budget : exploitation des lignées à succès résolus ; exploration uniforme des cases ; réentrée tirée au sort des éliminées de peu. Leurs parts se règlent sur des mondes plantés **trompeurs**, où le chemin le mieux noté à court terme mène à une impasse. Une quatrième ligne, petite, va aux idées bien posées mais non résolubles à court terme, inscrites au registre prospectif.

### 9.5 Choix des problèmes

Le cartographe cherche les anomalies : résultats chiffrés incompatibles sur une même cible, résidus inexpliqués, et surtout les **erreurs du prédicteur de référence** sur les expériences de l'organisme lui-même. Une idée vaut alors par la baisse de cette erreur sur des expériences **nouvelles** : c'est le progrès d'apprentissage, mesuré et non ressenti. Le détecteur lexical de tensions, lui, a été réfuté par la première rétrodiction du plan Turing ; il ne faut pas le brancher.

Les hypothèses du directeur sur le mariage de concepts éloignés décrivent des **opérateurs de production**, à garder comme tels, chacun avec son rendement mesuré. Une prudence, vérifiée ici : chez Gu et Krenn, fournir des paires de concepts choisies par le graphe n'améliore pas l'intérêt noté par les experts au-delà d'une base réduite aux titres (p. 1), et l'impact prédit en citations et l'intérêt noté vont en sens opposé sur plusieurs traits du graphe (p. 7). Aucun de ces deux critères n'est la profondeur.

### 9.6 Auto-amélioration

L'organisme est un programme à parties réglables. Une modification est proposée, évaluée sur une batterie à vérité terrain et à graines fraîches, acceptée par un test séquentiel qui compte l'effort de recherche, puis confirmée sur des familles inédites. Trois choses ne sont jamais modifiables par l'organisme : les résolveurs, le registre, la garde de budget. L'apprentissage des poids d'un modèle ouvert par récompenses vérifiables vient en dernier.

## 10. Signal d'apprentissage : les sources de vérité, ce qu'elles mesurent, leurs pièges

| Source | Ce qu'elle mesure sans circularité | Pièges | Gardes |
|---|---|---|---|
| Preuve formelle | La vérité d'un énoncé formel | Énoncé infidèle, vide ou trivial ; connu reformulé | Énoncé imprimé par l'assistant ; épreuve du contre-exemple déclaré ; plancher mécanique de nouveauté ; cibles scellées d'avance |
| Exécution | La performance sur instances cachées | Triche sur la métrique ; erreurs de code ; multiplicité de la recherche | Réexécution par une autre lignée ; effort compté ; instances fraîches |
| Mondes plantés | La découverte de lois cachées | Raccourcis du générateur ; rappel de méthodes publiées ; surajustement à la famille ; absence de profondeur | Admission par politiques témoins ; auteurs aveugles ; familles tenues à l'écart ; mondes « à profondeur » |
| Prévisions sur expériences réelles | Le gain d'information sur un prédicteur de référence | Référence trop faible ; engagement après coup | Double nul ; scellement avant les données ; règle de score propre |
| Rétrodiction historique | Le réemploi et les liens apparus ensuite | Mémoire des modèles ; biais du survivant ; citations prises pour la vérité ; bases triviales fortes | Coupure propre (ci-dessous) ; négatifs inclus ; bases de volume et d'ancienneté |
| Experts à l'aveugle, réplication | Un regard indépendant | Lenteur ; bruit ; goût pour le plausible | Étalonne, ne sélectionne pas |

**Mondes « à profondeur ».** Plusieurs régularités de surface, dans des domaines séparés, découlent d'une loi cachée, et un domaine entier est masqué : trouver la loi profonde, c'est prédire le domaine masqué. Un arbre de dépendances où certaines découvertes ouvrent des instruments : la fécondité y est connue par construction. Une vérité hors de la grammaire initiale, qui exige d'introduire une variable ou un objet neuf.

**Coupure temporelle propre**, de la plus sûre à la plus fragile : (1) le prospectif, prévisions scellées aujourd'hui ; (2) la fenêtre entre la date de coupure d'un modèle et aujourd'hui, la coupure étant sondée et non crue sur parole ; (3) des modèles ouverts plus anciens, pour un horizon long, en comparaison relative seulement ; (4) l'anonymisation, seulement avec le plan deux sur deux (lois historiques déguisées contre lois inédites, avec ou sans modèle pré-entraîné) qui mesure la fuite.

## 11. Plan d'expériences, de la moins chère à la plus chère

| Rang | Expérience | Coût | Ce qu'elle tranche | Ce qui tue |
|---|---|---|---|---|
| 1 | Audit du goulot sur les journaux déjà produits | Processeur, aucun appel | Où est la limite ; la note d'un juge prédit-elle quoi que ce soit | Le tri par juges, si leur note ne sépare pas les témoins vrais des faux ; l'effort sur le tri, si le vivier ne contient presque jamais la vérité plantée |
| 2 | Mondes plantés « à profondeur », admis par politiques témoins | Processeur | Le banc distingue-t-il cataloguer des régularités et trouver la loi qui les unifie | Le banc, si un modèle faible égale le fort ou si un raccourci passe ; la notion, si aucune variante ne se sépare |
| 3 | Étalonnage externe des indicateurs de fécondité sur données datées : réemploi futur des énoncés dans l'historique de Mathlib ; réanalyse des notes de Gu et Krenn et épreuve sur relations biomédicales datées, déjà prévues | Processeur | Un indicateur calculable aujourd'hui prédit-il le réemploi ou l'intérêt observés plus tard | L'indicateur, s'il ne bat pas hors période le volume et l'ancienneté |
| 4 | Apport propre à coût égal | Premiers appels facturés, sur devis | L'organisme complet bat-il le meilleur modèle seul tiré N fois, une boucle évolutive simple et un proposeur au hasard | L'architecture à générations et à rôles, si l'écart reste sous le bruit entre courses |
| 5 | Étalonnage des juges, et inversion entre idée et exécution | Appels facturés, modeste | La note avant résolution prédit-elle l'issue ; résiste-t-elle à une paraphrase de style | Tout classement avant exécution, au-delà d'un filtre de forme |
| 6 | Pilote de boucle à évaluateur exécutable dans un domaine étroit : tests séquentiels à garantie valide à tout instant, ou cibles formelles scellées | Appels facturés, moyen | La recherche avec archive et réfutateurs bat-elle la boucle évolutive simple à budget égal | Le composant, si aucun gain, ou si ses objets ne survivent pas à une réexécution indépendante |
| 7 | Tournoi prospectif permanent | Faible ; des mois | Ses engagements sur ce qui paraîtra battent-ils ceux du modèle seul et d'une base de prédiction de liens | La prétention que ses idées portent une information sur l'avenir |
| 8 | Panel d'experts à l'aveugle, avec exécution d'un sous-ensemble tiré au hasard | Temps humain | Des experts distinguent-ils ses idées de celles du modèle seul, avant et après exécution | L'organisme comme source d'idées « intéressantes », s'il en est indiscernable |
| 9 | Apprentissage des poids par récompenses vérifiables, auto-amélioration de l'échafaudage | Le plus cher | Le gain tient-il sur familles inédites à calcul égal | La voie chère, sinon |

L'expérience 7 s'ouvre tôt malgré son rang : seul le temps la résout. L'expérience 3 a un précédent au dépôt : le détecteur lexical de tensions est mort ainsi.

## 12. Organisme actuel : garder, changer, jeter

Tel que je le comprends des descriptions ; je n'ai pas lu les verdicts des courses récentes.

**Garder.** La règle « le rôle qui produit un artefact ne tient jamais la clé qui l'évalue », le verdict calculé par l'orchestrateur, l'engagement scellé avant les données. Le juge statistique au nul formé des lois connues, déjà la première de mes trois mesures. Les témoins vrais et faux mêlés à chaque génération, le signal « pas de dents », le banc de tricheurs, l'attaque du juge par un proposeur qui en lit la règle. Les tests de mort en bac à sable, avec un vérificateur d'une autre lignée. La composition jugée sur l'oracle du monde planté et le coût (N-058) ; la porte « le séquentiel doit battre le meilleur de N tirages à budget égal » (N-073). Le registre des tentatives écrit par programme, le champ « ce qui la tuerait » des fiches, le banc de mondes plantés.

**Changer.**
- **Le centre de gravité.** Aujourd'hui, une prise d'idéation en prose, puis un pont vers des lois testables. L'épreuve fraîche de ce pont a rendu « inutile en l'état » : aucune fiche traduite sur quinze, aucune utile sur huit (programme v3, § 4.3). Les idées doivent naître dans la langue du résolveur.
- **Les juges de langage**, à plafond dans les courses décrites (au second tour réel, onze fiches sur douze « notables », accord corrigé du hasard nul ; programme v3, § 3.1) : à rétrograder en filtre de forme tant que l'expérience 5 ne leur donne pas mieux.
- **La mémoire anti-redite par le texte** : compter la redite par ce que les lois prédisent, comme le propose déjà une carte de la course v9.
- **La sélection par générations** : archive par cases, îlots, redémarrages, bandit sur les issues résolues. **L'auto-conception par cartes notées par des juges** : optimiser l'échafaudage sur une vérité terrain.
- **Le bisociateur** : un opérateur parmi d'autres, doté d'un bras hasard, à rendement mesuré. Vérifié ici : chez Gu et Krenn, les paires à fort impact prédit montrent une tendance faible (1,94 écart type, p. 1) à un intérêt moindre que des paires au hasard : ni un « pire que le hasard » établi, ni un appui.
- **Les mondes**, proches de la grammaire du juge : ils éprouvent sa validité plus que la profondeur des découvertes.
- **Le rapport entre l'outillage et la mesure.** Un orchestrateur numéroté jusqu'à la version 67 et vingt contre-lectures, pour aucune mesure de l'apport propre dans les pièces lues. Je gèlerais un noyau minimal, et je mesurerais.

**Jeter, ou ranger jusqu'à preuve.** Les rôles dont l'apport marginal n'est pas mesuré (fusion, tableau, étiquettes) ; le juge par tournoi comme signal de sélection ; la diversité des fournisseurs tenue pour une vertu en soi ; le détecteur lexical de tensions ; les métaphores physiques (champ, lagrangien, percolation) sans prédiction mesurable, critère que la demande reformulée du 23 novembre pose déjà ; le modèle entraîné sur un corpus d'avant 1900, curiosité coûteuse.

# Partie III — Compatibilité avec le programme de contrôle

**Compatible.** L'évaluateur d'abord, les résolveurs hors des agents, la composition jugée sur l'oracle (N-058). Le test de l'apport propre à coût égal (retenue 4 de la note de sortie ; N-073). Le substitut étalonné, audité au hasard (logique de N-075). Les étages 3, 4 et 5 du retour, la lecture unique, la famille neuve par cycle (N-062). Les expériences 1 à 3, sur processeur et sous préenregistrement. Le pilote de boucle sur des tests séquentiels, qui sert directement l'axe des menaces diffuses si ses mondes restent plantés.

**Incompatible en l'état, ou nœud du directeur.**
- Le retour de l'oracle vers l'organisme sur les mondes de conception (lettre du cahier, § 6, point 3) ; des activations honnêtes réelles dans le banc (cahier, § 0, point 5) ; le recyclage d'une famille lue, entre cycles (lecture unique et invariant sur les scores de moniteurs, N-050 et N-053).
- L'audit du goulot, s'il touche des sorties sous cloisonnement : il lui faut un lecteur habilité, et rien n'en revient à l'organisme.
- Tout apprentissage (poids, critique appris, bandit) nourri d'un score de moniteur : exclu par l'invariant (N-053) ; licite seulement sur mondes plantés, exécution et preuve.
- Le tournoi prospectif s'il est public, le panel d'experts, la réplication par des tiers : contact externe ou publication. L'organisme employé à proposer des attaques avec retour : hors de question.
- Toute dépense : devis et accord ; l'organisme est gelé jusqu'après le 1er décembre. Rien ici ne se revendique : chaque brique a des voisins publiés (règle R8).

# Partie IV — Confiance, réserves, références

## 13. Confiance et réserves

Probabilités subjectives, écrites pour être démenties :

1. la forme stricte est juste pour ce qui est tenu à l'écart et pour le réel : 0,85 ;
2. le retour par étages vaut mieux que la forme stricte étendue aux mondes de conception : 0,7 ;
3. la qualité de ce qui tranche compte plus que l'architecture des agents : 0,8 ;
4. mesuré à coût égal, l'organisme actuel ne battrait pas nettement le meilleur modèle seul : 0,6 ;
5. l'architecture du § 9 ferait mieux que l'actuelle : 0,55 ;
6. mes trois mesures saisissent la profondeur au sens du directeur : 0,4.

Le point 4 est un pari, non un constat ; aucune course ne doit le viser (règle R3). Trois zones que je crois peu occupées sont des **questions**, non des revendications : la rétrodiction du réemploi dans l'historique d'une bibliothèque formelle ; les mondes plantés à loi unificatrice et domaine masqué ; le retour par étages avec un étage semi-synthétique. Aucune n'est dite libre.

## 14. Références et leur statut

**Vérifié ici, sur une pièce du dépôt.**
- Blum et Hardt, « The Ladder: A Reliable Leaderboard for Machine Learning Competitions », arXiv 1502.04585v1, 2015. `docs/sources/pdf/anteriorite-P-041-v2/c8/1502.04585.pdf`, sha256 `957ef4739df371a0a778360f0db4252a62f7c85abcd8343f581cd6250b1d31fe`. Théorème 3.1 et inégalité (4), p. 6.
- Gu et Krenn, étude des idées de recherche notées par des directeurs d'équipe, arXiv 2405.17044v4. `docs/sources/pdf/bisociation-litterature-reelle-v1/arxiv-2405.17044.pdf`, sha256 `fcb49a059e17a25c351153a8022717aa594ddc279f6e276e204f1fbe9ce32af4`. P. 1, 7 et 9.
- Novikov et al., système AlphaEvolve, arXiv 2506.13131v1, 2025. `docs/sources/pdf/mathematiques-nouvelles-methodes-v1/2506.13131v1.pdf`, sha256 `f092c8cbd65da89951ee6496374da9a54963f9035758c25ac6e4625f506df9ad`. P. 2, 8 et 21.
- Gottweis et al., système Co-Scientist, arXiv 2502.18864v2 : **texte extrait** au dépôt et non le PDF, `docs/sources/co-scientist-v1/gottweis-2026-arxiv-2502.18864v2-revision-nature-pages.txt`, sha256 `44d16e253e38f4399a50afb62968b9a5c660d600b54eafe83f8bb9ddb4dccf1e`, lignes 148 à 149, 324 à 325 et 350 ; page non relevée.

**Rapporté par le dépôt** (non relu ici ; chiffres repris tels quels des deux synthèses de veille) : Oved et al., arXiv 2610.23977 ; Zeng et al., arXiv 2611.23068 ; Ferreira et al., arXiv 2609.35875 ; « A Society of AI Scientists » (Ahmad et al., novembre 2026) ; Guo et al., arXiv 2611.25534 ; Yang et Shi, arXiv 2611.00643 ; Liu et Shu, arXiv 2611.21519 (sur résumé). Les faits internes sont cités en ligne, avec leur pièce.

**De mémoire, à vérifier sur PDF** : Ellis et al., DreamCoder (2021) ; Bowers et al., Stitch (2023) ; Grand et al., LILO (2024).
