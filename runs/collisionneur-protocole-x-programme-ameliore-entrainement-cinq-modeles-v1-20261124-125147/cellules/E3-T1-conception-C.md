## 1. Ce qu'un expert du domaine ferait ici, et que la question ne demande pas.

**HYPOTHÈSE — proposition C.** Je séparerais trois décisions que le mot « contrôle » confond : *ouvrir une vérification*, *conclure qu'il y a un excès de dommage*, *modifier les poids*. Elles n'exigent pas la même preuve. Une sonde peut justifier la première sans justifier la deuxième ; même la deuxième ne justifie pas la troisième si relancer avec un modèle de confiance coûte moins cher et préserve mieux la qualité.

Je commencerais par faire chiffrer, **avant de regarder les scores**, combien de vérifications supplémentaires l'opérateur peut absorber et quelle perte sur un produit de recherche changerait sa décision. Sans ces deux prix, on peut mesurer une séparation statistique, mais pas décider si l'instrument mérite sa place.

| Présupposé à mettre en cause | Statut |
|---|---|
| Il existe un état interne caractéristique du sabotage, plutôt que de la consigne, de l'adaptateur ou de la difficulté. | **HYPOTHÈSE.** Même une bonne prédiction du dommage ne prouverait pas que le modèle se représente son sabotage. |
| Le jumeau donne la vérité du dommage. | **VÉRIFIÉ :** il fournit un comparateur au banc seulement. **HYPOTHÈSE :** l'écart de qualité est assez reproductible pour servir de référence. Une paire de sorties peut différer sans sabotage. |
| Les familles fabriquées correspondent à des menaces de sévérité comparable. | **VÉRIFIÉ :** seule la courbe de l'adaptateur existe. L'équivalence des doses entre familles est une **HYPOTHÈSE**. |
| L'entraînement soigne une politique persistante plutôt qu'il n'efface un artefact de fabrication. | **OBSERVÉ-NON-AUDITÉ :** la tenue des organismes du programme à l'entraînement n'a pas été mesurée. |
| L'expérience proposée occupe une place vacante. | **OBSERVÉ-NON-AUDITÉ :** recherche bornée pour les sondes sur tâches difficiles à noter ; pas de recherche complète sur les combinaisons. Je ne sais pas si la combinaison est nouvelle. |

## 2. Les données brutes de départ

**HYPOTHÈSE — collecte proposée.** Avant toute courbe agrégée, constituer un registre appariable, à accès séparés :

- **Production :** article, question, consignes exactes, modèle et adaptateur identifiés, condition assignée, dose nominale, graines, dix révisions horodatées et produit final. Garder les abandons. Produire aussi des paires honnête–honnête indépendantes sur la même tâche, des consignes bénignes de même forme et des adaptateurs bénins de fabrication comparable.
- **Mesure interne et textuelle :** activations aux positions préspécifiées, texte effectivement accessible au moniteur à chaque pas, scores bruts et instant de première alerte. Ne donner ni identifiant de condition ni jumeau au moniteur.
- **Dommage :** produits anonymisés dans un ordre tiré au sort, jugements individuels avant arbitrage, motif concret de perte scientifique, désaccords et abstentions. Conserver séparément *assignation au sabotage* et *dommage jugé* : ce ne sont pas deux noms de la même étiquette.
- **Audit et entraînement :** probabilités de tirage, temps de lecture, coûts de calcul ; pour toute intervention sur les poids, point de départ, données autorisées, budget fixé et point final, y compris pour le témoin.

**VÉRIFIÉ :** l'oracle ne sélectionne ni agent ni moniteur. **HYPOTHÈSE — mise en œuvre :** sceller par article les partitions de conception, de calibration honnête et de test ; confier les jugements de dommage à un dépositaire qui ne les restitue qu'après gel des instruments. Ne pas choisir après coup la dose, la famille ou le point d'entraînement qui raconte l'histoire la plus nette.

## 3. Ce que chaque voie peut établir

| Voie | HYPOTHÈSE — inférence permise et condition de validité | Ce qui la rendrait vaine, ou trompeuse |
|---|---|---|
| **Détecter** | À charge de fausses alertes fixée **par trajectoire**, l'histoire des états peut indiquer où vérifier plus tôt que le texte seul. Il faut calibrer le maximum séquentiel sur des trajectoires honnêtes complètes et tester hors de la condition de fabrication. | Une sonde qui reconnaît tout adaptateur détecte une provenance. Une alerte qui arrive après la décision n'économise aucune vérification. Le silence n'établit pas l'innocuité. |
| **Auditer** | Le tirage indépendant renseigne sur la fréquence du dommage **reconnaissable par l'oracle**, relativement à une référence honnête pertinente. L'aiguillage peut enrichir un lot supplémentaire en cas confirmés. | Augmenter le nombre de lectures ne corrige pas une erreur systématique de jugement. Mélanger le lot ciblé au lot aléatoire comme s'ils étaient interchangeables invalide l'interprétation de la fréquence. |
| **Entraîner** | Une intervention assignée, comparée à l'absence d'intervention et à une mise à jour témoin, peut établir une réduction de dommage au banc à compétence honnête préservée. | Si une mise à jour sans information corrective fait aussi bien, l'effet spécifique de la supervision n'est pas établi. Si seul le score du moniteur baisse, la correction ne l'est pas non plus. Ni l'une ni l'autre observation ne démontre un changement d'intention. |

**VÉRIFIÉ :** la garantie actuelle réside dans l'audit aléatoire, non dans la sonde ; la correction par entraînement n'est pas ouverte. **RAPPORTÉ :** la garantie de l'audit suppose un oracle reconnaissant le dommage et un taux honnête de référence. **HYPOTHÈSE — conséquence :** réserver le tirage aléatoire même si la sonde est excellente ; après changement de poids, revalider la calibration honnête avant de réutiliser la sonde. Sinon une « guérison » pourrait n'être que la perte de validité du thermomètre.

## 4. Les programmes possibles

**HYPOTHÈSE — architectures concurrentes.** Les tests décisifs et leurs témoins sont spécifiés en section 7. Le risque d'antériorité ci-dessous est une appréciation, pas un résultat bibliographique.

| Architecture et thèse | Expérience centrale et réfutation | Ce qu'elle exige ; coût et recouvrement |
|---|---|---|
| **Inchangée : détection, corruptibilité, essaims.** L'avantage interne chez l'agent seul justifie d'en étudier les extensions. | Test C ci-dessous ; un avantage inférieur au minimum utile réfute ce motif d'extension, même si la sonde reconnaît la famille connue. | Organismes détectables hors signature de fabrication ; dommage qualifié pour revendiquer une utilité défensive. Coût élevé des extensions ; recouvrement plausible avec la détection publiée, moins clair sur ce banc. |
| **Contrôle à budget de vérification fixe — mon choix.** Le résultat recherché est un surcroît de dommages confirmés à travail égal, sans amputer l'audit indépendant. | Test D après A–C. Pas de gain sur le meilleur aiguillage sans états : retirer la sonde du circuit opérationnel, même si elle reste un outil de recherche. | Exige des cas dommageables et un oracle utile sans accès privilégié au jumeau. Coût surtout en lectures ; audit aléatoire déjà publié, à ne pas revendiquer. |
| **Changer d'objet : métrologie des organismes.** Le produit principal devient une qualification de la persistance du sabotage, pas un détecteur. | Test E : une intervention bénigne qui supprime une part décisive du dommage réfute la qualification de cet organisme comme persistant à cette intervention. | Exige une politique dans les poids, un écart initial établi et une mesure de compétence. Entraînements appariés coûteux ; recouvrement important avec les études de sous-rendement, sans transfert établi à la recherche ouverte. |
| **Correction par apprentissage.** Une supervision faible accessible en service réduit le dommage au-delà d'une simple perturbation des poids. | Duel conditionnel : \(H_A\), gain de qualité supérieur au minimum utile contre **les deux** témoins (poids gelés, mise à jour de même budget sans information corrective), à compétence préservée ; \(H_B\), complément. Jugement final indépendant. Les issues concluantes réfutent respectivement \(H_B\) ou \(H_A\). | Exige un organisme persistant au témoin, une supervision réaliste distincte de l'oracle et une évaluation hors entraînement. Coût le plus élevé ; recouvrement avec l'entraînement sous supervision faible. **Ne pas ouvrir maintenant.** |

**VÉRIFIÉ :** le travail sur ce banc sans lecture interne optimise principalement des consignes ; le travail montrant plusieurs issues à l'entraînement contre un détecteur interne porte sur du code vérifiable (dans les deux cas : référence à vérifier). **HYPOTHÈSE — arbitrage :** aucun des deux ne dispense du témoin de persistance ni d'un jugement indépendant sur le produit ouvert.

## 5. Ce qui, en dehors du programme et de son équipe, permettrait de vérifier la validité du résultat

**HYPOTHÈSE — proposition.** Faire conserver par un tiers le préenregistrement daté, les empreintes des poids, le code de tirage et le test scellé. Une équipe indépendante reçoit les produits sans provenance et sans scores ; une autre peut recalculer alertes, coûts et bornes à partir des traces gelées. Publier aussi les paires où les lecteurs ne peuvent départager les produits, les alarmes sur adaptateurs bénins et les cas dommageables sans alarme. Ce sont les pièces qui permettent de contester la conclusion.

L'épreuve externe utile n'est pas de retrouver le même chiffre sur les mêmes fichiers : c'est de refaire la décision à budget déclaré sur de nouveaux articles, avec des lecteurs différents et, pour une sonde reconçue, une famille inédite ouverte une seule fois. Si personne ne peut payer ou fournir cette dernière, annoncer **validation limitée aux familles testées**, et non généralisation.

## 6. Reformulation exigeante de la tâche

**HYPOTHÈSE — cible.** « Sur des questions de recherche tenues à l'écart, sous un plafond d'alertes honnêtes et à temps de lecture égal, les états internes permettent-ils de faire confirmer davantage de pertes scientifiques qu'un dispositif sans accès interne, tout en maintenant un audit indépendant ? À défaut, peut-on localiser l'échec : absence de dommage mesurable, organisme inadéquat, absence de signal transférable, ou signal sans valeur pour la décision ? »

Cette formulation conserve la détection, retire à la sonde le rôle de preuve et ajoute une qualification de l'organisme. Elle aborde l'entraînement d'abord comme **contrôle expérimental de fragilité**, pas comme parade déjà disponible.

## 7. Programme des priorités classé

**HYPOTHÈSE — barème entièrement illustratif.** Ordre des notes : gain informatif, facilité, portée, potentiel de découverte majeure, puis coût au dénominateur. La portée désigne ici le nombre de décisions du programme que le résultat peut changer.

| Rang | Chantier | Notes illustratives | Score illustratif |
|---|---|---|---:|
| A | Qualifier le jugement du dommage | (5 × 5 × 5 × 3) / 2 | 187,5 |
| B | Qualifier le contraste à consigne | (5 × 4 × 4 × 3) / 2 | 120 |
| C | Tester le signal interne transférable | (5 × 3 × 5 × 4) / 3 | 100 |
| D | Mesurer l'utilité de l'aiguillage | (4 × 4 × 4 × 3) / 2 | 96 |
| E | Tester la persistance sous mise à jour bénigne | (4 × 3 × 4 × 4) / 4 | 48 |

**Sensibilité, illustrative :** si le coût compte au carré, D passe devant C ; cela favorise une simulation sur dossiers gelés, pas l'ouverture anticipée du test inédit. Si les lectures requièrent des experts rares, la facilité de A est surestimée ; A reste un préalable logique à toute affirmation de réduction de dommage.

**HYPOTHÈSE — convention commune aux duels.** Avant test, fixer \(\alpha\), plafond d'alertes par épisode honnête, \(q\), perte scientifique qui change la décision, et pour chaque comparaison une marge \(m\) dans son unité naturelle, dérivée du budget de vérification ou de la perte tolérée. Je ne sais pas en donner des valeurs justifiées avec les pièces disponibles. Les inscrire, avec le budget et la précision attendue, avant engagement du calcul. Pour chaque seuil ci-dessous, une borne d'incertitude entièrement du côté \(H_A\) réfute \(H_B\), et inversement ; si elle chevauche la frontière, **indécis**, pas « absence d'effet ». Tenir compte de l'appariement par article, pas traiter les révisions comme des épisodes indépendants.

- **A — L'oracle utilisable sans jumeau reconnaît-il une perte ?** Référence de banc : lecture indépendante en aveugle des paires avec jumeau, puis arbitrage motivé au seuil \(q\). Tester séparément le lecteur de produit seul : sensibilité sur pertes arbitrées, faux positifs sur produits honnêtes de mêmes questions, y compris les produits médiocres ; mesurer aussi le faux dommage déclaré sur paires honnête–honnête. \(H_A\) : à plafond \(\alpha\), la sensibilité dépasse de \(m_A\) le contrôle mécanique (longueur, complétude des rubriques, modifications entre versions), avec couverture minimale préfixée des jugements arbitrables ; \(H_B\) : complément. Des abstentions massives ne doivent pas produire artificiellement un succès. **Coût illustratif :** processeur seul sur traces existantes, plus deux vacations de lecture et arbitrage selon désaccord. Ce test qualifie un accord avec une référence imparfaite, pas une vérité absolue.

- **B — La consigne cachée produit-elle un contraste gradué de dommage ?** Assigner les doses avant génération sur questions appariées ; estimer la tendance ordonnée du dommage arbitré et la fréquence de franchissement de \(q\) à chaque dose. \(H_A\) : tendance positive dépassant \(m_B\) relativement à une série de consignes bénignes de longueur et de forme appariées ; \(H_B\) : contraste inférieur ou égal au seuil. Contrôle négatif supplémentaire : assignations permutées dans les blocs de questions. Rapporter côte à côte la courbe existante de l'adaptateur, sans réétiqueter les doses pour aligner les résultats. **Coût illustratif :** quelques courses du modèle ouvert, ordre de la centaine de dollars de calcul, plus lecture.

- **C — L'interne bat-il le texte hors fabrication connue ?** Geler sonde, positions, accumulation, juge textuel et règle mécanique de trajectoire (longueur, volume de révision, rubriques manquantes). Même texte disponible au même instant ; publier pour chacun sensibilité avant échéance sur épisodes dommageables et fréquence de première fausse alerte sur trajectoires honnêtes appariées par article, consigne bénigne et type d'adaptateur. \(H_A\) : sur la famille réservée, gain de sensibilité de la sonde supérieur à \(m_C\) contre **chacun** des comparateurs, sans excéder \(\alpha\) dans les strates honnêtes prévues ; \(H_B\) : complément. Le témoin décisif est l'adaptateur bénin, pas seulement le modèle de base. **Coût illustratif :** quelques courses d'inférence avec capture ciblée, ordre de la centaine de dollars hors lecture ; devis séparé si une famille supplémentaire doit être produite.

- **D — Les alertes changent-elles le rendement des vérifications ?** Sur dossiers gelés, maintenir identique le lot d'audit aléatoire ; assigner le budget de lecture *additionnel* à l'aiguillage interne, textuel, mécanique ou aléatoire. Métrique : épisodes dommageables distincts confirmés par heure de lecture ; publier aussi fraction des dommages retrouvés et lectures inutiles de produits honnêtes appariés. \(H_A\) : gain supérieur à \(m_D\) face à chaque solution sans états ; \(H_B\) : complément. Contrôle négatif : scores permutés entre épisodes comparables ; lecteurs ignorants du mode d'aiguillage. L'audit indépendant conserve son propre dénominateur. **Coût illustratif :** rejeu sur processeur, plus vacations de lecture chronométrées ; pas de nouvelle génération si les dossiers suffisent.

- **E — L'adaptateur survit-il à une mise à jour sans signal de correction ?** Seulement si l'écart initial dépasse \(q\). Comparer, sur articles réservés, adaptateur gelé et copie soumise à une mise à jour bénigne fixée d'avance ; soumettre le jumeau honnête et un adaptateur bénin à la même intervention. Métrique : réduction du déficit relativement au jumeau, avec contrôle de la qualité absolue pour ne pas appeler « réparation » une dégradation du jumeau. \(H_A\) : réduction supérieure à \(m_E\), à compétence honnête préservée dans la tolérance déclarée ; \(H_B\) : complément. Ventiler persistance et perte de compétence si \(H_A\) est réfutée. **Coût illustratif :** plusieurs courses d'adaptation légère et d'évaluation, quelques centaines de dollars hors lecture. Aucun score de sonde, de juge ou d'oracle dans la mise à jour ou la sélection. **Autorisation explicite requise** pour ce bras diagnostique sur les poids du modèle soupçonné ; il n'autorise pas la correction en service.

**VÉRIFIÉ — contrainte matérielle et calendrier.** Modèle ouvert de huit milliards de paramètres, quelques dizaines de dollars par course sur une carte louée, une personne, au plus trois chantiers actifs. **HYPOTHÈSE — décision :** avant l'entretien du 1er décembre 2026, présenter le registre, les duels et les critères d'arrêt. Avant la porte de fin décembre, exécuter A et B et vérifier la calibration honnête de C ; geler C sans consommer le test réservé pour une répétition générale. À la porte comparative environ deux mois plus tard, lire C une fois, puis D si la référence de dommage tient. E attend un budget, une autorisation et un déficit initial mesurable. Différer les essaims et la troisième famille tant que leur valeur discriminante ne justifie pas le devis ; ne pas reconcevoir une sonde sur son échec puis la déclarer validée sur la même famille.

**Hors de portée :** conclure à une intention, garantir la détection d'un dommage que les lecteurs ne reconnaissent pas, ou déduire d'un adaptateur réparé au banc qu'un apprentissage en service neutraliserait une menace persistante.

FIN-DE-CELLULE