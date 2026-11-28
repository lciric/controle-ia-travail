# Réponse : un modèle testable de l'idée intéressante et de sa naissance (effort maximal, v1)

Classe C, 2026-11-23, session fille, GO-2026-11-23-21. Lus, empreintes vérifiées : demande reformulée (`230585b9…`), intuitions du directeur (`9d408b22…`), `CLAUDE.md`, `docs/notes/papier-dopamine-moniteur-v1/` ; aucune autre réponse ; « conscience et émergence » absent. Références vérifiées le 23 novembre (Crossref, arXiv, OpenAlex) ; chiffres lus sur PDF (fin de note) ; sinon « à vérifier ».

## Verdict

Le cœur (H1, H3) est déjà la théorie de l'appariement de structure : la solidité d'une analogie suit la structure relationnelle partagée, son rappel suit la surface [15, p. 524]. Reste ouverte, et testable sans dépense, l'interaction : la distance de surface ne paie que si la structure suit. Les seules notes d'intérêt publiques à grande échelle contredisent « loin, donc intéressant » [16]. Ferromagnétisme, résonance, Noether, transition de phase : sans contenu testable ; « champ » et « puits » en ont un.

## 1. Confrontation à la littérature

Trois questions se mêlent. **Intéresser un public** : une théorie intéresse quand elle nie une croyance de son public [8, p. 309] ; l'intérêt veut nouveauté et compréhensibilité perçues ensemble [30] ; formellement, surprise bayésienne : écart entre croyances avant et après [20]. **Être vraie et féconde** : seule l'épreuve tranche ; les idées jugées neuves avant exécution perdent davantage après [29]. **Produire** : occupé (découverte par la littérature [34], prédiction de liens [22, 33], fouille d'analogies [18], modèle de l'intéressant [41]).

| Hypothèse | Jugement | Appuis et contre-appuis |
|---|---|---|
| H1 mariage éloigné | Soutenue (solidité, réception) ; contredite comme recette ; occupée | Solidité ↔ structure, rappel ↔ surface [15, p. 524] ; analogies formelles et matérielles ; positives, négatives, neutres [17] ; combinaisons inattendues → impact, venues d'étrangers au domaine [28] ; fond conventionnel et dose d'atypique [37]. Contre : 2 analogies lointaines sur 99 au laboratoire, surtout pour expliquer [9, p. 7–8 du manuscrit] ; sources proches plus utiles [7] ; « trop loin » nuit [12] ; sur 4 451 notes de 110 directeurs de groupe [16, p. 6], l'intérêt baisse avec la distance sémantique entre les deux chercheurs (rang −0,223) et le degré du concept (−0,166) [16, p. 8] |
| H2 cascades | Soutenue ; occupée depuis 1986 | A–B et B–C dans des littératures disjointes, donc A–C [34] ; inférences du plus systématique vers le moins systématique [4] |
| H3 serrure et clé | Soutenue ; Noether écarté | Appariement un à un, connexité parallèle, systématicité [14, 10] |
| H4 ni près ni loin | Soutenue ; optimum non situé | Combinaisons neuves moins utiles en moyenne, plus variables [11] ; nouveauté risquée, reconnue tard [39] ; « trop loin » [12] |
| H5 champ | Fait soutenu ; explication disputée | Multiples fréquentes [24] ; hasard poissonnien contre air du temps [31, sources secondaires] ; queue longue contre Poisson [23] ; horloges et relativité, thèse discutée [13] ; sons d'un écoulement transsonique et horizon de trou noir [36] |
| H6 distinction | Soutenue, occupée | « Composition » dans les deux sens [8, p. 315] |
| H7 profondeur | En partie ; « près des nœuds » contredite | Unification [21] ; progrès de compression [26] ; concepts centraux, idées moins intéressantes [16, p. 8] |
| H8 émergence | Échange soutenu ; transition de phase non | Courtiers entre groupes [6] ; étrangers [28] ; marche renforcée sur un réseau de concepts [19] |
| H9 langage | En partie ; métaphysique hors du testable | Plongements qui anticipent des découvertes [35] ; contre : alignement non supervisé fragile entre langues ou domaines éloignés [32] ; premières composantes principales = fréquence des mots [25, p. 4] : l'analyse en composantes principales trouvera la surface |
| H10 surprise | Inconnue ; deux signaux | Dopamine : erreur de prédiction de la récompense [27] ; modèle de langage : neurones de valeur et d'erreur de différence temporelle par étape [40, p. 1] |

**L'exemple.** L'anesthésie générale réunit perte de conscience, amnésie, analgésie et immobilité [5] ; certains anesthésiques abolissent la réponse sans abolir forcément la conscience, liée à l'intégration de l'information [1]. Un « axe de douleur » muet lirait une analgésie, pas une anesthésie : la chaîne douleur → anesthésie → conscience confond deux composantes (H6). L'invariant à transporter est l'intégration. De même, le principe d'équivalence fusionne masses inerte et grave ; c'est la simultanéité que la relativité sépare.

## 2. Modèle formel minimal

**Objets.** Concepts V ; trois couches datées : usage U_t (cooccurrences) ; relations R_t, arêtes typées orientées (a, r, b) (cause, se mesure par, obéit à l'équation e) ; personnes P_t (auteurs × concepts). Amont N_k(a) : sous-graphe de R_t à k relations de a.

**Deux distances.** Surface d_S(a,b,t) = −log p̂_t(a,b), probabilité de combinaison sous un modèle appris sur U_t et P_t seuls (blocs stochastiques corrigés du degré, ou hypergraphe [28]) : la surprise relative aux habitudes ; un public g a sa version d_S^g. Structure d_R(a,b) : valeur de Gromov–Wasserstein fusionnée entre N_k(a) et N_k(b), a forcé sur b [38], qui compare des relations sans étiquette commune.

**Serrure et clé.** Le couplage optimal donne une application injective partielle φ de N_k(a) vers N_k(b). Sur les arêtes E_a : couverture κ, part des (i, r, j) dont l'image (φ(i), r, φ(j)) est dans E_b (analogie positive [17]) ; conflit χ, part dont l'image porte une relation incompatible (négative) ; inférences I, arêtes transportées sans image connue (neutre) : les graines ; systématicité σ, part des arêtes appariées dans la plus grande composante connexe appariée [14]. Score orienté K(a→b) = σκ − λχ, la base étant le côté le plus systématique [4]. H3 : K à k = 2 prédit mieux que toute ressemblance de nœuds (k = 0). H6 sort du même calcul : une identité apparente à χ élevé est fausse. La « projection » de H5 devient un coût de déformation de l'amont avant appariement : une serrure souple.

**Champ et contact.** h_ab(t) = Σ_m u_m(N(a),t)·u_m(N(b),t) : m parcourt méthodes, instruments et formalismes apparus depuis moins de τ ans ; u_m est la part des articles récents de l'amont qui emploient m. Contact A_ab(t) : auteurs ayant publié dans les deux amonts [33].

**Naissance.** Premier lien typé au temps τ_ab ; risque à temps discret :
logit P(τ_ab=t | τ_ab≥t) = α_t + β_S·d_S + β_K·K + β_SK·d_S·K + β_h·h + β_A·log(1+A) + γ·x,
x = bases (degrés, voisins communs, Adamic–Adar). Prédictions : β_S<0 (le rappel suit la surface [15]) ; β_SK>0 (plus la surface éloigne, plus la structure décide) ; β_h>0 ; β_A>0.

**Intérêt pour g.** I_g = d_S^g · c(K), c croissante et bornée (compréhensibilité [30]) ; la forme additive est la contre-hypothèse.

**H4 tirée de H1.** Soit c̄(x) = E[c(K) | d_S = x], estimée sur le graphe seul. L'intérêt moyen x·c̄(x) culmine en x* où l'élasticité x·c̄′/c̄ vaut −1 ; si c̄ décroît en exp(−x/ℓ), x* = ℓ. L'optimum est situé sans voir une note (dérivation élémentaire ; antériorité probable, non cherchée). Cela explique la pente négative de [16] si leurs paires sont surtout au-delà de x*, et prédit son inversion à K élevé.

**Profondeur (H7).** Gain de description ΔL = L(R) − L(R | φ), la structure appariée codée une fois, non deux (unification [21], compression [26]) ; fécondité F, part des inférences I confirmées en Δ ans. « Expliquer après coup sa surprise » : d_S élevé avant, ΔL élevé après.

| Analogie | Équivalent exact, grandeur | Sort |
|---|---|---|
| Puits | Communauté de conductance Φ (probabilité d'en sortir en un pas depuis sa loi stationnaire) ; profondeur 1/Φ, largeur = taille ; « distance inverse de la largeur » mêle paire et ensemble : retirée | Gardé s'il bat le degré |
| Champ | Covariable h_ab(t) | Gardé |
| Polarisation | Sous un champ, les moments d'un ferromagnétique s'alignent dans le même sens ; reste cause commune (h) et complémentarité (K orienté) | Écartée |
| Résonance | Corrélation croisée des croissances d'attention | Écartée |
| Noether, lagrangien | Ni action ni groupe continu sur un graphe de concepts ; équivalent : application qui préserve les relations (κ, χ) | Écarté |
| Percolation entre deux milieux | Chaînes typées cohérentes de longueur ≤ L entre deux blocs ; seuil contre linéaire | Forme à tester |
| Transition de phase | Seuil dont la netteté croît avec la taille ; invisible sur un corpus fini | Écartée |
| Emboîtement au hasard | Groupes indépendants faisant le même premier lien : Poisson(Λ_ab), Λ_ab = ∫ λ_ab(t)·A_ab(t) dt ; si λ varie avec h, sur-dispersion (queue longue [23]), qui doit baisser à h connu | Hypothèse nulle |

## 3. Données brutes

- Textes datés : sources LaTeX d'arXiv, PubMed Central ouvert ; métadonnées, citations, auteurs, résumés : OpenAlex ; dates des concepts : MeSH, PhySH, classification mathématique.
- Relations typées : SemMedDB, tirée de PubMed (licence UMLS : compte, donc nœud de décision) ; ailleurs, extraction par modèle ouvert validée sur un échantillon annoté.
- Graphe prêt : celui de [16], concepts de 2,44 millions d'articles, arêtes sur 58 millions [16, p. 1 et 3] ; Zenodo 10.5281/zenodo.13900962, CC BY 4.0, 3,0 Go (notice web).
- Équations : arbres de formules canonisés depuis LaTeX (analogies formelles [17]) ; témoins connus [36].
- Multiples : listes classiques réanalysées par [31] ; jumeaux publics [2] ; déplacement commun [23].
- Échecs : rétractations (Retraction Watch) ; hypothèses jamais confirmées ; registre des tentatives de l'organisme d'idéation ; notes basses de [16].
- Jugements : notes de [16], données d'évaluation déclarées publiques [16, p. 12] ; revues avant et après exécution [29].

Chaque variable vient d'une couche : d_S de U et P ; K et ΔL de R ; h des adoptions de méthodes ; A de P ; τ des dates ; F des confirmations.

## 4. Méthodes et outils

| Variable ou test | Algorithme | Outil |
|---|---|---|
| Concepts | Groupes nominaux filtrés, liés à Wikidata | scispaCy, chaîne de [16] |
| Relations | SemRep ; sinon schéma fermé | Qwen2.5-7B ou Llama-3.1-8B en local |
| d_S | Blocs stochastiques corrigés du degré ; plongements diachroniques alignés (Procuste) | graph-tool, gensim |
| K, κ, χ, σ | Gromov–Wasserstein fusionnée [38] ; appariement de structure sur petits amonts [10] ; struc2vec en base de rôle | POT, SME |
| Puits | Conductance, stabilité de Markov | graph-tool |
| Naissance | Risque logistique à temps discret ; témoins tirés du groupe à risque, poids connus | statsmodels |
| Intérêt | Régression ordinale, effet aléatoire par évaluateur ; validation croisée groupée ; aire sous la courbe, précision des N premiers | statsmodels, scikit-learn |
| Multiples ; seuil (H8) | Poisson contre binomiale négative ; régression segmentée | statsmodels, ruptures |
| H10 | Sondes de [40] ; surprise = −log p de l'énoncé, sommée ; lecture au dernier jeton, jamais de moyenne sur les jetons | transformers |

## 5. Validation hors de l'auteur du modèle

- **Futur tenu à l'écart.** Construire jusqu'à T0, régler sur (T0, T1], lire l'épreuve une seule fois sur (T1, T2] [22] ; code et seuils scellés avant (R1), contre-lus (R2), verdict par un agent neuf (R13).
- **Bases.** Attachement préférentiel, voisins communs, Adamic–Adar, surface seule, variables de réseau choisies à la main (meilleures que l'apprentissage de bout en bout [22]), classement sans exemple par un modèle de langage (aire sous la courbe de 67,44 % pour les idées très intéressantes [16, p. 9]).
- **Survivant.** Groupe à risque : toutes les paires non liées en T0 (ou un tirage aux probabilités connues) ; échecs et rétractations comme négatifs ; naissance, intérêt et fécondité rapportés à part.
- **Multiples.** À d_S et K égaux, les jumeaux [2] ont un h plus fort.
- **Aveugle.** Des experts de plusieurs communautés classent des fiches sans source : vraies découvertes de la période tenue à l'écart, anonymisées (témoins positifs) ; leurres à même d_S et χ élevé (témoins négatifs) ; idées du modèle et d'une base. Les évaluateurs pénalisent le neuf et le proche [3] : on modélise l'évaluateur.
- **Tiers.** Réplication par une autre équipe, autre extraction de concepts.
- **Réfutation du cœur.** (i) Sur l'épreuve, chez les paires éloignées, l'apport de K (k = 2) aux bases a un intervalle à 95 % entièrement sous le minimum scellé ; (ii) l'interaction d_S × K sur l'intérêt est nulle ou négative ; (iii) l'optimum observé tombe loin de x*.

## 6. Ce que les hypothèses oublient

1. **Le public** : l'intérêt est relatif (dans [16], p. 8, la proximité au domaine de l'évaluateur brouille la distance) ; il faut des croyances par communauté (d_S^g).
2. **Le coût de l'épreuve** : sans expérience faisable, pas de naissance ; idée jugée et idée exécutée divergent [29].
3. **La sélection sociale** : l'impact mesure aussi l'attention [3, 39].
4. **Le sens du transfert** : du mûr vers le jeune [4], testable sur le sens des citations.
5. **La recherche** : un score ne produit rien ; il faut une dynamique d'exploration [19] ; le tri est le goulot.
6. **La question** : l'importance du problème multiplie l'intérêt.
7. **La dérive des concepts** : versionner leur identité.
8. **Les liens défaits** : compter les fausses identités défaites.

## 7. Première expérience peu coûteuse : l'essai « surface et structure »

**Bras A (processeur, trois jours ; sans dépense si la machine du dépôt suffit, sinon devis).** Réanalyse des 2 996 idées notées bâties sur des paires de concepts [16, p. 8] et de leur graphe (contenu des données à vérifier). Un script aveugle aux notes calcule d_S (blocs stochastiques ; plongements des noms en contrôle), K0 (ressemblance de rôle des deux concepts, struc2vec) et K2 (Gromov–Wasserstein fusionnée des amonts à deux pas) ; contrôles : degré, rang de page, citations, proximité au profil de l'évaluateur, condition de génération (les paires tirées au hasard [16, p. 7] donnent une variation de d_S que nul n'a choisie).
- Prédictions : interaction d_S × K2 positive, la pente négative de l'intérêt en d_S s'inversant dans le tiers supérieur de K2 (H1) ; K2 bat K0 (H3) ; optimum près de x*, calculé sans les notes.
- Lecture (seuils proposés, à fixer dans un préenregistrement selon la règle « Qui conçoit ») : H1 soutenue si l'intervalle à 95 % de l'interaction est au-dessus de 0 et si l'apport de K2 à l'aire sous la courbe, dans le tiers éloigné, atteint 0,02 ; réfutée sur ce terrain si l'intervalle de l'apport est entièrement sous 0,01 et l'interaction non positive ; sinon non concluant. H3 de même, K2 contre K0. Environ un quart des notes sont hautes [16, p. 1] ; puissance simulée avant scellement.
- Limites : sans relations typées, A n'éprouve que la forme « position dans le graphe » de H3 ; chaque idée a été rédigée par un modèle qui jugeait lui-même la fusion [16, p. 4], ce qui peut écraser l'effet de K.

**Bras B (sur devis, une à deux journées de carte graphique).** Relations typées des concepts notés, extraites par un modèle ouvert d'une vingtaine de résumés chacun ; κ, χ, σ ; mêmes tests : la vraie épreuve de la serrure.

**Bras C (sans dépense).** Coupure temporelle sur le même graphe : paires non liées en T0, premier lien dans les trois ans ; β_SK>0 et apport de K2 chez les paires éloignées, au-dessus des bases.

**Complément H10 (sur devis).** Un modèle ouvert étudié par [40] lit chaque idée : surprise de l'énoncé du lien ; neurones de valeur et neurones « dopamine » lus avant et après lui (erreur de différence temporelle d'un pas). Ces neurones prédisent la confiance et guident la recherche comme modèle de récompense de processus [40, p. 1] : ils lisent la viabilité, non la nouveauté. Prédiction : la surprise suit d_S, l'erreur suit K, et seule leur succession (« surprendre puis expliquer ») prédit l'intérêt au-delà des deux. À lire, jamais à optimiser.

**Lecture d'ensemble.** A et C réfutés : le cœur, sous forme de graphe, tombe ; reste l'énoncé psychologique [15]. A et C soutenus : B, puis une épreuve prospective en aveugle. La vérité ne s'éprouve pas à ce prix.

**Antériorité (R8).** Occupé : voir le tableau de la partie 1. Non trouvés en quelques requêtes, ce qui n'est pas « nouveau » : l'interaction surface × compatibilité relationnelle sur des notes d'intérêt ; le champ expliquant la sur-dispersion des multiples.

## Références

1. Alkire M. T. et al. (2008). Consciousness and anesthesia. Science 322(5903):876–880. https://doi.org/10.1126/science.1149213
2. Bikard M. (2020). Idea twins: Simultaneous discoveries as a research tool. Strategic Management Journal 41(8):1528–1543. https://doi.org/10.1002/smj.3162
3. Boudreau K. J. et al. (2016). Looking across and looking beyond the knowledge frontier: Intellectual distance, novelty, and resource allocation in science. Management Science 62(10):2765–2783. https://doi.org/10.1287/mnsc.2015.2285
4. Bowdle B. F., Gentner D. (1997). Informativity and asymmetry in comparisons. Cognitive Psychology 34(3):244–286. https://doi.org/10.1006/cogp.1997.0670
5. Brown E. N. et al. (2010). General anesthesia, sleep, and coma. New England Journal of Medicine 363(27):2638–2650. https://doi.org/10.1056/NEJMra0808281
6. Burt R. S. (2004). Structural holes and good ideas. American Journal of Sociology 110(2):349–399. https://doi.org/10.1086/421787
7. Chan J. et al. (2015). Do the best design ideas (really) come from conceptually distant sources of inspiration? Design Studies 36:31–58. https://doi.org/10.1016/j.destud.2014.08.001
8. Davis M. S. (1971). That's interesting! Towards a phenomenology of sociology and a sociology of phenomenology. Philosophy of the Social Sciences 1(2):309–344. https://doi.org/10.1177/004839317100100211
9. Dunbar K. (1997). How scientists think: On-line creativity and conceptual change in science. In Ward T. B. et al. (dir.), Creative Thought, APA, 461–493. https://doi.org/10.1037/10227-017
10. Falkenhainer B. et al. (1989). The structure-mapping engine: Algorithm and examples. Artificial Intelligence 41(1):1–63. https://doi.org/10.1016/0004-3702(89)90077-5
11. Fleming L. (2001). Recombinant uncertainty in technological search. Management Science 47(1):117–132. https://doi.org/10.1287/mnsc.47.1.117.10671
12. Fu K. et al. (2013). The meaning of "near" and "far": The impact of structuring design databases and the effect of distance of analogy on design output. Journal of Mechanical Design 135(2):021007. https://doi.org/10.1115/1.4023158
13. Galison P. (2003). Einstein's Clocks, Poincaré's Maps: Empires of Time. W. W. Norton.
14. Gentner D. (1983). Structure-mapping: A theoretical framework for analogy. Cognitive Science 7(2):155–170. https://doi.org/10.1207/s15516709cog0702_3
15. Gentner D. et al. (1993). The roles of similarity in transfer: Separating retrievability from inferential soundness. Cognitive Psychology 25(4):524–575. https://doi.org/10.1006/cogp.1993.1013
16. Gu X., Krenn M. (2026). Generating interesting scientific ideas using knowledge graphs and LLMs: Evaluations with 100 research group leaders. PNAS 123(46):e2611349123 (d'après arXiv) ; lu sur arXiv:2405.17044v4. https://arxiv.org/abs/2405.17044
17. Hesse M. B. (1966). Models and Analogies in Science. University of Notre Dame Press (non lu : sources secondaires).
18. Hope T. et al. (2017). Accelerating innovation through analogy mining. KDD 2017:235–243. https://doi.org/10.1145/3097983.3098038
19. Iacopini I. et al. (2018). Network dynamics of innovation processes. Physical Review Letters 120(4):048301. https://doi.org/10.1103/PhysRevLett.120.048301
20. Itti L., Baldi P. (2009). Bayesian surprise attracts human attention. Vision Research 49(10):1295–1306. https://doi.org/10.1016/j.visres.2008.09.007
21. Kitcher P. (1981). Explanatory unification. Philosophy of Science 48(4):507–531. https://doi.org/10.1086/289019
22. Krenn M. et al. (2023). Forecasting the future of artificial intelligence with machine learning-based link prediction in an exponentially growing knowledge network. Nature Machine Intelligence 5(11):1326–1335. https://doi.org/10.1038/s42256-023-00735-0
23. Li L. et al. (2025). Is science inevitable? arXiv:2502.06190. https://arxiv.org/abs/2502.06190
24. Merton R. K. (1961). Singletons and multiples in scientific discovery: A chapter in the sociology of science. Proceedings of the American Philosophical Society 105(5):470–486 (première page à vérifier).
25. Mu J. et al. (2018). All-but-the-top: Simple and effective postprocessing for word representations. arXiv:1702.01417v2. https://arxiv.org/abs/1702.01417
26. Schmidhuber J. (2010). Formal theory of creativity, fun, and intrinsic motivation (1990–2010). IEEE Transactions on Autonomous Mental Development 2(3):230–247. https://doi.org/10.1109/TAMD.2010.2056368
27. Schultz W. et al. (1997). A neural substrate of prediction and reward. Science 275(5306):1593–1599. https://doi.org/10.1126/science.275.5306.1593
28. Shi F., Evans J. (2023). Surprising combinations of research contents and contexts are related to impact and emerge with scientific outsiders from distant disciplines. Nature Communications 14:1641. https://doi.org/10.1038/s41467-023-36741-4
29. Si C. et al. (2025). The ideation-execution gap: Execution outcomes of LLM-generated versus human research ideas. arXiv:2506.20803. https://arxiv.org/abs/2506.20803
30. Silvia P. J. (2005). What is interesting? Exploring the appraisal structure of interest. Emotion 5(1):89–102. https://doi.org/10.1037/1528-3542.5.1.89
31. Simonton D. K. (1979). Multiple discovery and invention: Zeitgeist, genius, or chance? Journal of Personality and Social Psychology 37(9):1603–1616. https://doi.org/10.1037/0022-3514.37.9.1603
32. Søgaard A. et al. (2018). On the limitations of unsupervised bilingual dictionary induction. ACL 2018:778–788. https://doi.org/10.18653/v1/P18-1072
33. Sourati J., Evans J. (2023). Accelerating science with human-aware artificial intelligence. Nature Human Behaviour 7(10):1682–1696. https://doi.org/10.1038/s41562-023-01648-z
34. Swanson D. R. (1986). Fish oil, Raynaud's syndrome, and undiscovered public knowledge. Perspectives in Biology and Medicine 30(1):7–18. https://doi.org/10.1353/pbm.1986.0087
35. Tshitoyan V. et al. (2019). Unsupervised word embeddings capture latent knowledge from materials science literature. Nature 571:95–98. https://doi.org/10.1038/s41586-019-1335-8
36. Unruh W. G. (1981). Experimental black-hole evaporation? Physical Review Letters 46(21):1351–1353. https://doi.org/10.1103/PhysRevLett.46.1351
37. Uzzi B. et al. (2013). Atypical combinations and scientific impact. Science 342(6157):468–472. https://doi.org/10.1126/science.1240474
38. Vayer T. et al. (2020). Fused Gromov-Wasserstein distance for structured objects. Algorithms 13(9):212. https://doi.org/10.3390/a13090212
39. Wang J. et al. (2017). Bias against novelty in science: A cautionary tale for users of bibliometric indicators. Research Policy 46(8):1416–1436. https://doi.org/10.1016/j.respol.2017.06.006
40. Xu G. et al. (2026). Sparse reward subsystem in large language models. arXiv:2602.00986 (v2 lue). https://arxiv.org/abs/2602.00986
41. Zhang J. et al. (2024). OMNI: Open-endedness via models of human notions of interestingness. ICLR 2024 ; arXiv:2306.01711. https://arxiv.org/abs/2306.01711

PDF lus (`docs/sources/pdf/`) : `2405.17044v4.pdf` (`fcb49a05…`) ; `gentner-rattermann-forbus-1993-roles-of-similarity-in-transfer-v1.pdf` (`ccb7655f…`) ; `dunbar-1997-how-scientists-think-manuscrit-auteur-v1.pdf` (`3f9af86e…`, pages du manuscrit) ; `davis-1971-thats-interesting-v1.pdf` (`d140f50c…`, pages de la revue) ; `1702.01417v2.pdf` (`2c2443b9…`) ; `2602.00986v2.pdf` (`da004f53…`). Le reste : résumés et notices (R7).
