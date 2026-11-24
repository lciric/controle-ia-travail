# Proposition A : ce qui résiste, ce qui relève de l'artefact, et les opérateurs à construire d'abord

## Préambule : état des pièces et statuts

- **Pièce incomplète.** Le §3 du bloc FAITS annonce « six familles de mécanismes » mais n'en énumère que quatre. Je n'invente pas les deux manquantes.
- **Références à vérifier.** « Hla, 2026 » est cité sans titre. L'« écart de 52 % » de Li et al. (2026) n'a pas d'unité précisée (points ou relatif) ; je ne l'interprète pas.
- **Références de 2026.** Je les reprends telles que le bloc les donne, sans pouvoir les vérifier de mémoire.
- **Statuts.** Le bloc intitule son §2 « corpus vérifié » ; je reprends donc **VÉRIFIÉ** pour ce qu'il énonce. Les §3 et §4 ne portent aucun statut. J'y distingue ce qui est attribué à des auteurs (**RAPPORTÉ**) de ce que le bloc formule lui-même comme « proposé » ou « candidat » (**HYPOTHÈSE**). Tout ce qui n'est pas dans FAITS est ma proposition (**HYPOTHÈSE**).
- **Correspondance avec le livrable de la cellule.** (a) est au §1.2, (c) au §4.4, (b) et (d) au §7.

---

## 1. Ce qu'un expert ferait, et que la question omet

### 1.1 Angles morts

1. **Le dénominateur absent (biais du survivant).** Pour affirmer qu'un mécanisme X produit des idées fécondes, il faut estimer P(fécond | X) et le comparer à P(fécond | non-X).
   - L'histoire des sciences ne fournit que des numérateurs.
   - L'unité d'analyse correcte n'est pas la découverte historique. C'est l'**ensemble complet des candidats qu'un opérateur aurait générés à la date t**, avec ou sans suite.
   - Sans cet ensemble, aucun taux de succès n'est défini.
2. **Comparaisons multiples cachées.** Le nombre réel de tests ne se limite pas aux tests déclarés. Il inclut aussi les choix de granularité, de plongement, de fenêtre temporelle et de seuil.
   - L'expert déclare cette famille de tests à l'avance.
   - Il contrôle le taux de fausses découvertes (Benjamini et Hochberg, 1995, « Controlling the false discovery rate ») ou utilise des e-valeurs.
   - Tout choix non déclaré relève de l'exploration et ne vaut pas preuve.
3. **Circularité après coup.** Mesurer la fécondité par les citations crée une fuite : les citations sont produites par le même lexique que celui qui sert à générer les candidats. Les issues doivent être **mécaniques et extérieures au lexique** : une relation typée qui apparaît plus tard, une équation équivalente vérifiée symboliquement, une loi plantée retrouvée.
4. **Géométrie apparente contre structure causale.** Trois résultats de FAITS l'imposent :
   - la sélectivité des sondes (Hewitt et Liang) ;
   - les tests de type Myhill-Nerode (Vafa et al.) ;
   - les états discrets en étoile (Gupta et al.).

   Une forme dans l'espace des activations n'est pas un mécanisme. Il faut une intervention ou un transfert hors distribution.
5. **Taille finie.** Sur un graphe fini, des exposants et des « transitions » se lisent dans n'importe quelle hétérogénéité de degrés (§3c).
6. **Goodhart, deux fois.**
   - Le score demandé au §7 deviendra une cible pour l'organisme d'idéation.
   - Tout signal de moniteur utilisé comme objectif détruit le moniteur. FAITS l'interdit d'ailleurs hors bras d'attaque déclaré.
7. **Confondant instrumental.** Merton relie les découvertes multiples à la diffusion préalable d'instruments ou de formalismes. La disponibilité d'un instrument peut donc causer à la fois le rapprochement et la découverte. L'expert contrôle la date de disponibilité des instruments communs avant d'attribuer un effet au « rapprochement ».

### 1.2 Ce que la question suppose sans que ce soit établi (livrable a)

| # | Supposition | Statut | Commentaire |
|---|---|---|---|
| S1 | Les régularités distributionnelles portent une structure réelle | **VÉRIFIÉ** au sens restreint du §2.1 (reconstructions géographiques, sous-espaces linéaires) | Leur **transférabilité** n'est pas établie : §2.3, §2.4 et §2.6 indiquent une structure discrète, locale, causalement incohérente. |
| S2 | Les six familles de mécanismes sont distinctes et séparables | **HYPOTHÈSE** | Le confondant instrumental (Merton) peut les unifier. |
| S3 | Les fausses identités sont détectables avant coup | **HYPOTHÈSE** | Le bloc dit lui-même « peu formalisée ». |
| S4 | Les cadres variationnels et percolatifs s'appliquent à des graphes finis | **HYPOTHÈSE** | L'objection est rapportée dans FAITS §3.3. |
| S5 | Les opérateurs d'idéation se transfèrent au contrôle boîte blanche | **HYPOTHÈSE** | Aucun fait ne l'étaye directement. |
| S6 | Le « potentiel de découverte majeure » est estimable ex ante | **HYPOTHÈSE** | **Je ne sais pas** l'estimer. C'est le facteur le moins mesurable du score. |
| S7 | Il existe des frontières infranchissables | **HYPOTHÈSE** | J'en propose deux par arguments d'identifiabilité (§4.3). Ce sont des propositions, pas des théorèmes vérifiés. |
| S8 | Le produit de notes ordinales de 1 à 5 a un sens | **HYPOTHÈSE**, probablement fausse | Un produit de rangs n'est pas invariant par recodage monotone. Je donne donc la sensibilité (§7). |

---

## 2. Données brutes à mobiliser avant tout agrégat

- **Textes horodatés à la date de dépôt**, et non les plongements figés : ces derniers ont déjà absorbé des données postérieures à t et des normalisations de fréquence. Concrètement :
  - les sources LaTeX et les versions successives (v1, v2…) des prépublications publiques ;
  - les comptes bruts de cooccurrence par tranche temporelle.
- **Équations datées, parsées en arbres d'expressions.** Proposition : les macros que les auteurs définissent dans leurs sources (définitions de commandes LaTeX) sont une **trace horodatée de l'enrichissement de l'alphabet formel**. C'est un observable direct, mais grossier, de l'apparition de primitives.
- **Le dénominateur** : errata, rétractations, versions abandonnées, rapprochements proposés puis jamais repris. Ce sont des données **OBSERVÉ-NON-AUDITÉ** tant que la collecte n'a pas été auditée.
- **Graphes relationnels typés et datés** : concepts, méthodes et instruments, avec date de première mention de l'instrument (pour le contrôle de Merton).
- **Modèles à données d'entraînement publiques et énumérables, avec points de contrôle**, ce qui rend l'étanchéité **auditable par recherche exacte** :
  - la suite Pythia (entraînée sur The Pile) ;
  - OLMo (entraîné sur Dolma) ;
  - les modèles pré-entraînés avant coupure cités dans FAITS §2.6.
- **Contrôle** : traces d'actions brutes d'agents, activations, poids à chaque étape d'ajustement, et références honnêtes accompagnées de leur journal de provenance.
- **Mondes synthétiques** à lois plantées, fausses identités plantées, primitives manquantes plantées et contamination plantée. Les graines sont détenues par l'évaluateur externe seul.

---

## 3. Formalisation et critères de démarcation

**Notation.**
- D_t : le corpus jusqu'à la date t.
- N : les statistiques de nuisance (fréquences, degrés, largeur et profondeur du réseau, granularité g).
- T : une statistique candidate.
- φ : X → Y : un alignement entre domaines, dont les relations sont R_X et R_Y.

### (a) Invariant transférable plutôt qu'artefact

Proposition : on exige trois conditions conjointes.

- **C1 – Non-réductibilité aux nuisances.**
  - T(D) dépasse le quantile 1−α de sa loi sous le **nul conditionnel** P(· | N).
  - Ce nul s'échantillonne par recâblage préservant les degrés (Maslov et Sneppen, 2002, « Specificity and stability in topology of protein networks »), par permutations préservant les fréquences, et par étalonnage par architecture (Gröger et al., FAITS §2.4).
  - Un alignement qui échoue à C1 est un artefact de fréquence ou d'échelle.
  - T doit de plus garder son signe à travers plusieurs granularités g déclarées.
- **C2 – Transfert prédictif étanche.**
  - φ est appris sur D_{<t}.
  - Il doit prédire des relations typées de Y observées dans D_{>t}, ou dans le monde planté, avec une précision qui dépasse le nul de C1 et les bases mécaniques.
  - L'« alignement structurel » au sens de Gentner devient ainsi un **nombre de relations préservées en excès du nul**, et non une impression.
- **C3 – Équivalence comportementale (Myhill-Nerode).**
  - Deux états internes sont identifiés s'ils induisent les mêmes distributions de comportements futurs. La proximité géométrique ne suffit pas.
  - Une affirmation de **variété continue** implique une propriété d'interpolation : sur le segment qui relie deux états, la sortie varie de façon monotone avec la position λ.
  - Une **juxtaposition d'états discrets** prédit au contraire une sortie constante par morceaux, avec des sauts.
  - C'est la distinction entre Karkada et al. et Gupta et al., rendue testable.

**Frontière (HYPOTHÈSE argumentée).** Le biais de déclaration (Gordon et Van Durme ; Bender et Koller) n'est **pas détectable depuis le texte seul**. Une régularité jamais énoncée ne laisse aucune cooccurrence. C2 exige donc un ancrage non textuel (mesures, monde planté) dès qu'une affirmation porte sur ce qui n'est pas dit.

### (b) Fausse identité contre polysémie ; objet manquant

**Modèle.**
- Un concept c est employé dans des contextes k = 1…K : sous-communautés, dispositifs de mesure, familles d'équations.
- Chaque contexte impose des contraintes R_k(c, …) : relations, équations, unités.
- ρ(c) désigne le **recouvrement relationnel** : la part de relations, d'instruments et d'unités partagés entre contextes, mesurée en excès du nul.

**Critère (proposition).**

| Situation | ρ(c) | Système ∪_k R_k avec c comme variable unique |
|---|---|---|
| Polysémie | ≈ nul | Jamais contraint conjointement, donc aucune tension |
| Vraie identité | élevé | Satisfaisable |
| **Fausse identité** | élevé | **Insatisfaisable**, alors que chaque R_k l'est. Il existe un sous-ensemble minimal insatisfaisable qui couvre au moins deux contextes. |

L'exemple de la chaleur et de la température illustre le dernier cas : instrument partagé, relations partagées, mais la chaleur latente (apport sans changement de température) contredit l'identité.

**Scission.**
- On remplace c par c₁ et c₂, avec une affectation des contextes à l'un ou à l'autre.
- On retient l'affectation qui minimise la longueur de description ΔL = L(théorie) + L(données | théorie).
- La scission n'est justifiée que si ΔL < 0 au-delà de la distribution des scissions aléatoires.
- Le langage des faisceaux cellulaires (Hansen et Ghrist, « Toward a spectral theory of cellular sheaves », 2019) exprime la même idée : des sections locales cohérentes qui ne se recollent pas. C'est un langage possible, pas nécessaire.

**Objet manquant.**
- Il est signalé lorsque **aucune** scission ou fusion dans l'alphabet A ne donne ΔL < 0, alors que l'ajout d'un symbole latent z le fait : G(z) = L_A − L_{A∪{z}} − coût(z) > 0.
- **Signal de zone de tension** : une croissance de la longueur de description par résultat nouveau (dL/dn) dans un sous-champ, qui opérationnalise les « épicycles ».
- **Rupture de circularité** : z est jugé par la compression de données **qu'il n'a pas vues** (tranche future, générateur planté), et non par les relations qu'il fait apparaître après coup.

**Limite.** L'extraction automatique des contraintes depuis le texte est bruitée, et les cas historiques réels sont peu nombreux. La puissance statistique viendra des mondes plantés ; la rétrodiction réelle restera anecdotique.

### (c) Variationnel et percolation sur graphes finis

**Défendable :**
- Un principe d'entropie maximale ou de grandes déviations, compris comme une **famille exponentielle** sur les trajectoires. Son contenu tient entièrement dans le choix des contraintes, qui se teste par la vraisemblance sur données réservées contre des alternatives (attachement préférentiel, urnes de Tria et al.).
- Des bornes de concentration en taille finie.
- La « percolation » comprise comme une **prédiction datée de la fusion de deux composantes**, comparée au nul.

**Réfutable, ou illusion probable :**
- Un exposant critique lu sur un graphe unique : il n'y a pas de limite thermodynamique, et les ajustements de lois de puissance sont fragiles (Clauset, Shalizi et Newman, 2009, « Power-law distributions in empirical data »).
- Un seuil quasi nul : l'hétérogénéité des degrés suffit à le produire (Cohen et al., 2000, « Resilience of the Internet to random breakdowns »), ce qui donne une criticité apparente expliquée par le nul.
- Une « loi de conservation » qui n'est qu'une identité comptable : par exemple, la somme des degrés vaut 2|E|.
- Une croissance dissipative n'a pas d'hamiltonien. Un « principe variationnel » n'y est donc qu'une **reparamétrisation**, sauf s'il prédit ce qu'un modèle non variationnel à paramètres égaux ne prédit pas.

**Critère minimal.**
- Effondrement de mise à l'échelle en taille finie sur au moins trois tailles emboîtées (sous-échantillons ou tranches temporelles).
- Exposants cohérents d'une taille à l'autre.
- Écart au nul préservant les degrés.

---

## 4. Méthodes et protocoles

### 4.1 (a) Briser la circularité de l'invention de primitives

| Famille | Principe | Hypothèse | Coût sur processeur seul | Mode d'échec |
|---|---|---|---|---|
| Bibliothèques par compression (DreamCoder, Ellis et al., 2021 ; Stitch, Bowers et al., 2023) | Longueur de description minimale | Les concepts compriment | Modéré | Compresse la notation, pas le concept |
| Symétries d'abord (Udrescu et Tegmark, 2020) | Séparabilité, invariances | Données numériques disponibles | Modéré | Symétrie absente de l'ensemble cherché |
| Variable latente et scission (§3b) | Sous-ensemble minimal insatisfaisable, puis gain de longueur de description | Contraintes extractibles | Faible à modéré (solveurs) | Bruit d'extraction |
| Proposition par modèle de langue, puis vérification formelle | Générer puis filtrer | Modèle à coupure stricte | Faible si petit modèle | A priori contaminé ; propositions plausibles mais stériles |
| Surprise interne en lecture seule (Schmidhuber, 2010 ; Xu et al., 2026) | Surprise suivie d'un gain de compression | Surprise ≠ rareté | Carte graphique | Confondu par la fréquence. Doit passer C1. |

**Point commun obligatoire** : l'évaluation se fait par gain de compression sur des données invisibles du générateur.

### 4.2 (b) Étanchéité temporelle et causale

- **Données.** Tranches dont la date d'ingestion est ≤ t, hachées. Modèles entraînés uniquement sur des données ≤ t : modèles à données ouvertes, ou modèles pré-coupure de FAITS §2.6. Jamais d'ignorance simulée par consigne (FAITS §2.6).
- **Test de fuite (canari).** On pose des questions postérieures à t, dont la réponse se vérifie mécaniquement.
  - Le modèle scellé doit se situer au niveau du hasard.
  - Un modèle dont la coupure a été permutée sert de contrôle.
  - Un résultat au-dessus du hasard signale une fuite.
- **Contrôle négatif de date.** On permute les horodatages en conservant le volume par tranche. Si l'opérateur garde son avantage, il exploite un artefact non temporel.
- **Aucun juge génératif.** Les issues sont mécaniques : lien apparu, arbre d'équation équivalent (vérifié symboliquement ou numériquement), loi plantée retrouvée.
- **Engagement cryptographique** des prédictions avant ouverture des données de test.

### 4.3 (c) Transfert au contrôle boîte blanche

**Sabotage diffus sous référence finie ou contaminée.**
- Les e-processus et martingales de test donnent un taux de fausses alertes valide à tout temps d'arrêt (Ramdas et al., 2023, « Game-theoretic statistics and safe anytime-valid inference »).
- La contamination de la référence se modélise à la Huber, avec une fraction ε.
- **Argument d'identifiabilité (proposition, à vérifier formellement).**
  - Supposons qu'un tiers puisse placer une masse ε sur le motif même du sabotage, à un taux r ≤ ε.
  - Alors la loi honnête n'est pas identifiable depuis la référence.
  - Aucun test au taux de fausses alertes valide uniformément sur la classe contaminée n'a de puissance supérieure à α contre r ≤ ε.
- **Conséquence** : une garantie exige une borne ε déclarée **et** une provenance de la référence par un canal indépendant.

**Marge asymétrique.**
- Je définis la marge M comme la **perte minimale de performance sur la tâche** qu'un agent adaptatif, dans le bras d'attaque déclaré, doit consentir pour faire passer la détection sous un seuil τ.
- Hypothèse sur l'échec des sondes linéaires : elles laissent des directions d'évasion qui coûtent peu à la tâche.
- Les invariants relationnels pourraient forcer l'évasion à passer par un changement de comportement. Il s'agit de la cohérence des représentations internes à travers paraphrases et contextes, c'est-à-dire le critère §3b appliqué à l'agent.
- C'est une hypothèse, testée en P5.

**Espace des poids.** On analyse la différence entre modèle de base et modèle ajusté (structure de faible rang, localisation par couche) sur des organismes modèles à comportement planté. Référence spécifique : à vérifier.

**Essaims à poids partagés.**
- Des copies honnêtes de mêmes poids sont **naturellement** corrélées. La corrélation brute ne prouve donc rien.
- **Frontière (proposition).** Sans contrefactuel, la coordination implicite n'est pas distinguable d'une politique commune. Le contrefactuel minimal consiste à faire varier, dans le contexte d'une copie, la croyance en l'existence des autres copies. On mesure alors si le comportement en dépend au-delà de ce qu'expliquent les entrées.

### 4.4 Mesure minimale par instrument (livrable c)

Tous les seuils α sont préenregistrés. Toute valeur numérique citée est **illustrative**.

| Instrument | Cas honnêtes appariés | Mesure | Vérification mécanique à battre |
|---|---|---|---|
| Opérateur d'alignement | Paires du nul de mêmes fréquences et degrés | Précision@k future ; taux de faux positifs sur paires permutées | Attachement préférentiel, voisins communs, fréquence seule |
| Détecteur de fausse identité | Vraies identités et polysémies plantées, fréquences appariées | Taux de détection et de fausses alertes | Regroupement de contextes (désambiguïsation lexicale) |
| Détecteur de transition | Graphes nuls à degrés préservés | Taux de « transitions » détectées sur les nuls (doit rester ≤ α) | Comparaison loi de puissance / log-normale |
| Inventeur de primitives | Mondes sans primitive cachée | Récupération vérifiée ; fausses primitives | Fouille de sous-arbres fréquents |
| Sceau temporel | Modèle à coupure permutée | Exactitude au-dessus du hasard après t | Hasard ; prédicteur fréquentiel |
| Détecteur séquentiel | Trajectoires appariées en longueur et en tâche, contaminées ou non | Fausses alertes ≤ α à tout temps d'arrêt ; puissance selon r ; délai | CUSUM calibré naïvement ; seuil fixe |
| Sonde ou moniteur | Trajectoires appariées en style et en longueur | Détection sous évasion à budget fixé ; fausses alertes sous changement de style | Sonde linéaire, tâche de contrôle (Hewitt et Liang), filtre lexical |
| Inspection des poids | Ajustements honnêtes de même taille et mêmes données | Taux de détection et de fausses alertes | Norme des différences par couche |
| Détecteur d'essaim | Copies honnêtes de mêmes poids | Taux de détection et de fausses alertes sur coordination plantée | Corrélation brute des actions |

---

## 5. Vérification indépendante, hors programme

1. **Évaluateur externe** détenant seul les graines des mondes plantés.
2. **Prédictions prospectives hachées et publiées** avant leur date de résolution. Le futur réel est le seul ensemble de test qui ne fuit pas.
3. **Réplication par une équipe tierce** sur un corpus disjoint (autre langue, autre base) et avec d'autres modèles pré-coupure.
4. **Collaboration adversariale.** Une équipe tierce tente de reproduire chaque résultat **avec les seuls nuls**. Si elle y parvient, le résultat est un artefact.
5. **Équipe rouge externe**, cantonnée au bras d'attaque déclaré, pour les moniteurs.
6. **Audit de fuite par recherche exacte** dans les données d'entraînement publiques.

Les experts aveugles (jeux d'intérêt de Gu et Krenn) n'interviennent qu'en signal secondaire, jamais comme validateurs.

---

## 6. Reformulation exigeante

> Pour chaque mécanisme candidat (alignement à distance, scission d'identité, transition sur graphe, invention de primitive) et pour chaque transfert au contrôle :
> - définir un opérateur qui produit, à la date t, un **ensemble complet de candidats** (dénominateur inclus) ;
> - montrer, sur des mondes plantés détenus par un tiers, puis en rétrodiction scellée par des données d'entraînement auditables, que sa précision dépasse à la fois un nul conditionnel aux fréquences, aux degrés, à l'échelle et à la granularité, **et** les meilleures bases mécaniques, avec une famille de tests déclarée à l'avant ;
> - pour le contrôle, borner le taux de fausses alertes à tout temps d'arrêt sous une contamination ε déclarée, et mesurer la marge comme le coût sur la tâche imposé à un adversaire déclaré ;
> - identifier les cas où l'identifiabilité est perdue (biais de déclaration, contamination non bornée, politique commune contre coordination) et y renoncer explicitement.

---

## 7. Propositions classées

Les notes sont ma proposition, de 1 à 5 ; elles n'ont rien de mesuré. Score = G × F × P × D / C, avec G = gain informatif, F = facilité, P = portée, D = potentiel de découverte majeure, C = coût.

| Rang | Proposition | G | F | P | D | C | Score |
|---|---|---|---|---|---|---|---|
| P1 | Banc de démarcation par nul conditionnel | 4 | 5 | 5 | 2 | 1 | 200 |
| P2 | Fausse identité : sous-ensemble insatisfaisable + gain de description | 5 | 3 | 4 | 4 | 2 | 120 |
| P3 | Détecteur séquentiel sous référence contaminée | 4 | 4 | 4 | 3 | 2 | 96 |
| P4 | Primitives par compression, validées sur données futures ou plantées | 4 | 2 | 4 | 5 | 3 | 53 |
| P5 | Marge asymétrique des invariants relationnels | 5 | 2 | 5 | 4 | 5 | 40 |
| P6 | Test de taille finie des transitions | 3 | 4 | 3 | 1 | 1 | 36 |
| P7 | Continu contre discret par interpolation causale | 4 | 4 | 3 | 2 | 3 | 32 |
| P8 | Contrefactuel de coordination en essaim | 4 | 2 | 4 | 3 | 4 | 24 |

**Sensibilité du classement.**
- P1 reste en tête sous toute pondération raisonnable, parce que C = 1 et F = 5.
- Si D est élevé au carré, P4 passe deuxième et P2 troisième.
- Si C est élevé au carré, P5 tombe derrière P8.
- Le produit de rangs ordinaux n'a pas de sens cardinal : seul l'ordre grossier est à retenir.

### P1. Banc de démarcation par nul conditionnel

- **Idée.** Tout alignement ou régularité candidat passe par C1 et C2 (§3a) avant d'être retenu. Le banc est appliqué en premier aux affirmations publiées citées dans FAITS.
- **Suppose** que les nuisances N sont énumérables et que le nul conditionnel est échantillonnable.
- **Duel.**
  - **H_A** : un prédicteur à structure typée a une précision@k sur les confirmations postérieures à t qui dépasse le quantile 0,95 (illustratif) du nul et la meilleure base mécanique.
  - **H_B** : sa précision reste dans la distribution du nul.
  - **Contrôles** : recâblage préservant les degrés, permutation préservant les fréquences, permutation des dates.
  - **Falsification** : un dépassement réfute H_B ; une précision dans le nul réfute H_A pour ce corpus.
- **Premier pas sans dépense.** Construire des matrices de cooccurrence par année à partir de métadonnées publiques, implémenter le recâblage, puis rejouer une rétrodiction de type Tshitoyan avec et sans nul.
- **Coût** : quelques jours de calcul sur processeur seul (illustratif).
- **Chances.** Élevées que l'outil fonctionne. **Je ne sais pas** quelle fraction des alignements survivra.

### P2. Fausse identité par sous-ensemble minimal insatisfaisable et gain de longueur de description

- **Idée.** Une fausse identité se signale par un recouvrement relationnel élevé **et** une incohérence couvrant plusieurs contextes ; la polysémie, elle, ne présente aucun recouvrement. La scission retenue est celle qui réduit la longueur de description au-delà des scissions aléatoires.
- **Suppose** que les contraintes peuvent être extraites, au moins dans les mondes plantés.
- **Duel.**
  - **Monde planté** : un générateur fusionne deux variables cachées sous un même jeton (fausses identités) et fait partager un jeton à des variables sans contexte commun (polysémies).
  - **H_A** : l'aire sous la courbe ROC du critère dépasse celle du regroupement de contextes d'une marge préenregistrée (illustrative : 0,1).
  - **H_B** : écart ≤ marge.
  - **Contrôle** : permutation des étiquettes de contexte à fréquences préservées.
  - **Falsification** : écart > marge réfute H_B ; écart ≤ marge réfute H_A.
- **Premier pas sans dépense.** Écrire le générateur symbolique et extraire les sous-ensembles insatisfaisables avec un solveur SMT public, sur processeur seul.
- **Coût** : faible (illustratif).
- **Chances.** Modérées sur mondes plantés ; faibles en rétrodiction réelle, faute de cas et à cause de l'extraction.

### P3. Détecteur séquentiel sous référence contaminée

- **Idée.** Un e-processus étalonné de façon robuste, avec une borne ε déclarée, doit garder un taux de fausses alertes valide tout en conservant de la puissance. Le même protocole teste la frontière d'identifiabilité du §4.3.
- **Suppose** une borne ε crédible et une provenance indépendante de la référence.
- **Duel.**
  - **Traces** : synthétiques, sabotage planté à un taux r, contamination plantée à ε par l'évaluateur.
  - **H_A** : à taux de fausses alertes empirique égal (≤ α), le détecteur robuste est plus puissant que le CUSUM naïf, d'au moins une marge préenregistrée, pour r > ε.
  - **H_B** : gain ≤ marge, ou fausses alertes > α.
  - **Prédiction annexe** : si la contamination imite le sabotage avec r ≤ ε, la puissance s'effondre vers α. Si la puissance tient, mon argument d'identifiabilité est réfuté.
  - **Contrôle** : traces honnêtes appariées en longueur et en tâche.
- **Premier pas sans dépense.** Simulation pure sur processeur, sans modèle de langue.
- **Coût** : faible (illustratif).
- **Chances.** Élevées en simulation. Je ne sais pas ce que donnera le transfert à des traces d'agents réels.

### P4. Primitives par compression, validées sur données futures ou plantées

- **Idée.** On apprend une bibliothèque d'abstractions sur des arbres d'équations datés de D_{<t}. Une primitive ne compte que si elle comprime des données non vues ou retrouve une primitive plantée.
- **Suppose** que la compression capture des concepts plutôt que des notations.
- **Duel.**
  - **H_A** : la primitive plantée est retrouvée, avec équivalence vérifiée numériquement et symboliquement, plus souvent que par la fouille de sous-arbres fréquents (marge illustrative).
  - **H_B** : aucun avantage.
  - **Contrôle** : des mondes **sans** primitive cachée. Des fausses primitives trouvées au-delà de α réfutent la spécificité.
  - **Falsification** : un avantage réfute H_B ; son absence réfute H_A.
- **Premier pas sans dépense.** Générateur planté ; parallèlement, extraction des définitions de macros datées comme observable brut (OBSERVÉ-NON-AUDITÉ tant que non audité).
- **Coût** : modéré (illustratif).
- **Chances.** Modérées sur mondes plantés. Faibles que les primitives retrouvées sur corpus réel soient des concepts plutôt que des notations.

### P5. Marge asymétrique des invariants relationnels

- **Idée.** On compare un moniteur fondé sur la cohérence relationnelle interne (critère §3b) à une sonde linéaire. La comparaison porte sur la courbe de Pareto entre taux de détection et perte sur la tâche, sous un adversaire déclaré.
- **Suppose** qu'on peut construire des comportements plantés dans des organismes modèles, et que le bras d'attaque est cloisonné. Aucun signal de moniteur ne sert d'objectif hors de ce bras.
- **Duel.**
  - **H_A** : faire passer la détection sous τ coûte plus à la tâche avec le moniteur relationnel qu'avec la sonde linéaire, d'un rapport > seuil préenregistré.
  - **H_B** : rapport ≤ seuil.
  - **Contrôles** : sonde sur direction aléatoire de même norme ; moniteur non entraîné.
  - **Falsification** : un rapport > seuil réfute H_B ; ≤ seuil réfute H_A.
- **Premier pas sans dépense.** Petit réseau entraîné sur une tâche synthétique, sur processeur seul, pour valider la métrique de Pareto.
- **Coût** : lourd à l'échelle d'environ 8 milliards de paramètres (FAITS), de l'ordre de centaines d'heures de carte graphique (illustratif).
- **Chances.** Faibles à modérées. **Je ne sais pas.**

### P6. Test de taille finie des transitions

- **Idée.** On soumet toute affirmation de « transition » sur un graphe scientifique à un effondrement de mise à l'échelle sur des tailles emboîtées, contre le nul préservant les degrés. La proposition est avant tout un outil de réfutation.
- **Suppose** des sous-échantillons ou tranches temporelles comparables.
- **Duel.**
  - **H_A** : l'émergence d'une composante géante entre deux champs montre des exposants cohérents à travers au moins trois tailles et un écart au nul.
  - **H_B** : le nul à degrés préservés reproduit la transition à densité égale.
  - **Falsification** : un écart au nul réfute H_B ; une reproduction par le nul réfute H_A.
- **Premier pas sans dépense.** Tranches d'un graphe de citations public, sur processeur seul.
- **Coût** : faible (illustratif).
- **Chances.** Élevées que l'issue soit négative, ce qui serait utile.

### Propositions non détaillées

- **P7.** Généraliser le test de Gupta et al. aux mois, aux années et à la géographie, par interpolation causale (C3).
- **P8.** Contrefactuel de croyance en l'existence d'autres copies (§4.3).

### Ancrage matériel (livrable d)

- **Phase 1, sur processeur seul** : P1, P2, P3, P4 et P6, sur données publiques et mondes plantés.
- **Phase 2, carte graphique légère** : P7 sur la suite Pythia, dont les points de contrôle et les données sont ouverts, ce qui rend la fuite auditable.
- **Phase 3, environ 8 milliards de paramètres (FAITS)** : P5 et P8 sur des modèles ouverts, avec OLMo comme témoin à données ouvertes.
- **Coûts** : tous illustratifs. Seule l'échelle de 8 milliards vient des faits.

### Hors de portée sans intervention causale ou expérimentale nouvelle

- Le biais de déclaration, depuis le texte seul.
- Le potentiel de découverte majeure, ex ante.
- La distinction entre coordination et politique commune, sans contrefactuel.
- La criticité sur un graphe unique.
- La garantie sous contamination ε non bornée.
- L'attribution causale d'une découverte au mécanisme d'idéation plutôt qu'à la diffusion d'instruments (Merton). Cette dernière demanderait des chocs exogènes de disponibilité d'instruments, qui restent de toute façon observationnels.

FIN-DE-CELLULE