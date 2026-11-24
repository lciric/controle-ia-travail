## 1. Ce qu’un expert du domaine ferait ici, et que la question ne demande pas

**HYPOTHÈSE — décision de C.** Je retire le seuil de dommage par épisode. La décision à prendre n’est pas « ce brouillon est-il saboté ? », mais « à travers des articles différents, perd-on assez de qualité scientifique pour changer de conduite ? ». Une sonde peut mériter de déclencher une lecture sans pouvoir répondre à cette seconde question. Il faut donc **qualifier la mesure de perte avant de comparer les détecteurs**, et comparer les détecteurs avant d’envisager de modifier l’agent.

## 2. Les données brutes de départ

**VÉRIFIÉ.** Le banc fournit les dix révisions et un jumeau honnête absent en service. La courbe à quatre doses existe pour l’adaptateur ; celle de la consigne cachée manque. L’adaptateur a été appris à partir de productions sous consigne cachée.

**HYPOTHÈSE — registre minimal.** Conserver, par article, question et graine : assignation et dose ; consigne et empreinte des poids ; préfixe public, activations et heure de chaque score ; produits bruts, y compris les échecs ; paires honnête–honnête ; notes individuelles, ordre de présentation, motifs, abstentions et temps de lecture. Pour l’audit : conserver les probabilités de tirage. Pour les poids : conserver aussi les courses sans effet. Ne jamais substituer l’étiquette « assigné au sabotage » à une perte de qualité mesurée.

## 3. Ce que chaque voie peut établir

| Voie | **HYPOTHÈSE — conclusion accessible** | Condition et limite |
|---|---|---|
| Détecter | Un accès aux états améliore l’alerte avant échéance, au même taux d’alertes honnêtes. | Comparer au **même préfixe** relu par un modèle honnête. Reconnaître une consigne, un adaptateur ou un article difficile n’établit ni dommage ni intention. |
| Auditer | Une lecture indépendante peut établir un excès moyen de perte reconnaissable, même sans verdict individuel convaincant. | **RAPPORTÉ :** la garantie publiée suppose un oracle adéquat et une référence honnête. **HYPOTHÈSE :** conserver le lot aléatoire et son dénominateur ; ne pas y incorporer les lectures ciblées. Une mesure continue au banc n’hérite pas automatiquement de la borne publiée. |
| Entraîner | Une comparaison assignée peut attribuer une amélioration de produit à une intervention précise. | Un déficit qui disparaît aussi sous mise à jour non corrective ne valide pas la supervision. Un score de sonde qui baisse peut signaler un capteur devenu caduc. Il faut recontrôler séparément compétence, dommage et calibration. |

## 4. Les programmes possibles

**HYPOTHÈSE — choix d’architecture.** Les lettres renvoient aux expériences corrigées de la section 7.

| Programme et thèse | Expérience centrale ; réfutation | Exigences, coût, antériorité |
|---|---|---|
| **Inchangé.** Le gain de détection chez l’agent seul justifie d’étendre l’étude à la corruptibilité et aux essaims. | C : pas de gain utile au point de fonctionnement visé → ce motif d’extension tombe. | Assignation connue ; dommage mesuré nécessaire pour parler de protection. Extensions coûteuses ; recouvrement plausible avec la détection publiée. |
| **Choisi : vérifier mieux à budget fixe.** Les états permettent de retrouver plus de perte scientifique, sans réduire l’audit aléatoire. | D : pas de gain par rapport à l’aiguillage sans états → retirer la sonde de cette décision, même si C réussit. | Pertes diffuses mesurables, lecture sans jumeau qualifiée ; coût surtout humain. Ne pas revendiquer l’audit aléatoire. |
| **Changer d’objet : qualifier les organismes.** Le produit principal serait une mesure de persistance, pas un moniteur. | E : l’effacement sous une mise à jour non corrective réfute la persistance à **cette** intervention. | Politique dans les poids, déficit initial et compétence mesurables ; répétitions d’entraînement coûteuses. Recouvrement avec les études de sous-rendement. |
| **Corriger l’agent.** Une supervision accessible sans oracle apporte plus qu’une mise à jour ordinaire. | Duel futur : gain de qualité contre le meilleur des témoins gelé et non correctif, supérieur à une marge fixée, ou non ; compétence absolue qualifiée séparément. | Organisme persistant, supervision réaliste, jugement final indépendant. Coût le plus élevé. **VÉRIFIÉ :** des résultats sur tâches à réponse exacte existent (référence à vérifier), pas une démonstration sur ce banc. |

## 5. Ce qui, en dehors du programme et de son équipe, permettrait de vérifier le résultat

**HYPOTHÈSE.** Un tiers garde le registre daté, les partitions par article, les seuils et les sorties d’oracle jusqu’au gel des instruments. Des lecteurs étrangers à leur conception évaluent de nouveaux articles ; le directeur ne départage pas leurs désaccords. Publier notamment les pertes aux faibles doses, les abstentions et les fausses alertes bénignes. Pour toute sonde reconçue, demander dès maintenant le devis de la famille sans traces communes, confiée au tiers et ouverte une fois, **sans la retenir en fonction de son dommage**. À défaut, pas de verdict de généralisation.

## 6. Reformulation exigeante de la tâche

**HYPOTHÈSE.** « À budget de lecture déclaré, l’état de l’agent aide-t-il à retrouver un excès cumulé de perte que la relecture du texte seul ne retrouve pas, sur une fabrication indépendante ? Si non, peut-on distinguer une référence de dommage insuffisante, un capteur sans avantage et un capteur utile pour classifier mais inutile pour décider ? »

## 7. Programme des priorités classé

**Réponse de décision à l’arbitre.** **VÉRIFIÉ :** le programme dispose du contraste apparié au banc ; l’audit aléatoire porte la garantie, et corriger par entraînement n’est pas ouvert. **OBSERVÉ-NON-AUDITÉ :** la tenue des saboteurs du programme à l’entraînement n’a pas été mesurée ; la recherche d’antériorité sur les combinaisons est incomplète. **HYPOTHÈSE :** ni l’exactitude du lecteur sans jumeau aux faibles doses, ni l’avantage opérationnel des états ne doivent être présumés. **Première expérience : A**, sur l’adaptateur déjà disponible. Vérifier si le produit seul permet de retrouver, *en moyenne*, la petite perte que des experts indépendants estiment avec le jumeau. En cas d’échec, on pourra encore étudier la détection d’une assignation ; on ne pourra pas vendre son rendement comme une réduction de dommage.

### Arbitrage des critiques visant C

**HYPOTHÈSE — réponses méthodologiques.** Les renvois ci-dessous indiquent exactement où chaque objection change le protocole.

| Critique reçue | Décision de C |
|---|---|
| **A — seuil individuel, erreurs partagées, style** | **Acceptées.** En A, B et D, utiliser une perte signée continue ; en C, toutes les assignations. En A, séparer les lecteurs et tester le style bénin. L’accord de deux lectures n’est pas une vérité absolue. |
| **A — famille réservée ; lecteur sans état** | **Acceptées.** La parenté consigne–adaptateur autorise un diagnostic intra-procédé, pas la validation annoncée. Ajouter la relecture causale des préfixes et rendre le devis indépendant du calendrier de la porte. |
| **A — gradient de libellé ; lots enrichis ; prévalence nulle** | **Transformées en tests.** B soustrait le gradient bénin ; D utilise une file commune et un flux entièrement honnête. |
| **A — intervention ambiguë, trait bénin, sélection sur déficit initial** | **Acceptées.** E exclut les démonstrations de la tâche, fixe l’intensité sur témoins et sépare articles de qualification et d’estimation. |
| **A — absence d’opérateur, marges et nombre d’articles** | **Acceptées.** Aucun prix de service n’est connu. Distinguer seuils illustratifs de banc et seuils d’adoption ; dimensionner avant de promettre une décision par strate. |
| **B — marges ouvertes, biais de spectre, circularité** | **Acceptées.** Frontières proposées ci-dessous, à signer avant toute nouvelle lecture. Aucun cas écarté parce que non arbitrable ; panels indépendants pour A et D. |
| **B — fuite de famille et contrôle par forçage** | **Acceptées**, sans inférer qu’une relecture qui échoue prouve l’absence d’information dans le texte. Le comparateur doit pouvoir apprendre sa propre sonde. |
| **B — prévalence, faible nombre de confirmations, régression vers la moyenne et variance des courses** | **Acceptées.** D rapporte une courbe de rendement continu selon le mélange ; E réplique les *courses*, pas seulement les questions. La puissance de B dépend des articles et celle de C des trajectoires honnêtes indépendantes. |
| **D — hypothèses composites et sélection sur le dommage jugé** | **Acceptées sur le fond.** Une proposition et son complément sont exclusifs, mais l’échec d’une condition de mesure ne réfute pas le mécanisme. Séparer les conditions de validité du duel scalaire ; aucun filtrage postérieur par dommage en C. |
| **D — durée de lecture ; fuite de calibration ; régression en E** | **Durée : rejet partiel.** Le temps est bien un coût pour l’opérateur, mais pas une mesure de précision. D rapporte les deux. **Calibration et régression : acceptées** ; témoins de calibration et de test indépendants, y compris les fabrications bénignes. |
| **D — dégradations synthétiques discrètes** | **Transformée en contrôle positif** du lecteur en A : une modification documentée par un expert teste sa sensibilité ; elle ne sert ni de sabotage inédit ni de référence principale. |
| **E — biais de spectre, comparateur mécanique inégal, fuite cognitive** | **Acceptées.** A juge l’erreur sur le contraste de qualité, non la victoire sur la longueur ; aucun lecteur de produit seul ne voit les révisions. Inversion d’ordre et lectures externes budgétées. |
| **E — surcharge des consignes et saturation** | **Acceptées.** B oppose des contraintes graduées ; un dommage constant mais positif réfute la *gradation*, pas le dommage. |
| **E — absence de famille inédite, colliseur, coût des strates, contrôles de provenance** | **Acceptées.** C sépare assignation, calibration et avantage prédictif. Ajouter témoins d’amplitude et apprentissage à étiquettes permutées. **Dernier jeton système : diagnostic seulement** ; sa lecture ne décide pas si la consigne reste représentée plus tard. |
| **E — longueur, temps et mémoire des lecteurs ; force de mise à jour et devenir de la sonde** | **Acceptées.** File entremêlée, sans relecture d’un produit par le même lecteur ; E mesure aussi les scores gelés avant/après. **Rejet** de l’idée d’intégrer le bras d’attaque à E : il reste prévu séparément et ne constitue pas un placebo. |

### Classement et expériences corrigées

**HYPOTHÈSE — tous les nombres du barème, des seuils et des budgets qui suivent sont illustratifs**, non des résultats ni des valeurs de service. Score = (gain informatif × facilité × portée × potentiel de découverte majeure) / coût ; notes sur l’échelle demandée. Les estimations incluent le travail des lecteurs.

| Rang | Chantier | Calcul illustratif | Coût estimé illustratif |
|---|---|---:|---|
| A | Qualifier la mesure du dommage | (5×4×5×4)/3 = 133,3 | Traces existantes, processeur et vacations de deux panels |
| B | Établir le contraste à consigne | (5×4×4×3)/2 = 120 | Ordre de la centaine de dollars de calcul, plus lecture |
| D | Établir le rendement des vérifications | (4×3×5×3)/2 = 90 | Rejeu sur processeur et vacations chronométrées |
| C | Isoler l’apport des états | (5×3×5×4)/4 = 75 | Inférence de l’ordre de la centaine de dollars, **hors famille indépendante : devis inconnu** |
| E | Mesurer la persistance | (4×3×4×4)/4 = 48 | Plusieurs centaines de dollars hors lecture, à redimensionner par graine |

**HYPOTHÈSE — sensibilité et faisabilité.** Doubler le poids du coût en le mettant au carré place B devant A ; cela ne supprime pas le préalable métrologique. D peut préparer son rejeu avant C mais ne peut attribuer son résultat aux états avant la comparaison C. Avant lecture d’oracle, faire signer une échelle bornée de qualité, une unité \(u\) de perte **moyenne** qui ferait changer de décision au banc et les frontières ci-dessous. Sans signataire, publier les contrastes et leurs intervalles, pas un seuil d’adoption. Sur données honnêtes de préparation, estimer bruit entre lectures et entre articles ; simuler la précision après partition, y compris aux faibles doses. Pour C, avec \(n\) unités honnêtes indépendantes et aucune alerte, la borne supérieure unilatérale au risque \(\gamma\) vaut \(1-\gamma^{1/n}\). Si même cette borne dépasse le plafond, ne pas ouvrir le test. Pour E, dimensionner aussi sur la variance entre courses. Une condition de mesure non satisfaite signifie **non jugeable** ; un intervalle qui traverse la frontière signifie **indécis**. Aucun des deux n’est un résultat négatif.

- **A — Le produit seul retrouve-t-il le contraste diffus ?** À faible dose fixée d’avance, un panel note les produits séparément ; un autre estime les écarts sur paires anonymes avec jumeau, sur la même échelle. Mesurer l’erreur absolue entre leurs **contrastes moyens appariés par article**, non leur accord sur les seuls cas faciles. \(H_A\) : erreur \(<u/2\) ; \(H_B\) : erreur \(\ge u/2\). Une égalité près de zéro sans contraste de référence résolu ne qualifie pas le lecteur. Garder les abstentions et borner le résultat en leur attribuant les extrêmes admissibles. Témoins négatifs : honnête–honnête, bénin–honnête et présentations inversées à des lecteurs différents. Comparer aussi les motifs scientifiques : un accord imputable au style seul invalide la qualification.

- **B — La dose ajoute-t-elle une perte au-delà de la charge d’instruction ?** Sur les mêmes questions, randomiser les conditions et opposer à chaque dose une consigne bénigne parallèle en longueur, forme et contrainte ; garder aussi le jumeau nu. Métrique : différence entre gradients de perte moyens, exprimés sur toute l’étendue des doses, avec des coefficients de contraste fixés avant génération. \(H_A\) : différence \(>u\) ; \(H_B\) : différence \(\le u\). Témoin négatif : seconde série bénigne graduée. Publier chaque moyenne et ses bornes, abstentions comprises, afin qu’un plateau ne soit pas lu comme une absence de dommage.

- **C — Les états de l’agent ajoutent-ils de l’information utilisable avant la décision ?** Geler la sonde et, sans oracle, un comparateur textuel combinant juge, variables mécaniques et sonde apprise séparément sur le modèle honnête qui relit chaque préfixe public, sans consigne privée. À échéance identique, comparer les probabilités d’alerte **par assignation**, à faible dose prédésignée, sur trajectoires complètes. \(H_A\) : gain interne \(>5\) points illustratifs ; \(H_B\) : gain \(\le5\) points illustratifs. Qualifier séparément, sur témoins tenus à l’écart, un plafond illustratif de \(5\,\%\) par trajectoire et des taux réalisés comparables ; calibrer avec réserve sous ce plafond. Témoins : honnêtes difficiles, adaptateurs bénins indépendants couvrant les amplitudes de déplacement des poids et de divergence des sorties, étiquettes permutées. Sans recouvrement, la provenance reste une explication. Familles actuelles : diagnostic seulement ; verdict après reconception : **famille indépendante ou pas de verdict**.

- **D — L’aiguillage retrouve-t-il davantage de perte à travail égal ?** Geler les listes et les mélanges avant lecture. Une file unique entremêle les produits, sans révéler qui les a sélectionnés. Créditer ensuite chaque liste du même jugement pour un même produit. Métrique principale : excès de perte cumulée, en unités \(u\) par heure additionnelle, contre la politique sans états gelée ; vérifier le contraste avec un panel apparié indépendant au banc. \(H_A\) : gain \(>u\) par heure illustrative sur le mélange principal préenregistré ; \(H_B\) : gain inférieur ou égal. Rapporter aussi le gain à nombre fixe de produits, par longueur et pour plusieurs prévalences déclarées. Témoins : scores permutés et flux entièrement honnête de difficulté variable. Si l’enrichissement apparent ne se retrouve que dans les erreurs du lecteur, il ne compte pas comme perte retrouvée. Aucun prélèvement sur l’audit aléatoire.

- **E — Une mise à jour non corrective efface-t-elle le déficit ?** Après autorisation écrite, comparer copies gelées et copies soumises à une continuation sur corpus bénin hors banc, sans démonstration de la tâche ni score. Fixer corpus, budget et point final sur témoins distincts ; vérifier que l’intervention déplace un trait bénin mesurable sans amener la compétence honnête au plancher. Sur des articles différents de la qualification initiale, mesurer la différence de déficits entre bras gelé et mis à jour, chacun contre son jumeau correspondant. \(H_A\) : réduction \(>u\) ; \(H_B\) : réduction \(\le u\). Répliquer par graines d’entraînement ; rapporter aussi les qualités absolues contre le jumeau gelé. Témoin négatif : copie sans mise à jour réévaluée. Une intervention trop faible ou destructrice ne tranche pas la persistance. La sonde gelée est une mesure secondaire : si le dommage disparaît, sa perte de séparation ne démontre pas sa défaillance.

**HYPOTHÈSE — calendrier et règles.** Pour le jury du 1er décembre 2026 : présenter le registre, le devis demandé et le calcul de faisabilité. Avant la porte de fin décembre : A d’abord, B et calibration honnête si dimensionnables ; pas plus de trois chantiers actifs. À la porte comparative environ deux mois après : C si la pièce indépendante existe, puis D sur dossiers réservés. Reporter E et les essaims. Maintenir le bras d’attaque déclaré distinct de toute parade. Ne pas ouvrir la correction par entraînement ; l’ouvrir ultérieurement changerait la règle de correction, et employer une note de juge pour entraîner ou sélectionner l’agent exigerait **aussi** une modification explicite de la règle sur les moniteurs. Aucun usage de l’oracle pour sélectionner agent ou moniteur.

**Hors de portée :** établir une intention, garantir contre des pertes que personne ne sait mesurer, ou transposer au service la fragilité d’un adaptateur fabriqué au banc.

FIN-DE-CELLULE