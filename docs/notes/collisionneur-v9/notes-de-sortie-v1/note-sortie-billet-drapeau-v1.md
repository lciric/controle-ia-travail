# Rendre public un texte court avant les résultats : note de sortie du collisionneur

- **Date** : 2026-11-22, 19:43 UTC.
- **Dossier** : `runs/collisionneur-protocole-x-billet-drapeau-v1-20261122-110018`.
- **Accord** : GO-2026-11-22-33, plafond de 50 dollars (`registres/essaim/vers-mere/collisionneurs-v8d-2026-11-22-1233-v1.md`).
- **Dépense** : 16,96 dollars sur une ligne de 50 (`etat.md` du dossier). Par clé, selon le même compte rendu : Anthropic 6,86 ; Google 8,53, dont Neon 3,67 ; OpenAI 1,57. La part d'Astra est surestimée d'environ 20 % : le dossier l'a comptée au prix d'un modèle plus ancien (`declaration-prix-astra-v1.md` du dossier).
- **Tours** : dix-huit cellules sur dix-huit, toutes complètes : six conceptions (tour III.1), six critiques croisées (III.2), six réponses (III.3). La réponse de Neon (F, III.3) a demandé un second essai après une coupure de flux. Le premier essai est compté au pire, 1,65 dollar.
- **Note écrite après coup** (dossier fini le 22 novembre à 12:33 UTC, avant la règle des notes de sortie).

Rédigé par un lecteur Opus 5.5, classe C, à partir des seules cellules du dossier, lues en entier. Le lecteur est du même modèle qu'une des cellules (lettre B) ; elle est traitée comme les autres.

**Ce que la note n'est pas.** Aucune cellule ne rapporte de mesure. Tout ce qui suit est argument, calcul sous hypothèses ou protocole proposé. Les seuils, effectifs et coûts sont qualifiés d'illustratifs par leurs auteurs. Plusieurs modèles marquent « vérifié » leurs propres calculs ou des références ; aucun de ces calculs n'a été refait par un lecteur extérieur au collisionneur, et aucune référence n'a été contrôlée.

**Attention aux étiquettes.** Chaque modèle numérote à sa façon les contenus possibles du texte (C0 à C5). Le même sigle désigne des choses différentes d'une cellule à l'autre. La note nomme donc chaque contenu par ce qu'il est.

## 1. La question

Une équipe prépare une étude empirique ; aucune mesure n'est faite. Des travaux voisins paraissent. L'étude éprouve un dispositif de détection contre un adversaire, et certaines mesures ne valent que si des éléments restent inconnus de certaines personnes ou de certains systèmes. Faut-il rendre public un texte court avant les résultats ? La question demande :

1. quels contenus un tel texte peut porter ;
2. pour chacun, son effet sur la reconnaissance ultérieure, sur la probabilité qu'un autre groupe publie d'abord, sur la validité des mesures, sur ce qu'apprendrait un adversaire, sur la qualité et le coût de l'étude ;
3. à quelles conditions publier avant, publier après ou ne rien publier ;
4. quelles vérifications, indépendantes de l'équipe, diraient que le choix était le bon ;
5. l'argument le plus fort pour chaque option, puis un choix et ce qui le ferait changer.

L'en-tête de la question signale une version 2, corrigée après un « test de devinette ». Le protocole et les résultats de ce test ne sont pas transmis aux modèles ; Fable, Opus, Astra et Neon le relèvent (A, B, D, F, III.1 ou III.3).

## 2. En bref

- **Personne ne veut publier les éléments secrets avant la fin.** Les six modèles l'écrivent au tour III.1 : c'est détruire les mesures qui en dépendent.
- **La date peut se prouver sans rien montrer.** Les six proposent, chacun de son côté, de sceller maintenant le protocole complet : empreinte cryptographique horodatée, ou dépôt sous embargo chez un tiers. Tous jugent donc incomplète l'alternative « avant, après, rien ».
- **Quatre modèles ne publieraient aucun texte lisible avant les mesures** : Argon, Astra, Carbon et Neon (C, D, E, F). Opus publierait la question, les hypothèses et les métriques avec l'empreinte (B). Fable ne le ferait que si un test préalable montre que ce texte ne laisse pas deviner les éléments secrets (A). Ces positions n'ont pas bougé au tour III.3.
- **Les critiques ont surtout démoli les plans de mesure.** Aux effectifs écrits au III.1, presque aucune issue « sans danger » n'était atteignable. Exemple : avec 20 canaris, aucune borne ne passe sous 5 % ; il en faut environ 72 (A, B, C, III.2). Tous ont relevé leurs effectifs et adopté une même règle de lecture, avec une issue « non concluant ».
- **Ce qui reste hors de portée d'une seule équipe** : l'effet du texte sur le devancement (non identifiable sur un cas) et sur la reconnaissance (des centaines de juges par bras). « Le choix était le bon » n'est pas vérifiable ; seules le sont des prédictions écrites d'avance et des traces de processus (A, B, D, F).
- **Premières expériences proposées** : aucune ne publie le texte. Quatre se font hors ligne, sur des modèles ouverts (A, B, C, E). Astra montre le texte exact à des lecteurs autorisés, ensuite exclus de l'étude. Neon interroge les vrais systèmes cibles sur des prépublications d'autres équipes.

## 3. Ce que chaque modèle a proposé

### Claude Fable 5.2 (lettre A)

- **Proposition centrale** (A, III.1). Onze présupposés de la question, dont :
  - le régime pertinent est peut-être l'adversaire informé, pour un dispositif destiné à servir (principe de Kerckhoffs) ;
  - « le choix était le bon » n'est pas observable, seules des prédictions écrites d'avance le sont ;
  - deux options manquent : l'engagement scellé daté et le texte scindé (partie publique, partie scellée).

  Cinq contenus, du plus neutre au plus destructeur : empreinte salée du protocole ; question et périmètre ; hypothèses, métriques et seuils ; mécanisme du dispositif ; éléments scellés.
- **Plan** (A, III.1). Cinq duels :
  - D1, le texte laisse-t-il deviner les éléments secrets, mieux qu'un placebo ?
  - D2, adversaire informé contre adversaire naïf, à fausses alertes fixées ;
  - D3, reconnaissance par vignettes (rien, empreinte ouverte après coup, note publique) ;
  - D4, taux de base du devancement sur les parutions des douze derniers mois ;
  - D5, une relecture scellée trouve-t-elle des défauts plantés ?

  Coût avancé : moins de 100 euros pour D1, 50 à 400 pour D2, 700 à 2 000 pour D3 (illustratif).
- **Choix** (A, III.1). Une « quatrième voie, séquencée » : engagement scellé maintenant ; tests sans rien publier ; texte public limité à la question et aux hypothèses seulement si D1 conclut à l'absence de fuite ; mécanisme après le bras naïf ; éléments secrets jamais avant la fin.
- **Défauts relevés** (III.2).
  - La règle de D1 permet deux verdicts à la fois : un intervalle entre 0 et 5 points valide les deux hypothèses (D, E, F).
  - Le seuil de détection est fixé et évalué sur les mêmes cas honnêtes (C, D, F).
  - D4 est presque toujours non concluant : à 20 %, une ou zéro parution laisse l'intervalle de part et d'autre du seuil (B, C).
  - D5 n'a pas de bras public : il ne peut pas dire ce qu'une exposition publique trouverait (B, D, E).
  - L'empreinte ne cache ni la date ni, selon le registre, l'identité (E, F).
- **Après les critiques** (A, III.3). Fable accepte presque tout.
  - D1′ : questionnaire rédigé par un tiers qui connaît les secrets mais pas le texte ; trois placebos de rédacteurs distincts plus un placebo tiré des articles antérieurs de l'équipe ; bras sans texte ; clé leurre ; fuites plantées à trois niveaux (littérale, paraphrasée, déductible seulement avec les travaux voisins) ; devineurs neufs pour la confirmation.
  - D2′ : lots honnêtes disjoints, empreinte du détecteur avant et après, contrôle positif sur un détecteur de référence faible.
  - D4 est retiré comme duel ; D5′ ne mesure plus qu'une sensibilité absolue.
  - Il rejette deux points. Le questionnaire fermé ne biaise pas l'écart, puisque les deux bras reçoivent les mêmes options. La valeur de non-jugeabilité « 0,0015 » d'Argon n'est pas reproduite.
  - Il juge le duel « note contre empreinte » probablement non jugeable : environ 430 évaluateurs par bras pour une marge de 10 points (illustratif).
  - Compte révisé : huit issues réfutantes au lieu de douze annoncées.

### Claude Opus 5.5 (lettre B)

- **Proposition centrale** (B, III.1). Dix présupposés. Deux se distinguent :
  - les travaux voisins peuvent, sans rien devoir à l'équipe, rendre publics des éléments proches des éléments secrets ;
  - le bénéfice de qualité peut venir de l'engagement (fixer hypothèses et seuils) et non de la publicité.
- **Plan** (B, III.1). Six duels :
  - E1, information apportée à l'adversaire (rien, texte réel, placebo, méthode complète) ;
  - E2, ingestion d'un texte en ligne par des systèmes à recherche web, mesurée par des chaînes-canaris ;
  - E3, effet d'un drapeau sur le devancement, sur un corpus observationnel apparié ;
  - E4, reconnaissance par vignettes ;
  - E5, défauts trouvés par un protocole public ou par un audit interne ;
  - E6, éléments secrets créés avant ou après la publication.

  Coût avancé : 0,5 à 1,5 millier d'euros de calcul, 2 à 5 milliers pour les relecteurs (illustratif).
- **Choix** (B, III.1). Hybride : publier la question, les hypothèses et les métriques, sans méthode ni éléments secrets ; y joindre l'empreinte du protocole complet, déposé sous embargo ; générer au moins la moitié des éléments secrets après la publication.
- **Défauts relevés** (III.2).
  - E6 est aveugle à une fuite du procédé : les deux moitiés sortent du même procédé et sont touchées également (A, C, D, E, F).
  - E3 souffre d'un biais de temps immortel : une question sans drapeau n'entre au corpus qu'une fois publiée (A, C, D, E, F).
  - Le bras « absence de pièce » de E4 sert au seuil mais manque à la liste (D, E, F).
  - Les requêtes hebdomadaires de E2 peuvent provoquer elles-mêmes l'indexation (C).
  - Le placebo qui décrit un faux détecteur détourne l'adversaire au lieu d'être neutre (E, F).
  - Le banc de décisions simulées mesure l'accord avec un modèle publié, pas la justesse (A, C, D, E, F).
- **Après les critiques** (B, III.3).
  - Opus reconnaît que E6 était « le défaut le plus grave » de sa conception. Il le remplace par E6b : une famille d'éléments secrets touchée par le texte, une famille orthogonale, et un contrôle positif où un indice de classe est divulgué exprès.
  - E2′ ajoute deux cohortes, interrogée chaque semaine ou seulement à la fin, pour tester l'auto-contamination. Le nombre de canaris est fixé après mesure des fausses alertes : environ 72, jusqu'à 290.
  - E3′ devient la plus faible des expériences et n'a plus le pouvoir de faire basculer le choix.
  - Le banc de décisions est rétrogradé : il mesure une conformité à des standards déclarés.
  - Il rejette en partie deux critiques : le rappel littéral est la bonne mesure pour une fuite d'instances ; et il refuse de déposer des prépublications fictives sur un serveur scientifique, ce qui en polluerait le registre.
  - Choix maintenu, avec deux changements : tous les éléments secrets générés après la publication, et un canari propre à l'exemplaire déposé chez le tiers, idée tirée de la critique de Fable contre Astra.

### Argon (identifiant gemini-4-argon, lettre C)

- **Proposition centrale** (C, III.1). Cinq présupposés, dont l'existence non établie d'une rédaction à la fois assez précise pour être reconnue et assez vague pour ne rien révéler. Cinq contenus, dont un « jalon avec cas-canaris » (dix à cinquante exemples publiés). Pour chaque option, des conditions précises ; publier avant exige quatre conditions conjointes, dont une cible coupée d'Internet.
- **Plan** (C, III.1). Quatre expériences :
  - Exp. 1, publier réellement un billet sur un lot de cas et comparer avec un lot secret, sur la cible réelle ;
  - Exp. 2, test de devinette par une équipe rouge, parmi dix cibles candidates ;
  - Exp. 3, dérive de réplication entre protocole libre et protocole figé ;
  - Exp. 4, une équipe concurrente avec billet, une sans, puis un jury.

  Coût avancé : 725 dollars en 48 heures (illustratif).
- **Choix** (C, III.1). Aucun texte lisible avant ; empreinte horodatée du protocole, du code et des seuils.
- **Défauts relevés** (III.2).
  - L'Exp. 1 exécute la décision qu'elle prétend éclairer : publier contre la cible détruit l'aveugle (A, B, E, F).
  - Une équipe par bras dans l'Exp. 4 : aucune variance estimable (A, B, C, D, E, F).
  - L'empreinte annoncée à 100 % de détection et 0 % de fausses alertes signale toutes les reformulations de prose, qui sont ses propres cas honnêtes (A, B, E, F).
  - « Toujours préférable » pour l'empreinte contredit son propre constat que les noms d'auteurs fuient (A, B, F).
  - Des références sont marquées « vérifié » sans appui ; Shannon (1949) est cité pour l'horodatage par hachage, ce que son texte ne traite pas selon A et B.
  - « Ne rien publier » si un échec est jugé « défaut local » est un degré de liberté après coup (A).
- **Après les critiques** (C, III.3).
  - Argon accepte presque tout. Il réattribue l'horodatage à Haber et Stornetta (1991, à vérifier) sans changer ses statuts.
  - L'Exp. 1 passe sur un jumeau hors ligne, avec trois familles de cas : visée, secrète, orthogonale.
  - L'Exp. 3 devient un plan 2 × 2 : protocole figé ou libre, sur le jeu de l'équipe et sur un jeu frais d'auditeur.
  - L'Exp. 4 passe à seize unités par bras, avec mesure de la vitesse de base.
  - L'empreinte devient un arbre de quatre feuilles : prose, spécification statistique, code, et vecteur de scores sur un jeu étalon. Il annonce de nouveau 0 % de fausses alertes et 100 % de détection.
  - Il scinde l'empreinte en dépôt nominatif et dépôt anonyme ; seul le second éviterait la fuite d'identité.
  - Un résultat négatif est désormais publié, sauf si les contrôles d'étalonnage du banc échouent.
  - Rejet partiel : un test hors ligne sans retour du détecteur n'est pas une « mesure » au sens de l'énoncé.

### Astra (identifiant gpt-6.2-astra, lettre D)

- **Proposition centrale** (D, III.1). La plus courte. Deux distinctions reprises par d'autres :
  - un dépôt privé répond à « qu'aviez-vous prévu et quand ? », pas à « qui a rendu le travail public en premier ? » ;
  - apprendre quelque chose, modifier son comportement et invalider une mesure sont trois critères distincts.

  « Publier d'abord » y désigne la première publication d'un résultat comparable, pas d'une intention. Astra dit enfin que ne pas publier de billet ne veut pas dire taire les résultats défavorables.
- **Plan** (D, III.1). Quatre duels (crédit, concurrence par tournoi rémunéré, fuite sur une réplique à catégories fictives avec un modèle Pythia, qualité nette en heures). Règle de lecture : hypothèses complémentaires, intervalle, aucune réfutation si l'intervalle traverse la frontière. Pilote à environ 12 euros de calcul et 2 000 euros de juges (illustratif).
- **Choix** (D, III.1). Différer le texte public jusqu'au gel des mesures qui exigent l'ignorance ; confier dès maintenant à un tiers, sous accès restreint, la question, les critères et la liste des éléments à cacher.
- **Défauts relevés** (III.2).
  - Aucun contrôle positif : un banc insensible ne se distingue pas d'un texte sans danger (A, B, F).
  - Aux effectifs indiqués, l'indécision est quasi certaine, et elle mène au report : le choix est fixé par l'a priori (A).
  - La réplique fictive et Pythia ne se transportent pas à la cible réelle (A, B, C, E, F).
  - Les « heures de reprise évitées » ne s'observent pas (A, B, C, E, F).
  - Le tiers dépositaire devient une personne informée (A).
- **Après les critiques** (D, III.3).
  - Astra accepte, retire la réplique comme substitut de la cible et le tournoi de la règle de décision.
  - Premier duel : sur le texte exact, avec ses auteurs, sa date et son titre, devant des lecteurs autorisés puis exclus de l'étude. Trois bras : travaux voisins seuls, travaux voisins plus billet, travaux voisins plus note neutre. Réponse libre notée en aveugle, sans liste de choix.
  - Préalable : établir en privé, pour chaque mesure, le triplet « élément réservé, qui doit l'ignorer, jusqu'à quand ».
  - Repère de dimensionnement : environ 12 800 unités par bras pour trancher une marge de 3 points (illustratif).
  - Le crédit devient une question documentaire sur archives datées. La qualité compare des coûts enregistrés, sur le même texte, entre discussion publique et revue confidentielle.
  - Il rejette une critique : une reformulation n'a pas à passer pour le même fichier, seulement pour le même plan.
  - Choix maintenu : dépôt privé contrôlé, report jusqu'à la fin effective du recueil, relecture confidentielle dès maintenant.

### Carbon (identifiant gemini-4-carbon, lettre E)

- **Proposition centrale** (E, III.1). Six présupposés, dont la confusion entre publicité en clair et preuve publique d'antériorité. Cinq contenus, dont un « appel public à banc d'essai partagé » qui transformerait la course en coordination. Pour la vérification après coup, une idée propre : dater le script de génération des sondes par la valeur future d'une balise aléatoire publique.
- **Plan** (E, III.1). Quatre duels : contamination par indexation ou ajustement fin léger ; évasion d'un adversaire informé, avec contrainte d'utilité ; reconnaissance, billet lisible contre empreinte ; effet du verrouillage sur le biais d'optimisme. Coût avancé : 126 à 2 326 euros (illustratif).
- **Choix** (E, III.1). Publier après, précédé d'une empreinte scellée encadrée par la balise.
- **Défauts relevés** (III.2).
  - Décisions sur estimation ponctuelle, sans zone d'indécision : au seuil, chaque hypothèse est « réfutée » une fois sur deux (A, C, F).
  - Le seuil absolu de détection sous divulgation ignore le bras sans divulgation (A, B, F).
  - Filtrer les attaques sur l'utilité après coup crée un biais de survivant (A, C, D, F).
  - Le « contrôle négatif » par détecteur factice est en fait un contrôle positif (B, C, D, F).
  - Le seuil de 0,57 du contrôle permuté est mal calibré : le maximum attendu vaut environ 0,55 (B, C).
  - La balise ne prouve pas l'absence de mesures avant le dépôt, ni l'absence de dépôts multiples abandonnés (A, B, C, D, F).
- **Après les critiques** (E, III.3).
  - Carbon accepte presque tout (35 critiques comptées, 27 acceptées, 6 en tests, 2 rejets).
  - Rejet 1 : il maintient « vérifié » pour les propriétés cryptographiques conditionnelles, l'implémentation réelle restant une hypothèse.
  - Rejet 2 : il refuse d'interroger des services fermés pendant l'arbitrage, car journaliser les sondes chez un tiers serait une fuite.
  - Il propose une règle de décision différente des autres (section 4).
  - E1* : index dilué à 100 000 documents, mesure explicite de la probabilité de récupération du billet.
  - E2* : 150 paires de campagnes sans retour du détecteur, issue conjointe « non détecté et utile ».
  - E3* : cinq bras, statistique de Mann et Whitney.
  - E4* : soixante tâches historiques.
  - Registre public à identité liée contre les dépôts multiples ; vecteur de scores de référence dans l'arbre de l'empreinte.

### Neon (identifiant gemini-4-neon, lettre F)

- **Proposition centrale** (F, III.1). Dix présupposés, dont l'asymétrie de réputation si le détecteur échoue après une annonce. Six contenus, du condensat horodaté muet au protocole complet sous embargo avec revue fermée.
- **Plan** (F, III.1). Quatre expériences : gain d'évasion d'une équipe rouge ; contamination par vingt canaris publiés ; reconnaissance par vignettes, jury aveugle aux dates ; qualité, dépôt public contre revue fermée.
- **Choix** (F, III.1). Publier après ; scellement immédiat et revue fermée sous embargo.
- **Défauts relevés** (III.2).
  - Le seuil de Fisher est incohérent : une sonde sur vingt contre zéro donne p = 0,5, pas moins de 0,01 (A, B, C, D, E).
  - Avec zéro sur vingt, la borne haute vaut environ 14 à 17 % : l'issue « sans contamination » est impossible (A, B, C, D, E).
  - Le choix n'est donc pas révisable en pratique (A, E).
  - Cinq tours de retour du détecteur écrasent l'écart entre bras (A, C).
  - Un jury aveugle aux dates ne peut pas juger une antériorité (A, D, E).
  - Publier vingt canaris signale la campagne (B).
- **Après les critiques** (F, III.3).
  - Neon accepte les erreurs de calcul comme « erreur mathématique directe ».
  - Exp. 1 : soixante agents par bras, régime principal sans retour du détecteur, clones synthétiques.
  - Exp. 2 refondue : audit passif de 150 prépublications authentiques d'autres équipes, parues sur le canal cible, appariées à 150 items privés, interrogation unique des vrais systèmes cibles.
  - Exp. 3 : dates visibles, 250 chercheurs par bras.
  - Exp. 4 : même document en fermé et en public.
  - Rejet partiel 1 : un condensat peut recevoir un jeton d'horodatage gardé privé, ou être ancré sans identité.
  - Rejet partiel 2 : la reconnaissance est un jugement communautaire, donc mesurer les normes du jury est l'objet pertinent.
  - Choix maintenu.

## 4. Accords et désaccords

### Accords indépendants au tour III.1

- **Les éléments secrets ne se publient jamais avant la fin** (A, B, C, D, E, F).
- **Séparer la preuve de date de la publicité.** Empreinte salée horodatée, ou dépôt sous embargo chez un tiers (A, B, C, D, E, F). Cinq le présentent comme une option que la question oubliait (A P9, B S2, C P2, E présupposé 6, F présupposé 7).
- **Une gradation des contenus.** Question et périmètre ; hypothèses, métriques et seuils ; mécanisme du détecteur ; éléments secrets. Plus le contenu est précis, plus il protège l'attribution et plus il renseigne adversaire et concurrents (B S8, et les tableaux des six).
- **Le signe de l'effet sur le devancement est inconnu.** Dissuasion ou attraction (A P8, B E3, D, E présupposé 5, F présupposé 4). Argon penche pour une hausse du risque avec tout texte lisible (C, tableau 2.1).
- **Un texte sans données vaut peu comme crédit.** Le crédit irait au premier résultat (C P1, E présupposé 1, F présupposé 3, D tableau) ; tous le marquent hypothèse, à vérifier.
- **Le contrefactuel n'est pas observable sur un cas** (A P10, B S7, D portée, F présupposé 9). Juger sur l'issue est un biais de résultat (B S7).
- **Le détecteur doit battre des vérifications mécaniques** : longueur, mots-clés, perplexité, régression sur groupes de lettres ou de mots, sur des cas honnêtes appariés (A, B, C, D, E, F).
- **L'exécution hors ligne sur des modèles ouverts figés** est la façon de tester sans fuite (A, C, E, F). Fable ajoute qu'un modèle dont les poids précèdent le texte ne peut pas l'avoir appris, par simple chronologie, mais que cela ne vaut ni pour des personnes, ni pour des systèmes servis et mis à jour (A, III.1 (d)).

### Convergence née des critiques

- **Règle de lecture.** Proposée par Astra (D, III.1 et III.2) : deux hypothèses complémentaires autour d'une marge unique ; un intervalle entièrement d'un côté réfute l'autre ; un intervalle à cheval est « non concluant ». Reprise nommément par Fable, Opus, Argon et Neon au III.3. Carbon en adopte une variante (voir les désaccords).
- **Contrôle positif par un détecteur factice fragile.** Idée de Carbon (E, III.1), qu'il appelait contrôle négatif. Requalifiée en contrôle positif par Opus, Argon, Astra et Neon (III.2), adoptée par Fable, Opus, Argon, Carbon et Neon (III.3). Elle sépare un adversaire trop faible d'un détecteur robuste.
- **Issue conjointe « évadé et utile », sur toutes les tentatives.** Critique de Fable contre Opus et Carbon (A, III.2) ; adoptée par Opus, Argon, Carbon et Neon.
- **Attaques sans retour du détecteur** dans le régime principal. Critique de Fable et d'Argon contre Neon ; adoptée par Neon, Argon, Carbon et Opus.
- **Lots honnêtes disjoints** pour fixer le seuil et pour le tester (C, D, F, III.2) ; adoptés par les six.
- **Placebo du même domaine, sans mécanisme**, plutôt qu'un sujet sans rapport ou un faux détecteur (E, F contre B ; B contre E). Opus en fait un duel (E1b) ; Carbon et Neon l'adoptent ; Argon garde un placebo « sur un sujet connexe sans rapport » (C, III.3).
- **Dates visibles et note datée après le rival** comme contrôle négatif de reconnaissance. Contrôle d'Opus (B, III.1), repris par Fable, Argon, Carbon, Neon et Astra.
- **Ne jamais tester en publiant contre la cible réelle.** Contre l'Exp. 1 d'Argon ; Argon passe sur jumeau hors ligne.
- **Une fuite du procédé est invisible à une comparaison « avant, après ».** Contre l'E6 d'Opus (A, C, D, E, F). Une famille orthogonale, non concernée par le texte, sert de témoin : Opus (E6b) et Argon (Exp. 1) l'adoptent.
- **L'empreinte révèle des métadonnées et ne prouve pas l'unicité du dépôt.** Fable (A, I2), Argon (contre la balise de Carbon), Astra et Neon. Réponses : registre public à identité liée (E, C), canari propre à l'exemplaire déposé (B), dépôt chiffré sans accès du dépositaire (D). Fable note l'arbitrage : un registre lié à l'identité rend les dépôts comptables mais révèle l'existence et la date du projet (A, III.3).
- **Une empreinte d'archive entière signale toute reformulation.** Arbre séparant prose, spécification, code et vecteur de scores sur un jeu étalon (Carbon puis Argon, avec la critique de Neon).
- **Interroger souvent contamine.** Argon contre Opus et Neon (III.2) : Opus compare une cohorte interrogée chaque semaine à une cohorte interrogée à la fin ; Neon passe en interrogation unique.

**Calculs sur lesquels les modèles divergent légèrement.** Une sonde sur vingt contre zéro donne p = 0,5 au test exact de Fisher : les cinq critiques concordent. Pour atteindre p < 0,01 avec zéro côté privé, il faut 7 sur 20 selon Fable, environ 6 selon Opus et Carbon ; Argon donne les deux, 7 en bilatéral et 6 en unilatéral (p ≈ 0,0101). Avec zéro sur vingt, la borne haute vaut environ 17 % (Fable), 14 % (Opus, Astra, Carbon) ; Argon et Neon donnent 16,8 % en bilatéral et 13,9 % en unilatéral. Le nombre de canaris nécessaire pour passer sous 5 % vaut 72 en bilatéral et 59 en unilatéral (Argon) ; Carbon écrit que la borne reste au-dessus de 5 % jusqu'à 58. Le lecteur n'a rien recalculé.

| Modèle | Première expérience au tour III.3 | Ce qu'elle expose | Coût avancé (illustratif) |
|---|---|---|---|
| Fable (A) | Étape 1 de D1′ : le secret est-il devinable sans le texte, et le test repère-t-il des fuites diffuses ou seulement grossières ? | Rien ; modèles figés hors ligne | Quelques heures de calcul |
| Opus (B) | E1′, volet agents, avec la famille orthogonale (E6b) ; E2′ en parallèle | Rien pour E1′ ; pages de test en ligne pour E2′ | Non chiffré au III.3 |
| Argon (C) | Étalonnage du détecteur sur pilote synthétique, puis devinette et évasion hors ligne sur le brouillon | Rien | 25 heures de carte graphique, environ 50 dollars |
| Astra (D) | Duel de lecture sur le texte exact contre les travaux voisins seuls | Le billet, à des lecteurs autorisés puis exclus | Non chiffré |
| Carbon (E) | Viabilité du détecteur hors échantillon, puis E2* (évasion sous divulgation contre placebo) | Rien | Moins de 150 euros |
| Neon (F) | Audit passif de 150 prépublications d'autres équipes, interrogation unique des vrais systèmes cibles | Requêtes aux systèmes cibles | Moins de 25 euros de calcul, plus les frais d'interface des systèmes |

### Désaccords

- **Un texte lisible avant les mesures ?** Opus oui (question, hypothèses, métriques), avec empreinte et embargo (B, III.3). Fable seulement si D1′ réfute la fuite (A, III.3). Argon, Astra, Carbon et Neon non (C, D, E, F, III.3). Les critiques n'ont pas tranché : aucune mesure ne départage.
- **La forme de la règle de décision.** Cinq modèles gardent une zone « non concluant ». Carbon sépare deux hypothèses par un écart (par exemple 2 et 7 points) et calibre l'effectif pour que l'estimation tombe toujours d'un côté d'un pivot (E, III.3). Sa règle ne laisse aucune issue muette, si la précision prévue est atteinte. Elle n'a pas été critiquée, puisqu'elle date du dernier tour.
- **Questionnaire fermé ou réponse libre.** Argon et Neon reprochent au questionnaire de fournir les réponses (C, F, III.2). Fable rejette ce biais sur l'écart entre bras et ajoute une réponse ouverte recueillie d'abord (A, III.3). Argon garde un choix parmi dix dispositifs réels (C, III.3). Astra passe à la réponse libre notée en aveugle (D, III.3).
- **Toucher ou non les vrais systèmes cibles.** Neon interroge les vrais systèmes cibles dès sa première expérience (F, III.3). Carbon refuse d'interroger des services fermés pendant l'arbitrage, car les sondes y seraient journalisées (E, III.3, rejet A.6). Argon, Fable et Carbon restent sur des modèles ouverts hors ligne. Neon n'a pas été critiqué sur ce point, sa refonte datant du dernier tour.
- **Le statut « vérifié ».** Argon l'appose à des références et à des calculs ; Carbon à des propriétés cryptographiques ; Neon à des calculs. Fable et Opus le contestent pour les références d'Argon (A, B, III.2). Argon accepte sur le fond sans changer ses statuts ; Carbon maintient (E, III.3, rejet B.8). Fable, Opus et Astra ne se l'attribuent pas.
- **Ne rien publier, même après.** Argon, Carbon et Neon l'admettent si le dispositif protège un système actif sans correctif, ou si les mesures sont contaminées (C, E, F). Astra rappelle que ne pas publier de billet ne justifie pas de taire des résultats défavorables (D, III.1 et III.3). Argon a retiré sa clause « échec dû à un défaut local » (C, III.3).
- **Effectifs pour la reconnaissance.** Quarante pairs par bras (Argon), 120 avec une statistique de rangs (Carbon), 250 (Neon), environ 340 (Opus), 175 à 430 selon la comparaison (Fable). Aucun modèle ne justifie ses marges autrement que par un exemple.
- **La reconnaissance se mesure-t-elle par un jury ?** Neon : oui, c'est un jugement communautaire (F, III.3). Astra : non, une question documentaire sur archives datées (D, III.3). Opus : par vignettes, en intention déclarée (B).

## 5. Ce qui est neuf, ce qui est fragile

### Neuf, au regard de ce que les modèles citent comme connu

Aucun modèle ne revendique de nouveauté. L'engagement scellé, le préenregistrement et le principe de Kerckhoffs sont présentés comme connus. Pourraient être propres au dossier, sous réserve d'une recherche bibliographique que personne n'a faite :

- tester d'abord si le secret est déjà devinable sans le texte, et fixer la résolution du test par une gamme de fuites plantées, dont une seulement déductible avec les travaux voisins (Fable, A, III.3) ;
- le triplet « élément réservé, qui doit l'ignorer, jusqu'à quand », établi en privé pour chaque mesure avant toute discussion de publication (Astra, D, III.3) ;
- une famille orthogonale d'éléments secrets, non concernée par le texte, comme témoin de la fuite de procédé (Opus, B, III.3 ; Argon, C, III.3) ;
- un canari propre à l'exemplaire déposé chez le tiers, qui traite le dépositaire comme une personne informée (Opus, d'après la critique de Fable contre Astra) ;
- une empreinte en arbre avec un vecteur de scores sur un jeu étalon, qui sépare une refactorisation neutre d'un changement de comportement (Carbon, Argon, III.3) ;
- la balise aléatoire publique future qui date l'instanciation des sondes, avec ses limites reconnues (Carbon, E, III.1 et III.3) ;
- l'audit passif de la contamination sur des prépublications authentiques d'autres équipes, sans rien émettre (Neon, F, III.3).

### Fragile

- **Aucun banc ne se transporte à la cible réelle.** Modèles figés, jumeaux, vignettes fictives : tous mesurent un effet sous exposition forcée, pas la probabilité qu'un système ou une personne lise le texte (A, D, E, III.3). Astra le dit sans détour : une réplique fictive peut vérifier qu'un test décèle une fuite, elle ne peut pas innocenter le vrai billet (D, III.3).
- **Les effectifs utiles sont élevés.** Environ 12 800 unités par bras pour une marge de 3 points (D, III.3) ; plusieurs centaines de juges par bras pour la reconnaissance ; de l'ordre d'un millier de courses par bras pour la concurrence (A, C, III.2). Les questions de crédit et de devancement sont probablement hors de portée d'une seule équipe.
- **L'effet sur le devancement reste non identifiable.** L'étude observationnelle d'Opus n'a plus le pouvoir de faire basculer le choix (B, III.3) ; Fable retire son taux de base (A, III.3).
- **L'empreinte ne prouve pas tout.** Ni l'absence de pilotes avant le dépôt, ni, sans registre nommé, l'unicité du dépôt (A, B, C, D, III.2 ; Carbon l'accepte, E, III.3). Carbon écrit pourtant encore, dans sa synthèse, que l'empreinte « prouve mathématiquement » l'absence de retouche fonctionnelle (E, III.3, (c) 1).
- **Les 0 % et 100 % de l'arbre d'Argon** sont de nouveau des affirmations par construction, non éprouvées (C, III.3, 2.5), alors que la même forme avait été réfutée au tour précédent.
- **Les règles et plans du dernier tour n'ont pas été critiqués.** Cela vaut pour la règle à pivot de Carbon, l'audit passif de Neon sur les vrais systèmes cibles et le duel de lecture d'Astra devant des lecteurs informés.
- **Le test de devinette du dossier lui-même n'est pas transmis.** Les modèles l'imaginent (A, C, E) sans le connaître.
- **Calculs « vérifiés » sans vérificateur extérieur.** Les petites discordances du chapitre 4 montrent que le contrôle croisé laisse passer des écarts de convention.
- **Coûts.** De 12 euros (pilote d'Astra) à plusieurs milliers d'euros (volets humains d'Opus, de Carbon, de Neon) ; tous illustratifs, sans ingénierie ni temps de recrutement.

## 6. Références à vérifier

Aucune de ces références n'a été vérifiée. Toutes sont citées de mémoire par les modèles, qui inventent parfois des titres, des auteurs ou des années. Argon les marquait « vérifié » au tour III.1, statut contesté par Fable et Opus.

| Référence telle que citée | Qui la cite | Pour quoi faire |
|---|---|---|
| Kerckhoffs (1883), « La cryptographie militaire », *Journal des sciences militaires* | Fable, Carbon, Neon ; Opus nomme le principe | La sécurité ne doit reposer que sur la clé |
| Kerr (1998), « HARKing: Hypothesizing After the Results are Known » | Fable, Argon | Hypothèses formulées après les résultats |
| Nosek, Ebersole, DeHaven, Mellor (2018), « The preregistration revolution » | Fable, Argon | Préenregistrement |
| Merton (1957), « Priorities in Scientific Discovery » | Fable | Courses à la priorité |
| Tramèr, Carlini, Brendel, Madry (2020), « On Adaptive Attacks to Adversarial Example Defenses » | Fable | Attaquant trop faible pour départager |
| Shannon (1949), « Communication Theory of Secrecy Systems » | Argon | Cité pour l'horodatage par hachage ; attribution contestée (Fable, Opus), retirée par Argon |
| Haber, Stornetta (1991), « How to Time-Stamp a Digital Document » | Argon (III.3) | Horodatage par hachage |
| Goodhart (1975), « Problems of Monetary Management: The U.K. Experience » | Argon (titre ajouté au III.3) | Adversaire qui optimise contre la règle connue |
| Platt (1964), « Strong Inference » | Argon, Carbon | Inférence forte |
| Clopper, Pearson (1934), « The Use of Confidence or Fiducial Limits Illustrated in the Case of the Binomial » | Argon (III.2) ; borne employée par tous | Borne après zéro succès |
| Gail, Wieand, Piantadosi (1984), « Biased estimates of treatment effect in randomized experiments with nonlinear regressions and omitted covariates » | Argon (III.2) | Biais par covariable omise |
| Schoenfeld (1983), « Sample-Size Formula for the Proportional-Hazards Regression Model » | Argon (III.2) | Effectif d'un modèle de risques proportionnels |
| DeLong, DeLong, Clarke-Pearson (1988), « Comparing the Areas under Two or More Correlated Receiver Operating Characteristic Curves… » | Argon (III.2) | Variance d'une aire sous la courbe |
| Hanley, McNeil (1982), « The Meaning and Use of the Area under a Receiver Operating Characteristic (ROC) Curve » | Argon (III.2) | Idem |
| Mann, Whitney (1947), « On a Test of Whether one of Two Random Variables is Stochastically Larger than the Other » | Carbon (III.3) | Statistique de rangs |
| Intervalle de Garwood ; intervalle de score de Wilson et Newcombe ; indice d'accord « AC1 » ; delta de Burrows | Argon ; Neon (« référence à vérifier ») ; Neon ; Argon | Intervalle de Poisson ; différence de proportions ; accord entre juges ; stylométrie |
| Horodatage par un tiers, norme RFC 3161 ; OpenTimestamps ; dépôts sous embargo d'OSF ou de Zenodo | Neon, Argon ; Argon ; Opus, Argon | Horodatage ; durée maximale d'embargo à vérifier (Opus) |
| Balise publique d'aléa (Carbon ; « balise NIST » selon Argon) | Carbon, Argon | Dater l'instanciation des sondes |
| Format « Registered Report » | Argon, Carbon (« référence à vérifier ») | Revue du protocole avant collecte |
| OpenAlex | Opus | Métadonnées bibliographiques |
| Pratique des chaînes-canaris ; travaux empiriques sur les courses à la priorité | Fable (« à vérifier », non nommés) | Contrôle de fuite ; taux de base |
| Modèles ouverts : Llama 3.1 et 3.3, Qwen2.5, Mistral 7B et Small 24B, Pythia, Gemma ; encodeur BAAI/bge-m3 | Fable, Opus, Argon, Astra, Carbon, Neon | Versions, licences et dates de gel à vérifier (Fable) |

## 7. Propositions retenues et non retenues

Critères appliqués : soutien de plusieurs modèles, résistance aux critiques, coût, réversibilité, et ce que la proposition tranche pour la suite.

### Retenues

1. **Sceller maintenant le protocole complet, dans un seul dépôt nommé, en écrivant ce que le dépôt révèle et ce qu'il ne prouve pas.**
   - *Soutien.* Les six, indépendamment, au III.1.
   - *Ce qui a été corrigé.* L'empreinte révèle une date, et selon le registre une identité (E, F contre A ; C contre lui-même). Elle ne prouve ni l'absence de pilotes antérieurs ni l'unicité du dépôt sans registre nommé (A, B, C, D contre E). Le dépositaire devient une personne informée (A contre D), d'où le canari propre à l'exemplaire (B) ou le dépôt chiffré sans accès (D).
   - *Coût.* Quasi nul.
   - *Point ouvert.* Registre public lié à l'identité (dépôts comptables, projet visible) ou dépôt confidentiel chez un tiers (projet caché, confiance dans le tiers) : l'arbitrage de Fable (A, III.3) n'est pas tranché.

2. **Établir en privé, pour chaque mesure, quel élément doit rester ignoré, par qui, et jusqu'à quand.**
   - *Soutien.* Astra (D, III.1 et III.3) ; Fable y renvoie en séparant personnes et modèles figés (A, III.1 (d)) ; Opus et Carbon distinguent les canaux d'ingestion (B S5, E présupposé 2).
   - *Ce qu'elle tranche.* Si les « systèmes » à tenir ignorants sont des modèles figés exécutés hors ligne, la publication ne peut pas les atteindre, par chronologie (A). Si ce sont des personnes ou des systèmes servis et mis à jour, l'ingestion devient la question centrale.
   - *Coût.* Une demi-journée de travail interne ; aucune exposition.

3. **Avant tout texte lisible, des tests hors ligne non destructeurs, dans cet ordre.**
   - (a) Le secret est-il déjà devinable sans le texte, et le test repère-t-il des fuites diffuses (A, III.3) ? Si le domaine public suffit, l'argument de validité contre la publication tombe.
   - (b) Le texte exact laisse-t-il deviner davantage que les travaux voisins seuls, contre un placebo du même domaine, avec des devineurs ou lecteurs ensuite exclus de l'étude (A, D ; B et C par leurs devinettes et évasions) ?
   - *Soutien et résistance.* Quatre premières expériences sur six portent sur la fuite ou l'évasion hors ligne (A, B, C, E) ; celle d'Astra porte sur le texte exact. C'est la version qui a survécu aux critiques des questionnaires construits par l'équipe.
   - *Point faible.* Sous exposition forcée et sur modèles ouverts ; le transport à la cible reste une hypothèse (A, D).

4. **Qualifier d'abord le détecteur lui-même.** Il doit battre les vérifications mécaniques sur des cas honnêtes appariés, avec des lots disjoints pour le seuil et pour le test.
   - *Soutien.* Argon et Carbon le placent en premier (C, E, III.3) ; Neon en fait une condition (F) ; Opus pose un taux minimal de détection sans divulgation comme prérequis (B, III.3).
   - *Ce qu'elle tranche.* Sans cela, aucun test d'adversaire informé n'est interprétable, et il n'y a « rien à annoncer » (E, III.3).
   - *Point faible.* Le pilote ne doit pas entamer le jeu réservé de l'étude (B contre F, accepté par F).

5. **Lire toutes les expériences avec la même discipline.** Marge unique, intervalle et issue « non concluant » ; contrôle positif par un détecteur factice fragile ; issue conjointe « évadé et utile » sur toutes les tentatives ; attaques sans retour du détecteur ; placebo du même domaine.
   - *Soutien.* Adoptée par les six au III.3, Carbon avec sa variante à pivot.
   - *Coût.* Nul ; c'est une règle d'écriture.

6. **Pour la qualité, une relecture confidentielle plutôt qu'une discussion publique, en l'état.**
   - *Soutien.* Astra, Carbon et Neon la proposent dès maintenant (D, E, F, III.3) ; Argon avec la relecture interne (C).
   - *Ce qu'on sait.* Aucun plan transmis n'établit, sans publier, que la critique publique trouve davantage (A, III.3).

### À reprendre ensuite

- **L'ingestion par les systèmes** (Neon, Exp. 2 ; Opus, E2′). Seulement si la retenue 2 montre que des systèmes servis ou connectés doivent rester ignorants. L'audit passif de Neon interroge les vrais systèmes cibles : avant de le lancer, peser l'objection de Carbon sur la journalisation des requêtes.
- **L'effet du verrouillage** (plan 2 × 2 d'Argon ; E4* de Carbon sur soixante tâches historiques). Utile comme étude de méthode, sans lien direct avec la décision de publier.
- **La reconnaissance par vignettes** (A, B, E, F) et **la concurrence sur courses réelles** (D). Études de communauté, hors de portée d'une seule équipe aux effectifs avancés.

### Non retenues

- **Publier réellement un billet contre la cible pour mesurer son effet** (Argon, Exp. 1 au III.1) : l'expérience exécute la décision qu'elle prétend éclairer ; retirée par Argon.
- **Comparer des éléments secrets créés avant et après la publication** (Opus, E6) : aveugle à une fuite du procédé ; remplacée par la famille orthogonale.
- **Le taux de base du devancement sur douze mois** (Fable, D4) : presque toujours non concluant ; retiré comme duel.
- **Le corpus observationnel de drapeaux** (Opus, E3) : temps immortel et causalité inverse ; refondu sans pouvoir de bascule.
- **Le tournoi rémunéré de concurrence et la réplique à catégories fictives** (Astra) : non transportables ; retirés.
- **Le jury aveugle aux dates** (Neon, Exp. 3) : il mesure un recouvrement, pas une antériorité ; corrigé.
- **Le banc de décisions simulées comme juge du « bon choix »** (Opus, instrument 4) : il mesure l'accord avec son propre modèle ; rétrogradé.
- **Vingt canaris, seuils ponctuels sans intervalle, seuil absolu de détection sous divulgation, filtrage sur l'utilité après l'attaque** (Neon, Carbon) : non jugeables ou biaisés ; corrigés par leurs auteurs.
- **L'empreinte d'archive entière « à 100 % et 0 % »** (Argon, III.1) : contredite par ses propres cas honnêtes.
- **Taire un résultat négatif jugé « défaut local »** (Argon, III.1) : degré de liberté après coup ; retiré par Argon.

### Ce qui reste à trancher

- Le registre du dépôt : public lié à l'identité ou confidentiel chez un tiers (retenue 1).
- La nature des personnes et systèmes à tenir ignorants (retenue 2), qui décide si l'ingestion doit être mesurée.
- Le seul désaccord de fond qui subsiste : publier ou non, avant les mesures, un texte limité à la question, aux hypothèses et aux métriques (Opus pour, Fable sous condition, les quatre autres contre). Les retenues 3 et 4 sont les mesures qui le départageraient.
