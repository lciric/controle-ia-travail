État des pièces transmises : les blocs FAITS et QUESTION DE L'ARBITRE sont complets et intègres ; s'agissant du Tour III.1 à l'aveugle, les propositions A et C ne sont pas transmises.

---

## 1. Analyse d'expert et présupposés non établis de la question — *Livrable (a)*

Avant de construire un pipeline d'exploration, un spécialiste de la découverte computationnelle, de l'apprentissage statistique et du contrôle boîte blanche auditerait les hypothèses implicites que l'énoncé tient pour acquises sans preuve :

1. **Transférabilité de la découverte sur corpus vers le contrôle adaptatif** `[HYPOTHÈSE]`. La question suppose qu'un mécanisme d'idéation conçu pour extraire des lois sur des archives scientifiques produira des instruments opérants pour le contrôle boîte blanche. Or, la nature ne modifie pas ses symétries lorsqu'on la mesure, tandis qu'un agent soumis à une pression de sélection ou de style contourne activement les régularités linéaires ou stylistiques `[RAPPORTÉ]`. Ce qui suffit à reconstruire passivement le tableau périodique — Tshitoyan et al. (2019, titre complet et coauteurs : référence à vérifier, *Nature* 571 issu des faits, arXiv : pas sûr) `[VÉRIFIÉ]` — ne garantit aucune marge asymétrique face à une évasion adaptative `[HYPOTHÈSE]`.
2. **Assimilation d'une géométrie de représentation à un générateur causal** `[HYPOTHÈSE]` (partiellement réfutée dans le corpus `[VÉRIFIÉ]`). Retrouver des cartes géographiques ou temporelles dans les cooccurrences ou dans Llama-2 — Gurnee et Tegmark (2023, *Language Models Represent Space and Time*, arXiv 2310.02207 issu des faits) `[VÉRIFIÉ]` — n'établit pas que le système possède l'équivalence d'états causale. Des modèles très précis sur des trajectoires échouent aux tests de type Myhill-Nerode et au transfert vers des lois voisines — Vafa et al. (2024, arXiv 2406.03689 issu des faits ; 2025, arXiv 2507.06952 issu des faits ; titres exacts : pas sûr — références à vérifier) `[VÉRIFIÉ]` — et une variété apparemment circulaire à grande échelle peut se réduire localement à sept rayons discrets en étoile non pilotables de façon lisse — Gupta, Fruengel et Heimersheim (2026, titre : pas sûr — référence à vérifier, arXiv 2610.37796 issu des faits) `[VÉRIFIÉ]`.
3. **Validité du filtrage sur processeur seul (CPU) avant le passage aux modèles à huit milliards de paramètres** `[HYPOTHÈSE]`. Le programme impose un tri rapide sur CPU avant les campagnes sur modèles ouverts autour de huit milliards de paramètres `[RAPPORTÉ]`. Or Gröger, Wen et Brbić (2026, titre : pas sûr — référence à vérifier, arXiv 2602.14486 issu des faits) `[VÉRIFIÉ]` montrent que largeur et profondeur confondent les métriques spectrales globales. Un proxy sur petit réseau ou matrice réduite peut donc créer ou masquer un signal à grande largeur, sauf si chaque métrique est nativement étalonnée par permutation à dimension et degrés fixés `[HYPOTHÈSE]`.
4. **Neutralité des prétraitements historiques malgré le masquage temporel** `[HYPOTHÈSE]`. Même en bannissant l'ignorance simulée par consigne — qui laisse un écart de 52 % sur 477 questions et neuf modèles chez Li et al. (2026, titre : pas sûr — référence à vérifier, arXiv 2601.13717 issu des faits) `[VÉRIFIÉ]` — au profit de coupures strictes avant 1913 ou 1900 — Luo et al. (2026, titre : pas sûr — référence à vérifier, arXiv 2606.02991 issu des faits) ; Hla (2026, titre : pas sûr — référence à vérifier, arXiv : pas sûr) `[VÉRIFIÉ]` —, un expert vérifierait la fuite induite par la normalisation rétroactive des notations chimiques/mathématiques lors de la numérisation moderne et le réglage d'hyperparamètres sur des découvertes connues `[HYPOTHÈSE]`.
5. **Invariance de la formule multiplicative de priorisation** `[HYPOTHÈSE]`. Multiplier quatre notes ordinales de 1 à 5 traite des rangs comme des échelles de rapport et amplifie la variance subjective du critère `potentiel_de_découverte_majeure` `[HYPOTHÈSE]`. Un statisticien accompagnerait ce score d'une analyse de sensibilité aux perturbations de $\pm 1$ point `(illustratif)` par critère.

---

## 2. Données brutes de départ à privilégier

Toute représentation pré-entraînée ou graphe pré-agrégé écrase la chronologie, incorpore le biais de déclaration — Gordon et Van Durme (2013, *Reporting Bias and Knowledge Acquisition*, arXiv : pas sûr) `[VÉRIFIÉ]` — et détruit la polarité des énoncés (confirmation contre anomalie). Il faut partir de quatre flux bruts exploitables sur CPU `[HYPOTHÈSE]` :

1. **Arbres syntaxiques abstraits (AST) d'équations typées et graphes de preuves formelles horodatés par commit** : archives publiques de Lean (`mathlib`), Metamath et sources LaTeX d'arXiv antérieures à une coupure fixe, analysées en opérateurs, variables et dimensions physiques avant toute vectorisation `[HYPOTHÈSE]`. Avantage : vérification mécanique exacte sans juge génératif `[RAPPORTÉ]`.
2. **Journaux d'événements relationnels bruts `(date, document, prédicat_syntaxique_signé, arguments, valeur/unité)`** extraits de corpus pré-coupure (archives pré-1900 ou pré-1913 `[VÉRIFIÉ]`, tables expérimentales de matériaux) *avant* tout seuillage en arêtes binaires, afin de conserver les distributions complètes de fréquence et les contradictions empiriques intra-domaine `[HYPOTHÈSE]`.
3. **Mondes synthétiques procéduraux à lois et anomalies plantées** : automates finis déterministes, systèmes algébriques ou dynamiques dont l'évaluateur externe détient seul le générateur minimal, avec variables délibérément confondues ou invariants latents omis `[RAPPORTÉ]`.
4. **Journaux bruts d'actions séquentielles et tenseurs de poids statiques $(W_Q, W_K, W_V, W_O, W_{\text{MLP}}, W_U)$** de modèles ouverts lus par tranches sur disque, couplés à des banques d'activations brutes extraites en passe avant unique sans post-traitement génératif `[HYPOTHÈSE]`.

---

## 3. Démarcation théorique et risques méthodologiques

### 3.1 Ce qui est mathématiquement inférable contre ce qui est sous-déterminé

- **Inférable sous conditions explicites** :
  1. *La géométrie relationnelle du second ordre* : la factorisation implicite d'information mutuelle ponctuelle décalée — Mikolov, Chen, Corrado et Dean (2013, *Efficient Estimation of Word Representations in Vector Space*, arXiv 1301.3781 issu des faits) ; Pennington, Socher et Manning (2014, *GloVe: Global Vectors for Word Representation*, arXiv : pas sûr) ; Levy et Goldberg (2014, *Neural Word Embedding as Implicit Matrix Factorization*, arXiv : pas sûr) `[VÉRIFIÉ]` — et les symétries de cooccurrence par paires reconstruisent des variétés latentes lorsque le taux de co-mention est une fonction monotone d'une distance sous-jacente, comme pour 119 cités assyriennes ou 50 villes américaines — Tobler et Wineburg (1971, titre : pas sûr — référence à vérifier, arXiv : pas sûr) ; Barjamovic et al. (2017, document de travail NBER 23992 issu des faits, titre : pas sûr — référence à vérifier, arXiv : pas sûr) ; Louwerse et Zwaan (2009, titre : pas sûr — référence à vérifier, arXiv : pas sûr) ; Karkada et al. (2026, titre : pas sûr — référence à vérifier, arXiv 2602.15029 issu des faits) `[VÉRIFIÉ]`.
  2. *L'accord topologique des voisinages locaux* après étalonnage de permutation neutralisant largeur et profondeur — Gröger, Wen et Brbić (2026, précité, arXiv 2602.14486 issu des faits) `[VÉRIFIÉ]`, qualifiant fortement l'hypothèse de convergence globale de Huh, Cheung, Wang et Isola (2024, *The Platonic Representation Hypothesis*, arXiv 2405.07987 issu des faits) `[HYPOTHÈSE]`.
  3. *La sur-complexité syntaxique et les violations de transitivité* dans des corpus d'équations et de preuves formelles `[HYPOTHÈSE]`.
- **Non inférable à partir des seules statistiques de forme** :
  1. *L'ancrage référentiel et le quotient d'états causal minimal (Myhill-Nerode)* : la forme distributionnelle seule ne détermine ni la référence — Bender et Koller (2020, *Climbing towards NLU: On Meaning, Form, and Understanding in the Age of Data*, arXiv : pas sûr) `[VÉRIFIÉ]` — ni la loi transférable hors support observationnel — Vafa et al. (2024, 2025, précités) `[VÉRIFIÉ]`.
  2. *La continuité différentiable locale* à partir d'une projection globale lisse — Gupta, Fruengel et Heimersheim (2026, précité) `[VÉRIFIÉ]`.
  3. *Les fréquences objectives du monde physique*, déformées par la sous-déclaration de l'évidence et les biais culturels — Gordon et Van Durme (2013, précité) ; Caliskan, Bryson et Narayanan (2017, *Semantics Derived Automatically from Language Corpora Contain Human-Like Biases*, arXiv 1608.07187 issu des faits) `[VÉRIFIÉ]`.

### 3.2 Audit formel des quatre familles de mécanismes de découverte

1. **Alignement inter-domaines à distance de surface** — Gentner (1983, *Structure-Mapping: A Theoretical Framework for Analogy*, arXiv : pas sûr) ; Swanson (1986, *Fish Oil, Raynaud's Syndrome, and Undiscovered Public Knowledge*, arXiv : pas sûr) ; Uzzi, Mukherjee, Stringer et Jones (2013, *Atypical Combinations and Scientific Impact*, arXiv : pas sûr) `[RAPPORTÉ]`.
   - *Verdict* : **Fragile sur texte non typé ; solide uniquement sur homomorphismes d'opérateurs typés** `[HYPOTHÈSE]`. Le chaînage lexical $A\text{-}B\text{-}C$ explose par polysémie et les analogies vectorielles reposent en partie sur des règles d'exclusion d'entrée — Linzen (2016, *Issues in Evaluating Semantic Spaces Using Word Analogies*, arXiv 1606.07736 issu des faits) ; Nissim, van Noord et van der Goot (2020, *Fair Is Better than Sensational: Man Is to Doctor as Woman Is to Doctor*, arXiv 1905.09866 issu des faits) `[VÉRIFIÉ]`. Le mécanisme ne devient rigoureux que lorsqu'il cherche un isomorphisme partiel entre graphes d'équations adimensionnées ou graphes relationnels typés sous contrainte de conservation des arités `[HYPOTHÈSE]`.
2. **Séparation de concepts confondus (scission conceptuelle)** — Davis (1971, titre : pas sûr — référence à vérifier, arXiv : pas sûr) ; Lakatos (1976, *Proofs and Refutations*, arXiv : pas sûr) `[RAPPORTÉ]`.
   - *Verdict* : **Mécanisme sous-exploité et formalisable algébriquement** `[HYPOTHÈSE]`. Le verrou est la confusion avec l'homonymie ordinaire `[RAPPORTÉ]`. Or les deux phénomènes ont des signatures topologiques opposées `[HYPOTHÈSE]` : un *homonyme* engendre deux clusters de contextes quasi disjoints (forte modularité de partition), tandis qu'une *fausse identité conceptuelle* (ex. chaleur/température `[RAPPORTÉ]`) réside dans **un seul cluster expérimental dense** mais engendre une **frustration de cycles signés** (dans le sous-régime $R_1$, $X$ croît avec $Y$ ; dans le sous-régime $R_2$ du même domaine, $X$ croît à $Y$ constant, violant l'unicité de fonction d'état).
3. **Dynamiques variationnelles et percolation sur graphes finis** — Burt (2004, *Structural Holes and Good Ideas*, arXiv : pas sûr) ; Tria et al. (2014, titre : pas sûr — référence à vérifier, arXiv : pas sûr) `[RAPPORTÉ]`.
   - *Verdict* : **Risque élevé d'artefact statistique** `[HYPOTHÈSE]`. Sans limite thermodynamique ni continuité d'espace de phases `[RAPPORTÉ]`, l'hétérogénéité lourde des degrés et l'arbitraire ontologique (fusionner ou scinder des sous-disciplines) fabriquent mécaniquement des pseudo-exposants critiques. Toute loi d'entropie de trajectoire qui ne bat pas un modèle nul microcanonique préservant la séquence jointe des degrés temporels doit être rejetée `[HYPOTHÈSE]`.
4. **Création de nouvelles abstractions hors de l'alphabet existant** — Carey (2009, titre : pas sûr — référence à vérifier, arXiv : pas sûr) ; Kuhn (1962, *The Structure of Scientific Revolutions*, arXiv : pas sûr) ; Udrescu et Tegmark (2020, *AI Feynman: A Physics-Inspired Method for Symbolic Regression*, arXiv : pas sûr) ; Schmidhuber (2010, titre : pas sûr — référence à vérifier, arXiv : pas sûr) `[RAPPORTÉ]`.
   - *Verdict* : **Scindé en deux pistes solides et une piste risquée** `[HYPOTHÈSE]`. La décomposition préalable par symétries/séparabilité (Udrescu et Tegmark, 2020 `[RAPPORTÉ]`) et l'anti-unification d'AST par longueur de description minimale (MDL comptabilisant le coût exact de la nouvelle définition sur théorèmes tenus à l'écart) brisent la circularité sans oracle génératif `[HYPOTHÈSE]`. À l'inverse, exploiter en lecture seule les sous-systèmes internes épars de surprise/récompense de modèles de langue — Xu et al. (2026, titre : pas sûr — référence à vérifier, arXiv 2602.00986 issu des faits) `[RAPPORTÉ]` — risque de confondre nouveauté formelle, rareté lexicale et réminiscence de pré-entraînement `[HYPOTHÈSE]`.

### 3.3 Synthèse des six menaces méthodologiques et parades

| Biais | Source établie | Parade mécanique obligatoire `[HYPOTHÈSE]` |
|---|---|---|
| Fréquence | Hamilton, Leskovec et Jurafsky (2016, *Diachronic Word Embeddings Reveal Statistical Laws of Semantic Change*, arXiv 1605.09096 issu des faits) ; Dubossarsky, Weinshall et Grossman (2017, *Outta Control: Laws of Semantic Change and Inherent Biases in Word Representation Models*, arXiv : pas sûr) `[VÉRIFIÉ]` | Stratification par déciles de fréquence et permutations préservant fréquences et degrés `[RAPPORTÉ]` |
| Échelle (largeur/profondeur) | Gröger, Wen et Brbić (2026, précité) `[VÉRIFIÉ]` | Z-score sur 1 000 `(illustratif)` permutations aléatoires de mêmes largeur et profondeur |
| Survivant | Rétro-sélection des percées connues `[RAPPORTÉ]` | Évaluation prospective exhaustive de *tous* les candidats émis à $t_0$, avec pénalité Benjamini-Hochberg `[RAPPORTÉ]` |
| Sondes mémorisantes | Hewitt et Liang (2019, *Designing and Interpreting Probes with Control Tasks*, arXiv 1909.03368 issu des faits) `[VÉRIFIÉ]` | Sélectivité $\text{Sel} = \text{Score}_{\text{réel}} - \text{Score}_{\text{étiquettes permutées par type}}$ |
| Fuites temporelles | Écart de 52 % sous consigne chez Li et al. (2026, précité) `[VÉRIFIÉ]` | Masquage temporel strict — Ma et al. (2026, titre : pas sûr — référence à vérifier, arXiv 2605.03762 issu des faits) `[VÉRIFIÉ]` —, modèles pré-coupure ou mondes synthétiques neufs |
| Circularité | Juges génératifs ou optimisation sur sonde `[RAPPORTÉ]` | Critères MDL/formels purs ; sondes en lecture seule hors boucle d'entraînement `[RAPPORTÉ]` |

---

## 4. Méthodes, instruments de contrôle boîte blanche, mesures minimales et ancrage matériel — *Livrables (c) et (d)*

### 4.1 Trois méthodes transférant l'analyse structurelle vers le contrôle boîte blanche

1. **Détection séquentielle par e-processus de Huber-DKW sous référence contaminée** `[HYPOTHÈSE]`. Pour détecter sur un horizon quelconque un sabotage dilué sous garantie de faux positifs toujours valide $\mathbb{P}_{H_0}(\exists t \ge 1 : E_t \ge 1/\alpha) \le \alpha$ lorsque la base d'étalonnage « honnête » de $n$ épisodes contient jusqu'à une fraction $\epsilon$ d'épisodes corrompus par un tiers `[RAPPORTÉ]`, les tests CUSUM empiriques échouent : un seul outlier gonfle le seuil ou déclenche de fausses alertes `[HYPOTHÈSE]`. On construit une martingale de test non paramétrique sur scores bornés $s_t \in [0,1]$ `(illustratif)` dont la dérive de référence $\hat{\mu}_{1-\epsilon}^{\text{sup}}$ majore par inégalité de Dvoretzky-Kiefer-Wolfowitz (DKW) l'espérance de la loi tronquée des $(1-\epsilon)$ épisodes de référence les plus bas, combinée par médiane de moyennes de sous-blocs `[HYPOTHÈSE]`.
2. **Sondes d'holonomie relationnelle locale (lecture seule)** `[HYPOTHÈSE]`. Au lieu d'une sonde linéaire ponctuelle $w^\top h(x)$ vulnérable à la rotation de style et à la mémorisation `[RAPPORTÉ]`, on soumet l'entrée $x$ à un cycle fermé de $k = 6$ `(illustratif)` transformations syntaxiques/algébriques préservant l'invariant logique $(g_1, \dots, g_k)$ inspiré des tests d'équivalence de Myhill-Nerode — Vafa et al. (2024, précité) `[VÉRIFIÉ]`. On mesure la distorsion du graphe des $m = 15$ `(illustratif)` plus proches voisins étalonnée par permutation (Gröger et al., 2026 `[VÉRIFIÉ]`) et l'erreur de fermeture du cycle linéaire inter-couches `[HYPOTHÈSE]`.
3. **Audit spectral direct des poids et de l'asymétrie de coordination** `[HYPOTHÈSE]`. Sans passe avant coûteuse, on extrait les valeurs singulières et vecteurs singuliers des produits bilinéaires $W_{OV} = W_O W_V$, $W_{QK} = W_Q^\top W_K$ et de la matrice de désimbrication $W_U$ `[HYPOTHÈSE]`. Pour détecter un canal de coordination implicite entre copies partageant leurs poids `[RAPPORTÉ]`, on mesure l'indice de bris de symétrie sous le groupe symétrique $S_K$ d'options isomorphes : si les poids projettent asymétriquement des étiquettes sémantiquement permutables vers un mode dominant commun, deux copies convergeront sans communiquer vers ce point focal `[HYPOTHÈSE]`.

### 4.2 Mesures minimales de fonctionnement par instrument nommé — *Livrable (c)*

*(Tous les seuils chiffrés ci-dessous sont marqués `(illustratif)` et destinés au préenregistrement avant lecture des résultats.)*

| Instrument nommé dans la question | Taux de détection minimal (TPR) et fausses alertes (FPR) `(illustratif)` | Cas honnêtes appariés | Vérification mécanique simple à battre |
|---|---|---|---|
| **1. Aligneur inter-domaines** (rapprochements) | Rappel@50 $\ge 0{,}30$ ; taux de fausses découvertes $\text{FDR} \le 0{,}10$ sur rétrodiction temporelle stricte | Paires d'équations/domaines de mêmes degrés, fréquences lexicales et distance temporelle sans pont validé à $+10$ ans `(illustratif)` | Cosinus TF-IDF / PMI décalée et chaînage $A\text{-}B\text{-}C$ non typé de Swanson |
| **2. Scissionneur de concepts confondus** | $\text{TPR} \ge 0{,}75$ à $\text{FPR} \le 0{,}05$ ($\text{AUROC} \ge 0{,}80$) | Termes polysémiques ordinaires (homonymes) et termes scientifiques mono-sens appariés par fréquence et degré | Modularité de Louvain / bimodalité de clustering des plongements contextuels |
| **3. Détecteur d'émergence sur graphes finis** | $\text{TPR} \ge 0{,}65$ à $\text{FPR} \le 0{,}05$ après z-score de permutation | Sous-graphes de mêmes séquences de degrés temporels et même granularité sans émergence ultérieure | Centralité d'intermédiarité / trous structuraux statiques de Burt (2004) |
| **4. Synthétiseur d'abstractions (MDL)** | Redécouverte $\text{TPR} \ge 0{,}70$ des primitives ablatées ; fausses primitives retenues $\le 0{,}05$ (gain MDL hors échantillon $\le 0$) | Corpus formels complets sans ablation où aucun enrichissement d'alphabet n'est requis | Compression fréquentielle de sous-arbres (type Lempel-Ziv / BPE syntaxique sans symétries) |
| **5. Détection séquentielle** (sabotage diffus) | $\text{TPR} \ge 0{,}80$ avant $T = 1\,000$ pas ; $\text{FPR}_{\infty} \le 0{,}05$ *anytime-valid* sous contamination $\epsilon = 0{,}05$ | Suites d'actions honnêtes appariées en longueur, entropie d'actions et difficulté de tâche | CUSUM empirique non tronqué et test de Wald glissant sur moyenne empirique |
| **6. Sondes boîte blanche robustes** | $\text{TPR} \ge 0{,}75$ sous paraphrase d'évasion ; $\text{FPR} \le 0{,}02$ ; sélectivité Hewitt-Liang $\ge 0{,}35$ | Requêtes honnêtes soumises aux mêmes transformations syntaxiques, de longueur et perplexité appariées | Sonde linéaire logistique $L_2$ ponctuelle + filtre de perplexité scalaire |
| **7. Audit direct des poids** | $\text{TPR} \ge 0{,}75$ à $\text{FPR} \le 0{,}05$ sur modèles avec déclencheur planté ou coordination $> 1/K + 0{,}20$ | Modèles ouverts propres affinés sur le même volume de jetons, même architecture et hyperparamètres | Norme de Frobenius, norme spectrale maximale brute et kurtosis des poids par couche |

### 4.3 Ancrage matériel et budget de calcul — *Livrable (d)*

- **Échelon 1 — Filtrage CPU strict (Actions 1 à 4 et prototypage des Actions 5 et 6)** : 1 poste ou serveur CPU 16 cœurs / 64 Go de RAM `(illustratif)`, sans carte graphique `[RAPPORTÉ]`. Modèles ouverts légers pour tests d'activations sur CPU : suite `EleutherAI/Pythia-160m` et `Pythia-410m` (poids et points de contrôle intermédiaires publics) `[RAPPORTÉ]` ; l'inspection SVD par tranches des poids d'un modèle de 7 à 8 milliards de paramètres en `bfloat16` (~16 Go sur disque `(illustratif)`) s'exécute aussi sur CPU en lisant couche par couche (< 4 Go RAM actifs `(illustratif)`). Temps par expérience : 2 à 12 heures CPU `(illustratif)`. Coût infonuagique estimé : **1 € à 8 € par expérience `(illustratif)`**.
- **Échelon 2 — Validation ciblée sur modèles ouverts autour de huit milliards de paramètres `[RAPPORTÉ]` (uniquement pour les pistes ayant survécu à l'échelon 1)** : `allenai/OLMo-7B` (retenu en priorité car son corpus de pré-entraînement Dolma est intégralement ouvert et vérifiable contre les fuites `[RAPPORTÉ]`) et `meta-llama/Meta-Llama-3-8B` ou `mistralai/Mistral-7B-v0.3` `[RAPPORTÉ]`. Calcul requis : passe avant d'extraction d'activations et jeux de coordination sur 1 carte GPU 24 à 80 Go VRAM pendant 4 à 15 heures `(illustratif)` (plus entraînement contrôlé d'adaptateurs LoRA dans le seul bras d'attaque déclaré `[RAPPORTÉ]`). Coût estimé : **10 € à 45 € par campagne `(illustratif)`**.

---

## 5. Vérification indépendante

Pour établir hors de l'équipe de conception que les gains mesurés ne proviennent ni d'un sur-ajustement ni d'une fuite :

1. **Préenregistrement cryptographique** : dépôt public d'une empreinte SHA-256 du code d'analyse, des hyperparamètres figés, des seuils de décision et du plan de correction des comparaisons multiples *avant* réception des jeux de test `[RAPPORTÉ]`.
2. **Séquestre externe en double aveugle** : un évaluateur indépendant génère avec une graine secrète (a) les mondes synthétiques à lois plantées `[RAPPORTÉ]`, (b) les traces d'étalonnage contaminées à un taux inconnu $\epsilon \in [0, 0{,}10]$ `(illustratif)`, et (c) un lot mélangé de points de contrôle de modèles ouverts propres et modifiés (bras d'attaque séparé `[RAPPORTÉ]`).
3. **Vérifiabilité déterministe hors ligne** : exécution intégrale des scripts d'évaluation dans un conteneur sans accès réseau, sans appel à un juge génératif `[RAPPORTÉ]`, avec vérification automatique des sommes de contrôle des archives pré-coupure (pré-1900 / 1913 `[VÉRIFIÉ]`).
4. **Publication obligatoire des distributions nulles** : chaque score publié doit être accompagné du code générant ses contrôles par permutation de degrés/fréquences/dimensions et ses tâches de sélectivité aux étiquettes permutées.

---

## 6. Reformulation exigeante du problème

> **Problème reformulé.** *Étant donné des flux bruts horodatés d'équations typées, de preuves formelles, de relations textuelles pré-coupure, de traces séquentielles et de tenseurs de poids de modèles ouverts (~8 milliards de paramètres `[RAPPORTÉ]`), comment construire des opérateurs algorithmiques vérifiables sans juge génératif et d'abord réfutables sur processeur seul `[RAPPORTÉ]`, qui : (1) extraient des invariants structurels (frustration signée intra-cluster, primitives compressives MDL, homomorphismes typés) survivant aux contrôles de permutation de fréquence, de degré et de dimension d'échelle `[VÉRIFIÉ]`, et (2) convertissent ces invariants en moniteurs boîte blanche en lecture seule garantissant simultanément un contrôle valide à tout instant des fausses alertes sous contamination $\epsilon$ de la référence et un coût d'évasion asymétrique mesurable face aux sondes linéaires et scalaires `[HYPOTHÈSE]` ?*

---

## 7. Programme d'actions prioritaires classé et expériences décisives — *Livrables (b) et (d)*

### 7.1 Classement des huit pistes candidates selon la formule imposée

Formule : `score = (gain_informatif × facilité × portée × potentiel_de_découverte_majeure) / coût` (notes de 1 à 5 ; toutes les notes attribuées et tous les scores calculés ci-dessous sont marqués `(illustratif)`).

| Rang | Action | Gain `(ill.)` | Facilité `(ill.)` | Portée `(ill.)` | Potentiel `(ill.)` | Coût `(ill.)` | **Score `(illustratif)`** | Retenue (Top 6) |
|---|---|---|---|---|---|---|---|---|
| **1** | **A1.** E-processus séquentiel robuste à une référence contaminée | 5 | 5 | 5 | 4 | 1 | **500,0** | Oui |
| **2** | **A2.** Scission conceptuelle par frustration de cycles signés | 5 | 4 | 4 | 5 | 1 | **400,0** | Oui |
| **3** | **A3.** Test microcanonique des dynamiques variationnelles / percolation | 5 | 5 | 4 | 3 | 1 | **300,0** | Oui |
| **4** | **A4.** Synthèse d'objets formels par anti-unification MDL et symétries | 4 | 4 | 4 | 4 | 1 | **256,0** | Oui |
| **5** | **A5.** Sondes d'holonomie de cycle (Myhill-Nerode local) sous évasion | 5 | 4 | 5 | 5 | 2 | **250,0** | Oui |
| **6** | **A6.** Audit spectral des poids et coordination implicite inter-copies | 5 | 3 | 5 | 5 | 2 | **187,5** | Oui |
| 7 | **A7.** Homomorphismes d'équations typées inter-domaines pré-coupure | 4 | 3 | 4 | 3 | 1 | 144,0 | Non (lot 2) |
| 8 | **A8.** Lecture seule de sous-systèmes internes de surprise (cf. Xu et al., 2026) | 4 | 2 | 3 | 4 | 3 | 32,0 | Non (lot 2) |

*(Note de sensibilité : sous perturbation uniforme de $\pm 1$ point `(illustratif)` des numérateurs, les quatre actions purement CPU A1–A4 restent en tête devant les actions hybrides CPU/GPU A5–A6 `[HYPOTHÈSE]`.)*

---

### 7.2 Six expériences décisives préenregistrées (`H_A` contre `H_B`)

#### Action 1 — Détection séquentielle sous contamination de référence (Score : 500,0 `illustratif`)
- **`H_A`** `[HYPOTHÈSE]` : Sur des trajectoires de $T = 1\,000$ `(illustratif)` actions où un sabotage diffus n'agit que sur une fraction $p_s = 0{,}03$ `(illustratif)` des pas, avec une base d'étalonnage de $n = 500$ `(illustratif)` trajectoires contenant $\epsilon = 0{,}05$ `(illustratif)` d'épisodes contaminés plantés par un tiers, l'e-processus quantile-écrêté de Huber-DKW respecte un taux de fausses alertes cumulé sur tout l'horizon $\text{FPR}_{\infty} \le 0{,}05$ `(illustratif)` et atteint $\text{TPR} \ge 0{,}80$ `(illustratif)`, surpassant d'au moins $+0{,}25$ `(illustratif)` de TPR le CUSUM empirique ré-étalonné au même $\text{FPR}_{\infty}$.
- **`H_B`** `[HYPOTHÈSE]` : L'écrêtement requis pour couvrir $\epsilon = 0{,}05$ `(illustratif)` sans connaître les épisodes contaminés absorbe le signal dilué ($p_s = 0{,}03$ `(illustratif)`), entraînant soit $\text{FPR}_{\infty} > 0{,}05$ `(illustratif)`, soit $\text{TPR} < 0{,}80$ `(illustratif)`, soit un écart $< +0{,}25$ `(illustratif)` face au CUSUM empirique.
- **Métrique et seuil** : Couple $(\text{FPR}_{\infty}, \text{TPR})$ estimé sur $2\,000$ `(illustratif)` épisodes indépendants ; seuils $\text{FPR}_{\infty} \le 0{,}05$ et $\text{TPR} \ge 0{,}80$ `(illustratif)`.
- **Contrôle négatif explicite** : Permutation temporelle circulaire des scores à l'intérieur des épisodes honnêtes + contamination adversarialement placée juste sous le quantile $1-\epsilon$ de la référence.
- **Premier pas CPU et coût** : Simulation Monte-Carlo + rejeu de traces publiques d'agents sur 8 cœurs CPU en 2 heures `(illustratif)` ; **coût : ~1 € `(illustratif)`**.
- **Issues de réfutation** : Observer $\text{FPR}_{\infty} \le 0{,}05$, $\text{TPR} \ge 0{,}80$ et $\Delta\text{TPR} \ge +0{,}25$ `(illustratif)` réfute `H_B` ; toute violation de l'une de ces trois bornes réfute `H_A`.

#### Action 2 — Scission conceptuelle par frustration de cycles signés (Score : 400,0 `illustratif`)
- **`H_A`** `[HYPOTHÈSE]` : Sur (i) des mondes synthétiques mêlant $50$ `(illustratif)` concepts fusionnés plantés, $50$ `(illustratif)` homonymes et $200$ `(illustratif)` concepts purs, puis (ii) des archives scientifiques pré-1900 `[VÉRIFIÉ]`, le score de frustration de cycles signés intra-cluster sépare les concepts fusionnés des homonymes et termes stables avec $\text{AUROC} \ge 0{,}80$ `(illustratif)`, un gain $\Delta\text{AUROC} \ge +0{,}15$ `(illustratif)` sur la modularité contextuelle, et $p < 0{,}01$ `(illustratif)` corrigé Benjamini-Hochberg contre le modèle nul.
- **`H_B`** `[HYPOTHÈSE]` : Le bruit de déclaration et l'incomplétude des prédicats extraits confondent frustration signée, homonymie et bruit de fréquence ($\text{AUROC} < 0{,}80$, ou $\Delta\text{AUROC} < +0{,}15$, ou $p \ge 0{,}01$ `(illustratif)`).
- **Métrique et seuil** : $\text{AUROC}$ hors échantillon et $\Delta\text{AUROC}$ face au détecteur de bimodalité de plongements.
- **Contrôle négatif explicite** : Permutations aléatoires des signes relationnels préservant exactement les degrés signés par nœud et les fréquences lexicales.
- **Premier pas CPU et coût** : Extraction syntaxique spaCy/UD et calcul spectral du laplacien signé sur CPU (6 heures `(illustratif)`) ; **coût : ~3 € `(illustratif)`**.
- **Issues de réfutation** : Atteindre simultanément $\text{AUROC} \ge 0{,}80$, $\Delta\text{AUROC} \ge +0{,}15$ et $p < 0{,}01$ `(illustratif)` réfute `H_B` ; l'échec sur au moins un critère réfute `H_A`.

#### Action 3 — Test microcanonique des dynamiques variationnelles et de percolation (Score : 300,0 `illustratif`)
- **`H_A`** `[HYPOTHÈSE]` : Sur des graphes de concepts/citations horodatés découpés par fenêtres quinquennales `(illustratif)` à étanchéité stricte, l'entropie variationnelle de trajectoires et l'indice de percolation étalonnés en z-score sur $1\,000$ `(illustratif)` graphes nuls microcanoniques (préservant degrés joints temporels) et invariants sous fusion/scission de $20\,\%$ `(illustratif)` des classes ontologiques prédisent l'émergence de nouveaux ponts à $+5$ ans `(illustratif)` avec un gain de Précision@100 $\ge +0{,}15$ `(illustratif)` ($p < 0{,}01$ `(illustratif)`) sur la centralité des trous structuraux de Burt.
- **`H_B`** `[HYPOTHÈSE]` : Une fois neutralisés l'hétérogénéité des degrés et le grain ontologique, le gain résiduel tombe sous $+0{,}15$ `(illustratif)` (ou $p \ge 0{,}01$ `(illustratif)`), établissant que les signatures critiques observées sur graphes finis sont des artefacts d'échelle et de degrés.
- **Métrique et seuil** : $\Delta\text{Précision@100} \ge +0{,}15$ `(illustratif)` à $p < 0{,}01$ `(illustratif)` et dérive relative $< 10\,\%$ `(illustratif)` sous coarsening ontologique.
- **Contrôle négatif explicite** : Ré-échantillonnage par échanges d'arêtes dirigés préservant l'ordre chronologique et les degrés entrants/sortants exacts.
- **Premier pas CPU et coût** : Sous-graphe temporel arXiv/OpenAlex pré-2015 `(illustratif)` sur 16 cœurs CPU (8 heures `(illustratif)`) ; **coût : ~4 € `(illustratif)`**.
- **Issues de réfutation** : Surpasser le seuil avec stabilité ontologique réfute `H_B` ; l'effondrement sous le modèle nul ou sous changement de grain réfute `H_A` (et clôture immédiatement cette branche théorique).

#### Action 4 — Synthèse d'objets formels hors alphabet par MDL et symétries (Score : 256,0 `illustratif`)
- **`H_A`** `[HYPOTHÈSE]` : Sur $100$ `(illustratif)` sous-théories de Lean `mathlib` et systèmes d'équations physiques dont une définition intermédiaire clé a été ablatée et développée en termes primitifs, l'anti-unification d'AST guidée par réduction de symétries dimensionnelles et critère MDL strict réalise un gain net de compression $\ge 15\,\%$ `(illustratif)` sur des théorèmes/équations tenus à l'écart (coût de la nouvelle définition inclus) et dépasse d'au moins $+10$ points de pourcentage `(illustratif)` une compression d'arbres fréquentielle sans symétries.
- **`H_B`** `[HYPOTHÈSE]` : La recherche hors alphabet sur-apprend des abréviations syntaxiques locales non transférables ou subit une explosion combinatoire (gain MDL net hors échantillon $< 15\,\%$ ou écart $< +10$ points `(illustratif)`).
- **Métrique et seuil** : Gain relatif de longueur binaire minimale d'AST sur le pli de test disjoint.
- **Contrôle négatif explicite** : Corpus formels non ablatés et AST aléatoires préservant les fréquences d'opérateurs (où le gain MDL net attendu doit rester $\le 0$ `(illustratif)`).
- **Premier pas CPU et coût** : Analyseur d'AST Python/Rust sur `mathlib` et 100 équations physiques sur CPU (10 heures `(illustratif)`) ; **coût : ~5 € `(illustratif)`**.
- **Issues de réfutation** : Gain net $\ge 15\,\%$ et avance $\ge +10$ points `(illustratif)` réfutent `H_B` ; résultat inférieur réfute `H_A`.

#### Action 5 — Sondes d'holonomie relationnelle contre sondes linéaires sous évasion (Score : 250,0 `illustratif`)
- **`H_A`** `[HYPOTHÈSE]` : En lecture seule stricte (aucun entraînement de l'agent sur la sonde `[RAPPORTÉ]`), face à des paraphrases stylistiques et reformulations d'évasion qui abaissent une sonde linéaire $L_2$ sous $\text{TPR} < 0{,}40$ `(illustratif)`, la sonde d'holonomie locale sur cycles de $k = 6$ `(illustratif)` transformations maintient $\text{TPR} \ge 0{,}75$ à $\text{FPR} \le 0{,}02$ `(illustratif)`, une marge $\Delta\text{TPR} \ge +0{,}35$ `(illustratif)` sur la sonde linéaire et une sélectivité de Hewitt-Liang $\ge 0{,}35$ `(illustratif)` après étalonnage de dimension Gröger-Wen-Brbić.
- **`H_B`** `[HYPOTHÈSE]` : En raison des rayons discrets locaux (Gupta et al., 2026 `[VÉRIFIÉ]`) et de l'instabilité hors support (Vafa et al., 2024, 2025 `[VÉRIFIÉ]`), les requêtes honnêtes elles-mêmes présentent un défaut d'holonomie élevé, empêchant d'obtenir simultanément $\text{TPR} \ge 0{,}75$, $\text{FPR} \le 0{,}02$ et sélectivité $\ge 0{,}35$ `(illustratif)`.
- **Métrique et seuil** : $\text{TPR}$ sous évasion à $\text{FPR} \le 0{,}02$ fixé sur cas honnêtes appariés, plus sélectivité $\text{Sel}$.
- **Contrôle négatif explicite** : Tâche de contrôle de Hewitt et Liang (étiquettes permutées par type d'entité) + permutations aléatoires des coordonnées par couche.
- **Premier pas CPU et coût** : Prototypage sur `Pythia-410m` sur CPU (6 heures, ~3 € `(illustratif)`), puis passe d'extraction unique sur `OLMo-7B` / `Llama-3-8B` (**coût total : ~20 € `(illustratif)`**).
- **Issues de réfutation** : Respect conjoint des trois seuils réfute `H_B` ; échec sur $\text{FPR}$, $\text{TPR}$ ou sélectivité réfute `H_A`.

#### Action 6 — Audit spectral direct des poids et coordination implicite (Score : 187,5 `illustratif`)
- **`H_A`** `[HYPOTHÈSE]` : Sur un banc aveugle de $40$ `(illustratif)` points de contrôle ouverts propres contre modifiés (bras d'attaque séparé `[RAPPORTÉ]`) et de jeux symétriques à $K = 4$ `(illustratif)` choix permutés entre copies partageant leurs poids, l'indice d'asymétrie spectrale étalonné sur $(W_{OV}, W_{QK}, W_U)$ détecte les déclencheurs plantés avec $\text{TPR} \ge 0{,}75$ à $\text{FPR} \le 0{,}05$ ($\Delta\text{AUROC} \ge +0{,}25$ `(illustratif)` sur les normes scalaires) et prédit le taux de coordination implicite inter-copies avec une corrélation de Spearman $\rho \ge 0{,}70$ `(illustratif)`.
- **`H_B`** `[HYPOTHÈSE]` : La superposition poly-sémantique dilue les comportements conditionnels et les bris de symétrie de coordination à travers des centaines de directions singulières indiscernables du spectre de Marchenko-Pastur ($\text{TPR} < 0{,}75$ à $\text{FPR} \le 0{,}05$, ou $\Delta\text{AUROC} < +0{,}25$, ou $\rho < 0{,}70$ `(illustratif)`).
- **Métrique et seuil** : $(\text{TPR}, \text{FPR})$ sur le lot aveugle et $\rho$ de Spearman entre indice statique des poids et excès comportemental de coordination au-dessus de $1/K = 0{,}25$ `(illustratif)`.
- **Contrôle négatif explicite** : Poids permutés par blocs respectant les normes par tête et modèles propres affinés sur des domaines rares bénins.
- **Premier pas CPU et coût** : SVD tronquée par tranches sur CPU sur `Pythia-410m` puis `OLMo-7B` (5 heures CPU, ~3 € `(illustratif)`), suivie de la vérification comportementale sur GPU (**coût total : ~30 € `(illustratif)`**).
- **Issues de réfutation** : Atteindre les trois bornes réfute `H_B` ; tout manquement réfute `H_A`.

---

### 7.3 Limites résiduelles et inconnues ouvertes

1. **Superposition distribuée dans les poids** : si `H_B` l'emporte dans l'Action 6, **je ne sais pas** s'il existe un invariant calculable en temps polynomial sur les seuls poids statiques capable de distinguer un comportement conditionnel distribué sur de nombreuses couches d'une spécialisation syntaxique rare légitime sans connaître la loi d'entrée du déclencheur `[HYPOTHÈSE]`.
2. **Sabotage à fréquence inférieure à la contamination par pas** : dans l'Action 1, lorsque la contamination corrompt une fraction $\epsilon$ de *chaque* trajectoire de référence (et non une fraction $\epsilon$ des épisodes) avec $\epsilon \ge p_s$, la séparation statistique sans hypothèse structurelle sur la dépendance temporelle du saboteur devient mathématiquement non identifiable `[HYPOTHÈSE]`.
3. **Volume des archives pré-1900** : **je ne sais pas** si la taille et la couverture expérimentale des corpus numérisés antérieurs à 1900 `[VÉRIFIÉ]` suffisent pour tester à puissance statistique élevée la scission conceptuelle hors d'une dizaine de cas historiques documentés sans recourir massivement aux mondes synthétiques `[HYPOTHÈSE]`.
4. **Passage de l'invention syntaxique à la pertinence empirique** : l'Action 4 valide la compression formelle d'un alphabet existant, mais ne garantit pas à elle seule la proposition d'une expérience physique nouvelle lorsque les données brutes omettent entièrement la variable pertinente (biais d'inobservabilité instrumentale) `[HYPOTHÈSE]`.

FIN-DE-CELLULE