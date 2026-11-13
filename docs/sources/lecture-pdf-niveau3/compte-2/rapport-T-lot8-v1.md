# Rapport d'antériorité — théorème négatif « T » — lot 8 (trois pièces sur l'échangeabilité et l'invariance de groupe) — v1

- Date : 2026-11-13 ; début de la lecture 22:37:53 UTC, fin de rédaction 22:47:00 UTC (heures relevées par `date -u`).
- Lecteur : sous-agent neuf, modèle A. Je n'ai écrit ni le programme, ni les décisions, ni aucun rapport antérieur.
- Mandat : verdict d'antériorité sur le seul énoncé T (décision N-003), par lecture intégrale de trois PDF.

## Empreintes des trois pièces (vérifiées contre leur compagnon `.sha256` avant lecture : concordance des trois)

| fichier | pages | empreinte sha256 |
|---|---|---|
| `2310.01153v5.pdf` (Koning, « Measuring Evidence against Exchangeability and Group Invariance with E-values ») | 45 | `e8cd3532247d69817c47ecf7773c1da5318e87404b9e29d3d95f6fef69ab0544` |
| `2102.00630v4.pdf` (Ramdas, Ruf, Larsson, Koolen, « Testing exchangeability: fork-convexity, supermartingales, and e-processes ») | 34 | `2ada73f4abaf779b06baa558f49893678feec1d5b1451e083e842dd14117fd57` |
| `1906.09256v3.pdf` (Vovk, « Testing randomness ») | 34 | `0a9a1f2c7e96107f4f573e9aa3dd8f1d79798b84cbbd9923bd3db2ecb81efbe3` |

Dossier des pièces : `/tmp/claude-0/-home-user-controle-ia-travail/7e7693dc-fcf8-5081-b2b3-044ac9061481/scratchpad/pieces-10016a61/docs/sources/pdf/niveau3-v1/lot8/` (branche `prep/etat-de-l-art-niveau3-pieces-v1`, tête `10016a61`). Numérotation des pages : page du fichier ; dans les trois pièces elle coïncide avec le numéro imprimé en pied de page (vérifié par extraction page à page).

## Fichiers lus (liste exacte)

1. `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-0500-v1/interdits-communs-v2.md` (en entier).
2. `…/scratchpad/pieces-10016a61/docs/sources/lecture-pdf-niveau3/consignes-v1/consigne-commune-lecture-v1.md` (en entier).
3. `docs/decisions/decision-N-003-N-004-v1.md`, lignes 17 à 52.
4. `docs/notes/note-mathematique-lemme-theoreme-v2.md`, lignes 1 à 55 et 86 à 131.
5. `docs/programme-controle-ia-v2.md`, lignes 85 à 125.
6. `docs/etat-de-l-art/niveau2-v1/anteriorite-v1.md`, lignes 113 à 129.
7. `docs/etat-de-l-art/etat-de-l-art-verifie-niveau3-v1.md`, lignes 154 à 171.
8. `docs/etat-de-l-art/etat-de-l-art-verifie-niveau3-v1-contre-lecture-v1.md`, lignes 368 à 407.
9. Les trois PDF ci-dessus, en entier (annexes, preuves, références, tableaux), et leurs trois compagnons `.sha256`.

Rien d'autre n'a été ouvert. Aucune ouverture fautive. Aucun refus d'un contrôle de permissions ou d'un classifieur.

## Contrôle des citations

- Script : `verifier_citations_v1.py` (dossier de travail), lancé par `python3 -I` ; pour chaque citation il vérifie l'empreinte du PDF, extrait la page par `pdftotext` avec et sans `-layout`, normalise (espaces, ligatures, césures avec et sans trait d'union réel, apostrophes, guillemets, tirets) et cherche la citation.
- Essais préalables : cas juste (réussite), trois cas altérés — mot changé, page fausse, empreinte fausse — (trois échecs, attendus). Journal : `journal-T-v1.txt`.
- **Citations contrôlées : 72. Échecs : 0.** Liste complète : `citations-T-v1.json`. Dans ce rapport, toute citation tirée d'un PDF est entre guillemets anglais doubles, en anglais, et figure mot pour mot dans ce fichier.
- Les formules sont recopiées à part et marquées « lu sur le PDF, non contrôlé par programme ».

---

## 0. En tête : occupations, même partielles

1. **Unification temps × agents — occupée en partie par Koning (2310.01153v5).** Le cadre général est écrit : tester l'invariance d'une loi sous un groupe compact quelconque agissant sur l'espace des données (p. 1, 2), sous un sous-groupe (p. 13, remarque 6), et en particulier sous le **produit des groupes de permutations à l'intérieur de blocs**, présenté explicitement comme un **sous-groupe des permutations de l'ensemble des observations individuelles**, plus faible que l'échangeabilité pleine, avec l'emboîtement « rejeter l'invariance par blocs rejette l'échangeabilité » (p. 21-23, exemples 10, 13 ; p. 35, exemple 14). L'application au « hot hand » multiplie des e-valeurs d'échangeabilité calculées joueur par joueur (p. 5, 26) : c'est exactement le sous-groupe « permutations du temps à l'intérieur de chaque agent », sans qu'il soit nommé ainsi. **Non fait** : l'ensemble d'indices à deux axes I ⊂ {1..N} × {1..T}, le second sous-groupe (permutations des agents à l'intérieur de chaque pas), l'affirmation que le temps et les agents sont deux sous-groupes d'un même objet, et l'usage de ce cadre pour un énoncé négatif face à un attaquant.
2. **T2, noyau probabiliste — occupé en partie par Koning (2310.01153v5), comme fond classique attribué à Eaton (1989).** Lemme 1, conditions 3 à 5 (p. 8) et section 2.5 (p. 9) : une loi invariante est un mélange de lois uniformes sur les orbites ; tirer un élément uniforme du groupe, indépendamment, et l'appliquer à une variable quelconque donne la loi moyennée sur le groupe. L'identité de T2 (« un réarrangement dans H suivi d'un rebrassage uniforme sur H rend exactement P₀ ») en découle en deux lignes (raisonnement du lecteur, section 2.3 ci-dessous). **Non fait** : l'attaquant, la permutation dépendante des données π_Y, la lecture comme impossibilité pour le défenseur (« aucun moniteur ne dépasse son taux »), et le volet « le groupe compte » sous la forme du programme (seulement des voisins, p. 13 et 22).
3. **T2, mécanisme du rebrassage — contre-indice chez Vovk (1906.09256v3)** : permuter au hasard un jeu de données non aléatoire fait perdre toute évidence au test (p. 10, 12, 13, 15), présenté comme contrôle de bon sens, groupe plein seulement, sans attaquant.

Rien d'autre n'est occupé, même en partie : T1 (voisin), T3 (voisins), distinction C/K et ses signes (voisin, contre-indice faible pour la seule moitié qualitative), T4 (ne touche pas), mesure sur activations (ne touche pas).

**Verdict d'ensemble sur T : « occupé en partie ».**

---

## 1. Ce que dit T (rappel, pour la confrontation)

Décision N-003 (l. 17-52) et note v2 (section 4) : scores X_{i,t} sur I ⊂ {1..N} × {1..T} ; trois groupes de permutations de I (temps à l'intérieur de chaque agent ; agents à l'intérieur de chaque pas ; toutes). T1 : une attaque de classe C (π_Y ∈ G) laisse inchangée trajectoire par trajectoire toute statistique G-invariante. T2 : P₀ invariante sous H, attaque X = σ ∘ π_Y(Y) avec π_Y ∈ H et σ uniforme sur H indépendante ⇒ X ~ P₀ exactement ; « le groupe compte » (exemple à trois agents, rebrassage sur tout I détecté, rebrassage du temps agent par agent non détecté). T3 : bornes trajectorielles du balayage, de Page, de la co-élévation ; neutralisation de l'autocorrélation et du test des suites par un attaquant adaptatif. Classes C et K et signes (somme et processus e au-dessus du taux sous dépendance positive, en dessous sous dépendance négative ; max à son taux ou en dessous par Slepian). T4 : somme lue séquentiellement sous sommes partielles dominées. Revendiqué : unification, distinction C/K et signes, garanties locales face à un attaquant adaptatif, transposition aux activations et sa mesure ; T1 avoué élémentaire.

---

## 2. Fiche — Koning, 2310.01153v5 (45 pages, arXiv math.ST, version du 10 février 2026 imprimée en p. 1 ; aucune venue de revue imprimée)

### 2.1 Ce que fait l'article
- Objet : “We study e-values for quantifying evidence against exchangeability and general invariance of a random variable under a compact group.” (p. 1). “Permutation tests are a special case of more general group invariance tests” (p. 2).
- Fond sur l'invariance (section 2, attribué à Eaton 1989, p. 6, 8) : “any invariant probability may be viewed as a mixture over uniform probabilities on orbits.” (p. 8) ; “Condition 4 states that a draw from an invariant random variable Y can be decomposed (de-convolved) into first sampling an orbit representative” (p. 8) ; “Condition 5 restates this in terms of orbits: a draw from Y can be viewed as first sampling an orbit” (p. 8) ; “This decomposition is the key to testing invariance, where the idea is to effectively discard the first part of this sampling process, and only test whether Y is uniform conditional on the orbit in which it is observed.” (p. 9) ; “We can construct an invariant probability from a probability measure P by averaging it over the group” (p. 9), et, pour une loi déjà invariante, “so that this averaging has no effect.” (p. 9).
  - Formules (lu sur le PDF, non contrôlé par programme) : lemme 1, p. 8 — (3) Y =d GY avec G ~ Unif(G) indépendant ; (4) Y =d G[Y] ; (5) Unif(O_Y) est une version de la loi conditionnelle de Y sachant O_Y. Section 2.5, p. 9 — P̄ := E_G[GP] ; « if Y ~ P, then GY ~ P̄ ».
- Caractérisation (section 3) : “It states that an e-value is valid for group invariance if and only if it is valid for a uniform distribution on each orbit.” (p. 11) ; “In particular, we may view the problem of testing group invariance as first observing the orbit” (p. 11). E-valeur exacte générique (théorème 3, p. 12 ; formule lu sur le PDF, non contrôlé : ε_T(y) = T(y) / E_G T(Gy)) ; version de Monte-Carlo (théorème 4, p. 13).
- Sous-groupes : “As invariance under G implies invariance under all its subgroups, this guarantees the resulting e-value is valid.” (p. 13) ; “Koning and Hemerik [2023] note that we can strategically select the subgroup based on the test statistic and alternative to increase power.” (p. 13) ; “Koning [2024b] observes that this can even yield methods that are more powerful than using the entire group G.” (p. 13).
- E-valeurs optimales (section 4) ; une fonction invariante est constante sur les orbites : “thus constant on each orbit and so absorbed into the multiplier” (p. 17).
- E-processus pour l'invariance sous filtration quelconque (section 5) : “In addition, we characterize e-processes for group invariance for arbitrary filtrations, and provide tools to construct them.” (p. 1) ; “The key challenge when constructing e-processes for group invariance is that the sequential analogue of Corollary 1 is typically not useful.” (p. 18).
- Martingales de test sous une suite de groupes (section 6) : “We show how they may easily be constructed by tailoring conditional e-values for their increments based on subgroups that stabilize the previous data.” (p. 5) ; invariance par blocs, “Suppose we sequentially observe potentially unequally sized batches of data” (p. 21) ; “then within-batch exchangeability is weaker than exchangeability of individual observations: we exclude permutations that swap observations across batches.” (p. 22) ; “Specifically, the groups we consider here are subgroups of the permutations on the set of the individual observations.” (p. 22) ; “This means rejecting within-batch exchangeability also rejects exchangeability.” (p. 23). Réduction par statistique équivariante : “by using a statistic that is equivariant under a subgroup of the group. The problem then reduces to testing invariance of the statistic under the subgroup.” (p. 5) ; “Hence, the hypothesis of F invariance of H(X) is at least as large as that of G invariance of X.” (p. 34) ; “In Example 14, we illustrate this approach by showing how we may reduce from exchangeability” (p. 35).
- Impossibilité de Ramdas et collègues réinterprétée : “A consequence is that it is impossible to sequentially test exchangeability with a test martingale under the filtration” (p. 23) ; “Our discussion gives some context around their impossibility result” (p. 23).
- Invariance « à travers une statistique » et contre-exemple : “this condition is insufficient for testing invariance: we include a counterexample in Appendix 10.2.” (p. 9) ; “In Example 18, the underlying random variable is not invariant, but looks invariant through certain statistics.” (p. 37) ; “The order does look exchangeable through the statistic that returns only the first position.” (p. 37) ; annexe 10.2 : marginales identiques, dépendance choisie, “Moreover, it puts no restriction on the dependence structure of the individual elements, which we will exploit.” (p. 38), d'où “so that the group invariance test is not valid.” (p. 38).
- Application : “We leverage the powerful merging properties of e-values by multiplying e-values across players to obtain a more powerful e-value.” (p. 5) ; “We apply this idea to the controlled shooting experiment data collected by Gilovich et al. [1985], with 26 shooters taking up to 100 shots each.” (p. 26) ; “Table 1 reports the product of the e-values for the individual shooters.” (p. 26).

### 2.2 Chiffres (nature indiquée)
- Simulation cas-témoins (p. 24, figure 1, p. 25) : 40 lots, θ = 25, 1 000 simulations, 100 permutations de Monte-Carlo (auteurs) ; « roughly 95% » des e-processus au-dessus de 20 au lot 23 sous l'alternative (auteurs, lu sur la figure et le texte p. 24).
- Hot hand, tableau 1 p. 26 : produit des e-valeurs 0,007 / 0,180 / 3,108 / 4,460 / 7,489 / 5,525 selon le déclencheur et β (auteurs). Exemple chiffré p. 26 : e-valeur ≈ 1,0095 pour la suite 111010 (auteurs).
- Contre-exemple p. 38 : taux de rejet 0,5 pour α = 1/3 (k = 2, n = 3) (auteurs).

### 2.3 Confrontation, composante par composante
- **Unification — occupée en partie.** Fait : invariance sous un groupe compact quelconque ; sous-groupes ; groupe produit des permutations intra-blocs comme sous-groupe des permutations de toutes les observations, emboîté sous l'échangeabilité pleine (p. 13, 21-23, 35) ; fusion par produit d'e-valeurs calculées par joueur (p. 5, 26), qui revient au sous-groupe « temps à l'intérieur de chaque agent ». Non fait : indices à deux axes ; sous-groupe « agents à l'intérieur de chaque pas » ; énoncé « deux sous-groupes d'un même objet » ; usage négatif face à un attaquant. Ce qui reste est une **instance** du cadre de Koning ; un statisticien pourra le dire, et le constat C2 de la contre-lecture l'avait anticipé.
- **T1 — voisin.** L'article écrit le dual : une fonction invariante est constante sur les orbites (p. 17), et tester l'invariance revient à jeter l'information d'orbite (p. 9, 11) ; pour les permutations, l'orbite est le multi-ensemble. L'exemple 18 (p. 37) exhibe une loi non invariante qui « paraît » invariante à travers certaines statistiques. Aucun attaquant, aucune affirmation de puissance égale au taux sous une attaque qui reste dans l'orbite.
- **T2 — occupée en partie (noyau probabiliste).** Raisonnement du lecteur (calcul, non imprimé dans la pièce) : π_Y ∈ H laisse l'orbite inchangée, donc π_Y(Y) a la même loi d'orbite que Y ; σ uniforme indépendante rend σ ∘ π_Y(Y), sachant l'orbite, uniforme sur l'orbite (conditions 3-4 du lemme 1, section 2.5) ; P₀ invariante est le mélange des uniformes sur les orbites selon cette même loi d'orbite (p. 8, condition 5) ; donc X ~ P₀. Toutes les briques sont imprimées p. 8-9 comme fond classique ; l'identité de T2 n'est pas écrite telle quelle, et sa lecture adverse (attaque indétectable, défenseur sans recours) n'apparaît nulle part. « Le groupe compte » : voisin — l'invariance par blocs est plus faible que l'échangeabilité (p. 22), le choix du sous-groupe change la puissance (p. 13) ; l'énoncé du programme (une P₀ invariante seulement sous un sous-groupe laisse détecter un rebrassage plus large) et l'exemple à trois agents ne sont pas écrits.
- **T3 — ne touche pas.** Aucune statistique locale (balayage, Page, co-élévation), aucune garantie trajectorielle, aucun attaquant adaptatif. L'alternative « hot hand » (série de k réussites, p. 26) n'est qu'un voisin lointain de « r actions consécutives hautes ».
- **Classes C et K — voisin ; contre-indice faible pour la seule moitié qualitative.** L'annexe 10.2 (p. 38) montre que des marginales identiques avec une dépendance choisie suffisent à fausser le taux d'un test d'invariance : c'est la moitié qualitative de « préserver les marginales n'est pas préserver le taux ». Non fait : le contraste C/K comme classes d'attaque, les signes (somme et processus e au-dessus du taux sous dépendance positive, en dessous sous négative), le max sous Slepian. Les mots « copula » et « Slepian » n'apparaissent pas (recherche dans le texte extrait).
- **T4 — ne touche pas.**
- **Application aux activations — ne touche pas.**

### 2.4 Limites reconnues, réserves du lecteur
- Groupes compacts supposés partout ; groupes non compacts seulement esquissés (remarques 4 et 11, p. 11, 20).
- Résultats « trop beaux » : aucun ; les simulations sont des illustrations ; la comparaison avec de la Peña (figure 2, p. 25) est à l'avantage de l'auteur, cohérente avec l'inadmissibilité rappelée p. 34 (pas de réserve forte).
- Cohérence interne : rien de contradictoire relevé.

---

## 3. Fiche — Ramdas, Ruf, Larsson, Koolen, 2102.00630v4 (34 pages, arXiv math.ST, 23 juillet 2021 ; venue non imprimée dans la pièce ; Koning la cite p. 28 comme parue dans International Journal of Approximate Reasoning, 141:83-109, 2022)

### 3.1 Ce que fait l'article, et ce qu'établit exactement le résultat d'impossibilité
- Cadre : une seule suite binaire, nul « échangeable », filtration canonique des données.
- **Impossibilité (exactement)** : “Nonnegative supermartingales (NSMs) are a workhorse of sequential inference, but we prove that they are powerless for this problem.” (p. 1) ; “this implies that any NSM under exchangeability is necessarily nonincreasing, hence always yields a powerless test for any alternative.” (p. 1) ; “Theorem 17 proves that every NSM under exchangeability must be a nonincreasing process and thus powerless.” (p. 3). Mécanisme : l'enveloppe fork-convexe fermée du nul contient toutes les lois — “Every law P over the space of binary sequences belongs to the closed fork-convex hull of” (p. 17, théorème 17) ; “they are incapable of detecting any deviation from exchangeability.” (p. 18) ; “rendering them powerless to distinguish non-exchangeable distributions from exchangeable ones.” (p. 26). Conséquence : “any Q-safe e-process with nontrivial power cannot be a Q-NSM” (p. 6).
  - Formules (lu sur le PDF, non contrôlé) : définition 10 p. 14 (combinaison fork-convexe des processus de vraisemblance) ; théorème 13 p. 16 (toute surmartingale non négative pour Q l'est pour son enveloppe fork-convexe fermée).
- **Ce n'est pas une impossibilité de détecter l'écart à l'échangeabilité** : l'article construit un e-processus sûr, non surmartingale, de puissance un contre les alternatives markoviennes d'ordre un — “we prove that it has power one against any first-order Markovian alternative” (p. 26) ; théorème 7, p. 11 (taux exponentiel r*, lu sur le PDF, non contrôlé).
- Impossibilités informelles d'une autre nature : “Since testing arbitrary deviations from exchangeability is information theoretically impossible, we focus on Markovian alternatives.” (p. 1) ; “This example relies on ensuring that the information required to detect a deviation from the null is exhausted early on in the sequence.” (p. 5) ; “Recall that it is impossible to detect all deviations from exchangeability.” (p. 18) ; “In fact, one can argue that it is information theoretically impossible to design any power one test, including tests that are tuned to detect a single change point.” (p. 22). Clôture convexe : “safe and consistent e-processes do not exist and neither do valid, power-one tests.” (p. 4), pour un nul indépendant et identiquement distribué contre son enveloppe convexe (les lois échangeables).
- Lecture « adaptative » de l'enveloppe fork-convexe : “if Reality wanted to draw an infinite sequence from the fork-convex hull of Q” (p. 26), “each time using the observed data to pick the next (conditional) distribution as it wishes.” (p. 26).
- Distinction explicite : “The last setting should especially not be confused with change point detection” (p. 19).

### 3.2 Chiffres
- Pluie de Londres : 4 404 jours, 59 % de jours pluvieux (auteurs, p. 23) ; rejet visuel (figure 7, p. 23).
- Changement de régime Ber(0,1)⁵⁰⁰⁰ puis Ber(0,4)⁵⁰⁰⁰ : p-processus sous 10⁻²⁰ en fin de suite (auteurs, légende figure 6, p. 22) ; A_∞ ≈ 10¹⁷ avec l'ajusteur (auteurs, p. 25).

### 3.3 Confrontation
- **Unification — ne touche pas** (une suite, permutations du temps seulement).
- **T1 — ne touche pas.**
- **T2 — voisin (nature différente), pas une occupation.** T2 est une impossibilité par **égalité des lois** : la sortie de l'attaque a exactement la loi P₀, donc aucun test, quelle que soit sa forme, ne dépasse son taux. Le théorème 17 est une impossibilité d'une **classe de statistiques** (les surmartingales non négatives sous le nul échangeable, dans la filtration des données), causée par la filtration et la fork-convexité, contre **toute** alternative ; d'autres statistiques (e-processus non surmartingales) y échappent. Les deux résultats ne se recouvrent pas. Ce que le résultat touche : (i) un moniteur construit comme surmartingale d'échangeabilité dans la filtration des scores serait aveugle avant toute attaque, ce qui ne doit pas être porté au crédit de l'attaquant ; (ii) la remarque informelle p. 1, 5, 18, 22 (« détecter tout écart est impossible ») est un voisin de l'esprit « impossibilité sans structure », sans le mécanisme du rebrassage ni groupe.
- **T3 — voisin, volet « attaquant adaptatif » seulement.** L'enveloppe fork-convexe est la loi d'une Réalité qui choisit pas à pas la loi suivante au vu des données (p. 26), contre laquelle toute une classe de statistiques séquentielles est aveugle. Autre mécanisme que la neutralisation de l'autocorrélation et du test des suites par réarrangement ; aucune garantie locale.
- **Classes C et K — voisin.** Les alternatives markoviennes stationnaires gardent la marginale de Bernoulli et changent la dépendance ; l'article montre qu'un e-processus conçu pour elles les détecte (p. 11, 26). Rien sur le signe de la somme ou du max sous dépendance positive ou négative.
- **T4 — ne touche pas.** **Activations — ne touche pas.**

### 3.4 Limites reconnues, réserves
- Données binaires (extensions finies, p. 12) ; alternatives markoviennes ; l'exemple 9 (p. 12) montre une chaîne d'ordre deux contre laquelle l'e-processus d'ordre un est sans puissance (limite reconnue).
- « Trop beau » : aucun ; les contrôles de bon sens (p. 19-20) sont cohérents avec le théorème 7.

---

## 4. Fiche — Vovk, 1906.09256v3 (34 pages, arXiv math.PR, 29 mars 2020 ; venue non imprimée ; Koning cite p. 29 « Testing randomness online », Statistical Science 36(4), 2021 — identité avec cette pièce probable, non vérifiée)

### 4.1 Ce que fait l'article
- Revue : “This paper reviews known methods of testing the two hypotheses concentrating on the online mode of testing, when the observations arrive sequentially.” (p. 1) ; validité “including conformal versions of the CUSUM and Shiryaev-Roberts procedures.” (p. 1). “Conformal martingales are constructed on top of conventional machine-learning algorithms” (p. 2).
- Validité : p-valeurs conformes indépendantes et uniformes sous l'hypothèse (proposition 3.1, p. 7), étendue à l'échangeabilité à horizon fini : “The conclusion of Proposition 3.1 will still hold even if we relax the assumption of” (p. 7). “Conformal martingales are exchangeability martingales, i.e., stochastic processes that are martingales with respect to any exchangeable distribution.” (p. 8) ; dans la filtration naturelle, “the only exchangeability martingales are almost sure constants.” (p. 8).
- Équivariance de la mesure de non-conformité (proposition 2.1, p. 5) et son échec pour le caractère aléatoire : “Let us check that Proposition 2.1 ceases to be true if” (p. 6).
- **Rebrassage comme contrôle** : figures 2 et 4, versions « randomly permuted » des jeux de données — “after observing the first n digits of a randomly permuted USPS dataset” (p. 10) ; “unlike the more stable right panel showing the p-values for a randomly permuted dataset” (p. 12) ; “The conformal martingale is trying to gamble against an exchangeable sequence of observations, which is futile, and so its value decreases exponentially quickly.” (p. 15).
- Détection de rupture : “A typical example of change detection is where we observe attacks, which we assume to be IID, on a computer system.” (p. 15 ; « attaques » au sens d'intrusions observées, pas d'un adversaire du moniteur) ; “A standard multistage procedure of raising alarms is the CUSUM procedure proposed by Page” (p. 16) ; propositions 4.1 et 4.3, corollaires 4.2 et 4.5 (p. 17-20 : temps moyen avant première fausse alarme ≥ c ; fréquence asymptotique des alarmes ≤ 1/c ; formules lues sur le PDF, non contrôlées). “In this paper we only discuss validity results for CUSUM and Shiryaev-Roberts in the context of randomness testing and do not claim their optimality.” (p. 21) ; “we simply do not have enough structure to specify a meaningful optimization problem.” (p. 21).
- Efficacité grossière : “Proposition 5.3 may be interpreted as saying that there is not much difference between testing randomness and testing exchangeability.” (p. 23) ; propositions 5.3 et 6.2 (facteurs 1,5·√N et N, lus sur le PDF, non contrôlés) ; aléa = échangeabilité et binomialité du compte : “It says, informally, that the randomness of” (p. 33), “might be perfectly exchangeable whereas it will not be random” (p. 33).

### 4.2 Chiffres
- p-valeurs du test de Bartels sur USPS : 2,7 × 10⁻¹¹ et 7,5 × 10⁻¹⁶ (auteurs, tableau 1, p. 6).
- USPS : valeur finale 4,71 × 10¹⁸ ; sur le jeu permuté au hasard, 0,0142 (auteurs, légende figure 2, p. 10). Mélange simple : 2,18 × 10¹⁰ (auteurs, p. 10).
- Absentéisme : 100,50 ; permuté, 0,00841 (auteurs, légende figure 4, p. 13) ; variante 3 446,75 (auteurs, p. 14).

### 4.3 Confrontation
- **Unification — ne touche pas** (une suite, permutations des observations).
- **T1 — voisin.** La décomposition « aléa = échangeabilité + binomialité » (p. 33, d'après Kolmogorov et Vovk 1986) sépare l'information d'orbite (le compte, c'est-à-dire le multi-ensemble binaire) de l'information intra-orbite ; c'est la séparation sur laquelle T1 et T2 reposent. Pas d'attaquant, pas de statistique invariante aveuglée.
- **T2 — contre-indice (mécanisme du rebrassage, groupe plein).** L'article montre et dit que permuter uniformément un jeu de données non aléatoire en fait une suite échangeable contre laquelle parier est « futile » (p. 10, 12, 13, 15), avec, en combinant les propositions 3.1 et la remarque 3.2 (p. 7), qu'aucune martingale conforme ne peut alors croître en espérance. Non fait : l'attaquant, l'égalité exacte à P₀ (le jeu permuté est échangeable, pas nécessairement de loi P₀ ; la proposition 5.3 dit seulement que les deux nuls sont proches), les sous-groupes, « le groupe compte ».
- **T3 — voisin.** CUSUM de Page et Shiryaev-Roberts conformes, avec des garanties de **validité** (fausses alarmes), pas de garantie de détection trajectorielle sous dommage structuré, pas d'attaquant adaptatif ; optimalité explicitement non revendiquée (p. 21).
- **Classes C et K — ne touche pas** (rien sur copule, signes, Slepian).
- **T4 — ne touche pas.** **Activations — ne touche pas** (surveillance de prédicteurs déployés, p. 2-3, voisin lointain du cadre, pas des activations).

### 4.4 Limites reconnues, réserves
- Cas binaire et horizon fini pour l'efficacité (p. 3-4) ; précision des bornes reconnue « very low » (p. 27, conclusion) et proposition 5.3 dite « very crude » (p. 32) (non contrôlé par programme).
- « Trop beau » : la chute des martingales sur les jeux permutés est attendue par construction (contrôle de bon sens) ; pas de réserve.

---

## 5. Table composante × article

| composante | Koning 2310.01153v5 | Ramdas et al. 2102.00630v4 | Vovk 1906.09256v3 |
|---|---|---|---|
| Unification temps × agents (sous-groupes de permutations de I, plus le groupe plein) | **occupée en partie** — cadre général et sous-groupe produit intra-blocs faits (p. 13, 21-23, 35 ; joueurs p. 5, 26) ; deux axes, sous-groupe « agents par pas », usage négatif non faits | ne touche pas | ne touche pas |
| T1 aveuglement trajectoriel des statistiques invariantes | voisin (p. 9, 11, 17, 37) | ne touche pas | voisin (p. 33) |
| T2 identité du rebrassage (X ~ P₀) | **occupée en partie** — briques imprimées comme fond classique (p. 8-9) ; identité et lecture adverse non écrites | voisin, autre nature (p. 1, 3, 17-18, 26) | **contre-indice** — rebrassage uniforme qui rend le test futile, groupe plein (p. 10, 12, 13, 15) |
| T2 « le groupe compte » | voisin (p. 13, 22-23) | ne touche pas | ne touche pas |
| T3 garanties locales (balayage, Page, co-élévation) | ne touche pas | ne touche pas | voisin — validité du CUSUM conforme seulement (p. 16-21) |
| T3 neutralisation des statistiques d'ordre globales par un attaquant adaptatif | ne touche pas | voisin — Réalité adaptative et enveloppe fork-convexe, autre mécanisme (p. 26) | ne touche pas |
| Classes C et K, signes, Slepian | voisin ; contre-indice faible pour la moitié qualitative (p. 9, 38) | voisin (alternatives markoviennes, p. 11, 26) | ne touche pas |
| T4 somme séquentielle sous sommes partielles dominées | ne touche pas | ne touche pas | ne touche pas |
| Application aux activations réelles et mesure | ne touche pas | ne touche pas | ne touche pas |

## 6. Verdict d'ensemble sur T

**« occupé en partie ».** Le cadre de l'unification (invariance sous un groupe compact quelconque, sous-groupes produits des permutations intra-blocs emboîtés dans l'échangeabilité) et le noyau probabiliste de T2 (décomposition d'une loi invariante en orbite puis uniforme sur l'orbite ; un tirage uniforme indépendant du groupe restaure la loi moyennée) sont imprimés chez Koning, le second comme fond classique attribué à Eaton (1989). Vovk montre en pratique le mécanisme du rebrassage contre les tests d'échangeabilité. Ramdas et collègues établissent une impossibilité d'une autre nature (filtration et fork-convexité), qui ne recouvre pas T2.

## 7. Ce qui reste revendicable (formulation)

« Dans les pièces lues, n'ont pas été trouvés : (a) l'écriture du temps et des agents comme deux sous-groupes de permutations d'un même ensemble d'indices à deux axes, avec le groupe plein, **comme instance** du cadre de l'invariance de groupe (Koning 2310.01153), mise au service d'énoncés négatifs face à un attaquant ; (b) la lecture adverse de l'identité de rebrassage — un attaquant qui réarrange dans H puis rebrasse uniformément sur H est indétectable par tout moniteur de scores dès que la loi honnête est H-invariante — et sa version par sous-groupe chiffrée sur un exemple (le groupe compte), l'identité elle-même étant classique ; (c) la distinction entre attaque à multi-ensemble préservé et attaque à marginales préservées, avec ses conséquences de signe pour la somme, le processus e et le max (Slepian) ; (d) les garanties trajectorielles du balayage, de la somme cumulée de Page et de la co-élévation sous dommage structuré, et la neutralisation des statistiques d'ordre globales par un attaquant adaptatif ; (e) l'énoncé T4 ; (f) la transposition aux activations réelles et sa mesure. »

## 8. Ce qu'une phrase publique sur T ne doit pas affirmer

1. Que l'écriture commune du temps et des agents par sous-groupes de permutations est un cadre nouveau : c'est une instance du test d'invariance sous un groupe compact et ses sous-groupes (Koning, p. 13, 21-23) ; il faut citer Koning (et Eaton 1989 pour le fond).
2. Que l'identité de T2 (rebrassage uniforme ⇒ loi honnête exacte) est un résultat mathématique nouveau : elle découle en deux lignes du lemme 1 et de la section 2.5 de Koning (p. 8-9), classiques.
3. Que le rebrassage qui aveugle les tests d'échangeabilité est une découverte : Vovk l'utilise comme contrôle (p. 10, 12-13, 15).
4. Que T2 est, ou généralise, le résultat d'impossibilité de Ramdas, Ruf, Larsson et Koolen : le leur porte sur les surmartingales non négatives dans la filtration des données, pas sur l'égalité des lois ; et il ne dit pas que l'échangeabilité est indétectable séquentiellement (leur e-processus a puissance un contre les alternatives markoviennes, p. 26).
5. Qu'« aucun test séquentiel d'échangeabilité ne peut détecter » quoi que ce soit (faux, Ramdas et al. p. 26 ; Koning section 5) ; ou que l'aveuglement d'un moniteur construit comme surmartingale d'échangeabilité dans la filtration des scores est dû à l'attaquant (il l'est avant toute attaque, Ramdas et al. p. 3, 17-18).
6. Que la distinction marginales contre multi-ensemble est sans antécédent dans la littérature des tests d'invariance : Koning (p. 38) montre que des marginales égales ne garantissent pas le taux d'un test d'invariance (moitié qualitative) ; seuls les signes et l'usage comme classes d'attaque restent non trouvés.
7. Que « libre » signifie « trou du champ » : non trouvé dans trois pièces, plus les lots antérieurs ; les voisins non lus ci-dessous restent à lire.

## 9. Voisins nommés dans les pièces et non lus (page où ils sont nommés)

Les plus probables pour T en premier.
- Koning et Hemerik (2023), « More Efficient Exact Group Invariance Testing: using a Representative Subgroup », Biometrika — Koning p. 12, 13, 31 (choix du sous-groupe et puissance : voisin direct de « le groupe compte »).
- Koning (2024b), « More power by using fewer permutations », Biometrika — Koning p. 13.
- Chiu et Bloem-Reddy (2023), « Non-parametric hypothesis tests for distributional group symmetry », arXiv 2307.15834 — Koning p. 10 (“Ranks, signs and normalization are special cases of a representative inversion”).
- Lardy et Pérez-Ortiz (2024), « Anytime-valid tests of group invariance through conformal prediction », arXiv 2401.15461 — Koning p. 6 (ils “apply this to testing group invariance in a setting similar to Section 6 and Appendix 9.”).
- Pérez-Ortiz, Lardy, de Heide, Grünwald (2024), « E-statistics, group invariance and anytime-valid testing », Annals of Statistics — Koning p. 5-6 (Koning note qu'ils “require that the group action is free, which means that if” … et affirme : “This means that the settings do not overlap, except for the uninteresting setting in which the group only contains the identity element.”, p. 6 ; à vérifier sur la source).
- Saha et Ramdas (2024), « Testing exchangeability by pairwise betting », AISTATS — Koning p. 22 (“The idea to test sequential invariance of all observations by batching units into pairs has been independently explored by Saha and Ramdas”).
- Ramdas, Barber, Candès, Tibshirani (2023a), « Permutation tests using arbitrary permutation distributions » ; Hemerik et Goeman (2018), « Exact testing with random permutations » — Koning p. 13.
- Eaton (1989), « Group invariance applications in statistics », IMS (source classique du lemme 1) — Koning p. 6, 8.
- Koning et van Meer (2025), « Sequentializing a test: Anytime validity is free », arXiv 2501.03982 (dans le lot 8, hors de mon mandat) — Koning p. 19, 35, 37.
- Kashlak (2022), « Asymptotic invariance and robustness of randomization tests » — Koning p. 9.
- Vovk (2025), « Testing exchangeability in the batch mode with e-values and markov alternatives » ; Wang et Ramdas (2022), Ignatiadis, Wang, Ramdas (2023) (e-valeur « soft-rank ») — Koning p. 6.
- Ramdas, Ruf, Larsson, Koolen (2022a), « Admissible anytime-valid sequential inference must rely on nonnegative martingales », arXiv 2009.03167 — Koning p. 19, 28 ; Ramdas et al. p. 3 et suivantes.
- Vovk, Petej, Nouretdinov, Ahlberg, Carlsson, Gammerman (2021), « Retrain or not retrain: Conformal test martingales for change-point detection », arXiv 2102.10439 — Ramdas et al. p. 23.
- Manole et Ramdas (2021), filtrations échangeables et sous-martingales inverses, arXiv 2103.09267 — Ramdas et al. p. 27.
- Ho et Wechsler (2010), « A martingale framework for detecting changes in data streams by testing exchangeability » — Vovk p. 2.
- Fedorova, Nouretdinov, Gammerman, Vovk (2012), « Plug-in martingales for testing exchangeability on-line » — Vovk p. 11.
- Volkhonskiy et al. (2017), « Inductive conformal martingales for change-point detection » ; McDonald (1990), « A cusum procedure based on sequential ranks » — Vovk p. 16.
- Wald et Wolfowitz (1943), test exact du caractère aléatoire fondé sur la corrélation sérielle ; Bartels (1982), version des rangs du rapport de von Neumann — Vovk p. 5, 6 (voisins classiques du volet « autocorrélation et suites » de T3).

## 10. Ce que je n'ai pas fait

- Je n'ai lu aucun autre PDF du lot 8 (en particulier ni 2501.03982, ni 1906.08938, ni 2605.16140, ni math/0410072) ni aucun des voisins de la section 9.
- Je n'ai pas lu les lignes 190 à 215 du programme ni la décision N-013 que cite la consigne commune : la consigne de mandat nommait seulement les lignes 85 à 125 et les extraits ci-dessus.
- Je n'ai pas exécuté la routine de reprise du dépôt (registres interdits par la consigne) ; aucune commande git ; aucun appel réseau ni de modèle ; aucune recherche récursive dans le dépôt.
- Je n'ai pas rédigé la phrase publique qui déclarerait T (rôle exclu).
- La seule « recherche » de mots a porté sur les textes extraits des trois pièces, dans mon dossier de travail.

## 11. Refus

Aucun refus d'un contrôle de permissions, d'un crochet ou d'un classifieur. Aucune ouverture fautive.
