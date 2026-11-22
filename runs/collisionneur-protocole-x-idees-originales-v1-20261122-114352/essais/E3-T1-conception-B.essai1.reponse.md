# Proposition B · Tour III.1 · conception ciblée, à l'aveugle

## 0. État des pièces

- Les blocs FAITS et QUESTION ont un contenu identique et annoncent la même empreinte sha256. Je ne l'ai pas recalculée : elle reste **non vérifiée**.
- Le bloc FAITS ne contient **aucun fait muni d'un statut**. Il ne contient que le texte de la question. Aucune donnée empirique n'est donc transmise. Tout ce qui suit est HYPOTHÈSE, dérivation mathématique ou référence RAPPORTÉE de mémoire, avec sa certitude.
- L'identifiant « réponse 05c72e05… » est tronqué. Je n'en reconstitue pas le contenu.
- Aucune autre proposition n'est visible à ce tour : la règle B1 est sans objet ici.
- La question fixe cinq points (Q1 à Q5) et le tour fixe quatre livrables, (a) à (d). Je suis la structure (a) à (d) et je renvoie explicitement à Q1–Q5 aux endroits concernés.

---

## 1. (a) Ce que la question suppose sans que ce soit établi

| # | Présupposé | Statut | Conséquence s'il est faux |
|---|---|---|---|
| P1 | Les idées se rangent en **classes d'équivalence** décidables (on sait quand deux idées sont « la même »). | HYPOTHÈSE | Sans canonisation, « rarement proposée » n'a pas de sens. En texte libre, chaque formulation est unique et tout paraît rare. |
| P2 | La rareté « pour le système » est une propriété stable. | HYPOTHÈSE | Elle dépend de l'invite, de la température, de l'ordre des appels et des modèles inclus. Elle n'est définie que **relativement à un générateur de référence figé**. |
| P3 | La fiabilité du contrôle, établie sur des cas d'essai à vérité connue, **se transfère aux idées rares**. | HYPOTHÈSE (la question l'affirme pour les cas d'essai seulement) | Les idées rares sont probablement hors de la distribution de calibrage. Leur taux de faux positifs peut être plus élevé, ce qui fait gonfler les fausses découvertes justement dans la sous-population visée. |
| P4 | « Indépendant des modèles » implique des **erreurs du contrôle non corrélées** à celles du générateur. | HYPOTHÈSE | Si le contrôle a été conçu à partir des idées fréquentes du domaine, ses angles morts peuvent coïncider avec la queue de la distribution. |
| P5 | Les « appels indépendants » le sont statistiquement (pas de cache, de graine fixe ni de contexte partagé). | Inconnu, et la question le dit | Une convergence apparente peut venir d'un artefact d'infrastructure. |
| P6 | Le support du système contient des idées **à la fois vraies et rares**. | HYPOTHÈSE | Si ce n'est pas le cas, le taux est nul quelle que soit l'intervention. On peut seulement déplacer de la masse, pas créer du vrai hors support. |
| P7 | Les « fausses découvertes » sont mesurables. | HYPOTHÈSE | Sans vérité terrain indépendante du contrôle, on ne mesure que le **désaccord avec le contrôle**, pas l'erreur. |
| P8 | Le « coût total » s'exprime dans une unité commune à la génération et au contrôle. | HYPOTHÈSE | Le contrôle peut dominer le coût. Augmenter la génération réduit alors mécaniquement le nombre d'idées contrôlées. |
| P9 | Rare pour le système veut dire original pour le monde. | HYPOTHÈSE, probablement fausse en général | Une idée rare pour un modèle peut être banale dans la littérature. La question ne demande pas cette équivalence, mais le mot « originales » du titre la suggère. |
| P10 | Le contrôle produit une sortie graduée (score, p-valeur) et pas seulement un verdict binaire. | HYPOTHÈSE | Les procédures de contrôle du taux de fausses découvertes (FDR) exigent des p-valeurs valides. |

---

## 2. Réponse à Q1 : mesurer rareté et valeur sans juge-modèle

**Rareté (HYPOTHÈSE de méthode)**

1. **Canonisation mécanique C.** Selon le domaine :
   - forme normale pour une formule (système de calcul formel) ;
   - équivalence fonctionnelle pour un programme (sorties identiques sur une batterie d'entrées fixée) ;
   - identifiant canonique pour une molécule.

   Là où aucune forme normale n'existe, la rareté n'est pas mesurable sans juge. C'est un résultat d'analyse, pas un échec (voir §6).
2. **Générateur de référence G₀ figé.** On fixe modèles, invite, température et nombre d'appels réellement indépendants N.
3. **Estimation.** On note n_c la fréquence de la classe c. Pour une idée isolée, p̂(c) = n_c / N.
   - La masse totale non observée s'estime par Good–Turing, f₁ / N (f₁ = nombre de classes vues une fois). Référence : I. J. Good, 1953, « The population frequencies of species and the estimation of population parameters », *Biometrika*. RAPPORTÉ, certitude élevée sur l'attribution.
   - Le nombre de classes s'estime par Chao1. Référence : A. Chao, 1984, « Nonparametric estimation of the number of classes in a population », *Scandinavian Journal of Statistics*. RAPPORTÉ, certitude élevée.
4. **Idée absente de l'échantillon de référence.** On n'a qu'une borne supérieure : p ≤ −ln(0,05)/N ≈ 3/N à 95 %. C'est une dérivation (règle de trois), pas un chiffre empirique.
5. **Échantillons disjoints obligatoires.** La rareté s'estime sur un échantillon de référence séparé de celui où l'on sélectionne. Sinon une idée retenue *parce qu'elle* est apparue une fois voit sa rareté biaisée par la sélection (malédiction du gagnant).

**Valeur (HYPOTHÈSE de méthode)**

- Valeur minimale : verdict positif du contrôle O, **corrigé par les caractéristiques opératoires de O mesurées dans la strate de rareté** de l'idée (voir E1).
- Option plus stricte : « non triviale », c'est-à-dire non équivalente (par C) à une classe fréquente ni impliquée par une combinaison de classes fréquentes, lorsque le domaine permet de tester l'implication mécaniquement.
- Ce que cela ne mesure pas : l'originalité par rapport au monde (P9). Sur un modèle à corpus d'entraînement ouvert, on peut au mieux tester mécaniquement la présence de la forme canonique dans ce corpus.

---

## 3. (b) Expériences décisives (inférence forte)

**Socle commun.** Le FDR n'est mesurable (P7) que sur deux types de terrain :
- **(i) des mondes à vérité plantée** : domaines synthétiques où la vérité de chaque idée est connue par construction (loi cachée dans un simulateur, fonction cachée, programme cible) et où l'on a délibérément placé des vérités de faible probabilité sous G₀ ;
- **(ii) un domaine réel à contrôle exact** (constructions combinatoires vérifiables, programmes jugés sur tests cachés exhaustifs), qui sert de réplication.

Tous les seuils ci-dessous sont **illustratifs**. Ils sont à préenregistrer avant toute collecte.

### E0 · Les appels indépendants convergent-ils ? (préalable : décide si « rare » est discriminant)

- **H_A** : la masse non observée Û(N) = f₁/N tombe sous ε pour un budget N atteignable. La rareté est alors une queue mesurable.
- **H_B** : Û(N) reste au-dessus de ε. Presque tout est « rare » à ce budget.
- **Métrique** : Û(N) et courbe de raréfaction (nombre de classes en fonction de N), avec intervalle par bootstrap sur les appels.
- **Seuil** : ε = 0,05 à N = 10⁴ (illustratif).
- **Contrôles** :
  - négatif : un générateur aléatoire non-LLM, à grammaire uniforme sur le même espace canonique, doit rester en H_B ;
  - positif : un générateur forcé à répéter doit tomber en H_A ;
  - infrastructure : relancer avec une graine identique doit reproduire la sortie (en local), relancer avec des graines différentes ne doit pas reproduire au-delà de l'attendu (sinon il y a un cache).
- **Falsification** :
  - si Û ≤ ε avec intervalle sous ε, H_B est falsifiée ;
  - si l'intervalle de Û est entièrement au-dessus de ε, H_A est falsifiée. Dans ce cas, la question doit être reposée : la rareté n'est pas informative à ce budget et le critère se ramène à « classe nouvelle et confirmée ».
- **Dépendance** : E0 n'a de sens que si C est validé (§4). Un canoniseur qui fusionne trop fabrique un faux H_A.

### E1 · Le contrôle reste-t-il fiable dans la queue ? (décide si viser la rareté gonfle les fausses découvertes)

- **H_A** : FPR_O(strate rare, p̂ ≤ τ) ≤ FPR_O(cas d'essai) + δ, et TPR_O(rare) ≥ TPR_O(essai) − δ.
- **H_B** : le FPR est plus élevé dans la strate rare, au-delà de δ.
- **Métrique** : FPR et TPR par strate de rareté (définie sur l'échantillon de référence G₀), intervalle de confiance à 95 %, sur les mondes plantés où la vérité est connue.
- **Seuil** : δ = 0,02 ; τ = 10⁻³ (illustratifs). Taille par strate calculée pour que la demi-largeur de l'intervalle soit inférieure à δ/2.
- **Contrôle négatif : leurres appariés.** Pour chaque idée vraie rare, on construit une variante fausse par perturbation minimale (une constante, un signe, une condition), de même longueur et de même strate. O doit rejeter les leurres au même taux que les faux cas d'essai.
- **Falsification** :
  - si la borne inférieure de l'intervalle sur FPR_rare − FPR_essai dépasse δ, H_A est falsifiée. Toute intervention qui « augmente les rares » augmente alors mécaniquement les fausses découvertes, sauf réplication indépendante (I6) ;
  - si l'intervalle entier est sous δ, H_B est falsifiée.

### E2 · Gabarit à coût égal, appliqué à chaque intervention I contre une base B₀

- **Grandeur visée, Y** : nombre de classes canoniques distinctes c telles que :
  - p̂_G₀(c) ≤ τ, mesurée sur l'échantillon de référence figé et disjoint (jamais sur la distribution de I, ce qui serait trivialement satisfaisable) ;
  - c est confirmée par O ;
  - c est vraie selon la vérité plantée ou le contrôle exact.
- **Coût** : unité unique, tokens générés + appels à O convertis en temps de calcul (P8). Le budget est identique pour I et B₀.
- **H_A** : Y_I ≥ (1 + r)·Y_B₀ et FDR_I ≤ FDR_B₀ + δ.
- **H_B** : non (pas de gain, ou FDR dégradé).
- **Seuils** : r = 0,2 ; δ = 0,02 ; au moins 5 graines indépendantes et instances de problèmes tirées au hasard (illustratifs).
- **Contrôles négatifs** :
  1. **vérification mécanique à battre** : un générateur aléatoire non-LLM au même coût. Si l'aléatoire fait aussi bien, le système multi-modèles n'apporte rien sur ce domaine ;
  2. **placebo** : une invite reformulée sans contenu nouveau.
- **Falsification** :
  - H_A est falsifiée si la borne supérieure de l'intervalle sur Y_I/Y_B₀ est sous 1 + r, ou si la borne inférieure sur FDR_I − FDR_B₀ dépasse δ ;
  - H_B est falsifiée si les deux conditions de H_A tiennent sur les mondes plantés **et** se répliquent sur le domaine réel.

### Interventions candidates (Q2) et critère d'abandon (Q3)

Chaque intervention passe par E2, plus un duel spécifique quand elle repose sur un mécanisme propre.

**I1 · Générateurs de base (non alignés) au lieu de versions instruites**
- *Garantit* : rien par construction.
- *Hypothèse* : l'alignement par préférences réduit la diversité des sorties.
- *Indice pour* : R. Kirk et al., 2024, « Understanding the Effects of RLHF on LLM Generalisation and Diversity », ICLR. RAPPORTÉ ; certitude moyenne sur le détail des résultats, élevée sur l'existence et le thème.
- *Indice contre* : les modèles de base produisent davantage de sorties hors format, donc davantage d'appels à O gaspillés à coût égal. Référence à vérifier.
- *Abandon* : E2 falsifie H_A sur les deux terrains.

**I2 · Hétérogénéité des familles de modèles plutôt qu'un modèle répété**
- *Duel spécifique.* H_A : la masse partagée entre supports canoniques de familles différentes est inférieure à la masse partagée entre graines d'une même famille. H_B : elle est supérieure ou égale.
- *Métrique* : recouvrement pondéré par les fréquences (somme des min(p_i, p_j)).
- *Indice pour* : HYPOTHÈSE (corpus et recettes d'entraînement différents).
- *Indice contre* : forte part de corpus communs, convergence plausible. Référence à vérifier.
- *Abandon* : le rapport inter/intra a un intervalle contenant 1 et une borne supérieure inférieure à 1,1 (illustratif), **et** E2 ne montre pas de gain. Si les familles convergent, payer plusieurs modèles ne sert à rien.

**I3 · Exclusion des modes**
- *Mécanisme* : rejet à l'échantillonnage des classes déjà fréquentes (via C), ou liste d'exclusion dans l'invite.
- *Garantit* : par construction, et seulement en version rejet mécanique, moins de répétitions dans la sortie.
- *Ne garantit pas* : que la masse déplacée tombe sur du vrai.
- *Risque* : migration vers une queue fausse.
- *Duel spécifique.* H_A : parmi les rares produites par I3, la proportion de vraies est au moins celle observée parmi les rares produites naturellement par G₀. H_B : elle est plus faible.
- *Abandon* : la borne supérieure de l'intervalle sur la différence est négative, au-delà de δ.

**I4 · Température plus élevée / échantillonnage sans troncature**
- *Garantit* : mécaniquement, plus de masse sur la queue.
- *Ne garantit pas* : de la vérité dans la queue.
- *Indice contre* : dégradation de la cohérence à haute température. Référence à vérifier.
- *Abandon* : comme E2. On note en plus le point où Y décroît en fonction de la température.

**I5 · Boucle évolutive avec retour du contrôle**
- *Indice pour* : B. Romera-Paredes et al., 2024, « Mathematical discoveries from program search with large language models », *Nature* (FunSearch). RAPPORTÉ ; certitude élevée sur l'attribution. Limite : l'évaluateur y est programmatique et exact. Ce travail ne renseigne donc pas sur le FDR avec un contrôle imparfait.
- *Indice contre* : suroptimisation contre un évaluateur imparfait. L. Gao, J. Schulman, J. Hilton, 2023, « Scaling Laws for Reward Model Overoptimization », ICML. RAPPORTÉ ; certitude moyenne-élevée. C'est une analogie : ce travail porte sur des modèles de récompense appris, pas sur un contrôle externe.
- *Duel spécifique.* H_A : les idées confirmées par O issues de la boucle se répliquent sur un contrôle O′ tenu à l'écart (jamais vu par la boucle) au même taux que les confirmées de B₀. H_B : leur taux de réplication est plus bas (effet Goodhart).
- *Abandon* : la borne inférieure de l'écart de réplication dépasse δ.

**I6 · Allocation du budget de contrôle**
- *Mécanisme* : filtre mécanique bon marché, puis O avec contrôle du FDR sur des p-valeurs, puis réplication des rares sur O′.
- *Garantit* : FDR ≤ α sous indépendance ou dépendance positive des p-valeurs (Y. Benjamini, Y. Hochberg, 1995, « Controlling the false discovery rate: a practical and powerful approach to multiple testing », *JRSS B*), et sous dépendance arbitraire avec la correction de Y. Benjamini, D. Yekutieli, 2001, « The control of the false discovery rate in multiple testing under dependency », *Annals of Statistics*. RAPPORTÉ ; certitude élevée sur ces deux attributions.
- *Ne garantit pas* : la **validité** des p-valeurs de O dans la strate rare. On revient à E1 et à P10.
- *Seule intervention qui vise directement* « sans augmenter les fausses découvertes ».
- *Abandon* : le FDR empirique sur les mondes plantés dépasse α + δ (borne inférieure de l'intervalle).

**Interaction à tester explicitement.** I3 et I4 *produisent* de la rareté ; I6 *protège* le FDR. L'hypothèse que je juge la plus risquée, et donc la plus informative, est la suivante : **I4 + I6 bat I4 seul et B₀** sur Y à coût égal. Elle est falsifiée si le coût de la réplication imposée par I6 réduit le nombre de candidats contrôlés au point que Y_{I4+I6} ≤ Y_B₀.

---

## 4. (c) Instruments nommés par la question : mesure minimale de fonctionnement

| Instrument | Détection | Fausses alertes | Cas honnêtes appariés | Vérification mécanique à battre | Seuil minimal (illustratif) |
|---|---|---|---|---|---|
| **Contrôle indépendant O** | TPR sur idées vraies, par strate de rareté | FPR sur idées fausses, par strate | Paires (vraie, leurre minimalement perturbé) appariées en longueur, domaine et strate ; les strates rares sont **obligatoires** | « Accepter tout ce qui passe la vérification syntaxique » et « accepter tout ce qui passe les exemples publics » | O bat les deux de ≥ 0,1 en score de Youden **dans la strate rare** ; sinon O n'apporte rien là où on l'utilise |
| **Canoniseur C** (pour compter « rarement ») | Rappel des doublons sur paires équivalentes construites par transformations neutres déterministes (renommage, réordonnancement, gabarits de paraphrase) | Taux de fusions abusives sur paires quasi identiques mais non équivalentes (une constante qui change le comportement) | Paires équivalentes et non équivalentes de même longueur, tirées des sorties réelles de G₀ | Égalité exacte après normalisation ; MinHash sur n-grammes | Rappel ≥ 0,95 et fusions abusives ≤ 0,01 ; si C ne bat pas MinHash, on utilise MinHash |
| **Estimateur de rareté** (p̂, Good–Turing, Chao1) | Couverture des intervalles de p̂ et de la masse non observée | Proportion d'idées classées « rares » alors que leur vraie probabilité est > τ | Générateur simulé à loi connue (par exemple de type Zipf) sur le même espace canonique | Fréquence brute sans correction | Couverture empirique dans [0,93 ; 0,97] pour un nominal de 0,95 |
| **Indépendance des appels** (inconnue, P5) | Taux de sorties identiques sous graines différentes, comparé au taux attendu sous G₀ estimé | Signalement de dépendance alors que l'exécution locale est contrôlée | Mêmes invites rejouées en local (graines maîtrisées) et via l'interface du fournisseur | Hachage exact des sorties | Écart non significatif entre local et fournisseur ; sinon les appels ne sont pas indépendants et E0 est invalide |
| **Compteur de fausses découvertes** | FDR estimé (par exemple par leurres, dans l'esprit de R. F. Barber, E. J. Candès, 2015, « Controlling the false discovery rate via knockoffs », *Annals of Statistics* ; RAPPORTÉ, certitude élevée sur l'attribution, l'adaptation ici est une HYPOTHÈSE) | Écart entre FDR estimé et FDR réel | Mondes plantés où le FDR réel est connu | Estimation naïve « 1 − précision sur cas d'essai » | Écart \|FDR estimé − réel\| ≤ δ |
| **« Jugement d'un modèle »** (exclu par la question, utile comme comparateur) | Accord avec la rareté mécanique et la vérité plantée | Classements « original » de leurres ou d'idées fréquentes | Mêmes paires que pour C et O | C + O mécaniques | Si le juge ne bat pas C + O, l'exclusion ne coûte rien ; s'il les bat, l'exclusion a un coût à documenter |

Remarque : un plongement vectoriel produit par un modèle est un jugement de modèle déguisé. Je ne l'admets comme canoniseur que s'il bat MinHash sur les paires ci-dessus. Il reste dans ce cas un instrument validé, pas une vérité.

---

## 5. (d) Ancrage matériel (tous les chiffres sont illustratifs)

**Modèles ouverts**
- Llama 3.1 8B et 70B, base et instruit ;
- Qwen2.5 7B et 72B, base et instruit ;
- Mistral 7B ;
- OLMo 2. Son corpus d'entraînement est public, ce qui permet de tester P9 mécaniquement (la forme canonique est-elle dans le corpus ?).

Les paires base/instruit servent I1, les familles différentes servent I2. Inférence locale (par exemple vLLM), indispensable pour maîtriser les graines (P5). Existence et disponibilité de ces modèles : RAPPORTÉ, de mémoire, certitude élevée.

**Domaines**
- (i) mondes à vérité plantée : lois cachées dans un simulateur, fonctions cachées, avec vérités de faible probabilité délibérément placées ;
- (ii) synthèse de programmes jugée sur tests cachés exhaustifs ;
- (iii) constructions combinatoires vérifiables exactement.

**Calcul (illustratif)**
- Échantillon de référence G₀ : 10⁵ générations × 300 tokens ≈ 3·10⁷ tokens par générateur.
- Sur un modèle 8B, avec un débit agrégé de l'ordre de 2·10³ tokens/s sur un GPU de classe A100, cela fait environ 4 GPU-heures. Un 70B sur 4 GPU coûte un ordre de grandeur de plus.
- Plan complet : 6 bras (B₀, I1 à I5, plus combinaisons), 5 graines, 3 terrains, plus E0 et E1. Ordre de grandeur : quelques centaines à un millier de GPU-heures de génération.
- Coût de génération : de l'ordre de 10³ à quelques 10³ € à 2 €/GPU-heure.
- Le coût du contrôle O dépend du domaine. Il peut dominer, ce qui justifie l'unité de coût commune (P8).

**Mesure de E1**
- Environ 10³ leurres par strate et par terrain (illustratif) pour atteindre la demi-largeur visée.

---

## 6. Q4 : limites de principe

1. **Estimation de la rareté individuelle.** Good–Turing estime la masse *agrégée* des inobservés, pas la probabilité d'une idée inobservée en particulier. Distinguer p = 10⁻⁵ de p = 10⁻⁷ demande un N d'ordre 1/p (dérivation). La rareté fine coûte en proportion de son inverse.
2. **Support.** Une intervention redistribue la masse de G₀ ; elle ne crée pas de vérité hors du support atteignable (P6). La troncature (top-p, top-k) peut avoir mis du vrai à probabilité nulle ; la retirer (I4) le rend atteignable, mais ne le rend pas fréquent.
3. **Taux de base.** Si la proportion de vraies parmi les rares est π et le FPR de O est f, la proportion de fausses découvertes parmi les confirmées rares est minorée par f(1 − π) / (f(1 − π) + TPR·π) (Bayes, dérivation). Quand π est petit, même un f faible donne un FDR élevé. C'est la logique de J. P. A. Ioannidis, 2005, « Why most published research findings are false », *PLoS Medicine* (RAPPORTÉ, certitude élevée sur l'attribution). La réplication (I6) est alors la seule voie, et elle coûte.
4. **Horizon du contrôle.** On ne confirme que ce que O sait tester. Les idées vraies hors de son domaine de validité sont invisibles, donc comptées comme « non confirmées ». Le taux mesuré est borné par la couverture de O.
5. **Arbitrage budgétaire.** À coût total égal, chaque token de génération supplémentaire retire du budget de contrôle. Le rythme est borné par le débit de O dès que celui-ci domine le coût.
6. **Goodhart.** Toute boucle qui optimise contre O découvre aussi les erreurs de O (I5). Seul un contrôle tenu à l'écart permet de le mesurer.
7. **Rareté relative et originalité.** La rareté est relative à G₀. L'originalité dans le monde exige un corpus de référence, et ce test n'est pas mécanisable en général.

---

## 7. Q5 : le problème est-il mal posé ?

En partie, et pour des raisons précises :
- « rarement proposées » est indéfini sans P1 (canonisation) et sans générateur de référence figé (P2) ;
- « fausses découvertes » est indéfini sans vérité terrain au-delà du contrôle (P7) ;
- « à coût total égal » est indéfini sans unité commune (P8) ;
- « fiable sur cas d'essai » ne dit rien de la strate visée (P3).

**Reformulation proposée (HYPOTHÈSE de cadrage).**
On se donne :
- un générateur de référence G₀ figé ;
- un canoniseur C validé contre MinHash sur des paires appariées ;
- un contrôle O dont TPR et FPR sont mesurés **par strate de rareté** sur des mondes plantés ;
- un budget B dans une unité commune.

Le problème devient alors : quelle intervention I maximise l'espérance de Y (classes distinctes de probabilité sous G₀ au plus τ, confirmées par O et vraies), sous la contrainte FDR ≤ α, avec transfert du résultat des mondes plantés au domaine réel validé par réplication sur un contrôle exact ?

Si E0 montre que la masse non observée ne descend pas sous ε au budget accessible, on remplace « rare » par « nouvelle relativement à G₀ » : on garde la contrainte de vérité et on abandonne la gradation de rareté.

**Ce que je compte comme réfutable dans cette proposition**
- E0 peut invalider l'usage de la rareté ;
- E1 peut invalider l'idée qu'on peut viser la queue sans gonfler les fausses découvertes ;
- chacune des interventions I1 à I6 a un critère d'abandon chiffré (seuils illustratifs, à préenregistrer) ;
- le générateur aléatoire non-LLM peut invalider l'utilité du système multi-modèles sur un domaine donné.

FIN-DE-CELLULE