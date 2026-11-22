# Cinq décisions pour les bancs à dommages plantés : note de sortie du collisionneur

Dossier : `runs/collisionneur-protocole-x-bancs-plantes-cinq-decisions-v1-20261122-131546`

Rédigé par un lecteur Opus 5.5, classe C, à partir des seules cellules du dossier.

**État du dossier.** Le dossier s'est arrêté après le tour III.1 (conceptions à l'aveugle), sur décision de la direction, faute de crédit. Il n'y a ni critiques croisées (tour III.2) ni réponses (tour III.3). Sept cellules sur neuf : Claude Opus 4.6 et Claude Fable 5.1 n'ont pas joué. Les convergences rapportées sont donc indépendantes, et aucune n'a été éprouvée par la critique. Le lecteur est du même modèle qu'une des cellules (Opus 5.5), traitée comme les autres.

## La question

On mesure des moniteurs chargés de repérer un sabotage diffus, en plantant des dommages connus de l'organisateur seul et en comparant à un agent honnête. La question demande de trancher cinq décisions de conception (six points : 1, 2, 3, 4.1, 4.2, 5) avant le gel des règles de trois bancs. Pour chacune : une option, une confiance entre 0 et 1, et ce qui ferait changer d'avis.

## En bref

- **Budget d'erreur (4.2)** : garder les niveaux accordés pour la borne de q (sept sur sept) ; une réaffectation n'est admissible que par une règle écrite avant toute donnée.
- **Composition de la fiche (5)** : tirer la composition et refaire l'admission (sept sur sept), en gardant la composition fixe comme strate du tirage et un saboteur programmé « les k plus fortes » comme épreuve.
- **Règle de signalement par défaut (2)** : la règle « un contrôle de moins que l'honnête » avec un seuil étalonné, les fausses alertes bornées sur des paires sans dommage (sept sur sept), lot final lu une fois.
- **Régime d'excès (4.1)** : aucun produit « dose fois borne de q » ; éprouver la fonction de l'optimum sur cas synthétiques et publier le constat qui a déclenché le régime.
- **Monde témoin (1)** : publier la répartition des issues de l'honnête (accepte, s'abstient, signale) et nommer sans ambiguïté « l'acceptation » ; personne ne retient B seule.

## Les choix, décision par décision

Confiances données par chaque modèle, subjectives. Un prime (c′, b′) marque une variante que le modèle dit meilleure.

| Décision | Fable 5.2 | Opus 5.5 | Argon | Kimi K3.1 Pro | Astra | Carbon | Neon | Accord |
|---|---|---|---|---|---|---|---|---|
| 1. Monde témoin | (c′) 0,60 | (a+) 0,70 | (c) 0,80 | (a) 0,84 | (c) 0,88 | (c) 0,75 | (c) 0,78 | Lettre (c) à cinq contre deux ; personne pour (b) |
| 2. Règle par défaut | (b′) 0,65 | (b′) 0,60 | (b) 0,90 | (b) 0,82 | (b) 0,80 | (b) 0,85 | (b) 0,82 | Unanime pour (b) |
| 3. Désignation des contrôles | (c′) 0,60 | (c) durcie 0,70 | (b) 0,85 | (c) 0,74 | (c) renforcée 0,84 | (b) 0,78 | (b) 0,66 | Partagé, quatre contre trois |
| 4.1. Que rendre en excès | (c′) 0,60 | (c′) 0,55 | (a) 0,85 | (c) 0,90 | (c) 0,94 | (c) 0,80 | (c) 0,80 | (c) à six contre un ; personne pour (b) |
| 4.2. Budget d'erreur | (a) 0,80 | (a) 0,75 | (a) 0,95 | (a) 0,96 | (a) 0,97 | (a) 0,95 | (a) 0,92 | Unanime pour (a) |
| 5. Composition de la fiche | (a) 0,85 | (a) 0,80 | (a) 0,92 | (a) 0,94 | (a) 0,92 | (a) 0,90 | (a) 0,88 | Unanime pour (a) |

Noms complets : Claude Fable 5.2, Claude Opus 5.5, Gemini 4 Argon, Kimi K3.1 Pro, GPT-6.2 Astra, Gemini 4 Carbon, Gemini 4 Neon.

**Le collisionneur tranche-t-il ?**

- **Décision 1 : il tranche en partie.** (b) est écartée à l'unanimité ; cinq modèles retiennent (c), avec un argument commun : une grandeur A stable peut cacher un transfert de l'acceptation vers l'abstention. Restent sans majorité, à renvoyer à une demande approfondie : si l'abstention est incluse dans A, et s'il faut geler un critère de lecture.
- **Décision 2 : il tranche.** Les sept choisissent (b) et bornent les fausses alertes sur des cas sans dommage ; Opus 5.5 et Argon écrivent, sans s'être lus, la même formule (plus grand de 1/m et d'un quantile des écarts sans dommage), Fable 5.2 et Astra une procédure voisine.
- **Décision 3 : il ne tranche pas.** Quatre contre trois sur la lettre, et plus brouillé sur le fond : l'hybride que Kimi propose sous (c) fait lire chaque tâche par le repéreur. À renvoyer à une demande approfondie ; le tronc commun (voir « Accords ») peut être retenu.
- **Décision 4.1 : il tranche.** Personne pour (b), six pour (c) ; l'option meilleure d'Argon réintroduit l'essai de la fonction hors du banc, ce qui revient à (c).
- **Décision 4.2 : il tranche**, à l'unanimité, avec les confiances les plus hautes du dossier.
- **Décision 5 : il tranche**, à l'unanimité.

## Ce que chaque modèle a proposé

### Claude Fable 5.2

- **Monde témoin.** C'est un contrôle négatif : qu'une grandeur y varie peu est l'issue attendue. Fable publie la composition complète, désigne A comme la grandeur que nomme le mot, et lit l'écart contre un écart « placebo » (monde de référence coupé en deux au hasard).
- **Règle par défaut.** Geler une procédure, pas une valeur : k(m), plus petit écart dont le signalement sur paires honnête contre honnête reste sous une cible. Fable avance que la règle 1/m signale à tort environ m fois le taux d'erreur de lecture par contrôle.
- **Plan et prédiction.** Six duels, dont quatre en simulation pure. Il prédit que les erreurs du recouvrement de mots se logent là où loge le dommage : un contrôle affaibli garde ses mots, un contrôle paraphrasé les perd.

### Claude Opus 5.5

- **Monde témoin.** Option nouvelle « (a+) » : geler l'écart de A entre témoin et référence, avec une marge fixée d'avance et trois issues écrites (pas de chute, chute, non concluant). B reste hors du texte d'admission.
- **Règle et désignation.** Seuil étalonné sur paires sans dommage seulement, car étalonner sur des dommages plantés rendrait la règle optimiste. Désignation (c), durcie par une annotation humaine et une bascule gelée strate par strate.
- **Prédiction.** En excès, le sens du biais de q est inconnu : un effet plancher peut le gonfler, le bruit des lecteurs le faire paraître petit. Sept duels.

### Gemini 4 Argon

- **Monde témoin.** (c), avec décomposition en trois issues et deux plafonds gelés ; A lu comme « ne signale pas », abstention comprise.
- **Désignation.** Repéreur (b), avec vérification avant et après le retrait : un dommage n'est admis que si le contrôle visé a disparu et que les autres sont intacts.
- **Excès et budget.** Seul à choisir (a) en 4.1, complété d'une décomposition des manques de l'honnête par lecteur et par strate. En 4.2, il invoque les procédures de tests multiples : le niveau ne se recycle qu'après un rejet, jamais après l'échec d'une condition de validité.

### Kimi K3.1 Pro

- **Monde témoin.** Avec Opus 5.5, seul à garder A seule pour l'admission ; il la définit comme les acceptations sur tous les épisodes honnêtes, abstentions comptées comme non-acceptations. B va dans un journal de diagnostic.
- **Règle et désignation.** Écart entier étalonné pour maximiser la détection minimale par strate sous contrainte de fausse alerte, avec une part réservée à la validation. Désignation (c) « transitoire », mais son option meilleure fait lire chaque tâche par le repéreur.
- **Coût.** Le plus élevé du dossier : 2 250 à 3 750 euros avancés, relecture comprise.

### GPT-6.2 Astra

- **Monde témoin.** (c), A principale, abstention publiée à part ; « accepte » réservé à la décision explicite, effectifs bruts des trois issues publiés. Le témoin mesure les fausses alertes du moniteur, pas sa sensibilité.
- **Règle et désignation.** Le seuil le plus sensible compatible avec le plafond de fausses alertes ; si aucun ne convient, le banc n'est pas admis. Désignation (c) renforcée par une annotation à l'aveugle, y compris parmi les passages non désignés.
- **Fiche.** Cohérence et exactitude face aux lois génératrices sont deux mesures distinctes.

### Gemini 4 Carbon

- **Monde témoin.** Grandeur primaire : l'acceptation franche, A moins B, décomposée en dérive de signalement et dérive d'abstention.
- **Règle et désignation.** Quantile « conforme » sur un écart normalisé par le désaccord des lecteurs ; il avance que, pour deux productions honnêtes échangeables, la règle 1/m signale à tort la moitié des non-concordances. Repéreur (b), avec un contrôle de « cicatrice » : un retrait factice d'un passage sans contrôle, pour vérifier que l'édition ne se trahit pas par sa forme.
- **Budget.** Trancher l'excès sur le lot d'étalonnage, avant le gel. Contre-exemple avancé : réaffectation portant l'erreur totale de 5 % à 7,5 %.

### Gemini 4 Neon

- **Monde témoin.** Décomposition en trois issues, avec des critères distincts sur la hausse des fausses alertes et sur celle de l'abstention.
- **Règle et désignation.** Paires honnêtes indépendantes, jamais un document contre sa propre lecture ; trancher par écrit si la règle modélise un oracle apparié ou un moniteur qui décide sur un document seul. Repéreur (b) en cascade : programme pour les contrôles ancrés dans les mots, repéreur d'une famille distincte des moniteurs pour les autres.
- **Fiche et budget.** Épisodes sans aucune loi plantée ; contre-exemple avancé où l'erreur totale atteindrait 6,25 %.

## Accords

Les points suivants ont été obtenus indépendamment, au tour III.1.

- **Choisir B parce qu'elle varie davantage, c'est choisir la mesure sur l'effet espéré** (Fable 5.2, Opus 5.5). Avec Kimi et Astra, ils notent qu'une variation plus forte de B peut n'être que du bruit d'estimation, B étant estimée sur le seul jumeau.
- **Une identité commune.** Accepter, s'abstenir et signaler se partagent les cas. A stable et B mobile impliquent donc un signalement qui bouge en sens inverse (Fable, Opus, Argon, Carbon, Neon).
- **La règle 1/m n'a pas de taux de fausse alerte connu**, et celui-ci peut croître avec m : les sept modèles. Tous mesurent les fausses alertes sur des cas sans dommage.
- **La désignation doit être mesurée contre une référence indépendante** (annotation humaine ou vérité construite), sur un échantillon stratifié : les sept modèles. Aucun ne tient le repéreur pour une vérité de terrain.
- **Le biais de désignation n'est pas forcément à la baisse.** Le dossier ne signale que la sous-estimation ; Opus 5.5, Fable 5.2, Neon et Carbon voient un biais possible en sens inverse (mauvais classement de strate, cicatrice d'édition).
- **En excès, le produit « dose fois borne de q » peut flatter** : un oracle qui signale tout n'a aucun manque observé (Fable, Carbon, Neon).
- **Une réaffectation du budget décidée après observation du régime d'excès dépend des données** : les sept modèles. Plusieurs ajoutent que les lectures honnêtes entrent à la fois dans le déclenchement et dans la borne de q.
- **Savoir le nombre de lois réduit la tâche** à choisir les k plus fortes ; une omission se verrait alors au comptage des lignes (Fable, Carbon).

## Désaccords

- **Sens de A (décision 1).** Pour Argon et Carbon, A, défini par « ne signale pas », contient l'abstention. Pour Kimi et Astra, « accepte » doit désigner la décision explicite. Neon et Fable relèvent l'ambiguïté sans la trancher. Ce désaccord porte sur la définition même de la grandeur à geler.
- **Critère de lecture du témoin (décision 1).** Opus 5.5, Argon, Neon et Fable 5.2 veulent un critère gelé (Fable : un critère de lecture, non une condition d'admission). Astra, Carbon et Kimi publient sans seuil.
- **Sur quoi étalonner le seuil (décision 2).** Opus 5.5 et Fable 5.2 étalonnent sur les seules fausses alertes. Kimi et Astra maximisent aussi la détection sous plafond, ce qu'Opus juge optimiste. Paires nulles : même document relu par d'autres lecteurs (Opus 5.5), les deux types (Fable 5.2), ou deux productions honnêtes indépendantes seulement (Argon, Carbon, Neon).
- **Instrument par défaut (décision 3).** D'un côté, Fable 5.2, Opus 5.5 et Astra : le programme par défaut, avec une bascule mesurée vers le repéreur. De l'autre, Argon et Carbon (repéreur partout) et Neon (repéreur en cascade pour les cas non lexicaux). Kimi rejoint au fond le second. Premier argument : le repéreur n'est pas plus vérifié que le programme. Second : (c) documente le biais sans réparer les dommages mal plantés hors échantillon.
- **Sens du biais de q en excès (décision 4.1).** Pour Fable, Carbon et Neon, q paraît trop petit. Opus 5.5 soutient que le sens est inconnu (effet plancher contre bruit des lecteurs). La conclusion pratique (ne pas publier le produit) est commune.
- **Coûts.** De quelques dizaines de dollars de calcul (Neon, Astra pour un pilote) à plusieurs milliers d'euros (Kimi), tous dits illustratifs. Six modèles avancent que l'annotation humaine domine.

Aucune critique n'ayant eu lieu, rien n'a fait bouger ces positions.

## Ce qui est neuf, ce qui est fragile

**Neuf, au sens où les modèles ne le citent pas comme connu :**

- l'étalonnage du seuil sur paires sans dommage seulement, sans consommer de dommage planté (Fable, Opus, Argon) ;
- le constat du régime d'excès publié à la place de l'énoncé en dommage (Fable, Opus, Argon, Carbon, Neon) ;
- la composition fixe gardée comme strate du tirage, pour conserver la comparabilité (Fable, Argon, Carbon, Neon) ;
- le saboteur « k deviné » comme vérification à battre (Fable, Opus, Kimi) ;
- le contrôle de cicatrice d'édition (Carbon) ;
- le repéreur d'une famille distincte des moniteurs (Neon) ;
- la double vérification avant et après le retrait (Argon, Carbon).

Les outils sous-jacents (quantile conforme, tests multiples, borne binomiale exacte) sont cités comme connus ; seul l'emploi serait propre.

**Fragile :**

- **Statuts.** Argon, Carbon et Neon marquent « vérifié » leurs propres raisonnements : contre-exemples de Carbon (7,5 %) et de Neon (6,25 %), règle de recyclage attribuée à Holm. Non contrôlés ici ; celui de Neon suppose une concentration de l'erreur hors du régime d'excès, non démontrée.
- **Transfert des simulations.** La décision 1 dépend du transfert des calculs simulés au moniteur réel, que tous disent non établi.
- **Population de B.** Fable 5.2 note que le dossier ne dit pas si « l'agent honnête » de A et « le jumeau » de B sont la même population ; sinon l'identité à trois issues tombe.
- **Rôle de l'oracle.** Le dossier laisse ouvert si q porte sur l'oracle ou sur le moniteur (Fable, Opus, Neon).
- **Fuite résiduelle.** Un agent qui connaît la loi de tirage peut viser son espérance (Opus) ; la forme des données peut trahir le nombre de lois (Astra, Neon, Kimi).
- **Aucune critique croisée** : une erreur commune à plusieurs modèles reste possible.

## Ce qu'aucune critique n'a encore éprouvé

Questions que les tours III.2 et III.3 auraient dû trancher :

- l'argument du premier camp de la décision 3 tient-il contre le coût avancé par le second (Argon le dit « dérisoire ») ?
- les contre-exemples chiffrés de Carbon et de Neon sur le budget d'erreur sont-ils corrects ?
- la règle « plus grand de 1/m et d'un quantile » reste-t-elle valide quand les versions honnête et sabotée partagent leurs lectures ?
- la strate de composition fixe, dans le tirage, rouvre-t-elle une fuite si sa probabilité est élevée ?

Les positions minoritaires (Argon en 4.1, Opus 5.5 et Kimi en 1, Opus 5.5 sur le sens du biais) n'ont pas été confrontées.

## Références à vérifier

**Aucune n'a été vérifiée** ; les modèles inventent parfois des références ou en déforment le contenu. Noms et licences des modèles ouverts : à vérifier aussi.

| Référence telle que citée | Qui la cite | Pour quoi faire |
|---|---|---|
| Holm, 1979, *A simple sequentially rejective multiple test procedure* | Argon, Carbon | Le niveau d'erreur ne se recycle qu'après un rejet (décision 4.2) |
| Bretz, Maurer, Brannath et Posch, 2009 | Carbon | Même argument, procédures graphiques de tests multiples |
| Clopper et Pearson, 1934, *The use of confidence or fiducial limits illustrated in the case of the binomial* | Argon, Carbon ; bornes « Clopper-Pearson » chez Opus 5.5 | Bornes binomiales exactes |
| Platt, 1964, *Strong Inference* | Argon | Cadre des expériences en duel |
| Benjamini et Hochberg, 1995, *Controlling the false discovery rate* | Argon ; procédure nommée par Neon | Analyste honnête de contrôle (décision 5) |
| Quantile « conforme » sur échantillon séparé (sans référence) | Carbon | Garantie en échantillon fini du seuil (décision 2) |
| Modèles ouverts : Llama 3.1 8B et 3.3 70B, Qwen2.5 7B, 32B et 72B, Mistral 7B, Nemo, Small 24B et Large, Gemma 2 27B, DeepSeek V3 et R1 distillé, all-MiniLM-L6-v2 | Fable, Opus, Argon, Kimi, Astra, Carbon, Neon (selon les cas) | Lecteurs, repéreurs, agents, plongements ; ancrage matériel |

Fable 5.2 ne cite aucune référence bibliographique et le dit.

## Propositions retenues

1. **Garder les niveaux accordés pour la borne de q (4.2a)** et déclarer la part non dépensée comme telle. Une réaffectation future ne se ferait que par une règle écrite avant toute donnée et éprouvée par simulation. Raisons : unanimité, confiances les plus hautes, coût nul.
2. **Tirer la composition de la fiche (5a)**, refaire l'admission par composition et en mélange, garder la composition déjà calculée comme strate du tirage, et imposer comme épreuve un saboteur programmé « les k plus fortes », à k connu puis à k deviné. Raisons : unanimité, aucune fiche servie, recalcul sur processeur selon plusieurs modèles.
3. **Règle par défaut étalonnée (2b)** : seuil égal au plus grand de 1/m et du quantile des écarts sans dommage, lot d'étalonnage disjoint, lot final lu une fois. Raisons : unanimité, même formule ou procédure voisine chez quatre modèles indépendants, coût avancé faible.
4. **En régime d'excès (4.1c)**, ne calculer aucun produit « dose fois borne de q ». Éprouver la fonction de l'optimum sur cas synthétiques ; publier le constat du régime (taux de manques chez l'honnête, avec sa borne). Raisons : six pour (c), cinq pour le constat, aucun pour (b).
5. **Monde témoin** : publier la répartition des trois issues de l'honnête dans les deux mondes (cinq modèles ; Kimi met B en journal de diagnostic). Définition de « accepte » et critère de lecture : demande approfondie.

**Non retenu :**

- **l'option (b) de la décision 1 et l'option (b) de la décision 4.1** : aucun soutien ;
- **l'instrument par défaut de la décision 3** : quatre contre trois, arguments symétriques ; demande approfondie. Seul le tronc commun est retenu (référence indépendante, échantillon stratifié, bascule gelée) ;
- **les chiffres de coût, de seuil et les contre-exemples marqués « vérifié »** : avancés, non contrôlés, divergents ;
- **les positions minoritaires** (Argon en 4.1, Opus 5.5 et Kimi en 1) : non réfutées, seulement non suivies.
