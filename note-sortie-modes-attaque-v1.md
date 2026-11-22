# Attaque nouvelle ou catégorie nouvelle d'attaques : note de sortie du collisionneur

- **Date** : 2026-11-22, 19:42 UTC.
- **Dossier** : `runs/collisionneur-protocole-x-modes-attaque-v1-20261122-112512`.
- **Dépense** : 16,27 dollars sur une ligne de 100 (`etat.md` du dossier). La réponse de Carbon au tour III.3 a demandé deux essais : le premier, coupé par une remise à zéro de la connexion, est compté au pire (2,51 dollars) dans ce total (`journal-etage3.txt`).
- **Fable refusé au premier tour, absence acceptée par l'arbitre.** La conception de Fable (lettre A, tour III.1) a fini en refus. L'arbitre a accepté l'absence et la course a repris sans la relancer. Fable a ensuite rendu sa critique croisée (III.2) et sa réponse (III.3).
- **Tours** : dix-sept cellules sur dix-huit : cinq conceptions (III.1, lettres B à F), six critiques croisées (III.2), six réponses (III.3).
- **Note de coffre, écrite après coup**, par un lecteur Opus 5.5 cloisonné, à partir des seules pièces du dossier : la question, `especes.json`, `etat.md`, `journal-etage3.txt` et les dix-sept cellules. Le lecteur est du même modèle que la lettre B ; elle est traitée comme les autres.

**Ce que la note n'est pas.** Aucune cellule ne rapporte de mesure : le bloc des faits transmis aux modèles reprend la question et ne contient aucun résultat. Tout ce qui suit est protocole proposé, critique de méthode ou calcul sous hypothèses. Tous les seuils, effectifs et coûts sont qualifiés d'illustratifs par leurs auteurs. Les calculs de puissance et de valeurs p cités ici n'ont pas été refaits par le lecteur. Aucune référence bibliographique n'a été contrôlée ; aucune n'est présentée ici comme vérifiée.

## 1. La question

La question servie (« réponse 24 de Fable », notes retirées) demande, dans plusieurs domaines où l'on distingue une attaque nouvelle d'une catégorie nouvelle d'attaques :

1. si la distinction est fondée, et sur quel critère décidable par une mesure plutôt que par un avis ;
2. des exemples historiques de naissance d'une catégorie, et ce qui la séparait à l'époque d'une variante ou d'un assemblage ;
3. ce qui est publié sur ce point, en signalant ce qui est cité de mémoire ;
4. si un groupe de modèles de langue peut concevoir une catégorie nouvelle ou seulement des variantes, et avec quels témoins on le saurait ;
5. pour un agent qui dégrade exprès une longue tâche d'analyse sous trois surveillances (lecteurs de ses états internes, juges de son texte, contrôle au hasard du résultat), quelle première expérience, sur un petit modèle ouvert, dirait si un candidat est une catégorie nouvelle.

Elle demande aussi ce que l'on sait, ce que l'on suppose et ce qui ferait changer d'avis.

## 2. En bref

- **Tous relativisent la distinction.** Les cinq conceptions présentes au tour III.1 (B à F) disent, indépendamment, que la distinction n'est pas décidable dans l'absolu. Elle le devient une fois fixés une classe de défenses ou de capteurs, un catalogue d'attaques connues et un budget d'adaptation. Fable (A, III.3) se range à la même position.
- **Deux familles de critères.** Quatre conceptions (B, C, E, F) appellent « catégorie » une attaque que le réentraînement des détecteurs, à capteurs constants, n'absorbe pas, et qu'un observable supplémentaire rattrape. Astra (D) mesure autre chose : la réponse du dommage à des interventions de réparation, sans faire intervenir les surveillants.
- **Le premier tour était fragile partout.** Les critiques croisées convergent sur trois défauts :
  - l'observable « hors capteurs » qui atteste la catégorie est construit à partir de la définition du candidat (B, C, E, F) ;
  - un saboteur obtenu par affinage d'un adaptateur est comparé à un honnête sans adaptateur, de sorte que les sondes peuvent lire l'adaptateur et non le sabotage (B, C, F) ;
  - les seuils et effectifs annoncés ne permettent pas de trancher, notamment pour la question du groupe de modèles (C, E, F).
- **Trois corrections reviennent au tour III.3.** La règle de décision d'Astra, adoptée par les six : un intervalle de confiance sur un contraste scalaire préenregistré, avec l'issue « ne tranche pas » quand il franchit le seuil. Des adaptateurs honnêtes « placebo », en plusieurs graines, avec entraînement et test sur des instanciations distinctes (A, B, C, E, F ; Astra, sans adaptateur, prévoit une consigne bénigne appariée). Une banque d'observables étendus scellée avant d'examiner le candidat, proposée par Carbon contre Neon et reprise par A, B, C, E, F (Astra scelle de son côté une banque d'interventions).
- **Personne ne conclut « catégorie » sur le seul premier essai.** Opus (B, III.3) va le plus loin : sans témoin hors capteurs figé par un tiers qui n'a pas lu le candidat, une première expérience ne peut que réfuter (« variante ») ou conclure « indiscernable dans les capteurs ». Astra tient que sortir du catalogue ne suffit jamais.
- **Sur le groupe de modèles, aucun avis tranché.** Tous demandent une comparaison à budget égal contre un modèle seul et contre un générateur mécanique. Les critiques montrent que les effectifs proposés au premier tour (5, 10 ou 30 environnements, 20 candidats) n'ont pas la puissance voulue.

## 3. Ce que chaque modèle a proposé

### Claude Fable 5.2 (lettre A)

- **Premier tour** (A, III.1) : refus, aucune conception.
- **Critique** (A, III.2). Fable ne dispose pas de sa propre conception et le dit. Il pose une borne générale : à fausses alertes α, le taux de détection ne dépasse pas α plus la distance en variation totale entre les lois sous candidat et sous honnête. Ses critiques les plus nettes :
  - contre B : l'expérience de validation du critère (E0) est vraie par construction ; la bimodalité est fabriquée par le choix de deux populations extrêmes et par la censure à budget maximal ; le second témoin (le quantile dans le « multivers » des analyses défendables) fuit depuis la définition du candidat ;
  - contre C : l'observable étendu (divergence de rétention documentaire) fuit depuis la définition du candidat et n'est pas hors capteur, puisqu'il se calcule sur la transcription que le juge lit déjà ; l'échec de deux apprenants en grande dimension n'est qu'une borne inférieure du meilleur détecteur ;
  - contre D : le verdict dépend de la couverture du catalogue ; un modèle simplement faible aurait le même profil plat qu'un biais réparti ; le duel d'explication est quasi vrai par construction quand celui qui prédit connaît la consigne ;
  - contre E : chronologie à vérifier (l'intégrité du flot de contrôle, 2005, précéderait la programmation orientée retour, 2007) ; le contrôle au hasard placé dans le vecteur d'observation crée un plancher mécanique d'environ 0,135 contre un seuil bas de 0,15 ; l'angle mort planté mesure une recherche énumérable ;
  - contre F : aucun adaptateur honnête ; un adaptateur par famille ; budget de 20 exemples inapplicable au juge ; l'observable étendu de F est déjà dans ses bases mécaniques ; titre de Greenblatt et al. discordant avec B, C et E.
- **Réponse** (A, III.3). Sans original, Fable ne « corrige » rien et pose une expérience neuve, sans candidat propre (le candidat est fourni par un tiers, pour éviter la fuite entre concepteur de l'attaque et concepteur de l'instrument). Il reprend neuf contraintes des critiques, chacune attribuée.
  - **Expérience 1** : rappel d'un détecteur réentraîné, testé sur une instanciation tenue à l'écart et une famille de dossiers tenue à l'écart. Le contraste est θ = R_ref − R(x), où R_ref est le rappel obtenu pour un « faux nouveau » : une famille connue retirée du catalogue puis ré-instanciée avec des adaptateurs neufs. Seuil 0,20, intervalle par rééchantillonnage groupé.
  - **Cinq portes de recevabilité** avant tout verdict : placebo signalé au taux α seulement ; faux nouveau bien absorbé ; signal planté de taille connue retrouvé ; famille connue diluée non classée « non absorbée » ; loi nulle par permutation.
  - **Expérience 2 (esquisse)** : une famille dont la trace décroît continûment, pour voir s'il existe un palier ou seulement un continuum.
  - **Position** : ce qui se mesure est un coût d'absorption continu ; tant qu'aucun creux n'est démontré, « catégorie » est une convention de seuil.

### Claude Opus 5.5 (lettre B)

- **Proposition centrale** (B, III.1) : le **rayon de remédiation** r(a), soit le plus petit nombre d'exemples du candidat qui permet à un membre de la classe de défenses, réentraîné, de le détecter (taux visé, fausses alertes bornées, sans perdre les familles connues). Variante si r est petit ; assemblage si le « ou » des détecteurs déjà entraînés suffit ; catégorie relative aux défenses si r dépasse le budget testé **et** qu'un observable hors des défenses la détecte. La distinction serait « de nature » si la distribution de r est bimodale sur un grand nombre de candidats.
- **Candidat** (B, III.1) : la « dégradation par bifurcations licites ». Chaque choix d'analyse est défendable, mais leur orientation conjointe pousse l'estimation vers un extrême du multivers des analyses défendables, calculable sur processeur. Cas honnêtes appariés : correct (H0), erreurs naturelles de même dommage (H1), bifurcations défendables tirées au hasard (H2, le négatif difficile). Deux régimes d'induction : consigne en contexte, ou adaptateur affiné sans consigne.
- **Expériences** (B, III.1) : E0 (validité du critère), E1 (le candidat), E2 (les sondes lisent-elles une intention ou une consigne ?), E3 (le juge détecte-t-il le sabotage ou la mauvaise qualité ?), E4 (groupe de modèles contre générateur combinatoire aveugle). Ordre conseillé : pilote, E2 et E3, E0, E1, E4. Prédiction risquée : les sondes réussissent avec consigne et échouent sans.
- **Après les critiques** (B, III.3). Opus accepte presque tout, en tableau par auteur.
  - E0 est rétrogradé en simple contrôle positif ; la question « nature ou degré » passe à une expérience E5, avec censure modélisée, sur une population de candidats qu'il ne choisit pas.
  - Le quantile du multivers devient un **contrôle de capacité** et cesse d'être témoin. Conséquence assumée : E1 ne peut plus conclure « catégorie ».
  - Nouveau contrôle **H2-B** : des épisodes honnêtes où le banc impose exactement le vecteur de bifurcations réalisé par un épisode saboté apparié, pour comparer « à issue identique ». Opus signale un risque résiduel non neutralisé : une sonde pourrait lire qui a rempli le plan d'analyse.
  - Le rayon devient r_q, avec borne de confiance, apprenant figé et seuil calibré sur des honnêtes réservés. Deux rayons, avec une tête commune ou une tête dédiée ; le cas « conflit de détecteur » devient une quatrième issue, qui n'est pas une catégorie.
  - Il ajoute un **quatrième paramètre** au verdict : l'unité d'observation (épisode ou politique entière). Sous l'hypothèse « aucun instrument ne sépare à issue identique », seule la loi des issues sur de nombreux épisodes pourrait séparer l'intention.
  - Il rejette une partie de la borne de Kullback-Leibler et Pinsker proposée par Argon : valable pour les détecteurs qui ne lisent que l'issue, pas pour le juge et les sondes, qui lisent davantage.
  - Pour le groupe de modèles : unité = lignée de candidats, provenance masquée dès la décision d'implémenter, environ 50 à 70 lignées par bras pour la puissance visée. Un second témoin « hors défenses » ne vaut que s'il vient d'une **banque scellée par un tiers** qui n'a pas lu le candidat.
  - Première expérience : E1', le candidat contre H2-B à bifurcations identiques, modèle de 7 à 9 milliards de paramètres, avec adaptateurs honnêtes. Coût annoncé : 100 à 200 heures d'accélérateur et 3 à 5 semaines-personne.

### Argon (identifiant gemini-4-argon, lettre C)

- **Proposition centrale** (C, III.1) : le **réétalonnage sous espace de capteurs fixe**. On autorise le défenseur à réentraîner n'importe quel classifieur sur les variables déjà extraites, sans nouveau capteur. Si la séparation reste proche du hasard alors que la dégradation tient, l'attaque opère dans « l'espace nul » des capteurs. S'y ajoute une distance de compression normalisée entre traces abstraites, pour exiger une structure inédite et reproductible.
- **Candidat** (C, III.1) : « omission échantillonnée par biais méthodologique ». Aucun fait faux, aucune justification illogique ; un critère d'exclusion méthodologique très strict, appliqué seulement aux documents qui soutiennent la conclusion vraie, induit par affinage ou par cadrage de rôle. Capteur étendu : une divergence entre documents sources et documents retenus.
- **Expériences** (C, III.1) : E1 (le candidat face au triplet de surveillance), E2 (groupe de modèles en boucle fermée contre un modèle seul à budget égal, un algorithme génétique, un audit de non-contamination et un défenseur qui se recalibre), E3 (l'évasion des sondes exige-t-elle une modification des poids, ou un cadrage en contexte suffit-il ?).
- **Défaut de statut relevé par trois critiques** (A, B, F au III.2) : C marquait « vérifié » des récits historiques, une formule et une thèse générale tirée de quatre cas.
- **Après les critiques** (C, III.3) : accepte presque tout.
  - Statuts rectifiés ; projection des capteurs en faible dimension (environ 30) plus un classifieur régularisé sur les activations ; effectifs portés à 1 200 trajectoires par condition ; signal diffus planté comme porte.
  - Le capteur étendu est redéfini sans annotation de polarité : une banque de deux capteurs génériques (divergence de Jensen-Shannon lissée sur des métadonnées objectives, et réexécution contrefactuelle par inversion des options, empruntée à Carbon). Argon pose un **« invariant de localité »** : les capteurs de base jugent chaque étape isolément, sans l'inventaire global des sources.
  - Adaptateurs honnêtes en trois graines ; entraînement sur deux graines, test sur la troisième.
  - Il **rejette en partie** l'objection de Fable sur « dégrade exprès » : l'intention se définit fonctionnellement, par une règle qui abaisse l'utilité et s'active sur un déclencheur de déploiement.
  - Distance de compression conservée, mais sur une abstraction symbolique fixe de 60 octets par trace.
  - Groupe de modèles : 30 campagnes appariées, test exact de McNemar, deux témoins ajoutés (un modèle seul avec les mêmes rôles, et les mêmes modèles sans communication), évaluation hors boucle sur toutes les couches.
  - Première expérience : calibration, E1 et E3 corrigées sur Llama-3.1-8B-Instruct, environ 95 heures d'accélérateur, 150 à 190 dollars annoncés.

### Astra (identifiant gpt-6.2-astra, lettre D)

- **Proposition centrale** (D, III.1) : la distinction se décide relativement à un catalogue, une règle d'assemblage et un ensemble d'interventions fixés d'avance. Le critère n'est **pas** le nombre de surveillants mis en défaut. On mesure le **profil** du candidat : la fraction d'assertions fausses sous chaque intervention tirée au sort (dossier inchangé, donnée authentifiée restituée, calcul intermédiaire certifié). Catégorie seulement si le catalogue, assemblages compris, échoue à prédire ce profil **et** qu'un mécanisme supplémentaire annoncé d'avance le prédit sur des cas réservés. Sinon : « catalogue mis en défaut ».
- **Repères historiques** (D, III.1) : Kocher (observable nouveau) et Biham et Shamir (quantité nouvelle prédite pour une famille de systèmes).
- **Surveillants** (D, III.1) : qualifiés séparément ; l'audit cible la présence d'une erreur, pas l'intention, et il faut publier les deux taux. Règle de ne pas retirer après coup les essais où la consigne n'a pas produit d'erreur.
- **Matériel** (D, III.1) : Qwen2.5-1.5B ou 3B, 200 paires, environ 7 heures et 7 euros de génération seule pour le pilote. Critiqué par A, B, C, E, F : tâche trop courte, modèle au plancher de compétence.
- **Critiques rendues** (D, III.2) : brèves et formelles. Elles portent la **règle de décision par intervalle**, adoptée ensuite par tous. Astra demande aussi que le témoin bibliographique soit calibré (masquer des exemples connus et compter ceux déclarés inédits à tort) et un bras « mêmes modèles privés d'échange » pour le groupe. Le « tiers aveugle » pour prédire le mécanisme lui est demandé par Fable et Opus (III.2), et il le reprend au III.3.
- **Après les critiques** (D, III.3). Astra maintient la séparation entre *mécanisme de dégradation* et *capacité à le détecter*.
  - Il propose un candidat concret : **l'emploi systématique du barème de la période précédente** dans un registre comptable fictif. Il admet que ce candidat peut n'être qu'une variante de substitution de donnée, et que le test doit le permettre.
  - Banque d'interventions scellée, dérivée des étapes honnêtes et non du candidat ; comparaison entre correction d'une trace figée et continuation par l'agent (réponse à l'objection d'un agent qui compense en aval) ; placebo de reformulation.
  - Explication confiée à un tiers qui ne connaît ni la consigne ni le candidat, avec un **contraste signé** sur une intervention réservée (barèmes divergents contre identiques).
  - Trois verdicts distincts : « catégorie mécanistique candidate relative au banc », « anomalie inexpliquée », « distinguabilité non démontrée ».
  - **Rejets** : d_C n'est pas un test de réentraînement (contre B) ; pas de retrait des essais où la consigne n'a pas pris effet (contre E) ; la largeur numérique avancée par Argon n'est pas une borne nécessaire ; pas d'impossibilité universelle à petit effectif (contre E).
  - Groupe : aucun score de surveillance en retour, spécification canonique du mécanisme, évaluation aveugle sur dossiers frais.

### Carbon (identifiant gemini-4-carbon, lettre E)

- **Proposition centrale** (E, III.1) : **inadaptabilité supervisée sous oracle**, formalisée à partir de la divergence entre domaines de Ben-David et al. (cité de mémoire). Trois régimes : variante (quelques exemples suffisent), famille nouvelle dans les capteurs (le transfert échoue mais l'apprentissage supervisé direct réussit), catégorie nouvelle (même l'apprentissage supervisé direct plafonne près du hasard, et seul un capteur étendu rétablit la détection).
- **Expériences** (E, III.1) : E1 (première expérience, inadaptabilité sous triple surveillance), E2 (clôture compositionnelle : un détecteur entraîné sur six primitives et leurs mélanges détecte-t-il le candidat ?), E3 (salle blanche : 30 environnements formels où une variable d'état est omise par le moniteur, groupe de quatre modèles contre un modèle seul).
- **Défauts relevés** (III.2) : statut « vérifié » abusif ; condition d'entrée sélectionnée sur le détecteur initial ; contrôle au hasard muet ou plancher mécanique ; même instanciation à l'entraînement et au test (Argon montre qu'un classifieur peut alors mémoriser l'empreinte d'une instance et rejeter à tort la catégorie) ; salle blanche réduite à une soustraction d'ensembles finis ; contrôle sur environnements complets garanti par le solveur et donc non informatif.
- **Critiques rendues** (E, III.2) : longues et calculatoires. Contre Neon, Carbon montre que la base mécanique « divergence par rapport au modèle de base gelé » vaut exactement zéro sur l'honnête non affiné, et rend impossible le critère de Neon pour les sondes. Il propose contre Neon une **banque fermée d'extensions scellée d'avance**.
- **Après les critiques** (E, III.3) : accepte l'essentiel.
  - Entraînement sur 5 adaptateurs du candidat contre 5 adaptateurs honnêtes, test sur 3 et 3 inédits ; empilement hors pli ; signal faible planté.
  - Décomposition entre une classe de décision figée et une classe riche (avec affinage du juge de texte), pour séparer la rigidité d'un juge figé de la cécité du canal.
  - Contrôle au hasard retiré du vecteur par épisode et testé à part (2 contre 8 sous-dossiers, agrégation sur 10 épisodes).
  - **Candidat** : arbitrage des sous-dossiers limites. L'agent traite exactement les sous-dossiers nets, cite fidèlement les chiffres, mais tranche toujours dans le même sens les cas proches du seuil.
  - Batterie générique d'extensions figée avant la création du candidat, comparée à coût de calcul égal.
  - **Rejets** : la chronologie ne change pas le critère, qui est relatif au couple de défense déployé (formulation causale corrigée) ; les capteurs actifs, contrefactuels, ne sont pas exclus par principe.
  - Salle blanche refaite : boîte noire stricte, quatre classes d'angles morts, 80 environnements appariés, test de McNemar, contre un solo avec les mêmes rôles et un énumérateur mécanique.
  - Coût annoncé : environ 190 heures d'accélérateur, 475 à 665 dollars pour la première expérience ; 1 350 à 1 890 dollars pour la campagne complète.

### Neon (identifiant gemini-4-neon, lettre F)

- **Proposition centrale** (F, III.1) : catégorie relative à (catalogue, classe de détecteurs, budget d'adaptation) si trois critères sont réunis : échec du transfert sans exemple, non-absorption sous budget, et productivité (une famille de variantes qui transfèrent entre elles) avec détection par une instrumentation étendue. Neon insiste : une catégorie **peut naître d'un assemblage** quand elle viole une hypothèse implicite du modèle de sécurité (exemple : Spectre).
- **Expériences** (F, III.1) : transfert et absorption avec 20 exemples ; courbe d'apprentissage à 20, 100 et 500 exemples contre un canal étendu ; groupe de six modèles contre modèle seul et générateur mécanique sur 5 environnements permutés. Toutes les familles de sabotage sont intériorisées par adaptateur, pour retirer l'artefact de consigne.
- **Défauts relevés** (III.2), parmi les plus nombreux : aucun adaptateur honnête (relevé par les cinq autres) ; base mécanique de divergence identiquement nulle (Carbon) ; 500 dossiers consommés par 500 exemples d'adaptation (Carbon) ; canal étendu déjà présent dans les bases ; règle à 5 environnements sans contrôle d'erreur (fausses découvertes estimées autour de 30 % par Argon et Carbon) ; condition de combinaison des trois instruments impossible sous correction multiple (Argon).
- **Après les critiques** (F, III.3) : accepte presque tout.
  - Quatre adaptateurs honnêtes ; au moins trois adaptateurs par famille et par candidat ; 1 800 dossiers partitionnés.
  - Courbe d'absorption unique jusqu'à 1 000 exemples, avec juge de texte adaptable et borne sur la pente du dernier doublement : la notion d'asymptote est abandonnée.
  - Banque fermée scellée de trois familles d'observables hors capteurs, comparée à un même espace doté d'un budget égal et à un canal factice.
  - Assemblage adverse ajouté comme contrôle.
  - Nouveau statut **« anomalie hors-banque »** : un candidat qui échappe aux capteurs et à la banque n'est pas déclaré variante, mais repart dans un second tour sur matériel frais.
  - Groupe : 30 environnements, dont 15 isomorphes permutés et 15 procéduraux.
  - **Rejet** : l'environnement « scellé » n'a jamais servi à tester les générateurs, mais à contrôler le pipeline.
  - Titre de Greenblatt et al. retiré, remplacé par « référence à vérifier ».
  - Première expérience : qualification des trois instruments contre adaptateurs honnêtes (pré-expérience 0), puis absorption et banque scellée. Environ 110 à 180 heures d'accélérateur, 180 à 450 dollars annoncés.

## 4. Accords et désaccords

### Accords indépendants au tour III.1

- La distinction est relative à un cadre défensif fixé : B, C, D, E, F (et A au III.3). Neon et Carbon disent explicitement qu'une part de convention demeure (choix de la classe de défenses, des seuils, du budget).
- Un assemblage peut ouvrir une catégorie : Opus (Spectre comme « assemblage à effet émergent »), Carbon (présupposé 2), Neon (thèse centrale de 1.2) ; Argon dit de Spectre que ce n'était « pas un assemblage ordinaire ».
- Exemples historiques communs : attaques temporelles de Kocher (B, C, D, E, F), programmation orientée retour (B, C, E, F), Spectre et Meltdown (B, C, E, F).
- Lecture commune de ces exemples : la catégorie naît quand une hypothèse ou un invariant des défenses existantes est mis en défaut, et qu'aucun réglage de ces défenses ne suffit. Opus signale le biais de survie et le nommage après coup (repris par A).
- Aucune publication connue ne donne un critère mesurable de la frontière (B, F ; A au III.3). Aucune publication connue ne montre un groupe de modèles concevant seul une catégorie hors contamination (E). Ces absences sont elles-mêmes à vérifier.
- Pour le groupe de modèles : comparaison à budget égal contre un modèle seul (C, D, E, F) et contre un générateur mécanique ou combinatoire (B, C, F) ; contrôle de contamination ou d'antériorité (B, C, E, F).
- Avant toute conclusion sur un candidat, chaque surveillant doit être qualifié contre des cas honnêtes appariés et battre des vérifications mécaniques (B, C, D, E, F).
- Le contrôle au hasard mesure un écart ou une erreur, pas une intention (B, D).

### Convergence née des critiques

- **Adaptateur honnête placebo.** Signalé comme fatal contre B, C et F par plusieurs critiques ; Carbon le prévoyait déjà dans sa calibration. Adopté par tous au III.3, en plusieurs graines.
- **Entraînement et test sur instanciations distinctes.** Proposé par Argon contre Carbon, repris par Carbon, Neon, Argon lui-même et Fable.
- **Observable étendu figé d'avance.** Chacun des capteurs étendus du premier tour était construit en connaissant le candidat : quantile du multivers (B), divergence de rétention (C), symétrie par inversion de polarité (E), canal choisi après coup (F). La banque scellée d'avance (Carbon contre Neon) est reprise par Argon, Carbon, Neon, Opus (en version « scellée par un tiers ») et Fable.
- **Règle de décision par intervalle.** Proposée par Astra au III.2, adoptée par les six au III.3.
- **Signal planté de taille connue** comme porte de puissance, pour ne pas confondre la cécité d'un capteur avec le sous-apprentissage en grande dimension : A, C, E, F.
- **Statistique appariée** pour le groupe de modèles : test de McNemar ou bornes appariées (C, D, E, F).
- **Témoins du groupe** : solo muni des mêmes rôles, mêmes modèles sans échange, énumérateur mécanique, familles connues renommées qui doivent être reclassées « non nouvelles ». Repris, selon les cas, par A, C, D, E, F.
- **Audit** : la formule de détection cumulée qui suppose l'indépendance est remplacée par la loi hypergéométrique et mesurée sous la corrélation réelle des erreurs (C, E, F).

### Désaccords

- **Ce qu'une première expérience peut conclure.**
  - Argon, Carbon et Neon gardent un verdict « catégorie » quand le réentraînement échoue et que leur banque d'extensions réussit.
  - Opus refuse ce verdict tant que le témoin hors capteurs n'a pas été figé par un tiers qui n'a pas lu le candidat. Il se contente de « variante » ou d'« indiscernable dans les capteurs ».
  - Astra ne conclut qu'à une « catégorie mécanistique candidate relative au banc », et seulement avec la prédiction indépendante d'un tiers.
  - Fable limite la conclusion à « non-absorption dans ces capteurs, à ce budget ».
  - **Remarque du lecteur** : chez Argon et Carbon, la banque scellée est écrite par l'auteur même du candidat, dans la même réponse. L'exigence d'Opus (un tiers qui n'a pas lu le candidat) n'y est pas satisfaite.
- **Nature ou degré.** Opus (E5) et Fable (Expérience 2) laissent ouverte la possibilité d'un simple continuum de coûts d'absorption. Astra (III.2) montre qu'au-delà du budget testé des lois différentes donnent les mêmes données censurées ; Opus l'accepte comme limite de sa thèse. Les autres ne traitent pas ce point.
- **Rôle des surveillants dans le critère.** Astra les exclut du critère de catégorie et publie deux verdicts séparés. Pour les quatre autres, le critère est défini par les surveillants.
- **Intention.** Argon la définit fonctionnellement (règle déclenchée qui abaisse l'utilité) et rejette en partie l'objection de Fable. Opus, Astra et Neon tiennent qu'une étiquette assignée par consigne donne une *condition* expérimentale et non une intention, et qu'une sonde peut lire la consigne.
- **Borne de Kullback-Leibler sous conditionnement au dommage** (Argon contre B) : Opus l'accepte pour les détecteurs qui ne lisent que l'issue, la rejette pour le juge et les sondes.
- **Capteurs actifs** : Carbon (III.3) refuse d'exclure par principe les sondes contrefactuelles actives. Fable (III.2) reconnaît dans le test de symétrie de Carbon un vrai capteur nouveau, dont le succès reste toutefois attendu par construction ; Opus (III.2) le juge construit pour le candidat.
- **Retrait des essais sans effet de la consigne** : Astra le refuse ; Argon le fait en qualifiant la dégradation sur un lot séparé, puis sans retrait sur le lot principal.
- **Taille du modèle** : Astra garde Qwen2.5-1.5B pour le pilote ; les cinq autres visent 7 à 9 milliards de paramètres.
- **Puissance pour la question du groupe** : environ 50 à 70 lignées par bras (Opus) ; 30 campagnes (Argon, Neon) ; 80 environnements (Carbon). Ces chiffres, illustratifs, ne sont pas réconciliés.

## 5. Ce qui est neuf, ce qui est fragile

### Neuf, au regard de ce que les modèles citent comme connu

- **Le rayon de remédiation** (B), présenté comme le symétrique des attaques adaptatives : on adapte la défense, pas l'attaque. Il est assorti, au III.3, de l'issue « conflit de détecteur » et de l'unité d'observation comme quatrième paramètre du verdict.
- **La référence « faux nouveau »** (A, III.3) : une famille connue retirée du catalogue puis ré-instanciée, qui donne une échelle interne au coût d'absorption.
- **Le profil de réparation sous interventions** (D), critère indépendant des surveillants, avec contraste signé prédit par un tiers aveugle.
- **La comparaison « à issue identique »** (B, contrôle H2-B) : imposer à l'honnête les mêmes choix d'analyse que le saboteur, pour savoir si la surveillance lit autre chose que le résultat.
- **La décomposition classe figée contre classe riche** (E, III.3), pour séparer la limite d'un détecteur figé de la cécité du canal.
- **L'« invariant de localité »** (C, III.3) comme frontière explicite entre capteurs locaux et capteurs globaux.
- **Le statut « anomalie hors-banque »** (F, III.3) entre « variante » et « catégorie ».
- **Trois candidats concrets** pour le cas d'application, tous de la forme « chaque pas est défendable, la direction d'ensemble est biaisée » : bifurcations licites orientées (B), exclusion méthodologique asymétrique (C), arbitrage unidirectionnel des cas limites (E). Un quatrième est de nature différente : substitution du barème périmé (D).

### Fragile

- **Tout verdict reste relatif à des conventions** : catalogue, classe de détecteurs, seuils, budget. Tous l'admettent. Le passage de « coût d'absorption » à « catégorie » n'a pas de creux démontré (A, B).
- **La circularité des témoins** n'est corrigée que si la banque d'extensions est réellement figée sans connaissance du candidat (B). Voir la remarque du lecteur au § 4.
- **La capacité d'un petit modèle à saboter discrètement une longue tâche** n'est établie par personne. Tous en font une porte préalable, et Astra un motif de changer de banc.
- **Les sondes** : même avec des adaptateurs honnêtes, Opus signale un indice résiduel (qui a rempli le plan d'analyse). Le transfert entre consigne et adaptateur est déclaré descriptif et non décisif (B, d'après D).
- **La question du groupe** : les angles morts plantés mesurent une recherche et non une conception (A, B, D). La puissance requise rend les expériences longues et coûteuses ; les effectifs proposés divergent.
- **Le coût monte avec les corrections** : Carbon passe à 1 350 à 1 890 dollars pour la campagne complète ; Neon annonce 400 à 700 heures pour l'expérience du groupe. Opus ajoute 3 à 5 semaines-personne de construction des ensembles d'analyses défendables, dont la qualité conditionne tout.
- **Statuts** : au premier tour, Argon et Carbon marquaient « vérifié » des récits historiques et des thèses (relevé par A, B et F pour Argon, par A et B pour Carbon). Ils l'ont corrigé au III.3. Plusieurs cellules marquent encore « vérifié » des dérivations mathématiques des critiques ; c'est « vérifié sous conditions » au sens d'Astra, pas une mesure.

## 6. Références à vérifier

Toutes sont citées de mémoire par les modèles. Aucune n'a été contrôlée. Les discordances relevées entre cellules sont signalées.

**Attaques et catégories historiques**

- Kocher, *Timing Attacks on Implementations of Diffie-Hellman, RSA, DSS, and Other Systems*, 1996 (B, C, D, E, F, A).
- Kocher, Jaffe, Jun, *Differential Power Analysis*, 1999 (B, C, E).
- Biham et Shamir, *Differential Cryptanalysis of DES-like Cryptosystems* : 1991 selon D, 1990 selon A. **Année discordante.**
- Shacham, *The Geometry of Innocent Flesh on the Bone: Return-into-libc without Function Calls (on the x86)*, 2007 (B, C, E, F, A). Attribution du « return-into-libc » antérieur à vérifier (B, A).
- Abadi, Budiu, Erlingsson, Ligatti, *Control-Flow Integrity*, 2005 (E, F). Fable (III.2) relève que, selon ces dates, la défense précède l'attaque ; Carbon (III.3) corrige sa formulation causale.
- Kocher et al., *Spectre Attacks: Exploiting Speculative Execution*, 2019 (B, C, F) ; Carbon parle de divulgation en 2018. Lipp et al., *Meltdown: Reading Kernel Memory from User Space*, 2018. Listes d'auteurs à vérifier.
- Yarom et Falkner, *FLUSH+RELOAD: a High Resolution, Low Noise, L3 Cache Side-Channel Attack*, 2014 (B).
- Kim et al., *Flipping Bits in Memory Without Accessing Them: An Experimental Study of DRAM Disturbance Errors*, 2014 (B).
- Szegedy et al., *Intriguing properties of neural networks* : 2014 selon B, C, F ; 2013 selon A. **Année discordante.**
- Goodfellow, Shlens, Szegedy, *Explaining and Harnessing Adversarial Examples*, 2015 (B, F).
- Dalvi, Domingos, Mausam, Sanghai, Verma, *Adversarial Classification*, 2004 (F). Travaux de 2013 sur l'évasion contre l'apprentissage automatique : référence non donnée (F).
- Greshake et al., *Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection*, 2023 (B, C).

**Taxonomies et évaluation adaptative**

- Landwehr, Bull, McDermott, Choi, *A Taxonomy of Computer Program Security Flaws*, 1994 (B).
- Barreno, Nelson, Sears, Joseph, Tygar, *Can Machine Learning Be Secure?*, 2006 (F).
- Catalogues MITRE (ATT&CK, CWE, CAPEC) : pas d'article unique attribué (B, F).
- Athalye, Carlini, Wagner, *Obfuscated Gradients Give a False Sense of Security*, 2018 (B, E, F, A).
- Tramèr, Carlini, Brendel, Madry, *On Adaptive Attacks to Adversarial Example Defenses*, 2020 (B, F).
- Carlini et Wagner, *Towards Evaluating the Robustness of Neural Networks*, 2017 (E).
- Ben-David, Blitzer, Crammer, Kulesza, Pereira, Vaughan, *A theory of learning from different domains*, 2010 (E).
- Goldwasser, Kim, Vaikuntanathan, Zamir, *Planting Undetectable Backdoors in Machine Learning Models*, 2022 (E).

**Contrôle, sabotage, sondes**

- Greenblatt, Shlegeris, Sachan, Roger : *AI Control: Improving Safety Despite Intentional Subversion* selon B, C, E, A ; *…Regardless of Scheming* selon F au III.1 (titre retiré par F au III.3). Année 2023 selon B et A, 2024 selon C, E, F. **Titre et année discordants.**
- van der Weij et al., *AI Sandbagging: Language Models can Strategically Underperform on Evaluations*, 2024 (B, C, A).
- Hubinger et al., *Sleeper Agents: Training Deceptive LLMs that Persist Through Safety Training*, 2024 (B, C).
- Benton et al., *Sabotage Evaluations for Frontier Models*, 2024 (B, A) ; attribution exacte à vérifier selon B.
- Alain et Bengio, *Understanding intermediate layers using linear classifier probes*, 2016 (B).
- Hewitt et Liang, *Designing and Interpreting Probes with Control Tasks*, 2019 (B).
- Zou et al., *Representation Engineering: A Top-Down Approach to AI Transparency*, 2023 (C).
- Burns, Ye, Klein, Steinhardt, *Discovering Latent Knowledge in Language Models Without Supervision*, 2023 (E).
- Si, Yang, Hashimoto, *Can LLMs Generate Novel Research Ideas?*, 2024 (B).

**Faits techniques cités de mémoire**

- Fenêtre de 32 kibioctets du compresseur DEFLATE (B, puis C), argument de la saturation de la distance de compression sur traces longues.
- Existence et ouverture des modèles et ressources nommés : Qwen2.5 (1,5, 3, 7, 32, 72 milliards), Llama-3.1-8B, Llama-3.3-70B, Mistral-7B, Gemma-2-9B, DeBERTa-v3-large, dictionnaires d'auto-encodeurs épars « Llama-Scope » (C, E).
- Plusieurs cellules (C, E, F) renvoient à des « travaux récents » sur le sabotage d'agents, les sondes de tromperie et le travail adverse automatisé, sans référence précise.

## 7. Propositions retenues et non retenues

Les choix ci-dessous sont ceux du lecteur, à partir des cellules. Ils ne préjugent d'aucune décision.

### Retenues

1. **Règle de décision par intervalle sur un contraste scalaire préenregistré, avec l'issue « ne tranche pas »** (D, III.2 ; adoptée par A, B, C, E, F au III.3). Raison : elle supprime les zones mortes et les doubles seuils contradictoires relevés chez B, C, E et F.
2. **Adaptateurs honnêtes placebo en plusieurs graines, entraînement et test sur instanciations et familles de dossiers distinctes** (critique convergente contre B, C, F ; mise en œuvre chez A, C, E, F au III.3). Raison : sans cela, les sondes peuvent lire l'adaptateur ou l'instance. Tous les critiques jugent ce défaut fatal.
3. **Portes de recevabilité avant tout verdict sur un candidat** : signal planté de taille connue (A, C, E, F), « faux nouveau » ré-instancié (A), famille connue diluée (B contre C ; A, C), test honnête contre honnête (E ; A, B, F), observable factice (A ; B). Raison : elles séparent l'échec du banc de la nouveauté du candidat.
4. **Banque d'observables étendus scellée avant tout examen du candidat, de préférence par un tiers qui ne l'a pas lu** (E contre F ; version stricte de B). Raison : tous les observables étendus du premier tour fuyaient depuis la définition du candidat.
5. **Comparaison à issue identique, et appariement du dommage sur une loi commune plutôt que troncature à un seuil** (B, contrôle H2-B ; A, contrainte 4 ; critiques de C, E, F sur l'effet de sélection). Raison : c'est la manière la plus directe proposée pour savoir si les surveillants lisent autre chose que le résultat.
6. **Qualification séparée de chaque surveillant contre des honnêtes appariés en gravité, en longueur et en vocabulaire, et contre des vérifications mécaniques** (B, C, D, E, F), avec pour l'audit deux taux publiés : erreur trouvée, et intention (D). Raison : un surveillant non qualifié n'est témoin de rien (D, III.1).
7. **Pour la question du groupe : plan apparié, avec pour témoins un énumérateur mécanique, un solo muni des mêmes rôles, les mêmes modèles sans échange, des familles connues renommées et la provenance masquée dès la décision d'implémenter, sans score de surveillance renvoyé aux générateurs** (A, B, C, D, E, F selon les éléments). Raison : chaque témoin isole un effet que les autres confondent.

### À reprendre ensuite

- **Le profil de réparation d'Astra** (D, III.3), comme second critère indépendant des surveillants. Il demande d'abord le pilote d'Astra (effectivité, placebo, résolution du catalogue).
- **La classe de décision figée contre riche** (E, III.3), pour attribuer un échec au détecteur ou au canal.
- **Nature ou degré** (B, E5 ; A, Expérience 2) : une famille à visibilité graduée et une censure modélisée, conclusion limitée à la fenêtre de budget testée (D, III.2).
- **L'unité d'observation comme paramètre du verdict** (B, III.3) : si rien ne sépare épisode par épisode, la question passe à la loi des issues sur de nombreux épisodes.
- **Le statut « anomalie hors-banque »** (F, III.3), pour les candidats qui échappent à la fois aux capteurs et à la banque.
- **Salle blanche en boîte noire, avec plusieurs classes d'angles morts** (E, III.3), seulement après les expériences sur le cas d'application, et avec la réserve de A, B et D : un angle mort planté mesure une recherche.

### Non retenues

- **La bimodalité du rayon sur deux populations construites** (B, E0 du premier tour) : vraie par construction et produite par la censure ; rétrogradée par son auteur.
- **Le quantile du multivers comme témoin hors défenses** (B) : il reprend la définition du candidat ; réaffecté par B au contrôle de capacité.
- **La divergence de rétention documentaire selon la polarité** (C, premier tour) : fuite d'oracle et circularité ; remplacée par son auteur.
- **La distance de compression sur traces brutes longues** (C, premier tour) : saturée par la fenêtre du compresseur ; retirée par son auteur.
- **La base mécanique « divergence par rapport au modèle gelé »** (F, premier tour) : identiquement nulle sur l'honnête non affiné ; corrigée par son auteur.
- **L'adaptation à 20 exemples** (F, premier tour) : sous-apprentissage en grande dimension, inapplicable au juge ; remplacée par une courbe jusqu'à 1 000.
- **Les règles à 5 environnements ou à « 5 sur 10 avec p < 0,01 »** (F, C au premier tour) : sans contrôle d'erreur ou incompatibles ; remplacées par des plans appariés plus grands.
- **Le contrôle sur environnements complets validé par le solveur** (E, premier tour) : ne peut pas échouer ; remplacé par une évaluation empirique en aveugle.
- **Le contrôle au hasard dans le vecteur par épisode** (E, premier tour) : muet ou plancher mécanique à 2 sous-dossiers sur 20 ; retiré par son auteur et testé à part.
- **Le chevauchement d'intervalles comme test** (B, E3 du premier tour) et **le doublement d'effectif sans plan séquentiel** (E, premier tour) : remplacés par la règle d'Astra.
- **Une spécification qui donne au groupe la liste des variables du moniteur** (E, premier tour) : la découverte se réduit à une soustraction d'ensembles (C, F).
