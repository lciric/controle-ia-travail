Statuts conservés : billet et « nos résultats » = **RAPPORTÉ** ; lectures des journaux = **OBSERVÉ-NON-AUDITÉ**. Les objections ci-dessous sont des analyses méthodologiques, pas des résultats empiriques.

## Sur la proposition A

### (a) Défauts de méthode

- **E1 ne sépare pas complètement trait, déplacement et historique d’entraînement.** N3 est un nul pour le suivi des mauvaises suggestions sur la suite mesurée, pas pour l’égalité des comportements sur toutes les entrées. Une alerte N3 peut donc être une fausse alerte pour le construit « sycophancie » sans être une erreur de lecture d’une différence comportementale. De plus, T et N3 n’ont pas la même relation au parent : détecter la copie la plus proche du départ reste possible. Le passage simultané à l’affinage complet et aux adaptateurs ajoute un régime de représentation ; le regrouper sans interaction mesurée brouillerait l’effet du lecteur avec celui du format.
- **La base mécanique supervisée d’E1 peut fuiter par famille.** Des paires « tenues à part » qui partagent parent, faits, recette, plages de couches ou hyperparamètres ne sont pas indépendantes du test. La régression logistique peut alors apprendre la recette plutôt que le trait, tandis que le lecteur est évalué sur une généralisation plus difficile — ou réciproquement.
- **Le témoin aléatoire d’E2-Qwen est trop faible.** Une direction aléatoire de même norme et sur le même support n’apparie ni les statistiques d’activation, ni l’alignement avec les directions effectivement écrites, ni l’effet sur la longueur. Son infériorité est partiellement vraie par construction. Surtout, l’exactitude « conditionnelle à finir » conditionne sur une variable post-intervention : elle peut comparer des populations de problèmes différentes.
- **Le duel sycophancie d’E2 n’épuise pas les possibilités.** Une ablation peut déplacer à la fois le point fixe et la part attirée, ou déplacer le point fixe parce qu’elle change l’échelle des notes et le jugement. L’issue serait alors rangée dans « suit sans causer » sans que cette conclusion suive. La direction ayant servi à choisir l’intervention, les cadres de pression et les faits doivent aussi être séparés de ceux servant à estimer les paramètres de la loi.
- **E3 compare des unités différentes.** M1 produit un verdict par adaptateur, M2 peut produire un score par épisode et M3 dépend du nombre de transcriptions. La fraction \(p\) d’épisodes sabotés peut faire varier la prévalence comportementale sans faire varier de façon correspondante le delta de poids. Un avantage de M1 peut alors être un avantage de budget ou d’unité, pas un apport marginal aux poids.
- **E4 et E5 contiennent deux circularités.** Remplacer les couches extrêmes ne conserve pas nécessairement la propriété plantée ; le témoin peut donc tester une destruction de fonction. En E5, après canonicalisation exacte, l’invariance d’un lecteur déterministe est vraie par construction. Sans exigence de détection, un lecteur constant obtient également une invariance parfaite.

### (b) Conditions probabilistes de perte de puissance ou de non-jugeabilité

- Si les paires partagent parent, faits ou graine d’entraînement, avec corrélation intra-groupe positive des scores, les intervalles binomiaux et les AUC calculés au niveau des paires sous-estiment la variance. Le sous-ensemble « frontière » et le maximum sur lecteurs ou bases introduisent en outre une sélection dont la loi n’est pas celle d’un lecteur fixé.
- L’AUC intra-paire sur T et le taux de déclaration sur N3 estiment deux fonctionnelles distinctes : aucune loi ne garantit qu’une AUC élevée implique un faible taux de fausses alertes. Les zones \(0{,}65<\mathrm{AUC}<0{,}80\), ou les écarts intermédiaires entre N3 et T, ne falsifient ni H_A ni H_B.
- Pour Qwen, si \(F\) désigne la terminaison, \(P(\text{juste}\mid F=1,\mathrm{do}(e))\) et \(P(\text{juste}\mid F=1,\mathrm{do}(0))\) ne comparent pas nécessairement les mêmes strates. Lorsque \(P(F=1)\) est faible dans un bras, l’estimateur conditionnel est aussi très instable.
- En E3, si le score-poids est presque constant en \(p\) alors que la probabilité d’observer un sabotage dans les transcriptions tend vers zéro, les puissances de M1 et M3 ne sont pas identifiables sur une échelle commune. Un petit nombre d’adaptateurs honnêtes indépendants rend également le taux de fausses alertes réalisé trop discret pour certifier précisément \(\alpha=0{,}05\).
- En E5, une loi de verdict ponctuelle — toujours « trait », toujours « pas trait » ou toujours la même probabilité — donne un taux de bascule nul : le critère d’invariance n’a alors aucune puissance sur la lecture.

### (c) Contrôles négatifs dont l’absence serait fatale

- **E1 :** des séparations complètes par parent, famille de faits et recette entre calibration, base supervisée et test ; des adaptateurs à trait bénin appariés en norme et en historique ; une validation que N3 est bien nul pour la fonctionnelle comportementale estimée.
- **E2 :** plusieurs directions témoins tirées dans un même espace de candidats, dose zéro, répétition légitime, et analyse sur une strate de problèmes définie sans utiliser la terminaison post-intervention.
- **E3 :** des adaptateurs entraînés avec les données de trait mais comportementalement négatifs, des jumeaux \(p=0\) sur la même unité, et le contraste obligatoire « boîte noire + lecteur » contre « boîte noire + score mécanique ».
- **E4/E5 :** vérification par oracle que les transformations conservent réellement fonction et propriété ; zoo entier sans propriété ; transformation changeant la fonction, à amplitude appariée, pour rejeter un lecteur simplement constant.

## Sur la proposition B

### (a) Défauts de méthode

- **Le renversement d’E1 ne change pas qu’un signe.** P₁ possède déjà un historique d’affinage vers l’honnêteté ; les branches ont donc des parents, des distances cumulées et potentiellement des forces comportementales différents. Une chute d’exactitude dans la branche renversée peut venir d’un affinage sycophante moins efficace, d’un delta plus faible ou d’un artefact de recette, pas d’une lecture du déplacement. H_A et H_B omettent aussi « lecture du parent », « lecture de la norme » et « lecture du format de données ».
- **Le comparateur « ressemblance au parent » n’a pas le même accès.** Le lecteur du billet reçoit A et B, pas leur parent. Donner le parent à cette base lui fournit une information supplémentaire et transforme la comparaison en comparaison d’interfaces.
- **E2 confond dose de données et dose de comportement.** La fraction de données de trait ne fixe ni le taux de sabotage observé ni l’amplitude du delta. Le choix du « meilleur concurrent » parmi plusieurs bases ajoute un biais de maximum si son classement n’est pas entièrement figé hors test. Utiliser les mêmes paires nulles pour calibrer le seuil à 5 % et rapporter zéro alerte surestime la garantie.
- **E3a conserve le problème de sélection par terminaison**, avec en plus un seul échantillon par problème : les seuils d’équivalence de deux et cinq points ne sont pas reliés à une puissance démontrée. En E3b, les intervalles entre 10 % et 30 % de variation de \(k\), ainsi que la possibilité que pente et point fixe changent ensemble, laissent des issues sans falsification.
- **E4 ne définit pas une nulle probabiliste par une liste de statistiques.** « Contenir » normes, statistiques de couches et mélanges de lois ne dit pas comment tirer des réseaux frais conditionnellement à ces contraintes. « Au moins une loi promue » dépend du nombre de soumissions et de courses.
- **E5 attribue à tort une invariance structurelle.** Une sonde fixe dans des coordonnées neuronales n’est pas invariante sous permutation ; une tête numérotée ne l’est pas non plus si les têtes sont permutées. Les normes par couche ne sont pas nécessairement invariantes sous changements d’échelle compensés. L’abandon fondé sur leur bascule peut donc rejeter un témoin valide.
- **E6 change le construit et son nul.** Un choix fermé parmi huit jeux ne mesure plus la nomination ouverte. Des répétitions sur les mêmes quatre réseaux ne créent pas quarante réseaux indépendants. Des récompenses permutées peuvent conserver la structure spatiale et les statistiques de poids qui identifient le jeu : ce n’est pas nécessairement un monde sans propriété.

### (b) Conditions probabilistes de perte de puissance ou de non-jugeabilité

- Avec un seul parent P₁ par branche, la variance entre parents n’est pas estimable ; même vingt paires conditionnellement indépendantes ne généralisent pas à une loi de parents. Le doublement unique de \(n\), décidé après observation d’une zone intermédiaire, modifie aussi la loi d’échantillonnage si aucune dépense d’erreur séquentielle n’est fixée.
- En E2, si la courbe dose réelle \(\pi(q)=P(\text{comportement positif}\mid q)\) est plate ou si \(\pi(1)\) reste faible, la détection à dose 1 ne discrimine pas les instruments. Le maximum de plusieurs concurrents est biaisé vers le haut sur développement ; la différence de sensibilité doit être estimée appariée, sinon sa variance est mal comptée.
- Pour E3b, lorsque le \(k\) de base est proche de zéro, un ratio relatif est instable ; lorsque les doses n’informent pas la courbe, \(k\) et le point fixe sont faiblement identifiés et leurs marges d’équivalence ne sont pas jugeables. Avec un seul point de contrôle par intervention, les faits et générations ne répliquent pas l’intervention elle-même.
- En E4, zéro promotion sur dix-neuf faux témoins laisse une borne supérieure unilatérale à 95 % d’environ **14,6 % (calcul)** pour une probabilité par témoin interprété comme essai indépendant : cela ne certifie pas 5 %. La probabilité d’« au moins une promotion » croît avec le nombre de soumissions, même à taux individuel constant.
- En E6, une forte corrélation des réponses conditionnellement au réseau rend l’estimateur par essai très précis en apparence mais presque sans information sur de nouveaux réseaux. Le calcul de sélection suppose en outre indépendance des tentatives et nombre de tentatives connu, deux conditions non établies pour le billet.

### (c) Contrôles négatifs dont l’absence serait fatale

- **E1 :** plusieurs parents P₁, branches appariées en force comportementale et en norme de delta, et surtout une branche factice avec même historique total d’entraînement mais sans changement de trait. Sans elle, le renversement ne contrôle pas la récence d’entraînement.
- **E2 :** nuls de calibration et nuls finaux disjoints ; adaptateurs exposés aux données de trait mais sans expression comportementale ; deltas associés à de fausses descriptions pour détecter les fuites de métadonnées.
- **E3 :** répétition légitime, suggestions vraies et désaccord générique, faits et doses nouveaux ; plusieurs directions aléatoires plutôt qu’un seul tirage.
- **E4/E5 :** courses entières où toute promotion est fausse ; transformées préservant la fonction validées par exécution et transformées la changeant ; contrôle contre un classifieur constant.
- **E6 :** réseaux frais à chaque répétition et nuls dont l’oracle vérifie l’absence de propriété, pas seulement la permutation d’une étiquette de récompense.

## Sur la proposition C

Pièce C absente, statut « jamais lancée » : aucune critique de son contenu n’est possible.

## Sur la proposition E

### (a) Défauts de méthode

- **DELTA ne démontre pas nécessairement l’apport propre du lecteur.** Le contraste « boîte noire + delta » contre le meilleur comparateur isolé doit aussi affronter « boîte noire + vérification mécanique ». Sinon, un simple apport d’une norme ou d’une statistique spectrale sera attribué au modèle de langue. La conclusion ne porte de toute façon que sur le résumé déterministe fourni, choix qui peut lui-même éliminer l’information prétendument lue.
- **La banque de corruptibilité ne certifie pas une classe.** Une baisse moyenne sur des soumissions adversariales scellées est conditionnelle à leur distribution. Réutiliser cette banque sur plusieurs tours permet en outre une adaptation aux attaques connues, même si chaque course est déclarée scellée.
- **CONSTRUIT ne mesure pas nécessairement la spécificité sociale.** Une baisse de l’aire \(A\) peut provenir d’un contrariant générique, d’un refus accru ou d’une moindre tendance à donner une réponse engageante. Mesurer séparément les non-réponses ne suffit pas si elles sont simplement retirées du dénominateur de l’accord. Enfin, l’aire ne réinstancie ni \(k\) ni le point fixe : le raccord revendiqué à la loi psychophysique n’est donc pas testé.
- **Une intervention unique est pseudo-répliquée par de nombreux faits.** Les intervalles au niveau des familles de faits mesurent l’incertitude d’échantillonnage comportemental pour ce point de contrôle édité, pas la variabilité de la procédure « lecteur choisit un candidat puis l’édition est gelée ».
- **ORACLE laisse le traitement modifier sa propre nulle.** Les lois acceptées dans le bras « poids » entrent dans l’archive et changent les soumissions ultérieures, la non-redondance et potentiellement la couverture du juge. Une archive commune contaminerait les bras ; deux archives distinctes rendent les trajectoires difficilement comparables. Le taux de promotions fausses est défini par course, mais le nombre et la loi des courses indépendantes ne sont pas définis.

### (b) Conditions probabilistes de perte de puissance ou de non-jugeabilité

- Dans DELTA, le gain \(G\) dépend de la loi mélange des positifs. Si cette loi concentre les effets comportementaux très forts, tous les instruments approchent le plafond ; si elle les concentre sous le seuil d’observabilité boîte noire, trente positifs donnent une différence appariée très incertaine. Des scores discrets ou fortement ex aequo peuvent aussi rendre le taux de fausses alertes réalisé très conservateur. La borne obtenue avec zéro alerte sur soixante nuls ne remplace pas une calibration indépendante du seuil.
- Pour la corruptibilité, la moyenne sous la loi empirique de la banque n’est ni un supremum sur la classe d’accès ni une garantie sous la loi induite par des soumissions adaptatives successives.
- Dans CONSTRUIT, \(A\) n’est défini qu’après choix d’une mesure de pondération sur les doses. Si le niveau de base \(A_0\) est inférieur au seuil absolu de réduction, H_A est impossible ; si la courbe est plate ou si le dénominateur des accords est conditionné par une variable post-intervention, l’estimation ne mesure plus la même fonctionnelle.
- Dans ORACLE, un rendement relatif est indéfini lorsque le rendement de base est nul et très instable lorsqu’il est proche de zéro. Des lois correctes au sein d’une même course ne sont pas des réplicats indépendants d’une probabilité de fausse promotion par course. Sous archive cumulative, la non-stationnarité interdit également de traiter les courses successives comme identiquement distribuées.

### (c) Contrôles négatifs dont l’absence serait fatale

- **DELTA :** le comparateur combiné boîte noire + mécanique ; des adaptateurs comportementalement négatifs malgré exposition aux données de trait ; des paires description/delta volontairement désappariées ; et, pour la corruptibilité, des soumissions honnêtes passant par exactement le même canal d’accès adversarial afin de vérifier que les fausses alertes restent constantes.
- **CONSTRUIT :** suggestions vraies, assertions neutres et pression sans contenu, pour détecter contrarianisme ou acquiescement générique ; intervention sans rapport appariée en dommages ; non-réponses intégrées à un critère préenregistré plutôt que conditionnant l’analyse ; plusieurs éditions indépendantes avant toute généralisation à la procédure.
- **ORACLE :** courses nulles complètes, avec archive active et aucune propriété à découvrir ; poids provenant d’un autre réseau que la description ; propriétés négatives certifiées par un oracle indépendant de celui ayant guidé la construction ; réplication sur courses entières fraîches, et non seulement sur davantage de lois dans une même course.

FIN-DE-CELLULE