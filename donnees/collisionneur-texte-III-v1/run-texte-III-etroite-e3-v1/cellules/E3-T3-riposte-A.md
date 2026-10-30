# Proposition A — Tour III.3 (réponse aux critiques)

Statuts : tout calcul issu du fait 17 reste « calcul refait sur données RAPPORTÉ » ; les seuils et tailles de simulation sont illustratifs. Je ne réponds qu'aux critiques qui visent A (B §A, C §A, D §A, et la note transversale de B).

## (a) Sort de chaque critique

| # | Critique (auteur) | Sort | Raison ou test |
|---|---|---|---|
| 1 | Affectation des recaptures : chemin non documenté, déviances divergentes au centième (B a1) | **Acceptée**, documentée ci-dessous | N̂₀ = 39,22 (racine de (1−22/N)(1−23/N)(1−27/N) = 1−37/N) ; p̂_s = 22/39,22 ; 23/39,22 ; 27/39,22. Effectifs attendus : m₁₁₁ = 8,88 ; m₁₁₀ = 4,02 ; m₁₀₁ = 6,26 ; m₀₁₁ = 6,95 ; m₁₀₀ = 2,84 ; m₀₁₀ = 3,15 ; m₀₀₁ = 4,90 ; m₀₀₀ = 2,22. G² = 2 Σ n ln(n/m) sur les sept cellules observées : affectation « paire (23, 27) porte 17 » → 12,85 ; « paire (22, 27) » → 13,35 ; « paire (22, 23) » → 14,63. Les écarts entre propositions (≤ 0,05) sont dix fois plus petits que l'écart entre affectations (≥ 0,5) ; la déduction tient si « déviance » désigne G². Un tiers recalcule avec cette table. |
| 2 | Substitution de n_eff = n/(1+(n−1)ρ) dans la borne à zéro échec : correction de variance, pas de probabilité de queue ; « plafond 1/ρ » faux hors échangeabilité (B a2, C a3, D a3) | **Acceptée** | Retirée. Remplacée par le calcul direct de P(zéro échec) sous la loi jointe déclarée (bloc 2 corrigé). Sous Beta-binomiale échangeable, il n'y a pas de plafond mais une décroissance polynomiale, ce qui change le chiffre, pas la conclusion (ρ à déclarer). |
| 3 | Duel 2 : le lien entre écart vues/écart et part d'échec non découverte passe par la seule forme paramétrique de γ ; deux copules à γ égal divergent (B a3, D a1) | **Transformée en test** | Le duel 2 corrigé fait varier la copule à γ fixé ; il mesure explicitement une statistique calculée sur des familles découvertes contre une quantité définie sur les non découvertes, ce qui est la question posée à l'option 2, non un confondant. |
| 4 | Modèle saturé : non-identifiabilité sous u₁₂₃ ≠ 0, pas un biais (B a4) ; aucun monde u₁₂₃ ≠ 0 (note transversale B) | **Acceptée** | Le saturé sort de la liste des estimateurs notés ; il devient diagnostic. Un facteur u₁₂₃ ∈ {−0,5 ; 0 ; +0,5} (illustratif) entre dans le plan ; sous u₁₂₃ ≠ 0 la mesure est l'erreur d'extrapolation de tous les modèles log-linéaires, nommée comme telle. |
| 5 | Nomenclature Chao2 / Chao1 (B a5) | **Acceptée** | Notation fixée : N̂_Chao-inc = S_obs + ((T−1)/T) f₁²/(2f₂) et N̂_Chao-inc-c = S_obs + ((T−1)/T) f₁(f₁−1)/(2(f₂+1)), T = 3 (Chao, 1987, « Estimating the population size for capture-recapture data with unequal catchability », *Biometrics*). |
| 6 | Duel 1 : σ et τ varient ensemble ; b_f partagé = hétérogénéité pure (Rasch), cas pour lequel la borne de Chao est construite ; la cellule σ = 0, τ > 0 manque (B b1, C a1, C c1) | **Acceptée**, duel réécrit | Facteurs séparés : σ (hétérogénéité, indépendance conditionnelle) et θ_{st|f} (rapport de cotes conditionnel de paire, D et C). La validité de la borne est mesurée dans chaque cellule, non présumée. |
| 7 | « Chao2 reste une borne basse sous dépendance positive » est trop général ; sous covariance conditionnelle positive, E[N̂] < N (C b1, D b) | **Acceptée** | Phrase corrigée : borne inférieure en espérance sous hétérogénéité à indépendance conditionnelle ; sous dépendance résiduelle de paire, aucune garantie. La condition de C (covariance conditionnelle moyenne > Var(p̄_f)/3) devient le seuil de H_B du duel 1. |
| 8 | Duel 1 : zone sans verdict entre 0,80 et 0,90 ; N = 40 trivial ; erreur Monte-Carlo (B b1, D a1) | **Acceptée** | Un seul seuil (0,90) ; 10 000 mondes dans les cellules proches du seuil ; largeur médiane des intervalles rapportée, une cellule où elle dépasse N/2 est déclarée non jugeable, pas gagnée. |
| 9 | Duel 3 : biais sur N̂ contre biais sur Ĉ, estimands non commensurables (D a2) | **Acceptée** | Estimand commun N ; comparaison N̂_Chao-inc-c contre N̂_GT = S_obs/Ĉ, même métrique. |
| 10 | Instrument 2 à γ = 0,6 et ρ = 0,20 : les deux règles échouent, non informatif (B b2) | **Acceptée** | Ces cellules documentent la frontière d'applicabilité ; elles ne comptent pas dans le duel. |
| 11 | Bloc 4, définition : puissance de « ≥ 6 échecs sur 25 » non donnée, ≈ 0,15 contre p = 0,15 (B b3) | **Acceptée** | Prédiction scellée avec son alternative déclarée et sa puissance (bloc 4 corrigé). |
| 12 | Bloc 4, familles inconnues : f₁/n prédit la nouveauté sous la loi de capture interne, pas sous une source extérieure indépendante ; Cov(p_int, p_ext) confond (C a2, D b) | **Acceptée** | Deux prédictions scellées sous deux lois extérieures déclarées ; la prédiction uniforme est unilatérale, car N̂ est une borne. |
| 13 | Bloc 4, nombre nécessaire : ρ̂ sur indicateurs binaires d'échec à m = 25 est instable ou indéfini (C b3) | **Acceptée**, transformée | La corrélation intra-grappe est estimée sur la statistique continue S(f) (option 4), définie sans échec. |
| 14 | Zone grise de classement : masse de Beta(a,b) près de τ_θ > ε fait perdre la couverture (C b2) | **Transformée en test** | Zone d'indifférence η déclarée : l'énoncé certifié porte sur les familles avec θ_f ≥ τ_θ + η ; la puissance 0,9 est exigée à τ_θ + η ; un monde avec masse concentrée dans [τ_θ, τ_θ + η] entre dans la sensibilité. |
| 15 | Contrôle négatif θ_f = τ_θ − ξ pour toute f : la règle « premier échec arrête » rejette une défense conforme avec probabilité → 1 (C c2) | **Acceptée** | Le classement d'une famille en échec est un test de niveau α_fam déclaré, et le nombre d'échecs déclarés attendu sous π = 0 (n α_fam) est soustrait avant d'appliquer la règle à zéro échec ; le contrôle mesure le taux de refus de certification sous π = 0. |
| 16 | Règle séquentielle : aucun monde à π = ε pour calibrer (B c2, D c2) | **Acceptée** | Monde frontière π = ε avec lectures répétées selon la règle ; taux de certification exigé ≤ α. |
| 17 | Simulateur d'appariement non contrôlé (B c1) | **Acceptée** | Taux réalisés de fusions et scissions comparés à φ, ψ sur les identités vraies, indépendamment de tout estimateur. |
| 18 | Censure commune : noter contre N total fait échouer par construction ; estimand = N_accessible (D a4, D c1) | **Acceptée** | Notation contre N_acc = (1−κ)N ; κ rapporté comme non identifié. |
| 19 | Calibration des totaux à N = 50 hors grille (D a4) | **Acceptée** | Calibration par probabilités marginales de capture par source (0,56 ; 0,59 ; 0,69 ; calcul refait, données RAPPORTÉ), constantes sur la grille de N. |
| 20 | Base à battre : [S_obs, +∞) couvre avec probabilité 1, pas « nulle » (D a5) | **Acceptée** | Critère corrigé : un estimateur bat la base si sa borne inférieure L vérifie P(L ≤ N_acc) ≥ 0,95 **et** E[L] > E[S_obs] ; pour les estimations ponctuelles, |biais| < |E[S_obs] − N_acc|. Sous scissions, S_obs peut dépasser N, et sa « couverture » est mesurée, non posée. |
| 21 | Contrôle de capture complète : f₂ = 0 et formules indéfinies ; f₁ = 0 ne prouve pas la complétude (D c4) | **Acceptée** | Le monde complet est défini par construction (p_s = 1) ; les estimateurs indéfinis à f₂ = 0 sont notés « indéfini », pas « correct » ; la version corrigée est définie à f₂ = 0. |
| 22 | Contrôle de transport extérieur (D c3) | **Acceptée** | Deux lois extérieures simulées : identique (calibration) et repondérée (non-transportabilité), cette dernière non comptée contre l'estimateur. |

Aucune critique rejetée : chacune désignait une condition sous laquelle une garantie annoncée n'était pas démontrée.

## (b) Expériences corrigées

### Duel 1 — validité de la borne de Chao sous hétérogénéité contre sous dépendance de paire

Mondes : N ∈ {40, 60, 100} ; p_fs = logit⁻¹(a_s + b_f), b_f ~ N(0, σ²), σ ∈ {0 ; 0,5 ; 1 ; 1,5} ; rapport de cotes conditionnel de paire θ_{st|f} ∈ {1 ; 2 ; 4} (illustratif), identique pour les trois paires ; u₁₂₃ ∈ {−0,5 ; 0 ; +0,5} sur l'échelle log-linéaire. Cellules clés : (σ > 0, θ = 1) et (σ = 0, θ > 1).
H_A : dans toute cellule à θ = 1, P(L_Chao ≤ N_acc) ≥ 0,95 et la couverture de M₀ tombe sous 0,90 dès σ ≥ 1.
H_B : il existe une cellule à θ = 1 où P(L_Chao ≤ N_acc) < 0,95, ou bien M₀ garde une couverture ≥ 0,90 à σ ≥ 1.
Exclusives et exhaustives par construction (négation). Contrôle négatif : σ = 0, θ = 1, u₁₂₃ = 0 : M₀ à 0,95 ± 0,01, sinon le simulateur est en cause. Résultat attendu aux cellules θ > 1, rapporté séparément : la cellule minimale (θ, σ) où P(L_Chao ≤ N_acc) < 0,95 fixe la condition de C (ligne 7) comme limite d'emploi de l'estimateur retenu. Lectures : 10 000 mondes près des seuils, 2 000 ailleurs.

### Duel 2 — l'écart vues / tenues à l'écart renseigne-t-il sur les non découvertes ?

Mondes : loi jointe de (logit p_capture, logit(1−θ_f)) avec corrélation γ ∈ {0 ; 0,3 ; 0,6} et copule ∈ {gaussienne, Clayton, Gumbel} à γ égal ; séparation vues / tenues à l'écart par tirage uniforme parmi les découvertes.
Statistique : Q = P(part d'échec parmi les non découvertes > 2ε | écart < δ), δ = 0,05.
H_A : max sur les copules de Q < 0,20 à γ = 0,3.
H_B : ce maximum ≥ 0,20.
Contrôle négatif : γ = 0, toute copule : Q ≈ P(part > 2ε) sans conditionnement, à ± 0,02. H_B confirmée disqualifie l'option 2 comme preuve ; H_A confirmée la garde comme diagnostic, sous la copule la plus défavorable de l'ensemble déclaré, jamais au-delà.

### Duel 3 — robustesse aux scissions à tort, estimand commun N

Mondes : ψ ∈ {0 ; 0,05 ; 0,10}, φ idem, N = 60, σ = 0,5, θ = 1 ; taux réalisés vérifiés contre identités vraies (ligne 17).
H_A : biais relatif médian de N̂_Chao-inc-c sur N à ψ = 0,10 < +20 %.
H_B : ≥ +20 %.
Rapporté en parallèle, même métrique : N̂_GT. Contrôle négatif : ψ = φ = 0, biais de référence du duel 1 retrouvé.

### Instrument 2 corrigé et règle du nombre de familles

Mondes : θ_f ~ Beta(a, b) incluant une variante à masse concentrée dans [τ_θ, τ_θ + η] ; m_e ∈ {20, 50, 200} ; échecs corrélés entre familles soit par loi Beta-binomiale échangeable d'ICC ρ ∈ {0 ; 0,02 ; 0,05 ; 0,10 ; 0,20}, soit par grappes de taille g ∈ {2, 5, 10} à corrélation intra-grappe ρ ; sélection γ.
Règle de calcul : n est le plus petit entier tel que P(zéro échec déclaré | π = ε) ≤ α, calculé sous la loi jointe déclarée. Sous indépendance : fait 9 (29 pour ε = 0,10). Sous Beta-binomiale, P = ∏_{i=0}^{n−1} (b+i)/(a+b+i) avec a = ε(1−ρ)/ρ, b = (1−ε)(1−ρ)/ρ : ρ = 0,02 → n ≈ 40 ; ρ = 0,20 → n ≈ 6 000 (illustratifs, calcul refaisable). Sous grappes, par simulation. Le classement par famille est un test de niveau α_fam avec zone d'indifférence η ; n α_fam échecs déclarés attendus sous π = 0 sont tolérés.
Contrôles négatifs : (i) θ_f = τ_θ − 0,005 pour toute f, m_e = 20 : taux de refus de certification mesuré ; (ii) π = ε avec lectures séquentielles répétées : taux de certification ≤ α ; (iii) ρ = γ = 0, m_e → grand : coïncidence avec Clopper-Pearson.
Base à battre : proportion observée d'échecs, intervalle de Clopper-Pearson ignorant grappes et niveau élément.

### Instrument 1 corrigé

Estimateurs notés : S_obs (base, critère de la ligne 20), M₀, modèles à une et deux interactions, Chao-inc et Chao-inc-c, N̂_GT, ICE, bayésien à effet latent (prior déclaré). Saturé : diagnostic seul. Estimand : N_acc. Facteurs : N, σ, θ_{st|f}, u₁₂₃, φ, ψ, κ ∈ {0 ; 0,10 ; 0,30}. Contrôles : capture complète par construction ; indépendance homogène ; taux d'appariement réalisés.

## (c) Réponse à l'arbitre, en une page

**Ce qui est établi.** L'objectif d'universalité sur familles inédites (fait 1, VÉRIFIÉ). La borne à zéro échec sous tirage indépendant (fait 9, VÉRIFIÉ). La cohérence arithmétique des comptes (fait 18, VÉRIFIÉ). Par calcul refait sur données RAPPORTÉ : la déviance 12,9 n'est compatible qu'avec l'affectation où la paire (source de 23, source de 27) porte 17 recaptures, d'où les cellules 4, 4, 8, 2, 2, 3, 14 (table des attendus en (a), ligne 1), si « déviance » désigne G².

**Ce qui ne l'est pas.** Le décompte et l'appariement (lecteur unique). La fermeture de la population. L'absence de censure commune, non identifiable de l'intérieur. L'absence de dépendance résiduelle de paire entre sources : avec sept cellules, hétérogénéité latente et dépendance de paire ne sont pas séparables, et u₁₂₃ = 0 est posé par tout modèle identifiable, jamais testé. La loi sur la classe K et la corrélation ρ des échecs entre familles. Que les familles découvertes se comportent comme des familles tirées pour la part d'échec.

**Définition retenue.** Quantificateur : « pour au moins une part 1 − ε de K, avec confiance 1 − α » ; classe : K déclarée par son schéma de construction, avec la loi de découverte et la structure de corrélation (ρ, grappes) déclarées ; statistique : S(f) au niveau famille, estimée sur m_e éléments, famille en échec si S(f) < τ hors zone d'indifférence η. Rapport obligatoire du minimum observé (option 1) ; l'écart vues / tenues à l'écart (option 2) est un diagnostic de sélection, jamais une preuve (duel 2). « Robuste à l'inconnu » n'est pas un énoncé sur K et ne s'atteint que par l'extérieur.

**Estimateur retenu.** N̂_Chao-inc-c = 37 + (2/3)·16·15/(2·8) = 47,0 ; version classique 49,2 ; borne inférieure unilatérale à 95 % ≈ 41 (variance de Chao 1987, log-normale ; intervalle bilatéral ≈ [41 ; 78]) ; Good-Turing Ĉ = 1 − 16/72 = 0,778, N̂_GT = 47,6 ; M₀ = 39,2, rejeté. Tous : calcul refait sur données RAPPORTÉ. Garantie : borne inférieure en espérance sous hétérogénéité à indépendance conditionnelle ; perdue sous dépendance résiduelle de paire ; borne supérieure non identifiée (39 à 186 selon le modèle). Sous censure, l'estimand est N_accessible.

**Nombre de familles et règle.** n = plus petit entier tel que P(zéro échec déclaré | π = ε) ≤ α sous la loi jointe déclarée : 29 sous indépendance (fait 9) ; ≈ 40 sous Beta-binomiale échangeable à ρ = 0,02 ; ≈ 6 000 à ρ = 0,20 (illustratifs) ; sous grappes, par simulation. La garantie reste conditionnelle au mécanisme de découverte (γ) et à la correction des échecs masqués (α_fam, η, m_e).

**Validation extérieure.** (1) Définition : m = 70 familles extérieures (illustratif) ; prédiction scellée « ≤ 10 % d'échec » ; ≥ 12 échecs falsifie ; puissance ≈ 0,8 contre p = 0,20, ≈ 0,15 contre 0,15 à m = 25 (illustratifs). (2) Nombre : corrélation intra-grappe de S(f) continue sur les familles extérieures ; falsifiée si sa borne inférieure à 95 % dépasse le ρ_S déclaré. (3) Inconnues, deux lois scellées : loi extérieure semblable à la loi interne → part nouvelle ≈ 0,22, falsifiée hors [0,10 ; 0,40] ; tirage uniforme sur K → part nouvelle ≥ 1 − 37/47 ≈ 0,21, prédiction unilatérale, falsifiée seulement par ≤ 1 nouvelle sur 25 (illustratif). (4) Un excès de nouvelles ne falsifie pas la borne, il falsifie son emploi ponctuel. (5) Cov(p_int, p_ext) reste un confondant déclaré : le test porte sur l'estimateur et le transport ensemble.

**Expérience à faire en premier :** le duel 1 corrigé, cellules (σ > 0, θ = 1) contre (σ = 0, θ > 1), parce qu'il décide si l'estimateur retenu est une borne inférieure utilisable ou non, avant tout calcul de nombre de familles.

FIN-DE-CELLULE