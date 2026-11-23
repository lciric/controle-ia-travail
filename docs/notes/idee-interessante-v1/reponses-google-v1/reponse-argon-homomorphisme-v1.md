### Thèse liminaire : rejet partiel et remplacement de la proposition

La proposition selon laquelle une analogie scientifique se réduit à un **homomorphisme de graphes typés** ou à une **équivariance d’opérateurs discrets** doit être **rejetée sous sa forme stricte**, puis **remplacée**. 

1. **Pourquoi l'homomorphisme de graphes échoue :** Un homomorphisme de graphes envoie une arête sur une arête. Or, une analogie scientifique relie fréquemment une relation élémentaire d'un domaine $A$ à une *chaîne composée* d'opérations dans un domaine $B$ (changement de granularité). Sans opération de composition et sans équations de commutativité (équivalence de chemins), un graphe ne distingue pas une déduction valide d'une boucle causale incohérente.
2. **Pourquoi l'équivariance stricte échoue :** Les réseaux conceptuels de deux disciplines éloignées ne partagent presque jamais le même groupe de symétrie global avant la découverte ; leurs symétries sont locales, partielles et brisées par les conditions aux limites propres à chaque domaine.
3. **Par quoi la remplacer :** L'objet mathématique minimal qui capture l'invariance analogique est un **span (ou cospan) de foncteurs partiels entre catégories de schémas** (au sens des *ologs* de Spivak & Kent, 2012, où les chemins commutatifs encodent les lois), muni d'une **relaxation métrique asymétrique** (transport optimal de Gromov-Wasserstein orienté) pour absorber l'alignement imparfait des vocabulaires et des résolutions.

---

### 1. Objets : définitions formelles et mise à l'épreuve

#### Définitions des candidats

*   **Graphe étiqueté et graphe typé :** Soit un graphe orienté $G = (V, E, s, t)$ où $s, t : E \to V$ sont les applications source et cible. Un graphe est *étiqueté* s'il est muni d'applications $\ell_V : V \to \Sigma_V$ et $\ell_E : E \to \Sigma_E$ vers des alphabets fixes. Un graphe est *typé* (Corradini et al., 1997) s'il est muni d'un graphe de types $T$ et d'un homomorphisme de graphes $\tau : G \to T$.
*   **Homomorphisme, homomorphisme partiel, isomorphisme de sous-graphe :** Un homomorphisme $f : G \to G'$ est un couple $(f_V : V \to V', f_E : E \to E')$ tel que $s' \circ f_E = f_V \circ s$ et $t' \circ f_E = f_V \circ t$ (et $\tau' \circ f = \tau$ dans le cas typé). Il est *partiel* s'il est défini sur un sous-graphe $G_0 \subseteq G$. C'est un *isomorphisme de sous-graphe* si $f_V$ et $f_E$ sont injectifs (plongement exact de $G$ dans $G'$).
*   **Foncteur entre catégories :** Une catégorie $\mathcal{C}$ ajoute à un graphe orienté une loi de composition associative des chemins ($g \circ f$) et des morphismes identités ($1_X$), ainsi que des relations d'équivalence entre chemins (diagrammes commutatifs). Un foncteur $F : \mathcal{C} \to \mathcal{D}$ envoie objets sur objets et morphismes sur morphismes en conservant les identités et la composition : $F(g \circ f) = F(g) \circ F(f)$. Contrairement à l'homomorphisme de graphes, un foncteur peut envoyer une flèche atomique $f$ de $\mathcal{C}$ sur un chemin composé $h_k \circ \dots \circ h_1$ de $\mathcal{D}$.
*   **Équivariance sous un groupe ou un groupoïde :** Soit $G$ un groupe agissant sur deux espaces $X$ et $Y$. Un opérateur $\Phi : X \to Y$ est équivariant si $\Phi(g \cdot x) = g \cdot \Phi(x)$ pour tout $g \in G$. Si l'action n'est définie que localement (symétries partielles dépendant de l'état), $G$ est remplacé par un *groupoïde* $\mathcal{G}$ (catégorie dont tous les morphismes sont inversibles), et l'équivariance n'est imposée que là où la composition dans $\mathcal{G}$ est définie.

#### Évaluation sur les trois exemples

| Exemple | Ce que capturent les candidats | Ce qu'ils manquent (et quel objet résout le défaut) |
| :--- | :--- | :--- |
| **1. Gravitation terrestre et céleste (Newton)** | **Graphe typé / Homomorphisme :** Capture la fusion ontologique consistant à envoyer les nœuds « Pomme » et « Lune » sur un même type $T_{\text{corps}}$ soumis à une arête « attire ». <br>**Équivariance :** Capture l'invariance de la loi sous le groupe de Galilée (changement de référentiel entre la surface terrestre et le repère héliocentrique). | Un homomorphisme de graphes ne peut pas exprimer que la *force* est égale à la *dérivée seconde* de la position. Il manque la structure opérationnelle : l'identification entre l'accélération de la pesanteur $g$ et l'accélération centripète $v^2/r$ exige un **foncteur** qui conserve les diagrammes commutatifs du calcul différentiel. |
| **2. Écoulements de fluides et horizon de trou noir (Unruh, 1981)** | **Isomorphisme de sous-graphe :** Capture la correspondance exacte, terme à terme, entre les variables de l'équation d'onde d'une perturbation acoustique linéaire dans un fluide irrotationnel barotrope et celles d'un champ scalaire sans masse dans une métrique courbe (métrique acoustique de Painlevé-Gullstrand). | L'homomorphisme global échoue : les équations de Navier-Stokes ne sont pas isomorphes aux équations d'Einstein. Il s'agit d'un **span de foncteurs** $\mathcal{C}_{\text{fluide}} \leftarrow \mathcal{C}_{\text{cinématique}} \rightarrow \mathcal{C}_{\text{RG}}$ : seule la sous-catégorie cinématique de propagation des modes (et la condition de franchissement $v > c_{\text{son}} \leftrightarrow r < r_{\text{horizon}}$) est préservée, tandis que la dynamique engendrant la métrique est rejetée hors du domaine du foncteur. |
| **3. Douleur sous anesthésie $\leftrightarrow$ États internes d'un LLM** | **Homomorphisme partiel :** Permet de projeter la dissociation entre « activation nociceptive sous-corticale / autonome » et « absence de rapport verbal conscient » sur la dissociation entre « représentation interne dans le flux résiduel (*residual stream*) » et « sortie bloquée par le réglage fin (RLHF) ». | Les types ontologiques sont incommensurables (biologie vs algèbre linéaire) : un graphe typé échoue si $T$ est fixe. Ce qui définit l'analogie ici est l'**équivariance sous un groupoïde d'interventions causales** (au sens des opérations $\text{do}(x)$ de Pearl ou d'*activation patching*) : l'opération « administrer un analgésique / ablater le noyau spécifique » commute avec la projection vers l'état interne, alors que l'opération « bloquer l'effecteur moteur / filtrer le *token* de sortie » laisse l'état latent invariant. |

---

### 2. Alignement imparfait : mesures, complexité et échecs

Lorsque deux réseaux $G_1$ et $G_2$ sont extraits de corpus aux vocabulaires disjoints ($\Sigma_1 \cap \Sigma_2 = \emptyset$), l'alignement ne peut reposer sur les étiquettes.

#### 1. Distance d'édition de graphes (*Graph Edit Distance*, GED)
*   **Définition et conservation :** Nombre minimal d'opérations élémentaires (insertion, suppression, substitution de nœuds et d'arêtes), pondérées par coût, pour transformer $G_1$ en $G_2$ (Sanfeliu & Fu, 1983). Conserve la topologie locale exacte à un bruit additif près.
*   **Coût de calcul :** NP-difficile dans le cas général (Zeng et al., 2009). Les solveurs exacts (A*) sont impraticables au-delà de quelques dizaines de nœuds sans heuristiques agressives.
*   **Échecs connus :** Très sensible aux différences de densité et de résolution. Si une relation causale directe $A \to B$ dans $G_1$ est détaillée en $A \to X \to Y \to B$ dans $G_2$, la GED pénalise lourdement l'ajout des nœuds intermédiaires alors que l'analogie fonctionnelle est parfaite.

#### 2. Moteur d'appariement de structures (*Structure-Mapping Engine*, SME)
*   **Définition et conservation :** Algorithme fondé sur la théorie de Gentner (1983) et implémenté par Falkenhainer, Forbus et Gentner (1989). Il construit des hypothèses de correspondance locales entre prédicats, puis les fusionne en maximisant un score de *systématicité* qui privilégie les relations d'ordre supérieur (par ex. `CAUSE(PLUS_GRAND(x,y), MOUVEMENT(y))`) au détriment des attributs isolés.
*   **Coût de calcul :** Polynomial en pratique grâce à des règles d'élagage gloutonnes sur des arbres de prédicats bornés, bien que le sous-problème de clique maximale sous-jacent soit NP-difficile en théorie.
*   **Échecs connus :** Dépendance critique à la représentation d'entrée (*hand-coding bottleneck*, Chalmers, French & Hofstadter, 1992). Si deux domaines n'utilisent pas les mêmes symboles de connecteurs logiques d'ordre supérieur en entrée, SME ne trouve aucun point d'ancrage.

#### 3. Homomorphismes approchés ou gradués
*   **Définition et conservation :** Relaxation de la condition d'adjacence en minimisant la distorsion $\sum_{(u,v) \in E_1} (1 - A_2(f(u), f(v)))$ ou via les densités d'homomorphismes de petits motifs $F$ dans $G_1$ et $G_2$ (théorie des *graphons*, Lovász, 2012). Conserve la distribution statistique des motifs locaux (triangles, étoiles, cycles).
*   **Coût de calcul :** Le comptage exact de motifs de taille $k$ coûte $O(|V|^k)$ dans le pire cas ; la relaxation continue par programmation semi-définie ou spectrale est polynomiale.
*   **Échecs connus :** Deux graphes peuvent avoir des densités de motifs locaux proches (co-spectralité ou proximité en norme de coupe) tout en ayant des chemins globaux de déduction incompatibles.

#### 4. Transport optimal de Gromov-Wasserstein (GW)
*   **Définition et conservation :** On représente chaque graphe comme un espace métrique mesuré $(V_i, d_i, \mu_i)$, où $d_i$ est une matrice de distances ou de similarités asymétriques (plus court chemin orienté, noyau de diffusion de la chaleur) et $\mu_i$ une mesure de probabilité sur les nœuds. La distance de Gromov-Wasserstein (Mémoli, 2011) cherche un couplage probabiliste $\pi \in \Pi(\mu_1, \mu_2)$ minimisant :
    $$\text{GW}_p^p(G_1, G_2) = \min_{\pi \in \Pi(\mu_1, \mu_2)} \sum_{u,u' \in V_1} \sum_{v,v' \in V_2} |d_1(u,u') - d_2(v,v')|^p \pi(u,v)\pi(u',v')$$
    Elle conserve la **géométrie relationnelle globale** à une isométrie près, sans jamais comparer directement un nœud de $G_1$ à un nœud de $G_2$ dans un espace ambiant commun. En remplaçant $d_i$ par la matrice des plus courts chemins, GW gère naturellement le changement de granularité (un chemin de longueur $L$ s'aligne sur une distance proportionnelle).
*   **Coût de calcul :** Problème quadratique non convexe. Avec régularisation entropique, chaque itération de descente par projections de Sinkhorn s'exécute en $O(|V|^3)$ opérations matricielles lorsque les coûts sont décomposables (Peyré, Cuturi & Solomon, 2016).
*   **Échecs connus :** Si $d_i$ est symétrique, GW est invariant par réflexion : il peut inverser le sens de la causalité (envoyer les causes sur les effets si le graphe est symétrique par renversement des flèches). Il faut impérativement utiliser une variante asymétrique (matrices de coûts orientées $C_i(u,u') \neq C_i(u',u)$) et le problème souffre de minima locaux.

---

### 3. Symétrie et conservation : y a-t-il un théorème de Noether discret ?

#### Les analogues discrets
*   **Groupe d'automorphismes $\text{Aut}(G)$ :** Ensemble des permutations de $V$ préservant l'adjacence (et les types). C'est la symétrie globale d'un réseau fixe.
*   **Groupoïde de symétries :** Ensemble des isomorphismes entre sous-graphes locaux $U \cong U'$ de $G$. Il capture la répétition d'un même mécanisme explicatif à différents endroits d'une théorie.
*   **Invariants de graphes :** Grandeurs inchangées sous $\text{Aut}(G)$ (spectre du laplacien, polynôme de Tutte, homologie persistante du complexe de cliques).
*   **Naturalité catégorielle :** Soient deux foncteurs $F, H : \mathcal{C} \to \mathcal{D}$ représentant deux modélisations d'un domaine $\mathcal{C}$ dans un domaine $\mathcal{D}$. Une transformation naturelle $\eta : F \Rightarrow H$ est une famille de morphismes $\eta_X : F(X) \to H(X)$ telle que pour toute flèche $f : X \to Y$ dans $\mathcal{C}$, le carré $\eta_Y \circ F(f) = H(f) \circ \eta_X$ commute. C'est la définition exacte de l'invariance d'une traduction vis-à-vis des déductions internes.

#### Énoncé de type Noether : le démontré contre le spéculatif

*   **Ce qui est démontré (en dynamique discrète sur graphe) :**
    1. *Mécanique discrète variationnelle :* Lorsqu'un système discret possède un lagrangien discret $L_d(q_k, q_{k+1})$ défini sur les arêtes d'un graphe temporel, toute symétrie continue à un paramètre du lagrangien discret engendre une quantité exactement conservée le long de la trajectoire discrète (théorème de Noether discret ; Marsden & West, 2001).
    2. *Processus de Markov sur graphes :* Pour une équation maîtresse (dynamique linéaire de probabilité $\frac{dp}{dt} = H p$ sur un graphe fini), Baez et Fong (2013) ont démontré un analogue exact du théorème de Noether : un opérateur $O$ commute avec le générateur infinitésimal $H$ ($[O, H] = 0$, symétrie de la dynamique) si et seulement si l'espérance de $O$ (et de $O^2$) est conservée au cours de l'évolution pour toute distribution initiale.
    3. *Conservation spectrale :* Si un graphe possède un groupe d'automorphismes non trivial $\text{Aut}(G)$, l'opérateur de diffusion (laplacien du graphe $L$) commute avec les matrices de permutation $P_g$ ($g \in \text{Aut}(G)$). Cela scinde l'espace d'états en sous-espaces invariants (représentations irréductibles de $\text{Aut}(G)$) au sein desquels la masse diffusée est piégée ou dégénérée.

*   **Ce qui est spéculatif (et faux sans structure supplémentaire) :**
    Appliquer directement le théorème de Noether à un **réseau statique de concepts scientifiques** est une erreur de catégorie mathématique. Le théorème de Noether classique exige un groupe de Lie *continu* agissant sur une fonctionnelle d'action, et le théorème de Baez-Fong exige un générateur dynamique $H$ décrivant un flux sur le graphe. Un réseau de concepts statique n'a ni lagrangien canonique, ni équation maîtresse intrinsèque. 
    
    *Le substitut rigoureux :* Dans un réseau de concepts formalisé comme une catégorie $\mathcal{C}$, ce qui joue le rôle d'« équation du mouvement », c'est l'**ensemble des relations d'équivalence de chemins** (les diagrammes commutatifs $\gamma_1 \sim \gamma_2$ qui expriment les lois du domaine). La « quantité conservée » par un foncteur d'analogie $F : \mathcal{C} \to \mathcal{D}$ n'est pas un scalaire énergétique, mais l'**homologie du nerf de la catégorie** (ou la commutativité des cycles) : si deux chaînes causales $\gamma_1$ et $\gamma_2$ aboutissent à la même conséquence dans $\mathcal{C}$ ($\gamma_1 = \gamma_2$), alors leurs images doivent aboutir à la même conséquence dans $\mathcal{D}$ ($F(\gamma_1) = F(\gamma_2)$).

---

### 4. Avant la découverte : détection précoce et risques de circularité

L'hypothèse à tester est la suivante : une découverte inter-domaines à la date $t^*$ est précédée, à une date $t_0 < t^*$, par un **changement de représentation** dans l'un des domaines (introduction d'un nouveau formalisme, d'un instrument ou d'une réduction d'échelle) qui rapproche brusquement la géométrie relationnelle de son réseau conceptuel $G_A(t)$ de celle de $G_B(t)$, avant que quiconque n'ait publié de terme de liaison entre $A$ et $B$.

#### Données datées et construction des graphes
1.  **Corpus strictement filtré :** Deux sous-corpus disjoints $\mathcal{D}_A(\le t)$ et $\mathcal{D}_B(\le t)$ extraits d'archives horodatées (par ex. *Physical Review* / *arXiv* / *PubMed*), en excluant tout article citant simultanément des journaux de $A$ et de $B$ avant $t^*$.
2.  **Extraction de graphes orientés sans fuite sémantique :** Les nœuds sont les entités ou variables physiques/biologiques ; les arêtes orientées sont les dépendances fonctionnelles ou causales (extraites soit par analyse syntaxique de dépendances sur le texte et les équations — où une équation $y = f(x, z)$ crée les arêtes $x \to y$ et $z \to y$ — soit par un extracteur figé).

#### Calcul de la divergence structurelle
À chaque pas de temps discret $t \in \{t_1, \dots, t^* - 1\}$, on calcule sur chaque graphe $G_i(t)$ la matrice de transition asymétrique de marche aléatoire régularisée (ou la matrice des plus courts chemins orientés tronqués) $C_i(t)$. On évalue la divergence de Gromov-Wasserstein purement structurelle (sans utiliser d'étiquettes textuelles sur les nœuds) :
$$\Delta(t) = \text{GW}_2\big(C_A(t), \mu_A(t) \;;\; C_B(t), \mu_B(t)\big)$$
Le signal de pré-découverte est une **rupture de pente négative** significative $\frac{d\Delta}{dt} \ll 0$ à un instant $t_{\text{rep}} < t^*$, coïncidant avec l'adoption d'une nouvelle représentation dans $A$ ou $B$, suivie d'une concentration de la matrice de couplage optimal $\pi^*(t)$ (baisse de l'entropie de Shannon $H(\pi^*)$).

#### Trois risques majeurs de circularité (et comment les éliminer)
1.  **Contamination anachronique par le modèle d'extraction :** Si l'on utilise un grand modèle de langage (LLM) entraîné sur des textes postérieurs à $t^*$ pour extraire les graphes $G_A(t)$ et $G_B(t)$, le modèle projettera sa connaissance future de l'analogie dans la manière même dont il segmente les concepts à la date $t$. *Remède :* Utiliser uniquement un analyseur syntaxique déterministe (type Universal Dependencies + parseur d'arbres syntaxiques d'équations LaTeX/MathML) ou un modèle de langue pré-entraîné exclusivement sur des textes antérieurs à $t$.
2.  **Contamination lexicale diffuse :** Avant l'article fondateur à $t^*$, des auteurs peuvent emprunter informellement des métaphores du domaine cible. Si la métrique d'alignement utilise des plongements lexicaux (*word embeddings*, comme dans *Fused Gromov-Wasserstein*), la baisse de $\Delta(t)$ ne mesurera qu'un rapprochement de vocabulaire, non une invariance mathématique. *Remède :* Interdire toute information lexicale dans le calcul de $\text{GW}_2$ (les nœuds sont anonymisés en indices $\{1, \dots, n\}$ ; seule la matrice d'adjacence orientée $A(t)$ est fournie à l'algorithme).
3.  **Biais de sélection de sous-graphes (*cherry-picking* rétrospectif) :** Construire $G_A(t)$ en ne sélectionnant que les articles qui mèneront à la découverte à $t^*$. *Remède :* Définir $G_A(t)$ et $G_B(t)$ à partir des $K$ articles les plus cités à l'instant $t$ au sein des codes de classification standards des deux sous-disciplines (par ex. codes PACS ou MeSH existant à la date $t$).

---

### 5. Expérience minimale : protocole falsifiable

Testons l'alignement structurel avant l'article d'Unruh (1981) reliant l'acoustique des fluides en mouvement et l'évaporation des trous noirs (rayonnement de Hawking).

*   **Changement de représentation historique testé :** Entre 1973 et 1976, la physique des trous noirs passe d'une représentation purement géométrique/classique (solutions des équations d'Einstein) à une représentation en termes de **propagation de modes de champs quantiques et de transformations de Bogoliubov** au voisinage d'un horizon (Hawking, 1974, 1975). De son côté, l'acoustique des milieux inhomogènes en écoulement utilise déjà la théorie du potentiel de vitesse et des rayons acoustiques dans un écoulement de fond (Blokhintsev, 1946 ; Pierce, 1974 - *à vérifier pour la date exacte de la formulation variationnelle de Pierce*).
*   **Données :** Corpus *Physical Review* (APS Data Set for Research), strictement découpé par année de 1965 à 1980 (avant la soumission d'Unruh en décembre 1980 / publication en mai 1981).
    *   *Domaine A (Relativité générale / Trous noirs) :* Articles contenant `"black hole"` ou `"event horizon"` ou `"Schwarzschild"`.
    *   *Domaine B (Acoustique des fluides en écoulement) :* Articles contenant (`"acoustic"` ou `"sound wave"`) et (`"inhomogeneous medium"` ou `"moving medium"` ou `"potential flow"`), en excluant tout article mentionnant `"relativity"`, `"gravity"`, `"black hole"`, `"Hawking"`.
    *   *Construction du graphe annuel $G_i(t)$ :* Pour chaque domaine et chaque fenêtre glissante de 3 ans $[t-2, t]$, extraction du graphe de co-dépendance des variables dans les équations et des prédicats physiques (nœuds = symboles mathématiques normalisés par leur rôle différentiel — ex. opérateur d'Alembertien, gradient de vitesse, potentiel scalaire, fréquence, température — et concepts associés ; arêtes orientées $u \to v$ si $u$ apparaît dans l'opérateur différentiel gouvernant $v$ ou implique $v$ dans le texte). Anonymisation totale des étiquettes des $N=100$ nœuds les plus centraux (centralité de PageRank) de chaque graphe.
*   **Algorithme :**
    1. Calcul de la matrice de distances orientées régularisées $C_i(t) = \exp(\beta A_i(t))$ (noyau de communicabilité orientée) pour $i \in \{A, B\}$.
    2. Résolution du problème de Gromov-Wasserstein entropique asymétrique (Peyré et al., 2016) entre $(C_A(t), \mu_{\text{unif}})$ et $(C_B(t), \mu_{\text{unif}})$, donnant la distance $\Delta_{AB}(t)$ et la matrice de transport optimal $\pi^*(t)$.
    3. Génération de deux contrôles négatifs : (i) $N_{\text{perm}} = 1\,000$ graphes aléatoires préservant exactement la séquence des degrés entrants et sortants de $G_B(t)$ (modèle de configuration orienté) ; (ii) un domaine contrôle $C$ de taille comparable (par ex. physique des semi-conducteurs cristallins, $G_C(t)$).
*   **Prédiction :**
    1. La distance normalisée $Z_{AB}(t) = \frac{\Delta_{AB}(t) - \mathbb{E}[\Delta_{\text{perm}}(t)]}{\sigma(\Delta_{\text{perm}}(t))}$ subit une chute statistiquement significative entre la période pré-Hawking (1965–1973) et la période post-Hawking (1975–1980).
    2. Sur la fenêtre 1976–1980, le couplage optimal $\pi^*(t)$ aligne (dans son top-3 de probabilité marginale) le nœud correspondant à la « vitesse d'écoulement du fluide » avec la « coordonnée radiale / décalage vers le rouge gravitationnel », et la « vitesse du son » avec la « vitesse de la lumière / horizon ».
*   **Seuil de succès :**
    *   Rupture structurelle sur la série temporelle $Z_{AB}(t)$ entre 1974 et 1977 avec $p < 0{,}01$ (test de permutation par rapport au modèle de configuration et par rapport à la trajectoire contrôle $Z_{AC}(t)$).
    *   Précision d'alignement (Hits@3) sur les 5 paires de variables canoniques de l'analogie d'Unruh (1981) strictement supérieure à l'espérance d'un appariement par simple rang de degré (test exact de Fisher, $p < 0{,}01$).
*   **Résultat qui réfuterait la proposition :**
    1. *Réfutation de la détectabilité pré-découverte :* Si $Z_{AB}(t)$ reste stationnaire de 1965 à 1980 ($p > 0{,}05$) et ne chute qu'*après* 1981 (une fois qu'Unruh a explicitement réécrit les équations hydrodynamiques sous forme de tenseur métrique $g_{\mu\nu}$), alors l'invariance structurelle n'préexiste pas dans la littérature : elle est entièrement **construite** par l'acte de reformulation de l'auteur de la découverte.
    2. *Réfutation de la suffisance de la topologie :* Si le couplage $\pi^*(t)$ donne une distance $\Delta_{AB}(t)$ faible mais aligne les variables physiques de manière incohérente (Hits@3 indistinguable d'un appariement par simple degré des nœuds), alors la topologie d'un réseau de concepts sans typage algébrique des opérateurs différentiels est sous-déterminée et impropre à capturer une analogie scientifique.

---

### Références bibliographiques

*   Baez, J. C., & Fong, B. (2013). A Noether theorem for Markov processes. *Journal of Mathematical Physics*, 54(1), 013301.
*   Blokhintsev, D. I. (1946). *Acoustics of a nonhomogeneous moving medium* (en russe ; trad. anglaise NACA Technical Memorandum 1399, 1956).
*   Chalmers, D. J., French, R. M., & Hofstadter, D. R. (1992). High-level perception, representation, and analogy: A critique of artificial intelligence methodology. *Journal of Experimental & Theoretical Artificial Intelligence*, 4(3), 185–211.
*   Corradini, A., Montanari, U., Rossi, F., Ehrig, H., Heckel, R., & Löwe, M. (1997). Algebraic approaches to graph transformation—Part I: Basic concepts and double pushout approach. In G. Rozenberg (Ed.), *Handbook of Graph Grammars and Computing by Graph Transformations, Vol. 1: Foundations* (pp. 163–245). World Scientific.
*   Falkenhainer, B., Forbus, K. D., & Gentner, D. (1989). The structure-mapping engine: Algorithm and examples. *Artificial Intelligence*, 41(1), 1–63.
*   Gentner, D.