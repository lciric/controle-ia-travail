# Proposition E — Critique croisée de méthode

**Statuts.** Les contenus attribués aux pièces sont **RAPPORTÉS**, sans validation de leurs affirmations. Mes objections et conditions de défaillance sont des **HYPOTHÈSES** à examiner ; les identités explicitement démontrées sont **VÉRIFIÉES comme calculs conditionnels**, non comme résultats du programme. Aucun résultat expérimental n’est disponible ici. Les seuils nouveaux restent symboliques, à geler avant évaluation.

## Sur la proposition A

Pièce A absente — statut transmis : REFUS ; aucune critique de son contenu n’est possible.

## Sur la proposition B

### (a) Défauts de méthode

**B-F1 — La fraction « active » et son contrôle ne mesurent pas l’activité pertinente.**  
**RAPPORTÉ :** B compte comme actives toutes les actions appartenant à une classe non singleton.

**HYPOTHÈSE critique :** une classe peut contenir plusieurs actions mais des coûts identiques ; certaines permutations peuvent aussi conserver des valeurs en place. Cette fraction surestime alors le traitement effectif. Son seuil ne détermine pas, à lui seul, la puissance de P3.

**VÉRIFIÉ — identité combinatoire :** permuter entre actions les vecteurs complets d’indicateurs conserve exactement leurs effectifs, donc les tailles de classe et cette fraction. Le contrôle proposé ne produit pas les quasi-singletons annoncés. Permuter séparément les indicateurs définirait un autre contrôle, dont la loi doit être spécifiée.

**Biais :** faux sentiment de capacité, puis faux négatif sur P3.  
**Garde / révision de gravité :** compter les changements de **valeur** et leur amplitude logarithmique ; la gravité diminue si ces quantités, pondérées selon l’estimand de P3, restent suffisantes sur des tâches réservées.

---

**B-F2 — Étendue médiane des classes : mauvais substitut au contraste P3.**  
**HYPOTHÈSE critique :** la médiane des étendues donne le même poids à une petite classe et à une grande. Elle ne caractérise ni le déplacement moyen des actions, ni l’erreur relativement à la référence cachée. Raffiner les classes réduit leurs étendues individuellement, mais ne garantit pas une diminution de la médiane non pondérée après modification du nombre de classes.

**Biais :** faux positif de faisabilité ou arrêt injustifié.  
**Garde :** conserver l’étendue comme diagnostic descriptif ; juger la faisabilité avec le contraste maître–témoin et les pondérations gelées de P3. **Changement d’avis :** démonstration d’une borne reliant réellement le diagnostic au contraste retenu.

---

**B-F3/F4 — Fidélité numérique, identité et détection sont confondues.**  
**RAPPORTÉ :** B propose une médiane d’erreur élève–maître, puis invoque sa petitesse pour relativiser les fuites.

**HYPOTHÈSE critique :** une petite médiane laisse libres les queues, les formats, les mots et les dépendances entre champs. Elle ne garantit pas P4. B mélange également taux de détection à un seuil et AUC : ces paramètres ne sont pas interchangeables.

Exiger M-3 « comme identité » sur des générations indépendantes de l’élève n’est pas justifié par la construction rapportée. Chez l’élève, il faut un critère probabiliste d’équivalence, pas une égalité de fichiers.

Enfin, égalité des marginales n’implique pas égalité de la loi jointe. La conclusion d’aveuglement exige la définition exacte de l’entrée et de la fonction de score de chaque base.

**Biais :** faux positif de discrétion ; éventuellement faux négatif si l’on exige une identité empirique impossible à obtenir par échantillonnage.  
**Garde / révision :** auditer les caractéristiques effectivement accessibles au score, puis borner séparément la fuite et l’erreur de transfert, hors entraînement.

---

**B-F5/F7 — Les critères changent la question et les duels ne correspondent pas aux issues.**  
**HYPOTHÈSE critique :** imposer un incrément minimal à chaque intervalle renforce P3 sans justification fournie. Un couplage « aléatoire à même Kendall » nécessite une loi de tirage explicite : la procédure rapportée utilise déjà des inversions tirées par graine. Sans contraste de lois, le contrôle n’isole aucune direction supplémentaire.

L’inversion complète n’attribue pas à chaque action sa valeur individuellement la plus éloignée. Une forte M2 ne distingue pas non plus copie, erreur accidentelle et stratégie spontanée.

Les issues de F1, F3 et F7 ajoutent des conditions absentes des hypothèses correspondantes. Elles ne constituent donc pas des falsifications logiquement symétriques.

**Biais :** rejet artificiel de P3 ou faux positif de portée.  
**Garde / révision :** séparer hausse terminale, monotonie et mécanisme ; définir pour chacun un paramètre et son complément exact.

---

**B-F6 et instruments — Non-rejet pris pour preuve ; contrôles mal ciblés.**  
**HYPOTHÈSE critique :** une valeur de test non significative ne falsifie pas une différence. Comparer le témoin distillé au modèle nu confond réécriture et entraînement ; le contrôle octet par octet, lui, cible correctement la réécriture.

« Battre un prédicteur de M2 nulle » en RMSE n’est pas une validation de M2. De même, exiger que la base batte les seuls indicateurs de forme n’est informatif que sous une alternative où le coût apporte effectivement de l’information.

**RAPPORTÉ :** plusieurs seuils et puissances de B ne portent pas la mention « illustratif », malgré leur absence des faits. Ses propositions d’adaptation du rang ou de la grille nécessiteraient une version neuve et un scellement propre.

### (b) Conditions de perte de puissance ou de non-jugement — lois, paramètres, estimateurs

**HYPOTHÈSES conditionnelles.** Notons \(T\) la tâche, \(K\) la classe, \(X\) le log-coût honnête, \(Y_p\) le log-coût déclaré, \(R\) la référence logarithmique cachée, \(S_p\) le score de base. Posons \(D_p=|Y_p-R|-|Y_0-R|\).

| Mesure ou critère de B | Conditions probabilistes |
|---|---|
| Fraction active | \(P(n_K\geq 2)>0\) mais \(P(Y_p\neq X)=0\). Plus généralement, \(P(Y_p\neq X)\) ne détermine pas \(E[D_p]\). |
| Étendue intra-classe | La loi des étendues sous échantillonnage uniforme des classes diffère de celle induite par \(P(K)\). Sa médiane peut rester fixe alors que \(E[D_p]\) varie. |
| P3 et tests d’incréments | \(\operatorname{Var}(\widehat E[D_p])\) est grande relativement au carré du contraste visé. Si les erreurs sont corrélées conditionnellement à \(T\), le nombre d’actions n’est pas le nombre d’unités indépendantes. |
| Fidélité médiane | \(\operatorname{Med}|Y_p-Y_p^{M}|\leq\varepsilon\) n’impose aucune borne utile sur les probabilités de queue ni sur \(\mathrm{TV}(P(S_p),P(S_0))\). |
| AUC et P4 | \(\operatorname{AUC}=P(S_p>S_0)+\tfrac12P(S_p=S_0)\). Si \(P(S_p)=P(S_0)\), l’AUC population vaut \(\tfrac12\). Une AUC proche de cette valeur n’identifie pas l’égalité des lois. |
| Non-différence du témoin | Pour \(\theta=E[M2_0-M2_{\rm nu}]\), un intervalle couvrant simultanément la zone d’équivalence et son complément ne permet aucun verdict d’équivalence. |
| Seuil de M2 « massive » | Deux lois mécanistiques distinctes peuvent induire la même loi de \(|Y_p-R|\) : le mécanisme n’est alors pas identifiable par M2. |
| M-3 | Si \(Z\) désigne toutes les entrées du score, \(P_p(Z_j)=P_0(Z_j)\) pour chaque composante n’implique pas \(P_p(Z)=P_0(Z)\). |
| Généralisation | Si les mêmes tâches conditionnent sélection du seuil et évaluation, la loi de \(\widehat\theta\) conditionnelle à la sélection diffère de sa loi préenregistrée non conditionnelle. |

**VÉRIFIÉ — justification de l’AUC :** sous deux lois de score identiques et des tirages indépendants, les probabilités de supériorité et d’infériorité sont égales ; la demi-pondération des égalités donne la valeur indiquée.

### (c) Contrôles négatifs dont l’absence serait fatale

**HYPOTHÈSES de nécessité, relatives aux conclusions visées :**

- **Pour attribuer un effet au réappariement :** chaîne identité complète, mêmes données, ordre, budget d’apprentissage et décodage ; contrôle octet par octet avant entraînement. Le modèle nu reste un repère séparé.
- **Pour juger l’activité :** classes à coûts constants et classes sans permutation possible. Le déplacement doit y être nul.
- **Pour calibrer la base :** deux groupes honnêtes indépendants, avec séparation par tâches ; étiquettes permutées dans les strates échangeables pour auditer la procédure statistique.
- **Pour revendiquer l’inversion plutôt qu’une détérioration générique :** contrôle actif décorrélant action et coût tout en conservant les contraintes pertinentes, selon une loi gelée. Son absence est fatale à cette attribution, pas à la seule mesure de P3.
- **Pour exclure une fuite instrument–évaluation :** référence cachée et tâches finales absentes de toute sélection de seuil, classe, rang ou graine.

## Sur la proposition C

### (a) Défauts de méthode

**C-E1 — Une erreur absolue n’est ni le contraste P3 ni une borne de l’élève.**  
**RAPPORTÉ :** C qualifie M2 du maître à dose maximale de « borne supérieure théorique ».

**HYPOTHÈSE critique :** cette affirmation n’est pas établie. La référence cachée n’est pas nécessairement le coût initial utilisé pour trier ; l’élève peut produire des valeurs hors du multiensemble. Même une borne sur le déplacement du maître ne serait donc pas une borne générale sur M2 de l’élève.

Le témoin identité a un déplacement nul relativement au coût initial, mais pas nécessairement une M2 nulle relativement à la référence cachée.

**Biais :** faux positif de capacité si le plancher honnête est élevé ; faux négatif par arrêt prématuré.  
**Garde / révision :** utiliser le contraste apparié maître–témoin ; n’accepter une borne qu’avec son domaine et sa démonstration.

---

**C-E2 — Le ratio proposé ne teste ni linéarité ni monotonie.**  
**HYPOTHÈSE critique :** le ratio des M2 brutes contient le plancher honnête. Une valeur élevée peut donc accompagner un effet nul. Une distance de Kendall moyenne sous permutation uniforme ne fixe pas un ratio de dommages : celui-ci dépend de la loi des valeurs et de la référence.

Des transpositions adjacentes successives ne restent pas limitées aux voisins du classement initial. La courbe « plate puis explosive » est une possibilité, pas une conséquence générale.

**Biais :** validation artificielle de progressivité ou rejet d’une réponse légitime.  
**Garde / révision :** vérifier séparément la dose réalisée et les contrastes appariés ; examiner leur loi sur les graines sans choisir la plus favorable.

---

**C-E3 — Entropie croisée et corrélation de rang : interprétations trop fortes.**  
**HYPOTHÈSE critique :** l’entropie croisée vise une distribution conditionnelle, pas nécessairement une médiane ou une constante. L’effondrement dépend aussi du décodage et de la spécification du modèle.

Une corrélation négative contre la référence cachée n’est ni nécessaire ni suffisante pour démontrer le transfert exact de l’inversion construite contre les coûts initiaux. Bruit de référence, ex æquo et mélange des classes peuvent changer le signe ou rendre l’estimateur indéfini. Le duel omet les transferts partiels et les mélanges de mécanismes.

**Biais :** faux négatif de transfert ou faux positif de mécanisme.  
**Garde / révision :** mesurer séparément concordance avec les cibles du maître, dépendance à l’action et dommage contre la référence ; évaluer sans filtrer préalablement sur une M2 favorable.

---

**C-E4 — Dépendance autorégressive possible ne signifie pas invariance impossible.**  
**HYPOTHÈSE critique :** placer `COST` avant d’autres champs ouvre une voie causale, sans prouver son utilisation. Inversement, le placer en dernier n’empêche pas l’adaptateur de modifier les champs antérieurs.

L’AUC empirique exactement au hasard n’est garantie que si les multisets de scores évalués sont exactement identiques avec le traitement approprié des égalités. Une identité de marginales générales ne suffit pas.

**Biais :** exclusion injustifiée d’une architecture ou fausse validation de P4.  
**Garde / révision :** définir les lois conditionnelles visées et auditer l’entrée complète du score ; ne pas substituer la position syntaxique à la mesure.

---

**C-E5 et validation de M2 — Témoins modifiés et calibration incorrecte.**  
**HYPOTHÈSE critique :** les affirmations de gradient quasi nul et de concentration du témoin ne sont pas des conséquences nécessaires de la distillation. Des normes de paramètres similaires ne garantissent pas des perturbations fonctionnelles similaires.

Exiger après coup que P3 dépasse aussi le modèle nu, ou réancrer le contraste sur un maximum, change l’estimand. Cela doit devenir une analyse distincte, gelée.

**VÉRIFIÉ — calcul conditionnel :** pour \(E=X-R\) et un décalage positif \(a\),
\[
|E+a|-|E|\in[-a,a].
\]
Multiplier un coût honnête par \(10^a\) n’augmente donc pas nécessairement M2 de \(a\). Le contrôle positif proposé par C peut faire échouer un instrument correct.

**RAPPORTÉ :** C programme des lectures de M2 et des expériences sur l’élève avant scellement final. **HYPOTHÈSE critique :** ce calendrier ne respecte pas R1 tel que fourni ; l’étiquette « conception » n’accorde pas d’exemption. Le statut ouvert du modèle et les projections précises ne sont pas non plus établis par les faits.

### (b) Conditions de perte de puissance ou de non-jugement — lois, paramètres, estimateurs

**HYPOTHÈSES conditionnelles**, avec les notations précédentes :

| Mesure ou critère de C | Conditions probabilistes |
|---|---|
| Capacité du maître | \(E|Y_1^M-R|\) élevé avec \(E[D_1^M]\) faible ; si \(R\neq X\) avec probabilité positive, l’erreur brute n’identifie pas le déplacement causal. |
| Ratio intermédiaire | Si \(E|Y_1^M-R|\) est nul, le ratio est indéfini ; s’il est proche de zéro, sa variance peut devenir grande. Un plancher commun dominant rend le ratio peu sensible aux contrastes. |
| Kendall réalisé | \(P(p_{\rm réalisé}=p_{\rm nominal})<1\), ou dénominateur nul après exclusion des ex æquo. La loi \(P(p_{\rm réalisé}\mid p_{\rm nominal},K)\) est alors nécessaire. |
| Corrélations intra-classe | Variance de rang nulle : corrélation indéfinie. Faible probabilité de paires comparables : variance élevée. Une faible dépendance entre \(R\) et \(X\) atténue la concordance avec les cibles construites depuis \(X\). |
| Filtrage sur M2 | La loi \(P(\widehat\tau\mid\widehat{M2}\geq\delta)\) peut différer de \(P(\widehat\tau)\) ; les intervalles non conditionnels ne conservent pas automatiquement leur couverture. |
| AUC élève | Un intervalle d’AUC intersectant à la fois la zone d’équivalence et son complément rend le verdict non jugeable. |
| Concentration du témoin | Le paramètre \(\Delta_0=E[M2_{\rm nu}-M2_0]\) peut être négatif hors tolérance : cette région n’est couverte par aucune issue annoncée dans E5. |
| Injection multiplicative | \(P(E<-a)\) élevé entraîne \(E[|E+a|-|E|]<0\) ; une calibration exigeant une hausse proche de \(a\) est invalide sous cette loi. |
| Lisibilité | Si \(L\) indique une sortie exploitable, \(P(L\mid p,M2)\) dépend de M2 : \(E[M2\mid L,p]\) n’identifie pas \(E[M2\mid p]\). |
| Référence basse/haute | Un écart entre statistiques d’ordre dépend de la densité locale et des masses atomiques ; il ne détermine pas seul la précision du contraste apparié. |

### (c) Contrôles négatifs dont l’absence serait fatale

- **Référence :** coût initial, estimation cachée et réplication honnête indépendante évalués séparément ; absence fatale à l’interprétation du « zéro » et du plancher.
- **Rangs :** coûts constants et coûts indépendants de l’action conditionnellement à la classe ; absence fatale à l’interprétation mécanistique d’une corrélation.
- **Témoin :** réplications indépendantes du témoin identité, mêmes budgets et règles d’arrêt ; absence fatale à l’attribution des écarts à la dose plutôt qu’à la graine d’entraînement.
- **Lisibilité :** audit des sorties exclues, avec règle gelée ; absence fatale si l’exclusion dépend du traitement et du dommage.
- **Séparation :** tâches et références d’évaluation non utilisées pour sélectionner classes, seuils ou versions.

### Règle d’inférence forte pour les vérifications proposées

**HYPOTHÈSE méthodologique :** chaque vérification doit porter sur un paramètre explicite \(\theta\), avec deux hypothèses complémentaires :
\[
H_A:\theta\leq c,\qquad H_B:\theta>c.
\]
Pour une équivalence, prendre comme \(\theta\) une distance entre lois ; pour une hausse, le contraste gelé. Un intervalle entièrement d’un côté du seuil réfute l’autre hypothèse au risque préenregistré. Un intervalle traversant le seuil donne **non jugeable**, jamais « absence d’effet ». Une identité finie, elle, se décide exactement par audit.

## Sur la proposition D

Pièce D absente — statut transmis : ECHEC ; aucune critique de son contenu n’est possible.

FIN-DE-CELLULE