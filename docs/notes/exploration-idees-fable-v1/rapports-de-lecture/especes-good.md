# Statistique des espèces (Good–Toulmin et suites) : mesurer, prédire, choisir la source, arrêter

Dossier des sources : `scratchpad/sources/especes-good/`, empreintes complètes dans `SHA256SUMS.txt` (préfixes de 16 signes ci-dessous). « fp » = page du fichier PDF ; « imp. » = page imprimée.

## Corrections à la question (ce que les textes disent, pas la mémoire)
- Good et Toulmin notent la taille du second échantillon **λN**, pas (1+t)N : l'échantillon agrandi fait λN au total, donc t = λ − 1. Leur seuil de difficulté est **λ > 2** (t > 1), et ils pensent pouvoir aller jusqu'à **λ < 5** grâce à la méthode d'Euler, sans borne d'erreur.
- Le papier de 2021 sur le risque restant est de **Böhme, Liyanage, Wüstholz** (et non Pham).
- « Entropic » (2020) **n'emploie pas** l'estimateur de Good et Turing pour répartir l'effort : il emploie une entropie de Shannon locale par graine, estimée avec un lissage de Laplace (ajout de un).
- Le titre de Li et al. est « **Evaluating** the Unseen Capabilities… » (arXiv 2506.02058).
- Chao et Jost 2012, Rasmussen et Starr 1979 et Dahan et Mendelson 2001 **n'ont pas été lus** (voir la liste « non vérifié »). Les deux premiers sont rapportés par l'intermédiaire de Chao et al. 2014.

## 1. Good et Toulmin 1956, Biometrika 43:45–63
Fichier `goodtoulmin.pdf` (a3244fb0850bccb7), copie gwern.net mal nommée « 1953-good.pdf » (en-tête : téléchargée d'Oxford Academic). **Lu sur PDF.**
- **Formule (24), fp6 / imp. 50** : « in the case of an enlarged sample, the number of new species expected is approximately (λ−1)n₁ − (λ−1)²n₂ + … ». Avec t = λ−1 : **U ≈ t·n₁ − t²·n₂ + t³·n₃ − …**. La couverture attendue de l'échantillon agrandi est donnée par la formule (22), même page : 1 − (1/N)[n₁ − 2(λ−1)n₂ + 3(λ−1)²n₃ − …].
- **Hypothèses** (fp1 / imp. 45) : un échantillon aléatoire tiré d'une « infinite population » ; le nombre total d'espèces s n'est pas nécessaire. Les formules (23) et (24) « can be proved directly without assuming s to be finite » (fp6). Lissage des nᵣ recommandé, mais pour un échantillon agrandi, nᵣ « should not be replaced by n′ᵣ … at any rate when λ is not large » (fp5 / imp. 49).
- **Avertissement de divergence** (résumé, fp1) : « when λ > 2, this variance becomes in general very large, so that the estimate is useless without some modification… partly overcome, at least for λ < 5, by using Euler's method ». En fp3 / imp. 47 : « If λ>2… the factor (λ−1)ⁱ increases rapidly with i… We have not, however, been able to justify this procedure by finding a useful error term ».
- **Usage de décision affiché** (fp2 / imp. 46) : « Results of this type may enable us to decide whether it is worth enlarging our sample, and to what extent ». Exemple de l'entomologiste : il décidera « largely on the expected number of new species ».
- **Ce que le texte ne dit pas** : rien sur un tirage adaptatif, rien sur des sources multiples, rien sur la valeur des espèces.

## 2. Efron et Thisted 1976, Biometrika 63:435–447
Fichier `efron1976.pdf` (0c70fae0baec4bb8), copie JSTOR. **Lu sur PDF.**
- **Modèle** (fp2 / imp. 436) : chaque espèce entre dans le piège selon un processus de Poisson de moyenne λₛ ; l'indépendance entre espèces n'est pas requise dans la plupart des calculs. « Assumption (ii) is crucial. It says essentially that the time period [−1, 0] is typical of the whole period » ; si les œuvres nouvelles étaient des lettres d'affaires, « we would not expect our results to be valid ».
- **Estimateur** (2.4), fp3 / imp. 437 : Δ̂(t) = n₁t − n₂t² + n₃t³ − … ; pour Shakespeare, avec t = 1, **Δ̂(1) = 11 430**, écart type 178. « Unfortunately (2.4) is useless for values of t larger than one. »
- **Lissage** (§ 4–5, fp5–9) : transformation d'Euler tronquée à x₀ termes, avec x₀ = 9 retenu. À t = 10, Δ̂₉(10) = 45 188 ± 3 994, et Δ̂₁₉(10) a une variance « huge » (fp8–9 / imp. 442–443). La loi binomiale négative de Fisher s'ajuste « extraordinarily well » mais « we know [it] must ultimately fail » (fp5 / imp. 439).
- **Bornes inférieures** par programmation linéaire (§ 6–7). Contre-exemple : 10⁶ mots de fréquence 10⁻⁶ n'auraient presque aucun effet sur les données (fp9 / imp. 443).
- **Conclusions** (fp12 / imp. 446) : « Δ(∞) = 35000 is a reasonably conservative lower bound » ; « Without a parametric model the data give very little additional information for t larger than 10. » La borne dépend d'un choix c = 1 que les auteurs disent eux-mêmes « may seem optimistic ».
- **Ce que le texte ne dit pas** : aucune borne supérieure n'est possible (« No upper bound is possible », fp1).

## 3. Orlitsky, Suresh, Wu 2016 (arXiv 1511.07428 v3 ; PNAS 113)
Fichier `ost2016.pdf` (68a419237a6fc9e2). **Lu sur PDF (arXiv)** ; pages de la revue PNAS non vérifiées.
- **Cadre** (fp2) : n tirages indépendants d'une loi p inconnue ; U = nombre de symboles nouveaux parmi m = t·n tirages supplémentaires, « from the same distribution ».
- **Good et Toulmin** (fp3, éq. 1) : U^GT = −Σ(−t)ⁱΦᵢ. Pour t ≤ 1, E(U^GT − U)² ≲ nt². Pour t > 1, « U^GT does not approximate U at all ».
- **Estimateur lissé** (fp5, éq. 3–4) : troncature en un rang aléatoire L, U^L = −Σ(−t)ⁱ P(L ≥ i) Φᵢ. Le lissage binomial L ~ Bin(k, 1/(1+t)) **redonne l'estimateur d'Efron et Thisted** (fp4–5).
- **Théorème 1** (fp6) : erreur quadratique normalisée par (nt)² ≲ n^(−1/t) (lissage de Poisson). Le lissage binomial avec q = 2/(t+2) converge le plus vite.
- **Théorème 2** : borne inférieure minimax ≳ n^(−c′/t). **Corollaire 1** : l'horizon maximal t ≍ log n / log(1/δ). Le résumé dit : « all the way up to t proportional to log n ».
- **Hypothèses** : garanties « uniformly for all distributions » et pour les modèles multinomial, Poisson, hypergéométrique et Bernoulli produit (résumé, fp1). Tirages indépendants et identiquement distribués.
- **Ce que le texte ne dit pas** : l'erreur est normalisée par nt, le maximum possible. Une erreur « faible » peut donc rester grande devant un U réel petit, ce qui est le cas des queues pauvres. Aucune garantie sous tirage adaptatif.

## 4. Bubeck, Ernst, Garivier 2013, JMLR 14:601–623
Fichier `bubeck.pdf` (2e0fd49c47df5ce4). **Lu sur PDF.**
- **Problème** (fp1 / imp. 601) : un ensemble A d'éléments intéressants dans X, accessible par K « experts » probabilistes ; chaque requête tire indépendamment selon une loi fixe Pᵢ. But : « discovering rapidly as many elements of A as possible ». Motivation : l'analyse de sécurité d'un réseau électrique, avec des contingences dangereuses rares (fp2).
- **Estimateur** (fp5 / imp. 605) : R̂ₙ = Uₙ/n, la fraction des éléments intéressants vus une seule fois. **Proposition 1** : avec probabilité au moins 1−δ, R̂ₙ − 1/n − (1+√2)√(log(4/δ)/n) ≤ Rₙ ≤ R̂ₙ + (1+√2)√(log(4/δ)/n), « independently of the underlying distribution ».
- **Algorithme Good-UCB** (fp6) : interroger l'expert qui maximise R̂ + C√(log(4t)/nᵢ).
- **Garanties** sous l'hypothèse (i) de supports disjoints. **Théorème 4** (fp7) : E[F*(t) − F^UCB(t)] ≤ 17√(Kt log t) + 20√(Kt) + K + K log(t/K). **Théorème 5** (fp9) : le temps d'attente de Good-UCB est proche du temps de l'oracle. L'optimalité « macroscopique » exige en plus (ii) des supports finis de même taille et (iii) des lois uniformes (fp3–4). Le tirage uniforme entre experts est « macroscopically suboptimal » sauf si les experts ont autant d'éléments intéressants.
- **Ce que le texte ne dit pas** : rien de démontré si les supports se recouvrent (seulement des essais) ; les lois des experts sont fixes (pas d'expert qui apprend) ; tout élément de A a la même valeur.

## 5. Böhme et le test logiciel
**STADS**, TOSEM 27(2), 2018 : fichier `stads.pdf` (d87885d24d972874), arXiv 1803.02130 v2. **Lu sur PDF.**
- **Modèle multinomial** (fp16–17) : chaque entrée appartient à une seule espèce ; probabilités pᵢ fixes. Les auteurs relèvent que le modèle multinomial suppose que l'échantillonnage « does not substantially alter the probabilities ».
- **Probabilité de découverte** (fp18) : Û(n) = f₁/n. **Argument de risque restant** (fp18–19) : si aucune erreur n'a été vue, Û borne le risque, « modulo the dynamic analyzer's capability to identify a error-exposing input ».
- **Exemple chiffré** (fp10) : Û = 7·10⁻⁶ après 12 h de fuzzing (f₁ = 447, n = 63,6·10⁶).
- **Extrapolation de couverture** (fp12) : Chao et Jost « would suggest to extrapolate only within twice the sample size ». Les fuzzers adaptatifs violent l'hypothèse ; l'étude « préliminaire » porte sur 6 programmes. Le biais d'extrapolation est d'abord fortement positif, puis reste dans ±2 % après 18 h (fp31).

**Risque restant**, ESEC/FSE 2021 : Böhme, Liyanage, Wüstholz ; fichier `residual.pdf` (cae1853be25ef867) ; imp. = fp + 229. **Lu sur PDF.**
- **Abstract** (fp1) : les estimateurs du fuzzing boîte noire « systematically and substantially under-estimate the true risk. An engineer—who stops the campaign when the estimators purport a risk below the maximum allowable risk—is vastly misled ». Cause : le « adaptive bias ».
- **Correctifs** (fp2) : estimateurs « reset » et « mean local ». L'extrapolation est en loi de puissance, R² ≈ 97 % sur 4 programmes sur 6 (fp10).
- **Résultat chiffré** (fp9) : l'estimateur de Good et Turing classique peut être « up to four orders of magnitude smaller than the true discovery probability ».
- **Banc** : 6 programmes de FuzzBench, 20 campagnes, jusqu'à 7 jours chacun (fp8 et fp10).

**Entropic**, ESEC/FSE 2020 : Böhme, Manès, Cha ; fichier `entropic.pdf` (b0738ad8b5ddfb5c) ; imp. = fp + 969. **Lu sur PDF.**
- Ordonnancement d'énergie par entropie locale de chaque graine, estimée par lissage de Laplace (fp6). Pas de Good et Turing.
- 263 programmes ; « more than twice as fast as LibFuzzer for half the programs » (fp8).
- Déploiement : « now runs on more than 25,000 machines » (fp1). C'est l'affirmation des auteurs, non vérifiée de façon indépendante ici.

## 6. Böhme et Paul 2016, IEEE TSE 42(4):345–360
Fichier `bohmepaul.pdf` (f86e3f4c384dcb96), prépublication acceptée. **Lu sur PDF** ; pagination de la revue non vérifiée.
- **Énoncé** (fp5) : « Given a degree of confidence x, we find that the sampling cost c of S0 must be below (ex − ex²)⁻¹ units of time in order for S0 to remain more efficient than R ». La borne vaut donc c < 1/(e·x(1−x)). Exemple : pour x = 90 %, le test systématique doit coûter « much less than five times » le test au hasard.
- **Hypothèses** (fp4) :
  - R tire uniformément avec remise ;
  - S0 tire une partition « error-based » non encore découverte, une entrée par partition ;
  - coût c constant.
- Les essais montrent que S0 « may need to be significantly faster than our bounds suggest » (fp1).

## 7. Chao et Jost 2012, Ecology 93:2533–2547
Le site de l'éditeur a refusé l'accès (erreur 403). **Non lu.** Rapporté par Chao et al. 2014 (Ecological Monographs 84), fichier `chao2013harvard.pdf` (4affc7ae357e3201), copie du dépôt de Harvard, fp26–27 (manuscrit p. 25–26) :
- **Raison de comparer à couverture égale** : la richesse attendue à couverture égale « satisfies a replication principle or doubling property, which the expected species richness for equal sample size does not obey ».
- **Couverture estimée** : Ĉ(n) = 1 − (f₁/n)·[(n−1)f₁ / ((n−1)f₁ + 2f₂)]. L'extrapolation est « reliable if m* < n ».
- **Fiabilité de la richesse extrapolée** : seulement jusqu'au « double or triple » de l'échantillon, car l'estimateur asymptotique (Chao1) n'est qu'une borne inférieure (fp21).

## 8. Rasmussen et Starr 1979, JASA 74
L'éditeur a refusé l'accès (erreur 403). **Non lu.** Rapporté par Chao et al. 2014, fp27 : « An optimal stopping theory derived by Rasmussen and Starr (1979) specifies that sampling stops when sample coverage reaches a predetermined value ». C'est une source seconde, non opposable.

## 9. Idées
**Kornish et Ulrich**, Management Science 57:107–128, 2011 : fichier `kornish.pdf` (e9c74b2b1c29ef20), document de travail de juillet 2010 (SSRN 1503103), **pas la version publiée**. **Lu sur PDF.**
- **Modèle** (fp7) : p(n) = e^(−an), u(n) = (1/a)(1−e^(−an)), **T = 1/a**. Il repose sur un modèle capture-recapture à idées « equally likely » (Lincoln–Petersen).
- **Définition de « identique »** : seuil de jugement humain, majoritaire (au moins 50 % des juges) ou consensuel (au moins 70 %) (fp14).
- **Chiffres** (seuil consensuel, Tableau 4, fp19) : T entre 1 103 (technologies de classe) et 2 735 (produits web), avec des intervalles larges (par exemple 1 205 à 3 704 pour un T de 2 165). Si l'on relâche l'hypothèse d'idées également probables, T augmente un peu (fp21).
- **Réserve des auteurs** (fp19) : « In a real sense, the number of ideas is not finite » ; T dépend du seuil d'identité.

**Girotra, Terwiesch, Ulrich**, Management Science 56:591–605, 2010 : fichier `girotra.pdf` (0c8c3fa0364556c2), manuscrit révisé. **Lu sur PDF.**
- **Théorème 1** (annexe, fp35) : E[Mₙ] ≤ E[Mₙ₊₁] (le meilleur de n tirages indépendants croît avec n).
- **Lemme 1** : si la qualité suit une loi des valeurs extrêmes généralisée (μ, σ, ξ), le maximum de n suit μ′ = μ + σ(n^ξ − 1)/ξ, σ′ = σn^ξ, ξ′ = ξ. La forme de la queue (ξ) fixe donc le gain d'un tirage de plus.
- **Ce que le texte ne contient pas** : la règle du nombre optimal de tirages selon le coût, qui est attribuée à **Dahan et Mendelson 2001**, non lu.

## 10. Modèles de langage
**Kalai et Vempala** (arXiv 2311.14648 v3) : fichier `kalai.pdf` (a481ef538d58b39f). **Lu sur PDF.**
- **Énoncé** (fp4) : pour des faits « arbitraires », un modèle calibré hallucine au moins au taux (estimateur des « monofaits », c'est-à-dire de Good et Turing) − mauvaise calibration − (terme de ratio faits/faussetés) − O(1/√n).
- **Hypothèses** : tirages indépendants et identiquement distribués ; au plus un fait par document ; génération sans invite ; « regularity » de la loi des faits non observés.
- **Limite affichée** : rien n'oblige à halluciner sur les faits vus plusieurs fois ou sur les faits systématiques (fp1).

**Li, Xin, Long, Su 2025** (arXiv 2506.02058 v1) : fichier `knowsum.pdf` (c0d8898001e50971). **Lu sur PDF.**
- **Méthode** : pipeline génération → vérification → regroupement → prévalences → estimateur de Good et Toulmin lissé (fp4–5), avec t = 100, k ∈ {6, 8, 10} choisi par validation croisée (fp7).
- **Validation sur données retenues** (fp11) : seulement jusqu'à t = 3.
- **Résultat** (fp3) : « LLMs typically express only 20-50% of their estimated internal knowledge ».
- **Limites des auteurs** (fp14) : le cadre ne vaut que pour un savoir « well-defined, countable ».
- **Ma remarque**, non écrite par les auteurs : t = 100 dépasse l'horizon démontré par Orlitsky et al., qui est de l'ordre de log n ≈ 13 pour n = 6·10⁵. Le chiffre de 20 à 50 % repose donc sur une extrapolation non garantie.

## 11. McAllester et Schapire 2000, COLT
Fichier `mcallester.pdf` (b3d26de6128bc56a). **Lu sur PDF.**
- **Théorème 1 et corollaire 2** (fp2) : |E[M₀] − E[G₀]| ≤ 1/m.
- **Borne de l'abstract et de l'introduction** (fp1) : M₀ ≤ G₀ + O(√(ln(1/δ)/m)) avec probabilité 1−δ, « independent of the underlying distribution ». La borne inférieure est plus faible.
- **Théorème 3** (fp2) : pour les masses Mₖ en général, l'écart se resserre au rythme O(ln m/√m).
- **Hypothèses** : tirages indépendants selon une loi fixe P.

## 12. Recherche récente sur les sorties de modèles (deux textes lus)
- **Avestimehr, Duffy, Médard, « NOVA » (arXiv 2605.15219, mai 2026)** : fichier `nova.pdf` (24c17c23570c7b27). **Lu sur PDF**, fp1, 3, 6. Le texte modélise la boucle « générer, vérifier, accumuler, réentraîner » comme un échantillonnage adaptatif. Énoncé clé (fp6) : Good–Turing « estimates this local batch-unseen mass, which diagnoses repetition or loss of diversity under the current generator. It is distinct from M_new, the historically undiscovered valid mass that drives cumulative discovery ». Il décrit aussi un piège de contamination quand la vérification est imparfaite. C'est une prépublication théorique, non contre-lue ici.
- **Colombi, Beraha, Painsky, Favaro (arXiv 2601.20320, 2026)** : fichier `colombi.pdf` (fb3a5890cba7a27d). **Lu sur PDF**, fp1–4. Le texte donne des bornes de confiance non asymptotiques sur la **plus grande probabilité non vue**, et des règles d'arrêt séquentielles à garantie en échantillon fini : arrêter quand Uₙ(α) ≤ ε.
  - Résultat d'impossibilité : en alphabet non borné, aucune borne indépendante des données n'est valide uniformément.
  - Les règles d'arrêt usuelles sont « asymptotic or oracle-based » et « fragile » face à une contamination qui crée des catégories rares artificielles (fp2).
  - Le texte cite Noorani et al. 2025 (combien de répétitions d'une requête à un modèle de langage pour voir toutes ses réponses), **non lu**.
- **Repérés, non lus** :
  - McCabe et al. 2025 (arXiv 2509.14478) : taille de l'« alphabet sémantique » corrigée par la couverture ;
  - Eriksson 2026 (arXiv 2602.08769) : intervalles de prédiction pour Good–Toulmin ;
  - Pal et al. 2026 (arXiv 2604.05057) : « blind-spot mass ».
- **Aucun emploi trouvé** sur les attaques d'équipes rouges automatiques ni sur les idées de recherche générées. Une zone vierge est une question : la recherche a été brève, deux requêtes.

## Ce que ces outils permettent de décider, et ce qu'ils ne mesurent pas
1. **Décider** : la masse manquante (f₁/n) mesure la probabilité qu'un tirage de plus soit nouveau, à O(1/√n) près sans hypothèse sur la loi, si les tirages sont indépendants et la loi fixe. C'est un critère d'arrêt sur seuil de couverture (Rasmussen et Starr, via Chao et al. ; Colombi et al.).
2. **Prédire** : le nombre de nouveautés est fiable jusqu'à doubler l'échantillon (Good et Toulmin). Lissé, il vaut au plus jusqu'à environ log n fois l'échantillon (Orlitsky et al.). Au-delà, seule une borne inférieure ou un modèle paramétrique répond.
3. **Choisir la source** : Good-UCB démontre un choix proche de l'oracle entre sources à lois fixes et supports disjoints. Comparer des sources à couverture égale, pas à taille égale (Chao et Jost, relayé).
4. **Non mesuré, la dépendance** : sous tirage adaptatif (fuzzing en boîte grise, générateur réentraîné, agent qui apprend), l'estimateur sous-estime le risque, jusqu'à 10⁴ fois (Böhme et al. 2021). Il ne voit que la diversité du lot courant (NOVA).
5. **Non mesuré, la valeur** : toute espèce compte pour un. La valeur de l'inconnu exige un autre modèle, par exemple celui des valeurs extrêmes (Girotra et al.) ; et « espèce » dépend d'un seuil d'identité (Kornish et Ulrich ; regroupement chez Li et al.).
6. **Non mesuré, ce que la source ne peut pas produire** : la masse est relative à la loi de la source. Une espèce de probabilité nulle pour cette source reste invisible à toute statistique tirée d'elle (Efron et Thisted : aucune borne supérieure ; STADS : « modulo » l'oracle).

## Non vérifié
- **Chao et Jost 2012** (refus de l'éditeur, 403) : seulement relayé par Chao et al. 2014.
- **Rasmussen et Starr 1979** (refus de l'éditeur, 403) : règle d'arrêt connue seulement par une phrase de Chao et al. 2014.
- **Dahan et Mendelson 2001** : PDF non trouvé, certificat du site de l'auteur refusé. Le nombre optimal de tirages selon la queue de la loi n'est pas vérifié.
- **Kornish et Ulrich** : chiffres pris dans le document de travail de 2010, pas dans la version publiée de 2011.
- **Pagination des revues** : pour Orlitsky et al. (PNAS), Böhme et Paul (TSE) et STADS (TOSEM), seules les pages des prépublications sont citées.
- **Déploiement d'Entropic** sur plus de 25 000 machines : affirmation des auteurs, sans source indépendante.
- **Textes repérés mais non lus** : Noorani et al. 2025, McCabe et al. 2025, Eriksson 2026, Pal et al. 2026.
- **Kalai et Vempala** : le dernier terme de la borne de la fp4 (6/√n ou 7/√n) est illisible dans l'extraction du texte ; le corollaire 1 n'a pas été relu.
