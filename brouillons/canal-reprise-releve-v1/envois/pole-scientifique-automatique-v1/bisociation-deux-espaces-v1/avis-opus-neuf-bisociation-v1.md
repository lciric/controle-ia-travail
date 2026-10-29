# Avis d'un Opus neuf — la recombinaison bisociative à deux espaces — v1

- Modèle : Opus 5.5 (`claude-opus-5-5`), sous-agent neuf. Heure de début, lue sur `date -u` : 2026-10-29T12:18:14Z.
- **Non-auteur** : je n'ai écrit ni la question, ni les pièces A à D, ni aucun code du pôle. Avis lu à côté de la synthèse, non compté dans « commun ».
- Interdits respectés : ni `donnees/`, ni branche git, ni `prereg/P3-consignes-v1.md`, ni `diag/*/traces` ; aucun réseau, aucune dépense, rien scellé.
- Pièces lues (SHA-256 calculé par moi avant rédaction) : question : `73a30ab727445969b7ecb8300ba0fef5efd7dfcf9c59cd93943d6ce77e1c4cc3` ; A `orchestrateur-pole-v7/pole/recombinaison.py` : `71faad38644c77ae2cc21f23bfb1011c48fe674a08e542983819425ee47bd3d0` ; B `trancher-recombinaison-v1.md` : `72cff8a067641cab173f3b6fbba32976a64989ded279d078ec4da432a582e4bf` ; préenregistrement : `5335614b2b8b38deb50408c4755401242e5a8436f82b1f9e8be48e57f9dd2985` ; `monde_v1.py` : `af907b1d5d779dfc1c4353503d31059f20d031a4b4324fea3ca775ad6a6bc98c` ; `trancher_v1.py` (début et décision) : `781335dda51954f5d4ac1ab25ce0ce850a421d8c0c2346ae8284fddc8a6609e0` ; `methodes_v1.py` parcouru (signatures seulement ; empreinte reprise de la table de B § 10, non recalculée : `2f7a8b11…`) ; C `question-course-2-defense-fusion-v1.md` (préambule) : `f89e0791571aced904e6f97e24df19cba54246e1bf77a06713dc9cfa0acfed2e` ; D `conception-pole-scientifique-v1.md` (§ 1, point 5 du cycle) : `a4f94148c9c55b76f208edecd7220b51a8e21ca69f52e50c7f2abb6484b81b52`.
- Régime exploratoire. Tout chiffre renvoie à une pièce ; le reste est marqué SUPPOSÉ.

## Verdict en trois lignes

1. Il faut changer d'**ensemble de base** : un processus déterminantal sur les **paires** (et non sur les fiches), dont la qualité diagonale porte la bisociation de la paire.
2. Bisociation d'une paire = aire² du parallélogramme des domaines, (1 − ⟨d_i, d_j⟩²)^α, multipliée par la proximité conceptuelle ⟨c_i, c_j⟩^β ; la répulsion entre paires vient d'un noyau de Schur, domaine-paire ⊙ concept partagé.
3. Pourquoi : un processus déterminantal ne sait que **repousser**. Il ne peut pas attirer deux fiches proches en concept. L'attraction doit donc vivre dans la qualité d'un objet qui est déjà la paire.

## Point de lecture préalable (à confirmer par Lazar)

Le mot de 13:12 dit : « maximiser le volume […] en même temps qu'on **minimise** leur proximité conceptuelle ». La question, elle, demande des parents **proches** en concepts. J'ai suivi la question (loin en domaine, proche en concept). Si Lazar voulait dire « minimiser la **distance** conceptuelle », c'est la même forme. Sinon, il suffit de changer le signe de β, et tout le reste tient.

## 1. L'objectif

**Le diagnostic, tiré de la pièce B.**
- Le déterminant d'un noyau sur les **fiches** diversifie les articles, pas les paires. Un ensemble divers d'articles contient toutes les paires de domaines (B § 3).
- Pour une paire, la pénalité du noyau corrigé vaut q_i² q_j² ((1 + γ)² − cos⁴). À cos 0,28, elle n'est que de 0,6 % (B § 3).
- Toute forme au niveau des fiches est donc hors sujet. C'est le cas de S_domaine ⊙ S_concept ou de S_domaine ⊕ S_concept : elles repoussent les fiches semblables en concept, soit le **contraire** du but.
- Raison générale : un processus déterminantal impose des corrélations négatives, P(i et j) ≤ P(i) P(j) (Kulesza et Taskar 2012, à vérifier). Aucun choix de noyau sur les fiches ne favorise une paire proche en concept.

**Options.**
- (O1) **Contrainte** : filtrer cos_ij < τ et partage de concept, puis tirer par strates. Avantage : simple ; c'est le diagnostic b_eloigne augmenté (+11,9 / +6,6, B § 1). Inconvénient : le concept reste un filtre, donc il n'est pas dans l'objectif. τ est un seuil dur.
- (O2) **Marche de Swanson guidée par les concepts**. On part d'une ancre, on choisit un concept ∝ idf, on arrive sur une fiche d'un domaine éloigné. Avantage : la meilleure forme mesurée (+3,5 / +3,8, B § 1) ; elle évite les moyeux. Inconvénient : aucune répulsion entre les paires tirées, et l'éloignement n'y est qu'implicite (paires éloignées 0,446, B § 1).
- (O3, **recommandée**) **Processus déterminantal sur les paires**. Ensemble de base 𝒫 = paires valides (étage commun de B § 2) ; pour P = (i, j) : qualité : b_P = q_i q_j · (1 − ⟨d_i,d_j⟩²)^α · (κ_ij + ε)^β, avec κ_ij = ⟨c̃_i, c̃_j⟩ ∈ [0, 1] et c̃ le vecteur de concepts pondéré par l'idf, normé ; répulsion domaine : S^D_{PP'} = (cos_ik cos_jl + cos_il cos_jk) / √((1 + cos_ij²)(1 + cos_kl²)), avec P' = (k, l) ; répulsion concept : S^C_{PP'} = ⟨ψ_P, ψ_P'⟩, avec ψ_P = (c̃_i ⊙ c̃_j)/‖·‖, et ψ_P = e_P (vecteur propre à la paire) si la paire ne partage aucun concept ; noyau : L = diag(√b) (S^D ⊙ S^C) diag(√b) + γI.

**Semi-défini positif.** S^D est la matrice de Gram des tenseurs symétrisés normés φ_P = (d_i⊗d_j + d_j⊗d_i)/‖·‖, car ⟨φ_P, φ_P'⟩ vaut l'expression ci-dessus (‖d_i⊗d_j + d_j⊗d_i‖² = 2 + 2 cos_ij²). Elle est donc semi-définie positive. S^C est une matrice de Gram, donc semi-définie positive. Leur produit de Schur l'est aussi (théorème de Schur). D S D l'est encore, avec D diagonale positive. Avec + γI (γ > 0), L est définie positive : la décomposition de Cholesky passe, et le déterminant est bien défini et strictement positif.

**Ce que le déterminant mesure.** Pour un ensemble Y de paires, log det L_Y ≈ Σ_{P∈Y} log b_P + log det (S^D ⊙ S^C)_Y (égalité exacte quand γ → 0). Cette quantité se lit en deux parts :
- la **bisociation cumulée** des paires, où chaque terme est α · log aire²(d_i, d_j) + β · log κ_ij + log q_i q_j ;
- le **volume²** du parallélépipède des paires dans l'espace (domaine-paire ⊗ concept partagé) : il pénalise deux paires de la même strate de domaines **et** du même concept-pont. C'est le stratifié (b) rendu doux, et l'évitement des moyeux de (d1).

**« Minimiser le produit scalaire » est-il contenu dans « maximiser le volume » ?**
- Pour une paire de vecteurs unitaires, oui, exactement : aire² = 1 − ⟨d_i,d_j⟩². Aucun terme à part n'est nécessaire.
- Pour le volume d'un ensemble de k fiches, non (B § 3).
- Le terme est toutefois **plat** : aux cosinus de B (0,54 / 0,28 / 0,03, B § 5), 1 − cos² vaut 0,708 / 0,922 / 0,999. Il faut donc un exposant : avec α = 4, on obtient 0,252 / 0,721 / 0,996 (calcul de ma main).

**Ce qui le distingue d'un tirage déterminantal classique.** L'ensemble de base est fait de paires, pas de fiches. Le concept entre en **attraction**, par la qualité, et en **répulsion**, entre les paires. Le domaine entre en attraction de l'éloignement à l'intérieur de la paire, et en répulsion des strates entre les paires.

**Coût.** Il y a m ≤ n(n − 1)/2 paires (n = 40 donne au plus 780 ; valides : SUPPOSÉ, quelques centaines). Noyau : O(m² · s), avec s le nombre de concepts non nuls. Glouton : O(m k²) par Cholesky incrémentale (Chen, Zhang et Zhou 2018, à vérifier), contre O(m k⁴) pour le `tirage_glouton` actuel, qui reste correct ici (k = 12). On garde les paires des générations passées dans l'ensemble conditionnant, pour que la répulsion traverse les générations.

**Pseudo-code**, compatible avec la pièce A (`vecteurs_domaine`, `produit`, `cholesky` et `tirage_glouton` repris tels quels) :
```
def vecteurs_concepts(listes, df, n):                 # idf : log(n / df[c]) ; norme 1 ; c ∈ liste fermée (§ 2)
    return normer([{c: log(n / df[c]) for c in set(l)} for l in listes])
def bisociation(di, dj, ci, cj, qi, qj, a, b, eps):
    aire2 = 1 - produit(di, dj) ** 2                   # aire² du parallélogramme des domaines
    return qi * qj * aire2 ** a * (produit(ci, cj) + eps) ** b
def noyau_paires(paires, D, C, q, a=4, b=2, eps=1e-3, gamma=1e-3):
    cos = [[produit(u, v) for v in D] for u in D]
    psi = [normer(hadamard(C[i], C[j])) or base(p) for p, (i, j) in enumerate(paires)]
    r = [sqrt(bisociation(D[i], D[j], C[i], C[j], q[i], q[j], a, b, eps)) for i, j in paires]
    L = matrice(len(paires))
    for p, (i, j) in enumerate(paires):
        for s, (k, l) in enumerate(paires):
            sd = (cos[i][k] * cos[j][l] + cos[i][l] * cos[j][k]) / sqrt((1 + cos[i][j]**2) * (1 + cos[k][l]**2))
            L[p][s] = r[p] * sd * produit(psi[p], psi[s]) * r[s] + (gamma if p == s else 0.0)
    cholesky(L)                                        # garde R5 : lève NonDefiniePositive, aucun repli
    return L
def ponts(a, b):                                       # pont = concept partagé (repli : opérateur partagé)
    return sorted(set(a.concepts) & set(b.concepts)) or sorted(set(a.operateurs) & set(b.operateurs))
def tirer_bisociatif(candidates, deja, k, **h):
    paires = [(i, j) for i, j in combinaisons(candidates) if valide(i, j, deja)]   # étage commun de B § 2
    L = noyau_paires(paires, vecteurs_domaine(...), vecteurs_concepts(...), aptitudes, **h)
    return [paires[p] for p in tirage_glouton(L, k)]   # conditionné par les paires déjà fusionnées (gardées en tête)
```
Recommandation : (O3), avec (O1) et (O2) comme témoins. Confiance que (O3) est **la bonne forme** : 0,65. Confiance qu'elle bat (d1) sur les mondes étendus : 0,45 (SUPPOSÉ).

## 2. La représentation des concepts

**Options.**
- (R1) **Champ déclaré par le proposeur**, sur une liste fermée. Avantage : gratuit ; le proposeur connaît son mécanisme. Inconvénient : manipulable, puisque déclarer le concept à la mode rapproche de tout.
- (R2) **Modèle tiers hors boucle** : il étiquette sur la liste fermée, puis l'étiquetage est scellé **avant** le tirage. Avantage : il voit le fond. Inconvénient : coût, et biais du modèle. Ce n'est pas un « juge dans la boucle » s'il est scellé avant le tirage (critère gelé de la question).
- (R3) **Extraction par programme** : motifs, symboles, citations canoniques (Ville, Wald, Fano…). Avantage : reproductible, non manipulable par la paraphrase. Inconvénient : rappel faible (couverture SUPPOSÉE entre 0,45 et 0,70, comme les niveaux de B § 5).

**Recommandation : règle des deux sources sur trois.** Un concept entre dans c_i s'il est donné par deux sources au moins parmi R1, R2 et R3.
- La déclaration seule ne suffit jamais.
- Trois concepts au plus par fiche ; c̃ est normé, donc ajouter des étiquettes **dilue** chacune ; la pondération idf ôte la valeur des concepts moyeux.
- Les poids α et β ne sont pas révélés aux proposeurs.
- Un concept déclaré doit être **utilisé** dans le protocole : le programme vérifie que le motif apparaît dans la méthode ou le code, pas seulement dans le titre.
- Surveillance : le taux de désaccord entre R1 et les sources R2 et R3 est suivi par proposeur. Au-delà de 0,3 (SUPPOSÉ), le champ R1 de ce proposeur est ignoré.
- Confiance : 0,6.

**Champ de gabarit** à ajouter à la pièce C après « méthode » : **concepts mobilisés**. Trois identifiants au plus, pris dans la liste ci-dessous, chacun avec la phrase de la méthode qui l'emploie. Liste fermée initiale de 36 entrées, avec l'identifiant et un motif de programme indicatif :
1. `rvs` test séquentiel du rapport de vraisemblance (Wald) ; 2. `evaleur` e-valeur, e-processus ;
3. `richesse` martingale de test, processus de richesse, pari ; 4. `ville` inégalité maximale de Ville ou de Doob ;
5. `concentration` Hoeffding, Bernstein, Freedman ; 6. `rupture` détection de rupture (CUSUM, Page, Lorden, Shiryaev) ;
7. `composite` test composite, rapport de vraisemblance universel ; 8. `fdr` taux de fausses découvertes (Benjamini-Hochberg, e-BH) ;
9. `conforme` prédiction conforme, échangeabilité ; 10. `kl` divergence de Kullback-Leibler ; 11. `fdiv` f-divergences, divergence de Rényi ;
12. `vt` variation totale, méthode de Le Cam ; 13. `pinsker` Pinsker, Bretagnolle-Huber ; 14. `fano` borne de Fano, information mutuelle ;
15. `traitement` inégalité de traitement des données ; 16. `np` lemme de Neyman-Pearson, test le plus puissant ;
17. `invariance` test invariant sous un groupe, invariant maximal ; 18. `suffisance` statistique suffisante ;
19. `minimax` bornes minimax inférieures, Assouad ; 20. `noyau2e` test à deux échantillons à noyau (écart moyen maximal) ;
21. `transport` transport optimal, Wasserstein ; 22. `projection` projection aléatoire, Johnson-Lindenstrauss ;
23. `pacbayes` bornes PAC-bayésiennes (« probablement approximativement correct ») ;
24. `rademacher` complexité de Rademacher, dimension de Vapnik-Tchervonenkis ; 25. `robuste` robustesse distributionnelle, boule d'ambiguïté ;
26. `jeu` jeu à somme nulle, minimax de von Neumann ; 27. `bandit` bandits, regret ; 28. `dpp` processus ponctuel déterminantal ;
29. `sousmod` sous-modularité, glouton ; 30. `causal` intervention, médiation, contrefactuel ;
31. `sousespace` sous-espace, composantes principales ; 32. `clairseme` détection de signal clairsemé, « critère supérieur » de Donoho-Jin ;
33. `confidentialite` confidentialité différentielle ; 34. `canal` capacité de canal, stéganographie (Shannon, Cachin) ;
35. `importance` changement de mesure, échantillonnage préférentiel ; 36. `extremes` valeurs extrêmes, maxima.

La liste est figée par version (R12). Toute addition crée une nouvelle version, jamais en cours de génération.

**Test de séparabilité domaine / concept**, préenregistré, sur un échantillon annoté à la main (SUPPOSÉ : 60 fiches, deux annotateurs). Quatre mesures :
- (i) **fuite** : précision d'un classifieur domaine ← concepts, en validation croisée, à comparer à la même mesure sous permutation. On exige moins de 10 points au-dessus du hasard (SUPPOSÉ) ;
- (ii) **transposition** : on réécrit une fiche dans le vocabulaire d'un autre domaine, avec le même mécanisme. La concordance des concepts doit être ≥ 0,8 et les domaines doivent changer ;
- (iii) **fausse proximité** : deux fiches du même domaine à mécanismes différents. κ doit rester bas, sous 0,3 en moyenne (SUPPOSÉ) ;
- (iv) **accord** entre R2 et R3, mesuré par un kappa de Cohen ≥ 0,6 (SUPPOSÉ).

Si (i) ou (ii) échoue, la représentation code le domaine : arrêt, et l'on ne passe pas au point 3 sur les vraies fiches.

## 3. Le test : squelette du préenregistrement v2 (mondes à deux espaces)

**Hypothèse.** La proximité conceptuelle **dans l'objectif** (O3) augmente la part de vrais ponts tirés par rapport aux trois témoins :
- le tirage stratifié (b) ;
- la forme v6.3 (a) ;
- la marche de Swanson (d1), sur les étiquettes d'opérateur et sur les étiquettes de concept (d1c).
À information égale, elle l'augmente aussi par rapport au concept utilisé comme **filtre** seulement.
Signe prédit : positif contre (b), (a) et (N_filtre) ; nul ou positif contre (d1c).

**Générateur `monde_v2.py`** (nouveau nom, R12), qui étend `monde_v1.py`. Ajouts :
- C = 10 concepts latents ; chaque opérateur latent de groupe reçoit un concept ; un concept moyeu présent dans 30 % des articles (SUPPOSÉ) ;
- **vrais ponts conceptuels** : 3 paires d'articles de champs différents, à opérateurs de **noms différents**, sous un même concept non moyeu, avec des contraintes rendues compatibles ;
- **ponts de surface** : 3 paires éloignées qui partagent un mot d'opérateur (homonyme) sous des concepts différents ;
- **faux ponts** : 3 paires qui partagent un concept, mais dont les contraintes vraies sont incompatibles ;
- **ponts proches** : 3 paires d'un même champ qui partagent un concept, comptées fausses dans le monde ordinaire et vraies dans le monde inversé ;
- **canal des concepts** : couverture, parasites et **fuite de domaine ρ**, c'est-à-dire la probabilité qu'une étiquette soit remplacée par le concept dominant du domaine. Niveaux bien (0,85 ; 0,05 ; 0,05), moyen (0,65 ; 0,15 ; 0,15), mal (0,45 ; 0,30 ; 0,30), tous SUPPOSÉS ;
- les greffes et jumeaux de v1 sont gardés.

Vérité : domaines éloignés, concept latent commun non moyeu, contraintes vraies compatibles.

**Validation avant toute méthode**, sur des graines distinctes : la séparabilité (i) mesurée dans le monde (fuite ≤ 10 points en « bien ») et les cosinus comme en B.

**Étage commun.** Domaines observés différents, filtre de contraintes. Partage d'**une étiquette d'opérateur ou de concept**. Tous les bras voient les **mêmes** observations, ce qui évite de favoriser (O3) par construction (R4).

**Bras.**
- Témoins : (b), (a) v6.3, (d1), (d1c), (c) uniforme.
- Candidate : (N) = (O3).
- Ablations, non éligibles : N_β0 (sans concept) ; N_α0 (sans éloignement) ; N_filtre (stratifié parmi les paires éloignées qui partagent un concept) ; N_fiches (noyau sur fiches S^D ⊙ S^C, l'option « ⊙ » de la question) ; N_q1 (q ≡ 1).
- Diagnostics : b_eloigne, oracle.

**Hyperparamètres.** α ∈ {1, 2, 4, 8}, β ∈ {0,5 ; 1 ; 2 ; 4}, ε = γ = 10⁻³. Réglés sur 200 mondes de validation en M_moyen seul, scellés avant les mondes de décision.

**Budget.** Comme B § 2 : 4 paires × 3 générations, 40 candidats.

**Métriques.**
- Primaire : **précision**, la part de vrais ponts parmi les 12 paires tirées. C'est le substitut synthétique de la « part de filles réussies » : il n'y a pas de fusion ici (B § 6).
- Secondaires : part de paires **éloignées et conceptuellement proches** tirées, sur le latent (et sur l'observé, rapportée) ; rappel par mécanisme ; pièges : surface, moyeu conceptuel, faux ponts ; strates distinctes par paire.
- Intervalles : 2 000 rééchantillonnages appariés des mondes, comme en B.

**Conditions** (600 mondes chacune) : M_bien, M_moyen, M_mal ; SP (sans pont, placebo de B § 2.1) ; INV (vérité inversée) ; V_fuite (ρ = 0,6) ; V_concepts_absents ; V_moyeu_conceptuel (0,6) ; V_surface (9 ponts de surface) ; NR : les mondes v1 inchangés, pour vérifier la non-régression.

**Règle d'adoption (gelée).** Δ_X = précision(N) − précision(b) dans la condition X. (N) est adoptée si toutes les conditions suivantes sont réunies :
- (1) Δ ≥ +5 points **et** rapport ≥ 1,25 en M_bien et en M_moyen, borne basse > 0 ;
- (2) N − d1c a une borne basse > 0 en M_bien et en M_moyen ;
- (3) SP : aucun écart dont l'intervalle exclut 0 ;
- (4) INV : Δ_INV − Δ_M_bien < 0, borne haute < 0. C'est le contrôle corrigé de B § 7.2 ;
- (5) NR : Δ ≥ −1 point (borne basse) sur les mondes v1 ;
- (6) V_fuite : l'avantage baisse (Δ_V_fuite < Δ_M_bien). Sinon, il ne vient pas des concepts.

Le seuil absolu de +12 de B est remplacé par un seuil à la fois absolu et relatif (critique de B § 7.3). Ce changement est **à décider par Lazar avant scellement** : je le propose, je ne le gèle pas.

**Lecture « ingrédient manquant ».** **Oui** si N − N_β0 ≥ +3 points et N − N_filtre ≥ +3 points, bornes basses > 0, en M_bien et en M_moyen. **Non** si la borne haute de N − N_filtre est < +2 points dans les deux : le concept suffit alors comme filtre. **Indécis** sinon.

**Puissance.** D'après B § 1, une demi-largeur d'intervalle d'environ 1,5 point à 400 mondes donne un écart-type apparié par monde d'environ 15,3 points (mon calcul). Pour détecter 3 points à α = 0,05 bilatéral avec une puissance de 0,8, il faut environ 204 mondes. Avec une correction de Bonferroni sur 4 contrastes (α = 0,0125), il en faut environ 290. 600 mondes par condition donnent de la marge. Coût : processeur seul, quelques heures en Python pur (SUPPOSÉ ; B : 93 s pour v1, mais le noyau sur les paires est environ 400 fois plus lourd).

**Liste d'arrêt.** Validation du générateur ratée : fuite > 10 points en « bien », ou cosinus hors bornes. Échec de Cholesky sur un noyau (R5, aucun repli silencieux). Plafond de l'oracle < 0,30. Placebo défaillant sur plus de 5 % des écarts. Toute lecture avant scellement. Contre-lecture R2 absente, ce qui était la réserve de B § 9. Garde testée sur un cas sain et sur un artefact (R5) : par exemple un noyau volontairement non semi-défini (la forme (e) de A, `noyau_fautif`) doit lever l'erreur.

**Passage sur les vraies fiches de la course 2** (exploratoire, jamais décisif seul).
- On fige le vivier des survivantes et les concepts (règle des deux sources sur trois), scellés **avant** tout verdict des filles.
- Chaque bras ((b), (d1c), (N)) tire ses k paires sur le même vivier.
- On fusionne **toutes** les paires tirées, union mélangée, sans que le juge ni la fusion connaissent le bras.
- Dénominateur : les paires tirées. Une fusion refusée compte comme un échec, et l'on ne retire aucune fille après coup (lecture sans sélection sur le verdict, N-053 ; contenu de N-053 non lu par moi : SUPPOSÉ).
- Mesures : part de filles notables (K1 à K5 de C), puis part qui survivent à leur test gelé (D, point 4).
- Avec environ 20 paires par bras, l'erreur type est d'environ 0,11 (SUPPOSÉ) : seul un effet massif se lirait.

## 4. Antériorité (de mémoire, toutes à vérifier sur PDF, R7)

- **Processus déterminantaux** : Kulesza et Taskar, « Determinantal Point Processes for Machine Learning », 2012 : décomposition qualité × diversité, processus structurés ; Kulesza et Taskar, « k-DPPs: Fixed-size Determinantal Point Processes », 2011 ; Gillenwater, Kulesza et Taskar, « Discovering Diverse and Salient Threads in Document Collections », 2012 : ensemble de base fait de **chaînes** de documents. C'est le plus proche de (O3) ; Chen, Zhang et Zhou, « Fast Greedy MAP Inference for Determinantal Point Process to Improve Recommendation Diversity », 2018.
- **Bisociation** : Koestler, « The Act of Creation », 1964 ; Berthold (éditeur), « Bisociative Knowledge Discovery », 2012 (projet BISON) ; Dubitzky, Kötter, Schmidt et Berthold, « Towards Creative Information Exploration Based on Koestler's Concept of Bisociation », 2012.

  BISON définit déjà la bisociation par des concepts-ponts et une **similarité structurelle** entre domaines : c'est l'occupant probable de l'idée « deux espaces ».
- **Analogie** : Gentner, « Structure-Mapping: A Theoretical Framework for Analogy », 1983 : relations communes et attributs de surface différents, soit la même idée en sciences cognitives ; Hope, Chan, Kittur et Shahaf, « Accelerating Innovation Through Analogy Mining », 2017 : vecteurs « but » et « mécanisme », proches en mécanisme et loin en domaine. C'est une **collision probable** sur le principe.
- **Découverte littéraire** : Swanson, « Fish Oil, Raynaud's Syndrome, and Undiscovered Public Knowledge », 1986 ; Swanson et Smalheiser, « An Interactive System for Finding Complementary Literatures », 1997 ; Henry et McInnes, « Literature Based Discovery: Models, Methods, and Trends », 2017 ; Sourati et Evans, « Accelerating Science with Human-Aware Artificial Intelligence », 2023 ; Krenn et collaborateurs, « Forecasting the Future of Artificial Intelligence with Machine Learning-Based Link Prediction », 2023 : rétrodiction, cf. B § 8.
- **Recombinaison** : Uzzi, Mukherjee, Stringer et Jones, « Atypical Combinations and Scientific Impact », 2013 ; Mouret et Clune, « Illuminating Search Spaces by Mapping Elites », 2015 ; Pugh, Soros et Stanley, « Quality Diversity: A New Frontier for Evolutionary Computation », 2016 ; Moraglio, Krawiec et Johnson, « Geometric Semantic Genetic Programming », 2012 ; Meyerson et collaborateurs, « Language Model Crossover: Variation through Few-Shot Prompting », 2023 ; Lehman et collaborateurs, « Evolution through Large Models », 2022 ; Wang et collaborateurs, « SciMON: Scientific Inspiration Machines Optimized for Novelty », 2024 ; Radensky et collaborateurs, « Scideator », 2024 : recombinaison de facettes « but / mécanisme / évaluation ».
- **Zone vierge = question (R8).** Je ne connais pas de processus déterminantal **sur des paires** dont la qualité porte l'aire des domaines × la proximité conceptuelle, appliqué à la recombinaison de fiches d'hypothèses.

  Le **principe** est en revanche occupé (Gentner ; Hope et collaborateurs ; BISON). Revendiquer seulement la **forme** et son test à vérité plantée, jamais « la bisociation à deux espaces ».

  Requêtes à faire : « determinantal point process pairs ground set analogy », « bisociation determinantal », « analogy mining mechanism purpose diversity sampling ».

## Réserves

- Le monde v2 encode mon hypothèse : les concepts existent comme variables latentes séparées du domaine. V_fuite et NR sont là pour en mesurer le prix.
- Pour les poids α et β : l'adoption ne repose pas sur une recherche en grille faite sur les mondes de décision.
- (d1c) est un témoin fort et peut suffire. Une issue « Swanson guidé par concepts suffit » est permise par la règle (2).
