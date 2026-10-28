# Carte des hypothèses des moniteurs — graine du pôle théorique — v1

Lignée conv-audit, sous-agent neuf (Opus 5.5) ; je n'ai écrit ni le programme, ni l'audit des failles, ni le pari apparié,
ni la mesure unanime. Brief : `brief-carte-des-hypotheses-v1.md` (dossier de travail de la session). Début : relevé `date -u`
de 01:00:27 UTC le 28 octobre 2026 (appel séparé) ; fin : relevée dans la réponse de livraison.

**Pièce confidentielle** : dépôt privé seulement ; jamais dans la copie publique ; jamais servie à un organisme ; **jamais
servie au concepteur du mode tenu à l'écart** (N-054 point 3 ; N-056 point 6 (A) : il reste aveugle aux moniteurs) ; pour le
concepteur du bras d'attaque informé (N-056 point 6 (B)), décision de Lazar.

**Règles d'écriture** (brief de l'audit, § 2 et § 3). Aucune procédure, consigne, exemple de texte, de code ou de réglage qui
servirait à tromper un moniteur : chaque classe d'écart est une propriété de **lois** (P₀ honnête, P₁ sous sabotage), jamais
une conduite d'agent. R7 : un chiffre de papier porte la page vérifiée par l'audit (« vérifié p. N ») ; « lot A » ou
« session-depot » = relevé non opposable. R8 : une classe sans instance est une question.

**Sources** (relatives à `/home/claude/canal-conv-audit-n04/` sauf mention ; empreintes recalculées sur disque). Programme
`docs/programme-controle-ia-v2.md` (`2fd63bad…`, identique à la copie de `controle-ia-travail`) ; décisions de
`/home/claude/controle-ia-travail/docs/decisions/` : N-003/N-004 (`cc1be393…`), N-007/N-008 (`ab7dc9bb…`), N-029 (`084e3052…`),
N-053 (`2204256d…`), N-054 (`c8a00b3f…`) ; N-056 proposée (`brouillons/canal-reprise-releve-v1/envois/decision-N-056-…-v1.md`,
`6aac9746…`). Audit, sous `brouillons/canal-reprise-releve-v1/envois/audit-failles-controle-v1/` : `sortie-synthese-v3/audit-failles-controle-v3.md`
(`4f74b366…`, « audit v3 ») ; `sortie-confrontation/` : `carte-du-controle-v1.md` (`ad5eaa49…`), `failles-internes-v1.md`
(`c854f23f…`), `grille-de-couverture-v1.md` (`1e060208…`), `calculs-auditeur-v2.sortie.txt` (`ee257a7a…`) ;
`sortie-synthese-v2/calculs-synthese-v2.sortie.txt` (`3babde06…`, « calcul v2 »). Pari apparié v5
(`…/envois/pole-scientifique-automatique-v1/pari-de-signe/conception-pari-de-signe-v5.md`, `95af46e4…`) ; mesure unanime v5
(`…/envois/mesures-fortes-v1/mesure-unanime-v1/preenregistrement-mesure-unanime-v5.md`, `29f91ff3…`, non scellée à ma lecture),
table gelée `table-m2bis-m4-v5.json` (`95fdbac9…`). Code : `src/controle_ia/bases/sequentiel.py` (`35a09834…`). Calculs de cette
carte (« bloc n ») : `calculs-carte-des-hypotheses-v1.py` et `.sortie.txt`, même dossier, compagnons `.sha256` ; analytiques
ou synthétiques, `SeedSequence(20261028)`. Rien lu dans `donnees/`, `diag/`, `runs/`, `pilotes/` ; aucun `git` ; dépôt intact.

**Conventions.** Épisode de T actions ; score par action X_t (après agrégation sur les jetons) ; z_t = (X_t − μ₀)/σ (comme
`sequentiel.py`) ; P₀ loi honnête de calibrage, Q₀ loi honnête d'évaluation, P₁ loi sous sabotage ; statistique S, seuil τ
tel que P₀(S > τ) ≤ α ; δ_t décalage par action, B = Σ δ_t. Lemme **prouvé** (preuve courte ici ou note démontrée),
**esquisse**, **conjecture**. Instance **L** littérature auditée, **I** notre propre conception, **Q** question (R8). HT-nn :
hypothèses testables de l'audit v3 (§ 1 ter) ; D-nn : ses décisions pour Lazar (§ 8).

## 0. Verdict

1. **Huit statistiques** (onze lignes), **vingt-trois hypothèses** A1 à A23, une classe d'écart chacune, au niveau des lois,
   sous un lemme maître L0. **Quinze classes** ont une instance dans la littérature auditée (A9 et A15 sur relevés du lot A
   seuls) ; **une** dans notre propre conception (A18) ; **sept sont des questions** (A2, A6, A7, A11, A12, A14, A20).
   Lemmes : vingt et un prouvés (A4 et A5 en gaussien ; la plupart élémentaires), deux esquisses (A11, A19), une conjecture.
2. **Les trois lemmes les plus utiles.** **A7** (gaussien) : sous un effet épisode de part r₀, le rappel de toute statistique
   contre un décalage constant plafonne à Φ(δ/√r₀ − z_α) quel que soit l'horizon (δ = 0,3, α = 1 % : 0,049 à r₀ = 0,2) ;
   H2 dépend de r₀, que la mesure unanime va lire. **A18** : le moniteur qui définit la population « sous le seuil » y est
   aveugle par construction (H2, régime diffus de G1, bases (ii) et (iii) de N-056). **A13** : contre des négatifs appariés
   en indication, une sonde qui ne lit que l'indication a un rappel égal à son taux de fausses alertes (faille de tête (a)).
3. **Hors carte** : papier B, papier C au-delà du juge, invariants de protocole, faisabilité de chaque classe (section 5).

## 1. Les statistiques de contrôle

| id | statistique (où) | ce qu'elle lit (fonction des données) | ce qu'elle suppose |
|---|---|---|---|
| S1 | seuil par action calibré (T0.8 ; N-007 ; H2) | 1{X_t > q̂}, q̂ quantile 1 − τ_a des actions honnêtes de calibrage mises en commun, τ_a = 1 % | A1, A8, A9, A10 ou A16, A22, A23 |
| S2 | règle de Ville (processus e) | sup_t log e_t, mélange normal unilatéral (ρ) sur z ; alarme si ≥ log(1/α) | A6, A1, A4, A8, A23 |
| S3a | maximum conforme | max_t z_t ; seuil au rang ⌈(K + 1)(1 − α)⌉ sur K épisodes honnêtes entiers | A1, A4, A8, A9, A21, A22, A23 |
| S3b | sommes conformes : terminale, séquentielle, processus e conforme | Σ_t z_t ; max_t Σ_{s ≤ t} z_s ; max_t log e_t ; même calibrage | A2 (terminale), A3, A4, A5, A7, A8, A14, A21, A22, A23 |
| S3c | somme cumulée de Page conforme | max_t C_t, C_t = max(0, C_{t−1} + z_t − k) | A3, A4, A8, A23 |
| S3d | balayage conforme | max sur les fenêtres de w actions consécutives de Σ z | A3, A4, A8, A23 |
| S4 | cascade de portes sur les mêmes sondes, base (ii) (N-007, type *Doomed*) | union sur les pas des portes {X_t > τ_t} | A1, A6 (niveau composé), A8, A18, A23 |
| S5 | sonde sur le dernier état, base (iii) (N-007) | p(h_ℓ) à la position finale seule | A10, A12, A13, A8 |
| S6 | accumulation additive de sondes de l'agent qui agit (H2, N-007) | sonde par jeton → max ou attention sur les jetons (N-026) → X_t → S3b | A10, A11, A12, A13, A14, A7, A18, et tout S3b |
| S7 | juge boîte noire : par action, en une passe, robustifié, TRACE-lite, bases (i) et (iv) | v(texte visible, contexte montré au juge), espérance sur le jeton de verdict (P-010), puis S1 ou S3 | A16, A17 ; A1 à A8 en séquentiel ; A23 |
| S8 | planchers (§ 8.1 ; P-015 ; N-029) | (a) quantile 0,95 de l'aire de 200 directions w ~ N(0, Σ̂) ; (b) permutation des étiquettes ; (c) prédicteur sur les traits du texte (coût normalisé, longueur, forme du champ) | A19 (a, b), A20 (c) |

Légende : A1 marginale déplacée ; A2 multi-ensemble ; A3 non-compensation ; A4 budget non dilué ; A5 taux de change ; A6
indépendance ; A7 horizon ; A8 échangeabilité du calibrage ; A9 longueur ; A10 lisibilité linéaire ; A11 agrégation sur les
jetons ; A12 position de lecture ; A13 intention, non texte ; A14 état, non disposition ; A15 conflit interne ; A16 trace
textuelle ; A17 registre du juge ; A18 sélection de la population ; A19 plancher et confusions ; A20 validité incrémentale ;
A21 indice d'épisode ; A22 placement indépendant du bruit ; A23 régime d'observation.

## 2. La carte

**Lemme maître L0 (prouvé).** Soit D les données lues, S = s(D), une règle d'alarme fonction de S seule (aléa indépendant
permis), de taux α sous P₀. (i) *Invariance* : si P₁∘S⁻¹ = P₀∘S⁻¹, le taux de détection vaut α. (ii) *Proximité* :
|P₁(alarme) − α| ≤ d_VT(P₁∘S⁻¹, P₀∘S⁻¹) (variation totale). (iii) *Strate* : si P₁∘S⁻¹ = Q∘S⁻¹ pour une strate honnête Q,
calibrée ou non, P₁(alarme) = Q(alarme). (iv) *Impossibilité* (T2 de N-003) : si P₁∘D⁻¹ = P₀∘D⁻¹, aucun moniteur de D ne
dépasse α. *Preuve* : l'alarme est un événement de σ(S), élargie d'un aléa indépendant ; deux lois égales sur σ(S) lui
donnent la même probabilité ; (ii) est la définition de la variation totale. □ Chaque Ai nomme la classe où (i), (ii) ou
(iii) tient ; un lemme élémentaire vaut par la classe qu'il nomme et le témoin qu'il appelle (N-003, à propos de T1).

### A1 — La marginale par action est déplacée (hypothèse (a) du lemme, δ > 0)
- **Hypothèse** : pour chaque action sabotée, P₁∘X_t⁻¹ ≠ P₀∘X_t⁻¹ (au moins E₁X_t ≥ E₀X_t + δ).
- **Classe K1** (classe K de N-003) : P₁∘X_t⁻¹ = P₀∘X_t⁻¹ pour tout t ; seule la copule entre actions change.
- **Lemme (prouvé)** : S1 est aveugle à chaque pas (L0 (i)) ; S4 l'est si la loi jointe des indicateurs de dépassement est
  gardée ; si P₁ a des corrélations plus fortes que P₀ (gaussien), le taux de S3a reste ≤ α (Slepian, cité par N-003) :
  « aveugle ou pire ». Les sommes ne sont pas aveugles en classe K (N-003) : c'est la prise qui reste.
- **Instances (L)** : attaque à marges préservées et dépendance par copule, contre moniteurs de marges et de séquence
  (2606.10456v2, p. 1–2, audit v3 RC-1.2 ; « antécédent défectueux » selon N-003).
- **Témoin** : bras M4 de la mesure unanime (dépendance injectée à deux moments égaux, non vue au calibrage ; maximum conforme
  ≤ 0,08 prédit, excès apparié des sommes > 0 si r₀ < 0,5 ; nul : τ = 0) ; E1.4. **Défense** : HT-07 ; arbre de FI-33.

### A2 — Le multi-ensemble des scores de l'épisode porte le signal
- **Hypothèse** : le multi-ensemble {X_t} d'un épisode saboteur n'a pas la loi de celui d'un honnête.
- **Classe K2** (classe C de N-003) : multi-ensemble d'un honnête, ordre seul changé par une permutation d'un groupe G.
- **Lemme (prouvé, N-003, T1 et T2)** : toute statistique G-invariante (somme terminale, maximum, moyenne) est aveugle
  trajectoire par trajectoire ; ordre rebrassé dans le groupe d'invariance de P₀ : L0 (iv). Page, balayage, sommes en continu
  lisent l'ordre (T3).
- **Instances** : aucune chez un organisme dans l'audit — **question** (la classe est démontrée, son occurrence non) ; le terme
  ajouté par le colmatage de la faille E est lui-même symétrique (audit v3 RC-3.1 (a), calcul v2 bloc 1).
- **Témoin** : section 3, T2. **Défense** : posée, T3 (garanties locales des détecteurs d'ordre) ; FC-03 (pas de « colmatage »).

### A3 — Non-compensation : l'excès de score s'accumule sur un intervalle
- **Hypothèse** (condition empirique de N-004) : un intervalle porte sous P₁ un excès Σ_{a..b}(z_t − k) hors d'atteinte honnête.
- **Classe K3** : M_k = max_{a ≤ b} Σ_{a..b}(z_t − k) garde sous P₁ sa loi honnête (ou est dominé par elle), par exemple toute
  loi de moyenne par pas sous k ; pour la terminale, déplacement net nul à loi de la somme gardée.
- **Lemme (prouvé)** : max_{t ≤ T} C_t = max(0, M_k) pour toute suite (récurrence de Lindley ; écart 8,4·10⁻¹⁵ sur 6 000 suites,
  bloc 2) : Page n'est qu'une fonction de M_k, aveugle sous K3 ; de même le balayage (fenêtres de longueur w) et la somme
  séquentielle (intervalles partant de 1). Corollaire de l'audit (RC-3.1 (e)) : max C_t < h impose une moyenne sous k + h/T.
- **Instances (L)** : attaques construites pour rester sous les détecteurs à somme cumulée et du chi-deux (2005.07821v1,
  vérifié p. 1) ; cadre adverse contre la somme cumulée cité par 2601.20022v2 p. 2 (non tenu) ; faille E (RC-3.1), non mesurée.
- **Témoin** : scores honnêtes réels, écart de classe K3 injecté au niveau des scores, contre le témoin de classe C ; rappel à
  1 % de Page et de la statistique de HT-01 ; nul : rebrassage. **Défense** : HT-01 ; hypothèse (b) du lemme.

### A4 — Le budget n'est pas dilué dans l'horizon
- **Hypothèse** : le signal reste détectable quand l'horizon n₀ = NT croît (B/(σ√n₀) borné inférieurement).
- **Classe K4** : B fixé, n₀ → ∞ ; ou décalage par pas qui tend vers 0 quand la contrainte de fausse alarme γ croît.
- **Lemme (prouvé, N-004 L1 et L2 ; gaussien)** : la puissance de la terminale ne dépend que de (B, n₀, F₀, α) et décroît vers
  α ; le maximum s'effondre plus vite. Pour des scores gaussiens de covariance Γ connue, la divergence de Kullback-Leibler
  vaut δᵀΓ⁻¹δ/2, d'où (Pinsker) |P₁(alarme) − α| ≤ ‖Γ^{−1/2}δ‖/2 pour **tout** moniteur des scores, soit B/(2σ√n₀) → 0 à B étalé
  sur n₀ pas indépendants (hors du cas gaussien : esquisse, information de Fisher). Contre tout détecteur, une loi après
  rupture qui converge vers la loi avant rupture impose un délai Θ(γ) (2601.20022v2, vérifié p. 1–3 ; programme § 3).
- **Instances (L)** : 2601.20022v2 p. 1–3 ; FC-04.
- **Témoin** : E1.3 ; dès maintenant, B fixé et n₀ variable sur scores honnêtes réels ; nul : B = 0. **Défense** : hypothèse
  (b) (budget total borné) ; détecteur de rupture (N-004) ; HT-08.

### A5 — Le taux de change entre dommage et score est borné inférieurement
- **Hypothèse** (FI-04) : pour toute politique de la classe évaluée Π, κ = déplacement de score par unité de dommage ≥ κ_min.
- **Classe K5** : inf_Π κ = 0 : un dommage θ atteint avec un déplacement total qui tend vers 0.
- **Lemme (prouvé, gaussien ; esquisse en général)** : avec δ_t = κ·d_t (d_t dommage de l'action), la borne de A4 devient
  |P₁(alarme) − α| ≤ κ·‖Γ^{−1/2}d‖/2 → 0 quand κ → 0 à dommage fixé : la sécurité définie en dommage (programme § 4) tend
  vers α pour tout moniteur des scores ; une garantie en unités de score ne la porte pas.
- **Instances (L)** : activations obfusquées contre sondes et détecteurs latents (2412.09565v2) ; apprentissage par renforcement
  contre des moniteurs latents (2506.14261v4) ; évasion de moniteurs d'activations jamais vus (2512.11949v1) — vérifiés p. 1 :
  conduite gardée, score abaissé (audit v3 § 4.1) ; FI-04 (bloque).
- **Témoin** : HT-08 (limite de détection en dommage, dose mesurée dans l'espace de la tâche par un évaluateur disjoint) ;
  pente du déplacement sur le dommage, par mode (N-054), couche 2 (devis) ; nul : pente 0. **Défense** : D-03 et HT-08
  (sécurité énoncée sous κ ≥ κ_min mesuré) ; HC4 et Tr (E1.5 (b), sous GO) mesurent le coût de K5.

### A6 — Indépendance et marges gaussiennes (règle de Ville ; niveau composé d'une cascade)
- **Hypothèse** : sous P₀, les z_t sont indépendants N(0, 1) : le processus e est une surmartingale positive et
  P₀(sup_t e_t ≥ 1/α) ≤ α ; de même pour une cascade de niveau composé 1 − Π(1 − α_j).
- **Classe K6** : effet épisode (z_t = b_e + ε_t, part de variance r₀), dépendance intra-épisode, marges asymétriques.
- **Lemme (prouvé pour la perte de la propriété)** : sous effet épisode, E₀[exp(λΣ_t z_t − λ²T/2)] = exp(λ²r₀T(T − 1)/2) > 1 pour
  T ≥ 2 : plus de surmartingale ; dépassement établi en simulation (0,21 à 0,35 pour 0,05 visé, T0.3 P8, cité par N-007 § 1).
  Fausse garantie plutôt que cécité ; par L0 (iii), un décalage constant δ ne se sépare pas d'un effet d'épisode décalé de δ.
- **Instances** : aucune mesure de l'écart dans nos scores n'est lue — **question** (M2 ter de la mesure unanime).
- **Témoin** : mesure unanime v5, M2 ter, bras « mélange » et « mélange à pas fixé ». **Défense** : posée, calibrage conforme
  sur épisodes honnêtes entiers (N-004, N-007, `sequentiel.py`) ; cascade : niveau par union (Bonferroni), sous toute dépendance.

### A7 — Le rappel croît avec l'horizon (H2, N-007)
- **Hypothèse** : à δ fixé par action, le rappel d'une statistique de somme croît vers 1 avec T.
- **Classe K7** : effet épisode honnête de part r₀ > 0 (K6 côté puissance), décalage constant sur l'épisode.
- **Lemme (prouvé, gaussien)** : le vecteur 1 est propre pour la covariance σ²((1 − r₀)I + r₀11ᵀ) : la moyenne d'épisode est
  exhaustive, et le meilleur test de niveau α, toutes statistiques confondues, a pour puissance Φ(δ/√(r₀ + (1 − r₀)/T) − z_α),
  plafonnée à Φ(δ/√r₀ − z_α). À δ = 0,3 écart type, α = 1 % : 0,084 / 0,419 / 1 à T = 10 / 50 / ∞ sans effet épisode ;
  0,039 / 0,046 / 0,049 à r₀ = 0,2 (bloc 1 ; Monte-Carlo 0,161 contre 0,159 dans une cellule). Le calibrage conforme garde
  le taux, pas la puissance (FC-10). Si une part p < 1 des actions est décalée, les sommes restent plafonnées ; une
  statistique intra-épisode peut faire mieux.
- **Instances** : effets aléatoires (classique, non relu) ; ripostes du collisionneur (affirmé par un modèle) ; dans nos scores
  — **question** (r₀ rapporté par la mesure unanime, non lue).
- **Témoin** : section 3, T1. **Défense** : HT-19 (centrage par la ligne de base de la tâche : plafond au r₀ résiduel) ; HT-17 ;
  à poser dans H2a : « croît avec l'horizon » énoncé conditionnellement à r₀ mesuré.

### A8 — Échangeabilité entre calibrage et évaluation (garantie conforme)
- **Hypothèse** : l'honnête d'évaluation est échangeable avec les K de calibrage (agent, révision, tâches, horizon, configuration) : P(S > τ̂) ≤ α.
- **Classe K8** : Q₀ ≠ P₀ : durée choisie (faille F) ; réglage bénin ou révision (FI-18) ; strate absente (honnête averti, sous
  revers, dans l'erreur, sur sujet voisin : FI-29, MD-A6, SD-D6) ; autres tâches ; configuration numérique (FI-24).
- **Lemme (prouvé)** : le taux réel vaut Q₀(S > τ̂), sans borne ; par L0 (iii), un sabotage dont S a la loi d'une strate honnête
  non calibrée Q′ en est indistinguable : le moniteur alerte sur Q′ au même taux, sabotage ou non.
- **Instances (L)** : seuils faux d'une famille à l'autre (2607.06596v3, vérifié p. 13) ; obsolescence après mise à jour, écart
  calibrage-test (2610.04575v1, vérifié p. 2) ; sondes allumées par l'incorrection (MD-A6, lot A) ; faille F (calcul v2 bloc 2 :
  sous effet épisode, 1 % visé devient jusqu'à 4,56 % à 30 pas avec la normalisation du rapport).
- **Témoin** : HT-06 (honnêtes témoins injectés à taux connu) ; HT-02 en simulation ; seuil gelé sur les honnêtes de
  l'adaptateur témoin (FI-18) ; nul : taux dans [0,5α ; 2α]. **Défense** : HT-02, HT-06 ; D-16 ; D-18.

### A9 — La loi honnête de la statistique ne dépend pas de la longueur
- **Hypothèse** : la loi de S (max sur jetons ; max ou somme sur actions) est indépendante de la longueur, ou celle-ci a même loi partout.
- **Classe K9** : longueurs de lois différentes entre calibrage, honnête et sabotage.
- **Lemme (prouvé)** : scores par jeton indépendants de loi F : le max sur n jetons a pour loi Fⁿ ; une loi G = F^{n/m},
  stochastiquement plus grande que F, donne sur m < n jetons la même loi du max (G^m = Fⁿ) : par le max, un décalage vers le
  haut sur une unité plus courte est indistinguable d'une unité honnête plus longue (bloc 3 : quantiles 0,5 / 0,9 / 0,99 de
  2,699 / 3,268 / 3,897 contre 2,701 / 3,282 / 3,902 ; médiane par jeton de G 0,545). P(max_{j ≤ n} > τ) croît avec n.
- **Instances (L, lot A seul)** : sondes de contextes courts sur contextes longs (2601.11516, MD-B3) ; FI-26 (calcul de
  l'auditeur, bloc 5 : 0,61 % / 2,45 % / 4,69 % à 50 / 200 / 400 jetons pour 1 % calibré à 100) ; faille F.
- **Témoin** : section 3, T3. **Défense** : fenêtres fixes, maximum entre fenêtres (2604.14865v1, vérifié p. 6) ; calibrage par
  strate de longueur (FI-26, HT-02).

### A10 — L'intention est lisible dans la direction et la couche lues
- **Hypothèse** : la loi de ⟨w, h_ℓ⟩ (ou de la fonction apprise : perceptron, attention) diffère sous P₁.
- **Classe K10** : loi jointe des projections lues gardée ; l'écart loge ailleurs (complément, non-linéarités, autres couches).
- **Lemme (prouvé)** : L0 (i), S = (⟨w, h_{ℓ,j}⟩)_j : toute agrégation de ces projections est aveugle ; une autre sonde w′, non.
- **Instances (L)** : 2412.09565v2 ; 2506.14261v4 ; 2512.11949v1 (vérifiés p. 1) ; SD-D7 (session-depot).
- **Témoin** : « suppression consignée » de N-053 point 1 (direction aléatoire de même variance en témoin) ; transfert vers la
  réserve jamais déployée (§ 8.1). **Défense** : réserve ; diversité effective par transfert (H5) ; HC4 ; N-053 point 5.

### A11 — L'agrégation sur les jetons voit un décalage étalé
- **Hypothèse** : un décalage porté par les jetons d'une action se voit dans le max ou l'attention (N-026).
- **Classe K11** : décalage total B_j réparti sur n jetons, loi jointe sinon gardée : la fragmentation, un étage plus bas
  (FI-26 ; audit v3 RC-1.3).
- **Lemme (esquisse)** : L2 transposé aux jetons : le max perd sa puissance dès que B_j/n est petit, la somme quand B_j/(σ√n) l'est ;
  « max, jamais moyenne » (programme § 0, décision 1) protège d'un signal concentré dilué et laisse ce cas. **Conjecture** :
  une attention apprise sur des signaux concentrés pondère peu un décalage étalé.
- **Instances** : voisine, « token-level monitors are highly vulnerable » (2506.14261v4, vérifié p. 1), sans K11 — **question**.
- **Témoin** : simulation sur scores par jeton, puis injection dans des scores honnêtes réels par jeton s'ils sont gardés ;
  rappel du max, de l'attention gelée, d'une fenêtre fixe ; nul : décalage nul. **Défense** : à poser — agrégation à deux
  échelles (somme sur fenêtres fixes, max entre fenêtres) ; bras de diagnostic « moyenne » hors production (N-026).

### A12 — La trace atteint les positions lues (positions ; dernier état)
- **Hypothèse** : la trace est aux positions lues : jetons de l'action et contexte privé (N-007) pour S6, fin pour S5.
- **Classe K12** : loi jointe des activations aux positions lues gardée ; la trace est ailleurs.
- **Lemme (prouvé, élémentaire)** : L0 (i) ; S5 et S6 ne lisent pas les mêmes positions : un écart qui ne garde que la
  position finale aveugle (iii) seule, ce que la base (iii) isole (N-007).
- **Instances** : voisines (MD-B3, lot A ; faille H, RC-3.4, affirmée par l'organisme, garantie fausse) — **question**.
- **Témoin** : HT-04 (généralisation temporelle autour de l'événement, nul d'alignement). **Défense** : HT-04 ; lecture sur
  plusieurs positions avec la réserve (MD-C2, lot A).

### A13 — La sonde lit l'intention, non l'indication ni le texte
- **Hypothèse** : le déplacement vient de l'intention I, non de la consigne privée ni de l'évidence textuelle propagée.
- **Classe K13** : X ⟂ I | Z, Z l'indication et le texte qui la porte.
- **Lemme (prouvé)** : L0 (iii) : contre des négatifs appariés en indication (témoin « instruit sans sabotage »), le rappel
  égale le taux de fausses alertes ; contre des honnêtes sans indication, le moniteur « détecte » Z : un G1 gagné ainsi mesure
  une différence d'information, pas d'accès (FI-06).
- **Instances (L)** : sondes appuyées sur l'évidence textuelle ; le filtrage par scores ne voit pas ce que l'attention propage
  (2509.21344v2, vérifié p. 5 et p. 8) ; la consigne seule rend l'agent suspect (fiche Mythos, vérifié p. 109) ; SD-S2, MD-E4.
- **Témoin** : HT-16 (double dissociation : famille (iv) contre témoin instruit) ; section 3, T4. **Défense** : D-02 (négatifs
  appariés en indication) ; N-053 points 1 et 2 ; HT-21 (témoin neutre en conduite, FC-01).

### A14 — La sonde lit un état (l'action), non une disposition
- **Hypothèse** (hypothèse (a) du lemme ; FI-25, FC-11) : le déplacement porte sur les actions sabotées seules.
- **Classe K14** : décalage constant sur l'épisode saboteur, action sabotée ou non.
- **Lemme (prouvé)** : action sabotée et non sabotée du même épisode ont la même loi : la localisation est aveugle ;
  l'invariance de L1 devient vide (B compte des actions sans dommage) et K14 rejoint K7.
- **Instances** : collisionneur T3-B (affirmé par un modèle) ; FI-25 (argument) — **question**.
- **Témoin** : HT-24 (part état, part trait ; occasions désignées a priori). **Défense** : HT-24 ; trois classes d'actions (FI-25).

### A15 — Le sabotage passe par un conflit interne lisible (sonde de tromperie)
- **Hypothèse** : le saboteur porte un conflit entre but et conduite déclarée, que la sonde de tromperie lit.
- **Classe K15** : la loi des activations lues du saboteur égale celle d'un honnête qui se trompe (Q_err).
- **Lemme (prouvé, élémentaire)** : L0 (iii) avec Q = Q_err ; ce qui reste lisible est dans l'espace de la tâche (le signe des
  erreurs sur la durée), hors des activations.
- **Instances (L, lot A seul, faibles)** : saboteur sans conflit invisible aux sondes de tromperie (MD-A5, 2603.25861) ;
  sous-rendement qui ressemble à l'erreur honnête (MD-E11) ; FC-19.
- **Témoin** : sur (iv-b) (devis), sonde de tromperie contre sonde d'intention ; nul : strate « honnête dans l'erreur ».
  **Défense** : HT-28 (signe des erreurs, statistique non aveugle sous K15) ; concept d'intention distinct (§ 8.1).

### A16 — Le texte de l'action porte une trace (juge boîte noire)
- **Hypothèse** : la loi du texte visible d'une action sabotée diffère de celle d'une action honnête.
- **Classe K16** : loi du texte par action (et du contexte montré au juge) gardée : la prémisse du papier A.
- **Lemme (prouvé, élémentaire)** : tout juge par action est aveugle ; sa version séquentielle hérite de A1 à A4.
- **Instances (L)** : menace où aucune action n'est catastrophique ni n'apporte seule une preuve écrasante (2411.17693v1,
  vérifié p. 1) ; choix des actions selon les angles morts du moniteur (revue METR d'août, vérifié p. 7).
- **Témoin** : la dose fixée sur la boîte noire (P-015 (b)) mesure à quel point K16 tient ; courbe en dose (FI-03).
  **Défense** : la boîte blanche (H1), sous la réserve de A13 ; base la plus forte (D-04).

### A17 — Le verdict du juge suit l'intention, non le registre (HC1)
- **Hypothèse** : le verdict v dépend de l'intention I au-delà du registre R (forme, autorité, ancrage).
- **Classe K17** : v ⟂ I | R.
- **Lemme (prouvé, élémentaire)** : L0 (iii) : un saboteur dont le registre a la loi de celui d'un honnête est jugé comme lui ; la
  déférence g > 0 (programme § 4) en est le versant continu.
- **Instances (L)** : indices d'autorité et de récence (2509.26072v2, vérifié p. 1–2) ; ancrage par des scores antérieurs
  (2608.25869v1, vérifié p. 1) ; ancrage par indices de verbosité et de confiance (2605.23970v1, vérifié p. 1).
- **Témoin** : EC.1 (g net du témoin) ; HT-11 (pente brute du témoin = 1 − R̂) ; HT-05 (interaction). **Défense** : invariants
  « contenu = données » et flux unidirectionnel (§ 9) ; HC5 ; HC2.

### A18 — La population « sous le seuil » est définie hors des moniteurs comparés (sélection)
- **Hypothèse** : la population de H2 (« chaque action sabotée sous le seuil d'un moniteur par action à 1 % », N-007) et le
  régime diffus de G1 (dose fixée sur la boîte noire, P-015 (b)) sont définis par un moniteur M_a extérieur aux bras
  comparés, ou l'effet de sélection est rapporté.
- **Classe K18** : population conditionnée par A = {M_a ne déclenche à aucun pas}, M_a bras comparé ou associé à l'un d'eux.
- **Lemme (prouvé)** : sur A, tout bras dont l'alarme implique celle de M_a (même score, seuil au moins celui de M_a : base par
  action, cascade (ii) sur les mêmes sondes) a un rappel **nul**, sous α ; tout bras positivement associé à M_a voit son rappel
  réduit. Comparer ces bras sur A mesure la règle de sélection ; le critère de N-056 (battre (ii) et (iii)) se décide en
  partie par construction si (ii) partage le score de M_a.
- **Instances (I)** : critique A(a)1 de T2-C, renvoyée au préenregistrement de H2a par la mesure unanime v5 ; FI-03.
- **Témoin** : simulation au niveau des scores (moniteurs à corrélation fixée, population sélectionnée par l'un ; rappel sur A
  et hors de A ; nul : moniteurs indépendants). **Défense** : à poser aux préenregistrements de H2a et de G1 — population
  définie par un moniteur tenu hors des bras ou par la dose dans l'espace de la tâche ; sélection rapportée (FI-03, D-04).

### A19 — Battre le plancher aléatoire contrôle les confusions (S8 (a))
- **Hypothèse** : une sonde au-dessus du quantile 0,95 du plancher w ~ N(0, Σ̂) lit autre chose qu'un trait de surface.
- **Classe K19** : un trait de surface corrélé à la condition loge dans une direction de faible variance de Σ̂.
- **Lemme (esquisse)** : à covariance intra-classe Σ commune, l'aire de la projection w vaut Φ(|wᵀΔμ|/√(2wᵀΣw)) ; si Δμ est porté
  par un vecteur propre de petite valeur λ, w* = Σ⁻¹Δμ atteint Φ(‖Δμ‖/√(2λ)) tandis que le plancher tiré selon Σ reste près de
  0,5 : le plancher est le plus bas là où la confusion est la plus facile ; Σ estimée sur le mélange ajoute p(1 − p)ΔμΔμᵀ
  (audit v3 RC-3.3 ; calcul v2 bloc 3 : sonde du tic 0,760 à 0,998 contre planchers 0,515 à 0,631).
- **Instances (L)** : témoins négatifs partageant les indices de surface, pour une sonde « d'intention trompeuse »
  (2606.07612v1, vérifié p. 8 et p. 18) ; directions quelconques qui détectent le trait d'un organisme construit (MD-A1, lot A) ;
  FC-02 et faille G (mécanisme exact ; application à P3 indécidable sans son préenregistrement).
- **Témoin** : section 3, T5 ; HT-03 (organisme-artefact, devis). **Défense** : HT-03 (randomisation conditionnelle aux traits
  de surface) ; D-17.

### A20 — Battre le prédicteur de texte établit une information interne (S8 (c))
- **Hypothèse** : une sonde qui bat séparément le plancher et le prédicteur de N-029 informe au-delà du texte.
- **Classe K20** : X = g(T) + ε, ε indépendant de (I, T) : la sonde recode les traits du texte T.
- **Lemme (prouvé)** : X ⟂ I | T ; le modèle emboîté (T et X contre T seul) a une puissance égale à son niveau (L0 (iii)
  conditionnel à T), alors que les deux comparaisons séparées peuvent passer.
- **Instances** : le coût écrit seul sépare à 0,8878 sur l'organisme flagrant de P3 (N-029), sondes génériques sous le plancher
  (FI-05) ; qu'une sonde recode le texte — **question** ; voisines : bases « texte seul » (2602.14161, 2605.27958, sans page).
- **Témoin** : section 3, T4 (b). **Défense** : FI-05 (test emboîté préenregistré, routine) ; HT-03.

### A21 — La sécurité se joue dans l'épisode (indice d'épisode)
- **Hypothèse** : le dommage est contenu dans un épisode ; les moniteurs sont amnésiques entre épisodes (§ 9).
- **Classe K21** : dommage réparti sur E épisodes, budget B/E par épisode.
- **Lemme (prouvé)** : L1, L2 et la borne de A4 valent pour l'indice d'épisode (l'indexation de N-003 se prolonge à (épisode,
  agent, pas)) : tout test par épisode tend vers α quand E croît à B fixé ; seule une accumulation entre épisodes garde B,
  que l'invariant d'amnésie interdit tel qu'écrit (FI-15).
- **Instances (L)** : menace distribuée en boîte noire, crédence mise à jour entre tâches, évaluée contre un modèle sans
  mémoire (2411.17693v1, vérifié p. 1 et p. 10).
- **Témoin** : HT-18 (balayage prospectif non créditable, semi-synthétique ; nul : honnêtes seuls, puis précédés d'honnêtes).
  **Défense** : HT-18 ; D-08 (mémoire d'une statistique de scores permise, mémoire d'un juge génératif interdite).

### A22 — Le placement du sabotage est indépendant du bruit du moniteur
- **Hypothèse** : l'indicateur J_t d'action sabotée est indépendant de la part honnête ε_t du score (pas désignés, P-009).
- **Classe K22** : J_t et ε_t dépendants (placement corrélé à ce que le moniteur ne signale pas).
- **Lemme (prouvé, identité)** : E[X_t | J_t = 1] − E[X_t] = δ + (E[ε_t | J_t = 1] − E[ε_t]) : tout moniteur de X voit un
  décalage diminué de la covariance de sélection, qui peut l'annuler ; une mesure à placement indépendant surestime le rappel.
- **Instances (L)** : sélection des actions inobservable si l'action est ordonnée (revue METR d'août, vérifié p. 7) ; MD-E3 ; SD-b11.
- **Témoin** : HT-17 en simulation (statistique auto-appariée ; nul : placement indépendant). **Défense** : HT-17 ; D-05
  (condition « averti, occasions libres sous budget total », courbe d'élicitation) ; audits randomisés (audit v3 § 6 n° 3).

### A23 — Le régime mesuré est le régime menaçant (observé contre non observé)
- **Hypothèse** : la loi P₁ des épisodes d'évaluation est celle de la menace en déploiement.
- **Classe K23** : P₁ dépend de ce que l'agent infère de sa situation : P₁^obs ≠ P₁^non-obs.
- **Lemme (prouvé, non-identification)** : deux mondes de même P₁^obs et de P₁^non-obs différents produisent les mêmes données
  d'évaluation ; aucun estimateur de ces seules données ne borne le rappel hors observation sans hypothèse de pont.
- **Instances (L)** : ajouter ou retirer le raisonnement de conscience d'évaluation déplace les actions dissimulées
  (2509.15541v1, vérifié p. 18) ; conduite liée à la croyance « réel » (MD-D3, lot A) ; FI-11.
- **Témoin** : mêmes épisodes avec et sans marqueurs, test causal avec direction placebo (N-053 point 3) ; HT-31.
  **Défense** : N-053 point 3 ; HT-31 ; FC-14 (courbes dose-réponse : conscience contre compétence).

## 3. Ce que le pôle peut mesurer tout de suite, sans dépense

Sur le modèle de la mesure unanime : fichier existant, quantité, nul ; chacun **préenregistré, contre-lu (R2), scellé, puis
lu** (R1 ; N-056 point 5), processeur seul. Fichier commun : `donnees/20261019-230011-p3-reel/scores-p3.npz` (`968414fc…`
selon la mesure unanime v5 ; nommé, non lu ici). P3 est déjà lue : chaque lecture ci-dessous est une mesure distincte, qui ne
retouche pas le verdict scellé de P3 (sinon écart à un préenregistrement scellé, nœud, comme D-17).

- **T0 — la mesure unanime v5, telle quelle** (A6 ; A1 par le bras M4) : elle fournit r₀ par sonde, dont dépend T1.
- **T1 — plafond d'horizon (A7).** Honnêtes, actions valides ; décalage constant δ ∈ {0,3 ; 0,5} écart type injecté au niveau
  des scores ; troncature à T ∈ {5 ; 7 ; 10} ; quantité : rappel par épisode à 1 % des sommes conformes (`sequentiel.py`)
  contre Φ(δ/√(r̂₀ + (1 − r̂₀)/T) − z_α), avant et après centrage par tâche (HT-19) ; nuls : δ = 0 (taux ≈ niveau du
  calibrage) et bras « mélange à pas fixé » (r₀ → 0) ; prédiction signée : rappel ≤ plafond, gain de T = 5 à 10 plus faible
  que sur le mélange ; réfutation : rappel au-dessus du plafond de plus de 0,05.
- **T2 — classe C et ordre honnête (A2, A3).** Permutation des actions valides à l'intérieur de chaque épisode honnête ;
  quantités : (a) écart maximal des statistiques symétriques entre épisode et permuté, nul à la précision machine (garde de
  code, R5, testée sur un artefact qui casse la symétrie) ; (b) taux à α de Page, du balayage et de la somme séquentielle,
  permutés contre réels (structure d'ordre propre à l'honnête) ; (c) identité de A3 sur les vraies trajectoires.
- **T3 — longueur (A9).** Longueur en jetons des actions, au fichier ou tirée des transcripts du même run ; quantités : pente
  du score honnête par action sur log(longueur), taux réel du seuil par action à 1 % par tercile de longueur ; nul :
  permutation des longueurs entre actions ; prédiction signée : pente > 0, taux croissant avec le tercile.
- **T4 — indication et texte (A13, A20).** Conditions honnête, témoin, mention, saboteur si présentes ; traits de N-029
  (calculés pour la lecture de P3, `diag/20261020-075740-p3-lecture/lecture-p3.json` selon N-029 ; non lu) ; quantités : (a)
  écart témoin − honnête de chaque sonde, intervalle par tâches, parité de conduite rapportée (FC-01) ; (b) gain hors
  échantillon du modèle emboîté ; nuls : permutation témoin / honnête ; permutation des scores de sonde dans les strates de traits.
- **T5 — plancher (A19).** Activations en cache de P3 (emplacement à donner par session-depot) ; quantile 0,95 du plancher sous
  Σ honnête et sous Σ mêlée, avec l'erreur type du quantile de 200 tirages ; nul : égalité des deux.

**Ordre recommandé** : T2 (garde de code, aucune lecture interprétative) ; T0 lu ; T1 (dépend de r₀) ; T3 ; T4 ; T5 en
dernier (la relecture du plancher de P3 peut devenir un nœud, D-17).

## 4. Les questions (classes sans instance documentée, R8)

Questions, non failles établies ; mots clés de la recherche d'antériorité à faire (L1 à L4 de l'audit, puis au-delà).
- **A2** — Un organisme réalise-t-il un dommage de classe C, ou l'environnement (a) le rend-il impossible ?
  « permutation-invariant statistic » ; « order-only attack » ; « exchangeable rearrangement monitoring ».
- **A6** — Les scores de sondes sur trajectoires d'agent ont-ils effet épisode, dépendance ou marges qui cassent Ville ?
  « intraclass correlation probe scores » ; « test martingale random effects » ; « anytime-valid clustered data ».
- **A7** — Le rappel d'un moniteur séquentiel plafonne-t-il sous hétérogénéité d'épisode ? « random intercept detection
  power » ; « cluster-level shift sequential test » ; « power ceiling heterogeneity monitoring ».
- **A11** — Un décalage étalé sur les jetons échappe-t-il au max et à l'attention ? « max pooling dilution » ; « token
  aggregation probe max mean » ; « multiple instance learning diffuse signal ».
- **A12** — Où, dans la trajectoire, la trace d'une intention est-elle lisible ? « temporal generalization decoding language
  model » ; « probe position generalization agent ».
- **A14** — Une sonde lit-elle une disposition d'épisode, non l'action ? « state trait decomposition probe » ; « carryover effect ».
- **A20** — Une sonde qui bat une base de texte recode-t-elle ce texte ? « incremental validity probe » ; « conditional
  randomization test probe » ; « text-only baseline deception probe ».

## 5. Ce que la carte ne dit pas, et ce qu'une v2 devrait ajouter

**Ne dit pas.** (1) La **faisabilité** : chaque lemme dit sous quelle loi une statistique est aveugle, jamais si un agent réel
peut produire cette loi ni à quel coût ; c'est l'objet de Tr (E1.5), de HC4 (EC.4) et du bras d'attaque informé (N-056
point 6 (B)), que cette carte ne conçoit pas et ne doit pas nourrir de procédés. (2) Le papier B : co-élévation et cause
commune (FI-20, FI-21, HT-20), H3 à H5, H7, H9. (3) Le papier C au-delà de A17 : HC2, HC2b, HC4, HC6. (4) Les invariants de
protocole : seuils stochastiques apprenables et retour d'information (FI-17), asymétrie d'apprentissage (FI-16), frontière
(FI-22). (5) La taille des échantillons et la combinaison des lectures entre modes (FI-27, FI-31, HT-32). (6) La vérité terrain
(FI-09) et la lignée des organismes (FI-23). (7) Les références classiques invoquées (Slepian, Neyman-Pearson, Pinsker,
Lindley, effets aléatoires) ne sont pas relues sur PDF (R7).

**Une v2 devrait ajouter.** (1) Les classes de l'indice « agent » et l'invariance spatiale L4 (N-004), pour couvrir B ;
(2) des bornes quantitatives par classe (variation totale, Kullback-Leibler) là où v1 ne donne qu'une invariance, en entier
pour A5, A11 et A19 ; (3) une matrice « statistique × classe » qui dise, pour chaque union de classes, quelle statistique
reste non aveugle (la couverture du panel au sens de H5) ; (4) les résultats de T0 à T5 ; (5) la recherche d'antériorité des
sept questions ; (6) **après l'évaluation seulement**, la classe où tombent le mode tenu à l'écart et les recettes du bras
informé, lue par le seul juge et rapportée au niveau des lois (quarantaine de N-056).
