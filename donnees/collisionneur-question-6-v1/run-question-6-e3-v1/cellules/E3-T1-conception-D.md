# Proposition D — identification causale ou représentation utile ?

**Verdict.** L’apprentissage profond, non supervisé compris, **ne peut pas identifier des causes à partir de la seule distribution observationnelle et sans hypothèse causale**. Deux mondes peuvent produire exactement les mêmes observations tout en ayant des effets différents sous `do(contact)`. Le modèle reçoit alors les mêmes données et ne peut pas restituer deux réponses causales différentes. L’auto-supervision change l’objectif d’apprentissage, pas cet argument.

En revanche, un couple **modèle + données + hypothèses structurelles** peut parfois identifier des facteurs latents ou une structure. Cela n’identifie pas automatiquement « les paramètres qui créent la fertilité » : il faut encore relier les facteurs à une intervention et à un effet structural. Pour une dose de contact \(d\) et des attributs de paire \(z\), l’objet pertinent serait par exemple  
\[
\tau(z)=E[Y(d_1)-Y(d_0)\mid z],
\]
et non le seul recouvrement d’un facteur latent.

**Statuts.** Les pièces sont des affirmations **RAPPORTÉES**, pas des résultats audités : aucun code, journal de randomisation, résultat sur graines ou mesure de fertilité n’est fourni. Les références ci-dessous sont **RAPPORTÉES, non relues ici sur PDF**. Les protocoles proposés sont des **HYPOTHÈSES de conception**. Tous les seuils et budgets numériques sont **illustratifs**.

## (a) Ce que la question suppose sans l’avoir établi

| Présupposé | Statut | Réserve |
|---|---|---|
| La fertilité est une probabilité mesurable et attribuable au croisement. | **HYPOTHÈSE** | Il manque l’unité, la fenêtre, la dose, la règle de provenance et l’issue. Une citation peut mesurer visibilité ou prestige plutôt que naissance par croisement. |
| Il existe des paramètres causaux stables, de petite dimension, communs aux niches et périodes. | **HYPOTHÈSE** | Ils peuvent varier avec les institutions, être nombreux, ou n’exister que pour un mécanisme particulier. |
| Les « paramètres » sont des interventions manipulables. | **HYPOTHÈSE** | Dose et calendrier sont manipulables ; distance de domaine ou âge d’une niche sont plutôt des modérateurs. |
| Identifier des sources latentes identifie leurs effets sur la fertilité. | **HYPOTHÈSE** | Même un recouvrement parfait des latentes ne donne ni orientation du graphe, ni équation structurale, ni effet `do(...)`. |
| L’ordre temporel des citations fournit gratuitement l’ordre causal. | **HYPOTHÈSE** | L’horodatage de publication n’est pas nécessairement celui de l’exposition ou de la conception ; confusion cachée et interférence demeurent. |
| Sous-domaines, pays et décennies sont des environnements valides, avec décalages parcimonieux des seuls mécanismes non causaux. | **HYPOTHÈSE** | Ils peuvent aussi changer l’issue, son instrument de mesure et le mécanisme causal lui-même. |
| Non-gaussianité et séries temporelles suffisent à identifier la structure. | **HYPOTHÈSE** | Des comptes de citations non gaussiens ne démontrent ni bruits structurels indépendants, ni linéarité, ni acyclicité, ni suffisance causale. |
| Les courses offrent des affectations réellement randomisées et une fertilité jugée indépendamment. | **RAPPORTÉ, non audité** | Aucun journal ne permet de vérifier tirage, respect de l’affectation ou indépendance du juge. |
| Les causes apprises dans les courses se transportent à la science humaine. | **HYPOTHÈSE** | Carrières, financement et prestige peuvent modifier les mécanismes. |
| Un modèle non supervisé apprendra surtout taille, âge, prestige et langue. | **HYPOTHÈSE testable** | Le dossier ne fournit aucune sortie de modèle permettant de l’affirmer empiriquement. |

La réponse conv-audit-6 relève donc trop vite que plusieurs hypothèses seraient « offertes par nos données ». Les résultats rapportés — Locatello et al., 2019, *Challenging Common Assumptions in the Unsupervised Learning of Disentangled Representations* ; Hyvärinen et Pajunen, 1999, *Nonlinear Independent Component Analysis: Existence and Uniqueness Results* ; Khemakhem et al., 2020, *Variational Autoencoders and Nonlinear ICA: A Unifying Framework* — ne dispensent pas de vérifier leurs conditions précises.

## (b) Épreuves qui trancheraient

### Épreuve 1 — mondes appariés à vérité plantée

- **H_A :** dans son domaine d’hypothèses, chaque méthode candidate retrouve les facteurs causaux et leur effet, et rejette un accompagnateur corrélé.
- **H_B :** elle ne récupère que des axes prédictifs ou des artefacts, même lorsque son ajustement observationnel est excellent.

Construire des mondes conformes aux hypothèses et des mondes compagnons ne violant qu’une condition : variable auxiliaire invalide, confondeur caché, bruit gaussien, mécanisme changeant ou inversion de la relation causale. Planter une cause, une non-cause corrélée et des mondes observationnellement équivalents mais à effets `do(...)` différents.

- **Métriques :** recouvrement des facteurs vrais après appariement optimal ; erreur sur l’effet causal ; taux de sélection de la non-cause ; stabilité entre graines.
- **Seuil illustratif :** détection ≥ 0,80, fausses alertes ≤ 0,05, intervalles à 95 % sur 200 mondes et 20 graines, avec au moins 20 % de réduction d’erreur face aux contrôles mécaniques.
- **Contrôles négatifs :** auxiliaire permutée, temps inversé, cause à effet nul, étiquettes causales échangées sans changer les observations.
- **Issues :** réussite dans les mondes conformes et rejet dans les mondes violés falsifient **H_B sur ce banc** ; échec de recouvrement ou fausses alertes excessives falsifient **H_A pour cette méthode**. Un contrôle nul déclaré actif falsifie la chaîne d’évaluation.

### Épreuve 2 — les hypothèses dites « gratuites »

- **H_A :** temps et environnements apportent une information stable au-delà du calendrier et de la comptabilité des citations.
- **H_B :** leur signal apparent disparaît après contrôle de taille, âge, popularité, langue et rythme de publication.

Geler les environnements et en réserver un entier avant analyse. Comparer les relations retenues dans tous les environnements à celles d’un modèle mécanique.

- **Métriques :** erreur dans le pire environnement, stabilité du signe, stabilité des variables sélectionnées.
- **Seuil illustratif :** ≥ 10 % de gain hors environnement sur le meilleur contrôle mécanique et signe stable dans ≥ 90 % des environnements.
- **Contrôles négatifs :** fertilité antérieure au contact, variables du futur, étiquettes d’environnement permutées.
- **Issues :** échec falsifie **H_A** ; persistance après tous les contrôles falsifie **H_B comme explication purement mécanique**. Cela ne suffit toujours pas à établir une cause : un confondeur stable peut aussi être invariant.

### Épreuve 3 — intervention prospective jamais vue

- **H_A :** les paramètres retenus prédisent quantitativement l’effet d’une dose ou règle de contact nouvelle et ajoutent de l’information causale.
- **H_B :** un modèle prédictif sans structure causale fait aussi bien, ou les paramètres ne prédisent pas l’intervention.

Randomiser les paires entre doses et règles, réserver une dose et une règle entières, figer le résultat et faire juger à l’aveugle par un juge indépendant de la sélection.

- **Métrique :** erreur sur \(\tau\), différence de probabilité de fertilité à horizon fixe, couverture des intervalles et comparaison à la ligne de base.
- **Seuil illustratif :** erreur absolue ≤ 5 points de pourcentage, bon signe et ≥ 20 % de réduction d’erreur ; effectif déterminé par puissance avant la course.
- **Contrôles négatifs :** contact simulé sans exposition, fertilité pré-randomisation, intervention préenregistrée sans effet.
- **Issues :** prédiction réussie avec avantage falsifie **H_B dans l’organisme** ; échec ou égalité avec la base falsifie **H_A dans sa version incrémentale**. La randomisation fournit l’identification ; le réseau ne fait alors qu’estimer.

### Épreuve 4 — transport externe

- **H_A :** le modèle prédit signe et amplitude d’un estimande commun dans une expérience humaine ou naturelle indépendante.
- **H_B :** ses effets sont propres aux agents, aux juges et à la mesure de l’organisme.

- **Métrique et seuil :** effet externe dans l’intervalle de transport préenregistré ; à défaut d’estimande commun, l’épreuve est non décisive.
- **Contrôles négatifs :** pseudo-dates, résultats antérieurs et paires témoins non exposées.
- **Issues :** réussite falsifie **H_B pour l’environnement testé** ; écart hors tolérance falsifie **H_A-transport**. Un placebo positif falsifie d’abord l’identification externe.

## (c) Mesure minimale de fonctionnement des instruments

Barre commune **illustrative** : détection ≥ 0,80 et fausses alertes ≤ 0,05, sur cas d’apprentissage séparés des cas de test. Les cas honnêtes sont appariés par taille, architecture, budget de réglage et qualité d’ajustement observationnel ; seule la vérité causale ou une hypothèse change.

| Instrument | Détection et fausses alertes minimales | Vérifications mécaniques à battre |
|---|---|---|
| VAE, démêlage non supervisé, contrastif auto-supervisé | Retrouver les facteurs plantés de façon stable ; ne pas déclarer causale la variable compagnon dans les mondes appariés. | ACP/ICA, taille-âge-popularité-langue, permutations et graines multiples. Reconstruction ou vraisemblance ne comptent pas comme détection causale. |
| ICA non linéaire **sans auxiliaire** | Récupération stable malgré des mélanges équivalents ; fausses alertes mesurées sur des rotations ou reparamétrisations laissant les observations inchangées. | ACP, rotations arbitraires, variances et ordre des variables. Un échec attendu ne doit pas être requalifié en estimation causale. |
| ICA non linéaire **avec auxiliaire** | Recouvrement quand les hypothèses exactes tiennent ; alarme nulle lorsque l’auxiliaire est post-outcome, permutée ou insuffisamment variable. | Horodatage seul, étiquette d’environnement seule, auxiliaire mélangée et modèle sans auxiliaire. |
| Représentations causales temporelles | Retrouver facteurs et cibles d’intervention lorsque celles-ci sont connues ; fausses alertes sous cibles mal étiquetées ou confusion latente. | Modèle markovien, dernier état, simples décalages temporels et informations du futur supprimées. |
| LiNGAM / découverte sous non-gaussianité | Orientation et arêtes correctes dans le cas linéaire, acyclique, sans confondeur ; fausses arêtes dans les cas gaussien, non linéaire ou confondu. | Ordre temporel, tri par variance et corrélation. Voir Shimizu et al., 2006, *A Linear Non-Gaussian Acyclic Model for Causal Discovery* — **RAPPORTÉ**. |
| PCMCI sur séries | Détection des liens retardés à taux de fausses arêtes fixé, sur séries régulières ; alarmes sous non-stationnarité et événements irréguliers. | Corrélations croisées, Granger, calendrier et autocorrélation. Voir Runge et al., 2019, *Detecting and Quantifying Causal Associations in Large Nonlinear Time Series Datasets* — **RAPPORTÉ**. |
| Prédiction causale invariante | Couvrir les vrais parents lorsque les environnements n’interviennent pas sur l’issue ; exclure les non-parents lorsque le mécanisme de mesure change. | Modèle groupé, effets propres à l’environnement, prédiction hors environnement. Voir Peters, Bühlmann et Meinshausen, 2016, *Causal Inference by Using Invariant Prediction: Identification and Confidence Intervals* — **RAPPORTÉ**. |
| Double ML, forêts causales, TARNet/DragonNet | Erreur et calibration des effets sous randomisation ou absence de confusion ; aucun effet dans les mondes à effet nul. | Effet constant, régressions séparées du traitement et du résultat, validation croisée. Ces instruments estiment un effet identifié ; ils ne testent pas leur propre identification. |

PCMCI, LiNGAM et l’invariance ne deviennent pas de l’apprentissage profond par juxtaposition à un réseau. L’ablation interne et la régression symbolique restent également des descriptions du modèle appris tant qu’elles ne passent pas les épreuves 1 et 3.

## (d) Ancrage matériel

**HYPOTHÈSE de dimensionnement — chiffres tous illustratifs.**

- Aucun grand modèle de langue n’est nécessaire pour tester l’identification. Utiliser des implémentations ouvertes et figées d’iVAE/TCL, de petits MLP ou GNN, ainsi que `causal-learn`, `lingam`, `tigramite` et `EconML` ; publier code, graines, environnements et générateurs. Un encodeur de texte ouvert peut être ajouté après vérification de version et de licence, mais ne doit pas servir de juge de vérité.
- Épreuves 1–2 : 200 mondes, 20 graines, modèles de 1 à 10 millions de paramètres : environ **1 000–4 000 GPU-heures**, plus préparation CPU et **2–10 To** de stockage.
- Sous-échantillon scientométrique de \(10^6\) travaux et \(10^7\) liens : environ **500–2 000 CPU-heures** et **200–800 GPU-heures**, selon l’usage du texte.
- À prix interne supposé, calcul seul : environ **2 000–20 000 €**. Sont exclus salaires, corpus intégral, licences, annotation humaine et interventions prospectives. Ces dernières doivent être budgétées après le calcul de puissance, non dimensionnées arbitrairement.

La prétention générale « identifier à lui seul, sans hypothèse » est déjà réfutée par l’équivalence observationnelle. Chaque prétention restreinte doit, elle, mourir si elle échoue aux taux de détection/fausses alertes, aux contrôles mécaniques ou à l’intervention inédite. Sans ces garde-fous, le programme mesure une représentation utile, pas une cause de fertilité.

FIN-DE-CELLULE