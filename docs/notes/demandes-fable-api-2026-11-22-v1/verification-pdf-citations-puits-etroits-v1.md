# Vérification sur PDF de huit citations (puits étroits) — v1

Heure : 2026-11-22 14:37 UTC (`date -u`).
Règle suivie : R7 (aucun énoncé opposable sans PDF empreinté, page citée).
Dossier des PDF : `docs/sources/pdf-puits-etroits-v1/` ; chaque PDF a son compagnon `.sha256`.
Lecture : `pdftotext` (poppler). Aucun script lancé depuis le dossier des PDF.

## Réserve générale sur la provenance

Trois PDF ne viennent pas de l'éditeur ni de l'auteur. Ce sont des copies hébergées par des pages de cours d'universités. Leur licence n'est pas vérifiée. La session mère décide de les garder ou non avant le commit :
- Dorfman 1943 : scan JSTOR (avec la page de garde JSTOR, usage personnel) hébergé par un cours de l'université de Tampere. L'article est en accès libre chez l'éditeur (Project Euclid), mais Project Euclid bloque le téléchargement automatique (pare-feu Incapsula).
- Nisan et Szegedy 1994 : PDF de l'éditeur (Birkhäuser) hébergé sur la page d'un enseignant de l'université de Vilnius, qui n'est pas un des auteurs.
- Trakhtenbrot 1984 : PDF de l'éditeur (IEEE, article payant) hébergé sur le site d'un cours de l'université de Virginie.

Hesterberg 1995 vient de l'archive de la revue Technometrics tenue par le département de statistique de Carnegie Mellon. Woodard et al. 2009 vient du miroir EMIS de la revue (accès libre). Rao et Regev vient d'arXiv. La traduction de Levin vient de la page personnelle de Lance Fortnow.

Accès refusés, non contournés : Project Euclid (Halmos, et Dorfman chez l'éditeur) ; SIAM (Gillman, payant, code 403) ; dépôt du MIT (thèse de Gillman, pare-feu, code 429) ; Elsevier (Blumer et al., payant) ; mathnet.ru (original russe de Levin, page HTML au lieu du PDF). Une tentative par l'archive du web pour Project Euclid a été refusée par la garde de la session ; elle n'a pas été reprise.

---

## 1. Hesterberg 1995

- Référence : Tim Hesterberg, « Weighted Average Importance Sampling and Defensive Mixture Distributions », Technometrics, vol. 37, n° 2, mai 1995, p. 185-194. DOI 10.1080/00401706.1995.10484303.
- Source : https://www.stat.cmu.edu/technometrics/90-00/vol-37-02/v3702185.pdf
- Chemin : `docs/sources/pdf-puits-etroits-v1/hesterberg-1995-defensive-mixture-v1.pdf`
- Empreinte : `b6871553f52d96e8831fceeadfb08f3d208bc910af5c09c9e762ff4a5ea1c217`
- Page : 189 de la revue (page 5 du PDF), section 6.1, équations (6.1) et (6.2).
- Citations exactes :
  - (6.1) : « g_λ(x) = λf(x) + (1 − λ)g₀(x) » (λ entre 0 et 1, f la loi cible).
  - « First, the weight function is bounded by 1/λ because W(x) = f(x)/g_λ(x) ≤ f(x)/(λf(x)) = 1/λ. » (le scan rend λ par « h »).
  - « Second, the asymptotic variance of any of the equivalent estimates is guaranteed no worse than 1/λ times the variance of the simple Monte Carlo estimate. »
  - « The term "defensive" refers to the use of f as one component of the mixture to bound W. »
- Verdict : **confirmée en partie.**
- Écarts :
  - Chez Hesterberg, la composante défensive est la loi cible f elle-même. Le rapport borné est f/g ≤ 1/λ. Transposé à q = (1 − ε)·p + ε·u, c'est **u/q ≤ 1/ε** qui est borné (si u joue le rôle de la cible), pas p/q. Écrit tel quel, « p/q ≤ 1/ε » est faux : on a seulement p/q ≤ 1/(1 − ε).
  - La borne de variance porte sur la variance **asymptotique** : au plus 1/λ fois celle de la méthode de Monte-Carlo simple.
  - q(c) ≥ ε·u(c) est immédiat par construction ; l'article ne l'écrit pas sous cette forme.
  - « On perd au plus la fraction ε du budget » n'est pas dans l'article. C'est une lecture (la part ε des tirages va à la composante défensive), pas un énoncé de Hesterberg.

## 2. Levin 1973

- Référence : L. A. Levin, « Универсальные задачи перебора », Проблемы передачи информации 9:3 (1973), p. 115-116 ; trad. « Universal sequential search problems », Problems of Information Transmission 9:3 (1973), p. 265-266. Traduction reprise en annexe de B. A. Trakhtenbrot, « A Survey of Russian Approaches to Perebor (Brute-Force Search) Algorithms », Annals of the History of Computing 6:4 (1984), p. 384-400.
- Sources :
  - Traduction anglaise récente : https://lance.fortnow.com/papers/files/Levin%20Universal.pdf (origine de la traduction non dite dans le fichier ; à traiter comme traduction non officielle).
  - Trakhtenbrot 1984 : https://uvatoc.github.io/docs/levin.pdf
  - L'original russe (mathnet.ru) n'a pas été obtenu.
- Chemins et empreintes :
  - `docs/sources/pdf-puits-etroits-v1/levin-1973-universal-search-fortnow-v1.pdf` — `4d4df86b9f5a32fdd57d6a251559861918cc909a8931f10954f845b8595c68c4`
  - `docs/sources/pdf-puits-etroits-v1/trakhtenbrot-1984-perebor-survey-v1.pdf` — `73afb6f5dd26fee0c8ddc05eb96d9316652e52119fa6bf0cfe35021dfb114d65`
- Pages : traduction de Fortnow, p. 2 ; Trakhtenbrot, p. 400 (annexe, traduction) et p. 397 (commentaire).
- Citations exactes :
  - Annexe de Trakhtenbrot, p. 400 : « THEOREM 2. For any [w] search problem A(x, y) there exists an algorithm that solves it in a time that is optimal up to multiplication by a constant and the addition of a number comparable with the length of x. »
  - Trakhtenbrot, p. 397 : « Unfortunately, there is no description of the optimal algorithm in Levin (1973) ».
  - Trakhtenbrot, p. 397 : « Levin's original idea as seen in Levin (1980) was [...] the strings y are to be checked in the increasing order of Kt(y/x) [...] It equals the minimal sum of the length of the program p and the logarithm of the time it spends ».
- Verdict : **confirmée en partie.**
- Écart : l'article de 1973 énonce seulement l'optimalité « à une constante multiplicative près ». Il ne décrit pas l'algorithme et n'écrit pas le facteur 2^L(c). La forme « temps de l'ordre de 2^L(c) fois le temps du programme » vient de travaux postérieurs (Levin 1980 selon Trakhtenbrot, et les exposés ultérieurs). Il faut citer une de ces sources pour le facteur 2^L, après vérification sur PDF.

## 3. Blumer, Ehrenfeucht, Haussler et Warmuth 1987

- Référence : A. Blumer, A. Ehrenfeucht, D. Haussler, M. K. Warmuth, « Occam's Razor », Information Processing Letters 24(6), 1987, p. 377-380. DOI 10.1016/0020-0190(87)90114-1.
- Source : aucune copie légale trouvée. Article payant chez Elsevier. Le lien de cours cité par Wikipédia (université de Buffalo) renvoie une erreur 404.
- Chemin, empreinte, page, citation : néant.
- Verdict : **non vérifiable.**
- Note : un PDF du même groupe d'auteurs existe sur une page de cours (« Learnability and the Vapnik-Chervonenkis Dimension », Journal of the ACM 1989). Ce n'est pas l'article demandé ; il n'a pas été versé.

## 4. Woodard, Schmidler et Huber 2009

- Référence : Dawn B. Woodard, Scott C. Schmidler, Mark Huber, « Sufficient Conditions for Torpid Mixing of Parallel and Simulated Tempering », Electronic Journal of Probability 14 (2009), article n° 29, p. 780-804. DOI 10.1214/EJP.v14-638. (Revue : Electronic Journal of Probability, pas Annals of Applied Probability. Le papier compagnon sur le mélange rapide est, lui, dans Annals of Applied Probability ; non vérifié ici.)
- Source : https://www.maths.tcd.ie/EMIS/journals/EJP-ECP/article/download/638/870.pdf (miroir EMIS, accès libre).
- Chemin : `docs/sources/pdf-puits-etroits-v1/woodard-schmidler-huber-2009-torpid-mixing-v1.pdf`
- Empreinte : `eb59a71e9226bab158c052aa148a094c34ec40374f33f6d40b82fd43216fba0b`
- Pages : 780 (résumé), 782 (introduction), 797-798 (section 5), 799 (conclusion).
- Citations exactes :
  - p. 780 : « More generally, anytime a multimodal distribution includes both very narrow and very wide peaks of comparable probability mass, parallel and simulated tempering are shown to mix slowly. »
  - p. 780 : « For a multimodal distribution, the persistence is a measure of how "spiky", or tall and narrow, one peak is relative to the other peaks of the distribution. »
  - p. 799 : « if the simulated tempering chain is initialized in one of the wide peaks [...] the tempering chain will take a very large number of iterations to discover the narrow peaks of the distribution. »
- Verdict : **confirmée, avec deux précisions.**
- Précisions : (a) la condition exige des pics de **masse de probabilité comparable** ; (b) « lent » signifie ici « torpide » au sens formel de l'article (défini en section 2, à relire avant de citer un ordre de grandeur). Le mot « profond » de l'affirmation correspond à « tall » (haut) dans l'article.

## 5. Halmos 1946

- Référence : Paul R. Halmos, « The Theory of Unbiased Estimation », Annals of Mathematical Statistics 17(1), mars 1946, p. 34-43. DOI 10.1214/aoms/1177731020.
- Source : article en accès libre sur Project Euclid, mais le téléchargement automatique est bloqué par le pare-feu du site. Aucune autre copie légale trouvée.
- Chemin, empreinte, page, citation : néant.
- Verdict : **non vérifiable** sur PDF.
- Ce qu'on peut dire, sans valeur opposable : le résumé (vu dans les résultats de recherche, non lu sur PDF) annonce une condition nécessaire et suffisante d'existence d'un estimateur sans biais, appliquée aux moments, et l'unicité de l'estimateur symétrique de variance minimale. Un article qui commente Halmos (Konijn, Journal of the Australian Mathematical Society) résume : les moments centrés d'ordre m ≥ 2 ont un estimateur sans biais si et seulement si n ≥ m. Si cela se confirme sur PDF, l'article sert la **seconde** lecture (pas d'estimateur sans biais d'une fonctionnelle de degré trop élevé, donc de 1/p, à taille d'échantillon fixée), pas la première (aucun budget fini ne garantit de trouver l'objet). À vérifier avant toute citation.

## 6. Gillman 1998

- Référence : D. Gillman, « A Chernoff Bound for Random Walks on Expander Graphs », SIAM Journal on Computing 27(4), 1998, p. 1203-1220. DOI 10.1137/S0097539794268765. Version de conférence : FOCS (l'année 1993 ou 1994 n'est pas tranchée ; les sources secondaires divergent).
- Sources :
  - Article : payant chez SIAM (code 403). Non obtenu.
  - Thèse du MIT (1993), dépôt DSpace : https://dspace.mit.edu/handle/1721.1/17332 ; fiche lue, PDF refusé par le pare-feu (code 429).
  - Source secondaire versée : Rao et Regev, « A Sharp Tail Bound for the Expander Random Sampler », arXiv:1703.10205v2, https://arxiv.org/pdf/1703.10205v2
- Chemin : `docs/sources/pdf-puits-etroits-v1/rao-regev-2017-expander-sampler-arxiv-1703.10205v2-source-secondaire-v1.pdf`
- Empreinte : `73797c236bf8c13025875f170d4b35359453d4085c62828edaae907a464ce584`
- Page : Rao et Regev, p. 1 (résumé) et bibliographie.
- Citations exactes :
  - Fiche DSpace du MIT (métadonnée, pas un PDF) : « Gillman, David Wallace » ; « by David Gillman. »
  - Rao et Regev, p. 1 : « Gillman showed in 1993 that the number of marked vertices seen in a random walk of length n is concentrated around its expectation, Φ := µn, independent of the size of the graph. »
  - Rao et Regev, bibliographie : « [Gil98] D. Gillman. A Chernoff bound for random walks on expander graphs. SIAM J. Comput., 27(4):1203–1220, 1998. »
- Verdict :
  - Prénom : **David** (David Wallace Gillman), confirmé par la fiche du MIT ; pas sur le PDF de l'article.
  - Énoncé de la borne : **non vérifiable** sur l'article. On sait seulement, par source secondaire, qu'il s'agit d'une concentration du nombre de visites d'un ensemble marqué autour de µn, indépendante de la taille du graphe. Les constantes exactes ne doivent pas être citées sans le PDF.

## 7. Nisan et Szegedy 1994

- Référence : Noam Nisan, Mario Szegedy, « On the Degree of Boolean Functions as Real Polynomials », Computational Complexity 4 (1994), p. 301-313.
- Source : https://web.vu.lt/mif/s.jukna/boolean/Nisan-Szegedy.pdf (voir réserve de provenance).
- Chemin : `docs/sources/pdf-puits-etroits-v1/nisan-szegedy-1994-degree-boolean-v1.pdf`
- Empreinte : `059743f397f0a148e9117ee2f7762bd9a73b80b023c033ffca1e5fae6c2f9abe`
- Pages : 301 (résumé), 303-304 (théorèmes 1.2, 1.3, 1.5), 308 (lemme 3.5), 310 (lemme 3.8, théorème 3.9).
- Ce que l'article établit (citations exactes ; le texte extrait est bruité, symboles rétablis) :
  - p. 301 : « Our first result is a tight lower bound of Ω(log n) on the degree needed to represent any Boolean function that depends on n variables. »
  - p. 301 : « for every Boolean function f, the following measures are all polynomially related: The decision tree complexity of f. The degree of the polynomial representing f. The smallest degree of a polynomial approximating f in the L_max norm. »
  - p. 304, théorème 1.3 : « deg(f) ≤ D(f) ≤ 16 deg(f)^8 ».
  - p. 308, lemme 3.5 (fonctions nulles en 0 et valant 1 sur tout vecteur de poids 1, dont le « ou ») : « deg(f) ≥ √(n/2) ; deg~(f) ≥ √(n/6) ».
  - p. 310, lemme 3.8 : bornes du degré par la sensibilité par blocs, bs(f).
- Verdict : **infirmée** (l'attribution ne tient pas).
- Raison : l'article ne parle ni de recherche aléatoire, ni d'arbres de décision probabilistes à erreur bornée, ni d'une borne Ω(M). Il traite du degré exact, du degré approché et de la sensibilité par blocs, en déterministe. Il donne Ω(√n) pour le degré approché du « ou ». Ce résultat sert plus tard aux bornes inférieures **quantiques** (ordre √M), pas à la borne Ω(M) en aléatoire classique. Pour Ω(M) en aléatoire classique, il faut une autre source (par exemple la borne par la sensibilité par blocs de Nisan 1991, à vérifier sur PDF).

## 8. Dorfman 1943

- Référence : Robert Dorfman, « The Detection of Defective Members of Large Populations », Annals of Mathematical Statistics 14(4), décembre 1943, p. 436-440. JSTOR 2235930.
- Source : https://webpages.tuni.fi/uta_statistics/liski-arkisto/mtt-perusteet10/mttp-kurssi10/Materiaalia/Dorfman-Ann1943.pdf (scan JSTOR ; voir réserve de provenance).
- Chemin : `docs/sources/pdf-puits-etroits-v1/dorfman-1943-detection-defective-v1.pdf`
- Empreinte : `bf3ed6c9f53c110e54a90c79001469d44eca1dea2d3ab1a233d41eb2e11a852d`
- Pages : 437 (formule du coût), 438 (table I). Page 1 du PDF = page de garde JSTOR.
- Citations exactes :
  - p. 437 : « E(T) = N/n + n(N/n)p' » ; coût relatif « C = T/N = 1/n + p' = 1 + 1/n − (1 − p)^n ».
  - p. 438 : « For a prevalence rate of .01 it is clear from the chart that only 20% as many tests would be required by group tests with groups of 11 than by individual testing. »
  - p. 438, table I (extrait) : taux 1 % → taille 11, coût relatif 20 % ; 2 % → 8, 27 % ; 4 % → 6, 38 % ; 10 % → 4, 59 % ; 15 % → 3, 72 %.
- Verdict : **confirmée en partie.**
- Écart : l'article ne contient aucune formule en √p, ni « taille optimale vers 1/√p ». Il donne la formule exacte du coût et une table numérique. Les chiffres de la table concordent avec l'approximation (taille ≈ 1/√p, coût ≈ 2√p) : à 1 %, 1/√p = 10 contre 11 dans la table, 2√p = 20 % contre 20 %. Mais cette approximation est une dérivation, pas un énoncé de Dorfman. Chiffre exact à citer : 20 % de tests avec des groupes de 11 pour un taux de 1 % (p. 438).

---

## Table de synthèse

| n° | Citation | PDF versé | Page | Verdict |
|---|---|---|---|---|
| 1 | Hesterberg 1995, mélanges défensifs | oui | 189 | Confirmée en partie : borné, c'est u/q ≤ 1/ε (la composante défensive est la cible) ; p/q ≤ 1/(1 − ε) ; variance asymptotique ≤ 1/λ fois Monte-Carlo simple ; « perte au plus ε du budget » absente |
| 2 | Levin 1973, recherche universelle | traduction et Trakhtenbrot 1984 | 400, 397 | Confirmée en partie : optimal à une constante multiplicative près ; le facteur 2^L(c) n'est pas dans l'article de 1973 (vient de travaux postérieurs) |
| 3 | Blumer et al. 1987, rasoir d'Occam | non (payant) | — | Non vérifiable |
| 4 | Woodard, Schmidler, Huber 2009 | oui | 780, 799 | Confirmée : pics étroits et larges de masse comparable ⇒ mélange lent ; revue Electronic Journal of Probability |
| 5 | Halmos 1946, estimation sans biais | non (pare-feu de Project Euclid) | — | Non vérifiable ; d'après sources secondaires, il servirait la lecture « pas d'estimateur sans biais à taille fixée », pas « aucun budget ne garantit de trouver » |
| 6 | Gillman 1998, borne de Chernoff sur expanseurs | non (payant) ; source secondaire versée | — | Prénom : David (fiche du MIT) ; énoncé de la borne non vérifiable |
| 7 | Nisan et Szegedy 1994, degré | oui | 301-310 | Infirmée : pas de borne Ω(M) en recherche aléatoire ; l'article donne degré, degré approché (≥ √(n/6) pour le « ou »), sensibilité par blocs |
| 8 | Dorfman 1943, tests groupés | oui | 437-438 | Confirmée en partie : pas de √p dans l'article ; table : 1 % → groupes de 11, 20 % des tests ; concorde avec 2√p mais c'est une dérivation |
