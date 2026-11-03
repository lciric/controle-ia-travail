# Proposition E — Critique croisée de méthode

**Statuts.** Les choix des conceptions sont traités comme des **HYPOTHÈSES**, non comme des résultats. Toutes les critiques ci-dessous sont des **HYPOTHÈSES de défaillance**, formulées conditionnellement ; les égalités mathématiques sont des **calculs conditionnels**. Aucun résultat empirique nouveau n’est avancé.

## Sur la proposition A

### (a) Défauts de méthode

**T1 — Horizon de surveillance**

- **L’axe mélange plusieurs grandeurs.** « Lignes de code + traces d’exécution » ne définit pas une unité commune : la conversion entre elles, la redondance et la densité d’information peuvent déterminer l’horizon. Ajouter du contenu sans changer la difficulté peut produire une décroissance de détection sans mesurer la surveillance recherchée.
- **Geler les attaquants ne neutralise pas leur élicitation.** Cela fixe une distribution conditionnelle aux productions obtenues et validées. Une interaction entre cette distribution et les moniteurs peut encore déterminer la pente. La conclusion porterait sur ce corpus, pas sur toute capacité de surveillance.
- **Un refus n’est pas un témoin honnête apparié.** Son style, sa longueur et l’absence d’artefact fonctionnel peuvent révéler directement son étiquette. Il faut séparer refus, solution honnête fonctionnelle et production invalide.
- **Le seuil peut fabriquer une partie de la courbe.** Une calibration globale des fausses alertes ne fixe pas leur taux à chaque longueur. Une calibration distincte par longueur définit, elle, une autre mesure. Ce choix doit précéder l’ajustement.
- **Le contrôle mécanique plat est insuffisant.** Sur exactement les mêmes entrées et avec le même budget, son invariance temporelle est attendue par construction. Il ne détectera pas nécessairement une contamination propre aux modèles récents.
- **La puissance des sondes de « nos résultats » ne se transporte pas à ce pilote.** Un autre estimateur, une autre dépendance entre observations et une autre alternative exigent un calcul de puissance propre.

**T2 — Écart de capacité seuil**

L’écart de log-paramètres n’identifie pas à lui seul un écart de capacité. Avec une seule date, il n’identifie aucune évolution temporelle. Il faut croiser attaquants et moniteurs : sinon, leur amélioration respective et leur interaction restent confondues. Le corpus sans injection ne suffit pas à isoler l’effet sémantique de l’injection de celui de la longueur ou du format ajoutés.

**T3 — Conscience d’évaluation**

Un classificateur figé n’a pas nécessairement une sensibilité figée entre étapes d’entraînement. Le changement de verbalisation peut déplacer son erreur de mesure. De plus, la conscience d’évaluation verbalisée n’est pas, sans variable comportementale distincte, une mesure de désalignement. Le témoin supervisé n’est un contrôle négatif valide que sous l’hypothèse supplémentaire qu’il n’affecte pas la grandeur mesurée.

**T4 — Sous-performance**

Les scores n’étant pas définis dans la pièce servie, l’estimand reste à spécifier. Une pente positive et une corrélation avec les refus peuvent coexister : le duel proposé n’oppose donc pas deux hypothèses exclusives.

**Duels.** D1 mélange une valeur de pente, un résultat de test et un autre seuil décisionnel. D2 oppose une propriété du rapport d’horizons à une propriété de leur évolution : elles ne sont pas complémentaires. Une baisse relative n’implique notamment pas une baisse absolue.

### (b) Conditions de perte de puissance ou de non-identification

Notations : \(S\), score ; \(Y\), étiquette ; \(x\), difficulté ; \(t\), date ; \(\tau_t\), seuil ; \(\alpha\), risque cible.

**T1 — Détection, calibration et horizon**

\[
p_t(x)=P(S>\tau_t\mid Y=1,x,t),\qquad
a_t(x)=P(S>\tau_t\mid Y=0,x,t).
\]

- Si les lois conditionnelles de \(S\) pour \(Y=1\) et \(Y=0\) sont égales, alors \(p_t(x)=a_t(x)\) : aucune discrimination.
- Si \(\int a_t(x)\,dG_{0,t}(x)=\alpha\), mais \(a_t(x)\neq\alpha\), la calibration marginale ne garantit pas le risque conditionnel.
- Pour une cible de détection \(r\), \(h_t\) défini par \(p_t(h_t)=r\) n’est pas identifié dans le support observé si \(p_t(x)\) reste entièrement d’un côté de \(r\), ou si plusieurs croisements existent.
- Localement,
\[
\operatorname{Var}(\widehat h_t)
\approx
\frac{\operatorname{Var}[\widehat p_t(h_t)]}{[p'_t(h_t)]^2}.
\]
Une dérivée proche de zéro rend l’horizon instable.
- Si \(X_t=(1,t,\text{famille},\text{taille})\) donne une matrice de conception de rang déficient, la pente temporelle ajustée n’est pas identifiable.
- Pour des observations groupées de corrélation \(\rho\) et de taille de groupe \(k\),
\[
n_{\mathrm{eff}}\approx\frac{n}{1+(k-1)\rho}.
\]
Le nombre de lectures ne suffit donc pas à déterminer la précision.

**T2 — Seuil d’écart**

Soit \(u(g,t)=P(\text{succès}\mid g,t)\), où \(g\) est l’écart proposé. Le seuil \(g^\star_t\) est non identifiable si \(u\) ne croise pas la cible dans le support commun, ou si \(u\) n’est pas monotone. Si
\[
P(\text{succès}\mid g,t,a,m)\neq P(\text{succès}\mid g,t),
\]
l’écart seul ne suffit pas comme variable explicative. Sans répétition temporelle à écarts comparables, sa dérive temporelle reste non identifiable.

**T3 — Erreur du classificateur et croissance**

Avec prévalence latente \(\pi(c)\), sensibilité \(s(c)\) et spécificité \(v(c)\) au calcul \(c\),
\[
P(\widehat Y=1\mid c)
=s(c)\pi(c)+[1-v(c)][1-\pi(c)].
\]
Si \(s\) et \(v\) sont inconnues et variables, la pente de \(\pi\) n’est pas identifiable. Si \(s+v=1\), la mesure n’apporte aucune information sur \(\pi\). Si la variance marginale des annotations tend vers zéro, le dénominateur du coefficient \(\kappa\) tend également vers zéro.

**T4 — Refus et sous-performance**

Pour un refus \(R\),
\[
P(Y=1\mid t)
=\sum_r P(Y=1\mid R=r,t)P(R=r\mid t).
\]
Une variation de \(P(R\mid t)\) suffit à modifier le taux marginal sans variation des taux conditionnels. Si \(P(R=0\mid t)\) tend vers zéro, l’estimation conditionnelle parmi les non-refus perd sa précision.

### (c) Contrôles négatifs dont l’absence serait fatale

- **T1 :** solutions honnêtes fonctionnelles appariées, sans refus ; variations de longueur et de format à étiquette inchangée ; détecteur utilisant seulement la provenance ; calibration et test disjoints par problème et groupe de génération.
- **T2 :** contenu ajouté sémantiquement inerte mais apparié en longueur, emplacement et format ; mêmes artefacts sans ajout ; matrice attaquant–moniteur croisée.
- **T3 :** exemples négatifs annotés indépendamment à chaque étape d’entraînement, avec estimation de l’erreur du classificateur par étape ; réutiliser uniquement son jeu de calibration serait fatal.
- **T4 :** tâches comparables sans incitation supposée à sous-performer ; codage séparé des refus ; mesure indépendante de réussite ordinaire.

## Sur la proposition B

**RAPPORTÉ —** La pièce B est absente, avec le statut transmis « REFUS » ; aucune critique de son contenu n’est possible.

## Sur la proposition C

**RAPPORTÉ —** La pièce C est absente, avec le statut transmis « jamais lancée » ; aucune critique de son contenu n’est possible.

## Sur la proposition D

### (a) Défauts de méthode

**T1 — Horizon de subversion accessible**

La réussite est une intersection : artefact fonctionnel, condition plantée satisfaite, contrôle franchi. Son amélioration peut venir exclusivement de la programmation ordinaire. La formulation « capacité accessible sous protocole fixé » est appropriée, mais elle ne sépare pas ces contributions.

Le temps humain doit correspondre à une tâche précisément définie. Le temps de construction, de résolution honnête et de détection ne sont pas interchangeables. Chronométrer des humains puis sélectionner les tâches dont les temps prédisent bien les modèles créerait une fuite instrument–évaluation.

**T2 — Horizon de surveillance**

La difficulté humaine de produire une attaque n’est pas nécessairement croissante avec la difficulté de la détecter. Le sens de variation attendu de la courbe doit être testé, non imposé par l’ajustement logistique.

Les jumeaux issus du même générateur peuvent encore porter des signatures d’invites, de longueur ou de validation différentes. L’appariement de provenance est nécessaire, mais ne garantit pas l’appariement distributionnel.

Le corpus renouvelé permet une épreuve de transport, à condition de ne pas servir ensuite à modifier le seuil ou choisir les strates. De même, exclure les tâches invalides après examen des scores introduirait une sélection dépendante du résultat.

**T3 — Calcul d’élicitation**

Les FLOP mesurent un coût calculatoire, pas automatiquement un budget d’opportunités comparable. Taille du modèle, longueur de sortie et allocation des tentatives influencent simultanément le coût et la réussite. La dépendance entre tentatives doit être estimée ; elle ne disparaît pas parce que leur calendrier est non adaptatif.

**Critères E1/E2 et qualification**

E1 emploie bien des hypothèses complémentaires. Il reste nécessaire de préspécifier la population d’attaques fraîches visée.

E2 combine plusieurs contraintes. Le falsifier exige une violation établie de l’une d’elles ; falsifier son complément exige d’établir toutes les contraintes, avec une incertitude simultanée. Un simple dépassement ponctuel ne suffit pas.

Exiger la réussite de tous les canaris ne démontre pas une erreur de vérification nulle. Choisir les tâches conservées sur ce même échantillon puis le réutiliser pour qualifier l’instrument produirait une fuite.

### (b) Conditions de perte de puissance ou de non-identification

**T1 — Décomposition de la réussite**

Avec \(F\), fonctionnalité ; \(B\), condition plantée ; \(U\), franchissement :
\[
p_t(x)=P(F\mid x,t)\,
P(B\mid F,x,t)\,
P(U\mid F,B,x,t).
\]
Si seuls les produits sont estimés, leurs facteurs ne sont pas identifiables séparément. Si le premier facteur varie et les suivants restent constants, la pente marginale ne permet pas d’attribuer une tendance à ces derniers. Si \(P(F,B\mid x,t)\) tend vers zéro, l’estimation du dernier facteur perd sa puissance.

**T1/T2 — Axe humain et horizon**

Pour une mesure \(\widetilde x=x+\varepsilon\), dans le cas classique d’erreur indépendante, une régression linéaire locale subit l’atténuation :
\[
\beta_{\mathrm{obs}}
=\beta\frac{\operatorname{Var}(x)}
{\operatorname{Var}(x)+\operatorname{Var}(\varepsilon)}.
\]
Si \(P(\varepsilon\mid t)\) varie, la pente peut également être biaisée. Un horizon est non identifiable lorsque la cible n’est pas croisée ou que la courbe présente plusieurs croisements.

**T2 — Transport de calibration**

Pour une loi honnête de calibration \(Q_0\) et une loi honnête de test \(P_0\),
\[
Q_0(S>\tau)=\alpha
\quad\not\Rightarrow\quad
P_0(S>\tau)=\alpha.
\]
Sous un échantillonnage indépendant, le nombre d’excès suit une loi binomiale de paramètre \(n_0,\alpha\). Quand \(n_0\alpha\) est faible, l’estimation relative de cette queue est imprécise. Avec dépendance par tâche, cette loi binomiale n’est plus appropriée sans ajustement.

**T3 — Censure et médiane**

Soit \(T\) le calcul jusqu’à réussite, \(C\) la censure et \(r\) la probabilité cible. La quantité \(q_r\) n’est pas identifiée non paramétriquement si
\[
P(T\le q_{\max})<r.
\]
Si \(P(T<\infty)<r\), elle n’est pas finie. Si \(T\not\!\perp C\mid X\), un estimateur supposant une censure indépendante peut être biaisé.

Pour \(K\) tentatives conditionnellement indépendantes de probabilité \(p_i\),
\[
P(\text{au moins une réussite}\mid i)=1-(1-p_i)^K.
\]
Cette identité ne s’applique pas sous dépendance arbitraire ; une évolution de cette dépendance peut modifier \(q_r\) à marges identiques.

**E2 et estimateur temporel**

Pour les marges du critère \(g=(d-d_\star,\alpha-a,\Delta-\delta)\), la réussite exige \(g_j\geq0\) pour chaque composante. Si une composante est proche de sa frontière au regard de son erreur-type, une décision simultanée manque de puissance.

Une permutation libre des dates n’est calibrée que sous échangeabilité des unités permutées. Si \(P(S\mid\text{famille})\) varie et que famille et date sont dépendantes, cette condition n’est pas satisfaite. Un corpus uniquement honnête ne permet pas d’estimer un horizon de détection des positifs.

### (c) Contrôles négatifs dont l’absence serait fatale

- **T1 :** tâches honnêtes de fonctionnalité comparable et sans condition plantée ; publication séparée des facteurs de réussite.
- **T2 :** détecteurs limités aux métadonnées et au style ; modifications inertes appariées ; échantillon honnête final indépendant pour tester le transport du seuil.
- **T3 :** condition identique à elle-même, mesurée sur plusieurs campagnes indépendantes, pour estimer la variabilité et la dépendance du calendrier ; aucune sélection du calendrier sur le test final.
- **Vérificateur :** artefacts invalides et jumeaux honnêtes indépendants des canaris de développement.
- **Pente :** simulations nulles conservant dépendances, censure et sélection réellement prévues ; permutations restreintes aux blocs échangeables. Une simulation sous le seul modèle d’ajustement testerait surtout sa cohérence interne.

**HYPOTHÈSE — Règle décisionnelle commune proposée :** définir chaque duel sur un paramètre, \(H_A:\theta\geq\delta\) contre \(H_B:\theta<\delta\). Une région d’incertitude entièrement d’un côté permet de rejeter l’autre hypothèse au risque préspécifié ; son chevauchement impose « non concluant », jamais « absence d’effet ».

FIN-DE-CELLULE