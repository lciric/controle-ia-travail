# Critique croisée de méthode : tour III.2, proposition A

**État des pièces.** Les pièces B et C sont transmises en entier : chacune se termine par sa ligne de clôture, et aucune coupure n'est visible.

**Conventions de statut.** Les contenus du §2 des FAITS sont repris en `VÉRIFIÉ`. Ceux des §1, §3 et §4 sont repris en `RAPPORTÉ`, comme le font B et C. Toutes mes affirmations propres (dérivations, conditions, tests) sont des `HYPOTHÈSE`. Tout nombre que je calcule à partir de seuils déjà illustratifs reste marqué « illustratif ».

---

## Sur la proposition B

### (a) Défauts de méthode

**A.1. Statuts sans source dans le dossier.** B attribue `[RAPPORTÉ]` à des éléments que les FAITS ne contiennent pas :
- l'ouverture intégrale de Dolma pour OLMo-7B ;
- « pénalité Benjamini-Hochberg », alors que le dossier dit seulement « correction des comparaisons multiples » ;
- « variables délibérément confondues ou invariants latents omis » ;
- « 1 poste CPU sans carte graphique ».

Je ne modifie aucun de ces statuts. Je signale seulement qu'aucun ne se rattache à une pièce. C'est un défaut de traçabilité qui contamine le tableau 3.3, où des parades proposées par B apparaissent comme rapportées.

**A.2. Action 1 (e-processus Huber-DKW).**
- *Vrai par construction.* Le contrôle $\mathbb{P}_{H_0}(\exists t: E_t\ge 1/\alpha)\le\alpha$ découle de l'inégalité de Ville dès que le processus est une surmartingale sous la nulle déclarée `[HYPOTHÈSE]`. Si le simulateur tire des scores honnêtes i.i.d. et une contamination de taux exactement $\epsilon$, la borne $\text{FPR}_\infty\le 0{,}05$ vérifie le code, pas l'hypothèse. Le critère n'a de pouvoir réfutant que si la nulle simulée viole les hypothèses de l'outil. B ne prévoit aucune violation de ce type : pas de dépendance temporelle, pas de dérive bénigne de difficulté, pas de $\epsilon_{\text{réel}}>\epsilon_{\text{déclaré}}$.
- *Non vérifiable tel qu'écrit.* Un $\text{FPR}_\infty$ « sur tout l'horizon » ne s'estime pas sur des épisodes de $T=1\,000$ pas (illustratif). On mesure au mieux un $\text{FPR}_{\le T}$.
- *Fuite construction/évaluation.* Le « CUSUM empirique ré-étalonné au même $\text{FPR}_\infty$ » reste ambigu. S'il est ré-étalonné sur les trajectoires honnêtes propres qui servent à mesurer le FPR, la référence reçoit un oracle que l'e-processus n'a pas. S'il est ré-étalonné sur la référence contaminée, il faut l'écrire. Dans un cas comme dans l'autre, le $\Delta\text{TPR}\ge+0{,}25$ n'est pas interprétable.

**A.3. Action 2 (frustration de cycles signés).**
- *Vrai par construction.* Dans le monde synthétique, B définit la fausse identité *par* la signature qu'il veut détecter : $X$ croît avec $Y$ dans $R_1$, et $X$ croît à $Y$ constant dans $R_2$. Si le générateur est écrit par l'équipe, $\text{AUROC}\ge 0{,}80$ mesure la fidélité du détecteur à sa propre définition. Il faudrait un générateur externe qui plante aussi des fusions sans conflit de signe, par exemple une rupture d'échelle ou une hétéroscédasticité par sous-régime.
- *Homonymes trop faciles.* Si les homonymes simulés occupent des clusters disjoints, la modularité les sépare trivialement, et le $\Delta\text{AUROC}$ contre la modularité devient un artefact du choix des négatifs.
- *Confusion fatale avec l'issue historique.* Le dossier mentionne deux destins pour une identité sous tension : la promotion en principe (masses inerte et grave) et la scission (chaleur/température) `[RAPPORTÉ]`. Une frustration signée peut marquer *toute* identité contestée. B ne compare jamais « tension qui a mené à une scission » et « tension qui a mené à une promotion ». Le score risque donc de mesurer l'intensité de controverse.
- *Fuite temporelle par l'outillage.* Les régimes $R_1/R_2$ et le typage des prédicats sont extraits avec spaCy/UD, entraînés sur de la langue moderne. Les régimes peuvent aussi être délimités par un vocabulaire né de la scission elle-même (« chaleur latente »). Dans ce cas, l'étiquette de régime contient l'issue.

**A.4. Action 3 (test microcanonique).**
- *Référence fatale absente.* Seul Burt sert de comparaison. Pour une prédiction de liens à cinq ans, la référence minimale est l'attachement préférentiel (produit des degrés), éventuellement Adamic-Adar. Burt est corrélé au degré, et la Précision@100 est dominée par les nœuds de haut degré `[HYPOTHÈSE]`.
- *Conditionnement sur l'issue.* Un modèle nul qui « préserve la séquence jointe des degrés temporels » sur toute la période, post-$t_0$ compris, fixe la croissance des degrés futurs. Or celle-ci est corrélée aux nouveaux ponts. Le nul doit être restreint à $t\le t_0$.
- *Estimateur indéfini.* « Entropie variationnelle de trajectoires » n'a pas d'estimateur spécifié. Le biais des estimateurs d'entropie sur graphes finis à degrés lourds dépend de la taille, ce qui recrée le confondant d'échelle.

**A.5. Action 4 (MDL et anti-unification sur mathlib).**
- *Vrai par construction.* Une définition « développée en termes primitifs » laisse des copies syntaxiques instanciées de son corps. Retrouver une macro inlinée revient à compresser une redondance, pas à créer un objet hors alphabet.
- *Fuites par les noms.* Les noms de lemmes (`foo_add`, etc.), la structure des preuves et les fichiers du même cône de dépendance conservent l'empreinte du concept ablaté. Il faut renommer, et découper les plis par cône de dépendance.
- *Incohérence d'outil.* La « réduction de symétries dimensionnelles » d'Udrescu et Tegmark (2020) `[RAPPORTÉ]` porte sur des données numériques. Sur des AST Lean, elle n'a pas de définition.
- *Code MDL non figé.* Le gain de 15 % (illustratif) dépend du code universel choisi pour les AST. Ce code doit être préenregistré, sinon on peut l'ajuster.

**A.6. Action 5 (sondes d'holonomie).**
- *Vrai par construction.* Si les paraphrases d'évasion appartiennent à la même famille que le cycle $(g_1,\dots,g_k)$, la sonde y est invariante par définition.
- *Sélection sur l'échec de la référence.* Prendre comme ensemble d'évasion les exemples qui font tomber la sonde linéaire sous $\text{TPR}<0{,}40$ sélectionne sur ses erreurs. Le $\Delta\text{TPR}$ est alors gonflé par régression vers la moyenne.
- *Critères mal définis.*
  - L'étiquette cible (« honnête » contre quoi ?) et son mode d'obtention ne sont pas spécifiés. Elle ne peut pas provenir d'un juge génératif `[RAPPORTÉ]`.
  - La sélectivité de Hewitt-Liang suppose une sonde entraînée sur une tâche et une tâche de contrôle. Un défaut d'holonomie n'a pas de tâche de contrôle évidente.
  - L'« étalonnage Gröger-Wen-Brbić » vise des métriques de similarité inter-modèles `[VÉRIFIÉ]`. Son transfert à une sonde reste une hypothèse non déclarée.

**A.7. Action 6 (poids et coordination).**
- *Vrai par construction, côté coordination.* Deux copies de mêmes poids qui tirent indépendamment sur la même loi $p$ sur $K$ options s'accordent avec probabilité $\sum_i p_i^2\ge 1/K$, avec égalité seulement si $p$ est uniforme `[HYPOTHÈSE de modélisation : tirages indépendants à prompt fixe]`. L'« excès au-dessus de $1/K$ » est donc une mesure de non-uniformité de sortie. Le biais positionnel, qui préfère la première option, produit cette « coordination » chez tout modèle. Un indice de poids qui prédit la concentration de sortie n'établit rien sur la coordination.
- *Vrai par construction, côté détection.*
  - Si le bras d'attaque utilise LoRA et les modèles propres un affinage complet, ou un autre rang, le détecteur reconnaît la méthode d'affinage.
  - Si le point de contrôle de base est accessible, $W_{\text{mod}}-W_{\text{base}}$ *est* l'attaque.
  - Marchenko-Pastur n'est pas une nulle pertinente pour des poids entraînés.

**A.8. Décision au point estimé.** Toutes les issues de B sont jugées sur des estimations ponctuelles en conjonction de trois seuils, sans intervalle de confiance. Près des seuils, c'est le bruit d'échantillonnage qui « réfute ».

### (b) Conditions de perte de puissance ou de non-jugeabilité

Toutes les conditions ci-dessous sont des `[HYPOTHÈSE]`.

1. **Action 1, plancher d'identifiabilité.** Notations :
   - les scores honnêtes ont une variance $\sigma_0^2$ ;
   - un sabotage affecte une fraction $p_s$ des pas avec un décalage moyen $\delta$ ;
   - la référence a $n$ épisodes, dont une fraction $\epsilon$ contaminée de façon adverse.

   La borne supérieure robuste de la moyenne honnête porte alors un biais irréductible d'ordre $c\,\sigma_0\sqrt{\epsilon}$, plus un terme $O(\sigma_0\sqrt{\log(1/\alpha)/n})$. C'est le taux minimax d'estimation robuste de la moyenne sous variance bornée, que je crois standard (référence à vérifier).

   La puissance tend vers $\alpha$, quel que soit $T$, dès que $p_s\delta \lesssim c\,\sigma_0\sqrt{\epsilon}+O(\sigma_0/\sqrt{n})$. Avec les valeurs de B ($p_s=0{,}03$, $\epsilon=0{,}05$, scores dans $[0,1]$, $\delta\le1$, tout illustratif), il faut $\sigma_0\lesssim 0{,}13$ (illustratif, avec $c\approx1$). Si la variance honnête dépasse cette valeur, $H_B$ est vraie par construction.
2. **Action 1, dépendance temporelle.** Si les scores honnêtes sont autocorrélés, de coefficient $\phi$, la taille effective de la référence devient $n_{\text{eff}}\approx n(1-\phi)/(1+\phi)$ (illustratif, cas AR(1)). La validité de type DKW, qui suppose l'indépendance, n'est alors plus garantie : le FPR n'est plus jugeable.
3. **Action 2, bruit de signe.** Si l'extraction inverse chaque signe avec une probabilité $q$, indépendamment, un cycle de longueur $L$ voit sa parité basculer avec probabilité $\tfrac12\bigl(1-(1-2q)^L\bigr)$ `[HYPOTHÈSE de modélisation]`. Le contraste entre vraie frustration et bruit est atténué d'un facteur $(1-2q)^L$, par exemple $0{,}8^6\approx0{,}26$ pour $q=0{,}1$ et $L=6$ (illustratif). Le nombre de cycles croissant avec le degré, le score devient alors une fonction de la fréquence.
4. **Action 2, rétrodiction historique.** B admet lui-même une dizaine de cas. Avec 10 positifs et 10 négatifs à $\text{AUROC}=0{,}80$, l'erreur type de Hanley et McNeil (1982, « The meaning and use of the area under a receiver operating characteristic (ROC) curve ») vaut environ $0{,}10$, soit un intervalle à 95 % d'environ $\pm0{,}2$ (illustratif). Le seuil de $0{,}80$ ne peut alors être ni atteint ni réfuté.
5. **Action 3.** Si $P(\text{pont}\mid\text{paire})$ est presque entièrement expliquée par $d_i d_j$, la Précision@100 conditionnelle au produit des degrés n'a pas de variance exploitable. Les 100 paires partagent en outre des nœuds, ce qui rend invalide une loi binomiale de référence.
6. **Action 5.** Borner un FPR de $0{,}02$ avec zéro erreur observée exige $n\ge 3/0{,}02=150$ cas honnêtes (règle de trois ; illustratif, dérivé d'un seuil illustratif). B ne précise pas $n$.
7. **Action 6.** Si les 40 modèles (illustratif) sont équilibrés, soit 20 modèles propres, une seule fausse alerte vaut $\text{FPR}=0{,}05$. Le critère « à $\text{FPR}\le0{,}05$ » est alors discontinu et non jugeable. Un $\rho$ de Spearman sur environ 20 points a de son côté une variance trop grande pour départager $0{,}70$.

### (c) Contrôles négatifs dont l'absence serait fatale

- **Action 1 :**
  - trajectoires honnêtes sous dérive bénigne de difficulté ;
  - contamination de taux $\epsilon_{\text{réel}}=2\epsilon_{\text{déclaré}}$ ;
  - nulle AR(1).
- **Action 2 :**
  - identités sous tension historiquement *promues en principe* ;
  - homonymes intra-domaine ;
  - extraction refaite avec un analyseur figé avant coupure, ou sans lexique moderne.
- **Action 3 :**
  - référence d'attachement préférentiel ;
  - nulle restreinte à $t\le t_0$.
- **Action 4 :**
  - concepts ablatés renommés ;
  - plis séparés par cône de dépendance ;
  - nulle grammaticale bien typée, par une grammaire probabiliste ajustée au corpus, au lieu d'AST aléatoires que l'on rejette trivialement ;
  - abandon du « corpus non ablaté » comme contrôle : son gain attendu n'est pas nul, puisque mathlib contient des redondances réelles.
- **Action 5 :** famille de transformations d'évasion disjointe du cycle et tirée par l'évaluateur externe.
- **Action 6 :**
  - modèles propres affinés par LoRA de même rang ;
  - mesure de l'accord sous permutation *indépendante* de l'ordre des options pour chaque copie.

### Test de recevabilité proposé (inférence forte)

- **$H_A$** : la frustration signée sépare les identités destinées à la scission des identités destinées à la promotion en principe, avec un $\text{AUROC}$ dont la borne inférieure de l'intervalle bootstrap dépasse $0{,}5$.
- **$H_B$** : la frustration mesure l'intensité de controverse. Une fois appariée sur le volume de documents polémiques et la fréquence, son $\text{AUROC}$ scission/promotion a un intervalle qui contient $0{,}5$, alors que son $\text{AUROC}$ contre les identités non contestées reste supérieur à $0{,}5$.
- **Contrôle négatif :** permutation des étiquettes de destin à l'intérieur des strates de controverse.
- **Premier pas sur processeur seul :** sur monde synthétique, faire planter par l'évaluateur externe les deux destins avec un même taux de conflit.
- **Issues :** la séparation après appariement réfute $H_B$. Le seul effet de controverse réfute $H_A$.

---

## Sur la proposition C

### (a) Défauts de méthode

**C.1. Inférence forte rompue par construction.** Pour les Actions 1, 2, 3 et 5, les conditions de $H_A$ et de $H_B$ ne portent pas sur le même dispositif, ou laissent une zone intermédiaire :
- **Action 1** : $H_A$ est posée sans dérive ni $N_{\text{ref}}$, alors que $H_B$ ajoute « dérive bénigne » et $N_{\text{ref}}=1000$. Les deux peuvent être vraies en même temps.
- **Action 2** : $H_A$ juge la stabilité « sous changement de granularité », $H_B$ la variation « entre graphe projeté et hypergraphe ». Ce sont deux contrastes différents.
- **Action 5** : $H_A$ demande $\ge10\,\%$ et $\ge60\,\%$, $H_B$ $\le2\,\%$ et $<20\,\%$ (tout illustratif). Un gain de 5 % avec 40 % de recouvrement ne réfute ni l'une ni l'autre. Les issues falsificatrices de C réfutent $H_A$ sur des seuils qui ne réfutent pas $H_B$.

C reconnaît cette « zone grise » dans ses limites, mais cela contredit la règle B4 au niveau de chaque expérience. Il faut des hypothèses complémentaires sur un même dispositif, avec une règle d'indétermination fondée sur l'intervalle de confiance.

**C.2. Action 1.**
- *Frontière mal spécifiée.* La frontière « $\rho>2\epsilon_{\max}$ » est linéaire en $\epsilon$ et omet l'amplitude $\delta$ du décalage par pas sabotés. Sans $\delta$ ni $\sigma_0$, une fréquence $\rho$ n'est pas une condition d'identifiabilité (voir b.1).
- *Fuite construction/évaluation.* Le CUSUM « recalibré » porte la même ambiguïté que chez B.

**C.3. Action 2 (urnes et percolation sur hypergraphe).**
- *Vrai par construction.* Les recâblages nuls conservent les dates d'entrée des concepts. Ils conservent donc le processus de nouveauté lui-même : la loi de Heaps, cible principale des urnes de Tria et al. (2014, « The dynamics of correlated novelties ») `[RAPPORTÉ]`, est reproduite par la nulle. Le seul gain jugeable est la *corrélation* des nouveautés, c'est-à-dire l'adjacence des nouveaux concepts aux concepts récemment nouveaux. C ne l'isole pas.
- *Métrique non invariante.* Un « gain relatif de log-vraisemblance de +5 % » (illustratif) dépend du nombre d'événements et de l'entropie de base, qui changent avec la granularité. La comparaison entre granularités n'est pas invariante.
- *Confondant exogène.* La diffusion d'instruments ou de formalismes communs (Merton, 1961) `[RAPPORTÉ]` et la croissance des financements par champ ne sont pas contrôlées. Une urne endogène peut absorber un choc exogène.

**C.4. Action 3 (tension intra-documentaire).**
- *Confusion avec l'issue historique.* Comme chez B, il manque le contraste avec les identités promues en principe `[RAPPORTÉ]`. Une « coexistence de contraintes contradictoires dans les mêmes documents » caractérise aussi les débats qui se sont conclus *sans* scission.
- *Sélection rétrospective.* La date de scission, qui définit « pré-scission », est fixée après coup, ce qui expose au biais du survivant. Le volume de cas réels est le même que chez B (b.4).
- *Vrai par construction.* Si le corpus synthétique est généré par l'équipe, le résultat l'est aussi.

**C.5. Action 4 (alignement typé).**
- *Cible inadaptée.* Les jeux de Gu et Krenn (2026) et de Sternlicht et Hope (2025) `[RAPPORTÉ]` mesurent l'*intérêt jugé par des experts* ou des recombinaisons recensées, pas des ponts réalisés après $t_0$. Ils sont construits avec le savoir de 2025-2026, et peut-être avec des plongements. Si l'aligneur emploie des traits voisins, c'est une fuite d'instrument.
- *Critère non jugeable.* Les « faux positifs par polysémie audités » exigent un étiquetage humain, coté 5 en coût et absent du budget, ou un juge génératif, interdit `[RAPPORTÉ]`.
- *Typage anachronique.* Le schéma de typage des relations, extrait par des outils modernes, peut encoder des distinctions postérieures à $t_0$.
- *Instabilité du gain relatif.* Un « +50 % relatifs » sur une précision de base faible est instable. Il faut un gain absolu avec intervalle.

**C.6. Action 5.**
- *Vrai par construction.* Si les opérateurs plantés sont décomposables par symétrie, la méthode guidée par symétries gagne par construction. Il faut aussi des opérateurs plantés sans symétrie exploitable.
- *Critère non jugeable sur données réelles.* Sur le « dépôt public de preuves », il n'existe pas de vérité plantée : le taux de recouvrement n'y est pas défini.
- *Contrôle trop facile.* Le contrôle « sous-arbres permutés » brise le typage. On le rejette trivialement.

**C.7. Action 6.**
- *Cible non définie.* L'étiquette de « détection » dans un monde synthétique (déviation de loi ? comportement planté ?) n'est pas précisée.
- *Vrai par construction.* La famille de perturbations de style est choisie par ceux qui construisent les invariants : l'invariance est construite, pas mesurée.
- *Variance de graine non traitée.* Les modèles de Vafa et al. (2024) `[VÉRIFIÉ]` montrent des représentations incohérentes. La qualité de l'invariant dépend donc de la graine d'entraînement du petit transformeur, et C ne prévoit aucune réplication multi-graines dans cette action.

**C.8. Coordination (§4, point 4).**
- *Vrai par construction.* C compare l'accord entre copies identiques à l'accord entre modèles de graines distinctes. Le premier vaut $\sum p_i^2$, le second $\sum p_i q_i$, et la différence est positive dès que $p\neq q$ `[HYPOTHÈSE de modélisation]`. L'« excès » mesuré contre des graines distinctes est garanti.
- *Neutralisé par construction.* L'appariement sur l'entropie de sortie neutralise en revanche exactement $\sum p_i^2$ pour les copies honnêtes. Ce qui reste à mesurer doit donc être défini contre une nulle d'invariance aux étiquettes, ce que C n'écrit pas.

**C.9. Statut absent.** La phrase « il existe une frontière statistique d'identifiabilité au-dessous de laquelle *aucun* détecteur ne peut garantir… » (§1, point 3) est formulée comme un fait et ne porte aucun statut. Je la traite comme une `HYPOTHÈSE` de ma part, sans la reclasser chez C.

### (b) Conditions de perte de puissance ou de non-jugeabilité

Toutes les conditions ci-dessous sont des `[HYPOTHÈSE]`.

1. **Action 1.**
   - *Plancher.* Le plancher est d'ordre $\sigma_0\sqrt{\epsilon}$ et non $\epsilon$. Pour $\epsilon_{\max}=0{,}015$, $\sqrt{\epsilon}\approx0{,}12$, alors que $2\epsilon\approx0{,}03$ (illustratif). Le critère $\rho>2\epsilon_{\max}$ est donc trop optimiste d'un facteur environ $4\sigma_0$ (illustratif), et la puissance s'effondre quand $\rho\,\delta\lesssim c\,\sigma_0\sqrt{\epsilon}$.
   - *Dérive.* Une dérive bénigne d'amplitude $\eta$ dans les scores honnêtes s'ajoute à ce plancher. Si $\eta\ge\rho\,\delta$, sabotage et dérive ne sont plus identifiables sans covariable de difficulté.
2. **Action 2.** Si la vraisemblance hors échantillon du modèle nul bipartite et celle de l'urne diffèrent seulement par un terme de taille $O(k/N_{\text{événements}})$, avec $k$ le nombre de paramètres ajoutés, le gain n'est pas détectable sans correction de complexité. Si de plus les dates d'entrée sont conditionnées, la loi marginale de la nouveauté est identique sous les deux modèles et seule la covariance conditionnelle reste testable.
3. **Action 3.** Si $P(\text{tension}\mid\text{scission})\approx P(\text{tension}\mid\text{promotion})$, l'AUROC contre les homonymes peut rester élevée alors que le score n'a aucune valeur prédictive sur le destin. Le critère de C ne distingue pas ces deux cas.
4. **Action 4.** Si la précision de base $\pi_0$ est petite, l'estimateur du gain relatif $\hat\pi/\hat\pi_0$ a une variance de l'ordre de $1/(K\pi_0)$ sur $K=50$ (illustratif). Pour $\pi_0$ de l'ordre de quelques pour cent, le seuil de +50 % n'est pas jugeable.
5. **Action 6 et audit des poids.** Borner un $\text{FPR}\le0{,}01$ avec zéro erreur exige $\ge300$ modèles honnêtes (règle de trois ; illustratif, dérivé du seuil illustratif de C), ce qui n'est pas réalisable autour de huit milliards de paramètres. Pour les petits transformeurs, si la variance entre graines du score d'invariance dépasse l'effet visé ($+0{,}20$, illustratif), le résultat n'est pas réplicable avec une seule graine.

### (c) Contrôles négatifs dont l'absence serait fatale

- **Action 1 :**
  - dérive bénigne sans sabotage, à amplitude graduée ;
  - $\epsilon_{\text{réel}}>\epsilon_{\max}$ ;
  - CUSUM calibré sur la *même* référence contaminée.
- **Action 2 :**
  - nulle qui conserve les dates d'entrée *mais* rompt l'adjacence temporelle des nouveautés, par permutation des voisins à l'intérieur de chaque fenêtre ;
  - covariable de croissance exogène par champ.
- **Action 3 :** identités contestées mais promues en principe, appariées en volume de controverse.
- **Action 4 :**
  - jeu de vérité reconstruit à partir des seuls ponts réalisés après $t_0$, et non de l'intérêt jugé ;
  - extracteurs figés avant coupure.
- **Action 5 :**
  - opérateurs plantés sans symétrie ;
  - nulle grammaticale bien typée.
- **Action 6 :**
  - au moins 5 graines par configuration (illustratif) ;
  - famille de perturbations disjointe tirée par l'évaluateur.
- **Coordination :** permutation indépendante de l'ordre et des étiquettes des options pour chaque copie.

### Test de recevabilité proposé (inférence forte)

- **$H_A$** : la frontière de détectabilité de l'e-processus robuste est linéaire en $\epsilon$, conformément au critère de C. La pente log-log de $(\rho\delta)_{\min}$ en fonction de $\epsilon$ vaut environ 1.
- **$H_B$** : la frontière suit $\sigma_0\sqrt{\epsilon}$. La pente vaut environ $1/2$ et l'ordonnée à l'origine est proportionnelle à $\sigma_0$.
- **Métrique :** pente estimée sur une grille de $\epsilon$ et de $\sigma_0$, avec intervalle bootstrap.
- **Règle de décision :** un intervalle qui exclut $1/2$ réfute $H_B$. Un intervalle qui exclut $1$ réfute $H_A$. Un intervalle qui contient les deux impose d'élargir la grille avant toute conclusion ; ce n'est pas une issue acceptable.
- **Contrôle négatif :** $\rho=0$, pour lequel aucune détection ne doit dépasser $\alpha$.
- **Premier pas sur processeur seul :** simulation NumPy, de l'ordre de quelques heures sur un poste (illustratif).

---

## Ce que cette critique ne tranche pas

- Les constantes du plancher robuste ($c$) et leur dépendance à la forme de la loi honnête : je ne les connais pas, et la référence est à vérifier.
- Pour l'invention d'objets hors alphabet, je ne sais pas construire un contrôle négatif qui soit à la fois bien typé et garanti sans redondance réelle. Les deux propositions butent sur ce point, et je n'ai pas de solution.

FIN-DE-CELLULE