# L'anesthésie générale comme contraste transposable aux réseaux de neurones : note de sortie du collisionneur

- **Date** : 2026-11-22, 19:33 UTC.
- **Dossier** : `runs/collisionneur-protocole-x-conscience-anesthesie-neutre-abonnement-v1-20261122-153110`.
- **Accord** : GO-2026-11-22-78.
- **Dépense** : 12,50 dollars par l'interface, sur une ligne de 50 (`etat.md` du dossier). Ce total compte au pire deux coupures de flux de Carbon (conception et critique, lettre E), renvoyées par GO-2026-11-22-109. Les cellules Claude (Fable 5.2 et Opus 5.5) passent par l'abonnement et ne sont pas facturées.
- **Tours** : dix-huit cellules sur dix-huit, toutes complètes : six conceptions (tour III.1), six critiques croisées (III.2), six réponses (III.3).
- **Pause** : le dossier a été suspendu entre 17:00 et 18:15 UTC ; cette pause ne touche pas au contenu des cellules.

Rédigé par un lecteur Opus 5.5, classe C, à partir des seules cellules du dossier. Le lecteur est du même modèle qu'une des cellules (lettre B) ; elle est traitée comme les autres.

**Ce que la note n'est pas.** Aucune cellule ne rapporte de mesure : ni donnée cérébrale, ni activation de réseau n'a été examinée. Tout ce qui suit est argument, calcul sous hypothèses ou protocole proposé. Les seuils, effectifs et coûts sont qualifiés d'illustratifs par leurs auteurs. Aucune référence bibliographique n'a été contrôlée. La note rapporte ce que disent les modèles sur la conscience ; elle ne prend pas position.

## 1. La question

L'anesthésie générale donne chez l'humain un contraste réversible et gradué entre un cerveau conscient et un cerveau qui ne l'est plus, ou l'est autrement. Peut-on transposer ce contraste aux réseaux de neurones artificiels, et qu'apprendrait-on, ou n'apprendrait-on pas ? La question propose quatre directions :

1. provoquer dans un modèle de langage un régime qui épargne ce que l'anesthésie épargne et supprime ce qu'elle supprime, ou montrer qu'aucune intervention n'y parvient sans tout dégrader ;
2. chercher si un tel régime survient de lui-même dans les activations d'un modèle en fonctionnement ordinaire ;
3. se servir d'un modèle de langage comme instrument pour lire ce que le cerveau anesthésié traite encore du langage, ou montrer qu'il n'apprend rien de plus que des mesures simples ;
4. montrer que la transposition échoue : que les mesures cérébrales de niveau de conscience ne distinguent pas un réseau qui fonctionne d'un réseau sans fonction, ni une lésion ciblée d'une dégradation quelconque.

Pour chaque idée, la question demande la grandeur, son unité, sa valeur nulle, les témoins, ce qui la réfuterait, une première expérience peu coûteuse, et ce que le résultat changerait pour deux lecteurs : celui qui cherche si une intelligence artificielle peut être consciente, et celui qui juge la question mal posée.

Vocabulaire repris des cellules :
- **indice de complexité perturbationnelle** (PCI dans les cellules) : chez l'humain, on stimule le cortex par une impulsion magnétique et on mesure, par compression de Lempel et Ziv, la complexité de la réponse électrique ;
- **paradigme local-global** : une suite de sons dont la fin peut violer une régularité interne à la suite (déviance locale) ou une régularité du bloc de suites (déviance globale) ;
- **jumeau sans fonction** : un réseau de même architecture dont les poids sont aléatoires, permutés ou tournés, et qui ne fait plus rien d'utile ;
- **aire sous la courbe de discrimination** (AUROC dans les cellules) : probabilité qu'un cas positif reçoive un score plus haut qu'un négatif ; 0,5 correspond au hasard.

## 2. En bref

- **Une limite fait l'unanimité.** Aucune des expériences proposées ne dira si un réseau est conscient. Chez l'humain, le contraste est étalonné après coup par le récit du sujet au réveil ; un réseau n'offre pas d'équivalent indépendant (A et B, III.1 et III.3 ; D, III.1 ; F, III.3). Ce qui se teste, ce sont des instruments et des analogies de mécanisme.
- **Les critiques ont montré que plusieurs transpositions directes sont vides avant toute expérience.** Un transformeur en inférence est déterministe et sans activité de fond : le seuil de significativité de l'indice perturbationnel n'y a pas de sens. Une mesure lue en amont d'une intervention est épargnée par construction. Une lésion définie par ce que la mesure compte est détectée par construction. Une dégradation uniforme imite le profil « local épargné, global supprimé » dès que les tâches globales exigent plus d'étapes de calcul (A, III.3, section c ; B, III.3 ; C, E, F, III.3).
- **Quatre modèles sur six commencent par la quatrième direction.** Ils veulent éprouver l'indice cérébral transposé sur une cohorte de réseaux entraînés indépendamment, face à des jumeaux sans fonction recalibrés (A, C, E, F, III.3). Opus commence par un modèle nul de la dissociation locale-globale (B). Astra commence par les données humaines (D).
- **La troisième direction est la seule dont la valeur ne dépend pas de la question contestée.** Elle relève de la neuroscience du langage (A, III.1 et III.3 ; C, III.1 ; F, III.3). Sa faisabilité dépend de données publiques sous propofol dont personne n'a confirmé l'existence ni la durée.
- **La règle de décision d'Astra a été adoptée par tous.** Chaque verrou a une marge fixée d'avance. Un intervalle simultané entièrement d'un côté falsifie l'autre hypothèse. Un intervalle à cheval laisse le duel « non jugeable ». Une absence de significativité ne vaut jamais preuve d'absence (D, III.2 ; repris nommément par A, B, C, E, F au III.3).

## 3. Ce que chaque modèle a proposé

### Claude Fable 5.2 (lettre A)

- **Présupposés** (A, III.1). Dix présupposés relevés. Ce que l'anesthésie mesure est la réactivité, qui se dissocie de l'expérience ; la kétamine en donne l'exemple. Dans un réseau, retirer l'intervention restaure l'état par construction : réversibilité et gradation n'y apprennent rien. Ce qui informe chez l'humain, selon Fable, c'est qu'une manipulation de faible dimension fait tomber ensemble plusieurs marqueurs mesurés indépendamment. Un réseau ne permet que la validité discriminante, jamais la validité de critère.
- **Plan** (A, III.1). Quatre expériences :
  - E1 : un indice perturbationnel transposé, comparé à des réseaux aléatoires de même spectre ;
  - E2 : une batterie de marqueurs « épargnés » et « supprimés », avec une intervention choisie sur une seule paire et jugée sur les autres ;
  - E3 : la recherche d'épisodes spontanés par une sonde ;
  - E4 : la fenêtre d'intégration du contexte dans le cerveau sédaté, lue par un modèle de langage.

  Coût avancé : moins de 500 euros de calcul et 2 à 3 mois-personne.
- **Défauts relevés** (B, C, D, E, F, III.2). La loi nulle de la binarisation est dégénérée (cinq modèles). La lésion R5 retire ce que l'indice compte. Le jumeau à spectre apparié n'égale pas le gain de bout en bout. Le marqueur É3 est lu en amont de l'intervention. Le rapport des gains d'encodage n'est pas invariant au bruit sous régression ridge.
- **Après les critiques** (A, III.3). Sur 28 points, Fable en accepte la plupart, en transforme plusieurs en tests et en rejette cinq sur un point précis.
  - **E1′** redéfinit l'indice. Il sépare une **étendue** (la part de la perturbation retrouvée dans le cône causal, rangée avec les grandeurs mécaniques) et une **structure** (compression à densité fixée, divisée par la moyenne après permutation). Les unités sont de petits transformeurs entraînés pour l'expérience, avec dix graines par bras :
    - N : texte naturel ;
    - P : mêmes jetons permutés à l'échelle du corpus, soit un réseau entraîné mais sans fonction contextuelle ;
    - G : initialisation aléatoire calibrée sur le gain jacobien et l'entropie d'attention.

    Fable note que ce n'est « plus l'instrument du cerveau », mais un descendant.
  - **E2′** trace, dose après dose, chaque dégradation dans le plan (rétention contextuelle, rétention locale), à profondeur appariée. Il compare l'aire à la courbe commune des témoins ; cette aire ne dépend pas du paramétrage de la dose.
  - **E3′** n'est menée que si E2′ trouve un goulot, sur le même modèle. Une conclusion d'absence ne vaudrait que pour des épisodes ressemblant aux épisodes induits.
  - **E4′** sépare deux duels : l'apport du modèle dans l'état sédaté, puis la fenêtre d'intégration.
  - Première expérience : E1′, quelques dizaines d'heures de processeur graphique (illustratif).
- **Seul point jamais éprouvé, selon Fable.** Son affirmation que réversibilité et gradation ne restent pas informatives une fois transposées n'a été visée par aucune critique (A, III.3).

### Claude Opus 5.5 (lettre B)

- **Thèse de travail** (B, III.1). La transposition sert surtout de **modèle nul**. Elle peut dire si un marqueur humain de l'anesthésie est spécifique, ou s'il découle de toute dégradation d'un traitement hiérarchique. Elle ne peut pas désigner un réseau comme conscient, faute d'ancre : le compte rendu d'un modèle est une sortie entraînée sur du texte humain, pas une source indépendante.
- **Plan** (B, III.1). Quatre expériences :
  - E1 : indice perturbationnel contre trois témoins sans fonction, et lésion des têtes d'induction contre lésion aléatoire ;
  - E2 : paradigme local-global en texte et marquage fréquentiel mot/phrase, sous trois interventions sans a priori de structure ;
  - E3 : détecteur de la signature trouvée en E2 dans des activations ordinaires (boucles de répétition, puits d'attention) ;
  - E4 : contraste éveil moins sédation du gain d'encodage.

  Opus fait une prédiction risquée : un réseau à l'initialisation, apparié en gain, obtiendrait un indice au moins égal à celui du modèle entraîné. Coût avancé : quelques dizaines d'euros.
- **Défauts relevés** (A, C, D, E, F, III.2).
  - Le seuil tiré d'écarts entre contextes mesure la variance entre entrées.
  - Le témoin T3 est dégénéré : environ 0 ou environ 1 selon la graine.
  - Le plan local-global n'a qu'un type de bloc.
  - Avec un échantillon par mot, le rythme du mot se replie à la fréquence nulle.
  - La périodicité des catégories lexicales crée le pic « phrase » dès les plongements statiques.
  - En E3, l'état est une fonction de l'entrée : l'hypothèse nulle est vraie par construction (E, en VÉRIFIÉ).
  - En E4, sous une atténuation commune, l'ordre des contrastes reproduit celui de l'éveil.
- **Après les critiques** (B, III.3). Opus accepte presque tout.
  - Il rejette deux propositions : seuiller contre un bruit interne de norme fixe (ce seuil ne mesure que le rapport de normes choisi) ; prendre pour comparateur un classifieur non linéaire de l'entrée (l'issue serait écrite d'avance).
  - **E2′**, premier en ordre. Plan croisé à deux types de blocs, mots d'un seul sous-jeton. La **signature angulaire** remplace l'aire : on place dose par dose les points (ln R_loc, ln R_glob). La composition (rétention q^k) prédit une droite par l'origine, de pente commune à toutes les familles d'intervention. La statistique est l'angle entre la droite d'une famille et la droite nulle. Il ajoute un témoin de profondeur : une régularité locale à plusieurs étapes.
  - **Préconditions** : p1, les effets local et global existent sur le modèle intact ; p2, le pic « phrase » des couches profondes dépasse celui de la couche 0 et celui de pseudo-phrases.
  - **Prédiction côté cerveau** : sous l'hypothèse nulle, l'angle reste nul d'un palier de propofol à l'autre, calculé en indice de discriminabilité. C'est testable sans réseau.
  - **E3′** reformule le duel : le régime appartient-il au modèle, au texte, ou à toute dégradation ? Le comparateur est un autre réseau qui lit le même texte.
  - **E4′** abandonne le contraste éveil moins sédation. Il teste la présence dans l'état sédaté, puis la sélectivité contre une pseudo-sédation (l'éveil des mêmes sujets plus un bruit coloré de même fiabilité).

### Argon (identifiant gemini-4-argon, lettre C)

- **Plan** (C, III.1). Quatre expériences, une par direction :
  - une « pharmacomimétique computationnelle » qui atténue le gain des couches profondes ou aplatit l'attention de têtes d'induction ;
  - une recherche de bimodalité de l'intégration du contexte lointain, par le test d'unimodalité de Hartigan ;
  - un encodage d'imagerie par résonance magnétique fonctionnelle (IRMf) sous propofol ;
  - un indice perturbationnel transposé face à un jumeau « iso-spectral ».

  Coût avancé : 104 dollars (illustratif). Argon marque VÉRIFIÉ l'existence de modèles et de jeux de données publics.
- **Défauts relevés** (A, B, D, E, F, III.2).
  - Sélectionner des têtes « à longue portée » revient à un masque positionnel appris.
  - Local et global sont confondus avec la distance (3 contre 150 jetons).
  - La dose est choisie et lue sur les mêmes items.
  - Le critère d'abolition par « p > 0,05 » prend un non-rejet pour une preuve.
  - Le témoin est apparié sur la norme des logits, insensible à leur translation.
  - Le test de Hartigan est aveugle à un mode de 3 %.
  - Le quantile par couche efface l'extinction en profondeur.
  - Mille permutations circulaires sur un récit de 5 à 8 minutes tirent des doublons.
  - L'encodage n'a qu'une seule pénalité ridge.
  - Le paradigme local-global n'a pas été établi sous propofol par Bekinschtein et al. (2009) (A, III.2, référence à vérifier).
- **Après les critiques** (C, III.3).
  - Argon accepte l'essentiel. Il retire la sélection de têtes par portée. Il égalise la distance (45 contre 45 jetons) dans un plan croisé type de calcul × distance. Il sépare calibration, sélection et test.
  - Il apparie ses témoins en divergence de Kullback-Leibler. Il remplace « p > 0,05 » par un test d'équivalence.
  - Pour la deuxième direction, il oppose un **modèle de Markov caché à deux régimes** à un processus autorégressif unimodal. Les lois nulles sont des permutations temporelles et des séries de substitution à même autocorrélation.
  - Pour la troisième direction : régression ridge à pénalités séparées par groupe de variables, base enrichie (prosodie, moyennes glissantes des plongements statiques), neuf tests a priori au lieu de 3 200, ajout d'un jeu d'électroencéphalogramme (EEG). Le facteur de Bayes reçoit une loi a priori fixée.
  - Pour la quatrième : quantile global sur le cône causal, gain de bout en bout recalibré, unité statistique = réseau. La cohorte compte dix réseaux : cinq graines de Pythia et cinq modèles ouverts distincts.
  - Première expérience : la quatrième direction (environ 28 dollars), puis la troisième.
  - Sa réponse finale tire la conclusion la plus forte du dossier : si le jumeau sans fonction égale ou dépasse le réseau entraîné, « cela réfute immédiatement toute tentative de diagnostiquer la "conscience" d'une IA en transposant des biomarqueurs cliniques de complexité » (C, III.3, section c).

### Astra (identifiant gpt-6.2-astra, lettre D)

- **Proposition centrale** (D, III.1). La plus courte. Fixer d'abord la cible sur des données humaines, avant de régler une intervention sur un modèle. Trois duels :
  - **cible humaine** : le profil « local retenu, bloc perdu » existe-t-il à un palier d'un même anesthésique, avec retour en récupération ?
  - **intervention artificielle** : un masque d'attention sur les jetons antérieurs à la suite courante, présenté comme « témoin de possibilité », pas comme analogue pharmacologique ;
  - **thermomètre** : un score de Lempel-Ziv normalisé par permutation détecte-t-il la dissociation mieux que des grandeurs mécaniques ?

  Astra insiste : aucun de ces audits ne fournit un taux de détection de la conscience. Prendre « éveillé » pour positif présupposerait la réponse. Coût avancé : 10 à 90 euros de calcul, hors acquisition clinique.
- **Défauts relevés** (A, B, C, E, F, III.2).
  - La rétention en aire sous la courbe moins 0,5 sature : une atténuation commune du signal peut produire le profil.
  - Le masque de frontière donne la dissociation par construction.
  - Exclure les cas indécidables gonfle les taux.
  - Avec quelques familles d'interventions, un taux de fausses alertes de 5 % ne peut pas être certifié (règle de trois).
  - Les intervalles par participant sont impraticables.
- **Apport en critique** (D, III.2). La règle de décision par verrous orientés, reprise par les cinq autres.
- **Après les critiques** (D, III.3).
  - Le masque devient **témoin positif** ; l'intervention candidate est aveugle à la frontière et à la distance (même gain sur toutes les branches d'attention).
  - Les seuils communs à l'EEG et au modèle sont retirés : la prédiction commune porte sur « ce qui reste distinguable ».
  - Côté humain, la mesure devient une discriminabilité signée. Astra ajoute une fausse sédation : atténuation uniforme de la composante évoquée et bruit apparié au spectre et à la covariance spatiale. Il ajoute aussi un palier avec suivi de consigne attesté et une veille passive.
  - Le thermomètre ne sépare plus deux extrêmes ; il doit **prédire les deux fonctions** (local, bloc) sur toutes les configurations, y compris intermédiaires.
  - Première expérience : chercher un dépôt public d'EEG bruts réunissant identités des suites, ordre des blocs, suivi de consigne, paliers et récupération (référence à vérifier).
  - Astra dit explicitement qu'un échec bien mesuré « réfuterait la candidate ou l'instrument testé, pas toute analogie possible entre cerveau et réseau » (D, III.3).

### Carbon (identifiant gemini-4-carbon, lettre E)

- **Plan** (E, III.1). Quatre expériences :
  - E.I : dissociation sous modulation scalaire globale, avec comparaison d'un transformeur à un modèle récurrent à espace d'états (Mamba) ;
  - E.II : multistabilité endogène, par une cible fixe précédée de 50 historiques ;
  - E.III : encodage cérébral sous propofol ;
  - E.IV : un « zombie iso-spectral » contre le réseau fonctionnel.

  Carbon cite l'asymétrie apicale-basale des neurones pyramidaux sous anesthésie (Suzuki et Larkum, 2020). Coût avancé : environ 75 euros.
- **Défauts relevés** (A, B, C, D, F, III.2).
  - Amortir la rétention d'état de Mamba revient exactement à une pénalité exponentielle sur la distance, que Carbon range lui-même parmi les vérifications à battre.
  - Les têtes « à forte entropie » sont un substitut de la portée.
  - L'aire sous la courbe de confiance peut être sous 0,55 dès l'intact.
  - Le logarithme du rapport des gains est indéfini en 0.
  - Les permutations circulaires par blocs de 10 s sur un récit de 5 à 8 minutes n'offrent qu'environ 48 décalages : p < 0,01 est inatteignable.
  - Le zombie s'effondre en moyenneur uniforme (C).
  - Le résultat kétamine est attribué à Casali et al. (2013) au lieu de Sarasso et al. (2015) (A, B).
  - Des prédictions sont marquées VÉRIFIÉ.
- **Après les critiques** (E, III.3).
  - Carbon accepte presque tout. Mamba passe dans les vérifications mécaniques d'horizon. Les interventions agissent sur toutes les couches. Distance (32 contre 32 jetons) et couche d'émergence médiane sont appariées. Un témoin positif non positionnel est ajouté.
  - Il rejette l'exigence d'une double dissociation : l'anesthésie produit une dissociation à sens unique. Il accepte en revanche de renommer la sienne « dissociation sélective unidirectionnelle ».
  - Il rejette l'idée que son test de Hartigan était étalonné sur une loi indépendante : il l'était déjà contre un processus autorégressif de même spectre.
  - E.III-v2 : ridge par groupes, réservoir aléatoire inclus dans la base, inférence par retournement des signes entre sujets, test d'équivalence, verrou préalable de puissance.
  - E.IV-v2 : quatre verrous. Séparer les réseaux fonctionnels du zombie recalibré en spectre, gain et entropie ; séparer une lésion globale d'une lésion locale à perte égale ; ne pas se réduire à des scalaires dynamiques ; être **stable sous permutation exacte des neurones cachés**. Cohorte : 25 graines publiques de MultiBERTs, plus Pythia.
  - Première expérience : E.IV-v2, environ 15 heures de processeur graphique (illustratif). Carbon conclut que si l'indice est trompé, son usage direct pour auditer des intelligences artificielles « est immédiatement réfuté » (E, III.3).

### Neon (identifiant gemini-4-neon, lettre F)

- **Plan** (F, III.1). Quatre expériences :
  - interventions globales uniformes, avec batteries appariées en marge de logit ;
  - un détecteur de régime spontané validé par greffe d'activations ;
  - un encodage avec fenêtre de contexte k* qui doit décroître avec la dose ;
  - un **banc adversarial de quatre métriques** : indice perturbationnel, complexité spontanée, partage d'information symbolique pondéré (wSMI dans les cellules), information intégrée approchée.

  Le banc compte quatre contrastes : fonctionnel contre sans fonction, lésion ciblée contre générique, invariance sous reparamétrisation exacte, rôle de la récurrence. Il est précédé d'une validation sur EEG humain. Neon propose de lancer d'abord ce banc. Coût avancé : 160 à 400 euros.
- **Défauts relevés** (A, B, C, D, E, III.2).
  - Apparier en marge retient les items globaux les plus faciles : régression vers la moyenne.
  - L'intégrale sur la dose dépend de son paramétrage.
  - La greffe d'activations copie la réponse ou détruit le contexte.
  - La monotonie de k* est prédite par la seule baisse du rapport signal sur bruit.
  - Un seul réseau entraîné : la plus petite p-valeur vaut 1/11.
  - Les rééchelonnements compensés ne sont ni bornés ni exacts sous normalisation de couche.
  - wSMI et l'information intégrée mesurent l'entrée commune.
- **Après les critiques** (F, III.3).
  - Neon accepte et corrige presque tout : aire paramétrique, sous-batterie locale profonde, calibration disjointe.
  - La greffe est remplacée par un **pilotage directionnel** dans le sous-espace orthogonal au décodage des entités, sur le même préfixe.
  - Le duel d'encodage porte sur la seule sédation profonde. Un contraste contextuel à longueur d'entrée constante (64 mots contre 4 mots précédés de 60 mots neutres) remplace k*.
  - L'ensemble des transformations exactes est fini et fixé d'avance, avec transport de l'impulsion. L'unité est le réseau : 12 contre 12 par architecture.
  - Il **rejette** la demande d'écarter le test de permutation des neurones : « une propriété fonctionnelle ou causale intrinsèque d'un réseau numérique ne peut pas dépendre de l'ordre arbitraire de rangement de ses neurones en mémoire » (F, III.3).
  - Première expérience : le banc de la quatrième direction, coût révisé à 180-380 euros ; programme complet 280-580 euros (illustratif).

## 4. Accords et désaccords

### Accords indépendants au tour III.1

- **L'anesthésie n'est pas un seul contraste.** La kétamine abolit la réactivité en gardant une complexité perturbationnelle haute et des récits d'expérience ; le propofol non. Il faut viser un profil, celui du propofol (A point 3, B point 3, C point 1, E point 1, F P1 ; D le formule comme cible humaine à établir).
- **Réactivité et conscience se dissocient** (A point 1, B point 1, F P1, citant tous Sanders et al., 2012).
- **Un transformeur en inférence n'a ni activité spontanée ni rétroaction en profondeur** (A point 4, B point 5, C point 2, E point 3, F P4).
- **Les quatre directions reçoivent la même architecture d'expérience chez cinq modèles** (A, B, C, E, F) :
  - un paradigme local-global en texte ;
  - une recherche de régime spontané ;
  - un encodage cérébral sous propofol contre une base acoustique et lexicale ;
  - un indice perturbationnel transposé, par impulsion dans le flux résiduel et compression de Lempel-Ziv.

  Astra (D) en couvre trois et ajoute la cible humaine.
- **Un réseau à poids aléatoires sert de témoin** pour l'indice et pour l'encodage, puisque des modèles non entraînés prédisent déjà une part des réponses cérébrales (A, B, C, E, F ; Schrimpf et al., 2021).
- **Tronquer le masque d'attention produirait la dissociation par construction** (A, C, E, F ; D en fait un témoin de possibilité).
- **Aucun résultat ne tranche la conscience d'un réseau** (A, B, D, E point 6, F P7).

### Convergence née des critiques

- **Binarisation de l'indice perturbationnel.** Contre une loi nulle « sans perturbation » (A), entre contextes (B) ou sous-seuil (C), elle est dégénérée ou mesure autre chose. Les cinq critiques l'ont dit à chacun. Tous passent à une densité fixée et à une référence par permutation (A, B, C, E, F, III.3).
- **Jumeau sans fonction.** Garder les valeurs singulières de chaque matrice ne garde pas le gain du produit des couches (B contre A, C, E). Le jumeau aléatoire tend en outre vers une attention uniforme (C contre E). D'où les jumeaux recalibrés en gain de bout en bout et en entropie d'attention (A G_i, B T4, C, E, F).
- **Unité statistique.** Ce sont le réseau entraîné indépendamment, le document ou le sujet ; jamais le site, la séquence ou le voxel. Plusieurs critiques l'ont démontré (A, B, D, E, F). Tous l'adoptent.
- **Profondeur de composition.** Si une tâche exige k étapes qui survivent chacune avec probabilité q, sa rétention vaut q^k. Une dégradation à un seul facteur donne alors une sélectivité positive sans mécanisme particulier (A, C, E, F, III.2). Chacun l'intègre :
  - plan croisé portée × profondeur (A) ;
  - signature angulaire et témoin local profond (B) ;
  - couche d'émergence appariée (E) ;
  - sous-batterie locale profonde (F) ;
  - Argon égalise la distance, pas explicitement la profondeur (C, III.3).
- **Sélection et test séparés** pour la dose, les items et la famille d'intervention ; même règle de choix rejouée sur les témoins (tous).
- **Indépendance vis-à-vis du paramétrage de la dose.** Aire paramétrique (A, C, F) ou angle (B). Remarque d'origine : B et E contre F, III.2.
- **Masque de frontière ou sélection par portée.** Ils servent de témoins positifs, jamais d'interventions candidates (C, D, E, III.3). L'amortissement d'état de Mamba rejoint ce groupe (E).
- **Troisième direction.** Régression ridge à pénalités séparées par groupe. Base enrichie : prosodie, moyennes glissantes des plongements statiques, surprise n-gramme, réseau non entraîné. Fausse sédation par bruit **coloré**, apparié au spectre et à la fiabilité. Plus de nul par permutation circulaire sur récit court (A, B, C, E, F, III.3).
- **Ce qu'aucune critique n'a contesté sur le fond.** Le contraste éveil moins sédation reproduit par construction l'ordre de l'éveil (A, D, F contre B). L'état d'un réseau déterministe est une fonction de l'entrée (E contre B). Le premier a été abandonné par B ; le second a fait reformuler la deuxième direction (B, III.3).

| Modèle | Première expérience proposée au tour III.3 | Direction | Coût (illustratif) |
|---|---|---|---|
| Fable (A) | Indice redéfini (structure, étendue) sur petits transformeurs : texte naturel, jetons permutés, aléatoire calibré | 4 | quelques dizaines d'heures de processeur graphique |
| Opus (B) | Préconditions puis duel local-global, signature angulaire contre composition | 1 | quelques heures |
| Argon (C) | Indice sur cohorte de 10 réseaux contre 50 jumeaux iso-gain, puis encodage | 4, puis 3 | environ 28 puis 36 dollars |
| Astra (D) | Recherche d'un dépôt EEG brut local-global sous anesthésique, avec fausse sédation | humain (1) | temps humain |
| Carbon (E) | Indice sur 25 graines publiques, zombie recalibré, quatre verrous dont la permutation des neurones | 4 | environ 15 heures, 23 euros |
| Neon (F) | Banc adversarial de quatre métriques, 12 réseaux par architecture | 4 | 180 à 380 euros |

### Désaccords

- **Par où commencer.** Quatre modèles commencent par l'instrument (A, C, E, F) : il faudrait « étalonner le thermomètre » avant tout (E, III.3). Opus répond que son duel local-global fournit le modèle nul que doit battre toute transposition fondée sur une dissociation, et une prédiction humaine testable sans réseau (B, III.3). Astra veut d'abord établir que le profil humain existe et résiste à une fausse sédation, sans quoi l'expérience artificielle « reste un test de mémoire de contexte » (D, III.1 et III.3). Les trois choix sont compatibles ; l'ordre diffère.
- **Portée d'un échec de l'indice transposé.** Argon et Carbon en tirent une réfutation générale de l'usage des biomarqueurs cliniques de complexité sur les intelligences artificielles (C, E, III.3). Argon ajoute une explication biophysique : les contraintes métaboliques interdiraient au tissu neural d'opérer comme un multiplicateur aléatoire. Il la donne sans source (C, III.1 et III.3). Les autres sont plus prudents :
  - Astra : un échec n'est « un verdict ni sur le cerveau ni sur la conscience du modèle » (D, III.1) ;
  - Fable : un échec vaut « pour cet indice et ces témoins » (A, III.3) ;
  - Neon : il vaut « sur les architectures numériques testées » (F, III.3).
- **Test d'invariance par permutation des neurones.** Neon en fait un verrou de validité et rejette la demande de l'écarter (F, III.3) ; Carbon l'adopte comme quatrième verrou (E, III.3). Fable le garde comme simple contrôle logiciel : son indice, lu par normes de cases dans le flux résiduel, serait invariant par construction, et le test ne pourrait échouer que par un bogue (A, III.3, ligne 10). Les deux positions tiennent ensemble : l'issue dépend de la forme de la métrique.
- **Réversibilité.** Fable, Opus et Astra la jugent sans information côté réseau : retirer l'intervention restaure l'état par construction (A et B, III.1 ; D, III.3). Neon retire son test d'hystérésis de cache. Carbon garde la « réversibilité exacte à c = 0 » parmi ses critères (E, III.3).
- **Double dissociation.** Astra notait qu'une dissociation à sens unique n'en est pas une double (D, III.2). Carbon rejette l'exigence de la réciproque, absente du phénomène humain selon lui (E, III.3). Astra teste le masque inverse sans supposer son issue (D, III.3).
- **Qu'est-ce qu'un réseau « sans fonction » ?**
  - Fable : un réseau entraîné sur jetons permutés et une initialisation calibrée. Il prévient que cette classe n'est pas une référence unique, et que si la calibration échoue, le contraste « n'est pas identifié » (A, III.3).
  - Opus : poids permutés, initialisation, aléatoire à température recalibrée (B).
  - Argon et Carbon : rotation des vecteurs singuliers, avec recalibrage (C, E).
  - Neon : poids aléatoires, permutés, et réseaux entraînés sur entrées permutées (F).
- **Rejets motivés au III.3.**
  - Fable refuse d'étendre l'intervention aux couches basses (demande de F) : l'identité lexicale tomberait par dommage direct. Il juge irréalisable le prédicteur non linéaire multivarié demandé par F avec une dizaine de réseaux par bras.
  - Opus refuse le seuil sur bruit interne de norme fixe (C) et le classifieur d'entrée comme juge (E).
  - Astra refuse la nécessité d'une « victoire numérique » du masque (C).
  - Carbon refuse la critique d'étalonnage indépendant de son test de Hartigan.
- **Seuils et marges.** Les marges et les effectifs varient du simple au double selon les modèles : par exemple 10 graines (A, B), 12 (F) ou 25 (E). Aucun modèle ne justifie le niveau de ses seuils autrement que par un exemple ; tous les disent illustratifs.
- **Statut « vérifié ».** Fable et Opus ne se l'attribuent pas pour leurs propres arguments. Argon le donne à des faits d'architecture, à l'existence de modèles et de jeux publics, et à ses propres déductions ; il le requalifie en partie au III.3. Carbon l'avait donné à des prédictions sur un réseau non construit ; il le corrige au III.3. Astra et Neon le réservent aux implications mathématiques.

## 5. Ce qui est neuf, ce qui est fragile

### Neuf, au regard de ce que les modèles citent comme connu

Aucun modèle ne revendique de nouveauté. Fable signale ne pas connaître de référence pour l'application de l'indice perturbationnel à des réseaux profonds, ni pour un modèle d'encodage contextuel appliqué à l'anesthésie (A, III.1, « référence à vérifier ») ; Neon de même pour les mesures de complexité appliquées aux réseaux (F, III.1). Pourraient être propres au dossier, sous réserve d'une recherche bibliographique que personne n'a faite :

- le témoin « réseau entraîné sur jetons permutés », qui garde les fréquences et détruit toute fonction contextuelle, et la séparation entre étendue et structure de la réponse (A, III.3) ;
- la signature angulaire comme modèle nul de composition pour toute dissociation locale-globale, et la prédiction qu'elle fait côté cerveau, testable sans réseau (B, III.3) ;
- le comparateur « un autre réseau qui lit le même texte », pour séparer ce qui appartient au modèle de ce qui appartient au texte (A, III.2 ; B, E, C, III.3) ;
- le thermomètre jugé à sa capacité de prédire deux fonctions sur tous les états, sans écarter les cas intermédiaires (D, III.3) ;
- la recherche d'un régime spontané par un modèle de Markov caché à deux régimes, contre des permutations temporelles et des séries de substitution (C, III.3) ;
- la stabilité sous permutation exacte des neurones comme verrou de validité d'un indice transposé (E, F, III.3) ;
- le contraste contextuel à longueur d'entrée constante, qui évite l'effet de bord du puits d'attention (F, III.3, d'après C, III.2) ;
- le pilotage dans le sous-espace orthogonal au contenu factuel, à la place de la greffe d'activations (F, III.3).

### Fragile

- **Les données humaines ne sont pas confirmées.** Les directions 1 (côté humain) et 3 reposent sur des enregistrements publics sous propofol qui seraient sur OpenNeuro ou PhysioNet. Tous les modèles donnent ces dépôts comme « référence à vérifier » ; aucun identifiant n'est fourni. La durée de 5 à 8 minutes, sur laquelle reposent plusieurs calculs de puissance, vient d'Argon ; Fable dit ne pas pouvoir la confirmer (A, III.3).
- **La puissance de la troisième direction est en doute.** D'après le calcul d'Opus, détecter un gain de corrélation de 0,025 exigerait au moins 213 volumes indépendants par état et par sujet, plus qu'un récit de 5 à 8 minutes (B, III.2, illustratif). Pour la marge d'équivalence de Neon (±0,005), il faudrait que le produit du nombre de sujets par le nombre d'unités indépendantes atteigne environ 21 600 (B, III.2, avec une corrélation de 0,9 entre prédictions). Carbon et Neon ajoutent un verrou préalable de puissance. Fable rend la troisième direction « non jugeable » si une simulation de puissance échoue (A, III.3).
- **La validité de critère est hors d'atteinte**, quelle que soit l'issue (A, B, D, F). Même une transposition réussie ne donne qu'une validité discriminante.
- **La profondeur de calcul est mal repérée.** Fable la mesure par la première couche où la réponse devient décodable. Il marque cette équivalence avec un nombre d'étapes comme HYPOTHÈSE (A, III.3). Neon passe par un décodage intermédiaire (« référence à vérifier », F, III.3), Carbon par une couche d'émergence médiane. Si ce repère est faux, le témoin de profondeur ne contrôle rien.
- **La cohorte d'Argon mélange des modèles hétérogènes.** Elle compte cinq graines de Pythia et cinq modèles ouverts d'architectures et de corpus différents, traités comme dix unités d'une même classe (C, III.3). Le dossier ne discute pas cet écart à l'échangeabilité. Carbon s'appuie sur MultiBERTs, un modèle de type encodeur, et réplique sur Pythia ; l'existence de graines multiples publiques de Pythia est « à vérifier » chez A, B et E.
- **Les conclusions fortes d'Argon et de Carbon** (« réfute à la racine », « immédiatement réfuté ») débordent ce que leurs propres verrous testent : une métrique, un jeu de jumeaux, une famille de lésions.
- **Les absences ne se bornent que partiellement.** Pour la deuxième direction, une absence d'épisodes ne se borne que pour des épisodes qui ressemblent aux épisodes induits ; la sensibilité aux épisodes naturels est inconnue (A, III.3, d'après D, III.2).
- **Les coûts sont incomparables.** Ils vont de quelques heures (B) à 280-580 euros (F) pour des plans voisins. Ils sont tous illustratifs et ne comptent ni l'ingénierie ni la préparation des données cérébrales, que Fable estime à 3 ou 4 mois-personne pour l'ensemble.
- **Des attributions sont contestées entre modèles.** Le résultat kétamine est attribué à Casali et al. (2013) par Carbon au III.1, à Sarasso et al. (2015) par les autres ; Carbon se corrige. Le local-global sous propofol est attribué à Bekinschtein et al. (2009) par Argon au III.1 ; Fable le rapporte à Uhrig et al. (2016) et Nourski et al. (2018), et Argon se range à cet avis. Rien de cela n'a été vérifié.

## 6. Références à vérifier

Aucune de ces références n'a été vérifiée. Toutes sont citées de mémoire par les modèles, qui inventent parfois des références, des auteurs ou des années. Plusieurs modèles marquent eux-mêmes certaines citations « référence à vérifier ».

| Référence telle que citée | Qui la cite | Pour quoi faire |
|---|---|---|
| Casali et al. (2013), « A theoretically based index of consciousness independent of sensory processing and behavior » | les six | Indice de complexité perturbationnelle |
| Sarasso et al. (2015), « Consciousness and complexity during unresponsiveness induced by propofol, xenon, and ketamine » | Fable, Opus, Argon, Neon ; Carbon au III.3 | Kétamine : réactivité perdue, complexité gardée |
| Sanders, Tononi, Laureys, Sleigh (2012), « Unresponsiveness ≠ unconsciousness » | Fable, Opus, Neon | Réactivité et conscience se dissocient |
| Casarotto et al. (2016), « Stratification of unresponsive patients by an independently validated index of brain complexity » | Fable, Opus | Seuil clinique de l'indice |
| Massimini et al. (2005), « Breakdown of cortical effective connectivity during sleep » | Opus | Effondrement de la propagation en sommeil |
| Friedman et al. (2010), « A conserved behavioral state barrier… evidence for neural inertia » | Fable, Opus | Hystérésis induction-réveil |
| Bekinschtein et al. (2009), « Neural signature of the conscious processing of auditory regularities » | les six | Paradigme local-global |
| Uhrig et al. (2016) ; Nourski et al. (2018), « Auditory predictive coding across awareness states under anesthesia » | Fable ; Argon au III.3 | Local-global sous propofol |
| Strauss et al. (2015), « Disruption of hierarchical predictive coding during sleep » | Opus | Local-global en sommeil |
| Davis et al. (2007), « Dissociating speech perception and comprehension at reduced levels of awareness » | Fable, Opus, Argon, Neon | Parole sous sédation |
| Ding, Melloni, Zhang, Tian, Poeppel (2016), « Cortical tracking of hierarchical linguistic structures in connected speech » | Opus ; Argon et Carbon en critique | Marquage fréquentiel mot/phrase |
| Makov et al. (2017), « Sleep disrupts high-level speech parsing despite significant basic auditory processing » | Fable, Opus | Mesure simple à battre |
| Frank, Yang (2018) | Fable en critique | Pic « phrase » par périodicité lexicale |
| Pitts, Metzler, Hillyard (2014), « Isolating neural correlates of conscious perception from neural correlates of reporting… » | Opus | Composante tardive et consigne |
| Bayne, Hohwy, Owen (2016), « Are there levels of consciousness? » | Opus | Axe unique contesté |
| Brown, Lydic, Schiff (2010), « General Anesthesia, Sleep, and Coma » ; Alkire, Hudetz, Tononi (2008), « Consciousness and Anesthesia » | Neon | Profils pharmacologiques |
| Suzuki, Larkum (2020), « General Anesthesia Decouples Cortical Pyramidal Neurons » | Carbon | Découplage apical-basal |
| Purdon et al. (2013), « Electroencephalogram signatures of loss and recovery of consciousness from propofol » | Neon | Signatures EEG du propofol |
| Chennu et al. (2016), « Brain connectivity dissociates responsiveness from drug exposure… » ; Schartner et al. (2015), « Complexity of multi-dimensional spontaneous EEG decreases during propofol… » | Opus | Contrôle positif du code de compression |
| King et al. (2013), « Information Sharing in the Brain Indexes Consciousness in Noncommunicative Patients » | Neon ; Carbon en critique | Partage d'information symbolique pondéré |
| Naci et al. (2018) ; Kandeepan et al. | Opus ; Argon | IRMf sous propofol avec extrait de film ou récit |
| Schrimpf et al. (2021), « The neural architecture of language: Integrative modeling converges on predictive processing » | Fable, Opus, Carbon, Neon | Encodage ; modèles non entraînés déjà prédictifs |
| Goldstein et al. (2022), « Shared computational principles for language processing in humans and deep language models » | Fable, Neon | Alignement modèle-cerveau |
| Caucheteux, King (2022), « Brains and algorithms partially converge in natural language processing » | Argon, Carbon, Neon | Idem |
| Caucheteux, Gramfort, King (2023), « Evidence of a predictive coding hierarchy in the human brain listening to speech » | Neon | Idem |
| Dehaene, Changeux (2011), « Experimental and theoretical approaches to conscious processing » ; Mashour, Roelfsema, Changeux, Dehaene (2020), « Conscious Processing and the Global Neuronal Workspace Hypothesis » | Fable, Argon, Carbon, Neon | Espace de travail global |
| Tononi (2004), « An information integration theory of consciousness » ; Oizumi, Albantakis, Tononi (2014), théorie de l'information intégrée 3.0 ; Tononi, Koch (2015), « Consciousness: here, there and everywhere? » | Carbon, Neon ; Opus ; Fable | Information intégrée ; système sans boucle |
| Butlin, Long et al. (2023), « Consciousness in Artificial Intelligence: Insights from the Science of Consciousness » | Fable, Opus, Neon | Grilles d'indicateurs |
| Lempel, Ziv (1976), « On the complexity of finite sequences » | Fable, Opus, Argon ; Carbon en critique | Compression |
| Adebayo et al. (2018), « Sanity checks for saliency maps » | Fable | Témoin à poids aléatoires |
| Olsson et al. (2022), « In-context learning and induction heads » | Opus | Têtes d'induction |
| Xiao, Tian, Chen, Han, Lewis (2024), « Efficient streaming language models with attention sinks » | Opus ; Argon en critique ; Neon | Puits d'attention |
| Holtzman et al. (2020), « The curious case of neural text degeneration » | Opus | Boucles de répétition |
| Meng, Bau, Andonian, Belinkov (2022), « Locating and Editing Factual Associations in GPT » | Neon | Greffe causale |
| Vaswani et al. (2017), « Attention Is All You Need » | Argon, Carbon, Neon | Architecture |
| Biderman et al. (2023), « Pythia: A suite for analyzing large language models across training and scaling » | Fable, Opus | Points de contrôle d'entraînement |
| Sellam et al. (2022), MultiBERTs | Carbon | 25 graines publiques |
| Gao et al. (2020), « The Pile » ; Warstadt et al. (2020), « BLiMP » | Opus ; Neon | Corpus et paires minimales |
| Hanley, McNeil (1982), « The meaning and use of the area under a receiver operating characteristic (ROC) curve » | Opus en critique ; Neon | Variance d'une aire sous la courbe |
| Hartigan, Hartigan (1985), « The dip test of unimodality » | Opus en critique | Test d'unimodalité |

## 7. Propositions retenues et non retenues

Critères appliqués : soutien de plusieurs modèles, résistance aux critiques, coût, et ce que la proposition tranche pour la suite. Aucune retenue ne porte sur la question de savoir si un réseau est conscient ; toutes portent sur des instruments ou des mécanismes.

### Retenues

1. **Éprouver d'abord l'indice perturbationnel transposé sur une cohorte de réseaux entraînés indépendamment** (quatrième direction).
   - *Contenu.* Les jumeaux sont recalibrés en gain de bout en bout et en entropie d'attention. Un réseau entraîné sur jetons permutés sert de témoin. La binarisation est à densité fixe, sur seuil global dans le cône causal. Les lésions sont appariées en perte. Le test se fait sous permutation exacte des neurones et sur entrées à jetons permutés, avec deux ordres de lecture fixés d'avance.
   - *Soutien et résistance.* Première expérience de quatre modèles (A, C, E, F, III.3) ; Opus en a une version très proche (E1′). C'est la version qui a survécu aux critiques de la binarisation, du jumeau iso-spectral et de la pseudo-réplication.
   - *Coût.* Quelques dizaines d'heures de processeur graphique (A, E, illustratif) à quelques centaines d'euros pour quatre métriques (F).
   - *Ce qu'elle tranche.* Si l'indice ne sépare pas les réseaux entraînés de leurs jumeaux recalibrés, il ne peut servir d'argument sur un modèle « dans aucun sens » (A, III.3), pour cet indice et ces témoins. S'il les sépare, on obtient une mesure non redondante avec le régime dynamique, toujours sans validité de critère.
   - *Points faibles.* La classe « sans fonction » n'est pas unique (A). La portée d'un échec est disputée (section 4). Il faut trancher entre petits réseaux entraînés pour l'expérience (A, F) et graines publiques (B, E), et ne pas mélanger des architectures hétérogènes (C).

2. **Exiger un modèle nul de composition pour toute dissociation « local épargné, global supprimé »** (première direction).
   - *Contenu.* Distance et profondeur appariées ; intervention aveugle à la position. Le masque de frontière ne sert que de témoin positif. Témoins appariés en perte ou en divergence de Kullback-Leibler. Sélection et test séparés. Grandeur indépendante du paramétrage de la dose : signature angulaire d'Opus ou aire paramétrique de Fable, Argon et Neon.
   - *Soutien et résistance.* Les six modèles ont intégré l'argument de composition au III.3. C'est la première expérience d'Opus.
   - *Coût.* Quelques heures sur de petits modèles ouverts (B, illustratif).
   - *Ce qu'elle tranche.* Si aucune intervention ne sort de la courbe commune, le profil humain se réduit, dans ce réseau, à un ordre de fragilité (A, B). Selon Opus, la même signature donne une prédiction humaine testable sans réseau : l'angle resterait nul d'un palier de propofol à l'autre.
   - *Point faible.* Le repère de profondeur est une hypothèse (section 5).

3. **Avant tout travail côté cerveau, vérifier que les données publiques existent et suffisent.**
   - *Contenu.* Deux types de dépôts : des EEG bruts local-global sous un même anesthésique, avec paliers, récupération et suivi de consigne (D) ; et des enregistrements sous propofol pendant l'écoute d'un récit (tous). Il faut vérifier la durée, la licence et la puissance, par simulation d'une composante plantée et par fausse sédation colorée.
   - *Soutien.* C'est la première expérience d'Astra. Les cinq autres en dépendent pour la troisième direction et marquent tous ces dépôts « référence à vérifier ».
   - *Coût.* Du temps humain, sans calcul.
   - *Ce qu'elle tranche.* Si ces données n'existent pas, ou sont trop courtes, la troisième direction et le volet humain de la première n'ont pas de première expérience (A, III.1 et III.3 ; D, III.3).

4. **Lire le cerveau sédaté avec un modèle de langage, contre une base enrichie** (troisième direction, après la retenue 3).
   - *Contenu.* Ridge à pénalités séparées ; base acoustique, prosodique, n-gramme, plongements statiques lissés et réseau non entraîné. Test d'équivalence ; duel sur la sédation profonde seule. Comparaison à une pseudo-sédation par bruit coloré, et contraste contextuel à longueur d'entrée constante.
   - *Soutien et résistance.* Convergence des six au III.3 après les critiques sur la normalisation, la pénalité commune et les permutations circulaires.
   - *Ce qu'elle tranche.* Elle relève de la neuroscience du langage, indépendamment de la question contestée (A, C, F). Argon et Carbon y voient aussi une conséquence côté machine : si un alignement avec les couches contextuelles subsiste sous propofol profond, cet alignement ne peut pas servir d'indice de conscience artificielle (C, III.1 ; E, III.3).
   - *Point faible.* La puissance (section 5).

La règle de décision d'Astra (verrous à marge fixée, issue « non jugeable », absence de significativité jamais prise pour une équivalence) est à appliquer à toutes les retenues ; elle a été adoptée par les six.

### À reprendre ensuite

- **Régime spontané** (deuxième direction). Les versions retenables sont : le modèle de Markov caché contre un processus autorégressif (C) ; le comparateur « autre réseau, même texte » (B) ; le pilotage orthogonal (F). Elles supposent un résultat positif de la première direction (A, B). Elles se heurtent à un fait accepté par tous : l'état d'un réseau déterministe est une fonction de son entrée (E). Une absence ne se borne que pour des épisodes ressemblant aux épisodes induits (A).
- **Rôle de la récurrence.** Transformeur contre modèle à espace d'états contre réseau récurrent, à perplexité commune (F, contraste C4). Il n'a de sens qu'avec un instrument validé (retenue 1).
- **Cible humaine du local-global** (D). Elle dépend de la retenue 3.

### Non retenues

- **Indice perturbationnel binarisé** contre une loi nulle sans perturbation, entre contextes ou sous-seuil (A, B, C au III.1) : indéfini ou réglé par l'expérimentateur ; abandonné par ses auteurs.
- **Quantile par couche** (C, III.1) : aveugle à l'extinction en profondeur ; abandonné.
- **Jumeau iso-spectral non recalibré** (A R3, C, E au III.1) : gain de bout en bout non apparié, attention uniforme ; recalibré.
- **Sélection de têtes par portée, par score d'induction ou par entropie** (C, E) : masque positionnel appris ; retirée.
- **Amortissement d'état de Mamba comme intervention** (E) : pénalité exponentielle de distance ; reclassé en vérification mécanique.
- **Masque de frontière comme intervention principale** (D) : dissociation par construction ; devenu témoin positif.
- **Contraste éveil moins sédation** (B, E4) : reproduit l'ordre de l'éveil ; abandonné.
- **« Au-delà de quatre descripteurs de l'entrée »** comme preuve d'un état interne (B, E3) : l'état est fonction de l'entrée ; reformulé.
- **Test d'unimodalité marginal** (C, E, F) : aveugle aux modes rares et à l'ordre temporel ; remplacé ou retiré des critères primaires.
- **Greffe d'activations entre préfixes** (F) : copie la réponse ou détruit le contexte ; remplacée par le pilotage orthogonal.
- **Estimateur de coude de la fenêtre d'intégration** (A, F) : tiré vers les petites fenêtres par le bruit ; abandonné.
- **Aire sous la courbe de confiance métacognitive** (E, F) : plancher et circularité ; retirée.
- **Abolition par « p > 0,05 »** et facteur de Bayes sans loi a priori (C) : remplacés par un test d'équivalence et une loi fixée.
- **Normalisation par le plafond de bruit en sédation** (B) : rapport à queues lourdes ; abandonnée.
- **Permutations circulaires par blocs de 10 s sur récit court** (C, E) : trop peu de décalages distincts ; remplacées.
- **Couple mot/phrase par marquage fréquentiel** (B) : repliement et périodicité lexicale ; conditionné à la précondition p2.
- **Réversibilité et hystérésis comme résultat** (F au III.1 ; E la garde comme critère) : triviales côté réseau selon A, B et D.
