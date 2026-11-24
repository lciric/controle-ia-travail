# Proposition A : Collisionneur 3×3, tour III.1 (à l'aveugle)

**Pièces et correspondance avec le livrable.**
- Le §3 des faits annonce « six familles de mécanismes » mais n'en liste que quatre. La pièce est visiblement coupée et je n'invente pas les deux familles manquantes.
- Les propositions B et C ne m'ont pas été transmises, puisque ce tour se joue à l'aveugle. Je ne formule donc aucune critique contre elles.
- Le bloc QUESTION fixe la forme en 7 points. Le livrable (a)–(d) y est intégré ainsi : (a) au point 1, (c) au point 4, (b) et (d) au point 7.

**Convention de statut.**
- Le dossier qualifie le corpus du §2 de « vérifié ». Je le note **VÉRIFIÉ (dossier §2)** sans l'avoir reproduit.
- Les énoncés du §3 sont posés comme candidats ou objections. Je les note **RAPPORTÉ (dossier §3)**.
- Tout ce qui est de moi est **HYPOTHÈSE**, autrement dit une proposition.
- Les titres sont donnés quand je suis sûr. Les identifiants arXiv sont seulement ceux du dossier, marqués « id. dossier ».

---

## 1. Analyse d'expert

### (a) Ce que la question suppose sans que ce soit établi

| # | Présupposé | Statut | Pourquoi c'est fragile |
|---|---|---|---|
| P1 | La « fécondité » d'une idée a une définition opérationnelle | Non établi. Le biais du survivant est signalé : RAPPORTÉ (dossier §3.1) | Sans dénominateur (les rapprochements stériles), aucune précision n'est calculable. |
| P2 | Les mondes synthétiques à lois plantées représentent la découverte réelle | HYPOTHÈSE. Le dossier les impose comme contrainte, il ne les valide pas | Le générateur encode la théorie de la découverte de son concepteur, d'où un risque de circularité. |
| P3 | Les corpus datés contiennent un signal antérieur des idées futures | VÉRIFIÉ (dossier §2.5) pour des cas rétrospectifs : Tshitoyan et al., 2019, *Unsupervised word embeddings capture latent knowledge from materials science literature* ; Luo et al., 2024, *Large language models surpass human experts in predicting neuroscience results*, id. dossier 2403.03230. La généralisation reste une HYPOTHÈSE | Ces succès ne sont pas comparés, dans le dossier, à des prédicteurs topologiques triviaux. |
| P4 | Un test sur processeur prédit le comportement d'un modèle d'environ 8 milliards de paramètres | HYPOTHÈSE | Gröger, Wen et Brbić (2026, id. dossier 2602.14486, titre pas sûr) montrent que les métriques globales sont confondues par la largeur et la profondeur (VÉRIFIÉ, dossier §2.4). Le transfert d'échelle est donc précisément ce qui est en doute. |
| P5 | La rétrodiction étanche est faisable avec des modèles de langue | Partiellement. La coupure simulée par consigne laisse un écart de 52 % (Li et al., 2026, id. dossier 2601.13717 : VÉRIFIÉ, dossier §2.6) | Seuls le masquage strict ou des modèles pré-entraînés avant la coupure sont admissibles. |
| P6 | L'« utilité pour le contrôle boîte blanche » se mesure sans juge humain ni génératif | HYPOTHÈSE | Le dossier interdit le juge génératif. Il faut donc des cas plantés appariés. |
| P7 | Les mécanismes de découverte sont séparables et testables un par un | HYPOTHÈSE | Les mécanismes partagent les mêmes statistiques sous-jacentes (voir le point 3). |

### Ce qu'un spécialiste examinerait d'abord

1. **Le modèle nul avant le mécanisme.**
   - Les plongements prédictifs factorisent une information mutuelle ponctuelle décalée (Levy et Goldberg, 2014, *Neural Word Embedding as Implicit Matrix Factorization* : VÉRIFIÉ, dossier §2.2).
   - Les symétries de cooccurrence par paires gouvernent la géométrie même sans co-apparition (Karkada et al., 2026, id. dossier 2602.15029 : VÉRIFIÉ, dossier §2.3).
   - Conséquence (HYPOTHÈSE) : une large part de la « connaissance latente » pourrait n'être que de la cooccurrence de second ordre, que des prédicteurs de liens topologiques (voisins communs, Adamic-Adar, attachement préférentiel) capturent déjà sans aucun apprentissage.
   - C'est le premier test à faire, et il est trivial sur processeur.
2. **L'évaluation, et non la génération, est le goulot.** Un système qui produit beaucoup d'idées sans dénominateur ni mondes nuls (sans loi plantée) ne peut pas mesurer son taux de fausses découvertes.
3. **La contrainte processeur est un atout d'étanchéité.**
   - Des modèles par comptage ou de petits plongements entraînés uniquement sur des tranches antérieures à t sont étanches par construction (HYPOTHÈSE de conception).
   - Un grand modèle pré-entraîné ne l'est pas (P5).
4. **Le local et le discret plutôt que le global et le continu.**
   - Les données vont dans ce sens : convergence surtout locale après étalonnage (dossier §2.4) ; géométrie circulaire se comportant comme sept états discrets (Gupta, Fruengel et Heimersheim, 2026, id. dossier 2610.37796 : VÉRIFIÉ, dossier §2.3).
   - Tout instrument de contrôle qui suppose un pilotage lisse le long d'une direction globale est suspect (HYPOTHÈSE).
5. **La loi de Goodhart sur les moniteurs.** Le dossier interdit d'optimiser contre un moniteur hors bras d'attaque déclaré. Toute mesure de robustesse doit donc être faite dans un bras d'attaque explicitement séparé et préenregistré.
6. **La limite informationnelle du sabotage dilué.**
   - En détection séquentielle classique (test séquentiel de Wald, CUSUM), le délai de détection croît comme log(1/α) divisé par l'information de Kullback-Leibler par pas.
   - Un sabotage dont la divergence totale reste bornée ne peut pas être détecté de façon fiable, quel que soit l'outil (cadre classique ; formulation exacte : référence à vérifier pour Lorden, 1971).
   - La question n'est donc pas « peut-on détecter tout sabotage dilué ? », mais « quel budget de dommage reste détectable à α donné, sous référence contaminée ? ».

---

## 2. Données brutes de départ

Le principe directeur (HYPOTHÈSE) est de ne garder que des données à partir desquelles **tout contrôle de permutation préservant fréquences et degrés peut être recalculé**. Cela exclut les représentations dont la date d'entraînement est inconnue.

| Source brute | Ce qu'elle contient | Pourquoi elle plutôt qu'une version agrégée |
|---|---|---|
| Résumés datés et métadonnées (PubMed/MEDLINE avec descripteurs MeSH datés, métadonnées arXiv, graphe de citations OpenAlex) | Comptes de co-mention par document, avec date et identifiant | Permet le recâblage à degrés préservés et la coupure stricte. Les « concepts » OpenAlex sont, à ma connaissance, attribués par un classifieur : je les écarte comme vérité-terrain (à vérifier). |
| Sources LaTeX d'arXiv | Équations en jetons, datées | Archive d'équations brute nécessaire pour les signaux de tension formelle (dossier §3.4). |
| Historique git de mathlib (Lean) | Introduction datée de définitions et refactorisations de preuves | Seule archive que je connaisse où la naissance d'un objet formel est horodatée au commit près. La migration Lean 3 → Lean 4 crée un artefact massif à exclure (date exacte à vérifier). |
| Mondes synthétiques générés par l'évaluateur externe | Corpus, graphes, flux d'actions à lois plantées scellées | Seule vérité-terrain sans biais de déclaration ; contrainte du dossier §1. |
| Activations et poids bruts de petits modèles à données d'entraînement publiques (suite Pythia : Biderman et al., 2023, *Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling*), puis de modèles ouverts d'environ 8 milliards de paramètres | États internes non projetés | Les dictionnaires de caractéristiques pré-entraînés par des tiers sont des représentations pré-agrégées, à n'introduire qu'après les tests sur activations brutes. |

---

## 3. Démarcation théorique et risques méthodologiques

### Ce qui peut et ne peut pas être inféré

**Inférable, au moins partiellement.**
- La structure relationnelle reflétée dans les symétries de cooccurrence : géographie (Louwerse et Zwaan, 2009, *Language encodes geographical information* ; Barjamovic et al., 2017), couleurs (Abdou et al., 2021, *Can Language Models Encode Perceptual Structure Without Grounding? A Case Study in Color*, id. dossier 2109.06129), espace et temps (Gurnee et Tegmark, 2023, *Language Models Represent Space and Time*, id. dossier 2310.02207). Statut : VÉRIFIÉ (dossier §2.1).
- Des voisinages locaux stables entre modèles : VÉRIFIÉ (dossier §2.4).

**Non inférable, ou non garanti.**
- L'ancrage référentiel (Bender et Koller, 2020, *Climbing towards NLU: On Meaning, Form, and Understanding in the Age of Data*).
- Ce qui n'est jamais écrit (Gordon et Van Durme, 2013, *Reporting bias and knowledge acquisition*).
- Une loi transférable aux tâches voisines, même quand la prédiction est bonne (Vafa et al., 2024, *Evaluating the World Model Implicit in a Generative Model*, id. dossier 2406.03689 ; Vafa et al., 2025, titre pas sûr, id. dossier 2507.06952). Statut : VÉRIFIÉ (dossier §2.5–2.6).

**Démarcation proposée (HYPOTHÈSE).** Un corpus textuel donne accès aux statistiques de ce que des humains ont écrit sur le monde. Une « découverte » textuelle n'est revendicable que si elle a deux propriétés :
- c'est un motif présent avant t, non co-mentionné avant t, qui bat les prédicteurs topologiques et fréquentiels ;
- elle est *vérifiée hors texte* : par une loi plantée, une expérience, ou une preuve formelle.

### Solidité formelle par mécanisme

| Mécanisme | Statut | Critère de solidité proposé (HYPOTHÈSE) | Menaces principales | Vérification mécanique à battre |
|---|---|---|---|---|
| Alignement inter-domaines (Gentner, 1983, *Structure-mapping: A theoretical framework for analogy* ; Swanson, 1986, *Fish oil, Raynaud's syndrome, and undiscovered public knowledge*) | RAPPORTÉ (dossier §3.1) | L'alignement doit préserver des relations *typées*. Son gain doit survivre au recâblage à degrés préservés. | Polysémie (chaînage non typé), biais du survivant, corrélation négative moyenne entre distance brute et intérêt (dossier §3.1), règles d'exclusion des analogies (Linzen, 2016, *Issues in evaluating semantic spaces using word analogies*) | Adamic-Adar, filtre fréquentiel apparié |
| Scission de concepts confondus (Lakatos, 1976, *Proofs and Refutations*) | RAPPORTÉ (dossier §3.2) : « peu formalisée » | Une fausse identité produit des *prédicats incompatibles dans un même voisinage thématique*. Un homonyme produit des *voisinages thématiques disjoints*. Les deux signatures sont distinctes et testables. | Confusion avec l'homonymie ; effectif historique minuscule | Induction de sens par regroupement de contextes |
| Émergence par percolation ou principes variationnels | RAPPORTÉ (dossier §3.3) : objection de taille finie | L'exposant ou la date de transition doit être invariant à la granularité et absent du modèle de configuration. | Hétérogénéité des degrés, granularité, taille finie | Modèle de configuration ; urnes à déclenchement (Tria et al., 2014, *The dynamics of correlated novelties*) |
| Nouvelles abstractions (Carey, 2009 ; Kuhn, 1962) | RAPPORTÉ (dossier §3.4) : circularité | Le signal doit précéder l'introduction de l'objet *et* battre les contrôles d'activité (taille, fréquence d'édition). | Circularité : l'objet n'est visible qu'a posteriori ; biais de rétrospection | Fréquence de sous-termes répétés, compression générique |
| Dérive sémantique et lois statistiques (Hamilton et al., 2016, *Diachronic Word Embeddings Reveal Statistical Laws of Semantic Change* ; Dubossarsky et al., 2017, *Outta Control: Laws of Semantic Change and Inherent Biases in Word Representation Models*) | VÉRIFIÉ (dossier §2.5) : biais de fréquence | Contrôle par corpus mélangé dans le temps | Fréquence | Même pipeline sur un corpus à dates permutées |

### Biais transversaux

1. **Fréquence et degré.** Il faut stratifier systématiquement par décile.
2. **Échelle.** La largeur et la profondeur confondent les métriques globales (dossier §2.4).
3. **Survivant.** Le dénominateur doit couvrir *toutes* les paires candidates.
4. **Sondes mémorisantes.** Il faut mesurer la sélectivité sur tâche de contrôle (Hewitt et Liang, 2019, *Designing and Interpreting Probes with Control Tasks*, id. dossier 1909.03368).
5. **Fuites temporelles.** La consigne de coupure ne suffit pas (P5).
6. **Circularité.** Le même générateur sert à concevoir et à évaluer le système. Contre-mesure (HYPOTHÈSE) : l'évaluateur externe dispose de *plusieurs familles* de générateurs, dont certaines sont conçues pour que le mécanisme y *échoue*. Un mécanisme qui « réussit » partout est suspect.

---

## 4. Méthodes, outils et protocoles ; (c) mesures minimales par instrument

### Protocole commun (HYPOTHÈSE)

- **Préenregistrement haché** avant lecture des résultats.
- **Trois types de mondes** :
  - à loi plantée ;
  - nul (aucune loi : le système doit se taire) ;
  - piège (la loi plantée ressemble à un artefact connu).
- **Rétrodiction** à coupure stricte, avec recâblage à degrés préservés et permutation des dates.
- **Correction des comparaisons multiples** (contrôle du taux de fausses découvertes).
- **Juge génératif exclu** de la validation (contrainte du dossier §1).

### (c) Mesure minimale pour chaque instrument

| Instrument | Mesure minimale | Cas honnêtes appariés | Vérifications mécaniques à battre |
|---|---|---|---|
| **Système d'idéation** | Taux de récupération des lois plantées ; taux d'alerte sur les mondes nuls ; précision@k en rétrodiction, stratifiée par fréquence | Mondes nuls de même taille et de mêmes marges que les mondes plantés | Prédicteurs de liens topologiques ; générateur de paires aléatoires apparié en fréquence ; heuristique de « termes en hausse récente » |
| **Détecteur séquentiel de sabotage** | Taux de fausses alertes *toujours valide* sur flux honnêtes ; taux de détection et délai en fonction du budget de dommage ; dégradation en fonction du taux de contamination ε de la référence | Jumeaux : même tâche, même graine, différant seulement par le dommage planté par l'évaluateur | CUSUM sur scores bruts ; seuil à fenêtre fixe ; borne d'un test séquentiel « oracle » connaissant la loi du sabotage, qui donne un plafond et non une cible |
| **Sonde de représentation** | Sélectivité selon Hewitt et Liang ; taux de détection à taux de fausses alertes fixé, avant et après le bras d'attaque déclaré | Même entrée avec ou sans la variable plantée | Sonde sur direction aléatoire ; **classifieur de surface sur le texte d'entrée seul**. Une sonde qui ne bat pas ce classifieur ne lit pas l'intérieur du modèle (HYPOTHÈSE). |
| **Audit des poids** | Aire sous la courbe ROC (AUROC) clair contre planté | Jumeaux entraînés à l'identique sauf le comportement planté par l'évaluateur | Norme de la différence avec le point de départ, si celui-ci est disponible : il faut donc aussi évaluer *sans* le point de départ. Échantillonnage comportemental boîte noire à budget de calcul égal. Si l'audit ne bat pas ce dernier, la boîte blanche n'apporte rien. |
| **Détecteur de coordination entre copies** | Corrélation excédentaire des actions | **Le bon modèle nul est « mêmes poids, contextes indépendants »** (HYPOTHÈSE) | Je ne sais pas s'il existe un détecteur fiable (voir ci-dessous). |

### Sur la coordination (HYPOTHÈSE)

- Des copies identiques peuvent se coordonner sans aucun canal, par des points focaux partagés. Un détecteur de canal serait donc aveugle par construction.
- Ce qui est détectable, c'est la *politique focale elle-même*. Il faut alors la distinguer d'une politique honnête simplement déterministe.

### Contamination de la référence (dérivation personnelle, à vérifier)

- Une p-valeur conforme vaut (1 + nombre de scores de référence supérieurs ou égaux au score testé) / (n + 1).
- Si k des n points de référence sont contaminés, ce compte varie d'au plus k, donc la p-valeur d'au plus k/(n+1).
- Des contaminants à *score bas*, qui « paraissent très honnêtes », gonflent le taux de fausses alertes. Des contaminants à score haut font perdre de la puissance.
- Corriger α en α − k_max/(n+1) préserve la validité *si* l'échangeabilité tient. Les flux d'actions ont une dépendance temporelle qui peut la rompre. C'est l'objet de l'action A3.
- Les tests par paris et e-processus (Ramdas, Grünwald, Vovk et Shafer, 2023, *Game-theoretic statistics and safe anytime-valid inference*) donnent la validité à tout instant d'arrêt sous l'hypothèse nulle *correctement spécifiée*. C'est précisément ce que la contamination met en cause.

---

## 5. Vérification indépendante

1. **Évaluateur externe détenteur des lois plantées.** Il les scelle par engagement haché avant génération et ne les révèle qu'après la soumission des sorties.
2. **Prédictions prospectives datées.** Le système publie aujourd'hui des liens et des scissions candidats, notés plus tard. C'est le seul test non rétrodictif ; il est lent, mais immunisé contre les fuites.
3. **Réplication sur un corpus disjoint**, d'un autre domaine et d'une autre langue, avec le pipeline gelé.
4. **Équipe rouge séparée** pour le bras d'attaque, sans accès aux seuils préenregistrés de l'équipe de défense.
5. **Publication des données de comptage et des nuls**, pour que tout tiers puisse recalculer les permutations.
6. **Experts aveugles à la provenance** (système ou paires aléatoires appariées), sollicités pour l'intérêt seulement, jamais pour la validité. Une collaboration adversariale avec un tenant de l'hypothèse nulle topologique est souhaitable.

---

## 6. Reformulation exigeante du problème

> Il ne s'agit pas de construire un générateur d'idées, mais un **banc d'épreuve**. Ce banc doit dire, mécanisme par mécanisme, s'il existe un signal *mesurable avant t* qui prédit l'apparition après t d'un lien, d'une scission ou d'une définition formelle, à quatre conditions :
> - **mieux que** le modèle nul topologique et fréquentiel ;
> - **sans alerter** sur les mondes nuls ;
> - **en conservant son avantage** quand la granularité ou l'échelle change ;
> - **en se transposant** en instruments de contrôle dont la garantie de fausses alertes survit à une référence contaminée et à un adversaire déclaré.
>
> Un mécanisme qui ne bat pas son vérificateur mécanique est classé comme artefact, quelle que soit l'élégance de son analogie.

---

## 7. Programme d'actions classé ; (b) duels et (d) ancrage

Les notes sont mes jugements (HYPOTHÈSE), sur l'échelle 1–5 de la question.

| Action | Gain | Facilité | Portée | Découverte | Coût | Score |
|---|---|---|---|---|---|---|
| A3 Détection séquentielle sous référence contaminée | 5 | 5 | 5 | 3 | 1 | **375** |
| A1 Plongements contre modèle nul topologique | 5 | 5 | 4 | 3 | 1 | **300** |
| A2 Scission contre homonymie, monde synthétique | 4 | 4 | 4 | 4 | 1 | **256** |
| A5 Tension formelle avant nouvelle définition (mathlib) | 4 | 3 | 3 | 5 | 1 | **180** |
| A6 Marge asymétrique des sondes (petit modèle synthétique) | 4 | 3 | 5 | 3 | 1 | **180** |
| A7 Chaînage typé contre filtre fréquentiel | 4 | 4 | 3 | 3 | 1 | **144** |
| A4 Invariance de l'exposant de percolation à la granularité | 4 | 5 | 3 | 2 | 1 | 120 |
| A8 Audit des poids sur jumeaux plantés | 4 | 3 | 5 | 4 | 3 | 80 |
| A9 Coordination entre copies | 3 | 2 | 5 | 4 | 3 | 40 |

Tous les seuils ci-dessous sont **illustratifs** et doivent être fixés par préenregistrement.

### A3. Garantie séquentielle sous référence contaminée

- **H_A** : la correction α − k_max/(n+1) appliquée à un e-processus conforme maintient le taux de fausses alertes à tout instant d'arrêt sous α, même sur des flux à dépendance temporelle, avec une contamination adverse de taux ε ≤ ε_max.
- **H_B** : la dépendance temporelle rompt l'échangeabilité. Une contamination choisie par l'évaluateur fait alors dépasser α malgré la correction.
- **Métrique** : taux empirique de fausses alertes sur flux honnêtes en fonction de ε et de la portée de dépendance ; puissance et délai en fonction du budget de dommage, rapportés à la borne oracle.
- **Seuil** (illustratif) : fausses alertes ≤ α + 2 erreurs-types sur 10⁴ flux.
- **Contrôle négatif** : flux honnêtes rendus *indépendants et identiquement distribués*. Les deux hypothèses y prédisent la validité ; s'il y a échec, le banc est défectueux.
- **Premier pas sur processeur** : générateur de flux à chaîne de Markov dans le monde synthétique de l'évaluateur, avec dommages plantés abstraits. Aucun modèle n'est requis.
- **Coût** (illustratif) : quelques heures de processeur.
- **Ce qui falsifie** :
  - H_A est réfutée si l'excès de fausses alertes est significatif pour une portée de dépendance donnée.
  - H_B est réfutée si la validité tient sur toute la grille préenregistrée.
- **Issue secondaire** : si la puissance reste au niveau du hasard, même à budget élevé, la limite tient au moniteur et non au test.

### A1. La « connaissance latente » bat-elle le modèle nul topologique ?

- **H_A** : la géométrie distributionnelle (matrice PPMI réduite par SVD, ou petits plongements entraînés avant t) porte une information sur les liens futurs que la topologie locale et la fréquence n'expliquent pas.
- **H_B** : le gain de cette géométrie s'annule une fois qu'on stratifie par fréquence et qu'on contrôle la topologie. C'est ce que suggèrent Levy et Goldberg (2014) et Karkada et al. (2026), d'après le dossier §2.2–2.3.
- **Métrique** : gain d'aire sous la courbe précision-rappel (ΔAUC-PR) du modèle « topologie + plongement » sur le modèle « topologie seule ». Le calcul porte sur *toutes* les paires non liées au-dessus d'une fréquence minimale, par décile.
- **Seuil** (illustratif) : ΔAUC-PR ≥ 0,02, avec un intervalle de confiance excluant 0 dans au moins 7 déciles sur 10.
- **Contrôle négatif** : le même pipeline appliqué à un corpus recâblé à degrés préservés et à des cibles à dates permutées. Le gain doit y être nul.
- **Premier pas sur processeur** : une tranche annuelle de résumés PubMed, d'abord limitée à un domaine.
- **Coût** (illustratif) : une journée de processeur.
- **Ce qui falsifie** :
  - H_A est réfutée si le gain est nul ou égal à celui obtenu sur le corpus recâblé.
  - H_B est réfutée par un gain stable sur l'ensemble des déciles.
- **Portée** : si H_B l'emporte, les succès rétrospectifs du dossier §2.5 sont à requalifier comme des signaux topologiques. C'est une économie majeure de calcul sur carte graphique.

### A2. Fausse identité contre homonymie

- **Monde synthétique** : l'évaluateur génère trois types de jetons.
  - (i) Un jeton T émis pour deux concepts latents du *même* domaine, dont un prédicat porte des valeurs incompatibles. C'est l'analogue structurel de la paire chaleur/température.
  - (ii) Un jeton T′ émis pour deux concepts de domaines disjoints : un homonyme.
  - (iii) Des jetons non confondus, appariés en fréquence.
- **H_A** : un score de conflit de prédicats dans un voisinage thématique partagé (gain de longueur de description d'une scission, restreint aux assertions typées) sépare (i) de (ii), là où l'induction de sens échoue.
- **H_B** : fausse identité et homonymie sont statistiquement indiscernables. Aucun score ne bat l'induction de sens.
- **Métrique** : AUROC entre (i) et (ii), à taux de fausses alertes fixé sur (iii).
- **Seuil** (illustratif) : AUROC ≥ 0,8, et au moins 0,1 au-dessus de l'induction de sens.
- **Contrôle négatif** : mondes sans confusion plantée. Le score ne doit rien signaler au-delà de α.
- **Premier pas sur processeur** : générateur et comptes, sans réseau.
- **Coût** (illustratif) : quelques heures.
- **Ce qui falsifie** :
  - H_A est réfutée si l'AUROC (i)/(ii) n'est pas meilleure que celle de l'induction de sens.
  - H_B est réfutée par une séparation nette, *y compris* sur les générateurs-pièges.
- **Pont vers le contrôle (HYPOTHÈSE)** : le même score, appliqué à une direction de sonde, testerait si un « concept de sûreté » sondé confond deux variables. Les quelques cas historiques ne servent qu'à une description, sans valeur décisive.

### A5. La tension formelle précède-t-elle la nouvelle définition ?

- **H_A** : avant le commit qui introduit une définition D dans mathlib, les preuves refactorisées plus tard autour de D montrent une redondance compressible (sous-termes répétés, croissance de longueur) supérieure à celle de preuves témoins appariées.
- **H_B** : ce signal n'excède pas celui des témoins appariés en âge, en taille et en fréquence d'édition. Les définitions naissent pour des raisons d'organisation non prédictibles.
- **Métrique** : AUROC d'une prédiction faite à t de l'introduction d'une abstraction dans la fenêtre Δ.
- **Seuil** (illustratif) : AUROC ≥ 0,65, et au-dessus du modèle d'activité.
- **Contrôle négatif** : dates d'introduction permutées entre fichiers d'âge égal ; période de migration Lean 3 → Lean 4 exclue.
- **Premier pas sur processeur** : extraction de l'historique git et décomptes de sous-termes.
- **Coût** (illustratif) : une à deux journées de processeur, plus le temps d'ingénierie.
- **Ce qui falsifie** :
  - H_A est réfutée si l'AUROC ne dépasse pas celle du modèle d'activité.
  - H_B est réfutée si le surplus est stable dans le temps.
- **Limite** : le transfert vers la physique ou les équations est une HYPOTHÈSE non testée ici. Cette action brise la circularité du dossier §3.4 seulement *dans un domaine où l'objet est horodaté*.

### A6. Marge asymétrique des sondes

- **Modèle** : petit transformeur entraîné sur processeur sur un monde à variable plantée, à la manière de Li et al., 2023, *Emergent World Representations: Exploring a Sequence Model Trained on a Synthetic Task*, id. dossier 2210.13382.
- **Bras d'attaque déclaré** : optimisation contre une sonde linéaire P. Le protocole est détenu par l'équipe rouge et n'est pas détaillé ici.
- **H_A** : un détecteur fondé sur un invariant distinct (accord de voisinages locaux étalonné par permutation, ou intervention causale) conserve un taux de détection supérieur au seuil, à taux de fausses alertes fixé, quand la performance sur la tâche est préservée.
- **H_B** : l'évasion contre P se transfère à *tous* les détecteurs fondés sur les représentations dès que la performance est préservée. Il n'y a pas de marge asymétrique.
- **Seuil** (illustratif) : taux de détection ≥ 0,7 à 5 % de fausses alertes.
- **Contrôle négatif** : la même optimisation contre une direction aléatoire. Les détecteurs ne doivent pas y perdre de puissance.
- **Vérification mécanique** : classifieur de surface sur les entrées.
- **Coût** (illustratif) : une à trois journées de processeur pour un modèle de quelques millions de paramètres.
- **Ce qui falsifie** :
  - H_A est réfutée si tous les détecteurs tombent sous le seuil.
  - H_B est réfutée si un détecteur tient sur au moins 3 graines préenregistrées.
- **Contrainte** : aucun signal de sonde ne sert à entraîner l'agent hors de ce bras d'attaque (dossier §1).

### A7. Chaînage A-B-C typé contre filtre de fréquence

- **H_A** : typer l'intermédiaire B (types sémantiques MeSH, datés et attribués par des humains) réduit les faux positifs à rappel égal, au-delà de ce qu'obtient un filtre fréquentiel.
- **H_B** : le gain du typage est entièrement reproduit en excluant les intermédiaires B de haute fréquence. Autrement dit, le typage n'est qu'un filtre de polysémie déguisé en filtre de fréquence.
- **Métrique** : précision à rappel fixé sur les liens A-C apparus après t.
- **Seuil** (illustratif) : +5 points de précision au-dessus du filtre fréquentiel.
- **Contrôle négatif** : types permutés entre termes de même fréquence.
- **Coût** (illustratif) : une journée de processeur.
- **Ce qui falsifie** :
  - H_A est réfutée si les types permutés font aussi bien.
  - H_B est réfutée si le surplus persiste à fréquence appariée.

### Actions non retenues dans les six premières

- **A4** : rapide et probablement réfutante pour l'hypothèse de criticité. Elle passe en septième position.
- **A8 et A9** : elles exigent des modèles plus gros ou n'ont pas de modèle nul établi (A9 : je ne sais pas en construire un convaincant aujourd'hui).

### (d) Ancrage matériel (illustratif sauf mention)

| Étape | Matériel | Coût |
|---|---|---|
| A1–A7 | Processeur seul, une station de 32 à 64 cœurs | Quelques jours de processeur au total, illustratif |
| Transfert d'échelle de A6 et A8 | Modèles ouverts d'environ 8 milliards de paramètres (taille : dossier §1), activations seulement, sans entraînement complet | Quelques dizaines d'heures de carte graphique, illustratif |
| Rétrodiction avec un modèle de langue | Uniquement des modèles pré-entraînés avant la coupure (dossier §2.6 : Luo et al., 2026, id. dossier 2606.02991 ; Hla, 2026) ou un masquage strict (Ma et al., 2026, id. dossier 2605.03762). Les modèles d'environ 8 milliards de paramètres à données non datées sont exclus de la rétrodiction. | Non estimé |

La passerelle vers les cartes graphiques n'est ouverte que si, en A1, H_B est réfutée, ou si, en A6, H_A survit. Sinon, le calcul lourd n'a pas d'objet mesurable (HYPOTHÈSE).

### Limites qui subsistent

1. Les mondes synthétiques ne valident que ce que leur générateur sait planter. La circularité est réduite, pas supprimée.
2. Les deux familles manquantes du §3 ne sont pas couvertes.
3. Le transfert du processeur vers l'échelle d'environ 8 milliards de paramètres reste une HYPOTHÈSE, précisément mise en doute par le dossier §2.4.
4. La dérivation k/(n+1) est la mienne et doit être vérifiée.
5. Pour la coordination entre copies, je ne sais pas.
6. La formule de score est multiplicative et récompense les actions faciles. Une action à fort potentiel mais coûteuse (A8) peut être sous-classée.
7. Les prédictions prospectives ne donnent rien avant plusieurs années.

FIN-DE-CELLULE