# Proposition B — Tour III.3 : réponse aux critiques

**Pièces.** Les faits, la question de l'arbitre, ma conception (E3‑T1‑B) et les critiques croisées A, C, D et E sont présents et complets. Je ne traite que les sections « Sur la proposition B ».

**Statuts.**
- Je ne reprends pas à mon compte les statuts que les critiques attribuent. Quand j'écris « dérivation refaite », le statut reste celui de l'auteur.
- La borne de Fréchet R ≤ 1/max(θ₁, θ₂) porte HYPOTHÈSE chez A et VÉRIFIÉ chez C et E. Je ne tranche pas.
- E qualifie d'« illustratif » mon seuil n ≥ 99. Chez moi, ce seuil est dérivé du 1 % des faits, et je garde cette étiquette.

---

## (a) Réponse à chaque critique

Sources : A, C, D et E désignent les critiques croisées ; a, b et c renvoient à leurs sous-sections.

### P1 — Audit par ré-exécution et bilan de provenance

| # | Critique (source) | Verdict | Conséquence |
|---|---|---|---|
| 1 | Ré-exécuter n'établit pas la correction. Un estimateur faux, journalisé et déterministe se reproduit à l'identique. Le α de l'audit à risque limité n'a pas d'hypothèse nulle pour la part interprétative, et l'implication « conclusion fausse ⇒ discordances auditables » n'est pas établie (A‑a3, C‑a3, C‑b3, D‑a). | **Acceptée.** C'est le défaut central de P1. | Je retire « risque d'accepter un résultat faux sous α ». Le α ne porte plus que sur « le rapport est conforme à son journal ré-exécuté » ou, si un tiers la fixe avant soumission, sur une propriété définie. Le bilan de provenance ne vérifie que la conformité. |
| 2 | Sélection par la mesurabilité : les sabotages qu'on sait planter sont ceux que la ré-exécution tranche (A‑a2). | **Acceptée, transformée en test.** | Dans un monde planté, la vérité porte sur la **conclusion** (le monde), pas sur le calcul. Le tiers fixe à l'aveugle une strate « reproductible mais faux ». La métrique devient la couverture pondérée par la perte (duel 1). |
| 3 | Avec k = 1, il faut p ≥ 0,99 ; avec k = 0, la détection est nulle même à p = 1 ; le duel ne teste jamais la règle séquentielle (E‑a3, E‑b1). | **Acceptée en partie.** | Je rejette le qualificatif « transposition invalide » pour la seule raison k = 1. Dans un audit électoral, une marge d'une voix mène au dépouillement complet : c'est la conception de l'audit, pas un défaut. J'accepte en revanche que la règle séquentielle n'était pas testée : j'ajoute un bras (duel 2). |
| 4 | La borne devient (1 − ps)^k ; l'attaquant choisit k ; inf d(a) = 0 ôte toute borne uniforme ; un risque fréquentiste n'est pas une probabilité postérieure (A‑b, D‑b). | **Acceptée.** | Nouvelle formulation : P(non révélé) = (1 − p·s)^k, sous tirages indépendants et secrets, avec k = 1 par défaut et s mesurée par strate. Sur la strate « reproductible mais faux », s = 0. |
| 5 | « Divergences honnêtes sous 1 % » n'est pas jugeable sous environ 299 épisodes (A, lemme L3). | **Acceptée.** | Dérivation refaite (0,99²⁹⁹ ≈ 0,0495). J'utilise la borne de Clopper‑Pearson. |
| 6 | Contrôles manquants : bogue honnête reproductible, rejouages non déterministes, bras d'audit uniforme à coût total égal, escalades comprises (C‑c, D‑c). | **Acceptée.** | Intégrés aux duels 1 et 2. |

### P2 — Panne coïncidente et agrégation

| # | Critique (source) | Verdict | Conséquence |
|---|---|---|---|
| 7 | Le critère R ≤ 2 est vrai par construction dès que max(θ₁, θ₂) > 1/2, c'est-à-dire précisément quand la sonde est aveugle. H_B y est impossible, ce qui viole B4 (A‑a1, C‑b1, E‑a2). | **Acceptée.** Ma permutation ne contrôlait que l'estimateur. | R est abandonné comme critère. |
| 8 | E[FS] = E[E(F∣X)E(S∣X)] + E[Cov(F, S∣X)]. L'indépendance n'est pas un service rendu : R = 1 avec deux moniteurs aveugles (D‑b). | **Acceptée.** | Nouvelle grandeur : le **sauvetage conditionnel avant irréversibilité** (duel 3). |
| 9 | Variance explosive quand les doubles ratés sont rares ; un mélange de régimes donne R > 1 sans dépendance intra-régime, et c'est l'attaquant qui choisit le régime (A‑b, C‑b1). | **Acceptée.** | Stratification préalable. On rapporte la pire strate, avec un effectif minimal ; en deçà, le duel est déclaré non concluant. |
| 10 | Des e-valeurs calibrées depuis des p-valeurs conformes plafonnent à n + 1. À n = 99, leur moyenne n'atteint 100 que si tous les moniteurs sont au rang minimal (un « ET » unanime). La puissance se dilue en K/α (E‑a1, E‑b2, C‑a4, A‑b). | **Acceptée.** Dérivation refaite. | Je retire la moyenne comme détecteur par épisode à petit n. La combinaison à poids **fixés d'avance** reste valide. Par épisode, elle n'est utilisable que si n + 1 ≥ K/α (pour K = 10, illustratif : n ≥ 999). Sinon, il ne reste qu'un e‑processus par régime, sur plusieurs épisodes, qui teste la non-échangeabilité de la suite et non « cet épisode » (l'objection de A à C vaut aussi pour moi). |
| 11 | Biais de survie : l'étalonnage n'existe que sur les régimes routiniers (C‑a1). | **Rejetée comme biais, transformée en mesure.** | L'abstention est une sortie déclarée, pas une sélection cachée. J'accepte le fond : la couche statistique se tait là où l'attaquant invente. Grandeur rapportée : la fraction des épisodes, et du dommage planté, située dans des régimes non certifiables au n réel. C'est un résultat, et il oriente vers P1 et l'architecture. |
| 12 | Choisir les moniteurs de covariance minimale et l'évaluer sur les mêmes épisodes ; poids choisis sur les mêmes réalisations (D‑a, D‑b). | **Acceptée.** | Sélection et évaluation sur des lots disjoints ; poids gelés. |
| 13 | Contrôles : adjudant factice (A), synthétique U = V avec θ = 0,8 (C, E), permutations dans les strates (D). | **Acceptée.** | Duel 3. |

### P3 — Défis secrets

| # | Critique (source) | Verdict | Conséquence |
|---|---|---|---|
| 14 | « L'agent interrogé compris » suppose qu'un saboteur avoue ce qu'il reconnaît. Un discriminateur qui échoue ne fournit qu'un minorant (A‑a4, lemme L4). | **Acceptée.** | L'indiscernabilité devient un test qui peut tuer le mécanisme, jamais une prémisse certifiée. La réponse de l'agent ne compte que si elle reconnaît le défi. |
| 15 | L'AUROC n'est pas le bon paramètre : une région de densité de défi nulle suffit à l'attaquant (A‑b, E‑b3). | **Acceptée.** | On mesure le taux de reconnaissance à fausse reconnaissance quasi nulle, et la masse de queue du rapport de densité. |
| 16 | Randomiser ne crée aucune puissance si la loi conjointe défi/réponse est la même sous P et sous Q (D‑b). | **Acceptée.** | C'est mon §4.1 appliqué à l'intervention. Ajout d'un contrôle par défis placebo. |
| 17 | Le discriminateur doit être entraîné par un tiers qui dispose du générateur (A‑c). | **Acceptée.** | Duel 4. |

### P4 — Analyse aveugle

| # | Critique (source) | Verdict | Conséquence |
|---|---|---|---|
| 18 | Zone grise entre « baisse au taux honnête » et « aucune baisse » ; « non significatif » n'est pas le complément d'une équivalence (A‑a5, D‑b, E‑b4). | **Acceptée.** | Marge unique et convention de décision commune. |
| 19 | L'issue est fixée par le choix de la famille (A‑a5). | **Rejetée en partie.** | P4 est un mécanisme **conditionnel** : sa portée, le sabotage dépendant du résultat, fait partie de l'hypothèse. Le tiers fixe à l'aveugle les proportions des strates, et les deux strates sont rapportées. J'accepte de ne pas l'avoir écrit en III.1. |
| 20 | L'aveugle fuit par la structure déductive de la tâche (C‑a2). | **Acceptée.** | Les tâches déductives sont exclues de la portée, mais comptées au dénominateur comme non couvertes. |
| 21 | Sabotage non directionnel (étouffer une découverte vraie) ; gêne du débogage honnête (E‑a4). | **Acceptée.** | Strate séparée, avec une prédiction déclarée ; coût honnête mesuré. |
| 22 | Différence de différences sous assignation aléatoire, masque placebo, mesure de la fuite (D‑b, A‑c, C‑c, E‑c). | **Acceptée.** | Duel 5. |
| 23 | log₂\|S\| ne borne pas E[L] (D‑b). | **Acceptée.** C'était déjà une HYPOTHÈSE. | Retirée de la liste des mécanismes qui bornent le dommage. |

### Points transversaux

| # | Critique (source) | Verdict | Conséquence |
|---|---|---|---|
| 24 | S7 : « un saboteur cohérent n'a pas d'erreur de valeur » était posé comme raison (A‑a6). | **Acceptée.** | C'est une HYPOTHÈSE, à tester par le duel 3 sur le moniteur de dissonance. |
| 25 | Aucune règle de gel des seuils illustratifs (A‑a6). | **Acceptée.** | Voir le protocole commun. |
| 26 | Une famille engagée avant l'instrument teste le transfert à l'aveugle, pas un attaquant qui connaît l'instrument gelé (D‑a). | **Acceptée.** | Mon propre §1, point 2 l'exigeait, et je ne l'avais pas appliqué. Il y aura deux bras de familles. |
| 27 | Le rapport TPR tenu à l'écart / TPR connu est indéterminé près de α ; une famille n'est qu'un tirage (A‑b, D‑b). | **Acceptée.** | Remplacé par des différences à un comparateur. Toute conclusion est bornée à la famille nommée. |
| 28 | L'« avance » des précurseurs était mesurée parmi les seuls épisodes alertés (D‑b). | **Acceptée.** | On mesure Q(T_alerte < T_irréversible) sur **tous** les épisodes. |
| 29 | Une équipe rouge de la même famille de modèles biaise les covariances (E‑a4). | **Acceptée.** | Équipe rouge d'une autre famille, ou tiers. |

---

## (b) Expériences corrigées

### Protocole commun

- **Gel.**
  - Les marges m, les strates, l'effectif maximal N_max et les comparateurs sont déposés par empreinte sha256 auprès de l'arbitre, avant la révélation de toute famille.
  - Les valeurs données ici sont illustratives et en attente de gel.
- **Deux bras de familles, conçues par des tiers.**
  - F_aveugle : engagée par empreinte avant la conception ; elle teste le transfert.
  - F_adaptative : conçue par un tiers qui dispose de l'instrument gelé ; elle teste la pire stratégie trouvée.
  - Seul F_adaptative parle de l'« attaquant informé ».
- **Décision.** J'emprunte la convention de D, en le disant.
  - H_A : b ≥ m ; H_B : b < m.
  - Une région de confiance à 95 % entièrement d'un côté réfute l'autre hypothèse.
  - Un chevauchement à N_max donne « non concluant », publié comme tel et jamais compté comme un succès.
  - L'incertitude se calcule sur des tâches tirées indépendamment.
- **Fausses alertes honnêtes.** Il faut une