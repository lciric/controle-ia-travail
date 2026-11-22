# Proposition B — Tour III.1 : conception ciblée

**Pièces reçues.** Le bloc FAITS ne contient que l'énoncé de la question. Il est identique au bloc QUESTION, avec la même empreinte annoncée, et ne transmet aucun fait empirique. Je n'ai pas recalculé les empreintes sha256, car les octets exacts ne sont pas reproductibles depuis le rendu. Je ne vois pas les propositions A, C, D, E et F à ce tour : je n'en critique ni n'en utilise aucune.

**Convention.** Tous les niveaux, seuils, tailles et coûts qui suivent sont **illustratifs**, sauf les constantes mathématiques.

---

## 0. Notation, et ce qu'une preuve suffit à trancher

- **Tirages** X₁, X₂, …, dans L(G) ou hors de L(G).
- **Vérificateur** V : objet → {1, 0, ⊥}, où ⊥ signifie « délai dépassé ».
- **Fréquence** p = P(V(X)=1).
- **Coûts unitaires** : c_g pour produire, c_v pour vérifier, avec r = c_v/c_g.
- **Risque** δ.

**R1 — VÉRIFIÉ (calcul).** Si les tirages sont i.i.d., P(aucun succès en n tirages) = (1−p)ⁿ ≤ e^{−pn}. Pour tout p ≥ p₀, n ≥ ln(1/δ)/p₀ suffit. Prix : n(c_g+c_v).

**R2 — VÉRIFIÉ.** Pour n fixé, sup_{p>0} (1−p)ⁿ = 1. Aucune garantie de succès dans un budget fini n'est uniforme en p inconnu. Toute garantie positive exige un p₀ ou une loi a priori sur p.

**R3 — VÉRIFIÉ (calcul).** Après n échecs i.i.d., p ≤ 1−δ^{1/n} ≤ ln(1/δ)/n au niveau 1−δ. Références RAPPORTÉES : Clopper & Pearson (1934), « The use of confidence or fiducial limits illustrated in the case of the binomial » ; Hanley & Lippman-Hand (1983), « If nothing goes wrong, is everything all right? Interpreting zero numerators ».
- C'est la seule garantie qu'on obtient sans hypothèse sur p, et elle est négative.
- Si l'arrêt dépend des données, il faut des intervalles valides à tout instant. RAPPORTÉ : Howard, Ramdas, McAuliffe & Sekhon (2021), « Time-uniform, nonparametric, nonasymptotic confidence sequences ».

**R4 — VÉRIFIÉ (méthode de Laplace).** Cas de tirages échangeables, c'est-à-dire i.i.d. sachant un P aléatoire (par exemple une population d'instances) :
- P(échec en n) = E[(1−P)ⁿ].
- Si P a une masse π₀ en 0 et une densité ~ c·p^{b−1} près de 0, alors P(échec en n) − π₀ ~ cΓ(b)·n^{−b}.
- Le budget pour descendre à π₀+ε croît alors comme ε^{−1/b}, et non comme ln(1/ε).

**R5 — VÉRIFIÉ (Bayes).** Soit α le taux de fausses acceptations de V et β son taux de faux rejets.
- La précision des acceptés vaut p(1−β)/[p(1−β)+(1−p)α].
- Elle n'est ≥ ½ que si α ≤ p(1−β)/(1−p).
- Quand p est petit, c'est donc α, et non le budget, qui borne la garantie.

**R6 — RAPPORTÉ.** Dagum, Karp, Luby & Ross (2000), « An optimal algorithm for Monte Carlo estimation ». Estimer p à erreur relative ε demande de l'ordre de ln(1/δ)/(ε²p) tirages vérifiés. Estimer p coûte donc environ 1/ε² fois plus que trouver un succès.

**R7 — VÉRIFIÉ (algèbre).** On place un filtre F avant V : coût c_f, taux de détection t, taux de fausses alertes f.
- Coût par succès confirmé sans filtre : (c_g+c_v)/p.
- Avec filtre : [c_g+c_f+c_v(tp+f(1−p))]/(tp).
- Le filtre fait gagner **si et seulement si** c_v(1−p)(t−f) > c_g(1−t)+c_f.
- Un filtre aléatoire (t = f) ne gagne jamais.

**R8 — VÉRIFIÉ (calcul).** Le décodage contraint par masquage, token par token, échantillonne ∏ₜ p(xₜ|x_{<t})/Zₜ(x_{<t}). Ce n'est pas p(x)/Z, la loi du modèle conditionnée à la grammaire. Les deux diffèrent dès que Zₜ dépend du préfixe. L'effet empirique de cet écart est RAPPORTÉ par Park, Wang, Berg-Kirkpatrick, Polikarpova & D'Antoni (2024), « Grammar-Aligned Decoding ».

R1 à R8 ne demandent pas d'expérience. Les duels de (b) portent sur ce qu'aucune preuve ne donne :
- la loi de P pour des générateurs réels ;
- la dépendance effective entre tirages ;
- t en fonction de p ;
- l'effet des méthodes sur p ;
- la stabilité de α.

---

## (a) Ce que la question suppose sans que ce soit établi

**S1. « Générateur aléatoire » et « la fréquence p ».** Cela suppose une loi stationnaire et des tirages i.i.d. ou échangeables. **HYPOTHÈSE** implicite. L'item 3 laisse la corrélation ouverte, mais p n'est défini que si la loi est fixe. Face à un générateur adaptatif ou adverse, p n'existe pas et R1 ne s'applique plus.

**S2. « On ne peut qu'obtenir des tirages ».** C'est un modèle d'accès sans probabilités : **HYPOTHÈSE** de cadrage. Or la grammaire est publique, donc l'expérimentateur peut toujours construire son propre échantillonneur uniforme ou un énumérateur. Références RAPPORTÉES : Flajolet, Zimmermann & Van Cutsem (1994), « A calculus for the random generation of labelled combinatorial structures » ; Duchon, Flajolet, Louchard & Schaeffer (2004), « Boltzmann samplers for the random generation of combinatorial structures ».
- Conséquence (VÉRIFIÉ, raisonnement) : une garantie revendiquée pour le générateur ne vaut que comparée à celle de cet échantillonneur de référence.
- Avec un modèle ouvert, les log-probabilités sont calculables par construction : « tirages seulement » est un choix, pas une contrainte.

**S3. Objets « écrits dans une grammaire ».** Cela suppose que le générateur ne sort que des mots de L(G), ou que les sorties hors grammaire se détectent pour un coût négligeable. **HYPOTHÈSE.** Rien n'assure qu'un modèle de langue non contraint la respecte ; le taux π de sorties acceptées par l'analyseur se mesure (c).

**S4. « Vérificateur indépendant ».** Trois sens ne sont pas distingués :
- (i) V est exact (α = β = 0) ;
- (ii) ses erreurs sont indépendantes de celles du générateur ;
- (iii) il est soustrait à l'optimisation, sans rétroaction.

**HYPOTHÈSE** dans chacun des trois sens. Par R5, le sens (i) pèse d'autant plus que p est petit. Le sens (iii) tombe dès qu'on entraîne ou qu'on sélectionne contre V.

**S5. « Dit si ».** Cela suppose que V termine et répond par oui ou non. **HYPOTHÈSE.** Le délai dépassé (⊥) est un troisième verdict, et le compter comme échec ou comme abstention change p.

**S6. « Coûteux ».** Cela suppose un coût fixe par objet. **HYPOTHÈSE.** Un négatif peut coûter un délai maximal, un positif une exécution complète : r n'est pas un scalaire.

**S7. Un seul p.** **HYPOTHÈSE.** p dépend du triplet (générateur, configuration d'échantillonnage, instance). Sur une population d'instances, P est aléatoire et c'est R4 qui remplace R1.

**S8. « Produits puis reconnus ».** L'objectif implicite est d'obtenir au moins un succès. **HYPOTHÈSE** sur l'objectif. Les autres objectifs ont des prix différents (R3, R6) : k succès distincts, couverture de toutes les solutions, estimation de p, certificat d'absence.

**S9. « Dans un budget donné ».** Cela présuppose qu'une garantie positive existe. R2 (VÉRIFIÉ) montre qu'il faut pour cela une information de plus, un p₀ ou un a priori ; la question le prévoit avec « s'il en est ». L'unité du budget n'est pas fixée : tirages, vérifications, argent ou temps.

**S10. « Taille de la grammaire ».** Le terme hésite entre le nombre de règles |G| et le nombre de mots de longueur ≤ ℓ, souvent exponentiel en ℓ. Seul le second entre dans p sous une loi uniforme. **HYPOTHÈSE** sur le sens visé.

**S11. « Puits étroits » (titre).** L'image suppose une structure de voisinage, avec des quasi-solutions autour des solutions. **HYPOTHÈSE.** Sans cette structure (régime « aiguille »), aucune stratégie de recherche sans répétition ne bat le tirage, en moyenne sur toutes les fonctions objectif. RAPPORTÉ : Wolpert & Macready (1997), « No free lunch theorems for optimization ».

**S12. « Méthodes répandues ».** Elles ne sont pas nommées. La liste testée en (c) est mon choix (**HYPOTHÈSE** de pertinence).

**S13. En-tête « orientée 0,55 avec contexte du dépôt, 0,40 sans ».** **RAPPORTÉ**, non audité. Ni l'échelle, ni l'échantillon, ni le devineur ne sont décrits ; je ne m'en sers pas.

---

## (b) Duels décisifs

Tout est pré-enregistré. Une issue qui ne tombe dans aucune des deux zones déclenche l'augmentation d'échantillon prévue, pas une interprétation.

### D1 — Tirages i.i.d. ou dépendants, dans les conditions réelles d'exécution

- **H_A** : pour une instance et une configuration fixées, les verdicts V(Xᵢ) sont i.i.d. Bernoulli(p), et R1/R3 s'appliquent.
- **H_B** : les conditions réelles d'exécution (graines, cache de préfixes, regroupement en lots, dérive du service) créent une dépendance qui fait sous-couvrir R3.
- **Protocole** :
  - 20 instances à p modéré.
  - Pour chacune, un échantillon de référence de 100·n tirages fixe p.
  - Puis 200 sous-échantillons de n tirages, collectés dans les conditions de production (lots, requêtes concurrentes).
- **Métriques** :
  - couverture empirique de l'intervalle de Clopper–Pearson à 95 % ;
  - indice de dispersion des succès, par bloc de tirages consécutifs et par lot du serveur.
- **Seuil** : H_A est rejetée si la couverture est < 0,93, ou si la dispersion est significative à 1 % après correction de Holm.
- **Contrôle négatif** :
  - les mêmes verdicts permutés au hasard, ce qui détruit l'ordre ; le test doit y rejeter au taux nominal ;
  - un générateur Bernoulli pseudo-aléatoire de même p.
- **Contrôle positif** : une chaîne de Markov à deux états, de marginale p et de corrélation ρ = 0,2. Sans puissance ≥ 0,8 sur ce contrôle, pas de conclusion.
- **Issue qui falsifie H_A** : sous-couverture sur les tirages réels, absente sur les tirages permutés. R1 et R3 ne valent alors pas pour ce générateur tel qu'il est servi, et il faut raisonner en nombre effectif de tirages.
- **Issue qui falsifie H_B** : couverture ≥ 0,93 et dispersion non significative, alors que le contrôle positif est détecté. Une éventuelle dépendance reste alors < ρ.

### D2 — Population : décroissance exponentielle ou loi de puissance

On note U(k) la fraction d'instances non résolues après k tirages.

- **H_A** : sur les instances résolubles, P est minoré par un p₀ > 0, donc U(k) − π₀ décroît exponentiellement.
- **H_B** : P a une densité ~ c·p^{b−1} près de 0, donc U(k) − π₀ ~ C·k^{−b} (R4).
  - RAPPORTÉ : Brown et al. (2024), « Large Language Monkeys: Scaling Inference Compute with Repeated Sampling », observent une couverture qui croît avec k sur plusieurs ordres de grandeur.
  - RAPPORTÉ : Schaeffer et al. (2025), « How Do Large Language Monkeys Get Their Power (Laws)? », attribuent la loi de puissance agrégée à la queue de la loi des probabilités de succès par problème près de 0.
- **Protocole** :
  - 300 instances, 2 000 tirages vérifiés par instance.
  - U(k) est estimé par l'estimateur sans biais de pass@k de Chen et al. (2021), « Evaluating Large Language Models Trained on Code ».
  - On ajuste les deux modèles sur k ≤ n/16 et on prédit U(n).
  - 30 instances, tenues à part, reçoivent 10·n tirages pour tester l'extrapolation.
- **Métriques** :
  - écart entre log U observé et log U prédit ;
  - log-vraisemblance hors échantillon : modèle bêta-binomial contre mélange à support minoré.
- **Seuil** : un modèle est rejeté si sa prédiction sort de l'intervalle bootstrap à 95 % de l'observation.
- **Contrôle négatif** : deux populations synthétiques dont la loi de P est connue (une bêta, une uniforme sur [p₀, 1]), passées dans le même pipeline au même n. Si la procédure ne retrouve pas le bon régime, le duel est déclaré non informatif à ce n.
- **Issue qui falsifie H_A** : U(n) au-dessus de la bande exponentielle. Il n'existe alors pas de budget logarithmique en 1/ε pour la population.
- **Issue qui falsifie H_B** : U(n) sous la bande de la loi de puissance.
- **Limite (VÉRIFIÉ, R3)** : au-delà de k ≈ n, π₀ et « p minuscule » ne se distinguent plus. Le duel ne tranche que sur la plage observée.

### D3 — Filtre bon marché : transférable ou aveugle aux puits

Le cadre est R7.

- **H_A** : t et f, mesurés sur des instances à p modéré, valent aussi pour p faible ; t reste constant à Δ près.
- **H_B** : t baisse avec p. Le filtre (modèle de récompense, juge LLM) reconnaît les succès typiques, pas les rares, au point d'inverser l'inégalité de R7 sous un seuil p*.
- **Protocole** :
  - Les instances sont réparties en strates selon le p̂ estimé en D2.
  - Dans chaque strate, **tous** les candidats passent par F et par V.
  - Le verdict de V sur ces mêmes candidats fournit les cas appariés. Ce coût est le prix de la mesure.
- **Métriques** :
  - t et f par strate ;
  - signe de c_v(1−p)(t−f) − c_g(1−t) − c_f, avec les coûts mesurés.
- **Seuil** : H_B est retenue si t(strate basse) < t(strate haute) − 0,2, avec un IC 95 % qui exclut 0, **et** si le signe s'inverse.
- **Contrôles négatifs** :
  - un filtre aléatoire au même taux de passage. R7 prédit une perte ; un gain mesuré signale une erreur de comptabilité ;
  - un filtre mécanique : analyse syntaxique, déduplication, compilation ou typage.
- **Issue qui falsifie H_A** : t chute avec p.
- **Issue qui falsifie H_B** : t reste plat, avec un IC de largeur < Δ.

### D4 — Décodage contraint par la grammaire, contre le rejet

On compare les coûts par succès confirmé.
- Décodage contraint : (c′_g + c_v)/p_GCD.
- Rejet : [(c_g + c_a)/π + c_v]/p_RS, où π est le taux de sorties libres acceptées par l'analyseur et c_a le coût de l'analyse.
- Quand c_v domine c′_g et (c_g+c_a)/π, la comparaison se réduit à p_GCD contre p_RS (VÉRIFIÉ, algèbre).

Les deux hypothèses :
- **H_A** : à r ≥ 100 (pré-enregistré), le décodage contraint coûte au plus autant par succès que le rejet.
- **H_B** : à ce r, il coûte plus, parce que p_GCD < p_RS (écart de R8).

Le protocole :
- **Bras de référence** : un échantillonnage conditionnel approché par Monte-Carlo séquentiel.
  - RAPPORTÉ : Lew, Zhi-Xuan, Grand & Mansinghka (2023), « Sequential Monte Carlo steering of large language models using probabilistic programs ».
  - Loula et al. (2025), « Syntactic and semantic control of large language models via sequential Monte Carlo » : référence à vérifier.
- **Métrique** : log du rapport des coûts par succès, par instance, avec un IC 95 % sur les instances. Les coûts sont mesurés séparément, ce qui permet de faire varier r par simple comptabilité.
- **Contrôle négatif** : une grammaire triviale, qui accepte toute sortie du modèle. L'écart attendu est nul.
- **Issue qui falsifie H_A** : le décodage contraint coûte plus au r pré-enregistré.
- **Issue qui falsifie H_B** : il coûte au plus autant que le rejet.

### D5 — Affinage sur le signal du vérificateur : support élargi ou rétréci

- **H_A** : pour toute instance où p_base > 0, p_affiné ≥ p_base.
- **H_B** : un ensemble non négligeable d'instances passe de p_base > 0 à p_affiné ≈ 0. RAPPORTÉ : Yue et al. (2025), « Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model? », observent que le modèle de base dépasse le modèle entraîné par RL en pass@k pour k grand.
- **Métrique** : nombre d'instances où la borne basse de Clopper–Pearson de p_base dépasse la borne haute de p_affiné, avec contrôle de Benjamini–Hochberg à 5 %.
- **Seuil** : H_B si ce nombre est > 0 après correction et dépasse 2 % des instances.
- **Contrôle négatif** : la base contre elle-même, sur deux jeux de tirages indépendants. Le décompte doit rester au niveau des fausses découvertes attendues.
- **Issue qui falsifie H_A** : des instances perdues de façon significative.
- **Issue qui falsifie H_B** : aucune instance perdue, avec une puissance de 0,8 pour détecter p divisé par 10 sur les instances où p_base ≥ 10/n.
- **Portée** : sous H_B, améliorer le générateur ne garantit rien sur les puits étroits, et il faut un portefeuille base + affiné.

### D6 — Vérificateur stable ou exploité sous pression de sélection

- **H_A** : α est le même sur les sorties sélectionnées sous pression (best-of-n via un proxy, générateur affiné contre V) que sur les tirages bruts.
- **H_B** : α croît avec la pression.
  - RAPPORTÉ : Gao, Schulman & Hilton (2023), « Scaling laws for reward model overoptimization », décrivent un phénomène analogue pour des modèles de récompense proxy.
  - Son extension à un vérificateur exécutable reste une HYPOTHÈSE.
- **Protocole** : un vérificateur de référence V*, plus fort et plus lent, est appliqué à un échantillon des sorties acceptées par V, pour n ∈ {1, 16, 256}.
- **Métrique** : α̂ = P(V*=0 | V=1) à chaque niveau de pression, et sa pente en fonction de log n.
- **Seuil** : pente > 0, avec un IC 95 % qui exclut 0.
- **Contrôle négatif** : un sous-ensemble aléatoire des acceptés, de même effectif, sans sélection.
- **Issue qui falsifie H_A** : une pente positive. Avec R5, la précision s'effondre dès que α atteint l'ordre de p.
- **Issue qui falsifie H_B** : une pente nulle avec un IC étroit.

---

## (c) Mesure minimale par instrument

| Instrument | Détection | Fausse alerte | Cas honnêtes appariés | Vérifications mécaniques à battre |
|---|---|---|---|---|
| Vérificateur V | 1−β = P(V=1 \| V*=1) | α = P(V=1 \| V*=0) ; exiger α ≪ p dans la strate visée (R5) | Paires (solution connue, mutant à une édition dont V* confirme l'échec), même longueur et même style ; plus les sorties brutes du générateur | V* ; tests par mutation ; sous-ensemble moins cher de V (s'il a le même α, V est surdimensionné) |
| Générateur | p_gen à budget égal ; rapport p_gen/p_unif pour plusieurs bornes de longueur ℓ | Taux de sorties hors grammaire ; doublons ; masse manquante de Good–Turing (Good 1953, « The population frequencies of species and the estimation of population parameters », RAPPORTÉ) | Mêmes instances, même distribution de longueurs | Échantillonneur uniforme sur L(G) (S2) ; énumération quand L_{≤ℓ} est petit |
| Grammaire / analyseur | Accepte les mots de L(G) | Accepte un mot hors de L(G) | Mots engendrés par G et mutants hors grammaire | Analyse différentielle par deux analyseurs indépendants |
| Diagnostic de dépendance (D1) | Rejette sous la dépendance implantée ρ | Rejette sur des verdicts permutés | Mêmes verdicts, ordre réel contre ordre permuté | Test des séquences (runs) classique |
| Bornes sur p (R3) | Couverture ≥ niveau nominal | Déclare p < p₀ alors que p ≥ p₀ | p de référence tiré d'un grand échantillon (D1) | Clopper–Pearson à n fixé ; séquences de confiance si l'arrêt est adaptatif |
| Filtre (modèle de récompense, juge LLM) | t par strate de p | f par strate | Mêmes candidats, verdict de V | Filtre aléatoire au même taux de passage ; analyse + déduplication + compilation |
| Vote majoritaire / auto-cohérence (Wang et al. 2023, « Self-consistency improves chain of thought reasoning in language models ») | Réponse retenue correcte | Réponse majoritaire fausse retenue | Instances dont la sortie se réduit à une valeur comparable | V appliqué aux m réponses distinctes les plus fréquentes, à nombre d'appels égal |
| Décodage contraint | p_GCD | Solutions que trouve le rejet et qu'il perd | Mêmes instances, mêmes prompts | Rejet + analyse ; SMC (D4) |
| Affinage / RL | Instances gagnées | Instances perdues (D5) | Mêmes instances, même k | Modèle de base à k égal |

**Remarque sur le vote (VÉRIFIÉ, raisonnement).** Si V est exact, toute sélection suivie de V a une précision de 1. Le vote ne peut donc qu'économiser des appels à V, et c'est cette économie, à rappel égal, qu'il faut mesurer. Deux résultats RAPPORTÉS vont dans ce sens :
- Brown et al. (2024) observent que la sélection par vote ou par modèle de récompense plafonne alors que la couverture continue de croître.
- Stroebl, Kapoor & Narayanan (2024), « Inference Scaling fLaws: The Limits of LLM Resampling with Imperfect Verifiers », rapportent que les faux positifs du vérificateur bornent le gain du ré-échantillonnage.

---

## (d) Ancrage matériel (tous les chiffres sont illustratifs)

**Bancs.**
1. **Synthétique.**
   - Une grammaire hors contexte publique, avec une propriété implantée à p réglable.
   - Une variante « aiguille », définie par un hachage à clé et sans structure, sert de contrôle négatif pour S11 et D3.
   - Le vérificateur est bon marché, et son coût est simulé en comptabilité pour balayer r.
2. **Code.**
   - HumanEval (Chen et al. 2021) et MBPP (Austin et al. 2021, « Program Synthesis with Large Language Models »).
   - V = les tests d'origine. V* = les tests étendus d'EvalPlus (Liu, Xia, Wang & Zhang 2023, « Is your code generated by ChatGPT really correct? Rigorous evaluation of large language models for code generation »).
   - Ce couple sert directement D6.
3. **Preuve.**
   - miniF2F (Zheng, Han & Polu 2022, « MiniF2F: a cross-system benchmark for formal Olympiad-level mathematics »), avec le noyau Lean 4 comme V.
   - Vérifications mécaniques obligatoires : rejet de `sorry`, liste des axiomes utilisés.
   - On s'attend à un α proche de 0 (HYPOTHÈSE, à confirmer par D6), ce qui mettrait D2 à D5 à l'abri de R5.

**Modèles ouverts.**
- Un modèle de code de 7 B paramètres et sa version 32 B de la même famille, par exemple Qwen2.5-Coder.
- Un prouveur Lean ouvert, par exemple DeepSeek-Prover-V1.5.
- Pour D5, une paire base / affiné-RL publiée par le même laboratoire. Si l'affiné a aussi reçu un SFT, ce facteur de confusion doit être déclaré.

**Logiciels.**
- Service : vLLM (Kwon et al. 2023, « Efficient memory management for large language model serving with PagedAttention »).
- Décodage contraint : Outlines (Willard & Louf 2023, « Efficient guided generation for large language models »).

**Volumes et coûts.**

| Poste | Hypothèses | Ordre de grandeur |
|---|---|---|
| Tirages | D1+D2 ≈ 8·10⁵ ; D3–D6 du même ordre | ≈ 1,6·10⁶ tirages × 400 tokens ≈ 6·10⁸ tokens |
| Génération, 7 B | 10⁴ tokens/s sur un H100, en lots | ≈ 17 GPU-heures |
| Génération, 32 B | ×4 | ≈ 70 GPU-heures |
| Coût de génération | 2 à 4 USD par GPU-heure | ≈ 35 à 350 USD |
| Vérification | Tests 0,1–1 s CPU ; Lean 1–30 s par tentative ; 10⁶ vérifications | 30 à 8 000 heures-cœur selon le banc |
| Coût de vérification | 0,02 à 0,05 USD par heure-cœur | ≤ ≈ 420 USD |
| **Total** | Hors audit humain | **Quelques centaines à environ 1 000 USD** |

La vérification domine le temps de calcul, ce qui place l'expérience dans le régime r grand visé par la question. Un audit humain de V* sur 200 sorties n'est nécessaire que si V* n'est pas mécanique.

---

## Ordre d'exécution, et ce qui reste hors de portée

**Ordre.**
1. **D1 d'abord.** Si H_A tombe, toutes les bornes des autres duels se recalculent avec un nombre effectif de tirages.
2. **D6 sur le banc code.** Si α n'est pas petit devant p, R5 invalide D2 à D5 sur ce banc.
3. **D2**, qui fournit les strates de D3.
4. **D3, D4, D5.**

**Ce que ces duels ne donnent pas.** Aucun ne fournit de garantie a priori pour une instance nouvelle et un générateur réel. Par R2, une telle garantie exige un p₀, que seule une hypothèse sur le générateur peut fournir. Les duels réfutent ou retiennent ces hypothèses ; ils ne les remplacent pas.

FIN-DE-CELLULE