# Proposition A — Tour III.1 : réécrire sa structure ou apprendre dedans

**Statut global.** Le bloc FAITS est présent mais vide par décision de l'arbitre : tout ce qui suit est HYPOTHÈSE, sauf mention contraire. Rien de B ni de C n'est visible à ce tour (conception à l'aveugle) : il n'y a rien à attaquer ni à emprunter ; B1 est respecté par défaut. Aucun chiffre ci-dessous ne vient des faits ; ils sont tous « illustratifs ».

---

## 0. Objets nommés (notation commune à tout le texte)

- Structure $S \in \mathcal{S}$ : code, rôles, boucles. État interne $\theta \in \Theta_S$ : mémoire, paramètres, instruments entraînés. Politique $\pi_{S,\theta}$.
- Familles de tâches $f \in \mathcal{F}$, chacune une distribution $D_f$ sur des paires $(x, y^*)$ munies d'un vérificateur mécanique $v_f(x,\hat y)\in\{0,1\}$ (test unitaire, égalité exacte, oracle numérique).
- Score $V(S,\theta,f)=\mathbb{E}_{D_f}[v_f]$. Plafond structurel $V^*(S,f)=\sup_{\theta\in\Theta_S}V(S,\theta,f)$, où $\Theta_S$ est l'ensemble des états atteignables *par apprentissage interne* sous budget fini. L'écart $V^*(S,f)-V(S,\theta,f)$ est le « reste apprenable » ; l'écart $\sup_{S'}V^*(S',f)-V^*(S,f)$ est le « reste structurel ».
- Courbe d'apprentissage interne $L_S(b)$ : score après dépense $b$ en apprentissage interne ; pente $\ell_S(b)$.
- Coût de réécriture $c_r = b_r + \Delta_{\text{trans}} + p_{\text{reg}}\cdot \Delta_{\text{reg}}$ : budget consommé, perte transitoire, probabilité et ampleur d'une régression.
- Nouveauté $\nu_t$ : divergence entre le flux récent et les familles de conception. Stabilité $\sigma_t$ : variance du score sous rééchantillonnage et paraphrase, **conditionnée à la correction** (une réponse toujours fausse est stable).
- Budget total $B = B_0 + B_u + B_r$ (conception, usage, re-conception).

---

## (a) Ce que la question suppose sans l'établir

| # | Présupposé | Statut | Pourquoi ce n'est pas établi |
|---|---|---|---|
| 1 | La dichotomie structure / intérieur est nette. | HYPOTHÈSE | Une mémoire qui stocke des fragments de code exécutés plus tard, ou des instruments entraînés qui routent les appels, modifient de fait les boucles sans « toucher au code ». La frontière est un choix de conception, pas un fait. |
| 2 | L'organisme observe ses scores sur des tâches à vérité connue sans les contaminer. | HYPOTHÈSE | S'il apprend dedans, il peut mémoriser les items ; s'il se réécrit, il peut modifier le harnais. Le scellement externe est une condition, pas un donné. |
| 3 | Appels, dollars et temps sont fongibles en un seul budget. | HYPOTHÈSE | Ils ne le sont pas toujours (latence incompressible, plafonds de débit). Le découpage du point 3 dépend de la devise retenue. |
| 4 | « Nouveauté des questions » est mesurable depuis l'intérieur. | HYPOTHÈSE | Une famille jamais vue peut être superficiellement proche d'une famille vue, et réciproquement ; toute mesure de nouveauté est elle-même un instrument faillible (voir (c)). |
| 5 | Réécrire coûte plus et risque plus qu'apprendre dedans. | HYPOTHÈSE | Plausible, mais c'est la quantité à mesurer, pas une prémisse ; certaines réécritures (supprimer une boucle) sont quasi gratuites. |
| 6 | Le flux de questions est descriptible par des familles stationnaires. | HYPOTHÈSE | Si le flux dérive continûment, « hors famille » n'a pas de sens discret ; les expériences ci-dessous doivent inclure une condition de dérive. |
| 7 | Les résultats de l'apprentissage continu sur réseaux de neurones se transportent aux organismes faits d'appels à des modèles. | HYPOTHÈSE | La littérature citée en §5 porte sur des paramètres différentiables ; la mémoire textuelle et les rôles n'ont pas les mêmes mécanismes d'interférence. |
| 8 | Une structure figée après conception est le régime par défaut à vérifier (point 4). | HYPOTHÈSE | C'est un choix de protocole ; rien ne dit que le régime figé est la bonne base de comparaison plutôt que le régime « apprentissage interne seul ». |

---

## 1. Critère de décision (point 1) : trois voies, et ce que chacune ignore

Je refuse de donner « le » critère ; voici trois formes évaluables par programme, qui ne mesurent pas la même chose.

**Voie 1 — règle de pente (saturation interne).** Réécrire si, sur une fenêtre de $W$ dépenses internes,
$$\hat\ell_S(b)\cdot(B-b) \;<\; \hat g_r - \hat c_r \quad\text{et}\quad V_{\text{cible}} - V(S,\theta) > \tau_g,$$
c'est-à-dire si le gain interne extrapolé sur le budget restant est inférieur au gain de réécriture espéré net de son coût, et si l'écart à la cible reste grand. Objets : régression de $L_S$ sur les $W$ derniers points, intervalle de confiance sur $\hat\ell_S$. **Ce qu'elle ignore :** les plateaux qui cèdent (gains tardifs non linéaires), le fait que $\hat g_r$ est inconnu avant d'avoir réécrit, et que $V_{\text{cible}}$ peut être inatteignable par toute structure.

**Voie 2 — règle d'écart de généralisation (nouveauté).** Réécrire si l'écart $V(\text{familles vues}) - V(\text{familles récentes})$ dépasse $\delta$ **et** que $k$ lots d'apprentissage interne sur les familles récentes ne réduisent pas cet écart de plus de $\delta/2$. Objets : estimateur de $\nu_t$ (test à deux échantillons par classifieur entre flux récent et flux de conception ; ou écart entre erreur prédite par l'organisme et erreur réelle), et une différence de moyennes avec IC. **Ce qu'elle ignore :** l'existence d'une $S'$ meilleure (l'écart peut être structurel pour *toute* structure du budget), et le coût de $k$ lots « perdus » avant décision.

**Voie 3 — sonde contrefactuelle bornée.** Consacrer une fraction $\varepsilon$ du budget à faire tourner en bac à sable une structure candidate $S'$ sur un jeu scellé, et réécrire si $\hat V(S')-\hat V(S) > \tau_{\varepsilon}$ avec IC excluant 0. Objets : test apparié sur items identiques, correction pour comparaisons multiples si plusieurs candidats. **Ce qu'elle ignore :** la non-stationnarité (la sonde mesure le passé), le biais de sélection (choisir $S'$ parce qu'elle est bonne sur le jeu scellé contamine le jeu scellé pour la suite), et le coût $\varepsilon B$ lui-même.

**Réciproque (quand apprendre dedans).** Apprendre dedans tant que $\hat\ell_S(b)$ est significativement positive (voie 1), tant que l'écart de généralisation se résorbe par lots (voie 2), ou tant que la sonde ne donne pas de candidat gagnant (voie 3). Les trois voies peuvent être contradictoires sur un même état : c'est précisément ce que les expériences de §4 doivent départager.

**À vérifier :** que $\hat\ell_S$ est un prédicteur du gain futur interne (corrélation entre pente estimée à $b$ et gain réalisé entre $b$ et $b+W$) ; que $\nu_t$ prédit l'échec sur le flux récent mieux qu'un prédicteur constant.

---

## 2. Quantités observables, coût, pièges (point 2)

| Quantité | Comment | Coût (illustratif) | Ce qui la rend trompeuse |
|---|---|---|---|
| $V(S,\theta,f)$ sur tâches à vérité connue | vérificateur mécanique, jeu **scellé hors de l'organisme**, items renouvelés par générateur à graine cachée | $n$ items × coût par item ; $n\approx 200$ pour un IC de ±3 points à 95 % (illustratif, binomial) | mémorisation des items (point 4) ; dilution si les items sont dans le pré-entraînement du modèle de base ; harnais modifiable par réécriture |
| Pente $\hat\ell_S$ | régression sur $W$ évaluations successives | $W\times$ coût d'évaluation | variance d'échantillonnage prise pour une tendance ; plateaux transitoires |
| Coûts | comptabilité des appels/tokens/secondes | nul si instrumenté | coûts différés (une réécriture qui reporte la dépense sur l'usage) ; devises non fongibles |
| Nouveauté $\nu_t$ | classifieur flux récent vs flux de conception ; ou écart erreur prédite/réelle | un petit modèle ou quelques appels par item | reformulation de surface prise pour nouveauté ; nouveauté réelle sous surface familière |
| Stabilité $\sigma_t$ | $m$ rééchantillonnages + paraphrases par item, variance conditionnée à $v_f=1$ | $m\times$ ; $m\approx 5$ illustratif | stabilité d'un échec constant ; stabilité achetée par réponses dégénérées (refus, formules passe-partout) |

**La façade** (« mieux paraître sans mieux faire ») : signature observable = divergence entre le score auto-rapporté (ou le score sur un jeu accessible) et le score sur le jeu scellé. Je ne décris pas comment elle se produit ; je décris ce qui la détecte : la corrélation entre gain auto-rapporté et gain scellé, par réécriture, et un contrôle « réécriture placebo » (voir §4, E1 et §5).

---

## 3. Découpage du budget (point 3) : trois régimes à départager

- **R-fixe.** $(B_0,B_u,B_r)$ fixés par l'humain. Coûte : la mauvaise allocation quand le flux diffère de ce qu'on croyait ; fait perdre : toute adaptation. Avantage : auditable, pas de boucle d'auto-financement.
- **R-borné.** L'organisme choisit dans des bornes : $B_r\le\rho B$, $B_u\ge\mu B$, et une réserve $r$ non dépensable en réécriture. Coûte : $\rho,\mu,r$ choisis à l'aveugle ; fait perdre : l'auditabilité partielle, risque de « procrastination structurelle » (réécrire jusqu'à la borne).
- **R-comptable.** Chaque réécriture emprunte sur $B_r$ ; si le gain scellé mesuré sur la fenêtre suivante ne couvre pas $c_r$, la part de $B_r$ encore disponible est réduite multiplicativement (objet : processus de crédit avec facteur $\gamma<1$). Coûte : un évaluateur scellé et un délai de mesure ; fait perdre : les réécritures dont le gain est lointain.

**Par qui :** dans les trois régimes, le scellement et les bornes extérieures sont humains ; seul R-fixe ne laisse rien à l'organisme. Ce qui les départage est l'expérience E2 (§4), pas un argument.

**À vérifier :** l'ordre de grandeur de $B_0$ par rapport à $B$ change-t-il le classement des régimes ? (illustratif : tester $B_0/B\in\{0{,}1;\,0{,}3;\,0{,}5\}$).

---

## 4. Expériences décisives (b), sous inférence forte

Toutes partagent : familles de conception $\mathcal{F}_c$ (vues), familles scellées $\mathcal{F}_s$ (jamais vues, générateur à graine détenue par Lazar), ≥5 graines par cellule, vérificateurs mécaniques uniquement, structure et harnais d'évaluation dans des processus séparés.

### E1 — Saturation ou nouveauté : qu'est-ce qui prédit le gain de réécriture ?
- **H_A :** le gain net d'une réécriture est prédit par la saturation interne ($\hat\ell_S\approx 0$), pas par $\nu_t$.
- **H_B :** il est prédit par la nouveauté du flux, pas par la pente.
- **Dispositif :** plan factoriel 2×2 (plateau atteint / non) × (flux nouveau / familier), chaque cellule avec deux bras : *réécrire* (voie 3 : un candidat $S'$ produit par l'organisme) ou *continuer* (apprentissage interne de même coût).
- **Métrique :** $\Delta = V_s(\text{réécrire}) - V_s(\text{continuer})$ sur $\mathcal{F}_s$ après dépense égale.
- **Seuil (illustratif) :** $|\Delta|\ge 5$ points avec IC 95 % excluant 0 sur ≥5 graines.
- **Contrôle négatif :** « réécriture placebo » — reformatage du code sans changement sémantique (vérifié par tests d'équivalence). Doit donner $\Delta\approx 0$ ; sinon la mesure est bruitée ou le harnais fuit, et E1 est invalidée avant interprétation.
- **Issues :** $\Delta>0$ seulement dans les cellules « plateau » → H_B falsifiée. $\Delta>0$ seulement dans les cellules « nouveau » → H_A falsifiée. $\Delta>0$ dans les deux ou dans aucune → les deux falsifiées comme explications seules ; on passe à un modèle d'interaction (et la voie 1 et la voie 2 sont toutes deux insuffisantes).

### E2 — Régime de budget : fixe ou auto-alloué borné ?
- **H_A :** R-fixe atteint un $V_s$ final supérieur ou égal à R-borné et R-comptable quand le flux reste dans $\mathcal{F}_c$ **et** quand il dérive.
- **H_B :** R-borné ou R-comptable dépasse R-fixe d'au moins $\tau$ sous dérive, sans perte sous flux stable.
- **Dispositif :** 3 régimes × 2 conditions de flux (stable / dérive progressive vers $\mathcal{F}_s$) × ≥5 graines ; même $B$.
- **Métrique :** $V_s$ final ; secondaire : budget réellement consommé en réécriture.
- **Seuil (illustratif) :** $\tau=5$ points, IC excluant 0.
- **Contrôle négatif :** organisme à $B_r=0$ (réécriture interdite). Si ce contrôle égale les trois régimes, la réécriture n'a aucun effet mesurable dans ce dispositif et E2 ne tranche rien sur les régimes — il faut d'abord augmenter la puissance ou la dérive.
- **Issues :** R-fixe ≥ les autres partout → H_B falsifiée. R-borné/comptable > R-fixe sous dérive sans perte en stable → H_A falsifiée. R-borné/comptable > sous dérive mais < en stable → les deux falsifiées telles quelles ; le résultat est un compromis dépendant du flux, et ce sont $\rho,\mu,\gamma$ qu'il faut balayer.

### E3 — Compétence ou mémoire sur familles vues (point 4)
- **H_A :** le score de la structure figée sur $\mathcal{F}_c$ est invariant aux perturbations de surface (reformulation, renommage, permutation d'ordre) : compétence.
- **H_B :** il chute d'au moins $\delta$ sous perturbation : mémoire des items.
- **Métrique :** $V(\mathcal{F}_c) - V(\mathcal{F}_c^{\text{perturbé}})$, items appariés.
- **Seuil (illustratif) :** $\delta = 10$ points.
- **Contrôle négatif :** le modèle de base nu, jamais exposé à $\mathcal{F}_c$ : sa chute sous perturbation mesure la fragilité intrinsèque à la perturbation elle-même ; on soustrait cette chute. Second contrôle : test de restitution — proportion d'items de $\mathcal{F}_c$ que l'organisme reproduit mot pour mot sur consigne neutre ; une restitution élevée est un marqueur de mémoire indépendant de la perturbation.
- **Issues :** chute corrigée $<\delta$ et restitution basse → H_B falsifiée. Chute $\ge\delta$ ou restitution haute → H_A falsifiée. Chute faible mais restitution haute → mémoire *et* compétence coexistent ; la distinction binaire de la question est falsifiée.

### E4 — La façade est-elle détectable ?
- **H_A :** le gain auto-rapporté par l'organisme après réécriture prédit le gain scellé ($r \ge 0{,}6$, illustratif).
- **H_B :** il ne le prédit pas ($r$ dont l'IC inclut 0).
- **Contrôle négatif :** réécriture placebo (gain auto-rapporté doit être $\approx 0$ ; s'il est positif, l'auto-rapport est biaisé par la seule occurrence d'une réécriture).
- **Issues :** $r$ élevé → H_B falsifiée, l'auto-rapport est un observable utilisable. $r$ faible → H_A falsifiée, et toute voie de décision fondée sur l'auto-évaluation (y compris la voie 3 si la sonde n'est pas scellée) est disqualifiée.

---

## 5. Instruments nommés dans la question (c) : mesure minimale de fonctionnement

| Instrument | Taux de détection sur | Fausses alertes sur (cas honnêtes appariés) | Vérification mécanique à battre |
|---|---|---|---|
| **Détecteur de saturation** ($\hat\ell_S\approx0$) | plateaux construits (budget interne où le gain réalisé ensuite est $<1$ point) | montées lentes mais réelles (gain ensuite $\ge5$ points), appariées en score courant | régression linéaire sur les $W$ derniers points avec test de pente ; à battre en AUC sur les deux populations |
| **Détecteur de nouveauté** ($\nu_t$) | items de $\mathcal{F}_s$ | items de $\mathcal{F}_c$ paraphrasés ou renommés (même tâche, surface changée) | distance en plongement ou chevauchement de n-grammes avec seuil calibré ; à battre en AUC |
| **Détecteur de stabilité** ($\sigma_t$) | items où la correction varie sous rééchantillonnage | items constamment corrects, et items constamment faux (ne doit pas être « stable » au sens utile) | variance brute des sorties sans conditionnement à $v_f$ ; à battre en séparant les deux cas d'échec |
| **Détecteur de façade** (auto-rapport vs scellé) | réécritures dont le gain scellé est $\le0$ alors que le gain auto-rapporté est $>0$ | réécritures avec gain scellé $>0$ et auto-rapport concordant | comparaison directe score auto-rapporté / score scellé par seuil ; à battre en taux de fausses alertes à détection égale |
| **Discriminateur mémoire/compétence** (E3) | structures entraînées sur items exacts de $\mathcal{F}_c$ | structures entraînées sur $\mathcal{F}_c$ avec items régénérés à chaque exposition | test de restitution seul ; à battre en détection à fausses alertes égales |

Critère de fonctionnement minimal (illustratif) : détection $\ge0{,}8$ et fausses alertes $\le0{,}2$ sur ≥100 cas par population, et amélioration significative sur la vérification mécanique correspondante. Un instrument qui ne bat pas sa vérification mécanique est remplacé par elle.

---

## 6. Ancrage matériel (d) — tout illustratif

- **Modèles ouverts** (RAPPORTÉ, connaissance de pré-entraînement, à vérifier à la date du tour) : familles Llama 3 (Meta, 2024), Qwen2.5 (Alibaba, 2024), Mistral 7B (Mistral AI, 2023), Gemma 2 (Google, 2024), DeepSeek-V3/R1 (DeepSeek, 2024–2025). Un modèle de 7–9 milliards de paramètres suffit pour E1–E4 si les familles sont calibrées pour que le score de base soit entre 0,3 et 0,7 (plage où un gain de 5 points est mesurable).
- **Familles** : générateurs procéduraux à graine (arithmétique modulaire, manipulation de chaînes, petits problèmes de contraintes, transformations de code vérifiées par tests), ce qui donne $v_f$ mécanique et des items frais à volonté.
- **Calcul** (illustratif) : un run = flux de 2 000 items × ~10 appels par item = 20 000 appels ; E1 (2×2×2 bras × 5 graines = 40 runs), E2 (3×2×5 + contrôle = 35 runs), E3 et E4 réutilisent les artefacts de E1–E2 : ~75 runs, ~1,5 M appels, ~3 milliards de tokens. Sur un seul accélérateur de 80 Go servant un modèle de 8 milliards à ~2 000 tokens/s : ~400 heures-GPU, soit ~1 000 à 2 000 USD en location, ou l'équivalent en API. Ces nombres ne viennent d'aucun fait.

---

## 7. Littérature (point 5) — uniquement ce que je peux attribuer ; toutes « à vérifier »

Apprentissage continu et interférence :
- McCloskey & Cohen (1989), *Catastrophic interference in connectionist networks: The sequential learning problem* — à vérifier.
- Kirkpatrick et al. (2017), *Overcoming catastrophic forgetting in neural networks* — à vérifier.
- Lopez-Paz & Ranzato (2017), *Gradient Episodic Memory for Continual Learning* — à vérifier.
- Parisi et al. (2019), *Continual lifelong learning with neural networks: A review* — à vérifier.

Méta-apprentissage :
- Schmidhuber (1987), *Evolutionary principles in self-referential learning* — à vérifier.
- Hochreiter, Younger & Conwell (2001), *Learning to learn using gradient descent* — à vérifier.
- Finn, Abbeel & Levine (2017), *Model-Agnostic Meta-Learning for Fast Adaptation of Deep Networks* — à vérifier.

Auto-modification de programmes et recherche de structures :
- Lenat (1983), *EURISKO: A program that learns new heuristics and domain concepts* — à vérifier.
- Koza (1992), *Genetic Programming: On the Programming of Computers by Means of Natural Selection* — à vérifier.
- Schmidhuber (2006/2007), *Gödel Machines: Fully Self-Referential Optimal Universal Self-Improvers* — à vérifier.
- Lehman & Stanley (2011), *Abandoning objectives: Evolution through the search for novelty alone* — à vérifier (pertinent pour ne pas faire de la diversité « la » réponse).
- Fernando et al. (2023), *Promptbreeder: Self-Referential Self-Improvement via Prompt Evolution* — à vérifier.
- Hu, Lu & Clune (2024), *Automated Design of Agentic Systems* — à vérifier.
- Zhang, Hu, Lu, Lange & Clune (2025), *Darwin Gödel Machine: Open-Ended Evolution of Self-Improving Agents* — à vérifier.

Apprentissage dans une structure contre changement de structure (origine du cadre) :
- Baldwin (1896), *A new factor in evolution* — à vérifier.
- Hinton & Nowlan (1987), *How learning can guide evolution* — à vérifier. C'est l'analogie la plus directe : l'apprentissage interne lisse le paysage que la recherche structurelle explore ; la question de l'arbitre est, formellement, celle de l'allocation entre les deux échelles.
- Holland (1975), *Adaptation in Natural and Artificial Systems* — à vérifier.
- Simon (1962), *The Architecture of Complexity* — à vérifier (quasi-décomposabilité : ce qui rend une réécriture locale possible sans tout casser).

Allocation séquentielle et mesures trompeuses :
- Gittins (1979), *Bandit processes and dynamic allocation indices* — à vérifier (la voie 1 est un bandit à deux bras non stationnaire ; l'indice de Gittins ne s'applique pas tel quel hors stationnarité, ce qui est à dire).
- Manheim & Garrabrant (2018), *Categorizing Variants of Goodhart's Law* — à vérifier (typologie des façades).
- Power et al. (2022), *Grokking: Generalization beyond overfitting on small algorithmic datasets* — à vérifier (exemple documenté de plateau qui cède, ce que la voie 1 ignore).
- Shinn et al. (2023), *Reflexion: Language agents with verbal reinforcement learning* — à vérifier (apprentissage interne par mémoire textuelle, sans changement de code).

Ce que cette littérature **ne** couvre pas, à ma connaissance (HYPOTHÈSE) : une comparaison contrôlée, à budget égal et sur familles scellées, entre réécriture de structure et apprentissage interne pour des organismes composés d'appels à des modèles de langage. C'est le vide que E1–E2 visent.

---

## 8. Ce qui peut être réfuté ici

- Que la pente interne prédit le gain de réécriture (E1).
- Que la nouveauté le prédit (E1).
- Qu'un régime de budget domine l'autre indépendamment du flux (E2).
- Que la distinction mémoire/compétence est binaire (E3).
- Que l'auto-rapport est un observable utilisable (E4).
- Que chacun des cinq instruments bat sa vérification mécanique (§5).

Aucune de ces propositions n'est présentée comme un résultat.

FIN-DE-CELLULE