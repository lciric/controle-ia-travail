# Correction des poids du nul — angle « inférence universelle bien faite » — v1

**Statut.** Mise au point exploratoire, **aucune revendication**. Aucun préenregistrement : rien ici n'est une expérience
décisive. Toutes les issues sont rapportées à l'identique, celles qui échouent comprises. Processeur seul, aucun appel
réseau, aucun appel payant, aucun commit.

- Auteur : concepteur neuf, sous-agent de la session mère ; je n'ai écrit aucune des pièces citées.
- Date : 2026-11-15, de 09:12 à 11:12 UTC (`date -u`) ; dépôt lu sur `main`, tête `88a19ce1`.
- Calculs : Python 3.13, numpy 2.4.6, scipy (`.venv/bin/python`), 3 processus sur une machine partagée (charge de 6 à 12).
- Dossier : `docs/notes/organisme-idees-juge-v1/correction-poids-v1/universelle/`. Chaque fichier y a son compagnon
  `.sha256` ; la table des empreintes est en section 9.

## 0. Ce que je trouve, en sept lignes

1. **Les deux façons des fiches violent une seule et même condition** : le dénominateur doit **majorer, sur la part
   jugée, la vraisemblance du vrai membre** (H4 de la preuve du nul limité). Elles mettent au dénominateur une **loi de
   probabilité normalisée** qui « devine » le membre (prédiction en ligne ; ajustement sur l'autre moitié) ; pour une copie
   exacte, E[W] = Σ P*²/D ≥ 1 et E[log W] = KL(P* ‖ D) ≥ 0 (lemme B, section 3). Le banc le voit : copie exacte promue dans
   95,5 % à 100 % (en ligne) et 9,7 % à 43,5 % (moitié) des mondes des quatre cas de membres du nul limité, au lieu de 0.
2. **Aucune façon valide d'« apprendre les poids » ne regagne la puissance perdue sur ce banc.** Le maximum sur la part
   jugée est le plus petit dénominateur qui domine tous les membres (lemme A) : toute variante qui garde cette domination
   est sous le v9 trajectoire par trajectoire. Les variantes valides qui laissent une part des tirages apprendre (moitié
   jugée, découpes croisées, sous-échantillons, région de confiance) tiennent leur taille (0 promotion sur 400 à 1 000 mondes
   par cas) mais perdent nettement contre le v9 (par exemple, à λ = 0,40 : v9 0,493 ; confiance 0,277 ; sous-échantillons
   0,270 ; croisées 0,230 ; moitié jugée 0,177).
3. Le seul gain valide mesuré est la **lecture dense** (tous les dix tirages au lieu de tous les vingt-cinq ; Ville couvre
   tous les instants) : +0,007 / +0,027 / 0 aux trois doses, faible.
4. Les dénominateurs **pénalisés vers le bas** et le **mélange a priori** des membres ne sont pas valides (garantie α·e^c
   et α/π) ; le banc des copies voit le mélange (17,9 % à 54,3 % de copies promues) et la pénalité forte (100 %), il **ne
   voit pas** une pénalité d'un nat (une copie a W ≤ 1, donc W·e < 1/α) : angle mort déclaré.
5. Le prix du v9 du banc vient surtout de la **liberté par morceau** (deux jeux de poids), peu de la **recherche des
   coupures** : à λ = 0,25, v8 0,383, nul limité à la seule coupure de l'archive 0,130, v9 du banc 0,080.
6. Ce qui regagnerait la puissance sans perdre la taille, en théorie, est la valeur e contre l'**enveloppe convexe** du nul
   (projection d'information inverse, poids appris **sur la carte**, pas sur les tirages) ; je ne sais pas la certifier
   sur la classe continue du nul ; écartée ici, nommée comme piste (section 7).
7. Rien ne change la conception scellée du juge ; deux propositions seraient des nœuds du directeur : lecture dense
   (instants écrits dans l'engagement) ; et, si un jour la projection inverse se certifie, une valeur e d'une autre forme.

## 1. Ce que j'ai lu (empreintes recalculées le 15 novembre, égales à leurs compagnons)

| pièce | chemin | sha256 |
|---|---|---|
| preuve de validité du nul limité | `docs/notes/organisme-idees-juge-v1/preuve-validite-nul-limite-v1.md` | `44f249409193778ccbaaa12b6c5e74d64434dfb87be77382d8bb9438459281b2` |
| préenregistrement de l'idée 1.1 | `docs/notes/organisme-idees-juge-v1/prereg-nul-par-morceaux-limite-v1.md` | `46ef2b92119ee5dff05727b90ca8bdd3ba57b52f9c1c75893750c792a2abc089` |
| contre-lecture | `docs/notes/organisme-idees-juge-v1/contre-lecture-prereg-nul-limite-et-preuve-v1.md` | `763fc6e29cd80868dcdb1d848eafdc928a39fca7244fa16eb0ac721ec705014e` |
| nul v9 (copie, lue, jamais exécutée) | `docs/notes/organisme-idees-juge-v1/copie-nul-v9-a41b7b5/orchestrator/pole/nul_v9.py` | `7ae450df2482246122bf9fbcf0fa5ef30b4a7e4c6f0d09531e83af048e46ee95` |
| pari, tirages frais | `docs/notes/organisme-courbe-dose-reponse-v1/code-organisme-94bfd92/orchestrator/pole/selection_pari.py` | `359928110d757cd54cc0d2773910c7360895b68cac5d17e0e4b4e9933ef306bc` |
| nul v8 | `…/code-organisme-94bfd92/orchestrator/pole/nul_v8.py` | `cc452aafd17121a7c0ec42829eea47063ffee1f6cdf7f642e264d528f976b888` |
| membres ajustés, certificat, instants | `…/code-organisme-94bfd92/orchestrator/pole/nul_filles_v2.py` | `0ed9b4adbcddc4ad77a1c97d5cbd5706f14926e9c47fe96ce2bab3221a138910` |
| jugement d'une carte fraîche | `…/code-organisme-94bfd92/orchestrator/pole/a_blanc_v59.py` | `606aa8b4fcc38786b38cf2954da46533eed9384232a56100d22ff30b8ce0826c` |
| relevé, section 1.1 | `docs/notes/organisme-conception-propre-v1/relecture-exploratoire-v2/releve-idees-reutilisables-v1.md` | `bd253b6c68f6baada0e61b5381f029b52838ca34aa092502e55253c662451c6c` |
| fiches argon-p1-01 (n° 0), opus-p1-05 (n° 9), fable-p1-05 (n° 13), argon-p2-01 (n° 14) | `runs/course-ideation-conception-propre-v1/20261113-235541-course-ideation-conception-propre-v1-g1/copies/sortie--fiches-validees.json` | `a9f9594e2dc3a7a553c54577202817758e3f7ef231445f1a48d500fc647389d5` |
| verdict de la validation du v9 | `docs/verdicts/verdict-validation-nul-v9-v1.md` | `1407e460367754bb9f76b37174f3a21585970864eb9beaa2699494d90125c1ea` |

Ce que « puissance perdue » veut dire (verdict, « En tête » et « Portée ») : les 18 lignes fatales du banc des tricheurs v9
sont tenues, mais la perte appariée de puissance du v9 contre le v8 dépasse la marge de 0,05 sur une ligne (I02,
interaction faible hors de l'archive) ; le v9 reste valide, il coûte des promotions de vraies découvertes. Je ne reprends
aucun chiffre de ce verdict dans mes essais.

## 2. Le banc (recopié, simplifié, déclaré)

Code : `banc_universelle_v1.py`. **Aucun fichier des dossiers de copie n'est exécuté ni importé** ; la logique utile est
recopiée (famille par morceaux à bruit aveugle commun de `nul_v9.py`, l. 19 à 25 ; certificat de Frank-Wolfe de
`nul_filles_v2._lineaire` et `nul_v9._certificats` ; lecture aux instants fixés et promotion de `evaluer_v9`).
- K = 3 issues ; deux traits z ~ N(0, 1) ; sous-population g ∈ {0, 1} ; n = 200 tirages frais ; instants 25, 50, …, 200 ;
  α = 0,05 ; promotion si log W_t ≥ log 20 à un instant lu ; pari plein (numérateur = la loi gelée de la carte).
- Archive : S1, S2 (softmax aléatoires, poids N(0 ; 1,5²), biais N(0 ; 0,3²)) et S3 = si_sinon(z_jA > s_A, U1, U2), qui
  porte **la coupure de l'archive** (s_A uniforme sur [−1 ; 1] au centième, hors de la grille à 0,05 près).
- Classes du nul (membres linéaires seulement ; les membres log-linéaires du v8 sont absents ; uniforme et marginales
  sont des cas du bruit aveugle) : **v8 du banc** = aucune coupure ; **limité** = aucune coupure et coupure de l'archive ;
  **v9 du banc** = aucune coupure, sous-population, coupure de l'archive et **neuf seuils par trait** (déciles de N(0, 1)) —
  le vrai v9 parcourt tout seuil réel ; mon v9 est plus petit, son prix est donc **sous-estimé** (essai « grille fine »,
  section 5.3).
- Calcul de chaque maximum : montée par espérance-maximisation plus un pas de Frank-Wolfe tous les trois pas ; **valeur
  rendue = valeur atteinte + écart de Frank-Wolfe** (borne haute exacte), élagage par question à 10⁻³ nat (même précision
  que `TOLERANCE_GROUPE` du v9), au plus 400 pas. Un arrêt prématuré coûte de la puissance, jamais de la validité.
- Cas de taille (carte = loi du monde, copie exacte) : **interieur** (membre du nul limité à poids tirés au hasard,
  bruit 5 % à 40 %) ; **sommet** (bord du simplexe : une loi connue de chaque côté de la coupure de l'archive, sans bruit —
  c'est aussi la copie par morceaux pure sur une coupure de l'archive) ; **extreme** (poids 0,99 / 0,005, bruit 1 % concentré
  sur une issue) ; **bruite** (copie par morceaux sur la coupure de l'archive avec 40 % de bruit aveugle) ; et, hors du nul
  limité mais dans le v9 du banc : **sous_population**, **grille** (copie sur un seuil de la grille).
- Cas de puissance (vraie découverte, une composante neuve) : monde = carte = (1 − λ)·(membre intérieur) + λ·N, N softmax
  neuve hors de l'archive, λ ∈ {0,25 ; 0,40 ; 0,55}. Doses placées par un **pilote** de 40 mondes par dose sur v8 et v9
  seuls (graine 777, λ ∈ {0,2 ; 0,35 ; 0,5 ; 0,7} : v8 0,275 / 0,725 / 0,85 / 0,95, v9 0 / 0,5 / 0,675 / 0,9 ; script hors
  dossier, sortie non gardée — chiffre de réglage, non opposable), aucune méthode comparée au pilote.
- Graines : `numpy.random.SeedSequence(entropy=E, spawn_key=(indice du cas, r))`, scindée en (monde, sous-ensembles) ;
  E = 20261115101 (taille), 20261115201 (puissance), 20261115301 (coût) ; écrites dans chaque sortie. Même clé ⇒ même
  monde d'un lot à l'autre : les lots « a » et « b » sont appariés (vérifié : le v9 est identique monde par monde,
  `sortie-appariement-puissance-v1.json`).
- **Écart au plan de dix minutes** : le premier lot (`sortie-taille-interieur-v1.json`, toutes les méthodes, 1 000 mondes)
  a duré 857 s sous une charge de 10 ; j'ai alors arrêté la suite (arrêt par identifiant de processus, 31997) et scindé
  les méthodes en lots « a » (1 000 mondes) et « b » (600 ou 400 mondes) ; le nombre de mondes réduit est dit cas par cas.
- **Contrôle de monotonie** (v9 ≤ limité ≤ v8 trajectoire par trajectoire, vrai pour les vrais maxima) : excès au plus
  0,82 nat dans 4 mondes sur 1 000 (cas grille), 1 à 2 mondes ailleurs ; c'est l'écart de certificat d'une question non
  convergée en 400 pas (une borne haute trop lâche baisse la richesse de la classe concernée) : coût en puissance des
  classes v8 ou limitée dans ces mondes, aucun effet sur la validité.

## 3. Quatre lemmes qui disent où est la marge

Notations du juge (`nul_v9.py`, `nul_filles_v2.evaluer_v2`) : plan x_1..x_n gelé (n = 200), carte q gelée avant les tirages
frais, instants lus T = {25, 50, …, 200}, α = 0,05 ; nul 𝒩 = union de familles Θ_F (une par partition F : aucune
coupure, sous-population, coupure de l'archive, coupures d'un trait) ; L_θ(y_A) = Π_{s ∈ A} p_θ(y_s | x_s) pour une part
A des tirages ; « part jugée » = les tirages dont W fait le produit ; D_t = dénominateur à l'instant t ;
log W_t = Σ_{s ≤ t} log q(y_s | x_s) − log D_t. Valide = P(∃ t ∈ T : W_t ≥ 1/α) ≤ α pour tout monde de 𝒩.

**Lemme A (le maximum est le plus petit dénominateur qui domine).** Soit une règle qui calcule D_t à partir des issues
y_1..t (et de tout ce qui est gelé). Si D_t(y) ≥ L_θ(y_1..t) pour tout θ ∈ 𝒩 et toute suite y (domination trajectoire par
trajectoire, l'hypothèse H4 de la preuve du nul limité), alors D_t(y) ≥ sup_θ L_θ(y_1..t) pour toute suite y, donc
W_t ≤ W_t^{v9} trajectoire par trajectoire (au certificat près).
*Preuve.* Le supremum est le plus petit des majorants de la famille {L_θ(y)}_θ, point par point. ∎
Conséquence : **aucune** variante qui garde la domination trajectoire par trajectoire — dénominateur lissé, pénalisé vers
le haut, maximum sur une enveloppe, maximum pris séparément sur deux moitiés — ne peut promouvoir une carte que le v9 ne
promeut pas. Un dénominateur « lissé ou pénalisé dont on prouve qu'il domine encore la vraisemblance du vrai membre »
pour **tout** membre est donc ≥ au maximum : valide, jamais plus puissant. La seule marge de ce côté est le certificat
(écart de Frank-Wolfe, au plus 10⁻³ nat ici).

**Lemme B (un dénominateur qui est une loi de probabilité promeut les copies).** Soit A une part jugée, et D une loi de
probabilité sur les suites y_A, fixée sachant ce qui est hors de A (poids appris sur une autre part) ou prévisible
(produit de prédictions p_{w_{s−1}}(y_s | x_s), poids appris sur le passé), ou un mélange a priori de membres. Pour une
copie exacte q = P_{θ*} d'un membre : E[W] = Σ_{y_A} P_{θ*}(y_A)² / D(y_A) ≥ 1 et E[log W] = KL(P_{θ*} ‖ D) ≥ 0, avec
égalité seulement si D = P_{θ*} sur A.
*Preuve.* Cauchy-Schwarz : (Σ P)² ≤ (Σ P²/D)(Σ D) avec Σ D = Σ P = 1. Gibbs pour le logarithme. Pour une prédiction
séquentielle, KL(P* ‖ D) est le regret cumulé du prédicteur, qui croît avec le nombre de tirages pour toute famille à
paramètres libres ; pour une loi fixée D ≠ P*, il croît linéairement. ∎
Ce lemme dit **exactement la condition que violent les fiches** : le dénominateur d'une valeur e valide contre un nul
composite qui contient les copies ne peut pas être une loi normalisée qui « devine » le membre ; il doit être un majorant
non normalisé (Σ_y sup_θ L_θ(y) > 1). Le surplus de masse du maximum, log Σ_y sup_θ L_θ(y) (somme de Shtarkov, complexité
paramétrique au sens de la longueur de description minimale ; référence à vérifier sur pièce : Shtarkov, 1987 ;
Rissanen, 1996), est **le prix en puissance** : il grandit avec la classe. Les deux façons des fiches suppriment ce
surplus, donc la garantie avec lui.
- argon-p2-01 (poids appris en ligne) : D = Π_s p_{w_{s−1}}(y_s | x_s), loi prévisible normalisée → lemme B ; c'est une
  martingale sous la loi prédictive, pas sous un membre fixe (preuve du nul limité, § 8.1).
- argon-p1-01 (poids ajustés sur la première moitié, valeur e sur la seconde) : D = L_{ŵ(D1)}(y_{D0}), loi normalisée sur
  D0 sachant D1 → lemme B conditionnellement à D1 ; l'inférence universelle fait l'inverse : c'est l'alternative qui
  s'apprend hors de la part jugée, et le maximum du nul se prend **sur** la part jugée.
- fable-p1-05 (mélange à poids fixes de lois par morceaux) et point 5 de `nul_v9.py` : D = Σ_F π_F L_{θ_F}, loi
  normalisée → lemme B ; même avec le maximum de chaque famille dans le mélange, W ≤ Λ / π_{F*} : garantie α / π_{F*}.

**Lemme C (combiner des parts fixées d'avance reste valide).** Soient des parts S_1..S_B ⊂ {1..n} fixées avant les tirages
(sans lire les issues), et W^b_t = Π_{s ≤ t, s ∈ S_b} q / sup_θ L_θ(y_{S_b ∩ [1..t]}). Alors pour tout monde θ* de 𝒩,
ē_t = (1/B) Σ_b W^b_t vérifie P(∃ t : ē_t ≥ 1/α) ≤ α.
*Preuve.* W^b_t ≤ Λ^b_t = Π_{s ≤ t, s ∈ S_b} q(y_s | x_s) / P_{θ*}(y_s | x_s) (domination sur la part, lemme A). Chaque Λ^b
est une martingale positive de départ 1 pour la filtration de **tous** les tirages (un facteur par tirage de S_b, 1
sinon ; q est gelée, les issues sont indépendantes sachant le plan). La moyenne est une martingale positive de départ 1 ;
Ville. ∎ Remarque : le produit W^A·W^B de deux parts complémentaires est valide aussi, mais
sup L(y_A)·sup L(y_B) ≥ sup L(y_A, y_B) : il est sous le v9 trajectoire par trajectoire (lemme A).

**Lemme D (région de confiance apprise sur une part, maximum pris sur la part jugée).** D1 = tirages 1..100, D0 = tirages
101..200, β ∈ (0, α). C = {θ : log L_θ(y_{D1}) > log q(y_{D1}) − log(1/β)}. Pour tout λ ≥ 0 et t ≤ 100,
B_λ(t) = sup_θ [log L_θ(y_{D0, ≤ t}) + λ log L_θ(y_{D1})] − λ (log q(y_{D1}) − log(1/β)) majore sup_{θ ∈ C} log L_θ(y_{D0, ≤ t}).
Promotion si log q(y_{D0, ≤ t}) − min_λ B_λ(t) ≥ log(1/(α − β)) à un instant lu. Alors P(promotion) ≤ α pour tout monde de 𝒩.
*Preuve.* (1) P(θ* ∉ C) = P(q(y_{D1}) / L_{θ*}(y_{D1}) ≥ 1/β) ≤ β (Markov ; q gelée, rapport d'espérance ≤ 1). (2) Sur
{θ* ∈ C}, pour chaque λ, le terme ajouté est ≥ 0 en θ*, donc log L_{θ*}(y_{D0, ≤ t}) ≤ B_λ(t) (dualité faible), puis
≤ min_λ B_λ(t) ; chaque B_λ est un maximum de fonction concave, borné par un certificat de Frank-Wolfe pondéré. (3) Donc,
sur cet événement, W_t ≤ Λ^{D0}_t, martingale positive sur D0 sachant D1 : P(∃ t : Λ^{D0}_t ≥ 1/(α − β)) ≤ α − β (Ville).
(4) Union : β + α − β = α. ∎ C'est la seule façon de « laisser une part apprendre les poids du nul » que j'ai trouvée
valide : la part apprend une **région**, payée β, jamais un point. Référence de forme à vérifier sur pièce : Berger et
Boos, 1994 (valeur p maximisée sur une région de confiance) ; Wasserman, Ramdas et Balakrishnan, « Universal inference »
(ensembles de confiance universels).

**Remarque (lecture dense).** La preuve du nul limité, pas 4, et la contre-lecture (p2) établissent que Ville couvre tous les
instants : lire à chaque dizaine de tirages au lieu de chaque vingt-cinquaine reste valide et ne peut que promouvoir plus.

## 4. Les méthodes, une par une

Chaque méthode : énoncé ; validité (preuve ou raison de l'échec) ; taille ; artefact ; puissance ; coût ; ce qu'elle
changerait à la conception scellée. Chiffres : tables de la section 5, fichier et empreinte en section 9.

### 4.1 Référence : maximum certifié sur tous les tirages (façon nul v9 ; aussi « maximum courant séquentiel »)
- **Énoncé.** log W_t = Σ_{s ≤ t} log q(y_s | x_s) − max_F V_F(t), V_F(t) = valeur atteinte + écart de Frank-Wolfe de la
  famille F sur les t premiers tirages ; F parcourt les partitions du v9 du banc ; promotion si log W_t ≥ log 20, t ∈ T.
  Avec un numérateur gelé, c'est **exactement** la variante séquentielle de l'inférence universelle (alternative apprise
  sur le passé — ici, avant le gel —, maximum du nul sur tout le passé) : rien à corriger.
- **Validité.** Théorème 1 de la preuve du nul limité (H1 à H8), appliqué à la classe du v9 du banc : valide.
- **Taille.** 0 sur 1 000 dans chacun des six cas (bornes hautes de Clopper-Pearson 0,0037) ; log W maximal ≤ 0 partout.
- **Puissance.** 0,080 / 0,493 / 0,800 aux trois doses ; v8 0,383 / 0,723 / 0,910 ; limité 0,130 / 0,603 / 0,847.
- **Coût.** 0,149 s par carte (un processus) ; le juge réel parcourt toutes les coupures : plus cher.
- **Conception scellée.** Aucun changement (c'est le v9).

### 4.2 Fiche argon-p2-01 : poids appris en ligne (artefact obligatoire)
- **Énoncé.** Sur la partition de l'archive (deux cellules), poids des J lois connues et des K lois certaines propres à
  chaque cellule, initialisés uniformes, mis à jour après chaque tirage par descente exponentielle (pas η = 0,05 ou 0,2) ;
  dénominateur = Π_s p_{w_{s−1}}(y_s | x_s).
- **Validité : non.** Condition violée : la domination de la vraisemblance du vrai membre sur la part jugée (H4). Le
  dénominateur est une loi prévisible normalisée ; lemme B : pour une copie, log W_t = regret du prédicteur ≥ 0 en
  espérance, croissant avec t. La « martingale de valeur initiale 1 » de la fiche est une martingale sous la loi
  prédictive, pas sous un membre fixe.
- **Taille (artefact).** Copie exacte promue : interieur 0,955 [0,940 ; 0,967] (η = 0,05) et 0,999 (η = 0,2) ; sommet,
  extreme : 1,000 ; bruite 0,993 et 0,999 ; hors du nul limité : 1,000. **Le banc voit l'échec.**
- **Puissance.** 0,957 / 0,987 / 0,997 : sans objet (taille perdue).
- **Coût.** 0,003 s par carte. **Conception.** Non proposable.

### 4.3 Fiche argon-p1-01 : poids ajustés sur la première moitié, valeur e sur la seconde (artefact obligatoire)
- **Énoncé.** Maximum de vraisemblance des poids du nul limité sur les tirages 1 à 100 ; W sur 101 à 200 avec ces poids
  fixés ; lecture à 25, 50, 75, 100 tirages de la seconde moitié.
- **Validité : non.** Même condition violée : le dénominateur L_{ŵ(D1)}(y_{D0}) est une loi normalisée sur la part jugée
  sachant D1 (lemme B) ; l'inférence universelle met l'apprentissage **au numérateur** (l'alternative) et le maximum du nul
  **sur** la part jugée.
- **Taille (artefact).** interieur 0,435 [0,404 ; 0,466] ; sommet 0,097 [0,079 ; 0,117] ; extreme 0,148 [0,127 ; 0,172] ;
  bruite 0,360 [0,330 ; 0,391] ; hors du nul limité (sous_population 0,989, grille 0,903 : sa classe ne les contient pas).
  **Le banc voit l'échec**, plus faiblement au bord du simplexe (le maximum de la première moitié y tombe juste).
- **Puissance.** 0,643 / 0,800 / 0,907 : sans objet. **Coût.** 0,114 s. **Conception.** Non proposable.

### 4.4 Moitié jugée : la correction directe de argon-p1-01
- **Énoncé.** Même découpe, mais le maximum certifié du nul (classe v9 du banc) est pris **sur la seconde moitié**, celle
  où W est évalué : log W_{t₀} = Σ_{101 ≤ s ≤ 100 + t₀} log q − max_F V_F(seconde moitié, t₀ premiers).
- **Validité : oui.** Théorème 1 appliqué à la part D0 (la part D1 ne sert à rien : le numérateur est déjà gelé).
- **Taille.** 0 sur 1 000 (interieur), 0 sur 600 (sommet, extreme, bruite), 0 sur 400 (sous_population, grille).
- **Puissance.** 0,010 / 0,177 / 0,500 : nettement sous le v9 (−0,07 / −0,32 / −0,30, appariés). Ce n'est pas une surprise : la moitié des
  preuves est jetée, sans rien gagner, puisqu'il n'y a pas d'alternative à apprendre.
- **Coût.** 0,084 s. **Conception.** Changerait la règle de promotion (part jugée) : nœud, **non recommandée**.

### 4.5 Découpes croisées, moyenne de valeurs e
- **Énoncé.** Parts paire et impaire, fixées d'avance ; e_t = ½(W^A_t + W^B_t), chaque W calculé sur sa part avec le
  maximum certifié **sur sa part**, à chaque instant lu.
- **Validité : oui** (lemme C, anytime : la moyenne de deux martingales de test de la filtration commune).
- **Taille.** 0 sur 1 000 (interieur), 0 sur 600 (sommet, extreme, bruite), 0 sur 400 (sous_population, grille).
- **Puissance.** 0,013 / 0,230 / 0,620 : sous le v9 (−0,07 / −0,26 / −0,18). La moyenne de deux demi-preuves vaut au plus la
  meilleure des deux ; le produit (valide aussi) est sous le v9 par le lemme A.
- **Coût.** 0,178 s. **Conception.** Nœud, **non recommandée**.

### 4.6 Sous-échantillonnage (moyenne sur B = 4 moitiés tirées au hasard)
- **Énoncé.** Quatre moitiés S_b tirées avant les issues (graine propre, scindée de celle du monde) ; e_t = moyenne des W^b_t.
  Retire l'aléa de la découpe.
- **Validité : oui** (lemme C).
- **Taille.** 0 sur 1 000 (interieur), 0 sur 600 (sommet, extreme, bruite), 0 sur 400 (sous_population, grille).
- **Puissance.** 0,010 / 0,270 / 0,637 : un peu au-dessus des découpes croisées, toujours sous le v9 (−0,07 / −0,22 / −0,16).
- **Coût.** 0,370 s (≈ B fois le v9 sur 100 tirages). **Conception.** Nœud, **non recommandée**.

### 4.7 Région de confiance apprise sur une moitié, maximum restreint sur l'autre (« confiance »)
- **Énoncé.** Lemme D : D1 apprend une **région** C des poids du nul (au prix β = 0,025), jamais un point ; le maximum du
  nul se prend sur D0 et seulement dans C, borné par dualité faible (λ ∈ {0 ; 0,25 ; 1 ; 4 ; 16}) ; seuil log(1/(α − β)) =
  log 40. C'est, à ma connaissance, la seule façon valide de **laisser une part des tirages apprendre les poids du nul**.
- **Validité : oui** (lemme D : β + (α − β) = α).
- **Taille.** 0 sur 1 000 (interieur), 0 sur 600 (sommet, extreme, bruite), 0 sur 400 (sous_population, grille).
- **Puissance.** 0,013 / 0,277 / 0,650 : la meilleure des variantes à découpe, mais sous le v9 (−0,07 / −0,22 / −0,15 ; McNemar exact p ≤ 2·10⁻⁶ à chaque dose). Quand la
  carte bat toute la classe sur D1, C est vide et la richesse explose (log W jusqu'à 277), d'où une forte promotion
  conditionnelle ; mais le seuil plus haut et la moitié des tirages coûtent plus que la restriction ne rend, sur ce banc.
  Avec une grille fine (19 seuils par trait), le v9 du banc fait 0,075 [0,043 ; 0,121] et la confiance 0,020 [0,006 ; 0,050] (200 mondes à λ = 0,25, nul limité 0,155, v8 0,390) : l'écart ne se renverse pas.
- **Coût.** 0,233 s (cinq valeurs de λ × quatre instants). **Conception.** Changerait la valeur e (part de α
  dépensée à part, deux seuils) : nœud, **non recommandée en l'état** ; piste si la classe du nul grandit beaucoup (mondes
  à 8 traits, toutes les coupures), à éprouver sur un banc où le prix des coupures domine.

### 4.8 Lecture dense (tous les dix tirages)
- **Énoncé.** Le v9, lu à 10, 20, …, 200 au lieu de 25, …, 200.
- **Validité : oui** (pas 4 de la preuve du nul limité ; contre-lecture, p2 : Ville borne tous les instants à la fois).
- **Taille.** 0 sur 1 000 (interieur) et 0 sur 1 000 (sommet), lots « dense » à part ; par construction aucune copie d'un
  membre n'a W > 1 à aucun instant.
- **Puissance.** 0,087 / 0,520 / 0,800 contre 0,080 / 0,493 / 0,800 : +0,007 / +0,027 / 0 (appariés : la méthode promeut
  tout ce que le v9 promeut).
- **Coût.** 0,241 s (2,5 fois plus d'instants). **Conception.** Les instants sont écrits dans l'engagement
  (`instants_lecture`) et la valeur e de la règle e-BH s'arrête au premier instant lu au-dessus de m/α : changer T est un
  changement de conception, **nœud du directeur** ; gain faible, seule proposition de cet angle qui gagne sans rien perdre.

### 4.9 Dénominateurs pénalisés vers le bas (« lissés » par une pénalité)
- **Énoncé.** log W_t + c(t) : c = 1 nat ; c = (d/2)·log t, d = 7 (pénalité de complexité).
- **Validité : non.** W ≤ e^{c}·Λ : garantie α·e^{c} seulement (Ville appliquée à Λ ≥ 1/(α e^{c})). Le lemme A dit qu'aucune
  pénalité vers le bas ne garde la domination ; une pénalité vers le haut la garde et n'est jamais plus puissante.
- **Taille.** c = (d/2) log t : 1,000 dans les six cas (log W max ≈ 18,5). **c = 1 nat : 0 partout — angle mort du banc** :
  pour une copie W ≤ 1, donc W·e ≈ 2,7 < 20 ; le défaut ne se voit que pour une carte voisine du monde sans en être une
  copie, cas que mon banc ne contient pas.
- **Puissance.** c = 1 nat : 0,127 / 0,563 / 0,830 (sans objet : invalide).
- **Coût.** celui du v9. **Conception.** Non proposable.

### 4.10 Mélange a priori des membres (fable-p1-05 ; point 5 de `nul_v9.py`)
- **Énoncé.** Dénominateur log Σ_F π_F exp(V_F(t)), π uniforme sur les 21 partitions.
- **Validité : non.** Loi normalisée au sens du lemme B dès que les V_F sont des vraisemblances ; avec les maxima, W ≤ Λ/π_{F*} :
  garantie 21·α.
- **Taille.** interieur 0, extreme 0, bruite 0 ; **sommet 0,179** [0,156 ; 0,204] ; **sous_population 0,543** ; **grille
  0,330** ; log W max 3,04 = log 21 (la borne est atteinte). **Le banc voit l'échec.**
- **Puissance.** 0,130 / 0,557 / 0,827 : sans objet. **Coût.** celui du v9. **Conception.** Non proposable.

## 5. Résultats (chaque cellule : promotions / mondes, taux, intervalle de Clopper-Pearson bilatéral à 95 %)

### 5.1 Taille : copie exacte d'un membre (carte = loi du monde), au niveau du juge

| méthode | interieur | sommet | extreme | bruite | sous_population | grille |
|---|---|---|---|---|---|---|
| v8 | 209/1000 0,209 [0,184 ; 0,235] | 983/1000 0,983 [0,973 ; 0,990] | 972/1000 0,972 [0,960 ; 0,981] | 731/1000 0,731 [0,702 ; 0,758] | 993/1000 0,993 [0,986 ; 0,997] | 976/1000 0,976 [0,965 ; 0,985] |
| limite | 0/1000 0,000 [0,000 ; 0,004] | 0/1000 0,000 [0,000 ; 0,004] | 0/1000 0,000 [0,000 ; 0,004] | 0/1000 0,000 [0,000 ; 0,004] | 993/1000 0,993 [0,986 ; 0,997] | 910/1000 0,910 [0,890 ; 0,927] |
| v9 | 0/1000 0,000 [0,000 ; 0,004] | 0/1000 0,000 [0,000 ; 0,004] | 0/1000 0,000 [0,000 ; 0,004] | 0/1000 0,000 [0,000 ; 0,004] | 0/1000 0,000 [0,000 ; 0,004] | 0/1000 0,000 [0,000 ; 0,004] |
| v9_dense | 0/1000 0,000 [0,000 ; 0,004] | 0/1000 0,000 [0,000 ; 0,004] | — | — | — | — |
| moitie_jugee | 0/1000 0,000 [0,000 ; 0,004] | 0/600 0,000 [0,000 ; 0,006] | 0/600 0,000 [0,000 ; 0,006] | 0/600 0,000 [0,000 ; 0,006] | 0/400 0,000 [0,000 ; 0,009] | 0/400 0,000 [0,000 ; 0,009] |
| croisee | 0/1000 0,000 [0,000 ; 0,004] | 0/600 0,000 [0,000 ; 0,006] | 0/600 0,000 [0,000 ; 0,006] | 0/600 0,000 [0,000 ; 0,006] | 0/400 0,000 [0,000 ; 0,009] | 0/400 0,000 [0,000 ; 0,009] |
| sous_echantillons | 0/1000 0,000 [0,000 ; 0,004] | 0/600 0,000 [0,000 ; 0,006] | 0/600 0,000 [0,000 ; 0,006] | 0/600 0,000 [0,000 ; 0,006] | 0/400 0,000 [0,000 ; 0,009] | 0/400 0,000 [0,000 ; 0,009] |
| confiance | 0/1000 0,000 [0,000 ; 0,004] | 0/600 0,000 [0,000 ; 0,006] | 0/600 0,000 [0,000 ; 0,006] | 0/600 0,000 [0,000 ; 0,006] | 0/400 0,000 [0,000 ; 0,009] | 0/400 0,000 [0,000 ; 0,009] |
| penalise_1nat | 0/1000 0,000 [0,000 ; 0,004] | 0/1000 0,000 [0,000 ; 0,004] | 0/1000 0,000 [0,000 ; 0,004] | 0/1000 0,000 [0,000 ; 0,004] | 0/1000 0,000 [0,000 ; 0,004] | 0/1000 0,000 [0,000 ; 0,004] |
| penalise_bic | 1000/1000 1,000 [0,996 ; 1,000] | 1000/1000 1,000 [0,996 ; 1,000] | 1000/1000 1,000 [0,996 ; 1,000] | 1000/1000 1,000 [0,996 ; 1,000] | 1000/1000 1,000 [0,996 ; 1,000] | 1000/1000 1,000 [0,996 ; 1,000] |
| melange_a_priori | 0/1000 0,000 [0,000 ; 0,004] | 179/1000 0,179 [0,156 ; 0,204] | 0/1000 0,000 [0,000 ; 0,004] | 0/1000 0,000 [0,000 ; 0,004] | 543/1000 0,543 [0,511 ; 0,574] | 330/1000 0,330 [0,301 ; 0,360] |
| fiche_en_ligne_0.05 | 955/1000 0,955 [0,940 ; 0,967] | 1000/1000 1,000 [0,996 ; 1,000] | 1000/1000 1,000 [0,996 ; 1,000] | 993/1000 0,993 [0,986 ; 0,997] | 1000/1000 1,000 [0,996 ; 1,000] | 1000/1000 1,000 [0,996 ; 1,000] |
| fiche_en_ligne_0.2 | 999/1000 0,999 [0,994 ; 1,000] | 1000/1000 1,000 [0,996 ; 1,000] | 1000/1000 1,000 [0,996 ; 1,000] | 999/1000 0,999 [0,994 ; 1,000] | 1000/1000 1,000 [0,996 ; 1,000] | 1000/1000 1,000 [0,996 ; 1,000] |
| fiche_moitie | 435/1000 0,435 [0,404 ; 0,466] | 97/1000 0,097 [0,079 ; 0,117] | 148/1000 0,148 [0,127 ; 0,172] | 360/1000 0,360 [0,330 ; 0,391] | 989/1000 0,989 [0,980 ; 0,995] | 903/1000 0,903 [0,883 ; 0,921] |

Appartenance : interieur, sommet, extreme, bruite sont des membres de toutes les classes (nul limité, v9 du banc, classes des fiches) ; sous_population et grille ne sont membres que du v9 du banc (pour v8, limité et les fiches, ces lignes sont des copies **hors classe** : leurs promotions y sont le trou attendu, pas une erreur de taille). Pour v8, les six lignes sont hors classe (aucune n'est un mélange sans coupure) : ses promotions sont les dents du banc. log W maximal sur tous les mondes : ≤ 0 pour v9, limité, moitié jugée, croisées, sous-échantillons, confiance et lecture dense dans les cas de leur classe.

Sources : `sortie-taille-interieur-v1.json` ; `sortie-taille-interieur-dense-v1.json` ; `sortie-taille-sommet-a-v1.json` ; `sortie-taille-sommet-b-v1.json` ; `sortie-taille-sommet-dense-v1.json` ; `sortie-taille-extreme-a-v1.json` ; `sortie-taille-extreme-b-v1.json` ; `sortie-taille-bruite-a-v1.json` ; `sortie-taille-bruite-b-v1.json` ; `sortie-taille-sous_population-a-v1.json` ; `sortie-taille-sous_population-b-v1.json` ; `sortie-taille-grille-a-v1.json` ; `sortie-taille-grille-b-v1.json` (empreintes en section 9).

### 5.2 Puissance : vraie découverte, une composante neuve, mêmes tirages et mêmes instants (300 mondes par dose)

| méthode | λ = 0,25 | λ = 0,40 | λ = 0,55 | écart apparié au v9 (seule la méthode / seul le v9) |
|---|---|---|---|---|
| v8 | 0,383 | 0,723 | 0,910 | +0,303 (91/0) ; +0,230 (69/0) ; +0,110 (33/0) |
| limite | 0,130 | 0,603 | 0,847 | +0,050 (15/0) ; +0,110 (33/0) ; +0,047 (14/0) |
| v9 | 0,080 | 0,493 | 0,800 | référence |
| v9_dense | 0,087 | 0,520 | 0,800 | +0,007 (2/0) ; +0,027 (8/0) ; +0,000 (0/0) |
| moitie_jugee | 0,010 | 0,177 | 0,500 | -0,070 (1/22) ; -0,317 (2/97) ; -0,300 (1/91) |
| croisee | 0,013 | 0,230 | 0,620 | -0,067 (1/21) ; -0,263 (1/80) ; -0,180 (0/54) |
| sous_echantillons | 0,010 | 0,270 | 0,637 | -0,070 (0/21) ; -0,223 (2/69) ; -0,163 (0/49) |
| confiance | 0,013 | 0,277 | 0,650 | -0,067 (0/20) ; -0,217 (1/66) ; -0,150 (0/45) |
| penalise_1nat | 0,127 | 0,563 | 0,830 | +0,047 (14/0) ; +0,070 (21/0) ; +0,030 (9/0) |
| melange_a_priori | 0,130 | 0,557 | 0,827 | +0,050 (15/0) ; +0,063 (19/0) ; +0,027 (8/0) |
| fiche_en_ligne_0.05 | 0,957 | 0,987 | 0,997 | +0,877 (263/0) ; +0,493 (148/0) ; +0,197 (59/0) |
| fiche_moitie | 0,643 | 0,800 | 0,907 | +0,563 (174/5) ; +0,307 (100/8) ; +0,107 (42/10) |

Intervalles par cellule dans les sorties ; valeurs p exactes de McNemar dans `sortie-appariement-puissance-v1.json`. Le v9 est identique monde par monde dans les lots « a » et « b » (vérifié par le script d'appariement). Les lignes penalise_1nat, melange_a_priori et fiches sont sans objet en puissance (méthodes non valides), données pour l'apparier.

### 5.3 Grille fine (19 seuils par trait), λ = 0,25, 200 mondes (seuil d'archive tiré hors de la grille fine : mondes non appariés à 5.2 ; `sortie-puissance-0.25-fine-v1.json`)

| v8 | limité | v9 du banc | confiance |
|---|---|---|---|
| 0,390 [0,322 ; 0,461] | 0,155 [0,108 ; 0,213] | 0,075 [0,043 ; 0,121] | 0,020 [0,005 ; 0,050] |

### 5.4 Coût par carte (secondes, un processus, machine partagée ; 20 mondes par colonne)

| méthode | copie (interieur) | découverte (λ = 0,40) |
|---|---|---|
| v8 | 0,114 | 0,101 |
| limite | 0,131 | 0,112 |
| v9 | 0,167 | 0,149 |
| v9_dense | 0,272 | 0,241 |
| moitie_jugee | 0,114 | 0,084 |
| croisee | 0,219 | 0,178 |
| sous_echantillons | 0,420 | 0,370 |
| confiance | 0,279 | 0,233 |
| penalise_1nat | 0,165 | 0,147 |
| penalise_bic | 0,159 | 0,144 |
| melange_a_priori | 0,160 | 0,138 |
| fiche_en_ligne_0.05 | 0,004 | 0,003 |
| fiche_en_ligne_0.2 | 0,004 | 0,003 |
| fiche_moitie | 0,161 | 0,114 |

Les lignes penalise_* et melange_a_priori recomptent le v9 qu'elles réutilisent (leur coût propre est nul). Le juge réel (toutes les coupures, membres log-linéaires) est plus cher ; seuls les rapports comptent.

## 6. L'artefact : ce que le banc voit des deux façons non valides

- **Poids appris en ligne (argon-p2-01)** : copie exacte d'un membre promue dans 955 à 1 000 mondes sur 1 000 (η = 0,05) et
  999 à 1 000 sur 1 000 (η = 0,2), dans chacun des quatre cas de membres du nul limité ; log W maximal jusqu'à 176. Échec net.
- **Poids ajustés sur une moitié (argon-p1-01)** : 435 (interieur), 97 (sommet), 148 (extreme), 360 (bruite) sur 1 000, au
  lieu de 0 ; bornes basses de Clopper-Pearson toutes au-dessus de 0,079, donc au-dessus de α. Échec net, plus faible au bord
  du simplexe.
- Le même banc, sur les mêmes mondes, rend 0 sur 1 000 au v9, au nul limité et aux quatre variantes à découpe correctes :
  **le banc voit l'échec et ne voit pas d'échec là où la preuve n'en laisse pas**.
- **Angle mort déclaré** : une pénalité vers le bas plus petite que log(1/α) (ici 1 nat) n'est pas vue, parce que le banc
  ne joue que des copies exactes (W ≤ 1) ; il faudrait des cartes voisines du monde sans en être des copies (ligne Q7 du
  préenregistrement de l'idée 1.1) pour la voir. Le défaut est démontré (section 4.9), pas mesuré.
- Ces chiffres recoupent, par un autre programme et d'autres mondes, ceux de la preuve du nul limité (§ 8.3) et de la
  contre-lecture (§ 4) ; je ne les compare pas un à un (familles de mondes différentes).

## 7. Ce que j'ai écarté, et pourquoi

1. **Valeur e contre l'enveloppe convexe du nul (projection d'information inverse), poids appris sur la carte.** Pour une
   carte q fixée, p* = argmin sur l'enveloppe convexe des lois jointes du nul de KL(q ‖ p) donne E_θ[q/p*] ≤ 1 pour tout membre
   θ, sans le surplus de masse du maximum : c'est la seule façon d'« apprendre les poids » qui regagnerait la puissance sans
   perdre la taille (les poids dépendent de la carte et du plan, jamais des tirages ; pour une copie, p* = q et W = 1).
   Écartée ici : sur les 200 tirages joints et une classe continue, je ne sais ni la calculer exactement ni **certifier**
   E_θ[q/p] ≤ 1 pour tous les θ (une approximation sur un ensemble fini de membres n'est valide que pour ces membres) ; la
   version tirage par tirage est vide, car les lois certaines δ_k font de l'enveloppe à un tirage le simplexe entier (W = 1).
   Référence à vérifier sur pièce : Grünwald, de Heide et Koolen, « Safe testing » ; c'est l'option (ii) du § 8.4 de la
   preuve du nul limité. Piste nommée, hors de mon angle.
2. **Suite de confiance apprise sur les mêmes tirages** (région C_t calculée sur le passé, maximum restreint à C_t) : valide,
   mais sur C_t toute loi a q/L_θ < 1/β, si bien que la promotion n'arrive que quand C_t se vide, c'est-à-dire quand le v9
   franchit le seuil 1/β = 40 : dominée par le v9 au seuil 20. Pas jouée.
3. **Produit des valeurs e de deux moitiés** : valide, sous le v9 trajectoire par trajectoire (lemme C, remarque). Pas jouée.
4. **Poids bornés loin du bord** (μ ≥ ε, « lissage » des poids) : c'est un nul plus petit, qui ne contient plus les copies
   au sommet (cas « sommet » : une loi connue par morceau) ; même prix que la restriction, sans le choix explicite des
   coupures. Pas jouée.
5. **Vérifier E_θ[q/D] ≤ 1 par simulation** pour un dénominateur appris : un essai sur des membres tirés au hasard n'est pas
   une preuve (le pire membre est au bord, là où la simulation tire peu) ; écarté comme méthode, gardé comme banc.
6. **Numérateur appris** (pari à fraction, alternative ré-estimée sur le passé) : valide (variante séquentielle), mais hors
   du sujet des poids du nul, et sans gain attendu quand la carte est la loi du monde.

## 8. Ce que cela changerait à la conception scellée (je nomme, je ne tranche pas)

- **Aucune** des méthodes valides de cet angle ne bat le v9 du banc en puissance, sauf la lecture dense (+0,007 / +0,027 /
  0). Ma lecture : dans l'angle « inférence universelle », la puissance perdue par le v9 n'est pas une erreur de méthode
  qu'on corrigerait en apprenant mieux les poids ; c'est le prix de la classe du nul (lemme A ; surplus de masse du
  maximum, lemme B). Ce prix vient surtout, sur ce banc, de la liberté des poids par morceau (v8 → limité : −0,253 / −0,120 /
  −0,063), moins de la recherche des coupures (limité → v9 : −0,050 / −0,110 / −0,047 ; la grille fine ne l'augmente pas
  nettement : 0,075 contre 0,080, mondes non appariés).
- **Nœud 1 (directeur) : lecture dense.** Instants écrits dans l'engagement et dans la règle d'arrêt de la valeur e (e-BH) ;
  gain faible, aucune perte de taille par la preuve. Recommandation : ne pas en faire une version du juge pour ce seul gain ;
  la garder en réserve si un autre changement ouvre une version.
- **Nœud 2 (directeur) : région de confiance (lemme D).** Valide, la meilleure des variantes à découpe, mais sous le v9 ici ;
  à rééprouver seulement sur un banc où le prix des coupures domine (mondes à 8 traits, toutes les coupures du vrai v9).
- **Les autres voies de regain sont hors de cet angle** : restreindre la classe (nul limité, nœud R-1779 déjà ouvert) ou
  changer la forme de la valeur e (projection inverse, à certifier). Les deux sont des décisions de dessin du juge.
- **Correction à porter au relevé** (déjà dite par la preuve du nul limité, § 9) : les fiches argon-p1-01 et argon-p2-01
  ne sont pas valides ; ajouter fable-p1-05 (mélange à poids fixes au dénominateur), que le banc voit aussi échouer.

## Citations obligatoires (N-064, N-067)

POPPER (Huang et al., ICML 2025), `docs/sources/pdf/huang-2025-icml-pmlr-267-popper-automated-hypothesis-validation-agentic-sequential-falsifications.pdf` ;
Dwork et al., arXiv 1506.02629 (2015) ; Blum et Hardt, « The Ladder », arXiv 1502.04585 (2015) ; Co-Scientist (Gottweis et
al., Nature 655, p. 487-496, 2026) ; Qu, Chen et Wang, « Propose, Don't Judge », arXiv 2609.27051 — chemins et empreintes
dans la preuve du nul limité. Références de méthode, **toutes à vérifier sur pièce** (aucun PDF lu, aucun chiffre repris) :
Wasserman, Ramdas et Balakrishnan, « Universal inference » ; Berger et Boos (1994) ; Grünwald, de Heide et Koolen, « Safe
testing » ; Shtarkov (1987) ; Rissanen (1996) ; Ville (1939). Aucune revendication.

## 9. Fichiers de ce dossier et empreintes (chaque fichier a son compagnon `.sha256`)

| fichier | sha256 |
|---|---|
| `banc_universelle_v1.py` | `68381bc5de78d928af29c6fae5084145f420911eca91873de9d929d6ebc6cb12` |
| `essai_universelle_appariement_v1.py` | `87bef4a6156e5a10245826ac6a11d4ea31f40c2689003436c0721088f7b9aef1` |
| `essai_universelle_cout_v1.py` | `67ca2824054d95629296751859ce67d49c3875a133b3484f9830bee21989f2dc` |
| `essai_universelle_lot_v1.py` | `fd7cc43d00164ea23157d0908412d7de722625c1fefb657354019a6112d85126` |
| `essai_universelle_taille_v1.py` | `62e7481a11a475a5626a889b59394afc63bbc2dd35cd391a9810762194a6b97c` |
| `journal-cout.txt` | `b352d65b99433c59ba4976bd6737246d172e204a20a10a33ee5c465399bfd9d4` |
| `journal-puissance-0.25-a.txt` | `8c54ba5e522ac96b36d9eaa87458f5e83986c2b1b16e6ab2e6befc892769f86a` |
| `journal-puissance-0.25-b.txt` | `419d1675142197f0333bce136b63081cbe0b904a9530dc52b04d190b839cfb0e` |
| `journal-puissance-0.25-fine.txt` | `e3f2e0064abd44957e8a3b745c9b24600647d8dda08e1d781c1ef718bcc76345` |
| `journal-puissance-0.40-a.txt` | `5dc9f571813337f864213617bf5214e090db54cf1ee4598b02d0d3ae882c4444` |
| `journal-puissance-0.40-b.txt` | `71989250f6998089ea3769bda41c73f8379cc4e64433b196edf31dd6a63567b5` |
| `journal-puissance-0.55-a.txt` | `c737383718177571990ebe49fcfa2922c8f94bee57ac0d1502ca39b702b0d135` |
| `journal-puissance-0.55-b.txt` | `b38adb31f5cbcbb0419a5db1cfae83170011386d324756ae06aecc3c491cbf36` |
| `journal-taille-bruite-a.txt` | `e904df325115ced54fd1ebf0edda0495f220c3ba8b84f278cf71c9356a461e2c` |
| `journal-taille-bruite-b.txt` | `6ecd4b90e6a022a4551ba3422965f5d033d7922273fcf81b934b993d73ae93c5` |
| `journal-taille-extreme-a.txt` | `6ee2e1eae2e5c212c01ed475a21ca06f6736f4150879023e495cb8277fc5c309` |
| `journal-taille-extreme-b.txt` | `ba570d07e5748d241d719fe8f2c646aeb5d582e9e77cbad3d7a6df694f87c8c4` |
| `journal-taille-grille-a.txt` | `cb6c0486c0a708319ccf86cfa0d2477d95865fa2cfc01b6122cef236f0f85e8e` |
| `journal-taille-grille-b.txt` | `ed8c977752fb13124c411aa115eef90e7156458ed31bb5806eb93c7e203ed95a` |
| `journal-taille-interieur-dense.txt` | `99707946181b4628aca1944dda0cc5b4fc5ddf2f11598df53ba5f93efde7f499` |
| `journal-taille-interieur.txt` | `c9c690fbd1039cc741b0f7870760d12ff2f44ca297f2a4bb3866ac1f8fbb8f7e` |
| `journal-taille-sommet-a.txt` | `bb4dbbbf08d2bb4e767e28259509c90edc1af22fa905e988da1ddc894e7d376b` |
| `journal-taille-sommet-b.txt` | `c983da7e06d44fe7156d7fdeb0f4d28acef47975b78281e36cd845b06db8a896` |
| `journal-taille-sommet-dense.txt` | `14c8430e9e4792d46cadc07352aaa0945fe683caa773235de2730f35d73bb785` |
| `journal-taille-sous_population-a.txt` | `2a4c42b9ddddab6a5cd9463a3b6534a31280450843cc4baa608c9bb2e8220241` |
| `journal-taille-sous_population-b.txt` | `9e5f5d7eff7c53d102432b77ea18af923accd496b4b312942827fd897d00a70d` |
| `sortie-appariement-puissance-v1.json` | `662874bd7f4fcb0f3b374c8b8a03d918881faa4476c7988a7afb56a2c0dea6d4` |
| `sortie-cout-v1.json` | `735b3661ba6f20f389e8dc0db2169587768554ace082376717d407771abb7f57` |
| `sortie-puissance-0.25-a-v1.json` | `73f1cb7ea7bfc0ff8292fd2b68fe28ad0dfe8baa02f50b4f0436cf7ac22b4f99` |
| `sortie-puissance-0.25-b-v1.json` | `0f98ed754412d0bbe0df2474433e07a2e1e9530689d079bd82e167a14db9ffd6` |
| `sortie-puissance-0.25-fine-v1.json` | `51e1f6ae73a205e1a88869b332d1c260d3696f68a14bc8495977c6aa98f012ae` |
| `sortie-puissance-0.40-a-v1.json` | `7794cb94a9aae07a24bdcb9b52be7bbf18ee6976ed4e82deaf6581a4209081d7` |
| `sortie-puissance-0.40-b-v1.json` | `cb1f5fd7cec793693e1aa2276bb871226182422d7a6f493328e3f88004aafd79` |
| `sortie-puissance-0.55-a-v1.json` | `4d6c9833c9a3e3e9e8e31c5e70eb63f3ed85d4716fe11ccfbec20d431a1d5b22` |
| `sortie-puissance-0.55-b-v1.json` | `f0d58436d5abec9eb41947c3a0e3b339c746b924b64179213fad599915c9e53f` |
| `sortie-taille-bruite-a-v1.json` | `26e226ca31ea998637bd07a5850b2325419e001d83e50c4dae73e37c9de5644f` |
| `sortie-taille-bruite-b-v1.json` | `b21a736453fc34d117b001b5796f90145543cd16d1d17042ecf8dd7c67793a3a` |
| `sortie-taille-extreme-a-v1.json` | `391796d0a7abd66deba68c2a454e5f5b470ce86e43d46bc051495f8e179eff78` |
| `sortie-taille-extreme-b-v1.json` | `8ab2d499200596e81e8c3389859592a2988151419b11628408f6b5e7b7bdb080` |
| `sortie-taille-grille-a-v1.json` | `f2111a21b9836a97ea97ad26a1dcdb7fe695b4f601dc4d4e49512c88d3da7949` |
| `sortie-taille-grille-b-v1.json` | `fba8843278ea9ffaf7b0231f82970ec0524e684af8f9f072562dd7907f9e6205` |
| `sortie-taille-interieur-dense-v1.json` | `25a1d56b0cd89edfa1637881f587e88cfb60decb886d4f77cd6546b99de02eec` |
| `sortie-taille-interieur-v1.json` | `8b4a1d3b3f1e1542b03d55eda7b50f29c11a82495b4b6f52c416e4790f413443` |
| `sortie-taille-sommet-a-v1.json` | `5973a2652c7ac442e09367f42b22bd90eec2a729c71840087dd518862a3f0504` |
| `sortie-taille-sommet-b-v1.json` | `d334b7c74a3dded14132cd58b722d84931d78796672ff464e31c8d64ba59e00f` |
| `sortie-taille-sommet-dense-v1.json` | `8a411d00b72d72c4b072abbc72d3de0c30d92b1da702c6311e4204c0c9548f83` |
| `sortie-taille-sous_population-a-v1.json` | `afc94c06035d7d1f77cba26b9449486afa961181cd34898e5a9ad44d3cd8bb9d` |
| `sortie-taille-sous_population-b-v1.json` | `1818972d4cd8eee9b608f79e7e420783e7912ed2c44d5548057b8f7069b02a88` |
