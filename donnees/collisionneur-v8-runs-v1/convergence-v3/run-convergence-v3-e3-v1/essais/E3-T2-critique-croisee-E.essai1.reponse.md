**VÉRIFIÉ — pièces absentes :** le pilote complet, les entrées `resultats` du calibrage et le PDF annoncé ne sont pas servis ; je n’en reconstruis aucun contenu.

# Proposition E — critique croisée de méthode

**Convention.** Les mentions **VÉRIFIÉ** ci-dessous désignent une lecture du code servi ou un contre-calcul explicité, non une nouvelle exécution. Les résultats empiriques cités par les propositions conservent leur statut. Les contre-exemples nouveaux sont **illustratifs**.

**HYPOTHÈSE — règle proposée pour les duels.** Chaque comparaison doit définir un paramètre populationnel \(\vartheta\), puis opposer \(H_A:\vartheta>c\) à \(H_B:\vartheta\le c\). Une borne inférieure dépassant \(c\) réfute \(H_B\) ; une borne supérieure située sous \(c\) réfute \(H_A\), au risque préenregistré. Un intervalle chevauchant \(c\) reste **indéterminé** : il ne falsifie rien. Cette distinction manque dans plusieurs conceptions.

## Sur la proposition A

### (a) Défauts de méthode

**VÉRIFIÉ — erreur dans l’argument sur les retours i.i.d.** A affirme qu’une loi i.i.d. à peu de modes peut produire \(I_3\) supérieur à la référence d’échangeabilité par sa seule géométrie. Ce n’est pas vrai sous les conditions invoquées. Conditionnellement au déplacement courant, les similarités aux déplacements précédents sont échangeables. Sans égalités, chacune a la même probabilité d’être maximale : on retrouve \((t-2)/(t-1)\). Avec des égalités, le test strict `>` peut **réduire**, non augmenter, cette probabilité. Une mixture i.i.d. continue à peu de modes ne suffit donc pas à expliquer l’excès.

La permutation reste utile, mais elle teste l’échangeabilité temporelle, **pas spécifiquement l’existence d’un cycle**. Une alternance stochastique ou une dérive non stationnaire peut la faire rejeter.

**VÉRIFIÉ — conclusions dépassant les quantificateurs testés.**

- Le maximum de V sur quelques moniteurs candidats est une borne inférieure du supremum sur la classe linéaire. Leur échec ne réfute pas l’existence d’un autre moniteur performant, ni tous les mécanismes produisant un moniteur pur.
- Des poids mélangés rendus pour B ne démontrent pas l’absence de tout équilibre pur du jeu complet.
- L’absence d’équilibre pur ne démontre pas une orbite périodique, ni des revisites à horizon fini.
- Un poids maximal minimal faible parmi les équilibres prouve l’existence d’une stratégie mélangée optimale, pas la nécessité de mélanger.

**VÉRIFIÉ — mauvais nom de métrique.**  
\(v_G-\min_jU(\bar p,j)\) est un déficit de sécurité du défenseur dans \(G\), pas NashConv d’un profil. Il ne mesure aucune possibilité d’amélioration du défenseur contre une stratégie adverse \(q\).

**HYPOTHÈSE — confusions causales.** Un avantage de \(A_q\) peut provenir du jeu d’attaques, de sa pondération, de l’initialisation ou de la sélection finale. Il ne suffit pas à désigner « la règle uniforme » comme cause. De même, moyenner les poids dépend de leur échelle, alors que les décisions seuillées peuvent rester inchangées sous une transformation affine positive des scores.

### (b) Conditions mesurables de perte de puissance ou de non-jugement

| Mesure | Condition au niveau des lois, paramètres et estimateurs |
|---|---|
| \(I_3\) et permutation | **VÉRIFIÉ — contre-calcul :** si deux lois de trajectoires induisent la même loi de \(I_3\), aucun test fondé uniquement sur \(I_3\) ne les distingue. Des déplacements nuls ou des masses atomiques créent des égalités ; la référence sans égalités n’est alors plus applicable telle quelle. |
| Maximum des V candidats | **HYPOTHÈSE :** si l’écart entre le meilleur candidat testé et le supremum de la classe dépasse la marge, le verdict « plafond de classe » est non identifiable. Si sélection et estimation utilisent les mêmes erreurs Monte-Carlo, le maximum est optimiste. |
| Décroissance du déficit restreint | **VÉRIFIÉ — définition :** lorsque \(G_T\) change avec \(T\), les déficits portent sur des jeux différents. Une décroissance n’identifie pas à elle seule une convergence dans un jeu fixe. |
| Moyenne des poids, cosinus | **VÉRIFIÉ — invariance :** des représentations \(s\) et \(as+b\), \(a>0\), donnent les mêmes décisions après calibration correspondante, mais pas les mêmes moyennes de paramètres. Une annulation des poids moyens peut rendre la calibration non définie. |
| Pureté | **VÉRIFIÉ — contre-exemple illustratif :** plusieurs lignes optimales identiques autorisent une mixture diffuse sans aucun avantage fonctionnel sur une ligne seule. |

### (c) Contrôles négatifs indispensables

**HYPOTHÈSE — contrôles requis :**

- Lois i.i.d. continues **multimodales**, puis lois atomiques avec traitement explicite des égalités : indispensables pour éprouver A4.
- Loi temporelle markovienne alternante sans périodicité déterministe : indispensable avant d’appeler tout rejet de permutation « cycle ».
- Moniteurs fonctionnellement identiques sous reparamétrisation : la conclusion sur la moyenne ne doit pas dépendre arbitrairement de leur échelle.
- Sélection des candidats sur un échantillon, estimation du candidat retenu sur un autre.
- Matrice à lignes optimales dupliquées : le diagnostic de « mélange nécessaire » doit y être négatif.

**HYPOTHÈSE — duel réparable.** Opposer « le meilleur membre de la **liste gelée** gagne plus que la marge » à son complément, et non « une défense linéaire quelconque existe » à « aucune n’existe ».

---

## Sur la proposition B

### (a) Défauts de méthode

**VÉRIFIÉ — NashConv est incorrectement défini.** Pour le gain de détection \(U\), maximisé par le défenseur et minimisé par l’adversaire :

\[
\operatorname{NashConv}(p,q)
=\sup_m U(m,q)-\inf_\theta U(p,\theta).
\]

V est une recherche de **minimum**, non de maximum. La formule ultérieure de B,
\(V(B)+(1-\text{taux du meilleur moniteur})\), ne s’annule pas à l’équilibre.

**Contre-exemple illustratif, VÉRIFIÉ par substitution :** si toutes les lois adverses égalent la loi propre et tous les détecteurs ont exactement le taux \(\alpha\), tous les gains valent \(\alpha\). NashConv vaut zéro ; cette formule vaut un.

**VÉRIFIÉ — « grille exhaustive » n’est pas établi.** Un ensemble fini dans l’espace continu des paramètres ne devient pas exhaustif par augmentation de son effectif. Il faut un rayon de couverture et un contrôle de variation du gain. La projection des points sur la contrainte peut en outre produire des doublons et une couverture très inégale.

**VÉRIFIÉ — autres erreurs d’identification.**

- Uniformiser les **occurrences** historiques reproduit leurs fréquences, même si une même stratégie apparaît plusieurs fois.
- Le gain d’un détecteur linéaire seuillé n’est pas linéaire dans ses poids.
- Une valeur à horizon fini ne réfute pas une convergence asymptotique sans borne de vitesse applicable.
- Le déficit « valeur restreinte moins V » ne couvre que la réponse adverse ; il ne suffit pas à certifier un équilibre complet.
- Une baisse de ce déficit ne montre pas que l’infériorité de B face à une autre classe venait de l’horizon.

**HYPOTHÈSE — confusion dans la régularisation.** La pénalité sur les poids mélange stabilité fonctionnelle, choix de coordonnées et choix d’échelle. Sélectionner ensuite le meilleur \(\lambda\) sur les mêmes instances ajoute un biais de sélection.

### (b) Conditions mesurables de perte de puissance ou de non-jugement

| Mesure | Condition |
|---|---|
| Minimum sur une grille | **HYPOTHÈSE :** si le gain est \(L\)-Lipschitz et la grille couvre le domaine à rayon \(h\), l’erreur de discrétisation est bornée par \(Lh\). Sans \(L\) ou \(h\) contrôlé, aucune certification ; si \(Lh\) dépasse la marge, le contraste n’est pas jugeable à cette marge. |
| NashConv approché | **VÉRIFIÉ — inégalité :** une maximisation sur des candidats sous-estime le supremum ; une minimisation sur des candidats surestime l’infimum. Leur différence peut donc masquer une exploitabilité réelle. |
| Seuils à horizon fini | **VÉRIFIÉ — identifiabilité :** deux lois de processus identiques jusqu’à l’horizon observé peuvent avoir des limites différentes. Aucune statistique de ce préfixe ne tranche leurs comportements asymptotiques. |
| « Cycle supprimé » par régularisation | **HYPOTHÈSE :** si la loi de \(U(m_t,\theta_t)\) reste stationnaire alors que les décisions changent, \(I_1\) perd toute puissance sur la stabilité fonctionnelle. Un détecteur presque figé produit aussi peu de variation sans gain de sécurité. |
| Pureté en augmentant \(T\) | **HYPOTHÈSE :** lorsque l’incertitude des coefficients de \(G\) dépasse l’écart entre stratégie pure et mixte, la fréquence de pureté dépend davantage du bruit et des tolérances numériques que du jeu populationnel. |

### (c) Contrôles négatifs indispensables

**VÉRIFIÉ — contrôle constant mal spécifié.** Dans le code, un score constant échoue à la garde de variance ; avec un seuil égal au score et une comparaison stricte, il ne détecterait rien. Il ne produit pas automatiquement un taux \(\alpha\).

**HYPOTHÈSE — contrôles requis :**

- Détecteur aléatoire indépendant des observations, de loi Bernoulli\((\alpha)\), pour une véritable référence sans discrimination.
- Jeu à gain constant pour invalider immédiatement une formule incorrecte de NashConv.
- Minimum analytique connu pour mesurer l’erreur de la grille.
- Défense figée et réponses répétées indépendantes pour mesurer les retours induits par l’estimateur.
- Régularisation nulle et reparamétrisations fonctionnellement identiques.
- Évaluation indépendante du \(\lambda\) choisi.

Le bras D n’est pas un contrôle négatif établi de « non-cycle » : l’utiliser ainsi incorporerait la conclusion recherchée dans la validation.

---

## Sur la proposition C

### (a) Défauts de méthode

**VÉRIFIÉ — confusion entre moyenne nulle et absence de détection linéaire.** Une moyenne d’attaque nulle ne supprime pas les différences de queues.

**Contre-exemple illustratif, VÉRIFIÉ par calcul :** avec
\(P_0=\mathcal N(0,1)\) et
\(Q=\{\mathcal N(a,1)+\mathcal N(-a,1)\}/2\),
la moyenne de Q est nulle, mais le détecteur \(x>z_{1-\alpha}\) détecte avec probabilité

\[
\frac{\bar\Phi(z_{1-\alpha}-a)+\bar\Phi(z_{1-\alpha}+a)}2.
\]

Cette probabilité tend vers une moitié quand \(a\) augmente. La seule géométrie des moyennes ne justifie donc pas le plafond annoncé.

**VÉRIFIÉ — comparaison mal attribuée.** C1 emploie les moniteurs de **B**, pas ceux de A. Son écart avec A ne prouve pas l’effet de moyenner la trajectoire de A.

**VÉRIFIÉ — garanties de capacité non démontrées.** Compter les unités et les colonnes de G ne garantit ni domination d’une ligne ni nécessité de mélanger. Chaque colonne représente une loi, non une direction unique. La condition \(m<K\,T\) n’implique pas la borne de support invoquée.

**VÉRIFIÉ — direction de borne inversée.** Le minimum atteint par une recherche locale est supérieur ou égal à l’infimum populationnel. Hors erreur d’échantillonnage, il donne une borne **supérieure** de la sécurité garantie de la défense fixée, contrairement à la « borne basse » annoncée.

**HYPOTHÈSE — causalité non identifiée.** L’agrégation pondérée change simultanément le support, la fonction de score et le seuil recalibré. Son éventuel avantage ne peut être attribué uniquement à une « perte de Jensen ». Il n’existe pas ici d’ordre universel entre mixture de décisions et agrégation recalibrée.

**VÉRIFIÉ — validations circulaires.** Qualifier A de trajectoire cyclique forcée et D de trajectoire monotone, puis les utiliser pour valider l’instrument qui doit établir ces propriétés, est circulaire. Une moyenne simulée correcte d’\(I_3\) ne démontre pas le taux de fausses alertes d’un test.

### (b) Conditions mesurables de perte de puissance ou de non-jugement

| Mesure | Condition |
|---|---|
| \(D_{\rm train}\) et saturation | **VÉRIFIÉ — identifiabilité :** une faible détection du moniteur obtenu est compatible avec une classe insuffisante **ou** un oracle défaillant. Sans majorant du supremum de la classe, ces explications restent indistinguables. |
| Critère basé sur les moyennes | **VÉRIFIÉ :** si deux lois ont mêmes moyennes mais queues différentes, les moyennes ne suffisent pas à déterminer U ; le contre-exemple ci-dessus l’établit. |
| Support actif de B′ | **HYPOTHÈSE :** si un poids populationnel est proche du seuil de support, son inclusion devient instable. Choisir le support et estimer son bénéfice sur les mêmes gains bruités introduit une sélection adaptative. |
| Avantage de l’agrégation | **VÉRIFIÉ — définition :** il dépend de la loi jointe des scores sous \(P_0\) et \(Q_\theta\), pas seulement des taux marginaux. Une forte corrélation peut annuler le gain attendu de plusieurs moniteurs. |
| Tests de sous-capacité | **HYPOTHÈSE :** si plusieurs lois adverses partagent la même région de rejet favorable, augmenter leur nombre ne crée pas de besoin de mixture ; le comptage des lois perd alors son pouvoir discriminant. |
| Matrice H et scores historiques | **HYPOTHÈSE :** réutiliser les mêmes évaluations pour sélectionner les moniteurs puis mesurer leur avantage rend les gains historiques optimistes. Un échantillon frais de chaque loi est nécessaire. |

### (c) Contrôles négatifs indispensables

**HYPOTHÈSE — contrôles requis :**

- Lois symétriques à moyenne nulle mais queues séparables, pour invalider une saturation déduite des seuls premiers moments.
- Plusieurs lois adverses toutes bien détectées par le même moniteur, malgré un nombre de lois supérieur au nombre d’unités.
- Moniteurs dupliqués et moniteurs fortement corrélés pour éprouver l’explication par dilution.
- Support choisi sur des données distinctes de celles évaluant le gain.
- Lois de trajectoires sans périodicité mais avec répulsion temporelle.

**VÉRIFIÉ — contrôles au bit irréalisables tels qu’écrits.** Le code refuse `unites_Bp < 2`, et les codes de bras déterminent des graines distinctes. Les identités \(B'_1=B\), \(D_1=A\) nécessitent une adaptation explicite de la garde et du couplage aléatoire. Pour un support réduit à un moniteur, vérifier d’abord l’égalité des **décisions sur les mêmes observations** ; des recherches adverses utilisant d’autres graines ne garantissent pas des V identiques au bit.

---

## Sur la proposition D

### (a) Défauts de méthode

**VÉRIFIÉ — risque de convergence vraie par construction.** Résoudre un équilibre de la matrice courante puis mesurer NashConv sur cette même matrice donne un écart nul, à tolérance numérique près. Cela valide le solveur, pas la fermeture du jeu vis-à-vis de stratégies absentes.

**VÉRIFIÉ — E1 ne teste pas « aucune mixture ».** La mixture uniforme et la mixture optimale sur G n’épuisent pas les mixtures optimales contre les lois hors G. Leur échec ne réfute pas l’existence d’une autre mixture utile.

**HYPOTHÈSE — factoriel E2 insuffisamment isolé.** Passer à une réponse tabulaire exacte change aussi le domaine des stratégies admissibles. Pour identifier l’erreur d’oracle, les réponses exacte et approchée doivent optimiser **la même fonction sur le même domaine**. Les hypothèses « asymétrie principale » et « approximation suffisante » peuvent également être vraies ensemble.

**VÉRIFIÉ — E3 confond mélange disponible et nécessaire.** La minimisation du poids maximal peut répartir la masse entre moniteurs fonctionnellement identiques. Elle exerce le tirage informatique sans exercer une diversification utile.

**VÉRIFIÉ — E4 : absence de preuve n’est pas réfutation.** Un intervalle compatible avec l’absence d’effet peut aussi contenir l’effet revendiqué. Seule une borne supérieure excluant cet effet réfute la revendication quantitative.

### (b) Conditions mesurables de perte de puissance ou de non-jugement

**VÉRIFIÉ — certification restreinte réparable.** Posons

\[
v(G)=\max_p\min_jp^\top G_{\cdot j},
\qquad
d(G)=\max_i\min_jG_{ij}.
\]

L’écart \(v(G)-d(G)>0\) exclut une stratégie pure optimale **dans G**. Si
\(\|\widehat G-G\|_\infty\le\eta\), l’erreur sur cet écart est au plus \(2\eta\). Lorsque l’écart estimé ne dépasse pas cette incertitude, la nécessité de mélanger n’est pas certifiée. Elle reste, même certifiée, limitée au jeu restreint.

**HYPOTHÈSE — autres conditions critiques :**

- **Distance fonctionnelle :** sous une loi de référence R, deux moniteurs ayant mêmes décisions R-presque sûrement ont distance nulle, même s’ils diffèrent fortement sous certaines \(Q_\theta\). Si R ne couvre pas ces régions, l’instrument est aveugle.
- **Sélection des tâches intérieures :** si l’inclusion dépend de \(\widehat G\), l’estimande devient conditionnelle à cette sélection. Réutiliser \(\widehat G\) pour confirmer l’avantage favorise les écarts dus au bruit.
- **Comparaisons temporelles :** si les distributions évaluées changent avec le tour, une différence de performance confond changement du moniteur et changement de loi.
- **Transfert :** si train et test partagent une variable latente de source Z, une partition par observations peut conserver la dépendance. L’incertitude calculée comme si les observations étaient indépendantes devient trop faible.

### (c) Contrôles négatifs indispensables

**HYPOTHÈSE — contrôles requis :**

- Matrice à lignes optimales identiques : mixture diffuse, mais avantage mixte nul.
- Profil à équilibre restreint exact auquel on ajoute une colonne tenue à l’écart exploitable : NashConv restreint doit rester distingué du diagnostic externe.
- Défense figée médiocre **et** défense figée à équilibre connu : la stabilité seule ne doit ni suffire ni être systématiquement pénalisée.
- Moniteurs identiques R-presque sûrement mais différents sous une loi tenue : contrôle de couverture de la distance fonctionnelle.
- Sélection des tâches sur un lot, évaluation sur un autre ; publication séparée des performances conditionnelles et non conditionnelles.
- Permutations d’étiquettes respectant les groupes de dépendance, plutôt que permutations individuelles.

**HYPOTHÈSE — duel réparable.** Pour E3, opposer un avantage mixte populationnel restreint supérieur à une marge gelée à son complément. Pour E4, opposer un gain transféré supérieur à une marge au complément, sans assimiler un résultat imprécis à une réfutation.

FIN-DE-CELLULE