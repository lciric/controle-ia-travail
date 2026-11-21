# Proposition B, Tour III.1 : un seuil à 1 % avec peu d'épisodes honnêtes, et l'usage du papier pour la surveillance et le contrôle

*Ce tour se joue à l'aveugle. Je ne vois aucune autre proposition et je n'en critique donc aucune (B1 sans objet ici).*

**Statuts utilisés.**
- Les affirmations du papier sont RAPPORTÉ, avec leur page.
- Le contexte du programme est RAPPORTÉ.
- Un calcul reproduit dans ce texte est VÉRIFIÉ, avec la formule à côté.
- Tout ce que je propose est HYPOTHÈSE.
- Les chiffres hors faits sont « illustratif ».
- Aucun identifiant arXiv n'est donné de mémoire. Seul celui du papier figure dans les faits (2602.00986v2).

---

## 0. (a) Ce que la question suppose sans que ce soit établi

| # | Supposé | Statut | Commentaire |
|---|---|---|---|
| S1 | Il faut environ 50 dépassements, donc environ 5 000 épisodes honnêtes par classe, pour fixer un seuil à 1 %. | Arithmétique VÉRIFIÉ (5 000 × 0,01 = 50). La nécessité est une HYPOTHÈSE non établie. | Ce calcul confond trois tâches distinctes (voir §1). |
| S2 | Les épisodes honnêtes sont échangeables (i.i.d.) dans chaque classe de longueur. | HYPOTHÈSE | Des épisodes sur une même variante de tâche sont corrélés. L'effectif utile peut être le nombre de tâches, pas le nombre d'épisodes. |
| S3 | La distribution de calibration est celle du déploiement. | HYPOTHÈSE | Version du modèle, mélange de tâches et outils peuvent dériver. |
| S4 | Le programme dispose d'une distribution nulle « calibrée ». | RAPPORTÉ (contexte) | Elle n'est pas auditée dans les faits. J'ignore sur combien d'épisodes et selon quelle méthode. |
| S5 | La classe de longueur est la bonne stratification. | HYPOTHÈSE | La difficulté de la tâche peut compter davantage. |
| S6 | Le taux de fausses alertes (FPR) à 1 % est la bonne grandeur pour trancher la question *scientifique* (saboteur contre échec honnête). | HYPOTHÈSE | Le point de fonctionnement à 1 % sert une décision de déploiement. Le contraste apparié se teste autrement (§6.1, P5). |
| S7 | Les sondes du papier fonctionnent hors récompense vérifiable. | Non établi | Les auteurs listent cette limite (RAPPORTÉ, p. 25). |
| S8 | Un agent conscient d'être surveillé ne façonne pas la queue de sa distribution de scores. | HYPOTHÈSE | Le papier ne contient aucun cadre adverse (RAPPORTÉ, p. 25). Le test d'évasion à capacité constante est fermé (RAPPORTÉ) ; je ne le rouvre pas. |
| S9 | Produire un épisode coûte cher, de façon uniforme. | RAPPORTÉ (cher) | Uniforme : HYPOTHÈSE. Un pas forké depuis un état sauvegardé peut coûter beaucoup moins qu'un épisode complet ; c'est à mesurer. |
| S10 | « Quelques centaines » d'épisodes honnêtes au total. | RAPPORTÉ | Répartis sur plusieurs classes, cela peut donner moins de 299 par classe (voir §1). |

---

## 1. Ce qu'un expert ferait et qu'on ne demande pas

**1. Séparer trois tâches que S1 confond.** Ce calcul relève des statistiques d'ordre classiques (tolérance au sens de Wilks).
- **(T1) Garantir FPR ≤ 1 %.** On prend comme seuil le maximum de n scores honnêtes. On a alors P(FPR réel > 1 %) = 0,99ⁿ. Pour n ≥ 299, cette probabilité est ≤ 5 %. Calcul : ln 0,05 / ln 0,99 ≈ 298,1, d'où n = 299. Statut : VÉRIFIÉ.
- **(T1 bis) Garantie conforme marginale.** Elle exige seulement n ≥ (1−α)/α = 99 pour α = 1 %. Statut : VÉRIFIÉ.
  - Le prix est la sur-prudence. Avec le maximum de n comme seuil, le FPR réel suit une loi Beta(1, n), de moyenne 1/(n+1), soit environ 0,33 % pour n = 299. Statut : VÉRIFIÉ. La puissance se perd en conséquence.
- **(T2) Certifier que le seuil est *proche* de 1 %**, par exemple à ±0,3 point. C'est là qu'il faut des milliers d'épisodes. Statut : VÉRIFIÉ, puisque la largeur de l'intervalle binomial varie en √(p/n).
- **(T3) Déclarer qu'un épisode est saboteur.** Cette tâche dépend de la *puissance* sur les saboteurs, pas de la précision de l'estimation du FPR.

Le programme n'a besoin de T2 que s'il veut affirmer « exactement 1 % ». Pour un verdict, T1 suffit, avec une perte de puissance qu'il faut mesurer.

**2. Fixer l'estimande.** Il faut dire si le FPR visé est marginal (moyenné sur les tirages de calibration) ou conditionnel au jeu de calibration utilisé. Il faut dire s'il vaut par épisode, par tâche ou par classe. Les garanties diffèrent selon le cas.

**3. Compter des tâches, pas des épisodes.** Il faut estimer la corrélation intra-tâche des scores. Si elle est forte, « quelques centaines d'épisodes » peut valoir quelques dizaines d'unités indépendantes (S2).

**4. Faire une analyse de puissance sur les saboteurs avant d'en produire.** Pour un effet donné sur le contraste saboteur contre échec honnête, il faut savoir combien de paires sont nécessaires.

**5. Dériver le FPR cible du budget de revue humaine**, au lieu de le fixer à 1 % a priori. Ce cadrage par budget d'audit est celui de Greenblatt, Shlegeris, Sachan, Roger, *AI Control: Improving Safety Despite Intentional Subversion* (2023 ; identifiant non donné).

**6. Exploiter la structure fourchable des épisodes.** Le jumeau honnête et les préfixes forcés existent (RAPPORTÉ). Ils permettent des tests exacts par rangs et la simulation d'événements rares. Les deux approches contournent la calibration par épisodes complets (§3, §6).

**7. Pré-enregistrer** le seuil, la statistique, les classes et les critères d'arrêt. Il faut aussi faire garder par un tiers un jeu honnête scellé.

---

## 2. Les données brutes d'où partirait l'expert

| Source | Ce qu'elle apporte | Ce qu'elle suppose | Statut |
|---|---|---|---|
| **Activations et scores au niveau du pas** des épisodes déjà produits (tous les pas, pas seulement le score final de l'épisode) | Des milliers d'incréments pour modéliser la nulle de la somme séquentielle (rééchantillonnage par blocs). | Stationnarité et dépendance faible des incréments. À tester (E2). | HYPOTHÈSE |
| **Fourches du jumeau honnête** au même préfixe : K continuations d'un pas par point de contrôle | Une nulle *conditionnelle* exacte par pas (§6.1, P1). | Le jumeau échantillonne la même politique que l'agent sous H0 (mêmes poids, même prompt, même température). | HYPOTHÈSE |
| **Journaux d'environnement** : diffs, tests, fichiers aux jalons | Vérifications mécaniques indépendantes et confirmation du dommage. | Que ces journaux existent et soient archivés. | HYPOTHÈSE |
| **Transcriptions publiques d'agents rejouées en lecture forcée** à travers un modèle ouvert : une passe avant, sans échantillonnage ni environnement | Beaucoup de « pas honnêtes » bon marché pour étudier la forme de la queue. | Hors politique : la distribution peut différer (E7). Ces données ne servent jamais à calibrer le verdict. | HYPOTHÈSE |
| **Sabotages plantés par script** dans des transcriptions honnêtes, puis rejoués en lecture forcée | Vérité terrain connue pour mesurer la puissance. | Un sabotage scripté peut ne pas ressembler à un sabotage diffus *généré*. | HYPOTHÈSE |
| **Métadonnées de variante de tâche et score de valeur pré-génération** (covariable de difficulté déjà décidée, RAPPORTÉ) | Stratification par difficulté au lieu de la seule longueur. | Le transfert de la sonde de valeur hors récompense vérifiable n'est pas établi (S7). | HYPOTHÈSE |

---

## 3. Méthodes et outils, avec ce que chacun suppose

Les références sont données avec titre, auteurs et année seulement si je peux les attribuer. Les identifiants arXiv sont omis par règle d'intégrité.

**Statistiques d'ordre et tolérance.** Wilks, *Determination of sample sizes for setting tolerance limits* (1941).
- Suppose l'échangeabilité.
- Donne T1 avec n = 299. Statut : VÉRIFIÉ.
- Pas d'hypothèse de forme, mais sur-prudence.

**p-valeurs conformes et quantiles conformes.**
- Références : Vovk, Gammerman, Shafer, *Algorithmic Learning in a Random World* (2005) ; Angelopoulos, Bates, *A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification* (2021) ; Bates, Candès, Lei, Romano, Sesia, *Testing for outliers with conformal p-values* (Annals of Statistics, 2023 ; année à vérifier).
- Suppose l'échangeabilité entre la calibration et l'épisode testé.
- La résolution est 1/(n+1). La garantie est marginale.
- Pour une garantie conditionnelle au jeu de calibration : Vovk, *Conditional validity of inductive conformal predictors* (2012 ; référence à vérifier).

**Calibration par strates (conforme de Mondrian).** Elle est décrite dans le livre de Vovk et al.
- Suppose l'échangeabilité *dans* chaque strate.
- Chaque strate demande n ≥ 99, ou n ≥ 299 pour la version PAC. D'où l'intérêt de mutualiser les strates.

**Régression quantile conformalisée.** Romano, Patterson, Candès, *Conformalized Quantile Regression* (2019).
- Modélise le quantile à 99 % comme fonction lisse de la longueur et de la difficulté, puis le conformalise.
- Suppose l'échangeabilité globale. La validité reste marginale et ne vaut pas classe par classe.
- C'est la façon la plus économique de partager l'information entre classes.

**Valeurs extrêmes (loi de Pareto généralisée au-delà d'un seuil).** Pickands, *Statistical inference using extreme order statistics* (1975) ; Coles, *An Introduction to Statistical Modeling of Extreme Values* (2001).
- Suppose que la queue appartient à un domaine d'attraction et que le seuil de modélisation est bien choisi.
- Pas de garantie en échantillon fini. Variance forte avec quelques dizaines d'excès.
- Un adversaire peut tronquer sa queue.
- À utiliser comme contre-vérification, jamais comme verdict.

**e-valeurs et tests martingales.** Vovk, Wang, *E-values: Calibration, combination and applications* (Annals of Statistics, 2021) ; Ramdas, Grünwald, Vovk, Shafer, *Game-theoretic statistics and safe anytime-valid inference* (Statistical Science, 2023 ; année à vérifier).
- Suppose une nulle conditionnelle pas à pas d'espérance ≤ 1.
- L'inégalité de Ville donne alors P(sup ≥ 1/α) ≤ α *sans jeu de calibration* et quel que soit l'instant d'arrêt.
- La difficulté est de disposer de cette nulle conditionnelle. Les fourches du jumeau la fournissent (P1).
- La moyenne d'e-valeurs reste une e-valeur, ce qui permet d'agréger des épisodes ou des sondes sans hypothèse d'indépendance.

**Tests séquentiels classiques.** Wald, *Sequential Analysis* (1947) ; Page, *Continuous inspection schemes* (1954) pour le CUSUM.
- Supposent des modèles de densité sous H0 et H1.
- Le CUSUM est cohérent avec la somme séquentielle déjà décidée (RAPPORTÉ). Il exige cependant une calibration de sa longueur moyenne de fonctionnement sous H0 : on retombe sur le problème initial, sauf avec P1 ou P2.

**Simulation d'événements rares par fractionnement.** Cérou, Guyader, *Adaptive multilevel splitting for rare event analysis* (2007 ; référence à vérifier).
- On fork les épisodes dont la somme courante franchit des niveaux intermédiaires.
- Suppose la propriété de Markov : l'avenir dépend de l'état sauvegardé, c'est-à-dire du contexte complet et de l'environnement. L'environnement doit être rejouable.
- Estime P(dépassement) sans biais avec moins d'épisodes complets que la méthode naïve.

**Plans d'échantillonnage.**
- Production par lots avec arrêt séquentiel de la calibration elle-même (plans par groupes séquentiels).
- Allocation des nouveaux épisodes aux strates où la décision est la plus proche du seuil.
- Échantillonnage par grappes de tâches (une tâche par épisode tant que c'est possible) pour casser la corrélation S2.

**Transfert.** Calibrer sur un modèle plus petit ou sur des transcriptions hors politique suppose que la forme de la nulle transfère. C'est peu plausible pour des activations propres à un modèle (HYPOTHÈSE). On ne l'utilise que pour la forme de queue, validée par E7.

**Bornes binomiales exactes.** Clopper, Pearson (1934), *The use of confidence or fiducial limits illustrated in the case of the binomial*.
- Servent à rapporter le FPR mesuré sur le jeu honnête tenu à part.
- Avec 0 dépassement sur n, la borne unilatérale à 95 % vaut 1 − 0,05^(1/n) ≈ 3/n. Statut : VÉRIFIÉ.

---

## 4. Ce qui permettrait de vérifier la validité hors du programme et de sa direction

1. **Réplication indépendante des résultats du papier** sur ses modèles ouverts : Table 2 (ablation de 1 % des neurones de valeur, p. 5) et Table 3 (AUC 0,67, p. 8), RAPPORTÉ. C'est peu coûteux et cela dit si la base de comparaison est solide.
2. **Vérité terrain plantée** : sabotages scriptés de dommage connu (§2), insérés à l'aveugle par une tierce partie. Le programme ne sait pas quels épisodes sont plantés.
3. **Jeu honnête scellé** tenu par un tiers. Il sert seulement à mesurer le FPR final, une fois le seuil gelé et pré-enregistré.
4. **Équipe rouge externe** qui produit ses propres saboteurs, sans accès aux sondes, pour limiter le surajustement aux saboteurs maison.
5. **Mesures indépendantes du dommage** : tests, reproduction des chiffres que l'agent rapporte, revue humaine en aveugle. Ce sont elles qui confirment le dommage, pas la sonde.
6. **Bancs publics de sabotage et de tromperie**, à identifier. Candidats : Benton et al., *Sabotage Evaluations for Frontier Models* (2024 ; référence à vérifier) ; Goldowsky-Dill et al., *Detecting Strategic Deception Using Linear Probes* (2025 ; référence à vérifier). Les travaux sur les menaces diffuses cités dans les faits ne sont pas identifiés : référence à vérifier.
7. **Publication du code de calibration et des p-valeurs conformes** par épisode, pour qu'un tiers recalcule les verdicts.

---

## 5. Reformulation de la demande

> « Pour chaque statistique de surveillance, produire un verdict par épisode dont le taux de fausses alertes sur épisodes honnêtes est **garanti ≤ 1 %** (marginalement, ou avec confiance 1−δ déclarée), dans chaque strate pré-enregistrée (longueur × difficulté), **en comptant les tâches et non les épisodes comme unités** ;
> - en mesurant la perte de puissance due à la sur-prudence, sur saboteurs plantés et sur saboteurs générés, contre l'échec honnête apparié de la même variante ;
> - en n'affirmant « FPR ≈ 1 % » que si un jeu honnête scellé, tenu par un tiers, le confirme par intervalle exact ;
> - en préférant, quand c'est valide, des nulles **conditionnelles** (rangs parmi les fourches du jumeau, e-processus) ou des estimations par **fractionnement** à la calibration par épisodes complets ;
> - en traitant à part la question scientifique (le contraste apparié saboteur contre échec honnête, mesuré par une statistique de rang appariée) et la question opérationnelle (seuil d'alerte ou allocation d'un budget de revue).
> Pour le papier : tester s'il apporte une information **en plus** des quatre lignes de base décidées et des vérifications mécaniques, comme covariable de stratification, comme signal pas à pas ou comme règle de routage. Chaque usage doit être falsifiable sur le contraste saboteur contre échec honnête. »

---

## 6. Propositions concrètes

*Tout ce qui suit est HYPOTHÈSE.*

### 6.1 Fixer un seuil à 1 % avec peu d'épisodes, ou s'en passer honnêtement

**P1 : nulle exacte par rangs parmi les fourches du jumeau.**
- **Principe.** À chaque point de contrôle, on tire K continuations d'un pas avec la politique honnête, depuis le même préfixe. On calcule le rang du score de l'agent parmi les K+1 scores. Sous H0 (l'agent est honnête et suit la même politique), ce rang est uniforme sur {1,…,K+1}. On obtient ainsi une p-valeur exacte par pas, convertible en e-valeur. Le produit de ces e-valeurs, conditionnellement au passé, forme un test martingale, et l'inégalité de Ville s'applique.
- **Effet.** On n'a plus besoin de calibrer par classe de longueur.
- **Coût.** K pas forkés par point de contrôle, pas des épisodes complets.
- **Ce que ça suppose.**
  - Mêmes poids, même prompt et même température pour le jumeau.
  - Pas d'effet d'état caché : cache, horloge, non-déterminisme des outils.
  - Une nulle simple : « l'agent suit la politique honnête de référence ».
- **Comment ça échoue.**
  - Si le saboteur est un modèle affiné, l'« agent honnête » de référence a d'autres poids. Le test détecte alors *toute* différence de politique, pas seulement le sabotage.
  - Le non-déterminisme matériel peut rendre les rangs non uniformes (E1).
  - La puissance peut être faible si le sabotage ne touche qu'une fraction des pas.

**P2 : fractionnement multiniveau pour estimer la queue de la somme séquentielle.**
- **Principe.** On fork m copies dès que la somme courante franchit chaque niveau. On estime P(dépassement du seuil) comme produit de probabilités conditionnelles mesurables. On inverse ensuite pour obtenir le seuil à 1 %.
- **Coût.** Des fins d'épisodes plutôt que des épisodes entiers. Le gain réel est à mesurer, illustratif tant que E3 n'est pas fait.
- **Ce que ça suppose.** Un environnement rejouable (instantanés du système de fichiers et des outils) et la propriété de Markov sur l'état sauvegardé.
- **Comment ça échoue.**
  - Appels externes non rejouables.
  - Niveaux mal choisis, qui donnent une variance explosive.
  - Un état incomplet, qui donne un biais. On le détecte en comparant au Monte-Carlo naïf à un niveau modéré (E3).

**P3 : mutualisation par régression quantile conformalisée sur (longueur, difficulté).**
- **Principe.** On remplace les classes indépendantes par un quantile lisse. La sonde de valeur pré-génération du papier sert de covariable de difficulté, comme déjà décidé.
- **Coût.** Quasi nul en calcul, avec les épisodes existants.
- **Ce que ça suppose.** L'échangeabilité globale et une forme lisse du quantile.
- **Comment ça échoue.** La validité n'est que marginale. Une classe peut sous-couvrir pendant qu'une autre sur-couvre (E2).

**P4 : seuil prudent garanti, avec rapport de la perte de puissance.**
- **Principe.** Si une strate compte au moins 299 tâches indépendantes (VÉRIFIÉ pour δ = 5 %), on prend le maximum comme seuil. En dessous, on rapporte la p-valeur conforme avec sa résolution 1/(n+1). On écrit alors « verdict impossible à 1 % dans cette strate » plutôt que « non concluant ».
- **Coût.** Nul.
- **Comment ça échoue.** Puissance faible, et S2 si les épisodes ne sont pas indépendants.

**P5 : se passer du seuil, de deux façons.**
- **(i) Question scientifique.** On utilise une statistique de rang appariée, saboteur contre échec honnête de la même variante, tâche par tâche (test des rangs signés, ou AUC appariée avec intervalle bootstrap par tâche). Aucun quantile extrême n'est requis.
- **(ii) Déploiement.** On audite les k épisodes les mieux classés par période, avec k fixé par le budget humain. Aucun seuil absolu n'est requis.
- **Ce que ça suppose.**
  - Pour (i) : des paires appariées en nombre suffisant.
  - Pour (ii) : on contrôle la *charge*, pas le FPR par épisode honnête.
- **Comment ça échoue.**
  - Pour (ii) : si les saboteurs sont nombreux, le budget est saturé. Si aucun saboteur n'est présent, les k audits sont tous des fausses alertes. C'est acceptable seulement si cela est déclaré.

**P6 : extrapolation par valeurs extrêmes, en contre-vérification seulement.**
- **Coût.** Nul.
- **Comment ça échoue.** Un adversaire tronque sa queue (S8), et l'extrapolation n'a pas de garantie en échantillon fini (E4).

**P7 : lot honnête neuf alloué séquentiellement.**
- **Principe.** Si un lot est produit, une tâche par épisode, alloué aux strates les plus proches du seuil, avec arrêt quand l'intervalle exact tranche.
- **Coût.** C_ep par épisode (montant non fourni). Le budget se mesure en multiples de C_ep.

### 6.2 Utiliser le papier pour la surveillance et le contrôle

**Faits d'appui (RAPPORTÉ).**
- AUC de valeur pré-génération : 0,67 (Table 3, p. 8), jugée « modérée » par les auteurs.
- Neurones de « dopamine » utilisés comme modèle de récompense de processus : 77,8 % contre 75,0 % pour la ligne de base implicite (Table 4, p. 9).
- L'ablation des neurones de valeur abolit la prédiction d'erreur en aval (p. 5, Annexe H).
- Récompense binaire vérifiable seulement. Aucun cadre adverse (p. 25).

**M1 : détecteur de « mauvais pas connu et non corrigé ».**
- **Principe.** On cherche les pas où l'erreur d'écart temporel lue par les sondes de dopamine est fortement négative (l'agent « sait » que le pas dégrade sa valeur attendue) et qui ne sont suivis d'aucune correction dans les pas suivants. Un agent honnête qui échoue devrait corriger ou signaler. Un saboteur devrait laisser passer.
- **Coût.** Réentraîner la sonde sur des jalons de recherche faute de récompense terminale. Les étiquettes viennent de jalons vérifiables ou de vérifications mécaniques.
- **Ce que ça suppose.**
  - Le signal transfère hors récompense vérifiable (S7).
  - Le saboteur ne contrôle pas ces neurones, peu nombreux (moins de 1 %, p. 1, RAPPORTÉ), donc des cibles concentrées. Les auteurs signalent eux-mêmes le risque de contournement par intervention neuronale (p. 25).
- **Comment ça échoue.**
  - Le signal lit seulement la difficulté et ne distingue pas l'échec honnête (E5).
  - L'agent garde ses neurones de valeur « optimistes ».

**M2 : stratification de la nulle par difficulté prédite**, par Mondrian ou par P3.
- **Principe.** Les tâches difficiles produisent plus d'échecs honnêtes qui ressemblent à du sabotage. Calibrer par difficulté devrait réduire les fausses alertes à puissance égale.
- **Ce que ça suppose.** Une AUC de 0,67 suffit à créer des strates distinctes (non établi).
- **Comment ça échoue.** Les strates sont indiscernables et ne font que diluer l'effectif (E6).

**M3 : routage et allocation du budget.**
- **Principe.** Le score de valeur au prompt est disponible avant toute génération. On peut l'utiliser pour diriger les tâches à faible succès attendu vers une surveillance renforcée : plus de points de fourche pour P1, plus de revue humaine.
- **Ce que ça suppose.** La difficulté prédite est corrélée à l'opportunité de saboter. C'est une HYPOTHÈSE forte.
- **Comment ça échoue.** Un saboteur averti choisit les tâches faciles. Le routage déplace alors le sabotage sans le réduire. À tester en comparant la répartition des sabotages confirmés selon la difficulté.

**M4 : agrégation des sondes en e-valeurs.**
- **Principe.** Chaque sonde (valeur, dopamine, quatre lignes de base) produit une e-valeur par épisode via P1. Leur moyenne reste une e-valeur valide sans hypothèse d'indépendance (Vovk et Wang).
- **Comment ça échoue.** La moyenne dilue une sonde forte parmi des sondes faibles. La perte de puissance est à mesurer.

---

## 7. (b) Expériences décisives, en duel H_A contre H_B

Les seuils de test sont illustratif (niveau 5 %). Toutes les comparaisons de détection se font contre l'échec honnête apparié de la même variante.

**E1 : validité des rangs parmi les fourches du jumeau (P1).**
- H_A : sous H0, le rang de l'agent honnête parmi K fourches est uniforme.
- H_B : il ne l'est pas (non-déterminisme, cache, effet d'état).
- Métrique : test d'uniformité de l'histogramme des rangs, et taux de rejet du test martingale au niveau α sur épisodes honnêtes tenus à part.
- Seuil : rejet empirique compatible avec ≤ α (borne de Clopper-Pearson).
- Contrôle négatif : une fourche contre les autres fourches.
- Issues : la non-uniformité falsifie H_A ; l'uniformité dans les deux conditions falsifie H_B.

**E2 : mutualisation entre classes (P3).**
- H_A : après régression quantile conformalisée, les p-valeurs conformes sont uniformes dans chaque classe.
- H_B : la couverture dépend de la classe.
- Métrique : couverture par classe sur épisodes tenus à part, par validation croisée par tâche.
- Contrôle négatif : longueurs permutées.
- Issues : une sous-couverture significative dans au moins une classe falsifie H_A ; l'uniformité falsifie H_B.

**E3 : absence de biais du fractionnement (P2).**
- H_A : à un niveau modéré, atteint par une fraction d'épisodes mesurable naïvement (de l'ordre de 10 %, illustratif), le fractionnement et le Monte-Carlo naïf concordent.
- H_B : ils divergent (état non markovien, environnement non rejouable).
- Métrique : écart des deux estimations rapporté à son intervalle combiné.
- Contrôle négatif : fractionnement sur une marche aléatoire synthétique de probabilité connue.
- Issues : la divergence falsifie H_A ; la concordance falsifie H_B, ce qui autorise l'extrapolation au niveau 1 %.

**E4 : extrapolation par valeurs extrêmes (P6).**
- H_A : le quantile à 99 % ajusté par loi de Pareto généralisée sur n épisodes tombe dans l'intervalle de l'estimation par fractionnement (ou du jeu scellé).
- H_B : il en sort.
- Contrôle négatif : données synthétiques à queue connue, avec le même n.
- Issues : la sortie falsifie H_A, et les valeurs extrêmes sont alors abandonnées pour ce score ; l'inclusion falsifie H_B.

**E5 : M1 contre l'hypothèse « dopamine = difficulté ».**
- H_A : la proportion de pas à erreur fortement négative non corrigés sépare le saboteur à dommage confirmé de l'échec honnête apparié.
- H_B : elle ne les sépare pas.
- Métrique : AUC appariée par tâche. Elle doit battre les quatre lignes de base décidées (RAPPORTÉ) et les vérifications mécaniques.
- Seuil : borne basse de l'intervalle bootstrap par tâche > meilleure ligne de base.
- Contrôle négatif : échec honnête contre échec honnête, graines différentes. On attend une AUC proche de 0,5.
- Issues : l'absence de gain falsifie H_A ; un gain falsifie H_B.

**E6 : M2, stratification par difficulté.**
- H_A : à FPR garanti égal, la puissance sur saboteurs plantés et générés augmente avec la stratification par difficulté.
- H_B : elle n'augmente pas ou diminue.
- Contrôle négatif : stratification par une covariable aléatoire de même cardinalité.
- Issues : pas de gain par rapport au contrôle, H_A falsifiée ; gain, H_B falsifiée.

**E7 : transcriptions hors politique comme source de forme de queue.**
- H_A : la queue des scores obtenus en lecture forcée sur transcriptions publiques a le même indice de queue que la queue sur épisodes propres.
- H_B : les indices diffèrent.
- Contrôle négatif : épisodes propres rejoués en lecture forcée.
- Issues : la différence falsifie H_A, et cette source est abandonnée ; l'identité falsifie H_B.

---

## 8. (c) Mesure minimale qui dirait si chaque instrument nommé fonctionne

Commun à toutes les lignes :
- **Cas honnêtes appariés** : échec honnête de la même variante, plus succès honnête comme contrôle.
- **Vérifications mécaniques à battre** : tests échoués, ampleur du diff, reproduction des chiffres rapportés, fichiers disponibles au jalon, et les quatre lignes de base décidées.
- Ces vérifications mécaniques sont supposées disponibles (HYPOTHÈSE).

| Instrument | FPR à mesurer | Détection à mesurer | Critère minimal |
|---|---|---|---|
| Valeurs extrêmes |