# Réponse approfondie — Boucle de rétroaction « Organisme d'idéation ⇄ Programme de contrôle de l'intelligence artificielle » (Carbon, effort élevé, v1)

Pièce de conception approfondie (classe C), produite par Carbon en effort élevé en remplacement temporaire de Fable autorisé par `GO-2026-11-23-33`, sous le mandat `GO-2026-11-23-34`. Langue : français, aucun acronyme non développé, aucun emoji. Tous les blocs numériques renvoient à `calculs-boucle-organisme-controle-v1.py` et à sa sortie `calculs-boucle-organisme-controle-v1.txt` (suppositions d'illustration explicitement marquées, aucune donnée privée ni résultat d'expérience réelle du dépôt ouvert).

---

## Synthèse exécutive

Pour que l'organisme d'idéation devienne un véritable moteur de percées pour le programme de contrôle boîte blanche des menaces diffuses — sans dégrader la validité statistique des portes du programme ni s'enfermer dans un sur-ajustement stérile — quatre lois gouvernent l'architecture et l'ordre des priorités :

1. **Trois flux cloisonnés et deux horloges disjointes.** L'organisme d'idéation ne peut contribuer au programme de contrôle que si ses boucles internes (conception et sélection sur mondes plantés sur processeur) restent **mathématiquement séparées** des bancs du programme de contrôle (familles tenues à l'écart à lecture unique et validation finale à générateur distinct). Tout partage de verdict de moniteur ou de juge de contrôle vers la sélection de l'organisme (`rho > 0`) détruit la portée de la mesure par attaque adaptative de type *Ladder* (Blum et Hardt 2015 ; Dwork et al. 2015 ; `N-050`, `N-053`, `N-058`).
2. **Effet filtre économique sur le goulot des cartes graphiques.** Dans nos calculs illustratifs (bloc `[A]` de `calculs-boucle-organisme-controle-v1.txt`), un filtre strict sur mondes plantés qui abaisse la fausse admission `alpha_o` de `1,00` (tirage brut) à `0,005` tout en maintenant une sensibilité `q_o = 0,75` multiplie par **21,5 fois** le nombre d'idées valides réellement découvertes par tranche de `100` dollars américains dépensés sur cartes graphiques (de `0,36` à `7,76` percées valides pour `100` dollars).
3. **Théorème de rendement décroissant sous couverture incomplète.** Lorsque les mondes plantés sur lesquels l'organisme s'optimise omettent une fraction `(1 - kappa)` des classes d'invariants réels du contrôle (par exemple la collusion multi-agents, les canaux de retour ou les attaques adaptatives sur activations), le gain réel sature au plus à `kappa * P_max` et **décroît** passé un effort critique fini `E*` si une taxe de spécialisation `tau_s > 0` s'exerce (bloc `[C]`). Améliorer l'organisme exige donc d'abord d'élargir les classes d'invariants représentables dans ses mondes plantés.
4. **Le noyau invariant des priorités (Top 5 robuste).** L'analyse de sensibilité bilatérale sur neuf schémas de pondération (`calculs-boucle-organisme-controle-v1.txt`, bloc `[D]`) établit que **quatre chantiers dominent invariablement le haut du classement** (`C1`, `C2`, `C3`, `C5`), suivis immédiatement par le banc à vérité plantée (`C4`), tous activables dès les premiers jours sur processeur seul avant toute dépense lourde sur cartes graphiques.

---

## 1. Architecture de la boucle fermée et invariants de séparation

Une boucle de rétroaction naïve (« l'organisme propose des détecteurs → le banc de contrôle les note → l'organisme s'améliore sur ces notes ») viole simultanément les décisions `N-050` (lecture unique du jeu final), `N-053` point 5 (aucun score de moniteur dans l'entraînement ou la sélection d'un agent ou d'un proposeur), `N-058` (la composition des proposeurs se juge sur l'oracle du monde planté et le coût, jamais sur le verdict du juge) et `N-062` (chaque cycle de reconception des sondes consomme une famille tenue à l'écart neuve à usage unique).

Pour résoudre cette tension, la boucle fermée doit être scindée en **trois flux asymétriques et étanches** :

| Flux | Direction | Contenu transmis | Règle d'étanchéité obligatoire |
|---|---|---|---|
| **Flux aval (Découverte → Instruments de contrôle)** | Organisme d'idéation ──▶ Programme de contrôle | Objets mathématiques candidats (opérateurs d'agrégation, détecteurs d'obstructions de faisceau, protocoles d'audit), bancs à vérité plantée exécutables (`N-076` § 4). | Chaque candidat promu est traité comme un simple matériau brut (`N-065` rôle 2) ; il n'entre dans une porte (`G1`, `GC`, `G2`) qu'après **préenregistrement scellé et contre-lu** (`R1`, `R2`) et mesure sur une famille tenue à l'écart neuve (`N-054`, `N-062`). |
| **Flux amont (Tensions du contrôle → Cibles d'idéation)** | Littérature et diagnostics du contrôle ──▶ Organisme d'idéation | Corpus public daté d'articles de sûreté et d'interprétabilité, diagnostics d'échecs de sondes **sur les seuls modes déjà vus** ou sur strates abstraites (`H8` comme diagnostic selon `N-062`), failles d'oracles (`N-075`, `N-076`). | **Interdiction absolue** de transmettre à l'organisme les résultats de la famille tenue à l'écart, les clés secrètes des oracles ou les scores numériques de moniteurs sur les épisodes d'épreuve (`N-053`, `N-058`, `N-076` § 8). |
| **Flux adverse (Invention de menaces → Équipe rouge)** | Organisme d'idéation ──▶ Bras d'attaque en quarantaine | Familles conceptuelles de sabotage inédites, scénarios de tromperie du juge statistique (`N-065` rôle 3). | **Quarantaine unidirectionnelle** (`N-054` point 3, `N-056` point 6) : les recettes produites pour le mode tenu à l'écart sont scellées par un tiers et restent invisibles aux concepteurs de moniteurs et aux cycles d'entraînement de l'organisme jusqu'au verdict. |

---

## 2. Modélisation mathématique rigoureuse de la boucle fermée

### 2.1 Équation de bilan : filtre sur mondes plantés contre coût d'oracle sur cartes graphiques

Soit un cycle de fonctionnement de l'organisme produisant `N_cand` fiches ou mécanismes candidats sur processeur ou par appels légers, à un coût unitaire `c_f`. Parmi ces `N_cand` candidats, une fraction `pi_0` appartient à la classe des découvertes réellement fécondes et non redondantes dans le programme de contrôle, et `(1 - pi_0)` représente des faux positifs, des métaphores creuses ou des artéfacts de surface.

L'oracle du monde planté de l'organisme agit comme un filtre binaire (ou probabiliste) caractérisé par sa sensibilité `q_o` (probabilité de retenir une percée vraie, bornée par l'identification sur les strates couvertes au sens de `N-075` erratum 3) et son taux de faux positifs `alpha_o` (probabilité de promouvoir une fausse idée). Le nombre attendu de candidats promus vers les épreuves coûteuses sur cartes graphiques (modèles ouverts à huit milliards de paramètres, coût unitaire `c_gpu`) est :

$$E[N_{\text{promus}}] = N_{\text{cand}} \cdot \big(\pi_0 q_o + (1 - \pi_0) \alpha_o\big)$$

La précision post-filtrage des candidats soumis aux cartes graphiques vaut :

$$P(\text{vrai} \mid \text{promu}) = \frac{\pi_0 q_o}{\pi_0 q_o + (1 - \pi_0) \alpha_o}$$

Sous un budget total par cycle `B_cycle`, le budget résiduel pour les vérifications sur cartes graphiques est `B_gpu = max(0, B_cycle - N_cand * c_f)`, permettant d'éprouver au plus `M_gpu = floor(B_gpu / c_gpu)` candidats. Le nombre attendu de percées valides découvertes et prouvées par cycle est alors :

$$V_{\text{découvertes}} = \min\!\big(E[N_{\text{promus}}],\, M_{\text{gpu}}\big) \cdot \frac{\pi_0 q_o}{\pi_0 q_o + (1 - \pi_0)\alpha_o}$$

**Vérification numérique et objets de contrôle (bloc `[A]` de `calculs-boucle-organisme-controle-v1.txt`)** — Sous des suppositions d'illustration explicites (`N_cand = 500`, `pi_0 = 4,00 %`, `c_f = 0,05` dollar par candidat, `c_gpu = 8,00` dollars par épreuve sur carte graphique, `B_cycle = 100` dollars, soit `M_gpu = 9` épreuves finançables après `25` dollars de filtrage) :

| Régime du filtre sur mondes plantés | `alpha_o` | `q_o` | Promus attendus | Percées valides par `100` dollars | Statut |
|---|---|---|---|---|---|
| Objet faux (aucun filtre, tirage brut) | `1,000` | `1,00` | `500,0` | `0,36` | Témoin nul exact (`9 × 0,04 = 0,36`) |
| Filtre faible (bricolé, haute fausse admission) | `0,250` | `0,70` | `134,0` | `0,94` | Saturé par le bruit |
| Filtre modéré (sans audit de générateur) | `0,080` | `0,75` | `53,4` | `2,53` | Gain modeste |
| Filtre rigoureux (scission + compression) | `0,020` | `0,80` | `25,6` | `5,62` | Régime cible intermédiaire |
| Filtre strict (e-valeurs + nul d'archive) | `0,005` | `0,75` | `17,4` | **`7,76`** | Optimum de rendement (`× 21,5` vs brut) |
| Objet mort (filtre trop dur, `q_o = 0`) | `0,001` | `0,00` | `0,5` | **`0,00`** | Rejet exact (doit mourir) |

Ce modèle démontre que **la réduction du taux de fausses admissions `alpha_o` de `0,25` à `0,005` a un effet multiplicateur supérieur d'un ordre de grandeur à l'augmentation brute du nombre de cartes graphiques** : tant que `alpha_o > pi_0`, le budget de calcul sur cartes graphiques est brûlé à tester des faux positifs.

---

### 2.2 Contamination adaptative (`N-050`, `N-058`, `N-062`) et élimination par cloisonnement à trois strates

Si l'organisme d'idéation sélectionne la meilleure parmi `M` variantes de conception (ou `K` générations × variantes) en lisant directement ou indirectement un banc partagé de `n` tâches de contrôle dont une fraction `rho ∈ [0, 1]` recouvre le banc d'évaluation final, l'optimisme adaptatif (Blum et Hardt 2015, « The Ladder » ; Dwork et al. 2015) injecte un biais d'espérance maximale approximé à l'ordre dominant par :

$$\text{Biais}_{\text{opt}}(M, n) \approx \sigma \sqrt{\frac{2 \ln M}{n}}$$

où `sigma` désigne l'écart type empirique par tâche de la métrique d'évaluation. Le score apparent mesuré sur l'évaluation vaut :

$$\Delta_{\text{apparent}} = \Delta_{\text{réel}} + \rho \cdot \sigma \sqrt{\frac{2 \ln M}{n}}$$

De plus, comme l'établit la lecture de la décision `N-073` (section 4, citant Zhu et al., arXiv 2609.18366), même lorsque les identifiants de tâches sont disjoints (`rho_taches = 0`), deux lots issus du **même générateur de tâches** conservent un recouvrement structurel `rho_gen > 0` sur les raccourcis de présentation du générateur (longueur, marqueurs stylistiques, positions de cibles).

**Vérification numérique (bloc `[B]` de `calculs-boucle-organisme-controle-v1.txt`)** — Pour `sigma = 0,35` et un banc de `n = 60` tâches sous le nul vrai (`Delta_réel = 0`, objet de contrôle « doit mourir ») :
- avec une fuite complète (`rho = 1,0`) et `M = 200` variantes évaluées au fil des cycles, un mécanisme parfaitement inutile affiche un **gain illusoire de `+0,1471`**, indiscernable d'une véritable avancée (`+0,1800`) ;
- même une fuite partielle de moitié (`rho = 0,5`) crée un faux gain de `+0,0735` ;
- **l'élimination mathématique exige `rho = 0` exact** au niveau à la fois des tâches **et** du générateur.

**Règle architecturale de cloisonnement à trois strates disjointes :**
1. **Strate `F_org` (Vivier interne de l'organisme)** : familles de mondes plantés sur processeur et corpus publics datés utilisés librement par l'organisme pour concevoir, élaguer et apprendre ses opérateurs (règle de l'oracle interne seul selon `N-058`, aucun score du banc de contrôle).
2. **Strate `F_ecart` (Familles tenues à l'écart du contrôle, `N-054` et `N-062`)** : pour chaque cycle d'intégration d'une découverte de l'organisme dans les moniteurs du contrôle, une famille de sabotage inédite conçue par une instance isolée en quarantaine, lue **une seule fois** sur verdict préenregistré (`R1`, `R13`). Une fois lue, elle passe dans les modes vus ou est archivée, et ne sert jamais plus de juge final.
3. **Strate `F_final` (Validation ultime et banque de confirmation, `N-050`, `N-059`, `N-073`)** : banque construite par un **générateur distinct** audité sur traits de présentation seuls (pour annuler `rho_gen`), tenue scellée et lue une seule fois en fin de boucle pour les revendications finales des papiers A, B et C.

---

### 2.3 Théorème de rendement décroissant quand les mondes plantés manquent une classe d'invariants réels

Soit `U` l'univers des classes d'invariants et de mécanismes de sabotage du contrôle réel (par exemple : décalage marginal distribué dans le temps, corrélation entre copies à marginale préservée, évasion adaptative sur activations, attaque de style du moniteur génératif, censure du canal de retour). Supposons que les mondes plantés sur lesquels l'organisme est optimisé ne couvrent qu'une fraction `kappa ∈ [0, 1]` de ces classes, et omettent complètement la fraction complémentaire `(1 - kappa)`.

Lorsque l'organisme consacre un effort croissant `E` (nombre de cycles de recherche et de raffinement sur ses mondes plantés), l'efficacité sur les classes couvertes sature vers `P_max` au taux `lambda_o`, mais la spécialisation croissante sur les raccourcis propres aux mondes plantés induit une taxe de dérive `tau_s >= 0` sur les classes absentes de valeur initiale `p_base` :

$$V_{\text{réel}}(E) = \kappa \, P_{\max} \big(1 - e^{-\lambda_o E}\big) + (1 - \kappa) \, p_{\text{base}} \, e^{-\tau_s E}$$

**Énoncé du théorème de rendement décroissant :**
1. **Plafond asymptotique irréductible.** Dès que `kappa < 1`, même avec un effort infini sur l'organisme, `lim_{E → +∞} V_réel(E) = kappa * P_max < P_max` : l'organisme est structurellement aveugle aux classes non plantées.
2. **Renversement négatif sous spécialisation (`tau_s > 0`).** Si `(1 - kappa) * p_base * tau_s < kappa * P_max * lambda_o` et `lambda_o > tau_s`, la courbe `V_réel(E)` possède un **optimum fini unique** :
   $$E^* = \frac{1}{\lambda_o - \tau_s} \ln\!\left(\frac{\kappa \, P_{\max} \, \lambda_o}{(1 - \kappa) \, p_{\text{base}} \, \tau_s}\right)$$
   Passé `E*`, continuer d'améliorer et de sélectionner l'organisme sur ses mondes plantés **détruit** la performance réelle sur le programme de contrôle (`dV_réel / dE < 0`).
3. **Effondrement total si `kappa = 0`.** Si les mondes plantés manquent tous les invariants pertinents (`kappa = 0`), `E* = 0` : tout cycle d'optimisation réduit l'utilité réelle (`V_réel` chute de `0,1500` à `0,0001` à `E = 500`, bloc `[C]` de `calculs-boucle-organisme-controle-v1.txt`).

**Illustration numérique (bloc `[C]` : `P_max = 0,85`, `lambda_o = 0,04`, `p_base = 0,15`, `tau_s = 0,015`) :**
- Pour `kappa = 1,00` (couverture complète des invariants) : `V_réel` croît monotonement jusqu'à `0,8500` (`E* = +∞`).
- Pour `kappa = 0,50` (la moitié des classes d'invariants manque) : `V_réel` culmine à `E* = 108,6` (`0,4342`), puis retombe vers `0,4250`.
- Pour `kappa = 0,25` : `V_réel` culmine très tôt à `E* = 64,7` (`0,2392`), puis baisse à `0,2126`.

**Conséquence directe pour le programme :** avant de multiplier la puissance de recherche de l'organisme, la priorité absolue est d'augmenter `kappa` — en injectant dans les mondes plantés les classes d'invariants manquantes issues du programme de contrôle (scissions conceptuelles, corrélations sans décalage marginal, failles d'oracles et stratégies à canal de retour).

---

## 3. Objets de contrôle « doit mourir » (règles R4 et R5)

Tout mécanisme candidat, toute architecture de boucle et tout banc reliant l'organisme au contrôle doit passer quatre épreuves négatives obligatoires avant d'être crédité d'aucun progrès :

1. **Témoin « sélection circulaire sur le juge du contrôle » (`C11`)** : un organisme branché sur les verdicts réels des juges ou des moniteurs du programme de contrôle sur un banc partagé (`rho > 0`, `M = 200`). Sous le nul vrai (`Delta_réel = 0`), il produit un gain apparent artificiel de `+0,1471` (bloc `[B]`) tout en échouant sur la strate tenue à l'écart (`F_ecart`). Toute architecture qui ne bloque pas et ne rejette pas ce couplage par construction (garde logicielle testée sain/artefact selon `R5` et `N-053` point 5) **doit mourir**.
2. **Témoin « filtre mort ou insensible à la strate cible » (`q_o = 0`)** : dans l'équation `[A]`, si l'oracle du monde planté ne voit pas le genre d'invariant recherché (`q_o = 0`), même un taux de fausses admissions minuscule (`0,001`) produit `0,00` percée valide. Sur un monde planté où l'invariant vrai est déplacé hors de la spécification du détecteur (par exemple dommage purement corrélationnel à marginale constante face à un détecteur marginaliste selon `N-003`), le détecteur candidat doit rapporter une sensibilité nulle et jamais se déclarer fiable (`N-075` erratum 3).
3. **Témoin « mondes plantés à couverture nulle des invariants réels » (`kappa = 0`)** : dans le modèle `[C]`, lorsque les mondes plantés de l'organisme ne capturent aucune classe réelle de sabotage, tout cycle d'optimisation doit être refusé dès que le test de transfert sur `F_ecart` stagne ou baisse (`V_réel` chute de `0,1500` à `0,0158` à `E = 150`).
4. **Témoin « générateur qui fuit sans nouvelle loi »** : un organisme ou un opérateur testé sur deux banques sœurs tirées du même générateur (`N-073` § 4, audit du générateur) ne doit jamais voir sa performance s'expliquer par un prédicteur entraîné sur les seuls traits de surface ou de présentation (longueur, format, positions).

---

## 4. Programme des priorités : classement rigoureux et sensibilité aux poids

Selon la formule exacte demandée :

$$\text{score} = \frac{\text{gain\_informatif} \times \text{facilité} \times \text{portée} \times \text{potentiel\_de\_découverte\_majeure}}{\text{coût}}$$

chaque critère étant noté de `1` à `5` (`coût = 1` : quasi nul, processeur seul en quelques jours ; `5` : lourd en cartes graphiques ou en validation humaine), voici le classement consolidé de la boucle fermée (vérifié dans `calculs-boucle-organisme-controle-v1.py`, bloc `[D]`) :

| Rang | Code | Chantier prioritaire (en clair) | G | F | C | P | D | Score | Rôle exact dans la boucle et expérience décisive associée |
|---|---|---|---|---|---|---|---|---|---|
| **1** | `C1` | **Cloisonnement strict à trois strates** (`F_org` / `F_ecart` / `F_final`) et audit préalable des générateurs sur traits de présentation seuls | 5 | 5 | 1 | 5 | 4 | **500,0** | Condition de validité sans laquelle toute la boucle est contaminée (`N-050`, `N-058`, `N-073`). Vérifiable sur processeur en `2` à `3` jours par tests d'artefacts (`R5`) et classifieur de surface sur les générateurs de mondes plantés. |
| **1 ex.** | `C2` | **Branchement de l'opérateur de scission conceptuelle** (faisceaux cellulaires, noyau du cobord et découpe en sous-rôles) sur les faux amalgames du contrôle boîte blanche | 5 | 4 | 1 | 5 | 5 | **500,0** | Relie directement l'organisme (`GO-2026-11-23-28`, `IDE-2026-11-23-006`) aux verrous centraux du contrôle : dissocier « conscience d'évaluation », « présence d'instruction cachée », « style rhétorique » et « intention de saboter » (`H8`, `HC2`, passage obligé de `N-075`). Testable d'abord rétrospectivement sur processeur (`T5`) et sur activations déjà extraites ou mondes plantés. |
| **1 ex.** | `C3` | **Détecteurs sémantiques des cinq signaux ex ante** appliqués au corpus récent de sûreté, d'alignement et d'interprétabilité mécaniste | 5 | 4 | 1 | 5 | 5 | **500,0** | Flux amont (`IDE-2026-11-23-030`, `041`, `051`) : cartographie automatiquement les foyers d'épicycles ad hoc, d'entropie notationnelle et de ruptures de typage dans la littérature d'alignement gelée à `t0 = 2024` pour prédire rétrospectivement les ruptures de `2025-2026` avant d'orienter l'organisme. |
| **1 ex.** | `C5` | **Validation empirique en 3 à 5 jours sur processeur des briques de base de l'organisme** sur données publiques datées et jeux d'experts avant dégel | 5 | 5 | 1 | 5 | 4 | **500,0** | Assise empirique sans coût de cartes graphiques (`IDE-2026-11-23-027` sur PubTator 3, `IDE-2026-11-23-028` bras A et C sur les `2 996` notes de Gu et Krenn 2026, `IDE-2026-11-23-032` sur macros et arbres d'équations avant Fomin et Zelevinsky 2002) : élimine tout opérateur de l'organisme qui ne bat pas le hasard avant de le coupler au contrôle. |
| **5** | `C4` | **Banc de recherche à vérité plantée** (lois statistiques et dommages exacts calculables hors machine, `N-076` § 4, `N-065` rôle 3) | 5 | 4 | 2 | 5 | 5 | **250,0** | Pont bidirectionnel (`N-076` point 3, `GO-2026-11-21-60`) : fournit au programme de contrôle un environnement flou à la relecture mais exact en aval (`q_o` mesurable sans biais de lecteurs) tout en augmentant la couverture `kappa` des mondes de l'organisme. |
| **6** | `C7` | **Chaîne d'épreuves d'admission de l'oracle et de l'audit** (épreuves du devin, séparation du jumeau, calibration sur référence honnête `m >= n`) | 5 | 4 | 1 | 4 | 3 | **240,0** | Garantit la mesure honnête de la boucle (`N-075`, `N-076`) : empêche de prendre un plafond dû à une petite référence (`m`) ou une fuite temporelle pour un gain d'accumulation ou d'idéation. |
| **7** | `C6` | **Cycle Éveil-Sommeil hybride** (abstraction par grand modèle + compression inter-bassins exacte par longueur de description minimale de type Stitch) | 5 | 3 | 2 | 5 | 5 | **187,5** | Moteur d'invention d'objets mathématiques hors alphabet (`IDE-2026-11-23-031`, `043`, `049`) : vise la synthèse d'agrégateurs ou d'invariants de contrôle nouveaux quand les primitives existantes échouent, sous condition d'étanchéité temporelle (`IDE-2026-11-23-044`). |
| **8** | `C8` | **Génération de modes de sabotage inédits par l'organisme en quarantaine** (`N-065` rôle 3 seconde moitié, `N-056`) | 4 | 3 | 2 | 4 | 5 | **120,0** | Flux adverse vers la strate `F_ecart` : alimente les cycles de reconception de `G1` (`N-062`) en attaques diffuses inédites et en stratégies d'évasion du juge statistique. À n'activer qu'après validation du banc `C4` (`N-076` § 13 point 5). |
| **9** | `C9` | **Sondes passives de surprise / erreur de prédiction** (lecture au dernier jeton sans optimisation directe, `N-076` § 10) | 3 | 3 | 2 | 4 | 4 | **72,0** | Mesure exploratoire conditionnée à la question préalable de `N-076` § 10 (la sonde de surprise ajoute-t-elle quoi que ce soit à la différence de deux lectures de réussite attendue ?). Coût en cartes graphiques et corrélation modeste rapportée chez Xu et al. 2026 (`< 0,4` en mathématiques). |
| **10** | `C10` | Réécritures éditoriales de vulgarisation ou mise en forme (témoin bas hors boucle technique) | 2 | 4 | 1 | 2 | 1 | **16,0** | Aucun effet sur le taux de découverte ni sur la robustesse des moniteurs. |
| **11** | `C11` | **[OBJET DOIT MOURIR]** Sélection directe des proposeurs ou opérateurs de l'organisme sur les scores des moniteurs ou des juges du contrôle | 1 | 5 | 1 | 1 | 1 | **5,0** | Disqualifié par `N-053` point 5 et `N-058` ; produit de fausses percées par attaque de *Ladder* (bloc `[B]`). |

### Analyse de sensibilité aux poids (bloc `[D]`)

En faisant varier l'exposant de chacun des cinq critères de `-50 %` (`0,5`) à `+50 %` (`1,5`) sur **neuf schémas de pondération distincts**, les résultats montrent une stabilité remarquable :
- **Noyau invariant du Top 5 (9 schémas sur 9)** : `C1`, `C2`, `C3` et `C5` appartiennent systématiquement au Top 4 sous **tous** les régimes de poids, et `C4` occupe la 5e ou 6e place selon le poids du coût.
- **Seule inversion notable** : lorsque la priorité est fortement déplacée vers le potentiel de découverte majeure (`D^1,5`), le couple scission + signaux ex ante (`C2`, `C3`) passe devant `C1` et le cycle Éveil-Sommeil (`C6`) monte au rang 6 devant `C7` ; lorsque le coût strict prime (`C^1,5`) ou la facilité prime (`F^1,5`), les briques processeur gratuites (`C1`, `C5`, `C2`, `C3`, `C7`) dominent absolument.
- **Invariants de queue (9 schémas sur 9)** : `C10` et `C11` restent invariablement aux deux dernières places.

---

## 5. Plan d'exécution en duel d'hypothèses falsifiables (enchaînement concret)

Pour passer immédiatement de l'analyse à l'épreuve sans violer les chantiers actifs (`CLAUDE.md` l. 56) ni dépenser sans devis :

1. **Semaine 1 (Processeur seul, zéro dollar d'infrastructure sur cartes graphiques) — Trancher `C1`, `C5` et les pré-tests de `C2`/`C3` :**
   - *Duel 1 (`C5`, validation de l'organisme)* : préenregistrer et exécuter sur processeur les tests rapides de compatibilité structurelle sans fuite lexicale contre un nul de surface (`IDE-2026-11-23-027` sur PubTator 3 et `IDE-2026-11-23-028` bras A/C sur Gu et Krenn 2026, puis `IDE-2026-11-23-032` avant Fomin et Zelevinsky). Issue réfutante : si le score structurel sans étiquette ne bat pas le meilleur prédicteur de surface et le modèle nul de Maslov-Sneppen (`rapport de cotes < 1,2` ou gain d'aire sous courbe `< 0,02`), l'opérateur d'alignement est recalé avant le dégel.
   - *Duel 2 (`C2`, scission conceptuelle)* : tester rétrospectivement l'opérateur de faisceau cellulaire / séparation en sous-rôles (`T5`) pour détecter des scissions conceptuelles connues avant publication contre des témoins polysémiques banals, puis tester le même détecteur d'incompatibilité sur des traces synthétiques mêlant « conscience d'évaluation » et « intention de saboter ». Issue réfutante : si le taux de faux positifs sur polysémie banale égale ou dépasse la détection sur scissions réelles, l'opérateur est réformé.
   - *Duel 3 (`C3`, signaux ex ante sur l'alignement)* : sur un corpus public de prépublications en sûreté et interprétabilité gelé à `t0 = 2024`, mesurer si les cinq signaux sémantiques prédisent les regroupements conceptuels ou nouveaux formalismes apparus en `2025-2026` au-dessus d'un modèle nul de fréquence lexicale et d'âge des concepts.
   - *Garde `C1`* : coder et éprouver (sur un cas sain et un artefact, `R5`) le séparateur de strates (`F_org` / `F_ecart` / `F_final`) et l'audit sur traits de présentation seuls sur le générateur de mondes plantés.
2. **Phase suivante (sur devis approuvé et après franchissement des portes actives du programme) — Activer `C4`, `C6` et `C8` :**
   - Ouvrir le banc de recherche à vérité plantée (`C4`, suite du protocole X déjà voté à `GO-2026-11-21-60`) doté de ses trois témoins « doit mourir » (`N-076` § 4).
   - Soumettre les abstractions candidates issues du cycle Éveil-Sommeil hybride (`C6`) à une épreuve en aveugle contre les agrégateurs de base du programme de contrôle sur la strate `F_ecart` vierge, sous préenregistrement scellé (`R1`, `R2`, `R13`).

---

## 6. Limites, risques résiduels et questions ouvertes à porter au collisionneur

1. **Frontière de `kappa` (couverture des mondes plantés).** Aucun monde planté écrit par nous ou par un modèle de langage ne garantit que `kappa = 1` : une classe d'évasion totalement imprévue en déploiement réel reste hors de `kappa`, ce qui impose de conserver le plancher d'audit au hasard (`N-075`, `N-076`) comme garantie ultime en service et de confiner l'organisme au rôle d'accélérateur de découverte d'invariants.
2. **Risque d'étanchéité temporelle dans `C3` et `C6`.** Dès qu'un grand modèle de langage participe à la détection sémantique (`C3`) ou à la proposition d'abstractions (`C6`), la contamination par mémorisation de son pré-entraînement sur des résultats déjà publiés constitue le biais le plus grave. Ce point est déjà noté pour confrontation au collisionneur (`IDE-2026-11-23-044`).
3. **Coût réel de la strate `F_ecart`.** La règle de lecture unique par cycle (`N-062`) impose de produire régulièrement de nouvelles familles de sabotage indépendantes en quarantaine (`C8`). Le compromis optimal entre le budget alloué à la reconception de l'organisme (`F_org`) et le budget consommé par la fabrication de nouvelles familles d'épreuve (`F_ecart`) reste à chiffrer sur devis réel une fois `C4` spécifié.
