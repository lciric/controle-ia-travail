Voici la proposition **C** pour le Tour III.1 du Collisionneur épistémique.

*Note d'intégrité (Règle 2) : La pièce jointe d'origine de Gemini (`27841389…`, mentionnée dans la pièce A) et les résultats d'exécution du plan P sont absents des pièces transmises (seul le plan P figé avant lancement à `de4dbf6` est fourni) ; leur contenu n'est pas inventé.*

---

# (a) Ce que la question suppose sans que ce soit établi (et réponse au point 1 sur l'état de l'art)

### 1.1 Présupposés non établis dans la question et les pièces

1. **Qu'une fusion par modèle de langue de deux fiches parentes produise un gain prédictif réel au-delà du nul augmenté.** Statut : **HYPOTHÈSE** (explicitement listée comme non établie dans la pièce R1). Toute l'architecture d'allocation suppose que le taux de base $v(s)$ n'est pas identiquement nul dans la réalité.
2. **Que le « juge v1 » (nul augmenté des parents, de leurs mélanges et enveloppes, marge $2\delta_0 = 0,02$) bloque tous les tricheurs scriptés ou les filles dégénérées.** Statut : **OBSERVÉ-NON-AUDITÉ** dans son principe, mais avec une faille connue (**RAPPORTÉ** dans la pièce P : *« Le trou connu du critère des filles ("parent + loi aveugle") est exclu de cet essai, et dit »*). Si une fille combine un parent fort et du bruit éligible qui passe ce trou, son taux de survie sous l'hypothèse fausse dépasse $\alpha$.
3. **Que la similarité de domaine $s \in [0 ; 0,8]$ soit mesurable de façon lisse, non dégénérée et invariante à l'échelle sur les fiches d'hypothèses.** Statut : **HYPOTHÈSE**. Dans la pièce R2 (**RAPPORTÉ**), le passage de TF-IDF aux fréquences brutes a fait passer les cosinus inter-domaines de $(0,11 / 0,009)$ à $(0,28 / 0,03)$. Une fenêtre rigide $[0,12 ; 0,26]$ dépend entièrement de la normalisation lexicale choisie : ce qui est dans la « bande du milieu » en fréquences brutes tombe à $0,009$ (hors fenêtre) en TF-IDF.
4. **Que maximiser l'entropie du verdict ($p \approx 0,5$) dans l'allocateur à fenêtre (pièce P) aide à maximiser le nombre de découvertes vraies par dollar.** Statut : **HYPOTHÈSE** (et mathématiquement contradictoire avec l'objectif). Dans le plan P (**RAPPORTÉ**), le monde « cloche » a une probabilité constante $v(s) = 0,5$ sur toute la fenêtre $[0,12 ; 0,26]$. Mais si $v(s)$ variait dans la fenêtre (ex. un pic à $0,8$ au centre et $0,5$ aux bords), l'allocateur de Gemini défini dans P choisirait *systématiquement les bords* ($p \approx 0,5$, entropie maximale) au détriment du centre ($p = 0,8$, espérance maximale).
5. **Que le budget par génération ($B = 40$ tests dans P) permette à un bandit en ligne à 8 cases (Thompson ou tri glouton) de converger mieux qu'un a priori structuré.** Statut : **HYPOTHÈSE**. Avec 40 tirages répartis sur 8 cases de largeur $0,1$, chaque case reçoit en moyenne 5 tirages. Pour une probabilité de promotion de $0,5$ contre $0,05$, la variance binaire d'un prieur $\text{Bêta}(1,1)$ sur les 15 à 20 premiers tirages domine le signal.

### 1.2 Ce qui est établi dans la littérature (Réponse au point 1)

* **Sur les combinaisons de revues citées au sein d'un article :**
  * Uzzi, B., Mukherjee, S., Stringer, M., & Jones, B. (2013), « Atypical Combinations and Scientific Impact », *Science*, vol. 342, n° 6157, pp. 468–472. Statut des chiffres : **RAPPORTÉ** (lus par transcription dans la pièce A, non vérifiés sur PDF empreinté). Sur 17,9 millions d'articles du Web of Science, la conventionnalité est mesurée par la médiane du score $z$ des paires de revues co-citées dans la bibliographie d'un *même* article, et la nouveauté par le 10ᵉ centile de ce score $z$. Les articles combinant forte conventionnalité et forte nouveauté ont un taux de « hits » (articles dans les 5 % les plus cités) de **9,11 pour 100** (contre 5 pour 100 en moyenne), tandis que ceux à faible conventionnalité et forte nouveauté sont à **5,33 pour 100**.
  * **Ce que cela n'établit pas (HYPOTHÈSE) :** Que la distance entre *deux articles parents* suive une courbe en cloche. Chez Uzzi et al. (2013), la relation n'est pas une fenêtre intermédiaire sur un axe unique (« ni trop proche ni trop loin »), c'est la **conjonction** de deux extrêmes sur la distribution interne des références d'un article : une médiane très conventionnelle *et* une queue (10ᵉ centile) très atypique.
* **Sur la distance interdisciplinaire et l'impact / le financement :**
  * Wang, J., Veugelers, R., & Stephan, P. (2017), « Bias against novelty in science: A cautionary tale for users of bibliometric indicators », *Research Policy* (pages exactes : référence à vérifier). Montre que les combinaisons nouvelles de revues ont une variance d'impact plus élevée, pénalisée à court terme (3 ans) mais récompensée à long terme et dans des revues hors du domaine d'origine. Statut : **RAPPORTÉ** (littérature).
  * Bromham, L., Dinnage, R., & Hua, X. (2016), « Interdisciplinary research has consistently lower funding success », *Nature*, vol. 534 (pages exactes : référence à vérifier). Mesure une relation monotone négative entre la distance phylogénétique des disciplines d'un projet et son succès de financement. Statut : **RAPPORTÉ** (littérature).
  * Leahey, E., Beckman, C. M., & Stanko, T. L. (2017), « Prominent but Less Productive: The Impact of Interdisciplinarity on Scientists' Research », *Administrative Science Quarterly* (pages exactes : référence à vérifier). Montre un compromis variance / productivité, pas une fenêtre magique universelle. Statut : **RAPPORTÉ** (littérature).
* **Sur le corpus réel du programme (pièce T, métadonnées arXiv 2003–2016) :**
  * Statut : **RAPPORTÉ** (pièce T, vérifié par empreintes). Le taux de base de cooccurrence future entre termes spécifiques de champs différents varie fortement selon la paire de champs : `cs – physique` est à **0,76 %** $[0,72 ; 0,80]$, `physique – q-bio` à **0,47 %** $[0,38 ; 0,58]$, `math – cs` à **0,36 %** $[0,28 ; 0,46]$, `math – physique` à **0,17 %** $[0,16 ; 0,18]$, et `math – q-bio` à **0,11 %** $[0,03 ; 0,40]$.
  * Surtout, à l'intérieur de ces paires inter-champs, la prédiction de lien par **allocation de ressources (RA)** atteint **10,65 %** $[10,08 ; 11,23]$ de précision à 10 000 (et **28,40 %** à 1 000), contre **0,22 %** pour le tirage stratifié (ST). Or, l'allocation de ressources $\text{RA}(A, C) = \sum_{B \in N(A) \cap N(C)} \frac{1}{\text{deg}(B)}$ est une fonction **strictement croissante** de la densité de voisinage partagé (pondérée par la rareté des intermédiaires). Elle prouve que, conditionnellement au fait que deux termes appartiennent à des champs distincts, ce sont les paires ayant le **plus fort couplage structurel local** qui forment des ponts réalisés, et non une bande médiane de distance.

---

# (b) La bonne variable et le bon objectif d'allocation (Réponse aux points 2 et 3)

### 2.1 Pourquoi la similarité de domaine $s$ est la mauvaise variable, et comment mesurer la bonne sur nos fiches

Dans le pôle (pièce C, **RAPPORTÉ**), une fiche d'hypothèse contient : un énoncé, une **prédiction signée et chiffrée** (qui engage une loi prédictive $\hat{P}(Y \mid X)$ des issues $Y$ sachant les traits $X$), une métrique, un **nul**, des **domaines**, des **opérateurs** et des **contraintes de validité**. Un parent survivant n'est pas un nuage de mots : c'est un **prédicteur testé** sur un espace de traits.

La similarité lexicale de domaine $s = \cos(d_A, d_B)$ confond deux géométries orthogonales :
1. **La distance sémantique de surface** (le vocabulaire du domaine d'application).
2. **La complémentarité fonctionnelle des lois prédictives** (ce que les parents prédisent sur les traits $X$).

Comme l'a démontré l'essai R2 (**RAPPORTÉ**), un noyau sur les seuls vecteurs de domaine $d_i$ échoue (−4,8 points contre le stratifié), tandis que la marche sur les opérateurs rares (d1) ou l'allocation de ressources (RA dans T) capture les vrais ponts. Sur des fiches d'hypothèses, nous disposons de bien mieux que des étiquettes : nous avons les **signatures prédictives** et la **décomposition de l'information sur l'urne de calibrage**.

Voici les trois variables calculables mécaniquement à coût quasi nul *avant* d'allouer le budget du juge frais (en utilisant uniquement les 50 tirages de calibrage déjà prévus dans la pièce P, ou une table d'instances communes) :

1. **Le couplage d'opérateurs pondéré par l'allocation de ressources ($\text{RA}_{\text{op}}(A, B)$) :**
   Sur le graphe biparti Fiches × Opérateurs/Variables, $\text{RA}_{\text{op}}(A, B) = \sum_{o \in O_A \cap O_B} \frac{1}{\text{freq}(o)}$. C'est la transposition directe du gagnant de la pièce T (**RAPPORTÉ**) aux fiches.
2. **L'orthogonalité des résidus prédictifs ($1 - |\rho_{\text{res}}(A, B)|$) :**
   Sur un lot de calibrage commun de taille $N_{\text{cal}} = 50$ (**RAPPORTÉ** dans P), chaque parent $i \in \{A, B\}$ produit un vecteur de scores de pari ou de log-vraisemblances ponctuelles $\ell_i(x_k, y_k)$ pour $k = 1, \dots, N_{\text{cal}}$. Si $\text{corr}(\ell_A, \ell_B) \approx 1$, les deux parents captent le même signal sous deux jargons différents (jumeaux redondants : la fille ne pourra pas battre leur enveloppe de $2\delta_0$). Si $\text{corr}(\ell_A, \ell_B) \approx 0$ (ou négative par sous-populations complémentaires, comme dans le monde « Vraie » de la pièce P où A prédit la sous-population 0 et une loi neuve prédit la 1), il existe un espace de **synergie**.
3. **La marge de synergie de pré-calibrage ($\Delta_{\text{syn}}(F \mid A, B)$) :**
   Pour une fiche fille $F$ candidate (déjà formulée avec son code/loi prédictive gelée), on évalue sur un micro-échantillon de criblage (ex. $n_0 = 15$ tirages, **illustratif**, pris sur les 50 de calibrage) le gain empirique de $F$ sur l'enveloppe convexe de ses parents :
   $$\Delta_{\text{syn}}(F \mid A, B) = \frac{1}{n_0} \sum_{k=1}^{n_0} \ell_F(x_k, y_k) - \max_{\lambda \in [0,1]} \frac{1}{n_0} \sum_{k=1}^{n_0} \log\big(\lambda P_A(y_k \mid x_k) + (1-\lambda) P_B(y_k \mid x_k)\big)$$
   Si $\Delta_{\text{syn}} \le 0$, la fille est dominée par le mélange de ses parents avant même d'acheter les 200 tirages frais du juge.

*Ce que cela remplace :* La « Boucle d'or » d'Uzzi (conventionnalité + nouveauté) n'est pas une bande $s \in [0,12 ; 0,26]$ sur une seule variable ; c'est un **produit de deux variables orthogonales** : un **ancrage d'opérateur fort** ($\text{RA}_{\text{op}}(A, B) > \tau_{\text{op}}$, qui évite la chimère incompatible) **ET** une **divergence de domaine et de signature prédictive** ($s(A, B)$ faible et $|\rho_{\text{res}}(A, B)|$ faible, qui évite la redondance triviale).

### 2.2 Le bon objectif d'allocation (et pourquoi le score d'entropie de Gemini est une erreur de catégorie)

Attaquons directement la formule rapportée dans A : $\text{Score}(p) = H_2(p) \times 4p(1-p) \times \text{pénalité}$.
1. **Redondance algébrique :** Au voisinage de $p = 0,5$, l'entropie binaire en bits s'écrit par développement de Taylor $H_2(p) = 1 - \frac{2}{\ln 2}(p - 1/2)^2 + O((p-1/2)^4)$, tandis que $4p(1-p) = 1 - 4(p - 1/2)^2$. Les deux facteurs sont deux approximations concaves du même pic en $p = 0,5$. Leur produit $H_2(p) \cdot 4p(1-p)$ ne fait qu'élever la courbure au carré sans justification théorique.
2. **Confusion entre apprentissage actif de frontière et maximisation de découvertes sous budget fini :**
   Viser $p \approx 0,5$ est optimal quand l'objectif final est d'estimer une *fonction de réponse globale* sur tout l'espace (échantillonnage d'incertitude / *uncertainty sampling*). Or, dans le pôle (pièce C et pièce P, **RAPPORTÉ**), la récompense finale n'est pas la précision de la carte de calibration : c'est le **nombre de découvertes vraies promues par dollar** ($\sum_{t=1}^B \mathbb{I}\{\text{fille}_t \text{ promue et vraie}\} / B$) à l'horizon court d'une génération ($B = 40$).
   Si une strate $k$ a une probabilité de promotion estimée $\hat{p}_k = 0,75$ et une autre $\hat{p}_{k'} = 0,50$, l'allocateur entropique de Gemini (tel que codé dans P) **préfère la strate à $0,50$ et refuse de tirer la strate à $0,75$**, perdant $0,25$ découverte par dollar à chaque tirage !
3. **Comment éviter de récompenser la survie facile ?**
   Comme le relève justement la pièce A (**RAPPORTÉ**), sous le juge v1 (nul augmenté des parents + enveloppes + marge $2\delta_0$), toute fille triviale (copie ou mélange des parents) a une probabilité de promotion bornée par le niveau du test $\alpha$. **Sauf** si le juge comporte le « trou connu » mentionné dans P (« parent + loi aveugle »).
   Si une fille tricheuse passe ce trou avec une probabilité de promotion $p_{\text{triche}} > \alpha$, ni l'espérance de promotion $\hat{p}$, ni l'entropie $H_2(\hat{p})$ ne protègent l'allocateur : en fait, si $p_{\text{triche}} \approx 0,5$, l'allocateur entropique se jettera *exclusivement* sur les tricheurs !
   La seule parade rigoureuse est double :
   * **En amont (dans le juge) :** Fermer le trou « parent + loi aveugle » en exigeant que la fille batte chaque parent *individuellement sur chaque sous-population déclarée ou induite par l'arbre de partition des traits*, ou en incluant dans le nul composite le parent régularisé par l'a priori uniforme $(1-\epsilon)P_A + \epsilon U$.
   * **Dans l'allocateur :** Récompenser le bandit non pas par la simple binaire de promotion $\mathbb{I}\{\text{promue}\}$, mais par la **promotion pondérée par la sévérité tronquée** ou en soustrayant le taux de fausses promotions mesuré sur des **témoins négatifs plantés** (des filles synthétiques « parent + loi aveugle » injectées à chaque génération, conformément à la pièce C).

4. **Quel allocateur choisir et quand ?**
   * Pour un budget court ($B = 40$, réservoir $N = 300$, pièce P), un bandit à 8 cases indépendantes ($\text{Bêta}(1,1)$) souffre d'un démarrage à froid trop lent : explorer 8 cases coûte au moins 16 à 24 tirages avant de séparer $p=0,5$ de $p=0,05$.
   * La fenêtre ne doit **ni être fixée d'avance de façon rigide** (elle s'effondre si le monde est croissant, décroissant ou aux bords), **ni être apprise sans structure** par 8 cases aveugles.
   * **La solution : Échantillonnage de Thompson structuré à basse dimension (ou Gradient de Connaissance sur régression logistique quadratique).** Au lieu de 8 cases disjointes à 16 paramètres libres, on modélise le log-odds de promotion sur la distance normalisée par rang $u = \text{rang}(s)/N \in [0, 1]$ avec **3 paramètres seulement** :
     $$\text{logit}\, p(u) = \theta_0 + \theta_1 \left(u - \tfrac{1}{2}\right) + \theta_2 \left(u - \tfrac{1}{2}\right)^2$$
     Cette famille à 3 paramètres contient exactement : le monde plat ($\theta_1 = \theta_2 = 0$), le monde croissant ($\theta_1 > 0, \theta_2 \approx 0$), le monde décroissant ($\theta_1 < 0, \theta_2 \approx 0$), le monde en cloche / Boucle d'or ($\theta_2 < 0$), et le monde aux bords ($\theta_2 > 0$). Avec 3 paramètres au lieu de 8 cases indépendantes, l'information d'un tirage en $u$ met à jour toute la courbe en moins de 10 essais (**illustratif**).

---

# (c) Expériences décisives en inférence forte (Réponse au point 4)

Chaque expérience oppose deux hypothèses exclusives $H_A$ et $H_B$, sur processeur ou corpus existant, avec métrique, seuil, contrôle négatif et condition de falsification bilatérale.

## Expérience 1 (Simulation sur le banc P) : Fenêtre rigide d'entropie contre Apprentissage en ligne (et audit du plan P)

Avant de proposer une variante, nous analysons le plan P (**RAPPORTÉ**) tel qu'il est scellé, et nous prédisons un **défaut mécanique caché dans la définition du monde « cloche » de P**.
Dans P :
* $s$ est tiré uniformément sur $[0 ; 0,8]$ pour 300 filles.
* La fenêtre $[0,12 ; 0,26]$ a une largeur de $0,14$, soit $0,14 / 0,80 = 17,5\%$ du réservoir ($300 \times 0,175 = 52,5$ filles en moyenne dans la fenêtre, $\ge 40$, donc la fenêtre n'est presque jamais épuisée pour un budget de 40).
* Dans le monde « cloche » de P, $v(s) = 0,5$ sur $[0,12 ; 0,26]$ et $0,05$ ailleurs.
* **Observation critique sur les 8 cases de Thompson et du Tri dans P :** Les 8 cases de largeur $0,1$ sur $[0 ; 0,8]$ sont $[0 ; 0,1[, [0,1 ; 0,2[, [0,2 ; 0,3[, \dots, [0,7 ; 0,8]$. Or la fenêtre $[0,12 ; 0,26]$ est **à cheval sur deux cases** ($[0,1 ; 0,2[$ et $[0,2 ; 0,3[$) !
  * Dans la case 2 ($[0,1 ; 0,2[$), la cloche couvre $[0,12 ; 0,20[$, soit $80\%$ de la case : le taux vrai de la case 2 est $0,8 \times 0,5 + 0,2 \times 0,05 = \mathbf{0,41}$.
  * Dans la case 3 ($[0,2 ; 0,3[$), la cloche couvre $[0,20 ; 0,26]$, soit $60\%$ de la case : le taux vrai de la case 3 est $0,6 \times 0,5 + 0,4 \times 0,05 = \mathbf{0,32}$.
  * Même si un oracle donnait à Thompson et au Tri la vraie valeur exacte de chaque case dès $t=0$, le meilleur qu'ils puissent faire dans le monde « cloche » de P est de tirer dans la case 2 à $v = 0,41$, tandis que la fenêtre de Gemini tire par définition dans $[0,12 ; 0,26]$ à $v = 0,50$ ! Cet écart de $0,50 - 0,41 = 0,09$ découverte vraie par dollar (plus le coût d'exploration des 6 mauvaises cases sur un petit budget de 40) est un **artefact de discrétisation (désalignement de grille)** en faveur de la fenêtre dans le monde « cloche ».

Nous posons donc le duel suivant sur l'infrastructure exacte de P :

* **Hypothèse $H_A$ (Valeur intrinsèque du filtre à fenêtre + entropie) :** L'allocateur à fenêtre $[0,12 ; 0,26]$ visant l'entropie maximale bat les allocateurs qui apprennent en ligne lorsque la vérité est unimodale intermédiaire, même lorsque la cloche n'est pas une fonction indicatrice constante alignée sur $[0,12 ; 0,26]$, et sans s'effondrer catastrophiquement hors cloche.
* **Hypothèse $H_B$ (Artefact d'indicatrice et supériorité du bandit structuré) :** L'avantage de la fenêtre dans le monde « cloche » de P provient uniquement (1) du fait que la fenêtre reçoit gratuitement les bornes exactes $[0,12 ; 0,26]$ alors que les cases de largeur $0,1$ de Thompson chevauchent les bords, et (2) du fait que $v(s)$ est un plateau constant à $0,5$ dans la fenêtre (ce qui neutralise le défaut du critère d'entropie). Dès que la cloche a un pic supérieur à $0,5$ (ex. $v(s) = 0,85$ sur $[0,16 ; 0,22]$ et $0,50$ sur les flancs $[0,12 ; 0,16[\cup]0,22 ; 0,26]$) ou que l'on oppose la fenêtre à un bandit quadratique à 3 paramètres ($\text{logit}\, p(u) = \theta_0 + \theta_1 u + \theta_2 u^2$), le critère d'entropie fait perdre la fenêtre dans la cloche à pic, et la fenêtre rigide perd massivement dans les mondes « bords », « croissant » et « décroissant ».
* **Protocole et métrique :**
  1. Exécuter les 5 mondes préenregistrés de P (cloche, bords, croissant, décroissant, plat), 30 répétitions, $B = 40$, juge v1.
  2. Ajouter un 6ᵉ monde **« cloche à cœur riche »** : $v(s) = 0,85$ si $s \in [0,16 ; 0,22]$, $v(s) = 0,50$ si $s \in [0,12 ; 0,16[ \cup ]0,22 ; 0,26]$, et $0,05$ ailleurs.
  3. Ajouter un 5ᵉ allocateur : **Thompson quadratique (TQ)** (3 paramètres $(\theta_0, \theta_1, \theta_2)$ sur le rang normalisé $u$, mise à jour par approximation de Laplace à chaque pas, choix par tirage de Thompson de la fille maximisant $\hat{p}_i$).
  4. Métrique : découvertes vraies par dollar ($V / 40$), différences appariées $D_1$ (fenêtre − meilleur appris de P) et $D_{\text{TQ}}$ (fenêtre − TQ), IC à 95 % par bootstrap (10 000 tirages).
* **Contrôle négatif :** Monde « plat » ($v(s) = 0,20$ partout) et contrôle de calibration du juge : le taux de fausses promotions par test de filles fausses doit rester $\le \alpha + 2\sqrt{\alpha(1-\alpha)/N_{\text{faux}}}$.
* **Seuils et issues falsifiantes :**
  * **Falsification de $H_A$ :** Si (1) dans les mondes « bords », « croissant » et « décroissant », l'IC à 95 % de $D_1$ est entièrement sous $0$ (perte nette supérieure à $-0,15$ découverte/dollar, **illustratif**), **ET** (2) dans le monde « cloche à cœur riche », l'allocateur à fenêtre (qui chasse $p \approx 0,5$ sur les flancs) perd contre le tri par espérance et contre TQ ($D < 0$, IC sous 0). Alors l'objectif d'entropie est réfuté et la fenêtre fixe est rejetée comme règle générale (verdict de P : « à écarter » ou au mieux « sous condition d'oracle »).
  * **Falsification de $H_B$ :** Si la fenêtre bat TQ ($D_{\text{TQ}} > 0$, IC au-dessus de 0) dans les deux mondes en cloche *et* ne perd pas dans les mondes monotones/bords.

## Expérience 2 (Données réelles, rétrodiction arXiv 2003–2016 de la pièce T) : Courbe en cloche de distance contre Couplage d'opérateurs (RA)

Nous utilisons les matrices et le million de paires candidates déjà extraits et empreintés dans la pièce T (**RAPPORTÉ**, `scores-principal-v1.npz` et `issues-principal-v1.npz`, 1 000 000 de paires, 2 752 positives). Aucun téléchargement requis.

* **Hypothèse $H_A$ (Fenêtre « Boucle d'or » sur données réelles) :** Le taux de cooccurrence future (2011–2016) de deux termes candidats qui ne cooccurrent jamais en 2003–2010 suit une courbe en cloche (non monotone, maximale dans une bande intermédiaire) en fonction de la similarité contextuelle/domaine de leurs profils de documents en 2003–2010, et restreindre l'allocation de ressources (RA) à cette fenêtre $[s_{\min}, s_{\max}]$ améliore la précision à 10 000 d'au moins $+2,0$ points de pourcentage (seuil D2 de la pièce T).
* **Hypothèse $H_B$ (Monotonie du couplage structurel et redondance de la fenêtre) :** Conditionnellement à l'absence de cooccurrence directe avant 2010, la probabilité de pont futur croît de façon **monotone** avec la proximité de second ordre (mesurée par $\text{RA}$, $\text{AA}$ ou le cosinus de la distribution des co-termes en 2003–2010). Filtrer par une « bande du milieu » en écartant la tranche supérieure de similarité de profil détruit la tête de liste de RA et fait **baisser** la précision à 10 000.
* **Protocole et métrique :**
  1. Sur lesDocuments d'avant (2003–2010, pièce T), définir pour chaque terme candidat $i$ son vecteur de profil de sous-catégories arXiv (ou son vecteur de voisins normalisé $v_i$ sur le vocabulaire d'avant, strictement sans fuite temporelle) et calculer la similarité cosinus $s(A, C) = \cos(v_A, v_C)$ pour chacune des 1 000 000 de paires candidates.
  2. Découper les 1 000 000 de paires en 10 déciles $Q_1, \dots, Q_{10}$ de $s(A, C)$.
  3. Calculer le taux de ponts réalisés (2011–2016) $r_k$ dans chaque décile $Q_k$ avec son intervalle de Wilson à 95 %, ainsi que la précision à 10 000 de :
     * $\text{RA}$ global (référence connue : **10,65 %**, **RAPPORTÉ** dans T) ;
     * $\text{RA}_{\text{fenêtre}}$ : $\text{RA}$ restreint aux déciles médians $[Q_2, Q_4]$ (correspondant aux centiles 10 %–40 % de la « Boucle d'or ») ;
     * $\text{RA}_{\text{hybride}}$ : produit du rang de $\text{RA}$ (ancrage d'opérateur) et d'une pénalité sur la redondance intra-sous-catégorie.
* **Contrôle négatif :**
  1. Issues permutées (20 permutations, comme dans T) : tous les déciles et toutes les variantes doivent retomber au taux de base **0,2752 %** ($\pm 4$ erreurs-types).
  2. Réplication sur le découpage placebo 2003–2006 / 2007–2010 (`scores-placebo-v1.npz`, **RAPPORTÉ** dans T).
* **Seuils et issues falsifiantes :**
  * **Falsification de $H_A$ :** Si (1) la suite $(r_1, \dots, r_{10})$ est monotone croissante (tau de Kendall $\ge 0,8$) ou si le décile supérieur $Q_{10}$ a un taux $r_{10} \ge \max_{2 \le k \le 8} r_k$, **OU** (2) si $\text{Précision@10000}(\text{RA}_{\text{fenêtre}}) - \text{Précision@10000}(\text{RA}) < +2,0$ points (a fortiori si l'écart est négatif).
  * **Falsification de $H_B$ :** Si un décile intermédiaire $Q_k$ ($k \in \{2,\dots,8\}$) bat significativement à la fois $Q_1$ et $Q_{10}$ (intervalles de Wilson disjoints aux deux extrémités) **ET** que $\text{RA}_{\text{fenêtre}}$ bat $\text{RA}$ d'au moins $+2,0$ points sur le découpage principal et le placebo.

## Expérience 3 (Sur les fiches du pôle) : Similarité de domaine $s$ contre Synergie prédictive et Couplage d'opérateurs

Cette expérience tranche la question 2 : quelle variable sépare réellement les filles vraies des filles fausses ou triviales avant l'appel complet au juge ?

* **Hypothèse $H_A$ (Suffisance de la similarité de domaine $s$) :** Le filtre par fenêtre de similarité de domaine des parents $s \in [0,12 ; 0,26]$ sélectionne un sous-ensemble de filles ayant une précision (part de filles vraies promues) supérieure à celle d'un tri par synergie prédictive de pré-calibrage $\Delta_{\text{syn}}$ combiné au couplage d'opérateurs $\text{RA}_{\text{op}}$.
* **Hypothèse $H_B$ (Supériorité de la synergie fonctionnelle $\Delta_{\text{syn}} \times \text{RA}_{\text{op}}$) :** À budget total d'échantillonnage égal (en comptant les $n_0 = 15$ tirages de criblage dans le budget total de tirages du juge !), un allocateur à deux étages (Étage 1 : filtrer par $\text{RA}_{\text{op}} > 0$ et allouer $n_0 = 15$ tirages pour mesurer $\Delta_{\text{syn}}$ ; Étage 2 : n'envoyer au test complet de 250 tirages que les filles avec $\Delta_{\text{syn}} > \delta_0$) multiplie par au moins $\times 1,4$ (**illustratif**) le nombre de découvertes vraies par dollar dans *tous* les mondes $v(s)$ (cloche, bords, croissant, décroissant, plat), car il mesure l'effet de la fille au lieu de deviner sa vérité à partir de l'étiquette de ses parents.
* **Protocole et métrique :**
  Dans les 5 mondes de P, le budget d'une répétition est de $40 \times 250 = 10\,000$ tirages élémentaires d'instances.
  * Bras 1 (Fenêtre de P) : teste 40 filles à 250 tirages chacune dans $[0,12 ; 0,26]$.
  * Bras 2 (Criblage par synergie $\Delta_{\text{syn}}$ + $\text{Ortho}(A,B)$) : crible $K = 120$ filles (**illustratif**, coût $120 \times 15 = 1\,800$ tirages) choisies par Thompson sur $(\text{RA}_{\text{op}}, |\rho_{\text{res}}(A,B)|)$, puis alloue les $8\,200$ tirages restants ($32$ tests complets de 250 tirages) aux 32 filles ayant le plus grand $\Delta_{\text{syn}}$.
* **Contrôle négatif :**
  1. Garantir que les 15 tirages de criblage ne sont **jamais réutilisés** dans les 200 tirages frais du juge v1 (sinon biais de sélection / inflation de $\alpha$). Vérification mécanique : dans un monde purement nul ($v(s) \equiv 0$, 100 % de filles fausses), le taux de promotion par fille testée au second étage doit rester $\le \alpha$.
  2. Injecter 10 % de tricheurs « parent A + loi aveugle » (le trou mentionné dans P) pour vérifier lequel des deux bras se fait piéger.
* **Seuils et issues falsifiantes :**
  * **Falsification de $H_A$ :** Si le Bras 2 bat le Bras 1 ($D = \text{Bras 2} - \text{Bras 1} > 0$, IC à 95 % au-dessus de 0) sur la moyenne des 5 mondes et dans au moins 4 mondes sur 5.
  * **Falsification de $H_B$ :** Si le coût du criblage (les 8 tests complets sacrifiés sur 40) n'est pas compensé par la sélection sur $\Delta_{\text{syn}}$ dans le monde « cloche » ($D < 0$ dans « cloche »).

---

# (d) Mesure minimale de fonctionnement de chaque instrument nommé (Réponse au point (c) du livrable)

Pour chaque instrument nommé dans la question, nous définissons : le taux de détection (TPR / rappel), le taux de fausses alertes (FPR / FDR), les paires de cas honnêtes appariés sur lesquels les mesurer, et la vérification mécanique triviale à battre.

| Instrument nommé | Cas honnêtes appariés (Positifs vrais vs Négatifs subtils) | Mesure minimale : Détection (TPR) et Fausses alertes (FPR) | Vérification mécanique (baseline) à battre |
| :--- | :--- | :--- | :--- |
| **1. Le Juge figé v1** (test de pari contre nul composite : parents, mélanges, enveloppes, marge $2\delta_0=0,02$) | **Positif :** Fille vraie (parent A sur sous-pop 0, loi neuve de force $\in [0,3 ; 1,5]$ sur sous-pop 1).<br>**Négatif apparié (même marge apparente) :** (i) Enveloppe harmonique aveugle des parents ; (ii) **Trou de P** : « Parent A + bruit/loi aveugle sur une variable muette » ; (iii) Pari couvert (*hedged bet*) interpolant A et B. | **FPR (priorité absolue, R1) :** $\le \alpha$ (ex. $0,05$, avec IC supérieur de Wilson $< 0,065$ sur 500 tirages par tricheur) sur *chacun* des 6 tricheurs scriptés de R1 + le trou « parent + loi aveugle ».<br>**TPR :** $\ge 0,80$ (**illustratif**) pour une force d'effet $\ge 0,6$ sur 200 tirages frais. | Test du rapport de vraisemblance standard contre le seul meilleur parent ($\max(\ell_A, \ell_B)$) sans enveloppe convexe (qui échoue face à l'enveloppe aveugle, **RAPPORTÉ** dans R1). |
| **2. La mesure de distance / similarité entre parents ($s$ vs $\text{RA}_{\text{op}}$)** | **Positif :** Paires de parents de champs distincts partageant un opérateur latent non-moyeu (greffes et jumeaux de R2, ou ponts réalisés 2011–2016 de T).<br>**Négatif apparié :** Paires des mêmes champs partageant uniquement un opérateur « moyeu » générique (présent dans 25 % des articles, R2) ou un homonyme inter-champ. | **TPR@k (Rappel/Précision à budget fixé) :** Sur les mondes à moyeux dominants de R2, précision $\ge 0,20$ (d1 atteint $0,210$, **RAPPORTÉ** dans R2).<br>**FPR (taux de pièges moyeux/homonymes tirés) :** Part de moyeux $< 0,15$ (contre $0,385$ pour le stratifié dans R2) et invariance au changement de pondération TF-IDF vs fréquences brutes (corrélation de rang de Spearman $\ge 0,90$). | Tirage stratifié uniforme par paire de domaines + filtre lexical (précision $0,203$ en monde bien observé, $0,040$ avec moyeux dominants dans R2 ; $0,22\%$ dans T, **RAPPORTÉ**). |
| **3. Le Filtre de compatibilité des contraintes** | **Positif :** Deux fiches parentes opérant sur des régimes compatibles (ex. même échelle asymptotique, hypothèses de régularité non contradictoires).<br>**Négatif apparié :** Deux fiches partageant le même opérateur et le même domaine, mais aux domaines de validité mutuellement exclusifs (ex. $N \to \infty$ gaussien vs échantillon fini à queue lourde $\alpha < 2$). | **Rappel des paires compatibles :** $\ge 0,57$ (valeur mesurée dans R2 : $0,57$ à $0,60$, **RAPPORTÉ**).<br>**FPR (rejets à tort de vrais ponts) :** $\le 0,05$ (mesuré à 4–5 % dans R2, **RAPPORTÉ**).<br>**Taux de fuite d'incompatibles :** Doit descendre sous $0,15$ (**illustratif** ; actuellement à $0,262 - 0,274$ dans R2 et $34,4\%$ dans R1, ce qui reste le point faible mécanique). | Filtre d'antonymie lexicale simple (qui laisse encore passer $34,4\%$ de fusions contradictoires dans R1 et $\sim 27\%$ dans R2, **RAPPORTÉ**). À battre par vérification de satisfiabilité (SMT/intervalles) sur les plages numériques des variables des fiches. |
| **4. L'Allocateur de budget d'expériences** (Fenêtre, Thompson, Tri, ou TQ) | **Positif :** Filles vraies dans le réservoir de 300 candidates, à travers les 5 géométries de monde $v(s)$ de P.<br>**Négatif apparié :** Filles fausses situées dans la même strate de distance $s$, + monde à vérité inversée (« bords », « croissant », « décroissant »). | **Gain net $D_2$ contre le hasard :** IC à 95 % strictement $> 0$ dans *tous* les mondes non plats.<br>**Gain net $D_1$ contre le meilleur appris sans structure :** $> 0$ dans la cloche.<br>**Borne de regret adversarial (FPR d'allocation) :** Perte maximale contre le hasard dans un monde inversé bornée par $-0,05$ découverte/dollar (**illustratif** ; un allocateur aveugle bloqué dans $[0,12 ; 0,26]$ perd jusqu'à $-0,20$ quand les vraies sont aux bords). | 1) Tirage uniforme (hasard).<br>2) Tri glouton par moyenne a posteriori sur 8 cases de largeur $0,1$ (défini dans P, **RAPPORTÉ**). |

---

# (e) Ce qu'on perdrait (Analyse de regret asymétrique — Réponse au point 5)

Opposons les deux erreurs de décision possibles sur l'adoption de la fenêtre fixe $[0,12 ; 0,26]$ (associée au score d'entropie) :

### 1. Ce qu'on perd à adopter la fenêtre si elle est fausse (Erreur de type I architecturale : **Perte irremplaçable et aveuglement permanent**)
Si la vraie distribution $v(s)$ des découvertes est monotone croissante (ex. l'allocation de ressources dans T où les paires à fort couplage dominent), monotone décroissante (comme dans le diagnostic `b_eloigne` de R2 qui gagne $+11,9$ points en ciblant les strates les plus éloignées), ou bimodale aux bords :
1. **Censure dure à $100\%$ hors de la fenêtre (Taux de rappel nul sur $82,5\%$ de l'espace) :** Dans le plan P (**RAPPORTÉ**), la fenêtre $[0,12 ; 0,26]$ ne couvre que $17,5\%$ de $[0 ; 0,8]$. Tant qu'il y a au moins 40 candidates dans cette bande (ce qui arrive presque toujours avec $N=300$, puisque $300 \times 0,175 = 52,5 > 40$), l'allocateur à fenêtre **n'explore jamais un seul point hors de $[0,12 ; 0,26]$**. Il ne peut même pas apprendre qu'il se trompe : sa cécité est auto-entretenue.
2. **Chiffrement de la perte sèche (à partir des paramètres de P, RAPPORTÉ) :**
   * Dans le monde « bords » de P ($v(s) = 0,50$ si $s < 0,06$ ou $s > 0,60$, et $0,05$ sur $[0,06 ; 0,60]$), la fenêtre $[0,12 ; 0,26]$ tombe **intégralement dans la zone morte** à $v(s) = 0,05$. L'allocateur à fenêtre ne trouvera en espérance que $\approx 0,05 \times \text{puissance} \le \mathbf{0,05}$ découverte vraie par dollar (soit 2 découvertes sur 40 tests), alors que même le **pur hasard** a une espérance de vérité de $\frac{0,26}{0,80}\times 0,50 + \frac{0,54}{0,80}\times 0,05 = \mathbf{0,196}$ (près de 4 fois plus que la fenêtre !), et qu'un bandit appris monte vers $0,35 - 0,40$ (**illustratif**).
   * Pire encore : si la fenêtre est *vraie* mais que le pic au centre de la fenêtre atteint $p = 0,80$ tandis que ses bords internes sont à $p = 0,50$, la règle d'entropie maximale de Gemini force l'allocateur à **fuir le pic à $0,80$ pour stagner sur la frontière à $0,50$**, perdant $37,5\%$ des découvertes à l'intérieur même de sa propre fenêtre.
3. **Fragilité métrique :** Comme montré en R2 (**RAPPORTÉ**), un simple changement de prétraitement du texte (TF-IDF vs fréquences brutes) déplace les cosinus de $0,28$ à $0,11$. Une fenêtre figée en dur à $[0,12 ; 0,26]$ devient silencieusement obsolète dès que le corpus ou la taille des fiches change.

### 2. Ce qu'on perd à écarter la fenêtre fixe si la vérité suit réellement la fenêtre (Erreur de type II architecturale : **Coût d'apprentissage transitoire, borné et récupérable**)
Si la vraie valeur suit effectivement la cloche de P ($v(s) = 0,50$ sur $[0,12 ; 0,26]$ et $0,05$ ailleurs) et que nous écartons la fenêtre rigide au profit d'un allocateur qui apprend en ligne (comme le tri par espérance, Thompson par cases, ou Thompson quadratique TQ) :
1. **Aucune zone n'est censurée :** L'allocateur en ligne explore l'ensemble du domaine, découvre empiriquement que la densité de promotions est élevée dans $[0,12 ; 0,26]$, et y concentre ensuite son budget.
2. **Chiffrement du coût maximal :** La perte se réduit au **coût d'exploration initial** (tester quelques filles hors de la fenêtre au début des 40 tirages) plus l'éventuel effet de bord des cases. Avec un bandit quadratique à 3 paramètres (TQ) ou un bandit multi-échelle, ce coût transitoire est borné par $5$ à $8$ tirages d'exploration sur $40$ (**illustratif**), soit un écart d'environ $0,04$ à $0,08$ découverte par dollar sur la première génération, qui tombe à **zéro** aux générations suivantes si le prieur $(\theta_0, \theta_1, \theta_2)$ est transmis avec un facteur d'oubli contrôlé d'une génération à l'autre.

**Conclusion de l'analyse de regret :** Le risque est radicalement asymétrique. Adopter la fenêtre fixe expose à une **perte permanente et non détectable** (jusqu'à $-75\%$ contre le hasard dans le monde « bords »), tandis que la remplacer par un allocateur bayésien qui *apprend* la forme de $v(s)$ (en visant l'espérance / Thompson et non l'entropie) ne coûte qu'un **délai d'exploration initial borné** si la cloche existe, tout en protégeant le pôle si elle n'existe pas.

---

# (f) Ancrage matériel (Réponse au point (d) du livrable)

Conformément à la ligne directrice de R1, R2 et T (**RAPPORTÉ**), toutes les expériences décisives proposées ci-dessus s'exécutent **sur processeur seul (CPU), sans appel à des modèles de langue payants et sans téléchargement réseau supplémentaire** :

1. **Expérience 1 (Exécution du plan P + monde « cloche à cœur riche » + allocateur TQ) :**
   * **Environnement :** Python 3.13.17 (bibliothèque standard + NumPy 2.3.4 / SciPy 1.16.3, versions déjà installées et empreintées dans R2 et T, **RAPPORTÉ**).
   * **Modèles ouverts :** Aucun appel de LLM nécessaire (simulation mathématique directe des lois prédictives et du juge v1).
   * **Calcul et temps estimés :** 6 mondes $\times$ 30 répétitions $\times$ 5 allocateurs $\times$ 40 tests $\times$ 250 tirages = $9 \times 10^6$ évaluations vectorisées élémentaires. Temps d'exécution sur 1 cœur CPU : **15 à 45 secondes** (**illustratif**, par comparaison avec les 4 000 mondes de R2 exécutés en 93 secondes, **RAPPORTÉ**).
   * **Coût financier :** **0,00 USD**.

2. **Expérience 2 (Test de la fenêtre par déciles sur la rétrodiction arXiv 2003–2016) :**
   * **Environnement :** Réutilisation directe des fichiers `resultats/scores-principal-v1.npz`, `resultats/issues-principal-v1.npz` et `resultats/vocabulaire-principal-v1.npz` déjà produits dans la pièce T (**RAPPORTÉ**).
   * **Calcul et temps estimés :** Calcul des cosinus de profils sur le graphe d'avant (43 162 termes, 1 000 000 de paires), découpage en 10 déciles et 1 000 rééchantillonnages bootstrap. Temps d'exécution sur CPU (2 processus, comme dans T) : **moins de 3 minutes** (**illustratif**).
   * **Coût financier :** **0,00 USD**.

3. **Expérience 3 (Criblage par synergie $\Delta_{\text{syn}}$ et fermeture du trou « parent + loi aveugle » du juge v1) :**
   * **Environnement :** Même banc Python/NumPy que l'Expérience 1.
   * **Calcul et temps estimés :** Optimisation convexe à 1 paramètre $\lambda \in [0,1]$ sur $n_0 = 15$ points (par recherche sur grille de 21 points ou Brent) pour 120 filles par répétition. Temps d'exécution : **moins de 60 secondes** sur CPU (**illustratif**).
   * **Coût financier :** **0,00 USD**.
   * *Note pour le passage ultérieur à la Génération 1 avec de vraies fusions de fiches (pièce C) :* Lorsque les fiches filles seront générées par des modèles ouverts ou par API (trois familles distinctes exigées par R1 : générateur, extracteur, fusionneur — par ex. Qwen-2.5-72B-Instruct ou Llama-3.3-70B-Instruct en ouvert, **illustratif**), le pré-criblage CPU par $\text{RA}_{\text{op}}$ avant fusion et par $\Delta_{\text{syn}}$ sur $n_0=15$ tirages avant le juge complet divisera par **3 à 5** (**illustratif**) le coût d'exécution des agents expérimentateurs en bac à sable.

FIN-DE-CELLULE