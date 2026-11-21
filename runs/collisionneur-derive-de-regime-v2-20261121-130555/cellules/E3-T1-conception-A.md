# Proposition A — Tour III.1

**Pièces.** Les blocs FAITS et QUESTION sont présents et ne paraissent pas coupés. Je ne peux pas attribuer la référence « CURA » (auteurs et titre me sont inconnus) : **référence à vérifier**. Conformément à la règle 3, je ne donne aucun identifiant arXiv ; les travaux sont cités par auteurs, année et titre, de mémoire.

**Convention.** « CALCUL » désigne une dérivation que je fais ici, vérifiable à la main. Les n et les taux qui y entrent sont **illustratifs** : les faits disent seulement « quelques centaines ».

---

## (a) Ce que la question suppose sans que ce soit établi

| # | Supposition | Statut |
|---|---|---|
| S1 | Le taux réel triple sous changement de régime | RAPPORTÉ (CURA). Le programme ne le tient pas pour acquis sans la page lue. Dans les mondes plantés, le triplement est une propriété de construction, pas une observation. |
| S2 | Le triplement vient du changement de régime et non du bruit d'étalonnage | HYPOTHÈSE. Voir le CALCUL du §1 : le bruit seul produit un doublement dans environ 6 % des tirages. |
| S3 | La cible à tenir est 1 % de fausses alertes, et non un budget de relecture | HYPOTHÈSE |
| S4 | Il existe une correction qui conserve un seuil fixe | HYPOTHÈSE |
| S5 | Le régime est observable au moment du test | HYPOTHÈSE. C'est plausible pour la tâche, la version et la longueur, douteux pour la « source bénigne ». |
| S6 | On dispose en déploiement d'épisodes sûrement honnêtes pour ré-étalonner | HYPOTHÈSE. Le flux de déploiement est un mélange non étiqueté. |
| S7 | Une garantie « de long terme » est celle dont le programme a besoin | HYPOTHÈSE. Elle porte sur une fréquence d'alertes dans le temps, pas sur le taux chez les honnêtes d'un régime. |
| S8 | Le jumeau honnête est échangeable avec l'agent honnête | HYPOTHÈSE. Les faits disent l'écart « fragile ». |

---

## 1. Ce qu'un expert ferait sans qu'on le demande

**1.1 Mesurer le bruit du seuil avant d'accuser la dérive.** Un seuil placé sur la k-ième statistique d'ordre de n scores honnêtes échangeables a un taux réel de loi Beta(n+1−k, k). C'est un résultat classique (Wilks 1941, « Determination of sample sizes for setting tolerance limits » ; Vovk 2012, « Conditional validity of inductive conformal predictors »).

CALCUL, n = 300 illustratif :
- Le seuil à 1 % est le 3ᵉ plus grand score. Le taux réel suit Beta(3, 298), de moyenne 1,0 % et d'écart-type 0,57 %.
- P(taux réel ≥ 2 %) ≈ 6 % ; P(taux réel ≥ 3 %) ≈ 0,6 %.

Un triplement est donc rarement du bruit pur, mais un doublement l'est souvent. Toute mesure d'« effet de dérive » doit être lue contre cette bande.

**1.2 Vérifier que 1 % est certifiable.** Pour certifier un taux ≤ α avec confiance 1−δ, même en prenant le maximum comme seuil, il faut (1−α)ⁿ ≤ δ.

CALCUL, δ illustratifs : n ≥ 230 pour δ = 10 % ; n ≥ 299 pour δ = 5 %.

Avec quelques centaines d'épisodes, le programme est à la limite de ce qui se certifie sans aucune dérive. Toute stratification fait passer chaque strate sous cette limite. C'est un trilemme : quantile extrême, petit n, non-stationnarité. On ne tient pas les trois.

**1.3 Décomposer l'excès.** L'écart de taux entre régimes se décompose en deux termes (décomposition de type Kitagawa) :
- composition : Σ_g (π′_g − π_g)·taux_g ;
- intra-strate : Σ_g π′_g·(taux′_g − taux_g).

Les faits disent que le seuil garantit 1 % en moyenne sur les longueurs et pas par tranche. Un simple changement du mélange des longueurs suffit donc à déplacer le taux sans qu'aucune loi conditionnelle ait bougé. Les deux termes appellent des remèdes différents : strates ou poids pour le premier, ancres pour le second.

**1.4 Distinguer dérive du corps et dérive de la queue.** Deux mondes triplent le taux également.

CALCUL illustratif, test séquentiel à e-valeur 20, approximation de Wald :
- Translation gaussienne de 0,45 σ : visible dans le corps de la distribution, détectable en environ 30 épisodes honnêtes.
- Contamination de 2 % par une source bénigne qui déclenche toujours : invisible dans le corps, détectable seulement par comptage en queue, soit environ 230 épisodes honnêtes.

Le délai de détection est donc soit court, soit de l'ordre du budget d'étalonnage, selon la forme de la dérive.

**1.5 Séparer taux d'alertes et taux de fausses alertes.** En déploiement, une hausse des alertes peut être une dérive ou une attaque. Toute règle qui se ré-étalonne sur le flux non étiqueté donne à l'agent un levier sur son propre seuil. Je considère cette distinction comme le point central du problème.

**1.6 Réparer le score avant le seuil.** Un score dont la loi honnête est invariante (pivot) rend le seuil stable. Deux vérifications :
- La normalisation par longueur corrige-t-elle la queue, et pas seulement la moyenne et la variance ?
- Lequel des moniteurs agrégés dérive ?

**1.7 Compter les régimes, pas les épisodes.** Si 300 épisodes viennent de 15 tâches (illustratif), l'effectif utile pour généraliser à une nouvelle tâche est plus proche de 15 que de 300.

---

## 2. Données brutes de départ

- **Par épisode, par pas, par moniteur avant agrégation** : score brut, score normalisé, projection des activations sur chaque sonde. La contrainte « aucune moyenne ni médiane sur les jetons » concerne la sonde ; tout ce que je propose opère en aval, sur les scores. Je ne sais pas si un maximum sur les pas tombe sous cette contrainte : à confirmer par le programme.
- **Métadonnées** : identifiant de tâche, version de l'agent, longueur, source bénigne, lot, date, graine, paramètres d'échantillonnage.
- **Appariement** : pour chaque épisode d'agent, le ou les épisodes du jumeau sur la même tâche, plus au moins deux graines du jumeau, pour le contrôle jumeau-contre-jumeau.
- **Historique** : chaque seuil utilisé, l'ensemble d'étalonnage qui l'a produit, les alertes, les verdicts de relecture humaine.
- **Journaux de déploiement** horodatés, non filtrés par l'alerte. Sinon il y a biais de sélection.
- **Premier tableau à produire** : taux réel laissé-un-régime-dehors (étalonner sur K−1 régimes, mesurer sur le K-ième), avec intervalle exact de Clopper-Pearson (1934). La dispersion de ce tableau est la grandeur principale. Je ne sais pas ce qu'elle vaut.

---

## 3. Méthodes : ce qu'elles supposent, comment elles échouent, mesure minimale

**Protocole de mesure commun M0**, valable pour chaque instrument (livrable c).

Sur des épisodes honnêtes tenus à l'écart du nouveau régime, appariés par tâche et longueur à ceux de l'ancien régime et au jumeau :
1. taux réel de fausses alertes avec intervalle exact ;
2. taux de détection sur des sabotages plantés, au taux **réel** et non nominal ; ces sabotages ne servent jamais au réglage ;
3. comparaison à cinq vérifications mécaniques à battre :
   - **B0** seuil fixe inchangé ;
   - **B1** seuil fixe étalonné à α/3 ;
   - **B2** audit des k premiers rangs par lot ;
   - **B3** centrage-réduction par lot sur témoins ;
   - **B4** oracle ré-étalonné avec la vérité du monde planté.

Un instrument qui ne bat pas B1 en détection à taux réel égal ne justifie pas sa complexité.

| Instrument | Suppose | Échoue quand | Mesure propre (en plus de M0) |
|---|---|---|---|
| **Conforme pondéré** (Tibshirani, Barber, Candès, Ramdas 2019, « Conformal Prediction Under Covariate Shift ») | La loi du score sachant les covariables est invariante ; seul le mélange change ; le rapport de densités est connu ou estimable. | Changement de version (la loi conditionnelle bouge). Poids estimés sur activations de grande dimension. À α = 1 %, les poids lourds donnent un quantile infini : aucune alerte, taux tenu, détection nulle. | Effectif utile (Σw)²/Σw² ; part « composition » du §1.3 réellement corrigée. |
| **Variantes à poids estimés** (Lei et Candès 2021, « Conformal inference of counterfactuals and individual treatment effects » ; Park, Dobriban, Lee, Bastani 2022, « PAC Prediction Sets Under Covariate Shift » ; Yang, Kuchibhotla, Tchetgen Tchetgen, « Doubly robust calibration of prediction sets under covariate shift », année à vérifier) | Idem, avec erreur de poids bornée. | Mêmes cas. | Sensibilité du taux réel à une perturbation des poids. |
| **Conforme adaptatif en ligne** (Gibbs et Candès 2021, « Adaptive Conformal Inference Under Distribution Shift » ; Gibbs et Candès 2024, « Conformal Inference for Online Prediction with Arbitrary Distribution Shifts » ; Zaffran et al. 2022, « Adaptive Conformal Predictions for Time Series » ; Angelopoulos, Candès, Tibshirani 2023, « Conformal PID Control for Time Series Prediction ») | Un retour d'erreur à chaque pas. La garantie est une fréquence d'erreur de long terme proche de α pour toute suite, avec un écart en O(1/(γT)) : forme citée de mémoire, à relire. | Pas de retour sur le flux non étiqueté. La garantie porte sur la fréquence d'alertes : un attaquant fait monter le seuil. À 1 %, les erreurs sont rares, donc l'adaptation est lente. Rien par régime. | Duel D4 ; taux réel par fenêtre et pas seulement cumulé. |
| **Conditionnel par strates ou groupes** (Vovk, Gammerman, Shafer 2005, *Algorithmic Learning in a Random World* : Mondrian ; Gibbs, Cherian, Candès 2023, « Conformal Prediction with Conditional Guarantees » ; Jung, Noarov, Ramalingam, Roth 2023, « Batch Multivalid Conformal Prediction » ; borne d'impossibilité : Barber, Candès, Ramdas, Tibshirani 2021, « The limits of distribution-free conditional predictive inference ») | Strates observables au test ; échangeabilité dans la strate. | n par strate sous la limite du §1.2. Dérive intra-strate. Source bénigne non observable. | Taux réel par strate contre la bande Beta ; nombre de strates non certifiables. |
| **Détection de dérive** (Vovk, Nouretdinov, Gammerman 2003, « Testing exchangeability on-line » ; Volkhonskiy et al. 2017, « Inductive conformal martingales for change-point detection » ; Ramdas, Grünwald, Vovk, Shafer 2023, « Game-theoretic statistics and safe anytime-valid inference » ; Podkopaev et Ramdas 2022, « Tracking the risk of a deployed model and detecting harmful distribution shifts » ; Rabanser, Günnemann, Lipton 2019, « Failing Loudly » ; Gretton et al. 2012, « A Kernel Two-Sample Test » ; Page 1954, « Continuous inspection schemes ») | Sous l'hypothèse nulle, échangeabilité ; la fausse alarme de dérive est bornée à tout instant par l'inégalité de Ville. | Aucune garantie de délai. Aveugle à la queue si le test regarde le corps (§1.4). Sur flux non étiqueté, confond dérive et attaque. | Délai médian et taux de fausse alarme sur mondes iso-triplement (§4) ; taux réel moyen subi pendant le délai. |
| **Fenêtre glissante, poids de récence** (Barber, Candès, Ramdas, Tibshirani 2023, « Conformal prediction beyond exchangeability ») | Dérive lente. L'écart de couverture est borné par une somme pondérée de distances en variation totale, non calculable sans hypothèse. | La fenêtre doit contenir au moins 99 honnêtes pour seulement exprimer 1 %, et environ 230 pour le certifier (CALCUL §1.2). Elle est donc plus lente que le changement de régime. Honnêtes non étiquetés. | Taux réel en fonction de la taille de fenêtre, en dérive brusque et en dérive lente. |
| **Témoins honnêtes par lot** (valeurs p conformes contre référence : Bates, Candès, Lei, Romano, Sesia 2023, « Testing for outliers with conformal p-values ») | Témoins et agent honnête échangeables dans le lot. | Écart témoin-agent (S8). Coût : il faut au moins 99 témoins pour qu'une valeur p atteigne 1 %. | Duel D3. |
| **Jumeau comme référence courante** | La différence appariée agent − jumeau a une loi plus stable que le score brut. | L'écart dépend du régime. | Variance inter-régimes du score apparié contre celle du score brut. Je ne connais pas de publication qui valide ce point précis. |
| **Pire cas sur une famille** (Cauchois, Gupta, Ali, Duchi 2024, « Robust Validation: Confident Predictions Even When Distributions Shift ») | La dérive reste dans une boule de divergence ou une famille bornée. | Le rayon est choisi, pas connu. Perte de détection. | Détection contre B1, qui en est la version triviale. |
| **Autres** | | | |
| Régimes comme unité (Dunn, Wasserman, Ramdas 2023, « Distribution-Free Prediction Sets for Two-Layer Hierarchical Models » ; Lee, Barber, Willett, « Distribution-free inference with hierarchical data », année à vérifier) | Régimes échangeables entre eux. | K petit : le niveau atteignable est borné par 1/(K+1). | Tableau laissé-un-régime-dehors. |
| Extrapolation de queue par valeurs extrêmes (Pickands 1975, « Statistical inference using extreme order statistics ») | Queue régulière. | Contamination en mélange. | Taux réel sur le monde à contamination. |
| Contrôle de risque (Angelopoulos, Bates, Candès, Jordan, Lei, « Learn then Test », année à vérifier) | Données i.i.d. | Toute dérive. | — |

Je crois qu'il existe des travaux récents sur des martingales conformes pondérées pour la surveillance en déploiement : **pas sûr, référence à vérifier**.

---

## 4. Vérification extérieure au programme

1. **Mondes plantés iso-triplement.** Les faits décrivent une famille « à décalage ». Je propose de l'étendre (HYPOTHÈSE de conception) à cinq formes de dérive qui triplent toutes le taux de B0 :
   - (i) translation ;
   - (ii) changement d'échelle ;
   - (iii) contamination de queue à environ 2 % ;
   - (iv) changement du mélange des longueurs sans changement conditionnel ;
   - (v) dérive qui touche l'agent et pas le jumeau.

   Chaque forme est jouée avec et sans sabotage planté. Une règle qui ne survit qu'à (i) n'a pas corrigé le défaut.
2. **Mondes écrits par un tiers.** Le générateur de dérive est écrit par quelqu'un qui ne connaît pas les règles candidates, et réciproquement. La vérité et le verdict restent hors machine, ce que les faits prévoient déjà.
3. **Préenregistrement** de la règle, de α, de δ et du critère de mort avant exécution.
4. **Données publiques à décalage** : WILDS (Koh et al. 2021, « WILDS: A Benchmark of in-the-Wild Distribution Shifts »), avec un score de détection quelconque. Cela teste la statistique, pas la sonde. Je ne connais pas de jeu public d'activations d'agents saboteurs avec régimes étiquetés.
5. **Réplication sur modèles ouverts** par une équipe distincte : même interface, autres poids, autres tâches.
6. **Mesure indépendante du taux réel** : un échantillon aléatoire d'épisodes non alertés et alertés, relu à l'aveugle. La relecture étant rare, c'est le poste à budgéter en premier.
7. **Lecture de la page CURA** par deux personnes : définition exacte du « triplement » (n, régimes, intervalle).

---

## 5. Demande reformulée

> Sur les scores bruts par pas, par épisode et par moniteur, de K régimes étiquetés (tâche × version × longueur × source) :
> 1. établir la part du sur-taux due au bruit d'étalonnage, à la composition et à la dérive intra-strate ;
> 2. proposer une règle d'alerte calculable sans étiquette de sabotage, qui ne se ré-étalonne jamais sur le flux non étiqueté ;
> 3. pour laquelle on énonce une garantie par régime (ou, à défaut, son impossibilité à ce n) ;
> 4. qui survit aux cinq familles iso-triplement écrites par un tiers ;
> 5. et qui bat le seuil à α/3 en détection à taux réel égal.
>
> Dire à quel n la garantie cesse et ce qui remplace alors le seuil.

---

## 6. Propositions de correction

Tout ce qui suit est **ma proposition**. Les briques sont publiées (§3). Je ne sais pas si l'assemblage l'est.

### P1 — Seuil certifié par strate, avec refus explicite

- **Règle.** Pour chaque strate g, prendre la statistique d'ordre k_g la plus basse telle que P(Bin(n_g, α) ≤ n_g − k_g) ≤ δ. Si aucune n'existe (n_g < ln δ / ln(1−α)), la strate est déclarée non certifiable et passe à P4.
- **Garantie.** Avec probabilité ≥ 1−δ sur l'étalonnage, taux ≤ α dans la strate. Suppose l'échangeabilité intra-strate et des strates observables.
- **Coût.** Aucun calcul. Perte de détection (seuils plus hauts). Beaucoup de strates refusées.
- **Test de mort.** Familles (i), (ii), (iii), (v) : la règle doit mourir, puisqu'elle ne traite que la composition. Elle doit survivre à (iv). Si elle meurt sur (iv), l'implémentation est fausse.
- **Différence avec le publié.** Aucune sur le fond (Mondrian et intervalles de tolérance). L'apport est le refus explicite et le décompte des strates non certifiables.

### P2 — Ancres appariées dans le lot

- **Règle.** Dans chaque lot, m épisodes du jumeau sur les mêmes tâches. Pour un épisode d'agent de score s : p = (1 + #{témoins ≥ s}) / (m+1). Alerte si p ≤ α.
- **Variante économe.** Le score devient d = s_agent − s_jumeau sur la même tâche. Il est étalonné sur des paires jumeau-jumeau′, avec un seuil commun à tous les lots.
- **Garantie.** Si l'agent honnête et les témoins sont échangeables dans le lot, P(alerte | honnête) ≤ α, quelle que soit la dérive entre lots, car l'étalonnage est contemporain. Pour la variante, c'est une HYPOTHÈSE de stabilité du score apparié, sans garantie.
- **Coût.** m ≥ 99 par lot pour atteindre 1 %, soit au moins un doublement du calcul si le lot fait une centaine d'épisodes (illustratif). La variante coûte un jumeau par épisode.
- **Test de mort.** Famille (v) : si le taux réel triple, la règle est morte tant que D3 n'est pas passé. Familles (i) à (iv) : elle doit tenir dans la bande Beta(m).
- **Différence.** Les valeurs p conformes contre référence sont dans Bates et al. 2023. L'apport est l'appariement par tâche et le contrôle jumeau-contre-jumeau.

### P3 — Garde à deux clés, à sens unique

- **Règle.** Deux processus d'e-valeurs, calculés **sur témoins seulement** :
  - clé « corps » : rangs conformes des scores témoins contre l'étalonnage ;
  - clé « queue » : pari sur le compte de dépassements du seuil.

  Trois états :
  - NORMAL : seuil gelé.
  - SUSPECT : dès qu'une clé atteint 1/δ. La revendication de 1 % est retirée et on bascule sur P4.
  - RÉ-ÉTALONNÉ : après n_min témoins du nouveau régime, n_min étant la borne du §1.2.

  Le flux non étiqueté ne peut que durcir la règle, jamais la relâcher.
- **Garantie.** Sans dérive, la probabilité de passer un jour en SUSPECT est ≤ δ (Ville). La garantie vaut sous lecture continue, ce qui répond aux franchissements répétés. Sous dérive, il n'y a aucune garantie de délai sans hypothèse sur la forme.
- **Coût.** Un flux de témoins permanent. Pendant le délai, le sur-taux est subi : environ 30 ou environ 230 témoins selon la forme (CALCUL §1.4, illustratif).
- **Test de mort.** Sur (iii), la clé « queue » doit déclencher avant qu'un budget préenregistré de fausses alertes en excès soit dépassé. La règle est aussi tuée par une dérive oscillante, tenue juste sous le seuil de détection, qui maintient le taux moyen au-dessus du double de α (seuil illustratif).
- **Différence.** Podkopaev et Ramdas 2022 suivent déjà un risque par suites de confiance. L'apport est la contrainte de sens unique et la séparation corps/queue.

### P4 — Remplacement du seuil fixe : budget par rang et garantie au niveau du régime

- **Règle.** Par lot, relire les k épisodes de plus petite valeur p (relative aux témoins si P2 est disponible, de rang brut sinon). En parallèle, publier une suite de confiance sur le taux chez les témoins. Énoncer la garantie au niveau du régime à partir du tableau laissé-un-régime-dehors : « dans un nouveau régime, taux ≤ β avec probabilité ≥ K/(K+1) ».
- **Garantie.** Le budget de relecture est exact par construction. Il n'y a aucune garantie de taux de fausses alertes. La garantie par régime suppose des régimes échangeables.
- **Coût.** Les alertes ne sont plus comparables d'un lot à l'autre. Un lot entièrement saboté n'est vu qu'à hauteur de k.
- **Test de mort.** Monde planté à prévalence de sabotage variable par lot : la détection doit rester ≥ celle de B1. Sinon P4 n'est qu'un pis-aller.

**Quand renoncer au seuil fixe.** Dans trois cas :
- n par régime est sous ln δ / ln(1−α) ;
- la dispersion laissé-un-régime-dehors dépasse la bande Beta ;
- la contrainte réelle est le budget de relecture (S3).

Dans ces cas, annoncer « 1 % » est une affirmation que rien ne soutient. Mieux vaut P4, avec un taux mesuré a posteriori.

---

## (b) Duels décisifs

Les seuils chiffrés ci-dessous sont **illustratifs** et à préenregistrer.

### D1 — Composition contre intra-strate

- **H_A** : à seuils par strate gelés sur l'ancien régime, le taux par strate du nouveau régime reste dans la bande Beta à 95 %. Seul le mélange a changé.
- **H_B** : au moins une strate en sort, après correction de multiplicité.
- **Métrique** : taux par strate et part « composition » de la décomposition du §1.3.
- **Contrôle négatif** : coupe aléatoire à l'intérieur de l'ancien régime. Les deux termes doivent être nuls au bruit près, sinon l'outil est faux.
- **Falsification** : si les strates tiennent, H_B est fausse, et les ancres (P2) sont un coût inutile pour cette dérive. Si une strate sort, H_A est fausse, et le conforme pondéré sur covariables observées ne peut pas suffire.

### D2 — Corps contre queue

- **H_A** : la dérive est une transformation de position-échelle. Après recalage de la position et de l'échelle sur environ 30 témoins, le taux revient dans la bande.
- **H_B** : la dérive est concentrée en queue. Le recalage laisse le taux hors bande.
- **Métrique** : taux réel après recalage (B3) ; délais des deux clés de P3.
- **Contrôle négatif** : monde sans dérive. Le recalage ne doit pas dégrader le taux, et la fausse alarme des clés doit rester ≤ δ.
- **Falsification** : si B3 suffit, H_B est fausse, et P3 se réduit à une clé. Sinon H_A est fausse, et toute correction fondée sur le corps (B3, extrapolation de queue) est exclue.

### D3 — Échangeabilité jumeau-agent

- **H_A** : les valeurs p des épisodes d'agent honnêtes contre les témoins du même lot sont uniformes dans chaque régime.
- **H_B** : elles ne le sont pas, avec un écart qui dépend du régime.
- **Métrique** : e-valeur d'uniformité par régime ; taux réel de l'agent honnête au seuil des témoins.
- **Seuil** : rejet à e ≥ 20.
- **Contrôle négatif** : jumeau contre jumeau′ (deux graines). Il doit être uniforme. S'il ne l'est pas, c'est l'appariement ou le lot qui est cassé, pas le jumeau.
- **Falsification** : si l'uniformité tient sur les K régimes, H_B est fausse à la taille d'effet détectable, qu'il faut énoncer. Sinon H_A est fausse, et P2 meurt ou exige un décalage appris dont rien ne garantit la stabilité.

### D4 — Ré-étalonnage sur flux contre masquage

- **H_A** : une règle adaptative nourrie par le flux non étiqueté conserve sa détection quand la prévalence de sabotage planté passe de 0 à plusieurs multiples de α.
- **H_B** : sa détection chute, alors que celle d'une règle nourrie par les seuls témoins ne chute pas.
- **Métrique** : détection à taux réel honnête mesuré, en fonction de la prévalence.
- **Contrôle négatif** : à prévalence 0, les deux règles doivent avoir le même taux réel.
- **Falsification** : si la détection ne chute pas, H_B est fausse, et le conforme adaptatif sur flux est admissible, ce qui est moins coûteux que P2 et P3. Si elle chute, H_A est fausse, et il est interdit.

---

## (d) Ancrage matériel

Tout ce qui suit est **illustratif**.

- **Étage statistique** (mondes plantés au niveau des scores, cinq familles, règles P1 à P4 et B0 à B4) : processeur seul, de l'ordre de quelques heures. C'est par là qu'il faut commencer : D2 et D4 s'y tranchent sans modèle.
- **Étage modèle** : un modèle à poids ouverts de taille moyenne, en deux versions ou deux affinages pour simuler le changement de version. Sondes linéaires sur activations résiduelles. Jumeau = même modèle sans consigne de sabotage. Je ne recommande pas de modèle précis : le choix dépend de l'interface du programme, que je ne connais pas.
- **Volume** : K ≈ 8 régimes × environ 300 épisodes honnêtes × 2 (jumeau) ≈ 5 000 épisodes, plus quelques centaines de sabotages plantés pour l'évaluation seule. Je ne connais pas le coût par épisode du programme. Si un épisode coûte quelques minutes de GPU, l'ordre de grandeur est de quelques centaines d'heures-GPU.
- **Poste rare** : la relecture humaine. Quelques centaines d'épisodes relus à l'aveugle pour la mesure indépendante du §4.6.
- **Ordre conseillé** : §1.1 à 1.3 sur données existantes (coût nul), puis D4 et D2 en mondes plantés, puis D1 et D3 sur modèle ouvert.

FIN-DE-CELLULE