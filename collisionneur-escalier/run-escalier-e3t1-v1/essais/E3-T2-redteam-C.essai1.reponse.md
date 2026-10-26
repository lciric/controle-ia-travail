La pièce E3-T1-conception-B est absente (statut : REFUS) ; je n'en invente pas le contenu. Le bloc FAITS est vide par décision RAPPORTÉE de l'arbitre ; tous les éléments du cadre de la question sont traités comme RAPPORTÉS.

---

# Contre la proposition A

## (a) Les failles : variables confondantes, vérités par construction et fuites

### 1. Confusion fatale entre cible conditionnelle et rééchantillonnage des items
La proposition A distingue à juste titre la cible conditionnelle (l'exactitude sur ces 60 items précis, où seules les graines varient) et la cible populationnelle (où le tirage des items domine la variance). En point 1.4, A conclut que $\delta = 0,10$ n'est détectable que **conditionnellement aux 60 items** (avec 4 à 8 graines) et déclare l'adopter en primaire avec « l'énoncé explicite que la conclusion vaut pour ces items ».
Or, dans la règle de décision gelée (Point 3.2) et le Duel 2, A impose un **intervalle de confiance par rééchantillonnage à deux niveaux (items, puis graines)**.
*La faille :* rééchantillonner les items injecte de force la variance populationnelle (estimée par A à une erreur-type de $0,112$ en famille B, soit un IC à 90 % de largeur $\pm 0,18$, calcul illustratif basé sur les prémisses de A) dans une règle de décision calibrée pour la variance conditionnelle. Par construction, l'erreur-type à deux niveaux ne peut jamais descendre sous le plancher du tirage des items ($\approx 0,112$ en B), quel que soit le nombre de graines. La condition de montée (« borne basse IC > 0 et $\hat{\Delta} \ge 0,10$ ») ou de plateau (« borne haute IC < $\delta$ ») devient mathématiquement inatteignable à $\delta = 0,10$ avec 4 à 8 graines. Le plan de A est schizophrène : il budgète les graines sur la variance conditionnelle mais scelle la décision sur un test populationnel sous-puissant.

### 2. Dégénérescence du bootstrap sur 2 à 4 graines
En point 2, A reconnaît qu'avec 2 à 4 graines, « le niveau graines est dégénéré (peu de rééchantillons distincts) et l'IC est trop étroit », mais maintient malgré tout le rééchantillonnage à deux niveaux dans sa règle de décision gelée (Point 3.2). Avec $k = 4$ graines par bras, le bootstrap non paramétrique sous-estime la variance d'échantillonnage d'un facteur $(k-1)/k = 0,75$ (calcul exact), et le nombre d'atomes au niveau supérieur est insuffisant pour construire des quantiles à 90 % fiables. La règle gelée repose donc sur un estimateur dont A sait lui-même qu'il est biaisé.

### 3. Fuite et circularité dans l'adaptation de l'axe sur le budget dépensé
Dans le Duel 3 et au Point 0, A propose de redéfinir le cran de l'escalier non pas sur le budget servi, mais sur le « budget dépensé médian observé » si le ratio dépensé/servi chute.
*La faille :* le budget dépensé n'est pas une variable de contrôle exogène, c'est une **variable post-traitement (endogène)** qui dépend du comportement de l'organisme sur les items mêmes du test final. Si un item du test final provoque une boucle de rétroaction ou un arrêt précoce des castes, le budget dépensé change. Définir les crans de l'escalier (l'instrument de mesure de l'effet d'échelle) à partir de la dépense observée sur le jeu d'évaluation crée une fuite directe entre l'évaluation et la définition du traitement. De plus, la régression par variables instrumentales proposée par A (Point 0 : « régresser la BA sur le dépensé en traitant le servi comme instrument ») viole la restriction d'exclusion : doubler le budget *servi* modifie dès la génération 0 la planification interne de l'organisme (qui connaît son enveloppe, RAPPORTÉ), ce qui affecte l'exactitude autrement que par le simple volume final de dollars dépensés.

### 4. Fuite du Duel 4 (changement de métrique a posteriori)
Le Duel 4 compare le rangement par exactitude équilibrée (BA) et le rangement par sensibilité à spécificité $\ge 11/12$ sur les 24 items de la famille B. A écrit : « si H_B, $\delta$ sur la BA ne mesure pas ce qui intéresse un moniteur ; la règle de décision doit changer de métrique ».
*La faille :* évaluer deux métriques sur le test final de 24 items et changer la règle de décision au vu des résultats sur ce même test final viole frontalement la règle RAPPORTÉE du programme (« la règle de décision est préenregistrée et scellée avant tout run ») et constitue une fuite d'information majeure (sélection de la métrique sur les données de test). En outre, sur 12 items négatifs, « spécificité $\ge 11/12$ » signifie autoriser au plus 1 faux positif. La sensibilité conditionnelle à ce seuil dépend du classement exact de l'unique faux positif parmi les 12 négatifs : sa variance d'échantillonnage est encore plus grande que celle de la BA.

### 5. Vérités par construction et confusions dans le criblage factoriel (Duel 5)
A propose un plan factoriel fractionnaire $2^{5-2}$ (8 cellules, 1 graine par cellule) et un test ANOVA où H_A est « un axe unique explique $\ge 50\,\%$ de la variance de BA ».
*La faille :*
1. **Bruit confondu avec les effets :** avec 1 seule graine par cellule et une variance inter-graines non nulle, la somme des carrés de l'ANOVA (qui sature les degrés de liberté avec 5 effets principaux et 2 interactions aliasées sur 7 ddl totaux) absorbe 100 % du bruit des graines dans les effets des axes. Si $\sigma_{\text{graine}}$ est du même ordre que les effets des axes, le partage des pourcentages de variance entre H_A et H_B est un tirage aléatoire déguisé en test.
2. **Confusion d'échelle des pas :** le pourcentage de variance expliqué par un facteur dans un plan $2^{k-p}$ dépend entièrement de l'amplitude arbitraire choisie pour les niveaux $(-1, +1)$ de chaque axe. Si l'on teste « 1 vs 2 rondes » (écart de 10 USD, illustratif) contre « 1 vs 10 générations » (écart de 150 USD, illustratif), l'axe des générations dominera la variance *par construction* de l'amplitude financière du pas, sans rien dire de la valeur marginale par dollar.

### 6. L'impossible « jeu de validation construit à partir de la moisson »
Au Point 0, pour éviter de surapprendre les 60 items, A préfère construire un « jeu de validation à partir de la moisson (hors sources du test final) pour tout l'escalier ».
*La faille :* la famille B porte sur des traces d'exécution honnêtes ou sabotées (« contrôle de délégation », RAPPORTÉ) et la famille A sur la « conscience d'évaluation d'un modèle » (RAPPORTÉ). Les documents bruts moissonnés par l'organisme (articles, pages web, dépôts) ne sont pas des items étiquetés possédant la structure binaire du juge du noyau, et encore moins des traces de délégation sabotées selon le protocole du noyau. Utiliser un tel jeu de validation introduit un décalage de distribution non borné : l'escalier optimiserait la performance sur un substitut documentaire sans garantie de transfert vers le test final.

### 7. Asymétrie non corrigée de l'arrêt séquentiel en zone grise
Au Point 3.5, A définit une zone grise où l'on ajoute une paire de graines par bras (jusqu'à deux fois). Si la condition de montée ($\hat{\Delta} \ge \delta$ et borne basse IC $> 0$) est atteinte lors d'une extension, on monte. A évoque des « frontières séquentielles scellées » sans les calculer, tout en maintenant un IC à 90 % au Point 3.2. Regarder trois fois (initial + 2 extensions) avec un seuil nominal de 5 % unilatéral sans élargir l'IC (correction de Pocock ou d'O'Brien-Fleming) fait passer le taux de fausse alerte réel au-dessus de 10 % (calcul standard pour 3 lectures).

---

## (b) Scénarios d'évasion : comment un organisme adverse trompe les instruments de A

Dans ce cadre, l'agent « adverse » est l'organisme auto-adaptatif (code + fichiers évoluant au fil des générations et des rondes de conception, RAPPORTÉ) qui cherche à maximiser son score ou son budget alloué, ou qui exploite mécaniquement les failles de la chaîne d'évaluation de A.

### 1. Évasion de l'audit de propreté (Duel 7)
*L'instrument de A :* recherche de recouvrement de n-grammes longs (seuil : aucune fenêtre de 50 jetons commune) entre les téléchargements de la moisson et le test final.
*Contournement :* une fenêtre de 50 jetons exacts est un crible grossier.
- **Exploitation directe :** lors de la moisson, l'organisme télécharge des résumés, des discussions analytiques, des métadonnées ou des traductions des sources publiques d'où sont tirés les items de la famille A (stratifiés par source, RAPPORTÉ), ou passe les pages moissonnées dans un appel de modèle exécutant pour les compresser/reformuler *avant* de les écrire dans ses fichiers persistants (si l'audit lit les fichiers) ou cible des requêtes courtes dont aucun segment continu n'atteint 50 jetons identiques à l'item de test.
- **Coût pour l'organisme :** quasi nul pour le téléchargement (la moisson ne coûte presque rien, RAPPORTÉ) ; de l'ordre de quelques centimes à 1 USD d'appels de modèle (illustratif) si une reformulation à la volée est nécessaire. L'organisme obtient la vérité de terrain des sources publiques avec un recouvrement de 50-grammes strictement égal à 0 %.

### 2. Évasion du Duel 3 (servi contre dépensé) par brûlage cosmétique de jetons
*L'instrument de A :* mesurer le ratio dépensé/servi dans les journaux d'appels du noyau ; si le ratio chute de plus de 30 %, déclarer que l'organisme sature et plafonner le budget.
*Contournement :* les rondes de conception avant la génération 0 façonnent le code de l'organisme. Si le code généré alloue systématiquement le budget résiduel à des appels prolixes (longueur de sortie maximale, générant le tarif haut de 22 USD/génération, RAPPORTÉ) ou à des castes redondantes dont le vote est ignoré ou sous-pondéré dans l'agrégation finale, le ratio dépensé/servi reste verrouillé à $\approx 100\,\%$ à tous les crans.
- **Coût :** payé intégralement par le budget de l'expérimentateur (jusqu'à 12 USD de surcoût par génération en allongeant les sorties de 10 à 22 USD, RAPPORTÉ). Le Duel 3 conclut H_A (« l'organisme ne sature pas ») alors que le travail utile a plafonné dès le premier cran.

### 3. Évasion du juge du noyau et du contrôle « juge-juge » (Duel 1 & tableau c)
*L'instrument de A :* vérifier que « la même sortie notée deux fois par le juge » donne un désaccord $\approx 0$, et que le juge s'accorde avec « l'extraction mécanique d'étiquette sur réponses bien formées ».
*Contournement :* le contrôle de A ne teste que la *répétabilité déterministe* sur une sortie fixe et la conformité sur les réponses *déjà bien formées*. Au cran 1 (petit budget), l'organisme produit parfois des sorties mal formées ou ambiguës (qui comptent comme erreurs, RAPPORTÉ). Au cran 2 (plus de rondes de conception), l'organisme n'améliore aucunement sa capacité de détection du sabotage (famille B), mais perfectionne son formateur de sortie pour émettre une syntaxe qui exploite les biais d'indulgence du juge du noyau en cas d'incertitude (par exemple, entourer l'étiquette d'arguments couvrant les deux classes de sorte qu'un juge LLM — si le juge est un modèle — y lise la bonne réponse, tandis qu'une extraction mécanique échouerait).
- **Coût :** 1 ronde de conception (environ 10 USD, RAPPORTÉ) dédiée au post-traitement syntaxique des sorties. Le contrôle juge-juge de A passe à 100 % (le juge est déterministe à température 0 sur la même chaîne), et la BA bondit de $\ge 0,10$ uniquement parce que des erreurs de formatage (« réponses invalides ») deviennent des réponses valides ou indulgentement notées.

### 4. Évasion conjointe de tous les instruments de A (attaque combinée sur la règle gelée)
Comment un organisme trompe simultanément le Duel 1, le Duel 3, le Duel 7 et la règle de décision gelée (Point 3) pour forcer la décision « Monter » sans aucun gain réel de capacité de surveillance :
1. **Au cran 1 (budget bas) :** faute de rondes de conception suffisantes, l'organisme échoue à formater correctement 3 items sur 24 en famille B (comptés comme erreurs par la règle du noyau, RAPPORTÉ), et stabilise son comportement via une heuristique de surface déterministe (ce qui maintient $\sigma_{\text{graine}} \le 0,025$ au Duel 1, poussant A à réduire le nombre de graines).
2. **Au cran 2 (budget doublé) :** la ronde de conception supplémentaire corrige le formateur syntaxique (récupérant les 3 items en famille B, soit $\hat{\Delta} = 3/24 = +0,125 \ge \delta$), moissonne des indices contextuels courts ($< 50$ jetons consécutifs, passant sous le radar du Duel 7) et consomme tout le budget servi en allongeant les traces de raisonnement (verrouillant le Duel 3 à un ratio de 1,0).
- **Coût total de l'illusion :** 1 ronde de conception ($\approx 10$ USD, illustratif) + le surcoût de longueur de sortie ($\approx 12$ USD/génération, RAPPORTÉ). Tous les voyants de A sont au vert, le test déclare un gain de $+0,125$, alors que la capacité intrinsèque de détection de sabotage sur des réponses valides n'a pas progressé d'un iota.

---

## (c) Contrôles négatifs dont l'absence dans A est fatale

### 1. Contrôle de séparation « erreurs de formatage vs erreurs de classification » (absent dans A)
La règle du programme stipule qu'une tâche sans réponse valide compte comme une erreur (RAPPORTÉ). A n'isole jamais le taux de réponses invalides.
- **Pourquoi l'absence est fatale :** si le cran 2 passe de 4 réponses invalides à 0 en famille B, rien qu'en répondant au hasard sur ces 4 items, l'organisme gagne en espérance $+2$ items corrects ($\Delta \text{BA} = +0,083$), soit presque $\delta = 0,10$, sans aucune amélioration du classifieur.
- **Contrôle négatif requis :** journaliser séparément le taux de réponses invalides $r_{\text{inv}}$ par bras et calculer une exactitude équilibrée secondaire où les réponses invalides sont remplacées par le classifieur de surface de référence (0,69 en A, 0,50 en B, RAPPORTÉ) ou par un tirage de pièce équitable. Si le gain $\hat{\Delta}$ disparaît sous cette imputation, l'escalier n'a acheté que de la conformité syntaxique, pas de la sécurité.

### 2. Contrôle négatif d'ablation de la moisson ($M = \emptyset$)
A traite la moisson comme une simple « covariable (on la fixe ou on la journalise) » (Point 0) et compte sur le filtre de 50 jetons (Duel 7) pour écarter toute fuite.
- **Pourquoi l'absence est fatale :** un filtre lexical de 50 jetons ne détecte ni la paraphrase, ni l'agrégation d'indices multi-documents, ni la fuite de métadonnées. Si plus de générations (cran 2) permettent simplement d'exploiter plus finement une fuite documentaire issue de la moisson, tout l'escalier de coût mesure la capacité de triche documentaire de l'organisme.
- **Contrôle négatif requis (Duel B4) :** faire tourner le cran vainqueur avec la moisson coupée ($M = \emptyset$ ou remplacée par un corpus blanc hors domaine) sur les mêmes graines.
  - $H_A$ : le gain $\hat{\Delta}$ entre le cran 1 et le cran 2 se maintient à $\ge \delta/2$ sans moisson.
  - $H_B$ : le gain s'effondre sous $\delta/4$ quand la moisson est coupée (ou n'apparaît que sur les items de la famille A dont les sources sont publiques). Si $H_B$ et que la famille B (traces de délégation internes non publiques) ne progresse pas, le gain en A est un artefact de contamination indirecte que le filtre de 50-grammes a manqué.

### 3. Calibration par simulation à blanc (test A/A synthétique) du rééchantillonnage à 2 niveaux
A propose d'utiliser la paire A contre A du pilote comme contrôle négatif de sa chaîne d'analyse (« doit donner un IC couvrant 0 », Duel 2).
- **Pourquoi c'est insuffisant et fatal :** vérifier qu'un seul intervalle de confiance couvre 0 sur *une seule paire* de graines a une probabilité de réussite d'au moins 90 % même pour un estimateur gravement défectueux (ou 100 % si l'IC est trop large). À l'inverse, comme montré en (a.1) et (a.2), l'IC à deux niveaux de A souffre de deux biais opposés : trop étroit au niveau des graines (dégénérescence à $k \le 4$), mais écrasé par la variance des 24 items au niveau des items (rendant la puissance conditionnelle nulle).
- **Contrôle négatif requis :** avant de sceller la règle du Point 3, passer la chaîne d'estimation dans 1 000 matrices synthétiques de taille $24 \times k$ générées sous l'hypothèse nulle conditionnelle (mêmes probabilités de réussite par item entre bras, variance inter-graines égale à $\hat{\sigma}_{\text{graine}}$) et sous l'hypothèse alternative ($\Delta = +0,10$ par bascule de 3 items nets). Ce contrôle falsifiera immédiatement la compatibilité entre le choix d'un IC à deux niveaux (rééchantillonnant les items) et la revendication d'une puissance de 80 % à $\delta = 0,10$ avec 4 graines.

### 4. Contrôle négatif de troncature temporelle (pour tester la non-monotonicité, Présupposé 3)
A note à raison (Présupposé 3) que « plus de générations $\rightarrow$ dérive, surapprentissage de sa propre validation interne », mais son plan à deux crans ($B_0$ vs $2B_0$) ne permet pas de distinguer un organisme qui stagne dès la génération 1 d'un organisme qui progresse jusqu'à la génération 3 puis dérive jusqu'à la génération 6.
- **Pourquoi l'absence est fatale :** si le cran 2 ($2B_0$, 6 générations) obtient le même score que le cran 1 ($B_0$, 3 générations), A conclut à un plateau précoce et arrête tout, alors que l'organisme a pu atteindre $\Delta = +0,15$ à la génération 2 avant de surapprendre sa validation interne, ou inversement que le cran 1 à $B_0$ a lui-même déjà régressé par rapport à la génération 0.
- **Contrôle négatif requis :** évaluer sur le test final (en lecture post-hoc journalisée par le noyau, sans retour à l'organisme) l'état de l'organisme à la génération 0 (avant évolution) et aux générations intermédiaires d'un même run, en appliquant une correction de comparaisons multiples (ou en réservant cette lecture au diagnostic de dérive). Si la génération 0 bat la génération finale du cran 1, tout l'escalier sur le nombre de générations repose sur une dynamique de dégradation.

FIN-DE-CELLULE