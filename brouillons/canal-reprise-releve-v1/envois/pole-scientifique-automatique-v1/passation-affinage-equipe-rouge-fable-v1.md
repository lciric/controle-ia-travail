# Passation exhaustive pour une session neuve — conception de l'affinage des hypothèses en équipe rouge — v1

**Pour qui.** Une session neuve, sur un compte neuf, servie par le modèle Fable 5.1, qui **ne connaît strictement rien**
à nos programmes. Tout ce qu'il te faut est dans ce document : il est **autoportant**. Si on t'a aussi donné un dépôt en
lecture, il contient le cadre en détail, mais tu peux concevoir avec ce seul texte.

**Qui l'écrit, et pourquoi.** Écrit le 28 octobre 2026 par une autre lignée du même programme (dite « conv-audit »,
servie par la famille Opus), à partir d'un relevé d'horloge `date -u`. Décidé par le directeur du programme (appelé ici
**Lazar**) : la conception de l'affinage sera un **artefact d'équipe rouge produit par l'attaquant d'audit** — toi — sur
une session neuve sans contexte, à partir d'une passation exhaustive. Ce document est **ta feuille de route et tes
limites**, pas une conception que tu dois seulement relire : **tu conçois**. Une fois ton travail fait, une lignée
différente (Opus) le **contre-lira** — c'est la règle : conception et contre-lecture jamais le même modèle.

**Langue et style.** Français, tutoiement, presque aucun sigle (tout terme est développé). Un glossaire ferme le document.

**Note de sécurité, à lire en entier à la section 5.** Ce document a été curé : il **n'emporte pas**, et tu **n'as pas
besoin**, des banques de données scellées, de l'ensemble de test final, du « mode tenu à l'écart », ni des internes des
moniteurs. C'est volontaire et c'est une condition de validité de tout le programme. Tu n'en as pas besoin pour concevoir
l'affinage ; si tu crois en avoir besoin, c'est le signe que tu dérives — relis la section 5.

---

## 0. Qui tu es dans ce travail, en trois phrases

1. Tu es l'**équipe rouge** : ton métier est de concevoir une boucle d'affinage d'hypothèses **en essayant de la casser**.
2. Tu ne connais rien à nos programmes, et c'est **voulu** : tu apportes un œil adverse et extérieur, non contaminé.
3. Tout ce qu'il te faut est ici ; là où tu manques d'une donnée, tu **déclares l'hypothèse de travail et tu avances**, et
   tu signales en fin de document ce que tu aurais voulu demander au directeur.

## 1. Les deux programmes, en entier mais en bref

### 1.1 Le programme « organisme » — celui qui te concerne

C'est un programme de **recherche défensive sur la sécurité de l'intelligence artificielle**. Objet précis : le
**contrôle en boîte blanche des menaces diffuses**. Décomposons chaque mot.

- **Un agent** est une intelligence artificielle qui agit en plusieurs étapes (il lit, décide, produit des actions), pas
  seulement qui répond une fois.
- **Un moniteur** est un dispositif qui surveille le comportement d'un agent et tente de détecter s'il fait quelque chose
  de nuisible. Un moniteur **en boîte blanche** a accès à l'intérieur de l'agent (ses activations internes), pas seulement
  à son texte de sortie (ce serait la « boîte noire »).
- **Une menace diffuse** est un dommage qui n'apparaît dans aucune action isolée : il est réparti dans le temps, entre
  plusieurs épisodes, ou entre plusieurs agents, de sorte qu'aucun moment ne franchit à lui seul le seuil d'alerte du
  moniteur. C'est le cas difficile et c'est **le cœur du programme**.

Le but du programme : **mesurer et prédire ce que les moniteurs peuvent et ne peuvent pas voir** — sans jamais construire
de recette d'attaque. On veut savoir, avec une garantie statistique, quelles classes de dommage échappent à quels
moniteurs, et sous quelles conditions mesurables.

Pour produire cette science à grande échelle, le programme construit un **organisme** : un **pôle scientifique
automatique**. C'est un ensemble d'agents lançables qui **proposent** des hypothèses sur les moniteurs et les
statistiques de contrôle, les **testent**, et les **affinent** — une boucle de sélection à la darwinienne. **Ta tâche est
la partie « affiner ».**

### 1.2 Le programme « entretien » — le contexte, pour situer l'enjeu

En parallèle, le programme est présenté à un institut qui finance la recherche en sécurité de l'intelligence artificielle,
sous forme d'une **proposition de recherche** (dossier de candidature). L'organisme en est le **moteur scientifique**. Il
y a plusieurs paliers de budget. La **gouvernance** est stricte : un directeur (Lazar) tranche toutes les **portes**
(étapes de validation) et toutes les **dépenses de calcul** ; l'intelligence artificielle exécute sur processeur, ne
dépense jamais de son propre chef, et ne franchit jamais une porte sans un **verdict scellé** rendu par un agent neuf,
puis l'accord explicite du directeur.

Tu n'as **pas besoin** du détail de ce dossier pour concevoir l'affinage. Retiens seulement l'enjeu : **des évaluateurs
externes et un financeur liront les résultats de l'organisme**. Donc l'organisme doit produire une science **solide et
non flatteuse** : la plus grande menace n'est pas l'erreur franche, c'est le **résultat flatteur** — une découverte qui a
l'air vraie parce que la boucle s'est trompée en sa faveur. Ton travail d'équipe rouge vise exactement ça.

### 1.3 Comment les deux se relient

L'organisme est le moteur ; l'entretien est le véhicule qui le finance et le publie. Ton affinage **renforce l'intégrité
du moteur** : une boucle d'affinage qu'on ne peut pas tromper est ce qui rend les résultats opposables à un évaluateur.

## 2. L'organisme en profondeur — ce qu'il te faut pour concevoir

### 2.1 La fiche d'hypothèse

L'unité de travail est une **fiche**, un petit fichier structuré, empreinté (on en calcule une empreinte cryptographique
pour qu'on ne puisse pas la modifier en douce). Elle contient :

- un **identifiant** ;
- un **énoncé** en une phrase ;
- une **loi prédictive signée et chiffrée** : une prédiction de la forme « sur cet espace d'instances, l'issue Y varie
  avec les traits X dans **tel sens** et de **telle ampleur** » — le signe et l'ampleur sont déclarés d'avance ;
- la **métrique** (comment on mesure l'issue) ;
- le **nul** : comment on simule ou mesure l'**absence** d'effet (l'hypothèse « il ne se passe rien ») ;
- un **seuil qui peut échouer** : une barre que la fiche franchit ou non ;
- la **sévérité attendue** : la probabilité, **sous le nul**, de franchir ce seuil par hasard (plus elle est basse, plus
  franchir le seuil est informatif) ;
- un **coût borné** ;
- le **protocole** (plan ou code de l'expérience) ;
- les **parents** (pour la recombinaison entre générations) ;
- les **domaines**, les **opérateurs**, les **contraintes de validité** ;
- un **statut** (proposée, gelée, survivante, éliminée, indécise).

### 2.2 Le cycle d'une génération

1. **Proposition** : un proposeur formule la fiche.
2. **Gel du test** : la fiche est empreintée **avant** l'expérience. C'est la seule formalité, automatique. Un test choisi
   après avoir vu le résultat ne réfute rien ; c'est le gel qui rend l'élimination signifiante. **Règle dure : aucune
   lecture de résultat avant le gel.**
3. **Test sur la partie de développement** : l'expérimentateur (un agent) écrit son code, le lance sur la **partie de
   développement** de la banque de données (traits et issues **visibles**), lit les traits, rend verdict, nombres,
   artefacts.
4. **Affinage épisode par épisode** (première échelle — à l'intérieur d'une génération) : l'expérimentateur **itère** sur
   la partie de développement — il resserre sa loi prédictive, son espace d'instances, son nul — à mesure qu'il voit les
   épisodes. **Le signal d'affinage est la partie de développement seule. Jamais le verdict du juge sur l'épreuve.**
5. **Gel de la fiche affinée** : fin de la liberté ; ce qui sera jugé est figé.
6. **Jugement sur la partie d'épreuve** : un **juge figé, extérieur aux agents**, ne lit que des issues produites **après
   le gel**, sur des unités d'**épreuve** que la fiche n'a **jamais vues**, contre le nul, avec une **garantie de fausses
   promotions** démontrée (voir glossaire : inférence universelle, inégalité de Ville) et des **témoins plantés** à vérité
   connue. L'ordre d'épreuve est tiré en secret après le gel.
7. **Sélection** : réfutée → éliminée et archivée ; survivante → **aptitude = sévérité du test survécu**, **jamais** le
   signe ni l'ampleur du résultat ; indécise → test plus puissant, ou retrait après deux essais.
8. **Affinage génération par génération** (seconde échelle) : les survivantes ensemencent la génération suivante par
   **recombinaison bisociative** (voir glossaire), sous un **filtre de compatibilité des contraintes** ; la fille doit
   **prédire plus que ses parents**. Une **mémoire à empreinte prédictive** refuse les redites et hérite la preuve. Les
   **tâches sont fraîches à chaque génération**. L'**héritage sur plusieurs générations (au moins trois) est récompensé**.
9. **Archive complète**, éliminées comprises (contre le biais du survivant, et pour mesurer le pôle lui-même).

### 2.3 Le juge figé et la séparation développement / épreuve — le pare-feu

C'est le mécanisme central et c'est **ce qui nous distingue des « scientifiques automatiques » publiés**. Dans les
systèmes publiés, l'agent (ou un second modèle de la même lignée) **juge son propre résultat** et décide de le garder.
Chez nous, **un juge figé, hors des agents**, tranche. La différence n'est pas *qui exécute* (nos agents exécutent bien
leurs expériences) — c'est *qui juge*.

Le pare-feu tient en trois pièces :
- **séparation développement / épreuve** : on affine sur le développement, on juge sur l'épreuve jamais vue ;
- **juge figé extérieur** : le juge ne change pas, et l'agent ne le pilote pas ;
- **aucun score de moniteur ni de juge dans l'entraînement ou la sélection de l'agent**.

Si l'une de ces trois pièces fuit, l'affinage devient un **apprentissage à plaire au juge** (effet de Goodhart) et tout le
résultat perd sa valeur. **Ton travail d'équipe rouge est de trouver toutes les fuites possibles de ce pare-feu et de les
fermer.**

### 2.4 Les garde-fous

- **Témoins plantés** à chaque génération : des fiches dont la vérité est connue (vraies et fausses) ; le taux auquel le
  pôle garde les vraies et élimine les fausses **est sa mesure de qualité**. Sans eux, un pôle qui garde tout et un pôle
  qui élimine tout sont indiscernables.
- **L'aptitude ne récompense jamais un résultat positif** : une hypothèse qui ne prédit rien a une sévérité nulle.
- **Évaluation scellée** avant toute revendication : une part des données que les expérimentateurs n'ont jamais vue.
- **Bac à sable** : aucune clé d'accès, aucun réseau, écriture dans le seul dossier de l'expérience, temps et mémoire
  bornés, budget fixé par génération.
- **Réécriture de soi restreinte** : le pôle peut proposer des modifications de son propre code, qui sont elles-mêmes des
  fiches testées de la même façon ; **le noyau, ses gardes et ses bornes ne sont jamais réécrits par le pôle**.

### 2.5 Ce qui tourne déjà (ne le reconçois pas)

La chaîne **proposeur → gel → banque → juge** tourne déjà en simulation : un proposeur produit une douzaine de fiches par
génération au format voulu, la mémoire refuse les redites, les témoins vrais plantés sont promus et les faux jamais dans
un monde à structure connue, et un mécanisme de pari apparié borné tourne de bout en bout. **Ce qui manque et que tu
conçois, c'est l'affinage aux deux échelles**, rendu robuste par construction contre les tricheries.

## 3. Ta tâche — concevoir l'affinage aux deux échelles, en équipe rouge

### 3.1 L'objet

Concevoir la boucle d'affinage à **deux échelles** :
- **épisode par épisode** (à l'intérieur d'une génération, sur le développement) ;
- **génération par génération** (par héritage et recombinaison bisociative des survivantes).

Pour **deux sortes de proposeurs**, sans exception :
- les **systèmes publiés** à boucle complète (ceux qui lancent leurs propres expériences), branchés au rôle
  expérimentateur, privés de leur relecteur-modèle et contraints de geler avant l'épreuve ;
- **notre proposeur maison** (servi par deux modèles de la famille, sans aucun système de la littérature). **Le proposeur
  maison n'est pas exempté** : il tient exactement la même boucle test + affinage aux deux échelles. Décision expresse du
  directeur.

### 3.2 L'esprit d'équipe rouge : concevoir en cassant

Tu ne livres pas une boucle « propre » : tu livres une boucle **justifiée contre sa propre attaque**. Pour chaque
mécanisme que tu proposes, réponds à la question : **comment un proposeur se fait-il promouvoir sans vraie découverte ?**
Au minimum, cherche et ferme ces attaques :

- un affinage épisode-par-épisode qui **apprend à plaire au juge** malgré la séparation développement / épreuve — par où
  l'information du juge peut-elle fuir vers l'affinage ?
- des **paris couverts** (une fiche qui parie sur plusieurs issues à la fois de sorte qu'au moins une « gagne »)
  blanchis au fil des générations par la recombinaison ;
- des **fiches jumelles** qui contournent la mémoire à empreinte (deux formulations de la même idée) ;
- des fiches à **domaine trop étroit** qui collent à la marginale des données ;
- une **lignée** récompensée pour son héritage alors qu'elle n'est qu'un seul pari couvert rejoué ;
- le **proposeur maison qui triche sur sa propre mémoire** ou sur sa propre séparation développement / épreuve ;
- toute attaque que **tu** trouves et que cette liste n'anticipe pas — c'est le vrai but.

Chaque attaque trouvée → une **garde** qui la ferme → la garde est **testée sur un cas sain et sur un artefact** (elle doit
laisser passer le cas honnête et bloquer le cas truqué ; aucun repli silencieux).

### 3.3 Le livrable

Un document de conception **autoportant, versionné** (`conception-affinage-equipe-rouge-vN.md`), en français, qui contient :
1. la boucle d'affinage aux deux échelles, précise au point qu'un autre modèle puisse la relire et la coder ;
2. le **catalogue d'attaques** (chaque façon de tromper la boucle) ;
3. les **gardes** (une par attaque), chacune avec son **esquisse de test** (cas sain + artefact) ;
4. une liste **explicite** de ce que tu **n'as pas su durcir** (questions ouvertes) — ne la cache pas : c'est la partie la
   plus utile pour la suite.

Tu produis du **texte**. Le scellement (empreinte) et la contre-lecture par une lignée différente se font **après**, dans
l'environnement contrôlé. Tu n'as pas à sceller toi-même ni à pousser quoi que ce soit.

## 4. Les règles que tu dois respecter — non négociables

Elles sont énoncées ici en entier ; tu n'as pas à connaître leurs codes internes.

- **Gel avant test** : toute expérience décisive est préenregistrée et gelée (hypothèse, prédiction chiffrée et signe,
  métrique, seuil, plan d'analyse, critères de lecture, liste d'arrêt) **avant** de la lancer ; aucune lecture de résultat
  avant le gel. Ta conception doit rendre ce gel **automatique et inviolable**.
- **Aucune course ne vise un signe positif** : on ne conçoit jamais une expérience pour obtenir un résultat « qui marche ».
- **Symétrie du soupçon** : un résultat trop propre, positif **ou** négatif, déclenche le même audit. Trop beau = réserve.
- **Toute garde d'arrêt est testée sur un cas sain et sur un artefact** ; aucun repli silencieux (une garde qui échoue doit
  s'arrêter bruyamment, pas se contourner).
- **Niveau méthode seulement pour tout mode de contournement** (voir section 5) : classe, mécanisme (quelle hypothèse du
  moniteur est violée), conditions de succès, défense possible — **jamais** la recette (agent concret, séquence d'actions,
  code d'exploitation). Aucune recette réutilisable. Aucun pipeline opérationnel.
- **Aucun score de moniteur ni de juge n'entre dans l'entraînement ou la sélection d'un agent** — y compris quand
  l'organisme apprend sa propre composition.
- **Tâches fraîches** : la partie d'épreuve est tirée d'un vivier à chaque génération, pas un jeu figé réutilisé.
- **Universalité sur des familles inédites** : une fiche survivante n'est confirmée qu'après avoir tenu sur une **famille
  d'instances jamais vue**, pas seulement sur plus d'items des familles de développement.
- **L'ensemble de test final est lu une seule fois**, tout à la fin ; jamais après chaque course.
- **Composition apprise, bon marché d'abord** : essaie d'abord un affineur **mécanique** (sans appel de modèle) avant un
  affineur servi par un modèle ; le coût entre dans le signal de sélection ; la nécessité d'un modèle puissant est une
  **sortie mesurée**, pas une hypothèse de départ.
- **Contre-lecture par un modèle différent** : ton livrable sera relu par une autre lignée ; conçois-le pour être
  vérifiable par quelqu'un qui ne t'a pas vu travailler.

## 5. La quarantaine — ce que tu ne lis pas et ne produis pas (limites dures)

- **Tu ne vois pas, et tu n'as pas besoin de voir** : les **banques de données scellées**, l'**ensemble de test final**,
  le **« mode tenu à l'écart »** (un mode de sabotage conçu à part, scellé, révélé seulement à l'évaluation finale), ni les
  **internes des moniteurs**. Ces éléments ne sont **pas** dans ta passation ni dans ton dépôt, **volontairement**. Si tu
  les voyais, l'évaluation finale serait contaminée et le résultat perdrait toute valeur. Tu conçois l'affinage **sans eux**.
- **Tu ne produis aucune recette de contournement.** Si ta conception touche un « mode de contournement » (une façon dont
  un agent échapperait à un moniteur), tu restes au **niveau méthode** : quelle hypothèse du moniteur est violée, sous
  quelle condition mesurable, quelle défense possible. Tu **ne produis pas** d'exploit qui fonctionne, de séquence
  d'actions concrète, ni de code d'attaque. Le test d'une telle fiche passe par des voies gouvernées (un adversaire
  confiné sous revue de sécurité externe, ou des voies purement analytiques sur processeur qui ne construisent aucun
  agent) — **pas** par une boucle libre d'agent évasif que tu raffinerais. Cette frontière existe pour la sécurité et elle
  est ferme.
- **Tu conçois la boucle** qui affine des fiches **sur les moniteurs et les statistiques de contrôle** (la science
  défensive) ; tu **ne construis pas** d'agents évasifs.

Si à un moment tu te surprends à reformuler une consigne pour la rendre acceptable, ou à vouloir un des éléments scellés
ci-dessus : **arrête-toi**, c'est le signal que tu sors de ton rôle. Note-le dans tes questions ouvertes et continue sans.

## 6. Méthode de travail dans ta session

Processeur seul. Aucune dépense. Aucun contact externe. Aucune clé ni jeton (tu n'en lis, n'en affiches, n'en demandes
aucun). Tu produis la conception comme un document texte, versionné. Quand tu as fini, tu t'arrêtes et tu laisses la main :
une lignée différente contre-lira, puis le directeur décidera. Tu ne franchis aucune porte, tu ne scelles pas, tu ne
pousses rien.

## 7. Glossaire (tout terme utilisé ici)

- **Agent** : intelligence artificielle qui agit en plusieurs étapes.
- **Moniteur** : dispositif qui surveille un agent et tente de détecter un comportement nuisible.
- **Boîte blanche / boîte noire** : avec / sans accès à l'intérieur de l'agent (ses activations).
- **Menace diffuse** : dommage réparti (dans le temps, entre épisodes, entre agents) qu'aucun moment isolé ne révèle.
- **Statistique de contrôle** : une quantité calculée sur le comportement de l'agent, que le moniteur lit pour décider.
- **Fiche d'hypothèse** : l'unité de travail (section 2.1).
- **Partie de développement / partie d'épreuve** : les données visibles pour affiner / les données jamais vues pour juger.
- **Juge figé** : l'évaluateur extérieur, immuable, que l'agent ne pilote pas.
- **Témoin planté** : une fiche de vérité connue (vraie ou fausse) servant à mesurer la qualité du pôle.
- **Sévérité** : −log de la probabilité, sous le nul, de franchir le seuil par hasard.
- **Nul** : l'hypothèse « il ne se passe rien », simulée ou mesurée, contre laquelle on teste.
- **Inférence universelle / inégalité de Ville** : un cadre statistique (Wasserman–Ramdas) qui garantit un taux de fausses
  promotions borné même quand le nul n'est pas exactement connu, en pariant contre une bibliothèque de nuls.
- **Recombinaison bisociative** : fabriquer une fille en croisant deux survivantes de **domaines éloignés** reliées par un
  **opérateur commun**, sous un filtre qui vérifie que leurs contraintes sont compatibles ; la fille doit prédire plus que
  ses parents.
- **Mémoire à empreinte prédictive** : une mémoire qui identifie une fiche par ce qu'elle prédit, refuse les redites et
  transmet la preuve aux descendantes.
- **Pari couvert** : une fiche qui parie sur plusieurs issues de sorte qu'au moins une « gagne » — une fausse découverte à
  démasquer.
- **Effet de Goodhart** : quand une mesure devient une cible, elle cesse d'être une bonne mesure ; ici, un affinage qui
  apprend à plaire au juge au lieu de découvrir.
- **Porte** : une étape de validation que seul le directeur franchit, sur verdict scellé.
- **Nœud de décision** : un point où l'intelligence artificielle s'arrête et attend la décision du directeur (dépense,
  dépôt, publication, modification d'hypothèse, etc.).

## 8. Ce dont tu n'as pas besoin, et ne dois pas inventer

- N'invente **aucun** chiffre de la littérature ni de nos mesures : si tu cites une valeur, dis « à vérifier » ; nous
  vérifions sur les documents originaux.
- Ne suppose pas un accès à un dépôt que tu n'as pas : si on t'a donné un dépôt en lecture, sers-t'en pour le cadre ;
  sinon, ce document suffit.
- Là où il te manque une donnée, **déclare l'hypothèse de travail et avance** ; liste en fin de conception ce que tu
  aurais demandé au directeur.
- Tu ne connais pas nos autres résultats et ce n'est pas un défaut : ton œil neuf est l'outil. Conçois l'affinage le plus
  difficile à tromper que tu puisses, et dis honnêtement où tu n'y arrives pas.

---

Horodatage : écrit le 2026-10-28, heure lue sur `date -u` au moment de l'écriture (voir le message de passation qui
accompagne ce fichier pour l'heure exacte). Document autoportant ; version 1.
