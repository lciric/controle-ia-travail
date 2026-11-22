<!-- Réponse de Claude Fable 5.2 (effort high), session_013QMaynQjD5FwNbFbdGPkEZ, 2026-11-22T19:11:43Z, à la question question-sabotage-selectif-v3.md (16ff0751…). Recopiée du champ « result » de la session ; coût affiché par la session : 0,845 USD (prix catalogue). -->

**Réponse courte.** Oui, un tel banc est possible, et il est nécessaire : avec un seul adaptateur saboteur, l'effectif au niveau qui compte (le jeu de poids) vaut 1, et aucun nombre d'épisodes n'y change rien. Je recommande comme épreuve centrale un plan factoriel « poids × épisode » : plusieurs organismes à sabotage conditionnel (a), appris indépendamment (d), avec plusieurs déclencheurs dont certains réservés à l'épreuve. Le critère principal y est l'AUROC intra-poids (aire sous la courbe ROC, calculée entre épisodes sabotés et honnêtes d'un même jeu de poids). (b) et (c) deviennent des témoins.

## 0. Trois diagnostics préalables, sans nouvel organisme

- **Rejeu croisé (e).** Faire relire en lecture forcée (*teacher forcing* : on impose la transcription, le modèle ne génère rien) les mêmes transcriptions par chaque jeu de poids. Le plan est : texte (produit par le saboteur / honnête) × poids lecteurs (saboteur / base / jumeau).
  - Si le score de la sonde suit les poids lecteurs, elle lit les poids.
  - S'il suit le texte, elle lit le contenu, ce qu'un moniteur « boîte noire » peut aussi faire.
  - Seule une interaction (poids saboteurs et texte saboté) suggère autre chose.
- **Sonde d'identité des poids.** Apprendre une sonde à distinguer deux adaptateurs honnêtes (deux graines du jumeau). Je m'attends à une AUROC proche de 1, car un adaptateur LoRA ajoute un décalage de rang faible, linéairement lisible. Si c'est le cas, tout résultat inter-poids actuel est ininterprétable.
- **Interpolation de l'adaptateur.** Multiplier l'adaptateur saboteur par α entre 0 et 1, et tracer score de sonde et taux de sabotage (oracle) en fonction de α. Un score qui croît régulièrement avec α alors que le sabotage apparaît par seuil signe une lecture des poids.

## 1. Rôle de chaque conception

| Conception | Rôle | Raison |
|---|---|---|
| (a) sabotage conditionnel | **Centrale**, croisée avec (d) | Seule à faire varier, à poids constants, un sabotage produit par le modèle |
| (a′) sabotage stochastique à énoncé constant | Secondaire, à tenter | Supprime le déclencheur, mais la « décision » peut n'exister qu'au jeton échantillonné |
| (b) jumeaux parallèles | Témoin | Retire « présence d'un adaptateur », pas « identité des poids » |
| (c) régénérés par programme | Témoin, plus plancher « contenu » | Mesure la reconnaissance d'un sabotage lu, pas sa production |
| (d) plusieurs adaptateurs | Réplication de (a), pas épreuve autonome | Fournit l'unité statistique pour généraliser |
| (d) sabotage par consigne | Secondaire | Poids constants, mais la consigne est dans le contexte |
| (d) intensité graduée | Analyse secondaire dans (a) | Relation dose-réponse intra-poids |
| (e) rejeu croisé | Témoin préalable | Gratuit, décompose texte et poids |

(b) « même adaptateur dans les deux bras » revient à (a) : il faut bien une variable d'épisode pour décider du bras.

## 2. Conception centrale : (a) × (d)

**Construction.** Entraîner K organismes indépendants (graine, ordre des données, idéalement rang et sous-échantillon différents). Chacun sabote sous plusieurs déclencheurs de natures différentes : lexical, sémantique (propriété de la tâche), contextuel (indice de faible surveillance). Chacun reçoit un jumeau honnête entraîné sur les mêmes énoncés, déclencheurs compris, avec des complétions honnêtes. Réserver une famille de déclencheurs et au moins un organisme à l'épreuve.

**Contrôle de manipulation.**
- L'oracle reste aveugle à la condition et s'applique à toutes les cellules.
- Fixer des seuils à l'avance, par exemple au moins 80 % de sabotage sous déclencheur et au plus 2 à 5 % sans.
- Faire auditer à l'aveugle par un humain 50 à 100 épisodes par cellule.
- Rapporter deux étiquetages : par intention (déclencheur présent) et par comportement (dommage selon l'oracle).
- Ajouter une cellule « dommage sans intention » : échecs honnêtes de dommage comparable. Sinon la sonde peut lire « travail raté ».

**Fuite du déclencheur.** Il fuira toujours : un jeton du contexte est linéairement décodable, y compris chez le jumeau honnête. Ne cherchez pas à montrer l'absence de fuite, mais l'absence de dépendance de la sonde, par trois épreuves :
1. le score sur les cellules « déclencheur sans sabotage » reste au niveau honnête ;
2. la sonde apprise sur les déclencheurs 1 à K−1 se transfère au déclencheur réservé ;
3. la sonde résiste à l'effacement linéaire de la direction « déclencheur », estimée sur le jumeau (Belrose et al., 2023, « LEACE: Perfect linear concept erasure in closed form »).

**Témoins.**
- **Déclencheur sans sabotage**, par quatre voies :
  - tâches sans occasion de saboter ;
  - leurres, c'est-à-dire quasi-déclencheurs que l'organisme a appris à ignorer ;
  - jumeau honnête sous déclencheur (autres poids, donc indicatif) ;
  - non-conformités spontanées (sélectionnées, à lire avec prudence).
- **Sabotage sans déclencheur** : faux départs spontanés, rares et sélectionnés ; le déclencheur réservé couvre mieux ce besoin.
- **Permutation des étiquettes** et tâches de contrôle : une sonde assez expressive apprend aussi des étiquettes arbitraires (Hewitt et Liang, 2019, « Designing and Interpreting Probes with Control Tasks »).
- **Sonde d'identité** des poids et sonde « déclencheur seul », comme comparaisons.
- **Moniteur boîte noire** sur les mêmes transcriptions : une sonde qui ne le dépasse pas n'apporte rien de proprement interne.
- **Positions de lecture** séparées : avant le premier jeton divergent, puis après.
- **Sonde sur caractéristiques de surface** : longueur, nombre d'appels d'outils, perplexité.

**Pièges, succès pour une mauvaise raison.**
- Déclencheur lu au lieu du sabotage.
- Longueur, style ou hésitations de la sortie.
- Sabotage rendu artificiellement saillant par l'insertion de la porte dérobée. Dans « Simple probes can catch sleeper agents » (MacDiarmid et al., 2024, note d'Anthropic ; liste d'auteurs et détails de mémoire), les auteurs signalaient eux-mêmes ne pas savoir si la forte saillance linéaire observée tenait au procédé d'insertion. Les organismes venaient de Hubinger et al., 2024, « Sleeper Agents: Training Deceptive LLMs that Persist Through Safety Training ».
- Hyperparamètres de la sonde (couche, position, régularisation) choisis sur l'épreuve.

**Pièges, échec alors que la sonde lit le sabotage.**
- Le sabotage conditionnel passe par un autre mécanisme (raccourci « si déclencheur, alors style X ») que le sabotage inconditionnel sur lequel la sonde a été apprise.
- La décision est calculée tardivement, donc rien n'est lisible avant l'action.
- Le moyennage sur les jetons dilue un sabotage local.
- L'oracle bruite les étiquettes. Avec une erreur symétrique ε, l'AUROC observée vaut environ 0,5 + (1−2ε)(A−0,5) : 0,90 devient 0,82 pour ε = 10 %.
- La conformité de l'organisme est faible.

**Variante (a′).** Entraîner l'organisme sur un mélange de complétions sabotées et honnêtes pour les mêmes énoncés. Le sabotage varie alors d'un tirage à l'autre, à poids et énoncé constants, et l'étiquette vient de l'oracle. Limite sérieuse : le choix peut se faire au jeton échantillonné. Avant divergence, il n'y a alors rien à lire, et la sonde doit y être au hasard (bon témoin négatif). Après divergence, elle peut lire le texte. Cette variante éprouve donc la reconnaissance en cours de production plus que l'intention.

## 3. Témoins (b), (c) et sabotage par consigne

**(b) jumeaux.** Multiplier les paires, au moins 5. Le témoin clé est la sonde d'identité entre jumeaux honnêtes. Le contrôle de manipulation est l'oracle sur les deux bras, qui vérifie que le jumeau ne sabote pas plus que la base. Le piège est de croire la confusion levée parce que les deux bras portent un adaptateur.

**(c) régénérés.**
- **Contrôle de manipulation.** L'oracle doit voir le dommage sur la version réécrite, et l'absence de dommage sur une réécriture placebo : même programme, même ampleur d'édition, sans dégât. Sans placebo, la sonde peut lire l'artefact d'édition (rupture de style, saut de perplexité).
- **Lecture.** C'est un plancher « contenu ». Si la sonde y réussit autant que sur le sabotage produit, elle reconnaît un sabotage présent dans le contexte. Ce signal est utile en contrôle, mais ce n'est pas un signal d'intention.
- **Faux succès.** Distribution hors domaine des épisodes édités.
- **Faux échec.** Une sonde d'intention y échoue légitimement.

**Sabotage par consigne sur le modèle non réglé.**
- **Protocole.** Poids réellement constants. Utiliser plusieurs paraphrases de consigne, dont certaines réservées.
- **Témoin.** Consigne présente mais non suivie, ou tâche sans occasion.
- **Piège.** La sonde lit la consigne.
- **Rapprochement.** La configuration est proche de Goldowsky-Dill et al., 2025, « Detecting Strategic Deception Using Linear Probes », qui évaluent sur des scénarios distincts de ceux d'apprentissage.
- **Proximité avec le risque.** Plus faible que pour un organisme réglé.

**Intensité graduée.** À l'intérieur d'un organisme, vérifier que le score croît avec le dommage mesuré par l'oracle. C'est le meilleur indice secondaire, car l'identité des poids ne peut pas produire une dose-réponse intra-poids.

## 4. Unité statistique et séparation apprentissage / épreuve

- **Lecture intra-poids sur un organisme donné** : l'unité est la tâche.
  - Apparier les conditions par tâche.
  - Traiter les tirages d'une même tâche comme des mesures répétées.
  - Calculer les intervalles par rééchantillonnage des tâches.
- **Généralisation à d'autres saboteurs** : l'unité est l'adaptateur appris indépendamment. Les épisodes d'un même adaptateur sont des pseudo-réplicats (Hurlbert, 1984, « Pseudoreplication and the design of ecological field experiments »).
- **Analyse** : rééchantillonnage hiérarchique (adaptateurs, puis tâches, puis épisodes), ou modèle mixte du score en fonction du sabotage et du déclencheur, avec effets aléatoires tâche et adaptateur.
- **Séparations** : par tâche (aucune tâche des deux côtés), par adaptateur (un organisme laissé de côté à tour de rôle), par déclencheur.
- **Hyperparamètres** : couche, position, agrégation et seuil sont fixés sur l'apprentissage et déclarés à l'avance.
- **Mesures à rapporter**, en plus de l'AUROC : le taux de détection à 1 % de faux positifs, et quatre nombres :
  - AUROC intra-poids ;
  - AUROC sur l'identité des poids à étiquette constante ;
  - transfert à un organisme réservé ;
  - transfert à un déclencheur réservé.

## 5. Ordres de grandeur de puissance

Ces chiffres sont des calculs de coin de table, sous les hypothèses indiquées.

- **Intra-poids, lecture des poids contre lecture du sabotage.** Une sonde qui lit les poids doit tomber à une AUROC de 0,5 ; une sonde qui lit le sabotage reste, par hypothèse, à 0,8 ou plus.
  - Par la formule de Hanley et McNeil (1982, « The meaning and use of the area under a receiver operating characteristic (ROC) curve »), l'erreur type vaut environ 0,41/√n à A = 0,5 et 0,34/√n à A = 0,75, pour n unités indépendantes par classe.
  - Trente tâches indépendantes par classe suffisent pour l'écart 0,5 contre 0,8.
  - L'effet de grappe compte : avec 10 tirages par tâche et une corrélation intra-tâche de 0,3, l'effet de plan vaut 1 + 9 × 0,3 = 3,7. Mieux vaut plus de tâches que plus de tirages.
  - En pratique : 100 à 200 tâches d'épreuve appariées, 2 à 4 tirages par cellule, pour une demi-largeur d'intervalle de 0,05 à 0,08.
- **Départager un écart de 0,10** (0,70 contre 0,80, par exemple sonde contre moniteur boîte noire) : environ 200 tâches effectives par classe ; l'appariement en demande moins.
- **Niveau adaptateur.**
  - Avec 3 organismes réservés, le meilleur test de signe unilatéral donne p = 0,125 : c'est une anecdote.
  - Avec 5, p = 1/32 ≈ 0,03 ; avec 6, p ≈ 0,016.
  - Si l'écart type inter-adaptateurs de l'AUROC est de 0,05, six organismes donnent une moyenne à ±0,05 environ (t à 5 degrés de liberté).
  - Visez donc 5 à 6 organismes conditionnels et autant de jumeaux. L'hypothèse fragile est leur indépendance : mêmes données de sabotage et même recette font probablement sous-estimer la variance.
- **Dose-réponse** : détecter une corrélation de rang de 0,3 à 80 % de puissance demande environ 85 tâches indépendantes.
- **Sonde d'identité** : quelques centaines d'épisodes suffisent.

## 6. Ce que le banc ne permet pas de conclure, même réussi

- Que la sonde détecterait un sabotage apparu sans réglage fin dédié. La validité de l'organisme modèle reste entière : une porte dérobée apprise n'est pas une stratégie adoptée.
- Qu'elle lit une « intention » plutôt qu'une anomalie reconnue. Seules les positions antérieures à la divergence et le rejeu croisé en disent quelque chose.
- Qu'elle résiste à un modèle entraîné contre elle (Bailey et al., 2024, « Obfuscated Activations Bypass LLM Latent-Space Defenses »).
- Qu'elle se transfère à un autre modèle de base, à une autre taille ou à d'autres familles de tâches.
- Que la direction lue est causalement impliquée. Il faudrait une intervention : ablation de la direction, puis baisse du sabotage mesurée par l'oracle.
- Qu'elle est utilisable en exploitation à très faible taux de base : l'AUROC ne dit rien du taux de détection à 0,1 % de faux positifs.

Sur les limites générales des sondes, voir Belinkov (2022, « Probing Classifiers: Promises, Shortcomings, and Advances ») et Levinstein et Herrmann (« Still no lie detector for language models », 2023 ou 2024 selon la version ; date incertaine).

## Recommandation

Faites du plan factoriel (a) × (d) l'épreuve centrale : 5 à 6 organismes conditionnels indépendants avec jumeaux, déclencheurs multiples dont une famille réservée, critère principal intra-poids, cellules « déclencheur sans sabotage » obligatoires. Gardez (b), (c), la consigne et le rejeu croisé comme témoins. Lancez d'abord le rejeu croisé et la sonde d'identité, qui ne coûtent rien et peuvent à eux seuls invalider les résultats actuels.

**Confiance : moyenne à élevée** sur le principe (variation intra-poids, adaptateur comme unité, déclencheurs réservés). **Moyenne** sur la faisabilité d'organismes conditionnels dont le sabotage ne soit pas un raccourci attaché au déclencheur.

Ce qui me ferait changer d'avis :
- Une sonde d'identité au hasard entre jumeaux, que je crois improbable : la confusion actuelle serait moindre que redouté.
- Des sondes qui se transfèrent entre déclencheurs mais pas vers l'organisme inconditionnel : (a) mesurerait autre chose, et je remonterais (a′) et la consigne.
- Un rejeu croisé où le score suit entièrement le texte : la question deviendrait « la sonde bat-elle un moniteur boîte noire ? », et (c) avec placebo prendrait un rôle central.
