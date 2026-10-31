# Proposition D — tour III.1

**Convention de statut.** Je qualifie de **VÉRIFIÉ** uniquement ce que la synthèse déclare avoir relu dans le papier ; je n’ai pas moi-même audité ce papier. Les récits des positions de B, C et D sont **RAPPORTÉS** par la synthèse. Toute identification à l’organisme, à la pince ou à l’arène reste une **HYPOTHÈSE** tant que le code, le protocole ou une mesure ne l’établit pas.

## (a) Résolution des divergences

### 1. Valeur de \(n\)

**Je maintiens : \(n\) est non identifiable à partir des pièces servies.** Les valeurs \(n=3\) et \(n=6\) sont des **HYPOTHÈSES**, non des paramètres mesurés.

L’information décisive est le code de l’orchestrateur : définition d’un lot, effectif auquel correspond le \(n\) du modèle, croissance éventuelle \(n\to2n\), capacité, moment du comptage et règle de répartition entre filles. Une moyenne observée de fiches par lot ne suffirait pas si la taille varie ou si le lot de l’organisme n’est pas la protocelle du modèle. En conséquence, aucun seuil dépendant de \(n\) ne doit être préenregistré comme prédiction de la course 2 avant cet audit.

### 2. Identité de \(q\)

**Je maintiens que \(q\) n’est pas identifié, mais j’accepte la définition de C comme candidat conditionnel.** Si le noyau à deux parents est validé, \(q_{vv}\) peut désigner la probabilité qu’une paire vraie–vraie produise une descendante fonctionnelle vraie ; ce n’est pas encore le \(q\) scalaire du papier.

Tant que \(q_{vf}\), \(q_{ff}\), la reproduction à un parent et la génération spontanée ne sont pas mesurés, réduire ces issues à un seul \(q\) est une **HYPOTHÈSE** supplémentaire. Il faut aussi un typage indépendant des parents et des produits : un score attribué par le même modèle que le bisociateur ne suffit pas. Le scalaire du papier ne devient pertinent que si les autres voies fertiles sont nulles ou négligeables à un seuil préenregistré, et si la fidélité est suffisamment stationnaire.

**Duel d’identification, commun aux points (a)2, (a)4 et (a)5.**  
\(H_A\) : seule la voie *trans* vraie–vraie est fertile ; les voies *cis*, vraie–fausse, fausse–fausse et spontanée ont chacune une probabilité \(\leq\delta\).  
\(H_B\) : au moins une de ces voies alternatives a une probabilité \(>\delta\).

- **Métrique :** taux de descendantes fonctionnelles par essai, par type de paire, avec juge indépendant ; \(\delta\) est fixé avant les données à partir du bruit mesuré du juge et du rembourrage inerte.
- **Contrôle négatif :** absence de parent, rembourrage inerte de même longueur et produits copiés sans bisociation.
- **Issues :** une borne inférieure d’intervalle \(>\delta\) sur une voie alternative falsifie \(H_A\) ; des bornes supérieures \(\leq\delta\) sur toutes les alternatives, avec une voie vraie–vraie positive et des contrôles valides, falsifient \(H_B\) **à l’échelle de détection choisie**. Elles ne prouvent pas une stérilité universelle.

### 3. Pince et arène

**(i) Je maintiens qu’aucune prédiction du papier n’est actuellement testable dans la pince.** La condition nécessaire du levier citée par C ne devient applicable qu’après démonstration que la pince réalise bien la règle de division correspondante.

Le levier décrit dans la synthèse conserve des paires lors d’une division ; un juge qui promeut des fiches individuelles n’en est pas une instanciation par construction. La candidate conditionnelle serait la condition nécessaire sur \(\bar r\) — synthèse, section 4, P9 : p. 68, l. 4991 — et non une condition suffisante de maintien de la défense. Le test préalable doit donc mesurer la rétention conjointe des paires et comparer une division réellement aveugle à une division fondée sur le contenu. Sans cette correspondance, P9 teste l’ingénierie de la pince, pas le papier.

**(ii) Dans l’arène adaptative, je maintiens l’inapplicabilité par défaut.** Un régime couvert par le modèle reste possible, mais seulement dans une arène expérimentalement figée : générateur et défense gelés, paramètres stationnaires, classes et poids mesurés, population et division contrôlées, injection exogène connue.

Cette arène figée serait une instance artificielle du modèle, non une validation de son application à l’arène ordinaire. La non-stationnarité seule n’interdit pas des fenêtres figées ; elle interdit de transposer sans réserve un rayon spectral stationnaire à la trajectoire adaptative complète.

### 4. Extinction quadratique à fécondité infinie

**Je modifie partiellement ma position du tour 1.** À fécondité infinie, une loi de vitesse qui ne fait que reparamétrer le temps n’est effectivement plus nécessaire si l’extinction est énoncée pour la chaîne de types ; en revanche, le seul compte de naissances vraies en \(O(1/N^2)\) ne démontre toujours pas l’extinction sans préciser remplacement, dilution et nombre d’essais par événement.

L’extinction tient dans un noyau explicitement défini avec tirage non assortatif des deux parents, absence d’autoappariement fertile, \(q_{vf}=q_{ff}=0\), aucune injection ou copie spontanée, et règle de remplacement qui empêche l’accumulation protégée des vraies. Elle tombe, ou doit être recalculée, si une voie hybride est fertile, si les vraies s’associent préférentiellement, si des lots conservent les paires, ou si le nombre d’essais par remplacement dépend de la composition. Ainsi, je retire l’objection portant sur le seul temps physique, mais pas celle portant sur le noyau probabiliste incomplet.

### 5. Source de la première mesure

**Je maintiens la priorité à une expérience prospective, après audit et préenregistrement, avant toute lecture des journaux.** Les journaux pourront ensuite servir de réplication ou d’analyse exploratoire, sans modification des seuils.

Les journaux existants introduisent un risque de choix des comparaisons informé par les issues, une puissance insuffisante et des confusions propres à la course 2 — injection, consommation des parents, évolution du vivier. Des appels nouveaux non randomisés introduiraient eux aussi un biais : changement de distribution, de versions ou de protocole, donc impossibilité d’attribuer directement le résultat à la course 2. La conception prospective doit donc geler les versions et inclure les contrôles, plutôt que simplement produire de nouveaux appels.

### 6. Destruction contre archivage

**Je maintiens l’archivage en quarantaine, sans réinjection.** Si l’archive est réellement inaccessible au vivier, destruction et archivage ont la même dynamique ; aucune expérience sur \(\rho\) ne peut les distinguer.

La mesure décisive est donc double : une mesure séparée de \(q_B\) et de l’avantage reproductif effectif \(\theta'\), qui détermine si une réinjection pourrait être envisagée, et un audit de confinement de l’archive. Une réapparition d’un fragment archivé dans le vivier falsifie l’équivalence dynamique. L’intérêt probatoire et les coûts de conservation sont des choix d’ingénierie, non des théorèmes du papier.

## (b) Politique consolidée sur les fusions inachevées

### 1. Acceptation et modification

**J’accepte la politique, avec une modification importante : la condition sur \(\theta'\) autorise seulement un test du bain, elle ne justifie pas sa recommandation.** La garde dans le vivier ne devrait être adoptée que si elle montre un gain contre la quarantaine à fécondité et conditions comparables.

Le seuil \(\theta'<2(1-\tau)\) est une condition de domaine du bain, pas une preuve de bénéfice — synthèse, section 6 : p. 59, l. 4286. La perte des inachevées multiplie la fécondité requise par \(1/(1-\tau)\), mais ne coûte rien sur la charge à fécondité infinie — synthèse, section 6 : p. 8, l. 703 et p. 10, l. 863. Enfin, le comparateur de la p. 59 était « copies rapides seules, copies lentes perdues », non « rejet de toutes les inachevées » : c’est la correction I12.

La mesure de \(q_B\) doit pouvoir inclure, dans une épreuve isolée, les appariements \(B+B\) et \(F+B\). L’interdiction d’apparier deux brouillons concerne le vivier et la réinjection ; sinon \(q_B\) ne serait pas identifiable. Si un brouillon produit des descendantes fonctionnelles, il faut le modéliser comme un type distinct, pas comme un parasite stérile.

### 2. Testabilité avant lecture des journaux

**Les trois options sont testables prospectivement avant lecture, mais la garde conditionnelle n’est pas éligible avant les mesures séparées de \(\theta'\), \(q_B\) et \(\tau\).** Aucun de ces tests n’exige les journaux de la course 2.

Détruire et archiver peuvent être comparés comme politiques de confinement ; leur équivalence dynamique se teste par audit et contrôle de fuite. Le bain contrôlé et la quarantaine peuvent être comparés dans un run prospectif à capacité fixe. Ce qui serait impossible sans journaux, c’est seulement d’estimer rétroactivement l’effet de ces politiques **dans la course 2 déjà réalisée**.

**Duel décisif sur le vivier.**  
\(H_A\) : le vivier n’apporte aucun gain, \(\Delta\rho=\rho_{\text{vivier}}-\rho_{\text{quarantaine}}\leq0\).  
\(H_B\) : il apporte un gain, \(\Delta\rho>0\).

- **Métrique et seuil :** \(\rho\) au niveau des lots, estimateur étalonné, seuil \(0\), horizon et effectifs fixés avant les données.
- **Contrôle négatif :** rembourrage inerte apparié en longueur et en exposition, sans re-troncation ; bras supplémentaire avec brouillons réellement inertes.
- **Issues :** une borne inférieure de \(\Delta\rho>0\) falsifie \(H_A\) ; une borne supérieure \(\leq0\) falsifie \(H_B\). Un intervalle couvrant \(0\) est un défaut de puissance, pas une victoire par défaut du bain.

### 3. Papier ou cadrage ?

**Je ne peux pas affirmer rétroactivement que le cadrage n’a pas compté : le « t’es sûr ? » invitait explicitement au doute.** Je retire donc toute interprétation de mon accord comme preuve indépendante.

Ce que je conserve sur le texte est limité : les identités sur la perte et les copies recopiables, et les trois sorts possibles des inachevées — synthèse, section 6 : p. 56, identités (i) et (ii), et p. 16, l. 1542-1543. Ces passages réfutent une règle universelle « toujours jeter » ; ils ne prescrivent pas l’archivage. Mon choix d’archiver vient de l’option de mesure conservée, donc d’un argument d’ingénierie.

## (c) Prédictions et ordre des travaux

### 1. Tri des douze prédictions

| Prédiction | Classe | Décision et correction |
|---|---|---|
| **P1** | **F** | Remplacer \(n=6\), \(R\) et \(U\) supposés par les valeurs du code ; utiliser le noyau exact ou les bornes applicables, et un estimateur spectral étalonné. Le seuil \(0,40\) ne doit pas passer pour une valeur générale du papier. |
| **P2** | **F** | Séparer les tests de \(q_{vf}\), \(q_{ff}\), du *cis* et du spontané ; préciser le juge et les contrôles. Un intervalle dans \([0;0,02]\) établit au plus une équivalence à cette tolérance, pas la stérilité exacte. |
| **P3** | **S** | Retenir la version D : seuil \(\delta\) fixé par simulation avant les données, juge indépendant et rembourrage inerte. Retirer la formulation « sans coût » de B. |
| **P4** | **F** | I12 supprime la motivation « bain supérieur au rejet ». Remplacer \(n=6\) par le \(n\) audité, définir opérationnellement \(\theta'\), recalculer le noyau et recentrer l’hypothèse sur \(\Delta\rho\), non sur une supériorité présumée. |
| **P5** | **S** | Duel vivier contre quarantaine, seuil \(0\), capacité fixe et estimateur étalonné. Les mesures préalables de \(\theta'\) et \(q_B\) sont des conditions de déclenchement. |
| **P6** | **A** | Version moins identifiée et moins puissante de P5, sans taille d’effet fixée. Conserver seulement son calcul de puissance comme contribution méthodologique. |
| **P7** | **S** | Duel \(\rho>1\) contre \(\rho\leq1\), injection exogène exclue par le code, persistance sur horizon scellé. Une extinction observée falsifie l’allumage endogène sur ce régime ; une croissance transitoire seule ne le confirme pas. |
| **P8** | **S** | Préenregistrement **conditionnel**, activé seulement après validation du noyau et identification de \(q\). Une persistance dans le domaine d’extinction falsifie le transfert ; une extinction ne valide pas à elle seule toute la correspondance. |
| **P9** | **A** | La correspondance juge–levier n’est pas établie. À reconcevoir seulement après démonstration que la pince réalise la règle de division et mesure le \(\bar r\) pertinent. |
| **P10** | **S** | Test asymétrique : un contre-exemple reproduit falsifie H2 ; une marge certifiée ne ferme que les boîtes traitées. Un échec de certification ne falsifie pas H2. |
| **P11** | **A** | Prédiction qualitative non signée, remplacée par P7 et P8. |
| **P12** | **A** | Tests d’ingénierie hors papier, non prédictions du modèle. Leur contenu peut être recyclé en validation d’instruments, sans statut de test des théorèmes. |

### 2. Ordre des travaux

**Je conserve les préalables de la section 8, mais je déplace la lecture des journaux après les mesures prospectives.**

1. **Audit du code et du confinement** : \(n\), division, consommation des parents, injection, tirages, \(\theta\), \(\theta'\), archive.
2. **Étalonnage des instruments** : juge, estimateur spectral et contrôles mécaniques. Si \(\rho<1\) et \(\rho>1\) ne sont pas distinguables aux effectifs disponibles, déclarer la course 2 non jugeable pour l’allumage avant toute lecture.
3. **Noyaux exacts aux petites tailles et calculs de puissance**, en parallèle ; certification H2 comme chantier processeur indépendant.
4. **Préenregistrement scellé et contre-lu**, puis devis et GO.
5. **Runs prospectifs** : d’abord *cis/trans* et typage des paires, ensuite \(\theta'\)/\(q_B\), puis P5 ; P7 lorsque l’injection est effectivement contrôlable.
6. **Lecture des journaux**, sans modification des seuils, comme réplication ou exploration.

### 3. Recodage des noyaux exacts

**Difficulté : modérée pour le noyau exact à petite taille et fécondité infinie, si le papier complet est disponible ; impossible à garantir avec la seule synthèse.** Celle-ci ne contient pas toutes les définitions nécessaires de \(B\), \(H\), des conditions de division et des cas à fécondité finie.

Le recodage doit être vérifié contre les valeurs déjà relevées, notamment \(U_c(3)=0{,}450266\), et contre les limites analytiques — synthèse, section 9 : p. 42, l. 2880-2896. Les extensions avec bain, re-troncation et fécondité finie seraient **difficiles**, car elles demandent davantage que le calcul d’une valeur propre.

### 4. Effet des inexactitudes majeures

**Oui : I12 change P4 de formellement signée à F.** Le duel reste utile, mais son interprétation et son comparateur doivent être réécrits ; il ne devient pas A, car une comparaison directe vivier–quarantaine reste informative.

I4 et I10 imposent d’écarter les valeurs issues de \(R_{\min}\simeq0{,}22n\) hors domaine asymptotique ; elles contribuent à P1 = F et P11 = A. I11 était déjà corrigée en condition nécessaire dans P9, mais cette correction ne répare pas la correspondance avec la pince.

### Instruments et ancrage matériel

- **Juge et bisociateur :** mesurer taux de détection des produits fonctionnels et taux de fausses alertes sur des cas honnêtes appariés par longueur, format et difficulté, avec vérité fonctionnelle indépendante. Ils doivent battre les vérifications mécaniques : schéma et syntaxe, tests exécutables, copie exacte d’un parent, règle fondée sur la longueur. Les contrôles sans parent et à rembourrage inerte fixent le taux de fausse fertilité.
- **Estimateur spectral :** sur matrices simulées à \(\rho=0{,}95\) et \(1{,}05\), mesurer détection du bon côté de \(1\) et fausses alertes d’allumage. Inclure des cas où moyenne par mère et valeur propre de Perron divergent ; l’estimateur doit battre cette moyenne naïve.
- **Orchestrateur :** tests unitaires avec graines et issues connues pour consommation des parents, poids de tirage, répartition des filles, injection et fuite d’archive. Une documentation sans test reproductible reste **OBSERVÉ-NON-AUDITÉ**.

**Ancrage proposé :** bisociateur et juge à poids ouverts, de familles distinctes, versions gelées, exécution locale pour les contrôles ; calcul CPU pour les petits noyaux, simulations de puissance et certification par intervalles, calcul GPU seulement si l’inférence locale l’exige. Ordre de grandeur **illustratif**, aucun prix n’étant fourni dans les faits : quelques jours CPU, 16–64 Go de mémoire, et quelques centaines à quelques milliers USD selon le nombre de runs et la location GPU ; les appels payants restent conditionnés à un devis et à un GO.

FIN-DE-CELLULE