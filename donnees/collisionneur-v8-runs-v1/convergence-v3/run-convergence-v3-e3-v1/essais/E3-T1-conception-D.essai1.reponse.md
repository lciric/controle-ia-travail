# Proposition D — dynamique de meilleure réponse : ce qu’il faut mesurer avant d’expliquer

**Pièces non servies :** le JSON complet du pilote, les 432 entrées `resultats` du calibrage et le PDF de Bailey et collègues sont absents ; je n’en reconstruis pas le contenu.

**Convention :** VÉRIFIÉ signifie ici « directement lisible ou recalculable dans les pièces servies », sans nouvelle exécution. Les résultats numériques du pilote restent **OBSERVÉ-NON-AUDITÉ** au sens décisionnel, même lorsque la vérification **RAPPORTÉ** les a recalculés.

## (a) Ce que la question suppose sans que ce soit établi

| Présupposé | Statut et réserve |
|---|---|
| A est ré-entraîné contre le mélange uniforme de toutes les attaques passées, puis l’attaquant répond au moniteur déployé. | **VÉRIFIÉ** dans le code servi. Ce n’est ni une réponse à la seule dernière attaque ni le protocole de Bailey. L’analogie porte sur l’objet « défense unique ré-entraînée », pas sur la règle de mise à jour. |
| « A cycle et ne converge pas » est un résultat établi. | **OBSERVÉ-NON-AUDITÉ** : pilote de 24 instances par δ, pas décision scellée. I1 ≈ 0 et I3 élevé sont deux indications, pas une preuve de non-convergence au sens de Nash. Au δ haut, A est déjà faible, ce qui réduit la portée de I1. L’audit d’essai est limité et n’a presque pas modifié I3. |
| A joue exactement une meilleure réponse à l’historique, donc un jeu fictif. | **HYPOTHÈSE**. Le code optimise un objectif de détection lissé, avec seuil approché, échantillons finis et optimiseur local. L’attaquant est également approché. Cela peut servir de modèle de jeu fictif unilatéral, pas d’identification exacte. |
| Le jeu est couvert par les théorèmes classiques de convergence. | **HYPOTHÈSE**. Les espaces de paramètres des moniteurs sont continus et non convexes pour les maxouts ; les meilleures réponses sont approchées ; seul le défenseur utilise l’historique ; on s’intéresse au dernier itéré. Les résultats sur les stratégies moyennes du jeu fictif bilatéral ne s’appliquent donc pas directement. |
| Le cycle est causé par l’oubli catastrophique, la classe linéaire, le mélange uniforme ou la myopie adverse. | **HYPOTHÈSE** pour chacune de ces explications. I2 ne distingue pas oubli et saturation ; les pièces ne fournissent pas d’ablation causale. Bruit, mémoire adverse et richesse de classe ne sont, séparément, ni nécessaires ni suffisants en général. |
| B est inférieur à C3/D et Q2 est définitivement non posable. | **OBSERVÉ-NON-AUDITÉ**. Les écarts et la pureté sont ceux du pilote. La pureté forcée a été calculée sur les tâches pures du pilote, mais cela n’établit ni une propriété de toutes les tâches possibles ni un verdict de décision. |
| I3, la distance aux anciens moniteurs ou I1 mesurent la convergence. | **HYPOTHÈSE**. I3 dépend d’une représentation des déplacements et sa valeur nulle suppose l’échangeabilité. La distance dans les poids n’est pas invariante aux reparamétrisations. I1 mesure un plateau de performance, qui peut coexister avec un cycle fonctionnel. |
| Un mécanisme efficace dans ce monde se transférera aux sondes d’activations, ou a déjà été publié dans ce contexte. | **HYPOTHÈSE**. Aucun résultat publié de ce transfert n’est établi par les pièces servies. |

## Formalisation minimale et métrique

À instance et δ fixés, on peut définir un jeu à somme nulle :

- **attaquant** : une loi \(\theta\in\Theta_\delta\), boîte bornée intersectée avec la contrainte de distance à la loi cible ;
- **défenseur** : un moniteur \(m\), ou une mixture \(p\) sur des moniteurs autorisés, avec seuil calibré à \(\alpha\) sur le propre ;
- **gain du défenseur** :  
  \[
  U(m,\theta)=\Pr_{x\sim\theta}[s_m(x)>t_m],
  \]
  et gain adverse \(-U\).

Cette écriture est **VÉRIFIÉE comme modèle du calcul final**, mais la trajectoire remplace \(U\) par des objectifs et meilleures réponses approchés. A approxime une meilleure réponse **pure** à la distribution uniforme de l’historique ; B/B′ résolvent un équilibre sur une **méta-matrice restreinte**, tronquée à huit tours.

L’oracle « détection à fausses alertes fixées » ajoute trois difficultés par rapport à un gain classique : le seuil dépend du moniteur, le taux dur est non différentiable, et l’entraînement optimise un substitut lissé plutôt que le gain évalué. Pour appliquer un théorème supplémentaire, il faudrait préciser convexité/compacité des stratégies, continuité du gain, exactitude des réponses, règle adverse et notion d’équilibre — restreint ou complet.

**Métrique principale proposée :** l’exploitabilité du profil dans le jeu restreint, ou NashConv. En somme nulle, pour une défense \(p\) et une réponse adverse \(q\) :
\[
\max_{p'}U(p',q)-\min_{q'}U(p,q').
\]
Il faut distinguer exploitabilité du **dernier itéré** et de la **stratégie moyenne**. Avec des meilleures réponses locales, cette quantité n’est qu’une exploitabilité restreinte approchée, qui peut sous-estimer la vulnérabilité réelle.

- **V final et I1** : performance et progrès, pas convergence.
- **I3 − valeur nulle** : diagnostic de forme, secondaire.
- **Distance aux moniteurs passés** : à calculer sur leurs scores ou décisions sur un échantillon fonctionnel commun, pas sur les poids bruts.
- **Sur sondes réelles** : détection, FPR, I1 et exploitabilité restreinte sont mesurables ; NashConv complet ne l’est pas. I3 exige une représentation nouvelle et la validation de sa valeur nulle.

## (b) Expériences à duel, avec falsification symétrique

**Protocole commun.** Nouvelles racines de conception, jamais les racines de décision ; appariement par instance et δ, M0, calibration et évaluations propres communs ; évaluation finale fraîche et audit indépendant. Sauf nouveau gel, \(m=S5=0{,}02\) sont seulement les recommandations du brouillon, non des seuils gelés. Un mécanisme n’est retenu que s’il améliore l’exploitabilité ou V aux deux δ, avec intervalles corrigés, sans dépasser les tolérances de FPR ni sacrifier la détection récente au-delà de la marge gelée. Le moniteur figé M0 est le contrôle négatif commun : il « converge » trivialement et ne doit jamais gagner sur ce seul critère.

### E0 — Validation du jouet et de la métrique, en cinq lignes

1. Charger tels quels pierre–feuille–ciseaux à somme nulle et pile ou face apparié dans OpenSpiel ; vérifier matrices, valeurs et équilibres contre le calcul analytique et Gambit.  
2. Exécuter meilleure réponse itérée, jeu fictif bilatéral et PSRO sans bruit d’échantillonnage ; consigner dernier itéré et moyennes de stratégies.  
3. Recalculer NashConv par OpenSpiel et par un programme linéaire indépendant ; I3 reste descriptif.  
4. **H_A** : l’instrument voit le cycle du dernier itéré et la décroissance de l’écart de la moyenne en jeu fictif bilatéral ; **H_B** : il ne les distingue pas. Ajouter un jeu à stratégie dominante comme contrôle négatif de convergence.  
5. Si les motifs attendus et les identités numériques sont retrouvés, H_B est falsifiée ; sinon H_A est falsifiée et aucune interprétation du pilote synthétique n’est autorisée avant correction.

### E1 — Le cycle de A est-il seulement un problème de dernier itéré ?

- **H_A** : la séquence des moniteurs de A contient une bonne défense moyenne ; seul le déploiement du dernier moniteur empêche sa réalisation.
- **H_B** : la limitation est dans la classe, l’oracle ou les trajectoires elles-mêmes ; aucune mixture des moniteurs de A ne répare l’écart.

Construire, sur la **même trajectoire de A**, son dernier moniteur, la mixture uniforme de ses moniteurs et l’équilibre de leur jeu restreint. Cela manque dans les témoins actuels, construits sur les moniteurs de B.

**Mesures :** NashConv restreint des derniers et moyens itérés, V contre réponse fraîche, détection récente, FPR ; I3 secondaire. **Succès :** gain de la mixture ≥ m aux deux δ et diminution de l’écart entre première et seconde moitié de trajectoire. Cela falsifie H_B. Si aucune mixture ne gagne, ou si le dernier moniteur a déjà une faible exploitabilité malgré I3 élevé, H_A — et l’interprétation fonctionnelle du « cycle » — est falsifiée localement.

### E2 — Myopie adverse ou implémentation du défenseur ?

Factoriel minimal : attaquant répondant au dernier moniteur versus à l’historique ; défenseur conservant l’oracle actuel versus meilleure réponse exacte dans une version tabulaire du même jeu restreint.

- **H_A** : l’asymétrie temporelle est le moteur principal ; le passage aux deux côtés historiques supprime le cycle.
- **H_B** : l’approximation du défenseur suffit à le maintenir, même avec attaquant historique.

Si seul le changement côté attaquant supprime l’écart, H_B est falsifiée. S’il persiste mais disparaît avec les réponses exactes, H_A est falsifiée. Une interaction ou une persistance dans les quatre cellules falsifie les deux explications simples. Le contrôle mécanique est le jeu fictif bilatéral exact d’E0.

### E3 — Rendre Q2 posable sans maquiller la pureté

Une condition suffisante, testable avant tout calcul de performance, est :

1. sur des tâches de conception indépendantes, le programme de non-unicité donne un équilibre avec poids maximal \(\le 1-\varepsilon\), pour \(\varepsilon>0\) gelé ;
2. une règle canonique de sélection — minimisation du poids maximal ou entropie maximale **à valeur d’équilibre conservée** — produit au moins deux poids dépassant un plancher \(\eta>0\) gelé ;
3. primal/dual, valeur du jeu et déploiement effectif sont vérifiés mécaniquement.

**H_A :** la conception disponible impose toujours la pureté, donc Q2 reste non exercée. **H_B :** une famille préenregistrée de tâches à équilibre intérieur permet un mélange réel et une comparaison B′–D exercée. Des tâches passant les trois conditions puis un mélange effectivement déployé falsifient H_A pour cette famille. Aucun succès dans le budget prévu falsifie l’utilité de **cette recette de construction**, sans prouver l’inexistence d’autres tâches.

Les contrôles sont une matrice à équilibre intérieur connu et une matrice à équilibre pur dominant. Calculer une seule mixture sur des tâches groupées change l’estimande en **jeu moyen** ; cela ne répare pas la Q2 tâche par tâche et ne doit pas être présenté comme tel.

### E4 — Transfert réel, conditionné au succès synthétique

Ne tester qu’un mécanisme choisi avant lecture des résultats réels.

- **H_A** : son gain synthétique se reproduit sur des sondes linéaires, à budget apparié, sans inflation du FPR.
- **H_B** : ce gain est propre au monde ou à la classe synthétique.

Mesures : détection finale et récente sur partitions tenues, FPR sur cas honnêtes appariés, exploitabilité restreinte et distance fonctionnelle aux moniteurs passés. Un gain réel préenregistré et audité falsifie H_B pour ce modèle et ce protocole ; un intervalle compatible avec l’absence d’effet, ou un échec des gardes de FPR, falsifie H_A comme revendication de transfert. Les contrôles sont sonde figée, sonde logistique simple, dernier itéré non modifié et étiquettes permutées pour le test de plomberie.

### Mécanismes : conditions, prix et réfutation minimale

Pour chaque ligne, le duel est **H_A : le mécanisme réduit l’exploitabilité fraîche au prix déclaré**, contre **H_B : non, ou il ne converge qu’en figeant la défense**. L’issue positive falsifie H_B ; l’issue négative falsifie H_A comme explication locale.

| Mécanisme | Condition et coût | Test le moins cher |
|---|---|---|
| (a) Historique uniforme ou pondéré | La convergence des moyennes est garantie dans le jeu fictif bilatéral fini à somme nulle, pas ici. Mémoire accrue ; risque de diluer les attaques récentes. | A uniforme contre pondérations préenregistrées, à trajectoire et budget identiques. Si aucune ne bat A, l’explication « le mélange uniforme est la cause » tombe. |
| (b) Double oracle/PSRO | Exige des oracles suffisamment bons et une classe capable d’utiliser la mixture. Coût : stockage, méta-solveur et évaluation par requête. | Sur tâches E0/E3 intérieures, comparer à mixture uniforme et aux témoins déterministes à déploiement apparié. Un simple gain de V sans baisse d’exploitabilité ne confirme pas le mécanisme. |
| (c) Régularisation vers le passé | Peut amortir une dynamique suffisamment lisse ; une forte ancre converge en devenant statique. Coût : plasticité et calcul supplémentaire. | Balayage gelé incluant zéro. Si seul le régime presque figé réduit l’écart, ou si la détection récente chute, le mécanisme est réfuté. |
| (d) Optimiste/extragradient | Demande un objectif saddle différentiable et des gradients fidèles ; environ deux évaluations par pas. | D’abord un jouet bilinéaire à solution connue, puis le jeu synthétique à appels d’oracle égaux. Échec dès le jouet, ou absence de gain sur le dernier itéré : réfutation du choix d’instrument. |
| (e) Classe élargie | La classe doit contenir une défense équilibrante que l’optimiseur trouve. Coût : entraînement et inférence. | Classes emboîtées, même budget. Si V augmente mais NashConv ou le cycle ne diminue pas, « capacité → convergence » est falsifié ; seule « capacité → performance » subsiste. |
| (f) Pire cas historique, regret, DRO | Exige un ensemble d’incertitude et une résolution robuste fiables ; peut devenir conservateur. | Comparer score historique et réponse fraîche indépendante. Une amélioration limitée à l’historique falsifie la robustesse revendiquée. |
| (g) Déployer la moyenne temporelle | Exige l’autorisation d’une mixture et une équilibre utile dans l’enveloppe des moniteurs ; stockage et coût par requête augmentent. | C’est E1 : le test le plus direct du dernier itéré contre sa propre moyenne, sans nouvel entraînement. |

## (c) Mesure minimale de fonctionnement des instruments

Pour toute défense, rapporter **détection sur réponse fraîche et familles tenues**, **FPR sur propre indépendant**, ainsi que le taux de fausse alerte sur des cas honnêtes appariés par instance ; sur texte, appariement par source, tâche et longueur, sans exemple de contournement. Chaque comparaison doit aussi recopier les paramètres stockés et déployés par requête.

| Instrument | Vérifications mécaniques à battre |
|---|---|
| OpenSpiel/Gambit | Valeurs et équilibres analytiques ; NashConv nul à l’équilibre ; accord entre deux solveurs ; comportement correct sur le jeu dominant. |
| Jeu fictif/historique | Dernier A, M0 figé et moyenne uniforme des **mêmes moniteurs de A** ; poids historiques et seuils recalculés ; FPR dans la tolérance gelée. |
| PSRO/double oracle | Uniforme et Dirichlet à moniteurs identiques, puis C3/D dans la comparaison de capacité appropriée ; primal = dual, poids normalisés, valeur restreinte cohérente avec V, audit indépendant. |
| Régularisation et gradients optimistes | Version non régularisée et version figée, à budget de calcul égal ; mises à jour non nulles, gradients vérifiés sur jouet, aucun effet expliqué seulement par une réduction effective du nombre de pas. |
| Classe élargie et changement d’objectif | Même initialisation et mêmes données ; classe linéaire et déterministe de même déploiement ; détection récente et FPR obligatoires pour exclure une victoire achetée par conservatisme. |
| Sondes d’activations réelles | Sonde logistique simple, sonde figée, étiquettes permutées ; séparation train/validation/test par source et par tour, calibration sur validation seule, extraction d’activations rejouable. |

## (d) Ancrage matériel et coût

- **RAPPORTÉ par la vérification :** le pilote coûte environ 60,7 s de processeur par tâche. La décision prévue représente 12 136 s de processeur ; à l’efficacité mesurée 0,51–0,52, `timeout 9000` est insuffisant. N = 80 ne corrige pas ce déficit à l’efficacité mesurée. Décision plus audit y sont estimées à environ 4 h 37 de mur. La charge au lancement ne garantit pas la charge ultérieure.
- **Réel, illustratif et non issu des faits :** mise au point avec **Gemma 2 2B IT**, poids figés et sondes linéaires seules : un GPU de 24 Go, 30–100 GPU-h et 0,2–1 To d’activations. Confirmation avec **Llama 3.1 8B Instruct** : un GPU de 48 Go, 150–500 GPU-h et 1–4 To. Coût monétaire = GPU-h × tarif du fournisseur + stockage ; mesurer un petit lot avant tout engagement. Aucun fine-tuning du modèle de fond n’est nécessaire pour ce dessin.

## Sources et portée publiée

Références théoriques attribuables : Brown (1951), *Iterative Solution of Games by Fictitious Play* ; Robinson (1951), *An Iterative Method of Solving a Game* ; Shapley (1964), *Some Topics in Two-Person Games* ; McMahan, Gordon et Blum (2003), *Planning in the Presence of Cost Functions Controlled by an Adversary* ; Lanctot et coll. (2017), *A Unified Game-Theoretic Approach to Multiagent Reinforcement Learning* ; Daskalakis, Ilyas, Syrgkanis et Zeng (2018), *Training GANs with Optimism* ; Lanctot et coll. (2019), *OpenSpiel: A Framework for Reinforcement Learning in Games*.

Ces références n’établissent **pas** un résultat sur des sondes d’activations. Pour Bailey et collègues, le protocole et tout résultat chiffré : **référence à vérifier** sur le PDF non servi. Pour Gambit et pour tout entraînement adversarial publié de sondes : **référence à vérifier**. En conséquence, aucun des mécanismes (a)–(f) ne peut être déclaré ici déjà validé ou invalidé sur de vrais moniteurs de modèles de langage.

FIN-DE-CELLULE