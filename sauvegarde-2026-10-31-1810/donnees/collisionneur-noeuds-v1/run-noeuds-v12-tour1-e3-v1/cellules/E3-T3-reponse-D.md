# Proposition D — tour III.3

Je réponds uniquement aux sections visant D. Statuts conservés : **[V]** vérifié, **[R]** rapporté, **[ONA]** observé-non-audité, **[H]** hypothèse. Les calculs numériques des critiques ne sont pas ré-audités ; je retiens leur direction lorsqu’elle est fondée, pas automatiquement leurs valeurs. Tout nouveau seuil chiffré est **illustratif** jusqu’à son gel. Le brouillon 6 du semi-réel n’étant pas servi, je n’en déduis rien.

## (a) Réponse aux critiques

### N1 — validation et fuite de rareté

- **A, B et C sur la circularité du test de contrastes : acceptées.** Le critère R4(iii) porte sur une erreur de code nommée et suppose les bras exécutés **[V]**. Il ne peut donc pas servir de porte V0. De plus, le déplacement produit par une permutation des concepts peut mesurer un signal légitime, non une fuite.
- **A et B sur la sensibilité : acceptées.** Mon montage ne permettait pas d’exclure un artefact plus petit que la demi-largeur d’un contraste. Je retire toute affirmation implicite d’absence d’artefact.
- **Correction** : séparer strictement la validation du générateur, avant invocation, du test de mécanisme, après invocation et dont la conséquence doit être écrite dans la v3. Aucun bras candidat n’est exécuté avant scellement.

### N3 — substitut Gu–Krenn

- **A sur la population absente et B sur l’absence d’effet minimal : acceptées.** « Ponts plantés vrais » n’avait pas de population définie pour ce substitut, et une borne basse de gain simplement supérieure à zéro ne définit pas une utilité.
- **Correction** : évaluation rétrospective sur apparition de liens, avec réglage et test sur fenêtres temporelles disjointes, et plus petit gain utile gelé avant le test. Cette épreuve mesure un classement de liens, pas une fertilité sémantique.

### N4 — profil du bras méta et lecteurs

- **A sur le balayage non gelé : acceptée.** Un balayage qui traverse le seuil de décision ne tranche rien.
- **B sur deux lecteurs d’accord sur une mauvaise niche : acceptée.** Kappa et Jaccard ne mesurent pas ce défaut systématique.
- **Correction** : famille de lois et règle de décision gelées avant calcul ; ajout d’un jeu étiqueté par une référence humaine, contenant des cas où les deux lecteurs peuvent partager la même erreur.

### N5 — boîte externe et non-lecture

- **A sur le rejeu impossible d’É5 : acceptée.** Les gardes d’É5 dépendent nécessairement des classes ; elles ne sont pas rejouables sur les seules consommations.
- **A sur le contenu du message : acceptée.** Déplacer la clé vers une autre session ne suffit pas : des comptes trop fins ou un ordre de sortie peuvent recréer un canal.
- **Correction** : distinguer les décisions de consommation, effectivement rejouables, des gardes d’É5, dont il faut borner la sortie et tester les artefacts de message.

### N6 — centrage, M1 et puissance

- **A sur « M1 encore informative » : acceptée.** Je nomme désormais les estimateurs : taux d’ensembles acceptés non vides, inclusion de C, inclusions de L/C⁰, et abstention sous H.
- **A sur Bθc : acceptée.** Une récupération de z₁ sous précondition violée n’est pas automatiquement fausse. Le contraste pertinent est apparié entre iVAE et M5, avec récupération des autres latentes et stabilité entre graines.
- **B sur la suspension de DL-12 : acceptée.** « Réécrire M1 » signifie réécrire sa **lecture dans le préenregistrement**, non modifier la méthode publiée. Si le test de résidu n’est pas concluant, DL-12 retourne à l’arbitre au lieu de rester implicitement acceptée.
- **C sur PUISθ : exigence acceptée, multiplicateur numérique non retenu.** La puissance doit être recalculée dans toute la zone de qualification, notamment à corrélation 0,70 **[R]**. Le facteur précis proposé par C repose sur une approximation de non-centralité non établie ici.

### N9 — B-i et cases appariées

- **A sur le changement de statut de B-i : acceptée.** B-i appartient à la conjonction du préenregistrement v2 servi **[V]**. Le rendre descriptif serait une modification du test décisif, à soumettre comme nœud distinct ; mon option (a) ne la présuppose pas.
- **A sur les cases vides : acceptée.** Une règle de regroupement ou de non-estimabilité doit être écrite avant lecture. Une aire non estimable ne peut être remplacée silencieusement par l’aire aléatoire.

### N10 — coût d’attaque et équilibre dégénéré

- **A sur la borne du coût : acceptée.** Une attaque trouvée fournit une borne **haute** du coût minimal, pas une borne basse **[V, pièce 22]**. L’échec d’une batterie ne conclut que sur cette batterie et ces budgets.
- **A et B sur la classe d’attaquants et les paramètres : acceptées.** Classe, budget de référence, budget maximal, taux de contournement, plancher d’utilité, fausse alerte et unité de coût doivent être gelés ; sans cela, pas de verdict.
- **C sur le biais de sélection : acceptée comme correction d’ambiguïté.** Aucune tâche ne sera retirée parce que les poids y sont purs. B′ est évalué sur toutes les tâches ; la dégénérescence est rapportée et restreint l’interprétation du mécanisme, non l’échantillon.

### N11 — retrait, puissance, transport et ponts plantés

- **A et C sur les contributions uniques : acceptées.** Exiger zéro vrai unique rendrait presque tout retrait impossible, y compris pour un bras bruité. La permutation des noms de bras et un bras fantôme uniforme deviennent obligatoires.
- **B sur la puissance : acceptée.** La formule ne répond pas seule à « combien ? ». Un pilote scellé doit estimer la variance appariée avant tout nombre de mondes.
- **B sur les deux régimes : acceptée sur le blocage pratique, pas sur une circularité logique nécessaire.** Deux régimes indépendants pourraient être mesurés ; mais j’enlève cette condition du **retrait local**. Elle ne concerne que la revendication de transport ou de retrait global.
- **A, B et C sur la marge et le transport : acceptées.** La marge sera fixée indépendamment des résultats, comme écart maximal toléré pour l’allocation. À huit fusions par bras **[R]**, aucune équivalence de transport ne sera revendiquée.
- **A sur les lecteurs : acceptée.** Leur sortie porte uniquement sur l’identité de la cible, jamais sur sa qualité ; elle doit être étalonnée sur des cas à réponse connue.
- **B et C sur les contrôles de plantation : acceptées.** J’ajoute paires chimères, pont inversé, cibles permutées et test unilatéral de mémorisation d’un parent tronqué.

## (b) Expériences corrigées

Dans tous les duels suivants, un intervalle dans la zone intermédiaire **falsifie la prédiction de puissance du plan** ; il ne produit pas de verdict scientifique.

### 1. N1 : deux étages non circulaires

**Avant invocation.** La v3 déclare les lectures, change explicitement V5 après nœud, utilise des graines nouvelles et conserve l’ancienne grandeur comme rapport sans seuil. Aucun N n’est exécuté.

- **H_A** : la plomberie visée par T2 est tenue, écart ≤ 0,5 **[R, seuil existant]**.
- **H_B** : elle ne l’est pas.
- T2 sous le seuil falsifie H_B ; au-dessus, H_A est falsifiée et l’arrêt est conservé. Ce test reste un contrôle presque acquis par construction : il ne valide pas les contrastes.

**Après l’invocation unique.** La v3 ajoute, avant scellement, un placebo \(P_{\mathrm{rar}}\) utilisant seulement la rareté observable de l’étiquette retenue, sans κ. Il est évalué sur tous les mondes, avec analyses stratifiées par type d’étiquette ; M_inertes, statuts permutés et \(N_{\beta0}\) sont les contrôles.

- **H_A** : N apporte au-delà de \(P_{\mathrm{rar}}\) un gain au moins égal à la marge gelée.
- **H_B** : \(P_{\mathrm{rar}}\) reproduit l’avantage et N ne le dépasse pas de cette marge.
- La première issue falsifie H_B ; la seconde falsifie H_A et interdit de lire le contraste comme gain conceptuel. Elle ne modifie rétroactivement ni V0 ni la validation.

### 2. N3 : population et effet utile

Population gelée : paires non reliées à \(t_0\), traits antérieurs à \(t_0\) ; positives reliées dans \((t_0,t_1]\), négatives encore non reliées à \(t_1\). Réglage sur une fenêtre antérieure, test sur une fenêtre disjointe ; appariement par degré, âge et strate ; permutation intra-strate.

- **H_A** : le substitut dépasse la meilleure base mécanique d’au moins \(\delta_{S31}\), plus petit gain jugé utile et gelé avant test.
- **H_B** : le gain est inférieur à \(\delta_{S31}\).
- Borne basse au-dessus de \(\delta_{S31}\) : H_B falsifiée. Borne haute au-dessous : H_A falsifiée. Bases : degré, âge, attachement préférentiel, Simpson et règle basique.

### 3. N4 : verdict conditionnel et lecteurs étalonnés

Une famille finie de lois, incluant les variantes défavorables déjà décrites **[R]**, et les tables corrigées sont gelées. Avec \(q=0,5\), **illustratif** :

- **H_A** : pour toute loi de la famille, \(P(\text{zéro paire dans le profil})\le q\).
- **H_B** : au moins une loi donne \(P>q\).
- Le maximum sur la famille tranche l’une ou l’autre. Ce verdict est conditionnel à la famille ; il ne prétend pas mesurer la loi des futures fiches réelles.

Séparément, un jeu à niches connues, validé par référence humaine, mesure exactitude des niches et structures, y compris les accords sur erreur. Un kappa élevé ne compense pas une exactitude insuffisante.

### 4. N5 : deux tests au lieu d’un rejeu unique

1. **Décisions de consommation** : rejeu strictement identique sur M7 seul.
2. **Aval d’É5** : à sortie gelée d’É5 et consommations identiques, les classes sont réétiquetées.  
   - **H_A** : aucune décision aval ne change.  
   - **H_B** : au moins une change.  
   Tout changement falsifie H_A ; aucun changement sur la batterie complète falsifie H_B pour les canaux testés.

La boîte ne rend que les booléens et comptes minimaux gelés, sans identifiants ni ordre de classe. Les artefacts incluent comptes trop fins, identifiants triés par classe, lecture hors journal et modification de l’ordre des appels. Un artefact non détecté falsifie la garde.

### 5. N6 et N9 : mesures rendues explicites

Pour DL-12, centrage et \(\kappa=1\) sont comparés à graines appariées. Sous \(\beta=0\), on mesure erreurs sur C/C⁰ par environnement et résidu de T1 ; pour M1, les quatre estimateurs nommés plus haut. **H_A** : tailles nominales restaurées et M1 encore informative ; **H_B** : résidu ou M1 non informative. Le nombre de graines est fixé par un pilote jouet mesurant la variance inter-graines ; si elle empêche le contraste, le résultat est non concluant.

PUISθ est évalué sur la zone complète de qualification. S’il est faux, la table d’estimation devient descriptive selon la règle écrite, sans ajournement indéfini.

Pour N9, B-i reste décisif sauf nouveau nœud. Les regroupements de cases sont fixés avant lecture ; une case sans témoin admissible rend B-ii non estimable et le test non concluant selon la règle amendée avant scellement.

### 6. N10 : courbe de coût trouvé, sans prétention au minimum

La classe comprend les optimiseurs locaux prévus et au moins un optimiseur indépendant, avec des budgets dépassant le budget de référence. Pour chaque budget, on mesure si une attaque satisfait conjointement contournement, utilité et fausse alerte, sur tâches honnêtes appariées en difficulté.

- **H_A** : aucun optimiseur de la batterie ne réussit dans le budget de référence.
- **H_B** : au moins un y réussit.
- Une réussite falsifie H_A. Une absence de réussite jusqu’au budget maximal falsifie H_B **pour cette batterie seulement**, sans borne basse sur le coût minimal universel. Une forte divergence entre optimiseurs donne « non concluant : optimisation ».

B′ est comparé sur toutes les tâches au meilleur moniteur unique et au « ou » déterministe. La pureté des poids est un résultat descriptif ; elle n’exclut aucune observation.

### 7. N11 : retrait local et transport séparés

**Pilote de variance.** Après scellement de la v3, sur mondes synthétiques indépendants, les trois règles de bras sont appliquées aux mêmes mondes et budgets. Le pilote estime \(\sigma_D\), avec grappes par monde ; pour les ponts réels, la grappe est la sous-session. Le nombre requis suit alors la formule appariée, avec effet minimal et confiance gelés. Sans ce pilote : « retrait non décidable ».

**Retrait local.** Il exige domination du rendement à coût comparable, fausses promotions non dégradées et intervalles séparés selon la règle gelée. Les uniques deviennent une grandeur secondaire, comparée à leur distribution sous permutation des noms de bras et à un bras fantôme uniforme. Ils ne sont plus une condition nécessaire. Le retrait global n’est pas déduit de ce seul régime.

**Transport.** La marge \(\delta_T\) est l’écart maximal de contraste jugé sans conséquence pour l’allocation, fixée avant lecture.  
- **H_A** : les contrastes sont équivalents entre régimes dans \(\delta_T\).  
- **H_B** : au moins un régime s’en écarte davantage.  
L’équivalence falsifie H_B ; un dépassement falsifie H_A ; un effectif insuffisant falsifie la puissance. La course 2 ne porte donc aucune preuve d’équivalence.

**Ponts plantés.** Outre leurres et cibles permutées : paires chimères incompatibles, pont inversé dont les deux parents sont postérieurs à la cible, et production à partir d’un seul parent tronqué pour détecter la récitation du second. La correspondance exacte/proche/surface/aucune reste aveugle ; les lecteurs sont étalonnés sur cas connus, et tout désaccord non résolu est non concluant.

## (c) Réponse à l’arbitre

**Établi.** La validation servie fait échouer V5 et le verdict R13 est non concluant **[R]** ; le diagnostic sur mondes d’essai explique des mécanismes plausibles mais reste **[ONA]**. La contradiction littérale A21/É5 est établie par les textes **[V]**. N-058 impose oracle planté et coût pour la composition, jamais le verdict de qualité du juge **[V]**. Chez Bailey et collègues, les extraits servis établissent localement un coût d’évasion et l’insuffisance d’OAT pour fermer l’attaque **[V]** ; leur transport à notre défense reste **[H]**.

**Non établi.** Que T2 préserve les contrastes ; que le substitut apporte un signal utile ; la fréquence réelle du profil méta ; la suffisance de l’aveugle v55 ; la puissance à corrélation 0,70 ; la supériorité du coût d’attaque sur son gain ; enfin tout classement transportable des bras. La course 2, à elle seule, ne peut pas établir ce transport.

**Expérience à faire en premier : la validation v3 de N1**, scellée, sur graines nouvelles, avec T2 comme contrôle limité, l’ancienne V5 en rapport, et le placebo rareté déjà préenregistré pour l’invocation ultérieure. Elle lève d’abord la porte sans exécuter N prématurément, puis permet de tester proprement le mécanisme qui fonde N11. Les ponts plantés du pré-pilote restent subordonnés à une annexe de plomberie ; ils ne doivent ni retarder cette validation ni servir à comparer les bras avant que puissance et correspondance soient démontrées.

FIN-DE-CELLULE