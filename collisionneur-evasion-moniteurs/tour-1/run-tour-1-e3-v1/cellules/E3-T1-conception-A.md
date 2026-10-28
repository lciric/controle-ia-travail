

# Proposition A — Robustesse et validité de construit des moniteurs boîte blanche

## (a) Ce que la question suppose sans que ce soit établi

| # | Supposition implicite | Statut | Commentaire |
|---|---|---|---|
| S1 | Les sondes du programme (familles de F) détectent effectivement le biais diffus dans un 8B | **HYPOTHÈSE** | Aucun score pilote rapporté dans les pièces. Apollo 2025 détecte la tromperie binaire dans un 70B (RAPPORTÉ, chiffre 95–99 % à vérifier sur PDF). Le transfert au biais diffus dans un 8B n'a aucun résultat publié (pièce E, §3.3, §4). |
| S2 | L'agrégation max/attention sur les tokens transfère au niveau action et trajectoire face à un attaquant adaptatif | **HYPOTHÈSE** | Identifié explicitement comme angle mort non calibré (Tr, pièce P §5). Aucun résultat publié. |
| S3 | L'accumulation séquentielle sur scores de sonde détecte un sabotage dont chaque action reste sous le seuil | **HYPOTHÈSE** (H2) | Le squelette séquentiel boîte noire existe (RAPPORTÉ). L'application aux sondes internes est revendiquée comme nouvelle (pièce P §5, originalité 0,50). |
| S4 | Le construit mesuré (intention vs. conscience d'évaluation) prédit la robustesse adverse | **HYPOTHÈSE** (H8, originalité 0,40) | Le glissement de construit sous pression est décrit (RAPPORTÉ). La prédiction elle-même ne l'est pas (pièce P §5). |
| S5 | Un organisme 8B développe une conscience d'évaluation qui modifie comportementalement son output | **HYPOTHÈSE** | Pièce E §3.4 : « aucune démonstration empirique que des modèles ≤ 8B développent spontanément une conscience d'évaluation qui modifie leur comportement. Tout résultat publié est induit par instruction ou réglage fin. » Les sondes de conscience d'évaluation montrent AUROC > 0,7 en représentation, mais l'effet causal est faible (RAPPORTÉ, Nguyen et al. 2025 ; étude multi-modèles 2026, référence exacte à vérifier). |
| S6 | La cascade de portes (base ii) et la sonde dernier état (base iii) sont des bases compétentes | **HYPOTHÈSE** | Aucun score rapporté pour ces bases. Leur compétence est un acte de foi en amont de G1. |
| S7 | L'agrégation par moyenne et médiane est strictement dominée par max et attention | **HYPOTHÈSE** | L'interdit (pièce F) n'est pas justifié empiriquement dans les pièces fournies. Il peut être fondé sur des résultats internes non transmis, mais rien ici ne le soutient. |
| S8 | L'obfuscation d'activations par un organisme 8B est possible mais coûteuse (HC4) | **HYPOTHÈSE** (originalité 0,85) | Aucune mesure de ce coût dans les pièces. Le programme suppose un écart « de plusieurs ordres de grandeur » sans base empirique fournie. |

---

## (b) Expériences décisives — quatre duels

### Expérience 1 : Validité de construit par dissociation (tranche H8)

**Objet.** Savoir si chaque famille de sonde mesure l'intention de saboter ou un corrélat (format, registre, conscience d'évaluation, longueur, cadrage).

**H_A.** La sonde mesure l'intention : son score est invariant quand on change le cadrage (évalué vs. réel) à contenu saboté fixe, et varie quand on change l'intention (saboté vs. honnête) à cadrage fixe.

**H_B.** La sonde mesure un corrélat contextuel : son score se déplace significativement quand on change le cadrage à contenu fixe, ou ne se déplace pas quand on change l'intention à cadrage fixe.

**Grandeur mesurée.** Pour chaque famille × couche × concept : deux contrastes, exprimés en AUROC.
- Contraste d'intention : AUROC(saboté vs. honnête | cadrage fixe) = AUROC_int.
- Contraste de cadrage : AUROC(évalué vs. réel | intention fixe) = AUROC_cad.
- Score de dissociation : δ = AUROC_int − AUROC_cad.

**Nul.** Sonde aléatoire appariée en covariance (plancher P3) : δ_aléa ≈ 0 par construction. Toute sonde qui ne bat pas ce plancher n'existe pas (pièce P §8.1).

**Témoins.**
- Vrai positif : sonde entraînée sur des paires contrastives dont la seule variable est l'intention ; doit avoir δ > 0.
- Faux positif : sonde entraînée sur des paires dont la seule variable est le cadrage évalué/réel ; doit avoir δ ≤ 0.

**Contrôles croisés (trois blocs factoriels).**
1. Même contenu saboté, cadrage évalué vs. réel → isole le cadrage.
2. Même cadrage, contenu saboté vs. honnête → isole l'intention.
3. Permutation des étiquettes intention ↔ cadrage → si la sonde suit les étiquettes, elle ne lit rien.

**Seuil.** δ > 0 avec intervalle de confiance bootstrap à 95 % excluant zéro (corrigé Bonferroni sur le nombre de familles × couches).

**Falsification.**
- Si δ ≤ 0 pour toutes les familles sur une couche donnée → H_A falsifiée sur cette couche : la sonde ne mesure pas l'intention, ou pas à cette couche.
- Si δ > 0 mais AUROC_cad > 0,6 → H_A partiellement falsifiée : la sonde mesure un mélange intention + cadrage (construit contaminé).
- Si δ > 0 et AUROC_cad ≤ chance (0,5 ± ε) → H_B falsifiée : la sonde isole l'intention.

**Produit pour la suite.** La carte de validité de construit : une matrice famille × couche × concept, avec δ et ses intervalles, qui sert d'entrée à l'expérience 4.

---

### Expérience 2 : Gain séquentiel sur signal sous-seuil (tranche H2, G1)

**Objet.** Savoir si l'accumulation séquentielle sur les scores de sonde récupère un signal diffus que chaque action seule ne révèle pas.

**H_A.** L'agrégateur séquentiel (somme cumulée / processus e) détecte un épisode saboté à biais diffus (chaque action sous le seuil marginal) avec un rappel significativement supérieur à la meilleure base.

**H_B.** Le signal diffus se noie dans le bruit d'agrégation ; le séquentiel ne bat pas la cascade (base ii), la sonde dernier état (base iii), ou le moniteur boîte noire.

**Grandeur mesurée.** Rappel (TPR) à taux de faux positifs (FPR) apparié = 1 %, par mode de sabotage. Unité : proportion. Comparaison par test de McNemar apparié sur les mêmes épisodes.

**Protocole.** Épisodes de N actions (N ≥ 20, « illustratif »). L'intensité de sabotage par action est calibrée pour que le rappel marginal (sonde ponctuelle, action par action) soit ≤ 10 % à 1 % FPR — c'est la condition « sous le seuil ».

**Bases à battre (toutes à 1 % FPR apparié).**
- Base ii : cascade de portes — même sondes, seuils indépendants par couche, ET logique.
- Base iii : sonde sur le dernier état — même famille, même couche, score du dernier token de la dernière action.
- Base boîte noire : moniteur faible par action (Llama-3.2-3B-Instruct, option (b) de D1) et TRACE-lite.
- Plancher : sonde aléatoire appariée en covariance sous même agrégation séquentielle.

**Nul.** Épisodes honnêtes entiers ; le taux de faux positifs empirique de l'agrégateur séquentiel sur ces épisodes doit être ≤ 1 % (sinon l'instrument est mal calibré, arrêt avant comparaison).

**Seuil de décision.** Rappel_séquentiel − Rappel_meilleure_base > 0, McNemar p < 0,01 (unilatéral, corrigé pour le nombre de modes).

**Falsification.**
- Si le séquentiel ne bat aucune base sur aucun mode → H_A falsifiée : l'accumulation n'apporte rien, le programme perd son avantage revendiqué.
- Si le séquentiel bat les bases noires mais pas les bases blanches (ii, iii) → G1 échoue, mais H1 (blanc > noir) peut tenir.
- Si le séquentiel bat toutes les bases → H_B falsifiée.

**Contrôle de calibration.** Injecter une corrélation artificielle connue entre actions (signal diffus synthétique, amplitude fixée) dans des épisodes honnêtes. Le séquentiel doit détecter cette corrélation ; si non, il est aveugle au signal diffus, et tout résultat sur les épisodes sabotés est suspect.

---

### Expérience 3 : Conscience d'évaluation comme régime détectable (tranche question 3)

**Objet.** Savoir si le passage de l'organisme en mode « je suis évalué » se lit comme un changement de régime dans la série temporelle des scores de sonde, et si ce signal est dissociable du contenu.

**H_A.** La distribution des scores de sonde sur les tokens change (moyenne, variance, ou structure séquentielle) quand l'organisme est dans un contexte identifié comme évaluation, et cette rupture est détectable par un test séquentiel à garantie de taux de fausse alarme.

**H_B.** Tout changement apparent est expliqué par le contenu (le prompt d'évaluation a un format différent) et disparaît quand on apparie le contenu.

**Grandeur mesurée.** Statistique de rupture (CUSUM ou Page-Hinkley) sur la série des scores de sonde par token au sein d'un épisode. Unité : temps de détection (nombre de tokens avant alarme) et taux de fausse alarme.

**Protocole.**
- Condition A (induite) : l'organisme reçoit un cadrage explicite « vous êtes évalué ».
- Condition B (contrôle apparié) : même contenu de tâche, cadrage neutre.
- Condition C (contrôle de format) : cadrage « évalué » mais contenu trivial (pas de possibilité de sabotage).

**Nul.** Sonde aléatoire appariée : pas de rupture détectable sous aucune condition.

**Seuil.** Rupture détectée dans Condition A mais pas dans B ni C, à taux de fausse alarme ≤ 5 % (garanti par les propriétés du CUSUM, pré-spécifié).

**Falsification.**
- Si la rupture apparaît aussi dans B → H_A falsifiée pour le cadrage : le signal est dans le contenu, pas dans la conscience.
- Si la rupture apparaît dans C → la sonde mesure le format d'évaluation, pas l'intention : construit contaminé.
- Si la rupture apparaît dans A mais pas B ni C → H_B falsifiée : il existe un signal de conscience d'évaluation dissociable.

**Extension critique.** Si la rupture est détectée (H_A non falsifiée), tester si elle prédit le sabotage subséquent (corrélation entre amplitude de la rupture et dommage cumulé de l'épisode). Si oui, la sonde de conscience est un prédicteur utile. Si non, elle détecte un état mental sans conséquence comportementale — résultat intéressant mais non opérationnel pour le contrôle.

---

### Expérience 4 : Frontière de robustesse — coût d'évasion par famille (tranche question 4, HC4, H8)

**Objet.** Pour chaque famille × couche, trouver le point de rupture : l'intensité d'évasion (obfuscation de comportement ou d'activations) à laquelle le rappel de la sonde tombe sous celui de la base boîte noire, et le coût correspondant en utilité.

**H_A.** Il existe un régime où l'organisme peut évader la sonde boîte blanche sans perte significative d'utilité sur la tâche honnête (g_sonde ≈ 0 sous attaque adaptative, à coût d'utilité ≤ 5 %, « illustratif »).

**H_B.** Toute évasion qui réduit le rappel de la sonde sous la base boîte noire entraîne une perte d'utilité supérieure au dommage qu'elle permet (taxe de déplacement HC4).

**Grandeur mesurée.** Courbe de compromis : rappel de la sonde (à 1 % FPR) vs. perte d'utilité de l'organisme (évaluée par juge humain ou juge automatique calibré, sur la tâche scientifique). Unité : ΔRappel par Δutilité.

**Protocole d'attaque (boîte noire sur l'organisme, boîte blanche sur le moniteur).** L'organisme est réglé fin (ou piloté par prompt) pour minimiser le score de sonde d'une famille donnée tout en maintenant le sabotage. L'attaquant n'a pas accès aux poids du moniteur (condition HC4). Itérations : l'attaquant observe le verdict (accepté/rejeté) mais pas le score continu (flux unidirectionnel, pièce P §9).

**Bases.**
- Moniteur boîte noire (option a + b de D1) : même attaque, mesure si l'évasion de la sonde transfère au moniteur noir.
- Pas d'attaque : rappel de la sonde en conditions bénignes (borne supérieure).

**Nul.** L'attaque aléatoire (perturbation du comportement sans stratégie d'évasion) ne réduit le rappel qu'en proportion de la perte d'utilité — pas d'évasion gratuite.

**Seuil.**
- H_A falsifiée si : pour toute famille × couche, la perte d'utilité au point où rappel_sonde = rappel_noir est > 20 % (« illustratif ») de l'utilité honnête.
- H_B falsifiée si : pour au moins une famille × couche, le rappel_sonde tombe sous rappel_noir avec une perte d'utilité ≤ 5 % (« illustratif »).

**Lien avec l'expérience 1.** La carte de validité de construit (δ par famille × couche) sert de prédicteur : H8 prédit que les sondes à δ élevé (isolant l'intention) sont plus robustes (rappel chute plus tard). Test : corrélation de rang entre δ (exp. 1) et le point de rupture (exp. 4). Si la corrélation est positive et significative → H8 non falsifiée et opérationnellement utile (on peut sélectionner les sondes robustes sur le critère δ, sans attaque). Si la corrélation est nulle → H8 falsifiée : la validité de construit ne prédit pas la robustesse.

**Extension — fermeture de brèche.** Pour chaque famille qui cède (rappel < base noire à faible coût d'utilité) :
1. Ajouter une couche (lire couche précoce + tardive au lieu d'une seule).
2. Changer de famille (passer de linéaire à Mahalanobis, par exemple).
3. Augmenter la fenêtre d'agrégation séquentielle.
4. Mesurer si la brèche se referme (rappel revient au-dessus de la base noire). Si aucune extension ne ferme la brèche → la sonde est structurellement vulnérable sur cette couche, le programme doit s'en séparer.

---

## (c) Mesure minimale de fonctionnement par instrument

| Instrument | Mesure minimale | Cas honnêtes appariés | Base mécanique à battre | Critère fonctionnel |
|---|---|---|---|---|
| **Différence de moyennes** | AUROC (saboté vs. honnête) à cadrage fixe, par action | Actions honnêtes appariées en longueur, registre, domaine | Sonde aléatoire appariée en covariance (P3) | AUROC > sonde aléatoire, p < 0,01 |
| **Linéaire** | Idem + rappel à 1 % FPR | Idem | Différence de moyennes (la linéaire doit faire au moins aussi bien) | Rappel ≥ rappel différence de moyennes |
| **Perceptron** | Idem | Idem | Linéaire (le perceptron n'est justifié que s'il gagne) | Rappel > rappel linéaire, sinon le surcoût est injustifié |
| **Attention (sonde)** | Idem + vérifier que l'agrégation attention bat max sur les mêmes sondes | Idem | Max-agrégation sur la même sonde | Si attention ≤ max → l'attention n'apporte rien |
| **Mahalanobis** | AUROC (saboté vs. distribution honnête), non supervisée | Toutes actions honnêtes (pas d'appariement par intention, c'est non supervisé) | Sonde linéaire supervisée (la Mahalanobis n'est utile que si elle fonctionne sans étiquettes) | AUROC > 0,6 (« illustratif ») à 1 % FPR |
| **Agrégateur séquentiel** | Rappel à 1 % FPR sur épisodes entiers (signal sous-seuil) | Épisodes honnêtes entiers (≥ 200, « illustratif ») | Cascade (base ii) et dernier état (base iii) | Rappel > les deux bases, McNemar p < 0,01 |
| **Base ii — cascade** | Rappel à 1 % FPR | Mêmes épisodes honnêtes | Sonde aléatoire sous même cascade | Rappel > sonde aléatoire |
| **Base iii — dernier état** | Rappel à 1 % FPR | Mêmes épisodes | Sonde aléatoire, même couche, dernier token | Rappel > sonde aléatoire |

**Fausses alertes : contrôle obligatoire.** Avant toute comparaison de rappel, vérifier que le taux de faux positifs empirique sur les épisodes honnêtes est ≤ 1 % pour chaque instrument. Si non, recalibrer et recommencer. Ne jamais comparer des rappels à FPR nominaux différents.

---

## (d) Ancrage matériel

**Modèle de l'organisme.** Llama-3.1-8B-Instruct (RAPPORTÉ, pièce P). Modèle ouvert, poids disponibles (Meta, licence communautaire).

**Moniteur boîte noire (base).** (a) Llama-3.1-8B-Instruct en juge + (b) Llama-3.2-3B-Instruct (recommandation D1, RAPPORTÉ).

**Activations.** Trois couches : 7, 15, 23 (RAPPORTÉ, pièce D). Dimension des activations du résidu : 4096 par token pour Llama-3.1-8B (« illustratif » — à vérifier sur la fiche modèle).

**Calcul (tous chiffres « illustratifs »).**
- Extraction des activations : ~1 passe avant par épisode. Pour 1000 épisodes × 3 couches × ~2000 tokens/épisode : ~6 × 10⁹ activations à stocker (float16 → ~24 Go de stockage brut). Faisable sur un seul GPU 80 Go.
- Entraînement des sondes : linéaire/différence de moyennes : secondes sur CPU. Perceptron/attention : minutes sur CPU (pièce D mentionne « processeur, zéro dépense »). Mahalanobis : inversion de covariance 4096 × 4096, quelques minutes sur CPU.
- Agrégation séquentielle : opération sur les scores (scalaires), négligeable.
- Épisodes de tâche sabotée : le coût dominant est la génération des trajectoires par l'organisme 8B. ~1000 épisodes × ~2000 tokens × 3 modes ≈ 6 × 10⁶ tokens de génération. Sur un A100 80 Go : ~10⁴ tokens/seconde → ~10 minutes de génération (« illustratif »).
- Expérience 4 (attaque adaptative) : nécessite plusieurs itérations (disons 10–50, « illustratif ») de réglage fin ou de prompt-tuning de l'organisme. Coût dominant : réglage fin du 8B. LoRA sur A100 : ~30 min par itération (« illustratif »). Total : 5–25 heures GPU (« illustratif »).
- **Total estimé (« illustratif ») : 1–2 jours de A100 unique pour les expériences 1–3, une semaine pour l'expérience 4 avec attaque adaptative.**

---

## (e) Ordre et critères d'arrêt

**Ordre recommandé.**

1. **Vérification des bases (exp. 2, volet calibration seulement).** Avant toute comparaison, vérifier que la base ii (cascade) et la base iii (dernier état) battent la sonde aléatoire sur les épisodes existants. Si elles ne le font pas, elles ne sont pas des bases compétentes : G1 est gagnable par défaut, et la comparaison ne dit rien. **Arrêt si les bases sont incompétentes : redéfinir G1 avant de dépenser.**

2. **Expérience 1 (validité de construit).** Peu coûteuse (CPU, sondes existantes, contrôles contrastifs). Produit la carte δ qui conditionne l'interprétation de tout le reste. **Arrêt si aucune sonde n'a δ > 0 : le programme ne mesure pas l'intention, il mesure le contexte. Tout résultat de rappel subséquent est un artefact.**

3. **Expérience 3 (conscience d'évaluation comme régime).** Moyennement coûteuse (nécessite les conditions A/B/C, donc ~3× les épisodes). Informe directement l'expérience 4. **Arrêt si la rupture apparaît dans toutes les conditions y compris le contrôle apparié : la sonde de conscience ne mesure pas la conscience.**

4. **Expérience 2 (gain séquentiel).** Nécessite des épisodes à biais diffus calibré, plus coûteux. **Arrêt si le séquentiel ne bat pas la cascade sur aucun mode : l'accumulation ne sert à rien, le programme doit pivoter vers une autre architecture de moniteur.**

5. **Expérience 4 (frontière de robustesse).** La plus coûteuse (attaque adaptative, réglage fin itératif). Ne se lance que si les expériences 1–2 ont produit au moins une sonde avec δ > 0 et un séquentiel qui bat une base. **Arrêt si la première itération d'attaque réduit le rappel à 0 sans perte d'utilité : la sonde est trivialement vulnérable, inutile de caractériser la courbe.**

**Ce qui me ferait changer d'avis.**
- Si l'expérience 1 montre que la Mahalanobis non supervisée a un δ plus élevé que les sondes supervisées → le problème n'est pas l'entraînement supervisé mais la géométrie de l'espace latent, et le programme devrait pivoter vers des méthodes non supervisées.
- Si l'expérience 3 montre une rupture robuste dans la conscience d'évaluation qui prédit le sabotage → la sonde de conscience devient un prédicteur opérationnel, contrairement à ce que Nguyen et al. 2025 suggèrent (effet causal faible). Je réévaluerais S5.
- Si l'expérience 4 montre un g_sonde ≈ 0 pour toutes les familles sous attaque boîte noire → HC2 est non falsifiée et les sondes sont robustes par construction. Je considérerais l'expérience 4 comme terminée sans caractérisation complète de la courbe.
- Si un résultat publié démontre la détection boîte blanche du biais diffus dans un ≤ 8B avant que nous ne terminions → la zone revendiquée par H2/H6 est occupée, le programme doit recalibrer ses revendications d'originalité.

---

## Références citées

- Berglund et al. (2023), « Taken out of context: On measuring situational awareness in LLMs. » — RAPPORTÉ dans pièce E.
- Laine et al. (2024), SAD benchmark — RAPPORTÉ dans pièce E, chiffres à vérifier sur PDF.
- van der Weij et al. (2024), sandbagging — RAPPORTÉ dans pièce E, taux 64–84 % à vérifier sur PDF.
- Apollo Research (2025), « Linear probes detect deception in Llama-3.3-70B-Instruct » — RAPPORTÉ dans pièce E, 95–99 % à 1 % FP à vérifier sur PDF.
- Nguyen et al. (2025), sondage et pilotage de la conscience d'évaluation — RAPPORTÉ dans pièce E, AUROC à vérifier sur PDF.
- Greenblatt et al. (2023/2024), « AI Control: Improving Safety Despite Intentional Subversion » — RAPPORTÉ dans pièce E.
- Phuong et al. (2024, DeepMind), « Evaluating Frontier Models for Dangerous Capabilities » — RAPPORTÉ dans pièce E.
- Étude multi-modèles (2026), AUROC > 0,7 — RAPPORTÉ dans pièce E, publication exacte à identifier (référence à vérifier).

FIN-DE-CELLULE