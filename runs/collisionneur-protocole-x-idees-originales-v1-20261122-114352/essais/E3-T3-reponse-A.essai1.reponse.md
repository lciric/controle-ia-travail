# Proposition A — Tour III.3 : réponse aux critiques

## 0. Constats d'intégrité

- **Bloc FAITS.** Il reproduit la question et ne contient aucun fait porteur de statut. Je ne recalcule pas l'empreinte. La source (« réponse 28 de Fable ») n'est pas transmise et son identifiant est tronqué.
- **Pièces.** Ma conception III.1 et les cinq critiques (B, C, D, E, F) sont présentes ; chacune se termine par sa ligne de clôture. Je ne réponds qu'aux sections « Sur la proposition A ».
- **Statuts.** C, D, E et F marquent des dérivations « VÉRIFIÉ ». Je ne change pas ces statuts ; aucun n'est adossé au bloc FAITS. Quand je m'appuie sur l'une d'elles, je dis que j'ai refait le calcul et sous quelles hypothèses. Mes corrections sont des HYPOTHÈSES de conception. Rien ci-dessous n'est un résultat.
- **Chiffres.** Aucun. Tous les seuils sont des paramètres à préenregistrer (q, τ, δ, ε, θ, α, n, K₀).

## (a) Verdict sur chaque critique

Un même défaut est souvent relevé par plusieurs critiques ; je nomme alors toutes les sources et je signale leurs divergences.

| # | Critique (sources) | Verdict | Conséquence |
|---|---|---|---|
| K1 | Sur le banc, κ à verdicts binaires fusionne toutes les inégalités vraies dans une seule classe (B, C, D, E, F). | **Acceptée.** | Défaut réel de ma conception : D2, D3 et D4 étaient vides sur ce banc. κ est redéfini en (b). |
| K2 | Le gain en « cas résolus » est nul ou sans objet pour des inégalités (D, E). | **Acceptée.** | La valeur devient un resserrement strict de borne, voir (b). |
| K3 | Mes paires négatives pour κ diffèrent sur une sonde : leur séparation est acquise par construction (D, F). | **Acceptée.** | Remplacées par des vraies distinctes plantées et des fausses indiscernables sur sondes. |
| K4 | Fuite entre les sondes de κ et les graphes de T (B, C, F). | **Acceptée.** | Ensembles de graphes disjoints et gelés ; contrôle T′ sur échantillon disjoint. |
| K5 | Tautologies rares dérivées de vraies fréquentes (E). | **Transformée en test** (E0-c). | |
| R1 | f₁/N est une masse agrégée et ne certifie pas la rareté d'une classe ; il faut un panel frais et une couverture simultanée (B, C, E, F). | **Acceptée.** | Certification par panel, voir (b). |
| R2 | Le panel P₀ et le bras de base peuvent se recouvrir (B, C, F). | **Acceptée.** | Trois tirages indépendants, déclarés. |
| R3 | Une classe absente du panel reçoit p̂ = 0 et devient « rare » gratuitement (F). | **Acceptée.** | Verdict à trois états : rare certifiée, non rare, indéterminée. |
| R4 | L'intervalle bootstrap sur f₁/N est biaisé vers le bas (F). | **Acceptée.** J'ai refait le calcul : sous rééchantillonnage multinomial, une classe vue k fois redevient singleton avec probabilité k(1−k/N)^(N−1). | Bootstrap retiré de D1. |
| R5 | La collision entre deux appels (Σp²) et la masse nouvelle sont deux quantités ; f₁/N ne vise que la seconde (D). | **Acceptée.** | D1 rapporte les deux. Une loi peut avoir à la fois un mode lourd et une queue ouverte : mon opposition « puits contre queue » n'était pas une dichotomie. |
| R6 | D1 non jugeable sous variance trop forte, corrélation intra-lot ou sous-fusion de κ (B). | **Acceptée.** | Conditions préenregistrées de non-jugeabilité. Je lis le terme de sous-fusion de B comme un majorant. |
| D2-1 | Le nul de D2 rend H_A presque acquise, et ma conclusion sur « le mode contient tout » ne s'en déduit pas (B, F). | **Acceptée.** | Phrase retirée ; D2 scindé. L'affirmation de B qu'une inégalité aléatoire est presque toujours fausse est une HYPOTHÈSE : je la mesure (π_nul). |
| D2-2 | Le rapport des taux est indéfini si le nul ne produit aucune vraie (D, F). | **Acceptée.** | Différence au lieu de rapport ; second nul par mutation. |
| D2-3 | Perdre D2 ne justifie pas d'abandonner toutes les interventions (D). | **Acceptée en partie**, voir sous le tableau. | |
| D2-4 | Auditer les singletons d'un échantillon privilégie les masses voisines de 1/N (E). | **Acceptée comme limite déclarée.** | D2 porte sur la queue pondérée par sa masse, seule atteignable par tirage (L1). |
| D3-1 | D3 comparait des proportions de fausses parmi les confirmées, pas les erreurs du contrôle (D). | **Acceptée.** | D3 scindé en D3a (erreurs conditionnelles) et D3b (proportion auditée). |
| D3-2 | Benjamini-Hochberg appliqué globalement laisse les vraies fréquentes masquer les fausses rares (E). | **Acceptée.** | Procédure appliquée à la seule famille des classes rares certifiées. |
| D3-3 | Plancher des p-valeurs conformes (C, E, F). | **C rejetée dans sa forme ; E et F acceptées**, voir sous le tableau. | |
| D3-4 | Les fausses de calibration ne sont pas échangeables avec les fausses rares, dont le contre-exemple serait d'ordre intermédiaire (C, E, F). | **Transformée en test** (D3a, monde nul en queue). Le mécanisme d'E est une HYPOTHÈSE : je mesure l'ordre du plus petit contre-exemple par strate. | |
| D3-5 | L'α-investing ne doit pas être crédité du FDR ordinaire (D). | **Acceptée.** | De mémoire, Foster et Stine (2008) bornent un rapport d'espérances (RAPPORTÉ, certitude moyenne). Retiré du garde-fou. |
| D4-1 | Le rapport de rendements est indéfini si R_base = 0 ; la puissance n'est pas dimensionnée (B, D, F). | **Acceptée.** | Contraste linéaire ; puissance simulée avant collecte. |
| I1-1 | I1 confond l'allocation et la liste d'exclusion (C). | **Acceptée.** | Plan factoriel. |
| I1-2 | Sous exclusion, f₁/N ne mesure plus rien (C, D, E). | **Acceptée.** | J'avais noté la perte d'indépendance sans en tirer la conséquence. Pilote changé ; test de la source saturée d'E adopté. |
| I2-1 | Issues non couvertes (D) ; recouvrement confondu par l'entropie, la profondeur de tirage et les échecs de syntaxe (F, D). | **Acceptée.** | Le recouvrement devient un diagnostic ; le duel porte sur le rendement. |
| I3-1 | Issue non couverte ; il faut un dialogue factice de même coût (D). | **Acceptée.** | |
| I4-1 | Une pente nulle est compatible avec un écart constant supérieur à δ (D, F). | **Acceptée.** | Critère de niveau, dès la première itération. |
| I4-2 | Il manque un second échantillon de petits graphes du même ordre (C). | **Acceptée.** | Il sépare le surajustement d'échantillon de la rupture entre ordres. |

**Sur D3-3.** C écrit que, dès que M_cal + 1 < K/q, le nombre de rejets est nul « quelle que soit la loi des scores ». Je rejette cette généralité par un contre-exemple. Si m₁ candidats atteignent ensemble la p-valeur minimale 1/(M_cal + 1), la procédure les rejette dès que 1/(M_cal + 1) ≤ m₁·q/K. La condition de C ne vaut donc que pour m₁ = 1. E et F donnent la forme avec m₁, que je retiens.

F ajoute le cas d'un atome au score maximal. Il s'applique à mon banc : T y est presque binaire, la p-valeur de tout candidat au score parfait vaut à peu près le taux de passage a₀ des fausses de calibration, et le garde-fou se réduit à un seuil sur a₀·K/m₁. Je le déclare : sur ce banc, la procédure n'apporte rien de plus fin que ce seuil.

**Sur D2-3.** D a raison sur un point : la prévalence sous P₀ ne borne pas ce qu'une recherche guidée peut atteindre. Je restreins donc la règle d'arrêt. Une défaite en D2 fait abandonner, pour la source concernée, les interventions qui rééchantillonnent sa queue : I1, I3 et sa contribution à I2. Elle ne condamne pas I4, qui sera jugée en D4 contre une boucle à mutation mécanique.

## (b) Expériences corrigées

### Banc révisé

- **Idées.** Ce sont des bornes supérieures d'un invariant cible fixé : « I(G) ≤ f(J₁(G), …, J_k(G)) pour tout graphe », avec f dans une grammaire fermée. La cible est isolée à gauche, ce qui retire les réécritures par changement d'échelle ou de membre.
- **Graphes.** Trois ensembles disjoints et gelés avant toute génération : S_κ (sondes), S_T (contrôle) et S_frais (confirmation). S'y ajoute S_T′, de même ordre que S_T et disjoint de lui. L'oracle reste l'énumération exhaustive jusqu'à un ordre supérieur.
- **Canoniseur κ.** La signature est le vecteur quantifié des valeurs de f sur S_κ. Deux bornes vraies distinctes ont des signatures distinctes dès qu'elles diffèrent sur une sonde.
  - *Limite assumée 1.* Le verdict sur S_κ est fonction de la classe. Il est compté comme une part du contrôle, pas comme une confirmation.
  - *Limite assumée 2.* Deux bornes égales sur les sondes et différentes ailleurs restent fusionnées. L'unité confirmée est donc le représentant soumis, et l'hétérogénéité de vérité dans une classe est auditée.
- **Valeur.** g(x) est le nombre de graphes de S_frais où f_x est strictement plus petite que le minimum des bornes fréquentes confirmées. Ce portefeuille fréquent est figé sur le panel P₀. Par construction, une combinaison convexe ou un maximum de bornes fréquentes obtient g = 0.
- **Rareté par classe.**
  - Un panel P₀ de n tirages frais, indépendant de tous les bras, n'est jamais montré à une intervention.
  - Chaque bras soumet au plus K₀ classes à la certification, K₀ étant identique entre bras et fixé d'avance. Un bras qui en confirme davantage est sous-échantillonné au hasard, puis son compte est extrapolé. La multiplicité ne pénalise donc pas le bras le plus productif.
  - Une classe est « rare certifiée » si sa borne binomiale supérieure, au niveau α divisé par le nombre total de classes testées K, est ≤ τ.
  - La certification exige n ≥ ln(K/α) / (−ln(1−τ)). En deçà, aucune classe n'est certifiable. τ se choisit donc avec n, pas librement.
- **Nuls mécaniques.** Deux générateurs : dérivation aléatoire dans la grammaire, et mutation d'un seul élément d'une borne fréquente confirmée.

### E0 — Instruments, avant tout tirage de modèle

- **Duel.** H_A : κ sépare K bornes vraies plantées, deux à deux non équivalentes, en K classes, et son taux de sous-fusion ε_s sur réécritures mécaniques reste sous un seuil préenregistré. H_B : au moins une fusion de vraies distinctes, ou ε_s au-dessus du seuil.
- **Matériel planté.** Des bornes démontrées de la littérature, à lister avec leur source avant gel (références à vérifier). La non-équivalence est attestée mécaniquement par un graphe où les valeurs diffèrent.
- **Contrôles négatifs.**
  - (a) Fausses indiscernables sur S_κ et distinguables ailleurs : elles mesurent la sur-fusion.
  - (b) T contre T′ : si l'instrument est sain, l'accord est inchangé ; s'il chute, la confirmation était héritée d'un échantillon.
  - (c) Tautologies d'E : elles doivent obtenir g = 0.
  - (d) Avec des vraies plantées au score parfait, aux mêmes M_cal, K et q, le garde-fou doit en rejeter.
- **Si H_B est retenue :** le banc est abandonné et rien en aval n'est exécuté. **Si H_A est retenue :** l'objection K1 est écartée pour ce κ, sur ce banc seulement.

### D1 — Les appels reviennent-ils aux mêmes classes ?

- **Tirages.** Par source, indépendants et sans exclusion, un appel par contexte.
- **Deux quantités rapportées.** Le taux de collision entre paires d'appels, et la masse nouvelle f₁/N.
- **Duel.** H_A : masse nouvelle au budget N < θ. H_B : ≥ θ.
- **Intervalles.** Ils viennent de réplications indépendantes, pas d'un bootstrap. Leur couverture est vérifiée sur un générateur synthétique à loi plate, puis à queue lourde. Une variance analytique existe peut-être (référence à vérifier).
- **Non jugeable si :** ε_s mesuré en E0 n'est pas petit devant θ, ou si la corrélation intra-lot estimée est positive sans correction.
- **Si H_B est falsifiée :** tirer davantage de cette source est abandonné. **Si H_A est falsifiée :** la saturation n'est pas le goulot de cette source.

### D2 — La queue apporte-t-elle quelque chose ?

- **Population.** Les classes du bras de base certifiées rares par le panel, auditées par l'oracle.
- **D2a, signal ou bruit.** H_A : π_rare − π_nul > 0, contre chacun des deux nuls. H_B : ≤ 0.
- **D2b, apport au mode.** Z est le nombre, par unité de coût, de classes rares certifiées, vraies selon l'oracle et de gain g > 0. H_A : Z_P₀ > Z_mutation. H_B : Z_P₀ ≤ Z_mutation.
  - Si H_B est falsifiée, la thèse « le mode et ses voisins mécaniques contiennent tout » tombe sur ce banc.
  - Si H_A est falsifiée, la règle d'arrêt restreinte s'applique.
- **Descriptif.** π par strate (rare, fréquente), avec permutation des étiquettes de rareté. C'est le contraste demandé par B ; il fournit le taux de base de L2.

### D3 — Transport du contrôle

- **D3a, erreurs conditionnelles.** Sur un échantillon aléatoire de classes proposées, confirmées ou non, l'oracle donne le taux de fausse confirmation a_s et la sensibilité t_s par strate.
  - H_A : a_rare − a_fréq ≤ δ et t_fréq − t_rare ≤ δ. H_B : l'un des deux écarts dépasse δ.
  - Contrôle de D : rééchantillonner pour changer la seule prévalence. D3a doit rester stable ; s'il bouge, l'estimateur est confondu.
  - Contrôle d'E : monde à queue entièrement fausse, avec des bornes dont le plus petit contre-exemple est d'ordre intermédiaire entre S_T et l'oracle.
- **D3b, proportion auditée.** Dans la famille rare certifiée, H_A : la proportion de fausses parmi les confirmées est ≤ q + δ. H_B : > q + δ. Si H_A est falsifiée, la calibration est refaite par strate et par ordre de contre-exemple, ou le garde-fou est déclaré invalide en queue.

### D4 — Gabarit des interventions

- **Tirages.** Panel, bras de base et bras d'intervention sont indépendants. L'essai A/A compare la stratification sur un même tirage et sur deux tirages indépendants.
- **Contraste.** C = R_int − (1+ε)·R_base, défini même si R_base = 0.
- **Duel.** H_A : E[C] > 0 et écart des proportions auditées ≤ δ (marge de non-infériorité). H_B : E[C] ≤ 0 ou écart > δ.
- **Puissance.** Elle est simulée avant collecte à partir de la variance A/A. Si elle est insuffisante, l'essai est déclaré non jugeable et n'est pas lancé.

### Duels propres

- **I1, scindée en plan factoriel.**
  - Facteurs : allocation (uniforme, ou pilotée par f₁/N mesuré sur des appels-sondes sans exclusion) × liste (aucune, réelle, placebo de même longueur et de même masse exclue).
  - Sous exclusion, le pilote est le taux observé de classes nouvelles passant T, pas f₁/N.
  - Test d'E : une source synthétique à support fini épuisé passe dans la boucle. H_A : l'allocation la coupe. H_B : elle continue de l'alimenter.
  - Abandon : facteur par facteur.
- **I2.**
  - Duel sur le contraste de rendement entre l'union de familles et le meilleur modèle unique avec variation de température. Ce modèle est choisi sur un pilote séparé ; la contrainte de format est identique dans tous les bras.
  - Le recouvrement en strate rare certifiée reste un diagnostic. Son nul vient de pseudo-familles obtenues par partage aléatoire d'une source, à nombre égal de sorties analysables.
  - Contrôle de F : deux températures d'un même modèle. Si elles franchissent le seuil, le diagnostic est écarté.
- **I3.** Duel sur le rendement seul. H_A : contraste isolé contre débat > 0 et écart ≤ δ. H_B : sinon. Témoin : un dialogue factice de même coût, au contenu non informatif. Le nombre de classes distinctes est descriptif.
- **I4.**
  - L'écart entre confirmation sur cas de recherche et sur S_frais est mesuré à chaque itération. H_A : il reste ≤ δ partout, première itération comprise. H_B : il dépasse δ quelque part.
  - S_T′ et l'oracle décomposent l'écart en surajustement d'échantillon et rupture entre ordres.
  - Bras à battre : la même boucle avec mutation mécanique, à coût égal.
  - Témoin : retour de recherche permuté, audit intact.

## (c) Réponse à l'arbitre, en une page

**Ce qui est établi.** Aucun fait empirique : le bloc FAITS est vide. Seuls des arguments tiennent, sous leurs hypothèses écrites. Ce ne sont pas des résultats.

1. La rareté n'est pas une propriété de l'idée. Elle est relative à un protocole de tirage figé P₀ et à un canoniseur κ (questions 1 et 5).
2. La rareté d'une classe ne se certifie que par un panel frais et une borne binomiale simultanée. En dessous d'une taille de panel calculable, rien n'est certifiable (L1).
3. f₁/N (Good, 1953, RAPPORTÉ) estime une nouveauté agrégée sous tirages indépendants. Il ne vaut ni par classe, ni sous exclusion.
4. Aucune intervention sur le générateur ne garantit quoi que ce soit sur les fausses découvertes. Le garde-fou conforme (Bates et al., 2023 ; Benjamini et Hochberg, 1995, RAPPORTÉS) ne garantit que sous échangeabilité, et son plancher de p-valeur borne sa puissance.
5. La proportion de fausses parmi les confirmées dépend du taux de base en queue, et pas seulement du contrôle (L2).
6. Ma conception III.1 était invalide sur son propre banc. Le κ à verdicts binaires fusionnait toutes les vraies. Les cinq critiques l'ont vu ; je le concède.

**Ce qui ne l'est pas.**

- L'existence de « puits étroits » : la question dit elle-même l'ignorer.
- La queue des modèles contient-elle plus de vrai, et de vrai utile, qu'un générateur mécanique ?
- Le contrôle garde-t-il ses taux d'erreur en strate rare ?
- Une seule des interventions I1 à I4 bat-elle le tirage simple à coût égal ? Aucun indice sourcé ne le mesure sur des idées.
- Le κ révisé fonctionne-t-il ? C'est une HYPOTHÈSE, que E0 teste.
- Les verdicts du banc se transportent-ils à un domaine sans oracle ? Aucune expérience proposée ne le teste.
- L'importance d'une idée, au-delà du critère du contrôle (L7).

**L'expérience à faire en premier : E0.**

- Elle ne demande aucun appel de modèle et précède tout le reste.
- H_A : κ sépare les K bornes vraies plantées et fusionne leurs réécritures mécaniques, au seuil préenregistré. H_B : il échoue sur l'un des deux points.
- Si H_B est retenue, le banc tombe et, avec lui, tout décompte de « classes rares vraies ».
- Si H_A est retenue, l'objection commune aux cinq critiques est écartée pour ce canoniseur, sur ce banc et pas ailleurs.

Viennent ensuite D1, puis D2. D2 reste le point d'arrêt le moins cher pour les interventions de rééchantillonnage ; il ne juge pas I4.

FIN-DE-CELLULE