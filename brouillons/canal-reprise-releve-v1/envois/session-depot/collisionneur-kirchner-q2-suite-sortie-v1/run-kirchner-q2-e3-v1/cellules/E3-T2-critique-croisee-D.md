Les points suivants sont des critiques de méthode ; les mécanismes empiriques envisagés restent des **HYPOTHÈSES**. Les résultats repris des pièces conservent leur statut **RAPPORTÉ** ou **OBSERVÉ-NON-AUDITÉ**.

## Sur la proposition A

### (a) Défauts de méthode

- **E1 ne sépare pas sélection et changement de composition.** Le rang dépend du score, mais celui-ci dépend aussi de la classe de plant, de son intensité et de la méthode honnête sur laquelle il est greffé. Une baisse de rappel au sommet peut donc venir d’une surreprésentation de classes difficiles, sans dégradation *au sein d’une classe*. L’enrichissement \(E\) mélange en outre prévalence des plants, probabilité d’atteindre le top-\(k\) et faux négatifs ; il ne remplace pas les deux estimands distincts
  \[
  P(\text{non détecté}\mid V=1,S_k=1,c),\qquad
  P(S_k=1\mid V=1,\text{non détecté},c).
  \]
- **Le rappel sur plants n’est pas nécessairement un plafond du rappel spontané.** Cela suppose une relation d’ordre stochastic­que entre difficulté des plants et difficulté naturelle, non démontrée. Des plants trop visibles donnent un rappel optimiste ; des plants artificiellement atypiques peuvent donner l’inverse.
- **Le contrôle « classe R sans gain » ne discrimine pas bruit et sélection.** Sous l’hypothèse testée, l’absence de gain empêche précisément l’enrichissement par le score. Un résultat nul y est donc attendu même si le classement sélectionne fortement les faux négatifs ailleurs.
- **E2 conserve une malédiction du gagnant.** La population hors banc est fraîche, mais \(S\) semble servir à la fois à choisir les configurations et à établir leur avantage. Sans remesure de \(S\) sur épisodes frais, le contraste top-dix contre configurations aléatoires mélange transfert et surévaluation du classement initial.
- **E3 emploie une mauvaise probabilité de resoumission.** Un taux de basculement \(f\) n’est pas la probabilité \(p_i\) qu’une méthode réellement dégradée passe une évaluation. Même avec essais indépendants conditionnellement à la méthode, la probabilité recherchée est
  \[
  1-\mathbb E_i[(1-p_i)^n],
  \]
  et non \(1-(1-f)^n\). Avec évaluateur déterministe ou erreurs de retest corrélées, cette expression ne vaut plus non plus.
- **E4 ne démontre pas à lui seul des angles morts corrélés.** Juge et moniteur peuvent partager des variables observables — longueur, provenance, similarité à l’archive — sans partager de représentation ou de famille. Le mécanisme proposé dépasse l’estimand mesuré.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- Pour E1, soit \(n_{c,k}\) le nombre de plants exécutés de classe \(c\) effectivement sélectionnés dans le top-\(k\). Si \(n_{c,k}\approx0\), le rappel stratifié et \(E\) sont non estimables. Si les plants sont corrélés par gabarit, agent ou méthode hôte, la taille effective n’est pas le nombre de plants : avec corrélation intraclasse \(\rho\) et grappes de taille \(m\), elle est approximativement divisée par \(1+(m-1)\rho\).
- \(E\) devient instable lorsque la proportion globale de faux négatifs approche zéro ; son dénominateur est alors estimé avec très peu d’événements. Le rappel perd aussi toute puissance discriminante aux plafonds \(R\approx0\) ou \(R\approx1\).
- Sans support commun des scores et des difficultés entre détectés et non détectés, la standardisation par classe ne suffit pas : distinguer composition et effet propre du rang exige alors un modèle non identifiable à partir des seuls verdicts.
- Pour E2, si la variance interconfigurations du vrai score de surveillabilité est nulle, ou si sa fiabilité \(\lambda=\sigma^2_{\text{vrai}}/(\sigma^2_{\text{vrai}}+\sigma^2_{\text{mesure}})\) est faible, \(\rho\) mesure surtout du bruit et est attenué. Le contraste top/aléatoire devient également non jugeable si le rappel hors banc est constant par plafond.
- Pour E3, si les retests sont presque parfaitement corrélés, augmenter \(m\) mesure une propriété fixe des poids et de l’évaluateur, pas une probabilité de franchissement par resoumission.
- Pour E4, le rappel « après promotion » est non estimable pour toute classe dont aucun plant n’est promu ; il ne faut pas convertir cette absence en rappel nul ou en sélection parfaite.

### (c) Contrôles négatifs indispensables

- **E1 : permutation des scores au sein des lots et des classes**, en conservant tailles et dépendances. Sans ce contrôle, les plants sans gain ne suffisent pas à valider l’estimateur d’enrichissement.
- **Séparation des générateurs de plants** entre développement, calibration du seuil et test, avec familles de tâches entières réservées. Sans cela, le rappel mesure la reconnaissance du procédé de construction.
- **E2 : permutation des étiquettes ou des scores \(S\) avant sélection**, répétée sur plusieurs tirages, et remesure fraîche de \(S\). Le seul contrôle « le rappel R doit monter » est un contrôle positif de manipulation, pas un contrôle négatif du transfert.
- **E3 : rejets indépendants simulés à \(p_i\) connu**, pour vérifier que l’estimation de \(f\) et la formule de resoumission ne confondent pas bascule, passage et corrélation.

## Sur la proposition B

### (a) Défauts de méthode

- **La métrique de co-ratage de la fiche 1 n’identifie pas un effet de famille.** Conditionner sur « \(M_i\) rate » sélectionne des items différents selon le moniteur de référence. Sous indépendance conditionnelle à une difficulté latente \(X\),
  \[
  r_{ij}=\frac{\mathbb E[p_i(X)p_j(X)]}{\mathbb E[p_i(X)]\,\mathbb E[p_j(X)]}.
  \]
  Ainsi \(r_{ij}\) varie avec les taux marginaux de ratage et la distribution des difficultés, même sans angle mort partagé propre à une famille. La différence entre deux \(r\) n’en est donc pas une mesure pure.
- **Famille, rôle et modalité d’entrée sont confondus.** \(M_{\text{code}}\) et \(M_{\text{traj}}\) ne reçoivent pas la même information. Une comparaison same/autre famille faite sur ces rôles peut attribuer à la famille un effet dû à la complémentarité des entrées.
- **La covariance de la fiche 2 n’implique pas le signe de \(\Delta(k)\).** Le rappel du top-\(k\) dépend de toute la loi jointe score–détection–classe et du nombre de violations sélectionnées. Une covariance négative au sein des classes peut coexister avec \(\Delta(k)=0\), et réciproquement.
- **Le bras naturel mesure une prévalence résiduelle, pas directement un rappel.** Auditer seulement des non-signalées introduit une vérification dépendante du verdict ; comparer top-3 et rangs médians confond en outre fréquence des violations, gain de score et détectabilité.
- **Dans la fiche 3, \(T\) hérite des défauts d’un ratio.** Il compare aussi des \(d'\) obtenus avec moniteurs et distributions différents : leur égalité numérique ne garantit pas une échelle commune.
- **La fiche 4 ne rend pas réutilisation et couverture orthogonales.** R1 et R2 changent simultanément la règle de promotion, les tirages et potentiellement l’information disponible. Pour W2, des tirages frais n’élargissent pas par construction la nulle : l’échec de couverture ne constitue donc pas un test empirique indépendant de ce défaut.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- Le co-ratage est non identifiable dès que les probabilités de ratage sont proches de zéro ou de un, ou que le nombre d’items ratés par le moniteur de référence est faible. Un bootstrap sur items surestime la précision si les items partagent gabarits, jumeaux honnêtes ou tâches.
- L’effet de difficulté n’est séparable d’un effet famille que si les taux marginaux sont comparables et si le modèle de difficulté est correctement spécifié ; deux estimateurs ajustés sur des modèles différents peuvent conclure en sens opposés.
- Pour \(\Delta(3)\), le dénominateur est le nombre de violations effectivement présentes dans le top-3, non le nombre de classements rejoués. Mille rééchantillonnages d’un même pool ne créent pas mille observations indépendantes.
- Le ratio \(T\) a une variance potentiellement explosive lorsque le gain frais au dénominateur approche zéro ; son espérance peut ne pas exister utilement. Un \(d'\) est également non jugeable aux taux empiriques nuls ou parfaits sans convention de régularisation préspécifiée.
- Sous R1, \(1-(1-\alpha)^n\) exige des erreurs conditionnelles valides et indépendantes ; avec réutilisation adaptative, ce n’est ni une borne générale ni nécessairement la loi du nombre de consultations.

### (c) Contrôles négatifs indispensables

- **Fiche 1 : paires à entrées strictement identiques et difficultés appariées**, avec permutation des étiquettes de famille à propriétés marginales fixées. La permutation des verdicts dans une classe ne teste pas l’ajustement de difficulté.
- **Fiche 2 : scores permutés au sein des pools**, en plus des tricheries placebo. Dans le bras naturel, audit aveugle d’échantillons de signalées et de non-signalées, avec validation préalable de l’auditeur sur vérité plantée.
- **Fiche 3 : moyenne sur plusieurs sélections à étiquettes permutées.** Une variante aléatoire unique peut posséder un vrai gain ; attendre nécessairement un gain nul est incorrect.
- **Fiche 4 : témoin non adaptatif à budget et information équivalents.** Sans lui, aucune différence R1–R2 n’est attribuable spécifiquement à la réutilisation.

## Sur la proposition C

### (a) Défauts de méthode

- **La fiche 1 confond forum, retour d’information et composition du pool.** Le forum modifie les scores honnêtes, la diffusion des méthodes et le mélange des classes. Le protocole ne précise pas si les plants sont injectés avant ou après génération : s’ils sont ajoutés après, le mécanisme de réplication par le forum n’est pas testé.
- **Le contrôle proposé avec le nul v8 est invalide pour \(C_{\mathrm{rec}}\).** W2 est précisément présenté comme une classe que v8 déclare ne pas couvrir, avec douze promotions sur douze **[OBSERVÉ-NON-AUDITÉ, nos résultats §3]**. Il ne peut servir de témoin « couvert » pour cette classe.
- **La fiche 2 change trop de choses entre banc et hors banc.** Classe de violation, tâche, distribution des candidats et parfois nature de l’intervention varient ensemble. Le gain hors banc peut donc refléter la difficulté ou le taux de violations plutôt que le transfert de surveillabilité.
- **La conscience d’évaluation est post-traitement.** Conditionner l’analyse à son seuil peut sélectionner sur une variable affectée à la fois par la configuration et par la détectabilité ; cela ne démontre ni masquage ni causalité.
- **Dans la fiche 3, \(T_1\) et \(T_2\) changent trois facteurs : transparence, contenu du retour et couverture du nul.** Une chute de \(p_{\mathrm{W2}}\) peut être entièrement due à v9. Si v9 ferme la classe W2 testée, la réduction est partiellement vraie par construction.
- **Le volet post-médiane compare des procédures, pas seulement deux règles d’arrêt.** Seuil d’e-valeur et 99e centile diffèrent par données, budget et critère d’utilité. Transposer la dispersion \(\pm0,64\) de Petri à une courbe dose–réponse d’une autre échelle est invalide **[RAPPORTÉ pour la dispersion, pièce Kirchner §5]**.
- **Les duels conjoncts ne sont pas exclusifs clause par clause.** Une victoire du volet transparence ne tranche pas le volet e-valeurs. De même, dans la fiche 1, \(p>0,10\) n’établit pas une absence d’effet.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- Le test exact de Fisher sur trajectoires suppose des unités indépendantes ; rondes, agents, courses et copies de forum violent cette hypothèse. Le nombre de plants n’est pas la taille effective.
- \(\Delta\mathrm{Rappel}\) est non estimable si le top décile contient trop peu de plants, et non informatif si le rappel global est au plafond. \(\Delta\Delta\) devient également instable si les deux bras n’ont aucun support commun de scores.
- Pour la fiche 2, si le gain frais en distribution est nul, le test hors banc ne porte pas sur le transfert d’un gain. Si les violations hors banc sont rares ou si \(\mathrm{TPR}@5\%\) vaut presque partout zéro ou un, les dix points demandés sont hors résolution.
- Le passage d’AUC à \(\mathrm{TPR}@\mathrm{FPR}\) n’est pas anodin : deux lois de scores peuvent classer différemment ces paramètres. Les hypothèses ne sont donc pas définies par un estimand unique.
- Pour le volet e-valeurs, si le seuil n’est jamais franchi dans une course, la méthode « première au franchissement » n’existe pas ; conditionner aux courses avec franchissement sélectionne alors sur le résultat. Si les deux procédures choisissent la même méthode, le contraste est nul par construction.

### (c) Contrôles négatifs indispensables

- **Fiche 1 : sélection à scores permutés sur un pool figé**, puis forum rejoué avec traces figées. Sans ces deux placebos, l’interaction forum–classement n’est pas attribuable au mécanisme annoncé.
- **Fiche 2 : validation fraîche du gain \(B_{\mathrm{mon}}\)** et sélection à étiquettes permutées. Le contrôle \(\Delta\mathrm{TPR}_{\mathrm{in}}\) est une vérification positive ; les prédicteurs aléatoires ne remplacent pas un placebo de sélection.
- **Fiche 3 : plan factoriel transparence × couverture**, à retour identique, et comparaisons appariées à budget égal pour l’arrêt. Les anciens témoins v8 sont des tests de non-régression, pas des contrôles négatifs suffisants pour ces nouveaux contrastes.

## Sur la proposition E

### (a) Défauts de méthode

- **E-S mesure un changement de distribution conditionnelle, pas une dégradation du moniteur.** Celui-ci étant figé, \(D\) mélange nécessairement composition en familles, gravité et difficulté. La standardisation proposée ne résout ce problème que sur le support commun.
- **Le contraste avec filtre n’est pas entièrement factoriel.** Pour isoler son apport, il faut comparer uniforme-avec-filtre à uniforme-sans-filtre, puis classement-avec-filtre à classement-sans-filtre, avec audit identique ; sinon filtrage et classement restent confondus.
- **E-T peut certifier le gain initial sur les données ayant servi à choisir la configuration.** La condition « gain réel sur le banc de développement » ne suffit pas : sans remesure fraîche, le prérequis peut être satisfait par la seule malédiction du gagnant.
- **La qualité moyenne comparable ne rend pas les pools comparables.** Deux configurations peuvent avoir même score moyen mais des lois de scores, de gravité des violations et de difficulté différentes. \(G\) mesure alors l’effet conjoint de la configuration et du classement, pas uniquement le transfert de surveillabilité.
- **L’appariement honnête/invalide ne garantit pas l’absence de fuite.** Si une sortie de l’oracle mécanique contribue directement ou indirectement au score du classement, la sélection utilise une partie de l’étiquette de test.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- Pour E-S, la variance de \(R_C\) dépend du nombre de violations exécutées retenues par classement, et non des 768 candidats pilotes. Si ce nombre est faible, l’intervalle traverse naturellement la marge ; si elle est nulle, \(R_C\) et \(D\) sont indéfinis.
- Le rappel standardisé exige, pour chaque famille et gravité retenues, une probabilité non nulle d’apparaître dans les deux branches. Sans support commun, l’estimand standardisé dépend d’une extrapolation de modèle.
- Une probabilité de sélection presque déterministe peut laisser très peu de lots où une même violation est tantôt retenue, tantôt non retenue : la dépendance de lot réduit alors fortement la taille effective malgré de nombreuses traces.
- Pour E-T, si le gain frais de développement est nul ou si la variance interconfigurations du vrai paramètre de surveillabilité est nulle, la sélection ne produit aucun traitement identifiable. \(G\) ne mesure plus que du bruit de sélection.
- Même avec violations abondantes, \(G\) perd sa puissance si les rappels sont aux plafonds, si les fausses alertes imposent des seuils extrêmes, ou si les distributions de gravité n’ont pas de support commun entre configurations.

### (c) Contrôles négatifs indispensables

- Le contrôle de scores permutés, déjà présent, est nécessaire mais doit être complété par **uniforme contre uniforme**, avec mêmes tailles de lots et même analyse : cela valide l’absence de biais de l’estimateur et le calcul de sa variance.
- **Verdicts du moniteur permutés au sein des familles de lots** : tout contraste systématique résiduel révèle une fuite d’étiquettes ou une erreur du pipeline.
- **Calibration du seuil, estimation du gain de développement et test final sur trois partitions indépendantes.** Sans remesure fraîche du gain, le contrôle à étiquettes permutées ne suffit pas à écarter la sélection sur bruit.
- **Classement placebo calculé sans aucune information de l’oracle**, puis vérification que l’oracle n’entre ni dans les scores ni dans l’appariement des candidats retenus. Sans cette séparation, la prétendue sélection aveugle aux violations n’est pas établie.

FIN-DE-CELLULE