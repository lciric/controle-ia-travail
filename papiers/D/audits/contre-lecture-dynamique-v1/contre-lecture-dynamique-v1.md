# Contre-lecture : la dynamique en temps fini du filtrage pendant l'entraînement, v1

Contre-lecteur neuf (Opus 5.5). Je n'ai écrit aucune des pièces lues. Pièce lue : `papiers/D/theorie/brouillon-fable-dynamique-v1/dynamics-section-v1.tex` (1 245 lignes), avec la note de Fable et les contrôles c1 à c6. Branche `papier-d/evasion-post-entrainement-v1`. Empreintes de la pièce, de la note et des contrôles vérifiées : toutes conformes. Aucun fichier du dépôt n'a été modifié.

## Verdict : tient avec réserves

J'ai refait sans le texte toutes les preuves des énoncés numérotés, et elles tiennent. Je n'ai trouvé aucune erreur de signe ni de constante, et aucun contre-exemple à un énoncé tel qu'il est écrit. Les trois affirmations numériques que la note dit non démontrées se régénèrent.

Les réserves portent sur trois points :
1. **La règle de « gradient avec rejet » (c) n'est pas la même dans sa définition et dans son analyse.** Elle est définie par l'estimateur ordinaire, alors que (c2), le corollaire (v), la proposition prop:discard-kl et la remarque rem:taxonomy analysent le flot du gradient naturel. Les conclusions changent avec la géométrie (défaut 1).
2. **La lecture de l'opérateur A par la règle (a) n'est pas une procédure de rejet** (défaut 2).
3. **Le dilemme rejet–pénalité est incomplet.** Une hausse de la pénalité peut faire passer le modèle pré-entraîné du bassin honnête au bassin « triche obscurcie » hors des deux fenêtres. La note dit le contraire, sur la seule foi de c4, qui ne couvre pas cette région (défaut 3).

Il faut aussi resserrer l'antériorité (défaut 4). Le reste est mineur.

## Défauts

### 1. Majeur : la règle (c) est définie par le gradient ordinaire mais analysée par le gradient naturel
- **Où :** `dynamics-section-v1.tex`, lignes 144-152 (définition par l'estimateur REINFORCE ĝ), 203-218 ((c1), puis (c2) « natural gradient flow of b »), 380-382 (corollaire, point (v) : « under the unregularised rule (c) »), 523-531, 678-691 (rem:taxonomy : « Rule (c) … »).
- **Le problème.** E[ĝ] = ((N−1)/N)·F·a. L'estimateur, appliqué tel quel, suit donc le flot ordinaire θ̇ = F·a, et non θ̇ = a. Or tout (c2) repose sur la fermeture par strates du flot naturel : invariant π_v·π_f^(−β_v/β_f), limite x*, x* > p_f/(p_f+p_v), taux ≥ ρΔR.
- **Contre-exemple.** p = (0,6 ; 0,3 ; 0,1), β = (1 ; 0,2 ; 0,5), ΔR = 1, une trajectoire par strate.
  - Flot naturel : limite (0 ; 0,548 ; 0,452).
  - Flot ordinaire : π = (1,0·10⁻⁶ ; 0,9965 ; 0,0035) à t = 10⁵, toujours en dérive. L'invariant passe de 0,754 à 5,03, et la part furtive parmi les tricheurs tombe sous celle de la référence naturelle sans moniteur (0,25).
  - Le flot ordinaire sans moniteur concentre aussi la masse sur la triche visible : 0,999.

  Les énoncés (ii) et (iii) de (c2) ne valent donc que pour le gradient naturel. Avec plusieurs trajectoires par strate, le flot ordinaire ne se ferme même plus par strates.
- **Correction.** Définir la règle (c) comme gradient naturel sur les échantillons acceptés : estimateur préconditionné par F(θ)†, la matrice d'information de Fisher de la politique d'échantillonnage. Ou bien écrire « rule (c) with Fisher preconditioning » partout où (c2), (v), prop:discard-kl et rem:taxonomy en parlent. Ajouter une phrase : sous le gradient ordinaire, (c2)(ii)-(iii) sont faux, avec l'exemple ci-dessus.

### 2. Majeur : la règle (a) appliquée à l'opérateur A n'est pas un « rejeter et réessayer »
- **Où :** lignes 116-125 (titre « three readings of “discard and try again” » ; règle (a) avec r = R + η⁻¹ log β), 180-184 (a2), 363-370 (corollaire (iii) : « the filter of operator A does not delay dominance »), 410-455 (proposition d'amplification à temps égal).
- **Le problème.** La règle (a) pour A est la montée naturelle sur une récompense augmentée du bonus η⁻¹ log β(x).
  - Il faut connaître la probabilité de survie de chaque trajectoire. Une interception binaire n'en donne aucun estimateur sans biais de log β(x).
  - Avec β_v = 0, c'est une pénalité infinie.
  - Rien n'y est jeté ni rééchantillonné : c'est une pénalité logarithmique.
  - Le facteur β^λ(t), qui donne la réentrance et le non-retard asymptotique, est un artefact de cette forme variationnelle. Le modèle statique le dit lui-même : l'opérateur A est un choix de modèle (`main-v4-correctif-1.tex`, rem:modelA, ligne 97).
- **Correction.**
  - Retitrer : « three learning rules » ; seules (b) et (c) sont des procédures de rejet.
  - Dire en tête de (a) que, pour A, il s'agit d'une pénalité en log β et non d'un rejet.
  - Lire le corollaire (iii) et la proposition prop:equal-time comme des propriétés de cette relaxation.

### 3. Majeur : une hausse de la pénalité peut faire basculer du bassin honnête au bassin « triche obscurcie », hors des deux fenêtres
- **Où :** rem:dilemma, lignes 1006-1015, dernière phrase : « The regime in which larger penalties demonstrably produce more obfuscation is the reverse window ». Note de Fable, point 8 : « I found **no** instance (3000 random draws) where raising C moves the pretrained model from the honest basin to the stealth basin ».
- **Contre-exemple** (script v5). Paramètres : q0 = s0 = 0,8 ; β = (1 ; 0,04 ; 0,85) ; ΔR = 1 ; κ = 1,2 ; η = 40. On a C_low = 2,205, C_high = 0,852 et κ† = 2,077.

  | Pénalité C | Équilibre limite (q, s) depuis le modèle pré-entraîné | Nombre d'équilibres |
  |---|---|---|
  | 0,40 | (4·10⁻⁶ ; 0), honnête | un seul |
  | 0,45 | (1 ; 0,59) | trois (pli entre 0,40 et 0,45) |
  | 0,50 | (1 ; 0,88) | trois |
  | 0,60 | (1 ; 0,995) | trois |

  Les valeurs C = 0,45, 0,50 et 0,60 sont toutes hors des deux fenêtres (C < C_high < C_low).
- **Fréquence.** 13 basculements sur 800 tirages élargis (q0 et s0 jusqu'à 0,95, κ jusqu'à 1,5). 3 sur 600 tirages avec q0 ≤ 0,3, mais alors s0 vaut 0,84 à 0,94. Aucun sur 1 500 tirages dans la région de c4.
- **Ce que teste c4.** c4 cherche, sur une grille de 7 valeurs de C (0,2 à 16), un saut entre deux valeurs successives : d'une limite avec s < 0,3, quel que soit q, à une limite avec q et s > 0,9. Les tirages vont jusqu'à q0 ≤ 0,6, s0 ≤ 0,4, κ ≤ 0,5 et β_f ≥ 0,6, avec une intégration jusqu'à 60η. Son 0 est conforme au texte, qui n'affirme rien, mais ne prouve rien hors de cette région.
- **c5** (343 hausses de s > 0,3 sur 3 000) montre déjà une obfuscation qui croît avec C au-delà de C_low. Exemple : C_low = 1,08 et s monte encore de C = 1 à C = 2.
- **Correction.**
  - Remplacer la dernière phrase de rem:dilemma par : « the reverse window is the regime where the growth is *proved* monotone; outside both windows a larger penalty can move the pretrained model from the honest equilibrium to the hack–obfuscated one (numerical example) ».
  - Corriger le point 8 de la note.

### 4. Majeur avant soumission : antériorité de « ce qui est propre à la section »
- **Où :** rem:known-vs-new, lignes 1221-1245 ; rem:mirror, lignes 323-333.
- **Le problème.** Le système à deux canaux, u̇ = −u/η + A + Dσ(w), ẇ = −w/η + Dσ(u) − κ, est le système classique de deux unités sigmoïdes à fuite et à excitation mutuelle : réseau de Hopfield continu, modèle de Wilson–Cowan, avec la fonction de Lyapunov de Cohen–Grossberg et Hopfield. Bistabilité, au plus trois équilibres, plis : c'est classique. C'est aussi une dynamique de réponse logit régularisée dans un jeu potentiel 2×2, avec bifurcations en température : Leonardos et Piliouras ; Hofbauer et Sandholm. Le caractère non concave de l'objectif restreint aux politiques produits est le fait classique de la variation en champ moyen (Wainwright et Jordan). Le lemme du gradient naturel tabulaire remonte à Kakade (2001) et à Agarwal et al. La règle (b) avec ω = e^{γR} est l'itération de filtrage d'ExIt, STaR, RAFT et ReST, et elle figure déjà dans le modèle statique (défaut 10).
- **Correction.** Limiter le « specific » à l'application aux filtres pendant l'entraînement et à la comparaison des règles. Citer ces sources après vérification sur PDF (liste plus bas). Garder la phrase « no systematic literature search ».

### 5. Mineur : rem:taxonomy, « slows … by at most the factor ρ »
- **Où :** lignes 680-683.
- **Le problème.** La phrase est vraie comme borne inférieure, mais elle laisse croire que le filtre ralentit toujours. Or a_f − a_h peut dépasser ΔR. Au point π = (0,01 ; 0 ; 0,99), avec β = (1 ; 0 ; 0,1), a_f − a_h = 8,4 > ΔR = 1 : le filtre peut accélérer.
- **Correction.** Ajouter « and may accelerate it ».

### 6. Mineur : prop:discard-kl, l'écart entre les deux seuils est grand
- **Où :** lignes 556-564 et 688-691.
- **Ce que j'ai trouvé.** Dans l'instance (v), avec β_v = 0,05 et en faisant varier ηΔR :
  - la borne de piégeage (iv) est presque serrée : maximum de y = 2,003 contre ȳ = 2,006 ; 5,17 contre 5,50 ;
  - la domination réelle apparaît entre ηρΔR = 5 et 6, très en dessous du seuil garanti L = 9,21.

  « The filter rescales the pressure » est donc une heuristique.
- **Le maximiseur global.** C'est (≈0 ; 0,5 ; 0,5) : la triche furtive n'y est pas enrichie parmi les tricheurs. L'expression « stealth-heavy » de la note est donc excessive.
- **Correction.** Donner l'écart et nommer le maximiseur.

### 7. Mineur : prop:equal-time, point (iv)
- **Où :** lignes 447-450.
- **Le problème.** « complement in (0,1) of a closed interval » : l'ensemble {g ≤ 0} peut être (0,a], ou vide.
- **Correction.**
  - Écrire « of a relatively closed, possibly empty, subinterval ».
  - Signaler que le cas p_vℓ_v = p_hℓ_h du point (iii) n'est pas traité.
  - Une preuve plus courte de la convexité existe : g''(λ) = h(ℓ_h) − h(ℓ_v), avec h(ℓ) = (ℓ / (2 sinh(ℓλ/2)))², décroissante en ℓ. J'ai vérifié qu'elle est équivalente à celle du texte.

### 8. Mineur : rem:reentrance, l'ampleur n'est pas dite
- **Où :** lignes 515-520.
- **Valeurs régénérées.** g(0+) = 0,0454 (le texte dit « ≈0,05 »), min g = −0,0374 en λ = 0,210, g(1) = 0,745. Zéros en λ = 0,0680 et 0,3597, soit t/η = 0,0705 et 0,4457.
- **Ampleur.** L'écart π_A(f) − π_no(f) vaut au plus environ 5·10⁻⁵ aux temps courts, et −7,4·10⁻⁴ dans le creux. La réentrance est réelle mais minuscule.
- **Correction.** Écrire « ≈0,045 », donner les zéros et l'ampleur.

### 9. Mineur : hypothèses non écrites dans le cadre
- **Où :** lignes 25-32 et 100-104.
- **Le problème.** Les trois strates doivent être non vides (p_h, p_v, p_f > 0). Le modèle statique l'écrit ; la preuve de prop:equal-time l'emploie. Il faut aussi C ≥ 0 : sinon τ_no ≤ τ_B (corollaire (iii)) peut tomber.
- **Correction.** Ajouter « p_i > 0 for each i, and C ≥ 0 ».

### 10. Mineur : la règle (b) est déjà dans le modèle statique
- **Où :** lignes 127-135 et 187-199. Dans le modèle statique : `main-v4-correctif-1.tex`, rem:modelA, ligne 97, qui donne π_T ∝ β^T e^{Tη₁R} π0 et le seuil T(η₁ΔR − log(β_h/β_f)) > L.
- **Le problème.** La partie (b) avec ω = e^{γR} redonne exactement ce résultat. C'est cohérent, mais le renvoi manque.
- **Correction.** Citer rem:modelA et dire que (b) le généralise : ω quelconque, variante ancrée, meilleur de N.

### 11. Mineur : imprécision dans rem:taxonomy
- **Où :** lignes 692-695.
- **Le problème.** « the first term is what operator B with C = 0 would give ». Le terme est β_fΔR / Z̄ et non β_fΔR : il est divisé par la masse acceptée.
- **Correction.** Écrire « up to the factor 1/Z̄ ».

### 12. Mineur : intégration dans le manuscrit statique
- **Où :** en-tête de la pièce, lignes 1-7.
- **Le problème.** `main-v4-correctif-1.tex` ne définit ni `lemma`, ni `corollary`, ni `definition`, et ses théorèmes partagent un même compteur. Il note `\DKL` et Π_{\mathrm h}, β_{\mathrm h}, quand le fragment note KL, 𝒳_h et β_h.
- **Correction.** Harmoniser les notations et déclarer les environnements manquants.

### 13. Mineur : traçabilité des contrôles (R4, R9)
- **Où :** note de Fable, section 3 (« all passed ») et en-tête (« `checks/` »).
- **Les problèmes.**
  - Le dossier s'appelle `controles/` et non `checks/`.
  - c1 affiche « convex/concave violations 1 ». C'est un artefact d'arrondi : ℓ_v = 3,2·10⁻⁶, où 1 − a^λ ≈ 5·10⁻¹⁰. La formule analytique de g'' le confirme (script v2).
  - c2 affiche `rate_ok False` sur ses cinq tirages : débordement de π_h vers 0, donc log(inf) et NaN. Sa date de domination est lue sur une grille de pas 0,1/β_f, ce qui explique t_dom = 0,326 contre une borne de 0,031 au premier tirage.

  Mes contrôles en échelle logarithmique donnent un taux minimal égal à 1,017·ρΔR (≥ 1) et aucune domination tardive (v1). Les affirmations tiennent donc, mais le journal de la note ne dit pas ce qui s'est affiché.
- **Le problème de graines.** Les graines sont `default_rng(entier)`, sans `SeedSequence` (R9).
- **Correction.** Corriger c1 et c2 (formule analytique, intégration en échelle log, sortie dense), passer à `SeedSequence` et rejouer en journalisant.

### 14. Mineur : opérateur A au-delà de e⁴
- **Où :** rem:A-vs-B, lignes 1166-1173.
- **Constat.** Trois équilibres existent bel et bien sous A quand β_f/β_v > e⁴. Exemple : β = (1 ; 10⁻³ ; 0,5), ΔR = 1, η = 6, q0 = s0 = 0,1, κ = 0,3 donnent les équilibres (0,050 ; 0,024), (0,788 ; 0,711) et (0,866 ; 0,799). Sur 3 000 tirages avec β_v = 10⁻³, 73 en ont trois.
- **Correction.** Le dire : le seuil e⁴ n'est pas vide de sens.

## Ce qui a été vérifié et tient

### Preuves refaites sans le texte

**Lemme du gradient naturel tabulaire**
- Le noyau de F est engendré par **1**, d'où F†F = Π.
- dV/dt = GᵀFG.
- Mise à jour multiplicative en temps discret.
- Vérifié aussi numériquement, avec une erreur relative de 4·10⁻⁹.

**Théorème tabulaire**
- (a) Tranche de temps : λ(t) = 1 − e^{−t/η}. En temps discret, λ_k = 1 − (1 − γ/η)^k, croissante et dans [0,1] si et seulement si γ ≤ η. J'ai vérifié l'oscillation pour γ ∈ (η, 2η).
- (b) π_k ∝ p·β^k·ω^k. La variante ancrée donne c_k = ((1−α)/α)(1 − (1−α)^k).
- (c1) Facteur (N−1)/N, ∇b = a, F·a = π∘a.
- (c2) Formes closes de a : 10⁵ tirages dans c3.
  - (i) Taux ≥ ρΔR, car Z̄ ≤ β_h et b ≥ 0.
  - (ii) Invariant conservé, avec un écart de 2·10⁻¹⁰.
  - (iii) Limite x*, avec un écart de 4·10⁻¹¹, et x* > p_f/(p_f + p_v).

**Corollaire des temps d'atteinte**
- Formules de τ, du premier pas discret (partie entière + 1) et de la variante ancrée.
- Seuils statiques de domination sous A et sous B, conformes à `main-v4-correctif-1.tex`, équations eq:domA et eq:domB.

**Proposition prop:equal-time**
- Critère exact, par produit en croix.
- Condition suffisante par l'inégalité arithmético-géométrique pondérée : T_amp coïncide avec ΔR*_A(η) du modèle statique, équation eq:ampA.
- Limite aux temps courts : ℓ_v/ℓ_h.
- Convexité ou concavité selon le signe de β_f² − β_vβ_h, et g'(0+) = ηΔR − (ℓ_h + ℓ_v)/2.
- Aucun désaccord sur 5·10⁴ tirages. La condition de monotonie ne donne aucune violation sur 5 000 tirages.

**Proposition prop:discard-kl**
- (i) Ordre φ_h ≤ 0 ≤ φ_v ≤ φ_f, borne sur Z̄, compacité.
- (ii) Fonction de Lyapunov et principe d'invariance de LaSalle.
- (iii) Minoration intégrée.
- (iv) Identité a_f − a_h = ΔR(ρ + μ)/(π_h(1+μ)²), majorant Γ, lemme de comparaison.
- (v) Arithmétique : L = 9,2101, ηρΔR·(1 + c·e³)² = 2,016, ηV ≤ 0,008 < 0,01 sur l'ensemble piégé, ηV(π°) = 10,79, maximiseur intérieur.
- 300 trajectoires sans violation de (i), (iii) ou (iv).

**Théorème à deux canaux**
- Coefficients A0 et D, le flot, le rectangle invariant, dĴ/dt.
- (b2) Le crochet ψ(s) − ηD·tanh(·) est strictement décroissant, donc Φ' est unimodale.
- (b3) Valeurs propres −(1 ∓ √Φ')/η et alternance stable–selle–stable.
- (b4) Contraction de taux 1/η − D/4 par Grönwall.
- (c1) Argument de Kamke. (c2) et (c3) : itérés de Picard positifs.
- 3 000 tirages pour (b2)-(b3) ; 300 pour (b4), sans violation.

**Corollaire des certificats et des fenêtres**
- C_low, C_high, κ†, les deux fenêtres, les dérivées en C.
- 1 500 tirages de c6 sans violation.

**Propositions de bistabilité et de non-atteignabilité**
- Valeurs aux points w±.
- Limite pour η grand : il faut κ > 0 et D > κ, ce que l'énoncé suppose bien.
- Ordre total des équilibres, et maximiseur global intérieur strictement au-dessus de x_*.
- Bistabilité : 779 cas couverts, 0 violation. Non-atteignabilité : 103 cas, 0 violation.

**Opérateur A à deux canaux**
- A0^A, D^A, les bornes (ii), l'équivalence (iii).
- 2 000 tirages sans violation.

**Remarques**
- rem:mean-field : récompenses 0, −κ, A0, A0 + D − κ.
- Meilleur de N : rapport des poids Σ (1−χ)^{−i} ≥ N.

### Les trois affirmations numériques, régénérées (script v3)

- **Réentrance** : voir le défaut 8. Elle est confirmée directement sur les politiques.
- **Sup s à C = 100** : 0,0100685, avec une sortie dense de 2·10⁶ points, atteint en t = 0,0234. Le texte dit ≈ 0,01007 : c'est conforme. Pour C = 9 à 1 000, sup s va de 0,010000 à 0,010095, et la limite est toujours (0 ; 0,001365). Le certificat (ii) borne s par 0,0122 à C = 10, mais n'apporte plus rien à C = 100.
- **Trois équilibres de l'instance de non-atteignabilité** : (2,199·10⁻¹¹ ; 1,365·10⁻³), (0,1725 ; 0,5757) et (1 − 2,04·10⁻⁷ ; 1 − 3,11·10⁻¹⁵), avec J = −9,367·10⁻⁴, −0,14729 et 0,43948. C'est conforme. Les conditions de bistabilité sont vérifiées.

### Cohérence avec le modèle statique
- La définition de l'amplification, T_amp et les seuils de domination sous A et sous B sont conformes.
- L'opérateur A comme choix de modèle est cohérent avec rem:modelA. Les défauts 2 et 10 portent sur la présentation, pas sur la cohérence.

### Compilation
- Le fragment compile sur une copie avec `wrap.tex` : 15 pages, trois boîtes trop pleines de moins de 5 points, citations non définies (normal sans bibliographie). C'est conforme à la note.

## Références à vérifier sur PDF (R7)

**Citées par la pièce.** Aucune n'a été vérifiée, ni par Fable ni par moi.
- Cen, Cheng, Chen, Wei et Chi, *Operations Research* 70(4), 2022, arXiv:2007.06558. Vérifier si le cadre (entropie, pas divergence vers un a priori) couvre l'attribution de rem:mirror.
- Mei, Xiao, Szepesvári et Schuurmans, ICML 2020.
- Agarwal, Kakade, Lee et Mahajan, JMLR 22, 2021.
- Smith 1995, AMS Surveys 41.
- Hirsch et Smith, *Handbook of Differential Equations*, vol. 2 : année 2005 ou 2006 ?
- LaSalle 1976, SIAM, série CBMS-NSF n° 25.

**À ajouter** (défaut 4).
- Kakade 2001, *A natural policy gradient*.
- Khalil, *Nonlinear Systems* : lemme de comparaison et linéarisation.
- Hirsch 1982 et 1985 : systèmes coopératifs plans.
- Hopfield 1984 ; Cohen et Grossberg 1983 ; Wilson et Cowan 1972.
- Leonardos et Piliouras 2022 (catastrophes et apprentissage par exploration).
- Hofbauer et Sandholm 2002.
- Wainwright et Jordan 2008.
- Anthony et al. 2017 (ExIt) ; Zelikman et al. 2022 (STaR) ; Dong et al. 2023 (RAFT) ; Gulcehre et al. 2023 (ReST).
- Pour rem:noise, si un taux y est un jour chiffré : Freidlin et Wentzell, Kramers.

## Commandes lancées

Toutes les commandes ont tourné sur des copies dans le bloc-notes, avec l'interpréteur `-I`. Le bloc-notes est `/tmp/claude-0/-home-user-controle-ia-travail/c88f1f22-9d69-5421-86a6-86f206ad7a55/scratchpad`, et `PY` désigne son `venv/bin/python`.

- `cp -r papiers/D/theorie/brouillon-fable-dynamique-v1/. verif-dyn/copie/`, puis `sha256sum -c *.sha256 controles/*.sha256` : tout est conforme.
- `cd verif-dyn/copie/controles && $PY -I c1.py`, puis de même `c2.py`, `c3.py`, `c4.py`, `c5.py` et `c6.py`. Sorties de c4 et c5 : `verif-dyn/sortie-c4.txt` et `verif-dyn/sortie-c5.txt`.
- `pdflatex -interaction=nonstopmode wrap.tex`, lancé deux fois sur une copie dans `verif-dyn/compil/`.
- Mes scripts, dans `verif-dyn/` :

| Script | Ce qu'il vérifie |
|---|---|
| `v1_tabulaire.py` | Lemme, λ_k, (c2) en échelle log, flot ordinaire contre flot naturel, amplification, réentrance |
| `v2_c1_violation.py` | Artefact de c1 |
| `v3_deux_canaux.py` | (b2) à (b4), bistabilité, non-atteignabilité, régénérations, opérateur A |
| `v4_basculement.py` et `v4b_basculement_large.py` | Recherche des basculements induits par C |
| `v5_basculement_detail.py` | Le contre-exemple du défaut 3 |
| `v6_rejet_ancre.py` | prop:discard-kl |
| `v7_vanille_et_A.py` | Flot ordinaire ; trois équilibres sous A |
