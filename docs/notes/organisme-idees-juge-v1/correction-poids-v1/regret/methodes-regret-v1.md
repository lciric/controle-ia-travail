# Poids du nul appris en ligne, corrigés par une borne de regret — méthodes étudiées — v1

- **Statut** : mise au point exploratoire, **aucune revendication**. Toutes les issues sont rapportées de la même façon ;
  aucun essai ne visait un signe. Rien n'est adopté : toute adoption est une décision du directeur (section 9).
- **Auteur** : concepteur neuf, sous-agent ; je n'ai écrit aucune des pièces citées.
- **Date** : 2026-11-15 (UTC), dépôt lu sur `main` (tête `e2bef750`), aucun commit.
- **Calcul** : processeur seul, Python 3.13, numpy 2.4.6, scipy 1.17.1, `.venv/bin/python -I -B`, 3 processus. Machine
  partagée (charge de 3 à 10 pendant les essais) : les durées sont indicatives.

## 0. Le verdict en cinq lignes

1. Toute correction par une borne de regret **certifiée** donne un juge valide, mais son dénominateur est, trajectoire par
   trajectoire, **au-dessus du maximum de vraisemblance exact** de la même famille. Elle ne peut donc **jamais** regagner
   de puissance sur le maximum certifié du nul v9 : elle en perd toujours (théorème 2, section 3).
2. Chiffre : la borne du mélange uniforme vaut 19,7 nats (membre linéaire) et 23,5 nats (membre par morceaux) à
   200 tirages, contre un seuil de log 20 = 3,0 nats. Sur le banc, le surcoût médian sur le maximum est de 8 à 15 nats.
3. Taille : les deux méthodes corrigées promeuvent **0** copie sur 1 000 dans chaque cas (0 sur 500 pour la copie coupée
   hors de l'archive avec la structure v9 réduite). Les deux façons des fiches échouent nettement dans le même banc :
   73 % à 100 % de promotions (en ligne sans correction), 10 % à 30 % (moitié).
4. Puissance (vraies découvertes, doses 0,1 ; 0,2 ; 0,35) : le maximum certifié v9 réduit promeut 0,4 % ; 10,0 % ; 55,6 % ;
   le nul limité aux coupures de l'archive 1,4 % ; 18,2 % ; 68,8 % ; les méthodes corrigées 0 % ; 0 % ; 0,2 % au plus.
5. La meilleure correction possible (borne calculée sur les données mêmes, ou correction minimax) **redonne exactement le
   maximum** : on paie deux calculs pour le même verdict. Dans cet angle, il n'y a rien à regagner. La puissance perdue se
   regagne ailleurs : en réduisant la classe (nul limité), ou par une valeur e qui ne domine pas trajectoire par trajectoire
   (section 8).

## 1. Ce que j'ai lu (empreintes recalculées, égales à leurs compagnons `.sha256`)

| pièce | empreinte |
|---|---|
| `docs/notes/organisme-idees-juge-v1/preuve-validite-nul-limite-v1.md` | `44f249409193778ccbaaa12b6c5e74d64434dfb87be77382d8bb9438459281b2` |
| `docs/notes/organisme-idees-juge-v1/prereg-nul-par-morceaux-limite-v1.md` | `46ef2b92119ee5dff05727b90ca8bdd3ba57b52f9c1c75893750c792a2abc089` |
| `docs/notes/organisme-idees-juge-v1/contre-lecture-prereg-nul-limite-et-preuve-v1.md` | `763fc6e29cd80868dcdb1d848eafdc928a39fca7244fa16eb0ac721ec705014e` |
| `docs/notes/organisme-conception-propre-v1/relecture-exploratoire-v2/releve-idees-reutilisables-v1.md` (section 1.1) | `bd253b6c68f6baada0e61b5381f029b52838ca34aa092502e55253c662451c6c` |
| `runs/course-ideation-conception-propre-v1/20261113-235541-course-ideation-conception-propre-v1-g1/copies/sortie--fiches-validees.json` (argon-p1-01 = n° 0, opus-p1-05 = n° 9, fable-p1-05 = n° 13, argon-p2-01 = n° 14) | `a9f9594e2dc3a7a553c54577202817758e3f7ef231445f1a48d500fc647389d5` |
| `docs/verdicts/verdict-validation-nul-v9-v1.md` (seul fichier ouvert de ce dossier) | `1407e460367754bb9f76b37174f3a21585970864eb9beaa2699494d90125c1ea` |

Code lu, **jamais exécuté ni importé** : `copie-nul-v9-a41b7b5/orchestrator/pole/nul_v9.py` (docstring, calcul par lots,
certificat) ; dans `code-organisme-94bfd92/orchestrator/pole/` : `selection_pari.py` (`proba`, `tirer_instances`,
`loi_softmax_aleatoire`, `PLANCHER`, `trajectoire_numerateur`), `nul_filles_v2.py` (`construire_engagement_v2`),
`a_blanc_v59.py` (`juger_carte`). La logique utile est **recopiée en réduit** dans `essai_regret_banc_v1.py` (section 4).

Ce que « puissance perdue » veut dire (verdict, section « Lecture ») : le v9 tient sa taille sur les 18 lignes fatales, mais
sa perte de puissance appariée contre le v8 dépasse la marge de 0,05 sur une ligne (I02 : 0,105 ; intervalle unilatéral
[0,0894 ; 0,1223]). La question est donc : peut-on regagner cette puissance **sans perdre la taille** ?

## 2. Notations (celles du juge)

Plan x_1..x_n (n = 200), x_s = (z_s, g_s) ; instants T = {25, 50, …, 200} ; seuil α = 0,05 ; carte q (loi gelée) ;
tirages frais y_1..y_n après le gel. Richesse log W_t = log q(y_1..t) − D_t ; promotion s'il existe t ∈ T avec
log W_t ≥ log 20. Dénominateur D_t = maximum, sur les membres du nul, de leur valeur à l'instant t. Pour un membre ajusté
de famille Θ (un polytope), ℓ_t(θ) = Σ_{s ≤ t} log p_θ(y_s | x_s) et la valeur du v9 est le **maximum certifié**
V_t = min(0, ℓ_t(u) + écart de Frank-Wolfe en u) ≥ sup_Θ ℓ_t.

Familles (lois connues L_1..L_J, lois certaines δ_1..δ_K) :
- membre linéaire : p_θ(y | x) = Σ_j μ_j L_j(y | x) + Σ_k ρ_k 1[y = k], simplexe de dimension d = J + K − 1 ;
- membre par morceaux sur une partition à C morceaux (coupure de l'archive, seuil d'un trait, sous-population) : μ propre à
  chaque morceau, ρ **commun** ; dimension d = C·(J − 1) + K (`nul_v9.py` : bruit aveugle commun).

Dans les deux cas p_θ(y | x) est **linéaire et positif en θ** : c'est tout ce dont les preuves ont besoin.

## 3. Deux résultats qui gouvernent tout l'angle

**Théorème 1 (validité d'une correction par regret).** Hypothèses : (H1) la famille Θ, la règle d'apprentissage et la borne
B_t sont fixées avant les tirages ; (H2) la règle produit une loi prédictive p̂_s(· | x_s) qui ne dépend que de x_s et des
issues passées ; (H3) pour **toute** suite d'issues, Σ_{s ≤ t} log p̂_s(y_s) + B_t ≥ sup_Θ ℓ_t (borne de regret certifiée,
au pire cas) ; (H4) le monde est P* = p_{θ*}, θ* ∈ Θ, sans mémoire, et la carte est prévisible au-dessus du plancher.
Alors, avec D_t = Σ log p̂_s + B_t (et le maximum avec les autres membres), P(promotion) ≤ α.

*Preuve.* (1) Par (H3), D_t ≥ sup_Θ ℓ_t ≥ ℓ_t(θ*) = log P*(y_1..t), pour toute suite. (2) Donc W_t ≤ Λ_t = q(y_1..t)/P*(y_1..t).
(3) Λ est une martingale de test sous P* (espérance conditionnelle de chaque facteur ≤ 1). (4) Inégalité de Ville :
P(∃ t : Λ_t ≥ 1/α) ≤ α ; T ⊂ {1..n}. ∎ C'est exactement l'argument du v8 et du v9, avec D_t à la place du maximum.

**Théorème 2 (domination : le maximum est le plus petit dénominateur valide trajectoire par trajectoire).** Si un
dénominateur D_t vérifie D_t ≥ log P(y_1..t) pour **tout** P de la classe et **toute** suite (c'est ce que donne (H3)),
alors D_t ≥ sup_Θ ℓ_t, pour toute suite. *Preuve* : prendre le supremum sur P de l'inégalité. ∎
Conséquence : pour toute correction par regret certifiée, D_t^corrigé ≥ sup_Θ ℓ_t ≥ V_t − écart_t. Donc
**log W_t^corrigé ≤ log W_t^max + écart_t** : la méthode corrigée promeut au plus ce que promeut le maximum certifié (à
l'écart du certificat près, 10⁻³ nat dans le v9). Le surcoût exact est B_t − (sup_Θ ℓ_t − Σ log p̂_s) ≥ 0 : la borne
moins le regret effectivement subi sur ces tirages.

## 4. Le banc (réduit au niveau du juge)

`essai_regret_banc_v1.py` (empreinte section 10) recopie : K = 3, 2 traits gaussiens, 2 sous-populations, n = 200, T à
8 instants, α = 0,05, plancher 10⁻¹², lois softmax tirées comme `loi_softmax_aleatoire` (force 1,5). Archive : J = 2 lois
connues, L1 softmax, L2 = « si z0 > 0,3 alors A sinon B » ; la coupure d'archive est donc {z0 > 0,3}.
Membres fixes : uniforme, marginale d'entraînement (100 instances à part), chaque loi connue seule. Membres ajustés :
- **MAX-La** (nul limité aux coupures de l'archive) : membre linéaire + membre par morceaux sur la coupure d'archive ;
- **MAX-v9r** (« v9 réduit ») : en plus, sous-population et 7 seuils par trait (octiles du plan, fixés avant les tirages) ;
  17 membres ajustés, 136 calculs (membre × instant) par carte.

Réductions dites : membres tempérés et inclinés, moyennes glissantes omis ; seuils sur une grille au lieu de tout seuil
réel (le dénominateur du v9r est plus bas que celui du vrai v9) ; pari plein, sans fraction. Optimisation par EM dans la
paramétrisation ρ = s·r, μ_c = (1 − s)·m_c, 400 itérations au plus, arrêt à 10⁻³ nat ; le **certificat** (valeur + écart de
Frank-Wolfe) est gardé au plus petit sur les itérations. Mon EM converge moins bien que les points intérieurs du v9 : écart
résiduel maximal 1,31 nat sur un calcul (sorties, champ `ecart_certificat_max`). Cela coûte de la puissance aux méthodes
« MAX », jamais de validité.

Mélange uniforme : la mesure uniforme sur le polytope a pour image exacte, dans la paramétrisation (s, r, m_c),
s ~ Bêta(K, C(J − 1) + 1), r ~ Dirichlet(1), m_c ~ Dirichlet(1), indépendants (jacobien s^{K−1}(1 − s)^{C(J−1)}). Le mélange
est estimé par échantillonnage d'importance défensif (1 000 échantillons ; 500 sur v9r). Vérifié contre un calcul exact en
dimension 2 (programmation dynamique sur les monômes) : erreur à t = 200 entre −0,20 et +0,38 nat, médiane |≤ 0,008| nat
(`sorties/essai_regret_bornes_v1.json`). Dans le banc, aucun calcul où « mélange estimé + borne » passe sous le maximum
exact (champ `R1_La_lots_sous_le_maximum_exact` = 0 partout).

Graines : `numpy.random.SeedSequence`, entropies 2026111501 (bornes), 2026111502 (taille, `spawn_key` = indice du cas),
2026111503 (puissance, `spawn_key` = indice de la dose), un enfant par monde ; écrites dans chaque sortie.

## 5. Les méthodes, une par une

### R0-a — Poids appris en ligne sans correction (argon-p2-01) — NON VALIDE

1. *Énoncé.* Pour le membre linéaire et le membre sur la coupure d'archive, poids par cellule sur {L_j, δ_k} mis à jour
   après chaque tirage (gradient exponentié, pas η = 0,05 et 0,2 : A1-EG ; ou mélange bayésien uniforme : A1-BAYES) ;
   D_t = max(membres fixes, Σ_{s ≤ t} log p̂_s).
2. *Échec.* Sous un membre fixe P* = p_{θ*}, E[q/p̂] = Σ_y P*(y) q(y)/p̂(y) ; pour une copie (q = P*), c'est Σ P*²/p̂ ≥ 1
   (Cauchy-Schwarz). Pathologiquement : log W_t = ℓ_t(θ*) − Σ log p̂_s, le regret du prédicteur contre θ*, positif et
   croissant (de l'ordre de (d/2)·log t). Aucune domination (théorème 2 violé).
3. *Taille (1 000 mondes par cas).* Voir tableau 6.1 : 72,9 % à 99,9 % de promotions, sauf la copie d'un sommet (L1 seule),
   à 0 %, parce que la loi connue seule est déjà un membre fixe du nul.

### R0-b — Poids ajustés sur la première moitié (argon-p1-01) — NON VALIDE

1. *Énoncé.* EM par cellule indépendante sur les tirages 1..100 ; valeur e sur 101..200 contre max(membres fixes, p_ŵ) ;
   lecture aux instants 125..200.
2. *Échec.* Le nul est fixé hors de la part évaluée : E[W | 1..100] = Π_s Σ_y P*(y)²/p_ŵ(y) ≥ 1 pour une copie ; c'est le
   numérateur, pas le nul, que l'inférence universelle estime hors de la part évaluée.
3. *Taille.* 9,9 % à 30,0 % de promotions (tableau 6.1).

### R1 — Mélange uniforme (portefeuille universel) corrigé par la borne ε — VALIDE, DOMINÉ

1. *Énoncé.* Pour chaque membre ajusté de famille Θ (dimension d), p̂ = mélange bayésien sous la mesure uniforme sur Θ ;
   D_t = max(membres fixes, max_membres [log ∫ p_θ(y_1..t) dπ + R(t, d)]), avec
   **R(t, d) = d·log((t + d)/d) + t·log((t + d)/t)**. Version par morceaux (« regret contre le meilleur découpage ») : un
   mélange par partition, poids propres à chaque morceau, bruit commun, puis maximum sur les partitions (R1-COVER-v9r).
2. *Preuve de la borne (hypothèses : Θ convexe de dimension d ; p_θ linéaire et positif en θ ; π uniforme sur Θ).*
   (a) Soit θ̂ un maximiseur de ℓ_t, ε ∈ ]0, 1[ et S_ε = {(1 − ε)θ̂ + εv : v ∈ Θ} ⊂ Θ (convexité). (b) S_ε est l'image de Θ
   par une homothétie de rapport ε : π(S_ε) = ε^d. (c) Pour θ ∈ S_ε et chaque tirage : p_θ = (1 − ε)p_θ̂ + ε p_v ≥ (1 − ε)p_θ̂
   (positivité). (d) Donc ∫ p_θ(y_1..t) dπ ≥ ε^d (1 − ε)^t exp(sup ℓ_t). (e) ε = d/(t + d) donne R(t, d). ∎ Le théorème 1
   s'applique avec B_t = R(t, d) ; vérifié sur 7 200 contrôles exacts en dimension 2, aucun dépassement (bornes, `cas_exact`).
   Remarque : la borne ne dépend pas du point θ̂ ; elle couvre les sommets et le bord du simplexe.
3. *Taille.* 0 promotion dans chaque cas (tableau 6.1).
4. *Valeur de la borne* (`sorties/essai_regret_bornes_v1.json`, table) à t = 200 : membre linéaire J = 2 : 19,69 nats ;
   membre par morceaux J = 2 : 23,51 ; J = 6 : 33,91 et 48,95. Regret effectif mesuré en dimension 2 (borne 11,22) :
   médiane 3,7 (intérieur), 6,2 (sommet), 4,6 (bord), maximum 8,66 nats. La borne au pire cas est 2 à 3 fois le regret subi.
5. *Puissance.* Nulle en pratique : 0 % ; 0 % ; 0,2 % (La) et 0 % (v9r) aux doses 0,1 ; 0,2 ; 0,35 (tableau 6.2).
   Surcoût médian sur le maximum certifié (différence des log W max médians) : 10,8 nats (copies intérieures), 8,2
   (sommet), 15,0 nats (découvertes, dose 0,35, structure v9r).

### R2 — Gradient exponentié lissé corrigé par une borne de Hedge — VALIDE, INUTILISABLE

1. *Énoncé.* Par cellule indépendante (sur-ensemble de la famille à bruit commun, donc valide pour elle), poids w sur m = J + K
   composantes, prédiction w̃ = (1 − γ)w + γ/m, mise à jour w ∝ w·exp(η(1 − γ)x/(w̃·x)) ;
   B_t = C·log m/η + η·t·G²/8 + t·log(1/(1 − γ)), G = (1 − γ)m/γ ; η, γ fixés d'avance (minimum de B_200).
2. *Preuve (hypothèses : composantes ≥ 0 ; η, γ fixés).* (a) ℓ_s(w) = −log(w̃·x_s) est convexe ; ℓ_s(w_s) − ℓ_s(w*) ≤ g_s·(w_s − w*).
   (b) Les composantes de g_s sont dans [−G, 0] car w̃·x ≥ (γ/m)x_j. (c) Inégalité de Hedge (lemme de Hoeffding) sur des
   pertes linéaires d'étendue G : Σ g_s·w_s − min_j Σ g_sj ≤ log m/η + η t G²/8, et Σ g_s·w* ≥ min_j Σ g_sj. (d) ℓ_s(w*) ≤
   −log(w*·x_s) + log(1/(1 − γ)). Sommer, et additionner sur les C cellules. ∎ Sans lissage (γ = 0), G est infini : le bord
   du simplexe (lois certaines δ_k, copies au sommet) interdit toute borne finie.
3. *Valeur.* η = 0,038, γ = 0,43 : B_200 = 196,5 nats (une cellule) ; 228,0 nats (deux cellules) (bornes, champ
   `borne_gradient_exponentie`). *Taille* 0 partout ; *puissance* 0 partout ; log W max médian vers −64 à −70 nats.

### R3 — Borne de regret dépendante des données, certifiée — VALIDE, ÉGALE AU MAXIMUM

1. *Énoncé.* Remplacer R(t, d) par le regret effectivement subi sur ces tirages, certifié : B_t = V_t − Σ log p̂_s, avec V_t
   le maximum certifié.
2. *Preuve.* D_t = V_t : c'est le v9 lui-même (théorème 1 avec (H3) exacte par le certificat).
3. *Constat.* Aucune borne dépendante des données ne peut être plus petite que sup ℓ_t − Σ log p̂_s (théorème 2), et toute borne
   qui relie le mélange au supremum passe par le calcul du supremum. La version la plus fine redonne le maximum, au prix d'un
   calcul de plus. Même chose pour la correction **minimax** (loi de vraisemblance maximale normalisée, dite de Shtarkov) :
   son logarithme plus le logarithme de sa constante de normalisation vaut exactement sup ℓ_t. Pas d'essai séparé : identité
   (MAX-v9r et R1-BORNE-v9r promeuvent les mêmes mondes, tableau 6.2).

### R4 — Mélange sur les découpages (a priori sur les coupures) — VALIDE, DOMINÉ PAR R1

1. *Énoncé.* D_t = log Σ_P π_P ∫ p_θ dπ_P + R(t, d) + log(1/π_min) (mélange sur M partitions, π uniforme : log M).
2. *Preuve et domination.* log Σ_P π_P e^{a_P} + log M ≥ max_P a_P : D_t ≥ celui de R1-COVER-v9r, donc valide (théorème 1) et
   au plus aussi puissant. Avec tous les seuils réels du v9 (t + 1 coupures par trait), log M ≈ log(2(t + 1) + 1) ≈ 6 nats de
   plus. Le mélange **sans** le terme log(1/π_min) est le dénominateur que la docstring de `nul_v9.py` (point 5) écarte : sa
   garantie tombe à α/π_{F*}. Pas d'essai séparé (inégalité trajectoire par trajectoire).

### R5 — Constante calibrée par simulation, plus petite que la borne — NON VALIDE EN GARANTIE

1. *Énoncé.* Diviser par exp(c) avec c < R(t, d), choisi pour que la taille simulée reste sous α.
2. *Échec.* La garantie exige le pire cas sur un continuum de mondes du nul ; une simulation n'en voit qu'un nombre fini.
   La borne en espérance sup_{P*} log E_{P*}[P*/mélange] n'a pas de forme calculable (somme sur 3^t suites). Les copies au
   sommet subissent le plus grand regret (bornes : médiane 6,2 contre 3,7 nats à l'intérieur) : c utile resterait proche de
   la borne. Écarté sans essai.

## 6. Tableaux

### 6.1 Taille : copie exacte de la loi du monde (taux, intervalle de Clopper-Pearson à 95 %)

| cas (fichier de sortie) | mondes | MAX-La | R1-COVER-La | R2-EG-La | A1-BAYES | A1-EG 0,05 | A1-EG 0,2 | A2-MOITIE |
|---|---|---|---|---|---|---|---|---|
| intérieur du membre linéaire (`--interieur_lineaire`) | 1 000 | 0 [0 ; 0,004] | 0 [0 ; 0,004] | 0 | 0,729 [0,700 ; 0,756] | 0,754 [0,726 ; 0,780] | 0,823 [0,798 ; 0,846] | 0,146 [0,125 ; 0,169] |
| sommet : L1 seule (`--sommet_L1`) | 1 000 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| bord : 0,7 L2 + 0,3 δ_k (`--bord_L2_delta`) | 1 000 | 0 | 0 | 0 | 0,994 [0,987 ; 0,998] | 0,999 [0,994 ; 1] | 0,999 | 0,099 [0,081 ; 0,119] |
| copie par morceaux sur la coupure d'archive (`--morceaux_archive`) | 1 000 | 0 | 0 | 0 | 0,998 [0,993 ; 1,000] | 0,998 | 0,998 | 0,168 [0,145 ; 0,193] |
| poids extrêmes par morceaux, bruit commun 0,02 (`--poids_extremes_morceaux`) | 1 000 | 0 | 0 | 0 | 0,996 [0,990 ; 0,999] | 0,996 | 0,996 | 0,300 [0,272 ; 0,330] |
| copie par morceaux hors de l'archive (seuil médian de z1) (`--morceaux_hors_archive`) | 500 | 0,980 * | 0,786 * | 0 | 1,000 | 1,000 | 1,000 | 0,978 |

\* Hors de la classe de La (trou rouvert par construction, `preuve-validite-nul-limite-v1.md`, section 7) : ce n'est pas un
défaut de validité. Sur ce cas, avec la structure v9 réduite (qui contient ce seuil) : **MAX-v9r 0/500, R1-COVER-v9r 0/500,
R2-EG-v9r 0/500** [0 ; 0,0074]. 500 mondes au lieu de 1 000 : la version à 1 000 mondes a dépassé la limite de dix
minutes et a été arrêtée par son délai, sans sortie.

### 6.2 Puissance : vraie découverte, monde = (1 − dose)·(½ L1 + ½ L2) + dose·N, N softmax neuve ; carte = monde ; 500 mondes par dose

| méthode | dose 0,1 (`--d0.1`) | dose 0,2 (`--d0.2`) | dose 0,35 (`--d0.35`) |
|---|---|---|---|
| MAX-v9r (maximum certifié, façon v9) | 0,004 [0,001 ; 0,014] | 0,100 [0,075 ; 0,130] | 0,556 [0,511 ; 0,600] |
| MAX-La (nul limité aux coupures de l'archive) | 0,014 [0,006 ; 0,029] | 0,182 [0,149 ; 0,219] | 0,688 [0,645 ; 0,728] |
| R1-BORNE-v9r (plafond de R1-COVER-v9r exact) | 0,004 | 0,100 | 0,556 |
| R1-COVER-La | 0 [0 ; 0,007] | 0 | 0,002 [0,000 ; 0,011] |
| R1-COVER-v9r | 0 | 0 | 0 |
| R2-EG-La, R2-EG-v9r | 0 | 0 | 0 |
| (artefact) A1-EG 0,2 / A2-MOITIE | 0,996 / 0,310 | 0,998 / 0,414 | 0,994 / 0,672 |

Appariement sur les mêmes tirages (champs `promues_par_elle_seule_contre_MAX-v9r` et `promues_par_MAX-v9r_seul`) :
R1-COVER-v9r ne promeut aucun monde que MAX-v9r ne promeut pas, et manque 2, 50 et 278 mondes que MAX-v9r promeut. MAX-La
promeut 5, 41 et 66 mondes de plus que MAX-v9r et n'en manque aucun (inclusion attendue : classe plus petite). La
« puissance » des artefacts n'a pas de sens : ils promeuvent aussi les copies.

## 7. Artefact : ce que le banc voit

Les deux façons des fiches échouent nettement dans le même banc, sur les mêmes mondes que les méthodes corrigées :
en ligne sans correction, 72,9 % à 99,9 % des copies intérieures, au bord, par morceaux et à poids extrêmes ; moitié,
9,9 % à 30,0 % (bornes basses à 95 % : 0,081 à 0,272, toutes au-dessus de 0,05). Le banc **voit** donc l'invalidité. Un
seul cas ne la voit pas : la copie d'un sommet (L1 seule), parce que la loi connue seule est un membre fixe du nul et
domine déjà le dénominateur ; je le dis : ce cas ne teste rien pour les artefacts. Mes chiffres sont du même ordre que ceux
de la preuve (section 8.3 : 96,5 % à 100 % et 64,9 %), avec un banc différent (deux lois connues dépendant des traits,
membres fixes du juge présents) : la moitié est moins promue ici, parce que les membres fixes et le maximum avec eux
absorbent une partie de l'écart.

## 8. Ce qu'il reste de puissance, et où la chercher

- Dans cet angle : **rien**. Le théorème 2 fixe le plafond (le maximum exact), le v9 l'atteint à 10⁻³ nat près, et toute
  correction certifiée paie de 8 à 15 nats de plus sur ce banc (de l'ordre de (d/2)·log t + d : la borne au pire cas moins le
  regret subi). La correction est **plus coûteuse que le maximum lui-même**, en nats et en calcul (section 9).
- Ailleurs (hors de mon angle, à vérifier par les autres angles) : réduire la classe (MAX-La gagne 5 à 66 mondes sur 500
  sur MAX-v9r, au prix de la copie hors archive promue à 98 %) ; ou une valeur e qui ne domine pas trajectoire par
  trajectoire mais seulement en espérance (projection d'information inverse, piste de la preuve, section 8.4 (ii)) : le
  théorème 2 ne s'y applique pas.

## 9. Coût de calcul par carte, et ce que cela changerait à la conception scellée

Durées moyennes par carte (machine chargée ; `duree_par_monde_s_moyenne` des sorties) : structure La (16 calculs) :
maximum certifié 0,14 à 0,22 s, mélange estimé 0,09 à 0,14 s **en plus** (la proposition d'importance part du point de
l'EM), gradient exponentié 0,03 à 0,04 s. Structure v9r (136 calculs) : maximum 1,42 à 1,54 s, mélange 0,76 à 0,91 s
**en plus**, gradient exponentié 0,19 à 0,23 s. Un mélange **exact** (non estimé, nécessaire pour une garantie sans
réserve d'estimation) demande une somme sur les monômes dont le nombre croît comme t^d : hors de portée à d = 5, t = 200.
R1 et R3 coûtent donc **plus** que le maximum, pour un verdict égal (R3) ou moins puissant (R1).

Ce que l'adoption changerait (je nomme, je ne tranche pas) : remplacer la valeur d'un membre ajusté du v9 par « mélange +
borne » serait un nul neuf (v10), donc une modification du juge et de sa description publique, avec sa propre validation
scellée : **nœud du directeur**. Je ne recommande pas d'ouvrir ce nœud pour R1, R2, R4 (dominés) ni pour R3 (identique au
v9). Correction à porter au relevé (non un nœud) : la variante « poids appris en ligne » ne se répare pas par une borne de
regret au sens d'un gain de puissance.

## 10. Fichiers (dossier `docs/notes/organisme-idees-juge-v1/correction-poids-v1/regret/`, chacun scellé par un compagnon `.sha256`)

| fichier | rôle | empreinte |
|---|---|---|
| `essai_regret_banc_v1.py` | banc commun (logique du juge recopiée en réduit) | `8d1c44db471067333a3b267d95e393ff85eadc06ffa50faf689b7176b1e8ae65` |
| `essai_regret_juge_v1.py` | jugement d'un monde par toutes les méthodes | `f698afe7a141bb5b5963f3b3699671d09dc46d3c5602d996b439eaa9e9b11135` |
| `essai_regret_bornes_v1.py` | bornes, cas exact en dimension 2 | `03c3f8c79a9624d59bd916a2e611a1b342cfdd212c7d3f87f575d13f7e5773c5` |
| `essai_regret_taille_v1.py` | essais de taille | `aacdb7d9f45c1ab2c86dc4c7c7c950f1401dcaab21c983170743eda8e98046fb` |
| `essai_regret_puissance_v1.py` | essais de puissance | `9772a899dad20edf80d8769ee9d554032e7d7ceb2992c930ef9dff49d3a32312` |
| `sorties/essai_regret_bornes_v1.json` | | `a6b84c8534dc87008a9ec3323b0ab1c53370c76dfde8d4d9780c5c4cc1fe3c3a` |
| `sorties/essai_regret_taille_v1--interieur_lineaire.json` | | `81e70e4265c67eaab6cf206ffc7a40957d547ba7131fe31043797ebb48e9965e` |
| `sorties/essai_regret_taille_v1--sommet_L1.json` | | `05e273d3ff2c8f85d17c396cbf1b294f2daf63158d0ed02931e0cd863e24d556` |
| `sorties/essai_regret_taille_v1--bord_L2_delta.json` | | `af67a8519d126afcbbf427d6a1f51509b69273c1f778e50beb632094bcce58a7` |
| `sorties/essai_regret_taille_v1--morceaux_archive.json` | | `13459f7ef540d452653cd5ee9625eff4198e16873f4347987fc6dd0e0da89699` |
| `sorties/essai_regret_taille_v1--poids_extremes_morceaux.json` | | `0adba3dbbb1bd803adb3da86bd136313b25ab7d97e8dfe5116fdb1ab4d0b8fb1` |
| `sorties/essai_regret_taille_v1--morceaux_hors_archive.json` | | `50f615b1ee8b5088e94f5a927d3ec76a967a7f9175cb33acbeab4ccb3ae0186a` |
| `sorties/essai_regret_puissance_v1--d0.1.json` | | `c0ad7c0fe29e5728480d49648c9a9a6b8df8b49fa6291ce1157719cd31a13af4` |
| `sorties/essai_regret_puissance_v1--d0.2.json` | | `3987af243431942fb2e40c891db399fb1c50cbc0a229789edb76d243bfe2703e` |
| `sorties/essai_regret_puissance_v1--d0.35.json` | | `51d40d4cb5aba9fcf3e8e5d4d02fb52665786e299bae7f7a65a7793fc862efd4` |

Les programmes n'ont pas
changé depuis les essais.

## 11. Réserves

1. Banc réduit (section 4) : deux lois connues, seuils sur une grille, membres log-linéaires omis, certificat moins serré
   que celui du v9. Les conclusions des théorèmes 1 et 2 ne dépendent pas du banc ; les chiffres, si.
2. Le mélange du banc est **estimé** (erreur mesurée en dimension 2 seulement) ; la taille de R1 tient ici sans aucun calcul
   sous le maximum exact, mais une mise en production demanderait un mélange exact ou majoré.
3. Puissance et cas hors archive sur 500 mondes (limite de temps) ; doses fixées après un seul monde d'essai du code (dose 0,5,
   saturé), avant tout essai de puissance.
4. Doses au-dessous de 0,35 : la puissance de toutes les méthodes valides est faible ; l'ordre des méthodes est le même
   aux trois doses.

## Références (toutes à vérifier sur pièce ; aucun chiffre n'en est repris)

Cover, « Universal portfolios », Mathematical Finance, 1991 (mélange uniforme, borne de regret) ; Freund et Schapire (Hedge) ;
Helmbold, Schapire, Singer et Warmuth (gradient exponentié pour les portefeuilles) ; Shtarkov (loi de vraisemblance maximale
normalisée) ; Wasserman, Ramdas et Balakrishnan, « Universal inference », 2020 (citée par `nul_v8.py`) ; Grünwald, de Heide
et Koolen, « Safe testing » (projection d'information inverse). Les preuves ci-dessus sont écrites ici, sans appui sur ces
textes.
