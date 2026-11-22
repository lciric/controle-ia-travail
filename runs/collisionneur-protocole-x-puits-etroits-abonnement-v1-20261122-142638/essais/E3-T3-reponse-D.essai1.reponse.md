# Proposition D — Réponse aux critiques

**RAPPORTÉ —** Aucun journal de tirages, coût mesuré ni verdict de référence du générateur cible n’est fourni. Les protocoles ci-dessous ne sont pas des résultats.

## (a) Décisions sur les critiques visant D

| Critique | Décision |
|---|---|
| **A, B, C, E, F — Les duels sur le budget uniforme et sur la dépendance sont déjà tranchés.** | **Acceptée.** Je les retire de la liste des expériences. Ce sont des preuves par contre-exemple : elles réfutent des énoncés universels sans rien mesurer sur la source effectivement servie. |
| **A, B, C, E, F — Le signe du gain sur le banc gelé ne tranche pas au niveau de la loi.** | **Acceptée.** Le signe reste exact *pour ce banc*. **VÉRIFIÉ —** Sous égalité des probabilités de discordance dans les deux sens, le gain empirique et sa valeur opposée ont même loi. La probabilité d’un gain strictement positif est donc la moitié de la probabilité d’un gain non nul, et non une erreur de décision contrôlée. Je remplace le signe par un intervalle apparié et une marge d’utilité fixée avant le test. |
| **A, B, E — Sélection du meilleur comparateur ; F — sélection du seuil ou du quota.** | **Acceptée comme risque du protocole.** **HYPOTHÈSE —** Le comparateur principal sera l’ordre de tirage avec cache exact. Si un prédicat nécessaire est disponible, la décision de l’intégrer au comparateur sera prise sur calibration séparée. Score, seuil, politique d’arrêt, quota et départage seront gelés avant l’évaluation. Aucun maximum calculé sur le test ne servira de référence. |
| **A, B, C, E, F — Rareté des discordances ; plancher et plafond.** | **Acceptée.** **VÉRIFIÉ —** Une session discordante doit contenir un positif produit et ne peut pas avoir été résolue par les deux politiques. Une recherche où presque rien n’est produit et une recherche où presque tout est reconnu peuvent donc toutes deux être peu informatives sur le classement. Je conserve toutes les sessions, y compris les doubles échecs, dans le dénominateur. |
| **A, C, F — Propriété synthétique favorable au score ; partage de motifs ; domaine énumérable.** | **Transformée en contrôles.** Une corrélation entre syntaxe et propriété n’est pas en soi une fuite ; choisir la propriété *parce que* le score y réussit ne teste pas son transfert. **HYPOTHÈSE —** Séparer les familles de propriétés et de gabarits, puis tester la politique gelée sur la cible. Garder le petit domaine exhaustif pour vérifier le code ; utiliser aussi un domaine dont l’exploration exhaustive excède le budget. **VÉRIFIÉ —** Une table accessible à l’auditeur seul ne permet pas à la politique de faire produire un objet absent de ses tirages. |
| **A — Méthodes répandues, taille de grammaire et rapport des coûts insuffisamment traités.** | **Partiellement acceptée.** La répétition, le rejet par filtre et la mémoïsation étaient traités ; leurs garanties sont nommées en (c). **HYPOTHÈSE —** J’ajoute en (b) une comparaison à taille de langage et tarifs préspécifiés. Le cardinal du langage n’est pas la longueur de la description grammaticale. |
| **B, C, E, F — Coût conditionnel, quota entier, troncature et fidélité du rejeu.** | **Acceptée pour le banc ; rejetée comme erreur de la formule de coût moyen.** D limitait explicitement cette formule à la vérification de *tous* les retenus. Je donne ci-dessous le calcul distinct sous quota. **VÉRIFIÉ —** Qu’un surcoût ne change pas le quota entier à un budget donné est un effet réel du plafond, pas un coût nul. **HYPOTHÈSE —** Publier dépenses et quota ; ne pas apparier sur le temps de décision dans l’échantillon de rendement. |
| **B, C, E, F — Trop peu de positifs pour mesurer la détection ; négatifs appariés non représentatifs.** | **Acceptée, avec précision.** **VÉRIFIÉ —** Sur \(n\) étiquettes i.i.d., la probabilité d’un dénominateur positif nul est \((1-p)^n\) ; elle dépasse la moitié exactement lorsque \(p<1-2^{-1/n}\). Avec \(K>0\) positifs indépendants représentatifs *tous acceptés*, la borne inférieure binomiale unilatérale de sensibilité au risque \(\alpha\) vaut \(\alpha^{1/K}\). Elle ne vaut pas pour n’importe quel nombre d’acceptations. **HYPOTHÈSE —** Auditer séparément les négatifs naturels sans appariement et réserver les paires construites au diagnostic. |
| **A, C, E, F — Absence de mesure sur la dépendance réelle ; borne conditionnelle non identifiable ; couverture de la borne après zéro succès.** | **Acceptée pour la mesure ; rejetée comme objection à l’énoncé i.i.d. à horizon fixe.** **VÉRIFIÉ —** Estimer le risque moyen après une suite d’échecs ne borne pas le risque après *chaque historique détaillé*. Un mélange comportant des sessions toujours négatives peut invalider l’inversion binomiale sur les tirages groupés. Je n’applique cette inversion ni à ces tirages ni après un arrêt choisi selon les verdicts. |
| **A, B, C, E, F — Le score constant ne contrôle que le départage.** | **Acceptée.** J’adopte les contrôles par permutation, bruit et propriété indépendante, avec une restriction : le gain attendu d’un score sans information n’est nul que si les bras ont les mêmes occasions de vérifier des objets distincts au même coût. Un gain observé sur une graine ne démontre pas une fuite. |
| **B — Statut des déductions de D.** | **Distinction maintenue.** « VÉRIFIÉ » qualifie ici les conséquences mathématiques dont le calcul est donné sous hypothèses explicites. Il ne qualifie ni la satisfaction de ces hypothèses par le générateur ni l’exécution d’un protocole. Aucun statut des pièces n’est modifié. |

## (b) Expériences corrigées

### D’abord : le budget annoncé suffit-il sur la source cible, sans classement ?

**HYPOTHÈSE — Protocole.** Fixer la propriété, la version du service, le régime de session, le plafond dur \(B\), le risque d’échec admissible \(\delta\) et la politique de référence. Une unité expérimentale est une session entière. Tirer des sessions de même loi avec réinitialisations indépendantes si l’interface les permet ; conserver l’ordre et la date des appels. Sans réplication indépendante justifiable, publier une description des trajectoires, pas un intervalle binomial de population.

**HYPOTHÈSE — Duel.** Soit \(z_B\) la probabilité qu’une session de référence ne rende **aucun témoin véritable accepté à temps**. Opposer \(H_A:z_B\le\delta\) à \(H_B:z_B>\delta\). Fixer à l’avance le nombre de sessions et le niveau de confiance. Sur les indicatrices d’échec par session, une borne supérieure \(\le\delta\) écarte \(H_B\) au risque annoncé ; une borne inférieure \(>\delta\) écarte \(H_A\). Un intervalle qui chevauche le seuil est **non concluant**, et non une troisième hypothèse. L’indépendance *intra*-session n’est pas requise pour ce duel.

**HYPOTHÈSE — Diagnostic qui explique un échec.** Auditer hors ligne les objets effectivement produits, par une vérité indépendante des verdicts opérationnels. Distinguer : aucun positif tiré ; positif tiré mais non vérifié à temps ; positif vérifié mais rejeté ; annonce sans témoin véritable. Conserver un journal à horizon de tirages fixe, sans arrêt au premier succès, pour les diagnostics de dépendance. Pour chaque rang \(k\) préspécifié, estimer
\[
h_k=\Pr(Y_{k+1}=1\mid Y_1=\cdots=Y_k=0)
\]
par le nombre de premiers succès au rang \(k+1\) divisé par le nombre de sessions encore sans succès après \(k\) tirages. Publier ce dénominateur ; s’il est nul, le risque n’est pas estimable. Comparer les sessions intactes à des sessions recomposées par permutation **entre sessions, à rang, propriété et fenêtre temporelle identiques**. Cela diagnostique un effet de regroupement ; l’absence d’écart ne prouve pas l’indépendance.

### Ensuite : un classement achète-t-il un gain utile au même plafond ?

**HYPOTHÈSE — Duel apparié.** Sur une réserve indépendante de celle utilisée pour concevoir les politiques, comparer le score au comparateur gelé. Soient \(p_{10}\) et \(p_{01}\) les probabilités que seule la politique scorée, respectivement seule la référence, rende un témoin confirmé. Pour une marge d’utilité \(\varepsilon>0\) choisie par l’arbitre avant l’essai, opposer
\[
H_A:\Delta=p_{10}-p_{01}>\varepsilon,\qquad
H_B:\Delta\le\varepsilon .
\]
Les deux politiques voient les mêmes flux dans le même ordre de production, mais paient leurs propres tirages, calculs, accès au cache et vérifications. Le budget économisé par le comparateur sans score reste utilisable.

**VÉRIFIÉ — Décision et dimensionnement.** Sur \(J\) sessions i.i.d., les comptes de discordances donnent chacun, marginalement, un compte binomial. Construire pour chaque \(p_{ab}\) discordant un intervalle binomial exact \([L_{ab},U_{ab}]\) de risque \(\alpha/2\). Par borne de l’union,
\[
[L_{10}-U_{01},\ U_{10}-L_{01}]
\]
couvre \(\Delta\) avec probabilité au moins \(1-\alpha\). Une borne basse \(>\varepsilon\) réfute \(H_B\) au risque annoncé ; une borne haute \(\le\varepsilon\) réfute \(H_A\) au même sens. Sinon, aucune réfutation. Si \(d=p_{10}+p_{01}\), la probabilité de n’observer aucune discordance vaut \((1-d)^J\). **HYPOTHÈSE —** Dimensionner sur un pilote disjoint par calcul de puissance multinomial pour des gains de part et d’autre de la marge ; si le budget ne permet pas de les distinguer, l’annoncer avant le test.

**HYPOTHÈSE — Contrôles et coûts.**

- Conserver le score constant pour tester le départage. Pour tester le signal, employer aussi des rangs aléatoires continus, des scores permutés à coût inchangé et un score réappris après permutation des étiquettes. Pour le contrôle de propriété, attribuer après gel une étiquette aléatoire secrète à chaque **objet distinct**, conservée lors de ses répétitions. Égaliser le nombre d’objets distincts vérifiés pour ce diagnostic seulement ; ne pas l’égaliser dans le duel de rendement.
- Interdire aux politiques l’accès à la vérité d’audit et aux temps futurs. Prévoir un flux assez long pour les deux bras ; si sa longueur ne suffit pas, ne pas interpréter son épuisement comme un échec du générateur. Valider le rejeu par des passes chronométrées en ordre randomisé, à charge comparable et état du cache matériel déclaré. Une décision interrompue au plafond coûte le temps consommé mais ne compte pas comme reconnaissance.
- Fixer un couple principal *langage–tarif* pour la décision. Sur des domaines secondaires de cardinaux différents, comparer à masse positive fixée, puis sous loi uniforme à nombre de positifs fixé : le premier contraste sépare taille et masse, le second les fait varier ensemble de façon connue. Rejouer la politique sous des tarifs annoncés d’avance dans une unité commune ; distinguer cette analyse de sensibilité des mesures aux coûts physiques réels. Rapporter les coûts des objets retenus, rejetés, positifs et négatifs sans supposer leurs moyennes égales.

**VÉRIFIÉ — Contrôle analytique du plafond.** Pour \(m\) tirages i.i.d., un filtre booléen de taux de rétention \(r>0\), posons \(u=\Pr(X\in S,F=1)\). Si le budget paie les \(m\) productions et filtrages, puis au plus \(k\) vérifications à prix constant, vérifier **les premiers retenus dans l’ordre de tirage**, sans cache, donne exactement
\[
\Pr(R_B)=1-\mathbb E\!\left[(1-u/r)^{\min(K,k)}\right],
\qquad K\sim{\rm Bin}(m,r).
\]
Conditionnellement aux positions retenues, chacune porte indépendamment un positif avec probabilité \(u/r\). Pour \(r=0\), aucun témoin n’est reconnu. Ce calcul teste la comptabilité du quota ; il ne s’applique pas au tri par score ni aux coûts dépendant de l’objet.

## (c) Réponse à l’arbitre — une page

**VÉRIFIÉ — Ce qui est garanti.** Soit \(R_B\) l’événement « un objet effectivement tiré, véritablement positif, est reconnu avant le plafond \(B\) ». Avec vérificateur exact, tirages i.i.d. de loi \(P\), \(p=P(S)\), coûts constants positifs \(c_g,c_v\) et vérification dans l’ordre, \(n=\lfloor B/(c_g+c_v)\rfloor\) essais donnent
\[
\Pr_P(R_B)=1-(1-p)^n.
\]
Ainsi, **pour toute loi de masse positive et tout** \(0<\delta<1\), **il existe un budget fini** atteignant \(1-\delta\). Pour choisir ce budget *avant* de connaître la loi, un plancher certifié \(0<p_0<1\) suffit : prendre \(n=\lceil\log\delta/\log(1-p_0)\rceil\). Si \(p_0=1\), un essai suffit. L’arrêt au premier succès est presque sûr pour chaque \(p>0\), avec coût moyen \((c_g+c_v)/p\), mais sans plafond déterministe si \(p<1\).

**VÉRIFIÉ — Ce qui est impossible sans hypothèse supplémentaire.** Aucun budget fini ne vaut pour **toutes** les lois i.i.d. de masse positive arbitrairement petite : même avec vérification gratuite, au plus \(m=\lfloor B/c_g\rfloor\) tirages produisent un positif avec probabilité au plus \(mp\). À marginale \(p\) connue, la répétition du seul premier tirage donne une probabilité de succès égale à \(p\), quel que soit l’horizon positif. En revanche, un risque conditionnel de succès minoré par \(q>0\) après toute histoire d’échec donne, par produit des probabilités conditionnelles, un risque d’échec au plus \((1-q)^n\). Un seul témoin prouve l’existence, pas un tel plancher.

**VÉRIFIÉ — Ce que changent la grammaire et la méthode.** Sur un langage fini de \(N\) objets dont \(K>0\) sont positifs, une permutation uniforme sans remise donne après \(n\le N\) essais un risque d’échec \(\binom{N-K}{n}/\binom Nn\), nul dès \(n>N-K\). Ni la finitude ni la publicité de la grammaire n’imposent cette loi de parcours. L’énumération peut trouver un témoin sans que la source l’ait produit. Un parseur syntaxique ne sélectionne rien si toutes les sorties sont valides. La mémoïsation exacte évite des revérifications si la propriété est fixe ; elle ne crée pas de positif. Le filtrage par condition nécessaire conserve tous les positifs **parmi les tirages**, pas nécessairement parmi les vérifications payables. Le classement *best-of-\(m\)* ne garantit rien sur les premiers rangs sans hypothèse sur le score. L’échantillonnage préférentiel qui impose de changer la loi de proposition exige un autre accès. Le rapport \(c_v/c_g\) détermine ce que vaut une vérification évitée ; il ne mesure ni le rappel du filtre ni le coût conditionnel des objets qu’il retient.

**VÉRIFIÉ — Ce qu’une observation peut établir.** À horizon fixe, après zéro positif sur \(n>0\) essais i.i.d. exactement étiquetés, l’inversion de \((1-p)^n=\delta\) donne la borne **supérieure** unilatérale \(1-\delta^{1/n}\), non un plancher pour la recherche suivante. Référence : C. J. Clopper et E. S. Pearson, 1934, *The Use of Confidence or Fiducial Limits Illustrated in the Case of the Binomial*.

**HYPOTHÈSE — Première expérience à faire.** Mesurer directement, sur des sessions cibles indépendantes au plafond réel, la probabilité que **l’ordre brut avec cache exact** rende un témoin confirmé. Auditer les objets produits mais non reconnus. Si les sessions échouent faute de production, aucun reclassement de ces objets ne les sauvera ; si des témoins produits restent non vérifiés, le duel de classement a une cible mesurable. Ni la fréquence cible, ni l’exactitude du vérificateur matériel, ni un gain du score ne sont établis ici.

FIN-DE-CELLULE