# Rapport d'antériorité — théorème négatif « T » — lot 8 (trois pièces sur l'échangeabilité et l'invariance de groupe) — v2

- Date : 2026-11-13 ; travail de la version 2 commencé à 22:58:42 UTC, fin de rédaction 23:04:20 UTC (heures relevées par `date -u`). Lecture initiale (version 1) : 22:37:53 à 22:47:00 UTC.
- Lecteur : modèle A ; contre-lecteur : modèle B ; A ≠ B. Le lecteur n'a écrit ni le programme, ni les décisions, ni la contre-lecture.
- Rapport remplacé : `docs/sources/lecture-pdf-niveau3/compte-2/rapport-T-lot8-v1.md`, sha256 `443a83f971e691af1c64c7aa49490398c1badffb5e9986a226e05f60719feedf`, archivé sans modification (son archive : `fichiers-de-travail-T-lot8-v1.tar`, `a1d6d7a4ec39effa1b4dee3bbc3743132f8642a817cfcfbbe095afdc11eb66a9`).
- Contre-lecture intégrée : `docs/sources/lecture-pdf-niveau3/compte-2/contre-lecture-rapport-T-lot8-v1.md`, sha256 `3f950c920f54ede9e195b521af437cc2423764175611ab49479cd42099a89883` (verdict du contre-lecteur : « tient avec corrections », trois constats majeurs A, B, C, aucun bloquant, mineurs D à J) ; son archive `fichiers-de-travail-contre-lecture-T-lot8-v1.tar`, sha256 `5e28b8453a4d6adc637efe37a4480fb5a3c3126f35eea4f6e45ae350f701b4b1` (empreintes vérifiées avant lecture ; archive extraite dans un sous-dossier neuf du dossier de travail).
- Mandat : verdict d'antériorité sur le seul énoncé T (décision N-003), par lecture intégrale de trois PDF.

## Empreintes des trois pièces (vérifiées contre leur compagnon `.sha256` : concordance des trois)

| fichier | pages | empreinte sha256 |
|---|---|---|
| `2310.01153v5.pdf` (Koning, « Measuring Evidence against Exchangeability and Group Invariance with E-values ») | 45 | `e8cd3532247d69817c47ecf7773c1da5318e87404b9e29d3d95f6fef69ab0544` |
| `2102.00630v4.pdf` (Ramdas, Ruf, Larsson, Koolen, « Testing exchangeability: fork-convexity, supermartingales, and e-processes ») | 34 | `2ada73f4abaf779b06baa558f49893678feec1d5b1451e083e842dd14117fd57` |
| `1906.09256v3.pdf` (Vovk, « Testing randomness ») | 34 | `0a9a1f2c7e96107f4f573e9aa3dd8f1d79798b84cbbd9923bd3db2ecb81efbe3` |

Dossier des pièces : `/tmp/claude-0/-home-user-controle-ia-travail/7e7693dc-fcf8-5081-b2b3-044ac9061481/scratchpad/pieces-10016a61/docs/sources/pdf/niveau3-v1/lot8/` (branche `prep/etat-de-l-art-niveau3-pieces-v1`, tête `10016a61`). Numérotation : page du fichier ; dans les trois pièces elle coïncide avec le numéro imprimé en pied de page.

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
10. Pour la version 2 : `docs/sources/lecture-pdf-niveau3/compte-2/contre-lecture-rapport-T-lot8-v1.md` (en entier) ; son archive, extraite (seul `citations-contre-lecture-T-v1.json` a été rejoué par mon script : 41 citations, 0 échec ; les autres fichiers extraits n'ont pas été ouverts) ; mon propre `rapport-T-lot8-v1.md` (relu).
11. Relectures ligne à ligne pour la version 2, sur le texte extrait page à page : Koning p. 8, 9, 11, 20 à 24, 26, 37 à 39 ; Ramdas et collègues p. 3, 6, 8, 11, 12, 17, 20, 21, 22 ; Vovk p. 5, 8, 17, 25, 33.

Rien d'autre n'a été ouvert. Aucune ouverture fautive. Aucun refus d'un contrôle de permissions, d'un crochet ou d'un classifieur.

## Contrôle des citations

- Script : `verifier_citations_v1.py` (inchangé depuis la version 1), lancé par `python3 -I` : empreinte du PDF, extraction de la page par `pdftotext` avec et sans `-layout`, normalisation (espaces, ligatures, césures avec et sans trait d'union réel, apostrophes, guillemets, tirets), recherche de la citation. Essais de la version 1 : cas juste réussi, trois cas altérés (mot changé, page fausse, empreinte fausse) en échec, comme attendu (journal `journal-T-v1.txt`).
- **Citations contrôlées dans la version 2 : 110. Échecs : 0.** Liste : `citations-T-v2.json`. Un second script (`verifier_rapport_cite_v2.py`) vérifie que les citations entre guillemets anglais doubles du rapport et celles du fichier sont exactement les mêmes.
- Les formules sont décrites ou recopiées à part et marquées « lu sur le PDF, non contrôlé par programme ».

---

## 0. En tête : occupations, même partielles

1. **Unification temps × agents — occupée en partie par Koning (2310.01153v5), plus largement que ne le disait la version 1.**
   - **Écrit dans la pièce.** L'invariance sous un groupe compact quelconque (p. 1, 2) et sous un sous-groupe (p. 13, remarque 6). Le **groupe produit des permutations à l'intérieur de lots qui arrivent l'un après l'autre**, présenté comme sous-groupe des permutations de l'ensemble des observations individuelles, plus faible que l'échangeabilité pleine (p. 21-23, exemples 10 et 13 ; p. 35, exemple 14). Dans la simulation 7.1 (p. 23-24), **le lot est un intervalle de temps et ses éléments sont des unités** : c'est, au nom près, le sous-groupe « permutations des agents à l'intérieur de chaque pas » de N-003.
   - **Pas écrit comme groupe.** Le sous-groupe « temps à l'intérieur de chaque agent » serait une autre instance de l'exemple 10 (un lot par agent). Koning ne le pose pas : dans l'application au « hot hand », il multiplie des e-valeurs calculées joueur par joueur et justifie le produit par l'**indépendance** des e-valeurs (p. 26). Que ce produit teste l'invariance sous ce groupe produit est une déduction du lecteur.
   - **Non fait.** Le tableau à deux indices I ⊂ {1..N} × {1..T} où la même unité revient d'un pas à l'autre ; les deux partitions (par agent, par pas) du même ensemble d'indices prises ensemble, avec le groupe plein ; l'affirmation que le temps et les agents sont deux sous-groupes d'un même objet ; l'usage de ce cadre pour un énoncé négatif face à un attaquant.
2. **T2, noyau probabiliste — occupé en partie par Koning, comme fond classique attribué à Eaton (1989).**
   - **Imprimé.** L'identité du rebrassage seul : une variable invariante a la même loi que sa transformée par un élément uniforme indépendant du groupe (lemme 1, condition 3, p. 8). Pour une loi quelconque, la transformée a la loi moyennée sur le groupe (section 2.5, p. 9). Les autres briques : pour un point fixé, son image par un élément uniforme est uniforme sur son orbite (p. 11, p. 39) ; absorption de la mesure de Haar (p. 9) ; condition 5 du lemme 1 (p. 8).
   - **Non imprimé.** La composition avec un réarrangement π_Y qui dépend des données : elle est déduite par le lecteur, en deux lignes. Pas davantage la lecture adverse (attaque indétectable, défenseur sans recours).
3. **T2, volet « le groupe compte » — voisin proche chez Koning.** Le fait qualitatif est imprimé, du côté du testeur : tester l'invariance sous un sous-groupe moins riche, c'est tester une hypothèse plus large et perdre de la puissance (remarque 12, p. 23 ; cas extrême de l'exemple 12, p. 23). L'exemple 18 (p. 37) exhibe une loi invariante sous des permutations par blocs seulement. Non écrits : la lecture du côté de l'attaquant et l'exemple chiffré à trois agents.
4. **T2, mécanisme du rebrassage — contre-indice chez Vovk (1906.09256v3).** Permuter au hasard un jeu de données non aléatoire rend le pari « futile » (p. 10, 12, 13, 15). C'est un contrôle de bon sens, sur le groupe plein, sans attaquant.

Restent non occupés :
- T1 (voisin) ;
- T3 (voisins seulement) ;
- la distinction C/K et ses signes (voisins, et un contre-indice faible pour la seule moitié qualitative, sur une statistique de position) ;
- T4 (ne touche pas) ;
- la mesure sur activations (ne touche pas).

**Verdict d'ensemble sur T : « occupé en partie ».**

---

## Suite donnée à la contre-lecture

Chaque constat a été vérifié sur le PDF aux pages en cause avant décision ; aucun n'est retenu par déférence. Le contre-lecteur a raison sur les dix points ; sur A et H, la version 2 ajoute une précision qu'il ne donnait pas.

| constat | gravité | décision | où dans la version 2 | motif |
|---|---|---|---|---|
| A — le sous-groupe « agents à l'intérieur de chaque pas » est écrit chez Koning, au nom près | majeur | corrigé | sections 0 (point 1), 2.1, 2.3, 5, 7 (a), 8 (point 8) | Les pages 21, 23-24 et 35 portent un groupe produit par lots dont le lot est un intervalle de temps et dont les éléments sont des unités (“As a batch of data, we consider the combined observations of both the treated and control units that arrived in the previous interval of time.”, p. 24) ; je précise que les unités ne reviennent pas d'un lot à l'autre, ce qui laisse non écrit le tableau à deux indices. |
| B — « c'est exactement le sous-groupe temps à l'intérieur de chaque agent » : trop fort | majeur | corrigé | sections 0 (point 1), 2.3, 5 | La page 26 fonde le produit sur l'indépendance (“the product of independent e-values is also an e-value.”), pas sur un groupe ; le lien au groupe produit est marqué comme déduction du lecteur. |
| C — « le groupe compte » : la remarque la plus proche n'est pas relevée | majeur | corrigé | sections 0 (point 3), 2.1, 2.3, 5, 7 (b), 8 (point 9) | La remarque 12 (p. 23) imprime « sous-groupe moins riche, hypothèse plus large, puissance perdue » (“This shows where the test martingale loses power compared to an e-process.”) ; classement gardé à « voisin », qualifié de proche. |
| D — noyau de T2 : briques citées inexactes | mineur | corrigé | sections 0 (point 2), 2.1, 2.3 | Les conditions 3-4 du lemme 1 supposent la variable invariante, ce que π_Y(Y) n'est pas a priori ; les briques justes sont la section 2.5 pour une loi quelconque (“We can also express this in terms of random variables”, p. 9), l'uniformité de l'image d'un point fixé (p. 11, 39), l'absorption de Haar (p. 9) et la condition 5 (p. 8). |
| E — Ramdas et collègues, C et K : glose non portée par la page ; section 4.3 non relevée | mineur | corrigé | sections 3.1, 3.3 | La pièce ne parle ni de stationnarité ni de marginale conservée (elle fixe seulement le premier tirage “say, for simplicity with”, p. 6) ; la figure 5 (p. 21) oppose dépendance détectée et probabilités variables non détectées. |
| F — Ramdas et collègues : condition de la « puissance un » omise | mineur | corrigé | sections 3.1, 8 (point 4) | Le théorème 7 vaut pour une chaîne non de Bernoulli et “provided the chain does not have any absorbing states” (p. 11). |
| G — Ramdas et collègues, T3 : l'exemple 9 est un voisin, pas seulement une limite | mineur | corrigé | sections 3.3, 5 | Des alternatives “that appear to be Bernoulli when summarized by only first order transition parameters” (p. 11) rendent l'e-processus d'ordre un sans puissance (p. 12) : dépendance invisible à une statistique d'ordre donnée, sans adversaire. |
| H — section « phrase publique » : trois lignes manquent, une à préciser | mineur | corrigé | section 8 (points 6, 8, 9, 10) | Lignes 8 à 10 ajoutées et ligne 6 précisée (statistique de position, vecteur “which is not an exchangeable n-vector”, p. 38) ; pour la ligne 10, je précise que Vovk énonce le cas des martingales (p. 8) et que Ramdas et collègues prouvent le cas plus fort des surmartingales non négatives. |
| I — voisins nommés et non lus : manques | mineur | corrigé | section 9 | Les pages de chaque voisin ajouté ont été vérifiées sur le texte extrait (Lehmann et Stein p. 2, 4, 5, 16, 31 ; Chung et Fraser p. 13 ; Ritzwoller et Romano, Miller et Sanjurjo p. 5, 17, 26 ; Kallenberg p. 10, 11, 35 ; Vovk 1986 p. 4, 31-34 ; Page, Poor et Hadjiliadis, Shiryaev p. 15-16, 20 ; Žitković, Delbaen, Epstein et Schneider p. 14). |
| J — Vovk, T2 : appui à resserrer | mineur | corrigé | sections 4.1, 4.3 | L'appui direct est la page 25 (“are IID and uniform on [0, 1] under any exchangeable probability measure”) et la page 15, non la seule remarque 3.2 ; classement inchangé. |

---

## 1. Ce que dit T (rappel, pour la confrontation)

Décision N-003 (l. 17-52) et note v2 (section 4) :
- **Cadre.** Scores X_{i,t} sur I ⊂ {1..N} × {1..T} ; trois groupes de permutations de I : le temps à l'intérieur de chaque agent, les agents à l'intérieur de chaque pas, toutes les permutations.
- **T1.** Une attaque de classe C (π_Y ∈ G) laisse inchangée, trajectoire par trajectoire, toute statistique G-invariante.
- **T2.** P₀ est invariante sous H ; l'attaque est X = σ ∘ π_Y(Y), avec π_Y ∈ H et σ uniforme sur H, indépendante ; alors X ~ P₀ exactement. « Le groupe compte » : dans l'exemple à trois agents, un rebrassage sur tout I est détecté, un rebrassage du temps agent par agent ne l'est pas.
- **T3.** Bornes trajectorielles du balayage, de Page et de la co-élévation ; neutralisation de l'autocorrélation et du test des suites par un attaquant adaptatif.
- **Classes C et K et leurs signes.** La somme et le processus e passent au-dessus de leur taux sous dépendance positive, en dessous sous dépendance négative ; le max reste à son taux ou en dessous (Slepian).
- **T4.** La somme lue séquentiellement, sous sommes partielles dominées.
- **Revendiqué :** l'unification, la distinction C/K et ses signes, les garanties locales face à un attaquant adaptatif, la transposition aux activations et sa mesure. T1 est avoué élémentaire.

---

## 2. Fiche — Koning, 2310.01153v5 (45 pages, arXiv math.ST, version du 10 février 2026 imprimée en p. 1 ; aucune venue de revue imprimée)

### 2.1 Ce que fait l'article
- **Objet.** “We study e-values for quantifying evidence against exchangeability and general invariance of a random variable under a compact group.” (p. 1). “Permutation tests are a special case of more general group invariance tests” (p. 2).
- **Fond sur l'invariance** (section 2, attribué à Eaton 1989, p. 6, 8).
  - Le lemme 1 énonce des conditions équivalentes : “Y is an invariant random variable under a compact group G if one of the following equivalent conditions holds” (p. 8).
  - Décomposition en orbites : “any invariant probability may be viewed as a mixture over uniform probabilities on orbits.” (p. 8) ; “Condition 4 states that a draw from an invariant random variable Y can be decomposed (de-convolved) into first sampling an orbit representative” (p. 8) ; “Condition 5 restates this in terms of orbits: a draw from Y can be viewed as first sampling an orbit” (p. 8).
  - Ce qu'on teste : “This decomposition is the key to testing invariance, where the idea is to effectively discard the first part of this sampling process, and only test whether Y is uniform conditional on the orbit in which it is observed.” (p. 9).
  - Absorption de la mesure de Haar, “which follows from Lemma 1 by considering the invariant random variable” G lui-même, et “the fact that the Haar measure on a compact group is both left- and right-invariant.” (p. 9).
  - Section 2.5 : “We can construct an invariant probability from a probability measure P by averaging it over the group” (p. 9). Pour une loi déjà invariante, “so that this averaging has no effect.” (p. 9). Pour une loi quelconque, “We can also express this in terms of random variables” (p. 9).
  - Formules (lu sur le PDF, non contrôlé par programme) :
    - lemme 1, p. 8 : (3) Y =d GY avec G ~ Unif(G) indépendant ; (4) Y =d G[Y] ; (5) Unif(O_Y) est une version de la loi conditionnelle de Y sachant O_Y ;
    - p. 9 : GG =d GG =d G ;
    - section 2.5, p. 9 : P̄ := E_G[GP], et si Y ~ P alors GY ~ P̄, pour P quelconque ;
    - p. 11 et preuve du théorème 1, p. 39 : pour y fixé, Gy ~ Unif(O_y).
- **Caractérisation** (section 3).
  - “It states that an e-value is valid for group invariance if and only if it is valid for a uniform distribution on each orbit.” (p. 11).
  - “In particular, we may view the problem of testing group invariance as first observing the orbit” (p. 11).
  - E-valeur exacte générique : théorème 3, p. 12 (formule lue sur le PDF, non contrôlée : ε_T(y) = T(y) / E_G T(Gy)). Version de Monte-Carlo : théorème 4, p. 13.
- **Sous-groupes.**
  - “One may also replace G in (3.2) with a random variable that is uniform on a compact subgroup [Chung and Fraser, 1958].” (p. 13).
  - “As invariance under G implies invariance under all its subgroups, this guarantees the resulting e-value is valid.” (p. 13).
  - “Koning and Hemerik [2023] note that we can strategically select the subgroup based on the test statistic and alternative to increase power.” (p. 13).
  - “Koning [2024b] observes that this can even yield methods that are more powerful than using the entire group G.” (p. 13).
- **E-valeurs optimales** (section 4).
  - “This recovers the main result of Lehmann and Stein [1949].” (p. 16).
  - Une fonction invariante est constante sur les orbites : “thus constant on each orbit and so absorbed into the multiplier” (p. 17).
  - Pour les permutations, l'orbite est le multi-ensemble : “Permuting such a shot sequence exactly fixes the number of hits” (p. 17).
- **E-processus** (section 5).
  - “In addition, we characterize e-processes for group invariance for arbitrary filtrations, and provide tools to construct them.” (p. 1).
  - “The key challenge when constructing e-processes for group invariance is that the sequential analogue of Corollary 1 is typically not useful.” (p. 18).
- **Martingales de test sous une suite de groupes** (section 6, p. 20-23, relue ligne à ligne).
  - Lien avec Ramdas et collègues : “The second is as an e-process that is anytime valid for the fork-convex hull of a hypothesis” (p. 20). Les martingales de test sont plus exigeantes, ce qui “this necessarily makes them less powerful than e-processes in settings where this additional guarantee is not important.” (p. 21).
  - Construction : “We show how they may easily be constructed by tailoring conditional e-values for their increments based on subgroups that stabilize the previous data.” (p. 5).
  - Exemple 10, invariance par lots : “Suppose we sequentially observe potentially unequally sized batches of data” (p. 21), avec pour groupe le produit des groupes de permutations de chaque lot (formule lue sur le PDF, non contrôlée : G_n = P_0 × P_1 × … × P_n), “where Pi is the group of permutations acting on the batch Yi” (p. 21).
  - La page 22 précise : “then within-batch exchangeability is weaker than exchangeability of individual observations: we exclude permutations that swap observations across batches.” ; et : “Specifically, the groups we consider here are subgroups of the permutations on the set of the individual observations.”
  - Remarque 12 (p. 23) : avec la martingale de test, “we are testing a larger hypothesis than” l'invariance sous le groupe d'origine, et “This shows where the test martingale loses power compared to an e-process.”
  - Exemple 12 (p. 23) : le sous-groupe stabilisateur se réduit à l'identité, “only contains the identity element for each n.”, d'où “A consequence is that it is impossible to sequentially test exchangeability with a test martingale under the filtration” des données, “as previously observed by Vovk [2021] and Ramdas et al.” (p. 23) ; “Our discussion gives some context around their impossibility result” (p. 23).
  - Exemple 13 (p. 23) : “This means rejecting within-batch exchangeability also rejects exchangeability.”
- **Simulation 7.1** (p. 23-24).
  - Les lots sont des intervalles de temps et leurs éléments des unités : “In each interval of time, we receive the outcomes of a number of treated and control units” (p. 23) ; “As a batch of data, we consider the combined observations of both the treated and control units that arrived in the previous interval of time.” (p. 24).
  - Hypothèse testée : “In particular, we will test the null hypothesis that the elements of a batch” sont échangeables (p. 24).
  - Les unités d'un lot sont nouvelles : elles ne reviennent pas d'un lot à l'autre (lu sur le PDF, p. 23-24).
- **Réduction par statistique équivariante.**
  - “by using a statistic that is equivariant under a subgroup of the group. The problem then reduces to testing invariance of the statistic under the subgroup.” (p. 5).
  - “Hence, the hypothesis of F invariance of H(X) is at least as large as that of G invariance of X.” (p. 34).
  - “In Example 14, we illustrate this approach by showing how we may reduce from exchangeability” (p. 35), avec des blocs de temps consécutifs d'une seule suite, “where Pi permutes the observations within the ith batch of data” (p. 35).
- **Invariance « à travers une statistique » et contre-exemples.**
  - “this condition is insufficient for testing invariance: we include a counterexample in Appendix 10.2.” (p. 9).
  - Exemple 18 (p. 37) : “In Example 18, the underlying random variable is not invariant, but looks invariant through certain statistics.” ; “Here, the resulting order of the numbers is not invariant under all permutations” ; “only the 8 orders 1234, 1243, 2134, 2143, 3412, 3421, 4312 and 4321 can occur” — une loi invariante sous des permutations par blocs seulement ; “The order does look exchangeable through the statistic that returns only the first position.”
  - Annexe 10.2 (p. 38) : marginales identiques et dépendance choisie (“Moreover, it puts no restriction on the dependence structure of the individual elements, which we will exploit.”), sur un vecteur “which is not an exchangeable n-vector” dont toutes les coordonnées sauf la première sont égales. Pour le test fondé sur la première coordonnée, “the probability of rejection equals” un demi quel que soit le niveau (valeur lue sur le PDF), “so that the group invariance test is not valid.”
- **Application.**
  - “We leverage the powerful merging properties of e-values by multiplying e-values across players to obtain a more powerful e-value.” (p. 5).
  - La justification imprimée du produit est l'indépendance : “the product of independent e-values is also an e-value.” (p. 26).
  - “We apply this idea to the controlled shooting experiment data collected by Gilovich et al. [1985], with 26 shooters taking up to 100 shots each.” (p. 26) ; “Table 1 reports the product of the e-values for the individual shooters.” (p. 26).
  - L'alternative : “For simplicity, we say a player is 'hot' if they hit k shots in a row.” (p. 26) ; “long sequences are required to detect a hot hand” (p. 26).

### 2.2 Chiffres (nature indiquée)
- Simulation cas-témoins (p. 24, figure 1, p. 25) :
  - 40 lots, θ = 25, 1 000 simulations, 100 permutations de Monte-Carlo (auteurs) ;
  - « roughly 95% » des e-processus au-dessus de 20 au lot 23 sous l'alternative (auteurs, texte p. 24).
- Hot hand :
  - tableau 1 p. 26 : produit des e-valeurs 0,007 / 0,180 / 3,108 / 4,460 / 7,489 / 5,525 selon le déclencheur et β (auteurs) ;
  - suite 111010 : e-valeur ≈ 1,0095 (auteurs, p. 26).
- Contre-exemple p. 38 : taux de rejet 0,5 pour α = 1/3 (k = 2, n = 3) (auteurs).

### 2.3 Confrontation, composante par composante
- **Unification — occupée en partie.**
  - Fait :
    - le cadre général (p. 1, 2, 13) ;
    - le groupe produit des permutations à l'intérieur de lots, sous-groupe des permutations de toutes les observations, emboîté sous l'échangeabilité pleine (p. 21-23, 35) ;
    - dans la simulation 7.1, des lots indexés par le temps et faits d'unités (p. 23-24), soit, au nom près, le sous-groupe « agents à l'intérieur de chaque pas ».
  - Hors groupe : le produit des e-valeurs joueur par joueur (p. 5, 26) est justifié dans la pièce par l'indépendance, non par un groupe. Qu'il revienne à tester l'invariance sous le groupe produit « temps à l'intérieur de chaque agent » est une **déduction du lecteur** (calcul, non imprimé) : sachant les orbites de chaque joueur, la loi invariante est le produit des lois uniformes sur ces orbites.
  - Non fait :
    - le tableau à deux indices où la même unité revient d'un pas à l'autre ;
    - les deux partitions du même ensemble d'indices prises ensemble, avec le groupe plein ;
    - l'énoncé « deux sous-groupes d'un même objet » ;
    - l'usage négatif face à un attaquant.
- **T1 — voisin.**
  - Ce que la pièce écrit, le dual de T1 : une fonction invariante est constante sur les orbites (p. 17) ; l'orbite des permutations est le multi-ensemble (p. 17) ; tester l'invariance revient à jeter l'information d'orbite (p. 9, 11).
  - L'exemple 18 (p. 37) exhibe une loi non invariante qui « paraît » invariante à travers certaines statistiques.
  - Absent : l'énoncé qu'une statistique invariante garde son taux sous un réarrangement choisi par un attaquant.
- **T2, identité — occupée en partie (noyau probabiliste).**
  - Raisonnement du lecteur (calcul, non imprimé dans la pièce). Posons Z = π_Y(Y). Comme π_Y ∈ H, Z a la même orbite que Y, donc la même loi d'orbite. Soit σ uniforme indépendante :
    - pour tout point fixé, son image par σ est uniforme sur son orbite (p. 11, p. 39) ;
    - donc, sachant l'orbite, σZ est uniforme sur l'orbite ; de façon équivalente, σZ a la loi moyennée sur le groupe de la loi de Z (section 2.5, p. 9, valable pour une loi quelconque) ;
    - P₀ invariante est le mélange des lois uniformes sur les orbites, selon cette même loi d'orbite (p. 8, condition 5) ;
    - d'où X = σZ ~ P₀.
  - Ce qui est imprimé : l'identité du rebrassage seul appliqué à une variable invariante (lemme 1, condition 3, p. 8) et ses briques.
  - Ce qui ne l'est pas : la composition avec un réarrangement dépendant des données ; la lecture adverse (attaque indétectable, défenseur sans recours), absente des trois pièces.
- **T2, « le groupe compte » — voisin proche.**
  - Le fait qualitatif est imprimé du côté du testeur : sous-groupe moins riche, hypothèse plus large, puissance perdue (remarque 12, p. 23, et son cas extrême, l'exemple 12, p. 23).
  - Autres appuis : l'invariance par lots est plus faible que l'échangeabilité (p. 22) ; le choix du sous-groupe change la puissance (p. 13) ; l'exemple 18 (p. 37) exhibe une loi invariante sous des permutations par blocs seulement.
  - Non écrit : la lecture du côté de l'attaquant (une loi honnête invariante seulement sous un sous-groupe laisse détecter un rebrassage plus large) et l'exemple chiffré à trois agents.
- **T3 — ne touche pas.**
  - Aucune statistique locale (balayage, Page, co-élévation) ; aucune garantie trajectorielle ; aucun attaquant adaptatif. Le mot « adaptive » ne qualifie que la taille des lots et la validité (p. 21, 23).
  - L'alternative « hot hand » (série de k réussites, p. 26) n'est qu'un voisin lointain de « r actions consécutives hautes ».
- **Classes C et K — voisin ; contre-indice faible pour la seule moitié qualitative.**
  - L'annexe 10.2 (p. 38) montre que des marginales identiques, avec une dépendance positive parfaite choisie, suffisent à fausser le taux d'un test d'invariance. Mais ce test est fondé sur une **statistique de position** (la première coordonnée) : ce n'est ni la somme, ni le max, ni un processus e.
  - Non fait : le contraste C/K comme classes d'attaque ; les signes (somme et processus e au-dessus du taux sous dépendance positive, en dessous sous dépendance négative) ; le max sous Slepian. Les mots « copula » et « Slepian » n'apparaissent pas dans le texte extrait.
- **T4 — ne touche pas.**
- **Application aux activations — ne touche pas.**

### 2.4 Limites reconnues, réserves du lecteur
- Groupes compacts supposés partout ; les groupes non compacts ne sont qu'esquissés (remarques 4 et 11, p. 11, 20).
- Aucun résultat « trop beau » : les simulations sont des illustrations. La comparaison avec de la Peña (figure 2, p. 25) est cohérente avec l'inadmissibilité rappelée p. 34.

---

## 3. Fiche — Ramdas, Ruf, Larsson, Koolen, 2102.00630v4 (34 pages, arXiv math.ST, 23 juillet 2021)

Venue non imprimée dans la pièce. Koning la cite p. 28 comme parue dans International Journal of Approximate Reasoning, 141:83-109, 2022.

### 3.1 Ce que fait l'article, et ce qu'établit exactement le résultat d'impossibilité
- **Cadre.** Une seule suite binaire, nul « échangeable », filtration canonique des données : “All martingale statements in this paper will implicitly refer to this canonical filtration.” (p. 3) ; “We now return to the main focus of this paper, which is binary sequences” (p. 17).
- **Impossibilité (exactement).**
  - Énoncés : “Nonnegative supermartingales (NSMs) are a workhorse of sequential inference, but we prove that they are powerless for this problem.” (p. 1) ; “this implies that any NSM under exchangeability is necessarily nonincreasing, hence always yields a powerless test for any alternative.” (p. 1) ; “Theorem 17 proves that every NSM under exchangeability must be a nonincreasing process and thus powerless.” (p. 3).
  - Mécanisme : l'enveloppe fork-convexe fermée du nul contient toutes les lois — “Every law P over the space of binary sequences belongs to the closed fork-convex hull of” (p. 17, théorème 17). D'où : “they are incapable of detecting any deviation from exchangeability.” (p. 18) ; “rendering them powerless to distinguish non-exchangeable distributions from exchangeable ones.” (p. 26).
  - Conséquence : “any Q-safe e-process with nontrivial power cannot be a Q-NSM” (p. 6).
  - Formules (lu sur le PDF, non contrôlé) : définition 10, p. 14 ; théorème 13, p. 16.
- **Ce n'est pas une impossibilité de détecter l'écart à l'échangeabilité.**
  - L'article construit un e-processus sûr, qui n'est pas une surmartingale.
  - Il a puissance un contre les alternatives markoviennes d'ordre un qui ne sont pas de Bernoulli et n'ont pas d'état absorbant : “we prove that it has power one against any first-order Markovian alternative” (p. 26, résumé final), borné par le théorème 7 et sa discussion (p. 11), presque sûrement “provided the chain does not have any absorbing states”.
- **Impossibilités informelles d'une autre nature.**
  - “Since testing arbitrary deviations from exchangeability is information theoretically impossible, we focus on Markovian alternatives.” (p. 1).
  - “This example relies on ensuring that the information required to detect a deviation from the null is exhausted early on in the sequence.” (p. 5).
  - “Recall that it is impossible to detect all deviations from exchangeability.” (p. 18).
  - “In fact, one can argue that it is information theoretically impossible to design any power one test, including tests that are tuned to detect a single change point.” (p. 22) ; “no test can possibly have power one” (p. 22).
  - Clôture convexe : “safe and consistent e-processes do not exist and neither do valid, power-one tests.” (p. 4), pour un nul indépendant et identiquement distribué contre son enveloppe convexe.
- **Lecture « adaptative » de l'enveloppe fork-convexe.** “if Reality wanted to draw an infinite sequence from the fork-convex hull of Q” (p. 26), “each time using the observed data to pick the next (conditional) distribution as it wishes.” (p. 26).
- **Dépendance contre probabilités variables** (section 4.3, p. 20-21). Une source « collante », à fréquences limites égales à un demi, est détectée ; une source de Bernoulli à probabilité variable ne l'est pas : “The right picture confirms that this is due to the Markovian aspect of the source, and not due to the changing probabilities.” (p. 21, figure 5).
- **Ce que l'article ne dit pas.** Ni stationnarité ni marginale conservée : il fixe seulement la probabilité du premier tirage à un demi, “say, for simplicity with” (p. 6, valeur lue sur le PDF).
- **Limite d'ordre.** Des alternatives d'ordre supérieur “that appear to be Bernoulli when summarized by only first order transition parameters” (p. 11) rendent l'e-processus d'ordre un sans puissance (exemple 9, p. 12).
- **Distinction explicite.** “The last setting should especially not be confused with change point detection” (p. 19).
- **Travail le plus proche, selon les auteurs.** “The most directly related work is that of Vovk [36], who proposed a very different approach based on conformal prediction” (p. 8).

### 3.2 Chiffres
- Pluie de Londres : 4 404 jours, 59 % de jours pluvieux (auteurs, p. 23).
- Suite Ber(0,1)⁵⁰⁰⁰ suivie de Ber(0,4)⁵⁰⁰⁰ : p-processus sous 10⁻²⁰ en fin de suite (auteurs, légende de la figure 6, p. 22) ; A_∞ ≈ 10¹⁷ avec l'ajusteur (auteurs, p. 25).

### 3.3 Confrontation
- **Unification — ne touche pas** (une suite, permutations du temps seulement).
- **T1 — ne touche pas.**
- **T2 — voisin, d'une autre nature ; pas une occupation.**
  - T2 est une impossibilité par **égalité des lois** : elle vaut pour tout test et toute filtration.
  - Le théorème 17 est une impossibilité d'une **classe de statistiques** (les surmartingales non négatives sous le nul échangeable, dans la filtration des données). Elle vaut contre toute alternative, et d'autres statistiques y échappent. Les deux ne se recouvrent pas.
  - Ce que le résultat touche : un moniteur construit comme surmartingale d'échangeabilité dans la filtration des scores serait aveugle avant toute attaque. Les remarques informelles (p. 1, 5, 18, 22) sont des voisines de l'esprit « impossibilité sans structure ».
- **T3 — voisin, pour le volet « attaquant adaptatif » et le volet « statistiques d'ordre ».**
  - L'enveloppe fork-convexe est la loi d'une Réalité qui choisit pas à pas (p. 26), contre laquelle toute une classe de statistiques séquentielles est aveugle.
  - L'exemple 9 (p. 11-12) exhibe une dépendance d'ordre deux invisible à la statistique des transitions d'ordre un.
  - Les deux sont sans adversaire du moniteur, sans réarrangement et sans garantie locale.
- **Classes C et K — voisin.**
  - L'e-processus conçu pour les alternatives markoviennes détecte une dépendance entre tirages successifs (p. 11, 26).
  - La section 4.3 oppose une source « collante » à fréquences limites égales, détectée, à une source de Bernoulli à probabilité variable, non détectée (p. 20-21, figure 5).
  - Rien sur le signe de l'erreur de la somme ou du max sous dépendance positive ou négative. L'article ne parle pas de marginales conservées.
- **T4 — ne touche pas.**
- **Activations — ne touche pas.**

### 3.4 Limites reconnues, réserves
- Données binaires (extensions finies, p. 12) et alternatives markoviennes ; l'exemple 9 est une limite reconnue.
- Aucun résultat « trop beau ».

---

## 4. Fiche — Vovk, 1906.09256v3 (34 pages, arXiv math.PR, 29 mars 2020)

Venue non imprimée. Koning cite p. 29, et Ramdas et collègues p. 8 et 26 (référence 36), « Testing randomness online », Statistical Science, 2021. L'identité avec cette pièce est probable, non vérifiée.

### 4.1 Ce que fait l'article
- **Objet.** “This paper reviews known methods of testing the two hypotheses concentrating on the online mode of testing, when the observations arrive sequentially.” (p. 1). La validité est donnée “including conformal versions of the CUSUM and Shiryaev-Roberts procedures.” (p. 1). “Conformal martingales are constructed on top of conventional machine-learning algorithms” (p. 2).
- **Tests en lot.** “Nonparametric statistics provides us with plenty of p-variables for testing exchangeability” (p. 5). Équivariance de la mesure de non-conformité (proposition 2.1, p. 5), et son échec pour le caractère aléatoire : “Let us check that Proposition 2.1 ceases to be true if” (p. 6).
- **Validité.**
  - Proposition 3.1 (p. 7), étendue à l'échangeabilité à horizon fini : “The conclusion of Proposition 3.1 will still hold even if we relax the assumption of” (p. 7).
  - “Conformal martingales are exchangeability martingales, i.e., stochastic processes that are martingales with respect to any exchangeable distribution.” (p. 8).
  - “It is easy to check that for the natural underlying filtration” des observations, “the only exchangeability martingales are almost sure constants.” (p. 8).
  - Appui direct, p. 25 : les valeurs p conformes “are IID and uniform on [0, 1] under any exchangeable probability measure”.
- **Rebrassage comme contrôle** (figures 2 et 4, versions « randomly permuted ») : “after observing the first n digits of a randomly permuted USPS dataset” (p. 10) ; “unlike the more stable right panel showing the p-values for a randomly permuted dataset” (p. 12) ; “The conformal martingale is trying to gamble against an exchangeable sequence of observations, which is futile, and so its value decreases exponentially quickly.” (p. 15).
- **Détection de rupture.**
  - “A typical example of change detection is where we observe attacks, which we assume to be IID, on a computer system.” (p. 15). Les « attaques » sont ici des intrusions observées, pas un adversaire du moniteur.
  - “A standard multistage procedure of raising alarms is the CUSUM procedure proposed by Page” (p. 16).
  - Validité seulement : “we do not expect the first alarm to be raised too soon under the hypothesis of randomness” (p. 17) ; propositions 4.1 et 4.3, corollaires 4.2 et 4.5 (p. 17-20 ; formules lues sur le PDF, non contrôlées).
  - Optimalité non revendiquée : “In this paper we only discuss validity results for CUSUM and Shiryaev-Roberts in the context of randomness testing and do not claim their optimality.” (p. 21) ; “we simply do not have enough structure to specify a meaningful optimization problem.” (p. 21).
- **Efficacité grossière.**
  - “Proposition 5.3 may be interpreted as saying that there is not much difference between testing randomness and testing exchangeability.” (p. 23). Propositions 5.3 et 6.2 : facteurs 1,5·√N et N (lus sur le PDF, non contrôlés).
  - Aléa = échangeabilité + binomialité du compte : “It says, informally, that the randomness of” (p. 33) une suite tient à deux conditions, elle “should be exchangeable, and the number of 1s in it should be binomial” (p. 33) ; une suite “might be perfectly exchangeable whereas it will not be random” (p. 33).

### 4.2 Chiffres
- Test de Bartels sur USPS : p-valeurs 2,7 × 10⁻¹¹ et 7,5 × 10⁻¹⁶ (auteurs, tableau 1, p. 6).
- USPS : valeur finale 4,71 × 10¹⁸ ; 0,0142 sur le jeu permuté au hasard (auteurs, figure 2, p. 10) ; mélange simple 2,18 × 10¹⁰ (auteurs, p. 10).
- Absentéisme : 100,50 ; 0,00841 sur le jeu permuté (auteurs, figure 4, p. 13) ; variante 3 446,75 (auteurs, p. 14).

### 4.3 Confrontation
- **Unification — ne touche pas** (une suite, permutations des observations).
- **T1 — voisin.** La décomposition « aléa = échangeabilité + binomialité » (p. 33, d'après Vovk 1986) sépare l'information d'orbite de l'information intra-orbite. Pas d'attaquant, pas de statistique invariante aveuglée.
- **T2 — contre-indice (mécanisme du rebrassage, groupe plein).**
  - Permuter uniformément un jeu de données en fait une suite échangeable, contre laquelle parier est « futile » (p. 15 ; figures p. 10, 12, 13).
  - Sous toute loi échangeable, les valeurs p conformes sont indépendantes et uniformes (p. 25) : aucune martingale conforme ne croît alors en espérance.
  - Non fait : l'attaquant ; l'égalité exacte à P₀ (le jeu permuté est échangeable, pas nécessairement de loi P₀) ; les sous-groupes.
- **T3 — voisin.** CUSUM de Page et Shiryaev-Roberts conformes, avec des garanties de validité seulement (p. 16-21) ; aucune garantie de détection sous dommage structuré, pas d'attaquant adaptatif.
- **Classes C et K — ne touche pas.**
- **T4 — ne touche pas.**
- **Activations — ne touche pas.**

### 4.4 Limites reconnues, réserves
- Cas binaire et horizon fini pour l'efficacité (p. 3-4).
- Précision des bornes reconnue comme « very low » (p. 27) ; proposition 5.3 dite « very crude » (p. 32) (non contrôlé par programme).
- Aucun résultat « trop beau » : la chute sur les jeux permutés est attendue par construction.

---

## 5. Table composante × article (version 2)

| composante | Koning 2310.01153v5 | Ramdas et al. 2102.00630v4 | Vovk 1906.09256v3 |
|---|---|---|---|
| Unification temps × agents | **occupée en partie** — cadre général, groupe produit par lots, lots indexés par le temps et faits d'unités (p. 13, 21-24, 35) faits ; produit par joueur justifié par l'indépendance, non par un groupe (p. 5, 26) ; tableau à deux indices, deux partitions ensemble, usage négatif non faits | ne touche pas | ne touche pas |
| T1 | voisin (p. 9, 11, 17, 37) | ne touche pas | voisin (p. 33) |
| T2, identité du rebrassage | **occupée en partie** — rebrassage seul imprimé (p. 8-9, 11, 39) ; composition avec un réarrangement dépendant des données déduite ; lecture adverse non trouvée | voisin, autre nature (p. 1, 3, 17-18, 26) | **contre-indice** — groupe plein, sans attaquant (p. 10, 12, 13, 15, 25) |
| T2, « le groupe compte » | **voisin proche** — moitié qualitative imprimée du côté du testeur (remarque 12, p. 23 ; p. 13, 22, 37) | ne touche pas | ne touche pas |
| T3, garanties locales | ne touche pas | ne touche pas | voisin — validité seule du CUSUM conforme (p. 16-21) |
| T3, statistiques d'ordre neutralisées par un attaquant adaptatif | ne touche pas | voisin — Réalité adaptative (p. 26) ; dépendance invisible à l'ordre un (exemple 9, p. 11-12) | ne touche pas |
| Classes C et K, signes, Slepian | voisin ; contre-indice faible, moitié qualitative, statistique de position (p. 9, 38) | voisin — dépendance détectée contre probabilités variables (p. 11, 20-21, 26) | ne touche pas |
| T4 | ne touche pas | ne touche pas | ne touche pas |
| Activations réelles et mesure | ne touche pas | ne touche pas | ne touche pas |

## 6. Verdict d'ensemble sur T

**« occupé en partie »** (inchangé ; la contre-lecture rend le même verdict).

- **Ce qui est imprimé chez Koning.**
  - Le cadre de l'unification : invariance sous un groupe compact quelconque ; groupe produit par lots emboîté dans l'échangeabilité, avec des lots indexés par le temps dans la simulation 7.1.
  - Le noyau probabiliste de T2 (identité du rebrassage seul et ses briques), comme fond classique attribué à Eaton (1989).
  - Le fait qualitatif « sous-groupe plus petit, hypothèse plus large, puissance perdue » (remarque 12).
- **Chez Vovk.** Le mécanisme du rebrassage contre les tests d'échangeabilité, montré en pratique.
- **Chez Ramdas et collègues.** Une impossibilité d'une autre nature (filtration et fork-convexité), qui ne recouvre pas T2.

Aucun théorème, proposition, corollaire, lemme ou remarque des trois pièces n'énonce une composante classée ici « non trouvée » ; la recherche active du contre-lecteur le confirme.

## 7. Ce qui reste revendicable (formulation)

« Dans les pièces lues, n'ont pas été trouvés :
- (a) l'application, à un tableau de scores indexé par l'agent et par le pas, de deux sous-groupes produits de permutations par blocs (par agent et par pas), considérés ensemble avec le groupe plein et mis au service d'énoncés négatifs face à un attaquant. Les deux sous-groupes sont des instances du groupe produit par lots de Koning (2310.01153, exemple 10), et celui « par pas » y est écrit, au nom près, dans la simulation 7.1 ;
- (b) la lecture adverse de l'identité de rebrassage : un attaquant qui réarrange dans H puis rebrasse uniformément sur H est indétectable par tout moniteur de scores dès que la loi honnête est H-invariante. L'identité elle-même est classique et la composition se déduit en deux lignes. De même pour sa version par sous-groupe, lue du côté de l'attaquant et chiffrée sur un exemple ; le fait qualitatif (sous-groupe plus petit, hypothèse plus large, puissance perdue) est imprimé chez Koning (p. 23) ;
- (c) la distinction entre attaque à multi-ensemble préservé et attaque à marginales préservées, avec ses conséquences de signe pour la somme, le processus e et le max (Slepian) ;
- (d) les garanties trajectorielles du balayage, de la somme cumulée de Page et de la co-élévation sous dommage structuré, et la neutralisation des statistiques d'ordre globales par un attaquant adaptatif ;
- (e) l'énoncé T4 ;
- (f) la transposition aux activations réelles et sa mesure. »

## 8. Ce qu'une phrase publique sur T ne doit pas affirmer

1. Que l'écriture commune du temps et des agents par sous-groupes de permutations est un cadre nouveau : c'est une instance du test d'invariance sous un groupe compact et ses sous-groupes (Koning, p. 13, 21-24). Il faut citer Koning, et Eaton (1989) pour le fond.
2. Que l'identité de T2 (rebrassage uniforme ⇒ loi honnête exacte) est un résultat mathématique nouveau : le rebrassage seul est imprimé (Koning, p. 8-9), et la composition avec un réarrangement dépendant des données se déduit en deux lignes.
3. Que le rebrassage qui aveugle les tests d'échangeabilité est une découverte : Vovk l'utilise comme contrôle (p. 10, 12-13, 15).
4. Que T2 est, ou généralise, le résultat d'impossibilité de Ramdas, Ruf, Larsson et Koolen. Le leur porte sur les surmartingales non négatives dans la filtration des données, pas sur l'égalité des lois ; il ne dit pas non plus que l'échangeabilité est indétectable séquentiellement. Leur e-processus a puissance un contre les alternatives markoviennes d'ordre un qui ne sont pas de Bernoulli et sans état absorbant (p. 11, 26).
5. Qu'« aucun test séquentiel d'échangeabilité ne peut détecter » quoi que ce soit (faux : Ramdas et collègues p. 26, Koning section 5). Ni que l'aveuglement d'un moniteur construit comme surmartingale d'échangeabilité dans la filtration des scores est dû à l'attaquant : il l'est avant toute attaque (Ramdas et collègues p. 3, 17-18).
6. Que la distinction entre marginales et multi-ensemble est sans antécédent dans la littérature des tests d'invariance. Koning (p. 38) montre que des marginales égales, avec une dépendance positive parfaite, ne garantissent pas le taux d'un test d'invariance. Mais c'est pour une statistique de position, pas pour la somme ni le max, et sans énoncé de signe : seuls les signes et l'usage comme classes d'attaque restent non trouvés.
7. Que « libre » signifie « trou du champ » : il s'agit de trois pièces, en plus des lots antérieurs, et les voisins non lus ci-dessous restent à lire.
8. Que le sous-groupe « permutations des agents à l'intérieur de chaque pas » est une écriture nouvelle : c'est, au nom près, le groupe produit par lots de Koning, les lots arrivant un par intervalle de temps (p. 21, 23-24).
9. Que « le groupe compte » est un fait nouveau : « sous-groupe moins riche, hypothèse plus large, puissance perdue » est imprimé chez Koning (remarque 12, p. 23). Seuls la lecture du côté de l'attaquant et l'exemple chiffré restent non trouvés.
10. Que l'impossibilité d'une martingale d'échangeabilité non triviale dans la filtration des données est propre à Ramdas et collègues. Vovk énonce le cas des martingales (p. 8) ; Ramdas et collègues prouvent le cas plus fort des surmartingales non négatives (p. 17-18) ; Koning le relit comme dégénérescence d'un sous-groupe (p. 23).

## 9. Voisins nommés dans les pièces et non lus (page où ils sont nommés)

Les plus probables pour T en premier.

**Choix du sous-groupe et puissance** (voisins du volet « le groupe compte ») :
- Koning et Hemerik (2023), « More Efficient Exact Group Invariance Testing: using a Representative Subgroup », Biometrika — Koning p. 12, 13, 31. Voisin direct.
- Koning (2024b), « More power by using fewer permutations », Biometrika — Koning p. 13.
- Chung et Fraser (1958), « Randomization tests for a multivariate two-sample problem » — Koning p. 13. Origine des tests par sous-groupe.
- Lehmann et Stein (1949), « On the theory of some non-parametric hypotheses » — Koning p. 2, 4, 5, 16, 31. Source classique de la puissance des tests d'invariance ; premier endroit où chercher un énoncé « puissance égale au niveau contre une alternative invariante ».

**Tests d'invariance de groupe, séquentiels ou non** :
- Chiu et Bloem-Reddy (2023), « Non-parametric hypothesis tests for distributional group symmetry », arXiv 2307.15834 — Koning p. 10 (“Ranks, signs and normalization are special cases of a representative inversion”).
- Lardy et Pérez-Ortiz (2024), « Anytime-valid tests of group invariance through conformal prediction », arXiv 2401.15461 — Koning p. 6 (ils “apply this to testing group invariance in a setting similar to Section 6 and Appendix 9.”).
- Pérez-Ortiz, Lardy, de Heide, Grünwald (2024), « E-statistics, group invariance and anytime-valid testing », Annals of Statistics — Koning p. 5-6. Koning note qu'ils “require that the group action is free, which means that if” … et affirme : “This means that the settings do not overlap, except for the uninteresting setting in which the group only contains the identity element.” (p. 6) ; à vérifier sur la source.
- Saha et Ramdas (2024), « Testing exchangeability by pairwise betting », AISTATS — Koning p. 22 (“The idea to test sequential invariance of all observations by batching units into pairs has been independently explored by Saha and Ramdas”).
- Ramdas, Barber, Candès, Tibshirani (2023a), « Permutation tests using arbitrary permutation distributions » ; Hemerik et Goeman (2018), « Exact testing with random permutations » — Koning p. 13.
- Koning et van Meer (2025), « Sequentializing a test: Anytime validity is free », arXiv 2501.03982 (dans le lot 8, hors de mon mandat) — Koning p. 19, 35, 37.
- Kashlak (2022), « Asymptotic invariance and robustness of randomization tests » — Koning p. 9.
- Vovk (2025), « Testing exchangeability in the batch mode with e-values and markov alternatives » ; Wang et Ramdas (2022) et Ignatiadis, Wang, Ramdas (2023), pour l'e-valeur « soft-rank » — Koning p. 6.
- Ramdas, Ruf, Larsson, Koolen (2022a), « Admissible anytime-valid sequential inference must rely on nonnegative martingales », arXiv 2009.03167 — Koning p. 19, 28 ; Ramdas et collègues p. 3 et suivantes.

**Fondements probabilistes de l'invariance** :
- Eaton (1989), « Group invariance applications in statistics », IMS — Koning p. 6, 8. Source classique du lemme 1.
- Kallenberg (2011, 2017, 2021) — Koning p. 10, 11, 35. Décomposition des lois invariantes, noyaux d'inversion.
- Vovk (1986), « On the concept of the Bernoulli property » — Vovk p. 4, 31-34. Décomposition « échangeable et compte binomial ».

**Séries et statistiques d'ordre** (voisins de T3) :
- Ritzwoller et Romano (2022), « Uncertainty in the hot hand fallacy: Detecting streaky alternatives to random Bernoulli sequences » ; Miller et Sanjurjo (2018) — Koning p. 5, 17, 26. Puissance de statistiques de séries contre des alternatives « à séries ».
- Wald et Wolfowitz (1943), test exact du caractère aléatoire fondé sur la corrélation sérielle ; Bartels (1982), version des rangs du rapport de von Neumann — Vovk p. 5, 6. Voisins classiques du volet « autocorrélation et suites ».

**Somme cumulée, détection de rupture et martingales conformes** (voisins de T3 et de L) :
- Page (1954), « Continuous inspection schemes » ; Poor et Hadjiliadis (2009), « Quickest Detection » ; Shiryaev (2019), « Stochastic Disorder Problems » — Vovk p. 15-16, 20.
- Vovk, Petej, Nouretdinov, Ahlberg, Carlsson, Gammerman (2021), « Retrain or not retrain: Conformal test martingales for change-point detection », arXiv 2102.10439 — Ramdas et collègues p. 23.
- Ho et Wechsler (2010), « A martingale framework for detecting changes in data streams by testing exchangeability » — Vovk p. 2.
- Fedorova, Nouretdinov, Gammerman, Vovk (2012), « Plug-in martingales for testing exchangeability on-line » — Vovk p. 11.
- Volkhonskiy et al. (2017), « Inductive conformal martingales for change-point detection » ; McDonald (1990), « A cusum procedure based on sequential ranks » — Vovk p. 16.

**Fork-convexité et Réalité adaptative** :
- Manole et Ramdas (2021), filtrations échangeables et sous-martingales inverses, arXiv 2103.09267 — Ramdas et collègues p. 27.
- Žitković ; Delbaen ; Epstein et Schneider (fork-convexité, m-stabilité, « rectangularité ») — Ramdas et collègues p. 14. Voisins du volet « Réalité qui choisit pas à pas ».

## 10. Ce que je n'ai pas fait

- Je n'ai lu aucun autre PDF du lot 8 (ni 2501.03982, ni 1906.08938, ni 2605.16140, ni math/0410072) ni aucun voisin de la section 9.
- Je n'ai pas lu les lignes 190 à 215 du programme ni la décision N-013 que cite la consigne commune : mon mandat nommait seulement les extraits listés plus haut.
- Je n'ai pas vérifié les démonstrations des pièces ; j'ai vérifié ce que les pages énoncent. Les figures n'ont été lues que par leurs légendes et le texte.
- Je n'ai pas modifié la version 1 ni la contre-lecture.
- Je n'ai pas exécuté la routine de reprise du dépôt (les registres sont interdits par la consigne).
- Aucune commande git, aucun appel réseau ni de modèle, aucune recherche récursive dans le dépôt.
- Je n'ai pas rédigé la phrase publique qui déclarerait T (rôle exclu).

## 11. Refus

Aucun refus d'un contrôle de permissions, d'un crochet ou d'un classifieur. Aucune ouverture fautive.
