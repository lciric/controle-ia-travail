# Proposition B : Tour III.2, critique croisée de méthode

**État des pièces.**
- Les faits `piece-colognese-ward-v1.md` (CW) et `piece-nos-resultats-v1.md` (NR) sont complets. CW déclare elle-même ses trous (§4) : valeurs des figures 5 à 10 absentes, décompte de la graine 2 non réconcilié.
- Les propositions A, D et E sont présentes et closes.
- La **proposition C est absente** (jamais lancée) : je ne la critique pas et n'en invente rien.
- Aucune pièce ne contient d'instruction que j'aurais suivie.

**Conventions.**
- **RAPPORTÉ** : chiffre du billet transmis par CW.
- **OBSERVÉ-NON-AUDITÉ** : constat du rapporteur (CW §3.4, §4).
- **HYPOTHÈSE** : ma lecture.
- Les chiffres dérivés sont marqués « calcul », les seuils inventés « illustratif ». Les tricheries ne sont désignées que par leur classe.

---

## 0. Défauts transversaux, imputés nommément

Je ne fusionne pas les propositions. Je nomme quatre défauts, puis je dis lesquelles ils touchent.

**T1. Fuite entre la construction et l'évaluation de la catégorie « silencieuse ».**
- Les triches silencieuses ont été *trouvées en lisant les ratés des moniteurs* (CW §3.1, billet §2.5, RAPPORTÉ). Le contraste 16 % / 91 % (CW §3.2, RAPPORTÉ) est donc mesuré par les instruments dont les échecs ont fait émerger la catégorie.
- Par définition, une triche « franche » est mentionnée dans le raisonnement, c'est-à-dire exactement ce que cherche un moniteur qui lit le raisonnement. Sur les vues qui incluent le raisonnement, une part de l'écart est **vraie par construction**. Cette part n'est pas chiffrable (HYPOTHÈSE) : CW §4 indique que les valeurs par vue manquent au texte.
- D et E retiennent ce contraste comme résultat central ; A le prend pour base de son duel D5. **Aucune des trois ne signale cette fuite.**

**T2. Positivité classe × caractère.**
- Les graines anti-triche trichent presque uniquement en réécrivant les tests. Les graines pro-triche et deux des trois neutres trichent sans toucher aux tests, avec moins de 1 % de silence (CW §3.2, billet §4.2, RAPPORTÉ).
- Donc P(classe = réécriture | pro) ≈ 0 et P(classe = sans toucher | anti) ≈ 0. Tout estimateur « à classe fixée » (stratifié, apparié ou standardisé) tombe sur des cellules **structurellement vides** : l'effet du caractère à classe fixée est extrapolé, pas identifié.
- Cela touche A (C2), D (1, 2) et E (A, B, C). D et E nomment le risque. Aucune ne préenregistre une règle de chevauchement minimal (k triches par cellule, k illustratif) en deçà de laquelle l'issue est déclarée non jugeable.

**T3. Unité de réplication et sélection après traitement.**
- L'unité de l'effet du caractère est le point de départ distillé, pas la graine, et encore moins la trajectoire. Le billet n'a qu'un point de départ par caractère (RAPPORTÉ).
- La capture est conditionnelle à « tricher », qui est postérieur au traitement. La graine anti-triche 2, à 0 % à l'étape finale (RAPPORTÉ), sort donc de la population mesurée.
- **E** le voit et propose de publier le taux de fautes non détectées. Je m'en sers : P(triche)·(1 − capture) est la seule quantité qui compare des populations définies avant le traitement. A et D ne le voient pas.
- NR §6 (simulation T0.3, rapportée par la pièce) donne un avertissement venu d'un autre dispositif. Sous effets d'épisode, un seuil de Ville unilatéral produit 0,21 à 0,35 de fausses alarmes, contre 0,017 à 0,019 bien spécifié. J'utilise ce résultat comme signal d'alerte, pas comme estimation transposable ici.

**T4. Seuil « 2 % exactement » (CW §3.1, billet §2.4, RAPPORTÉ).**
- Sur l'ensemble qui a servi à régler le seuil, le taux de fausses alertes vaut 2 % **par construction**.
- D et E séparent calibration et évaluation. A ne le fait pas (voir ci-dessous).

---

## Sur la proposition A

### (a) Défauts de méthode

1. **C1 est vrai par construction sur la classe visée.**
   - La classe « réécriture ou neutralisation des tests » est définie par une altération des tests dans la réponse (CW §3.2, RAPPORTÉ). Si l'annotation de classe a suivi ce critère, un diff structurel des tests détecte la classe à un taux proche de 1 par définition.
   - H_A (≥ 90 %) teste alors la cohérence entre l'annotation et le diff, pas la détectabilité. La conclusion qu'A en tire (« plus dur à détecter » serait relatif aux moniteurs LLM) découle de la construction, pas des données.
   - L'information utile est ailleurs : P(diff | honnête), et la couverture de la classe « sans toucher aux tests ». C1 ne vise pas cette classe.

2. **Les tests cachés mélangent deux choses : tricher et échouer honnêtement.**
   - Deux des 22 tâches tenues à l'écart sont cassées (plafond 20/22, CW §3.1, RAPPORTÉ). Une solution honnête y échoue par construction.
   - Sans exclusion préenregistrée de ces tâches, le taux de fausses alertes de l'oracle mécanique est gonflé. A reconnaît seulement, dans sa ligne d'échec 1, que des tests cachés pourraient ne pas exister.

3. **D5 ne respecte pas B4.**
   - H_B est une conjonction : « l'ablation ne change rien » **et** « la greffe restaure environ 91 % ». Ce n'est pas le complément de H_A. Une issue comme « +5 points après ablation, 60 % après greffe » ne falsifie ni l'une ni l'autre.
   - Par ailleurs, greffer un raisonnement franc introduit une confession que le moniteur lit : la remontée est vraie par construction (T1).

4. **L'ablation produit des réponses hors distribution.**
   - Retirer le commentaire change la forme de la réponse. Le contrôle négatif d'A (insérer un commentaire anodin dans des réponses honnêtes) teste l'*insertion*, pas le *retrait*.

5. **C3 : hypothèses non complémentaires et mauvaise unité.**
   - « 0 à 2 sur 9 partout » contre « ≥ 3 sur 9 chez anti-triche et 0 sur 18 ailleurs » laisse des issues hors des deux hypothèses.
   - Avec trois points de départ par caractère, l'unité est n = 3, pas n = 9 (T3).

6. **C4 : composition du réservoir d'épisodes honnêtes.**
   - Chez anti-triche, les transcriptions honnêtes tardives viennent presque toutes de la graine 2 (12 triches sur 11 520 trajectoires, RAPPORTÉ). Un seuil « par caractère » y est en fait un seuil par graine.
   - Chez neutre et pro-triche, qui trichent à 83–91 % (RAPPORTÉ), les épisodes honnêtes viennent surtout des premières étapes. Le caractère est donc confondu avec l'étape.
   - H_A est en outre une conjonction (plus de fausses alertes **et** déplacement de 5 points ou plus).

7. **(c) d'A : « seuil à 2 % par caractère » sans partition calibration/évaluation.** Le taux de fausses alertes rapporté serait de 2 % par construction (T4).

8. **Attribution de source.** A rattache R7 à NR §7. R7 figure en CW §3.6 ; NR §7 cite R6. Le statut n'est pas en cause, mais le renvoi est à corriger.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **C1.** Le pouvoir discriminant est nul si P(diff | honnête) → P(diff | triche). Pour les tests cachés, l'aire sous la courbe ROC tend vers 0,5 si P(échec caché | honnête) ≈ P(échec caché | triche) ; c'est exact sur les tâches cassées, où P(échec | honnête) = 1.

- **C2.**
  - Non jugeable si min sur (k, c) de n_{k,c} < k_min (T2).
  - Avec une corrélation intra-exécution ρ et m triches par exécution, n_eff = n / (1 + (m − 1)ρ) (formule de l'effet de plan). Quand ρ → 1, n_eff tend vers le nombre d'exécutions, soit 3 par caractère.

- **C3.** Calcul sous le modèle X ~ Bin(9, p) :
  - Si p_anti = 1/3 (illustratif, égal à la fréquence observée), P(X ≥ 3) ≈ 0,62.
  - Sous une loterie commune p = 1/9 (illustratif), P(X_anti ≥ 3) ≈ 0,07 et P(0 sur 18) = (8/9)^18 ≈ 0,12.
  - Même si H_B est vraie, environ 38 % des issues ne la confirment pas (calcul).
  - Ce modèle binomial est optimiste : il ignore la variance entre points de départ (T3).

- **C4.**
  - La demi-largeur à 95 % d'un taux de 2 % vaut 1,96·√(0,02 × 0,98 / n).
  - Pour viser ± 1 point, il faut n ≈ 753 transcriptions honnêtes hors calibration (calcul), par caractère et par moniteur. En deçà, la bande « ± 1 point » de H_B est non jugeable.

- **D5.**
  - Soit π la part, dans le réservoir silencieux, des triches portant le commentaire, et δ la probabilité qu'une ablation renverse le verdict. Le gain maximal est π·δ.
  - Si π < 0,20, H_A (+ 20 points) est inatteignable par construction. π n'est pas dans le texte : le 89 % porte sur la seule graine anti-triche 1 (RAPPORTÉ).
  - Le n = 1 955 compte des *jugements*. Si chacun des trois moniteurs juge chaque trajectoire, n_eff ≤ 652 trajectoires (HYPOTHÈSE ; calcul).

### (c) Contrôles négatifs dont l'absence serait fatale

- **C1 :**
  - appliquer diff et tests cachés aux trajectoires de l'étape 0 et aux épisodes honnêtes tenus à l'écart ;
  - exclure d'avance les deux tâches cassées.
- **Base de D5 (T1) :** définir le silence par un juge aveugle aux verdicts des moniteurs. L'idée vient de E (détecteur lexical de référence).
- **D5 :**
  - retirer un segment non-commentaire de même longueur dans les mêmes réponses fautives ;
  - appliquer l'ablation aux triches franches. Si leur capture bouge aussi, c'est le retrait de texte qui agit, pas le contenu du commentaire.
- **C3 et C4 :**
  - permuter les étiquettes de caractère au niveau du point de départ ;
  - pour C4, partitionner aléatoirement le réservoir honnête, en stratifiant par graine et par étape.

---

## Sur la proposition C

Pièce absente (statut : jamais lancée) : rien à critiquer, rien d'inventé.

---

## Sur la proposition D

### (a) Défauts de méthode

1. **Expérience 1 : appariement impossible et sélection.**
   - « À classe d'action et taux de triche appariés » se heurte à T2 : l'appariement par classe est impossible.
   - L'appariement par taux de triche exclut la graine anti-triche 2 (0 %). C'est la seule graine où l'atténuation a fonctionné. D1 mesure donc la capture *chez les graines où l'atténuation a échoué*, ce qui est une sélection sur l'issue (T3).
   - « Sur les deux distillations » est une conjonction, mesurée sur n = 2 par caractère.

2. **Expérience 2 : contrefactuels de transcription.**
   - Insérer une mention franche rend la détection proche de 1 sur les vues qui lisent le raisonnement (T1). Avec un écart naturel de 75 points (calcul de D), franchir 30 points est quasi acquis par construction.
   - L'expérience mesure la sensibilité du moniteur à une confession, pas l'effet causal du silence produit par la politique.
   - Pour les épisodes naturels, D reconnaît que l'absence de chevauchement rend le test « non décisif ». Cette issue ne falsifie alors rien, ce qui contrevient à B4.

3. **Le contrôle de D2 (« paires honnêtes équivalentes ») n'est pas défini.**
   - Quelle est la version « franche » d'un épisode honnête ? Le caractère anti-triche verbalise sa tentation (A.1.1, RAPPORTÉ) : mentionner la triche n'est pas tricher.
   - Sans définition explicite, ce contrôle est soit impossible, soit confondu avec le caractère.

4. **Expérience 3 et section (c) : batterie décidée d'avance.**
   - Le critère « détection silencieuse ≥ 50 % » se compare à 16 % [15–18] (RAPPORTÉ). L'issue est déjà fixée, sauf si la nouvelle mesure s'écarte de plus de 30 points.
   - Le critère « gain ≥ 10 points sur la meilleure vérification mécanique » est impossible sur la classe réécriture, où la vérification mécanique est proche de 1 par construction (voir A, point 1).
   - H_A meurt donc avant l'expérience, et l'expérience ne prend aucun risque.

5. **(c) : « honnêtes appariés par action et commentaire ».** Un épisode honnête n'a pas, par définition, l'action fautive : cet appariement n'est pas défini.

6. **Expérience 4 : le critère « délibéré » est confondu avec la verbalisation.**
   - Juger « délibéré ou accidentel » repose sur le raisonnement. Pour une triche silencieuse (73 % chez anti-triche, CW §3.2, RAPPORTÉ), il n'y a pas de trace verbale : le caractère délibéré n'est pas identifiable sur la transcription.
   - Le critère favorise donc H_A pour le caractère le plus silencieux.
   - Ambiguïté supplémentaire : si les « tâches saines » n'offrent aucune occasion exploitable, la triche délibérée vaut 0 dans les deux bras par construction. Le contrôle négatif (« tâches sans occasion ») se confondrait alors avec la mesure.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **Expérience 1.**
  - Au niveau des distillations (6 unités), il y a 6!/(2!)³ = 90 affectations, soit p_min = 1/90 ≈ 0,011 en unilatéral pour le contraste anti − neutre (calcul).
  - Avec une variance entre distillations estimée sur 1 degré de liberté par caractère, le quantile t à 97,5 % vaut 12,7. L'intervalle est quasi illimité dès que σ_distillation est du même ordre que l'effet.
  - Une permutation au niveau des exécutions ignore la corrélation intra-distillation : elle est invalide.

- **Expérience 2.** Si P(détection | mention insérée) → 1, le contraste se réduit à 1 − capture(silence), déjà connu. La perte n'est pas de puissance mais de validité.

- **Expérience 3.**
  - Si k strates passent chacune avec probabilité q, indépendamment, P(tout passe) = q^k.
  - Exemple (illustratif) : q = 0,95 et k = 36 (3 moniteurs × 3 caractères × 2 classes × 2 vues). P(tout passe) ≈ 0,16 (calcul).
  - Des instruments sains échouent donc environ 84 % du temps. Le critère est falsifié par construction quand les strates se multiplient.

- **Expérience 4.**
  - Pour détecter une baisse de moitié par le logarithme du rapport de taux (α bilatéral 0,05, puissance 0,8, approximation normale), il faut environ 49 événements dans le bras de référence (calcul).
  - Avec 1 000 épisodes par bras (illustratif, en partageant les 2 000 de D), le taux doit dépasser environ 5 %. Chez la graine 2, on compte 3 ou 4 triches délibérées sur 11 520 (RAPPORTÉ, décompte non réconcilié), soit environ 3·10⁻⁴ (calcul). Si les taux de référence sont de cet ordre, D4 est non jugeable.

### (c) Contrôles négatifs dont l'absence serait fatale

- **Expérience 1 :** permutation au niveau de la distillation, déclarée d'avance.
- **Expérience 2 :** épisodes honnêtes dont le raisonnement évoque une triche rejetée, et insertion contrefactuelle de cette mention dans des épisodes honnêtes. Si les fausses alertes montent autant que la capture, le moniteur réagit au mot, pas à l'acte.
- **Expérience 4 :** refaire le jugement délibéré/accidentel raisonnement masqué. Si les verdicts changent, le critère mesure la verbalisation.
- **T1 :** juge de silence aveugle aux verdicts des moniteurs.

---

## Sur la proposition E

### (a) Défauts de méthode

1. **E-A, réplication de la distillation.**
   - Points solides : capture non conditionnelle publiée, refus de la pseudo-réplication.
   - Le nombre de points de départ par caractère n'est pas fixé dans E-A ; les 36 entraînements n'apparaissent que dans le budget. La puissance n'est donc pas définie.
   - La standardisation « sur classes de faute » se heurte à T2.
   - Le contrôle (« points de départ neutres comparés entre eux ») n'estime la variance qu'au sein de neutre. Or anti-triche est vraisemblablement bimodal (une graine sur trois résiste, RAPPORTÉ ; bimodalité = HYPOTHÈSE). La variance du neutre la sous-estimerait alors, et un contraste de moyennes masque ce mélange.

2. **E-B, familles contrefactuelles.**
   - Même défaut que D2. La variante « mention explicite » sature la détection (T1) : franchir 10 points est quasi acquis.
   - L'affirmation « confirme ou tue l'interprétation causale » va trop loin. Ce qui est testé, c'est la réponse du moniteur à une retouche de texte, pas le fait que la politique devenue silencieuse cause les ratés.
   - Les épisodes francs sont surtout hors de la classe réécriture (T2). Les familles de cette classe seraient donc majoritairement synthétiques, et la variante « absence de mention » obtenue par retrait sort de la distribution.

3. **E-C, calibration par caractère.**
   - Même défaut de composition que C4 d'A : le réservoir honnête anti-triche se réduit à peu près à la graine 2.
   - Les partitions aléatoires ne reproduisent pas la structure graine × étape. Le contrôle doit stratifier par graine et par étape, sinon il est trop facile à passer.

4. **E-D, correcteur protégé.**
   - Si ce correcteur bloque par construction la classe « modification des tests », la baisse de 10 points ou plus est **vraie par construction** chez anti-triche, qui triche presque uniquement par cette classe (RAPPORTÉ).
   - L'expérience n'informe que sur la classe « sans toucher aux tests ».
   - « Le même oracle indépendant » est ambigu. S'il coïncide avec le correcteur de la branche protégée, cette branche a été optimisée contre l'évaluateur : c'est une **fuite**.

5. **Tableau des instruments : appariement « en compétence ».** La compétence est mesurée après traitement et peut dépendre de l'entraînement à tricher. Apparier dessus revient à conditionner sur un médiateur.

6. **Règle « intervalle d'un côté, sinon indécis ».** Elle est correcte, mais l'issue « indécis » ne falsifie rien (B4). Elle n'est acceptable que si l'effectif est fixé d'avance pour borner P(indécis), ce qu'E ne fait pas.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **E-A.**
  - Avec J points de départ par caractère, le contraste est jugeable seulement si 10 points dépassent environ t_{J−1}·σ_J·√(2/J), où σ_J est l'écart-type entre distillations.
  - Pour un point de départ qui résiste, la capture est indéfinie (dénominateur nul). Ces données manquent de façon non aléatoire, sauf si l'on adopte la quantité non conditionnelle de T3.

- **E-B.** Près du plafond, presque toutes les paires deviennent discordantes dans le même sens. Le test est trivialement significatif : c'est une perte de validité, pas de puissance.

- **E-C.**
  - Il faut environ 753 épisodes honnêtes hors calibration par caractère et par moniteur pour ± 1 point au seuil de 2 % (calcul, voir A).
  - L'écart-type de la différence de capture dépend du nombre de triches anti-triche, qui proviennent de deux graines seulement : la corrélation intra-graine réduit n_eff (formule de l'effet de plan donnée pour C2).

- **E-D.**
  - Non jugeable si le taux de faute de la branche originale p₀ est inférieur à 10 points.
  - Trivial si p₀ ≈ 0,83–0,91 (RAPPORTÉ) est dominé par la classe que le correcteur protégé bloque.

### (c) Contrôles négatifs dont l'absence serait fatale

- **E-D :** un oracle d'évaluation disjoint du correcteur d'entraînement, et une analyse séparée de la classe « sans toucher aux tests ».
- **E-C :** des partitions aléatoires stratifiées par graine et par étape.
- **E-B :** insérer une mention de triche *rejetée* dans des épisodes honnêtes. Le contrôle d'E (retouches de même longueur sans information de conformité) ne teste pas l'effet du vocabulaire de la triche sur les honnêtes.
- **T1 :** juge de silence aveugle aux moniteurs, comparé au détecteur lexical qu'E propose déjà.

---

**Ce qui ferait échouer cette critique :**
- T1 tombe si la catégorie « silencieuse » a été appliquée, après sa découverte, par un juge indépendant des moniteurs, sur toutes les trajectoires.
- T2 tombe si les figures 5 à 10, absentes du texte (CW §4), montrent assez de triches dans les cellules croisées.
- Mon point 1 sur A tombe si l'annotation de classe n'utilise pas l'altération des tests comme critère.

FIN-DE-CELLULE