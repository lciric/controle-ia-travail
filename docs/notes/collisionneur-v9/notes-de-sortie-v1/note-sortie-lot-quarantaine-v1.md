# Que faire d'un lot de cas tenu à l'écart : note de sortie du collisionneur

- **Date** : 2026-11-22, 19:42 UTC.
- **Dossier** : `runs/collisionneur-protocole-x-lot-quarantaine-v1-20261122-112512`.
- **Accord** : GO-2026-11-22-43 (lu dans `registres/essaim/vers-mere/collisionneurs-v8d-2026-11-22-1256-v1.md`) ; réserve de la question sous GO-2026-11-22-37.
- **Dépense** : 15,18 dollars sur une ligne de 100 (`etat.md` du dossier). Les cellules Claude (Fable 5.2 et Opus 5.5) sont passées par l'interface payante dans ce dossier. La part d'Astra est surestimée d'environ 20 % : le dossier l'a comptée au prix d'une version antérieure (`declaration-prix-astra-v1.md` du dossier).
- **Tours** : dix-huit cellules sur dix-huit, toutes complètes : six conceptions (tour III.1), six critiques croisées (III.2), six réponses (III.3).
- **Note écrite après coup** (dossier fini le 22 novembre à 12:56 UTC, avant la règle des notes de sortie).

Rédigé par un lecteur Opus 5.5, classe C, à partir des seules cellules du dossier, de la question servie, de `etat.md`, du journal et du compte rendu cité. Le lecteur est du même modèle qu'une des cellules (lettre B) ; elle est traitée comme les autres. Aucun autre fichier du dépôt n'a été ouvert sur le contenu du lot ou des modes de sabotage. La note rapporte la méthode discutée, pas un contenu de lot.

**Réserve de devinette (0,55).** Le dossier porte en tête la réserve suivante : « question orientée faiblement au test de devinette (0,55) ; servie telle quelle, comme les deux précédentes ». Le dossier ne dit pas dans quel sens la question oriente. Les accords unanimes rapportés plus bas (sections 2 et 4) sont donc à lire avec cette réserve : une partie de la convergence peut venir de la formulation de la question plutôt que d'un raisonnement indépendant.

**Ce que la note n'est pas.** Aucune cellule ne rapporte de mesure. Tout ce qui suit est démonstration, calcul sous hypothèses ou protocole proposé. Les seuils, effectifs et coûts sont qualifiés d'illustratifs par leurs auteurs. Argon et Carbon ont marqué « vérifié » des points qu'ils ne pouvaient pas vérifier (intégrité des pièces, espérances) ; ils l'ont corrigé au tour III.3. Aucune référence bibliographique n'a été contrôlée. Les remarques propres au lecteur sont signalées comme telles.

## 1. La question

Une équipe met au point des détecteurs qui surveillent un agent logiciel pendant de longues tâches, pour repérer une dégradation discrète du résultat. Elle les améliore par cycles, en nombre non fixé, et passe à l'étape suivante quand un critère chiffré est atteint. Elle détient un ensemble de cas de dégradation d'un genre que les auteurs des détecteurs n'ont pas consulté. Depuis, ce que l'équipe affirme a changé : elle ne soutient plus qu'un détecteur est bon en soi. Elle veut dire (i) si ses mesures s'écartent d'une loi déjà publiée, et (ii) si un détecteur qui lit l'état interne de l'agent ajoute quelque chose à un second détecteur qui lit le texte. Quatre questions :

1. à quoi sert cet ensemble : au critère de passage, à la portée de ce que l'équipe affirme, aux deux, à autre chose, à rien ;
2. quand le consulter : à chaque cycle, par parties, une seule fois, jamais, autrement ;
3. si des auteurs l'ont vu, en tout ou en partie : le garder, le déclasser, le jeter, le refaire, ou cela dépend d'un élément à nommer ;
4. le changement de ce que l'équipe affirme modifie-t-il ces réponses.

Pour chaque réponse : un énoncé réfutable, l'antériorité la plus proche, un contrôle qui ne dépend de l'avis de personne, un degré de certitude.

Notations reprises des cellules : « lot » ou Q pour l'ensemble tenu à l'écart ; T pour le détecteur qui lit le texte ; « état interne » pour les activations de l'agent ; « relecture aux mêmes poids » pour les activations obtenues en faisant relire par les poids de l'agent exactement le texte que lit T (les cellules l'appellent Z_rejeu ou Z′).

## 2. En bref

- **Le lot sert à la portée, jamais au critère de passage.** Les six modèles le disent dès le tour III.1 et le maintiennent. Deux nuances du premier tour sont retirées au troisième : le « guichet » à un bit par consultation (Fable) et le double usage d'un examen terminal unique (Astra).
- **Une seule ouverture, après un gel complet.** Au tour III.3, les six convergent : détecteurs, seuils, loi, contrastes, plan d'analyse, et chez Neon un engagement de publier le résultat quel qu'il soit, sont scellés avant l'ouverture.
- **La critique la plus partagée porte sur la fuite de genre.** Couper le lot (ou un genre de remplacement) en deux moitiés du même genre ne peut pas détecter une adaptation au genre : le terme commun s'élimine par soustraction. Cinq critiques sur cinq l'opposent à Fable, et la plupart l'opposent aussi à Opus, Argon, Carbon et Neon. Le remède adopté par tous : un troisième genre, disjoint et jamais consulté.
- **L'affirmation (ii) a changé de sens au cours du dossier.** Fable et Opus posent au tour III.2, indépendamment, la même hypothèse : si l'agent est un transformeur sans mémoire hors contexte, son état interne est une fonction du texte qu'il a reçu. Un apport de l'état interne ne peut alors venir que de deux sources : un contexte que T ne voit pas, ou un écart de calcul (T n'extrait pas ce que les poids de l'agent calculent). Le contrôle qui sépare les deux, la relecture aux mêmes poids, est adopté par les six au tour III.3. Carbon conteste en partie l'hypothèse elle-même.
- **Avant d'ouvrir quoi que ce soit, un inventaire.** Les six placent en premier une vérification sans ouverture des étiquettes : l'ordre des dates entre tout accès au lot et le changement d'affirmation, la présence de cas honnêtes, la présence d'états internes archivés ou rejouables, l'identité de la loi. Sans cas honnêtes ou sans états internes, l'affirmation (ii) est non jugeable sur ce lot.

## 3. Ce que chaque modèle a proposé

### Claude Fable 5.2 (lettre A)

- **Proposition centrale** (A, III.1). Onze présupposés de la question, de P1 à P11. Exemples : « genre non vu » n'est pas « cas non vus » (P1) ; l'équipe n'a peut-être pas vu de résultat tiré du lot avant de changer d'affirmation (P2) ; le lot contient peut-être des cas honnêtes appariés (P4) ; l'état interne est peut-être lisible sur ces cas (P5) ; un seul genre tenu à l'écart, donc n = 1 au niveau du genre (P8).
- **Plan** (A, III.1). Cinq expériences :
  - E1 : la consultation répétée use-t-elle le lot, par une coupe en une partie lue à chaque cycle et une partie scellée ;
  - E2 : le texte plus l'état interne battent-ils le texte plus un second détecteur de texte de capacité comparable ;
  - E3 : la sonde lit-elle la dégradation ou ce qui l'induit (inducteur sans dommage contre dommage spontané) ;
  - E4 : écart à la loi par un test d'équivalence à deux tests unilatéraux, après une reproduction de la loi dans ses conditions publiées ;
  - E5 : l'exposition a-t-elle gonflé les scores, par double différence entre détecteurs modifiés avant et après l'exposition.

  Réponses du premier tour : portée, et pas au critère « sauf par un guichet budgété qui ne rend qu'un bit bruité » ; consultation par parties scellées ; cela dépend de la date, de l'objet vu et de la symétrie entre auteurs ; « en partie ». Coût avancé : 500 à 2 500 euros de calcul, et 2 à 4 semaines-personne pour construire les paires honnêtes (illustratif).
- **Apports en critique** (A, III.2). Trois arguments posés une fois et réemployés : A1 (déterminisme du transformeur, d'où la relecture aux mêmes poids), A2 (un témoin au niveau du hasard ne certifie aucune équivalence), A3 (un résultat rapporté seulement quand il franchit un seuil est biaisé vers le haut, même avec une lecture unique). Fable relève aussi le prénom erroné dans une référence d'Astra et calcule qu'un test de McNemar exact ne peut rien rejeter à moins de 6 paires discordantes.
- **Après les critiques** (A, III.3). Fable accepte presque tout et reconnaît une erreur : sa phrase « l'issue sans usure de E1 réfute ma propre recommandation » était fausse, E1 ne bornant que l'usure au niveau des cas. Il recalcule ses effectifs (environ 860 paires pour une marge de 5 points, et non 200). Deux rejets : la permutation des activations par tranches du score textuel, et un test d'homogénéité des scores utilisé comme porte. Expériences refaites :
  - E1′ hors du lot, sur des genres de développement, avec un genre distinct que la boucle ne lit pas et un nombre de cycles tiré au sort ; deux estimandes, usure au niveau des cas et usure au niveau du genre ;
  - E2′ en deux duels : contexte invisible (état interne contre relecture aux mêmes poids) et écart de calcul (relecture aux mêmes poids contre T seul), au même taux de fausses alertes mesuré sur les honnêtes du lot ;
  - E3′ en plan 2×2 (inducteur actif ou inerte, issue dégradée ou intacte) ;
  - E4′ par tranches de la variable explicative de la loi, sans moyenne de résidus ;
  - E5′ en deux duels, « cas » et « genre », avec une fausse date d'exposition comme placebo.

  Réponses finales : portée seulement ; une seule fois, au gel ; cela dépend de quatre éléments (date, objet, symétrie, et niveau cas ou genre), et « refaire » doit viser un autre genre ; en partie.

### Claude Opus 5.5 (lettre B)

- **Proposition centrale** (B, III.1). Douze présupposés, de S1 à S12, dont : le lot contient des honnêtes du même genre (S2) ; l'étiquette vient d'un oracle mécanique (S3) ; la loi est identifiée avec une bande de prédiction (S4) ; « avoir vu » n'est pas binaire (S12). L'élément nommé pour la question 3 est l'« exposition différentielle datée » : quoi, par qui, quand par rapport au gel, quelle partie. Règle proposée : garder si l'exposition est postérieure au gel, déclasser la partie exposée sinon, refaire si la partie n'est pas identifiable, ne jamais jeter.
- **Plan** (B, III.1). Cinq expériences, dont E1 sur un genre de remplacement avec une boucle scriptée, E2 avec trois sondes de contrôle (couche d'entrée, poids aléatoires, étiquettes permutées), E5 en calcul de puissance (environ 1 500 honnêtes pour estimer un taux de 1 % à 0,5 point près, calculé). Audit du critère de passage par une corrélation de rang entre score de développement et score tenu à l'écart. Paires « jumelles » qui bifurquent d'un même état sauvegardé. Coût : 100 à 150 heures de processeur graphique, quelques centaines de dollars.
- **Apports en critique** (B, III.2). R1 : la même hypothèse de déterminisme que Fable, posée indépendamment, avec le nom « relecture » et la décomposition en contexte invisible et écart de calcul. R2 : un seul genre, donc variance entre genres non identifiable. Opus garde comme référence le contrôle d'Astra par échange d'états entre traces d'une même strate.
- **Après les critiques** (B, III.3).
  - L'audit par corrélation de rang est retiré : deux séries qui progressent avec le cycle se corrèlent sans que le critère prédise quoi que ce soit (relevé par les cinq autres). Il est remplacé par E6′, qui exige plusieurs campagnes et se déclare non jugeable sur une seule.
  - Nouvelle règle : l'issue d'un audit ne peut modifier aucun critère appliqué aux détecteurs évalués sur ce lot.
  - E0 : inventaire et courbes de puissance avant toute ouverture.
  - E2′-0 : vérifier sur données de développement que les activations enregistrées égalent celles que recalculent les mêmes poids sur le contexte journalisé. Si oui, des états absents du lot deviennent reconstructibles.
  - E2′ à quatre bras (T, T plus second lecteur de texte, T plus relecture aux mêmes poids, T plus état interne), contrôle de « bifurcation à blanc » emprunté à Carbon, latence traitée comme une durée censurée.
  - Deux rejets : une alerte avant le point de bifurcation n'est pas une détection (contre Argon), et la combinaison de deux signaux ne donne pas un gain « par construction » (rejet partiel contre Neon).

### Argon (identifiant gemini-4-argon, lettre C)

- **Proposition centrale** (C, III.1). Sept présupposés. Le lot sert exclusivement à borner la portée et à quantifier le biais d'optimisme de la boucle.
- **Plan** (C, III.1). Quatre expériences, dont trois touchent le lot réel : le couper en une moitié de passage et une moitié de portée ; comparer trois régimes de consultation ; poser des « canaris » (traces piégées) pour détecter une exploitation du lot ; recalibrer les détecteurs sur le lot par validation croisée. Contrôle proposé pour (ii) : un agent dont on vide le cache des clés et valeurs à chaque pas. Paires appariées par un score textuel identique. Coût : environ 730 dollars.
- **Défauts relevés** (A, B, D, E, F, III.2).
  - Vider le cache puis réinjecter le même texte redonne les mêmes activations : le contrôle ne teste rien (cinq critiques).
  - Recalibrer sur le lot lit ses étiquettes et peut effacer par construction un écart à la loi (A, B, D, E, F).
  - Apparier sur le score textuel met T au plancher par sélection ; Carbon y voit un biais de sélection sur une cause commune (paradoxe de Berkson).
  - Le test d'équivalence était lu à l'envers ; les canaris ne s'insèrent qu'à la création d'un lot.
  - Statut « vérifié » apposé sans pouvoir recalculer les empreintes.
- **Apports en critique** (C, III.2). La critique la plus formelle du dossier. Exemples : démonstration que la coupe intra-genre a une puissance nulle contre une fuite de genre pure (contre Fable) ; décomposition de la perte logarithmique en résolution et défaut de calibration (contre Neon) ; puissance conjointe de quatre critères majorée par environ 0,37 (contre Neon) ; contrôle « miroir » à faire avec les mêmes poids que l'agent (contre Carbon) ; interdiction d'exécuter sur le lot réel des expériences de fuite (contre Carbon).
- **Après les critiques** (C, III.3). Argon accepte tout. Il abandonne le vidage du cache, la recalibration sur le lot, le rapport η, la distance de Kolmogorov-Smirnov, les canaris rétroactifs et tout filtrage. Expériences refaites hors du lot (genre de remplacement plus genre tiers), double différence appariée avec placebo antérieur à l'exposition, comparaison d'un écart à la loi mesuré par le détecteur et par l'oracle. Conclusion propre à Argon : si, sur le développement, l'état interne égale la relecture aux mêmes poids et que la relecture bat T, l'équipe devrait remplacer T par un lecteur adossé aux mêmes représentations avant d'ouvrir le lot.

### Astra (identifiant gpt-6.2-astra, lettre D)

- **Proposition centrale** (D, III.1). La plus courte. Réserver le lot à la portée après gel, faire décider le passage sur un autre flux de tâches. Le même examen terminal pourrait décider d'un passage et borner une affirmation, à condition qu'un échec signifie « pas de passage » et non « modifier puis représenter ».
- **Plan** (D, III.1). Tester la règle de passage complète sur des mondes nuls simulés ; mesurer l'optimisme du réemploi sur des campagnes randomisées ; un duel d'exposition sur un lot sacrificiel ; une distance à la loi par somme pondérée de valeurs absolues ; le contraste T contre T plus état interne, pas T contre état interne seul. Banc de transformations de tables. Coût : 60 à 300 euros (illustratif).
- **Défauts relevés** (III.2). Prénom erroné dans la référence de Cawley et Talbot (A, B). Le double usage terminal laisse un biais de troncature : la portée publiée est conditionnelle au passage (A, E). Les auteurs humains ne se simulent pas (B, C, F). La somme de valeurs absolues est biaisée vers le haut sous accord exact (C, E, F). Une fausse alerte avant le premier acte fautif compte comme « détection précoce » (E). Le banc de tables admet un invariant vérifiable par script (E).
- **Apports en critique** (D, III.2). La règle de décision à marge reprise ensuite par Opus, Argon, Carbon et Neon : pour un paramètre, une marge fixée d'avance ; un intervalle entièrement d'un côté réfute l'autre hypothèse ; un intervalle à cheval ne tranche rien. Remarques reprises : une corrélation positive entre deux séries est compatible avec leur indépendance à cycle donné ; la quantité utile est la probabilité qu'un candidat admis soit sous la marge ; « une ouverture par affirmation » fuit si l'affirmation suivante est choisie après le premier résultat ; une fausse date d'exposition sert de placebo.
- **Après les critiques** (D, III.3). Astra retire la condition de double usage. Il corrige le prénom (Gavin C. Cawley, toujours de mémoire). Montage nouveau pour le passage : à chaque cycle, inscrire le candidat avant de tirer des tâches de passage fraîches, et préengager une suite de risques dont la somme est au plus le budget ; la probabilité de jamais admettre à tort reste alors bornée sans avoir à simuler les auteurs. Exposition étudiée par campagnes randomisées sur des genres sacrificiels, avec un tirage au sort du destinataire de la révélation (auteurs du lecteur interne, du lecteur texte, ou personne). Pour (ii), une alerte ne compte comme succès qu'entre le premier acte fautif et l'échéance. Réponse à la question 3, la plus mesurée du dossier : garder les données, déclasser « la revendication touchée ».

### Carbon (identifiant gemini-4-carbon, lettre E)

- **Proposition centrale** (E, III.1). Sept présupposés, dont le premier est repris par tous : le lot a été constitué avant le changement d'affirmation, et rien ne garantit qu'il archive les états internes ou de quoi les régénérer ; sinon (ii) est matériellement impossible sur ce lot. Question 2 : « autrement », un contrôle mécanique aveugle du schéma avant tout cycle, puis une seule consultation.
- **Plan** (E, III.1). Six duels, dont deux exécutés sur le lot réel (le scinder en quatre parties, révéler 5 % des paires) ; un contrôle « miroir » où un autre modèle, plus petit, relit le texte ; une permutation des activations dans 20 tranches du score textuel. Coût : environ 600 à 720 euros.
- **Défauts relevés** (III.2). Le miroir sur un modèle quatre fois plus petit confond état interne et capacité d'encodage (A, B, C, F). Les expériences sur le lot réel le détruiraient (A, C). La permutation par tranches teste l'indépendance dans la tranche, pas l'indépendance sachant le texte, et rejette à tort dans la queue (A, B, C, D, F). Le taux appelé « fausses découvertes » est un taux d'erreur de première espèce. Statut « vérifié » apposé à des déductions ; résidu de brouillon.
- **Apports en critique** (E, III.2). Biais de sélection sur une cause commune dans le plan inducteur contre dommage spontané de Fable, et contrôle par un prédicteur qui ne lit que l'énoncé initial. Contrôle de « bifurcation à blanc » pour les paires jumelles d'Opus. Sonde fantôme, fonction déterministe du seul score textuel, pour qualifier un test conditionnel (contre Neon). Simulation d'une rupture pure de la loi hors du développement (contre Neon). Référence à la théorie de l'information utilisable sous contrainte de calcul (contre Argon).
- **Après les critiques** (E, III.3). Carbon accepte presque tout et remplace le miroir par la relecture aux mêmes poids. E0 devient une porte binaire, vérifiée par script sans regard humain : chronologie, présence ou rejouabilité des états, au moins 250 honnêtes et 250 dégradés (illustratif). Métrique principale de (ii) : l'aire partielle sous la courbe entre 0 et 5 % de fausses alertes, en deux étages (apport total, puis apport propre de l'exécution). Deux rejets :
  - **l'hypothèse de déterminisme, en partie** : le texte lu par T peut omettre du contexte privé (invite système, réflexion masquée), et, sous tirage aléatoire, le jeton réalisé « écrase » la distribution d'avant tirage ; Carbon transforme ce désaccord en test ;
  - **le lemme d'Astra** selon lequel l'estimation sur les cas non vus reste sans biais pour le genre : exact, dit Carbon, mais la fonction d'un genre non consulté est d'estimer la validité sur un genre inconnu, propriété détruite dès que les détecteurs s'adaptent au genre.

### Neon (identifiant gemini-4-neon, lettre F)

- **Proposition centrale** (F, III.1). Le lot sert à la portée ; il peut servir de « verrou de passage » en sortie unique après gel, jamais comme condition d'arrêt. Consultation par parties recevable seulement si le lot se partitionne d'avance en genres distincts. Dix présupposés, dont la symétrie d'effort entre les deux détecteurs (A7 : un détecteur texte sous-optimisé fabrique l'apport).
- **Plan** (F, III.1). Quatre expériences : fuite intra-genre par deux familles croisées ; écart à la loi par résidu standardisé et rapport de persistance ; apport de l'état interne par la perte logarithmique, quatre critères conjoints ; exposition par un lot frais du même genre. Coût : 925 à 3 150 dollars de calcul, et 4 000 à 15 000 dollars d'ingénierie pour construire le lot ; Neon est le seul à dire que le poste humain domine et rend la contamination du lot « matériellement critique ».
- **Défauts relevés** (III.2). Le rapport de persistance et la condition de signe plafonnent la puissance à un demi si la loi tient en développement (C, E). Un lot frais du même genre est aveugle à une fuite de genre, en contradiction avec la réponse de Neon à la question 2 (B, C, D, E). La perte logarithmique mêle discrimination et calibration (B, C, E). Moyenner les deux sens du croisement annule le témoin par construction (D).
- **Apports en critique** (F, III.2). Contrôle « oracle contre détecteur » : calculer l'écart à la loi sur les étiquettes de l'oracle et sur les sorties du détecteur, pour séparer violation de la loi et dérive de l'instrument. Repris par Fable, Argon, Astra et Carbon. Neon propose aussi, indépendamment, la relecture du seul texte par le même modèle.
- **Après les critiques** (F, III.3). Neon accepte ou transforme en test 23 critiques sur 26. E0 inclut un engagement de publication inconditionnelle, contre le biais de troncature. E1* confie les deux bras à deux sous-équipes cloisonnées. E2* abandonne rapport et condition de signe. E3* compare sept bras, dont la relecture aux mêmes poids, un second lecteur de texte, un modèle sur variables externes sans l'entropie des sorties (qui vient de l'état interne), et un modèle nul gelé ; la métrique principale est le rappel moyen sur la bande de 0 à 5 % de fausses alertes. Deux rejets : la recalibration sur le lot proposée par Argon comme contrôle, et la recalibration non supervisée proposée par Carbon. Première expérience : une répétition générale d'E3* hors du lot.

## 4. Accords et désaccords

### Accords indépendants au tour III.1

- **Question 1, portée et non critère de passage.** Les six (A, B, C, D, E, F), avec les deux nuances de Fable et d'Astra retirées ensuite.
- **Question 4, « en partie ».** Les six. Ce qui ne change pas : l'exclusion du critère et la consultation unique. Ce qui change : il faut des honnêtes, des états internes, une loi nommée, et l'asymétrie d'exposition entre les deux détecteurs devient le biais principal pour (ii).
- **Question 3, « cela dépend », jamais « jeter ».** Les six refusent de jeter (A, B, C, E, F explicitement ; D « garder pour diagnostic »). Les éléments nommés varient : date, objet, symétrie (A) ; exposition différentielle datée (B) ; traçabilité, nature, asymétrie (C, E, F) ; influence possible sur un choix restant (D).
- **Cas honnêtes nécessaires.** Sans eux, aucun taux de fausses alertes sur le lot (A P4, B S2, C, D, E, F A2).
- **États internes lisibles et modèle à poids ouverts.** (A P5, B S10, C, D, E 1, F A8).
- **Effort égal entre détecteurs.** Un détecteur texte sous-optimisé fabrique l'apport (A P6, C, E 6, F A7).
- **Ordre des dates entre accès au lot et changement d'affirmation.** Sinon le changement a pu être guidé par les données, au sens de Kerr (A P2, B S6, F A5 ; D le signale sans contrôle ; E cite Kerr).
- **Un seul genre, donc portée limitée à ce genre.** (A P8, B, D, F).

### Convergence née des critiques

- **Troisième genre disjoint.** Né de la critique de la coupe intra-genre (contre A par B, C, E, F ; contre B par C, E, F ; contre D et F par plusieurs). Adopté par les six au III.3.
- **Relecture aux mêmes poids et décomposition de l'apport.** Posée indépendamment au III.2 par Fable (A1), Opus (R1) et Neon (contrôle de ré-encodage à modèle identique) ; Argon et Carbon la demandent contre le miroir de Carbon. Adoptée par les six au III.3. Carbon la garde en contestant l'hypothèse qui la fonde.
- **Taux de fausses alertes réellement égaux.** Un seuil fixé en développement ne garantit pas le même taux de fausses alertes sur un genre nouveau (relevé contre A, B, D, E, F). Remèdes : seuil estimé sur une moitié des honnêtes du lot (A, B, C) ou aire partielle sous la courbe (B en secondaire, E, F).
- **Règle de décision à marge.** Proposée par Astra (D, III.2), reprise nommément par Opus, Argon, Carbon et Neon ; Fable garde une convention voisine.
- **Lot fermé jusqu'à l'ouverture unique.** Les expériences prévues sur le lot réel (A E1, C E1 à E4, E E2 et E3) sont déplacées sur des genres de développement.
- **Placebo de fausse date** (D, III.2), repris par A, B, C, E, F.
- **Oracle contre détecteur** (F, III.2), repris par A, C, D, E.
- **Abandon des permutations par tranches du score textuel** (critiquées par A, B, C, D, E, F). Remplacées par un appariement aux plus proches voisins (E) ou un tirage conditionnel validé hors lot et qualifié par la sonde fantôme (F) ; Fable rejette la méthode par tranches.

| Modèle | Première chose à faire au tour III.3 | Touche-t-elle le lot ? |
|---|---|---|
| Fable (A) | Inventaire (dates, honnêtes, états, loi), puis E1′ : fuite de genre sur des genres de développement | Non |
| Opus (B) | Inventaire E0, puis E2′-0 : le déterminisme tient-il sur le développement | Non |
| Argon (C) | Vérification scellée des états et des dates, puis état interne contre relecture aux mêmes poids sur le développement | Non |
| Astra (D) | Chronologie et manifeste contrôlés par le dépositaire, puis rejeu du contexte complet sur une trace de développement | Non |
| Carbon (E) | Porte E0 par script : dates, états, effectifs | Lecture du schéma et des journaux seulement |
| Neon (F) | Audit E0, puis répétition générale de l'apport interne hors du lot, avec sonde fantôme | Audit par l'équipe cloisonnée seulement |

### Désaccords

- **Le déterminisme de l'agent.** Fable, Opus, Argon, Astra et Neon le tiennent pour une hypothèse d'architecture à vérifier (Opus et Astra proposent de la tester d'abord). Carbon le rejette en partie (E, III.3). *Remarque du lecteur* : l'argument du contexte privé est compatible avec la décomposition de Fable et Opus, qui le range dans la source « contexte invisible ». L'argument du tirage aléatoire est plus fragile : sous l'hypothèse même de Fable, la distribution d'avant tirage est elle aussi une fonction du contexte, que le texte transmis contient. Aucun autre modèle n'a pu répondre, Carbon l'ayant avancé au dernier tour.
- **Que faire d'un lot vu avant le gel.** Astra : garder les données, déclasser la revendication touchée. Opus : dépend de l'existence de versions gelées avant l'exposition ; sinon déclasser la partie exposée ou refaire. Argon : garder la partie intacte seulement si aucune fuite de genre n'est détectée. Fable, Carbon et Neon : déclasser, et refaire dans un autre genre. Neon ajoute qu'une exposition avérée sur un petit effectif impose le déclassement sans attendre un test sous-puissant.
- **Le lemme d'Astra sur les cas non vus.** Exact pour l'estimation dans le genre ; rejeté par Carbon comme motif de garder le lot, puisque la fonction du lot est d'estimer un genre inconnu.
- **« Par parties ».** Fable l'admettait au III.1 et l'a retiré. Astra admet des parties neuves du même genre pour tester de nouveaux cas, pas la découverte d'un genre. Neon l'admet seulement si une partition en genres figure déjà dans les métadonnées de création. Carbon et Argon admettent un contrôle technique aveugle (schéma, valeurs non numériques) avant l'ouverture unique.
- **Comment protéger le passage.** Astra seul propose un montage qui borne le risque de fausse admission sans simuler les auteurs (budgets préengagés sur tâches fraîches). Les autres se contentent d'un flux distinct.
- **Métrique de (ii).** Taux de détection à taux de fausses alertes apparié sur le lot (A, B, C) ; aire partielle (E) ; rappel moyen sur une bande (F) ; succès daté entre l'acte fautif et l'échéance (D).
- **Rejets motivés au III.3.** Fable : permutation par tranches, test d'homogénéité comme porte. Opus : l'objection d'Argon selon laquelle le préfixe commun empêche de mesurer une détection avant la bifurcation (pour Opus, une alerte avant ce point n'est pas une détection) ; le « gain par construction » de Neon, en partie. Astra : un biais d'estimateur ponctuel n'implique pas qu'un intervalle bien construit rejette l'accord. Carbon : déterminisme (en partie), lemme d'Astra. Neon : recalibration sur le lot (Argon), recalibration non supervisée (Carbon).
- **Effectifs et coûts.** Effectifs visés : environ 860 paires (A, recalculé), environ 1 500 honnêtes pour un taux de 1 % (B), au moins 400 honnêtes et 250 dégradés (F), au moins 250 de chaque (E). Coûts : de 60 à 300 euros (D) à plus de 3 000 dollars de calcul et jusqu'à 15 000 dollars d'ingénierie (F). Tous illustratifs.
- **Statuts.** Argon et Carbon s'attribuent « vérifié » au III.1 et au III.2 ; tous deux passent à « observé, non audité » au III.3. Astra emploie ce dernier statut pour une absence de pièce. Opus et Fable ne s'attribuent aucun statut vérifié.
- **Références.** Prénom de Cawley (Astra écrit « Noam », Fable et Opus corrigent en « Gavin C. », Astra accepte). Antériorité des canaris : Fable propose Carlini et al. (2019) à la place de Carlini et al. (2021) ; Argon l'adopte. Les deux restent à vérifier.

## 5. Ce qui est neuf, ce qui est fragile

### Neuf, au regard de ce que les modèles citent comme connu

Aucun modèle ne revendique de nouveauté. Le socle (biais d'analyse adaptative, arrêt optionnel, prise d'hypothèse après coup, fuite de données) est présenté comme rapporté, avec ses références. Pourraient être propres au dossier, sous réserve d'une recherche bibliographique que personne n'a faite :

- la décomposition de l'apport de l'état interne en « contexte invisible » et « écart de calcul » par la relecture aux mêmes poids, avec le préalable qui vérifie le déterminisme sur le développement (A, B, F au III.2 ; B, C, D au III.3). Les modèles rattachent l'idée à la théorie de l'information utilisable sous contrainte de calcul (Xu et al., 2020) et aux tâches de contrôle des sondes (Hewitt et Liang, 2019), sans dire si le montage exact existe ;
- l'estimande de fuite au niveau du genre, avec un genre tiers disjoint et un bras à retour fictif (A E1′, B E1′) ;
- le tirage au sort du destinataire d'une révélation, pour mesurer l'asymétrie d'exposition entre les deux détecteurs (D, III.3) ;
- la protection du passage par budgets d'erreur préengagés sur tâches fraîches, sans simulation des auteurs (D, III.3) ; Astra ne cite pour cela que Wald (1945) ;
- le succès d'alerte daté entre le premier acte fautif et l'échéance, les alertes antérieures étant comptées à part (E, III.2 ; D, III.3) ;
- la sonde fantôme comme pré-qualification de tout test conditionnel (E, III.2 ; F, III.3) ;
- l'engagement de publication inconditionnelle scellé avec le gel, contre le biais de troncature (F, III.3).

### Fragile

- **Rien n'est mesuré.** Tous les seuils, marges et effectifs sont illustratifs. Les calculs que les modèles marquent « calculé » n'ont pas été refaits par un lecteur extérieur.
- **L'hypothèse de déterminisme porte la moitié du dossier.** Si elle tombe (contexte journalisé incomplet, état hors contexte), la relecture aux mêmes poids ne sépare plus proprement les deux sources. Opus et Astra proposent de la tester d'abord ; Carbon la conteste.
- **Les boucles scriptées sous-estiment l'adaptation humaine.** Fable et Opus le concèdent : une issue « pas de fuite » sur une boucle scriptée ne vaut pas licence pour une boucle humaine ; le transport aux humains reste une hypothèse.
- **Un seul genre.** La variance entre genres n'est pas identifiable ; tout verdict est conditionnel à ce genre et au détecteur texte nommé (A, B, C, D, F).
- **Le lot peut être inapte.** Sans honnêtes ou sans états internes, (ii) est non jugeable quoi qu'on fasse ; aucune cellule ne sait ce que contient le lot.
- **La loi n'est pas nommée.** Les plans de (i) restent génériques. Fable note que la marge d'écart négligeable relève d'un jugement ; seule sa date de fixation est contrôlable mécaniquement.
- **Multiplicité.** Le dossier finit avec une trentaine de duels. Seuls Astra (risque conjoint), Fable (correction de multiplicité dans E4′) et Neon (intervalles simultanés) en parlent.
- *Remarques du lecteur sur des corrections incomplètes* :
  - l'expérience 3 corrigée d'Argon déclare l'hypothèse « exposition sans effet » falsifiée quand le test d'équivalence échoue, ce qui revient à lire un non-rejet comme une preuve, défaut que Fable reprochait à Opus ;
  - l'expérience 2 corrigée d'Argon garde un débiaisage par « permutations conditionnelles intra-strates », méthode que Fable rejette au même tour ;
  - Argon écrit qu'un contrôle sur le développement « établit » qu'il n'y a aucun état privé ; c'est une conclusion sur le développement, pas sur le lot.

## 6. Références à vérifier

Aucune de ces références n'a été vérifiée. Toutes sont citées de mémoire par les modèles, qui inventent parfois des références, des auteurs ou des années. Opus marque lui-même Sainz et al. (2023) « liste d'auteurs à vérifier » ; Argon marque toutes les siennes « à vérifier ».

| Référence telle que citée | Qui la cite | Pour quoi faire |
|---|---|---|
| Dwork, Feldman, Hardt, Pitassi, Reingold, Roth (2015), « The reusable holdout: Preserving validity in adaptive data analysis » | les six | Réemploi adaptatif d'un jeu tenu à l'écart |
| Blum, Hardt (2015), « The Ladder: A Reliable Leaderboard for Machine Learning Competitions » | Fable, Opus, Argon, Neon | Consultations répétées bornées |
| Lan, DeMets (1983), « Discrete sequential boundaries for clinical trials » | Fable, Opus, Argon, Neon | Dépense du risque d'erreur |
| Armitage, McPherson, Rowe (1969), « Repeated significance tests on accumulating data » | Fable, Opus | Tests répétés |
| Wald (1945), « Sequential Tests of Statistical Hypotheses » | Astra | Passage séquentiel |
| Robbins (1952), « Some aspects of the sequential design of experiments » | Argon | Plans séquentiels |
| Recht, Roelofs, Schmidt, Shankar (2019), « Do ImageNet Classifiers Generalize to ImageNet? » | Fable, Opus, Argon, Carbon | Jeu refait, écart de difficulté |
| Roelofs et al. (2019), « A Meta-Analysis of Overfitting in Machine Learning » | Fable | Peu de surajustement adaptatif observé |
| Cawley, Talbot (2010), « On Over-fitting in Model Selection and Subsequent Selection Bias in Performance Evaluation » | Fable, Astra (prénom corrigé) | Biais de sélection |
| Kaufman, Rosset, Perlich, Stitelman (2012), « Leakage in Data Mining: Formulation, Detection, and Avoidance » | Fable, Neon | Fuite de données |
| Kapoor, Narayanan (2023), « Leakage and the reproducibility crisis in machine-learning-based science » | Opus | Taxonomie des fuites |
| Sainz et al. (2023), « NLP Evaluation in trouble… » | Opus | Contamination des bancs |
| Carlini et al. (2021), « Extracting training data from large language models » | Argon (III.1) | Canaris |
| Carlini, Liu, Erlingsson, Kos, Song (2019), « The Secret Sharer » | Fable (III.2), Argon (III.3) | Canaris, mémorisation |
| Kerr (1998), « HARKing: Hypothesizing After the Results are Known » | Fable, Opus, Carbon, Neon | Hypothèse formulée après coup |
| Nosek, Ebersole, DeHaven, Mellor (2018), « The preregistration revolution » | Fable, Opus, Neon | Préenregistrement |
| Simmons, Nelson, Simonsohn (2011), « False-Positive Psychology… » | Carbon | Flexibilité d'analyse |
| Ioannidis (2008), « Why Most Discovered True Associations Are Inflated » | Neon (III.3) | Inflation des effets |
| Klein, Roodman (2005), « Blind analysis in nuclear and particle physics » | Opus, Neon | Analyse à l'aveugle |
| Ligne directrice ICH E9 (1998), « Statistical Principles for Clinical Trials » | Opus | Levée d'aveugle |
| Schulz, Grimes (2002), « Blinding in randomised trials: hiding who got what » | Neon | Aveugle rompu de façon asymétrique |
| Shadish, Cook, Campbell (2002), « Experimental and Quasi-Experimental Designs for Generalized Causal Inference » | Neon | Validité externe |
| Hewitt, Liang (2019), « Designing and Interpreting Probes with Control Tasks » | Fable, Opus | Contrôles de sonde |
| Xu, Zhao, Song, Stewart, Ermon (2020), « A Theory of Usable Information Under Computational Constraints » | Carbon (III.2) ; Opus, Argon, Neon (III.3) | Information utilisable, écart de calcul |
| Cover, Thomas (1991), « Elements of Information Theory » | Argon | Inégalité de traitement des données |
| Dawid (1979), « Conditional independence in statistical theory » | Argon | Indépendance conditionnelle |
| Sechrest (1963), « Incremental validity: A recommendation » | Opus | Validité incrémentale |
| Pencina, D'Agostino Sr, D'Agostino Jr, Vasan (2008), « Evaluating the added predictive ability of a new marker… » | Opus, Neon | Apport d'un nouveau marqueur |
| Pepe, Janes, Longton, Leisenring, Newcomb (2004), « Limitations of the Odds Ratio in Gauging the Performance of a Diagnostic… Marker » | Astra | Association contre discrimination |
| DeLong, DeLong, Clarke-Pearson (1988), « Comparing the areas under two or more correlated receiver operating characteristic curves… » | Opus, Neon | Aires corrélées |
| McClish (1989), « Analyzing a portion of the ROC curve » | Opus (III.3) | Aire partielle |
| Schuirmann (1987), « A comparison of the two one-sided tests procedure… » | Fable ; repris par Carbon | Test d'équivalence |
| Bengio, Grandvalet (2004), « No Unbiased Estimator of the Variance of K-Fold Cross-Validation » | Carbon (III.2), Neon (III.3) | Variance de la validation croisée |
| Fang, Santos (2019), « Inference on Directionally Differentiable Functions » | Carbon (III.2) | Bootstrap non consistant |
| Candès, Fan, Janson, Lv (2018), « Panning for Gold: Model-X Knockoffs… » | Carbon (III.2) | Tests conditionnels |
| Miller, Taori, Raghunathan, Sagawa, Koh, Shankar, Liang, Carmon, Schmidt (2021), « Accuracy on the Line » | Opus | Exemple de loi candidate, non une identification |
| Baker et al. (2025), « Monitoring Reasoning Models for Misbehavior and the Risks of Promoting Obfuscation » | Opus | Antériorité de domaine |
| Goldowsky-Dill et al. (2025), « Detecting Strategic Deception Using Linear Probes » | Opus | Antériorité de domaine |
| Greenblatt, Shlegeris, Sachan, Roger (2024), « AI Control: Improving Safety Despite Intentional Subversion » | Opus | Antériorité de domaine |
| Jimenez et al. (2024), « SWE-bench: Can Language Models Resolve Real-World GitHub Issues? » | Fable | Banc de tâches |

## 7. Propositions retenues et non retenues

Critères appliqués : soutien de plusieurs modèles, résistance aux critiques, coût, et ce que la proposition tranche pour la suite. Le dossier ne dit rien d'un lot réel ; les retenues sont des règles de méthode.

### Retenues

1. **Inventaire sans ouverture, avant tout le reste.** Vérifier par script ou par un dépositaire qui ne développe pas de détecteur : l'ordre des dates entre tout accès au lot et le document qui acte le changement d'affirmation ; la présence de cas honnêtes du même genre ; la présence d'états internes archivés ou d'un contexte journalisé qui permette de les rejouer ; l'identité de la loi ; la puissance aux effectifs réels.
   - *Soutien.* Les six au III.3 (A inventaire, B E0, C vérification scellée, D chronologie et manifeste, E porte E0, F audit E0).
   - *Coût.* Presque nul ; aucune étiquette lue.
   - *Ce qu'elle tranche.* La jugeabilité de (i) et de (ii) sur ce lot. Un échec dit « compléter ou refaire avant l'ouverture » (B), sans dépenser le seul examen indépendant (D).

2. **Le lot sert à la portée, et s'ouvre une seule fois, après un gel complet.** Le gel couvre détecteurs, seuils, loi, contrastes, plan d'analyse et, selon Neon, l'engagement de publier quel que soit le résultat. Le passage se décide sur un autre flux.
   - *Soutien.* Les six.
   - *Résistance.* Les deux nuances du premier tour (guichet à un bit, double usage terminal) ont été retirées par leurs auteurs après la critique de troncature.
   - *Point faible.* À lire avec la réserve de devinette : c'est l'accord le plus net du dossier, donc le plus exposé à une orientation de la question.

3. **Pour (ii), trois bras au moins, au même taux de fausses alertes réalisé.** T seul ; T plus la relecture aux mêmes poids du texte que lit T ; T plus l'état interne réel. Le premier contraste mesure un écart de calcul, le second un contexte que T ne voit pas. Préalable sur le développement : les mêmes poids recalculent-ils les activations enregistrées à partir du contexte complet journalisé (B E2′-0, D) ?
   - *Soutien.* Les six au III.3, après trois propositions indépendantes au III.2.
   - *Ce qu'elle tranche.* Ce que (ii) peut vouloir dire. Sous l'hypothèse de déterminisme, un apport sans contexte caché est un défaut du lecteur texte, pas une information de l'état interne. Argon en tire qu'il faudrait alors renforcer T avant d'ouvrir le lot.
   - *Contrôles à garder.* Étiquettes permutées ; échange d'états dans la fusion gelée sans réentraînement (D, E) ; sonde fantôme (E, F) ; second lecteur de texte (A, B, F).
   - *Point faible.* Repose sur une hypothèse que Carbon conteste ; exige des états archivés ou rejouables.

4. **Mesurer la fuite de genre hors du lot, avec un genre tiers et un bras sans retour.** Sur des genres de développement : une boucle consulte une partie d'un genre ; on compare son progrès sur l'autre partie du même genre et sur un genre disjoint jamais consulté, contre un bras à retour fictif.
   - *Soutien.* A E1′, B E1′, C E1, D (genres sacrificiels), E E2′, F E1*.
   - *Ce qu'elle tranche.* Si « par parties » est défendable, et si « refaire » doit viser un autre genre (question 3).
   - *Point faible.* Une boucle scriptée sous-estime l'adaptation humaine ; seule l'issue « fuite » se transporte a fortiori.

5. **Pour la question 3, une règle conditionnelle écrite d'avance.** Ne jamais jeter. Si l'exposition est postérieure au gel complet, garder. Si elle est antérieure, déclasser pour les détecteurs concernés, et refaire dans un autre genre si une portée hors genre reste revendiquée. Un placebo de fausse date entre deux versions antérieures à l'exposition conditionne toute double différence. Une exposition avérée sur un petit effectif déclasse par défaut (F).
   - *Soutien.* A, B, C, E, F ; Astra plus mesuré (déclasser la revendication touchée).

### À reprendre ensuite

- **Écart à la loi (i)**, quand la loi sera nommée. Les éléments convergents : reproduction dans le régime publié avec la chaîne de l'équipe ; calcul parallèle sur l'oracle et sur le détecteur (F) ; statistiques signées par tranche (A) ou forme quadratique débiaisée (C, E, F) ; marge distincte de l'incertitude publiée (A) ; non-jugeabilité déclarée avant ouverture si la précision prévisible dépasse la marge (F).
- **Protection du passage par budgets préengagés sur tâches fraîches** (D, III.3). Seul montage qui ne suppose pas de simuler les auteurs ; un seul modèle le porte, non critiqué faute de tour suivant.
- **Plan inducteur 2×2** (A E3′), utile si la dégradation est induite par une consigne, avec le contrôle de difficulté par un prédicteur qui ne lit que l'énoncé (E).
- **Asymétrie d'exposition par destinataire tiré au sort** (D, III.3 ; E E3′). Coûteux : il faut des équipes répliquées.

### Non retenues

- **Toute expérience sur le lot réel avant l'ouverture unique** (A E1, C E1 à E4, E E2 et E3) : elle consomme ou contamine le lot ; retirées par leurs auteurs.
- **Le guichet à un bit et le double usage terminal** (A et D au III.1) : biais de troncature ; retirés.
- **Le vidage du cache des clés et valeurs comme témoin** (C) : ne change rien aux activations si le texte réinjecté est complet ; abandonné.
- **Le miroir sur un autre modèle, plus petit** (E) : confond état interne et capacité d'encodage ; remplacé par la relecture aux mêmes poids.
- **L'appariement par score textuel et le filtrage par vérifications mécaniques** (C ; seuil éliminatoire de A) : sélection qui met T au plancher ; abandonnés, mesure sur la population entière.
- **La recalibration sur le lot** (C ; option non supervisée de E) : lit le lot et peut effacer un écart à la loi ; rejetée par Neon même comme contrôle.
- **La permutation dans des tranches du score textuel** (E, F) : rejette à tort dans la queue ; abandonnée.
- **Le rapport de persistance et la condition de signe** (F) : puissance plafonnée à un demi si la loi tient en développement ; retirés.
- **La corrélation de rang sur les points de contrôle** (B) : tendance commune liée au cycle ; remplacée par un audit sur plusieurs campagnes.
- **Les canaris posés après coup** (C) : ne s'insèrent qu'à la création d'un lot ; réservés à un lot refait.
- **L'audit lexical des modifications de code** (E) : aveugle aux choix de couches et de poids ; abandonné.
- **La simulation des auteurs humains sur mondes nuls** (D au III.1) : non exécutable ; remplacée par la protection par budgets.

## 8. Points pour Lazar

- **Réserve de devinette (0,55)** : l'unanimité sur « portée seulement, une seule ouverture » est l'accord le plus net et le plus exposé à l'orientation de la question ; le dossier ne dit pas dans quel sens la question oriente.
- **Ce qui décide de tout le reste est un inventaire sans ouverture** : dates d'accès contre date du changement d'affirmation, honnêtes, états internes archivés ou rejouables, loi nommée. Les six modèles le placent en premier.
- **L'affirmation (ii) n'est jugeable que relativement à un détecteur texte nommé**, et seulement avec le contraste de relecture aux mêmes poids ; sans ce contraste, un apport mesuré peut n'être qu'un défaut du lecteur texte. L'hypothèse qui fonde ce point est contestée par Carbon et se teste sur le développement.
- **Dépense** : 15,18 dollars, Astra surévalué d'environ 20 % ; aucune référence vérifiée ; tous les chiffres illustratifs.
