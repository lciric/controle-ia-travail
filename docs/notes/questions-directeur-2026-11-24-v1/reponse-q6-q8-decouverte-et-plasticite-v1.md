# Réponse aux questions 6 et 8 du directeur : peut-on démontrer comment maximiser la probabilité d'une découverte ; la plasticité d'un graphe de domaine comme indice d'une zone de découverte (v1)

- **Nature** : pièce de travail (classe C). Aucune dépense, aucun appel à un modèle externe, calculs sur processeur seulement. Non committée.
- **Heure** : `2026-11-28T05:38:08Z` (`date -u`, fin de rédaction). Travail commencé le 24 novembre, coupé par le quota, repris le 28 novembre.
- **Auteur** : Claude Fable 5.2, effort maximal, sous-agent ; branche `idees/questions-directeur-2026-11-24-v1`.
- **Demandes servies telles quelles** : question 6 (`demandes-reformulees-quatre-points-v1.md`, `52d1cc47…`, ligne 174 et suivantes) ; question 8 (`demandes-reformulees-quatre-points-q8-q11-v1.md`, `632c7af2…`, lignes 14 à 52).
- **Fichiers lus** (empreintes abrégées) : `CLAUDE.md` (`c6a1ca39…`) ; mandat (`ab6f19bb…`) ; les trois compléments (`58d2e517…`, `b2dc5ebe…`, `43716a8a…`). Pièces qui priment : erratum transversal des notations (`72afe693…`) ; contre-lectures (`9cefaa1f…`, `31eb1c07…`) ; errata des questions 1 (`b89f7430…`), 3 (`6018b273…`, `10e81026…`), 4 (`b359bf15…`, `72baac36…`), 5 (`7bcaec6f…`, `16bcc89c…`), 7 (`b142acfd…`), 9 (`c4a93d16…`, `271df959…`) et errata mineurs (`fcac74f5…`, `9d72f859…`) ; note du modèle unifié (`f2f0a700…`) et son erratum 1 (`619b6feb…`). Réponses aux questions 1 (`2cc29632…`), 2 (`7f4cf73f…`), 3 (`af126ebf…`), 4 (`249c611c…`), 5 (`0bdc9810…`), 7 (`937e3e69…`) et 9 (`e981c88c…`). Sous `docs/notes/idee-interessante-v1/` : réponse de Fable (`8ec4f9e0…`), trois réponses de Carbon (`a9532fbb…`, `01f859c0…`, `3f92cede…`), intuitions du directeur (`6f6397ee…`), messages du directeur et rapport de priorités du 23 novembre (`0a18a98e…`, `88d80f76…`). Réponse de Carbon sur la boucle entre l'organisme et le contrôle, et son script (`f744320d…`, `7a9e68e0…`) ; Plan Turing (`69c8deae…`) ; décisions N-058 (`854f2724…`) et N-053 (`2204256d…`) ; préenregistrement et verdict exécutif du rapport sur la rétrodiction des foyers de tension (`dcc8de2e…`, `0a617ab1…`) ; synthèse sur les puits étroits et son erratum (`6112172f…`, `ec724355…`). Rien d'ouvert sous `coffre/`, `docs/verdicts/`, `runs/`, `diag/`, `donnees/`.
- **Scripts joints**, même dossier, graines par `numpy.random.SeedSequence` : `enumeration-allocation-decouverte-v1.py` (`5c57a810…`) et sa sortie `enumeration-allocation-decouverte-v1-sortie.txt` (`2ddf8af0…`) ; `simulation-plasticite-bifurcation-v1.py` (`cb69ac93…`) et sa sortie `simulation-plasticite-bifurcation-v1-sortie.txt` (`ce1f8618…`). Les deux scripts partiels du 24 novembre restent intacts sous `partiel-fable-q6-q8-coupe-quota-v1/`. Les chiffres du texte sans référence viennent de ces deux sorties ou s'en déduisent par un calcul d'une ligne ; ceux du résultat négatif (R-5241) et de la rubrique 13F60 viennent des pièces du dépôt citées.
- **Longueurs** (`wc -w` en locale UTF-8, du titre de chaque partie à sa dernière ligne ; la locale C en compte moins, 3 875 et 2 908) : partie I, 3 992 mots pour 4 000 ; partie II, 2 996 mots pour 3 000. Les tableaux sont écrits barres collées aux cellules et les formules sans espace autour de `+` et `−` ; le rendu n'en est pas changé.
- **Notations** : celles de l'erratum transversal et de la note du modèle unifié (κ, part des conflits seulement ; `ϑ`, coefficient de la surprise dans la crédibilité ; `r`, type d'une relation). Propres à cette pièce : `θ_j` et `ε_j`, a priori et chance de détection d'un lieu (à ne pas confondre avec `ϑ`) ; `π₀`, `q_o`, `α_o`, `q_d`, `u`, caractéristiques du filtre ; `H`, taux de réussite latent d'un proposeur ; `M_φ`, nombre de paires alignées d'un cortège (noté m dans la sortie du script) ; `p`, probabilité de succès d'une épreuve (notée q pour les boîtes dans la sortie) ; `b`, facteur d'actualisation. Dans la partie II, `m`, `J`, `h`, `h₀`, `T`, `A` appartiennent au modèle jouet de la section 4.
- **Statuts** : « démontré » n'est écrit que pour un énoncé à hypothèses écrites et preuve donnée ou citée ; « mesuré » désigne ici un calcul sur modèle jouet, jamais une mesure sur un domaine réel.
- **Références** : numérotées, en fin de pièce, avec lien et état de lecture ; sources lues sur fichier et empreintes en annexe B.

---

# Partie I — Peut-on démontrer comment maximiser la probabilité d'une découverte ? (question 6)

**Verdict.** On ne démontre pas « la » manière de maximiser la probabilité d'une découverte : on démontre, sous une loi a priori et des hypothèses écrites, six règles d'allocation, toutes anciennes, vérifiées ici par énumération. Les trois objectifs possibles (au moins une découverte, leur nombre, la meilleure) commandent trois indices différents, et un filtre bon marché, utile aux idées ordinaires, peut détruire les idées profondes. Les conditions d'émergence se ramènent à un seul critère de branchement, dont l'hypothèse porteuse reste à mesurer.

## 1. Le problème, posé

**Décideur** : l'orchestrateur de l'organisme, non les proposeurs ni un lecteur. **Actions**, à chaque pas : choisir un lieu `j` (question ouverte, anomalie, paire de voisinages) ; y faire engendrer un candidat (coût `c_g`) ; le filtrer ou non à bas prix (`c_f`) ; l'éprouver sur l'oracle à vérité (`c_v`, avec délai) ; s'arrêter. **Budget** `B`, dur. **Information** : avant l'épreuve, des traits calculés par programme sur la fiche et le graphe gelé (surprise `S`, score serrure-clé réduit `Z_r`, ancrage à une anomalie, lieu, proposeur) ; après, le verdict de l'oracle et, si elle se mesure, une portée. Aucun trait n'est l'avis d'un lecteur quand il s'agit de choisir une composition (décision sur la composition des proposeurs, N-058) : l'ordre d'épreuve des fiches qui comptent pour ce choix est fixé sans lecteur (erratum 1 de la question 1).

**Découverte** : énoncé validé par un oracle à vérité (fait planté retrouvé, preuve vérifiée, prédiction datée confirmée), que la batterie connue n'implique pas. **Découverte profonde** : validée, de portée à distance `W` (surprise retirée hors du voisinage, question 2) au-dessus d'un seuil, de profondeur locale tenue (dont la robustesse aux perturbations des faits ; note du modèle unifié, section 6) et rare au hasard (`Rar_τ` petite). Tout cela se lit après coup ; avant, on n'a que des traits.

**Trois objectifs, trois indices** (`p_i` probabilité de succès du candidat `i`, `c_i` son coût, `V_i` sa valeur).

- *Nombre espéré*, `Σ p_i` : indice `p_i/c_i`.
- *Au moins une*, `1−Π(1−p_i)` : indice `−ln(1−p_i)/c_i`, qui préfère un candidat sûr à deux moyens.
- *La meilleure* : valeur de réserve de Weitzman, `z_i` solution de `c_i = E[(X_i−z_i)⁺]`, soit `z = V−c/p` pour une boîte à deux issues [1, p. 7] ; on ouvre par `z` décroissant et l'on s'arrête quand le meilleur acquis dépasse les `z` restants.

Ces indices divergent. Candidats (probabilité 0,9 ; coût 2), (0,5 ; 1), (0,5 ; 1), budget 2 : « au moins une » prend le premier (0,90 contre 0,75), « nombre espéré » les deux autres (1,00 contre 0,90) ; sur 400 instances, 43 divergences, perte jusqu'à 0,135. Boîtes (0,9 ; valeur 2) et (0,1 ; valeur 10), de coût 0,5 : `p·V/c` vaut 3,6 et 2,0, les valeurs de réserve 1,44 et 5,00 ; ouvrir d'abord la boîte risquée rapporte 1,67 contre 1,62. Le délai retourne l'ordre : avec un facteur d'actualisation `b` par épreuve, `z = (b·p·V−c)/(1−b+b·p)` [1, p. 9, équation 7] donne 0,92 contre 0,77 à `b = 0,75`. L'arrêt diffère aussi : premier succès, épuisement du budget, ou valeur de réserve.

## 2. Le modèle unifié

**Une notation**, celle de la note du modèle unifié : taux de naissance `λ_ab(t) = p⁰_t(a,b)·exp(β·Z_ab+γ·F_t+δ·P_t)` ; surprise `S = −log p⁰` ; crédibilité `q = σ(q₀+β′·Z−ϑ·S)` ; intérêt `I = q·(S+W)`. Pour la décision, `λ` est un a priori sur les lieux, `q` une probabilité de succès par épreuve, `W` une valeur : c'est la structure de la théorie de la recherche (énoncé 2).

**Où Fable et Carbon divergent.**

|Point|Fable|Carbon|Ce que le choix change|
|---|---|---|---|
|Structure dans le taux|`exp(β·Z_r)`, réduit contre recâblage|logistique de `K_C` brut|sans nul, `K_C` lit taille et degrés ; la logistique sature|
|Surface|`p⁰` multiplie ; l'optimum de distance vient de l'intérêt|optimum fixe `μ` dans le taux|mobile contre fixe ; `μ` s'identifie mal, distance de surface et contact `C_soc` étant tirés de la même matrice d'auteurs par concept|
|Contact et cadres|dans l'exposant|préfacteur `η₀·C_soc+η₁·F`|chez Carbon, taux nul sans contact ni cadre|
|Intérêt|`q·(S+W)`|`d_surf·K_C`, borné|ni optimum intérieur ni portée chez Carbon|
|Conflits|`c−κ`|`c_C·exp(−γ_C·χ_C)`|classements différents (note, section 3)|
|Découvertes simultanées|`1−e^{−λτ}`|`1−(1+Λ)·e^{−Λ}`|deux événements (« une autre équipe, sachant la mienne » ; « deux équipes au moins ») : pas une contradiction|
|Émergence|rapport de branchement ; `c_A·c_B = 1`|rayon spectral d'une matrice sans retour pondérée|un seul critère (énoncé 6), exact sans boucles courtes seulement|

**Dérivation refaite : la distance optimale.** Avec `W` indépendant de `S`, `∂I/∂S = −q·g`, où `g = ϑ·(1−q)·(S+W)−1` croît en `S`. Un optimum intérieur `S*` existe si et seulement si `ϑ·W·(1−σ(q₀+β′Z)) < 1` ; sinon l'optimum est au bord `S = 0` : quand la portée attendue est grande, l'évident suffit. À l'optimum, `S*+W = 1/[ϑ·(1−q*)]`, et le théorème des fonctions implicites donne

`dS*/dZ = β′·q*/ϑ−(1−q*)·∂W/∂Z` ; `dS*/dW = −(1−q*)` ; `d(S*+W)/dZ = β′·q*/ϑ+q*·∂W/∂Z`.

Trois conséquences. (i) Le corollaire de Fable (« la distance optimale recule quand la structure s'emboîte mieux ») tient si et seulement si `∂W/∂Z < β′·q*/[ϑ·(1−q*)]`, condition déjà relevée par l'erratum 2 de la question 5 ; avec une pente tirée entre 0 et 3, `S*` recule dans 288 cas et se rapproche dans 255. (ii) Ce qui tient dès que `∂W/∂Z ≥ 0`, c'est que l'information totale visée `S*+W` croît avec `Z` : voilà la forme à tester. (iii) La distance optimale diminue quand la portée attendue croît, ce qu'aucune des deux réponses ne dit. Vérification : 800 tirages de paramètres, 543 optimums intérieurs, 257 au bord, aucun désaccord, formes closes exactes à 10⁻⁹ près (partie A).

**Erreurs et glissements relevés.**

1. Le « théorème de rendement décroissant » de Carbon (réponse sur la boucle entre l'organisme et le contrôle, section 2.3) : l'algèbre est juste, mais elle dérive une courbe posée (une « taxe de dérive » exponentielle supposée). C'est une hypothèse munie d'un optimum, non un théorème sur l'organisme. Il note κ la part des classes couvertes : à renommer, κ étant réservé à la part des conflits.
2. Sa table du filtre se recalcule à l'arrondi près, mais « tant que `α_o > π₀`, le budget est brûlé » n'est pas le critère exact (énoncé 5), et le gain a un plafond, `1/π₀ = 25`, déjà approché à 21,55.
3. Le seuil spectral : l'article cité [24] traite la matrice sans retour non pondérée ; la version pondérée par les probabilités d'arêtes n'y figure pas (à vérifier ailleurs), et le critère n'est qu'une borne hors des graphes localement arborescents.
4. « Avalanche si `n ≥ 1` » (Fable) : à `n = 1` l'extinction est certaine ; il faut `n > 1`, et dans un cortège le vivier est fini (énoncé 6).

## 3. Ce qui se démontre

Six énoncés ; la lettre entre parenthèses renvoie à la partie du script qui vérifie.

**Énoncé 1 — Ordre d'épreuve.** *Hypothèses* : succès indépendants de probabilités `p_i` connues, coûts `c_i > 0`, arrêt au premier succès. *Énoncé* : l'ordre par `p_i/c_i` décroissant minimise le coût espéré jusqu'au premier succès. *Preuve* : placer `i` juste avant `j` plutôt que juste après change le coût de `Π(1−p_k)·(p_j·c_i−p_i·c_j)`, produit sur les prédécesseurs : négatif ou nul si et seulement si `p_i/c_i ≥ p_j/c_j`. Résultat ancien [3, 4] (notices). *Vérification* : 260 instances sur 260 (B1). *Contre-exemples* : sous budget dur, l'exemple de la section 1 (l'ordre `p/c` obtient 0,75 contre 0,90) ; sous corrélation, un échec abaisse les candidats voisins et l'indice se recalcule (énoncé 4). *Pour « la meilleure »* : la politique de réserve est optimale (théorème de Weitzman [1, p. 6-7], cas des indices de Gittins [2], notice) ; elle égale la programmation dynamique dans 300 instances sur 300, délai compris, quand l'indice `E[X]/c` perd dans 162, jusqu'à 15,5 % (B3, B4).

**Énoncé 2 — Effort par lieu.** *Hypothèses* : un objet caché dans une seule des cellules, d'a priori `θ_j` ; un effort `x_j` dans la bonne cellule détecte avec probabilité `1−e^{−ε_j·x_j}` (`ε_j`, chance de détection par unité d'effort, petite pour un puits rare) ; budget `Σ x_j = B`. *Énoncé* : l'allocation optimale est `x_j = (1/ε_j)·[ln(θ_j·ε_j/ν)]⁺`, `ν` fixé par le budget. *Preuve* : objectif concave séparable sous contrainte linéaire ; les conditions de Karush, Kuhn et Tucker sont nécessaires et suffisantes. C'est l'allocation de Koopman [5], version séquentielle [6] ; l'idée d'allouer la recherche par utilité marginale est chez Peirce [7] (notices ; page de [5] à vérifier). *Conséquences* : seules sont fouillées les cellules où `θ_j·ε_j > ν` ; la masse a posteriori après échec y est proportionnelle à `1/ε_j`. À petit budget tout va au lieu probable et facile ; l'effort ne gagne les puits rares qu'avec le budget : dans l'exemple (a priori 0,40 ; 0,30 ; 0,20 ; 0,10 ; chances de détection 0,20 ; 0,05 ; 0,02 ; 0,20), le puits le plus rare reçoit 0 tirage sur 30, 33 sur 100, 161 sur 300. *Vérification* : le glouton marginal égale l'optimum exhaustif, 150 instances sur 150 (C). *Contre-exemple* : si la détection exige un effort minimal (une chaîne de plusieurs étapes), les rendements ne décroissent plus : partager entre deux cellules un budget égal à ce minimum ne détecte rien, le concentrer détecte avec la probabilité a priori de la cellule.

**Énoncé 3 — Viser le maximum.** *Hypothèses* : `n` tirages indépendants d'une source ; on garde le meilleur. *(a)* Si la source B est un étalement de A à moyenne constante (A plus un bruit de moyenne conditionnelle nulle [10]), alors `E[max_n B] ≥ E[max_n A]` pour tout `n`. *Preuve* : le maximum est convexe ; inégalité de Jensen conditionnelle. *(b)* Dans une famille position-échelle `X = l+e·Y`, `E[max_n] = l+e·m_n`, où `m_n`, espérance du maximum de `n` copies de `Y`, croît avec `n` : la source de plus grande échelle l'emporte dès que `m_n > (l_B−l_A)/(e_A−e_B)`, et sa queue dépasse l'autre au-delà de `x* = (l_B·e_A−l_A·e_B)/(e_A−e_B)`. *Exemple* : lois normales A (moyenne 0, écart type 2) et B (1 ; 1) : `x* = 2`, A devant dès `n = 4` (D). *Lecture* : pour un seuil haut ou beaucoup de tirages, l'échelle d'une source compte plus que sa moyenne ; pour un seuil bas, la dispersion nuit. *Contre-exemple* : la variance ne fait pas la queue. A vaut +3 ou −3 (variance 9) ; B vaut 0 (probabilité 0,98), +5 ou −5 (0,01 chacun ; variance 0,5) : `P(A ≥ 4) = 0`, `P(B ≥ 4) = 0,01`. Hors de ces deux cadres rien n'est garanti : pour les bandits visant le maximum, aucune politique n'égale à coup sûr la meilleure source [13, théorème 11, p. 4]. Usage antérieur : [11, 12] (notices).

**Énoncé 4 — Diversité sous corrélation.** *Hypothèses* : sur un puits donné, un proposeur a un taux de réussite latent `H`, aléatoire et inconnu ; sachant `H`, ses tirages réussissent indépendamment. *(a)* `P(au moins un succès en n tirages) = 1−E[(1−H)^n] ≤ 1−(1−E[H])^n`, avec égalité si et seulement si `H` est constant (Jensen) ; quand `n` croît, la probabilité plafonne à `P(H > 0)`. *(b)* Entre `K` proposeurs de latents indépendants et de même loi, la répartition la plus égale des tirages minimise l'échec ; tout confier à un seul le maximise. *Preuve* : `ln E[(1−H)^m]` est convexe en `m` (inégalité de Lyapounov), donc la somme sur les proposeurs est convexe au sens de Schur. *(c)* Si le latent est commun (même modèle, mêmes données, même mémoire), la répartition ne change rien. *(d)* Sous dépendance quelconque, la probabilité d'au moins un succès dans l'ensemble choisi et l'espérance du maximum sont croissantes et sous-modulaires (une couverture et un maximum le sont, état par état) ; le glouton à cardinal fixé atteint donc au moins `1−1/e` de l'optimum [14] (théorème rapporté ; page à vérifier), version adaptative [15] (notice). *Chiffres* (latent de loi bêta, moyenne 0,1) : 20 tirages d'un seul proposeur donnent 0,58, contre 0,88 s'ils étaient indépendants ; 12 tirages répartis (12, 0, 0), (6, 6, 0), (4, 4, 4) donnent 0,49 ; 0,58 ; 0,63. *Vérification* : (b) dans 200 instances sur 200 ; aucune violation de la sous-modularité sur 120 ; pire rapport du glouton à l'optimum 0,857 (E). *Contre-exemple* : une découverte composite (pièce 1 et pièce 2) vaut 0 pour chaque pièce seule et 1 pour la paire : rendements croissants, le glouton ne voit rien. C'est le cas des moitiés qui doivent se rencontrer (question 4).

**Énoncé 5 — Filtre bon marché.** *Hypothèses* : candidats indépendants, part `π₀` de vrais ; filtre de sensibilité `q_o` et de fausse admission `α_o` ; épreuve sans erreur ; budget grand devant le coût d'un candidat. Le taux de vraies découvertes par unité de coût vaut `π₀/(c_g+c_v)` sans filtre et `π₀·q_o/(c_g+c_f+u·c_v)` avec, où `u = π₀·q_o+(1−π₀)·α_o` est le taux de passage. *Énoncé* : le filtre augmente le taux si et seulement si `c_v·(1−π₀)·(q_o−α_o) > (1−q_o)·c_g+c_f` ; le gain ne dépasse jamais `1/π₀`. *Preuve* : algèbre. *Corollaire* : pour une sous-classe que le filtre reconnaît avec la sensibilité `q_d`, il en augmente le taux si et seulement si `q_d > (c_g+c_f+u·c_v)/(c_g+c_v)`. *Vérification* : signe exact, 5 000 instances sur 5 000 ; tirage de contrôle 0,0607 contre 0,0608 (F). *Contre-exemples* : (i) idées profondes sous-notées : aux coûts de Carbon le seuil vaut 0,068 ; à `q_d = 0,10` le filtre multiplie les ordinaires par 13,3 et les profondes par 1,5 ; à `q_d = 0,03` il multiplie les profondes par 0,45. Un filtre réglé sur l'ordinaire trie contre le profond ; un biais d'évaluateurs humains contre la nouveauté est rapporté [19] (notice seule ; à vérifier). (ii) Candidats rares : si l'on peut tout éprouver, le filtre ne fait que perdre (0,60 découverte attendue contre 0,80).

**Énoncé 6 — Criticalité de l'émergence.** *Hypothèse porteuse* (propriété de branchement) : chaque naissance en induit d'autres indépendamment, selon une même loi de moyenne `n`. *(a)* Si `n ≤ 1` (loi non dégénérée), extinction presque sûre, et descendance totale moyenne `1/(1−n)` pour `n < 1` ; si `n > 1`, survie de probabilité strictement positive (processus de Galton-Watson ; [20], page à vérifier). *(b)* Un processus de Hawkes est stationnaire si et seulement si `n < 1`, par sa représentation en grappes [21] (notice). *(c)* Dans un graphe biparti aléatoire à degrés de Poisson, une composante géante existe si et seulement si `c_A·c_B > 1` [22, p. 1 et 3]. *(d)* Sur un graphe quasi transitif, le seuil de percolation est au moins l'inverse de la valeur propre dominante de la matrice sans retour [25, théorème 4, p. 3] ; la borne devient une égalité quand le graphe est localement arborescent [24, p. 1 et 3]. *Unité* : les trois critères du dossier n'en font qu'un, « la valeur propre dominante de l'opérateur de descendance moyenne vaut 1 ». *Vérification* : descendance 2,01 et 10,11 pour `n = 0,5` et 0,9 ; composante géante 0,163 simulée contre 0,164 théorique à `c_A·c_B = 1,5` (G). *Contre-exemples* : (i) boucles courtes : un réseau triangulaire et sa version recâblée à degrés constants ont le même rayon (5,0000), donc le même seuil prédit (0,2) ; à la probabilité de lien 0,25, leur plus grande composante vaut 0,03 et 0,51, et le seuil exact du premier est 0,347 [26] (notice). Dans un domaine dense en triangles, le critère spectral est nécessaire, non suffisant. (ii) Vivier fini : un cortège aligne un nombre fini `M_φ` de paires ; la « survie » devient une part finale `s = 1−e^{−n·s}` (0,58 à `n = 1,5`), jamais une avalanche sans fin. *Dans le modèle de Fable* : `n = (e^ζ−1)·M_φ·(taux de base × durée)` ; un cortège n'est critique que s'il est large et proche de naître (à multiplicateur 3 et produit taux par durée 0,01, il faut `M_φ ≥ 50`).

Outils nommés par la demande, non mobilisés (notices) : gain d'information espéré [17], qui optimise l'apprentissage d'un paramètre et non la trouvaille ; processus déterminantaux [16], pour tirer des ensembles divers ; seuil de Molloy et Reed [23], qui étend (c) aux degrés quelconques.

## 4. Ce qui se conjecture

1. *L'information totale visée `S*+W` croît avec `Z_r`.* Manque : `W` mesuré en fonction de `S` et de `Z_r`. Plus petit cas : le plan deux par deux de la question 7, sur un monde planté.
2. *Une anomalie ancrée élève le produit de l'a priori et de la chance de détection de son lieu.* Manque : le « gain d'anomalie », succès par oracle à budget égal avec et sans fiche d'anomalie. Plus petit cas : le banc de correspondances plantées de la question 5, contre la référence exacte `1−(1−Rar_τ)^B`.
3. *La portée des découvertes a une queue lourde*, auquel cas l'objectif « la meilleure » et l'énoncé 3 dominent. Manque : la loi de `W`. Plus petit cas : un indice de queue sur les fiches validées d'un monde planté.
4. *Séparer puis confronter bat la mise en commun précoce*, qui corrèle les latents (énoncé 4), pourvu que les moitiés finissent par se rencontrer. Manque : la corrélation induite. Plus petit cas : deux bras à tirages égaux, issue par oracle.
5. *Les cortèges ont la propriété de branchement* : les naissances induites induisent à leur tour, au même taux. Manque : `n` par génération. Plus petit cas : la descendance validée de chaque fiche validée, sur trois générations.
6. *Le « principe variationnel » du directeur est l'égalisation des rendements marginaux par un chercheur optimal* (énoncé 2), non une loi de la nature ; la répartition du travail entre chercheurs est un sujet ancien [8, 9] (notices). Manque : a priori et chances de détection mesurés. Plus petit cas : un monde planté où ils sont connus, l'allocation de l'organisme comparée à celle de Koopman.
7. *Profondeur et étroitesse vont ensemble* (conjecture de la note, section 3). Plus petit cas : un banc à deux dimensions, étroit par profond.

## 5. Ce qui se mesure

**Paramètres dont tout dépend.** A priori `θ_j` et chance de détection `ε_j` par lieu : connus sur monde planté ; ailleurs, fréquences passées par type de lieu. Probabilités `p_i` : calibration des traits sur des fiches éprouvées dans un ordre fixé sans lecteur. Loi de la portée, surtout sa queue. Loi du latent `H` : sur-dispersion de la matrice des succès, proposeur par puits, au-delà du binomial. Caractéristiques du filtre, `q_o`, `α_o` et surtout `q_d`, sur des fiches à vérité connue, la strate profonde comptée à part. Coûts et délais, mesurés et non déclarés. Rapport `n` par génération, largeur `M_φ` des cortèges.

**Sensibilité.** Aux coûts de Carbon, le signe du filtre ne dépend presque pas de `α_o` (il aide dès que `α_o < 0,74`) ; il dépend entièrement de `q_d` (seuil 0,068). L'allocation de Koopman se retourne avec le budget : le lieu le plus rare passe de 0 à 54 % de l'effort entre 30 et 300 tirages. Le croisement de l'énoncé 3 passe de `n = 4` à `n ≈ 10` si l'écart des moyennes, rapporté à l'écart des échelles, passe de 1 à 1,5. Un seul proposeur plafonne : 0,80 à 100 tirages, 0,93 à 1 000. Près du seuil, la taille des cascades varie comme `1/(1−n)` : de 2 à 10 entre `n = 0,5` et 0,9.

**Hors d'atteinte d'une démonstration.** (1) L'a priori sur les lieux : toute politique n'est optimale que relativement à lui (théorèmes d'absence de repas gratuit [27], notice). (2) La justesse des `p_i` annoncés avant l'épreuve : affaire de calibration. (3) La queue de la portée : sans hypothèse sur elle, aucune garantie [13]. (4) La validité de l'oracle hors des classes qu'il couvre : c'est le plafond de Carbon, vrai par construction, invisible de l'intérieur. (5) Le lien entre profondeur mesurée avant coup et fécondité : différé par nature.

## 6. Vérification

Chaque énoncé de la section 3 est vérifié par `enumeration-allocation-decouverte-v1.py` (graine racine 2026112406, dix secondes sur processeur, sortie jointe), parties A à G citées à chaque énoncé. Aucun désaccord entre énoncé et énumération. Le script confirme sur petits paramètres ; il ne remplace pas les preuves.

Deux énoncés méritent un énoncé nu dans l'assistant de preuve Lean 4, le lemme d'échange de l'énoncé 1 et le critère du filtre de l'énoncé 5 : ils sont purement algébriques, et la boucle de l'organisme s'y appuierait. Ils sont écrits en annexe A, non compilés (Lean n'est pas installé dans le conteneur). La dérivation refaite à l'aveugle par un autre modèle, que la reformulation demande, n'a pas été faite : ce mandat interdit tout appel externe.

## 7. Critères de découverte profonde

Règle : chaque mesure est calculée par programme ou par oracle ; aucun avis de lecteur ne sert à choisir une composition. La température n'étant réglable sur aucun proposeur Claude actuel (erratum 2 de la question 3), diversité et dispersion viennent de la composition (modèles, invites, mémoires, questions d'entrée), non d'un réglage.

|Critère|Statut|Mesure dans l'organisme|Étage|Gonflage sans découverte, et parade|
|---|---|---|---|---|
|Ancrage à une anomalie ou à un problème ouvert daté|conjecturé (conjecture 2)|gain d'anomalie à budget égal|choix des questions|rattacher toute fiche à une anomalie célèbre ; ancrage calculé, non déclaré|
|Surprise retirée ailleurs, compression|mesurable (question 2)|baisse de surprise sur des faits tenus à l'écart, hors du voisinage|épreuve, mémoire|redite des faits, hypothèses qui retirent tout ; coût de description des ajouts|
|Compatibilité de structure `Z_r` (couverture et part des conflits à part)|propriétés démontrées (note) ; effet conjecturé|calcul sur les relations du graphe gelé|croisement, tri|taire les conflits (`c−κ` récompense l'esquive) ; relations tirées du graphe, non de la fiche|
|Scission d'une fausse identité|conjecturé|part des anomalies qui tombent après scission, contre un nul de placement (partie II)|croisement|tout scinder ; coût d'un nœud ajouté|
|Objet créé hors de l'alphabet des relations|heuristique|sur monde planté à objet caché : relations prédites confirmées|génération|un objet neuf par fiche ; nombre minimal de relations confirmées|
|Diversité et indépendance des proposeurs|démontré sous latents indépendants (énoncé 4)|sur-dispersion de la matrice proposeur par puits|composition|paraphrases ; diversité comptée sur les issues d'oracle|
|Génération séparée avant confrontation|conjecturé (conjecture 4)|deux bras à tirages égaux|génération, croisement|fausse indépendance (même invite, même mémoire)|
|Coût et délai de l'épreuve|démontré (énoncé 1, réserve avec délai)|coût et délai consignés par fiche|tri, épreuve|idées invérifiables à coût déclaré bas ; coût mesuré|
|Négatifs et taux de base|démontré (énoncé 5 ; [18], notice)|`π₀` par lieu, registre de tous les échecs|mémoire, tri|taire les échecs ; consignation par l'orchestrateur|
|Étanchéité temporelle|condition de validité|date de coupure des modèles contre date de gel ; témoins de rappel|épreuve|rappel présenté comme découverte|
|Conditions d'émergence|démontré sous la propriété de branchement (énoncé 6)|`n` par génération, largeur des cortèges|mémoire, croisement|chaînes d'autocitation ; seules comptent les descendantes validées|
|Queue de la source|démontré dans une famille position-échelle (énoncé 3)|quantile haut de la portée par source|composition|bruit dispersé ; quantile lu sur les issues d'oracle|
|Sensibilité du filtre sur la strate profonde|démontré (énoncé 5)|fiches profondes plantées passées au filtre|tri|sans objet : grandeur du filtre|
|Robustesse aux perturbations des faits|mesurable|tenue du score sous retrait de faits|épreuve|fiches vagues, robustes parce que vides ; exiger des prédictions confirmées|

**Les cinq premiers.** (1) L'épreuve par oracle à vérité, avec taux de base, négatifs consignés et étanchéité temporelle : sans elle rien ne se mesure. (2) L'ancrage à une anomalie datée : seul critère qui agit sur l'a priori des lieux, facteur dominant de l'énoncé 2. (3) L'indépendance réelle des proposeurs avant confrontation : démontrée, peu coûteuse. (4) La sensibilité du filtre mesurée sur la strate profonde : seul étage qui détruit le profond sans que cela se voie. (5) La portée à distance mesurée après coup, avec la compatibilité de structure comme trait avant coup.

**Ce qui me ferait changer d'avis.** Un gain d'anomalie nul à budget égal sur le banc planté ferait descendre (2). Une sur-dispersion nulle de la matrice proposeur par puits rendrait (3) inutile. Un `q_d` mesuré au niveau de `q_o` viderait (4). Une portée sans queue lourde ramènerait l'objectif au nombre espéré, où l'indice `p/c` suffit. Un `n` mesuré très en dessous de 1 partout sortirait les conditions d'émergence de la liste active.

---

# Partie II — La plasticité d'un graphe de domaine, indice d'une zone de découverte ? (question 8 ; suite de la partie I, non refaite)

**Verdict.** Prise comme mollesse de la structure présente (dégénérescence, susceptibilité, écart spectral), la plasticité se calcule mais désigne le désordre : dans le monde planté jouet, elle est plus haute dans le jumeau sans rien à découvrir que dans la région à distinction cachée (aires sous la courbe 0,04 à 0,16). La bonne grandeur est dans la seconde moitié de la question : la part des anomalies qu'une restructuration compatible fait tomber, contre un nul de placement (aire 0,998). Entre anomalies et ouverture, le lien est un seuil avec hystérésis ; onze régions ne peuvent pas le tester, il en faut plus de cent.

## 1. La plasticité, définie

**Cadre.** Une région gelée à la date `t` : des concepts et des relations typées datées, chacune ramenée à un signe (attendue ou anomale au regard de la structure présente). Une restructuration `σ` donne à chaque concept un rôle (distinction binaire, blocs, scission d'un nœud) ; son énergie `E(σ)` compte les relations laissées inexpliquées, plus un coût de description. `E_0` est le nombre d'anomalies avant restructuration, `E_min` le minimum sur une classe fixée d'avance. Rien ne se réfère à la découverte à prédire : pas de circularité.

|Grandeur|Formule|Coût|Confusions, et parade|
|---|---|---|---|
|Dégénérescence|`log₂` du nombre de `σ` à une anomalie de l'optimum ; à grande échelle, entropie a posteriori d'un modèle à blocs stochastiques [47, 49]|`2^(N−1)` états, ou échantillonnage|taille, nœuds de faible degré, densité ; rapporter par concept, contre le nul de recâblage|
|Susceptibilité|part des relations dont le retournement déplace toutes les structures optimales ; voisin : [48]|une optimisation par relation|densité, activité ; apparier sur le degré|
|Mollesse|inverse de l'écart entre les deux plus petites valeurs propres du laplacien signé [50]|une diagonalisation|taille, degré moyen, ponts ; normaliser par le degré|
|Part compressible des anomalies|`1−E_min/E_0`, en écarts types du nul de placement (autant d'anomalies replacées au hasard sur les mêmes relations)|indice de frustration, par programme en nombres entiers [51]|densité de cycles (sur un arbre elle vaut 1 quelles que soient les anomalies) ; le nul de placement la retire|

**Monde planté jouet** (partie E du script : 120 graphes connexes de 20 concepts et 40 relations ; une distinction cachée sur 6 concepts engendre les anomalies, 3 signes sont ensuite retournés au hasard ; le jumeau porte autant d'anomalies, placées au hasard). Aires sous la courbe, région plantée contre jumeau : nombre d'anomalies 0,548 ; dégénérescence 0,042 ; susceptibilité 0,052 ; mollesse 0,161 ; part compressible 0,998, à 4,84 écarts types du nul en moyenne (minimum 2,47).

**Lecture.** Les trois premières grandeurs lisent le désordre. Une région dont les anomalies viennent d'une seule distinction manquante est rigide : optimum unique ou presque (logarithme 0,00 sans bruit, 0,42 avec), susceptibilité 0,02 (0,09), contre 1,76 et 0,36 pour le jumeau. Dans le paysage des restructurations, la zone prometteuse est un puits profond (la part compressible tient sous trois signes retournés : 1,00 puis 0,84, contre 0,61 pour le jumeau) et étroit (peu de voisines font aussi bien) : la forme du puits de la correspondance (note, section 6).

**Le paramètre a-t-il un sens ?** Le mot recouvre deux grandeurs de signes opposés. La mollesse de la structure présente est identifiable, mais se confond avec taille et densité et ne désigne rien. L'existence d'une restructuration compatible qui absorbe les anomalies est identifiable au-dessus d'un seuil de détection (section 2) et distincte du nombre d'anomalies. Je propose de la nommer « part compressible des anomalies » et de ne plus dire « plasticité » sans préciser laquelle.

**Démontré** : un graphe signé est équilibré si et seulement s'il se sépare en deux camps, liens positifs dedans, négatifs entre (théorème de structure [35 ; preuve dans 36]) ; donc `E_min = 0` si et seulement si toutes les anomalies viennent d'une distinction binaire (360 cas sur 360).

## 2. L'anomalie dans la structure

|Forme|Définition|Extraction datée, sans modèle postérieur au gel|Cas de la correspondance|
|---|---|---|---|
|Trou|relation ou nœud attendu absent sous un modèle génératif ajusté à `t` : graphe aléatoire hiérarchique [38], modèle à blocs, liens manquants et liens faux [45]|relations de bases structurées, datées par l'article source ; aucun texte lu|absente entre les images (relation prédite) ; extrémité sans image (objet manquant)|
|Cycle signé frustré|produit des signes négatif [35] ; l'indice de frustration est le nombre minimal de relations à retirer [37]|corrélations positives et négatives datées ; cycles courts énumérés|contredite (comptée dans κ) quand le cycle passe par la correspondance|
|Deux chemins de types incompatibles|généralise le cycle à un alphabet muni d'une composition ; cas signé : l'équilibre équivaut à « tous les chemins entre deux points ont le même signe » [35]|table de composition des types fixée avant `t`|contredite|
|Résidu concentré|l'écart entre l'observé et l'attendu a une valeur propre qui sort du bruit [52]|spectre du résidu|contredites et absentes portées par les mêmes nœuds : profil d'un objet manquant|

Deux résultats du jouet (partie D : résidu sur 400 concepts, structure plantée dans une région de 80). (i) Compter ne distingue rien : 3 677 anomalies avec structure, autant dans le jumeau permuté, 3 620 sous le bruit seul, sur 79 800 paires. (ii) La détection a un seuil : faible jusqu'à la force 1 (0,03 ; 0,11 ; 0,25), certaine à 1,5 ; la valeur propre dominante suit la loi des matrices déformées (2,172 contre 2,167 [53 ; 54, p. 11]) et son vecteur propre localise la région (masse 0,64 contre 0,20 au hasard). Sous le seuil la méthode spectrale ne voit rien ; d'autres méthodes restent à examiner.

Le « trou là où l'on attendrait un nœud relié » du directeur est la première forme, que la prédiction de liens occupe déjà. Une zone de découverte se distinguerait d'un manque de données par la concentration des résidus sur les mêmes nœuds et leur chute sous une même restructuration.

## 3. Les relations demandées

**La structure initiale prédit-elle la plasticité ?** *Mesuré dans un jouet* (partie F : 10 concepts, 3 rôles, toutes les affectations énumérées) : de 0,5 à 3 contraintes par concept, le logarithme décimal du nombre d'états minimaux passe de 3,87 à 1,32, la part de concepts gelés dans un amas de 0,05 à 0,85. *Sur données* : mesurable par la densité de relations typées ; phénomènes connus en satisfaction de contraintes [56] (résumé).

**Prédit-elle la portée hors du point, et l'étroitesse ?** *Démontré dans le cas signé* : dans un graphe connexe équilibré, les deux camps sont uniques à l'échange près, donc le signe de toute relation absente est fixé par n'importe quel chemin [35]. La capacité prédictive hors du point est la rigidité *après* restructuration, non la mollesse avant : la part des relations absentes sur lesquelles toutes les structures optimales s'accordent, grandeur calculable [49]. Un optimum unique, sans voisin presque aussi bon, est un puits étroit au sens de la note. *Conjecturé* : que cette portée locale annonce la portée à distance `W`.

**Un graphe rigide rend-il les puits plus difficiles à trouver ?** Deux rigidités, deux réponses. *Ancienne structure rigide* (section 4) : la barrière par concept passe de 0,12 à 0,33 puis 0,81 quand la rigidité passe de 1,5 à 2 puis 3 : oui. *Structure cherchée très contrainte* (partie F, recherche locale sur instances à solution plantée, 80 concepts) : médiane de 40 retouches à la densité 1 ; 553 à 2 ; 3 680 à 2,6 ; 899 à 3 ; 180 à 10. Facile, difficile, facile : le plus dur est l'intermédiaire, où les contraintes gèlent des amas sans guider ; très contraint, le puits est unique et la pente y mène, motif connu des problèmes à solution plantée [55, p. 1-3]. Mesuré dans le jouet, transposé par analogie.

**Plus d'anomalies, plus d'ouverture ?** Non : un seuil (section 4), et leur nombre seul ne sépare rien (aire 0,548).

## 4. Équilibres et bifurcations

**Modèle minimal.** `N` concepts, chacun dans l'ancien schéma (−1) ou le nouveau (+1), de moyenne `m` ; chacun suit ses voisins avec la force `J` (la rigidité) ; la charge `h` est la charge d'anomalies `A` moins le coût d'entrée `h₀` du schéma nouveau ; `T` est un bruit d'exploration, sans rapport avec la température d'échantillonnage d'un proposeur. Équilibres : `m = tanh((J·m+h)/T)`.

**Démontré dans le modèle** (calcul élémentaire ; parties A et C).

- `J/T ≤ 1` : un seul équilibre, réponse continue, aucune crise.
- `J/T > 1` : deux équilibres stables pour `|h| < h_pli`, où `h_pli = J·m_p−T·artanh(m_p)`, `m_p = √(1−T/J)` ; au pli l'ancien schéma disparaît et `m` saute (de 1,50 à `J/T = 1,5`). Le retour ne se fait qu'à `−h_pli` : hystérésis, de largeur 0,42 (2,61 à `J/T = 3`).
- La susceptibilité de l'ancienne structure diverge au pli (à `J/T = 1,5`) : 0,43 à charge nulle, 2,43 à 90 % de la charge critique, 8,98 à 99 %. La réponse à une anomalie de plus est faible loin du seuil, explosive près de lui.
- Statique ou dynamique : si un afflux d'anomalies alimente la charge et que le schéma en place la résorbe, trois régimes : afflux absorbé (0 bascule) ; bascule unique sans retour (1) ; va-et-vient (60), artefact d'un jouet où seules les anomalies soutiennent le schéma nouveau.

**Indicateurs précurseurs.** Près d'un pli le retour à l'équilibre ralentit, variance et autocorrélation montent [33 ; lu dans 34, p. 19-21]. Dans le modèle (partie B, 300 répliques, 5 % de fausses alarmes), la puissance d'un test de tendance sur 15 instantanés va de 0,06 à 0,17 pour la variance, de 0,02 à 0,05 pour l'autocorrélation ; sur 30, de 0,11 à 0,32 et de 0,03 à 0,07 ; il en faut 300 pour 0,58 à 0,98. Dans une petite région (100 concepts), jusqu'à 89 % des bascules surviennent avant 80 % de la charge critique, poussées par le bruit, sans avertissement. Échecs connus : faux positifs et négatifs, longues séries nécessaires [34, p. 31] ; limites de détection [57] ; changements de régime sans avertissement [58] (résumé). Quinze à trente graphes annuels par région ne portent pas ces indicateurs : le test doit comparer beaucoup de régions à une date, non suivre une région.

**Transposé par analogie**, non démontré : que les concepts soient des unités binaires couplées en moyenne, la charge un scalaire, le bruit stationnaire. La forme n'est pas neuve : réseau de contraintes qui bascule quand assez de données passent à l'hypothèse rivale et résiste à une seule [30] ; modèles dynamiques des révolutions de Kuhn [59, 60], paradigmes en compétition [61] (notices, résumés).

## 5. Le test relationnel et daté (décrit, non lancé)

- **Unité** : une région du graphe, par champ : sous-arbre de profondeur fixée de l'arbre des descripteurs médicaux de la Bibliothèque nationale de médecine des États-Unis (MeSH) ; en réplique, section de la classification des sujets mathématiques, dossier de la bibliothèque mathlib. Plusieurs centaines de régions.
- **Gel** à `t` : relations typées et signées, datées par l'article source (PubTator 3, SemMedDB). Aucun texte libre.
- **Mesure** : part compressible des anomalies, en écarts types du nul ; les trois autres grandeurs comme bases.
- **Issue**, décidée par des comités qui ignorent la mesure : dans les dix ans après `t`, descripteur créé, scindé, fusionné ou déplacé dans la région (le déplacement est le « saut de branche » de Thagard [31 ; lu dans 32, p. 793-794]). Issue secondaire : indice de rupture des articles de la région [40], aux biais discutés [42, 43].
- **Réserve** : l'issue date la reconnaissance, non la découverte : la rubrique des algèbres amassées (13F60) a été créée quand 17 notices de 2003 à 2006 étaient déjà dispersées sur 10 sections (question 9). D'où l'horizon long.
- **Bases à battre** : activité et croissance ; nombre d'anomalies ; meilleurs traits de prédiction de liens ; l'extracteur lexical réfuté ; l'apprentissage supervisé sur les versions passées d'une ontologie, qui prédit déjà les zones d'extension de l'ontologie des gènes (mesure F moyenne jusqu'à 0,79 sur un sous-ensemble [64, p. 1]).
- **Nul** : échanges d'arêtes de même type et de même signe, qui préservent degrés, types et signes, comme chez [44] ; plus le nul de placement.
- **Effets fixes** par champ et par année ; taille et densité en covariables ; modèle de survie stratifié.
- **Prédiction** (signes et seuils proposés, à geler au préenregistrement) : à champ fixé, aire sous la courbe de la part compressible d'au moins 0,60, borne basse à 95 % au-dessus de 0,55, et au moins 0,05 de plus que la meilleure base ; à part compressible fixée, coefficient négatif ou nul pour dégénérescence, susceptibilité et mollesse. **Réfutation** : borne haute sous 0,55 avec au moins 250 régions, ou aucun gain sur « nombre d'anomalies et activité ».
- **Puissance** (partie G) : avec onze régions, il faut une aire observée de 0,80 pour rejeter le hasard, et la puissance va de 0,11 à 0,49 pour une aire vraie de 0,60 à 0,80 ; il faut 120 régions pour une aire vraie de 0,65 (puissance 0,89), 250 pour 0,60 (0,86).
- **Le résultat négatif, dans sa taille** : la rétrodiction préenregistrée des foyers de tension par extraction lexicale (R-5241 : 502 articles, onze sous-domaines, aire 0,1667, intervalle à 95 % de 0 à 0,4667) réfute un comptage de mots dominé par le registre disciplinaire, non une mesure relationnelle. Trois choix évitent sa cause d'échec : aucun mot compté ; effets fixes par champ ; un nul qui conserve types et degrés, soit la part du registre qui passe dans les relations.
- **Monde planté** (prototype : partie E) : une réorganisation plantée ; un jumeau au même nombre d'anomalies placées au hasard, où la mesure doit donner zéro écart type ; un second jumeau sans anomalie. Dose : le nombre de signes retournés ; attendu : un seuil de détection.

## 6. Antériorité, sur PDF

|Source et lecture|Ce qu'elle occupe déjà|Ce qui reste une question|
|---|---|---|
|Kuhn 1962 [28] (PDF, édition de 1970)|la découverte commence par la conscience d'une anomalie (p. 52) ; plus le paradigme est précis, mieux il signale l'anomalie (p. 65) ; en crise, les versions prolifèrent et les règles se relâchent (p. 71, 84, 91)|aucune mesure, aucun seuil|
|Lakatos 1976 [29] (articles de 1963-1964 lus ; livre non lu)|contre-exemples locaux et globaux (I, p. 12) ; exclusion des monstres (p. 15) ; incorporation du lemme (II, p. 130) ; concepts engendrés par la preuve, qui remplacent les concepts naïfs (IV, p. 314-320) : la scission des fausses identités|rien de quantitatif|
|Thagard 1989 [30] (PDF)|cohérence explicative par satisfaction de contraintes, liens excitateurs et inhibiteurs (p. 435-439) ; « harmonie » `Σ w_ij·a_i·a_j` (p. 443) ; bascule et conservatisme (p. 441)|prédiction datée sur graphes extraits, avec nul|
|Thagard 1992 [31] (livre non vu ; source seconde [32, p. 793-794] ; à vérifier)|degrés de changement conceptuel, jusqu'au saut de branche et au changement d'arbre|leur prédiction avant coup|
|Scheffer et collègues 2009 [33] (lu dans [34, p. 19, 21, 31])|indicateurs précurseurs et leurs limites|leur usage sur la science ; un pilote sur deux cas rapporte un signal de contenu, lu par modèles de langage sur titres et résumés, en avance de 25 et de 14 à 19 trimestres sur l'indice de rupture [63, p. 2-4, 7-9]|
|Cartwright et Harary 1956 [35] (PDF)|théorème de structure, équivalence par les chemins (p. 286) ; degré d'équilibre, part des cycles positifs (p. 288) ; équilibre local en un point (p. 289)|son usage comme prédicteur daté d'une restructuration|
|Clauset, Moore et Newman 2008 [38] (PDF, prépublication)|graphe aléatoire hiérarchique, liens manquants (p. 1-3) ; ensemble de dendrogrammes échantillonné (p. 6)|ce qui sépare un trou fécond d'un manque de données|
|Chen 2004 [39] (page web ; pages à vérifier)|points pivots entre fronts de recherche, par tranches de temps ; l'outil « ne comprend aucun algorithme pour détecter ces nœuds par calcul »|la prédiction avant coup|
|Funk et Owen-Smith 2017 [40] (PDF)|indice de rupture, de −1 à 1 (p. 794-795)|—|
|Park, Leahey et Funk 2023 [41] (prépublication)|baisse de l'indice, selon le domaine : 91,9 à 100 % pour les articles, 93,5 à 96,4 % pour les brevets (p. 3)|tendance d'époque, à retirer par effets fixes ; biais discutés [42, 43] (notices)|
|Uzzi et collègues 2013 [44] (PDF)|nul par échanges préservant comptes et dates de citations (p. 468) ; noyau conventionnel et queue atypique : succès 9,11 % contre 5 % (p. 470)|—|
|Guimerà et Sales-Pardo 2009 [45] ; Marvel, Strogatz et Kleinberg 2009 [46] (PDF, prépublications)|fiabilité d'un lien, liens manquants et faux, somme sur toutes les partitions [45, p. 1-2] ; énergie des triades, états coincés [46, p. 1-2]|—|

Voisins trouvés en plus : trous d'un réseau de concepts comme cavités topologiques [62, p. 1-5] ; dégénérescence de la modularité [47] ; « nuage de frustration » des graphes signés [65] et réseaux biologiques signés décomposés en sous-systèmes monotones [66] (notices). Non trouvée : la part compressible des anomalies, contre un nul de placement, comme prédicteur daté d'une restructuration officielle. C'est une question, non une zone vierge : la recherche n'est pas exhaustive, et quand les auteurs de [64] écartent la réorganisation d'une branche entière (p. 13), ils bornent leur article, non le champ.

## 7. Ce que cette partie ne permet pas de conclure

- Qu'une région de part compressible élevée contienne une découverte : le jouet plante la distinction ; rien n'est mesuré sur des données.
- Que les restructurations réelles tiennent dans la classe fixée d'avance : une théorie unificatrice peut exiger un objet hors de l'alphabet, invisible à cette mesure.
- Que le modèle de champ moyen décrive un domaine : c'est une analogie, et son va-et-vient un artefact.
- Que l'issue officielle date la découverte : elle date sa reconnaissance.
- Que le signal existe sous le seuil de détection, ni que la portée à distance suive la portée locale.
- Que l'antériorité soit complète.

---

# Nœuds pour Lazar

Aucun n'engage de dépense ; chacun attend un mot.

1. **Quel objectif gouverne l'organisme d'idéation** : au moins une découverte, leur nombre, ou la meilleure ? L'indice de tri et la règle d'arrêt en dépendent (partie I, section 1). Recommandation : « la meilleure » pour les questions qui visent le profond, « le nombre » pour les bancs d'étalonnage ; confiance moyenne.
2. **Mesurer la sensibilité de tout filtre sur une strate profonde plantée avant de s'en servir** (partie I, énoncé 5), et inscrire au Plan Turing le « gain d'anomalie » et le banc étroit par profond. Recommandation : oui ; confiance élevée pour la première mesure, moyenne pour les deux autres.
3. **Le nom** : réserver « part compressible des anomalies » à la grandeur qui sépare la région plantée de son jumeau, et ne plus dire « plasticité » sans préciser laquelle (partie II, section 1) ; à verser à la version 2 de la note du modèle unifié. Recommandation : oui.
4. **Ouvrir ou non le test relationnel et daté** (partie II, section 5) comme pièce décisive : préenregistrement conçu par Fable, contre-lu par Opus ; issue principale sur les révisions de l'arbre des descripteurs médicaux, réplique sur la classification des sujets mathématiques ; tout sur processeur, avec des données ouvertes à télécharger. Recommandation : d'abord le monde planté, qui ne coûte rien, puis le test ; confiance moyenne.
5. **Vérifications restées à faire**, hors de ce mandat : dérivation refaite à l'aveugle par un autre modèle ; compilation des deux énoncés Lean de l'annexe A ; lectures marquées « à vérifier » dans les références.

---

# Références

État de lecture : « PDF, p. » : lu sur PDF, pages citées (fichiers et empreintes en annexe B) ; « notice » ou « résumé » : existence et référence contrôlées en ligne (Crossref ou arXiv), texte non lu ; « à vérifier » : énoncé ou page non contrôlés.

**Partie I**

1. Weitzman, M. L., « Optimal search for the best alternative », rapport MIT-EL-78-008, 1978. <https://doi.org/10.2172/6795538> (texte : <https://www.osti.gov/servlets/purl/6795538>). PDF, p. 6 à 9. Version publiée : *Econometrica* 47(3), 641-654, 1979, <https://doi.org/10.2307/1910412>, non lue.
2. Gittins, J. C., « Bandit processes and dynamic allocation indices », *Journal of the Royal Statistical Society, Series B* 41(2), 148-164, 1979. <https://doi.org/10.1111/j.2517-6161.1979.tb01068.x>. Notice.
3. Simon, H. A. et Kadane, J. B., « Optimal problem-solving search: all-or-none solutions », *Artificial Intelligence* 6(3), 235-247, 1975. <https://doi.org/10.1016/0004-3702(75)90002-8>. Notice.
4. Kadane, J. B. et Simon, H. A., « Optimal strategies for a class of constrained sequential problems », *The Annals of Statistics* 5(2), 237-255, 1977. <https://doi.org/10.1214/aos/1176343791>. Notice.
5. Koopman, B. O., « The theory of search. III. The optimum distribution of searching effort », *Operations Research* 5(5), 613-626, 1957. <https://doi.org/10.1287/opre.5.5.613>. Notice ; énoncé et page à vérifier.
6. Black, W. L., « Discrete sequential search », *Information and Control* 8(2), 159-162, 1965. <https://doi.org/10.1016/S0019-9958(65)90052-5>. Notice.
7. Peirce, C. S., « Note on the theory of the economy of research » (1879), réimprimé dans *Operations Research* 15(4), 643-648, 1967. <https://doi.org/10.1287/opre.15.4.643>. Notice.
8. Kitcher, P., « The division of cognitive labor », *The Journal of Philosophy* 87(1), 1990, p. 5 et suivantes. <https://doi.org/10.2307/2026796>. Notice.
9. Weisberg, M. et Muldoon, R., « Epistemic landscapes and the division of cognitive labor », *Philosophy of Science* 76(2), 225-252, 2009. <https://doi.org/10.1086/644786>. Notice.
10. Rothschild, M. et Stiglitz, J. E., « Increasing risk: I. A definition », *Journal of Economic Theory* 2(3), 225-243, 1970. <https://doi.org/10.1016/0022-0531(70)90038-4>. Notice.
11. Dahan, E. et Mendelson, H., « An extreme-value model of concept testing », *Management Science* 47(1), 102-116, 2001. <https://doi.org/10.1287/mnsc.47.1.102.10666>. Notice.
12. Girotra, K., Terwiesch, C. et Ulrich, K. T., « Idea generation and the quality of the best idea », *Management Science* 56(4), 591-605, 2010. <https://doi.org/10.1287/mnsc.1090.1144>. Notice.
13. Nishihara, R., Lopez-Paz, D. et Bottou, L., « No regret bound for extreme bandits », 2016. <https://arxiv.org/abs/1508.02933>. PDF (version 3), théorème 11, p. 4.
14. Nemhauser, G. L., Wolsey, L. A. et Fisher, M. L., « An analysis of approximations for maximizing submodular set functions — I », *Mathematical Programming* 14(1), 265-294, 1978. <https://doi.org/10.1007/BF01588971>. Notice ; page du théorème à vérifier.
15. Golovin, D. et Krause, A., « Adaptive submodularity: theory and applications in active learning and stochastic optimization », prépublication, 2010. <https://arxiv.org/abs/1003.3967>. Notice.
16. Kulesza, A. et Taskar, B., « Determinantal point processes for machine learning », *Foundations and Trends in Machine Learning* 5(2-3), 123-286, 2012. <https://doi.org/10.1561/2200000044>. Notice.
17. Lindley, D. V., « On a measure of the information provided by an experiment », *The Annals of Mathematical Statistics* 27(4), 986-1005, 1956. <https://doi.org/10.1214/aoms/1177728069>. Notice.
18. Ioannidis, J. P. A., « Why most published research findings are false », *PLoS Medicine* 2(8), e124, 2005. <https://doi.org/10.1371/journal.pmed.0020124>. Notice.
19. Boudreau, K. J., Guinan, E. C., Lakhani, K. R. et Riedl, C., « Looking across and looking beyond the knowledge frontier: intellectual distance, novelty, and resource allocation in science », *Management Science* 62(10), 2765-2783, 2016. <https://doi.org/10.1287/mnsc.2015.2285>. Notice ; énoncé à vérifier.
20. Harris, T. E., *The Theory of Branching Processes*, Springer, 1963. <https://doi.org/10.1007/978-3-642-51866-9>. Notice ; page à vérifier.
21. Hawkes, A. G. et Oakes, D., « A cluster process representation of a self-exciting process », *Journal of Applied Probability* 11(3), 493-503, 1974. <https://doi.org/10.2307/3212693>. Notice.
22. Newman, M. E. J., Strogatz, S. H. et Watts, D. J., « Random graphs with arbitrary degree distributions and their applications », *Physical Review E* 64, 026118, 2001. <https://arxiv.org/abs/cond-mat/0007235>. PDF (prépublication, version 2), p. 1 et 3 ; l'article traite les degrés quelconques et les graphes bipartis, le cas des degrés de Poisson s'en déduit.
23. Molloy, M. et Reed, B., « A critical point for random graphs with a given degree sequence », *Random Structures & Algorithms* 6(2-3), 161-180, 1995. <https://doi.org/10.1002/rsa.3240060204>. Notice.
24. Karrer, B., Newman, M. E. J. et Zdeborová, L., « Percolation on sparse networks », *Physical Review Letters* 113, 208702, 2014. <https://arxiv.org/abs/1405.0483>. PDF (prépublication, version 2), p. 1, 3, 4 et 6 ; matrice sans retour non pondérée.
25. Hamilton, K. E. et Pryadko, L. P., « Tight lower bound for percolation threshold on an infinite graph », *Physical Review Letters* 113, 208701, 2014. <https://arxiv.org/abs/1405.0050>. PDF (prépublication, version 1, intitulée « … on a quasi-regular graph »), p. 1 et 3 ; le théorème 4 porte sur les graphes simples quasi transitifs.
26. Sykes, M. F. et Essam, J. W., « Exact critical percolation probabilities for site and bond problems in two dimensions », *Journal of Mathematical Physics* 5(8), 1117-1127, 1964. <https://doi.org/10.1063/1.1704215>. Notice.
27. Wolpert, D. H. et Macready, W. G., « No free lunch theorems for optimization », *IEEE Transactions on Evolutionary Computation* 1(1), 67-82, 1997. <https://doi.org/10.1109/4235.585893>. Notice.

**Partie II**

28. Kuhn, T. S., *The Structure of Scientific Revolutions*, University of Chicago Press, 1962 ; deuxième édition augmentée, 1970. Copie lue : <https://www.lri.fr/~mbl/Stanford/CS477/papers/Kuhn-SSR-2ndEd.pdf>. PDF de la deuxième édition, p. 52, 65, 71, 84, 91 ; la pagination de l'édition de 1962 n'a pas été vue.
29. Lakatos, I., *Proofs and Refutations: The Logic of Mathematical Discovery*, Cambridge University Press, 1976. <https://doi.org/10.1017/CBO9781139171472>. Livre non lu (table des matières de l'éditeur seulement). Lu : les articles dont il est tiré, « Proofs and refutations » (I) à (IV), *The British Journal for the Philosophy of Science* 14, numéros 53 à 56, 1963-1964 (<https://doi.org/10.1093/bjps/XIV.53.1>, <https://doi.org/10.1093/bjps/XIV.54.120>, et les deux numéros suivants). PDF, partie I p. 12 et 15, partie II p. 130, partie IV p. 314 et 320.
30. Thagard, P., « Explanatory coherence », *Behavioral and Brain Sciences* 12(3), 435-467, 1989. <https://doi.org/10.1017/S0140525X00057046>. PDF, p. 435 à 443.
31. Thagard, P., *Conceptual Revolutions*, Princeton University Press, 1992. <https://doi.org/10.1515/9780691186672>. Livre non vu ; contenu rapporté par [32] ; à vérifier.
32. Bozdag, S. et De Benedetto, M., « Taking up Thagard's challenge: a formal model of conceptual revision », *Journal of Philosophical Logic* 51(4), 791-824, 2022. <https://doi.org/10.1007/s10992-021-09650-4>. PDF, p. 793-794.
33. Scheffer, M. et collègues, « Early-warning signals for critical transitions », *Nature* 461, 53-59, 2009. <https://doi.org/10.1038/nature08227>. Lu dans la reproduction de [34] ; pagination de la revue non vue.
34. Dakos, V., *Expecting the unexpected*, thèse, université de Wageningen, 2011, chapitre 2 (« This chapter is based on the paper » [33]). <https://edepot.wur.nl/168815>. PDF, p. 19, 21 et 31 de la thèse.
35. Cartwright, D. et Harary, F., « Structural balance: a generalization of Heider's theory », *Psychological Review* 63(5), 277-293, 1956. <https://doi.org/10.1037/h0046049>. PDF, p. 286, 288 et 289.
36. Harary, F., « On the notion of balance of a signed graph », *Michigan Mathematical Journal* 2(2), 143-146, 1953. <https://doi.org/10.1307/mmj/1028989917>. Notice.
37. Harary, F., « On the measurement of structural balance », *Behavioral Science* 4(4), 316-323, 1959. <https://doi.org/10.1002/bs.3830040405>. Notice.
38. Clauset, A., Moore, C. et Newman, M. E. J., « Hierarchical structure and the prediction of missing links in networks », *Nature* 453, 98-101, 2008. <https://arxiv.org/abs/0811.0484>. PDF (prépublication, version 1), p. 1 à 3 et 6.
39. Chen, C., « Searching for intellectual turning points: progressive knowledge domain visualization », *Proceedings of the National Academy of Sciences* 101 (supplément 1), 5303-5310, 2004. <https://doi.org/10.1073/pnas.0307513100>. Texte lu sur la page de PubMed Central (<https://pmc.ncbi.nlm.nih.gov/articles/PMC387312/>) ; pages à vérifier.
40. Funk, R. J. et Owen-Smith, J., « A dynamic network measure of technological change », *Management Science* 63(3), 791-817, 2017. <https://doi.org/10.1287/mnsc.2015.2366>. PDF, p. 791, 794 et 795.
41. Park, M., Leahey, E. et Funk, R. J., « Papers and patents are becoming less disruptive over time », *Nature* 613, 138-144, 2023. <https://doi.org/10.1038/s41586-022-05543-x>. Lu : la prépublication, <https://arxiv.org/abs/2106.11184> (version 2), p. 3 ; les chiffres de la version publiée peuvent différer.
42. Petersen, A. M., Arroyave, F. et Pammolli, F., « The disruption index is biased by citation inflation », *Quantitative Science Studies* 5(4), 936-953, 2024. <https://doi.org/10.1162/qss_a_00333>. Notice.
43. Holst, V. et collègues, « Dataset artefacts are the hidden drivers of the declining disruptiveness in science », prépublication, 2024. <https://arxiv.org/abs/2402.14583>. Notice.
44. Uzzi, B., Mukherjee, S., Stringer, M. et Jones, B., « Atypical combinations and scientific impact », *Science* 342(6157), 468-472, 2013. <https://doi.org/10.1126/science.1240474>. PDF, p. 468 et 470.
45. Guimerà, R. et Sales-Pardo, M., « Missing and spurious interactions and the reconstruction of complex networks », *Proceedings of the National Academy of Sciences* 106(52), 22073-22078, 2009. <https://arxiv.org/abs/1004.4791>. PDF (prépublication), p. 1 et 2.
46. Marvel, S. A., Strogatz, S. H. et Kleinberg, J. M., « Energy landscape of social balance », *Physical Review Letters* 103, 198701, 2009. <https://arxiv.org/abs/0906.2893>. PDF (prépublication, version 2), p. 1 et 2.
47. Good, B. H., de Montjoye, Y.-A. et Clauset, A., « Performance of modularity maximization in practical contexts », *Physical Review E* 81, 046106, 2010. <https://arxiv.org/abs/0910.0165>. PDF (prépublication), p. 1.
48. Karrer, B., Levina, E. et Newman, M. E. J., « Robustness of community structure in networks », *Physical Review E* 77, 046119, 2008. <https://arxiv.org/abs/0709.2108>. PDF (prépublication), p. 1.
49. Peixoto, T. P., « Revealing consensus and dissensus between network partitions », *Physical Review X* 11, 021003, 2021. <https://arxiv.org/abs/2005.13977>. PDF (prépublication), p. 1.
50. Kunegis, J. et collègues, « Spectral analysis of signed graphs for clustering, prediction and visualization », *Proceedings of the 2010 SIAM International Conference on Data Mining*, 559-570. <https://doi.org/10.1137/1.9781611972801.49>. Notice.
51. Aref, S., Mason, A. J. et Wilson, M. C., « A modeling and computational study of the frustration index in signed networks », *Networks* 75(1), 95-110, 2020. <https://doi.org/10.1002/net.21907>. Notice.
52. Lei, J., « A goodness-of-fit test for stochastic block models », *The Annals of Statistics* 44(1), 401-424, 2016. <https://arxiv.org/abs/1412.4857>. PDF (prépublication), p. 1.
53. Baik, J., Ben Arous, G. et Péché, S., « Phase transition of the largest eigenvalue for nonnull complex sample covariance matrices », *The Annals of Probability* 33(5), 1643-1697, 2005. <https://arxiv.org/abs/math/0403022>. PDF téléchargé ; résumé seul lu.
54. Benaych-Georges, F. et Nadakuditi, R. R., « The eigenvalues and eigenvectors of finite, low rank perturbations of large random matrices », *Advances in Mathematics* 227(1), 494-521, 2011. <https://arxiv.org/abs/0910.2120>. PDF (prépublication, version 3), p. 11.
55. Krzakala, F. et Zdeborová, L., « Hiding quiet solutions in random constraint satisfaction problems », *Physical Review Letters* 102, 238701, 2009. <https://arxiv.org/abs/0901.2130>. PDF (prépublication), p. 1 à 3.
56. Zdeborová, L. et Krzakala, F., « Phase transitions in the coloring of random graphs », *Physical Review E* 76, 031131, 2007. <https://doi.org/10.1103/PhysRevE.76.031131>. Résumé.
57. Boettiger, C. et Hastings, A., « Quantifying limits to detection of early warning for critical transitions », *Journal of the Royal Society Interface* 9(75), 2527-2539, 2012. <https://arxiv.org/abs/1204.6231>. PDF (prépublication), p. 1.
58. Hastings, A. et Wysham, D. B., « Regime shifts in ecological systems can occur with no warning », *Ecology Letters* 13(4), 464-472, 2010. <https://doi.org/10.1111/j.1461-0248.2010.01439.x>. Résumé.
59. Sterman, J. D., « The growth of knowledge: testing a theory of scientific revolutions with a formal model », *Technological Forecasting and Social Change* 28(2), 93-122, 1985. <https://doi.org/10.1016/0040-1625(85)90009-5>. Notice.
60. Sterman, J. D. et Wittenberg, J., « Path dependence, competition, and succession in the dynamics of scientific revolution », *Organization Science* 10(3), 322-341, 1999. <https://doi.org/10.1287/orsc.10.3.322>. Résumé.
61. Bornholdt, S., Jensen, M. H. et Sneppen, K., « Emergence and decline of scientific paradigms », *Physical Review Letters* 106, 058701, 2011. <https://doi.org/10.1103/PhysRevLett.106.058701>. Résumé.
62. Ju, H. et collègues, « The network structure of scientific revolutions », prépublication, 2020. <https://arxiv.org/abs/2010.08381>. PDF (version 2), p. 1, 3 et 5.
63. Ustyuzhanin, A., Trofimova, E. et Zuenko, D., « Citations are late. Reading epistemic instability from what papers believe, years before the citation graph catches up », prépublication, 2026. <https://arxiv.org/abs/2610.07397>. PDF (version 1), p. 2 à 4 et 7 à 9.
64. Pesquita, C. et Couto, F. M., « Predicting the extension of biomedical ontologies », *PLoS Computational Biology* 8(9), e1002630, 2012. <https://doi.org/10.1371/journal.pcbi.1002630>. PDF, p. 1 et 13.
65. Rusnak, L. et Tešić, J., « Characterizing attitudinal network graphs through frustration cloud », *Data Mining and Knowledge Discovery* 35(6), 2498-2539, 2021. <https://doi.org/10.1007/s10618-021-00795-z>. Notice.
66. DasGupta, B., Enciso, G. A., Sontag, E. et Zhang, Y., « Algorithmic and complexity results for decompositions of biological networks into monotone subsystems », *Biosystems* 90(1), 161-178, 2007. <https://doi.org/10.1016/j.biosystems.2006.08.001>. Notice.

**Vérifiées et écartées du texte** (pistes de la demande reformulée, non utilisées faute de lecture) : Kauffman et Levin 1987 (<https://doi.org/10.1016/S0022-5193(87)80029-2>) ; Decelle, Krzakala, Moore et Zdeborová 2011 (<https://doi.org/10.1103/PhysRevLett.107.065701>) ; Leydesdorff, Wagner et Bornmann 2018 (<https://doi.org/10.1007/s11192-018-2734-6>) ; Burt 2004 (<https://doi.org/10.1086/421787>) ; Dakos et collègues 2012 (<https://doi.org/10.1371/journal.pone.0041010>). **Cherchées et non trouvées** (non citées) : Mitten 1960 sur l'ordre d'épreuve ; Cicirello et Smith 2005 sur les bandits visant le maximum ; Cheeseman et collègues 1991 sur la transition de difficulté.

---

# Annexe A — Vérifications par script, et énoncés nus en Lean 4

**`enumeration-allocation-decouverte-v1.py`** (partie I ; graine racine 2026112406, sept graines filles par `numpy.random.SeedSequence` ; numpy et bibliothèque standard, fractions exactes là où c'est possible ; environ dix secondes).

|Énoncé|Partie|Ce qui est énuméré ou simulé|Résultat|
|---|---|---|---|
|Distance optimale (section 2)|A|800 tirages de paramètres, maximum cherché sur une grille de pas 10⁻⁴, dérivées par différences finies|aucun désaccord avec la condition d'existence ; formes closes à 3·10⁻¹⁰ près|
|Énoncé 1, ordre `p/c`|B1|260 instances de 3 à 7 candidats, toutes les permutations|260 sur 260|
|Section 1, deux objectifs sous budget dur|B2|400 instances de 6 candidats, tous les sous-ensembles|43 divergences, perte maximale 0,135|
|Énoncé 1, politique de réserve|B3, B4|300 instances sans délai et 300 avec, 3 à 5 boîtes, programmation dynamique exhaustive|300 sur 300 deux fois ; l'indice `E[X]/c` perd dans 162 cas|
|Énoncé 2, allocation de Koopman|C|150 instances de 4 cellules, budgets de 5 à 18 tirages, toutes les répartitions|150 sur 150|
|Énoncé 3, maximum|D|calcul exact sur lois finies ; lois normales|croisement à `x* = 2` ; A devant dès `n = 4`|
|Énoncé 4, diversité|E|200 instances de répartition ; 120 instances de 6 candidats et 8 états du monde|200 sur 200 ; aucune violation ; pire rapport du glouton 0,857|
|Énoncé 5, filtre|F|5 000 instances ; un tirage de contrôle|5 000 sur 5 000 ; 0,0607 contre 0,0608|
|Énoncé 6, émergence|G|processus de Galton-Watson ; graphe biparti de 500 et 8 000 nœuds ; réseau triangulaire de 64 par 64 et sa version recâblée ; vivier fini de 2 000 paires|accord avec la théorie à la taille finie près ; contre-exemple des boucles courtes|

**`simulation-plasticite-bifurcation-v1.py`** (partie II ; graine racine 2026112408, six graines filles ; moins d'une minute) : A, champ moyen (plis, sauts, susceptibilité, barrières) ; B, indicateurs précurseurs (300 répliques par case) ; C, système lent et rapide (trois régimes) ; D, résidu structuré (400 concepts, région de 80) ; E, anomalies de signe (120 graphes de 20 concepts, les 2¹⁹ séparations en deux camps énumérées) ; F, contraintes de rôles (59 049 affectations énumérées ; recherche locale sur 80 concepts) ; G, puissance d'une aire sous la courbe selon le nombre de régions.

**Deux énoncés nus en Lean 4**, non compilés (Lean n'est pas installé dans le conteneur) ; le premier est le lemme d'échange de l'énoncé 1 pour deux candidats, le second le critère du filtre de l'énoncé 5.

```lean
import Mathlib

/-- Lemme d'échange : éprouver d'abord le candidat de plus grand rapport
probabilité sur coût ne coûte pas plus, en espérance, jusqu'au premier succès. -/
theorem echange_adjacent (p₁ p₂ c₁ c₂ : ℝ) (hc₁ : 0 < c₁) (hc₂ : 0 < c₂)
    (h : p₂ / c₂ ≤ p₁ / c₁) :
    c₁ + (1 - p₁) * c₂ ≤ c₂ + (1 - p₂) * c₁ := by
  sorry

/-- Critère du filtre : p0 part de vrais, q sensibilité, a fausse admission,
cg, cf, cv coûts d'un candidat, du filtre et de l'épreuve. -/
theorem critere_filtre (p0 q a cg cf cv : ℝ) (hp : 0 < p0) (hp1 : p0 < 1)
    (hq : 0 < q) (ha : 0 ≤ a) (hcg : 0 ≤ cg) (hcf : 0 ≤ cf) (hcv : 0 < cv) :
    p0 / (cg + cv) < p0 * q / (cg + cf + (p0 * q + (1 - p0) * a) * cv)
      ↔ (1 - q) * cg + cf < cv * (1 - p0) * (q - a) := by
  sorry
```

# Annexe B — Sources lues sur fichier, avec empreintes

Dossier : `/tmp/claude-0/-home-user-controle-ia-travail/72cb7e89-3107-5c40-8de3-bdb9cf3a5211/scratchpad/pdf-q6-q8/` (la page de Chen 2004 est sous `…/scratchpad/html-q6-q8/`). Empreintes SHA-256.

- `baik-ben-arous-peche-2005-arxiv-math-0403022v2.pdf` — `09c7b1bd0432390bfe108254280e57f621255251c7e571bce7572d0ca3bfd897`
- `benaych-georges-nadakuditi-2011-arxiv-0910.2120v3.pdf` — `aa2955815d315f6d6b793cae3a4c63a91f7fd3a5f0b2269bcece7e999835e242`
- `boettiger-hastings-2012-arxiv-1204.6231v1.pdf` — `ba12224f06815fd6f0a21025cd0713af75fa1ff56f264e35f3df2a252659006f`
- `cartwright-harary-1956-structural-balance.pdf` — `39f4d81139e8b5ce7d02c0ffd211a555655fcb9ef9570e2b4d5f18cc055361c5`
- `clauset-moore-newman-2008-arxiv-0811.0484v1.pdf` — `dd8a5a729b502b6b12ed92400f3d24c45e256dffd29555881c81ac3cf555b1ac`
- `dakos-2011-these-wageningen-chapitre-2-reproduit-scheffer-2009.pdf` — `c679753fe79cf20c95911ce24c4a265e5d43ff0e99bb6ed16aa1b05bb6f3ffb1`
- `funk-owen-smith-2017-management-science-63-791.pdf` — `dad58420e88f0a68f945fe7b5a762d317cb140ca1955ada81debc0628609ac42`
- `good-montjoye-clauset-2010-arxiv-0910.0165v2.pdf` — `ef2dcc72f62a9a839c5a3289aa9712978f5ba48a14d485cb13658d69556ed8ab`
- `guimera-sales-pardo-2009-arxiv-1004.4791v1.pdf` — `c5af49e3777608f68f4130f5814d71d4fcb1b82690de542aca304023ceabfad2`
- `hamilton-pryadko-2014-arxiv-1405.0050v1.pdf` — `65fb4e9017dec124d30bc786b274480538776c7d0a9a13b43370cc9e0f38818d`
- `ju-et-al-2020-arxiv-2010.08381v2.pdf` — `200851e6540841d086f0066771a7ec0818caf6c70a8b5634e88c61d61151fb60`
- `karrer-levina-newman-2008-arxiv-0709.2108v1.pdf` — `fa6803edd684c0e462437f58f304056765e41140ae66ff98767f8b606e659286`
- `karrer-newman-zdeborova-2014-arxiv-1405.0483v2.pdf` — `e55f25f65c23f88aabeac30bb381c4c05596bbec6cbec6adfe47552753e02824`
- `krzakala-zdeborova-2009-arxiv-0901.2130v2.pdf` — `4e9031703ea10f6824abf2256f5e0b45f04f743cf16e62c8bb0fb88de200d525`
- `kuhn-1970-structure-of-scientific-revolutions-2e-ed.pdf` — `a80d2659b084e2c0e5adea1dc8b32e91e1ef29dce5db8213de155df04116b2bd`
- `lakatos-1963-1964-proofs-and-refutations-bjps-14-parties-I-a-IV.pdf` — `a3a9c369d58960cd076e48e0c531289c814ffea39741c08ba26fd04db79716cb`
- `lakatos-1976-proofs-and-refutations-table-des-matieres-cup-2015.pdf` — `649ffb938b86bd7aa16e7032eb039d54eeb984ba9ad93ba553d252361cfac9cc`
- `lei-2016-arxiv-1412.4857v2.pdf` — `eff8cf028fea8b2f539fb634ce4ca2ccf08bdfed97503eddffe6599778dad237`
- `marvel-strogatz-kleinberg-2009-arxiv-0906.2893v2.pdf` — `170857a9b30441379f15dfb8e593b06507d5f6db3097f1e4cc6e0e879b22a377`
- `newman-strogatz-watts-2001-arxiv-cond-mat-0007235v2.pdf` — `939b3d7d96af9aa1d1ac750b22847a8b4383ad4369f81e783c7a665cdb3c7c02`
- `nishihara-lopez-paz-bottou-2016-arxiv-1508.02933v3.pdf` — `50159c0c9435470c4b39cc9dbd5a90943bd6e4f2b5a2773d98f5d5f688776151`
- `park-leahey-funk-2023-arxiv-2106.11184v2.pdf` — `1a9bb5cbe0d75f2f89d965060367c7f4ce5d28c5305d1bb836928283d9912689`
- `peixoto-2021-arxiv-2005.13977v5.pdf` — `b389d42f4367596444628082917ef1bacb96cbd5c28b960deacf59c632e264e1`
- `pesquita-couto-2012-plos-comput-biol-8-e1002630.pdf` — `b3141cd7acfd03442da512262b7d708afa80375ba2abfc7fe803f48e6a7f7a56`
- `source-seconde-thagard-1992-jpl-2021-s10992-021-09650-4.pdf` — `6f0032e94c8fa7f21667a543ee3853560234af748cf23b5a150fd2cc2b9aeeda`
- `thagard-1989-explanatory-coherence-bbs-12-435.pdf` — `54010c6aecbb229dea20f464a2a06fd6214ccf037973e78904a17b84fd7f5492`
- `ustyuzhanin-et-al-2026-arxiv-2610.07397v1.pdf` — `c5f56cd4232509832c05629880bdf522f824558a219c1335a2c7656c882ec837`
- `uzzi-et-al-2013-science-342-468.pdf` — `ff927fdb43bde2b13f56ca2234848fccf1154652e4d7e1c9f818237df05d298a`
- `weitzman-1978-rapport-osti-6795538.pdf` — `546b8b0344acd58b96e2ea9ab753a3b70dd87803d9ecd4d7b69b7fdb15373303`
- `chen-2004-pmc.html` — `e34c0c4dd10537001043d0185ce8cdfeb6c23d47da7043722ac6207157820681`
