# Preuve de validité — nul par morceaux limité aux conditions de l'archive — v1

**Statut.** Pièce écrite et scellée **avant tout jeu** du banc de l'idée 1.1 (mot de Lazar R-2851 : « preuve écrite de
validité scellée avant le jeu pour 1.1 »). Elle accompagne `prereg-nul-par-morceaux-limite-v1.md` (même dossier). Non
contre-lue : la contre-lecture (R2) par un sous-agent neuf d'un autre modèle est à faire (section 11). **Aucun résultat du
banc n'existe** : le banc n'est pas écrit. Les calculs des sections 8 et 10 sont des comptes sur processeur, sans code ni
donnée du banc, faits pour vérifier ce que j'écris ; leurs scripts sont recopiés en entier.

- **Auteur** : concepteur neuf (modèle A au sens de R-2851), sous-agent de la session mère ; je n'ai écrit ni le relevé, ni
  les fiches, ni le juge, ni les nuls v8 et v9, ni aucune pièce citée.
- **Date** : 2026-11-15, début de rédaction 08:21 UTC (`date -u`). Dépôt lu sur `main` (tête `ff85c5f0` au début ; lecture
  seule, aucun commit).
- **Calculs** : Python 3.13.18, numpy 2.4.6, scipy 1.17.1 (`/home/user/controle-ia-travail/.venv/bin/python -I -B`).

## 0. Ce que la pièce établit, en six lignes

1. Le nul limité garde une **garantie de taille α sur sa propre classe** : si la loi du monde est un membre d'une famille
   du nul limité, la probabilité de promouvoir une carte, à l'un des instants de lecture fixés, est au plus α (théorème 1).
   C'est l'argument de l'inférence universelle que portent déjà les nuls v8 et v9, appliqué à une famille plus petite.
2. Il ne garde **aucune garantie hors de sa classe**, en particulier sur les copies par morceaux coupées ailleurs qu'aux
   conditions retenues, que le v9 couvre : c'est le prix de la restriction ; il se mesure, il ne se démontre pas (section 7).
3. Trajectoire par trajectoire, sur les mêmes tirages : richesse du nul limité ≤ richesse du v8 ; et, pour les variantes à un
   seul niveau de coupure, richesse ≥ richesse du v9 aux écarts de certificat près (section 6).
4. Les deux façons d'« apprendre les poids » que proposent les fiches — **en ligne** (argon-p2-01) et **sur une moitié des
   tirages** (argon-p1-01) — **ne sont pas valides** : une copie exacte d'un membre du nul y est promue (section 8 :
   démonstration et calcul, 96,5 % à 100 % et 64,9 % des répétitions au lieu d'au plus 5 %).
5. La validité ne dépend ni du nombre de conditions ni du nombre de membres ; seule la puissance en dépend.
6. Le banc ne s'écarte d'aucune conception scellée ; **adopter** un nul limité au juge serait une version neuve du nul :
   nœud de Lazar (section 9).

## 1. Ce que j'ai lu (chemin, empreinte sha256 recalculée le 15 novembre)

| pièce | chemin | empreinte |
|---|---|---|
| relevé d'idées (idée 1.1) | `docs/notes/organisme-conception-propre-v1/relecture-exploratoire-v2/releve-idees-reutilisables-v1.md` | `bd253b6c68f6baada0e61b5381f029b52838ca34aa092502e55253c662451c6c` |
| fiches validées (argon-p1-01 = n° 0, argon-p2-01 = n° 14, opus-p1-05 = n° 9, fable-p1-05 = n° 13) | `runs/course-ideation-conception-propre-v1/20261113-235541-course-ideation-conception-propre-v1-g1/copies/sortie--fiches-validees.json` | `a9f9594e2dc3a7a553c54577202817758e3f7ef231445f1a48d500fc647389d5` (égale à son compagnon) |
| copie empreintée du code de l'organisme au commit `94bfd92` (53 fichiers, `sha256sum -c` conforme le 15 novembre) | `docs/notes/organisme-courbe-dose-reponse-v1/code-organisme-94bfd92/` : `LISEZMOI.md`, `empreintes-copie-v1.txt` | `e552c7eb8ccff4c8787ef7eba7288b583193c456477e8f56fb3fb3e7576409c1` ; `0153e02d4522fe21eb1cf52985574eba38b5f260f7a3a08183d63589f29f32df` |
| juge par pari (richesse, tirages frais, bibliothèque) | `…/orchestrator/pole/selection_pari.py` | `359928110d757cd54cc0d2773910c7360895b68cac5d17e0e4b4e9933ef306bc` |
| membres ajustés, lecture aux instants fixés, certificat de Frank-Wolfe | `…/orchestrator/pole/nul_filles_v2.py` | `0ed9b4adbcddc4ad77a1c97d5cbd5706f14926e9c47fe96ce2bab3221a138910` |
| nul v8 (argument de validité, classe couverte et non couverte) | `…/orchestrator/pole/nul_v8.py` | `cc452aafd17121a7c0ec42829eea47063ffee1f6cdf7f642e264d528f976b888` |
| membres d'archive, règle e-BH | `…/orchestrator/pole/cycle.py` | `798f039042e3ee1f18df5c566f5a0ddee5dac5c98225c8ce621e267174c8ee18` |
| jugement d'une carte fraîche (`juger_carte`) | `…/orchestrator/pole/a_blanc_v59.py` | `606aa8b4fcc38786b38cf2954da46533eed9384232a56100d22ff30b8ce0826c` |
| description publique du nul v9 (l. 64) | `livrables/page-publique-organisme-2026-11-10-v1/resultats/attaque-goodhart-v2/README.md` | `c549a31b266b6952c9f7fc2922243eab21ca304fe7626099310016f071f8ccbb` |
| verdict de la validation du v9, recalculé (« puissance perdue ») | `docs/notes/ideation-organisme-v1/validation-nul-v9-v1/audit-verdict-validation-nul-v9-v1.md` | `9086a420a082ed8fd7d76dc666ef5ef336a9f6842be8ff90e4aca7db0d72f7c8` |
| vérification courte du v9 (14 empreintes, dont `nul_v9.py`) | `docs/notes/ideation-organisme-v1/validation-nul-v9-v1/verification-courte-brouillon4-nul-v9-v1.md` | `2992166d95ef13e13d351a9b95e178ff7f8269a8810b0f4f4bfff3cfb928caad` |
| note de la brèche W2 (« moins de deux lois connues : aucun membre par morceaux ») | `docs/notes/ideation-organisme-v1/breche-w2-v1/note-breche-w2-v1.md` | `4d3a6d1c84b8f4790ff9635f974da840ec577c62b31a8cfb1a73ded1440da404` |
| préenregistrement de la boucle réelle, brouillon 3 (l. 272 : le v9 « ferme le trou par morceaux ») | `docs/notes/organisme-boucle-reelle-v1/preenregistrement-boucle-reelle-organisme-v1-brouillon3.md` | `04598de62300185806975ae5df5fcdd054557f9a46b935e40d7d3479c240ec23` |
| recoupement (bornes 7 et 9, J1, J6) et synthèse (§ 8) | `docs/notes/organisme-bassins-etroits-v1/recoupement-methodes-v1.md` ; `docs/notes/collisionneur-bassins-etroits-v1/synthese-v1.md` | `eecd98fab0beff8c99414380a5d12b18feafd1581d38c7fe54b94491327ab172` ; `5fd7e26fc8c04ddd131bcd5b9c03afd118ccd6bd8458e90f1aa6685a51f9517a` |

**Le code du nul v9 n'est pas dans ce dépôt.** `orchestrator/pole/nul_v9.py` (`7ae450df2482246122bf9fbcf0fa5ef30b4a7e4c6f0d09531e83af048e46ee95`)
est dans le dépôt public de l'organisme (`https://github.com/lciric/ideation-organism`, commits `66dbcf1` et suivants), avec
sa preuve (`orchestrator/prereg/rapport-redaction-nul-v9.md`, section 3), son banc (`orchestrator/demonstrations/banc_tricheurs_v9.py`,
`7e4bff5995df2a7d62a4f5a2f5f9176da614e657a55b05183325fa2fc6e24e44`) et le texte de sa validation
(`orchestrator/prereg/preenregistrement-validation-nul-v9-v1.md`, `54c5713d07f61b7f2bb3dd8218f4bca881a044a2b11508015db5e727d62c18fb`).
Les paquets git versés dans ce dépôt (`code-v66`, `code-v67`, `a1-v4-reprise-v9`) sont incrémentaux : leurs commits
prérequis (`cef5ea60…`, `7e415cba…`, `8947bc80…`) n'y sont pas (`git bundle verify`, 15 novembre). Je n'ai pas récupéré le
dépôt public (consigne : s'arrêter sur ce point). Les dix autres fichiers dont dépend le v9 dans le bloc gelé de sa
validation sont dans la copie `94bfd92`, **aux mêmes empreintes** (comparaison faite : `__init__`, `caviardage`,
`controles_pari`, `cycle`, `fiche`, `memoire`, `nul_filles_v2`, `nul_v8`, `outils`, `selection_pari`). Ce que je dis du
v9 vient de sa description publique et des pièces ci-dessus ; la section 6 (b) en dépend et doit être relue sur le code.

## 2. Le juge tel que le code le calcule (notations)

Une carte fraîche est jugée par `a_blanc_v59.juger_carte` (le juge de la boucle réelle v66 et v67 l'appelle tel quel) :

- un **plan** de n = 200 instances x_s = (z_s, g_s), tirées de la graine de la tâche ; des **instants de lecture**
  T = {25, 50, …, 200} (`cycle.instants_reguliers(200, 8)`), écrits dans l'engagement ; seuil α = 0,05 ;
- une **bibliothèque** 𝒩 : membres ordinaires (marginale ajustée, uniforme, moyennes glissantes, marginale d'entraînement
  tirée de 100 instances à part), et membres d'archive du nul v8 (`nul_v8.membres_archive_v8`, qui appelle
  `cycle.membres_de_l_archive(..., ajuste=True)`) : pour chaque loi connue L_j, la loi seule, son mélange à l'uniforme sur
  une grille, la loi tempérée et inclinée (membre log-linéaire ajusté), et la **mise en commun linéaire**
  Σ_j π_j·L_j + Σ_k ρ_k·δ_k (δ_k : loi certaine de l'issue k), ajustée ;
- l'**engagement** (loi q de la carte, plan, bibliothèque, instants, α) est gelé ; les **tirages frais** y_1..y_n sont tirés
  ensuite, d'une graine dérivée de son empreinte (`selection_pari.tirer_frais`), sous l'ordre d'exécution secret ;
- la **richesse** (`nul_filles_v2.evaluer_v2`) : pour t ∈ T,
  log W_t = log q(y_1..t) − D_t, où D_t = max( trajectoires des membres ordinaires à t ; V_m(t) des membres ajustés ),
  et V_m(t) est la valeur maximale du membre m sur les t premières issues **plus sa marge d'optimisation** (écart de
  Frank-Wolfe pour le membre linéaire, `_lineaire` ; décrément de Newton au carré pour un membre log-linéaire, `_logit`) ;
- **promotion** de la carte seule : il existe t ∈ T tel que log W_t ≥ log(1/α). **Valeur e** pour la règle e-BH
  (`cycle.appliquer_multiplicite`) : W arrêtée au premier t ∈ T où elle atteint m/α, sinon W_n.

## 3. Le nul limité

**Lois connues.** 𝒦 = {L_1, …, L_J} : les lois d'archive de l'espace de la carte (et les deux parents d'une fille), celles
que `cycle.membres_de_l_archive` retient.

**Conditions de l'archive, C_arch.** Par un parcours de l'arbre de chaque loi de 𝒦 (mêmes clés que
`selection_pari.types_de_la_loi` : `si`, `sinon`, `loi`, `base`, `defaut`, `lois`, `composantes`) :
- nœud `si_sinon` de condition `{"indice": j, "seuil": s}` → la partition {z_j > s} | {z_j ≤ s} (`_condition` lit
  « > seuil », seuil 0 par défaut) ; de condition `{"sous_population": v}` → la partition par la sous-population ;
- nœud `par_sous_population` → la partition par la sous-population.
Seuils lus à six décimales ; doublons retirés. C_arch est **une fonction de l'archive seule**, connue avant le gel.

**Partitions déclarées, C_decl.** La partition par la sous-population et, pour chaque trait j, {z_j > 0} : celles que le juge
emploie déjà pour les formes si/sinon des filles (`selection_pari.bibliotheque_fille` : « sous-population, signe de chaque
trait »).

**Partitions retenues.** 𝒫₁(C) : une partition par élément de C. 𝒫₂(C) : 𝒫₁(C) plus, pour chaque paire d'éléments distincts
de C, leur partition commune la plus fine (au plus quatre cellules non vides pour deux seuils).

**Famille d'une partition P.** Pour une instance x de la cellule c(x) de P :
p_{μ,ρ}(y | x) = Σ_j μ_{c(x),j}·L_j(y | x) + Σ_k ρ_k·1[y = k], avec μ ≥ 0, ρ ≥ 0 et, **pour chaque cellule c**,
Σ_j μ_{c,j} + Σ_k ρ_k = 1 : des poids des lois connues propres à chaque cellule, une part aveugle commune. C'est, d'après sa
description publique (`c549a31b…`, l. 64 : « every one-level piecewise recombination of the known laws (by sub-population,
or on either side of any real threshold on one trait), with a common blind noise »), la famille des membres par morceaux du
v9, **restreinte à une liste finie de partitions** ; le préenregistrement exige que le code du nul limité reprenne celui du v9
en ne changeant que cette liste (si le code du v9 dit autre chose de la part aveugle, c'est le code qui fait foi et la
section 6 (b) se relit sur lui).

**Valeur certifiée.** f_t(μ, ρ) = Σ_{s ≤ t} log p_{μ,ρ}(y_s | x_s) est concave (logarithme d'une forme linéaire) sur un
polytope dont les sommets sont (ρ = e_k, μ = 0) pour chaque issue k, et (ρ = 0, μ_c = e_{j_c} dans chaque cellule c) pour
chaque choix d'une loi connue par cellule. Pour tout point admissible u, l'écart de Frank-Wolfe
g_t(u) = max_{sommets v} ∇f_t(u)·(v − u) majore f_t* − f_t(u) (concavité). La valeur employée est
V_P(t) = min(0, f_t(u) + g_t(u)) ≥ f_t* : elle domine le maximum de la famille **quel que soit l'état de l'optimiseur**. La
maximisation de ∇f·v sur les sommets se fait cellule par cellule (comparer max_k ∂_{ρ_k} f à Σ_c max_j ∂_{μ_{c,j}} f) ; on a
∇f·u = t (homogénéité), d'où g = max(…) − t, comme dans `nul_filles_v2._lineaire`. Vérifié numériquement (section 10).

**Nul limité.** 𝒩_L(C, ν) = 𝒩₈ ∪ {F_P : P ∈ 𝒫_ν(C)}, avec ν ∈ {1, 2}, **seulement si J ≥ 2** (avec moins de deux lois
connues, aucun membre par morceaux, comme le v9 : note W2, `4d3a6d1c…`, section 3). Les trois bras du préenregistrement :
**La** = 𝒩_L(C_arch, 1) ; **La2** = 𝒩_L(C_arch, 2) (lettre des fiches : « intersections d'au plus deux conditions ») ;
**Ld** = 𝒩_L(C_arch ∪ C_decl, 1).

## 4. Théorème 1 — taille sur la classe du nul limité

**Hypothèses.**
- **H1 (gel).** La loi q de la carte, le plan x_1..x_n, les instants T, la bibliothèque — donc C et 𝒩_L — sont fixés avant
  les tirages frais et entrent dans l'empreinte de l'engagement. En particulier C est calculé sur l'archive, **jamais** sur
  les tirages frais.
- **H2 (fraîcheur).** Les issues fraîches sont tirées après le gel, d'une graine dérivée de l'empreinte, indépendamment de
  tout ce qui a servi à bâtir q, x, C et la marginale d'entraînement.
- **H3 (monde dans la classe).** La loi du monde est une loi conditionnelle P*(y | x) qui ne lit pas l'historique et qui
  appartient à une famille de la bibliothèque : P* = p_{θ*}, θ* ∈ Θ_m, pour un membre m de 𝒩_L.
- **H4 (certificat).** Pour tout membre ajusté m et tout t ∈ T, V_m(t) ≥ sup_{θ ∈ Θ_m} Σ_{s ≤ t} log p_θ(y_s | x_s). Exact
  pour le membre linéaire et pour les membres par morceaux (section 3) ; pour un membre log-linéaire, la marge de Newton
  n'est une borne qu'« au second ordre près de l'optimum, sans preuve » (`nul_v8.py`, docstring, point 5) : le théorème ne
  vaut pour un monde de la classe log-linéaire que sous cette réserve, héritée du v8.
- **H5 (prévisibilité).** q(· | x_s, y_<s) ne dépend que de x_s et des issues passées dans l'ordre du plan, et reste au-dessus
  du plancher 10⁻¹² (`selection_pari.PLANCHER`).
- **H6 (ordre).** Sous l'ordre d'exécution secret, pour un monde qui ne lit pas l'historique, les issues rangées dans l'ordre du
  plan sont indépendantes sachant les instances, y_s ~ P*(· | x_s).
- **H7 (instants).** T est fini et fixé d'avance (`instants_lecture` sous l'empreinte).
- **H8 (lecture).** Promotion = il existe t ∈ T avec log W_t ≥ log(1/α) ; aucune autre règle (pas de choix du nul, des
  conditions ou des instants après avoir vu les issues ; pas de « meilleur de plusieurs nuls »).

**Énoncé.** Sous H1 à H8, P(promotion) ≤ α, conditionnellement à l'archive, à la carte, au plan et à la marginale
d'entraînement.

**Preuve.**
1. *Domination.* Pour t ∈ T, D_t ≥ V_{m*}(t) ≥ sup_{θ ∈ Θ_{m*}} Σ_{s ≤ t} log p_θ(y_s | x_s) ≥ Σ_{s ≤ t} log P*(y_s | x_s)
   (H3, H4).
2. *Majoration.* log W_t = log q(y_1..t) − D_t ≤ log Λ_t, où Λ_t = Π_{s ≤ t} q(y_s | x_s, y_<s) / P*(y_s | x_s).
3. *Martingale.* Pour la filtration F_t = σ(y_1, …, y_t), le plan étant fixé : E[q(y_t | ·) / P*(y_t | x_t) | F_{t−1}] =
   Σ_{y : P*(y | x_t) > 0} q(y | ·) ≤ 1 (H5, H6). Λ est une surmartingale positive, Λ_0 = 1.
4. *Ville.* P(∃ t ≥ 1 : Λ_t ≥ 1/α) ≤ α (inégalité de Ville pour une surmartingale positive). Comme T ⊂ {1, …, n} et
   W_t ≤ Λ_t : P(∃ t ∈ T : W_t ≥ 1/α) ≤ α. ∎

**Remarques.** (i) Le nombre de partitions et de membres n'entre nulle part : la garantie ne s'affaiblit pas quand C grandit ;
seule la puissance baisse (le maximum D_t monte). (ii) **Carte membre** (copie exacte d'un membre de la classe) : son
numérateur est la vraisemblance d'un point θ_carte de la famille, donc ≤ D_t : W_t ≤ 1 **à chaque tirage**, plus fort que
Ville ; toute promotion d'une telle carte au banc est un défaut de code ou de certificat (règle d'audit A1 du
préenregistrement). (iii) L'argument est celui du rapport de vraisemblance scindé de l'inférence universelle, que
`nul_v8.py` (docstring, points 3 et 4) attribue à Wasserman, Ramdas et Balakrishnan, « Universal inference », PNAS, 2020
(référence de méthode citée par le code ; PDF non versé au dépôt ; aucun chiffre n'en est tiré, R7).

## 5. Corollaire — valeurs e et règle e-BH

La valeur e d'une carte, e = W_τ avec τ = premier t ∈ T où W_t ≥ m/α (sinon max T), est un temps d'arrêt borné de la
filtration : E[e] ≤ E[Λ_τ] ≤ Λ_0 = 1 (arrêt optionnel d'une surmartingale positive). La règle de Benjamini et Hochberg sur
valeurs e (Wang et Ramdas, 2022, citée par `cycle.py`), avec m fixé avant toute issue (`m_fixe`), borne alors par α le taux de
fausses découvertes **sous dépendance quelconque** entre cartes. Toutes les cartes d'une génération testant la même
hypothèse « le monde est dans la classe de 𝒩_L(C) », ce taux est, sous cette hypothèse, la probabilité d'au moins une
promotion.

## 6. Comparaisons trajectoire par trajectoire (mêmes tirages, mêmes instants)

**(a) Limité contre v8.** 𝒩₈ ⊆ 𝒩_L : mêmes membres, mêmes valeurs, plus d'autres. Donc D_t^L ≥ D_t^8 et **W_t^L ≤ W_t^8** pour
tout t ∈ T : toute promotion sous un nul limité en est une sous le v8 ; la puissance d'un nul limité est au plus celle du v8.

**(b) Limité à un niveau contre v9.** Si la famille du v9 est celle de la section 3 (partitions à un niveau par la
sous-population et par tout seuil réel d'un trait), chaque F_P, P ∈ 𝒫₁(C_arch ∪ C_decl), est une famille du v9 (le v9 couvre
tout seuil réel ; sur un échantillon, la partition qu'induit un seuil de l'archive est l'une de celles qu'il parcourt). Alors,
pour P de La ou de Ld : V_P^L(t) ≤ sup_{F_P} + g_P(t) ≤ D_t^9 + g_P(t), et D_t^L ≤ max(D_t^8, D_t^9 + g_max(t)) ≤ D_t^9 + g_max(t)
(car D^9 ≥ D^8). D'où **log W_t^L ≥ log W_t^9 − g_max(t)**, g_max(t) étant le plus grand écart de certificat des membres par
morceaux du nul limité à l'instant t. Avec une tolérance d'arrêt de l'optimiseur de 10⁻⁴ nat (préenregistrement), La et Ld
promeuvent tout ce que le v9 promeut, sauf égalité à 10⁻⁴ nat près ; leur puissance est au moins celle du v9 **par
construction** : la question du banc est l'ampleur de l'écart, pas son signe.

**(c) La2 contre v9.** Les partitions à deux niveaux ne sont pas des membres du v9 : aucun ordre. Le signe de l'écart de
puissance entre La2 et le v9 est une vraie prédiction.

**(d) Conséquence sur les copies hors de la classe limitée.** Pour un monde de la classe du v9 hors de celle d'un nul limité,
les promotions du nul limité sont encadrées par celles du v9 (en dessous) et celles du v8 (au-dessus) : aucune garantie.

## 7. Ce que la garantie ne couvre pas

1. **Les copies coupées hors de C** : seuil hors de l'archive, et, pour La, sous-population ou signe d'un trait quand
   l'archive n'en porte aucun (la forme de W2 : « S1 sur une sous-population, S2 sur l'autre ») ; trou rouvert par
   construction, à mesurer.
2. **Le critère de nouveauté** : l'hypothèse testée porte sur le monde (« il est dans la classe ») ; dans un monde qui porte une
   vraie composante, la garantie ne borne pas la part des fausses découvertes au sens de l'oracle (faits du collisionneur,
   `d19b5400…`, § 4 ; conception du monde riche v3, `386d48ba…`, § 3.3 (c)).
3. **Les générations** : la garantie vaut à archive donnée ; le contrôle des erreurs d'une génération à l'autre n'est écrit
   nulle part (recoupement, `eecd98fa…`, § 9), inchangé.
4. **La réserve log-linéaire** (H4), héritée du v8.
5. **Le prix du certificat** : un certificat lâche coûte de la puissance, jamais de la validité.
6. **Toute règle qui choisirait C après avoir vu des issues** (ajouter la coupure que suggèrent les tirages frais) rompt H1 et
   n'est pas couverte. Choisir entre La, La2 et Ld **au vu du banc** pour la production est une décision de dessin, prise sur
   d'autres tirages que ceux de production : elle ne touche pas la garantie par carte.

## 8. Les deux variantes des fiches ne sont pas valides

**8.1 Poids appris en ligne (argon-p2-01, fiche n° 14, champ `demande_organisme`, point 3).** Le dénominateur y est
Π_s p_{w_{s−1}}(y_s | x_s), poids mis à jour après chaque épisode. La fiche affirme que le produit des rapports « forme une
martingale de valeur initiale 1 » sous le nul étendu. C'est une martingale sous la **loi prédictive** p_{w_{s−1}}, pas sous un
membre fixe P* du nul : E_{P*}[q(y) / p_{w}(y)] = Σ_y P*(y)·q(y) / p_w(y), qui, pour une copie (q = P*), vaut Σ_y P*(y)² / p_w(y) ≥ 1
(Cauchy-Schwarz), avec égalité seulement si p_w = P*. Pour une copie exacte, log W_t est le **regret** du prédicteur
séquentiel contre P*, qui croît comme (d/2)·log t pour d paramètres libres : une copie est promue.

**8.2 Poids ajustés sur la première moitié, valeur e sur la seconde (argon-p1-01, fiche n° 0).** Pour une copie (q = P*),
E[log W | première moitié] = (n/2)·KL(P* ‖ p_ŵ) ≥ 0 et E[W | première moitié] = (Σ_y P*(y)² / p_ŵ(y))^{n/2} ≥ 1 (écrit
sans traits ; avec des traits, c'est un produit de facteurs par instance, chacun ≥ 1 par la même inégalité) : pas une
valeur e. L'inférence universelle fait l'inverse : c'est **l'alternative** qui s'estime hors de la part évaluée, et le maximum
de vraisemblance **du nul** se calcule sur la part même où W est évaluée (`nul_v8.py`, docstring, point 4 : « c'est
l'alternative, au numérateur, qui doit être estimée hors de cette part »).

**8.3 Calcul.** Monde = membre du nul « mélange, par cellule, de deux lois connues et des lois certaines δ_k », 4 cellules,
3 issues, 200 tirages, lecture aux instants 25 à 200 ; carte = loi du monde (copie exacte) ; 1 000 mondes. Sortie (fichier
de sortie `673a7a1aeefbe4793680477cc4c9c6dfad6ac32e812b7c106a5446733c28ebdf`, script `865025d9915150d3cfac98cfbb7e9eb19fe414ffcb52bd14d199758351b2a7d9`,
dans le dossier de travail de la session ; recopiés ici en entier) :

```
(a) en ligne, eta=0.05 : promue (instants 25..200) 0.965 ; log W final médian 8.71
(a) en ligne, eta=0.2 : promue (instants 25..200) 1.000 ; log W final médian 20.15
(a) en ligne, eta=1.0 : promue (instants 25..200) 1.000 ; log W final médian 104.74
(a') Krichevsky-Trofimov par cellule : promue (instants 25..200) 1.000 ; log W final médian 11.93 ; part log W final > 0 : 1.000
(b) moitié : promue en fin de seconde moitié 0.649 ; lecture continue 0.732 ; log W médian 4.71
(c) inférence universelle certifiée (200 premiers mondes, 8 instants) : promue 0.000 ; plus grand log W -0.567
```

Lecture : le défaut n'est pas un mauvais réglage du pas (la ligne (a') remplace la descente exponentielle par le prédicteur
séquentiel de Krichevsky et Trofimov, proche de l'optimum : la copie est encore promue partout) ; il est dans la forme. La
construction retenue (c), celle du v8 et du v9, donne W ≤ 1 à la copie.

```python
"""Contre-exemples (processeur seul, aucun code du dépôt ; v3 : exposant borné à 50, prédicteur de
Krichevsky-Trofimov par cellule, contrôle (c) calculé avec certificat de Frank-Wolfe).
Monde = membre du nul composite « mélange, par cellule, de deux lois connues et des lois certaines δ_k » ;
carte = loi du monde elle-même (copie exacte). Une valeur e valide pour ce nul vaut au plus 1.
(a) nul appris en ligne par descente exponentielle (argon-p2-01), pas η ;
(a') nul appris en ligne par le meilleur prédicteur séquentiel simple (Krichevsky-Trofimov par cellule) ;
(b) nul ajusté par maximum de vraisemblance sur la première moitié, valeur e sur la seconde (argon-p1-01) ;
(c) inférence universelle : maximum de vraisemblance du même nul sur les mêmes tirages, plus l'écart de Frank-Wolfe.
"""
import numpy as np

K, CELLULES, N, ALPHA, R = 3, 4, 200, 0.05, 1000
INSTANTS = np.arange(25, N + 1, 25)
PLANCHER = 1e-12
SEUIL = np.log(1 / ALPHA)


def monde(rng):
    L = [rng.dirichlet(np.ones(K), size=CELLULES) for _ in range(2)]
    B = np.zeros((CELLULES, 2 + K, K))
    B[:, 0, :], B[:, 1, :] = L
    for k in range(K):
        B[:, 2 + k, k] = 1.0
    w = rng.dirichlet(np.ones(2 + K), size=CELLULES)
    P = np.einsum("cj,cjk->ck", w, B)
    cel = rng.integers(0, CELLULES, size=N)
    y = np.minimum((rng.random(N)[:, None] > np.cumsum(P[cel], axis=1)).sum(axis=1), K - 1)
    return B, P, cel, y


def en_ligne(B, P, cel, y, eta):
    w = np.full((CELLULES, 2 + K), 1.0 / (2 + K))
    lw, s = np.empty(N), 0.0
    for t in range(N):
        c, yt = cel[t], y[t]
        comp = B[c, :, yt]
        p = max(PLANCHER, float(w[c] @ comp))
        s += np.log(P[c, yt]) - np.log(p)
        lw[t] = s
        w[c] *= np.exp(np.minimum(eta * comp / p, 50.0))
        w[c] /= w[c].sum()
    return lw


def kt(B, P, cel, y):
    n = np.zeros((CELLULES, K))
    lw, s = np.empty(N), 0.0
    for t in range(N):
        c, yt = cel[t], y[t]
        p = (n[c, yt] + 0.5) / (n[c].sum() + 0.5 * K)
        s += np.log(P[c, yt]) - np.log(p)
        lw[t] = s
        n[c, yt] += 1
    return lw


def em_certifie(G, iterations=3000):
    """max_v Σ log(G v) sur le simplexe ; rend la valeur + écart de Frank-Wolfe (borne haute du maximum)."""
    t, J = G.shape
    v = np.full(J, 1.0 / J)
    for _ in range(iterations):
        m = np.maximum(G @ v, PLANCHER)
        g = G.T @ (1 / m)
        if g.max() - t < 1e-7:
            break
        v = v * g / t
        v /= v.sum()
    m = np.maximum(G @ v, PLANCHER)
    ecart = max(0.0, float((G.T @ (1 / m)).max() - t))
    return min(0.0, float(np.log(m).sum()) + ecart)


def moitie(B, P, cel, y):
    h = N // 2
    wm = np.full((CELLULES, 2 + K), 1.0 / (2 + K))
    for c in range(CELLULES):
        idx = np.where(cel[:h] == c)[0]
        if len(idx):
            G = B[c][:, y[idx]].T
            v = wm[c].copy()
            for _ in range(400):
                v = v * (G.T @ (1 / np.maximum(G @ v, PLANCHER))) / len(idx)
                v /= v.sum()
            wm[c] = v
    p2 = np.maximum(np.einsum("tj,tj->t", wm[cel[h:]], B[cel[h:], :, y[h:]]), PLANCHER)
    return np.cumsum(np.log(P[cel[h:], y[h:]]) - np.log(p2))


def universelle(B, P, cel, y):
    sortie = []
    for t in INSTANTS:
        num = float(np.log(P[cel[:t], y[:t]]).sum())
        den = sum(em_certifie(B[c][:, y[:t][cel[:t] == c]].T) for c in range(CELLULES) if (cel[:t] == c).any())
        sortie.append(num - den)
    return np.array(sortie)


def main():
    racine = np.random.SeedSequence(20261115)
    mondes = [monde(np.random.default_rng(s)) for s in racine.spawn(R)]
    for eta in (0.05, 0.2, 1.0):
        lws = [en_ligne(*m, eta) for m in mondes]
        fin = np.array([lw[-1] for lw in lws])
        print(f"(a) en ligne, eta={eta} : promue (instants 25..200) {np.mean([lw[INSTANTS - 1].max() >= SEUIL for lw in lws]):.3f} ; "
              f"log W final médian {np.median(fin):.2f}")
    lk = [kt(*m) for m in mondes]
    fk = np.array([l[-1] for l in lk])
    print(f"(a') Krichevsky-Trofimov par cellule : promue (instants 25..200) {np.mean([l[INSTANTS - 1].max() >= SEUIL for l in lk]):.3f} ; "
          f"log W final médian {np.median(fk):.2f} ; part log W final > 0 : {np.mean(fk > 0):.3f}")
    l2 = [moitie(*m) for m in mondes]
    f2 = np.array([l[-1] for l in l2])
    print(f"(b) moitié : promue en fin de seconde moitié {np.mean(f2 >= SEUIL):.3f} ; lecture continue {np.mean([l.max() >= SEUIL for l in l2]):.3f} ; "
          f"log W médian {np.median(f2):.2f}")
    lu = [universelle(*m) for m in mondes[:200]]
    mx = max(float(l.max()) for l in lu)
    print(f"(c) inférence universelle certifiée (200 premiers mondes, 8 instants) : promue {np.mean([l.max() >= SEUIL for l in lu]):.3f} ; "
          f"plus grand log W {mx:.3g}")


if __name__ == "__main__":
    main()
```

**8.4 Alternatives valides.** (i) Celle retenue : maximum de vraisemblance certifié du nul limité sur les tirages mêmes (v8,
v9). (ii) Une valeur e par pas contre l'enveloppe convexe du nul (projection d'information inverse) serait valide sans
ajustement sur les issues, mais changerait la forme de la valeur e du juge : écart, nœud, non proposée ici. Piste de
lecture seulement (Grünwald, de Heide et Koolen, « Safe testing », Journal of the Royal Statistical Society B, 2024 ; non
versée, non lue sur PDF : aucune affirmation n'en dépend).

## 9. Écarts et nœuds

- **Le banc** ne change ni le juge de production (nul v8, R-1779) ni le v9 : aucun écart à une conception scellée.
- **Adopter La, La2 ou Ld comme nul du juge** = version neuve du nul (v10) : **modification du juge, nœud de Lazar**. C'est
  l'option « chercher un nul moins coûteux » du nœud ouvert par R-1779 ; elle exigerait sa propre validation scellée, comme
  le v9 (`54c5713d…`).
- **Correction à porter au relevé** (non un nœud) : le relevé (`bd253b6c…`, § 1.1 et § 7, point 1) présente la variante (c)
  « à poids appris en ligne » comme la partie la plus neuve. Cette partie n'est pas valide (section 8) ; ce qui reste valide
  et neuf dans ce dépôt est la **restriction de la liste des partitions**, sous la construction existante.
- **Question de sens** (R-1768, R-1779 : une copie « S1 sur une sous-population, S2 sur l'autre » est-elle une découverte ?),
  ouverte : la lecture de La contre Ld en dépend (Ld ferme cette copie, La non).
- **Copie du code du v9** dans le dépôt : préalable du banc, non faite par moi (section 1) ; décision de la mère ou mot de
  Lazar, sur le modèle de R-2148 (copie empreintée versée par la session-dépôt).

## 10. Vérifications faites

**(a) Lemme du certificat (section 3).** 300 jeux tirés au hasard (3 issues, 3 lois connues, 4 cellules, 20 à 119 épisodes) ;
valeur + écart de Frank-Wolfe après 5, 50 et 2 000 pas, comparés à un optimum calculé à part (SLSQP, huit départs). Sortie
(`2674c65b346010971066ef9aeb26ac9532996dbc10face4554d52cadbfe4630b`, script `cd529082536dbabadea882e3000830ff732c78ca4892cda14ff74b01de8deea5`) :

```
    5 pas de Frank-Wolfe : valeur + écart sous l'optimum de référence dans 0 jeux sur 300 ; marge minimale 0.322 nat
   50 pas de Frank-Wolfe : valeur + écart sous l'optimum de référence dans 0 jeux sur 300 ; marge minimale 0.0279 nat
 2000 pas de Frank-Wolfe : valeur + écart sous l'optimum de référence dans 0 jeux sur 300 ; marge minimale 0.00201 nat
```

La marge reste positive (validité) et décroît avec les pas (prix en puissance d'un certificat lâche). Script en entier :

```python
"""Vérification numérique du lemme de certificat (processeur seul, sans code du dépôt) : membre par morceaux
p(y|x) = Σ_j μ_{c(x),j} L_j(y|x) + Σ_k ρ_k 1[y=k], μ, ρ ≥ 0, Σ_j μ_{c,j} + Σ_k ρ_k = 1 pour chaque cellule c.
f(μ, ρ) = Σ_s log p(y_s|x_s) est concave ; l'écart de Frank-Wolfe g = max_sommet ∇f·v − ∇f·x borne f* − f(x).
Sommets du polytope : ρ = e_k (μ = 0) ; ou ρ = 0 et μ_c = e_{j_c} pour chaque c. On compare f(x) + g à un optimum
calculé à part (SLSQP, nombreux départs) sur 300 jeux tirés au hasard, après 5, 50 et 2000 pas de Frank-Wolfe."""
import numpy as np
from scipy.optimize import minimize

K, J, C = 3, 3, 4

def tirer(rng, n):
    L = rng.dirichlet(np.ones(K), size=(n, J))          # L_j(·|x_s) : (n, J, K)
    cel = rng.integers(0, C, size=n)
    y = rng.integers(0, K, size=n)
    A = np.zeros((n, C * J + K))                         # a_s · x = p(y_s|x_s)
    for s in range(n):
        A[s, cel[s] * J:(cel[s] + 1) * J] = L[s, :, y[s]]
        A[s, C * J + y[s]] = 1.0
    return A, cel

def f(A, x):
    return float(np.log(np.maximum(A @ x, 1e-300)).sum())

def grad(A, x):
    return A.T @ (1.0 / (A @ x))

def sommet_max(gr):
    # meilleur sommet pour la forme linéaire gr : ρ = e_k, ou μ_c = e_{argmax_j} dans chaque cellule
    best_rho = gr[C * J:].max()
    best_mu = sum(gr[c * J:(c + 1) * J].max() for c in range(C))
    v = np.zeros_like(gr)
    if best_rho >= best_mu:
        v[C * J + int(gr[C * J:].argmax())] = 1.0
    else:
        for c in range(C):
            v[c * J + int(gr[c * J:(c + 1) * J].argmax())] = 1.0
    return v, max(best_rho, best_mu)

def fw(A, pas):
    x = np.zeros(C * J + K); x[:C * J] = 1.0 / J         # départ : mélange uniforme par cellule, ρ = 0
    x = 0.5 * x; x[C * J:] = 0.5 / K                     # point intérieur
    for it in range(pas):
        gr = grad(A, x)
        v, _ = sommet_max(gr)
        g = 2.0 / (it + 3.0)
        x = x + g * (v - x)
    gr = grad(A, x)
    _, m = sommet_max(gr)
    return f(A, x), max(0.0, m - float(gr @ x))

def optimum(A, rng, departs=8):
    nvar = C * J + K
    cons = [{"type": "eq", "fun": (lambda x, c=c: x[c * J:(c + 1) * J].sum() + x[C * J:].sum() - 1.0)} for c in range(C)]
    best = -np.inf
    for _ in range(departs):
        rho = rng.dirichlet(np.ones(K)) * rng.uniform(0.05, 0.9)
        x0 = np.concatenate([np.concatenate([rng.dirichlet(np.ones(J)) * (1 - rho.sum()) for _ in range(C)]), rho])
        r = minimize(lambda x: -f(A, np.maximum(x, 1e-12)), x0, method="SLSQP", bounds=[(0, 1)] * nvar,
                     constraints=cons, options={"maxiter": 500, "ftol": 1e-12})
        if r.success:
            best = max(best, f(A, np.maximum(r.x, 1e-12)))
    return best

rng = np.random.default_rng(np.random.SeedSequence(20261115))
viol = {5: 0, 50: 0, 2000: 0}; marge_min = {5: np.inf, 50: np.inf, 2000: np.inf}; N = 300
for _ in range(N):
    A, _ = tirer(rng, int(rng.integers(20, 120)))
    fopt = optimum(A, rng)
    for pas in viol:
        val, ecart = fw(A, pas)
        marge = val + ecart - fopt
        marge_min[pas] = min(marge_min[pas], marge)
        if marge < -1e-6:
            viol[pas] += 1
for pas in viol:
    print(f"{pas:5d} pas de Frank-Wolfe : valeur + écart sous l'optimum de référence dans {viol[pas]} jeux sur {N} ; marge minimale {marge_min[pas]:.3g} nat")
```

**(b) Code lu.** Les modules de la section 1, sur la copie `94bfd92` (`sha256sum -c empreintes-copie-v1.txt` : 53 sur 53
conformes). **Non fait** : aucun banc, aucune lecture de `nul_v9.py` (absent), aucune course.

## 11. Contre-lecture à faire (R2)

Sous-agent neuf d'un autre modèle que l'auteur (modèle B au sens de R-2851), qui n'a écrit ni cette pièce, ni le
préenregistrement, ni le code du juge. Fichiers à lire, explicitement : cette pièce ; `prereg-nul-par-morceaux-limite-v1.md`
(même dossier) ; `selection_pari.py`, `nul_filles_v2.py`, `nul_v8.py`, `cycle.py` (fonctions `membres_de_l_archive`,
`appliquer_multiplicite`, `instants_reguliers`), `a_blanc_v59.py` (`juger_carte`) de la copie `94bfd92` ; la page publique
(`c549a31b…`, l. 55 à 66) ; et, si la copie en est versée, `nul_v9.py` (`7ae450df…`). Points à éprouver : H1 à H8 suffisent-elles ;
la famille de la section 3 est-elle bien celle du v9 (part aveugle commune ou par cellule) — de quoi dépend la section 6 (b) ;
les deux contre-exemples de la section 8 ; les remarques (ii) et la règle d'audit A1 qui en découle.

## Citations obligatoires (N-064, N-067)

POPPER (Huang et al., ICML 2025), `docs/sources/pdf/huang-2025-icml-pmlr-267-popper-automated-hypothesis-validation-agentic-sequential-falsifications.pdf`
(`a3c4b3701543a84a74602ae46a624b955e201bb83baeea2c219213a0e65b4998`) ; Dwork et al., arXiv 1506.02629 (2015),
`docs/sources/pdf/anteriorite-P-041-v2/c8/1506.02629.pdf` (`dcfbb9aa401c62949123be2d74787c4f9cca48597f18860760ef1580ddb4bc71`) ;
Blum et Hardt, « The Ladder », arXiv 1502.04585 (2015), `…/c8/1502.04585.pdf` (`957ef4739df371a0a778360f0db4252a62f7c85abcd8343f581cd6250b1d31fe`) ;
Co-Scientist (Gottweis et al., Nature 655, p. 487-496, 2026), `docs/sources/co-scientist-v1/gottweis-2026-nature-655-487-accelerating-scientific-discovery-with-co-scientist.pdf`
(`351f49d89d2f4f4ed84eed4225c09cc95470c41aa3becd0aa3e06b3bd8ba54c3`) ; et la liste de `docs/decisions/decision-N-067-v1.md`,
section 6, dont, sur ce point : Qu, Chen et Wang, « Propose, Don't Judge », arXiv 2609.27051 (`…/c8/2609.27051.pdf`,
`2a8ded0119a1db422aa548fdc3be80b2861f0548bc8166256be60572a2fddb03`, p. 1 : arbitre par paris dont la garantie tient à tout
temps d'arrêt) ; aucune revendication n'est faite ici (le nul formé des lois connues reste sous la clause d'usage public de
N-067).
