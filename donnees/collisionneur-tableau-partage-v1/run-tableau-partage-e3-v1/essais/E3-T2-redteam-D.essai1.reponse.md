## Sur la proposition A

### (a) Défauts de méthode

- **Le préfiltrage des doublons peut exclure précisément ses échecs.** Les lecteurs ne reçoivent que les paires candidates retenues par recouvrement de trigrammes. Le rappel calculé sur ces candidates ne mesure donc pas le rappel sur toutes les paires. Les réécritures plantées ne lèvent ce biais que si leur famille est indépendante de celle ayant servi à régler le préfiltre. Ensuite, une fausse paire positive peut fusionner plusieurs composantes et une fausse négative peut en scinder une : le nombre d’idées n’a pas la variance d’un simple compte de paires.
- **Idées distinctes et diversité lexicale ne sont pas deux mesures indépendantes de la convergence.** Une baisse du recouvrement peut accompagner une reformulation sans augmenter le nombre de composantes ; inversement, une normalisation de surface peut réduire la distance sans réduire les idées. La distance entre composantes ne devient pas sémantique parce qu’elle est calculée après regroupement.
- **La part du prolifique est partiellement vraie par construction.** Le quota de lecture plafonne mécaniquement la part servie par auteur : la retrouver sous le seuil ne valide pas l’absence d’influence. La comparaison de cette part à la condition sans tableau est, elle, indéfinie pour les entrées du tableau. Enfin, une composante réunissant des fiches de plusieurs proposeurs n’a pas d’auteur unique : sans règle d’attribution fractionnaire gelée, la part des idées et l’entropie entre proposeurs sont non jugeables.
- **La chaîne inerte mesure une propagation, pas toute la prise.** L’égalité entre entrées plantées et entrées honnêtes, ou l’absence de chaîne chez le juge, laisse ouverte une prise sans traceur. Pour la séparation, « la même fiche » avec et sans passage par le tableau n’est pas une unité appariée si le passage intervient avant sa production : les deux conditions diffèrent alors par toute la génération, pas seulement par une fuite insérée.
- **Rien ne sépare explicitement réglage et évaluation.** Les mêmes familles de paires plantées peuvent servir à choisir les seuils de préfiltrage, de recouvrement et de garde, puis à annoncer leurs performances. Les mêmes témoins servent aussi à vérifier l’étalonnage et à conclure à l’équivalence entre conditions. Sans cas et témoins de confirmation gelés, les seuils illustratifs sont optimistes.
- **Les duels ne sont pas tous exhaustifs.** Au duel C contre B, une baisse du nombre d’idées ou une prise positive peut falsifier H_A sans réaliser H_B, qui porte seulement sur une chute de diversité. Le rééchantillonnage par proposeur est également incohérent avec l’unité déclarée case × conception : il faut conserver l’appariement des cases et traiter séparément les dépendances texte, case et proposeur.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **Doublons.** Lorsque leur prévalence approche zéro ou un, κ peut chuter malgré un accord brut élevé ; le rappel ou le taux de fausses alertes devient alors presque sans réplications positives ou négatives. Sous erreurs corrélées au sein d’un proposeur, le nombre effectif de paires est très inférieur au nombre nominal, et les composantes deviennent instables.
- **Convergence et coût.** Si les longueurs, les taux de validation ou les budgets de génération diffèrent entre conceptions, les distributions de recouvrement et les ratios idées/dépense changent sans changement équivalent d’idées. Avec peu de cases ou des ratios à queue lourde, les intervalles et effets aléatoires annoncés ne garantissent pas la puissance des seuils illustratifs.
- **Garde et séparation.** Zéro occurrence sur un petit nombre de plantations n’implique pas une probabilité nulle ; il faut rapporter l’intervalle binomial ou le bornage par grappes. Si la distribution des effets est largement disjointe de celle du traceur, la sensibilité de la prise est nulle par construction. Le recouvrement perd aussi sa calibration lorsque la longueur des fiches ou la part due à la question commune varie.
- **Témoins et rôles.** Près d’un plancher ou d’un plafond de reconnaissance, l’écart admis n’a presque aucune puissance. Des témoins répétés et regroupés dans peu de cases ne fournissent pas des observations indépendantes. Pour le rôle, des classes déséquilibrées, une validation croisée fuyant entre fiches d’un même proposeur ou peu de proposeurs rendent le seuil « hasard plus marge » non probant.

### (c) Contrôles négatifs indispensables

- Un **échantillon aléatoire de paires non préfiltrées**, avec des non-doublons certifiés indépendamment ; des paires venant d’autres cases ne sont pas nécessairement des non-doublons.
- Un **tableau placebo apparié en taille, forme et coût de lecture**, sans partage inter-proposeurs, pour isoler l’effet du partage de celui de l’allongement du contexte. La condition sans tableau seule ne sépare pas ces deux effets.
- Une **permutation des étiquettes de rôle** dans toute la procédure de prédiction, avec séparation par case et par proposeur. S’y ajoutent, sans être des contrôles négatifs, deux contrôles positifs faute desquels les zéros sont vides : insertion connue dans le flux destiné au juge avant la barrière, et famille de plantations de confirmation inédite.

## Sur la proposition B

### (a) Défauts de méthode

- **Le “tableau complet” évalué n’est plus en lecture et écriture libres.** Gabarit fermé, types fermés et bornes le rapprochent d’une conception intermédiaire. Les duels ne distinguent donc pas les effets respectifs de la quantité lue, de la liberté d’écriture et du surcroît de contexte.
- **« Poids : évité » ne suit pas de la borne mécanique.** Celle-ci borne une part d’entrées, non la distribution des idées attribuées ni leur dépendance au texte servi. Le tirage au sort de l’ordre n’est pas un contrôle négatif : il peut modifier les effets de position sans créer une condition d’influence nulle.
- **La garde est circulaire.** La formulation donnée semble confondre l’instruction plantée, qui doit être écrite par un tiers, et la chaîne inerte, qui n’est que son traceur. Si seule la chaîne est plantée, l’expérience mesure sa propagation et non la garde. Détecter exactement une chaîne unique alors qu’elle n’a pas été plantée donne en outre des fausses alertes presque trivialement nulles ; cela ne mesure ni les refus d’entrées honnêtes ni les fautes du filtre.
- **La qualité sur fiches promues est post-traitement.** Si les conceptions changent la promotion, les médianes portent sur des populations différentes. L’étalonnage sur témoins ne répare pas cette sélection. La diversité cosinus reste, elle, subordonnée à un plongement dont la stabilité sous changement de longueur et de forme n’est pas mesurée.
- **Le duel des rôles se contredit.** H_A compare rôles et absence de rôle, mais une supériorité des étiquettes sans consigne suffit à falsifier H_A même lorsque le gain annoncé sur l’absence de rôle est réalisé. Cette condition doit entrer dans H_A elle-même. Par ailleurs, aucun duel direct C contre B ne falsifie la préférence finale pour C, et les mesures de prise propres à C ne sont pas un critère du duel C contre A.
- **Les comptes de code ne sont pas des unités reproductibles.** La liste ne fixe ni granularité, ni tests, ni dispositifs de plantation et de scellement ; les totaux annoncés ne sont donc pas comparables sans inventaire gelé.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **Prolificité.** Lorsque les quotas laissent presque aucune variance à la part d’entrée, cette mesure ne peut pas détecter d’effet. Si les composantes sont fréquemment multi-auteurs, la fraction attribuée à un proposeur dépend entièrement d’une convention non fournie.
- **Garde.** Avec peu de plantations et une prise de base proche de zéro, ni la supériorité sur la base ni une prise nulle ne sont démontrables. Si les plantations diffèrent des entrées honnêtes par leur longueur ou leur forme, détection et fausses alertes mesurent ce confondant. Le taux conditionnel « si prise positive » est inestimable lorsque aucun cas positif n’est observé.
- **Diversité et idées.** Si le plongement est invariant à des regroupements reconnus par les lecteurs, ou sensible principalement à la longueur, ses distances ne soutiennent pas l’estimand. Près des prévalences extrêmes de doublons, κ et les composantes perdent à nouveau leur stabilité.
- **Témoins, duels et rôles.** Quelques témoins communs, corrélés par case et par configuration de juge, ne permettent pas une équivalence étroite, surtout près des taux extrêmes. Une assignation non permutée des rôles confond rôle et proposeur ; quelques grappes ne suffisent pas à estimer un effet aléatoire. La sélection de la recommandation et son évaluation sur les mêmes cases ajoutent un biais de sélection.

### (c) Contrôles négatifs indispensables

- Remplacer le contrôle d’ordre par un **partage placebo sans information croisée**, apparié en volume et en coût, tout en conservant le sans-tableau comme référence distincte.
- Pour la garde, utiliser **la même entrée honnête avec et sans élément planté**, des familles de réglage et de confirmation disjointes, et mesurer séparément refus honnêtes, détection amont et prise aval.
- Pour la prédiction du rôle, ajouter la **permutation des étiquettes** et une évaluation hors case et hors proposeur. Pour les coûts et les duels, un placebo de service de même taille est nécessaire afin que l’absence de gain ne soit pas confondue avec une simple différence de contexte.

## Sur la proposition C

### (a) Défauts de méthode

- **Le tableau complet est lui aussi redéfini.** Lecture limitée à des résumés tronqués et écriture retardée ne testent pas la lecture et l’écriture libres demandées. Surtout, les mesures du bloc 1 portent sur cette conception gardée ; elles ne démontrent pas la sécurité de C, dont les pistes courtes restent un canal à évaluer directement.
- **Le filtre destiné au juge laisse un chemin ouvert et son test est vrai par construction.** Le recouvrement n’est appliqué qu’aux entrées d’un autre proposeur : le chemin depuis une entrée du même proposeur échappe donc au filtre. Dans l’évaluation, l’extrait planté dépasse le seuil de longueur et porte toujours la chaîne. Le filtre est ainsi placé dans son domaine de détection garanti, tandis que la recherche exacte obtient également une réussite presque tautologique. Rien ne démontre alors l’avantage annoncé sur des traces sans chaîne.
- **La reconnaissabilité des témoins est remplacée par une moyenne de notes.** Des reconnaissances en sens opposés peuvent se compenser sans déplacer cette moyenne. L’écart de score mesure une dérive de notation, pas nécessairement la reconnaissance des témoins vrais et faux.
- **Le contrôle négatif du détecteur n’est pas un négatif connu.** Des fiches issues de textes différents ne garantissent pas des idées différentes ; exiger zéro doublon sur ce contrôle peut donc traiter de vraies détections comme des fautes. Les plantations à vocabulaire disjoint garantissent aussi une faiblesse de la base trigramme : elles ne suffisent pas à établir un gain général si elles servent également au réglage.
- **La qualité est deux fois déplacée.** Conditionner sur les fiches validées introduit une sélection différente par conception lorsque gardes et quarantaines varient. Si l’HYPOTHÈSE relative au fait 13 ne tient pas, remplacer l’équivalence de qualité par le taux de validation mécanique change l’estimand : ce taux n’est pas une qualité équivalente.
- **Diversité et rôles comportent des fuites supplémentaires.** Choisir la fiche la plus longue de chaque composante confond diversité, longueur et dépense. Pour le rôle, un découpage aléatoire des fiches entre entraînement et test laisserait partager proposeur, case et style ; sans permutation des étiquettes, le hasard estimé est lui-même biaisé.
- **Deux justifications dépassent les faits.** Le fait 4 vérifie le calcul d’un surplus, non l’affirmation que la proportion citée de fiches est simplement « en doublon ». Le principe du fait 8 est vérifié comme principe de code, non comme efficacité « éprouvée ». Le fait 10 ne fournit pas non plus de tarifs permettant de reproduire les coûts illustratifs.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **Détecteur.** Sous faible prévalence, les réécritures plantées peuvent dominer l’estimation du rappel tandis que les faux positifs naturels dominent le graphe. Le vote majoritaire ne répare pas un κ faible ; les erreurs corrélées par lecteur, case ou proposeur rendent le nombre de composantes très instable.
- **Garde et séparation.** Si la prise de base est nulle, la réduction à zéro n’a aucune puissance comparative. Si les traces hors chaîne ont une longueur inférieure au seuil ou un recouvrement redistribué, le taux de fuite réel reste positif pendant que le test planté affiche une détection parfaite. Les fiches honnêtes longues peuvent simultanément faire exploser les fausses alertes.
- **Témoins.** Avec des notes bornées, peu de témoins et une variance entre cases, l’écart moyen peut rester sous le seuil illustratif alors que la distribution de reconnaissance change. Une longueur ou une forme encore inégale entre témoins et fiches rend cet écart non interprétable comme effet du tableau.
- **Duels et rôles.** Les tests appariés sur peu de cases n’assurent ni la puissance des gains relatifs ni celle des équivalences multiples. Les ratios par dollar et le produit idées × diversité peuvent avoir des distributions très asymétriques ; agréger par case ne supprime pas cette instabilité. Les pistes vides ne contrôlent pas la longueur servie. Enfin, une permutation circulaire non équilibrée laisse une association résiduelle entre rôle, case et proposeur.

### (c) Contrôles négatifs indispensables

- Des **non-doublons certifiés**, appariés en longueur et en provenance, plus un audit de paires naturelles indépendant des plantations ; les paires entre textes différents ne suffisent pas.
- Pour la séparation, des fiches honnêtes présentant un **recouvrement fortuit avec la question commune**, et des cas de confirmation sans chaîne inerte. Sans ces derniers, la supériorité sur la recherche exacte reste vraie par construction.
- Pour C spécifiquement, un **placebo de pistes apparié en taille, forme, position et coût**, ainsi que des plantations propres à C ; les pistes vides et la sécurité mesurée sur B ne remplissent pas ces fonctions.
- Pour les rôles, permutation des étiquettes et découpage d’évaluation par case et proposeur. L’historique de la course 1 ne peut pas tenir lieu de contrôle contemporain, car les conditions et les témoins ne sont pas établis comme équivalents.

FIN-DE-CELLULE