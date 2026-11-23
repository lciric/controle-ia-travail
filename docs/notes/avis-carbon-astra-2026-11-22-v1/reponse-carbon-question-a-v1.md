### 1. Recommandation et niveau de confiance

**Recommandation : une option (b) guidée par le diagnostic du classifieur (appariement strict des gabarits + bornes nommées), couplée à une version symétrisée de (a) comme analyse co-rapportée (et repli pré-spécifié). Rejet ferme de (c) et de (a) appliquée seule dès maintenant.**

Concrètement, tant qu'aucun appel de modèle n'a été lancé (vos données de résultat sont encore vierges, donc réviser le générateur maintenant ne gonfle aucun risque de faux positif expérimental), la séquence optimale est :
1. **Diagnostiquer puis corriger le générateur — option (b) élargie** : ne pas se contenter de remplacer des grands littéraux par `0` ou `1`, mais **apparier les gabarits syntaxiques (1 pour 1)** entre vrais, faux tôt et pièges d'un monde à l'autre, et loger les bornes dans des constantes nommées du monde (voir pourquoi ci-dessous).
2. **Conserver la mesure sur contre-exemples vérifiés — option (a) corrigée — en co-analyse systématique** (en obligeant *les deux* bras à fournir un témoin structuré lorsqu'ils répondent « faux »), et n'en faire le critère principal de repli que si l'une des trois familles de mondes s'avère mathématiquement réfractaire à l'équilibrage après une itération bornée.

**Pourquoi ce choix plutôt que (a), (b) naïve ou (c) ?**
* **Pourquoi rejeter (c) :** Avec une aire observée de **0,939 à 0,982** sur 42 graines, relever le seuil pour ne pas déclencher la règle imposerait de le placer vers **0,985 ou 0,99**. Déplacer une barre pré-fixée de 0,75 à > 0,98 au vu des données vide le contrôle de toute substance. Surtout, à une aire de 0,96, un simple sac de bigrammes sépare quasi parfaitement le vrai du faux même à très bas taux de fausses alarmes : l'artefact n'est pas « limite », il est massif.
* **Pourquoi la révision 1 a échoué — et pourquoi (b) naïve (« mettre 0 ou 1 ») ne suffira pas seule :** Dans votre bayésien naïf, **chaque nombre est déjà remplacé par le même jeton `NUM`**. Pour ce classifieur, `0`, `1` et `9485731` sont **strictement indiscernables** ! Si l'aire reste à 0,94–0,98 après la première révision, ce n'est donc pas la grandeur des nombres qui trahit les faux dans le classifieur : c'est un déséquilibre dans la **fréquence des gabarits**, les **opérateurs/quantificateurs** ou l'usage d'**identifiants vs littéraux** (`c` vs `NUM`). À l'inverse, un modèle de langue voit les vrais chiffres : remplacer un grand littéral par `0`, `1` ou une constante nommée du monde `K` (définie aussi dans les mondes où l'énoncé est vrai, avec le même ordre de grandeur) est indispensable pour le LLM, *mais* doit s'accompagner d'un **équilibrage exact des gabarits** (chaque gabarit d'énoncé générant la même proportion de vrais, faux tôt et pièges à travers les mondes d'une famille) pour faire tomber l'aire du classifieur vers 0,50–0,60.
* **Pourquoi ne pas appliquer (a) immédiatement sans corriger le générateur :**
  1. Même si (a) empêche de marquer un point en devinant « faux » au style, une fuite de forme à 0,96 **contamine le comportement de l'agent avec outil** : en reconnaissant à la syntaxe qu'un énoncé a la tête d'un piège planté, le modèle (ou son relecteur) sait qu'il faut continuer à chercher au-delà de $N$ en Python au lieu de s'arrêter, tandis qu'il s'arrête tôt sur les énoncés ayant la syntaxe d'un vrai.
  2. Comme la part de pièges résolus par contre-exemple exact est inconnue, basculer aveuglément sur (a) expose l'essai à un **manque de puissance statistique** sévère si l'agent ne dépasse pas $N$ sur les pièges (voir calcul en section 4).

**Niveau de confiance :**
* **Élevé (85 %)** sur la décision méthodologique : rejeter (c), ne pas figer le banc d'essai à 0,94–0,98 d'aire avant tout appel LLM, et symétriser (a).
* **Modéré à élevé (70 %)** sur la faisabilité technique d'abaisser la fuite de style sous un seuil sain dans *chacune* des trois familles par appariement de gabarits et constantes du monde (l'incertitude résiduelle tient aux contraintes algébriques propres à vos trois familles, non détaillées ici).

---

### 2. Pertinence du seuil de 0,75 comme instrument de décision

Tel quel, **l'instrument est mal calibré à quatre niveaux**. Je ne le conserverais pas en l'état.

1. **Choix de l'aire ROC globale (et du masquage `NUM`) :**
   * *Inadéquation au régime de fausses alarmes de l'étude :* L'aire ROC intègre uniformément tous les taux de fausses alarmes (FPR de 0 à 1). Or votre test impose une borne haute $\le 0{,}10$ sur les 75 vrais — ce qui exige en pratique **au plus 2 ou 3 fausses alarmes sur 75** (FPR observé $\le 2{,}7\,\%$ à $4{,}0\,\%$ selon que l'intervalle à 95 % est bilatéral ou unilatéral). Deux générateurs ayant tous deux une aire de 0,75 ont des impacts opposés dans ce régime :
     * Cas 1 (chevauchement gaussien régulier, $\text{AUC}=0{,}75$) : à $\text{FPR}=3\,\%$, le rappel atteignable par la forme seule n'est que de **~16 %** (inoffensif face à une marge différentielle de 0,20 entre deux bras partageant le même modèle de base).
     * Cas 2 (50 % des faux utilisent un gabarit absent des vrais, et les 50 % restants sont identiques aux vrais : $\text{AUC}=0{,}75$) : à **$\text{FPR}=0\,\%$**, la forme seule donne gratuitement **50 % de rappel** !
   * *Angle mort du jeton `NUM` :* En écrasant tous les nombres sous `NUM`, l'instrument est aveugle aux indices numériques évidents pour un LLM (nombre à 7 chiffres vs `0` ou `1`, primalité, parité, proximité avec $N$).
   * *Entraînement groupé (faux tôt + pièges ensemble) :* Entraîner un seul modèle sur tous les faux mêlés dilue les indices si les deux strates ont des styles différents, et ignore la séparabilité *pièges contre faux tôt* (qui indique à l'agent quand chercher au-delà de $N$).

2. **Choix de la valeur 0,75 :**
   * Sur un générateur **programmatique** où vous contrôlez les gabarits, une vraie valeur populationnelle de 0,75 traduit déjà un fort déséquilibre structurel (un appariement propre vise **0,50 à 0,60**). À l'inverse, sur une *seule* graine de petite taille (30 vrais et ~15 faux par strate), l'erreur-type de l'aire sous l'hypothèse nulle ($\text{AUC}=0{,}50$) vaut $\text{SE}_0 = \sqrt{\frac{n_+ + n_- + 1}{12 n_+ n_-}} \approx \mathbf{0{,}092}$, de sorte que le bruit d'échantillonnage est énorme.

3. **Règle du « maximum des deux strates » :**
   * **C'est le bon principe sur le fond**, car les pièges représentent 49 % des faux (37/75) et les faux tôt 51 % (38/75) : si une seule strate fuit à 100 %, elle suffit à franchir la marge de 0,20.
   * En revanche, prendre le `max` empirique de deux estimateurs bruités sur petits effectifs crée un biais positif de sélection si l'on ne moyenne pas d'abord sur un grand nombre de graines.

4. **Absence d'intervalle de confiance :**
   * Ce que l'on juge ici est une propriété du **programme générateur**, pas d'un tirage isolé. Sur 30 vrais par graine, une aire individuelle oscille facilement de $\pm 0{,}15$ autour de 0,60 ; en revanche, moyennée sur **42 graines indépendantes**, l'erreur-type tombe à $\approx 0{,}092/\sqrt{42} \approx \mathbf{0{,}014}$ (sur vos 42 graines, l'intervalle empirique serré $[0{,}939 ; 0{,}982]$ prouve d'ailleurs avec une certitude totale que le vrai biais dépasse 0,95).

**Par quoi le remplacer ?**
* Évaluer le **générateur sur $\ge 40$ graines** (validation croisée groupée par mondes, avec intervalle de confiance à 95 % par bootstrap sur les mondes/graines).
* Entraîner **trois classifieurs séparés** (*faux tôt vs vrais*, *pièges vs vrais*, et à titre diagnostique *pièges vs faux tôt*) incluant, en plus des n-grammes avec `NUM`, **des descripteurs numériques élémentaires** : $\lfloor\log_{10}(1+|x|)\rfloor$, indicatrices $x \in \{0,1,2\}$, signe, longueur en jetons et profondeur de parenthésage.
* Remplacer le seuil unique $\text{AUC} \le 0{,}75$ par un double critère aligné sur votre test :
  1. **$\max_{\text{strate}} \text{Rappel}@(\text{FPR} \le 0{,}05) < 0{,}15$** (borne haute de l'IC à 95 % sur les 40+ graines strictement sous votre marge de 0,20, idéalement $\le 0{,}10$) ;
  2. **$\max_{\text{strate}} \overline{\text{AUC}} \le 0{,}65$** en moyenne inter-graines.

---

### 3. Équité de la règle (a) entre les deux bras et ce qui reste mesurable

**Telle que décrite dans le cadre, la règle (a) n'est pas équitable.** Elle souffre d'une asymétrie **procédurale** (corrigeable) et d'une asymétrie **mathématique** (irréductible).

**1. Asymétrie procédurale (biais de protocole massif si non corrigé) :**
* Dans votre description, *« tout contre-exemple avancé par le bras avec outil est vérifié en arithmétique exacte »*, tandis que le bras nu *« rend un verdict ; il peut citer une valeur »* (formulation optionnelle, sans vérification exacte explicitement branchée). Si l'on exige un contre-exemple vérifié sans **imposer dans la consigne du bras nu de fournir obligatoirement un témoin explicite** et sans **passer ce témoin au même vérificateur exact**, le rappel du bras nu est mécaniquement écrasé vers 0 par simple défaut de format.
* **Piège caché sur les 75 vrais (fausses alarmes) :** Sur un énoncé **vrai**, aucun contre-exemple vérifié ne peut exister par définition mathématique ! Si la règle (a) redéfinit « déclarer faux » comme « déclarer faux + contre-exemple vérifié » partout, **le taux de fausses alarmes tombe mécaniquement à 0/75 pour les deux bras**, rendant la contrainte $\text{FPR} \le 0{,}10$ et les 75 vrais totalement caducs. Pour garder un contrôle valide, les fausses alarmes sur les 75 vrais doivent continuer de compter **tout verdict « faux » prononcé** (vérifié ou non).
* *(Notons au passage une autre asymétrie déjà présente hors règle (a) : le bras avec outil bénéficie aussi d'un **modèle relecteur d'une autre famille** et de plusieurs tours de réflexion, contre un seul appel sans relecture pour le bras nu — l'effet mesuré est donc celui du couple « Python + relecture croisée », pas de Python seul.)*

**2. Asymétrie mathématique (même après symétrisation de la consigne et du vérificateur) :**
* L'hypothèse initiale porte sur un **problème de décision** (*repérer qu'un énoncé est faux*). La règle (a) le remplace par un **problème de recherche constructive de témoin exact**.
* Or un modèle sans outil peut légitimement démontrer qu'une borne $\forall t,\, E(t) < c$ est fausse **sans pouvoir calculer arithmétiquement le témoin exact** $t_0 \in [N, 3N]$ (croissance asymptotique, contradiction de parité ou de signe, ordre de grandeur, résidu modulaire) — là où le calcul mental échoue forcément sur des entiers ou modules un peu grands. Sous la règle (a), une démonstration déductive juste du bras nu vaut **zéro**.

**Que reste-t-il de mesurable sous la règle (a) (une fois symétrisée) ?**
* **Ce qui reste proprement mesuré :** le **gain de capacité constructive** procuré par l'agent outillé ($\text{Rappel}_{\text{témoin}}(\text{Outil}) - \text{Rappel}_{\text{témoin}}(\text{Nu})$), pratiquement **immunisé contre l'effet de forme** sur le score (deviner au style qu'un énoncé est un piège ne permet pas d'inventer un $t_0 > N$ qui passe la vérification exacte, sauf si $t_0$ se lit trivialement dans le texte comme $c$ ou $c+1$). Sur les *faux tôt*, on mesure l'avantage du calcul exact sur le calcul mental ; sur les *pièges*, on mesure la capacité de l'agent à chercher au-delà de $N$ ou à inverser la formule en Python.
* **Ce qui disparaît de la mesure :** toute supériorité (ou égalité) en raisonnement mathématique qualitatif/non constructif, ainsi que les cas où Python détecte une divergence ou une incohérence sans isoler un témoin exact.

---

### 4. Contrôles supplémentaires à ajouter avant de trancher (sans appel de modèle)

Quatre vérifications purement programmatiques, exécutables en quelques secondes sur vos 42 graines existantes, lèveront l'essentiel des inconnues :

1. **Inspection des poids du bayésien naïf et ventilation par famille de mondes :**
   * Extraire les 20 unigrammes/bigrammes ayant le plus fort rapport de vraisemblance $|\log P(w \mid \text{Faux}) - \log P(w \mid \text{Vrai})|$, calculer l'aire **séparément dans chacune des 3 familles de mondes**, et afficher la table de contingence `(identifiant de gabarit × classe de vérité)`.
   * *Pourquoi :* Au lieu de deviner pourquoi l'aire vaut 0,96, vous verrez immédiatement quel mot, opérateur ou déséquilibre de fréquence entre gabarits trahit les pièges, et si le problème vient d'une seule famille ou des trois (testant directement la faisabilité de (b)).

2. **Classifieur « non masqué » (avec traits numériques) évalué à $\text{FPR} \le 0{,}05$ :**
   * Entraîner une régression logistique rapide ajoutant aux n-grammes la taille des nombres ($\log_{10}|x|$), leur rapport à $N$, et les indicatrices `0`/`1`.
   * *Pourquoi :* Évite l'écueil inverse où vous feriez tomber le bayésien masqué `NUM` à 0,55 tout en laissant des constantes géantes qui trahissent les pièges auprès d'un LLM.

3. **Trois lignes de base déterministes de recherche de témoins (sans LLM) :**
   * Faire tourner sur les 42 graines trois petits scripts fixes passés au vérificateur exact :
     1. *Énumération naïve $t \le N$* (vérifie qu'elle résout 100 % des faux tôt et 0 % des pièges) ;
     2. *Énumération bornée en temps (ex. 1 seconde de Python au-delà de $N$, ou $t \le 3N$)* : vérifie si $3N$ est si petit que n'importe quelle boucle brute trouve tous les pièges instantanément, ou si grand qu'aucune énumération ne peut aboutir ;
     3. *Test des valeurs triviales du texte* ($0, 1, -1, N, N+1$, constantes littérales $c, c\pm 1$) : vérifie qu'un modèle nu ne peut pas obtenir un « contre-exemple vérifié » simplement en recopiant un nombre de l'énoncé.

4. **Calcul de puissance et d'effet plafond sur les 75 faux sous la règle (a) :**
   * Avec $n = 75$ faux et une **marge minimale de 0,20** dans un test de score apparié ($\alpha = 0{,}05$ unilatéral ou $0{,}025$), franchir significativement le seuil de 0,20 exige une différence de rappel **observée** d'environ **$\hat{\Delta} \ge 0{,}29$ à $0{,}33$** (typiquement $\text{SE}(\hat{\Delta}) \approx \sqrt{(p_{10}+p_{01}-\Delta^2)/75} \approx 0{,}055\text{–}0{,}063$).
   * Or les *faux tôt* ne représentent que $38/75 = \mathbf{0{,}507}$ des faux ! Si, sous la règle (a), l'agent Python se contentait d'énumérer jusqu'à $N$ (échouant sur les 37 pièges) pendant que le bras nu résout mentalement ne serait-ce que 16 *faux tôt* faciles ($t \in \{0,1,2\}$, soit $16/75 = 0{,}213$), l'écart observé plafonnerait à $0{,}507 - 0{,}213 = \mathbf{0{,}294}$ — à la limite exacte de l'échec statistique par pur effet plafond. Simuler cette courbe de puissance fixe le taux minimal de *pièges* que l'outil doit pouvoir résoudre pour que (a) soit viable.

---

### 5. Ce qui serait faux dans cette recommandation si un point du cadre était inexact

Voici cinq points précis du cadre dont l'inexactitude invaliderait une brique directe de ma recommandation :

1. **Si des appels aux modèles ont déjà été effectués (ou si un pré-enregistrement externe interdit désormais de retoucher le générateur) :**
   * Ma recommandation principale de privilégier l'option (b) *sans coût statistique* serait **fausse**. Modifier le générateur après avoir observé (même partiellement) le comportement des deux bras introduirait un biais de sélection post-hoc ; il faudrait alors geler le générateur tel quel et appliquer une version symétrisée de **(a)**.
2. **Si le remplacement des nombres par `NUM` dans votre code actuel comporte des exceptions (ex. `0` et `1` laissés en clair, nombres négatifs en `- NUM`, ou grands nombres écrits sous forme d'expressions composées `NUM ^ NUM + NUM`) :**
   * Mon diagnostic selon lequel remplacer un grand littéral par `0` ou `1` ne peut pas, à lui seul, faire baisser l'aire actuelle du bayésien naïf serait **faux** : cette seule modification (telle que suggérée en (b)) pourrait alors suffire à faire chuter fortement l'aire mesurée.
3. **Si la structure mathématique d'au moins une des trois familles lie intrinsèquement la vérité au gabarit syntaxique :**
   * Par exemple, si dans un monde fini d'une de vos familles, toute formule dépassant un seuil pour la première fois dans $[N, 3N]$ exige *nécessairement* un degré algébrique ou des opérateurs absents des énoncés vrais du même monde, alors ma cible d'abaisser l'aire vers $\le 0{,}65$ par simple appariement de gabarits et constantes nommées serait **inatteignable** sans changer la définition mathématique de cette famille (forçant le repli sur (a)).
4. **Si le bras nu reçoit en réalité déjà une consigne exigeant un contre-exemple explicite passé au même vérificateur exact (tandis que les fausses alarmes restent comptées sur tous les verdicts « faux ») :**
   * Ma critique d'iniquité *procédurale* et de dégénérescence du taux de fausses alarmes sur les 75 vrais en section 3 serait **caduque** ; seules resteraient vraies la distorsion *mathématique* (décision vs construction de témoin) et la tension sur la puissance statistique si les pièges ne sont pas résolus au-delà de $N$.
5. **Si les 150 énoncés (ou tous les énoncés d'un même monde) sont soumis groupés dans une même fenêtre de contexte au lieu d'appels strictement indépendants par énoncé :**
   * Ma nuance en section 2 selon laquelle le classifieur supervisé surestime ce qu'un appel LLM isolé peut exploiter (faute d'accès aux fréquences relatives des gabarits) serait **fausse** : en voyant plusieurs énoncés ensemble, un LLM peut comparer leurs formes en contexte et exploiter exactement les mêmes déséquilibres de fréquence que le bayésien naïf.