# Preuve, version 2 — poids du test de référence (« nul ») de l'idée 1.1 : nul limité, projection par blocs, lecture à 40 instants, rejet par famille

**Statut.** Pièce préalable au scellement du préenregistrement v2 de l'idée 1.1 (préalable 2 du brouillon :
« une pièce "preuve, version 2", scellée et contre-lue, qui porte les corrections p1 à p6, le lemme de la projection par
blocs sous la garde P4, et la preuve du rejet par famille »). Scellée par empreinte (R6) ; **non contre-lue** : la
contre-lecture (R2) par un sous-agent neuf reste à faire (section 15). Elle **remplace** la preuve v1 pour l'usage du
préenregistrement v2 ; la v1 reste archivée sans modification (R12). Processeur seul, sans dépense. **Aucun résultat du
banc n'existe** ; les seuls calculs sont des énumérations exactes sur de petits cas, sans code du juge (section 13,
script en annexe).

**Ce texte n'adopte rien et ne revendique rien.** Il dit sous quelles hypothèses chaque bras du préenregistrement garde
sa garantie de taille. Adopter une de ces voies dans le juge (nul « v10 », nouvelle règle de lecture, nouvelle valeur e,
garde P4 en production) est **réservé à Lazar**. Aucune revendication de nouveauté : les arguments employés (rapport de
vraisemblance scindé de l'inférence universelle, inégalité de Ville, arrêt optionnel, valeur e de bloc certifiée) sont
ceux que les pièces citées attribuent à la littérature, à vérifier sur pièce (section 14).

- **Auteur** : sous-agent neuf de la session mère ; je n'ai écrit ni la preuve v1, ni sa contre-lecture, ni les
  brouillons du préenregistrement v2, ni leurs contre-lectures, ni la synthèse, ni les rendus des angles, ni leurs
  réfutations, ni le juge, ni les nuls v8 et v9.
- **Date** : 2026-11-15, rédaction de 20:45 à 21:35 UTC environ (`date -u`) ; dépôt lu sur `main`, tête `eeee7230` ; aucun
  commit, aucune poussée, aucun appel réseau, aucun appel payant ; rien lu sous `diag/`, ni sous `runs/` de 7a ou 7b, ni
  sous `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/`.
- **Calculs** : Python 3.13.18, numpy 2.4.6, scipy 1.17.1 (`.venv/bin/python -I -B`), processeur seul. Script et sorties versés à côté
  de ce texte, dans `docs/notes/organisme-idees-juge-v1/preuve-idee-1-1-poids-du-nul-v2-outils/`, chacun avec son
  compagnon `.sha256` (section 13).

## 0. Ce qui est établi, en bref

**Prouvé ici** (preuve écrite pas à pas, et, pour chaque lemme, vérification par énumération exacte sur un petit cas) :
1. **Nul limité** (La, Ld) : taille au plus α sur **sa propre classe**, à tout ensemble d'instants de lecture ; rien hors
   de sa classe (théorème 1). Encadrements trajectoire par trajectoire contre J8, J9 et entre bras, à l'écart résiduel du
   certificat près (proposition 2).
2. **Garde P4 sur la grammaire réelle** : une loi dont l'arbre ne contient ni `sans_remise` ni `moyenne_glissante` ne lit
   pas l'historique, sur le code lu (lemme 3, forme « refus ») ; la forme « gel de l'historique au début du bloc » rend
   P4 vraie **pour une autre carte, la carte gelée**, qui est alors la carte jugée (lemme 4).
3. **Projection par blocs** : la valeur e d'un bloc divisée par son certificat exact a une espérance au plus 1 sous
   chaque membre de la famille (lemme 5, sous P1 à P6 dont P4) ; la projection a un certificat égal à 1 (lemme 6) ; le
   minimum des processus de blocs et de la richesse des autres membres a une taille au plus α aux fins de bloc (Ville,
   théorème 8), et sa valeur arrêtée est une valeur e (corollaire 9).
4. **Lecture à 40 instants** (J9-D40) : valide sur toute la classe du v9 ; sa valeur arrêtée, prise sur le maximum des
   deux engagements, est une valeur e (théorème 10).
5. **Rejet par famille et réunion qui définit J9-D** : taille au plus α pour la carte seule (théorème 11). La statistique
   naturelle de cette règle **n'est pas une valeur e** (espérance 1,4 dans un exemple exact) : elle ne fournit qu'une
   p-valeur, donc **ne se branche pas telle quelle sur la règle e-BH** ; une forme arrêtée membre par membre, à seuil fixé
   d'avance, **est** une valeur e (proposition 13) — c'est une définition neuve, non adoptée.
6. **Sans P4, le lemme tombe** : avec la carte `sans_remise` de composition [1, 1], écrite dans la grammaire, l'espérance
   exacte de la valeur e de bloc vaut 4/3, et l'inégalité de Ville est violée d'un facteur 4/3 (section 11) ; la forme
   « gel » et le maximum certifié restent valides sur les mêmes cas.
7. **Lois connues seulement par tirages** : le certificat calculé « comme si les lois estimées étaient exactes » n'est pas
   un certificat du vrai nul ; calcul exact : une copie exacte du nul promue avec probabilité 0,288 au lieu d'au plus
   0,05 (10 tirages par cellule pour estimer la loi, 200 tirages frais ; section 12).

**Plausible, non prouvé ici** : que la liste des coupes du v9 relue pour J9-Dc rende bien, coupe par coupe, une borne
haute certifiée (code non exécuté, section 10.4) ; que la garde « refus » soit complète **en production** (elle l'est sur
la copie `94bfd92` de `selection_pari.proba`, lemme 3) ; les ampleurs de puissance (aucune n'est traitée ici).

**Ouvert** : la réserve log-linéaire héritée du v8 (marge de Newton) ; la lecture d'un processus de blocs entre deux fins
de bloc ; le pari à fraction sous la projection ; l'existence d'une carte de la grammaire qui atteint le trou de P4 **dans
le juge complet** ; le branchement d'une forme de J9-D sur la règle e-BH avec l'héritage des filles ; le certificat
robuste pour des lois estimées avec des traits ; les références de méthode, non relues sur PDF.

## 1. Pièces lues (empreintes sha256 recalculées le 15 novembre, égales à leurs compagnons `.sha256`, ou, pour les modules de `94bfd92`, à `empreintes-copie-v1.txt`)

| pièce | chemin | empreinte |
|---|---|---|
| preuve v1 (archivée, inchangée) — **[P1]** | `docs/notes/organisme-idees-juge-v1/preuve-validite-nul-limite-v1.md` | `44f249409193778ccbaaa12b6c5e74d64434dfb87be77382d8bb9438459281b2` |
| contre-lecture de la v1 (corrections p1 à p6) — **[CL]** | `docs/notes/organisme-idees-juge-v1/contre-lecture-prereg-nul-limite-et-preuve-v1.md` | `763fc6e29cd80868dcdb1d848eafdc928a39fca7244fa16eb0ac721ec705014e` |
| synthèse de la course de conception — **[SYN]** | `docs/notes/organisme-idees-juge-v1/correction-poids-v1/synthese-correction-poids-du-nul-v1.md` | `48e46c10b163e0cb7d49a7d9c1f09bde2e7c4ac488467739e5b6e8a45c0941b4` |
| angle « projection » (lemmes 1 et 2, proposition 3, théorème 4) — **[PROJ]** | `…/correction-poids-v1/projection/methodes-projection-v1.md` | `681eb7f5c75b9599ddb7508b575f1824fb126fa781409104e08115d106e51f2e` |
| sa réfutation (garde P4, § 5) — **[R-PROJ]** | `…/correction-poids-v1/projection/refutation-projection-v1.md` | `7bfaa88eae7485c973ab6d07271324eca4da4b0bf1404aa1e7e2afce00f5d5e4` |
| angle « toute autre voie » (lemmes A et B) — **[LIB]** | `…/correction-poids-v1/libre/methodes-libre-v1.md` | `e7a2bb6c67241cbb41477c3f6839d802392d74e60960272e5da10ef2cbffc14c` |
| sa réfutation (§ 3 et § 10 : 40 instants, membre par membre) — **[R-LIB]** | `…/correction-poids-v1/libre/refutation-libre-v1.md` | `8ee42bd6ba74f7326f9f1540db5538bee1373f9a6e6bfa8143ef62ea9f58318b` |
| réfutation « inférence universelle » (§ 8.1 : un instant de rejet par famille) — **[R-UNI]** | `…/correction-poids-v1/universelle/refutation-universelle-v1.md` | `f1f03b19f034579ccfa41a360bdc33a7e09d9c48ed456ff375f6b86ba033af84` |
| brouillon 1 du préenregistrement v2 — **[B1]** | `docs/notes/organisme-idees-juge-v1/organisme-idee-1-1-poids-du-nul-v2-brouillon1.md` | `916985cec9ba027effa9fdcf4bf70827424a838ed875358ae213dc1f60d30b55` |
| sa contre-lecture (M2 : carte gelée ; J9-D par réunion) — **[CL2]** | `docs/notes/organisme-idees-juge-v1/contre-lecture-idee-1-1-v2-brouillon1-v1.md` | `d5e71f6c7ee41600a207255614685c303ecca68aecdf457291eaf9a6d6571c4b` |
| nul v9, copie empreintée (lu, jamais exécuté) — **[V9]** | `docs/notes/organisme-idees-juge-v1/copie-nul-v9-a41b7b5/orchestrator/pole/nul_v9.py` | `7ae450df2482246122bf9fbcf0fa5ef30b4a7e4c6f0d09531e83af048e46ee95` |
| liste d'empreintes de la copie `94bfd92` (53 fichiers, `sha256sum -c` : 53 conformes) | `docs/notes/organisme-courbe-dose-reponse-v1/code-organisme-94bfd92/empreintes-copie-v1.txt` | `0153e02d4522fe21eb1cf52985574eba38b5f260f7a3a08183d63589f29f32df` |
| grammaire, `proba`, richesse — **[SP]** | `…/code-organisme-94bfd92/orchestrator/pole/selection_pari.py` | `359928110d757cd54cc0d2773910c7360895b68cac5d17e0e4b4e9933ef306bc` |
| lecture aux instants, membre linéaire — **[NF2]** | `…/orchestrator/pole/nul_filles_v2.py` | `0ed9b4adbcddc4ad77a1c97d5cbd5706f14926e9c47fe96ce2bab3221a138910` |
| nul v8 (réserve log-linéaire) — **[V8]** | `…/orchestrator/pole/nul_v8.py` | `cc452aafd17121a7c0ec42829eea47063ffee1f6cdf7f642e264d528f976b888` |
| refus au gel des cartes qui lisent l'historique (juge v1 sans « urne »), règle e-BH — **[CY]** | `…/orchestrator/pole/cycle.py` | `798f039042e3ee1f18df5c566f5a0ddee5dac5c98225c8ce621e267174c8ee18` |

Le brouillon 2 du préenregistrement (`organisme-idee-1-1-poids-du-nul-v2-brouillon2.md`, commit `eeee7230`) a été
survolé pour vérifier que ses définitions de la garde P4 (numérateur de W^reste sous gel = carte gelée) et de J9-D sont
celles que je prouve ; il n'est pas une pièce de cette preuve.

## 2. Le juge, ses objets et les notations

- **Plan** x_1, …, x_n (n = 200), x_s = (z_s, g_s) ; **issues** y_1, …, y_n rangées dans l'ordre du plan ; K issues.
  Filtration F_t = σ(engagement, y_1, …, y_t). Tout ce qui suit est **conditionnel à l'archive, à la carte, au plan et à
  la marginale d'entraînement**.
- **Carte** : une loi ℓ de la grammaire. Sa loi prédictive à l'instance s est
  q_s(·) = `proba`(ℓ, x_s, h, s − 1) ([SP], l. 109 à 174), où h est l'historique passé à la fonction ; `proba` ne lit que
  h[: s − 1] et renormalise après le plancher 10⁻¹² (`_normaliser`, l. 97 à 100). Deux types lisent h :
  `TYPES_LISANT_L_HISTORIQUE` = (« sans_remise », « moyenne_glissante ») ([SP], l. 58).
- **Instants** : T₈ = {25, 50, …, 200} (instants du juge) ; T₄₀ = {5, 10, …, 200} ; T₈ ⊂ T₄₀. **Blocs** :
  B_b = {25(b − 1) + 1, …, 25b}, b = 1..8 ; a_b = 25(b − 1) issues précèdent le bloc b.
- **Bibliothèque** 𝒩 : membres m, chacun une famille Θ_m de lois conditionnelles sans mémoire (un singleton pour un
  membre ordinaire), et une **valeur** V_m(t) à chaque instant lu : la log-vraisemblance exacte des t premières issues
  pour un membre ordinaire, une **borne haute certifiée** du maximum sur Θ_m pour un membre ajusté (valeur atteinte plus
  écart de Frank-Wolfe, bornée par 0 : [V9] l. 31 à 35 et `_certificats` l. 218 à 229 ; [NF2] `_lineaire` l. 91).
- **Richesse** (pari plein, engagement sans `fractions`) : log W_t = Σ_{s ≤ t} log q_s(y_s) − D_t, D_t = max_m V_m(t).
  Promotion de la carte seule s'il existe t lu avec log W_t ≥ log(1/α), α = 0,05.
- **Rapport au monde** : pour une loi du monde P*, Λ_t = Π_{s ≤ t} q_s(y_s) / P*(y_s | x_s), Λ_0 = 1.
- **Écart résiduel** d'un membre ajusté à t : g_m(t) = V_m(t) − (valeur atteinte par l'optimiseur) ≥ 0 ; il majore
  l'écart vrai V_m(t) − sup_{Θ_m}.

## 3. Hypothèses, numérotées

**Pour toutes les règles à maximum (J8, J9, La, Ld, J9-D40, J9-D) :**
- **H1 (gel).** La carte, le plan, la bibliothèque (donc la liste des membres et des partitions) et α sont fixés et
  empreintés avant le tirage de la première issue fraîche ; les partitions des nuls limités sont calculées sur l'archive
  seule ([P1] § 3), jamais sur des issues fraîches.
- **H2 (fraîcheur).** Les issues fraîches sont tirées après le gel, d'une graine dérivée de l'empreinte de l'engagement,
  indépendamment de ce qui a servi à bâtir la carte, le plan, la bibliothèque et la marginale d'entraînement.
- **H3 (monde sans mémoire, dans la classe).** Il existe un membre m* et θ* ∈ Θ_{m*} tels que la loi du monde soit
  P* = p_{θ*}(· | x), qui ne lit pas l'historique. La **classe** d'une bibliothèque est la réunion de ses Θ_m.
- **H4 (certificat).** Pour tout membre m et tout instant lu t : V_m(t) ne dépend que de l'engagement et de y_1..y_t, et
  V_m(t) ≥ sup_{θ ∈ Θ_m} Σ_{s ≤ t} log p_θ(y_s | x_s). Exact pour les membres ordinaires, pour le membre linéaire et pour
  chaque membre par morceaux (lemme du certificat, [P1] § 3 ; [CL] § 2.1 ; [V9] l. 31 à 35). **Pour un membre
  log-linéaire, seulement « au second ordre près de l'optimum, sans preuve »** ([V8], docstring, l. 66 à 69) : tout ce
  qui suit ne vaut, pour un monde de la classe log-linéaire, que sous cette réserve héritée.
- **H5 (carte prévisible).** Pour chaque s, q_s est une loi (positive, de somme 1) qui ne dépend que de l'engagement, de
  x_s, de s et de y_1..y_{s−1}. *Le plancher 10⁻¹² n'est pas nécessaire à la borne ; il garde log W fini* ([CL] p2). Une
  carte qui lit l'historique **vérifie** H5.
- **H6 (ordre).** Sous le monde, la loi de y_s sachant F_{s−1} est P*(· | x_s) (issues indépendantes sachant le plan,
  dans l'ordre du plan).
- **H7 (instants).** L'ensemble des instants lus est une partie de {1, …, n}, et D_t ne lit que y_1..y_t. **Qu'il soit
  fixé d'avance n'est pas nécessaire** aux théorèmes à maximum (l'inégalité de Ville couvre tous les instants à la
  fois) : c'est une discipline de gel, gardée ([CL] p2).
- **H8 (lecture).** La décision est celle de la règle écrite, avec D_t maximum sur **tous** les membres de la
  bibliothèque gelée ; pas de « meilleur de plusieurs nuls », pas de membre retiré après lecture. *(Le choix des instants
  après lecture n'est pas exclu par nécessité, voir H7.)*

**Pour les bras à projection (J9-P, La-P), en plus :**
- **P1 (gel des familles et des blocs).** La liste finie 𝔽 des familles projetées et la grille des blocs sont fixées avant
  les issues fraîches ; pour J9-P, la liste des coupures ne dépend que du plan gelé.
- **P2 (monde dans une famille projetée).** H3 et H6 avec θ* dans une famille F* ∈ 𝔽, ou dans un membre de W^reste.
- **P3 (dénominateur prévisible par bloc).** La loi φ_{F,b} employée pour le bloc b ne dépend que de l'engagement et de
  y_1..y_{a_b}.
- **P4 (numérateur gelé par bloc), écrite pour la grammaire du juge.** Pour tout bloc b et tout s ∈ B_b, la loi
  q̃_s qui entre **au numérateur, dans la projection et dans le certificat** du bloc b ne dépend que de l'engagement, de
  x_s, de s et de y_1..y_{a_b} — **pas** de y_{a_b + 1}, …, y_{s−1}. Dans la grammaire, P4 n'est pas acquise au pari
  plein ([R-PROJ] § 1, écart 1 ; § 5). Elle est obtenue sous l'une de deux formes, déclarées au gel :
  - **P4-R (refus)** : la carte est refusée au gel (comptée « refusée », jamais promue) si
    `types_de_la_loi`(ℓ) ∩ `TYPES_LISANT_L_HISTORIQUE` ≠ ∅ ([SP], l. 58 à 75) ; sinon q̃_s = q_s. Le lemme 3 montre que
    P4 est alors vraie.
  - **P4-G (gel de l'historique au début du bloc)** : pour s ∈ B_b, q̃_s = q^G_s := `proba`(ℓ, x_s, (y_1, …, y_{a_b}),
    s − 1), l'historique passé à la fonction étant **tronqué** aux a_b premières issues. P4 est vraie par construction
    pour q^G (lemme 4). **La carte jugée est alors q^G, pas la carte soumise** ([CL2] M2) ; le numérateur de W^reste est
    q^G aussi (une seule carte jugée, comme le brouillon 2 l'écrit).
- **P5 (positivité).** P_φ(y | x_s) > 0 pour toute issue y avec q̃_s(y) > 0 ; avec le plancher, q̃_s(y) > 0 pour tout y :
  il faut donc φ à l'intérieur relatif du polytope (bruit aveugle ρ_k > 0 pour tout k), ce que l'algorithme
  d'espérance-maximisation garde à partir d'un départ intérieur ; un essai de code doit le vérifier.
- **P6 (linéarité).** Pour chaque F ∈ 𝔽 et chaque x, θ ↦ P_θ(· | x) est affine sur un polytope Θ_F de sommets connus V_F :
  pour les familles du v9, « une loi connue par cellule, bruit nul » ou « bruit = δ_k, poids nuls » ([V9] l. 31 à 35 ;
  [PROJ] § 3). Les membres log-linéaires et les moyennes glissantes ne vérifient pas P6 : ils restent dans W^reste.

**Pour le rejet par famille, en plus :**
- **R1 (liste des familles).** La liste des familles lues une à une est fixée avant les issues fraîches : membres nommés
  de la bibliothèque (J9-D), ou coupures du plan gelé (J9-Dc) ; la classe est leur réunion.

## 4. Les corrections p1 à p6 de [CL], et où elles sont portées

| | correction demandée ([CL] § 2.2) | traitement ici |
|---|---|---|
| p1 | tolérance d'arrêt : celle du code du v9, `TOLERANCE_GROUPE` = 10⁻³ nat ([V9] l. 108), et non 10⁻⁴ | **acceptée** : proposition 2 emploie l'écart résiduel g_m(t) mesuré à chaque évaluation, au plus 10⁻³ nat quand l'optimiseur a convergé ; aucune tolérance fixe n'entre dans une garantie |
| p2 | H7 suffisante, non nécessaire ; idem « ou des instants » en H8 ; plancher non nécessaire en H5 | **acceptée** : H5, H7, H8 récrites (section 3) ; c'est ce qui fonde la lecture à 40 instants (théorème 10) |
| p3 | remarque (ii) vraie pour le pari plein seulement | **acceptée** : théorème 1, remarque (b) ; pour la projection, « près de 1 », jamais « au plus 1 » (remarque après le lemme 6) |
| p4 | corollaire e-BH trop large (bibliothèque propre à la carte, héritage, `m_fixe`) | **acceptée** : corollaire 1 ; la règle e-BH est citée d'après [CY], non relue sur PDF |
| p5 | § 6 (d) vaut pour La et Ld, pas pour La2 ; W^La2 ≤ W^La et W^Ld ≤ W^La | **acceptée** : proposition 2 (La2 n'est plus un bras du v2, l'inégalité est gardée pour mémoire) |
| p6 | statut périmé : la copie du v9 est versée et lue | **acceptée** : [V9] est lu (famille l. 15 à 25 ; certificats l. 218 à 229 ; coupes l. 398 à 417, seuils l. 413 ; élagage l. 276 à 288, arrêt de groupe l. 286) ; la proposition 2 (b) est relue sur lui |

## 5. Deux outils élémentaires

**Lemme V (Ville, version discrète).** Soit (M_k)_{k=0..N} une surmartingale positive pour une filtration (G_k), M_0 ≤ 1.
Pour tout α ∈ ]0, 1[, P(∃ k ≤ N : M_k ≥ 1/α) ≤ α.
*Preuve.* τ = premier k avec M_k ≥ 1/α (τ = N sinon) est un temps d'arrêt borné ; par arrêt optionnel,
E[M_τ] ≤ M_0 ≤ 1 ; sur {∃ k : M_k ≥ 1/α}, M_τ ≥ 1/α ; donc (1/α)·P(∃ k) ≤ E[M_τ] ≤ 1. ∎

**Lemme Λ.** Sous H5 et H6, (Λ_t)_{t=0..n} est une surmartingale positive de départ 1 pour (F_t).
*Preuve.* E[Λ_t | F_{t−1}] = Λ_{t−1}·Σ_{y : P*(y|x_t) > 0} q_t(y) ≤ Λ_{t−1}, car q_t est F_{t−1}-mesurable (H5) et
y_t ~ P*(· | x_t) sachant F_{t−1} (H6). ∎ *(H5 suffit : une carte qui lit l'historique reste couverte.)*

**Lemme M (minimum et maximum de bornes).** (a) Le minimum de deux bornes hautes certifiées d'une même quantité en est
une. (b) Si, pour chaque i, une statistique W^(i) vérifie P_P(∃ t ∈ T : W^(i)_t ≥ 1/α) ≤ α pour toute loi P de la
classe 𝒞_i, alors min_i W^(i) vérifie la même borne pour toute loi de ∪_i 𝒞_i. (c) Si plusieurs statistiques sont
**chacune majorée trajectoire par trajectoire par le même** Λ_t, leur maximum l'est aussi.
*Preuve.* (a) min(u, v) ≥ x si u ≥ x et v ≥ x. (b) Pour P ∈ 𝒞_i, {∃ t : min ≥ 1/α} ⊂ {∃ t : W^(i)_t ≥ 1/α}.
(c) Immédiat. ∎

## 6. Nul limité (La, Ld) : validité sur sa classe

**Définitions** ([P1] § 3, inchangées sauf la liste des bras). Lois connues L_1..L_J de l'archive (J ≥ 2, sinon aucun
membre par morceaux, comme le v9). Pour une partition P du plan, fixée par l'archive, la famille
F_P = {p_{μ,ρ} : p(y | x) = Σ_j μ_{c(x),j} L_j(y | x) + ρ_y ; μ, ρ ≥ 0 ; Σ_j μ_{c,j} + Σ_k ρ_k = 1 pour chaque cellule c}
(poids propres à la cellule, bruit aveugle **commun**, comme [V9] l. 15 à 25). **La** = 𝒩₈ ∪ {F_P : P = une coupure
{z_j ≤ s} | {z_j > s} de l'archive, à seuil **fixé**} ; **Ld** = La ∪ {F_P : P = sous-population, ou signe d'un trait}.

**Théorème 1 (taille sur la classe).** Sous H1 à H8, pour la bibliothèque La (ou Ld) et tout monde de **sa** classe,
P(∃ t lu : log W_t ≥ log(1/α)) ≤ α, quel que soit l'ensemble des instants lus (H7).
*Preuve.*
1. *Domination* : pour t lu, D_t ≥ V_{m*}(t) ≥ sup_{Θ_{m*}} Σ_{s ≤ t} log p_θ(y_s | x_s) ≥ Σ_{s ≤ t} log P*(y_s | x_s)
   (H3, H4 ; pour F_P, le lemme du certificat est exact).
2. *Majoration* : log W_t ≤ log Λ_t, trajectoire par trajectoire.
3. *Surmartingale* : lemme Λ.
4. *Ville* : lemme V sur {0, …, n} ; les instants lus en sont une partie. ∎

**Remarques.** (a) Ni le nombre de partitions ni le nombre de membres n'entre dans la borne : la validité ne dépend pas
de la taille de la liste ; seule la puissance en dépend ([CL] § 2.1). (b) **Sous le pari plein** (engagement sans
`fractions`), une carte qui est un point θ_carte d'un membre a un numérateur ≤ exp(D_t), donc W_t ≤ 1 à chaque instant ;
**sous le pari à fraction**, seule la borne de Ville vaut ([CL] p3). (c) Aucune garantie hors de la classe : une copie
coupée hors des partitions retenues n'est pas couverte (prix de la restriction, [P1] § 7).

**Corollaire 1 (valeur e, règle e-BH).** La valeur e d'une carte, e = W_τ, τ = premier t ∈ T₈ où W_t ≥ m/α (sinon n),
vérifie E[e] ≤ E[Λ_τ] ≤ 1 (arrêt optionnel, lemme Λ). **Pour des cartes fraîches jugées sur la même archive (même
classe, sans héritage, m fixé avant toute issue par `m_fixe`)**, et si le monde est dans cette classe, la règle de
Benjamini et Hochberg sur valeurs e borne par α la probabilité d'au moins une promotion. Le théorème de cette règle est
cité d'après [CY] (`appliquer_multiplicite`, l. 717), **non relu sur PDF** ; le banc ne s'en sert pas (promotion de la
carte seule) ([CL] p4).

**Proposition 2 (encadrements, trajectoire par trajectoire, mêmes issues, mêmes instants).** Notons g^X(t) le plus
grand écart résiduel des membres ajustés du bras X à t.
- (a) 𝒩₈ ⊂ La : D^La_t ≥ D^8_t − g^8(t), donc log W^La_t ≤ log W^J8_t + g^8(t) (l'écart disparaît si les membres
  communs sont calculés par le même code sur les mêmes issues, cas du banc).
- (b) Chaque F_P de La ou de Ld est contenu dans un membre du v9 : le v9 parcourt, pour chaque trait et chaque instant,
  s = −∞ et chaque valeur distincte du trait parmi les t instances ([V9] l. 413), donc la partition qu'un seuil fixé
  induit sur les t premières instances est l'une de ses coupes ; une coupe élaguée garde son certificat dans le maximum
  ([V9] l. 276 à 288). D'où V^La_P(t) ≤ sup_{F_P} + g^La(t) ≤ D^9_t + g^La(t), et
  **log W^La_t ≥ log W^J9_t − g^La(t)** (de même pour Ld). Avec la tolérance du code du v9 (`TOLERANCE_GROUPE` = 10⁻³ nat,
  l. 108), inchangée, La et Ld promeuvent tout ce que le v9 promeut, **sauf** quand log W⁹ dépasse le seuil de moins que
  g^La(t) (au plus 10⁻³ nat quand l'optimiseur a convergé ; mesuré à chaque évaluation) ([CL] p1).
- (c) La ⊂ Ld (et, pour mémoire, 𝒫₁(C_arch) ⊂ 𝒫₂(C_arch)) : **log W^Ld_t ≤ log W^La_t + g^La(t)** et
  log W^La2_t ≤ log W^La_t + g^La(t) ([CL] p5).
- (d) Conséquence : pour un monde de la classe du v9 hors de celle de La ou de Ld, les promotions de La et de Ld sont
  encadrées par celles du v9 (en dessous, à l'écart résiduel près) et du v8 (au-dessus) ; **aucune garantie** ([CL] p5).
*Preuve.* Chaque inégalité vient de « un dénominateur qui contient plus de membres est plus haut », appliquée membre à
membre avec V ≥ sup ≥ valeur atteinte = V − g. ∎

## 7. La garde P4 sur la grammaire réelle

**Lemme 3 (forme « refus » : une loi sans type lisant l'historique ne lit pas l'historique).** Sur la copie `94bfd92`
de `selection_pari.py` ([SP]) : si `types_de_la_loi`(ℓ) ne contient ni « sans_remise » ni « moyenne_glissante », alors
pour toute instance x, tout instant t et tous historiques h, h′ : `proba`(ℓ, x, h, t) = `proba`(ℓ, x, h′, t).
*Preuve*, par récurrence sur la profondeur de l'arbre de ℓ, en suivant `proba` (l. 109 à 174) :
- feuilles qui ne lisent ni h ni rien d'autre que x et t : « fixe » (l. 112), « softmax » (l. 114 à 118, lit z), « derive_lineaire »
  (lit t), « calendrier » (lit t), « deterministe » (lit t) ; t est l'indice du plan, fixé par le plan gelé ;
- nœuds qui transmettent h **inchangé** à des sous-lois : « par_sous_population » (`lois`[g] ou `defaut`),
  « melange » (`composantes`), « si_sinon » (`si`, `sinon` ; la condition ne lit que l'instance, `_condition`, l. 103 à
  106), « enveloppe » (`lois`), « echelle » (`loi`, instance réechelonnée), « transformee » (`base` ; les options
  `melange_aveugle`, `puissance`, `inclinaison`, `oscillation` ne lisent que des constantes et z) ;
- seules « moyenne_glissante » (l. 131 à 135 : `historique[max(0, t − w):t]`) et « sans_remise » (l. 156 à 159 :
  `Counter(historique[:t])`) lisent h ;
- `types_de_la_loi` (l. 61 à 75) parcourt exactement les clés par lesquelles `proba` descend (`si`, `sinon`, `loi`,
  `base`, `defaut` ; `lois` et `composantes`, en liste ou en dictionnaire) : toute sous-loi que `proba` peut évaluer est
  visitée. Par récurrence, `proba`(ℓ, x, h, t) ne dépend pas de h. ∎
*Conséquence.* Sous P4-R, une carte acceptée a q_s = `proba`(ℓ, x_s, ∅, s − 1) : q_s ne dépend que de x_s et de s ; P4,
P3 (pour les projections calculées au gel) et H5 sont vraies. **Portée** : prouvé sur le code lu ; tout ajout d'un type
à la grammaire, ou d'une clé de descente, oblige à refaire la preuve (essai de code : comparer `types_de_la_loi` à la
liste des clés lues par `proba`). Le juge de production v1 sans « urne » refuse déjà ces cartes au gel ([CY] l. 318 à
327), avec le même test : la forme « refus » est donc celle du juge v1 sans urne ; le banc, qui emploie
`BIBLIOTHEQUE_STANDARD` (juge v0), les accepte (écart de montage dit par [CL2] m11).

**Lemme 4 (forme « gel de l'historique »).** Pour s ∈ B_b, posons q^G_s = `proba`(ℓ, x_s, (y_1..y_{a_b}), s − 1).
(i) q^G_s est une loi (renormalisée après plancher). (ii) q^G_s ne dépend que de l'engagement, de x_s, de s et de
y_1..y_{a_b} : P4 vraie pour q^G. (iii) q^G vérifie H5 (a_b ≤ s − 1). (iv) Si ℓ n'a aucun type lisant l'historique,
q^G = q (lemme 3) : pour une carte sans mémoire, refus, gel et absence de garde coïncident. (v) **Sinon q^G ≠ q en
général**, et q^G dépend de la grille des blocs : « sans_remise » ne décompte que les issues des blocs passés ;
« moyenne_glissante » de fenêtre w voit une fenêtre vide, donc la loi uniforme, dès que s − 1 − w ≥ a_b.
*Preuve.* (i) `_normaliser`. (ii) et (iii) : l'argument h passé à `proba` est la suite tronquée, fonction de
y_1..y_{a_b} ; `proba` ne lit que h[: s − 1], ici h entier. (iv) Lemme 3. (v) Lecture des l. 131 à 135 et 156 à 159. ∎
*Conséquence pour la lecture (M2 de [CL2]).* Sous P4-G, **toute promotion porte sur la carte gelée q^G**, qui n'est pas
la carte soumise ; elle ne vaut que comme contrôle de validité. Les théorèmes 8 et 9 ci-dessous valent pour q^G.
Adopter cette forme dans le juge changerait ce qu'une carte parie : question de sens, réservée au nœud de Lazar.
*Exigence de code* : sous gel, la loi est évaluée par un appel qui reçoit l'historique tronqué ; le `Cache` du juge
([SP] l. 356 à 367) passe toutes les issues et ne convient pas tel quel.

## 8. Projection par blocs : le lemme, avec certificat exact

**Définition (valeur e d'un bloc).** Pour une famille F ∈ 𝔽 vérifiant P6, un bloc B (|B| = b) et φ ∈ Θ_F fixé selon P3,
avec q̃ selon P4 :
- r_s(y) = q̃_s(y) / P_φ(y | x_s), s ∈ B ;
- **certificat** c_B(φ) = max_{v ∈ V_F} (1/b)·Σ_{s ∈ B} Σ_y P_v(y | x_s)·r_s(y) — une liste finie de sommes finies,
  calculée exactement (lois discrètes connues) ;
- e_B = Π_{s ∈ B} r_s(y_s) / max(1, c_B)^b ; W^F aux fins de bloc : produit des e_B des blocs écoulés.
Pour les familles du v9 : le maximum sur les sommets se calcule cellule par cellule, c_B = (1/b)·max( max_k Σ_s r_s(k) ;
Σ_c max_j Σ_{s ∈ B ∩ c} Σ_y L_j(y | x_s)·r_s(y) ) — c'est le maximum du gradient aux sommets, divisé par b.

**Lemme 5 (valeur e de bloc).** Sous P1 à P6, pour tout θ ∈ Θ_F : E_θ[e_B | F_{a_b}] ≤ 1.
*Preuve.*
1. *Factorisation.* Sachant F_{a_b}, φ (P3) et les r_s (P4) sont fixés ; sous θ, les issues du bloc sont indépendantes,
   y_s ~ P_θ(· | x_s) (P2). Donc E_θ[Π_s r_s(y_s) | F_{a_b}] = Π_s m_s(θ), m_s(θ) = Σ_y P_θ(y | x_s)·r_s(y), fini (P5).
   **C'est le seul pas qui emploie P4** : si r_s dépendait de y_{a_b + 1}..y_{s−1}, le produit ne se factoriserait pas.
2. *Moyennes.* Π_s m_s(θ) ≤ ((1/b)·Σ_s m_s(θ))^b (inégalité arithmético-géométrique, m_s ≥ 0).
3. *Sommet.* θ ↦ (1/b)·Σ_s m_s(θ) est affine (P6) ; son maximum sur le polytope est atteint en un sommet : ≤ c_B(φ).
4. E_θ[e_B | F_{a_b}] ≤ (c_B / max(1, c_B))^b ≤ 1. ∎
Le certificat ne suppose **aucune convergence** : φ quelconque (même mal ajusté) donne une valeur e valide ; un φ mauvais
coûte b·log c_B nats de puissance, jamais de validité. *Vérification* : section 13, partie A.

**Lemme 6 (la projection a un certificat égal à 1).** Si φ* minimise Σ_{s ∈ B} KL(q̃_s ‖ P_θ(· | x_s)) sur Θ_F (calcul
qui ne lit que q̃, les lois connues et le plan), alors c_B(φ*) = 1.
*Preuve.* θ ↦ Σ_s KL(q̃_s ‖ P_θ) est convexe (P6). À l'optimum, la dérivée dans toute direction θ − φ* est ≥ 0 :
Σ_s Σ_y q̃_s(y)·(P_θ − P_φ*)(y | x_s) / P_φ*(y | x_s) ≤ 0, soit Σ_s m_s(θ) ≤ Σ_s Σ_y q̃_s(y) = b ; avec θ = un sommet,
c_B ≤ 1 ; avec θ = φ*, m_s = 1, donc c_B = 1. ∎
*Remarque (p3).* Pour une carte membre de F, φ* = q̃ et e_B = 1 à l'erreur de l'optimiseur près ; avec un optimiseur
arrêté, e_B peut dépasser 1 sur une suite donnée (seule l'espérance est bornée) : l'audit d'une carte membre est « près
de 1 », jamais « au plus 1 ».

**Proposition 7 (la projection est le meilleur choix certifié sous la loi de la carte).** Si le monde suit q̃ dans le
bloc, pour tout φ ∈ Θ_F : E_q̃[log e_B(φ)] ≤ E_q̃[log e_B(φ*)] = Σ_{s ∈ B} KL(q̃_s ‖ P_φ*(· | x_s)).
*Preuve* ([PROJ] § 3, relue pas à pas) : E[log e_B(φ)] = Σ_s E[log(q̃_s / P_φ*)] + Σ_s E[log(P_φ* / P_φ)] − b·log max(1, c_B(φ)) ;
par Jensen, Σ_s E[log(P_φ* / P_φ)] ≤ b·log((1/b)·Σ_s Σ_y q̃_s(y)·P_φ*(y | x_s) / P_φ(y | x_s)) ≤ b·log c_B(φ), car φ* est
un point du polytope et le maximum d'une forme affine y est pris en un sommet. Le deuxième terme est compensé par le
troisième. ∎ *(Ce n'est pas le vrai numéraire du bloc, qui demande des sommes sur K^25 suites : [PROJ] § 3, réserve ;
aucune affirmation n'en dépend.)*

**Théorème 8 (J9-P et La-P : minimum de processus, Ville aux fins de bloc).** Soit la richesse
log W_t = min( log W^reste_t ; min_{F ∈ 𝔽} log W^F_t ), t ∈ T₈ (fins de bloc), où W^reste est la richesse du juge sur
la bibliothèque privée des membres linéaires et par morceaux, **avec le même numérateur q̃** (q sous P4-R, q^G sous P4-G).
Sous H1 à H8 pour W^reste, P1 à P6 pour les familles projetées, et pour tout monde sans mémoire de la classe
(réunion des membres de W^reste et des familles de 𝔽) : P(∃ t ∈ T₈ : W_t ≥ 1/α) ≤ α.
*Preuve.* Si le monde est dans F* ∈ 𝔽 : par le lemme 5 et le conditionnement emboîté, (W^{F*}_{25b})_{b=0..8} est une
surmartingale positive de départ 1 pour (F_{25b}) ; W ≤ W^{F*} aux fins de bloc ; lemme V. Si le monde est dans un
membre de W^reste : W ≤ W^reste ≤ Λ (théorème 1, pas 1 et 2, avec q̃, qui vérifie H5 par les lemmes 3 et 4) ; lemmes Λ
et V. Lemme M (b). ∎
**Classe.** Pour J9-P, 𝔽₉ = {famille linéaire ; sous-population ; pour chaque trait j et chaque valeur c de z_j sur le
plan gelé, la coupure {z_j ≤ c} | {z_j > c}} : toute coupure réelle induit sur les 200 instances la partition d'une de
ces coupures (ou aucune coupure) ; **comme lois sur le plan**, la classe est celle du v9 ([PROJ] § 4, M3). Le nombre de
familles n'entre pas dans la borne. *Vérification* : section 13, partie B.

**Corollaire 9 (valeur e).** Avec τ = première fin de bloc où W_t ≥ m/α (sinon n), E[W_τ] ≤ 1 : τ est un temps d'arrêt de
(F_{25b}), W_τ ≤ W^{F*}_τ (ou ≤ Λ_τ), arrêt optionnel. ∎

**Ce que le théorème 8 ne couvre pas.** (i) **Une carte sans garde qui lit l'historique du bloc** (section 11). (ii) La
lecture d'un processus de blocs **entre deux fins de bloc** : non couverte par cette preuve (ouvert). (iii) Le **pari à
fraction**, dont le numérateur lit la marginale en ligne du bloc courant ([SP] l. 377 à 398) : P4 fausse, sauf gel par
bloc (M9 de [PROJ], non traité ici). (iv) La réserve log-linéaire, dans W^reste (H4). (v) Le membre de bibliothèque
« moyenne_glissante » de W^reste lit l'historique **comme membre du nul** : sans effet sur la validité (lemme M), une
loi du monde qui lirait l'historique est hors de H3 de toute façon ([CL2] m13).

## 9. Lecture à 40 instants (J9-D40)

**Théorème 10.** Soient deux engagements de même plan, mêmes issues, même bibliothèque, lus l'un sur T₈ (J9), l'autre
sur T₄₀ (« jumeau »), avec des solveurs qui peuvent différer (départs chaînés différents) : W^(8) et W^(40). Sous H1 à
H8, pour tout monde de la classe du v9 :
(a) P(J9-D40 promeut) = P(∃ t ∈ T₈ : W^(8)_t ≥ 1/α, ou ∃ t ∈ T₄₀ : W^(40)_t ≥ 1/α) ≤ α ;
(b) W̃_t = max(W^(8)_t·1[t ∈ T₈], W^(40)_t), t ∈ T₄₀, vérifie W̃_t ≤ Λ_t, et sa valeur arrêtée au premier t ∈ T₄₀ où
W̃_t ≥ m/α (sinon n) est une valeur e.
*Preuve.* Chaque engagement vérifie H4 : W^(8)_t ≤ Λ_t et W^(40)_t ≤ Λ_t (théorème 1, pas 1 et 2) ; lemme M (c) :
W̃_t ≤ Λ_t ; l'événement (a) est {∃ t ∈ T₄₀ : W̃_t ≥ 1/α} ⊂ {∃ t : Λ_t ≥ 1/α} ; lemmes Λ et V. (b) : arrêt optionnel de
Λ. ∎ La promotion « J9 ⇒ J9-D40 » vaut par définition ; la garantie reste α ; le taux observé peut monter, sous α.

## 10. Rejet par famille (J9-D), réunion, et pourquoi ce n'est pas une valeur e

### 10.1 La règle et sa validité

**Règle par membre.** Pour une liste ℳ fixée (R1), la carte est promue si, pour **chaque** m ∈ ℳ, il existe
t_m ∈ T₄₀ avec log q(y_1..t_m) − V_m(t_m) ≥ log(1/α) (les t_m peuvent différer). J9-D est la **réunion** : J9, ou
J9-D40, ou la règle par membre sur l'engagement jumeau ([B1], bras 5 ; brouillon 2, même définition).

**Théorème 11 (taille de J9-D).** Sous H1 à H8 et R1, pour tout monde sans mémoire d'un membre m* ∈ ℳ et toute carte
qui vérifie H5 : P(J9-D promeut) ≤ α.
*Preuve.*
1. *Bornes réunies.* Pour t ∈ T₈, V*_m(t) = min(V^(8)_m(t), V^(40)_m(t)) ; pour t ∈ T₄₀ \ T₈, V*_m(t) = V^(40)_m(t).
   Par le lemme M (a), V*_m vérifie H4.
2. *Inclusion.* J9 promeut à t ∈ T₈ ⇒ pour tout m, log q − V^(8)_m(t) ≥ log(1/α) ⇒ log q − V*_m(t) ≥ log(1/α). De même
   pour J9-D40 (à t ∈ T₄₀, sur V^(40), donc sur V*) et pour la règle par membre (sur V^(40)). La réunion est donc
   contenue dans l'événement R* = {∀ m ∈ ℳ, ∃ t_m ∈ T₄₀ : log q(y_1..t_m) − V*_m(t_m) ≥ log(1/α)}.
3. *Un seul membre suffit.* R* ⊂ {∃ t ∈ T₄₀ : log q(y_1..t) − V*_{m*}(t) ≥ log(1/α)} ⊂ {∃ t : Λ_t ≥ 1/α}, car
   V*_{m*}(t) ≥ Σ_{s ≤ t} log P*(y_s | x_s) (H3, H4).
4. Lemmes Λ et V. ∎
*Remarques.* (a) Le choix de t_m après lecture est permis : Ville borne tous les instants à la fois ([R-UNI] § 8.1).
(b) « ∃ t ∀ m » ⊂ « ∀ m ∃ t_m » : J9-D40 est contenu dans la règle par membre calculée sur les mêmes valeurs ; la
réunion avec J9 n'est nécessaire que parce que les deux engagements ont des solveurs différents ([CL2], point 5) ; le
point 1 ramène toute la réunion à une seule règle par membre, sur les bornes réunies V*. (c) La protection d'une carte
membre reste entière sous le pari plein : une carte point de m* a log q − V*_{m*}(t) ≤ 0 à chaque t, donc m* n'est
jamais rejeté et la carte n'est jamais promue. (d) Le niveau ne se
partage pas : chaque membre doit être rejeté au niveau α ([LIB] lemme B, sens suffisant, tel que [R-LIB] § 3 le borne).
*Vérification* : section 13, partie D.

### 10.2 Ce qui n'est pas une valeur e

La sortie de J9-D est une **décision** au niveau α. Sa statistique naturelle est
S = min_{m ∈ ℳ} max_{t ∈ T₄₀} q(y_1..t) / exp(V*_m(t)), et {J9-D promeut} ⊂ {S ≥ 1/α}.
- **S n'est pas une valeur e.** Sous un monde de m*, S ≤ max_t Λ_t, et le maximum courant d'une martingale n'a pas une
  espérance au plus 1 en général. *Exemple exact* : un membre ordinaire unique {P*}, P* = (1/2, 1/2), carte (0,9 ; 0,1),
  lecture à t = 1 et t = 2 ; S = max(Λ_1, Λ_2) prend les valeurs 3,24 ; 1,8 ; 0,36 ; 0,2 avec probabilité 1/4 chacune :
  **E[S] = 1,4 > 1**. Énumération sur des membres par morceaux : section 13, partie D.
- **Ce que S est.** P(S ≥ 1/α) ≤ α **pour tout** α à la fois (théorème 11) : min(1, 1/S) est une p-valeur valide,
  pas une valeur e.
- **Pourquoi elle ne se branche pas telle quelle sur la règle e-BH.** La garantie de la règle de Benjamini et Hochberg sur
  valeurs e (taux de fausses découvertes au plus α sous dépendance quelconque, citée par [CY], non relue sur PDF) suppose
  que chaque statistique a une espérance au plus 1 sous son hypothèse nulle ; `appliquer_multiplicite` ([CY] l. 717)
  reçoit des richesses arrêtées à m/α, ajoute un cumul d'héritage aux filles et ne fixe m que si `m_fixe` est donné
  ([CL] p4). Brancher S (ou sa décision) à la place viole l'hypothèse du théorème : rien ne borne alors le taux. Une
  p-valeur relève d'autres règles (Benjamini et Hochberg sous dépendance positive, Benjamini et Yekutieli sous
  dépendance quelconque ; non relues sur PDF), qui ne sont pas la règle du juge.

### 10.3 Deux façons valides d'en tirer une valeur e (prouvées ; non adoptées)

**Proposition 12 (étalonnage).** Si f : [0, 1] → [0, ∞[ est décroissante et ∫₀¹ f = 1, et si p est une p-valeur valide
(P(p ≤ u) ≤ u pour tout u), alors E[f(p)] ≤ 1.
*Preuve.* E[f(p)] = ∫₀^∞ P(f(p) > v) dv ; f décroissante : {f(p) > v} ⊂ {p ≤ u_v} avec u_v = sup{u : f(u) > v} ; donc
E[f(p)] ≤ ∫₀^∞ u_v dv = ∫₀¹ f(u) du = 1. ∎ Appliquée à p = min(1, 1/S) : une valeur e, au prix d'une perte de puissance.

**Proposition 13 (arrêt membre par membre, seuil fixé d'avance).** Soit c > 0 fixé avant les issues (par exemple
c = m/α avec m fixé par `m_fixe`). Pour chaque m, τ_m = premier t ∈ T₄₀ où q(y_1..t)/exp(V*_m(t)) ≥ c (sinon n), et
E′_c = min_m q(y_1..τ_m) / exp(V*_m(τ_m)). Sous H1 à H8 et R1, pour tout monde de la classe : E[E′_c] ≤ 1, et
{E′_c ≥ c} est exactement l'événement « par membre » au seuil c.
*Preuve.* τ_{m*} est un temps d'arrêt borné (V*_{m*}(t) ne lit que y_1..y_t) ; E′_c ≤ q(y_1..τ_{m*})/exp(V*_{m*}(τ_{m*}))
≤ Λ_{τ_{m*}} ; E[Λ_{τ_{m*}}] ≤ 1 (lemme Λ, arrêt optionnel). Égalité des événements : si chaque membre franchit c à un
instant lu, chaque terme du minimum vaut au moins c ; sinon un membre ne franchit jamais c, et son terme, pris à n, est
sous c. ∎
**Réserves.** E′_c est une **définition neuve de la valeur e du juge** : l'adopter est une modification du juge (nœud de
Lazar). E′_c n'est pas ordonnée avec la valeur e de J9 sous le seuil c (elle peut être plus basse), donc son effet sur
la puissance de la règle e-BH à plusieurs cartes est inconnu ; son interaction avec l'héritage des filles n'est pas
étudiée. *Vérification* : section 13, partie D (E[E′_c] ≤ 1 sur les cas énumérés).

### 10.4 J9-Dc (une famille par coupure du plan)

Même preuve, avec ℳ = la liste des coupures du plan gelé (R1) et V_c(t) la borne certifiée de la coupe que c induit sur
les t premières instances. **Plausible, non prouvé ici** : que la copie renommée de `detail_morceaux_groupe` rende bien,
pour chaque coupe, une valeur ≥ le maximum de sa famille, y compris pour une coupe élaguée (dans [V9], une coupe élaguée
garde son meilleur certificat, l. 276 à 288 ; je n'ai pas lu la fonction qui les rend coupe par coupe). C'est un
préalable de code, à établir par son différentiel ([B1], bras 5).

## 11. Sans P4, le lemme tombe : contre-exemple chiffré

**Cadre.** K = 2 ; famille F₀ des **lois constantes** (sommets δ_0, δ_1 ; elle vérifie P6 ; c'est la part « bruit
aveugle » de tout membre linéaire, et la famille entière d'un membre linéaire dont les lois connues sont des lois
`fixe`) ; monde constant P(y = 0) = p, membre de F₀. **Carte** : `sans_remise` de composition [1, 1], écrite dans la
grammaire (`valider_loi`, [SP] l. 242 à 246 : effectifs entiers ≥ 0 de somme ≥ 1) ; q_1 = (1/2, 1/2), puis, l'issue
vue retirée, q_2 = l'autre issue (au plancher près). Bloc de b = 2, **sans garde** : projection et certificat calculés
sur les lois que la carte a réalisées.

**Calcul.** Sur F₀, la projection de (q_1, q_2) est leur moyenne : (1/4, 3/4) si y_1 = 0. Certificat : pour δ_0,
(1/2)·((1/2)/(1/4) + 0) = 1 ; pour δ_1, (1/2)·((1/2)/(3/4) + 1/(3/4)) = 1 ; c = 1 (le lemme 6 tient : ce n'est pas le
certificat qui manque, c'est P4). Si y_2 ≠ y_1 : e = (1/2·1)/(1/4·3/4) = 8/3 ; si y_2 = y_1 : e ≈ 0 (plancher). D'où
**E_p[e_B] = 2p(1 − p)·8/3 = (16/3)·p(1 − p)**, soit **4/3 pour p = 1/2**, 1,12 pour p = 0,3, 0,48 pour p = 0,1 (mêmes
valeurs que [R-PROJ] § 5, calcul exact, carte « pile ou face puis l'autre issue »). **Ville violée** : pour
α ∈ ]3/8 ; 1/2[, P(e_B ≥ 1/α) = 1/2 > α ; le plus grand rapport P/α vaut 4/3, atteint à α = 3/8.

**Énumération** (section 13, partie C ; monde p = 1/2, 2^n suites, blocs de 2 à 6, n de 2 à 12) : sur 48 configurations (8 cartes de la grammaire × 6 découpages), **12 violent Ville sous la forme sans garde**, toutes avec
`sans_remise` : plus grand rapport sup_α P(promotion)/α de 1,0001 à **1,3333** (composition [1, 1], α = 3/8) ; espérance
exacte de la valeur e du premier bloc de 1,0455 à 1,6793 pour les compositions [1, 1] à [6, 6]. À α = 0,05 et sur ces
petits n (au plus 12 tirages), la plus grande probabilité de promotion sans garde est 0,0083 (composition [3, 3], blocs
de 4) : à cette échelle, la violation se voit aux α plus grands ; à l'échelle du juge, voir ci-dessous. Avec
`moyenne_glissante` (fenêtres 1 et 2, lissages 0,001 et 0,5), l'espérance de la valeur e du premier bloc reste sous 1
(0,03 à 0,75) et aucune violation n'apparaît : le trou n'est pas atteint par **toute** carte qui lit l'historique, il
l'est par celles qui « savent » la composition du bloc. **Sous gel : 0 violation sur 48**, espérance du premier bloc
égale à 1. **Maximum exact des lois constantes sur les tirages mêmes (forme du juge à maximum), même carte non gelée :
0 violation** ; rapport au monde : 0 violation. Fichier : `preuve-idee-1-1-poids-du-nul-v2-outils/sortie-verif-preuve-idee-1-1-v2-C.txt` (`df956fe1f1007d3c34e15f327e949b60b1d27004d5642ec7ab0c0bc48325f637`).

**Pourquoi le juge à maximum reste valide sur les mêmes cartes.** Son numérateur est le produit des q_s, prévisibles
(H5), et son dénominateur majore la vraisemblance du monde : lemme Λ. La projection, elle, fait entrer dans φ et dans c
les q_s du bloc, qui lisent les issues du bloc : le pas 1 du lemme 5 tombe.

**À l'échelle du juge** (chiffres de [R-PROJ] § 5, `7bfaa88e…`, non refaits ici ; rejoués en partie par [SYN] § 3) :
« sans_remise » [70, 70, 70] dans un monde uniforme, méthode par blocs sur le membre linéaire : 206/2 000 promues
[0,090 ; 0,117] ; carte écrite pour l'attaque (hors grammaire), monde ½·L₁ + ½·L₂ : 904/2 000 [0,430 ; 0,474], et 19/60
pour M3 avec le code de l'auteur ; témoin gelé : 0/13 000. Limites dites par la réfutation : dans le juge complet, le
membre ordinaire « uniforme » couvrirait le premier cas ; les mélanges de « sans_remise » cassent l'espérance (1,011 à
1,031) sans rien promouvoir (0/4 000) ; la carte d'attaque n'est pas vérifiée comme écrivable. **Ouvert** : qu'une carte
de la grammaire atteigne le trou dans le juge complet (minimum avec W^reste).

## 12. Lois connues seulement par tirages : le certificat « comme si exact » n'est pas valide

**Proposition 14.** Si les sommets L_j sont remplacés par des estimations L̂_j, la borne certifiée calculée majore le
maximum sur la famille estimée F̂, pas sur la vraie famille F. H4 n'est plus vraie pour F, et un monde de F n'est
généralement pas dans F̂ (H3 fausse pour F̂) : ni le théorème 1 ni le théorème 8 ne s'appliquent. Le défaut touche aussi
bien le maximum certifié que la projection.
*Preuve.* Le lemme du certificat borne sup_{F̂}, par construction ; pour une copie exacte q = P* ∈ F \ F̂, la richesse
croît comme n·KL(P* ‖ projection sur F̂) en espérance. ∎
**Calcul exact** (section 13, partie E ; deux cellules, deux issues, L(1 | g) = (0,1 ; 0,9), famille « loi connue plus
bruit aveugle commun », carte = monde = L, lecture à la fin seulement, probabilité exacte par somme sur tous les comptes) :
avec N = 10 tirages par cellule pour estimer L et m = 20 tirages frais par cellule, P(copie promue) = **0,0567 > α** ;
N = 20 : 0,0192 ; N = 50 : 0,0016 ; avec m = 100 tirages frais par cellule (200 en tout, comme le juge), **0,2880**
(N = 10) et **0,1810** (N = 20), au lieu d'au plus 0,05 ; avec les vraies lois, 0,0000 dans les cinq cas. Le défaut
croît avec le nombre de tirages frais et décroît avec N, comme le dit la proposition (n·KL). Fichier :
`preuve-idee-1-1-poids-du-nul-v2-outils/sortie-verif-preuve-idee-1-1-v2-E.txt` (`c3b10a9cdbd0b97b64ab6ab17177b21b5db6e03b3612a65148d08d4ed0b1bd27`). Pour comparaison, [PROJ] § 7 mesure 429/2 000
[0,197 ; 0,233] à 50 tirages par loi, sans traits (`681eb7f5…`).
**Correction possible** (certificat robuste sur une boule de confiance, [PROJ] § 7) : taille au plus α + δ dans le cas
d'école sans traits, si l'inégalité de concentration employée est juste (Weissman et al., **non relue sur PDF**) ; avec
des traits, non faite. **Sans objet pour le juge actuel**, dont les lois connues sont des lois de la grammaire, connues
exactement ; à reprendre seulement si une archive à lois estimées apparaît.

## 13. Vérifications par énumération exacte

Script `verif_preuve_idee_1_1_v2.py` (annexe, recopié en entier ; versé à `preuve-idee-1-1-poids-du-nul-v2-outils/verif_preuve_idee_1_1_v2.py`, `134661a14e67cca72fdf93bf75cddcfaaa02b57f54e808e6ab794f457af53e30`, compagnon `.sha256`), lancé par
`.venv/bin/python -I -B verif_preuve_idee_1_1_v2.py <partie>` depuis le dossier de travail de la session ; graines
`numpy.random.SeedSequence(entropy=202611152, spawn_key=(partie,))`. Aucun code du juge n'est importé ; les deux lois qui
lisent l'historique sont recopiées de [SP]. Les sorties emploient la numérotation de [PROJ] (« lemme 1 », « théorème 4 »), qui correspond ici au
lemme 5 et au théorème 8 ; la partie D numérote « théorème 1 » comme ici. La partie D a d'abord été lancée sur n = 12
(arrêtée par son PID après 17 minutes, sans sortie lue) puis réduite à n = 10 ; seule la sortie ci-dessous existe. Sorties (une par partie, empreintes ci-dessous ; recopiées ici) :

Partie A — `preuve-idee-1-1-poids-du-nul-v2-outils/sortie-verif-preuve-idee-1-1-v2-A.txt` (`4ce53bbdb7666c3a8d5ecf121cbb64d0c848bbec13ff81cd2ad0b01bd1153255`) :

```
A. lemme 1, 200 jeux (K=3, b=3, 2 cellules, 2 lois connues) : plus grand log sup_θ E_θ[e_B] projection 4.441e-16 ; φ au hasard -9.092e-04
A. sans division par le certificat (φ au hasard) : plus grand log max_sommets E_θ[Π r] 11.038
A. lemme 2 : certificat de la projection (3000 pas d'EM) entre 1.000000 et 1.000021
```

Partie B — `preuve-idee-1-1-poids-du-nul-v2-outils/sortie-verif-preuve-idee-1-1-v2-B.txt` (`2767b8d5372a71e8bcc5e8fbacc4e773d6bd09fd9dc19504ee5ffd1c0fc5dd7f`) :

```
B. théorème 4, 40 plans (K=2, n=8, blocs de 2, familles {cellules A, linéaire}), mondes de la famille A (projection de la carte, 3 au hasard, 6 sommets) : plus grand P(promotion)/α α=0.5 : 0.8701 ; α=0.25 : 0.3002 ; α=0.1 : 0.6162 ; α=0.05 : 0.3059
```

Partie C — `preuve-idee-1-1-poids-du-nul-v2-outils/sortie-verif-preuve-idee-1-1-v2-C.txt` (`df956fe1f1007d3c34e15f327e949b60b1d27004d5642ec7ab0c0bc48325f637`) (extrait : lignes C1, résumé, et les 12 lignes de violation) :

```
C1. sans_remise [1, 1], un bloc de 2, nul = lois constantes :
    p = 0.5 (nu) : E[e_B] = 1.333333 (16/3·p(1−p) = 1.333333) ; plus grand certificat 1.000000
    p = 0.5 (gel) : E[e_B] = 1.000000 (16/3·p(1−p) = 1.333333) ; plus grand certificat 1.000000
    p = 0.3 (nu) : E[e_B] = 1.120000 (16/3·p(1−p) = 1.120000) ; plus grand certificat 1.000000
    p = 0.3 (gel) : E[e_B] = 1.000000 (16/3·p(1−p) = 1.120000) ; plus grand certificat 1.000000
    p = 0.1 (nu) : E[e_B] = 0.480000 (16/3·p(1−p) = 0.480000) ; plus grand certificat 1.000000
    p = 0.1 (gel) : E[e_B] = 1.000000 (16/3·p(1−p) = 0.480000) ; plus grand certificat 1.000000
C2. monde constant p = 1/2 ; par carte : E[e_B1] (nu / gel) ; P(∃ fin de bloc : W ≥ 1/α) exacte (nu / gel / maximum certifié sur les tirages mêmes / rapport au monde)
    sans_remise [1, 1]                         b=2 n= 2 E[e_B1] 1.3333 / 1.0000 ; sup_α P/α : nu 1.3333 (α = 0.3750) ; gel 0.0000 ; maximum 1.0000 ; rapport au monde 1.0000 ; P(nu, α = 0,05) 0.0000  <-- Ville violée
    sans_remise [1, 1]                         b=2 n= 8 E[e_B1] 1.3333 / 1.0000 ; sup_α P/α : nu 1.3333 (α = 0.3750) ; gel 0.0000 ; maximum 1.0000 ; rapport au monde 1.0000 ; P(nu, α = 0,05) 0.0000  <-- Ville violée
    sans_remise [1, 1]                         b=2 n=12 E[e_B1] 1.3333 / 1.0000 ; sup_α P/α : nu 1.3333 (α = 0.3750) ; gel 0.0000 ; maximum 1.0000 ; rapport au monde 1.0000 ; P(nu, α = 0,05) 0.0000  <-- Ville violée
    sans_remise [2, 2]                         b=2 n= 8 E[e_B1] 1.1657 / 1.0000 ; sup_α P/α : nu 1.0133 (α = 0.2930) ; gel 0.0000 ; maximum 1.0000 ; rapport au monde 1.0000 ; P(nu, α = 0,05) 0.0000  <-- Ville violée
    sans_remise [2, 2]                         b=2 n=12 E[e_B1] 1.1657 / 1.0000 ; sup_α P/α : nu 1.0400 (α = 0.2930) ; gel 0.0000 ; maximum 1.0000 ; rapport au monde 1.0000 ; P(nu, α = 0,05) 0.0000  <-- Ville violée
    sans_remise [2, 2]                         b=3 n=12 E[e_B1] 1.4311 / 1.0000 ; sup_α P/α : nu 1.0061 (α = 0.3902) ; gel 0.0000 ; maximum 0.8438 ; rapport au monde 1.0000 ; P(nu, α = 0,05) 0.0000  <-- Ville violée
    sans_remise [2, 2]                         b=4 n=12 E[e_B1] 1.5404 / 1.0000 ; sup_α P/α : nu 1.0580 (α = 0.3545) ; gel 0.0000 ; maximum 1.0000 ; rapport au monde 1.0000 ; P(nu, α = 0,05) 0.0000  <-- Ville violée
    sans_remise [3, 3]                         b=4 n=12 E[e_B1] 1.4440 / 1.0000 ; sup_α P/α : nu 1.0904 (α = 0.6417) ; gel 0.0000 ; maximum 0.8000 ; rapport au monde 1.0000 ; P(nu, α = 0,05) 0.0083  <-- Ville violée
    sans_remise [3, 3]                         b=6 n=12 E[e_B1] 1.6793 / 1.0000 ; sup_α P/α : nu 1.0001 (α = 0.3125) ; gel 0.0000 ; maximum 1.0000 ; rapport au monde 1.0000 ; P(nu, α = 0,05) 0.0000  <-- Ville violée
    sans_remise [6, 6]                         b=2 n=12 E[e_B1] 1.0455 / 1.0000 ; sup_α P/α : nu 1.0242 (α = 0.9249) ; gel 0.0000 ; maximum 1.0000 ; rapport au monde 1.0000 ; P(nu, α = 0,05) 0.0000  <-- Ville violée
    sans_remise [6, 6]                         b=3 n=12 E[e_B1] 1.0982 / 1.0000 ; sup_α P/α : nu 1.0354 (α = 0.8474) ; gel 0.0000 ; maximum 1.0000 ; rapport au monde 1.0000 ; P(nu, α = 0,05) 0.0000  <-- Ville violée
    sans_remise [6, 6]                         b=4 n=12 E[e_B1] 1.1609 / 1.0000 ; sup_α P/α : nu 1.0553 (α = 0.8259) ; gel 0.0000 ; maximum 1.0000 ; rapport au monde 1.0000 ; P(nu, α = 0,05) 0.0000  <-- Ville violée
C2. configurations où Ville est violée (sup_α P/α > 1) : nu 12 sur 48 ; gel 0 ; maximum certifié 0 ; rapport au monde 0 ; plus grand E[e_B1] sous gel 1.000000
    (les 36 autres lignes de C2, sans violation, sont dans le fichier)
```

Partie D — `preuve-idee-1-1-poids-du-nul-v2-outils/sortie-verif-preuve-idee-1-1-v2-D.txt` (`9b2c9008047e92573ce700afd558d94eabf437c3c36d91feecf33ff9fd903e0a`) :

```
D. 12 plans (K=2, n=10, membres {cellules A, cellules B, linéaire}, monde dans A ; projection de la carte et deux mondes au hasard) — plus grand P(règle)/α :
    J9              α=0.5 : 0.3085 ; α=0.25 : 0.3767 ; α=0.1 : 0.6602
    J9-D40          α=0.5 : 0.4762 ; α=0.25 : 0.4570 ; α=0.1 : 0.6849
    par membre      α=0.5 : 0.4762 ; α=0.25 : 0.4570 ; α=0.1 : 0.6849
    réunion         α=0.5 : 0.4762 ; α=0.25 : 0.4570 ; α=0.1 : 0.6849
    Ville du monde  α=0.5 : 0.8998 ; α=0.25 : 0.9280 ; α=0.1 : 0.8307
D. suites promues, sommées sur les plans et les mondes (J9 / J9-D40 / par membre) : α=0.5 : 2775/5136/5139 ; α=0.25 : 1302/2097/2097 ; α=0.1 : 435/651/651
D. statistique S = min_m max_t W^m_t : plus grande espérance 2.2828 ; E[max_t Λ_t] la plus grande 4.8289
D. forme arrêtée membre par membre E' (seuil c = 4 fixé d'avance) : plus grande espérance 0.8056
D. exemple à la main : E[max(Λ_1, Λ_2)] = 1.4000
```

Partie E — `preuve-idee-1-1-poids-du-nul-v2-outils/sortie-verif-preuve-idee-1-1-v2-E.txt` (`c3b10a9cdbd0b97b64ab6ab17177b21b5db6e03b3612a65148d08d4ed0b1bd27`) :

```
E. N = 10 tirages par cellule pour estimer L, m = 20 tirages frais par cellule, lecture à la fin : P(copie promue) certificat « comme si exact » 0.0567 ; vraies lois 0.0000 (α = 0.05)
E. N = 20 tirages par cellule pour estimer L, m = 20 tirages frais par cellule, lecture à la fin : P(copie promue) certificat « comme si exact » 0.0192 ; vraies lois 0.0000 (α = 0.05)
E. N = 50 tirages par cellule pour estimer L, m = 20 tirages frais par cellule, lecture à la fin : P(copie promue) certificat « comme si exact » 0.0016 ; vraies lois 0.0000 (α = 0.05)
E. N = 10 tirages par cellule pour estimer L, m = 100 tirages frais par cellule, lecture à la fin : P(copie promue) certificat « comme si exact » 0.2880 ; vraies lois 0.0000 (α = 0.05)
E. N = 20 tirages par cellule pour estimer L, m = 100 tirages frais par cellule, lecture à la fin : P(copie promue) certificat « comme si exact » 0.1810 ; vraies lois 0.0000 (α = 0.05)
```


**Lecture.**
- **A (lemme 5).** Sur 200 jeux (K = 3, blocs de 3, deux cellules, deux lois connues dépendant de l'instance), le plus
  grand log sup_θ E_θ[e_B] vaut 4,4·10⁻¹⁶ avec la projection (zéro à la précision de la machine : l'espérance vaut 1 en
  θ = φ*, lemme 6) et −9,1·10⁻⁴ avec un φ tiré au hasard : jamais au-dessus de 0. Sans la division par le certificat, la
  même quantité monte à 11,0 : la division est nécessaire. Le certificat de la projection (3 000 pas) est entre 1,000000
  et 1,000021 (lemme 6, à l'arrêt de l'optimiseur près). L'espérance est calculée par la somme sur les 27 suites, pas par
  la formule produit : le pas 1 est éprouvé.
- **B (théorème 8).** Sur 40 plans (K = 2, n = 8, blocs de 2, minimum de deux familles), pour 10 mondes de la famille par
  plan (dont la projection de la carte, pire cas de [R-PROJ]), le plus grand P(promotion)/α vaut 0,87 (α = 0,5), 0,30
  (0,25), 0,62 (0,1), 0,31 (0,05) : toujours sous 1, et la borne mord (0,87).
- **C (sans P4).** Voir section 11.
- **D (théorèmes 1, 10, 11 ; section 10.2 ; proposition 13).** Sur 12 plans (K = 2, n = 10, trois membres dont deux par
  morceaux, maximum certifié sur les tirages mêmes, monde dans un membre), le plus grand P/α vaut au plus 0,66 (J9),
  0,68 (J9-D40), 0,68 (par membre), 0,68 (réunion), sous 0,93 pour l'événement de Ville du monde, qui contient la réunion
  sur **chaque** suite (vérifié par assertion). Promotions sommées : J9 2 775, J9-D40 5 136, par membre 5 139 à α = 0,5
  (le gain de la lecture dense est grand ici parce que n est petit ; il ne se transpose pas). **S = min_m max_t W^m_t a
  une espérance jusqu'à 2,28** (et E[max_t Λ_t] jusqu'à 4,83) : S n'est pas une valeur e. **E′_c (c = 4) a une espérance
  au plus 0,81** : sous 1, comme la proposition 13 le dit. Exemple à la main : 1,4000.
- **E (lois estimées).** Voir section 12.
- **Ce que ces vérifications ne montrent pas.** Ce sont de petits cas (n ≤ 12, ou des comptes) ; elles éprouvent les pas
  des preuves, pas le code du juge, ni le banc, ni les ampleurs à n = 200. Les maxima sont calculés par
  espérance-maximisation avec certificat (borne haute valide quel que soit l'arrêt), sauf en C (maximum exact des lois
  constantes).

## 14. Ce qui est prouvé, plausible, ouvert

| énoncé | statut | appui |
|---|---|---|
| théorème 1 : La, Ld de taille ≤ α sur leur classe, tout ensemble d'instants | **prouvé** (sous H4 ; réserve log-linéaire héritée) | § 6 ; partie D |
| proposition 2 : encadrements J8 / La / Ld / J9, à l'écart résiduel près | **prouvé** sur la lecture de [V9] (coupes l. 413, élagage l. 276 à 288) | § 6 |
| corollaire 1 : valeur e arrêtée ; e-BH | valeur e **prouvée** ; théorème e-BH **cité, non relu** | § 6 |
| lemme 3 : garde « refus » complète sur la grammaire | **prouvé sur la copie `94bfd92`** ; en production, **plausible** (même code à vérifier) | § 7 |
| lemme 4 : garde « gel » ; la carte jugée est la carte gelée | **prouvé** | § 7 |
| lemmes 5, 6, proposition 7, théorème 8, corollaire 9 : projection par blocs | **prouvés sous P1 à P6** | § 8 ; parties A, B |
| lecture d'un processus de blocs entre deux fins de bloc | **ouvert** | § 8 |
| pari à fraction sous projection | **ouvert** (non traité) | § 8 |
| théorème 10 : J9-D40, et valeur e par le maximum des deux engagements | **prouvé** | § 9 |
| théorème 11 : J9-D (réunion) de taille ≤ α pour la carte seule | **prouvé** | § 10.1 ; partie D |
| S n'est pas une valeur e ; ne se branche pas tel quel sur e-BH | **prouvé** (contre-exemple exact) | § 10.2 ; partie D |
| propositions 12, 13 : valeurs e tirées de J9-D | **prouvées** ; adoption, puissance, héritage : **ouverts** | § 10.3 |
| J9-Dc : borne certifiée coupe par coupe dans la copie renommée | **plausible**, préalable de code | § 10.4 |
| sans P4, le lemme 5 et Ville tombent, carte de la grammaire | **prouvé** (calcul exact) | § 11 ; partie C |
| une carte de la grammaire atteint le trou dans le juge complet | **ouvert** | § 11 |
| lois estimées : certificat « comme si exact » non valide | **prouvé** (calcul exact) | § 12 ; partie E |
| certificat robuste pour lois estimées | **plausible** sans traits (inégalité non relue) ; **ouvert** avec traits | § 12 |
| réserve log-linéaire (marge de Newton) | **ouvert**, héritée du v8 | H4 |
| références : Ville, inférence universelle, e-BH, Benjamini-Yekutieli, numéraire, « Safe testing », Weissman et al. | **non relues sur PDF** ; aucun chiffre n'en est tiré (R7) ; les lemmes V, Λ, M, 12 sont démontrés ici sans elles | — |

## 15. Contre-lecture à faire (R2)

Sous-agent neuf, qui n'a écrit ni cette pièce, ni les brouillons du préenregistrement v2, ni la synthèse, ni les
rendus des angles. Fichiers à lire, explicitement : cette pièce ; [P1], [CL], [PROJ] § 3 et § 7, [R-PROJ] § 1 et § 5,
[R-LIB] § 3 et § 10, [R-UNI] § 8.1, [B1] (bras 3 et 5), [CL2] (M2, point 5) ; [SP] l. 55 à 175 et 242 à 246 ; [V9]
l. 15 à 45, 100 à 112, 218 à 292, 398 à 417 ; [CY] l. 312 à 330 ; le script de l'annexe. Points à éprouver : P4 telle
qu'écrite suffit-elle au pas 1 du lemme 5 ; le lemme 3 couvre-t-il toute la grammaire lue ; la carte jugée sous gel ;
l'inclusion du pas 2 du théorème 11 et le minimum des bornes ; l'exemple E[S] = 1,4 ; la proposition 13 (temps d'arrêt
propre à chaque membre) ; les énumérations des parties A à E.

## Citations obligatoires (N-064, N-067)

POPPER (Huang et al., ICML 2025), `docs/sources/pdf/huang-2025-icml-pmlr-267-popper-automated-hypothesis-validation-agentic-sequential-falsifications.pdf`
(`a3c4b3701543a84a74602ae46a624b955e201bb83baeea2c219213a0e65b4998`) ; Dwork et al., arXiv 1506.02629 (2015),
`docs/sources/pdf/anteriorite-P-041-v2/c8/1506.02629.pdf` (`dcfbb9aa401c62949123be2d74787c4f9cca48597f18860760ef1580ddb4bc71`) ;
Blum et Hardt, « The Ladder », arXiv 1502.04585 (2015), `docs/sources/pdf/anteriorite-P-041-v2/c8/1502.04585.pdf`
(`957ef4739df371a0a778360f0db4252a62f7c85abcd8343f581cd6250b1d31fe`) ; Co-Scientist (Gottweis et al., Nature 655,
p. 487-496, 2026), `docs/sources/co-scientist-v1/gottweis-2026-nature-655-487-accelerating-scientific-discovery-with-co-scientist.pdf`
(`351f49d89d2f4f4ed84eed4225c09cc95470c41aa3becd0aa3e06b3bd8ba54c3`) ; et la liste de `docs/decisions/decision-N-067-v1.md`
(`966dd9dc3fae61cbe1f10ee2a54f401ddf7af5041eeaacd81ad9f8b264661589`), section 6, dont Qu, Chen et Wang, « Propose, Don't
Judge », arXiv 2609.27051, `docs/sources/pdf/anteriorite-P-041-v2/c8/2609.27051.pdf`
(`2a8ded0119a1db422aa548fdc3be80b2861f0548bc8166256be60572a2fddb03`). Empreintes recalculées le 15 novembre ; contenu non
relu par moi, aucun chiffre n'en est tiré ; aucune revendication n'est faite ici (le nul formé des lois connues reste
sous la clause d'usage public de N-067).

## Annexe — script des vérifications (recopié en entier)

```python
"""Vérifications par énumération exacte des suites d'issues, pour la preuve, version 2, de l'idée 1.1 (poids du nul).
Processeur seul ; numpy et scipy ; aucun code du juge n'est importé ni exécuté (la logique des deux lois de la grammaire
qui lisent l'historique, « sans_remise » et « moyenne_glissante », est recopiée de selection_pari.proba, copie 94bfd92).

Parties :
 A. lemme 1 (projection par blocs, certificat exact) : sup sur θ de E_θ[e_B] ≤ 1, par énumération des K^b suites ;
    nécessité de la division par le certificat.
 B. théorème 4 (minimum de processus par blocs, Ville aux fins de bloc) : P(promotion) exacte ≤ α.
 C. contre-exemple sans P4 : cartes de la grammaire qui lisent l'historique du bloc ; forme « gel » ; maximum certifié.
 D. théorème 1 (nul limité, maximum certifié sur les tirages mêmes), lecture à tous les instants, rejet par famille,
    réunion J9 ∪ J9-D40 ∪ (par membre) ; statistique min_m max_t (pas une valeur e) ; forme arrêtée membre par membre.
 E. lois connues seulement par tirages : certificat « comme si exact » non valide (probabilité exacte).
Graines : numpy.random.SeedSequence(20261115_2), dérivées par partie (spawn_key).
"""
import itertools
import math
import sys

import numpy as np
from scipy.optimize import minimize

PLANCHER = 1e-12
RACINE = 202611152


def rng_de(cle):
    return np.random.default_rng(np.random.SeedSequence(entropy=RACINE, spawn_key=(cle,)))


def normaliser(p):
    p = np.maximum(PLANCHER, np.asarray(p, dtype=float))
    return p / p.sum()


# ---------------------------------------------------------------------------------------------------------------------
# Famille « poids des lois connues propres à la cellule, bruit aveugle commun » (forme du v9 et du membre linéaire du v8).
# Paramètre linéaire x = (μ_{c,j} pour c < C, j < J ; ρ_k pour k < K), Σ_j μ_{c,j} + Σ_k ρ_k = 1 pour chaque c.
# L : (n, J, K) lois connues aux instances ; cel : (n,) cellule de chaque instance.
# ---------------------------------------------------------------------------------------------------------------------
def probas_famille(x, L, cel, C):
    n, J, K = L.shape
    mu = x[:C * J].reshape(C, J)
    rho = x[C * J:]
    return np.einsum("nj,njk->nk", mu[cel], L) + rho[None, :]


def em_famille(Y, L, cel, C, iterations=2000):
    """EM sur la forme « mélange à deux niveaux » (bruit avec probabilité r, sinon loi j de la cellule) ; Y (n, K) poids
    des issues : une indicatrice (maximum de vraisemblance) ou q_s (projection d'information inverse). Rend x."""
    n, J, K = L.shape
    r, rt, w = 0.5, np.full(K, 1.0 / K), np.full((C, J), 1.0 / J)
    tot = Y.sum()
    for _ in range(iterations):
        bruit = r * rt[None, :]                                          # (n, K)
        lois = (1 - r) * w[cel][:, :, None] * L                          # (n, J, K)
        p = np.maximum(bruit + lois.sum(1), 1e-300)
        rb = (Y * bruit / p)                                             # (n, K)
        rl = (Y[:, None, :] * lois / p[:, None, :]).sum(2)               # (n, J)
        nb = rb.sum()
        r = nb / tot
        rt = rb.sum(0) / max(nb, 1e-300)
        for c in range(C):
            s = rl[cel == c].sum(0)
            if s.sum() > 0:
                w[c] = s / s.sum()
    return np.concatenate([((1 - r) * w).ravel(), r * rt])


def gradient_sommets(Y, L, cel, C, x):
    """Plus grande valeur, sur les sommets du polytope, de la forme linéaire ∇f(x) où f(x) = Σ_s Σ_y Y_sy log p_x(y|x_s)."""
    n, J, K = L.shape
    p = np.maximum(probas_famille(x, L, cel, C), 1e-300)
    R = Y / p                                                            # (n, K)
    g_rho = R.sum(0)                                                     # sommet ρ = e_k
    g_mu = np.einsum("nk,njk->nj", R, L)                                 # (n, J)
    tot_mu = sum(g_mu[cel == c].sum(0).max() for c in range(C) if (cel == c).any())
    return max(g_rho.max(), tot_mu)


def max_certifie(y, L, cel, C, iterations=2000):
    """Borne haute certifiée (valeur atteinte + écart de Frank-Wolfe, bornée par 0) du maximum de vraisemblance de la
    famille sur les issues y (n,)."""
    n, J, K = L.shape
    Y = np.eye(K)[y]
    x = em_famille(Y, L, cel, C, iterations)
    f = float(np.log(np.maximum(probas_famille(x, L, cel, C)[np.arange(n), y], 1e-300)).sum())
    ecart = max(0.0, gradient_sommets(Y, L, cel, C, x) - n)
    return min(0.0, f + ecart)


def em_lot(Y, L, cel, C, iterations=400):
    """EM par lots : Y (S, n, K) poids des issues (indicatrices, comptes ou q_s) ; L (S ou 1, n, J, K) ; cel (n,)."""
    S, n, K = Y.shape
    J = L.shape[2]
    r = np.full(S, 0.5); rt = np.full((S, K), 1.0 / K); w = np.full((S, C, J), 1.0 / J)
    tot = Y.sum((1, 2))
    masques = [cel == c for c in range(C)]
    for _ in range(iterations):
        bruit = r[:, None, None] * rt[:, None, :]
        lois = (1 - r)[:, None, None, None] * w[:, cel][:, :, :, None] * L
        p = np.maximum(bruit + lois.sum(2), 1e-300)
        rb = Y * bruit / p
        rl = (Y[:, :, None, :] * lois / p[:, :, None, :]).sum(3)
        nb = rb.sum((1, 2))
        r = nb / tot
        rt = rb.sum(1) / np.maximum(nb, 1e-300)[:, None]
        for c in range(C):
            if masques[c].any():
                sc = rl[:, masques[c]].sum(1)
                w[:, c] = sc / np.maximum(sc.sum(1, keepdims=True), 1e-300)
    return r, rt, w


def max_certifie_lot(Y, L, cel, C, iterations=400):
    """Borne haute certifiée du maximum de Σ Y log p_x sur la famille, par lots (valeur atteinte + écart de Frank-Wolfe,
    bornée par 0)."""
    r, rt, w = em_lot(Y, L, cel, C, iterations)
    bruit = r[:, None, None] * rt[:, None, :]
    p = np.maximum(bruit + ((1 - r)[:, None, None, None] * w[:, cel][:, :, :, None] * L).sum(2), 1e-300)
    f = (Y * np.log(p)).sum((1, 2))
    R = Y / p
    g_rho = R.sum(1).max(1)
    g_mu = np.einsum("snk,snjk->snj", R, np.broadcast_to(L, (Y.shape[0],) + L.shape[1:]))
    tot_mu = np.zeros(Y.shape[0])
    for c in range(C):
        if (cel == c).any():
            tot_mu += g_mu[:, cel == c].sum(1).max(1)
    ecart = np.maximum(0.0, np.maximum(g_rho, tot_mu) - Y.sum((1, 2)))
    return np.minimum(0.0, f + ecart)


def certificat_bloc(q, L, cel, C, phi):
    """c_B(φ) = max_v (1/b) Σ_s Σ_y P_v(y|x_s) q_s(y) / P_φ(y|x_s) (lemme 1)."""
    return gradient_sommets(q, L, cel, C, phi) / q.shape[0]


def sommets(C, J, K):
    out = []
    for k in range(K):
        x = np.zeros(C * J + K); x[C * J + k] = 1.0; out.append(x)
    for choix in itertools.product(range(J), repeat=C):
        x = np.zeros(C * J + K)
        for c, j in enumerate(choix):
            x[c * J + j] = 1.0
        out.append(x)
    return out


def point_au_hasard(rng, C, J, K):
    r = rng.uniform()
    rho = rng.dirichlet(np.ones(K)) * r
    mu = rng.dirichlet(np.ones(J), size=C) * (1 - r)
    return np.concatenate([mu.ravel(), rho])


def point_de_parametres(z, C, J, K):
    """Paramétrage libre → point du polytope (pour la recherche du pire θ)."""
    z = np.clip(z, -30.0, 30.0)
    r = 1 / (1 + math.exp(-z[0]))
    rt = np.exp(z[1:1 + K] - z[1:1 + K].max()); rt /= rt.sum()
    zw = z[1 + K:].reshape(C, J)
    w = np.exp(zw - zw.max(1, keepdims=True)); w /= w.sum(1, keepdims=True)
    return np.concatenate([((1 - r) * w).ravel(), r * rt])


def toutes_suites(K, n):
    return np.array(list(itertools.product(range(K), repeat=n)), dtype=int)


# ---------------------------------------------------------------------------------------------------------------------
def partie_A(repetitions=200):
    """Lemme 1 : pour une carte sans mémoire et φ quelconque fixé avant le bloc, sup_θ E_θ[e_B] ≤ 1 ; espérance calculée
    par la somme sur les K^b suites (pas par la formule produit, pour éprouver le pas 1)."""
    K, J, C, b = 3, 2, 2, 3
    rng = rng_de(1)
    suites = toutes_suites(K, b)
    pire = {"projection": -np.inf, "phi au hasard": -np.inf}
    pire_sans_division = -np.inf
    cert_projection = []
    for _ in range(repetitions):
        L = rng.dirichlet(np.ones(K), size=(b, J))
        cel = np.array([0, 1, rng.integers(0, 2)])
        q = rng.dirichlet(np.ones(K) * 0.7, size=b)
        phis = {"projection": em_famille(q, L, cel, C, 3000), "phi au hasard": point_au_hasard(rng, C, J, K)}
        for nom, phi in phis.items():
            Pphi = np.maximum(probas_famille(phi, L, cel, C), 1e-300)
            r = q / Pphi                                                  # (b, K)
            c = certificat_bloc(q, L, cel, C, phi)
            if nom == "projection":
                cert_projection.append(c)
            num = np.prod(r[np.arange(b)[None, :], suites], axis=1)       # (K^b,)
            e = num / max(1.0, c) ** b

            def esperance(theta, e=e):
                Pt = probas_famille(theta, L, cel, C)
                return float((np.prod(Pt[np.arange(b)[None, :], suites], axis=1) * e).sum())

            cands = sommets(C, J, K) + [point_au_hasard(rng, C, J, K) for _ in range(100)]
            meilleur = max(esperance(t) for t in cands)
            for _ in range(3):
                z0 = rng.normal(size=1 + K + C * J)
                res = minimize(lambda z: -esperance(point_de_parametres(z, C, J, K)), z0, method="Nelder-Mead",
                               options={"maxiter": 3000, "xatol": 1e-10, "fatol": 1e-14})
                meilleur = max(meilleur, -res.fun)
            pire[nom] = max(pire[nom], math.log(meilleur))
            if nom == "phi au hasard":
                ns = max(float((np.prod(probas_famille(t, L, cel, C)[np.arange(b)[None, :], suites], axis=1) * num).sum())
                         for t in sommets(C, J, K))
                pire_sans_division = max(pire_sans_division, math.log(ns))
    cp = np.array(cert_projection)
    print(f"A. lemme 1, {repetitions} jeux (K=3, b=3, 2 cellules, 2 lois connues) : plus grand log sup_θ E_θ[e_B] "
          f"projection {pire['projection']:.3e} ; φ au hasard {pire['phi au hasard']:.3e}")
    print(f"A. sans division par le certificat (φ au hasard) : plus grand log max_sommets E_θ[Π r] {pire_sans_division:.3f}")
    print(f"A. lemme 2 : certificat de la projection (3000 pas d'EM) entre {cp.min():.6f} et {cp.max():.6f}")


# ---------------------------------------------------------------------------------------------------------------------
def processus_blocs(q, L, cel_list, C_list, b, suites):
    """log W aux fins de bloc pour chaque famille (carte sans mémoire : projections et certificats au gel) ; rend
    (S, nb_blocs) = minimum sur les familles."""
    n = q.shape[0]
    nb = n // b
    logW = None
    for cel, C in zip(cel_list, C_list):
        lw = np.zeros((len(suites), nb))
        acc = np.zeros(len(suites))
        for B in range(nb):
            idx = np.arange(B * b, (B + 1) * b)
            phi = em_famille(q[idx], L[idx], cel[idx], C, 1500)
            Pphi = np.maximum(probas_famille(phi, L[idx], cel[idx], C), 1e-300)
            r = q[idx] / Pphi
            c = certificat_bloc(q[idx], L[idx], cel[idx], C, phi)
            acc = acc + np.log(r[np.arange(b)[None, :], suites[:, idx]]).sum(1) - b * math.log(max(1.0, c))
            lw[:, B] = acc
        logW = lw if logW is None else np.minimum(logW, lw)
    return logW


def partie_B(repetitions=40):
    K, J, n, b = 2, 2, 8, 2
    rng = rng_de(2)
    suites = toutes_suites(K, n)
    alphas = (0.5, 0.25, 0.1, 0.05)
    pire_rapport = {a: 0.0 for a in alphas}
    for i in range(repetitions):
        L = rng.dirichlet(np.ones(K), size=(n, J))
        celA = rng.integers(0, 2, size=n)
        cel1 = np.zeros(n, dtype=int)
        q = rng.dirichlet(np.ones(K) * 0.6, size=n)
        logW = processus_blocs(q, L, [celA, cel1], [2, 1], b, suites)
        mondes = [em_famille(q, L, celA, 2, 3000)] + [point_au_hasard(rng, 2, J, K) for _ in range(3)] + sommets(2, J, K)
        for theta in mondes:
            P = probas_famille(theta, L, celA, 2)
            prob = np.prod(P[np.arange(n)[None, :], suites], axis=1)
            for a in alphas:
                pa = float(prob[(logW >= math.log(1 / a)).any(1)].sum())
                pire_rapport[a] = max(pire_rapport[a], pa / a)
    print(f"B. théorème 4, {repetitions} plans (K=2, n=8, blocs de 2, familles {{cellules A, linéaire}}), mondes de la "
          f"famille A (projection de la carte, 3 au hasard, 6 sommets) : plus grand P(promotion)/α "
          + " ; ".join(f"α={a} : {v:.4f}" for a, v in pire_rapport.items()))


# ---------------------------------------------------------------------------------------------------------------------
# Lois de la grammaire qui lisent l'historique (recopie de selection_pari.proba, copie 94bfd92, l. 131-134 et 156-159).
def sans_remise(composition, historique, t):
    vus = np.bincount(np.asarray(historique[:t], dtype=int), minlength=len(composition)) if t else np.zeros(len(composition))
    return normaliser([max(0, c - v) for c, v in zip(composition, vus)])


def moyenne_glissante(k, fenetre, lissage, historique, t):
    recents = list(historique[max(0, t - fenetre):t])
    compte = np.bincount(np.asarray(recents, dtype=int), minlength=k) if recents else np.zeros(k)
    return normaliser([(compte[i] + lissage) / (len(recents) + k * lissage) for i in range(k)])


def lois_realisees(carte, y, b, forme):
    """q_s pour s = 0..n−1 : « nu » = historique complet (y[:s]) ; « gel » = historique arrêté au début du bloc de s."""
    out = []
    for s in range(len(y)):
        h = y[:s] if forme == "nu" else y[:(s // b) * b]
        out.append(carte(h, s))
    return np.array(out)


def partie_C():
    K = 2
    # (C1) exemple exact : sans_remise [1, 1], un bloc de 2, famille des lois constantes (sommets δ_0, δ_1), projection =
    # moyenne des lois réalisées (minimise Σ KL(q_s ‖ φ) sur les lois constantes), certificat exact.
    def e_bloc(Q, yb):
        phi = Q.mean(0)
        c = max((Q[:, k] / phi[k]).mean() for k in range(Q.shape[1]))
        return float(np.prod(Q[np.arange(len(yb)), yb] / phi[yb]) / max(1.0, c) ** len(yb)), c

    print("C1. sans_remise [1, 1], un bloc de 2, nul = lois constantes :")
    for p in (0.5, 0.3, 0.1):
        for forme in ("nu", "gel"):
            E, cmax = 0.0, 0.0
            for yb in itertools.product(range(K), repeat=2):
                yb = np.array(yb)
                Q = lois_realisees(lambda h, s: sans_remise([1, 1], h, s), yb, 2, forme)
                e, c = e_bloc(Q, yb)
                pr = np.prod(np.where(yb == 0, p, 1 - p))
                E += pr * e
                cmax = max(cmax, c)
            print(f"    p = {p} ({forme}) : E[e_B] = {E:.6f} (16/3·p(1−p) = {16 / 3 * p * (1 - p):.6f}) ; plus grand certificat {cmax:.6f}")

    # (C2) recherche, parmi des cartes de la grammaire, de violations exactes de Ville (monde p = 1/2, constant, membre de
    # tout nul qui contient les lois constantes) ; lecture aux fins de bloc ; blocs de b ; n tirages.
    cartes = {}
    for a in (1, 2, 3, 6):
        cartes[f"sans_remise [{a}, {a}]"] = (lambda a: (lambda h, s: sans_remise([a, a], h, s)))(a)
    for f in (1, 2):
        for lam in (1e-3, 0.5):
            cartes[f"moyenne_glissante fenêtre {f}, lissage {lam}"] = (lambda f, lam: (lambda h, s: moyenne_glissante(2, f, lam, h, s)))(f, lam)
    print("C2. monde constant p = 1/2 ; par carte : E[e_B1] (nu / gel) ; P(∃ fin de bloc : W ≥ 1/α) exacte (nu / gel / maximum certifié sur les tirages mêmes / rapport au monde)")
    resultats = []
    for nom, carte in cartes.items():
        for b, n in ((2, 2), (2, 8), (2, 12), (3, 12), (4, 12), (6, 12)):
            suites = toutes_suites(K, n)
            lw = {"nu": np.zeros((len(suites), n // b)), "gel": np.zeros((len(suites), n // b))}
            lmax = np.zeros((len(suites), n // b))
            lvrai = np.zeros((len(suites), n // b))
            e1 = {"nu": 0.0, "gel": 0.0}
            for i, y in enumerate(suites):
                for forme in ("nu", "gel"):
                    Q = lois_realisees(carte, y, b, forme)
                    acc = 0.0
                    for B in range(n // b):
                        idx = np.arange(B * b, (B + 1) * b)
                        e, _ = e_bloc(Q[idx], y[idx])
                        acc += math.log(max(e, 1e-300))
                        lw[forme][i, B] = acc
                        if B == 0:
                            e1[forme] += e * 0.5 ** n
                Qn = lois_realisees(carte, y, b, "nu")
                lq = np.cumsum(np.log(Qn[np.arange(n), y]))
                for B in range(n // b):
                    t = (B + 1) * b
                    k1 = int(y[:t].sum())
                    ph = k1 / t
                    lm = (k1 * math.log(ph) if k1 else 0.0) + ((t - k1) * math.log(1 - ph) if t - k1 else 0.0)
                    lmax[i, B] = lq[t - 1] - lm                                 # carte réelle, maximum exact des lois constantes
                    lvrai[i, B] = lq[t - 1] - t * math.log(0.5)
            def pire_rapport(M):
                """sup sur α ∈ ]0, 1[ de P(max_B log W ≥ log 1/α)/α = max_v P(M ≥ v)·e^v, v > 0 (monde uniforme : poids égaux)."""
                m = np.sort(M.max(1))[::-1]
                meilleur, a_pire = 0.0, None
                for i_v, v in enumerate(m):
                    if v <= 1e-12:
                        break
                    r = float((m >= v - 1e-12).mean()) * math.exp(v)
                    if r > meilleur:
                        meilleur, a_pire = r, math.exp(-v)
                return meilleur, a_pire
            rn, an = pire_rapport(lw["nu"]); rg, _ = pire_rapport(lw["gel"]); rm, _ = pire_rapport(lmax); rv, _ = pire_rapport(lvrai)
            p05 = float((lw["nu"] >= math.log(20) - 1e-12).any(1).mean())
            resultats.append((nom, b, n, e1["nu"], e1["gel"], rn, an, rg, rm, rv, p05))
    for nom, b, n, en, eg, rn, an, rg, rm, rv, p05 in resultats:
        marque = "  <-- Ville violée" if rn > 1 + 1e-9 else ""
        a_txt = f"{an:.4f}" if an is not None else "—"
        print(f"    {nom:42s} b={b} n={n:2d} E[e_B1] {en:.4f} / {eg:.4f} ; sup_α P/α : nu {rn:.4f} (α = {a_txt}) ; gel {rg:.4f} ; "
              f"maximum {rm:.4f} ; rapport au monde {rv:.4f} ; P(nu, α = 0,05) {p05:.4f}{marque}")
    print(f"C2. configurations où Ville est violée (sup_α P/α > 1) : nu {sum(r[5] > 1 + 1e-9 for r in resultats)} sur "
          f"{len(resultats)} ; gel {sum(r[7] > 1 + 1e-9 for r in resultats)} ; maximum certifié {sum(r[8] > 1 + 1e-9 for r in resultats)} ; "
          f"rapport au monde {sum(r[9] > 1 + 1e-9 for r in resultats)} ; plus grand E[e_B1] sous gel {max(r[4] for r in resultats):.6f}")


# ---------------------------------------------------------------------------------------------------------------------
def partie_D(repetitions=12):
    """Théorème 1 (maximum certifié sur les tirages mêmes) avec trois membres (cellules A, cellules B, linéaire) ; monde
    dans A ; lectures : T8 = {5, 10} (« éparse »), T40 = {1..10} (« dense ») ; règles : J9 (∃t∈T8 ∀m), J9-D40
    (J9 ou ∃t∈T40 ∀m), par membre (∀m ∃t_m∈T40), réunion ; statistiques : S = min_m max_t W^m_t, E' = min_m W^m_{τ_m}."""
    K, J, n = 2, 2, 10
    T8 = [4, 9]                           # indices 0..n−1 des instants 5 et 10
    rng = rng_de(4)
    suites = toutes_suites(K, n)
    alphas = (0.5, 0.25, 0.1)
    pire = {(r, a): 0.0 for r in ("J9", "J9-D40", "par membre", "réunion", "Ville du monde") for a in alphas}
    ES_max, EE_max, Emax_lambda = 0.0, 0.0, 0.0
    gain = {a: [0, 0, 0] for a in alphas}
    for i in range(repetitions):
        L = rng.dirichlet(np.ones(K), size=(n, J))
        celA = rng.integers(0, 2, size=n)
        celB = rng.integers(0, 2, size=n)
        cel1 = np.zeros(n, dtype=int)
        q = rng.dirichlet(np.ones(K) * 0.6, size=n)
        membres = [(celA, 2), (celB, 2), (cel1, 1)]
        lq = np.cumsum(np.log(q[np.arange(n)[None, :], suites]), axis=1)       # (S, n)
        V = np.zeros((3, len(suites), n))
        Yall = np.eye(K)[suites]                                              # (S, n, K)
        for m, (cel, C) in enumerate(membres):
            for t in range(1, n + 1):
                V[m, :, t - 1] = max_certifie_lot(Yall[:, :t], L[None, :t], cel[:t], C, 600)
        lW = lq[None, :, :] - V                                               # (3, S, n)
        lmin = lW.min(0)                                                      # dénominateur = maximum des membres
        mondes = [em_famille(q, L, celA, 2, 3000)] + [point_au_hasard(rng, 2, J, K) for _ in range(2)]
        for theta in mondes:
            P = probas_famille(theta, L, celA, 2)
            lP = np.cumsum(np.log(P[np.arange(n)[None, :], suites]), axis=1)
            prob = np.exp(lP[:, -1])
            lam = lq - lP
            for a in alphas:
                s = math.log(1 / a)
                r_j9 = (lmin[:, T8] >= s).any(1)
                r_d40 = r_j9 | (lmin >= s).any(1)
                r_mem = (lW >= s).any(2).all(0)
                r_un = r_j9 | r_d40 | r_mem
                r_v = (lam >= s).any(1)
                assert not np.any(r_un & ~r_v), "réunion hors de l'événement de Ville du monde"
                for nom, ev in (("J9", r_j9), ("J9-D40", r_d40), ("par membre", r_mem), ("réunion", r_un), ("Ville du monde", r_v)):
                    pire[(nom, a)] = max(pire[(nom, a)], float(prob[ev].sum()) / a)
                gain[a][0] += int(r_j9.sum()); gain[a][1] += int(r_d40.sum()); gain[a][2] += int(r_mem.sum())
            S = np.exp(lW.max(2).min(0))                                       # min_m max_t W^m_t
            ES_max = max(ES_max, float((prob * S).sum()))
            Emax_lambda = max(Emax_lambda, float((prob * np.exp(lam.max(1))).sum()))
            c = 1 / 0.25                                                       # seuil fixé d'avance
            Ep = np.full(len(suites), np.inf)
            for m in range(3):
                franchit = lW[m] >= math.log(c)
                tau = np.where(franchit.any(1), franchit.argmax(1), n - 1)
                Ep = np.minimum(Ep, np.exp(lW[m][np.arange(len(suites)), tau]))
            EE_max = max(EE_max, float((prob * Ep).sum()))
    print(f"D. {repetitions} plans (K=2, n=10, membres {{cellules A, cellules B, linéaire}}, monde dans A ; projection de la "
          f"carte et deux mondes au hasard) — plus grand P(règle)/α :")
    for nom in ("J9", "J9-D40", "par membre", "réunion", "Ville du monde"):
        print(f"    {nom:15s} " + " ; ".join(f"α={a} : {pire[(nom, a)]:.4f}" for a in alphas))
    print("D. suites promues, sommées sur les plans et les mondes (J9 / J9-D40 / par membre) : "
          + " ; ".join(f"α={a} : {g[0]}/{g[1]}/{g[2]}" for a, g in gain.items()))
    print(f"D. statistique S = min_m max_t W^m_t : plus grande espérance {ES_max:.4f} ; E[max_t Λ_t] la plus grande {Emax_lambda:.4f}")
    print(f"D. forme arrêtée membre par membre E' (seuil c = 4 fixé d'avance) : plus grande espérance {EE_max:.4f}")
    # exemple à la main : S n'est pas une valeur e (un membre fixe P* = (1/2, 1/2), carte (0,9 ; 0,1), lu à t = 1 et 2)
    lam = [max(1.8 ** (2 - k) * 0.2 ** k, (1.8 if y1 == 0 else 0.2)) for y1 in (0, 1) for k in ([0, 1] if y1 == 0 else [1, 2])]
    print(f"D. exemple à la main : E[max(Λ_1, Λ_2)] = {np.mean(lam):.4f}")


# ---------------------------------------------------------------------------------------------------------------------
def partie_E():
    """Lois connues par tirages. Deux cellules g ∈ {0, 1}, deux issues ; loi connue L(1|g) = (0,1 ; 0,9) ; famille
    « loi connue plus bruit aveugle commun » (membre linéaire à une loi connue : sommets L, δ_0, δ_1) ; carte = monde = L
    (copie exacte, membre du vrai nul). Estimation L̂ sur N tirages par cellule ; m tirages frais par cellule ; lecture à
    la fin seulement (borne basse du taux à plusieurs instants). Probabilité exacte (somme sur tous les comptes)."""
    from scipy.stats import binom
    alpha = 0.05
    s = math.log(1 / alpha)

    def bornes(k0, k1, a0, a1, m):
        """Comptes en quatre pseudo-instances (g, y) pondérées ; L (S, 4, 1, 2) ; une seule cellule de poids (C = 1)."""
        S = len(k0)
        Y = np.zeros((S, 4, 2))
        Y[:, 0, 1] = k0; Y[:, 1, 0] = m - k0; Y[:, 2, 1] = k1; Y[:, 3, 0] = m - k1
        L = np.zeros((S, 4, 1, 2))
        for i, a in ((0, a0), (1, a0), (2, a1), (3, a1)):
            L[:, i, 0, 1] = a; L[:, i, 0, 0] = 1 - a
        return max_certifie_lot(Y, L, np.zeros(4, dtype=int), 1, 400)

    for N, m in ((10, 20), (20, 20), (50, 20), (10, 100), (20, 100)):
        K0, K1 = np.meshgrid(np.arange(m + 1), np.arange(m + 1), indexing="ij")
        K0, K1 = K0.ravel(), K1.ravel()
        pk = binom.pmf(K0, m, 0.1) * binom.pmf(K1, m, 0.9)
        lq = K0 * math.log(0.1) + (m - K0) * math.log(0.9) + K1 * math.log(0.9) + (m - K1) * math.log(0.1)
        v = bornes(K0.astype(float), K1.astype(float), np.full(len(K0), 0.1), np.full(len(K0), 0.9), m)
        p_vrai = float(pk[lq - v >= s].sum())
        p_plug = 0.0
        for h0 in range(N + 1):
            for h1 in range(N + 1):
                ph = binom.pmf(h0, N, 0.1) * binom.pmf(h1, N, 0.9)
                if ph < 1e-14:
                    continue
                v = bornes(K0.astype(float), K1.astype(float), np.full(len(K0), h0 / N), np.full(len(K0), h1 / N), m)
                p_plug += ph * float(pk[lq - v >= s].sum())
        print(f"E. N = {N} tirages par cellule pour estimer L, m = {m} tirages frais par cellule, lecture à la fin : "
              f"P(copie promue) certificat « comme si exact » {p_plug:.4f} ; vraies lois {p_vrai:.4f} (α = {alpha})")


if __name__ == "__main__":
    parties = sys.argv[1:] or ["A", "B", "C", "D", "E"]
    for p in parties:
        {"A": partie_A, "B": partie_B, "C": partie_C, "D": partie_D, "E": partie_E}[p]()
        sys.stdout.flush()
```
