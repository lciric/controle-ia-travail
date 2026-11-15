# Apprendre les poids du nul sans perdre la taille — angle « projection d'information inverse (numéraire) » — v1

**Statut.** Mise au point exploratoire, **aucune revendication**. Toutes les issues sont rapportées à l'identique : les
méthodes qui échouent le sont avec leur chiffre. Aucun essai ne vise un signe. Rien n'est adopté : toute adoption au juge
est une décision de Lazar (section 9).

- **Auteur** : concepteur neuf, sous-agent de la session mère ; je n'ai écrit aucune des pièces citées.
- **Date** : 2026-11-15, de 09:14 à 13:30 UTC environ (`date -u`). Dépôt lu sur `main` (tête `88a19ce1`), lecture seule,
  aucun commit.
- **Calculs** : Python 3.13.18, numpy 2.4.6, scipy 1.17.1, processeur seul (machine partagée, 2 à 3 processus à moi).
  Aucun code des dossiers de copie n'a été exécuté : la logique utile est **recopiée** dans mes programmes (section 2).
- **Toutes les références de la littérature sont à vérifier sur pièce** ; aucun chiffre n'en est repris.

## 0. En bref

1. **Le principe qui répare.** Les poids du nul peuvent être choisis par n'importe quel moyen — calculés à partir de la
   carte (projection), appris sur les tirages **passés**, ou ajustés sur une moitié — **pourvu** qu'ils soient gelés avant
   un bloc de tirages et que la valeur e du bloc soit **divisée par son certificat exact** c^b, où
   c = max sur les sommets du nul de (1/b)·Σ_s Σ_y P_sommet(y | x_s)·q_s(y) / P_poids(y | x_s). Le certificat est une liste
   finie de sommes (lois discrètes connues) ; il ne dépend d'aucune convergence. Preuve : lemme 1 (section 3), par
   l'inégalité des moyennes, la linéarité du nul en ses poids et l'indépendance des tirages frais.
2. **Les blocs sont les huit intervalles entre instants de lecture** (25 tirages chacun) ; la richesse est une
   surmartingale aux huit instants ; Ville s'applique ; le nombre de familles (coupures) n'entre pas dans la garantie.
3. **Le meilleur choix certifié** sous la loi de la carte est la **projection d'information inverse** de la carte sur la
   famille, bloc par bloc (certificat = 1 à l'optimum, lemme 2 ; croissance maximale, proposition 3).
4. **Taille, sur 1 000 mondes par cas** (500 pour trois cas de bord de classe) : aucune des douze méthodes valides n'a
   promu une seule carte dont le monde est dans sa classe, sur 9 cas (copie exacte d'un membre, poids extrêmes, bord du
   simplexe, copie par morceaux sur une coupure de l'archive, cartes hors classe dans un monde de la classe), sauf M2 et
   M2c sur une carte neuve dans un monde coupé (1 et 3 sur 1 000, sous α). **Artefact** : sur les mêmes mondes, la façon
   « en ligne » des fiches promeut la copie exacte dans 93,3 % à 100 % des mondes, la façon « moitié » dans 58,2 % à 81,4 %.
5. **Puissance** (section 6) : la projection par blocs sur **toutes les coupures** (M3, même classe que le v9) promeut plus
   que le maximum certifié façon v9 (R9) sur les 9 lignes de vraies découvertes, de +0,045 à +0,185, et regagne de 0,41 à
   0,82 de la perte du v9 contre le v8 ; elle reste en dessous du membre linéaire seul (R8). Même signe, à classe égale, pour
   M1 contre R8 et M2b contre le nul limité RLa. Réserve : banc à moi, 100 à 200 mondes par dose, R9 recopié et simplifié.
6. **Les façons des fiches, corrigées par le certificat** (M7, M7b, M8) sont **valides mais sans puissance** : apprendre
   les poids sur les tirages fait exploser le certificat (une loi certaine sous-pondérée dans une cellule).
7. **Lois connues seulement par tirages** : le certificat « comme si exact » ne tient plus (21,5 % de fausses promotions à
   50 tirages par loi) ; un certificat robuste (boule de confiance) rend la taille ≤ α + δ, au prix de la puissance.

## 1. Pièces lues (empreintes recalculées, égales à leurs compagnons)

| pièce | chemin | sha256 |
|---|---|---|
| preuve de validité du nul limité | `docs/notes/organisme-idees-juge-v1/preuve-validite-nul-limite-v1.md` | `44f249409193778ccbaaa12b6c5e74d64434dfb87be77382d8bb9438459281b2` |
| préenregistrement de l'idée 1.1 | `docs/notes/organisme-idees-juge-v1/prereg-nul-par-morceaux-limite-v1.md` | `46ef2b92119ee5dff05727b90ca8bdd3ba57b52f9c1c75893750c792a2abc089` |
| contre-lecture | `docs/notes/organisme-idees-juge-v1/contre-lecture-prereg-nul-limite-et-preuve-v1.md` | `763fc6e29cd80868dcdb1d848eafdc928a39fca7244fa16eb0ac721ec705014e` |
| nul v9 (copie, lu, jamais exécuté) | `docs/notes/organisme-idees-juge-v1/copie-nul-v9-a41b7b5/orchestrator/pole/nul_v9.py` | `7ae450df2482246122bf9fbcf0fa5ef30b4a7e4c6f0d09531e83af048e46ee95` |
| pari, richesse, tirages frais | `docs/notes/organisme-courbe-dose-reponse-v1/code-organisme-94bfd92/orchestrator/pole/selection_pari.py` | `359928110d757cd54cc0d2773910c7360895b68cac5d17e0e4b4e9933ef306bc` |
| nul v8 | `…/orchestrator/pole/nul_v8.py` | `cc452aafd17121a7c0ec42829eea47063ffee1f6cdf7f642e264d528f976b888` |
| membres ajustés, 8 instants, certificats | `…/orchestrator/pole/nul_filles_v2.py` | `0ed9b4adbcddc4ad77a1c97d5cbd5706f14926e9c47fe96ce2bab3221a138910` |
| jugement d'une carte fraîche | `…/orchestrator/pole/a_blanc_v59.py` | `606aa8b4fcc38786b38cf2954da46533eed9384232a56100d22ff30b8ce0826c` |
| relevé d'idées, § 1.1 | `docs/notes/organisme-conception-propre-v1/relecture-exploratoire-v2/releve-idees-reutilisables-v1.md` | `bd253b6c68f6baada0e61b5381f029b52838ca34aa092502e55253c662451c6c` |
| fiches (argon-p1-01 n° 0, opus-p1-05 n° 9, fable-p1-05 n° 13, argon-p2-01 n° 14) | `runs/course-ideation-conception-propre-v1/20261113-235541-course-ideation-conception-propre-v1-g1/copies/sortie--fiches-validees.json` | `a9f9594e2dc3a7a553c54577202817758e3f7ef231445f1a48d500fc647389d5` |
| verdict de la validation du v9 (« puissance perdue ») | `docs/verdicts/verdict-validation-nul-v9-v1.md` (seul fichier ouvert de ce dossier) | `1407e460367754bb9f76b37174f3a21585970864eb9beaa2699494d90125c1ea` |

Ce que « puissance perdue » veut dire (verdict, section « Lecture selon la section 7 ») : le v9 tient sa taille (18 lignes
fatales sur 18) mais perd, contre le v8 apparié, 105 promotions sur 1 000 sur la ligne d'interaction faible I02 (0,381
contre 0,486), au-delà de la marge de 0,05 ; trois autres pertes (0,038 à 0,046) sont non jugeables.

Ce que les fiches demandent (champ `demande_organisme`, lu en entier) : argon-p2-01 met à jour en ligne, par descente
exponentielle, des poids par cellule (lois de l'archive et lois aveugles fixes) sur la partition des conditions de l'archive
(intersections d'au plus deux) et affirme une « martingale de valeur initiale 1 » ; argon-p1-01 ajuste ces poids par maximum
de vraisemblance sur la première moitié des tirages et évalue la valeur e sur la seconde ; opus-p1-05 et fable-p1-05 élargissent
le nul aux recollages sur une grille publique (maximum de vraisemblance, ou mélange à poids fixes).

## 2. Le banc (logique recopiée, simplifications dites)

Programmes : `essai_projection_commun_v1.py` (lois, familles, optimiseurs, certificats), `essai_projection_cas_v1.py`
(mondes et cartes), `essai_projection_methodes_v1.py` (bras), `essai_projection_taille_v1.py`,
`essai_projection_puissance_v1.py`, `essai_projection_tirages_v1.py`, `essai_projection_fusion_v1.py` (empreintes,
section 11).

- **Juge recopié** : plan de n = 200 instances (2 traits gaussiens, 2 sous-populations), K = 3 issues, instants
  T = {25, …, 200} (`cycle.instants_reguliers(200, 8)`), α = 0,05, promotion si log W_t ≥ log 20 en un instant de T
  (`nul_filles_v2.evaluer_v2`, carte seule), **pari plein** (numérateur = loi de la carte, comme `a_blanc_v59.juger_carte`,
  qui ne déclare pas `fractions`).
- **Archive** : celle du banc A2 du préenregistrement de l'idée 1.1 : S1, S2 softmax aléatoires ; S3 = si_sinon sur
  z_jA > s_A ; S4 = si_sinon sur z_(1−jA) > s_B ; lois connues L_1..L_4 = S1..S4 ; coupures de l'archive A et B, et leur
  partition commune à quatre cellules (F4, la partition des fiches).
- **Familles du nul**, linéaires en leurs poids : « bruit commun » (forme du membre linéaire du v8 et des membres par
  morceaux du v9 : poids des lois connues propres à la cellule, loi aveugle ρ commune) ; « bruit par cellule » (forme des
  fiches : un simplexe par cellule sur les 4 lois connues et les 3 lois certaines).
- **Simplifications** : les membres ordinaires du v8 autres que le membre linéaire (marginale d'entraînement, moyennes
  glissantes) et le membre log-linéaire ne sont pas au banc ; ils entreraient à l'identique, par minimum, dans tous les bras.
  Les références par maximum de vraisemblance sont prises à la **valeur atteinte** par l'EM (borne basse du maximum), ce qui
  leur est **plus favorable** que le certificat du v9 : tout écart de puissance en faveur d'une méthode de projection est
  donc plutôt sous-estimé. La référence « façon v9 » (R9) parcourt, à chaque instant t, toutes les coupures des deux traits
  entre valeurs des t premières instances et la sous-population ; elle élague par 25 pas d'EM puis affine les 8 meilleures
  coupures sur 300 pas (élagage heuristique : il ne peut que baisser le dénominateur, donc avantager R9).
- **Optimiseurs** : EM pondéré (projection : poids q_s(y) ; maximum de vraisemblance : issue observée), accéléré par SQUAREM
  avec garde (un pas accéléré n'est gardé que s'il reste intérieur et ne fait pas baisser la valeur). Le certificat rend tout
  état de l'optimiseur valide ; le nombre de pas ne coûte qu'en puissance (300 pas ; M3 : départ chaud depuis la projection
  sans coupure du bloc puis 150 pas).
- **Graines** : `numpy.random.SeedSequence(entropy=racine, spawn_key=(…))`, racines 2026111509 (taille), 2026111510
  (puissance), 2026111511 (tirages), dérivation écrite dans chaque sortie.
- **Nombre de mondes et durée** : la machine était partagée avec d'autres agents (charge 9 à 13 sur 4 cœurs). Pour tenir
  chaque simulation sous dix minutes, chaque cas est découpé en tranches de 250 (ou 500) mondes, chacune une simulation à
  part, fusionnées ensuite (contiguïté vérifiée). Réductions **dites** : trois cas de taille de bord de classe (T06, T08,
  T09) sur 500 mondes au lieu de 1 000 ; deux cas prévus (T02 « une loi connue seule », T07 « copie par sous-population »)
  et un cas de carte surconfiante (T11) **non joués**, faute de temps de calcul ; puissance sur 200 mondes par dose (V1,
  V4) et 100 (V3).

## 3. Le lemme commun : projection par blocs, validité certifiée composante par composante

**Cadre.** Une famille du nul F = {P_θ : θ ∈ Θ} est **linéaire en ses poids** : pour chaque instance x, θ ↦ P_θ(· | x)
est affine sur un polytope Θ dont on connaît la liste finie V des sommets. C'est le cas du membre linéaire du v8
(`ajuste_lineaire:archive` : sommets = une loi connue L_j, ou une loi certaine δ_k) et de chaque membre par morceaux du v9
(`ajuste_morceaux` : sommets = une loi connue par cellule, ou une loi certaine δ_k commune ; `nul_v9.py`, l. 19 à 25 et
`_certificats`, l. 218 à 229). Ce n'est **pas** le cas du membre log-linéaire (`ajuste_log`) ni des moyennes glissantes :
ils restent jugés comme aujourd'hui, et se combinent par minimum (section 3.4).

Les instants de lecture T = {25, 50, …, 200} découpent le plan gelé en huit **blocs** B_1, …, B_8 de 25 instances.

**Définition (valeur e de bloc).** Pour un bloc B (|B| = b) et une loi φ ∈ Θ choisie avant les issues du bloc :
- r_s(y) = q_s(y) / P_φ(y | x_s), pour s ∈ B et chaque issue y ;
- **certificat** c_B(φ) = max_{v ∈ V} (1/b)·Σ_{s ∈ B} Σ_y P_v(y | x_s)·r_s(y) — une liste finie de sommes, calculée
  exactement (lois discrètes connues) ;
- e_B = Π_{s ∈ B} r_s(y_s) / max(1, c_B)^b.
La richesse de la famille F à l'instant t_b (fin du bloc b) est W^F_{t_b} = Π_{b' ≤ b} e_{B_b'}.

**Hypothèses (numérotées).**
- **P1 (gel).** La carte q, le plan x_1..x_n, les instants T, la liste des familles et des blocs sont fixés avant les
  tirages frais (empreinte de l'engagement), comme H1 de la preuve du nul limité.
- **P2 (fraîcheur et ordre).** Sous un monde de la famille, les issues rangées dans l'ordre du plan sont indépendantes
  sachant les instances, y_s ~ P_θ(· | x_s), avec un même θ ∈ Θ au moins à l'intérieur de chaque bloc (H2, H6 de la preuve
  du nul limité).
- **P3 (dénominateur prévisible).** La loi φ_b du bloc b ne dépend que de l'engagement et des issues des blocs précédents.
- **P4 (numérateur gelé par bloc).** q_s ne dépend que de x_s et des issues des blocs précédents (pari plein : vrai ;
  pari à fraction de `trajectoire_numerateur`, qui lit les issues du bloc courant : faux, voir M9).
- **P5 (positivité).** P_φ(y | x_s) > 0 pour toute issue y où q_s(y) > 0.
- **P6 (linéarité).** θ ↦ P_θ(y | x) affine sur Θ, de sommets V (ci-dessus).

**Lemme 1.** Sous P1 à P6, pour tout θ ∈ Θ : E_θ[e_B | issues des blocs précédents] ≤ 1.

*Preuve.*
1. Sachant le passé, φ et q sont fixés (P3, P4) ; les issues du bloc sont indépendantes (P2). Donc
   E_θ[Π_s r_s(y_s)] = Π_s m_s(θ), avec m_s(θ) = Σ_y P_θ(y | x_s)·r_s(y) ≥ 0 (fini par P5).
2. Inégalité des moyennes arithmétique et géométrique : Π_{s ∈ B} m_s(θ) ≤ ((1/b)·Σ_s m_s(θ))^b.
3. (1/b)·Σ_s m_s(θ) est affine en θ (P6) : son maximum sur le polytope Θ est atteint en un sommet, donc il vaut au plus
   c_B(φ), quel que soit θ.
4. E_θ[e_B | passé] ≤ (c_B / max(1, c_B))^b ≤ 1. ∎

Le certificat ne suppose **aucune convergence** de l'optimiseur : quelle que soit φ, la division par max(1, c_B)^b rend
e_B valide ; un φ mal ajusté coûte b·log c_B nats de puissance, jamais de la validité. C'est la consigne « on divise par la
borne certifiée si elle dépasse 1 », bloc par bloc.

**Lemme 2 (la projection a un certificat égal à 1).** Si φ* minimise Σ_{s ∈ B} KL(q_s ‖ P_θ(· | x_s)) sur Θ (projection
d'information inverse de la carte sur la famille, calculée à partir de q, des lois connues et du plan seuls), alors
c_B(φ*) = 1.

*Preuve.* La fonction θ ↦ Σ_s KL(q_s ‖ P_θ) est convexe (P6). Condition d'optimalité au point φ* : pour tout θ ∈ Θ, la
dérivée dans la direction θ − φ* est ≥ 0, soit −Σ_s Σ_y q_s(y)·(P_θ − P_φ*)(y | x_s) / P_φ*(y | x_s) ≥ 0, donc
Σ_s m_s(θ) ≤ Σ_s Σ_y q_s(y) = b. Avec θ = un sommet, c_B ≤ 1 ; avec θ = φ*, m_s = 1, donc c_B = 1. ∎

**Proposition 3 (la projection est le meilleur choix certifié sous la loi de la carte).** Si le monde suit la carte q,
pour toute φ ∈ Θ : E_q[log e_B(φ)] ≤ E_q[log e_B(φ*)] = Σ_{s ∈ B} KL(q_s ‖ P_φ*(· | x_s)).

*Preuve.* E_q[log e_B(φ)] = Σ_s E_q[log(q_s / P_φ*)] + Σ_s E_q[log(P_φ* / P_φ)] − b·log max(1, c_B(φ)). Par l'inégalité de
Jensen, Σ_s E_q[log(P_φ* / P_φ)] ≤ b·log((1/b)·Σ_s Σ_y q_s(y)·P_φ*(y | x_s) / P_φ(y | x_s)) = b·log((1/b)·Σ_s m_s(φ*; φ))
≤ b·log c_B(φ). Le second terme est donc compensé par le troisième. ∎

C'est le sens précis de « poids calculés, non ajustés » : les poids du nul sont ceux de la projection de la carte ; ils ne
lisent aucune issue du bloc jugé, et parmi tous les choix prévisibles certifiés ils maximisent la croissance attendue de la
richesse sous l'hypothèse que la carte est vraie. **Réserve.** Le vrai numéraire du bloc (au sens de Larsson, Ramdas et Ruf,
à vérifier sur pièce) est q^B / P_{W*}, où P_{W*} est le mélange, sur θ, des lois produits Π_s P_θ(· | x_s), sous un a priori
W* le moins favorable (projection d'information inverse sur l'enveloppe convexe des lois produits ; « Safe testing » de
Grünwald, de Heide et Koolen, à vérifier sur pièce). Il exige des sommes sur 3^25 suites par bloc : non calculable ici. La
valeur e du lemme 1 est valide et au plus égale à ce numéraire en croissance ; elle n'en est pas l'égale.

**Théorème 4 (processus, plusieurs familles, huit instants).** Soit une liste finie de familles F_1, …, F_M fixée avant les
tirages (P1), chacune vérifiant P6, et W_t = min_m W^{F_m}_t aux instants de T. Sous un monde de l'une des familles
(P2 pour cette famille), P(∃ t ∈ T : W_t ≥ 1/α) ≤ α.

*Preuve.* Pour la famille F* du monde, W^{F*} est, aux fins de bloc, une surmartingale positive de départ 1 (lemme 1 et
conditionnement emboîté). W ≤ W^{F*}. Inégalité de Ville sur les huit fins de bloc. ∎

Le nombre M de familles n'entre pas dans la borne (comme pour le maximum du v9). La valeur e pour la règle e-BH (W arrêtée au
premier instant où elle atteint m/α) est un temps d'arrêt de la filtration des blocs : E ≤ 1 (arrêt optionnel), comme
la section 5 de la preuve du nul limité.

**Combinaison avec les membres non linéaires.** Le juge garde, pour les membres ordinaires et log-linéaires, son
dénominateur actuel (maximum certifié sur les tirages mêmes). La richesse retenue est min(W_actuelle_sans_membres_linéaires,
W_projection) : chacune est valide sous sa classe, le minimum l'est sous l'union.

## 4. Les méthodes, une par une

Notations du juge : carte q (pari plein), plan x_1..x_200 gelé, tirages frais y_s, instants T et blocs B_1..B_8,
membres de l'archive (lois connues L_j, lois certaines δ_k), coupures (A, B de l'archive ; toutes les valeurs du plan
pour la façon v9). « Classe » = ensemble des mondes sous lesquels la garantie de taille vaut. Les chiffres de taille
viennent de `sortie-taille-v1.json` (section 11) ; ceux de puissance de `sortie-puissance-v1.json`.

### M1 — projection par blocs sur le membre linéaire du v8 (mélange fini)
- **Énoncé.** Famille F_lin : P_θ(y | x) = Σ_j π_j·L_j(y | x) + ρ_y. Pour chaque bloc, φ_b = projection de q sur F_lin
  (EM pondéré par q_s(y), sur les 25 instances du bloc, sans issue) ; e_b du lemme 1 ; W = produit.
- **Validité.** Lemme 1 (P6 : sommets L_j et δ_k) et lemme 2 ; théorème 4 avec M = 1. Classe : celle du membre linéaire.
- **Taille.** 0 promotion sur 1 000 pour T01 (copie exacte), T03 (poids 0,97 / 0,03), T04 (loi aveugle constante, sommet
  du simplexe), Clopper-Pearson [0 ; 0,0037] ; plus grand log W d'une copie 0,047. Hors classe (mesuré, sans garantie) :
  T05 987/1 000, T10 31/1 000 — le banc voit bien qu'une copie par morceaux n'est pas dans le membre linéaire.
- **Puissance, coût, conception** : sections 6, 7 et 9.

### M2 — projection par blocs sur la partition à quatre cellules de l'archive, bruit commun (F4)
- **Énoncé.** Famille F4 (cellules = intersections des coupures A et B), poids propres à la cellule, ρ commun ; projection
  par bloc ; lemme 1. Elle contient F_lin, F_A, F_B et la copie à deux niveaux sur les coupures de l'archive.
- **Validité.** Lemme 1 (sommets : une loi connue par cellule, ou δ_k) ; classe F4.
- **Taille.** 0/1 000 sur T01, T03, T04, T05, T12 ; 0/500 sur T08 (copie par morceaux avec bruit commun) et T09 (deux
  niveaux) ; **1/1 000** sur T10 (carte neuve, monde coupé ; [0 ; 0,0056]) — sous α. Hors classe : T06 (coupure hors
  archive) 458/500.

### M2b — minimum des projections par blocs sur F_lin, F_A, F_B
- **Énoncé.** Trois processus (M1 et une projection par coupure de l'archive), minimum aux instants (théorème 4, M = 3).
  Version « projection » du nul limité aux coupures de l'archive (La de l'idée 1.1).
- **Taille.** 0/1 000 sur T01, T03, T04, T05, T10, T12 ; 0/500 sur T08. Hors classe : T06 462/500, T09 482/500.

### M3 — minimum des projections par blocs sur F_lin, la sous-population et toutes les coupures du plan (façon v9)
- **Énoncé.** Pour chaque trait j et chaque valeur c du plan gelé, la coupure z_j > c ; plus la sous-population ; plus
  F_lin ; 402 familles en tout, chacune un processus par blocs ; W = minimum. Calcul : dans un bloc de 25, une coupure
  n'induit que 26 partitions ; chacune est projetée une fois (8 × 2 × 24 projections + 16), puis chaque coupure additionne
  ses 8 blocs. Le plan étant gelé, la liste des coupures est fixée avant les tirages (P1) ; toute coupure réelle s
  induit sur le plan la même partition qu'une valeur c du plan : la classe est **celle du v9** (un niveau, bruit commun).
- **Validité.** Théorème 4 ; le nombre de coupures n'entre pas dans la borne.
- **Taille.** 0/1 000 sur T01, T03, T04, T05, T10, T12 ; 0/500 sur T06 (coupure hors archive) et T08 ; plus grand log W
  d'une copie 0,25 (T08). Hors classe : T09 (deux niveaux) 471/500 — le même trou que le v9.

### M4 — projection à horizon fixe à chaque instant, seuil de Bonferroni
- **Énoncé.** À chaque t ∈ T, un seul « bloc » = les t premières instances ; projection sur F4 ; e^(t) du lemme 1 ;
  promotion si un e^(t) ≥ 8/α (borne de l'union sur les 8 instants).
- **Validité.** Lemme 1 à chaque t (horizon fixé d'avance), puis union : P ≤ 8·(α/8) = α.
- **Taille.** 0 sur tous les cas de sa classe (comme M2). Hors classe : T06 446/500.

### M5 — projection pas à pas (blocs d'une seule instance) avec bruit aveugle — **valide, sans puissance par nature**
- **Énoncé.** Comme M1 avec des blocs de taille 1 (projection recalculée à chaque instant).
- **Pourquoi elle échoue.** Les lois certaines δ_k sont des sommets du nul : c_s ≥ q_s(k) / P_φ(k | x_s) pour tout k, donc
  e_s ≤ 1 à chaque pas, **quel que soit φ** (pour une instance seule, le nul contient toutes les lois constantes, c'est-à-dire
  tout le simplexe). C'est la raison exacte pour laquelle la version séquentielle demande des blocs longs.
- **Mesure.** 0 promotion partout, taille et puissance (log W max ≤ 0 partout).

### M6 — projection pas à pas sur l'enveloppe des lois connues (sans bruit aveugle), en minimum avec M1
- **Énoncé.** À chaque instance, φ_s = projection de q_s sur conv{L_1(x_s), …, L_4(x_s), uniforme} ; certificat par pas
  c_s = max_j Σ_y L_j(y | x_s)·q_s(y) / φ_s(y) ; e_s = q_s(y_s) / φ_s(y_s) / max(1, c_s). W = min(W_pas, W_M1).
- **Validité.** Lemme 1 avec b = 1 et θ libre à chaque pas : la classe couverte est **tout monde dont la loi, à chaque
  instance, est un mélange des lois connues et de l'uniforme, avec des poids qui peuvent varier d'une instance à l'autre**
  (même en lisant l'historique). Elle contient toutes les copies par morceaux, à toute profondeur, sur toute coupure, oblique
  ou douce (aiguillage doux), plus la classe de M1 par le minimum.
- **Taille.** 0/1 000 sur T01, T03, T04, T05, T10, T12 ; 0/500 sur T06 et **T09 (deux niveaux, que le v9 et M3 laissent
  passer)**. Trou : T08 (copie par morceaux avec un bruit aveugle commun non uniforme) **41/500**, hors de sa classe.
- **Question de sens** : cette classe tient pour « rien de neuf » toute loi qui reste, instance par instance, dans
  l'enveloppe des lois connues ; c'est plus large que « recombinaison par morceaux » (section 9).

### M2c — projection par blocs sur F4 « bruit par cellule » (la famille même des fiches)
- **Énoncé.** Comme M2 sur la famille des fiches (lois certaines propres à chaque cellule) ; certificat aux sommets « une
  composante par cellule ».
- **Taille.** 0 sur sa classe sauf **3/1 000** sur T10 ([0,0006 ; 0,0087]), sous α. Hors classe : T06 451/500.

### M7 — poids appris sur le passé (façon argon-p2-01), gelés par bloc, divisés par le certificat
- **Énoncé.** Famille des fiches ; φ_b = maximum de vraisemblance sur les issues des blocs précédents (uniforme au premier
  bloc) ; e_b divisé par max(1, c_b)^25.
- **Validité.** Lemme 1 (P3 : φ_b ne lit que le passé). **C'est la correction valide de la fiche argon-p2-01.**
- **Taille.** 0 partout dans sa classe. Plus grand log W d'une copie 1,87 (T03).
- **Échec en puissance** (section 6) : les poids appris donnent une probabilité très faible à une issue dans une cellule
  là où la carte en met ; le sommet δ_k de cette cellule fait monter c_b, et 25·log c_b efface tout gain.

### M7b — comme M7, poids mêlés à moitié avec la projection de la carte
- **Énoncé.** φ_b = ½·(maximum de vraisemblance sur le passé) + ½·(projection de q sur le bloc), un point de la famille.
- **Validité.** Lemme 1. **Taille** : 0 partout dans sa classe. **Puissance** : section 6.

### M8 — poids ajustés sur la première moitié (façon argon-p1-01), certificat par bloc sur la seconde
- **Énoncé.** φ = maximum de vraisemblance sur les blocs 1 à 4 ; blocs 5 à 8 divisés chacun par leur certificat ; lecture
  aux instants 125 à 200.
- **Validité.** Lemme 1 (φ gelée avant le bloc 5). **C'est la correction valide de la fiche argon-p1-01.**
- **Taille.** 0 partout dans sa classe. **Puissance** : section 6.

### M9 — alternative prévisible à fraction, projection par bloc (version séquentielle de l'alternative)
- **Énoncé.** Pour λ ∈ {0,25 ; 0,5 ; 0,75 ; 1}, q^λ_b = λ·q + (1 − λ)·m̂_b, m̂_b = marginale de Laplace des issues des blocs
  passés, gelée au début du bloc ; projection de q^λ_b sur F4 ; W = moyenne sur λ des quatre processus.
- **Validité.** Lemme 1 pour chaque λ (P4 : q^λ ne lit que le passé), moyenne de surmartingales. Le pari à fraction
  actuel du juge (`trajectoire_numerateur`) **lit les issues du bloc courant** : il ne satisfait pas P4 et ne peut pas être
  employé tel quel avec un dénominateur par blocs ; M9 en est la forme compatible.
- **Taille.** 0 partout dans sa classe.

## 5. Artefact obligatoire : les deux façons des fiches, sans correction, dans le même banc

Mêmes mondes, mêmes tirages, même famille (F4 « bruit par cellule », celle des fiches). Taux de promotion de la carte
(`sortie-taille-v1.json`) :

| façon | T01 copie exacte | T03 poids extrêmes | T04 loi aveugle constante | T05 copie coupure archive | T08 bruit commun | T09 deux niveaux |
|---|---|---|---|---|---|---|
| A1 en ligne, pas 0,05 (argon-p2-01) | 933/1 000 | 1 000/1 000 | 992/1 000 | 1 000/1 000 | 500/500 | 500/500 |
| A1 en ligne, pas 0,2 | 1 000/1 000 | 1 000/1 000 | 1 000/1 000 | 1 000/1 000 | 500/500 | 500/500 |
| A2 moitié, lu à 200 (argon-p1-01) | 814/1 000 | 641/1 000 | 795/1 000 | 582/1 000 | 371/500 | 283/500 |
| A2 moitié, lu de 125 à 200 | 847/1 000 | 663/1 000 | 813/1 000 | 603/1 000 | 384/500 | 290/500 |

Et dans des mondes de la classe avec une carte hors classe (T10, T12) : A1 de 113 à 218 sur 1 000, A2 de 86 à 143 sur
1 000, contre au plus 5 %. **Le banc voit les deux façons échouer nettement** (intervalles de Clopper-Pearson tous au-dessus
de 0,05 ; T01 A1 pas 0,05 : [0,916 ; 0,948] ; T05 A2 fin : [0,551 ; 0,613]). Les mêmes poids, gelés par bloc et divisés par le
certificat (M7, M8), tombent à 0 promotion sur les mêmes mondes : la correction est exactement le certificat.

## 6. Puissance sur de vraies découvertes (mêmes tirages, mêmes instants)

Carte = monde ; trois familles d'une composante neuve, trois doses chacune, fixées d'avance (grilles du préenregistrement de
l'idée 1.1, sans réglage) : V1(δ) effet neuf global ; V3(γ) composante conditionnelle à un seuil décentré hors de l'archive ;
V4(λ) loi neuve sur une sous-population. 200 mondes par dose pour V1 et V4, 100 pour V3 (réduction dite, section 2).
Source : `sortie-puissance-v1.json`. Taux de promotion :

| bras | V1 0,25 | V1 0,5 | V1 0,75 | V3 0,4 | V3 0,8 | V3 1,2 | V4 0,1 | V4 0,2 | V4 0,3 |
|---|---|---|---|---|---|---|---|---|---|
| R8 (v8, membre linéaire, maximum) | 0,365 | 0,775 | 0,930 | 0,220 | 0,820 | 0,910 | 0,090 | 0,525 | 0,720 |
| RLa (nul limité aux coupures de l'archive, maximum) | 0,325 | 0,690 | 0,875 | 0,140 | 0,690 | 0,860 | 0,045 | 0,415 | 0,630 |
| RF4 (partition à 4 cellules, maximum) | 0,250 | 0,630 | 0,840 | 0,090 | 0,640 | 0,830 | 0,025 | 0,285 | 0,540 |
| R9 (façon v9, maximum certifié sur toutes les coupures) | 0,160 | 0,580 | 0,800 | 0,030 | 0,540 | 0,800 | 0,010 | 0,155 | 0,375 |
| M1 projection, membre linéaire | 0,415 | 0,820 | 0,960 | 0,300 | 0,880 | 0,950 | 0,150 | 0,630 | 0,810 |
| M2 projection, F4 bruit commun | 0,340 | 0,735 | 0,930 | 0,270 | 0,790 | 0,940 | 0,120 | 0,540 | 0,760 |
| M2b projection, min(lin, A, B) | 0,370 | 0,725 | 0,925 | 0,260 | 0,850 | 0,940 | 0,125 | 0,560 | 0,785 |
| **M3 projection, toutes coupures (classe du v9)** | 0,260 | 0,660 | 0,865 | 0,140 | 0,670 | 0,890 | 0,055 | 0,340 | 0,520 |
| M4 horizon fixe, Bonferroni (F4) | 0,190 | 0,585 | 0,825 | 0,060 | 0,630 | 0,880 | 0,050 | 0,370 | 0,610 |
| M5 pas à pas avec bruit | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| M6 pas à pas sur l'enveloppe + M1 | 0,140 | 0,465 | 0,735 | 0,070 | 0,380 | 0,710 | 0,000 | 0,050 | 0,110 |
| M2c projection, F4 bruit par cellule | 0,145 | 0,630 | 0,820 | 0,120 | 0,660 | 0,880 | 0,085 | 0,385 | 0,675 |
| M7 appris sur le passé, certifié | 0 | 0 | 0,005 | 0 | 0 | 0 | 0 | 0 | 0 |
| M7b appris et lissé, certifié | 0 | 0,005 | 0,055 | 0 | 0 | 0,060 | 0 | 0 | 0 |
| M8 moitié, certifiée | 0 | 0 | 0,005 | 0 | 0 | 0 | 0 | 0 | 0 |
| M9 fraction prévisible (F4) | 0,245 | 0,660 | 0,885 | 0,080 | 0,680 | 0,910 | 0,055 | 0,365 | 0,665 |

**Comparaisons appariées** (différence des taux sur les mêmes mondes, intervalle de Wald à 95 % ; toutes les valeurs dans
`comparaisons_appariees`) :
- **M3 contre R9** (même classe, celle du v9) : +0,100 [+0,056 ; +0,144] ; +0,080 [+0,042 ; +0,118] ; +0,065 [+0,031 ; +0,099] ;
  +0,110 [+0,049 ; +0,171] ; +0,130 [+0,053 ; +0,207] ; +0,090 [+0,034 ; +0,146] ; +0,045 [+0,016 ; +0,074] ;
  +0,185 [+0,129 ; +0,241] ; +0,145 [+0,091 ; +0,199] (ordre des colonnes) — positif sur les 9 lignes.
- **Part de la perte du v9 regagnée** par M3, (M3 − R9) / (R8 − R9), descriptive : de 0,41 à 0,82 selon la ligne, autour de
  la moitié (0,49 ; 0,41 ; 0,50 ; 0,58 ; 0,46 ; 0,82 ; 0,56 ; 0,50 ; 0,42).
- **M3 contre RLa** (le nul limité, qui rouvre les coupures hors archive) : de −0,110 [−0,163 ; −0,057] à +0,030 ; M3 garde
  la classe du v9 pour une puissance proche de celle du nul limité, sans l'égaler sur V4.
- **M3 contre R8** : de −0,200 à −0,020 ; la fermeture de toutes les coupures garde un prix.
- **M2b contre RLa** (même classe) : de +0,035 [+0,003 ; +0,067] à +0,160 [+0,083 ; +0,237], positif sur les 9 lignes.
- **M1 contre R8** (même classe) : de +0,030 [+0,006 ; +0,054] à +0,105 [+0,051 ; +0,159], positif sur les 9 lignes.
- **M6** perd contre R9 sur 8 lignes sur 9 en estimation ponctuelle (jusqu’à −0,265 [−0,329 ; −0,201]) : sa classe, bien plus large, contient une partie des
  découvertes (V4 surtout : la loi neuve mêlée à S1 reste souvent dans l'enveloppe des lois connues).
- **M4** (Bonferroni) ≥ R9 mais < M2 : les blocs valent mieux que la borne de l'union.
- **M9** < M2 : sur une carte juste, la fraction ne sert à rien et coûte la moyenne sur λ.
- **M7, M7b, M8** : puissance nulle ou presque (au plus 0,06) : la correction des fiches est valide et inutile.

**Lecture prudente (R4, « trop beau = réserve »).** Les gains de M1, M2b et M3 sur leurs références de même classe sont
de même signe sur toutes les lignes ; deux raisons de s'en méfier et deux de ne pas les croire gonflés :
(i) **mon R9 perd beaucoup plus que le vrai v9 sur son banc** (ici jusqu'à 0,37 contre R8 sur V4 0,2 ; le verdict du v9
donne 0,105 au plus) : mon archive (quatre lois, dont deux si_sinon) et mes doses diffèrent, et R9 n'a pas les autres
membres du v8 ; l'ampleur ne se transpose pas ; (ii) le banc est petit (100 à 200 mondes par dose). En sens contraire :
(iii) les références sont prises à la valeur **atteinte** de l'EM (et l'élagage de R9 ne fait que baisser son
dénominateur), ce qui les avantage ; (iv) le gain a une cause démontrée : la projection ne paie pas le surajustement du
maximum sur les tirages (lemme 2, proposition 3), et le gain croît avec le nombre de familles (M1 contre R8 : +0,03 à
+0,10 ; M3 contre R9 : +0,045 à +0,185). Une confirmation demanderait un banc préenregistré, le vrai code du v9 et ses
autres membres.

## 7. Lois de l'archive connues seulement à travers des tirages

Dans le juge, les lois de l'archive sont des lois écrites dans la grammaire : connues exactement ; le certificat est exact.
Si une loi L_j n'était connue que par m tirages (estimée L̂_j) :
- **Le certificat « comme si exact » n'est plus valide** : c est calculé aux sommets L̂_j, pas aux vrais L_j ; une copie d'un
  membre du vrai nul n'est plus dans l'enveloppe des L̂_j et la richesse monte comme n·KL(q ‖ projection sur L̂).
- **Correction** : pour une boule de confiance ‖L_j − L̂_j‖₁ ≤ ε_j, sup_L Σ_y L(y)·f(y) ≤ Σ_y L̂_j(y)·f(y) + (ε_j / 2)·(max f − min f)
  (car L − L̂_j est de somme nulle et de norme 1 au plus ε_j), f = q / φ. Certificat robuste = max_j de cette borne (et des δ_k).
  Sur l'événement « toutes les boules contiennent la vraie loi » (probabilité ≥ 1 − δ, tirages de l'archive indépendants des
  tirages frais), le lemme 1 tient pour le vrai nul ; donc P(promotion) ≤ α + δ. Le rayon vient d'une inégalité de
  concentration de la loi empirique en norme 1 de la forme P(‖L̂ − L‖₁ ≥ ε) ≤ (2^K − 2)·exp(−m·ε² / 2) (Weissman et al., 2003,
  **à vérifier sur pièce** : la garantie α + δ en dépend).
- **Essai** (`essai_projection_tirages_v1.py`, cas d'école sans traits : deux lois connues, nul = segment ; 2 000 mondes par
  case ; `sorties/tirages-v1.json`) :

| m tirages par loi | ε₁ | copie : plug-in P1 | copie : robuste P2 | découverte : vraies lois P0 | plug-in P1 | robuste P2 |
|---|---|---|---|---|---|---|
| 50 | 0,53 | **429/2 000** [0,197 ; 0,233] | 0/2 000 | 0,873 | 0,863 | 0,181 |
| 200 | 0,27 | **62/2 000** [0,024 ; 0,040] | 0/2 000 | 0,881 | 0,876 | 0,479 |
| 1 000 | 0,12 | 1/2 000 | 0/2 000 | 0,871 | 0,870 | 0,703 |
| 5 000 | 0,05 | 0/2 000 | 0/2 000 | 0,889 | 0,892 | 0,824 |

  Lecture : le plug-in n'est pas valide aux petits m (21,5 % à m = 50) ; le certificat robuste est valide mais coûte de la
  puissance tant que ε est grand (b·log c croît comme 25·ε/2 par bloc). Avec des traits, il faudrait un modèle des L_j(· | x)
  et une région de confiance sur ce modèle : non fait.

## 8. Coût de calcul par carte

Temps processeur moyen par carte (une évaluation complète des 8 instants, mesuré sur la machine partagée, donc gonflé ;
`temps_processeur_moyen_s` des sorties) :

| méthode | s par carte | méthode | s par carte |
|---|---|---|---|
| M1 | 0,05 | M6 | 0,08 à 0,10 |
| M2 | 0,05 à 0,06 | M2c | 0,07 à 0,08 |
| M2b | 0,08 à 0,09 | M7 | 0,07 à 0,08 |
| M3 | 0,46 à 0,53 | M7b | 0,14 à 0,16 |
| M4 | 0,18 à 0,21 | M8 | 0,01 |
| M5 | 0,03 | M9 | 0,21 à 0,23 |

Les quatre références par maximum de vraisemblance ensemble : 2,2 à 2,4 s par carte (R9 en porte l'essentiel ; temps non
séparé par référence dans les sorties). M3 est donc environ quatre fois moins cher que ma référence façon v9, parce qu'une
coupure n'induit que 26 partitions par bloc et que les projections ne dépendent pas des tirages (elles peuvent être
calculées **avant** les tirages, au gel, et journalisées). Pour mémoire, la note W2 donne 0,25 à 0,29 s par évaluation
appariée v8 et v9 avec le vrai code (cité par le préenregistrement de l'idée 1.1) : mes temps, en Python non optimisé sur une
machine chargée, ne se comparent pas à ceux-là.

## 9. Ce que chaque méthode changerait à la conception scellée du juge (nœuds, non tranchés)

Toute adoption est **une version neuve du nul (v10), donc une modification du juge : décision de Lazar**, avec sa propre
validation scellée (comme celle du v9, `54c5713d…`) et une description publique changée. Ce que cela toucherait :
1. **Forme de la valeur e** (`nul_filles_v2.evaluer_v2`, `nul_v9`) : aujourd'hui log W_t = log q(y_1..t) − max des membres
   (vraisemblance maximale certifiée sur les tirages mêmes) ; demain, pour les membres linéaires en leurs poids
   (`ajuste_lineaire:archive`, `ajuste_morceaux`), un produit de valeurs e de blocs, et la richesse = minimum de cette
   richesse et de la richesse actuelle restreinte aux autres membres. C'est l'écart déjà nommé en [PREUVE] § 8.4 (ii).
2. **Blocs = intervalles entre instants de lecture** : les instants deviennent une partie du calcul et non plus seulement de
   la lecture ; changer `instants_lecture` change la valeur e.
3. **Le numérateur** : le pari à fraction (`trajectoire_numerateur`, `fractions`) lit les issues du bloc courant ; il doit
   être gelé par bloc (M9) ou abandonné ; le pari plein convient.
4. **Le certificat** change d'objet : il ne majore plus un maximum sur les tirages, il borne l'espérance du rapport sous
   chaque sommet ; il se calcule exactement et se journalise par bloc (valeur de c − 1).
5. **M3** garde exactement la classe du v9 ; **M6** l'élargit (toute loi restant dans l'enveloppe des lois connues, instance
   par instance) et perd la copie avec bruit aveugle commun non uniforme (T08 : 41/500) : c'est une **question de sens** de
   « rien au-delà de l'archive » (R-1768, R-1779), pour Lazar ; **M2, M2b, M4, M9** gardent la classe des coupures de
   l'archive (même question que La contre Ld dans l'idée 1.1).
6. **M7, M7b, M8** (fiches corrigées) : valides mais sans puissance sur ce banc ; je ne les propose pas.
7. **Inchangé** : la règle e-BH (valeur e arrêtée au premier instant ≥ m/α : temps d'arrêt de la filtration des blocs), le
   gel, la fraîcheur, l'ordre secret, les membres log-linéaires et ordinaires (réserve log-linéaire du v8 inchangée).
8. **Garde de code à prévoir** : refuser tout φ qui lirait une issue du bloc courant ; refuser un certificat non calculé ;
   essai de mutation « certificat retiré » (qui doit faire promouvoir les copies, comme A1 et A2).

## 10. Ce que j'ai écarté, et pourquoi

- **Numéraire exact par bloc** (projection sur l'enveloppe convexe des lois produits, a priori le moins favorable sur θ) :
  optimal, mais 3^25 suites par bloc ; non calculable ici ; ma valeur e en est une minorante valide.
- **Une seule projection sur tout l'horizon, lue aux 8 instants sans correction** : le lemme 1 ne tient qu'à l'horizon où
  la projection est faite ; aux instants intermédiaires la somme des m_s n'est pas bornée : non valide (remplacé par M4,
  Bonferroni, et par les blocs).
- **Minimum sur les familles pris bloc par bloc** (Π_b min_F e_{F,b}) : valide mais plus petit que min_F Π_b ; écarté.
- **Mélange a priori sur les familles au dénominateur** : ne garde que α / π_F (docstring de `nul_v9.py`, point 5) ; écarté.
- **Point unique θ̄ calculé sur l'alternative pour tout l'horizon et pas de certificat** : c'est M4 sans Bonferroni ; non
  valide aux instants intermédiaires.
- **Bruit aveugle commun dans la version pas à pas (M6) par une grille de bruits** : valide seulement sur la grille, et un
  maximum sur une grille continue demanderait une borne de continuité ; non fait ; le trou T08 reste mesuré.
- **Cas T02, T07, T11** : prévus, non joués faute de temps de calcul (section 2).

## 11. Fichiers et empreintes (sha256 ; chacun scellé par un compagnon .sha256)

Dossier `docs/notes/organisme-idees-juge-v1/correction-poids-v1/projection/` :

| fichier | sha256 |
|---|---|
| `essai_projection_cas_v1.py` | `539f6a6cfce71eaab9010fa9cd16a2607a0bf9faf9499286bcb6fb7f25bda837` |
| `essai_projection_commun_v1.py` | `1f4ada977b6cdb96378f3c913df0119bcf6fc333981217ecbbb3583b38f2ca54` |
| `essai_projection_fusion_v1.py` | `91558384cdb628a05891bee4d8afacac597f4b934bd4e1532c0de9c38654c5f4` |
| `essai_projection_methodes_v1.py` | `29704896ec641feff607d42c2636c456e372a2a9f4deb589efd4b8256c8b4105` |
| `essai_projection_puissance_v1.py` | `039b64a073e1f8aceea39e3729f5b56415100e270879e008106b50757191d6a7` |
| `essai_projection_taille_v1.py` | `7da6a53101bf9585b37432af835072fd8492e27cc2be41d8dd1bb58c5498afe5` |
| `essai_projection_tirages_v1.py` | `98af724bdc0abe9bde55164070314df40f2d6c6ff323b2275be4eb66db893933` |
| `sortie-taille-v1.json` | `7cac7416933534063a007114067af00919cfa475ef3dedf26403337940228e07` |
| `sortie-puissance-v1.json` | `b5bab27c1975b8d0e0d3edff9217a2800151ec42368711b5229f2f6a3fb44623` |
| `sorties/puissance-V1-d0-r0000-0100-v1.json` | `689872875a56a0e8b07e3bd968a1ba8d6fa312f2bb858c10c3f09aef705f8fc3` |
| `sorties/puissance-V1-d0-r0100-0200-v1.json` | `07490e70b0ecabf0f2c6c4e2a6b8bebf8efbdae981d22f5539fe60ebe71c61f2` |
| `sorties/puissance-V1-d1-r0000-0100-v1.json` | `6d8db28b9ec397df5fcfedc38b40f182e2da0f0689a84ce7eeb82336f629ad08` |
| `sorties/puissance-V1-d1-r0100-0200-v1.json` | `802da2bed9681b309b5267b4d2aebb0c4105a032b432c43f3a6cbe792aadba78` |
| `sorties/puissance-V1-d2-r0000-0100-v1.json` | `059a1a81178c574f01c1f68737950086c7432ad2cf3b1ec12fd063b41afd8c0b` |
| `sorties/puissance-V1-d2-r0100-0200-v1.json` | `ef635a32920958709319775240c7e5f7ee67eff86e50b9bb75f7a9601b5168f3` |
| `sorties/puissance-V3-d0-r0000-0100-v1.json` | `ea347be3ea092264dcd021936d623ba75f4a0304f7775edd899c8cf266cd4924` |
| `sorties/puissance-V3-d1-r0000-0100-v1.json` | `8dbdaef0710ae3dcb578d0a1694cf8c5ff5386bcf19e1c62b60b5a5b42b25cc6` |
| `sorties/puissance-V3-d2-r0000-0100-v1.json` | `033a92b2c5593529e4f6510170e44ae97c882e791e4d043e18524d880a146266` |
| `sorties/puissance-V4-d0-r0000-0100-v1.json` | `498a17a115b6509c60f76a224224f71bbc81bded1779a972efbe43681d11c743` |
| `sorties/puissance-V4-d0-r0100-0200-v1.json` | `0d51379edbd037f9a5c6266bb1954020aa1b09d4234dd4c1fceadb4069701d8e` |
| `sorties/puissance-V4-d1-r0000-0100-v1.json` | `4ec95fa7f4cdffb0543f6aa069d0483d7446edc796be110612c99a65edf59d6a` |
| `sorties/puissance-V4-d1-r0100-0200-v1.json` | `266f61e373eed8ceee35766fd3b2d15c409acc58953727f6f46c21ea0f651ed1` |
| `sorties/puissance-V4-d2-r0000-0100-v1.json` | `2d2abe975f7139cb49e1ffe48fd59a9d19ae2f6d10e6e1ddefb1fb9b2d4b17e5` |
| `sorties/puissance-V4-d2-r0100-0200-v1.json` | `3934a888022327893f9561a0e53c0ae4335c80f4d1feed1ba2d0a6b0dd8d1670` |
| `sorties/taille-T01-r0000-0500-v1.json` | `a84df189dac55a1c0287d67214a6ee22e23efde2ce517ad69cf0158dbd9380a8` |
| `sorties/taille-T01-r0500-1000-v1.json` | `9665019f6a60773ff67ac6fff1619e03b0a118d94783984ae916c3adfabe8fad` |
| `sorties/taille-T03-r0000-0250-v1.json` | `5a43880320931443bc0deb4dfff8d79cd14afe699b59f519bb5837ca6d158b7c` |
| `sorties/taille-T03-r0250-0500-v1.json` | `ea43fa5996e7628736fa2032f95ed4fe54979b7f92454b16c9cb45a79f4b0ee7` |
| `sorties/taille-T03-r0500-0750-v1.json` | `e2d52b045e6c949a5c68e98ac1eb6e413b6c924b6541472679801676082373e1` |
| `sorties/taille-T03-r0750-1000-v1.json` | `f0b4cc3d96b96427d736b8c7d67c0e30f5b9b6225deee55551e57d96ef88fa06` |
| `sorties/taille-T04-r0000-0250-v1.json` | `c4637a388f4d1f8b3ee8275d739906df96cbdff25ed50ef15a5af6d25adfce05` |
| `sorties/taille-T04-r0250-0500-v1.json` | `0daec1651e75977406cfc960e57c29fad9511682c861d01783e8bfb524f8b04f` |
| `sorties/taille-T04-r0500-0750-v1.json` | `176ae01619f0dcabc6642e0dfe492d9c6919374aaf09e1e411f4c3323afccb0e` |
| `sorties/taille-T04-r0750-1000-v1.json` | `aec5d4c27224712b05f5ae3542df7e1187e96eb4432dacdf1e67d68a27e4177f` |
| `sorties/taille-T05-r0000-0250-v1.json` | `df2c3cea0d23a69a5360a39f6a69338c8017180231ac501830f221fb9f5059f5` |
| `sorties/taille-T05-r0250-0500-v1.json` | `38d4c808d30a7b17e33ffc31a49920b9a66ff0b8080716b4712a164ae1426ca9` |
| `sorties/taille-T05-r0500-0750-v1.json` | `e14885cb9a8168eabdb0ff3a00e0b4993c9d98fa5058ab40d618b33a57decdbe` |
| `sorties/taille-T05-r0750-1000-v1.json` | `03d7e9d40e781c87db4f09582d4f853d97ed3560b3cd01c83838e564546910e8` |
| `sorties/taille-T06-r0000-0250-v1.json` | `0ab12374ac280f4df32fa34ba4c18084ff9b94ce6c9d71d538683c5f0eaeb8cf` |
| `sorties/taille-T06-r0250-0500-v1.json` | `74dfd74f5a5e67554a9d43b0f1c95aa53e563b6b790f4696b9ff332ec6e85848` |
| `sorties/taille-T08-r0000-0250-v1.json` | `bb707b1f520ec7dce5ab74d21b1c63add212a8379876b3ed914fcd4235a70ce1` |
| `sorties/taille-T08-r0250-0500-v1.json` | `3b36235b129c23ac57459dec40751ec115823aea7579d7ed0f78121feb95821c` |
| `sorties/taille-T09-r0000-0250-v1.json` | `8405ea1fe800cf9057ac091101f893a12f580c5f496209cd77ef35abe94f2e69` |
| `sorties/taille-T09-r0250-0500-v1.json` | `c89d80ebc3c8095dcd2f5a834246d0e8d8f8acb0447f15c3b81fc419f9f298b0` |
| `sorties/taille-T10-r0000-0250-v1.json` | `e40d169ecc191c440f1f020fe052610c1125e64644e12b1a3e9117662ed37d8c` |
| `sorties/taille-T10-r0250-0500-v1.json` | `6deecb5e9700c22d29b7deccafbd4586eeae7d06ac72be6a10de70675eb7a9f6` |
| `sorties/taille-T10-r0500-0750-v1.json` | `d5e6a891a07e33c6cc0f010eb9e4d16e85b00b29c6421d48b853417b4dc18853` |
| `sorties/taille-T10-r0750-1000-v1.json` | `a199a49dc00eedf317c304f21b3c409e729ec52831bd3970ba5b23c13954aa6a` |
| `sorties/taille-T12-r0000-0250-v1.json` | `3b1b9f592ae12926fd4ed0653fe8bd5140b5bb2d9bf5ff21952d40a6a2636ada` |
| `sorties/taille-T12-r0250-0500-v1.json` | `56b9497a5dba3ab4dbaabaadfecef5056a6a170341757bcd52aaa1b5f3caef47` |
| `sorties/taille-T12-r0500-0750-v1.json` | `927e4756ad5c61e2c70f2fc23fd4bf25f9cd99fde278ad9985be4a10192bd066` |
| `sorties/taille-T12-r0750-1000-v1.json` | `a473cee8cdb34953fa4569c0d0aa9607b2b22c7bac7a8a217739e3224aaaa6f5` |
| `sorties/tirages-v1.json` | `590fb30ab3d8fce3350d245ccc07b04fe4216f628d5309f6fda7a5af6025c11e` |

Les tranches de `sorties/` sont la source des deux fichiers fusionnés ; la fusion vérifie leur contiguïté et recopie leur empreinte. Ce texte : son empreinte est dans son compagnon `methodes-projection-v1.md.sha256`.
