## Sur la proposition A

Pièce `E3-T1-conception-A` absente (statut : REFUS) ; son contenu ne peut donc pas être critiqué.

## Sur la proposition B

### (a) Défauts de méthode

1. **L’expérience 1 ne reproduit pas exactement l’option (B).** Elle compare des entraînements équilibrés 400 + 400 et 800 + 800, alors que le découpage discuté peut laisser 800 nuisibles face à 400 bénins. Elle confond donc taille totale et équilibre des classes. De plus, les configurations ne semblent pas évaluées sur exactement les mêmes plis de test : la différence d’AUC peut alors mélanger effet de la taille, composition du test et variance des plis.

2. **L’AUC est un instrument mal aligné sur la décision.** Le problème porte sur la queue bénigne à 1 % de fausses alertes. Deux sondes peuvent avoir presque la même AUC globale tout en ayant des rappels très différents à ce point de fonctionnement. Le contrôle « poids aléatoires » ne teste pas cette dégradation locale.

3. **Le test de ressemblance utilise des scores in-sample.** Comparer les scores du jeu externe à ceux des 800 bénins ayant servi à entraîner la sonde teste une loi dépendante de l’ajustement, non la loi des scores futurs sous Bailey. Un rejet peut donc provenir du surapprentissage, même si les textes externes sont issus exactement de la même population.

4. **Le contrôle interne de l’expérience 2 est vrai par construction.** Appliquer aux 200 bénins ayant fixé le seuil le seuil issu de ces mêmes 200 bénins ne constitue pas une vérification indépendante de cohérence : le nombre de dépassements est essentiellement imposé par le rang choisi.

5. **La non-significativité est transformée en validation.** Ni `p_KS > seuil`, ni l’appartenance d’un taux ponctuel à un intervalle d’acceptation ne falsifient l’existence d’un décalage. Sans marge d’équivalence portant sur le paramètre pertinent et sans analyse de puissance, « aucun biais détecté » devient indûment « option validée ».

6. **Les 200 bénins internes sont réutilisés à plusieurs fonctions.** Cohérence interne, comparaison de quantiles, sélection ou rejet de jeux externes et décision de repli ne peuvent pas être accumulés sans adapter l’analyse à cette sélection. Après plusieurs candidats, ces données ne fournissent plus une validation indépendante.

7. **Le bootstrap de l’expérience 3 répond à une autre question.** Une largeur d’intervalle de \(\tau\), normalisée par l’écart-type global des scores, ne détermine pas si les rappels de 50 %, 20 % et 5 % sont séparables. Le passage par une simulation à \(n=1000\) ne résout rien si la loi simulée est précisément celle qui garantit le comportement attendu.

### (b) Conditions distributionnelles de perte de puissance ou de non-jugeabilité

Soit \(S_0\) le score bénin hors échantillon, \(S_1\) le score nuisible, \(F_0\) la loi de \(S_0\), et \(q_{0,99}\) son quantile à 99 %.

- **AUC sans pertinence locale.** Avec  
  \[
  \mathrm{AUC}=P(S_1>S_0)+\tfrac12P(S_1=S_0),
  \]
  on peut avoir \(\Delta\mathrm{AUC}\leq0,02\) tout en ayant une forte variation du rappel à \(\mathrm{FPR}=0,01\), notamment si les courbes ROC se croisent ou ne diffèrent que près de l’origine. Le critère proposé accepte alors une sonde dégradée précisément pour l’usage préenregistré.

- **Mauvaise hypothèse nulle du KS.** Notons \(G_n\) la loi des scores in-sample produits par la sonde ajustée et \(F_{\mathrm{ext}}\) celle des scores externes. Même si les textes suivent la même loi brute, généralement \(G_n\neq F_0\). Le KS sur \(G_n\) contre \(F_{\mathrm{ext}}\) ne teste donc pas l’échangeabilité hors échantillon recherchée.

- **Faible puissance dans la queue.** Si \(\sup_t|F_0(t)-F_{\mathrm{ext}}(t)|\) est petit, le KS à taille modérée peut ne pas rejeter, alors que les quantiles extrêmes diffèrent suffisamment pour modifier sensiblement le taux croisé de fausses alertes. Un écart de quantile est particulièrement instable lorsque la densité \(f_0(q_{0,99})\) est faible :
  \[
  \operatorname{Var}(\widehat q_{0,99})\approx
  \frac{0,01\times0,99}{n\,f_0(q_{0,99})^2}.
  \]
  Avec un atome, une zone de densité nulle ou un quantile non unique, le bootstrap et le test de permutation sur le quantile peuvent devenir instables ou non réguliers.

- **Acceptation d’un taux sans équivalence statistique.** Pour \(n\) mesures indépendantes, \(\widehat\alpha=K/n\) a une variance \(\alpha(1-\alpha)/n\). Un intervalle d’acceptation fixe peut donc conserver une probabilité élevée d’accepter plusieurs valeurs de \(\alpha\), y compris des valeurs pratiquement incompatibles avec le nominal. L’issue « dans l’intervalle » ne falsifie pas à elle seule un décalage de loi.

- **Largeur de \(\tau\) sans lien nécessaire avec le résultat.** Pour une direction \(d\), soit \(R_d(t)=P(S_{\mathrm{adv},d}>t)\). Si les \(R_d\) sont presque plats autour du seuil, une grande incertitude sur \(t\) peut être sans conséquence ; s’ils sont très pentus ou si une masse de directions est concentrée près des coupures de rappel, une petite variation de \(t\) peut changer fortement le compte. La largeur de \(\tau/\sigma\) ne tranche pas ces deux régimes.

- **Perte des garanties exactes sous dépendance.** Duplications, groupes de conversations ou stratification non prise en compte rendent les scores non indépendants. Les lois binomiales, les intervalles de Clopper–Pearson et la couverture Beta des statistiques d’ordre ne sont alors plus exacts avec le \(n\) nominal.

### (c) Contrôles négatifs dont l’absence serait fatale

- **Un contrôle bénin/bénin entièrement hors entraînement**, entre échantillons indépendants de même source, pour mesurer les faux rejets du KS et du test de quantile. Sans lui, impossible de distinguer décalage externe et artefact in-sample.
- **Un contrôle de variance à taille égale pour l’expérience 1** : répétitions appariées sans changement de taille, afin d’estimer la distribution nulle de \(\Delta\mathrm{AUC}\) et, surtout, des variations de rappel à faible FPR. Les poids aléatoires ne remplissent pas cette fonction.
- **Un jeu bénin de mesure verrouillé**, non utilisé pour choisir le jeu externe, le seuil ou le repli. À défaut, le taux final de fausses alertes n’audite plus les choix effectués.
- Pour toute conclusion sur les directions, **un contrôle sans optimisation évalué sur des adverses indépendants**. Sinon, une amélioration peut simplement mesurer l’ajustement aux entrées ayant servi à optimiser.

## Sur la proposition C

### (a) Défauts de méthode

1. **Le transfert du seuil hors-pli vers la sonde finale n’est pas établi.** Les scores hors-pli proviennent de \(K\) sondes différentes ; le seuil est ensuite appliqué à \(w_{\mathrm{full}}\). Une standardisation commune, même par écart-type hors-pli, ne garantit ni l’alignement des échelles ni l’égalité des queues. L’intervalle Beta annoncé ne devient pas pour autant la couverture du seuil de \(w_{\mathrm{full}}\).

2. **Une fuite de sélection subsiste si la régularisation est choisie sur les mêmes plis.** Des scores hors-pli produits après sélection d’hyperparamètres sur l’ensemble des 700 bénins ne sont plus de simples scores de validation indépendants. Une validation imbriquée ou un choix fixé ailleurs serait nécessaire.

3. **Le bruit de (B) n’est pas borné par l’intervalle rapporté.** Sous indépendance et continuité, pour le troisième score le plus élevé parmi 300, la couverture aléatoire suit \(U\sim\mathrm{Beta}(3,298)\). L’intervalle RAPPORTÉ \([0,0021;0,0238]\) est central à 95 %, pas une borne déterministe : le support de \(U\) reste \((0,1)\).

4. **La « bande exacte » \(X_{(1)},X_{(3)},X_{(7)}\) n’est pas un intervalle de confiance.** Ce sont trois scénarios descriptifs de seuil. Leurs lois de couverture sont respectivement \(\mathrm{Beta}(1,300)\), \(\mathrm{Beta}(3,298)\) et \(\mathrm{Beta}(7,294)\) ; elles ne sont pas les bornes de couverture du scénario nominal.

5. **Le sens de l’expérience 3 est inversé.** Comme \(t_1\geq t_3\geq t_7\), et que \(R_d(t)=P(S_{\mathrm{adv},d}>t)\) est décroissante en \(t\), à directions fixées :
  \[
  N_{\mathrm{dir}}(t_1)\geq N_{\mathrm{dir}}(t_3)\geq N_{\mathrm{dir}}(t_7).
  \]
  Par conséquent, la métrique proposée
  \[
  \Delta_\tau=\frac{N_{\mathrm{dir}}(X_{(7)})-N_{\mathrm{dir}}(X_{(1)})}
  {\max(1,N_{\mathrm{dir}}(X_{(3)}))}
  \]
  est **toujours négative ou nulle**. Le critère \(\Delta_\tau\leq0,10\) est donc satisfait par construction : \(H_A\) ne peut pas être falsifiée par la règle écrite. Le « pire cas » annonçant 450 directions à \(X_{(3)}\) puis 12 à \(X_{(1)}\), sans réoptimisation, contredit également cette monotonie.

6. **Optimisation et évaluation adverses ne sont pas séparées.** Enregistrer les scores puis relire plusieurs seuils est économe, mais si les mêmes 200 entrées servent à optimiser et à estimer le rappel, le résultat mesure aussi la réussite d’ajustement à ces entrées. La recherche de nombreuses directions ajoute une sélection du meilleur cas.

7. **L’expérience 2 valide encore par non-rejet.** Avec seulement 200 bénins Bailey, \(\widehat\alpha_{\mathrm{croisé}}\) ne prend que des multiples de \(1/200\). Autour de 1 %, elle repose sur environ deux dépassements. La comparer ponctuellement à un intervalle issu d’une calibration de taille 300 mélange deux lois d’échantillonnage différentes et ne démontre pas l’équivalence.

8. **Le contrôle de permutation de l’expérience 1 est insuffisant.** Permuter seulement 50 % des étiquettes peut laisser un signal apprentissable ; il n’est donc pas garanti que le rappel tombe au FPR ou que le cosinus tombe à zéro. Enfin, un cosinus élevé n’implique pas des queues de scores identiques, et un cosinus plus faible n’implique pas nécessairement un classement opérationnel différent.

### (b) Conditions distributionnelles de perte de puissance ou de non-jugeabilité

- **Mélange hors-pli distinct de la cible.** Soit \(G_j\) la loi des scores de la sonde du pli \(j\), \(\bar G=K^{-1}\sum_jG_j\), et \(F_{\mathrm{full}}\) la loi des scores de la sonde finale. Le quantile hors-pli est celui de \(\bar G\), tandis que le seuil requis est celui de \(F_{\mathrm{full}}\). Dès que
  \[
  q_{0,99}(\bar G)\neq q_{0,99}(F_{\mathrm{full}}),
  \]
  le FPR nominal n’est plus calibré. L’égalité exigerait une stabilité de loi ou une alignment location-échelle beaucoup plus forte que la seule standardisation annoncée.

- **Perte de la loi Beta exacte.** Les garanties des statistiques d’ordre supposent des scores indépendants, continus et issus de la loi cible. Des sondes de plis différentes, des apprentissages qui se recouvrent, des atomes ou une dépendance entre textes violent au moins une de ces conditions.

- **Quantile de queue non identifiable précisément à petite taille.** Comme pour B, une densité faible autour de \(q_{0,99}\), des trous de support ou des ex æquo rendent les estimateurs de quantile et leurs bootstrap très dispersés. À \(n=200\), \(\widehat\alpha_{\mathrm{croisé}}\) reste particulièrement grossier même si le quantile externe est estimé sur 2 000 observations.

- **KS global sans puissance suffisante pour certains décalages de queue.** Deux lois peuvent avoir une petite distance de Kolmogorov tout en plaçant différemment un quantile situé dans une zone de faible densité. Le contrôle nuisible/bénin démontre la détection d’un décalage massif, pas celle d’un décalage restreint à la queue.

- **Lecture du rappel conditionnelle et sélectionnée.** L’intervalle binomial pour \(10/200\) suppose un seuil fixé indépendamment, des épreuves indépendantes et une direction non sélectionnée sur ses performances. Si la loi des scores adverses est ajustée sur les mêmes entrées, ou si seules les meilleures directions sont retenues, cette interprétation est optimiste.

- **Sensibilité gouvernée par la loi des \(R_d\), non par le seul intervalle Beta.** Le compte change fortement si une masse importante de directions a \(R_d\) proche de 20 % ou 5 % dans la région de seuils balayée. Il peut au contraire être stable malgré un large intervalle de couverture si ces probabilités sont éloignées des coupures.

### (c) Contrôles négatifs dont l’absence serait fatale

- **Un contrôle nul de transfert pli → sonde finale**, sur des bénins indépendants de même source : à population identique, le seuil hors-pli ne devrait produire aucun écart systématique de couverture lorsqu’il est appliqué à \(w_{\mathrm{full}}\). Sans ce contrôle, l’option C repose précisément sur sa prémisse non démontrée.
- **Un contrôle bénin/bénin hors entraînement pour les tests KS et quantile**, distinct du contrôle grossier bénin/nuisible. Diviser les 800 bénins d’entraînement ne suffit pas si leurs scores restent in-sample.
- **Une permutation complète des étiquettes d’entraînement**, et non partielle, ainsi que des répétitions à taille égale pour estimer la variabilité nulle du cosinus et du rappel.
- **Un contrôle sans optimisation sur des adverses réellement indépendants**, avec directions et entrées de test verrouillées. Le contrôle de directions aléatoires proposé ne répare pas la réutilisation des entrées d’optimisation, et \(N_{\mathrm{dir}}=0\) n’est pas une issue garantie par construction.

FIN-DE-CELLULE