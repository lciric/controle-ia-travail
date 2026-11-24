### 1. Le zéro est-il forcé ?

Avant d'interpréter pourquoi les juges séparent mal le saboteur de l'honnête, il faut séparer deux questions : **étant donné leurs notes par action, obtenir zéro épisode en alerte sur 256 est-il surprenant ?** Non — ce zéro est même potentiellement forcé à 100 %, et statistiquement banal sinon. Ce qui appelle explication n'est pas le passage des notes au zéro d'alerte, mais la platitude des notes elles-mêmes face à un coût multiplié par environ dix-huit.

**Faits établis utilisés dans le calcul.** L'étalonnage du seuil utilise $N = 256$ épisodes honnêtes pour viser $\alpha = 1\,\%$ de fausses alertes par épisode entier par rang conforme, avec inégalité stricte ($S > \tau$ : une égalité n'alerte pas). La note d'action est bornée dans $[0, 100]$ (espérance sur les jetons « 0 » à « 100 »). Sur les 256 épisodes dits sabotés, seuls $K = 192$ (doses 0,50 à 1,00) ont un effet établi sur le coût ; à la dose 0,25 (+0,09, intervalle couvrant zéro), **tous** les surveillants du tableau, y compris « mots et coût », donnent zéro alerte au maximum. À pleine dose, à 1 % de fausses alertes *par action*, les deux juges avec raisonnement ne détectent que 0,2 % et 1,3 % des actions, et 23,75 % des actions sont non lues contre 12,66 % chez l'honnête.

**Premier mécanisme (zéro arithmétiquement forcé, probabilité 100 %).** Sous rang conforme exact à $\alpha = 0,01$ sur $N = 256$, la valeur-$p$ conforme d'un score d'épisode $Y$ vaut $(1 + \#\{i : M_i \ge Y\}) / 257 \le 0,01$, ce qui exige $\#\{i : M_i \ge Y\} \le 1$, soit $Y > M_{(255:256)}$ (la 255e statistique d'ordre sur 256). **Supposé :** cette convention standard est celle du code (**je ne sais pas** si le code utilise $M_{(255:256)}$ ou le quantile empirique $M_{(254:256)}$). Dans les deux cas, il suffit que **deux** épisodes honnêtes sur 256 (soit deux actions sur environ $256 \times 10 \times (1 - 0,1266) \approx 2\,236$ actions honnêtes lues) atteignent la borne supérieure de 100 à la précision machine pour fixer $\tau = 100$. Avec l'alerte stricte $Y > 100$ sur une échelle bornée à 100, le zéro sur 256 est **mathématiquement obligatoire**, quel que soit le saboteur. Même sans atteindre 100, un empilement discret sur un jeton favori (« 90 », « 95 ») écrase les alertes, comme l'illustre déjà la règle du coût brut (aire 0,84 mais seulement 4 alertes sur 64 à pleine dose à cause de 86 % d'égalités au seuil). **Je ne sais pas** si $\tau$ atteint un tel palier pour les juges, cette donnée manquant au verdict (F.1).

**Second mécanisme (zéro non surprenant même pour des notes continues sans aucune égalité).** **Supposé :** notes continues et absence totale de signal (hypothèse nulle d'échangeabilité entre épisodes honnêtes et sabotés). Une erreur classique consiste à calculer $(1 - 0,01)^{256} = 7,6\,\%$, en oubliant que les $K$ épisodes de test affrontent **le même** seuil aléatoire $M_{(255:256)}$. Sur $N + K$ épisodes continus échangeables, obtenir zéro alerte équivaut exactement à ce que les deux plus grands scores de l'ensemble fusionné tombent dans l'échantillon d'étalonnage :
$$\mathbb{P}(\text{0 alerte} \mid H_0 \text{ continue}, \tau = M_{(255:256)}) = \frac{\binom{256}{2}}{\binom{256+K}{2}} = \begin{cases} \frac{256 \times 255}{512 \times 511} = \mathbf{25,0\,\%} & (K = 256), \\ \frac{256 \times 255}{448 \times 447} = \mathbf{32,6\,\%} & (K = 192 \text{ à effet établi}). \end{cases}$$
(Si le code utilisait $M_{(254:256)}$, ces probabilités resteraient de 12,4 % et 18,6 %.) Trois faits établis relèvent encore cette probabilité au-delà de 25–33 % :
1. **Raréfaction du maximum par action :** un épisode honnête compte en moyenne $8,73$ actions lues contre $7,63$ à pleine dose ; le maximum d'un échantillon plus court est mécaniquement plus bas.
2. **Inversion de queue :** passer de 1 % de fausses alertes par épisode ($\approx 0,78\,\%$ marginal pour $2/257$) à l'échelle de l'action impose un seuil par action d'environ $0,78\,\% / 8,73 \approx 0,09\,\%$ (sous indépendance intra-épisode supposée). Or, même au seuil dix fois plus lâche de 1 % par action, l'un des juges ne détecte que **0,2 %** des actions à pleine dose (cinq fois *moins* que chez l'honnête) et l'autre 1,3 %.
3. **Corrélation par tâche :** les 256 épisodes répètent 4 fois les mêmes 64 tâches ; une corrélation positive intra-tâche concentre les dépassements et accroît la probabilité de zéro global.

**Proposition — Vérifications immédiates sur les notes existantes (sans carte graphique) :**
- Lire la valeur numérique de $\tau$, le maximum global observé sur chaque juge, la convention d'indice conforme du code, et la fraction exacte d'épisodes d'étalonnage et de test vérifiant $Y = \tau$.
- Recalculer le nombre d'alertes sous bris d'égalité uniforme (rang conforme lissé).
- Tracer les quantiles 99 % et 99,9 % des notes *par action* par dose et vérifier si le saboteur comprime la queue haute des notes.
- Vérifier la dépendance du maximum d'épisode au nombre d'actions effectivement lues par épisode.

---

### 2. Les explications rivales

Six causes distinctes peuvent expliquer le silence des juges génériques. Elles ne sont pas mutuellement exclusives (notamment entre le juge de trois milliards et celui de huit milliards), mais chacune porte une signature propre vérifiable d'abord sur les fichiers existants, sans carte graphique.

#### Cause 1 — Censure au seuil strict par discrétisation ou plafonnement (C.3, F.1)
- **Prédiction propre (proposition d'épreuve) :** les notes séparent en réalité le saboteur dans la queue haute, mais un amas d'égalités en $S = \tau$ (ou $\tau = 100$) bloque l'inégalité stricte. Contrairement aux autres causes, l'aire sous la courbe en queue droite ou le rang conforme lissé récupère immédiatement des alertes, **sans** modifier les notes par action. *(Note : établi que l'aire globale est 0,52–0,56 et le rappel par action à 1 % est 0,2–1,3 %, donc cette cause ne peut expliquer à elle seule la platitude des juges avec raisonnement, mais elle peut expliquer l'écrasement d'autres variantes.)*
- **Contrôle le moins cher (sans carte graphique) :** tabuler la distribution empirique autour de $\tau$ et recalculer les alertes avec bris d'égalité aléatoire pour tous les juges (y compris en une passe).
- **Confirmation / infirmation :** confirmée comme verrou si la part d'égalités en $\tau$ dépasse quelques pourcents ou si $\tau = 100$ ; écartée si $\tau < 100$, les égalités sont quasi nulles et le bris d'égalité laisse le nombre d'alertes proche de zéro.

#### Cause 2 — Corruption mécanique de la lecture de note : balises imposées et discordance texte-jetons (A.6, A.9, C.4)
- **Prédiction propre :** le modèle détecte une anomalie dans son raisonnement ou en une passe, mais la mesure numérique finale est détruite soit par troncature avant la balise (établi pour 70,5 à 75,0 % des actions du juge de trois milliards avec raisonnement, qui chute de 0,65 en une passe à 0,52–0,56 avec raisonnement), soit parce que la masse de probabilité tombe hors des jetons exacts « 0 » à « 100 » (par exemple jetons précédés d'une espace ou format inattendu), soit parce que le texte de raisonnement exprime un doute que la note numérique écrase.
- **Contrôle le moins cher (sans carte graphique) :** (a) recalculer l'aire du juge de trois milliards uniquement sur les 25 à 29,5 % d'actions à balise naturelle ; (b) vérifier dans les journaux la somme des probabilités portées par les jetons « 0 » à « 100 » ; (c) chercher par expressions régulières dans les textes de raisonnement déjà produits par le juge de huit milliards à pleine dose toute mention d'anomalie budgétaire ou d'ordre de grandeur, et corréler cette mention à la note lue.
- **Confirmation / infirmation :** confirmée si le sous-ensemble à balise naturelle remonte nettement, si la masse sur « 0 »–« 100 » est faible, ou si les raisonnements écrits du huit milliards signalent des coûts aberrants sans que la note suive ; écartée si la masse est proche de 1, la balise naturelle sur le huit milliards et son texte ne mentionnent jamais d'écart de coût.

#### Cause 3 — Myopie du cadrage sur la « dernière modification » et biais des actions non appliquées (A.6, C.5)
- **Prédiction propre :** le saboteur introduit le coût gonflé lors d'un seul pas (par exemple la rédaction initiale au pas 1), puis consacre les neuf autres pas à des retouches textuelles bénignes (ou échoue plus souvent à appliquer ses actions : 23,75 %). Tandis que « coût brut » et « mots et coût » lisent l'état courant qui conserve le surcoût sur les dix pas (d'où des aires par action de 0,84 et 0,97), un juge à qui l'on demande seulement si *la dernière modification* est sabotée répond légitimement « non » sur huit ou neuf pas sur dix — ce qui plafonne mécaniquement son aire par action près de 0,55.
- **Contrôle le moins cher (sans carte graphique) :** extraire des états enregistrés la variation du coût à chaque pas ($\Delta \text{coût}_t$) et recalculer l'aire des juges *uniquement sur les pas où le champ de coût est créé ou accru* (ainsi qu'au pas $t = 1$ isolément).
- **Confirmation / infirmation :** confirmée si l'aire des juges grimpe franchement sur les seuls pas où $\Delta \text{coût}_t > 0$ tout en valant 0,50 ailleurs ; écartée si l'aire reste sous 0,58 même sur les actions qui multiplient directement le coût.

#### Cause 4 — Cécité informationnelle par absence d'étalon de coût (A.6, A.9, E.5)
- **Prédiction propre :** comme l'agent honnête s'écarte lui-même de plus d'un facteur dix du coût de référence dans 43,7 % des cas au pilote (établi, A.9), les coûts honnêtes balaient plusieurs ordres de grandeur d'une tâche à l'autre. Privé du coût de référence et d'exemples honnêtes, un juge générique interprète un budget dix-huit fois supérieur au pair honnête *de la même tâche* comme une estimation imprécise bénigne tant que le montant absolu reste dans l'enveloppe générale des projets possibles — mais ses notes montent dès que le montant absolu franchit un ordre de grandeur manifestement absurde dans l'absolu.
- **Contrôle le moins cher (sans carte graphique) :** régresser les notes existantes des juges sur le logarithme du coût absolu déclaré à travers toutes les conditions (y compris le saboteur à consigne explicite), en isolant le décile supérieur des montants absoluts en monnaie.
- **Confirmation / infirmation :** confirmée si la pente de la note sur le coût absolu est nulle dans la zone de recouvrement inter-tâches mais devient nettement positive sur les montants extrêmes ; écartée si la pente reste plate même sur les montants les plus extravagants du corpus.

#### Cause 5 — Dissimulation par cohérence interne du texte (rationalisation du surcoût)
- **Prédiction propre :** le saboteur ne gonfle pas un chiffre isolé ; il redimensionne dans le texte l'ampleur apparente du protocole (matériel, volume d'essais) pour justifier le budget. Un lecteur sans budget cible voit alors une proposition chère mais cohérente. Unique prédiction : le juge réagit sur les épisodes *incohérents* (coût très élevé mais traits textuels du prédicteur à douze traits ou du sac de mots indiquant une petite expérience), et reste muet sur les épisodes où texte et coût bougent ensemble.
- **Contrôle le moins cher (sans carte graphique) :** calculer sur les épisodes à pleine dose le résidu du logarithme du coût prédit par les seuls traits lexicaux existants, et comparer les notes des juges entre fort résidu positif (surcoût nu, non justifié) et faible résidu (surcoût accompagné lexicalement).
- **Confirmation / infirmation :** confirmée si les juges notent plus sévèrement les surcoûts nus que les surcoûts justifiés ; écartée si les notes sont aussi plates sur les incohérences criantes.

#### Cause 6 — Incapacité intrinsèque (et auto-complaisance de lignée) des modèles de trois et huit milliards en surveillance ouverte (B, E.2)
- **Prédiction propre :** conformément à Ryd et al. (E.2, où Llama-3.1 de huit milliards est qualifié de superviseur « très faible »), ces petits modèles génériques produisent du quasi-bruit dès qu'aucun mot-clé caricatural de malveillance n'apparaît, ou bien le juge de huit milliards fait preuve de complaisance envers les productions de son propre modèle. Deux faits établis appuient déjà cette lecture : l'accord de rang quasi nul entre les deux juges avec raisonnement (0,07 sur l'honnête, 0,04 à pleine dose) et le paradoxe du trois milliards en une passe (aire 0,65) battant le huit milliards (0,55). Unique prédiction : l'accord intra-modèle entre lecture en une passe et avec raisonnement est lui aussi très bas, et les 0,65 du trois milliards en une passe proviennent d'un artefact stylistique de l'adaptateur plutôt que d'une lecture du coût.
- **Contrôle le moins cher (sans carte graphique) :** calculer (a) l'accord de rang entre une passe et raisonnement au sein de chaque modèle sur les mêmes actions, et (b) **l'aire du juge de trois milliards en une passe sur l'adaptateur témoin contre l'honnête** (absente du tableau B, où seul son zéro d'alerte figure, alors que « mots et coût » y atteint 0,68), ainsi que sa corrélation partielle au coût déclaré.
- **Confirmation / infirmation :** confirmée si la cohérence interne est quasi nulle, la pente au coût nulle même sur surcoût incohérent, et si le trois milliards en une passe réagit aussi à l'adaptateur témoin ; écartée si une lecture cohérente du coût existe déjà dans une variante existante.

---

### 3. Ce qu'une base boîte noire doit être pour que la comparaison ait un sens

**Ce qui est établi (D.1, D.3) :** la porte opposera une sonde séquentielle sur états internes à « la meilleure base boîte noire, toutes variantes confondues », bras génériques et spécialisés rapportés à part, avec lecture unique d'un mode de sabotage tenu à l'écart, sans service tiers. **Je ne sais pas** si la sonde interne sera entraînée uniquement sur des trajectoires honnêtes (détection d'anomalie) ou supervisée sur d'autres modes de sabotage connus avant d'affronter le mode tenu à l'écart. **Proposition :** l'échelle des bases doit couvrir ces régimes sans trou informationnel, en six échelons du plus pauvre au plus riche.

#### Échelle proposée des bases boîte noire
1. **Échelon 0 — Juge générique aveugle par pas (base actuelle, plancher informationnel) :**
   - *Sait :* tâche, état courant, dernière modification ; aucun exemple honnête, aucune référence.
   - *Apprend :* uniquement le seuil scalaire final sur épisodes honnêtes.
   - *Modèle :* modèles ouverts de trois et huit milliards de paramètres (deux lignées, A.8).
2. **Échelon 1 — Surveillant générique ancré sur la normalité honnête et la trajectoire complète :**
   - *Sait :* la trajectoire entière (actions appliquées **et** tentatives non appliquées, C.5) ainsi que des exemples d'épisodes honnêtes et de témoins bénins sur tâches d'entraînement ; aucune connaissance d'aucun sabotage.
   - *Apprend :* une mesure d'anomalie à une classe sur traits textuels, métadonnées d'échec d'action et surprise lexicale (log-vraisemblance du texte produit lue par le modèle honnête ouvert de base, sans accès aux états internes de l'agent).
   - *Modèle :* modèle ouvert de huit milliards de paramètres + détecteur statistique d'anomalie à une classe.
3. **Échelon 2 — Architecture générique structurée et durcie (variantes dues de A.8) :**
   - *Sait :* trajectoire entière, exemples honnêtes, jeux publics d'étalonnage et sabotages *connus hors du mode tenu à l'écart*.
   - *Apprend :* consigne optimisée contre attaques (« juge durci », E.1) et modèle temporel séquentiel appris sur observateur séparé (A.8), combinés au moniteur en trois temps (triage, inspection, jugement, E.4).
   - *Modèle :* modèles ouverts de huit milliards de deux lignées distinctes.
4. **Échelon 3 — Plafond générique ouvert de grande capacité (référence d'échelle de modèle, D.3) :**
   - *Sait et apprend :* exactement comme l'échelon 2, sans service tiers.
   - *Modèle :* grand modèle ouvert exécuté localement (par exemple soixante-dix milliards de paramètres ou équivalent ouvert disponible, *supposé* accessible sous l'accord prévu en D.3).
5. **Échelon 4 — Classifieur textuel séquentiel à parité exacte d'étiquettes avec la sonde :**
   - *Sait :* **strictement les mêmes épisodes étiquetés** (honnêtes, témoins distillés, modes de sabotage d'entraînement hors mode tenu à l'écart) que ceux fournis à la sonde interne, mais réduits au texte émis et aux indicateurs d'actions échouées.
   - *Apprend :* une tête linéaire ou séquentielle régularisée avec la même fonction de perte et la même pénalisation d'artefact d'adaptateur que la sonde.
   - *Modèle :* représentations textuelles extraites d'un lecteur ouvert figé de huit milliards (et du modèle de l'échelon 3 si disponible).
6. **Échelon 5 — Surveillant spécialisé sur mode connu (plafond de domaine, rapporté à part selon D.1) :**
   - *Sait :* le champ cible du sabotage étudié, mais avec une normalisation par tâche calculée **exclusivement sur des épisodes honnêtes** (éliminant le centrage sur les neuf conditions de A.5).
   - *Apprend :* classifieur supervisé par validation croisée sur tâches disjointes contre témoin distillé honnête aux mêmes doses (C.2).
   - *Modèle :* prédicteur statistique léger sur traits du domaine et sac de mots (sert à qualifier « diffus » contre « flagrant » en D.2, non à juger le transfert aveugle sur le mode tenu à l'écart).

#### Conditions d'équité avec la sonde sur états internes (propositions)
- **Parité des données d'entraînement :** sur le mode tenu à l'écart (D.1), la sonde doit battre le maximum des **échelons 1 à 4** nourris des *mêmes* épisodes d'entraînement. Opposer une sonde entraînée sur des exemples honnêtes et sabotés à un juge de l'échelon 0 privé de tout repère honnête fausse la comparaison.
- **Parité d'immunité à l'artefact d'adaptateur (C.2) :** puisque le texte seul trahit déjà l'adaptateur témoin à 0,68 d'aire, les états internes le trahiront plus encore. Le budget de 1 % de fausses alertes doit être garanti à la fois sur l'honnête nu et sur le **témoin distillé honnête aux quatre doses**, pour la sonde comme pour la boîte noire.
- **Parité d'observabilité des échecs d'action (C.5) :** si la sonde observe l'agent pendant les 23,75 % d'actions non appliquées, la boîte noire doit aussi recevoir ces tentatives rejetées (ou leur décompte).
- **Parité de règle de seuil :** même rang conforme **lissé** (bris d'égalité aléatoire à graine scellée) afin que chaque méthode consomme réellement son budget nominal de 1 % de fausses alertes.

#### Ce qu'un relecteur exigeant demanderait
1. *Preuve de non-lecture du réglage fin :* l'aire et le taux d'alerte de la sonde (et des bases) sur le témoin distillé honnête aux doses 0,25 à 1,00.
2. *Dissociation entre accès interne et taille de modèle :* reporter le grand juge ouvert *après* la porte (D.3) est la principale vulnérabilité du devis. Un relecteur objectera qu'une sonde qui bat un juge de huit milliards (« très faible », Ryd et al., E.2) n'a pas battu la boîte noire, mais un modèle sous-dimensionné.
3. *Gain marginal :* la combinaison « meilleure boîte noire + sonde » bat-elle la meilleure boîte noire seule au seuil de 1 % ?

---

### 4. Les épreuves d'admission d'un juge

L'absence actuelle de témoin positif propre aux juges (établi, B) interdit de savoir si un juge muet est aveugle au sabotage étudié ou simplement hors d'état de fonctionner. **Proposition :** avant toute lecture d'épisodes d'évaluation, tout juge doit franchir un sas d'admission à double face sur le reliquat déjà disponible des épisodes d'étalonnage ($320 - 256 = 64$ épisodes honnêtes hors seuil, établi en A.4) et sur les témoins.

#### Objets que le juge doit réussir (témoins positifs de sensibilité et d'intégrité)
1. **Intégrité mécanique de sortie :** sur les 64 épisodes honnêtes hors seuil, taux de balises de verdict produites naturellement (sans imposition) quasi total, masse de probabilité cumulée sur les jetons « 0 » à « 100 » proche de l'unité, et seuil conforme à 1 % strictement inférieur à 100.
2. **Défaut planté textuel manifeste hors coût (objet P1a) :** épisodes honnêtes hors seuil où l'on injecte mécaniquement une altération grossière générique (contradiction explicite avec la question de recherche ou mention directe d'altération du protocole). Le juge doit dépasser largement son plancher par permutation et afficher un rappel substantiel à 1 % de fausses alertes.
3. **Défaut planté arithmétique grossier sur le coût (objet P1b) :** épisodes honnêtes hors seuil où le seul coût d'une petite expérience est multiplié par un facteur caricatural (par exemple $10^6$) sans modifier le texte justificatif. Distingue la cécité générale de la cécité spécifique aux champs numériques.
4. **Monotonie et répétabilité :** croissance monotone de la note moyenne sur trois paliers d'intensité d'un défaut planté, et accord de rang positif élevé entre deux lectures indépendantes ou reformulations neutres.
5. **Jeux publics d'étalonnage externes (prévus en A.8) :** dépassement franc du plancher de permutation sur au moins deux modes de sabotage publics hors du mode tenu à l'écart.

#### Objets sur lesquels la discrimination du juge doit échouer (témoins négatifs et d'invariance)
Un juge valide **doit échouer à séparer** (aire non supérieure au plancher de permutation et taux d'alerte conforme à 1 %) :
1. **Partage honnête contre honnête :** les 64 épisodes honnêtes de réserve face aux 256 d'étalonnage (vérifie l'absence de fuite d'ordre ou d'identifiant).
2. **Témoin distillé honnête aux quatre doses (C.2) et adaptateur témoin (A.3) contre agent honnête nu :** toute « réussite » ici prouve que le juge détecte la signature stylistique de la distillation et non la malveillance.
3. **Témoins à consigne bénins (A.3) et variations neutres de longueur ou de mise en forme à fond scientifique et coût constants.**

#### Règle écrite d'avance en cas d'échec à l'admission (proposition pré-enregistrée)
- **Verrouillage temporel :** l'admission est jugée *avant* ouverture des conditions sabotées d'évaluation.
- **Échec mécanique ou échec sur P1a :** le juge est déclaré **« instrument invalide »**, exclu de la porte de comparaison (D.1) et de la qualification « diffus » (D.2), et consigné uniquement en annexe technique ; il doit être réparé ou remplacé par un échelon supérieur avant lecture du test.
- **Réussite sur P1a mais échec sur P1b :** le juge est admis avec la mention **« aveugle aux ordres de grandeur numériques »** ; il reste rapporté dans le bras générique documentaire, mais ne peut servir seul de référence boîte noire face à une sonde sur un sabotage quantitatif sans les échelons 1 à 4.
- **Échec d'invariance (discrimination du témoin distillé honnête ou des témoins à consigne) :** le seuil de 1 % du juge est obligatoirement recalculé sur l'union du témoin bénin le plus pénalisant et de l'honnête, jamais sur l'honnête nu seul.

---

### 5. La symétrie

Dans un programme où une méthode nouvelle (la sonde boîte blanche) doit battre une base de référence (la boîte noire, D.1), **une base anormalement muette est un résultat tout aussi « trop propre » (complaisant envers l'hypothèse principale) qu'un détecteur anormalement infaillible**. Or les cinq clauses actuelles de C.6 ne surveillent que la sur-performance globale ou le silence simultané de *tous* les surveillants.

#### Conditions symétriques proposées à ajouter (déclenchement disjonctif : une seule suffit)
1. **Silence d'un bras sous sabotage prouvé :** à toute dose où l'effet comportemental du sabotage est statistiquement établi **et** où un surveillant spécialisé dépasse 0,85 d'aire, l'audit se déclenche si la meilleure variante du bras générique reste sous son plancher par permutation ou produit zéro alerte par épisode.
2. **Sous-couverture au seuil ou inversion de queue :** déclenchement dès qu'un surveillant présente (a) un taux de détection à pleine dose inférieur à son taux nominal de fausses alertes (cas du 0,2 % observé en B), (b) un seuil $\tau$ égal au maximum théorique de l'échelle, ou (c) une part d'égalités au seuil dans l'étalonnage dépassant un plafond fixé d'avance (par exemple 10 %).
3. **Défaillance mécanique ou incohérence interne :** déclenchement si le taux de balises imposées ou d'actions non évaluées pour défaut de format dépasse un seuil bas (par exemple 5 %), si une variante « avec raisonnement » est significativement battue par sa propre lecture « en une passe », ou si l'accord de rang entre deux juges génériques à pleine dose est quasi nul.

#### Traitement après coup des égalités au seuil et des balises imposées sans altérer un texte scellé (proposition)
1. **Intangibilité du chiffre scellé :** le tableau primaire du verdict actuel reste inchangé et archivé tel quel, assorti d'un avertissement métrologique explicite sur les réserves C.3 et C.4. On ne réécrit jamais un protocole après lecture des données.
2. **Avenant de diagnostic post-hoc horodaté et sans paramètre libre :** publier séparément, sous l'étiquette explicite *« analyse de sensibilité secondaire non pré-enregistrée »* :
   - *Pour les égalités au seuil :* l'encadrement déterministe complet `[alerte stricte S > τ ; alerte large S ≥ τ]` accompagné de **l'espérance analytique exacte du rang conforme lissé** (qui restaure mathématiquement $\alpha = 1\,\%$ sans aucun paramètre à régler).
   - *Pour les balises imposées :* une présentation en trois lignes sans retouche de modèle : (i) population entière scellée ; (ii) sous-ensemble à balise naturelle (en affichant le taux d'exclusion de 70,5–75,0 %) ; (iii) bornes extrêmes d'imputation de pire et meilleur cas (notes manquantes fixées à 0 puis à 100).
3. **Protocole scellé de version suivante ($v+1$) pour la porte à venir :** inscrire le rang conforme lissé (à graine fixée d'avance) et le sas d'admission de la section 4 dans un nouvel acte scellé *avant* de lancer les variantes manquantes (A.8) et *avant* l'unique lecture du mode de sabotage tenu à l'écart (D.1). Sur les 64 tâches de coût déjà lues, toute nouvelle passe portera le statut de « relecture sur banc connu », la valeur probante primaire scellée étant portée par les jeux neufs et le mode tenu à l'écart.

---

### 6. Plan

Tous les ordres de grandeur de coût ci-dessous sont **supposés** (aucun coût d'exécution ou de temps humain ne figurant au dossier).

#### Phase 1 — Sur les données existantes, sans carte graphique (immédiat)
1. **Audit du seuil et des égalités (section 1 et cause 1) :** extraire $\tau$, la part d'égalités, le rang conforme lissé et les queues à 99 % et 99,9 % pour tous les juges ; corriger aussi hors fuite la normalisation de « mots et coût » en centrant chaque tâche sur l'étalonnage honnête seul. *Coût supposé : 0,5 à 1 jour-personne d'ingénieur, calcul négligeable sur processeur central.*
2. **Autopsie des causes 2 à 6 sur journaux existants :** (a) aire du trois milliards hors balises imposées et masse des jetons « 0 »–« 100 » ; (b) fouille lexicale des raisonnements écrits du huit milliards ; (c) aire stratifiée selon $\Delta \text{coût}_t > 0$ et selon le nombre d'actions lues ; (d) régression des notes sur le coût absolu et sur les surcoûts lexicalement incohérents ; (e) **aire du trois milliards en une passe sur l'adaptateur témoin** et accords de rang intra-modèle (une passe contre raisonnement). *Coût supposé : 1 à 2 jours-personnes, zéro carte graphique.*
3. **Rédaction de l'avenant de sensibilité post-hoc et du protocole scellé $v+1$** (clauses d'admission de section 4, audit symétrique de section 5, échelle de bases de section 3). *Coût supposé : 1 jour-personne.*

#### Phase 2 — Ce qui demande une course sur cartes graphiques (après scellement de $v+1$)
4. **Sas d'admission des juges (section 4) sur les 64 épisodes honnêtes hors seuil + défauts plantés P1a et P1b :** qualifie la chaîne de lecture et départage définitivement cécité générale et cécité au coût. *Coût supposé : quelques heures-carte graphique (quelques centaines d'inférences courtes).*
5. **Production du témoin distillé honnête manquant aux doses 0,25, 0,50, 0,75 et 1,00 (C.2) :** indispensable avant toute comparaison avec des sondes internes. *Coût supposé : modéré, de l'ordre de quelques dizaines d'heures-carte graphique pour quatre réglages fins d'adaptateur et $4 \times 64$ épisodes de dix pas.*
6. **Exécution des variantes boîte noire dues (A.8) et des échelons 1, 2 et 4 de la section 3** (ancrage sur exemples honnêtes, trajectoire complète incluant tentatives non appliquées, moniteur en trois temps, juge durci, modèle temporel, autre lignée, deux jeux publics). *Coût supposé : significatif, de l'ordre de quelques dizaines à quelques centaines d'heures-carte graphique selon le moniteur en trois temps et l'optimisation du juge durci.*

#### Phase 3 — Ce qui demande la décision du directeur
7. **Avancer le grand juge ouvert (D.3) *avant* ou *à* la porte de comparaison :** maintenir ce plafond *après* la porte expose le verdict sonde contre boîte noire à une réfutation frontale (victoire contre un superviseur « très faible »). Décider maintenant de l'inclure au moins sur l'évaluation de la porte. *Coût supposé : négociation de l'accord interne + quelques dizaines à une centaine d'heures sur nœud multi-cartes graphiques.*
8. **Arbitrer la règle de la porte D.1 sur les échelons 1 et 4 :** acter que la « meilleure base boîte noire » inclut le droit aux mêmes épisodes d'entraînement (honnêtes et autres modes) et aux mêmes indicateurs d'actions échouées que la sonde interne. *Coût supposé : décision de gouvernance sans coût de calcul propre.*
9. **Statuer sur les juges actuels de trois et huit milliards s'ils ratent l'admission P1a/P1b :** entériner leur déclassement hors dénominateur de référence conformément à la règle pré-écrite.

#### Confiance dans la lecture « juges faibles » et conditions de révision
- **Confiance actuelle : 0,85** dans la lecture selon laquelle le zéro reflète la **faiblesse du dispositif de jugement générique actuel** (modèles de trois et huit milliards sous-dimensionnés en surveillance ouverte, rupture de format sur 70,5–75 % du trois milliards, absence de repère honnête, cadrage local sur la dernière modification et règle d'alerte stricte), et **non** un sabotage invisible dans le texte (puisque le coût brut seul atteint déjà 0,84 d'aire et « mots et coût » 0,97).
- **Pourquoi pas 1,00 (les 0,15 restants) :** **je ne sais pas** encore si un juge même très grand, maintenu *sans coût de référence ni exemples honnêtes* (A.6), peut distinguer une inflation d'un facteur dix-huit textuellement rationalisée dans un domaine où l'agent honnête dévie déjà d'un facteur dix dans 43,7 % des cas (A.9 ; Hebbar, E.5). Si l'obstacle est cette impossibilité informationnelle sans étalon plutôt que la taille des modèles, remplacer huit milliards par soixante-dix milliards sous la même consigne aveugle échouera aussi.
- **Ce qui me ferait changer d'avis :**
  - *Baisse sous 0,30 (sabotage réellement furtif pour tout juge générique sans étalon) :* si l'audit sans carte graphique écarte l'effet de seuil et l'effet « dernière modification », que les juges réussissent les défauts plantés P1a et P1b (surcoût absurde non justifié), **et** qu'un grand juge ouvert ainsi que le moniteur en trois temps restent sous 0,60 d'aire tant qu'on leur refuse des exemples honnêtes, parce que le saboteur rend chaque surcoût scientifiquement plausible.
  - *Réorientation vers un pur bogue mécanique d'instrument (sans faiblesse de compréhension) :* si le retrait des balises imposées, le bris d'égalité au seuil ou la restriction aux seuls pas modifiant le coût suffisent dès la Phase 1 à faire monter les notes existantes au-dessus de 0,75 d'aire.

---

### 7. Ce que ce résultat permet de dire dès maintenant, et ce qu'il ne permet pas de dire

#### Ce qu'il permet de dire dès maintenant (établi)
- **Sur le saboteur :** la distillation inscrit une inflation nette du coût aux doses 0,50, 0,75 et 1,00 (jusqu'à $+1,26$ en logarithme décimal, environ dix-huit fois), mais **aucun effet n'est établi à la dose 0,25** ($+0,09$, intervalle couvrant zéro).
- **Sur la visibilité textuelle :** à pleine dose, le sabotage laisse une trace boîte noire massive, détectable sans apprentissage par le coût brut (aire 0,84 ; 0,90 sur consigne explicite) et fortement par un classifieur spécialisé (« mots et coût » : aire 0,97, 47,7 % de détection par action à 1 % de fausses alertes).
- **Sur les juges génériques joués :** interrogés par pas sans référence ni exemple honnête, les juges de trois et huit milliards avec raisonnement sont inopérants sur cette tâche (aires 0,52 à 0,56 sous le plancher de permutation, accord de rang quasi nul de 0,04 à 0,07) et le trois milliards avec raisonnement souffre d'un défaut majeur de format (70,5 à 75,0 % de balises imposées).
- **Sur deux pièges métrologiques du banc :** le réglage fin laisse une trace textuelle hors sabotage (« mots et coût » à 0,68 d'aire sur l'adaptateur témoin), le saboteur échoue presque deux fois plus souvent à appliquer ses actions (23,75 % contre 12,66 %), et l'alerte stricte par rang conforme sur 256 épisodes écrase sévèrement la sensibilité en présence d'égalités (86 % d'égalités réduisant une aire de 0,84 à 4 alertes sur 64).
- **Sur la gouvernance :** l'audit pré-enregistré des résultats « trop propres » est aveugle à l'effondrement unilatéral d'un bras de référence.

#### Ce qu'il ne permet pas de dire dès maintenant
- **Il ne permet pas de dire que la surveillance boîte noire générique échoue sur ce sabotage**, ni d'utiliser ce zéro comme référence face à des sondes internes (D.1), tant que manquent un témoin positif propre aux juges, les variantes prévues en A.8, l'ancrage sur exemples honnêtes et un modèle de capacité suffisante (D.3).
- **Il ne permet pas d'imputer le silence des juges à une cause unique** (capacité des modèles, absence de repère face aux 43,7 % d'écarts honnêtes, cadrage sur la seule dernière modification, ou écrasement au seuil) avant l'audit sans carte graphique de la Phase 1.
- **Il ne permet pas d'attribuer au coût les 0,65 d'aire du juge de trois milliards en une passe** tant que son aire sur l'adaptateur témoin n'a pas été lue.
- **Il ne permet pas de sceller définitivement la frontière « diffus / flagrant » (D.2)** sans le témoin distillé honnête aux quatre doses (C.2) et sans renormaliser « mots et coût » sur les seuls épisodes honnêtes (A.5).