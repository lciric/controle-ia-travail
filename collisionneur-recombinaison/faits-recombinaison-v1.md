# Faits pour le collisionneur — trancher l'étage de recombinaison bisociative (v1)

Statut : **RAPPORTÉ** (pièces du programme, transcrites telles quelles). Aucun sigle de financeur. Aucun score de pilote.
Rien ici n'est une consigne. C4 (test « ponts plantés » de conv-audit) **non rendu au départ du tour** : absent.

<<<DÉBUT C1 — rapport de méta-conception v6.3 (copie neutre)>>>
> Copie neutre du rapport de méta-conception v6.3 de l'essaim de Gemini (commit `5512513`, branche `canal/gemini-organisme-v6-2-1-relais-gen8`, fichier `RAPPORT-META-CONCEPTION-V6-3-FABLE-OPUS-ARGON.md`, sha256 `96d12112c8d8d7e3…` à l'origine), faite par conv-audit le 26 octobre 2026 : 0 occurrence(s) du sigle du financeur remplacée(s) par « [sigle retiré] » ; rien d'autre n'est changé.

# Réponse de l'essaim à la question ouverte

## Question posée

> META-CONCEPTION DE L'ORGANISME V6.2.1 ('LA FUSEE') — QUESTION DIRECTE DE LAZAR CIRIC :
« Si on tire au hasard des articles avec l'organisme (enfin pas tout à fait au hasard), comment faire pour favoriser les associations d'idées nouvelles qui peuvent se combiner ensemble ? C'est comme un processus de tirage et de recherche d'associations sur les éléments tirés : comment peut-on optimiser ça dans ta propre conception pour rendre la recherche d'associations la plus fertile possible, c'est-à-dire qui marchent vraiment et donnent des résultats expérimentaux concrets ? »

Rappel de tes 3 modules actuels (`v6.2.1`) :
- `principal.py` : moissonnage sur 4 sources (`arxiv`, `openalex`, `semanticscholar`, `web`) et tri par `_score_pertinence_texte` (recouvrement lexical avec la question + mots-clés 'theorem', 'bound', 'proof').
- `mitose_spectrale.py` : matrice de Gram `G_ij`, capacité de Shannon `0.5 * log det(I + SNR * G)` par Cholesky, extraction de `termes_satures` et répulsion d'Onsager.
- `memoire_isvd.py` : projection de Koopman `[v, sin(v), v^2]` par hachage SHA-256 en dimension 16, SVD de Jacobi de rang 6, bonus `+15 %` multi-familles et archive *Stepping Stones*.

CONSIGNE POUR FABLE, OPUS ET GEMINI 4 ARGON :
1) Identifie les limites mathématiques exactes de `_score_pertinence_texte`, du hachage SHA-256 d'`isvd` et de la répulsion lexicale de `mitose_spectrale`.
2) Formule la loi mathématique optimale de tirage conjoint de paires/k-uplets d'articles (DPP bilinéaire Domaine x Opérateur, bandit contextuel de ponts de Swanson A<->B<->C, synergie d'information mutuelle de Williams-Beer) et l'opérateur de synthèse par somme amalgamée (pushout catégoriel B o A).
3) Donne le plan d'implémentation exact en Python pur (sans dépendance externe, respectant C-01 à C-17) pour la future `v6.3` ainsi que 4 protocoles falsifiables (avec Métrique, Seuil chiffré et Coût <= 5 $) pour prouver le gain de fertilité de la `v6.3` sur la `v6.2.1`.

## 1. Réponse finale

**Conclusion retenue (confiance agrégée : `0.808`) :** Remplacement du tri lexical v6.2.1 par un pipeline v6.3 en Python pur combinant SimHash sur n-grammes avec normalisation spherique pre-Koopman, tirage DPP bilineaire Domaine x Operateur regularise par Sinkhorn-Knopp, repulsion d'Onsager sur graphe de ligne pour preserver les pivots de Swanson, et synthese par pushout categoriel sous filtre de compatibilite des contraintes.

### 1. Réponse finale consolidée de l'essaim : Architecture bisociative `v6.3`

Pour maximiser la fertilité expérimentale des associations d'idées, la `v6.3` remplace le filtrage unaire de la `v6.2.1` par un pipeline algébrique et catégoriel en quatre étages, implémentable en Python pur :

1. **Encodage et Mémoire ISVD régularisée (`memoire_isvd.py`)** : Le hachage cryptographique SHA-256 (qui détruit la topologie locale par effet d'avalanche) est remplacé par un **SimHash morphologique** sur $n$-grammes de caractères, séparant chaque article $i$ en deux vecteurs unitaires ($\|v\|_2 = 1$) : Domaine ($d_i \in \mathbb{R}^{16}$) et Opérateur ($o_i \in \mathbb{R}^{16}$, filtré sur le lexique mathématique/méthodologique). Cette normalisation sphérique empêche le terme quadratique $v^2$ de l'expansion de Koopman $[v, \sin(v), v^2]$ d'écraser le spectre ($\sigma_1 = 269.0 \gg \sigma_6 = 4.41$).
2. **Tirage conjoint par DPP bilinéaire régularisé par Sinkhorn-Knopp (`principal.py`)** : Au lieu du tri séparable `_score_pertinence_texte`, la sélection d'un sous-ensemble $S$ de $k$ articles suit un Processus Ponctuel Déterminantal $\mathbb{P}(S) \propto \det(L_S)$. Le noyau $L_{ij} = q_i q_j \cdot \langle o_i, o_j \rangle^2 \cdot (1 - \langle d_i, d_j \rangle^2)$ est garanti semi-défini positif (PSD) par produit de Schur. Pour éviter l'effondrement modal en régime creux ($n \approx 20$) et la domination des hubs méthodologiques génériques (ex. GNN, *Art.7–12*), $L$ subit 5 itérations d'équilibrage bistochastique de **Sinkhorn-Knopp** et une régularisation de Tikhonov ($L \leftarrow \text{Sinkhorn}(L) + \gamma I$).
3. **Répulsion sur graphe de ligne et Bandit de Swanson (`mitose_spectrale.py`)** : La répulsion d'Onsager est déplacée des mots isolés vers les *arêtes* du graphe de ligne (paires conceptuelles co-occurrentes, inspiré d'ALIGNN, *Art.10*). Cela préserve les termes-pivots $B$ nécessaires aux ponts de Swanson $A \leftrightarrow B \leftrightarrow C$ (*Art.11*), explorés par un bandit UCB1 pondérant la synergie de Williams-Beer (estimée par l'écart d'entropie de Shannon $\log\det$ jointe vs marginale via Cholesky) et le bonus *Stepping Stones* (+15 %).
4. **Synthèse par Pushout Catégoriel filtré** : Deux articles tirés $(A, C)$ ne sont fusionnés en somme amalgamée $A \sqcup_B C$ (blending conceptuel sans perte de structure, *Art.4, Art.6*) que si l'interface opératoire $B = O_A \cap O_C$ est non vide et satisfait un filtre de compatibilité des contraintes (absence de contradictions d'hypothèses comme *linéaire/non-linéaire* ou *stationnaire/transitoire*, cf. *R1, R3*).

**Plan d'implémentation Python pur (C-01 à C-17) et Protocoles falsifiables ($\le 5\$$) :**
* *Implémentation (`math`, `hashlib`, `random`)* : Remplacer `_score_pertinence_texte` par `_tirage_dpp_sinkhorn(articles, k=4)` utilisant la décomposition de Cholesky existante de `mitose_spectrale.py` pour l'échantillonnage glouton map-DPP et le calcul d'information mutuelle.
* **P1 (Stabilité spectrale ISVD)** : Ratio de conditionnement $\sigma_1/\sigma_6$ sur 50 cycles. Seuil : passage de $60.9$ (`v6.2.1`) à $\le 12.0$ grâce à la normalisation sphérique pré-Koopman (Coût : $0\$$).
* **P2 (Fertilité inter-domaines)** : Taux de paires tirées avec chevauchement de domaine $\langle d_i, d_j \rangle < 0.25$ et couplage d'opérateur $\langle o_i, o_j \rangle > 0.50$. Seuil : $\ge 45\%$ contre $< 10\%$ en `v6.2.1` (Coût : $1.20\$$ API).
* **P3 (Rétention des ponts de Swanson)** : Recall@5 sur 20 triades historiques reconstruites $(A, B, C)$ en masquant $A \leftrightarrow C$. Seuil : $\ge 60\%$ de redécouverte du pivot $B$ sans suppression par Onsager (Coût : $2.00\$$).
* **P4 (Validité expérimentale du Pushout)** : Taux de protocoles synthétisés compilables et non contradictoires évalués à l'aveugle sur 30 tirages. Seuil : gain net $\ge +30\%$ sur `v6.2.1` (Coût : $1.80\$$).

---

### 2. Raisonnement contradictoire et arbitrage des castes

L'arbitrage fait émerger une synthèse stricte en croisant les quatre critiques :
* **Fable (#1) vs Argon (#2)** : Fable pose la fondation théorique (DPP Domaine×Opérateur, UCB Swanson, Williams-Beer, Pushout), mais Argon démontre que le noyau bilinéaire naïf n'est pas PSD (faisant échouer Cholesky dans `mitose_spectrale.py`), que SHA-256 détruit la géométrie par effet d'avalanche, et que la répulsion d'Onsager actuelle élimine les pivots $B$ de Swanson en les traitant comme des `termes_satures`. L'adoption du produit de Schur, du SimHash et du graphe de ligne d'Argon résout ces trois défauts.
* **Opus (#3) et Fable-Critique (#4) vs le consensus (#1/#2)** : Opus prouve qu'en régime réel ($n \approx 12\text{--}30$ articles moissonnés), un DPP standard dégénère en un top-$k$ déterministe dominé par 2 ou 3 valeurs propres. Cependant, sa marche aléatoire pondérée par l'IDF est réfutée par la Caste #4 : elle s'effondre sur les « hubs méthodologiques » génériques et n'explique pas l'explosion spectrale de Koopman ($\sigma_1 = 269.0$) due à l'absence de normalisation avant $v^2$. L'intégration de la normalisation sphérique, de l'équilibrage de Sinkhorn-Knopp et du filtre de compatibilité des contraintes (Caste #4) stabilise le DPP à petit $n$ tout en garantissant que le pushout catégoriel ne fusionne pas des formalismes incompatibles.

---

### 3. Points d'incertitude résiduels de l'essaim

1. **Pauvreté des résumés courts** : Sans accès au texte intégral ni parseur syntaxique lourd (contrainte Python pur), l'extraction par heuristiques lexicales des contraintes de domaine et des opérateurs sur des résumés de moins de 150 mots risque de laisser l'interface du pushout $B$ vide ou bruitée dans $25\%$ à $35\%$ des tirages.
2. **Synergie non-lexicale** : L'estimation de la synergie de Williams-Beer par déterminant de Gram sur n-grammes peut sous-évaluer l'isomorphisme structurel entre deux articles aux notations mathématiques totalement disjointes.

## 2. Raisonnement qui y mène

L'essaim a procédé par mitose adaptative, répulsion spectrale des concepts saturés et arbitrage contradictoire :
- **Capacité de Shannon-Gram de la délibération** : `3.618972` (gain marginal : `0.723794`, similarité inter-castes : `0.305903`).
- **Termes saturés soumis à répulsion orthogonale** : `['article', 'aux', 'bruit', 'cholesky', 'confiance', 'dans']`.
- **Moissonnage documentaire endogène** : `36` références extraites et `3` documents téléchargés sur les requêtes `['computational creativity conceptual blending scientific discovery', 'literature based discovery graph neural networks link prediction', 'quality diversity algorithms MAP-Elites open-ended hypothesis generation', 'submodular optimization determinantal point processes diverse retrieval', 'active learning Bayesian optimization experimental design LLM', 'cross-domain analogy mining semantic graphs scientific innovation']`.

- **Étape Caste #1 (`monoculture_analytique`, espèce `CLAUDE_FABLE_5_1`, poids `0.1832`)** : Le remplacement de _score_pertinence_texte par un noyau DPP bilinéaire Domaine×Opérateur couplé à un bandit Swanson UCB et une synergie Williams-Beer approchée constitue la transformation mathématiquement fondée minimale pour rendre le moteur bisociatif de v6.3 fertile en associations inter-domaines non triviales, implémentable en Python pur.
- **Étape Caste #2 (`monoculture_croisee`, espèce `GEMINI_4_ARGON`, poids `0.2129`)** : Pour éviter l'indéfinition spectrale du noyau bilinéaire naïf et la destruction des termes-pivots de Swanson par la répulsion d'Onsager, la v6.3 doit utiliser un noyau de Schur strictement PSD couplant similarité d'opérateurs (via SimHash morphologique) et orthogonalité de domaines, tout en déplaçant la répulsion spectrale sur le graphe de ligne des transitions conceptuelles.
- **Étape Caste #3 (`sonde_orthogonale_onsager`, espèce `CLAUDE_OPUS`, poids `0.1782`)** : Le DPP dégénère en régime n≈20 articles et le hachage SHA-256 détruit les ponts de Swanson ; une marche aléatoire sur graphe biparti Concepts×Articles pondérée par IDF des concepts-ponts est plus robuste, implémentable en dict+random, et falsifiable par taux de paires inter-domaines ≥40%
- **Étape Caste #4 (`critique_adversariale_limites`, espèce `CLAUDE_FABLE_5_1`, poids `0.2079`)** : Les approches par graphe de ligne, DPP et marche IDF échouent face aux hubs méthodologiques, à la dérive quadratique du spectre de Koopman et aux obstructions de recollement du pushout catégoriel ; la v6.3 nécessite un équilibrage de Sinkhorn-Knopp couplé à un filtre de compatibilité des contraintes avant synthèse.
- **Étape Caste #5 (`arbitre_synthese_contradictoire`, espèce `GEMINI_4_ARGON`, poids `0.2178`)** : Remplacement du tri lexical v6.2.1 par un pipeline v6.3 en Python pur combinant SimHash sur n-grammes avec normalisation spherique pre-Koopman, tirage DPP bilineaire Domaine x Operateur regularise par Sinkhorn-Knopp, repulsion d'Onsager sur graphe de ligne pour preserver les pivots de Swanson, et synthese par pushout categoriel sous filtre de compatibilite des contraintes.

## 3. Ce qui vient de quelle caste

### Moissonneur documentaire endogène (`noyau_client.rechercher` / `telecharger`)
- **[arxiv] Seeing Differently: Modeling Interpretive Perspectives in Computational Creativity using a Four-World Framework** (2026-05-28, `2607.28644v1`) : Creativity in computational systems is often evaluated as an objective property of artifacts, with existing Computational Creativity (CC) frameworks assessing creative merit at the level of outputs or systems rather than interpretive context. However, artistic meaning is inherently perspective-dependent and can vary across viewers and critical traditions. This paper proposes a computational approach to modeling inter
- **[arxiv] IPPOG : Bridging the gap between science education at school and modern scientific research** (2020-11-30, `2011.14743v1`) : The International Particle Physics Outreach Group (IPPOG) has been making concerted and systematic efforts to present and popularise particle physics across all audiences and age groups since 1997. Today the scientific community has in IPPOG a strategic pillar in fostering long-term, sustainable support for fundamental research around the world. One of the main tools IPPOG has been offering to the scientific communit
- **[arxiv] Ethics and Creativity in Computer Vision** (2021-12-06, `2112.03111v1`) : This paper offers a retrospective of what we learnt from organizing the workshop *Ethical Considerations in Creative applications of Computer Vision* at CVPR 2021 conference and, prior to that, a series of workshops on *Computer Vision for Fashion, Art and Design* at ECCV 2018, ICCV 2019, and CVPR 2020. We hope this reflection will bring artists and machine learning researchers into conversation around the ethical an
- **[arxiv] Imagine for Me: Creative Conceptual Blending of Real Images and Text via Blended Attention** (2025-06-30, `2506.24085v2`) : Blending visual and textual concepts into a new visual concept is a unique and powerful trait of human beings that can fuel creativity. However, in practice, cross-modal conceptual blending for humans is prone to cognitive biases, like design fixation, which leads to local minima in the design space. In this paper, we propose a T2I diffusion adapter "IT-Blender" that can automate the blending process to enhance human
- **[arxiv] Creative Data Generation: A Review Focusing on Text and Poetry** (2023-05-15, `2305.08493v2`) : The rapid advancement in machine learning has led to a surge in automatic data generation, making it increasingly challenging to differentiate between naturally or human-generated data and machine-generated data. Despite these advancements, the generation of creative data remains a challenge. This paper aims to investigate and comprehend the essence of creativity, both in general and within the context of natural lan
- **[arxiv] An Argument-based Creative Assistant for Harmonic Blending** (2016-03-06, `1603.01770v1`) : Conceptual blending is a powerful tool for computational creativity where, for example, the properties of two harmonic spaces may be combined in a consistent manner to produce a novel harmonic space. However, deciding about the importance of property features in the input spaces and evaluating the results of conceptual blending is a nontrivial task. In the specific case of musical harmony, defining the salient featur
- **[openalex] Neural networks for link prediction in realistic biomedical graphs: a multi-dimensional evaluation of graph embedding-based approaches** (2018, `https://openalex.org/W2804186728`) : BACKGROUND: Link prediction in biomedical graphs has several important applications including predicting Drug-Target Interactions (DTI), Protein-Protein Interaction (PPI) prediction and Literature-Based Discovery (LBD). It can be done using a classifier to output the probability of link formation between nodes. Recently several works have used neural networks to create node representations which allow rich inputs to 
- **[openalex] Benchmarking Graph Neural Networks** (2020, `https://openalex.org/W3007332492`) : In the last few years, graph neural networks (GNNs) have become the standard toolkit for analyzing and learning from data on graphs. This emerging field has witnessed an extensive growth of promising techniques that have been applied with success to computer science, mathematics, biology, physics and chemistry. But for any successful field to become mainstream and reliable, benchmarks must be developed to quantify pr
- **[openalex] Advanced graph and sequence neural networks for molecular property prediction and drug discovery** (2022, `https://openalex.org/W3120618935`) : MOTIVATION: Properties of molecules are indicative of their functions and thus are useful in many applications. With the advances of deep-learning methods, computational approaches for predicting molecular properties are gaining increasing momentum. However, there lacks customized and advanced methods and comprehensive tools for this task currently. RESULTS: Here, we develop a suite of comprehensive machine-learning 
- **[openalex] Atomistic Line Graph Neural Network for improved materials property predictions** (2021, `https://openalex.org/W3212512279`) : Abstract Graph neural networks (GNN) have been shown to provide substantial performance improvements for atomistic material representation and modeling compared with descriptor-based machine learning models. While most existing GNN models for atomistic predictions are based on atomic distance information, they do not explicitly incorporate bond angles, which are critical for distinguishing many atomic structures. Fur
- **[openalex] Improving Automated Literature-based Discovery with Neural Networks: Neural biomedical Named Entity Recognition, Link Prediction and Discovery** (2019, `https://openalex.org/W2951092820`) : Literature-based Discovery (LBD) uses information from explicit statements in literature to generate new or unstated knowledge. Automated LBD can thus facilitate hypothesis testing and generation from large collections of publications to support and accelerate scientific research, which is adversely affected by publication explosion and knowledge fragmentation. Existing methods, however, use methodologies which are i
- **[openalex] Prediction of protein–protein interaction using graph neural networks** (2022, `https://openalex.org/W4280617006`) : Proteins are the essential biological macromolecules required to perform nearly all biological processes, and cellular functions. Proteins rarely carry out their tasks in isolation but interact with other proteins (known as protein-protein interaction) present in their surroundings to complete biological activities. The knowledge of protein-protein interactions (PPIs) unravels the cellular behavior and its functional
- **[Document téléchargé : `http://arxiv.org/abs/2607.28644v1`]** Source http://arxiv.org/abs/2607.28644v1 : https://arxiv.org/api/v03riQ2gdBboDY4j8x18qxfX0ss arXiv Query: search_query=&amp;id_list=2607.28644v1&amp;start=0&amp;max_results=10 2026-10-26T17:01:57Z 10 1 0 http://arxiv.org/abs/2607.28644v1 Seeing Differently: Modeling Interpretive Perspectives in Computational Creativity using a Four-World Framework 2026-05-28T04:02:54Z Creativity in computational systems is often evaluated as an objective property of artifacts, with existing Computational Creativity (CC) frameworks assessing creative merit at the level of outputs or systems rather than interpretive context. However, artistic meaning is 
- **[Document téléchargé : `http://arxiv.org/abs/2011.14743v1`]** Source http://arxiv.org/abs/2011.14743v1 : https://arxiv.org/api/IrN7yPMFR1grIkApUoJCdqiPXWQ arXiv Query: search_query=&amp;id_list=2011.14743v1&amp;start=0&amp;max_results=10 2026-10-26T17:01:57Z 10 1 0 http://arxiv.org/abs/2011.14743v1 IPPOG : Bridging the gap between science education at school and modern scientific research 2020-11-30T12:56:40Z The International Particle Physics Outreach Group (IPPOG) has been making concerted and systematic efforts to present and popularise particle physics across all audiences and age groups since 1997. Today the scientific community has in IPPOG a strategic pillar in fostering long-term, sustain
- **[Document téléchargé : `http://arxiv.org/abs/2112.03111v1`]** Source http://arxiv.org/abs/2112.03111v1 : https://arxiv.org/api/nXlGoNLYg5lYxRQWKbL0kIRiOVs arXiv Query: search_query=&amp;id_list=2112.03111v1&amp;start=0&amp;max_results=10 2026-10-26T17:01:57Z 10 1 0 http://arxiv.org/abs/2112.03111v1 Ethics and Creativity in Computer Vision 2021-12-06T15:23:08Z This paper offers a retrospective of what we learnt from organizing the workshop *Ethical Considerations in Creative applications of Computer Vision* at CVPR 2021 conference and, prior to that, a series of workshops on *Computer Vision for Fashion, Art and Design* at ECCV 2018, ICCV 2019, and CVPR 2020. We hope this reflection will bring art

### Caste #1 — `monoculture_analytique` (espèce : `CLAUDE_FABLE_5_1`, mode : `MONOCULTURE`, confiance : `0.74`)
- **Axe d'exploration** : Analyse initiale et decomposition formelle de la question
- **Thèse** : Le remplacement de _score_pertinence_texte par un noyau DPP bilinéaire Domaine×Opérateur couplé à un bandit Swanson UCB et une synergie Williams-Beer approchée constitue la transformation mathématiquement fondée minimale pour rendre le moteur bisociatif de v6.3 fertile en associations inter-domaines non triviales, implémentable en Python pur.
- **Contribution** :

# Analyse formelle : Méta-conception du moteur bisociatif v6.3

## 1. Chaîne de raisonnement et réponse structurée

### 1.1 Limites mathématiques exactes des trois modules actuels

**`_score_pertinence_texte`** opère par recouvrement lexical (intersection de sacs de mots normalisés). Sa limite fondamentale est l'absence de géométrie sémantique : deux articles partageant zéro token mais occupant des régions voisines dans l'espace conceptuel reçoivent un score nul. Formellement, si `s(A,Q) = |V_A ∩ V_Q| / |V_Q|`, alors `s` est une pseudo-métrique de Jaccard dégénérée — symétrique mais aveugle aux synonymies et aux analogies structurelles inter-domaines. C'est précisément là que la bisociation (Koestler) échoue : les ponts les plus fertiles relient des vocabulaires *disjoints*.

**`memoire_isvd.py` / SHA-256** : le hachage SHA-256 vers ℝ¹⁶ est une projection *aléatoire non contrôlée*. La propriété de Johnson-Lindenstrauss garantit la préservation des distances euclidiennes pour des vecteurs denses, mais ici les vecteurs d'entrée sont des entiers de hachage — leur géométrie est uniforme par construction cryptographique, donc *maximalement non-informative* pour la similarité sémantique. La projection de Koopman `[v, sin(v), v²]` introduit une non-linéarité, mais appliquée à du bruit uniforme, elle produit un espace de features pseudo-aléatoire sans structure exploitable. Le bonus `+15 % multi-familles` est heuristique non fondé analytiquement.

**`mitose_spectrale.py` / répulsion d'Onsager** : la matrice de Gram `G_ij` est construite sur des vecteurs TF-IDF ou lexicaux, donc souffre du même biais lexical que `_score_pertinence_texte`. La capacité de Shannon `0.5 * log det(I + SNR * G)` mesure la diversité *lexicale* du corpus sélectionné, non la diversité *structurelle* des opérateurs mathématiques ou des méthodes. La répulsion d'Onsager évite les doublons terminologiques mais pas les redondances conceptuelles profondes.

### 1.2 Loi optimale de tirage conjoint et opérateur de synthèse

**DPP bilinéaire Domaine × Opérateur** : le tirage d'un k-uplet `{a₁,...,aₖ}` devrait suivre une distribution déterminantale `P({a₁,...,aₖ}) ∝ det(L_S)` où `L` est un noyau de qualité-diversité bilinéaire :

```
L_ij = q(aᵢ) · φ(aᵢ)ᵀ · φ(aⱼ) · q(aⱼ)
```

avec `q(a)` = score de qualité (pertinence à la question), et `φ(a)` = vecteur de *signature opératoire* de l'article (type de preuve, structure de l'opérateur principal : variationnel, spectral, stochastique, topologique). En Python pur, `φ` peut être approximé par un dictionnaire de motifs syntaxiques extraits par regex sur l'abstract (termes `"gradient"`, `"eigenvalue"`, `"martingale"`, `"sheaf"`, etc.) normalisés en vecteur binaire de dimension ~50. Le déterminant de la sous-matrice `k×k` se calcule par Cholesky incrémental — coût `O(k²·d)`, compatible C-01 à C-17.

**Bandit contextuel de ponts Swanson A↔B↔C** : chaque article est un nœud, une arête `(aᵢ, aⱼ)` porte un poids `w_ij = MI(Xᵢ ; Xⱼ | Q)` (information mutuelle conditionnelle à la question). En pratique, `MI` est approchée par cooccurrence de termes-ponts dans les abstracts : si `aᵢ` contient `{gradient, Onsager}` et `aⱼ` contient `{Onsager, optimal transport}`, le terme-pont `Onsager` crée un arc de valeur `log(P(Onsager|aᵢ,aⱼ) / P(Onsager|aᵢ)·P(Onsager|aⱼ))`. Le bandit UCB sélectionne à chaque génération le triplet `(A,B,C)` maximisant `Σ w_AB + w_BC + bonus_exploration / √n_tirages`.

**Synergie Williams-Beer** : la synergie `Syn(X₁;X₂→Y)` mesure l'information sur `Y` (la question) que `X₁` et `X₂` fournissent *ensemble* mais pas séparément. Approximation tractable en Python pur : `Syn ≈ MI(X₁,X₂;Y) - MI(X₁;Y) - MI(X₂;Y) + Red(X₁;X₂;Y)` où la redondance `Red` est bornée par `min(MI(X₁;Y), MI(X₂;Y))`. Cela identifie les paires dont la combinaison est super-additive — exactement les paires bisociatives fertiles.

**Pushout catégoriel `B ∘ A`** : l'opérateur de synthèse est une somme amalgamée dans la catégorie des espaces de concepts. Si `A` et `B` partagent un sous-concept `C` (terme-pont Swanson), le pushout `A ⊔_C B` est le nouvel espace conceptuel minimal contenant les deux et identifiant `C`. En Python, cela se traduit par la fusion de deux graphes de termes avec identification des nœuds-ponts et propagation des arêtes — implémentable avec des dictionnaires natifs.

### 1.3 Plan d'implémentation Python pur pour v6.3

```python
# MODULE: bisociation_dpp.py (v6.3)

import math, hashlib, re
from itertools import combinations

# --- Signature opératoire (φ) ---
OPERATEURS = [
    "gradient", "eigenvalue", "martingale", "sheaf", "kernel",
    "variational", "spectral", "stochastic", "topological", "optimal transport",
    "conformal", "Bayesian", "causal", "symplectic", "ergodic",
    "manifold", "entropy", "divergence", "Lagrangian", "Hamiltonian",
    "fixed point", "contraction", "measure", "cohomology", "diffusion"
]

def signature_operatoire(texte: str) -> list:
    """Vecteur binaire de présence d'opérateurs mathématiques."""
    t = texte.lower()
    return [1 if op in t else 0 for op in OPERATEURS]

def norme(v):
    n = math.sqrt(sum(x*x for x in v))
    return n if n > 0 else 1.0

def cosine(v1, v2):
    return sum(a*b for a,b in zip(v1,v2)) / (norme(v1) * norme(v2))

# --- Noyau DPP bilinéaire ---
def noyau_L(articles: list, scores_qualite: dict) -> list:
    """
    L_ij = q(i) * cos(phi_i, phi_j) * q(j)
    articles: liste de dicts avec 'id', 'texte'
    """
    n = len(articles)
    phis = [signature_operatoire(a['texte']) for a in articles]
    L = [[0.0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            qi = scores_qualite.get(articles[i]['id'], 1.0)
            qj = scores_qualite.get(articles[j]['id'], 1.0)
            L[i][j] = qi * cosine(phis[i], phis[j]) * qj
    return L

def det_sous_matrice(L, indices):
    """Déterminant par élimination de Gauss (Python pur, O(k^3))."""
    k = len(indices)
    M = [[L[i][j] for j in indices] for i in indices]
    det = 1.0
    for col in range(k):
        pivot = None
        for row in range(col, k):
            if abs(M[row][col]) > 1e-12:
                pivot = row; break
        if pivot is None: return 0.0
        M[col], M[pivot] = M[pivot], M[col]
        if col != pivot: det *= -1
        det *= M[col][col]
        for row in range(col+1, k):
            f = M[row][col] / M[col][col]
            for c in range(col, k):
                M[row][c] -= f * M[col][c]
    return abs(det)

# --- Termes-ponts Swanson ---
def extraire_termes(texte: str, top_n=20) -> set:
    tokens = re.findall(r'\b[a-z]{4,}\b', texte.lower())
    freq = {}
    for t in tokens:
        freq[t] = freq.get(t, 0) + 1
    triés = sorted(freq, key=lambda x: -freq[x])
    return set(triés[:top_n])

def poids_swanson(a1: dict, a2: dict) -> float:
    """Information mutuelle approchée par termes-ponts partagés."""
    t1 = extraire_termes(a1['texte'])
    t2 = extraire_termes(a2['texte'])
    ponts = t1 & t2
    if not ponts: return 0.0
    # Approximation: log(|ponts|+1) / log(|t1|+|t2|-|ponts|+1)
    return math.log(len(ponts) + 1) / math.log(len(t1) + len(t2) - len(ponts) + 2)

# --- Synergie Williams-Beer approchée ---
def synergie_wb(a1: dict, a2: dict, question_termes: set) -> float:
    """
    Syn ≈ MI(a1,a2;Q) - MI(a1;Q) - MI(a2;Q)
    approximé par recouvrement de termes-ponts avec Q
    """
    t1 = extraire_termes(a1['texte'])
    t2 = extraire_termes(a2['texte'])
    t12 = t1 | t2
    mi_joint = len(t12 & question_termes) / (len(question_termes) + 1)
    mi1 = len(t1 & question_termes) / (len(question_termes) + 1)
    mi2 = len(t2 & question_termes) / (len(question_termes) + 1)
    return mi_joint - mi1 - mi2  # positif = synergie, négatif = redondance

# --- Sélection DPP greedy de k articles ---
def selectionner_dpp_greedy(articles, scores_qualite, k=5):
    """
    Sélection greedy maximisant det(L_S) par ajout séquentiel.
    Complexité : O(n * k^3)
    """
    L = noyau_L(articles, scores_qualite)
    n = len(articles)
    selectionnes = []
    candidats = list(range(n))
    for _ in range(k):
        meilleur, meilleur_score = None, -1.0
        for c in candidats:
            indices = selectionnes + [c]
            score = det_sous_matrice(L, indices)
            if score > meilleur_score:
                meilleur_score = score
                meilleur = c
        if meilleur is None: break
        selectionnes.append(meilleur)
        candidats.remove(meilleur)
    return [articles[i] for i in selectionnes]

# --- Pushout catégoriel (fusion par termes-ponts) ---
def pushout_conceptuel(a1: dict, a2: dict) -> dict:
    """
    Somme amalgamée : graphe de termes fusionné avec identification des ponts.
    Retourne un dict représentant l'espace conceptuel hybride.
    """
    t1 = extraire_termes(a1['texte'], top_n=30)
    t2 = extraire_termes(a2['texte'], top_n=30)
    ponts = t1 & t2
    termes_a = t1 - ponts
    termes_b = t2 - ponts
    return {
        'ponts': ponts,
        'termes_a': termes_a,
        'termes_b': termes_b,
        'termes_fusionnes': t1 | t2,
        'score_fertilite': len(ponts) * math.log(len(termes_a) + len(termes_b) + 1)
    }

# --- Bandit UCB sur triplets Swanson ---
class BanditSwanson:
    def __init__(self):
        self.compteurs = {}   # (id1,id2): n_tirages
        self.recompenses = {} # (id1,id2): somme_recompenses

    def score_ucb(self, paire, w_base, t_total):
        n = self.compteurs.get(paire, 0)
        mu = self.recompenses.get(paire, 0.0) / (n + 1e-9)
        exploration = math.sqrt(2 * math.log(t_total + 1) / (n + 1))
        return mu + w_base * exploration

    def selectionner_triplet(self, articles, question_termes, t_total):
        meilleur_score = -1.0
        meilleur_triplet = None
        for i, j, k_idx in combinations(range(len(articles)), 3):
            a, b, c = articles[i], articles[j], articles[k_idx]
            w_ab = poids_swanson(a, b)
            w_bc = poids_swanson(b, c)
            syn = synergie_wb(a, c, question_termes)
            score = (self.score_ucb((a['id'],b['id']), w_ab, t_total) +
                     self.score_ucb((b['id'],c['id']), w_bc, t_total) +
                     syn)
            if score > meilleur_score:
                meilleur_score = score
                meilleur_triplet = (a, b, c)
        return meilleur_triplet

    def mettre_a_jour(self, paire, recompense):
        self.compteurs[paire] = self.compteurs.get(paire, 0) + 1
        self.recompenses[paire] = self.recompenses.get(paire, 0.0) + recompense
```

### 1.4 Quatre protocoles falsifiables

**Protocole P1 — Fertilité bisociative brute**
- *Métrique* : taux de paires `(aᵢ, aⱼ)` tirées avec `Syn_WB > 0` (synergie positive)
- *Seuil* : v6.3 ≥ 40 % de paires synergiques vs v6.2.1 ≤ 15 % (estimé)
- *Procédure* : 100 tirages de paires sur corpus fixe de 50 articles, calcul `Syn_WB` pour chaque paire
- *Coût* : 0 $ (calcul local)

**Protocole P2 — Diversité opératoire (DPP)**
- *Métrique* : entropie de Shannon sur la distribution des opérateurs `φ` dans les k-uplets sélectionnés : `H_op = -Σ p_op log p_op`
- *Seuil* : `H_op(v6.3) ≥ 1.5 * H_op(v6.2.1)` sur 50 sessions
- *Procédure* : comparer les sélections de k=5 articles par les deux versions sur même corpus
- *Coût* : 0 $

**Protocole P3 — Ponts Swanson validés par juge externe**
- *Métrique* : proportion de triplets `(A,B,C)` où B est reconnu comme terme-pont valide par GPT-4o (juge aveugle)
- *Seuil* : v6.3 ≥ 60 % de triplets validés vs baseline aléatoire ~20 %
- *Procédure* : 20 triplets soumis à GPT-4o avec prompt standardisé (coût ~0.10 $/triplet)
- *Coût* : 2 $

**Protocole P4 — Fertilité expérimentale réelle (Stepping Stones)**
- *Métrique* : nombre de nouvelles hypothèses archivées dans `stepping_stones` après 10 sessions de l'essaim
- *Seuil* : v6.3 produit ≥ 3 nouvelles hypothèses non-redondantes (cosine < 0.7) vs v6.2.1 ≥ 1
- *Procédure* : sessions parallèles sur même question avec les deux versions, déduplication par cosine sur signatures opératoires
- *Coût* : < 5 $ (appels API si nécessaire)

---

## 2. Incertitudes et limites

**Non vérifié** : l'approximation de `MI` par cooccurrence de termes-ponts est une heuristique — la vraie information mutuelle nécessiterait des distributions de probabilité sur l'espace conceptuel, inaccessibles sans embedding dense. La synergie Williams-Beer est ici une borne inférieure, pas la valeur exacte.

**Hypothèse non validée** : que la signature opératoire `φ` sur ~25 opérateurs capture suffisamment la diversité structurelle des méthodes mathématiques. Des articles en topologie algébrique et en apprentissage statistique peuvent partager le terme "cohomologie" sans aucune synergie réelle.

**Limite de scalabilité** : la sélection DPP greedy est `O(n·k³)` — pour `n=200` articles et `k=10`, cela représente ~2×10⁶ opérations, acceptable, mais le bandit sur triplets est `O(C(n,3))` = `O(n³/6)`, soit ~1.3×10⁶ pour `n=200` — limite haute pour Python pur sans NumPy.

**Condition de réfutation** : si P1 montre que v6.3 ne dépasse pas 25 % de paires synergiques, la thèse que le DPP bilinéaire améliore la bisociation est réfutée et il faudrait reconsidérer la définition de `φ`.

---

```json
{"position": "Le remplacement de _score_pertinence_texte par un noyau DPP bilinéaire Domaine×Opérateur couplé à un bandit Swanson UCB et une synergie Williams-Beer approchée constitue la transformation mathématiquement fondée minimale pour rendre le moteur bisociatif de v6.3 fertile en associations inter-domaines non triviales, implémentable en Python pur.", "confiance": 0.74, "incertitude": "L'approximation de MI par cooccurrence lexicale peut sous-estimer la synergie réelle entre articles de domaines très éloignés partageant peu de vocabulaire mais beaucoup de structure — le protocole P3 est le seul test empirique direct de cette limite."}
```

### Caste #2 — `monoculture_croisee` (espèce : `GEMINI_4_ARGON`, mode : `MONOCULTURE`, confiance : `0.86`)
- **Axe d'exploration** : Seconde perspective independante et verification des premisses
- **Thèse** : Pour éviter l'indéfinition spectrale du noyau bilinéaire naïf et la destruction des termes-pivots de Swanson par la répulsion d'Onsager, la v6.3 doit utiliser un noyau de Schur strictement PSD couplant similarité d'opérateurs (via SimHash morphologique) et orthogonalité de domaines, tout en déplaçant la répulsion spectrale sur le graphe de ligne des transitions conceptuelles.
- **Contribution** :

### 1) Réponse et chaîne de raisonnement : Vérification des prémisses et régularisation duale

**A. Pathologies cachées de `v6.2.1` et critique des prémisses de la Caste #1**
1. **`_score_pertinence_texte`** est une forme linéaire séparable $S(A) = \sum_{a \in A} s(a)$. Elle maximise la redondance intra-domaine et aveugle le tirage aux complémentarités opératoires.
2. **Hachage SHA-256 dans `memoire_isvd.py`** : Effet d'avalanche cryptographique ($\mathbb{E}[\langle h(w_1), h(w_2)\rangle] = 0$ pour $w_1 \neq w_2$). La non-linéarité de Koopman $[v, \sin(v), v^2]$ appliquée sur du bruit blanc amplifie la variance isotrope : le spectre ISVD ($\sigma_1 = 269.0 \gg \sigma_6 = 4.41$) capture la fréquence brute des tokens et détruit la topologie des graphes d'opérateurs.
3. **Répulsion d'Onsager dans `mitose_spectrale.py`** : Pénaliser les `termes_satures` au niveau atomique interdit la réutilisation des *termes-pivots* ($B$ dans le pont de Swanson $A \leftrightarrow B \leftrightarrow C$, [Art.7, Art.11]). Sans $B$, le poussé catégoriel s'effondre en produit libre disjoint (chimères).

*Contre-exemple à la Caste #1 :* Un noyau DPP bilinéaire $L = K_{\text{op}} \circ (J - K_{\text{dom}})$ n'est **pas garanti semi-défini positif (PSD)** car la matrice complémente $J - K_{\text{dom}}$ possède des valeurs propres négatives dès que le rang $> 1$, faisant échouer la factorisation de Cholesky. De plus, l'information mutuelle de Williams-Beer est sous-échantillonnée sur des résumés courts ($N < 200$ mots).

**B. Formulation mathématique corrigée : DPP sur Graphe de Ligne et Pushout Pondéré**
1. **Noyau L-ensemble PSD et Graphe de Ligne ([Art.10]) :** Pour garantir $L \succeq 0$, chaque article $i$ est projeté sur deux dictionnaires fixes de taille $D=16$ : domaine $\hat{d}_i \in \mathbb{S}^{15}$ et opérateur formel $\hat{o}_i \in \mathbb{S}^{15}$. On définit la matrice de caractéristiques $B_i = \hat{o}_i (\I - \hat{d}_i \hat{d}_i^\top)^{1/2} \in \mathbb{R}^{16 \times 16}$. Le noyau de Gram :
$$L_{ij} = q_i q_j \operatorname{Tr}(B_i^\top B_j) = q_i q_j \langle \hat{o}_i, \hat{o}_j \rangle \left(1 - \langle \hat{d}_i, \hat{d}_j \rangle^2\right)$$
est strictement PSD (produit de Schur de matrices PSD). Inspiré d'ALIGNN ([Art.10]), la répulsion d'Onsager est déplacée des nœuds $w$ vers le **graphe de ligne** $L(G)$ (paires orientées $(w_1 \to w_2)$), préservant les pivots $B$ tout en bloquant les transitions déjà explorées.
2. **Synergie par Surprise de Rényi d'ordre 2 et Bandit Swanson :** La synergie de Williams-Beer sur le triplet $(A, B, C)$ est stabilisée par l'entropie de collision $H_2(X) = -\log \sum p_x^2$ : $\text{Syn}_2(A,C|B) = \max(0, I_2(A;B) + I_2(C;B) - I_2(A;C))$. Le tirage séquentiel suit un score UCB sur les ponts $B$ : $\text{Score}(A,C) = \max_{B} \sqrt{I_2(A;B)I_2(C;B)} + c \sqrt{\frac{\ln t}{n_{AC}+1}}$.
3. **Somme amalgamée (Pushout $A \sqcup_B C$) pondérée par Perspectives ([Art.1, Art.6]) :** En extrayant les triplets relationnels $(s, r, o)$, l'interface $B = O(A) \cap O(C)$ sert d'amalgame. Selon le cadre à 3 personas d'[Art.1], on évalue la validité du pushout par produit scalaire sur 3 vecteurs d'orientation $\vec{u}_{\text{formel}}, \vec{u}_{\text{empirique}}, \vec{u}_{\text{structurel}}$.

**C. Plan d'implémentation Python pur (`v6.3`) et 4 Protocoles Falsifiables**
- `memoire_isvd.py` : Remplacer SHA-256 par un SimHash de sous-mots (3-grammes de caractères projetés par table de Rademacher déterministe en dim 16), préservant la distance cosinus avant Koopman.
- `mitose_spectrale.py` : Calculer `G_ij` avec le noyau $L_{ij}$ ci-dessus via `cholesky` existant ; indexer `termes_satures` par tuples de bigrammes `(m1, m2)`.
- `principal.py` : Remplacer `_score_pertinence_texte` par sélection gloutonne de Schur sur $L_{ij}$ + extraction du pont $B$ maximisant $\text{Syn}_2$.

**Protocoles falsifiables (Coût $\le 5\$$) :**
1. **Stabilité spectrale ISVD (P1) :** Ratio d'entropie effective $\exp(-\sum \hat{\sigma}_k \ln \hat{\sigma}_k)$ sur 50 résumés. Seuil : passage de $1.82$ (`v6.2.1`) à $\ge 3.40$ (`v6.3`). Coût : $0\$$ (CPU local).
2. **Rappel temporel de Swanson (P2) :** Sur 100 paires biomédicales/physiques disjointes avant $t_0=2022$ et co-citées en $2025$ ([Art.7, Art.11]). Métrique : *Hit@10* du pivot $B$. Seuil : `v6.3` $\ge 35\%$ vs `v6.2.1` $\le 10\%$. Coût : $0\$$ (API OpenAlex).
3. **Faisabilité d'ablation du Pushout (P3) :** 20 synthèses évaluées à l'aveugle sur la présence d'un protocole testable (équation + métrique). Seuil : taux de succès $\ge 65\%$ contre $\le 25\%$ pour `v6.2.1`. Coût : $1.80\$$ (API LLM).
4. **Survie Cholesky sous contrainte (P4) :** Taux de matrices $L_{ij}$ générées sans exception `ValueError` (non-PSD) sur 1000 tirages aléatoires. Seuil : $100\%$ avec $I - (\hat{d}\hat{d}^\top)^2$ contre $< 40\%$ avec la différence naïve. Coût : $0\$$.

---

### 2) Ce dont je ne suis pas sûr (Limites et conditions de réfutation)
- **Granularité des dictionnaires $D=16$ :** Si les 16 ancres d'opérateurs sont trop génériques (ex: *matrix*, *bound*), $\langle \hat{o}_i, \hat{o}_j \rangle \to 1$ partout et le noyau dégénère en simple répulsion de domaine.
- **Sparsité du graphe de ligne :** Sur des résumés $< 120$ mots, l'intersection exacte des relations d'opérateurs $O(A) \cap O(C)$ peut être vide malgré le SimHash, forçant un repli sur des co-occurrences lâches.
- **Condition de réfutation :** Si dans le protocole P2, le remplacement du tri lexical par le DPP bilinéaire n'améliore pas le *Hit@10* d'au moins $+15$ points, l'hypothèse de séparabilité Domaine/Opérateur à partir de seuls résumés est réfutée.

### Caste #3 — `sonde_orthogonale_onsager` (espèce : `CLAUDE_OPUS`, mode : `HYBRIDE`, confiance : `0.72`)
- **Axe d'exploration** : Exploration orthogonale hors des termes satures et contre-exemples
- **Thèse** : Le DPP dégénère en régime n≈20 articles et le hachage SHA-256 détruit les ponts de Swanson ; une marche aléatoire sur graphe biparti Concepts×Articles pondérée par IDF des concepts-ponts est plus robuste, implémentable en dict+random, et falsifiable par taux de paires inter-domaines ≥40%
- **Contribution** :

# Sonde orthogonale : Contre-exemples et axes négligés

## 1. Chaîne de raisonnement — Attaque des prémisses

Les deux positions précédentes convergent sur un noyau DPP couplant similarité d'opérateurs et orthogonalité de domaines. Je teste la solidité de cette prémisse partagée par trois angles orthogonaux.

**Contre-exemple A : Effondrement du DPP en régime creux.** Un DPP sur une matrice L de taille n×n requiert le calcul de det(L_S) pour tout sous-ensemble S. Quand le corpus moissonné par cycle est petit (n ≈ 12-30 articles, ce qui est le cas réel de v6.2.1), le spectre de L est dominé par 2-3 valeurs propres. Le DPP dégénère alors en un échantillonneur quasi-déterministe qui sélectionne toujours le même sous-ensemble modal. La diversité promise est illusoire : on retombe sur un top-k déguisé. Les deux castes ignorent ce régime n≪100 qui est précisément celui de l'organisme.

**Contre-exemple B : Le pont de Swanson A↔B↔C suppose une transitivité sémantique que le hachage SHA-256→dim16 de l'ISVD détruit.** Le hachage projette des vecteurs sémantiques dans un espace pseudo-aléatoire où la distance cosinus entre deux projections est asymptotiquement constante (concentration de la mesure en haute dimension après hachage). Aucun bandit UCB ne peut exploiter un signal de pont si les embeddings intermédiaires sont décorrélés par construction. Avant d'ajouter un bandit Swanson, il faut réparer la représentation.

**Contre-exemple C : La synergie Williams-Beer est calculable analytiquement uniquement pour des variables discrètes à faible cardinalité.** Sur des distributions continues (scores de pertinence), l'estimation par binning introduit un biais O(1/bins) et une variance O(1/n_samples) qui, pour n≈20 articles, rendent la décomposition PID (information partielle) numériquement instable. Aucun seuil falsifiable proposé ne tient.

## 2. Axe complémentaire : Tirage par marche aléatoire sur graphe biparti pondéré

Au lieu du DPP (coûteux, dégénéré en petit n), je propose un **graphe biparti Concepts×Articles** construit incrémentalement. Chaque article est relié aux concepts qu'il mentionne (extraits par TF-IDF sur le corpus local, sans dépendance externe). Le tirage bisociatif devient une **marche aléatoire à temps de mélange contrôlé** : on part d'un article-ancre, on traverse 2 arêtes (article→concept→article'), et on collecte l'article d'arrivée. La probabilité de transition est pondérée par l'inverse de la fréquence du concept-pont (les concepts rares créent des ponts plus fertiles — c'est exactement le mécanisme de Swanson sans bandit).

**Avantage critique** : en Python pur, c'est un dict-of-sets + random.choices, O(1) par tirage. Pas de déterminant, pas de Cholesky, pas d'estimation de PID.

**Protocole falsifiable** : Sur 5 cycles de moissonnage (coût ≤ 2$), comparer le taux de paires d'articles tirées partageant zéro mot-clé commun mais reliées par un concept-pont de degré ≤ 3 dans le graphe. Seuil : la marche aléatoire doit produire ≥ 40% de paires inter-domaines vs ≤ 15% pour le tri par _score_pertinence_texte actuel.

## 3. Incertitudes

- Je ne suis pas sûr que le graphe biparti reste connexe avec n≈20 articles ; en dessous d'un seuil de connectivité, la marche dégénère aussi.
- L'extraction de concepts par TF-IDF local peut être bruitée sans lemmatisation (pas de dépendance externe).
- Le DPP pourrait fonctionner si on utilise un noyau de projection de rang fixe k=3 (DPP k-élémentaire), mais les castes précédentes n'ont pas spécifié cette restriction.

### Caste #4 — `critique_adversariale_limites` (espèce : `CLAUDE_FABLE_5_1`, mode : `HYBRIDE`, confiance : `0.84`)
- **Axe d'exploration** : Identification des angles morts, cas limites et conditions de refutation
- **Thèse** : Les approches par graphe de ligne, DPP et marche IDF échouent face aux hubs méthodologiques, à la dérive quadratique du spectre de Koopman et aux obstructions de recollement du pushout catégoriel ; la v6.3 nécessite un équilibrage de Sinkhorn-Knopp couplé à un filtre de compatibilité des contraintes avant synthèse.
- **Contribution** :

### 1) Réponse et chaîne de raisonnement : Angles morts et limites des propositions pour la v6.3

L'analyse critique des propositions émises par les castes précédentes et de l'architecture `v6.2.1` révèle quatre vulnérabilités mathématiques majeures qui menacent la fertilité expérimentale réelle de la future `v6.3` :

**A. Pathologie non-stationnaire de l'expansion de Koopman et effondrement spectral**
Dans `memoire_isvd.py`, le relèvement non-linéaire $[v, \sin(v), v^2]$ appliqué sur des projections aléatoires par hachage en dimension 16 souffre d'une asymétrie d'échelle critique. Sans normalisation sphérique stricte ($\|v\|_2 = 1$) préalable, le terme quadratique $v^2$ domine le spectre de covariance dès que $\|v\|_\infty > 1$, tandis que $\sin(v)$ sature. Cela explique la dégénérescence du spectre ISVD actuel ($\Sigma_1 = 269.0 \gg \Sigma_6 = 4.41$) : la SVD de Jacobi de rang 6 ne capture pas des invariants dynamiques de Koopman, mais la dérive de variance des moments pairs, créant un filtre aveugle aux isomorphismes structurels faibles.

**B. Explosion combinatoire du graphe de ligne et biais des moyennes-hubs**
La Caste #2 propose de déplacer la répulsion sur le graphe de ligne $L(G)$ (inspiré d'ALIGNN, Art.10) pour préserver les pivots de Swanson. Or, un nœud-pivot $B$ de degré $d_B$ dans le graphe d'interactions génère $\binom{d_B}{2} = \mathcal{O}(d_B^2)$ arêtes dans $L(G)$. Pour un corpus moissonné à la volée, les concepts méthodologiques transversaux (« *optimization* », « *matrix* », « *bound* ») agissent comme des hubs qui saturent la matrice de Cholesky en $\mathcal{O}(d_{\max}^6)$, étouffant les véritables ponts bisociatifs rares. Quant à la marche aléatoire pondérée par IDF (Caste #3), elle confond *rareté lexicale* et *compatibilité opératoire* : un terme rare partagé entre deux domaines est souvent une coïncidence terminologique (homonymie inter-disciplinaire) plutôt qu'un foncteur de transfert valide.

**C. Obstruction cohomologique au Pushout Catégoriel ($A \leftarrow B \rightarrow C$)**
La consigne postule que l'opérateur de synthèse procède par somme amalgamée ($A \sqcup_B C$). Mathématiquement, ce pushout n'existe et n'est non-trivial que si les morphismes d'injection $f: B \to A$ et $g: B \to C$ préservent la structure interne de l'opérateur $B$. En texte libre (résumés d'articles), deux domaines peuvent partager le même opérateur nominal $B$ sous des axiomatiques contradictoires (ex: régularité continue vs topologie discrète). Sans vérification de cohérence des pré-conditions, l'amalgamation produit des chimères formelles (hallucinations syntaxiques sans validité expérimentale).

**D. Loi de tirage corrigée et implémentation Python pur**
Pour surmonter ces limites en Python standard (`math`, `collections`), le tirage doit opérer non sur les textes bruts, mais sur des triplets typés `(Domaine, Opérateur, Contrainte_de_validité)` extraits par patrons syntaxiques :
1. **Pré-conditionnement de Sinkhorn-Knopp** (5 itérations en Python pur) sur la matrice d'adjacence bipartie Domaine $\times$ Opérateur avant calcul du noyau de Schur, neutralisant l'effet de hub des termes fréquents sans détruire la définie-positivité.
2. **Filtre de recollement local** : un couple de documents $(d_i, d_j)$ partageant un opérateur $B$ est pénalisé si la divergence de Jensen-Shannon de leurs contextes de contraintes dépasse un seuil critique $\tau$, garantissant la faisabilité du pushout.

### 2) Ce dont je ne suis pas sûr (Limites, hypothèses et conditions de réfutation)

* **Hypothèse non vérifiée** : Que les résumés (abstracts) moissonnés contiennent suffisamment d'informations sur les *conditions de validité* d'un théorème ou d'un algorithme pour détecter une obstruction au pushout sans lire le corps de l'article.
* **Cas limite d'invalidation** : En régime de très faible recouvrement ($N < 15$ textes disparates), la régularisation de Sinkhorn sur une matrice ultra-creuse peut ne pas converger et uniformiser artificiellement du bruit pur.
* **Protocole de réfutation à bas coût ($\le 5\$$)** :
  * *Métrique* : Taux de survie aux contre-exemples formels (Un LLM juge évalue à l'aveugle si l'hybridation générée $A \sqcup_B C$ viole une hypothèse mathématique explicite de $A$ ou $C$ sur 50 tirages).
  * *Seuil de falsification* : La `v6.3` est réfutée si le taux d'invalidité formelle dépasse $35\%$ ou si le gain de survie par rapport au tirage aléatoire stratifié de `v6.2.1` est inférieur à $+20$ points de pourcentage (coût API $\approx 1.20\$$).

### Caste #5 — `arbitre_synthese_contradictoire` (espèce : `GEMINI_4_ARGON`, mode : `HYBRIDE`, confiance : `0.88`)
- **Axe d'exploration** : Arbitrage des votes, synthese contradictoire et redaction finale
- **Thèse** : Remplacement du tri lexical v6.2.1 par un pipeline v6.3 en Python pur combinant SimHash sur n-grammes avec normalisation spherique pre-Koopman, tirage DPP bilineaire Domaine x Operateur regularise par Sinkhorn-Knopp, repulsion d'Onsager sur graphe de ligne pour preserver les pivots de Swanson, et synthese par pushout categoriel sous filtre de compatibilite des contraintes.
- **Contribution** :

### 1. Réponse finale consolidée de l'essaim : Architecture bisociative `v6.3`

Pour maximiser la fertilité expérimentale des associations d'idées, la `v6.3` remplace le filtrage unaire de la `v6.2.1` par un pipeline algébrique et catégoriel en quatre étages, implémentable en Python pur :

1. **Encodage et Mémoire ISVD régularisée (`memoire_isvd.py`)** : Le hachage cryptographique SHA-256 (qui détruit la topologie locale par effet d'avalanche) est remplacé par un **SimHash morphologique** sur $n$-grammes de caractères, séparant chaque article $i$ en deux vecteurs unitaires ($\|v\|_2 = 1$) : Domaine ($d_i \in \mathbb{R}^{16}$) et Opérateur ($o_i \in \mathbb{R}^{16}$, filtré sur le lexique mathématique/méthodologique). Cette normalisation sphérique empêche le terme quadratique $v^2$ de l'expansion de Koopman $[v, \sin(v), v^2]$ d'écraser le spectre ($\sigma_1 = 269.0 \gg \sigma_6 = 4.41$).
2. **Tirage conjoint par DPP bilinéaire régularisé par Sinkhorn-Knopp (`principal.py`)** : Au lieu du tri séparable `_score_pertinence_texte`, la sélection d'un sous-ensemble $S$ de $k$ articles suit un Processus Ponctuel Déterminantal $\mathbb{P}(S) \propto \det(L_S)$. Le noyau $L_{ij} = q_i q_j \cdot \langle o_i, o_j \rangle^2 \cdot (1 - \langle d_i, d_j \rangle^2)$ est garanti semi-défini positif (PSD) par produit de Schur. Pour éviter l'effondrement modal en régime creux ($n \approx 20$) et la domination des hubs méthodologiques génériques (ex. GNN, *Art.7–12*), $L$ subit 5 itérations d'équilibrage bistochastique de **Sinkhorn-Knopp** et une régularisation de Tikhonov ($L \leftarrow \text{Sinkhorn}(L) + \gamma I$).
3. **Répulsion sur graphe de ligne et Bandit de Swanson (`mitose_spectrale.py`)** : La répulsion d'Onsager est déplacée des mots isolés vers les *arêtes* du graphe de ligne (paires conceptuelles co-occurrentes, inspiré d'ALIGNN, *Art.10*). Cela préserve les termes-pivots $B$ nécessaires aux ponts de Swanson $A \leftrightarrow B \leftrightarrow C$ (*Art.11*), explorés par un bandit UCB1 pondérant la synergie de Williams-Beer (estimée par l'écart d'entropie de Shannon $\log\det$ jointe vs marginale via Cholesky) et le bonus *Stepping Stones* (+15 %).
4. **Synthèse par Pushout Catégoriel filtré** : Deux articles tirés $(A, C)$ ne sont fusionnés en somme amalgamée $A \sqcup_B C$ (blending conceptuel sans perte de structure, *Art.4, Art.6*) que si l'interface opératoire $B = O_A \cap O_C$ est non vide et satisfait un filtre de compatibilité des contraintes (absence de contradictions d'hypothèses comme *linéaire/non-linéaire* ou *stationnaire/transitoire*, cf. *R1, R3*).

**Plan d'implémentation Python pur (C-01 à C-17) et Protocoles falsifiables ($\le 5\$$) :**
* *Implémentation (`math`, `hashlib`, `random`)* : Remplacer `_score_pertinence_texte` par `_tirage_dpp_sinkhorn(articles, k=4)` utilisant la décomposition de Cholesky existante de `mitose_spectrale.py` pour l'échantillonnage glouton map-DPP et le calcul d'information mutuelle.
* **P1 (Stabilité spectrale ISVD)** : Ratio de conditionnement $\sigma_1/\sigma_6$ sur 50 cycles. Seuil : passage de $60.9$ (`v6.2.1`) à $\le 12.0$ grâce à la normalisation sphérique pré-Koopman (Coût : $0\$$).
* **P2 (Fertilité inter-domaines)** : Taux de paires tirées avec chevauchement de domaine $\langle d_i, d_j \rangle < 0.25$ et couplage d'opérateur $\langle o_i, o_j \rangle > 0.50$. Seuil : $\ge 45\%$ contre $< 10\%$ en `v6.2.1` (Coût : $1.20\$$ API).
* **P3 (Rétention des ponts de Swanson)** : Recall@5 sur 20 triades historiques reconstruites $(A, B, C)$ en masquant $A \leftrightarrow C$. Seuil : $\ge 60\%$ de redécouverte du pivot $B$ sans suppression par Onsager (Coût : $2.00\$$).
* **P4 (Validité expérimentale du Pushout)** : Taux de protocoles synthétisés compilables et non contradictoires évalués à l'aveugle sur 30 tirages. Seuil : gain net $\ge +30\%$ sur `v6.2.1` (Coût : $1.80\$$).

---

### 2. Raisonnement contradictoire et arbitrage des castes

L'arbitrage fait émerger une synthèse stricte en croisant les quatre critiques :
* **Fable (#1) vs Argon (#2)** : Fable pose la fondation théorique (DPP Domaine×Opérateur, UCB Swanson, Williams-Beer, Pushout), mais Argon démontre que le noyau bilinéaire naïf n'est pas PSD (faisant échouer Cholesky dans `mitose_spectrale.py`), que SHA-256 détruit la géométrie par effet d'avalanche, et que la répulsion d'Onsager actuelle élimine les pivots $B$ de Swanson en les traitant comme des `termes_satures`. L'adoption du produit de Schur, du SimHash et du graphe de ligne d'Argon résout ces trois défauts.
* **Opus (#3) et Fable-Critique (#4) vs le consensus (#1/#2)** : Opus prouve qu'en régime réel ($n \approx 12\text{--}30$ articles moissonnés), un DPP standard dégénère en un top-$k$ déterministe dominé par 2 ou 3 valeurs propres. Cependant, sa marche aléatoire pondérée par l'IDF est réfutée par la Caste #4 : elle s'effondre sur les « hubs méthodologiques » génériques et n'explique pas l'explosion spectrale de Koopman ($\sigma_1 = 269.0$) due à l'absence de normalisation avant $v^2$. L'intégration de la normalisation sphérique, de l'équilibrage de Sinkhorn-Knopp et du filtre de compatibilité des contraintes (Caste #4) stabilise le DPP à petit $n$ tout en garantissant que le pushout catégoriel ne fusionne pas des formalismes incompatibles.

---

### 3. Points d'incertitude résiduels de l'essaim

1. **Pauvreté des résumés courts** : Sans accès au texte intégral ni parseur syntaxique lourd (contrainte Python pur), l'extraction par heuristiques lexicales des contraintes de domaine et des opérateurs sur des résumés de moins de 150 mots risque de laisser l'interface du pushout $B$ vide ou bruitée dans $25\%$ à $35\%$ des tirages.
2. **Synergie non-lexicale** : L'estimation de la synergie de Williams-Beer par déterminant de Gram sur n-grammes peut sous-évaluer l'isomorphisme structurel entre deux articles aux notations mathématiques totalement disjointes.

## 4. Ce dont l'essaim n'est pas sûr

- **Caste #1 (`monoculture_analytique`)** : L'approximation de MI par cooccurrence lexicale peut sous-estimer la synergie réelle entre articles de domaines très éloignés partageant peu de vocabulaire mais beaucoup de structure — le protocole P3 est le seul test empirique direct de cette limite.
- **Caste #2 (`monoculture_croisee`)** : La richesse d'extraction des opérateurs formels sur des résumés courts (< 150 mots) sans parseur syntaxique lourd peut laisser l'interface du pushout catégoriel vide dans plus de 30 % des tirages.
- **Caste #3 (`sonde_orthogonale_onsager`)** : Connexité du graphe biparti en régime très creux (n<15) et qualité de l'extraction de concepts sans NLP externe
- **Caste #4 (`critique_adversariale_limites`)** : L'extraction en Python pur des contraintes de validité depuis de simples résumés d'articles peut s'avérer trop bruitée pour garantir l'existence réelle de la somme amalgamée sans accès au texte intégral.
- **Caste #5 (`arbitre_synthese_contradictoire`)** : L'extraction sans NLP externe des operateurs et des contraintes de validite sur des resumes courts (<150 mots) peut laisser l'interface du pushout categoriel vide ou bruitee dans environ 30% des tirages.

--- ORGANISATION ---
- **Appels consacrés à la question ouverte** : `6` tentés | `6` OK | `0` échecs (Total génération : `6` tentés, `6` OK, `0` échecs, coût cumulé : `0.12` USD).
- **Moissonnage documentaire (`rechercher` / `telecharger`)** : `6` recherches tentées (`6` OK, statuts=`{'OK': 6}`) | `3` téléchargements tentés (`3` OK, statuts=`{'OK': 3}`).
- **Castes mobilisées (`5`)** :
  * Caste #1 : rôle=`monoculture_analytique` | espèce=`CLAUDE_FABLE_5_1` | mode=`MONOCULTURE` | axe="Analyse initiale et decomposition formelle de la question"
  * Caste #2 : rôle=`monoculture_croisee` | espèce=`GEMINI_4_ARGON` | mode=`MONOCULTURE` | axe="Seconde perspective independante et verification des premisses"
  * Caste #3 : rôle=`sonde_orthogonale_onsager` | espèce=`CLAUDE_OPUS` | mode=`HYBRIDE` | axe="Exploration orthogonale hors des termes satures et contre-exemples"
  * Caste #4 : rôle=`critique_adversariale_limites` | espèce=`CLAUDE_FABLE_5_1` | mode=`HYBRIDE` | axe="Identification des angles morts, cas limites et conditions de refutation"
  * Caste #5 : rôle=`arbitre_synthese_contradictoire` | espèce=`GEMINI_4_ARGON` | mode=`HYBRIDE` | axe="Arbitrage des votes, synthese contradictoire et redaction finale"
- **Votes et confiances par caste** :
  * Caste #1 (`monoculture_analytique`, `CLAUDE_FABLE_5_1`) : confiance=`0.74` | poids_vote=`0.1832` | vote="Le remplacement de _score_pertinence_texte par un noyau DPP bilinéaire Domaine×Opérateur couplé à un bandit Swanson UCB et une synergie Williams-Beer approchée constitue la transformation mathématiquement fondée minimale pour rendre le moteur bisociatif de v6.3 fertile en associations inter-domaines non triviales, implémentable en Python pur." | incertitude="L'approximation de MI par cooccurrence lexicale peut sous-estimer la synergie réelle entre articles de domaines très éloignés partageant peu de vocabulaire mais beaucoup de structure — le protocole P3 est le seul test empirique direct de cette limite."
  * Caste #2 (`monoculture_croisee`, `GEMINI_4_ARGON`) : confiance=`0.86` | poids_vote=`0.2129` | vote="Pour éviter l'indéfinition spectrale du noyau bilinéaire naïf et la destruction des termes-pivots de Swanson par la répulsion d'Onsager, la v6.3 doit utiliser un noyau de Schur strictement PSD couplant similarité d'opérateurs (via SimHash morphologique) et orthogonalité de domaines, tout en déplaçant la répulsion spectrale sur le graphe de ligne des transitions conceptuelles." | incertitude="La richesse d'extraction des opérateurs formels sur des résumés courts (< 150 mots) sans parseur syntaxique lourd peut laisser l'interface du pushout catégoriel vide dans plus de 30 % des tirages."
  * Caste #3 (`sonde_orthogonale_onsager`, `CLAUDE_OPUS`) : confiance=`0.72` | poids_vote=`0.1782` | vote="Le DPP dégénère en régime n≈20 articles et le hachage SHA-256 détruit les ponts de Swanson ; une marche aléatoire sur graphe biparti Concepts×Articles pondérée par IDF des concepts-ponts est plus robuste, implémentable en dict+random, et falsifiable par taux de paires inter-domaines ≥40%" | incertitude="Connexité du graphe biparti en régime très creux (n<15) et qualité de l'extraction de concepts sans NLP externe"
  * Caste #4 (`critique_adversariale_limites`, `CLAUDE_FABLE_5_1`) : confiance=`0.84` | poids_vote=`0.2079` | vote="Les approches par graphe de ligne, DPP et marche IDF échouent face aux hubs méthodologiques, à la dérive quadratique du spectre de Koopman et aux obstructions de recollement du pushout catégoriel ; la v6.3 nécessite un équilibrage de Sinkhorn-Knopp couplé à un filtre de compatibilité des contraintes avant synthèse." | incertitude="L'extraction en Python pur des contraintes de validité depuis de simples résumés d'articles peut s'avérer trop bruitée pour garantir l'existence réelle de la somme amalgamée sans accès au texte intégral."
  * Caste #5 (`arbitre_synthese_contradictoire`, `GEMINI_4_ARGON`) : confiance=`0.88` | poids_vote=`0.2178` | vote="Remplacement du tri lexical v6.2.1 par un pipeline v6.3 en Python pur combinant SimHash sur n-grammes avec normalisation spherique pre-Koopman, tirage DPP bilineaire Domaine x Operateur regularise par Sinkhorn-Knopp, repulsion d'Onsager sur graphe de ligne pour preserver les pivots de Swanson, et synthese par pushout categoriel sous filtre de compatibilite des contraintes." | incertitude="L'extraction sans NLP externe des operateurs et des contraintes de validite sur des resumes courts (<150 mots) peut laisser l'interface du pushout categoriel vide ou bruitee dans environ 30% des tirages."
- **Mémoire spectrale ISVD ayant servi** :
  * Spectre `Sigma` : `[269.001247, 76.028743, 61.74514, 52.371704, 49.756688, 4.412544]`
  * Exemplaires actifs en mémoire : `12` (erreur de troncature de Frobenius : `0.709468`)
  * Résumé transmis aux castes : `Spectre ISVD Sigma=[269.001247, 76.028743, 61.74514, 52.371704, 49.756688, 4.412544] | Journal d'ablation : statut_parent=STAGNANT | delta_score=0.0 | retour_arriere=None |  R1 (gen 9, E=250.160942): [Moisson web] [Brave GreyLit] SING: SDE Inference via Natural Gradients (June 21, 2025) : Here, we propose SDE Inference via Natural Gradients (SING), <strong>a method that leverages natural gradient VI to efficiently ex |  R2 (gen 6, E=244.790451): [Moisson web] Cyberspace Security Using Adversarial Learning and Conformal Prediction (2015) : This paper advances new directions for cyber security using adversarial learning and conformal prediction in order to enhance |  R3 (gen 14, E=241.926603): [Moisson openalex] A Novel State-Centric Necessary Condition for Time-Optimal Control of Controllable Linear Systems Based on Augmented Switching Laws (2025) : Most existing necessary conditions for optimal control based |  R4 (gen 17, E=241.906547): [Moisson arxiv] Phase transition of the largest eigenvalue for non-null complex sample covariance matrices (2004-03-01) : We compute the limiting distributions of the largest eigenvalue of a complex Gaussian sample covar`
- **Capacité spectrale Shannon-Gram de la question ouverte** : capacité=`3.618972`, gain_marginal=`0.723794`, termes_satures=`['article', 'aux', 'bruit', 'cholesky', 'confiance', 'dans']`.

<<<FIN C1>>>

<<<DÉBUT C2 — relecture de la méta-conception par conv-audit>>>
# Relecture critique — rapport de méta-conception v6.3 de l'essaim (Fable + Opus + Argon) — v1

De : conv-audit, le 2026-10-26 à 17:22:23 UTC (heure lue sur `date -u` dans la commande qui écrit cette ligne).
Objet relu : `RAPPORT-META-CONCEPTION-V6-3-FABLE-OPUS-ARGON.md` (`96d12112…`, commit `5512513` de la branche
`canal/gemini-organisme-v6-2-1-relais-gen8`), contre le code réel de la v6.2.1 (`7ea3270`, arbre `4f13647a…`) et le
spectre réel de la génération 18 (`memoire_isvd.json`, Sigma = [269.001247, …, 4.412544] : le ratio 60,9 est vérifié).
Statut : relecture sur pièces et sur code ; les vérifications numériques tournent en parallèle (deux agents sur
processeur, dossiers `/var/tmp/essais-meta-conception-v1/a` et `b`) ; verdicts chiffrés à leur retour. Régime
exploratoire (R-522) : rien d'opposable.

## Verdict d'ensemble

Le rapport est de bonne facture (castes réellement contradictoires, limites avouées, protocoles chiffrés), mais **deux
des quatre briques portent un défaut mathématique réel**, une troisième n'est pas motivée par une trace, et les quatre
protocoles répètent le défaut déjà vu dans les expériences du rapport consolidé (seuils ronds sans nul calibré). Rien
n'est à jeter : chaque brique a un correctif plus simple que la proposition.

## Brique 1 — SimHash + normalisation sphérique pré-Koopman (`memoire_isvd.py`)

- **Le diagnostic, tel qu'écrit, est faux sur un point vérifiable** : le code v6.2.1 normalise déjà chaque vecteur
  relevé à norme 1 (`extraire_vecteur_koopman`, dernière ligne). « L'élévation quadratique non normalisée écrase le
  spectre » ne peut donc pas être le mécanisme tel quel.
- **Le mécanisme probable** (à confirmer par l'essai a) : (1) `base` — la somme des hachages par jeton — n'est pas
  normalisée avant le relèvement : ses composantes croissent comme la racine du nombre de jetons, donc `sin(val)` sature
  et oscille, et `val²` grandit, **avant** la normalisation finale ; (2) surtout, les coordonnées `i % 3 == 2` valent
  `val² ≥ 0` : tous les exemplaires partagent le même demi-espace sur un tiers des coordonnées — une direction commune
  que la normalisation par vecteur n'enlève pas, et qui suffit à faire un σ1 dominant. **Le remède du rapport
  (normaliser avant le relèvement) borne (1) mais ne corrige pas (2)** ; le correctif manquant est un **centrage**
  (soustraire la moyenne des exemplaires avant le spectre), qui est l'usage standard avant toute décomposition.
- **SimHash sur n-grammes** : fondé — le hachage SHA-256 par jeton entier est bien à effet d'avalanche (vérifié dans le
  code) et détruit les racines morphologiques ; l'essai a mesure le gain réel.
- **Effet de bord non traité par le rapport** : changer l'encodage change la mesure de nouveauté et donc le **critère
  d'arrêt** des générations (convergence de Cauchy du spectre + saturation de Shannon) ; les 18 générations accumulées ne
  sont plus comparables. Toute v6.3 doit re-étalonner son critère d'arrêt et le dire.

## Brique 2 — noyau de tirage « DPP bilinéaire » + Sinkhorn (`principal.py`)

- **Le noyau annoncé « strictement PSD par produit de Schur » ne l'est pas sous la forme donnée.** La matrice
  M_ij = 1 − ⟨d_i,d_j⟩² a une diagonale nulle (d_i unitaires) donc une trace nulle : dès qu'elle n'est pas nulle, elle a
  une valeur propre négative ; le produit de Schur ⟨o_i,o_j⟩² ∘ M n'hérite d'aucune garantie (le théorème de Schur vaut
  pour un produit de deux matrices PSD ; M n'en est pas une). **C'est exactement le piège que la caste 2 reproche à la
  caste 1.** La forme « trace » affichée comme équivalente, Tr(B_iᵀB_j), vaut en réalité ⟨o_i,o_j⟩·(14 + ⟨d_i,d_j⟩²) en
  dimension 16 : elle est PSD, mais elle **récompense** (faiblement) la similarité de domaine au lieu de la pénaliser —
  l'égalité affichée dans le rapport est fausse. L'essai b le mesure.
- **Défaut de conception plus profond** : dans un processus ponctuel déterminantal, on ne peut pas « récompenser » la
  similarité d'opérateur dans le noyau — toute similarité y produit de la répulsion. Ce que la méta-conception veut
  (paires à opérateur commun ET domaines éloignés) se construit autrement : la **diversité de domaine dans le noyau**
  (S_ij = ⟨d_i,d_j⟩², PSD), la **pertinence d'opérateur dans la qualité** q_i (adéquation à la question), et
  l'appariement par pont après tirage. L = diag(q) S diag(q) est PSD par construction. C'est le correctif que l'essai b
  compare.
- **Sinkhorn** : l'équilibrage symétrique D L D préserve la semi-définie positivité (congruence) — juste ; mais équilibré
  sur L entier, il aplatit aussi les qualités q (les marges portent q²) : à faire sur S seulement. La dégénérescence à
  n ≈ 20 (caste 3) est réelle ; tirage de taille fixée + Tikhonov la mitigent — le rapport l'a.

## Brique 3 — répulsion sur graphe de ligne (`mitose_spectrale.py`)

- **L'affirmation « la répulsion actuelle détruit les pivots de Swanson » n'est appuyée par aucune trace.** Dans le code,
  `termes_satures` = jetons présents dans au moins 75 % des textes, plafonnés à six ; dans les sorties réelles (gen 18 et
  méta-conception), les termes saturés sont des mots-outils (« article », « aux », « dans », « bruit », « cholesky »,
  « confiance ») — pas des pivots. Le danger existe en principe (un pivot présent dans 75 % des textes d'une génération) ;
  avant de payer le graphe de ligne (nombre d'arêtes en d_B² autour d'un pivot de degré d_B — l'objection de la caste 4
  est juste), essayer deux remèdes à coût quasi nul : liste d'arrêt des mots-outils ; exemption des termes à fort
  contraste inter-domaines. L'essai b mesure le seuil où un pivot sature et compare les trois remèdes.
- **Le bandit sur les ponts n'a pas de récompense définie.** Aucune des castes ne dit ce que « succès d'un pont » veut
  dire après coup. Règle du programme : **aucun score de course n'entre dans l'organisme** ; la récompense devra être
  interne (synergie réalisée, hypothèse archivée non redondante) et écrite avant toute implémentation — sinon le bandit
  est une boucle sur soi.

## Brique 4 — « pushout catégoriel » filtré

- Le code proposé (caste 1) est une **fusion d'ensembles de termes** (union, intersection comme « ponts ») : aucun
  morphisme, aucune structure préservée — « somme amalgamée » est décoratif, comme « répulsion d'Onsager » l'était déjà
  (contre-lecture de la synthèse, CLS-10). À nommer « fusion sur interface commune ».
- `score_fertilite = |ponts| · log(|termes_a| + |termes_b| + 1)` **récompense la verbosité** (il croît avec la taille des
  vocabulaires à ponts constants) : à normaliser. L'essai b le montre et compare une version normalisée.
- **La vraie bonne idée du rapport est le filtre de compatibilité des contraintes** (caste 4 : l'homonymie
  inter-domaines fabrique des chimères) : implémentable tout de suite par paires de marqueurs contradictoires, testable
  sur vérité terrain plantée (essai b).

## Protocoles P1 à P4 — même famille de défauts que les expériences du rapport consolidé

- Deux jeux de protocoles incompatibles coexistent (caste 1 contre arbitre) sous les mêmes noms P1 à P4 : à unifier.
- Seuils ronds sans nul calibré ni baseline mesurée (« < 10 % en v6.2.1 » : estimé, pas mesuré) ; P3 (caste 1) repose sur
  un juge-modèle non étalonné ; P3 (arbitre) sur « 20 triades historiques reconstruites » qui n'existent pas encore (qui
  les construit, avec quel biais de sélection ?). P1 (arbitre) tel qu'écrit est un résultat acquis d'avance si le
  centrage suffit (même défaut que HR3 du rapport consolidé) : l'essai a propose une version qui peut échouer.
- Bon réflexe à garder : P4 de la caste 2 (taux de survie de la factorisation de Cholesky sur 1 000 tirages) est un vrai
  test mécanique ; c'est d'ailleurs lui qui aurait détecté le défaut de la brique 2.

## Trois points de méthode

1. **Auto-évaluation** : le rapport sort de l'organisme et propose sa propre refonte ; ses « confiances » (0,72 à 0,88)
   sont des déclarations, pas des mesures. Les verdicts chiffrés viendront des essais a et b (code indépendant), du
   collisionneur (autres modèles), et de rien d'autre.
2. **Confidentialité** : le sigle du financeur apparaît 287 fois dans la branche de Gemini (noms de dossiers et
   rapports) ; aucun montant. Dépôt privé, mais règle R-515 : à signaler à Lazar — soit on l'accepte pour les brouillons
   de Gemini, soit Gemini renomme en « programme » dans ses prochaines poussées. La copie publique expurgée ne doit en
   aucun cas reprendre ces dossiers.
3. **Lignage** : la v6.3 devra partir de la v6.2.1 (C-01 à C-17 gardées), déclarer ses changements, et re-étalonner son
   critère d'arrêt (brique 1). Rien dans les quatre briques ne touche aux gardes de sûreté du noyau : c'est le bon
   périmètre.

<<<FIN C2>>>

<<<DÉBUT C3a — génération 0 : synthèse>>>
# Pôle scientifique automatique — synthèse de la génération 0 (les hypothèses de l'organisme sur sa propre structure, testées) — v1

De : conv-audit, le 2026-10-26 18:13:27 UTC. Génération 0 : les affirmations du rapport de méta-conception v6.3 de l'essaim de Gemini
(`96d12112…`) testées par calcul indépendant, sur processeur, par deux expérimentateurs (brique 1 : `5b7011b1…` ; briques
2 à 4 : `929cbc32…`), runs déterministes relancés. Régime exploratoire (R-522), non opposable. **Pas encore vérifié par un
agent d'une autre famille** (étape suivante du pôle).

## Verdict

Sur dix-huit affirmations testées : **cinq survivent, dix sont éliminées, trois indécises.** Les deux briques
« mathématiquement fondées » du rapport (le noyau de tirage, la répulsion sur graphe de ligne) **tombent** ; les deux
idées qui survivent sont des correctifs, dont l'un est le mien et l'autre le contraire de ce que j'avais écrit. Surtout,
**le rapport décrit un code qui n'existe pas** : ni `_score_pertinence_texte`, ni la décomposition de Cholesky, ni le
log-déterminant qu'il prétend réutiliser ne sont dans la v6.2.1 — la refonte est bâtie sur une lecture fausse du code.

## Ce qui survit (à réutiliser dans le pôle)

- **La mémoire spectrale actuelle est aveugle aux textes réels** (rappel du plus proche voisin 0,000, hasard 0,038 ;
  accord 0,014). Vrai défaut, à corriger.
- **Normaliser la somme des hachages avant le relèvement** : meilleur gain mesuré (rappel +0,135 ; accord 0,014 → 0,48
  sur 27 textes réels).
- **SimHash sur n-grammes** préserve la morphologie au niveau du mot (aire 0,987 contre 0,458) ; indécis au niveau du
  texte.
- **Le correctif du noyau de tirage** (diversité de domaine dans le noyau, pertinence dans la qualité, opérateur
  réintroduit après tirage) : diversité 0,90 à 0,95 pour un hasard de 0,74, qualité gardée, pas de dégénérescence.
- **Le filtre de compatibilité des contraintes** : utile (fusions contradictoires 57 % → 0 % sur lexique propre), mais
  fragile sur du bruit réaliste (57 % → 34 %, rappel 0,61) ; à garder, à ne pas surestimer.

## Ce qui est éliminé

- Le noyau « PSD par produit de Schur » du rapport : **1 000 violations sur 1 000** (λ_min médian −0,715) ; réparé par
  γ ≥ 0,37, il repousse justement les paires qu'il visait.
- L'égalité « trace = 1 − ⟨d,d⟩² » : fausse (la trace vaut 14 + ⟨d,d⟩²) ; la forme trace récompense la similarité de
  domaine.
- « La répulsion détruit les pivots de Swanson » : réfutée sur l'organisme réel (les termes saturés de la génération 18
  sont des mots-outils, aucun pivot) ; le graphe de ligne proposé coûte C(d_B, 2) et bloque 78 % des ponts.
- Le diagnostic « v² écrase par explosion de variance » (σ1 est une direction moyenne, pas une variance) ; « Koopman sur
  bruit blanc amplifie la variance isotrope » ; « SHA-256 maximalement non informatif » ; le protocole P1 (un encodage
  nul le passe à 100 %) ; le critère d'arrêt par convergence du spectre (absent du code) ; mon propre correctif de
  recentrage (sans effet) ; le rang effectif 1,82 annoncé (vrai : 3,96).

## Ce que la génération 0 établit pour le choix du moteur

- La voie « perfectionner notre organisme » part d'une **refonte fausse sur le code** : à refaire sur le vrai code, avec
  les deux correctifs survivants seulement. Le moissonnage et le tri réels de la v6.2.1 ne sont pas ceux que le rapport
  décrit — à relire avant toute conception.
- La génération 0 a coûté 0 dollar (processeur) et a éliminé dix affirmations sur dix-huit par des tests qui pouvaient
  échouer : c'est le mode de fonctionnement visé pour le pôle.

## Suite

1. Vérification de ces verdicts par un agent neuf d'une autre famille (étape « vérificateur » du pôle).
2. Relecture v2 pour Gemini (corrigée par ces essais, mes erreurs comprises), sur une branche à part ; Lazar la lui
   transmet.
3. Génération 1 : recombinaison des cinq survivants en fiches filles + témoins plantés, dans l'orchestrateur du pôle.

<<<FIN C3a>>>

<<<DÉBUT C3b — génération 0 : essais des briques 2 à 4>>>
# Essais des briques 2, 3 et 4 de la méta-conception (organisme v6.2.1) — v1

Rédigé le 2026-10-26T18:11:09Z (heure lue sur `date -u`). Lignée conv-audit, sous-agent, travail sur processeur seulement.
Entrées en lecture seule : `fournis/rapport-meta-conception.md` (empreinte `96d12112c8d8d7e376943fa42fc0a4d6faed52b7ed09ae9ecac981c65949c6cf`) et `fournis/organisme/` (27 fichiers, empreintes dans `manifeste-essais-v1.json` ; intacts après les runs, aucun fichier compilé écrit).
Fonctions de l'organisme et de la caste 1 : copies exactes extraites du source par l'arbre syntaxique (empreinte de chaque segment consignée), jamais importées. Python 3.13.17, numpy 2.5.3, scipy 1.18.1, `python3 -I -B`. Graines : `numpy.random.SeedSequence(entropy=20261026, spawn_key=(tâche, …))`, détail par fichier de résultats. Relance complète : `sh lancer_tout_v1.sh`. Une seconde relance donne des résultats identiques hors champs d'heure et de durée (les 7 fichiers).

## Verdict

- Brique 2 : le noyau du rapport n'est pas semi-défini positif (1 000 jeux en violation sur 1 000 ; sa diagonale est nulle, donc sa trace aussi). Sinkhorn-Knopp plus γI ne le répare qu'à γ ≥ 0,37, et le noyau réparé repousse alors exactement les paires qu'il devait favoriser. L'égalité « trace = 1 − ⟨d,d⟩² » est fausse : la trace vaut 14 + ⟨d,d⟩². Le correctif (similarité de domaine dans le noyau, qualité à part, partage d'opérateur réintroduit après tirage) donne 0,89 à 0,94 de paires de domaines différents et 99,5 à 100 % d'ensembles bisociatifs.
- Brique 3 : la répulsion actuelle ne voit aucun pivot. Ses 6 termes sont les 6 premiers, par ordre alphabétique, de 35 jetons présents dans les 5 textes : mots-outils, clé du gabarit, mots de la question. Un pivot n'y entre qu'à f ≥ ⌊0,75 n⌋/n et en l'absence de 6 mots-outils omniprésents. Le graphe de ligne coûte bien en d_B² (pente 2,007). Il est dominé par une exemption appuyée sur une fréquence de fond.
- Brique 4 : le score de fertilité a un biais de verbosité (×2,5 à ponts constants). La normalisation réduit ce biais sans l'annuler. Le filtre de contradictions est parfait sur un lexique propre, mais garde 34 % de fusions contradictoires dès qu'on ajoute un bruit réaliste.

## 0. Faits de code relevés avant les essais

| Fait | Preuve |
|---|---|
| `_score_pertinence_texte` n'existe pas dans le code v6.2.1 fourni : la question de Lazar et le rapport décrivent un tri qui n'est pas là. | 0 occurrence dans les fichiers `.py` de `fournis/organisme/` (recherche sur tout le répertoire) |
| `mitose_spectrale.py` ne contient ni Cholesky ni log-déterminant. La « capacité » vaut n / (1 + (n − 1) s̄) · log(1 + SNR), où s̄ est la similarité quadratique moyenne hors diagonale. « La décomposition de Cholesky existante de mitose_spectrale.py » sur laquelle le plan du rapport s'appuie n'existe pas. | `mitose_spectrale.py` l. 31-42 ; 0 occurrence de `cholesky` dans les `.py` |
| La « répulsion d'Onsager » n'est qu'une phrase de consigne envoyée aux castes 3 et 4 (« Termes deja satures… ne repete pas les arguments deja acquis »). Elle ne touche jamais le tirage d'articles. La liste affichée dans le rapport, calculée sur 5 textes, l'est après la boucle et n'est injectée nulle part. | `principal.py` l. 1252-1268, 1399, 1431 |
| `decomposer_jacobi_symetrique` renvoie \|λ\| triées, donc perd le signe. À son plafond par défaut de 120 rotations, elle ne converge pas à 20×20 (résidu relatif médian 0,046). À 16×16, matrice de type mémoire, l'erreur sur σ1/σ6 reste ≤ 0,51 %, et le 60,9 du protocole P1 n'est donc pas en cause. Dans les essais : 5 000 rotations, signe restitué par le quotient de Rayleigh, résidu ≤ 1,9e-10, écart au calcul de référence d'algèbre linéaire ≤ 4,4e-15. | [instrument], [b2-psd] |
| L'expression des jetons de l'organisme est en ASCII seulement : un mot accentué est coupé en fragments (« bilinéaire » → « bilin », « aire » ; « chaîne » → « cha »). L'extraction de la caste 1 (`\b[a-z]{4,}\b`) élimine au contraire tout mot accentué. | [b3-gen18] ; copie de `extraire_termes` |

## 1. Brique 2 — noyau de tirage

### Essai 1 : semi-définie positivité de la forme du rapport

Méthode. 1 000 jeux de n = 20 couples (d_i, o_i) unitaires tirés uniformément sur la sphère de dimension 16, q_i uniforme sur [0,5 ; 1,5]. Le noyau est assemblé sous la forme exacte L_ij = q_i q_j ⟨o_i,o_j⟩² (1 − ⟨d_i,d_j⟩²), puis décomposé par la copie de la fonction de Jacobi de l'organisme. Violation si λ_min < −10⁻⁸.

| Mesure | Valeur |
|---|---|
| Jeux en violation | **1 000 / 1 000** (de même à 120 rotations : un quotient de Rayleigh négatif suffit à le certifier) |
| λ_min | médiane −0,715 (de −1,414 à −0,366) ; λ_min/λ_max médiane −0,545 |
| Valeurs propres négatives par matrice | 10 à 13 sur 20 (médiane 11) |
| \|diagonale\| max ; \|trace\| max | 2,3e-15 ; 7,0e-15 |
| Mineurs principaux 2×2 négatifs | 189 380 / 190 000 (les autres ont L_ij < 10⁻⁶) |

Pourquoi. ⟨d_i,d_i⟩ = 1 annule la diagonale de M = J − C∘C, donc celle de L, donc sa trace. Une matrice symétrique non nulle de trace nulle a une valeur propre négative. Le théorème du produit de Schur exige deux facteurs semi-définis positifs, et M ne l'est pas. La note de la consigne (« K∘M n'est pas forcément indéfini ») est juste en général, mais ici K = (O∘O) a une diagonale unité et M une diagonale nulle : l'indéfinition est certaine dès que L ≠ 0. Conséquences : P({i}) ∝ L_ii = 0 pour tout singleton, P({i,j}) ∝ −L_ij² < 0 pour toute paire. Aucun tirage n'est défini. Cholesky échoue dans 200 corpus sur 200, en version gloutonne incrémentale comme en version de la bibliothèque d'algèbre linéaire [b2-tirages].

Sinkhorn-Knopp (5 itérations) puis + γI. Écart à la bistochasticité après 5 itérations : 2,9e-4 en médiane. La version symétrisée D L D est une congruence, elle conserve l'inertie : λ_min reste négatif (médiane −0,484). Violations : 1 000 / 1 000 pour γ ∈ {10⁻⁶ ; 10⁻³ ; 10⁻² ; 10⁻¹}. Le γ minimal requis vaut 0,37 à 0,66 (médiane 0,48), soit la moitié d'une somme de ligne, et non une régularisation « de Tikhonov ». À ce γ, la diagonale est constante : la qualité disparaît, et l'effet sur la sélection s'inverse (essai 3).

**Affirmation « garanti semi-défini positif par produit de Schur » : réfutée (1 000 / 1 000 violations).**

### Essai 2 : forme « trace » de la caste 2

Pour d unitaire, P = I − d dᵀ est un projecteur (P² = P à 5,6e-16), donc P^{1/2} = P et Tr(P_i P_j) = D − 2 + ⟨d_i,d_j⟩².

| Mesure (190 000 paires, D = 16) | Valeur |
|---|---|
| \|T − (14 + c²)\| max, racine exacte P^{1/2} = P | **3,6e-15** |
| idem, racine numérique (décomposition propre ; Jacobi de l'organisme sur 20 jeux) | 6,5e-8 ; 3,7e-8. L'erreur est en racine de la précision machine, à cause de la valeur propre nulle de P. |
| \|T − (1 − c²)\| min | **13,0** |
| Plage de T ; corrélation de Pearson T / c² | [14,000 ; 14,732] ; 1,0000000000000 (≥ 0,99999999999998) |
| Semi-définie positivité de ⟨o,o⟩·T | 0 / 1 000 violations ; λ_min ≥ 0,288 |

**Égalité « Tr[…] = 1 − ⟨d,d⟩² » : réfutée. La trace vaut 14 + ⟨d,d⟩².** La forme trace est bien semi-définie positive. Sa dépendance au domaine n'est que de 1/14 (de 14 à 15), et elle va dans le mauvais sens pour la lecture « affinité » du rapport : plus les domaines se ressemblent, plus le terme est grand, alors que (1 − c²) diminue. Dans un processus déterminantal, son terme dominant 14·⟨o_i,o_j⟩ est une similarité, donc une répulsion. Elle écarte les paires qui partagent un opérateur : 5,5 à 16 % d'ensembles bisociatifs contre 33,5 à 71,5 % au hasard (essai 3).

### Essai 3 : correctif et comparaison

Corpus synthétiques. n = 20 articles, 5 domaines, 8 opérateurs. d_i et o_i sont le prototype de leur étiquette plus un bruit isotrope (norme ≈ 0,6), en dimension 16. Trois configurations : étiquettes uniformes et indépendantes ; « hubs » (domaines inégaux, opérateurs selon une loi de Zipf d'exposant 1,2) ; « corrélée » (chaque domaine a un opérateur maison avec probabilité 0,6). 200 corpus par configuration. Sélection gloutonne du déterminant maximal, k = 4, départage au premier indice. Correctif : L = diag(q)(S + 10⁻³ I)diag(q), S_ij = ⟨d_i,d_j⟩². Mesures : « domaines » = part des 6 paires de domaines différents ; « bisoc » = ensembles contenant une paire même opérateur ET domaines différents (l'association visée) ; « q » = qualité moyenne. Les méthodes c3 à c5 utilisent les étiquettes d'opérateur, supposées extraites.

| Méthode | domaines (unif. / hubs / corr.) | bisoc (unif. / hubs / corr.) | q |
|---|---|---|---|
| hasard | 0,793 / 0,744 / 0,790 | 0,500 / 0,715 / 0,335 | 0,99-1,02 |
| tri par qualité (analogue d'un tri séparable) | 0,812 / 0,738 / 0,794 | 0,490 / 0,675 / 0,305 | 1,37-1,38 |
| a1 rapport, déterminant signé | 0,848 / 0,794 / 0,810 | 0,930 / 0,935 / 0,705 | 1,12-1,13 |
| a2 rapport, \|det\| (code de la caste 1) | 0,849 / 0,821 / 0,655 | 0,975 / 0,985 / 0,735 | 1,14-1,16 |
| a3 rapport réparé (Sinkhorn + γ minimal) | 0,726 / 0,615 / 0,808 | **0,000 / 0,060 / 0,005** | 0,99-1,00 |
| b forme trace | 0,828 / 0,734 / 0,854 | **0,055 / 0,160 / 0,050** | 1,33-1,36 |
| c1 correctif | **0,947 / 0,896 / 0,929** | 0,585 / 0,770 / 0,415 | 1,35-1,37 |
| c3 correctif, partage dans q (q·(1 + partenaires bisociatifs)) | 0,945 / 0,906 / 0,921 | 0,915 / 0,985 / 0,870 | 1,27-1,29 |
| c4 correctif conditionné à un opérateur-pivot | 0,894 / 0,843 / 0,728 | 1,000 / 0,995 / 0,975 | 1,10-1,20 |
| c5 correctif, paire garantie après tirage | **0,936 / 0,891 / 0,922** | **1,000 / 1,000 / 0,995** | 1,32-1,35 |

Erreurs-types : ≤ 0,021 sur « domaines », ≤ 0,035 sur « bisoc ». Une paire bisociative existe dans 200, 200 et 199 corpus.

Lecture dans les deux sens.
- En glouton, la forme du rapport favorise le partage d'opérateur entre domaines (bisoc 0,705 à 0,985), mais par accident algébrique. Avec une diagonale nulle, le déterminant à 3 éléments vaut 2·L_ab·L_ac·L_bc et récompense un triangle d'affinités. Ce n'est pas un processus déterminantal : Cholesky échoue (200 / 200), 17 à 25 % des sous-ensembles de taille 4 ont un déterminant négatif, et aucun tirage n'existe. Dès qu'on le rend semi-défini positif, il fait l'inverse (bisoc 0,000 à 0,060). Sur le critère P2 du rapport (paires ⟨d,d⟩ < 0,25 et ⟨o,o⟩ > 0,5), a2 obtient 0,48 / 0,55 / 0,34 et le correctif c1 seulement 0,13 / 0,20 / 0,08.
- Le correctif donne la meilleure diversité de domaines à qualité conservée. Le partage d'opérateur n'y est ni favorisé ni détruit : c1 vaut 0,585 / 0,770 / 0,415 contre 0,500 / 0,715 / 0,335 au hasard. Un processus déterminantal ne sait que repousser : par l'inégalité de Hadamard, det(L_S) ≤ Π L_ii, et toute similarité hors diagonale fait baisser la probabilité. L'attraction voulue sur l'opérateur ne peut donc pas être mise dans le noyau. **Il faut la réintroduire après tirage (c5)** : bisoc 0,995 à 1,000 pour un coût de 0,005 à 0,011 en diversité et de 0,008 à 0,039 en qualité. Dans q (c3), c'est moins sûr, car un score unaire ne garantit pas la paire. Le conditionnement (c4) coûte en diversité (0,728 en configuration corrélée) et en qualité.

Dégénérescence (tirage exact de taille 4, loi P(S) = det(L_S)/Σ sur les 4 845 sous-ensembles ; 20 corpus par configuration ; 50 tirages, une graine chacun) [b2-degen] :

| Noyau (configuration uniforme ; entre parenthèses, plage sur les 3 configurations) | prob. modale (moy.) | distincts / 50 (moy. ; min) | domaines E[·] | bisoc E[·] | rang(q, inclusion) |
|---|---|---|---|---|---|
| c1 correctif, sans Sinkhorn ni γ | 0,0025 | 49,15 ; 46 | 0,839 (0,778-0,846) | 0,491 | **0,96** (0,95-0,97) |
| c1 + γ = 10⁻³·λ_max | 0,0025 | 49,15 ; 46 | 0,838 | 0,491 | 0,96 |
| Sinkhorn sur S seul + γ | 0,0041 | 49,35 ; 48 | 0,862 (0,827-0,868) | 0,497 | **0,83** (0,77-0,83) |
| Sinkhorn sur L entier + γ | 0,0013 | 49,75 ; 49 | 0,865 | 0,512 | **0,03** (0,03-0,05) |
| b forme trace | 0,0028 | 49,25 ; 47 | 0,798 | 0,337 | 0,96 |
| a réparé (Sinkhorn + γ minimal) | 0,00025 | 49,55 ; 48 | 0,797 | 0,416 | 0,04 |
| rapport brut ; Sinkhorn + γ = 10⁻³ | indéfini (17-25 % ; 11-17 % de déterminants négatifs) | — | — | — | — |
| forme trace + Sinkhorn | Sinkhorn impossible (entrées négatives, ⟨o,o⟩ non carré) | — | — | — | — |
| référence uniforme | 0,0002 | 49,75 attendu | 0,799 | 0,474 | — |

- Aucune dégénérescence du tirage exact à n = 20, avec ou sans Sinkhorn + γI. On obtient 44 à 50 ensembles distincts sur 50 graines (moyennes 48,6 à 49,9) pour une probabilité modale ≤ 0,013. Pourtant les 3 premières valeurs propres portent 53 à 71 % de la trace : la dominance spectrale invoquée par la caste 3 est réelle, mais elle n'entraîne pas d'effondrement.
- Le glouton que le rapport implante est déterministe : 1 ensemble distinct sur 50 permutations de l'ordre du corpus, avec ou sans Sinkhorn + γI (1,05 à 1,1 pour « a réparé », par quasi-égalités). Sinkhorn + γI n'y change rien.
- γ augmente le nombre effectif d'ensembles en uniformisant. Pour γ de 0 à 10·λ_max, la diversité attendue passe de 0,839 à 0,796, soit la valeur uniforme 0,799 ; la diversité est perdue, pas gagnée.
- Sinkhorn sur L entier efface q : à convergence exactement, puisque l'échelonnement bistochastique de diag(q) K diag(q) est celui de K ; après 5 itérations, la corrélation de rang passe de 0,96 à 0,03. Sinkhorn sur S seul garde q (0,77 à 0,83) et gagne 0,02 à 0,05 de diversité. **S'il faut Sinkhorn, c'est sur S seulement.**

## 2. Brique 3 — répulsion et pivots de Swanson

### Seuil d'entrée du pivot

`termes_satures` = jetons de fréquence documentaire ≥ max(2, ⌊0,75 n⌋), triés par (−fréquence, ordre alphabétique), 6 premiers. Le seuil réel vaut ⌊0,75 n⌋/n : 60 % à n = 5, 70 % à n = 10, 75 % à n = 20.

Corpus : textes A et C sur deux vocabulaires disjoints (60 mots chacun, loi de Zipf), pivot B dans m des n textes en alternance A/C, k mots-outils présents dans tous les textes (plus 20 mots-outils à probabilité 0,5 quand k > 0). 200 graines par cellule. Probabilité que B soit dans `termes_satures` [b3-synth] :

| n (seuil) | k = 0 | k = 3 | k = 6 | k = 12 |
|---|---|---|---|---|
| 5 (3/5) | f = 0,6 : 0,73 à 1,00 ; f ≥ 0,8 : 1,00 | f = 0,6 : 0,00-0,07 ; 0,8 : 0,77-0,97 ; 1 : 1,00 | 0 pour f < 1 ; f = 1 : 0,98-1,00 | 0 pour f < 1 ; f = 1 : 1,00 (« calcium ») / **0,00** (« magnesium ») |
| 10 (7/10) | 0 pour f ≤ 0,6 ; **1,00 dès f = 0,7** | f = 0,7 : 0,73-0,89 ; ≥ 0,8 : 0,97-1,00 | 0 pour f < 1 ; f = 1 : 1,00 | 0 pour f < 1 ; f = 1 : 1,00 / **0,00** |
| 20 (15/20) | 0 pour f ≤ 0,7 ; **1,00 dès f = 0,75** | idem k = 0 | 0 pour f < 1 ; f = 1 : 1,00 | 0 pour f < 1 ; f = 1 : 1,00 / **0,00** |

Le pivot entre dès f ≥ ⌊0,75 n⌋/n tant que moins de 6 jetons le précèdent. Avec 6 mots-outils omniprésents ou plus, il n'entre jamais pour f < 1. À f = 1, il n'entre que si l'ordre alphabétique le place parmi les 6 premiers ex aequo : « calcium » oui, « magnesium » non avec 12 mots-outils. Le plafond de 6 et les mots-outils protègent donc le pivot, par accident.

### Cas réel : la liste du rapport (gen18)

Les 5 textes des castes, reconstruits depuis le rapport (corps + ligne de vote JSON pour les castes 2 à 5), redonnent **exactement** capacité 3,618972, gain 0,723794, similarité 0,305903 et les 6 termes [b3-gen18]. Il y a 35 jetons présents dans les 5 textes, 67 dans 4 et 93 dans 3 : 195 candidats pour 6 places. **Les 6 termes du rapport sont les 6 premiers, par ordre alphabétique, des 35 ex aequo.**

| Jeton | Nature |
|---|---|
| aux, dans | mots-outils |
| confiance | clé JSON imposée par le gabarit de consigne. Les autres mots du gabarit présents partout (« incertitude », « position », « raisonnement ») sont coupés par l'ordre alphabétique. |
| cholesky | mot de la question |
| article, bruit | vocabulaire du sujet (« bruit » vient en partie de « bruitée » coupé par l'accent) |

Les 35 ex aequo se répartissent ainsi : 15 mots-outils ou nombres, 9 mots de la question (dont « ponts », « swanson », « tirage »), 4 clés du gabarit, 1 fragment d'accent, 6 autres mots du sujet. **Aucun pivot.** Les 5 textes répondent à la même question : il n'y a pas de littératures A et C disjointes, la notion de pivot de Swanson ne s'applique pas. Les listes réellement injectées dans les consignes étaient, pour la caste 3 (2 textes), ['100', '200', '256', '_score_pertinence_texte', 'aire', 'amalgam'] : 3 nombres, un nom de fonction, 2 fragments d'accents. Pour la caste 4 (3 textes) : ['100', '256', '_score_pertinence_texte', 'article', 'aux', 'avec'].

### Remèdes

Vérité terrain : pivot B (à garder), hub générique H présent dans 90 % des textes des deux domaines (à repousser), mots-outils (à ignorer). 200 graines par cellule. « paire-pont bloquée » signifie qu'une paire (B, mot de domaine) est repoussée, ce qui bloque le pont lui-même. Pour (c), la « rétention » stricte compte aussi les paires (B, mot-outil) et (B, H), qui ne bloquent pas de pont.

| Remède (k = 12 mots-outils, f = 0,8) | rétention de B | paire-pont bloquée | H repoussé | part de mots-outils dans la liste | liste vide | unités comptées |
|---|---|---|---|---|---|---|
| base (organisme) n = 5 ; n = 20 | 1,00 ; 1,00 | 0 ; 0 | 0,00 ; 0,00 | **1,00 ; 1,00** | 0 ; 0 | 239 ; 954 jetons |
| (a) liste d'arrêt | **0,00 ; 0,00** | 1,00 ; 1,00 | 0,95 ; 0,99 | 0 ; 0 | 0 ; 0 | idem |
| (b) exemption des ponts entre groupes contrastés (τ = 0,5, 0,7 ou 0,9 : identiques) | 1,00 ; 1,00 | 0 ; 0 | **0,01 ; 0,00** | 0 ; 0 | 0,00 ; **1,00** | + bissection spectrale |
| (b+) idem, et seulement si la fréquence de fond est ≤ 0,1 | **1,00 ; 1,00** | 0 ; 0 | **0,96 ; 0,99** | 0 ; 0 | 0,00 ; 0,01 | + corpus de fond (300 textes) |
| (c) paires co-occurrentes, brutes | 1,00 ; 1,00 | 0 ; 0 | 0,44 ; 0,14 | **1,00 ; 1,00** | 0 ; 0 | 5 638 ; 22 401 paires |
| (c) paires co-occurrentes, après liste d'arrêt | 0,34 ; 0,46 | 0 ; 0 | 0,80 ; 0,54 | 0 ; 0 | 0,00 ; 0,47 | 1 618 ; 6 447 paires |

- Sans mots-outils (k = 0) et à f ≥ seuil, la base et (a) détruisent B dans 57 à 100 % des cas (100 % dès f = 0,8). C'est le seul régime où l'affirmation du rapport est vraie.
- (b) garde B mais exempte aussi H : un pivot et un hub générique ont la même distribution dans un corpus à deux domaines, et aucune règle interne au corpus ne les sépare. La répulsion est vidée (liste vide 100 % pour n ≥ 10). Sur les textes réels, le contraste vaut 0,47 < τ : rien n'est exempté et (b) se comporte comme (a). La marge est mince (0,47 contre τ = 0,5) : la bissection retient la bipartition de contraste maximal, alors que la moyenne sur toutes les bipartitions vaut 0,08.
- Seul (b+), avec une référence externe, garde B et repousse H.
- (c) ne bloque aucune paire-pont pour n ≥ 10. **À n = 5 et f = 1 (5 textes, le régime réel de la question ouverte), il en bloque dans 78 à 79 % des corpus** : un mot de A présent dans les 3 textes A atteint le seuil 3/5. Il perd H quand H est seul fréquent (liste vide 100 % à f = 0,6 pour n ≥ 10, après liste d'arrêt). Sur les textes réels, les 6 paires repoussées sont toutes ('article', x), encore par ordre alphabétique.

Coût du graphe de ligne [b3-synth] : sur 28 corpus (longueurs 30 à 240, d_B de 45 à 642), le comptage explicite des arêtes passant par B est égal à C(d_B, 2) dans 28 cas sur 28. La pente log-log est **2,007**. Le graphe de ligne complet compte 0,88 à 17,7 millions d'arêtes pour 20 textes synthétiques, et **2,21·10⁸** pour les 5 textes réels [b3-gen18] (1 191 jetons, 334 406 paires distinctes, 707 455 arêtes par jeton présent partout). La version par bigrammes orientés coûte d_entrée·d_sortie (≤ 324 ici), mais sur les textes réels ses paires saturées sont des artefacts : ('confiance', 'incertitude'), ('cat', 'goriel'), ('cha', 'raisonnement').

## 3. Brique 4 — fusion « pushout »

### Biais de verbosité du score de fertilité

Fonctions `extraire_termes` et `pushout_conceptuel` copiées à l'identique du code de la caste 1 [b4].

Ponts constants (p ponts plantés 3 fois dans chaque texte, V mots propres par texte) :

| p | score original, V = 2 → V ≥ 30 − p (plafond des 30 termes) | score normalisé, idem |
|---|---|---|
| 1 | 1,61 → 4,08 (×2,53) | 0,322 → 0,069 (×0,21) |
| 3 | 4,83 → 12,02 (**×2,49**) | 0,690 → 0,211 (×0,31) |
| 8 | 12,88 → 30,45 (×2,37) | 1,073 → 0,586 (×0,55) |

Population réaliste : 2 000 paires, p vrai de 0 à 6, longueurs de 10 à 150 jetons par texte, 30 % de vocabulaire général partagé, donc des ponts fortuits.

| Score | corr. de rang avec p vrai | avec la verbosité | partielle verbosité \| p | partielle p \| verbosité |
|---|---|---|---|---|
| original | 0,837 | 0,274 | **0,534** | 0,877 |
| normalisé \|ponts\|/\|union\|·log(1 + \|diff. sym.\|) | **0,872** | 0,153 | **0,351** | 0,886 |
| \|ponts\| seul | 0,857 | 0,228 | 0,477 | 0,885 |

Dans les strates de p, la corrélation avec la verbosité vaut 0,50 à 0,61 pour l'original et 0,22 à 0,45 pour le normalisé. Le résidu vient des ponts fortuits, qui croissent avec la longueur : 1,53, 2,34 puis 3,20 ponts en moyenne selon la tranche. **Le biais est établi. La normalisation le réduit sans l'annuler, et l'inverse à ponts strictement constants.** Corriger le résidu demanderait de comparer le recouvrement à son attendu sous hasard, ou de pondérer les ponts par leur rareté de fond. Ce n'est pas testé ici.

### Filtre de compatibilité des contraintes

Filtre minimal. Quatre axes (linéaire / non linéaire, stationnaire / transitoire, discret / continu, convexe / non convexe), formes françaises et anglaises, expression Unicode, formes négatives masquées avant de chercher les positives. Il y a contradiction si un texte vaut + et l'autre − sur un même axe ; un texte portant les deux marqueurs vaut « ± » et n'est pas compté. Corpus : 200 corpus de 20 textes (10 A, 10 C), valeur plantée +, − ou ∅ par axe (probabilités 0,3 / 0,3 / 0,4), d'où environ 56 % de paires contradictoires. Bruits : paraphrase hors lexique, mention du marqueur contraire hors affirmation, homographe « continue ». Les fusions candidates sont les paires A×C d'interface non vide selon `pushout_conceptuel`.

| Régime (paraphrase, mention contraire, homographe) | candidates | contradictoires acceptées sans filtre | avec filtre | précision | rappel | rejets à tort |
|---|---|---|---|---|---|---|
| propre (0 ; 0 ; 0) | 11 593 | 57,4 % | **0,0 %** | 1,000 | 1,000 | 0,0 % |
| réaliste (0,15 ; 0,15 ; 0,10) | 11 676 | 55,9 % | **34,4 %** | 0,938 | 0,608 | 5,1 % |
| bruité (0,30 ; 0,30 ; 0,20) | 11 726 | 56,3 % | **48,1 %** | 0,817 | 0,354 | 10,2 % |

Par construction, la part de contradictions *détectées* parmi les fusions acceptées est de 0 % avec filtre ; sans filtre, elle vaut 57,4 %, 36,3 % ou 24,4 % selon le régime. Par ailleurs, **65 à 67 % des fusions candidates n'ont aucun des ponts plantés dans leur interface** : la condition « B = O_A ∩ O_C non vide » est remplie par les mots du gabarit et les marqueurs eux-mêmes.

## 4. Verdicts par affirmation

| Code | Affirmation (source) | Verdict | Chiffre |
|---|---|---|---|
| F1 | `principal.py` trie par `_score_pertinence_texte` (question, rapport) | réfutée | 0 occurrence |
| F2 | `mitose_spectrale.py` calcule 0,5 log det(I + SNR G) par Cholesky ; « décomposition de Cholesky existante » (question, rapport) | réfutée | l. 31-42 : approximation n/(1 + (n − 1) s̄) ; 0 Cholesky |
| A1 | L = q q ⟨o,o⟩²(1 − ⟨d,d⟩²) garanti semi-défini positif par produit de Schur (rapport, castes 2 et 5) | **réfutée** | 1 000 / 1 000 ; λ_min médiane −0,715 ; diagonale nulle |
| A2 | Tr[(I − d_i d_iᵀ)^{1/2}(I − d_j d_jᵀ)^{1/2}] = 1 − ⟨d_i,d_j⟩² (caste 2) | **réfutée** | = 14 + ⟨d,d⟩² à 3,6e-15 ; écart ≥ 13,0 |
| A3 | La forme trace est semi-définie positive (caste 2) | établie | 0 / 1 000 ; λ_min ≥ 0,288 |
| A4 | La forme trace couple similarité d'opérateur et orthogonalité de domaine (caste 2) | réfutée | bisoc 0,055 / 0,160 / 0,050 contre 0,500 / 0,715 / 0,335 au hasard |
| A5 | 5 itérations de Sinkhorn-Knopp + γI rendent le noyau du rapport utilisable (rapport) | réfutée | violations 1 000 / 1 000 pour γ ≤ 0,1 ; γ min 0,37-0,66 ; réparé : bisoc 0,000-0,060 |
| A6 | Un processus déterminantal dégénère en top-k à n ≈ 20 (caste 3) ; Sinkhorn + γI l'évite (rapport) | réfutée (les deux) | tirage exact : 48,6-49,9 distincts / 50 avec ou sans ; glouton : 1 / 50 avec ou sans |
| A7 | Sinkhorn-Knopp neutralise les hubs sans détruire la définie-positivité (caste 4) | partielle | inertie conservée (congruence) ; sur L entier, q effacé (rang 0,96 → 0,03) ; sur S seul, q gardé (0,77-0,83), diversité +0,02 à +0,05 |
| A8 | Correctif : similarité de domaine dans S, qualité à part → domaines éloignés (consigne) | établie | domaines 0,896-0,947 contre 0,744-0,793 ; q 1,35-1,37 |
| A9 | Le correctif perd le partage d'opérateur (consigne) | partielle | au niveau du hasard (0,415-0,770 contre 0,335-0,715) ; après tirage : 0,995-1,000 |
| B1 | La répulsion actuelle détruit les pivots B en les traitant comme termes saturés (castes 2 et 5) | partielle → réfutée pour l'organisme réel | liste réelle : 0 pivot ; pivot listé seulement si f ≥ ⌊0,75 n⌋/n et < 6 mots-outils omniprésents |
| B2 | La répulsion sur le graphe de ligne préserve les pivots (castes 2 et 5) | partielle | paire-pont bloquée 0 % pour n ≥ 10, 78-79 % à n = 5, f = 1 ; hub perdu |
| B3 | Un pivot de degré d_B génère C(d_B, 2) = O(d_B²) arêtes du graphe de ligne (caste 4) | établie | 28 / 28 égalités ; pente 2,007 ; 2,21·10⁸ arêtes sur gen18 |
| B4 | … et sature la matrice de Cholesky en O(d_max⁶) (caste 4) | non testée | aucune factorisation de Cholesky du graphe de ligne dans le code |
| R1 | Remède (a), liste d'arrêt (consigne) | partielle | liste nettoyée (mots-outils 1,00 → 0) mais pivot exposé (rétention 0,00 dès f = 0,8 ; 0,43-0,45 au seuil exact à n = 5) |
| R2 | Remède (b), exemption des ponts entre domaines contrastés (consigne) | partielle | rétention 1,00 mais hub repoussé 0,00-0,01, liste vide 100 % (n ≥ 10) |
| R3 | Remède (b+), exemption avec fréquence de fond (ajouté) | établie | rétention 1,00 ; hub 0,95-0,99 ; mots-outils 0 |
| C1 | Le score \|ponts\|·log(\|A\| + \|B\| + 1) mesure la fertilité (caste 1) | réfutée (biaisé) | ×2,49 à ponts constants (p = 3) ; partielle verbosité 0,534 |
| C2 | Version normalisée \|ponts\|/\|union\|·log(1 + \|diff. sym.\|) corrige le biais (consigne) | partielle | partielle 0,534 → 0,351 ; rang avec p vrai 0,837 → 0,872 ; inversion à ponts constants (×0,31) |
| C3 | Le filtre de compatibilité garantit que le pushout ne fusionne pas des formalismes incompatibles (castes 4 et 5) | partielle | 57,4 % → 0,0 % (propre) ; 55,9 % → 34,4 % (réaliste) ; 56,3 % → 48,1 % (bruité) |
| C4 | Une interface B = O_A ∩ O_C non vide signale un pont opératoire (castes 2 et 5) | réfutée | 65-67 % des interfaces sans aucun pont planté |

## 5. Réserves

- Tout est synthétique, sauf les 5 textes de gen18, reconstruits exactement. Les taux absolus (bisoc, contradictions) dépendent des paramètres des générateurs, documentés dans chaque fichier de résultats ; les comparaisons entre méthodes, à corpus et graines égaux, sont la partie transposable.
- Les méthodes c3 à c5 utilisent les étiquettes d'opérateur. En pratique il faudrait les extraire, et c'est la limite que le rapport reconnaît lui-même pour les résumés de moins de 150 mots.
- J'ai défini moi-même le remède (b) : groupes par bissection spectrale, contraste = 1 − sim_inter/sim_intra. Une première définition, 1 − cos des centroïdes sur le vocabulaire privé des candidats, donnait 0,95, puis 0,77, sur des textes de même sujet : elle a été rejetée avant les runs finaux. Le seuil τ n'est étalonné que sur deux situations (deux domaines disjoints ; gen18 à 0,47), et la marge sur gen18 est mince. (b+) suppose un corpus de fond. L'archive de l'organisme pourrait en tenir lieu, ce qui n'est pas vérifié.
- Le filtre de contradictions est évalué sur un lexique que j'ai écrit et sur des bruits que j'ai choisis. Son rappel réel sur des résumés moissonnés est inconnu (affirmation C3 indécise sur ce point).
- Résultats « trop propres » à auditer (R4) : 1 000 / 1 000 en A1 et 0 / 1 000 en A3 sont des conséquences algébriques exactes (diagonale nulle ; produit de Schur de facteurs semi-définis positifs), pas des coïncidences d'échantillon. 28 / 28 en B3 est une identité de comptage. Le 0,0 % du filtre propre tient à un lexique planté identique à celui du détecteur.

## 6. Fichiers et empreintes

| Code | Fichier (sous `sortie/`) | SHA-256 |
|---|---|---|
| [b2-psd] | `resultats-b2-psd-trace-v1.json` | `57f816234f81becb3a1fd74403fa7126b83d004824aa2dac15fc389ffb172170` |
| [b2-tirages] | `resultats-b2-tirages-v1.json` | `abc28160eeed51048f274983995ac694eb3761a1005d036fb3356e810d595ccb` |
| [b2-degen] | `resultats-b2-degenerescence-v1.json` | `6d97d6a3607735d6e6aabfc0839ba42554409f87619cbce34f98afa3b0bf0a83` |
| [b3-gen18] | `resultats-b3-gen18-v1.json` | `cb9f6a8c33d8f0e0de2c360becd5e42792b8115eef6b2b87aa41fd24b0889306` |
| [b3-synth] | `resultats-b3-synthetique-v1.json` | `d81dde06b69b5846fccb5b40527ff6381febc2f50d050c6ccc07f4878d6c9ce6` |
| [b4] | `resultats-b4-v1.json` | `a60706696d26013faccb05261defa06f127d0d6a139efc36d28ffe3a7b4c6db2` |
| [instrument] | `resultats-instrument-jacobi-v1.json` | `b3675a120e18192002a6098db248534ade8203db4cc96e8643a4cc4379db684b` |
| manifeste | `manifeste-essais-v1.json` (versions, graines, empreintes des fournis et du code) | `ec1277af235eb6b99a766c4ca286cc3169942b919fe3818648e338209fbf4c9a` |

Code : `commun_v1.py`, `corpus_articles_v1.py`, `textes_v1.py`, `essai_b2_psd_trace_v1.py`, `essai_b2_tirages_v1.py`, `essai_b2_degenerescence_v1.py`, `essai_b3_gen18_v1.py`, `essai_b3_synthetique_v1.py`, `essai_b4_v1.py`, `essai_instrument_jacobi_v1.py`, `manifeste_v1.py`, `lancer_tout_v1.sh`. Chaque fichier a son compagnon `.sha256`.

## 7. Génération 0 — survit / éliminée / indécise

- F1 — tri de `principal.py` par `_score_pertinence_texte` : **éliminée** (fonction absente).
- F2 — capacité par log-déterminant et Cholesky existante dans `mitose_spectrale.py` : **éliminée** (ni l'un ni l'autre dans le code).
- A1 — noyau du rapport garanti semi-défini positif par produit de Schur : **éliminée** (1 000 / 1 000 violations).
- A2 — égalité « trace = 1 − ⟨d,d⟩² » : **éliminée** (trace = 14 + ⟨d,d⟩²).
- A3 — forme trace semi-définie positive : **survit** (0 / 1 000).
- A4 — forme trace au service du couplage d'opérateur entre domaines : **éliminée** (bisoc 0,05-0,16 contre 0,34-0,72 au hasard).
- A5 — Sinkhorn-Knopp (5 itérations) + γI répare le noyau du rapport : **éliminée** (γ ≥ 0,37 requis, et l'effet s'inverse).
- A6 — dégénérescence en top-k à n ≈ 20, évitée par Sinkhorn + γI : **éliminée** (48,6-49,9 distincts / 50 en tirage exact ; glouton déterministe dans tous les cas).
- A7 — Sinkhorn-Knopp sans dommage : **survit sur S seul, éliminée sur L entier** (q effacé, rang 0,96 → 0,03).
- A8 — correctif « similarité de domaine dans S, qualité à part » : **survit** (diversité 0,896-0,947, qualité conservée).
- A9 — partage d'opérateur à réintroduire hors du noyau, après tirage : **survit** (bisoc 0,995-1,000, diversité 0,891-0,936).
- B1 — la répulsion actuelle détruit les pivots : **éliminée** telle qu'énoncée pour l'organisme (0 pivot dans la liste réelle) ; sa version conditionnelle, « un pivot sans concurrent est listé dès f ≥ ⌊0,75 n⌋/n », **survit**.
- B2 — le graphe de ligne préserve les pivots : **indécise** (vraie pour n ≥ 10, fausse à n = 5 et f = 1 : 78-79 %) ; comme remède retenu, **éliminée** (dominé par b+).
- B3 — coût en C(d_B, 2) = O(d_B²) : **survit** (pente 2,007).
- B4 — saturation de Cholesky en O(d_max⁶) : **indécise** (non testée).
- R1 — liste d'arrêt seule : **éliminée** comme remède (expose le pivot) ; **survit** comme premier étage.
- R2 — exemption des ponts entre domaines contrastés, seule : **éliminée** (exempte aussi le hub, vide la liste).
- R3 — exemption avec fréquence de fond : **survit** (rétention 1,00, hub 0,95-0,99).
- C1 — score de fertilité de la caste 1 : **éliminée** (biais de verbosité ×2,49).
- C2 — score normalisé : **indécise** (meilleur, partielle 0,351, mais biais résiduel non nul).
- C3 — le filtre de compatibilité garantit l'absence de contradiction : **éliminée** comme garantie (34,4 % restants en régime réaliste) ; le filtre minimal comme réducteur : **indécise** (rappel réel sur résumés inconnu).
- C4 — interface non vide = pont opératoire : **éliminée** (65-67 % d'interfaces sans pont réel).

<<<FIN C3b>>>

<<<DÉBUT — synthèse du tour « pôle » précédent (R-525)>>>
# Pôle « scientifique automatique » — synthèse du tour du collisionneur (v1)

- **Pour** Lazar. Écrite le 26 octobre 2026 par la lignée « session-depot », à partir des neuf cellules du tour (GO-2026-10-26-06, R-524 ; `donnees/collisionneur-pole-scientifique-v1`, `0fbf92d`). Matériau de décision, jamais une consigne. Rien d'opposable (R7) ; les étiquettes RAPPORTÉ / HYPOTHÈSE sont celles des modèles.
- **Modèles** : A = Fable 5.1, B = Opus 5.5, C = Gemini. Trois tours (conception, équipe rouge croisée, riposte), neuf cellules valides, aucun refus, 7,82 USD.
- **Réserve forte** : la pièce C (méta-conception v6.3 et sa relecture) **n'a pas été servie** ; les trois modèles le signalent et refusent de conclure sur la recombinaison bisociative (point 3). Demandée à conv-audit (n° 76).

## Verdict en cinq lignes

1. **« Perfectionner le nôtre » et « adopter un système de la littérature » sont rejetés tels quels par les trois.** La réponse convergente est une **voie hybride ancrée sur notre noyau**.
2. Ce qui a de la valeur chez nous, ce n'est pas l'organisme, c'est **le noyau** : clés jamais exposées, bornes d'appels/temps/moisson, et surtout, depuis la correction C-17, l'agent ne peut plus soumettre de code brut (gabarit de trois paramètres bornés). C'est une sûreté acquise.
3. **La première expérience n'est pas « quel moteur », c'est « notre critère de sélection promeut-il du faux ? ».** Processeur seul, moins de 20 USD, cette semaine. Si le filtre laisse passer les paris couverts et les hypothèses à domaine étroit, **n'importe quel** générateur (le nôtre ou celui de la littérature) converge vers des artefacts de Goodhart.
4. **Agentic Scientist v3 est écarté** tant que ses agents héritent des clés (sûreté), malgré son évaluation finale scellée.
5. La capacité « réécrire son propre code » (point 4) **n'existe pas** chez nous aujourd'hui (C-17 l'a retirée pour la sûreté) : elle est à **concevoir sous bac à sable**, pas à « perfectionner ».

## Les points de convergence des trois modèles

- **Architecture recommandée** : garder le noyau (sûreté), y greffer l'idéation/mutation d'un moteur de la littérature **en conteneur sans clés** *si* la première expérience montre notre grammaire bornée insuffisante, et ajouter un **évaluateur figé tenu par le noyau, hors des agents** — absent des deux voies aujourd'hui.
- **Sélection darwinienne sans Goodhart** : sévérité *ex ante* — le test et le nul sont **figés par le noyau avant** l'expérience, les tirages sont **frais après** l'engagement de l'hypothèse. Nul **composite** (bibliothèque de prédicteurs aveugles au domaine ; inférence universelle de Wasserman–Ramdas) pour que l'inégalité de Ville tienne même si le nul n'est pas exactement connu. **Contenu** d'une hypothèse = risque déclaré (divergence à une référence) × couverture du domaine : un pari couvert est classé bas, une hypothèse qui ne prédit rien ne survit pas.
- **Qui écrit le test** : avec nul figé et tirages après dépôt, peu importe (Ville tient) — mais c'est **à vérifier**, et c'est l'objet de la première expérience.
- **Recombinaison bisociative** (sous réserve de la pièce C) : forme minimale = tirage (éloignement des domaines × similarité d'opérateur sur arbre syntaxique **canonisé**) + filtre mécanique de contraintes + fusion ; test sur des mondes à isomorphismes plantés **contre un tirage stratifié recevant exactement le même prompt et le même filtre** ; réfutée si l'écart < ~12 points.
- **Validité de construit des sondes** (B soulève, C adopte) : une sonde linéaire qui lit une **transcription** mesure la représentation du **lecteur**, pas forcément l'état interne de l'agent qui a agi. À garder pour tout le programme.

## La première expérience (convergente, chiffrée par les trois)

**Valider le critère de sélection**, avant tout choix de moteur. Processeur seul, activations réelles mises en cache, moins de 20 USD, deux à trois jours.
1. Étalonnage A/A : deux courses identiques pour fixer le plancher de bruit.
2. Duel sur une population à vérité connue (hypothèses vraies, biais de sous-population, **paris couverts**) : (bras 1) un sélecteur **mécanique** *ex ante* sans appel de modèle, qui choisit les instances où l'hypothèse et le nul divergent le plus ; (bras 2) le même, plus un agent « réfutateur » d'une autre espèce ; (bras 3) la sélection par score moyen (le témoin faible).
3. Contrôles **fatals** : parasite de Kelly et nul dans la bibliothèque → promotion ≤ α ; paris couverts promus seulement si leur part nette est vraie. Un échec invalide le critère et **arrête tout**.
4. Règle d'arrêt : si le bras 1 (mécanique, zéro appel) élimine ≥ 95 % des fausses hypothèses et égale le bras 2 (réfutateur modèle) à un bruit près, on **économise définitivement** les appels du réfutateur et on passe au duel « grammaire bornée contre Python libre sous prison du noyau », qui, lui, tranche la voie.

## Ce qu'aucun modèle n'a pu établir (tous en HYPOTHÈSE)

- Que l'organisme apprenne d'une génération à l'autre, ou que ses castes calibrent mieux qu'une auto-cohérence à budget égal, ou que la mémoire ISVD apporte quelque chose (aucune ablation dans les faits).
- Que la bisociation batte un tirage stratifié (pièce C absente).
- Que les critères de sélection corrigés résistent vraiment (écrits, non courus).
- Qu'un banc synthétique planté prédise le réel (B et A proposent un pont à mesurer).

## Pour toi, maintenant

- **Décision de voie** : hybride ancrée sur le noyau (recommandation des trois). Ce n'est pas un nœud bloquant tout de suite — la première expérience est faisable sans trancher la voie.
- **Dépense** : la première expérience est sur processeur, quasi gratuite (quelques appels de contrôle). Un préenregistrement minimal scellé (R1) suffirait à la lancer.
- **À débloquer** : la pièce C (méta-conception) pour le volet recombinaison.

<<<FIN synthèse R-525>>>
