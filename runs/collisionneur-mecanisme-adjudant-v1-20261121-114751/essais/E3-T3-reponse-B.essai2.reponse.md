# Proposition B, tour III.3 : réponse aux critiques

*Pièces : les faits, la question de l'arbitre, ma conception III.1 et les critiques croisées A, C, D et E sont présents et paraissent complets. Je ne réponds qu'aux sections « Sur la proposition B ».*

*Statuts : je reprends chaque énoncé d'un critique avec l'étiquette que lui donne son auteur, et je n'en change aucune. Quand deux auteurs étiquettent différemment le même énoncé, je donne les deux étiquettes.*

---

## 0. Ce que les critiques changent à ma thèse

Ma thèse disait : faute de pouvoir lire la différence entre honnête et saboté, il faut soit la **créer**, soit **s'en passer**. Les critiques laissent cette alternative debout mais retirent trois appuis.

1. **Créer de la différence est nécessaire, pas suffisant (D).**
   - La borne de variation totale (§4.1 de ma conception) s'applique aussi à la loi conjointe défi-réponse. Si l'attaquant peut reproduire cette loi, randomiser le défi ne crée aucune puissance.
   - « Créer la différence » devient donc : créer une différence **que l'attaquant ne peut pas reproduire sans coût**. C'est une HYPOTHÈSE propre à chaque mécanisme, pas une conséquence du §4.1.

2. **Se passer de la différence par l'aléa du défenseur ne garantit rien là où aucune discordance n'est auditable (D, C, A).**
   - Notons d(a) la probabilité qu'un tirage d'audit révèle une discordance sur le produit a.
   - Si l'attaquant choisit la strate, la garantie vaut le minimum des d(a) sur les strates. Pour un choix scientifiquement faux mais fidèlement ré-exécuté, ce minimum est 0.
   - Ma conception nommait cet angle mort (« aveugle à un détournement entièrement journalisé »), mais aucun duel ne le mesurait.

3. **P2 perd son rôle d'alarme certifiée (E, C, A).**
   - Une e-valeur obtenue en calibrant une p-valeur conforme sur n épisodes vaut au plus n + 1.
   - À n = 99 et pour un seuil 1/α = 100, la moyenne de K e-valeurs n'atteint le seuil que si toutes les e-valeurs sont maximales. L'agrégation fonctionne alors comme un « ET » unanime, l'inverse de la redondance cherchée.
   - Les moniteurs deviennent donc un **triage** au-dessus d'un plancher d'audit uniforme, rôle qui n'exige aucune certification.

---

## 1. Verdicts (livrable a)

| # | Critique (auteur, section) | Verdict | Ce que je change |
|---|---|---|---|
| 1 | R ≤ 2 est vrai par construction dès que max(p₁, p₂) ≥ 1/2, car R ≤ 1/max(p₁, p₂) (A-a1 et A-b ; C-b1 ; E-a2 et E-b2) | Acceptée | Une issue du duel était impossible : il violait B4. R est abandonné comme critère (voir X3). |
| 2 | R vaut 1 sous indépendance même quand les deux moniteurs sont aveugles : il mesure une dépendance, pas un service (D-b) | Acceptée | La grandeur de décision devient la perte sauvée avant l'instant d'irréversibilité, comparée à l'audit uniforme de même coût. |
| 3 | Remplacer R par φ ou par la corrélation tétrachorique (C-c2) | Rejetée comme critère, gardée comme diagnostic | φ mesure encore une dépendance et non un service (ligne 2). |
| 4 | La variance de R̂ explose quand θ₁₂ est petit ; un mélange de régimes donne R > 1 même avec indépendance dans chaque régime ; l'attaquant choisit le régime (C-b1, A-b) | Acceptée | Rapport par régime et pour le pire régime. L'issue « non jugeable » est déclarée d'avance si les ratés de la sonde sont trop rares. |
| 5 | E[FS] contient le terme E[Cov(F, S ∣ X)] : la difficulté par tâche n'explique pas toute la coïncidence (D-b) | Transformée en test | Plusieurs graines par tâche, pour estimer θᵢ(x) et séparer les deux termes (X3). |
| 6 | E-valeurs calibrées plafonnées à n + 1, d'où une règle unanime ; dilution linéaire en K (E-a1 et E-b2 ; C-a4 ; A-b) | Acceptée. C'est le défaut le plus grave de P2. | Plus d'alarme certifiée à petit n. Les moniteurs servent au triage au-dessus du plancher d'audit. |
| 7 | Poids des e-valeurs choisis sur les mêmes réalisations (D-b) | Acceptée | Poids engagés avant les données. Sans objet après la ligne 6. |
| 8 | Biais de survie : n'étalonner que là où n ≥ 99 abandonne les régimes rares, où l'attaquant opère (C-a1) | Acceptée, transformée | Un régime non certifié reçoit un taux d'audit uniforme majoré et reste au dénominateur. Premier pas : compter ces épisodes. |
| 9 | La garantie conforme est marginale, pas conditionnelle. Certifier ≤ 1 % à 95 % avec zéro alerte exige n ≥ 299 (A, lemme L3) | Acceptée | Mon n ≥ 99 reste un plancher marginal, statut inchangé (VÉRIFIÉ). L3 garde son statut selon A (HYPOTHÈSE) ; mon recalcul, 0,99²⁹⁹ ≈ 0,0495, concorde. Les taux sont jugés par intervalle de Clopper-Pearson. |
| 10 | Choisir les moniteurs de covariance minimale puis estimer leur complémentarité sur les mêmes épisodes (D-a3) | Acceptée | Plis séparés pour la sélection et pour l'estimation. |
| 11 | Sélection par mesurabilité : on plante surtout ce qu'une ré-exécution tranche (A-a2) | Acceptée, transformée | Le tiers déclare les strates avant l'évaluation : trace dans le calcul, ou trace dans un choix. La vérité d'un choix vient de la construction du monde, pas de la ré-exécution. Résultats par strate, jamais agrégés, car les poids du mélange seraient les miens. |
| 12 | L'audit à risque limité perd sa prémisse : pas de fonction de dépouillement, artefacts produits par l'agent (A-a3). Il manque l'implication « conclusion fausse ⇒ discordances auditables » (D-a1). Si γ < 1, le risque réel vaut 1 quand le risque affiché est α (C-b3). | Acceptée | Je retire la prétention à un risque α sur le résultat scientifique. Il reste deux garanties : « journal ré-exécuté = journal déclaré », et les affirmations calculatoires dont un tiers fixe la référence. |
| 13 | Reproductibilité n'est pas exactitude ; une provenance complète peut retracer un choix faux (C-a3, D-a2) | Acceptée | Contrôle « bug honnête reproductible » ajouté (X2). |
| 14 | Le duel à p = 1 ne teste pas la règle séquentielle ; une seule étape (k = 1) renverse la conclusion (E-a3, E-b1) | Acceptée | Ajout d'un bras d'audit uniforme de même coût total, escalades comprises (D-c le demande aussi). |
| 15 | « L'arrêt séquentiel exige de ré-exécuter la quasi-totalité de la trace » (E-a3) | Rejetée en partie | Le bilan de provenance restreint le tirage à la généalogie de l'affirmation décisive, pas à la trace entière. La taille de cette généalogie est inconnue ; elle devient une mesure de X2. |
| 16 | La borne devient (1 − ps)^k ; l'attaquant choisit k ; le calendrier d'audit peut fuir ; si inf d(a) = 0, aucune borne uniforme (A-b, D-b) | Acceptée, transformée | Sensibilité s mesurée par strate ; test de fuite du calendrier (X2). Formulation corrigée : un risque fréquentiste de certification n'est pas la probabilité que le résultat soit faux (D). |
| 17 | AUROC ≤ 0,6 est le mauvais paramètre : une région de tâches réelles sans masse de défi suffit à l'attaquant (A-b, E-b3) | Acceptée | Nouveau paramètre : taux de reconnaissance à fausse reconnaissance quasi nulle (X4). |
| 18 | Un discriminateur qui échoue ne majore rien (A, L4). « L'agent interrogé compris » suppose que le saboteur avoue (A-a4). | Acceptée | L'indiscernabilité peut être réfutée, jamais établie. Les discriminateurs sont entraînés par un tiers qui dispose du générateur de défis. |
| 19 | Si la loi conjointe défi-réponse est identique sous P et Q, randomiser ne crée rien (D-b) | Acceptée | Correction de la thèse (§0, point 1). |
| 20 | P4 : l'issue est fixée par le choix de la famille (A-a5) | Acceptée, transformée | Le tiers classe les familles avant l'épreuve (dépendantes du résultat ou non). Les conclusions sont restreintes à une strate. |
| 21 | L'aveugle fuit par le canal fonctionnel : la grandeur décisive se déduit de la tâche (C-a2 ; contrôles A-c, C-c3, E-c3) | Acceptée dans sa portée | P4 est restreinte aux tâches où la grandeur décisive est une donnée, et précédée d'un test de fuite. C étiquette RAPPORTÉ que les tâches sont mathématiques ou algorithmiques. Je ne trouve pas cet énoncé dans les faits ; je garde l'étiquette mais ne m'appuie pas dessus. |
| 22 | Masquer entrave le débogage honnête (E-a4) | Rejetée en partie | Mon duel contenait déjà le contrôle « perte honnête avec et sans aveugle ». Je le conserve. |
| 23 | Sabotage non directionnel : gonfler le bruit pour étouffer une découverte vraie (E-a4, E-c2) | Acceptée, transformée | Strate rapportée à part. Je prédis que P4 n'y fait rien. |
| 24 | Zone grise du duel P4 ; « non significatif » n'est pas une équivalence ; il faut une double différence P/Q et un masque placebo (E-b4, D-b, D-c) | Acceptée | Test d'équivalence, assignation aléatoire, bras placebo (X5). |
| 25 | log₂\|S\| ne borne pas E[L] sans restriction sur L (D-b) | Acceptée | Retirée. Elle était HYPOTHÈSE et ne porte plus rien. |
| 26 | Précurseurs : estimer Q(T_alerte < T_irréversible) sur tous les épisodes, pas l'avance moyenne parmi les épisodes alertés (D-b) | Acceptée | Métrique remplacée. |
| 27 | Le rapport TPR tenu à l'écart / TPR connu est indéfini ou trompeur ; une famille est un seul tirage (A-b, D-b) | Acceptée. La seconde partie n'est pas corrigeable au budget. | Je rapporte les deux TPR avec leurs intervalles, et l'écart à l'audit uniforme. Toute conclusion reste restreinte à la famille testée. |
| 28 | Une famille fixée avant l'instrument teste un transfert à l'aveugle, pas une attaque adaptative (D-a4) | Acceptée, transformée | Deux phases (§2). J'appliquais mal ma propre exigence d'attaques adaptatives (ma conception, §1, point 2). |
| 29 | Équipe rouge de la même famille de modèles que l'agent (E-a4) | Acceptée | Équipe rouge d'une autre famille. |
| 30 | S7 : la raison donnée est elle-même une hypothèse ; les seuils illustratifs n'ont pas de règle de gel (A-a6) | Acceptée | S7 reste HYPOTHÈSE, et sa justification aussi. Les seuils sont gelés par le tiers et engagés par empreinte. |
| 31 | Contrôles négatifs manquants (A-c, C-c, D-c, E-c) | Acceptés | Intégrés à X1–X5. |

---

## 2. Expériences corrigées (livrable b)

**Règles communes, nouvelles par rapport à III.1 :**

- **Gel.** Seuils, marges m, effectifs maximaux et strates sont fixés par le tiers et engagés par empreinte sha256 avant l'ouverture des données (ligne 30).
- **Deux phases.**
  - Phase 1 : une famille conçue à l'aveugle, engagée avant la conception des instruments.
  - Phase 2 : une attaque adaptative par un tiers contre l'instrument gelé.
  - Je ne sais pas si la phase 2 est faisable au budget des faits ; A ne le sait pas non plus.
- **Équipe rouge** d'une autre famille de modèles que l'agent et le jumeau.
- **Unité statistique** : la tâche tirée indépendamment, jamais le jeton ni le segment. Plusieurs graines par tâche.
- **Dénominateur** : toutes les tâches assignées, refus et omissions compris. C'est la condition de D, que je reprends en le disant.
- **Décision.**
  - Un intervalle à 95 % entièrement d'un côté de la marge réfute l'autre hypothèse.
  - S'il chevauche la marge, on ajoute des épisodes jusqu'au maximum gelé, puis on déclare « non concluant ».
  - Aucune zone grise n'est rapportée comme un résultat.
- **Portée** : une famille est un tirage. Généraliser au « nouveau » exige plusieurs familles conçues par plusieurs tiers.

### X1 (nouvelle, à faire en premier) : fermer le canal non vérifiable par conception de la tâche

*J'emprunte à D l'idée d'une propriété fixée par le tiers avant la soumission, et je la soumets à un duel de pire cas.*

- **Pourquoi elle passe devant.**
  - L'audit (X2) ne garantit quelque chose que là où d(a) > 0, et un attaquant informé se placera là où d(a) = 0.
  - Le seul levier sans détection est que les choix non vérifiables ne puissent plus porter beaucoup de perte.
  - Si ce levier n'existe pas, X2 à X5 deviennent secondaires pour le problème (C).
- **Montage.**
  - Mondes plantés dont la vérité est connue. Assignation aléatoire, tâche par tâche, à trois bras :
    - **libre** : l'agent choisit son analyse ;
    - **contraint** : le tiers fixe, avant la soumission, la décision visée, la forme canonique du produit et la propriété vérifiée ; le reste est renvoyé au témoin ou rendu réversible ;
    - **placebo** : contrainte de même format, sans restriction réelle.
  - L'équipe rouge (phase 2) cherche à maximiser la perte de décision L tout en passant la vérification.
- **Grandeurs.**
  - Excès de perte du pire cas trouvé : ΔL = L_rouge − L_honnête, dans le bras contraint.
  - Coût honnête : taux de refus et de travail honnête empêché.
- **Duel.**
  - H_A : borne supérieure de ΔL < m (illustratif) **et** refus honnête < r (illustratif).
  - H_B : borne inférieure de ΔL ≥ m, **ou** refus honnête ≥ r.
- **Issues.**
  - Si H_A tient, elle falsifie « le dommage interprétatif est irréductible par conception de la tâche », mais seulement contre l'équipe rouge testée : un pire cas trouvé minore le pire cas réel.
  - Si H_B tient, elle falsifie la possibilité de borner (C) par conception sur ces tâches. Le problème (C) doit alors reposer sur l'architecture (irréversibilité, autorisations), pas sur l'audit.
- **Contrôles.**
  - Bug honnête reproductible : il doit être compté comme perte acceptée.
  - Les tâches qui n'admettent aucune propriété fixable restent au dénominateur.
  - Bras placebo.

### X2 (ex-P1, rétrécie) : plancher d'audit sur la généalogie de l'affirmation décisive

- **Mécanisme.**
  - On tire en secret des nœuds de la généalogie de l'affirmation décisive, à un taux plancher uniforme λp, auquel s'ajoute un surplus orienté par les moniteurs. Chaque nœud tiré est ré-exécuté sous forme canonique.
  - Propriété du protocole, vraie par construction et non un résultat empirique : chaque nœud est audité avec une probabilité au moins λp, quels que soient les scores des moniteurs.
  - Borne qui en découle (HYPOTHÈSE quant à ses prémisses) : P(nœud saboté non révélé) ≤ 1 − λp·s, si le calendrier ne fuit pas, où s est la sensibilité mesurée de la ré-exécution sur la strate.
- **Duel.**
  - H_A : à coût total égal, escalades comprises, le tirage sur la généalogie avec plancher réduit la perte acceptée d'au moins m (illustratif) par rapport à l'audit uniforme sur toute la trace.
  - H_B : la réduction est inférieure à m.
  - Si H_B tient, le ciblage n'apporte rien de plus que des vérifications supplémentaires (D). Si H_A tient, l'hypothèse « le ciblage par généalogie est inutile » est falsifiée.
- **Mesures.**
  - s par strate, avec intervalle de Clopper-Pearson.
  - Taille de la généalogie décisive rapportée à celle de la trace (réponse à la ligne 15).
  - Divergences honnêtes à la ré-exécution : le critère « ≤ 1 % » n'est jugé qu'à partir d'environ 299 épisodes sans divergence (L3).
- **Contrôles.**
  - **Bug honnête reproductible** : il doit passer l'audit. C'est la mesure directe de la strate où d(a) = 0.
  - **Fuite du calendrier** : un prédicteur tiers et l'agent prédisent les nœuds qui seront audités. Au-dessus du hasard, la borne tombe.

### X3 (ex-P2) : sauvetage sous panne de la sonde

- **Données.** Matrice conjointe épisode × moniteur, avec plusieurs graines par tâche pour estimer θᵢ(x) et le terme de covariance conditionnelle (ligne 5).
- **Grandeurs.**
  - ρ_adj = Q(l'adjudant alerte avant l'instant d'irréversibilité | la sonde rate), pondérée par la perte L.
  - ρ_unif : la même quantité pour l'audit uniforme de même budget.
  - Diagnostics seulement : P(alerte de l'adjudant | la sonde touche) et φ.
- **Duel.**
  - H_A : borne inférieure de ρ_adj − ρ_unif ≥ m (illustratif).
  - H_B : borne supérieure de ρ_adj − ρ_unif < m.
- **Issues.**
  - H_A falsifie, pour cette famille, « quand la sonde est aveugle, aucun second regard ne fait mieux que le hasard ».
  - H_B falsifie la valeur ajoutée de cet adjudant par rapport au hasard.
  - Issue « non jugeable » déclarée d'avance si les ratés de la sonde sont moins de N_min (illustratif). Elle signifie que la sonde suffit sur cette famille, et ne dit rien du second regard.
- **Contrôles.**
  - Adjudant factice : tirage de Bernoulli indépendant, au même taux marginal que l'adjudant réel, passé par le même calcul. Il doit donner ρ ≈ ρ_unif (A).
  - Permutations des appariements à l'intérieur des strates de difficulté (D).
  - Plis séparés pour la sélection et l'estimation.
  - Rapport par régime et pour le pire régime.

### X4 (ex-P3) : défis secrets

- **Étape 1 : réfuter l'indiscernabilité.**
  - Un tiers qui dispose du générateur entraîne des discriminateurs.
  - Grandeur : fraction des tâches réelles reconnues comme réelles alors qu'aucun défi tenu à l'écart n'est mal classé, avec borne de Clopper-Pearson.
  - H_A : cette fraction est au moins δ (illustratif). L'indiscernabilité est falsifiée et le mécanisme est mort.
  - H_B : elle reste sous δ pour tous les discriminateurs testés. Cela falsifie seulement la séparabilité par cette classe de discriminateurs (L4) ; rien n'est établi.
- **Étape 2, seulement si H_B.**
  - Même duel que X3 : TPR des défis contre audit uniforme de même budget.
  - Contrôle de D : des défis sans intervention utile doivent donner un TPR d'environ α.

### X5 (ex-P4, conditionnelle) : analyse aveugle

- **Préalable : test de fuite.**
  - Seules entrent les tâches où la grandeur décisive est une donnée.
  - Un prédicteur tiers et l'agent prédisent la grandeur masquée avant la levée de l'aveugle.
  - Une prédiction au-dessus du hasard exclut la tâche.
- **Montage.**
  - Assignation aléatoire entre masque, absence de masque et masque placebo, sous P (honnête) et sous Q (attaque).
  - Familles classées d'avance par le tiers : dépendantes du résultat, ou non directionnelles (étouffement d'une découverte vraie).
- **Grandeur.** Double différence (masque contre sans masque, puis Q contre P) du taux d'atteinte de la conclusion fausse plantée.
- **Duel, sur la strate dépendante du résultat.**
  - H_A : borne inférieure ≥ m (illustratif).
  - H_B : intervalle entièrement contenu dans [−m, m] (test d'équivalence).
  - H_A falsifie « l'aveugle n'a pas d'effet propre au sabotage ». H_B falsifie P4 dans son domaine revendiqué.
- **Strate non directionnelle.** Rapportée séparément. Je prédis qu'elle ne montre aucun effet.
- **Contrôle.** La perte honnête avec et sans masque doit rester dans la marge.

### Chances révisées (estimations subjectives, illustratives)

| Mécanisme | Chances |
|---|---|
| X1 | ≈ 0,3 que H_A survive à une équipe rouge adaptative |
| X2 | ≈ 0,5 que le ciblage batte l'audit uniforme ; s ≈ 0 sur la strate des choix est presque certain par construction |
| X3 | ≈ 0,2 |
| X4 | ≈ 0,15 |
| X5 | ≈ 0,15 dans son domaine restreint |
| P2 comme alarme certifiée | Retiré tant que n + 1 reste sous la condition donnée par E (ligne 6) : ce n'est plus une question de chances |

---

## 3. Réponse à l'arbitre, en une page (livrable c)

**Le mécanisme adjudant que je défends après critique** n'est pas un détecteur. C'est une règle de conception jointe à l'aléa du défenseur :

- (i) mettre chaque tâche sous une forme où une propriété fixée par un tiers, avant la soumission, porte la décision ;
- (ii) auditer en secret la généalogie de l'affirmation décisive, avec un plancher uniforme qu'aucun score ne peut abaisser ;
- (iii) cantonner les moniteurs, sondes comprises, au triage au-dessus de ce plancher.

Ce qu'il garantit ne dépend d'aucune distribution d'attaques, mais ne couvre que la partie de la tâche où une discordance est auditable.

**Ce qui est établi (sur le papier ; aucun résultat empirique ne l'est) :**

- **Borne de variation totale** (VÉRIFIÉ, ma conception, §4.1). Aucun détecteur passif ne dépasse α + TV(P, Q), lentilles comprises. Elle s'applique aussi aux défis : intervenir est nécessaire, pas suffisant.
- **Plancher conforme 1/(n + 1)** (VÉRIFIÉ) : n ≥ 99 épisodes honnêtes par régime pour une garantie marginale à 1 %. La garantie conditionnelle en exige davantage, n ≥ 299 avec zéro alerte observée (L3 de A, HYPOTHÈSE selon A).
- **(1 − p)^k sous ses hypothèses** (VÉRIFIÉ). La borne est vide quand s = 0 ou quand le calendrier fuit, et l'attaquant choisit k = 1.
- **Borne de Fréchet R ≤ 1/max(p₁, p₂)** (HYPOTHÈSE selon A ; VÉRIFIÉ selon C et E). Elle a falsifié la forme de mon duel P2, pas une hypothèse empirique.
- **Plafond n + 1 des e-valeurs calibrées sur n épisodes** (VÉRIFIÉ selon E, section b). Il retire à l'agrégation par e-valeurs tout rôle d'alarme à petit n.

**Ce qui n'est pas établi :**

- **La décorrélation des pannes sous une attaque nouvelle** (S1). La mesurer suppose une attaque adaptative conçue par un tiers, et je ne sais pas si elle est faisable au budget.
- **La part de la perte de sabotage qui tombe dans la partie auditable**, et la possibilité de la réduire par conception de la tâche. C'est le chiffre qui décide de (C).
- **L'indiscernabilité des défis.** Elle ne peut être que réfutée.
- **L'étanchéité de l'aveugle** sur les tâches où la grandeur décisive se calcule.
- **Toute généralisation au « nouveau ».** Une famille est un seul tirage.

**L'expérience à faire en premier.**

1. **Le premier pas, sans dépense** : sur les journaux existants, compter
   - la fraction des tâches qui admettent une propriété fixable par un tiers avant soumission ;
   - la fraction des épisodes tombant dans des régimes non certifiables (n < 99) ;
   - la taille des généalogies décisives rapportée à la trace.
2. **Ensuite, X1.**
   - Son issue détermine si (C) peut reposer sur l'audit ou doit reposer sur l'architecture seule.
   - Si H_B tient, la valeur de X2 à X5 pour (C) s'effondre, et il vaut mieux le savoir avant de les financer.
   - Si H_A tient, X2 devient l'expérience suivante, car elle porte la seule garantie quantifiée sur toutes les stratégies dont nous disposons.

FIN-DE-CELLULE