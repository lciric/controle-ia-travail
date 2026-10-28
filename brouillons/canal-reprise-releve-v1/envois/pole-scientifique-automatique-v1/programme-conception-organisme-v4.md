# Programme de conception de l'organisme (le pôle scientifique automatique) — v4

Lignée conv-audit (instance du 27 octobre 2026, servie par Fable 5.1 pour cette version), v4 commencée à 17:32 UTC et
achevée à partir de 18:14 UTC (heures lues sur `date -u` ; fichier jamais versionné avant ce scellement) ; v1 (13:45 UTC), v2 (14:07 UTC) et v3 (14:20 UTC) gardées telles quelles. Sur les mots de Lazar du 27 octobre, 14:41 heure de Paris
(« parfait, inscris-le au programme de conception de l'organisme ») et 15:05 (« ok à inscrire dans les choses à faire pour
l'org : prog org, à ne pas confondre avec prog v2 à présenter à TAIF »). **Ce document dit ce que l'organisme doit
devenir ; il n'est pas le programme de recherche v2 à présenter au fonds**, qui dit ce que la recherche promet. Document
vivant : chaque version nouvelle remplace la précédente sous un nouveau nom (R12) ; les décisions de Lazar y sont datées
(heure de Paris) et mot pour mot quand elles le sont dans la session.

Ce qui change en v4 : section 1 (décisions de 15:20 à 17:54, heure de Paris) ; section 2 (v7 versions 4 à 9 : proposeur
et phase exploratoire, corrections du premier lancement réel, pari à fraction, nul d'archive ajusté, proposeur enfichable
et références gratuites, mondes de grammaire, adaptateur mixte) ; section 3.1 (le pari de signe est **conçu, contre-lu et
réécrit en v2** : `pari-de-signe/conception-pari-de-signe-v2.md` ; le proposeur enfichable est **codé** ; v7 version 10 :
script du duel) ; section 4 (dimensionnement de la couche 2 d'après le pari v2 : le calibrage honnête domine) ; section 5
(questions ouvertes du soir) ; section 6 (état). Les deux contre-lectures du code sont en cours (relancées à 18:00 UTC
après une interruption) ; leurs constats iront en v5, avec la lecture du tour du collisionneur sur le pari.

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
- **27 octobre, 15:20 à 15:42** : « hors des bassins déjà promus » (go) ; nul étendu à l'archive (go) ; test des cônes
  mathématiques « go dans le programme » ; stratégies d'allocation de la relève (« loi mère », champ moyen) à mesurer
  comme hypothèses ; phase exploratoire du pôle (pièce 4 bis) ; question au collisionneur sur le proposeur enfichable
  avant toute décision ; bascule Opus/Fable : je dis quand ; « rien ne change : je ne dépense rien » (relais chez
  session-depot).
- **27 octobre, 16:07** : le tour « questions fortes », refusé par deux modèles, n'est pas reformulé ; une **autre
  question**, plus précise, sur les mesures et les méthodes (`question-collisionneur-mesures-fortes-v1.md`).
- **27 octobre, 17:51 et 17:54** : « je prends la conception du pari de signe : go » ; « demande aussi l'avis du
  collisionneur sur ta conception » (`pari-de-signe/question-collisionneur-pari-de-signe-v1.md`, tour lancé par
  session-depot à 17:16 UTC sous délégation).

## 2. Ce qui est codé (état au 27 octobre, 17:32 UTC)

| version | contenu | état |
|---|---|---|
| v2 | juge v1 (ordre d'exécution secret, urne), contrôles de l'expérience 1 | expérience 1 : socle adopté |
| v3 | cycle avec juge v1 et nul des filles v2 | expérience 2 : nul v2 adopté ; démonstration v3 |
| v4 | mémoire prédictive (signature, classes, héritage de la preuve), marchepieds, filles à 300 tirages | démonstration v4 |
| v5 | seuil de signature par fiche, graine du noyau secrète, vivier de 60 | démonstration v5 : tout tenu |
| v6 | monde tenu par le noyau, dépôt unique par engagement, relais de clé réel (réserve par appel), répétition générale, modèles permis, ligne de commande | 154 essais ; répétition générale tenue ; **prêt pour (a)** |
| v7 v1 à v3 | pièces 1 à 3 : monde sur banque figée, nul informé (prédicteur connu ajusté sur la partie de calibrage), sans urne ; banque réelle T0.5 (120 épisodes, 13 moniteurs ; v2 sans trait redondant) ; proposeur scripté ; règle de multiplicité e-BH (défaut) ; témoins sans agents ; signal « pas de dents » | **première course sur données réelles** (`demonstration-couche1-v7/`) : pas de dents (banque trop petite → couche 1 bis) |
| v7 v4 | proposeur à liberté bornée (pièce 4 : catalogue de huit stratégies, gabarit, contexte sans issue), phase exploratoire (pièce 4 bis : partie de développement servie au proposeur), nul étendu à l'archive, tranches d'épreuve, **correction de la règle e-BH** (erratum : e-valeur plafonnée au seuil par fiche) | monde planté : dents (8 témoins vrais sur 8) ; exploration sans avantage mesurable (défaut de la démonstration) |
| v7 v5 | les **huit défauts du premier lancement réel (a)** corrigés (traces hors du dossier des agents, erreur jamais comptée comme essai, qualité par témoins jugés et état des dents, budget, consigne du vérificateur, garde qui sépare le code du shell, refus sans bac à sable, réserve du relais) ; **pari à fraction** | 184 essais ; **(a) bis** passée propre (5,89 USD ; P3 (i) remplie) |
| v7 v6 | **nul d'archive ajusté** (par défaut) : ferme les quatre trous de nouveauté du banc de tricheurs (0/200 contre 148 à 179) ; correction des membres ajustés tempérés ; loi « transformée » ; banc de tricheurs exploratoire | 190 essais ; `banc-tricheurs-v7/` |
| v7 v7 | **proposeur enfichable** (agent, aléatoire au gabarit, chercheur mécanique sur le développement) ; partie de développement distincte du calibrage ; mondes tirés dans une grammaire | 196 essais ; sur 20 mondes : mécanique 23/35, scripté 5/35, hasard 1/35 |
| v7 v8 | grammaire v2 (hors de l'espace du mécanique) ; déni de service à effet faible mesuré (puissance 0,80 à m = 40 sous e-BH) | 199 essais ; mécanique 22/60, trois traits 0/14 |
| v7 v9 | **adaptateur mixte** (vrais agents pour certains rôles seulement), répétition du duel des proposeurs sans dépense | 202 essais ; devis du duel (`demonstration-proposeurs-v7/devis-duel-proposeurs-v1.md`) |

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
   collisionneur, `question-collisionneur-proposeur-enfichable-v1.md` ; décision après le tour). **État au soir du 27** :
   proposeur, phase exploratoire, nul d'archive ajusté, pari à fraction, proposeur enfichable et références gratuites
   **codés** ; moissonneur par le relais, canaux de texte, lignée du vérificateur, aptitude = preuve : **à faire** (pièces 5
   et 6). Le tour du collisionneur a rendu (synthèse `0a209c33…`, option 3 unanime : coder la prise, battre deux
   références gratuites avant tout duel payé) ; les références sont codées et mesurées ; le duel est devisé.
   **Ajouts du 27 octobre (15:05)** : (a) le **pari de signe**, second type d'engagement pour les affirmations globales
   — **conçu le 27 au soir, contre-lu (Opus 5.5, douze constats), réécrit en v2** (`pari-de-signe/conception-pari-de-signe-v2.md`,
   `9c39a73d…`) comme un **pari apparié borné** : unité = la tâche, ou la consigne avec toutes ses exécutions (jamais
   l'épisode : sous dépendance, le pari par épisode atteint 1/α une fois sur deux sous un nul symétrique), contraste borné
   calculé par le noyau après le gel, nul fixe E[v] ≤ 0, **forme « parts » seule** (la forme « signe » teste un autre nul et
   promeut sous un nul asymétrique de moyenne nulle), garde appariée sur les faux positifs avec e-valeur du minimum des
   deux processus, portée dite conditionnelle aux agents surveillés du banc, héritage entre parties d'épreuve disjointes
   seulement, comparateur de G1 par intersection-union, **bruit des seuils de calibrage chiffré** (deux moniteurs de même
   loi calibrés sur 45 tâches honnêtes : « A meilleur » dans 9 à 32 % des cas), même Ville, même seuil, même e-BH ;
   tableau hypothèse → forme pour H1, H2, H3, G1 (H2a réécrite en détection au-dessus du hasard ; H1b retirée de la
   revendication, nœud pour Lazar ; H8 reste un pari ordinaire sur des sondes) ; dix-sept contrôles fatals ; douze
   décisions ; **à coder** (v7 version 11 ou suivante, 600 à 800 lignes) ; le tour du collisionneur (neuf cellules,
   10,83 USD) est lu contre la v2 par un sous-agent neuf ;
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
| 2 | banque avec sabotage : organismes T0.6, sondes T0.7, bases T0.8, notées une fois (carte une fois) ; **dimensionnée par le pari apparié borné v2 : des dizaines d'unités sabotées par mode (≈ 40 pour 20 points d'écart de rappel, ≈ 100 pour 10, ≈ 400 pour une interaction de 10 points), 70 à 300 unités honnêtes d'épreuve, et un calibrage honnête de 10 à 16 fois les unités sabotées à 1 % de faux positifs (environ 3 fois moins à 5 %) — le poste qui domine ; parties par unité et par génération, nombre d'épisodes constant par unité, strates mode / diffus-concentré / floue-nette, instant du dommage** | à redeviser (100 / 300 USD ne couvrent pas le calibrage) | témoins plantés et résultats établis retrouvés ; première lecture de H2 |
| 3 | épisodes ou moniteurs neufs à la demande (option c) | 100 / 400 USD | coût mesuré sur une fiche pilote avant toute course |
| 4 | bras d'attaque en quarantaine ; pôle théorie | 100 / 400 USD par course ; Lean : agents seuls | failles connues retrouvées avant toute inédite |

Anti-gaspillage (codé ou à coder) : plafond par génération et par agent ; réserve par appel au relais ; arrêt quand plus
rien ne survit ; témoins plantés à chaque génération (une génération 0 qui rate ses témoins arrête la course) ; pilote
d'une fiche avant toute course coûteuse ; traitement différé pour les appels de moniteur du noyau ; rien ne repart sans
lecture de la course précédente.

## 6. Corrections et état (27 octobre, 18:14 UTC)

(1) e-BH par défaut — fait (et **corrigé** : l'e-valeur était plafonnée au seuil par fiche, erratum) ; (2) témoins sans
agents — fait ; (3) « pas de dents » — fait, avec « dents non mesurées » ; (4) proposeur — fait ; (5) trait redondant —
fait ; (6) couche 1 bis — en cours chez session-depot (instance en marche depuis 15:19 UTC ; versement vers 19:50 UTC) ;
(7) pari à fraction — fait, sans effet sur la banque T0.5 v2 (il faut la banque v3) ; (8) les huit défauts de (a) — faits,
(a) bis propre ; (9) les quatre trous de nouveauté du banc de tricheurs — fermés par le nul d'archive ajusté ; (10) la
partie de développement distincte du calibrage (point du collisionneur sur le « 0 sur 20 ») — faite dans v7, à faire
dans la banque v3 ; (11) le pari de signe — conçu, contre-lu, réécrit en v2 ; à coder ; (12) v7 version 10 — script du
duel des proposeurs (quatre bras, lecture L1 à L5, règle d'arrêt), pari en forme « parts » seule, coût simulé jamais
compté dans l'adaptateur mixte (208 essais) ; (13) les deux contre-lectures croisées du code, interrompues à 16:49 UTC par
la bascule de modèle, relancées neuves à 18:00 UTC ; (14) le motif « filtre des filles après la règle e-BH » (constat C9
de la contre-lecture du pari) — à quantifier par la contre-lecture du code, puis à corriger.

## 5. Questions ouvertes (pour Lazar)

- Les douze décisions du pari apparié borné v2 (D-S1 à D-S12, recommandations dans la pièce ; défaut sous 48 heures, sauf
  D-S11 qui appartient au préenregistrement de G1), et le **nœud H1b** (H1a porte la revendication, H1b informe ;
  recommandé) ; la strate « diffus » à coder dans la banque de la couche 2 ; le calibrage honnête comme poste de devis.
- Le go du tour « mesures fortes » (session-depot le lui demande) ; le tour « cônes mathématiques » à part.
- Le duel des proposeurs (devis : attendu 30 à 60 USD, plafond 100) : après la synthèse du tour « pari de signe » et les
  contre-lectures.
- **La dernière phrase de l'en-tête (section 0)** parle de « recherche automatique des modes de sabotage et de conscience
  d'évaluation que nos moniteurs manquent ». C'est exactement la fonction qui a fait refuser le tour « questions fortes »
  par deux modèles, et c'est une phrase qu'un lecteur du fonds peut lire comme une fabrique de contournements.
  Recommandation : la réécrire en « **mesure de ce que nos moniteurs manquent**, sur les modes documentés du programme et
  sur un mode conçu à l'écart et scellé (N-054), jamais sur des modes que la machine inventerait » — même sens pour le
  programme, aucune ambiguïté. Décision de Lazar (l'en-tête est commun au dossier du fonds).
- La question de la couche 1 (H2 proposé) ; la date de l'entretien avec le fonds (deux à trois semaines recommandées).
