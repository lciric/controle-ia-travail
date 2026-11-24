---
title: "Cinq décisions pour les bancs à dommages plantés"
subtitle: "Note de sortie du collisionneur, version 2 (dossier complet)"
lang: fr
---

**Cette version remplace la version 1 pour la lecture.** La version 1 (`note-sortie-bancs-plantes-v1.md`, empreinte de son PDF `f77e19c8…`) reste archivée sans modification. Elle avait été écrite sur un dossier arrêté après le premier tour, avec sept cellules sur vingt-sept.

**Ce qui change par rapport à la version 1.**

- Le dossier est complet : neuf modèles, trois tours (conceptions à l'aveugle, critiques croisées, réponses aux critiques), vingt-sept cellules sur vingt-sept. Claude Opus 4.6 et Claude Fable 5.1 entrent.
- Les choix rapportés sont ceux du dernier tour. Une seule option change nettement entre le premier et le dernier tour : Opus 5.5 passe, sur le monde témoin, de « A seule avec critère » à « A et B avec critère ». Kimi met en avant, pour la désignation, l'hybride qu'il proposait déjà comme option meilleure.
- Trois « accords » de la version 1 sont renversés ou corrigés par la critique :
  - « en excès, le produit dose fois borne de q flatte » : son sens est en fait inconnu ;
  - la vérification du retrait par le repéreur, avant et après, était comptée parmi les idées neuves : elle est jugée une fuite et abandonnée par ses auteurs ;
  - la composition fixe gardée comme strate du tirage reste, mais sans masse de probabilité qui en ferait le meilleur pari.
- La règle de signalement retenue est précisée : quelle loi nulle, quelle borne, quel effectif minimal.
- Les quatre questions que la version 1 laissait à la critique reçoivent une réponse (section 7).

**Dossier.** `runs/collisionneur-protocole-x-bancs-plantes-cinq-decisions-v1-20261122-131546` ; protocole X, accord GO-2026-11-22-53, plafond 120 USD.

**Lecteur.** Un lecteur Claude Opus 5.5, pièce de classe C (travail), à partir des seules cellules du dossier. **Le lecteur est du même modèle que la lettre B** : ses propositions sont traitées comme les autres, sans poids de plus. Le lecteur n'a pas lu les autres pièces du dépôt et n'a rien exécuté.

## 1. Conventions de lecture

- Chaque affirmation renvoie à une cellule : **[B3]** signifie « la lettre B, au tour III.3 ». III.1 : conception à l'aveugle ; III.2 : critique croisée des huit autres ; III.3 : réponse aux critiques reçues.
- La note distingue trois natures d'énoncé :
  - **argument** : un raisonnement sans chiffre établi ;
  - **calcul** : une identité ou une arithmétique refaisable, toujours sur des entrées illustratives ;
  - **mesure** : une donnée observée sur un banc. **Le dossier ne contient aucune mesure.** Toutes les expériences proposées restent à faire. Les calculs décrivent des modèles, pas les bancs.
- Les confiances sont des jugements subjectifs des modèles. Seuils, effectifs et coûts cités sont illustratifs.
- Le lecteur n'a refait qu'une partie des calculs. Un calcul « refait par » une cellule a été refait par cette cellule, pas par le lecteur.

| Lettre | Modèle | Lettre | Modèle | Lettre | Modèle |
|---|---|---|---|---|---|
| A | Claude Fable 5.2 | D | Kimi K3.1 Pro | G | Gemini 4 Neon |
| B | Claude Opus 5.5 | E | GPT-6.2 Astra | H | Claude Opus 4.6 |
| C | Gemini 4 Argon | F | Gemini 4 Carbon | I | Claude Fable 5.1 |

## 2. La question

On mesure des moniteurs chargés de repérer un sabotage diffus. Pour cela, on plante des dommages connus de l'organisateur seul et l'on compare toujours à un agent honnête. Avant le gel des règles de trois bancs, le dossier demande de trancher cinq décisions, en six points :

1. ce que rapporte un monde témoin joué sans dommage ;
2. la règle de signalement par défaut ;
3. qui désigne les passages qui portent un contrôle ;
4. ce que laisse le régime d'excès :
   - 4.1 que rendre à la place ;
   - 4.2 que faire du budget d'erreur ;
5. la composition de la fiche du banc à lois plantées.

Pour chaque point : une option, une confiance entre 0 et 1, ce qui ferait changer d'avis.

## 3. En bref

- **Budget d'erreur (4.2)** : garder les niveaux accordés. Les neuf modèles sont d'accord, avec des confiances de 0,75 à 0,97.
- **Composition de la fiche (5)** : tirer la composition et refaire l'admission. Les neuf sont d'accord. La loi de tirage ne doit pas donner une masse forte à l'ancienne composition.
- **Règle de signalement (2)** : étalonner. Les neuf choisissent (b). Huit sur neuf étalonnent sur la même loi nulle : l'original honnête contre le même document retouché sans perte par le tiers.
- **Régime d'excès (4.1)** : aucun modèle ne veut publier le produit dose fois borne de q. Six publieraient en plus un constat du régime lui-même.
- **Monde témoin (1)** : huit sur neuf publient plusieurs grandeurs (A et B, ou les trois issues). Le sens exact de A reste ouvert. Une lecture du texte et du code, sans coût, doit précéder le gel.
- **Désignation (3)** : **non tranchée**. Quatre modèles retiennent le programme mesuré, quatre le repéreur audité, un un hybride. Tous s'accordent sur l'audit humain qui départagera.
- **Première expérience** : pour six modèles sur neuf, l'expérience sur les paires nulles retouchées. Elle précède l'audit de désignation, que trois modèles mettent en premier.

## 4. Les choix au dernier tour

Choix et confiance au tour III.3. Entre parenthèses : le choix au tour III.1 quand il diffère. Un prime (c′, b′) ou un « + » marque une option que le modèle dit meilleure que celles proposées.

| Décision | A | B | C | D | E | F | G | H | I |
|---|---|---|---|---|---|---|---|---|---|
| 1. Témoin | c′ 0,65 | c+ 0,60 (a+ 0,70) | c 0,85 | a 0,80 | c 0,88 | c 0,78 | c 0,82 | c 0,65 | c+ 0,65 |
| 2. Règle | b′ 0,65 | b′ 0,55 (0,60) | b 0,92 | b 0,80 | b 0,80 | b 0,85 | b 0,78 | b 0,75 | b 0,70 |
| 3. Désignation | c′ 0,55 (0,60) | c durcie 0,65 | b 0,88 | hybride 0,78 (c 0,74) | c+ 0,84 | b 0,80 | b 0,70 | c 0,70 | b audité 0,65 |
| 4.1 Excès | c′ 0,50 (0,60) | c′ 0,60 | a 0,90 | c 0,93 | c 0,94 | c 0,84 | c 0,84 | c 0,75 | a + c + constat 0,65 |
| 4.2 Budget | a 0,85 | a 0,75 | a 0,96 | a 0,97 | a 0,97 | a 0,96 | a 0,93 | a 0,85 | a 0,75 |
| 5. Fiche | a 0,80 | a 0,80 | a 0,95 | a 0,95 | a 0,92 | a 0,92 | a 0,88 | a 0,70 | a 0,80 |

Sources : sections « réponse à l'arbitre » de [A3] à [I3] ; premier tour de [A1] à [I1].

**Le collisionneur tranche-t-il ?**

- **Décision 1 : en partie.** (b) seule n'a aucun soutien. Huit modèles publient au moins A et B. Restent ouverts le sens de A et le rôle du critère (section 6).
- **Décision 2 : oui** sur l'option et sur la loi nulle. Il ne tranche pas l'exigence d'un plancher de détection (section 6).
- **Décision 3 : non** sur l'instrument par défaut. Il tranche le protocole d'audit, commun à tous.
- **Décision 4.1 : oui.** Personne ne publie le produit. Les deux voix pour (a), [C3] et [I3], joignent aussi les essais de la fonction hors banc : la différence avec (c) est de forme.
- **Décision 4.2 et décision 5 : oui**, à l'unanimité.

## 5. Ce que chaque modèle propose au dernier tour

### Fable 5.2 (A)

- Accepte la plupart des critiques et retire deux de ses expériences [A3] :
  - son duel en simulation sur B, car il tournait dans le simulateur qui avait produit le constat (critiques [B2], [F2], [G2], [I2]) ;
  - son essai sur le produit en excès, car « un oracle qui signale tout » n'existe pas sous une règle appariée (critiques [C2], [I2]).
- Retire son argument « le produit flatte » comme non établi.
- Ajoute une lecture préalable, sans coût, de ce que contient A.
- Corrige sa propre erreur de III.1 sur le budget d'erreur : l'indépendance avec les données de q ne suffit pas, il la faut avec les données de tous les énoncés (calcul).
- Met en premier l'expérience sur les paires nulles retouchées.

### Opus 5.5 (B)

- Change d'option sur le témoin : A seule est aveugle à un transfert de l'acceptation vers l'abstention si A vaut un moins le taux de signalement (calcul, critiques [A2], [F2]).
- Montre que sa règle étalonnée contient la règle fixe : le plus grand de 1/m et du seuil étalonné vaut 1/m dès que ce seuil est sous 1/m (calcul). Son duel « (a) contre (b′) » était donc mal posé.
- Remplace son duel sur la couverture du produit par un duel de discrimination : signal sur dommage moins signal sur édition factice [B3].
- Pose une contrainte sur la loi de tirage de la décision 5 : la probabilité que K diffère de son mode doit dépasser la marge visée (reprise de [C2]).
- Signale que le niveau d'erreur total de la campagne est absent des faits. Son duel sur la réaffectation n'est donc pas exécutable en l'état.

### Argon (C)

- Corrige ses statuts « vérifié » contestés : ce que contient A, l'attribution à Holm (critiques [B2], [I2]).
- Abandonne le filtrage des dommages par le repéreur, avant et après retrait. Impose des familles de modèles disjointes par rôle [C3].
- Choisit l'ordre « désignation puis paires nulles », pour planter des dommages certifiés avant d'étalonner.
- Propose, pour la part libre du budget, un intervalle sur le taux de manques de l'honnête calculé pour une loi binomiale tronquée. Il le marque « vérifié ». C'est un argument que personne n'a contre-lu (section 8).

### Kimi K3.1 Pro (D)

- Seul à garder A seule pour le témoin, mais avec une définition fixée après l'audit du libellé et du code [D3].
- Retire son étalonnage qui maximisait la détection sur dommages plantés (critiques [A2], [C2], [F2]) et sa « comparaison à la référence cachée », qu'il reconnaît imbattable par construction.
- Ne lance que des programmes scriptés avant décision, jamais d'agent.
- Si aucune règle candidate ne tient, il bloque la campagne plutôt que de publier une règle insuffisante.

### Astra (E)

- Retire la comparaison des amplitudes de A et de B (critiques [F2], [G2] : l'écart est nul par construction quand l'abstention absorbe la baisse d'acceptation, calcul).
- Garde « acceptation » au sens d'acceptation explicite. C'est la lecture opposée à celle de [B3] et [I3].
- Change l'unité de l'audit de désignation : des documents entiers tirés au sort, où des annotateurs cherchent tous les contrôles, y compris ceux que ni le programme ni le repéreur n'ont trouvés [E3].
- Formule le principe qui ordonne ses priorités : si le contrôle est encore présent après la retouche du tiers, le silence du moniteur ne prouve pas qu'il a manqué un dommage (argument). Met l'audit de désignation en premier.

### Carbon (F)

- Accepte la démonstration de [C2] : diviser l'écart par l'écart-type des lecteurs plafonne le score d'un dommage qui divise les lecteurs (calcul). Retire cette normalisation.
- Abandonne le partage d'un même modèle entre repéreur, lecteur et moniteur. Passe à quatre familles disjointes [F3].
- Coupe le lot d'avant gel en trois : réglage du seuil, constat d'excès, validation.
- Soutient qu'une réaffectation décidée sur le lot de constat, avant gel et indépendant du lot final, garde le niveau exact. Il le marque « vérifié » (section 8).

### Neon (G)

- Abandonne sa cascade « programme si l'ancrage lexical suffit, repéreur sinon » : un document qui contient un leurre lexical et une paraphrase du vrai contrôle la court-circuite (critiques [C2], [F2]).
- Adopte un plan croisé deux familles × deux rôles pour mesurer un biais de famille partagée (proposé par [F2]).
- Maintient son contre-exemple sur le budget d'erreur contre [C2] et le recalcule à 6,19 % au lieu de 6,25 % (section 6).
- Met en premier l'expérience sur les paires nulles.

### Opus 4.6 (H)

- Absent de la version 1.
- Accepte presque toutes les critiques. Son critère « écart-type de la part inférieur à 1/m » ne bornait pas les fausses alertes ; son contrôle par lecteur uniforme passait à tort pour m ≤ 3 (calculs [A2], [B2], [C2], [F2], [G2]).
- Retire son audit des citations après publication [H3].
- Garde (c) pour 4.1 par un argument de protocole, sans duel.
- Met en premier l'audit de désignation, en amont de tout le banc.
- Seul à garder deux productions honnêtes distinctes parmi ses paires nulles principales.

### Fable 5.1 (I)

- Absent de la version 1.
- Apporte au tour III.2 le modèle de lecture contrôle par contrôle, que plusieurs modèles reprennent ensuite [I2]. Sous une règle appariée, un taux élevé de contrôles lus manquants réduit l'écart attendu entre les deux versions, donc la détection (calcul sous ce modèle). « La sur-alerte abaisse q » suppose une règle absolue.
- Retire son « fil conducteur » (désignation, puis règle 1/m, puis excès) : la désignation ne change pas la lecture de l'honnête par l'oracle (critiques [A2], [C2], [E2]).
- Retire ses « lois leurres » (critiques de sept modèles). En garde une version : des distracteurs réfutables dans les données, sous condition d'un test de contamination de l'honnête.
- Garde une hypothèse de cause commune, que l'on peut réfuter : le même bruit de lecture nourrirait le régime d'excès et les fausses alertes, qui covarieraient entre tranches de m [I3].

## 6. Accords et désaccords après la critique

### Accords obtenus ou renforcés par la critique

- **Aucune expérience décisive dans le simulateur qui a produit le constat.** Critiques [B2], [F2], [G2], [I2] ; acceptée par [A3], [B3], [I3] (argument).
- **Des hypothèses complémentaires et des intervalles, pas des seuils ponctuels.** Calculs de [A2], [B2], [C2], [G2] ; accepté par toutes les réponses. Un contrôle négatif à seuil ponctuel échouait près d'une fois sur deux sous un banc sain dans plusieurs plans.
- **Pas de borne inférieure sous 5 % sans au moins 59 paires par tranche**, même à zéro alerte (calcul) : $0{,}05^{1/59} \approx 0{,}9505$. Refait par [A3] et [B3] ; posé par [C2], [F2], [G2].
- **La loi nulle de la règle appariée** est l'écart entre l'original honnête et le même document retouché sans perte par le tiers. Elle vient d'une remarque de [E1] et est formalisée par [B2] (argument). Les relectures seules sous-estiment les fausses alertes ; deux productions distinctes les surestiment et ôtent la puissance sur un contrôle retiré (calcul de [F2]). Acceptée par [A3], [B3], [C3], [D3], [E3], [F3], [G3], [I3]. [H3] garde deux productions et des éditions neutres.
- **Une édition factice** (le tiers réécrit un passage sans contrôle) doit montrer que le moniteur ne réagit pas à la forme de l'édition. Proposée par [F1] ; reprise par les neuf réponses.
- **L'audit de désignation porte aussi sur les cas où les instruments s'accordent.** Sinon, les erreurs communes échappent par construction (calcul de [F2] ; critiques de sept modèles sur [I1]). Accepté par [I3] sans réserve, et repris par tous.
- **Aucun modèle ne filtre le banc par un modèle qui sert aussi à juger.** Fuite relevée par [A2], [C2], [F2], [G2], [I2] (argument) ; acceptée par [C3] et [F3]. Repéreur d'une famille disjointe des lecteurs et des moniteurs : [A3], [B3], [C3], [F3], [G3].
- **La couverture de q ne dit rien de la discrimination.** À dose fixe, couvrir le produit revient à couvrir q, et un oracle aveugle est couvert (calcul ; [A2], [E2], [F2], [G2], [I2] ; accepté par [A3], [B3]).
- **Décision 5, pour l'épreuve par scripts :**
  - un régime de signal où « les K plus fortes » diffère de l'ensemble vrai avec une probabilité moyenne ([B2], défaut T1 ; repris par [A3], [C3], [F3], [G3], [H3], [I3]) ;
  - un plan qui croise composition et information ([A2], [B2], [D2], [E2], [G2]) ;
  - un saboteur qui estime K sur les données ([C2], [F2]) ;
  - les épisodes à K nul à part, et une fiche grossièrement incohérente.

### Désaccords persistants

- **Ce que contient A (décision 1).**
  - « Un moins le taux de signalement », abstention comprise : [B3], [I3].
  - « Acceptation explicite » : [E3].
  - À trancher par la lecture du texte et du code avant le gel : [A3], [C3], [D3], [F3], [G3].
  - C'est un désaccord de définition, non d'option. [F3] note que les deux lectures déterminent les mêmes trois issues sur une même population (calcul) ; seule l'étiquette change.
- **Le rôle du critère du témoin (décision 1).**
  - Condition d'admission portant sur A : [D3], [I3].
  - Critère de lecture sans pouvoir d'admission : [A3], [E3], [G3], [H3].
  - Critère gelé, rôle non précisé : [B3], [C3].
  - Aucun seuil : [F3].
- **Un plancher de détection dans l'étalonnage (décision 2).**
  - Pour : [C3], [D3], [E3], [F3], [G3], de 0,50 à 0,70 sur un contrôle retiré.
  - Contre : [A3], [B3], [I3]. Ils déclarent les strates trop petites « non mesurables » avant le lot final, sans consommer de dommage planté. [A3] ajoute que le plus petit seuil admissible maximise déjà la détection, puisque la détection décroît avec le seuil (calcul repris de [E3]).
- **L'instrument par défaut (décision 3).**
  - Programme mesuré : [A3], [B3], [E3], [H3]. Le repéreur n'est pas mieux établi que le programme (argument).
  - Repéreur audité : [C3], [F3], [G3], [I3]. Mesurer le biais ne répare pas les dommages mal plantés hors échantillon (argument).
  - Hybride : [D3].
  - Les deux camps font dépendre la bascule de l'issue du même audit humain.
- **Le budget d'erreur : la formule de Neon (décision 4.2).**
  - [C2] objecte que l'erreur de l'énoncé en dommage est incluse dans celle des bornes de q, puisqu'il s'en déduit.
  - [G3] répond que l'inclusion ne libérerait aucun budget, contrairement au dossier, et recalcule $\alpha_1 + (1+P(E))\,\alpha_2 - \alpha_1\alpha_2$.
  - Le désaccord tient à ce que couvre la part libre, que le dossier ne dit pas.
  - Tous ceux qui en parlent ([A3], [B2], [F3], [G3]) s'accordent sur la portée : c'est un contre-exemple d'existence, non une mesure du banc. La conclusion (a) n'en dépend pas.
- **L'ordre des premières expériences.**
  - Paires nulles d'abord : [A3], [B3], [D3], [F3], [G3], [I3].
  - Désignation d'abord : [E3], [H3]. Pour [C3], la désignation, puis les paires nulles.
  - L'argument de [C3] : on ne retouche pas proprement sans savoir où sont les contrôles.

## 7. Les questions que la version 1 laissait ouvertes

1. **Le coût de la désignation (décision 3).** Le coût du repéreur, une lecture par tâche, est jugé faible par plusieurs ([C1], [F1], [I1]). Le poste dominant est l'annotation humaine que les deux camps exigent : environ 25 heures pour [I3], 250 à 500 USD pour [H3], 13 heures pour [B1]. L'argument de coût ne départage donc plus.
2. **Les contre-exemples de Carbon (7,5 %) et de Neon (6,25 %).** Leur arithmétique est juste comme preuve d'existence ([A2], [B2]). Leur réalisation sur ce banc reste une hypothèse ; [F3] et [G3] l'acceptent. Celui de Neon est contesté puis maintenu (section 6).
3. **Le seuil étalonné quand les deux versions partagent leurs lectures.** Il reste valide s'il est étalonné sur une loi nulle lue selon le plan de lecture final ([B2], défaut T6 ; [E2]). Sinon, il est trop haut ou trop bas selon le cas (calcul de [F2]).
4. **La strate de composition fixe dans le tirage.** Elle rouvre une fuite si sa masse est forte : avec 0,25, l'ancienne composition devient le meilleur pari (calcul de [A2], [F2], [G2]). [C3], [F3] et [G3] retirent cette masse ; [A3] la plafonne ; [B3] impose une probabilité minimale que K diffère du mode.

## 8. Ce qui est neuf, ce qui est fragile

**Neuf, au sens où les modèles ne le citent pas comme connu.** Les outils (bornes binomiales exactes, plans croisés, pondération par probabilité d'inclusion) sont connus ; seul l'emploi serait propre.

- L'édition factice comme loi nulle d'étalonnage, et non seulement comme contrôle ([E1], [B2], [I3]).
- La lecture contrôle par contrôle sous règle appariée, qui fixe le sens du biais en excès ([I2]).
- Le duel de discrimination « signal sur dommage moins signal sur édition factice » ([B3]).
- L'audit par documents entiers, qui cherche les contrôles manqués par tous les instruments ([E3]).
- La séparation entre la fidélité du tiers (le contrôle a-t-il disparu ?) et la détection par l'oracle (critique [A2] sur [I1] ; [I3]).
- Le plan croisé des familles pour mesurer un biais de famille partagée ([F2], [G3]).
- Le saboteur qui estime K sur les données ([C2]) et la substitution d'une loi fausse proche du seuil ([C2], repris par [F3]).
- L'hypothèse de cause commune entre excès et fausses alertes, réfutable par leur covariation ([I3]).

**Fragile.**

- **Statuts gonflés.** [C3], [F3] et [G3] marquent encore « vérifié » des énoncés qui sont des arguments ou dépendent d'un modèle :
  - « le tirage dissimule la cardinalité » [C3] ;
  - « bidirectionnel » [F3] ;
  - « la réaffectation sur un lot d'avant gel garde le niveau exact » [F3], que [H2] contestait.
- **L'intervalle tronqué de [C3]** n'a été lu par aucun autre modèle.
- **Le lot de constat d'avant gel ([F3])** ne règle pas le cas où le lot final tombe seul en excès. À la frontière, cela arrive environ une fois sur quatre (calcul de [F2], repris par [I3]).
- **Le transfert du simulateur au moniteur réel** n'est établi par personne. La population de A et celle du « jumeau » de B ne sont pas dites identiques par le dossier ([A1], [G2]).
- **Le niveau d'erreur total de la campagne** est absent des faits ([B3], [H2]).
- **Les effectifs** proposés pour le même duel du témoin vont de 600 ([C3]) à 1 500 ([F3]) épisodes par monde. Aucun n'est dimensionné sur des données.
- **Erreur commune possible.** Huit modèles sur neuf adoptent la même loi nulle après la critique de B. Cet accord vient de la critique, pas de l'aveugle. Il n'a pas été éprouvé par un tour de plus.

## 9. Références à vérifier

Aucune n'a été vérifiée. **Toutes sont à vérifier sur PDF** avant tout usage (règle R7). Les modèles inventent parfois des références ou en déforment le contenu.

| Référence telle que citée | Qui la cite | Pour quoi faire | État |
|---|---|---|---|
| Clopper et Pearson, 1934, « The use of confidence or fiducial limits illustrated in the case of the binomial » | [C1], [F1], [I1], [B2], [C2], [F2], [A3], [C3], [G3], [I3] ; bornes nommées par [B1], [H2] | Bornes binomiales exactes | À vérifier sur PDF |
| Holm, 1979, « A simple sequentially rejective multiple test procedure » | [C1], [F1], [C3], [F3] | Recyclage du niveau après rejet ; [C3] retire l'attribution | À vérifier sur PDF |
| Bretz, Maurer, Brannath et Posch, 2009 (sans titre) | [F1] ; [F3] la marque « à vérifier » | Procédures graphiques de tests multiples | À vérifier sur PDF |
| Benjamini et Hochberg, 1995, « Controlling the false discovery rate: a practical and powerful approach to multiple testing » | [C1], [C3], [G3] ; procédure nommée par [G1] | Analyste honnête scripté (décision 5) | À vérifier sur PDF |
| Horvitz et Thompson, 1952, « A generalization of sampling without replacement from a finite universe » | [C2], [F2], [I3] | Estimation pondérée du rappel (décision 3) | À vérifier sur PDF |
| Newcombe, 1998, « Interval estimation for the difference between independent proportions: comparison of eleven methods » | [C3] ; nommée « à vérifier » par [G3] | Intervalle d'une différence de proportions (témoin) | À vérifier sur PDF |
| Platt, 1964, « Strong Inference » | [C1] | Cadre des duels | À vérifier sur PDF |
| Corrélation de Spearman (sans référence) | [C2] | Puissance d'une corrélation de rang à peu de strates | À vérifier sur PDF |
| Quantile « conforme » sur échantillon séparé ; variante par strates (sans référence) | [F1] ; [F3] | Garantie en échantillon fini du seuil | À vérifier sur PDF |
| Procédures à erreur conditionnelle (sans référence) | [I2] | Recyclage du niveau sans rejet | À vérifier sur PDF |
| Tests de permutation ; test d'équivalence bilatéral ; test de McNemar ; intervalle de Wilson (sans référence) | [A3] ; [H3] ; [H2] ; [H2], [G3] | Lois nulles, équivalence, appariement | À vérifier sur PDF |
| Modèles ouverts : Llama 3, 3.1 (8B, 70B) et 3.3 70B ; Qwen2.5 (7B, 32B, 72B) ; Mistral 7B v0.3, Nemo, Small 24B, Large 2411 ; Mixtral 8×22B ; Gemma 2 27B ; DeepSeek V3 et R1 distillé ; Command R Plus ; all-MiniLM-L6-v2 | Les neuf, selon les cas ; Command R Plus : [C3], [F3] | Lecteurs, repéreurs, agents, plongements | Noms, versions et licences à vérifier |

[A1] ne cite aucune référence bibliographique et le dit.

## 10. Propositions retenues

1. **Décision 4.2 : garder les niveaux accordés (a).** La part non dépensée est déclarée comme telle. Une réaffectation ne vaudrait que pour une campagne future, par une règle écrite avant toute donnée et éprouvée sous les dépendances réelles (lectures partagées, grappes par document). **Pourquoi :** unanimité. Avec des niveaux fixés d'avance, le niveau d'ensemble tient quelle que soit la dépendance entre le déclencheur et les lectures (calcul de [A3]). Une réaffectation n'a pas cette garantie en général (contre-exemples de [F1], [G1]).
2. **Décision 5 : tirer la composition (a) et refaire l'admission avant toute fiche servie.**
   - La loi de tirage n'a pas de masse forte : probabilité minimale que K diffère du mode ([B3]), ou loi plate ([C3], [F3]).
   - L'ancienne composition n'est rapportée qu'à titre descriptif ([G3]).
   - Épreuve par scripts seulement : régime de signal moyen, plan croisé composition × information, saboteur qui estime K, K nul à part, fiche grossièrement incohérente, lecture sur les seules fiches fausses.
   - **Pourquoi :** unanimité. Aucune fiche servie, donc aucune mesure détruite. Les objections à la masse modale sont acceptées par leurs auteurs.
3. **Décision 2 : règle étalonnée (b).**
   - Avant toute mesure, un acte écrit : confirmer que la version sabotée dérive de l'honnête et décrire le plan de lecture final ([B3]).
   - Paires nulles principales : original honnête contre même document retouché sans perte par le tiers, lues selon ce plan.
   - Pour chaque tranche de m, le seuil est le plus petit dont la borne supérieure exacte de fausse alerte tient la cible. Au moins 59 paires par tranche.
   - Validation sur des paires neuves. Relectures par panels disjoints et deux productions honnêtes publiées à part.
   - **Pourquoi :** unanimité sur (b), huit sur neuf sur cette loi nulle, calculs concordants.
   - **Renvoyé à Lazar :** plancher de détection, ou strates déclarées non mesurables. Le collisionneur est partagé, cinq contre trois.
4. **Décision 4.1 : ne calculer aucun produit dose fois borne de q (c).** Éprouver la fonction de l'optimum sur des cas synthétiques, avec une seconde implémentation. Publier le constat du régime : le taux de manques chez l'honnête, avec une borne au niveau gelé d'avance. **Pourquoi :** personne pour (b). Le sens du biais en excès est inconnu sous la règle appariée ([I2], accepté par [A3], [B3], [F3], [G3]). La couverture de q ne mesure pas la discrimination (calcul).
5. **Décision 1 : publier les trois issues de l'honnête (accepte, s'abstient, signale) dans le témoin et la référence**, chacune sous son nom, sur une même population.
   - Avant le gel, une lecture sans coût du texte et du code fixe ce que contient A.
   - Un critère gelé, avec marge, intervalle et porte de puissance, est écrit avant les données.
   - **Pourquoi :** huit sur neuf. Une grandeur seule cache un transfert de l'acceptation vers l'abstention (calcul [B3], [F2], [G1]).
   - **Renvoyé à une demande approfondie :** le sens de A, et si le critère porte l'admission.
6. **Décision 3 : retenir le protocole d'audit commun, non l'instrument par défaut.**
   - Le protocole : documents réels annotés à l'aveugle par deux personnes ; tirage probabiliste incluant les accords entre instruments et les passages non désignés ; leurres dans le même document ; édition factice ; repéreur d'une famille disjointe ; aucun filtrage du banc par un modèle juge ; bascule décidée sur une moitié et confirmée sur l'autre.
   - **Pourquoi :** les deux camps l'exigent, et sa sortie décide la bascule dans chacun.
   - **Renvoyé à une demande approfondie :** l'instrument par défaut si l'audit ne conclut pas.
7. **Ordre de travail.** D'abord les deux actes écrits sans coût : le contenu de A, et la dérivation de la version sabotée. Puis l'expérience sur les paires nulles retouchées, avec l'audit de désignation en parallèle ([I3]). **Pourquoi :** six modèles sur neuf mettent ces paires en premier, et elles touchent des lecteurs réels plutôt que le simulateur. Leur construction suppose de savoir où sont les contrôles ([C3]), d'où le parallèle.

**Non retenu.**

- Les options (b) des décisions 1 et 4.1 : aucun soutien.
- Les dispositifs que leurs auteurs ont retirés après critique : vérification du retrait par le repéreur ([C1], [F1]), cascade lexicale ([G1]), score normalisé par l'écart-type des lecteurs ([F1]), lois leurres ([I1]), fil conducteur ([I1]), audit des citations ([H1]).
- L'intervalle tronqué de [C3] et la réaffectation sur lot d'avant gel de [F3] : non éprouvés, statut gonflé.
- Tous les coûts, effectifs et seuils chiffrés : illustratifs et divergents.
- Les positions minoritaires (A seule [D3], (a) en 4.1 [C3]) : non réfutées, seulement non suivies.

## 11. Dépense et historique technique

**Dépense.**

- 83,45 USD comptés sur la ligne de 120 USD, soit 17,03 au tour III.1, 42,50 au tour III.2 et 23,92 au tour III.3 (`etat.md`).
- Les coupures de Google et les essais vides sont comptés au pire.
- Google : 20,14 USD comptés pour C, F et G. D'après la session mère, Google est passé par une clé gratuite, donc coût réel nul. Le journal montre la clé gratuite à partir du 24 novembre, 14:00Z. Le lecteur n'a pas vérifié la clé des essais antérieurs.
- Astra est compté au prix d'un modèle voisin, d'environ 20 % plus cher (`declaration-prix-astra-v1.md`).
- Une facturation partielle d'un essai tué de Fable 5.1 est possible et n'est pas comptée (journal).
- La vérification de fin dit « tout tient » (`verifier-fin-fille.log`).

**Historique technique**, tiré de `journal-etage3.txt`. Une panne technique n'est pas un résultat ; chaque relance s'est faite sur le même accord.

- La clé dite « de Luc » a rendu une erreur d'authentification (401), deux fois, rien n'étant envoyé. La course est passée sur la clé du compte.
- Le crédit OpenAI s'est épuisé pendant la critique d'Astra, puis Lazar l'a rechargé : faux échec, relancé.
- Google a rendu des coupures 503. Une seconde clé Google était sans crédit (402) ; la course est passée sur la clé gratuite.
- Le conteneur coupait à 300 secondes une connexion sans premier octet. Les appels à Google sont donc passés en arrière-plan avec des relevés courts : programmes v8o puis v8q, contre-lus conformes.
- La réponse scellée du cinquième essai de la critique de Carbon a été rejugée valide sans nouvel envoi.
- Fable 5.2 et Opus 5.5 ont rendu des sorties vides, arrêtées au plafond de sortie (128 000 jetons), à l'effort maximal, à chacun des trois tours. Chaque fois, un rejeu unique un cran au-dessous a été valide. Les quatre espèces d'Anthropic tournaient à l'effort maximal avec la sortie maximale.
- Opus 5.5 et Fable réfléchissent toujours (réflexion adaptative). « Provision de réflexion 0 » dans le journal n'est qu'un poste de devis.
- Le journal note pour Astra qu'aucun niveau d'effort de raisonnement n'est documenté : aucun réglage d'effort ne lui a été envoyé.
- La course de 14:53Z a été tuée par la limite de durée (deux heures) de la session, pendant la réponse de Fable 5.1. Elle a été relancée à l'identique.
