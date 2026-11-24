## 1. Ce qu’un expert du domaine ferait ici, et que la question ne demande pas

Il fixerait **l’unité sur laquelle porte chaque conclusion**. Classer un épisode issu d’un adaptateur connu, détecter un dommage sur un nouvel article et généraliser à un adaptateur fabriqué indépendamment sont trois prétentions différentes. Multiplier les épisodes d’un même adaptateur précise la première mesure ; cela ne fournit pas de répétitions indépendantes de sa fabrication.

**VÉRIFIÉ** — Le jumeau honnête n’existe qu’au banc ; la garantie du programme repose sur une fraction auditée au hasard ; l’oracle ne doit sélectionner ni agent ni moniteur. **OBSERVÉ-NON-AUDITÉ** — La tenue des saboteurs à l’entraînement n’a pas été mesurée. **HYPOTHÈSE** — Ils se représentent leur sabotage. Un succès de classification n’établirait pas cette hypothèse ; un échec ne la réfuterait pas davantage.

Dans la suite, les plans, objections expérimentales et scénarios de C ont statut **HYPOTHÈSE**, non résultat. Les égalités de lois sont des **conditions à tester**, pas des propriétés attribuées aux données. Je sépare défaut de puissance (paramètre défini, estimation imprécise) et non-identification (mêmes observations possibles pour des réponses différentes).

## 2. Les données brutes de départ

Demander, avant les courbes : identifiants d’article, de question, de fabrication des poids, de graine et de course ; assignations de condition et de dose ; trajectoires entières, sorties et scores non seuillés par pas ; produits des jumeaux ; jugements individuels, ordre de présentation et identité pseudonymisée du juge ; indicateurs de tirage pour audit **avec leur probabilité conditionnelle** ; historique des versions, accès au jeu inédit et décisions déjà prises. Un coefficient de corrélation n’est pas une donnée brute.

**VÉRIFIÉ** — Les quatre doses existent pour l’adaptateur ; la courbe manque pour la consigne. Je ne sais pas combien de fabrications indépendantes, de flux honnêtes frais ni de jugements répétés sont disponibles. Il faut distinguer les données manquantes des résultats négatifs.

## 3. Ce que chaque voie peut établir — critique croisée

**Détecter** peut établir un excès d’alertes sur un flux défini, à risque d’alerte honnête contrôlé ; pas sa cause. **Auditer** peut estimer un taux de produits jugés dommageables si le tirage est connu ; le passage au dommage scientifique demande une validation indépendante du jugement. **Entraîner** peut établir un effet comparatif sur les produits, à capacité honnête mesurée ; ni une baisse du soupçon ni une hausse de la récompense ne suffit. Le lien utile entre voies est testable : à dommage donné, la sonde guide-t-elle mieux les audits ? Le lien nuisible l’est aussi : après mise à jour, une sonde reste-t-elle informative **lorsque le dommage persiste** ?

Notation : \(Z\) désigne la condition fabriquée, \(Y\) le dommage de référence au banc, \(O\) le verdict sur produit seul, \(S\) le score interne, \(T\) le texte disponible au même instant, \(X\) les strates fixées avant traitement. \(\tau\) est le premier franchissement, \(h\) l’horizon. Les probabilités de franchissement portent sur des **flux entiers**, pas sur des pas empilés.

### Sur la proposition A

**(a) Défauts de méthode.** A a raison de demander un dommage après le bras déclaré, mais « bras d’attaque = parade » ne découle pas de l’interdiction d’utiliser l’oracle : des objectifs auxiliaires, des données ou des règles d’arrêt différents définissent des interventions différentes. Son rapport signal/dérive moyenne ne juge pas la queue de franchissement. Battre un lecteur tiers du texte ne démontre pas une représentation du sabotage. Enfin, choisir l’organisme de l’expérience suivante d’après sa rétention mesurée par l’oracle serait une sélection par l’oracle ; décider si une *question* reste mesurable n’autorise pas à choisir le meilleur survivant.

**(b) Conditions sur les lois et estimateurs.**

- C1 : \(R=\Delta_S/\max_x|\mu_{0x}-\mu_0|\) est indéfini si le dénominateur est nul. Même à moyennes identiques, \(P_{0x}(\tau\le h)>\alpha\) invalide le seuil dans la strate \(x\). Pour le dommage, c’est \(|E\widehat\Delta_Y|/\mathrm{SE}(\widehat\Delta_Y)\), non l’écart divisé par la dispersion d’un seul jugement, qui gouverne la précision.
- C2 : si \(P(Z\mid S,T,X)=P(Z\mid T,X)\), le gain optimal conditionnel est nul, même si l’AUROC interne dépasse celle du lecteur textuel ajusté. Un intervalle d’écart contenant zéro n’est pas un intervalle d’équivalence.
- C3/C5 : si l’intervalle du dommage initial contient zéro, le rapport post/pré peut avoir un intervalle non borné. Si les lois jointes de \((S,T,O)\) coïncident sous deux mécanismes post-entraînement, leur distinction par ces mesures n’est pas identifiable.
- C4 : pour une inclusion de probabilité \(p\), \(E[O^2/p]\) gouverne le second moment du terme pondéré. Même si \(p\) est indépendant de \(O\) après permutation, \(E[1/p]\ge 1/E[p]\) : **le rapport des coûts attendu n’est pas nécessairement l’unité**. Si \(p=0\) sur une strate de masse positive, son taux de dommage n’est pas identifiable par rejeu.

**(c) Contrôles négatifs indispensables.** Flux honnêtes avec même moyenne mais dépendances temporelles différentes ; permutations par blocs conservant article et procédure ; aiguillage placebo avec les **mêmes probabilités inégales** ; mise à jour placebo à déplacement de politique comparable, en plus du jumeau entraîné. Sans ce dernier contraste, C5 mesure un changement, pas l’effet propre du signal de sonde.

### Sur la proposition B

**(a) Défauts de méthode.** Égalité des performances avant et après génération n’implique pas identité de l’information lue. Une erreur scientifique réelle d’un honnête n’est pas une fausse alerte de dommage ; elle peut être une fausse accusation de sabotage. En C5, trouver le premier cas et resserrer une borne de prévalence sont des objectifs distincts. À budget total fixe, réserver moins d’audits uniformes peut conserver la couverture nominale tout en élargissant la borne. Enfin, réapprendre la sonde *sur* la famille inédite ne la teste pas sur cette famille.

**(b) Conditions sur les lois et estimateurs.**

- C1 : \(\mathrm{AUC}(S_{\rm pré})=\mathrm{AUC}(S_{\rm post})\) est compatible avec \(P(S_{\rm pré}\ne S_{\rm post})>0\) et des erreurs disjointes. Si \(P(Y>0\mid Z=\mathrm{honnête})>0\), \(P(O>0\mid Z=\mathrm{honnête})\) n’est pas le taux de faux positifs pour \(Y\).
- C2/C4 : si \(P_{\rm post}(Y>0)=0\), le rappel post-entraînement conditionnel au dommage est indéfini ; la perte de séparation par \(Z\) ne mesure plus une perte de sensibilité au dommage. Si seule \(P(S\mid Y=0)\) se décale, le taux d’alerte au seuil gelé peut changer à AUROC constante.
- C3 : si \(P(\tau\le h)<1/2\), la médiane n’est pas estimable dans la fenêtre. La quantité \(E[\min(\tau,h)]\) reste définie. Une dose minimale entre doses observées n’est pas identifiée sans loi d’interpolation.
- C5 : sous tirages indépendants de rendement \(q=P(O>0\mid\mathrm{audité})\), \(P(\tau>k)=(1-q)^k\). Deux plans de même \(q\) ont ici le même délai, même avec des variances différentes de l’estimateur de prévalence.

**(c) Contrôles négatifs indispensables.** Consignes bénignes appariées avec mesure pré-génération ; produits honnêtes effectivement médiocres jugés à l’aveugle ; flux sans mise à jour pour tester la dérive ; rejeu à coût et censure identiques avec aiguillage indépendant du dommage.

### Sur la proposition D

**(a) Défauts de méthode.** D appelle \( \mathrm{TPR}/\alpha \) « accélération d’audit » : c’est un rapport de taux de sélection, pas un nombre d’audits économisés. Retenir les doses où l’oracle apparaît monotone fait dépendre le résultat du filtre d’évaluation. La courbe consigne « complétée » n’est pas un fait acquis. Comparer le modèle du programme aux saboteurs publics change simultanément modèle, fabrication et tâche. En C5, apparier sur la note faible **après** entraînement risque de retenir des sous-populations différentes. Une sonde hors gradient n’est pas pour autant un juge indépendant du dommage.

**(b) Conditions sur les lois et estimateurs.**

- C1 : \(\rho_{\rm rang}(d,E[O\mid d])\) peut être maximal alors que \(O\perp Y\mid d\) ; inversement \(\mathrm{Var}(E[Y\mid d])=0\) rend la corrélation de doses non informative même pour \(O=Y\).
- C2/C4 : avec prévalence \(\pi\), rappel \(r\) et faux positifs \(f\) pour le dommage, le rendement parmi les alertes vaut \(\pi r/[\pi r+(1-\pi)f]\), non \(r/f\). Si \(P(Y\mid Z,X)\) change entre conditions de comparaison, le rappel par \(Z\) ne standardise pas la gravité.
- C3 : si \(P(\text{tâche}=x\mid\text{modèle})\) a des supports disjoints, l’effet propre de la taille n’est pas identifié. Une rétention faible sous un traitement et forte sous un autre satisfait des morceaux des deux hypothèses de D.
- C5 : si les supports des notes post-traitement ne se recouvrent pas, le contraste à note égale est indéfini ; si \(P(S\mid Y=0)\) est invariant mais \(P(S\mid Y>0)\) change, aucune estimation sur honnêtes seuls n’identifie le rappel.

**(c) Contrôles négatifs indispensables.** Éditions stylistiques sans changement de fond, ordre des paires inversé ; bras sans optimisation pour chaque famille et chaque juge ; calibration et vérification sur honnêtes distincts. Comparer des budgets de surveillance égaux, pas seulement des seuils égaux.

### Sur la proposition E

**(a) Défauts de méthode.** L’autocorrélation forte est postulée, pas mesurée ; l’indépendance des pas n’est pas nécessaire à toute garantie séquentielle. L’appariement sur la divergence KL après fabrication peut éliminer une partie du phénomène étudié. En P2, entraîner le seul honnête ne donne aucun rappel post-traitement. Qualifier F3 par l’oracle, puis ne publier le duel que si elle « passe », conditionne la lecture unique. En P5, une note faible fournie par un juge reste un score de moniteur, même hors ligne : **VÉRIFIÉ** — son usage pour entraîner l’agent hors bras déclaré est interdit.

**(b) Conditions sur les lois et estimateurs.**

- P1/P3 : si \(E_0[M_t\mid\mathcal F_{t-1}]\le M_{t-1}\) pour un processus positif initialisé à l’unité, l’autocorrélation seule n’invalide pas la borne de franchissement de \(1/\alpha\). Si les supports de KL bénin et saboteur sont disjoints, le contraste apparié n’est pas identifié.
- P2 : \(P_{\rm post}(S\mid Z=\mathrm{honnête})\) ne détermine pas \(P_{\rm post}(S\mid Y>0)\). P3 : \(E[\widehat\Delta\mid\widehat R_{\rm placebo}>c]\ne E[\widehat\Delta]\) en général.
- P4 : une forte corrélation marginale oracle–humain est compatible avec \(\mathrm{Cov}(O,Y\mid X)=0\) dans chaque article. Le coût pour une puissance \(1-\beta\) est \(\inf\{k:P_1(\tau\le k)\ge1-\beta\}\), pas le délai médian.
- P5 : \(E[Y_{\rm post}]>0\) avec \(P(\tau\le h\mid Y>0)=P_0(\tau\le h)\) est compatible avec l’échec simultané des deux hypothèses proposées.

**(c) Contrôles négatifs indispensables.** Flux honnêtes intacts réservés après fixation du seuil ; fabrications bénignes indépendantes non choisies pour leur score ; placebo sur F3 publié quelle qu’en soit l’issue ; paires à fond identique et style modifié pour les juges humains comme automatiques.

## 4. Les programmes possibles

| Architecture | Thèse, expérience et réfutation | Exigences ; coût ; antériorité |
|---|---|---|
| Continuité | La sonde gagne sur le texte : duel gelé, réfuté si son avantage utile est exclu. | Famille réservée ; dommage documenté, sans exigence de robustesse à l’entraînement ; calcul modéré. |
| Audit aiguillé | La sonde réduit le coût d’une décision définie : rejeu à couverture et puissance égales ; réfuté sans économie utile. | Tirages connus, oracle validé ; faible coût marginal si les verdicts existent. **VÉRIFIÉ** : l’audit aléatoire lui-même n’est pas une contribution du programme. |
| Changement d’objet : valider l’oracle | Le produit seul conserve le contraste scientifique apparié : notation externe par article ; réfuté si un biais de style explique le contraste. | Produits appariés, pas de saboteur tenace requis ; coût surtout humain. |
| Caractérisation de l’entraînement | La baisse de dommage dépasse celle d’un placebo : comparaison randomisée, réfutée si l’effet spécifique utile est exclu. | Dommage initial mesurable, capacité honnête contrôlée ; coût de plusieurs mises à jour. Pas de parade ouverte. |

**OBSERVÉ-NON-AUDITÉ** — Recherche d’antériorité incomplète. Je ne sais pas laquelle de ces expériences précises a déjà été faite ; référence à vérifier.

## 5. Vérification extérieure

Confier à un tiers les identifiants de fabrication, le lot scellé et l’exécution unique, y compris si le résultat est indécis. Faire reproduire séparément la cotation du dommage et la probabilité de franchissement sur des flux honnêtes neufs. Une réplication sur un autre modèle teste le **protocole**, non le transport automatique des coefficients de la sonde.

## 6. Reformulation exigeante

À risque honnête et horizon fixés, quelle économie de décision la lecture interne apporte-t-elle **sur des produits indépendamment jugés**, au-delà d’un lecteur du texte disponible au même instant ? Si les poids changent, séparer la variation du dommage de celle de la sensibilité à dommage comparable.

## 7. Programme des priorités classé

Notes, scores et coûts relatifs **illustratifs** ; tuple = gain, facilité, portée, découverte, coût ; score = produit des quatre premiers divisé par le dernier. Pour chaque ligne, \(H_A:\theta>m\) contre \(H_B:\theta\le m\), marge d’utilité préenregistrée dans l’unité indiquée. Un intervalle entièrement au-dessus réfute \(H_B\), entièrement au-dessous réfute \(H_A\) ; sinon **indécis**, sans relecture.

| Chantier décisif | \(\theta\) et seuil \(m\) | Contrôle négatif ; coût estimé | Tuple → score |
|---|---|---|---|
| Calibration séquentielle | Marge entre risque nominal et pire probabilité honnête de franchissement ; seuil nul | Flux bénins frais par fabrication ; inférence | (5,5,4,2,2) → 100 |
| Validité du verdict | Avantage prédictif du verdict sur le style seul pour le jugement externe *intra-article* ; marge minimale de précision utile | Éditions stylistiques aveugles ; annotation | (5,4,4,3,3) → 80 |
| Duel interne–texte | Gain de rappel à horizon et risque identiques ; marge de rappel justifiant le surcoût | Famille bénigne de même procédé ; inférence scellée | (5,3,5,3,3) → 75 |
| Économie d’audit | Audits économisés à puissance et couverture fixées ; seuil de rentabilité incluant le calcul | Aiguillage placebo de même budget ; rejeu CPU si verdicts complets | (3,4,3,2,1) → 72 |
| Caractérisation sous mise à jour | Dommage résiduel apparié après placebo fixé ; marge de dommage scientifiquement discernable | Honnête mis à jour et branche sans mise à jour ; calcul et jugement | (4,3,4,3,3) → 48 |

Au coût au carré, le rejeu passe en tête **sans devenir exécutable avant validation du verdict**. Avant la porte d’instruments : calibration, verdict et courbe consigne manquante. Ensuite : duel unique, puis rejeu. Caractérisation seulement sous périmètre autorisé, sans choisir de poids d’après l’oracle ; mesurer aussi le dommage dans le bras déclaré ultérieur. Différer les essaims ; ne pas ouvrir maintenant l’entraînement correctif sur note faible.

**Hors de portée :** inférer l’intention depuis une alerte, certifier l’absence de dommage en service sans référence, ou conclure d’un placebo sur un organisme à l’efficacité générale d’une parade.

FIN-DE-CELLULE