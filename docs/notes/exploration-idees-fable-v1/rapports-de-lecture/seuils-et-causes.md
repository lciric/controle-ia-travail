# Rapport de lecture — seuils et causes (22 novembre 2026)

Dossier des sources : `/tmp/claude-0/-home-user-controle-ia-travail/7225ef84-cf06-5367-97a0-6c2a4e600e2b/scratchpad/sources/seuils-et-causes/`. Tous les PDF ont été contrôlés par `file`/`pdfinfo`. « p. N » = page du fichier PDF ; numéro imprimé entre crochets s'il diffère.

## 1. Janson, Łuczak, Turova, Vallier 2012 — percolation d'amorçage sur G(n,p)
- Réf. : Janson S., Łuczak T., Turova T., Vallier T. (2012), « Bootstrap percolation on the random graph G_{n,p} », Annals of Applied Probability 22(5), 1989–2047. Tiré à part arXiv (pagination différente de la revue, dit p. 1).
- URL : https://arxiv.org/pdf/1012.3535 (v2) ; fichier `arxiv-1012.3535.pdf`, sha256 `b5e9b50bc1eb5752959f9b0f3f8c3bacef8873c961c768d6e3fe8d6979440d37`.
- Formules, p. 7 : (3.1) « tc := ((r − 1)!/(n p^r))^{1/(r−1)} » ; (3.2) « ac := (1 − 1/r) tc » ; « In particular, for r = 2, tc := 1/(np²) and ac := 1/(2np²). »
- Conditions sur p, p. 8 : « Theorem 3.1. Suppose that r ≥ 2 and n^{−1} ≪ p ≪ n^{−1/r}. »
- En dessous, p. 9 : « (i) If a/ac → α < 1, then A∗ = (ϕ(α) + op(1))tc » ; « in the subcritical case (i), we thus have w.h.p. A∗ < (r/(r − 1))a ≤ 2a, so the activation will not spread to many more than the originally active nodes. »
- Au-dessus, p. 9 : « (ii) If a/ac ≥ 1 + δ, for some δ > 0, then A∗ = n − op(n); in other words, we have w.h.p. almost percolation. » Percolation complète (iii) si et seulement si « np − (log n + (r − 1) log log n) → ∞ ».
- Résumé, p. 1 : « the final size of activation with a high probability is either n − o(n) or it is o(n). »
- Largeur de la fenêtre, p. 11 : « the precise threshold for a is a∗c ± O(√ac), with a width of the threshold of the order √ac ∼ √a∗c. » Théorème 3.6 (iii), p. 11 : si (a − a∗c)/√ac → y, « P(A∗ > n − b∗) → Φ((r − 1)^{1/2} y) ».
- Seuil en p à a fixé, p. 10 (Th. 3.4) : « For r = 2, (3.12) simplifies to pc = (2na)^{−1/2}. »
- Remarque des auteurs, p. 3 : « It might be a better model for the spread of rumors or other ideas or beliefs ».
- Statut : lu sur PDF, p. 1, 3, 7–11.

## 2. Processus de Galton-Watson
Deux textes en accès libre ; Otter 1949 et Dwass 1969 non obtenus (non essayés faute de temps).
- (A) Lalley S., « Branching Processes », notes de cours (Univ. of Chicago, Stat 312), sans date. URL : https://galton.uchicago.edu/~lalley/Courses/312/Branching.pdf ; fichier `lalley-branching.pdf`, sha256 `25b102199bc1c98901f6125a74bd61f02a98b40307d8dc45d8cdfd9bdc5ce8be`.
- (B) van der Hofstad R., « Random Graphs and Complex Networks, Volume I », version libre de l'auteur. URL : https://www.win.tue.nl/~rhofstad/NotesRGCN.pdf ; fichier `vdhofstad-rgcn1.pdf`, sha256 `7b0e2952beebdcb3bcc8c367174df7c04b369b2f219fa51ffbda21a2f4eb6dd3`.

| Point | Texte, page, citation | Statut |
|---|---|---|
| (a) extinction certaine ssi m ≤ 1 | (A) p. 5, Prop. 4 : « extinction is certain (that is, has probability one) if and only if the Galton-Watson process is critical or subcritical » (hors loi dégénérée en 1 : « Unless the offspring distribution is the degenerate distribution that puts mass 1 at k = 1 »). (B) p. 104 [86], Th. 3.1 : « η = 1 when E[X] < 1, while η < 1 when E[X] > 1. Further, η = 1 when E[X] = 1 and P(X = 1) < 1. » | lu sur PDF |
| (b) queue en n^(−3/2) au point critique | (B) p. 121 [103], (3.6.22), cas Poisson λ = 1 : « P∗1(T∗ = n) = (2π)^{−1/2} n^{−3/2} [1 + O(n^{−1})] » ; p. 122 [104] : « The above n^{−3/2} behavior is associated more generally with the distribution of the total progeny whose offspring distribution has finite variance (see, e.g., Aldous (1993, Proposition 24)). » La forme générale n'est donc qu'énoncée avec renvoi, démontrée ici pour le cas Poisson seulement. | lu sur PDF (général : par renvoi) |
| (c) survie ≈ 2(m−1)/σ² | Forme générale avec σ² **non trouvée**. Seul le cas Poisson (σ² = λ ≈ 1) : (B) p. 122 [104], (3.6.27) : « When λ ↘ 1, ζλ = 2(λ − 1)(1 + o(1)). » Voisin dans (A) p. 5, Prop. 5 (B) : au point critique, durée de vie « If µ = 1 then P{τ > n} ∼ 2/(σ² n) as n → ∞ » (c'est la queue de l'instant d'extinction, pas la survie près du seuil). | partiel |

## 3. Clauset, Shalizi, Newman 2009 — lois de puissance
- Réf. : Clauset A., Shalizi C. R., Newman M. E. J. (2009), « Power-law distributions in empirical data », SIAM Review 51(4). URL : https://arxiv.org/pdf/0706.1062 (v2, 2 février 2009) ; fichier `arxiv-0706.1062.pdf`, sha256 `b73aede05194f26b2446bd7003129f4d2caeaa5d9a0c47e5a652d3387ec2ac9f`.
- Méthode, p. 3 (Box 1) : « 1. Estimate the parameters xmin and α … 2. Calculate the goodness-of-fit … If the resulting p-value is greater than 0.1 the power law is a plausible hypothesis for the data, otherwise it is rejected. 3. Compare the power law with alternative hypotheses via a likelihood ratio test ». Test d'adéquation par la statistique de Kolmogorov-Smirnov (p. 15) et données synthétiques.
- Bilan, p. 23 : « The p-values in Table 6.1 indicate that 17 of the 24 data sets are consistent with a power-law distribution. The remaining seven data sets all have p-values small enough that the power-law model can be firmly ruled out. »
- p. 26 : « There is only one case—the distribution of the frequencies of occurrence of words in English text—in which the power law appears to be truly convincing » ; « The log-normal, on the other hand, is not ruled out for any of our data sets except the HTTP connections. In general, we find that it is extremely difficult to tell the difference between log-normal and power-law behavior. » ; « for almost a dozen data sets … the power-law with a cut-off is clearly favored over the pure power law. »
- p. 30 : les données sont « often compatible with other distributions as well, such as log-normal or stretched exponential distributions. »
- Statut : lu sur PDF, p. 3, 23, 26, 30.

## 4. Signes avant-coureurs
- Scheffer et al. 2009, Nature 461, 53–59 : pas de PDF en accès libre trouvé sur la revue, un dépôt ou un site d'auteur. Une copie existe sur une page de cours tierce (web.physics.rutgers.edu) ; non téléchargée, ce n'est pas une source autorisée par la consigne. Statut : non lu. Les passages ci-dessous viennent de Boettiger et Hastings, qui le citent.
- Réf. : Boettiger C., Hastings A. (2012), « Early warning signals and the prosecutor's fallacy », Proc. R. Soc. B 279. Lu dans la **prépublication** arXiv 1210.1204v1 (3 oct. 2012, titre « Early Warning Signals and the Prosecutor's Fallacy »), qui peut différer de la version publiée. URL : https://arxiv.org/pdf/1210.1204 ; fichier `arxiv-1210.1204.pdf`, sha256 `8be911bc2b4f37d7e43bd7667ceb2b7e6d47b3a6f3693848930efdc8bda16685` (pdftotext signale une table xref reconstruite ; le texte est lisible).
- Signes avant-coureurs, p. 2 : « Two of the most commonly used are a pattern of increasing variance (Carpenter and Brock, 2006) and a pattern of increasing autocorrelation (van Nes and Scheffer, 2007) ».
- Biais, p. 1 (résumé) : « This difference arises by conditionally selecting systems known to experience a transition of some sort and failing to account for the bias this introduces … By analysing simulated systems that have experienced transitions purely by chance, we reveal an elevated rate of false positives in common warning signal statistics. »
- Chiffres, p. 4 : « We simulated 20,000 replicates of a stochastic individual-based birth-death process with an Allee threshold » ; p. 5 : « In this time window 266 of the 1,000 replicates experience population collapse. » **Incohérence interne (20 000 contre 1 000) dans la prépublication**, à vérifier sur la version publiée. Statistique : tau de Kendall sur la variance et l'autocorrélation des 266 répliques (p. 5).
- p. 7 : « such conditionally selected examples are more likely to show signs associated with an early warning … This increases the risk of false positives ». Le texte lu **ne donne aucun taux de fausses alertes chiffré** ; la différence est montrée par des distributions de tau (Fig. 2, p. 14).
- Méthode fondée sur un modèle, p. 6 : « None of the estimates across the 266 simulations differed from zero … the model-based estimation shows no evidence of bias » ; réserve p. 9 : « This should not however be taken as evidence that the model-based approach is immune to the bias of the Prosecutor's Fallacy. »
- Remède, p. 9 : « Experimental procedures avoid the hazard of the Prosecutor's fallacy by generating a complete sample of replicates ».
- Statut : lu sur PDF (prépublication), p. 1, 2, 4–7, 9.

## 5. Guimerà, Uzzi, Spiro, Amaral 2005 — assemblage des équipes
- La version Science 308, 697–702 n'a pas été obtenue. PubMed Central (PMC2128751) renvoie une page reCAPTCHA (refus, non contourné). Europe PMC fullTextXML renvoie une erreur 500. La copie amarallab.github.io est une page HTML et non un PDF.
- Lu : le **manuscrit** de décembre 2004, sur le site de B. Uzzi (Kellogg), 17 pages, « TeX output 2004.12.17 ». Il peut différer de la version publiée. URL : https://www.kellogg.northwestern.edu/faculty/uzzi/ftp/guimera_et_al_science_rd_12-17-04.pdf ; fichier `guimera-uzzi-draft-2004.pdf`, sha256 `79f7a77c2f6e0f594fcafbe57955e922975278ad47252f242c361f920adecb1b`.
- (a) Transition, p. 5–6 : « We find that the network goes through a percolation transition at a critical line pc(m, q). That is, the system experiences a sharp transition from a multitude of small clusters to a situation in which one large cluster, comprising a large fraction S of the individuals, emerges—the so-called giant component » ; p. 15 (Fig. 3) : « for any value of q, the model displays a percolation transition as the fraction p of incumbents increases from 0 to 1, and that the critical fraction pc depends on q ». Valeurs par champ, p. 15 (Tableau 1) : S = 0,70 pour les comédies musicales de Broadway, 0,68 en psychologie sociale, 0,75 en écologie, 0,92 en astronomie.
- (b) Lien avec la qualité, p. 8 : « We found that p was positively correlated with impact factor, whereas q was negatively correlated with impact factor, for both ecology and social psychology » ; S aussi associé à l'impact ; « Surprisingly, neither p, q, or S were significantly correlated with impact factor in astronomy. » Aucun coefficient chiffré dans le texte ; les rs sont dans la Fig. 5 (non lue en image).
- (c) Nature de la preuve, p. 17 (légende Fig. 5) : « use the Spearman rank-order correlation coefficient rs to determine significant correlations. A correlation is considered significant if the probability P(rs) is smaller than 5%. » Corrélation entre revues, facteur d'impact comme indice : « We used each journal's impact factor as a proxy for the quality of teams' output » (p. 7–8). D'après le Tableau 2 (p. 16), on compte 7 revues en psychologie sociale, 10 en écologie et 6 en astronomie (décompte fait par moi sur le tableau). Les données viennent de Web of Science, 1955–2004.
- Statut : lu sur PDF (manuscrit), p. 1, 5–8, 15–17.

## 6. Évaluation hors ligne à partir de journaux
**Li, Chu, Langford, Wang 2011**
- Réf. : Li L., Chu W., Langford J., Wang X. (2011), « Unbiased Offline Evaluation of Contextual-bandit-based News Article Recommendation Algorithms », WSDM 2011. URL : https://arxiv.org/pdf/1003.5956 ; fichier `arxiv-1003.5956.pdf`, sha256 `ea72ce425888ae8adba1957a9f0acbef7ed0dc232a52982b9e7424d7ef73ae19`.
- Condition, p. 3 : « assuming that the individual events are i.i.d., and that the logging policy chose each arm at each time step uniformly at random ».
- Non-biais, p. 4, Théorème 1 : « For all distributions D of contexts and payoffs, all algorithms A, all T, all sequences of events hT, and all stream S containing i.i.d. events from a uniformly random logging policy and D, we have Pr_{A,D}(hT) = Pr_{Policy_Evaluator(A,S)}(hT). »
- Coût, p. 4 : « each event is retained by this algorithm with probability exactly 1/K ».
- Extension, p. 9 : « may be extended to work for data collected by any random policy with rejection sampling, which enjoys similar unbiasedness guarantees, but reduces the data efficiency ».
- Écart à la théorie, p. 6 : « the setting differs in some ways from the i.i.d. assumption made in our theorems ».
- Statut : lu sur PDF, p. 3, 4, 6, 9.

**Dudík, Langford, Li 2011**
- Réf. : Dudík M., Langford J., Li L. (2011), « Doubly Robust Policy Evaluation and Learning », ICML 2011. URL : https://arxiv.org/pdf/1103.4601 (v2) ; fichier `arxiv-1103.4601.pdf`, sha256 `fd0c6570334e8479ba91e0c287a111d90ca145a473c00b8b224b7b47ddf9b010`.
- Ce qu'il faut journaliser : le texte **ne pose pas** l'obligation de journaliser la probabilité. Il suppose une politique passée inconnue et une probabilité estimée. p. 2 : « The policy chooses an action a ∼ p(a | x, h) … Note that neither the distribution D nor the policy [p is known] » (fin de phrase coupée par la page). p. 3 : « IPS forms an approximation p̂(a | x, h) of p(a | x, h) » et « Since we typically have a good (or even accurate) understanding of the datacollection policy, it is often easier to obtain a good estimate p̂ ».
- Double robustesse, p. 1 : « if either one of the two estimators (in DM and IPS) is correct, then the estimation is unbiased ». p. 3, Th. 1 : le biais vaut « |E_S[V̂DR] − V^π| = E_S[(1/|S|) Σ ∆δ] » ; « if either ∆ ≈ 0, or δ ≈ 0, the expected value of the doubly robust estimator will be close to the true value ». Réserve, p. 3 : « In practice, it is rare to have an accurate estimation of either ̺ or p. »
- Variance, p. 3 : « IPS typically has a much larger variance, due to the range of the random variable increasing. The issue becomes more severe when p(a | x, h) gets smaller. » p. 4 (Th. 2) : le terme de variance « can be much larger for IPS if p(π(x) | x) ≪ 1 ». p. 1 : la variance est grande « especially when the past policy differs significantly from the policy being evaluated. »
- Gain mesuré, p. 7 : « the DR estimator often reduces the rmse by a fraction between 10% and 20%, and on average by 13.6% » (expérience Yahoo, estimateur de récompense raisonnable).
- Statut : lu sur PDF, p. 1–4, 7.

## 7. Bettencourt, Kaiser, Kaur 2009
- DSpace du MIT (1721.1/50230) : le lien de fichier (`/bitstreams/bf8ce93f-…/download`) renvoie « Web Firewall · 429 … Log in … ». C'est un refus ; il n'a pas été contourné. Aucune prépublication arXiv de ce même article n'a été trouvée : arXiv 1504.00319, de Bettencourt et Kaiser, est un autre article (2015). Statut : non lu. D'après la page de résultats de recherche, l'article porte sur huit champs et sur la taille relative de la plus grande composante, et la fusion froide n'y fait pas la transition. Ces éléments ne sont pas vérifiés.

## Non vérifié
- Point 2 : Otter 1949 et Dwass 1969 non obtenus. La formule générale de survie ≈ 2(m−1)/σ² n'a pas été trouvée dans les textes lus, seulement le cas Poisson 2(λ−1). La queue en n^(−3/2) n'est démontrée que pour le cas Poisson ; le cas général l'est par renvoi à Aldous 1993, non lu.
- Point 4 : Scheffer et al. 2009 non lu (aucun PDF de source autorisée). Boettiger et Hastings 2012 : version publiée non lue ; aucun taux de fausses alertes chiffré dans la prépublication ; incohérence entre 20 000 et 1 000 répliques non résolue.
- Point 5 : version publiée dans Science non lue (reCAPTCHA de PubMed Central, erreur d'Europe PMC). Valeurs rs de la Fig. 5 non lues. Le décompte des revues est de moi, d'après le Tableau 2 du manuscrit.
- Point 6 : versions publiées (WSDM, ICML) non comparées aux versions arXiv.
- Point 7 : texte intégral non obtenu (refus 429 de DSpace). Les huit champs, la forme de la transition, les réserves et la présence du mot « ignition » ne sont pas vérifiés.
