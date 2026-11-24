*Note sur les pièces transmises [VÉRIFIÉ] :* aucune pièce n'est absente, vide ou coupée ; les blocs `FAITS` et `QUESTION DE L'ARBITRE` sont toutefois identiques (même empreinte `sha256`), de sorte que l'ensemble des entrées fournies est constitué des dix intuitions du chercheur, toutes de statut `HYPOTHÈSE`, sans donnée empirique vérifiée. Les résultats issus de la littérature publiée sont marqués `RAPPORTÉ`. Les sept parties ci-dessous suivent la forme fixée par l'arbitre tout en intégrant explicitement les livrables `(a)` à `(d)` du Tour III.1.

---

## 1. Confrontation à la littérature et présupposés non établis

### 1.1 Livrable (a) : ce que la question suppose sans que ce soit établi

Avant d'évaluer H1–H10, l'énoncé embarque huit présupposés implicites qui ne sont pas établis :
1. **Unité du phénomène `[HYPOTHÈSE]` :** qu'un même mécanisme géométrique engendre à la fois l'intérêt humain, la validité scientifique et la découverte cognitive.
2. **Primauté du mariage éloigné `[HYPOTHÈSE]` :** que les idées fécondes naissent surtout par rapprochement de domaines lointains (H1), plutôt que par raffinement local, résolution d'anomalie empirique ou nouvel instrument.
3. **Suffisance du texte de surface `[HYPOTHÈSE]` :** que la structure relationnelle ou mathématique abstraite est extractible sans supervision depuis le seul langage des publications (H9).
4. **Existence d'un mécanisme physique unifié derrière les exemples historiques `[HYPOTHÈSE]` :** les cas cités (horloges/chemins de fer pour la relativité, mécanique des fluides pour les trous noirs, pomme/Lune) sont des épisodes historiques documentés `[RAPPORTÉ]`, mais leur généralisation en « champ » universel (H5) repose sur un échantillon rétrospectif non audité `[OBSERVÉ-NON-AUDITÉ]`.
5. **Invariance sémantique dans les cascades `[HYPOTHÈSE]` :** que le transfert A–B, B–C vers un domaine jeune (douleur–anesthésie–conscience → motif interne d'un LLM, H2) conserve le sens opératoire des termes intermédiaires sans équivoque.
6. **Auto-filtrage par alignement structurel `[HYPOTHÈSE]` :** que la compatibilité de deux réseaux conceptuels (H3, H6) suffit à écarter les fausses analogies avant l'épreuve empirique.
7. **Opérationnalité des analogies physiques `[HYPOTHÈSE]` :** que les notions de champ ferromagnétique, puits, polarisation, résonance, théorème de Noether, lagrangien et percolation possèdent un équivalent mesurable pertinent sur des graphes conceptuels.
8. **Guide par surprise scalaire `[HYPOTHÈSE]` :** qu'un signal de surprise de type erreur de prédiction (H10) oriente un agent vers des idées scientifiquement fécondes plutôt que vers du bruit imprévisible.

### 1.2 Distinction de trois questions que H1–H10 confondent

Les dix hypothèses mélangent trois objets distincts qu'un modèle doit séparer :
- **Q1 — Ce qui rend une idée intéressante pour un public humain :** propriété *relationnelle et datée* entre une proposition et les croyances a priori d'une communauté à l'instant $t$. Davis (1971, *That's Interesting! Towards a Phenomenology of Sociology and a Sociology of Phenomenology*, *Philosophy of the Social Sciences*) `[RAPPORTÉ]` montre qu'une thèse paraît intéressante lorsqu'elle contredit une assomption tenue pour acquise par son public sans heurter son socle axiomatique. Q1 ne garantit ni vérité ni fécondité : la phrénologie ou les rayons N ont été jugés intéressants en leur temps `[RAPPORTÉ]`.
- **Q2 — Ce qui rend une idée vraie et féconde :** propriété *épistémique et empirique*, liée à sa capacité à formuler des prédictions risquées corroborées par l'expérience, à résoudre des anomalies et à unifier des phénomènes par compression déductive (Kitcher, 1981, *Explanatory Unification*, *Philosophy of Science*) `[RAPPORTÉ]`. Une idée locale et peu surprenante peut être hautement féconde.
- **Q3 — Comment produire une idée :** mécanisme cognitif, social ou algorithmique d'exploration d'un espace d'hypothèses. Un algorithme optimisant Q1 (surprise textuelle) n'optimise pas Q2 (validité empirique).

### 1.3 Verdict sur H1–H10

Toutes les entrées H1–H10 restent de statut `HYPOTHÈSE`. Confrontation aux travaux existants `[RAPPORTÉ]` :

- **H1 (mariage éloigné) — Partiellement soutenue pour Q1/impact, contredite sous forme forte pour Q2/Q3.** Uzzi, Mukherjee, Stringer & Jones (2013, *Atypical Combinations and Scientific Impact*, *Science*) montrent que les articles les plus cités associent un socle *hautement conventionnel* à une injection atypique ciblée, non une grande distance globale. Foster, Rzhetsky & Evans (2015, *Tradition and Innovation in Scientists' Research Strategies*, *American Sociological Review*) montrent que les sauts distants sont rares et risqués. En observation directe de laboratoires, Dunbar (1997, *How scientists think: On-line creativity and conceptual change in science*, dans Ward, Smith & Vaid, *Creative Thought*) montre que les découvertes quotidiennes reposent surtout sur des analogies *locales*, les analogies lointaines servant plutôt à la pédagogie ; Gick & Holyoak (1980, *Analogical problem solving*, *Cognitive Psychology*) documentent la rareté du transfert analogique lointain spontané.
- **H2 (cascades A–B–C et transferts) — Déjà établie comme heuristique (Q3), contredite comme critère de validité (Q2).** Formalisée par Swanson (1986, *Fish Oil, Raynaud's Syndrome, and Undiscovered Public Knowledge*, *Perspectives in Biology and Medicine*). Mais Smalheiser (2012, *Literature-based discovery: Beyond the ABCs*, *JASIST*) montre que la transitivité naïve A–B–C engendre une explosion de faux positifs par polysémie et non-transitivité causale. Le saut vers un « motif d'anesthésie » dans un LLM est une `HYPOTHÈSE` exposée au glissement sémantique.
- **H3 (serrure et clé ; Noether et lagrangien) — Déjà établie pour l'alignement relationnel ; métaphore sans contenu testable pour Noether/lagrangien.** La correspondance de structures relationnelles d'ordre supérieur est la théorie classique de Gentner (1983, *Structure-Mapping: A Theoretical Framework for Analogy*, *Cognitive Science*), implémentée dans SME (Falkenhainer, Forbus & Gentner, 1989, *The Structure-Mapping Engine: Algorithm and Examples*, *Artificial Intelligence*) et ACME (Holyoak & Thagard, 1989, *Analogical Mapping by Constraint Satisfaction*, *Cognitive Science*). En revanche, le théorème de Noether (1918, *Invariante Variationsprobleme*, *Nachrichten von der Gesellschaft der Wissenschaften zu Göttingen*) exige une symétrie différentiable continue d'une action ; sans action continue définie sur des concepts discrets, l'invocation ne produit aucune prédiction mesurable.
- **H4 (ni trop près ni trop loin) — Soutenue pour Q1 et banale sans métrique fixée a priori.** Courbe en U inversé de la curiosité (Berlyne, 1960, *Conflict, Arousal, and Curiosity*, McGraw-Hill), concept d'« adjacent possible » (Kauffman, 2000, *Investigations*, Oxford University Press ; Tria, Loreto, Servedio & Strogatz, 2014, *The dynamics of correlated novelties*, *Scientific Reports*) et pénalisation institutionnelle de la nouveauté extrême (Wang, Veugelers & Stephan, 2017, *Bias against novelty in science: A cautionary tale for users of bibliometric indicators*, *Research Policy*).
- **H5 (champ, air du temps, ferromagnétisme, appariement aléatoire de protéines) — Phénomène des multiples soutenu ; « champ » et « protéines » = métaphores sans contenu testable.** Les découvertes simultanées sont établies (Ogburn & Thomas, 1922, *Are Inventions Inevitable? A Note on Social Evolution*, *Political Science Quarterly* ; Merton, 1961, *Singletons and Multiples in Scientific Discovery*, *Proceedings of the American Philosophical Society*), ainsi que le rôle d'instruments ou d'analogues partagés (Galison, 2003, *Einstein's Clocks, Poincaré's Maps: Empires of Time*, Norton ; Unruh, 1981, *Experimental Black-Hole Evaporation?*, *Physical Review Letters*). Toutefois, Simonton (1979, *Multiple Discovery and Invention: Zeitgeist, Genius, or Chance?*, *Journal of Personality and Social Psychology*) montre qu'un processus de Poisson d'essais indépendants une fois les prérequis disponibles suffit à reproduire la distribution des multiples sans postuler de « champ ».
- **H6 (connexion et distinction / tri des fausses identités) — Partiellement soutenue sur le plan cognitif, contredite comme effet automatique d'une projection géométrique.** Hesse (1966, *Models and Analogies in Science*, University of Notre Dame Press) formalise les analogies positives, négatives et neutres ; Thagard (1989, *Explanatory coherence*, *Behavioral and Brain Sciences*) modélise les contraintes négatives. Mais l'histoire des sciences (fluide calorique, éther élastique `[RAPPORTÉ]`) montre que de riches isomorphismes locaux ne suffisent pas à trier vraies et fausses invariances sans test empirique.
- **H7 (profondeur, concepts nœuds, levée de mystère) — Partiellement soutenue (unification et trous structuraux), vulnérable à la circularité rétrospective.** Kitcher (1981) et Thagard (1989) fondent l'unification explicative ; Burt (2004, *Structural Holes and Good Ideas*, *American Journal of Sociology*) relie les ponts entre communautés à la génération d'idées valorisées. « Expliquer après coup pourquoi elle surprenait » n'est testable que si la surprise est mesurée *avant* la découverte.
- **H8 (émergence, transition de phase, percolation) — Métaphore non testable pour une idée individuelle ; soutenue uniquement au niveau macroscopique de diffusion.** Les seuils de composante géante (Erdős & Rényi, 1960, *On the evolution of random graphs*, *Publ. Math. Inst. Hung. Acad. Sci.*) et les modèles épidémiques de propagation d'idées (Goffman & Newill, 1964, *Generalization of epidemic theory: An application to the transmission of ideas*, *Nature*) décrivent l'adoption collective d'un champ, non la genèse d'une idée singulière.
- **H9 (structure cachée extractible du langage sans supervision) — Partiellement soutenue pour des régularités distributionnelles locales, contredite pour des invariants mathématiques profonds.** Mikolov, Yih & Zweig (2013, *Linguistic Regularities in Continuous Space Word Representations*, NAACL-HLT) et Tshitoyan et al. (2019, *Unsupervised word embeddings capture latent knowledge from materials science literature*, *Nature*) capturent des proximités latentes au sein d'un domaine homogène. Mais Linzen (2016, *Issues in evaluating semantic spaces using word analogies*, RepEval), Rogers, Drozd & Li (2017, *The (Too Many) Problems of Analogical Reasoning with Word Vectors*, *SEM) et Bender & Koller (2020, *Climbing towards NLU: On Meaning, Form, and Understanding in the Age of Data*, ACL) montrent que les espaces vectoriels textuels échouent sur les relations abstraites complexes et ne distinguent pas association lexicale et contrainte causale.
- **H10 (signal de surprise dopaminergique) — Contredite sous forme de surprise brute, soutenue uniquement sous forme de progrès de compression.** Schultz, Dayan & Montague (1997, *A Neural Substrate of Prediction and Reward*, *Science*) établissent que la dopamine code une erreur de prédiction de *récompense*, non une nouveauté épistémique libre. La surprise bayésienne (Itti & Baldi, 2009, *Bayesian surprise attracts human attention*, *Vision Research*) attire l'attention, mais Schmidhuber (2010, *Formal Theory of Creativity, Fun, and Intrinsic Motivation (1990–2010)*, *IEEE TAMD*) et Pathak, Agrawal, Efros & Darrell (2017, *Curiosity-driven Exploration by Self-supervised Prediction*, ICML) montrent qu'un agent maximisant la surprise brute se fige sur du bruit stochastique : seul le *progrès de compression* évite ce piège.

---

## 2. Modèle formel minimal

Seuls quatre éléments survivent à la partie 1 : la séparation entre surface et graphe relationnel typé, l'alignement partiel avec conflits explicites, le choc méthodologique/instrumental daté, et la séparation des fonctions objectifs Q1, Q2, Q3.

### 2.1 Objets, variables et équations

On définit un **graphe multicouche daté** $G_t = (V_t, E_t^{\text{surf}}, E_t^{\text{rel}}, E_t^{\text{soc}})$ construit exclusivement à partir des documents publiés jusqu'à $t$ :
- $V_t$ : concepts normalisés apparus $\le t$.
- $E_t^{\text{surf}}$ : arêtes pondérées de co-occurrence lexicale/bibliographique. Distance de surface inter-domaines $d_t^{\text{surf}}(u,v) \in [0, \infty)$ mesurée par la distance cosinus de plongements textuels datés $\le t$ combinée au plus court chemin pondéré dans $E_t^{\text{surf}}$.
- $E_t^{\text{rel}}$ : graphe relationnel **typé et orienté** issu d'ontologies, de schémas causaux ou d'arbres syntaxiques d'équations (AST) datés $\le t$.
- $E_t^{\text{soc}}$ : couche communautés/auteurs et graphe biparti concepts–méthodes/instruments $M_t$.

**Alignement structurel net (résidu testable de H3 et H6) :** pour deux voisinages relationnels $H_u, H_v \subset (V_t, E_t^{\text{rel}})$ et un appariement injectif partiel $\phi : S_u \to S_v$ tel que $\phi(u)=v$, on définit la couverture relationnelle $C(\phi) \in [0,1]$ (part des relations d'ordre supérieur conservées) et le taux de conflit $K(\phi) \in [0,1]$ (part des relations typées incompatibles ou de signes opposés) :
$$S_t^{\text{struct}}(u,v) = \max_{\phi} \big[ C(\phi) - \lambda K(\phi) \big], \qquad \lambda > 0.$$
En version continue sur graphes pondérés, $1 - C(\phi)$ est remplacé par la distance de Gromov-Wasserstein $\mathrm{GW}(H_u, H_v)$ (Mémoli, 2011, *Gromov–Wasserstein Distances and the Metric Approach to Object Matching*, *Foundations of Computational Mathematics*) `[RAPPORTÉ]`.

**Choc méthodologique partagé (résidu mesurable de H5) :** soit $\mathbf{m}_t(u)$ le vecteur TF-IDF des instruments/méthodes co-utilisés avec $u$ dans $[t-\Delta, t]$. La convergence méthodologique est :
$$I_t(u,v) = \operatorname{sim}\!\big(\mathbf{m}_t(u), \mathbf{m}_t(v)\big) - \operatorname{sim}\!\big(\mathbf{m}_{t-\Delta}(u), \mathbf{m}_{t-\Delta}(v)\big).$$

**Trois équations distinctes pour Q3, Q1 et Q2 :**
1. *Probabilité de naissance d'un lien $e_{uv}$ dans $(t, t+\delta]$ (Q3) :*
$$\operatorname{logit} P\big(e_{uv} \in (t, t+\delta] \mid \mathcal{F}_t\big) = \beta_0 + \beta_1 \log(k_u k_v) - \beta_2 d_t^{\text{surf}}(u,v) + \beta_3 S_t^{\text{struct}}(u,v) + \beta_4 I_t(u,v) + \beta_5 \mathrm{AA}_t(u,v),$$
où $k_u$ est le degré de $u$ dans $E_t^{\text{surf}}$ et $\mathrm{AA}_t(u,v)$ le score d'Adamic-Adar (Adamic & Adar, 2003, *Friends and neighbors on the Web*, *Social Networks*) `[RAPPORTÉ]` sur $E_t^{\text{surf}} \cup E_t^{\text{soc}}$.
2. *Intérêt perçu par un public $C$ à la date $t$ (Q1) :*
$$U_t^{\text{hum}}(u,v \mid C) = D_{\mathrm{KL}}\!\big(P_t(\cdot \mid C, e_{uv}) \,\|\, P_t(\cdot \mid C)\big)\cdot \sigma\!\big(\alpha [S_t^{\text{struct}}(u,v) - \tau]\big) - \gamma\, d_t^{\text{surf}}(u,v),$$
qui produit une courbe non monotone en $d_t^{\text{surf}}$ sans postuler un optimum ad hoc.
3. *Fécondité épistémique d'une hypothèse $h$ associée à $(u,v)$ (Q2) :* non réductible au texte, définie par le gain de compression prédictive hors-échantillon (principe MDL / Schmidhuber, 2010) sur un ensemble d'observations ou d'anomalies $\mathcal{D}$ :
$$Y^{\text{épist}}(h) = L(\mathcal{D} \mid M_t) - L(\mathcal{D} \mid M_t \cup \{h\}) - L(h \mid M_t).$$

### 2.2 Audit des analogies physiques

| Analogie | Verdict | Justification ou équivalent mathématique exact |
|---|---|---|
| **Puits** | **Écartée** | Simple image d'un minimum local ; aucun potentiel conservatif mesurable. |
| **Champ (ferromagnétique)** | **Écartée** | Remplacée intégralement par la covariable observable $I_t(u,v)$ (instruments partagés) et les prérequis communs. |
| **Polarisation** | **Écartée** | Aucun vecteur dipolaire ou orientation antisymétrique mesurable entre concepts. |
| **Résonance** | **Écartée** | Aucun oscillateur ni fréquence propre ; la compatibilité structurelle est déjà $S_t^{\text{struct}}(u,v)$. |
| **Noether et lagrangien** | **Écartée** | Requiert un groupe continu différentiable agissant sur une action ; sur graphes discrets, la grandeur exacte est l'homomorphisme partiel $S_t^{\text{struct}}(u,v)$. |
| **Percolation** | **Écartée pour une idée singulière ; retenue uniquement au niveau macro** | Équivalent exact : fraction $S_{\max}(t)$ de la composante connexe géante de $G_t$ franchissant le seuil critique de Molloy-Reed $\langle k^2\rangle / \langle k\rangle = 2$ (Molloy & Reed, 1995, *A critical point for random graphs with a given degree sequence*, *Random Structures & Algorithms*) `[RAPPORTÉ]`. Mesure l'émergence collective d'un champ, non la genèse d'une idée. |

### 2.3 Modèles de base minimaux (baselines) et comparaison

Le modèle le plus simple expliquant la formation de nouveaux mariages sans aucune des hypothèses H1–H10 comporte trois niveaux emboîtés :
- **B0 (attachement préférentiel seul) :** $\operatorname{logit} P(e_{uv}) = \beta_0 + \beta_1 \log(k_u k_v)$ (Barabási & Albert, 1999, *Emergence of Scaling in Random Networks*, *Science*) `[RAPPORTÉ]`.
- **B1 (proximité topologique et sociale mécanique) :** B0 augmenté de $-d_t^{\text{surf}}(u,v)$ et de $\mathrm{AA}_t(u,v)$ sur $E_t^{\text{surf}} \cup E_t^{\text{soc}}$. Capture mécaniquement la proximité locale et les chaînes courtes A–B–C sans structure cachée.
- **B2 (nouveauté combinatoire par urnes de Pólya corrélées) :** modèle de Tria et al. (2014) `[RAPPORTÉ]`, qui engendre l'apparition corrélée de nouveautés et l'adjacent possible sans alignement structurel ni champ.

**Comparaison :** notre modèle minimal n'ajoute à B1 que deux termes testables : $\beta_3 S_t^{\text{struct}}$ et $\beta_4 I_t$. Si ces deux coefficients n'améliorent pas la prédiction hors-échantillon temporel par rapport à B1, le modèle minimal doit être abandonné au profit de B1.

---

## 3. Données brutes et extraction des variables

1. **Corpus datés en texte intégral et métadonnées :** **OpenAlex** (métadonnées, concepts hiérarchiques, citations, auteurs, dates), **PubMed Central Open Access (PMC OA)** et **sources LaTeX d'arXiv**. Ils fournissent $V_t$, les degrés $k_u$, le graphe social $E_t^{\text{soc}}$, la distance de surface $d_t^{\text{surf}}$ et les trajectoires de citations postérieures. Les sections « Méthodes » de PMC OA et d'arXiv alimentent les profils instrumentaux $\mathbf{m}_t(u)$ pour $I_t(u,v)$.
2. **Ontologies et bases mécanistiques versionnées :** archives horodatées de **MeSH/UMLS**, **Gene Ontology**, **ChEBI**, **Reactome** et **Wikidata**. Elles fournissent des relations typées orientées (activation, inhibition, catalyse, inclusion) pour construire $E_t^{\text{rel}}$ et calculer $C(\phi)$ et $K(\phi)$ indépendamment des co-occurrences textuelles.
3. **Corpus d'équations symboliques :** équations LaTeX extraites des sources arXiv (physique, biologie quantitative, économie, réseaux), converties en arbres syntaxiques abstraits (AST) alpha-équivalents (variables anonymisées). Deux domaines partagent une structure mathématique mesurable si leurs AST présentent un sous-arbre opératoire commun non trivial.
4. **Découvertes simultanées :** listes historiques d'Ogburn & Thomas (1922) et Merton (1961) `[RAPPORTÉ]` complétées, pour l'époque contemporaine, par des paires de prépublications indépendantes soumises dans une fenêtre courte (par exemple $\le 90$ jours `[illustratif]`) sans coauteur commun ni citation croisée sur arXiv/bioRxiv, vérifiées par recouvrement de résultats ou attribution conjointe ultérieure.
5. **Analogies et mariages ayant échoué (lutte contre le biais du survivant) :** aucun catalogue standardisé à grande échelle d'analogies scientifiques échouées n'existe actuellement en format ouvert `[OBSERVÉ-NON-AUDITÉ]`. On construit donc trois ensembles observables non sélectionnés sur le succès : (i) l'ensemble exhaustif des paires de concepts nouvellement co-publiées dans $(T_0, T_0+\delta]$ qui restent sans suite (zéro reprise ultérieure ou rétraction), (ii) les hypothèses biomédicales et repositionnements pharmacologiques appariés entre PubMed et **ClinicalTrials.gov** ayant échoué en phase II/III, et (iii) un jeu curé d'analogies historiques réfutées (calorique, éther mécanique, analogies organiques en sociologie) annoté hors modèle.

---

## 4. Méthodes, outils et audit minimal des instruments

### 4.1 Algorithmes nommés par variable et par test

- **Distance de surface $d_t^{\text{surf}}$ :** entraînement de plongements lexicaux **Word2Vec (Skip-Gram)** et **TF-IDF + SVD tronquée** strictement sur le corpus $\le t$ (aucun modèle pré-entraîné post-$t$), combiné au plus court chemin pondéré (**Dijkstra**) sur $E_t^{\text{surf}}$.
- **Alignement structurel $S_t^{\text{struct}}$ :** sur petits graphes typés, **SME** (Falkenhainer, Forbus & Gentner, 1989) ; à grande échelle, filtrage par **noyaux de graphes de Weisfeiler-Lehman** (Shervashidze, Schweitzer, van Leeuwen, Mehlhorn & Borgwardt, 2011, *Weisfeiler-Lehman Graph Kernels*, *JMLR*) `[RAPPORTÉ]` puis alignement continu par **Gromov-Wasserstein** (Peyré, Cuturi & Solomon, 2016, *Gromov-Wasserstein Averaging of Kernel and Distance Matrices*, ICML) `[RAPPORTÉ]` et extension Fused Gromov-Wasserstein (`référence à vérifier`), complété d'un comptage explicite des arêtes de signes/types opposés $K(\phi)$. Sur les équations, conversion via **LaTeXML/SymPy** puis distance d'édition d'arbres par l'algorithme de **Zhang-Shasha** (Zhang & Shasha, 1989, *Simple Fast Algorithms for the Editing Distance between Trees and Related Problems*, *SIAM Journal on Computing*) `[RAPPORTÉ]`.
- **Choc méthodologique $I_t$ :** extraction d'entités méthodes/instruments sur les sections Méthodes par dictionnaires contrôlés (MeSH/EDAM) + NER supervisé, puis variation de similarité cosinus pondérée par BM25 entre $[t-2\Delta, t-\Delta]$ et $[t-\Delta, t]$.
- **Surprise et progrès de compression :** perplexité et $D_{\mathrm{KL}}$ calculées sur un modèle probabiliste de liens ou un encodeur entraîné exclusivement sur $\le t$ ; progrès de compression mesuré par la réduction de perte log-vraisemblance hors-échantillon lorsqu'une hypothèse est intégrée au modèle prédictif.
- **Percolation macroscopique :** suivi de $S_{\max}(t)$ par **Union-Find** et comparaison par critère **BIC** d'un modèle à rupture de seuil contre une croissance logistique lisse.
- **Prédiction et tests :** régression logistique $L_2$ et **LightGBM**, évalués par **AUC-PR** (aire sous la courbe précision-rappel, adaptée au fort déséquilibre) et **log-loss**, avec tests de permutation par blocs disciplinaires.

### 4.2 Livrable (c) : mesure minimale de fonctionnement de chaque instrument nommé

Chaque instrument envisagé dans la question doit franchir une validation minimale avant tout usage scientifique (tous les seuils chiffrés ci-dessous sont `[illustratif]`) :

1. **ACP / modèles non supervisés d'extraction des dimensions abstraites du langage (H9) :**
   - *Cas honnêtes appariés :* paires interdisciplinaires partageant un isomorphisme mathématique vérifié (AST d'équations) avant co-publication vs paires négatives appariées par discipline, date, fréquence lexicale et distance de surface (incluant homonymes lexicaux sans isomorphisme).
   - *Mesure minimale :* rappel à $\mathrm{FPR} \le 5\,\%$ `[illustratif]` et gain $\Delta\mathrm{AUC\text{-}PR} \ge +0{,}05$ `[illustratif]`.
   - *Vérifications mécaniques à battre :* similarité cosinus TF-IDF, score d'Adamic-Adar sur $E_t^{\text{surf}}$, et recouvrement morphologique de sous-chaînes (cognats).
2. **Critère serrure-clé par alignement de graphes (H3 / H6) :**
   - *Cas honnêtes appariés :* analogies fécondes vérifiées vs fausses analogies échouées et analogies purement superficielles, appariées sur la taille et la distribution des degrés des voisinages $H_u, H_v$.
   - *Mesure minimale :* taux de détection $\ge 60\,\%$ pour un $\mathrm{FPR} \le 15\,\%$ `[illustratif]`, avec baisse mesurable du FPR lorsque la pénalité de conflit $K(\phi)$ est activée.
   - *Vérifications mécaniques à battre :* comparaison des seuls vecteurs de degrés locaux et similarité de Jaccard sur les sacs d'étiquettes de voisins (sans topologie d'arêtes).
3. **Détecteur de « champ / air du temps » par choc instrumental $I_t$ (H5) :**
   - *Cas honnêtes appariés :* découvertes simultanées indépendantes vs découvertes uniques (*singletons*) appariées par discipline, date et popularité des concepts parents.
   - *Mesure minimale :* taux de détection sur multiples vs FPR sur *singletons* appariés ($\Delta\mathrm{AUC\text{-}PR} \ge +0{,}05$ et rapport de cotes ajusté $> 1{,}5$ `[illustratif]`).
   - *Vérifications mécaniques à battre :* modèle nul de Poisson fondé sur la seule croissance du nombre d'auteurs et d'articles dans les deux disciplines (Simonton, 1979).
4. **Détecteur de cascades A–B–C (H2) :**
   - *Cas honnêtes appariés :* liens A–C validés ultérieurement (ex. repositionnements approuvés) vs chaînes A–B–C de même fréquence de B ayant échoué en essai clinique ou reposant sur un terme B polysémique.
   - *Mesure minimale :* précision @ top-$100$ et $\mathrm{FPR} \le 20\,\%$ `[illustratif]` sur les chaînes polysémiques.
   - *Vérifications mécaniques à battre :* attachement préférentiel ($k_A k_C$) et Adamic-Adar non typé.
5. **Signal scalaire de surprise « dopaminergique » (H10) :**
   - *Cas honnêtes appariés :* flux chronologique mêlant propositions validées ultérieurement, propositions surprenantes réfutées/rétractées, et permutations aléatoires de concepts rares.
   - *Mesure minimale :* taux de détection des propositions validées dans le top $5\,\%$ du score avec $\mathrm{FPR} < 10\,\%$ `[illustratif]` sur les permutations aléatoires.
   - *Vérifications mécaniques à battre :* rareté combinatoire inverse ($-\log P(u)P(v)$), perplexité d'un modèle n-gramme simple, et progrès de compression MDL.

---

## 5. Validation hors de l'auteur et expériences décisives

### 5.1 Protocole de validation hors-auteur

- **Prédiction rétrospective strictement temporelle :** coupure figée à $T_0$ (ex. $T_0 = 2015$ `[illustratif]`). Tous les graphes, ontologies, plongements et modèles sont construits *strictement* sur $\le T_0$ (exclusion de tout LLM pré-entraîné post-$T_0$ pour éviter la fuite temporelle). Évaluation sur l'émergence de nouveaux liens dans $(T_0, T_0+3]$ et leur survie/fécondité dans $(T_0+3, T_0+8]$ `[illustratif]`, face à B0, B1 et B2.
- **Traitement du biais du survivant :** la cohorte d'évaluation inclut l'ensemble des paires non reliées à $T_0$ qui sont nouvellement tentées dans $(T_0, T_0+3]$ — succès, impasses non citées, échecs cliniques et rétractations — plutôt qu'une liste rétrospective de découvertes célèbres.
- **Test sur les découvertes simultanées :** comparaison systématique entre *multiples* indépendants et *singletons* appariés sur la fenêtre future.
- **Évaluation humaine en double aveugle :** échantillon stratifié ($N = 300$ propositions `[illustratif]`) anonymisé et normalisé stylistiquement, mêlant prédictions du modèle, prédictions de B1, mariages historiques réels et faux positifs appariés. Des experts indépendants notent séparément : (1) surprise (Q1), (2) cohérence mécanistique, (3) priorité de test expérimental, avec contrôle de l'accord inter-juges ($\alpha$ de Krippendorff $\ge 0{,}60$ `[illustratif]`).
- **Préenregistrement :** dépôt public horodaté (type OSF) avant ouverture des données post-$T_0$, figeant hyperparamètres (calibrés sur $T_{-1} < T_0$), métriques primaires, contrôles négatifs et seuils de réfutation.

### 5.2 Livrable (b) : trois expériences décisives en inférence forte ($H_A$ contre $H_B$)

Tous les seuils numériques ci-dessous sont `[illustratif]` et préenregistrés avant test.

- **Expérience E1 — Alignement structurel (H1/H3) contre topologie de surface (B1) :**
  - **$H_A$ :** L'alignement relationnel $S_t^{\text{struct}}$ (sur $E_t^{\text{rel}}$ et AST d'équations $\le T_0$) améliore la prédiction des mariages interdisciplinaires féconds au-delà de B1 (popularité, $d_t^{\text{surf}}$, Adamic-Adar).
  - **$H_B$ :** À popularité et voisinage indirect contrôlés, $S_t^{\text{struct}}$ n'apporte aucun gain prédictif ; l'effet apparent de proximité cachée se réduit à B1.
  - *Métrique et seuil :* $\Delta\mathrm{AUC\text{-}PR} \ge +0{,}05$ ($p < 0{,}01$, permutation par blocs disciplinaires) et $\beta_3 > 0$ (IC $95\,\%$ excluant $0$) `[illustratif]` sur le quartile supérieur de $d_t^{\text{surf}}$.
  - *Contrôle négatif :* permutation aléatoire des types/signes d'arêtes de $E_t^{\text{rel}}$ à distribution de degrés fixée.
  - *Issues falsifiantes :* seuil franchi **et** disparition du gain sur le contrôle négatif $\Rightarrow$ **$H_B$ falsifiée**. Gain $< +0{,}02$ `[illustratif]` **ou** maintien du gain sur le graphe permuté $\Rightarrow$ **$H_A$ falsifiée**.

- **Expérience E2 — Convergence instrumentale (H5 épurée) contre Poisson/volume (Simonton) :**
  - **$H_A$ :** Le choc méthodologique $I_t(u,v)$ prédit les découvertes simultanées indépendantes mieux que le volume d'activité des communautés.
  - **$H_B$ :** La fréquence des découvertes simultanées s'explique entièrement par un processus de Poisson dépendant du nombre d'auteurs actifs, du taux de publication et des prérequis directs.
  - *Métrique et seuil :* $\Delta\mathrm{BIC} \le -10$ et $\Delta\mathrm{AUC\text{-}PR} \ge +0{,}05$ `[illustratif]` sur *multiples* vs *singletons* appariés.
  - *Contrôle négatif :* permutation temporelle des dates d'adoption instrumentale (placebo chronologique).
  - *Issues falsifiantes :* seuil franchi et effet nul sur le placebo $\Rightarrow$ **$H_B$ falsifiée**. Échec du seuil ou signal présent sur le placebo $\Rightarrow$ **$H_A$ falsifiée**.

- **Expérience E3 — Progrès de compression contre surprise brute (H10, Q1 vs Q2) :**
  - **$H_A$ :** Le progrès de compression prédictive discrimine les idées fécondes (Q2) des fausses pistes surprenantes là où la surprise brute confond fécondité et bruit.
  - **$H_B$ :** La surprise brute (perplexité/$D_{\mathrm{KL}}$ datée $\le T_0$, bornée à la fenêtre H4) atteint une précision équivalente ou supérieure au progrès de compression.
  - *Métrique et seuil :* $\Delta\text{Précision@5\%} \ge +0{,}10$ et $\Delta\mathrm{FPR} \le -0{,}10$ (test de McNemar apparié, $p < 0{,}01$) `[illustratif]` sur hypothèses biomédicales validées vs échouées/rétractées.
  - *Contrôle négatif :* injection de $20\,\%$ `[illustratif]` de paires aléatoires synthétiques (test du piège du bruit).
  - *Issues falsifiantes :* avantage net du progrès de compression et rejet du bruit $\Rightarrow$ **$H_B$ falsifiée** (réfutation de H10 naïve). Égalité ou avantage de la surprise brute avec rejet du bruit $\Rightarrow$ **$H_A$ falsifiée**.

### 5.3 Résultat qui réfuterait globalement le modèle

Le modèle formel minimal est **réfuté** si, sur la fenêtre future préenregistrée, il ne bat pas la baseline mécanique B1 d'au moins $\Delta\mathrm{AUC\text{-}PR} \ge +0{,}05$ `[illustratif]` sur la prédiction de mariages féconds **et** échoue au contrôle négatif de permutation des types relationnels, ou s'il obtient une note humaine inférieure ou égale à B1 sur la cohérence mécanistique.

---

## 6. Ce que les hypothèses oublient

Les dix hypothèses traitent la découverte comme une géométrie interne au discours scientifique et omettent cinq déterminants essentiels :
1. **Les anomalies empiriques et le coût de falsification :** nombre de percées naissent d'un désaccord persistant entre théorie et mesure (Kuhn, 1962, *The Structure of Scientific Revolutions*, University of Chicago Press) `[RAPPORTÉ]`, non d'un mariage conceptuel. Sans modéliser l'anomalie empirique ni le coût matériel d'un test, on ne distingue pas combinatoire verbale et science testable.
2. **Causalité et équifinalité mathématique :** deux systèmes très différents peuvent obéir à la même équation (ex. lois de puissance ou diffusion) pour des raisons mécanistiques incompatibles. L'alignement formel est un filtre heuristique, jamais une preuve de mécanisme commun.
3. **Organisation sociale, taille des équipes et incitations :** Wu, Wang & Evans (2019, *Large teams develop and small teams disrupt science and technology*, *Nature*) `[RAPPORTÉ]`, Foster et al. (2015) `[RAPPORTÉ]` et Wang et al. (2017) `[RAPPORTÉ]` montrent que la taille des équipes, le financement, l'aversion au risque des carrières et le conservatisme de l'évaluation pèsent lourdement sur ce qui est exploré et publié.
4. **La mort et la réfutation des concepts :** un modèle réaliste doit représenter le taux d'abandon, la rétraction et l'élimination de fausses catégories, sans quoi il ne mesure que l'accumulation de combinaisons.
5. **L'invention de concepts nouveaux (*problem finding*) :** certaines avancées créent une observable ou une variable sans équivalent dans les concepts parents, ce qu'aucun modèle purement combinatoire sur un vocabulaire $V_t$ figé ne peut engendrer.

---

## 7. Une première expérience peu coûteuse et son ancrage matériel

### 7.1 Cible, protocole en duel ($H_A$ vs $H_B$) et lecture

**Hypothèse ciblée :** **H9 couplée à H1/H3**, car elle est à la fois le point le plus fragile et le verrou pratique du projet. Si des méthodes non supervisées sur le langage (H9) ne retrouvent même pas des isomorphismes mathématiques objectifs déjà présents dans les équations, il devient inutile de bâtir un détecteur d'idées sur le seul texte ; il faudra investir directement dans des graphes formels ($E_t^{\text{rel}}$).

**Protocole (4 à 6 jours `[illustratif]`) :**
- **Terrain :** sous-ensemble ouvert d'arXiv (physique statistique `cond-mat.stat-mech`, biologie quantitative `q-bio`, finance quantitative `q-fin`, réseaux `cs.SI`) coupé strictement à $T_0 = 2016$ `[illustratif]`, période future $(2016, 2022]$ `[illustratif]`.
- **Étalon-or structural indépendant du texte :** parsing des équations LaTeX en AST canonisés (variables anonymisées). On sélectionne $N = 500$ `[illustratif]` paires interdisciplinaires sans co-occurrence directe $\le 2016$ mais partageant un sous-arbre opératoire non trivial (ex. opérateur de Fokker-Planck ou dynamique de Potts), appariées 1:5 ($2\,500$ négatifs `[illustratif]`) par discipline, date et fréquence lexicale.
- **Contrôles négatifs :** (i) paires homonymes (même terme de surface, AST incompatibles) ; (ii) AST à opérateurs permutés aléatoirement.
- **Duel $H_A$ contre $H_B$ :**
  - **$H_A$ (viabilité de H9) :** des représentations textuelles non supervisées entraînées *uniquement* sur arXiv $\le 2016$ (SVD/ACP sur TF-IDF, Word2Vec temporel, et un petit encodeur Transformer entraîné de zéro sur $\le 2016$) détectent ces isomorphismes sans recouvrement lexical **et** prédisent les futurs mariages $(2016, 2022]$ mieux que B1 (TF-IDF + Adamic-Adar lexical).
  - **$H_B$ (échec du texte seul) :** les représentations non supervisées $\le 2016$ ne surpassent pas B1 dès que le vocabulaire est disjoint et tombent dans le piège des homonymes, tandis que l'alignement direct sur AST ($S_t^{\text{struct}}$) y parvient.
- **Seuils et lecture `[illustratif]` :**
  - Seuil pour valider $H_A$ : $\Delta\mathrm{AUC\text{-}PR} \ge +0{,}08$ au-dessus de B1 sur la détection d'isomorphismes sans cognats lexicaux **et** $\mathrm{FPR} \le 15\,\%$ sur les homonymes.
  - Si $H_A$ franchit le seuil $\Rightarrow$ **$H_B$ est falsifiée** (H9 survit à son premier crash-test).
  - Si $\Delta\mathrm{AUC\text{-}PR} < +0{,}03$ ou $\mathrm{FPR} > 30\,\%$ sur les homonymes alors que l'alignement AST dépasse $+0{,}15$ $\Rightarrow$ **$H_A$ (et H9) est falsifiée** : réorientation vers les graphes formels/symboliques.
  - Si l'alignement AST échoue lui aussi à prédire les mariages $(2016, 2022]$ mieux que B1 $\Rightarrow$ la composante prédictive de H1/H3 est fragilisée dès la première semaine.

### 7.2 Livrable (d) : ancrage matériel

- **Modèles et logiciels ouverts :**
  - *Anti-fuite temporelle (modèles entraînés strictement sur $\le 2016$) :* **scikit-learn** (TF-IDF, SVD/ACP, régression $L_2$), **Gensim** (Word2Vec/FastText), **LightGBM**, et un encodeur ouvert architecture **RoBERTa-base** (~$125\,\text{M}$ paramètres `[illustratif]`) pré-entraîné *de zéro* sous **PyTorch / Hugging Face Transformers** sur le corpus arXiv $\le 2016$.
  - *Extraction syntaxique locale (et non jugement de surprise) :* **Qwen2.5-7B-Instruct** ou **Llama-3.1-8B-Instruct** en inférence locale 4-bit (**vLLM**) pour l'extraction structurée d'entités méthodologiques, auditée manuellement sur $200$ phrases `[illustratif]`.
  - *Équations et graphes :* **LaTeXML**, **SymPy**, **NetworkX / igraph**, **POT (Python Optimal Transport)**.
- **Calcul nécessaire `[illustratif]` :**
  - Parsing AST, graphes et baselines sur ~$200\,000$ articles arXiv $\le 2016$ (~$50$ à $150$ Go de sources) : 1 serveur CPU $16$–$32$ cœurs, $64$ Go RAM, $12$ à $24$ heures.
  - Pré-entraînement *de zéro* de l'encodeur ~$125\,\text{M}$ paramètres (~$2$ milliards de tokens) + alignements Gromov-Wasserstein : 1 GPU **NVIDIA A100 80 Go** (ou **L40S / RTX 4090**) pendant $24$ à $48$ heures.
- **Coût estimé `[illustratif]` :**
  - Location cloud GPU (1× A100 80 Go pendant $48$ h à ~$1{,}5$–$2{,}5\,\$/\text{h}$) : **$75$ à $120\,\$$**.
  - Instance CPU, stockage temporaire ($500$ Go SSD sur $7$ jours) et transfert des archives arXiv : **$30$ à $80\,\$$**.
  - **Total matériel/calcul : ~$100$ à $200\,\$$** `[illustratif]` (hors temps humain ; coût marginal nul sur cluster académique).

FIN-DE-CELLULE