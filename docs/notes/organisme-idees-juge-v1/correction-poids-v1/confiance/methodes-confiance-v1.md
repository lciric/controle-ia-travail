# Poids du nul appris par ensemble de confiance, puis maximum sur cet ensemble (Berger et Boos) — v1

**Statut.** Mise au point exploratoire, **aucune revendication**. Rien n'est préenregistré ; aucun essai ne visait un
signe ; toutes les issues sont rapportées de la même façon, celles qui échouent comprises. Processeur seul, aucun appel
réseau ni payant, aucun commit. Toute adoption est une décision du directeur (section 9) : je la nomme, je ne la tranche pas.

- **Auteur** : concepteur neuf, sous-agent ; je n'ai écrit aucune des pièces citées ni le code du juge.
- **Date** : 2026-11-15, de 11:20 à 13:40 UTC environ (`date -u`) ; dépôt lu sur `main`, tête `e2bef750`.
- **Calculs** : Python 3.13.18, numpy 2.4.6, scipy 1.17.1 (`.venv/bin/python -I -B`), `nice -n 10`, trois processus au plus.

## 0. Ce que la note établit, en sept lignes

1. **Théorème BB** (section 3) : prendre le maximum du nul sur un ensemble de confiance C des poids, de niveau 1 − β, et
   lire le pari au niveau α − β, garde la taille α sur **toute** la classe du v9, que C soit construit sur n'importe quels
   tirages, y compris les tirages évalués. C'est la façon valide de « corriger » les deux façons des fiches.
2. **Lemme 1** : si C est construit sur les tirages évalués eux-mêmes, il contient le maximum de vraisemblance du nul dès
   qu'il n'est pas vide : **aucun gain possible**, seulement le prix β. Le gain demande des tirages de confiance disjoints.
3. **Taille mesurée** (1 000 mondes par cas obligatoire) : aucune méthode à ensemble de confiance ne promeut une copie
   exacte ni une carte hors classe dans un monde du nul (0 sur 1 000 partout ; non-couverture mesurée au plus 0,5 %, sous β).
4. **Artefact** : sur le même banc, la façon « en ligne » promeut une copie exacte dans 93,6 % à 100 % des mondes, la façon
   « moitié » dans 5,2 % à 31,8 % selon le cas obligatoire (nette dans les cas intérieur et bord, à la limite au sommet) ; le banc voit
   donc l'échec.
5. **Puissance avec les 100 tirages d'entraînement du juge** : gain nul ou minime (au mieux +3 points sur 500 mondes),
   souvent une perte (le prix β) ; la version « moitié des tirages frais » et la version séquentielle par blocs perdent
   beaucoup (−7 à −19 points).
6. **Puissance avec 1 000 tirages de confiance** (situation d'un juge qui tirerait plus d'entraînement, ou qui mettrait
   en commun les tirages des autres cartes de la génération) : l'ensemble coupé regagne 14 %, 42 % et 55 % du prix du v9
   aux trois doses, sans rien céder de la classe du v9 ; le nul limité en regagne plus (64 % à 76 %) mais laisse passer les
   copies coupées hors de l'archive (78,4 % sur la grille).
7. Une archive à six lois ne change pas le tableau (gain ≤ 4,5 points à 100 tirages de confiance).

## 1. Ce que j'ai lu (empreintes recalculées le 15 novembre, égales à leurs compagnons)

| pièce | chemin | empreinte |
|---|---|---|
| preuve de validité du nul limité | `docs/notes/organisme-idees-juge-v1/preuve-validite-nul-limite-v1.md` | `44f249409193778ccbaaa12b6c5e74d64434dfb87be77382d8bb9438459281b2` |
| préenregistrement de l'idée 1.1 (banc, lignes V1, bras) | `docs/notes/organisme-idees-juge-v1/prereg-nul-par-morceaux-limite-v1.md` | `46ef2b92119ee5dff05727b90ca8bdd3ba57b52f9c1c75893750c792a2abc089` |
| contre-lecture (échec refait) | `docs/notes/organisme-idees-juge-v1/contre-lecture-prereg-nul-limite-et-preuve-v1.md` | `763fc6e29cd80868dcdb1d848eafdc928a39fca7244fa16eb0ac721ec705014e` |
| code du nul v9 (lu, jamais exécuté) | `docs/notes/organisme-idees-juge-v1/copie-nul-v9-a41b7b5/orchestrator/pole/nul_v9.py` | `7ae450df2482246122bf9fbcf0fa5ef30b4a7e4c6f0d09531e83af048e46ee95` |
| pari, tirages frais ; membres ajustés, instants ; nul v8 ; jugement d'une carte (lus, jamais exécutés) | `docs/notes/organisme-courbe-dose-reponse-v1/code-organisme-94bfd92/orchestrator/pole/` : `selection_pari.py`, `nul_filles_v2.py`, `nul_v8.py`, `a_blanc_v59.py` | empreintes de la liste `empreintes-copie-v1.txt` de la copie (non recalculées une à une ici) |
| relevé d'idées, § 1.1 | `docs/notes/organisme-conception-propre-v1/relecture-exploratoire-v2/releve-idees-reutilisables-v1.md` | `bd253b6c68f6baada0e61b5381f029b52838ca34aa092502e55253c662451c6c` |
| fiches argon-p1-01 (n° 0), argon-p2-01 (n° 14), opus-p1-05 (n° 9), fable-p1-05 (n° 13) | `runs/course-ideation-conception-propre-v1/20261113-235541-course-ideation-conception-propre-v1-g1/copies/sortie--fiches-validees.json` | `a9f9594e2dc3a7a553c54577202817758e3f7ef231445f1a48d500fc647389d5` |
| verdict de la validation du v9 (« puissance perdue ») | `docs/verdicts/verdict-validation-nul-v9-v1.md` (seul fichier ouvert dans ce dossier, par son chemin exact) | `1407e460367754bb9f76b37174f3a21585970864eb9beaa2699494d90125c1ea` |

Ce que « puissance perdue » veut dire (verdict, « En tête » et « Lecture selon la section 7 ») : le v9 tient sa taille
(18 lignes fatales tenues), mais sur la ligne I02 (interaction faible hors de l'archive) sa puissance appariée est
inférieure à celle du v8 de 0,105, plus du double de la marge de 0,05 ; c'est le prix du nul plus large. La question de
cette note : regagner ce prix sans perdre la taille, en « apprenant les poids » d'une façon valide.

Ce que disent les fiches (champ `demande_organisme`) : argon-p1-01 (n° 0) ajuste les poids par morceau « par maximum de
vraisemblance sur la première moitié des tirages frais » et évalue la valeur e sur la seconde ; argon-p2-01 (n° 14) met à
jour les poids en ligne par descente exponentielle. opus-p1-05 et fable-p1-05 élargissent la classe (grille de déciles,
mélange à poids fixes) sans apprendre de poids.

## 1 bis. Le banc (simplifications déclarées ; le banc n'est pas le juge)

Code : `essai_confiance_banc_v1.py` (`3490044a4d21872f0ebf5193b1c19b19e3a9975da4069c73f882ee69117aecc9`). La logique
utile du juge y est **recopiée et simplifiée** d'après la lecture de `nul_v9.py` et des fichiers de la copie `94bfd92` ;
aucun fichier des dossiers de copie n'est exécuté ni importé.

- K = 3 issues, deux traits z ~ N(0, 1) (six décimales), une sous-population g ∈ {0, 1} ; n = 200 tirages frais ; instants
  T = {25, …, 200} ; α = 0,05 ; pari plein (numérateur = loi de la carte) ; 100 instances d'entraînement tirées du monde,
  comme `a_blanc_v59.juger_carte` (variante à 1 000).
- Lois connues : S1, S2 softmax (poids N(0 ; 1,5²), biais N(0 ; 0,3²)), S3 = si_sinon(z_jA > s_A, U1, U2) ; à J = 6, plus
  S4, S5 et S6 = si_sinon(z_(1−jA) > s_B, U3, U4).
- Nul : les familles « mélange des lois connues par morceau + bruit aveugle commun » de `nul_v9.py`, sur les partitions :
  aucune (le membre linéaire, **« v8 du banc »**), sous-population, coupure(s) de l'archive, et **une grille fixe de neuf
  seuils par trait** (déciles de N(0, 1)) au lieu de tout seuil réel (**« v9 du banc »**). **« Limité »** : aucune + coupures
  de l'archive. Les membres log-linéaires et ordinaires du v8 sont absents (les ordinaires sont des cas particuliers du bruit
  aveugle). Conséquence : le prix du v9 du banc est **sous** celui du vrai v9 (moins de coupures à surajuster).
- Maximum certifié : EM multiplicatif (80 pas, départ chaud d'un instant au suivant), puis écart de Frank-Wolfe, borné par 0,
  comme `nul_v9.py` ; la valeur rendue est toujours un majorant, quel que soit l'optimiseur. Les trois références et toutes
  les méthodes utilisent le même optimiseur ; λ = 0 dans le calcul contraint rend exactement la valeur du v9 du banc.
- Graines (R9) : `numpy.random.SeedSequence(entropy=2026111531, spawn_key=(indice du cas, J, indice du monde))`, un
  générateur par monde, tirages frais d'abord puis entraînement : **mêmes tirages frais et mêmes instants pour toutes les
  méthodes**, et pour n_tr = 100 et 1 000. Chaque sortie écrit sa racine, sa dérivation et ses `spawn_key`.
## 2. Notations (celles du code du juge, simplifiées comme dans le banc)

- **Carte** : loi prédictive q, gelée avec le plan x_1..x_n (n = 200), les instants de lecture T = {25, 50, …, 200}
  (`cycle.instants_reguliers(200, 8)`) et α = 0,05, avant les **tirages frais** y_1..y_n (`selection_pari.tirer_frais`).
- **Nul** : 𝒩 = ∪_P F_P. Une **partition** P (aucune, sous-population, coupure de l'archive, coupure de la grille) a au
  plus deux morceaux ; la **famille** F_P est l'ensemble des lois
  p_θ(y | x) = (1 − ρ)·Σ_j b_{c(x), j}·L_j(y | x) + ρ·r̃(y), θ = (P, ρ, r̃, b), où L_1..L_J sont les **membres de
  l'archive** (lois connues), b_c un poids par morceau, r̃ une loi aveugle **commune** aux morceaux et ρ sa part : c'est la
  famille des membres « morceaux » de `nul_v9.py` (a^P_j = (1 − ρ) b_{c,j}, r = ρ r̃).
- **Log-vraisemblance** : ℓ_t(θ) = Σ_{s ≤ t} log p_θ(y_s | x_s) ; pour un jeu de tirages Z quelconque, ℓ_Z(θ).
- **Maximum certifié** (façon nul v9) : D_t ≥ sup_{θ ∈ 𝒩} ℓ_t(θ), par EM puis écart de Frank-Wolfe, borné par 0.
- **Richesse et pari** : log W_t = log q(y_1..t) − D_t ; **promotion** s'il existe t ∈ T avec log W_t ≥ log(1/α).
- **Ensemble de confiance** : C, partie de l'ensemble des θ, construite par une règle fixée d'avance à partir de tirages
  Z_c (« tirages de confiance »). **Méthode de Berger et Boos** : remplacer D_t par D_t^C ≥ sup_{θ ∈ C} ℓ_t(θ)
  (−∞ si C est vide) et lire au niveau α' = α − β.

## 3. Le théorème commun et le lemme qui borne le gain

**Hypothèses** (numérotées comme celles de la preuve du nul limité, plus B1 à B3) :
- H1 (gel) : q, le plan, T, et la **règle** de construction de C sont fixés avant les tirages frais (C lui-même dépend des
  tirages de confiance) ;
- H2 (fraîcheur) : les tirages frais sont tirés après le gel ; q(· | x_s, y_<s) est prévisible ;
- H3 (monde dans la classe) : la loi du monde est p_θ* pour un θ* du nul, sans mémoire ;
- H4 (certificat) : D_t^C ≥ sup_{θ ∈ C} ℓ_t(θ) sur toute trajectoire ;
- H5 (plancher) : q ≥ 10⁻¹² ;
- H6 (ordre) : sachant les instances, les issues sont indépendantes, y_s ~ p_θ*(· | x_s) ;
- H7, H8 : instants fixés d'avance, une seule règle de lecture ;
- **B1 (couverture)** : pour tout θ* du nul, P_θ*(θ* ∈ C) ≥ 1 − β ;
- B2 (pour les versions séquentielles) : couverture **simultanée** à tous les blocs : P_θ*(θ* ∈ C_b pour tout b) ≥ 1 − β ;
- B3 (certificat contraint) : voir le lemme 2.

**Théorème BB.** Sous H1 à H8 et B1 (ou B2), P_θ*(il existe t ∈ T : log q(y_1..t) − D_t^C ≥ log(1/α')) ≤ α' + β = α.

*Preuve.*
1. Soit E = {θ* ∈ C}. Sur E, pour tout t : D_t^C ≥ sup_{θ ∈ C} ℓ_t(θ) ≥ ℓ_t(θ*) (H4). Cette domination est
   **trajectoire par trajectoire** : elle ne demande aucune indépendance entre C et les tirages évalués.
2. Donc, sur E, W_t ≤ Λ_t = Π_{s ≤ t} q(y_s | ·) / p_θ*(y_s | x_s).
3. Λ est une surmartingale positive de valeur 1 sous θ* (H2, H5, H6 : E[q(y_t | ·)/p_θ*(y_t | x_t) | passé] ≤ 1) ;
   Ville : P(il existe t : Λ_t ≥ 1/α') ≤ α'.
4. P(promotion) ≤ P(non E) + P(E et il existe t ∈ T : Λ_t ≥ 1/α') ≤ β + α'. ∎

Pour la version par blocs, l'étape 1 se fait bloc par bloc : sur E = {θ* ∈ C_{b−1} pour tout b}, chaque terme
sup_{C_{b−1}} ℓ_{bloc b} domine ℓ_{bloc b}(θ*), et la somme domine ℓ_t(θ*).

**Lemme 1 (pas de gain sans tirages disjoints).** Si C est construit sur les tirages évalués eux-mêmes sous la forme
C_t = {θ : ℓ_t(θ) ≥ κ_t} (tout ensemble « de rapport de vraisemblance », dont la suite de confiance séquentielle
κ_t = log m_t − log(1/β)), alors : ou bien C_t est vide, ou bien il contient le maximum de vraisemblance du nul sur ces
tirages, et sup_{C_t} ℓ_t = sup_𝒩 ℓ_t.
*Preuve.* Si θ ∈ C_t, le maximiseur θ̂ vérifie ℓ_t(θ̂) ≥ ℓ_t(θ) ≥ κ_t, donc θ̂ ∈ C_t. ∎
Conséquence : la seule différence avec le v9 est la règle « ensemble vide ⇒ promue », et le prix β. Si m = q (la carte),
la promotion devient « W_t ≥ 1/max(α', β) », plus dure que « W_t ≥ 1/α » : **strictement moins puissant que le v9**. Si m
est un autre prédicteur, la carte est promue parce que m bat le nul, et non parce que q le bat : la règle change de sens.
**Le gain demande donc des tirages de confiance disjoints des tirages évalués** ; et il n'existe que si le maximum de
vraisemblance des tirages évalués tombe hors de C.

**Lemme 2 (maximum certifié sur l'ensemble).** Pour une famille F_P, C = {θ : ℓ_c(θ) ≥ κ} et tout λ ≥ 0 :
sup_{θ ∈ F_P ∩ C} ℓ_e(θ) ≤ sup_{θ ∈ F_P} [ℓ_e(θ) + λ ℓ_c(θ)] − λκ ≤ FW(ℓ_e + λ ℓ_c) − λκ,
où FW est le certificat de Frank-Wolfe du problème pondéré (concave, poids ≥ 0 ; grad·u = somme des poids par
homogénéité ; sommets du polytope : une loi connue par morceau, ou ρ r̃ = δ_k). Si FW(ℓ_c) < κ, F_P ∩ C est vide.
*Preuve.* Sur F_P ∩ C, ℓ_c − κ ≥ 0 ; la seconde inégalité est le certificat de Frank-Wolfe (concavité). ∎
On prend le minimum sur λ ∈ {0 ; 0,3 ; 1 ; 3} × n_e/n_c : λ = 0 rend la valeur du v9, la méthode n'est donc **jamais
moins puissante que le v9 au même niveau** — elle l'est seulement par le prix β.

**Constructions de C, valides en fini (aucune asymptotique).**
- **Ensemble séquentiel** (« préquentiel ») : on range les tirages de confiance z_1..z_N dans un ordre fixé, on prend un
  prédicteur prévisible m(z_k | z_<k) (ici : le meilleur membre ajusté sur les tirages précédents, réajusté tous les 25,
  lissé à 0,2 % vers l'uniforme), et C = {θ : ℓ_Z(θ) ≥ Σ_k log m(z_k | z_<k) − log(1/β)}. Couverture : Π m/p_θ* est une
  martingale de test sous θ*, Ville donne P(il existe k : Π m/p_θ* ≥ 1/β) ≤ β ; la couverture est **valide à tout instant**
  (c'est la suite de confiance de la version par blocs). C'est la place où des **poids appris en ligne** deviennent
  valides : dans l'ensemble, non dans la valeur e.
- **Ensemble universel coupé** : Z = (Z1, Z2) ; m̃ = meilleur membre ajusté sur Z1 (lissé) ;
  C = {θ : ℓ_{Z2}(θ) ≥ log m̃(Z2) − log(1/β)}. Couverture : Markov sur E[m̃(Z2)/p_θ*(Z2) | Z1] ≤ 1. C'est la place où les
  **poids ajustés sur une moitié** deviennent valides : la moitié sert à centrer l'ensemble, pas à remplacer le nul.

**Ordre de grandeur du gain (heuristique, non démontré).** Le rayon de C, compté en log-vraisemblance sur les tirages de
confiance, vaut environ le regret du prédicteur plus log(1/β) (ensemble séquentiel, de l'ordre de (d/2)·log n_c pour d
paramètres libres), ou (d/2)(1 + n2/n1) + log(1/β) (ensemble coupé). Ramené aux tirages évalués, il est multiplié par
n_e/n_c. Le surajustement du v9 sur les tirages évalués est de l'ordre de d/2 plus le prix de la recherche sur les
coupures. L'ensemble ne « mord » que si n_c est grand devant n_e : avec les 100 tirages d'entraînement du juge
(n_c = 100 < n_e = 200), on attend un gain presque nul ; avec n_c = 1 000, un gain partiel. Quand l'archive compte plus
de lois, d croît des deux côtés : on n'attend pas de changement du rapport, et on le mesure (J = 6).

## 4. Les méthodes étudiées (énoncé, validité, coût, ce qu'elles changeraient)

Toutes sont calculées dans `essai_confiance_methodes_v1.py` (`c8b5021b934a89e6a09bfb5d8efad7289799864eb08155c2e33f5d27484e1848`),
à deux valeurs de β (0,01 et 0,025 ; pari lu au seuil log(1/(α − β))). Le majorant contraint (lemme 2) est vérifié à part
(section 4.0). Les chiffres de taille, de puissance et de coût sont aux sections 5 à 8.

### 4.0 Vérification du lemme 2

`essai_confiance_certificat_v1.py` (`7b51877c23b58a47fd0f522ec93790adfeef9a709982d2312a896a0bd47a9003`), sortie
`sorties/certificat-v1.json` (`0bfe3a97d96eb7cff18ee7e452cb5bf58fd5de8ff5a77df415cbc1ce8dd64779`) : 200 petits problèmes ×
4 seuils κ, comparés à un maximum contraint calculé à part (SLSQP, huit départs). **0 violation sur 600 cas faisables**, marge
minimale (borne − référence) 1,0·10⁻⁴ nat ; κ au-dessus du sup : famille déclarée vide 200 fois sur 200 ; la contrainte
abaisse le majorant de 1,90 nat en médiane (au plus 18,4).

### 4.1 BB_A — ensemble construit sur les tirages évalués eux-mêmes (suite de confiance séquentielle)

1. *Énoncé.* À chaque instant t ∈ T, C_t = {θ : ℓ_t(θ) ≥ Σ_{s ≤ t} log m(y_s | y_<s) − log(1/β)}, m = meilleur membre
   ajusté sur les tirages frais précédents (réajusté tous les 25), lissé ; dénominateur = maximum certifié sur C_t.
2. *Validité.* Théorème BB avec B2 (Ville sur Π m/p_θ*, couverture à tout instant). **Valide.** Par le lemme 1, le
   dénominateur vaut −∞ (C_t vide, promue) ou celui du v9 : la méthode ne peut que perdre (le prix β), sauf par la branche
   « vide », qui promeut parce que m bat le nul, non parce que la carte le bat.
3. *Taille* : 0 promotion partout (section 5). 5. *Puissance* : jamais une promotion que le v9 n'ait pas (« méthode seule »
   = 0 dans toutes les lignes), perte de 0 à 4 points à β = 0,01 et de 2 à 4 à β = 0,025. 6. *Coût* : celui du v9 plus un
   prédicteur séquentiel (≈ 0,04 s). 7. *Conception* : aucun intérêt à l'adopter ; écartée.

### 4.2 BB_T_seq — ensemble séquentiel sur les tirages d'entraînement

1. *Énoncé.* Tirages de confiance = les n_tr tirages d'entraînement (instances et issues tirées du monde, déjà tirés par le
   juge pour la marginale d'entraînement) ; C = {θ : ℓ_tr(θ) ≥ Σ_k log m(z_k | z_<k) − log(1/β)} ; dénominateur à chaque
   t ∈ T : min sur λ du majorant du lemme 2, sur toutes les partitions du v9 du banc ; famille vide ⇒ −∞.
2. *Validité.* Théorème BB, B1 par Ville. Les tirages d'entraînement sont disjoints des tirages frais ; la domination de
   l'étape 1 ne demande même pas cette indépendance. **Valide**, sur toute la classe du v9. Hypothèse en plus de H1 à H8 :
   l'entraînement est tiré du **même monde** (vrai dans `a_blanc_v59.juger_carte`, l. 169-170).
3. à 6. : sections 5 à 8. 7. *Conception* : C entre dans l'engagement (il est fixé avant les tirages frais) ; la valeur
   rendue n'est plus une valeur e (voir 9.2).

### 4.3 BB_T_coupe — ensemble universel coupé sur les tirages d'entraînement

1. *Énoncé.* Entraînement coupé en deux moitiés Z1, Z2 ; m̃ = meilleur membre ajusté sur Z1, lissé ;
   C = {θ : ℓ_{Z2}(θ) ≥ log m̃(Z2) − log(1/β)} ; dénominateur comme 4.2.
2. *Validité.* Théorème BB, B1 par Markov conditionnellement à Z1. **Valide.** C'est la correction exacte de la fiche
   argon-p1-01 : la moitié sert à **centrer un ensemble** qui contient le vrai θ* avec probabilité ≥ 1 − β, au lieu de
   **remplacer** le nul par un point ajusté qui n'est jamais θ*.
3. à 6. : sections 5 à 8. 7. *Conception* : comme 4.2.

### 4.4 BB_S_moitie — une part des tirages frais pour l'ensemble, l'autre pour le pari

1. *Énoncé.* m̃ ajusté sur l'entraînement ; C = {θ : ℓ_{y_1..100}(θ) ≥ log m̃(y_1..100) − log(1/β)} ; pari sur
   y_101..t seulement, lu aux instants 125 à 200 : log W_t = log q(y_101..t) − majorant de sup_C ℓ_{y_101..t}.
2. *Validité.* Théorème BB appliqué à la seconde moitié (Λ commence à l'instant 100). **Valide.**
3. à 6. : sections 5 à 8. **Échoue en puissance** : la moitié du pari est perdue, et l'ensemble construit sur 100 tirages
   ne compense pas. 7. *Conception* : instants de lecture changés (quatre au lieu de huit) ; écartée.

### 4.5 BB_Q_blocs — version séquentielle prévisible (suite de confiance valide à tout instant)

1. *Énoncé.* Pour chaque bloc b de 25 tirages frais, C_{b−1} = {θ : ℓ(θ) ≥ Σ log m − log(1/β)} sur la suite
   « entraînement puis blocs 1..b−1 » (même prédicteur séquentiel) ; dénominateur à t = 25·b :
   Σ_{b' ≤ b} majorant de sup_{C_{b'−1}} ℓ_{bloc b'} ; lu aux 8 instants du juge.
2. *Validité.* Théorème BB avec B2 : la couverture simultanée de tous les C_b vient de Ville sur une seule martingale.
   **Valide.**
3. à 6. : sections 5 à 8. **Échoue en puissance** : un maximum par bloc paie le surajustement huit fois (chaque bloc a son
   propre maximum), ce que l'ensemble ne compense pas. 7. *Conception* : forme du dénominateur changée ; écartée.

### 4.6 Choix de β

β entre deux fois : dans le seuil du pari (log(1/(α − β)) : 3,22 nat à β = 0,01 ; 3,69 nat à β = 0,025, contre 3,00) et
dans le rayon de l'ensemble (+ log(1/β) : 4,6 nat ou 3,7 nat). Mesuré : β = 0,01 donne un taux de promotion
supérieur ou égal à celui de β = 0,025 dans les 9 groupes de puissance, pour chacune des cinq méthodes (45 comparaisons sur
45, `sorties/resume-v1.json`, section 7). Le rayon dépend peu de β (log), le seuil du pari beaucoup plus : un β petit
est préférable. Le choix de β doit être fixé avant les tirages (H1) ; le choisir au vu d'un banc pour la production est une
décision de dessin, sans effet sur la garantie par carte.

### 4.7 Artefacts : les deux façons des fiches, sur le même banc

- **F1_en_ligne** (argon-p2-01) : poids par morceau sur les J lois connues et les K lois certaines, appris en ligne par
  descente exponentielle (pas 0,05), sur **la partition du monde lui-même** (le cas le plus favorable à la fiche) ;
  log W_t = Σ log q − Σ log p_{w_{s−1}}. *Raison de l'échec* : [PREUVE] § 8.1 — E_θ*[q/p_w] = Σ P*²/p_w ≥ 1 pour une copie ;
  log W est le regret du prédicteur, qui croît.
- **F2_moitie** (argon-p1-01) : poids de la famille du monde ajustés au maximum de vraisemblance sur y_1..100, valeur e sur
  y_101..t, lue aux instants 125 à 200. *Raison de l'échec* : [PREUVE] § 8.2 — E[W | première moitié] ≥ 1 ; le point ajusté
  n'est pas θ*.

## 5. Taille (monde = membre du v9 du banc ; niveau du juge, 8 instants)

Source de tous les chiffres des sections 5 à 7 : `sorties/resume-v1.json`
(`ac6bd796164910e0111aa7cdd775145be8fee2e748e2af35e6ffd692de6eab11`), calculé par `essai_confiance_resume_v1.py`
(`8eb63830cafeb5a328cfbf8eeb0754d1ac08bd6463487f50beea67c5cdee2199`) sur les 64 lots `sorties/taille-*.json` et
`sorties/puissance-*.json` (empreintes en section 13 et dans le champ `sources` du résumé), produits par
`essai_confiance_lot_v1.py` (`d6b884582dac79428a3d16e903e2770a42a29281cac05044327532320f7899b9`). Intervalles : Clopper-Pearson
bilatéral à 95 %.

Cas (J = 3, n_tr = 100 sauf mention) : **intérieur** (partition aucune, poids de Dirichlet, ρ ~ U[0,05 ; 0,4]) ;
**sommet** (une seule loi connue, ρ = 0 : poids extrêmes) ; **bord** (coupure de la grille, ρ = 0, un morceau sur une arête du
simplexe, l'autre sur un sommet) ; **morceaux_archive** (si_sinon(z_jA > s_A, S1, S2) : copie par morceaux sur une coupure
de l'archive) ; **morceaux_grille**, **sous_population** (copies par morceaux hors de l'archive) ; **bruit_extreme**
(ρ = 0,95 sur une loi certaine). Cartes : **copie** (loi du monde) et **hors_classe** (0,7 monde + 0,3 softmax aléatoire).

**Taux de promotion des copies exactes** (sur `mondes`) :

| cas | mondes | toutes les méthodes BB (10 bras) | v9_banc | limite | v8_banc | F1_en_ligne | F2_moitie |
|---|---|---|---|---|---|---|---|
| intérieur | 1 000 | 0 [0 ; 0,0037] | 0 | 0 | 0 | 0,936 [0,919 ; 0,950] | 0,318 [0,289 ; 0,348] |
| sommet | 1 000 | 0 [0 ; 0,0037] | 0 | 0 | 0 | 1,000 [0,996 ; 1] | 0,052 [0,039 ; 0,068] |
| bord | 1 000 | 0 [0 ; 0,0037] | 0 | 0,527 | 0,712 | 0,999 [0,994 ; 1] | 0,203 [0,179 ; 0,229] |
| morceaux_archive | 1 000 | 0 [0 ; 0,0037] | 0 | 0 | 0,962 | 1,000 [0,996 ; 1] | 0,096 [0,079 ; 0,116] |
| morceaux_grille | 250 | 0 [0 ; 0,0146] | 0 | 0,784 | 0,932 | 1,000 | 0,108 |
| sous_population | 250 | 0 [0 ; 0,0146] | 0 | 0,948 | 0,976 | 1,000 | 0,044 |
| bruit_extreme | 250 | 0 [0 ; 0,0146] | 0 | 0 | 0 | 1,000 | 0,324 |
| intérieur, J = 6 | 250 | 0 [0 ; 0,0146] | 0 | 0 | 0 | 0,848 | 0,428 |
| intérieur, n_tr = 1 000 | 100 | 0 [0 ; 0,0362] | 0 | 0 | 0 | 0,900 | 0,300 |

**Cartes hors classe dans un monde du nul** : 0 promotion pour toutes les méthodes BB et pour v9_banc dans tous les cas
(F1 : 0,184 à 0,996 ; F2 : 0 à 0,192 ; limite et v8 promeuvent là où le monde est hors de leur classe, comme attendu).

**Non-couverture** (θ* hors de C, mesurée directement) : au plus 5 sur 1 000 (intérieur, BB_T_coupe et BB_S_moitie à
β = 0,025 ; borne haute 0,0116 < 0,025) ; au plus 1 sur 1 000 à β = 0,01 (borne haute 0,0056 < 0,01). **Audit A1** (copie
promue alors que l'ensemble la couvrait = défaut de certificat) : 0 dans tous les cas. La taille mesurée est nulle parce
qu'une copie hors de C n'est promue que si C exclut aussi tout ce qui l'explique aussi bien : l'inégalité du théorème est
large ici.

Lecture : les dix bras BB tiennent la taille sur toute la classe du v9 du banc, aux poids extrêmes, au bord du simplexe et
sur les copies par morceaux, y compris hors de l'archive (où le nul limité promeut 52,7 % à 94,8 % des copies).

## 6. Artefact : le banc voit-il l'échec des deux façons des fiches ?

Oui, nettement pour la façon en ligne, nettement pour la façon « moitié » dans les cas intérieur, bord et bruit extrême :
- F1_en_ligne promeut une **copie exacte** dans 93,6 % (intérieur) à 100 % (sommet, morceaux) des 1 000 mondes ;
- F2_moitie dans 31,8 % (intérieur, [0,289 ; 0,348]), 20,3 % (bord), 9,6 % (morceaux_archive) des 1 000 mondes, et
  32,4 % (bruit extrême, 250 mondes) ; **au sommet, 5,2 % [0,039 ; 0,068] : à la limite de α**, parce qu'un monde d'une
  seule loi se réajuste presque exactement sur 100 tirages. Je le rapporte tel quel : sur ce cas, le banc ne sépare pas
  nettement F2 de la taille nominale ; il la sépare sur les trois autres cas obligatoires.
- Ordre de grandeur cohérent avec la preuve (96,5 % à 100 % et 64,9 %) et la contre-lecture (98 % à 100 % et 37 % à 76 %) :
  mes mondes ont moins de paramètres libres (bruit commun, deux morceaux) que les leurs (quatre morceaux, bruit par morceau).

## 7. Puissance (vraies découvertes ; mêmes tirages frais, mêmes instants pour toutes les méthodes)

Monde : S1' = softmax(W1 + δ·Δ, b1), Δ ~ N(0, 1) centré sur les issues (ligne V1 du préenregistrement de l'idée 1.1),
δ ∈ {0,25 ; 0,50 ; 0,75} ; carte = loi du monde. Taux de promotion (β = 0,01 pour les bras BB ; la ligne β = 0,025 est dans
la sortie et toujours inférieure ou égale). « Repris » = (BB − v9) / (v8 − v9) : part du prix du v9 regagnée.

**J = 3, n_tr = 100 (les 100 tirages d'entraînement du juge), 500 mondes par dose**

| δ | v8_banc | v9_banc | limite | BB_T_seq | BB_T_coupe | BB_S_moitie | BB_Q_blocs | BB_A | repris (coupe) |
|---|---|---|---|---|---|---|---|---|---|
| 0,25 | 0,330 | 0,120 | 0,264 | 0,106 | 0,110 | 0,046 | 0,030 | 0,106 | −5 % |
| 0,50 | 0,728 | 0,424 | 0,650 | 0,436 | 0,448 | 0,270 | 0,234 | 0,416 | 8 % |
| 0,75 | 0,862 | 0,616 | 0,788 | 0,644 | 0,646 | 0,490 | 0,472 | 0,608 | 12 % |

Apparié contre v9_banc (méthode seule / v9 seul ; valeur p exacte des paires discordantes) : BB_T_coupe 2/7 (p = 0,18),
16/4 (p = 0,012), 19/4 (p = 0,0026) ; BB_T_seq 0/7, 10/4, 18/4 ; BB_S_moitie 8/45, 25/102, 38/101 ; BB_Q_blocs 0/45,
8/103, 17/89 ; BB_A 0/7, 0/4, 0/4.

**J = 3, n_tr = 1 000 (variante : plus de tirages de confiance), 200 mondes par dose (les 200 premiers des 500 : mêmes
tirages frais)**

| δ | v8_banc | v9_banc | limite | BB_T_seq | BB_T_coupe | BB_S_moitie | BB_Q_blocs | BB_A | repris (coupe) |
|---|---|---|---|---|---|---|---|---|---|
| 0,25 | 0,385 | 0,135 | 0,295 | 0,160 | 0,170 | 0,050 | 0,040 | 0,120 | 14 % |
| 0,50 | 0,680 | 0,395 | 0,610 | 0,445 | 0,515 | 0,240 | 0,280 | 0,395 | 42 % |
| 0,75 | 0,840 | 0,630 | 0,790 | 0,725 | 0,745 | 0,545 | 0,540 | 0,620 | 55 % |

Apparié BB_T_coupe contre v9_banc : 9/2 (p = 0,065), 24/0 (p < 10⁻⁶), 24/1 (p = 2·10⁻⁶) ; contre limite : 2/27, 3/22, 2/11.

**J = 6 (archive à six lois), n_tr = 100, 200 mondes par dose**

| δ | v8_banc | v9_banc | limite | BB_T_seq | BB_T_coupe | BB_S_moitie | BB_Q_blocs | BB_A | repris (coupe) |
|---|---|---|---|---|---|---|---|---|---|
| 0,25 | 0,260 | 0,040 | 0,145 | 0,035 | 0,035 | 0,010 | 0,000 | 0,035 | −2 % |
| 0,50 | 0,765 | 0,320 | 0,560 | 0,310 | 0,330 | 0,215 | 0,110 | 0,305 | 2 % |
| 0,75 | 0,835 | 0,410 | 0,665 | 0,440 | 0,455 | 0,325 | 0,270 | 0,410 | 11 % |

Lecture.
- Le **prix du v9 du banc** contre le v8 du banc est grand (21 à 30 points à J = 3, 22 à 45 points à J = 6) : il croît avec
  le nombre de lois de l'archive, comme attendu (plus de poids libres par morceau).
- **Avec 100 tirages de confiance**, l'ensemble ne mord presque pas (le rayon, ramené aux 200 tirages évalués, dépasse le
  surajustement du v9) : gain au mieux de 3 points, perte à la dose faible. Ce n'est pas une correction utile en l'état du
  juge.
- **Avec 1 000 tirages de confiance**, l'ensemble coupé regagne 14 % à 55 % du prix, croissant avec la dose, et reste
  sous le nul limité (qui, lui, ne garde pas la classe du v9).
- L'ensemble **coupé** fait mieux que l'ensemble **séquentiel** à chaque dose (le regret du prédicteur séquentiel élargit
  le rayon) ; les versions qui prennent des tirages frais (BB_S_moitie) ou qui maximisent bloc par bloc (BB_Q_blocs)
  perdent toujours.
- Une archive plus riche (J = 6) ne rend pas l'ensemble plus utile à 100 tirages : le rayon croît avec le nombre de
  paramètres, comme le surajustement.

## 8. Coût de calcul par carte

`essai_confiance_cout_v1.py` (`1fe2051d41cbdf83c1be251e648fc019296bd2b0789bdb2066d395da655470e9`) ; temps processeur moyen
par carte sur 10 mondes du cas intérieur, machine partagée (indicatif) ; `sorties/cout-ntr100-J3-v1.json`
(`d3a7168938b70e4b63f833c897408c623339faa675ccbca5159aa271c41e9baf`) et `sorties/cout-ntr1000-J3-v1.json`
(`b00dff4fc1a8c690f087dfb53c5be57bd3979183ba7409f2dc8a586d939b68fc`).

| méthode | n_tr = 100 | n_tr = 1 000 |
|---|---|---|
| v9_banc (référence, 8 instants) | 0,048 s | 0,049 s |
| prédicteur séquentiel (BB_T_seq, BB_Q) | 0,037 s | 0,39 s |
| BB_T_seq (8 instants, 4 valeurs de λ) | 0,21 s | 0,92 s |
| BB_T_coupe | 0,15 s | 0,45 s |
| BB_S_moitie | 0,073 s | 0,082 s |
| BB_Q_blocs | 0,26 s | 1,12 s |
| F1_en_ligne / F2_moitie | 0,002 s / 0,007 s | 0,003 s / 0,007 s |

Le surcoût d'un bras BB_T est de 3 à 20 fois le maximum certifié du banc ; sur le vrai v9 (toutes les coupures réelles, par
points intérieurs), le facteur serait du même ordre par valeur de λ (chaque λ est un problème du v9 sur des tirages pondérés),
donc environ quatre fois le coût du v9 pour quatre valeurs de λ. Le temps par monde des lots (toutes méthodes ensemble,
machine chargée) est dans le champ `secondes_par_monde` du résumé : 1,2 à 3,1 s à n_tr = 100, 4,9 à 6,7 s à n_tr = 1 000.

## 9. Ce que chaque méthode changerait à la conception scellée du juge (nœuds du directeur, non tranchés)

### 9.1 Changements communs à toute méthode BB
- **Version neuve du nul** (v10 ou suivante) : le dénominateur devient « maximum certifié du v9 sur un ensemble de
  confiance », avec sa preuve (section 3) et sa propre validation scellée, comme celle du v9.
- **Niveau du pari** : seuil log(1/(α − β)) au lieu de log(1/α) ; β fixé dans l'engagement.
- **Engagement** : la règle de C (tirages de confiance, prédicteur, β, grille de λ) entre dans l'empreinte ; C est calculé
  avant les tirages frais (pour BB_T).

### 9.2 La forme de la valeur e (règle e-BH de `cycle.appliquer_multiplicite`)
La méthode BB donne un **test** de niveau α' + β, **pas une valeur e** : hors de l'événement de couverture, W n'est pas
borné en espérance. Trois issues possibles, chacune une décision du directeur : (a) valeur e binaire e = 1[promue]/α
(espérance ≤ 1 si α' + β = α, mais très peu puissante sous e-BH quand m est grand) ; (b) valeur p = min(1, β + 1/W)
(valide : P(β + 1/W ≤ u) ≤ β + (u − β)) et règle de Benjamini et Hochberg sur valeurs p, qui demande une hypothèse de
dépendance ou la correction de Benjamini et Yekutieli ; (c) un β par seuil de e-BH (β_k pour le niveau αk/m), plus lourd.
Je n'ai mesuré aucune de ces trois formes : le banc ne juge qu'une carte à la fois.

### 9.3 BB_T_seq, BB_T_coupe avec les 100 tirages d'entraînement actuels
Changement minimal (l'entraînement existe déjà dans `a_blanc_v59.juger_carte`). **Gain mesuré presque nul** : je ne
recommande pas de l'adopter pour regagner la puissance du v9.

### 9.4 BB_T_coupe avec beaucoup plus de tirages de confiance (la seule voie qui regagne une part du prix)
Deux façons d'avoir ces tirages, chacune un changement de conception :
- **plus d'entraînement** tiré du monde (constante `ENTRAINEMENT` de 100 à 1 000 ou plus) : coût en tirages du monde ;
- **mise en commun des tirages frais des autres cartes de la même génération** (même monde, tirages disjoints de ceux de la
  carte jugée) : aucun tirage de plus, mais les jugements des cartes deviennent dépendants entre eux, ce qui touche la règle
  de multiplicité (9.2) ; la validité demande seulement que ces tirages viennent du même monde (la domination de l'étape 1
  ne demande pas l'indépendance) ; que le cycle réel les tire bien du même monde est à vérifier avant toute adoption.
Le banc ne mesure que la première (n_tr = 1 000) ; la seconde a la même statistique pour une carte seule.

### 9.5 BB_A, BB_S_moitie, BB_Q_blocs
Valides mais dominées ou perdantes : rien à adopter.

## 10. Options écartées (et pourquoi)

1. **Ensemble construit sur les tirages évalués** (BB_A et toute variante « de rapport de vraisemblance ») : lemme 1, aucun
   gain possible ; mesuré, jamais une promotion de plus que le v9.
2. **Ensemble de type « moments » sur les tirages évalués** (intervalles sur les fréquences par morceau) : il peut exclure
   le maximum de vraisemblance, mais seulement quand les tirages contredisent le nul ; la carte serait alors promue parce
   que le monde n'est pas dans le nul, non parce qu'elle le bat — change le sens de la promotion ; non codé.
3. **Prédicteur m autre que le nul dans la suite de confiance** (par exemple un modèle plus riche) : même défaut de sens
   (branche « ensemble vide » de BB_A) ; non codé.
4. **Ensemble sur l'indice de partition seul** (choisir les coupures plausibles sur l'entraînement) : cas particulier de
   BB_T (l'ensemble sur θ contient l'indice de partition) ; les familles sont emboîtées (la partition « aucune » est dans
   toutes), donc aucune coupure ne s'exclut sous un monde sans morceaux ; non codé à part.
5. **Ensembles asymptotiques** (rapport de vraisemblance au seuil du khi-deux) : exclus par la consigne (garantie en fini) et
   faux ici (paramètres au bord du simplexe, coupures discrètes).
6. **Maximum par instant sur un ensemble qui se resserre avec les tirages frais déjà lus** (C_t construit sur y_1..t et
   appliqué à y_1..t) : c'est BB_A (lemme 1). La seule forme séquentielle qui applique un ensemble à des tirages qu'il n'a pas
   vus est BB_Q_blocs, qui perd.
7. **Choisir β ou la méthode au vu de ce banc pour la production** : non fait ; ce serait une décision de dessin.

## 11. Déclarations et écarts de procédure

- **Pilotes avant les lots gardés** (3 à 5 mondes, dossier de travail de la session, non gardés) : ils ont fait changer, avant
  tout lot gardé, (a) le calcul (dénominateurs calculés une fois par monde pour toutes les cartes), (b) EM 150 → 80 pas et la
  grille de λ de 5 à 4 valeurs (vitesse), (c) le lissage du prédicteur 0,02 → 0,002 (il coûtait jusqu'à 0,02 nat par tirage
  au seuil κ, donc élargissait l'ensemble). Le changement (c) a été fait après avoir vu, sur 3 mondes de puissance, que
  l'ensemble ne mordait pas : c'est un réglage de la méthode au vu d'un pilote, déclaré ; il ne touche pas la validité
  (tout prédicteur prévisible convient).
- **Durée** : les trois premiers lots (intérieur, mondes 0 à 750, 250 mondes chacun) ont duré 763 à 772 s, au-delà de dix
  minutes, sous une charge de 12 à 14 sur 4 cœurs ; les trois lots suivants de 250 ont été arrêtés par leur numéro de
  processus au bout d'une minute (sans sortie), et tous les lots suivants ont été réduits à 125 mondes (50 à n_tr = 1 000,
  100 à J = 6) : 128 à 302 s chacun.
- **Mondes réduits** (dit, pour tenir le temps) : 250 mondes au lieu de 1 000 pour morceaux_grille, sous_population,
  bruit_extreme et intérieur à J = 6 ; **100 mondes** pour intérieur à n_tr = 1 000 ; 200 mondes par dose pour la puissance
  à n_tr = 1 000 et à J = 6. Les quatre cas obligatoires (copie intérieure, poids extrêmes, bord, copie par morceaux sur une
  coupure de l'archive) ont 1 000 mondes.
- **Le banc n'est pas le juge** (section 1 bis) : grille de neuf coupures au lieu de toutes ; pas de membres log-linéaires ;
  bruit commun recopié de `nul_v9.py` ; prédicteurs et EM à moi. Les chiffres valent pour ce banc seulement.

## 12. Références (toutes « à vérifier sur pièce » ; aucun chiffre n'en est repris)

- R. L. Berger et D. D. Boos, « P values maximised over a confidence set for the nuisance parameter », Journal of the
  American Statistical Association, 1994 — idée de base (maximum sur un ensemble de confiance, prix β) ; à vérifier sur pièce.
- L. Wasserman, A. Ramdas, S. Balakrishnan, « Universal inference », PNAS, 2020 — ensemble universel coupé et ensemble par
  maximum courant ; cité par `nul_v8.py` ; à vérifier sur pièce.
- J. Ville, 1939 (inégalité pour les martingales positives) ; à vérifier sur pièce.
- R. Wang et A. Ramdas, 2022, règle e-BH (citée par `cycle.py`) ; à vérifier sur pièce.
- S. R. Howard, A. Ramdas et coauteurs, suites de confiance valides à tout instant (2021) ; à vérifier sur pièce.
- P. Grünwald, R. de Heide, W. Koolen, « Safe testing », 2024 (cité par la preuve, § 8.4, non lu) ; à vérifier sur pièce.

## 13. Fichiers de ce dossier (tous scellés, compagnon `.sha256` à côté)

Dossier : `docs/notes/organisme-idees-juge-v1/correction-poids-v1/confiance/`.

| fichier | sha256 |
|---|---|
| `essai_confiance_banc_v1.py` | `3490044a4d21872f0ebf5193b1c19b19e3a9975da4069c73f882ee69117aecc9` |
| `essai_confiance_certificat_v1.py` | `7b51877c23b58a47fd0f522ec93790adfeef9a709982d2312a896a0bd47a9003` |
| `essai_confiance_cout_v1.py` | `1fe2051d41cbdf83c1be251e648fc019296bd2b0789bdb2066d395da655470e9` |
| `essai_confiance_lot_v1.py` | `d6b884582dac79428a3d16e903e2770a42a29281cac05044327532320f7899b9` |
| `essai_confiance_methodes_v1.py` | `c8b5021b934a89e6a09bfb5d8efad7289799864eb08155c2e33f5d27484e1848` |
| `essai_confiance_resume_v1.py` | `8eb63830cafeb5a328cfbf8eeb0754d1ac08bd6463487f50beea67c5cdee2199` |
| `sorties/certificat-v1.json` | `0bfe3a97d96eb7cff18ee7e452cb5bf58fd5de8ff5a77df415cbc1ce8dd64779` |
| `sorties/cout-ntr100-J3-v1.json` | `d3a7168938b70e4b63f833c897408c623339faa675ccbca5159aa271c41e9baf` |
| `sorties/cout-ntr1000-J3-v1.json` | `b00dff4fc1a8c690f087dfb53c5be57bd3979183ba7409f2dc8a586d939b68fc` |
| `sorties/puissance-V1_0.25-ntr100-J3-r0000-0125-v1.json` | `808ecc6aaf8e93b808a6b9ec5498f1c8341b52eed066440a9e494d72d2e63bc5` |
| `sorties/puissance-V1_0.25-ntr100-J3-r0125-0250-v1.json` | `7c4a79bf29f3783e0e8331a8b9ea0b05db1c2192b0b7acfcce8d3f8c02f0971a` |
| `sorties/puissance-V1_0.25-ntr100-J3-r0250-0375-v1.json` | `a6b899a8c7857168fa10f649cc71d458f083e77816096704408abc09e3fcf8a1` |
| `sorties/puissance-V1_0.25-ntr100-J3-r0375-0500-v1.json` | `7119c206dd5b8d9e7632c2804d3d5457916c483f8c5afb6fa23092f8ef62a36d` |
| `sorties/puissance-V1_0.25-ntr100-J6-r0000-0100-v1.json` | `12f7e9f25ff1e7ae9c7c11128e33c60cbb06e6c6dc098f18a1c6a812b6dc84e7` |
| `sorties/puissance-V1_0.25-ntr100-J6-r0100-0200-v1.json` | `6b705d37ef20dc0870805ded0c2cd0e88eabdeb025ff9bd4f9dc8c8ef0c15f9a` |
| `sorties/puissance-V1_0.25-ntr1000-J3-r0000-0050-v1.json` | `b335680f0162c1c2327631a4f22e55d2de9d9301ac01ca5c160c3cf6e8499d4f` |
| `sorties/puissance-V1_0.25-ntr1000-J3-r0050-0100-v1.json` | `95f960a01babb91038fb8de4d16ee8fd299eb3a984620a6037ff28f3d228e137` |
| `sorties/puissance-V1_0.25-ntr1000-J3-r0100-0150-v1.json` | `f940a5a5674b877e00a975d3274abd4ad700c7a35656288d99f03d42f0e914fa` |
| `sorties/puissance-V1_0.25-ntr1000-J3-r0150-0200-v1.json` | `6e687ea3e1ac63f3c5b1056c1122d375d3f6ab6b08b6b24824d44ab773e44823` |
| `sorties/puissance-V1_0.50-ntr100-J3-r0000-0125-v1.json` | `ae30ecc5df293eefc36ede72a9cc8847b5431f64a4c3273770e0128ee1cc13e6` |
| `sorties/puissance-V1_0.50-ntr100-J3-r0125-0250-v1.json` | `33142caac473a55cd4ea82744558ae14f9f063629a774690c904e45cddd62949` |
| `sorties/puissance-V1_0.50-ntr100-J3-r0250-0375-v1.json` | `8975eb03f09e0c771b2f7abb65ef7a8bce5b247f33d964825d4cc4da45f3cb16` |
| `sorties/puissance-V1_0.50-ntr100-J3-r0375-0500-v1.json` | `a4af1e90a4b0e27bf8a67665d383143a710c630ef365ca39cd9f2e757d155355` |
| `sorties/puissance-V1_0.50-ntr100-J6-r0000-0100-v1.json` | `3d568d48fdad4383709f8752f3d58049de4f5c06cf8a153bc038bce486f6dea7` |
| `sorties/puissance-V1_0.50-ntr100-J6-r0100-0200-v1.json` | `3d5c1671a5a0826d898c78e571f4e1445a6c21764f10ef7ee7b9496b28cc4d4e` |
| `sorties/puissance-V1_0.50-ntr1000-J3-r0000-0050-v1.json` | `a0f1428d56c46028fa59376be877c92eb97ede33a7198e303b59a88cc9a6ccd9` |
| `sorties/puissance-V1_0.50-ntr1000-J3-r0050-0100-v1.json` | `6eca814c7e8e6ce1631c337da8e57b46b8d6b7bca055cb842d01daed24431dcf` |
| `sorties/puissance-V1_0.50-ntr1000-J3-r0100-0150-v1.json` | `1433112c04d9b7f592f7ced7f6fea2676f07ef90381d5ae9fb161e7b2ca5c9fb` |
| `sorties/puissance-V1_0.50-ntr1000-J3-r0150-0200-v1.json` | `1a7892662a0e4147885fdbf9a3e33f652a7be8dcb798b9a8f5b13648309b22bd` |
| `sorties/puissance-V1_0.75-ntr100-J3-r0000-0125-v1.json` | `ee0ecd0d99b3db0c36dd8571bbf5de373584c36a7cfa5891e24ea51b76e9fac5` |
| `sorties/puissance-V1_0.75-ntr100-J3-r0125-0250-v1.json` | `9193129441add355ff5c15abc33672945a3d3765713a7da21b801111ff50fb62` |
| `sorties/puissance-V1_0.75-ntr100-J3-r0250-0375-v1.json` | `cb6cafb887e946d91d0ca60a5fffb70b487ac3003a4e919aa20c8cb6f25e12a4` |
| `sorties/puissance-V1_0.75-ntr100-J3-r0375-0500-v1.json` | `a576401304be6d2b89611546b6d56699f41bb8eb4bcce1df9375d5a81db17c99` |
| `sorties/puissance-V1_0.75-ntr100-J6-r0000-0100-v1.json` | `2786e86ffc2744f7542f1332f4d7cf6956539e685d963eb5be9eb71d83bc809c` |
| `sorties/puissance-V1_0.75-ntr100-J6-r0100-0200-v1.json` | `d0539330006595bf508cd82b739f74321f0cb6186638705c8bc865622429db6f` |
| `sorties/puissance-V1_0.75-ntr1000-J3-r0000-0050-v1.json` | `48ab8283354bb50ce84556f09253685ae36350367a5d46e825cd743a3751f543` |
| `sorties/puissance-V1_0.75-ntr1000-J3-r0050-0100-v1.json` | `f32eadf3f14395f5b94eedd6040fdba9c1a6a40bcc894ff932b1b12d5fbe9e46` |
| `sorties/puissance-V1_0.75-ntr1000-J3-r0100-0150-v1.json` | `89d66cd902e11b4ca6cfb9a8fc5267317690ea5fcbf3a2901c9c975925058af7` |
| `sorties/puissance-V1_0.75-ntr1000-J3-r0150-0200-v1.json` | `9b4b387867d32df95b1c9a5bf5c46d3828da63d9c5b670f640843a9c1ea905a7` |
| `sorties/resume-v1.json` | `ac6bd796164910e0111aa7cdd775145be8fee2e748e2af35e6ffd692de6eab11` |
| `sorties/taille-bord-ntr100-J3-r0000-0125-v1.json` | `b8fdcc20fe1dae6a28e9b5e58fb69dd4058bfee8cebf94366c01610cd6ae4e94` |
| `sorties/taille-bord-ntr100-J3-r0125-0250-v1.json` | `40f9644dc5ca5b9ebeda90721a33a283610767296eb03df36934f01dc616f84f` |
| `sorties/taille-bord-ntr100-J3-r0250-0375-v1.json` | `0bdf38a5febd4097b2a8e5d1a8d22ba43ff563f00f950e41d085a5705d7c0bcb` |
| `sorties/taille-bord-ntr100-J3-r0375-0500-v1.json` | `265e396ca7a213b39d97bc4a9148b5af24c41b8d34558a39a56e1e205480e3c6` |
| `sorties/taille-bord-ntr100-J3-r0500-0625-v1.json` | `e00afc2faefd3b790ef78a1490b3338dc15b829ffaa50d6c38e9288d327fbd24` |
| `sorties/taille-bord-ntr100-J3-r0625-0750-v1.json` | `cd5bfcdb23fd6a0979eba456bfa20e98af040c1e430ea11345c84c5239a0ffc7` |
| `sorties/taille-bord-ntr100-J3-r0750-0875-v1.json` | `e05e2cdfb296f326059da1accac51c30652dde2f7a57cc838a8168d9019a5ac1` |
| `sorties/taille-bord-ntr100-J3-r0875-1000-v1.json` | `810aa47f56eca2771343405adc46d871a4875c9fd3b2698dc397d45da3510790` |
| `sorties/taille-bruit_extreme-ntr100-J3-r0000-0125-v1.json` | `870b30598377730c759edbe9573760ead7799f97c85981dbc61d4779bbe8795f` |
| `sorties/taille-bruit_extreme-ntr100-J3-r0125-0250-v1.json` | `bb0292ce0534e475aa1abffb79957f05ba2a56e76727ac68372784b587c0d92f` |
| `sorties/taille-interieur-ntr100-J3-r0000-0250-v1.json` | `2cdb878861c56d200f4fdaee686d9a42b565d6074ea0276ed4aef733ffbbd2ca` |
| `sorties/taille-interieur-ntr100-J3-r0250-0500-v1.json` | `470f75ede040ff8f8790cb3ae63ea8868c26c6e8b22dd90401e984f147a7bddc` |
| `sorties/taille-interieur-ntr100-J3-r0500-0750-v1.json` | `bf834ee91f516e658ab1296c62b51a60ec337b346800a32111ad30ddcb5e8f15` |
| `sorties/taille-interieur-ntr100-J3-r0750-0875-v1.json` | `69845728fa5744d19435697410f7b5212a5bcf7019fc37f3d1a3d91a8de9b13a` |
| `sorties/taille-interieur-ntr100-J3-r0875-1000-v1.json` | `83ded7e9295a4781c201465918da44970ac95ed0d380205f5393cbcc1ec36207` |
| `sorties/taille-interieur-ntr100-J6-r0000-0125-v1.json` | `474c4b4067aa2f982e5829ef6571470f2b9e93c0b5e085e564f46256959d0e79` |
| `sorties/taille-interieur-ntr100-J6-r0125-0250-v1.json` | `c610e2c95abd8b60889120b734ca7dcd47f6ed95bdb24f8e11859e2191441841` |
| `sorties/taille-interieur-ntr1000-J3-r0000-0050-v1.json` | `26708d56228f7f11e11449e4f4687387d8da5b5b0407a3b83a14ee997605efdb` |
| `sorties/taille-interieur-ntr1000-J3-r0050-0100-v1.json` | `f4f74d2d82e912699352843cd40865e9a435034ef52a1b14613d15227e0d99e5` |
| `sorties/taille-morceaux_archive-ntr100-J3-r0000-0125-v1.json` | `0865498e55429573696c7bc90496431cc84894977635fa3c8cbb8b0548ee7d78` |
| `sorties/taille-morceaux_archive-ntr100-J3-r0125-0250-v1.json` | `6ba01cc12ddde72450e773f08ee36125fdd1a9768f51c29f60135abe16dde668` |
| `sorties/taille-morceaux_archive-ntr100-J3-r0250-0375-v1.json` | `7615cd554fe17f7e16f75116956bf328e860c8381ce8390fa3f30aec28b37aca` |
| `sorties/taille-morceaux_archive-ntr100-J3-r0375-0500-v1.json` | `3bf2ddefe5c27815e083298b80de67f885d43ec9f26657e8d5d0ccfbc9d388c4` |
| `sorties/taille-morceaux_archive-ntr100-J3-r0500-0625-v1.json` | `d776b129e72016d32ebd490466ea58f4b144d8f3a31ea45b772c5996bb028142` |
| `sorties/taille-morceaux_archive-ntr100-J3-r0625-0750-v1.json` | `c75315ec5cf59ef2cf5e8db12839331ca3a492bbd18f314c735e982a6bc13b9f` |
| `sorties/taille-morceaux_archive-ntr100-J3-r0750-0875-v1.json` | `0f7e258704e0f2ae5810225791c3e18d6876b5832f1224145163c9dc920a4fc7` |
| `sorties/taille-morceaux_archive-ntr100-J3-r0875-1000-v1.json` | `6663b29f638f03ce0e413dd5d51d12858bc38057a60f5d6533d16fd178e37334` |
| `sorties/taille-morceaux_grille-ntr100-J3-r0000-0125-v1.json` | `00800d2c1a98796ffef0ed3660c209f295ba5be76a916105a7f449e945d6bf87` |
| `sorties/taille-morceaux_grille-ntr100-J3-r0125-0250-v1.json` | `3b1f24338f44ae26146b472108cf6a6020b5ab47906280ca1622ea6b6870d89e` |
| `sorties/taille-sommet-ntr100-J3-r0000-0125-v1.json` | `7466037f47404f141cc6003f3b27a84ee4e8370925dab128d8e140cb4c7e3a1c` |
| `sorties/taille-sommet-ntr100-J3-r0125-0250-v1.json` | `929db5ae79ecbf13f346eea90a135ad590fc172727ca6ac1023aa85fc7dd73c0` |
| `sorties/taille-sommet-ntr100-J3-r0250-0375-v1.json` | `604f4b89446edeaca11ba48ff46cbcba2c9b7d0d205915e1eb8b7329415a1403` |
| `sorties/taille-sommet-ntr100-J3-r0375-0500-v1.json` | `147575728403acf30bd5d0308945f17a90b2ac71966767156951c5cf4e39e63c` |
| `sorties/taille-sommet-ntr100-J3-r0500-0625-v1.json` | `fa2b5e5f533737e58d0977b40f0b2a6685330d33ce7e299e94c0c03bfb2ad4b6` |
| `sorties/taille-sommet-ntr100-J3-r0625-0750-v1.json` | `c0c9e1ab1b7e76335c714c609aa31be47d842870071bebd0db5f2bd160c14c61` |
| `sorties/taille-sommet-ntr100-J3-r0750-0875-v1.json` | `9e92ecf75fa820990e033fa26cb7cf216c815b22e4bfcd305a3939a986004fab` |
| `sorties/taille-sommet-ntr100-J3-r0875-1000-v1.json` | `e3b83b2a6a7beb097a822b391b3873c620ecb4f8e2574675f4b035d0120117fa` |
| `sorties/taille-sous_population-ntr100-J3-r0000-0125-v1.json` | `fd9eca2ae5a9479420c41886d2562e61f070ee7d3357bbf51a1ccef0ad2c7752` |
| `sorties/taille-sous_population-ntr100-J3-r0125-0250-v1.json` | `cfabd2d067c085b9b62960b5395901b27afc9a4d5d70434bbb7e712251331479` |

La note elle-même a son empreinte dans son compagnon `methodes-confiance-v1.md.sha256`.
