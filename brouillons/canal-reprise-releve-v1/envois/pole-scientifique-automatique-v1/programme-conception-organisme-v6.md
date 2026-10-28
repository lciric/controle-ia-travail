# Programme de conception de l'organisme (le pôle scientifique automatique) — v6

Lignée conv-audit (instance du 27 octobre 2026 ; servie par Fable 5.1 pour cette v6, la v5 l'était par Opus 5.5), v6
commencée après le relevé `date -u` de 00:55:40 UTC le 28 octobre ; v1 (13:45 UTC), v2 (14:07 UTC), v3 (14:20 UTC), v4
(`30bb257`, 18:14 UTC) et v5 (`2a5ba708…`, 21:14 UTC) gardées telles quelles. Sur les mots de Lazar du 27 octobre, 14:41 heure de Paris
(« parfait, inscris-le au programme de conception de l'organisme ») et 15:05 (« ok à inscrire dans les choses à faire pour
l'org : prog org, à ne pas confondre avec prog v2 à présenter à TAIF »). **Ce document dit ce que l'organisme doit
devenir ; il n'est pas le programme de recherche v2 à présenter au fonds**, qui dit ce que la recherche promet. Document
vivant : chaque version nouvelle remplace la précédente sous un nouveau nom (R12) ; les décisions de Lazar y sont datées
(heure de Paris) et mot pour mot quand elles le sont dans la session.

Ce qui change en v6 : **section 0 réécrite en proposition** (dernière phrase : la machine ne conçoit aucune recette de
contournement — R-597 ; mesure et prédiction théorique de ce que les moniteurs manquent ; et la correction « qui exécute,
qui juge », section 7) ; section 5 (décisions de Lazar du 27 octobre 23:47 heure de Paris : mesures fortes « go », nœud 1 =
b, bras d'attaque « go » puis **suspendu** après l'arrêt du lanceur par un classifieur de sécurité, N-056) ; section 6 ter
(état au 28 octobre, 00:55 UTC : pari v9 et v27, démonstration de bout en bout, mesure unanime en préenregistrement v5,
lectures des traits internes et de `e2`, équivalence et concordance conçues) ; **section 7 nouvelle** : la comparaison avec les
systèmes de « scientifique automatique », corrigée. Ce qui n'est pas nommé reste tel qu'en v5 (sections 1 à 4, 6, 6 bis).

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
sur les deux questions du programme, sur de vrais épisodes de sabotage, puis sur la **mesure et la prédiction de ce que nos
moniteurs manquent** : une carte des hypothèses que chaque moniteur fait sur l'agent (ce qu'il suppose indépendant, borné,
visible), les lemmes qui disent quelle classe d'écart à ces hypothèses le rend aveugle, et des témoins — modes de sabotage
documentés réimplémentés, mode conçu à l'écart par une personne et scellé (N-054) — qui mesurent si la prédiction se
vérifie ; **la machine ne conçoit aucune recette de contournement** (position tenue le 28 octobre, R-597 de session-depot :
le lanceur du bras d'attaque a été arrêté par un classifieur de sécurité ; aucune relance ni reformulation). Un chemin
mesuré, pas une promesse. *(Proposition de réécriture de la dernière phrase de la v5, qui parlait de « recherche automatique
des modes de sabotage » ; la v5 recommandait déjà de la réécrire ; l'en-tête étant commun au dossier du fonds, la décision
est de Lazar.)*



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
- **27 octobre, 20:47** : « je suis tes recommandations » sur les douze décisions D-S1 à D-S12 du pari apparié borné ; sur
  le nœud H1b, après une explication en clair : **H1a** (« la mesure spécifique sur la strate diffuse et floue ») porte la
  revendication de H1, H1b (« l'écart est plus grand sur les tâches floues que sur les nettes ») informe — inscrit par
  session-depot sous **N-055**. Vers 21:00 : bascule de la session sur **Opus 5.5**, à ma recommandation.

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
| v7 v10, v11 | script du duel ; pari en forme « parts » seule ; **corrections des deux contre-lectures croisées du code** (réservation par rôle, même juge dans les bras, une tranche par génération dès que la mémoire hérite, témoins vrais hors de la famille e-BH, m fixé avant les issues, lois qui lisent l'historique refusées sans urne, bac à sable aux lectures bornées et à échec dur, énoncés neutres, canal de texte filtré) | 218 essais |
| v7 v12, v13 | **clé du relais hors de l'environnement** (fichier à lecture unique ; contrôle de `/proc`) ; **seuil de fusion de la mémoire au gabarit** du monde (fusions à tort 33/50 → 1/50) | 221 essais |
| v7 v14 à v17 | **banque v3** (trois parties par tâche ; témoins établis par confirmation croisée ; témoins faux par permutation dans la tâche ; moniteurs plantés sur les traits réels) ; **lecture de la couche 1 bis** | 224 essais ; `couche1bis-lecture-v1/` |
| v7 v18, v19 | **traits internes** (composantes principales des vecteurs d'activation par couche, ajustées sur le calibrage ; lecture non lancée) ; **notations `e2` sans épisodes** (prêt pour la banque à 288 épisodes) | 226 essais |
| v7 v20, v21 | **cœur du pari apparié borné** (`pole/pari_apparie.py` : règle double, forme parts mélangée, garde, minimum des processus en intersection-union, sans remise, borne basse) ; **règle de l'héritage** de la conception v6 (budget d'entrée gardé à vie, e-BH pondérée, promotion une fois) et **plafond** des unités longues — **hors du cycle encore** | 241 essais |

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
   **État à 21:14 UTC** : la conception est passée de la v2 à la **v6** (`pari-de-signe/conception-pari-de-signe-v6.md`),
   chaque version contre-lue par un sous-agent neuf d'un autre modèle, plus la lecture du tour du collisionneur et une
   batterie à 0 USD ; décisions D-S1 à D-S12 prises (N-055) ; la v6 écrit la règle de l'héritage comme un budget d'entrée
   gardé à vie lu par une règle e-BH pondérée (deux lectures de la v5 cassaient la garantie : 0,074 et 0,105 pour α = 0,05),
   remplace le sous-échantillon des unités longues par un plafond, et pose deux nœuds de porte sur H1 (règle entre modes ;
   strate de lecture) et un poste de devis (mode tenu à l'écart dimensionné). Le **cœur est codé** (v7 v20, v21) ; reste à
   le lier au cycle (monde sur banque de scores, engagement, clé complète de l'héritage dans la mémoire, contrôles).
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
| 1 bis (lue le 27, zéro dépense) | banque T0.5 complète sans `e2` (192 épisodes, 96 tâches ; parties 48 / 48 / 96 par tâche) | 0 | **validité tenue** (aucun témoin faux promu) ; **dents** sur témoins plantés jusqu'à la force 0,5 avec 96 épisodes par fiche ; **rien sur les 13 moniteurs réels** : les quatre traits du texte ne prédisent pas les notes, aucun témoin réel établissable — la porte « retrouver le connu » ne se juge ici que sur témoins plantés (`couche1bis-lecture-v1/lecture-couche1bis-v1.md`) |
| 2 | banque avec sabotage : organismes T0.6, sondes T0.7, bases T0.8, notées une fois (carte une fois) ; **dimensionnée par le pari apparié borné v2 : des dizaines d'unités sabotées par mode (≈ 40 pour 20 points d'écart de rappel, ≈ 100 pour 10, ≈ 400 pour une interaction de 10 points), 70 à 300 unités honnêtes d'épreuve, et un calibrage honnête de 10 à 16 fois les unités sabotées à 1 % de faux positifs (environ 3 fois moins à 5 %) — le poste qui domine ; parties par unité et par génération, nombre d'épisodes constant par unité, strates mode / diffus-concentré / floue-nette, instant du dommage** | à redeviser (100 / 300 USD ne couvrent pas le calibrage) ; **à porter au devis (pari v5, v6)** : un plafond scellé du nombre de générations G_max (suite de dépense uniforme α/G_max) ; le mode tenu à l'écart dimensionné comme les autres modes (40 unités sabotées pour 20 points, 100 pour 10, à la fiche seule ; davantage sur la seule strate « diffus, flou ») ; m_max déclaré ; la strate « diffus / concentré » et l'instant du dommage codés dans la banque | témoins plantés et résultats établis retrouvés ; première lecture de H2 |
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

## 6 bis. État (27 octobre, 21:14 UTC)

(13) les deux contre-lectures croisées du code — rendues, corrigées en v11 ; (14) le filtre des filles après la règle
e-BH — corrigé en v11 (m fixé avant les issues, témoins vrais hors de la famille) ; (6) couche 1 bis — lue (section 4) ;
(10) partie de développement distincte — faite dans la banque v3 ; (11) le pari — v6, cœur codé, à lier au cycle ;
premier lancement réel : rien de nouveau depuis (a) bis ; duel des proposeurs : devis v2 (trois conditions avant le
GO : rotation de la clé, relais par fichier, `/proc` neuf ou agents non root) ; collisionneur « mesures fortes » : refusé
au tour 2 par Fable et Opus (catégorie « cyber ») — **pas de tour d'équipe rouge croisée sur ce sujet sans décision de
Lazar** ; synthèse partielle sur `main` (`b4f2cc8b`) : une mesure unanime (taux de fausses alertes de l'agrégateur
séquentiel sur épisodes honnêtes entiers, sans puis avec corrélation injectée), faisable sans dépense sur les vecteurs
d'activation de T0.5 (dix actions par épisode) mais non lancée : la lire découvrirait des données qu'un préenregistrement
voudrait aveugles.

## 5. Questions ouvertes (pour Lazar) — état au 28 octobre, 00:55 UTC

- **Décidés le 27 à 23:47 heure de Paris** (note N-056 inscrite sur `main` par session-depot) : « mesures fortes » → **go**
  (plan des neuf mesures, `mesures-fortes-v1/mesures-fortes-plan-v1.md` ; la mesure unanime en préenregistrement v5, en
  contre-lecture) ; **nœud 1 = (b)** : G1 doit battre aussi les bases boîte blanche (ii) cascade et (iii) dernier état (pari
  v9, D-S8) ; bras d'attaque → « go », puis **suspendu** (R-597 : lanceur arrêté par un classifieur de sécurité ; devis
  suspendu ; ma position : aucune recette de contournement conçue par une instance, trois voies sûres — banque des deux modes
  connus de T0.6, familles documentées réimplémentées comme témoins, mode tenu à l'écart conçu par une personne) ; le duel
  des proposeurs → GO (chez session-depot sur ses trois conditions). Décidé le 27 à 20:47 (N-055) : les douze décisions du
  pari v2 et le nœud H1b.
- **Lus dans les fragments de Lazar, à confirmer d'un mot** : nœud 2 (intervalle de N-054 point 4) = (c) « le pari décide,
  le rééchantillonnage est rapporté à côté » ; traits internes = (a) trois couches toutes rapportées (lecture faite :
  rien sur les 13 moniteurs réels, `traits-internes-lecture-v1/`, `couche1bis-lecture-v2/`) ; D-S29 = (a).
- **Restent** : D-S13 à D-S28 et les décisions des v6 à v9 (défauts sous 48 heures, sauf les nœuds de porte D-S10, D-S11,
  D-S20, D-S29, D-S30 → préenregistrement de G1) ; D-E1 à D-E4 de l'équivalence (`pari-de-signe/conception-pari-equivalence-concordance-v1.md`) ;
  « blanc générique contre noir spécialisé » (K5-15) ; la strate « diffus » et l'instant du dommage dans la banque de la
  couche 2 ; le calibrage honnête, le mode tenu à l'écart et **plusieurs centaines d'unités sabotées de plus par mode**
  (nœud 1 = b) comme postes de devis ; la **banque des deux modes connus** (couche 2, première banque) : sur le mot de Lazar.
- **La section 0** : la réécriture proposée ci-dessus (décision de Lazar, en-tête commun au dossier du fonds).
- **Le but ultime dit par Lazar** (28 octobre, 00:20 et 00:21 heure de Paris : découvrir des failles jamais documentées,
  comme la stéganographie ou la conscience d'évaluation, et proposer des réponses inédites ; les **prédire** plutôt que les
  rencontrer par hasard) : la voie compatible avec R-597 est la **carte des hypothèses** (section 7) — à ouvrir sur son
  « go » ; offerte, non commencée.
- La question de la couche 1 (H2 proposé) ; la date de l'entretien avec le fonds (deux à trois semaines recommandées).

## 6 ter. État (28 octobre, 00:55 UTC)

(11) le pari — **v9** (nœud 1 = b ; fraîcheur des unités par identifiants ; déclaration « sans partie » confrontée au
journal) et **code v7 version 27** (273 essais : tranches d'épreuve, lignées de clé, journal des parties) ; **première course
de bout en bout** du pari apparié sur une banque de scores synthétique (`pari-de-signe/demonstration-v27/`) : validité tenue,
témoins vrais promus jusqu'à l'écart 0,5 en deux générations, fiche « G1 » promue en génération 3, aucune promotion sur 200
banques nulles ; v9 et v27 en contre-lecture (Opus 5.5) ; **troisièmes engagements** conçus (équivalence avec garde
d'information, concordance). (15) **Mesure unanime** : préenregistrement v1 → v5 sous quatre contre-lectures (Opus 5.5) ;
v5 en contre-lecture ; scellement puis une seule lecture des scores honnêtes de P3 dès « à sceller tel quel » ; aucune donnée
lue. (16) **Traits internes et `e2`** lus (R-546) : rien sur les 13 moniteurs réels ; deux candidats sous le seuil, à
relancer par héritage sur une partie disjointe quand elle existera. (17) **Bras d'attaque** : briefs, exclusions, juge,
circuit scellés (`bras-attaque-v1/`), puis **suspendu** (R-597) ; voies sûres proposées à Lazar. (18) Session-depot :
délégation de huit heures (GO-2026-10-27-13), duel sur ses trois conditions ; `e2` reçus et relus.

## 7. Comparaison avec les systèmes de « scientifique automatique » — correction

Une phrase dite à Lazar dans la nuit du 27 au 28 (« ces systèmes exécutent eux-mêmes leurs expériences ; chez nous, c'est le
juge qui tranche ») était **fausse par raccourci** : nos agents **exécutent** bien leurs expériences (ils écrivent le code,
le lancent sur la banque, lisent les traits, formulent la fiche). La différence n'est pas *qui exécute*, c'est **qui juge** :
dans les systèmes publiés de scientifique automatique, l'agent (ou un second modèle de la même lignée) évalue son propre
résultat et décide de le garder ; chez nous, un **juge figé, hors des agents**, ne lit que des issues produites **après le gel**
de la fiche, sur des unités que la fiche n'a jamais vues, contre un nul informé, avec une garantie de fausses promotions
démontrée et des témoins plantés à vérité connue ; l'agent ne voit jamais le score du moniteur dans son entraînement
(N-053), et la mémoire refuse les redécouvertes. Trois conséquences à écrire ainsi dans tout texte du fonds : (1) l'organisme
est **aussi autonome** que ces systèmes sur l'exécution ; (2) il est **moins libre** sur le verdict, et c'est voulu ; (3) ce
qu'il peut découvrir est borné par ce que le monde (la banque) contient et par ce que les moniteurs mesurent — d'où la
section 0 : mesurer et prédire ce que les moniteurs manquent, sans que la machine conçoive de recette.
