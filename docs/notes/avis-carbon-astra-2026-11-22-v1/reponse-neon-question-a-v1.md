### 1. Recommandation et niveau de confiance

**Recommandation : une option (b) reformulée et séquencée — appelons-la (b') : diagnostic immédiat sans appel de modèle $\to$ refonte structurelle du générateur par appariement de gabarits (et de distributions numériques) $\to$ remplacement de l'instrument de détection de l'effet de forme, le tout *avant* de lancer les LLM.** En parallèle, conserver une version **corrigée et symétrisée de (a)** non pas comme remplacement de l'hypothèse principale dès aujourd'hui, mais comme **critère secondaire systématique** (et critère de repli documenté si le diagnostic prouve qu'une famille de mondes ne peut pas être débarrassée de son effet de forme).

**Pourquoi écarter (c) :** Relever le seuil *après* avoir observé une aire entre 0,939 et 0,982 sur 42 graines revient à déplacer la cible a posteriori. Surtout, une aire de ~0,96 obtenue par un bayésien naïf **aveugle aux valeurs numériques** (puisque tout nombre est remplacé par `NUM`) révèle une quasi-séparabilité lexicale et syntaxique entre vrais et faux. Aucun seuil défendable ne peut qualifier un tel signal de négligeable.

**Pourquoi ne pas appliquer (a) dès maintenant :**
1. **Aucun appel de modèle n'a encore été effectué.** On est toujours dans la phase de mise au point de l'appareil expérimental (le générateur a d'ailleurs déjà été révisé une fois). Corriger un biais massif *avant* la collecte ne viole pas la rigueur du protocole ; à l'inverse, lancer l'expérience sur une banque dont on sait qu'elle fuit à 0,96 gaspille le budget d'inférence et produit des résultats fragiles.
2. Comme détaillé en section 3, la règle (a) change profondément la question mesurée, crée une asymétrie forte entre les deux bras, et **ne supprime même pas totalement l'effet de forme pour le bras avec outil**.

**Pourquoi (b) telle que suggérée dans la parenthèse ne suffit pas (d'où (b')) :**
Il y a un point décisif dans le dispositif actuel : le classifieur remplace **chaque nombre par le même jeton `NUM`**. Par conséquent, remplacer un grand littéral par `0` ou `1` (qui deviennent eux aussi `NUM`) **ne change rigoureusement rien** à ce que voit le bayésien naïf ! (Seul le remplacement par une constante *nommée* du monde modifie le jeton.)
De plus, la première révision — qui consistait déjà à ajouter des vrais et des faux tôt « de même forme que les pièges » — n'a presque pas fait baisser l'aire (0,96–0,97 $\to$ 0,939–0,982). Continuer à retoucher le générateur à l'aveugle risque d'échouer pour la même raison. Il faut d'abord **identifier exactement ce que capte le classifieur** (proportions déséquilibrées entre gabarits, existence de gabarits exclusivement vrais, opérateurs ou mots-clés résiduels, déséquilibre entre les trois familles de mondes), puis imposer un **appariement strict par construction** : chaque squelette syntaxique (dans chaque famille de mondes) doit produire des vrais et des faux dans des proportions identiques, et avec des distributions de grandeurs numériques comparables (pour bloquer aussi les indices numériques que le bayésien naïf ne voit pas).

**Niveau de confiance : ~80 %** (très élevé, > 90 %, pour rejeter (c) et exiger un diagnostic avant de lancer les modèles ; autour de 80 % sur le succès complet de (b') dans les trois familles, car la faisabilité mathématique d'apparier parfaitement les pièges sans dénaturer les mondes reste à confirmer empiriquement).

---

### 2. Le seuil de 0,75 est-il un bon instrument ? Que mettre à la place ?

**Non.** L'instrument actuel cumule quatre défauts conceptuels et statistiques. Je ne le conserverais pas tel quel.

#### Les quatre faiblesses de l'instrument actuel

1. **Choix de l'aire ROC (AUC) et angle mort des caractéristiques :**
   - *Décalage avec le protocole expérimental :* L'AUC intègre sur tous les taux de fausses alarmes ($\text{FPR} \in [0,1]$) et ne dépend que des **rangs**, pas des probabilités. Or l'expérience impose une contrainte stricte sur la zone de faible FPR ($\text{FPR} \le 0,10$) et teste un écart de rappel $\ge 0,20$.
   - *Angle mort numérique (faux vert) :* En écrasant tous les nombres sur `NUM`, la sonde est **aveugle aux grands littéraux, grands modules premiers et bornes artificielles**, alors que les LLM les lisent en clair. Un générateur pourrait passer sous 0,75 au bayésien naïf tout en restant trivialement décodable à l'œil nu par les magnitudes numériques.
   - *Écart supervisé vs zero-shot (faux rouge partiel) :* Inversement, un classifieur supervisé apprend des corrélations arbitraires propres au générateur qu'un LLM *zero-shot*, lisant énoncé par énoncé sans connaître les proportions, n'exploite pas nécessairement dans le même sens — même si des déséquilibres de gabarits perturbent quand même ses a priori de vraisemblance.

2. **La règle « plus grande des deux strates » crée une amplification mécanique :**
   Le classifieur est entraîné sur *(faux tôt + pièges) contre vrais*, mais évalué séparément sur *pièges contre tous les vrais* et *faux tôt contre tous les vrais*. Or, parce que l'AUC ne regarde que les rangs, **un déséquilibre quasi nul entre gabarits suffit à faire franchir 0,75 !**
   *Exemple chiffré sur les effectifs du protocole (75 vrais, 38 faux tôt, 37 pièges) :*
   - Gabarit A : 37 pièges et 35 vrais $\Rightarrow P(\text{faux}\mid A) = 51{,}4\,\%$.
   - Gabarit B : 38 faux tôt et 40 vrais $\Rightarrow P(\text{faux}\mid B) = 48{,}7\,\%$.
   L'AUC **globale** (tous faux vs tous vrais) vaut **0,513** — l'effet de forme est pratiquement nul. Pourtant, comme le classifieur attribue systématiquement un score légèrement plus élevé à A qu'à B, **l'AUC « pièges contre tous les vrais »** vaut :
   $$\frac{40 + 0{,}5 \times 35}{75} = \mathbf{0{,}767} > 0{,}75.$$
   Même à 50/50 exact (37 pièges / 37 vrais en A, 38 faux tôt / 38 vrais en B), un simple basculement de bruit d'estimation donne déjà $\max(\text{AUC}) \approx 0{,}753$. En outre, prendre le `max` introduit un biais positif de sélection et masque quelle strate fuit.
   *Nuance cruciale :* Cet artefact mécanique plafonne vers ~0,75 sous équilibre ; il **ne peut pas expliquer** les valeurs de **0,939 à 0,982** observées sur 42 graines (qui impliquent qu'un faux d'au moins une strate surclasse ~95 % des vrais — donc un vrai déséquilibre massif).

3. **La valeur de 0,75 est paradoxale :**
   - Sur une **AUC globale**, 0,75 est en réalité **trop permissif** : sous un modèle binormal standard, $\text{AUC} = 0,75$ correspond à une séparation $d \approx 0,95$, ce qui donne déjà un **rappel d'environ 37 % à $\text{FPR} = 10\,\%$** (soit $+27$ points au-dessus du hasard, davantage que la marge minimale de $+0,20$ visée par l'expérience !).
   - Sur le **`max` des AUC stratifiées**, 0,75 est au contraire **trop sensible** aux déséquilibres mineurs montrés ci-dessus.

4. **L'absence d'intervalle de confiance :**
   Sur une graine d'essai d'environ 30 vrais (et ~15 faux par strate), l'erreur-type d'une AUC autour de 0,75 (approximation de Hanley-McNeil) est d'environ **0,08**, soit un IC à 95 % proche de **$[0{,}59 ; 0{,}91]$** (et encore **$[0{,}65 ; 0{,}85]$** sur les 150 énoncés réels). Sur les données actuelles, ce n'est pas l'absence d'IC qui gêne (42 graines toutes $\ge 0{,}939$ lèvent tout doute), mais pour une **règle de décision future** près du seuil, décider sur un point estimé unique sans IC est statistiquement incontrôlable.

#### Ce que je mettrais à la place

Un **protocole d'audit à trois niveaux**, calculé *sans appel de modèle* sur un **grand pool de graines du générateur** (ex. 50 à 100 graines, avec validation croisée par groupes de mondes et IC bootstrap groupé par monde) **puis vérifié sur l'échantillon final de 150 énoncés** :

1. **Invariant structurel de génération (contrôle déterministe) :** vérifier que, dans chaque gabarit et chaque famille de mondes, la proportion de vrais et de faux est équilibrée (ex. entre 45 % et 55 %). C'est plus direct et moins trompeur que n'importe quel classifieur.
2. **Deux sondes complémentaires :**
   - *Sonde lexicale/syntaxique* : bayésien naïf + régression logistique régularisée sur unigrammes/bigrammes (avec `NUM`).
   - *Sonde numérique et structurelle* : régression logistique ou arbres boostés sur des descripteurs des nombres et de la forme (ordre de grandeur $\log_{10}(|x|+1)$, présence de `0`/`1`, primalité, rapport aux constantes du monde, nombre de littéraux, longueur/profondeur syntaxique).
3. **Métriques alignées sur l'expérience, avec IC :**
   - **AUC globale** (tous faux vs tous vrais) **et AUC intra-gabarit** (ou en comparant chaque strate fausse uniquement aux vrais de *ses* gabarits).
   - **Rappel à $\text{FPR} \le 0,10$** (directement relié aux contraintes de l'expérience) et **perte logarithmique / précision équilibrée calibrée**.
   - **Critère de passage (ex. sur la borne haute de l'IC 95 % du générateur) :** AUC globale $\le 0,60$ (qui borne le rappel binormal à $\text{FPR}=0,10$ autour de ~18 %) **et** rappel à $\text{FPR} \le 0,10$ au plus de **0,20** (excès $\le 0,10$ par rapport au hasard, moitié de la marge cible), sur les deux sondes.

---

### 3. La règle (a) est-elle équitable entre les deux bras ? Que reste-t-il de mesurable ?

**Non, la règle (a) n'est pas équitable**, et sa formulation recèle une ambiguïté critique dont les **deux interprétations** biaisent la comparaison — en sens contraires :

#### Lecture 1 : La règle s'applique aux deux bras (un « faux » ne compte pour aucun bras sans contre-exemple vérifié exactement)
- **Asymétrie procédurale :** Tel que décrit, seul le bras avec outil fait vérifier ses contre-exemples en arithmétique exacte (« le bras nu rend un verdict ; il peut citer une valeur, mais n'exécute aucun calcul »). Sans consigne explicite demandant un témoin structuré au bras nu et sans passage par le même vérificateur exact, le bras nu est mécaniquement écrasé vers 0.
- **Asymétrie conceptuelle même si on symétrise le vérificateur :** L'hypothèse initiale porte sur la **détection d'énoncés faux**. Or un humain ou un LLM nu peut légitimement réfuter un énoncé par un argument analytique (parité, monotonie, croissance, contradiction) sans exhiber un témoin concret — surtout pour des pièges dont le premier contre-exemple est entre $N$ et $3N$. Exiger un contre-exemple numérique exact tout en interdisant tout calcul au bras nu transforme un test de *détection mathématique* en un test de *calcul arithmétique effectif*, taillé sur mesure pour le bras avec outil.
- **Neutralisation du contrôle des fausses alarmes :** Un énoncé vrai n'ayant aucun contre-exemple, le vérificateur exact impose mathématiquement **$\text{FPR} = 0$** sur les 75 vrais. La garde-fou $\text{FPR} \le 0,10$ devient vide (elle mesure la fiabilité du vérificateur, plus celle de l'agent), à moins de continuer à l'appliquer séparément sur les verdicts bruts.

#### Lecture 2 : La règle ne s'applique qu'au bras avec outil (contre-exemples vérifiés pour l'outil vs verdicts bruts pour le bras nu)
- **Asymétrie inverse, défavorable au bras avec outil :** On compare des réfutations certifiées (sans crédit pour les preuves sans témoin) aux verdicts bruts du bras nu (qui conserve le bénéfice de ses intuitions et des raccourcis de forme).
- **Risque grave d'effet plafond :** Si l'effet de forme (AUC ~0,96) permet au bras nu d'obtenir par exemple 0,75 ou 0,80 de rappel sur ses verdicts, alors battre ce score de $+0,20$ *uniquement avec des contre-exemples vérifiés* exige 0,95 à 1,00 de contre-exemples trouvés (y compris sur quasi tous les pièges au-delà de $N$), ce qui risque de rendre le test impuissant même si l'outil apporte un avantage majeur.

#### Un angle mort commun aux deux lectures : l'effet de forme biaise encore le bras avec outil
Même si l'on ne compte que les contre-exemples vérifiés, un effet de forme de 0,96 n'est pas neutralisé : **il sert d'oracle d'allocation d'effort de recherche**. Si la forme d'un énoncé « trahit » un piège, le bras avec outil sait qu'il ne doit pas s'arrêter à l'énumération jusqu'à $N$ et qu'il vaut la peine de chercher jusqu'à $3N$ ou davantage — ce qui gonfle artificiellement son rappel certifié sur les pièges par rapport à des énoncés sans signature de forme.

#### Que reste-t-il de mesurable sous la règle (a) ?
- **Sous Lecture 1 (symétrisée + contrôle FPR maintenu sur verdicts bruts) :** On ne mesure plus « quel bras repère mieux le faux », mais **le gain incrémental de réfutation certifiée** (la capacité supplémentaire du bac à sable à produire des témoins exacts, notamment au-delà du calcul mental et au-delà de $N$). C'est une mesure parfaitement rigoureuse et utile **comme critère secondaire ou mécanistique**, mais plus étroite que l'hypothèse initiale.
- **Sous Lecture 2 :** Seulement une **borne inférieure ultra-conservatrice** (les réfutations certifiées de l'outil dépassent-elles de $+0,20$ tous les verdicts du bras nu ?). Un succès serait très probant ; un échec serait ininterprétable.
- *(À exclure absolument :)* Une troisième lecture consistant à restreindre la comparaison au sous-ensemble d'énoncés où l'outil a trouvé un contre-exemple serait une **sélection post-traitement** statistiquement invalide (le bras avec outil y aurait 100 % de rappel par construction).

---

### 4. Mesures et contrôles supplémentaires (sans appel de modèle) avant de trancher

Avant de modifier le générateur ou de figer le seuil, j'exécuterais ces cinq contrôles rapides (coût LLM nul) :

1. **Décomposition complète de l'AUC actuelle et inspection des poids du bayésien naïf :**
   - Calculer séparément sur les 42 graines : `AUC(faux tôt vs vrais)`, `AUC(pièges vs vrais)`, **`AUC globale(tous faux vs tous vrais)`**, **`AUC(pièges vs faux tôt)`**, ainsi que le **rappel à $\text{FPR} \le 0,10$**.
   - Extraire les **20 unigrammes et bigrammes aux plus forts rapports de cotes (log-odds)** dans chaque classe. En quelques minutes, on sait si le signal vient d'un opérateur (`<` vs `<=`), d'un mot-clé, du jeton `NUM` ou d'une fonction propre à un gabarit.

2. **Tableaux de contingence et séparation « composition vs fuite interne » :**
   - Dresser les tableaux *(gabarit $\times$ strate)* et *(famille de mondes $\times$ strate)*, et calculer l'AUC **séparément dans chacune des trois familles de mondes** (il se peut qu'une seule famille explique 0,96 et que les deux autres soient déjà saines !).
   - Comparer deux modèles : (i) un classifieur utilisant **uniquement l'identifiant du gabarit + la famille** (sans le texte), et (ii) le bayésien naïf **à l'intérieur de chaque gabarit** (ou après pondération équilibrant les gabarits entre vrais et faux). On distingue ainsi immédiatement un simple déséquilibre de proportions (facile à réparer) d'une fuite syntaxique interne au gabarit.

3. **Sonde numérique et structurelle (sans masquage `NUM`) :**
   - Entraîner (en validation croisée groupée par mondes) un classifieur léger sur les grandeurs numériques et la structure (nombre de littéraux, max/médiane de $\log_{10}(|x|+1)$, présence de `0`/`1`, primalité des modules, ratio entre constantes de l'énoncé et constantes du monde, longueur en jetons, profondeur de l'expression), seul puis combiné aux n-grammes. Cela révèle si les nombres trahissent eux aussi les pièges — et donc si l'idée des « bornes naturelles » de l'option (b) est indispensable ou secondaire.

4. **Vérification du pipeline de validation croisée et de l'échelle d'essai :**
   - S'assurer que la CV à 4 plis est bien stratifiée par famille de mondes (sans fuite de conventions de nommage ni de prétraitement) et que le texte lu par la sonde est **strictement identique** à celui présenté aux LLM.
   - Vérifier la cohérence d'échelle entre les graines d'essai (**~30 vrais par graine**) et le banc expérimental réel (**75 vrais / 38 faux tôt / 37 pièges**), en calculant l'AUC sur un pool reproduisant exactement les effectifs et proportions cibles, avec IC bootstrap groupé par monde.

5. **Profilage des contre-exemples minimaux (sanité de la difficulté) :**
   - Sur les 42 graines, mesurer la distribution du plus petit contre-exemple : quelle part des « faux tôt » est triviale ($t \in \{0, 1, 2\}$, donc accessible de tête au bras nu) ? Pour les pièges, quel est le coût de calcul Python entre $N$ et $3N$ ? Cela permet d'anticiper la faisabilité réelle de la vérification exacte et la pertinence de l'écart $N$ vs $3N$.

---

### 5. Ce qui serait faux dans cette recommandation si un point du cadre était erroné

Plusieurs éléments de ma recommandation reposent sur des points précis du cadre ; s'ils étaient inexacts, la conclusion devrait changer :

1. **Si les indices détectés par le bayésien naïf ne se transfèrent pas à un LLM *zero-shot* mono-énoncé :**
   Ma recommandation suppose qu'une AUC de 0,94–0,98 représente un risque sérieux d'exploitation (ou de biais de taux de base) par les LLM. Si le diagnostic (section 4) montrait que le NB n'exploite que des conventions lexicales arbitraires et sémantiquement neutres — et que chaque énoncé est soumis au LLM isolément, sans contexte d'autres énoncés du même monde — alors le risque *zero-shot* serait bien moindre que ne le suggère 0,96, et un lourd travail de refonte (b') pourrait être disproportionné (même s'il resterait sain pour la validité générale du benchmark).

2. **Si l'appariement des gabarits est mathématiquement impossible dans une famille sans rendre les vrais triviaux :**
   Je suppose que l'on peut créer, dans les trois familles, des vrais de même gabarit que les pièges qui restent non triviaux. Si, en pratique, les seuls vrais coulés dans le gabarit des pièges étaient des bornes si lâches que le bras nu les reconnaîtrait immédiatement comme vraies (ou étaient impossibles à certifier), alors forcer (b') introduirait un **nouveau biais** (baisse artificielle des fausses alarmes). Il faudrait alors soit retirer/remplacer cette famille, soit assumer d'emblée un changement d'hypothèse vers la réfutation certifiée symétrique.

3. **Un point crucial du cadre qui limite la portée même si (b') réussit : la confusion du « modèle relecteur d'une autre famille » :**
   Le bras avec outil dispose non seulement d'un bac à sable Python, mais aussi d'une **relecture par un modèle d'une autre famille**, absente du bras nu (« un seul appel »). Même si (b') ramène l'effet de forme à AUC = 0,50, **l'expérience ne mesurera pas l'effet isolé de l'outil de calcul**, mais l'effet confondu *(outil Python + boucle multi-étapes + relecture par un second modèle)*. Si ce relecteur apporte l'essentiel du gain (ou filtre de lui-même tout « faux » non prouvé), alors la priorité méthodologique ne serait pas seulement le générateur, mais aussi l'ajout d'un bras contrôle « nu + même relecteur » (ou le retrait du relecteur).

4. **Si le protocole est déjà gelé (pré-enregistrement strict ou contrainte de calendrier) :**
   Ma recommandation suppose qu'on peut encore réviser le générateur et la règle de seuil avant la collecte LLM. Si le protocole était contractuellement ou scientifiquement verrouillé après l'audit sur 42 graines (ou si le délai interdisait toute nouvelle itération sur le générateur), modifier le seuil ou le générateur serait irrecevable : il faudrait exécuter strictement la règle (a) prévue (en présentant ses limites d'équité dans la discussion) et réserver (b') à une seconde expérience.

5. **Si la vraie question métier est la « réfutation certifiée » et non la « détection » :**
   Si l'usage cible de l'agent est en réalité la production de **contre-exemples vérifiables** (un verdict « faux » non prouvé étant jugé sans valeur pratique), alors ma critique conceptuelle de la Lecture 1 de (a) tombe en grande partie : l'exigence de contre-exemple vérifié devient la bonne définition de la tâche (il resterait tout de même à symétriser la vérification sur le bras nu, à surveiller le FPR brut et à corriger l'effet de forme comme oracle de recherche au-delà de $N$).

6. **Si les 0,939–0,982 provenaient d'un bug dans le script de la sonde plutôt que du générateur :**
   Je suppose que la validation croisée groupée par mondes et l'extraction de texte sont exemptes de fuite. Si la sonde voyait un métadonné, un formatage propre à la strate ou une fuite entre plis qui n'existe pas dans les prompts réellement envoyés aux LLM, alors réviser le générateur (b') serait inutile — d'où l'intérêt de commencer par l'inspection des poids et du pipeline (section 4) avant toute réécriture.