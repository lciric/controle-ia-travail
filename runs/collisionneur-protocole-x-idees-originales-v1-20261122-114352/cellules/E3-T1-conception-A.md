# Proposition A — Tour III.1 (conception ciblée, à l'aveugle)

## 0. Constats d'intégrité

- **Bloc FAITS :** il ne contient aucun fait porteur de statut. Il reproduit mot pour mot la question, avec la même empreinte déclarée, que je ne peux pas recalculer. La base factuelle transmise est donc vide.
- **Source :** la « réponse 28 de Fable, section C7 » n'est pas transmise et l'identifiant « 05c72e05… » est tronqué. Je n'en infère rien.
- **B1 :** aucune autre proposition n'est visible à ce tour ; la règle est sans objet.
- **Statuts :** rien ci-dessous n'est VÉRIFIÉ. Les présupposés sont des HYPOTHÈSES. La littérature est RAPPORTÉE de mémoire : j'en garantis l'attribution, pas le détail du contenu. Les protocoles sont des propositions de conception, pas des résultats.
- **Chiffres :** la question interdit tout chiffre sans source, alors que le livrable demande seuils et coûts. Je ne donne aucun chiffre empirique. Les seuils sont des paramètres à préenregistrer (q, τ, δ, ε, θ) et toute valeur numérique est marquée « illustratif ».

## (a) Ce que la question suppose sans que ce soit établi

| # | Présupposé | Statut | Ce qui casse s'il est faux |
|---|---|---|---|
| P1 | Une « idée » est une unité dénombrable : on sait décider sans modèle si deux sorties sont la même idée. | HYPOTHÈSE | La rareté n'est pas définie : elle varie avec la granularité. |
| P2 | Le contrôle est « indépendant des modèles ». | HYPOTHÈSE | Ses erreurs peuvent être corrélées à ce que les modèles proposent, par corpus communs ou par boucle de sélection. |
| P3 | La fiabilité sur cas à vérité connue se transporte aux idées rares. | HYPOTHÈSE | Les cas connus sont, par construction, peu rares ; le décalage porte sur l'axe étudié. |
| P4 | La rareté est une propriété de l'idée. | HYPOTHÈSE | Elle dépend du protocole de tirage : invite, température, versions, composition du système. |
| P5 | Rare pour le système vaut original. Le titre dit « idées originales », le corps dit « rarement proposées ». | HYPOTHÈSE | Une idée rare peut être connue, mal formée ou simplement du bruit. |
| P6 | Confirmée vaut valable. | HYPOTHÈSE | Le contrôle mesure une validité sur son critère ; une trivialité vraie passe. |
| P7 | Des appels « indépendants » existent. | HYPOTHÈSE | Les tirages d'un même modèle ne sont indépendants que conditionnellement à l'invite ; des modèles distincts partagent des données. |
| P8 | Le « coût total » est commensurable entre génération et contrôle. | HYPOTHÈSE | Si le contrôle domine le coût, l'optimum se déplace vers le filtrage. |
| P9 | « Sans augmenter les fausses découvertes » a un sens unique. | HYPOTHÈSE | Proportion parmi les confirmées et nombre par unité de coût donnent des verdicts opposés. |
| P10 | Il existe des « puits étroits » (titre). | HYPOTHÈSE | Le corps déclare l'ignorer ; si la queue est ouverte, le goulot est le contrôle, pas la génération. |
| P11 | Toute idée est soumissible au contrôle. | HYPOTHÈSE | Si un modèle doit formaliser l'idée pour la tester, son jugement rentre par cette porte. |

## Question 5 — le problème est partiellement mal posé ; je le repose

Les défauts sont P1, P4, P5, P9 et la contradiction entre le titre et le corps (P10). Je repose le problème ainsi :

> Étant donné un protocole de tirage de référence P₀ figé, un canoniseur mécanique κ et un contrôle T calibré par strate de rareté sur des cas à vérité connue disjoints de ceux qui servent à la sélection : maximiser, à coût C fixé (génération + contrôle), le nombre de classes κ de masse estimée sous P₀ inférieure à τ et confirmées sur cas frais, sous un taux de fausses découvertes ≤ q vérifié par un oracle coûteux sur échantillon.

Deux points en découlent :
- La rareté se mesure toujours sous P₀, jamais sous la distribution de l'intervention. Sinon une intervention rendrait une idée « fréquente » du seul fait de la proposer.
- L'originalité au sens du monde sort du périmètre : elle n'est pas mesurable sans corpus externe.

## Question 1 — mesurer sans juge-modèle

**Identité d'une idée (κ).** Je propose une signature comportementale : le vecteur des verdicts ou prédictions de l'idée sur une batterie fixe de cas-sondes. Deux sorties de même signature forment une classe. Cela exige des idées exécutables (P11). À défaut, on prend une forme normale syntaxique. Les plongements sont un jugement de modèle et sont exclus comme mesure primaire.

**Rareté.** C'est la masse de la classe sous P₀, estimée par comptage sur N tirages.
- La probabilité qu'un tirage supplémentaire tombe dans une classe jamais vue s'estime par f₁/N, où f₁ est le nombre de classes vues une seule fois. Source : Good (1953), « The population frequencies of species and the estimation of population parameters » ; RAPPORTÉ, certitude élevée.
- Cette quantité répond directement à « les appels reviennent-ils aux mêmes idées ? ».
- Une classe vue une fois n'a qu'une borne supérieure de masse, d'ordre 1/N ; la résolution ne va pas plus bas.

**Validité.** On calcule une p-valeur conforme du score de contrôle contre un jeu de calibration d'idées fausses connues, puis on applique une procédure de contrôle du taux de fausses découvertes.
- Sources : Bates, Candès, Lei, Romano et Sesia (2023), « Testing for outliers with conformal p-values » ; Benjamini et Hochberg (1995), « Controlling the false discovery rate: a practical and powerful approach to multiple testing ». RAPPORTÉ ; certitude élevée sur l'attribution, moyenne sur les conditions exactes de dépendance.
- La garantie vaut sous échangeabilité entre fausses idées connues et fausses idées proposées. C'est précisément P3.

**Valeur au-delà de la validité.** Je la mesure par le gain marginal : les cas frais résolus par l'idée et par aucune classe fréquente confirmée. L'idée doit en outre battre un générateur nul mécanique, par énumération ou combinaison aléatoire de même forme. L'importance scientifique n'est pas mesurée (limite L7).

## (b) Expériences décisives (question 3)

Conventions communes :
- Valeurs illustratives : q = 0,10 ; δ = 0,05 ; ε = 0,20 ; intervalles à 95 %.
- Une hypothèse est falsifiée quand l'intervalle est entièrement du mauvais côté du seuil.
- Si l'intervalle chevauche le seuil, l'issue est « non tranchée ». C'est un défaut de puissance, à déclarer et à ne pas interpréter.
- Le banc est un domaine à vérité totale, où un oracle coûteux donne la vérité de toute idée (voir d).

### D1 — Puits ou queue ouverte

- **H_A (puits) :** les tirages reviennent aux mêmes classes ; f₁/N < θ au budget N.
- **H_B (queue ouverte) :** f₁/N ≥ θ.
- **Métrique :** f₁/N par source (modèle × invite), avec intervalle par bootstrap, et prédiction en moitiés : la première moitié prédit le nombre de classes nouvelles de la seconde.
- **Contrôle négatif :** générateur synthétique de distribution connue (uniforme, puis à queue lourde) passé dans la même chaîne. L'estimateur doit retrouver la couverture plantée.
- **Si H_A est falsifiée :** la prémisse du titre tombe, et les interventions de diversification perdent leur motif. Le goulot devient le contrôle.
- **Si H_B est falsifiée :** « tirer davantage » est abandonné comme stratégie.

### D2 — La queue est-elle du signal ou du bruit ?

- **H_A :** les classes rares (masse ≤ τ sous P₀) sont vraies selon l'oracle plus souvent que des idées nulles mécaniques appariées en forme.
- **H_B :** elles le sont à un taux inférieur ou égal.
- **Métrique :** rapport des taux de vérité selon l'oracle. On n'utilise pas le contrôle, pour éviter la circularité.
- **Seuil :** rapport > 1.
- **Contrôles négatifs :** permutation des étiquettes de rareté ; classes fréquentes contre idées nulles. Si même les fréquentes ne battent pas le nul, le banc est invalide.
- **Si H_A est falsifiée :** j'abandonne toutes les interventions qui cherchent la rareté dans ce domaine.
- **Si H_B est falsifiée :** la thèse « le mode contient tout ce que le système sait » tombe.
- **Sous-produit :** le taux de vérité par strate de rareté donne le taux de base qui manque à P3.

### D3 — Le contrôle se transporte-t-il vers la queue ?

- **H_A :** la proportion de fausses parmi les confirmées est la même en strate rare et en strate fréquente, à δ près.
- **H_B :** elle est plus élevée en strate rare, de plus de δ.
- **Métrique :** différence des proportions auditées par l'oracle sur échantillon aléatoire de confirmées.
- **Contrôles négatifs :** étiquettes de rareté permutées ; idées nulles mécaniques, dont le taux de confirmation doit égaler le niveau nominal.
- **Si H_A est falsifiée :** la clause « fiable sur cas connus » ne couvre pas la cible. Toute intervention doit alors porter un seuil par strate, ou être abandonnée.
- **Si H_B est falsifiée :** l'objection de taux de base est écartée sur ce banc, et seulement sur ce banc.

### D4 — Gabarit commun aux interventions

À coût C égal, le coût du contrôle est inclus et l'audit par oracle reste hors budget, identique pour tous les bras.
- **Rendement R :** nombre de classes rares sous P₀, confirmées sur cas frais au niveau q, par unité de coût.
- **H_A :** R_intervention / R_base > 1 + ε, et l'écart des proportions auditées de fausses découvertes est ≤ δ.
- **H_B :** rapport ≤ 1 + ε, ou écart > δ.
- **Contrôles négatifs :** essai A/A (base contre base, graines différentes), qui donne la distribution nulle du rapport ; placebo de même longueur d'invite et de contenu non informatif.
- **Si H_B est retenue :** l'intervention est abandonnée.
- **Si H_A est retenue :** la thèse « à coût égal, rien ne bat le tirage simple » est falsifiée.

Chaque intervention ajoute un duel propre, donné ci-dessous.

## Question 2 — interventions

**Garde-fou commun (ce n'est pas une intervention).** La confirmation se fait sur cas frais, avec p-valeurs conformes et procédure de Benjamini-Hochberg. En version séquentielle : Foster et Stine (2008), « α-investing: a procedure for sequential control of expected false discoveries » (RAPPORTÉ, certitude élevée sur l'attribution).
- **Garantit :** un taux de fausses découvertes ≤ q, sous échangeabilité et conditions de dépendance.
- **Ne garantit pas :** le transport vers la queue (D3).

Aucune intervention sur le générateur ne garantit quoi que ce soit sur les fausses découvertes. Seul ce garde-fou le fait.

### I1 — Allocation pilotée par f₁/N, avec exclusion des classes déjà vues

- **Garantit :** sous tirages indépendants au sein d'une source, f₁/N estime la probabilité de nouveauté du prochain tirage. On cesse d'alimenter les sources saturées.
- **Ne garantit pas :** que les classes nouvelles soient vraies. L'exclusion par invite change la distribution, et l'indépendance est perdue.
- **Indice pour :** Good (1953), certitude élevée.
- **Indice contre :** Si, Yang et Hashimoto (2024), « Can LLMs generate novel research ideas? A large-scale human study with 100+ NLP researchers », rapportent que les doublons croissent avec le volume généré (RAPPORTÉ ; certitude moyenne-élevée ; chiffre non cité). Leur dédoublonnage repose, de mémoire, sur une similarité de plongements, donc sur un modèle : l'indice est indirect.
- **Duel propre :** liste d'exclusion réelle contre liste placebo, faite d'idées tirées au hasard hors archive.
- **Abandon :** le rendement ne dépasse pas celui du placebo, ou H_B en D2.

### I2 — Hétérogénéité de modèles plutôt que davantage de tirages d'un seul

- **Garantit :** rien a priori.
- **Ne garantit pas :** que l'union des supports dépasse le support du meilleur modèle.
- **Indice pour :** argument d'ensemble ; je n'ai pas de source mesurant cela sur des idées (référence à vérifier).
- **Indice contre :** Kleinberg et Raghavan (2021), « Algorithmic monoculture and social welfare » (RAPPORTÉ, certitude élevée sur l'attribution). L'argument est théorique et porte sur la décision, non sur l'idéation.
- **Duel propre.** H_A : le recouvrement des classes entre modèles est inférieur au recouvrement en moitiés d'un même modèle. H_B : les deux sont égaux, les modèles sont le même puits.
- **Vérification mécanique à battre :** un seul modèle avec température ou invites variées, à coût égal.
- **Abandon :** recouvrement inter-modèles ≈ recouvrement intra-modèle, ou rendement ≤ celui de la variation de température.

### I3 — Isolement avant contrôle : ni débat, ni vote, ni consensus comme filtre

- **Garantit :** un filtre majoritaire supprime par construction ce qui est rare. Le vote de cohérence retient le mode : Wang et al. (2023), « Self-consistency improves chain of thought reasoning in language models » (RAPPORTÉ, certitude élevée). L'isolement retire ce filtre.
- **Ne garantit pas :** la précision des propositions. Si la part de vraies baisse, le garde-fou perd en puissance à q fixé.
- **Indice contre :** Du, Li, Torralba, Tenenbaum et Mordatch (2023), « Improving factuality and reasoning in language models through multiagent debate », rapportent un gain de justesse par débat (RAPPORTÉ, certitude moyenne sur l'ampleur). Les contestations ultérieures sont une référence à vérifier.
- **Duel propre.** H_A : le bras avec débat produit moins de classes distinctes et un rendement moindre. H_B : le gain de précision compense, et son rendement est supérieur ou égal.
- **Abandon :** H_B.

### I4 — Recherche évolutive avec contrôle dans la boucle et archive par signature

- **Garantit :** rien sur les fausses découvertes si le même contrôle sert à sélectionner et à confirmer.
- **Ne garantit pas :** la généralisation hors des cas de recherche.
- **Indices pour :** Romera-Paredes et al. (2024), « Mathematical discoveries from program search with large language models » (RAPPORTÉ ; certitude élevée sur l'existence et le schéma générateur + évaluateur, moyenne sur les détails) ; Lehman et Stanley (2011), « Abandoning objectives: Evolution through the search for novelty alone » (certitude élevée).
- **Indice contre :** Dwork, Feldman, Hardt, Pitassi, Reingold et Roth (2015), « The reusable holdout: Preserving validity in adaptive data analysis ». La réutilisation adaptative d'un jeu de validation en dégrade la validité (certitude élevée).
- **Duel propre.** H_A : l'écart entre confirmation sur cas de recherche et sur cas frais ne croît pas avec les itérations. H_B : il croît.
- **Contrôle négatif :** la même boucle avec un contrôle aux étiquettes permutées. Toute « découverte » y est du surajustement et donne le plancher.
- **Abandon :** pente de l'écart positive au-delà de δ, ou rendement sur cas frais ≤ base.

## (c) Instruments : mesure minimale de fonctionnement

La question ne nomme expressément qu'un instrument, le contrôle, et son étalon, les cas à vérité connue. Les deux autres sont ceux que la question 1 oblige à construire ; ils sont de mon fait.

| Instrument | Détection | Fausse alerte | Cas honnêtes appariés | Vérifications mécaniques à battre |
|---|---|---|---|---|
| **Contrôle T** (nommé) | Part d'idées vraies selon l'oracle qui sont confirmées, par strate de rareté. | Part d'idées fausses confirmées, par strate. | Chaque idée vraie reçoit une jumelle fausse par mutation minimale d'un élément, et inversement. Moitié des paires issues des modèles, moitié d'un générateur mécanique. | « Toujours confirmer ». Confirmer si fréquent (vote des modèles). Heuristique de surface : longueur, recouvrement lexical avec les vraies connues. |
| **Cas à vérité connue** (nommés) | Capacité à repérer un cas contaminé : canaris plantés, retrouvés ou non par recouvrement de n-grammes. | Cas frais déclarés contaminés à tort. | Cas publics contre cas synthétiques de même forme, générés après gel. | Recherche de chaîne exacte normalisée. |
| **Canoniseur κ** (le mien) | Part de paires « même idée » fusionnées. Réécritures mécaniques qui préservent le sens : renommage, réordonnancement commutatif, changement d'unités. | Part de paires « idées distinctes » fusionnées. Jumelles dont le comportement diffère sur au moins un cas-sonde. | Ces deux familles de paires, de même longueur et même gabarit. | Hachage du texte normalisé. Seuil de Jaccard sur les lexèmes. |
| **Estimateur de retour f₁/N** (le mien) | Couverture des intervalles sur générateur synthétique connu. | Erreur de prédiction en moitiés sur données réelles. | Mêmes tirages, ordre permuté. | « Zéro classe nouvelle ». Extrapolation linéaire de la courbe de découverte. |

Règles de lecture :
- **Indépendance du contrôle.** Si T ne bat pas « confirmer si fréquent », il n'apporte rien d'indépendant des modèles et P2 est réfuté en pratique. Test complémentaire : l'erreur de T sur paires issues des modèles contre son erreur sur paires mécaniques. Un écart signe une dépendance.
- **Canoniseur.** Si κ ne bat pas Jaccard sur les paires appariées, on prend Jaccard, moins cher.
- **Cas d'essai.** Si le taux de proposition spontanée des cas publics dépasse nettement celui des cas synthétiques appariés, l'étalon est contaminé. La calibration doit alors se faire sur les cas synthétiques.

Je n'avance aucun taux attendu : aucun n'est sourcé.

## Question 4 — limites de principe

- **L1. Résolution.** Avec N tirages, on ne distingue pas les masses sous l'ordre de 1/N. L'extrapolation du nombre de classes non vues n'est fiable que sur un horizon au plus logarithmique en N, selon Orlitsky, Suresh et Wu (2016), « Optimal prediction of the number of unseen species » (RAPPORTÉ ; certitude élevée sur l'attribution, moyenne sur l'énoncé exact).
- **L2. Taux de base.** À contrôle fixé, la part de fausses parmi les confirmées dépend de la part de vraies parmi les proposées : Ioannidis (2005), « Why most published research findings are false » (certitude élevée). Aller vers la queue change ce taux. D2 le mesure et ne l'abolit pas.
- **L3. Transport.** La fiabilité du contrôle hors de tout voisinage à vérité connue n'est pas certifiable depuis les cas connus. Elle est seulement bornable par oracle sur échantillon, là où un oracle existe. Sur un domaine réel sans oracle, D3 n'est pas exécutable et P3 reste une HYPOTHÈSE.
- **L4. Support.** Le rééchantillonnage n'atteint que ce qui a une probabilité non nulle sous le système. Sans structure adaptée au domaine, aucune stratégie de recherche ne domine en moyenne : Wolpert et Macready (1997), « No free lunch theorems for optimization » (certitude élevée).
- **L5. Adaptativité.** Chaque usage du contrôle pour sélectionner consomme de la validité (Dwork et al., 2015). Le stock de cas frais borne le nombre de tours.
- **L6. Granularité.** Tout décompte d'idées est conditionnel à κ. La formalisation (P11) peut réintroduire un modèle.
- **L7. Valeur.** Le contrôle établit une validité sur son critère, pas une importance. Optimiser contre lui expose à l'effet Goodhart (référence à vérifier pour une formulation citable).

## (d) Ancrage matériel

Tout ce qui est chiffré ici est un dimensionnement illustratif, non sourcé. L'arbitre peut le rayer au titre de l'interdit de la question.

**Banc à vérité totale (proposition).** Les idées sont des inégalités entre invariants de graphes, écrites dans une grammaire fermée, donc exécutables.
- **Contrôle bon marché :** test sur un échantillon aléatoire de petits graphes.
- **Oracle coûteux :** énumération exhaustive jusqu'à un ordre supérieur. Outil : McKay et Piperno (2014), « Practical graph isomorphism, II » (certitude élevée sur l'attribution).
- **Signature :** vecteur de verdicts sur une batterie fixe de graphes.
- **Limite assumée :** la « vérité » est opérationnelle (vraie jusqu'à l'ordre énuméré), pas un théorème. Le banc teste les instruments, pas l'originalité (P5).

**Modèles.** Trois ou quatre familles à poids ouverts de lignées distinctes, par exemple Llama, Mistral, Qwen, Gemma. Versions à figer par empreinte des poids. Tailles de l'ordre de 7 à 9 milliards de paramètres, quantifiés (illustratif). Je n'avance aucune performance.

**Calcul (illustratif).**
- Un processeur graphique de 24 Go.
- De l'ordre de 10⁴ tirages courts par source pour D1 à D3.
- Quatre bras, avec une dizaine de réplications par bras pour D4.
- Contrôle et oracle sur processeurs classiques.
- Ordre de grandeur : quelques dizaines à quelques centaines d'heures de processeur graphique, soit quelques centaines d'euros en location.

**Ordre d'exécution.**
1. Instruments (c).
2. D1.
3. D2 et D3.
4. D4.

Si (c) échoue pour T ou pour κ, rien en aval n'est interprétable et on s'arrête. D2 est le point d'arrêt le moins cher : si H_B y est retenue, les quatre interventions tombent ensemble.

**Ce que ce plan ne dira pas.** Il ne dira pas si les résultats du banc se transportent à un domaine scientifique réel sans oracle. Ce point reste une HYPOTHÈSE, et aucune des expériences ci-dessus ne la teste.

FIN-DE-CELLULE