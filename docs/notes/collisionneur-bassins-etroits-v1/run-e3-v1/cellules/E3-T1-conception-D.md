# Proposition D

**Statuts.** Je n’ai contre-lu aucune des sources : je conserve leurs statuts sans les rehausser. Sauf mention contraire, les méthodes et résultats attendus ci-dessous sont des **HYPOTHÈSES de conception**. Tous les seuils, effectifs et coûts proposés sont **illustratifs**.

## 1. Ce que la question suppose sans que ce soit établi

| Supposition | Statut et conséquence |
|---|---|
| Un « groupe prédictif » ou un groupe de doublons représente un bassin d’idées. | **HYPOTHÈSE.** Le regroupement rapporté dans [C3] repère des formes canoniques égales ou des lois presque équivalentes ; deux cartes prédictivement proches peuvent encore provenir d’idées différentes, et deux étapes d’une même idée peuvent être éloignées. |
| La largeur est réglable par le programme qui plante le monde. | **HYPOTHÈSE**, et probablement fausse si elle est prise littéralement. Le programme règle la loi du monde ; la probabilité qu’un modèle propose spontanément l’idée dépend aussi du modèle, de la consigne et de l’archive. La largeur doit donc être **estimée sur des tirages d’étalonnage**, pas décrétée par l’oracle. |
| La profondeur admet une scalaire comparable entre mondes. | **HYPOTHÈSE.** Il faut la définir, par exemple comme le gain de vraisemblance sur tirages frais de la composante complétée par l’oracle sur la meilleure loi du nul élargi. Un grand effet brut ne suffit pas s’il est indétectable à taille d’échantillon disponible. |
| « Invisible en moyenne » implique « rarement proposé ». | **HYPOTHÈSE.** La composante conditionnelle, son annulation moyenne et la chaîne de profondeur 2 sont **RAPPORTÉES** dans [C4] ; sa découverte par de vrais proposeurs après archivage de sa condition est explicitement une **HYPOTHÈSE**. |
| Il existe plusieurs bassins étroits, profonds, exprimables dans les six formes et accessibles depuis la seule vue publique. | **HYPOTHÈSE.** Rien dans v67 ne l’établit. Les onze variantes proches et l’absence de promotion en génération 2 sont **RAPPORTÉES**, pour une course, sans généralisation démontrée. |
| Une consigne calculée sans oracle peut déplacer la loi des propositions vers ces bassins. | **HYPOTHÈSE.** Elle peut aussi seulement accroître le nombre de `si_sinon` et `melange`, ou produire des cartes non pertinentes. |
| Les résultats Bespoke se transfèrent à cet organisme. | **RAPPORTÉ**, observationnel et non reproduit pour les chiffres ; **HYPOTHÈSE** pour tout transfert causal. Ils ne démontrent ni l’effet des réinitialisations ni l’existence d’un gain à budget égal ici. |
| Le nul peut être élargi sans rendre le test invalide ou trop conservateur. | **HYPOTHÈSE.** La limite du juge hors de la classe du nul est **RAPPORTÉE**. Sa preuve ne borne pas les fausses découvertes au sens de l’oracle. |
| Des appels indépendants constituent le témoin pertinent. | **HYPOTHÈSE.** Les sessions neuves sont **RAPPORTÉES**, mais l’indépendance stochasticité des sorties, à modèle et vue identiques, doit être décrite précisément : graines, décodage, version et coût. |

Enfin, agir sur les consignes pendant une course est un **dessin neuf**, puisque [C3] rapporte que D2 ne doit pas piloter ces consignes. Le pilote ci-dessous ne modifie donc pas silencieusement la course en cours.

## 2. Méthodes, classées par coût de test et adéquation au problème

### M1 — Plans de couverture de questions publiques

**Objet exact.** Construire, avant tout résultat, un ensemble fini \(U\) de questions ne utilisant que les traits publics, les strates publiques et les lois archivées : « l’effet du trait \(i\) change-t-il de signe selon le signe du trait \(j\) ? », « une pente archivée persiste-t-elle dans chaque strate ? », etc. Un **tableau couvrant** de force \(t\) est une matrice dont les lignes attribuent des niveaux à \(k\) facteurs, telle que, pour tout choix de \(t\) facteurs, chaque combinaison de niveaux apparaisse au moins une fois.

L’orchestrateur affecte ces lignes à des appels ou à des angles de recherche. Il n’impose ni forme grammaticale ni quota de cartes par angle.

**Preuve et conjecture.** La couverture du tableau est vérifiable mécaniquement. Pour \(M\) questions et \(N\) affectations indépendantes uniformes, le nombre moyen de questions distinctes est
\[
M\left[1-(1-1/M)^N\right],
\]
alors qu’un programme équilibré en couvre \(\min(N,M)\). C’est une preuve sur la **couverture des consignes**, pas sur les idées produites. Que cela augmente la couverture certifiée par l’oracle reste une **conjecture**.

**Action et informations.** Programme hors agent ; vue complète conservée ; aucun verdict, score de nouveauté, résultat du juge ou tirage du monde. Les questions sont scellées avant les réponses.

**Pourquoi un gain serait possible.** À nombre d’appels fixe, on supprime des redondances d’affectation et on garantit que certaines conditions peu spontanées sont au moins examinées. Cela ne garantit ni leur examen effectif par le modèle ni leur expression dans la grammaire.

**Risques et compatibilité.** Verrouillage sur un mauvais dictionnaire ; consignes plus longues ; superficialité due à trop d’angles. Ce n’est ni une récompense numérique de nouveauté, ni un quota de formes, ni un masquage d’archive. En revanche, cela peut accroître la pression vers `si_sinon` et `melange` : les objections du premier tour, **OBSERVÉ-NON-AUDITÉ**, imposent donc de qualifier la garde avant toute comparaison de bras.

### M2 — Moments orthogonaux et géométrie locale de l’information

**Objet exact.** Pour une loi archivée \(P_0\), construire des statistiques publiques \(h(x,y)\), orthogonalisées contre ses scores paramétriques. Considérer les déformations normalisées
\[
p_\theta(y\mid x)=p_0(y\mid x)
 \exp\{\theta h(x,y)-a(\theta,x)\}.
\]
Sous régularité,
\[
D_{\mathrm{KL}}(P_0\|P_\theta)
=\frac{\theta^2}{2}\operatorname{Var}_{P_0}(h)+o(\theta^2).
\]
On retient notamment des \(h\) dont la moyenne globale est nulle mais dont la variance conditionnelle dans certaines strates ne l’est pas. Le cas \(h=\operatorname{signe}(x_j)(y-\mu_0(x))\), avec signe équilibré, formalise le type d’invisibilité moyenne décrit dans [C4].

**Preuve et conjecture.** L’orthogonalité et le développement local sont calculables ou vérifiables sous hypothèses explicites. Ils montrent seulement qu’une petite déformation n’est pas, au premier ordre, une petite variation des paramètres archivés considérés. Ils ne prouvent ni qu’elle est hors de **toutes** les recombinaisons du nul, ni que le monde la contient. Que fournir ces angles en langage naturel aide les proposeurs est une **conjecture**.

**Action.** L’orchestrateur peut calculer les moments à partir des lois d’archive et de simulations issues de ces seules lois, sans issues réelles ni oracle. M1 distribue ensuite les angles. À la génération suivante, le dictionnaire peut utiliser une condition désormais archivée, ce qui teste la chaîne de profondeur 2.

**Pourquoi un gain serait possible.** Au lieu de demander génériquement « soyez original », on couvre des directions précisément invisibles à une lecture marginale. Le gain requiert que la composante vraie soit proche du dictionnaire et que le modèle sache la traduire dans la grammaire.

**Risques.** Faux sentiment d’exhaustivité ; explosion combinatoire ; orthogonalité valable seulement autour de \(P_0\) ; fuite si les strates sont choisies après observation des résultats. Aucun score d’orthogonalité n’est servi comme récompense ni utilisé pour promouvoir.

### M3 — Divergences localisées pour ne pas confondre rareté et copie

**Objet exact.** Pour une famille finie \(\mathcal A\) de strates publiques fixée à l’avance, définir une divergence conditionnelle \(D_A(P,Q)\), puis
\[
\delta(P)=\max_{A\in\mathcal A}\inf_{Q\in\mathcal N^\*}
D_A(P,Q),
\]
où \(\mathcal N^\*\) est une version explicitement calculable du nul, incluant si possible les recombinaisons pertinentes. Pour une divergence additive, une différence confinée à \(A\) est multipliée par la masse \(r(A)\) dans la moyenne globale : la lecture globale peut donc la diluer.

**Preuve et conjecture.** La dilution et l’invariance aux reparamétrisations exactes sont mathématiquement vérifiables. Que \(\delta\) mesure une « idée » est faux en général ; qu’il améliore le diagnostic des bassins rares est une **conjecture**.

**Action.** Audit hors ligne, construction de cas difficiles et lecture descriptive par strates. Jamais de sélection par \(\delta\), jamais de prime servie aux agents.

**Risques.** Maximum optimiste sur beaucoup de strates, bruit de Monte-Carlo, strates trop petites, infimum intraitable. Une différence locale peut être une vraie découverte ou une copie légèrement modifiée : \(\delta\) seul ne tranche pas.

### M4 — E-valeurs robustes pour un nul composite explicite

**Objet exact.** Soit un nul dominé \(\mathcal N\), et une alternative candidate de densité \(q\), fixée avant les tirages d’évaluation. Lorsque le dénominateur est fini et calculable :
\[
e(X)=\frac{q(X)}{\sup_{P\in\mathcal N}p(X)}.
\]
Pour tout \(P_0\in\mathcal N\), \(\sup_{P\in\mathcal N}p(X)\ge p_0(X)\), donc, avec le traitement usuel des supports,
\[
\mathbb E_{P_0}[e(X)]\le
\mathbb E_{P_0}\!\left[\frac{q(X)}{p_0(X)}\right]\le 1.
\]

**Preuve et conjecture.** Cette inégalité est une preuve pour le nul effectivement spécifié. Une approximation sur grille ne vaut que pour cette grille. E-BH appliqué à de telles e-valeurs conserve sa garantie statistique pertinente ; cela ne prouve ni nouveauté sémantique ni contrôle des fausses découvertes au sens de l’oracle. La puissance suffisante reste une **conjecture**.

**Action.** Uniquement dans le juge mécanique, après preuve et tests de programmation. Aucun retour aux proposeurs.

**Risques.** Conservatisme extrême, supremum coûteux, alternative dépendant des données d’évaluation — ce dernier cas invalide la construction. M4 ne « certifie » rien hors du nul mathématiquement couvert.

## 3. Impossibilités et conditions de structure

1. **Pas de gain universel à vue identique.** Si deux mondes ont même vue publique et même archive mais des composantes cachées différentes, toute procédure limitée à cette vue produit la même loi de sorties dans les deux mondes. Avec \(K\) bassins symétriques incompatibles et aucune information les distinguant, aucun algorithme ne peut favoriser le bon dans tous les mondes. Un gain exige une structure exploitable : dictionnaire informatif, conditions publiques, ou archive séquentielle.
2. **La profondeur ne peut pas être optimisée directement sans information sur le monde.** On peut couvrir des directions ou estimer une détectabilité locale ; on ne peut pas classer les bassins inconnus par leur gain réel à partir de la seule vue.
3. **Aucune certification empirique n’est absolue hors du nul.** Même un million de contrôles négatifs ne prouve pas la validité pour toutes les recombinaisons non spécifiées. Si « certifiée en absolu » signifie littéralement pour toute loi hors classe, l’exigence est irréalisable. L’interprétation opérationnelle possible est : preuve d’e-valeur pour un nul explicite, plus audit séparé des erreurs au sens de l’oracle.
4. **Expressibilité et support non nul sont nécessaires.** Une idée hors grammaire est rejetée ; une idée à probabilité nulle sous toutes les consignes autorisées ne sera pas trouvée. Même avec support non nul, la profondeur doit être détectable avec les tirages frais disponibles.

Un gain est donc plausible seulement si les composantes ciblées sont exprimables, proches des questions M1–M2, accessibles après des consignes publiques, et testables contre un nul assez riche mais calculable.

## 4. Validation minimale des instruments

| Instrument | Cas honnêtes appariés et détection | Fausses alertes | Vérifications mécaniques à battre |
|---|---|---|---|
| M1+M2 | Mondes appariés avec composante conditionnelle présente/absente, mêmes traits publics et profondeurs calibrées. Mesurer composantes trouvées dans les propositions brutes, représentants et retenues, par coût. | Promotions sur monde sans composante ; copies renommées ; gain dû à la longueur des consignes. | Tirages indépendants ; consigne placebo de même longueur ; simple énumération lexicographique des paires de traits. Si cette énumération égale M1+M2, la sophistication est inutile. |
| M3 | Départ réel confiné à une strate rare contre copie exacte, à distance globale égale. Détection : taux de départs localisés correctement signalés. | Copies exactes, reparamétrisations et bruit Monte-Carlo signalés comme départs. | Canonisation existante, distance globale et regroupement actuel avec lecture par strates. |
| M4 | Alternatives scellées, additionnelles à l’archive, contre mondes dans chaque partie du nul composite. Détection : puissance e-BH à taille fixée. | FDP sur nul composite ; copies et recombinaisons par morceaux/produits/compositions. | Juge actuel et test exact disponible sur nul simple. La simulation contrôle le code, jamais la preuve. |
| Juge et regroupement actuels | Vraies composantes certifiées additionnelles, y compris conditionnelles. | Copies renommées et lois hors classe que le nul ne couvre pas. | Canonisation, générateur mécanique de recombinaisons et calcul oracle hors ligne. Aucun taux observé ne doit être présenté comme garantie absolue. |

## 5. Expérience décisive la moins chère

**Préalable bloquant.** Préenregistrement scellé ; preuve du domaine de validité du juge ; batterie de copies et de mondes nuls. Si les bras augmentent les cartes hors nul sans garde qualifiée, on ne lance pas la comparaison.

**Dessin.** Mondes nouveaux écrits par programme à graine scellée, appariés entre bras, en factoriel large/étroit × peu profond/profond. La largeur est estimée par le taux de succès brut du témoin sur des mondes d’étalonnage distincts ; la profondeur par le gain prédictif oracle certifié. Même modèle, archive, appels, plafonds de tokens et coût. Bras A : M1+M2. Bras B : consignes génériques indépendantes. Aucun bras ne voit verdict, oracle ou loi plantée. Lecteur final neuf et aveugle au bras ; audit identique si le résultat est trop propre.

**Duel.** Soit \(\Delta\) le gain de A sur B en composantes certifiées supplémentaires couvertes par les **cartes retenues**, par course à coût égal, dans la cellule étroit-profond préenregistrée. Seuil pratique \(\delta=0{,}20\) composante par course (**illustratif**) :

- **H_A** : \(\Delta\ge\delta\), sans dégradation mesurée de la garde au-delà de la marge scellée.
- **H_B** : \(\Delta<\delta\), ou dégradation de la garde.

Avec des intervalles à 95 % (**illustratif**) et randomisation au niveau course-monde :

- borne inférieure de \(\Delta\) au-dessus de \(\delta\) et garde non inférieure : **H_B est réfutée dans ce régime** ;
- borne supérieure sous \(\delta\), ou échec de garde : **H_A est réfutée** ;
- intervalles non concluants : l’affirmation « ce pilote était décisif » est réfutée ; on ne tranche pas en regardant le seul estimateur.

**Contrôles.** Monde entièrement dans le nul ; copies renommées injectées mécaniquement ; consigne placebo ; strates permutées, qui ne doivent pas créer de détection. Les trois étages D2 — brutes, représentants, retenues — distinguent « trouver », « ne pas dédoublonner à tort » et « survivre au juge ». Si A gagne, un second essai compare A à l’énumération lexicographique : à coût égal, ne pas la battre réfute l’utilité de la partie sophistiquée, pas nécessairement celle d’une consigne structurée.

## 6. Ancrage matériel

**HYPOTHÈSE de faisabilité.** Pour le pilote bon marché : `Qwen2.5-14B-Instruct` et `Qwen2.5-32B-Instruct`, comme candidats à poids ouverts, versions, licences, quantification et empreintes gelées. Leur aptitude à produire six cartes valides dans la grammaire n’est pas établie. L’inférence est sur GPU ; canonisation, distances et e-valeurs sont sur CPU, sauf supremum du nul potentiellement coûteux.

**Illustratif** : 96 appels, environ 0,5 million de tokens générés, 20–80 GPU·heures sur une carte de 48–80 Go pour le modèle 32B, 50–300 € de location, plus 5–20 CPU·heures ; développement, étalonnage du monde et lecture oracle exclus. La variance du pilote fixe l’effectif réellement nécessaire. Aucune dépense sans devis et GO.

## 7. Ce qui me ferait changer d’avis

J’abandonnerais M1–M2 si le témoin indépendant ou la simple énumération les égale, si le gain reste limité aux propositions brutes, s’il disparaît sur mondes et modèles réservés, ou s’il s’accompagne de copies ou de promotions indues. J’abandonnerais M3–M4 si leur coût ou leur conservatisme annule le gain de couverture.

À l’inverse, je soutiendrais un déploiement limité si un avantage reproduit apparaît spécifiquement dans les mondes étroits-profonds, survit à l’audit des copies et aux mondes réservés, demeure supérieur à l’énumération simple à coût mesuré, et si la garantie du juge reste valide sur un nul explicitement élargi. Une réplication causale des observations Bespoke pourrait aussi rouvrir la question des réinitialisations, mais ne validerait pas ces méthodes par procuration.

FIN-DE-CELLULE