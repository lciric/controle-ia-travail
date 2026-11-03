Les chiffres du billet restent **RAPPORTÉS** via les pièces ; les remarques ci-dessous sont des critiques de méthode, sans résultat nouveau.

Pour alléger les conditions probabilistes : \(Y\) désigne la faute selon un oracle indépendant, \(S\) le score d’un moniteur, \(\tau\) son seuil, \(g\) le caractère et \(k\) la classe de faute. On note \(C_g(\tau)=P(S>\tau\mid Y=1,g)\) et \(\alpha_g(\tau)=P(S>\tau\mid Y=0,g)\). Les trajectoires d’une même exécution ne constituent pas des réplications indépendantes.

## Sur la proposition A

### (a) Défauts de méthode

- **C1 peut devenir circulaire.** Si la « triche par réécriture des tests » est étiquetée à partir du même diff que celui qui sert de détecteur mécanique, sa sensibilité est proche de un par construction. Le diff mesure une modification, pas nécessairement une faute ; les tests cachés mesurent un échec sur leur distribution, pas toutes les fautes. Les deux vérifications ne couvrent donc ni le même estimand ni nécessairement la même population que les moniteurs.
- **C2 conditionne sur des variables post-traitement.** Caractère, taux de faute, classe, silence et stade d’apparition sont liés. Comparer \(P(\text{capture}\mid Y=1,g,k)\) sans population cible commune mélange effet du caractère, sélection des fautifs et composition des tâches. Le nombre de trajectoires par cellule ne répare pas la dépendance interne à chaque graine.
- **C3 reste sous-spécifié causalement.** Tant que le croisement points de départ distillés × graines de renforcement n’est pas préenregistré, variance de distillation et variance de renforcement peuvent rester aliénées. Ses deux régions de résistance ne couvrent pas tous les résultats possibles.
- **C4 risque une fuite calibration–évaluation.** Un seuil estimé puis présenté comme ayant le taux nominal sur les mêmes épisodes honnêtes atteint presque ce taux par construction. Le recalibrage par caractère change également le point de fonctionnement : une variation de capture ne suffit pas à distinguer équité et simple translation du seuil.
- **D5 ne sépare pas ses deux causes.** Commentaire et silence peuvent agir simultanément. L’ablation peut produire un texte hors distribution ; le raisonnement franc greffé peut fournir presque directement l’étiquette à prédire. Enfin, le commentaire ayant été repéré en lisant des ratés, réutiliser les mêmes épisodes pour l’hypothèse et son évaluation constitue une double utilisation des données.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **C1 :** avec un détecteur mécanique \(M\), si \(P(M=1\mid Y=1,K=k)\simeq0\) pour une masse non nulle de classes \(k\), sa capture globale est bornée par sa couverture, quel que soit le nombre d’épisodes. Si \(Y\) est défini par \(M\), \(P(M=1\mid Y=1)=1\) par construction.
- **C2 :** pour une standardisation \(C_g^w=\sum_k w_kC_{gk}\), le paramètre n’est pas identifiable dès qu’il existe \(k\) tel que \(w_k>0\) mais \(P(K=k\mid Y=1,g)=0\). Le même défaut vaut en ajoutant silence, tâche ou stade.
- **C3 :** dans un modèle hiérarchique avec variance entre points de départ \(\sigma_D^2\), un grand \(\sigma_D^2\) relativement à l’effet de caractère laisse l’estimateur dominé par quelques distillations. Avec une probabilité de résistance faible et peu d’exécutions indépendantes, zéro événement observé laisse un intervalle supérieur non nul : les duels restent indécis.
- **C4 :** si le nombre effectif d’honnêtes indépendants est faible, la variance du quantile \(\hat\tau_g\) se propage à \(\hat C_g\). Sur les données de calibration, \(\hat\alpha_g\) est mécaniquement proche de sa cible et ne valide pas le taux futur.
- **D5 :** si les issues des moniteurs avant/après ablation sont rarement discordantes, la différence appariée a une variance trop grande relativement à l’effet testé. Si \(\alpha_{\text{ablatif}}\neq\alpha_{\text{original}}\), la variation de capture mélange effet textuel et déplacement du taux de fausses alertes.

### (c) Contrôles négatifs dont l’absence serait fatale

1. **Pour C1 :** fautes étiquetées sans le diff, modifications légitimes de tests et classes de fautes hors portée mécanique. Sans eux, ni sensibilité ni utilité comparative ne sont interprétables.
2. **Pour D5 :** ablations témoins de même longueur, position et syntaxe, avec action et verdict mécanique inchangés, puis évaluation sur épisodes non utilisés pour découvrir le commentaire. Le seul commentaire anodin inséré chez des honnêtes ne contrôle pas l’artefact d’ablation.
3. **Pour C3–C4 :** contrastes entre points de départ d’un même caractère et calibration/évaluation honnêtes disjointes. Le caractère neutre comme seul témoin n’est pas un contrôle négatif de la distillation.

## Sur la proposition B

### (a) Défauts de méthode

- Le calcul exact invoqué pour la résistance est **conditionnel à un total observé de résistances**. Ce n’est pas sans précision la loi nulle non conditionnelle « probabilité commune de résistance » ; les deux tests n’ont pas le même niveau.
- **Duel 1 :** B améliore A par un placebo et un recalibrage, mais « commentaire » et « forme/silence » ne sont toujours pas des hypothèses exclusives. Le retrait aléatoire d’autres lignes ne reproduit ni la position ni la fonction syntaxique du commentaire. La mesure limitée à une graine ne fournit qu’une réplication d’entraînement.
- **Duel 2 :** une forte proportion de fautes sans modification des tests ne démontre pas, à elle seule, un faible rappel mécanique chez les anti-triche : cela dépend de la population sur laquelle le rappel est moyenné. L’intégrité des tests peut aussi devenir l’étiquette et le prédicteur simultanément.
- **Changement 3 :** rendre les tests non modifiables change aussi les récompenses accessibles, la difficulté et la distribution des fautes. La persistance du silence ne peut alors être attribuée à la seule disponibilité de la classe.
- **Changement 5 :** « triche franche, donc attrapée » ne suit pas des résultats rapportés, eux-mêmes confondus par classe. Aucune métrique, population fautive commune ni règle de décision n’est fournie pour ce bras.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **Résistance :** sous \(p_g=p\), la loi conditionnelle au nombre total de succès diffère de la loi binomiale non conditionnelle. Avec \(p_g\) proche de zéro et peu d’exécutions, les intervalles de \(p_a-p_n\) peuvent contenir simultanément les deux régions de décision.
- **Duel 1 :** si les paires de scores originaux/ablatés sont presque toujours concordantes, l’estimateur apparié perd sa puissance. Si les lois honnêtes ablatées diffèrent selon le caractère, un seuil commun recalibré sur le mélange laisse des \(\alpha_g\) inégaux.
- **Duel 2 :** si \(P(M=1\mid Y=1,g,k)\) varie avec \(k\) et que les lois \(P(K=k\mid Y=1,g)\) ne se chevauchent pas, aucun rappel global standardisé n’est identifiable.
- **Changement 3 :** si \(P(K=k\mid Y=1,g,e)\) dépend fortement de l’environnement \(e\), le contraste de silence conditionnel aux fautifs compare deux lois de sélection différentes ; il n’est pas transportable sans support commun.
- **Juge du silence :** si l’étiquette humaine et le score lexical dérivent des mêmes mentions explicites, leur accord estime surtout la reproductibilité de cette règle, non la validité d’une intention de dissimulation.

### (c) Contrôles négatifs dont l’absence serait fatale

1. **Duel 1 :** transformations témoins syntaxiquement appariées et épisodes d’évaluation séparés de ceux ayant servi à construire le retrait.
2. **Changement 3 :** environnement témoin subissant la même modification matérielle sans changer les permissions pertinentes, avec lois de récompense et de difficulté comparées. Sans lui, classe et environnement restent confondus.
3. **Inoculation :** cadrage verbal placebo et comparaison à population de fautes standardisée. Sans cela, un changement de verbalisation ou de compétence peut simuler l’effet recherché.

## Sur la proposition C

Pièce absente, déclarée jamais lancée ; je n’en invente pas le contenu.

## Sur la proposition E

### (a) Défauts de méthode

- **A standardise sur des médiateurs.** Classe de faute et stade d’entraînement peuvent être des effets du caractère. Les standardiser estime un contraste direct dans une population choisie, pas l’effet total du caractère ; les publier avec le taux inconditionnel de fautes non détectées ne suffit pas à rendre les deux estimands équivalents.
- **B identifie un effet sur le moniteur, pas l’effet naturel du silence.** E le reconnaît partiellement, mais ces contrefactuels ne peuvent pas confirmer à eux seuls l’interprétation causale de l’entraînement. Si les gabarits d’annotation sont construits après inspection des scores ou des ratés du même échantillon, il y a fuite instrument–évaluation.
- **C impose une partie de son résultat.** La calibration séparée force les taux de fausses alertes nominaux à être égaux ; elle ne démontre donc pas que les caractères sont également difficiles. La réduction de l’écart de capture peut provenir uniquement des quantiles honnêtes, sans changement de la loi des fautes.
- **D comporte une fuite potentielle entraînement–évaluation.** Si le correcteur protégé et l’oracle final partagent règles ou classes, la branche protégée est entraînée contre l’instrument qui la note. De plus, correcteurs original et protégé peuvent différer par sévérité et récompense honnête, pas seulement par vulnérabilité.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **A :** si les poids de standardisation dépendent de \(g\), les estimateurs visent des paramètres différents. Si le support des classes ou stades est disjoint, l’écart standardisé n’est pas identifiable. La puissance dépend du nombre de points de départ et de leur variance, non du nombre de trajectoires.
- **B :** soit \(S(t)\) le score sous annotation \(t\). Si \(P(S(1)>\tau\neq S(0)>\tau)\) est proche de zéro, peu de paires discordantes informent l’estimateur. Si les lois des textes synthétiques dépendent de \(S\) ou ont été ajustées sur l’échantillon d’évaluation, l’effet estimé n’est plus celui d’une intervention fixe.
- **C :** soient \(F_g\) et \(G_g\) les lois des scores honnêtes et fautifs. Si \(G_g=F_g\), alors, à seuil calibré sur \(F_g\), \(C_g=\alpha\) : la calibration ne crée aucun pouvoir discriminant. Des quantiles honnêtes très différents peuvent aussi produire une réduction de capture sans aucune différence résiduelle de détection conditionnelle.
- **D :** si l’oracle \(O\) satisfait \(P(O=1\mid Y=1,b,k)=0\) sur les classes où les branches \(b\) divergent, la réduction observée est nulle même pour une réduction réelle non nulle. Avec peu de branches indépendantes et une forte variance inter-exécutions, l’intervalle de l’effet reste non tranchant.

### (c) Contrôles négatifs dont l’absence serait fatale

1. **B :** gabarits gelés sur des données distinctes, textes naturels intacts et validation que seule l’information visée change. Les modifications de longueur comparable déjà prévues ne suffisent pas contre cette fuite.
2. **C :** permutations des caractères à l’intérieur de strates de tâche et de stade, appliquées à toute la procédure de calibration et de capture. Les seules partitions honnêtes ne contrôlent pas la sélection de la population fautive.
3. **D :** branche témoin où les deux correcteurs sont identiques, plus un troisième oracle et des classes d’évaluation absentes de la construction du correcteur. Sans eux, randomisation, récompense et métrique restent confondues.

FIN-DE-CELLULE