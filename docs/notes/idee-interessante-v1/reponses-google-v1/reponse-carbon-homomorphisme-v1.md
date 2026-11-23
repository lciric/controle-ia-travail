### Verdict liminaire sur la proposition

**La proposition initiale doit être rejetée sous sa forme stricte et remplacée.** Modéliser une découverte inter-domaines par un *homomorphisme de graphes typés* échoue pour deux raisons structurelles : (1) un homomorphisme envoie une arête sur une arête unique, alors qu’une analogie scientifique relie presque toujours une relation élémentaire d’un domaine à une *chaîne composée* de mécanismes dans l’autre ; (2) le typage partagé présuppose l’unification conceptuelle que la découverte doit justement accomplir. Quant à l’*équivariance globale d’opérateurs discrets*, elle postule une action de groupe (inversible, partout définie) absente des réseaux d’inférences ou de causalité, qui ne forment que des semi-groupes ou des catégories partielles.

**Remplacement proposé :**
* **Au niveau formel (cible de la découverte)** : un *span de foncteurs partiels* $\mathcal{C}_1 \xleftarrow{F_1} \mathcal{K} \xrightarrow{F_2} \mathcal{C}_2$ entre catégories de chemins quotients (*ologs* ; Spivak & Kent, 2012), doublé localement d’une équivariance de *groupoïde* restreinte au régime de validité.
* **Au niveau pré-formel (détection empirique avant découverte)** : un couplage de *Gromov-Wasserstein partiel* calculé non sur l’adjacence brute, mais sur les résolvantes de chemins orientés.

---

### 1. Objets : définitions et épreuve sur les cas réels

Notons nos cas d’épreuve : **(E1)** unification newtonienne de la chute des graves terrestres et des orbites célestes (Newton, 1687) ; **(E2)** horizons acoustiques dans les fluides transsoniques imitant l’évaporation des trous noirs (Unruh, 1981) ; **(E3)** persistance du traitement nociceptif sous anesthésie générale malgré l’abolition du rapport conscient (Brown, Lydic, & Schiff, 2010 ; Sanders, Tononi, Laureys, & Sleigh, 2012), transposée à la persistance d’états internes latents dans un modèle de langage (LLM) malgré le blocage du texte produit en surface (Burns, Ye, Klein, & Steinhardt, 2023).

#### 1.1. Graphe orienté typé et homomorphisme
* **Définition.** Un graphe orienté typé sur les alphabets de types $(\Sigma_V, \Sigma_E)$ est un n-uplet $G = (V, E, s, t, \ell_V, \ell_E)$ avec $s, t : E \to V$, $\ell_V : V \to \Sigma_V$ et $\ell_E : E \to \Sigma_E$. Un *homomorphisme* $G_1 \to G_2$ (relatif à un morphisme d’alphabets $\tau = (\tau_V, \tau_E)$) est un couple $(\phi_V : V_1 \to V_2, \phi_E : E_1 \to E_2)$ tel que $s_2 \circ \phi_E = \phi_V \circ s_1$, $t_2 \circ \phi_E = \phi_V \circ t_1$, $\ell_{V_2} \circ \phi_V = \tau_V \circ \ell_{V_1}$ et $\ell_{E_2} \circ \phi_E = \tau_E \circ \ell_{E_1}$ (homomorphisme strict si $\tau = \mathrm{id}$).
* **Épreuve.**
  * *(E1)* Capture l’identification conceptuelle *a posteriori* si $\tau_V$ fusionne les types aristotéliciens « sublunaire » et « supralunaire ». Manque tout si $\tau = \mathrm{id}$ (ensemble d’homomorphismes vide avant Newton) et échoue sur la granularité : « hauteur $\to$ chute rectiligne » ne s’envoie pas sur une arête unique « rayon $\to$ orbite fermée » sans décomposition infinitésimale.
  * *(E2)* Échoue globalement : un homomorphisme total exigerait que toute relation de la mécanique des fluides (viscosité, turbulence, capillarité) ait une image dans la relativité générale.
  * *(E3)* Dangereux : avec $\tau = \mathrm{id}$, aucun morphisme n’existe entre types biologiques (`fibre C`, `thalamus`) et types numériques (`couche résiduelle`, `logit`). Avec $\tau$ libre, l’homomorphisme préserve l’adjacence positive mais ne peut pas exprimer une *absence* ou *inhibition* d’arête (dissociation vers le rapport verbal), tout en gommant la différence ontologique entre dommage homéostatique vécu et vecteur d’activation.

#### 1.2. Homomorphisme partiel et isomorphisme de sous-graphe
* **Définition.** Un *homomorphisme partiel* $G_1 \rightharpoonup G_2$ est un homomorphisme défini sur un sous-graphe $G'_1 \subseteq G_1$ (soit un *span* $G_1 \hookleftarrow G'_1 \to G_2$). Un *isomorphisme de sous-graphe* exige $\phi_V, \phi_E$ injectifs sur $G_1$ entier vers $G'_2 \subseteq G_2$ (et, s’il est induit, la préservation de la non-adjacence).
* **Épreuve.**
  * *(E1)* L’homomorphisme partiel capture l’exclusion des propriétés non pertinentes (couleur ou chimie de la pomme). L’isomorphisme de sous-graphe manque la fusion non injective (chute parabolique et orbite elliptique projetées sur une même loi en $r^{-2}$ ; Newton, 1687).
  * *(E2)* Capture précisément la localité de l’analogie d’Unruh (1981) : seul le sous-graphe cinématique linéarisé (écoulement irrotationnel barotrope, franchissement $v > c_s$) s’injecte dans le sous-graphe du champ scalaire sur métrique de Schwarzschild, excluant les équations dynamiques d’Einstein. Manque toutefois la limite asymptotique continue (coupure atomique haute fréquence).
  * *(E3)* L’isomorphisme de sous-graphe induit capture enfin la non-adjacence (`état interne` $\nrightarrow$ `rapport externe`, mais `état interne` $\to$ `effet aval`). Il pèche cependant par trivialité : un motif d’embranchement filtré apparaît dans d’innombrables systèmes régulés sans pertinence scientifique, tandis qu’à l’échelle microscopique les circuits thalamocorticaux et *Transformers* ne sont aucunement isomorphes.

#### 1.3. Foncteur entre catégories
* **Définition.** À un graphe $G$ muni de relations d’équivalence entre chemins parallèles (schéma de connaissances ou *olog* ; Spivak & Kent, 2012) est associée une catégorie $\mathcal{C}(G)$ dont les flèches sont les chemins orientés composés. Un *foncteur* $F : \mathcal{C}_1 \to \mathcal{C}_2$ envoie objets sur objets et flèches sur *chemins*, préservant identités ($F(\mathrm{id}_X) = \mathrm{id}_{F(X)}$), composition ($F(g \circ f) = F(g) \circ F(f)$) et diagrammes commutatifs. Une analogie partielle s’écrit comme un *span* fonctoriel $\mathcal{C}_1 \xleftarrow{F_1} \mathcal{K} \xrightarrow{F_2} \mathcal{C}_2$ (Mac Lane, 1998).
* **Épreuve.**
  * *(E1)* Résout l’obstacle d’échelle : une flèche macroscopique (« pesanteur terrestre ») s’envoie sur un chemin composé (« masse gravitationnelle $\to$ force centrale $\to$ accélération centripète évaluée au rayon terrestre »), conservant les équations de dérivation comme diagrammes commutatifs. Manque la topologie métrique continue (limite différentielle).
  * *(E2)* Le sommet $\mathcal{K}$ du span isole exactement la théorie effective commune (propagation d’ondes sur variété lorentzienne effective et thermalité de Hawking ; Hawking, 1975 ; Unruh, 1981) et délimite formellement ce qui ne se relève pas dans $\mathcal{K}$ (gravitation dynamique d’Einstein d’un côté, physique moléculaire du fluide de l’autre).
  * *(E3)* Formalise proprement la dissociation fonctionnelle (commutation du chemin `stimulus` $\to$ `état latent` $\to$ `trace indirecte` et annulation du composé vers `rapport`), tout en marquant rigoureusement l’absence de foncteur sur les propriétés hors de $\mathcal{K}$ : valence affective, métabolisme et conscience phénoménale ne sont pas transportés.

#### 1.4. Équivariance sous un groupe ou un groupoïde
* **Définition.** Pour un groupe $\Gamma$ agissant sur deux espaces $X_1, X_2$, $\Phi : X_1 \to X_2$ est *équivariante* (relativement à un morphisme $\rho : \Gamma \to \Gamma'$) si $\Phi(\gamma \cdot x) = \rho(\gamma) \cdot \Phi(x)$ ; pour un opérateur discret d’évolution $T$, cela s’écrit $\Phi \circ T_1 = T_2 \circ \Phi$. Un *groupoïde* $\mathcal{G} \rightrightarrows B$ est une petite catégorie dont toute flèche est inversible, mais où la composition n’est définie que localement (Weinstein, 1996).
* **Épreuve.**
  * *(E1)* Capture le cœur physique de Newton (1687) : l’équivariance sous le groupe de Galilée et le groupe des rotations euclidiennes garantit que la même loi régit pomme et Lune. Mais cette équivariance opère sur l’espace-temps continu des solutions, *non* sur le graphe discret des concepts.
  * *(E2)* L’équivariance de *groupe* échoue (le fluide au laboratoire brise l’invariance de Lorentz fondamentale). Seul un *groupoïde* de difféomorphismes locaux préservant le cône acoustique dans le régime grandes longueurs d’onde capture la symétrie émergente (Unruh, 1981 ; Weinstein, 1996).
  * *(E3)* Il n’existe aucun groupe de symétrie pertinent reliant pharmacologie anesthésique et algèbre linéaire d’un LLM ; tout au plus observe-t-on une commutation triviale d’opérateurs de projection (bloquer le décodeur de sortie commute avec le calcul des couches antérieures), trop pauvre pour caractériser la douleur ou la conscience.

---

### 2. Alignement imparfait entre vocabulaires disjoints

| Méthode | Ce qu’elle conserve | Coût de calcul | Échecs connus |
| :--- | :--- | :--- | :--- |
| **Homomorphismes approchés / gradués** : relaxation matricielle $P \in [0,1]^{n_1 \times n_2}$ minimisant $\|A_1 P - P A_2\|$ ou densités d’homomorphismes (Lovász, 2012). | Densités locales de motifs orientés et voisinages immédiats. | Décision exacte ($H$-coloration) NP-complète hors cibles biparties / sans boucles (Hell & Nešetřil, 1990) ; relaxations spectrales ou convexes polynomiales. | Effondrement dégénéré vers les nœuds hub/puits sans contrainte de masse ; aveugle aux correspondances « arête $\leftrightarrow$ chemin ». |
| **Transport de Gromov-Wasserstein (GW)** : minimise $\sum L(C_1(i,k), C_2(j,l)) \pi_{ij}\pi_{kl}$ sous contraintes marginales (Mémoli, 2011). | Géométrie relationnelle intrinsèque (isométrie aux isomorphismes près, *sans aucun vocabulaire commun*) ; multi-échelle si $C_m$ encode les chemins. | Problème quadratique d’affectation non convexe (NP-difficile en exact) ; régularisation entropique en $O(N^4)$, réduite à $O(N^3)$ par itération pour pertes séparables sur graphes de taille $N$ (Peyré, Cuturi, & Solomon, 2016). | Minima locaux ; le GW standard force à coupler *toute* la masse et échoue si l’analogie ne porte que sur un petit sous-graphe (exigeant du GW partiel ; Chapel, Alaya, & Gasso, 2020, *pagination exacte à vérifier*). |
| **Distance d’édition de graphes (GED)** : coût minimal d’insertions, suppressions et substitutions (Sanfeliu & Fu, 1983). | Topologie locale exacte à un budget discret de perturbations près. | NP-difficile en exact et difficile à approximer (Garey & Johnson, 1979 ; Zeng et al., 2009). | Sensibilité arbitraire aux poids d’édition ; si les vocabulaires sont disjoints, le coût de substitution des étiquettes masque la structure ; inadapté aux graphes de tailles très disparates. |
| **Structure-Mapping Engine (SME)** : appariement privilégiant la profondeur relationnelle ou *systématicité* (Gentner, 1983 ; Falkenhainer, Forbus, & Gentner, 1989). | Hiérarchies causales et logiques d’ordre supérieur (`CAUSE`, `IMPLIQUE`) indépendamment des attributs d’objets. | Génération locale et fusion gloutonne polynomiales ; énumération globale exacte exponentielle dans le pire cas (Falkenhainer, Forbus, & Gentner, 1989). | Dépendance critique au codage manuel préalable (Chalmers, French, & Hofstadter, 1992) : exige que les relations d’ordre supérieur portent déjà le même prédicat dans les deux domaines. |

---

### 3. Symétrie, conservation et théorème de type Noether discret

#### Analogues discrets
* **Automorphismes** ($\mathrm{Aut}(G)$) : symétries bijectives globales d’un même réseau. Presque tous les grands graphes sont asymétriques (Erdős & Rényi, 1963), ce qui rend $\mathrm{Aut}(G)$ trivial sur des réseaux empiriques bruités.
* **Groupoïdes de symétries** (Weinstein, 1996) : isomorphismes partiels entre sous-graphes locaux, seuls capables d’exprimer des invariances de régime.
* **Invariants de graphes** : fonctions constantes par isomorphisme (spectre d’opérateurs, homologie dirigée). Attention : un homomorphisme général ne conserve *pas* les invariants d’isomorphisme, mais seulement des quantités monotones (existence de cycles orientés, bornes chromatiques).
* **Naturalité catégorique** (Mac Lane, 1998) : une transformation naturelle $\eta : F \Rightarrow G$ vérifiant $G(f) \circ \eta_X = \eta_Y \circ F(f)$ formalise l’invariance d’une traduction par rapport au choix du chemin de dérivation.

#### Énoncé de type Noether : séparation stricte
* **Ce qui est démontré.** Le théorème d’Emmy Noether (Noether, 1918) exige une fonctionnelle d’action variationnelle. En cadre discret, un théorème de Noether exact est démontré *si et seulement si* l’on dispose d’un **lagrangien discret** sur maillage variationnel — l’invariance continue du lagrangien discret conserve alors exactement une application moment discrète (Marsden & West, 2001). En l’absence de lagrangien, si le graphe porte une **dynamique markovienne continue en temps** de générateur $H$, Baez & Fong (2013) démontrent qu’un opérateur $O$ commutant avec $H$ (et préservant la mesure uniforme sur les états finaux) engendre une espérance conservée $\frac{d}{dt}\langle O \rangle = 0$ ; mais ils démontrent aussi un contre-exemple crucial : contrairement au cas hamiltonien, symétries du générateur et lois de conservation ne sont plus en correspondance bijective en régime dissipatif/stochastique.
* **Ce qui est spéculatif (ou faux).** Sur un réseau de concepts orienté dépourvu de lagrangien discret comme de générateur dynamique canonique, **il n’existe aucun théorème de Noether**. Invoquer une « charge sémantique conservée par symétrie d’analogie » est dénué de fondement mathématique. La seule « conservation » rigoureuse disponible ici est algébrique : la **préservation fonctorielle des relations de commutativité** ($g \circ f = h \implies F(g) \circ F(f) = F(h)$) et, lorsqu’une marche aléatoire canonique est fixée, l’entrelacement approximatif des sous-espaces spectraux dominants.

---

### 4. Détecter le rapprochement avant la découverte

Pour tester à une date $t < t^*$ (où $t^*$ est la première publication reliant deux domaines $D_1$ et $D_2$) si un changement de représentation (nouvel instrument, formalisme ou protocole dans $D_1$) rapproche structurellement $D_1$ de $D_2$ :

1. **Données datées.** Corpus d’articles horodatés par date de réception (ex. archives de revues physiques ou biomédicales), restreints strictement aux textes soumis à $\tau \le t$. On exclut tout document co-classé dans $D_1 \cap D_2$, toute citation croisée et tout auteur publiant dans les deux champs avant $t$.
2. **Calcul.** Extraction par analyse syntaxique dépendancielle déterministe (sans modèle neuronal pré-entraîné sur le futur) de graphes orientés d’assertions mécanistes ou mathématiques $G_1(t), G_2(t)$. Pour capturer la composition des chemins (fonctorialité approchée), on calcule pour chaque graphe sa matrice de résolvante orientée normalisée $R_m(t) = (I - \alpha \tilde{A}_m(t))^{-1}$ (avec $\alpha$ strictement inférieur à l’inverse du rayon spectral), puis la divergence de **Gromov-Wasserstein partielle entropique** $d_{\mathrm{PGW}}(R_1(t), R_2(t))$ (Peyré, Cuturi, & Solomon, 2016 ; Chapel, Alaya, & Gasso, 2020), standardisée en score $z(t)$ par rapport à un modèle nul de graphes aléatoires conservant exactement la séquence de degrés entrants/sortants et par rapport à une cohorte de domaines contrôles $\{D_k\}$. Le signal recherché est une chute abrupte $\Delta_t z(t) < 0$ immédiatement après l’introduction de la nouvelle représentation dans $D_1$, à recouvrement lexical nul.
3. **Risques de circularité.**
   * *Fuite temporelle de représentation* : utiliser un LLM ou des plongements lexicaux entraînés après $t^*$ injecte la découverte future dans l’extraction des graphes.
   * *Délimitation rétrospective* : découper $D_1$ et $D_2$ avec les mots-clés modernes post-$t^*$ sélectionne artificiellement les sous-graphes alignés ; il faut utiliser la taxonomie institutionnelle figée avant $t$.
   * *Convergence topologique générique* : la croissance de deux champs peut produire des motifs hub-périphérie similaires par simple attachement préférentiel, d’où l’obligation des contrôles $\{D_k\}$ appariés en taille et densité.

---

### 5. Expérience minimale et critère de réfutation

* **Données.** Corpus intégral de la *Physical Review* antérieur à la soumission d’Unruh (1981), segmenté annuellement jusqu’en 1980 inclus via la classification PACS d’époque (*date exacte de généralisation uniforme des codes PACS à toutes les sections APS dans les années 1970 à vérifier*) : $D_1$ = relativité générale et thermodynamique des trous noirs ; $D_2$ = dynamique des fluides compressibles et acoustique non linéaire ; $\{D_k\}$ = domaines contrôles de taille comparable dans la même revue (physique nucléaire, cristallographie, plasmas), après purge de tout article partageant auteurs ou références entre $D_1$ et $D_2$, et masquage intégral des étiquettes lexicales des nœuds.
* **Algorithme.**
  1. Extraction syntaxique figée (règles grammaticales hors apprentissage post-1980) des graphes orientés de dépendances entre grandeurs physiques et régimes asymptotiques par fenêtre glissante annuelle.
  2. Calcul des résolvantes orientées $R_m(t)$ sur la composante géante de chaque domaine.
  3. Calcul par Sinkhorn (Peyré, Cuturi, & Solomon, 2016) de la distance de Gromov-Wasserstein partielle $d_{\mathrm{PGW}}(R_1(t), R_2(t))$ et des distances contrôles $\{d_{\mathrm{PGW}}(R_1(t), R_k(t))\}_k$, ainsi que sur des réwirings aléatoires préservant les degrés orientés.
* **Prédiction et seuil.** Après la reformulation cinématique du rayonnement de Hawking (1975) dans $D_1$ et *avant* Unruh (1981), la baisse de distance $\Delta d_{\mathrm{PGW}}(D_1, D_2)$ doit se classer dans la queue inférieure des tests de permutation exacts et franchir le seuil nominal de significativité de $5\,\%$ (Fisher, 1925) après correction du taux de fausses découvertes sur les fenêtres temporelles et paires testées (Benjamini & Hochberg, 1995), *et* la matrice de transport optimal $\pi^*$ doit apparier les nœuds correspondant à `(vitesse d'écoulement / vitesse du son)` et `(métrique radiale / horizon des événements)`.
* **Résultat réfutant la proposition.** La proposition (même corrigée en foncteurs/GW sur chemins) est **réfutée** si : (1) jusqu’en 1980, $d_{\mathrm{PGW}}(D_1, D_2)$ reste indiscernable des domaines contrôles $\{D_k\}$ ou du modèle nul à degrés fixés ; ou (2) une distance faible est détectée mais le couplage optimal $\pi^*$ échoue à aligner les nœuds homologues physiques lorsqu’on démasque les étiquettes, démontrant que l’invariance topologique mesurée n’est qu’un artefact générique des graphes d’équations sans pouvoir prédictif sur l’analogie réelle.

---

### Références

* Baez, J. C., & Fong, B. (2013). A Noether theorem for Markov processes. *Journal of Mathematical Physics*, 54(1), 013301.
* Benjamini, Y., & Hochberg, Y. (1995). Controlling the false discovery rate: A practical and powerful approach to multiple testing. *Journal of the Royal Statistical Society: Series B (Methodological)*, 57(1), 289–300.
* Brown, E. N., Lydic, R., & Schiff, N. D. (2010). General anesthesia, sleep, and coma. *New England Journal of Medicine*, 363(27), 2638–2650.
* Burns, C., Ye, H., Klein, D., & Steinhardt, J. (2023). Discovering latent knowledge in language models without supervision. *Proceedings of the International Conference on Learning Representations (ICLR)*.
* Chalmers, D. J., French, R. M., & Hofstadter, D. R. (1992). High-level perception, representation, and analogy: A critique of artificial intelligence methodology. *Journal of Experimental & Theoretical Artificial Intelligence*, 4(3), 185–211.
* Chapel, L., Alaya, M. Z., & Gasso, G. (2020). Partial optimal transport with applications on positive-unlabeled learning. *Advances in Neural Information Processing Systems (NeurIPS)*, 33 *(pagination exacte à vérifier)*.
* Erdős, P., & Rényi, A. (1963). Asymmetric graphs. *Acta Mathematica Academiae Scientiarum Hungaricae*, 14(3–4), 295–315.
* Falkenhainer, B., Forbus, K. D., & Gentner, D. (1989). The structure-mapping engine: Algorithm and examples. *Artificial Intelligence*, 41(1), 1–63.
* Fisher, R. A. (1925). *Statistical Methods for Research Workers*. Edinburgh: Oliver and Boyd.
* Garey, M. R., & Johnson, D. S. (1979). *Computers and Intractability: A Guide to the Theory of NP-Completeness*. San Francisco: W. H. Freeman.
* Gentner, D. (1983). Structure-mapping: A theoretical framework for analogy. *Cognitive Science*, 7(2), 155–170.
* Hawking, S. W. (1975). Particle creation by black holes. *Communications in Mathematical Physics*, 43(3), 199–220.
* Hell, P., & Nešetřil, J. (1990). On the complexity of $H$-coloring. *Journal of Combinatorial Theory, Series B*, 48(1), 92–110.
* Lovász, L. (2012). *Large Networks and Graph Limits*. Providence: American Mathematical Society.
* Mac Lane, S. (1998). *Categories for the Working Mathematician* (2nd ed.). New York: Springer.
* Marsden, J. E., & West, M. (2001). Discrete mechanics and variational integrators. *Acta Numerica*, 10, 357–514.
* Mémoli, F. (2011). Gromov–Wasserstein distances and the metric approach to object matching. *Foundations of Computational Mathematics*, 11(4), 417–487.
* Newton, I. (1687). *Philosophiæ Naturalis Principia Mathematica*. Londini: Jussu Societatis Regiæ ac Typis Josephi Streater.
* Noether, E. (1918). Invariante Variationsprobleme. *Nachrichten von der Gesellschaft der Wissenschaften zu Göttingen, Mathematisch-Physikalische Klasse*, 1918, 235–257.
* Peyré, G., Cuturi, M., & Solomon, J. (2016). Gromov-Wasserstein averaging of kernel and distance matrices. *Proceedings of the 33rd International Conference on Machine Learning (ICML)*, PMLR 48, 2664–2672.
* Sanders, R. D., Tononi, G., Laureys, S., & Sleigh, J. W. (2012). Unresponsiveness $\neq$ unconsciousness. *Anesthesiology*, 116(4), 946–959.
* Sanfeliu, A., & Fu, K.-S. (1983). A distance measure between attributed relational graphs for pattern recognition. *IEEE Transactions on Systems, Man, and Cybernetics*, SMC-13(3), 353–362.
* Spivak, D. I., & Kent, R. E. (2012). Ologs: A categorical framework for knowledge representation. *PLoS ONE*, 7(1), e24274.
* Unruh, W. G. (1981). Experimental black-hole evaporation? *Physical Review Letters*, 46(21), 1351–1353.
* Weinstein, A. (1996). Groupoids: Unifying internal and external symmetry. *Notices of the American Mathematical Society*, 43(7), 744–752.
* Zeng, Z., Tung, A. K. H., Wang, J., Feng, J., & Zhou, L. (2009). Comparing stars: On approximating graph edit distance. *Proceedings of the VLDB Endowment*, 2(1), 25–36.