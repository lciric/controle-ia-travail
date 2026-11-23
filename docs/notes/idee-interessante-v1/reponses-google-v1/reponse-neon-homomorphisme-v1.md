### Verdict critique sur la proposition

La proposition initiale — substituer à l'invariance physique un homomorphisme de graphes typés ou l'équivariance d'opérateurs discrets sur un réseau de concepts — doit être **partiellement rejetée et remplacée**. Un homomorphisme de graphes typés est à la fois *trop faible* (il ignore la composition des dérivations, les relations d'ordre supérieur, les équations quantitatives et les régimes de validité) et *trop permissif* (il produit des alignements vacueux sur des graphes grossiers). Quant à l'équivariance d'opérateurs discrets, elle suppose déjà une symétrie commune agissant sur les deux domaines, alors qu'une découverte construit d'abord un pont *partiel* entre deux théories hétérogènes. Il convient de lui substituer un cadre dual : au niveau des *théories*, des foncteurs partiels ou *spans* entre modèles dynamiques/causaux restreints à un régime ; au niveau *documentaire*, des alignements approchés d'hypergraphes typés ou de catégories finiment présentées.

---

### 1. Objets : définitions et mise à l'épreuve

Éprouvons les six candidats sur trois cas : **(G)** l'unification de la gravitation terrestre et céleste (loi en $1/r^2$ ; Newton, 1687) ; **(F)** les écoulements de fluides imitant un horizon de trou noir via une métrique acoustique effective (Unruh, 1981) ; **(D)** la persistance d'un traitement sensoriel/nociceptif sous anesthésie malgré l'absence de réponse comportementale (Sanders et al., 2012), transposée aux représentations latentes d'un modèle de langage (LLM) qui restent décodables malgré le filtrage en sortie (Burns et al., 2023) — analogie spéculative utile comme test de faux positifs.

- **Graphe étiqueté ou typé.** Un graphe orienté étiqueté est un sextuplet $G=(V,E,s,t,\ell_V,\ell_E)$ muni d'applications source/but $s,t:E\to V$ et d'étiquettes $\ell_V:V\to\Sigma_V$, $\ell_E:E\to\Sigma_E$. Un *graphe typé* est un couple $(G,\tau_G)$ doté d'un morphisme $\tau_G:G\to T$ vers un graphe de types $T$ (objet de la catégorie tranche $\mathbf{Graph}/T$ ; Ehrig et al., 2006), imposant quelles arêtes typées peuvent relier quels nœuds typés.
  *Capture* : la taxonomie d'entités et de liens binaires dans **(G)**, **(F)** et **(D)**.
  *Manque* : les relations d'ordre supérieur (relations entre relations), les opérateurs différentiels (**G**, **F**), les bornes d'échelle (**F**) et le statut causal ou phénoménal des variables (**D**).

- **Homomorphisme.** Couple d'applications $h=(h_V,h_E):G\to G'$ préservant source, but ($h_V\circ s=s'\circ h_E$, $h_V\circ t=t'\circ h_E$) et typage ($\tau_{G'}\circ h=\tau_G$) (Hell & Nešetřil, 2004 ; Ehrig et al., 2006).
  *Capture* : la conservation d'incidences qualitatives (`corps attire corps` en **G** ; `vitesse critique` $\to$ `piégeage` en **F** ; `blocage en aval` en **D**).
  *Manque* : l'injectivité (des concepts distincts peuvent s'effondrer en un seul nœud), la structure quantitative (**G**, **F**) et la sélectivité sémantique — sur **(D)**, un homomorphisme réussit trivialement entre deux schémas de filtrage en sortie sans établir aucun mécanisme commun entre nociception biologique et activations d'un LLM.

- **Homomorphisme partiel.** Homomorphisme $h:D\to G'$ défini sur un sous-graphe $D\subseteq G$ (soit un *span* $G\hookleftarrow D\xrightarrow{h} G'$).
  *Capture* : la portée *locale* des analogies — écarter les frottements en **(G)**, restreindre **(F)** à la cinématique acoustique basses fréquences (sans transférer ni les équations d'Einstein ni le régime dispersif microscopique), isoler la dissociation interne/sortie en **(D)**.
  *Manque* : un critère intrinsèque fixant $D$ ; choisi *ad hoc*, $D$ rend **(D)** quasi infalsifiable en excluant biologie, homéostasie et phénoménologie.

- **Isomorphisme de sous-graphe.** Homomorphisme injectif $h:H\hookrightarrow G'$ (dit *induit* s'il reflète aussi l'absence d'arêtes).
  *Capture* : la préservation exacte d'un motif topologique sans effondrement dégénéré (**G**, **F**, **D**).
  *Manque* : la tolérance aux changements de granularité (concept agrégé d'un côté, décomposé de l'autre en **G** ou **F**), la géométrie continue (**F**) et la sémantique physique des nœuds (**D**).

- **Foncteur entre catégories.** Étant donné deux catégories $\mathcal{C},\mathcal{D}$, application $F:\mathcal{C}\to\mathcal{D}$ sur objets et morphismes vérifiant $F(\mathrm{id}_A)=\mathrm{id}_{F(A)}$ et $F(g\circ f)=F(g)\circ F(f)$ (Mac Lane, 1998).
  *Capture* : la *compositionnalité* des dérivations (force $\to$ accélération $\to$ trajectoire conique en **G**), la factorisation de **(F)** par un *span* vers une catégorie de champs sur métrique lorentzienne effective, la cohérence d'un *olog* conceptuel (Spivak & Kent, 2012) et la commutation des interventions comme test falsifiable d'abstraction causale en **(D)** (Beckers & Halpern, 2019).
  *Manque* : sans enrichissement analytique ou métrique, les constantes numériques (**G**), les bornes d'erreur de la limite hydrodynamique (**F**) et le fossé ontologique de **(D)**.

- **Équivariance sous un groupe ou un groupoïde.** Pour un groupe $G$ agissant sur $X$ et $Y$, un opérateur $T:X\to Y$ est $G$-équivariant si $T(g\cdot x)=g\cdot T(x)$ (Cohen & Welling, 2016). Pour un *groupoïde* $\mathcal{G}$ (catégorie dont tout morphisme est inversible, modélisant des symétries locales ; Weinstein, 1996), une $\mathcal{G}$-action est un foncteur de $\mathcal{G}$ vers $\mathbf{Set}$ ou $\mathbf{Vect}$, et un opérateur $\mathcal{G}$-équivariant est une transformation naturelle entre deux actions.
  *Capture* : les symétries rotationnelles et galiléennes de la loi unifiée en **(G)** et la covariance locale sous difféomorphismes et transformations conformes de l'équation d'onde acoustique en **(F)**.
  *Manque* : la mise en correspondance initiale entre vocabulaires disjoints (**G**, **F**) et toute pertinence sur **(D)**, où aucun groupe ou groupoïde de symétrie physique ne relie circuits nociceptifs et poids d'un LLM.

---

### 2. Alignement imparfait entre vocabulaires différents

Lorsque $\Sigma_1\cap\Sigma_2=\varnothing$, l'alignement ne peut s'appuyer sur l'identité lexicale et doit exploiter la structure relationnelle.

- **Homomorphismes approchés ou gradués.** Relâchement par maximisation d'adjacences préservées (problème d'affectation quadratique, QAP), densités d'homomorphismes et distance de coupe (Lovász, 2012), ou morphismes gradués/à coût minimal. *Conservé* : cohérence globale d'incidences ou statistiques de motifs. *Coût* : décider l'homomorphisme exact vers un graphe non orienté fixé $H$ non biparti sans boucle est NP-complet (Hell & Nešetřil, 2004) ; le QAP est NP-difficile et inapproximable à facteur constant en temps polynomial sauf si $\mathrm{P}=\mathrm{NP}$ (Sahni & Gonzalez, 1976). *Échecs* : effondrements non injectifs sur des motifs denses et perte de pouvoir discriminant des relaxations spectrales sur graphes réguliers.

- **Transport optimal de Gromov-Wasserstein (GW).** Recherche d'un couplage $\pi\in\Pi(\mu_1,\mu_2)$ minimisant la distorsion entre matrices de distances ou noyaux internes des deux graphes (Mémoli, 2011) ; le *Fused GW* combine structure et attributs (Vayer et al., 2020). *Conservé* : géométrie relationnelle par paires à isométrie près, indépendamment des étiquettes, par correspondances souples. *Coût* : optimisation quadratique non convexe NP-difficile en général ; la régularisation entropique avec pertes décomposables abaisse le coût par itération de $O(n^4)$ à $O(n^3)$ pour des graphes de taille comparable $n$ (Peyré, Cuturi & Solomon, 2016). *Échecs* : minima locaux, perte d'asymétrie si les distances sont symétriques, transport forcé de masse entre graphes de tailles inégales (partiellement levé par le GW non équilibré ; Séjourné, Vialard & Peyré, 2021) et cécité aux hyperarêtes d'ordre supérieur.

- **Distance d'édition de graphes (GED).** Coût minimal d'insertions, suppressions et substitutions de nœuds et d'arêtes transformant $G_1$ en $G_2$ (Sanfeliu & Fu, 1983). *Conservé* : proximité topologique globale. *Coût* : NP-difficile et APX-difficile (Zeng et al., 2009) ; l'approximation par appariement biparti de voisinages locaux s'exécute en $O((|V_1|+|V_2|)^3)$ (Riesen & Bunke, 2009). *Échecs* : sensibilité aux coûts choisis ; entre vocabulaires disjoints sans dictionnaire externe, toute substitution de nœud coûte autant, de sorte que les écarts de taille et de densité écrasent le sous-graphe analogique partagé.

- **Moteur d'appariement de structures (SME).** Implémentation algorithmique de la théorie de l'appariement structurel (Gentner, 1983 ; Falkenhainer, Forbus & Gentner, 1989). *Conservé* : correspondance biunivoque, connectivité parallèle et *systématicité* (préférence aux systèmes emboîtés de relations d'ordre supérieur). *Coût* : l'énumération exhaustive des appariements globaux cohérents est exponentielle en pire cas (Falkenhainer, Forbus & Gentner, 1989), tandis que la fusion gloutonne de SME opère en temps polynomial sans garantie d'optimum global (Forbus et al., 2017). *Échecs* : dépend d'une formalisation prédicative préalable lourde et, dans sa version canonique, de l'identité des prédicats relationnels — ce qui déplace le problème du changement de vocabulaire vers un encodage manuel biaisable.

---

### 3. Symétrie, conservation et statut d'un « Noether discret »

- **Automorphismes ($\mathrm{Aut}(G)$)** : symétries globales d'un graphe ; leurs orbites définissent des rôles structurels équivalents, mais les réseaux scientifiques réels sont génériquement rigides ($\mathrm{Aut}(G)=\{\mathrm{id}\}$).
- **Groupoïdes de symétries** : formalisent les symétries locales ou partielles entre sous-structures isomorphes (Weinstein, 1996), mieux adaptées aux réseaux modulaires hétérogènes.
- **Invariants de graphes** : spectre, densités de motifs (Lovász, 2012), signatures de Weisfeiler-Leman ($k$-WL). Ils sont invariants sous *réétiquetage*, statiques (sans conservation dynamique) et incomplets en temps polynomial (échec de la hiérarchie $k$-WL démontré par Cai, Fürer & Immerman, 1992).
- **Naturalité catégorique** : une transformation naturelle $\eta:F\Rightarrow G$ entre foncteurs $\mathcal{C}\to\mathcal{D}$ satisfait $G(f)\circ\eta_A=\eta_B\circ F(f)$ pour tout morphisme $f:A\to B$ (Mac Lane, 1998). Elle généralise l'équivariance aux transformations non inversibles ; le lemme de Yoneda établit en outre qu'un objet est déterminé à isomorphisme près par son réseau relationnel.

**Existe-t-il un énoncé de type Noether discret applicable ici ?**
- *Ce qui est démontré* : le théorème de Noether classique associe une symétrie continue (groupe de Lie) d'une fonctionnelle d'action variationnelle à une loi de conservation (Noether, 1918). En discret, des énoncés rigoureux existent mais exigent une *dynamique* explicite : (i) en mécanique variationnelle discrète, l'invariance d'un lagrangien discret sous un groupe de Lie continu implique la conservation exacte d'un moment discret (Marsden & West, 2001) ; (ii) pour un processus de Markov en temps continu sur un espace d'états discret, un théorème de Noether relie symétries uniparamétriques du générateur (sous réversibilité / bilan détaillé) et observables conservés (Baez & Fong, 2013).
- *Ce qui est spéculatif* : sur un **réseau de concepts statique et discret**, aucun théorème de type Noether n'est démontré. Deux conditions font défaut : une dynamique canonique (variationnelle ou génératrice) et le caractère infinitésimal des symétries. Présenter une analogie de graphes comme une loi de conservation noethérienne demeure donc une métaphore heuristique tant qu'aucune dynamique explicite d'inférence ou de modèle n'est spécifiée.

---

### 4. Avant la découverte : détection datée et circularité

Pour détecter à une date $t<t^*$ (avant publication du lien à $t^*$) qu'un changement de représentation $R\to R'$ accroît la qualité du meilleur alignement entre deux domaines $D_1$ et $D_2$, le protocole doit être strictement causal dans le temps.

- **Données datées.** Archives scientifiques horodatées (*arXiv*, *PubMed*, métadonnées *OpenAlex*) filtrées strictement à $\le t$. Suivant le principe d'isolement de Swanson (1986), tout article, auteur ou co-citation reliant déjà $D_1$ et $D_2$ est écarté. On construit deux couches de graphes : des graphes typés de relations conceptuelles et des graphes syntaxiques d'opérateurs/équations ou schémas causaux.
- **Calcul.** On détecte la transition $R\to R'$ de manière *endogène* dans $D_1$ seul (rupture de formalisme, de modularité interne ou de longueur de description, sans jamais consulter $D_2$). On mesure ensuite le gain différentiel d'alignement purement structurel (GW entropique non équilibré sur matrices de distances orientées, sans identité lexicale) :
  $$\Delta S_t = S\!\big(G_1^{(R')}(t), G_2(t)\big) - S\!\big(G_1^{(R)}(t), G_2(t)\big),$$
  standardisé par rapport à la distribution de paires témoins $(D_1,D_{\text{ctrl}})$ à la même date $t$ et à des modèles nuls à séquence de degrés conservée.
- **Risques de circularité.** Quatre biais peuvent fabriquer une détection illusoire : (i) *fuite temporelle*, si un extracteur LLM entraîné après $t^*$ homogénéise clandestinement les vocabulaires de $D_1$ et $D_2$ ; (ii) *ingénierie ontologique rétrospective*, si les types $T$ ou la date de $R'$ sont choisis en connaissant $t^*$ ; (iii) *artefact de densité*, un formalisme plus compact améliorant mécaniquement le score GW envers n'importe quel domaine ; (iv) *ponts latents* via des métaphores informelles préexistantes. Les garde-fous sont l'extraction syntaxique/symbolique déterministe sans modèle post-$t^*$, la détection aveugle de $R'$, l'appariement de densité des témoins et l'exclusion bibliographique stricte.

---

### 5. Expérience minimale et critère de réfutation

- **Données.** Un banc pré-enregistré de $K$ paires historiques $(D_1,D_2)$ reliées à une date $t^*$ documentée (ponts d'équations de type gravité analogue ou physique statistique/inférence), apparié à deux groupes témoins de taille et densité comparables : des paires négatives sans lien publié et des paires d'analogies heuristiques demeurées stériles (témoins de faux positifs). Sur textes $\le t<t^*$, sans aucun modèle pré-entraîné après $t^*$, une analyse syntaxique déterministe et un parseur symbolique d'équations génèrent $G^{\text{conc}}(t)$ (proposition initiale : graphe conceptuel typé) et $G^{\text{op}}(t)$ (proposition de remplacement : graphe d'opérateurs/structures causales).
- **Algorithme.** Filtrage anti-pont (Swanson, 1986) ; calcul de l'alignement purement structurel par GW entropique non équilibré sur distances orientées (Mémoli, 2011 ; Peyré, Cuturi & Solomon, 2016 ; Séjourné, Vialard & Peyré, 2021) ; normalisation par permutations sur témoins appariés à la date $t$ ; suivi du gain $\Delta S_t$ après transitions endogènes $R\to R'$.
- **Prédiction et seuil.** Tests unilatéraux corrigés pour comparaisons multiples par contrôle du taux de fausses découvertes (Benjamini & Hochberg, 1995) au niveau prédéfini $\alpha$ fixé lors du pré-enregistrement. La proposition initiale prédit $q<\alpha$ et un gain $\Delta S_t$ significativement supérieur aux témoins sur $G^{\text{conc}}(t)$ avant $t^*$. Notre critique prédit l'échec de $G^{\text{conc}}(t)$ et la supériorité significative de $G^{\text{op}}(t)$ pour discriminer les découvertes fécondes à la fois des paires négatives et des analogies stériles.
- **Résultat réfutateur.** La proposition initiale est **réfutée** si, sans fuite temporelle, $G^{\text{conc}}(t)$ ne dépasse pas le niveau de chance ($q\ge\alpha$) ou si son gain $\Delta S_t$ ne distingue pas vraies paires et témoins de même densité. Notre proposition de remplacement ($G^{\text{op}}$) est elle-même **réfutée** si elle ne surpasse pas $G^{\text{conc}}$ ou si les analogies stériles obtiennent des scores équivalents ou supérieurs aux découvertes avérées à taille contrôlée.

---

### Références

- Baez, J. C., & Fong, B. (2013). « A Noether Theorem for Markov Processes ». *Journal of Mathematical Physics*, 54(1), 013301.
- Beckers, S., & Halpern, J. Y. (2019). « Abstracting Causal Models ». *Proceedings of the AAAI Conference on Artificial Intelligence*, 33(01), 2678–2685.
- Benjamini, Y., & Hochberg, Y. (1995). « Controlling the False Discovery Rate: A Practical and Powerful Approach to Multiple Testing ». *Journal of the Royal Statistical Society: Series B*, 57(1), 289–300.
- Burns, C., Ye, H., Klein, D., & Steinhardt, J. (2023). « Discovering Latent Knowledge in Language Models Without Supervision ». *International Conference on Learning Representations (ICLR)*.
- Cai, J.-Y., Fürer, M., & Immerman, N. (1992). « An Optimal Lower Bound on the Number of Variables for Graph Identification ». *Combinatorica*, 12(4), 389–410.
- Cohen, T. S., & Welling, M. (2016). « Group Equivariant Convolutional Networks ». *Proceedings of the 33rd International Conference on Machine Learning (ICML)*, PMLR 48, 2990–2999.
- Ehrig, H., Ehrig, K., Prange, U., & Taentzer, G. (2006). *Fundamentals of Algebraic Graph Transformation*. Berlin : Springer.
- Falkenhainer, B., Forbus, K. D., & Gentner, D. (1989). « The Structure-Mapping Engine: Algorithm and Examples ». *Artificial Intelligence*, 41(1), 1–63.
- Forbus, K. D., Ferguson, R. W., Lovett, A., & Gentner, D. (2017). « Extending SME to Handle Large-Scale Cognitive Modeling ». *Cognitive Science*, 41(5), 1152–1201 (numéro et pagination à vérifier).
- Gentner, D. (1983). « Structure-Mapping: A Theoretical Framework for Analogy ». *Cognitive Science*, 7(2), 155–170.
- Hell, P., & Nešetřil, J. (2004). *Graphs and Homomorphisms*. Oxford : Oxford University Press.
- Lovász, L. (2012). *Large Networks and Graph Limits*. Providence : American Mathematical Society.
- Mac Lane, S. (1998). *Categories for the Working Mathematician* (2e éd.). New York : Springer.
- Marsden, J. E., & West, M. (2001). « Discrete Mechanics and Variational Integrators ». *Acta Numerica*, 10, 357–514.
- Mémoli, F. (2011). « Gromov–Wasserstein Distances and the Metric Approach to Object Matching ». *Foundations of Computational Mathematics*, 11(4), 417–487.
- Newton, I. (1687). *Philosophiæ Naturalis Principia Mathematica*. Londres : Jussu Societatis Regiæ ac Typis Josephi Streater.
- Noether, E. (1918). « Invariante Variationsprobleme ». *Nachrichten von der Gesellschaft der Wissenschaften zu Göttingen, Mathematisch-Physikalische Klasse*, 1918, 235–257.
- Peyré, G., Cuturi, M., & Solomon, J. (2016). « Gromov-Wasserstein Averaging of Kernel and Distance Matrices ». *Proceedings of the 33rd International Conference on Machine Learning (ICML)*, PMLR 48, 2664–2672.
- Riesen, K., & Bunke, H. (2009). « Approximate Graph Edit Distance Computation by Means of Bipartite Graph Matching ». *Image and Vision Computing*, 27(7), 950–959.
- Sahni, S., & Gonzalez, T. (1976). « P-Complete Approximation Problems ». *Journal of the ACM*, 23(3), 555–565.
- Sanders, R. D., Tononi, G., Laureys, S., & Sleigh, J. W. (2012). « Unresponsiveness ≠ Unconsciousness ». *Anesthesiology*, 116(4), 946–959.
- Sanfeliu, A., & Fu, K.-S. (1983). « A Distance Measure Between Attributed Relational Graphs for Pattern Recognition ». *IEEE Transactions on Systems, Man, and Cybernetics*, SMC-13(3), 353–362.
- Séjourné, T., Vialard, F.-X., & Peyré, G. (2021). « The Unbalanced Gromov Wasserstein Distance: Conic Formulation and Relaxation ». *Advances in Neural Information Processing Systems (NeurIPS)*, 34 (pagination à vérifier).
- Spivak, D. I., & Kent, R. E. (2012). « Ologs: A Categorical Framework for Knowledge Representation ». *PLoS ONE*, 7(1), e24274.
- Swanson, D. R. (1986). « Fish Oil, Raynaud's Syndrome, and Undiscovered Public Knowledge ». *Perspectives in Biology and Medicine*, 30(1), 7–18.
- Unruh, W. G. (1981). « Experimental Black-Hole Evaporation? ». *Physical Review Letters*, 46(21), 1351–1353.
- Vayer, T., Chapel, L., Flamary, R., Tavenard, R., & Courty, N. (2020). « Fused Gromov-Wasserstein Distance for Structured Objects ». *Algorithms*, 13(9), 212 (numéro d'article à vérifier).
- Weinstein, A. (1996). « Groupoids: Unifying Internal and External Symmetry — A Tour through Some Examples ». *Notices of the American Mathematical Society*, 43(7), 744–752.
- Zeng, Z., Tung, A. K. H., Wang, J., Feng, J., & Zhou, L. (2009). « Comparing Stars: On Approximating Graph Edit Distance ». *Proceedings of the VLDB Endowment*, 2(1), 25–36.