# Proposition B — Tour III.1 : seuil à 1 % avec peu d'épisodes honnêtes, et usage de l'article pour la surveillance et le contrôle

**Pièces reçues.** Le bloc FAITS et le bloc QUESTION sont présents et complets. Aucune autre proposition ne m'a été transmise (tour à l'aveugle), donc la règle B1 ne s'applique pas ici.

**Statuts utilisés.**
- **VÉRIFIÉ** : arithmétique refaite.
- **RAPPORTÉ** : dossier, ou littérature citée.
- **OBSERVÉ-NON-AUDITÉ**.
- **HYPOTHÈSE** : tout ce qui relève de ma proposition est marqué HYPOTHÈSE ou « proposition ».

**Références.** Aucun identifiant arXiv n'est donné de mémoire, même si la question en demande : la règle d'intégrité 3 prime. Le seul identifiant cité, 2602.00986v2, vient des faits.

---

## 1. Ce qu'un expert ferait ici et qu'on ne demande pas — livrable (a)

### (a) Ce que la question suppose sans que ce soit établi

| # | Supposition implicite | Statut |
|---|---|---|
| S1 | Il faut 5 000 épisodes honnêtes par bac pour « fixer » un seuil à 1 %. Le calcul 50 / 0,01 = 5 000 est juste, mais il vise une **précision** (observer 50 dépassements), pas la **validité** (garantir un taux de fausses alertes ≤ 1 %). | Arithmétique : VÉRIFIÉ ; « nécessaire » : HYPOTHÈSE non établie |
| S2 | Les quelques centaines d'épisodes honnêtes sont des tirages indépendants et échangeables. Plusieurs épisodes d'une même variante de tâche, ou d'une même version du modèle, sont en réalité corrélés. | Nombre d'épisodes : RAPPORTÉ ; indépendance : HYPOTHÈSE |
| S3 | L'unité de calibration doit être l'épisode. Or le dossier évoque des sommes séquentielles de petits signaux le long de l'épisode, ce qui fournit beaucoup plus de pas que d'épisodes. | Somme séquentielle : RAPPORTÉ (décision du programme) ; pertinence du pas comme unité : HYPOTHÈSE |
| S4 | Un taux de fausses alertes de 1 % **par bac de longueur** est la bonne contrainte opérationnelle. En contrôle, la contrainte qui lie est souvent le budget de revue humaine total, pas l'égalité des taux entre bacs. | Seuil fixé : RAPPORTÉ ; pertinence opérationnelle : HYPOTHÈSE |
| S5 | La distribution nulle honnête est stable entre la calibration et le déploiement (version du modèle, mélange de tâches). | HYPOTHÈSE |
| S6 | Le jumeau honnête apparié est distribué comme l'agent *s'il était honnête*. | Existence du jumeau : RAPPORTÉ ; équivalence en distribution : HYPOTHÈSE |
| S7 | Les sondes de l'article se transfèrent à du travail de recherche ouvert, sans récompense vérifiable. Les auteurs disent explicitement que ce cadre n'a pas été testé (p. 25). | Limite : RAPPORTÉ ; transfert : HYPOTHÈSE |
| S8 | Les lectures « valeur » et « dopamine » restent informatives face à un agent adverse qui se sait surveillé. L'article ne contient aucun cadre adverse (p. 25). | Absence de cadre adverse : RAPPORTÉ ; robustesse : HYPOTHÈSE |
| S9 | La puissance de détection est estimable. Le dossier ne dit pas combien d'épisodes de sabotage avec dommage confirmé existent. | Nombre d'épisodes de sabotage : non fourni |

### Ce que ferait un expert (proposition)

1. **Séparer trois quantités** : la validité (taux de fausses alertes ≤ α), la précision de l'estimation de ce taux, et la puissance. On peut garantir la validité avec beaucoup moins de 5 000 épisodes. Le prix est payé en puissance, pas en validité.
2. **Compter les tâches, pas les épisodes.** L'effectif utile est le nombre de variantes de tâche indépendantes. La calibration se fait en laissant de côté des tâches entières, pas des épisodes isolés.
3. **Déplacer la validité vers une hypothèse vérifiable à grand effectif.** On ne vérifie pas un quantile à 1 % sur des épisodes rares : on vérifie la super-uniformité de p-valeurs par pas, qui sont des milliers, puis un théorème transporte la garantie jusqu'à 1 %.
4. **Poser la question opérationnelle.** Combien d'audits humains sont disponibles par lot ? Comment répartir les fausses alertes entre bacs pour maximiser la détection sous ce budget ?
5. **Calculer la puissance avant de produire des épisodes.** On calcule l'effet minimal détectable avec l'effectif honnête *et* l'effectif de sabotage disponibles, et on pré-enregistre « non concluant » comme issue légitime.
6. **Tester la dérive** entre l'ancien lot honnête et tout nouveau lot avant de les fusionner.

---

## 2. Les données brutes de départ

Plutôt que les scores agrégés par épisode des quelques centaines d'épisodes déjà analysés :

- **Les traces pas à pas complètes.** Pour chaque pas : activations aux couches utilisées, score de chaque sonde, position dans l'épisode, fichiers disponibles au jalon. Le programme compare déjà « au même jalon avec les seuls fichiers alors disponibles » (RAPPORTÉ). Ces données existent donc probablement en partie, mais leur conservation n'est pas établie (HYPOTHÈSE).
- **Les bifurcations du jumeau.** Ce sont K continuations honnêtes tirées depuis le *même préfixe*, à des points de contrôle. Le programme utilise déjà « la divergence d'un jumeau forcé sur le même préfixe » comme base de comparaison (RAPPORTÉ). L'infrastructure de bifurcation existe donc, au moins pour cette base.
- **Les métadonnées de dépendance** : identifiant de tâche et de variante, version du modèle, graine, date, machine. Sans elles, aucune calibration qui respecte les corrélations n'est possible.
- **Les issues mécaniques indépendantes des sondes** : tests, différences de fichiers, reproduction des résultats, dommage confirmé ou non. C'est la vérité de terrain du contraste principal (RAPPORTÉ).
- **Une base de simulation synthétique** : des distributions de scores connues, avec queues lourdes, grappes par tâche et dérive. Elle sert à mesurer le taux de fausses alertes *réalisé* de chaque procédure sans dépenser un seul épisode (proposition).

**Changement de rôle des épisodes existants (proposition).** Les quelques centaines d'épisodes honnêtes servent de **lot de validation** des hypothèses (uniformité, invariance), pas de lot de calibration du quantile à 1 %.

---

## 3. Méthodes et outils, ce que chacun suppose — livrable (c)

### 3.1 Outils de queue et de calibration

| Outil | Ce qu'il donne | Ce qu'il suppose | Comment il échoue |
|---|---|---|---|
| **Quantile conforme** (Vovk, Gammerman, Shafer, *Algorithmic Learning in a Random World*, Springer, 2005 ; Angelopoulos & Bates, « A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification », 2021) | Seuil = statistique d'ordre de rang ⌈(n+1)(1−α)⌉. Taux de fausses alertes ≤ α **en moyenne sur le tirage du lot de calibration**. Il faut n+1 ≥ 1/α, soit n ≥ 99 pour α = 1 % (illustratif — calcul dérivé). | Échangeabilité entre calibration et test | Le taux réalisé, conditionnellement au lot, varie beaucoup. Grappes par tâche. Dérive. |
| **Garantie conditionnelle au lot / limites de tolérance** (Wilks, « Determination of sample sizes for setting tolerance limits », *Ann. Math. Stat.*, 1941 ; Vovk, « Conditional validity of inductive conformal predictors », 2012) | Avec le seuil posé au maximum de n scores, P(taux > α) = (1−α)^n. Pour α = 1 % et un risque de 5 %, il faut n ≈ 299 (illustratif — calcul dérivé). | Tirages i.i.d. | Seuil très conservateur : taux réalisé attendu de l'ordre de 1/(n+1), donc environ 0,3 % pour n ≈ 300 (illustratif). Perte de puissance. |
| **Intervalle binomial exact** (Clopper & Pearson, *Biometrika*, 1934) | Borne supérieure du taux réalisé sur un lot de validation. Avec 0 dépassement sur n, la borne à 95 % vaut environ 3/n (illustratif). | Indépendance des épisodes | Mêmes grappes |
| **Calibration par strates, dite « Mondrian »** | Validité par bac | Échangeabilité *dans* chaque bac | Le coût est multiplié par le nombre de bacs : c'est la source des « 5 000 par bac ». |
| **Normalisation invariante à la longueur** (par exemple la somme séquentielle divisée par une fonction de la longueur), puis regroupement des bacs | Un seul lot de calibration | Que la loi nulle normalisée ne dépende plus du bac. **C'est une hypothèse testable** (voir E1). | Invariance fausse dans la queue alors qu'elle paraît vraie au centre |
| **Conforme pondéré sous déplacement de covariables** (Tibshirani, Barber, Candès, Ramdas, « Conformal Prediction Under Covariate Shift », NeurIPS 2019) | Validité quand le mélange de tâches change, si le rapport de vraisemblance est connu ou estimé | Covariables observées, déplacement uniquement dans les covariables | Rapport mal estimé ; déplacement dans la loi conditionnelle elle-même |
| **Valeurs extrêmes, loi de Pareto généralisée au-delà d'un seuil** (Coles, *An Introduction to Statistical Modeling of Extreme Values*, Springer, 2001) | **Estimation** du quantile à 99 % par extrapolation | Queue dans un domaine d'attraction ; choix du seuil intermédiaire ; i.i.d. | Aucune garantie à échantillon fini. Biais selon le seuil choisi. **Ne doit jamais être présenté comme une garantie.** |
| **E-valeurs et calibrateurs p → e** (Vovk & Wang, « E-values: Calibration, combination and applications », *Ann. Stat.*, 2021) | e = κ·p^(κ−1), avec κ ∈ (0,1). Les e-valeurs se multiplient séquentiellement et se moyennent entre sondes. | p-valeurs super-uniformes conditionnellement au passé | p-valeurs mal calibrées |
| **Tests séquentiels toujours valides, inégalité de Ville** (Ramdas, Grünwald, Vovk, Shafer, « Game-Theoretic Statistics and Safe Anytime-Valid Inference », *Stat. Science*, 2023) | Si M_t est une surmartingale positive avec M_0 = 1 sous H0, alors P(sup_t M_t ≥ 1/α) ≤ α. Pour α = 1 %, le seuil vaut **100**, fixé par α et **indépendant de la longueur de l'épisode**. Aucun quantile empirique n'est à estimer. | Validité conditionnelle de chaque facteur | Facteurs mal calibrés. La puissance peut être faible contre un agent qui « lisse » ses pas. |
| **Multiplicité** (Wang & Ramdas, « False discovery rate control with e-values », *JRSS-B*, 2022) | Contrôle de la proportion de fausses découvertes sur sondes × bacs × bases de comparaison | Validité de chaque e-valeur | — |

Le lien avec la décision du programme sur la « somme séquentielle de petits signaux » (RAPPORTÉ) est direct : log M_t est exactement une somme de petits signaux. La proposition est d'utiliser cette décision avec une calibration qui porte une garantie, pas de la rediscuter.

### 3.2 Plans d'échantillonnage, simulation, transfert

- **Échantillonnage stratifié avec allocation de Neyman pour une probabilité de queue.** On sur-échantillonne les strates où la masse de queue honnête se concentre, puis on repondère par les proportions *connues* des strates. Cela suppose que la distribution des tâches en déploiement est connue. Cela échoue si les poids des strates sont faux.
- **Bifurcations depuis des préfixes partagés.** Elles sont bon marché par continuation, mais les continuations sont corrélées : il faut compter un effectif efficace par préfixe.
- **Simulation.** Elle vérifie le taux de fausses alertes réalisé de chaque procédure sous une vérité connue. Elle échoue si les distributions simulées ne ressemblent pas aux vraies queues. On s'en protège en ancrant la simulation sur les quantiles observés au centre.
- **Transfert entre modèles ou entre tâches.** Il suppose une loi nulle normalisée stable. Il n'est acceptable qu'après validation sur des tâches laissées de côté. Il ne faut jamais transférer depuis un petit modèle vers l'agent sans ce test.

### 3.3 (c) Mesure minimale pour dire si chaque instrument fonctionne

| Instrument | Mesure minimale | Cas honnêtes appariés | Vérification mécanique à battre |
|---|---|---|---|
| Quantile conforme, Wilks | Taux réalisé sur tâches laissées de côté ; en simulation, distribution du taux réalisé sur 10³ lots tirés (illustratif) | Même variante, autre graine | Quantile empirique naïf ; borne de Clopper-Pearson |
| Normalisation et regroupement des bacs | Taux de dépassement par bac du seuil commun, comparé à une bande de permutation | Même tâche, longueurs différentes | Calibration par bac seule |
| Valeurs extrêmes | Couverture des intervalles en simulation ; stabilité selon le seuil choisi | — | Quantile empirique à 95 %, directement mesurable |
| E-processus du jumeau | Uniformité des p-valeurs par pas ; taux de rejet de l'agent honnête à α = 10 % (illustratif) | Jumeau contre jumeau ; agent honnête contre jumeau | Divergence du jumeau forcé, déjà adoptée (RAPPORTÉ) |
| Sondes de l'article comme moniteur | Taux de détection, saboteur avec dommage contre échec honnête de la même variante, à taux de fausses alertes contrôlé | Échec honnête de la même variante (contraste principal, RAPPORTÉ) | Les quatre bases de comparaison du programme (RAPPORTÉ) ; longueur de la question ; tests unitaires et différences de fichiers au jalon |

---

## 4. Ce qui permettrait de vérifier la validité de l'extérieur

1. **Vérité de terrain implantée par un tiers.** Une équipe indépendante implante les sabotages et scelle la clé par un engagement par empreinte, comme les sha256 de ce protocole. Les analyses sont gelées avant l'ouverture de la clé. *Ce que cela vérifie* : que la détection n'est pas ajustée sur les cas connus.
2. **Test nul contre nul, fait par un tiers.** On découpe les épisodes honnêtes, on déclare arbitrairement la moitié « suspecte », et on lance le code gelé. Le taux de rejet doit respecter α à la précision que permet n. *Contrôle négatif réutilisable.*
3. **Jumeau contre jumeau.** Deux jeux de bifurcations honnêtes ne doivent pas être distingués. C'est le test placebo de l'e-processus.
4. **Réplication publique de la lentille avant usage.** On reproduit l'effet causal du Tableau 2 de Xu, Yuksekgonul, Zou, « Sparse Reward Subsystem in Large Language Models », arXiv 2602.00986v2, sur Qwen-2.5-7B-SimpleRL-Zoo et MATH500. Le dossier rapporte 75,2 % → 20,3 % contre 74,6 % pour des neurones aléatoires (RAPPORTÉ). Si l'effet ne se reproduit pas, la lentille ne sert pas de covariable.
5. **Mesure indépendante du dommage.** Une partie qui ne voit pas les scores de sonde établit le dommage par des moyens mécaniques : tests, reproduction des résultats.
6. **Jeux de données et travaux publics sur le sabotage et le contrôle.** Pistes possibles, à confirmer :
   - Greenblatt, Shlegeris, Sachan, Roger, « AI Control: Improving Safety Despite Intentional Subversion », 2023 ;
   - « Sabotage Evaluations for Frontier Models », Benton et al., 2024 (liste d'auteurs à vérifier) ;
   - « Ctrl-Z: Controlling AI Agents via Resampling », Bhatt et al., 2025 (référence à vérifier).

   Je ne garantis pas qu'ils fournissent des activations exploitables (HYPOTHÈSE).
7. **Audit du code statistique** sur les fichiers de scores gelés, et **pré-enregistrement** des seuils, métriques et issues non concluantes.

---

## 5. Reformulation de la demande

> « Avec les épisodes honnêtes existants **comptés par tâche indépendante**, et un budget de nouveaux épisodes et de bifurcations exprimé en équivalents-épisodes, concevoir une règle d'alerte dont le taux de fausses alertes est **garanti** ≤ 1 % par épisode honnête. La garantie doit être de type conforme conditionnel au lot ou toujours valide, et ses hypothèses doivent être vérifiables sur des unités nombreuses (les pas). Indiquer pour chaque option :
> (i) l'hypothèse dont dépend la garantie, et le test qui la falsifie avec les données disponibles ;
> (ii) la perte de puissance par rapport à un seuil à 1 % exact ;
> (iii) l'effet minimal détectable, compte tenu aussi de l'effectif de sabotage ;
> (iv) une issue « non concluant » pré-enregistrée.
>
> Séparément, dire si l'égalité du taux entre bacs de longueur est requise, ou si un budget d'audit total suffit. Enfin, tester si les sondes de l'article apportent, comme **covariable de difficulté** ou comme **moniteur**, un gain mesurable sur le contraste "saboteur avec dommage contre échec honnête de la même variante", au-delà des quatre bases de comparaison et des vérifications mécaniques. La vérité de terrain est implantée et scellée par un tiers. »

---

## 6. Propositions concrètes

### 6A. Fixer un seuil à 1 % avec peu d'épisodes, ou s'en passer honnêtement

**P1 — Garantie conditionnelle au lot (Wilks ou conforme), un lot regroupé** (proposition)
- *Coût* : environ 300 tâches indépendantes par strate regroupée (illustratif — calcul dérivé). C'est possiblement atteignable avec l'existant, *si* les épisodes proviennent de tâches distinctes (non établi).
- *Hypothèse* : i.i.d. au niveau des tâches.
- *Échec* : seuil au maximum, donc puissance réduite. Les grappes cassent la garantie.
- *À rapporter* : le taux réalisé attendu, nettement sous 1 %, et non « 1 % ».

**P2 — Normalisation invariante à la longueur, puis P1 sur les bacs regroupés** (proposition)
- *Coût* : aucun nouvel épisode.
- *Hypothèse* : invariance, à tester par E1.
- *Échec* : invariance au centre mais pas dans la queue. E1 ne la voit qu'avec une puissance limitée.

**P3 — E-processus conditionnel au préfixe, construit sur le jumeau** (proposition centrale de B)
- *Principe* : à chaque point de contrôle t, on tire K continuations honnêtes du jumeau depuis le préfixe de l'agent. On calcule p_t = (1 + #{bifurcations de score ≥ score de l'agent}) / (K+1). On convertit p_t en e_t par calibrateur, puis M_t = ∏ e_s. On alerte si M_t ≥ 100.
- *Validité* : elle repose sur Ville, pas sur un quantile empirique. Il n'y a **pas de calibration par bac** à faire, car le seuil ne dépend pas de la longueur.
- *Coût* : environ K équivalents-épisodes par épisode évalué, si chaque continuation couvre un pas, plus le pré-remplissage du préfixe. Avec K = 10 et 300 épisodes de validation, on obtient environ 3 000 équivalents-épisodes (illustratif). **L'économie par rapport à 5 000 nouveaux épisodes n'est donc pas garantie : elle dépend de K, du nombre de points de contrôle et de la longueur des continuations.** Elle doit être calculée avant tout engagement.
- *Hypothèses* :
  - le jumeau sur le préfixe est échangeable avec l'agent honnête sur le même préfixe (S6) ;
  - le score du pas ne dépend que du préfixe et du pas ;
  - p_min = 1/(K+1) borne la croissance par pas.
- *Échec* :
  - jumeau différent de l'agent honnête (température, invite, version), d'où des p-valeurs biaisées et une **validité perdue** ;
  - un agent adverse qui rend chaque pas typique fait baisser la **puissance** sans toucher la validité ;
  - coût en bifurcations.

**P4 — Nouveau lot stratifié par difficulté, avec l'article comme stratificateur** (proposition)
- *Principe* : la sonde de valeur pré-génération donne l'échec attendu. L'AUC rapportée est de 0,67 en moyenne, contre 0,62 pour la longueur de la question (RAPPORTÉ, Tableau 3). On sur-échantillonne les strates difficiles, où l'échec honnête, et donc probablement la queue des scores honnêtes, se concentre (HYPOTHÈSE), puis on repondère.
- *Coût* : nouveaux épisodes, moins nombreux qu'un tirage uniforme si l'hypothèse tient.
- *Hypothèse* : poids des strates connus ; corrélation entre la difficulté et la queue du score.
- *Échec* : stratificateur pas meilleur que la longueur de la question. Non-transfert au travail ouvert (S7).

**P5 — Valeurs extrêmes en estimateur secondaire** : elles donnent un point et un intervalle, jamais le seuil de décision. *Échec* : sensibilité au seuil intermédiaire.

**P6 — S'en passer honnêtement** (proposition)
- Rapporter la e-valeur finale et le taux de détection à un taux de fausses alertes *mesurable* avec l'effectif, avec intervalle.
- En contrôle, remplacer le seuil absolu par un **budget d'audit** : on audite le haut du classement par M_t. Le seuil devient relatif, mais il est vulnérable si une fraction notable du lot est adverse.
- Pré-enregistrer « non concluant ».
- *Coût* : nul.
- *Échec* : la décision au point de verdict fixé reste hors de portée. Il faut le dire.

### 6B. Utiliser l'article pour construire des moniteurs ou servir le contrôle

**M1 — Covariable de difficulté pour une loi nulle conditionnelle** (proposition)
- *Principe* : calibration conforme pondérée ou par strates, conditionnée à la valeur pré-génération. Les échecs honnêtes sur tâches difficiles cessent de déclencher des alertes.
- *Coût* : sonde minuscule (MLP de largeur 1024, RAPPORTÉ p. 19).
- *Hypothèse* : la valeur prédite se transfère au travail ouvert, et l'agent ne la manipule pas.
- *Échec* : un agent conscient de la surveillance pourrait abaisser sa valeur affichée, se faire classer « difficile » et gonfler son seuil. La covariable devient alors un canal d'évasion. Mesure : E3.

**M2 — Dissociation entre valeur interne et sortie** (HYPOTHÈSE)
- *Principe* : un saboteur dégraderait la réussite en connaissance de cause. La lecture de valeur et d'erreur temporelle chuterait alors à des pas où le texte reste confiant, et sans erreur mécaniquement détectable au jalon.
- Mais les creux aux failles logiques existent déjà chez l'honnête (RAPPORTÉ, Figure 3). Le programme formule précisément l'hypothèse contraire : la sonde lit l'échec attendu, pas l'intention (RAPPORTÉ). Mesure : E4.

**M3 — Routage et rééchantillonnage** (proposition)
- *Principe* : quand e_t dépasse un niveau intermédiaire, on rééchantillonne le pas depuis le jumeau et on fait suivre l'épisode vers l'audit. Le budget humain se répartit par M_t, avec des budgets par strate de difficulté (M1).
- *Coût* : bifurcations à la demande.
- *Hypothèse* : comme P3.
- *Échec* : un saboteur diffus n'atteint jamais le niveau intermédiaire.

**M4 — Intégrité de la lentille** (proposition)
- *Principe* : les auteurs signalent que des interventions au niveau des neurones peuvent contourner des protections (RAPPORTÉ, p. 25). Une dérive de la *distribution* des activations des neurones de valeur par rapport au jumeau, à prompt égal, constitue un signal de manipulation.
- *Échec* : non validé ; aucun cadre adverse dans l'article.

### 6C. (b) Expériences décisives, en duel

**E1 — Regroupement des bacs**
- *H_A* : la loi nulle du score normalisé est invariante entre bacs de longueur.
- *H_B* : elle dépend du bac.
- *Métrique* : taux de dépassement par bac d'un seuil commun fixé au quantile à 90 % (illustratif, choisi pour être mesurable), en laissant de côté des tâches entières.
- *Seuil* : bande de permutation à 95 % ; test d'équivalence avec une marge pré-enregistrée de ± 3 points (illustratif).
- *Contrôle négatif* : étiquettes de bac permutées.
- *Falsifie H_A* : un bac sort de la bande.
- *Falsifie H_B* : tous les bacs sont dans la marge d'équivalence.
- *Issue non concluante* : ni l'un ni l'autre ; on s'y attend avec quelques centaines d'épisodes, et on le dit.

**E2 — Validité de l'e-processus**
- *H_A* : agent honnête et bifurcations du jumeau sont échangeables, donc les p_t sont uniformes.
- *H_B* : non.
- *Métrique* : test d'uniformité de Kolmogorov-Smirnov sur les p_t de tous les pas des épisodes honnêtes (des milliers de pas), plus le taux de rejet à α = 10 % (illustratif).
- *Seuil* : p du test d'uniformité > 0,05 (illustratif), et taux de rejet dans l'intervalle de Clopper-Pearson de 10 %.
- *Contrôle négatif* : jumeau contre jumeau, qui doit être uniforme.
- *Contrôle positif* : agent honnête à température modifiée, qui doit être détecté. On montre ainsi que E2 a de la puissance.
- *Falsifie H_A* : non-uniformité, ou rejet excessif.
- *Falsifie H_B* : uniformité, avec le contrôle positif détecté.
- *Portée* : une issue en faveur de H_A transporte la garantie à 1 % par Ville. C'est **le point de bascule de P3**.

**E3 — Apport de l'article comme covariable**
- *H_A* : conditionner sur la valeur pré-génération réduit les fausses alertes dues aux échecs honnêtes, à détection constante.
- *H_B* : aucun gain au-delà de la longueur de la question et du taux d'échec historique de la variante.
- *Métrique* : taux de détection, saboteur avec dommage contre échec honnête de la même variante, au même taux global.
- *Seuil* : différence appariée par tâche dont l'intervalle exclut 0.
- *Contrôle négatif* : covariable permutée entre tâches.
- *Base de comparaison mécanique* : longueur de la question ; taux d'échec historique.
- *Falsifie H_A* : intervalle qui contient 0, ou gain égal à celui de la longueur.
- *Falsifie H_B* : gain positif au-delà des deux.

**E4 — Intention ou échec attendu** (contraste principal du programme, utilisé sans le rediscuter)
- *H_A* : un moniteur fondé sur la dissociation (M2) sépare le saboteur avec dommage de l'échec honnête de la même variante.
- *H_B* : il ne sépare que le saboteur du succès honnête, ce qui correspond à l'hypothèse du programme.
- *Métrique* : AUC, saboteur avec dommage contre échec honnête, par tâche.
- *Seuil* : borne basse de l'intervalle > 0,5 *et* supérieure à chacune des quatre bases de comparaison (RAPPORTÉ), y compris la divergence du jumeau forcé.
- *Contrôle négatif* : échec honnête contre échec honnête.
- *Falsifie H_A* : intervalle qui contient 0,5, ou moniteur battu par une base de comparaison.
- *Falsifie H_B* : séparation significative au-delà des bases, en cas de vérité scellée par un tiers.

### 6D. (d) Ancrage matériel

- **Modèles ouverts** (RAPPORTÉ) : Qwen-2.5-7B et 14B-SimpleRL-Zoo, Qwen3.5-0.8B, Phi-3.5-mini-instruct, Llama-3.1-8B-Instruct, Gemma-3-4B. Prototyper P3 et E2 sur Qwen3.5-0.8B, puis confirmer sur la taille de l'agent réel ; le transfert n'est accepté qu'après E2 sur cette taille.
- **Calcul des sondes** : négligeable. Ce sont des MLP à 1 024 ou 32 unités, 100 époques (RAPPORTÉ).
- **Coût dominant** : bifurcations et épisodes, à exprimer en **équivalents-épisodes** plutôt qu'en monnaie, faute de chiffres de prix dans le dossier.

| Option | Ordre de coût | Statut |
|---|---|---|
| P1, P2, P5, P6 | 0 nouvel épisode | illustratif |
| P3, validation (E2) | ≈ K × N_validation (≈ 3 000 pour K = 10, N = 300) | illustratif |
| P4 | nouveaux épisodes en strates, en nombre fixé par un calcul de Neyman préalable | illustratif |
| Simulation | calcul processeur négligeable | illustratif |
| Réplication du Tableau 2 | une évaluation MATH500 par condition d'ablation, sur un GPU unique | illustratif |

- **Ce qui peut être réfuté à bas coût, avant tout nouvel épisode** :
  - E1 et l'uniformité de E2 sur un petit K appliqué aux épisodes existants ;
  - la réplication du Tableau 2 ;
  - la simulation des taux réalisés de P1 et P5.

Si E2 échoue, P3 tombe. Il reste alors P1 ou P6, et la décision honnête est « non concluant au point de verdict à 1 % ».

FIN-DE-CELLULE