# Arbitrage : en quelle unité lire les décalages du saboteur, course « seuil et moniteurs » — v1

- Auteur : Claude Fable 5.2 (identifiant `claude-fable-5-2`, tel que mon invite système le nomme : « You are powered by the model named Fable 5.2. »), consulté comme arbitre sous GO-2026-11-21-27. Écrit le 2026-11-21. Classe C. Aucun appel payant, aucun commit, aucune poussée.
- Pas lu : aucune sortie d'auteur de mondes, aucune vérité des témoins, aucun résultat ; **ni le programme de vérité des témoins** (`calculer_verite_temoins_imposes_v1.py`, 4857343c…), qui n'est pas dans les dossiers nommés. Je ne sais donc pas comment il calcule l'« écart type » d'une loi : voir la réserve 1.

## 0. Verdict

**Tranché, sous une condition.** Les décalages du saboteur se lisent en **écarts types de la loi honnête de la tranche**. Condition : un **contrôle par l'aire**, écrit et contre-lu avant toute lecture de la sortie de l'auteur, vérifie que chaque décalage, ainsi lu, réalise bien l'aire dite. Sans ce contrôle, la lecture reste la meilleure lecture de la lettre, mais elle peut se tromper en silence, et je ne la donnerais pas pour tranchée.

Confiances, séparées parce qu'elles ne disent pas la même chose :
- que ce soit la meilleure lecture de la lettre : **0,80** ;
- qu'un auteur extérieur l'ait suivie pour une loi dont l'écart type ne vaut pas 1 : **0,60** seulement ;
- que la lecture **avec** le contrôle par l'aire donne un saboteur juste ou un écart nommé, jamais une erreur muette : **0,90**.

## 1. La lecture retenue, et ce qui la fonde

**Phrase opposable.** Les décalages du saboteur (`familles[i].saboteur.decalages`) se lisent en écarts types de la loi honnête de la tranche où le témoin est joué : le saboteur de la tranche est la loi `decalage` (loi honnête de la tranche, `delta_en_ecarts_types` = le nombre écrit). « Écart type » veut dire la racine de la variance de la loi `loi_honnete` entière de la tranche (le mélange entier, la somme de pas entière, la loi après arrondi), et non un paramètre nommé `sigma` ou `echelle`.

Pièces et lignes (texte servi v3, `docs/notes/ideation-seuil-moniteurs-v1/mandat-mondes-plantes-v3/erratum-mandat-1-v1/essai-mandat-auteur-mondes-plantes-seuil-et-moniteurs-v3-erratum-1-applique-v3.md`, branche `lot/compte-organisme-v1`, empreinte recalculée f3d871628d489f45…) :

1. **l. 103** : « Le saboteur […] : la loi honnête décalée. Trois tailles de signal, dites par l'aire sous la courbe […] Donne le décalage qui réalise chaque aire sous ta loi. » La taille du signal est **définie par l'aire** ; le décalage en est déduit. C'est le point qui porte tout le reste : ce que la lettre fixe, c'est l'aire, pas l'unité.
2. **l. 145** : `saboteur` est un objet à deux clés, `forme` et `decalages`, sans unité.
3. **l. 147** : `forme` est une loi de la grammaire fermée. Le seul constructeur de cette grammaire qui dise « une loi décalée » est `decalage` (loi, `delta_en_ecarts_types`). La forme fixe n'offre donc à l'auteur **aucun moyen d'écrire un décalage dans une autre unité**.
4. **l. 81** : pour T09, « donne le décalage en écarts types ». C'est la seule unité de décalage nommée dans tout le texte, et elle l'est deux fois (l. 81, l. 147).
5. **l. 145, encore** : le saboteur est écrit **une fois par famille**, alors que la loi honnête est écrite par tranche. Dans la famille D (« loi qui dépend de la tranche », l. 94), un seul nombre ne peut « réaliser chaque aire » dans des tranches d'échelles différentes que s'il est relatif à l'échelle de chaque tranche. Cela écarte l'unité brute là où les tranches diffèrent par l'échelle, et dit « de la tranche » plutôt que « de la famille ».
6. Ordre v6 (`…/conception-v6/ordre-course-seuil-et-moniteurs-v6.md`, 208454c500c455a4…), **l. 209** : « saboteur décalé, à trois tailles de signal (aire sous la courbe 0,69, 0,80 ou 0,95) », sans unité ; **l. 210**, « 0,446 écart type », parle de la dérive de F. La note de conception d'origine (4f3ae86f…, sur main, l. 198 et 199) dit la même chose, mot pour mot ou presque : elle se tait aussi. **Aucun texte scellé ne dit une autre unité** ; la constatation du vérificateur S (6dce2dc07c1fc6a3…, § 8) est exacte.
7. Le programme de vérification v3 (`…/programme-verification-sortie-mondes-v3/verifier_sortie_auteur_mondes_v3.py`, d0d50cec64febadb…, l. 1466 à 1471, choix `CH5`) applique déjà cette lecture : chaque nombre de `decalages` devient le `delta_en_ecarts_types` d'une loi `decalage` posée sur la loi honnête de la tranche choisie par la taille du témoin. Rien à changer à cette ligne.

Ce n'est pas un écart à la lettre : c'est une **lecture déclarée de session**, comme celle de la dérive de F. Pas d'erratum du texte servi.

## 2. Les autres lectures, et le contrôle qui lève l'ambiguïté

| lecture | ce qui la rendrait correcte | ce qui la rend fausse ou faible |
|---|---|---|
| **unité brute du score** (le nombre s'ajoute tel quel au score) | c'est le sens nu de « la loi honnête décalée » ; un auteur qui résout « quelle translation donne l'aire 0,80 sous ma loi » rend naturellement ce nombre ; c'est la seule lecture possible si la loi n'a pas d'écart type fini (Student à deux degrés de liberté ou moins) | contredit la seule unité nommée (l. 81, l. 147) ; ne peut pas tenir avec un seul nombre par famille quand les tranches diffèrent par l'échelle (famille D) |
| **écart type d'une loi poolée** (toutes tranches confondues) | rien dans les textes : la règle reçoit et le noyau mesure tranche par tranche (texte servi, l. 29 et 31) | aucune loi poolée n'est définie nulle part ; je l'écarte |
| **paramètre d'échelle de la loi** (`sigma` d'une log-normale, `echelle` d'une Student ou d'une Laplace) | un auteur peut confondre « échelle » et « écart type » ; pour la normale les deux coïncident | la lettre dit « écarts types », non « échelle » ; pour une Laplace l'écart type vaut l'échelle fois racine de deux, pour une Student à trois degrés racine de trois fois l'échelle |
| **écart type d'une composante** (dans C et I, la composante « honnête qui réussit ») | si l'auteur a pensé le saboteur contre l'honnête ordinaire | la loi honnête de la tranche est le mélange entier (l. 93, l. 101) ; `CH5` pose le décalage sur le mélange |
| **écart type de la loi honnête de la tranche** (retenue) | points 1 à 7 du § 1 | la lettre ne l'écrit pas pour `decalages` ; indéfinie sans variance finie |

Quand l'écart type de la loi vaut 1 (normale réduite, famille H à variance totale 1), toutes ces lectures donnent le même saboteur : il n'y a rien à trancher. L'enjeu est ailleurs, et il est gros. Calcul d'illustration de ma main, en flottants, non contre-lu : sous une normale d'écart type 2, le nombre 1,19 donne l'aire 0,80 lu en écarts types et 0,66 lu en unité brute ; sous une Student à trois degrés de liberté et d'échelle 1, le décalage brut qui réalise 0,80 vaut 1,54, et ce même nombre lu en écarts types donnerait l'aire 0,91. Une erreur d'unité déplace donc toute la puissance des témoins T05 et T07 et de tout témoin de grandeur `puissance`.

**Le contrôle par l'aire : il existe, et il lève l'ambiguïté sans la choisir.** L'aire entre la loi honnête et sa translatée d'une quantité δ est la probabilité qu'un score du saboteur dépasse un score honnête (un demi pour les ex æquo) ; elle croît avec δ ; c'est une intégrale à une dimension, donc « exacte » au sens du texte servi (l. 107). Pour chaque famille, chaque tranche et chacun des trois nombres :

1. calculer l'aire réalisée sous la lecture retenue (translation du nombre fois l'écart type de la loi honnête de la tranche) ;
2. calculer, **à titre de diagnostic**, l'aire réalisée sous l'unité brute, et le rapport entre la translation exacte qui réalise l'aire dite et le nombre écrit (s'il est le même pour les trois nombres, c'est l'unité de l'auteur) ;
3. comparer aux aires dites 0,69, 0,80 et 0,95.

Règle d'issue, à écrire avant la lecture de la sortie, sans repli silencieux (règle R5) [seuils : propositions, à geler par la mère] :
- **(a) conforme** : sous la lecture retenue, les trois aires sont à moins de 0,005 des aires dites (les aires sont données à deux décimales : c'est « réaliser l'aire dite ») ; un écart de plus de 0,001 est compté et nommé, comme au point 4 du § 6 du texte servi, sans changer la lecture. Repère sous une loi normale : 0,70, 1,19 et 2,33 écarts types passent à 0,001 ; 1,2 et 2,3 ne passent qu'à 0,005.
- **(b) unité brute constatée** : (a) échoue dans une tranche au moins, et l'unité brute réalise les trois aires à 0,005 dans les trois tranches. La famille porte un code nommé au compte rendu. Les témoins de cette famille qui demandent un saboteur **ne sont pas convertis** par le programme ; la session décide, par une lecture déclarée de plus, écrite au journal avant tout recalcul, si elle convertit les nombres (division par l'écart type de la tranche). Je recommande de l'accorder : l'aire est la définition de la lettre, et aucun résultat n'est lu pour choisir. Mais c'est un mot de la mère, pas un automatisme du programme.
- **(c) ni l'un ni l'autre**, ou écart type indéfini sans que l'unité brute réalise les aires, ou loi que le contrôle ne sait pas calculer : saboteur de la famille « non lisible », témoins à saboteur non convertis, code nommé, rapport à la mère. Ce n'est pas « illisible » au sens du § 6 : la famille reste, ses témoins de couverture aussi.

Ce contrôle ne lit que la loi et les nombres de l'auteur : aucune vérité des témoins, aucune issue. Il est de classe B (instrument) : contre-lecture par l'autre modèle, puis vérification des corrections.

## 3. Ce que je ne tranche pas

1. **Ce que le programme de vérité entend par « écart type »** dans son constructeur `decalage` : je ne l'ai pas lu. Si ce n'est pas la racine de la variance de la loi entière (par exemple s'il prend le paramètre `echelle`), la phrase du § 1 et le programme divergent : à vérifier par celui qui a le droit de le lire, avant le scellement. Même question pour une loi sans variance finie : que fait-il ?
2. **Le saboteur des mondes scellés** (celui que le générateur jouera dans la course) : je recommande qu'il soit gelé par son aire, le décalage exact recalculé chez la mère, plutôt que par le nombre de l'auteur. C'est une décision du scellement des mondes, hors de cet arbitrage.
3. **Voie plus propre, si l'auteur n'a pas encore été appelé** : une ligne de plus dans une version neuve du texte servi (« en écarts types de la loi honnête de la tranche »). Elle coûte une chaîne complète ; le contrôle par l'aire la rend inutile. Choix de la mère.
4. Points voisins, signalés sans les trancher : la convention des ex æquo dans l'aire pour la famille G ; l'ordre « arrondir puis décaler » ou l'inverse ; dans F, le saboteur est posé sur la loi honnête d'avant la dérive (`CH5`, l. 1468).

Rien ici ne demande le collisionneur. Lazar n'est requis que si l'issue (b) ou (c) se présente et que la mère veut autre chose que ce qui est écrit au § 2.

## 4. La phrase à citer dans la pièce de scellement de la mère

> Lecture déclarée de session, arbitrée par Claude Fable 5.2 sous GO-2026-11-21-27 (`docs/notes/ideation-seuil-moniteurs-v1/arbitrage-unite-decalages-v1/arbitrage-fable-unite-decalages-v1.md`) : le texte servi v3 (f3d87162…) et l'ordre v6 ne disent pas l'unité des trois décalages du saboteur ; ils se lisent en écarts types de la loi honnête de la tranche (racine de la variance de la loi `loi_honnete` entière), seule unité de décalage que le texte servi nomme (l. 81 et l. 147) ; la taille du signal restant définie par l'aire (l. 103), un contrôle écrit avant la lecture de la sortie vérifie, sous la loi de l'auteur, que chaque décalage ainsi lu réalise l'aire dite à 0,005 près, tout écart de plus de 0,001 étant compté et nommé ; si la lecture échoue, le saboteur de la famille n'est pas converti et le cas est rapporté, sans repli silencieux.

## 5. Réserves

1. Programme de vérité non lu (§ 3, point 1) : la lecture est fondée sur les textes et sur le programme de vérification v3, pas sur le moteur qui l'exécute.
2. Les nombres du § 2 sont des illustrations en flottants, de ma main, non contre-lues ; aucun n'est opposable.
3. Les seuils 0,005 et 0,001 sont des propositions ; le second reprend celui du point 4 du § 6 du texte servi, lui-même marqué [proposition].
4. Ma confiance de 0,60 sur la conduite de l'auteur est un jugement, non une mesure.
