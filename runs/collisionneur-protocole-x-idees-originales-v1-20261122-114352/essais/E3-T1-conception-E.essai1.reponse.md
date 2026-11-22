*Note d'intégrité (pièces transmises) : Les propositions A, B, C, D et F sont absentes (tour à l'aveugle), le bloc FAITS est strictement identique au bloc QUESTION DE L'ARBITRE sans jeu de données joint, et le document parent mentionné dans l'en-tête (« réponse 28 de Fable, section C7… réponse 05c72e05… ») n'est pas transmis au-delà de cet extrait.*

*Convention méthodologique : Conformément aux règles d'intégrité et à la consigne finale de la question, aucun chiffre empirique non sourcé n'est avancé comme résultat établi. Les seuils décisionnels et paramètres de dimensionnement requis pour rendre le protocole réfutable sont déduits de formules statistiques explicites ou de barèmes matériels publics, et systématiquement marqués `(illustratif)`. Les statuts épistémiques (`VÉRIFIÉ`, `RAPPORTÉ`, `OBSERVÉ-NON-AUDITÉ`, `HYPOTHÈSE`) demeurent invariants dans toute la cellule.*

---

## A. Présupposés non établis [Livrable (a)] et Reformulation du problème [Question 5]

### A.a. Ce que la question suppose sans que ce soit établi — Livrable (a)

L'énoncé contient l'affirmation explicite que l'on ignore si des appels indépendants reviennent aux mêmes idées (`VÉRIFIÉ` comme donnée de l'énoncé), mais repose sur plusieurs postulats implicites non démontrés :

* **P-alpha — Existence d'une équivalence intrinsèque entre « idées »** (`HYPOTHÈSE`) : Dire que des appels « reviennent aux mêmes idées » ou qu'une idée est « rarement proposée » suppose une relation d'équivalence $\sim$ sur les sorties textuelles. Sans projection déterministe vers un espace canonique ou comportemental, la rareté mesurée confond variation syntaxique de surface et originalité du mécanisme sous-jacent.
* **P-beta — Transférabilité hors-distribution de la fiabilité du contrôle indépendant** (`HYPOTHÈSE`) : L'énoncé pose que le contrôle est fiable sur des « cas d'essai dont la vérité est connue » (`VÉRIFIÉ` dans le cadre du problème) et traite implicitement la confirmation par ce contrôle dans la queue rare comme un gage de validité. Or, un vérificateur précis sur la distribution centrale des cas connus peut présenter un taux de faux positifs élevé dans les régions rares (« puits étroits »), où la sélection filtre précisément les failles du contrôle.
* **P-gamma — Décorrélation épistémique d'un système multi-modèles** (`HYPOTHÈSE`) : Des appels techniquement indépendants à plusieurs modèles de langue ne garantissent pas des erreurs ou des angles morts indépendants lorsque ces modèles partagent des corpus de pré-entraînement et des procédures d'alignement fortement recouvrants (`OBSERVÉ-NON-AUDITÉ` sur les familles ouvertes contemporaines).
* **P-delta — Couplage entre rareté générative et valeur du mécanisme** (`HYPOTHÈSE`) : Une idée rarement émise par le système et acceptée par le contrôle peut être triviale, inutilement complexe ou déjà connue hors du système (oubliée par l'alignement plutôt qu'originale dans le domaine).
* **P-epsilon — Neutralité de la structure de coût** (`HYPOTHÈSE`) : Raisonner « à coût total égal » sans séparer le coût marginal de génération $c_{\text{gen}}$ du coût marginal du contrôle indépendant $c_{\text{ver}}$ masque deux régimes opposés selon le rapport $c_{\text{ver}} / c_{\text{gen}}$.

### A.b. Pourquoi le problème est partiellement mal posé et comment le reposer — Question 5

Le problème tel que formulé est sous-déterminé sur trois points critiques :
* Premièrement, la notion de « même idée » n'est pas munie d'un morphisme d'observation calculable hors-modèle.
* Deuxièmement, exiger simultanément la *rareté* sous la loi du système et la *stabilité des fausses découvertes* via un contrôle calibré uniquement sur des cas connus confond le taux de faux positifs conditionnel à l'hypothèse nulle ($\alpha_V = P(V=1 \mid H_{\text{faux}})$) et le **taux de fausses découvertes** ($\text{FDR} = P(H_{\text{faux}} \mid V=1)$). Par inversion bayésienne (`VÉRIFIÉ` mathématiquement), si la proportion d'idées vraies $\pi(r)$ décroît lorsque la fréquence d'émission $r$ tend vers zéro, le $\text{FDR}$ augmente mécaniquement à contrôle $V$ inchangé.
* Troisièmement, un contrôle validé sur un ensemble fini de cas connus est vulnérable au sur-ajustement de sélection dès qu'on interroge massivement les queues de génération.

**Reformulation opératoire (`HYPOTHÈSE` de cadrage soumise au test) :**
> Soit un domaine muni : (i) d'un morphisme déterministe sans modèle $\phi : \mathcal{X} \to \mathcal{C}$ projetant chaque proposition brute $x$ sur une classe d'équivalence fonctionnelle $c = \phi(x)$ (coût $c_\phi$) ; (ii) d'un contrôle indépendant primaire $V$ (coût $c_{\text{ver}}$) et d'un protocole d'audit ou de second contrôle orthogonal sur sous-échantillon permettant de borner l'erreur hors-distribution ; (iii) d'une fonctionnelle d'utilité externe $U(c)$ évaluée sur données sous séquestre. À budget total fixé $B = N_{\text{gen}} c_{\text{gen}} + N_\phi c_\phi + N_{\text{ver}} c_{\text{ver}} + B_{\text{audit}}$, quelle politique d'échantillonnage et de filtrage maximise l'espérance du nombre de classes *distinctes* $c \in \mathcal{C}$ vérifiant à la fois $P_{\text{nominale}}(c) \le \tau$ (rareté sous la politique de référence) et $\Delta U(c) > \delta_U$ (valeur positive), sous la contrainte garantie $\text{FDR} \le q$ ?

---

## B. Mesures sans modèle [Question 1] et Calibration des instruments [Livrable (c)]

### B.a. Mesurer la rareté et la valeur sans se fier au jugement d'un modèle — Question 1

#### Mesure de la rareté sans modèle ($\phi$ + estimation de Good-Turing)
Toute mesure reposant sur des plongements neuronaux (*embeddings*) ou un LLM-juge réintroduit les angles morts représentationnels des modèles (`HYPOTHÈSE`). La mesure doit opérer en deux étapes déterministes :

* **Étape de quotient canonique $\phi(x)$ :**
  * *Domaine exécutable ou formel (mécanismes simulables, équations, stratégies, algorithmes)* : **Empreinte comportementale** (*phenotypic fingerprinting*). Chaque idée $x$ compilée en opérateur $f_x$ est évaluée sur un vecteur fixe d'entrées sondes canoniques $(z_1, \dots, z_m)$ couvrant le domaine : $\phi(x) = (f_x(z_1), \dots, f_x(z_m))$ après arrondi canonique ou réduction algébrique en forme normale. Deux formulations syntaxiquement disjointes produisant le même vecteur appartiennent à la même classe (`VÉRIFIÉ` par déterminisme de l'évaluation sur les sondes ; la complétude hors-sondes reste une `HYPOTHÈSE` contrôlée par la taille $m$).
  * *Domaine purement déclaratif non exécutable* : Projection des termes sur une ontologie fermée du domaine suivie d'un partitionnement hiérarchique par **distance de compression normalisée** $\text{NCD}(x, x') = \frac{Z(xx') - \min(Z(x), Z(x'))}{\max(Z(x), Z(x'))}$ calculée par un compresseur sans perte déterministe $Z$ (Li, Chen, Li, Ma et Vitányi, 2004, *The Similarity Metric* — `RAPPORTÉ` pour l'approximation pratique de la distance d'information normalisée).
* **Étape d'estimation fréquentiste de queue :** Sur $N$ appels i.i.d. à la politique nominale du système, soit $N_c$ le nombre d'occurrences de la classe $c = \phi(x)$ et $S_r$ le nombre de classes observées exactement $r$ fois. Pour les classes rares ($N_c$ faible), la fréquence brute $N_c / N$ surestime la probabilité des singletons observés et ignore la masse non vue (`VÉRIFIÉ` statistiquement). On utilise l'estimateur de **Good-Turing** lissé (Good, 1953, *The Population Frequencies of Species and the Estimation of Population Parameters* — `VÉRIFIÉ` pour l'identité d'espérance) :
  $$p_{\text{GT}}(c) = \frac{(r + 1) \, S_{r+1}}{N \, S_r} \quad (\text{pour } N_c = r), \qquad \hat{M}_0 = \frac{S_1}{N}$$
  où $\hat{M}_0$ estime directement la probabilité qu'un appel indépendant supplémentaire découvre une classe jamais observée jusque-là (répondant empiriquement à l'ignorance initiale sur le retour aux mêmes idées). La rareté objective d'une classe est alors sa surprenance $-\log p_{\text{GT}}(c)$ rapportée à la politique nominale figée.

#### Mesure de la valeur sans modèle ($\Delta U$ externe)
La valeur d'une classe confirmée $c$ ne doit jamais être estimée par sa rareté ni par un score linguistique, mais par son **gain marginal d'utilité externe** $\Delta U(c) = U(\mathcal{E}_0 \oplus c) - U(\mathcal{E}_0)$ par rapport à l'état de l'art mécanique $\mathcal{E}_0$ du domaine :
* *Valeur prédictive ou compressive* : Réduction de la **longueur de description minimale** (MDL) d'un jeu d'observations sous séquestre $\mathcal{D}_{\text{holdout}}$, soit $\Delta \text{MDL}(c) = L(\mathcal{D}_{\text{holdout}} \mid \mathcal{E}_0) - [L(c) + L(\mathcal{D}_{\text{holdout}} \mid \mathcal{E}_0 \oplus c)]$ en bits codés explicitement (Rissanen, 1978, *Modeling by Shortest Data Description* — `RAPPORTÉ`), pénalisant mécaniquement la complexité gratuite sans jugement subjectif.
* *Valeur opérationnelle ou déductive* : Marge d'amélioration mesurée sur un banc physique/numérique hors-échantillon (rendement, regret cumulé d'une stratégie face à un adversaire optimal, ou théorème cible prouvé dans un assistant de preuve à noyau minimal où l'acceptation syntaxique du certificat vaut démonstration formelle).

### B.b. Mesure minimale de fonctionnement de chaque instrument — Livrable (c)

Pour les quatre instruments impliqués dans la question, le fonctionnement minimal avant déploiement s'établit comme suit :

* **Instrument A — Système générateur multi-modèles**
  * *Seuils minimaux* : Taux de détection (couverture d'au moins `20 %` `(illustratif)` d'un ensemble de solutions rares connues mises sous séquestre à budget fixé) ; taux de fausses alertes structurelles (sorties non analysables ou hors-grammaire) $\le 15\,\%$ `(illustratif)`.
  * *Cas honnêtes appariés* : Problèmes résolus de la littérature mais transcrits sous un isomorphisme systématique de nomenclature et d'échelle numérique (neutralisant la récitation mémorielle) appariés à des instances mathématiquement sur-contraintes sans solution.
  * *Vérifications mécaniques à battre* : Énumération aléatoire guidée par une grammaire probabiliste hors-contexte (PCFG) et recherche locale par mutation syntaxique aveugle au même coût matériel.

* **Instrument B — Contrôle indépendant des modèles ($V$)**
  * *Seuils minimaux* : Taux de détection (sensibilité $1 - \beta$) $\ge 0{,}85$ `(illustratif)` sur cas vrais rares cachés ; taux de fausses alertes (FPR sous $H_{\text{faux}}$ hors-distribution) $\alpha_V \le 0{,}005$ `(illustratif)`, calibré par prédiction conforme inductive sur résidus d'étalonnage (Vovk, Gammerman et Shafer, 2005, *Algorithmic Learning in a Random World* — `VÉRIFIÉ` sous échangeabilité ; l'écart à l'échangeabilité en queue rare est testé par le contrôle négatif ci-dessous).
  * *Cas honnêtes appariés* : Paires *contrefactuelles minimales* (*near-miss*) — chaque mécanisme vrai connu est apparié à un leurre obtenu par une altération chirurgicale unique (inversion de signe causal, violation d'une condition aux limites rare, suppression d'un terme de couplage) qui invalide le mécanisme tout en conservant ses dimensions physiques et invariants globaux.
  * *Vérifications mécaniques à battre* : Vérificateur statique d'homogénéité dimensionnelle/typologique et classifieur linéaire entraîné sur des descripteurs syntaxiques superficiels (longueur, arité, fréquence des opérateurs).

* **Instrument C — Estimateur de rareté sans modèle ($\phi$ + Good-Turing)**
  * *Seuils minimaux* : Détection de nouveauté réelle (rappel sur mécanismes fonctionnellement distincts) $\ge 0{,}95$ `(illustratif)` ; fausses alertes de nouveauté (classer comme « classe distincte » une simple réécriture algébrique ou lexicale d'une classe déjà vue) $\le 0{,}05$ `(illustratif)` sur $m = 64$ `(illustratif)` sondes canoniques.
  * *Cas honnêtes appariés* : Paires d'équivalents camouflés (même loi/stratégie réécrite par changement de variables et permutation d'instructions) appariées à des paires de quasi-homographes (deux stratégies distinctes partageant plus de `85 %` `(illustratif)` de leurs jetons lexicaux).
  * *Vérifications mécaniques à battre* : Déduplication par empreinte cryptographique exacte (SHA-256 après normalisation d'espaces) et distance de Jaccard sur `3`-grammes `(illustratif)` de caractères.

* **Instrument D — Mesure externe de valeur ($\Delta U$ / $\Delta\text{MDL}$)**
  * *Seuils minimaux* : Taux de détection $\ge 0{,}80$ `(illustratif)` sur améliorations authentiques hors-échantillon ; fausses alertes de valeur $\le 0{,}05$ `(illustratif)` sous test de permutation aléatoire des cibles de validation.
  * *Cas honnêtes appariés* : Lois parcimonieuses vraies appariées à des interpolateurs polynomiaux ou tabulaires sur-paramétrés qui passent exactement les cas d'essai publics mais divergent hors-support.
  * *Vérifications mécaniques à battre* : Sélection uniforme au hasard parmi les candidats confirmés par $V$ et heuristique de longueur minimale brute (choisir la chaîne la plus courte validée par $V$).

---

## C. Interventions à coût total égal [Question 2]

On considère trois interventions à budget total strictement constant $B$.

### Intervention M-A : Déduplication comportementale pré-contrôle et contrôle FDR adaptatif

* **Mécanisme à coût égal :** Calculer l'empreinte rapide $\phi(x)$ ($c_\phi \ll c_{\text{ver}}$) sur chaque sortie générée et n'envoyer au contrôle coûteux $V$ qu'*un seul représentant par classe $\phi(x)$*. Le budget économisé en supprimant les vérifications redondantes des modes fréquents est réalloué à deux postes : (i) augmenter le nombre total d'appels génératifs $N_{\text{gen}}$, et (ii) durcir le seuil d'acceptation multiple via la procédure de Benjamini-Hochberg pondérée ou dépendante pour absorber l'accroissement du nombre d'hypothèses rares testées.
* **Ce qu'elle garantit et sous quelles hypothèses :**
  * Si $c_\phi < \rho \, c_{\text{ver}}$ où $\rho$ est le taux de collision modale du système, elle garantit algébriquement (`VÉRIFIÉ`) une augmentation du nombre de classes distinctes évaluées par $V$ à budget $B$ fixe.
  * Sous l'hypothèse (`HYPOTHÈSE`) que $V$ fournit des $p$-valeurs valides (uniformes ou stochastiquement supra-uniformes sous $H_{\text{faux}}$ même en queue rare) vérifiant l'indépendance ou la dépendance positive de régression (PRDS), le seuillage de Benjamini-Hochberg garantit $\text{FDR} \le q$ (Benjamini et Hochberg, 1995, *Controlling the False Discovery Rate: A Practical and Powerful Approach to Multiple Testing* ; Benjamini et Yekutieli, 2001, *The Control of the False Discovery Rate in Multiple Testing under Dependency* — `VÉRIFIÉ` pour les théorèmes mathématiques).
* **Ce qu'elle ne garantit pas :** Aucun gain si $c_{\text{ver}} \ll c_{\text{gen}}$ (contrôle quasi gratuit face à l'inférence LLM) ou si la loi du système est déjà quasi uniforme ($\rho \approx 0$ `(illustratif)`). Ne protège pas contre des faux positifs déterministes de $V$ hors-distribution (où la $p$-valeur nominale sous-estime la vraie probabilité d'erreur).
* **Meilleur indice connu POUR :** L'échantillonnage répété massif à l'inférence augmente continûment la couverture de solutions rares sur problèmes formels et algorithmiques dès lors qu'un filtre de vérification trie les candidats : Brown, Juravsky, Ehrlich, Clark, Le, Ré et Mirhoseini (2024), *Large Language Monkeys: Scaling Inference Compute with Repeated Sampling* (`RAPPORTÉ` ; fiabilité d'attribution élevée sur auteurs, année et titre ; l'étude porte sur la couverture *pass@k* et non directement sur le contrôle du FDR en queue).
* **Meilleur indice connu CONTRE :** Multiplier le nombre de candidats filtrés par un évaluateur imparfait amplifie la sélection d'artefacts qui exploitent les erreurs de l'évaluateur au-delà d'un volume critique : Gao, Schulman et Hilton (2023), *Scaling Laws for Reward Model Overoptimization* (`RAPPORTÉ` ; fiabilité d'attribution élevée sur auteurs, année et titre ; établi sur modèles de récompense appris, la transposition à un contrôle analytique ou expérimental reste une `HYPOTHÈSE`).

### Intervention M-B : Exploration taboue contrainte par grammaire et vérification en cascade

* **Mécanisme à coût égal :** Réduire le nombre brut d'appels $N_{\text{gen}}$ pour financer : (i) un décodage contraint par automate ou grammaire formelle dynamique qui interdit mécaniquement les préfixes structurels ou motifs opératoires des classes fréquentes déjà saturées ($N_c > k_{\text{sat}}$), orientant la masse de probabilité vers la recherche de nouveauté comportementale, et (ii) un **second contrôle indépendant orthogonal** $V_{\text{orth}}$ (test de stress hors-distribution plus coûteux) appliqué uniquement aux candidats rares ayant franchi $V$.
* **Ce qu'elle garantit et sous quelles hypothèses :**
  * Garantit par construction de l'automate (`VÉRIFIÉ`) la suppression exacte des motifs syntaxiques bannis sans effet rebond d'amorçage textuel.
  * Sous l'hypothèse (`HYPOTHÈSE`) d'indépendance conditionnelle des erreurs de $V$ et $V_{\text{orth}}$ sous $H_{\text{faux}}$ ($\text{Cov}(V, V_{\text{orth}} \mid H_{\text{faux}}) \le 0$ `(illustratif)`), le taux de faux positifs joint est majoré par $\alpha_V \cdot \alpha_{V_{\text{orth}}}$ (`VÉRIFIÉ` probabilistement), compensant la chute de prévalence $\pi(r)$ dans les régions forcées.
* **Ce qu'elle ne garantit pas :** Ne garantit pas que le modèle contraint produise des mécanismes sémantiquement cohérents ; si la distribution conditionnelle hors des modes bannis s'effondre dans du bruit syntaxiquement légal mais faux, le rythme net de découvertes chute malgré l'absence de doublons. Ne protège pas si l'indépendance conditionnelle entre $V$ et $V_{\text{orth}}$ échoue.
* **Meilleur indice connu POUR :** Privilégier explicitement la nouveauté comportementale dans l'exploration d'espaces structurés permet de franchir des impasses locales où l'optimisation directe ou l'échantillonnage non guidé stagne : Lehman et Stanley (2011), *Abandoning Objectives: Evolution Through the Search for Novelty Alone* (`RAPPORTÉ` ; fiabilité d'attribution élevée sur auteurs, année et titre, démontré en évolution neuro-comportementale hors LLM).
* **Meilleur indice connu CONTRE :** Forcer le décodage d'un modèle neuronal de langue dans ses queues de basse probabilité provoque une dégradation rapide de la cohérence logique et fonctionnelle des séquences : Holtzman, Buys, Du, Forbes et Choi (2020), *The Curious Case of Neural Text Degeneration* (`RAPPORTÉ` ; fiabilité d'attribution élevée sur auteurs, année et titre) ; de plus, l'exclusion négative par simple consigne textuelle échoue fréquemment (`RAPPORTÉ`, référence à vérifier).

### Intervention M-C : Cloisonnement de modèles *base* pré-alignement multi-familles et test d'invariance

* **Mécanisme à coût égal :** Remplacer les échanges multi-agents (coûteux en jetons de contexte et sujets au conformisme conversationnel) ainsi que les modèles affinés par préférence (RLHF/DPO) par des appels strictement isolés (zéro communication inter-modèles) répartis sur des modèles de base (*base models* pré-alignement) issus de familles architecturales et de corpus distincts, amorcés uniquement par complétion structurée minimale (*few-shot* formel). L'économie de jetons de dialogue finance des tests d'invariance par perturbation aléatoire des paramètres du contrôle $V$ sur chaque candidat retenu.
* **Ce qu'elle garantit et sous quelles hypothèses :**
  * L'isolation informationnelle garantit une corrélation nulle des tirages conditionnellement aux poids des modèles (`VÉRIFIÉ`).
  * Sous l'hypothèse (`HYPOTHÈSE`) que l'alignement post-entraînement concentre l'entropie sur les modes consensuels au détriment des queues valides et que les familles choisies ont des supports partiellement disjoints, l'union des supports accessibles croît à budget de jetons constant.
* **Ce qu'elle ne garantit pas :** Ne garantit aucune décorrélation si tous les modèles *base* héritent des mêmes biais de filtrage des corpus web publics ; risque de hausser le taux de rejet syntaxique initial des modèles *base* moins dociles au formatage.
* **Meilleur indice connu POUR :** Un ensemble de prédicteurs ou de générateurs n'améliore la couverture et la fiabilité globale que dans la mesure où ses membres présentent une diversité d'erreurs et de distributions : Dietterich (2000), *Ensemble Methods in Machine Learning* (`RAPPORTÉ` ; fiabilité d'attribution élevée) ; la réduction d'entropie et de diversité des sorties après alignement RLHF des modèles de langue est également documentée dans la littérature récente (`RAPPORTÉ`, référence à vérifier pour la liste complète des co-auteurs).
* **Meilleur indice connu CONTRE :** Sans alignement d'instruction, les modèles de base consacrent une part substantielle de leur masse de probabilité à des continuations hors-tâche ou bruitées (`OBSERVÉ-NON-AUDITÉ`), pouvant dissiper l'avantage d'entropie une fois rapporté au coût total par candidat valide.

---

## D. Expériences décisives en duel [Livrable (b)] et Critères d'abandon [Question 3]

Chaque expérience oppose deux hypothèses mutuellement exclusives $H_A$ et $H_B$ sur un banc d'essai où le contrôle opérationnel $V$ est doublé, **uniquement pour l'évaluation post-hoc du protocole**, d'une vérité terrain exacte sous séquestre $V^*$ (inaccessible aux interventions). On note $R_{\text{vrai}} = C_{\text{vrai, rare}} / B$ le rythme d'idées distinctes rares ($p_{\text{GT}}(c) \le 0{,}01$ `(illustratif)` sous la politique nominale) confirmées par $V$ **et** vraies selon $V^*$ par unité de budget, et $\widehat{\text{FDR}} = \frac{\#\{c \text{ confirmées par } V \text{ et fausses selon } V^*\}}{\max(1, \#\{c \text{ confirmées par } V\})}$. Le plafond toléré de fausses découvertes est fixé au niveau de référence $\widehat{\text{FDR}}_{\text{réf}}$ observé en base (ou au seuil cible $q = 0{,}10$ `(illustratif)`).

### Expérience Exp-Diag : Test de la concentration modale et de la validité du contrôle en queue

* **$H_A^{(\text{diag})}$ (`HYPOTHÈSE`) :** Sous $N = 10\,000$ `(illustratif)` appels indépendants au système nominal, le système présente à la fois une redondance substantielle (taux de collision fonctionnelle $1 - |\mathcal{C}_{\text{obs}}|/N \ge 0{,}30$ `(illustratif)`), un réservoir non épuisé de classes rares ($\hat{M}_0 = S_1/N \ge 0{,}01$ `(illustratif)`) **et** une précision du contrôle préservée en queue ($\widehat{\text{FDR}}_{\text{rare}} \le 0{,}10$ `(illustratif)` sur les classes avec $N_c = 1$ `(illustratif)`).
* **$H_B^{(\text{diag})}$ (`HYPOTHÈSE`) :** Soit le système n'a plus de queue accessible ($\hat{M}_0 < 0{,}01$ `(illustratif)`), soit il ne se répète déjà presque pas ($1 - |\mathcal{C}_{\text{obs}}|/N < 0{,}30$ `(illustratif)`), soit le contrôle $V$ s'effondre dans la queue rare ($\widehat{\text{FDR}}_{\text{rare}} > 0{,}10$ `(illustratif)`).
* **Métrique et seuil :** Triplet $(1 - |\mathcal{C}_{\text{obs}}|/N, \, \hat{M}_0, \, \widehat{\text{FDR}}_{\text{rare}})$ avec intervalles de confiance exacts de Clopper-Pearson au niveau `95 %` `(illustratif)`.
* **Contrôle négatif :** Générateur aléatoire syntaxiquement valide (mutations aléatoires d'AST sans LLM) soumis à $V$. Si son taux d'acceptation par $V$ excède `0,005` `(illustratif)`, l'insuffisance intrinsèque de $V$ hors-distribution est démontrée.
* **Issues falsificatrices :** Le franchissement simultané des trois seuils falsifie $H_B^{(\text{diag})}$ ; la violation d'au moins un seuil falsifie $H_A^{(\text{diag})}$ (si $\widehat{\text{FDR}}_{\text{rare}} > 0{,}10$ `(illustratif)`, toute exploitation des singletons sans refonte préalable de $V$ est réfutée).

### Expérience Exp-A et critère d'abandon de l'Intervention M-A

* **$H_A^{(\text{M-A})}$ (`HYPOTHÈSE`) :** À budget total $B$ égal sur `5` `(illustratif)` semences indépendantes, M-A accroît $R_{\text{vrai}}$ d'au moins `+20 %` `(illustratif)` par rapport à l'échantillonnage i.i.d. nominal sans filtre $\phi$, tout en maintenant $\widehat{\text{FDR}}(\text{M-A}) \le \widehat{\text{FDR}}_{\text{réf}}$ (test unilatéral de non-infériorité au seuil `0,05` `(illustratif)`).
* **$H_B^{(\text{M-A})}$ (`HYPOTHÈSE`) :** Le gain net $\Delta R_{\text{vrai}}$ est strictement inférieur à `+20 %` `(illustratif)` (surcoût de $\phi$, sur-fusion de vraies idées distinctes ou absence de redondance exploitable) **ou** $\widehat{\text{FDR}}(\text{M-A}) > \widehat{\text{FDR}}_{\text{réf}}$.
* **Contrôle négatif :** Déduplication purement textuelle par hachage SHA-256 exact avant $V$ au même budget $B$.
* **Falsification et critère précis d'abandon (Question 3) :** Un gain $\ge +20\,\%$ `(illustratif)` sans hausse significative du FDR falsifie $H_B^{(\text{M-A})}$. À l'inverse, $H_A^{(\text{M-A})}$ est falsifiée et **l'Intervention M-A est définitivement abandonnée** si l'une quelconque des conditions suivantes est observée : (i) $R_{\text{vrai}}(\text{M-A}) \le R_{\text{vrai}}(\text{SHA-256})$ (l'empreinte comportementale ne bat pas la déduplication de chaînes exactes), (ii) $\Delta R_{\text{vrai}} < +20\,\%$ `(illustratif)` face au système nominal, (iii) $\widehat{\text{FDR}}(\text{M-A}) > \widehat{\text{FDR}}_{\text{réf}}$ avec $p < 0{,}05$ `(illustratif)` au test exact de Fisher, ou (iv) l'audit hors-ligne révèle que $\phi$ écrase dans la même classe plus de `5 %` `(illustratif)` des paires d'idées vraies distinctes selon $V^*$.

### Expérience Exp-B et critère d'abandon de l'Intervention M-B

* **$H_A^{(\text{M-B})}$ (`HYPOTHÈSE`) :** À budget total $B$ égal, l'exploration taboue contrainte couplée au second contrôle $V_{\text{orth}}$ surpasse l'Intervention M-A seule d'au moins `+15 %` `(illustratif)` sur $R_{\text{vrai}}$, avec $\widehat{\text{FDR}}(\text{M-B}) \le \widehat{\text{FDR}}_{\text{réf}}$.
* **$H_B^{(\text{M-B})}$ (`HYPOTHÈSE`) :** La dégradation sémantique hors-mode ou le coût du double contrôle absorbe le budget, donnant $R_{\text{vrai}}(\text{M-B}) < 1{,}15 \times R_{\text{vrai}}(\text{M-A})$ `(illustratif)`, **ou** les erreurs de $V$ et $V_{\text{orth}}$ sont corrélées, laissant $\widehat{\text{FDR}}(\text{M-B}) > \widehat{\text{FDR}}_{\text{réf}}$.
* **Contrôle négatif :** Simple élévation de la température d'échantillonnage ($T = 1{,}3$ `(illustratif)`) sans automate tabou mais avec le même double contrôle $(V, V_{\text{orth}})$ à budget $B$ égal.
* **Falsification et critère précis d'abandon (Question 3) :** Battre à la fois M-A (`+15 %` `(illustratif)`) et le contrôle haute température à FDR maîtrisé falsifie $H_B^{(\text{M-B})}$. **L'Intervention M-B est abandonnée** (falsification de $H_A^{(\text{M-B})}$) dès que $R_{\text{vrai}}(\text{M-B}) \le R_{\text{vrai}}(\text{M-A})$, ou $R_{\text{vrai}}(\text{M-B}) \le R_{\text{vrai}}(\text{température élevée})$, ou $\widehat{\text{FDR}}(\text{M-B}) > \widehat{\text{FDR}}_{\text{réf}}$ ($p < 0{,}05$ `(illustratif)`).

### Expérience Exp-C et critère d'abandon de l'Intervention M-C

* **$H_A^{(\text{M-C})}$ (`HYPOTHÈSE`) :** À budget total $B$ égal, le pool isolé de modèles *base* multi-familles avec test d'invariance augmente $R_{\text{vrai}}$ d'au moins `+15 %` `(illustratif)` par rapport au même pool en versions alignées (*instruct/RLHF*) et réduit le recouvrement inter-modèles sur les classes rares (indice de Jaccard moyen $< 0{,}30$ `(illustratif)`), à $\widehat{\text{FDR}}(\text{M-C}) \le \widehat{\text{FDR}}_{\text{réf}}$.
* **$H_B^{(\text{M-C})}$ (`HYPOTHÈSE`) :** Le déchet syntaxique des modèles *base* ou l'homogénéité des corpus de pré-entraînement rend $R_{\text{vrai}}(\text{M-C}) < 1{,}15 \times R_{\text{vrai}}(\text{instruct})$ `(illustratif)`, ou maintient un recouvrement inter-familles $\ge 0{,}30$ `(illustratif)`, ou dégrade le $\widehat{\text{FDR}}$.
* **Contrôle négatif :** Un unique modèle *instruct* interrogé avec perturbations aléatoires de formulation de l'invite (*prompt paraphrasing*) au même budget total $B$.
* **Falsification et critère précis d'abandon (Question 3) :** Le franchissement conjoint du gain de `+15 %` `(illustratif)` et de la décorrélation Jaccard $< 0{,}30$ `(illustratif)` à FDR non accru falsifie $H_B^{(\text{M-C})}$. **L'Intervention M-C est abandonnée** (falsification de $H_A^{(\text{M-C})}$) si $R_{\text{vrai}}(\text{M-C}) \le R_{\text{vrai}}(\text{un seul modèle instruct + paraphrases})$, ou si $R_{\text{vrai}}(\text{M-C}) < 1{,}15 \times R_{\text{vrai}}(\text{pool instruct})$ `(illustratif)`, ou si $\widehat{\text{FDR}}(\text{M-C}) > \widehat{\text{FDR}}_{\text{réf}}$.

---

## E. Limites de principe [Question 4]

Quatre bornes théoriques contraignent irréductiblement ce que toute méthode peut espérer :

* **Limite bayésienne du taux de fausses découvertes en queue rare :** Pour un contrôle de sensibilité $1 - \beta$ et de taux de faux positifs hors-distribution $\alpha_V > 0$, la proportion de fausses découvertes parmi les idées confirmées de fréquence générative $r$ vaut exactement (Ioannidis, 2005, *Why Most Published Research Findings Are False* — `VÉRIFIÉ` pour l'identité de Bayes) :
  $$\text{FDR}(r) = \frac{\alpha_V \big(1 - \pi(r)\big)}{\alpha_V \big(1 - \pi(r)\big) + (1 - \beta)\,\pi(r)}$$
  Si la prévalence d'idées vraies $\pi(r) \to 0$ lorsque $r \to 0$, alors pour tout contrôle imparfait fixe ($\alpha_V > 0$), $\text{FDR}(r) \to 1$ (`VÉRIFIÉ`). Maintenir $\text{FDR} \le q$ impose $\alpha_V \le \frac{q}{1-q}(1-\beta)\frac{\pi(r)}{1-\pi(r)}$ : si les erreurs du contrôle sont systématiques (biais structurel commun sur les leurres), **aucune répétition** du même contrôle ne peut franchir ce plancher.
* **Borne de support et complexité d'échantillonnage :** Aucune allocation à budget fini ne peut extraire une classe $c^*$ hors du support syntaxique et représentationnel de l'union des modèles ($\sum_k w_k P_k(c^*) = 0$) (`VÉRIFIÉ`). Pour une classe présente avec probabilité $p^* > 0$, toute stratégie sans gradient ni oracle directionnel requiert en espérance $\Omega(1/p^*)$ tirages pour l'atteindre ; en outre, aucune statistique fréquentiste sur $N$ tirages ne peut distinguer individuellement deux probabilités inférieures à $1/N$ (`VÉRIFIÉ`).
* **Indécidabilité de l'équivalence fonctionnelle exacte :** Dès que le langage des mécanismes ou stratégies est Turing-complet, déterminer si deux descriptions syntaxiques calculent exactement la même fonction est indécidable (Rice, 1953, *Classes of Recursively Enumerable Sets and Their Decision Problems* — `VÉRIFIÉ`). Tout quotient calculable $\phi(x)$ en temps borné subit donc un compromis irréductible entre sous-regroupement (compter une variante comme nouvelle) et sur-regroupement (confondre deux idées coïncidant sur les $m$ sondes finies).
* **Non-universalité de l'extrapolation du contrôle :** Sans hypothèse structurelle forte reliant les cas d'essai connus aux régions rares inexplorées, la performance passée d'un évaluateur ou d'un algorithme de recherche sur un sous-ensemble fini ne borne pas son comportement sur le complémentaire (Wolpert et Macready, 1997, *No Free Lunch Theorems for Optimization* — `VÉRIFIÉ` pour l'optimisation boîte noire ; son impact exact sur un domaine physique structuré est une `HYPOTHÈSE` empirique à auditer).

---

## F. Ancrage matériel [Livrable (d)]

Pour exécuter de bout en bout les expériences **Exp-Diag** à **Exp-C** de manière reproductible sans API propriétaire opaque :

* **Modèles à poids ouverts retenus :** Trois familles architecturales distinctes disposant chacune d'une version pré-alignement (*base*) et d'une version alignée (*instruct*) à taille comparable (`7` à `8` milliards `(illustratif)` de paramètres en précision `BF16` `(illustratif)`) : **Llama-3.1-8B** (`8B` `(illustratif)`, licence communautaire Meta), **Qwen-2.5-7B** (`7B` `(illustratif)`, licence Apache `2.0` `(illustratif)`) et **Mistral-7B-v0.3** (`7B` `(illustratif)`, licence Apache `2.0` `(illustratif)`).
* **Banc d'essai exécutable à vérité connue :** Synthèse d'heuristiques symboliques pour problèmes combinatoires paramétrés (p. ex. rangement *online bin-packing* ou ordonnancement avec contraintes) où :
  * $\phi(x)$ est le vecteur des décisions prises sur $m = 64$ `(illustratif)` états sondes fixes ($\sim 5$ millisecondes `(illustratif)` CPU par candidat) ;
  * le contrôle primaire $V$ mesure la performance sur $k_{\text{val}} = 50$ `(illustratif)` instances standards ($\sim 0{,}2$ seconde `(illustratif)` CPU par candidat) ;
  * le contrôle orthogonal $V_{\text{orth}}$ teste des distributions adverses décalées ($k_{\text{orth}} = 100$ `(illustratif)` instances, $\sim 0{,}5$ seconde `(illustratif)` CPU) ;
  * l'oracle d'évaluation post-hoc $V^*$ (strictement isolé des interventions) résout l'écart à l'optimum exact par programmation linéaire en nombres entiers sur $k_{\text{test}} = 2\,000$ `(illustratif)` instances hors-distribution mises sous séquestre.
* **Calcul nécessaire :**
  * Campagne complète : `8` `(illustratif)` bras expérimentaux (`4` `(illustratif)` conditions principales + `4` `(illustratif)` contrôles négatifs) $\times$ `5` `(illustratif)` semences = `40` `(illustratif)` exécutions à budget unitaire équivalent à `10 000` `(illustratif)` générations de `512` `(illustratif)` jetons, soit environ `205` millions `(illustratif)` de jetons générés au total.
  * *Inférence GPU* : À un débit effectif de `3 000` `(illustratif)` jetons/s sous moteur vLLM sur `1` `(illustratif)` GPU serveur de `80` Go `(illustratif)` de VRAM (classe NVIDIA A100), la génération requiert environ `19` `(illustratif)` heures-GPU, portées à `26` `(illustratif)` heures-GPU en incluant la compilation des masques grammaticaux dynamiques de M-B.
  * *Vérification et audit CPU* : Environ `250 000` `(illustratif)` évaluations de $V$ / $V_{\text{orth}}$ plus l'audit exact $V^*$ sur l'ensemble des classes uniques découvertes, représentant environ `1 600` `(illustratif)` heures-cœur CPU (soit `25` `(illustratif)` heures sur un serveur de `64` `(illustratif)` cœurs).
* **Coût financier estimé :** Sur barème infonuagique public à la demande (`2,50` $ `(illustratif)` par heure-GPU `80` Go `(illustratif)` et `0,04` $ `(illustratif)` par heure-cœur CPU), le coût matériel total est d'environ `65` $ `(illustratif)` (GPU) + `64` $ `(illustratif)` (CPU) = **`129` $ `(illustratif)`** (soit une enveloppe prudente de `150` à `220` $ `(illustratif)` stockage et essais de calibration inclus ; une réplication à l'échelle `70B–72B` `(illustratif)` sur nœuds à `4` `(illustratif)` GPU porterait l'enveloppe à environ `1 400`–`1 900` $ `(illustratif)`).

FIN-DE-CELLULE