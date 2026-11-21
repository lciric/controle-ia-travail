### Préambule d'intégrité et convention de statuts

* **Intégrité des pièces (Règle 2)** : Dans ce tour à l'aveugle, les deux blocs attendus (`FAITS` et `QUESTION DE L'ARBITRE`) sont présents, complets et non coupés.
* **Statuts épistémiques (Règle 1)** : Les éléments du dossier sont marqués `[RAPPORTÉ]` ; l'existence de travaux voisins de 2026 croisés par hasard est `[RAPPORTÉ]`, mais leur recouvrement réel avec le pilier — puisqu'ils n'ont pas été lus — demeure `[OBSERVÉ-NON-AUDITÉ]` ; les équivalences mathématiques ou propriétés logiques directement démontrables sont marquées `[VÉRIFIÉ]` ; toute supposition implicite, mécanisme causal proposé ou estimation de comportement porte le statut `[HYPOTHÈSE]`.
* **Inconnues et chiffres (Règle 4 & consigne de l'arbitre)** : Aucune grandeur empirique absente des faits (budget par cible, volume exact de la bibliothèque Lean, tarif du lecteur humain, nombre d'articles de 2026 croisés) n'est inventée : nous écrivons explicitement **« je ne sais pas »**. Tout nombre hors des faits introduit pour paramétrer un protocole ou un dimensionnement matériel est un paramètre de conception proposé et marqué `(illustratif)`.

---

## I. Livrable (a) — Ce que la question suppose sans que ce soit établi

La question met en balance trois options — **(a)** lire et empreinter dès maintenant cinq zones par un agent avant tout scellement, **(b)** attendre la première revendication, **(c)** lire pour tout le pilier — qui reposent sur six présupposés non établis :

1. **Homogénéité de la notion de « nouveauté » sur les trois formes de cibles** `[HYPOTHÈSE]` *(implicite dans la question)*. Établi : les cibles payantes sont en liste fermée, à budget égal, sous trois formes : *objet à score exact*, *énoncé à démontrer ou réfuter*, *lemme de bibliothèque* `[RAPPORTÉ]`. Notre analyse : ces trois formes n'ont pas le même critère d'antériorité `[VÉRIFIÉ]`. Un *lemme de bibliothèque* est le plus souvent mathématiquement classique (p. ex. variante de Fano ou d'arrêt optionnel) mais neuf dans l'écosystème formel Lean ; un *objet à score exact* n'est invalidé que si une règle connue bat déjà ce score sur l'instance fixée ; seul l'*énoncé à démontrer ou réfuter* requiert l'absence de preuve ou de réfutation dans la littérature mathématique.
2. **Clôture disciplinaire des « cinq zones » de l'option (a)** `[HYPOTHÈSE]` *(implicite dans l'option a)*. En réalité, par dualité convexe et changement de vocabulaire `[VÉRIFIÉ]`, au moins quatre de ces zones possèdent des jumeaux exacts hors de leurs mots-clés statistiques :
   * la fusion de p-valeurs et d'e-valeurs sous dépendance arbitraire est mathématiquement isomorphe aux bornes de copules (Fréchet–Hoeffding, Rüschendorf) pour l'agrégation de risques en actuariat `[VÉRIFIÉ]` (voir Vladimir Vovk et Ruodu Wang, 2021 `(illustratif)`, *E-values: Calibration, combination and applications*) ;
   * un jeu d'inspection sous budget (Rudolf Avenhaus, Bernhard von Stengel et Shmuel Zamir, 2002 `(illustratif)`, *Inspection Games*) équivaut, par dualité minimax, à une frontière de test sous coût d'échantillonnage (comparaison d'expériences de David Blackwell, 1953 `(illustratif)`, *Equivalent Comparisons of Experiments*), mais se publie aussi en microéconomie sous le nom d'*audit stratégique / costly state verification* et en IA sous le nom de *Stackelberg security games* `[VÉRIFIÉ]` ;
   * quant à la cinquième zone (*recherche de programmes appliquée à des règles de décision*), c'est une méthode d'optimisation et non le corpus où résident les règles statistiques classiques susceptibles de collisionner `[VÉRIFIÉ]`.
3. **Suffisance d'une « empreinte d'article » produite *avant* de connaître l'énoncé-cible** `[HYPOTHÈSE]` *(implicite dans l'option a)*. Qu'un résumé structuré produit *a priori* capture la constante exacte, l'hypothèse fine de mesurabilité ou un corollaire implicite en annexe n'est pas établi.
4. **Neutralité des premières revendications vis-à-vis de l'antériorité** `[HYPOTHÈSE]` *(implicite dans l'option b)*. Les agents étant à base de modèles de langage `[RAPPORTÉ]`, leur mémoire paramétrique les attire en priorité vers les énoncés de la liste fermée déjà démontrés dans leur corpus d'entraînement ou leurs corollaires immédiats `[HYPOTHÈSE]`. Attendre la première revendication expose donc à découvrir la pollution de la liste fermée précisément après avoir dépensé le budget des pilotes.
5. **Confusion entre « veille bibliographique continue » et « audit d'antériorité requêté par cible »** `[HYPOTHÈSE]` *(implicite dans l'opposition gel vs lecture large)*. Le directeur a gelé la veille bibliographique pour économiser l'effort `[RAPPORTÉ]`. Or geler un flux passif hebdomadaire n'implique pas de sceller une cible à l'aveugle sans requête ciblée sur son énoncé précis.
6. **Paramètres économiques du programme** : **je ne sais pas** combien de cibles composent la liste fermée, quel est le budget par cible, quel est le coût d'une collision par rapport à une heure de lecteur humain, ni combien de travaux de 2026 ont été croisés `[OBSERVÉ-NON-AUDITÉ]`.

---

## II. Question 1 — Ce qu'un expert ferait ici, et qu'on ne demande pas

En distinguant ce qui est établi dans les faits de notre proposition méthodologique :

1. **Vider immédiatement les deux gisements à coût de recherche nul (avant tout débat macroscopique)** *(notre proposition)* :
   * *Lire la pile de 2026 déjà croisée* : plusieurs travaux voisins de 2026 ont été croisés par hasard sans être lus `[RAPPORTÉ]`, leur collision potentielle étant `[OBSERVÉ-NON-AUDITÉ]`. Puisque le coût de repérage est déjà nul et la proximité thématique présumée élevée `[HYPOTHÈSE]`, ne pas les auditer en premier est sous-optimal sous n'importe quelle option.
   * *Extraire mécaniquement le graphe des déclarations de la bibliothèque Lean publique* : cette bibliothèque couvre déjà une part du vocabulaire (divergences, Fano, Bretagnolle–Huber, identité de Wald, e-valeurs) `[RAPPORTÉ]`. Un script d'inspection de l'arbre syntaxique Lean cartographie en quelques minutes `(illustratif)` les signatures exactes déjà prouvées (alphabets finis vs espaces mesurables généraux, hypothèses d'intégrabilité de Wald).
2. **Tenter de « tuer » chaque cible candidate par calcul fini et sonde de mémorisation *avant* toute recherche documentaire** *(notre proposition)* :
   * *Trivialisation / réfutation sur petits cardinaux* : coder un programme linéaire ou semi-défini (LP/SDP) sur un alphabet de taille $2$ ou $3$ `(illustratif)` et un horizon $T \in \{2,3\}$ `(illustratif)`. Si une combinaison élémentaire des outils déjà cités dans les faits (inégalité de Bretagnolle–Huber, arrêt de Wald, moyenne arithmétique d'e-valeurs) atteint déjà la borne ou réfute l'énoncé, la cible est éliminée sans lire un seul article `[VÉRIFIÉ]`.
   * *Sonde d'attribution contradictoire* : interroger deux familles distinctes de modèles de langage en mode « réduction de cours » (*« À quel théorème classique d'économie, d'actuariat ou de théorie de l'information cet énoncé se réduit-il en moins de cinq lemmes ? »* — chiffre `(illustratif)`).
3. **Séparer l'utilité défensive pour le contrôle IA de la prime à la nouveauté mathématique** *(notre proposition)* :
   * Le programme a un objectif défensif sur le contrôle des systèmes d'IA `[RAPPORTÉ]`. Si une borne d'impossibilité de détection ou un équilibre d'inspection sous budget existe déjà dans un article d'audit économique ou de 2026, c'est une **mauvaise cible de « mathématiques nouvelles »**, mais un **acquis immédiat et peu coûteux pour le contrôle**. Un expert créerait une prime modique de « fermeture par importation bibliographique + formalisation Lean » plutôt que d'aligner toutes les cibles sur un budget égal `[RAPPORTÉ]` qui incite à ignorer la littérature `[HYPOTHÈSE]`.
4. **Calculer une signature numérique invariante au dialecte** *(notre proposition)* :
   * Deux théorèmes formulés l'un en « fusion de p-valeurs sous dépendance », l'autre en « borne de VaR sous copule inconnue » n'ont aucun mot en commun mais produisent **exactement la même constante rationnelle ou algébrique optimale** pour $K=2, 3, 4$ `(illustratif)` variables `[VÉRIFIÉ]`. Chercher ces constantes et formes duales traverse les frontières disciplinaires là où la recherche lexicale échoue `[HYPOTHÈSE]`.

---

## III. Question 2 — Les données brutes de départ

* **Bases d'articles et graphes de citations** :
  * Sources LaTeX brutes d'arXiv (indispensables pour parser les formules sans erreurs d'OCR `[VÉRIFIÉ]`), non limitées à `math.ST` et `stat.ME`, mais étendues aux silos jumeaux : `cs.IT` (frontières de détection / divergences), `cs.GT` et `econ.TH` (inspection / audit sous budget), `q-fin.RM` (agrégation sous dépendance arbitraire), `cs.LG` et `cs.PL` (synthèse de programmes).
  * Bases indexées avec classification mathématique fine MSC : zbMATH Open et MathSciNet (notamment `62L10` analyse séquentielle, `62C20` procédures minimax, `62G10` tests non paramétriques, `91Axx` théorie des jeux `[VÉRIFIÉ]`).
  * Graphes de citations ouverts (OpenAlex, Semantic Scholar) initialisés sur deux graines : les articles fondateurs correspondant au vocabulaire de la bibliothèque Lean (`[RAPPORTÉ]`) et la liste interne des travaux de 2026 croisés par hasard (`[RAPPORTÉ]`, liste exacte : **je ne sais pas**).
* **Bibliothèques formelles** :
  * La bibliothèque Lean de statistique publique mentionnée dans le dossier `[RAPPORTÉ]` (**je ne sais pas** quel est son identifiant de dépôt exact hors de cette description) et `mathlib4` (mesure, probabilités, martingales, espérance conditionnelle), incluant **leurs branches actives, *pull requests* ouvertes et *issues***, plus l'historique public Zulip Lean (`Is there code for X?`).
  * Corpus formels voisins pour détecter les théorèmes déjà mécanisés ailleurs : *Archive of Formal Proofs* (Isabelle/HOL) et `MathComp-Analysis` (Coq/Rocq).
* **Listes de problèmes ouverts** :
  * Contributions *Open Problems* de la conférence COLT (publiées dans PMLR), sections finales de problèmes ouverts des revues sur les e-processus / martingales de test (issues de l'inégalité de Jean Ville, 1939 `(illustratif)`, *Étude critique de la notion de collectif*) et tableaux de bord *Lean Blueprint* des projets de formalisation statistique actifs.
* **Notices de bancs (benchmarks)** :
  * Dépôts publics de synthèse évolutionnaire/LLM de programmes à score exact (évaluateurs déterministes de découverte combinatoire ou algorithmique — référence à vérifier pour chaque banc spécifique), bancs d'évaluation d'audit/détection en contrôle IA, et les cahiers des charges internes des cibles à score exact du programme (`[RAPPORTÉ]`, contenu détaillé : **je ne sais pas**).

---

## IV. Question 3 — Méthodes et outils précis d'une recherche d'antériorité : suppositions et modes d'échec

Aucun outil isolé ne garantit l'absence totale de collision hors d'un système formel clos `[VÉRIFIÉ]`. Une chaîne d'antériorité robuste empile six méthodes aux modes d'échec disjoints `[HYPOTHÈSE]` :

1. **Recherche lexicale structurée (BM25 sur sources `.tex` + codes MSC + expansion systématique vers les dialectes jumeaux)** :
   * *Ce qu'elle suppose* : que le résultat emploie au moins l'un des vocabulaires répertoriés (statistique, actuariat, économie de l'audit, théorie de l'information) ou une équation canonique nommée.
   * *Comment elle échoue* : manque les « lemmes techniques sans nom » enfouis au cœur de la preuve d'un article appliqué dont ni le titre ni le résumé ne mentionnent l'outil général.
2. **Récupération hybride dense/creuse + marche bidirectionnelle dans le graphe de citations (voisinage à $2$ sauts `(illustratif)` des articles-pivots et des papiers de 2026)** :
   * *Ce qu'elle suppose* : qu'une collision partage l'ancrage bibliographique fondamental (Fano, Bretagnolle–Huber, Wald, Vovk–Wang, Blackwell) ou une proximité sémantique globale.
   * *Comment elle échoue* : **cécité logique aux quantificateurs et aux hypothèses fines** — les plongements vectoriels confondent $\inf_\psi \sup_P$ et $\sup_P \inf_\psi$, ou nul stationnaire et nul non stationnaire `[VÉRIFIÉ]` ; en outre, les prépublications de 2026 n'ont pas encore accumulé de citations entrantes.
3. **Empreintage mathématique canonique par schéma typé (extraction structurée à partir du LaTeX complet)** :
   * *Principe* : extraire non un résumé en prose, mais un n-uplet normalisé : *(espace d'états, structure de dépendance/filtration, classe d'hypothèses nulles $\mathcal{P}_0$ et alternatives $\mathcal{P}_1$, contraintes de budget, fonctionnelle optimisée, sens de la borne, constantes explicites)*.
   * *Ce qu'il suppose* : que l'agent résout correctement la portée des hypothèses globales du document LaTeX (p. ex. une hypothèse *« Throughout Section 4, $P_t = P$ »* située trois pages `(illustratif)` avant le théorème).
   * *Comment il échoue* : hallucination de portée (oubli d'une hypothèse implicite de stationnarité créant une fausse alerte, ou non-détection qu'un théorème général pour une $f$-divergence couvre la cible pour le cas particulier de Hellinger).
4. **Hachage sémantique par évaluation sur petites instances finies et séquences extrémales** :
   * *Principe* : évaluer numériquement la valeur minimax de la cible sur de petits paramètres discrets ($K \in \{2,3,4\}$ `(illustratif)`) et confronter les constantes/formules fermées obtenues aux expressions extraites des articles candidats (ainsi qu'à l'OEIS pour les structures discrètes).
   * *Ce qu'il suppose* : que l'énoncé ou l'objet à score se spécialise non trivialement à de petites dimensions finies.
   * *Comment il échoue* : aveugle aux résultats purement asymptotiques à constantes non spécifiées ($\asymp$, $O(\cdot)$).
5. **Recherche formelle d'énoncés par unification et recherche sémantique sur types Lean** (tactiques natives `exact?`, `apply?`, `#find`, et moteurs d'indexation Lean tels que Loogle, Moogle ou LeanSearch — références à vérifier) :
   * *Ce qu'elle suppose* : que le résultat est déjà formalisé dans Lean et encodé avec des structures de types compatibles.
   * *Comment elle échoue* : muette sur toute la littérature non formalisée (dont les prépublications de 2026 `[OBSERVÉ-NON-AUDITÉ]`) et vulnérable au **schisme de représentation** dans Lean `[VÉRIFIÉ]` (un lemme prouvé sur des distributions finies `PMF α` ne s'unifie pas automatiquement avec son jumeau sur `MeasureTheory.Measure α`).
6. **Réduction déductive active (« attaque par corollaire court »)** :
   * *Principe* : face aux $k$ théorèmes publiés les plus proches (p. ex. $k = 10$ `(illustratif)`), demander à un agent prouveur (assisté de Lean ou d'un solveur SMT) de **démontrer la cible en supposant le théorème publié comme axiome**.
   * *Ce qu'elle suppose* : qu'une collision déguisée se déduit du théorème existant par changement de variables, dualité de Lagrange/Sion ou spécialisation en peu d'étapes.
   * *Comment elle échoue* : asymétrie logique `[VÉRIFIÉ]` — une réduction formellement vérifiée certifie la collision, mais l'échec du prouveur dans son budget de calcul ne prouve jamais l'absence de collision.

---

## V. Question 4 — Ce qui, hors du programme, vérifierait qu'une cible est neuve

1. **Mainteneurs de bibliothèques formelles** (mainteneurs de `mathlib4` et de la bibliothèque Lean de statistique publique) :
   * *Ce qu'ils vérifient* : la nouveauté **formelle et architecturale** d'un *lemme de bibliothèque* (absence de généralisation déjà présente sous un nom abstrait de théorie de la mesure ou en cours de revue dans une PR).
   * *Limite* : ne suivent pas nécessairement les prépublications de statistique ou de jeux d'inspection de 2026 `[HYPOTHÈSE]`.
2. **Moteurs externes de recherche formelle d'énoncés et compilation continue contre `HEAD` public** :
   * *Ce qu'ils vérifient* : l'absence de résolution automatique à un saut (`exact?`, `aesop?`) dans les dépôts publics à jour.
   * *Limite* : couverture restreinte au déjà-formalisé et sensibilité à l'encodage des types `[VÉRIFIÉ]`.
3. **Relecteur humain externe spécialiste du domaine** (distinct du lecteur interne si l'on veut une validation hors programme) :
   * *Ce qu'il vérifie* : le **folklore non publié** (*« résultat connu des spécialistes comme exercice sur le lemme de Le Cam »*), la non-vacuité des hypothèses et la littérature fraîche de sa propre communauté.
   * *Deux limites critiques* : (i) **cloisonnement disciplinaire** `[HYPOTHÈSE]` — un expert des e-valeurs ignore souvent la littérature des jeux d'inspection ou de l'audit microéconomique ; s'il reçoit l'énoncé nu sans dossier multi-dialectes, il manquera les collisions hors de son silo ; (ii) **coût de confidentialité** si les cibles du programme défensif ne peuvent être divulguées à l'extérieur (**je ne sais pas** quelle est la contrainte de confidentialité du programme).
4. **Exécution externe sur bancs publics d'étalons** (pour la forme *objet à score exact*) : confrontation directe du score aux implémentations de référence publiées sur les mêmes instances `[VÉRIFIÉ]`.

---

## VI. Livrables Tour III.1 (b) et (c) — Expériences décisives et mesures minimales des instruments

### (b) Trois expériences décisives en inférence forte (Règle B4)

Chaque expérience oppose deux hypothèses mutuellement exclusives sur un lot pilote avant généralisation :

* **Expérience E1 — Arbitrage temporel : filtrage avant scellement contre attente de la première revendication (Option b)**
  * **$H_A$ (Attraction précoce vers le connu)** : Parmi un lot pilote de cibles candidates non filtrées soumises aux agents, la proportion de cibles donnant lieu aux premières revendications qui s'avèrent en collision (dans la littérature, incluant la pile 2026 non lue, ou par réduction courte aux lemmes de la bibliothèque Lean publique) dépasse strictement le seuil économique de rentabilité $\tau^* = \frac{c_{\text{criblage}}}{B_{\text{cible}} + c_{\text{collision}}}$, où $c_{\text{criblage}}$ est le coût d'audit pré-scellement d'une cible, $B_{\text{cible}}$ le budget par cible et $c_{\text{collision}}$ le surcoût d'une collision tardive.
  * **$H_B$ (Rareté des collisions précoces — soutien à l'Option b)** : Cette proportion est inférieure ou égale à $\tau^*$ (à titre d'étalon opératoire si les coûts comptables ne sont pas encore arrêtés : $\le 10\%$ `(illustratif)` des premières revendications et $0$ `(illustratif)` collision directe dans la pile de 2026 déjà croisée).
  * **Métrique** : Taux de collisions certifiées (article explicite ou preuve de réduction validée par le lecteur humain) sur les premières revendications du pilote, et coût réel mesuré $c_{\text{criblage}}$.
  * **Contrôle négatif** : Insertion à l'aveugle dans le lot pilote de *témoins positifs déguisés* (théorèmes connus réécrits en jargon de contrôle IA, p. ex. borne de Bretagnolle–Huber reformulée en indétectabilité d'agent) et de *témoins mutés réellement neufs* (hypothèse modifiée changeant la constante minimax sur alphabet binaire, `[VÉRIFIÉ]` par LP). Si le pipeline d'audit manque un seul témoin positif déguisé (rappel $< 100\%$ `(illustratif)` sur témoins), l'instrument est invalidé avant toute conclusion.
  * **Issues falsifiantes** : Un taux observé $> \tau^*$ (ou une collision dès la lecture de la pile 2026 à coût de recherche nul) **falsifie $H_B$** et élimine l'Option (b). Un taux $\le \tau^*$ sous contrôle négatif valide **falsifie $H_A$**.

* **Expérience E2 — Étendue et granularité : empreintage *a priori* des cinq zones (Option a) contre recherche multi-dialectes centrée sur l'énoncé candidat**
  * **$H_A$ (Perméabilité inter-dialectes et perte d'information de l'empreinte *a priori*)** : Sur un banc d'énoncés-cibles ayant une antériorité réelle répartie entre les cinq zones et leurs disciplines jumelles (actuariat, audit économique, théorie de l'information), la recherche requêtée *à partir de l'énoncé précis* (avec traduction multi-dialectes et invariants petits-cas) obtient un rappel strictement supérieur à l'interrogation d'un index d'empreintes construit *a priori* sur les cinq zones ($\Delta R = R_{\text{énoncé}} - R_{\text{5\_zones}} > 0$, seuil pratique $\Delta R \ge 15$ points de pourcentage `(illustratif)`), pour un coût de calcul par cible retenue inférieur ou égal.
  * **$H_B$ (Suffisance de l'index *a priori* des cinq zones — soutien à l'Option a)** : $\Delta R \le 0$ (ou $< 15$ points `(illustratif)`) ou l'index *a priori* domine en coût amorti sur la taille réelle de la liste fermée.
  * **Contrôle négatif** : Sous-lot de collisions publiées *explicitement* dans les revues statistiques centrales avec le vocabulaire exact des cinq zones ; les deux méthodes doivent y atteindre un rappel $\ge 90\%$ `(illustratif)`, faute de quoi l'extracteur d'empreintes est lui-même défectueux.
  * **Issues falsifiantes** : $\Delta R \ge 15$ points `(illustratif)` à coût moindre ou égal **falsifie $H_B$** (réfute le pré-empreintage par zones avant formulation des cibles). L'issue inverse **falsifie $H_A$**.

* **Expérience E3 — Uniformité sur tout le pilier (Option c) contre stratification par les trois formes de cibles**
  * **$H_A$ (Rendement net négatif de la lecture large d'articles sur les Formes 1 et 2)** : Pour les *lemmes de bibliothèque* et les *objets à score exact*, une fois exécutées leurs vérifications mécaniques natives (scan Lean/PR pour les lemmes ; évaluation d'étalons classiques + LP petits cas pour les objets à score), l'ajout d'une recherche bibliographique large d'articles produit un gain d'évitement de collision strictement inférieur à son coût additionnel ($\text{gain net} < 0$).
  * **$H_B$ (Rentabilité uniforme sur tout le pilier — soutien à l'Option c)** : La lecture large d'articles dégage un $\text{gain net} \ge 0$ sur *chacune* des trois formes séparément.
  * **Contrôle négatif** : Énoncés de Forme 3 (*démontrer ou réfuter*) inclus en parallèle comme témoin de sensibilité où la recherche d'articles doit afficher un gain net positif.
  * **Issues falsifiantes** : Un gain net $< 0$ sur les lemmes ou les objets à score **falsifie $H_B$** (réfute l'Option c uniforme). Un gain net $\ge 0$ sur chacune des trois formes **falsifie $H_A$**.

### (c) Mesure minimale de fonctionnement de chaque instrument nommé dans la question

Pour éviter l'illusion de performance sur des paires faciles, **tous les instruments sont évalués sur des « quasi-jumeaux honnêtes appariés »** *(notre proposition)* : chaque collision vraie (énoncé existant renommé ou transposé d'un domaine jumeau) est appariée à un énoncé réellement neuf partageant exactement le même vocabulaire ambiant, mais dont une hypothèse structurelle modifiée (p. ex. passage d'observations échangeables à un nul non stationnaire adaptatif) change la valeur minimax vérifiée sur petit alphabet fini `[VÉRIFIÉ]`.

| Instrument nommé | Métriques minimales (sur jumeaux appariés) | Cas honnêtes appariés spécifiques | Vérification mécanique à battre (à taux de fausses alertes $\le$) |
| :--- | :--- | :--- | :--- |
| **1. Agent de lecture et d'empreintage d'articles** | Taux de détection $R$ des collisions (dont corollaires implicites) ; taux de fausses alertes $\text{FPR}$ sur jumeaux à hypothèse altérée. | Théorème publié avec hypothèse globale de section vs cible levant cette hypothèse ; fusion d'e-valeurs vs borne de copule actuarielle. | Recherche `BM25` sur sources `.tex` + normalisation d'équations + voisinage de citations à $2$ sauts `(illustratif)` sans lecture par agent. |
| **2. Bases d'articles (moteur de récupération)** | `Rappel@K` (p. ex. $K=25$ `(illustratif)`) sur collisions inter-domaines ; $\text{FPR}$ (bruit hors-sujet retenu). | Paires cross-domaines (audit économique $\leftrightarrow$ jeu d'inspection ; `cs.IT` $\leftrightarrow$ frontières de détection) contre quasi-homonymes non pertinents. | Requête booléenne restreinte aux mots-clés littéraux des cinq zones et aux citations directes de Fano, Bretagnolle–Huber et Wald. |
| **3. Bibliothèques formelles & recherche formelle d'énoncés** | $R$ sur lemmes déjà formalisés sous un autre type/nom ; $\text{FPR}$ (lemmes syntaxiquement voisins mais logiquement plus faibles). | Même lemme codé sur `PMF` finie vs `Measure` générale vs lemme manquant d'une hypothèse d'intégrabilité. | Tactiques Lean natives seules (`exact?`, `apply?`, `#find`) et recherche par expressions régulières sur les identifiants du dépôt. |
| **4. Listes de problèmes ouverts & notices de bancs** | $R$ sur conjectures déjà répertoriées ou scores déjà battus par un étalon ; $\text{FPR}$ sur variantes contraintes inédites. | Problème ouvert COLT vs variante à budget dur modifiant le régime ; banc de score vs étalon classique optimisé par grille. | Correspondance exacte de chaînes sur archives PMLR et exécution d'un script fixe d'étalons classiques (CUSUM, Wald, moyenne d'e-valeurs). |
| **5. Mainteneurs de bibliothèques** | $R$ sur doublons conceptuels ou PR concurrentes en cours ; $\text{FPR}$ (rejet à tort d'un lemme réellement absent). | Lemme de statistique subsumé par un lemme abstrait de `mathlib4` vs lemme de pont réellement manquant dans l'API publique. | Script automatisé inspectant `git log`, l'AST de `HEAD` et le texte de toutes les *pull requests* et branches publiques ouvertes. |
| **6. Relecteur du domaine (& juge de nouveauté)** | $R$ sur folklore et collisions inter-silos ; $\text{FPR}$ (déclarer « trivial/connu » un énoncé dont la preuve échoue sur le cas muté). | Folklore classique déguisé vs énoncé jumeau où l'argument standard échoue sur contre-exemple fini caché au relecteur. | Pipeline automatisé complet (récupération multi-dialectes + hachage LP petits cas + réduction assistée par prouveur) évalué seul à l'aveugle. |

---

## VII. Question 5 — Reformulation de la demande

La question initiale suppose un choix binaire de calendrier et un traitement uniforme du pilier. En tenant compte de l'objectif défensif `[RAPPORTÉ]`, de l'hétérogénéité des trois formes de cibles `[RAPPORTÉ]` et de la perméabilité disciplinaire `[VÉRIFIÉ]`, la vraie question décisionnelle est :

> **« Quelle cascade de filtres d'antériorité — différenciée selon chacune des trois formes de cibles (lemme Lean, objet à score exact, énoncé ouvert) et déclenchée par lots glissants au scellement de chaque cible candidate — minimise la somme du coût d'audit, du délai de lancement des pilotes et des collisions post-dépense, tout en convertissant immédiatement en outils de contrôle IA les résultats existants découverts en chemin ? »**

---

## VIII. Question 6 & Livrable (d) — Recommandation, coûts, hypothèses, bascules et ancrage matériel

### 1. Recommandation : Option (d) — Entonnoir stratifié par forme de cible, par lots glissants au scellement

Nous rejetons **(a)** (paralyse le démarrage des pilotes et manque les collisions hors des mots-clés des cinq zones), **(b)** (expose la liste fermée à brûler son budget sur des résultats déjà publiés ou mémorisés par les LLM) et **(c)** (gaspille de la lecture d'articles sur des lemmes Lean et des objets à score exact). Nous recommandons une **Option (d)** en trois temps :

* **Temps 0 — Déblaiement immédiat sans retarder les pilotes ($24\text{ à }48\text{ h}$ `(illustratif)`)** :
  1. Lire et empreinter **uniquement** les travaux de 2026 déjà croisés par hasard (`[RAPPORTÉ]` / `[OBSERVÉ-NON-AUDITÉ]`).
  2. Extraire automatiquement l'index des théorèmes et PR ouvertes de la bibliothèque Lean publique `[RAPPORTÉ]` et de `mathlib4`.
* **Temps 1 — Porte de scellement par lots glissants, stratifiée selon les trois formes** *(dès qu'un micro-lot de $5\text{ à }10$ `(illustratif)` cibles est prêt, les pilotes démarrent sans attendre le reste de la liste)* :
  * *Forme « Lemme de bibliothèque »* : **aucune lecture large d'articles**. Recherche formelle Lean + scan des PR + validation rapide mainteneur. *(Ajustement incitatif proposé : regrouper les lemmes en lots plutôt que les payer au même budget unitaire qu'un théorème ouvert).*
  * *Forme « Objet à score exact »* : **aucune lecture large d'articles**. Exécution obligatoire d'étalons classiques + solveur LP/DP sur petites instances pour fixer le score de référence, complétée d'une vérification ciblée des notices de bancs.
  * *Forme « Énoncé à démontrer ou réfuter »* : **audit profond centré sur l'énoncé précis avant scellement** : (i) test de réfutation/trivialisation LP sur petits alphabets et sonde de récitation LLM ; (ii) traduction dans les dialectes jumeaux (actuariat, audit économique, théorie de l'information, martingales) ; (iii) récupération hybride + graphe de citations à $2$ sauts `(illustratif)` et lecture/empreintage canonique des seuls $20\text{ à }30$ `(illustratif)` articles les plus proches + tentative de réduction déductive ; (iv) visa court du lecteur humain sur ce dossier pré-filtré. Si une preuve existe déjà et sert le contrôle IA, le résultat est **importé** à coût réduit et la cible retirée de la liste payante.
* **Temps 2 — Audit différentiel à chaque revendication de nouveauté** : nouvelle requête ciblée sur **le lemme clé ou l'invariant de la construction découverte par l'agent** (souvent plus révélateur de l'antériorité que l'énoncé initial `[HYPOTHÈSE]`), puis passage au juge de nouveauté et au lecteur humain `[RAPPORTÉ]`.

### 2. Ce que l'Option (d) suppose et ce qui la ferait changer

* **Hypothèses de validité** `[HYPOTHÈSE]` : (i) la liste fermée peut être scellée par tranches successives plutôt qu'en un bloc figé au jour initial ; (ii) le nombre d'énoncés théoriques candidats (Forme 3) reste suffisamment modéré pour que $N_{\text{cibles}} \times \text{coût(requête par énoncé)} < \text{coût(indexation exhaustive de 5 zones + jumeaux)}$ ; (iii) le hachage sur petites instances et la traduction multi-dialectes capturent les collisions trans-domaines.
* **Critères réfutables de bascule** :
  * *Bascule vers **(a) élargie aux dialectes jumeaux*** si l'institution impose de sceller d'un seul bloc initial un très grand nombre d'énoncés de Forme 3 (p. ex. $> 60$ `(illustratif)` énoncés couplés) **et** que l'Expérience E2 falsifie $H_A$ ($\Delta R \le 0$).
  * *Bascule vers **(b)*** uniquement si le coût de calcul d'un pilote par cible devient négligeable devant un audit d'énoncé ($B_{\text{cible}} \ll c_{\text{criblage}}$) **et** que l'Expérience E1 falsifie $H_A$ (taux de collision précoce $\le \tau^*$, zéro collision dans la pile 2026).
  * *Bascule vers **(c)*** uniquement si l'Expérience E3 falsifie $H_A$ (gain net positif de la lecture d'articles même sur les lemmes Lean et les objets à score exact).

### 3. Livrable Tour III.1 (d) — Ancrage matériel, modèles ouverts et coût estimé

**Je ne sais pas** quel est le volume exact de la liste fermée ni les coûts internes du programme ; tous les chiffres matériels ci-dessous sont donc marqués `(illustratif)`.

* **Pile logicielle et modèles ouverts (exécutables sur site sans fuite de cibles défensives)** :
  * *Ingestion mathématique* : parseur direct des sources `.tex` arXiv ; `Nougat` ou `Marker` (références à vérifier) uniquement en repli sur PDF sans source.
  * *Récupération et reclassement* : plongements ouverts `BAAI/bge-m3` ou `allenai/specter2` + reclasseur croisé `BAAI/bge-reranker-v2-m3` (numéros de version `(illustratif)`).
  * *Agent de traduction multi-dialectes et d'empreintage typé* : modèle ouvert à poids publics en raisonnement mathématique long contexte, type `Qwen2.5-Math-72B-Instruct` ou `DeepSeek-R1-Distill-Qwen-32B` (tailles `(illustratif)`).
  * *Vérification formelle et calcul petits cas* : `Lean 4` `(illustratif)` + index local `Loogle` / `LeanSearch` sur `mathlib4` et la bibliothèque statistique publique + prouveur ouvert type `DeepSeek-Prover-V1.5-7B` `(illustratif)` ; solveurs ouverts `Z3` (SMT) et `HiGHS` / `SCS` (LP/SDP).
* **Calcul et coût estimé `(illustratif)`** :
  * *Infrastructure* : $1$ `(illustratif)` serveur local doté de $2\text{ à }4$ `(illustratif)` GPU de $80\text{ Go}$ `(illustratif)` de VRAM et $64$ `(illustratif)` cœurs CPU pour la compilation Lean parallèle.
  * *Coût sous Option (d) par cible candidate de Forme 3* : expansion multi-dialectes + lecture intégrale et empreintage canonique de $25$ `(illustratif)` articles complets ($\approx 500\text{k}$ `(illustratif)` jetons en entrée, $\approx 60\text{k}$ `(illustratif)` en sortie) + solveur petits cas + tentatives de réduction Lean $\approx 20\text{ à }45$ `(illustratif)` minutes-GPU ($\approx 1\text{ à }4\text{ €}$ `(illustratif)` de calcul électrique/infonuagique par cible), suivies de $20\text{ à }30$ `(illustratif)` minutes du lecteur humain sur un dossier condensé. Les Formes 1 et 2 ne consomment que quelques minutes-CPU `(illustratif)` par cible.
  * *Contraste avec l'Option (a) ou (c)* : empreinter finement en amont $3\,000$ `(illustratif)` articles couvrant les cinq zones et leurs jumeaux exigerait $\approx 80\text{ à }150$ `(illustratif)` millions de jetons ($\approx 80\text{ à }200$ `(illustratif)` heures-GPU) et plusieurs semaines `(illustratif)` de latence initiale avant le moindre essai pilote, principalement sur des sous-domaines qu'aucune cible scellée n'interrogera.

FIN-DE-CELLULE