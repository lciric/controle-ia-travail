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
- **Modèles** : des poids ouverts de trois familles distinctes, par exemple Llama, Qwen et Mistral. Les versions sont à figer par empreinte au préenregistrement. Elles sont servies localement, avec graines et températures journalisées. Trois familles permettent l'hétérogénéité de E5 et un juge d'une autre famille que le générateur.
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