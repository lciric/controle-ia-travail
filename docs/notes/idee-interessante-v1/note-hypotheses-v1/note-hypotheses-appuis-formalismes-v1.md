---
title: "Ce qui rend une idée intéressante — hypothèses, appuis, formalismes, pistes de test"
subtitle: "Note de travail v1 — 23 novembre 2026"
lang: fr
---

# Mode d'emploi et réserves

- **Ce que c'est.** La synthèse des intuitions du directeur (messages 1 à 7 du 23 novembre, versés dans `intuitions-directeur-2026-11-23-v1.md`). Elle les classe en dix hypothèses, H1 à H10, puis en idées complémentaires. Pour chacune : ce qu'elle dit, ce qui la soutient, comment la formaliser, comment la tester.
- **D'où viennent les statuts.** Trois modèles de Google (Argon, Carbon, Neon) ont été interrogés séparément le 23 novembre. **Ils ont reçu la première version de la question, jugée non neutre (0,55) par un lecteur du collisionneur** : leurs avis ont pu être orientés par les hypothèses. Les réponses de Fable, d'Opus, du collisionneur et la revue bibliographique viendront en version 2.
- **Références.** Les classiques (Koestler, Gentner, Swanson, Kitcher, Burt…) sont donnés tels que les citent les modèles et la mère. **Aucun chiffre n'est opposable avant lecture du PDF, page citée (R7).** Un seul travail a été vérifié en ligne par la mère : Karkada et al. (2026). Les chiffres repris des modèles sont signalés « selon Argon / Carbon ».
- Pièce de classe C, sans contre-lecture.

# 1. Tableau d'ensemble

| | Hypothèse (résumé) | Argon | Carbon | Neon |
|---|---|---|---|---|
| H1 | Mariage de concepts éloignés en surface, proches en structure | Soutenue | Soutenue | Soutenue, nuance forte |
| H2 | Cascades A–B, B–C ⇒ A–C ; transfert vers un domaine jeune | Soutenue | Soutenue, insuffisante seule | Soutenue pour produire ; pas un critère de validité |
| H3 | Serrure et clé : les réseaux en amont doivent s'aligner ; invariant conservé | Soutenue (alignement) ; Noether = métaphore | Idem | Idem |
| H4 | Ni trop près ni trop loin | Soutenue | Soutenue, nuance asymétrique | Soutenue (intérêt) ; en partie (fécondité) |
| H5 | Champ d'interaction, air du temps, découvertes simultanées | Soutenue ; ferromagnétisme, protéines = métaphores | Idem | Idem |
| H6 | Connexion et distinction (fausses identités) | Soutenue | Soutenue | Soutenue ; non mesurée à grande échelle |
| H7 | Profondeur : près des nœuds, unification après coup | Soutenue | Soutenue | Unification oui ; proximité des nœuds en partie contredite |
| H8 | Émergence, transition de phase, percolation, surface de contact | Soutenue | En partie | Surface de contact oui ; transition thermodynamique stricte = métaphore |
| H9 | Structure mathématique cachée du langage | Soutenue | Soutenue, limite critique | En partie soutenue, en partie contredite |
| H10 | Signal de surprise, analogue dopaminergique | Soutenue | Soutenue, avec réserve | Signaux d'information oui ; surprise brute contredite |

**Accord des trois modèles.** Le cœur (H1, H3, H4, H6, H7) est soutenu. Noether et le lagrangien, le ferromagnétisme et l'appariement des protéines sont des métaphores à traduire ou à élaguer. **Désaccords** : H8 (la transition de phase stricte) et H9 (ce que valent les plongements de mots).

# 2. Les hypothèses une à une

## H1 — Le mariage éloigné

**Énoncé.** Une idée intéressante associe deux éléments sans lien logique évident, éloignés en surface (vocabulaire, disciplines, publications), mais proches sur une dimension cachée (structure relationnelle ou mathématique). La surprise vient de la distance de surface ; la viabilité, de la proximité cachée.

**Appuis.**

- La *bisociation* de Koestler (1964, *The Act of Creation*) : deux cadres de pensée cohérents mais habituellement incompatibles qui se rencontrent.
- La théorie de l'appariement de structures de Gentner (1983, *Cognitive Science* 7(2)) : une analogie apparie des relations, pas des attributs. L'atome de Rutherford ressemble au système solaire par « attire » et « tourne autour », jamais par « chaud ».
- Le mélange conceptuel de Fauconnier et Turner (2002) : l'« espace générique » commun aux deux entrées est la dimension cachée.
- Uzzi, Mukherjee, Stringer et Jones (2013, *Science* 342) : les articles à fort impact associent un socle très conventionnel à une petite part de combinaisons atypiques. L'étude porte sur 17,9 millions d'articles selon Argon et Carbon, chiffre à vérifier.
- Shi et Evans (2023, *Nature Communications*) : les combinaisons surprenantes de contenus et de contextes vont avec l'impact, et viennent souvent d'outsiders.
- Le fait empirique qui fonde la « surprise » : on retrouve en mémoire par la ressemblance de surface, si bien que les analogies lointaines sont valides mais rarement trouvées (Gick et Holyoak, problème de la tumeur et de la forteresse).

**Formaliser.** Deux distances par paire de concepts : `d_s(a,b)` en surface (usage, co-occurrence) et `d_σ(a,b) = 1 − q(φ*)` en structure, où `q` est la qualité du meilleur alignement des voisinages. Une idée « bisociative » a `d_s` grand et `d_σ` petit.

**Tester.** Sur des corpus datés, les paires à `d_s` grand et `d_σ` petit avant la date *t* deviennent-elles des liens féconds après *t*, mieux que la surface seule ? C'est le test T1 ou T2 de la partie 5.

## H2 — Cascades et transferts

**Énoncé.** Des chaînes de mariages (A lié à B, B lié à C, donc A–C neuf), et le transfert d'un résultat d'un domaine mûr vers un domaine jeune. Exemple : douleur et anesthésie, anesthésie et conscience, puis un motif d'« anesthésie » cherché dans les modèles de langage.

**Appuis.** Le modèle A-B-C de Swanson (1986, *Perspectives in Biology and Medicine* 30) : huile de poisson, viscosité du sang, maladie de Raynaud. Le transfert analogique guidé par le but : Holyoak et Thagard (1995, *Mental Leaps*).

**Limite** (Carbon, Neon) : seul, le chaînage produit beaucoup de faux positifs, à cause des mots à plusieurs sens. Il faut le filtre structurel de H3.

**Formaliser.** Les chemins de longueur 2 ou 3 dans la couche d'usage, pondérés par `q` dans la couche de structure.

## H3 — Serrure et clé, invariance

**Énoncé.** Il ne suffit pas que deux points s'emboîtent : les réseaux en amont de chaque parent doivent pouvoir coexister, et un invariant doit tenir sous la transformation qui les rapproche.

**Appuis.**

- Le *principe de systématicité* de Gentner (1983) : on préfère les systèmes de relations liés par des relations d'ordre supérieur, comme une cause.
- Le moteur d'appariement de structures (SME, Falkenhainer, Forbus et Gentner, 1989) exige une correspondance un pour un et une connectivité parallèle : si deux relations s'apparient, leurs arguments aussi. C'est la phrase du directeur « les réseaux en amont doivent coexister ».
- Les foncteurs, qui préservent la structure (Mac Lane, 1971 ; Spivak, 2014), et les « ologs » de Spivak et Kent (2012).
- Copycat de Hofstadter et Mitchell : une « profondeur conceptuelle » des concepts, et des distances qui raccourcissent quand ils sont activés. C'est le plus proche du puits et du champ du directeur.

**Noether et le lagrangien** : métaphore selon les trois modèles. Le théorème demande une action et une symétrie continue, absentes d'un graphe de concepts discret. Voir la partie 4, F10, pour ce qu'on peut sauver.

**Formaliser (traduction exacte).**

- La serrure-clé est un homomorphisme partiel de graphes typés, ce que calcule SME.
- « La même loi dans les deux domaines » est l'*équivariance* : `f ∘ T₁ = T₂ ∘ f`. La correspondance commute avec la dynamique ; la Lune et la pomme obéissent à la même équation du mouvement.
- « L'invariance doit tenir quelle que soit la projection » est la *naturalité* au sens des catégories.

## H4 — Ni trop près ni trop loin

**Appuis.**

- La courbe en U inversé de la curiosité (Berlyne, 1960).
- La « distance cognitive optimale » entre partenaires d'innovation (Nooteboom et al., 2007, selon Argon).
- L'arbitrage entre consolidation locale et sauts lointains (Foster, Rzhetsky et Evans, 2015).

**Nuance** (Carbon) : la fécondité ne culmine pas à une distance moyenne uniforme. Elle culmine dans un mélange : socle conventionnel plus queue très atypique (Uzzi et al., 2013).

## H5 — Champ d'interaction et air du temps

**Énoncé.** Deux concepts lointains interagissent s'ils répondent à un même « champ ». Ce champ naît d'un cadre nouveau (technologie, méthode, instrument) qui rend les deux réseaux **comparables, dans un même espace de description**. Les découvertes simultanées en sont la trace.

**Appuis.**

- Ogburn et Thomas (1922) recensent les découvertes multiples (148 cas, selon Argon et Carbon) ; Merton (1961) en fait la règle une fois les prérequis réunis.
- Simonton : le nombre de co-découvreurs suit à peu près une loi de Poisson.
- Galison (2003, *Einstein's Clocks, Poincaré's Maps*) : la synchronisation des horloges par télégraphe, les chemins de fer et le bureau des brevets comme substrat commun à Einstein et à Poincaré.

**Formaliser.** Voir la partie 4, F3 et F4. Le champ se mesure *avant* la découverte, par la diffusion d'un cadre commun dans les deux communautés, jamais par l'issue : c'est le garde-fou contre la circularité. Ferromagnétisme et protéines : métaphores selon les trois modèles. Le contenu qu'on en garde est une cause commune qui fait co-varier deux régions lointaines.

## H6 — Connexion et distinction

**Énoncé.** La même projection qui rapproche des concepts lointains sépare ce qui semblait identique (fausses identités).

**Appuis.**

- Davis (1971, *That's interesting!*) : une thèse intéressante soit unifie des phénomènes crus hétérogènes, soit dissocie des phénomènes crus identiques.
- Les « différences alignables » de Gentner et Markman (1997).
- Lakatos (1976, *Preuves et réfutations*) : la collision avec un contre-exemple force la scission de concepts confondus.
- Exemples : simultanéité « ici » contre « pour tous » ; chaleur contre température (Black) ; masse et poids.

**À corriger dans l'exemple du directeur.** Les masses inerte et grave sont une *connexion* et non une distinction. Ce sont deux concepts newtoniens égaux par l'expérience ; Einstein a fait de leur égalité un principe.

**Trou de la littérature** (Neon) : la scission est peu mesurée à grande échelle ; les modèles quantitatifs étudient surtout la recombinaison. C'est une piste prioritaire (T5, et l'opérateur de scission de l'organisme).

## H7 — Profondeur de l'idée fille

**Énoncé.** L'idée fille doit tomber près de concepts « nœuds » et expliquer après coup pourquoi elle surprenait : la Lune et la pomme.

**Appuis.**

- L'unification de Kitcher (1981, *Philosophy of Science* 48) : expliquer davantage avec moins de schémas d'argument.
- L'indice de disruption (Funk et Owen-Smith, 2017 ; Wu, Wang et Evans, 2019) : une idée disruptive *éclipse* ses références au lieu de s'y arrimer.

**Nuance** (Neon) : la proximité aux nœuds est en partie contredite. Les idées les plus disruptives déplacent les anciens nœuds au lieu de s'y accrocher. La profondeur se lirait donc moins dans « près des nœuds » que dans « devient un nœud ».

## H8 — Émergence, transition de phase, percolation

**Appuis.**

- Les trous structuraux de Burt (2004, *American Journal of Sociology* 110) : être à l'interface de deux réseaux denses va avec de meilleures idées.
- La naissance d'un domaine ressemble à une transition de percolation dans le réseau des coauteurs (Bettencourt, Kaiser et al., 2008 et 2009).
- Le possible adjacent (Kauffman) et le modèle d'urnes à déclenchement de Tria, Loreto, Servedio et Strogatz (2014).

**Désaccord.** Pour Neon, une transition thermodynamique stricte, avec exposants critiques en taille infinie, ne se transpose pas à des réseaux finis. Pour Carbon, la percolation *conceptuelle* pure reste à prouver.

**Position du directeur** : il faut les chercher, quitte à créer un cadre neuf. Outil : l'analyse de taille finie (partie 5, T6).

## H9 — La structure cachée du langage

**Appuis.**

- Mikolov et al. (2013) : des relations deviennent des translations dans l'espace des plongements de mots.
- Tshitoyan et al. (2019, *Nature* 571) : des plongements appris sur des résumés de science des matériaux retrouvent le tableau périodique et désignent des thermoélectriques avant leur découverte.
- **Karkada, Korchinski, Nava, Wyart et Bahri (2026, arXiv 2602.15029, ICML 2026, vérifié en ligne d'après le résumé)** : la co-occurrence de deux mois ne dépend que de l'intervalle qui les sépare. Cette symétrie de translation donne leur forme circulaire aux représentations, et la structure persiste quand on retire les phrases où les deux mois apparaissent ensemble.

**Limite** (Carbon, Neon) : les vecteurs de co-occurrence confondent proximité de thème et isomorphisme de relations. Il faut des représentations explicites des relations.

**Thèse faible**, soutenue : les corpus encodent la structure relationnelle du savoir. **Thèse forte**, non établie : le langage refléterait les lois de l'univers.

**Piste.** Chercher les *symétries des statistiques de co-occurrence* comme trace de symétries du réel (T7).

## H10 — Le signal de surprise

**Appuis.**

- La dopamine code une erreur de prédiction de récompense signée (Schultz, Dayan et Montague, 1997), pas une surprise pure.
- La surprise bayésienne, divergence entre ce qu'on croyait avant et après (Itti et Baldi, 2009).
- La curiosité comme *progrès de compression*, dérivée de la capacité à prédire (Schmidhuber, 2010) ; le progrès d'apprentissage (Oudeyer, Kaplan et Hafner, 2007).
- Dans les modèles de langage : un « sous-système de récompense éparse » (Xu, Yuksekgonul et Zou, arXiv 2602.00986, 2026), déjà étudié au dépôt (`docs/notes/papier-dopamine-moniteur-v1/`).

**Consensus.** La surprise brute est un mauvais signal : le bruit surprend sans rien apprendre. Le bon signal est la surprise *suivie* d'un gain de compression.

# 3. Idées complémentaires du directeur (messages 4 à 7)

1. **Le champ croît quand deux réseaux se rapprochent**, comme l'inverse d'une fonction croissante de la distance. Toute la difficulté est la bonne distance, dans les bonnes dimensions. Mais rapprocher ne suffit pas : il faut des collisions menées activement (expériences, publications). Poincaré a failli aboutir parce qu'il tenait la bonne invariance.
2. **Le champ est la direction dans laquelle un cadre nouveau rend deux réseaux comparables**, et non celle où l'invariance « apparaît évidente ». Le directeur a confirmé ce point.
3. **Le champ combine invariants et probabilités de rencontre** : la densité des réseaux, et la manière dont une transformation qui préserve l'invariance rapproche deux réseaux jusqu'à la collision.
4. **Mesurer directement les invariances** par le rapprochement des structures sous-jacentes. C'est la bonne mesure, à une condition d'hygiène temporelle : la calculer avec ce qui était écrit *avant* la date.
5. **Identités tenues pour vraies.** Découvrir qu'une identité « évidente » ne va pas de soi, avec des conséquences profondes une fois les réseaux identifiés. Trois figures :
   - l'identité contingente promue en principe ;
   - la fausse identité scindée ;
   - l'identité cachée entre domaines.
6. **Scission conceptuelle dans l'organisme**, et mécanismes disruptifs à l'origine des scissions.
7. **Anomalies** (Kuhn, 1962 ; Lakatos, 1970) : les échecs persistants d'un cadre doivent *polariser* la recherche d'analogies. C'est une couche des problèmes ouverts et des contradictions.
8. **Méta-espace mathématique.** Séparer la structure abstraite, qui préexiste, de sa transcription dans un alphabet humain, qui peut manquer (Carey, 2009). Deux phases :
   - découvrir des objets mathématiques nouveaux à partir de corpus et d'espaces bien choisis ;
   - les appliquer à la recherche d'idées.

   Une **troisième couche « méta »** du graphe porterait les anomalies, les problèmes ouverts et les objets formels en gestation. Difficulté : la circularité (trouver des objets qui ne se révèlent qu'avec des idées pas encore trouvées).
9. **Principe variationnel.** En trouver un pour un graphe conceptuel discret et dissipatif.
10. **Maximiser le progrès de compression** dans l'organisme.

# 4. Les formalismes candidats

- **F1. Graphe daté à plusieurs couches.**
  - Usage : mots, co-occurrences, publications.
  - Structure : relations typées, formes d'équations.
  - Humains : auteurs, communautés.
  - Méta : anomalies, problèmes ouverts, objets formels nouveaux (idée 8).
- **F2. Deux distances.**
  - `d_s` : distance de surface dans la couche d'usage.
  - `d_σ = 1 − q(φ*)` : distance de structure, où `q` est la qualité du meilleur alignement des voisinages en amont. Outils : SME, transport optimal de Gromov-Wasserstein (comparer deux réseaux sans vocabulaire commun), formes d'équations partagées.
- **F3. Taux de naissance d'un lien, sur le modèle de la cinétique chimique** : `F = λ · exp(−E/T) · q`.
  - `λ` : fréquence de rencontre, proportionnelle aux densités des deux voisinages et décroissante avec `d_s`.
  - `E` : barrière abaissée par un cadre commun, ce qui rend les réseaux comparables.
  - `q` : facteur stérique, la serrure-clé.
- **F3 bis. Version statistique, un modèle de risque à covariables datées** : `h_ab(t) = h₀ · exp(β·F_a(t)·F_b(t) + γ·q_ab(t) + δ·anomalie_ab(t))`. `F_a(t)` mesure la diffusion d'un cadre ou d'un instrument dans la communauté *a* ; `anomalie_ab(t)` la tension non résolue qui touche les deux.
- **F4. Découvertes multiples** : une fois les prérequis disponibles, `N(t)` chercheurs ayant le cadre trouvent avec une probabilité `p(t)`. Le nombre de co-découvreurs suit une loi de Poisson de paramètre `N·p`. Le substrat de Galison augmente `N` et `p`.
- **F5. Intérêt, relatif à un public** : `I(c) = surprise_public(c) × gain_compression(c)`.
  - La surprise se mesure contre ce que le public croyait à la date *t* (Davis ; surprise bayésienne).
  - Le gain est la baisse de l'erreur de prédiction sur les deux domaines parents une fois l'idée connue (Schmidhuber).
- **F6. Profondeur** : l'unification (Kitcher) ou le gain de compression ; dans les citations, l'indice de disruption.
- **F7. Invariance** : homomorphisme partiel de graphes typés ; équivariance `f ∘ T₁ = T₂ ∘ f` ; naturalité. Les automorphismes et groupoïdes de symétries sont l'analogue discret honnête d'une symétrie.
- **F8. Identités et scissions.**
  - Graphe : une identité est un nœud fusionné. La scission découpe le nœud en « personas » selon les communautés de son voisinage (méthode dite « ego-splitting »).
  - Isomorphisme : canonique, ou qui dépend d'un choix de cadre (la simultanéité).
  - **Faisceaux** : chaque concept porte une représentation locale et chaque lien une règle de passage. Une identification qui ne se recolle pas globalement laisse une obstruction mesurable : laplacien de faisceau, holonomie autour d'un cycle.
  - Théorie des types homotopiques : l'égalité est un chemin, et le *transport* le long de ce chemin emporte toute la structure. C'est la mesure de « l'implication profonde ».
- **F9. Dynamique d'émergence** :
  - urnes à déclenchement, où chaque nouveauté ouvre des possibles adjacents (Tria et al., 2014) ;
  - percolation sur réseaux multiplex ou interdépendants ;
  - **analyse de taille finie** pour chercher des exposants critiques sur des réseaux finis ;
  - topologie des lacunes : les cavités d'homologie persistante qui se comblent plus tard (Sizemore et al., 2018, à vérifier).
- **F10. Principe variationnel sans lagrangien canonique.**
  - Entropie maximale sur les trajectoires (« maximum caliber », Jaynes ; Pressé et al., 2013).
  - Action des grandes déviations (Onsager-Machlup).
  - Flots de gradient de l'entropie sur un graphe (Maas, 2011) : version discrète de la diffusion vue comme descente d'énergie libre.

  On *estime* l'action sur la croissance réelle des graphes, puis on teste si les trajectoires observées la minimisent mieux qu'un modèle nul.
- **F11. Méta-couche et objets formels nouveaux.**
  - Une couche des anomalies et des problèmes ouverts, qui pèse sur le risque de F3 bis.
  - Une couche des structures mathématiques : algèbres, catégories, formes d'équations, programmes.
  - Une révolution conceptuelle serait un *enrichissement* de cet alphabet de relations. Il serait précédé de signaux mesurables : anomalies persistantes, calculs ad hoc répétés, notations qui prolifèrent, problèmes ouverts qui convergent.

# 5. Pistes de test

Toutes demandent un préenregistrement scellé et une période tenue à l'écart (R1).

- **T1. Formes d'équations partagées** (proposition d'Argon).
  - Méthode : sur les sources LaTeX d'arXiv, repérer les paires de domaines qui partagent une forme d'équation sans se citer.
  - Prédiction : ces paires forment davantage de ponts ultérieurs que des paires témoins de même distance de surface. Quatre jours, sur processeur.
- **T2. Le cœur H1 × H3 en biomédecine** (proposition de Neon).
  - Méthode : figer le graphe à 2015 (SemMedDB, PubMed, OpenAlex) ; calculer `d_s` et l'alignement de Gromov-Wasserstein des voisinages ; prédire la fécondité des paires nées en 2016-2017, citées et reprises jusqu'en 2022.
  - Réfutation : `q` et l'interaction `d_s × q` n'apportent rien sur un modèle de surface et de chemins A-B-C.
- **T3. Découvertes multiples.** Les multiples de Merton, d'Ogburn et de Thomas tombent-ils là où un cadre commun venait de diffuser dans les deux communautés (F4) ?
- **T4. Progrès de compression, sur un modèle ouvert.** Préfixer une idée candidate et mesurer la baisse de la perte de prédiction sur des faits des *deux* domaines parents, contre une idée témoin de même longueur. Faisable sur un modèle de 8 milliards de paramètres.
- **T5. Scissions.** Le signal de scission en personas, ou l'obstruction du faisceau, monte-t-il dans les corpus *avant* la publication historique de la distinction ? Cas : masse, simultanéité, chaleur et température. Témoins : des mots à double sens sans conséquence.
- **T6. Transitions de phase.**
  - Méthode : analyse de taille finie sur la croissance des graphes de concepts de domaines naissants.
  - Réfutation : les courbes ne se superposent pas après mise à l'échelle.
- **T7. Symétries des co-occurrences.** Chercher dans des corpus scientifiques des statistiques invariantes par un groupe (translation, rotation, échelle), dans l'esprit de Karkada et al. (2026), et voir si elles annoncent des lois connues.
- **T8. Dans l'organisme d'idéation, au dégel.**
  - Trois opérateurs nouveaux : la scission d'identités tenues pour vraies ; la polarisation par les anomalies ; la récompense par le progrès de compression.
  - Juger sur l'oracle des mondes plantés et le coût, jamais sur l'avis d'un juge (N-058).
  - Tester aussi la percolation conceptuelle sur les graphes produits.

# 6. Ce qui manque encore (selon les modèles et la mère)

- **Le public** : l'intérêt dépend de ce qu'un public croit à une date (Davis).
- **Les échecs** : il faut les taux de base des analogies ratées, contre le biais du survivant.
- **Le coût et la faisabilité du test** : la technologie y joue de nouveau.
- **La fécondité aval** : combien de possibles l'idée ouvre.
- **Les porteurs humains** : les idées se rencontrent quand des gens se rencontrent.
- **Le moteur des anomalies** (Kuhn, Lakatos).
- **La genèse de nouvelles abstractions** (Carey).

# 7. Références citées

Classiques cités par les modèles et la mère, tous **à vérifier sur PDF** avant usage chiffré :

- Berlyne (1960)
- Bettencourt, Kaiser et al. (2008, 2009)
- Burt (2004)
- Carey (2009)
- Davis (1971)
- Falkenhainer, Forbus et Gentner (1989)
- Fauconnier et Turner (2002)
- Foster, Rzhetsky et Evans (2015)
- Funk et Owen-Smith (2017)
- Galison (2003)
- Gentner (1983)
- Gentner et Markman (1997)
- Gick et Holyoak (1980)
- Hofstadter et Mitchell (1995)
- Hofstadter et Sander (2013)
- Holyoak et Thagard (1995)
- Itti et Baldi (2009)
- Kauffman (1995)
- Kitcher (1981)
- Koestler (1964)
- Krenn et Zeilinger (2020)
- Kuhn (1962)
- Lakatos (1970, 1976)
- Maas (2011)
- Mac Lane (1971)
- Merton (1961)
- Mikolov et al. (2013)
- Nooteboom et al. (2007)
- Ogburn et Thomas (1922)
- Oudeyer, Kaplan et Hafner (2007)
- Pressé et al. (2013)
- Rzhetsky, Foster, Foster et Evans (2015)
- Schmidhuber (2010)
- Schultz, Dayan et Montague (1997)
- Shi et Evans (2023)
- Simonton (2004)
- Sizemore et al. (2018)
- Sourati et Evans (2023)
- Spivak et Kent (2012)
- Swanson (1986)
- Tria, Loreto, Servedio et Strogatz (2014)
- Tshitoyan et al. (2019)
- Uzzi, Mukherjee, Stringer et Jones (2013)
- Wu, Wang et Evans (2019)
- Xu, Yuksekgonul et Zou (2026, arXiv 2602.00986, lu au dépôt)

**Vérifié en ligne par la mère (résumé)** : Karkada, Korchinski, Nava, Wyart et Bahri (2026), « Symmetry in language statistics shapes the geometry of model representations », arXiv 2602.15029.
