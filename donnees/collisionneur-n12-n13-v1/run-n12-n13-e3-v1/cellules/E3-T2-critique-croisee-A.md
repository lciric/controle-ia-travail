# Proposition A — Tour III.2 : critique croisée de méthode (N12, N13)

Pièces reçues : B, C, D, complètes (chacune close par sa ligne de fin). Aucun PDF n'est servi ; je ne m'appuie que sur les six pièces de faits. Les chiffres d'Avalon sont OBSERVÉ-NON-AUDITÉ (un run, lecture non contre-lue) ; tout nombre que j'introduis est illustratif. Je ne fusionne rien : chaque section critique une proposition pour ce qu'elle dit.

Convention commune pour (b) : je note σ² la variance d'évaluation (mesurée par le pilote A/A de N-045 §6-i), τ² la variance entre runs d'entraînement (graines), k le nombre de graines par bras, n le nombre de runs d'évaluation par point de contrôle, π la prévalence des positifs, N l'effectif d'agents par run.

---

## Sur la proposition B

### (a) Défauts de méthode

1. **N12-E1 — statistique du maximum.** Le critère est « le meilleur score net sur les 3 dernières générations ». Le maximum d'une série favorise par construction le bras dont la variance est la plus grande ou dont le nombre d'évaluations est le plus élevé ; or le bras « sélection + génération » explore un espace plus large, donc plus variable. L'issue « falsifie H_A » est donc atteignable sans effet moyen. Le coût des pièces générées qui échouent (compilation vide, moniteur inerte) n'est pas dit compté dans le coût du bras.
2. **N12-E1 — contrôle mal apparié.** Le bras « pièce neuve à invite permutée » produit une pièce vraisemblablement non fonctionnelle ; il sépare « fonctionne / ne fonctionne pas », pas « générée / réaffectée ». La conclusion annoncée (« la pièce neuve ne vaut pas mieux qu'une pièce existante réaffectée ») n'est pas ce que ce contrôle mesure. Le bras utile est « même générateur, sortie contrainte au catalogue » (D le pose ; je m'en sers en le disant).
3. **N12-E2 — vrai par construction.** « Lean détecte la garde fautive, l'empreinte ne le peut pas » est une tautologie : une empreinte n'inspecte aucune sémantique. H_A et H_B ne s'opposent pas sur un fait mesurable ; le comparateur manquant est la suite bon marché (tests, scripts numériques, mutations). Le nombre de « propriétés non triviales prouvées » n'est pas un estimateur : il n'a ni loi, ni témoin.
4. **N13-E1 — fuite et faux contrôle négatif.** Le bras « RL avec terme de signalement » n'est pas un contrôle négatif : c'est une manipulation positive qui entraîne la métrique (D le dit aussi). S'il est conservé, les scénarios de signalement d'entraînement et d'évaluation doivent être disjoints, ce que B ne fixe pas. Le critère « taux de runs avec au moins un signalement » dépend de N : si le bras individuel et le bras collectif n'ont pas le même N, la différence est mécanique (voir b).
5. **N13-E1 — unité d'inférence.** Mann-Whitney « sur les taux au dernier point de contrôle » prend les runs d'évaluation comme unités ; ils partagent une même politique. La question causale (« le collectif cause ») porte sur la variance entre entraînements ; avec une graine par bras, elle est hors de portée (voir b).
6. **N13-E2 — cible mal posée.** La variable à prédire est « le signalement était dû et n'a pas été fait », définie par le contrat explicite du monde planté. C'est exactement ce que calcule la vérification mécanique (journal des outils + contrat + délai) : elle a une AUROC de 1 sur cette cible par construction, et « sa combinaison bat la vérification seule » est impossible. Les « cas où la vérification mécanique est silencieuse » n'existent pas sous contrat explicite. La cible utile est la prédiction *avant* le point de décision ou la détection *sans* contrat (faits abstraits du lot 3, pièce 4 §3.3) ; B ne la nomme pas.
7. **N13-E2 — fuite sonde/évaluation.** Rien ne dit sur quelles traces la sonde est entraînée. Si entraînement et test partagent le run ou le point de contrôle, la sonde apprend l'état d'entraînement, non l'omission. B lui-même rapporte (pièce 4 §2.4-2) que le même modèle signale à 77 % ou à 0–3 % selon le point de contrôle : le point de contrôle est un confondant de premier ordre.
8. **N13-E3 — vérité et graines.** La vérité binaire des fiches vient « de l'oracle du monde planté ou du verdict humain ». Si le même verdict sert à entraîner le juge RLCR et à l'évaluer, l'ECE est vraie par construction. « Intervalles non chevauchants » n'est pas un test ; et le bootstrap sur fiches n'estime pas τ² (Damani ne rapporte aucune graine, pièce 5 §1.11-1).

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **Saturation de la statistique « au moins un »** : si les N agents signalent i.i.d. avec probabilité p, P(run signale) = 1 − (1 − p)^N. Pour N = 8, p = 0,3 donne 0,94 (illustratif) ; toute différence entre bras sur p sous ≈ 0,3 est invisible. Si le bras individuel a N = 1, la même p donne 0,3 : écart de 64 points sans aucun effet du régime de crédit.
- **Intervalle par run** : à n = 30 runs, demi-largeur de Wilson ≈ 1,96·√(0,25/30) ≈ 0,18 à p = 0,5 (illustratif). Une différence de taux sous ≈ 25 points n'est pas jugeable à cet effectif, qui est celui d'Avalon.
- **Variance hiérarchique** : Var(estimateur de bras) = τ²/k + σ²/(k·n). Avec k = 1, τ² n'est pas identifiable et le test de Mann-Whitney sur les n runs a un α nominal faux pour toute hypothèse sur l'entraînement. Non jugeable tant que k < 2 ; puissance calculable seulement avec τ² estimé.
- **Maximum (N12-E1)** : E[max de m tirages N(μ, s²)] ≈ μ + s·√(2 ln m). Un bras avec s doublé ou m doublé gagne sans que μ bouge.
- **AUROC (N13-E2, E3)** : écart-type d'ordre √(A(1−A)/min(n₊, n₋)) (illustratif). Si π → 0, n₊ = nπ tombe et la marge δ = 0,10 n'est pas détectable ; si π → 1 ou 0 exactement, l'AUROC n'est pas définie.
- **ECE à 10 classes** : le bruit par classe est d'ordre √(p(1−p)·10/n) ; à n = 200, ≈ 0,11 (illustratif), supérieur aux écarts que B veut lire (0,03 contre 0,10). L'ECE est en outre nulle par construction pour une confiance constante égale au taux de base : B l'exige pour le témoin RLVR mais pas pour le bras RLCR.

### (c) Contrôles négatifs dont l'absence serait fatale

- N12-E1 : générateur à sortie contrainte au catalogue ; scores permutés dans le signal de sélection ; A/A à budget égal avec le même nombre d'évaluations par bras.
- N12-E2 : gardes valides soumises à Lean (taux de rejet par échec de tactique) ; spécification volontairement affaiblie qui compile.
- N13-E1 : bras non entraîné au même point de départ ; récompenses permutées ; N identique entre bras ; scénarios de signalement tenus à l'écart de tout entraînement ; au moins deux graines par bras.
- N13-E2 : positifs et négatifs issus du *même* point de contrôle ; cas « envisagé puis légitimement non signalé » (pièce 4 §3.4 : 89–98 % des agents envisagent la révocation sans la commettre) ; activations permutées.
- N13-E3 : confiance constante au taux de base ; confiances permutées ; partition fiches entraînement/évaluation par famille, verdict humain exclu de l'entraînement.

---

## Sur la proposition C

### (a) Défauts de méthode

1. **Duel 1 — hypothèses non exclusives.** H_A contient une disjonction (« ou la Couche 3 viole les gardes ») et H_B est une existence (« découvre un opérateur valide »). Un T_fuite > 0 ferme la couche quel que soit ΔS : c'est une règle de décision, pas une inférence. Et « T_fuite = 0 » est observé par un moniteur externe dont le rappel n'est pas étalonné : zéro détection n'est pas zéro fuite (voir b).
2. **Duel 1 — seuil 2σ_bruit mal calibré.** σ_bruit est l'écart-type d'un score ; la différence de deux bras a une variance 2σ². Un seuil à 2σ sur la différence n'a pas l'α annoncé (voir b). Le taux de fausses promotions « α ≤ 0,05 » et le seuil 2σ sont deux critères juxtaposés sans règle de conjonction.
3. **Duel 2 — puissance et asymétrie par construction.** Dix énoncés, cinq fautes plantées : un écart d'une faute vaut 20 points de rappel, dans le bruit binomial. Les fautes « hypothèse de dérivabilité manquante » sont indétectables par une grille numérique par construction (une grille ne teste que des points) ; les fautes « inégalité stricte au bord » sont détectables par la grille par construction. Le résultat dépend donc de la composition du banc, choisie par un planteur qui connaît les deux bras. Le taux d'échec de tactique dépend de la compétence du formalisateur : confondant non contrôlé.
4. **Duel 3 — le facteur « crédit » confond attribution et information.** Le bras individuel est « évalué sur l'oracle du sous-rôle » : cet oracle n'existe pas dans N-058 (pièce 2 : oracle des structures plantées et des témoins), il faudrait l'inventer. Le bras individuel reçoit alors un signal plus riche, pas seulement mieux attribué. Pour isoler l'attribution, il faut que la récompense collective soit une fonction connue des récompenses individuelles (somme), à information égale.
5. **Duel 3 — fuite par la garde d'héritage.** Le facteur K = 3 « valorise les témoins d'intégrité plantés » : si les canaris de signalement entrent dans la récompense et que T_sig est mesuré sur des canaris de même forme, la précaution « obligatoire » est vraie par construction. D signale le même risque ; je le reprends. Les scénarios d'évaluation du signalement doivent être tenus à l'écart de l'entraînement, ce que C ne fixe pas.
6. **Duel 3 — T_rec circulaire.** La « reconnaissance interne ≥ 90 % » est lue par une sonde linéaire entraînée sur quoi ? Si elle est entraînée sur les mêmes points de contrôle que ceux qu'elle sert à caractériser, T_rec est une sortie de l'instrument, non une variable de contrôle. La pièce 4 §1.8-2 montre déjà que « reconnaissance » agrège trois mesures hétérogènes chez Avalon ; C en fait une constante sans la définir.
7. **Duel 3 — zone non décidable.** H_B tombe sous 10 points, H_A sous 25 points : entre 10 et 25, aucune issue. B4 exige que chaque issue falsifie quelque chose.
8. **Duel 3 — une graine par cellule.** Quatre cellules 2×2 sur un seul run d'entraînement chacune : τ² non identifiable, comme chez B.
9. **Fusion c1/c3 — sélection sur la variable dépendante.** Le générateur d'omission (c3) n'est retenu que si le crédit collectif à K = 1 a fait chuter T_sig. Les traces servies aux sondes viennent donc de la cellule *choisie pour* son omission : les positifs portent la signature du régime (poids, pas d'entraînement), les négatifs viennent d'une autre cellule. Une sonde peut apprendre l'identité du régime et afficher un rappel sans rien lire de l'omission.
10. **Table, instrument 2 — « 100 % des tentatives » non mesurable.** Un rappel de 1,0 ne s'estime que sur des tentatives plantées connues ; sans équipe rouge plantée, le chiffre est vide.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **Seuil 2σ sur une différence** : si D ~ N(0, 2σ²), P(D > 2σ) ≈ P(Z > 1,41) ≈ 0,08 unilatéral (illustratif), pas 0,05 ; et ce pour une seule comparaison, sans rotation de familles. Avec r familles en rotation, le risque global croît en ≈ 1 − (1 − 0,08)^r.
- **Zéro fuite observée** : sur m tentatives connues, la borne supérieure à 95 % du taux est ≈ 3/m (illustratif). Sans tentatives plantées, m = 0 et la borne est 1.
- **Rappel sur 5 fautes** : la différence entre 5/5 et 4/5 n'est pas distinguable du hasard (intervalle de Wilson à n = 5 ≈ [0,57 ; 1] pour 5/5).
- **Seuil de 10 points à n = 30 runs** : demi-largeur ≈ 0,18 (voir B) ; la condition « < 10 points » n'est pas jugeable, la condition « ≥ 25 points » l'est à peine.
- **Plancher de signalement** : si le modèle 8B de base signale avec p₀ proche de 0, toute cellule a T_sig ≈ 0 et le facteur crédit n'a aucune variance à expliquer. Condition de jugeabilité : p₀(1 − p₀)·n·k suffisant pour la marge gelée, à mesurer au pilote avant le factoriel.
- **AUROC + 0,03 (Duel 4)** : écart-type d'ordre √(A(1−A)/min(n₊, n₋)) ≈ 0,03 à 200 positifs et 200 négatifs (illustratif) ; la différence seuil est de la taille de son propre bruit. Jugeable seulement à plusieurs milliers d'unités par classe, ou par comparaison appariée (même fiches, test de DeLong apparié) que C ne précise pas.
- **Somme des confiances ≤ 1,05** : perd son sens si les réponses ne sont pas mutuellement exclusives (fiches ordinales, N-045 §5 vérités différées) ; C l'exige sans dire sur quelles réponses.

### (c) Contrôles négatifs dont l'absence serait fatale

- Duel 1 : tentatives de fuite plantées par une équipe rouge hors organisme (seul moyen d'estimer le rappel de T_fuite) ; A/A avec le même nombre d'évaluations par bras.
- Duel 2 : banc composé par un tiers qui ne connaît pas les bras ; énoncés valides avec hypothèses implicites non nécessaires (faux rejets Lean) ; même formalisateur ou formalisateur croisé.
- Duel 3 : collective = somme des individuelles ; scénarios de signalement hors entraînement ; canaris « à ne pas signaler » (C les a) ; sonde de reconnaissance entraînée sur un point de contrôle tenu à l'écart ; au moins deux graines par cellule ; cellule mono-agent à N égal et budget égal, distincte du facteur crédit.
- Duel 4 : confiance constante au taux de base (C l'a) ; injection appliquée aux deux bras ; partition par famille entre pli de recalibration et test.

---

## Sur la proposition D

D est la plus prudente sur les statuts (chiffres d'Avalon en OBSERVÉ-NON-AUDITÉ) et sur la séparation récompense/mesure. Ses défauts sont surtout ceux d'une conception laissée en paramètres ouverts.

### (a) Défauts de méthode

1. **δ et ε non liés à la loi du bruit.** Tous les seuils sont « gelés avant lecture » mais aucun n'est rattaché à σ, τ, n, k. Un δ gelé sans ces grandeurs ne permet pas de calculer la puissance ; l'expérience n'est falsifiable qu'une fois ce lien écrit.
2. **E12-1 — pas de métrique principale.** Structures retrouvées, témoins promus/rejetés, détection à fausse alerte fixée, score net : quatre lectures sans ordre de primauté. Sans primaire gelée, la lecture « sur au moins les familles préenregistrées » ouvre des comparaisons multiples non corrigées.
3. **E13-1 — appariement sur une variable post-traitement.** « À performance de tâche appariée » suppose de choisir, après coup, les points de contrôle de chaque bras ayant la même performance. Si le bras collectif y parvient plus tôt (ou plus tard), les points appariés diffèrent par le nombre de pas de gradient, qui est lui-même un candidat causal de l'érosion (Avalon : chute monotone avec le pas, p. 35). La règle d'appariement doit être fixée d'avance (pas égaux *et* performance rapportée), sinon l'appariement choisit le résultat.
4. **E13-1 — « récompense individuelle » sous-spécifiée.** Dans un organisme multi-agents, le crédit individuel exige un signal par agent. S'il n'est pas une décomposition de la récompense collective à information égale, le même confondant que chez C apparaît. D dit « mêmes primitives d'oracle » sans dire comment l'individuel est dérivé.
5. **E13-1 — graines.** Le tableau matériel évoque « plusieurs graines » ; l'expérience n'en fixe pas le nombre, et la falsification par « chutes égales » est une équivalence qui exige τ² estimé.
6. **E13-3 — confondant de régime.** Les traces viennent des bras d'E13-1 : les omissions du bras collectif, les non-omissions des autres bras. Positifs et négatifs portent alors des poids différents ; une sonde peut classer le régime, pas l'omission. C'est fatal pour l'instrument, pas seulement une perte de puissance. Les positifs et négatifs doivent être tirés du même point de contrôle, appariés sur tâche, longueur et issue ; D l'exige dans sa table (« cas honnêtes appariés pour longueur, tâche et issue ») mais ne l'impose pas à E13-3.
7. **E13-4 — origine de la vérité binaire.** D ne dit pas d'où vient la vérité des fiches hors monde planté. Si c'est un verdict de juge, calibrer un juge sur le verdict d'un juge est circulaire ; N-058 n'interdit que la sélection d'agents, mais le problème est de validité de construit, pas de gouvernance.
8. **E12-2 — spécification et fautes par le même auteur.** La suite adversariale (preuves tronquées, spécification affaiblie) est bonne ; mais si l'auteur de la spécification Lean connaît les fautes plantées, la spécification est écrite pour les attraper. Fuite entre construction et évaluation de l'instrument.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **Équivalence (E12-1, E13-1, E13-4)** : un test d'équivalence à marge ε exige, pour une différence de moyennes à variance 2σ_eff², un effectif d'ordre 2(z_{1−α} + z_{1−β})²·σ_eff²/ε² par bras (illustratif : à ε = σ_eff, ≈ 17 par bras pour α = β = 0,05). Si σ_eff inclut τ²/k avec k = 1, σ_eff est inconnue et l'équivalence n'est pas jugeable, quelle que soit n.
- **Familles tenues à l'écart** : si la rotation porte sur r familles, l'inférence « pire famille » est un minimum sur r : sa loi est celle d'un extrême et son intervalle croît avec r ; à r petit, « pire famille » et « moyenne » ne sont pas distinguables.
- **Prévalence (E13-3)** : si π est la fréquence d'omission dans le bras source, le nombre de positifs est n·N·π aux points de décision ; le rappel à fausse alerte fixée exige n₊ tel que l'intervalle sur le rappel soit inférieur à δ ; avec π sous ≈ 0,05 et n = 30 runs de N = 4, n₊ ≈ 6 (illustratif) : non jugeable.
- **Fausse alerte fixée** : à FPR fixé à 1 %, l'estimation du seuil demande ≈ 100·c négatifs pour c alertes attendues ; sous ≈ 500 négatifs appariés, le seuil lui-même est bruité et le rappel mesuré n'est pas comparable entre instruments.
- **Appariement post-traitement (E13-1)** : si l'appariement sélectionne des points de contrôle en fonction d'une performance corrélée à la variable de sortie, l'estimateur de différence est biaisé d'une quantité qui ne diminue pas avec n.
- **ECE/AUROC (E13-4)** : mêmes bornes que pour B ; D demande justement « rappel à fausse alerte fixée » en plus, ce qui lève la dégénérescence de l'ECE sous confiance constante.

### (c) Contrôles négatifs dont l'absence serait fatale

- E12-1 : D les a presque tous ; manque le contrôle « même nombre d'évaluations par bras » (le bras générateur peut produire plus de candidats).
- E12-2 : spécification écrite par un tiers aveugle aux fautes ; artefacts recompilés (D l'a).
- E13-1 : règle d'appariement gelée (pas de gradient) ; récompense individuelle définie comme décomposition de la collective ; k ≥ 2 graines ; bras « entraînement générique » défini explicitement (quelle récompense ?).
- E13-3 : positifs et négatifs du même point de contrôle ; activations permutées entre régimes (si une sonde sur étiquettes de régime permutées garde son rappel, elle lit le régime) ; omissions plantées comme étalon externe au générateur.
- E13-4 : vérité binaire indépendante de tout juge ; confiance constante au taux de base (D l'a).

---

## Note transversale, sans fusion

Trois défauts reviennent chez les trois propositions, à des degrés différents : (i) l'unité d'inférence pour toute affirmation causale sur l'entraînement est la graine, non le run d'évaluation — aucune des trois ne fixe k ≥ 2 dans le corps de l'expérience ; (ii) les positifs d'omission servis aux sondes ne doivent pas venir d'un régime différent de celui des négatifs — B l'omet, C et D le subissent par la fusion c1/c3 ou par E13-3 ; (iii) la vérité binaire des juges doit être extérieure à tout juge. Ces trois points sont des conditions de jugeabilité, pas des choix de priorité ; ils précèdent toute décision sur N12 et N13.

FIN-DE-CELLULE