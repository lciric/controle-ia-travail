# Avis de conception

Les documents sources cités ne sont pas joints : je dispose du résumé transmis, pas des pièces primaires ni de leurs empreintes recalculées.

**Statuts employés.** Les faits repris ci-dessous conservent leur statut. Toutes les propositions de conception et toutes les anticipations de performance sont des **HYPOTHÈSES**. Les énoncés mathématiques sont des déductions sous hypothèses explicites, et non des résultats expérimentaux sur l’organisme. Aucun paramètre expérimental chiffré n’est proposé.

**Recommandation — HYPOTHÈSE.** Commencer par des **plans combinatoires de recherche d’interactions**, puis essayer des **arbres de continuation sans sélection intermédiaire**. Une troisième voie, les **plans déterminantaux**, offre une garantie précise de couverture, mais seulement sur les plans de recherche, pas directement sur les idées. Ces méthodes doivent modifier **l’amont des propositions**, jamais récompenser leur nouveauté ni assouplir leur admission.

## Ce que la question suppose sans l’établir

- **RAPPORTÉ.** Les appels actuels repartent déjà en session neuve. Le remède extérieur consistant à réinitialiser le contexte n’est donc pas directement transposable.
- **RAPPORTÉ.** Les observations extérieures associent changement de bassin et gain ; elles ne démontrent ni un effet causal du changement, ni un bénéfice dans cet organisme.
- **HYPOTHÈSE.** Un bassin sémantique possède une représentation exploitable dans les informations publiques : interaction entre traits, condition, sous-problème, composition. Sans ce lien, une méthode mathématique ne sait pas où exercer sa pression.
- **HYPOTHÈSE.** On peut modifier la distribution des idées par des plans de recherche, sans seulement modifier leur vocabulaire.
- **HYPOTHÈSE.** Les bassins recherchés sont exprimables dans la grammaire, additionnels au nul et détectables avec le budget du juge.
- **HYPOTHÈSE.** Une meilleure couverture des propositions brutes survit au regroupement, au choix du représentant et au test de mort.

Il faut surtout séparer des quantités différentes. Pour une distribution de propositions \(Q\), un bassin \(\mathcal B\), une région de traits \(A\) et une loi plantée \(P^\star\), posons :

\[
w=Q(\mathcal B),\qquad r=P_X(A),\qquad
\Delta=\inf_{p\in\mathcal N}
\mathbb E_{P^\star}\log\frac{P^\star(Y\mid X)}{p(Y\mid X)}.
\]

- \(w\) est la **largeur propositionnelle** ;
- \(r\) est la **fréquence d’une région de données** ;
- \(\Delta\) est un **gain prédictif populationnel contre le nul**, lorsque ces divergences sont définies.

Une interaction peut être invisible marginalement sans être rare dans les données. Un effet peut être fort dans une région rare tout en ayant un faible gain global. Enfin, une longue chaîne de construction n’implique pas un grand gain. Je mesurerais ces dimensions séparément.

## Le préalable commun : préserver la garde

**RAPPORTÉ.** La garde actuelle cède hors de sa classe de recombinaisons. **OBSERVÉ-NON-AUDITÉ.** Le premier tour signale précisément que la pression vers la diversité risque d’y pousser les propositions.

**HYPOTHÈSE de conception.** Avant tout duel, définir une classe opérationnelle de copies \(\mathcal C(\mathcal A)\), engendrée par l’archive \(\mathcal A\), avec des opérateurs et des limites explicites : conditions publiques admissibles, mélanges, produits ou compositions concernés. Il faut soit :

- prouver que le nul couvre cette classe ;
- soit restreindre l’expérience à une classe effectivement couverte.

Élargir le nul sans limite n’est pas une solution : il peut alors absorber les découvertes recherchées.

**Déduction conditionnelle.** Une construction suffisante, parfois très conservatrice, illustre ce que signifie une certification absolue. Pour une carte scellée \(q\), posons

\[
E(q)=\prod_i
\frac{q(Y_i\mid X_i)}
{\sup_{p\in\mathcal N}p(Y_i\mid X_i)}.
\]

Sous \(P^\star\in\mathcal N\), avec tirages frais et cartes fixées avant leurs issues,

\[
\mathbb E\!\left[
\frac{q(Y_i\mid X_i)}
{\sup_{p\in\mathcal N}p(Y_i\mid X_i)}
\,\middle|\,X_i,\text{passé}
\right]\leq \sum_y q(y\mid X_i)=1.
\]

L’itération donne \(\mathbb E E(q)\leq1\). Ce n’est **pas** une description du juge existant : c’est un exemple de preuve possible. Son calcul et sa puissance peuvent être prohibitifs.

Le regroupement peut ensuite dépendre des cartes et d’instances sans issue ; des moyennes à poids fixés avant les issues restent des valeurs e valides si la validité est conditionnelle à ces informations. Prendre le maximum ne le permet pas.

**RAPPORTÉ.** La garantie actuellement décrite porte sur le nul de l’archive, pas sur la fraction de fausses découvertes définies par l’oracle. Aucune méthode ci-dessous ne transforme cette garantie en une autre. Le contrôle entre générations doit également être explicité, pas seulement celui à l’intérieur d’une génération.

## Méthode A — Plans combinatoires pour interactions clairsemées

### Objet mathématique

**HYPOTHÈSE structurelle.** Une idée utile dépend d’un petit ensemble inconnu \(I\) de traits publics, de cardinal \(t\). Un appel peut raisonnablement examiner un bloc \(S\) de \(k\) traits.

Construire des blocs \(S_1,\ldots,S_M\) tels que

\[
\forall I,\ |I|=t,\qquad
n_I=\#\{j:I\subseteq S_j\}\geq \lambda.
\]

C’est un problème de couverture combinatoire. Une borne nécessaire est

\[
M\binom{k}{t}\geq\lambda\binom{d}{t},
\]

car chaque bloc couvre au plus \(\binom{k}{t}\) interactions de taille \(t\).

La propriété est vérifiable exhaustivement pour un univers suffisamment petit. On peut chercher les blocs par optimisation entière ou heuristique, mais **la couverture finale doit être certifiée**, indépendamment de la méthode de recherche.

### Pourquoi cela pourrait battre les tirages indépendants

Pour des blocs indépendants uniformes de taille \(k\), la probabilité de contenir une interaction donnée est

\[
p=\frac{\binom{k}{t}}{\binom{d}{t}}.
\]

La probabilité de l’exposer au moins une fois est \(1-(1-p)^M\). Une couverture certifiée l’expose nécessairement.

Une garantie plus forte existe pour un plan équilibré satisfaisant \(n_I=\lambda=Mp\). Supposons que chaque exposition découvre l’idée avec probabilité \(s\), indépendamment, et que les autres traits du bloc n’influencent pas \(s\). Alors :

\[
P_{\mathrm{plan}}(\text{échec})=(1-s)^{Mp},
\qquad
P_{\mathrm{iid}}(\text{échec})=(1-ps)^M.
\]

La concavité du logarithme donne

\[
p\log(1-s)\leq\log(1-ps),
\]

donc le plan équilibré ne fait pas moins bien dans ce modèle.

**Limite de la preuve.** Elle ne démontre ni l’indépendance des réponses des modèles, ni leur capacité à examiner réellement toutes les interactions du bloc.

### Lien avec les effets invisibles en moyenne

Pour des traits indépendants uniformes \(X_j\in\{-1,+1\}\), les caractères

\[
\chi_I(X)=\prod_{j\in I}X_j
\]

vérifient

\[
\mathbb E[\chi_I(X)\mid X_S]=0
\quad\text{si }I\not\subseteq S.
\]

**Esquisse.** Un facteur non observé conserve une moyenne nulle ; l’indépendance annule le produit conditionnel.

Cette identité explique pourquoi une recherche exclusivement marginale peut manquer une interaction, et pourquoi exposer conjointement ses traits est pertinent. Elle ne prouve pas que le proposeur la trouvera.

### Implantation et informations

**HYPOTHÈSE de conception.**

- L’orchestrateur construit les blocs à partir des noms et domaines des traits publics.
- Chaque appel reçoit **l’archive entière**, plus un axe d’examen : interactions et contrastes conditionnels dans son bloc.
- Aucun résultat du juge, aucune issue secrète et aucun score de nouveauté n’interviennent.
- Les cartes finales restent soumises à la grammaire et à la garde habituelles.

Il n’y a ni quota de formes grammaticales ni masquage d’archive : on répartit des **questions de recherche**, pas des formes de réponses.

### Risques

**HYPOTHÈSES à tester.** Le bon support peut être trop grand ; les traits publics peuvent être une mauvaise base ; examiner un bloc peut coûter exponentiellement en sa taille ; les proposeurs peuvent ignorer l’axe demandé. Une amélioration de couverture des blocs ne vaut donc pas encore amélioration de couverture des idées.

## Méthode B — Arbres de continuation sans récompense intermédiaire

### Objet mathématique

**HYPOTHÈSE structurelle.** Certaines idées exigent un préfixe coûteux à construire, mais réutilisable : une condition, une factorisation, une représentation ou un programme partiel.

On génère \(u\) préfixes, puis \(b\) continuations indépendantes pour chacun. **Tous les préfixes reçoivent le même traitement prévu d’avance** ; aucun n’est choisi parce qu’un moniteur le trouve prometteur.

Soient :

- \(c_0\), coût d’un préfixe ;
- \(c_1\), coût d’une continuation ;
- \(p\), probabilité qu’un préfixe soit utile ;
- \(s\), probabilité qu’une continuation réussisse sachant un préfixe utile.

Avec indépendance conditionnelle, un arbre échoue avec probabilité

\[
1-p\bigl[1-(1-s)^b\bigr].
\]

Pour \(u\) arbres indépendants :

\[
P_{\mathrm{arbre}}(\text{échec})
=\left[1-p\bigl(1-(1-s)^b\bigr)\right]^u,
\qquad
C=u(c_0+bc_1).
\]

Le témoin reconstruit un préfixe pour chaque proposition. Pour \(n\) tentatives :

\[
P_{\mathrm{iid}}(\text{échec})=(1-ps)^n,
\qquad C=n(c_0+c_1).
\]

En négligeant seulement les arrondis budgétaires, la comparaison exacte se fait entre les taux

\[
\frac{-\log\!\left(1-p[1-(1-s)^b]\right)}{c_0+bc_1}
\quad\text{et}\quad
\frac{-\log(1-ps)}{c_0+c_1}.
\]

### Pourquoi cela pourrait aider

**Déduction conditionnelle.** Si reconstruire un préfixe coûte cher et que plusieurs continuations exploitent réellement le même préfixe utile, sa mutualisation peut augmenter la probabilité de découverte par unité de coût.

Inversement, si le préfixe utile est très rare et les continuations presque toujours fructueuses, multiplier les préfixes est préférable. Ce dispositif n’a donc **aucune garantie uniforme**.

Pour une chaîne plus longue, le même calcul devient récursif ; sans structure réutilisable, l’arbre peut simplement consommer un budget exponentiel.

### Implantation et informations

**HYPOTHÈSE de conception.**

- Le modèle produit un objet intermédiaire typé, sans score : hypothèse de condition, décomposition ou esquisse de loi.
- L’orchestrateur le sérialise dans de nouveaux appels, toujours sans historique conversationnel.
- Les branches et leurs budgets sont fixés avant la course.
- Les objets intermédiaires ne sont ni promus ni présentés comme des lois acceptées.
- Seules les cartes terminales passent le juge.

C’est un **dessin neuf**, puisque la vue contient des brouillons de recherche en plus des éléments actuellement rapportés. Leur provenance doit être explicite.

### Compatibilité et risques

Aucun score de moniteur ne pilote le branchement ; aucun verdict ne revient au proposeur. Les dépendances entre cartes terminales ne détruisent pas à elles seules la validité des valeurs e.

**HYPOTHÈSES de risque.** Le partage du préfixe peut ancrer toutes les branches dans la même erreur. Il peut accroître les doublons ou seulement économiser des tokens sans découvrir davantage. Surtout, un arbre qui sélectionnerait ses préfixes par « potentiel » noté réintroduirait précisément le signal interdit : je ne le recommande pas.

## Méthode C — Plans déterminantaux, répulsion des axes plutôt que des idées

### Objet mathématique

**HYPOTHÈSE de conception.** Constituer avant la course un ensemble fini de plans publics : blocs d’interactions, contrastes conditionnels, décompositions ou transformations admissibles.

Soit une matrice \(V\in\mathbb R^{N\times M}\) à colonnes orthonormales. Le noyau

\[
K=VV^\top
\]

définit une loi déterminantale de projection sur des ensembles de \(M\) plans :

\[
P(S)=\det(K_S),\qquad |S|=M.
\]

Les lignes de \(V\) décrivent des plans, **pas la qualité des propositions obtenues**. La loi réduit la co-sélection de plans fortement alignés dans cette représentation.

### Garantie exacte contre un témoin indépendant

Supposons qu’un appel suivant le plan \(i\) atteigne un bassin fixé avec probabilité \(a_i\). Les réponses sont indépendantes conditionnellement aux plans.

Alors

\[
P_{\mathrm{det}}(\text{aucun succès})
=\det\!\left(I_M-V^\top\operatorname{diag}(a)V\right).
\]

Le témoin tire indépendamment \(M\) plans avec probabilités

\[
\pi_i=\frac{K_{ii}}{M}.
\]

Sa probabilité de succès par appel est

\[
q=\sum_i\pi_i a_i.
\]

Les valeurs propres \(\mu_j\) de
\(V^\top\operatorname{diag}(a)V\) appartiennent à \([0,1]\), et leur somme vaut \(Mq\). Donc

\[
P_{\mathrm{det}}(\text{aucun succès})
=\prod_j(1-\mu_j)
\leq
\left(1-\frac{\sum_j\mu_j}{M}\right)^M
=(1-q)^M.
\]

**Esquisse.** C’est l’inégalité arithmético-géométrique appliquée aux \(1-\mu_j\). Le membre de droite est exactement l’échec du témoin indépendant.

La même comparaison vaut bassin par bassin, donc aussi pour l’espérance du nombre de bassins atteints.

### Ce que cette preuve ne dit pas

Elle suppose :

- un coût identique par plan ;
- des probabilités \(a_i\) stables pendant le lot ;
- l’indépendance conditionnelle des réponses ;
- un bassin fixé indépendamment des réponses observées.

Elle ne garantit pas un gain important. Si le noyau ne représente aucune redondance pertinente, l’inégalité peut être presque une égalité. Elle ne résout pas non plus la puissance du juge.

### Implantation et contraintes

**HYPOTHÈSE de conception.** L’orchestrateur calcule le noyau à partir de métadonnées publiques gelées, puis tire le lot avant les appels.

Cela ne rouvre pas le rejet d’une récompense numérique de nouveauté :

- aucun score n’est calculé sur les idées produites ;
- aucun score n’est servi à un agent ;
- aucune promotion n’en dépend ;
- aucun nombre de cartes par forme grammaticale n’est imposé.

**Risque.** Si le noyau est ajusté pendant la course à partir des résultats ou de la diversité constatée, cette séparation disparaît. Pour le premier essai, il doit rester fixe.

## Ce qui est impossible sans structure

### Trouver un bassin arbitraire sans information

**Déduction conditionnelle.** Considérons \(N\) plans échangeables et un unique plan utile, choisi uniformément et indépendamment de toute information publique. Toute méthode examinant au plus \(M\) plans distincts a une probabilité de succès au plus \(M/N\).

**Preuve.** Conditionnellement à l’ensemble examiné, le plan utile y appartient avec probabilité égale à sa taille divisée par \(N\).

Éviter les répétitions aide ; identifier une direction privilégiée est impossible sans information supplémentaire.

### Détecter un effet rare sans observations suffisantes

Pour deux mondes \(P_0,P_1\) ne différant que dans une région de masse \(r\), si la divergence conditionnelle moyenne dans cette région vaut \(\kappa\), alors, sous tirages indépendants,

\[
D_{\mathrm{KL}}(P_1^{\,n}\Vert P_0^{\,n})=nr\kappa.
\]

L’inégalité entre variation totale et divergence donne

\[
\operatorname{TV}(P_1^{\,n},P_0^{\,n})
\leq\sqrt{\frac{nr\kappa}{2}}.
\]

Un test de niveau \(\alpha\) a donc une puissance au plus
\(\alpha+\sqrt{nr\kappa/2}\), plafonnée par l’unité. Une idée correctement formulée peut rester statistiquement indémontrable au budget disponible.

### Reconnaître universellement « la même idée »

**Déduction conditionnelle.** Dans une grammaire finie et bornée, certaines équivalences sont décidables par énumération. Pour des langages de programmes généraux, l’équivalence fonctionnelle ne l’est pas en général. Même une égalité prédictive ne définit pas à elle seule une identité sémantique.

**HYPOTHÈSE de conception.** La garde doit donc annoncer la fermeture opérationnelle qu’elle couvre, sans prétendre couvrir toute notion possible de copie.

Les gains proposés exigent respectivement **clairsemance des interactions**, **réutilisation de préfixes**, ou **redondance représentable entre plans**.

## L’expérience décisive la moins chère

### Duel retenu

**HYPOTHÈSE de conception.** Tester d’abord la méthode A, seule, contre son témoin indépendant. Ne pas combiner les méthodes : un succès deviendrait difficile à attribuer.

- \(H_A\) : à coût égal, la couverture combinatoire augmente d’au moins \(\delta_{\min}>0\) la couverture oracle finale des composantes ciblées.
- \(H_B\) : ce gain est inférieur à \(\delta_{\min}\).

Le seuil \(\delta_{\min}\), la tolérance budgétaire, le niveau d’incertitude et le nombre maximal de courses sont gelés avant les courses décisives.

### Monde planté réglable

**HYPOTHÈSE — famille illustrative.** Une composante simple est

\[
P_\theta(Y=1\mid X)
=\frac12+\beta\,\mathbf1_A(X)\chi_I(X),
\qquad |\beta|<\frac12,
\]

avec porte \(A\) dépendant de traits disjoints de \(I\), et traits de \(I\) symétriques indépendants.

Cette famille permet de régler :

- la rareté observationnelle \(r=P_X(A)\) ;
- la complexité d’exposition par \(|I|\), la taille des blocs et le nombre de traits ;
- le gain conditionnel par \(|\beta|\).

Contre la loi constante, le gain populationnel vaut

\[
\Delta=r\,g(\beta),
\]

où

\[
g(\beta)=
\left(\frac12+\beta\right)\log(1+2\beta)
+\left(\frac12-\beta\right)\log(1-2\beta).
\]

**Limite importante.** Ces paramètres ne règlent pas directement \(w\), la largeur sous la distribution des propositions des modèles. Celle-ci doit être estimée dans un pilote indépendant, puis les paramètres gelés. Dire « bassin étroit » sur la seule base d’un grand \(|I|\) serait abusif.

La profondeur comme gain est réglée ici ; la profondeur comme chaîne de dépendances demande un essai distinct. Une interaction complexe ne prouve pas une découverte obligatoirement séquentielle.

### Témoin réellement comparable

Le bras structuré reçoit un plan de blocs certifié. Le témoin reçoit des blocs indépendants uniformes, avec **les mêmes consignes, les mêmes modèles et la même archive entière**.

Une permutation aléatoire commune des noms de traits du plan structuré donne à chaque bloc la même distribution marginale que dans le témoin. La différence porte alors sur la coordination du lot, non sur un meilleur contenu individuel de consigne.

**HYPOTHÈSE de contrôle budgétaire.** Fixer les mêmes enveloppes d’appels, de tokens, de tirages du juge et de calcul ; publier les coûts réellement mesurés. Un résultat hors de la tolérance de coût préenregistrée ne tranche pas la question « à coût égal ».

### Métrologie et décision

**Métrique principale :** nombre de composantes plantées, certifiées additionnelles et détectables, couvertes par les **retenues**. Lire aussi les propositions brutes et les représentants pour localiser les pertes.

La définition de « couverte » doit inclure une récupération prédictive contre un monde où la composante est ablatée, y compris dans sa strate pertinente ; pas une ressemblance textuelle.

Déclarer \(H_A\) soutenue seulement si la borne inférieure de l’intervalle préenregistré du gain apparié dépasse \(\delta_{\min}\), avec coût conforme et garde intacte. Si l’intervalle chevauche le seuil : résultat indécis.

### Contrôles et ordre des dépenses

**HYPOTHÈSE de protocole.**

D’abord, sans proposeur :

- certifier les couvertures des plans ;
- tester la garde sur des cartes de recombinaison adversariales ;
- vérifier qu’une carte témoin exacte, réservée au banc et jamais servie aux proposeurs, est détectable.

Ensuite, sous devis et GO, effectuer le duel minimal avec proposeurs.

Contrôles négatifs :

- \(\beta=0\), absence de composante ciblée ;
- composante déjà contenue dans la fermeture déclarée de l’archive ;
- consigne focalisée remplacée par une consigne neutre, pour vérifier que les blocs agissent effectivement sur les réponses.

Un banc sans proposeur peut réfuter la conception, **pas démontrer que les modèles découvrent mieux**. L’oracle est lu après les courses pour l’évaluation ; aucun retour ne modifie les appels, leur composition ou leur durée. Le lecteur neuf applique les critères gelés et le même audit aux résultats positifs et négatifs.

## Ce qui me ferait changer d’avis

**HYPOTHÈSES de réfutation.**

Je renoncerais à privilégier les plans combinatoires si :

- les blocs sont mieux couverts, mais les interactions découvertes ne le sont pas ;
- le gain disparaît face au témoin de mêmes consignes et mêmes distributions marginales ;
- les bassins ciblés ne sont pas clairsemés dans les traits publics ;
- le coût de l’examen conjoint absorbe le bénéfice ;
- les gains bruts disparaissent au stade des retenues ;
- la garde élargie absorbe aussi les composantes supposées nouvelles.

Je privilégierais les arbres si des préfixes réutilisables réduisent effectivement le coût de découverte sans multiplier les copies. Je privilégierais les plans déterminantaux si leurs hypothèses de stabilité et d’indépendance sont suffisamment satisfaites et si le gain mesuré dépasse celui d’un simple évitement des répétitions.

**Conclusion — HYPOTHÈSE.** La piste défendable n’est pas de calculer une « originalité » à récompenser. C’est de remplacer des efforts redondants par une exploration coordonnée de structures publiques, avec une preuve locale de couverture ou d’économie, puis de laisser une garde indépendante décider de l’addition prédictive. Le passage de cette preuve locale aux découvertes réelles reste précisément l’objet du duel.

FIN-DE-CONSULTATION