# Proposition B — Tour III.1 : un harnais pour mesurer « étroit et profond »

**Pièces transmises.** Le bloc FAITS ne contient aucun fait étiqueté. Il est identique au bloc QUESTION (même empreinte sha256). Je ne dispose donc d'aucun fait VÉRIFIÉ. Le seul contenu factuel est le contexte : « une équipe prévoit un système multi-agents… », que je traite comme RAPPORTÉ. Tout le reste de ce texte est HYPOTHÈSE ou renvoi à la littérature.

**B1.** Le tour se joue à l'aveugle : je ne vois aucune autre proposition et n'en critique donc aucune.

**Thèse.** « Étroit » n'est pas une propriété d'une idée. C'est une propriété du couple (idée, chercheur de référence Q, relation d'équivalence entre idées). « Profond » doit se mesurer par un effet contrefactuel sur un solveur mécanique figé, et non par un jugement. Tant que Q, l'équivalence et le solveur ne sont pas fixés à l'avance, l'affirmation « le système trouve de l'étroit-profond » n'est pas réfutable (HYPOTHÈSE, que je défends).

---

## (a) Ce que la question suppose sans que ce soit établi

| # | Présupposé | Statut | Commentaire |
|---|---|---|---|
| P1 | Une équipe prévoit le système et veut valider un harnais d'abord. | RAPPORTÉ | Seul fait du contexte. |
| P2 | Il existe un « même espace d'idées candidates » où l'échantillonnage aléatoire est défini. | HYPOTHÈSE | Faux pour le texte libre. Vrai seulement pour un espace formel : grammaire d'expressions, énoncés Lean, programmes. Sans cela, la ligne de base « aléatoire » n'a pas de sens. |
| P3 | L'étroitesse est intrinsèque à l'idée. | HYPOTHÈSE, que je crois fausse | Elle dépend du chercheur de référence et de la canonicalisation. Testé par E2. |
| P4 | La classe « étroit ∧ profond » est non vide dans les espaces choisis. | HYPOTHÈSE | Si elle est vide, toute comparaison donne 0 = 0. Il faut la peupler par construction (mondes plantés) avant de la chercher ailleurs. |
| P5 | La profondeur est mesurable à horizon et coût finis. | HYPOTHÈSE | Seuls des substituts à horizon fini sont mesurables. La « conséquence scientifique » réelle se déploie sur des années. |
| P6 | Profondeur et rareté sont séparables. | HYPOTHÈSE | Testé par E3. Si elles sont fortement corrélées sous Q, on compte deux fois la même chose. |
| P7 | Un juge LM peut partager les préférences du générateur. | RAPPORTÉ (littérature, non vérifié ici) | Zheng et al. (2023, NeurIPS Datasets & Benchmarks, « Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena ») rapportent un biais d'auto-valorisation. Panickssery, Bowman & Feng (2024, NeurIPS, « LLM Evaluators Recognize and Favor Their Own Generations ») rapportent une auto-reconnaissance corrélée à l'auto-préférence. |
| P8 | « Le modèle unique le plus fort » est identifiable et stable. | HYPOTHÈSE | Il dépend du domaine et du budget. Il faut le choisir par une règle préenregistrée. |
| P9 | Le gain éventuel viendrait de l'interaction multi-agents. | HYPOTHÈSE | Concurrente : plus d'échantillons + filtrage par vérificateur (E5). |
| P10 | Un harnais peut être validé avant que le système existe. | HYPOTHÈSE, partiellement vraie | Faisable sur positifs plantés et leurres. Non faisable pour la fuite par rétroaction propre au système (E6 exige le système). |

**Où le cadrage me semble faux.**
1. « Étroit et profond » mêle deux axes. Il faut publier la distribution jointe (rareté sous Q, profondeur), pas un produit ni un score unique.
2. Les lignes de base proposées omettent la plus dangereuse : le modèle unique, avec le même vérificateur et le même budget converti en échantillons (best-of-N filtré).
3. « Rarement atteint par la recherche ordinaire » demande de nommer la recherche ordinaire. Plusieurs références Q doivent être rapportées.

---

## (b) Expériences décisives (inférence forte)

Platt (1964, *Science* 146 : 347–353, « Strong Inference ») sert de cadre. Tous les seuils ci-dessous sont **illustratifs**. Ils doivent être préenregistrés (Nosek et al., 2018, *PNAS* 115(11), « The preregistration revolution »).

Notations :
- Q est un générateur de référence (par exemple le modèle unique échantillonné à température 1, ou l'énumérateur).
- c(·) est une canonicalisation : forme normale symbolique, énoncé Lean normalisé, ou classe d'équivalence comportementale d'un programme.
- **Étroitesse** : n(x) = −log P_Q(c(x) atteint dans un budget de référence B₀).
- **Profondeur** : d(x) = gain d'un solveur mécanique figé S sur un ensemble tenu à l'écart de conséquences K_test quand x lui est fourni, moins le gain d'un contrôle de même complexité.

### E1 — Le harnais voit-il la structure ou la surface ? (monde planté)

- **H_A** : les scores (n, d) détectent les idées plantées étroites-profondes.
- **H_B** : les scores suivent des traits de surface (longueur, complexité syntaxique, vocabulaire).
- **Dispositif** : mondes synthétiques à loi cachée, par exemple une dynamique ou un système algébrique générés par grammaire. On y plante une loi rare (faible probabilité sous Q, connue par construction) qui explique un ensemble K de phénomènes tenus à l'écart. On ajoute trois types de leurres appariés en longueur et en complexité :
  - rare-mais-stérile (étroit, non profond) ;
  - commun-mais-utile (profond, non étroit) ;
  - commun-et-stérile.
- **Métrique** : sensibilité et taux de fausses alertes pour la cellule « étroit ∧ profond ».
- **Seuil (illustratif)** : sensibilité ≥ 0,8 et fausses alertes ≤ 0,05, sur 200 positifs et 600 leurres. L'intervalle à 95 % d'une proportion de 0,8 sur n = 200 vaut environ ±0,055.
- **Contrôle négatif** : mondes à étiquettes permutées, où la « loi » n'explique plus K. La détection doit tomber au hasard.
- **Issues** :
  - Si les leurres de même surface sont détectés au même taux que les positifs, H_A est falsifiée.
  - Si les seuils sont atteints et que la détection s'effondre sous permutation, H_B est falsifiée.

### E2 — L'étroitesse dépend-elle de la référence ?

- **H_A** : les classements d'étroitesse sont stables d'une référence Q à l'autre. Seuil illustratif : ρ de Spearman ≥ 0,7 entre Q₁ (modèle 8B), Q₂ (autre famille, 7B) et Q₃ (énumérateur).
- **H_B** : l'étroitesse est propre à Q (ρ ≤ 0,3).
- **Contrôle négatif** : même Q avec deux graines. Cela donne le plafond de ρ dû au bruit d'estimation. Si ce plafond est lui-même inférieur à 0,7, l'expérience manque de puissance et on augmente l'échantillonnage.
- **Issues** :
  - ρ ≥ 0,7 falsifie H_B : on peut parler d'étroitesse sans indice.
  - ρ ≤ 0,3 falsifie H_A : toute affirmation devra s'écrire « étroit relativement à Q_k ». Le cadrage « rarement atteint par la recherche ordinaire » est alors mal posé sans indice.
- **Coût statistique** : affirmer P_Q < 10⁻⁴ avec zéro occurrence demande n ≈ 3/10⁻⁴ = 30 000 tirages par problème (règle de trois, borne supérieure à 95 %). Le seuil 10⁻⁴ est illustratif. Pour des raretés plus extrêmes, il faut des estimateurs d'événements rares (échantillonnage préférentiel, découpage multiniveaux ; référence à vérifier pour la variante adaptée aux LM).

### E3 — La rareté seule prédit-elle la profondeur ?

- **H_A** : sous Q et à validité fixée, la profondeur croît avec la rareté (ρ(n, d | valide) ≥ 0,5, illustratif).
- **H_B** : rareté et profondeur sont quasi indépendantes (|ρ| ≤ 0,1).
- **Dispositif** : énoncés valides tirés de Q dans deux domaines, un monde planté et une bibliothèque formelle (voir E-formel ci-dessous).
- **Contrôle** : profondeur calculée sur des idées de complexité appariée mais fausses (une constante perturbée). On attend d ≈ 0.
- **Issues** :
  - Si H_A tient, la « profondeur » mesurée est en partie redondante avec la rareté. Il faut la redéfinir conditionnellement à n.
  - Si H_B tient, les deux axes sont informatifs séparément et la cellule jointe est un objet propre.
  - Chaque issue falsifie l'autre hypothèse.

### E4 — Comparaison principale

- **Quantité primaire** : par problème p, succ_C(p) = 1 si au moins une idée trouvée satisfait n ≥ η (relativement à Q préenregistré) **et** d ≥ δ **et** une validité mécanique, dans le budget C.
- **Unité d'analyse** : le problème. Les graines sont imbriquées dans les problèmes et moyennées avant le test. L'unité n'est pas l'idée, car les idées d'un même run ne sont pas indépendantes.
- **Coût** : comptabilité complète, à appliquer identiquement à chaque bras :
  - jetons d'entrée et de sortie de **tous** les agents, critiques et sélecteurs compris ;
  - appels au vérificateur ;
  - temps mural.
  Rapporter la courbe succ_C pour plusieurs C, pas un seul point.
- **H_A** : succ_C(système) − max_b succ_C(b) ≥ Δ_min. L'enveloppe des lignes de base est prise par problème ou globalement, à préenregistrer. Δ_min = 0,10 est illustratif.
- **H_B** : la différence est ≤ 0.
- **Règle de décision** : test apparié par problèmes (bootstrap par problème, ou McNemar si l'issue est binaire). Correction de Holm sur les comparaisons au-delà de l'enveloppe. Plan séquentiel de groupe (O'Brien & Fleming, 1979, *Biometrics* 35, « A multiple testing procedure for clinical trials »).
- **Contrôles négatifs** :
  1. **Test A/A** : le système contre lui-même, avec étiquettes de bras aléatoires. Il doit conclure « pas de différence » au taux nominal.
  2. **Système placebo** : un seul modèle, même nombre d'appels, rôles attribués au hasard sans interaction.
- **Issues** :
  - Borne inférieure de l'IC > Δ_min : H_B falsifiée.
  - Borne supérieure < Δ_min : H_A falsifiée.
  - Entre les deux : « non concluant », déclaré d'avance, avec un plafond de problèmes fixé.
- **Taille (illustrative)** : pour 0,30 contre 0,15, α = 0,05 bilatéral et puissance 0,8, l'approximation pour deux proportions donne n ≈ 7,84 × (0,21 + 0,1275) / 0,0225 ≈ 118 problèmes. L'appariement peut réduire ce nombre ; un pilote de 30 problèmes servira à estimer la corrélation intra-problème.

### E5 — Attribution : interaction ou volume filtré ?

- **H_A** : le gain vient de l'interaction (critique croisée, sélection entre agents divers).
- **H_B** : le gain vient du nombre d'échantillons et du filtrage par vérificateur.
- **Bras, tous à coût égal** :
  1. système complet ;
  2. système sans critique, jetons de critique réalloués à la génération ;
  3. système sans diversité de modèles (même modèle, plusieurs persona) ;
  4. modèle unique best-of-N avec le même vérificateur et la même règle de sélection.
- **Issues (seuil illustratif)** :
  - Si le bras 4 récupère ≥ 80 % du gain de E4 : H_A falsifiée pour la composante « interaction ».
  - Si le retrait de la critique fait perdre ≥ 50 % du gain alors que le bras 4 en récupère ≤ 20 % : H_B falsifiée.

### E6 — Fuite par rétroaction

- **H_A** : renvoyer au générateur la validité et la profondeur sur K_train ne gonfle pas la mesure.
- **H_B** : le système sur-apprend K_train (Goodhart ; Manheim & Garrabrant, 2018, « Categorizing Variants of Goodhart's Law », prépublication arXiv, identifiant à vérifier).
- **Métrique** : écart d(K_train) − d(K_test), avec et sans rétroaction.
- **Contrôle** : même système sans aucune rétroaction.
- **Issues** :
  - Si l'écart avec rétroaction dépasse l'écart sans rétroaction de plus d'un seuil préenregistré : H_A falsifiée, et le signal concerné passe en « retenu ».
  - Sinon : H_B falsifiée pour ce signal.

### E7 — Rétrodiction : trouvé ou rappelé ?

- **H_A** : les succès en rétrodiction reflètent une recherche.
- **H_B** : ils reflètent un rappel de données d'entraînement.
- **Dispositif** : modèles à données d'entraînement publiées (voir (d)). On recherche par n-grammes et par embeddings, dans le corpus, l'idée cible et ses paraphrases canonicalisées.
- **Métrique** : taux de succès sur cibles absentes du corpus contre cibles présentes.
- **Issues** :
  - Si les succès se concentrent sur les cibles présentes (rapport ≥ 3, illustratif) : H_A falsifiée pour ce dispositif.
  - Si les taux sont égaux et non nuls sur les cibles absentes : H_B falsifiée.
- **Limite** : impossible à faire avec des modèles dont les données sont fermées.

### E8 — Choix des régions

- **H_A** : une règle de choix de régions, préenregistrée et fondée sur un pilote, augmente le rendement en étroit-profond. Exemple de règle : faible couverture sous Q mais vérificateur dense.
- **H_B** : elle ne fait pas mieux que des régions tirées au hasard.
- **Dispositif** : apprendre la règle sur des régions de développement, puis l'évaluer sur des régions tenues à l'écart, contre un tirage aléatoire de même taille.
- **Contrôle** : la règle appliquée à des étiquettes de régions permutées.
- **Issues** : gain sur l'ensemble tenu à l'écart ≥ seuil, sinon H_A falsifiée. Sous permutation, le gain doit disparaître, sinon la règle capte un artefact.

---

## (c) Instruments : la mesure minimale qui dit s'ils fonctionnent

| Instrument | Cas honnêtes appariés | Détection / fausses alertes visées (illustratif) | Vérification mécanique à battre |
|---|---|---|---|
| **Juge LM** (si inévitable) | Même idée rédigée dans le style de la famille du générateur et dans celui d'une autre famille, puis paraphrasée par une troisième famille. Paires vraie/fausse de même complexité dans les mondes plantés. | Écart d'auto-préférence mesuré et rapporté comme borne du biais (≤ 0,05 visé). Rang du juge vs vérité plantée : AUC ≥ 0,8. | Régression logistique sur longueur + distance d'embedding au corpus + complexité syntaxique. Si le juge ne la bat pas, il est retiré. Il doit venir d'une autre famille que le générateur et être aveugle à la source. |
| **Estimateur d'étroitesse** | (i) Grammaire formelle où P_Q est calculable exactement (énumérateur pondéré). (ii) Paraphrases d'une idée commune, qui doivent rester « communes ». | Corrélation de rang estimation/vérité ≥ 0,9 en (i). Taux de paraphrases comptées comme nouvelles ≤ 0,02 en (ii). | Déduplication exacte de chaînes, puis forme normale (simplification symbolique, normalisation d'AST). La canonicalisation doit faire au moins aussi bien. |
| **Mesure de profondeur** | Loi plantée vraie contre loi de même complexité à constante perturbée. Lemme utile contre lemme de même longueur jamais utilisable. | Sensibilité ≥ 0,8 et fausses alertes ≤ 0,05 sur K_test. | Score de complexité seule (longueur, profondeur d'arbre). Si ce score prédit d aussi bien, d mesure la complexité et non la conséquence. |
| **Vérificateur de preuve formelle** (Lean 4 + Mathlib ; The mathlib Community, 2020, CPP, « The Lean Mathematical Library ») | Preuves correctes contre preuves contenant `sorry`, des axiomes ajoutés ou une tactique non sûre. | 0 acceptation de preuve avec axiome hors liste blanche (`#print axioms`). | Rejet syntaxique de `sorry`. **Le vérificateur ne contrôle pas la fidélité de l'énoncé** : audit humain d'un échantillon d'énoncés, taux de mésformalisation rapporté. |
| **Tests exécutables** | Solutions correctes contre mutants plantés. | Taux de mutants tués ≥ 0,9. Solutions correctes rejetées ≤ 0,01. | Tests fournis seuls, sans mutants. Il faut montrer que le jeu de tests distingue mieux que la couverture de lignes. |
| **Coupure temporelle (rétrodiction)** | Cibles certifiées présentes dans le corpus contre certifiées absentes (modèles à données ouvertes). | Détecteur de contamination : sensibilité ≥ 0,9 sur les présentes, fausses alertes ≤ 0,05 sur les absentes. | Recherche exacte de n-grammes. Si l'on ne peut pas la faire (données fermées), la coupure n'est pas un instrument mais une déclaration. |
| **Ligne de base « aléatoire »** | — | Doit retrouver les idées plantées à la fréquence prédite par leur probabilité sous la grammaire (test d'ajustement). | N'est définie que dans un espace formel : sinon, à retirer. |
| **Énumérateur mécanique** | Idées plantées de rang d'énumération connu. | Temps jusqu'au premier succès conforme au rang. | Comparaison possible à PySR pour la régression symbolique (Cranmer, 2023, « Interpretable Machine Learning for Science with PySR and SymbolicRegression.jl », prépublication arXiv, identifiant à vérifier). Antécédents : Schmidt & Lipson, 2009, *Science* 324 ; Udrescu & Tegmark, 2020, *Science Advances* 6(16), « AI Feynman ». |
| **Modèle unique le plus fort** | — | Choisi par une règle préenregistrée sur des problèmes de développement disjoints. | Doit être évalué avec le même vérificateur et la même sélection (bras 4 de E5). Sinon la comparaison avantage le système. |

---

## Réponses aux huit points

Pour chaque point : confiance entre 0 et 1, ce qui est établi, ce qui est conjecture.

**1. Cible — confiance 0,6.**
- *Établi* : un juge LM peut présenter un biais d'auto-préférence (RAPPORTÉ : Zheng et al., 2023 ; Panickssery et al., 2024).
- *Conjecture* : les définitions opérationnelles proposées :
  - n = −log P_Q(c(x)) relativement à Q nommé ;
  - d = gain contrefactuel d'un solveur figé sur K_test, moins le gain d'un contrôle de même complexité ;
  - la rareté se distingue de la profondeur par E3 et par le contrôle « fausse idée de même complexité ».
- *Biais du juge* : borné par l'écart mesuré sur des paires de style croisé, et jamais utilisé pour la quantité primaire si une mesure mécanique existe.
- *Cadrage* : la référence doit être plurielle (E2).

**2. Sources de vérité — confiance 0,65.**

| Source | Peut établir | Ne peut pas établir | Mode d'échec |
|---|---|---|---|
| Mondes plantés | n et d exactement, par construction | Transfert au réel | Le concepteur plante ce que ses propres a priori jugent rare ; le générateur peut partager ces a priori. |
| Rétrodiction à coupure | Pertinence réelle | Étroitesse non contaminée (sauf données ouvertes) ; profondeur hors du récit historique | Contamination ; biais de survivance dans le choix des cibles ; n minuscule. |
| Preuve formelle | Validité exacte ; profondeur par usage aval dans une bibliothèque (lemmes débloquant des cibles sous budget fixé) | Que l'énoncé dise ce qu'on croit | Mésformalisation ; lemmes valides mais triviaux. |
| Tests exécutables | Validité comportementale | Généralité | Couverture insuffisante ; piratage de récompense. |
| Autre : prédictions prospectives | Seule source sans contamination possible | — | Lente, avec peu d'échantillons. |

- *Conjecture* : aucune source ne suffit seule. Il faut au moins un monde planté et un domaine réel (formel), avec une vérification de transfert : corrélation des classements des systèmes entre sources.

**3. Comparaison — confiance 0,7.**
- Le dispositif est celui de E4 : quantité primaire succ_C(p), unité = problème, comptabilité complète des coûts, règle séquentielle préenregistrée contre l'enveloppe des lignes de base.
- L'attribution passe par E5.
- *Établi* : l'estimateur sans biais de pass@k (Chen et al., 2021, « Evaluating Large Language Models Trained on Code », prépublication arXiv, identifiant à vérifier) s'applique à succ_C quand on échantillonne plus de runs que nécessaire.
- *Conjecture* : l'effet attendu et la taille d'échantillon (illustratifs).

**4. Choix des problèmes — confiance 0,4.**
- *Conjecture* : les régions à faible couverture sous Q mais à vérificateur dense seraient plus fertiles.
- La recherche par nouveauté et l'illumination de l'espace offrent des outils, sans garantie : Lehman & Stanley, 2011, *Evolutionary Computation* 19(2), « Abandoning Objectives » ; Mouret & Clune, 2015, « Illuminating search spaces by mapping elites », prépublication arXiv, identifiant à vérifier. FunSearch (Romera-Paredes et al., 2024, *Nature* 625, « Mathematical discoveries from program search with large language models ») montre des trouvailles dans des régions à évaluateur rapide. C'est RAPPORTÉ, et cela ne dit rien de l'étroitesse au sens d'ici.
- Le choix se teste par E8, jamais en le supposant.
- *Établi (théorique)* : il n'existe pas de règle de choix universellement meilleure en moyenne sur tous les problèmes (Wolpert & Macready, 1997, *IEEE Trans. Evol. Comp.* 1(1), « No Free Lunch Theorems for Optimization »). Toute règle doit donc être validée sur une distribution de problèmes nommée.

**5. Rétroaction — confiance 0,6.**
- *Peut être renvoyé* :
  - validité mécanique (preuve acceptée, tests d'entraînement) ;
  - coût consommé ;
  - profondeur sur K_train, sous réserve de E6.
- *Doit être retenu* :
  - l'étroitesse n (la renvoyer transforme Q en adversaire et mesure l'évitement de Q, pas la découverte) ;
  - K_test ;
  - les tests tenus à l'écart ;
  - toute sortie du juge.
- *Règle* : tout ce qui entre dans la quantité primaire est calculé sur des données jamais exposées.
- *Conjecture* : renvoyer la validité seule ne fausse pas la mesure. Testable par E6.

**6. Validation du harnais — confiance 0,7.**
- Avant tout run coûteux, le harnais doit passer cinq épreuves :
  - E1, détection contre leurres et permutation ;
  - la ligne « estimateur d'étroitesse » de (c), calibration sur grammaire exacte et invariance aux paraphrases ;
  - E2, dépendance à la référence ;
  - le test A/A de E4 ;
  - une analyse de puissance sur pilote.
- Le harnais doit aussi montrer que chaque instrument bat sa vérification mécanique.
- E6 n'est réalisable qu'avec le système : c'est la limite de P10.

**7. Plan — confiance 0,6 sur l'ordre, 0,3 sur les tailles (illustratives).**

| Phase | Contenu | Arrêt si | Taille (illustratif) |
|---|---|---|---|
| 0 (CPU) | Grammaires, canonicalisation, mondes plantés, préenregistrement | Canonicalisation incapable de fusionner ≥ 98 % des paraphrases | — |
| 1 | E1 avec un petit modèle ouvert | Sensibilité < 0,8 ou fausses alertes > 0,05 : revoir les instruments | 200 positifs, 600 leurres |
| 2 | E2 + E3 | ρ inter-Q ≤ 0,3 : passer aux affirmations indexées par Q, sans arrêter | 30 000 tirages × 20 problèmes × 3 Q |
| 3 | Test A/A + pilote | Faux positifs A/A au-dessus du nominal : arrêt | 30 problèmes × 5 graines |
| 4 | E7 (contamination) sur modèles à données ouvertes | Détecteur sous les seuils de (c) : la rétrodiction est retirée du plan | ~100 cibles présentes et 100 absentes |
| 5 | E4 séquentiel | Arrêt pour efficacité ou futilité aux analyses intermédiaires | ~120 problèmes, jusqu'à 200 au plafond |
| 6 | E5 + E6 | Seulement si E4 conclut H_A | Mêmes problèmes, 4 bras |
| 7 | E8, puis prédictions prospectives | E8 nul : on abandonne le choix ciblé | Régions dév/test 50/50 |

- *Établi* : la règle de trois et la formule de taille pour deux proportions sont des calculs standards.
- *Conjecture* : les effets supposés.

**8. Limites — confiance 0,55.**
- *Hors de portée* :
  - la conséquence réelle à long terme ;
  - l'étroitesse relativement à « toute la recherche humaine » ;
  - les idées dont la conséquence échappe à tout vérificateur formalisable ;
  - la distinction trouver/rappeler avec des modèles à données fermées.
- *Preuve que la cible est mal posée* : E2 donne ρ ≤ 0,3 entre références raisonnables, **et** l'instabilité persiste sous changement de canonicalisation. « Étroit » n'est alors qu'un artefact de Q.
- *Preuve que le harnais est infaisable* :
  - E1 échoue malgré des instruments améliorés, c'est-à-dire que la surface explique les scores ;
  - ou bien les classements des systèmes ne se transfèrent pas des mondes plantés au domaine formel (ρ ≈ 0) ;
  - ou bien la classe étroit ∧ profond reste vide sous toutes les références dans le domaine réel. On ne pourrait alors falsifier H_A de E4 qu'au sens trivial 0 = 0.
- *Cadrage* : la question cherche un harnais général. Je soutiens (HYPOTHÈSE) qu'on ne peut obtenir qu'un harnais par domaine × référence, et que l'affirmation défendable est locale.

---

## (d) Ancrage matériel (tous les chiffres sont illustratifs)

**Modèles ouverts.**
- *Pour l'étroitesse non contaminée*, des modèles à données d'entraînement publiées : famille OLMo (Allen AI) et Pythia (EleutherAI, ordre des données connu). Ils sont indispensables pour E7. Version exacte et corpus : référence à vérifier.
- *Pour les références Q et les agents* : Llama 3.1 (8B, 70B), Qwen2.5 (7B, 72B, variantes mathématiques), distillations DeepSeek-R1. Le choix final du « plus fort » se fait par une règle préenregistrée.
- *Juge éventuel* : une famille absente du système.

**Outils.** vLLM pour l'inférence, Lean 4 + Mathlib, PySR pour l'énumérateur symbolique, bac à sable d'exécution pour les tests.

**Calcul (estimation grossière, illustratif).**

| Poste | Hypothèses | Volume | GPU | Coût |
|---|---|---|---|---|
| Phase 2 | 30 000 tirages × 20 problèmes × 3 Q × ~1 000 jetons ; débit agrégé d'un modèle 7–8B sur un H100 de l'ordre de 10⁴ jetons/s | ≈ 1,8·10⁹ jetons | ≈ 50 h | ≈ 100–250 $ à 2–5 $/h |
| Phase 5 | 120 problèmes × 5 bras × 5 graines × 2·10⁶ jetons, majoritairement avec un 70B à ~10³–2·10³ jetons/s sur 4 GPU | 6·10⁹ jetons | ≈ 3 000–7 000 h | ≈ 10⁴–3·10⁴ $ |
| Phase 6 | Ordre de la phase 5 | — | — | — |
| Vérification Lean et tests | Surtout CPU ; non négligeable en temps mural, faible en coût | — | — | — |
| Humain | Audit de fidélité de ~200 énoncés formalisés et de ~100 cibles de rétrodiction | — | — | ≈ 2–4 semaines-personne |

**Ce qui réfute le plus tôt et au moindre coût.** Les phases 0 à 3 coûtent moins de 1 % du total illustratif. Elles peuvent falsifier, avant toute dépense lourde :
- l'instrument de mesure (E1) ;
- la bonne pose de la cible (E2) ;
- la calibration du protocole (A/A).

FIN-DE-CELLULE