# Réponse à la question 10 du directeur : ce que la forme d'une anomalie permet de prédire du rôle de l'objet manquant (v1)

- **Nature** : pièce de travail (classe C). Aucune dépense, aucun appel à un modèle externe, calculs sur processeur seulement. Non committée.
- **Heure** : `2026-11-28T06:06:14Z` (`date -u`, fin de rédaction).
- **Auteur** : Claude Fable 5.2, sous-agent ; branche `idees/questions-directeur-2026-11-24-v1`.
- **Demande servie** : question 10, telle que reformulée (`demandes-reformulees-quatre-points-q8-q11-v1.md`, `632c7af2…`, lignes 89 à 120), avec la consigne du directeur (`complement-questions-10-11-et-apport-q5-v1.md`, `43716a8a…`).
- **Lus** : `CLAUDE.md` (`c6a1ca39…`) ; réponse aux questions 6 et 8 (`2ba05ea6…`) ; réponse à la question 7 (`937e3e69…`) ; erratum des notations (`72afe693…`) ; note du modèle unifié (`f2f0a700…`, section sur la correspondance) et son erratum 1 (`619b6feb…`). Rien d'ouvert sous `coffre/`, `docs/verdicts/`, `runs/`, `diag/`, `donnees/`.
- **Script joint**, même dossier : `forme-anomalie-objet-manquant-v1.py` (`47da91c6…`), sortie `forme-anomalie-objet-manquant-v1-sortie.txt` (`b2cfaa0e…`) ; graine racine 2026112810 (`numpy.random.SeedSequence`) ; 75 secondes ; deux exécutions, sorties identiques. Les critères de mort du monde planté sont écrits en tête du script avant la première exécution ; ce n'est pas un préenregistrement scellé, et le jouet n'est pas une expérience décisive.
- **Notations** : celles de la note du modèle unifié. `φ` est une correspondance (injection partielle) d'un voisinage source `A` vers un voisinage cible `B` ; une relation est confirmée (C1), contredite (C2, comptée dans la part des conflits `κ`), absente (C3) ou à extrémité sans image (C4) ; `Π_φ(y)` est le profil d'un nœud sans image.
- **Statuts** : « démontré » = hypothèses écrites et preuve donnée ou citée à la page ; « mesuré » = calculé sur un jouet. Références numérotées en fin de pièce, chacune avec son état de lecture.
- **Longueur** : sections « Verdict » à « Nœuds pour Lazar », 4 508 mots (`wc -w`, locale UTF-8, lignes de séparation des tableaux comprises).

---

## Verdict

1. La forme d'une anomalie fixe l'objet manquant **à isomorphisme près** dans quatre cadres où le résidu vit dans une structure de groupe : transports le long des relations d'un graphe (énoncé 2), monodromie (3), loi de composition tenue à un facteur près (4), caractère d'une représentation (6). Démontré ; l'énoncé 2 est la partie utile au graphe de domaine.
2. Hors de ces cadres, elle fixe au mieux le type et quelques invariants (champ extérieur d'une masse), et un résidu réduit à **un nombre** ne départage rien : dans le monde planté, l'exactitude « objet contre loi » vaut 0,47 à 0,51 avec un corps d'épreuve, 0,997 avec quatre.
3. « La forme prédit le type » est donc un théorème conditionnel, non une loi de l'histoire : Neptune, Mendeleïev et le clair de lune monstrueux la servent, leurs résidus étant riches ; Mercure, le nébulium et le spectre bêta la desservent. Le test sur un corpus daté reste à faire.

## 1. Définitions, posées avant les cas

**Anomalie.** Le résidu `ρ` = observé moins prédit par la théorie de base, dans un espace à nommer : un nombre, une fonction du temps, une famille indexée par des corps d'épreuve, des étiquettes sur les relations d'un graphe, une table de coïncidences entières.

**Forme.** Un invariant de `ρ` sous les changements de convention qui n'en changent pas le contenu. Liste fixée d'avance : (F1) le profil d'un nœud sans image ; (F2) la classe d'holonomie des transports le long des cycles ; (F3) la classe d'un facteur de composition (2-cocycle) ; (F4) la liste des facteurs simples d'un groupe de symétries ; (F5) la loi d'échelle du résidu sur plusieurs corps d'épreuve ; (F6) la décomposition d'entiers en dimensions de représentations ; (F0) un nombre seul.

**Type de l'objet manquant.** (T1) objet nouveau d'un genre connu (une planète, un élément) ; (T2) attribut caché porté par les objets connus (une distinction, un potentiel) ; (T3) dédoublement d'objets connus (une fausse identité à scinder) ; (T4) objet d'un genre nouveau qui change la règle de composition (un groupe plus gros, un espace gradué) ; (T5) loi changée ; (T6) erreur, fermée par remesure ou recalcul.

**La thèse.** Une application `Φ` des formes vers les types. Trois forces : (I) la forme détermine l'objet à isomorphisme près ; (II) le type et quelques invariants ; (III) rien.

## 2. Ce qui se démontre

### Énoncé 1 — Le trou : le profil est le rôle, et rien de plus

*Hypothèses.* `y` est un nœud de `A` sans image, dont tous les voisins ont une image. *Énoncé.* (a) Un objet `y*` ajouté à `B` rend confirmées toutes les relations de `y` si et seulement si ses relations avec l'image de `φ` contiennent `Π_φ(y)`. (b) Deux comblements de `B` par un objet qui porte exactement ce profil sont isomorphes par un isomorphisme qui fixe `B`. (c) Le profil ne dit rien des relations de `y*` avec les nœuds hors de l'image. *Preuve.* (a) est la définition de (C1) appliquée à chaque relation de `y`. (b) : envoyer un objet sur l'autre préserve toutes les relations, puisqu'ils ont les mêmes. (c) : ajouter à `y*` une relation vers un nœud hors de l'image ne change le cas d'aucune relation de `A`. ∎

Force (II) : le type (T1, un objet du genre de ses voisins) et le rôle, non l'objet.

**Énoncé 1 bis — Quand une case vide est-elle déterminée ?** *Hypothèses.* Une propriété suit un modèle additif `x_ij = l_i + c_j` (ligne plus colonne) ; certaines cases sont observées. *Énoncé.* La case `(i, j)` est déterminée si et seulement si la ligne `i` et la colonne `j` sont reliées dans le graphe biparti des cases observées. *Preuve.* Si un chemin `i, j₁, i₁, …, j` existe, `x_ij` est la somme alternée des cases du chemin (pour un rectangle : `x_ij = x_ij₁ − x_i₁j₁ + x_i₁j`). Sinon, ajouter une constante aux lignes de la composante de `i` et la retrancher à ses colonnes conserve toutes les cases observées et change `x_ij`. ∎ *Contre-exemple.* Une colonne entièrement absente n'est reliée à rien : le tableau ne prédit ni ses valeurs ni son existence.

### Énoncé 2 — Les conflits : attribut caché ou dédoublement, selon l'holonomie

Version discrète, sur un graphe, des pistes « monodromie » et « section locale qui ne se recolle pas ».

*Cadre.* `Γ` est un graphe connexe. Chaque relation orientée `e : u → v` porte un transport `g_e` dans un groupe `G` (le transport de la relation renversée est l'inverse) : il dit comment un attribut se transmet le long de la relation (pour des signes, `G = {+1, −1}` : « même camp » ou « camp opposé »). Un **potentiel** est une attribution `h` d'un élément de `G` à chaque sommet, avec `h(v) = g_e·h(u)` sur toute relation. L'**holonomie** d'un circuit fermé partant de `v₀` est le produit de ses transports ; ces produits forment un sous-groupe `Hol` de `G`, défini à conjugaison près quand on change `v₀`. L'anomalie est l'absence de potentiel ; sa forme est `Hol`.

*Énoncé.* (a) Un potentiel existe si et seulement si `Hol` est trivial ; les potentiels sont alors exactement les `h·c`, `c` dans `G` : l'attribut caché est unique à un choix global près. (b) Soit `Γ̂` le graphe de sommets `(x, a)`, `a` dans `G`, et de relations `(u, a) → (v, g_e·a)`. Sur `Γ̂`, `ĥ(x, a) = a` est un potentiel. La composante `Γ̂₀` de `(v₀, 1)` est un revêtement connexe de `Γ` à `|Hol|` feuillets. (c) Tout revêtement connexe de `Γ` sur lequel les transports relevés admettent un potentiel revêt `Γ̂₀` : son nombre de feuillets est un multiple de `|Hol|`, et s'il vaut `|Hol|` il est isomorphe à `Γ̂₀`.

*Preuve.* (a) Si `h` existe, le long d'un circuit fermé `h(v₀) = (produit)·h(v₀)`, donc le produit vaut 1. Réciproquement, on pose `h(x)` égal au produit des transports le long d'un chemin de `v₀` à `x` : deux chemins diffèrent par un circuit fermé, d'holonomie 1. Si `h` et `h′` sont deux potentiels, `h(x)⁻¹·h′(x)` est constant le long de chaque relation, donc constant. (b) La relevée d'une relation part de `(u, a)` et arrive en `(v, g_e·a)` : `ĥ` est un potentiel par construction. Relever un circuit fermé de `v₀` depuis `(v₀, 1)` mène à `(v₀, holonomie)` : la fibre de `Γ̂₀` au-dessus de `v₀` est `Hol`. (c) Soit `p : Γ′ → Γ` un tel revêtement, `h′` son potentiel, `v₀′` au-dessus de `v₀`. L'application `F(x′) = (p(x′), h′(x′)·h′(v₀′)⁻¹)` envoie relation sur relation, commute aux projections et envoie `v₀′` sur `(v₀, 1)` ; son image est dans `Γ̂₀` par connexité. Un morphisme entre revêtements connexes est lui-même un revêtement (fait standard) : le nombre de feuillets de `Γ′` est le degré de `F` fois `|Hol|`. ∎

*Vérification.* 240 graphes, groupes à 2, 3, 4 éléments et groupe des permutations de trois objets : (a), le compte des potentiels par force brute et la fibre, 240 sur 240 ; aucun revêtement connexe plus petit ne suffit, 133 sur 133, par énumération (partie A).

*Traduction.* Résidu : les relations contredites. Forme : `Hol`. Si `Hol` est trivial, l'objet manquant est un **attribut** (T2), unique à un choix global près, force (I) ; pour des signes, c'est le théorème d'équilibre de la réponse à la question 8. Sinon, **aucun attribut à valeurs dans `G` n'existe** (il n'en reste qu'un plus grossier, à valeurs dans le quotient de `G` par le sous-groupe normal qu'engendre `Hol`), et le plus petit revêtement qui garde toutes les relations est un **dédoublement** (T3) : chaque concept en `|Hol|` versions, le plan de recollement fixé à isomorphisme près. Le critère « scission d'une fausse identité » de la réponse à la question 6 (section 7), donné comme conjecturé, y gagne un énoncé.

*Limite, par contre-exemple.* Une seule relation fausse sur un cycle donne la même holonomie qu'un vrai dédoublement. La forme ne départage donc pas « quelques relations erronées » (T6) de « tout se dédouble » (T3) : c'est un choix de modèle (relations à retirer contre coût de description du dédoublement), donc l'affaire de la part compressible des anomalies (réponse à la question 8), non d'un théorème.

*Hypothèse qui tombe.* Si les types de relations ne se composent pas en groupe (« cause », « est un » n'ont pas d'inverse), (b) et (c) ne s'appliquent pas tels quels. Version sans inverse : non cherchée, question ouverte pour moi.

### Énoncé 3 — Monodromie : l'objet qui « déroule le tour » est l'orbite de l'anomalie

*Hypothèses.* `X` connexe par arcs, localement connexe par arcs, semi-localement simplement connexe ; `p : E → X` le revêtement des déterminations d'une grandeur ; `s` une détermination au-dessus de `x₀` ; `H` le stabilisateur de `s` pour l'action du groupe fondamental sur la fibre [1, p. 69]. *Énoncé.* (a) La composante `E_s` de `s` dans `E` est un revêtement connexe dont le sous-groupe associé est `H`. (b) Sur un revêtement connexe `q : (Y, y₀) → (X, x₀)`, la grandeur devient univaluée à partir de `s` si et seulement si `q_*π₁(Y, y₀) ⊂ H`, c'est-à-dire si `Y` se factorise par `E_s`. (c) `E_s` est déterminé à isomorphisme près par `H`, a `[π₁ : H]` feuillets et `N(H)/H` pour groupe de symétries. *Preuve.* (a) : l'image de `π₁(E_s, s)` est formée des lacets dont le relevé depuis `s` se referme [1, proposition 1.31, p. 61]. (b) : critère de relèvement [1, proposition 1.33, p. 61], appliqué à `q`. (c) : classification, nombre de feuillets et symétries [1, théorème 1.38, p. 67 ; proposition 1.32, p. 61 ; proposition 1.39, p. 71]. ∎

Force (I). Mais l'objet « prédit » n'est que l'anomalie suivie le long de tous les circuits : le groupe donne le plan du recollement, non la nature des feuillets. *Contre-exemple quand une hypothèse tombe* : sans l'hypothèse « semi-localement simplement connexe », le revêtement simplement connexe peut ne pas exister (bouquet de cercles de rayons décroissants) [1, p. 63].

### Énoncé 4 — Extensions : une composition « à un facteur près » prescrit un groupe plus gros

*Hypothèses.* Un groupe `Q` agit sur un groupe abélien `A`. Des opérations indexées par `Q` se composent à un élément de `A` près : `s(x)·s(y) = f(x, y)·s(xy)`. *Énoncé.* `f` est un 2-cocycle ; sa classe ne dépend pas du choix des `s(x)` ; les classes de `H²(Q, A)` correspondent aux classes d'isomorphisme d'extensions `1 → A → E → Q → 1` d'action donnée [2, chapitre II, exemple 1.18 (b), p. 65]. La classe est nulle si et seulement si l'on peut corriger les `s(x)` pour qu'ils composent exactement.

*Vérification par énumération* (partie B). Pour `Q` = groupe de Klein et `A` à deux éléments : 8 classes, qui donnent 4 groupes (abélien élémentaire, une fois ; produit des cycliques d'ordres 4 et 2, trois fois ; diédral d'ordre 8, trois fois ; quaternions, une fois). « Classe nulle si et seulement si une section exacte existe » : vrai dans les six cas énumérés. Les matrices de Pauli multipliées par `i` composent au signe près (6 produits sur 16 portent −1) ; ce résidu de signes définit le groupe des quaternions : en miniature, le « tour complet qui rend −1 » du spin.

Force (I) pour l'extension, mais deux limites. *Non-injectivité* : trois résidus distincts donnent le même groupe abstrait. *Dépendance au cadre* : avec `A` d'ordre 3, la même question n'a qu'une classe, nulle ; la forme n'existe que relativement au groupe d'ambiguïtés choisi. *Hypothèse qui tombe* : si `A` n'est pas abélien, cette classification ne tient plus telle quelle.

### Énoncé 5 — Galois : la forme prescrit un type négatif

*Énoncé cité.* En caractéristique nulle, une équation est résoluble par radicaux si et seulement si son groupe de Galois est résoluble [3, théorème 5.34, p. 77] ; les corps intermédiaires correspondent aux sous-groupes [3, théorème 3.17, p. 39] ; les facteurs simples d'une suite de composition ne dépendent pas de la suite [4, théorème 6.2, p. 88] ; le groupe alterné est simple à partir de cinq lettres [4, théorème 4.33, p. 69].

*Traduction.* Résidu : ce qui résiste aux radicaux. Forme : les facteurs simples. Chaque facteur cyclique d'ordre premier `p` prescrit l'adjonction d'une racine `p`-ième, les racines de l'unité étant présentes [3, proposition 5.27, p. 74]. Un facteur simple non abélien prescrit qu'**aucun** radical ne suffira : il faut un objet d'un autre genre, dont le théorème ne dit que les symétries. Force (II), et type négatif. *Limites.* Les facteurs ne déterminent pas le groupe (le groupe cyclique d'ordre 4 et le groupe de Klein ont les mêmes), d'où l'énoncé 4. *Hypothèse qui tombe* : en caractéristique `p`, `X^p − X − a` a un groupe abélien sans être résoluble par radicaux [3, remarque 3.29, p. 45].

### Énoncé 6 — Coïncidences entières : un caractère détermine un module, une dimension ne détermine rien

*Énoncé cité.* Sur les complexes, une représentation d'un groupe fini est déterminée à isomorphisme près par son caractère [5, corollaire 3.7, p. 35]. *Conséquences.* (a) Une suite de fonctions de classe à produits scalaires entiers positifs avec les caractères irréductibles détermine un module gradué, degré par degré. (b) Une suite de dimensions seule ne détermine rien : tout entier `n` est la dimension de `n` copies de la représentation triviale. Force (I) pour (a), (III) pour (b).

### Deux résultats de limite

**Limite 1 — Le champ extérieur ne fixe pas la source.** *Énoncé.* Soit `ρ₀` une densité à support dans une boule et `ψ` une fonction lisse à support dans cette boule. Les densités `ρ₀` et `ρ₀ + Δψ` ont le même potentiel newtonien hors de la boule. *Preuve.* Le potentiel est `Φ * ρ`, où `ΔΦ` est la masse de Dirac ; donc `Φ * Δψ = ψ`, nul hors de la boule. ∎ *Vérification* (partie C) : potentiel ajouté à l'extérieur au plus 1,3 × 10⁻⁵ de son échelle, égal à `ψ` à l'intérieur à 2 × 10⁻³ près. Force (II) : le résidu extérieur fixe le type (une masse), la masse totale et les moments harmoniques, non la répartition.

**Limite 2 — Un nombre ne départage pas ; une loi d'échelle départage.** *Hypothèses.* Orbite presque circulaire de rayon `a`, mouvement moyen `n`, accélération radiale perturbatrice `δf(r)` comptée vers l'extérieur. *Énoncé.* La précession vaut, au premier ordre, `(2δf(a)/a + δf′(a))/(2n)`. Pour `δf = ε·r^p` et un soleil de masse unité : `ε·(2+p)·a^(p+1/2)/2`. *Preuve.* Pour une attraction `g(r)`, la fréquence orbitale vérifie `Ω² = g/a` et la fréquence radiale `κ² = 3g/a + g′(a)` (linéarisation de `r̈ = h²/r³ − g(r)` autour du cercle) ; la précession est `Ω − κ`. ∎ *Conséquences.* (i) Sur un seul corps, toute famille munie d'une amplitude libre du bon signe s'ajuste exactement : objet et loi sont indiscernables. (ii) Sur plusieurs corps, la pente en `a` lit l'exposant `p`. (iii) La matière newtonienne, moyennée en anneau coplanaire, n'engendre que `p = −4, −6, …` (intérieure) ou `p = 1, 3, …` (extérieure) ; un autre exposant exclut le type « objet ». (iv) Pentes : −3,5 pour un quadrupôle intérieur, +1,5 pour un anneau extérieur, −1,5 pour une loi de puissance, −2,5 pour le terme relativiste, dont le coefficient dépend du moment cinétique de l'orbite (partie D). (v) `p = −2` est invisible : une masse centrale mal connue ne fait pas précesser.

## 3. Les pistes, jugées

|Piste|Théorème « forme → type » ?|Apport au graphe de domaine|Où la métaphore casse|
|---|---|---|---|
|Monodromie et revêtements|oui, force (I) (énoncés 2 et 3)|le plus fort : sépare, parmi les relations contredites (`κ`), celles qu'un attribut caché répare de celles qui exigent un dédoublement|il faut des types de relations composables en groupe ; une relation fausse imite un dédoublement ; l'objet prédit est un plan de recollement|
|Obstruction et cohomologie|oui : l'énoncé 2 est la cohomologie de degré un du graphe à coefficients dans `G` ; version linéaire : les sections globales sont la cohomologie de degré zéro d'un faisceau cellulaire, qu'un laplacien calcule [6, p. 2 et 7]|l'outil existe à grande échelle|la classe dépend du groupe de coefficients ; hors des groupes, l'obstruction cohomologique est suffisante mais non nécessaire [7, p. 1]|
|Galois et radicaux|oui dans son domaine, force (II), type négatif (énoncé 5)|l'idée d'une liste invariante de blocs irréductibles ; le reste est analogie|suppose un groupe qui permute des objets indiscernables, qu'un graphe empirique ne fournit pas|
|Extensions|oui, force (I) pour l'extension (énoncé 4)|faible dans un graphe empirique ; plausible dans le graphe méta-mathématique de la question 9|non-injectivité ; dépendance au groupe d'ambiguïtés|

Les quatre pistes disent une même chose : un résidu qui est un cocycle détermine l'objet qui le résout. Aucune ne couvre le cas (C4), qui relève de l'énoncé 1, plus pauvre.

**Lecture dans le cadre `φ`.** (C3) prédit une relation ; (C4), un objet du genre de ses voisins et son rôle (énoncés 1 et 1 bis) ; (C2), un attribut ou un dédoublement selon l'holonomie (énoncé 2). Aucun cas ne prédit une loi changée ni une erreur : ces deux types sortent du cadre de la correspondance, et c'est là que l'histoire trompe.

## 4. Les cas historiques, comme épreuves

|Cas|Forme disponible avant|Ce que la thèse en tire|Issue|
|---|---|---|---|
|Uranus (1846)|une fonction du temps sur plus d'un siècle : l'écart croît, décroît, s'annule presque vers 1830, puis grandit [8, p. 3]|famille des perturbations d'un corps extérieur : objet|objet, à 59 minutes d'arc de la longitude prédite (325°58′ contre 326°57′ [8, p. 5]) ; demi-grand axe prédit 36,15 unités astronomiques contre 30,11, masse 0,00011 masse solaire contre 0,0000515 [8, tableau 2, p. 14]|
|Mercure (1859-1915)|un nombre : 38,3 secondes d'arc par siècle chez Le Verrier [9, p. 1], 43 chez Newcomb [10, p. 49]|rien (limite 2)|planète ou anneau, quadrupôle solaire, loi de puissance d'exposant 2,00000016 [10, p. 49], tous écartés [11, p. 45] ; relativité générale|
|Cases vides (1871)|profil d'un nœud dans un tableau presque additif|objet du genre des voisins (énoncés 1 et 1 bis)|trois prédictions détaillées réussies, onze autres moins bien [12, notice] ; gaz nobles non prévus, aucun n'étant connu [13, p. 9]|
|Raies non attribuées|une raie|rien|hélium : élément, proposé en 1868, isolé en 1895 [13, p. 7-8] ; nébulium : oxygène et azote en états métastables, 1927-1928 ; coronium : fer très ionisé, 1942 [13, p. 10]|
|Spectre bêta continu|un spectre, plus les statistiques fausses de deux noyaux|une anomalie : rien ; deux qu'un même objet absorbe : objet|Bohr proposait une loi (énergie conservée en moyenne), Pauli une particule [14, p. 23-24] ; objet|
|Clair de lune monstrueux (1978-1992)|coïncidences sur trois coefficients, puis traces graduées|module gradué (énoncé 6)|module construit, conjecture démontrée [15, théorème 1.1]|
|Trois anomalies récentes|un nombre|rien|erreur : câble optique mal connecté, 73 nanosecondes [16, p. 18] ; recul thermique d'une sonde [17, p. 1] ; recalcul (réponse à la question 7)|

**Neptune.** Avant 1846, tout était proposé : erreurs des observations anciennes, choc d'une comète, milieu résistant, lune massive, gravitation changée à grande distance, planète [8, p. 3]. La forme a donné le type et la direction, non l'objet : la dégénérescence entre masse et distance (limite 1) a été levée par la règle de Titius-Bode [8, p. 12], fausse ici. Force (II).

**Mercure.** Le même raisonnement, sur un nombre, a donné Vulcain. La forme sur trois planètes tranche : les précessions mesurées, lues dans une source seconde [18, tableau 3, p. 15], donnent une somme des carrés des écarts réduits de 1,0 pour la loi relativiste sans paramètre libre, de 23,0 pour la loi de puissance et de 9,5 pour un quadrupôle intérieur, chacun avec un paramètre ajusté (partie E). Ces mesures sont postérieures ; ce que les données de 1895 permettaient reste à vérifier.

**Nébulium.** Ce qui a écarté le type « élément » n'est pas la raie mais une autre structure : le tableau périodique n'avait plus de case vide aux faibles masses [13, p. 9]. Pas de trou, pas d'objet.

**Spectre bêta.** Pauli relie deux anomalies par un seul objet, « sans renoncer au théorème de l'énergie » [14, p. 24] ; c'est la part compressible à l'œuvre. Mais son « neutron » tenait à la fois du neutron de Chadwick et du neutrino [14, p. 23] : à ma lecture, le type était juste et le nombre d'objets faux (un prédit, deux trouvés).

**Clair de lune monstrueux.** Nombres vérifiés : `196 884 = 196 883 + 1` [19, p. 1], `21 493 760 = 21 296 876 + 196 883 + 1` et `864 299 970 = 842 609 326 + 21 296 876 + 2·196 883 + 2·1` [19, p. 5] ; dimensions [19, p. 3] ; coefficients recalculés (partie F). Attributions : égalité de McKay [19, p. 1] ; traces graduées proposées par Thompson, conjecture de Conway et Norton [19, p. 6] ; module de Frenkel, Lepowsky et Meurman, démonstration de Borcherds pour ce module [15, théorème 1.1]. Trois nuances. (i) Les égalités de dimensions ne prescrivent rien seules (énoncé 6 b ; [19, p. 6]) ; leur poids vient de la parcimonie : avec des multiplicités de 0 à 2, les sommes possibles couvrent 2 × 10⁻⁵, 6 × 10⁻⁷ puis 5 × 10⁻⁸ des entiers de la plage, sous un nul uniforme grossier (partie F). (ii) Ce sont les traces sur toutes les classes qui déterminent le module gradué [19, p. 6]. (iii) Sa structure d'algèbre échappe à la forme : son unicité restait conjecturale en 2004 [19, p. 19] (état actuel à vérifier). En 1978 le groupe lui-même n'était que conjecturé ; il est construit en 1980 [19, p. 2].

**Bilan, sans valeur de preuve.** Les cas se rangent selon la richesse du résidu : forme riche (Uranus, cases vides, clair de lune), type bien prédit ; un nombre ou une raie (Mercure, nébulium, coronium, anomalies récentes), rien. Codage rétrospectif, d'un seul lecteur, sur des cas célèbres : il motive le test, sans le remplacer.

## 5. Un test daté de la thèse

**Volet 0 — monde planté, fait le 28 novembre 2026** (partie D ; critères écrits avant l'exécution). Des précessions sont engendrées soit par un objet (anneau intérieur ou extérieur), soit par une loi changée (loi de puissance, terme relativiste), sur `K` corps d'épreuve, avec bruit ; une règle de forme choisit la famille au meilleur ajustement pénalisé. Deux témoins faux devaient d'abord tomber au hasard : un seul corps (obtenu : 0,47 ; 0,49 ; 0,51) et le jumeau où objet et loi donnent presque la même pente (0,53, intervalle 0,49 à 0,57). Critère de mort : exactitude au plus 0,60 avec quatre corps et 5 % de bruit ; attendu : au moins 0,80. Obtenu : 0,997 ; avec deux corps, 0,92 ; avec quatre corps et 20 % de bruit, 0,94. *Lecture* : familles rivales connues et pentes distinctes, la forme prédit le type dès deux corps d'épreuve ; c'est le monde le plus favorable.

**Volet 1 — rétrodiction sur un corpus daté** (décrit, non lancé).
- *Unité* : une anomalie datée, tirée d'une source indépendante scellée avant tout codage (à choisir) ; au moins soixante, fermetures par remesure et recalcul comprises.
- *Forme*, codée sur les seuls textes antérieurs à la résolution, par une grille fixée (un nombre ; au moins trois corps d'épreuve ou trois relations ; structure de cycle ; trou de profil) ; deux lecteurs à l'aveugle, kappa de Cohen d'au moins 0,6. *Type*, codé à part sur l'issue.
- *Bases à battre* : taux de base des types ; modèle sur des traits sans forme (champ, âge, écart en unités d'incertitude).
- *Prédictions* (seuils à geler) : (P1) pour un résidu réduit à un nombre, la forme n'ajoute rien ; (P2) pour un résidu riche, gain d'exactitude équilibrée d'au moins 0,15, borne basse à 95 % au-dessus de 0.
- *Critère de mort* : borne haute du gain de (P2) sous 0,05. *Témoins faux* : issues permutées dans chaque champ (hasard exigé) ; si (P1) échoue, le codage a vu l'issue, épreuve nulle. *Dates* : corpus et grille scellés avant codage, lecture trois mois après.

**Volet 2 — prospectif.** Type prédit, scellé pour cinq anomalies ouvertes, lu le 31 décembre 2031. Candidates : l'alignement d'orbites lointaines de la ceinture de Kuiper, attribué à une planète (probabilité de hasard annoncée 0,007 %, au moins dix masses terrestres [20, p. 1]) ; les composantes sombres contre une gravité modifiée, que l'analogie de Neptune et de Vulcain sert déjà à discuter [21, p. 1 et 4]. Rien n'est scellé ici.

## 6. Ce que cette réponse ne permet pas de conclure

- Qu'une anomalie d'un domaine réel ait une forme au sens des énoncés 2 à 4 : ils exigent des transports en groupe ; rien n'est mesuré sur un graphe de domaine.
- Que la forme prédise le type en général : la limite 2 est un contre-exemple ; la sous-détermination est le cas ordinaire, les théorèmes décrivent des îlots.
- Que la forme départage l'objet de l'erreur : faux dès l'énoncé 2.
- Que le codage de la section 4 tienne à l'aveugle, ni que le monde planté vaille hors de familles rivales connues d'avance.

## 7. Antériorité (règle R8)

- **L'objet manquant d'une correspondance.** Le moteur d'appariement de structures de Falkenhainer, Forbus et Gentner introduit déjà dans la cible une « entité hypothétique » pour une entité de la base sans correspondant [23, p. 22 ; exemple p. 35]. Le cas (C4) est occupé depuis 1989.
- **Forme des dépendances et variable cachée.** Une variable latente unique impose des contraintes de tétrade sur les covariances, et la recherche de structure latente en part [24, p. 194 et 199] : un théorème « forme → type », occupé.
- **Nœuds manquants d'un réseau** : inférés avec les liens, leur nombre supposé connu [25, p. 3].
- **Sections qui ne se recollent pas, sur des données** : faisceaux et contextualité [26, p. 1-3 ; 7] ; laplacien de faisceau [6]. Les graphes à transports sont les graphes à gains et à tensions (Zaslavsky ; Gross : notices) : l'énoncé 2 n'est pas neuf en substance.
- **Philosophie.** La planète imaginaire de Lakatos (aucune anomalie ne force un type ; notice) ; Hanson sur Le Verrier (notice) ; Neptune et Vulcain appliqués à l'énergie sombre [21] ; Darden, la résolution d'anomalie comme diagnostic puis reconception d'un composant (notice) : voisin qualitatif le plus proche de « la forme oriente la réparation » ; cinq origines possibles d'un excès chez Hooper [27, p. 2].
- **Machines.** Tableau périodique réappris à partir de composés [28, p. 1] ; un banc de 2026 plante des mondes à particules cachées et à lois de force modifiées, où les meilleurs agents échouent sur les structures latentes [22, p. 1, 3 et 9] ; autre banc à grandeurs cachées [29, p. 1].
- **Non trouvé**, en quatre recherches : un corpus d'anomalies datées, codées par forme avant résolution et par type après, avec taux de base. Une question, non un trou établi.

## Nœuds pour Lazar

1. **Verser à la version 2 de la note** les énoncés 1, 1 bis et 2, et citer [23] pour le cas (C4). Recommandation : oui (confiance 0,8).
2. **Reformuler la thèse** : « la forme prédit le type quand le résidu a plus de dimensions que la famille rivale la moins contrainte ; un nombre ne prédit rien ». Recommandation : oui (0,8).
3. **Lancer le volet 1** : préenregistrement scellé, source indépendante, second lecteur d'une autre famille (dépense, donc devis). Recommandation : après la porte de sortie de la phase 0 ; variante sans dépense avec une grille codée par programme (0,6).
4. **Rejouer le volet 0 sur le banc publié [22]** (objet caché contre loi changée) plutôt que d'étendre le jouet, licence vérifiée d'abord. Recommandation : oui (0,6).
5. **Volet prospectif** : cinq prédictions scellées, lecture fin 2031 ; pièce décisive, à contre-lire. À ta main.

---

## Erreurs et glissements relevés dans les pistes

1. « Le groupe dit lequel » : c'est le stabilisateur de la détermination, à conjugaison près, qui classe le revêtement ; et l'objet « prédit » est l'orbite de l'anomalie elle-même (énoncé 3).
2. « 196 884 = 196 883 + 1 prescrivait la forme de l'objet » : les égalités de dimensions ne prescrivent rien seules ; ce sont les traces graduées de Thompson et la conjecture de Conway et Norton qui prescrivent, et seulement le module gradué, non sa structure d'algèbre.
3. « Démontré par Borcherds » : exact, pour le module de Frenkel, Lepowsky et Meurman [15, théorème 1.1].
4. « Neptune, un objet manquant » : type et direction justes, orbite et masse fausses (20 % et un facteur 2).
5. « Vulcain, une théorie manquante » : juste par l'issue ; la forme disponible, un nombre, ne le disait pas.
6. « Cases vides » : les succès détaillés sont trois ; les autres prédictions ont moins bien tenu [12, notice], et une colonne entière ne laisse pas de trou.
7. Détail : le théorème fondamental de la théorie de Galois porte le numéro 3.17 dans la version 5.10 du cours de Milne.

## Références

État : **L** = passage cité lu à la page indiquée, dans le texte extrait du fichier téléchargé (aucun de ces documents n'a été lu en entier ; les pages sont celles du fichier) ; **N** = notice ou résumé seulement ; **V** = à vérifier.

1. A. Hatcher, *Algebraic Topology*, 2002, p. 61, 63, 66-71. **L**
2. J. S. Milne, *Class Field Theory*, version 4.03, p. 65. **L**
3. J. S. Milne, *Fields and Galois Theory*, version 5.10, 2022, p. 39, 45, 74, 77. **L**
4. J. S. Milne, *Group Theory*, version 4.01, p. 52, 69, 88. **L**
5. P. Etingof et collègues, *Introduction to representation theory*, arXiv:0901.0827, p. 35. **L**
6. J. Hansen, R. Ghrist, « Toward a spectral theory of cellular sheaves », arXiv:1808.01513, p. 2, 6-7. **L**
7. S. Abramsky, S. Mansfield, R. S. Barbosa, « The cohomology of non-locality and contextuality », arXiv:1111.3620, p. 1-2, 5. **L**
8. D. Krajnović, « The contrivance of Neptune », arXiv:1610.06424, p. 3, 5, 9, 12, 14. **L** (source seconde pour les éléments de Le Verrier et d'Adams, tirés de Grosser 1962)
9. D. R. Constantin, « On the first determination of Mercury's perihelion advance », arXiv:1104.0548, p. 1. **L** (source seconde pour Le Verrier 1859)
10. A. Hall, « A suggestion in the theory of Mercury », *Astronomical Journal* 14, 49 (1894). **L** (fac-similé, reconnaissance de caractères)
11. C. M. Will, « The confrontation between general relativity and experiment », arXiv:1403.7377, p. 45. **L**
12. P. J. Stewart, « Mendeleev's predictions: success and failure », *Foundations of Chemistry* 21, 3-9 (2019). **N** (résumé de recherche ; accès refusé) ; décompte à vérifier, ainsi que celui de Scerri. **V**
13. W. T. Bridgman, « The cosmos in your pocket », arXiv:0710.0671, p. 7-10. **L** (source de vulgarisation savante ; dates à recouper)
14. L. M. Brown, « The idea of the neutrino », *Physics Today* 31 (9), 23 (1978), copie d'un dépôt universitaire. **L** (reconnaissance de caractères imparfaite) ; lettre de Pauli du 4 décembre 1930 non lue directement. **V**
15. R. E. Borcherds, « Monstrous moonshine and monstrous Lie superalgebras », *Inventiones Mathematicae* 109, 405-444 (1992), prépublication de l'auteur, p. 1-2. **L**
16. Collaboration OPERA, arXiv:1109.4897 (version 4), résumé, p. 16, 18. **L**
17. S. G. Turyshev et collègues, « Support for the thermal origin of the Pioneer anomaly », arXiv:1204.2507, p. 1. **L**
18. B. Berche, E. Medina, « The advance of Mercury's perihelion », arXiv:2402.04643, p. 9, 15. **L** (les mesures du tableau 3 y sont reprises d'une autre source : seconde main. **V**)
19. T. Gannon, « Monstrous Moonshine: the first twenty-five years », arXiv:math/0402345, p. 1-3, 5-6, 10, 19. **L** (attribution à Thompson de la deuxième égalité : non établie par cette source ; note de Thompson 1979 et article de Conway et Norton 1979 non lus. **V**)
20. K. Batygin, M. E. Brown, « Evidence for a distant giant planet in the solar system », arXiv:1601.05438, p. 1, 3. **L**
21. O. Lahav, M. Massimi, « Dark energy, paradigm shifts, and the role of evidence », arXiv:1405.1350, p. 1, 4. **L**
22. M. L. Wiemann et collègues, « DiscoverPhysics », arXiv:2605.26087 (version 2), p. 1-5, 9, 17. **L** ; licence non vérifiée. **V**
23. B. Falkenhainer, K. D. Forbus, D. Gentner, « The structure-mapping engine », *Artificial Intelligence* 41, 1-63 (1989), p. 22-23, 35. **L**
24. R. Silva, R. Scheines, C. Glymour, P. Spirtes, « Learning the structure of linear latent variable models », *Journal of Machine Learning Research* 7, 191-246 (2006), p. 194, 199. **L**
25. M. Kim, J. Leskovec, « The network completion problem », 2011, p. 1, 3. **L**
26. S. Abramsky, A. Brandenburger, « The sheaf-theoretic structure of non-locality and contextuality », arXiv:1102.0264, p. 1-3. **L**
27. D. Hooper, « What makes a discovery? », arXiv:2312.00672, p. 2. **L**
28. Q. Zhou et collègues, « Atom2Vec », arXiv:1807.05617, p. 1. **L** (résumé)
29. E. Ji, W. Wang, Y. Sun, « Unsatz », arXiv:2611.03713 (version 2), p. 1. **L** (résumé)

Citées sans lecture (**N**, toutes **V**) : I. Lakatos, « Falsification and the methodology of scientific research programmes » (1970) ; N. R. Hanson, *Isis* 53, 359-378 (1962) ; L. Darden, « Strategies for anomaly resolution » (1992, p. 251-273) ; T. Zaslavsky, « Biased graphs. I » (1989) ; J. L. Gross, « Voltage graphs » (1974) ; J. G. Thompson (1979) ; J. H. Conway, S. P. Norton (1979) ; I. Frenkel, J. Lepowsky, A. Meurman (1984, 1988) ; Y. Pu et collègues, arXiv:2602.06448 (résumé lu, non employé). Valeurs usuelles non revérifiées sur source, employées dans la partie E du script : demi-grands axes, excentricités et périodes de Mercure, Vénus et la Terre ; constante gravitationnelle héliocentrique ; unité astronomique. **V**

## Annexe — Fichiers téléchargés

Dossier `/tmp/claude-0/-home-user-controle-ia-travail/72cb7e89-3107-5c40-8de3-bdb9cf3a5211/scratchpad/pdf-q10/` ; empreintes sha256 abrégées.

|Fichier|Empreinte|Référence|
|---|---|---|
|`hatcher-algebraic-topology.pdf`|`bebb3032bf9021b9…`|1|
|`milne-class-field-theory.pdf`|`50d79af78250a9f1…`|2|
|`milne-fields-and-galois-theory.pdf`|`5c43ea0bf4ec190b…`|3|
|`milne-group-theory.pdf`|`826a86c9faebaa3a…`|4|
|`etingof-introduction-representation-theory-arxiv-0901.0827.pdf`|`30325e113dcd5d9d…`|5|
|`hansen-ghrist-2019-spectral-theory-cellular-sheaves-arxiv-1808.01513.pdf`|`4185dec93ca1eba5…`|6|
|`abramsky-mansfield-barbosa-2011-cohomology-contextuality-arxiv-1111.3620.pdf`|`c096b58eb49350ba…`|7|
|`krajnovic-2016-contrivance-of-neptune-arxiv-1610.06424.pdf`|`0b07a6c4fc01d085…`|8|
|`constantin-2011-first-determination-mercury-perihelion-arxiv-1104.0548.pdf`|`366c80d99601a9fc…`|9|
|`hall-1894-suggestion-theory-of-mercury-aj14-49.pdf`|`60b5938d914c55ef…`|10|
|`will-2014-confrontation-general-relativity-experiment-arxiv-1403.7377.pdf`|`87b6db17dcc30642…`|11|
|`bridgman-2007-cosmos-in-your-pocket-arxiv-0710.0671.pdf`|`2f5df78b34e313c0…`|13|
|`brown-1978-idea-of-the-neutrino-physics-today-copie-uab.pdf`|`842d5824675a0fe9…`|14|
|`borcherds-1992-monstrous-moonshine-lie-superalgebras.pdf`|`dee2cb9c3121cf1b…`|15|
|`opera-2012-neutrino-velocity-arxiv-1109.4897.pdf`|`69a5560d00e22b61…`|16|
|`turyshev-2012-pioneer-anomaly-thermal-arxiv-1204.2507.pdf`|`98359d64c5bab282…`|17|
|`berche-medina-2024-advance-of-mercury-perihelion-arxiv-2402.04643.pdf`|`84eaf50541ed720c…`|18|
|`gannon-2004-monstrous-moonshine-first-25-years-arxiv-math0402345.pdf`|`c416209187b2c911…`|19|
|`batygin-brown-2016-distant-giant-planet-arxiv-1601.05438.pdf`|`23c08971aa86ee16…`|20|
|`lahav-massimi-2014-dark-energy-paradigm-shifts-arxiv-1405.1350.pdf`|`be2e7467dffa0114…`|21|
|`2026-discoverphysics-benchmark-arxiv-2605.26087.pdf`|`08a978b3e24e8059…`|22|
|`falkenhainer-forbus-gentner-1989-structure-mapping-engine.pdf`|`e2c19224adf01f29…`|23|
|`silva-2006-learning-structure-linear-latent-variable-models-jmlr.pdf`|`3c6ad24eda9404ec…`|24|
|`kim-leskovec-2011-network-completion-problem-sdm.pdf`|`b5d3a3c9f6a4d31f…`|25|
|`abramsky-brandenburger-2011-sheaf-contextuality-arxiv-1102.0264.pdf`|`a06560481dd4dfdd…`|26|
|`hooper-2023-what-makes-a-discovery-arxiv-2312.00672.pdf`|`4b95349613d0c8f2…`|27|
|`zhou-2018-atom2vec-learning-atoms-arxiv-1807.05617.pdf`|`1481107e2589024b…`|28|
|`2026-unsatz-discovery-without-ansatz-arxiv-2611.03713.pdf`|`f123b33714b61d99…`|29|
|`2026-pievo-principle-evolvable-discovery-arxiv-2602.06448.pdf`|`05db18f9e33f3d43…`|résumé seul|
|`empirical-foundations-relativistic-gravity-arxiv-gr-qc0504116.pdf`|`79de6b10cc7d8100…`|téléchargé, non employé|

Incidents de collecte, à connaître : deux identifiants devinés de mémoire ont mené à des articles sans rapport (supprimés ; les bons fichiers ont été retrouvés par recherche) ; les sites de deux éditeurs ont refusé l'accès (références 12 et notices) ; je n'ai pas insisté.
