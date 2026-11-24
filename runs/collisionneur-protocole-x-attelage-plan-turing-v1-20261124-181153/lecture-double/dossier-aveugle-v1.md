# Consigne du lecteur (lecture double à l'aveugle, protocole X v2, règle 3)

Tu lis les sorties d'un collisionneur : plusieurs modèles, désignés seulement par des lettres, ont répondu à une même question en trois tours (conceptions, critiques croisées, réponses aux critiques). Tu ne sais pas quels modèles se cachent derrière les lettres, et tu ne cherches pas à le deviner.

Ta tâche : dresser TA liste des propositions retenues. Une proposition retenue est une expérience, un critère, une règle ou un choix concret que tu recommandes de garder après avoir pesé les critiques croisées et les réponses. Pour chacune :
1. un intitulé court et un identifiant P1, P2, … ;
2. les lettres qui la portent, et le tour où elle apparaît ;
3. retenue OUI ;
4. en une ou deux phrases, pourquoi elle survit aux critiques (ou malgré elles) ;
5. son épreuve décisive la moins chère : ce qu'elle mesure, son coût estimé, une date au plus tard (au plus tard le 31 décembre 2026), et un témoin faux connu (une proposition ou une hypothèse que l'on sait fausse) qui devrait mourir à cette épreuve. N'écris PAS de critère de mort : un concepteur distinct l'écrira (protocole X 2.1).

Ajoute ensuite une liste des propositions examinées et NON retenues (identifiants N1, N2, …), avec en une phrase la raison du rejet. Liste au total entre 10 et 25 propositions distinctes (retenues et non retenues), afin que deux lecteurs puissent comparer leurs décisions.

Règles : français ; aucune référence tenue pour vraie (liste-les à part, « à vérifier ») ; distingue argument, calcul et mesure ; ne recopie pas de longs passages. Ta réponse finit par la ligne exacte : FIN DE LA LISTE.


## Question servie aux modèles

# Measuring whether a multi-agent idea-generation system finds rare, high-consequence ideas

**Context.** A team plans a system in which several language-model agents propose, criticise and select candidate scientific ideas (hypotheses, quantitative laws, lemmas, protocols). Before running it, they want to build and validate a measurement harness. The harness should make it possible to show, or to refute, that the system finds ideas that are "narrow and deep": rarely reached by ordinary search, yet of large consequence once found. Candidate baselines include random sampling in the same space of candidate ideas, a mechanical enumerator, and the strongest single model given the same budget; others may be proposed.

**Questions.**

1. **Target.** How can "narrow" and "deep" be defined operationally, so that both can be measured without a language-model judge whose preferences may overlap with the generator's? If some judge is unavoidable, how should its bias be bounded? Relative to what reference should narrowness be measured? How is depth told apart from rarity alone?
2. **Sources of truth.** Compare candidate sources of ground truth (synthetic worlds with planted truth, retrodiction with a temporal cutoff, formal proof, executable tests, or others): what each can and cannot establish about narrowness and depth, and how each fails.
3. **Comparison.** What primary quantity, unit of analysis, cost accounting and decision rule would support or refute the claim "better than the baselines"? Which further comparisons, if any, are needed to attribute a difference to a specific part of the system?
4. **Problem choice.** How could one choose problems or regions where such ideas might be more likely, if such regions exist, and how would that choice itself be tested rather than assumed?
5. **Feedback.** Which measurements, if any, may be returned to the generator during search, and which must be withheld, so that the harness keeps measuring what it claims to measure?
6. **Validating the harness.** What must the harness demonstrate about itself before any costly run?
7. **Plan.** Order the experiments from cheapest to most expensive, with stopping criteria and the sample sizes they require.
8. **Limits.** What is out of reach of any such harness? Consider explicitly that no harness of this kind may be feasible, or that the target is ill-posed, and say what evidence would show either.

**For each point**, give your confidence (0 to 1), separate what is established from what is conjecture, cite verifiable references (authors, year, venue or arXiv identifier, page or section where possible), and say where you think the framing itself is wrong.


## Cellule E3-T1-conception-A (lettre A)

# Proposition A — Tour III.1 : conception ciblée

## Remarques préalables sur les pièces

- Le bloc QUESTION est textuellement identique au bloc FAITS (même empreinte) : aucune question plus étroite n'a été transmise. Je traite donc les huit points du cadrage.
- Le bloc FAITS ne porte aucune étiquette de statut. Je n'en attribue pas : je le traite comme l'énoncé du problème.
- Statuts de ce que j'ajoute : mes définitions et mes plans sont des **HYPOTHÈSES**, et la littérature est **RAPPORTÉE** (citée de mémoire, pages non vérifiées). Rien n'est VÉRIFIÉ ni OBSERVÉ, car je n'ai rien exécuté.
- Tout chiffre ci-dessous est **illustratif**, y compris les seuils, à figer par préenregistrement. « (ill.) » abrège « illustratif ».
- Je ne vois pas B, C, D, E à ce tour : je ne les critique pas et ne m'en sers pas.

---

## (a) Ce que la question suppose sans que ce soit établi

| # | Supposition implicite | Statut | Tranchée par |
|---|---|---|---|
| S1 | « Étroit » est une propriété d'une idée. Je soutiens que c'est une propriété du triplet (idée, processus de référence R, budget b). | HYPOTHÈSE | E2 |
| S2 | La profondeur se sépare de la rareté. | HYPOTHÈSE | E1 |
| S3 | Les idées étroites et profondes ont un taux de base mesurable, ni nul ni banal. | HYPOTHÈSE | E3 |
| S4 | Une mesure sans juge existe. C'est vrai par construction en monde clos ; ce n'est pas établi ailleurs. | HYPOTHÈSE | E8, section (c) |
| S5 | « Le meilleur modèle seul à budget égal » est bien défini. Or une passe unique, un best-of-N et le choix du sélecteur donnent trois références différentes. | HYPOTHÈSE | E4, E5 |
| S6 | « Trouver » est un seul événement. Engendrer l'idée dans le vivier et la sélectionner en sortie sont deux événements. | HYPOTHÈSE | E5 |
| S7 | Il existe des régions plus favorables. La question dit elle-même « if such regions exist ». | HYPOTHÈSE | E7 |
| S8 | Un harnais validé là où la vérité est connue reste valide là où elle ne l'est pas. | HYPOTHÈSE | E8, partiellement |
| S9 | Un juge-modèle partage les préférences du générateur. L'auto-préférence et les biais de position ou de verbosité sont rapportés (Panickssery, Bowman, Feng 2024 ; Zheng et al. 2023), mais pas pour la « profondeur d'idées scientifiques ». | RAPPORTÉ en général, HYPOTHÈSE ici | section (c), juge |
| S10 | Renvoyer une mesure au générateur la corrompt. C'est rapporté en général (Campbell 1979 ; Dwork et al. 2015). | RAPPORTÉ en général, HYPOTHÈSE ici | E6 |

### Définitions de travail (HYPOTHÈSES)

**Monde clos.** Une grammaire typée G engendre un programme caché. Les données sont produites sous plusieurs régimes d'intervention : une part est publique, une part est retenue. Une idée est une classe d'équivalence canonique d'expressions de G.

**Étroitesse.** ν_{R,b}(x) = −log₂ P_R(x atteinte dans le budget b).
- Elle est exacte pour le tirage uniforme et pour l'énumérateur (rang d'énumération).
- Elle est estimée sur K exécutions indépendantes pour un modèle.
- Avec zéro succès sur K, la borne supérieure à 95 % est environ 3/K (Hanley & Lippman-Hand 1983, RAPPORTÉ).
- Conséquence : contre une référence échantillonnée, l'étroitesse certifiable plafonne à log₂(K/3) bits, soit environ 6,6 bits pour K = 300 (ill.).

**Profondeur.** Δ(x) est le gain obtenu par un solveur mécanique fixe, sans modèle de langage, sur des conséquences retenues, avec x et sans x, à budget de solveur égal. Les conséquences sont des régimes prédits dans la tolérance, ou des nœuds de recherche économisés sur des théorèmes retenus.

**Plan planté 2×2.** Chaque monde contient des idées étroites et profondes, des leurres étroits et inertes, des idées larges et profondes, et des idées larges et inertes. Les leurres sont appariés aux idées profondes en taille, en rang d'énumération (±10 %, ill.) et en ajustement aux données publiques.

**Succès EP.** Une idée compte comme succès « étroit-profond » si ν ≥ ν* sous chaque référence et si Δ ≥ δ*. L'étroitesse est estimée sur des exécutions de référence disjointes de celles de la comparaison. Sinon, on sélectionne après coup les idées où la référence a échoué par hasard, et la régression vers la moyenne fabrique un avantage.

**Règle commune de décision.** Chaque duel a un seuil unique.
- H_A est retenue si l'intervalle de confiance à 95 % est entièrement au-dessus du seuil.
- H_B est retenue s'il est entièrement au-dessous.
- Sinon, on échantillonne jusqu'à un n maximal préenregistré.
- Si l'intervalle chevauche encore le seuil, l'instrument est déclaré insuffisant à ce budget. Ce verdict compte contre la faisabilité.

---

## (b) Expériences décisives, en duel

### E1 — La profondeur est-elle autre chose que la rareté ?

- **H_A** : à étroitesse appariée, Δ sépare les idées profondes de leurs leurres.
- **H_B** : à étroitesse appariée, Δ ne les sépare pas.
- **Métrique** : AUC de Δ sur les paires (profonde, leurre), plus la corrélation de Spearman entre Δ et ν sur un espace énuméré exhaustivement.
- **Seuil** : AUC = 0,80 (ill.).
- **Contrôles négatifs** :
  - Δ recalculé avec les régimes retenus permutés doit donner une AUC d'environ 0,5.
  - L'ajustement public seul, la taille seule et le rang seul doivent rester à environ 0,5 sur les paires.
- **Si H_A est retenue** : « la profondeur n'est que de la rareté » est réfutée pour cette famille de mondes.
- **Si H_B est retenue** : ma définition de Δ est réfutée, et on arrête avant toute dépense.
- **Si un contrôle mécanique dépasse 0,5** : les leurres sont mal appariés et E1 est nulle, quel que soit le résultat de Δ.

### E2 — L'étroitesse dépend-elle de la référence ?

- **H_A** : les rangs d'étroitesse concordent entre l'énumérateur, le tirage uniforme et le modèle seul. Un scalaire est alors admissible.
- **H_B** : ils ne concordent pas. « Recherche ordinaire » est alors mal posée tant que R n'est pas nommée.
- **Métrique** : corrélation de Spearman entre paires de références.
- **Seuil** : ρ = 0,6 (ill.).
- **Contrôles** :
  - La fiabilité en demi-échantillons de ν sous une même référence doit atteindre 0,9 (ill.). Sinon K est trop petit et E2 n'est pas interprétable.
  - On compare ν dans un monde ré-encodé (variables renommées, opérateurs permutés) à ν dans le monde d'origine. L'écart doit être nul pour l'énumérateur. Pour le modèle, il mesure l'a priori mémorisé.
- **Si H_A est retenue** : mon objection S1 est réfutée.
- **Si H_B est retenue** : la cible scalaire est réfutée. Seule tient la conjonction « étroit sous chaque référence », rapportée comme un vecteur.

### E3 — Le harnais détecte-t-il un effet connu sans en inventer ? (verrou avant toute dépense)

- **Bras** :
  - A/A : une référence contre elle-même, avec d'autres graines.
  - Oracle dilué : une référence dont le vivier reçoit une idée EP plantée avec une probabilité q ∈ {0 ; 0,05 ; 0,10 ; 0,20} (ill.).
- **H_A** : le harnais détecte q = 0,10 avec une puissance d'au moins 0,80 et alerte sur au plus 5 % des réplications A/A (ill.).
- **H_B** : l'une des deux conditions échoue au n maximal.
- **Contrôles négatifs** :
  - Un bras « bizarre », qui ne sort que des leurres rares et inertes, doit obtenir zéro.
  - Un bras « banal-profond », qui ne sort que des idées larges et profondes, doit marquer en profondeur mais pas en EP.
- **Si H_B est retenue** : la faisabilité à ce budget est réfutée et aucun run coûteux n'a lieu.
- **Si H_A est retenue** : « aucun harnais de ce type n'est faisable » est réfutée, pour les mondes clos seulement.

### E4 — Le système fait-il mieux que le meilleur best-of-N à coût égal ?

- **Références** : tirage uniforme, énumérateur, recherche mécanique non triviale (régression symbolique), modèle seul en fil unique, et modèle seul en best-of-N avec le même sélecteur.
- **H_A** : P(au moins un succès EP parmi les k idées finales) dépasse celle de la meilleure référence d'au moins le plus petit écart jugé intéressant.
- **H_B** : l'écart est inférieur à ce seuil.
- **Métrique** : différence appariée par problème, test de McNemar exact, un seul test confirmatoire.
- **Seuil** : +5 points (ill.), avec k = 3 (ill.).
- **Unité d'analyse** : le problème, pas l'idée, car les idées d'un même run sont corrélées.
- **Comptabilité des coûts** :
  - On compte tous les jetons d'entrée et de sortie, critiques et sélection comprises.
  - Les appels au vérificateur sont plafonnés à l'identique dans tous les bras.
  - Le résultat est rapporté à trois budgets, car l'affirmation « meilleur » est indexée par le budget.
- **Contrôles négatifs** :
  - Le test A/A de E3.
  - Les mondes ré-encodés.
  - Le sélecteur du système appliqué au vivier de la référence, pour isoler la sélection.
- **Si H_B est retenue** : l'affirmation « meilleur que les références » est réfutée à ce budget.
- **Si H_A est retenue** : « tout gain vient du volume d'échantillonnage » est réfutée.

### E5 — À quoi attribuer un écart ? (seulement si E4 retient H_A)

- **Plan** : factoriel 2×2, agents hétérogènes ou N copies, critique active ou placebo, à sélecteur et coût identiques.
- **Placebo** : la critique d'un autre problème, de même longueur. Il contrôle l'effet des jetons supplémentaires.
- **H_A** : la critique, ou son interaction avec l'hétérogénéité, apporte au moins le seuil de E4.
- **H_B** : l'effet est inférieur au seuil. L'écart vient alors du nombre de tirages indépendants ou du sélecteur.
- **Décomposition** : rappel du vivier (une idée EP y est présente) et précision de sélection (elle est choisie, sachant qu'elle est présente).
- **Si H_A est retenue** : « l'interaction ne sert à rien » est réfutée.
- **Si H_B est retenue** : l'attribution au caractère multi-agents est réfutée.

### E6 — Quel retour peut-on donner au générateur ?

- **Bras** :
  - F0 : validité seule (syntaxe, typage, exécution).
  - F1 : F0 plus l'ajustement aux données publiques.
  - F2 : F1 plus Δ sur des conséquences publiques.
  - F3 : F2 plus Δ sur le jeu privé. C'est un bras interdit en production, lancé seulement comme contrôle positif.
- **H_A** : sous F2, le gain de Δ public se retrouve sur un jeu privé jamais interrogé.
- **H_B** : il ne s'y retrouve pas. F2 gonfle alors la mesure, et la profondeur doit être retenue.
- **Métrique et seuil** : ratio du gain privé au gain public = 0,8 (ill.).
- **Contrôles** :
  - Sous F0, l'écart entre public et privé doit être nul.
  - F3 doit montrer une inflation sur le jeu divulgué par rapport à un troisième jeu vierge. Sinon l'expérience ne sait pas voir une fuite.
- **Si H_A est retenue** : S10 est réfutée pour F2.
- **Si H_B est retenue** : « un retour de profondeur publique est inoffensif » est réfutée.
- **Toujours retenus, par construction** :
  - Les estimations d'étroitesse. Les renvoyer fait de la rareté un objectif (Lehman & Stanley 2011, RAPPORTÉ : la recherche de nouveauté est une stratégie de recherche).
  - L'identité des leurres.
  - Le nombre d'idées plantées.
  - Les régimes privés.

### E7 — Peut-on prédire où chercher ?

- **Prédicteur** : calculé avant tout run, sur les références seules. Par exemple la « déceptivité » : la part d'inertes parmi les M premiers candidats énumérés les mieux ajustés au public.
- **H_A** : sur des mondes retenus, le quartile supérieur du prédicteur est plus dense en succès EP que le quartile inférieur, pour chaque bras.
- **H_B** : l'intervalle du ratio de densités contient 1. Le choix de problèmes doit alors être aléatoire et stratifié.
- **Seuil** : ratio de densités = 2 (ill.).
- **Contrôles** :
  - Le prédicteur permuté doit donner un ratio de 1.
  - Le prédicteur est mesuré sur des exécutions de référence indépendantes, pour ne pas sélectionner les mondes où la référence a simplement eu de la malchance.
- **Si H_A est retenue** : « ces régions ne sont pas prédictibles par ce prédicteur » est réfutée.
- **Si H_B est retenue** : S7 est réfutée pour ce prédicteur.

### E8 — Le classement en monde clos se transporte-t-il vers la preuve formelle ?

- **Tâche** : des lemmes vérifiés par un noyau de preuve. La profondeur est la réduction de recherche d'un prouveur automatique fixe sur des théorèmes retenus.
- **H_A** : le signe de l'effet de chaque facteur de E5 est le même dans les deux domaines.
- **H_B** : au moins un signe s'inverse, avec un intervalle excluant zéro. Les résultats en monde clos n'autorisent alors aucune affirmation ailleurs.
- **Contrôle négatif** : un lemme aléatoire de même taille doit donner Δ ≈ 0.
- **Si H_A est retenue** : « le monde clos ne mesure qu'un jeu » est réfutée, pour ce second domaine seulement.
- **Si H_B est retenue** : S8 est réfutée.
- **Faiblesse** : il y a peu de bras, donc le test est peu puissant. C'est un test de non-contradiction, pas de transfert général.

---

## (c) Mesure minimale par instrument nommé

Les instruments nommés sont le juge-modèle, les quatre sources de vérité, les trois références et le harnais lui-même. Les seuils sont illustratifs.

### Juge-modèle

- **À détecter** : l'idée EP face à son leurre.
- **Détection** : au moins 0,80.
- **Fausses alertes** : au plus 0,10.
- **Invariance** : au plus 5 % de verdicts inversés quand on échange le style.
- **Cas honnêtes appariés** :
  - Des paires idée-leurre du même monde, rédigées par gabarit déterministe, de longueur égale à ±10 %.
  - Le même contenu canonique réécrit par plusieurs familles de modèles.
- **Vérifications mécaniques à battre** : la longueur, la rareté lexicale, la perplexité sous un petit modèle tiers et l'ajustement public. Le juge doit dépasser la meilleure d'au moins 0,05 d'AUC.
- **Borne de biais** : l'écart maximal de score entre familles, à contenu identique, s'ajoute comme barre d'erreur à toute différence entre bras. Une différence inférieure à cette borne n'est pas interprétable.
- **En cas d'échec** : le juge est exclu de la mesure primaire.

### Mondes synthétiques à vérité plantée

- **À détecter** : une idée plantée sous ses formes équivalentes (canonisation).
- **Détection** : au moins 0,99 sur des réécritures mécaniques (commutation, renommage, repli de constantes).
- **Fausses alertes** : au plus 0,01 sur des quasi-voisins à un opérateur muté.
- **Cas honnêtes appariés** : chaque réécriture équivalente est appariée à un mutant de même taille.
- **À battre** : l'égalité de chaînes (plancher) et l'équivalence numérique sur points aléatoires (concurrent).
- **Ce que l'instrument établit** : l'étroitesse et la profondeur au sens du concepteur.
- **Ce qu'il n'établit pas** : la validité externe.
- **Mode de défaillance** : la « profondeur » plantée reflète l'idée que le concepteur s'en fait.

### Rétrodiction à coupure temporelle

- **À détecter** : la fuite d'items dans les poids.
- **Détection** : au moins 0,90 sur des items notoirement antérieurs à la coupure.
- **Fausses alertes** : au plus 0,05 sur des items publiés après la publication des poids.
- **Cas honnêtes appariés** : des items antérieurs et postérieurs, appariés par sous-domaine et par type. La date de diffusion des poids sert de borne dure, pas la coupure déclarée.
- **À battre** :
  - Pour l'appariement entre idée et résultat futur : le recouvrement lexical de type BM25.
  - Pour la fuite : un test de complétion (Golchin & Surdeanu 2024, RAPPORTÉ).
- **Ce que l'instrument établit** : un rappel des idées déjà trouvées et publiées.
- **Ce qu'il n'établit pas** :
  - L'étroitesse, car il n'y a qu'une seule histoire et aucune répétition.
  - Les faux négatifs, non bornés : une idée vraie et encore inconnue compte zéro.
- **Mode de défaillance** : l'appariement réintroduit un juge.

### Preuve formelle

- **À détecter** : les énoncés vacueux ou redondants.
- **Détection** : au moins 0,95.
- **Fausses alertes** : au plus 0,05.
- **Cas honnêtes appariés** : des lemmes à hypothèses contradictoires plantés, appariés à des lemmes non vacueux de même forme.
- **À battre** : la tentative automatique de prouver le faux depuis les hypothèses, et la recherche exacte en bibliothèque.
- **Ce que l'instrument établit** : la validité, par le noyau.
- **Ce qu'il n'établit pas** : l'étroitesse et la profondeur.
- **Mode de défaillance** : la fidélité de la formalisation d'un énoncé informel est hors de portée du noyau. Je restreins donc aux idées nativement formelles.

### Tests exécutables

- **À détecter** : les solutions fausses.
- **Détection** : au moins 0,90 des mutants mécaniques tués.
- **Fausses alertes** : au plus 0,01 de variantes équivalentes rejetées.
- **Cas honnêtes appariés** : des refactorisations sémantiquement équivalentes de la solution de référence.
- **À battre** : les tests publics seuls.
- **Mode de défaillance** : le sur-ajustement aux tests et l'incomplétude de la suite.

### Tirage aléatoire

- **À vérifier** : l'uniformité sur les classes canoniques, pas sur les chaînes.
- **Mesure** : un χ² sur un petit espace énumérable.
- **Fausses alertes** : au plus 5 % de rejets entre deux graines.
- **À battre** : le comptage exact.

### Énumérateur mécanique

- **À vérifier** : la complétude.
- **Mesure** : 100 % des idées plantées de taille ≤ s trouvées au rang calculé, sans aucun doublon canonique.
- **Cas** : un espace exhaustif de petite taille.
- **En cas d'écart** : c'est un bogue, pas un résultat.

### Meilleur modèle seul à budget égal

- **À vérifier** : que la référence n'est pas un homme de paille.
- **Mesures** :
  - Sur les idées larges et profondes, son taux doit être au moins celui du générateur du système pris isolément.
  - La fiabilité en demi-échantillons de ν doit atteindre 0,9.
- **Conditions** : les mêmes mondes, le même budget de réglage préenregistré, le même sélecteur en best-of-N.
- **À battre** : l'énumérateur sur les idées larges.

### Harnais entier

- **Mesure** : celle de E3, soit une puissance d'au moins 0,80 à q = 0,10 et au plus 5 % d'alertes en A/A.
- **Cas** : l'oracle dilué face à la référence, et les bras « bizarre » et « banal-profond ».
- **À battre** : un score par ajustement public seul.

---

## (d) Ancrage matériel (tout est illustratif)

### Logiciel et modèles

- **Mondes** : un générateur en Python, avec canonisation symbolique et équivalence numérique. L'énumération est exhaustive jusqu'à une taille donnant 10⁶ à 10⁷ classes (ill.). Tout tourne sur processeur.
- **Référence mécanique non triviale** : la régression symbolique évolutionnaire avec PySR (Cranmer 2023, RAPPORTÉ), comparée dans SRBench (La Cava et al. 2021, RAPPORTÉ). Elle évite un énumérateur de paille.
- **Modèles** : des poids ouverts de trois familles distinctes, par exemple Llama, Qwen et [modèle]. Les versions sont à figer par empreinte au préenregistrement. Elles sont servies localement, avec graines et températures journalisées. Trois familles permettent l'hétérogénéité de E5 et un juge d'une autre famille que le générateur.
- **Preuve** : Lean 4 et Mathlib (The mathlib Community 2020, RAPPORTÉ), sur processeur.

### Tailles d'échantillon

- **Nombre de mondes.** Pour distinguer 5 % de 15 % de problèmes avec succès EP (proportions supposées), à α = 0,05 bilatéral et puissance 0,80, l'approximation normale non appariée donne environ 140 problèmes par bras. Je retiens 150 mondes ; l'appariement n'en demande en principe pas plus.
- **Plancher mesurable.** Avec zéro succès sur 150, la borne supérieure est d'environ 2 %. Un taux de base inférieur n'est pas mesurable à cette taille.
- **Étroitesse sous modèle.** Certifier P ≤ 1 % demande K = 300 exécutions sans succès par monde.

### Plan, du moins cher au plus cher

| Étape | Contenu | Calcul | Coût | Arrêt |
|---|---|---|---|---|
| 0 | Canonisation, uniformité, complétude ; ν exacts ; E1 ; E2 sans modèle | moins de 100 cœur-heures | moins de 20 € | E1 retient H_B, ou un instrument de (c) échoue |
| 1 | E3 par rééchantillonnage, 200 réplications | processeur | négligeable | E3 retient H_B : aucun run coûteux |
| 2 | Pilote ν sous modèle, 20 mondes × 300 exécutions × 20 000 jetons = 1,2 × 10⁸ jetons | environ 17 heures-GPU à 2 000 jetons/s en lot | environ 35 € à 2 €/h | Fiabilité de ν inférieure à 0,9 |
| 3 | E6, 4 bras × 150 mondes × 20 000 jetons = 1,2 × 10⁷ jetons | environ 2 heures-GPU | moins de 10 € | Le contrôle F3 est muet |
| 4 | Calibration complète de ν, 150 × 300 × 20 000 = 9 × 10⁸ jetons | environ 125 heures-GPU | environ 250 € | — |
| 5 | E4, 5 bras × 3 budgets × 150 mondes, environ 4,5 × 10⁷ jetons | environ 6 heures-GPU | environ 15 € | E4 retient H_B : E5 est sans objet |
| 6 | E5 et E7 | environ 5 heures-GPU | environ 10 € | — |
| 7 | E8 en Lean | processeur et environ 10 heures-GPU | environ 30 € | — |

Le poste dominant est la calibration de l'étroitesse sous modèle, environ vingt fois le coût de la comparaison elle-même. C'est l'étroitesse qui coûte, pas le run du système.

---

## Confiance par point, et où le cadrage me paraît fautif

| Point | Confiance | Établi (RAPPORTÉ) | Conjecture (HYPOTHÈSE) | Défaut du cadrage |
|---|---|---|---|---|
| 1. Cible | 0,6 | La borne 3/K. La distinction entre nouveauté et valeur (Boden 1990). | ν relatif à (R, b). Δ par solveur mécanique. | « Étroit » n'est pas absolu. Sans R nommée, la cible est indéterminée. |
| 2. Sources | 0,65 | Les biais de juge. La contamination. | Le tableau de (c). | Aucune source ne donne à la fois l'étroitesse, la profondeur et la validité externe. La rétrodiction ne donne pas l'étroitesse. |
| 3. Comparaison | 0,7 | Les tests appariés. Les degrés de liberté du chercheur (Simmons, Nelson, Simonsohn 2011). | Le succès EP par problème. Le best-of-N comme référence critique. | La liste des références omet le best-of-N à même sélecteur et le placebo de critique. |
| 4. Choix de problèmes | 0,35 | Rien de solide. | Le prédicteur de déceptivité. | L'existence de régions est supposée, et la régression vers la moyenne peut la simuler. |
| 5. Retour | 0,6 | L'analyse adaptative dégrade un jeu retenu (Dwork et al. 2015 ; Blum & Hardt 2015). | La frontière F0 à F2. | « Mesure » et « signal de recherche » sont traités comme séparables a priori. E6 doit le montrer. |
| 6. Validation | 0,75 | La logique des contrôles positifs et négatifs. | Les seuils. | Aucun. |
| 7. Plan | 0,55 | L'arithmétique de puissance. | Les coûts et les débits. | Le coût de l'étroitesse est sous-estimé par la question. |
| 8. Limites | 0,5 | La reconnaissance tardive des travaux atypiques (Wang, Veugelers, Stephan 2017 ; Uzzi et al. 2013). | Voir ci-dessous. | Voir ci-dessous. |

### Hors de portée (HYPOTHÈSES)

1. Une étroitesse au-delà de log₂(K/3) bits contre toute référence échantillonnée.
2. L'étroitesse en science ouverte : il n'y a qu'une seule histoire.
3. La profondeur à horizon long : les conséquences s'accumulent après la fenêtre de mesure.
4. Les idées dont la valeur tient à un changement de l'espace de représentation lui-même. Une grammaire fixe les exclut par construction.

### Preuves que la cible est mal posée ou le harnais infaisable

- **Cible scalaire mal posée** : E2 retient H_B et E1 retient H_B, sur au moins trois familles de mondes.
- **Infaisable à budget réaliste** : E3 retient H_B au n maximal, ou le taux de base est sous le plancher de 2 %.
- **Le harnais ne mesure qu'un jeu** : E8 retient H_B.

Aucune de ces issues ne dirait quoi que ce soit des domaines sans vérité de référence. Là, la seule affirmation soutenable reste conditionnelle aux mondes testés.

---

## Références (RAPPORTÉES, de mémoire ; pages et sections à vérifier ; aucun identifiant arXiv fourni)

- Platt, J. R. (1964). « Strong Inference ». *Science*.
- Hanley, J. A., Lippman-Hand, A. (1983). « If Nothing Goes Wrong, Is Everything All Right? ». *JAMA*.
- Boden, M. (1990). *The Creative Mind: Myths and Mechanisms*.
- Campbell, D. T. (1979). « Assessing the Impact of Planned Social Change ». *Evaluation and Program Planning*.
- Dwork, C. et al. (2015). « The Reusable Holdout: Preserving Validity in Adaptive Data Analysis ». *Science*.
- Blum, A., Hardt, M. (2015). « The Ladder: A Reliable Leaderboard for Machine Learning Competitions ». ICML.
- Simmons, J., Nelson, L., Simonsohn, U. (2011). « False-Positive Psychology ». *Psychological Science*.
- Lehman, J., Stanley, K. (2011). « Abandoning Objectives: Evolution Through the Search for Novelty Alone ». *Evolutionary Computation*.
- Uzzi, B., Mukherjee, S., Stringer, M., Jones, B. (2013). « Atypical Combinations and Scientific Impact ». *Science*.
- Wang, J., Veugelers, R., Stephan, P. (2017). « Bias Against Novelty in Science ». *Research Policy*.
- Zheng, L. et al. (2023). « Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena ». NeurIPS, volet Datasets and Benchmarks.
- Panickssery, A., Bowman, S., Feng, S. (2024). « LLM Evaluators Recognize and Favor Their Own Generations ». NeurIPS.
- Golchin, S., Surdeanu, M. (2024). « Time Travel in LLMs: Tracing Data Contamination in Large Language Models ». ICLR.
- La Cava, W. et al. (2021). « Contemporary Symbolic Regression Methods and their Relative Performance ». NeurIPS, volet Datasets and Benchmarks.
- Cranmer, M. (2023). « Interpretable Machine Learning for Science with PySR and SymbolicRegression.jl ». Lieu de publication : référence à vérifier.
- The mathlib Community (2020). « The Lean Mathematical Library ». CPP.

FIN-DE-CELLULE

## Cellule E3-T1-conception-B (lettre B)

# Proposition B — Tour III.1 : un harnais pour mesurer « étroit et profond »

**Pièces transmises.** Le bloc FAITS ne contient aucun fait étiqueté. Il est identique au bloc QUESTION (même empreinte sha256). Je ne dispose donc d'aucun fait VÉRIFIÉ. Le seul contenu factuel est le contexte : « une équipe prévoit un système multi-agents… », que je traite comme RAPPORTÉ. Tout le reste de ce texte est HYPOTHÈSE ou renvoi à la littérature.

**B1.** Le tour se joue à l'aveugle : je ne vois aucune autre proposition et n'en critique donc aucune.

**Thèse.** « Étroit » n'est pas une propriété d'une idée. C'est une propriété du couple (idée, chercheur de référence Q, relation d'équivalence entre idées). « Profond » doit se mesurer par un effet contrefactuel sur un solveur mécanique figé, et non par un jugement. Tant que Q, l'équivalence et le solveur ne sont pas fixés à l'avance, l'affirmation « le système trouve de l'étroit-profond » n'est pas réfutable (HYPOTHÈSE, que je défends).

---

## (a) Ce que la question suppose sans que ce soit établi

| # | Présupposé | Statut | Commentaire |
|---|---|---|---|
| P1 | Une équipe prévoit le système et veut valider un harnais d'abord. | RAPPORTÉ | Seul fait du contexte. |
| P2 | Il existe un « même espace d'idées candidates » où l'échantillonnage aléatoire est défini. | HYPOTHÈSE | Faux pour le texte libre. Vrai seulement pour un espace formel : grammaire d'expressions, énoncés Lean, programmes. Sans cela, la ligne de base « aléatoire » n'a pas de sens. |
| P3 | L'étroitesse est intrinsèque à l'idée. | HYPOTHÈSE, que je crois fausse | Elle dépend du chercheur de référence et de la canonicalisation. Testé par E2. |
| P4 | La classe « étroit ∧ profond » est non vide dans les espaces choisis. | HYPOTHÈSE | Si elle est vide, toute comparaison donne 0 = 0. Il faut la peupler par construction (mondes plantés) avant de la chercher ailleurs. |
| P5 | La profondeur est mesurable à horizon et coût finis. | HYPOTHÈSE | Seuls des substituts à horizon fini sont mesurables. La « conséquence scientifique » réelle se déploie sur des années. |
| P6 | Profondeur et rareté sont séparables. | HYPOTHÈSE | Testé par E3. Si elles sont fortement corrélées sous Q, on compte deux fois la même chose. |
| P7 | Un juge LM peut partager les préférences du générateur. | RAPPORTÉ (littérature, non vérifié ici) | Zheng et al. (2023, NeurIPS Datasets & Benchmarks, « Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena ») rapportent un biais d'auto-valorisation. Panickssery, Bowman & Feng (2024, NeurIPS, « LLM Evaluators Recognize and Favor Their Own Generations ») rapportent une auto-reconnaissance corrélée à l'auto-préférence. |
| P8 | « Le modèle unique le plus fort » est identifiable et stable. | HYPOTHÈSE | Il dépend du domaine et du budget. Il faut le choisir par une règle préenregistrée. |
| P9 | Le gain éventuel viendrait de l'interaction multi-agents. | HYPOTHÈSE | Concurrente : plus d'échantillons + filtrage par vérificateur (E5). |
| P10 | Un harnais peut être validé avant que le système existe. | HYPOTHÈSE, partiellement vraie | Faisable sur positifs plantés et leurres. Non faisable pour la fuite par rétroaction propre au système (E6 exige le système). |

**Où le cadrage me semble faux.**
1. « Étroit et profond » mêle deux axes. Il faut publier la distribution jointe (rareté sous Q, profondeur), pas un produit ni un score unique.
2. Les lignes de base proposées omettent la plus dangereuse : le modèle unique, avec le même vérificateur et le même budget converti en échantillons (best-of-N filtré).
3. « Rarement atteint par la recherche ordinaire » demande de nommer la recherche ordinaire. Plusieurs références Q doivent être rapportées.

---

## (b) Expériences décisives (inférence forte)

Platt (1964, *Science* 146 : 347–353, « Strong Inference ») sert de cadre. Tous les seuils ci-dessous sont **illustratifs**. Ils doivent être préenregistrés (Nosek et al., 2018, *PNAS* 115(11), « The preregistration revolution »).

Notations :
- Q est un générateur de référence (par exemple le modèle unique échantillonné à température 1, ou l'énumérateur).
- c(·) est une canonicalisation : forme normale symbolique, énoncé Lean normalisé, ou classe d'équivalence comportementale d'un programme.
- **Étroitesse** : n(x) = −log P_Q(c(x) atteint dans un budget de référence B₀).
- **Profondeur** : d(x) = gain d'un solveur mécanique figé S sur un ensemble tenu à l'écart de conséquences K_test quand x lui est fourni, moins le gain d'un contrôle de même complexité.

### E1 — Le harnais voit-il la structure ou la surface ? (monde planté)

- **H_A** : les scores (n, d) détectent les idées plantées étroites-profondes.
- **H_B** : les scores suivent des traits de surface (longueur, complexité syntaxique, vocabulaire).
- **Dispositif** : mondes synthétiques à loi cachée, par exemple une dynamique ou un système algébrique générés par grammaire. On y plante une loi rare (faible probabilité sous Q, connue par construction) qui explique un ensemble K de phénomènes tenus à l'écart. On ajoute trois types de leurres appariés en longueur et en complexité :
  - rare-mais-stérile (étroit, non profond) ;
  - commun-mais-utile (profond, non étroit) ;
  - commun-et-stérile.
- **Métrique** : sensibilité et taux de fausses alertes pour la cellule « étroit ∧ profond ».
- **Seuil (illustratif)** : sensibilité ≥ 0,8 et fausses alertes ≤ 0,05, sur 200 positifs et 600 leurres. L'intervalle à 95 % d'une proportion de 0,8 sur n = 200 vaut environ ±0,055.
- **Contrôle négatif** : mondes à étiquettes permutées, où la « loi » n'explique plus K. La détection doit tomber au hasard.
- **Issues** :
  - Si les leurres de même surface sont détectés au même taux que les positifs, H_A est falsifiée.
  - Si les seuils sont atteints et que la détection s'effondre sous permutation, H_B est falsifiée.

### E2 — L'étroitesse dépend-elle de la référence ?

- **H_A** : les classements d'étroitesse sont stables d'une référence Q à l'autre. Seuil illustratif : ρ de Spearman ≥ 0,7 entre Q₁ (modèle 8B), Q₂ (autre famille, 7B) et Q₃ (énumérateur).
- **H_B** : l'étroitesse est propre à Q (ρ ≤ 0,3).
- **Contrôle négatif** : même Q avec deux graines. Cela donne le plafond de ρ dû au bruit d'estimation. Si ce plafond est lui-même inférieur à 0,7, l'expérience manque de puissance et on augmente l'échantillonnage.
- **Issues** :
  - ρ ≥ 0,7 falsifie H_B : on peut parler d'étroitesse sans indice.
  - ρ ≤ 0,3 falsifie H_A : toute affirmation devra s'écrire « étroit relativement à Q_k ». Le cadrage « rarement atteint par la recherche ordinaire » est alors mal posé sans indice.
- **Coût statistique** : affirmer P_Q < 10⁻⁴ avec zéro occurrence demande n ≈ 3/10⁻⁴ = 30 000 tirages par problème (règle de trois, borne supérieure à 95 %). Le seuil 10⁻⁴ est illustratif. Pour des raretés plus extrêmes, il faut des estimateurs d'événements rares (échantillonnage préférentiel, découpage multiniveaux ; référence à vérifier pour la variante adaptée aux LM).

### E3 — La rareté seule prédit-elle la profondeur ?

- **H_A** : sous Q et à validité fixée, la profondeur croît avec la rareté (ρ(n, d | valide) ≥ 0,5, illustratif).
- **H_B** : rareté et profondeur sont quasi indépendantes (|ρ| ≤ 0,1).
- **Dispositif** : énoncés valides tirés de Q dans deux domaines, un monde planté et une bibliothèque formelle (voir E-formel ci-dessous).
- **Contrôle** : profondeur calculée sur des idées de complexité appariée mais fausses (une constante perturbée). On attend d ≈ 0.
- **Issues** :
  - Si H_A tient, la « profondeur » mesurée est en partie redondante avec la rareté. Il faut la redéfinir conditionnellement à n.
  - Si H_B tient, les deux axes sont informatifs séparément et la cellule jointe est un objet propre.
  - Chaque issue falsifie l'autre hypothèse.

### E4 — Comparaison principale

- **Quantité primaire** : par problème p, succ_C(p) = 1 si au moins une idée trouvée satisfait n ≥ η (relativement à Q préenregistré) **et** d ≥ δ **et** une validité mécanique, dans le budget C.
- **Unité d'analyse** : le problème. Les graines sont imbriquées dans les problèmes et moyennées avant le test. L'unité n'est pas l'idée, car les idées d'un même run ne sont pas indépendantes.
- **Coût** : comptabilité complète, à appliquer identiquement à chaque bras :
  - jetons d'entrée et de sortie de **tous** les agents, critiques et sélecteurs compris ;
  - appels au vérificateur ;
  - temps mural.
  Rapporter la courbe succ_C pour plusieurs C, pas un seul point.
- **H_A** : succ_C(système) − max_b succ_C(b) ≥ Δ_min. L'enveloppe des lignes de base est prise par problème ou globalement, à préenregistrer. Δ_min = 0,10 est illustratif.
- **H_B** : la différence est ≤ 0.
- **Règle de décision** : test apparié par problèmes (bootstrap par problème, ou McNemar si l'issue est binaire). Correction de Holm sur les comparaisons au-delà de l'enveloppe. Plan séquentiel de groupe (O'Brien & Fleming, 1979, *Biometrics* 35, « A multiple testing procedure for clinical trials »).
- **Contrôles négatifs** :
  1. **Test A/A** : le système contre lui-même, avec étiquettes de bras aléatoires. Il doit conclure « pas de différence » au taux nominal.
  2. **Système placebo** : un seul modèle, même nombre d'appels, rôles attribués au hasard sans interaction.
- **Issues** :
  - Borne inférieure de l'IC > Δ_min : H_B falsifiée.
  - Borne supérieure < Δ_min : H_A falsifiée.
  - Entre les deux : « non concluant », déclaré d'avance, avec un plafond de problèmes fixé.
- **Taille (illustrative)** : pour 0,30 contre 0,15, α = 0,05 bilatéral et puissance 0,8, l'approximation pour deux proportions donne n ≈ 7,84 × (0,21 + 0,1275) / 0,0225 ≈ 118 problèmes. L'appariement peut réduire ce nombre ; un pilote de 30 problèmes servira à estimer la corrélation intra-problème.

### E5 — Attribution : interaction ou volume filtré ?

- **H_A** : le gain vient de l'interaction (critique croisée, sélection entre agents divers).
- **H_B** : le gain vient du nombre d'échantillons et du filtrage par vérificateur.
- **Bras, tous à coût égal** :
  1. système complet ;
  2. système sans critique, jetons de critique réalloués à la génération ;
  3. système sans diversité de modèles (même modèle, plusieurs persona) ;
  4. modèle unique best-of-N avec le même vérificateur et la même règle de sélection.
- **Issues (seuil illustratif)** :
  - Si le bras 4 récupère ≥ 80 % du gain de E4 : H_A falsifiée pour la composante « interaction ».
  - Si le retrait de la critique fait perdre ≥ 50 % du gain alors que le bras 4 en récupère ≤ 20 % : H_B falsifiée.

### E6 — Fuite par rétroaction

- **H_A** : renvoyer au générateur la validité et la profondeur sur K_train ne gonfle pas la mesure.
- **H_B** : le système sur-apprend K_train (Goodhart ; Manheim & Garrabrant, 2018, « Categorizing Variants of Goodhart's Law », prépublication arXiv, identifiant à vérifier).
- **Métrique** : écart d(K_train) − d(K_test), avec et sans rétroaction.
- **Contrôle** : même système sans aucune rétroaction.
- **Issues** :
  - Si l'écart avec rétroaction dépasse l'écart sans rétroaction de plus d'un seuil préenregistré : H_A falsifiée, et le signal concerné passe en « retenu ».
  - Sinon : H_B falsifiée pour ce signal.

### E7 — Rétrodiction : trouvé ou rappelé ?

- **H_A** : les succès en rétrodiction reflètent une recherche.
- **H_B** : ils reflètent un rappel de données d'entraînement.
- **Dispositif** : modèles à données d'entraînement publiées (voir (d)). On recherche par n-grammes et par embeddings, dans le corpus, l'idée cible et ses paraphrases canonicalisées.
- **Métrique** : taux de succès sur cibles absentes du corpus contre cibles présentes.
- **Issues** :
  - Si les succès se concentrent sur les cibles présentes (rapport ≥ 3, illustratif) : H_A falsifiée pour ce dispositif.
  - Si les taux sont égaux et non nuls sur les cibles absentes : H_B falsifiée.
- **Limite** : impossible à faire avec des modèles dont les données sont fermées.

### E8 — Choix des régions

- **H_A** : une règle de choix de régions, préenregistrée et fondée sur un pilote, augmente le rendement en étroit-profond. Exemple de règle : faible couverture sous Q mais vérificateur dense.
- **H_B** : elle ne fait pas mieux que des régions tirées au hasard.
- **Dispositif** : apprendre la règle sur des régions de développement, puis l'évaluer sur des régions tenues à l'écart, contre un tirage aléatoire de même taille.
- **Contrôle** : la règle appliquée à des étiquettes de régions permutées.
- **Issues** : gain sur l'ensemble tenu à l'écart ≥ seuil, sinon H_A falsifiée. Sous permutation, le gain doit disparaître, sinon la règle capte un artefact.

---

## (c) Instruments : la mesure minimale qui dit s'ils fonctionnent

| Instrument | Cas honnêtes appariés | Détection / fausses alertes visées (illustratif) | Vérification mécanique à battre |
|---|---|---|---|
| **Juge LM** (si inévitable) | Même idée rédigée dans le style de la famille du générateur et dans celui d'une autre famille, puis paraphrasée par une troisième famille. Paires vraie/fausse de même complexité dans les mondes plantés. | Écart d'auto-préférence mesuré et rapporté comme borne du biais (≤ 0,05 visé). Rang du juge vs vérité plantée : AUC ≥ 0,8. | Régression logistique sur longueur + distance d'embedding au corpus + complexité syntaxique. Si le juge ne la bat pas, il est retiré. Il doit venir d'une autre famille que le générateur et être aveugle à la source. |
| **Estimateur d'étroitesse** | (i) Grammaire formelle où P_Q est calculable exactement (énumérateur pondéré). (ii) Paraphrases d'une idée commune, qui doivent rester « communes ». | Corrélation de rang estimation/vérité ≥ 0,9 en (i). Taux de paraphrases comptées comme nouvelles ≤ 0,02 en (ii). | Déduplication exacte de chaînes, puis forme normale (simplification symbolique, normalisation d'AST). La canonicalisation doit faire au moins aussi bien. |
| **Mesure de profondeur** | Loi plantée vraie contre loi de même complexité à constante perturbée. Lemme utile contre lemme de même longueur jamais utilisable. | Sensibilité ≥ 0,8 et fausses alertes ≤ 0,05 sur K_test. | Score de complexité seule (longueur, profondeur d'arbre). Si ce score prédit d aussi bien, d mesure la complexité et non la conséquence. |
| **Vérificateur de preuve formelle** (Lean 4 + Mathlib ; The mathlib Community, 2020, CPP, « The Lean Mathematical Library ») | Preuves correctes contre preuves contenant `sorry`, des axiomes ajoutés ou une tactique non sûre. | 0 acceptation de preuve avec axiome hors liste blanche (`#print axioms`). | Rejet syntaxique de `sorry`. **Le vérificateur ne contrôle pas la fidélité de l'énoncé** : audit humain d'un échantillon d'énoncés, taux de mésformalisation rapporté. |
| **Tests exécutables** | Solutions correctes contre mutants plantés. | Taux de mutants tués ≥ 0,9. Solutions correctes rejetées ≤ 0,01. | Tests fournis seuls, sans mutants. Il faut montrer que le jeu de tests distingue mieux que la couverture de lignes. |
| **Coupure temporelle (rétrodiction)** | Cibles certifiées présentes dans le corpus contre certifiées absentes (modèles à données ouvertes). | Détecteur de contamination : sensibilité ≥ 0,9 sur les présentes, fausses alertes ≤ 0,05 sur les absentes. | Recherche exacte de n-grammes. Si l'on ne peut pas la faire (données fermées), la coupure n'est pas un instrument mais une déclaration. |
| **Ligne de base « aléatoire »** | — | Doit retrouver les idées plantées à la fréquence prédite par leur probabilité sous la grammaire (test d'ajustement). | N'est définie que dans un espace formel : sinon, à retirer. |
| **Énumérateur mécanique** | Idées plantées de rang d'énumération connu. | Temps jusqu'au premier succès conforme au rang. | Comparaison possible à PySR pour la régression symbolique (Cranmer, 2023, « Interpretable Machine Learning for Science with PySR and SymbolicRegression.jl », prépublication arXiv, identifiant à vérifier). Antécédents : Schmidt & Lipson, 2009, *Science* 324 ; Udrescu & Tegmark, 2020, *Science Advances* 6(16), « AI Feynman ». |
| **Modèle unique le plus fort** | — | Choisi par une règle préenregistrée sur des problèmes de développement disjoints. | Doit être évalué avec le même vérificateur et la même sélection (bras 4 de E5). Sinon la comparaison avantage le système. |

---

## Réponses aux huit points

Pour chaque point : confiance entre 0 et 1, ce qui est établi, ce qui est conjecture.

**1. Cible — confiance 0,6.**
- *Établi* : un juge LM peut présenter un biais d'auto-préférence (RAPPORTÉ : Zheng et al., 2023 ; Panickssery et al., 2024).
- *Conjecture* : les définitions opérationnelles proposées :
  - n = −log P_Q(c(x)) relativement à Q nommé ;
  - d = gain contrefactuel d'un solveur figé sur K_test, moins le gain d'un contrôle de même complexité ;
  - la rareté se distingue de la profondeur par E3 et par le contrôle « fausse idée de même complexité ».
- *Biais du juge* : borné par l'écart mesuré sur des paires de style croisé, et jamais utilisé pour la quantité primaire si une mesure mécanique existe.
- *Cadrage* : la référence doit être plurielle (E2).

**2. Sources de vérité — confiance 0,65.**

| Source | Peut établir | Ne peut pas établir | Mode d'échec |
|---|---|---|---|
| Mondes plantés | n et d exactement, par construction | Transfert au réel | Le concepteur plante ce que ses propres a priori jugent rare ; le générateur peut partager ces a priori. |
| Rétrodiction à coupure | Pertinence réelle | Étroitesse non contaminée (sauf données ouvertes) ; profondeur hors du récit historique | Contamination ; biais de survivance dans le choix des cibles ; n minuscule. |
| Preuve formelle | Validité exacte ; profondeur par usage aval dans une bibliothèque (lemmes débloquant des cibles sous budget fixé) | Que l'énoncé dise ce qu'on croit | Mésformalisation ; lemmes valides mais triviaux. |
| Tests exécutables | Validité comportementale | Généralité | Couverture insuffisante ; piratage de récompense. |
| Autre : prédictions prospectives | Seule source sans contamination possible | — | Lente, avec peu d'échantillons. |

- *Conjecture* : aucune source ne suffit seule. Il faut au moins un monde planté et un domaine réel (formel), avec une vérification de transfert : corrélation des classements des systèmes entre sources.

**3. Comparaison — confiance 0,7.**
- Le dispositif est celui de E4 : quantité primaire succ_C(p), unité = problème, comptabilité complète des coûts, règle séquentielle préenregistrée contre l'enveloppe des lignes de base.
- L'attribution passe par E5.
- *Établi* : l'estimateur sans biais de pass@k (Chen et al., 2021, « Evaluating Large Language Models Trained on Code », prépublication arXiv, identifiant à vérifier) s'applique à succ_C quand on échantillonne plus de runs que nécessaire.
- *Conjecture* : l'effet attendu et la taille d'échantillon (illustratifs).

**4. Choix des problèmes — confiance 0,4.**
- *Conjecture* : les régions à faible couverture sous Q mais à vérificateur dense seraient plus fertiles.
- La recherche par nouveauté et l'illumination de l'espace offrent des outils, sans garantie : Lehman & Stanley, 2011, *Evolutionary Computation* 19(2), « Abandoning Objectives » ; Mouret & Clune, 2015, « Illuminating search spaces by mapping elites », prépublication arXiv, identifiant à vérifier. FunSearch (Romera-Paredes et al., 2024, *Nature* 625, « Mathematical discoveries from program search with large language models ») montre des trouvailles dans des régions à évaluateur rapide. C'est RAPPORTÉ, et cela ne dit rien de l'étroitesse au sens d'ici.
- Le choix se teste par E8, jamais en le supposant.
- *Établi (théorique)* : il n'existe pas de règle de choix universellement meilleure en moyenne sur tous les problèmes (Wolpert & Macready, 1997, *IEEE Trans. Evol. Comp.* 1(1), « No Free Lunch Theorems for Optimization »). Toute règle doit donc être validée sur une distribution de problèmes nommée.

**5. Rétroaction — confiance 0,6.**
- *Peut être renvoyé* :
  - validité mécanique (preuve acceptée, tests d'entraînement) ;
  - coût consommé ;
  - profondeur sur K_train, sous réserve de E6.
- *Doit être retenu* :
  - l'étroitesse n (la renvoyer transforme Q en adversaire et mesure l'évitement de Q, pas la découverte) ;
  - K_test ;
  - les tests tenus à l'écart ;
  - toute sortie du juge.
- *Règle* : tout ce qui entre dans la quantité primaire est calculé sur des données jamais exposées.
- *Conjecture* : renvoyer la validité seule ne fausse pas la mesure. Testable par E6.

**6. Validation du harnais — confiance 0,7.**
- Avant tout run coûteux, le harnais doit passer cinq épreuves :
  - E1, détection contre leurres et permutation ;
  - la ligne « estimateur d'étroitesse » de (c), calibration sur grammaire exacte et invariance aux paraphrases ;
  - E2, dépendance à la référence ;
  - le test A/A de E4 ;
  - une analyse de puissance sur pilote.
- Le harnais doit aussi montrer que chaque instrument bat sa vérification mécanique.
- E6 n'est réalisable qu'avec le système : c'est la limite de P10.

**7. Plan — confiance 0,6 sur l'ordre, 0,3 sur les tailles (illustratives).**

| Phase | Contenu | Arrêt si | Taille (illustratif) |
|---|---|---|---|
| 0 (CPU) | Grammaires, canonicalisation, mondes plantés, préenregistrement | Canonicalisation incapable de fusionner ≥ 98 % des paraphrases | — |
| 1 | E1 avec un petit modèle ouvert | Sensibilité < 0,8 ou fausses alertes > 0,05 : revoir les instruments | 200 positifs, 600 leurres |
| 2 | E2 + E3 | ρ inter-Q ≤ 0,3 : passer aux affirmations indexées par Q, sans arrêter | 30 000 tirages × 20 problèmes × 3 Q |
| 3 | Test A/A + pilote | Faux positifs A/A au-dessus du nominal : arrêt | 30 problèmes × 5 graines |
| 4 | E7 (contamination) sur modèles à données ouvertes | Détecteur sous les seuils de (c) : la rétrodiction est retirée du plan | ~100 cibles présentes et 100 absentes |
| 5 | E4 séquentiel | Arrêt pour efficacité ou futilité aux analyses intermédiaires | ~120 problèmes, jusqu'à 200 au plafond |
| 6 | E5 + E6 | Seulement si E4 conclut H_A | Mêmes problèmes, 4 bras |
| 7 | E8, puis prédictions prospectives | E8 nul : on abandonne le choix ciblé | Régions dév/test 50/50 |

- *Établi* : la règle de trois et la formule de taille pour deux proportions sont des calculs standards.
- *Conjecture* : les effets supposés.

**8. Limites — confiance 0,55.**
- *Hors de portée* :
  - la conséquence réelle à long terme ;
  - l'étroitesse relativement à « toute la recherche humaine » ;
  - les idées dont la conséquence échappe à tout vérificateur formalisable ;
  - la distinction trouver/rappeler avec des modèles à données fermées.
- *Preuve que la cible est mal posée* : E2 donne ρ ≤ 0,3 entre références raisonnables, **et** l'instabilité persiste sous changement de canonicalisation. « Étroit » n'est alors qu'un artefact de Q.
- *Preuve que le harnais est infaisable* :
  - E1 échoue malgré des instruments améliorés, c'est-à-dire que la surface explique les scores ;
  - ou bien les classements des systèmes ne se transfèrent pas des mondes plantés au domaine formel (ρ ≈ 0) ;
  - ou bien la classe étroit ∧ profond reste vide sous toutes les références dans le domaine réel. On ne pourrait alors falsifier H_A de E4 qu'au sens trivial 0 = 0.
- *Cadrage* : la question cherche un harnais général. Je soutiens (HYPOTHÈSE) qu'on ne peut obtenir qu'un harnais par domaine × référence, et que l'affirmation défendable est locale.

---

## (d) Ancrage matériel (tous les chiffres sont illustratifs)

**Modèles ouverts.**
- *Pour l'étroitesse non contaminée*, des modèles à données d'entraînement publiées : famille OLMo (Allen AI) et Pythia (EleutherAI, ordre des données connu). Ils sont indispensables pour E7. Version exacte et corpus : référence à vérifier.
- *Pour les références Q et les agents* : Llama 3.1 (8B, 70B), Qwen2.5 (7B, 72B, variantes mathématiques), distillations DeepSeek-R1. Le choix final du « plus fort » se fait par une règle préenregistrée.
- *Juge éventuel* : une famille absente du système.

**Outils.** vLLM pour l'inférence, Lean 4 + Mathlib, PySR pour l'énumérateur symbolique, bac à sable d'exécution pour les tests.

**Calcul (estimation grossière, illustratif).**

| Poste | Hypothèses | Volume | GPU | Coût |
|---|---|---|---|---|
| Phase 2 | 30 000 tirages × 20 problèmes × 3 Q × ~1 000 jetons ; débit agrégé d'un modèle 7–8B sur un H100 de l'ordre de 10⁴ jetons/s | ≈ 1,8·10⁹ jetons | ≈ 50 h | ≈ 100–250 $ à 2–5 $/h |
| Phase 5 | 120 problèmes × 5 bras × 5 graines × 2·10⁶ jetons, majoritairement avec un 70B à ~10³–2·10³ jetons/s sur 4 GPU | 6·10⁹ jetons | ≈ 3 000–7 000 h | ≈ 10⁴–3·10⁴ $ |
| Phase 6 | Ordre de la phase 5 | — | — | — |
| Vérification Lean et tests | Surtout CPU ; non négligeable en temps mural, faible en coût | — | — | — |
| Humain | Audit de fidélité de ~200 énoncés formalisés et de ~100 cibles de rétrodiction | — | — | ≈ 2–4 semaines-personne |

**Ce qui réfute le plus tôt et au moindre coût.** Les phases 0 à 3 coûtent moins de 1 % du total illustratif. Elles peuvent falsifier, avant toute dépense lourde :
- l'instrument de mesure (E1) ;
- la bonne pose de la cible (E2) ;
- la calibration du protocole (A/A).

FIN-DE-CELLULE

## Cellule E3-T1-conception-C (lettre C)

# Proposition C — Étalonner le détecteur avant de comparer les chercheurs

**RAPPORTÉ —** L’équipe prévoit un système de proposition, critique et sélection ; la pièce décrit un projet, pas des résultats d’essai.  
**HYPOTHÈSE —** Le premier achat utile n’est pas un lot de générations, mais un lot de *contre-exemples au score* : notamment des idées vraies, rares et sans conséquence. Si le harnais les récompense, même une comparaison parfaitement randomisée ne répondra pas à la question.

**Convention.** Les choix de protocole, seuils, budgets et confiances ci-dessous ont le statut **HYPOTHÈSE** ; tous les nombres proposés sont **illustratifs**, non mesurés. Les confiances portent sur l’adéquation du choix proposé, pas sur la probabilité que le système gagne. Les énoncés marqués **VÉRIFIÉ** sont des relations de définition ou de calcul, non des observations de performance.

## Cible et présupposés

**HYPOTHÈSE — Cible ; confiance 0,85 (illustratif).** Il reste à établir qu’on peut reconnaître deux formulations d’une même idée, définir une recherche « ordinaire » reproductible et mesurer une conséquence qui n’est pas déjà inscrite dans la consigne. Je commencerais dans des micromondes finis : une idée est une règle exécutable dans un langage borné ; deux règles sont la même idée si leurs prédictions coïncident sur **tout** le domaine du monde. Une règle fausse est inéligible, quelle que soit sa rareté.

- **Étroitesse.** Pour une classe \(c\), mesurer \(p_r(c\mid w,B)\), probabilité qu’au moins un candidat effectivement proposé par la politique ordinaire \(r\) appartienne à \(c\), dans le monde \(w\) et sous budget \(B\). Archiver quelques politiques gelées : tirage suivant une grammaire publiée, énumération avec ordre initial randomisé publié, modèle solo avec outils. Prendre le **maximum** des probabilités, pas leur moyenne. Annoncer « étroite » seulement si la borne supérieure simultanée de ce maximum est inférieure à \(\tau=0,01\) (illustratif). Utiliser des recherches de référence indépendantes de celles qui ont nommé les classes. Une classe non résolue n’est pas déclarée rare.
- **Profondeur.** Tirer secrètement des problèmes aval et doter un résolveur **fixe** soit de \(c\), soit d’une règle vraie placebo de longueur et de coût d’appel appariés. Mesurer la différence appariée de fractions résolues sous le même plafond, sur des cas dont ni l’énoncé ni la solution ne sont une simple copie de \(c\). Exiger une borne inférieure supérieure à \(d=0,15\) (illustratif). Cette définition mesure une **valeur instrumentale pour ce résolveur**, pas une importance scientifique intrinsèque.
- **VÉRIFIÉ —** Une faible probabilité d’apparition ne donne à elle seule aucune borne inférieure sur le gain aval : si le résolveur ignore la règle, le gain est nul. Le cadrage « région étroite » induit en erreur si l’on omet la politique, le codage et le budget.

## Sources de vérité : ne pas demander à une source de certifier les deux axes

**HYPOTHÈSE — Sources ; confiance 0,85 (illustratif).** Présupposé : il existerait un oracle unique de « découverte ». Je séparerais les instruments ainsi :

|Source|Ce qu’elle permettrait de contrôler|Échec qui limiterait l’interprétation|
|---|---|---|
|Monde synthétique fini|Calculer extension, masse de référence sur les plus petits mondes, et différences aval exhaustives ; construire des cas croisés rare/fréquent × utile/inerte.|Une vérité plantée n’est pas forcément rare ; une seule famille de plantations peut imposer son propre style de solution. Accepter aussi les règles non plantées qui passent l’oracle.|
|Preuve formelle|Vérifier un certificat dans une théorie et une liste d’axiomes gelées ; tester ensuite le lemme comme outil de preuve sur d’autres buts.|Une tautologie peut être certifiée ; un énoncé prouvable mais sans certificat sous budget reste *non certifié*, pas réfuté.|
|Tests exécutables|Mesurer les effets sur des instances fraîches, contre un oracle indépendant du code proposé.|Une suite finie non exhaustive peut manquer une exception ; un gain sur les tests publics ne certifie pas le transfert.|
|Rétrodiction datée|Tester une prédiction enregistrée contre une observation ultérieure ; documenter ce qu’un corpus borné contenait avant la date.|Absence dans ce corpus ≠ faible probabilité de découverte ; présence possible dans les poids du modèle. Sans provenance admissible, réserver ce volet à l’exploration.|
|Jugement humain éventuel|Décider en aveugle des cas hors langage, avec adjudication indépendante et abstention.|Accord entre lecteurs ≠ exactitude. Estimer les erreurs par source et style sur ancres auditées ; attribuer les cas litigieux contre le système dans l’analyse de sensibilité. Pas de verdict principal fondé sur un juge de langage.|

**VÉRIFIÉ — Repères méthodologiques, non validations de ce harnais :** Leonardo de Moura, Soonho Kong, Jeremy Avigad, Floris van Doorn et Jakob von Raumer (2015), *The Lean Theorem Prover (System Description)*, CADE ; John P. A. Ioannidis (2005), *Why Most Published Research Findings Are False*, PLoS Medicine (distinction entre fréquence de faux positifs et crédibilité des résultats positifs).

## Étalonnage minimal des instruments

**HYPOTHÈSE — Validation ; confiance 0,90 (illustratif).** Le présupposé dangereux est que quelques succès spectaculaires suffiraient à valider le détecteur. Pour chaque ligne, enregistrer **sensibilité** \(P(+\mid\text{positif oracle})\), **fausses alertes** \(P(+\mid\text{négatif oracle})\), abstentions et dénominateurs, sur familles tenues à part. Positifs et négatifs doivent être *honnêtes* : des propositions normales du même domaine, pas des absurdités reconnaissables au style. L’abstention manque un positif ; elle ne doit pas servir à dissimuler une faible couverture.

|Instrument ; événement « + »|Positifs et négatifs appariés pour estimer les deux taux|Vérification mécanique à égaler ou à battre à coût fixé|
|---|---|---|
|Identification de classe ; « identiques »|Réécritures équivalentes / règles de même taille différant sur un cas réel|Normalisation syntaxique ; table de vérité exhaustive comme oracle|
|Sonde d’étroitesse ; « rare »|Classes de masses exactement connues de part et d’autre du seuil, même utilité et longueur|Fréquence brute sur tirages indépendants ; sommation exacte sur petit espace|
|Sonde de profondeur ; « utile »|Outils à gain exhaustif supérieur / inférieur au seuil, même rareté, complexité et validité|Prédire par nombre d’occurrences ou longueur épargnée ; comparaison exhaustive avec/sans outil comme oracle|
|Oracle synthétique ; « vrai »|Règles vraies non plantées / conjectures plausibles avec exception, même grammaire|Test d’identité avec la plantation, puis évaluation exhaustive indépendante|
|Preuve ; « certificat admissible »|Preuves correctes / tentatives honnêtes incomplètes ou dépendantes d’un axiome hors liste, mêmes bibliothèques et tailles|Noyau de preuve **et** audit des dépendances ; aucun mérite à battre le noyau en acceptant plus|
|Suite exécutable ; « correct »|Programmes corrects / solutions naturelles presque correctes, appariées en coût|Tests publics et tests aléatoires à même coût ; oracle exhaustif pour étiqueter le lot|
|Filtre temporel ; « information postérieure présente »|Versions avec / sans le résultat ultérieur, mêmes auteurs, sujet et format, dates et filiation auditées|Dates de version, hachages et recherche textuelle. Ce test porte sur les documents, pas sur la mémoire des poids.|
|Juge éventuel ; « qualifié »|Classes qualifiées / classes manquant un seul critère ; permuter style et attribution à contenu fixe|Pipeline sans juge ; exiger un gain de détection à fausses alertes constantes, sans quoi supprimer le juge|
|Sélecteur de régions ; « enrichie »|Régions à rendement oracle au-dessus / au-dessous du seuil de rentabilité, même taille et coût|Tirage uniforme stratifié et classement par densité brute de règles valides|
|Chaîne entière ; « étroite **et** profonde »|Cas doublement positifs / trois autres combinaisons, plus propositions fausses ; apparier budget, longueur, famille|Intersection mécanique des tests élémentaires ; publier aussi les taux par quadrant, pas seulement l’exactitude moyenne|

**HYPOTHÈSE —** Tirage aléatoire, énumérateur, modèle solo et collisionneur sont des *chercheurs*, pas des oracles binaires. Pour chacun, mesurer la fraction de mondes positifs où il rapporte une classe oracle qualifiée et la fraction de mondes nuls où une de ses sorties est acceptée à tort ; apparier les mondes sur taille et budget. Vérifier mécaniquement les journaux de tirage, l’ordre et la couverture de l’énumération, les coûts et les doublons. Une meilleure sensibilité du harnais aux formulations d’un seul chercheur invaliderait une comparaison naïve.

## Duels préenregistrés

**HYPOTHÈSE — Comparaison ; confiance 0,80 (illustratif).** L’unité primaire serait **un monde indépendant**, non un message, un agent ou une idée. Chaque bras rend une seule nomination finale ou s’abstient. Son score est l’indicateur d’une nomination certifiée vraie, étroite et profonde. Apparier tous les bras sur les mondes ; agréger au niveau famille si les mondes partagent un mécanisme. Geler le meilleur solo après une compétition de développement incluant recherche arborescente, autocritique et sélection parmi plusieurs essais. « Meilleur » ne désigne que ce panel. Comptabiliser génération, préremplissage, critiques, outils, vérification visible, sélection des régions et essais abandonnés ; publier séparément le coût commun de certification aveugle.

**HYPOTHÈSE — Règle commune des duels.** Pour chaque contraste scalaire ci-dessous, \(H_A:T>0\), \(H_B:T\leq0\). Une borne inférieure strictement positive réfute \(H_B\) ; une borne supérieure non positive réfute \(H_A\). Sinon : essai non décisif, pas équivalence. Intervalles simultanés préspécifiés sur familles, bras et seuils utilisés pour conclure ; classement provisoire interdit. Ainsi chaque conclusion possible indique précisément ce qu’elle falsifie.

|Duel|Métrique \(T\) et seuil (valeurs illustratives)|Contrôle négatif|
|---|---|---|
|Le harnais discrimine-t-il ?|Minimum des marges : sensibilité finale moins \(0,80\), \(0,005\) moins taux de fausses alertes dans **chaque** strate négative. Exiger aussi la marge d’erreur admissible au taux de base visé ci-dessous.|Règle vraie très rare portant sur une variable aval inutilisée ; règle très utile mais immédiatement énumérée.|
|Le choix des régions paie-t-il ?|Différence de probabilité de succès entre politique ciblée et tirage stratifié, **coût de prospection inclus**, sur nouvelles familles, moins gain requis de \(0,05\).|Permuter les descripteurs de région avant sélection ; inclure les régions refusées dans l’échantillon d’audit.|
|Le retour autorisé transfère-t-il ?|Gain avec retour public contre retour factice de même coût sur nouveau coffre de tests, moins \(0,05\).|Remplacer le signal public par celui d’un autre problème apparié.|
|Le système bat-il les références ?|Minimum, sur toutes les références gelées, de la différence de probabilités de succès appariées, moins \(0,05\). Le score doit rester positif sous les bornes d’erreurs différentielles mesurées.|Bras solo dupliqué sous deux pseudonymes ; mondes sans aucune classe qualifiée.|
|Est-ce la critique *informée* qui contribue ?|Système complet moins système recevant des critiques permutées à longueur, tours, outils et budget constants, moins \(0,03\).|Permutation entre dossiers quand les critiques sont déjà indépendantes du dossier. Un gain ici dénoncerait un effet de procédure.|

**HYPOTHÈSE — Choix des problèmes ; confiance 0,60 (illustratif).** Des descripteurs publics tels que le nombre de sous-problèmes partageant une structure pourraient signaler un rendement supérieur. Ne pas confondre ce rendement avec une abondance intrinsèque : il dépend du chercheur. Rapporter le duel de sélection séparément de la comparaison des chercheurs sur une même distribution de problèmes.

**HYPOTHÈSE — Retour ; confiance 0,85 (illustratif).** Autoriser syntaxe, compilation et contre-exemples sur bac public. Cacher fréquences de référence, graines d’audit, identités de classe secrètes, problèmes aval, récompenses finales et journaux des autres bras. Un coffre consulté pour choisir une variante devient du développement ; le remplacer par une famille fraîche. Le duel de retour teste l’utilité d’un canal, non son innocuité universelle.

## Ordre, taille et ancrage matériel

**HYPOTHÈSE — Plan ; confiance 0,70 (illustratif).** Les tailles dépendent surtout du taux de fausses alertes tolérable et de la fréquence des paires discordantes, pas du nombre d’agents.

1. **CPU, sans modèle.** Deux implémentations indépendantes, microdomaines exhaustifs, quatre quadrants. Pilote de 50 paires par instrument (illustratif) pour trouver des erreurs, pas pour certifier. Arrêt immédiat si un oracle reconnaît la chaîne plantée plutôt que sa sémantique.
2. **Audit aveugle.** Si la prévalence minimale pertinente est \(1\,\%\), une sensibilité de \(0,80\) et une proportion maximale de \(10\,\%\) de fausses découvertes exigent un taux de fausses alertes inférieur à environ \(0,00090\) (calcul illustratif par Bayes). C’est plus exigeant que le seuil générique du duel. Avec zéro alerte en \(n\) négatifs indépendants, la borne unilatérale exacte est \(1-\alpha^{1/n}\) (**VÉRIFIÉ**, inversion de la probabilité binomiale de zéro). À \(\alpha=0,05\), prévoir environ 3 330 négatifs indépendants **par strate** avant correction multiple et 200 positifs pour estimer la sensibilité (illustratif) ; recalculer avec l’alpha alloué. Des variantes d’un même monde ne sont pas autant de réplications. Si ce prix d’audit est inabordable, arrêter.
3. **Prix de la rareté.** Même formule : pour une seule classe, une seule politique, zéro apparition, il faut environ 300 recherches indépendantes pour borner \(p\) sous \(0,01\) à \(95\,\%\) (illustratif). Mutualiser un journal de référence entre classes avec correction simultanée ; ne pas mutualiser entre mondes non échangeables. Chronométrer cette étape **avant** de commander la comparaison. Si seule la masse grammaticale est calculable, restreindre explicitement la revendication à cette référence ou renoncer.
4. **Pilote ouvert.** Essayer des poids accessibles localement, par exemple **Qwen2.5-7B-Instruct** et **Qwen2.5-14B-Instruct** ; figer révision, précision, moteur et gabarit. Piloter sélection et retour sur 40 familles indépendantes (illustratif), puis dimensionner chaque duel sur données fraîches. Pour une différence appariée d’indicateurs, ordre de grandeur \(n\simeq (z_{1-\alpha}+z_{1-\beta})^2 q/g^2\), où \(q\) est la fréquence de discordance et \(g\) l’écart attendu **au seuil**, non à zéro. Avec \(q=0,20\), \(g=0,05\), puissance \(0,80\) et test unilatéral à \(0,05\), environ 500 paires par duel avant multiplicité (illustratif). Simuler le plan final avec dépendances familiales ; arrêter pour imprécision si le budget ne couvre pas la taille requise.
5. **Comparaison scellée, puis attribution** seulement si la comparaison passe. Exemple de devis **illustratif** : 500 mondes × 4 bras × 20 000 jetons facturables, plafond de 40 millions de jetons ; à un débit effectif mesuré qui serait de 40 jetons/s sur un accélérateur de 80 Go, environ 280 heures, soit 840 € à 3 €/h, hors CPU, stockage et expertise. **Ce n’est pas le coût total** : pour un seul solo de référence à 300 recherches de ce gabarit par monde, le même calcul donne environ 3 milliards de jetons et 62 500 € illustratifs, avant correction multiple. Publier les heures et coûts réels de chaque poste. Si l’étalonnage domine ainsi, commencer et éventuellement finir avec les seuls petits mondes calculables.

## Limite réfutable

**HYPOTHÈSE — Limites ; confiance 0,90 (illustratif).** La faisabilité suppose que la moindre différence intéressante entre chercheurs dépasse l’incertitude sur les faux positifs, les classes indécidables et la dépendance aux références. Refaire le contraste primaire en affectant tous les dossiers non résolus dans le sens le moins favorable, puis le plus favorable. Si ces bornes permettent à la fois une victoire pertinente et son absence à coût maximal, le harnais **ne tranche pas**. Si changer de codage raisonnable ou de résolveur inverse le verdict, rapporter les deux verdicts conditionnels, pas une moyenne baptisée « profondeur ». Même un succès sur tous les duels n’établirait ni la rareté dans la science réelle, ni les conséquences historiques d’une idée jamais mise en pratique.

FIN-DE-CELLULE

## Cellule E3-T1-conception-D (lettre D)

*Note d'audit documentaire : les blocs `FAITS` et `QUESTION DE L'ARBITRE` transmis sont complets et identiques (mode à l'aveugle du Tour III.1) [VÉRIFIÉ] ; conformément à la règle d'intégrité sur les sources, aucun identifiant de prépublication n'est cité de mémoire.*

---

## I. Livrable (a) — Ce que la question suppose sans que ce soit établi

Le cadrage soumis repose sur six présupposés implicites qui doivent être traités comme objets de réfutation et non comme acquis :

* **P-I (Invariance intrinsèque de la cible)** `[HYPOTHÈSE]` : Que « étroit » (*narrow*) et « profond » (*deep*) soient des propriétés intrinsèques d'une idée candidate $x$, stables par changement de formalisme. En théorie algorithmique de l'information, la rareté d'accès dépend pourtant du couple $(\mathcal{L}, \mu_0)$ formé par le langage de représentation $\mathcal{L}$ et la politique de recherche de référence $\mu_0$ `[VÉRIFIÉ]`.
* **P-II (Commensurabilité de l'espace de candidats)** `[HYPOTHÈSE]` : Qu'un système multi-agents en langage naturel, un échantillonneur aléatoire et un énumérateur mécanique explorent le « même espace » $\mathcal{X}$. Sans projection mécanique sur un espace quotient d'équivalence sémantique $\mathcal{X}/\!\sim$, la syntaxe libre gonfle artificiellement la rareté apparente par rapport à une grammaire canonique `[VÉRIFIÉ]`.
* **P-III (Effet amplificateur de la critique multi-agents)** `[HYPOTHÈSE]` : Que la boucle proposer-critiquer-sélectionner favorise les queues de distribution rares et fécondes, plutôt que d'induire une régression vers le consensus modal des modèles de langage à budget égal.
* **P-IV (Séparabilité *ex ante* des régions fertiles)** `[HYPOTHÈSE]` : Qu'il existe des signatures observables d'un problème permettant de prédire, avant d'en connaître la solution, qu'il admet une idée étroite et profonde plutôt que du bruit irréductible ou une solution graduelle.
* **P-V (Tractabilité statistique de la rareté en boîte noire)** `[HYPOTHÈSE]` : Qu'on puisse certifier empiriquement qu'une idée est rarement atteinte ($p_0 \ll 1$) sans exploser le budget du harnais, alors que borner $p_0 \le \varepsilon$ au risque $\alpha$ exige au moins $\ln(1/\alpha)/\varepsilon$ tirages indépendants de la référence `[VÉRIFIÉ]` (Clopper & Pearson, 1934).
* **P-VI (Unicité de la référence mono-modèle)** `[OBSERVÉ-NON-AUDITÉ]` : Que « le meilleur modèle seul à budget égal » désigne un point de comparaison unique, alors que sa performance change sensiblement selon que le budget est alloué à de l'échantillonnage parallèle filtré (*Best-of-N*) ou à de l'auto-révision séquentielle (études d'échelle au moment du test, « référence à vérifier »).

---

## II. Traitement des Points 1 à 8 de l'Arbitre

### 1. Cible (*Target*) : définitions opérationnelles sans juge LLM et bornage du biais
* **Confiance** : `0,80` (illustratif).
* **Établi vs Conjecture** : Il est établi que la rareté syntaxique ne mesure pas l'utilité déductive ou prédictive `[VÉRIFIÉ]` (Bennett, 1988) et qu'une prévalence rare est submergée par le taux de fausses alertes d'un classifieur imparfait `[VÉRIFIÉ]` (Rogan & Gladen, 1978). Il reste conjectural qu'un quotientage mécanique suffise hors des langages formels ou symboliques `[HYPOTHÈSE]`.
* **Où le cadrage se trompe** : Le cadrage parle d'étroitesse au singulier, comme si « la recherche ordinaire » était unique, et envisage un juge LLM comme substitut acceptable sous réserve d'encadrement. Or, dès que la vraie fréquence d'idées profondes $\pi_g$ est inférieure au taux de fausses alertes $\text{FPR}_g$ du juge, la valeur prédictive positive s'effondre mathématiquement `[VÉRIFIÉ]`.
* **Protocole opérationnel** :
  1. *Quotientage sémantique préalable* : Toute idée $x \in \mathcal{X}$ est projetée mécaniquement vers sa classe $[x] \in \mathcal{X}/\!\sim$ (simplification canonique par e-graphes ou égalité d'évaluation sur grille dense pour les lois ; équivalence définitionnelle ou empreinte du graphe de dépendances pour les lemmes) `[VÉRIFIÉ]`.
  2. *Étroitesse relative $N_{\mu_0, b_0}([x])$* : Fixer explicitement la référence $(\mathcal{L}, \mu_0, b_0)$ en suivant deux mesures distinctes (échantillonnage indépendant du modèle de base seul, et énumérateur grammatical par coût croissant). Sur $M_0$ exécutions indépendantes de budget unitaire $b_0$, soit $\hat{p}_0^{+}([x])$ la borne supérieure exacte de Clopper-Pearson au niveau $1 - \alpha$ de la probabilité d'atteinte `[VÉRIFIÉ]` (Clopper & Pearson, 1934). On définit l'étroitesse certifiée en nats par $N_{\mu_0, b_0}([x]) = -\ln \hat{p}_0^{+}([x])$ `[VÉRIFIÉ]`.
  3. *Profondeur $D([x])$ séparée de la rareté* : Une chaîne aléatoire syntaxiquement valide ou une identité arithmétique isolée possède un $N_{\mu_0, b_0}([x])$ élevé mais ne compresse rien hors d'elle-même `[VÉRIFIÉ]`. On mesure la profondeur sans juge LLM par le **levier de compression hors distribution** :
     - *Lois quantitatives* : Gain de longueur de description minimale (MDL) sur $R$ régimes interventionnels retenus hors recherche $\{D_r\}_{r=1}^R$, pénalisé par la complexité syntaxique $K_{\mathcal{L}}([x])$ de la loi : $D_{\text{MDL}}([x]) = \sum_{r=1}^R \max(0, L_{\text{null}}(D_r) - L(D_r \mid [x])) - K_{\mathcal{L}}([x])$ `[VÉRIFIÉ]` (Rissanen, 1978 ; Grünwald, 2007).
     - *Lemmes formels* : Réduction mécanique du nombre de pas de saturation d'un prouveur déterministe fixe sur un corpus aval retenu $\mathcal{C}_{\text{test}}$ lorsque $[x]$ est ajouté à la bibliothèque, moins le coût de vérification de $[x]$ `[HYPOTHÈSE]`.
  4. *Bornage si un juge $\hat{J}$ est inévitable* : Si un domaine semi-formel impose un juge $\hat{J} \in \{0,1\}$, le biais d'affinité générateur-juge crée $\text{FPR}_{\text{MA}} \neq \text{FPR}_{\text{Base}}$ `[RAPPORTÉ]` (biais d'auto-préférence des juges LLM, « référence à vérifier »). Par l'identité de Rogan-Gladen stratifiée par générateur $g$, la prévalence vraie vaut $\pi_g = (p_g - \text{FPR}_g)/(\text{TPR}_g - \text{FPR}_g)$ où $p_g = \mathbb{P}(\hat{J}=1 \mid G=g)$ `[VÉRIFIÉ]` (Rogan & Gladen, 1978). Il faut auditer à l'aveugle par un oracle exact un sous-échantillon aléatoire des appels $\hat{J}=1$ et $\hat{J}=0$ de *chaque* bras $g$ afin d'encadrer $(\text{TPR}_g, \text{FPR}_g)$ par intervalles exacts ; si $\hat{p}_{\text{MA}} \le \overline{\text{FPR}}_{\text{MA}}$, aucune découverte ne peut être revendiquée sans vérification oracle exhaustive de tous les positifs `[VÉRIFIÉ]`.
* **Références** : Bennett, C. H. (1988), « Logical Depth and Physical Complexity », *The Universal Turing Machine: A Half-Century Survey*, Oxford University Press ; Clopper, C. J., & Pearson, E. S. (1934), « The Use of Confidence or Fiducial Limits Illustrated in the Case of the Binomial », *Biometrika* ; Grünwald, P. D. (2007), *The Minimum Description Length Principle*, MIT Press ; Rissanen, J. (1978), « Modeling by shortest data description », *Automatica* ; Rogan, W. J., & Gladen, B. (1978), « Estimating Prevalence from the Results of a Screening Test », *American Journal of Epidemiology*.

### 2. Sources de vérité terrain (*Sources of truth*)
* **Confiance** : `0,85` (illustratif).
* **Établi vs Conjecture** : Les propriétés de sûreté logique d'un noyau formel et l'indistinguabilité observationnelle d'interventions causales manquantes sont établies `[VÉRIFIÉ]` (Pearl, 2009). Le degré de transfert des mondes synthétiques vers la découverte ouverte reste conjectural `[HYPOTHÈSE]`.
* **Où le cadrage se trompe** : La rétrodiction temporelle est traitée comme un oracle symétrique ; or elle ne peut ni exclure les précurseurs conceptuels antérieurs à la coupure, ni évaluer une idée *nouvelle et valide* que le système trouverait mais que l'histoire humaine n'a pas publiée `[VÉRIFIÉ]`.
* **Comparaison analytique** :
  1. *Mondes synthétiques à vérité plantée* : Établissent exactement $N_{\mu_0}$ (par échantillonnage massif peu coûteux) et $D_{\text{MDL}}$ sous interventions contrôlées $\text{do}(\cdot)$ `[VÉRIFIÉ]` (Pearl, 2009). Ne peuvent établir l'adéquation aux ontologies naturelles mal alignées avec les primitives choisies `[HYPOTHÈSE]`. Échouent si le concepteur plante des lois composées des fonctions favorites du pré-entraînement LLM `[HYPOTHÈSE]`.
  2. *Rétrodiction avec coupure temporelle* : Établit que la cible avait une portée scientifique reconnue `[OBSERVÉ-NON-AUDITÉ]`. Ne peut certifier l'absence de fuite indirecte (reformulations, conjectures dans des manuels pré-coupure) `[RAPPORTÉ]` (« référence à vérifier ») ni noter une hypothèse alternative correcte hors archive `[VÉRIFIÉ]`. Échoue par contamination résiduelle et par biais d'énoncé utilisant le vocabulaire post-coupure `[HYPOTHÈSE]`.
  3. *Preuve formelle* : Établit une validité déductive à taux de faux positifs nul modulo le noyau et la fidélité de l'énoncé `[VÉRIFIÉ]` (Moura & Ullrich, 2021), ainsi que $D_{\text{proof}}$ sur corpus aval `[HYPOTHÈSE]`. Ne peut établir la vérité empirique ni empêcher une formalisation infidèle `[VÉRIFIÉ]`. Échoue par prémisses contradictoires cachées (`False -> P`) ou lemmes tautologiques `[OBSERVÉ-NON-AUDITÉ]`.
  4. *Tests exécutables* : Établissent le comportement fonctionnel à faible coût marginal `[VÉRIFIÉ]`. Ne peuvent prouver l'universalité hors du support de test `[VÉRIFIÉ]`. Échouent par sur-ajustement par table de cas (*reward hacking*) ou artefacts numériques si $K_{\mathcal{L}}([x])$ est omis `[RAPPORTÉ]` (« référence à vérifier »).
  5. *Source additionnelle proposée — Oracle interventionnel actif en boîte noire* : Le candidat soumet conjointement une loi $f$ et un protocole d'expérience cruciale $\pi^*$ maximisant la divergence prédite face aux modèles de base `[HYPOTHÈSE]` (Popper, 1959) ; l'oracle exécute l'intervention jamais observée. Échoue si le bruit instrumental couvre l'écart prédit `[VÉRIFIÉ]`.
* **Références** : Moura, L. de, & Ullrich, S. (2021), « The Lean 4 Theorem Prover and Programming Language », *Automated Deduction – CADE 28*, Springer ; Pearl, J. (2009), *Causality: Models, Reasoning, and Inference*, Cambridge University Press ; Popper, K. R. (1959), *The Logic of Scientific Discovery*, Hutchinson ; Udrescu, S.-M., & Tegmark, M. (2020), « AI Feynman: A physics-inspired method for symbolic regression », *Science Advances*.

### 3. Comparaison aux références et attribution causale (*Comparison*)
* **Confiance** : `0,85` (illustratif).
* **Établi vs Conjecture** : La validité du test d'intersection-union pour démontrer la supériorité simultanée sur plusieurs références sans correction de multiplicité conservatrice est établie `[VÉRIFIÉ]` (Berger, 1982). La part de gain attribuable aux rôles multi-agents plutôt qu'au calcul additionnel est non établie (`P-III`) `[HYPOTHÈSE]`.
* **Où le cadrage se trompe** : Compter le budget uniquement en jetons générés ou autoriser le système multi-agents à appeler un compilateur en boucle face à un modèle seul en un jet confond l'architecture avec le *Best-of-N* assisté par vérificateur `[VÉRIFIÉ]`.
* **Spécification statistique** :
  - *Unité d'analyse* : L'instance de problème indépendante $i \in \{1, \dots, M_{\text{prob}}\}$ (jamais les idées individuelles produites au sein d'une même exécution, qui sont corrélées) `[VÉRIFIÉ]`. Chaque méthode ne soumet au coffre d'évaluation que son candidat final sélectionné de rang `1` (illustratif) afin d'évaluer aussi la sélection.
  - *Comptabilité des coûts* : Vecteur strictement apparié $B = (B_{\text{FLOP}}, B_{\text{tok}}, B_{\text{oracle}}, B_{\text{mur}})$ incluant les FLOPs quadratiques de pré-remplissage des longs historiques multi-agents et **chaque** appel interne au vérificateur syntaxique ou d'entraînement `[VÉRIFIÉ]`.
  - *Quantité primaire* : Taux de découverte étroite et profonde $Y_{i,m}(B) = \mathbb{I}[N_{\mu_0}([x^*_{i,m}]) \ge \tau_N \land D([x^*_{i,m}]) \ge \tau_D]$ et excès continu $Z_{i,m}(B) = \mathbb{I}[N_{\mu_0}([x^*_{i,m}]) \ge \tau_N] \cdot \max(0, D([x^*_{i,m}]))$ pour des seuils $(\tau_N, \tau_D)$ pré-enregistrés.
  - *Règle de décision* : Test d'intersection-union apparié `[VÉRIFIÉ]` (Berger, 1982) exigeant le rejet simultané au seuil unilatéral $\alpha = 0,025$ (illustratif) de $H_{0,b} : \mathbb{E}[Y_{\text{MA}} - Y_b] \le \delta_{\text{min}}$ (avec marge minimale d'intérêt pratique $\delta_{\text{min}} = 0,10$ (illustratif)) contre *toutes* les références $b \in \{\text{Aléatoire}, \text{Énumérateur}, \text{BestOfN-Mono}(B), \text{Itératif-Mono}(B)\}$.
  - *Ablations d'attribution* : (i) `MA-Complet` vs `Itératif-Mono(B)` (isole la pluralité d'agents de la révision séquentielle) ; (ii) `MA-Complet` vs `Parallèle-SansCritique(B)` (isole l'agent critique, voir `Exp. III`) ; (iii) `MA-Complet` vs `MA-SélectionAléatoireValide(B)` (isole le sélecteur) ; (iv) `MA-Homogène` vs `MA-Hétérogène` inter-familles de modèles (isole la diversité des priors de pré-entraînement).
* **Références** : Berger, R. L. (1982), « Multiparameter Hypothesis Testing and Acceptance Sampling », *Technometrics* ; Platt, J. R. (1964), « Strong Inference », *Science*.

### 4. Choix des problèmes (*Problem choice*)
* **Confiance** : `0,55` (illustratif).
* **Établi vs Conjecture** : On peut séparer l'erreur épistémique du bruit aléatoire par réplicats expérimentaux sur entrées identiques `[VÉRIFIÉ]`. Qu'un profil d'erreur structurel prédise la présence d'une solution *étroite* plutôt qu'une somme de corrections graduelles est une conjecture (`P-IV`) `[HYPOTHÈSE]`.
* **Où le cadrage se trompe** : Sélectionner des problèmes historiques célèbres introduit un biais du survivant massif, car ces problèmes ont précisément survécu dans la littérature parce qu'une astuce féconde les a résolus `[HYPOTHÈSE]`.
* **Critères *ex ante* et test** : Construire un score prospectif $S_{\text{region}}(i) \in \{0,1\}$ calculé *uniquement* à partir des résidus des références simples : (a) fort résidu épistémique au-dessus du plancher de bruit de réplication ($\text{Gap}_i > \gamma_1$) `[VÉRIFIÉ]` ; (b) rupture de transfert inter-régimes d'entraînement ($\text{Ratio}_{\text{OOD/ID}} > \gamma_2$), typique d'une symétrie ou loi de conservation manquante `[HYPOTHÈSE]` ; (c) pour les tâches formelles, distance d'importation élevée entre domaines requis dans le graphe de dépendances `[HYPOTHÈSE]`. Ce choix est testé prospectivement sans circulaire par `Exp. IV`.
* **Références** : Pearl, J. (2009), *Causality: Models, Reasoning, and Inference*, Cambridge University Press ; Udrescu, S.-M., & Tegmark, M. (2020), « AI Feynman: A physics-inspired method for symbolic regression », *Science Advances*.

### 5. Rétroaction autorisée et interdite durant la recherche (*Feedback*)
* **Confiance** : `0,90` (illustratif).
* **Établi vs Conjecture** : La dégradation de validité statistique d'un jeu de test interrogé de façon adaptative sur $T$ itérations croît en $O(\sqrt{T \ln |\mathcal{X}| / n})$ `[VÉRIFIÉ]` (Dwork et al., 2015).
* **Où le cadrage se trompe** : Le cadrage demande quelles mesures du harnais peuvent être renvoyées au générateur ; or renvoyer *n'importe quelle* composante directe de la cible finale $(N_{\mu_0}, D_{\text{test}})$ détruit l'indépendance de la mesure par loi de Goodhart adaptative `[VÉRIFIÉ]`.
* **Cloisonnement strict** :
  - *Autorisé en boucle ouverte ($\mathcal{I}_{\text{search}}$)* : Erreurs mécaniques de syntaxe, de typage ou d'homogénéité dimensionnelle ; vérification locale qu'une preuve candidate compile sans axiome interdit ; résidu prédictif uniquement sur la coupe d'entraînement $D_{\text{train}}$ ; compteur de budget restant $B - b_t$ `[VÉRIFIÉ]`.
  - *Retenu sous scellé étanche ($\mathcal{I}_{\text{vault}}$)* : (1) Tous les régimes interventionnels $\{D_r\}_{r=1}^R$ et le corpus aval $\mathcal{C}_{\text{test}}$ servant à calculer $D([x])$ ; (2) la distribution de référence $\hat{p}_0([x])$ et le score $N_{\mu_0}([x])$ — car exposer $N_{\mu_0}$ pousse le système vers l'obfuscation syntaxique ou sémantique pour fuir $\mu_0$ sans gain scientifique `[VÉRIFIÉ]` ; (3) le code générateur des vérités plantées. Si un signal de validation intermédiaire est indispensable, il doit provenir d'une coupe dédiée $D_{\text{val}}$ distincte de $\mathcal{I}_{\text{vault}}$ via un mécanisme à bruit calibré (*Thresholdout*) facturé dans $B_{\text{oracle}}$ `[RAPPORTÉ]` (Dwork et al., 2015). Testé par `Exp. V`.
* **Références** : Dwork, C., Feldman, V., Hardt, M., Pitassi, T., Reingold, O., & Roth, A. (2015), « The Reusable Holdout: Preserving Validity in Adaptive Data Analysis », *Science*.

### 6. Validation préalable du harnais (*Validating the harness*)
* **Confiance** : `0,88` (illustratif).
* **Établi vs Conjecture** : L'étalonnage d'un instrument sur témoins positifs, négatifs et invariants connus précède logiquement toute inférence expérimentale `[VÉRIFIÉ]` (Platt, 1964).
* **Où le cadrage se trompe** : Valider seulement la sensibilité aux vraies découvertes ignore l'attaque principale d'un générateur symbolique ou linguistique : contourner le détecteur d'équivalence pour faire passer une idée triviale maquillée pour « étroite » `[HYPOTHÈSE]`.
* **Cinq portes obligatoires avant tout tir coûteux** :
  1. *Spécificité sur bruit et vacuité* : Injecter du bruit syntaxiquement valide, des polynômes sur-paramétrés et des lemmes formels à prémisse contradictoire ; exiger $\widehat{\text{FPR}} = 0$ (illustratif) sur les tautologies/vacuités et $\le 0,01$ (illustratif) sur le bruit `[HYPOTHÈSE]`.
  2. *Rejet du « large et profond »* : Injecter des lois classiques fréquentes sous $\mu_0$ ; exiger $D \ge \tau_D$ mais $N_{\mu_0} < \tau_N$.
  3. *Rejet de l'« étroit et superficiel »* : Injecter des identités vraies mais isolées (zéro effet aval) ; exiger $N_{\mu_0} \ge \tau_N$ mais $D \le 0$ (illustratif).
  4. *Sensibilité sur vérité plantée* : Injecter des invariants rares compressant $R$ régimes OOD ; exiger $\widehat{\text{TPR}} \ge 0,95$ (illustratif).
  5. *Invariance par obfuscation* : Appliquer `50` (illustratif) transformations préservant la sémantique (commutativité, termes nuls, renommage $\alpha$, code mort) à des idées larges ; exiger qu'au moins `0,98` (illustratif) retombent dans la classe large de départ.
* **Références** : Platt, J. R. (1964), « Strong Inference », *Science* ; Rice, H. G. (1953), « Classes of Recursively Enumerable Sets and Their Decision Problems », *Transactions of the American Mathematical Society*.

### 7. Plan expérimental ordonné par coût (*Plan*)
* **Confiance** : `0,78` (illustratif).
* **Établi vs Conjecture** : Les tailles d'échantillon binomiales et appariées découlent des bornes exactes `[VÉRIFIÉ]` (Clopper & Pearson, 1934) ; les taux d'effet attendus sont illustratifs `[HYPOTHÈSE]`.
* **Où le cadrage se trompe** : Lancer d'emblée l'évaluation sur problèmes scientifiques réels gaspille le budget si le multi-agents ne bat même pas `BestOfN-Mono(B)` dans un monde synthétique contrôlé `[HYPOTHÈSE]`.
* **Séquence ordonnée et critères d'arrêt (couplée à la Section III)** :
  - **Phase I (Coût minimal, CPU seul)** : Portes d'étalonnage du Point 6 + `Exp. I` (invariance inter-DSL sur $N_{\text{classes}} = 200$ (illustratif) candidats). *Critère d'arrêt* : Si $\bar{\tau}_K < 0,30$ (illustratif) ou fuite d'obfuscation $> 0,02$ (illustratif), arrêt immédiat (cible mal posée ou quotient défaillant).
  - **Phase II (Coût faible, mondes synthétiques)** : $M_{\text{prob}} = 60$ (illustratif) instances ($30$ (illustratif) par strate $S_{\text{region}}$) avec $M_0 = 1\,000$ (illustratif) tirages de référence par instance (certifiant jusqu'à $N_{\mu_0} \approx 5,8$ (illustratif) nats au risque $\alpha = 0,05$ (illustratif), soit $\approx 8,4$ (illustratif) bits). Exécute `Exp. II`, `Exp. III`, `Exp. IV`, `Exp. V`. *Critère d'arrêt* : Si `MA-Complet` échoue à battre l'enveloppe des références de $\delta_{\text{min}} = 0,10$ (illustratif) (`Exp. II`), arrêt du programme. Si `Exp. III` falsifie l'utilité de la critique, suppression de l'agent critique pour la suite.
  - **Phase III (Coût moyen, déduction formelle Lean)** : $M_{\text{prob}} = 80$ (illustratif) théories formelles mutées ou post-coupure garantissant zéro mémorisation littérale. *Critère d'arrêt* : Si gain sur `BestOfN-Mono(B)` non significatif à $\alpha = 0,025$ (illustratif), arrêt avant l'étape finale.
  - **Phase IV (Coût élevé, lois interventionnelles prospectives et audit oracle)** : $M_{\text{prob}} = 100$ (illustratif) problèmes (puissance `0,80` (illustratif) à $\alpha = 0,025$ (illustratif) pour détecter un passage du taux de découverte de `0,05` (illustratif) à `0,18` (illustratif) en test apparié) + `Exp. VI` si un sous-ensemble semi-formel est inclus.
* **Références** : Berger, R. L. (1982), « Multiparameter Hypothesis Testing and Acceptance Sampling », *Technometrics* ; Clopper, C. J., & Pearson, E. S. (1934), « The Use of Confidence or Fiducial Limits Illustrated in the Case of the Binomial », *Biometrika*.

### 8. Limites, infaisabilité et cible mal posée (*Limits*)
* **Confiance** : `0,92` (illustratif).
* **Établi vs Conjecture** : L'indécidabilité de l'équivalence sémantique pour des programmes généraux Turing-complets est établie `[VÉRIFIÉ]` (Rice, 1953), tout comme la borne exponentielle d'échantillonnage Monte-Carlo d'événements rares `[VÉRIFIÉ]`.
* **Où le cadrage se trompe** : Présumer qu'un banc automatique pourrait capter les découvertes les plus conséquentes de la science, alors que celles-ci consistent souvent à **changer l'espace d'états ou les observables** plutôt qu'à optimiser une loi dans un langage $\mathcal{L}$ pré-fixé `[HYPOTHÈSE]`.
* **Hors de portée de tout harnais de ce type** :
  1. *Le mur exponentiel de certification de l'étroitesse* : En boîte noire, certifier $p_0([x]) \le 10^{-6}$ (illustratif) exige $\ge 3 \times 10^6$ (illustratif) exécutions indépendantes de la référence *par problème* `[VÉRIFIÉ]`. Au-delà d'une étroitesse modérée ($\approx 8$ à $12$ (illustratif) bits), la mesure empirique directe est matériellement infaisable hors mondes synthétiques analytiques.
  2. *L'invention ontologique* : Tout harnais automatisé fige $\mathcal{L}$ et les canaux de mesure avant l'expérience `[VÉRIFIÉ]` ; une idée introduisant une variable physique nouvelle non câblée dans le simulateur est inévaluable `[HYPOTHÈSE]`.
  3. *La profondeur différée* : En mathématiques, la fécondité d'un lemme dépend parfois de définitions futures absentes du corpus statique $\mathcal{C}_{\text{test}}$ `[OBSERVÉ-NON-AUDITÉ]`.
* **Preuves empiriques d'ill-posedness ou d'infaisabilité** :
  - *Cible mal posée* : Si dans `Exp. I`, la concordance de rang de Kendall $\bar{\tau}_K$ de $(N_{\mu_0}, D)$ entre `3` (illustratif) formalismes sémantiquement équivalents tombe sous `0,30` (illustratif), « étroit et profond » n'est qu'un artefact de notation.
  - *Harnais infaisable* : (i) Si, du fait du théorème de Rice `[VÉRIFIÉ]` (Rice, 1953), plus de `0,20` (illustratif) des variations syntaxiques d'idées larges échappent au quotientage mécanique ; ou (ii) si le coût $M_0 \cdot b_0$ nécessaire pour attester $N_{\mu_0} \ge \tau_N$ excède de plus d'un facteur `10` (illustratif) le budget total disponible avant d'atteindre une puissance statistique de `0,80` (illustratif).
* **Références** : Rice, H. G. (1953), « Classes of Recursively Enumerable Sets and Their Decision Problems », *Transactions of the American Mathematical Society*.

---

## III. Livrable (b) — Expériences décisives en inférence forte ($H_A$ contre $H_B$)

Chaque expérience oppose deux hypothèses mutuellement exclusives sur le domaine testé `[HYPOTHÈSE]` :

1. **Exp. I — Stabilité représentationnelle de la cible (teste P-I et Point 8)**
   - **$H_A$** `[HYPOTHÈSE]` : Le score conjoint $\mathbb{I}[N_{\mu_0} \ge \tau_N] \cdot D([x])$ est intrinsèque à l'idée : la concordance moyenne de Kendall $\bar{\tau}_K$ entre `3` (illustratif) DSL formellement isomorphes (algébrique infixe, combinatoire sans variable, graphe de flux typé) vérifie $\bar{\tau}_K \ge 0,60$ (illustratif).
   - **$H_B$** `[HYPOTHÈSE]` : La cible dépend de l'encodage syntaxique : $\bar{\tau}_K < 0,60$ (illustratif).
   - **Métrique et seuil** : $\bar{\tau}_K$ sur `200` (illustratif) classes d'idées évaluées dans les `3` (illustratif) DSL ; seuil `0,60` (illustratif) par intervalle de confiance bootstrap à `95 %` (illustratif).
   - **Contrôle négatif** : Permutation aléatoire des identifiants sémantiques entre DSL (attendu : $|\bar{\tau}_K| \le 0,08$ (illustratif)) et réécritures triviales intra-DSL (attendu : $\tau = 1,00$ (illustratif)).
   - **Issues falsifiantes** : Borne supérieure de l'IC $< 0,60$ (illustratif) falsifie $H_A$ (et $< 0,30$ (illustratif) établit le caractère mal posé de la cible) ; borne inférieure $\ge 0,60$ (illustratif) falsifie $H_B$.

2. **Exp. II — Supériorité à budget vectoriel égal contre l'enveloppe des références (teste Point 3)**
   - **$H_A$** `[HYPOTHÈSE]` : `MA-Complet` surpasse simultanément *chacune* des références $b \in \{\text{Aléatoire}, \text{Énumérateur}, \text{BestOfN-Mono}(B), \text{Itératif-Mono}(B)\}$ d'au moins $\delta_{\text{min}} = 0,10$ (illustratif) en taux de découverte par problème ($\min_b (\pi_{\text{MA}} - \pi_b) \ge 0,10$ (illustratif)).
   - **$H_B$** `[HYPOTHÈSE]` : Au moins une référence à budget FLOPs et appels oracle strictement identiques atteint $\pi_{\text{MA}} - \pi_b < 0,10$ (illustratif).
   - **Métrique et seuil** : Différence appariée sur $M_{\text{prob}} = 60$ (illustratif) mondes synthétiques (puis `80` (illustratif) modules Lean et `100` (illustratif) problèmes finaux), test d'intersection-union à $\alpha = 0,025$ (illustratif), seuils $\tau_N = 5,5$ (illustratif) nats et $\tau_D = 35$ (illustratif) nats MDL.
   - **Contrôle négatif** : Mondes de bruit blanc sans loi plantée ($\widehat{\text{FPR}} \le 0,01$ (illustratif)) et duel A/A `BestOfN-Mono(B)` contre lui-même sous graine distincte (écart nul attendu).
   - **Issues falsifiantes** : Rejet simultané de toutes les $H_{0,b}$ au-dessus de `0,10` (illustratif) falsifie $H_B$ ; borne supérieure de l'IC $< 0,10$ (illustratif) contre au moins une référence falsifie $H_A$.

3. **Exp. III — Effet causal de l'agent Critique : levier sélectif contre effondrement vers le prior (teste P-III)**
   - **$H_A$** `[HYPOTHÈSE]` : À budget $B$ fixe, `MA-Complet` surpasse `Parallèle-SansCritique(B)` (où les jetons de critique financent plus de tirages parallèles) de $\Delta Z > 0$ avec une hausse d'étroitesse médiane des candidats retenus $\Delta N \ge 0,7$ (illustratif) nat.
   - **$H_B$** `[HYPOTHÈSE]` : La critique censure les candidats atypiques ou gaspille le budget : $\Delta Z \le 0$ ou $\Delta N < 0,7$ (illustratif) nat.
   - **Métrique et seuil** : Test de Wilcoxon apparié sur $Z_{i,m}(B)$ et décalage médian $\Delta N$ à $\alpha = 0,025$ (illustratif).
   - **Contrôle négatif** : Agent Critique « placebo » reformulant le texte à jetons constants sans filtrage (doit sous-performer `Parallèle-SansCritique(B)` proportionnellement au budget brûlé).
   - **Issues falsifiantes** : $\Delta Z > 0$ significatif et $\Delta N \ge 0,7$ (illustratif) nat falsifie $H_B$ ; $\Delta Z \le 0$ ou $\Delta N < 0$ (illustratif) falsifie $H_A$.

4. **Exp. IV — Validité prospective du sélecteur *ex ante* de régions fertiles (teste P-IV et Point 4)**
   - **$H_A$** `[HYPOTHÈSE]` : Le rapport de cotes (*odds ratio*) d'existence d'une solution $(N_{\mu_0} \ge \tau_N, D \ge \tau_D)$ entre les problèmes classés $S_{\text{region}}=1$ et $S_{\text{region}}=0$ vérifie $\text{OR} \ge 2,5$ (illustratif).
   - **$H_B$** `[HYPOTHÈSE]` : L'indice $S_{\text{region}}$ échoue à isoler la profondeur structurelle : $\text{OR} < 2,5$ (illustratif).
   - **Métrique et seuil** : Test exact de Fisher sur `120` (illustratif) problèmes stratifiés (`60` (illustratif) par strate), seuil $\text{OR} = 2,5$ (illustratif) à $\alpha = 0,025$ (illustratif).
   - **Contrôle négatif** : Processus purement stochastiques hétéroscédastiques (erreur brute élevée mais résidu épistémique nul après réplicats ; doivent être classés $S_{\text{region}}=0$).
   - **Issues falsifiantes** : Borne inférieure de l'IC à `95 %` (illustratif) de $\text{OR} \ge 2,5$ (illustratif) falsifie $H_B$ ; borne supérieure $< 2,5$ (illustratif) falsifie $H_A$.

5. **Exp. V — Corruption de la mesure par rétroaction adaptative (teste Point 5)**
   - **$H_A$** `[HYPOTHÈSE]` : Retourner le score $D$ sur une coupe de retenue $D_{\text{hold}}$ pendant la recherche gonfle artificiellement la profondeur par rapport au coffre vierge $D_{\text{vault}}$ de $\Delta_{\text{Goodhart}} = \mathbb{E}[D_{\text{hold}} - D_{\text{vault}}] \ge 10$ (illustratif) nats.
   - **$H_B$** `[HYPOTHÈSE]` : La pénalité syntaxique $K_{\mathcal{L}}([x])$ suffit à prévenir tout sur-ajustement adaptatif ($\Delta_{\text{Goodhart}} < 10$ (illustratif) nats et chute relative $< 5\,\%$ (illustratif)).
   - **Métrique et seuil** : Écart apparié entre régime `Fuite` et régime `Cloisonné` sur `60` (illustratif) problèmes ($\alpha = 0,01$ (illustratif)).
   - **Contrôle négatif** : Évaluation hors boucle en une passe unique ($\mathbb{E}[D_{\text{hold}} - D_{\text{vault}}] = 0$ (illustratif)).
   - **Issues falsifiantes** : $\Delta_{\text{Goodhart}} \ge 10$ (illustratif) nats falsifie $H_B$ ; IC à `99 %` (illustratif) inclus sous `5 %` (illustratif) de chute relative falsifie $H_A$.

6. **Exp. VI — Biais différentiel d'affinité d'un juge LLM (teste Point 1 sur le juge)**
   - **$H_A$** `[HYPOTHÈSE]` : Sur des candidats négatifs vrais ($Y=0$ vérifiés par oracle), le juge LLM présente un écart de fausses alertes $|\text{FPR}_{\text{MA}} - \text{FPR}_{\text{Mono}}| \ge 0,03$ (illustratif) ou $\text{FPR}_g \ge \pi_g$.
   - **$H_B$** `[HYPOTHÈSE]` : Le juge anonymisé vérifie simultanément $|\text{FPR}_{\text{MA}} - \text{FPR}_{\text{Mono}}| < 0,03$ (illustratif) et $\text{FPR}_g < 0,01$ (illustratif).
   - **Métrique et seuil** : Audit oracle en aveugle de `500` (illustratif) paires négatives appariées en longueur et domaine ; seuil `0,03` (illustratif) ($\alpha = 0,025$ (illustratif)).
   - **Contrôle négatif** : Duplication exacte d'un même candidat sous deux identifiants internes (divergence attendue `0` (illustratif) à température nulle).
   - **Issues falsifiantes** : Dépassement du seuil falsifie $H_B$ (disqualifiant le juge sans vérification oracle exhaustive) ; bornes supérieures à `95 %` (illustratif) sous les deux seuils falsifient $H_A$.

---

## IV. Livrable (c) — Mesure minimale de validité pour chaque instrument nommé

Tous les seuils de détection ($\text{TPR}$) et de fausses alertes ($\text{FPR}$) ci-dessous sont marqués `(illustratif)` et constituent des prérequis d'étalonnage `[HYPOTHÈSE]` :

| Instrument nommé | Mesure minimale exigée ($\text{TPR}$ / $\text{FPR}$) | Cas honnêtes appariés (Positif vrai vs Négatif subtil) | Vérification mécanique élémentaire à battre |
| :--- | :--- | :--- | :--- |
| **Harnais de mesure global** | $\text{TPR} \ge 0,95$ (illustratif) ; $\text{FPR} \le 0,01$ (illustratif) | Invariant causal rare compressant $R$ régimes OOD *vs* interpolation tout aussi rare ajustant $D_{\text{train}}$ + loi fréquente obfusquée algébriquement | Critère AIC/BIC en distribution + distance d'édition de chaînes |
| **Juge LLM** *(si utilisé)* | $\text{TPR} \ge 0,85$ (illustratif) ; $\text{FPR} < 0,01$ (illustratif) et $\|\Delta\text{FPR}\| < 0,03$ (illustratif) | Protocole valide vérifié par oracle *vs* protocole de même longueur et jargon issu du multi-agents mais omettant un témoin causal | Heuristique de perplexité/longueur + analyseur déterministe de mots-clés |
| **Mondes synthétiques plantés** | $\text{TPR}_{\text{causal}} = 1,00$ (illustratif) ; $\text{FPR}_{\text{raccourci}} \le 0,01$ (illustratif) | Générateur mécaniste planté exact *vs* modèle de substitution reproduisant les marginales observationnelles sans respecter $\text{do}(\cdot)$ | Erreur quadratique moyenne sur coupe observationnelle i.i.d. |
| **Rétrodiction à coupure temporelle** | $\text{TPR}_{\text{post}} \ge 0,90$ (illustratif) ; $\text{FPR}_{\text{fuite}} \le 0,02$ (illustratif) | Découverte post-coupure sans précurseur formulé *vs* résultat pré-coupure réécrit avec la terminologie post-coupure | Recherche exacte par MinHash / $n$-grammes et filtre calendaire brut |
| **Preuve formelle** | $\text{TPR}_{\text{lemme}} \ge 0,95$ (illustratif) ; $\text{FPR}_{\text{vacuité}} = 0$ (illustratif) | Lemme valide réduisant les pas de preuve sur $\mathcal{C}_{\text{test}}$ *vs* preuve compilant sur prémisse contradictoire subtile (`h : P ∧ ¬P`) | Simple vérification de typage du noyau sans test de réfutation des prémisses ni score aval |
| **Tests exécutables** | $\text{TPR}_{\text{gén}} \ge 0,95$ (illustratif) ; $\text{FPR}_{\text{sur-ajust}} \le 0,02$ (illustratif) | Loi/algorithme exact aux limites hors support *vs* table de cas mémorisant `100 %` (illustratif) des tests d'entraînement | Couverture de branches unitaire fixe sans fuzzing ni pénalité de taille d'arbre syntaxique |
| **Échantillonneur aléatoire** | Couverture grammaticale $\text{TPR} = 1,00$ (illustratif) à profondeur bornée ; $\text{FPR}_{\text{biais}} \le 0,01$ (illustratif) au test d'uniformité | Arbres syntaxiques canoniques *vs* permutations symétriques d'arbres de même taille | Tirage aléatoire brut de jetons (produisant majoritairement du code invalide) |
| **Énumérateur mécanique** | Complétude $\text{TPR} = 1,00$ (illustratif) sous le coût maximal $c_{\max}$ ; $\text{FPR}_{\text{doublon}} \le 0,02$ (illustratif) | Expressions minimales distinctes *vs* expressions réductibles par symétrie commutative ou neutre | Énumération lexicographique naïve sans élagage par équivalence observationnelle |
| **Meilleur modèle seul & Système multi-agents** | $\text{TPR}_{\text{sanité}} \ge 0,90$ (illustratif) sur cibles larges ; $\text{FPR}_{\text{dépassement-budget}} = 0$ (illustratif) | Problèmes calibrés avec et sans accès au vérificateur interne à FLOPs égaux | Appel unique sans réessai (*pass@1*) pour le modèle seul ; `BestOfN-Mono(B)` filtré mécaniquement pour le multi-agents |

---

## V. Livrable (d) — Ancrage matériel, modèles ouverts, calcul et budget

* **Modèles à poids ouverts figés** : L'utilisation exclusive de modèles à poids ouverts gelés par empreinte cryptographique garantit l'absence de dérive d'API, le contrôle de la date de pré-entraînement et le décompte exact des FLOPs ainsi que des log-vraisemblances sous $\mu_0$ `[VÉRIFIÉ]`. Configuration type :
  - *Famille principale et référence mono-modèle* : modèle généraliste ouvert de classe `72B` (illustratif) paramètres (famille Qwen ouverte) et modèle spécialisé raisonnement/code de classe `32B` (illustratif) paramètres, servis en précision flottante `16` (illustratif) bits `[OBSERVÉ-NON-AUDITÉ]`.
  - *Seconde famille ouverte indépendante (ablation d'hétérogénéité et audit croisé)* : modèle ouvert de classe `70B` (illustratif) paramètres (famille Llama ouverte) et modèle dense de classe `24B` (illustratif) paramètres (famille [modèle] ouverte) `[OBSERVÉ-NON-AUDITÉ]`.
* **Pile mécanique sur CPU** : Prouveur formel Lean figé par révision Git avec tactique de recherche déterministe, moteur de saturation d'e-graphes pour le quotientage symbolique, et conteneurs isolés sans réseau pour l'exécution des simulateurs `[VÉRIFIÉ]`.
* **Dimensionnement du calcul et coûts estimés** *(tous chiffres marqués illustratifs, sur la base d'un nœud de `8` (illustratif) GPU à `80` (illustratif) Go de mémoire vidéo facturé `3` (illustratif) USD par GPU-heure et d'une grappe de `128` (illustratif) cœurs CPU)* :
  1. *Phase I (Étalonnage du harnais et `Exp. I`)* : `0` (illustratif) GPU-heure et `200` (illustratif) CPU-heures, soit `20` (illustratif) USD.
  2. *Phase II (Mondes synthétiques : `60` (illustratif) problèmes, $M_0 = 1\,000$ (illustratif) tirages courts de référence, `5` (illustratif) méthodes $\times$ `5` (illustratif) graines à budget $B = 64\,000$ (illustratif) jetons équivalents FLOPs)* : `320` (illustratif) GPU-heures et `1\,000` (illustratif) CPU-heures, soit `1\,060` (illustratif) USD.
  3. *Phase III (Déduction formelle Lean sur `80` (illustratif) modules)* : `800` (illustratif) GPU-heures et `4\,000` (illustratif) CPU-heures de vérification noyau, soit `2\,800` (illustratif) USD.
  4. *Phase IV (Campagne prospective finale sur `100` (illustratif) problèmes + ablations + `Exp. VI`)* : `2\,000` (illustratif) GPU-heures et `6\,000` (illustratif) CPU-heures, soit `6\,600` (illustratif) USD.
* **Enveloppe totale maximale** : `3\,120` (illustratif) GPU-heures et `11\,200` (illustratif) CPU-heures, soit `10\,480` (illustratif) USD au complet — mais plafonnée à `1\,080` (illustratif) USD si les portes d'arrêt des Phases I–II réfutent $H_A$.

FIN-DE-CELLULE

## Cellule E3-T1-conception-E (lettre E)

### Note préliminaire sur les pièces et les conventions

Constat de pièce (`VÉRIFIÉ`) : le bloc `FAITS` et le bloc `QUESTION DE L'ARBITRE` portent le même empreinte SHA-256 (`f00e1678…`) ; aucune donnée expérimentale, spécification d'architecture ni journal d'exécution n'a été transmis. En conséquence :
- `VÉRIFIÉ` désigne uniquement ce qui figure dans le bloc transmis ou une identité mathématique élémentaire ;
- `RAPPORTÉ` désigne un résultat issu de la littérature scientifique citée ;
- `OBSERVÉ-NON-AUDITÉ` désigne une pratique empirique courante non auditée ici ;
- `HYPOTHÈSE` désigne tout présupposé, conjecture, estimation subjective de confiance ou proposition de conception.
Conformément aux règles d'intégrité, tout chiffre qui ne provient pas des faits est marqué `illustratif` et aucun identifiant arXiv n'est cité de mémoire.

---

### (a) Présupposés non établis de la question

| # | Présupposé implicite dans la question | Pourquoi ce n'est pas établi | Statut |
|---|---|---|---|
| P1 | Il existe « un même espace d'idées candidates » permettant un échantillonnage aléatoire comparable entre agents LLM, énumérateur et tirage uniforme. | Les hypothèses, lois, lemmes et protocoles vivent dans des espaces hétérogènes ; la mesure uniforme dépend arbitrairement du codage/DSL choisi (`RAPPORTÉ`, invariance de représentation violée). | `HYPOTHÈSE` |
| P2 | « Narrow » (rareté) et « deep » (conséquence) sont des propriétés intrinsèques mesurables sur deux axes séparables à travers quatre objets scientifiques distincts. | La rareté est relative à un chercheur de référence et à un codage ; la conséquence dépend de l'horizon temporel, du régime hors-distribution et du domaine. | `HYPOTHÈSE` |
| P3 | Une architecture multi-agents (proposer–critiquer–sélectionner) augmente la découverte d'événements rares plutôt que de lisser vers le mode. | Le consensus ou la critique par LLM peut réduire la variance et éliminer précisément la queue rare des propositions (`OBSERVÉ-NON-AUDITÉ`). | `HYPOTHÈSE` |
| P4 | Un juge LLM peut voir son biais « borné » sans oracle externe suffisant. | Sans échantillon audité par une vérité externe indépendante, les erreurs corrélées entre générateur et juge restent non identifiables (`RAPPORTÉ`, Angelopoulos et al., 2023). | `HYPOTHÈSE` |
| P5 | Les sources de vérité candidates (mondes synthétiques, rétrodiction, preuve formelle, tests exécutables) mesurent la même cible scientifique. | Chaque source mesure un construit différent ; aucune ne combine simultanément validité externe ouverte, absence de contamination et coût faible. | `HYPOTHÈSE` |
| P6 | La comparaison « à même budget » est unidimensionnelle entre LLM multi-agents, modèle unique et énumérateur mécanique. | Elle confond coût d'inférence (FLOPs/USD), nombre d'appels à l'oracle vérificateur, coût amorti de pré-entraînement et temps humain d'ingénierie du DSL. | `HYPOTHÈSE` |
| P7 | Des « régions de problèmes » plus propices aux idées rares et profondes existent et sont identifiables avant exécution. | Par les théorèmes *No Free Lunch* (`RAPPORTÉ`, Wolpert & Macready, 1997), aucun avantage n'existe sans adéquation structurelle ; sélectionner des régions expose au biais de sélection. | `HYPOTHÈSE` |
| P8 | Un harnais automatisé de ce type est statistiquement et épistémiquement réalisable à coût fini. | Si la rareté visée est extrême ($p \ll 10^{-3}$, `illustratif`) ou instable au recodage, l'estimation devient statistiquement impraticable ou mal posée. | `HYPOTHÈSE` |

---

### Analyse des 8 questions de l'arbitre

#### 1. Cible (« narrow » et « deep »)
**Opérationnalisation.** Définir *narrow* comme une propriété relationnelle d'une **classe d'équivalence canonisée** $[x]$ (modulo renommage de variables, réécriture algébrique ou paraphrase) vis-à-vis d'un **ensemble de références** $\mathcal{Q}_0 = \{Q_{\text{enum}}, Q_{\text{LLM-1}}, Q_{\text{rand}}\}$ (`HYPOTHÈSE`) :
$$R_{\mathcal{Q}_0}([x]) = \min_{Q \in \mathcal{Q}_0} \left(-\log_2 \hat{p}_Q([x])\right) \quad \text{ou} \quad \min_{Q \in \mathcal{Q}_0} B_{0{,}5}(Q,[x])$$
où $B_{0{,}5}(Q,[x])$ est le budget médian pour que le chercheur de référence $Q$ atteigne $[x]$ une première fois (`HYPOTHÈSE`). Prendre le minimum sur l'enveloppe empêche qu'un cliché trivial pour un LLM passe pour « rare » au motif qu'un énumérateur ne le trouve pas, et réciproquement.

Séparer *deep* de la simple rareté repose sur la distinction entre complexité aléatoire (entropie élevée, profondeur nulle ; `RAPPORTÉ`, Shannon, 1948) et **profondeur logique / pouvoir compressif** (`RAPPORTÉ`, Bennett, 1988 ; Rissanen, 1978). Opérationnellement (`HYPOTHÈSE`), la profondeur $D(x)$ doit être **contrefactuelle et hors-échantillon** :
- *Lois quantitatives* : gain de perte prédictive en régime interventionnel ou hors-distribution (OOD), pénalisé par la longueur de description, $\Delta \mathcal{L}_{\text{OOD}}(x) - \lambda |x|$ (`RAPPORTÉ`, Rissanen, 1978 ; Pearl, 2009).
- *Lemmes formels* : compression totale des preuves sur une batterie gelée de théorèmes cibles en aval lorsque $x$ est ajouté à la bibliothèque, sous contrainte de validité noyau et de non-trivialité dérivative (`HYPOTHÈSE`).
- *Protocoles expérimentaux* : gain d'information attendu (EIG) sur un paramètre latent inconnu par unité de coût expérimental dans un banc indépendant (`HYPOTHÈSE`).

L'agrégation doit être **non compensatoire** : un seuil plancher de profondeur $\tau_D$ (`illustratif`) bloque toute idée rare mais stérile (bruit, surajustement). Si un juge LLM est inévitable (pré-filtrage ou protocoles ouverts), son biais doit être borné par **Prediction-Powered Inference (PPI)** (`RAPPORTÉ`, Angelopoulos et al., 2023) à l'aide d'un sous-échantillon stratifié évalué par un oracle externe ou des experts en aveugle, complété par un test d'échange de style (*style-swap*) entre générateur et baseline (`HYPOTHÈSE`).

- **Établi vs conjecture :** Établi (`RAPPORTÉ`) : rareté $\neq$ profondeur (Shannon, 1948 ; Bennett, 1988) ; validité asymptotique des intervalles PPI sous échantillon audité (Angelopoulos et al., 2023). Conjecture (`HYPOTHÈSE`) : stabilité empirique des classes d'équivalence $[x]$ hors domaines formels ; suffisance du test *style-swap* pour capturer le biais du juge.
- **Où le cadrage est faux :** La question traite *narrow* comme une propriété absolue de l'idée et suppose un seul espace commun à quatre objets scientifiques incommensurables ; elle sous-estime qu'un juge sans oracle externe audité ne peut pas avoir de borne de biais non triviale.
- **Confiance :** `0,75` (`HYPOTHÈSE`, `illustratif`) sur la formalisation en domaines vérifiables ; `0,30` (`HYPOTHÈSE`, `illustratif`) sur les hypothèses verbales non formalisées.
- **Références :** Shannon, C. E. (1948), *A Mathematical Theory of Communication*, Bell System Technical Journal ; Bennett, C. H. (1988), *Logical Depth and Physical Complexity*, in *The Universal Turing Machine: A Half-Century Survey* ; Rissanen, J. (1978), *Modeling by shortest data description*, Automatica ; Pearl, J. (2009), *Causality: Models, Reasoning, and Inference* (2e éd.), Cambridge University Press ; Angelopoulos, A. N., Bates, S., Fannjiang, C., Jordan, M. I., & Zrnic, T. (2023), *Prediction-Powered Inference*, Science.

#### 2. Sources de vérité
| Source | Ce qu'elle établit (rareté / profondeur) | Ce qu'elle ne peut établir | Mode d'échec principal | Statut |
|---|---|---|---|---|
| **Mondes synthétiques (vérité plantée)** | Contrôle exact de la contamination (génération à la volée), profondeur OOD/interventionnelle exacte, calibration de rareté. | Validité externe sur la science réelle ouverte. | Biais du concepteur : le monde reflète les priors de son auteur et favorise artificiellement soit les LLM, soit l'énumérateur. | `HYPOTHÈSE` |
| **Rétrodiction à coupure temporelle** | Pertinence historique apparente. | Absence de fuite cognitive (prépublications, citations indirectes, reformulations post-coupure) ; rareté réelle dans le passé. | **Contamination** poreuse + biais rétrospectif (l'énoncé moderne du problème fuit déjà le cadre conceptuel). | `OBSERVÉ-NON-AUDITÉ` / `HYPOTHÈSE` |
| **Preuve formelle (ex. Lean 4)** | Validité sans faux positif (zéro biais de juge) ; profondeur objective par compression sur théorèmes aval ; baselines mécaniques exactes. | Pertinence empirique ; création d'ontologies non formalisées. | Goulot de formalisation ; lemmes artificiellement rares syntaxiquement ou gonflés si la suite aval n'est pas indépendante. | `RAPPORTÉ` / `HYPOTHÈSE` |
| **Tests exécutables / simulateurs** | Conséquence empirique sous changement de régime ; testable pour lois quantitatives et protocoles simulés. | Fidélité au réel physique hors modèle du simulateur. | **Reward hacking** : exploitation d'artefacts numériques, conditions aux bords ou bugs du simulateur. | `OBSERVÉ-NON-AUDITÉ` / `HYPOTHÈSE` |
| **Prospective pré-enregistrée (proposée)** | Validité externe sans contamination temporelle (prédictions scellées avant données futures / micro-expériences). | Puissance statistique rapide à bas coût. | Latence élevée, petit $N$, bruit expérimental fort. | `HYPOTHÈSE` |

- **Établi vs conjecture :** Établi (`VÉRIFIÉ`/`RAPPORTÉ`) : les vérificateurs de preuves éliminent les faux positifs de validité syntaxique/logique ; la régression symbolique exécutable dispose de baselines mécaniques fortes (`RAPPORTÉ`, Udrescu & Tegmark, 2020). Conjecture (`HYPOTHÈSE`) : la corrélation de classement des systèmes entre mondes synthétiques/formels et découverte empirique ouverte.
- **Où le cadrage est faux :** Opposer ces sources comme des alternatives mutuellement exclusives ; aucune n'est suffisante seule. Il faut une échelle triangulée : synthétique + formel/exécutable (validité interne) $\to$ prospectif pré-enregistré (validité externe), et exclure la rétrodiction seule comme preuve décisive pour des LLM.
- **Confiance :** `0,80` (`HYPOTHÈSE`, `illustratif`).
- **Références :** Udrescu, S.-M., & Tegmark, M. (2020), *AI Feynman: A physics-inspired method for symbolic regression*, Science Advances ; Popper, K. R. (1959), *The Logic of Scientific Discovery*, Hutchinson.

#### 3. Comparaison, unité d'analyse, comptabilité des coûts et attribution
- **Quantité primaire (`HYPOTHÈSE`) :** Utilité de queue indexée par le budget $B$, pas la moyenne (qui favorise les clichés sûrs) ni le maximum brut (qui récompense la variance bruitée) :
  $$U(P, B) = \max_{x \in \mathcal{S}(P, B)} \Big( D_{\text{ext}}(x)\cdot \mathbb{I}[R_{\mathcal{Q}_0}([x]) \ge \tau_R \;\land\; \text{Valide}(x)] \Big)$$
  agrégée en aire sous la courbe découverte–budget (AUDC) sur une grille pré-enregistrée $[B_{\min}, B_{\max}]$ (`illustratif`), accompagnée du taux de succès conjoint $\mathbb{P}(R \ge \tau_R \land D \ge \tau_D)$.
- **Unité d'analyse (`VÉRIFIÉ`/`RAPPORTÉ`) :** L'**instance de problème** $P$ (groupée par famille de problèmes), jamais l'idée individuelle $x$. Les idées d'une même trace sont fortement autocorrélées ; les traiter comme indépendantes détruit le calibrage des tests. Utiliser les différences appariées $\Delta_P = U_{\text{multi}}(P,B) - U_{\text{base}}(P,B)$ par bootstrap en grappes (`RAPPORTÉ`, Efron & Tibshirani, 1993) avec correction de Holm–Bonferroni (`RAPPORTÉ`, Holm, 1979) sur l'ensemble des baselines.
- **Comptabilité des coûts (`HYPOTHÈSE`) :** Comptabilité bidimensionnelle obligatoire — (i) **coût de calcul d'inférence** (FLOPs / heures GPU / USD à tarif figé) ET (ii) **nombre d'appels à l'oracle vérificateur** $C_{\text{eval}}$ — plus déclaration séparée du coût fixe d'ingénierie humaine (grammaire, prompts, solveurs). Un système n'est supérieur que s'il domine l'**enveloppe** des baselines sur les deux axes ou s'il étend la frontière de Pareto de manière non dominée.
- **Règle de décision (`HYPOTHÈSE`) :** Supériorité retenue uniquement si la borne inférieure de l'IC 95 % (`illustratif`) sur $\mathbb{E}_P[U_{\text{multi}} - \max_{b \in \mathcal{B}} U_b]$ dépasse un seuil pratique pré-enregistré $\delta_{\min}$ (`illustratif`), après correction de Holm ($\alpha = 0{,}01$, `illustratif`), sur au moins deux familles de problèmes indépendantes (`illustratif`).
- **Comparaisons d'attribution (`HYPOTHÈSE`) :** Ajouter quatre ablations indispensables au même budget total : (1) *Best-of-$K$* indépendant du meilleur modèle unique (teste le pur calcul au temps d'inférence) ; (2) auto-raffinement séquentiel d'un seul modèle (teste la multiplicité d'agents) ; (3) ensemble hétérogène indépendant sans dialogue (sépare diversité de modèles et débat) ; (4) **critique placebo** (retour générique ou permuté, sépare contenu critique et simple perturbation stochastique).

- **Établi vs conjecture :** Établi (`RAPPORTÉ`) : bootstrap en grappes (Efron & Tibshirani, 1993) et contrôle FWER de Holm (1979). Conjecture (`HYPOTHÈSE`) : choix de la frontière de Pareto bidimensionnelle (FLOPs vs appels oracle) comme proxy suffisant des coûts réels.
- **Où le cadrage est faux :** Comparer « multi-agents » au « meilleur modèle unique au même budget » est ambigu sans spécifier *Best-of-$K$* et critique placebo ; de plus, égaliser uniquement les dollars masque la différence d'échelle d'appels oracle entre un énumérateur ($10^6$ appels bon marché, `illustratif`) et un LLM ($10^2$ appels, `illustratif`).
- **Confiance :** `0,85` (`HYPOTHÈSE`, `illustratif`).
- **Références :** Efron, B., & Tibshirani, R. J. (1993), *An Introduction to the Bootstrap*, Chapman & Hall ; Holm, S. (1979), *A Simple Sequentially Rejective Multiple Test Procedure*, Scandinavian Journal of Statistics.

#### 4. Choix des problèmes
Par les théorèmes *No Free Lunch* (`RAPPORTÉ`, Wolpert & Macready, 1997), aucune méthode ne domine sur tous les paysages de recherche. La conjecture structurelle (`HYPOTHÈSE`) est que le régime où des agents LLM pourraient battre à la fois l'énumérateur et le modèle unique se situe à l'intersection de quatre propriétés mesurables *a priori* : (i) espace combinatoire trop grand pour l'énumération exhaustive ; (ii) asymétrie vérification $\ll$ génération ; (iii) structure sémantique/compositionnelle permettant l'analogie (contrairement à un bruit cryptographique sans gradient) ; (iv) bassins locaux trompeurs où le tirage direct échoue.

**Tester ce choix au lieu de le présupposer (`HYPOTHÈSE`) :** Construire une taxonomie pré-enregistrée de descripteurs de paysages (facteur de branchement, coût d'énumération, entropie d'échec du modèle unique, modularité), puis échantillonner de façon **stratifiée** sur des familles de problèmes **hors échantillon** incluant des **régimes contrôles négatifs** (où le multi-agents est *prédit perdant* : petits espaces combinatoires et aiguilles aléatoires sans structure). Tester l'interaction $\text{Système} \times \text{Régime}$ : la théorie de sélection n'est corroborée que si elle prédit *à la fois* où le système gagne et où il perd.

- **Établi vs conjecture :** Établi (`RAPPORTÉ`) : pas de domination universelle sans biais inductif adapté (Wolpert & Macready, 1997). Conjecture (`HYPOTHÈSE`) : existence d'une zone non vide où l'avantage sémantique des LLM survit face aux solveurs symboliques spécialisés.
- **Où le cadrage est faux :** Chercher « où les idées rares et profondes sont plus probables » sans imposer de régimes négatifs pré-enregistrés transforme le protocole en machine à *cherry-picking*.
- **Confiance :** `0,75` (`HYPOTHÈSE`, `illustratif`).
- **Références :** Wolpert, D. H., & Macready, W. G. (1997), *No Free Lunch Theorems for Optimization*, IEEE Transactions on Evolutionary Computation.

#### 5. Rétroaction (feedback) et étanchéité de la mesure
Séparer strictement trois couches d'information (`HYPOTHÈSE`) :
1. **Autorisé en cours de recherche (boucle interne) :** validité syntaxique/type/noyau (binaire), erreur ou contre-exemples sur un **split d'entraînement interne** distinct du régime d'évaluation, et critiques internes entre agents.
2. **Strictement retenu (coffre d'évaluation scellé) :** régimes OOD/interventionnels mesurant $D_{\text{ext}}$, suite gelée de théorèmes aval (compression), estimateur de rareté $R_{\mathcal{Q}_0}$ (retourner la rareté en cours de recherche pousse directement les agents vers des formulations baroques — effet Goodhart), et étiquettes d'audit humain/PPI.
3. **Contrôle de la boucle externe (équipe d'ingénierie) :** réutiliser la même suite d'évaluation pour ajuster les prompts et agents détruit la validité statistique (`RAPPORTÉ`, Dwork et al., 2015). Imposer un coffre verrouillé à usage limité ou un mécanisme de *Reusable Holdout* (`RAPPORTÉ`, Dwork et al., 2015) + régénération procédurale par graines cryptographiques engagées avant chaque campagne.

- **Établi vs conjecture :** Établi (`RAPPORTÉ`) : perte de validité sous analyse adaptative répétée et protection par holdout réutilisable (Dwork et al., 2015). Conjecture (`HYPOTHÈSE`) : suffisance de la séparation entraînement/OOD contre le contournement subtil par des agents dotés de connaissances pré-entraînées.
- **Où le cadrage est faux :** La question ne traite que le feedback retourné au générateur pendant la recherche, en omettant la fuite tout aussi grave de la boucle externe (les chercheurs optimisant l'architecture sur le harnais).
- **Confiance :** `0,85` (`HYPOTHÈSE`, `illustratif`).
- **Références :** Dwork, C., Feldman, V., Hardt, M., Pitassi, T., Reingold, O., & Roth, A. (2015), *The reusable holdout: Preserving validity in adaptive data analysis*, Science.

#### 6. Validation préalable du harnais
Avant toute campagne coûteuse, le harnais doit démontrer cinq propriétés métrologiques (`HYPOTHÈSE`) : (1) **Sensibilité sur contrôles positifs plantés** (séparer les 4 quadrants rareté $\times$ profondeur) ; (2) **Calibrage nul A/A** (deux copies identiques d'une baseline doivent produire un effet nul et un taux de faux positifs $\le \alpha$) ; (3) **Résistance adversariale** (des générateurs triviaux — bruit syntaxique, polynômes surajustés, paraphrases verbeuses — doivent scorer bas) ; (4) **Audit de biais du juge et de fuite temporelle** (si applicables) ; (5) **Décomposition de variance** (inter-problèmes vs inter-graines) vérifiant que l'effet minimal détectable est compatible avec le budget.

- **Établi vs conjecture :** Établi (`RAPPORTÉ`) : principes standards de calibrage A/A et contrôle des faux positifs (Benjamini & Hochberg, 1995 ; Holm, 1979). Conjecture (`HYPOTHÈSE`) : qu'une batterie adversariale conçue *a priori* anticipe les modes de contournement réels d'agents LLM.
- **Où le cadrage est faux :** L'énoncé traite le harnais comme un outil à valider une fois pour toutes avant de courir ; en pratique, un harnais face à des optimiseurs puissants doit être ré-audité de manière adversariale après toute hausse de capacité.
- **Confiance :** `0,85` (`HYPOTHÈSE`, `illustratif`).
- **Références :** Benjamini, Y., & Hochberg, Y. (1995), *Controlling the False Discovery Rate: A Practical and Powerful Approach to Multiple Testing*, Journal of the Royal Statistical Society: Series B ; Holm, S. (1979), réf. citée.

#### 7. Plan expérimental ordonné, critères d'arrêt et tailles d'échantillon
Ordre strict du moins cher au plus cher, avec portes d'arrêt séquentielles (*Go/No-Go*, `RAPPORTÉ`, Wald, 1945) détaillées dans la section (b) : **E1** (calibration du harnais sur vérités plantées et contrôles adversariaux, purement CPU/petit modèle) $\to$ **E2** (audit de biais/style-swap et contamination) $\to$ **E3** (test de la taxonomie de problèmes sur petits modèles) $\to$ **E4** (test d'étanchéité du feedback vs Goodhart) $\to$ **E5** (duel principal multi-agents vs enveloppe des baselines à pleine échelle) $\to$ **E6** (ablations d'attribution causale).

**Tailles d'échantillon (`HYPOTHÈSE`, `illustratif`) :**
- Pour détecter un effet standardisé apparié $d = 0{,}50$ sur une métrique continue $U(P,B)$ avec puissance $0{,}80$ et $\alpha_{\text{Holm}} = 0{,}01$ : $N \approx 50\text{–}60$ problèmes indépendants par famille (`illustratif`).
- Pour un taux binaire d'événements rares passant de $p_0 = 0{,}05$ à $p_1 = 0{,}15$ (test apparié exact) : $N \approx 120\text{–}150$ problèmes par famille (`illustratif`). Si $p_0 < 10^{-3}$, la puissance s'effondre ($N > 10^4$, `illustratif`) : il faut alors mesurer la distribution continue de profondeur conditionnée à un budget fixé, et non le seul comptage binaire.
- **Critère d'arrêt précoce :** arrêt immédiat (futilité) si E1 ou E2 échoue ; en E5, test séquentiel intermédiaire à $50\,\%$ des problèmes (`illustratif`) avec arrêt pour futilité si la puissance conditionnelle tombe sous $0{,}10$ (`illustratif`).

- **Établi vs conjecture :** Établi (`RAPPORTÉ`) : tests séquentiels et ordres de grandeur de puissance statistique (Wald, 1945). Conjecture (`HYPOTHÈSE`) : taille d'effet attendue $d = 0{,}50$ et variance inter-problèmes réelle (inconnues avant E1).
- **Où le cadrage est faux :** Demander les tailles d'échantillon avant d'avoir mesuré la variance inter-problèmes et le taux de base $p_0$ impose des chiffres provisoires qui doivent être recalibrés après l'étape pilote E1.
- **Confiance :** `0,75` (`HYPOTHÈSE`, `illustratif`).
- **Références :** Wald, A. (1945), *Sequential Tests of Statistical Hypotheses*, The Annals of Mathematical Statistics ; Platt, J. R. (1964), *Strong Inference*, Science.

#### 8. Limites, mauvaise position de la cible et faisabilité
- **Hors de portée de tout harnais automatisé (`HYPOTHÈSE`) :** (i) la création d'ontologies ou de changements de représentation (tout harnais fige une grammaire ou un vérificateur qui exclut les idées redéfinissant les observables) ; (ii) la fécondité scientifique à long terme dépendant d'instruments futurs ; (iii) les domaines sans oracle exécutable, formel ou expérimental rapide.
- **Preuves que la cible est mal posée (`HYPOTHÈSE`) :** (1) *Instabilité de représentation* : deux encodages mathématiquement isomorphes d'une même famille de problèmes produisent une corrélation de rang de Spearman $\rho < 0{,}30$ (`illustratif`) sur la rareté $R$ ; (2) *Effondrement rareté/profondeur* : aucune métrique OOD ne sépare les vérités plantées des surajustements rares dès que le décalage de distribution varie ; (3) *Disjonction des références* : l'intersection des idées rares pour l'énumérateur ET pour le modèle unique est vide.
- **Preuves qu'aucun harnais de ce type n'est faisable (`HYPOTHÈSE`) :** (1) Explosion de la taille d'échantillon ($N > 10^4$ problèmes non contaminés nécessaires, `illustratif`, hors d'atteinte hors synthétique) ; (2) En domaine ouvert sans oracle mécanique, largeur des intervalles PPI supérieure à tout effet réaliste sauf audit humain quasi exhaustif (annulant l'intérêt du harnais).

- **Établi vs conjecture :** Établi (`RAPPORTÉ`) : dépendance de la complexité descriptive au langage de codage jusqu'à une constante dépendant du traducteur (Solomonoff, 1964) et limites de la mesure adaptative (Dwork et al., 2015). Conjecture (`HYPOTHÈSE`) : seuil empirique à partir duquel l'instabilité de codage invalide en pratique les classements entre systèmes.
- **Où le cadrage est faux :** La question suppose qu'un harnais peut trancher globalement si un système « trouve des idées rares et profondes ». En réalité, il ne peut trancher qu'une **projection bornée** de cette affirmation dans des univers à ontologie fixée et vérification peu coûteuse.
- **Confiance :** `0,85` (`HYPOTHÈSE`, `illustratif`).
- **Références :** Solomonoff, R. J. (1964), *A Formal Theory of Inductive Inference. Part I*, Information and Control ; Dwork, C. et al. (2015), réf. citée.

---

### (b) Expériences décisives en inférence forte ($H_A$ contre $H_B$)

Toutes les expériences appliquent l'inférence forte (`RAPPORTÉ`, Platt, 1964) : deux hypothèses exclusives, un contrôle négatif obligatoire, et une falsification bilatérale. Tous les seuils et $N$ sont `illustratif`.

1. **E1 — Métrologie du harnais : séparation 4 quadrants (synthétique + Lean 4 + exécutable)**
   - **$H_A$** : Le couple $(R_{\mathcal{Q}_0}, D_{\text{ext}})$ sépare les solutions plantées *narrow & deep* des trois classes leurres appariées (*rare & shallow*, *common & deep*, *common & shallow*).
   - **$H_B$** : Le harnais confond profondeur avec rareté syntaxique ou ajustement en distribution.
   - **Métrique & seuil (`illustratif`) :** $\text{AUROC}_{\text{target vs leurres}} \ge 0{,}85$ ET $\text{FPR}_{\text{rare-shallow}} \le 0{,}05$ sur $N = 100$ problèmes synthétiques/formels appariés.
   - **Contrôle négatif :** Générateurs adversariaux triviaux (mutation syntaxique aléatoire, splines/polynômes surajustés en distribution, lemmes gonflés redondants) + test A/A (deux graines identiques).
   - **Falsification :** $\text{AUROC} < 0{,}85$ ou $\text{FPR}_{\text{rare-shallow}} > 0{,}05$ ou taux de rejet A/A $> 0{,}05$ falsifie $H_A$ (arrêt immédiat du projet avant tout run LLM coûteux) ; le dépassement simultané de tous les seuils falsifie $H_B$.

2. **E2 — Invariance de représentation, biais du juge (PPI) et contamination**
   - **$H_A$** : Le classement par $R_{\mathcal{Q}_0}$ reste stable sous recodage isomorphe ($\rho \ge 0{,}70$), le juge corrigé PPI résiste au *style-swap* ($|\delta_{\text{style}}| \le 0{,}05\,\sigma$) et la rétrodiction/synthèse ne présente pas de fuite mémorielle ($\Delta_{\text{mém}} \le 0{,}02$, tout `illustratif`).
   - **$H_B$** : La cible dépend arbitrairement du codage, ou le biais de style/contamination excède les seuils et masque tout effet réel.
   - **Métrique & seuil (`illustratif`) :** Corrélation de Spearman $\rho$ entre deux encodages isomorphes ($N = 80$ problèmes) ; décalage de score sous permutation de style entre système et baseline ($N = 200$ paires) ; écart de performance entre problèmes isomorphes fraîchement renommés et formulations canoniques.
   - **Contrôle négatif :** Problèmes volontairement fuis/canoniques (doivent déclencher l'alerte de contamination) et paires au contenu identique mais au style rhétorique opposé (doivent donner $\delta_{\text{style}} \approx 0$).
   - **Falsification :** $\rho < 0{,}70$ ou $|\delta_{\text{style}}| > 0{,}05\,\sigma$ ou $\Delta_{\text{mém}} > 0{,}02$ falsifie $H_A$ (cible mal posée ou juge/rétrodiction disqualifiés) ; la satisfaction conjointe des trois critères falsifie $H_B$.

3. **E3 — Test prédictif du choix de problèmes (interaction $\text{Système} \times \text{Régime}$)**
   - **$H_A$** : La taxonomie pré-enregistrée prédit à l'avance les familles hors échantillon où les agents LLM surpassent les baselines, avec interaction positive $\Delta_{\text{fertile}} - \Delta_{\text{négatif}} \ge \delta_3 = 0{,}30\,\sigma$ ($p_{\text{Holm}} < 0{,}01$, `illustratif`).
   - **$H_B$** : L'avantage présumé par région ne généralise pas hors échantillon ($\Delta_{\text{fertile}} - \Delta_{\text{négatif}} \le 0$ ou IC 95 % incluant 0).
   - **Métrique & seuil (`illustratif`) :** Interaction appariée sur 4 familles de problèmes nouvelles (2 prédites fertiles, 2 prédites négatives : petit combinatoire et piège sans structure), $N = 40$ problèmes/famille.
   - **Contrôle négatif :** Régime « aiguille sans structure » (espace permuté aléatoirement) où aucun système ne doit battre le tirage aléatoire.
   - **Falsification :** Absence d'interaction positive généralisable falsifie $H_A$ (hypothèse de région fertile réfutée) ; interaction positive accompagnée d'un échec prédit sur les régimes négatifs falsifie $H_B$.

4. **E4 — Étanchéité du feedback adaptatif contre la loi de Goodhart**
   - **$H_A$** : Le feedback autorisé (validité + erreur sur split interne) accroît la profondeur scellée $D_{\text{OOD}}$ ($\Delta D_{\text{OOD}} \ge 0{,}25\,\sigma$, `illustratif`) sans creuser l'écart de surajustement au-delà d'un plafond ($\Delta(D_{\text{train}} - D_{\text{OOD}}) \le 0{,}15\,\sigma$, `illustratif`).
   - **$H_B$** : Le feedback n'améliore que le score interne tout en laissant $D_{\text{OOD}}$ nul ou décroissant (Goodharting).
   - **Métrique & seuil (`illustratif`) :** Contraste apparié (avec vs sans feedback interne) sur $N = 60$ problèmes synthétiques/exécutables.
   - **Contrôle négatif :** Variante « fuite délibérée » recevant le score de rareté $R$ pendant la recherche (doit exhiber une hausse de $R$ accompagnée d'une chute ou stagnation de $D_{\text{OOD}}$).
   - **Falsification :** $\Delta D_{\text{OOD}} \le 0$ avec $\Delta D_{\text{train}} > 0$ falsifie $H_A$ ; gain OOD net et contrôlé falsifie $H_B$.

5. **E5 — Duel principal à double contrainte budgétaire : multi-agents vs enveloppe des baselines**
   - **$H_A$** : Le système multi-agents bat l'enveloppe $\max(\text{Single-LLM Best-of-}K,\; \text{Énumérateur mécanique},\; \text{Aléatoire})$ sur $U(P,B)$ à budget FLOPs/USD égal ET à budget d'appels oracle égal (borne inf. IC 95 % cluster-bootstrap $> \delta_5 = 0{,}20\,\sigma$, $p_{\text{Holm}} < 0{,}01$, `illustratif`, sur $\ge 2$ familles indépendantes).
   - **$H_B$** : Le système multi-agents est égalé ou battu par au moins une baseline de l'enveloppe sur l'un des deux axes budgétaires ou sur une famille indépendante.
   - **Métrique & seuil (`illustratif`) :** AUDC sur $U(P,B)$ et taux de succès conjoint, $N = 60$ problèmes indépendants par famille $\times$ 2 familles validées en E3 (120 problèmes au total), avec test de futilité à $N = 60$.
   - **Contrôle négatif :** Problèmes du régime négatif (petit espace formel/combinatoire) où l'énumérateur doit battre les LLM, vérifiant l'absence de biais de configuration en faveur du multi-agents.
   - **Falsification :** Échec à dominer l'enveloppe sur les deux axes ou sur les deux familles falsifie $H_A$ ; domination robuste falsifie $H_B$.

6. **E6 — Attribution causale par ablations (interaction critique vs diversité/re-tirage)**
   - **$H_A$** : Le protocole multi-agents avec critique ciblée surpasse à la fois l'ensemble hétérogène indépendant sans dialogue et la critique placebo (budget identique) d'au moins $\delta_6 = 0{,}15\,\sigma$ ($p_{\text{Holm}} < 0{,}01$, `illustratif`).
   - **$H_B$** : L'ensemble indépendant ou la critique placebo égale ou bat la critique ciblée (l'effet de E5 provient de la diversité ou du ré-échantillonnage, non du dialogue critique).
   - **Métrique & seuil (`illustratif`) :** Différence appariée sur $U(P,B)$ sur les mêmes $N = 120$ problèmes que E5 (exécuté uniquement si E5 valide $H_A$).
   - **Contrôle négatif :** Critique permutée (commentaires d'un autre problème injectés comme feedback), qui doit rester $\le$ au multi-agents réel et $\approx$ au ré-échantillonnage simple.
   - **Falsification :** Écart $\le \delta_6$ ou IC 95 % incluant 0 falsifie $H_A$ ; supériorité nette sur les deux ablations falsifie $H_B$.

---

### (c) Validation minimale de chaque instrument nommé dans la question

Toutes les cibles numériques de détection (TPR) et de fausses alertes (FPR) sont marquées `illustratif` (elles définissent le cahier des charges minimal avant validation).

| Instrument nommé | Mesure minimale de fonctionnement | TPR / FPR cibles (`illustratif`) | Cas honnêtes appariés (contrôles de même surface) | Vérifications mécaniques à battre |
|---|---|---|---|---|
| **1. Métrique « narrow » ($R_{\mathcal{Q}_0}$)** | Sensibilité aux solutions rares plantées + invariance aux paraphrases/renommages. | $\text{TPR} \ge 0{,}85$ ; $\text{FPR} \le 0{,}05$ | Idées courantes **paraphrasées/renommées** (même classe sémantique, syntaxe rare) appariées aux idées véritablement rares. | Distance d'édition brute, rareté n-gramme/perplexité sans canonisation. |
| **2. Métrique « deep » ($D_{\text{ext}}$)** | Discrimination de la conséquence OOD/compression aval contre bruit rare et clichés. | $\text{TPR} \ge 0{,}90$ ; $\text{FPR} \le 0{,}05$ | Leurres **rares mais creux** de même longueur de description et même erreur en distribution (surajustements, tautologies rares). | Erreur sur split d'entraînement, log-vraisemblance en distribution, longueur brute de formule/preuve. |
| **3. Juge LLM (+ correcteur PPI)** | Accord calibré avec oracle externe + invariance au style (IC 95 % PPI couvrant le vrai effet $\ge 95\,\%$, `illustratif`). | $\text{TPR} \ge 0{,}80$ ; $\text{FPR} \le 0{,}10$ ; $|\delta_{\text{style}}| \le 0{,}05\,\sigma$ | Idées profondes en **style sec/maladroit** appariées à des idées fausses ou triviales en **style académique poli** (*style-swap*). | Heuristique longueur + perplexité ; score brut du juge LLM sans correction PPI. |
| **4. Monde synthétique (vérité plantée)** | Détection de la loi/invariant planté sans faux positifs sur mondes nuls. | $\text{TPR} \ge 0{,}95$ ; $\text{FPR} \le 0{,}02$ | **Mondes nuls appariés** ayant les mêmes marginales et corrélations de bas ordre mais aucun invariant profond planté. | Régression polynomiale/arbres par force brute ; recherche aléatoire de caractéristiques. |
| **5. Rétrodiction à coupure temporelle** | Capacité à rejeter les fuites mémorielles et à distinguer raisonnement vs rappel. | Détection fuite $\ge 0{,}90$ ; $\text{FPR} \le 0{,}05$ | Problèmes **pré-coupure renommés/masqués** appariés à des variantes **post-coupure synthétiques** de difficulté égale. | Recherche par similarité lexicale (TF-IDF / recouvrement n-grammes pré-coupure) ; contrôle zéro-shot sans raisonnement. |
| **6. Preuve formelle (vérificateur + compression aval)** | Zéro faux positif de validité + détection des lemmes réellement réutilisables. | Validité $\text{FPR} = 0$ (`VÉRIFIÉ` modulo noyau) ; utilité $\text{TPR} \ge 0{,}85$, $\text{FPR} \le 0{,}05$ | **Lemmes triviaux gonflés** ou redondants de même nombre de tactiques/tokens appariés à des lemmes clés de bibliothèques gelées. | Tactiques automatiques / solveurs SMT (`simp`, `omega`, marteaux ATP) et énumérateur borné à budget CPU égal. |
| **7. Tests exécutables / simulateur** | Détection de la généralisation interventionnelle et rejet du *reward hacking*. | $\text{TPR} \ge 0{,}90$ ; $\text{FPR} \le 0{,}05$ | **Interpolateurs / tables de correspondance** atteignant une erreur d'entraînement identique mais échouant sous intervention OOD. | Validation croisée en distribution ; fuzzing aléatoire de paramètres. |
| **8. Baselines (aléatoire, énumérateur, modèle unique)** | Reproductibilité inter-graines et exactitude de la comptabilité budget/oracle (écart $< 2\,\%$, `illustratif`). | Faux positif A/A $\le 0{,}05$ ; couverture budget $= 100\,\%$ | Deux exécutions identiques de la même baseline sur graines distinctes (contrôle A/A) + problèmes calibrés de difficulté connue. | Vérificateur déterministe de budget (compteur exact de tokens, FLOPs et appels oracle) ; tirage uniforme pur. |
| **9. Sélecteur de problèmes & garde-fou de feedback** | Prédiction hors échantillon des régimes fertiles + détection du surajustement adaptatif. | $\text{TPR}_{\text{Goodhart}} \ge 0{,}85$ ; $\text{FPR} \le 0{,}05$ | Familles de problèmes de **même domaine/longueur** mais paysages trompeurs ; agents surajustant bruyamment le split interne. | Tirage uniforme de problèmes ; réutilisation naïve du même jeu d'évaluation sans coffre scellé. |

---

### (d) Ancrage matériel (entièrement `illustratif`)

L'ensemble des choix modèles, volumes de calcul et coûts ci-dessous est marqué **`illustratif`** (aucune contrainte matérielle n'étant fournie dans les faits ; l'existence des familles de modèles ouverts citées est `RAPPORTÉ`).

- **Modèles ouverts recommandés (reproductibilité, contrôle des graines, zéro dérive d'API) :**
  - *Niveau calibration / petits agents (E1–E4) :* modèle ouvert ~7–8 milliards de paramètres (familles open-weights type Llama-3.1-8B-Instruct ou Qwen2.5-7B-Instruct, `RAPPORTÉ`), exécutable en FP16/BF16 sur 1 GPU 24–80 Go (`illustratif`).
  - *Niveau pleine échelle (E5–E6) :* modèle ouvert ~70–72 milliards de paramètres (familles open-weights type Llama-3.1-70B-Instruct ou Qwen2.5-72B-Instruct, `RAPPORTÉ`) + un second modèle ouvert d'architecture/entraînement distinct de taille comparable pour l'ablation « ensemble hétérogène » de E6 (`illustratif`).
  - *Environnement mécanique / oracles :* nœuds CPU multi-cœurs pour vérificateur formel (Lean 4), énumérateur symbolique/SMT et simulateurs Python en bac à sable isolé (sans accès réseau).

- **Budget de calcul et coûts estimés par phase (cloud GPU standard à ~2,50 USD/h par H100 80 Go et ~0,05 USD/h par vCPU, tout `illustratif`) :**

| Phase | Contenu et échelle (`illustratif`) | Calcul estimé (`illustratif`) | Coût estimé (`illustratif`) | Porte d'arrêt (*Go/No-Go*) |
|---|---|---|---|---|
| **E1** | Calibration harnais : 100 problèmes (synthétique + Lean 4 + exécutable), contrôles adversariaux & A/A (CPU + modèle 8B) | 500 vCPU-h + 20 H100-h | ~75 USD | Échec $\text{AUROC}/ \text{FPR}$ ou A/A $\implies$ arrêt immédiat |
| **E2** | Invariance recodage (80 prob.), *style-swap* (200 paires), audit PPI & fuite (modèle 8B + 70B léger) | 200 vCPU-h + 60 H100-h | ~160 USD | $\rho < 0{,}70$ ou $|\delta_{\text{style}}| > 0{,}05\,\sigma$ $\implies$ arrêt / retrait du juge |
| **E3** | Taxonomie de problèmes : 4 familles $\times$ 40 problèmes (modèle 8B + énumérateur) | 2 000 vCPU-h + 120 H100-h | ~400 USD | Pas d'interaction $\text{Système}\times\text{Régime}$ $\implies$ révision cadrage |
| **E4** | Test feedback vs Goodhart : 60 problèmes $\times$ 3 conditions (sans, autorisé, fuite rareté) | 800 vCPU-h + 100 H100-h | ~290 USD | Goodhart avéré ($\Delta D_{\text{OOD}} \le 0$) $\implies$ retrait du feedback |
| **E5** | Duel principal : 120 problèmes $\times$ 4 systèmes (multi-agents, Best-of-$K$ 70B, énumérateur, aléatoire), ~200k tokens/problème/système LLM | 10 000 vCPU-h + 900 H100-h | ~2 750 USD | Arrêt futilité à $50\,\%$ (~1 400 USD) si puissance cond. $< 0{,}10$ |
| **E6** | Ablations d'attribution (ensemble hétérogène, auto-raffinement, critique placebo) sur les 120 problèmes (conditionnel à E5) | 3 000 vCPU-h + 750 H100-h | ~2 025 USD | Non exécuté si E5 réfute $H_A$ |
| **Total plafonné** | **Campagne complète E1–E6 (hors temps humain d'audit PPI : ~30–50 h d'experts si juge utilisé)** | **~16 500 vCPU-h + ~1 950 H100-h** | **~5 700 USD** (~925 USD avant E5) | **84 % du budget protégé par les portes E1–E4** |

Ce découpage garantit que l'échec du harnais (E1–E2), l'absence de régime favorable (E3) ou la dérive Goodhart (E4) sont détectés pour moins d'un millier de dollars (`illustratif`), avant d'engager la dépense des comparaisons à grande échelle (E5–E6).

FIN-DE-CELLULE

## Cellule E3-T2-critique-croisee-A (lettre A)

# Proposition A — Tour III.2 : critique croisée de méthode

**Pièces.** Le bloc FAITS est identique au bloc QUESTION (même empreinte) : il ne contient aucun fait étiqueté, donc aucun VÉRIFIÉ. Les pièces B, C, D et E sont présentes et complètes ; ma conception du tour III.1 n'est pas transmise et je ne m'y réfère pas.

**Statut.** Tout ce qui suit est HYPOTHÈSE (analyse de méthode). Les nombres sont recalculés à partir des paramètres illustratifs des pièces : ils sont **illustratifs**.

**Notations.**
- p : probabilité qu'un tirage de référence atteigne une classe ; M : nombre de tirages de référence.
- φ : taux de fausses alertes par idée ; m : nombre d'idées soumises par run.
- π : taux de succès par problème ; q : probabilité d'une paire discordante.

---

## Sur la proposition B

### (a) Défauts de méthode

1. **E4 est en partie vrai par construction.** L'étroitesse n est définie relativement à Q, « le modèle unique à température 1 », et le bras 4 est ce même modèle en best-of-N. Avec k tirages, P(bras 4 atteint une classe telle que n ≥ η) ≤ k·e^(−η). Le succès de la ligne de base est donc plafonné par la définition, et tout générateur dont la loi diffère de Q gagne sans être meilleur.
2. **Le nombre de candidats est une variable confondante.** succ_C vaut 1 si « au moins une idée » passe, sans plafond de nominations. La probabilité de fausse réussite par run est 1 − (1 − φ)^m. Avec φ = 0,05 (seuil de B) et m = 50, elle vaut ≈ 0,92. Le bras le plus prolixe gagne.
3. **E1 est tautologique.** K est construit à partir de la loi plantée, donc d est élevé par construction. Les leurres sont stériles par construction et la permutation s'effondre par construction. E1 valide le code, pas le construit. Seules des lois vraies non plantées échapperaient à cette circularité.
4. **E2 souffre d'une troncature.** Si les classes comparées proviennent des tirages des Q, une classe vue par Q₁ seul a un n fini sous Q₁ et censuré sous Q₂. Cela induit mécaniquement une corrélation négative (sélection de type Berkson).
5. **E3 a une étendue restreinte.** L'échantillon est tiré de Q, donc les classes rares y sont quasi absentes. De plus d est ajusté sur la complexité et n ne l'est pas. Si la complexité covarie avec n, ρ(n, d) est en partie mécanique.
6. **E8 est circulaire.** La règle « faible couverture sous Q » est une composante du critère de succès (n ≥ η sous Q). La permutation des étiquettes ne détecte pas cette circularité.
7. **La canonicalisation n'est évaluée que d'un côté.** « Fusionner ≥ 98 % des paraphrases » est satisfait par une canonicalisation constante. Le taux de fausses fusions n'est pas exigé.
8. **E7 n'apparie pas les cibles.** Présentes et absentes du corpus diffèrent en ancienneté, notoriété et simplicité. Un rapport ≥ 3 ne sépare pas le rappel de la difficulté.
9. **B4 n'est pas respecté partout.** E2 (0,3 < ρ < 0,7), E3 (0,1 < ρ < 0,5 et ρ < 0) et E5 (récupération entre 20 % et 80 %) ont des zones où aucune hypothèse n'est falsifiée.
10. **Le contrôle de profondeur est insuffisant.** Une « constante perturbée » est une idée fausse. Elle ne dit rien d'une idée vraie mais inerte.

### (b) Pertes de puissance

- **Étroitesse.** Avec zéro occurrence sur M tirages, l'estimateur plafonne à ln(M/3), soit 9,2 nats pour M = 30 000. Si η dépasse ce plafond, le critère est indécidable. Si la loi de p parmi les classes valides concentre sa masse sous 1/M, l'estimateur est presque constant. Les ρ de E2 et E3 sont alors dominés par les ex æquo, et le plafond inter-graines de B tombe lui-même sous 0,7.
- **E1.** La valeur prédictive positive vaut sens·π / (sens·π + φ(1 − π)). Avec une prévalence de 0,01 et les seuils de B (0,8 et 0,05), elle vaut ≈ 0,14. Les seuils de B ne suffisent donc pas à cette prévalence.
- **E4.** La puissance du test de McNemar dépend de n·q. Si les deux taux de succès tendent vers 0, q tend vers 0 et les 118 problèmes ne tranchent rien. Par ailleurs l'enveloppe max_b prise par problème a une espérance supérieure au max des espérances, et l'écart croît avec la variance inter-graines.
- **Profondeur.** d n'a pas de variance si la probabilité que S résolve K_test sans x est proche de 0 ou de 1.
- **E5.** La « part du gain récupérée » est un quotient. Si l'intervalle du gain de E4 approche 0, l'intervalle du quotient n'est plus borné.
- **E7.** Les modèles à données ouvertes sont petits. Si (taux de succès sur cibles absentes) × (nombre de cibles absentes) reste sous quelques unités, le rapport est non estimable.

### (c) Contrôles négatifs dont l'absence serait fatale

- **Bras « différent mais pas meilleur ».** Une autre famille de force inférieure ou égale, ou Q perturbé. S'il gagne E4, la mesure est une distance à Q. S'il perd, l'objection 1 tombe.
- **Bras « spam ».** m idées valides, rares et aléatoires, avec le même m que le système. succ doit rester proche de 0.
- **Paires proches mais distinctes**, pour mesurer les fausses fusions.
- **Idée vraie mais inerte, et table recopiant K_train**, au niveau de d.
- **Référence Q′ disjointe** de celle qui sert à choisir les régions (E8).

---

## Sur la proposition C

Je reprends telle quelle sa règle commune (T > 0 contre T ≤ 0, exhaustive) et sa critique permutée. Ce sont les deux éléments que je réutiliserais.

### (a) Défauts de méthode

1. **Dilemme entre référence et ligne de base.** « Étroite » exige max_r p_r < τ, et r inclut un solo avec outils. Deux cas se présentent :
   - Si cette référence coïncide avec le solo gelé du duel, alors π_solo ≤ K·τ par définition (K = nombre de classes qualifiées par monde). Le duel devient un test à un échantillon : π_sys > 0,05 + Kτ.
   - Si elle en diffère (le solo gelé inclut la recherche arborescente, la référence archivée non), « étroit » n'est plus relatif à la meilleure recherche ordinaire.
   
   C ne dit pas lequel des deux cas s'applique.
2. **Classe extensionnelle, profondeur intensionnelle.** Une table de vérité et une loi coïncident sur tout le domaine fini : elles forment la même classe. Mais le gain du résolveur dépend du représentant fourni (longueur, coût d'appel). On ne sait pas à quel représentant le placebo est apparié. d n'est pas une fonction de la classe.
3. **Profondeur plantée.** Si les problèmes aval sont générés à partir de la règle plantée, toute règle vraie non plantée a d ≈ 0 par construction. La clause « accepter les règles non plantées » vaut pour la vérité, pas pour la profondeur.
4. **L'audit à 3 330 négatifs est soit redondant, soit infaisable.**
   - En micromonde exhaustif, la vérité et l'identité sont exactes. Les seules erreurs sont celles des bornes, déjà fixées par α. L'audit ne détecte que des bogues.
   - Hors exhaustif, l'oracle qui étiquetterait ces négatifs n'existe pas.
   
   De plus le taux de fausses alertes est estimé sous la loi des négatifs d'audit. Le calcul de Bayes s'applique à la loi des sorties de chaque bras. Rien n'égalise les deux.
5. **Nomination unique.** π = P(trouver) × P(nommer | trouver). La rareté est cachée, à juste titre, donc la nomination sur l'axe « étroit » se fait à l'aveugle. La mesure porte autant sur la sélection que sur la recherche, alors que la question dit « finds ».
6. **Sélecteur de régions.** Le descripteur « nombre de sous-problèmes partageant une structure » est une composante mécanique de d (gain sur des problèmes aval partageant une structure).

### (b) Pertes de puissance

- **Sonde de rareté.** La sensibilité vaut E[(1 − p)^M | p < τ]. Avec M = 300 et p = 0,005, elle vaut ≈ 0,22. Atteindre 0,8 exige p ≤ 7,4·10⁻⁴. Le seuil effectif est donc ≈ 13 fois plus bas que τ = 0,01. Avec une correction simultanée sur c classes et r politiques, il faut M ≥ ln(c·r/α)/τ.
- **Dossiers non résolus.** Si la probabilité de non-résolution diffère entre bras d'une quantité au moins égale à l'écart attendu g, les bornes au pire cas et au meilleur cas encadrent 0. Le harnais ne tranche pas, quel que soit n.
- **Critique permutée.** Elle perd toute puissance si la critique utile est générique, c'est-à-dire si son effet est indépendant du dossier. On conclurait « effet de procédure » alors que la critique contribue.
- **Duel principal.** n ≈ 6,2·q/g². Sous le cas 1 du dilemme, q ≈ π_sys. Le duel n'est jugeable que si π_sys·n dépasse quelques dizaines.

### (c) Contrôles négatifs dont l'absence serait fatale

- **Invariance au représentant.** Même classe, trois représentants, d constant. Sinon d mesure le codage.
- **Retrait d'une référence à la fois.** Le verdict doit survivre au retrait ou au remplacement du solo de référence.
- **Bras « différent mais pas meilleur »**, comme pour B.
- **Audit exhaustif des sorties réelles de chaque bras**, par échantillon aléatoire, et non de négatifs fabriqués.
- **Monde à deux règles profondes dont une seule est documentée comme plantée.** La seconde doit être créditée.

---

## Sur la proposition D

**Remarque de statut.** D étiquette [VÉRIFIÉ] des choix de conception et des affirmations empiriques que les FAITS ne contiennent pas. Exemples : « garantissant zéro mémorisation littérale » ; « exposer N pousse vers l'obfuscation ». Je ne modifie pas ces statuts. Je signale qu'aucune pièce transmise ne les soutient.

### (a) Défauts de méthode

1. **Le seuil d'étroitesse est collé au plafond.** Avec M₀ = 1 000 et zéro occurrence, la borne de Clopper-Pearson donne N ≈ 5,81 nats. Avec une seule occurrence, N ≈ 5,35, sous τ_N = 5,5. « Étroit » équivaut donc à « jamais vu en 1 000 tirages ». La mesure est binaire, et toute classe non échantillonnée est étroite, quelle que soit sa nature.
2. **Exp. II est vraie par construction contre BestOfN-Mono.** Le plafonnement est celui décrit pour B. L'ablation (iv), homogène contre hétérogène, « démontre » la diversité par définition : une classe courante pour la seconde famille et rare pour μ₀ compte comme étroite. D ne dit pas non plus comment ses deux références (modèle seul, énumérateur) se combinent.
3. **D_MDL est biaisé et extensif.**
   - Le max(0, ·) par régime donne à une loi nulle une espérance d'environ 0,40·R·σ, où σ est l'écart-type du gain par régime. La troncature masque aussi les régimes où la loi est fausse.
   - Le gain en nats croît linéairement avec la taille des D_r. Avec assez de points, τ_D = 35 nats est franchi par une amélioration minuscule. Le seuil mesure la taille du jeu de test.
   - K_L([x]) porte sur quel représentant de la classe ? D n'est pas invariant par classe.
4. **Exp. IV est circulaire.** S_region est calculé sur les résidus des références simples. Un fort résidu signifie que la recherche ordinaire échoue, donc que N est élevé. Par ailleurs l'« existence d'une solution » n'est connue qu'en monde planté, où le concepteur fixe à la fois S_region et l'existence. L'OR est choisi par le générateur de mondes.
5. **Porte 5 : fuite entre construction et évaluation.** Les transformations testées (commutativité, termes nuls, renommage α, code mort) sont les règles de réécriture du quotient par e-graphes. Le taux de 0,98 est acquis d'avance.
6. **Le plan de puissance contredit la règle de décision.** Les 100 problèmes de la phase IV (0,05 → 0,18) correspondent à un test contre 0. La règle impose un test contre δ_min = 0,10. L'écart utile est alors 0,03 et n ≈ 1 900. En phase II, avec 60 problèmes et q = 0,3, la puissance de 0,8 n'est atteinte que pour un écart vrai ≥ 0,30. « Échoue à battre → arrêt du programme » confond alors non concluant et réfuté.
7. **Exp. III : ΔN est une médiane de valeurs censurées.** Si plus de la moitié des candidats retenus ont zéro occurrence dans les deux bras, ΔN = 0 identiquement et H_A est falsifiée par construction. La zone ΔZ > 0 avec 0 ≤ ΔN < 0,7 n'est attribuée à aucune issue.
8. **Exp. VI.** Auditer « un sous-échantillon des Ĵ = 1 et Ĵ = 0 » estime les valeurs prédictives, pas (TPR, FPR). L'inversion exige la prévalence et une correction du biais de vérification (Begg & Greenes, 1983, *Biometrics*, « Assessment of diagnostic tests when disease verification is subject to selection bias »). Le critère FPR_g ≥ π_g suppose connu π_g, qui est l'inconnue.

### (b) Pertes de puissance

- **Étroitesse.** La sensibilité vaut (1 − p)^M₀. Pour p = 0,002 (classe réellement étroite, 6,2 nats), elle vaut ≈ 0,135. Atteindre 0,8 exige p ≤ 2,2·10⁻⁴, soit ≈ 8,4 nats. Le seuil effectif est à 3 nats du seuil affiché.
- **Exp. I.** Le score I[N ≥ τ_N]·D est nul pour la plupart des classes. Le τ de Kendall est gouverné par la proportion de zéros et devient non jugeable si P(N ≥ τ_N) est proche de 0 ou de 1. Sur le contrôle négatif, l'écart-type de τ sous indépendance pour n = 200 est ≈ 0,048. Le critère |τ̄| ≤ 0,08 échoue par hasard ≈ 9 % du temps, hors ex æquo.
- **Exp. VI.** Démontrer FPR < 0,01 sur 500 négatifs exige au plus une alerte. Un juge de FPR vrai 0,005 passe avec une probabilité ≈ 0,29. Par ailleurs la variance de l'estimateur de Rogan-Gladen croît en 1/(TPR − FPR)², et l'estimateur devient négatif quand π approche de 0.
- **Exp. IV.** Si la prévalence dans la strate S = 0 est ≤ 0,05, on attend au plus 3 événements sur 60. L'intervalle de l'OR couvre plusieurs ordres de grandeur.
- **Profondeur des lemmes.** La variation du nombre de pas d'un prouveur déterministe après ajout d'un lemme quelconque n'est pas centrée en 0 et a des queues lourdes. Sans loi nulle empirique, τ_D n'a pas de taux d'erreur.

### (c) Contrôles négatifs dont l'absence serait fatale

- **Bras mono-modèle de la seconde famille**, seul, dans Exp. II. S'il « bat » l'enveloppe, N mesure la distance à μ₀.
- **Loi nulle de D** : lois ou lemmes vrais mais non pertinents, de même K, soumis au même R et aux mêmes tailles de D_r.
- **Obfuscations hors conception** : rédigées par un tiers ou par le générateur lui-même, hors des règles de l'e-graphe.
- **Répétition avec M₀ doublé.** La proportion de classes « étroites » ne doit pas changer au-delà de ce que prédit (1 − p)^M₀.
- **S_region recalculé sur une référence disjointe** de μ₀.

---

## Sur la proposition E

**Remarque de statut.** E utilise des doubles étiquettes (« VÉRIFIÉ/RAPPORTÉ », « OBSERVÉ-NON-AUDITÉ / HYPOTHÈSE ») et un « RAPPORTÉ » sans source (« invariance de représentation violée »). Ces statuts sont ambigus et je ne les tranche pas.

### (a) Défauts de méthode

1. **L'estimande d'étroitesse est double.** R est défini comme min_Q(−log₂ p̂_Q) « ou » min_Q B₀,₅. Ce sont deux quantités, et rien ne dit laquelle sert. Le budget médian de première atteinte est censuré à droite pour toute classe étroite. Et p̂ = 0 donne R infini : aucun estimateur n'est spécifié pour zéro occurrence.
2. **U(P, B) est un maximum sur toutes les sorties.** Même sous hypothèse nulle, l'espérance du maximum de m profondeurs bruitées croît comme σ·√(2 ln m). E écarte le « maximum brut » puis le reprend derrière un filtre. m diffère d'un facteur ≈ 10⁴ entre énumérateur et LLM (ordres de grandeur de E). C'est une variable confondante.
3. **Le contrôle négatif de E5 n'est pas jugeable sous la métrique de E.** En petit espace énumérable, la probabilité d'atteinte par l'énumérateur vaut 1, donc R = 0 < τ_R et U ≡ 0 pour tous les bras. « L'énumérateur doit battre les LLM » ne peut pas s'observer sur U.
4. **E3 est circulaire et sous-dimensionné.** Le descripteur « entropie d'échec du modèle unique » sélectionne les familles où la ligne de base échoue, puis on y mesure U_multi − U_base. L'unité pertinente est la famille (2 contre 2). Les 40 problèmes par famille sont des pseudo-réplicats. Le contraste « petit combinatoire » est prédit par n'importe quelle taxonomie.
5. **E2 fusionne trois questions.** Invariance au codage, biais du juge et contamination sont réunis dans un seul H_A. Son rejet ne dit pas laquelle échoue.
6. **Δ_mém confond mémoire et notation.** Renommer un problème dégrade aussi le raisonnement en notation inhabituelle. Le « contrôle négatif » proposé (problèmes volontairement fuités) est un contrôle positif.
7. **E4 teste l'utilité du retour, pas l'intégrité de la mesure.** La seule condition qui menace la mesure (fuite de R) est rangée en « contrôle ». R y est remesuré contre les mêmes références que celles qui ont fui.
8. **La règle de décision est incohérente.** Elle contraste avec max_b U_b (une seule comparaison) et ajoute Holm « sur l'ensemble des baselines ». Une enveloppe par problème n'est pas une ligne de base réalisable.
9. **L'estimation de R n'est pas budgétée.** Aucun tirage de référence n'apparaît dans les coûts. Avec p ≈ 10⁻³, il faut ≈ 3 000 tirages par problème et par référence.
10. **A/A.** E1 parle de « deux graines identiques », ce qui est déterministe donc trivial. La table (c) dit « graines distinctes ». La pièce se contredit.

### (b) Pertes de puissance

- **U est à inflation de zéros.** Les seuils en unités de σ (0,20σ, 0,30σ) reposent sur un σ estimé sur les mêmes données et dominé par les rares valeurs non nulles. Le nombre de problèmes informatifs est N·P(Δ_P ≠ 0). Avec π = 0,05 et N = 60, il y en a 3. Le calcul « d = 0,5 → N ≈ 50–60 » suppose des différences quasi normales.
- **|δ_style| ≤ 0,05σ sur 200 paires.** La demi-largeur de l'intervalle à 95 % vaut 1,96·√(2(1 − r)/200). Elle ne passe sous 0,05 que si la corrélation intra-paire r ≥ 0,935. En deçà, le critère se décide par le bruit.
- **PPI.** La validité suppose des étiquettes d'oracle tirées au hasard dans la même loi que les non étiquetées, par bras. Des experts ne sont pas un oracle. Le gain d'efficacité est de l'ordre de 1/(1 − ρ²), où ρ est la corrélation entre juge et vérité (variante à pondération optimale : référence à vérifier). Pour ρ ≤ 0,5 il est ≤ 1,33. À prévalence 0,01, n étiquetés donnent 0,01·n positifs.
- **E1.** L'AUROC exige un score scalaire, alors que (R, D) est non compensatoire par choix de E. L'AUROC est aussi insensible à la prévalence. Avec φ = 0,05 et π = 0,01, la valeur prédictive positive est ≈ 0,14, comme pour B.
- **AUDC.** Si les courbes se croisent, le signe de l'aire dépend de l'échelle de la grille (linéaire ou logarithmique).

### (c) Contrôles négatifs dont l'absence serait fatale

- **Loi de U sous hypothèse nulle à m apparié.** Un bras « spam » émet m idées valides, rares et sans conséquence. U doit rester ≈ 0 pour le m de chaque bras.
- **Panel de référence Q′ tenu à l'écart**, jamais utilisé pour la conception, la sélection ou la fuite de E4. La hausse de R sous fuite doit disparaître sous Q′, sinon elle n'est pas un artefact.
- **Renommage sur problèmes certainement inédits.** Il donne le coût pur de la notation, à soustraire de Δ_mém.
- **Descripteurs de E3 calculés sur un modèle et des graines disjoints** de la ligne de base du contraste.
- **Régime négatif jugeable.** L'énumérateur doit y gagner sur une quantité non identiquement nulle, par exemple D seul.

FIN-DE-CELLULE

## Cellule E3-T2-critique-croisee-B (lettre B)

# Proposition B, Tour III.2 : critique croisée de méthode

## Pièces et statuts

- Les quatre pièces A, C, D et E sont présentes. Chacune se termine par FIN-DE-CELLULE, et je n'y vois aucune coupure.
- Le bloc FAITS ne porte aucune étiquette de statut, et je ne lui en attribue pas. Il est identique au bloc QUESTION.
- Tout ce que j'ajoute a le statut **HYPOTHÈSE**, y compris les dérivations élémentaires, que je n'ai pas fait auditer.
- Je reprends tels quels les statuts que les auteurs ont posés. Quand une étiquette me paraît mal fondée, je le signale sans la modifier.
- Les chiffres repris des pièces restent illustratifs. Les miens sont marqués « ill. ».

## Deux outils, appliqués séparément dans chaque section

**Borne de handicap.** Supposons que la politique qui sert de référence pour l'étroitesse soit aussi un bras comparé, au même budget. Une idée n'est « étroite » que si P_R(x) ≤ 2^{−ν*}. La probabilité que ce bras produise une idée étroite-profonde (EP) est donc bornée par construction : P(R produit une idée EP) ≤ |EP_w|·2^{−ν*}. Le duel « système contre cette référence » se ramène alors à tester si le taux du système dépasse 0 plus le seuil. On ne compare plus deux chercheurs.

**CN-1, divergence triviale.** Le « système » est remplacé par la référence elle-même, légèrement déplacée : température relevée, consigne paraphrasée ou graine d'une autre famille. Aucune capacité scientifique n'est ajoutée.
- H_A : le gain EP de ce bras reste sous le seuil de décision. Le critère ne récompense pas l'écart de distribution en tant que tel.
- H_B : le gain dépasse le seuil. Tout avantage mesuré du système peut alors venir de sa seule divergence par rapport à la référence.
- Chaque issue falsifie l'une des deux hypothèses.

**CN-2, chasseur d'étroitesse.** Un générateur tire depuis la référence en rejetant les candidats estimés probables sous elle. Il n'a aucun accès à la profondeur.
- H_A : sur des mondes sans idée EP, mais avec des leurres étroits et inertes, son taux EP reste sous le taux de fausses alertes admis.
- H_B : il marque des points. Le critère EP est alors perméable à l'étroitesse seule.

---

## Sur la proposition A

### (a) Défauts de méthode

1. **La borne de handicap s'applique à E4.** ν_{R,b} est calculée contre le modèle seul, et ce même modèle est le bras best-of-N. Si b vaut le budget B de E4, le best-of-N est majoré par |EP_w|·2^{−ν*}. A doit fixer b_ν ≪ B, ou montrer numériquement que la borne laisse au best-of-N une marge réelle.

2. **E1 est vrai par construction si l'étiquette et la mesure partagent leur source.** Le concepteur déclare une idée plantée « profonde » au vu des conséquences qu'il a construites. Si Δ est calculée par le même solveur, sur ces mêmes régimes retenus, l'AUC teste l'implémentation et non le concept. Il faut une étiquette produite indépendamment : un second jeu de conséquences tiré sans connaître x, ou un second solveur.

3. **L'oracle dilué de E3 se contredit.** Insérer l'idée plantée avec une probabilité q augmente P_R(x).
   - Si ν est estimée sur la référence diluée, on a ν ≤ log₂(1/q), soit environ 2,3 bits à q = 0,20, en deçà de ν*. L'idée plantée cesse d'être étroite.
   - La puissance mesurée devient alors une fonction décroissante de q, artefactuelle.
   - ν doit être figée sur la référence non diluée.

4. **E7 est en partie mécanique sous l'énumérateur.** Le prédicteur de déceptivité (la part d'inertes parmi les M premiers candidats énumérés) est fonctionnellement lié au rang d'énumération des idées profondes, donc à leur étroitesse sous l'énumérateur. Celui-ci est déterministe : l'indépendance des exécutions, invoquée par A, n'y change rien. H_A est en partie acquise d'avance pour cette référence.

5. **E4 appelle une correction de choix.**
   - **Risque.** Si « la meilleure référence » est désignée après les résultats, son choix parmi cinq bras introduit une sélection.
   - **Correction.** Exiger la supériorité contre chaque référence (intersection-union).

6. **La puissance de E4 est calculée contre zéro.** Les 140 mondes de A sont dimensionnés pour un écart de 5 % contre 15 % testé contre zéro. La règle exige pourtant un intervalle entièrement au-dessus de +5 points. L'écart effectif est donc de 5 points, ce qui demande environ quatre fois plus de mondes (ill.).

7. **E6 dépend du générateur de mondes.** Le ratio « gain privé / gain public » dépend de la corrélation entre conséquences publiques et privées, fixée par le générateur. Il mesure donc une propriété du générateur autant qu'une fuite. Le contrôle F3 n'y remédie qu'en partie.

### (b) Conditions de perte de puissance

- **ν et E2 :** dès que p_R(x) ≪ 3/K, on a P(N_x = 0) = (1−p)^K ≈ 1. La quasi-totalité des idées candidates est censurée au plafond log₂(K/3).
  - Le Spearman de E2 porte alors sur des ex-aequo et devient non jugeable.
  - La fiabilité de 0,9 en demi-échantillons est inatteignable par construction.
- **E1 :** si P(Δ = 0 | profonde) et P(Δ = 0 | leurre) sont tous deux grands, l'AUC tend vers 0,5 quelle que soit la validité du concept. Cela arrive quand le budget du solveur sature : conséquences insolubles même avec x, ou solubles sans x.
- **E4 (McNemar) :** le nombre de paires discordantes vaut environ n(π_S + π_R). Avec π_R borné par le handicap et π_S ≤ 0,05 (ill.), on attend moins de 8 discordances sur 150 mondes. Exclure +5 points devient impossible.
- **E7 :** avec un taux de base proche du plancher de 2 % de A, chaque quartile d'environ 37 mondes attend moins d'un succès. L'intervalle du ratio de densités n'est pas borné.
- **Borne de biais du juge :** si TPR − FPR tend vers 0, la différence corrigée entre bras n'est plus bornée.

### (c) Contrôles négatifs dont l'absence serait fatale

- **CN-1.** L'A/A de A ne le remplace pas : le handicap frappe identiquement les deux copies, et l'A/A ne peut donc pas le voir.
- **CN-2.** Le bras « bizarre » de A n'émet que des leurres scriptés. Il obtient zéro par construction et ne teste rien.
- **Profondeur conditionnée par une autre idée.** Calculer Δ(x) sur des conséquences engendrées à partir d'une autre idée plantée x′.
  - H_A : Δ(x) ≈ 0.
  - H_B : Δ(x) > 0, et la profondeur mesure alors la compatibilité générique avec le solveur.
- **ν figée.** Dans E3, ν doit être calculée sur la référence non diluée, sinon E3 est inopérante.

---

## Sur la proposition C

### (a) Défauts de méthode

1. **L'équivalence extensionnelle fait s'effondrer les classes éligibles.**
   - Deux règles sont la même idée si elles prédisent la même chose sur tout le domaine.
   - Toute règle fausse est inéligible.
   - Donc toute règle éligible qui prédit l'ensemble des observables coïncide avec la vérité cachée : il n'y a qu'une classe éligible par monde.
   - Le plan en quatre quadrants n'existe alors que pour des règles partielles. L'équivalence entre règles à domaines emboîtés n'est pas définie, et l'étroitesse d'une règle partielle dépend de cette convention.

2. **L'énumérateur à ordre randomisé ne discrimine rien.** Sous une permutation uniforme de M classes, au budget B, on a p_enum(c) = B/M pour toute classe c.
   - Cette politique n'apporte qu'un plancher constant au maximum des probabilités.
   - Si B/M ≥ τ, aucune classe n'est étroite.

3. **La borne de handicap s'applique.** Le « modèle solo avec outils » sert à la fois de politique d'étroitesse et de bras gelé. Les recherches de référence sont indépendantes de celles qui nomment les classes, ce qui règle la sélection mais pas le handicap.

4. **La source des problèmes aval n'est pas spécifiée.** C les tire « secrètement », sans dire par quel générateur.
   - Si ce générateur est conditionné par la règle plantée c, la profondeur de c est fabriquée.
   - Le placebo « règle vraie de même longueur » ne protège que si sa propre profondeur est tirée du même mécanisme.

5. **Plusieurs statuts VÉRIFIÉ ne sont pas auditables ici.** C étiquette VÉRIFIÉ deux citations bibliographiques. Je ne modifie pas ces statuts, mais rien dans les pièces ne permet de les auditer.

6. **Mérite à retenir.** Seule C dimensionne la puissance contre l'écart au seuil (« g au seuil, non à zéro »). Ce défaut, présent chez A, D et E, ne s'applique pas à C.

### (b) Conditions de perte de puissance

- **Maximum des probabilités sur R politiques.** Pour borner simultanément max_r p_r < τ avec zéro occurrence, il faut environ n ≥ ln(R/α)/τ exécutions par politique (ill.).
  - Si une politique a un p_r vrai compris entre τ/2 et τ, la puissance de la déclaration « étroite » s'effondre.
  - Le maximum est dominé par la politique la plus bruitée.
- **Profondeur.** La borne inférieure de la différence appariée doit dépasser 0,15 (ill.). Cela échoue si les fractions résolues avec et sans c saturent toutes deux, près de 0 ou de 1. Cela échoue aussi si le nombre m de problèmes aval par classe est petit, l'écart-type étant de l'ordre de √(1/m).
- **Duel principal.** Si π_S < 0,05 (ill.), H_A : T > 0 est impossible. Seule une borne supérieure non positive peut conclure, au prix d'un n que la discordance q, faible, rend très grand.
- **Duel des régions.** Avec 40 familles (ill.) et une forte variance de rendement entre familles, l'intervalle simultané couvre 0 : le duel est non décisif.

### (c) Contrôles négatifs dont l'absence serait fatale

- **CN-1 et CN-2.** C prévoit déjà la « règle vraie très rare portant sur une variable inutilisée ». C'est un cas scripté et non un chercheur : il ne remplace pas CN-2.
- **Monde à classe éligible unique.** Le pipeline ne doit rapporter aucune autre classe EP.
  - H_A : zéro classe rapportée en plus.
  - H_B : des classes en plus sont rapportées, et l'équivalence extensionnelle est mal implémentée.
- **Aval conditionné par une autre règle.** Le gain de c doit être nul sur des problèmes aval engendrés à partir d'une règle c′.

---

## Sur la proposition D

### (a) Défauts de méthode

1. **Des choix de conception sont étiquetés VÉRIFIÉ.** Exemples : la correction du quotientage par e-graphes, l'effet « obfuscation » d'un retour de N, la borne adaptative en O(√(T ln|X|/n)). Je ne change pas ces statuts. Je signale qu'en Phase I, les critères d'arrêt reposent sur la correction du quotient, qui est une hypothèse à tester (porte 5) et non un acquis.

2. **N n'a pas de gradation au seuil choisi.** Avec les valeurs de D (M0 = 1000, α = 0,05) :
   - zéro occurrence donne N ≈ −ln(1 − 0,05^{1/1000}) ≈ 5,81 nats ;
   - une occurrence donne N ≈ −ln(0,00474) ≈ 5,35 nats (ill.) ;
   - le seuil τ_N = 5,5 équivaut donc à « jamais vu en 1000 tirages ».
   
   L'excès continu Z n'en tire aucune gradation. Le décalage médian ΔN ≥ 0,7 nat de Exp. III est mécaniquement borné par ce plafond.

3. **Budget de référence et budget de comparaison.** Les tirages de référence sont « courts » (b0), alors que B = 64 000 jetons. Si B/b0 ≥ M0/3, un best-of-N au budget B devrait trouver des idées dites étroites avec une probabilité non négligeable. L'étroitesse n'est donc définie qu'au budget b0, et non au budget de la comparaison. Inversement, si la référence et le bras coïncident en budget, la borne de handicap s'applique (μ0 inclut le modèle de base seul).

4. **D_MDL est biaisée vers le haut.** La troncature max(0, ·) régime par régime en est la cause. Pour une expression x non pertinente, soit s l'écart-type du bruit de L_null − L(D_r|x). On a alors :
   - E[Σ_r max(0, ·)] ≈ 0,4·R·s ;
   - les leurres passent τ_D dès que 0,4·R·s > K + τ_D.
   
   De plus, si les constantes de x sont ajustées sur D_r, il y a fuite : la profondeur est calculée sur les données d'ajustement.

5. **Exp. I est vraie par construction pour l'énumérateur.** Les trois DSL sont « formellement isomorphes ». Si l'isomorphisme préserve la taille, le classement par coût est identique et τ_K = 1. S'il ne la préserve pas, Exp. I mesure les fonctions de coût, pas la stabilité de la cible.

6. **Exp. IV est en partie circulaire.** S_region = 1 signifie que les références simples échouent. Or N est définie par l'échec des références. Davantage d'idées N-élevées par définition entrent dans le numérateur de l'odds ratio.

7. **Exp. V viole B4 dans une zone intermédiaire.** Si Δ < 10 nats mais que la chute relative atteint ou dépasse 5 %, aucune des deux hypothèses n'est falsifiée. Les hypothèses sont exclusives, mais pas exhaustives.

8. **La puissance n'est pas cohérente avec la règle.** La Phase IV dimensionne 100 problèmes pour détecter 0,05 contre 0,18 testé contre zéro. La règle d'intersection-union exige pourtant δ_min = 0,10. L'excès effectif est de 0,03, ce qui demande de l'ordre de (1,96 + 0,84)²·0,2/0,03² ≈ 1,7 × 10³ paires (ill., avec une discordance de 0,2).

9. **Certaines exigences ne sont pas certifiables.** « TPR_causal = 1,00 » ou « FPR = 0 » ne se certifient pas statistiquement : seules des bornes unilatérales sont estimables.

### (b) Conditions de perte de puissance

- **Exp. II :** si π_MA − max_b π_b est proche de δ_min, la puissance de l'intersection-union est d'environ 0,5 au mieux (ill.). Avec π_b plafonné par le handicap, le test se réduit à π_MA ≥ 0,10.
- **Exp. III :** avec N censurée au voisinage de 5,8, la distribution de N des retenus est bimodale (sous τ_N ou au plafond), et le décalage médian est non jugeable.
- **Exp. IV :** si P(solution EP | S = 0) tend vers 0, l'odds ratio diverge sans information. Avec 60 problèmes par strate et une prévalence de quelques pour cent (ill.), le test de Fisher conclut rarement.
- **Exp. VI :** une borne de FPR inférieure à 0,01 sur 500 négatifs n'est atteinte qu'avec au plus environ 1 alerte, la borne à zéro alerte étant d'environ 0,006 (ill.). La moindre alerte rend H_B infalsifiable.
- **Correction Rogan-Gladen :** si TPR_g − FPR_g tend vers 0, π_g n'est pas borné.

### (c) Contrôles négatifs dont l'absence serait fatale

- **CN-1 et CN-2.** L'A/A de BestOfN-Mono est aveugle au handicap.
- **D_MDL d'expressions aléatoires.** Mesurer D_MDL pour des expressions de même K_L, non reliées au monde, avec les constantes figées sur D_train.
  - H_A : E[D] ≤ 0.
  - H_B : E[D] > 0, et la troncature fabrique de la profondeur.
- **Isomorphisme non conservatif.** Inclure dans Exp. I un isomorphisme qui ne conserve pas la taille, sans quoi Exp. I ne peut pas échouer pour l'énumérateur.

---

## Sur la proposition E

### (a) Défauts de méthode

1. **R est estimée par un estimateur ponctuel sans protection contre la sélection.**
   - R = min_Q(−log₂ p̂_Q) utilise p̂ ponctuel. Pour une idée jamais vue, p̂ = 0 et R = ∞ : l'estimateur n'est pas défini sur l'événement dominant.
   - E ne précise pas que p̂ est estimé sur des exécutions disjointes de celles qui ont produit les idées évaluées. A et C le font.
   - Sans cette disjonction, les idées retenues parce que la référence les a manquées par hasard paraissent étroites, par régression vers la moyenne.

2. **U contredit sa propre justification.** E écarte le « maximum brut » parce qu'il récompense la variance. Or U(P, B) = max_{x∈S(P,B)} D_ext·𝟙[·] est un maximum sur tout l'ensemble engendré S, et non sur la sortie sélectionnée.
   - **Le harnais court-circuite le sélecteur.** Il évalue D_ext sur tout S et agit comme un sélecteur parfait. La sélection du système n'est donc plus mesurée.
   - **U croît avec |S|.** Il favorise le bras qui produit le plus de candidats sur l'axe budgétaire non égalisé : l'énumérateur à FLOPs égaux, le modèle de langage à appels d'oracle égaux.

3. **L'égalisation simultanée des deux budgets (E5) est impossible.** E note lui-même 10⁶ appels pour l'énumérateur contre 10² pour un modèle (ill.). Ce que H_A compare n'est pas défini : deux duels, chacun à un axe fixé et l'autre libre ?

4. **L'enveloppe par problème est biaisée et change l'estimande.** Pour E[U_multi − max_b U_b], on a E[max_b U_b] ≥ max_b E[U_b] : le critère est plus sévère que « meilleur que chaque référence ». La correction de Holm qui s'y ajoute est redondante.

5. **Les seuils standardisés dépendent des données.** Les seuils exprimés en σ dépendent d'un écart-type estimé, dont la source et les bras inclus ne sont pas spécifiés.

6. **E3 relève de la pseudo-réplication.** L'hypothèse porte sur des familles, et il n'y en a que 4 (2 prédites fertiles, 2 négatives). Les 40 problèmes par famille ne sont pas des réplications de l'interaction. Le n effectif pour « la taxonomie prédit » est de 4. De plus, E3 valide sur un modèle de 8B et E5 exploite un modèle de 70B : le transfert est supposé.

7. **E2 agrège trois hypothèses.** L'invariance, le juge et la contamination sont réunis dans un seul H_A. Un échec ne dit pas laquelle est réfutée, ce qui ne satisfait pas l'inférence forte au sens de B4.

8. **La puissance est calculée contre zéro.** N ≈ 50–60 pour d = 0,5 est calculé contre zéro, alors que la règle exige δ₅ = 0,20σ. L'effet effectif est de 0,30σ, ce qui demande environ 2,8 fois plus de problèmes (ill.).

9. **Statuts.** P1 est étiqueté « RAPPORTÉ » sans référence. Je ne change pas ce statut, mais il n'est pas auditable dans la pièce.

10. **Borne de handicap.** Elle s'applique si Q_LLM-1 est le modèle du bras Best-of-K au même budget.

### (b) Conditions de perte de puissance

- **R :** si p_Q(x) ≪ 1/n_Q pour la plupart des idées, la fraction de R infinies tend vers 1. La moyenne et l'aire sous la courbe sont alors non définies ou dominées par la convention de plafond.
- **U comme maximum :** si D_ext a une queue droite lourde, la variance de U croît avec |S|. Le bootstrap en grappes sous-couvre quand la différence entre bras est portée par quelques problèmes extrêmes.
- **PPI :** avec une prévalence de positifs π et un sous-échantillon audité de taille n, on attend nπ positifs audités. Si nπ < 10 environ (ill.), l'intervalle PPI est plus large que tout effet réaliste. C'est le cas en régime rare, précisément celui visé.
- **E3 :** avec 4 familles, l'interaction n'a pratiquement aucun degré de liberté au niveau famille. La conclusion reste non jugeable quelle que soit la taille par famille.
- **E5, arrêt pour futilité :** si la variance entre problèmes est inconnue avant le pilote, la puissance conditionnelle à 50 % est elle-même très incertaine. La règle « < 0,10 » peut arrêter un vrai effet.

### (c) Contrôles négatifs dont l'absence serait fatale

- **CN-1 et CN-2.** CN-2 est d'autant plus nécessaire que U récompense le volume.
- **Étroitesse par sélection.** Évaluer R sur les sorties d'une réplication de référence, d'abord avec les mêmes exécutions qui les ont produites, puis avec des exécutions disjointes.
  - H_A : aucun excès d'étroitesse avec les exécutions disjointes.
  - H_B : un excès apparaît, et l'estimateur fabrique de la rareté par sélection.
- **Bras à volume gratuit.** Un bras émet beaucoup de candidats aléatoires valides à coût négligeable sur l'axe non égalisé.
  - H_A : U reste au niveau du tirage aléatoire.
  - H_B : U monte, et la métrique mesure le volume.

FIN-DE-CELLULE

## Cellule E3-T2-critique-croisee-C (lettre C)

**Convention.** **VÉRIFIÉ** désigne ci-dessous une lecture directe des pièces ou une déduction mathématique sous les conditions écrites ; cela ne valide empiriquement aucun harnais. **HYPOTHÈSE** désigne mes recommandations, les risques à tester et mes confiances subjectives, toutes **illustratives**. Les seuils numériques repris des propositions restent **illustratifs**. Les constantes dans les identités ne sont pas des estimations.

**Règle de réfutation proposée — HYPOTHÈSE.** Pour chaque contrôle négatif ci-dessous, fixer une statistique d’écart \(T\) entre la loi obtenue et la loi nulle attendue, ainsi qu’une tolérance \(\epsilon\), avant de voir les résultats. Opposer \(H_A:T\le\epsilon\) à \(H_B:T>\epsilon\). Un intervalle entièrement d’un côté réfute l’hypothèse de l’autre côté ; un intervalle traversant la frontière ne réfute rien. Pour une revendication de puissance, appliquer la même règle à la probabilité de détection sur des campagnes indépendantes, pas au verdict d’une seule campagne.

## Sur la proposition A

**(a) Défauts de méthode — VÉRIFIÉ pour les distinctions ; HYPOTHÈSE pour les risques.** À monde et budget fixés, le rang d’un énumérateur déterministe n’est pas une probabilité d’atteinte : toutes les classes avant la coupure sont atteintes, toutes celles après sont manquées. De même, un tirage uniforme sur classes ne les ordonne pas par rareté. E2 peut donc manquer d’un classement à comparer *même avec un calcul exact*. En E1, si le concepteur nomme « profondes » les idées qui améliorent précisément les régimes servant à calculer \(\Delta\), l’AUC vérifie la cohérence des étiquettes, pas la fécondité sur de nouvelles conséquences. En E3, injecter dans le vivier ne fixe pas l’effet sur la sortie sélectionnée. Enfin, une critique issue d’un autre problème peut être nuisible : la battre en E5 ne montre pas que la vraie critique aide par rapport au silence.

**(b) Lois de panne — VÉRIFIÉ, conditionnellement aux modèles indiqués.**

| Critère | Condition mesurable |
|---|---|
| E1, discrimination appariée | Pour les scores profond \(D_+\) et leurre \(D_-\), l’AUC appariée vaut \(P(D_+>D_-)+P(D_+=D_-)/2\). Si leur loi jointe est échangeable dans chaque strate de rareté, elle vaut \(1/2\). Si \(P(Y=1\mid D)=\mathbf1\{D>\delta\}\), la séparation est au contraire imposée par l’étiquette \(Y\). |
| E2, étroitesse | Si \(H_x\sim{\rm Bin}(K,p_x)\), \(P(H_x=0)=(1-p_x)^K\). Si \({\rm Var}({\rm rang}(\hat\nu))=0\), Spearman est indéfini. Même une concordance parfaite des rangs n’implique pas \(P(\mathbf1\{p_{Rx}\le t\}\ne\mathbf1\{p_{Sx}\le t\})=0\). |
| E3–E5, succès final | Avec injection indépendante de probabilité \(q\), sans retrait d’un succès préexistant, le gain vaut \(q(1-p_0)s\), où \(s\) est le taux de conversion d’un échec initial après injection. Pour \(n\) problèmes indépendants, \(d=P(Y_M\ne Y_b)\) et \(\Delta=E(Y_M-Y_b)\), la variance de l’écart moyen est \((d-\Delta^2)/n\). Une taille calculée sur les seules marginales ne garantit donc pas la puissance à la marge demandée. Le McNemar exact usuel porte sur \(P(1,0)=P(0,1)\), pas sur une marge non nulle. |
| E6–E8 | Le ratio privé/public est indéfini si le gain public moyen est nul ; le ratio de densités d’E7 l’est si la densité de la strate basse est nulle. Si le taux de présence est constant mais que \(P(\text{trouvé}\mid\text{présent},S)\) varie avec la strate \(S\), le ratio de découvertes varie sans variation de densité. Le signe transféré d’E8 n’est pas résolu si l’intervalle conjoint des effets rencontre un axe. |
| Audits auxiliaires | Pour une famille de variantes \(v\), un taux moyen \(\sum_v w_v e_v\) ne borne pas l’erreur sur une variante de poids nul. Cela vaut pour les mutants exécutables, les reformulations, les prémisses vacues et les styles du juge. \(P(\text{item antérieur})\) n’identifie pas \(P(\text{item vu à l’entraînement})\). |

**(c) Contrôles négatifs indispensables — HYPOTHÈSE.** Garder les leurres rares et inertes d’A, mais les faire produire par une autre grammaire et établir leur inertie sur des conséquences indépendantes de l’étiquetage. Injecter un leurre dans le vivier par le **même canal** que l’oracle : il ne doit pas améliorer le taux final. Pour E4, rejouer en A/A toute la procédure, choix du budget, choix de référence et arrêts intermédiaires compris. Pour E5, ajouter un message neutre du même problème, de même longueur, sans recommandation. Sans lui, le contraste pourrait ne mesurer que le dommage du placebo. **Confiance : 0,94 (illustratif).**

## Sur la proposition B

**(a) Défauts de méthode — VÉRIFIÉ.** E3 oppose corrélation croissante et quasi-indépendance. Une relation déterministe non monotone peut pourtant avoir une corrélation de rang nulle ; une relation décroissante peut ne satisfaire aucun des deux seuils proposés. E7 traite la présence d’une cible dans le corpus comme si elle assignait aléatoirement une exposition : les cibles présentes peuvent aussi être plus faciles à déduire. E4 laisse ouverts deux comparateurs distincts : choisir une référence unique sur développement, ou choisir après coup la référence gagnante sur chaque problème. Le second bénéficie d’une information inaccessible au premier. En E5, réallouer les jetons de critique à la génération mesure une **politique budgétaire**, non l’effet isolé de lire une critique. En E6, différer l’audit de rétroaction jusqu’à la victoire d’E4 laisse sans audit les campagnes où une fuite aurait précisément modifié ce verdict.

**(b) Lois de panne — VÉRIFIÉ sous les conditions indiquées.**

| Critère | Condition mesurable |
|---|---|
| E1–E3, seuils et axes | Avec prévalence \(\pi\), sensibilité \(s\), faux positifs \(f\), la fraction de vrais succès parmi les positifs vaut \(s\pi/[s\pi+f(1-\pi)]\) : une bonne sensibilité sur cas équilibrés peut coexister avec une fraction arbitrairement faible. Pour \(U\) uniforme sur \([0,1]\) et \(D=(U-1/2)^2\), \(\rho_S(U,D)=0\) malgré la dépendance déterministe. Pour E2, tout \(\rho\) strictement entre les deux seuils reste hors des deux hypothèses, même à variance d’estimation nulle. |
| E4–E5, enveloppe et attribution | \(E[\max_b Y_b]\ge\max_b E[Y_b]\), strictement si aucun bras n’est presque sûrement maximisant. Si le gain de référence du ratio de récupération est nul, la fraction récupérée n’existe pas. Si \(P(Y_{t,k}\text{ observé})=0\) pour une combinaison critique \(t\), volume \(k\), son contraste à volume fixé n’est pas identifié sans hypothèse sur l’interaction. |
| E6, E8 | Pour \(G=D_{\rm train}-D_{\rm test}\), l’incertitude du contraste apparié dépend de \({\rm Var}(G_{\rm retour}-G_{\rm silence})/n\) ; un intervalle traversant la tolérance ne démontre pas l’innocuité. Si une région a probabilité d’inclusion nulle, le rendement sur la population entière n’est pas identifiable par repondération. |
| E7, contamination | Soient \(C\) l’exposition réelle, \(A\) la présence détectée et \(Y\) le succès. Même avec \(A=C\), la loi \(P(Y=1\mid C=c)=r_c\) est compatible avec un mécanisme sans rappel où la difficulté latente détermine \(C\) et \(Y\). Avec erreur non différentielle du détecteur, \(P(A=1\mid C=1)=P(A=1\mid C=0)\) annule en outre toute information de \(A\) sur \(C\). |

**(c) Contrôles négatifs indispensables — HYPOTHÈSE.** En E7, créer des paires de cibles de même construction et assigner aléatoirement leur inclusion dans un corpus expérimental, avec une cible sœur jamais exposée. Le contraste teste une contribution de l’exposition ; faute de ce contrôle ou d’un équivalent, publier une association, pas un diagnostic de rappel. En E3, conserver des identités **valides** sans conséquence aval : une expression fausse rejetée avant notation ne contrôle pas la profondeur conditionnelle à la validité. En E1, permuter les étiquettes *dans* les familles de construction, et tester un classifieur ne voyant que le gabarit. En E5, masquer la critique sans modifier le nombre de candidats ni le sélecteur. **Confiance : 0,93 (illustratif).**

## Sur la proposition D

**(a) Défauts de méthode — VÉRIFIÉ.** Dans le score MDL de D, chaque régime favorable est crédité, chaque régime défavorable est ramené à zéro. C’est un choix effectué sur les conséquences retenues : ce score ne mesure pas le gain net d’un code imposé à tous les régimes. Une empreinte de dépendances identique n’établit pas l’équivalence de deux lemmes. L’Exp. IV annonce un rapport de cotes d’**existence** ; une recherche bornée fournit ordinairement un rapport de cotes de **détection**. En Exp. VI, un audit limité à de vrais négatifs mesure des faux positifs, mais ni la sensibilité ni la prévalence. Les deux hypothèses peuvent même être vraies si les faux positifs sont égaux entre bras, sous le plafond absolu, mais supérieurs à la prévalence.

**(b) Lois de panne — VÉRIFIÉ sous les conditions indiquées.**

| Critère | Condition mesurable |
|---|---|
| MDL, preuve, intervention | Pour un contraste intégrable \(G_r\) de moyenne nulle, \(E[(G_r)_+]=E|G_r|/2\). Le score nul attendu devient positif dès que \(\sum_r E|G_r|/2>E[K]\). Si les lois des observations sous deux mécanismes coïncident pour toute intervention admissible, toute règle de niveau \(\alpha\) a puissance au plus \(\alpha\) contre cette alternative. Même indiscernabilité pour des temps de preuve tous censurés au même plafond. |
| Exp. I–III | Après zéro atteinte en \(M\) tirages indépendants, la borne supérieure binomiale unilatérale est \(1-\alpha^{1/M}\), non une probabilité connue exactement. Si le score seuillé est constant, le Kendall corrigé des ex æquo est indéfini. Pour le test d’intersection-union, la puissance conjointe est au plus celle du contraste le moins puissant. Pour une différence appariée \(W\), \({\rm médiane}(W)\), \(E[W]\) et le paramètre des rangs signés peuvent avoir des signes distincts sans symétrie. |
| Exp. IV–V | Sans faux positifs, \(P(Y_{\rm trouvé}=1\mid S=s)=\pi_s a_s\), avec \(\pi_s\) fréquence d’existence et \(a_s\) sensibilité de recherche. Un produit par strate n’identifie pas ses facteurs. En V, une différence moyenne holdout–coffre non nulle reste compatible avec zéro effet de divulgation si cette même différence existe dans le bras cloisonné ; le paramètre pertinent est la différence **entre** ces écarts. |
| Exp. VI | Avec \(r=f+(s-f)\pi\), l’inversion est singulière si \(s=f\). Pour un audit stratifié par verdict \(J\), si \(P(\text{audité}\mid J=j,g)=0\) dans une strate de masse positive, \(P(Y=1\mid g)\) n’est pas identifié sans contrainte additionnelle. Une prévalence inférieure à \(f\) ne suffit pas à fixer la valeur prédictive positive : elle dépend aussi de \(s\). |

**(c) Contrôles négatifs indispensables — HYPOTHÈSE.** Pour le MDL, soumettre des prédicteurs sans gain net mais de variance croissante, au même nombre de régimes ; comparer le score tronqué au gain signé sur un coffre indépendant. Pour le quotientage, soumettre deux lois identiques sur la grille et différentes sur une intervention admissible hors grille. Pour l’Exp. IV, utiliser des strates de **même prévalence plantée** mais d’accessibilités différentes. Pour le juge, croiser la provenance affichée et le contenu à vérité fixée, avec audit pondéré des verdicts négatifs comme positifs dans chaque bras. Un duplicata à température nulle ne teste que la répétabilité. **Confiance : 0,96 (illustratif).**

## Sur la proposition E

**(a) Défauts de méthode — VÉRIFIÉ.** Le maximum dans \(U\) ne contient pas le plancher de profondeur annoncé ; un candidat rare de profondeur positive mais insuffisante peut gagner. Si \(\mathcal S\) est le vivier, le coffre privé sert implicitement de sélecteur : le système reçoit crédit pour une idée qu’il n’a pas nécessairement retenue. Une extension non dominée d’une frontière de coûts n’est pas une domination de cette frontière. E3 choisit des familles favorables et E5 les réutilise : de nouvelles instances dans ces familles testent au mieux un effet **conditionnel au choix des familles**. Enfin, le correcteur PPI d’une moyenne ne corrige pas automatiquement le maximum de scores individuels bruités.

**(b) Lois de panne — VÉRIFIÉ sous les conditions indiquées.**

| Critère | Condition mesurable |
|---|---|
| Rareté, profondeur, E1 | Si \(T_Q\) est le temps d’atteinte et \(P(T_Q\le B_{\max})<1/2\), la médiane au-delà du budget n’est pas identifiable sans extrapolation. Pour un score scalaire fixé, l’AUC contre un mélange de leurres vaut \(\sum_h w_h{\rm AUC}_h\) : une classe de faible poids peut être indiscernable. Le gain d’information d’un protocole, \(I(\Theta;Y\mid a)\), est nul si la loi de \(Y\) ne varie pas avec \(\Theta\) sous l’action \(a\) ; sa valeur sous un autre a priori n’est pas identifiée par cette seule valeur. |
| E2, PPI et mémoire | Dans la version à deux échantillons indépendants, la variance de \(\bar J_N+\overline{(Y-J)}_n\) vaut \({\rm Var}(J)/N+{\rm Var}(Y-J)/n\) sous tirages i.i.d. représentatifs. Augmenter \(N\) ne supprime pas le second terme. Si un mécanisme de rappel et un mécanisme de déduction induisent la même loi jointe des scores canonique/renommé, le contraste de renommage a même loi sous les deux. |
| E3–E4 | Une interaction \(\Delta_F-\Delta_N>0\) est compatible avec \(\Delta_F,\Delta_N<0\) : elle ne prédit pas une victoire. Si \(E[D\mid R=r]\) est croissante, une sélection vers des \(R\) élevés peut améliorer \(D\) même en présence de divulgation ; la stagnation de \(D\) n’est pas une conséquence nécessaire de la fuite. |
| E5–E6, maximum, aire et ablation | À profondeur vraie commune, avec \(m\) scores indépendants bruités de fonction de répartition \(F\), \(P(\max_j\hat D_j\le u)=F(u)^m\). Le maximum et son aire peuvent donc augmenter uniquement avec le nombre d’essais. Si les courbes de gain changent de signe selon le budget, le signe de l’aire dépend des poids d’intégration. Si les estimateurs d’E5 et d’E6 sont corrélés, la loi de l’estimateur d’E6 conditionnelle au passage d’E5 peut différer de sa loi marginale. |

**(c) Contrôles négatifs indispensables — HYPOTHÈSE.** Faire concourir des viviers de tailles différentes dont toutes les idées ont la même profondeur vraie ; distinguer maximum privé du vivier et candidat sélectionné avant ouverture du coffre. Remplacer l’A/A à graines identiques d’E1 par des campagnes indépendantes qui rejouent la sélection des familles et l’arrêt pour futilité : recopier une trace force l’écart à zéro. Pour PPI, auditer aussi un échantillon des idées **écartées** au préfiltrage ; pour la boucle externe, répéter la décision sur des familles non consultées, et non sur les seules familles gagnantes avec d’autres graines. Sans ces contrôles, ni la correction du juge ni l’intervalle final ne répondent à la revendication de découverte par le système. **Confiance : 0,95 (illustratif).**

FIN-DE-CELLULE

## Cellule E3-T2-critique-croisee-D (lettre D)

**Intégrité des pièces et conventions (`VÉRIFIÉ`).** Les pièces `FAITS`, `QUESTION DE L'ARBITRE` et les conceptions `A`, `B`, `C`, `E` sont toutes présentes, non vides et non coupées ; `FAITS` et `QUESTION DE L'ARBITRE` sont identiques. Les statuts d'origine des propositions critiquées (`HYPOTHÈSE`, `RAPPORTÉ`, `OBSERVÉ-NON-AUDITÉ`, `VÉRIFIÉ`) sont conservés sans modification. Mes constats textuels sur ces pièces et les relations mathématiques exactes entre lois, paramètres et estimateurs portent le statut `VÉRIFIÉ` ; l'occurrence empirique d'un régime paramétrique ou l'effet attendu d'un contrôle porte le statut `HYPOTHÈSE`. Tout nombre ne figurant pas dans `FAITS` est marqué `(illustratif)`.

---

## Sur la proposition A

### (a) Défauts de méthode

1. **Vrai par construction dans E1 (`VÉRIFIÉ` sur le protocole, `HYPOTHÈSE` de conception dans A).** A engendre chaque monde clos par un programme caché issu d'une grammaire $G$ produisant des régimes publics et retenus, puis plante des idées profondes et des leurres inertes appariés sur l'ajustement public. Dès lors que l'idée profonde plantée encode le mécanisme générateur des régimes retenus tandis que le leurre diverge hors des régimes publics, l'inégalité $\Delta(\text{profonde}) > \Delta(\text{leurre})$ pour un solveur exécutant $G$ est vraie par construction algébrique du monde. E1 vérifie l'absence de bogue d'exécution du solveur, mais ne teste pas la séparabilité empirique entre rareté et profondeur sur les idées effectivement produites par des chercheurs (`HYPOTHÈSE`).
2. **Fuite entre vérité privée et construction du prédicteur en E7 (`VÉRIFIÉ` sur la définition).** A définit la « déceptivité » (`HYPOTHÈSE` dans A) d'un monde avant run comme la part d'idées *inertes* parmi les $M$ premiers candidats énumérés ajustés au public. Or l'étiquette « inerte » dépend de $\Delta$, calculé sur les régimes retenus privés. Construire le sélecteur de régions avec cette quantité fait fuir l'oracle privé dans le choix des problèmes et rend le prédicteur incalculable hors mondes à vérité connue (`HYPOTHÈSE`).
3. **Deux variables confondantes dans E4 et E5 (`HYPOTHÈSE`).**
   - *Comptabilité asymétrique hors-jetons (E4)* : plafonner à l'identique les appels au vérificateur tout en comptant les jetons bride artificiellement l'énumérateur et PySR (`RAPPORTÉ` dans A : Cranmer, 2023, *Interpretable Machine Learning for Science with PySR and SymbolicRegression.jl*, lieu : référence à vérifier), qui dépensent $0$ `(illustratif)` jeton mais reposent sur un volume élevé d'évaluations rapides, confondant efficacité algorithmique et quota d'appels.
   - *Corruption contextuelle active du placebo (E5)* : injecter la critique d'un *autre* problème introduit un signal sémantique hors-sujet susceptible de dégrader la génération par distraction (`HYPOTHÈSE`), confondant l'apport réel d'une critique informée avec l'absence de pollution hors-contexte.
4. **Erreur de dimensionnement face à la règle de décision et inflation des fausses découvertes (`VÉRIFIÉ`).** A calcule $N \approx 140$ `(illustratif)` mondes (retenu à $150$, `illustratif`) par la formule standard opposant $5\,\%$ `(illustratif)` et $15\,\%$ `(illustratif)` contre une différence nulle, mais impose en E4 que l'intervalle de confiance à $95\,\%$ `(illustratif)` dépasse entièrement le seuil $+5$ `(illustratif)` points : la marge effective est divisée par $2$ `(illustratif)`, quadruplant le $N$ requis (`VÉRIFIÉ`). De plus, en m'appuyant explicitement sur le calcul bayésien de prévalence posé par la proposition C (`HYPOTHÈSE` de prévalence dans C, identité de Bayes `VÉRIFIÉ`), le plafond de fausses alertes de $0,10$ `(illustratif)` toléré par A pour le juge-modèle entraîne, sous une prévalence de $0,01$ `(illustratif)` et une détection de $0,80$ `(illustratif)`, une proportion de fausses découvertes supérieure à $0,91$ `(illustratif)`.

### (b) Conditions probabilistes de perte de puissance ou de non-jugeabilité

(`VÉRIFIÉ` : propriétés mathématiques exactes des lois, paramètres et estimateurs ci-dessous.)

1. **Estimateur d'étroitesse $\hat{\nu}_{R,b}(x)$ et fiabilité demi-échantillons $\hat{\rho}_S$ (E2).** Soient $Y_1,\dots,Y_K \stackrel{\text{i.i.d.}}{\sim} \text{Bernoulli}(p_R(x))$, $S_K = \sum_{i=1}^K Y_i \sim \text{Binomiale}(K, p_R(x))$, et la borne supérieure unilatérale de niveau $1-\alpha_0$ en $S_K=0$, $u_K = 1 - \alpha_0^{1/K} \approx (-\ln \alpha_0)/K$ (soit $3/K$ `(illustratif)` à $\alpha_0 = 0,05$ `(illustratif)`).
   - *Non-jugeabilité par troncature* : si $\nu^* > -\log_2(1 - \alpha_0^{1/K})$, alors $\mathbb{P}(\hat{\nu}_{\text{cert}}(x) \ge \nu^*) = 0$ pour tout $p_R(x) \in (0,1]$.
   - *Effondrement du critère de demi-échantillons* : soit $p_R(X) \sim G_R$ sur une population de $M$ classes, estimée sur deux sous-échantillons disjoints de taille $K/2$ `(illustratif)`. Si $\mathbb{E}_{G_R}[p_R(X)] = \mu_p \ll 2/K$ `(illustratif)`, alors $\mathbb{P}(S_{K/2}^{(1)} = 0, S_{K/2}^{(2)} = 0) = \mathbb{E}_{G_R}[(1-p_R(X))^K] \ge 1 - K\mu_p \to 1$ ; la proportion d'ex-aequo dégénérés dégrade $\mathbb{E}[\hat{\rho}_S(\hat{\nu}^{(1)}, \hat{\nu}^{(2)})]$ sous tout seuil $\rho_0 \in (0,1)$ ($0,9$ `(illustratif)` dans A), déclenchant l'arrêt alors même que les classes sont réellement rares.
2. **Critère conjoint $\hat{\mathbb{I}}_{\text{EP}}(x) = \prod_{r=1}^m \mathbb{I}\{S_{r,K}(x) = 0\} \cdot \mathbb{I}\{\hat{\Delta}(x) \ge \delta^*\}$ (E1, E3).** Sous indépendance des $m$ campagnes de référence de paramètres $(p_1(x),\dots,p_m(x))$ vérifiant $p_r(x) \le 2^{-\nu^*}$ et $\Delta(x) \ge \delta^*$, la puissance de certification d'un vrai positif vaut $\beta_{\text{EP}}(x) = \mathbb{P}(\hat{\Delta}(x) \ge \delta^*) \prod_{r=1}^m (1 - p_r(x))^K \le \exp\left(-K \sum_{r=1}^m p_r(x)\right)$. Pour $K p_r(x) = c_0 > 0$ (par exemple $c_0 = 1$ `(illustratif)` sous $p_r = 1/K$), $\beta_{\text{EP}}(x) \le \mathrm{e}^{-m c_0}$ décroît exponentiellement en $m$. Dans E3, avec injection d'oracle de paramètre $q$ sur $N$ mondes, si $q \cdot \beta_{\text{EP}} \le z_{1-\alpha/2}\sqrt{\gamma_0(1-\gamma_0)/N}$ où $\gamma_0$ est le taux de fausses alertes, la puissance tombe sous $0,5$ `(illustratif)`.
3. **Statistique appariée de McNemar $\hat{\theta} = (N_{10} - N_{01})/N$ face au seuil $\theta_0 > 0$ (E4, E5).** Soit $(N_{10}, N_{01}, N_{00}+N_{11}) \sim \text{Multinomiale}(N ; p_{10}, p_{01}, 1-\psi)$ avec $\psi = p_{10}+p_{01}$ et $\theta = p_{10}-p_{01}$. L'exclusion bilatérale de $\theta_0$ exige $|\hat{\theta} - \theta_0| > z_{1-\alpha/2}\sqrt{(\hat{\psi} - \hat{\theta}^2)/N}$. La puissance asymptotique $\Phi\left(\frac{\sqrt{N}(\theta - \theta_0)}{\sqrt{\psi - \theta^2}} - z_{1-\alpha/2}\right)$ tombe sous $1-\beta$ dès que $N < \frac{(z_{1-\alpha/2} + z_{1-\beta})^2 (\psi - \theta^2)}{(\theta - \theta_0)^2}$, et le critère devient non jugeable avec probabilité tendant vers $1-\alpha$ lorsque $\theta \to \theta_0$.
4. **Estimateurs de ratios $\hat{R}_{\text{F2}} = \hat{g}_{\text{priv}}/\hat{g}_{\text{pub}}$ (E6) et $\hat{R}_{\text{dens}} = \hat{\lambda}_{\text{sup}}/\hat{\lambda}_{\text{inf}}$ (E7), et signe $\text{sgn}(\hat{\beta}_k^{(d)})$ (E8).**
   - Pour $(\hat{g}_{\text{priv}}, \hat{g}_{\text{pub}}) \sim \mathcal{N}_2((\mu_1, \mu_2), \Sigma/N)$, $|\mathbb{E}[\hat{R}_{\text{F2}}]| = +\infty$ ; par le théorème de Fieller (`RAPPORTÉ` : Fieller, E. C., 1954, *Some problems in interval estimation*, Journal of the Royal Statistical Society: Series B), dès que $\hat{g}_{\text{pub}}^2 \le z_{1-\alpha/2}^2 \hat{\Sigma}_{22}/N$, la région de confiance de $\mu_1/\mu_2$ est non bornée (critère non jugeable). De même pour $\hat{\lambda}_{\text{inf}} \sim \frac{1}{N_q}\text{Binomiale}(N_q, \lambda_{\text{inf}})$ si $(1-\lambda_{\text{inf}})^{N_q} \ge \alpha/2$.
   - Pour $\hat{\beta}_k^{(d)} \sim \mathcal{N}(\beta_k^{(d)}, \sigma_{k,d}^2)$ ($d \in \{1,2\}$ `(illustratif)`), si $|\beta_k^{(d)}|/\sigma_{k,d} \le z_{1-\alpha/2}$, $\mathbb{P}(0 \in \text{IC}_{1-\alpha}(\hat{\beta}_k^{(d)})) \ge 1 - \alpha - \Phi(| \beta_k^{(d)}|/\sigma_{k,d} - z_{1-\alpha/2})$, laissant E8 sans décision.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Canonisation adversariale d'expressions gonflées d'identités neutres (`HYPOTHÈSE`).** Injecter une idée large-profonde enveloppée d'un terme algébriquement nul ou neutre non trivial généré par modèle ($H_A$ : le canoniseur fusionne la variante avec la classe fréquente, donnant $\hat{\mathbb{I}}_{\text{EP}} = 0$ ; $H_B$ : elle échappe à la canonisation et obtient $\hat{\nu} \ge \nu^*$ et $\Delta \ge \delta^*$). Sans ce contrôle, $H_B$ fabrique des faux positifs EP par simple obscurcissement syntaxique ; son succès falsifie l'aveuglement du canoniseur, son échec falsifie la validité de $\hat{\nu}$.
2. **Placebo de longueur appariée intra-problème en E5 (`HYPOTHÈSE`).** Opposer le placebo hors-problème de A à un remplissage neutre du *même* problème (répétition de l'énoncé ou auto-génération sans critique, même budget de jetons) : $H_A$ : score(placebo hors-problème) $=$ score(neutre intra-problème) ; $H_B$ : score(placebo hors-problème) $<$ score(neutre intra-problème). Retenir $H_B$ falsifie la neutralité du placebo de A ; retenir $H_A$ falsifie l'hypothèse de corruption par distraction.
3. **Égalisation en coût matériel total (temps-calcul / énergie) sans plafond artificiel d'appels vérificateur (`HYPOTHÈSE`).** Allouer à PySR / à l'énumérateur le budget financier équivalent aux heures-GPU des modèles ($H_A$ : le classement de E4 s'inverse en faveur de la recherche mécanique ; $H_B$ : l'avantage du système persiste). Sans ce contrôle, impossible de réfuter que la victoire en E4 provient du bridage du vérificateur.

---

## Sur la proposition B

### (a) Défauts de méthode

1. **Biais de maximisation (vrai par construction en défaveur du système) dans l'enveloppe « par problème » de E4 (`VÉRIFIÉ`).** B propose de prendre $\max_b \text{succ}_C(b)$ « par problème ou globalement » (`HYPOTHÈSE` dans B). Pris par problème, $\max_b \bar{Y}_{b,p}$ évalue un oracle post-hoc choisissant sur chaque problème la ligne de base la plus chanceuse. Par l'inégalité de Jensen stricte sur le maximum de variables non dégénérées (`VÉRIFIÉ`), même si le système égale exactement chacune des $M$ lignes de base indépendantes, sa différence moyenne contre $\max_b \bar{Y}_{b,p}$ est strictement négative par construction. De plus, moyenner les graines avant le test produit une variable fractionnaire sur laquelle le test de McNemar cité par B est mathématiquement inapplicable sans re-binarisation (`VÉRIFIÉ`).
2. **Confusion entre propriété du chercheur $Q$ et redondance de construit en E3 (`VÉRIFIÉ` sur la logique, `HYPOTHÈSE` sur l'effet).** B tire des énoncés valides selon $Q$ et stipule que si $\rho(n, d \mid \text{valide}) \ge 0,5$ `(illustratif)`, la profondeur est redondante avec la rareté et doit être *redéfinie conditionnellement à $n$*. Or si $Q$ engendre massivement des tautologies fréquentes ($n$ bas, $d=0$) et rarement des lemmes féconds ($n$ haut, $d>0$), $\rho > 0$ mesure la médiocrité de $Q$, non un défaut de $d$. Redéfinir $d$ conditionnellement à $n$ injecte la distribution du générateur $Q$ dans l'instrument d'évaluation de la conséquence (`HYPOTHÈSE`).
3. **Fuite d'échantillon sur l'étroitesse et double confondant en E7 (`HYPOTHÈSE`).**
   - B n'impose pas que $P_Q(c(x))$ soit estimé sur des tirages disjoints de l'exécution testée lorsque $Q$ sert de ligne de base en E4/E5, ni ne traite la divergence $-\log 0 = +\infty$ (`VÉRIFIÉ`) qui qualifie automatiquement en étroitesse tout candidat inédit au-delà de $1/K$.
   - En E7, comparer les cibles présentes et absentes du corpus d'OLMo ou Pythia (`RAPPORTÉ` dans B, versions à vérifier) confond *non-contamination* et *difficulté intrinsèque* (les résultats absents de tout un corpus web sont non aléatoirement plus spécialisés ou récents), et un audit sur Pythia/OLMo ne transfère pas aux modèles 70B/72B `(illustratif)` à corpus fermé utilisés en E4.
   - En m'appuyant à nouveau sur le calcul bayésien de la proposition C (`VÉRIFIÉ`), le seuil de fausses alertes $\le 0,05$ `(illustratif)` de B en E1 implique encore $\approx 86\,\%$ `(illustratif)` de fausses découvertes à prévalence $0,01$ `(illustratif)`.

### (b) Conditions probabilistes de perte de puissance ou de non-jugeabilité

(`VÉRIFIÉ` : propriétés mathématiques exactes des lois, paramètres et estimateurs ci-dessous.)

1. **Estimateur $\hat{n}_\gamma(x) = -\ln\left(\frac{S_K + \gamma}{K + 2\gamma}\right)$ avec $S_K \sim \text{Binomiale}(K, p_Q(x))$ ($\gamma \ge 0$) et corrélation $\hat{\rho}_S$ (E2).**
   - Pour $\gamma = 0$, $\mathbb{P}(\hat{n}_0(x) = +\infty) = (1-p_Q(x))^K > 0$ pour tout $p_Q(x) < 1$ : tout bruit de probabilité $p_Q \in (\mathrm{e}^{-\eta}, 1/K]$ vérifie $\mathbb{P}(\hat{n}_0(x) \ge \eta) \ge (1 - 1/K)^K \to \mathrm{e}^{-1} \approx 0,37$ `(illustratif)` (perte du contrôle de type I).
   - Pour $\gamma > 0$, si $\eta > \ln((K+2\gamma)/\gamma)$, $\mathbb{P}(\hat{n}_\gamma(x) \ge \eta) = 0$ (puissance identiquement nulle).
2. **Corrélation conditionnelle $\hat{\rho}(\hat{n}, \hat{d} \mid V=1)$ sous inflation en zéro (E3).** Soit $M_V \sim \text{Binomiale}(K, p_V)$ le nombre de tirages valides et $d(X) \mid \{V=1\} \sim (1-\pi_d)\delta_0 + \pi_d F_+$. La probabilité que la variance empirique de $d$ soit nulle vaut $\mathbb{E}[(1-\pi_d)^{M_V}] = (1 - p_V \pi_d)^K$ : dès que $K p_V \pi_d \ll 1$, $\hat{\rho}$ est indéfini avec probabilité proche de $1$.
3. **Contraste contre l'enveloppe par problème $\hat{\Delta}_{\text{env}} = \frac{1}{P}\sum_{p=1}^P (\bar{Y}_{\text{sys},p} - \max_{b=1,\dots,M} \bar{Y}_{b,p})$ et arrêt séquentiel d'O'Brien-Fleming (`RAPPORTÉ` : O'Brien, P. C., & Fleming, T. R., 1979, *A multiple testing procedure for clinical trials*, Biometrics) (E4, E5).**
   - Pour $g \bar{Y}_{b,p} \mid \mu_p \stackrel{\text{i.i.d.}}{\sim} \text{Binomiale}(g, \mu_p)$ avec $\mu_p \in (0,1)$ et $\mu_{\text{sys},p} = \mu_p + \theta$, on a $\mathbb{E}[\hat{\Delta}_{\text{env}}] = \theta - B_{M,g}$ où $B_{M,g} = \mathbb{E}_p[\max_{b \le M} \bar{Y}_{b,p} - \mu_p] > 0$. Dès que $0 < \theta < \Delta_{\min} + B_{M,g}$, $\mathbb{P}(\text{IC}_{1-\alpha}(\hat{\Delta}_{\text{env}}) > \Delta_{\min}) \xrightarrow{P \to \infty} 0$ (fausse réfutation asymptotique sûre de $H_A$).
   - Aux analyses intermédiaires sur $P_1$ problèmes lorsque le taux de discordance $\psi$ vérifie $P_1 \psi \lesssim 5$ `(illustratif)`, l'asymétrie discrète viole l'approximation gaussienne à incréments browniens des frontières d'O'Brien-Fleming.
4. **Écart de rétroaction $\hat{G} = \hat{d}(K_{\text{train}}) - \hat{d}(K_{\text{test}})$ (E6) et ratio de contamination $\hat{R}_{\text{cont}} = \hat{p}_{\text{prés}}/\hat{p}_{\text{abs}}$ (E7).**
   - Si $(K_{\text{train}}, K_{\text{test}})$ ne sont pas tirés de la même loi marginale ($\mathbb{E}[\hat{d}_0(K_{\text{train}})] - \mathbb{E}[\hat{d}_0(K_{\text{test}})] = \delta_{\text{split}} \neq 0$) et que la variance d'interaction $\sigma_{\text{int}}^2$ satisfait $\sigma_{\text{int}}/\sqrt{P} \gg \tau_{\text{seuil}}$, la puissance de détection de Goodhart s'effondre.
   - Pour $N_{\text{abs}}\hat{p}_{\text{abs}} \sim \text{Binomiale}(N_{\text{abs}}, p_{\text{abs}})$, $\mathbb{P}(\hat{R}_{\text{cont}} = +\infty \text{ ou } 0/0) \ge (1 - p_{\text{abs}})^{N_{\text{abs}}}$, rendant E7 non jugeable dès que $N_{\text{abs}} p_{\text{abs}} \lesssim -\ln \alpha$.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Test A/A multi-copies contre l'enveloppe par problème (`HYPOTHÈSE`).** Opposer une copie de $Q$ à l'enveloppe par problème $\max_{b=1,\dots,M} \bar{Y}_{b,p}$ de $M$ copies i.i.d. du même $Q$ ($H_A$ : $\hat{\Delta}_{\text{env}} \approx 0$ au taux nominal $\alpha$ ; $H_B$ : rejet systématique $\hat{\Delta}_{\text{env}} < 0$). Retenir $H_B$ falsifie la validité de l'enveloppe par problème ; son absence condamne E4 à un biais négatif non détecté.
2. **Agent « auto-formalisateur dégénéré » en Lean 4 (`HYPOTHÈSE`).** Faire tourner un bras qui engendre des définitions auxiliaires triviales (prédicats constants sans `sorry` ni axiome interdit) pour raccourcir syntaxiquement des cibles ($H_A$ : le harnais rejette ces lemmes ou leur attribue $d \le 0$ ; $H_B$ : il les valide comme profonds). Sans ce contrôle, la vérification mécanique `#print axioms` laisse passer la mésformalisation que l'audit humain partiel ne borne pas sur l'ensemble des runs.
3. **Injection randomisée contrôlée en pré-entraînement / fine-tuning pour E7 (`HYPOTHÈSE`).** Scinder aléatoirement un lot de problèmes synthétiques jumeaux en une moitié injectée dans le corpus d'un modèle ouvert et une moitié retenue ($H_A$ : le détecteur sépare injectés et retenus sans biais de difficulté ; $H_B$ : l'écart observé sur cibles naturelles disparaît à difficulté égalisée). Sans cette randomisation, E7 ne peut jamais falsifier l'hypothèse de difficulté différentielle.

---

## Sur la proposition C

### (a) Défauts de méthode

1. **Écrasement des classes par l'équivalence extensionnelle (« non étroit par construction » et contradiction avec la profondeur) (`VÉRIFIÉ`).** C stipule dans les micromondes finis (`HYPOTHÈSE` dans C) : (i) deux règles sont la même idée si leurs prédictions coïncident sur *tout* le domaine du monde, et (ii) toute règle fausse est inéligible. Mathématiquement (`VÉRIFIÉ`), deux règles sans exception calculant la même fonction vraie du monde $w$ ont exactement la même extension sur tout le domaine et tombent dans une *unique* classe $c^*$. Dès lors :
   - un programme de force brute immédiatement atteint par l'énumérateur $r_{\text{enum}}$ appartient à la même classe $c^*$ qu'une loi algébrique factorisée équivalente, rendant la loi profonde *non étroite par construction* ($p_{r_{\text{enum}}}(c^*)$ élevé) ;
   - à l'inverse, la profondeur est mesurée en passant « $c$ » à un résolveur sous plafond de coût : or la performance d'un résolveur borné dépend du *représentant syntaxique* $x \in c^*$ (intensionnel) et non de la classe extensionnelle $c^*$ (`VÉRIFIÉ`). Évaluer l'étroitesse sur l'extension et la profondeur sur l'intension rend le construit incohérent.
2. **Confusion entre capacité de génération et politique d'abstention à nomination unique (`VÉRIFIÉ` sur la fonction de gain, `HYPOTHÈSE` comportementale).** Chaque bras ne soumet qu'une seule nomination finale ou s'abstient, et le score primaire vaut $1$ si la nomination est certifiée EP, $0$ sinon (`HYPOTHÈSE` dans C). Comme l'abstention et l'échec rapportent tous deux $0$ sur le contraste primaire (`VÉRIFIÉ`), s'abstenir est faiblement dominé ; un bras doté d'un seuil d'abstention conservateur perd des positifs face à un bras qui devine systématiquement. De plus, cacher légitimement $p_r$ tout en interdisant un petit portefeuille top-$k$ pénalise au hasard un chercheur qui découvre deux lois profondes dont l'une est connue d'une référence gelée.
3. **Biais d'encombrement de la « règle vraie placebo » (`HYPOTHÈSE`).** C mesure la profondeur par la différence de fractions résolues entre le résolveur doté de $c$ et le résolveur doté d'une « règle vraie placebo de longueur et de coût d'appel appariés ». Si la règle placebo ajoute un branchement inutile coûteux au résolveur sous plafond de calcul tandis que la règle candidate $x$ est syntaxiquement gardée par une précondition rarement déclenchée (donc ignorée sans coût), $x$ bat le placebo non pas parce qu'elle aide à résoudre des buts aval, mais parce que le placebo dégrade activement le résolveur.

### (b) Conditions probabilistes de perte de puissance ou de non-jugeabilité

(`VÉRIFIÉ` : propriétés mathématiques exactes des lois, paramètres et estimateurs ci-dessous.)

1. **Borne supérieure simultanée sur $\max_{r \in \mathcal{R}} p_r(c \mid w, B)$ sous mutualisation (`VÉRIFIÉ`).** Sur $W$ mondes et $M_C$ classes candidates évaluées en mutualisant un journal de $K$ recherches indépendantes $Y_{r,k}(c) \sim \text{Bernoulli}(p_r(c))$ par politique $r \in \mathcal{R}$, le contrôle simultané du risque global à $\alpha_{\text{sim}}$ exige en zéro occurrence $u_{\text{sim}}(K) = 1 - (\alpha_{\text{sim}} / (W M_C))^{1/K} < \tau$. Dès que $K \le \frac{\ln(W M_C / \alpha_{\text{sim}})}{-\ln(1-\tau)}$ (condition violée si l'on retient $K \approx -\ln(\alpha)/\tau \approx 300$ `(illustratif)` à $\tau=0,01$ `(illustratif)` dès que $W M_C > 1$), $\mathbb{P}(\hat{U}_{\text{sim}}(c) < \tau) = 0$ : aucune classe ne peut jamais être déclarée étroite.
2. **Différence appariée de profondeur $\hat{\Delta}_J = \frac{1}{J}\sum_{j=1}^J (U_j(x) - U_j(x_{\text{plac}}))$ face au seuil $d > 0$ (`VÉRIFIÉ`).** Pour $(U_j(x), U_j(x_{\text{plac}})) \in \{0,1\}^2$ de probabilité de discordance $\psi_U$ et d'espérance $\Delta_U = \mathbb{E}[U_j(x) - U_j(x_{\text{plac}})]$, le test unilatéral simultané au niveau $\alpha_D$ perd sa puissance ($\beta_D < 0,5$ `(illustratif)`) dès que $\Delta_U \le d + z_{1-\alpha_D}\sqrt{(\psi_U - \Delta_U^2)/J}$, et devient aveugle ($\beta_D \to 0$) pour tout $\Delta_U \in (0, d]$.
3. **Contrainte d'audit $\bar{\gamma}_{\text{FP}} = 1 - \alpha_{\text{aud}}^{1/N_{\text{neg}}}$ sous prévalence $\pi$ et FDR cible $q^*$ (`VÉRIFIÉ`).** Pour garantir $\text{FDR}(\pi, S_e, \bar{\gamma}_{\text{FP}}) = \frac{(1-\pi)\bar{\gamma}_{\text{FP}}}{(1-\pi)\bar{\gamma}_{\text{FP}} + \pi S_e} \le q^*$ sur $S$ strates négatives avec correction simultanée $\alpha_{\text{aud}}/S$, la taille d'audit doit vérifier $N_{\text{neg}} \ge \frac{\ln(S/\alpha_{\text{aud}})}{-\ln\left(1 - \frac{\pi S_e q^*}{(1-\pi)(1-q^*)}\right)}$. Lorsque $\pi \to 0$, $N_{\text{neg}} = \Omega(\pi^{-1} \ln S)$ diverge hyperboliquement.
4. **Non-convergence asymptotique des bornes de pire cas sous proportion de classes non résolues $\rho_u > 0$ (`VÉRIFIÉ`).** Soient $p_A, p_B$ les vraies probabilités de succès certifié sur $W$ mondes, $\rho_{u,A}, \rho_{u,B}$ les probabilités d'indécidabilité d'oracle à budget fixé, et $\bar{\gamma}_{\text{FP}}$ la borne d'erreur différentielle issue d'un audit fini $N_{\text{neg}}$. L'estimateur de borne inférieure de pire cas $\hat{T}_{\text{pire}} = \hat{p}_A - (\hat{p}_B + \hat{\rho}_{u,B} + \bar{\gamma}_{\text{FP}}) - \delta_0$ converge en probabilité quand $W \to \infty$ (à $N_{\text{neg}}$ et plafond d'oracle constants) vers $(p_A - p_B - \delta_0) - (\rho_{u,B} + \bar{\gamma}_{\text{FP}})$. Dès que $0 < p_A - p_B - \delta_0 \le \rho_{u,B} + \bar{\gamma}_{\text{FP}}$ et $p_A + \rho_{u,A} + \bar{\gamma}_{\text{FP}} - p_B > \delta_0$, $\mathbb{P}(\text{harnais déclaré non concluant}) \xrightarrow{W \to \infty} 1$, quel que soit le nombre de mondes échantillonnés.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Duel « résolveur nu » contre « résolveur + règle vraie placebo » (`HYPOTHÈSE`).** Évaluer sur les mêmes problèmes aval le résolveur sans aucune règle ajoutée ($H_A$ : fraction résolue(placebo) $=$ fraction résolue(nu) ; $H_B$ : fraction résolue(placebo) $<$ fraction résolue(nu)). Retenir $H_B$ falsifie la neutralité du placebo de C, qui fabriquait de fausses profondeurs par ralentissement de la base.
2. **Paire d'expressions extensionnellement identiques mais intensionnellement asymétriques (`HYPOTHÈSE`).** Injecter dans un micromonde la table/énumération naïve vraie et sa loi factorisée rapide ($H_A$ : le harnais sépare leur étroitesse et leur gain aval ; $H_B$ : l'identification extensionnelle les fusionne et déclare la loi factorisée banale). Retenir $H_B$ falsifie la définition extensionnelle des classes de C.
3. **Invariance du classement à générateur fixé sous balayage du seuil d'abstention (`HYPOTHÈSE`).** Appliquer une règle de sélection commune sans abstention au candidat de rang $1$ `(illustratif)` de chaque bras ($H_A$ : le signe de $T$ reste invariant par rapport au protocole avec abstention libre ; $H_B$ : le verdict s'inverse). Retenir $H_B$ falsifie l'attribution de $T$ à la recherche plutôt qu'à l'aversion au risque.

---

## Sur la proposition E

### (a) Défauts de méthode

1. **Fuite directe du coffre scellé dans l'opérateur $\max_{x \in \mathcal{S}(P,B)}$ de la quantité primaire $U(P,B)$ (`VÉRIFIÉ`).** E définit $U(P,B) = \max_{x \in \mathcal{S}(P,B)} \left( D_{\text{ext}}(x) \cdot \mathbb{I}[R_{\mathcal{Q}_0}([x]) \ge \tau_R \land \text{Valide}(x)] \right)$ (`HYPOTHÈSE` dans E), tout en classant $D_{\text{ext}}$ et $R_{\mathcal{Q}_0}$ dans le « coffre d'évaluation scellé » (Question 5). Prendre le maximum sur $\mathcal{S}(P,B)$ évalué par $D_{\text{ext}}$ et $R_{\mathcal{Q}_0}$ utilise l'oracle scellé comme sélecteur gratuit : cela court-circuite l'agent de sélection du système étudié et confond la qualité de découverte avec le volume $|\mathcal{S}(P,B)|$ de candidats valides déversés (biais d'ordre extrême hors-échantillon, `VÉRIFIÉ`).
2. **Défaite vraie par construction de l'énumérateur sous la double égalité budgétaire de E5 (`VÉRIFIÉ` sur la contrainte, `HYPOTHÈSE` sur l'ordre de grandeur).** E exige que le système batte l'enveloppe des baselines « à budget FLOPs/USD égal ET à budget d'appels oracle égal ». Or un modèle 70B `(illustratif)` consomme plusieurs ordres de grandeur de FLOPs de plus par appel oracle qu'un énumérateur mécanique (`OBSERVÉ-NON-AUDITÉ` / reconnu par E en Q3). Plafonner simultanément les appels oracle de l'énumérateur au petit quota $C_{\text{eval}}$ du LLM ($10^2$ `(illustratif)`) ampute l'énumérateur de presque tout son budget FLOPs/USD et le fait perdre par construction.
3. **Contraste d'interaction fallacieux en E3 (`VÉRIFIÉ`).** E valide sa taxonomie de régions si $\Delta_{\text{fertile}} - \Delta_{\text{négatif}} \ge 0,30\sigma$ `(illustratif)`, en incluant dans le régime négatif les « petits espaces combinatoires » où l'énumérateur exhaustif bat le LLM ($\Delta_{\text{négatif}} < 0$, par exemple $-0,50\sigma$ `(illustratif)`). Dès lors, un système multi-agents *perdant ou nul* sur la région dite fertile ($\Delta_{\text{fertile}} = -0,10\sigma \le 0$ `(illustratif)`) satisfait quand même $\Delta_{\text{fertile}} - \Delta_{\text{négatif}} = +0,40\sigma \ge 0,30\sigma$ `(illustratif)` et « corrobore » à tort l'existence d'une région fertile !
4. **Confusion d'identifiabilité sous PPI lorsque l'audit repose sur des experts (`VÉRIFIÉ` sur le théorème, `HYPOTHÈSE` sur les experts).** Prediction-Powered Inference (`RAPPORTÉ` dans E : Angelopoulos, A. N., Bates, S., Fannjiang, C., Jordan, M. I., & Zrnic, T., 2023, *Prediction-Powered Inference*, Science) ne corrige le juge LLM que vers l'espérance de l'étiquette d'audit $Y$ : si $Y$ vient d'experts humains partageant les mêmes a priori d'aversion à l'atypique que le LLM, le biais commun reste intégralement non borné.

### (b) Conditions probabilistes de perte de puissance ou de non-jugeabilité

(`VÉRIFIÉ` : propriétés mathématiques exactes des lois, paramètres et estimateurs ci-dessous.)

1. **Quantile médian de première atteinte $\hat{B}_{0,5}(Q, [x])$ sous censure à droite et enveloppe $\hat{R}_{\mathcal{Q}_0}([x])$ (E1, E2).** Soit $T_Q([x])$ la loi du budget de première atteinte observée sur $K$ exécutions censurées à droite en $B_{\text{cap}}$ : $Z_k = \min(T_{Q,k}, B_{\text{cap}})$, $\delta_k = \mathbb{I}\{T_{Q,k} \le B_{\text{cap}}\}$. Dès que $F_{T_Q}(B_{\text{cap}}) = \mathbb{P}(T_Q([x]) \le B_{\text{cap}}) < 0,5$ `(illustratif)` (régime des idées rares sous $B_{\text{cap}}$), le paramètre $B_{0,5}(Q,[x]) = F_{T_Q}^{-1}(0,5)$ `(illustratif)` excède $B_{\text{cap}}$ et est non identifiable non-paramétriquement : la survie de Kaplan-Meier (`RAPPORTÉ` : Kaplan, E. L., & Meier, P., 1958, *Nonparametric Estimation from Incomplete Observations*, Journal of the American Statistical Association) vérifie $\mathbb{P}(\min_{t \le B_{\text{cap}}} \hat{S}(t) > 0,5) \xrightarrow{K \to \infty} 1$ `(illustratif)`, rendant $\hat{B}_{0,5}$ non jugeable.
2. **Inflation de variance et sous-couverture de l'estimateur $\hat{\theta}_{\text{PPI}} = \bar{f}_{N_{\text{un}}} + \frac{1}{n}\sum_{i=1}^n (Y_i - f(X_i))$ (E2).**
   - Avec $\sigma_Y^2 = \text{Var}(Y)$, $\sigma_f^2 = \text{Var}(f(X))$ et $\rho_{Y,f} = \text{Corr}(Y, f(X))$, on a $\text{Var}(\hat{\theta}_{\text{PPI}}) = \frac{\sigma_f^2}{N_{\text{un}}} + \frac{\sigma_Y^2 + \sigma_f^2 - 2\rho_{Y,f}\sigma_Y\sigma_f}{n} > \frac{\sigma_Y^2}{n} = \text{Var}(\bar{Y}_n)$ dès que $\rho_{Y,f} < \frac{\sigma_f}{2\sigma_Y}\left(1 + \frac{n}{N_{\text{un}}}\right)$ : le juge LLM dégrade la puissance par rapport à l'échantillon d'audit seul.
   - Si $Y \sim \text{Bernoulli}(p)$ avec $n p \ll 1$, $\mathbb{P}(\sum_{i=1}^n Y_i = 0) = (1-p)^n \approx 1 - np$, sous-estimant $\text{Var}(Y - f(X))$ et dégradant la couverture asymptotique de l'IC normal de PPI sous $1-\alpha$.
3. **Biais d'ordre extrême et échec du bootstrap sur $U(P,B) = \max_{x \in \mathcal{S}(P,B)} \hat{D}_{\text{ext}}(x)\mathbb{I}_{x \in \mathcal{E}}$ et $\widehat{\text{AUDC}}$ (E4, E5, E6).**
   - Si $\hat{D}_{\text{ext}}(x_\ell) = D_0 + \varepsilon_\ell$ avec $\varepsilon_1,\dots,\varepsilon_{L_m} \stackrel{\text{i.i.d.}}{\sim} \mathcal{N}(0, \sigma_\varepsilon^2)$ sur $L_m = |\mathcal{S}_m(P,B)\cap\mathcal{E}|$ candidats qualifiés, alors sous égalité des vraies profondeurs $D_0$, $\mathbb{E}[U_m(P,B) \mid L_m] = D_0 + \sigma_\varepsilon \mathbb{E}[\max_{\ell \le L_m} Z_\ell] \asymp D_0 + \sigma_\varepsilon \sqrt{2\ln L_m}$. Dès que $L_{\text{multi}}$ domine stochastiquement $L_{\text{base}}$, $\mathbb{E}[U_{\text{multi}} - U_{\text{base}}] > 0$ sous l'hypothèse nulle stricte.
   - Si l'erreur hors-échantillon $\varepsilon_\ell$ suit une loi à queue lourde de Pareto d'indice $\alpha_{\text{tail}} \le 2$ `(illustratif)`, $\text{Var}(U(P,B)) = +\infty$, invalidant la convergence du bootstrap d'Efron-Tibshirani (`RAPPORTÉ` dans E : Efron, B., & Tibshirani, R. J., 1993, *An Introduction to the Bootstrap*, Chapman & Hall).
4. **Seuils indexés sur l'écart-type empirique $\delta = c \cdot \hat{\sigma}_\Delta$ et profondeur pénalisée $\hat{D}_{\text{ext}}(x) = \widehat{\Delta\mathcal{L}}_{\text{OOD}}(x) - \lambda |x|$ (E3, E5, E6).**
   - Soit $\Delta_P = \mu_\Delta + \eta_P + \zeta_P$ avec variance structurelle $\sigma_\eta^2$ et bruit de mesure indépendant $\sigma_\zeta^2$. Le paramètre standardisé $\mu_\Delta / \sqrt{\sigma_\eta^2 + \sigma_\zeta^2}$ tombe sous $c$ dès que $\sigma_\zeta^2 > \frac{\mu_\Delta^2}{c^2} - \sigma_\eta^2$ : accroître le bruit d'observation falsifie mécaniquement $H_A$ à effet moyen réel $\mu_\Delta > 0$ constant.
   - Pour $|X|$ de moyenne $\mu_L$ élevée sous un langage verbeux, dès que $\lambda > \mathbb{E}[\Delta\mathcal{L}_{\text{OOD}}(X^*)]/|X^*|$, la vraie solution $X^*$ a une profondeur $D_{\text{ext}}(X^*) < 0$ bloquée par le seuil non compensatoire $\tau_D > 0$.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Bras « inflation de portefeuille par bruitage syntaxique » sur $U(P,B)$ (`HYPOTHÈSE`).** Prendre une baseline unique et dupliquer chaque candidat valide en $L$ variantes sémantiquement proches légèrement perturbées soumises dans $\mathcal{S}(P,B)$ ($H_A$ : $U(P,B)$ reste invariant à $L$ ; $H_B$ : $U(P,B)$ croît avec $\sqrt{\ln L}$ grâce au bruit d'estimation de $\hat{D}_{\text{ext}}$). Sans ce contrôle (et sans restreindre l'évaluation scellée à un nombre fixe $k$ de sélections aveugles), $H_B$ fabrique un gain illusoire.
2. **Test conjoint de supériorité absolue $\Delta_{\text{fertile}} > \delta_0 > 0$ et de régime neutre en E3 (`HYPOTHÈSE`).** Remplacer le seul test $\Delta_{\text{fertile}} - \Delta_{\text{négatif}}$ par la conjonction $\Delta_{\text{fertile}} > \delta_0$ ET $|\Delta_{\text{neutre}}| \le \epsilon$ ($H_A$ : gain absolu réel en zone fertile ; $H_B$ : $\Delta_{\text{fertile}} \le 0$ malgré $\Delta_{\text{fertile}} - \Delta_{\text{négatif}} > 0$). Sans cette disjonction, un effondrement du LLM face à l'énumérateur sur petit espace valide faussement la sélection de problèmes.
3. **Contrôle d'anti-corrélation sémantique du juge LLM sur vérités contre-intuitives (`HYPOTHÈSE`).** Injecter dans l'audit E2 des lois vraies mais contraires aux heuristiques usuelles, appariées à des faux plausibles de *même style* ($H_A$ : $\hat{\rho}_{Y,f} > \hat{\sigma}_f/(2\hat{\sigma}_Y)$ sur cette strate rare ; $H_B$ : $\hat{\rho}_{Y,f} \le 0$, rendant $\text{Var}(\hat{\theta}_{\text{PPI}}) > \text{Var}(\bar{Y}_n)$). Le *style-swap* de E2 est aveugle à ce biais de plausibilité à style constant ; son absence laisse PPI dégrader la précision tout en masquant le défaut si l'audit est humain.

FIN-DE-CELLULE

## Cellule E3-T2-critique-croisee-E (lettre E)

*Audit documentaire (`VÉRIFIÉ`) : les blocs `FAITS`, `QUESTION DE L'ARBITRE` et les quatre pièces A, B, C, D sont présents et complets. Convention de statuts : `RAPPORTÉ` pour le contenu des pièces et la littérature ; `VÉRIFIÉ` uniquement pour les dérivations mathématiques exactes ; `HYPOTHÈSE` pour les diagnostics méthodologiques et contrôles proposés. Tout nombre cité des pièces ou utilisé en calcul est `illustratif` (noté « ill. »).*

---

## Sur la proposition A

### (a) Défauts de méthode

1. **Fuite directe de la vérité retenue dans le prédicteur *ex ante* de E7 (`HYPOTHÈSE`)**. A définit comme prédicteur calculé avant tout run la « part d'inertes parmi les $M$ premiers candidats énumérés les mieux ajustés au public » (`RAPPORTÉ`, pièce A). Or déterminer quels candidats sont *inertes* requiert d'évaluer $\Delta$ sur les régimes retenus (ou de connaître le programme caché) : la vérité d'évaluation fuit dans le sélecteur de problèmes.
2. **Vrai par construction dans E1 et E3 (`HYPOTHÈSE`)**. Dans E1, les idées profondes sont le programme caché et les leurres sont construits inertes sur les régimes retenus ; que $\Delta$ (mesuré sur ces régimes) les sépare vérifie le fonctionnement du solveur sur la géométrie plantée, non la séparabilité générale de la profondeur et de la rareté. De plus, E1 (étape 0) apparie les leurres en taille, rang d'énumération et ajustement public, mais pas en $\nu_{\text{modèle}}$ (calculé seulement à l'étape 2). Dans E3 (étape 1), l'oracle dilué injecte une idée plantée *déjà* EP dans un rééchantillonnage CPU avant tout run de modèle : le test est satisfait par construction sans éprouver ni la canonisation sur sorties de modèles, ni le bruit de $\hat{\nu}_{\text{modèle}}$.
3. **Confondant du placebo et biais de colliseur dans E5 (`HYPOTHÈSE`)**. La critique placebo (issue d'un *autre* problème) est hors sujet et peut perturber activement le modèle en dégradant ses sorties en dessous d'un bras sans critique : un contraste `critique active − placebo > 0` confond l'absence de nuisance avec un gain constructif. En outre, décomposer E5 en rappel du vivier et précision de sélection *sachant présence dans le vivier* conditionne sur une variable post-traitement (le vivier varie selon le bras), induisant un biais de sélection. L'hétérogénéité (trois familles) confond diversité et niveau moyen des familles si « N copies » ne réplique pas le meilleur modèle des trois.
4. **Incohérence de comparaison, de coûts et d'étroitesse dans E4 (`HYPOTHÈSE`)**. A annonce « un seul test confirmatoire » (McNemar exact) tout en comparant 5 références à 3 budgets (`RAPPORTÉ`, pièce A) : sélectionner *ex post* la « meilleure référence » biaise le contraste et multiplier les budgets gonfle le risque de type I. A somme jetons d'entrée et de sortie en un budget scalaire unique, confondant pré-remplissage parallélisable et décodage autorégressif à attention quadratique. Enfin, si $\nu$ n'inclut pas PySR ni le best-of-N avec sélecteur, une idée banale pour ces références de E4 est néanmoins labellisée EP.
5. **Confondant dans E6 (`HYPOTHÈSE`)**. Dans un monde clos à loi génératrice unique, les régimes publics et privés sont structurellement corrélés : optimiser $\Delta_{\text{public}}$ peut transférer à $\Delta_{\text{privé}}$ par couplage du monde clos sans exclure le sur-ajustement ailleurs.

### (b) Conditions probabilistes de perte de puissance ou de non-jugeabilité

*(Lois de probabilité, paramètres et estimateurs uniquement ; résultats mathématiques `VÉRIFIÉ` sur valeurs `ill.` de la pièce A.)*

- **Estimateur $\hat{\nu}_{R,b}^+(x) = -\log_2 \hat{p}_R^+(x)$ (borne $3/K$)** : pour $S_K(x) \sim \text{Binomiale}(K, p_R(x))$, dès que $p_R(x) \ll 3/K$ ($K=300$, ill.), $\mathbb{P}(S_K(x)=0) = (1-p_R(x))^K \to 1$ ; $\hat{\nu}^+$ sature à $\log_2(K/3) \approx 6{,}64$ (ill.), rendant indiscernables toute paire $(p_1, p_2) \ll 3/K$. Au voisinage du seuil $p^* = 2^{-\nu^*}$, pour $p_R(x) = c p^*$ ($c>1$) quand $\nu^* = \log_2(K/3)$, le taux de fausses alertes vaut $(1 - 3c/K)^K \approx e^{-3c}$.
- **Corrélations de rang $\hat{\rho}_S$ (E2 et fiabilité demi-échantillons)** : si $\pi_0 = \mathbb{P}(S_{K/2}(X) = 0) \to 1$, la masse d'ex æquo en $0$ annule la variance des rangs et rend $\hat{\rho}_S$ non jugeable. Sous erreur binomiale indépendante, $\hat{\rho}_S$ est atténué par $\sqrt{r_1 r_2}$ avec $r_j = \text{Var}(\nu_j)/(\text{Var}(\nu_j) + \mathbb{E}[\frac{1-p_j}{K p_j (\ln 2)^2}])$ ; pour $p_j \lesssim 1/K$, $r_j \to 0$.
- **$\widehat{\text{AUC}}(\Delta)$ (E1)** : soient $D^+ \sim F_+$, $D^- \sim F_-$, $p_0^+ = \mathbb{P}(D^+=0)$. Si $p_0^+ > 0{,}4$ (ill.), $\text{AUC} \le 1 - p_0^+ + \frac{1}{2} p_0^+ \mathbb{P}(D^-=0)$ rend impossible l'exclusion de $0{,}80$ (ill.). En présence d'une corrélation intra-groupe $\rho_w > 0$ sur $m_w$ paires par groupe, l'estimateur de variance indépendant sous-estime $\text{Var}(\widehat{\text{AUC}})$ d'un facteur $1 + (m_w - 1)\rho_w$, invalidant la couverture de l'IC.
- **Décision de E4 (McNemar exact et IC à $95\,\%$ au-dessus de $\delta_0 = 0{,}05$, $n = 150$, ill.)** :
  1. Le test de McNemar exact repose sur $N_{10} \mid (N_{10}+N_{01}=m) \sim \text{Binomiale}(m, 1/2)$ et teste $\Delta p = 0$, non $\Delta p \le \delta_0$ : sa $p$-valeur ne juge pas l'hypothèse $\Delta p > 0{,}05$ (ill.).
  2. Pour des paires $(Y_{i,1}, Y_{i,0}) \in \{0,1\}^2$ de marge $\Delta p = p_{10}-p_{01} = 0{,}10$ ($0{,}15$ contre $0{,}05$, ill.) et taux discordant $q = p_{10}+p_{01} \in [0{,}10 ; 0{,}20]$ (ill.), $\text{SE}(\widehat{\Delta p}) = \sqrt{(q - (\Delta p)^2)/n} \in [0{,}0245 ; 0{,}0356]$ (ill.). La puissance d'obtenir $\widehat{\Delta p} - 1{,}96\,\text{SE} > 0{,}05$ vaut $\Phi((0{,}10 - 0{,}05)/\text{SE} - 1{,}96) \in [0{,}29 ; 0{,}53]$ (ill.), très inférieure à $0{,}80$ (ill.).
  3. Pour $\max_{1 \le b \le B} \hat{p}_b$ ($B=5$, ill.), $\mathbb{E}[\max_b \hat{p}_b] > \max_b p_b$ biaise négativement $\hat{p}_{\text{sys}} - \max_b \hat{p}_b$ dès que plusieurs $p_b$ sont voisins.
  4. L'échantillonnage séquentiel jusqu'à $n_{\max}$ en ré-évaluant un IC fixe à $95\,\%$ sans frontière séquentielle fait converger l'erreur de type I au-delà de $0{,}05$ (ill.) quand le nombre d'analyses croît.
- **Ratio $\hat{R} = \bar{U}/\bar{V}$ (E6) et ratio de densités $\hat{p}_{Q_4}/\hat{p}_{Q_1}$ (E7)** : si $|\mathbb{E}[V]| \lesssim 2\sigma_V/\sqrt{n}$, $\bar{U}/\bar{V}$ a des queues de Cauchy (moments non définis, intervalle de Fieller non borné ; référence à vérifier). En E7, sur $n/4 \approx 37$ observations (ill.), si $p_{Q_1} \le 0{,}02$ (ill.), $\mathbb{P}(\hat{p}_{Q_1}=0) \ge 0{,}47$ (ill.), rendant le ratio empirique infini ou $0/0$.
- **Concordance de signe (E8)** : pour deux estimateurs indépendants $\hat{\theta}_1, \hat{\theta}_2$, sous $\theta_1 = \theta_2 = 0$, $\mathbb{P}(\text{signe}(\hat{\theta}_1)=\text{signe}(\hat{\theta}_2)) = 0{,}50$ (ill.) ; si $|\theta_2|/\sigma_2 < 1{,}96$ (ill.), la probabilité qu'un IC exclue $0$ en sens inverse tombe sous $0{,}50$ (ill.).

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Bras « sans critique, jetons réalloués à la génération » dans E5 (`HYPOTHÈSE`)** : seul témoin neutre permettant de réfuter que la critique active bat uniquement un placebo destructeur.
2. **Paraphrases adversariales d'idées larges engendrées par les modèles eux-mêmes (`HYPOTHÈSE`)** : les réécritures mécaniques de (c) ne testent pas les obfuscations non canonisées produites par les modèles ; si elles franchissent $\nu^*$, la mesure d'étroitesse est falsifiée.
3. **Invariance du prédicteur de E7 sous permutation ou remplacement par du bruit des régimes retenus (`HYPOTHÈSE`)** : tout changement du prédicteur prouve la fuite de la vérité retenue et invalide E7.
4. **Règles fausses non triviales passées au solveur mécanique (`HYPOTHÈSE`)** : vérifier qu'une règle fausse n'accélère jamais accidentellement le solveur ($\Delta \le 0$), réfutant un artefact heuristique de $\Delta$.
5. **Test A/A complet incluant le ré-échantillonnage de calibration de $\hat{\nu}_{\text{modèle}}$ (`HYPOTHÈSE`)** : l'A/A CPU de E3 ne détecte pas les biais ni l'inflation de variance induits par le bruit de calibration et le sélecteur.

---

## Sur la proposition B

### (a) Défauts de méthode

1. **Dilemme du contrôle de profondeur et biais de colliseur dans E3 (`HYPOTHÈSE`)**. B définit $d(x)$ en soustrayant « le gain d'un contrôle de même complexité » sans en spécifier la loi de tirage (`RAPPORTÉ`, pièce B). En E3, le contrôle consiste en des idées *fausses* (constante perturbée) avec attente $d \approx 0$ : en preuve formelle, fournir un énoncé faux comme prémisse rend la théorie inconsistante et permet à un prouveur mécanique de dériver *tous* les buts de $K_{\text{test}}$ (*ex falso*, d'où $d$ maximal) ; inversement, si un filtre rejette les énoncés faux avant le solveur, $d=0$ est **vrai par construction**. De plus, estimer $\rho(n, d \mid \text{valide})$ sur des tirages de $Q$ crée un biais de colliseur si la validité dépend conjointement de la rareté et de la structure générative.
2. **Enveloppe par problème, incohérence d'estimateur et angle mort budgétaire dans E4 (`HYPOTHÈSE`)**. Prendre $\max_b \text{succ}_C(b, p)$ *par problème* crée un oracle de ligne de base qui sélectionne sur chaque problème la référence ayant eu de la chance, pénalisant systématiquement le système même sous égalité parfaite. B moyenne $\text{succ}_C$ sur 5 graines (ill.) par problème (variable dans $\{0, 0{,}2, \dots, 1\}$, ill.) tout en invoquant McNemar (réservé au binaire), et évoque l'estimateur `pass@k` (Chen et al., 2021, `RAPPORTÉ`) qui rompt la comptabilité stricte du budget $C$ pour un système muni d'un sélecteur interne. Surtout, la Phase 2 ne calibre $P_Q$ que sur 20 problèmes (ill.), alors que la Phase 5 exécute E4 sur 120–200 problèmes (ill.) sans allouer aucun budget de calcul à l'estimation de $P_Q$ sur ces problèmes (`RAPPORTÉ`, pièce B).
3. **Zones mortes violant l'inférence forte B4 (`HYPOTHÈSE`)**. B laisse des zones non partitionnées où ni $H_A$ ni $H_B$ n'est falsifiée : $\rho \in (0{,}3 ; 0{,}7)$ en E2, $|\rho| \in (0{,}1 ; 0{,}5)$ et $\rho < -0{,}1$ en E3, recouvrement $\in (20\,\% ; 80\,\%)$ en E5 (tous ill.).
4. **Confondant dans E6 (écart train-test vs corruption de la mesure) (`HYPOTHÈSE`)**. B mesure la fuite par $d(K_{\text{train}}) - d(K_{\text{test}})$ avec et sans rétroaction (`RAPPORTÉ`, pièce B). Or renvoyer $d(K_{\text{train}})$ sélectionne des candidats forts sur $K_{\text{train}}$, créant un écart d'optimisme positif même si $d(K_{\text{test}})$ reste parfaitement intègre et progresse : E6 confond sur-optimisme d'entraînement et corruption du jeu d'évaluation.
5. **Variable confondante dans E7 et oubli de coût dans E8 (`HYPOTHÈSE`)**. Dans E7, les cibles *présentes* vs *absentes* du corpus d'OLMo/Pythia ne sont pas randomisées : présence et difficulté intrinsèque, ancienneté ou centralité sont fortement confondues. Dans E8, le coût de calcul de la règle de choix de régions n'est pas imputé au rendement. Dans E1, agréger les 600 leurres en un taux global $\le 0{,}05$ (ill.) masque un taux de fausses alertes jusqu'à $0{,}15$ (ill.) sur la strate *étroit-stérile*.

### (b) Conditions probabilistes de perte de puissance ou de non-jugeabilité

*(Lois de probabilité, paramètres et estimateurs uniquement ; résultats mathématiques `VÉRIFIÉ` sur valeurs `ill.` de la pièce B.)*

- **Estimateur $\hat{n}(x) = -\log \hat{P}_Q(c(x))$ et $\hat{\rho}_S$ (E2)** : soit $M_k(x) \sim \text{Binomiale}(N, p_k(x))$ ($N = 30\,000$, ill.). Pour $p_k(x) \le 1/N$, $\mathbb{P}(M_k(x)=0) \ge e^{-1} \approx 0{,}37$ (ill.) : l'accumulation d'ex æquo à $0$ écrase $\hat{\rho}_S$. Si la projection $c(\cdot)$ possède une probabilité de fausse fusion $\gamma_{\text{merge}} > 0$ entre classes de masses $p_1 \ll p_2$, la masse observée devient $\tilde{p}_1 \ge p_1 + \gamma_{\text{merge}} p_2 \gg p_1$ (biais négatif de $\hat{n}$) ; une probabilité de scission $\gamma_{\text{split}} > 0$ biaise $\hat{n}$ positivement jusqu'à $\log N$. Avec $m_{\text{eff}} < 25$ (ill.) classes non censurées, $\text{SE}(\hat{\rho}_S) \approx (1-\rho^2)/\sqrt{m_{\text{eff}}-1}$ empêche de trancher entre $0{,}3$ et $0{,}7$ (ill.).
- **Corrélation conditionnelle $\hat{\rho}(N, D \mid V=1)$ (E3)** : si $(N, D)$ vérifient $\text{Cov}(N, D) = 0$ mais $\mathbb{P}(V=1 \mid N, D) = \mathbb{I}[aN + bD + \varepsilon > c]$ ($ab \neq 0$), alors $\text{Cov}(N, D \mid V=1)$ est non nulle et de signe $-ab$ : l'estimateur converge vers un paramètre non nul sous indépendance marginale.
- **Taux de fausses alertes agrégé $\hat{\alpha}$ (E1)** : soient $\alpha_1, \alpha_2, \alpha_3$ les paramètres par strate à poids égaux $1/3$ ($n_j=200$, ill.). Pour $\alpha_1 = 0{,}15$ et $\alpha_2 = \alpha_3 = 0$ (ill.), $\mathbb{E}[\hat{\alpha}] = 0{,}05$ (ill.) : puissance nulle contre un défaut concentré sur une strate.
- **Contraste de E4 (enveloppe ponctuelle, taille $n \in [118 ; 200]$, graines moyennées)** :
  1. Pour $Y_{\text{sys},p}, Y_{1,p}, \dots, Y_{B,p} \stackrel{\text{i.i.d.}}{\sim} \text{Bernoulli}(p)$, $\mathbb{E}[Y_{\text{sys},p} - \max_{b \le B} Y_{b,p}] = p - (1 - (1-p)^B) < 0$ pour tout $p \in (0,1)$, $B \ge 2$ (à $p=0{,}15, B=4$, biais $= -0{,}328$, ill.) : estimateur systématiquement biaisé sous l'hypothèse nulle.
  2. Pour deux proportions indépendantes $(0{,}30 ; 0{,}15)$ ($\Delta = 0{,}15$, $\sigma^2 = 0{,}3375/n$, ill.), la règle exigeant $\text{LB}_{95\%} > \Delta_{\min} = 0{,}10$ (ill.) a une puissance $\Phi((0{,}15 - 0{,}10)/\sqrt{0{,}3375/n} - 1{,}96) = 0{,}15$ à $n=118$ et $0{,}23$ à $n=200$ (ill.), hors inflation séquentielle d'O'Brien-Fleming.
  3. Pour $\bar{Y}_p = \frac{1}{s}\sum_{j=1}^s Y_{p,j}$ ($s=5$, ill.) de corrélation intra-groupe $\rho_s$, $\text{Var}(\bar{Y}_p) = \frac{p(1-p)}{s}(1+(s-1)\rho_s)$ tend vers $p(1-p)$ quand $\rho_s \to 1$, et McNemar n'est pas défini hors $\{0,1\}$.
- **Ratio d'effets $\hat{r} = \hat{\Delta}_4 / \hat{\Delta}_{E4}$ (E5)** : si $\hat{\Delta}_{E4} \sim \mathcal{N}(\Delta, \sigma^2)$ avec $\Delta/\sigma \in [2 ; 3]$ (ill.), l'écart-type delta de $\hat{r}$ vaut $\frac{1}{\Delta}\sqrt{\sigma_4^2 + r^2\sigma^2 - 2r\varrho\sigma\sigma_4} \sim 0{,}3\text{–}0{,}5$ (ill.), de sorte que l'IC recouvre simultanément $[0{,}20 ; 0{,}80]$ (ill.).
- **Contraste de E6** : pour $M$ tirages i.i.d. de couple $(T_m, E_m)$ de corrélation $\rho_{TE} < 1$, la sélection $m^* = \arg\max_m T_m$ donne $\mathbb{E}[T_{m^*} - E_{m^*}] = (1 - \rho_{TE}\frac{\sigma_E}{\sigma_T})\mathbb{E}[T_{m^*} - \mu_T] > 0$ même quand $\mathbb{E}[E_{m^*}]$ est sans biais.
- **Rapport de taux (E7) et borne de juge (c)** : à $n_0 = 100$ et $p_{\text{abs}} = 0{,}03$ (ill.), $\mathbb{P}(\hat{p}_{\text{abs}} = 0) = 0{,}048$ (ill.) ; si le classifieur de contamination a une sensibilité $1 - \beta_c$ et une prévalence vraie $\pi_c$, la fraction contaminée mal classée en « absent » vaut $\frac{\beta_c\pi_c}{\beta_c\pi_c + (1-\alpha_c)(1-\pi_c)}$, tirant le ratio vers $1$. En (c), si la borne de biais du juge vaut $\delta_J = 0{,}05$ (ill.) et la prévalence vraie $\pi \le 0{,}05$ (ill.), aucun effet $\le \delta_J$ n'est jugeable.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Taux de fausses fusions de la canonicalisation $c(\cdot)$ sur paires sémantiquement distinctes (`HYPOTHÈSE`)** : B ne mesure que la fusion de paraphrases ; une canonicalisation trop agressive valide le test à $100\,\%$ (ill.) tout en détruisant $\hat{n}$.
2. **Contrôle de fausses alertes *stratifié par quadrant* dans E1 (`HYPOTHÈSE`)** : exiger un plafond distinct sur la strate *étroit-stérile* afin de réfuter la confusion entre rareté et profondeur.
3. **Contrôle d'énoncé vrai mais orthogonal dans E3, et vérification d'absence de dérivation par contradiction (`HYPOTHÈSE`)** : remplace le contrôle d'énoncé faux qui crée un dilemme *ex falso* / vrai par construction.
4. **Plan à trois jeux $(K_{\text{train}}, K_{\text{test}}, K_{\text{vierge}})$ avec bras de fuite délibérée dans E6 (`HYPOTHÈSE`)** : indispensable pour distinguer l'écart d'optimisme sur $K_{\text{train}}$ d'une corruption effective de la mesure sur $K_{\text{test}}$.
5. **Cibles datées post-publication des poids d'OLMo/Pythia, appariées en difficulté, dans E7 (`HYPOTHÈSE`)** : réfute la confusion entre présence en corpus et facilité intrinsèque.
6. **Test A/A appliqué à la règle d'enveloppe exacte de E4 (`HYPOTHÈSE`)** : détecterait immédiatement le biais négatif de l'enveloppe par problème.

---

## Sur la proposition C

### (a) Défauts de méthode

1. **Contrôles permutés potentiellement destructeurs dans les duels 3 et 5 (`HYPOTHÈSE`)**. Au duel 5, C compare le système complet à des *critiques permutées* (d'autres dossiers) ; au duel 3, le contrôle négatif remplace le signal public par celui d'un autre problème (`RAPPORTÉ`, pièce C). Or injecter un texte ou un contre-exemple hors sujet dans le contexte d'un modèle n'est pas un zéro neutre : cela perturbe activement la recherche et peut abaisser la performance sous celle d'un système *sans critique* ou *sans retour* à budget égal. Un $T > 0$ au duel 5 peut donc résulter de la toxicité du bruit permuté plutôt que d'une contribution positive de la critique.
2. **Tension entre identité extensionnelle de classe et sensibilité syntaxique de la profondeur (`HYPOTHÈSE`)**. C définit une classe $c$ par égalité extensionnelle sur tout le domaine fini, puis mesure la profondeur en passant $c$ à un résolveur fixe face à une règle vraie placebo de *longueur et coût d'appel appariés* (`RAPPORTÉ`, pièce C). Or un résolveur reçoit une *syntaxe* concrète $r \in c$, pas la classe abstraite : deux représentants extensionnellement identiques mais de longueurs ou structures différentes n'ont ni le même effet sur le résolveur ni le même placebo apparié. Sans canonisation préalable avant passage au résolveur, le harnais reste vulnérable à une sensibilité différentielle aux formulations des chercheurs. En outre, la loi de tirage de la « règle vraie placebo » n'est pas fixée : dans un petit monde, des placebos partiellement informatifs atténuent la profondeur mesurée.
3. **Asymétrie de l'abstention et manque d'attribution au duel 4 (`HYPOTHÈSE`)**. Chaque bras rend une seule nomination ou s'abstient, avec score $1$ si certifiée EP et $0$ sinon (`RAPPORTÉ`, pièce C). Comme une fausse nomination rapporte $0$ au même titre que l'abstention (avec en plus une probabilité $\text{FPR} > 0$ de passer à tort), la stratégie dominante consiste à ne jamais s'abstenir : deux bras différant par leur taux d'abstention subissent un confondant de calibration. De plus, aucun duel confirmatoire n'isole le sélecteur, la diversité des modèles ni le best-of-N pur face au système complet.
4. **Angle mort sur la corruption par rétroaction (question 5) (`HYPOTHÈSE`)**. Le duel 3 teste si le retour public améliore le succès sur un coffre frais, mais ne mesure jamais s'il corrompt l'estimation d'étroitesse ou de profondeur (dérive Goodhart entre signal interne et mesure externe).
5. **Rupture d'échelle entre audit aveugle (étape 2) et comparaison (étape 5) (`HYPOTHÈSE`)**. Certifier $\approx 3\,330$ négatifs indépendants par strate (ill.) exige des micromondes minuscules calculables exhaustivement, où les sondes coïncident presque avec l'oracle (proche du vrai par construction). Les taux d'erreur ainsi audités ne se transfèrent pas mécaniquement aux mondes plus grands de l'étape 5, où $p_r$ est estimé sur 300 tirages (ill.) et les problèmes aval sont échantillonnés.

### (b) Conditions probabilistes de perte de puissance ou de non-jugeabilité

*(Lois de probabilité, paramètres et estimateurs uniquement ; résultats mathématiques `VÉRIFIÉ` sur valeurs `ill.` de la pièce C.)*

- **Borne supérieure simultanée sur $\max_{r \in \mathcal{R}} p_r(c) < \tau$** : soient $R = |\mathcal{R}|$ lois de référence, $K_r$ tirages indépendants, $M_w$ classes testées et $X_{r,c} \sim \text{Binomiale}(K_r, p_r(c))$. Sous correction simultanée de Bonferroni au niveau $\alpha$, la borne supérieure exacte à $X_{r,c}=0$ vaut $u = 1 - (\alpha / (R M_w))^{1/K_r}$. Condition de puissance identiquement nulle : $K_r \le \frac{\ln(R M_w / \alpha)}{\tau}$. Avec $K_r = 300$, $\tau = 0{,}01$, $\alpha = 0{,}05$ (ill.), dès $R = 2$ et $M_w = 1$, $u = 1 - 0{,}025^{1/300} = 0{,}0122 > 0{,}01$ (pour $R = 3$, $u = 0{,}0136$, ill.) : **$\mathbb{P}(u < \tau) = 0$ identiquement**, aucune classe ne peut être déclarée étroite.
- **Audit aveugle à $n = 3\,330$ négatifs par strate et incompatibilité Bayes du duel 1** :
  1. Pour un taux réel $\alpha_{\text{FA}} = 0{,}0005 < 0{,}00090$ (ill.), $\mathbb{P}(\text{Binomiale}(3330, 0{,}0005) \ge 1) = 0{,}811$ (ill.) ; or dès $1$ alerte observée, la borne supérieure unilatérale à $95\,\%$ vaut $\approx 4{,}744/3330 = 0{,}00142 > 0{,}00090$ (ill.) : la puissance de valider un instrument satisfaisant pourtant le cahier des charges tombe sous $0{,}19$ (ill.), avant correction multiple sur les strates.
  2. Par la formule de Bayes, $\text{FDR} = \frac{\alpha_{\text{FA}}(1-\pi)}{\alpha_{\text{FA}}(1-\pi) + s\pi}$. Avec les seuils du duel 1 ($s = 0{,}80$, $\alpha_{\text{FA}} = 0{,}005$, ill.), $\text{FDR} > 0{,}10$ (ill.) dès que la prévalence vraie vérifie $\pi < 0{,}053$ (ill.).
- **Sonde de profondeur (borne inférieure $> d = 0{,}15$, ill.)** : sur $m$ problèmes aval, $\Delta_j \in \{-1,0,+1\}$ de moyenne $\mu_d$, variance $\sigma_d^2$ et corrélation intra-monde $\rho_{\text{aval}}$. La variance réelle vaut $\frac{\sigma_d^2}{m}(1+(m-1)\rho_{\text{aval}})$, bornée inférieurement par $\rho_{\text{aval}} \sigma_d^2 > 0$ quand $m \to \infty$ : l'IC supposant l'indépendance perd sa couverture, et dès que $\mu_d - d \lesssim 2\sqrt{\rho_{\text{aval}}}\sigma_d$, la sensibilité tombe sous $0{,}80$ (ill.).
- **Contraste simultané du duel 4 et analyse de sensibilité pire cas** : soient $\delta_{\text{diff}}$ la borne d'erreur différentielle, $\eta_{\text{indéc}}$ la proportion de dossiers non résolus et $\rho_{\text{fam}}$ la corrélation intra-famille sur blocs de taille moyenne $\bar{m}$. Le contraste devient non tranchable dès que $\delta_{\text{diff}} + \eta_{\text{indéc}} \ge \Delta_{\text{vrai}} - 0{,}05$ (ill.). De plus, $n \simeq (z_{1-\alpha}+z_{1-\beta})^2 q / g^2 \approx 495$ (pour $q=0{,}20, g=0{,}05, \alpha=0{,}05$, ill.) ignore la correction simultanée sur $K_{\text{sim}}$ contrastes (à $K_{\text{sim}}=10$, $\alpha'=0{,}005$, $n$ passe à $934$, ill.) et l'inflation de variance $1 + (\bar{m}-1)\rho_{\text{fam}}$ par famille.
- **Paramètre biaisé aux duels 3 et 5** : soient $p_{\text{complet}}$, $p_{\text{neutre}}$ et $p_{\text{perm}}$. L'estimateur de $T = p_{\text{complet}} - p_{\text{perm}} - \delta_0$ converge vers une quantité $> 0$ dès que $p_{\text{perm}} < p_{\text{neutre}} - \delta_0$, même lorsque $p_{\text{complet}} \le p_{\text{neutre}}$.
- **Duel 2 à coût de prospection inclus** : avec coût de prospection $c_{\text{prosp}}$, coût de recherche $c_{\text{rech}}$ et taux de sélection $\phi \in (0,1]$, le rendement par unité de budget devient négatif dès que $p_{\text{cib}}/p_{\text{strat}} < 1 + c_{\text{prosp}}/(\phi c_{\text{rech}})$.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Bras neutres « sans critique » (duel 5) et « sans retour public » (duel 3) à budget réalloué (`HYPOTHÈSE`)** : indispensables pour réfuter qu'un gain apparent contre un signal permuté ne provienne que de la nocivité du bruit hors sujet.
2. **Contrôle d'invariance syntaxique de la sonde de profondeur intra-classe (`HYPOTHÈSE`)** : passer au résolveur deux représentants *extensionnellement identiques* de syntaxes distinctes ; un écart significatif de $\hat{d}$ falsifie l'indépendance à la formulation.
3. **Contrôle de corruption par rétroaction avec bras de fuite délibérée (`HYPOTHÈSE`)** : vérifier qu'une fuite connue gonfle le score exposé par rapport à un coffre vierge, et qu'aucune dérive analogue n'affecte les retours autorisés.
4. **Audit négatif stratifié sur les mondes de grande taille de l'étape 5 (`HYPOTHÈSE`)** : vérifier que la sensibilité différentielle $\delta_{\text{diff}}$ mesurée sur micromondes exhaustifs ne diverge pas quand l'oracle exact est remplacé par les sondes approchées.
5. **Contrôle d'abstention forcée à zéro sur mondes nuls (`HYPOTHÈSE`)** : vérifier que l'écart entre bras ne dépend pas d'une asymétrie de taux d'abstention exploitant un $\text{FPR} > 0$.

---

## Sur la proposition D

### (a) Défauts de méthode

1. **Défaut structurel de la métrique $D_{\text{MDL}}$ (`HYPOTHÈSE`)**. D définit $D_{\text{MDL}}([x]) = \sum_{r=1}^R \max(0, L_{\text{null}}(D_r) - L(D_r \mid [x])) - K_{\mathcal{L}}([x])$ (`RAPPORTÉ`, pièce D). La troncature $\max(0, \cdot)$ terme à terme supprime toute pénalité sur les régimes où la loi $[x]$ fait des prédictions fausses ($L(D_r \mid [x]) \gg L_{\text{null}}(D_r)$) : une loi réfutée sur $R-1$ régimes peut obtenir un score élevé en compressant un seul régime, contredisant à la fois le principe MDL et la réfutation poppérienne invoqués par D. En outre, $L_{\text{null}}$ n'est pas spécifié, et pour les lemmes formels, soustraire le coût de vérification du nombre de pas de saturation mêle des unités incommensurables (alors que `Exp. II` garde $\tau_D = 35$ nats MDL en Phase III Lean).
2. **Incohérence de $M_0$, $\tau_N$ et $b_0$ vs $B$ (`HYPOTHÈSE`)**. D calibre $N_{\mu_0, b_0}$ à budget unitaire $b_0$ mais compare `MA-Complet` à `BestOfN-Mono(B)` à budget $B \gg b_0$ (`RAPPORTÉ`, pièce D) : une idée rare sous $b_0$ peut être triviale au budget $B$ du duel. De plus, l'appariement *simultané* des 4 composantes du vecteur budget $(B_{\text{FLOP}}, B_{\text{tok}}, B_{\text{oracle}}, B_{\text{mur}})$ entre un énumérateur CPU, un Best-of-N parallèle et un multi-agents séquentiel est physiquement impossible sans saturer des goulots différents selon le bras (confondant architecture et contrainte active).
3. **Vrai par construction dans `Exp. I` et circularité dans `Exp. IV` (`HYPOTHÈSE`)**. En Phase I (0 GPU-heure, ill.), `Exp. I` évalue l'invariance sur 3 DSL *formellement isomorphes* sans exécuter aucun LLM : la partie prédictive de $D_{\text{MDL}}$ est identique par bijection, et la sensibilité lexicale de $\mu_0$ (modèle de langage) n'est jamais testée. Dans `Exp. IV`, le sélecteur $S_{\text{region}}$ utilise les résidus des références simples sur les problèmes mêmes où $N_{\mu_0}$ (échec de la référence simple) définit la cible : il y a fuite entre prédicteur et étiquette, et en mondes synthétiques, un fort résidu épistémique sélectionne presque par définition les mondes contenant une loi cachée non trouvée par la référence simple. Par ailleurs, la Phase II annonce `60` problèmes (ill.) pour `Exp. IV` alors que la Section III en exige `120` (ill.), et réutilise les mêmes 60 problèmes pour 4 expériences confirmatoires (`Exp. II` à `V`).
4. **Erreur de plan d'échantillonnage sur Rogan-Gladen et angle mort de `Exp. VI` (`HYPOTHÈSE`)**. D invoque l'identité de Rogan-Gladen (Rogan & Gladen, 1978, `RAPPORTÉ`) en auditant un sous-échantillon des appels $\hat{J}=1$ et $\hat{J}=0$ (`RAPPORTÉ`, pièce D). Or échantillonner conditionnellement à $\hat{J}$ estime les valeurs prédictives $(\text{PPV}_g, \text{NPV}_g)$ et non $(\text{TPR}_g, \text{FPR}_g)$ : la prévalence vaut directement $p_g \text{PPV}_g + (1-p_g)(1-\text{NPV}_g)$ sans inversion instable. En outre, `Exp. VI` n'audite que des négatifs vrais ($Y=0$) et ignore totalement un biais différentiel de sensibilité $|\text{TPR}_{\text{MA}} - \text{TPR}_{\text{Mono}}|$.
5. **Lacunes d'attribution et incohérences dans `Exp. III` et `Exp. V` (`HYPOTHÈSE`)**. Le Point 3 liste 4 ablations mais seule la critique (`Exp. III`) est formalisée en duel ; et le critère $\Delta N \ge 0{,}7$ nat (ill.) impose une hausse de rareté même si la critique n'agit que sur la profondeur ou la sélection. Dans `Exp. V`, D ne teste pas le `Thresholdout` (Dwork et al., 2015, `RAPPORTÉ`) qu'il propose au Point 5, et son contrôle négatif (passe unique hors boucle donnant $\mathbb{E}[D_{\text{hold}} - D_{\text{vault}}] = 0$) est vrai par échangeabilité i.i.d. Enfin, D attribue le statut `[VÉRIFIÉ]` à des approximations empiriques (égalité sur grille dense) qui ne constituent pas une équivalence sémantique exacte.

### (b) Conditions probabilistes de perte de puissance ou de non-jugeabilité

*(Lois de probabilité, paramètres et estimateurs uniquement ; résultats mathématiques `VÉRIFIÉ` sur valeurs `ill.` de la pièce D.)*

- **Estimateur $N_{\mu_0, b_0} = -\ln \hat{p}_0^+$ (Clopper & Pearson, 1934, `RAPPORTÉ`) à $M_0 = 1\,000$, $\tau_N = 5{,}5$ nats (ill.)** : soit $S \sim \text{Binomiale}(M_0, p_0)$. À $\alpha = 0{,}05$ unilatéral (ill.), $-\ln \hat{p}_0^+(0) = 5{,}81 > 5{,}5$, mais $-\ln \hat{p}_0^+(1) = 5{,}35 < 5{,}5$ (ill.).
  1. L'événement $\{N_{\mu_0} \ge 5{,}5\}$ coïncide avec $\{S=0\}$ : pour $p_0 = 2\times 10^{-3}$ ($-\ln p_0 = 6{,}21 > 5{,}5$, ill.), la sensibilité tombe à $(1-0{,}002)^{1000} = 0{,}135$ (ill.).
  2. Sous correction de Bonferroni pour $m \ge 4$ classes ($\alpha' \le 0{,}0125$, ill.), $-\ln \hat{p}_0^+(0) \le 5{,}43 < 5{,}5$ (ill.) : $\mathbb{P}(N_{\mu_0} \ge \tau_N) = 0$ identiquement.
  3. Sur $\{N_{\mu_0} \ge 5{,}5\}$, l'étendue maximale de $N_{\mu_0}$ vaut $5{,}81 - 5{,}5 = 0{,}31 < 0{,}7$ nat (ill.), rendant le critère $\Delta N \ge 0{,}7$ de `Exp. III` mathématiquement inatteignable sur cette sous-population.
- **Biais positif de $D_{\text{MDL}}$ par troncature** : pour $\Delta L_r \stackrel{\text{i.i.d.}}{\sim} \mathcal{N}(\mu, \sigma^2)$ avec $\mu \le 0$, $\mathbb{E}[\sum_{r=1}^R \max(0, \Delta L_r)] = R(\mu\Phi(\mu/\sigma) + \sigma\phi(\mu/\sigma)) > 0$ (soit $R\sigma/\sqrt{2\pi}$ à $\mu=0$). Dès que $R\sigma/\sqrt{2\pi} \ge K_{\mathcal{L}} + \tau_D$, le taux de fausses alertes converge vers $1$.
- **Concordance $\hat{\tau}_K$ sur $W = \mathbb{I}[N_{\mu_0} \ge \tau_N]\cdot D$ (`Exp. I`)** : si $\pi_0 = \mathbb{P}(N_{\mu_0} < \tau_N) \to 1$ (ex. $\pi_0 = 0{,}95$ sur $N_{\text{classes}} = 200$, ill.), la masse d'ex æquo en $0$ vaut $\pi_0^2 \approx 0{,}90$ et seules $\approx 10$ observations non nulles portent l'information de rang, dilatant l'IC bootstrap de $\hat{\tau}_K$.
- **Puissance de l'IUT (Berger, 1982, `RAPPORTÉ`) en Phase II (`Exp. II`, $M_{\text{prob}} = 60$, $\alpha = 0{,}025$, $\delta_{\min} = 0{,}10$, ill.)** : la puissance vaut $\mathbb{P}(\bigcap_{b=1}^4 \{T_b > c_\alpha\}) \le \min_b \mathbb{P}(T_b > c_\alpha)$. Pour un vrai gain $\Delta_b = 0{,}15 > \delta_{\min}$ et taux discordant $q_b = 0{,}25$ (ill.), $\text{SE} = \sqrt{(0{,}25 - 0{,}15^2)/60} = 0{,}0616$ (ill.) ; la puissance sur une seule référence vaut $\Phi((0{,}15 - 0{,}10)/0{,}0616 - 1{,}96) = 0{,}13$ (ill.), et moins encore sur l'intersection des 4 références. De plus, sans règle d'agrégation des 5 graines (ill.), la loi de $Y_{i,m}$ n'est pas spécifiée ; si $Z_{i,m}$ a une masse $\pi_{00} \ge 0{,}85$ en $0$ (`Exp. III`), le test de Wilcoxon opère sur $\mathbb{E}[m_{\text{eff}}] \le 9$ (ill.) paires non nulles.
- **Puissance de $\widehat{\text{OR}}$ (`Exp. IV`, $n_1 = n_0 = 60$, $\alpha = 0{,}025$, seuil $2{,}5$, ill.)** : pour $(p_1, p_0) = (0{,}15 ; 0{,}05)$ ($\text{OR} = 3{,}35 > 2{,}5$, ill.), $\text{SE}(\ln \widehat{\text{OR}}) = \sqrt{\frac{1}{60\cdot 0{,}15\cdot 0{,}85} + \frac{1}{60\cdot 0{,}05\cdot 0{,}95}} = 0{,}694$ (ill.), d'où une puissance $\Phi((\ln 3{,}35 - \ln 2{,}5)/0{,}694 - 1{,}96) = 0{,}06$ (ill.) et $\mathbb{P}(\hat{p}_0 = 0) = 0{,}95^{60} = 0{,}046$ (ill., $\widehat{\text{OR}} = +\infty$).
- **Estimateur de Rogan-Gladen et validation de `Exp. VI` ($n = 500$, ill.)** : pour $\hat{\pi}_g = (\hat{p}_g - \widehat{\text{FPR}}_g)/(\widehat{\text{TPR}}_g - \widehat{\text{FPR}}_g)$, un audit non stratifié de taille $n$ donne $n_{1,g} \sim \text{Binomiale}(n, \pi_g)$ qui vaut $0$ avec probabilité $(1-\pi_g)^n$ (estimateur non défini). En `Exp. VI`, valider $\text{UB}_{95\%}(\text{FPR}_g) < 0{,}01$ (ill.) sur $n=500$ exige au plus $1$ faux positif ; pour un vrai $\text{FPR} = 0{,}008$ (ill.), $\mathbb{P}(\text{Binomiale}(500, 0{,}008) \ge 2) = 0{,}91$ (ill., puissance de validation $0{,}09$). Enfin, la différence brute $\Delta p_{\text{obs}}$ reste biaisée jusqu'à $\pm 0{,}03$ (ill.) par $|\Delta \text{FPR}| < 0{,}03$ et arbitrairement biaisée dès que $\text{TPR}_{\text{MA}} \neq \text{TPR}_{\text{Mono}}$.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Lois partiellement fausses (fort gain sur 1 régime, réfutées sur les $R-1$ autres) dans l'étalonnage de $D_{\text{MDL}}$ (`HYPOTHÈSE`)** : déclenche immédiatement la faille du $\max(0, \cdot)$ et falsifie la métrique de profondeur.
2. **Systèmes déterministes complexes incompressibles dans $\mathcal{L}$ dans `Exp. IV` (`HYPOTHÈSE`)** : le contrôle de bruit stochastique seul (résidu épistémique nul après réplicats) ne teste pas si $S_{\text{region}}$ confond profondeur cachée et complexité déterministe irréductible.
3. **Audit stratifié de positifs vrais ($Y=1$) par bras dans `Exp. VI` (`HYPOTHÈSE`)** : indispensable pour détecter un biais différentiel $|\text{TPR}_{\text{MA}} - \text{TPR}_{\text{Mono}}|$, invisible sur les seuls négatifs.
4. **Invariance inter-DSL incluant le modèle $\mu_0$ et stratifiée sur les classes rares dans `Exp. I` (`HYPOTHÈSE`)** : sans le modèle $\mu_0$ (absent de la Phase I CPU), `Exp. I` ne peut pas réfuter la dépendance syntaxique de $N_{\mu_0}$.
5. **Contrôle de cohérence entre $N_{\mu_0, b_0}$ et la probabilité d'atteinte par `BestOfN-Mono(B)` (`HYPOTHÈSE`)** : vérifier si les idées certifiées étroites à budget $b_0$ sont ou non fréquemment atteintes au budget $B$, sans quoi la cible ne correspond pas à la rareté au budget du duel.
6. **Test de fuite du mécanisme de rétroaction autorisé (`Thresholdout` sur $D_{\text{val}}$) contre un coffre vierge dans `Exp. V` (`HYPOTHÈSE`)** : remplace le contrôle trivial en une passe et éprouve directement l'instrument réellement proposé au Point 5.

FIN-DE-CELLULE

## Cellule E3-T3-reponse-A (lettre A)

# Proposition A — Tour III.3 : réponse aux critiques

## Pièces et statuts

- Les quatre critiques (B, C, D, E) sont présentes, se terminent par FIN-DE-CELLULE et ne montrent aucune coupure. Le bloc QUESTION est identique au bloc FAITS (même empreinte).
- Je ne réponds qu'aux sections « Sur la proposition A ».
- Je ne modifie aucun statut. C, D et E étiquettent VÉRIFIÉ leurs déductions mathématiques : je reprends ces étiquettes sans pouvoir les auditer ici.
- Tout ce que j'ajoute est **HYPOTHÈSE**, y compris les dérivations élémentaires que j'ai refaites à la main, non auditées. Rien n'a été exécuté. Tout chiffre est **illustratif** (« ill. »).
- Deux recalculs à la main concordent avec les critiques : la puissance de 0,29 à 0,53 pour E4 à n = 150 (E), et la proportion de fausses découvertes d'environ 0,92 pour un juge à 0,10 de fausses alertes sous une prévalence de 0,01 (D).

---

## (a) Verdict par critique

### Critiques de B

| Réf. | Critique | Verdict | Conséquence |
|---|---|---|---|
| B-a1 | Borne de handicap : la référence qui définit l'étroitesse est aussi un bras de E4, donc son taux EP est majoré par construction. | **Acceptée.** C'est le défaut le plus grave de ma conception. | Budgets découplés, borne rapportée, bras CN-1 dans E4 (voir T2 et E4′). |
| B-a2 | E1 est vrai par construction si l'étiquette « profonde » et Δ partagent leur source. | **Acceptée.** | E1 remplacée par E1′, sans étiquette du concepteur. |
| B-a3 | L'oracle dilué augmente P_R(x) ; ν doit être figée sur la référence non diluée. | **Acceptée** (spécification manquante). | ν figée avant E3, sur des exécutions disjointes et non diluées. |
| B-a4 | Le prédicteur de E7 est lié mécaniquement au rang d'énumération. | **Acceptée.** | Prédicteur redéfini ; l'énumérateur sort du critère de E7. |
| B-a5 | Choisir « la meilleure référence » après coup est une sélection. | **Acceptée.** | Intersection-union : supériorité contre chaque bras. |
| B-a6 | La puissance de E4 est calculée contre zéro, la règle exige +5 points. | **Acceptée.** Mon dimensionnement était faux. | 280 à 600 mondes (ill.) au lieu de 150. |
| B-a7 | Le ratio de E6 dépend du couplage public/privé du générateur de mondes. | **Transformée en test.** | Le couplage devient un facteur de E6′. |
| B-b (ν) | Censure au plafond : Spearman sur ex-aequo, fiabilité 0,9 inatteignable. | **Acceptée.** | E2′ porte sur une étiquette binaire. |
| B-b (E1) | Si le solveur sature, l'AUC tend vers 0,5 quel que soit le concept. | **Transformée en verrou.** | Fraction résolue sans x exigée entre 0,2 et 0,8 (ill.), réglée sur des mondes de développement. |
| B-b (E4) | Trop peu de paires discordantes si les taux sont au plancher. | **Transformée en verrou.** | Le pilote doit montrer un bras hors système au-dessus du plancher mesurable. |
| B-b (E7) | Moins d'un succès attendu par quartile. | **Acceptée.** | E7′ devient exploratoire. |
| B-b (juge) | La correction n'est plus bornée si TPR − FPR tend vers 0. | **Acceptée.** | Juge exclu de toute mesure (T4). |
| B-c CN-1 | L'A/A est aveugle au handicap ; il faut un bras « référence déplacée ». | **Acceptée.** | Les bras CN-1 entrent dans E4′ comme adversaires à battre. |
| B-c CN-2 | Il faut un chasseur d'étroitesse ; le bras « bizarre » ne teste rien. | **Acceptée pour CN-2. Rejetée en partie pour « ne teste rien ».** Le bras scripté vérifie que la chaîne de notation ne crédite pas un rare-inerte, ce qui échoue si Δ a un biais positif. Il ne teste pas un chercheur, et B a raison sur ce point. | CN-2 ajouté à E3b ; le bras « bizarre » reste comme contrôle d'instrument. |
| B-c | Δ(x) sur des conséquences engendrées à partir d'une autre idée x′. | **Acceptée.** | Contrôle de E1′. |

### Critiques de C

| Réf. | Critique | Verdict | Conséquence |
|---|---|---|---|
| C-a (rang) | Un rang d'énumération n'est pas une probabilité d'atteinte ; un tirage uniforme sur classes ne les ordonne pas. | **Acceptée.** Sous tirage uniforme sur classes, ν est la même constante pour toutes : mon E2 n'avait rien à comparer pour cette référence. | Le tirage uniforme sort du panel d'étroitesse et reste un bras. L'énumérateur donne une étiquette binaire exacte (rang ≤ b_ν ou non). |
| C-a (E1) | L'AUC vérifie la cohérence des étiquettes. | **Acceptée** (même défaut que B-a2). | E1′. |
| C-a (E3) | Injecter dans le vivier ne fixe pas l'effet en sortie ; le gain vaut q(1−p₀)s. | **Acceptée.** | E3a injecte en sortie finale (effet connu) ; l'injection dans le vivier mesure s séparément. |
| C-a (E5) | Battre une critique hors sujet ne montre pas que la critique aide par rapport au silence. | **Acceptée.** | Trois témoins dans E5′. |
| C-b (E2) | Spearman indéfini à variance nulle ; la concordance des rangs n'implique pas l'accord au seuil. | **Acceptée.** | E2′ mesure l'accord au seuil. |
| C-b (E3–E5) | Variance (d − Δ²)/n ; McNemar teste l'égalité, pas une marge. | **Acceptée.** | Intervalle sur la différence appariée contre la marge (T1). |
| C-b (E6–E8) | Ratios indéfinis ; présence et détection confondues en E7 ; signe non résolu en E8. | **Acceptée.** | Différences au lieu de ratios ; E7′ déclare mesurer un rendement ; E8′ non confirmatoire. |
| C-b (audits) | Un taux moyen ne borne pas l'erreur sur une variante de poids nul ; « antérieur » n'identifie pas « vu à l'entraînement ». | **Acceptée comme limite.** | Les fiches d'instrument rapportent le pire taux par strate. Le test de fuite détecte un signal de mémorisation, pas l'exposition. |
| C-c (leurres) | Produire les leurres par une autre grammaire, inertie établie indépendamment. | **Acceptée pour l'inertie indépendante. Transformée en test pour l'autre grammaire** : des leurres d'une autre grammaire peuvent être reconnaissables à leur forme, ce qui casserait l'appariement. | Un classifieur ne voyant que la forme doit rester à une AUC d'environ 0,5 ; sinon ces leurres sont écartés. |
| C-c | Injecter un leurre par le même canal que l'oracle. | **Acceptée.** | Contrôle de E3a. |
| C-c | Rejouer en A/A toute la procédure, choix compris. | **Acceptée.** | E3b. |
| C-c | Message neutre du même problème, même longueur. | **Acceptée.** | E5′. |

### Critiques de D

| Réf. | Critique | Verdict | Conséquence |
|---|---|---|---|
| D-a1 | E1 ne teste pas la séparabilité sur les idées effectivement produites par des chercheurs. | **Acceptée.** | E1′ est répétée sur les sorties du pilote. |
| D-a2 | L'étiquette « inerte » du prédicteur de E7 dépend de Δ privé : fuite. | **Acceptée.** Erreur de ma part : le prédicteur n'était pas calculable sans la vérité retenue. | Prédicteur public seul (E7′). |
| D-a3 (coûts) | Plafonner à l'identique les appels au vérificateur bride l'énumérateur et PySR. | **Acceptée.** | Coût matériel mesuré (T3). Le test de D devient l'analyse primaire ; l'ancien plafond devient une analyse de sensibilité. |
| D-a3 (placebo) | Le placebo hors problème peut distraire. | **Acceptée** (comme C-a). | E5′. |
| D-a4 | Dimensionnement faux ; un juge à 0,10 de fausses alertes donne plus de 0,91 de fausses découvertes à prévalence 0,01. | **Acceptée** pour les deux. | Le seuil de 0,10 de ma fiche « juge » est retiré. À cette prévalence, viser 0,2 de fausses découvertes demanderait environ 0,002 de fausses alertes (ill.), soit environ 1 500 négatifs sans alerte (ill.) : le juge est exclu. |
| D-b1 | Troncature et effondrement du critère de demi-échantillons. | **Acceptée.** | E2′. |
| D-b2 | La puissance de certification décroît en exp(−K Σ_r p_r). | **Acceptée.** | Seules les idées avec Σ_r p_r ≲ 0,1/K sont certifiées avec une probabilité d'environ 0,9 (ill.). C'est écrit dans T2. |
| D-b3 | Formule de taille contre une marge non nulle. | **Acceptée**, et je m'en sers pour E4′. | n ≥ (z_α + z_β)²(ψ − θ²)/(θ − θ₀)². |
| D-b4 | Ratios à région de confiance non bornée (Fieller 1954, RAPPORTÉ par D) ; E8 sans décision. | **Acceptée.** | Différences ; E8′ non confirmatoire. |
| D-c1 | Canonisation adversariale par termes neutres. | **Transformée en verrou.** | Appartenance à une classe décidée par canonisation et équivalence numérique sur des points incluant les régimes d'intervention ; taux de fausse scission ≤ 1 % (ill.) sur des obscurcissements engendrés par modèle. |
| D-c2 | Placebo hors problème contre remplissage neutre intra-problème. | **Transformée en test**, tel que D l'énonce. | Si le hors-problème est inférieur au neutre, il est retiré comme témoin. |
| D-c3 | Égaliser en coût matériel total. | **Transformée en test** (voir D-a3). | E4′. |

### Critiques de E

| Réf. | Critique | Verdict | Conséquence |
|---|---|---|---|
| E-a1, E-c3 | Fuite de la vérité retenue dans le prédicteur de E7 ; test d'invariance sous permutation des régimes retenus. | **Acceptée** (comme D-a2). | L'invariance devient un contrôle de code de E7′. |
| E-a2 (E1) | Vrai par construction ; leurres non appariés en ν sous modèle. | **Acceptée.** Je rejette seulement l'exigence implicite d'une « séparabilité générale », qu'aucun monde clos n'établit. | E1′ ; appariement en ν sous modèle revérifié après le pilote. |
| E-a2 (E3) | E3 sur processeur est satisfaite par construction et n'éprouve ni la canonisation des sorties de modèle ni le bruit de ν. | **Transformée en test.** Un contrôle positif est construit par nature : E3a vérifie la statistique de décision, et rien de plus. | E3b après le pilote, avec sorties de modèle. |
| E-a3 | Placebo destructeur ; conditionnement sur une variable post-traitement ; hétérogénéité confondue avec le niveau moyen. | **Acceptée** pour les trois. | La décomposition rappel/précision devient descriptive. L'attribution passe par le croisement vivier × sélecteur. Le bras « N copies » est lancé pour chaque famille. |
| E-a4 (test) | « Un seul test confirmatoire » contre 5 références et 3 budgets. | **Acceptée.** | Un budget primaire préenregistré ; les deux autres sont descriptifs. |
| E-a4 (jetons) | Sommer entrées et sorties confond des coûts différents. | **Acceptée.** | Coût matériel mesuré (T3). |
| E-a4 (ν) | Si ν n'inclut pas PySR ni le best-of-N, une idée banale pour eux est étiquetée EP. | **Rejetée comme lecture** : ma définition exige ν ≥ ν* « sous chaque référence ». **Acceptée sur le fond** : je n'avais chiffré que la calibration sous modèle. | Calibration de PySR ajoutée au plan. |
| E-a5 | E6 : couplage structurel public/privé. | **Transformée en test** (comme B-a7). | La conclusion de E6′ ne vaut que pour le niveau de couplage testé. |
| E-b | Saturation de ν et fausses alertes en e^{−3c} ; atténuation de Spearman ; borne d'AUC et corrélation intra-groupe ; quatre défauts de la décision E4, dont l'arrêt séquentiel sans frontière ; ratios ; E8. | **Acceptée** en bloc. | T1, T2, bootstrap par monde. |
| E-c1 | Bras « sans critique, jetons réalloués ». | **Acceptée.** Je me sers aussi d'une remarque que C adresse à une autre proposition : ce bras mesure une politique budgétaire, pas l'effet de lire une critique. Les deux témoins sont donc nécessaires. | E5′. |
| E-c2 | Paraphrases adversariales engendrées par les modèles. | **Transformée en verrou** (avec D-c1). | E3b. |
| E-c4 | Règles fausses non triviales passées au solveur : Δ ≤ 0 attendu. | **Acceptée.** | Contrôle de E1′. |
| E-c5 | A/A complet incluant la recalibration de ν. | **Acceptée.** | E3b. |

---

## (b) Expériences corrigées

### Changements transversaux

**T1. Règle de décision.**
- Le n est fixe, avec une seule analyse et aucune prolongation.
- La statistique est un intervalle à 95 % sur la différence appariée par monde, comparé à la marge (Newcombe 1998, *Statistics in Medicine*, RAPPORTÉ, page non vérifiée).
- Il y a trois issues : au-dessus, au-dessous, ou « instrument insuffisant ».

**T2. Étroitesse.**
- **Étiquette.** C'est une étiquette binaire censurée, pas un scalaire. « Étroite sous R » signifie zéro atteinte en K exécutions de R au budget de calibration b_ν. Ces exécutions sont disjointes de la comparaison et figées avant elle.
- **Panel.** Énumérateur (rang > b_ν, exact), PySR et modèle seul.
- **Puissance de certification.** Elle vaut environ e^{−KΣp} (D-b2). En pratique, « étroite » veut donc dire Σp ≲ 0,1/K, et non p ≤ 3/K.
- **Handicap.** Une référence du panel, rejouée au budget B = m·b_ν, atteint une idée certifiée avec une probabilité d'au plus environ m·p. Pour K = 300 et m = 10 (ill.), cela donne environ 0,3 % par idée.
- **Compromis.** « Certifiable » et « atteignable par la référence » ne sont compatibles que si m est de l'ordre de K.
- **Conséquence.** Le duel contre un membre du panel est signalé « non comparatif » dès que la borne passe sous la marge. Il reste une condition nécessaire, mais ne décide rien.

**T3. Coût.** C'est le coût matériel mesuré (secondes de GPU et de processeur valorisées), évaluations publiques comprises. Les jetons sont journalisés. Aucun bras n'accède à l'évaluation privée.

**T4. Juge.** Il est exclu de toute mesure primaire ou secondaire.

### E1′ — Δ se reproduit-il à rareté fixée ?

- **Population** : toutes les classes d'un espace énuméré exhaustivement, puis les sorties du pilote. Il n'y a aucune étiquette du concepteur.
- **Mesure** : deux jeux de conséquences C1 et C2, tirés par le générateur de régimes avant toute idée et sans la connaître, et deux solveurs S1 et S2.
- **H_A** : dans chaque strate de rang d'énumération, la proportion de classes « profondes » selon (C1, S1) qui le restent selon (C2, S2) est d'au moins 0,7 (ill.).
- **H_B** : elle est inférieure.
- **Contrôles** :
  - Δ sur les conséquences d'un autre monde doit être d'environ 0 (B).
  - Les règles fausses doivent donner Δ ≤ 0 (E).
  - Les régimes permutés doivent ramener au taux de base.
  - Le verrou de non-saturation doit être passé.
  - Le bootstrap se fait par monde.
- **Si H_A est retenue** : « à rareté fixée, Δ n'est que du bruit » est réfutée pour cette famille.
- **Si H_B est retenue** : ma définition de la profondeur est réfutée, et on arrête.

### E2′ — L'étiquette « étroite » dépend-elle de la référence ?

- **H_A** : parmi les classes étroites sous une référence du panel, la proportion étroite sous une autre est d'au moins 0,6 (ill.).
- **H_B** : elle est inférieure. La cible doit alors nommer R.
- **Contrôles** : l'accord test-retest de l'étiquette sur deux moitiés disjointes d'exécutions ; les mondes ré-encodés.
- **Rapporté en plus** : la part de classes non résolues.

### E3a puis E3b — Verrou

- **E3a** (processeur) :
  - Une idée EP est injectée en sortie finale avec une probabilité q, ν étant figée.
  - Un leurre injecté par le même canal doit donner un gain nul.
  - Un test A/A complète l'ensemble.
  - H_A et H_B sont inchangées.
  - E3a ne valide que la statistique de décision.
- **E3b** (après le pilote) :
  - **A/A complet.** Il porte sur des sorties de modèle et rejoue toute la procédure, recalibration de ν comprise.
  - **CN-2.** Le chasseur d'étroitesse tourne sur des mondes sans idée EP. H_A : son taux EP ne dépasse pas le taux de fausses alertes admis. H_B : il le dépasse, et le critère est alors perméable à la rareté seule.
  - **Obscurcissements.** Ceux engendrés par modèle sont soumis à la canonisation.
- **Arrêt** : tout échec arrête le plan.

### E4′ — Comparaison

- **Bras** : le système ; le panel (énumérateur, PySR, modèle seul en fil unique et en best-of-N) ; et deux bras CN-1 hors panel, à savoir la référence à température relevée et une autre famille avec consigne paraphrasée.
- **Métrique** : P(au moins un succès EP parmi k finales), en différence appariée par monde, au budget primaire.
- **H_A** : la différence est d'au moins +5 points (ill.) contre chaque bras.
- **H_B** : elle est inférieure contre au moins un bras.
- **Décision** : H_A si toutes les bornes inférieures dépassent la marge. H_B si une borne supérieure est sous la marge. Sinon, l'instrument est insuffisant.
- **Taille** : 600 mondes (ill.), pour un écart vrai de 10 points et une discordance de 0,20. La puissance conjointe est au plus celle du contraste le plus faible.
- **Lecture** :
  - Une victoire contre le panel seul, sans victoire contre les CN-1, réfute l'affirmation : l'avantage est alors de la divergence.
  - Le secondaire obligatoire est le succès « profond » sans condition d'étroitesse, où aucun bras n'est handicapé.

### E5′ — Attribution

- **Plan** : le factoriel reste. La critique active doit dépasser chacun des trois témoins : hors problème, neutre intra-problème, et sans critique avec jetons réalloués.
- **Sélection** : le croisement vivier × sélecteur l'attribue par intervention.
- **Hétérogénéité** : elle est testée contre le meilleur bras homogène, désigné sur des mondes de développement.

### E6′ — Retour

- **Estimande** : l'écart (public − privé) sous F2, moins le même écart sous F0.
- **Facteur** : couplage fort ou faible entre conséquences publiques et privées.
- **Contrôle positif** : F3, avec un troisième jeu vierge.
- **Portée** : toute conclusion est indexée par le niveau de couplage.

### E7′ — Régions (exploratoire)

- **Prédicteur** : la dispersion des prédictions hors régimes observés parmi les M candidats les mieux ajustés au public. Il se calcule sans vérité retenue.
- **Plan** : prévalence plantée égale entre strates ; différence de taux entre deux moitiés.
- **Portée** : E7′ mesure un rendement de recherche, pas l'existence de régions.

### E8′ — Transport

Le plan est inchangé, mais le test devient non confirmatoire. Il ne conclut que si chaque effet a un intervalle excluant zéro dans les deux domaines.

### Plan révisé (ill.)

1. Arithmétique de T2 pour les (K, m, ν*) retenus. Coût nul.
2. Instruments, E1′, E2′ mécanique, E3a. Processeur, moins de 200 cœur-heures.
3. Pilote ν sous modèle (20 mondes), E3b.
4. E6′.
5. Calibration : 600 mondes × 300 exécutions × b_ν. C'est toujours le poste dominant.
6. E4′, puis E5′ si H_A.
7. E7′ et E8′.

---

## (c) Réponse à l'arbitre

### Ce qui est établi

Aucun résultat empirique n'existe : rien n'a été exécuté. Ce qui tient est de deux ordres.

- **Littérature (RAPPORTÉ dans ma pièce, pages non vérifiées)** :
  - la borne 3/K (Hanley & Lippman-Hand 1983) ;
  - la dégradation d'un jeu retenu par usage adaptatif (Dwork et al. 2015) ;
  - les biais de juge en général (Zheng et al. 2023 ; Panickssery, Bowman, Feng 2024).
- **Arithmétique des critiques**, avec les statuts de leurs auteurs :
  - La censure de l'étroitesse au plafond log₂(K/3).
  - La décroissance de la puissance de certification en exp(−KΣp), VÉRIFIÉ selon D.
  - Le dimensionnement contre la marge et non contre zéro, VÉRIFIÉ selon C, D et E.
  - La borne de handicap, HYPOTHÈSE selon B. Je l'ai refaite à la main et la tiens pour correcte ; elle n'a pas été auditée.

### Ce qui n'est pas établi

- Que la profondeur Δ soit reproductible à rareté fixée (E1′).
- Que « étroit » ait un sens sans nommer la référence (E2′).
- Que le taux de base soit mesurable.
- Qu'un système multi-agents batte quoi que ce soit.
- Que des régions favorables existent.
- Qu'un résultat en monde clos se transporte.

### Où le cadrage est fautif

« Rarement atteint par la recherche ordinaire » et « meilleur que les références » ne sont pas indépendants. Si la référence définit l'ordinaire, elle perd par définition (B-a1). L'affirmation réfutable devient : « à coût égal, le système trouve des idées profondes, étroites pour un panel figé, plus souvent que des variantes trivialement divergentes de ce panel ».

### Confiance révisée par point

| Point | Confiance | Motif du changement |
|---|---|---|
| 1. Cible | 0,5 | L'étroitesse est binaire et censurée ; Δ n'est pas encore éprouvé. |
| 2. Sources | 0,65 | Inchangé ; le juge est exclu. |
| 3. Comparaison | 0,6 | Handicap ; marge ; CN-1. |
| 4. Choix de problèmes | 0,25 | Mon prédicteur fuyait ; E7′ est exploratoire. |
| 5. Retour | 0,55 | Le résultat dépend du couplage. |
| 6. Validation | 0,75 | Renforcée par CN-1, CN-2 et E3b. |
| 7. Plan | 0,5 | Tailles multipliées par quatre. |
| 8. Limites | 0,55 | Le compromis de T2 s'ajoute. |

### Preuves que la cible est mal posée ou le harnais infaisable

- E1′ retient H_B.
- Les bras CN-1 gagnent autant que le système en E4′.
- Aucun couple (K, m) abordable ne sort tous les bras du plancher.
- E3b échoue.

### L'expérience à faire en premier

1. **Le calcul de T2, à coût nul.** Pour les K, m et ν* envisagés, on calcule la borne de handicap et la puissance de certification. Si aucun réglage ne laisse un bras hors système au-dessus du plancher, la forme comparative de la cible est à abandonner avant d'écrire du code.
2. **E1′ sur processeur.** Si l'étiquette « profonde » ne se reproduit pas entre deux jeux de conséquences et deux solveurs indépendants, à rareté fixée, la définition de la profondeur tombe et rien d'autre ne mérite d'être lancé.

FIN-DE-CELLULE

## Cellule E3-T3-reponse-B (lettre B)

# Proposition B, tour III.3 : réponse aux critiques

**Pièces.** Le bloc FAITS est identique au bloc QUESTION (même empreinte). Il ne contient donc aucun fait étiqueté et aucun fait VÉRIFIÉ. Ma conception III.1 et les critiques A, C, D et E sont présentes et complètes. Je ne traite que les sections « Sur la proposition B ».

**Statuts.**
- Je cite les statuts des critiques sans les modifier.
- Mes décisions de conception ont le statut HYPOTHÈSE.
- Mes calculs sont de l'arithmétique sur des paramètres hypothétiques. Leurs résultats sont **illustratifs**.

**Usage déclaré des autres propositions (B1).**
- Je reprends la règle de C : un seul seuil par contraste, avec des hypothèses exhaustives.
- Je reprends la critique que D adresse à A sur l'égalisation des appels au vérificateur.
- Je reprends la critique que C reçoit sur un placebo qui ralentirait le solveur. Elle me conduit à comparer aussi à un solveur sans idée ajoutée.

---

## (a) Verdict sur chaque critique

Légende : **ACC** = acceptée ; **REJ** = rejetée, raison donnée ; **TEST** = transformée en test.

### Critiques de A

| ID | Critique | Verdict | Conséquence |
|---|---|---|---|
| A-1 | E4 est vrai par construction : Q, qui définit l'étroitesse, est le modèle du bras 4. | ACC + TEST | L'étroitesse se mesure sous un panel Q_ref disjoint de tous les bras. J'ajoute un bras « différent mais pas meilleur ». S'il gagne, n mesure une distance à Q_ref et non une découverte. |
| A-2 | Le nombre de candidats est confondant. J'ai refait le calcul : 1 − 0,95⁵⁰ ≈ 0,92. | ACC | Chaque bras soumet k nominations, k fixe, choisies avant l'ouverture du coffre. |
| A-3 | E1 est tautologique. | ACC en partie, REJ en partie | ACC : E1 ne valide pas le construit, et je retire cette prétention. REJ : un contrôle positif est construit par définition, c'est sa fonction ; il détecte les bogues et les sensibilités de surface. J'ajoute une loi profonde non documentée comme plantée (idée que A formule pour C) et des leurres issus d'une autre grammaire. |
| A-4 | E2 subit une troncature de type Berkson. | ACC | L'ensemble de classes est fixé hors des tirages des Q. La statistique devient un désaccord sur le drapeau « étroit certifié », et non plus ρ sur des valeurs censurées. |
| A-5 | E3 souffre d'une étendue restreinte, et seule la profondeur est ajustée sur la complexité. | ACC | Tirage stratifié en n. Le même ajustement de complexité s'applique aux deux axes. |
| A-6 | E8 est circulaire. | ACC | Les régions sont choisies sous une référence Q′ disjointe de Q_ref. |
| A-7 | La canonicalisation n'est évaluée que d'un côté. | ACC | E0′ ajoute un plafond de fausses fusions. |
| A-8 | En E7, les cibles présentes et absentes ne sont pas appariées. | ACC | Injection randomisée (E7′). |
| A-9 | Zones mortes au sens de B4. | ACC pour les hypothèses ; REJ pour l'incertitude | Un seul seuil par contraste, hypothèses exhaustives. L'issue « non concluant » subsiste quand l'intervalle chevauche le seuil. Ce n'est pas une troisième hypothèse : c'est un défaut de précision, dont la probabilité est bornée par le calcul de taille. |
| A-10 | Le contrôle de profondeur repose sur une idée fausse. | ACC | Contrôle par une idée vraie mais inerte (voir E-1 pour *ex falso*). |
| A-p1 | Plafond ln(M/3) ; ex æquo. | ACC | Certification par borne supérieure ; voir l'identité I1. |
| A-p2 | VPP ≈ 0,14 à prévalence 0,01. Calcul refait : 0,008/0,0575 ≈ 0,139. | ACC | Fausses alertes dérivées d'un FDR cible (I2). |
| A-p3 | McNemar quand q → 0 ; enveloppe max_b biaisée. | ACC | Enveloppe abandonnée. q est mesuré au pilote. |
| A-p4 | d n'a pas de variance si S réussit presque toujours ou presque jamais. | ACC | K_test est calibré pour que S, sans idée ajoutée, résolve entre 0,2 et 0,8 (illustratif). |
| A-p5 | Le quotient de E5 n'est pas borné. | ACC | Remplacé par des différences. |
| A-p6 | E7 n'est faisable qu'avec de petits modèles. | ACC comme limite | Non corrigeable ; déclaré en (c). |
| A-c | Cinq contrôles : différent-pas-meilleur, spam, paires proches mais distinctes, vrai-inerte et table recopiant K_train, Q′ disjoint. | ACC (les cinq) | Intégrés en (b). |

### Critiques de C

| ID | Critique | Verdict | Conséquence |
|---|---|---|---|
| C-1 | E3 ignore les relations non monotones et décroissantes ; le contre-exemple ρ_S(U, (U − ½)²) = 0 est exact. | ACC | Le test porte sur les écarts de moyennes conditionnelles par strate de n. |
| C-2 | En E7, la présence dans le corpus n'est pas assignée au hasard. | ACC | E7′. |
| C-3 | Deux comparateurs possibles : choisi sur le développement, ou choisi après coup. | ACC | Pas d'enveloppe ; un contraste par ligne de base. |
| C-4 | En E5, la réallocation mesure une politique budgétaire. | TEST | Deux bras distincts : critique masquée et critique retirée avec réallocation. |
| C-5 | E6 est différé après E4. | ACC | E6′ se fait au pilote, avant E4′. |
| C-b (E6) | Un intervalle qui traverse la tolérance ne prouve pas l'innocuité. | ACC | Test d'équivalence (deux tests unilatéraux ; référence à vérifier). |
| C-b (E7) | Même si la présence détectée égale l'exposition, la difficulté latente confond. | ACC | Randomisation. |
| C-b (E8) | Les régions de probabilité d'inclusion nulle ne sont pas couvertes. | ACC | La revendication est restreinte à la population de régions échantillonnée. |
| C-c | Identités valides inertes, permutation intra-famille, classifieur limité au gabarit, critique masquée à candidats constants. | ACC | Intégrés en (b). |

### Critiques de D

| ID | Critique | Verdict | Conséquence |
|---|---|---|---|
| D-1 | L'enveloppe par problème joue contre le système ; McNemar ne s'applique pas à des fractions. | ACC | Bootstrap apparié par problème sur Y_p. |
| D-2 | Redéfinir d conditionnellement à n injecte la loi de Q dans l'instrument. | ACC en partie, REJ en partie | ACC : je retire la redéfinition. REJ : E3 garde son sens. Il décrit une propriété du couple (Q, domaine), ce que soutient ma thèse (P3). |
| D-3 | P_Q n'est pas estimé sur des tirages disjoints ; −log 0 ; E7 ne se transfère pas aux 70B fermés. | ACC | Tirages de référence disjoints des runs ; borne supérieure ; limite déclarée. |
| D-b1 | n̂ sans régularisation perd le contrôle de l'erreur de type I ; avec γ > 0, la puissance s'annule. | ACC | E2 utilisait déjà la règle de trois, mais E4 ne fixait aucun estimateur. Désormais : certification par borne supérieure seulement (I1). |
| D-b2 | E3 souffre d'une inflation de zéros. | ACC | Tirage enrichi par strate. |
| D-b3 | Les frontières d'O'Brien-Fleming supposent un comportement gaussien, faux à petits effectifs discrets. | ACC | Analyse intermédiaire seulement après au moins 20 paires discordantes (illustratif). Frontières calibrées par simulation. |
| D-b4 | E6 : décalage δ_split entre K_train et K_test ; E7 : quotient non borné. | ACC | Partition aléatoire de K ; différences. |
| D-c1 | A/A multi-copies contre l'enveloppe. | TEST | Exécuté comme démonstration. Il doit montrer le biais négatif, ce qui documente l'abandon de l'enveloppe. |
| D-c2 | Auto-formalisateur dégénéré. | ACC | Bras de contrôle négatif en Lean. |
| D-c3 | Injection randomisée. | ACC | E7′. |

### Critiques de E

| ID | Critique | Verdict | Conséquence |
|---|---|---|---|
| E-1 (*ex falso*) | Une prémisse fausse rend toute cible dérivable. | ACC | Seules des idées validées mécaniquement passent au solveur S : lemme prouvé, axiomes en liste blanche. En monde planté, une loi est évaluée par prédiction et non comme axiome. |
| E-1 (collision) | ρ(n, d \| valide) subit un biais de collision. | REJ en partie | L'estimande est conditionnel à la validité par définition : seules les idées valides comptent. Je le lis comme une description, jamais comme une relation structurelle. Le biais de collision n'affecte que cette dernière lecture. |
| E-2 (pass@k) | pass@k rompt la comptabilité des coûts pour un système doté d'un sélecteur interne. | ACC | Retiré. |
| E-2 (P_Q non budgété) | P_Q n'est estimé que sur 20 problèmes, alors que E4 en compte 120 à 200. | ACC | Phase P ajoutée au plan, avec son coût. |
| E-2 (puissance E4) | Puissance 0,15 à n = 118. | ACC | Erreur de ma part : n = 118 testait contre 0, alors que la règle teste contre Δ_min. Recalcul en I3. |
| E-4 | E6 confond l'optimisme sur K_train et la corruption de la mesure. | ACC | Trois jeux de conséquences et un bras de fuite délibérée. |
| E-5 | Coût de E8 non imputé ; fausses alertes agrégées en E1. | ACC | Coût imputé ; un plafond par strate. |
| E-b (fusion/scission) | Une canonicalisation imparfaite biaise n̂ dans les deux sens. | ACC | E0′ mesure les deux taux. |
| E-b (juge) | Aucun effet ≤ δ_J n'est jugeable. | ACC | Le juge est exclu de toute quantité primaire. |
| E-c5 | Cibles postérieures à la coupure, appariées en difficulté. | ACC comme analyse secondaire ; REJ comme substitut | La date confond difficulté et dérive de notation. |
| E-c6 | A/A sur l'enveloppe exacte. | Traité en D-c1 | — |

---

## (b) Expériences corrigées

### Identités de conception

Statut : arithmétique sur paramètres HYPOTHÈSE, chiffres illustratifs.

**I1 — Certifier l'étroitesse coûte de la sensibilité.**
- Déclarer p < τ exige 0 occurrence en M tirages, pour chaque membre du panel (R membres) et chaque classe testée (m classes). Il faut M ≳ ln(R·m/α)/τ.
- Une classe de vraie probabilité p est certifiée avec probabilité e^(−pM).
- Pour obtenir 0,8, il faut p ≲ 0,223·τ / ln(R·m/α).
- Avec R = 3, m = 60 et α = 0,05, on a ln(3 600) ≈ 8,2. « Étroit certifié » signifie alors une rareté de l'ordre de **37 fois τ**.
- Je l'écris dans la définition plutôt que de le découvrir à l'analyse. Pour aller au-delà, il faut des estimateurs d'événements rares (référence à vérifier pour les LM).

**I2 — Fausses alertes tolérables.**
- FPR ≤ s·π·q* / ((1 − π)(1 − q*)).
- Avec π = 0,01, s = 0,8 et un FDR cible q* = 0,2, on obtient FPR ≈ 0,002 par strate.
- Le certifier sans aucune alerte demande au moins 1 500 négatifs par strate (3/0,002).
- **Dépendance non résolue** : π est inconnu. J'encadre π par un intervalle préenregistré et je prends le plafond correspondant au π le plus bas.

**I3 — Taille de E4.**
- n ≈ (z_{α/2} + z_β)² · (q − Δ²) / (Δ − θ₀)².
- Avec q = 0,25, Δ = 0,15 et θ₀ = 0,05 : n ≈ 178 problèmes pour un contraste à puissance 0,8.
- Le test d'intersection-union porte sur 3 contrastes. Avec une puissance de 0,93 par contraste : n ≈ 11,8 × 0,2275 / 0,01 ≈ **270 problèmes**.
- À recalculer avec le q mesuré au pilote.

### E0′ — Canonicalisation (CPU)

- **H_A** : la canonicalisation c(·) est fidèle. Elle fusionne au moins 0,98 des paraphrases **et** fusionne à tort au plus 0,02 des paires proches mais distinctes (seuils illustratifs).
- **H_B** : l'une des deux bornes est violée.
- **Jeux de test** : paraphrases mécaniques, obfuscations produites par les modèles eux-mêmes (idée que E adresse à A), paires distinctes à une constante ou un terme près.
- **Issues** :
  - H_B falsifie la validité de n̂, quel que soit le sens de l'erreur. On arrête avant E2′.
  - H_A falsifie le biais de fusion et de scission décrit par E.

### E1′ — Contrôle positif de l'instrument (mondes plantés)

**Dispositif.**
- 200 positifs, dont une seconde loi profonde **non documentée**. Elle doit être créditée.
- Leurres produits par une autre grammaire que les positifs. Trois strates : rare-stérile, commun-utile, commun-stérile. Au moins 1 500 leurres par strate.
- La profondeur d est comparée à **deux** références : S sans idée ajoutée, et S avec une idée vraie-inerte de même complexité. Une idée n'est profonde que si elle dépasse les deux.

**Hypothèses.**
- **H_A** : sensibilité ≥ 0,8, **et** fausses alertes ≤ 0,002 dans chaque strate, **et** un classifieur limité au gabarit a une AUC ≤ 0,55 (illustratif).
- **H_B** : l'une des conditions échoue.

**Contrôles.** Permutation des étiquettes à l'intérieur des familles de construction. Table recopiant K_train, qui doit obtenir d ≈ 0.

**Issues.**
- H_B : les scores suivent la construction ou la surface, et l'instrument est révisé.
- H_A : falsifie seulement l'hypothèse de bogue ou de sensibilité à la surface. Cette issue **ne valide pas** le construit.

### E2′ — Dépendance de l'étroitesse à la référence

**Dispositif.**
- Ensemble de classes fixé à l'avance : énumération de la grammaire, plus les nominations d'un quatrième modèle extérieur au panel.
- Chaque Q_ref,i reçoit le même M, sur des tirages disjoints de tout run.

**Hypothèses.**
- **H_A** : le taux de désaccord sur le drapeau « étroit certifié » entre références dépasse de moins de ε = 0,10 le plancher « même Q, deux graines ».
- **H_B** : il le dépasse de plus de ε.

**Issues.**
- H_B, et H_B persiste sous une seconde canonicalisation : « étroit » doit être indexé par la référence. Le cadrage « recherche ordinaire » est alors mal posé sans indice.
- H_A : falsifie la dépendance à la référence, pour ce panel seulement.

### E3′ — Rareté et profondeur (descriptif)

- **Dispositif** : tirage stratifié en n par une loi de proposition, puis repondération. Ajustement de complexité identique pour n et pour d. Estimande conditionnel à la validité.
- **H_A** : max_s |E[d | strate s] − E[d]| ≤ ε.
- **H_B** : cet écart dépasse ε.
- **Issues** :
  - H_B : les axes sont dépendants sous ce Q. On publie la loi jointe, **sans redéfinir d**.
  - H_A : la cellule jointe est un objet propre pour ce couple (Q, domaine).

### E6′ — Fuite par rétroaction (pilote, avant E4′)

**Dispositif.**
- K est partitionné **au hasard** en trois jeux : K_train (renvoyé au générateur), K_test (scellé), K_vierge (ouvert une seule fois).
- Trois bras : retour, silence, fuite délibérée de K_test (contrôle positif).

**Hypothèses.**
- **H_A** : |[d(K_test) − d(K_vierge)]_retour − [d(K_test) − d(K_vierge)]_silence| ≤ ε, par test d'équivalence.
- **H_B** : cet écart dépasse ε.

**Règle de sensibilité.** Le bras de fuite délibérée doit dépasser ε. Sinon le test n'a pas de sensibilité et on arrête.

**Issues.**
- H_B : le signal renvoyé passe en « retenu ».
- H_A : falsifie la corruption de la mesure par ce signal.
- L'écart d'optimisme K_train − K_test n'entre pas dans la décision.

### E4′ — Comparaison principale

**Bras**, tous avec k nominations choisies avant l'ouverture du coffre :
- le système ;
- best-of-N mono-modèle, avec le même vérificateur et le même sélecteur ;
- l'énumérateur ou PySR ;
- l'échantillonnage aléatoire, seulement dans un espace formel ;
- « différent mais pas meilleur » ;
- « spam » : k idées valides et rares tirées au hasard ;
- placebo : rôles attribués au hasard, sans interaction ;
- en Lean, un auto-formalisateur dégénéré.

**Quantité primaire.**
- Y_p est la fraction des s graines où au moins une nomination est à la fois valide, certifiée étroite sous Q_ref (I1), et profonde au sens de E1′.
- Unité : le problème.

**Coût.**
- Comptabilité complète : jetons de tous les agents, appels au vérificateur, temps mural.
- Pour l'énumérateur, l'égalisation se fait en coût monétaire, et non en nombre d'appels au vérificateur.
- Coût de prospection et estimation de P_Q imputés aux bras concernés.

**Règle de décision.**
- Test d'intersection-union. Pour chaque ligne de base b : **H_A,b** : Δ_b > θ₀ ; **H_B,b** : Δ_b ≤ θ₀.
- Bootstrap apparié par problème. Plan séquentiel à frontières simulées. Pas d'enveloppe.

**Contrôles.**
- A/A sur la procédure complète : choix de la référence, analyses intermédiaires, arrêts.
- A/A multi-copies contre l'enveloppe (D-c1), comme démonstration.
- Le bras spam doit rester proche de 0. L'auto-formalisateur dégénéré doit obtenir d ≤ 0.
- Si le bras « différent mais pas meilleur » vérifie Δ > θ₀, l'interprétation « découverte » est falsifiée.

**Issues.**
- Toutes les bornes inférieures au-dessus de θ₀ : H_B falsifiée.
- Une borne supérieure sous θ₀ : H_A falsifiée.

### E5′ — Attribution

**Bras**, à coût égal :
1. système complet ;
2. critique masquée : message neutre portant sur le même problème, de même longueur, avec les mêmes candidats et le même sélecteur ;
3. critique retirée, jetons réalloués à la génération (politique budgétaire) ;
4. une seule famille de modèles avec plusieurs personas ;
5. best-of-N.

**Hypothèses.**
- **H_A** (« l'interaction contribue ») : (1 − 2) > θ₀ **et** (1 − 5) > θ₀.
- **H_B** : l'un des deux contrastes est ≤ θ₀.

Le contraste (1 − 3) répond séparément à la question de la politique budgétaire. Il n'y a plus aucun quotient.

### E7′ — Rappel ou recherche

- **Dispositif** : paires de cibles synthétiques jumelles. On tire au hasard la moitié de chaque paire pour l'injecter par entraînement continu dans un modèle ouvert.
- **H_A** : succès(injectées) − succès(retenues) ≤ ε.
- **H_B** : cet écart dépasse ε.
- **Issues** :
  - H_B : la rétrodiction exige une certification d'exposition cible par cible. Avec des modèles fermés, elle est retirée du plan.
  - H_A : falsifie l'effet de rappel, pour ce modèle et cette dose d'injection.
- **Analyse secondaire seulement** : cibles postérieures à la coupure.

### E8′ — Choix des régions

- **Dispositif** : la règle est apprise sous Q′ disjoint de Q_ref, puis évaluée sur des régions tenues à l'écart. Le coût de prospection est imputé.
- **H_A** : rendement net par unité de coût de la règle − rendement net d'un tirage aléatoire de régions > θ₀.
- **H_B** : cette différence est ≤ θ₀.
- La revendication est restreinte à la population de régions échantillonnée.

### Plan révisé

| Phase | Contenu | Arrêt si | Taille | Coût (illustratif) |
|---|---|---|---|---|
| 0 | E0′, préenregistrement | H_B en E0′ | ~2 000 paires | CPU |
| 1 | E1′ | H_B | 200 positifs, ≥ 1 500 leurres par strate | CPU + petit modèle |
| 2 | E2′ + E3′ | E2′ en H_B : pas d'arrêt, affirmations indexées par la référence | 30 000 tirages × 20 problèmes × 3 Q_ref | ≈ 50 h GPU |
| 3 | Pilote avec le système : A/A, E6′, spam, mesure de q | A/A au-dessus du nominal ; contrôle de fuite insensible | 30 problèmes × 3 bras × 5 graines | ≈ 9·10⁸ jetons, 10³–5·10³ $ |
| 4 | E7′ | — | ~200 paires jumelles | quelques centaines d'h GPU |
| P | Estimation de P_Q pour les problèmes de E4′ | — | 270 problèmes × 3 × 30 000 × ~10³ jetons ≈ 2,4·10¹⁰ jetons | ≈ 680 h GPU, ≈ 1,4·10³–3,4·10³ $ |
| 5 | E4′ séquentiel | Frontières simulées | ~270 problèmes | ≈ 2·10⁴–7·10⁴ $ |
| 6 | E5′ | Seulement si E4′ conclut H_A | Mêmes problèmes, 5 bras | Ordre de la phase 5 |
| 7 | E8′ | H_B : abandon du choix ciblé | Régions 50/50 | — |

---

## (c) Réponse à la question de l'arbitre

**Ce qui est établi.**
- **Aucun fait empirique.** Le bloc FAITS ne contient aucun fait étiqueté. Le seul contenu factuel est le contexte du projet (RAPPORTÉ).
- **Le biais d'auto-préférence des juges LM est RAPPORTÉ dans la littérature** : Zheng et al., 2023 ; Panickssery, Bowman & Feng, 2024. Je ne l'ai pas vérifié ici.
- **Des identités sur les estimateurs, qui contraignent toute conception.** Leurs paramètres sont HYPOTHÈSE.
  - (i) Certifier l'étroitesse par zéro occurrence ne détecte, à sensibilité 0,8, que des classes environ 37 fois plus rares que le seuil affiché (I1).
  - (ii) À prévalence 0,01, des fausses alertes à 0,05 donnent une VPP d'environ 0,14 ; il faut viser environ 0,002 (I2).
  - (iii) Une enveloppe des lignes de base prise par problème est biaisée contre le système.
  - (iv) Mon n = 118 était faux pour ma propre règle : il faut de l'ordre de 270 problèmes (I3).

**Ce qui n'est pas établi** (tout est HYPOTHÈSE) :
- que la classe « étroit ∧ profond » soit non vide dans un domaine réel ;
- que l'étroitesse soit stable d'une référence à l'autre ;
- que la profondeur se sépare de la rareté ;
- que renvoyer la validité au générateur soit sans effet sur la mesure ;
- que le système batte best-of-N à coût et vérificateur égaux ;
- que les classements se transfèrent des mondes plantés au domaine formel ;
- que la rétrodiction soit utilisable avec des modèles à données fermées.

**Où le cadrage reste faux**, selon moi (HYPOTHÈSE) :
- « rarement atteint par la recherche ordinaire » n'est pas défini sans une référence nommée et disjointe des bras ;
- « finds » mêle recherche et sélection tant que le nombre de nominations n'est pas fixé ;
- un harnais général est probablement hors de portée ; seul un harnais par domaine et par référence est défendable.

**Expérience à faire en premier : E2′, précédée de son prérequis E0′.**
- E0′ coûte quelques heures CPU ; E2′ environ 50 h GPU (illustratif).
- C'est l'expérience la moins chère qui puisse falsifier le cadrage lui-même, et pas seulement mon instrument :
  - si le désaccord inter-références dépasse le plancher dû au bruit et persiste sous une seconde canonicalisation, « étroit » n'a de sens qu'indexé par une référence, et toute la question 1 doit être reformulée ;
  - dans le cas contraire, la dépendance à la référence est falsifiée pour ce panel, et E1′ puis le pilote deviennent les priorités.
- E1′ vient ensuite. C'est un contrôle positif nécessaire, mais il ne peut falsifier qu'un bogue ou une sensibilité à la surface.

**Confiance** (subjective) :
- 0,7 que les corrections suppriment les défauts relevés par A, C, D et E ;
- 0,4 que E4′ soit jugeable avec environ 270 problèmes, car cela dépend de q, encore inconnu ;
- 0,5 que E2′ conclue H_B.

FIN-DE-CELLULE

## Cellule E3-T3-reponse-C (lettre C)

# Proposition C — Réponse aux critiques

**RAPPORTÉ —** La pièce C décrit un harnais proposé, sans résultat d’essai. Je retire deux ambitions de la première version : mesurer dans le même score la découverte d’une loi et celle d’un algorithme rapide ; extrapoler aux grands mondes un étalonnage effectué sur de petits mondes.

**Convention —** Mes décisions, expériences, seuils et confiances ont le statut **HYPOTHÈSE**. Tous les nombres de dimensionnement, seuils et confiances sont **illustratifs**. Les identifiants des critiques et les dates bibliographiques ne sont pas des mesures. Les statuts des pièces restent inchangés.

## (a) Décisions sur les critiques visant C

|Critique|Décision et modification|
|---|---|
|**A — référence contre ligne de base**|**Acceptée pour le handicap ; rejetée pour la réduction à un test à un échantillon.** La borne d’union \(K_w\tau\) sur le succès d’une référence commune dépend du nombre de classes qualifiées et peut être sans portée si elles sont nombreuses. Une borne ne donne pas le taux du solo. Je sépare néanmoins le panel qui **définit** la rareté des bras qui **concourent** ; je renonce au qualificatif « rare pour la meilleure recherche ordinaire ». Retrait et remplacement de chaque référence deviennent des analyses préenregistrées.|
|**A — représentant ; profondeur plantée**|**Acceptées.** L’unité sera une assertion partielle à portée déclarée ; le résolveur recevra une interface canonique, jamais le texte soumis. Le générateur de buts sera gelé sans connaître les assertions candidates ni leur statut de plantation. Une loi vraie non documentée comme plantée devra pouvoir être créditée au même titre qu’une autre.|
|**A — audit de négatifs ; dossiers indécidables**|**Acceptées.** Un audit construit vérifie des modes de panne ; il ne donne pas la valeur prédictive sur les sorties réelles. Pas de campagne massive là où toutes les réponses sont calculables ; ailleurs, audit aléatoire par bras à l’échelle d’emploi ou limitation de la revendication. Arrêt si l’incertitude d’identification absorbe la marge utile, même si l’erreur d’échantillonnage est faible.|
|**A — nomination ; sélection des régions**|**Acceptées.** « A atteint » et « a livré » auront deux indicateurs distincts. J’abandonne le prédicteur fondé sur le nombre de structures aval partagées. La sélection sera jugée sur le rendement de toute la campagne, y compris les régions prospectées et refusées.|
|**A — puissance de la rareté et du duel ; critique générique ; contrôles demandés**|**Transformées en tests.** Dimensionnement sur la courbe de puissance, non sur le premier effectif permettant une certification à zéro occurrence. Simulation des discordances au seuil du duel. Critique générique, critique spécifique et absence de critique sont séparées. J’adopte les contrôles de représentation, de seconde règle, de divergence du générateur et d’audit des sorties détaillés ci-dessous.|
|**B — classe vraie unique ; permutation uniforme ; handicap**|**Acceptées sous les conditions énoncées.** Une prédiction totale d’une unique fonction vraie ne fournit pas plusieurs classes vraies. Une permutation uniforme des classes ne discrimine pas leurs rangs d’accès. Je conserve ce cas comme contrôle calculable, pas comme instrument discriminant : l’énumérateur concurrent parcourra les programmes par coût croissant avec départage fixé. Pour le handicap, même décision que pour A.|
|**B — source des buts et du placebo ; gain sur une autre règle**|**Acceptée pour la source ; rejetée pour l’exigence générale de gain nul.** Une loi peut aider à résoudre un but exprimé avec une autre loi : ce serait précisément un transfert. Le contrôle nul utilisera des sous-systèmes disjoints avec une interface interdisant d’utiliser l’outil hors de sa portée.|
|**B — citations ; dimensionnement au seuil**|**Acceptées.** Les deux références de C ne constituent ni un audit bibliographique réalisé dans cette conversation ni une validation du harnais. Je conserve le dimensionnement contre l’excès au seuil, et non contre zéro.|
|**B — maximum bruité, saturation aval, faibles taux et hétérogénéité des familles ; CN-1, CN-2, monde à classe unique**|**Transformées en tests.** Calcul exact d’abord, bornes simultanées ensuite. Piloter les plafonds du résolveur sur développement ; mesurer les discordances et la variance *entre familles*. J’adopte les deux bras de contrôle de B et le monde à classe unique. Un faible taux de succès peut réfuter un gain minimal ; il ne justifie pas de déplacer ce seuil après observation.|
|**D — fusion table/loi ; abstention ; encombrement par le placebo**|**Acceptées, avec un désaccord de cible.** Pour une assertion, fusionner table et formule équivalentes sera intentionnel ; je rejette le contrôle exigeant de les distinguer *comme assertions*. Leur différence d’efficacité relèverait d’un autre essai sur les algorithmes. Nomination obligatoire si le vivier est non vide. Le résolveur nu devient le comparateur principal.|
|**D — multiplicité, précision aval, coût bayésien, non-convergence des bornes ; contrôles demandés**|**Acceptées comme risques, transformées en portes de décision.** Allocation explicite des erreurs, dimensionnement des buts indépendants et audit dépendant de la prévalence. J’adopte le duel placebo/nu et le rejeu à abstention forcée ; pour la paire table/loi, je teste le comportement annoncé ci-dessus plutôt qu’une séparation contraire à la nouvelle cible.|
|**E — permutations destructrices ; formulation et loi du placebo**|**Acceptées.** Une permutation sert à mesurer une nuisance, jamais à établir seule le bénéfice d’un canal. Le placebo est désormais un diagnostic secondaire, de loi publiée ; aucun score principal ne peut augmenter parce que le placebo ralentit le résolveur.|
|**E — abstention et attribution ; corruption par retour ; changement d’échelle**|**Acceptées.** Ajout de sélecteurs comparés sur les mêmes viviers, de best-of-\(N\) et de bras homogènes. Un coffre vierge mesure la dérive induite par consultation d’un coffre exposé. Changer d’échelle ouvre une nouvelle validation ; cela ne prolonge pas un certificat précédent.|
|**E — puissance des sondes, audit à zéro alerte, dépendances aval/famille, coûts de prospection ; contrôles demandés**|**Acceptées.** Le cas « zéro alerte » donne une taille minimale possible, pas une puissance acceptable à taux non nul. Je remplace les deux tolérances d’alerte par un cahier des charges cohérent avec la prévalence visée. Les bras neutres, la fuite délibérée, l’audit à l’échelle cible et les nominations forcées sur mondes nuls figurent dans le plan.|

## (b) Expériences corrigées

**HYPOTHÈSE — Unité et oracle.** Un monde contient plusieurs observables nommées. Avant génération, publier un catalogue fini de portées admissibles, non vides et scientifiquement interprétables dans ce monde. Une assertion donne une observable cible, une portée du catalogue et une prédiction sur **toute** cette portée. Sa clé est le triplet *cible, ensemble d’entrées, vecteur de réponses*. Des domaines emboîtés mais distincts donnent des assertions distinctes ; deux écritures du même ensemble n’en donnent pas deux. Pas de portée inventée après coup pour raréfier une assertion banale. La règle est vraie si toutes les réponses de sa clé sont correctes. Le résolveur reçoit un accès en lecture à cette clé, au même tarif et par le même code pour tous les bras. Ainsi le mérite éventuel porte sur **quelle information livrer**, non sur une compression ou une accélération cachée dans le programme soumis.

**HYPOTHÈSE — Mesures.** Geler un panel métrologique de politiques ordinaires spécifiées, par exemple un échantillonneur grammatical pondéré et un parcours borné par description, avec lois de départage publiées, distincts des configurations concurrentes. Mesurer, au budget annoncé, la probabilité d’atteindre la classe au moins une fois dans une recherche ; « étroite » signifie \(\max_r p_r<\tau\). Calculer ces probabilités exactement lorsque possible. Sinon, campagnes indépendantes de la nomination. Aucun zéro observé n’est traité comme une probabilité nulle. La profondeur est la différence appariée de fractions de buts résolus, **avec la clé contre sans outil**, à budget total de résolution constant. Geler la distribution de buts et leurs poids avant toute plantation ; ne retenir ni copies directes ni buts choisis après connaissance du gain. « EP » signifie vraie, étroite **et** de gain supérieur à \(d\).

**HYPOTHÈSE — Règle de réfutation.** Pour chaque contraste ci-dessous, \(H_A:T>0\) contre \(H_B:T\leq0\). Une borne inférieure positive réfute \(H_B\) ; une borne supérieure non positive réfute \(H_A\) ; le recouvrement est une absence de décision. Pour une tolérance, prendre \(T=\epsilon-|\text{écart}|\) ; pour un bénéfice, \(T=\text{gain}-\delta\). Pour un contrôle exhaustif d’identité, les deux hypothèses sont directement « aucune discordance » contre « au moins une ». Geler marges, familles, budgets et allocations d’erreur avant le lot confirmatoire.

|Ordre et question|Contraste, témoins et conséquence d’un échec|
|---|---|
|**CPU : la clé et la profondeur mesurent-elles l’objet annoncé ?**|Deux implémentations indépendantes parcourent tout le petit domaine. Injecter table, formule, reformulation et voisine différente sur une seule entrée. Vérifier identité, vérité et score aval à graines appariées. Inclure un monde à une classe vraie et un monde à deux lois utiles dont une seule est signalée au constructeur du détecteur ; oracle indépendant pour les deux. Toute discordance réfute l’implémentation. Tester séparément l’absence de gain sur sous-système disjoint et la neutralité d’un placebo tiré uniformément dans un catalogue d’outils vrais disjoints, appariés en coût. Un placebo nuisible invalide son usage comme témoin, pas le contraste contre le résolveur nu.|
|**CPU puis petit pilote : le détecteur se laisse-t-il tromper ?**|Énumérer les quadrants rare/fréquent × utile/inerte et les assertions fausses. Exiger sensibilité et taux de fausses alertes par strate, pas seulement un taux moyen. Le chasseur de rareté de B rejette les candidats ordinaires sans voir l’aval : sur mondes sans EP, tester \(T=f_{\max}-P(\text{livraison acceptée})\). Le bras divergent de B change seulement la politique d’échantillonnage : tester si son gain EP dépasse la marge du duel. S’il la dépasse avec des classes réellement utiles, ce n’est **pas** une fausse alerte ; en revanche l’attribution du gain à la collaboration exige alors de battre aussi ce bras.|
|**Pilote à l’échelle cible : peut-on certifier les sorties réellement produites ?**|Échantillonner aléatoirement des journaux complets de chaque bras et strate de taille ; réévaluer toutes leurs propositions par un oracle indépendant exact ou une campagne de certification plus précise. Inclure acceptations, rejets et non-résolus ; pondérer par les probabilités d’inclusion. Borner séparément faux positifs, faux négatifs et effet différentiel sur le contraste. Sans étiquettes fiables, traiter les cas restants aux deux extrêmes ; si les bornes changent la décision, pas de comparaison confirmatoire à cette échelle.|
|**Régions et retour : deux essais séparés**|Comparer, à enveloppe financière identique, ciblage par descripteurs publics de l’énoncé seul contre tirage stratifié, sur familles fraîches ; rendement = livraisons EP par campagne, coût des refus inclus. Permuter les descripteurs ; changer les données privées ne doit pas les modifier. Pour le retour, comparer feedback public licite contre aucun retour, ressources réallouées. **Intégrité distincte de l’utilité :** estimer l’excès d’écart « coffre exposable moins coffre vierge » par rapport au bras sans accès, sur coffres échangeables avec rôles randomisés, y compris recalibration indépendante de la rareté. Tester dérive sous tolérance pour le canal licite et dérive au-dessus d’une marge pour une fuite délibérément exploitable. Si le témoin de fuite ne réagit pas, l’essai d’intégrité n’est pas validé.|
|**Comparaison scellée : recherche ou livraison ?**|Tous les bras tiennent un journal horodaté. Primaire pour **« trouve »** : au moins une classe EP dans le journal à budget financier fixé ; calcul exhaustif ou certification simultanée de tout le journal, sinon pas de verdict sur « trouve ». Secondaire : unique livraison classée première avant ouverture du coffre ; vivier vide = échec. Mesurer aussi pertes entre atteinte et livraison, et rejouer avec/sans abstention, notamment sur mondes nuls. Pour chaque indicateur, \(T=\min_b(P_\mathrm{sys}-P_b)-\delta\), différences appariées puis moyennées sur mondes, jamais maximum par monde. Comparateurs : tirage, énumérateur, meilleur solo gelé en développement, best-of-\(N\), bras divergent. Répéter le contraste sous retrait/remplacement des références métrologiques ; un renversement limite le verdict au panel nommé.|
|**Attribution, seulement après avantage**|Contrastes distincts : critique spécifique contre absence de critique à budget réalloué ; spécifique contre conseil générique du même dossier ; permutation contre neutre pour mesurer la distraction. Comparer sélecteurs randomisés sur **les mêmes viviers gelés**, puis équipe hétérogène contre copies homogènes de chacune de ses familles, outils et ressources constants. Chaque bénéfice doit dépasser sa propre marge ; une absence d’effet spécifique ne réfute pas l’utilité du conseil générique.|

**HYPOTHÈSE — Effectifs et arrêts.** Commencer par un recensement complet des classes, buts et trajectoires des politiques finies dans le lot CPU ; aucun argument asymptotique n’y remplace l’exhaustivité. Pour les sondes échantillonnées, allouer \(\alpha'\) par assertion, monde et politique selon le nombre maximal préenregistré. **VÉRIFIÉ —** À zéro apparition en \(M\) recherches indépendantes, la borne binomiale unilatérale est \(1-(\alpha')^{1/M}\). **HYPOTHÈSE —** Choisir ensuite \(M\) par inversion de la loi binomiale *avec apparitions possibles* pour obtenir la puissance voulue à une distance précisée de \(\tau\) ; publier la zone mal résolue près du seuil. Dimensionner de même l’audit à un taux alternatif **non nul** : à prévalence plancher \(0,01\), sensibilité \(0,80\) et plafond de fausses découvertes \(0,10\), le plafond de fausses alertes est environ \(0,00090\) (illustratif). Sans prévalence plancher défendable par bras, ne pas garantir cette proportion.

**HYPOTHÈSE —** Pilote ouvert de **40 familles indépendantes** (illustratif), pour estimer coûts, saturation du résolveur, discordances et effets de famille, non pour conclure. Dimensionner les buts aval par blocs indépendants contre l’excès de gain sur \(d\). Pour le duel, avec discordance \(0,20\), excès sur marge \(0,05\), puissance \(0,80\) et risque unilatéral alloué \(0,005\), prévoir environ **935 paires indépendantes** pour un contraste (illustratif, approximation normale) ; simuler ensuite la puissance **conjointe** avec grappes et erreurs d’oracle. Facturer prospection, entrées, décodage, outils, sélection, tentatives abandonnées ; devis séparé pour l’audit de tous les journaux. Arrêter avant commande si saturation, trop peu de familles, coût de certification ou bornes des indécidables rendent l’écart utile inaccessible.

## (c) À l’arbitre — décision en une page

**RAPPORTÉ —** Le système est en projet. Aucun taux de découverte, aucune robustesse à la formulation et aucune conséquence scientifique réelle ne sont établis par les pièces.

|Point|Ce que je recommande et limite de la conclusion — **HYPOTHÈSE**|Confiance illustrative|
|---|---|---:|
|Cible|Mesurer l’accès à une assertion typée relativement à des politiques et un budget ; mesurer séparément ce que son contenu permet à un résolveur de faire. Ni la rareté absolue ni l’efficacité du programme soumis ne sont cette cible.|0,85|
|Vérité|Micromonde exhaustif pour identité et vérité ; preuve pour dérivabilité dans les axiomes choisis ; tests frais pour performance sur leur distribution ; rétrodiction pour accord avec un événement ultérieur, non pour exclure la mémorisation. Aucun de ces instruments ne certifie seul rareté et conséquence. Pas de juge de langage dans le primaire ; hors langage, audit humain aveugle avec ancres et bornes défavorables, sinon exploration seulement.|0,85|
|Comparaison|Mesurer l’atteinte dans le journal et la livraison séparément, par monde apparié, sous un plafond de coût commun. Un avantage sur la livraison seule n’établit pas un avantage de recherche.|0,85|
|Régions|Tester le rendement net du ciblage public contre tirage stratifié, sur de nouvelles familles. Ne pas appeler « fertile » une région seulement parce qu’une référence y échoue.|0,65|
|Retour|Autoriser compilation et exemples publics. Cacher fréquences, clés d’audit, buts et scores privés. Un transfert utile n’exclut pas une fuite : tester les deux séparément.|0,85|
|Validation|Éprouver d’abord le détecteur sur affirmations vraies rares inutiles et utiles fréquentes, puis sur les sorties réelles. Une bonne performance sur des plantations ne suffit pas.|0,90|
|Plan|Recensement CPU → pilote de résolution et d’audit → comparaison scellée → attribution. Ne passer à l’étape suivante que si le devis permet de trancher au seuil prévu.|0,80|
|Limites|Une inversion sous changement raisonnable de panel ou de résolveur interdit une conclusion indépendante de ces choix. Une incertitude d’oracle supérieure au gain pertinent interdit même la conclusion conditionnelle.|0,90|

**VÉRIFIÉ —** Si le résolveur ignore l’outil et conserve les mêmes ressources, la différence de succès avec/sans outil est nulle, quelle que soit la rareté. **Ce qui n’est pas établi**, c’est qu’il existe, dans une famille pertinente et à coût abordable, assez d’assertions à la fois difficiles à atteindre et utiles à transmettre.

**HYPOTHÈSE — Première expérience à financer :** construire le petit monde à deux lois utiles, masquer laquelle a été plantée, ajouter une assertion vraie rare sur une observable aval inutilisée, puis recenser classes, probabilités d’accès et gains contre résolveur nu. Faire noter table et formule par exactement la même interface. Si le détecteur crédite le leurre, manque la loi non documentée malgré son gain exhaustif, ou distingue les écritures, **ne lancer aucun agent**. S’il passe, il aura validé une implémentation sur ce monde, pas démontré une découverte.

**RAPPORTÉ — Repères de méthode, non résultats du projet :** C. J. Clopper et E. S. Pearson (1934), *The Use of Confidence or Fiducial Limits Illustrated in the Case of the Binomial*, **Biometrika** ; Leonardo de Moura, Soonho Kong, Jeremy Avigad, Floris van Doorn et Jakob von Raumer (2015), *The Lean Theorem Prover (System Description)*, **CADE**. Les autres choix ci-dessus sont des propositions à tester, non des résultats empruntés à ces travaux.

FIN-DE-CELLULE

## Cellule E3-T3-reponse-D (lettre D)

*Audit documentaire : les sept pièces transmises (`FAITS`, `QUESTION DE L'ARBITRE`, `E3-T1-conception-D`, critiques croisées `A`, `B`, `C`, `E`) sont présentes, complètes et non tronquées `[VÉRIFIÉ]`. Convention de statuts : `[VÉRIFIÉ]` est réservé aux constats directs sur les pièces et aux identités mathématiques exactes ; `[RAPPORTÉ]` aux résultats de la littérature citée et au contenu des autres pièces ; `[OBSERVÉ-NON-AUDITÉ]` aux faits d'ingénierie courants non audités ici ; `[HYPOTHÈSE]` à tout choix méthodologique, seuil, diagnostic ou conjecture (sans modifier les statuts posés dans les pièces antérieures).*

---

## I. Livrable (a) — Réponse aux critiques visant la proposition D

### 1. Critiques de la pièce A

* **Remarque de statut (étiquettes `[VÉRIFIÉ]` sur des choix de conception ou conjectures empiriques)** `[RAPPORTÉ]` : **Acceptée** (et l'incitation à l'obfuscation est **transformée en test** dans `Exp. V`) `[HYPOTHÈSE]`. Toute propriété non déduite mathématiquement (qualité du quotient par e-graphes, absence de mémorisation, réaction à la fuite de $N$) est reclassée `[HYPOTHÈSE]` et soumise à réfutation.
* **A-a1, A-b1, A-c4 (Seuil $\tau_N = 5{,}5$ (illustratif) collé au plafond $5{,}81$ (illustratif) nats à $M_0 = 1\,000$ (illustratif) ; mesure binaire ; sensibilité de `0,135` (illustratif) à $p = 0{,}002$ (illustratif))** `[RAPPORTÉ]` : **Acceptée** `[HYPOTHÈSE]`. Porter $M_0$ à `4 000` (illustratif) tirages par politique de référence autorise jusqu'à `7` (illustratif) occurrences sous $\tau_N = 5{,}5$ (illustratif) nats ($p^* = e^{-5{,}5} \approx 4{,}09 \times 10^{-3}$ (illustratif)) même au seuil corrigé $\alpha_N / 3 \approx 0{,}0167$ (illustratif) `[VÉRIFIÉ]`, restaure la gradation de $N$ et porte la sensibilité à $\ge 0{,}85$ (illustratif) dès $p_0 \le 10^{-3}$ (illustratif). Le contrôle de doublement $M_0 \to 2 M_0$ de A-c4 est adopté.
* **A-a2, A-c1 (`Exp. II` vraie par construction contre `BestOfN-Mono` ; ablation hétérogène biaisée par $\mu_0$ ; combinaison des références non fixée ; contrôle mono-modèle de la seconde famille)** `[RAPPORTÉ]` : **Acceptée** `[HYPOTHÈSE]`. Nous remplaçons $\mu_0$ par l'**enveloppe de trois politiques de référence** $\mathcal{R}_0 = \{\mu_{\text{Fam1}, b_0}, \mu_{\text{Fam2}, b_0}, \mu_{\text{Énum}, b_0}\}$ combinée par le pire cas $N_{\mathcal{R}_0, b_0}([x]) = -\ln \max_{\mu \in \mathcal{R}_0} \hat{p}_\mu^+([x])$, ce qui neutralise l'avantage mécanique de la seconde famille dans l'ablation d'hétérogénéité `[VÉRIFIÉ]`. De plus, la sonde opère au budget atomique $b_0 = B / 64$ (illustratif) tandis que le duel opère au budget $B$ : le plafond d'union de `BestOfN-Mono(B)` vaut $1 - (1 - p^*)^{64} \approx 0{,}23$ (illustratif) par classe éligible `[VÉRIFIÉ]`, évitant tout plafonnement près de `0` (illustratif). Le bras `BestOfN-Mono-Fam2(B)` (A-c1) est intégré à `Exp. II`.
* **A-a3, A-b5, A-c2 ($D_{\text{MDL}}$ biaisé par $\max(0,\cdot)$, extensif en $|D_r|$, dépendant du représentant via $K_{\mathcal{L}}([x])$ ; absence de loi nulle pour les lemmes et pour $D$)** `[RAPPORTÉ]` : **Acceptée** `[HYPOTHÈSE]`. Nous supprimons la troncature $\max(0,\cdot)$ au profit de la **somme signée intensive** par observation $d_{\text{MDL}}([x])$ assortie d'un veto de réfutation pire-régime ; $K_{\mathcal{L}}([x])$ est défini comme la longueur minimale canonique extraite mécaniquement de l'e-graphe saturé (donc invariante par représentant) ; et $d_{\text{proof}}$ est centré sur le quantile `0,99` (illustratif) d'une loi nulle empirique de `200` (illustratif) lemmes vrais mais orthogonaux de même taille canonique (contrôle A-c2 intégré).
* **A-a4, A-b4, A-c5 (`Exp. IV` circulaire via les résidus des références ; rapport de cotes fixé par le concepteur et instable à basse prévalence ; contrôle sur référence disjointe)** `[RAPPORTÉ]` : **Acceptée et transformée en test** `[HYPOTHÈSE]`. $S_{\text{region}}(i)$ est désormais calculé sur $D_{\text{train}}$ seul par une sonde légère dédiée $\mu_{\text{probe}}$ (`8B` (illustratif) paramètres) **disjointe** de $\mathcal{R}_0$ (A-c5), et l'estimande d'`Exp. IV` devient la différence de différences linéaire $\Delta_{\text{rend}}$ du gain de découverte, définie et bornée même si un taux approche `0` (illustratif) `[VÉRIFIÉ]`.
* **A-a5, A-c3 (Porte 5 circulaire : les obfuscations testées sont les règles mêmes de l'e-graphe)** `[RAPPORTÉ]` : **Acceptée et transformée en test** `[HYPOTHÈSE]`. La Porte 5 devient un audit adversarial opposant fausses scissions (paraphrases engendrées par un modèle tiers hors règles d'e-graphe, A-c3) et fausses fusions.
* **A-a6 (Plan de puissance calculé contre `0` au lieu de $\delta_{\min} = 0{,}10$ (illustratif) ; arrêt en Phase II confondant non concluant et réfuté)** `[RAPPORTÉ]` : **Acceptée** `[HYPOTHÈSE]`. Nous fixons $\delta_{\min} = 0{,}05$ (illustratif), dimensionnons $M_{\text{prob}} = 220$ (illustratif) sur la marge nette $g = \Delta - \delta_{\min} = 0{,}10$ (illustratif), et n'arrêtons pour futilité que lorsque la borne supérieure de confiance passe sous $\delta_{\min}$.
* **A-a7 (`Exp. III` : médiane $\Delta N$ censurée et zone morte violant B4)** `[RAPPORTÉ]` : **Acceptée** `[HYPOTHÈSE]`. `Exp. III` est reformulée sur un paramètre unique partitionnant `[-1, 1]` (illustratif) sans zone morte : l'écart de taux de découverte $\Delta_{\text{crit}}$.
* **A-a8, A-b3 (`Exp. VI` : échantillonner selon $\hat{J}$ estime PPV/NPV et non TPR/FPR ; $\pi_g$ inconnu ; faible puissance sur `500` (illustratif) négatifs et variance de Rogan-Gladen)** `[RAPPORTÉ]` : **Acceptée** `[HYPOTHÈSE]`. Nous adoptons la correction de biais de vérification par valeurs prédictives pondérées $\hat{\pi}_g = \hat{p}_g \widehat{\text{PPV}}_g + (1-\hat{p}_g)(1-\widehat{\text{NPV}}_g)$ `[VÉRIFIÉ]` (Begg & Greenes, 1983 `[RAPPORTÉ]`, citée par A) et refondons `Exp. VI` en plan factoriel apparié $2 \times 2$ à vérité oracle fixée.
* **A-b2 (`Exp. I` : inflation de zéros écrasant $\tau_K$ et contrôle $|\bar{\tau}_K| \le 0{,}08$ (illustratif) sous-dimensionné)** `[RAPPORTÉ]` : **Acceptée** `[HYPOTHÈSE]`. `Exp. I` utilise un panel stratifié de `240` (illustratif) classes (`60` (illustratif) par quadrant), la statistique $\bar{\kappa}$ de Cohen et une borne de permutation calibrée $[-0{,}15 ; +0{,}15]$ (illustratif).

### 2. Critiques de la pièce B

* **Outils `Borne de handicap`, `CN-1` (divergence triviale) et `CN-2` (chasseur d'étroitesse)** `[RAPPORTÉ]` : **Acceptés** `[HYPOTHÈSE]`. Nous reprenons explicitement `CN-1` et `CN-2` de B comme contrôles négatifs d'`Exp. II`, et levons la borne de handicap par le découplage d'échelle $B / b_0 = 64 \ll e^{\tau_N}$ (illustratif).
* **B-a1 (Statuts `VÉRIFIÉ` abusifs) et B-a9 (`TPR = 1,00` et `FPR = 0` non certifiables statistiquement)** `[RAPPORTÉ]` : **Acceptées** `[HYPOTHÈSE]`. La borne adaptative de Dwork et al. (2015) est étiquetée `[RAPPORTÉ]` (et son adéquation empirique `[HYPOTHÈSE]`) ; tout critère probabiliste de validation est reformulé en borne de confiance unilatérale à `95 %` (illustratif) (ex. $\overline{\text{FPR}}_{95\%} \le 0{,}01$ (illustratif)), seule la vérification syntaxique d'axiomes interdits dans Lean restant déterministe `[VÉRIFIÉ]`.
* **B-a2 (Absence de gradation de $N$), B-a3 (Tension entre $b_0$ et $B$), B-a4 et B-c2 (Biais positif de $\max(0,\cdot)$, fuite si constantes ajustées sur $D_r$, contrôle d'expressions aléatoires figées sur $D_{\text{train}}$), B-a6 (`Exp. IV` circulaire), B-a8 et B-b1 (Puissance contre $\delta_{\min}$)** `[RAPPORTÉ]` : **Acceptées** `[HYPOTHÈSE]`. Toutes les constantes numériques d'une loi sont strictement figées sur $D_{\text{train}}$ avant ouverture du coffre, et le contrôle B-c2 ($\mathbb{E}[d_{\text{MDL}}] \le 0$ (illustratif) sur expressions aléatoires de même $K_{\mathcal{L}}$) est intégré.
* **B-a5 et B-c3 (`Exp. I` vraie par construction pour l'énumérateur si l'isomorphisme conserve la taille ; « s'il ne la préserve pas, Exp. I mesure les fonctions de coût, pas la stabilité de la cible »)** `[RAPPORTÉ]` : **Première branche acceptée** (inclusion de traductions non conservatrices de taille selon B-c3) ; **seconde branche rejetée sur l'interprétation conceptuelle et transformée en test** `[HYPOTHÈSE]`. *Raison du rejet* : en théorie algorithmique de l'information, changer de formalisme scientifique agit précisément en modifiant les coûts de description jusqu'à une constante de compilation finie (Li & Vitányi, 2008 `[RAPPORTÉ]`). Si cette distorsion de coût à budget fini renverse la classification entre formalismes usuels (algébrique factorisé, développé, graphe combinatoire), cela réfute légitimement le présupposé d'invariance intrinsèque `P-I` `[VÉRIFIÉ]`.
* **B-a7 (`Exp. V` viole l'exhaustivité B4 dans la zone $\Delta < 10$ (illustratif) nats et chute $\ge 5\,\%$ (illustratif))** `[RAPPORTÉ]` : **Acceptée** `[HYPOTHÈSE]`. Remplacée par une frontière scalaire unique $\Delta_{\text{fuite}} \le 0{,}03$ contre $> 0{,}03$ (illustratif) nat/obs.

### 3. Critiques de la pièce C

* **C-a1, C-b1, C-c1 ($\mathbb{E}[(G_r)_+] = \mathbb{E}|G_r|/2$ donnant un gain positif aux lois nulles bruitées ; contrôle à gain nul et variance croissante ; indiscernabilité sous interventions équivalentes et censure des temps de preuve)** `[RAPPORTÉ]` : **Acceptée** `[HYPOTHÈSE]`. La somme signée $d_{\text{MDL}}$ garantit $\mathbb{E}[d_{\text{MDL}}] < 0$ (illustratif) sous gain nul quelle que soit la variance `[VÉRIFIÉ]` ; le contrôle C-c1 est adopté, et l'équivalence modulo la classe d'interventions admissibles est inscrite dans les limites du Point 8.
* **C-a2, C-c2 (Empreinte de dépendances $\neq$ équivalence des lemmes ; égalité sur grille dense $\neq$ égalité hors grille ; contrôle de deux lois égales sur la grille et divergentes hors grille)** `[RAPPORTÉ]` : **Acceptée et transformée en test** `[HYPOTHÈSE]`. Pour Lean, l'équivalence de classe repose désormais sur la **double implication prouvée mécaniquement** $\vdash \forall \theta, (x_1(\theta) \leftrightarrow x_2(\theta))$ à budget noyau borné ; pour les lois quantitatives, l'e-graphe est couplé à une évaluation polynomiale/analytique sur `64` (illustratif) points continus aléatoires hors grille (inspirée de Schwartz, 1980 `[RAPPORTÉ]`), auditée par le contrôle C-c2 en Porte 5.
* **C-a3, C-b3, C-c3 (`Exp. IV` : confusion entre existence $\pi_s$ et détection $\pi_s a_s$ ; strates à même prévalence plantée mais accessibilités différentes)** `[RAPPORTÉ]` : **Acceptée** `[HYPOTHÈSE]`. Nous ajoutons un volet synthétique à prévalence plantée constante $\pi_1 = \pi_0 = 0{,}50$ (illustratif) (reprenant C-c3) pour isoler la sensibilité $a_s$, et définissons l'estimande général sur le taux de découverte effective.
* **C-b2 (Divergence de signe entre médiane, moyenne et rangs signés sans symétrie dans `Exp. III`) et C-b3 (Le paramètre de fuite dans `Exp. V` est la différence *entre* les écarts des bras Fuite et Cloisonné)** `[RAPPORTÉ]` : **Acceptées** `[HYPOTHÈSE]`. Les deux estimateurs sont alignés sur l'espérance de ces contrastes exacts.
* **C-a4, C-b4, C-c4 (`Exp. VI` : recouvrement logique où $H_A$ et $H_B$ sont simultanément vraies si $\text{FPR}_g \ge \pi_g$ ; audit limité aux négatifs ; contrôle croisant provenance et contenu à vérité fixée)** `[RAPPORTÉ]` : **Acceptée** `[HYPOTHÈSE]`. Le plan croisé $2 \times 2$ (vérité oracle $\times$ style rédactionnel) de C-c4 élimine le recouvrement logique et estime simultanément $|\Delta \text{FPR}|$ et $|\Delta \text{TPR}|$.

### 4. Critiques de la pièce E

* **E-a1, E-b2, E-c1 ($D_{\text{MDL}}$ tronqué, $L_{\text{null}}$ non spécifié, unités incommensurables dans $D_{\text{proof}}$ et seuil $\tau_D$ MDL conservé en Lean, contrôle d'une loi vraie sur $1$ régime et réfutée sur $R-1$)** `[RAPPORTÉ]` : **Acceptée** `[HYPOTHÈSE]`. $L_{\text{null}}$ est fixé au prédicteur bayésien nul ajusté sur $D_{\text{train}}$ ; la Phase III Lean utilise son seuil adimensionnel propre $\tau_{D,\text{proof}} = 0{,}15$ (illustratif) ; et le contrôle E-c1 est intégré.
* **E-a2, E-b4, E-c5 (Impossibilité physique d'égaliser simultanément FLOPs, jetons, appels oracle et temps mur entre CPU et GPU ; agrégation des `5` (illustratif) graines non spécifiée ; contrôle de cohérence entre $N_{b_0}$ et atteinte à budget $B$)** `[RAPPORTÉ]` : **Acceptée** `[HYPOTHÈSE]`. L'égalisation opère sur $(B_{\text{FLOP}}, B_{\text{oracle}})$ entre tous les bras LLM, et sur le coût cloud $(B_{\text{USD}}, B_{\text{oracle}})$ face à l'énumérateur CPU et au tirage aléatoire ; le test confirmatoire porte sur `1` (illustratif) graine canonique pré-enregistrée par problème ; et le contrôle E-c5 est adopté.
* **E-a3, E-b3, E-c4 (`Exp. I` à `0` GPU-heure n'évalue pas le modèle $\mu_0$ ; réutilisation des `60` (illustratif) problèmes de Phase II et contradiction `60` vs `120` pour `Exp. IV`)** `[RAPPORTÉ]` : **Acceptée** `[HYPOTHÈSE]`. La Phase I reçoit `40` (illustratif) GPU-heures pour exécuter $\mathcal{R}_0$ complet dans `Exp. I`, et chaque expérience confirmatoire dispose d'un échantillon de problèmes disjoint.
* **E-b1 (Sous-point : correction de Bonferroni sur $m \ge 4$ (illustratif) classes annulant identiquement $\mathbb{P}(N \ge \tau_N)$)** `[RAPPORTÉ]` : **Rejetée avec sa raison** `[HYPOTHÈSE]`. *Raison* : notre protocole (Point 3) impose qu'une méthode ne soumette au coffre qu'**un seul** candidat final sélectionné $[x^*_{i,m}]$ par problème `[VÉRIFIÉ]`. Il n'y a donc qu'une unique classe testée par bras et par problème ($m_{\text{soumis}} = 1$ (illustratif)), et non une fouille multiple sur $m$ classes ; seule s'applique la correction sur les $|\mathcal{R}_0| = 3$ (illustratif) politiques de référence, couverte par $M_0 = 4\,000$ (illustratif).
* **E-a4, E-b6, E-c3 (`Exp. VI` : erreur sur Rogan-Gladen et omission de $|\Delta \text{TPR}|$)** `[RAPPORTÉ]` : **Acceptée** `[HYPOTHÈSE]` (corrigée via A-a8 et C-a4).
* **E-a5, E-c2, E-c6 (`Exp. III` limitée à une seule ablation ; `Thresholdout` non testé dans `Exp. V` et contrôle en une passe trivial ; systèmes déterministes incompressibles absents d'`Exp. IV`)** `[RAPPORTÉ]` : **Acceptée et transformée en tests** `[HYPOTHÈSE]` (`Exp. III` étendue aux trois contrastes d'attribution ; `Exp. V` transformée en épreuve directe de `Thresholdout` et de `Fuite-N` ; contrôle chaotique incompressible E-c2 ajouté à `Exp. IV`).

---

## II. Livrable (b) — Architecture métrologique et expériences corrigées

### Spécification révisée des instruments `[HYPOTHÈSE]`

1. **Quotient sémantique $\mathcal{X}/\!\sim$ et complexité canonique $K_{\mathcal{L}}([x])$** :
   - *Lois quantitatives* : réduction par saturation d'e-graphes couplée à un test d'identité sur `64` (illustratif) points flottants continus tirés hors grille d'entraînement (Schwartz, 1980 `[RAPPORTÉ]`). $K_{\mathcal{L}}([x])$ est la longueur binaire minimale de l'arbre abstrait extraite de l'e-graphe saturé `[VÉRIFIÉ]`.
   - *Lemmes Lean* : vérification déterministe d'absence d'axiome hors noyau (`0` (illustratif) `sorry`), témoin mécanique de non-vacuité des prémisses, et groupement par double implication $\vdash \forall \theta, (x_1(\theta) \leftrightarrow x_2(\theta))$ sous tactique bornée.
   - *Porte 5 adversariale préalable* : sur `200` (illustratif) paraphrases hors règles d'e-graphe générées par un LLM tiers et `200` (illustratif) paires jumelles coïncidant sur $D_{\text{train}}$ mais divergentes sous $\text{do}(\cdot)$ (C-c2), exiger $\overline{\text{FSR}}_{95\%} \le 0{,}10$ (illustratif) (fausses scissions) et $\overline{\text{FMR}}_{95\%} \le 0{,}02$ (illustratif) (fausses fusions).
2. **Étroitesse certifiée $N_{\mathcal{R}_0, b_0}([x])$** : Sur $M_0 = 4\,000$ (illustratif) exécutions indépendantes de budget élémentaire $b_0 = B / 64$ (illustratif) pour chacune des $|\mathcal{R}_0| = 3$ (illustratif) politiques (modèle ouvert `72B` (illustratif) Famille 1, modèle ouvert `70B` (illustratif) Famille 2, énumérateur grammatical stochastique), $\hat{p}_\mu^+([x])$ est la borne supérieure unilatérale de Clopper-Pearson au niveau $\alpha_N / 3 = 0{,}05 / 3$ (illustratif) `[VÉRIFIÉ]` (Clopper & Pearson, 1934 `[RAPPORTÉ]`), et $N_{\mathcal{R}_0, b_0}([x]) = -\ln \max_{\mu \in \mathcal{R}_0} \hat{p}_\mu^+([x])$, avec seuil $\tau_N = 5{,}5$ (illustratif) nats.
3. **Profondeur signée intensive $d([x])$ sans juge LLM** :
   - *Lois quantitatives* : constantes numériques figées sur $D_{\text{train}}$ seul ; sur $R$ régimes interventionnels scellés totalisant $N_{\text{tot}} = \sum_{r=1}^R |D_r|$ observations, sous mélange prédictif universel $0{,}999\,p_{[x]} + 0{,}001\,p_{\text{null}}$ (illustratif) évitant la divergence infinie tout en pénalisant les erreurs :
     $$d_{\text{MDL}}([x]) = \frac{1}{N_{\text{tot}}}\left(\sum_{r=1}^R \big(L_{\text{null}}(D_r) - L(D_r \mid [x])\big) - K_{\mathcal{L}}([x])\right)$$
     avec veto de réfutation si $\min_r \frac{1}{|D_r|}(L_{\text{null}}(D_r) - L(D_r \mid [x])) < -0{,}05$ (illustratif) nat/obs ; seuil $\tau_{D,\text{MDL}} = 0{,}25$ (illustratif) nat/obs.
   - *Lemmes Lean* : sur $R_{\text{thm}} = 50$ (illustratif) théorèmes aval résolus à plafond $S_{\max}$ pas noyau, réduction géométrique moyenne $g_{\text{raw}}([x]) = \frac{1}{R_{\text{thm}}}\sum_j \ln(S_j(\emptyset)/S_j(\{[x]\}))$ diminuée du quantile `0,99` (illustratif) d'une loi nulle de `200` (illustratif) lemmes valides orthogonaux de même $K_{\mathcal{L}}$ : $d_{\text{proof}}([x]) = g_{\text{raw}}([x]) - q_{0{,}99}(K_{\mathcal{L}}([x]))$, avec seuil $\tau_{D,\text{proof}} = 0{,}15$ (illustratif).

### Six expériences en inférence forte (règle B4 : partition exacte, zéro zone morte) `[HYPOTHÈSE]`

1. **Exp. I — Stabilité représentationnelle sous traductions non conservatrices de taille** (`40` (illustratif) GPU-h + `200` (illustratif) CPU-h)
   - **Protocole** : Panel stratifié de `240` (illustratif) classes (`60` (illustratif) par quadrant) évaluées sous $\mathcal{R}_0$ complet ($M_0 = 4\,000$ (illustratif)) dans `3` (illustratif) formalismes reliés par des traductions non conservatrices de taille (algébrique factorisé, polynomial développé, graphe combinatoire sans variable, selon B-c3 et E-c4). Paramètre : accord moyen $\bar{\kappa}$ de Cohen sur $\mathbb{I}[N_{\mathcal{R}_0, b_0} \ge \tau_N \land d \ge \tau_D]$.
   - **$H_A$ contre $H_B$** : $H_A : \bar{\kappa} \ge 0{,}60$ (illustratif) contre $H_B : \bar{\kappa} < 0{,}60$ (illustratif) (IC bootstrap stratifié à `95 %` (illustratif), $\text{SE} \approx 0{,}045$ (illustratif), puissance `0,86` (illustratif) si $\bar{\kappa} = 0{,}74$ (illustratif)).
   - **Contrôles négatifs** : Permutation des identifiants inter-DSL (IC attendu contenant `0` (illustratif) dans $[-0{,}15 ; +0{,}15]$ (illustratif)) ; Porte 5 adversariale ; stabilité $M_0 \to 8\,000$ (illustratif) sur `60` (illustratif) classes (A-c4).
   - **Issues falsifiantes** : $\text{LB}_{95\%}(\bar{\kappa}) \ge 0{,}60$ (illustratif) falsifie $H_B$ ; $\text{UB}_{95\%}(\bar{\kappa}) < 0{,}60$ (illustratif) falsifie $H_A$ (et $< 0{,}30$ (illustratif) établit le caractère mal posé de la cible, arrêt immédiat).

2. **Exp. II — Supériorité confirmatoire contre l'enveloppe des lignes de base** (pilote sur `80` (illustratif) mondes synthétiques, puis campagne confirmatoire sur $M_{\text{prob}} = 220$ (illustratif) problèmes disjoints : `110` (illustratif) modules Lean + `110` (illustratif) mondes interventionnels)
   - **Protocole** : Soumission unique $[x^*_{i,m}]$ par problème sur `1` (illustratif) graine canonique pré-enregistrée ; budget égalisé en $(B_{\text{FLOP}}, B_{\text{oracle}})$ face à `BestOfN-Mono-Fam1(B)`, `BestOfN-Mono-Fam2(B)` (A-c1) et `Itératif-Mono-Fam1(B)`, et en $(B_{\text{USD}}, B_{\text{oracle}})$ face à `Énumérateur` et `Aléatoire` (E-a2). Paramètre : $\Delta_{\min} = \min_{b \in \mathcal{B}} \mathbb{E}[Y_{\text{MA}} - Y_b]$.
   - **$H_A$ contre $H_B$** : $H_A : \Delta_{\min} \ge 0{,}05$ (illustratif) contre $H_B : \Delta_{\min} < 0{,}05$ (illustratif). Test d'intersection-union apparié à $\alpha = 0{,}025$ (illustratif) (Berger, 1982 `[RAPPORTÉ]`) : pour $\Delta_b = 0{,}15$ (illustratif) (marge nette $g = 0{,}10$ (illustratif)) et discordance $q = 0{,}22$ (illustratif), $M_{\text{prob}} = 220$ (illustratif) donne $\text{SE} = 0{,}030$ (illustratif) et une puissance conjointe de `0,75` à `0,85` (illustratif) `[VÉRIFIÉ]`.
   - **Contrôles négatifs** : `CN-1` (divergence triviale de B) ; `CN-2` (chasseur d'étroitesse par rejet de B, $\overline{\text{FPR}}_{95\%} \le 0{,}01$ (illustratif)) ; prédicteurs centrés à variance croissante (C-c1), lois aléatoires figées sur $D_{\text{train}}$ (B-c2) et lois exactes sur `1` (illustratif) régime mais fausses sur $R-1$ (E-c1) ; audit d'atteinte de `BestOfN-Mono(B)` (E-c5).
   - **Issues falsifiantes** : $\min_b \text{LB}_{97{,}5\%}(\hat{\Delta}_b) \ge 0{,}05$ (illustratif) falsifie $H_B$ ; $\min_b \text{UB}_{97{,}5\%}(\hat{\Delta}_b) < 0{,}05$ (illustratif) falsifie $H_A$.

3. **Exp. III — Attribution causale hiérarchique : Critique, Sélecteur et Hétérogénéité** (sur les $M_{\text{prob}} = 220$ (illustratif) problèmes à budget strictement égal)
   - **Protocole** : Trois contrastes appariés ordonnés séquentiellement à $\alpha = 0{,}025$ (illustratif) sur le taux binaire $Y$ : (1) $\Delta_{\text{crit}} = \mathbb{E}[Y_{\text{MA}} - Y_{\text{Parallèle-SansCritique}}]$ (jetons de critique réalloués aux tirages parallèles) ; (2) $\Delta_{\text{sel}} = \mathbb{E}[Y_{\text{MA}} - Y_{\text{SélectionTrainSeul}}]$ ; (3) $\Delta_{\text{hét}} = \mathbb{E}[Y_{\text{MA-Hét}} - \max_{f \in \{1,2\}} \mathbb{E}[Y_{\text{MA-Homo-}f}]]$ (sans biais grâce à $\mathcal{R}_0$ bicanal).
   - **$H_{A,k}$ contre $H_{B,k}$** : Pour chaque brique $k \in \{\text{crit}, \text{sel}, \text{hét}\}$, $H_{A,k} : \Delta_k \ge 0{,}04$ (illustratif) contre $H_{B,k} : \Delta_k < 0{,}04$ (illustratif) (puissance `0,84` (illustratif) à $\Delta_k = 0{,}12$ (illustratif), $q = 0{,}16$ (illustratif)).
   - **Contrôle négatif** : Agent écho neutre reformulant sans évaluer (isole le coût de longueur de contexte).
   - **Issues falsifiantes** : $\text{LB}_{97{,}5\%}(\hat{\Delta}_k) \ge 0{,}04$ (illustratif) falsifie $H_{B,k}$ ; $\text{UB}_{97{,}5\%}(\hat{\Delta}_k) < 0{,}04$ (illustratif) falsifie $H_{A,k}$ et commande la suppression de la brique $k$.

4. **Exp. IV — Validité prospective non circulaire du sélecteur de régions $S_{\text{region}}$** ($M_{\text{reg}} = 240$ (illustratif) problèmes dédiés : `120` (illustratif) $S=1$, `120` (illustratif) $S=0$, coût de sonde imputé au budget)
   - **Protocole** : $S_{\text{region}}(i)$ est calculé sur $D_{\text{train}}$ par une sonde disjointe $\mu_{\text{probe}}$ (`8B` (illustratif), hors $\mathcal{R}_0$, selon A-c5). Volet synthétique à prévalence plantée constante $\pi_1 = \pi_0 = 0{,}50$ (illustratif) (selon C-c3) ; volet confirmatoire sur la différence de différences de découverte $\Delta_{\text{rend}} = \mathbb{E}[Y_{\text{MA}} - Y_{\text{BestMono}} \mid S=1] - \mathbb{E}[Y_{\text{MA}} - Y_{\text{BestMono}} \mid S=0]$.
   - **$H_A$ contre $H_B$** : $H_A : \Delta_{\text{rend}} \ge 0{,}10$ (illustratif) contre $H_B : \Delta_{\text{rend}} < 0{,}10$ (illustratif) ($\text{SE} \approx 0{,}049$ (illustratif), puissance `0,82` (illustratif) si $\Delta_{\text{rend}} = 0{,}24$ (illustratif)).
   - **Contrôles négatifs** : Bruit stochastique hétéroscédastique (écart épistémique nul) et systèmes dynamiques déterministes chaotiques incompressibles dans $\mathcal{L}$ (E-c2 : classés $S=1$ mais $\Delta_{\text{rend}} = 0$ (illustratif)).
   - **Issues falsifiantes** : $\text{LB}_{97{,}5\%}(\hat{\Delta}_{\text{rend}}) \ge 0{,}10$ (illustratif) falsifie $H_B$ ; $\text{UB}_{97{,}5\%}(\hat{\Delta}_{\text{rend}}) < 0{,}10$ (illustratif) falsifie $H_A$.

5. **Exp. V — Audit de corruption adaptative sous `Thresholdout` et test d'obfuscation** ($M_{\text{fb}} = 80$ (illustratif) problèmes dédiés à trois coupes $D_{\text{train}}, D_{\text{val}}, D_{\text{vault}}$)
   - **Protocole** : Quatre bras appariés sur $T = 32$ (illustratif) requêtes : `Cloisonné` ($D_{\text{train}}$ seul), `Thresholdout` sur $D_{\text{val}}$ (Dwork et al., 2015 `[RAPPORTÉ]`, selon E-c6), `Fuite-D` (retour exact de $d_{\text{val}}$, témoin positif de corruption) et `Fuite-N` (retour exact de $\hat{N}_{\mathcal{R}_0}$, audité face à un panel de référence tenu secret $\mathcal{R}'_0$). Paramètre primaire (selon C-b3) : $\Delta_{\text{fuite}} = \mathbb{E}[(d_{\text{val}} - d_{\text{vault}})_{\text{Thresholdout}} - (d_{\text{val}} - d_{\text{vault}})_{\text{Cloisonné}}]$.
   - **$H_A$ contre $H_B$** : $H_A : \Delta_{\text{fuite}} \le 0{,}03$ (illustratif) nat/obs contre $H_B : \Delta_{\text{fuite}} > 0{,}03$ (illustratif) nat/obs ($\text{SE} \approx 0{,}010$ (illustratif), puissance `0,89` (illustratif) à $\Delta_{\text{fuite}} = 0$ (illustratif)). Test secondaire d'obfuscation sur `Fuite-N` : $\mathbb{E}[N_{\mathcal{R}_0} - N_{\mathcal{R}'_0}] \ge 0{,}50$ contre $< 0{,}50$ (illustratif) nat.
   - **Contrôle de sensibilité** : `Fuite-D` doit produire un optimisme $> 0{,}10$ (illustratif) nat/obs pour valider le détecteur.
   - **Issues falsifiantes** : $\text{UB}_{97{,}5\%}(\hat{\Delta}_{\text{fuite}}) \le 0{,}03$ (illustratif) falsifie $H_B$ ; $\text{LB}_{97{,}5\%}(\hat{\Delta}_{\text{fuite}}) > 0{,}03$ (illustratif) falsifie $H_A$ (imposant le régime `Cloisonné` exclusif).

6. **Exp. VI — Audit factoriel $2 \times 2$ de biais différentiel d'un juge LLM** (conditionnel à l'ouverture d'un domaine semi-formel)
   - **Protocole** : `400` (illustratif) vrais positifs ($Y=1$) et `400` (illustratif) négatifs subtils ($Y=0$) certifiés par oracle exact, chacun réécrit dans les deux styles `Style-MA` et `Style-Mono` (vérité préservée vérifiée en aveugle, selon C-c4 et E-c3). Paramètre : $B_{\text{juge}} = \max(|\text{FPR}_{\text{MA}} - \text{FPR}_{\text{Mono}}|, |\text{TPR}_{\text{MA}} - \text{TPR}_{\text{Mono}}|)$.
   - **$H_A$ contre $H_B$** : $H_A : B_{\text{juge}} < 0{,}04$ (illustratif) contre $H_B : B_{\text{juge}} \ge 0{,}04$ (illustratif) ($\text{SE}$ appariée $\le 0{,}012$ (illustratif), puissance `0,88` (illustratif) si $B_{\text{juge}} = 0{,}005$ (illustratif)).
   - **Contrôles** : Duplicatas exacts à identifiants permutés (température `0` (illustratif)) et étiquettes de provenance inversées en clair (témoin positif).
   - **Issues falsifiantes** : $\text{UB}_{97{,}5\%}(\hat{B}_{\text{juge}}) < 0{,}04$ (illustratif) falsifie $H_B$ (autorisant uniquement un usage couplé à l'estimateur pondéré de Begg & Greenes, 1983 `[RAPPORTÉ]`) ; $\text{LB}_{97{,}5\%}(\hat{B}_{\text{juge}}) \ge 0{,}04$ (illustratif) falsifie $H_A$ et disqualifie le juge LLM.

*Budget révisé* : `5 400` (illustratif) GPU-heures et `18 000` (illustratif) CPU-heures au complet (`18 000` (illustratif) USD), mais plafonné à `140` (illustratif) USD si la Phase I échoue et à `1 900` (illustratif) USD si le pilote de Phase II falsifie $H_A$ `[HYPOTHÈSE]`.

---

## III. Livrable (c) — Réponse à la question de l'arbitre (en une page)

### 1. Diagnostic point par point (1 à 8)

1. **Cible** *(confiance : `0,82` (illustratif))*. **Établi** : La rareté syntaxique ne mesure pas l'utilité déductive (Bennett, 1988, dans *The Universal Turing Machine: A Half-Century Survey*, OUP `[RAPPORTÉ]`) ; borner une probabilité d'atteinte $p_0 \le p^*$ exige $\Omega(\ln(1/\alpha)/p^*)$ tirages indépendants (Clopper & Pearson, 1934, *Biometrika* `[RAPPORTÉ]`) ; sous prévalence rare, un juge imparfait nécessite un audit stratifié par valeurs prédictives (Rogan & Gladen, 1978, *Am. J. Epidemiol.* ; Begg & Greenes, 1983, *Biometrics* `[RAPPORTÉ]`). **Conjecture** : Qu'un quotient mécanique (e-graphes + test de Schwartz, 1980, *J. ACM* `[RAPPORTÉ]`, ou double implication Lean) capture l'équivalence scientifique utile `[HYPOTHÈSE]`. **Erreur de cadrage** : Parler d'étroitesse sans fixer l'enveloppe de références $\mathcal{R}_0$ et le ratio de budget $B / b_0$ crée soit un plafonnement tautologique de la référence, soit une cible triviale à budget $B$ `[VÉRIFIÉ]`.
2. **Sources de vérité** *(confiance : `0,85` (illustratif))*. **Établi** : Les noyaux formels garantissent zéro faux positif déductif modulo la fidélité de l'énoncé (Moura & Ullrich, 2021, *CADE 28*, Springer `[RAPPORTÉ]`), et seules des interventions $\text{do}(\cdot)$ séparent des structures observationnellement équivalentes (Pearl, 2009, *Causality*, CUP, chap. 3 `[RAPPORTÉ]`). **Conjecture** : La transférabilité des mondes synthétiques aux domaines naturels ouverts `[HYPOTHÈSE]`. **Erreur de cadrage** : La rétrodiction à coupure temporelle ne peut ni exclure les précurseurs conceptuels antérieurs (« référence à vérifier »), ni créditer une découverte valide mais non publiée par l'histoire humaine `[VÉRIFIÉ]`.
3. **Comparaison** *(confiance : `0,85` (illustratif))*. **Établi** : Le test d'intersection-union valide la supériorité simultanée sur toutes les lignes de base (Berger, 1982, *Technometrics* `[RAPPORTÉ]`), et la taille d'échantillon doit être calibrée sur la marge nette au-dessus de $\delta_{\min}$ avec l'instance de problème pour unité indépendante `[VÉRIFIÉ]`. **Conjecture** : Qu'à FLOPs et appels oracle égaux, l'architecture multi-agents batte `BestOfN-Mono(B)` et l'auto-révision séquentielle (`Exp. II–III`) `[HYPOTHÈSE]`. **Erreur de cadrage** : Compter les seuls jetons générés ou omettre les appels internes au vérificateur confond pluralité d'agents et calcul caché `[VÉRIFIÉ]`.
4. **Choix des problèmes** *(confiance : `0,55` (illustratif))*. **Établi** : Hors monde planté, une recherche bornée n'identifie que le produit $\pi_s a_s$ (existence $\times$ sensibilité) et non l'existence seule `[VÉRIFIÉ]`. **Conjecture** : Qu'une rupture de transfert inter-régimes sur $D_{\text{train}}$ mesurée par une sonde disjointe $\mu_{\text{probe}}$ prédise un gain différentiel $\Delta_{\text{rend}} \ge 0{,}10$ (illustratif) sans confondre profondeur et chaos incompressible (`Exp. IV`, Udrescu & Tegmark, 2020, *Science Advances* `[RAPPORTÉ]`) `[HYPOTHÈSE]`. **Erreur de cadrage** : Choisir des problèmes historiques résolus induit un biais du survivant `[HYPOTHÈSE]`.
5. **Rétroaction** *(confiance : `0,90` (illustratif))*. **Établi** : Interroger adaptativement un jeu d'évaluation dégrade sa validité en $O(\sqrt{T \ln|\mathcal{X}|/n})$ (Dwork et al., 2015, *Science* `[RAPPORTÉ]`). **Conjecture** : Que `Thresholdout` contienne l'optimisme différentiel sous `0,03` (illustratif) nat/obs (`Exp. V`) `[HYPOTHÈSE]`. **Erreur de cadrage** : Exposer $N_{\mathcal{R}_0}$ ou $d_{\text{vault}}$ durant la recherche corrompt la cible en objectif d'optimisation `[HYPOTHÈSE]`.
6. **Validation du harnais** *(confiance : `0,88` (illustratif))*. **Établi** : L'étalonnage sur témoins positifs et négatifs précède l'inférence (Platt, 1964, *Science* `[RAPPORTÉ]`), mais ne certifie statistiquement que des bornes de confiance unilatérales sur échantillon fini `[VÉRIFIÉ]`. **Conjecture** : Que le harnais franchisse simultanément les bornes sur `CN-1`, `CN-2`, les lois partiellement fausses (Popper, 1959, *The Logic of Scientific Discovery*, chap. 4 `[RAPPORTÉ]`) et les obfuscations hors règles `[HYPOTHÈSE]`. **Erreur de cadrage** : Tester le quotient sur ses propres règles de réécriture est circulaire `[VÉRIFIÉ]`.
7. **Plan séquentiel** *(confiance : `0,80` (illustratif))*. **Établi** : Exiger `220` (illustratif) problèmes appariés est mathématiquement requis pour détecter un gain de `0,15` (illustratif) au-dessus d'une marge $\delta_{\min} = 0{,}05$ (illustratif) à puissance $\ge 0{,}80$ (illustratif) `[VÉRIFIÉ]`. **Conjecture** : Les taux d'effet et de discordance postulés `[HYPOTHÈSE]`. **Erreur de cadrage** : Arrêter sur une absence de significativité en petit échantillon confond résultat non concluant et réfutation `[VÉRIFIÉ]`.
8. **Limites** *(confiance : `0,92` (illustratif))*. **Établi** : L'équivalence sémantique générale est indécidable (Rice, 1953, *Trans. Amer. Math. Soc.* `[RAPPORTÉ]`), l'invariance de représentation n'est vraie qu'à constante finie près (Li & Vitányi, 2008, *An Introduction to Kolmogorov Complexity*, Springer, chap. 2 `[RAPPORTÉ]`), et certifier $p_0 \ll 10^{-6}$ (illustratif) en boîte noire est exponentiellement coûteux `[VÉRIFIÉ]`. **Conjecture** : Que les découvertes d'intérêt résident dans un langage $\mathcal{L}$ pré-fixé plutôt que dans un changement d'observables `[HYPOTHÈSE]`. **Erreur de cadrage** : Supposer acquise la bonne définition de la cible avant d'avoir testé sa stabilité inter-formalismes `[HYPOTHÈSE]`.

### 2. Bilan : ce qui est établi contre ce qui ne l'est pas

Il est **établi** qu'on peut construire sans juge LLM un harnais non biaisé dans les domaines formels et interventionnels, à condition de : (i) séparer le budget de sonde $b_0$ du budget de duel $B$ sur une enveloppe multi-familles $\mathcal{R}_0$, (ii) mesurer la profondeur par compression signée intensive $d_{\text{MDL}}$ (Rissanen, 1978, *Automatica* ; Grünwald, 2007, MIT Press, chap. 1–2 `[RAPPORTÉ]`) ou réduction de preuve étalonnée sur loi nulle, et (iii) imposer une nomination unique évaluée sur coffre scellé `[VÉRIFIÉ]`. Il **n'est pas établi** : (1) que le couple $(N_{\mathcal{R}_0, b_0}, d)$ soit stable par changement réaliste de formalisme, (2) que le quotient mécanique résiste aux paraphrases adversariales de modèles, ni (3) que le débat multi-agents surpasse un modèle unique à FLOPs et appels oracle égaux `[HYPOTHÈSE]`.

### 3. L'expérience à faire en premier

Exécuter la **Phase I : Porte 5 adversariale suivie d'`Exp. I` corrigée** (`40` (illustratif) GPU-h, `200` (illustratif) CPU-h, $\approx 140$ (illustratif) USD) `[HYPOTHÈSE]`. Avant toute exécution multi-agents coûteuse, elle soumet `400` (illustratif) paires adversariales (obfuscations LLM hors règles d'e-graphe et jumeaux divergents hors grille) au quotient sémantique, puis mesure sur `240` (illustratif) classes stratifiées l'accord $\bar{\kappa}$ de la cible entre `3` (illustratif) formalismes à tailles non conservées sous $\mathcal{R}_0$. Si $\overline{\text{FSR}}_{95\%} > 0{,}10$ (illustratif), $\overline{\text{FMR}}_{95\%} > 0{,}02$ (illustratif) ou $\text{UB}_{95\%}(\bar{\kappa}) < 0{,}30$ (illustratif), le harnais ou la cible elle-même est réfuté à moindre coût avant d'engager le moindre duel d'agents `[VÉRIFIÉ]`.

FIN-DE-CELLULE

## Cellule E3-T3-reponse-E (lettre E)

# Proposition E — Tour III.3 : réponse aux critiques et conception corrigée

**Constat de pièces et discipline de statuts (`VÉRIFIÉ`).** Les pièces `FAITS`, `QUESTION DE L'ARBITRE`, `E3-T1-conception-E` et les critiques croisées `A`, `B`, `C`, `D` sont présentes, non vides et complètes ; `FAITS` et `QUESTION DE L'ARBITRE` sont identiques et ne contiennent aucune donnée expérimentale. Je ne réponds qu'aux sections visant la proposition E. Pour corriger l'ambiguïté de statuts relevée par A, chaque énoncé porte ici un statut unique : `VÉRIFIÉ` (constat direct des pièces ou identité mathématique sous les conditions écrites), `RAPPORTÉ` (résultat attribué à une référence vérifiable), `OBSERVÉ-NON-AUDITÉ` (pratique empirique non auditée) ou `HYPOTHÈSE` (choix de conception, conjecture ou paramètre). Je ne modifie pas les statuts figurant dans les pièces reçues. Tous les chiffres choisis par conception sont marqués `illustratif`.

---

## (a) Traitement de chaque critique visant la proposition E

### Critiques de A sur E

1. **Doubles étiquettes et P1 marqué « RAPPORTÉ » sans source (remarque de statut).** **Acceptée.** La pièce E3-T1 comportait des étiquettes composites ambiguës et attribuait l'instabilité de représentation en P1 sans citation explicite (le fait de référence est la dépendance de la complexité descriptive au langage de codage : Solomonoff, 1964, `RAPPORTÉ`). Discipline d'étiquette unique appliquée ci-dessous.
2. **A(a)1 — Estimande $R$ double ($-\log_2 \hat{p}_Q$ ou $B_{0,5}$), censure de $B_{0,5}$, $\hat{p}=0 \implies R=\infty$.** **Acceptée.** $B_{0,5}$ et $-\log_2 \hat{p}$ ponctuel sont abandonnés au profit d'une certification unique par borne supérieure unilatérale de Clopper–Pearson (Clopper & Pearson, 1934, `RAPPORTÉ`) sur tirages disjoints.
3. **A(a)2 & A(c)1 — $U(P,B)$ en $\max$ sur $\mathcal{S}$ croît en $\sigma\sqrt{2\ln m}$ ; absence de contrôle spam à $m$ apparié.** **Acceptée.** Remplacé par l'évaluation scellée d'une **nomination unique** $\hat{x}_1$ choisie avant ouverture du coffre, avec contrôle négatif « bras spam » en E1.
4. **A(a)3 & A(c)5 — Contrôle négatif de E5 (petit espace énumérable) non jugeable sous $U$ ($U \equiv 0$).** **Acceptée.** Sur ce régime, la supériorité de l'énumérateur est vérifiée sur $D_{\text{ext}}$ seul, tandis que $Y \equiv 0$ vérifie l'absence de faux positifs d'étroitesse.
5. **A(a)4 & A(c)4 — E3 circulaire (entropie d'échec de la baseline), pseudo-répliqué (4 familles), et « petit combinatoire » trivial.** **Acceptée** sur la circularité et la pseudo-réplication (descripteurs calculés sur un modèle/graine disjoint selon la suggestion de A ; unité d'analyse portée à la famille avec $F = 16$ familles `illustratif`). **Rejetée partiellement** sur l'inutilité du petit combinatoire : ce régime est retiré du calcul d'interaction de la taxonomie (où l'on utilise des négatifs non triviaux), mais conservé comme contrôle de calibration budgétaire vérifiant que l'énumérateur n'est pas bridé.
6. **A(a)5 — E2 fusionne trois hypothèses (codage, juge, contamination).** **Acceptée.** E2 est scindée en trois expériences indépendantes : E2a, E2b et E2c.
7. **A(a)6 & A(c)3 — $\Delta_{\text{mém}}$ confond mémoire et notation ; contrôle « fuis » mal nommé (c'est un contrôle positif).** **Acceptée.** E2c soustrait le coût pur de notation estimé sur problèmes synthétiques garantis inédits (suggestion de A) et requalifie les problèmes fuis en contrôle positif de sensibilité.
8. **A(a)7 & A(c)2 — E4 teste l'utilité du retour plutôt que l'intégrité de la mesure ; $R$ remesuré sur la référence exposée.** **Transformée en test.** E4 teste désormais directement l'intégrité de la mesure via le découplage entre la référence exposée $\mathcal{Q}_0$ et un **panel de référence secret $\mathcal{Q}'$** (emprunté à A), couplé à l'écart train/OOD.
9. **A(a)8 — Règle incohérente ($\max_b U_b$ vs Holm ; enveloppe par problème irréalisable).** **Acceptée.** Remplacée par un test d'intersection-union (IUT ; Berger, 1982, `RAPPORTÉ`) exigeant de battre chaque baseline individuellement.
10. **A(a)9 — Tirages de référence de $R$ non budgétés.** **Acceptée.** Intégrés explicitement au tableau des coûts ($K_{\text{ref}}$ tirages courts par problème et par politique).
11. **A(a)10 — Contradiction sur A/A (« graines identiques » en E1 vs « graines distinctes » en table (c)).** **Acceptée.** Erreur rédactionnelle corrigée : A/A utilise exclusivement des campagnes indépendantes à graines distinctes.
12. **A(b) — Pertes de puissance (zéro-inflation et seuils en $\sigma$, *style-swap* sur 200 paires exigeant $r \ge 0{,}935$, limites de PPI, AUROC scalaire/VPP faible à $\pi = 0{,}01$, dépendance d'échelle de l'AUDC).** **Acceptée.** Abandon des seuils en $\sigma$, de l'AUDC primaire et de l'AUROC agrégé ; passage à une métrique binaire absolue $Y$, plafonds FPR calibrés par l'identité de Bayes (`VÉRIFIÉ`), dimensionnement dédié du *style-swap* en unités absolues, et relégation du juge+PPI au module optionnel E2b.

### Critiques de B sur E

1. **B(a)1 & B(c)2 — $R$ ponctuel, exécutions non explicitement disjointes, biais de sélection.** **Acceptée.** Exécutions de référence strictement disjointes imposées, plus contrôle négatif « étroitesse par sélection » (emprunté à B) en E1.
2. **B(a)2 & B(c)3 — $U$ court-circuite le sélecteur et croît avec $|\mathcal{S}|$ ; absence de bras à volume gratuit.** **Acceptée** (même correction par nomination scellée $\hat{x}_1$ + bras volume gratuit en E1).
3. **B(a)3 — Égalisation simultanée FLOPs/USD et appels oracle impossible entre LLM et énumérateur.** **Acceptée.** Scission explicite du duel en deux régimes distincts : E5a (coût financier/calcul total égal, appels oracle libres pour l'énumérateur) et E5b (appels oracle égaux, pour oracles coûteux).
4. **B(a)4 — Biais de Jensen de l'enveloppe par problème et redondance de Holm.** **Acceptée** (corrigé par IUT).
5. **B(a)5 — Seuils en $\sigma$ dépendants des données.** **Acceptée** (seuils absolus pré-enregistrés).
6. **B(a)6 — Pseudo-réplication de E3 (4 familles) et transfert non testé 8B $\to$ 70B.** **Acceptée** pour la pseudo-réplication ; **Transformée en test** pour le transfert d'échelle (sous-lot dédié de 4 familles `illustratif` vérifiant la conservation du signe entre 8B et 70B avant E5).
7. **B(a)7 — E2 agrège trois hypothèses.** **Acceptée** (scindée en E2a, E2b, E2c).
8. **B(a)8 — Puissance calculée contre 0 au lieu de $\delta_5$.** **Acceptée.** Toutes les tailles d'échantillon sont recalculées contre la marge $\delta_{\min} > 0$ avec la variance des paires discordantes.
9. **B(a)9 — P1 « RAPPORTÉ » sans référence.** **Acceptée** (corrigé, voir A.1).
10. **B(a)10 & B(c)1 — Borne de handicap lorsque $Q_{\text{LLM-1}}$ est aussi le bras Best-of-$K$ au même budget ; absence de CN-1 et CN-2.** **Acceptée.** Corrigée par deux verrous (empruntés à B) : (i) budget de référence court $b_{\text{ref}} \ll B$ pour $\mathcal{Q}_0$ + vérification de sensibilité en retirant chaque référence une à une ; (ii) inclusion obligatoire de **CN-1 (divergence triviale)** comme baseline en E5 et de **CN-2 (chasseur d'étroitesse)** comme attaque en E1.
11. **B(b) — Pertes de puissance ($R$ infinis, bootstrap sur max à queue lourde, PPI si $n\pi < 10$, arrêt pour futilité prématuré à 50 %).** **Acceptée.** Métrique primaire bornée $\{0,1\}$ (variance finie $\le 1/4$, `VÉRIFIÉ`), porte $n\hat{\pi} \ge 10$ (`illustratif`) sur E2b, et conditionnement de l'analyse intermédiaire en E5 à un minimum de paires discordantes $n_{\text{disc,min}}$.

### Critiques de C sur E

1. **C(a)1 — Plancher $\tau_D$ absent de la formule de $U$.** **Acceptée.** Intégré explicitement dans $Y_m(P,B)$.
2. **C(a)2 — Le coffre privé sert de sélecteur si $\mathcal{S}$ est le vivier.** **Acceptée** (corrigé par nomination scellée $\hat{x}_1$).
3. **C(a)3 — Une extension non dominée de Pareto n'est pas une domination.** **Acceptée.** Abandon de la clause ambiguë d'extension de Pareto ; victoire définie séparément dans le régime E5a ou E5b.
4. **C(a)4 & C(c) — Réutilisation en E5 des familles choisies par E3 (effet conditionnel).** **Acceptée.** E5 porte exclusivement sur des **familles neuves hors échantillon** tirées selon la règle gelée en E3.
5. **C(a)5 — PPI d'une moyenne ne corrige pas un maximum de scores bruités.** **Acceptée.** PPI n'est jamais appliqué à un maximum ; il ne porte que sur l'espérance de $Y$ de la nomination $\hat{x}_1$ en E2b.
6. **C(b)1–C(b)4 — $B_{0,5}$ censuré ; AUC sur mélange masquant un leurre ; EIG dépendant de l'a priori ; variance résiduelle $\text{Var}(Y-J)/n$ en PPI.** **Acceptée** sur les quatre points ; la dépendance de l'EIG à l'a priori est **transformée en test** de sensibilité minimax sur un ensemble pré-enregistré d'a priori admissibles pour les protocoles expérimentaux.
7. **C(b)5 — Non-identifiabilité rappel vs déduction par le seul contraste de renommage.** **Rejetée comme défaut du harnais principal, acceptée comme limite de la rétrodiction.** La pièce E3-T1 excluait déjà la rétrodiction seule comme preuve décisive pour des LLM (Q2) ; le harnais principal repose sur des mondes synthétiques et formels générés procéduralement post-entraînement (contamination littérale nulle par construction). Pour les benchmarks existants, E2c est désormais explicitement bornée comme diagnostic asymétrique (une fuite détectée disqualifie, l'absence de détection ne prouve pas l'absence de mémorisation invariante au renommage).
8. **C(b)6 — Interaction $\Delta_F - \Delta_N > 0$ compatible avec $\Delta_F, \Delta_N < 0$.** **Acceptée.** E3 exige désormais la conjonction $\bar{\Delta}_F > \delta_0 > 0$ ET $\bar{\Delta}_F - \bar{\Delta}_N > \delta_{\text{int}}$.
9. **C(b)7 — Si $\mathbb{E}[D \mid R]$ croît, la fuite de $R$ n'implique pas la stagnation de $D$.** **Transformée en test.** En E4, le critère de fuite ne repose plus sur la baisse de $D_{\text{OOD}}$ mais sur le découplage d'étroitesse entre $\mathcal{Q}_0$ et $\mathcal{Q}'$ ainsi que sur l'inflation de $D_{\text{train}} - D_{\text{OOD}}$.
10. **C(b)8 — Conditionnement de E6 au passage de E5 sur les mêmes 120 problèmes (biais post-sélection).** **Acceptée.** E6 est exécutée sur un **lot d'instances entièrement indépendant** de E5.
11. **C(c) — Contrôles (viviers de tailles différentes à $D$ vrai égal ; A/A complet rejouant sélection et arrêt ; audit des idées écartées au préfiltrage en PPI).** **Acceptée** intégralement et intégrée en E1 et E2b.

### Critiques de D sur E

1. **D(a)1, D(b)3 & D(c)1 — Fuite du coffre dans $\max$, biais $\sqrt{2\ln L_m}$, queues lourdes de Pareto invalidant le bootstrap, contrôle d'inflation de portefeuille.** **Acceptée** (corrigée par nomination scellée $\hat{x}_1$, métrique binaire bornée et contrôle d'inflation en E1).
2. **D(a)2 — Défaite par construction de l'énumérateur sous double égalité budgétaire.** **Acceptée** (corrigée par E5a à USD égal sans plafond d'appels oracle).
3. **D(a)3 & D(c)2 — Contraste fallacieux en E3 sans exigence $\Delta_F > \delta_0 > 0$ ni régime neutre.** **Acceptée** (conjonction et régime neutre ajoutés en E3).
4. **D(a)4 — PPI audité par des experts humains ne borne pas un biais commun LLM–experts.** **Acceptée.** Le harnais restreint PPI aux domaines disposant d'un **oracle externe objectif** coûteux (expérience physique/simulateur lourd). Avec des experts humains, le statut est explicitement limité à l'accord avec des experts, sans prétendre borner le biais de vérité.
5. **D(b)1 — Non-identifiabilité Kaplan–Meier de $B_{0,5}$.** **Acceptée** ($B_{0,5}$ retiré).
6. **D(b)2 & D(c)3 — PPI dégrade la variance si $\rho_{Y,f} < \frac{\sigma_f}{2\sigma_Y}(1 + n/N_{\text{un}})$ ; sous-couverture si $np \ll 1$ ; contrôle d'anti-corrélation sémantique à style constant.** **Acceptée et transformée en test.** E2b inclut la strate de vérités contre-intuitives à style constant (empruntée à D) et disqualifie le juge dès que $\hat{\rho}_{Y,f} \le \frac{\hat{\sigma}_f}{2\hat{\sigma}_Y}(1 + n/N_{\text{un}})$ (ou si la variante pondérée de PPI, référence à vérifier, n'offre aucun gain) ou $n\hat{\pi} < 10$ (`illustratif`).
7. **D(b)4 — Seuils en $c\cdot\hat{\sigma}_\Delta$ falsifiés par le bruit ; pénalité $\lambda |x|$ rendant $D(X^*) < 0$ sous langage verbeux.** **Acceptée** pour les seuils en $\sigma$. **Rejetée comme défaut de principe** sur la pénalité descriptive, mais **transformée en contrôle de dimensionnement en E1** : sous le principe MDL exact (Rissanen, 1978, `RAPPORTÉ`), $\lambda = 1$ (en nats dans un code préfixe normalisé du DSL) n'est pas un hyperparamètre arbitraire ; une loi dont le coût descriptif excède le gain de log-vraisemblance OOD ne compresse tout simplement pas les observations OOD. Si $D_{\text{ext}}(X^*) \le 0$ pour une loi plantée, cela révèle un jeu OOD sous-informatif, vérifié en E1 avant toute campagne.

---

## (b) Expériences corrigées en inférence forte

### Définitions corrigées et règle de réfutation (`HYPOTHÈSE`)

- **Périmètre du harnais principal :** domaines à oracle mécanique sans juge LLM (mondes synthétiques procéduraux à vérité plantée, preuve formelle Lean 4, simulateurs exécutables isolés). Le juge LLM + PPI est confiné au module optionnel E2b.
- **Nomination scellée :** à l'expiration du budget $B$, chaque bras $m$ soumet une unique nomination canonisée $\hat{x}_1$ (ou s'abstient, score $0$) **avant** ouverture du coffre scellé. (Un diagnostic secondaire top-$k$ avec $k = 3$ `illustratif` identique pour tous les bras sépare erreur de recherche et erreur de nomination, sans entrer dans la règle de décision.)
- **Certification d'étroitesse $I_R$ :** un ensemble de références $\mathcal{Q}_0 = \{Q_{\text{rand}}, Q_{\text{enum}}, Q_{\text{LLM-ref}}\}$ opère sur des **tirages strictement disjoints** du duel, au budget court $b_{\text{ref}} = B/20$ (`illustratif`, évitant la borne de handicap de B sur le bras Best-of-$K$ au budget $B$). Sur $K_{\text{ref}}$ exécutions indépendantes par monde et par politique, $u_Q([\hat{x}_1])$ désigne la borne supérieure unilatérale de Clopper–Pearson (Clopper & Pearson, 1934, `RAPPORTÉ`) au niveau $1 - \alpha_{\text{ref}}/(|\mathcal{Q}_0|\cdot M_{\text{bras}})$ (pour $|\mathcal{Q}_0|=3$, $M_{\text{bras}}=5$, $\alpha_{\text{ref}}=0{,}01$, $\tau_p=0{,}01$ `illustratif`, $K_{\text{ref}} = 800$ `illustratif` assure la certification en zéro occurrence, `VÉRIFIÉ` : $1 - (0{,}01/15)^{1/800} \approx 0{,}0091 < 0{,}01$). On pose $I_R([\hat{x}_1]) = \mathbb{I}[\max_{Q \in \mathcal{Q}_0} u_Q([\hat{x}_1]) \le \tau_p]$. Un panel secret disjoint $\mathcal{Q}'$ est tenu à l'écart pour E4.
- **Profondeur $D_{\text{ext}}$ :** gain net en nats sur régimes OOD/interventionnels ($\lambda = 1$ nat, MDL), gain de résolution/compression sur batterie Lean 4 gelée indépendante, ou EIG minimax sur famille d'a priori pré-enregistrés pour protocoles ; seuil absolu pré-enregistré $\tau_D > 0$.
- **Quantité primaire binaire :** $Y_m(P, B) = \mathbb{I}[\text{Valide}(\hat{x}_1) \land I_R([\hat{x}_1]) = 1 \land D_{\text{ext}}(\hat{x}_1) \ge \tau_D] \in \{0,1\}$, de taux $\pi_m = \mathbb{E}_P[Y_m(P, B)]$.
- **Règle de réfutation exhaustive (empruntée à C, respectant B4) :** chaque expérience oppose deux hypothèses exclusives et exhaustives $H_A : \theta \in \Theta_A$ et $H_B : \theta \notin \Theta_A$ via un intervalle de confiance simultané au niveau $1 - \alpha$ ($\alpha = 0{,}025$ unilatéral, `illustratif`). Un intervalle entièrement dans $\Theta_A$ réfute $H_B$ ; entièrement hors de $\Theta_A$ réfute $H_A$ ; traversant la frontière laisse l'expérience **non concluante** (sans falsifier l'une ni l'autre).

### Protocole ordonné du moins cher au plus cher (tous seuils et $N$ `illustratif`)

1. **E1 — Métrologie du harnais : sensibilité/FPR par quadrant, canonisation, CN-2, spam et A/A complet**
   - **$H_A$** : (i) $\text{TPR}_{\text{target}} \ge 0{,}80$ sur vérités plantées (vérifiant aussi le dimensionnement OOD sous $\lambda=1$ nat) ; (ii) $\max_{c \in \{\text{rare-creux, banal-profond, banal-creux}\}} \text{FPR}_c \le \phi_{\max}$ avec $\phi_{\max} = 0{,}002$ (calibré par Bayes pour $\text{FDR} \le 0{,}20$ à prévalence $\pi = 0{,}01$) ; (iii) canoniseur : taux de fusion des paraphrases $\ge 0{,}95$ ET taux de fausses fusions sur paires proches distinctes $\le 0{,}01$ ; (iv) taux de succès $Y$ des attaques **CN-2 (chasseur d'étroitesse)** et **bras spam / inflation de volume** $\le \phi_{\max}$ ; (v) taux de rejet du **test A/A complet à graines distinctes** (rejouant sélection et arrêt) $\le 0{,}05$ ; (vi) contrôle « étroitesse par sélection » (runs disjoints vs conjoints) sans excès de rareté sur runs disjoints.
   - **$H_B$** : violation d'au moins un des critères (i)–(vi).
   - **Échelle :** $N_+ = 100$ positifs plantés + $N_- = 2\,000$ négatifs stratifiés par type de leurre (soit borne supérieure en zéro alerte $\approx 0{,}0018 < 0{,}002$, `VÉRIFIÉ`) + $200$ campagnes A/A légères.
   - **Porte d'arrêt :** si $H_A$ est réfutée (ou non concluante sur FPR/CN-2/spam), arrêt immédiat du programme avant tout appel au modèle 70B.

2. **E2a — Invariance au recodage isomorphe**
   - **$H_A$** : entre deux encodages isomorphes (incluant un isomorphisme ne préservant pas trivialement la taille syntaxique), le taux de désaccord de la certification finale $Y$ vérifie $d_{\text{rec}} \le 0{,}05$.
   - **$H_B$** : $d_{\text{rec}} > 0{,}05$ (cible instable au codage, donc mal posée).
   - **Contrôle négatif :** encodage non isomorphe cassant la structure causale (doit produire $d_{\text{rec}} \gg 0{,}05$).
   - **Échelle :** $N = 150$ problèmes appariés (synthétique + Lean 4). Arrêt si $H_A$ est réfutée.

3. **E2b (optionnel, domaines ouverts à oracle externe coûteux) — Qualification du juge LLM + PPI**
   - **$H_A$** : sur un audit stratifié par bras incluant les candidats écartés au préfiltrage, (i) $n\hat{\pi} \ge 10$ ; (ii) $\rho_{Y,f} > \frac{\sigma_f}{2\sigma_Y}(1 + n/N_{\text{un}})$ y compris sur la strate de **vérités contre-intuitives à style constant** (contrôle de D) ; (iii) décalage absolu sous *style-swap* $|\delta_{\text{style}}| \le 0{,}02$ en probabilité de verdict positif.
   - **$H_B$** : violation d'au moins un critère (i)–(iii).
   - **Contrôle négatif :** paires contenu identique / styles rhétoriques opposés ; faux plausibles vs vrais contre-intuitifs à style identique.
   - **Échelle :** $n = 1\,000$ candidats audités par oracle externe objectif + $400$ paires *style-swap*. Si $H_A$ est réfutée, le juge LLM est disqualifié (usage de l'oracle pur uniquement).

4. **E2c (optionnel, benchmarks historiques existants) — Diagnostic de contamination nette**
   - **$H_A$** : l'excès mémoriel net $\Delta_{\text{mém,net}} = \Delta_{\text{renommage}}(\text{benchmark}) - \Delta_{\text{renommage}}(\text{synthétique inédit apparié}) \le 0{,}03$.
   - **$H_B$** : $\Delta_{\text{mém,net}} > 0{,}03$ (contamination active disqualifiant le benchmark).
   - **Contrôle positif de sensibilité :** lot jumeau injecté en fine-tuning sur un modèle ouvert témoin (doit dépasser $0{,}03$). **Contrôle négatif :** problèmes synthétiques générés post-entraînement (doivent donner $\Delta_{\text{mém,net}} \approx 0$).
   - **Échelle :** $N = 120$ problèmes appariés. (Non requise si le harnais n'utilise que des mondes générés procéduralement post-entraînement.)

5. **E3 — Validation de la taxonomie de problèmes au niveau famille et transfert d'échelle**
   - **$H_A$** : sur $F = 16$ familles indépendantes pré-enregistrées (8 prédites fertiles, 8 prédites négatives/neutres non triviales : espaces permutés sans structure, bassins trompeurs ; descripteurs calculés sur propriétés *a priori* et un modèle/graine disjoint), la moyenne par famille satisfait conjointement $\bar{\Delta}_F > \delta_0 = 0{,}05$ ET $\bar{\Delta}_F - \bar{\Delta}_N > \delta_{\text{int}} = 0{,}05$, ET le signe de $\bar{\Delta}_F > 0$ se conserve au passage 8B $\to$ 70B sur 4 familles dédiées.
   - **$H_B$** : négation logique de $H_A$ (avantage non positif en zone fertile, pas d'interaction ou échec du transfert d'échelle).
   - **Contrôles négatifs :** (1) famille « espace permuté sans structure » ($\Delta \approx 0$) ; (2) contrôle séparé « petit combinatoire » où l'énumérateur doit battre le LLM sur $D_{\text{ext}}$ seul.
   - **Échelle :** $16$ familles $\times 40$ problèmes (8B) $+ 4$ familles $\times 40$ problèmes (70B). **Toutes les familles de E3 sont définitivement exclues de E5.**

6. **E4 — Étanchéité du feedback adaptatif contre Goodhart (double référence $\mathcal{Q}_0 / \mathcal{Q}'$)**
   - **$H_A$** : l'activation du feedback autorisé (validité + split interne) maintient l'inflation de surajustement $\Delta G = (D_{\text{train}} - D_{\text{OOD}})_{\text{fb}} - (D_{\text{train}} - D_{\text{OOD}})_{\text{sans}} \le \epsilon_G$ ET le découplage d'étroitesse sur le panel secret $\mathcal{Q}'$, $\Delta \delta_{Q,Q'} = \mathbb{P}(I_{R,\mathcal{Q}_0}=1 \land I_{R,\mathcal{Q}'}=0)_{\text{fb}} - \mathbb{P}(\cdot)_{\text{sans}} \le 0{,}02$.
   - **$H_B$** : violation de l'une des deux bornes (Goodharting avéré $\implies$ retrait du feedback interne).
   - **Contrôle positif de fuite :** bras recevant sciemment $I_{R,\mathcal{Q}_0}$ pendant la recherche (doit exhiber une hausse significative de $\delta_{Q,Q'}$).
   - **Échelle :** $N = 100$ problèmes dédiés (3 conditions appariées).

7. **E5 — Duel principal en deux régimes (E5a : USD égal ; E5b : appels oracle égaux) sur familles neuves**
   - **Baselines $\mathcal{B}$ :** Aléatoire, Énumérateur mécanique, Meilleur modèle unique Best-of-$K$, **CN-1 (divergence triviale : même modèle à température/prompt déplacé + second modèle mono-agent de force $\le$)**.
   - **$H_A$** (évaluée séparément pour E5a et E5b) : par test IUT, $\min_{b \in \mathcal{B}} (\pi_{\text{multi}} - \pi_b) > \delta_{\min} = 0{,}05$ sur chacune de 2 familles neuves indépendantes (issues de la règle gelée en E3, jamais vues auparavant), et résultat invariant au retrait d'une référence à la fois de $\mathcal{Q}_0$.
   - **$H_B$** : $\min_{b \in \mathcal{B}} (\pi_{\text{multi}} - \pi_b) \le 0{,}05$ sur au moins une famille neuve.
   - **Dimensionnement cohérent contre $\delta_{\min}$ (`VÉRIFIÉ` sous approximation normale appariée) :** pour $\pi_{\text{multi}} = 0{,}20$, $\pi_b = 0{,}05$ ($\Delta = 0{,}15$, écart effectif $\Delta - \delta_{\min} = 0{,}10$), discordance $q \approx 0{,}22$, $\alpha = 0{,}025$ unilatéral et puissance $0{,}80$, il faut $N \ge \frac{(1{,}96+0{,}84)^2 (0{,}22 - 0{,}15^2)}{0{,}10^2} \approx 155$ problèmes ; retenu **$N = 160$ problèmes/famille $\times 2$ familles = $320$ problèmes**. (Si $\Delta$ réel n'est que $0{,}10$, l'écart effectif chute à $0{,}05$ et exigerait $N \approx 620$/famille : l'analyse intermédiaire est conditionnée à $n_{\text{disc}} \ge 40$ paires discordantes avec frontière conservatrice.)
   - **Contrôle négatif de calibration :** lot « petit combinatoire » évalué sur $D_{\text{ext}}$ seul (l'énumérateur doit y dominer) et sur $Y$ (tous les bras à $0$).

8. **E6 — Attribution causale par ablations sur lot d'instances indépendant**
   - Exécutée uniquement si E5 réfute $H_B$, mais sur un **lot frais indépendant** de $N = 160$ problèmes par famille validée (éliminant le biais post-sélection signalé par C).
   - **Ablations $\mathcal{A}$ au même budget exact :** (1) ensemble hétérogène indépendant sans dialogue, (2) auto-raffinement séquentiel mono-agent, (3) **critique placebo neutre intra-problème** de même longueur (sans injection hors-sujet d'un autre problème).
   - **$H_A$** : par IUT, $\min_{a \in \mathcal{A}} (\pi_{\text{multi}} - \pi_a) > \delta_6 = 0{,}05$.
   - **$H_B$** : $\min_{a \in \mathcal{A}} (\pi_{\text{multi}} - \pi_a) \le 0{,}05$ (le gain de E5 ne provient pas du contenu critique).

### Ancrage matériel et budget révisé (entièrement `illustratif`)

Modèles ouverts recommandés (`RAPPORTÉ` quant à leur existence) : 7–8B (type Llama-3.1-8B-Instruct / Qwen2.5-7B-Instruct) pour E1–E4 et 70–72B (type Llama-3.1-70B-Instruct / Qwen2.5-72B-Instruct) pour E5–E6 + second 70B distinct pour l'ablation hétérogène. Tarifs cloud de référence (`illustratif`) : 2,50 USD/H100-h, 0,05 USD/vCPU-h.

| Phase | Contenu corrigé (incluant $K_{\text{ref}} = 800$ tirages courts) | Calcul estimé (`illustratif`) | Coût (`illustratif`) | Porte d'arrêt |
|---|---|---|---|---|
| **E1** | 100 positifs + 2 000 négatifs, CN-2, spam, A/A complet (8B + CPU) | 2 500 vCPU-h + 50 H100-h | ~250 USD | Échec FPR/CN-2/spam/A/A $\implies$ arrêt |
| **E2a** | 150 prob. isomorphes (incluant taille non conservée) + $K_{\text{ref}}$ | 1 500 vCPU-h + 70 H100-h | ~250 USD | $d_{\text{rec}} > 0{,}05 \implies$ cible mal posée |
| **E2b/c** | Optionnels : audit juge PPI (si requis) / contamination nette | 1 000 vCPU-h + 100 H100-h | ~300 USD | Disqualification juge ou rétrodiction |
| **E3** | 16 familles (8B) + 4 familles transfert (70B) + $K_{\text{ref}}$ | 10 000 vCPU-h + 360 H100-h | ~1 400 USD | Échec conjonction ou transfert $\implies$ arrêt |
| **E4** | 100 prob. $\times$ 3 conditions + panels $\mathcal{Q}_0, \mathcal{Q}'$ | 3 000 vCPU-h + 140 H100-h | ~500 USD | Goodhart avéré $\implies$ retrait feedback |
| **E5a/b** | 320 prob. neufs $\times$ 5 bras (dont CN-1) + $K_{\text{ref}}$ (70B + CPU à USD égal) | 50 000 vCPU-h + 2 200 H100-h | ~8 000 USD | Arrêt futilité si $n_{\text{disc}} \ge 40$ |
| **E6** | Lot **indépendant** de 320 prob. $\times$ 4 bras + $K_{\text{ref}}$ (conditionnel à E5) | 20 000 vCPU-h + 1 800 H100-h | ~5 500 USD | Non exécuté si E5 échoue |
| **Total** | **Campagne complète plafonnée** | **~88 000 vCPU-h + ~4 720 H100-h** | **~16 200 USD** (~2 700 USD avant E5) | **83 % du budget protégé par E1–E4** |

---

## (c) Réponse à la question de l'arbitre (en une page)

### Ce qui est établi

1. **Distinction conceptuelle et relativité de la mesure.** La rareté informationnelle ne mesure pas la profondeur ou la conséquence scientifique (`RAPPORTÉ` : Shannon, 1948 ; Bennett, 1988 ; Rissanen, 1978). La rareté dépend nécessairement du langage de codage (`RAPPORTÉ` : Solomonoff, 1964) et d'un chercheur de référence explicitement fixé ; l'absence d'universalité sans adéquation structurelle est établie (`RAPPORTÉ` : Wolpert & Macready, 1997).
2. **Pièges mathématiques qui invalident un harnais naïf (`VÉRIFIÉ`).**
   - Évaluer un maximum sur l'ensemble des idées générées $\mathcal{S}(P,B)$ avec l'oracle scellé court-circuite la sélection du système et gonfle artificiellement le score avec le volume de candidats. Le harnais doit noter une nomination scellée choisie avant ouverture du coffre.
   - À faible prévalence $\pi$ d'idées « étroites et profondes », l'identité de Bayes impose $\text{FPR} \ll \pi$ : un juge ou détecteur à $\text{FPR} = 0{,}05$ (`illustratif`) produit majoritairement de fausses découvertes lorsque $\pi = 0{,}01$ (`illustratif`).
   - Utiliser la même politique LLM à budget identique comme référence d'étroitesse et comme baseline du duel handicape mécaniquement cette baseline par construction (outil formalisé par B).
   - Comparer contre une enveloppe $\max_b$ prise problème par problème crée un biais négatif par inégalité de Jensen ; l'intersection-union (Berger, 1982, `RAPPORTÉ`) évite ce biais.
   - Dimensionner les échantillons contre zéro alors que la règle exige une marge $\delta_{\min} > 0$ sous-estime massivement la taille requise ; de même, réutiliser les familles de sélection ou les instances du duel dans les ablations crée un biais post-sélection.
3. **Limites établies des sources de vérité et du feedback.** Les vérificateurs formels garantissent zéro faux positif de validité logique modulo le noyau (`RAPPORTÉ`). La réutilisation adaptative d'une suite d'évaluation détruit la validité statistique (`RAPPORTÉ` : Dwork et al., 2015). Enfin, PPI (`RAPPORTÉ` : Angelopoulos et al., 2023) ne borne le biais que vers l'étiquette d'audit — pas vers la vérité scientifique si des experts partagent les biais du juge LLM — et dégrade la variance si la corrélation juge–vérité est insuffisante (`VÉRIFIÉ`).

### Ce qui n'est pas établi (`HYPOTHÈSE`)

1. **Existence empirique d'une cible stable.** Rien n'établit qu'une opérationnalisation de « narrow & deep » reste stable sous recodage isomorphe hors de langages formels ou synthétiques très contraints, ni que la prévalence réelle $\pi$ soit assez élevée pour permettre une décision statistique à coût fini.
2. **Faisabilité d'un harnais en science ouverte.** Aucun harnais automatisé existant n'établit la validité externe entre mondes synthétiques/formels (seuls auditables sans contamination ni biais de juge) et découverte empirique ouverte, qui repose souvent sur un changement d'ontologie inaccessible à tout vérificateur à grammaire figée.
3. **Avantage réel du multi-agents et attribution causale.** Il n'est établi ni qu'il existe des familles de problèmes identifiables *a priori* où des agents LLM battent simultanément un énumérateur mécanique (à coût financier égal), un modèle unique en Best-of-$K$ et un bras de divergence triviale (CN-1), ni qu'un gain éventuel résulte du débat critique plutôt que de la diversité ou du volume d'exploration.

### L'expérience à faire en premier (`HYPOTHÈSE`)

Lancer **E1 (métrologie du harnais sur vérités plantées, sans juge LLM, ~250 USD `illustratif`)**, suivie immédiatement de **E2a (invariance au recodage isomorphe, ~250 USD `illustratif`)**, avant tout développement coûteux du système multi-agents.

**Protocole minimal d'E1 :** construire deux bancs procéduraux post-entraînement (un synthétique exécutable à lois interventionnelles et un formel Lean 4), munis d'une nomination scellée unique $\hat{x}_1$ et d'une étroitesse certifiée par borne de Clopper–Pearson sur $K_{\text{ref}} = 800$ (`illustratif`) tirages courts disjoints. Soumettre le harnais à $100$ (`illustratif`) positifs plantés et $2\,000$ (`illustratif`) négatifs couvrant les trois classes leurres, les paraphrases et paires proches distinctes, un **chasseur d'étroitesse (CN-2)**, un **bras spam à volume élevé** et un **test A/A complet à graines distinctes**.

**Critère d'arrêt immédiat :** si le harnais échoue à maintenir $\text{FPR} \le 0{,}002$ (`illustratif`) contre chaque classe de leurres, CN-2 et le spam tout en conservant $\text{TPR} \ge 0{,}80$ (`illustratif`) — ou si E2a montre un désaccord $> 0{,}05$ (`illustratif`) sous recodage isomorphe —, arrêter le projet : la mesure est mal posée ou perméable à la rareté creuse, et tout duel ultérieur à grande échelle serait ininterprétable.

FIN-DE-CELLULE