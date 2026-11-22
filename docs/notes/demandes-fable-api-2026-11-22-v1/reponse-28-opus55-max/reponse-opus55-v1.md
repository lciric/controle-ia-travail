# Demande 28 — faire trouver à l'organisme d'idéation les puits étroits et profonds — second regard indépendant (Opus 5.5)

## En-tête

- **Pièce de travail** (classe C). Écrite le 22 novembre 2026 vers 12:30Z (`date -u` relevé à 12:17:35Z avant l'écriture) par Claude Opus 5.5 (`claude-opus-5-5`), sous-agent lancé par la session mère, en effort maximal, à la demande du directeur (« lance Opus aussi sur les revendications et idées originales »). Second regard indépendant, en parallèle de Fable : je n'ai lu aucune réponse de Fable aux demandes 28 et 34. Cette pièce ne décide rien et ne déclare rien libre.
- **Dépôt lu** : branche `claude/blissful-ritchie-svldqy`, commit `7edaacce`.
- **Pièces lues.** Empreintes compagnons vérifiées « OK » par `controle_ia.scellement verifier` (seize premiers signes). L'alias sert dans les étiquettes.

| alias | chemin | empreinte |
|---|---|---|
| demande 28 | `docs/notes/demandes-fable-api-2026-11-22-v1/demande-28-idees-originales-puits-profonds-v1.md` | f552f514961f78be |
| recoupement | `docs/notes/organisme-bassins-etroits-v1/recoupement-methodes-v1.md` | eecd98fab0beff8c |
| table v1 | `docs/notes/demandes-fable-api-2026-11-22-v1/copies-sans-nom-v1/table-revendications-en-vigueur-v1-sans-nom-v1.md` | 02453d1d92fc5891 |
| 22P | `docs/notes/demandes-fable-api-2026-11-22-v1/reponse-22P/relecture-fable-api.md` | cb010f4cbd12b5fb |
| 27 | `docs/notes/demandes-fable-api-2026-11-22-v1/reponse-27-luc/relecture-fable-api.md` | 6a042a7b18124d58 |
| 29 | `docs/notes/demandes-fable-api-2026-11-22-v1/reponse-29/relecture-fable-api.md` | 2af768bc095e40a4 |
| CLAUDE.md | `CLAUDE.md` (fichier vivant, sans compagnon ; SHA-256 relevé) | 282542c96e0533c9 |

- **Non lu.** Les réponses de Fable aux demandes 28 et 34 ; les réponses 22A, 22B et 22C (connues seulement par ce qu'en rapporte 22P) ; aucun PDF ; aucun résultat de course ; aucun fichier interdit par le mandat. Je n'ai lancé aucun calcul ni aucun appel à un modèle.
- **Étiquettes.** [FAIT LU — alias, lieu] : lu dans la pièce citée. [RAPPORTÉ DE MÉMOIRE] : cité de mémoire, non vérifié sur PDF ; titres et années peuvent être inexacts ; la certitude est dite (élevée, moyenne, faible). [HYPOTHÈSE] : jugement, prévision ou dérivation de ma main, non vérifiée par un tiers. Une étiquette en tête d'un paragraphe, d'une liste ou d'un tableau couvre toutes ses lignes, sauf étiquette contraire. [PROPOSITION] marque un plan, une recommandation ou une option : ce n'est pas une affirmation, et les affirmations qu'elle contient portent leur propre étiquette.
- **Chiffres.** Aucun chiffre de l'état de l'art n'est donné. Les seuls nombres sont des seuils à sceller ou des bornes élémentaires, dits comme tels.

## Conclusion d'abord

[HYPOTHÈSE]
- « Puits étroit et profond » se mesure sans juge de nouveauté, par **deux références distinctes**. La **rareté** se lit sous la loi des propositions d'une population de proposeurs nommée : fréquence d'une classe d'idées à conséquences exécutables identiques. La **profondeur** se lit contre ce que l'archive prédit déjà : juge statistique et oracle des mondes plantés. Confondre les deux références fabrique de la fausse originalité.
- Rien en aval des proposeurs n'augmente la chance qu'une idée soit proposée [FAIT LU — recoupement, § 1 et § 8, borne 1]. La première mesure, gratuite, est de savoir **où l'entonnoir perd** dans les courses passées : idée jamais proposée, ou proposée puis perdue [FAIT LU — recoupement, § 9 : la question est ouverte].
- Le levier qu'un expert ajouterait : **nourrir les proposeurs de ce que les autres modèles n'ont pas vu**, c'est-à-dire des données brutes propres au programme. Les modèles de pointe tendent à converger vers les mêmes idées ; la rareté qui compte pour un papier est la rareté sous les modèles des concurrents.
- Il n'y a pas de méthode optimale dans l'absolu. L'optimum n'existe que relativement à une loi a priori, déclarée, sur les formes de puits [FAIT LU — recoupement, § 8, borne 2].
- Certifier qu'un puits est étroit coûte à peu près autant que le trouver par force brute : l'étroitesse doit donc venir de la construction du banc, pas d'une estimation.
- Confiance d'ensemble : 0,6.

## 1. Ce qu'un expert du domaine ferait ici, et qui n'est pas demandé

[PROPOSITION, sauf étiquette contraire]
1. **Diagnostiquer l'entonnoir avant toute méthode.** Pour chaque composante plantée des courses passées : a-t-elle été proposée par un proposeur, même une fois ; gardée par le gardien ; gardée au regroupement des doublons ; promue par le juge ? Ce calcul se fait par programme, sur processeur, sans qu'aucun modèle lise les mondes plantés. Il décide si l'on agit en amont (vue, proposeurs) ou en aval (regroupement, juge).
2. **Mesurer la rareté sous trois populations, pas une.** (a) Les proposeurs de l'organisme. (b) Les autres familles de modèles de pointe, c'est-à-dire ce que les assistants des concurrents proposeraient. (c) La littérature humaine. [HYPOTHÈSE] Une idée rare sous (a) et commune sous (b) est un risque d'être devancé ; rare sous (b) mais publiée en (c), c'est une collision.
3. **Ancrer une part de l'idéation dans des données que les modèles n'ont pas vues.** Journaux bruts des courses du programme, anomalies, échecs de gardes, statistiques des épisodes honnêtes, servis sous les règles de cloisonnement (seulement des pièces scellées et lues). [HYPOTHÈSE] C'est la seule source systématique de rareté sous (b), puisque les modèles de pointe partagent une grande part de leurs données d'entraînement.
4. **Rendre les idées exécutables avant de compter leur originalité.** Chaque idée porte une prédiction scellée ou un test exécutable ; alors l'équivalence et la valeur deviennent calculables. L'organisme le fait déjà pour les cartes [FAIT LU — recoupement, « Vocabulaire » : cartes = lois prédictives dans une grammaire publique] [FAIT LU — table v1, § 1.4, juge au nul formé des lois connues : une fiche n'est promue que si sa prédiction scellée bat ce que l'archive prédit déjà]. Pour les idées en texte libre (questions, mécanismes de contrôle, modes d'attaque), exiger une traduction en test sur le banc du programme avant tout compte.
5. **Définir la valeur par type d'idée.** Une question vaut par la valeur de l'information qu'elle apporte à une décision nommée du programme [RAPPORTÉ DE MÉMOIRE, certitude élevée : Howard, 1966, « Information Value Theory »]. Un mécanisme de contrôle vaut s'il attrape, à fausses alertes égales, des dommages plantés que les bases manquent. Un mode d'attaque ne s'éprouve qu'en quarantaine, sur le banc ; aucun mode opératoire n'est décrit ici.
6. **Planter des puits impossibles comme détecteurs de fuite.** Un puits sans palier (interaction sans marge d'ordre inférieur, sans parent archivé), placé au hasard après le gel de la vue, ne peut pas être trouvé plus vite qu'une énumération aveugle [FAIT LU — recoupement, § 8, bornes 2 et 3]. Une méthode qui le trouve plus vite a une fuite : c'est la règle R4 (trop beau = réserve).
7. **Faire varier la question, pas seulement les réponses.** Beaucoup de puits ne s'atteignent qu'en reformulant le problème. Le recoupement note que la question posée désignait la composante conditionnelle et que les suggestions s'en ressentent [FAIT LU — recoupement, § 11].
8. **Écrire le seuil de rentabilité d'une méthode avant de l'essayer** : le gain de probabilité par appel doit dépasser le surcoût par appel (dérivation en R3).

## 2. Les données brutes qu'il prendrait au départ

[PROPOSITION]
- Les **propositions brutes** de toutes les courses passées de l'organisme, et non les seules cartes retenues : texte, proposeur, vue servie, graine, jetons facturés, et le journal de l'entonnoir (refus du gardien, groupes de doublons, verdicts du juge).
- Un **échantillon de référence** large par proposeur, sous une vue neutre, sur des mondes d'étalonnage : la carte des bassins. Un second échantillon, indépendant (autres graines, autre famille), pour mesurer sans circularité.
- L'**archive** à chaque génération, et le registre des tentatives [FAIT LU — table v1, § 1.4, énoncé 5 : la mémoire est un registre des tentatives, non une archive de découvertes].
- Les **probabilités par jeton** de tout proposeur à poids ouverts : elles bornent la probabilité d'un texte de carte sous ce modèle.
- Des **corpus datés** de la littérature du contrôle de l'intelligence artificielle, pour des épreuves à coupure temporelle.
- L'**historique des revendications du programme trouvées occupées** : un jeu étiqueté de fausse originalité produite par l'idéation du programme lui-même. [FAIT LU — liste du dossier : un fichier `constats-collisionneur-retroanalyse-v1.md` existe dans le dossier de la demande ; je ne l'ai pas lu.]
- Les données brutes propres au programme que le cloisonnement permet de servir.

## 3. Les méthodes et outils qu'il emploierait

[PROPOSITION ; détail et limites en R3]
- Classes d'équivalence fonctionnelle (prédictions sur le jeu public, formes canoniques).
- Estimateurs d'espèces de l'écologie : masse manquante de Good et Turing, richesse de Chao, raréfaction et extrapolation par couverture, capture et recapture entre familles de proposeurs.
- Valeurs e et processus e contre le nul de l'archive, sur tirages frais.
- Plan apparié par monde ; analyse de survie du temps jusqu'à la découverte.
- Vérificateurs formels et solveurs exacts comme tests de mort, là où l'idée se formalise.
- Bornes inférieures (énumération aveugle, requêtes statistiques) comme détecteurs de fuite.

## 4. Ce qui, hors du directeur et de Claude, vérifierait le résultat

[PROPOSITION, sauf étiquette contraire]
- L'**oracle des mondes plantés** : un programme, pas un avis [FAIT LU — recoupement, « Vocabulaire » : juge calculé hors de tout agent].
- Un **concepteur de puits tiers**, d'une autre lignée ou humain, qui plante des formes inconnues des concepteurs de méthodes, dont une famille tenue à l'écart lue une seule fois [FAIT LU — CLAUDE.md : N-044, universalité sur familles inédites ; N-050, lot final lu une seule fois ; N-054, mode tenu à l'écart].
- Le **temps** : des épreuves à coupure temporelle (idées publiées après la coupure de tous les proposeurs) et des prédictions scellées maintenant, lues plus tard.
- Une **lecture d'antériorité sur pièce par un tiers** avant tout « neuf pour le champ » [FAIT LU — `docs/notes/demandes-fable-api-2026-11-22-v1/demande-34-note-des-revendications-v3-v1.md`, empreinte 7e0a328e6d04e184 : décision du directeur du 22 novembre].
- Le **collisionneur étalonné sur des témoins au statut connu** [FAIT LU — 22P, § 4].
- Des **experts du domaine en aveugle**, qui comparent par paires des idées sans connaître leur provenance.

## Demande reformulée

[PROPOSITION] « Définis, par des grandeurs calculables sur les sorties de l'organisme et sans juge de nouveauté, ce qu'est une idée rare et juste : la rareté sous une loi de propositions nommée, sur des classes d'idées à conséquences exécutables identiques ; la profondeur contre ce que l'archive prédit déjà, sur tirages frais et sous l'oracle des mondes plantés. Commence par dire où l'entonnoir de l'organisme perd ses idées étroites, à partir des propositions brutes des courses passées. Pour chaque famille de méthodes qui sort des modes communs, dis ce qu'elle garantit, ce qu'elle ne garantit pas, l'indice publié le plus fort pour et contre, et la contrainte du dépôt qui la limite (aucun score servi aux proposeurs). Donne les objets mathématiques et les outils, avec le lieu exact où chacun échoue, dont le coût de certifier l'étroitesse. Conçois un banc où des puits de formes connues, dont des puits impossibles et des leurres, sont plantés par un tiers ; compare l'organisme à des bases nommées à budget égal en jetons facturés, avec un critère de réfutation scellé. Dis ce qui passerait pour original sans l'être et le test qui le tue. Ordonne les expériences du moins cher au plus cher, chacune avec ce qu'elle décide et sa règle d'arrêt. Écris la question neutre. Marque chaque affirmation : lue, rapportée de mémoire ou hypothèse ; aucun chiffre sans source. »

## Réponse

### R1. Ce que « puits étroit et profond » et « bassin banal » veulent dire, de façon mesurable

**Classe d'une idée.** [FAIT LU — recoupement, « Vocabulaire » et § 8, borne 13] Deux cartes sont comparées sur un jeu public d'instances sans issue ; l'équivalence fonctionnelle n'est décidable que dans une grammaire bornée. [PROPOSITION] La classe [c] d'une idée est l'ensemble des idées qui ont les mêmes conséquences exécutables : pour une carte, les mêmes prédictions sur le jeu public, à une tolérance scellée ; pour une idée en texte libre, la même issue de son test exécutable. Sans test exécutable, pas de classe, donc pas de compte.

**Les deux références.** [HYPOTHÈSE]

| grandeur | définition | se calcule par | juge de nouveauté ? |
|---|---|---|---|
| **Étroitesse** w(c) | probabilité, par appel, qu'une population de référence nommée propose une idée de la classe c | fréquence sur un échantillon de référence S₀, disjoint de tout échantillon qui pilote l'organisme | aucun |
| **Profondeur** d(c) | ce que la classe gagne sur ce que l'archive prédit déjà | valeur e de la prédiction scellée contre le nul de l'archive, sur tirages frais ; sur monde planté, verdict de l'oracle et part de l'effet planté retrouvée | aucun |
| **Fécondité** f(c) | ce que la classe rend possible aux générations suivantes | descendants qui passent les tests de mort, par le registre des tentatives | aucun |

- [FAIT LU — table v1, § 1.4] Le juge au nul formé des lois connues mesure déjà la profondeur dans ce sens. Le principe de la fécondité par la descendance est cité, non revendiqué (énoncé 5, « Huxley-Gödel Machine » parmi les citations obligatoires).
- [HYPOTHÈSE] La rareté se lit sous **ce que les proposeurs proposent** ; la profondeur sous **ce que l'archive sait**. Ce sont deux objets. Une idée peut être rare sous les proposeurs et déjà dans l'archive (un oubli), ou commune sous les proposeurs et absente de l'archive (un acquis facile, que la génération suivante archivera).

**Quatre quadrants.** [HYPOTHÈSE]

| | profondeur faible | profondeur forte |
|---|---|---|
| **commune** | bassin banal | acquis facile : à archiver vite |
| **rare** | bizarrerie ou bruit | **puits** |

- **Puits étroit et profond** : w(c) ≤ ε et d(c) ≥ θ, vrai selon l'oracle ; ε et θ scellés d'avance, avec la population de référence nommée.
- **Bassin banal** : les classes les plus fréquentes, qui couvrent ensemble une part scellée de S₀, quelle que soit leur profondeur.
- **Grandeur de l'organisme** : le rendement en puits, R(B) = nombre de classes « puits » distinctes retenues et confirmées par l'oracle, pour un budget B en jetons facturés ; et, pour chaque puits planté, le **gain d'efficacité** λ(c) = p_org(c) / p₀(c), rapport des probabilités de proposition par appel de l'organisme et de la référence.

**Une prédiction audacieuse vérifiée.** [HYPOTHÈSE ; RAPPORTÉ DE MÉMOIRE, certitude élevée : Popper, 1959, « The Logic of Scientific Discovery » (contenu d'une hypothèse) ; Mayo, 2018, « Statistical Inference as Severe Testing »] Une idée profonde prédit ce que la référence juge improbable, et la prédiction se vérifie. Sur monde planté, l'improbabilité sous l'archive est exactement ce que mesure la valeur e : on retombe sur le juge existant. L'improbabilité sous les proposeurs, elle, est la rareté. Les deux se lisent séparément.

**Mesurer sans juge de nouveauté complaisant.** [PROPOSITION]
- Rareté : par fréquence de classes exécutables, jamais par un modèle qui note « est-ce nouveau ».
- Profondeur : par la valeur e et l'oracle.
- Distance à la littérature : par le collisionneur, étalonné sur des témoins au statut connu, ses erreurs rapportées, jamais comme score de sélection.
- « Neuf pour le champ » : seulement après lecture sur pièce par un tiers.

**Où cette définition échoue.**
- [FAIT LU — recoupement, § 1] La largeur d'un bassin dépend du modèle, de la vue et de l'archive ; elle ne s'estime que sur des mondes d'étalonnage.
- [HYPOTHÈSE] Les appels ne sont pas indépendants (même consigne, même cache, même température) : les estimateurs de fréquence sont biaisés vers la sur-confiance.
- [HYPOTHÈSE] **Résolution.** Avec N appels de référence, une classe jamais vue a une probabilité par appel dont la borne haute à 95 % vaut environ 3/N [RAPPORTÉ DE MÉMOIRE, certitude élevée : « règle de trois », borne élémentaire de la loi binomiale]. Certifier w(c) ≤ ε demande donc de l'ordre de 3/ε appels de référence, soit à peu près le coût de trouver la classe par force brute avec la référence. Conséquence : sur le banc, l'étroitesse doit être connue **par construction** (dénombrement des classes candidates à une complexité donnée, placement au hasard), et non estimée ; ailleurs, elle n'est dite que jusqu'à la résolution de S₀.
- [HYPOTHÈSE] Pour le texte libre sans test exécutable, aucune des trois grandeurs n'existe.

### R2. Les familles de méthodes connues pour sortir des modes communs

**Contrainte du dépôt, qui limite toutes les familles.** [FAIT LU — recoupement, § 1 et § 2, V12] Aucune proposition ne sert un score de nouveauté à un agent ; les méthodes qui supposent un score ou un verdict rendu au proposeur, ou un pilotage par le juge, sont écartées. [HYPOTHÈSE] Les méthodes de qualité et diversité ou de nouveauté ne peuvent donc vivre que dans l'orchestrateur (sélection, archive, allocation), jamais comme texte servi aux proposeurs.

[RAPPORTÉ DE MÉMOIRE pour toutes les sources du tableau ; certitude entre parenthèses ; aucun chiffre]

| famille | garantit | ne garantit pas | indice le plus fort pour | indice le plus fort contre |
|---|---|---|---|---|
| **Qualité et diversité** (cartes d'élites ; nouveauté seule) | une grille couverte dans un espace de descripteurs choisi d'avance ; le meilleur par case | rien hors des descripteurs ; ni la valeur (nouveauté seule) | Mouret et Clune, 2015, « Illuminating search spaces by mapping elites » (élevée) ; Lehman et Stanley, 2011, « Abandoning Objectives: Evolution Through the Search for Novelty Alone » (élevée) ; Samvelyan et collègues, 2024, « Rainbow Teaming: Open-Ended Generation of Diverse Adversarial Prompts » (élevée) | Cuccu et Gomez, 2011, « When Novelty Is Not Enough » (moyenne) : la nouveauté seule se dilue dans un grand espace ; Bradley et collègues, 2024, « Quality-Diversity through AI Feedback », et Zhang, Lehman, Stanley et Clune, 2024, « OMNI » (élevée pour l'existence) reposent sur un modèle qui juge la qualité ou l'intérêt : c'est le juge complaisant à éviter |
| **Échantillonnage contre la vraisemblance** (température, seuil relatif, décodage contrastif, échantillonnage verbalisé, modèles de base) | plus de diversité de surface par appel | la qualité ; la queue de la loi par jeton est surtout incohérente | Zhang et collègues, 2025, « Verbalized Sampling: How to Mitigate Mode Collapse and Unlock LLM Diversity » (moyenne) ; West et Potts, 2025, « Base Models Beat Aligned Models at Randomness and Creativity » (moyenne) ; Nguyen et collègues, 2025, « Turning Up the Heat: Min-p Sampling for Creative and Coherent LLM Outputs » (élevée) | Holtzman et collègues, 2020, « The Curious Case of Neural Text Degeneration » (élevée) ; Peeperkorn et collègues, 2024, « Is Temperature the Creativity Parameter of Large Language Models? » (élevée pour l'existence ; lien faible avec la nouveauté, rapporté) ; Kirk et collègues, 2024, « Understanding the Effects of RLHF on LLM Generalisation and Diversity » (élevée) : le réglage sur préférences réduit la diversité des sorties |
| **Cibles posées par un expert et vérificateur exact** | tout ce qui passe est juste au sens du vérificateur ; une recherche massive devient possible | la pertinence ; l'absence de faille du vérificateur | Romera-Paredes et collègues, 2024, « Mathematical discoveries from program search with large language models » (élevée) ; Novikov et collègues, 2025, « AlphaEvolve: A coding agent for scientific and algorithmic discovery » (élevée) ; Wagner, 2021, « Constructions in combinatorics via neural networks » (élevée) ; Trinh et collègues, 2024, « Solving olympiad geometry without human demonstrations » (élevée) | Skalse et collègues, 2022, « Defining and Characterizing Reward Hacking » (élevée) ; Krakovna et collègues, 2020, « Specification gaming: the flip side of AI ingenuity » (moyenne, billet) ; limité aux domaines où un évaluateur exact et bon marché existe |
| **Adversaire qui prédit l'idée banale et la retire** | l'éloignement de ce que l'adversaire prédit | la valeur ; pousse vers le bizarre | Sourati et Evans, 2023, « Accelerating science with human-aware artificial intelligence » (élevée) : des hypothèses qui évitent la région dense des chercheurs ; Elgammal et collègues, 2017, « CAN: Creative Adversarial Networks » (élevée) | Si, Hashimoto et Yang, 2025, « The Ideation-Execution Gap » (moyenne) : la nouveauté jugée avant exécution ne survit pas à l'exécution ; Si, Yang et Hashimoto, 2025, « Can LLMs Generate Novel Research Ideas? » (élevée) : idées jugées nouvelles, mais diversité qui sature quand on en génère beaucoup (rapporté) |
| **Recombinaison contrainte** | la couverture des affectations, non des idées [FAIT LU — recoupement, V3] | le sens des combinaisons ; un recollage par morceaux échappe au nul [FAIT LU — recoupement, § 8, borne 9] | Swanson, 1986, « Fish oil, Raynaud's syndrome, and undiscovered public knowledge » (élevée) ; Uzzi et collègues, 2013, « Atypical Combinations and Scientific Impact » (élevée ; étude d'observation) ; Shi et Evans, 2023, sur les combinaisons surprenantes et les chercheurs venus de loin (moyenne) | Wang, Veugelers et Stephan, 2017, « Bias against novelty in science » (élevée) : les combinaisons neuves ont des issues plus dispersées, succès et échecs (rapporté) |
| **Abstraction et transfert entre domaines** | rien : une analogie est une hypothèse | que la structure transférée tienne | Hope et collègues, 2017, « Accelerating Innovation Through Analogy Mining » (moyenne) ; Yasunaga et collègues, 2024, « Large Language Models as Analogical Reasoners » (élevée) | Lewis et Mitchell, 2024, sur les tâches contrefactuelles d'analogie (moyenne) : analogies de surface ; Gentner, 1983, « Structure-mapping » (élevée) : ressemblance de surface et ressemblance de relations se séparent |
| **Curriculum vers des problèmes plus durs** | une progression, là où la difficulté se mesure et s'apprend | une définition de « plus dur » pour des idées | Wang, Lehman, Clune et Stanley, 2019, « Paired Open-Ended Trailblazer » (élevée) ; Dennis et collègues, 2020, sur la conception non supervisée d'environnements (élevée) ; Zhao et collègues, 2025, « Absolute Zero » (moyenne) | l'espace des problèmes est paramétré par le concepteur ; je ne connais aucun transfert éprouvé aux idées de recherche avec validation tenue à l'écart [HYPOTHÈSE : mon ignorance, pas un trou du champ, R8] |
| **Programme de recherche à archive complète** | ne pas perdre les pierres de gué | la découverte elle-même | Ecoffet et collègues, 2021, « First return, then explore » (élevée) ; Zhang, Hu, Lu, Lange et Clune, 2025, « Darwin Gödel Machine » (élevée ; l'archive ouverte y bat la sélection gloutonne en ablation, rapporté) ; Lange et collègues, 2025, « ShinkaEvolve » (moyenne) : rejet des candidats trop proches | [FAIT LU — table v1, § 3] le dépôt cite Meta-Harness (Lee et collègues) comme indice contraire et Qin et collègues comme indice contraire à la prémisse ; coût qui croît avec l'archive |
| **Diversité des familles de proposeurs** (ajoutée) | des erreurs moins liées, si les familles diffèrent vraiment | que les idées diffèrent | intuition seulement | [FAIT LU — table v1, § 1.4, O8] le dépôt cite « Beyond Symmetric Agents » (Ferreira, Liu et Zheng) comme indice contraire ; Jiang et collègues, 2025, « Artificial Hivemind: The Open-Ended Homogeneity of Language Models (and Beyond) » (moyenne) : homogénéité entre modèles |
| **Ancrage dans des données que les modèles n'ont pas vues** (ajoutée) | une information absente des données d'entraînement communes | que l'information produise une idée | Tshitoyan et collègues, 2019, « Unsupervised word embeddings capture latent knowledge from materials science literature » (élevée) : anticipation de découvertes ultérieures, par coupure temporelle ; Yang et collègues, 2025, « MOOSE-Chem » (élevée pour l'existence) : redécouverte d'hypothèses publiées après la coupure | risque de fuite et de contamination ; données rares |

[HYPOTHÈSE] Lecture d'ensemble : les familles qui ont produit des résultats vérifiés hors de l'opinion ont toutes un vérificateur exact ou une coupure temporelle. Les familles qui reposent sur un modèle juge de l'intérêt sont celles dont l'indice contraire est le plus fort. L'organisme a déjà un vérificateur sur les cartes ; il en manque pour les idées en texte libre.

### R3. Les mathématiques et les outils précis, et où chacun échoue

[PROPOSITION pour l'usage ; RAPPORTÉ DE MÉMOIRE pour les sources, certitude élevée sauf mention]

| outil | ce qu'il calcule ici | où il échoue |
|---|---|---|
| **Classes fonctionnelles** (prédictions sur le jeu public ; formes canoniques : diagrammes de décision binaires pour les règles logiques, simplification symbolique) | l'identité de deux idées, sans juge | tolérance à fixer ; deux cartes égales sur le jeu public peuvent différer ailleurs [FAIT LU — recoupement, § 8, borne 13] ; rien pour le texte libre |
| **Estimateurs d'espèces** : Good, 1953 (masse manquante) ; Chao, 1984 (richesse) ; Chao et Jost, 2012 (raréfaction et extrapolation par couverture) ; Orlitsky, Suresh et Wu, 2016 (nombre d'espèces non vues) ; capture et recapture entre familles (Lincoln et Petersen) | la part de classes encore jamais proposées ; le recouvrement entre familles ; la courbe d'accumulation de l'organisme | appels dépendants ; singletons faits de bruit ; « capturabilité » inégale entre familles, qui biaise la recapture |
| **Densité dans un espace de plongement** (noyaux, plus proches voisins, score de Vendi : Friedman et Dieng, 2023) | une description secondaire de la dispersion | le plongement code la formulation, pas le mécanisme ; manipulable ; grande dimension. Jamais un critère |
| **Théorie de l'information** : surprise −log w(c) ; variation totale et divergence de Kullback et Leibler entre les lois de classes sous deux vues | si une vue déplace la loi des propositions ; ce que vaut une prédiction audacieuse vérifiée | estimations instables pour les classes rares, là précisément où elles comptent ; l'estimateur direct de la divergence est biaisé. Préférer la variation totale avec un test par permutation sur les comptes |
| **Processus ponctuels déterminantaux** (répulsifs) sur un catalogue de vues [FAIT LU — recoupement, V6 : garantie sous indépendance et stabilité des réponses] | un lot de vues mutuellement dissemblables | la dissemblance des vues n'est pas celle des cartes ; effet nul si la loi des cartes ne dépend pas de la vue |
| **Plans combinatoires** (tableaux couvrants) [FAIT LU — recoupement, V3] | chaque combinaison de focalisations devant au moins un appel | couvrir des affectations n'est pas couvrir des idées ; rien ne garantit que le proposeur travaille sa focalisation |
| **Portefeuille sous-modulaire hors ligne** : choisir le nombre d'appels par couple « proposeur × vue » pour maximiser la couverture pondérée par une loi a priori sur les formes de puits ; le glouton approche l'optimum (Nemhauser, Wolsey et Fisher, 1978) [FAIT LU — recoupement, P1 : sort « suspendue »] | la seule notion d'optimum qui ait un sens ici : relative à une loi a priori déclarée | fréquences des bassins étroits indiscernables de zéro au budget d'un pilote [FAIT LU — recoupement, P1] ; mise en commun hiérarchique (estimateurs bêta-binomiaux par famille de mondes) en atténue une part seulement [HYPOTHÈSE] |
| **Identification du meilleur bras, hors ligne** (Audibert, Bubeck et Munos, 2010) [FAIT LU — recoupement, P2] | le meilleur couple sur des mondes d'étalonnage | garantie pour la loi des mondes d'étalonnage, pas pour des mondes futurs |
| **Recherche arborescente de Monte-Carlo** (Kocsis et Szepesvári, 2006) | l'extension d'un programme de recherche par étapes | il faut une valeur aux nœuds ; tirée des verdicts, c'est un pilotage par le juge, écarté [FAIT LU — recoupement, V12], et une réutilisation adaptative des données (Dwork et collègues, 2015, déjà cité au dépôt) ; je ne le rouvre pas |
| **Valeurs e et processus e** (Ville, 1939 ; Ramdas, Grünwald, Vovk et Shafer, 2023) ; règle de Benjamini et Hochberg appliquée aux valeurs e (Wang et Ramdas, 2022) ; tests multiples en ligne par valeurs e (Xu et Ramdas, 2024, certitude moyenne) | la profondeur, avec garantie de niveau ; plus de tirages aux cartes à effet localisé [FAIT LU — recoupement, J1] | elles garantissent la validité, pas la découverte [FAIT LU — recoupement, J1] ; nul composite sans preuve [J1, J6] |
| **Vérificateurs formels** (Lean, Isabelle) et **solveurs exacts** (satisfiabilité, satisfiabilité modulo théories, programmation linéaire en nombres entiers) ; recherche de contre-exemples (méthode d'entropie croisée : Wagner, 2021) | des tests de mort pour les lemmes, bornes et invariants proposés | formalisation fautive ; preuve d'un autre énoncé que celui visé ; l'absence de contre-exemple trouvé n'est pas une preuve |
| **Longueur minimale de description** (Rissanen, 1978 ; Grünwald, 2007) | une pénalité contre le rembourrage : profondeur par unité de description | dépend des primitives choisies [FAIT LU — recoupement, C1] |
| **Profondeur logique** (Bennett, 1988) ; **progrès de compression** (Schmidhuber, 2010) ; **nouveauté et apprenabilité relatives à un observateur** (Hughes et collègues, 2024, « Open-Endedness is Essential for Artificial Superhuman Intelligence ») | le fondement des deux axes : rare pour l'observateur, apprenable et compressif une fois vu | non calculables en général ; substituts : nombre de prérequis d'une chaîne, gain de prédiction sur plusieurs mondes |
| **Bornes inférieures** : énumération aveugle sous placement uniforme [FAIT LU — recoupement, § 8, borne 2] ; requêtes statistiques pour les parités (Blum et collègues, 1994 ; Kearns, 1998) ; absence de repas gratuit (Wolpert et Macready, 1997) | les détecteurs de fuite du banc ; les attentes honnêtes | elles valent sous leurs hypothèses (placement indépendant de tout ce que voit le proposeur) |
| **Analyse de survie** (Kaplan et Meier ; temps moyen restreint) ; **plan apparié par monde** ; test exact de McNemar ; taille d'échantillon pour proportions appariées (Connor, 1987, certitude moyenne) | le temps jusqu'à la découverte, censuré au budget | puissance faible si les mondes sont peu nombreux ; les cartes d'un même appel ne sont pas indépendantes [FAIT LU — recoupement, § 10, « Unité d'analyse »] |

**Trois dérivations élémentaires, de ma main.** [HYPOTHÈSE, non vérifiées par un tiers]
1. **Seuil de rentabilité.** À budget égal C, compté en appels de la référence, une méthode de coût κ par appel et de probabilité p de proposer la classe c bat la référence (coût 1, probabilité p₀) si et seulement si (1 − p)^(1/κ) < 1 − p₀. Pour des probabilités petites, la condition devient λ = p / p₀ > κ : le gain d'efficacité doit dépasser le surcoût.
2. **Tempérer par classe, pas par jeton.** Répartir les tirages du juge ou le choix des représentants selon w(c)^(−β) ne change pas quelles classes sont proposées (borne 1 du recoupement) : cela réduit seulement les pertes en aval. La validité du juge n'en souffre pas si w est estimée sur S₀, indépendant des tirages frais du juge ; une présélection qui n'utilise pas ces tirages ne touche pas la validité d'une valeur e.
3. **Optimum.** « Optimal » n'a de sens que pour une loi a priori π déclarée sur les formes de puits : maximiser la somme sur c de π(c) · [1 − produit sur les bras de (1 − p_bras(c))^(n_bras)], sous contrainte de coût. Le risque résiduel est la masse des formes hors de π ; seule la famille tenue à l'écart la mesure.

### R4. Éprouver l'organisme sur un banc où des puits connus sont plantés

[PROPOSITION ; les familles F3, F5, F6 et le contrôle positif reprennent des contrôles que la critique a fait apparaître : FAIT LU — recoupement, § 10]

**Générateur.** Le générateur de mondes est audité d'abord, sur processeur, sous préenregistrement [FAIT LU — table v1, § 1.4, banque sœur : N-049]. Les puits sont plantés par un tiers. Aucun modèle ne lit les mondes plantés ; l'appariement entre cartes et composantes plantées se calcule hors des agents.

**Familles de puits**, chacune avec son rôle :

| famille | forme | rôle |
|---|---|---|
| F0 | effet additif large | contrôle positif : toute méthode doit le trouver, sinon l'instrument est en panne |
| F1 | interaction hiérarchique (parent archivé) | puits étroit et accessible : la cible principale |
| F2 | chaîne de prérequis sur plusieurs générations | profondeur en chaîne [FAIT LU — recoupement, § 8, borne 4] |
| F3 | formes hors structure : seuil décentré, effet non monotone, interaction de trois traits | méthode et monde trop assortis ? [FAIT LU — recoupement, § 9] |
| F4 | barrière de parité : interaction sans marge d'ordre inférieur ni parent, placée au hasard après le gel de la vue | **détecteur de fuite** : aucune méthode ne doit dépasser la borne d'énumération aveugle |
| F5 | leurres : recollage par morceaux de lois archivées, sans composante plantée | **détecteur de fausse originalité** : leur promotion doit rester sous le niveau α |
| F6 | monde nul | fausses promotions sous le niveau α |
| F7 | famille tenue à l'écart, formes conçues par le tiers, jamais vues par les concepteurs de méthodes | lue une seule fois, à la fin |

**Étroitesse.** Connue par construction : nombre de classes candidates à la complexité du puits, placement au hasard. Le taux de la référence n'est mesuré que là où il est mesurable (puits d'étroitesse intermédiaire). Au-delà, l'étroitesse est dite « sous la résolution » (R1).

**Bases nommées**, toutes à budget égal en jetons facturés, cartes refusées par le gardien comptées, même borne sur le nombre de tests dans tous les bras [FAIT LU — recoupement, § 10, « Coût »] :
- B0 : le meilleur proposeur seul, vue ordinaire, meilleur de N tirages ;
- B1 : tirage au hasard dans la grammaire, énumérateur mécanique sans modèle, jusqu'à une taille bornée [FAIT LU — recoupement, § 10, « Comparaisons minimales »] ;
- B2 : recherche par nouveauté seule : l'orchestrateur garde des pierres de gué par distance fonctionnelle, sans verdict ;
- B3 : l'organisme actuel ;
- M : l'organisme avec la méthode candidate.

**Statistique principale.** Pour chaque monde w et chaque bras : D(w) = 1 si une carte de la composante plantée est retenue par le juge et confirmée par l'oracle avant le budget B, sinon 0. Pour chaque base b, la différence appariée Δ_b = P(D_M = 1) − P(D_b = 1) sur les mondes de la famille. Règle d'intersection et d'union : M doit battre chaque base, comme la porte de fin de phase 1 l'exige entre modes [FAIT LU — table v1, § 1.1, porte G1].

**Critère de réfutation, à sceller.**
- La revendication « M atteint les puits étroits plus vite que la base b » est **réfutée** si la borne haute de l'intervalle à 95 % de Δ_b est sous une marge δ scellée, sur F1 et sur F7.
- Le banc est **nul et non avenu**, sans signe positif, si M bat significativement la borne d'énumération sur F4 (fuite), ou si les promotions sur F5 ou F6 dépassent α (fausse originalité), ou si F0 échoue (instrument). Le même audit suit un résultat trop beau ou trop propre, dans les deux sens (R4).
- Lecture par famille, jamais regroupée : un gain d'ensemble peut cacher un échec total dans une famille [FAIT LU — 29, R3, « Ce qui la fausse », point 2].

**Mesures secondaires.** Temps moyen restreint jusqu'au budget ; entonnoir par puits (proposé, gardé, retenu) ; gain λ par famille ; taux de fausse originalité (R5).

**Prévision scellée avec son signe** (R1). [HYPOTHÈSE, ma prévision] M ne bat pas B0 sur F0 ; ne bat aucune base sur F4 ; bat B0 sur F1 seulement si la méthode agit en amont ; et l'écart de B2 (nouveauté seule) à B0 est nul ou négatif à budget égal. Confiance 0,5.

**Taille.** Unité : le monde ; grappes : les familles. La formule de Connor (1987) pour proportions appariées donne le nombre de mondes à partir des probabilités de paires discordantes, à sceller après les deux premiers essais du plan (R6).

### R5. La fausse originalité et le test qui la tue

| forme | signe | test qui la tue |
|---|---|---|
| **Bruit** (carte arbitraire) | rare ; « vraie » par hasard sur les tirages vus | tirages frais ; valeur e à niveau scellé ; oracle [FAIT LU — recoupement, « Vocabulaire »] |
| **Bizarrerie** (vraie mais sans portée : effet confiné à une région négligeable) | rare ; valeur e proche de 1 ; gain minuscule | profondeur minimale θ scellée ; borne de détectabilité [FAIT LU — recoupement, § 8, borne 5] |
| **Reformulation, renommage** | rare dans les mots, commune dans la fonction | classes fonctionnelles ; forme canonique ; permutation commune des noms de traits [FAIT LU — recoupement, § 10, « Comparaisons minimales »] |
| **Recollage par morceaux** | neuve pour un nul de mélanges à poids constants | nul étendu aux recollages bornés [FAIT LU — recoupement, J4, J7] ; leurres F5 ; oracle |
| **Rembourrage** (conditions inutiles) | échappe au regroupement | longueur minimale de description ; ablation de chaque condition : la retirer change-t-il les prédictions ? |
| **Jargon** (nom neuf d'un concept connu) | rare dans les mots | collisionneur étalonné sur témoins ; lecture tierce ; traduction en test exécutable |
| **Exploitation du juge** | promue, fausse selon l'oracle | banc de l'attaque de Goodhart, bras qui reçoit les verdicts contre bras qui ne les reçoit pas [FAIT LU — table v1, § 1.4, O12] ; tirages frais |
| **Idée inexécutable** (vague) | jugée nouvelle, jamais testable | exiger une prédiction scellée ; [RAPPORTÉ DE MÉMOIRE, certitude moyenne] l'écart entre idéation et exécution (Si, Hashimoto et Yang, 2025) |
| **Fuite** (le monde passe dans la vue ou les données) | trop beau : dépasse une borne d'impossibilité | puits F4 ; audit du générateur ; coupure temporelle pour les vraies questions |
| **Rareté d'artefact** (rare seulement parce que S₀ est petit ou biaisé) | masse manquante de Good et Turing élevée | dire la résolution ; second échantillon de référence indépendant |

[HYPOTHÈSE] Règle générale : une idée n'est comptée « puits » que si elle passe **trois portes indépendantes** : rareté sous une référence nommée, à résolution dite ; profondeur sur tirages frais ; vérité selon l'oracle ou, hors banc, selon un test exécutable ou une coupure temporelle.

### R6. Plan d'expériences, du moins cher au plus cher

[PROPOSITION ; chaque étape payante passe par un devis et le mot du directeur ; tout essai décisif est préenregistré (R1)]

| étape | coût | mesure | décide | arrêt ou repli |
|---|---|---|---|---|
| **E0. Diagnostic de l'entonnoir** | processeur seul, sur les journaux des courses passées | par composante plantée : proposée ? gardée ? retenue ? ; courbes d'accumulation ; masse manquante ; recouvrement entre familles par capture et recapture | amont ou aval ; la diversité des familles élargit-elle la couverture ? | si les propositions brutes manquent : journaliser à la prochaine course |
| **E1. La vue déplace-t-elle les propositions ?** | petit : appels sur mondes d'étalonnage | variation totale entre lois de classes sous vue ordinaire, vue placebo (même format, table permutée) [FAIT LU — recoupement, § 10, « Vue placebo »], et liste des paires non croisées (V2) ; test par permutation | garder ou écarter toutes les méthodes de vue | aucun déplacement au-delà du placebo : écarter les méthodes de vue [FAIT LU — recoupement, § 9, première objection] |
| **E2. Réglages des proposeurs** | petit à moyen | gain λ sur classes étroites et taux de fausse originalité, pour : échantillonnage verbalisé, seuil relatif et température, modèle de base si accessible, exclusion des classes banales prédites, ancrage dans les données propres, reformulation de la question | la composition, jugée sur l'oracle et le coût, jamais sur le verdict du juge [FAIT LU — CLAUDE.md, N-058] | λ ≤ κ pour tous les réglages : ce n'est pas le levier |
| **E3. Banc à puits plantés** (R4), préenregistré | moyen | Δ_b par base ; validité sur F5 et F6 ; fuite sur F4 ; F7 lue une fois | la revendication, sa réfutation, ou la nullité du banc | audit de symétrie si trop beau ou trop propre |
| **E4. Chaînes et mémoire** | moyen à élevé | F2 sur plusieurs générations ; mémoire héritée, née vide, ou aucune | garder ou non le dessin à plusieurs générations | [FAIT LU — table v1, § 1.4, énoncé 5] la forme « héritée puis tenue, contre née vide et aucune » est déjà celle du programme ; rien de neuf n'y est dit |
| **E5. Transfert aux vraies questions** | moyen | épreuves à coupure temporelle bâties par un tiers sur la littérature du contrôle, postérieure à la coupure de tous les proposeurs ; prédictions scellées, lues plus tard | les gains du banc passent-ils au champ ? | contamination établie : épreuve écartée, dite |
| **E6. Entraîner un proposeur** sur les puits vérifiés | élevé (processeurs graphiques) | λ après entraînement, sur F7 et à coupure temporelle | investir ou non | seulement si E2 et E3 montrent un plafond ; touche la règle « aucun verdict servi » : nœud |

[HYPOTHÈSE] Architecture que je recommande si E0 à E3 le confirment : en amont, ancrage dans les données propres et reformulation des questions d'abord (ils changent l'information, pas seulement sa présentation), puis la composition choisie sur l'oracle ; en aval, regroupement fonctionnel, allocation des tirages tempérée par classe, processus e à arrêt optionnel pour les cartes à effet localisé, nul étendu aux recollages bornés ; entre générations, un registre des tentatives qui garde des pierres de gué exécutables, jamais versées au nul.

### R7. Question neutre pour le collisionneur, l'organisme et d'autres modèles avancés

[PROPOSITION ; à passer au test de devinette par un agent neuf avant tout envoi]

> Un dispositif réunit plusieurs générateurs automatiques de propositions (hypothèses, mécanismes, questions de recherche), des évaluateurs, des épreuves sur des mondes simulés dont un programme connaît la vérité, et une mémoire transmise d'un cycle au suivant. Les propositions qu'il produit le plus souvent sont rarement les plus utiles.
> 1. Par quelles grandeurs, calculables sur ses sorties, distingueriez-vous une proposition rare et juste d'une proposition commune, et d'une proposition rare parce que fausse, bizarre ou simplement reformulée ?
> 2. Si vous recourez à un évaluateur automatique de la nouveauté, comment mesurez-vous ses erreurs et sa complaisance ?
> 3. Quelles méthodes, quels objets mathématiques et quels outils augmenteraient, à coût égal, la part de propositions rares et justes ? Où chacun échoue-t-il ? Qu'est-ce qui est impossible quoi qu'on fasse ?
> 4. Quel banc d'essai, contre quelles comparaisons nommées et avec quel critère de réfutation écrit d'avance, montrerait que le dispositif fait mieux que des tirages indépendants au même coût ?
> 5. Dans quel ordre, du moins cher au plus cher, mèneriez-vous les expériences, et que déciderait chacune ?
> Dites votre degré de certitude et ce que vous citez de mémoire ; aucun chiffre sans sa source.

### Ce qui touche une règle ou un texte en vigueur

[FAIT LU pour les règles citées ; HYPOTHÈSE pour le rapprochement] Rien n'est modifié.
- Composition des proposeurs jugée sur l'oracle et le coût, jamais sur le verdict du juge [CLAUDE.md, N-058] : E2 et E3 s'y conforment.
- Aucun score servi aux proposeurs [recoupement, § 1, V12] : E6 et toute allocation par rareté servie au proposeur y toucheraient ; nœud.
- Mémoire = registre des tentatives [table v1, § 1.4, énoncé 5] : des pierres de gué non vérifiées y ont leur place, hors du nul.
- Universalité sur familles inédites [CLAUDE.md, N-044] et lot final lu une fois [CLAUDE.md, N-050] : F7.
- « Neuf pour le champ » après lecture tierce [demande 34] : rien de cette réponse n'est dit neuf.

### Antériorité et statut

[HYPOTHÈSE] Rien n'est revendiqué ici. La mesure à deux références, les estimateurs d'espèces appliqués aux sorties de modèles, et un banc à puits plantés avec leurres sont probablement occupés en partie (recherche de qualité et diversité ; bancs de redécouverte et mondes virtuels de découverte ; travaux sur la diversité des sorties de modèles). Une zone qui paraît vierge reste une question (R8) ; elle se vérifie plus durement parce qu'elle séduit. [RAPPORTÉ DE MÉMOIRE, certitude moyenne] Voisins à lire d'abord : Jansen et collègues, 2024, « DiscoveryWorld » ; Majumder et collègues, 2024, « DiscoveryBench » ; Gandhi et collègues, 2025, « BoxingGym » ; Zhang et collègues, 2025, « NoveltyBench » ; Agarwal et collègues, 2025, sur la découverte ouverte guidée par la surprise bayésienne (peut-être l'« AUTODISC » que cite la table v1, § 3 : rapprochement non vérifié).

## Réserves

- Je n'ai lu aucun PDF : toutes les sources de R2 à R5 sont rapportées de mémoire ; un titre peut être inexact.
- Je n'ai lu ni les conceptions de l'organisme, ni ses journaux, ni aucun monde planté : E0 suppose que les propositions brutes sont journalisées, ce que je n'ai pas vérifié.
- Opus et Fable sont de la même famille de modèles : un accord entre ma réponse et celle de Fable n'est pas une confirmation indépendante.
- Les trois dérivations de R3 sont de ma main ; elles demandent une vérification par un tiers avant d'entrer dans un préenregistrement.

## Décisions pour le directeur

**D-1. Adopter la mesure à deux références (rareté sous une loi de propositions nommée, profondeur contre le nul de l'archive) comme grandeur de l'originalité de l'organisme, sans juge de nouveauté.**
- Enjeu : sans elle, « original » reste un avis, et un juge complaisant décide.
- (a) Mesure seulement (banc, rapports), jamais signal de sélection. Avantage : aucune boucle de Goodhart. Inconvénient : l'organisme ne s'en sert pas pour mieux chercher.
- (b) Mesure et signal d'allocation dans l'orchestrateur, jamais servi aux proposeurs. Avantage : moins de pertes en aval. Inconvénient : un critère de rareté entre dans la sélection ; à éprouver d'abord.
- (c) Statu quo. Avantage : rien à changer. Inconvénient : le défaut redouté reste non mesuré.
- Recommandation : (a) maintenant, (b) après le banc. Confiance 0,65. Défaut sous 48 heures : (a).

**D-2. Lancer le diagnostic de l'entonnoir sur les courses passées.**
- Enjeu : il décide s'il faut agir en amont ou en aval ; il ne coûte que du processeur.
- (a) Maintenant, par programme, sans qu'aucun modèle lise les mondes plantés ni les fichiers protégés. Avantage : gratuit et décisif. Inconvénient : les journaux bruts peuvent manquer.
- (b) Sur la prochaine course seulement, instrumentée. Avantage : journaux complets. Inconvénient : une génération de retard.
- Recommandation : (a), puis (b) si les journaux manquent. Confiance 0,8. Défaut sous 48 heures : (a) (travail de routine sur processeur).

**D-3. Ouvrir les devis de l'essai « la vue déplace-t-elle les propositions ? », puis des réglages des proposeurs.**
- Enjeu : toutes les méthodes de vue reposent sur un effet que rien ne montre encore.
- (a) Devis des deux essais ensemble. Avantage : un seul aller-retour. Inconvénient : dépense engagée avant le diagnostic.
- (b) Diagnostic d'abord, puis devis du premier essai seul. Avantage : la dépense suit l'information. Inconvénient : quelques jours.
- Recommandation : (b). Confiance 0,7. Pas de défaut : dépense.

**D-4. Commander le préenregistrement du banc à puits plantés.**
- Enjeu : c'est le seul test de la phrase « l'organisme trouve des puits étroits ».
- (a) Conception par Fable (pièce décisive), puits plantés par un tiers d'une autre lignée, famille tenue à l'écart lue une fois ; scellement après les deux premiers essais. Avantage : conforme aux règles du dépôt ; strates réalistes. Inconvénient : quota de Fable ; délai.
- (b) Différer toute conception jusqu'après les deux premiers essais. Avantage : aucune conception perdue. Inconvénient : rien d'opposable avant.
- Recommandation : (a). Confiance 0,7. Défaut sous 48 heures : (b).

**D-5. Ajouter un bras « données propres au programme » aux réglages des proposeurs.**
- Enjeu : la rareté sous les modèles des concurrents, donc le risque d'être devancé.
- (a) Un bras, sous les règles de cloisonnement (pièces scellées et lues seulement). Avantage : seule source systématique de rareté externe. Inconvénient : une garde de fuite de plus.
- (b) Non. Avantage : rien à garder. Inconvénient : l'organisme reste dans le bassin commun aux concurrents.
- Recommandation : (a). Confiance 0,6. Défaut sous 48 heures : (a).

**D-6. Passer la question neutre au test de devinette avant tout envoi.**
- Enjeu : une question qui laisse deviner la réponse attendue rend l'avis des autres modèles sans valeur.
- (a) Test par un agent neuf, puis envoi au collisionneur, à l'organisme et aux modèles nommés. Avantage : neutralité mesurée. Inconvénient : un appel de plus.
- (b) Envoi direct. Avantage : vite. Inconvénient : neutralité supposée.
- Recommandation : (a). Confiance 0,8. Défaut sous 48 heures : (a).

FIN DE LA RÉPONSE
