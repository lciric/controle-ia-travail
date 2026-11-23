### Verdict liminaire sur la proposition

La proposition soumise comporte un diagnostic exact et une solution insuffisante. 

**Ce qui est valide :** Un réseau de concepts est effectivement discret, orienté et dépourvu de structure symplectique ou de densité lagrangienne canonique. Y chercher un hamiltonien pour appliquer mécaniquement la physique théorique relève de la métaphore abusive.

**Ce qui doit être rejeté et remplacé :** L’*homomorphisme de graphes typés* est un candidat trop faible et simultanément trop rigide pour formaliser l'analogie scientifique. Trop faible, car un graphe ne connaît que l'adjacence locale et ignore la *loi de composition* des relations ainsi que les *équations entre chemins* (diagrammes commutatifs) ; or, une analogie scientifique réduit souvent un chemin causal complexe du domaine source à une flèche unique du domaine cible. Trop rigide, car l'exigence de préservation exacte des arêtes échoue face au bruit et à la granularité asymétrique des lexiques. De même, l'*équivariance d'opérateurs discrets* suppose un groupe de symétrie non trivial agissant sur le réseau ; or, les grands graphes empiriques sont génériquement asymétriques (leur groupe d'automorphismes est trivial).

**Le remplacement proposé :** L'invariant exact d'une théorie conceptuelle n'est pas un graphe, mais une **esquisse catégorique** (*categorical sketch*, au sens d'Ehresmann) ou un **faisceau cellulaire** (*cellular sheaf*) sur un graphe ; le transfert analogique exact est un **foncteur** (ou un morphisme de faisceaux), et sa version empirique bruitée se mesure par le **transport optimal de Gromov-Wasserstein** sur les métriques de chemins, couplé à la **cohomologie des faisceaux** pour quantifier le défaut d'invariance.

---

### 1. Objets : définitions formelles et mise à l'épreuve

#### Définitions mathématiques
1. **Graphe orienté étiqueté et graphe typé :** Soit un graphe orienté $G = (V, E, s, t)$ où $s, t : E \to V$ sont les applications source et but. Il est *étiqueté* s'il est muni d'applications $\ell_V : V \to \Sigma_V$ et $\ell_E : E \to \Sigma_E$ vers des alphabets fixes. Il est *typé* par un graphe de types $T = (V_T, E_T, s_T, t_T)$ s'il est muni d'un homomorphisme de graphes $\tau_G : G \to T$ (c'est un objet de la catégorie tranche $\mathbf{Grph}/T$).
2. **Homomorphisme, homomorphisme partiel, isomorphisme de sous-graphe :** Un *homomorphisme* $f : G \to H$ est un couple $(f_V : V_G \to V_H, f_E : E_G \to E_H)$ tel que $s_H \circ f_E = f_V \circ s_G$ et $t_H \circ f_E = f_V \circ t_G$ (et $\tau_H \circ f = \tau_G$ dans $\mathbf{Grph}/T$). Un *homomorphisme partiel* de $G$ vers $H$ est un homomorphisme défini sur un sous-graphe $G' \subseteq G$. Un *isomorphisme de sous-graphe* est un homomorphisme injectif sur les sommets et les arêtes $f : G \hookrightarrow H$ (monomorphisme régulier s'il s'agit d'un sous-graphe induit).
3. **Foncteur entre catégories :** Soient $\mathcal{C}$ et $\mathcal{D}$ deux catégories (où les flèches se composent associativement et chaque objet possède une identité). Un foncteur $F : \mathcal{C} \to \mathcal{D}$ associe à tout objet $X$ un objet $F(X)$ et à tout morphisme $f : X \to Y$ un morphisme $F(f) : F(X) \to F(Y)$ tel que $F(\mathrm{id}_X) = \mathrm{id}_{F(X)}$ et $F(g \circ f) = F(g) \circ F(f)$.
4. **Équivariance sous un groupe ou un groupoïde :** Soit $K$ un groupe agissant sur des espaces de signaux $\mathcal{X}(G)$ et $\mathcal{X}(H)$ via des représentations $\rho_G$ et $\rho_H$. Un opérateur discret $\Phi : \mathcal{X}(G) \to \mathcal{X}(H)$ est $K$-équivariant si $\forall k \in K, \Phi \circ \rho_G(k) = \rho_H(k) \circ \Phi$. Si les symétries sont partielles et locales, $K$ est remplacé par un *groupoïde* $\mathcal{G}$ (petite catégorie dont tout morphisme est inversible), et l'équivariance n'est requise que pour les flèches composables $(g : u \to v) \in \mathcal{G}$.

#### Épreuve sur les trois exemples

| Exemple scientifique | Ce que capturent les objets | Ce qu'ils manquent (échec de la formalisation naïve) |
| :--- | :--- | :--- |
| **1. Gravitation terrestre et céleste (Newton)** | **Graphe typé & Homomorphisme :** Projettent `[Pomme] --(tombe)--> [Terre]` et `[Lune] --(orbite)--> [Terre]` sur le motif commun `[Masse m] --(attraction)--> [Masse M]`.<br>**Équivariance :** L'opérateur dynamique continu est équivariant sous le groupe de Galilée. | **Échec du graphe :** « Tomber » (trajectoire radiale dégénérée) et « orbiter » (conique non dégénérée) sont deux flèches statiques disjointes dans un graphe conceptuel. Le graphe manque l'*espace des phases* continu où ces deux concepts sont deux solutions de la même équation différentielle $\ddot{\mathbf{r}} = -\frac{GM}{r^3}\mathbf{r}$ distinguées par la vitesse tangentielle initiale. |
| **2. Écoulements fluides et horizon de trou noir (Unruh, 1981)** | **Homomorphisme partiel / Sous-graphe :** Isole la sous-structure acoustique du fluide et ignore la thermodynamique moléculaire.<br>**Foncteur :** Agit comme un foncteur d'oubli et de *linéarisation* depuis la mécanique des fluides et la relativité générale vers la catégorie commune des équations d'onde hyperboliques sur variétés lorentziennes. | **Échec de l'homomorphisme global :** Les graphes globaux des deux théories sont radicalement non isomorphes (les équations d'Euler/Navier-Stokes n'ont pas la topologie des équations d'Einstein). L'isomorphisme n'apparaît qu'après perturbation linéaire $\delta \psi$ autour d'un écoulement stationnaire irrotationnel barotrope, faisant émerger la métrique acoustique effective $g_{\mu\nu}^{\text{ac}}$ telle que $\Box_{g^{\text{ac}}} \delta\psi = 0$. Un graphe de concepts sans opérateur de dérivation (jet) ne peut pas voir cet alignement. |
| **3. Douleur sous anesthésie vs états internes d'un modèle de langage (LLM)** | **Foncteur & Factorisation :** Capturent l'annulation du morphisme de sortie. Le chemin `[Stimulus nociceptif] -> [Thalamus/Cortex] -> [Rapport conscient]` et `[Prompt sensible] -> [Couches cachées] -> [Token généré]` se factorisent tous deux par un morphisme nul sur la dernière flèche (blocage par le propofol ou filtre RLHF), tout en restant fidèles sur la sous-catégorie interne (réponse autonome / représentation linéaire détectable par *probing*). | **Échec de l'isomorphisme de sous-graphe :** Masque la différence de dynamique causale. Le traitement nociceptif biologique contient des boucles de rétroaction homéostatiques et humorales en temps continu ; le Transformer (LLM) est un graphe acyclique dirigé (*feed-forward*) à profondeur finie lors de l'inférence d'un token. L'équivariance sous intervention (dose d'analgésique vs *activation steering*) échoue dès que l'intervention biologique déclenche une rétroaction non linéaire absente du LLM. |

**Conclusion de la section 1 :** Pour capturer ces trois cas, il faut remplacer le graphe typé par une **esquisse catégorique** (Barr & Wells, 1985) ou un **Olog** (*Ontology Log*, Spivak & Kent, 2012) : une catégorie enrichie où certains cônes et cocônes sont marqués pour forcer des produits fibrés (définitions composées) et des égalités de chemins (lois physiques ou contraintes fonctionnelles).

---

### 2. Alignement imparfait entre vocabulaires disjoints

Lorsque deux domaines $A$ et $B$ utilisent des lexiques disjoints ($\Sigma_A \cap \Sigma_B = \emptyset$), l'alignement doit reposer exclusivement sur la géométrie relationnelle interne.

1. **Homomorphismes approchés ou gradués (Valued CSP) :**
   * *Principe :* On cherche une application $f : V_G \to V_H$ minimisant une fonction de coût de violation des arêtes $\mathcal{L}(f) = \sum_{(u,v) \in E_G} c_H(f(u), f(v))$, où $c_H(x,y) = 0$ si $(x,y) \in E_H$ et $>0$ sinon.
   * *Ce qu'il conserve :* La densité locale d'adjacence à une tolérance $\varepsilon$ près.
   * *Coût de calcul :* NP-difficile dans le cas général (inclut le problème d'homomorphisme de graphes et Max-Cut ; Hell & Nešetřil, 2004).
   * *Échecs connus :* Aveugle au changement d'échelle déductif (raffinement). Si une arête directe $(u,v) \in E_G$ correspond à une chaîne causale de longueur $k \ge 2$ dans $H$, la pénalité est maximale alors que l'analogie fonctionnelle est exacte.

2. **Transport optimal de Gromov-Wasserstein (GW) :**
   * *Principe :* On munit $G$ et $H$ de mesures de probabilité sur les sommets ($\mu_G, \mu_H$) et de matrices de coût interne $C_G, C_H$ (ex. distances géodésiques orientées ou noyaux de diffusion). On cherche un couplage $\pi \in \Pi(\mu_G, \mu_H)$ minimisant la distorsion relationnelle (Mémoli, 2011) :
     $$\mathrm{GW}_p^p(G, H) = \min_{\pi \in \Pi(\mu_G, \mu_H)} \sum_{i,j,k,l} |C_G(i,k) - C_H(j,l)|^p \pi_{i,j} \pi_{k,l}$$
   * *Ce qu'il conserve :* La géométrie métrique globale à isométrie près, avec possibilité de fractionnement de masse (un concept abstrait de $G$ peut se répartir sur un cluster de sous-concepts dans $H$).
   * *Coût de calcul :* Problème d'affectation quadratique non convexe, NP-difficile exactement. La régularisation entropique (Peyré, Cuturi, & Solomon, 2016) ramène chaque itération de projection de Sinkhorn à $O(|V_G||V_H|^2 + |V_G|^2|V_H|)$.
   * *Échecs connus :* Indétermination sous symétrie (si le graphe possède des automorphismes ou est régulier, le couplage s'effondre vers la mesure produit uniforme $\mu_G \otimes \mu_H$) ; insensibilité à l'orientation si $C_G$ est symétrisée.

3. **Distance d'édition de graphes (Graph Edit Distance, GED) :**
   * *Principe :* Coût minimal d'une séquence d'opérations élémentaires (insertion, suppression, substitution de sommets et d'arêtes) transformant $G$ en un graphe isomorphe à $H$.
   * *Ce qu'elle conserve :* Le sous-graphe commun maximal exact (noyau topologique dur).
   * *Coût de calcul :* NP-difficile (se réduit à l'isomorphisme de sous-graphe ; Garey & Johnson, 1979). Inapplicable exactement au-delà de quelques dizaines de sommets sans heuristiques relaxées.
   * *Échecs connus :* Explosion asymétrique face à la disparité de taille. Si $|V_G| \ll |V_H|$, la GED est intégralement dominée par le coût des $|V_H| - |V_G|$ suppressions de bruit, noyant le signal structurel du petit motif partagé.

4. **Moteur d'appariement de structures (Structure-Mapping Engine, SME) :**
   * *Principe :* Algorithme symbolique (Falkenhainer, Forbus, & Gentner, 1989) fondé sur le principe de *systématicité* de Gentner (1983) : il construit des correspondances locales entre prédicats de même arité, puis fusionne ces hypothèses en maximisant un score qui privilégie les relations d'ordre supérieur (ex. `CAUSE(P, Q)` ou `IMPLIQUE(P, Q)`).
   * *Ce qu'il conserve :* L'arité logique, la hiérarchie syntaxique et l'emboîtement causal.
   * *Coût de calcul :* Polynomial sur des arbres de prédicats à arité bornée via recherche locale, bien que la recherche du sous-graphe cohérent maximal reste NP-complète dans le cas non contraint.
   * *Échecs connus :* Dépendance fatale à l'encodage préalable (*hand-coding bottleneck*). Le SME exige que les connecteurs d'ordre supérieur portent *déjà* le même nom dans les deux domaines. Si les deux communautés expriment la causalité avec des syntaxes non unifiées, l'appariement échoue à s'amorcer.

---

### 3. Symétrie, conservation et théorème de Noether discret

#### Les analogues discrets de la symétrie
* **Groupe d'automorphismes $\mathrm{Aut}(G)$ :** Ensemble des permutations $\sigma \in S_V$ telles que la matrice d'adjacence $A$ commute avec la matrice de permutation $P_\sigma$ ($[A, P_\sigma] = 0$). Pour presque tous les réseaux empiriques réels, ce groupe est trivial ou réduit à quelques feuilles pendantes.
* **Groupoïde de symétries (Partitions équitables) :** Dans les réseaux de cellules couplées (Golubitsky, Stewart, & Török, 2005), même sans symétrie globale, deux nœuds peuvent recevoir des ensembles d'entrées isomorphes. Ces bijections locales forment un *groupoïde de symétrie* $\mathcal{B}$. Ses orbites définissent des partitions équilibrées (*equitable partitions*) qui garantissent l'existence de sous-espaces invariants de synchronisation pour toute dynamique admissible sur le graphe.
* **Naturalité catégorique :** Si deux domaines sont vus comme deux représentations (foncteurs) $F, G : \mathcal{C} \to \mathbf{Set}$ d'une même esquisse théorique $\mathcal{C}$, l'invariance du transfert analogique est formalisée par une **transformation naturelle** $\eta : F \Rightarrow G$. Pour toute inférence $f : X \to Y$ dans $\mathcal{C}$, le carré $\eta_Y \circ F(f) = G(f) \circ \eta_X$ commute : **ce qui est conservé, c'est la validité déductive des chemins** à travers le changement de vocabulaire.

#### Existe-t-il un théorème de Noether discret ici ? (Démontré vs Spéculatif)

**Ce qui est mathématiquement démontré :**
1. *Mécanique discrète variationnelle :* Lorsqu'un système discret sur réseau possède un lagrangien discret $L_d(q_k, q_{k+1})$ invariant sous l'action d'un groupe de Lie continu $G$, le théorème de Noether discret (Marsden & West, 2001) garantit la conservation exacte d'une application moment discrète $J_d$ le long des solutions des équations d'Euler-Lagrange discrètes.
2. *Dynamique linéaire sur graphe :* Si un opérateur d'évolution sur graphe (ex. marche quantique $e^{-itL}$ ou diffusion $e^{-tL}$ gouvernée par le laplacien $L$) commute avec une représentation $P_\sigma$ de $\mathrm{Aut}(G)$, alors les projections de l'état sur les sous-espaces propres associés aux représentations irréductibles de $\mathrm{Aut}(G)$ sont des quantités conservées au cours du temps $t$.
3. *Réseaux de flux passifs :* Sur un graphe muni de potentiels aux nœuds et de flux aux arêtes (réseaux de Kirchhoff), la loi de conservation du courant ($\partial^* J = 0$, où $\partial^*$ est la divergence sur graphe) découle de l'invariance de jauge globale du potentiel $V_i \mapsto V_i + c$ (Baez & Fong, 2013 « à vérifier : l'article traite des réseaux électriques passifs par foncteurs symplectiques, la connexion à l'invariance de jauge élémentaire est standard en théorie homologique des circuits »).

**Ce qui est spéculatif (et formellement faux) :**
Invoquer un théorème de Noether sur un *réseau de concepts* statique pour en déduire une « charge sémantique conservée » est une erreur de catégorie mathématique. Le théorème de Noether exige trois ingrédients absents d'un graphe conceptuel :
1. Une variable d'évolution (temps physique ou paramètre de flot) ;
2. Une fonctionnelle d'action $\mathcal{S}$ dont la dynamique réelle minimise la variation ($\delta \mathcal{S} = 0$) ;
3. Une symétrie continue (ou une différence finie exacte sur un maillage) permettant d'intégrer par parties la variation de l'action.

**Le substitut rigoureux :** Dans un réseau conceptuel sans dynamique lagrangienne, l'analogue d'une loi de conservation est **cohomologique**. Si l'on modélise un système de concepts et de contraintes par un *faisceau cellulaire* (*cellular sheaf*) $\mathcal{F}$ sur le graphe $G$ (assignant un espace vectoriel $\mathcal{F}(v)$ à chaque concept, un espace $\mathcal{F}(e)$ à chaque relation, et des applications de restriction linéaires $\mathcal{F}_{v \unlhd e} : \mathcal{F}(v) \to \mathcal{F}(e)$ ; Hansen & Ghrist, 2019), alors l'opérateur cobord $\delta^0$ mesure le désaccord local entre concepts reliés. Les « quantités conservées » (les invariants globaux cohérents à travers tout le réseau) sont très exactement les éléments du groupe de cohomologie de degré zéro :
$$H^0(G; \mathcal{F}) = \ker \delta^0 = \left\{ x \in \bigoplus_{v \in V} \mathcal{F}(v) \;\middle|\; \forall e=(u,v) \in E, \; \mathcal{F}_{u \unlhd e}(x_u) = \mathcal{F}_{v \unlhd e}(x_v) \right\}$$

---

### 4. Détection avant la découverte : protocole et risques de circularité

L'hypothèse épistémologique est qu'une découverte reliant les domaines $A$ et $B$ à la date $t_{\text{déc}}$ est précédée, à une date $t_0 < t_{\text{déc}}$, par un changement de représentation dans $A$ (nouvel instrument, nouveau formalisme mathématique) qui rend la topologie de $G_A(t_0)$ homomorphe ou isométrique à celle de $G_B(t_0)$ *avant* que quiconque ne publie le lien.

#### Données datées requises
* Corpus scientifiques à horodatage strict et immuable : archives de prépublications (arXiv avec métadonnées `v1` exactes), corpus de la société américaine de physique (APS dataset, indexé par codes PACS et dates de réception), ou base MEDLINE/PubMed filtrée strictement par date d'entrée (`DateCreated`), excluant les mises à jour rétroactives.

#### Calcul de détection à la date $t$
1. **Condition d'isolation :** À la date $t < t_{\text{déc}}$, sélectionner les paires de sous-domaines $(A, B)$ dont la distance bibliométrique est quasi infinie (zéro co-citation directe, zéro auteur commun sur la fenêtre $[t - \Delta t, t]$).
2. **Extraction purement relationnelle :** Pour chaque domaine, construire le graphe dirigé typé $G_A(t)$ et $G_B(t)$ des dépendances opératoires (sujet-verbe-objet ou graphe de dépendance des variables dans les équations).
3. **Effacement lexical (*Lexical Blinding*) :** Supprimer toutes les étiquettes textuelles des sommets. Ne conserver que la topologie orientée et un typage abstrait universel des arêtes (ex. : `dérivée_temporelle`, `proportionnel_à`, `inhibe`, `compose`).
4. **Mesure d'alignement différentiel :** Calculer la divergence de Gromov-Wasserstein typée $D_{\text{GW}}(G_A(t), G_B(t))$ sur les matrices de plus courts chemins dirigés. On cherche une chute brutale $\Delta_t D_{\text{GW}} = D_{\text{GW}}(t) - D_{\text{GW}}(t-1) \ll 0$ déclenchée par l'apparition d'un nouveau sous-graphe de représentation $R_A \subset G_A(t)$.

#### Trois risques critiques de circularité (et comment les éliminer)
1. **Contamination anachronique des plongements (Data Leakage des LLM) :** Utiliser un modèle de langage moderne (entraîné sur des textes postérieurs à $t_{\text{déc}}$) pour extraire les graphes ou vectoriser les concepts de l'année $t_0$ invalide toute l'expérience. Le LLM « sait » déjà que l'acoustique fluide et les trous noirs sont liés et projettera leurs vocabulaires de 1979 dans le même sous-espace latent. *Remède :* Utiliser exclusivement des analyseurs syntaxiques déterministes (grammaires de dépendances hors contexte) ou des modèles de langue entraînés *from scratch* sur un corpus tronqué à $t_0$.
2. **Rétro-ingénierie des ontologies :** Les arbres de catégories (comme le thésaurus MeSH ou les classifications Wikipédia) sont réécrits après les découvertes pour rapprocher les domaines fusionnés. *Remède :* Interdire toute ontologie externe non figée à la date $t_0$.
3. **Biais du survivant :** Tester uniquement la paire $(A, B)$ connue pour avoir convergé à $t_{\text{déc}}$ produira toujours des fluctuations interprétables a posteriori. *Remède :* Évaluer $(A, B)$ au sein d'une matrice complète de $N \times N$ domaines disjoints à la date $t_0$.

---

### 5. Expérience minimale falsifiable

Pour éprouver la thèse selon laquelle l'invariance structurelle précède et explique l'analogie scientifique, voici un protocole expérimental complet et réfutable.

* **Données :** Le jeu de données de l'American Physical Society (APS) découpé en tranches annuelles strictes de 1970 à 1985. On cible 20 découvertes inter-domaines historiques documentées (dont l'analogie d'Unruh, soumise en décembre 1980 / publiée en mai 1981 dans *Physical Review Letters*, reliant la mécanique des fluides compressibles [PACS 47.10/47.40] et la théorie quantique des champs en espace-temps courbe [PACS 04.60/04.70]), confrontées à un groupe de contrôle de 500 paires de codes PACS disjoints tirés aléatoirement sans co-citation avant 1981.
* **Algorithme :**
  1. Pour chaque tranche annuelle $t$ et chaque cluster PACS, extraire des articles les graphes de dépendance mathématique des équations : les sommets sont les symboles de variables, les arêtes orientées relient $x \to y$ si $x$ apparaît dans l'opérateur différentiel ou algébrique définissant $y$. Chaque sommet reçoit uniquement un vecteur d'attributs structurels intrinsèques $a_v \in \mathbb{R}^4$ : `[degré entrant, degré sortant, ordre maximal de dérivation subie, centralité de PageRank]`.
  2. Calculer la distance de *Fused Gromov-Wasserstein* (Vayer, Chapel, Flamary, Tavenard, & Courty, 2020) entre $G_A(t)$ et $G_B(t)$, qui combine la distance entre attributs structurels $a_v$ et la distorsion des matrices de plus courts chemins $C_A, C_B$ :
     $$\mathrm{FGW}_\alpha(G_A, G_B) = \min_{\pi \in \Pi(\mu_A, \mu_B)} \sum_{i,j,k,l} \left[ (1-\alpha)\|a_i^A - a_j^B\|_2^2 + \alpha |C_A(i,k) - C_B(j,l)|^2 \right] \pi_{i,j}\pi_{k,l}$$
     avec $\alpha = 0{,}8$ (pondération privilégiant la topologie pure).
  3. Pour chaque paire $(A, B)$ à la date $t$, générer une distribution nulle de 1 000 graphes permutés conservant la séquence de degrés orientés (algorithme de réassignation des arêtes de Maslov & Sneppen, 2002) afin de calculer un score standardisé $Z_{AB}(t) = \frac{\mathrm{FGW}(G_A, G_B) - \mu_{\text{nul}}}{\sigma_{\text{nul}}}$.
* **Prédiction et Seuil :**
  1. Pour les 20 paires historiques vraies, dans la fenêtre $[t_{\text{déc}} - 3 \text{ ans}, t_{\text{déc}} - 1 \text{ an}]$ (après l'introduction du formalisme pertinent mais avant toute co-citation), le score structurel franchit le seuil critique $Z_{AB}(t) < -3{,}0$ (correspondant à un quantile empirique $p < 0{,}01$).
  2. Dans le cas Unruh (1979-1980), la matrice de couplage optimal $\pi^*$ aligne avec le poids maximal le nœud structurel `[potentiel de vitesse irrotationnel` $\phi$ `]` du cluster fluide sur le nœud `[champ scalaire` $\psi$ `]` du cluster relativiste, et `[vitesse locale du son` $c_s$ `]` sur `[vitesse de la lumière / composante métrique` $g_{00}$ `]`, sans aucune information textuelle.
  3. Sur l'ensemble des paires $(A, B)$ évaluées à $t_0$, le classement par $-Z_{AB}(t_0)$ prédit l'apparition d'un article pont dans les 5 années suivantes avec une aire sous la courbe précision-rappel (AUC-PR) supérieure d'au moins un facteur 2 au modèle nul fondé sur la simple proximité de co-citation d'ordre 2 ou 3.
* **Résultat qui réfuterait la proposition :**
  La proposition (l'analogie découverte repose sur une invariance homomorphe/isométrique préexistante des réseaux de concepts) est **réfutée** si l'un des deux résultats suivants est observé :
  1. *Indistinguabilité pré-découverte :* Pour $t < t_{\text{déc}}$, le score $Z_{AB}(t)$ des paires historiques reste confiné dans l'intervalle de bruit $[-1{,}96, +1{,}96]$ et ne plonge sous $-3{,}0$ qu'*après* $t_{\text{déc}}$ (ce qui prouverait que l'isomorphisme structurel n'est pas *découvert* entre deux réseaux indépendants, mais *construit a posteriori* par les chercheurs qui réécrivent les deux domaines avec les mêmes équations une fois l'idée publiée).
  2. *Dégénérescence topologique :* Le couplage $\pi^*$ atteint $Z_{AB} < -3{,}0$ pour des centaines de paires aléatoires du groupe de contrôle sans valeur scientifique (faux positifs massifs), démontrant que la topologie des graphes d'équations ou de concepts est trop pauvre et générique (petit monde, lois de puissance) pour porter à elle seule la spécificité d'une invariance scientifique sans la sémantique continue des opérateurs différentiels sous-jacents.

---

### Références bibliographiques

* Baez, J. C., & Fong, B. (2013). A compositional framework for passive linear networks. *arXiv preprint arXiv:1504.05625* [« à vérifier » : prépublication diffusée initialement vers 2013-2015, publiée ensuite dans *Theory and Applications of Categories*, 33(38), 1158-1222 en 2018].
* Barr, M., & Wells, C. (1985). *Toposes, Triples and Theories*. Springer-Verlag.
* Falkenhainer, B., Forbus, K. D., & Gentner, D. (1989). The structure-mapping engine: Algorithm and examples. *Artificial Intelligence*, 41(1), 1-63.
* Garey, M. R., & Johnson, D. S. (1979). *Computers and Intractability: A Guide to the Theory of NP-Completeness*. W. H. Freeman.
* Gentner, D. (1983). Structure-mapping: A theoretical framework for analogy. *Cognitive Science*, 7(2), 155-170.
* Golubitsky, M., Stewart, I., & Török, A. (2005). Patterns of synchrony in coupled cell networks with multiple arrows. *SIAM Journal on Applied Dynamical Systems*, 4(1), 78-100.
* Hansen, J., & Ghrist, R. (2019). Toward a spectral theory of cellular sheaves. *Journal of Applied and Computational Topology*, 3(4), 315-358.
* Hell, P., & Nešetřil, J. (2004). *Graphs and Homomorphisms*. Oxford University Press.
* Marsden, J. E., & West, M. (2001). Discrete mechanics and variational integrators. *Acta Numerica*, 10, 357-514.
* Maslov, S., & Sneppen, K. (2002). Specificity and stability in topology of protein networks. *Science*, 296(5569), 910-913.
* Mémoli, F. (2011). Gromov–Wasserstein distances and the metric approach to object matching. *Foundations of Computational Mathematics*, 11(4), 417-487.
* Peyré, G., Cuturi, M., & Solomon, J. (2016). Gromov-Wasserstein averaging of kernel and distance matrices. *Proceedings of the 33rd International Conference on Machine Learning (ICML)*, PMLR 48, 2664-2672.
* Spivak, D. I., & Kent, R. E. (2012). Ologs: A categorical framework for knowledge representation. *PLoS ONE*, 7(1), e24274.
* Unruh, W. G. (1981). Experimental black-hole evaporation? *Physical Review Letters*, 46(21), 1351-1353.
* Vayer, T., Chapel, L., Flamary, R., Tavenard, R., & Courty, N. (2020). Fused Gromov-Wasserstein distance for structured objects. *Algorithms*, 13(9), 212.