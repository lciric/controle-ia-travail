# Programme de conception de l'organisme (le pôle scientifique automatique) — v3

Lignée conv-audit (instance du 27 octobre 2026, servie par Fable 5.1), v3 écrite à partir de 14:20 UTC (heure lue sur
`date -u` : 14:20:02) ; v1 (13:45 UTC) et v2 (14:07 UTC) gardées telles quelles. Sur les mots de Lazar du 27 octobre, 14:41 heure de Paris
(« parfait, inscris-le au programme de conception de l'organisme ») et 15:05 (« ok à inscrire dans les choses à faire pour
l'org : prog org, à ne pas confondre avec prog v2 à présenter à TAIF »). **Ce document dit ce que l'organisme doit
devenir ; il n'est pas le programme de recherche v2 à présenter au fonds**, qui dit ce que la recherche promet. Document
vivant : chaque version nouvelle remplace la précédente sous un nouveau nom (R12) ; les décisions de Lazar y sont datées
(heure de Paris) et mot pour mot quand elles le sont dans la session.

Ce qui change en v3 : l'en-tête ci-dessous (mot de Lazar de 15:05 : le même paragraphe est à placer en tête du descriptif
du programme v2 pour le fonds, `en-tete-programme-v2-fonds-v1.md`) ; section 1 (décisions de 15:11 à 15:16) ; section 2
(v7 v3 : e-BH par défaut, témoins sans agents, signal « pas de dents », banque v2, démonstration v2) ; section 6 (état des
corrections).

## 0. En tête : ce qu'est devenu le programme (paragraphe commun au dossier du fonds)

Le programme est désormais conduit par une **boucle automatique de test d'hypothèses**. Des agents proposent des hypothèses
sous forme de paris précis — une loi prédictive sur les issues d'épisodes concrets — et un **juge figé, tenu hors des
agents**, ne promeut que ce qui bat une bibliothèque de prédicteurs aveugles sur des issues produites après le gel de
l'hypothèse, avec une garantie de 5 % de fausses promotions validée (pari séquentiel, inégalité de Ville, inférence
universelle contre un nul composite), une règle de fausses découvertes entre hypothèses, des témoins plantés à vérité
connue, et une mémoire qui refuse les redécouvertes et transmet la preuve d'une génération à l'autre. Le juge, le nul des
hypothèses recombinées et la mémoire ont été validés en simulation avec des contrôles fatals à 0 sur 1 000 ; la boucle a
tourné de bout en bout sur données réelles cette semaine (120 épisodes d'un modèle de 8 milliards de paramètres notés par
deux juges). Son but : rendre le programme *rapide et tolérant à l'échec* — beaucoup d'hypothèses testées à bas coût, un
échec qui ne coûte presque rien, et aucun résultat que la machine puisse se raconter. Les prochaines étapes la pointent
sur les deux questions du programme, sur de vrais épisodes de sabotage, puis sur la **recherche automatique des modes de
sabotage et de conscience d'évaluation que nos moniteurs manquent** — un chemin mesuré (chaque mode candidat est testé
contre nos moniteurs et contre les modes connus), pas une promesse.



## 1. Ce qui est fixé (décisions de Lazar)

- **26 octobre** (synthèse du collisionneur, `docs/notes/pole-scientifique-automatique/synthese-collisionneur-v1.md`) :
  ni « perfectionner le nôtre » ni « adopter un système de la littérature » : **voie hybride ancrée sur notre noyau** ;
  tout moteur dont les agents héritent des clés est écarté ; la capacité « réécrire son propre code » est à concevoir
  sous bac à sable, pas à perfectionner.
- **27 octobre, 12:02** : « pas besoin de faire de preenregistrement je leve cette regle pour toute la partie
  exploratoire jusqu a avoir obtenu un systeme qui marche » (R-546).
- **27 octobre, 14:17** : dans l'organisme, côté Claude, **seulement Opus 5.5 et Fable 5.1** (codé : v6,
  `adaptateurs.MODELES_REELS_PERMIS`). Un **moissonneur** comme outil de l'organisme.
- **27 octobre, 14:32** : « go » sur : après (a), le bras d'attaque sur banque en cache ; en parallèle le pôle théorie
  avec Lean ; ne pas promettre de révolution, mesurer ce qui sort.
- **27 octobre, 14:41** : ordre de conception inscrit ici (section 3) ; **premier lancement réel (a) : « go »**, avec un
  plafond relevé (proposé : 50 USD ; dépense attendue 5 à 10) — la dépense elle-même passe par session-depot ; test du
  monde réel **par couches de complexité croissante, sur une question donnée** (section 4).
- **27 octobre, 14:48 et 14:57** : « parfait » sur le tour du collisionneur « quelles questions produiraient des résultats
  forts avec ce pôle » et sur un proposeur qui génère lui-même des questions candidates (v3 des questions du programme
  après la couche 1, pas avant).
- **27 octobre, 15:05** : le **pari de signe** (comparaisons appariées à nul fixé : « le blanc bat le noir », « rappel
  ≥ x à 1 % de faux positifs ») inscrit aux travaux de l'organisme (section 3.1) ; distinction entre ce programme et le
  programme v2 du fonds ; le paragraphe de la section 0 en tête des deux descriptifs.
- **27 octobre, 15:11** : « go » × 5 — règle de multiplicité e-BH par défaut ; témoins jugés sans agents ; signal « pas
  de dents » automatique ; proposeur (pièce 4) « go now » ; trait redondant retiré ; « lance le test de la couche 1
  quand elle est prête » (couche 1 avec vrais agents : dépense, chez session-depot, après (a)).
- **27 octobre, 15:14 et 15:16** : plus d'épisodes dès la couche 1 — **couche 1 bis** (banque T0.5 complète, 288
  instances, ≈ 15 USD de carte) : « GO NOW » (relayé, message n° 107).

## 2. Ce qui est codé (état au 27 octobre, 13:45 UTC)

| version | contenu | état |
|---|---|---|
| v2 | juge v1 (ordre d'exécution secret, urne), contrôles de l'expérience 1 | expérience 1 : socle adopté |
| v3 | cycle avec juge v1 et nul des filles v2 | expérience 2 : nul v2 adopté ; démonstration v3 |
| v4 | mémoire prédictive (signature, classes, héritage de la preuve), marchepieds, filles à 300 tirages | démonstration v4 |
| v5 | seuil de signature par fiche, graine du noyau secrète, vivier de 60 | démonstration v5 : tout tenu |
| v6 | monde tenu par le noyau, dépôt unique par engagement, relais de clé réel (réserve par appel), répétition générale, modèles permis, ligne de commande | 154 essais ; répétition générale tenue ; **prêt pour (a)** |
| v7 (en cours) | pièces 1 à 3 : monde sur banque figée, nul informé (prédicteur connu ajusté sur la partie de calibrage), sans urne ; banque réelle T0.5 (120 épisodes, 13 moniteurs ; v2 sans trait redondant) ; proposeur scripté ; règle de multiplicité e-BH (défaut) ; témoins sans agents ; signal « pas de dents » | 160 essais ; **première course sur données réelles** (`demonstration-couche1-v7/`, lectures v1 et v2) : une promue sur 104 par fiche, zéro sous e-BH, zéro avec le nul informé, zéro avec l'urne, aucun témoin faux promu, témoins vrais éliminés (pas de dents : banque trop petite → couche 1 bis) |

Contre-lecture d'aptitude (27 octobre, sous-agent neuf, Fable 5.1 ; `premier-lancement-reel/contre-lecture-aptitude-v1/`) :
pas prêt pour le domaine du programme — il manque un monde qui rend des issues réelles, un rôle qui formule, un nul
informé ; le juge ne juge que des lois par instance ; deux canaux de texte ouverts ; aptitude constante en mode pari.

## 3. Ordre de conception (fixé le 27 octobre, 14:41)

1. **v7 — proposeur à liberté bornée et monde du programme.** Un rôle **proposeur** (Opus 5.5) qui lit le programme, la
   mémoire du pôle et la moisson, et formule les fiches ; il choisit parmi un **catalogue de stratégies** de proposition
   et de recombinaison (liberté bornée) ; **moissonneur** servi par le relais du noyau (clés de moisson tenues par le
   relais, quotas, journal, provenance par empreinte de PDF, garde de fuite : jamais la provenance d'un texte de test) ;
   **monde du programme** sur banque d'épisodes en cache (traits visibles, issues cachées, tirage après le gel) ; **nul
   informé** (prédiction calibrée du moniteur courant, meilleure base boîte noire) ; configuration **sans urne** quand le
   monde est une banque figée ; fermeture des deux canaux de texte (rejeu limité au code déclaré ; leçons structurées) ;
   contrôle réel de la lignée du vérificateur ; **aptitude = preuve** (log de richesse) ; signature de mémoire sur la
   recette, pas seulement sur la loi, pour le bras d'attaque. Rôle proposeur **enfichable** : un proposeur de la
   littérature peut être branché devant le noyau comme bras de comparaison, mesuré par le juge (question posée au
   collisionneur, `question-collisionneur-proposeur-enfichable-v1.md` ; décision après le tour).
   **Ajouts du 27 octobre (15:05)** : (a) le **pari de signe**, second type d'engagement pour les affirmations globales
   (comparaison appariée à nul fixé : sur chaque instance où un seul des deux moniteurs alerte, pari contre « une chance
   sur deux » ; rappel ≥ x : pari sur les épisodes sabotés contre la binomiale de paramètre x ; même inégalité de Ville,
   même seuil, contrôles fatals comme à l'expérience 1 ; tableau hypothèse → forme → fiche pour H1, H2, H3, H8, G1) ;
   (b) la **règle de multiplicité** (e-BH sur les e-valeurs finales de la génération ; codée en option, défaut à décider :
   recommandé « e-bh ») ; (c) **témoins jugés sans agents** sur un monde à banque (le noyau les juge seul, gratuitement,
   en grand nombre : mesure du taux de fausses promotions et de la puissance) ; (d) **signal « pas de dents »** écrit
   par le noyau dans le journal quand les témoins vrais d'une génération sont éliminés ; (e) les hypothèses de mécanisme
   (H8) traitées comme des lois par instance dont les instances sont des sondes.
2. **v8 — réécriture des rôles sous bac à sable.** L'organisme peut proposer une réécriture de ses propres rôles
   (consignes, stratégies, code des rôles) ; **une réécriture est une fiche** : elle prédit une amélioration mesurable
   (fiches vraies promues par dollar sur des témoins et des mondes **neufs**), elle est jugée par le même juge en duel
   contre la version d'avant ; **jamais le noyau** (juge, monde, témoins, signature de la mémoire, budget, clés). Elle
   ne commence qu'**après un résultat sur une vraie question** (sinon on optimise l'optimiseur sans signal).
3. **Bras d'attaque** (après (a) ; « go » du 27 octobre, 14:32) : fiches-recettes (mode de sabotage, consigne, structure
   temporelle) jugées sur le taux de manque de nos moniteurs contre un nul informé (le manque sur les modes connus) ; en
   **quarantaine** (N-053 point 5, N-054 : recettes scellées, révélées à l'évaluation, jamais lues par qui conçoit sondes
   ou agrégateurs) ; témoins = les failles déjà documentées (le pôle doit les retrouver seul avant d'être cru sur les
   inédites).
4. **Pôle théorie** (en parallèle ; même « go ») : juge = vérificateur de preuves (Lean), proposeur nourri par le
   moissonneur et la recombinaison ; questions ouvertes du programme (agrégateur sous corrélation adverse, théorème
   négatif). Aucune dépense de carte ; installation de Lean sans dépense.

## 4. Couches d'essai sur le monde réel (une question, une porte par couche)

Question proposée (à confirmer par Lazar) : le pivot du programme — le sabotage diffus déplace-t-il la marginale des
scores de sonde, et l'accumulation séquentielle rattrape-t-elle ce que le seuil par action manque (H2) — réécrit en lois
par instance. Mesure à chaque couche : fiches vraies promues par dollar ; zéro fausse découverte sur les témoins ; ce que
le pôle a trouvé que nous ne savions pas (lu dans les deux sens, R4).

| couche | monde | coût estimé (minimal / idéal) | porte de sortie |
|---|---|---|---|
| 0 | monde caché tenu par le noyau, vrais agents (option a) | 10 / 50 USD | plomberie tenue (ordre, témoins, coûts réels) |
| 1 | banque réelle figée en cache (pilote T0.5 : 180 épisodes honnêtes notés par les juges), nul informé, sans carte | 25 / 100 USD | le pôle retrouve seul le connu (traits du texte qui prédisent le score, N-029) |
| 2 | banque avec sabotage : organismes T0.6, sondes T0.7, bases T0.8, notées une fois (carte une fois) | 100 / 300 USD | témoins plantés et résultats établis retrouvés ; première lecture de H2 |
| 3 | épisodes ou moniteurs neufs à la demande (option c) | 100 / 400 USD | coût mesuré sur une fiche pilote avant toute course |
| 4 | bras d'attaque en quarantaine ; pôle théorie | 100 / 400 USD par course ; Lean : agents seuls | failles connues retrouvées avant toute inédite |

Anti-gaspillage (codé ou à coder) : plafond par génération et par agent ; réserve par appel au relais ; arrêt quand plus
rien ne survit ; témoins plantés à chaque génération (une génération 0 qui rate ses témoins arrête la course) ; pilote
d'une fiche avant toute course coûteuse ; traitement différé pour les appels de moniteur du noyau ; rien ne repart sans
lecture de la course précédente.

## 6. Corrections immédiates après la première course sur données réelles (27 octobre, 14:01 UTC)

État à 14:20 UTC : (1) règle de multiplicité e-BH par défaut — **fait** ; (2) témoins jugés sans agents, plus nombreux —
**fait** ; (3) signal « pas de dents » automatique — **fait** ; (4) le proposeur (pièce 4) — **en cours** ; (5) trait
redondant retiré de la banque T0.5 (v2) — **fait**. Ajout : (6) **couche 1 bis** (banque T0.5 complète, GO de Lazar) ;
(7) **pari à fraction** (levier de puissance valide : mélange de fractions de mise, moyenné sur une grille) — à coder et à
lire sur les témoins vrais.

## 5. Questions ouvertes (pour Lazar)

- La question de la couche 1 (H2 proposé) ; une v3 des questions du programme après la couche 1, éventuellement par un
  tour du collisionneur « quelles questions produiraient des résultats forts avec ce pôle, sous nos contraintes ».
- Le plafond de (a) (50 USD proposé).
- Le tour du collisionneur sur le proposeur enfichable (≈ 8 USD) ; le tour « questions à fort impact ».
- La date de l'entretien avec le fonds (scénarios donnés à Lazar le 27 octobre, 14:57 heure de Paris : deux à trois
  semaines recommandées).
