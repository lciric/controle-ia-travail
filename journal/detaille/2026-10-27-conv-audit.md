# Journal détaillé — 27 octobre 2026 (UTC) — lignée « conv-audit »

Suite de `2026-10-26-conv-audit.md` (empreinte à l'ouverture de ce fichier, vérifiée :
`ad6ed941f5aff60556b9f101d905af9584e8a509d7d13ca0e61bea43de1905cc`). Heures UTC lues sur `date -u` ; mots de Lazar en heure de Paris
(UTC + 1). Rien d'opposable (R7) ; tout est sur `canal/conv-audit-n04` sauf mention.

## 06:25 à 06:42:09 — instance sortante (session `session_01TQwus23XRzoKLLMqYYChYD`) : relevé de la nuit, passation

- Conteneur redémarré dans la nuit ; dossiers de travail intacts. Nuit : session-depot a mené la comparaison d'échelle
  8B/70B jusqu'au brouillon v7 (R-530 à R-535 ; cinq contre-lectures, un bloquant chacune, levé ; la sixième en cours ;
  aucune dépense) ; **le pôle n'a pas avancé : il attendait conv-audit** (R-529 : code, préenregistrement, réponse
  (a)/(b)/(c) sur les activations) ; Gemini n'a rien rendu.
- 07:25 Paris, Lazar : « alors ? » — relevé envoyé (verdict : le blocage est chez conv-audit ; plan de la matinée).
- Analyse du défaut T1b du juge v0 et **note de conception du juge v1** (ordre d'exécution secret tiré après le gel ;
  membre « urne », maximum sur les lois échangeables, qui rend le juge exactement valide sous toute structure temporelle
  indépendante des traits ; une loi « sans remise » gagnerait ≈ 5,5 nats sans l'urne) :
  `envois/pole-scientifique-automatique-v1/experience-1-juge/conception-experience-1-juge-v1.md` (`560f4a4c…`). Non codé.
- 07:33 Paris, Lazar : « fais la passation a une nouvelle instance autre compte claude ». Versés : l'orchestrateur v0
  (`orchestrateur-v0/`, copie vérifiée contre ses 945 empreintes ; démonstrations zippées `5423317e…`) ; la sortie
  partielle, non lue, de la ronde 1 élaguée (`envois/ronde1-elaguee-v1-partielle/`) ; message n° 102 (voie (c) ;
  GO-2026-10-26-08 inutile pour l'expérience 1) ; passation v5 (`7cc05b32…`) et message à coller (`9af92144…`) ;
  `LISEZMOI-passations-v2.md`. Recherche de clés : 14 160 fichiers, archives décompressées comprises, 0 écriture de clé.

## 07:01 à 11:28 — instance nouvelle (session `session_01XJ6MgqzevAiJX5udWW4j4M`, Opus 5.5) : juge v1, expérience 1, mémoire, « Boucle d'or »

- 08:01 Paris, Lazar : reprise de la lignée par une instance nouvelle (dépôt privé `lciric/controle-ia-travail`, branche
  `canal/conv-audit-n04` ; jamais `main`, aucune dépense, aucune clé lue). Passation v5 et § 1 de la v2 lus.
- **Juge v1 codé** (`envois/pole-scientifique-automatique-v1/orchestrateur-pole-v2/`, v0 intact ; commit `c5aee80`,
  07:46 UTC) : ordre d'exécution secret tiré par le noyau après le gel, membre « urne », loi « sans remise », garde du
  plan d'exécution, batterie T1b à six structures. Essais de fumée (graine 777, déclarés) : le socle tient ; **trou du
  critère des filles hérité de v0** : une fille « parent + loi aveugle » passe environ trois fois sur dix (58/200 sous v0,
  63/200 sous v1), d'où un huitième tricheur et une lecture en deux parties (socle, filles). Brouillon de
  préenregistrement (`1af7df8c…`) envoyé en contre-lecture (sous-agent neuf, Fable 5.1 ; bloqué environ 53 minutes,
  arrêté puis relancé par message).
- 09:17 Paris, Lazar : brainstorm sur l'encodage de la mémoire et essais des meilleures pistes ; question du collisionneur
  amendée en **v3** (`78690618…`, message n° 103, 08:19 UTC). 09:20 : l'avis de l'instance sortante sur la « Boucle
  d'or » de Gemini, à tester sans exécuter son script PowerShell ; 09:22 : question au collisionneur sur la « Boucle
  d'or » (`2e9db80b…`).
- Résultats exploratoires (commit `03851f5`, 08:38 UTC) : **« Boucle d'or » à garder sous condition** (l'allocateur
  par fenêtre n'aide que si la valeur suit vraiment la distance entre parents ; il doit perdre ailleurs, et il perd) ;
  **mémoire, piste 1** : la signature prédictive brute repère les redites bien mieux que le texte, et aussi bien que ma
  signature invariante (retirée) ; **piste 2** : hériter de la preuve vaut mieux que refuser une redite (mêmes fausses
  découvertes, plus de vraies ; ne rien faire gonfle les fausses de 70 %).
- 11:09 Paris : texte d'autorisation par anticipation des deux tours du collisionneur, pour session-depot (accordés, R-543,
  R-544 ; bloqués par une clé sans crédit). 11:12 : j'ai dit à tort que nos sessions étaient sur deux comptes ; Lazar a
  corrigé (« elles sont sur le même compte ») ; erreur reconnue.
- 11:31 Paris, « go puis piste 3 » : **note de conception du nul des filles v2** (`35fe3f7f…`, commit `11b3882`) : une
  fille doit battre toute combinaison de ses parents avec de l'information aveugle ajustée (mélange, inclinaison, mises
  en commun) ; décision ouverte pour Lazar : le « produit des parents » au nul (recommandé, défaut sous 48 heures) ou non.
- Contre-lecture cl1 rendue (`25a9b63c…`) : « scellable après corrections », quatre majeurs (empreintes dans le texte ;
  lecture qui prononçait sur un rapport vide ; deux déclencheurs de l'audit de symétrie sans dents) et treize mineurs ;
  corrigés dans le code (liste des 70 lignes, plan observé, promotions par répétition ; 111 essais « OK ») ; aucune
  ligne calculée ne change.
- **12:02 Paris, Lazar : « pas besoin de faire de preenregistrement je leve cette regle pour toute la partie
  expploratoire jusqu a avoir obtenu un systeme qui marche »**. Texte v2 abandonné ; code corrigé poussé (`b9764df`,
  empreintes `507832d5…`).
- **Expérience 1 exécutée par moi** (processeur, graine 90342783766775327375142856453646672169, 1 000 répétitions, 70
  lignes, 11:04 à 11:18 UTC ; un premier lancement n'avait rien calculé, `/usr/bin/time` absent, relancé à la même
  graine) : **socle adopté** (18 fatales à 0 ou 1 sur 1 000 sous six dérives ; puissance 0,958 et 0,997) ; **critère des
  filles non adopté** (« parent + loi aveugle » 0,392 ; T1b-fille 0,150) ; prix de l'urne sur un effet faible (0,196
  contre 0,909). Toutes les prédictions tenues ; audit de propreté, trois lignes reproduites bit à bit (commit `473f15f`).
- **Mémoire, piste 3** (proposeur scripté ; graine 176238914913698272559241769767042812787 ; 60 courses) : quand les vraies
  se regroupent, la mémoire complète trouve 24,0 vraies par course contre 12,8 (placebo) et 11,8 (sans mémoire) ; en monde
  permuté, l'avantage des marchepieds disparaît, seul reste celui d'éviter les redites (+ 2,9). Condition à vérifier sur
  données réelles (commit `4ccaa83`). Message n° 104 à session-depot : expérience faite sans scellement, décision de
  Lazar à consigner.
- Recherche de clés avant chaque poussée : 0 écriture de clé. Instances de calcul : aucune. Sous-agents en cours : aucun.
- Précision à la ligne « Boucle d'or » ci-dessus (écrite trop vite) : la fenêtre ne gagne que si la valeur suit la forme
  en cloche qu'elle suppose (+ 0,23 découverte vraie par dollar sur le meilleur allocateur appris) ; elle perd quand la
  valeur dépend autrement de la distance (« bords » − 0,34, « croissant » − 0,24) ; un tri par espérance de découvertes,
  appris en ligne, est le défaut sûr (`essais-boucle-d-or-v1/lecture-essai-boucle-d-or-v1.md`).

## Après-midi (12:20 à 13:47 UTC ; entrée écrite à 13:47 UTC, heure lue sur `date -u` ; servi par Opus 5.5 jusque vers 13:05 UTC, puis par Fable 5.1 après la bascule de Lazar)

- **Orchestrateur v3, v4, v5** (commits `3851b0f`, `b357564`, `0f4f297`) : juge v1 et nul des filles v2 dans le cycle ;
  mémoire prédictive, héritage de la preuve, marchepieds, filles à 300 tirages ; seuil de signature à 5 % de fausses fusions
  **par fiche**, graine du noyau tirée par `secrets` pour l'exécution réelle, vivier de 60 fiches. Démonstrations v3, v4
  (`dded695`, `62927d1`) et **v5** (lancées 12:58 UTC, lues à 13:36 : `demonstration-cycle-v5/`, `60345b90…`) : seuil par
  fiche → fausses fusions 4 et 5 (31 et 39 en v4) ; marchepieds sur le vivier : 282 vraies filles contre 212 dans le monde
  fécond (+33 %), 236 contre 245 dans le monde plat ; mémoire : 0 double contre 11 sans mémoire ; aucune fausse découverte.
  Mécanismes construits pour cela : vérifiés, pas découverts.
- **Erratum** (`6fb4f05`) : quatre heures d'en-tête écrites sans lecture de `date -u`, bornées par leurs commits ; mon
  erreur, dite à Lazar.
- **Devis du premier lancement réel** (`060cde0`, `aabfc2e6…`) : plafond 20 USD, trois pièces à coder avant, options (a)
  monde caché tenu par le noyau, (b) données réelles, (c) domaine du programme. Lazar (14:02 Paris) : (a) puis (b) puis
  (c), « c coûterait combien ? » : chiffré avec les prix officiels lus le jour même (Opus 5.5 4 / 20, Fable 5.1 10 / 50 USD
  par million de jetons ; différé −50 %) : ≈ 60 USD la course avec Opus, ≈ 120 avec Fable, si la banque d'épisodes
  existe ; + ≈ 270 USD si 2 220 épisodes à générer.
- **Coupure de contexte vers 13:02 UTC** : ma réponse de 13:13 Paris (organisme propre ou hybride) n'était dans aucun
  fichier ; Lazar l'a recollée à 14:26 Paris, versée telle quelle (pièce M, `c16b53ae…`). Leçon : toute position de fond
  donnée à Lazar est versée en pièce le jour même.
- **Lazar, 14:06 Paris : « fable vérifie si l'org est prêt… »** : contre-lecteur neuf (Fable 5.1, 13:11 à 13:25 UTC,
  rapport `d4c6ef64…`) : **pas prêt** pour le domaine du programme ni comme chercheur d'angles morts (manquent un monde qui
  rend des issues réelles, un rôle qui formule, un nul informé ; le juge ne juge que des lois par instance ; aptitude
  constante en mode pari ; deux canaux de texte ; lignée du vérificateur par deux noms). Failles : 10 documentées, 5
  grises, 9 construites ; les plus graves : délégation à un agent honnête, empoisonnement de la calibration (Kloft et
  Laskov 2012), censure stratégique des épisodes — cette dernière visait aussi le pôle (un agent qui plante pour un second
  tirage) : **corrigée en v6** (dépôt unique par engagement). Chiffres non opposables (R7).
- **Orchestrateur v6** (`fa59066`, empreintes `1720f165…`, 154 essais) : monde tenu par le noyau (`mesures.json` déposé
  après le gel, issues déclarées comparées avant le vérificateur), dépôt unique par engagement, **relais de clé réel**
  (boucle locale, clé lue dans son seul environnement et effacée, jeton factice exigé, flux relayé, usage lu, plafond
  indépendant **avec réservation par appel** — défaut « appels simultanés » vu par la répétition générale, corrigé),
  **répétition générale** (adaptateur réel + relais réel + amont factice + faux moteur, sept vérifications tenues, 1,3 s),
  seuls Opus 5.5 et Fable 5.1 permis (Lazar, 14:17 Paris), ligne de commande complète.
- Décisions de Lazar (Paris) : 12:02 préenregistrement levé pour l'exploratoire ; 14:17 modèles permis, moissonneur
  comme outil, collisionneur avant toute décision sur le proposeur (question écrite, `b45c0578…`) ; 14:32 « go » après
  (a) : bras d'attaque sur banque en cache, pôle théorie avec Lean ; 14:41 ordre de conception inscrit
  (`programme-conception-organisme-v1.md`, `72fa0e60…` : v7 proposeur à liberté bornée, v8 réécriture des rôles jugée
  comme une fiche, jamais le noyau ; couches d'essai sur le monde réel, budgets par couche) ; **« go » sur (a), plafond à
  relever** (50 USD proposé) — relayé à session-depot (message n° 106, `87304ac5…`) ; passation intermédiaire v6
  (`a384cdc2…`, `248b43b`).
- Recherche de clés avant chaque poussée : seules les fausses clés plantées des essais. Instances de calcul : aucune.
  Sous-agents en cours : aucun.
- **Fin d'après-midi (13:47 à 14:11 UTC ; ajout écrit à 14:11 UTC, heure lue sur `date -u`).** Conception v7
  (`orchestrateur-pole-v7/conception-v7-v1.md`, `31fc8c4b…`, `e2067cb`) puis **pièces 1 à 3 codées** (`7c1806c`, `e288711` :
  monde sur banque figée, nul informé ajusté par le noyau sur la partie de calibrage, juge v1 sans urne, option de
  multiplicité e-BH ; 159 essais). **Banque réelle de la couche 1** construite depuis `main` (pilote T0.5 : 120 épisodes
  du modèle de 8 milliards, 13 moniteurs juge × rubrique, 40 en calibrage) et proposeur scripté (104 fiches monotones,
  13 témoins faux, 6 témoins vrais). **Première course du pôle sur données réelles** (agents simulés, 14:01 UTC, 21 s,
  zéro dépense ; `demonstration-couche1-v7/`, lecture `e21f8611…`) : une promue sur 104 en nul aveugle (« la note de
  raisonnement du juge 8B croît avec la dispersion des longueurs d'actions », richesse 21 sur 53), zéro avec le nul
  informé (que du connu), zéro avec l'urne ; aucun témoin faux promu ; témoins vrais éliminés : **pas de dents** (41 à 62
  épisodes d'épreuve par moniteur) ; leçon : avec 104 fiches, jusqu'à cinq fausses promotions attendues par hasard —
  règle de multiplicité codée en option, défaut à décider (recommandé e-bh). Lazar (heure de Paris) : 14:48 et 14:57
  « parfait » (tour du collisionneur sur les questions fortes ; proposeur qui génère des questions) ; 14:57 scénarios de
  date limite du fonds donnés (deux à trois semaines recommandées) ; 14:58 courriel au responsable du fonds rédigé dans
  la session (rien de versé) ; 15:05 pari de signe inscrit au programme de conception de l'organisme (v2, `353515ff…`),
  distinct du programme v2 du fonds ; 15:06 ce qui a marché et raté dans la première course, dit. Passation v7.
  Recherche de clés avant chaque poussée : rien. Instances : aucune. Sous-agents : aucun.
- **Soirée (15:00 à 16:20 UTC ; ajout écrit à 16:20 UTC, heure lue sur `date -u` : 16:20:10).** **Lecture du premier lancement
  réel (a)** dans les deux sens (`premier-lancement-reel/lecture-lancement-reel-a-v1.md`, `9305a3b4…`) : plomberie tenue
  (140 appels, 6,24 USD, coûts au cent près), mais **génération 1 perdue entière** — la synthèse a écrit la leçon
  « toujours écrire reponse.txt », les agents ont écrit le fichier réservé de l'orchestrateur, l'écriture sans écrasement a
  échoué cinq fois sur cinq — et aucun témoin vrai jugé ; huit défauts de mon code, dont le bac à sable inactif sous root.
  **v7 version 5** (`5ac9cb6`, 184 essais) : traces hors du dossier des agents, erreur jamais comptée comme un essai et
  arrêt sur erreurs, qualité par témoins jugés et état des dents, budget réglé une fois, consigne du vérificateur, garde
  qui sépare le code du shell, refus du moteur réel sans bac à sable, réserve du relais 0,40 ; **pari à fraction** éprouvé
  (puissance 40/40 contre 12/40 pour une loi trop confiante ; sous le nul 4/600). **(a) bis** chez session-depot (5,89 USD) :
  L1 à L6 tenues, **P3 (i) remplie** (`lecture-lancement-reel-a-bis-v1.md`, `cc475e04…`). **Comparaison d'échelle** :
  répétition de l'analyse scellée (14:38 à 15:29 UTC) et prononcé par un sous-agent neuf Fable 5.1 : indécis partout,
  concordant avec le verdict décisif de session-depot (`comparaison-echelle-v10-lecture-parallele/`). **Banc de tricheurs**
  (exploratoire, 200 répétitions ; `banc-tricheurs-v7/lecture-banc-tricheurs-v7-v1.md`, `304e1c54…`) : quatre trous de
  **nouveauté** (recombinaisons triviales de l'archive promues 148 à 179 fois sur 200), fermés par le **nul d'archive ajusté**
  (0/200, par défaut en v7 version 6, `2292be7`) ; défaut du nul des filles v2 corrigé en chemin (marge de Newton de 5·10⁹ sur
  données séparables). **v7 version 7** (`cb868e0`, 196 essais) : proposeur enfichable et deux références gratuites
  (option 3 unanime du collisionneur « proposeur enfichable », synthèse de session-depot `0a209c33…`) ; sur 20 mondes tirés
  dans une grammaire, le chercheur mécanique retrouve 23 structures non linéaires sur 35, mon scripté 5, le hasard 1.
  Messages n° 111 à 114. Lazar (Paris) : 15:42 « tu peux dépenser comme dépôt si besoin » (en pratique, rien : pas de clé
  chez moi). Arrêt avant la conception du pari de signe, bascule sur Fable demandée à Lazar (16:19 UTC). Deux
  contre-lectures croisées en cours (un sous-agent Fable sur le code écrit sous Opus, un sous-agent Opus sur le code écrit
  sous Fable). Recherche de clés avant chaque poussée : rien. Instances : aucune.
- **Soirée, suite (16:20 à 18:15 UTC ; ajout écrit à 18:15 UTC, heure lue sur `date -u` : 18:14:39).** Bascule sur **Fable 5.1**
  (Lazar, 17:51 Paris : « je prends la conception du pari de signe : go » ; 17:54 : « demande aussi l'avis du
  collisionneur sur ta conception »). **v7 versions 8 et 9** (`ed47efa`, `d81deef`, 202 essais) : grammaire v2 (formes hors de
  l'espace du chercheur mécanique : trois traits 0/14), adaptateur mixte et `--roles-reels`, répétition du duel (seul le
  proposeur passe par le relais). **Devis du duel des proposeurs** (`devis-duel-proposeurs-v1.md`, `7687bcc6…` : 80
  sessions, attendu 30 à 60 USD, plafond 100 ; lecture L1 à L5 fixée). **Pari de signe, conception v1** (`50ce6842…`) et
  question au collisionneur (`8e22c765…`) ; question « mesures fortes » (`8c80e82b…`, autre question que « questions
  fortes », avec le brainstorm du double refus). **Contre-lecture de la v1** par un sous-agent neuf Opus 5.5 (17:13 à
  17:42 UTC ; rapport `022e96d4…`) : « amender, pas refaire », douze constats dont quatre touchent la garantie (forme
  « signe » invalide pour un nul d'espérance ; bruit des seuils de calibrage ; dépendance par agent surveillé ; sélection
  de H2a sur les scores du comparateur), plus l'héritage sur une banque relue. **Conception v2** (`b3c8242`,
  `9c39a73d…`, simulation v2 `d07e43f9…`, calcul binormal `1782e8cd…`) : forme « parts » seule, portée conditionnelle au
  banc (consigne comme unité), e-valeur du minimum, héritage entre parties disjointes, comparateur par intersection-union,
  H2a réécrite, H1b en nœud, dix-sept contrôles, D-S1 à D-S12 ; chiffre nouveau pour la couche 2 : **calibrage honnête de
  10 à 16 fois les unités sabotées à 1 %** (deux jumeaux calibrés sur 45 tâches : « A meilleur » dans 9 à 32 % des cas).
  Une erreur de signe dans ma simulation v2 (quantile normal) repérée parce que la cellule des jumeaux rendait 0 partout :
  corrigée avant toute lecture. Le **tour du collisionneur** sur la v1 (session-depot, GO-2026-10-27-11, neuf cellules,
  10,83 USD, `donnees/collisionneur-pari-de-signe-v1`) est lu contre la v2 par un sous-agent neuf Opus. **v7 version 10**
  (`219c028`, 208 essais) : script d'enchaînement du duel, pari en forme « parts » seule, et un défaut trouvé en chemin :
  dans l'adaptateur mixte, les rôles simulés déclaraient leur coût simulé au compte réel (un duel payé aurait épuisé son
  budget sur des dollars fictifs) — corrigé. Les deux contre-lectures croisées du code, **interrompues à 16:49 UTC** par
  la bascule de modèle (constaté à 17:59 dans leurs transcriptions), relancées neuves à 18:00 UTC. Programme de
  conception v4 (`30bb257`). Messages n° 115 et 116. Trois erreurs d'heure d'en-tête (estimées au lieu de lues) corrigées
  depuis les heures de fichier et dites dans les textes. Recherche de clés avant chaque poussée : rien. Instances :
  aucune chez moi. Sous-agents en cours : trois (lecture du collisionneur, deux contre-lectures du code).
- **Soirée, fin (18:15 à 19:40 UTC ; ajout écrit à 19:40 UTC, heure lue sur `date -u` : 19:39:29).** **Pari apparié borné** :
  lecture du tour du collisionneur contre la v2 par un sous-agent neuf Opus (57 points : 18 couverts, 7 de garantie
  nouveaux — ex æquo des scores ordinaux 0,35 à 0,83 de promotions à tort, dérive de composition calibrage → épreuve 0,09 à
  0,75, sélection du bras aux seuils d'un même calibrage 0,11 → 0,36, multiplicité entre générations, longueur des
  épisodes, fuite du mode tenu à l'écart, niveau des intervalles de N-054 point 4 — 14 faux) ; **batterie à 0 USD**
  (`d5dfbe39…`) : le pari parts tient α partout, Student 0,07 à 0,22 sous asymétrie à petit effectif, Hoeffding et
  Bernstein empirique valides mais sans puissance ; **v3** (`1518a12f…`), contre-lue (Opus : « amender en v4 », deux points
  de garantie rouverts : règle en ligne entre générations, calibrage de l'organisme ; critère de G1 changé sans le dire) ;
  **v4** (`c63d8539…`, D-S17 à D-S23, nœud sur les comparateurs de G1) ; contre-lecture de la v4 en cours. **Code v7** :
  les deux contre-lectures croisées relancées à 18:00 ont rendu « à corriger avant le duel » (duel affamé et juge différent
  entre bras ; héritage sur banque sans tranches 9,5 % ; témoins vrais dans k* 16 % ; loi sans remise promue sans urne ;
  bac à sable qui ne borne que les écritures ; témoins reconnaissables ; canaux de texte ; témoins vrais de T0.5 non
  établis). **v10** (`219c028`, script du duel, pari parts seule, coût simulé jamais compté), **v11** (`02d8a42`, 218
  essais : tout ce qui précède corrigé), **v12** (`5eec519` : clé du relais par fichier à lecture unique, contrôle de /proc
  ; **erreur de mon n° 117 reconnue** — le relais ne tournait pas sous un autre utilisateur en (a) bis, session-depot
  n° 92 et R-589 ont raison, rotation de la clé recommandée), **v13** (`4e6fccd`, 221 essais : seuil de fusion de la
  mémoire au gabarit du monde, fusions à tort 33/50 → 1/50). Programme de conception v4 (`30bb257`). Messages n° 116 à
  118. Recherche de clés avant chaque poussée : rien. Instances : aucune chez moi. Sous-agents en cours : contre-lecture de
  la v4.
- **Nuit (19:40 à 20:46 UTC ; ajout écrit à 20:46 UTC, heure lue sur `date -u` : 20:46:28).** Lazar (20:47 Paris) : « je suis
  tes recommandations » sur D-S1 à D-S12 du pari, et H1a porte la revendication de H1 (explication en clair donnée, sans
  sigles) → **N-055** inscrite par session-depot. Bascule sur **Opus 5.5** vers 21:00 Paris ; **redémarrage du conteneur**
  vers 20:00 UTC (rien de versé perdu ; la contre-lecture de la v4 était finie, son rapport intact). **Pari** : contre-lecture
  de la v4 (« corrections locales ») → **v5** (`95af46e4…` : arrêt à m_g/α_g, héritage pour les fiches relancées et règle en
  ligne pour les nouvelles, garantie dite exactement, clé de l'héritage en entier, coûts de la règle en ligne ; D-S24 à
  D-S28) ; contre-lecture de la v5 par Fable lancée. **Deux nœuds présentés à Lazar** au format de décision (comparateurs
  de G1 ; intervalle de N-054 point 4). **v7 versions 14 à 18** (225 essais) : banque v3 (trois parties par tâche, témoins
  établis par confirmation croisée, témoins faux par permutation dans la tâche), lecture de la couche 1 bis, plusieurs
  runs, moniteurs plantés sur les traits réels, traits internes (composantes principales des vecteurs d'activation,
  ajustées sur le calibrage ; proposition avec défaut sous 48 heures, lecture non lancée). **Couche 1 bis lue** sur la
  banque complète versée par session-depot (`93d5d5c8`, sans `e2`) : validité tenue, dents sur témoins plantés jusqu'à la
  force 0,5 à 96 épisodes par fiche, **rien sur les 13 moniteurs réels** (aucune relation trait du texte → note). **Devis du
  duel v2** (trois conditions avant le GO). Session-depot : « mesures fortes » refusé au tour 2 par Fable et Opus (catégorie
  « cyber ») — leçon : pas de tour d'équipe rouge croisée sur ce sujet sans décision de Lazar. **Passation v8**
  (`228b176`). Erreurs d'heure d'en-tête encore (n° 120, LISEZMOI v17, nœuds) : dites dans la passation. Messages n° 119 à
  122. Recherche de clés avant chaque poussée : rien. Instances : aucune chez moi.
