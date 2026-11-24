**Proposition E — critique croisée de méthode**

**Statuts.** Les dispositifs attribués à chaque proposition sont **RAPPORTÉS** par sa pièce ; leur performance n’est pas un résultat de ce tour. Les scénarios de défaillance et les contrôles prescrits ci-dessous ont le statut **HYPOTHÈSE** de conception. Les identités données avec leurs conditions sont des déductions, pas des observations sur le banc. Les numéros de décision sont des repères ; aucun nouveau seuil numérique n’est proposé.

**Notation.** \(D\) indique un dommage effectif, \(S\) un signalement, \(X\) la part de l’objet de comparaison moins celle de l’objet testé, \(E\) le déclenchement de l’excès, \(U\) la borne de \(q\), et \(K\) le nombre de lois plantées. Pour les duels à marge \(\delta\), il faut opposer un paramètre à son complément exact, par exemple \(H_A:\theta\le\delta\) contre \(H_B:\theta>\delta\). Un intervalle entièrement d’un côté écarte l’hypothèse de l’autre côté au risque annoncé ; un intervalle traversant la frontière ne réfute ni l’une ni l’autre.

## Sur la proposition A

**(a) Défauts de méthode.** Le placebo par découpage de la référence ne reproduit pas nécessairement la variance du contraste entre mondes. Chercher le plus petit \(k(m)\) sur des paires nulles est pertinent, mais la borne attachée au seuil retenu doit rester valide après cette recherche. La vérité « par fabrication » teste d’abord la fidélité au générateur de passages. Surtout, dans E4, *préserver un classement* et *décroître avec le bruit* ne sont pas incompatibles : une baisse commune à toutes les strates peut réaliser les deux. E5 ne justifie pas que la frontière simulée soit le pire cas.

**(b) Conditions mesurables.**
- **D1–D2.** Si \(\operatorname{Var}(\widehat{\Delta B})\ne\operatorname{Var}(\widehat{\Delta B}_{placebo})\), le quantile placebo n’a pas le niveau annoncé. Si \(P(X\ge k/m\mid D,m)=P(X\ge k/m\mid\neg D,m)\), ce seuil respecte éventuellement le plafond sans discriminer.
- **D3.** Si \(P_{\rm cible}(s)>0=P_{\rm gabarits}(s)\) pour un type sémantique \(s\), sa sensibilité n’est pas estimable par E3. Une fidélité uniformément basse ne satisfait aucun des deux récits proposés.
- **D4.1–D4.2.** Si \(d_s\) est fixe et que le dommage vrai est défini comme \(d_sq_s\), sa couverture par \(d_sU_s\), pour dose positive, est exactement celle de \(q_s\) par \(U_s\) ; la corrélation de rang ne l’estime pas. Une simulation sur \(\Theta_g\) ne borne pas \(\sup_{\theta\notin\Theta_g}P_\theta(\text{au moins une erreur})\).
- **D5.** Si les fiches au seuil honnête et au rang \(K\) coïncident presque sûrement, leur contraste apparié est nul pour toute règle lisant les mêmes preuves. Cela ne mesure pas sa sensibilité aux omissions.

**(c) Contrôles négatifs indispensables.** Placebo de mondes reproduisant effectifs et appariements ; paires honnêtes nouvelles après sélection de \(k\) ; paraphrases intactes éditées par le tiers et jugées hors gabarits. Conserver l’oracle qui signale tout pour le classement, la procédure à niveaux fixes pour la couverture, et des fiches honnêtes de même cardinal pour le compteur.

## Sur la proposition B

**(a) Défauts de méthode.** Le duel sur la chute de A laisse de côté une hausse supérieure à la marge, pourtant compatible avec « pas de chute ». Le rapport signal/bruit de B peut augmenter avec l’effectif à effet pratique inchangé. Le seuil par quantile de B est discret : « au moins le quantile » n’équivaut pas à « au-dessus du quantile ». Basculer au repéreur sur une borne inférieure de rappel basse peut récompenser la seule imprécision. Enfin, les bras de D5 changent à la fois la composition et l’information révélée.

**(b) Conditions mesurables.**
- **D1–D2.** Si l’intervalle de \(\Delta A\) est entièrement au-dessus de \(+\delta\), les hypothèses de 1b ne classent pas cette issue. Si \(t_m=Q_{1-\alpha}(X\mid\neg D,m)\) et \(P(X>t_m)+P(X=t_m)>\alpha\) sous cette loi, le plafond est dépassé même avec le quantile de population.
- **D3.** Si les rappels du programme et du repéreur sont égaux et si l’intervalle de leur différence contient la marge de gain, le remplacement n’est pas justifié. La précision sur couples désappariés n’identifie pas la précision cible si leurs prévalences diffèrent.
- **D4.1–D4.2.** Si deux lois ont même distribution de \((X,E,U)\) mais des dommages réels différents, la couverture du dommage ne s’identifie pas à celle des manques observés. Si \(P(E)\) est faible, le nombre de répétitions conditionnelles effectives peut être insuffisant même avec une couverture marginale précise.
- **D5.** L’écart d’évasion peut être non nul avec un effet nul de révélation à tout \(K\), dès que \(P(\text{évasion}\mid K)\) varie et que les poids de \(K\) diffèrent entre bras.

**(c) Contrôles négatifs indispensables.** Valider le seuil, égalités comprises, sur de nouvelles paires nulles de même provenance que les paires finales. Vérifier humainement que les couples désappariés ne partagent effectivement aucun contrôle. Pour D5, donner au même script, sur les mêmes compositions tirées, soit une indication de cardinal permutée, soit aucune indication ; garder le bras honnête dans les deux conditions.

## Sur la proposition C

**(a) Défauts de méthode.** Le dossier ne tranche pas par son seul libellé si \(A-B\) est l’acceptation stricte. Le repéreur qui désigne le passage puis certifie son retrait sélectionne les dommages visibles *pour lui* ; son accord avant/après n’est pas une validation indépendante. Le contrôle par citation littérale teste un vrai porteur, pas une fausse désignation. Le diagnostic par lecteur en excès ne sépare pas un lecteur défaillant d’un contrôle effectivement absent chez l’honnête.

**(b) Conditions mesurables.**
- **D1–D2.** Si \(A=P(\mathrm{accepte})\), alors \(A-B\) n’est pas le paramètre visé dès que \(B>0\). Si la queue nulle finale de \(X\mid m\) dépasse celle de l’étalonnage au seuil retenu, le plafond ne se transporte pas ; les deux règles peuvent échouer ensemble.
- **D3.** Pour \(J=\) « retrait certifié », si \(P(J\mid D,s)=0\) sur une strate cible de masse positive, \(P(S\mid D,s)\) y est inestimable parmi les admis. Une différence de bornes \(U\) peut provenir d’effectifs différents à \(q\) identique.
- **D4.1–D4.2.** Si \(P(q>U\mid E)\ne P(q>U)\), conserver un niveau marginal ne garantit pas la couverture conditionnelle. Sous effet aléatoire de campagne, \(q(\theta_c)\) et \(\mathbb E[q(\theta_c)]\) sont des cibles distinctes ; le duel doit en choisir une, y compris pour le diagnostic honnête.
- **D5.** Si \(P(K=k\mid\text{format})\) est concentrée, l’ancrage reste reconnaissable. Le taux de fausses découvertes de l’honnête ne détermine pas sa probabilité d’acceptation par la cohérence.

**(c) Contrôles négatifs indispensables.** Journal des verdicts bruts sur les mêmes honnêtes ; édition factice préservant tous les contrôles, auditée en aveugle avec des objets refusés par le repéreur ; références honnêtes à présence certifiée par lecteur. Pour l’ancrage, tester le format seul sur des preuves permutées.

## Sur la proposition D

**(a) Défauts de méthode.** Une perturbation programmée des verdicts ne valide pas leur réponse à une variation des tâches. Maximiser la détection minimale reste interprétable si la validation réservée ne sert pas ensuite à choisir la famille de dommages. Arbitrer seulement les désaccords de désignation laisse invisibles les erreurs communes. La comparaison exacte à la référence cachée, proposée parmi les vérifications à battre, dispose d’une information que la règle de cohérence n’a pas : c’est un juge, pas un concurrent équitable.

**(b) Conditions mesurables.**
- **D1–D2.** Si \(\mathcal L(B\mid A,\text{perturbé})=\mathcal L(B\mid A,\text{nul})\), B n’ajoute pas de discrimination à A. Si \(\sup_{t:P(X\ge t\mid\neg D)\le\alpha}\min_s P(X\ge t\mid D,s)\) est inférieur à la cible, ni seuil fixe ni optimisation ne réussit.
- **D3.** Une masse \(P(L=R\ne Y)>0\), avec \(L,R\) les désignations et \(Y\) la vérité, échappe à l’arbitrage des seuls désaccords.
- **D4.1–D4.2.** Une borne constante égale au maximum possible couvre toujours : la couverture seule ne tranche pas l’utilité. Si \(P_\theta(E)=0\), la couverture sous excès n’est pas définie ; si le maximum du risque familial est hors des scénarios gelés, E4b ne l’estime pas.
- **D5.** Si \(\mathcal L(\text{preuves, fiche}\mid D)=\mathcal L(\text{preuves, fiche}\mid\neg D)\), toute détection sur ces entrées égale sa fausse alerte, même si le juge caché distingue les erreurs.

**(c) Contrôles négatifs indispensables.** Tâches honnêtes non perturbées avec même procédure d’appariement ; modifications bénignes du tiers dans la validation réservée ; audit aléatoire des accords. Pour l’optimiseur, inclure un cas infaisable où aucune garantie ne doit sortir. Pour la cohérence, comparer à un vérificateur sans référence cachée sur des fiches honnêtes également imparfaites.

## Sur la proposition F

**(a) Défauts de méthode.** L’identité par échangeabilité de F dépend du pas des parts ; elle ne s’étend pas automatiquement à une moyenne de lecteurs. La calibration conforme peut protéger un taux marginal sans protéger chaque taille \(m\). Le retrait factice est utile, mais n’a de valeur que s’il ressemble au retrait véritable hors perte du contrôle. L’excès de manques sur l’honnête n’implique pas mécaniquement une sur-alerte sur les *différences* de parts.

**(b) Conditions mesurables.**
- **D1–D2.** Si les verdicts sont appariés, \(\operatorname{Var}(\widehat{\Delta A})\) dépend de leur covariance ; deux intervalles binomiaux marginaux ne constituent pas un intervalle exact de différence. Si \(P(0<X<1/m)>0\), \(P(X\ge1/m)\ne P(X\ne0)/2\) sous symétrie. Un taux marginal \(\le\alpha\) autorise \(P(S\mid\neg D,m)>\alpha\).
- **D3.** Si les deux désignateurs ont des erreurs élevées et égales, un faible écart d’erreur n’en valide aucun.
- **D4.1–D4.2.** Si les parts sont identiquement nulles des deux côtés, \(X=0\) malgré les manques honnêtes : aucune sur-alerte au seuil positif. Si la décision de branchement et le seuil minimisent la même fréquence empirique, cette fréquence n’est pas une validation du diagnostic. Le risque sur grille ne borne le risque continu qu’avec un contrôle hors grille.
- **D5.** Si \(\mathcal L(\text{fiche top-}K)=\mathcal L(\text{fiche correcte})\) conjointement aux preuves, l’acceptation mesure aussi des succès légitimes. À cardinal égal, des compositions de forces différentes ne donnent pas le même taux d’admission.

**(c) Contrôles négatifs indispensables.** Paires nulles inédites par \(m\), après gel du normalisateur ; retraits factices appariés en longueur et position ; diagnostic d’excès sur honnêtes non utilisés pour choisir le seuil ; fiches top-\(K\) effectivement correctes, séparées des substitutions erronées.

## Sur la proposition G

**(a) Défauts de méthode.** La détection « hors abstention » sélectionne les épisodes que le moniteur accepte de juger. Changer la famille du repéreur change aussi sa compétence et les passages effectivement retirés. Le duel E4 joint deux affirmations : un défaut du produit dose–borne ne réfute pas le contrôle du risque familial. Enfin, sous cardinal nul, top-\(K\) informé rend une fiche vide : il n’échoue pas mécaniquement.

**(b) Conditions mesurables.**
- **D1–D2.** Si \(P(\text{non-abstention}\mid D,s)=0\), la détection conditionnelle est indéfinie dans \(s\). Si la variance entre productions domine celle entre lectures, le quantile entre productions peut donner \(P(S\mid D,s)\) faible sur retraits appariés malgré une bonne spécificité.
- **D3.** Si la distribution de taille du retrait effectif diffère selon la famille, un écart de \(P(S\mid\text{famille})\) subsiste même à sensibilité identique à taille fixée. \(1-\mathrm{précision}=P(\neg D\mid S)\), non \(P(S\mid\neg D)\).
- **D4.1–D4.2.** Sous \(S\perp D\), \(q=1-P(S)\) : sa baisse est réelle pour cette définition, mais ne mesure pas une discrimination. Elle n’impose aucune valeur à \(P(\bigcup_j F_j)\), où \(F_j\) désigne une erreur de garantie publiée.
- **D5.** Une entropie marginale élevée de \(K\) est compatible avec une entropie conditionnelle nulle sachant le format. Si \(P(K=0)\) change entre bras, une variation d’acceptation marginale n’identifie pas l’effet de révélation.

**(c) Contrôles négatifs indispensables.** Abstention aléatoire de mêmes marges ; retrait identique présenté aux moniteurs de familles différentes ; procédure à niveaux fixes sous les mêmes dépendances que le recyclage, en plus de l’oracle aveugle. Sous lois nulles, laisser l’honnête produire sa fiche sans lui imposer qu’elle soit vide.

## Sur la proposition H

**(a) Défauts de méthode.** La significativité de A n’établit ni son importance ni la redondance de B. L’écart-type d’une part au \(m\) médian ne teste pas la queue de la différence appariée. L’audit des premières citations sélectionne les usages visibles *après* publication ; il ne tranche pas la décision préalable de publier.

**(b) Conditions mesurables.**
- **D1–D2.** À \(\Delta A\ne0\) fixé, le rapport à l’erreur-type croît quand cette erreur tend vers zéro. À variance marginale des parts fixée, la covariance des lectures et la loi de queue de \(X\) peuvent faire varier \(P(X\ge1/m)\).
- **D3.** Si la précision est sous cible et le rappel au-dessus, la règle de réfutation par le rappel seul manque l’échec. Si \(P(s\mid\text{annoté})=0<P(s)\), le biais de plantation dans \(s\) n’est pas borné par cet audit.
- **D4.1–D4.2.** Pour un taux de mauvaise interprétation \(p>0\), la probabilité de zéro erreur parmi \(n\) citations indépendantes vaut \((1-p)^n\). Si aucune citation n’est disponible, le taux est inestimable. La couverture marginale d’une borne n’est pas la couverture simultanée des énoncés publiés.
- **D5.** Un taux de rejet entre les deux frontières proposées ne satisfait ni hypothèse. Si la probabilité de fiche incorrecte varie, le rejet non conditionné ne mesure pas spécifiquement la détection de cette erreur.

**(c) Contrôles négatifs indispensables.** Même moniteur ternaire dans deux copies du même monde ; paires honnêtes de chaque taille plutôt qu’un lecteur uniforme ; passages non porteurs mais lexicalement proches. Pour l’interprétation, inclure des sorties explicitement non garanties de valeur connue. Pour le recyclage, garder le branchement actif à niveaux fixes.

## Sur la proposition I

**(a) Défauts de méthode.** D1 prétend fixer une marge sur A par un duel portant sur B. La chaîne « désignation → signalement → excès » confond trois variables : un repérage raté ne modifie pas nécessairement la lecture de l’honnête. Étalonner et diagnostiquer l’excès sur les mêmes paires risque de rendre le diagnostic favorable par construction. Fabriquer des leurres pour que top-\(K\) soit faux teste le générateur choisi, non la fréquence ordinaire d’évasion.

**(b) Conditions mesurables.**
- **D1–D2.** Une même loi de \(\widehat{\Delta B}\) est compatible avec plusieurs \(\Delta A\). Si \(\mathcal L(X\mid\text{relecture})\ne\mathcal L(X\mid\text{nouvelle production})\), les deux lots n’estiment pas nécessairement la même queue nulle.
- **D3.** \(1-\mathrm{rappel}=P(L=0\mid Y=1)\) n’est le taux de paraphrase que sous une relation spécifique entre paraphrase et échec lexical. Les erreurs communes des repéreurs ne sont pas identifiables sur leurs seuls désaccords.
- **D4.1–D4.2.** Fixer le *paramètre* de manques au-dessus du seuil ne simule pas \(\mathcal L(U\mid E)\) si le déclenchement est aléatoire. Même \(P(q>U)\le\alpha\) ne donne pas le risque familial sans la loi jointe des autres erreurs.
- **D5.** Si \(P(K)\) est déséquilibrée, l’exactitude sans information peut atteindre \(\max_k P(K=k)\). L’échec d’un lecteur particulier ne borne pas l’exactitude optimale ; une réussite à partir de preuves pertinentes n’établit pas une fuite par métadonnées.

**(c) Contrôles négatifs indispensables.** Auditer aussi les accords de désignation ; diagnostiquer les manques sur un lot honnête neuf après choix du seuil ; conserver une campagne sans leurres. Pour \(K\), opposer à la prédiction par preuves une prédiction par format seul, évaluée hors construction contre le prédicteur modal. Sans cette séparation, « cardinal inférable » ne dit pas ce qu’il faut corriger.

FIN-DE-CELLULE