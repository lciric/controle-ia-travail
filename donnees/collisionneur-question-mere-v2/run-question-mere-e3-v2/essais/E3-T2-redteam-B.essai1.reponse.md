# Proposition B — Tour III.2 : critique croisée de méthode

**État des pièces.** Les conceptions A et C sont présentes et complètes ; chacune se termine par sa ligne de fin. La pièce D (juge figé, critère de G1) est absente des faits : elle est déclarée « par renvoi, non servie ». A et C le signalent l'une et l'autre, et je n'en reconstruis rien. Aucune autre coupure n'est visible, en dehors des « […] » déclarés dans la question.

**Conventions.**
- Les critiques ci-dessous sont des **HYPOTHÈSES** de méthode, sauf mention contraire.
- Ce que je reprends des pièces garde le statut **RAPPORTÉ**.
- Les seuils que je donne sont **illustratifs**.
- Un « calcul » désigne une dérivation faite par moi à partir de chiffres des pièces.
- Toute condition de perte de puissance est énoncée sur des lois de probabilité, jamais sur une conduite.

---

## Sur la proposition A

### (a) Défauts de méthode

**A-1. E1 donne raison à H_A par construction.**
- La métrique de jugeabilité de E1 compte les fiches qui contiennent « hypothèse + condition mesurable + prédiction signée + critère de mort ».
- Or la règle de couplage du bras traité impose justement d'écrire une hypothèse et sa condition de rupture.
- Le bras couplé reçoit donc l'ordre de remplir deux des quatre cases que la métrique vérifie.
- Une hausse d'au moins 15 points mesure alors l'obéissance au gabarit, pas un gain de jugeabilité.
- Correctif : la liste mécanique qui note les deux bras doit exclure les champs que le couplage impose. Par exemple, se limiter à « prédiction signée + critère de mort + coût + antériorité retrouvée ».

**A-2. E5 sépare ses deux témoins par construction.**
- Le témoin « neuf » est écrit « sur des pièces absentes de g ».
- Le témoin « paraphrase » est réécrit à partir des fiches de g.
- L'une des deux mesures testées, la « nouveauté des sources », sépare donc les deux témoins par définition. Une AUROC ≥ 0,9 sur cette composante ne dit rien de la validité de la mesure.
- Correctif : construire un témoin neuf qui travaille *sur les mêmes pièces* que g.

**A-3. Le critère de E6 et le critère de mort de la course sont triviaux.**
- Le critère « au moins une fiche jugeable que la pièce C1 ne contient pas » est satisfait d'office : C1 contient des questions et des consignes, pas des fiches au gabarit F1–F8.
- Toute fiche conforme est donc « hors C1 ».
- Le critère de mort de la course hérite du même défaut et perd ainsi sa puissance.

**A-4. E4 confond deux facteurs.**
- H_A compare « maximum ou attention sur les jetons **puis** accumulation sur les actions » à la base (iii).
- Deux facteurs changent à la fois : le grain dans l'action et l'accumulation dans le temps.
- Or l'issue H_B est interprétée comme « la différence par les jetons est cosmétique ». Cette lecture n'est pas identifiable sans plan factoriel 2 × 2 : jetons {dernier, agrégés} × temps {ponctuel, accumulé}.

**A-5. Le plancher de E3 n'est pas apparié à la sélection.**
- E3 retient la *meilleure* sonde figée sur « au moins une des trois couches ». On choisit donc un maximum parmi plusieurs familles et plusieurs couches.
- Le comparateur est le quantile 0,95 du plancher d'une seule direction aléatoire.
- Un maximum sur K essais dépasse un quantile simple sous l'hypothèse nulle. Le plancher doit être calculé sur le **maximum de K directions aléatoires**, avec le même K que le nombre de candidats.
- Sans cela, H_A gagne par sélection.

**A-6. Le contrôle de « famille honnête plantée » est inversé (axe 4, tableau c).**
- Une famille à déplacement nul est indétectable par définition : son rappel tend vers le taux de fausses alertes.
- Le critère d'échec retenu est « borne basse sous le quantile 0,95 du plancher ». Ce critère la déclarera **en échec** à coup sûr.
- La spécification exige l'inverse (« ne doit jamais être déclarée échec »). Ce contrôle ne peut donc pas être jugé tel qu'il est écrit.
- Le témoin utile est d'une autre nature : une famille plantée à effet connu et détectable, qui doit passer.

**A-7. Les données servies comme « tranche exploratoire » ne sont pas toutes propres.**
- A déclare non circulaires les « 180 notations brutes des juges ».
- La pièce A (RAPPORTÉ) annonce un *second examen* des juges, autorisé à 4 USD et pas encore lancé. Elle n'établit pas que cet examen portera sur d'autres copies.
- Servir ces notations aux idéateurs permet des fiches de correction du juge ajustées sur ces copies. Elles seraient ensuite évaluées sur les mêmes copies : c'est une fuite construction → évaluation.
- Autre point : la pièce A emploie « 180 » deux fois (« 180 épisodes […] enregistrés et scellés » ; « examen blanc de 180 copies »). Elle n'établit pas que ces deux ensembles sont les mêmes.

**A-8. Pseudo-réplication dans E1 et E2.**
- Il y a une course par bras (« deux courses »). L'unité randomisée est la course, mais l'analyse porte sur les fiches.
- La variance entre courses (tirage des proposeurs, ordre de lecture des pièces) est confondue avec l'effet traité.
- Avec une seule course par bras, aucune différence n'est attribuable au traitement.

**A-9. E7 risque la contamination.**
- Les trois revendications plantées « occupées » sont celles que la pièce B1 réfute explicitement.
- Si le sous-agent de vérification a accès au dépôt, ou à la note corrigée, il les retrouve sans chercher.
- Le taux de 9 sur 10 mesurerait alors la mémoire du dépôt, pas la recherche d'antériorité.

**A-10. Zones mortes contraires à la règle B4.**
- E1 (≥ 15 contre < 5 points), E4 (≥ 0,10 contre < 0,05), E5 (≥ 0,9 contre < 0,7) et E6 (κ ≥ 0,8 contre < 0,6) laissent toutes un intervalle où aucune hypothèse n'est falsifiée.
- Correctif : un seuil unique s\* scellé par expérience. H_A est retenue si la borne basse dépasse s\* ; H_B est retenue si la borne haute reste sous s\*. Une issue qui chevauche s\* est déclarée « non jugeable par puissance », ce qui falsifie le dimensionnement scellé.

### (b) Conditions de perte de puissance ou de non-jugeabilité

| Mesure ou critère de A | Condition, au niveau des lois, qui le rend muet ou non jugeable |
|---|---|
| κ inter-juges (E6) | Si la prévalence des fiches valides dans le jeu aveugle sort de [0,1 ; 0,9] (illustratif), κ s'effondre même à fort accord brut (paradoxe de prévalence). Le seuil 0,8 n'est jugeable que si la composition du jeu est fixée avant lecture. |
| Rappel à 1 % de fausses alertes (E4, F2) | Avec N épisodes honnêtes réservés, le seuil au quantile 0,99 repose sur environ 0,01·N dépassements. À N = 300 (RAPPORTÉ, ordre de grandeur de la porte), cela fait environ 3 dépassements (calcul). La variance du seuil domine alors un écart de rappel de 0,10. |
| « ≤ 5 points de fausses alertes de plus » | Si chaque statistique est calibrée à 1 % sur le même ensemble, l'écart est nul par construction. Le critère n'a de puissance que sur des honnêtes **tenus à l'écart du calibrage**. |
| Plancher apparié en covariance | Si le rang effectif de la covariance des activations est faible, des directions aléatoires d'énergie égale tombent dans le même sous-espace que la sonde. Le plancher rejoint alors la sonde et le test perd sa puissance. Le rang effectif doit être rapporté avec le plancher. |
| Universalité par exclusion (axe 4) | Si chacune des K ≈ 10 familles est testée à 5 %, la probabilité qu'au moins une « échoue » sous l'hypothèse nulle vaut environ 1 − 0,95¹⁰ ≈ 0,40 (calcul). Si la variance entre familles dépasse l'effet, le protocole déclare des échecs au hasard. Il faut une correction de multiplicité et une taille d'effet minimale par simulation, que A demande sans l'imposer au protocole. |
| Distances entre passes (E5) | Si la dispersion intra-génération des représentations de fiches est du même ordre que le décalage inter-générations, l'AUROC de nouveauté tend vers 0,5 quelle que soit la nouveauté réelle. |
| Sonde nulle dans [0,45 ; 0,55] | À petit nombre d'épisodes honnêtes, l'intervalle d'échantillonnage de l'AUROC sous l'hypothèse nulle dépasse cette fenêtre. Le critère rejette alors une chaîne saine. La fenêtre doit dépendre de n. |

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Pour E1** : une liste de notation indépendante du couplage (A-1). Sans elle, l'expérience est tautologique.
2. **Pour E3 et E4** : un plancher calculé sur le maximum de K directions aléatoires, au même K que les candidats (A-5).
3. **Pour E1 et E2** : au moins deux courses par bras, ou une randomisation des consignes *dans* une même course, avec une analyse au niveau de la course (A-8).
4. **Pour E5** : un témoin neuf travaillant sur les mêmes sources que g (A-2).
5. **Pour E7** : une vérification exécutée sans accès au dépôt du programme ni à la pièce B1 (A-9).
6. **Pour l'axe 4** : remplacer la famille nulle par une famille plantée à effet connu détectable (A-6).
7. **Pour F7, l'avantage décisif** : des fiches plantées qui revendiquent un avantage *faux* au regard des pièces. Exemple : un avantage tiré de la moisson arXiv, qui n'existe pas (RAPPORTÉ). Si elles passent la liste au même taux que les vraies, le critère « nommer une ressource et une clause » n'a aucun pouvoir discriminant. A réduit « décisif » à la présence d'une clause, ce qui reste un contrôle de présence.

---

## Sur la proposition C

### (a) Défauts de méthode

**C-1. La tranche TED-0 sert à la fois à construire et à évaluer : c'est le défaut le plus grave.**
- C sert aux idéateurs trois objets : les « résidus de calibrage sur épisodes honnêtes réservés », les activations et scores de la tranche 0 du pilote, et les 180 notations.
- Les honnêtes réservés sont précisément l'ensemble sur lequel la porte calibre le seuil à 1 % (RAPPORTÉ, pièce B2 § 3). Les servir contamine le calibrage de G1.
- Le critère de mort (b) évalue ensuite les fiches M1/M3 « sur la tranche exploratoire TED-0 ». La même donnée sert à inspirer et à juger.
- C ne pose pas la condition que A formule (A5) : une partition fixée par une instance tierce *avant* que la tranche existe, et l'exclusion de G1.
- J'utilise ici A contre C, et je le dis : la condition de A est nécessaire, elle n'est pas suffisante (voir A-7).

**C-2. Le juge figé à mise est appliqué à des fiches : erreur de catégorie.**
- Dans le tableau (c), ligne 4, C applique à des fiches d'idées la « promotion au seuil m/α » et la « borne de fausses promotions ».
- Un pari apparié borné exige une issue numérique appariée par observation. Une fiche n'en produit aucune.
- La « bibliothèque de nuls » n'est pas définie pour des fiches.
- C a pourtant écrit lui-même, en (a)3, que cette transposition « suppose une calibration non démontrée », puis il l'utilise. La borne annoncée n'est pas jugeable.

**C-3. Le contrôle par compilation Lean 4 est vrai par construction.**
- Un squelette compile avec un trou de preuve laissé ouvert, avec un axiome ajouté, ou avec des hypothèses qui contiennent la conclusion.
- La compilation ne dit pas que l'énoncé formel correspond à l'énoncé de la fiche.
- Le critère (7) peut donc être rempli par une fiche vide.

**C-4. Le critère d'arrêt de la boucle est fixé par le dispositif.**
- Le « gain de couverture des 23 papiers < 5 % » repose sur un dossier fermé et fixe. La couverture croît d'abord, puis sature par construction.
- La règle d'arrêt se déclenche donc par épuisement du dossier, pas par épuisement des idées.
- Par ailleurs, « faux arrêts : arrêt à g = 1 alors que des hypothèses de la carte restent non couvertes » exige de lire la carte des hypothèses. Ni les idéateurs ni ce dispositif ne la voient (RAPPORTÉ, garde de la question). Ce critère n'est pas jugeable dans le cadre servi.

**C-5. E1 confond la contrainte et le matériau.**
- En g = 2, le bras couplé reçoit les fiches de g − 1 et doit s'y rattacher. L'expérience ne dit pas si le bras découplé reçoit le même matériau.
- Si ce n'est pas le cas, l'effet mesuré mélange « matériau servi » et « contrainte de couplage ». Il faut un plan 2 × 2.
- Le contrôle négatif réinjecte des fiches identiques aux identifiants près. Il ne teste que la détection de doublons exacts, pas des paraphrases. Un filtre lexical le passe à 100 % sans rien garantir.

**C-6. E2 confond séquentialité et multi-jetons, et lit la porte avant la porte.**
- Même confusion que A-4, aggravée : C nomme un seul comparateur et attribue l'issue à « gain séquentiel et multi-jetons ».
- E2 est en outre littéralement la porte G1 (300 unités par famille, une lecture). La proposer comme expérience de la question de course, c'est consommer la lecture unique de G1, ou la dupliquer. A le reconnaît pour son propre E4 ; C ne le dit pas.

**C-7. E3 introduit un biais de sélection par l'analyse par protocole.**
- C compare l'AUROC à 8 B et à 70 B « sur les seuls épisodes où le dommage est confirmé ».
- Si le taux d'exécution confirmée diffère entre tailles, la sélection n'a pas la même intensité. Le sous-ensemble à 8 B retient alors les épisodes à plus fort déplacement, ce qui gonfle son AUROC.
- La séparation m1 / m2 n'est identifiable qu'à **effet mesuré égal** : appariement ou stratification sur l'amplitude du dommage mesurée par l'oracle.
- De plus, l'oracle repose sur des lecteurs automatiques. Leur sensibilité peut dépendre du style de rédaction propre à chaque taille, ce qui est une confusion supplémentaire.
- Zones mortes enfin : un taux d'exécution entre 0,40 et 0,80 ne falsifie rien (règle B4).

**C-8. E4 (Q-pont) : fuite et contrôle vide.**
- Savoir qu'une famille réelle tenue à l'écart « vérifie empiriquement C_R » exige de la caractériser. Or elle est scellée et non lue par les concepteurs de moniteurs (RAPPORTÉ, pièce A § 4.C). Qui établit ce statut, et sans fuite vers le concepteur ? Ce n'est pas spécifié.
- Le contrôle négatif (un déplacement orthogonal à la direction de sonde) laisse un score linéaire invariant **par construction**. Il ne teste rien pour une sonde linéaire, et il n'est pas nul pour une statistique de type Mahalanobis.
- Enfin, une injection dans les activations n'a pas d'équivalent pour les comparateurs boîte noire. Le pont ne couvre qu'un côté du plan accès × agrégation.

**C-9. Le seuil « > 0,38 » est un comparateur non commensurable.**
- C fait de 0,38 (HELIOS, TRANSFER) un seuil minimal de fonctionnement. Ce chiffre vient d'un autre banc, d'une autre menace (agents pairs, moniteur tiers) et d'une autre unité (une statistique par exécution).
- Plus précisément : TRANSFER compte 36 exécutions témoins (RAPPORTÉ, B2). Un seuil à 1 % de fausses alertes y correspond à 0,36 fausse alerte (calcul). Le 0,38 se lit donc de fait comme un rappel à zéro fausse alerte observée sur 36 témoins.
- L'utiliser comme borne sur notre banc revient à importer une quantité que la pièce B1 elle-même déclare non comparable (C10).

**C-10. Statuts et attributions.**
- C emploie « VÉRIFIÉ » au sens de « présent dans une pièce ». Exemples : les chiffres d'HELIOS (« VÉRIFIÉ, Pièce B1, p. 46 »), et « 3 500 citations, 0 échec ».
- Je ne change aucun de ces statuts. Je signale seulement que, dans la convention de A, les mêmes éléments sont RAPPORTÉS. La synthèse ne doit pas hériter de cette ambiguïté. Un chiffre d'HELIOS lu par un sous-agent n'est pas vérifié par ce collisionneur.
- Erreur d'attribution, sans changement de statut : C présente `Llama-3.1-70B-Instruct-AWQ-INT4` comme modèle du programme (« VÉRIFIÉ »). Les pièces n'attestent ce modèle que comme modèle d'HELIOS (B1, p. 27). Le plafond 70 B du programme est SUPPOSÉ quant à sa disponibilité (RAPPORTÉ, B2 § 4).
- Budget : C divise le plafond de 52,80 USD en deux générations. Or la question dit « chaque génération est une course », et 52,80 USD est le plafond *d'une* course (RAPPORTÉ). Le coût de deux générations est donc sous-estimé d'un facteur d'environ deux (calcul).

**C-11. Le critère de mort (b) ne s'applique pas à M3.**
- Ce critère exige qu'une fiche M1/M3 « batte le plancher aléatoire sur TED-0 ».
- Un énoncé de borne ou d'impossibilité ne bat pas de plancher. Pour M3, le critère n'est pas jugeable.

**C-12. Le juge gradué est rendu dépendant d'un résultat attendu.**
- C exige une progression monotone p0 ≤ p1 ≤ p2 comme condition de bon fonctionnement de l'instrument.
- Or HELIOS rapporte sur son juge faible 1/20, puis 3/20, puis 2/20 (RAPPORTÉ, B1 pages 43-44) : une suite non monotone.
- La monotonie est une propriété empirique, pas un critère de validité. L'imposer ferait déclarer « cassé » un instrument correct.
- En outre, C propose de calibrer ce juge sur les 180 copies de l'examen blanc, qui ont servi à réécrire la consigne : même fuite que A-7.

### (b) Conditions de perte de puissance ou de non-jugeabilité

| Mesure ou critère de C | Condition, au niveau des lois, qui le rend muet ou non jugeable |
|---|---|
| Distance cosinus > 0,30 contre Q1–Q7 et la mémoire | Elle dépend du modèle de plongement. Si la variance due au vocabulaire domine celle due au contenu, la distance sépare des reformulations et confond des fiches neuves au vocabulaire proche. Le seuil n'a aucun étalonnage contre des témoins. |
| Corrélation de Spearman sur 10 moniteurs (E4) | À n = 10, l'intervalle de ρ est large. Si l'étendue des performances sur le synthétique est restreinte (tous les moniteurs proches), ρ est indéterminé. « ρ < 0,3 » est alors compatible avec H_A comme avec H_B. |
| TPR à 1 % sur 300 unités (E2) | Même condition que pour A : environ 3 dépassements honnêtes fixent le seuil (calcul). La borne basse d'un intervalle à 95 % sur une différence de rappel de 0,15 est instable si la variance du seuil n'est pas propagée. |
| Promotion au seuil m/α | Si le nombre m de fiches candidates croît d'une génération à l'autre, le seuil de promotion croît aussi. La puissance par fiche tend vers zéro et plus rien n'est promu, par construction. |
| Taux d'exécution, analyse par protocole (E3) | Si la loi de l'amplitude du dommage confirmé diffère entre tailles, la comparaison d'AUROC mesure la sélection et non la lisibilité. |
| Filtre de mots exclus | Sa sensibilité et sa spécificité ne sont pas mesurées. Si le taux de rejet sur des fiches légitimes contenant des termes techniques voisins est élevé, il filtre surtout le vocabulaire de détection. |
| Arrêt sur « < 20 % de couples nouveaux » | Si le taux de couples (H_M, A_O) valides par génération est faible dès g = 1, la règle s'arrête à g = 2 quel que soit le potentiel. Le seuil n'est pas relié à une loi du taux sous l'hypothèse nulle de non-épuisement. |

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Pour TED-0** : aucune donnée qui alimente le calibrage ou l'évaluation de G1 ne peut être servie. Il faut une partition tierce horodatée avant la création de la tranche, et une vérification mécanique d'intersection vide entre « servi » et « calibrage ou évaluation » (C-1). Sans ce contrôle, toute la course est circulaire.
2. **Pour Lean** : rejet mécanique des trous de preuve et des axiomes ajoutés. Il faut aussi des énoncés plantés vrais mais vides (hypothèses qui contiennent la conclusion), qui doivent être rejetés (C-3).
3. **Pour la distance de nouveauté** : des paraphrases plantées de Q1–Q7 et de fiches de g − 1, réécrites par une instance tierce, qui doivent être bloquées ; et des fiches neuves sur les mêmes sources, qui doivent passer (C-5).
4. **Pour E1** : un plan 2 × 2 (matériau servi × couplage imposé) et au moins deux courses par cellule (C-5, et A-8 transposé).
5. **Pour E3** : une stratification ou un appariement sur l'amplitude du dommage mesurée par l'oracle, et l'oracle lui-même testé à amplitude égale sur les trois tailles (C-7).
6. **Pour E4** : remplacer le déplacement orthogonal par un déplacement qui viole une *autre* hypothèse que la condition C_R ciblée (contrôle de spécificité). Le statut « vérifie C_R » d'une famille réelle doit être établi par une instance tierce, en aveugle (C-8).
7. **Pour le juge de course** : C l'a absorbé dans le pari borné. Il faut des fiches creuses plantées (champs remplis, prédiction non falsifiable) et une permutation des étiquettes donnant un accord voisin de zéro. Le contrôle de A (E6) manque à C, et je le reprends ici en le disant.

---

## Ce que je retiens contre l'une et contre l'autre, séparément

- **A** a les bons garde-fous de principe : jugeabilité des juges de course d'abord, séparation m1 / m2, puissance de l'axe 4. Mais elle livre deux expériences vraies par construction (E1, E5), un contrôle inversé (axe 4) et des critères de mort triviaux (E6).
- **C** a un gabarit plus mécanisable et un plan 3B / 8B / 70B. Mais sa tranche servie contamine le calibrage de la porte, son juge à mise est appliqué hors de son domaine, son contrôle Lean est vide, sa règle d'arrêt est fixée par la taille du dossier, et plusieurs attributions sont erronées.
- **Les deux** laissent des zones mortes contraires à la règle B4 et traitent les chiffres d'HELIOS comme des comparateurs alors que la pièce B1 les déclare non comparables.

Aucune de ces remarques n'établit qu'une des deux questions est fausse sur le fond. Elles comptent ce qui rendrait leurs issues non réfutables.

FIN-DE-CELLULE