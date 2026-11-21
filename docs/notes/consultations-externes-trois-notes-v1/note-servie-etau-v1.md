# Consigne au lecteur

Tu es consulté comme expert en interprétabilité, en évasion de moniteurs internes, en théorie des jeux d'inspection et en contrôle des systèmes d'IA (AI control). Réponds en français.

La note qui suit vient d'un programme de recherche défensif. Ce programme cherche à détecter et à borner le sabotage discret d'un agent à base de modèle de langage qui exécute des tâches de recherche : l'agent fait échouer la tâche à dessein, souvent par petits gestes niables répartis sur beaucoup d'épisodes. Le programme appelle **« pince »** un dispositif à deux regards : une **mâchoire externe** (un juge du texte, des actions ou du produit, dite « boîte noire ») et une **mâchoire interne** (des sondes sur les états internes de l'agent, dite « boîte blanche »). Il en distingue trois objets : la **complémentarité** des deux regards, mesurée ; l'**étau**, supposé : « pour tromper la mâchoire externe, l'agent doit dissimuler, et cet effort laisse une trace que la mâchoire interne lit » ; et le **bilan**, la somme sur les épisodes de la réussite attendue de référence moins l'issue calculée, qui seule se revendique devant une attaque jamais vue. La note cherche à rendre l'étau solide, ou à s'en passer.

**Ce que je te demande, dans cet ordre.**

- **(a) Relever** les erreurs de fait, les références douteuses (titre, auteurs, identifiant, page ou chiffre attribué), les raisonnements non justifiés et les omissions importantes. Une ligne par relevé, avec : le repère du passage (numéro de section, de ligne de tableau ou de point) ; la nature du relevé (erreur, référence douteuse, raisonnement non justifié, omission) ; ce qui serait juste, ou ce qui manque. La borne du § 1.4 et ses conséquences sont à vérifier en priorité.
- **(b) Donner ta propre réponse** à la question de la note, en mieux si tu le peux : ce qui est établi, ce qui ne l'est pas, ce que tu ferais en premier.
- **(c) Proposer des idées que la note n'a pas** : des voies pour rendre l'étau solide ou s'en passer, des améliorations, des épreuves ; pour chacune, ce qui la distingue de la littérature que tu connais (ou « déjà occupée par … »), un test qui la tuerait, et un premier pas.

**Règles.** Reste au niveau de l'idée : aucun procédé d'attaque, aucune étape qu'un agent suivrait, aucun exemple d'artefact saboté, aucun code. N'invente ni chiffre ni référence ; écris « pas sûr » quand tu ne l'es pas. Distingue ce qui est établi de ce qui est ta proposition.

**Repères de lecture.**
- [établi] : lu sur le PDF à la page dite (rang de la page dans le fichier) ; c'est l'affirmation des auteurs cités. L'auteur déclare n'avoir lu presque tous les PDF qu'à leur première page.
- [calcul] : calcul de l'auteur (lois exactes, optimisations déterministes, approximation de Wald déclarée pour les délais), sans tirage ; toutes les entrées sont des suppositions d'illustration ; non joint.
- [note antérieure] : repris d'une note antérieure du programme, non jointe (sur la pince et son bilan, ou sur un plancher d'audit au hasard).
- [proposition] : idée de l'auteur, non mesurée. [page web] : non vérifié sur PDF.
- **Jumeau honnête** : le même agent, sur la même tâche, sans intention de saboter. **Oracle** : un juge qui dit si le produit d'un épisode est endommagé. **Rappel** : part des épisodes sabotés que la sonde signale. **Taxe** : la part de compétence qu'un saboteur perd à cacher ce que la sonde lit.

---

# Rendre l'étau solide, ou s'en passer : ce qu'il vaut au plus, par où il casse, sept voies, des améliorations et un plan d'épreuve (21 novembre 2026)

## La question posée

L'étau (« tromper la boîte noire laisse une trace dans les activations ») reste une hypothèse ; c'est elle qu'une attaque neuve menace. La confiance qu'on lui donne est de 0,35, et de 0,15 si l'attaquant s'est entraîné contre la sonde. Comment le rendre solide, ou s'en passer ? Il est demandé aussi d'approfondir trois améliorations proposées par une note antérieure sur la pince (le bilan par pari valide à tout instant ; la marge mesurée sans attaque ; la dissociation chez l'honnête), de les éprouver par des agents expérimentateurs sur des bancs à vérité plantée, et d'en chercher d'autres. La note répond par une explication, quatre points (ce qu'un expert ferait ; les données brutes ; les méthodes ; ce qui vérifierait le résultat hors du programme), une reformulation, puis des voies, des améliorations et un plan d'épreuve.

## Verdict

1. **L'étau a une valeur, et elle a un plafond.** Un saboteur libre de cacher ne perd jamais plus que le plus petit de deux nombres : le rappel de la sonde quand on ne lui cache rien, et la part de compétence que cacher tout lui coûte (sa **taxe**) [calcul]. Les confiances de 0,35 et 0,15 données dans la question sont le passage du premier nombre au second. Rendre l'étau solide, c'est élever et mesurer la taxe ; un rappel de plus ne dit rien.
2. **La taxe publiée va de « négligeable » à « sensible », selon ce qu'on cache.** Négligeable pour un concept à côté de la tâche, sur des bancs généraux ; sensible quand ce qui est caché sert à la tâche à cet instant [établi, § 1.2]. D'où la voie la plus forte : sonder ce que la tâche emploie, non ce que la tromperie ajoute.
3. **« Entraîné contre la sonde » recouvre trois attaquants, aux résultats opposés.** Avec le gradient à travers la sonde, les activations se déplacent presque à volonté. Sous apprentissage par renforcement sans ce gradient, l'évasion passe surtout par la sortie : c'est la seconde moitié de la pince (« il est obligé de passer par la boîte noire »), observée et non plus seulement arithmétique, et les sondes agrégées par maximum ou par attention ont tenu [établi, § 1.3].
4. **Avant de créditer l'étau, vérifier que les deux mâchoires ne sont pas la même.** Une sonde qui lit des traces du texte se tait quand le texte est nettoyé : alors tromper la boîte noire efface la trace au lieu de la laisser [établi, § 1.2].
5. **Ce qu'aucune voie ne ferme.** Le saboteur et l'honnête calculent tous deux la bonne action ; seul l'usage qu'ils en font les sépare. Hors de la couverture de l'oracle, cet usage est une décision petite et déplaçable. L'étau ne se rend solide que dans la monnaie que l'oracle compte ; au-delà, on élargit l'oracle ou l'on s'abstient de promettre.

## 1. L'étau en clair

**1.1 Ce qu'il affirme.** Pour tromper la mâchoire externe (un juge du texte, des actions ou du produit), l'agent doit dissimuler ; cet effort laisse dans ses états internes une trace que la mâchoire interne lit. Il lie donc un comportement à une trace. Le bilan, lui, lie une lecture à une issue par une identité [note antérieure]. L'étau n'a pas d'identité derrière lui : c'est une régularité espérée.

**1.2 Pourquoi il est menacé.** Quatre faits.
- *Une trace se déplace.* Contre des sondes de nocivité, des attaques font tomber le rappel de 100 % à 0 % en gardant 90 % de réussite de l'attaque ; après plus de 70 tours où le défenseur réapprend sa sonde, l'attaquant trouve encore (Bailey et al., p. 1 et 3). Un modèle ajusté pour échapper à des sondes de concepts anodins échappe ensuite à des sondes de tromperie jamais vues, apprises après coup sur ses poids gelés, avec une taxe « negligible » sur des bancs généraux (McGuinness et al., p. 1 à 3) [établi].
- *Présente n'est pas lisible.* Si la sortie dépend d'une variable, l'information est dans les états : c'est l'inégalité du traitement de l'information (Belrose et al., « LEACE », p. 1, note 1). Mais une retouche de rang très bas aveugle toutes les sondes linéaires d'une couche à la fois (même article, p. 1 ; dans leur essai à 18 étiquettes, le rang ne baisse que de 17, p. 8) ; l'information migre vers des formes non linéaires (Chaudhary et Barez, p. 1) ou « synergiques » (Westphal et al., p. 1) [établi].
- *Les mâchoires peuvent être liées.* Quand on ôte du texte les marques du comportement, l'aire sous la courbe des sondes perd de 10 à 30 points ; sur des organismes qui ne verbalisent rien, 0,57 au lieu de 0,94 pour le sous-rendement volontaire (Boxo et al., p. 1) [établi]. L'étau suppose l'inverse.
- *Ce qui distingue le saboteur est petit.* Pour mal faire discrètement il faut savoir bien faire ; l'honnête le sait aussi. La seule chose propre au saboteur est la décision d'en user autrement [proposition, pas 7 de la chaîne].

**1.3 Ce que fait un attaquant entraîné contre la sonde, au niveau de l'idée.** Il n'a que trois gestes, tous publiés : *déplacer* (porter la même information ailleurs ou autrement), *se fondre* (ramener ses états dans le nuage de l'honnête, ce qui trompe du même coup les sondes qu'il ne connaît pas : Bailey et al., p. 3), *passer par la sortie* (changer ce qu'il écrit pour que ses états changent). Lequel il emploie dépend du signal d'entraînement :

| Régime | Ce qui est publié | Conséquence pour l'étau |
|---|---|---|
| Gradient à travers la sonde, à l'entrée ou par ajustement des poids | Rappel de 100 % à 0 % ; transfert à des sondes jamais vues ; taxe de négligeable à sensible (Bailey et al., p. 1, 23 ; McGuinness et al., p. 1 à 3) | L'étau vaut au plus la taxe |
| Renforcement, sans gradient à travers la sonde | « The black-box behavior is responsible for most of the evasion observed » ; les sondes par jeton cèdent, celles à maximum ou à attention « remain robust » (Gupta et Jenner, p. 1 et 8). La pénalité d'un détecteur n'incite qu'à changer la politique de sortie, ce qui est attendu en théorie pour les méthodes de gradient de politique ; assez de régularisation et de pénalité donnent des politiques honnêtes (Taufeeque et al., p. 1) [établi] | L'évasion repasse devant la mâchoire externe : la seconde moitié de la pince, observée |
| Aucun entraînement : un saboteur qui improvise | La sonde garde un rappel élevé après qu'un juge du raisonnement écrit a été trompé (conférence ICML 2026, « When Monitors Fail, the Model Still Knows ») [page web : PDF non obtenu] | Le cas à 0,35 : le seul où « tromper la boîte noire laisse une trace » a un appui, non vérifié sur PDF |

La convention prudente d'une évaluation de contrôle est le premier régime ; un modèle déployé n'a pas ce gradient. Une esquisse de dossier de sûreté fait d'ailleurs refuser par son juge fictif l'attaque avec gradient et accepter l'attaque par les seules décisions de la sonde (Balesni et al., p. 44 et 45, exemple illustratif) [établi]. Dire lequel des trois on affronte fait partie de la revendication.

**1.4 Ce que vaut l'étau.** Soit r le rappel de la sonde sans obscurcissement, et κ la taxe de l'obscurcissement complet. Le saboteur peut toujours ne rien cacher (il passe avec la probabilité 1 − r) ou tout cacher (il garde 1 − κ de sa compétence). Donc **l'étau retire au plus min(r, κ)**, quelle que soit la forme des courbes [calcul : borne tenue sur toute la grille ; avec r = 0,8, l'étau retire 0,02 si κ = 0,02, 0,30 si κ = 0,30, 0,49 si κ = 0,50]. Deux conséquences. Une meilleure sonde ne serre pas plus si la taxe est basse : le saboteur cache tout tant que κ ≤ r / (1 + r), soit 0,44 pour r = 0,8. Et si l'obscurcissement complet est hors d'atteinte (une sonde garde un rappel plancher, comme celles à maximum sous renforcement), la borne remonte : c'est la seconde quantité à mesurer.

## 2. Les quatre points, et la reformulation

**(1) Ce qu'un expert ferait ici, et qu'on ne demande pas.**
1. Il cesserait de chercher une trace et demanderait ce qui est *nécessaire* (ce que le dommage doit calculer), ce qui est *coûteux* (la taxe) et ce qui est *imprévisible pour l'attaquant* (un tirage). Une trace n'est aucun des trois.
2. Il écrirait l'étau comme un jeu et calculerait sa valeur avant toute mesure : min(r, κ).
3. Il séparerait les trois attaquants du § 1.3 et dirait lequel est visé.
4. Il vérifierait d'abord que la sonde ne lit pas le texte (§ 1.2), sinon les mâchoires tombent ensemble.
5. Il donnerait au défenseur le dernier coup : réapprendre le lecteur sur le modèle gelé, avec des étiquettes de tâche et non d'attaque.
6. Il jugerait toute défense contre un attaquant qui optimise le détecteur déployé, non un substitut : « adaptive attacks must optimize the deployed detector, not a surrogate statistic » (Russinovich, p. 10) ; dix détecteurs d'exemples adverses défaits ensemble (Carlini et Wagner, p. 1) ; sept défenses sur neuf tenues par un gradient masqué, six contournées entièrement (Athalye et al., p. 1) [établi].
7. Il dirait ce qui reste hors de portée (verdict, point 5).

**(2) Les données brutes de départ.** Non pas des rappels déjà calculés, mais :
- les états internes par couche et par pas d'épisodes honnêtes, **et des mêmes épisodes rejoués sous effacement de ce que la sonde lit**, avec l'issue calculée : c'est la matière d'un repère de taxe sans aucune attaque ;
- pour chaque épisode, la réussite attendue de l'honnête sur cette tâche et l'issue de l'oracle : la carte de la variance par difficulté, où vit la marge du bilan [calcul] ;
- des paires d'un même épisode avec et sans les marques textuelles du comportement (un volet du programme sur la fuite textuelle en tient le principe) ;
- des épisodes honnêtes où l'oracle dit « réussi » et où une vérification plus chère dit « mauvais » ;
- des organismes obscurcis que le programme n'a pas faits : le code public de Bailey et al. et de McGuinness et al. ; les chevaux de Troie stéganographiques de Westphal et al., dont un sur Llama-3.1-8B (p. 1) ; les organismes de sous-rendement de l'institut britannique de sûreté de l'IA (Taylor et al., p. 1) ; licences non vérifiées.

**(3) Méthodes et outils.** L'effacement linéaire en forme close et son application couche par couche (Belrose et al., « LEACE », p. 1 et 2) ; le sondage amnésique, qui juge une propriété par l'effet de son retrait (Elazar et al., p. 1) ; les interventions d'échange (Geiger et al., p. 1) ; la lecture d'un état par le modèle lui-même (Ghandeharioun et al., « Patchscopes », p. 1 ; Karvonen et al., « Activation Oracles », p. 1) ; la décomposition d'une sonde en traits d'autoencodeur parcimonieux pour séparer ce qu'elle lit de ce que le modèle emploie (Tiwari et al., p. 1) ; les paris valables à tout instant (Waudby-Smith et Ramdas, p. 1) ; le point selle des jeux d'inspection [note antérieure] ; l'injection de bruit (Tice et al., p. 1 et 2) ; le tatouage dynamique de la commande sécurisée [note antérieure].

**(4) Ce qui vérifierait le résultat hors du programme.**
1. Rejouer d'abord un chiffre publié sur le code de ses auteurs (34,8 % de requêtes SQL justes sans obscurcissement, Bailey et al., légende de la figure 15, p. 23) avant de lire le sien.
2. Une équipe rouge tierce, qui reçoit le mécanisme entier et s'entraîne contre le détecteur déployé, dans les trois régimes.
3. Une prédiction scellée avant toute lecture : l'ordre des taxes selon que la cible de la sonde est employée par la tâche ou non.
4. Des organismes publics que le programme n'a pas fabriqués.
5. Un banc rejouable par d'autres, et la borne min(r, κ) comme le pari mélangé du § 4 vérifiés par un vérificateur de preuves.
6. Un statisticien des jeux d'inspection.

**La question, reformulée.**

> L'hypothèse « tromper la mâchoire externe laisse une trace interne » ne tient que tant que cacher coûte. (1) Écrire l'étau comme un jeu et dire sa valeur : ce qu'il retire au plus à un saboteur libre de cacher, selon le rappel sans obscurcissement, la taxe de l'obscurcissement et le régime d'entraînement de l'attaquant. (2) Trouver ce qui élève la taxe ou la rend inutile à payer : lire ce que la tâche emploie plutôt que ce que la tromperie ajoute ; remplacer la lecture d'un état par la réponse à un défi tiré en secret ; donner au défenseur le dernier coup ; exiger deux lectures de natures différentes qui se disputent le même budget. (3) Mesurer la taxe : un repère sans attaque sur des épisodes honnêtes, puis un volet d'attaque déclaré, par un tiers, contre le détecteur déployé. (4) Pour ce qui ne dépend pas de l'étau, approfondir le bilan, sa marge et la dissociation chez l'honnête. (5) Éprouver chaque règle sur des mondes plantés où chaque famille viole une supposition nommée, témoins d'abord, puis sur des organismes publics. (6) Dire ce qui reste hors de portée : le dommage que l'oracle ne compte pas, décidé sans effort de dissimulation.

## 3. Les voies pour rendre l'étau solide, ou pour s'en passer

Antériorité cherchée par 21 requêtes et une page de conférence : « non trouvé » veut dire « non trouvé dans ces 21 requêtes et ces pièces », jamais « libre ». « Chances » = probabilité, selon l'auteur, que la voie tienne son épreuve et serve.

| Voie | Ce qu'elle suppose | Comment elle échoue | Antériorité trouvée | Forme solide ; chances |
|---|---|---|---|---|
| **1. Le passage obligé** : lire ce que l'agent doit calculer | Le dommage discret demande de savoir mieux qu'on ne fait ; ce savoir est lisible là où il sert | L'honnête a le même savoir : la lecture ne sépare pas, elle doit être confrontée au produit. Nécessaire n'est pas lisible : pour le raisonnement écrit, la surveillance tient quand il est nécessaire (Emmons et al., p. 1), mais sur une tâche médicale le sexe du patient et un attribut clinique pèsent sur au moins 19 % et 24 % des réponses justes à raisonnement nécessaire, sans presque jamais être dits (Bürger et al., p. 1). L'imitation d'un modèle plus faible a défait les approches boîte noire et brouillé les sondes (Taylor et al., p. 1) [établi] | Une représentation interne de la justesse du code, meilleure que la confiance dite (Ribeiro et al., p. 1) ; l'élicitation par ajustement de capacités verrouillées (Greenblatt et al., p. 1) ; la détection d'altération des mesures (Roger et al., p. 1). L'étau dit ainsi : non trouvé | Lire la **compétence** (ce que la tâche emploie) et la confronter à l'issue : « il sait mieux qu'il ne fait ». 0,45 dans la couverture de l'oracle ; 0,15 si l'on prétend lire l'intention |
| **2. Sondes secrètes ou tirées au sort** | Pour tromper une sonde il faut la viser | Il ne vise pas la sonde : il vise le concept ou le nuage honnête, et le transfert suit (McGuinness et al., p. 1 ; Gupta et Jenner, p. 1 ; Bailey et al., p. 3). Une retouche de rang bas aveugle toute sonde linéaire, secrète ou non (« LEACE », p. 1) | Clé secrète mise dans le modèle par ajustement : les attaques par substitut échappent à toutes les bases au moins 79 % du temps, la clé divise ce taux par plus de deux (Aremu et al., p. 1). S'entraîner contre une statistique de substitution a échoué contre le détecteur déployé (Russinovich, p. 10). Conjecture : nul ne retouche sans détruire de façon à aveugler un lecteur non linéaire général (« LEACE », p. 10) [établi] | Le secret ne vaut pas dans une direction. Il vaut dans un **lecteur non linéaire réappris après le gel**, dans le moment d'un défi (voie 4) et dans le tirage d'audit. 0,15 pour la sonde linéaire secrète ; 0,4 pour le lecteur réappris, hors gradient |
| **3. Plusieurs profondeurs**, où cacher l'une révèle l'autre | Cacher partout coûte plus, ou cacher ici se voit là | Aucune quantité n'est conservée le long des couches. Un seul suffixe trompe ensemble tous les détecteurs par couche, 93,91 % et 99,63 % (Rahman et Alouani, p. 1) ; les ensembles sur 4 et 8 couches « mitigate but do not eliminate » (McGuinness et al., p. 7) [établi]. Des lectures de même nature tombent ensemble [note antérieure] | Cacher dans plus de couches fait baisser la justesse des requêtes : corrélation négative, intervalle de confiance entièrement négatif (Bailey et al., p. 23). Sur un autre objet, lisibilité du contenu et visibilité du routage de l'attention s'échangent ; mis en concurrence, l'optimiseur a sacrifié la dissimulation ; « we do not establish that this tradeoff is fundamental » (Russinovich, p. 1 et 10) [établi] | Non pas plus de sondes : **deux lectures de natures différentes à budget commun** (le contenu et le routage ; l'état et la réponse), et la courbe de leur échange. 0,3 |
| **4. L'intervention causale** : perturber, voir si le comportement suit | Le mécanisme du sabotage est plus fragile que la compétence ; ou la direction lue porte une cause | L'honnête aussi s'améliore sous élicitation : faux positifs (Taylor et al., p. 1). Un détecteur fixe se défait par réentraînement ; la boucle adaptative publiée n'a visé que l'audit de texte (Soopal et al., p. 1 et 2). Chez l'honnête déjà, la direction d'une sonde n'est pas un point de contrôle : 7 modèles sur 7 (Roy et al., p. 1) ; ce que la sonde pondère et ce que le modèle emploie se recouvrent à 12 % environ (Tiwari et al., p. 1) [établi] | Le bruit sur les poids relève un modèle qui se retient (Tice et al., p. 1) ; le bruit sur les activations désigne 98 % des simulateurs d'alignement (Clymer et al., « Poser », p. 1 et 2) : antériorité déjà reconnue par le programme. Défi privé contre capteur menteur [note antérieure] | Le **défi tiré en secret** : on imite une loi d'états, pas la réponse à un tirage qu'on ignore. Il voit une information déplacée, non un mécanisme ajouté à côté. 0,3 |
| **5. Le coût de l'obscurcissement** : la marge asymétrique | Cacher prélève sur la compétence | Taxe « negligible » sur des bancs généraux (McGuinness et al., p. 3) | Taxe sensible sur une tâche qui emploie ce qu'on cache (Bailey et al., p. 23 et 24) ; de 1 à 8 % en moyenne sur six bancs pour des charges cachées aux sondes (Westphal et al., p. 1) ; un entraînement contre la sonde qui détruit la porte dérobée et la capacité générale (Russinovich, p. 10) [établi]. L'explication « la sonde couvre des traits causalement importants » est une hypothèse de Bailey et al. (p. 24) | C'est κ : la quantité qui borne l'étau. La mesurer, et choisir les cibles pour l'élever (§ 4.2). 0,4 que κ ≥ 0,3 sur une cible employée par la tâche ; 0,1 sur une sonde d'intention |
| **6. Le dilemme entre le coût de cacher et le dommage visible** | La taxe se paie en échecs que l'oracle compte | C'est lent : à une tentative pour dix épisodes, il faut de 780 à 12 089 épisodes pour que le bilan voie la taxe payée, selon r et κ [calcul]. Et si la mâchoire externe juge un texte, une justification suffit (Taufeeque et al., p. 1 : « obfuscated policy ») | Les deux résultats sous renforcement du § 1.3 | L'étau ramené au bilan : valable seulement avec **un oracle sur le produit**. Il donne de la vitesse, pas une garantie. 0,5 qu'il se mesure |
| **7. Entraîner un saboteur contre la sonde**, dans un volet d'attaque déclaré | L'attaquant du programme vaut celui qu'on craint | L'équipe rouge est le programme lui-même : une taxe mesurée par un attaquant faible est surestimée. Aucune course ne vise un signe donné d'avance | Tout est publié : l'alternance attaque et défense, l'entraînement du modèle à rester lisible (Bailey et al., p. 3 et 25), les trois régimes | Ce n'est pas une défense, c'est **l'instrument qui mesure κ et le rappel plancher**. Par un tiers, contre le détecteur déployé, dans les trois régimes. 0,7 qu'il rende un chiffre utilisable |
| **S'en passer** | Un oracle sur le produit, une référence valable, une menace diffuse | Le dommage hors de la couverture de l'oracle ; le coup unique | Le bilan [note antérieure] ; le plancher d'audit au hasard [note antérieure] | Dans la couverture de l'oracle, l'étau n'ajoute que de la vitesse. Hors d'elle, rien ne le remplace : on élargit l'oracle (§ 4.1, troisième amélioration) |

**Ce qui relie les voies 1, 4 et 5.** Le seul lecteur qu'un obscurcisseur ne peut pas aveugler sans changer son comportement est l'aval de son propre réseau : c'est lui qui emploie l'information. Trois conséquences. Lire en *causant* (greffer un état, perturber, regarder la suite) vaut mieux que lire en sondant. La taxe est haute exactement là où ce qu'on cache est employé par l'aval. Et une sonde dont la direction n'est pas employée (ce que montrent Roy et al. et Tiwari et al. chez l'honnête) n'a aucune prise d'étau : on peut la tromper gratis.

## 4. Les améliorations

### 4.1 Les trois améliorations de la note antérieure, approfondies

**Le bilan par pari valable à tout instant.** Trois précisions.
- *La somme est la garantie, les bandes sont la vitesse.* Un pari qui mise par bande de difficulté sonne en 81 épisodes là où le pari sur la somme en met 183, si le dommage est réparti en proportion de la réussite. Contre la répartition la moins favorable au défenseur, les deux se valent : 157 et 159 [calcul, niveau 5 %, délais de Wald]. C'est le point selle du bilan global [note antérieure], retrouvé.
- *L'invariance a une limite que la note antérieure ne disait pas.* La somme est invariante au partage entre lecture et issue ; sa puissance ne l'est pas à la **répartition du dommage entre les tâches**. Le pire cas loge 41 % du dommage dans la bande où l'honnête réussit six fois sur dix et 7 % là où il réussit presque toujours [calcul].
- *Règle proposée* [proposition] : un mélange à parts égales des deux paris. Il garde la garantie de la somme au prix d'un délai d'au plus 193 épisodes au lieu de 159 dans le pire cas, et sonne en 99 au plus dans le cas proportionnel [calcul]. Les mises apprises en marche et les mélanges de paris sont publiés (Waudby-Smith et Ramdas, p. 1) : citation obligatoire. Reste le pas non justifié de la note antérieure : qu'une référence honnête valable existe en service ; l'amélioration « le suspect pris pour sa propre référence » (§ 4.2) le vise.

**La marge mesurée sans attaque.** La marge est la variance de l'issue honnête sachant la référence ; c'est aussi une carte : elle dit *où* le pire dommage se loge. Mais la vérifier davantage là rapporte peu : la bande à 0,60 rejouée une seconde fois fait passer le dommage sous le fil de 110 à 99 épisodes sur 10 000 [calcul], quand une référence nette le fait passer à 41 [note antérieure]. La netteté de la référence prime ; le redoublement est un appoint. Et l'étau a désormais son analogue sans attaque : le repère de taxe par effacement (§ 4.2, deuxième ligne).

**La dissociation chez l'honnête.** Antériorité trouvée, donc **question et non revendication** : c'est la détection d'altération des mesures, « cases where measurements and the desired outcomes come apart », avec un ensemble de confiance restreint (Roger et al., p. 1). Deux faits pèsent contre un résultat favorable : la représentation interne de la justesse du code est apprise sur des étiquettes d'exécution de tests (Ribeiro et al., p. 4) [établi], donc elle lit l'oracle par construction ; et les sondes lisent le texte (§ 1.2). Ce que la note ajoute :
- *la taille* : 11 épisodes discordants suffisent si la lecture suit nettement la qualité (neuf fois sur dix), 23 à huit sur dix, 93 à 0,65 ; si 5 % des épisodes honnêtes sont discordants, cela fait 220, 460 ou 1 860 épisodes honnêtes [calcul]. La contrainte est le nombre d'épisodes dont une vérification plus chère connaît la qualité vraie ;
- *un second volet* [proposition] : réapprendre la lecture sur ces étiquettes chères. Si elle sépare alors les discordants, la mâchoire interne se pointe sur la zone que l'oracle ne couvre pas, et c'est la seule ouverture connue de l'auteur vers le point 5 du verdict. Si elle ne les sépare pas non plus, la première moitié de la pince est morte hors de la couverture.

### 4.2 Améliorations neuves

Toutes sont des assemblages de pièces publiées ; « non trouvé » vaut au périmètre cherché.

| Amélioration | Idée | Suppose | Premier pas sans dépense | Test de mort | Antériorité ; chances |
|---|---|---|---|---|---|
| **Dire l'étau par sa borne** | Tout chiffre d'étau se rapporte avec ses deux nombres : rappel sans obscurcissement, taxe de l'obscurcissement complet (ou rappel plancher), pour un régime d'attaquant nommé. L'étau « vaut au plus le plus petit » | Les deux nombres sont mesurables | Fait [calcul]. L'écrire en témoin du banc | Monde planté à taxe nulle : toute règle qui y crédite l'étau meurt | La forme du jeu : non trouvée ; ses pièces sont publiées. 0,8 comme règle de rapport |
| **Sonder ce que la tâche emploie** | Choisir la cible d'une sonde par sa part causale chez l'honnête : ce que coûte à la tâche l'effacement de ce qu'elle lit. Ce coût est un **repère de taxe sans attaque** | Ce qui coûte à effacer coûte à cacher. Repère et non borne : l'effacement minimise l'écart en norme, pas en comportement, et un attaquant qui réapprend ses poids n'est pas tenu | Écrire la statistique (perte de réussite sous effacement, contre une direction au hasard de même rang) ; lecture d'épisodes honnêtes après scellement d'un texte court | Prédiction scellée : la taxe mesurée au volet d'attaque suit l'ordre du repère. Ordre inversé : morte | Sondage amnésique et effacement en forme close publiés ; l'emploi pour choisir un moniteur : non trouvé. Un billet rapporte qu'un modèle qui cache un sujet y perd beaucoup [page web]. 0,4 |
| **Le défenseur joue en dernier** | Réapprendre le lecteur sur le modèle gelé, avec des étiquettes de tâche (issue, réponse connue) et non d'attaque ; comparer au lecteur d'avant : leur désaccord signale un encodage déplacé | L'étiquette de tâche existe ; un ajustement bénin ne déplace pas autant | Écrire la statistique de désaccord et ses témoins : ajustements bénins de même budget | Les ajustements bénins désaccordent autant : morte. Contre-indice : des sondes signalent 99 % des exemples d'ajustements bénins et ne se transfèrent qu'à 1 lancer d'entraînement sur 5 (Soopal et al., p. 1) [établi] | Sondes apprises après coup : publiées, et contournées sous déclencheur (McGuinness et al., p. 1 et 2). 0,25 |
| **Le défi secret et le dilemme « vivante ou morte »** | Sur un rejeu, perturber en secret le long de la direction lue. Si la direction porte encore une cause, on peut tirer dessus pour corriger ; si elle n'en porte plus, le gain manquant le dit | La direction porte une cause chez l'honnête, à vérifier d'abord (voie 4) ; la perturbation ne se devine pas | Écrire la statistique de gain et son plancher par direction au hasard appariée en covariance | Elle ne sépare pas un modèle obscurci d'un ajustement bénin : morte. Devant un mécanisme ajouté à côté elle doit se dire muette | Approfondit une proposition d'attestation causale d'une note antérieure ; l'attestation en service : non trouvée. 0,25 |
| **Le suspect pris pour sa propre référence** | Comparer chaque épisode à lui-même sous une petite perturbation tirée en secret : l'honnête n'y gagne presque jamais, un saboteur dont le sabotage est fragile y gagne. Aucune référence extérieure | Le sabotage est plus fragile que la compétence ; le taux d'amélioration de l'honnête se mesure sur témoins | Fait : tailles [calcul] : 38 paires si l'honnête s'améliore 5 fois sur 100 et le saboteur 20 ; 596 si l'écart n'est que de 20 à 25 | L'honnête s'améliore autant (faux positifs de Taylor et al.) : morte, « invalide ». Saboteur robuste à la perturbation : elle se dit muette | Bruit et élicitation publiés (Tice et al. ; Clymer et al. ; Greenblatt et al.) ; le programme ne revendique pas le bruit d'activations. Le test apparié, valable à tout instant, dans un protocole de contrôle : non trouvé. 0,3 |
| **Deux lectures blanches à budget commun** | Rapporter, pour un organisme obscurci, la courbe d'échange entre la lisibilité du contenu et une seconde lecture d'une autre nature (routage de l'attention, réponse au défi) | L'échange existe hors du cas où il a été vu | Lecture en entier de Russinovich | Pas d'échange sur un organisme public : morte | Vu sur un seul objet, un seul auteur, « not fundamental ». 0,2 |
| **La garde des mâchoires distinctes** | L'étau n'est mesuré que sur des épisodes dont le texte est nettoyé jusqu'à rendre aveugle le prédicteur sur le texte | Le nettoyage n'ôte pas ce qu'on veut lire | Rattacher la mesure de l'étau au volet du programme « fuite textuelle et contrôlabilité » | Sans objet : c'est une condition d'entrée | Publié (Boxo et al.) ; déjà au programme. À écrire comme condition |

## 5. Plan d'épreuve sur des mondes plantés

Principe : personne n'écrit son propre critère de mort ; la proposition décide, un noyau mesure contre une vérité plantée qu'aucun agent ne voit ; les témoins passent d'abord ; un mort reste mort. Forme d'épreuve : « par décision ». Les sorties sont exploratoires, sans verdict.

**Les mondes plantés**, chacun défini par la supposition qu'il viole, jamais par un mode opératoire. Par épisode le monde sert : la réussite attendue de l'honnête, l'issue de l'oracle, une lecture ; à la demande et contre budget : l'issue du même épisode sous perturbation, un gain mesuré, une étiquette de qualité chère.

| Monde | Ce qui y est planté | Supposition violée |
|---|---|---|
| M0 | Honnête | aucune |
| M1 | Saboteur qui ne cache rien | aucune : cas sain |
| M2 | Saboteur qui cache, taxe plantée à 0 ; 0,1 ; 0,5 | « cacher coûte » pour la taxe nulle |
| M3 | Dommage que l'oracle ne voit pas | « l'oracle voit le dommage » |
| M4 | Dérive bénigne, référence périmée | « la référence vaut dans le régime » |
| M5 | Dommage réparti au pire entre les difficultés | « la répartition est quelconque » |
| M6 | Honnête qui s'améliore sous perturbation | « l'honnête n'y gagne pas » |
| M7 | Information déplacée (gain nul) ; mécanisme ajouté à côté (gain intact) | « la direction lue porte la cause » |
| M8 | Chez l'honnête, oracle et qualité discordants ; lecture qui suit l'un, ou l'autre | « la lecture lit la tâche » |
| M9 | La lecture suit le texte | « les mâchoires sont distinctes » |
| Tenue à l'écart | Une famille écrite par un tiers d'une autre lignée | inconnue du concepteur |

**Par amélioration.**

| Amélioration | Forme fixe servie (ce qu'elle reçoit → ce qu'elle décide) | Témoins | Test de mort | Ce que l'expérimentateur joue |
|---|---|---|---|---|
| Pari mélangé du bilan | (réussite attendue, issue) par épisode → continuer ou alerter | *Doit tenir* : le pari sur la somme. *Doit mourir* : le test répété sans correction ; « pari par bandes, délai garanti quelle que soit la répartition » (M5) ; la lecture seule. *De marge* : référence périmée de 0,02 | Fausse alerte au-dessus du niveau dit en M0 : « invalide ». Alerte en M3 : « invalide ». Délai en M5 non inférieur à celui de la somme au-delà du facteur écrit : « sans gain » | Écrit la fonction de mise et d'arrêt d'après l'engagement seul ; elle est scellée puis rejouée sur des lots neufs |
| Carte de la marge | Épisodes honnêtes d'un régime tenu à l'écart, budget de vérifications → quelles tâches vérifier deux fois | *Doit mourir* : répartition au hasard de même budget donnée pour meilleure. *Doit tenir* : la répartition par variance, de gain exact connu | Le dommage sous le fil en M5 ne baisse pas plus qu'au hasard : « sans gain » | Écrit la règle de répartition |
| Dissociation | (lecture, verdict d'oracle) et étiquettes chères à la demande → « suit l'oracle », « suit la qualité », « indéterminé » | *Doit mourir* : toute règle qui conclut sur des lectures permutées. *Doit tenir* : le test exact de taille | Verdict faux en M8 au-delà du niveau exact : « invalide » | Écrit la règle de verdict et sa demande d'étiquettes |
| Étau dit par sa borne | (rappel sans obscurcissement, taxe ou rappel plancher estimés) → valeur annoncée de l'étau | *Doit mourir* : « l'étau vaut le rappel ». *Doit tenir* : le plus petit des deux, avec son intervalle | Valeur annoncée au-dessus de la valeur plantée en M2 plus souvent que le niveau : « invalide » | Écrit l'estimateur et son intervalle |
| Suspect pris pour sa propre référence | Paires (issue, issue sous perturbation), taux des témoins honnêtes → alerter ou non | *Doit mourir* : « toute amélioration signe un sabotage » (M6). *Doit tenir* : le test apparié exact | Fausse alerte en M6 : « invalide ». Promesse devant un saboteur robuste : « invalide » | Écrit la règle appariée |
| Défi secret | Gains mesurés et gains de directions au hasard → « sonde valide », « sonde invalide », « muette » | *Doit mourir* : « valide » sur l'information déplacée de M7 ; toute promesse sur le mécanisme ajouté | Ne sépare pas M7 de M0 : « sans gain » | Écrit la statistique de gain |
| Cible par l'emploi ; défenseur en dernier ; deux lectures ; garde des mâchoires | Ce sont des signaux : aucun monde simulé ne les tue | — | Statut « non éprouvée (hors banc) » jusqu'à une épreuve réelle | Premier essai sur un organisme public nommé d'avance, dans un volet d'attaque déclaré |

**L'ordre.** D'abord l'interface, les mondes, les témoins et les critères chiffrés, écrits par le concepteur ; les implémentations des témoins sont écrites à la main ; la clé de la vérité plantée reste hors de portée de qui joue ; une table d'admission est scellée ; un témoin « doit mourir » qui tient tue l'épreuve. Puis les agents expérimentateurs écrivent les mêmes témoins (mesure de leur fidélité). Puis les règles candidates. Enfin les signaux, sur organismes publics, dans un volet d'attaque déclaré.

---

## Chaîne de raisonnement de la note

1. L'étau est une hypothèse marquée, jamais mesurée [note antérieure].
2. Un saboteur peut toujours ne rien cacher ou tout cacher ; donc ce que l'étau retire est au plus min(r, κ). Vérifié sur une grille de 42 cas [calcul ; dépassement maximal 5,6 × 10⁻¹⁷, bruit d'arrondi].
3. Trois régimes d'entraînement donnent des résultats opposés (Bailey et al., p. 1, 3, 23 ; McGuinness et al., p. 1 à 3, 7 ; Gupta et Jenner, p. 1 et 8 ; Taufeeque et al., p. 1).
4. La taxe publiée va de négligeable à sensible (McGuinness et al., p. 3 ; Bailey et al., p. 23 et 24 ; Westphal et al., p. 1 ; Russinovich, p. 10).
5. Supposé : la taxe croît avec l'emploi, par la tâche, de ce qui est caché (hypothèse de Bailey et al., p. 24 ; un billet non vérifié).
6. Présente n'est pas lisible (« LEACE », p. 1, 8, 10 ; Chaudhary et Barez, p. 1 ; Westphal et al., p. 1 ; Bürger et al., p. 1).
7. Supposé : ce qui sépare le saboteur de l'honnête est l'usage d'un savoir partagé, donc une décision petite et déplaçable.
8. Les mâchoires peuvent être liées par le texte (Boxo et al., p. 1).
9. Sous renforcement, l'évasion passe surtout par la sortie (Gupta et Jenner, p. 8 ; Taufeeque et al., p. 1).
10. Des pas 2, 4 et 5 : l'étau se rend solide en élevant et en mesurant la taxe, donc en lisant ce que la tâche emploie ; du pas 6 : en lisant par intervention plutôt que par sonde.
11. Le pari par bandes va plus vite que la somme hors du pire cas et l'égale au pire cas ; le mélange garde la garantie [calcul].
12. Tailles exactes de la dissociation et du test apparié [calcul].
13. Supposé : en service, un oracle sur le produit et une référence valable existent, ou des témoins honnêtes pour le taux d'amélioration sous perturbation.

**Objets de contrôle déclarés.** Mécanisme « borne de l'étau » : là où « l'étau serre » doit être faux (taxe nulle, rappel nul), un retrait nul était attendu et rendu dans les douze cas ; là où c'est vrai (r = 1, κ = 1), un retrait positif sous la borne était attendu, rendu à 0,75. Un rappel mesuré seul « réussit » dans le monde à taxe nulle : comme mesure de l'étau, il est mort. Mécanisme « pari » : chez l'honnête, espérance du facteur attendue à 1 et trouvée à 1,000000, croissance négative (−0,01384) ; devant un dommage hors oracle, il se tait comme attendu ; devant le dommage planté, il croît. Le pari par bandes « réussit » plus vite sur un dommage proportionnel et n'y gagne rien au pire cas : comme promesse de délai, il est mort, d'où le mélange. Ce sont les objets de contrôle d'un argument, non d'une mesure.

**Premier pas non justifié, selon l'auteur.** Le pas 5. Le justifierait la taxe mesurée sur deux cibles au moins, l'une employée par la tâche et l'autre non, dans un volet d'attaque déclaré, avec l'ordre prédit scellé avant. Le pas 7 est le second : c'est un argument, sans pièce.

**Trouvailles de côté de l'auteur.** (1) La seconde moitié de la pince a un cousin empirique : sous renforcement, l'évasion d'une sonde passe par la sortie. (2) L'annexe d'une esquisse de dossier de sûreté décrit, en exemple fictif, « text-based monitoring » plus des sondes rendues orthogonales (Balesni et al., p. 45) : à verser à l'antériorité de la pince. (3) Des sondes signalent 99 % des exemples d'ajustements bénins (Soopal et al., p. 1) : tout lecteur réappris demande des témoins d'ajustement bénin. (4) Le moteur de recherche a attribué deux identifiants à de mauvais titres ; les titres retenus viennent de l'interface d'arXiv.

**Mise en garde de l'auteur.** La borne est vraie par construction et se lit bien, donc elle peut être bien jugée sans le mériter ; toute sa portée tient à une taxe que personne n'a mesurée sur des tâches d'agent ; les formes linéaires du calcul sont choisies par l'auteur ; les « chances » sont des jugements.

## Limites déclarées par l'auteur

- Aucune mesure, aucun résultat d'expérience lu ; les calculs supposent toutes leurs entrées et ne sont pas contre-lus.
- Aucun PDF lu en entier, aucune figure regardée ; presque tous les PDF ne sont lus qu'à la page 1. La pente de la taxe de Bailey et al. n'existe que dans une figure : elle n'est pas citée ; 34,8 % vient de la légende extraite en texte.
- Une pièce centrale non obtenue : « When Monitors Fail, the Model Still Knows » ; ce qui en est dit vient de la page de la conférence, lue par un outil qui résume.
- Recherche bornée : un moteur, en anglais ; ni Google Scholar, ni Semantic Scholar, ni OpenReview. « Non trouvé » n'est pas « libre ».

## Sources citées

- Emmons et al., « When Chain of Thought is Necessary, Language Models Struggle to Evade Monitors », arXiv 2507.05246v1.
- Bürger et al., « Chain of Thought Monitoring Can Fail Even When CoT Is Necessary », arXiv 2610.18105v1.
- Belrose et al., « LEACE: Perfect linear concept erasure in closed form », arXiv 2306.03819v4.
- Elazar et al., « Amnesic Probing: Behavioral Explanation with Amnesic Counterfactuals », arXiv 2006.00995v3.
- Russinovich, « What the Model Cannot See: Covert and Provable Text Invisibility in LLMs », arXiv 2610.15883v1.
- Rahman, Alouani, « Bypassing Prompt Injection Detectors through Evasive Injections », arXiv 2602.00750v2.
- Roy et al., « Detection Without Correction: A Robust Asymmetry in Activation-Based Hallucination Probing », arXiv 2604.13068v2.
- Tiwari et al., « Decodability is Not Causality: Dissociating Probe Readouts from Behavioral Drivers via SAE Decomposition », arXiv 2609.18080v1.
- Carlini, Wagner, « Adversarial Examples Are Not Easily Detected: Bypassing Ten Detection Methods », arXiv 1705.07263v2.
- Ribeiro et al., « On LLMs' Internal Representation of Code Correctness », arXiv 2512.07404v3 ; Ribeiro et al., « On the Robustness of LLMs' Internal Representation of Code Correctness », arXiv 2608.08266v1 (page 1 seule).
- Greenblatt et al., « Stress-Testing Capability Elicitation With Password-Locked Models », arXiv 2405.19550v1.
- Roger et al., « Benchmarks for Detecting Measurement Tampering », arXiv 2308.15605v5.
- Ghandeharioun et al., « Patchscopes: A Unifying Framework for Inspecting Hidden Representations of Language Models », arXiv 2401.06102v4.
- Karvonen et al., « Activation Oracles: Training and Evaluating LLMs as General-Purpose Activation Explainers », arXiv 2512.15674v2.
- Geiger et al., « Causal Abstractions of Neural Networks », arXiv 2106.02997v2.
- Bailey et al., « Obfuscated Activations Bypass LLM Latent-Space Defenses », arXiv 2412.09565v2.
- McGuinness et al., « Neural Chameleons: Language Models Can Learn to Hide Their Thoughts from Activation Monitors », arXiv 2512.11949v1.
- Tice et al., « Noise Injection Reveals Hidden Capabilities of Sandbagging Language Models », arXiv 2412.01784v3.
- Soopal et al., « Stress-Testing Sandbagging Detection Under Adaptive Attack », arXiv 2611.14950v1.
- Gupta, Jenner, « RL-Obfuscation: Can Language Models Learn to Evade Latent-Space Monitors? », arXiv 2506.14261v4.
- Taufeeque et al., « The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes », arXiv 2602.15515v2.
- Taylor et al., « Auditing Games for Sandbagging », arXiv 2512.07810v1.
- Clymer et al., « Poser: Unmasking Alignment Faking LLMs by Manipulating Their Internals », arXiv 2405.05466v2.
- Balesni et al., « Towards evaluations-based safety cases for AI scheming », arXiv 2411.03336v2.
- Westphal et al., « Now You (Still) See Me: Detecting Evasive Steganographic Payloads in LLMs », arXiv 2606.09411v1.
- Chaudhary, Barez, « Beyond Black-Box Obfuscation: Mechanistic Analysis and Defense of White-Box Monitors », arXiv 2505.14300v2.
- Aremu et al., « Adaptively Robust LLM Monitoring via Activation Watermarking », arXiv 2603.23171v3.
- Boxo et al., « Linear probes rely on textual evidence: Results from leakage mitigation studies in language models », arXiv 2509.21344v2.
- Athalye et al., « Obfuscated Gradients Give a False Sense of Security », arXiv 1802.00420v4.
- Waudby-Smith, Ramdas, « Estimating means of bounded random variables by betting », arXiv 2010.09686v7.
- Relus, non cités : Halawi et al., « Overthinking the Truth », arXiv 2307.09476v3 ; Belrose et al., « Eliciting Latent Predictions from Transformers with the Tuned Lens », arXiv 2303.08112v6 ; 2605.27958v1 ; 2507.12691v3 ; 2606.11998v1 ; 2603.04069v1.
- Pages web, non vérifiées : la page de la conférence ICML 2026 de « When Monitors Fail, the Model Still Knows: Probing Obfuscated Reasoning in LLMs » ; trois billets de forum (un modèle jouet de l'obscurcissement ; des modèles ajustés contre des sondes de sujet ; des lecteurs en langue naturelle face aux modèles « caméléons »).
