# Avis de conception

*Les textes intégraux [F12], [S1], [C3], [C4] et [B] ne sont pas inclus ici ; je m’en tiens au résumé transmis, sans reconstituer leur contenu.*

Les applications aux proposeurs sont toutes des **HYPOTHÈSES**. Les blocs marqués **VÉRIFIÉ** ci-dessous sont uniquement des déductions mathématiques sous les hypothèses énoncées, non des résultats expérimentaux.

## 1. Ce que la question suppose sans que ce soit établi

1. **Le goulot est bien l’exploration.**  
   **RAPPORTÉ :** la génération 1 de v67 a produit onze variantes proches, puis la génération 2 aucune promotion. Cela ne dit pas si les bassins étroits n’ont produit aucune proposition brute, ont produit des propositions mal groupées, ou ont produit de bonnes cartes ensuite perdues par manque de puissance du juge. La lecture à trois étages — propositions brutes, représentants, retenues — est donc indispensable avant d’investir dans la recherche.

2. **Il existe une population de bassins étroits et profonds transférable à cet organisme.**  
   **RAPPORTÉ :** les bassins de Bespoke Labs concernent d’autres tâches et n’ont pas été reproduits ici.  
   **RAPPORTÉ :** le monde v4 contient une composante conditionnelle invisible en moyenne et une chaîne possible de profondeur 2.  
   **HYPOTHÈSE conservée :** de vrais proposeurs peuvent trouver cette composante après archivage de sa condition.

3. **Largeur structurelle et largeur comportementale sont réglables.** Ce n’est pas automatique. On peut régler dans le monde :
   - la masse \(r\) de la région où réside le signal ;
   - l’ordre \(t\) d’une interaction ;
   - le nombre \(d\) de prérequis ;
   - l’amplitude du gain.
   
   Mais on ne peut pas régler directement, par un bouton du monde, la probabilité \(\pi_0\) qu’un modèle propose spontanément l’idée. Celle-ci doit être mesurée sur des mondes de calibration distincts.

4. **Une vue publique peut modifier cette probabilité à coût égal.** C’est le point empirique central. Une mathématique qui optimise des focalisations ne sert à rien si les proposeurs répondent de la même façon à toutes les vues.

5. **Il existe des données publiques d’exploration avec issues, distinctes des tirages du juge.** Leur existence n’est pas établie par les faits. Les méthodes 1 et 3 ci-dessous sont inapplicables sans elles, sauf à créer explicitement cette pièce dans un dessin neuf.

6. **Trouver et promouvoir sont deux problèmes différents.** Une composante peut avoir un grand effet local mais un gain global trop faible pour être détectée sur une région rare. Une meilleure exploration peut alors augmenter les propositions brutes sans augmenter les retenues.

### Critère élémentaire de gain

Pour une cible \(b\), soit

\[
p_i=\Pr(\text{la proposition }i\text{ entre dans }b\mid V_i),
\]

où \(V_i\) est la vue servie. Sous **HYPOTHÈSE d’indépendance conditionnelle** des appels,

\[
S_B=1-\prod_{i=1}^{K}(1-p_i).
\]

Le témoin de \(K\) appels indépendants avec vue ordinaire \(V_0\), où \(p_i=p_0\), donne

\[
S_A=1-(1-p_0)^K.
\]

**VÉRIFIÉ — calcul conditionnel :** \(S_B>S_A\) si et seulement si

\[
\sum_{i=1}^{K}-\log(1-p_i)>K\bigl[-\log(1-p_0)\bigr].
\]

Ainsi, ni la couverture d’un espace de vues, ni une distance entre lois, ni une entropie plus grande ne constituent déjà un gain. Il faut déplacer les probabilités effectives de proposition.

---

## 2. Méthodes proposées, dans l’ordre où je les testerais

### 2.1. Orthogonalisation fonctionnelle des résidus et plans factoriels de focalisation

C’est la méthode la plus directement adaptée à la composante conditionnelle des faits.

#### Objet mathématique

On dispose d’une loi publique de référence \(q_0\), par exemple une loi de l’archive ou un mélange public dont les poids sont fixés d’avance, jamais choisi par valeur e. Soit \(m_0(x)\) sa prédiction moyenne et, sur des données publiques d’exploration,

\[
R=Y-m_0(X),\qquad g(x)=\mathbb E[R\mid X=x].
\]

On choisit une base orthonormale \(\{\phi_S\}\) pour la loi publique \(\mu\) des traits :

\[
\mathbb E_\mu[\phi_S]=0,\qquad
\mathbb E_\mu[\phi_S\phi_T]=\mathbf 1_{\{S=T\}}.
\]

Pour des traits binaires indépendants et centrés, on peut prendre les contrastes de Walsh

\[
\chi_S(x)=\prod_{j\in S}x_j .
\]

Les coefficients résiduels sont

\[
a_S=\langle g,\phi_S\rangle
   =\mathbb E[g(X)\phi_S(X)].
\]

**VÉRIFIÉ — exemple conditionnel :** si

\[
g(x)=\beta x_1x_2,\qquad \mathbb E[X_2]=0,
\]

alors

\[
\mathbb E[g(X)\mid X_1]=0,
\]

mais \(a_{\{1,2\}}=\beta\). Le signal est donc invisible dans une moyenne conditionnelle à un seul trait, tout en étant parfaitement identifiable dans le contraste d’ordre 2.

Si \(|R\phi_S|\leq G\), un estimateur empirique sur \(n\) observations indépendantes satisfait, pour tout contraste fixé,

\[
\Pr\!\left(|\widehat a_S-a_S|\geq\eta\right)
\leq 2\exp\!\left(-\frac{n\eta^2}{2G^2}\right).
\]

C’est une garantie d’estimation du résidu, **pas** une garantie que le proposeur comprendra ou exploitera le contraste.

#### Endroit et calcul

L’orchestrateur, hors de tout agent :

1. calcule les contrastes sur les seules données publiques d’exploration ;
2. construit un dictionnaire de focalisations d’ordre borné ;
3. attribue ces focalisations selon un plan factoriel ou un parcours cyclique gelé ;
4. sert à chaque proposeur une vue complète — archive non masquée — avec une focalisation publique supplémentaire.

Le proposeur ne reçoit ni valeur e, ni verdict, ni récompense de nouveauté. On peut ne lui servir que le sous-problème public à examiner, sans le coefficient numérique.

#### Pourquoi cela pourrait battre les tirages indépendants

Le témoin demande implicitement au modèle de redécouvrir qu’il faut chercher une interaction. Ici, le budget est consacré à tester la capacité prédictive une fois le contraste pertinent rendu saillant. Le gain reste subordonné à

\[
p_b(V_S)>p_0
\]

pour au moins certaines focalisations, ce qui est précisément ce que le pilote doit mesurer.

#### Compatibilité et risques

- Aucune récompense numérique de nouveauté n’entre dans le juge ou dans la vue.
- Aucun quota de `si_sinon` ou `melange` : les focalisations portent sur des fonctions et des traits, pas sur la grammaire.
- Aucune archive n’est masquée.
- Le balayage exploratoire de nombreux contrastes ne remplace pas e-BH : toutes les cartes passent la même garde sur tirages frais.
- Le nombre de contrastes croît combinatoirement avec l’ordre ; une couverture exhaustive devient rapidement trop chère.
- Un résidu peut être du bruit, un artefact de \(q_0\), ou un signal sans traduction dans la grammaire.
- **RAPPORTÉ :** le juge cède hors de la classe de son nul. Aucune comparaison de bras ne doit précéder le certificat de garde requis pour les nouvelles familles effectivement explorées.

### 2.2. Splitting multiniveau sur un graphe public de prérequis

Cette méthode vise les bassins dont l’idée complète est improbable en une carte, mais dont chaque étape devient accessible après archivage de la précédente.

#### Objet mathématique

On représente l’état de recherche par un graphe orienté acyclique public \(G=(V,E)\). Un nœud ne contient ni oracle ni texte secret : il décrit seulement des éléments publics, par exemple les traits et conditions déjà représentés dans les formes canoniques archivées. Une arête représente un prérequis supplémentaire à examiner.

Le niveau \(j\) est atteint lorsque la carte correspondante a été **retenue** et figure donc dans l’archive ordinaire. L’orchestrateur affecte ensuite des appels neufs à la frontière du graphe, selon un ordre canonique ou cyclique, jamais selon les valeurs e.

Soit \(h_j\) la probabilité qu’un appel au niveau \(j\) produise l’étape suivante **et la fasse retenir**, conditionnellement à l’atteinte du niveau \(j\). Avec \(K_j\) appels indépendants à ce niveau,

\[
s_j=1-(1-h_j)^{K_j}.
\]

Pour une chaîne de \(d\) étapes, sous ce modèle simplifié,

\[
S_B=\prod_{j=0}^{d-1}s_j,
\qquad K=\sum_j K_j .
\]

**VÉRIFIÉ — condition de gain :** ce splitting bat le témoin si

\[
\prod_{j=0}^{d-1}\left[1-(1-h_j)^{K_j}\right]
>
1-(1-p_0)^K .
\]

Ce n’est pas une preuve que \(h_j\) est grand ; c’est une formule qui indique quoi mesurer.

#### Endroit et calcul

- À chaque génération, l’orchestrateur lit uniquement les formes canoniques publiques de l’archive.
- Il construit la frontière et les focalisations correspondantes.
- Les proposeurs travaillent en sessions neuves.
- La sélection statistique et le regroupement des doublons restent inchangés.

#### Pourquoi cela pourrait atteindre un bassin étroit

**RAPPORTÉ :** la composante conditionnelle v4 est décrite comme trouvable une fois sa condition archivée. Le splitting consacre précisément du budget à cet événement conditionnel, au lieu d’exiger que condition et effet conditionnel soient inventés simultanément.

#### Compatibilité et risques

- Le mécanisme ne récompense pas la nouveauté : il réutilise seulement l’archive déjà produite par la sélection ordinaire.
- Aucun score du juge n’est servi aux agents.
- La profondeur oracle ne pilote pas la course ; elle sert seulement à l’évaluation.
- Le graphe peut devenir trop large, ou enfermer la recherche dans des raffinements d’un bassin large. Il faut donc conserver une exploration depuis la racine.
- Une étape vraie mais non retenue ferme toute la descente correspondante.
- Le nombre de générations devient une contrainte : si l’horizon est inférieur au nombre de prérequis, la méthode ne peut pas terminer la chaîne.

### 2.3. Balayage multi-échelle des résidus pour les signaux confinés à une région rare

Cette méthode répond directement au problème de dilution, sans transformer une distance globale en récompense.

#### Objet mathématique

On construit un arbre public de régions \(\mathcal T\) dans l’espace des traits. Pour chaque région \(A\in\mathcal T\), sur les données publiques :

\[
R_A=\sum_{i:X_i\in A}R_i,\qquad
V_A=\sum_{i:X_i\in A}\widehat{\operatorname{Var}}(R_i\mid X_i),
\]

puis, lorsque \(V_A>0\),

\[
T_A=\frac{R_A}{\sqrt{V_A}}.
\]

Les régions sont examinées à plusieurs échelles ; une focalisation est construite à partir d’une région nominée, éventuellement confirmée sur une seconde partie des données publiques.

**VÉRIFIÉ — modèle simplifié :** supposons que le résidu moyen vaille \(\delta\) dans \(A\), zéro ailleurs, que \(\Pr(X\in A)=r\), et que la variance résiduelle soit approximativement \(v\). Alors

\[
\mathbb E[R_A]\simeq nr\delta,\qquad V_A\simeq nrv,
\]

donc le signal standardisé local est de l’ordre de

\[
T_A\simeq \delta\sqrt{\frac{nr}{v}}.
\]

Le même calcul sur tout l’espace donne un signal global environ \(\sqrt r\) fois plus petit. La normalisation locale ne crée pas d’information, mais elle évite de la noyer dans la moyenne globale.

#### Endroit, intérêt et limites

L’orchestrateur sert une focalisation publique sur une région et, si nécessaire, la combine avec les contrastes de la méthode 1. Cela peut être utile lorsque l’idée étroite est une exception locale plutôt qu’une interaction polynomiale simple.

Mais :

- si \(nr\) est petit, le scan ne peut pas localiser grand-chose ;
- le maximum sur de nombreuses régions sélectionne aussi du bruit ;
- une partition inadaptée peut couper le bassin en morceaux ;
- cette focalisation risque précisément d’encourager des lois par morceaux hors du nul certifié.

Le scan reste donc exploratoire ; il ne modifie ni promotion ni seuil statistique.

### 2.4. Pure exploration hors ligne des couples « proposeur × méthode de vue »

Cette méthode est moins directe et plus coûteuse ; elle ne devient pertinente que si l’un des mécanismes précédents montre un effet brut.

Soit un bras \(a\), composé d’un proposeur et d’un générateur de vues. Sur une microcourse de calibration à budget fixé, on mesure par l’oracle :

\[
Z_{a,t}=
\mathbf 1\{\text{le bassin cible est couvert par les propositions brutes}\}.
\]

On note \(\mu_a=\mathbb E[Z_{a,t}]\). Avec \(n\) microcourses indépendantes par bras et \(Z_{a,t}\in[0,1]\),

\[
\Pr(|\widehat\mu_a-\mu_a|\geq\varepsilon)
\leq 2e^{-2n\varepsilon^2}.
\]

Pour \(A\) bras, si

\[
n\geq \frac{1}{2\varepsilon^2}\log\frac{2A}{\delta},
\]

alors tous les \(\widehat\mu_a\) sont à \(\varepsilon\) près avec probabilité au moins \(1-\delta\). Le meilleur bras est identifié si son avance sur le second excède \(2\varepsilon\).

**Portée exacte :** cette garantie concerne la distribution des mondes de calibration, pas les mondes futurs.

L’objection contre une récompense de nouveauté ne s’applique pas directement ici : \(Z\) n’entre ni dans le juge cible, ni dans une sélection de cartes, ni dans un signal servi à un agent. C’est une évaluation oracle hors course, cohérente avec le principe que la composition des proposeurs est jugée sur oracle et coût. Elle exige néanmoins des mondes de validation disjoints, car elle peut fortement surajuster la famille de calibration.

### Verrou statistique commun

**RAPPORTÉ :** la preuve actuelle porte sur \(H_0\) « le monde appartient à la classe du nul » et ne borne pas les fausses découvertes au sens de l’oracle. Les méthodes ci-dessus ne changent rien à cette limite.

Une construction illustre ce qu’un certificat devrait démontrer. Soit une densité alternative \(f\), ajustée indépendamment des données d’évaluation, et une classe nulle \(\mathcal N_0\). Posons

\[
e(Z)=\inf_{q\in\mathcal N_0}\frac{f(Z)}{q(Z)}.
\]

Pour tout \(q_0\in\mathcal N_0\),

\[
\mathbb E_{q_0}[e]
\leq
\mathbb E_{q_0}\!\left[\frac{f(Z)}{q_0(Z)}\right]
\leq 1.
\]

C’est donc un e-value valide sous cette classe, avec les conventions usuelles de support. Mais l’infimum peut être extrêmement conservateur ou incalculable, et cette construction ne prouve ni la puissance ni la validité de tout le protocole adaptatif. Une simulation favorable seule ne serait pas un certificat absolu.

---

## 3. Ce qui est impossible en principe, et où un gain peut exister

### Impossibilités

1. **Aucun gain sans information ni réponse différentielle des proposeurs.**  
   Si \(p_b(V_i)=p_0\) pour toutes les vues disponibles, le critère du §1 donne exactement la même probabilité de succès. La sophistication du scheduler est alors sans effet.

2. **Aucune garantie uniforme contre un bassin placé arbitrairement.**  
   Supposons \(M\) cellules de recherche et qu’un appel n’en examine qu’une. Avec \(K<M\) appels et sans retour informatif, tout parcours laisse au moins \(M-K\) cellules non examinées. Un adversaire peut y placer la cible. Il n’existe donc pas de garantie de découverte uniforme à budget fixé.

3. **Aucune localisation sur des données qui ne contiennent pas la région.**  
   Si deux mondes ne diffèrent que sur \(A\) et qu’aucune observation publique ne tombe dans \(A\), leurs données observées ont la même loi. Aucun calcul sur ces données ne peut distinguer les mondes. La probabilité de ce vide est \((1-r)^n\).

4. **Aucune puissance contre des alternatives observationnellement indiscernables.**  
   Si un monde nul et un monde alternatif induisent la même distribution d’évaluation, toute procédure a le même comportement dans les deux. Préserver strictement la validité sous le nul interdit alors d’obtenir aussi une forte puissance.

5. **La profondeur ne répare pas une garde inadéquate.**  
   Une idée peut être correctement proposée, puis rejetée parce que son gain global est trop faible ou parce que le nul ne couvre pas la classe pertinente. Améliorer l’exploration ne résout ni problème.

### Structures sous lesquelles un gain est plausible

Un gain est **HYPOTHÈSE testable** lorsque simultanément :

- le bassin est représenté par des contrastes d’ordre modéré ou par des régions d’un arbre raisonnablement petit ;
- les données publiques fournissent assez d’observations pour estimer ces contrastes ;
- les vues focalisées augmentent effectivement \(p_i\) ;
- les prérequis sont archivables et accessibles dans la grammaire ;
- le juge a assez de puissance une fois l’idée proposée ;
- la garde est certifiée pour les classes que la focalisation favorise ;
- pour l’allocation hors ligne, les performances se transfèrent des mondes de calibration aux mondes de validation.

---

## 4. Expérience décisive la moins chère

Je testerais **uniquement la méthode 1**, sur une génération, avant tout splitting ou bandit coûteux.

### Monde et réglages

Le programme à graine scellée fait varier séparément :

- \(r_w=\Pr_w(X\in A_w)\), largeur structurelle ;
- \(t_w\), ordre de l’interaction cible ;
- \(\Delta_w\), profondeur prédictive ;
- éventuellement \(d_w\) dans une réplication ultérieure.

La profondeur oracle peut être définie par

\[
\Delta_w=
D_{\mathrm{KL}}(P_w^\star\|Q_{-b})
-
D_{\mathrm{KL}}(P_w^\star\|Q_{+b}),
\]

où \(Q_{-b}\) est la meilleure loi autorisée sans la composante cible et \(Q_{+b}\) la meilleure avec l’idée complétée.

La largeur comportementale \(\pi_{0,w}\) est mesurée sur calibration, jamais présentée comme un paramètre directement réglé. Les valeurs de la grille, les coûts et les tailles d’échantillon sont scellés avant ouverture.

### Duel à coût égal

- **Bras A :** appels indépendants ordinaires, avec une focalisation placebo sans information.
- **Bras B :** mêmes proposeurs, mêmes sessions neuves et mêmes limites par appel, mais focalisations issues des contrastes orthogonaux publics.

Les deux bras utilisent les mêmes données publiques, le même monde apparié, le même juge et le même budget total. Le calcul du diagnostic est comptabilisé dans le coût de B ; si nécessaire, B reçoit donc moins d’appels, ce qui rend la comparaison prudente.

### Métriques et seuil

Pour chaque course, l’oracle mesure :

\[
C^{\mathrm{brut}}_{a,w}
=\mathbf 1\{\text{au moins une proposition brute couvre la cible}\},
\]

\[
C^{\mathrm{ret}}_{a,w}
=\mathbf 1\{\text{au moins une retenue couvre la cible}\}.
\]

La métrique principale est

\[
G=\mathbb E_w[C^{\mathrm{ret}}_{B,w}-C^{\mathrm{ret}}_{A,w}],
\]

sur la grille étroite-profonde préenregistrée. La couverture brute et l’utilité pondérée

\[
U_a=\mathbb E_w[\Delta_w C^{\mathrm{ret}}_{a,w}]
\]

sont secondaires.

Le duel est :

\[
H_A:G\leq \delta_{\min}
\qquad\text{contre}\qquad
H_B:G>\delta_{\min}.
\]

On conclut pour B seulement si la borne inférieure unilatérale de l’intervalle apparié dépasse \(\delta_{\min}\), avec taille d’échantillon et risque fixés par calcul de puissance avant scellement. Le nombre de mondes et les seuils numériques relèvent du préenregistrement, pas d’un choix après observation.

### Contrôles négatifs et audit

- Mondes sans composante cible et strictement dans le nul certifié, avec les mêmes leurres larges.
- Copies renommées de lois archivées.
- Focalisations placebo ou coefficients permutés, à longueur de vue comparable.
- Recombinaisons par morceaux, produits ou compositions uniquement dans la mesure où la garde prétend les couvrir.
- Aucune hausse des promotions indues au-delà de la tolérance gelée, en plus du certificat mathématique.
- Lecture finale par un lecteur neuf et même audit d’un résultat trop propre dans les deux sens.

Si B améliore la couverture brute mais pas les retenues, le pilote conclut à un problème de garde ou de puissance, **pas** à une réussite de découverte. S’il n’améliore même pas la couverture brute, l’hypothèse de réponse aux vues est démentie dans ce régime.

---

## 5. Ce qui me ferait changer d’avis

Je recommande actuellement un micro-pilote borné, pas un déploiement. Je renoncerais à cette direction si :

- l’audit à trois étages montrait que les bassins cibles sont déjà souvent proposés mais perdus ensuite ;
- les focalisations ne modifiaient pas les probabilités brutes à coût égal ;
- l’effet disparaissait face aux focalisations placebo, sur des mondes held-out ou avec une autre famille de proposeurs ;
- le gain brut ne devenait pas un gain retenu sans affaiblir la garde ;
- le coût des diagnostics et des microcourses absorbait l’avantage ;
- des appels indépendants supplémentaires ou une remise à zéro neutre du contexte obtenaient le même résultat à budget égal ;
- aucun certificat de garde ne pouvait être fourni pour les classes que la méthode favorise.

À l’inverse, je passerais au splitting multiniveau seulement après une amélioration préenregistrée de la couverture brute **et** retenue, reproduite sur validation disjointe, avec contrôles nuls propres. Le critère décisif n’est donc pas la sophistication mathématique, mais le déplacement mesuré de \(p_i\), suivi d’une découverte retenue, sans dépense supplémentaire ni perte de validité.

FIN-DE-CONSULTATION