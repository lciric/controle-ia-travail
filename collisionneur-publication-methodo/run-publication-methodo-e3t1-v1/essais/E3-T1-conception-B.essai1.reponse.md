# Cellule III.1 — Proposition B

**Pièces.** Le bloc FAITS ne contient aucun fait, par décision de l'arbitre. Tout ce que décrit la question est donc au mieux RAPPORTÉ par l'arbitre. Je n'ai pas vérifié les empreintes sha256 et je ne les certifie pas. A et C ne me sont pas visibles (tour à l'aveugle) : la règle B1 ne s'applique pas ici, aucune autre proposition n'est attaquée ni utilisée.

---

## (a) Ce que la question suppose sans que ce soit établi

| # | Présupposé | Statut | Ce qui le vérifierait |
|---|---|---|---|
| a1 | Le cadre existe tel que décrit : organismes, noyau fixe, exécutants figés, règles de scellement. | RAPPORTÉ | Un dépôt avec empreintes et horodatage externe. |
| a2 | Coûts et délais : « quelques milliers de dollars », 24 à 48 h, 20 à 45 USD par course, « quelques heures de GPU ». | RAPPORTÉ | Factures et journaux d'exécution. |
| a3 | La « conscience d'évaluation » est une propriété du modèle, et pas seulement du texte d'entrée. | HYPOTHÈSE | Un construit opérationnel, avec validité convergente (comportement et activations) et discriminante (traits de surface). |
| a4 | Il existe une vérité terrain pour l'étiqueter. En pratique, les étiquettes portent sur le contexte (évaluation ou déploiement simulé), pas sur un état interne. | HYPOTHÈSE | Accord entre plusieurs opérationnalisations indépendantes. |
| a5 | Une sonde linéaire sur un modèle de 8 milliards de paramètres lit ce construit plutôt que des marqueurs lexicaux. | HYPOTHÈSE | Duel X1 ci-dessous. |
| a6 | Une sonde lisible implique que le modèle *utilise* l'information. | HYPOTHÈSE, souvent fausse en interprétabilité | Une intervention causale (pilotage ou ablation de la direction). |
| a7 | Le « maintien des contraintes à la délégation » est observable dans des traces textuelles accessibles. | HYPOTHÈSE | Un corpus de traces de délégation avec contraintes annotées. |
| a8 | Le progrès d'une génération à l'autre ne vient pas d'un surajustement à l'ensemble de sélection. | HYPOTHÈSE | Familles tenues à l'écart et bras permuté (duel X3). |
| a9 | E1 est lisible « quel que soit le signe ». Cela n'est vrai que si la puissance permet une conclusion d'équivalence. | HYPOTHÈSE, non établie par la question | Calcul de puissance sur l'unité « graine ». |
| a10 | Les hypothèses de l'essaim sont nouvelles et non triviales. | HYPOTHÈSE | Recherche bibliographique journalisée et scellée avant le test. |
| a11 | Les deux courses du pilote sont indépendantes. | HYPOTHÈSE | Elles ne le sont pas si la génération 2 de S agit sur le noyau, ou si M réutilise le même état. |
| a12 | Le lectorat visé pondère les critères cités (préenregistrement, témoins, puissance). | HYPOTHÈSE plausible, sans fait joint | Lecture des normes affichées par ces forums et laboratoires (à vérifier). |
| a13 | Des agents exécutants peuvent tenir « aucune lecture avant scellement ». | HYPOTHÈSE | Une contrainte mécanique : résultats chiffrés tant que l'empreinte du préenregistrement n'est pas publiée. Une consigne ne suffit pas. |

Point d'attaque sur le vocabulaire : « conscience » est un terme qui sera lu comme anthropomorphe. « Reconnaissance d'un contexte d'évaluation » dit la même chose de façon plus défendable et ne promet rien sur un état interne (a3, a4).

---

## (b) Expériences décisives (inférence forte)

**Règle commune aux duels.** Chaque duel a trois issues préenregistrées :
- H_B falsifiée ;
- H_A falsifiée par un test d'équivalence (TOST, Lakens 2017) dans une borne fixée à l'avance ;
- non concluant, déclaré comme tel.

Tous les seuils ci-dessous sont **illustratifs**.

### X1 — La sonde lit-elle autre chose que la surface ?

- **H_A** : la sonde apporte une information sur l'étiquette au-delà de celle d'un prédicteur de surface.
- **H_B** : le signal de la sonde se réduit aux traits de surface.
- **Unité statistique** : la *famille de gabarits* d'invites. Les items d'un même gabarit ne sont pas indépendants, donc le n effectif est le nombre de familles.
- **Métrique** : ΔAUROC = AUROC(sonde + surface) − AUROC(surface seule), sur des familles jamais vues à l'entraînement. Intervalle par bootstrap sur les familles.
- **Seuils (illustratifs)** :
  - borne inférieure de l'intervalle > 0,02 : H_B falsifiée ;
  - intervalle entièrement dans ±0,02 : H_A falsifiée.
- **Prédicteur de surface à battre** : régression logistique TF-IDF, liste de mots-clés (« test », « évaluation », « benchmark », formats QCM), longueur, présence de consignes.
- **Contrôles négatifs** :
  - tâche de contrôle à étiquettes permutées (Hewitt et Liang, 2019) ;
  - direction aléatoire de même norme ;
  - même sonde sur une couche d'embedding (couche 0).
- **Contrôle positif** : un jeu à marqueurs explicites, où sonde et prédicteur de surface doivent tous deux réussir. S'ils échouent, le pipeline est cassé et rien n'est interprétable.

### X2 — Transfert d'un protocole explicite vers un protocole non intrusif

C'est l'exemple de l'arbitre, reformulé pour être décisif. Comparer des scores moyens entre les deux protocoles est trivial : la sonde réagit aux marqueurs. Le test utile est le **transfert**.

- **H_A** : une direction apprise sur des contextes explicites sépare les contextes évaluation/déploiement du protocole non intrusif, sans aucun marqueur.
- **H_B** : elle ne transfère pas ; l'AUROC non intrusive ≈ 0,5.
- **Plan apparié** : la même tâche de base est rendue sous les deux protocoles et sous deux cadres (évaluation, déploiement). La perplexité et la longueur sont égalisées entre les cadres.
- **Seuils (illustratifs)** :
  - borne inférieure de l'AUROC de transfert > 0,6 : H_B falsifiée ;
  - intervalle dans [0,45 ; 0,55] : H_A falsifiée.
- **Contrôles** : les mêmes que X1, plus une sonde entraînée sur le prédicteur de surface du protocole explicite. Si celle-ci transfère aussi bien, le transfert est lexical.
- **Option causale** : ajouter ou soustraire la direction et mesurer un changement de comportement préenregistré. C'est ce qui ferait passer de « lisible » à « utilisé » (a6).

### X3 — L'essaim apprend-il (H-E1) ?

- **H_A** : sur les familles tenues à l'écart, le gain entre la génération 0 et la génération G du bras évolutif dépasse celui du bras gelé **et** celui du bras à score permuté.
- **H_B** : les gains sont indiscernables. Le « progrès » s'explique alors par du bruit, une régression vers la moyenne ou une sélection sur l'ensemble de test.
- **Unité** : la graine (une course complète). Les items à l'intérieur d'une course sont corrélés et ne comptent pas comme unités.
- **Métrique** : différence de gain, avec un intervalle sur les graines.
- **Puissance (calcul explicite, entrées illustratives)** : pour une comparaison appariée à d_z = 0,8 (effet supposé grand), α = 0,05 bilatéral, puissance 0,8, n ≈ (1,96 + 0,84)² / 0,64 ≈ 12 graines par comparaison. Conclure à l'équivalence demande davantage. Avec 1 à 3 graines, une issue nulle n'est **pas** informative ; elle doit être préenregistrée comme « non concluant ».
- **Contrôle négatif** : le bras permuté doit produire un nul. S'il « apprend », c'est le score ou la fuite qui est en cause, pas l'essaim.

### X4 — Gradient conçu par l'essaim (expérience 3)

**Attaque contre le plan rapporté.** Le comparer à un « bras sans entraînement » rend H_B presque impossible : n'importe quelle sonde entraînée bat une sonde non entraînée. Le résultat serait frappant, pas informatif, et le plan ne respecte pas B4.

Duel corrigé :
- **H_A** : la sonde dont la perte, l'architecture et les données sont conçues par l'essaim bat une régression logistique standard, avec les mêmes données d'origine, le même budget de calcul et le même protocole de validation.
- **H_B** : elle ne fait pas mieux.
- **Métrique** : AUROC sur familles tenues à l'écart.
- **Seuils (illustratifs)** : borne inférieure de Δ > 0,02 falsifie H_B ; équivalence dans ±0,02 falsifie H_A.
- **Garde-fou spécifique** : l'essaim écrit aussi les *données*. Il faut donc un jeu d'évaluation scellé, produit par une autre famille de modèles ou par des humains, que l'essaim ne voit jamais. Sans cela, il peut apprendre ses propres artefacts.
- **Le bras sans entraînement** reste utile comme contrôle positif de cohérence : la sonde de l'essaim doit le battre, sinon le pipeline est défectueux.

### X5 — Le contrôle des fausses découvertes tient-il sous la dépendance réelle ?

- **H_A** : la procédure choisie maintient un FDR empirique ≤ q sur des simulations dont la structure de dépendance imite le flux (hypothèses corrélées, mêmes items réutilisés).
- **H_B** : le FDR empirique dépasse q.
- **Seuil (illustratif)** : FDR empirique > q + 0,02 sur 1 000 flux simulés falsifie H_A.
- **Contrôle** : une procédure non corrigée doit violer q. Sinon la simulation est trop facile.

**Hors B4, déclaré** : le pilote (expérience 2) est descriptif par construction. Il n'oppose pas d'hypothèses et ne doit pas être présenté comme un test.

---

## (c) Instruments : la mesure minimale qui dirait s'ils fonctionnent

Toutes les cibles chiffrées de ce tableau sont **illustratives**.

| Instrument | Cas « pièges » (détection) | Cas honnêtes appariés (fausses alertes) | Vérification mécanique à battre |
|---|---|---|---|
| Sonde de reconnaissance d'évaluation | Contextes d'évaluation sans marqueur lexical | Même tâche en cadre déploiement, longueur et perplexité égalisées | TF-IDF + logistique, liste de mots-clés, longueur ; TPR à FPR fixé à 5 % (illustratif) |
| Essaim comme détecteur d'évaluation dans le texte | Transcriptions où le modèle reconnaît l'évaluation implicitement | Transcriptions appariées sans reconnaissance, même thème | Recherche regex de verbalisations (« ceci est un test »), juge à un seul appel de modèle |
| Essaim comme détecteur de perte de contraintes | Délégations où une contrainte de la tâche mère est supprimée ou affaiblie (injection contrôlée) | Délégations où la contrainte est conservée mais **paraphrasée** | Correspondance de chaînes et d'embeddings entre contraintes mère et fille ; juge à un appel |
| Bras à score permuté | Pipeline à signal injecté connu : le vrai bras doit le détecter | Le bras permuté sur le même pipeline doit rester nul | Pas d'amélioration de la génération 0 à G attendue sous permutation |
| Témoin « un modèle, vote à k » | — | — | Coût apparié vérifié par journal de jetons. Un écart de coût > 10 % (illustratif) invalide la comparaison |
| Familles tenues à l'écart | Test de fuite : chercher dans les fichiers de l'organisme des n-grammes des familles cachées | — | Hachage des familles avant la course ; recherche de recouvrement exact et approximatif |
| Relecteur neuf | k erreurs plantées dans un préenregistrement (seuil manquant, unité erronée, règle d'arrêt absente) ; taux de détection | Préenregistrement propre : nombre d'objections infondées | Un linter qui vérifie que chaque hypothèse a métrique, seuil, unité, règle d'arrêt et contrôle |
| Scellement et empreintes | Fichier modifié après scellement : la non-concordance doit être détectée (100 % attendu) | Fichier intact : 0 fausse alerte attendue | sha256 avec horodatage **externe** (étiquette git poussée chez un tiers, ou horodatage public). Une empreinte locale seule ne prouve pas l'antériorité |
| Contrôle de nouveauté et de redécouverte | Hypothèses déjà publiées glissées parmi les candidates ; taux marqué « non nouvelle » | Hypothèses reformulées mais réellement distinctes (difficile à garantir, à déclarer) | Recherche des plus proches voisins par embeddings sur un corpus d'articles |
| Procédure de contrôle des fausses découvertes | Simulations avec non-nuls connus : puissance | Nuls connus : FDR empirique | Bonferroni (trop conservateur) et absence de correction (doit échouer) |

Si un instrument ne bat pas sa vérification mécanique sur ses cas appariés, il ne doit pas servir de critère dans une expérience préenregistrée.

---

## (d) Ancrage matériel

Tous les chiffres de cette section sont **illustratifs**, sauf ceux marqués RAPPORTÉ.

- **Modèles ouverts d'environ 8 milliards de paramètres** : Llama 3.1 8B Instruct (Meta, 2024) ; Qwen3-8B (Alibaba, 2025) ; Ministral 8B (Mistral AI, 2024). Disponibilité et versions à vérifier à la date de la demande. Il faut fixer l'empreinte de révision des poids dans le préenregistrement.
- **Outils** : transformers (Hugging Face), TransformerLens ou nnsight pour les activations, scikit-learn pour les sondes.
- **Calcul des activations** : environ 2 × 8·10⁹ ≈ 1,6·10¹⁰ FLOP par jeton. Pour 2 000 items × 512 jetons ≈ 10⁶ jetons, cela donne ≈ 1,6·10¹⁶ FLOP, soit quelques minutes sur un GPU de 40 à 80 Go à un débit effectif de 10¹⁴ FLOP/s.
- **Stockage** : 4 096 dimensions × 32 couches × 2 octets ≈ 262 ko par item, soit ≈ 0,5 Go pour 2 000 items (dernier jeton ou moyenne).
- **Entraînement des sondes** : quelques minutes sur CPU. Les bootstraps sur familles dominent le temps de calcul, sans dépasser des heures.
- **Coût d'un test de niveau objet (X1 + X2)** : 5 à 15 h de GPU loué à 2–4 USD/h, plus la génération des stimuli par API. Ordre de grandeur : < 100 USD par test.
- **E1** : « quelques milliers de dollars » (RAPPORTÉ). Avec ≈ 12 graines par comparaison (X3), le coût réel pourrait être un multiple de ce chiffre. C'est à vérifier avant tout scellement.

---

## Réponses aux six points

### 1. Crédibilité : informatif contre frappant

**Ce que chaque critère neutralise :**

| Critère | Ce qu'il neutralise |
|---|---|
| Préenregistrement | Jardin des chemins bifurquants (Gelman et Loken, 2013), HARKing, changement de critère |
| Témoins | Explications concurrentes (surface, fuite, pipeline) |
| Puissance | Nuls ininformatifs et effets gonflés chez les gagnants (Button et al., 2013) |
| Taille d'effet et intervalle | Confusion entre « significatif » et « important » |
| Réplication (graines, modèles, gabarits) | Variance non mesurée |
| Code et données | Erreurs de calcul non détectables |

En interprétabilité, deux critères s'ajoutent : le test hors distribution (familles tenues à l'écart) et l'intervention causale.

**Formalisation proposée** (une voie parmi d'autres).

Soient des hypothèses H_A et H_B, des explications parasites H_C (surface, fuite), et des issues o préenregistrées. Un **plan** est informatif si :

1. pour chaque issue o, |log P(o | H_A) / P(o | H_B)| ≥ τ : toute issue déplace la croyance ;
2. pour l'issue confirmante o⁺, P(o⁺ | H_C) ≪ P(o⁺ | H_A) : les explications parasites sont dominées.

Un **résultat** est frappant si sa surprise −log P(o) est grande sous les croyances de fond du lecteur, alors que log P(o | H_A) / P(o | H_C) ≈ 0. Autrement dit, il étonne mais ne départage pas.

Exemple : « la sonde détecte l'évaluation avec une AUROC de 0,95 » est frappant tant qu'un TF-IDF fait aussi bien.

**Voie alternative** : mesurer l'information mutuelle attendue I(H ; X) du plan (point 2). Ce qui départage les deux formalisations : la condition 2 rend H_C explicite, alors que l'information mutuelle la cache dans la définition de H.

### 2. Quoi publier en premier : information par unité de coût

**Formalisation (voie 1).** IG_e = I(H ; X_e) en bits, rapporté à c_e + λ·t_e.

Calcul explicite, pour une hypothèse binaire avec a priori 0,5 et α = 0,05 (toutes entrées illustratives) :

| Puissance | P(+) | P(H \| +) | P(H \| −) | Gain d'information |
|---|---|---|---|---|
| 0,8 | 0,425 | 0,94 | 0,17 | ≈ 0,48 bit |
| 0,3 | 0,175 | 0,86 | 0,42 | ≈ 0,085 bit |

La puissance multiplie l'information d'un facteur d'environ 5,6.

En appliquant ce calcul aux coûts de (d) :
- un test de niveau objet bien puissant : ≈ 0,48 bit pour < 100 USD (illustratif) ;
- E1 avec 1 à 3 graines : puissance faible, donc ≈ 0,1 bit pour quelques milliers de dollars (RAPPORTÉ pour le coût, illustratif pour la puissance).

**Voie 2 : valeur attendue de l'information échantillonnée** (Howard, 1966). Elle demande une décision en aval avec ses utilités, par exemple « investir ou non dans le programme d'essaims ». Elle peut inverser le classement si E1 conditionne une décision coûteuse que les tests de niveau objet n'éclairent pas.

**Ce qui départage les deux voies** : l'existence d'une décision explicite à enjeu. S'il y en a une, la voie 2 l'emporte ; sinon, la voie 1 suffit.

**Ce qui reste informatif avec une issue négative :**

| Expérience | Informatif si négatif ou nul ? |
|---|---|
| E1 | Seulement avec équivalence et assez de graines (X3). Le bras permuté valide le pipeline dans tous les cas. |
| Pilote | Informe sur la mécanique (incidents), jamais sur le niveau objet. |
| Expérience 3 contre « sans entraînement » | Un négatif est informatif (pipeline cassé), un positif ne l'est presque pas. Contre une sonde standard, un nul avec équivalence devient informatif. |
| Tests de niveau objet issus de M | Un non-transfert (X2) avec équivalence est un résultat sur le modèle de 8 milliards de paramètres, publiable quel que soit le signe. |

**Voies possibles**, sans en désigner une seule :
- (i) pilote M, puis tests de niveau objet, puis E1 ;
- (ii) E1 d'abord, si l'objet du premier écrit est l'essaim ;
- (iii) préenregistrement public de E1 avant exécution, puis test de niveau objet.

### 3. Ordre des deux courses du pilote

Soient V_S et V_M les valeurs d'information, p_S et p_M les probabilités d'une course sans incident.

- M en premier vaut V_M + p_M·V_S.
- S en premier vaut V_S + p_S·V_M.
- M en premier est préférable si et seulement si V_M(1 − p_S) > V_S(1 − p_M).

**Argument (hypothèses, non vérifiées) :**
- **Testabilité** : V_M ≥ V_S, car M produit des mécanismes et protocoles directement transformables en X1 et X2. S produit des propositions sur l'organisme lui-même, testables seulement par une autre course évolutive (coûteuse, a8) et exposées à la redécouverte de la littérature sur l'apprentissage automatique de structures.
- **Risque d'incident** : p_M ≥ p_S est plausible, car S invite la génération 2 à toucher à sa structure, et donc potentiellement au noyau fixe (a11).

Si ces deux inégalités tiennent, M passe en premier.

**Voie contraire** : lancer S d'abord comme essai de contrainte mécanique. Elle ne se défend que si l'on accepte de perdre M en cas d'incident. Elle devient la bonne option si p_M n'est pas significativement supérieure à p_S.

**Dépendance** : les deux courses doivent partir d'un état restauré par empreinte, pour que S ne contamine pas M ni l'inverse.

### 4. De l'hypothèse produite au test

**Chaîne de traitement :**

1. Journaliser **toutes** les hypothèses produites, avec leur empreinte, y compris celles qui sont rejetées. Ce journal est le dénominateur de la multiplicité, car la sélection elle-même est une source de comparaisons multiples.
2. Appliquer un score de sélection scellé : P(testable dans le budget) × π(1 − π) × 1/coût. Le terme π(1 − π), où π est la probabilité a priori que l'hypothèse soit vraie, est maximal quand l'issue est la plus incertaine. Ce score est filtré par :
   - un contrôle de nouveauté (recherche journalisée, requêtes scellées) ;
   - une probabilité de redécouverte estimée par les plus proches voisins.
3. Traduire chaque hypothèse retenue en duel X1 ou X2 (unité, métrique, bornes d'équivalence).
4. Calculer la puissance. En plan apparié, n ≈ (z₁₋α/₂ + z₁₋β)² / d_z². Avec d_z = 0,3 (illustratif) : ≈ 87 unités ; avec d_z = 0,2 : ≈ 196. L'unité doit être la famille de gabarits si les items sont générés à partir de gabarits.

**Contrôle des comparaisons multiples dans un flux.** Plusieurs voies, et ce qui les départage :

| Procédure | Cadre | Hypothèse requise | Limite |
|---|---|---|---|
| BH par lot (Benjamini et Hochberg, 1995) | Lot préenregistré | Indépendance ou dépendance positive (PRDS) | Non garanti si les hypothèses de l'essaim et les items sont corrélés de façon arbitraire |
| BY (Benjamini et Yekutieli, 2001) | Lot | Dépendance arbitraire | Conservatrice |
| α-investing (Foster et Stine, 2008) ; LORD (Javanmard et Montanari, 2018) ; SAFFRON (Ramdas et al., 2018, à vérifier) | Flux, décisions irrévocables, ordre fixé à l'avance | Le plus souvent indépendance | La puissance dépend de l'ordre |
| e-valeurs + e-BH (Vovk et Wang, 2021 ; Wang et Ramdas, 2022) | Lot ou flux | Dépendance arbitraire ; arrêt optionnel et ajout de données permis | Moins puissant à n fixe |

**Critères départageurs** : structure de dépendance (connue ou non), besoin d'arrêt optionnel, flux ou lot, puissance à budget fixé. X5 permet de trancher empiriquement sur la dépendance réelle.

**Biais propres aux hypothèses issues d'un modèle de langue :**
- **Contamination** : l'hypothèse « nouvelle » peut être une restitution de la littérature (a10). De plus, les stimuli générés par un modèle partagent la distribution d'entraînement du modèle sondé.
- **Circularité** : si l'essaim écrit l'hypothèse *et* les données de test, il peut tester ses propres artefacts. Il faut séparer les familles de modèles entre génération et test.
- **Confirmation et complaisance** : l'essaim tend à proposer des hypothèses alignées sur le cadrage de la question, d'où un biais vers les hypothèses vraies par construction ou triviales.
- **Sélection a posteriori** : choisir les hypothèses après avoir vu des données exploratoires sur le même modèle.

**Ce que le préenregistrement neutralise** : la flexibilité analytique, le changement de critère, le HARKing.

**Ce qu'il ne neutralise pas** : la validité de construit (a3, a4), la contamination, les biais de génération des stimuli, la sélection des hypothèses qu'on préenregistre (sauf si le journal complet est déposé), et un relecteur de la même famille de modèles que l'auteur.

### 5. Ordre et forme de publication

**Voie (i) : les tests d'abord.** L'affirmation porte sur le modèle de 8 milliards de paramètres. Elle est réfutable et ne dépend pas de la provenance.

Pour la provenance, on écrit : « hypothèses produites par un pipeline automatisé fondé sur des modèles de langue, décrit dans un écrit ultérieur ». On y joint l'empreinte horodatée de la description scellée de l'organisme et du journal complet des hypothèses, que l'on révèlera plus tard (engagement par hachage).

Risque : le lecteur escompte la provenance. Il ne faut donc pas en faire un argument. Elle se place en méthodes, pas dans le résumé.

**Voie (ii) : E1 d'abord**, comme écrit méthodologique, nuls inclus. Elle se défend si la puissance est suffisante (X3).

**Voie (iii) : billet de préenregistrement public avant exécution**, sur le modèle des rapports enregistrés. C'est la voie la moins coûteuse en crédibilité.

**Critère départageur** : l'affirmation sur laquelle on veut que le lecteur révise sa croyance.

**À joindre** :
- préenregistrement avec empreinte et horodatage externe ;
- code d'analyse qui produit **chaque** chiffre du texte ;
- items et gabarits ;
- empreinte de révision du modèle ;
- scores par item ;
- poids des sondes ;
- graines ;
- environnement figé ;
- activations, ou script pour les régénérer.

**Structure** :
- un résumé court listant les affirmations avec leur statut ;
- méthodes ;
- résultats, nuls compris ;
- contrôles ;
- « ce qui nous ferait changer d'avis » ;
- limites.

Longueur de 3 000 à 6 000 mots (illustratif), registre sobre.

**Erreurs classiques d'un premier écrit :**
- surinterprétation (« conscience ») ;
- absence de prédicteur de surface ;
- une seule graine ;
- exemples choisis à la main ;
- confusion entre exploratoire et confirmatoire ;
- longue introduction sur le programme ;
- vocabulaire propre au projet (« organisme », « noyau ») non défini ;
- pas de dialogue avec les travaux antérieurs ;
- texte qui sonne généré.

### 6. Références

Les attributions marquées « à vérifier » doivent être contrôlées avant toute citation.

**Génération d'hypothèses par des modèles de langue :**
- Si, Yang, Hashimoto (2024), « Can LLMs Generate Novel Research Ideas? A Large-Scale Human Study with 100+ NLP Researchers ».
- Lu et al. (2024), « The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery ».
- Platt (1964), « Strong Inference », *Science*.

**Contrôle des fausses découvertes :**
- Benjamini et Hochberg (1995), « Controlling the False Discovery Rate: A Practical and Powerful Approach to Multiple Testing », *JRSS B*.
- Benjamini et Yekutieli (2001), « The Control of the False Discovery Rate in Multiple Testing under Dependency », *Annals of Statistics*.
- Foster et Stine (2008), « α-investing: a procedure for sequential control of expected false discoveries », *JRSS B*.
- Javanmard et Montanari (2018), « Online Rules for Control of False Discovery Rate and False Discovery Exceedance », *Annals of Statistics*.
- Ramdas, Zrnic, Wainwright, Jordan (2018), « SAFFRON: an adaptive algorithm for online control of the false discovery rate » : à vérifier.
- Vovk et Wang (2021), « E-values: Calibration, Combination and Applications », *Annals of Statistics*.
- Wang et Ramdas (2022), « False Discovery Rate Control with E-values », *JRSS B*.
- Shafer (2021), « Testing by Betting », *JRSS A*.

**Crédibilité et méthode :**
- Ioannidis (2005), « Why Most Published Research Findings Are False ».
- Simmons, Nelson, Simonsohn (2011), « False-Positive Psychology ».
- Button et al. (2013), « Power Failure ».
- Nosek et al. (2018), « The Preregistration Revolution », *PNAS*.
- Lakens (2017), « Equivalence Tests: A Practical Primer… ».
- Gelman et Loken (2013), « The garden of forking paths » (texte de travail ; support exact à vérifier).
- Howard (1966), « Information Value Theory ».

**Sondes :**
- Alain et Bengio (2016), « Understanding intermediate layers using linear classifier probes ».
- Hewitt et Liang (2019), « Designing and Interpreting Probes with Control Tasks ».
- Belinkov (2022), « Probing Classifiers: Promises, Shortcomings, and Advances ».

**Reconnaissance d'évaluation et conscience situationnelle :**
- Laine et al. (2024), « Me, Myself, and AI: The Situational Awareness Dataset (SAD) for LLMs » : à vérifier.
- Needham, Edkins, Pimpale, Bartsch, Hobbhahn (2025), « Large Language Models Often Know When They Are Being Evaluated » : à vérifier.
- Travaux de sondes linéaires de la reconnaissance d'évaluation sur des modèles ouverts : référence à vérifier.
- Contrôle de l'IA : Greenblatt, Shlegeris et al. (2024), « AI Control: Improving Safety Despite Intentional Subversion » : à vérifier.

---

**Ce qui est réfutable dans cette proposition :**
1. M produit plus d'hypothèses testables que S. Réfuté si, sur les deux courses, la proportion d'hypothèses de S qui passent le filtre de sélection est supérieure.
2. Le plan de l'expérience 3 contre « sans entraînement » est non informatif. Réfuté si une sonde standard ne bat pas, elle non plus, le bras non entraîné.
3. E1 à 1–3 graines ne peut pas conclure à l'équivalence. Réfuté par un calcul de puissance sur une variance inter-graines mesurée plus faible que supposé.

FIN-DE-CELLULE