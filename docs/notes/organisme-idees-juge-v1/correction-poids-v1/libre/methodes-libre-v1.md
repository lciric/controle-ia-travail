# Correction des poids du nul — angle « toute autre voie » — v1

**Statut.** Mise au point exploratoire, sur processeur, **aucune revendication**. Concepteur neuf : je n'ai écrit ni le juge,
ni les nuls v8 et v9, ni la preuve du nul limité, ni son préenregistrement, ni la contre-lecture, ni les fiches. Rédaction le
2026-11-15, de 13:35 à 16:05 UTC (`date -u`), dépôt lu sur `main` (tête `e2bef750`), aucun commit, aucune poussée, aucun appel
réseau ni payant. Toute adoption est une **décision du directeur** : je nomme les changements, je ne les tranche pas.

## 0. Verdict en cinq lignes

1. **Aucune méthode de cet angle n'est à la fois valide sur toute la classe du nul v9 et plus puissante que lui.** Ce n'est pas
   un manque d'essais : le lemme A (section 3) montre que, parmi les dénominateurs qui dominent la vraisemblance de chaque
   membre trajectoire par trajectoire, le maximum certifié du v9 est le plus petit. « Apprendre les poids » dans cette forme
   ne peut que perdre (correction valide) ou casser la taille (sans correction).
2. Les seules voies de cet angle qui **regagnent** de la puissance sont celles qui **rétrécissent la classe** (nul limité aux
   coupures de l'archive, nul limité plus partitions déclarées, grille publique de seuils) : gain apparié sur le v9 de +0,04 à
   +0,14 sur les trois doses, **payé** par des copies promues hors de la classe retenue (copie à une coupure hors de l'archive :
   0,90 à 0,95 ; copie par sous-population sous le nul limité seul : 0,99). Valides sur leur propre classe, non valides sur
   celle du v9.
3. Les voies « calibrer le seuil par simulation » (au pire cas sur une grille, avec ou sans la projection de la carte ; ou par
   rééchantillonnage sous le nul ajusté) n'ont **aucune preuve** (la marge de grille est hors d'atteinte : 10²⁵ points au
   moins), **dépassent α** sur des membres du bord (jusqu'à 0,617 sans la projection, 0,07 et 0,10 avec) et sont **moins
   puissantes** que le nul limité certifié qu'elles devaient battre (−0,16 à −0,35 apparié).
4. Les règles « filtre OU partage du niveau » et « pari mixte » sont **non valides** sur la classe du v9 (0,94 sur la copie
   hors archive) ; la règle « ET » est valide mais **égale** au v9, promotion pour promotion (lemme B).
5. **Artefact vu** : sur ce banc, les deux façons des fiches échouent nettement (en ligne : 0,999 à 1,000 des copies exactes
   promues ; moitié : 0,20 à 0,58) ; le banc voit donc le défaut.

## 1. Pièces lues (empreintes recalculées, égales à leurs compagnons `.sha256`)

| pièce | chemin | sha256 |
|---|---|---|
| preuve du nul limité | `docs/notes/organisme-idees-juge-v1/preuve-validite-nul-limite-v1.md` | `44f249409193778ccbaaa12b6c5e74d64434dfb87be77382d8bb9438459281b2` |
| préenregistrement de l'idée 1.1 | `docs/notes/organisme-idees-juge-v1/prereg-nul-par-morceaux-limite-v1.md` | `46ef2b92119ee5dff05727b90ca8bdd3ba57b52f9c1c75893750c792a2abc089` |
| contre-lecture | `docs/notes/organisme-idees-juge-v1/contre-lecture-prereg-nul-limite-et-preuve-v1.md` | `763fc6e29cd80868dcdb1d848eafdc928a39fca7244fa16eb0ac721ec705014e` |
| nul v9 (lu, jamais exécuté) | `docs/notes/organisme-idees-juge-v1/copie-nul-v9-a41b7b5/orchestrator/pole/nul_v9.py` | `7ae450df2482246122bf9fbcf0fa5ef30b4a7e4c6f0d09531e83af048e46ee95` |
| copie du code `94bfd92` (53 fichiers, `sha256sum -c` conforme) | `docs/notes/organisme-courbe-dose-reponse-v1/code-organisme-94bfd92/` : `selection_pari.py`, `nul_v8.py`, `nul_filles_v2.py`, `a_blanc_v59.py` lus (`trajectoire_numerateur`, `juger_carte`), jamais exécutés | liste `empreintes-copie-v1.txt` |
| relevé, § 1.1 | `docs/notes/organisme-conception-propre-v1/relecture-exploratoire-v2/releve-idees-reutilisables-v1.md` | `bd253b6c68f6baada0e61b5381f029b52838ca34aa092502e55253c662451c6c` |
| fiches n° 0 (argon-p1-01), 14 (argon-p2-01), 9 (opus-p1-05), 13 (fable-p1-05), champ `demande_organisme` | `runs/course-ideation-conception-propre-v1/20261113-235541-course-ideation-conception-propre-v1-g1/copies/sortie--fiches-validees.json` | `a9f9594e2dc3a7a553c54577202817758e3f7ef231445f1a48d500fc647389d5` |
| verdict du v9 (seul fichier ouvert dans `docs/verdicts/`, par son chemin) | `docs/verdicts/verdict-validation-nul-v9-v1.md` | `1407e460367754bb9f76b37174f3a21585970864eb9beaa2699494d90125c1ea` |

« Puissance perdue », d'après ce verdict : la validation décisive du v9 tient sa taille sur toutes ses lignes fatales, mais sa
perte de puissance appariée contre le v8 dépasse la marge 0,05 sur une ligne (interaction faible I02 : 105 sur 1 000) ; les
autres pertes sont sous la marge à l'observé. C'est ce prix que l'angle cherche à regagner.

## 2. Les quatre angles des autres concepteurs, écartés de mon travail

1. **Projection d'information inverse** (valeur e par pas contre l'enveloppe convexe du nul).
2. **Inférence universelle** (découpage : l'alternative estimée hors de la part évaluée, ou variantes).
3. **Ensemble de confiance puis maximum** (poids estimés, puis maximum sur une région de confiance).
4. **Poids en ligne corrigés du regret** (dénominateur appris, plus une borne de regret garantie).

Je ne les ai ni réécrits, ni essayés. Le lemme A (section 3) dit seulement où les deux derniers se situent par rapport au v9
(point (b)) ; il ne les juge pas.

## 3. Deux lemmes qui bornent l'angle

Notations du juge (`nul_filles_v2.evaluer_v2`, `nul_v9.py`) : carte q, plan x_1..x_n (n = 200) gelé avant les tirages
frais y_1..y_n, instants T = {25, 50, …, 200}, α = 0,05 ; richesse log W_t = log q(y_1..t) − D_t ; promotion s'il existe
t ∈ T avec log W_t ≥ log(1/α). Classe 𝒞 du v9 : partitions à un niveau P (une cellule ; sous-population ; deux côtés d'un
seuil réel d'un trait), membre 𝒞_P = {p_θ : sur la cellule c, Σ_j μ_{c,j} L_j + ρ, μ ≥ 0, ρ ≥ 0, Σ_j μ_{c,j} + Σ_k ρ_k = 1},
L_j lois connues (membres de l'archive), ρ bruit aveugle commun ; 𝒞 = ∪_P 𝒞_P.

**Lemme A — le maximum est le plus petit dénominateur dominant.** Appelons *dominant* un dénominateur D_t, fonction des
issues, tel que D_t(y_1..t) ≥ log p_θ(y_1..t | x_1..t) pour tout θ ∈ 𝒞 et toute suite d'issues.
*Preuve.* Pour une suite fixée, D_t majore l'ensemble {log p_θ(y_1..t) : θ ∈ 𝒞}, donc sa borne supérieure, qui est le
maximum certifié du v9 à son écart de certificat près. ∎
*Conséquences.* (a) Les poids appris des fiches (en ligne, ou ajustés sur une moitié, ou ajustés sur toute autre donnée)
donnent un dénominateur log p_ŵ(y) **sous** le maximum sur une partie des suites : il ne domine pas, l'argument de Ville de
la preuve du nul limité (théorème 1, pas 1) ne s'applique plus ; c'est la cause des échecs mesurés (section 5). (b) Toute
correction qui rend ces poids dominants donne un dénominateur au-dessus du maximum, donc une richesse plus petite, trajectoire
par trajectoire : jamais plus puissante que le v9. (c) À classe fixée et sous la forme « q / dénominateur dominant », il n'y a
**aucune** façon d'apprendre les poids qui regagne la puissance. Restent trois portes : rétrécir la classe (méthodes 1 à 3),
changer le seuil au lieu du dénominateur (méthodes 4 à 6), ou quitter la domination trajectoire par trajectoire pour une
surmartingale sous chaque θ (angles des autres concepteurs).

**Lemme B — le niveau ne se partage pas entre les morceaux d'une union.** Une règle « promue si et seulement si, pour chaque P,
un test φ_P de niveau α_P sur 𝒞_P rejette » a pour taille sur 𝒞 au plus max_P α_P, car un monde de 𝒞_P n'est promu que si
φ_P rejette. Il faut donc α_P ≤ α pour **chaque** P : aucune somme, aucun budget à redistribuer ; retirer un membre (α_P = 1)
ouvre 𝒞_P en entier. Une règle « OU » (promue si l'un des tests rejette) a une taille au moins égale à celle de chacun de ses
tests : elle n'est valide sur 𝒞 que si chacun l'est. ∎

## 4. Le banc (processeur, numpy seul)

**Code.** Mes programmes recopient la logique utile du juge (aucun fichier des dossiers de copie n'est exécuté ni importé) :
`essai_libre_commun_v1.py` (`5d8f2a6cd6fe53b34c53ea01a0d8f3f5fc33d59656a0b118601f07021207a013`) ;
`essai_libre_banc_v2.py` (`a4699a71d78dd8e82a8ee89faec3828bfeb358a0ae976c84ac03a9a1de076ac1`) ;
`essai_libre_projection_carte_v1.py` (`65a5c81e4a940caf5152f3beba0a555f72582c75bc35e1b1d9e4de6db02c6d9d`) ;
`essai_libre_cout_v1.py` (`43bf38e76d2770e289f0ec985ea112702936251c89c349512e8701bcd02e4661`) ;
`essai_libre_resume_v1.py` (`6643362cc4148cc569da0337c01c3a241394c7436c4fcfc67307cfa6cdeadb16`). La v1 du banc
(`essai_libre_banc_v1.py`, `05a0c97b6a778075856ba014fe7df9724d3a753a18f8993f780081d44b3c65fd`) a été arrêtée par PID avant sa
première sortie (trop lente pour tenir dix minutes par tranche sur des cœurs partagés) ; elle n'a produit aucun chiffre.

**Espace.** Celui du banc B du préenregistrement de l'idée 1.1 : K = 3 issues, deux traits gaussiens arrondis à six
décimales, deux sous-populations ; lois softmax de force 1,5 (biais 0,3). Archive : S1, S2 softmax et S3 = si_sinon({z_jA >
s_A}, U1, U2) ; lois connues (S1, S2, S3) ; coupure de l'archive C_arch = {z_jA > s_A}, s_A uniforme sur [−1 ; 1] au centième,
|s_A| ≥ 0,05.

**Juge recopié, et simplifications dites.** Pari plein (numérateur = vraisemblance de la carte, comme une carte fraîche de
`a_blanc_v59.juger_carte`) ; n = 200, T = {25, …, 200}, α = 0,05. Membres : seulement les mélanges de lois connues avec bruit
aveugle commun (famille de `nul_v9.py`, docstring, l. 19 à 25) ; la partition « une cellule » tient lieu du membre linéaire du
v8 ; **les membres ordinaires et log-linéaires du v8 sont omis** (dénominateur plus petit que celui du juge : la puissance de
tous les bras est surestimée de la même façon ; la validité des bras valides n'en dépend pas, puisque leur classe contient
encore chaque monde de taille). Valeur d'un membre = valeur atteinte + écart de Frank-Wolfe, bornée par 0 (certificat de
`nul_v9._certificats`) ; optimiseur : espérance-maximisation (forme close, `em_certifie`), au lieu des points intérieurs du
v9 ; arrêt d'une partition quand son certificat est à 5·10⁻³ du meilleur atteint (élagage comme le v9) ou au plus 400 pas.
Vérifié avant le jeu sur trois partitions contre un optimiseur indépendant (programmation quadratique séquentielle, huit
départs) : le certificat reste au-dessus de l'optimum (marges 0,003 à 0,004 nat). Reste de certificat maximal observé sur
toutes les évaluations (résumé, champ `reste_certificat_max_par_nul` des tranches) : v9 0,575 nat, La 0,064, Ld 0,054,
grille 0,121 — réserve : quelques évaluations du v9 sont lâches, ce qui sous-estime un peu sa puissance (jamais sa taille).

**Mondes et cartes** (carte = loi du monde ; dans les cas de taille, c'est une copie exacte d'un membre) :

| cas | monde | dans la classe de |
|---|---|---|
| T1 | une cellule, poids Dirichlet(1) sur 3 lois connues + 3 lois certaines (membre intérieur) | toutes |
| T2 | S1 seule (sommet) | toutes |
| T3 | une cellule, poids Dirichlet(0,1) (poids extrêmes, bord du simplexe) | toutes |
| T4 | S1 si z_jA ≤ s_A, S2 sinon (copie par morceaux sur la coupure de l'archive) | v9, La, Ld |
| T4b | même coupure, poids Dirichlet(1) par cellule, bruit aveugle commun de poids U[0 ; 0,3] | v9, La, Ld |
| T5 | S1 sur g = 0, S2 sur g = 1 (copie par sous-population) | v9, Ld, grille |
| T6 | S1 / S2 de part et d'autre d'un seuil ±U[0,3 ; 1,0] hors de la coupure de l'archive (écart ≥ 0,3 sur le même trait) | v9 |
| V1(δ) | softmax(W1 + δΔ, b1), Δ normal centré par trait (composante neuve), δ ∈ {0,3 ; 0,5 ; 0,7} | aucune |

**Mondes simulés.** 1 000 par cas de taille (T1 à T6), 500 par dose de puissance (choix pour tenir le temps : 68 tranches de
125 mondes, chacune sous dix minutes). Le maximum sur toutes les coupes (v9) n'a été calculé que sur T6 et V1 (option
`AVEC_V9`) : sur T1 à T5, la promotion par le v9 est impossible là où La ne promeut pas, par emboîtement (le v9 contient la
classe La : D_v9 ≥ D_La − reste) ; l'emboîtement est vérifié à chaque instant de chaque monde où les deux sont calculés :
**0 violation** sur 2 500 mondes.

**Graines (R9).** `numpy.random.SeedSequence(entropy=2026111501, spawn_key=(cas, r))`, un générateur par monde consommé dans
l'ordre : archive, plan, monde, tirages frais, puis simulations ; flux de calibrage de Mc2 : `spawn_key=(1000 + cas, r)` ; coût :
`spawn_key=(508, r)`. Écrites dans chaque sortie.

**Sorties.** 68 tranches `sorties/sortie-banc-cas*-v2.json` et 26 tranches `sorties/sortie-projection-cas*-v1.json`, chacune
scellée ; le résumé **[R]** = `sortie-resume-libre-v1.json` (`b3e7f382c7884496e3a63a8ad7f86aea6be8c804c6b52099ad8946e9d502a0f6`)
vérifie l'empreinte de chaque tranche avant lecture et les liste toutes avec leur sha256 (champ `fichiers`). Coût **[C]** =
`sorties/sortie-cout-v1.json` (`d735da4505fe268cd44d5d53e6d24ff8234a7acfaddae330572cd493ac4df692`). Tout chiffre ci-dessous
vient de [R], champ `cas.<numéro>.taux` ou `cas.<numéro>.apparie` (numéros : T1 = 0, T2 = 1, T3 = 2, T4 = 3, T4b = 4, T5 = 5,
T6 = 6, V1 à 0,3 / 0,5 / 0,7 = 7 / 8 / 9), sauf mention de [C]. Intervalles : Clopper-Pearson bilatéraux à 95 %.

## 5. Tableau de taille (taux de promotion de la carte ; [R], `cas.0` à `cas.6`, `taux`)

| bras | T1 intérieur | T2 sommet | T3 bord | T4 coupure archive | T4b morceaux archive | T5 sous-pop. | T6 hors archive |
|---|---|---|---|---|---|---|---|
| v9 (référence) | 0 par emboîtement | 0 par emboîtement | 0 par emboîtement | 0 par emboîtement | 0 par emboîtement | non calculé | 0,000 [0 ; 0,0037] |
| La (méthode 1) | 0,000 [0 ; 0,0037] | 0,000 | 0,000 | 0,000 | 0,000 | **0,991** [0,983 ; 0,996] | **0,948** [0,932 ; 0,961] |
| Ld (méthode 2) | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | **0,897** [0,877 ; 0,915] |
| grille (méthode 3) | 0,000 | 0,000 | 0,000 | **0,384** [0,354 ; 0,415] | 0,001 [0 ; 0,006] | 0,000 | **0,394** [0,364 ; 0,425] |
| A1 en ligne (artefact) | **0,999** [0,994 ; 1] | **1,000** | **1,000** | **1,000** | **0,999** | 1,000 | 1,000 |
| A2 moitié (artefact) | **0,570** [0,539 ; 0,601] | **0,202** [0,178 ; 0,228] | **0,428** [0,397 ; 0,459] | **0,227** [0,201 ; 0,254] | **0,581** [0,550 ; 0,612] | 0,990 | 0,950 |
| Mc grille au pire cas (méthode 4) | **0,269** [0,242 ; 0,298] | 0,057 [0,044 ; 0,073] | **0,617** [0,586 ; 0,647] | 0,070 [0,055 ; 0,088] | **0,111** [0,092 ; 0,132] | 0,967 | 0,895 |
| Mc2 grille + projection de la carte (méthode 5) | 0,047 [0,035 ; 0,062] | 0,046 [0,034 ; 0,061] | **0,070** [0,055 ; 0,088] | 0,056 [0,043 ; 0,072] | 0,036 [0,025 ; 0,050] | non calculé | non calculé |
| Md rééchantillonnage (méthode 6) | 0,047 [0,035 ; 0,062] | 0,036 [0,025 ; 0,050] | **0,102** [0,084 ; 0,122] | 0,034 [0,024 ; 0,047] | 0,054 [0,041 ; 0,070] | 0,973 | 0,865 |
| OU partage du niveau (méthode 7) | — | — | — | — | — | — | **0,939** [0,922 ; 0,953] |
| ET (méthode 8) | — | — | — | — | — | — | 0,000 |
| pari mixte (méthode 9) | — | — | — | — | — | — | **0,940** [0,923 ; 0,954] |

Lecture : en gras, un taux au-dessus de α là où le monde est dans la classe que le bras prétend couvrir, ou un trou rouvert
hors de sa classe. Mc, recalculé sur un flux de graines indépendant avec le programme de la projection, redonne 0,276, 0,061,
0,610, 0,068, 0,110 ([R], `taux.Mc_recalcule`) : l'échec n'est pas un hasard de tirage.

## 6. Tableau de puissance (V1, 500 mondes par dose, mêmes tirages, mêmes instants ; [R], `cas.7` à `cas.9`)

| bras | δ = 0,3 | δ = 0,5 | δ = 0,7 | gain apparié sur v9 (0,3 / 0,5 / 0,7) | gain apparié sur La |
|---|---|---|---|---|---|
| v9 | 0,336 [0,295 ; 0,379] | 0,650 [0,606 ; 0,692] | 0,792 [0,754 ; 0,827] | — | −0,140 / −0,118 / −0,084 |
| La | 0,476 [0,432 ; 0,521] | 0,768 [0,729 ; 0,804] | 0,876 [0,844 ; 0,904] | +0,140 / +0,118 / +0,084 (70, 59, 42 gagnées ; 0 perdue) | — |
| Ld | 0,440 | 0,754 | 0,856 | +0,104 / +0,104 / +0,064 (0 perdue) | — |
| grille | 0,400 | 0,722 | 0,836 | +0,064 / +0,072 / +0,044 (0 perdue) | — |
| Mc | 0,280 | 0,566 | 0,716 | −0,056 / −0,084 / −0,076 | −0,196 / −0,202 / −0,160 |
| Mc2 | 0,188 | 0,422 | 0,580 | — | −0,288 / −0,346 / −0,296 |
| Md | 0,208 | 0,434 | 0,590 | −0,128 / −0,216 / −0,202 | −0,268 / −0,334 / −0,286 |
| OU | 0,396 | 0,730 | 0,856 | +0,060 / +0,080 / +0,064 | — |
| ET | 0,336 | 0,650 | 0,792 | 0 (égal au v9, monde pour monde) | — |
| pari mixte | 0,424 | 0,748 | 0,862 | +0,088 / +0,098 / +0,070 | — |
| A1, A2 (non valides) | 1,000 ; 0,534 | 1,000 ; 0,744 | 1,000 ; 0,846 | sans objet (taille cassée) | — |

Le maximum certifié du v9 et le nul limité aux coupures de l'archive sont les deux références demandées ; Ld et la grille sont
les autres formes « classe rétrécie ».

## 7. Méthodes, une par une

Pour chaque méthode : (1) énoncé, (2) validité, (3) taille, (4) artefact (section 8), (5) puissance, (6) coût par carte
([C], médiane sur 20 cartes, un cœur partagé, à prendre comme ordre de grandeur), (7) ce qu'elle changerait à la conception
scellée.

### Référence — maximum certifié sur toute la classe (façon v9)
(1) D_t = max sur toutes les partitions à un niveau (une cellule, sous-population, toutes les coupes des deux traits aux valeurs
observées) de la valeur certifiée. (2) Valide (théorème 1 de la preuve du nul limité appliqué à la classe entière ; lemme A :
c'est le plus petit dénominateur dominant). (3) T6 : 0,000 ; T1 à T5 : 0 par emboîtement. (5) 0,336 / 0,650 / 0,792. (6) 0,16 s
par carte sur ce banc (8 instants). (7) Rien : c'est le v9.

### Méthode 1 — nul limité aux coupures de l'archive (La ; restructuration par parcimonie)
(1) D_t = max(une cellule ; partition par C_arch) — l'idée 1.1 du préenregistrement, que ce banc joue pour la première fois
dans cet angle, sans rien de son plan scellé (aucune lecture de ses critères). (2) **Valide sur la classe La seulement**
(théorème 1, hypothèses H1 à H8 : C_arch fonction de l'archive seule) ; non valide sur la classe du v9 (lemme B : les membres
retirés sont ouverts). (3) 0 sur T1 à T4b ; **0,991** sur T5, **0,948** sur T6. (5) Gain apparié sur le v9 : +0,140, +0,118,
+0,084, aucune carte promue par le v9 et refusée par La (emboîtement). (6) 0,10 s. (7) Version neuve du nul (classe plus
petite) : décision du directeur, liée à la question de sens « une copie coupée ailleurs qu'à l'archive est-elle une
découverte ? » ; validation scellée à part.

### Méthode 2 — nul limité plus partitions déclarées (Ld ; hiérarchie archive puis partitions publiques)
(1) Partitions : une cellule, C_arch, sous-population, signe de chaque trait. (2) Valide sur sa classe (même théorème).
(3) Ferme la copie par sous-population (T5 : 0,000) ; **T6 : 0,897**. (5) +0,104, +0,104, +0,064. (6) 0,10 s. (7) Comme la
méthode 1 ; ferme la forme de l'attaque de la brèche W2.

### Méthode 3 — grille publique de seuils (déciles du plan, fixés avant les tirages)
(1) Partitions : une cellule, sous-population, coupes aux neuf déciles du plan pour chaque trait (lettre voisine de la fiche
opus-p1-05). (2) Valide sur la classe « grille » (les déciles sont des fonctions du plan, gelé avant les tirages). (3) **T4 :
0,384** (ma grille n'inclut pas la coupure de l'archive : une copie de l'archive elle-même passe ; il faudrait y ajouter
C_arch) ; **T6 : 0,394** (une coupe hors grille n'est que partiellement rattrapée par la coupe de grille voisine). (5) +0,064,
+0,072, +0,044. (6) 0,07 s. (7) Version neuve du nul ; trou partiel mesurable, non nul.

### Méthode 4 — seuil critique simulé au pire cas sur une grille de poids (Mc)
(1) Statistique des fiches en ligne (A1 : richesse contre le nul appris par descente exponentielle, pas 0,2, cellules de
l'archive), lue à T ; seuil = maximum, sur 17 points de la classe La (9 sommets « une loi connue par cellule », 3 lois
certaines, le centre, 4 points tirés), du quantile 0,95 de la statistique simulée (100 simulations par point, plan et carte
fixés). (2) **Pas de preuve.** Pour qu'un seuil calé sur une grille couvre tout monde hors grille, il faut borner la
probabilité de promotion entre deux points voisins. Borne par le rapport des vraisemblances : P_θ'(R) ≤ ρⁿ·P_θ(R) avec
ρ = max p_θ'/p_θ ; garder un facteur 2 sur n = 200 tirages exige ρ ≤ 1,0035, soit 3 986 points par dimension sur 7
dimensions : **10^25,2 points**. Borne par la variation totale (≤ n·½‖θ − θ'‖₁) : **10^31,1 points** ([R], `marge_grille_Mc`).
Hors d'atteinte. (3) **T1 : 0,269 ; T3 : 0,617 ; T4b : 0,111** : le pire cas n'est pas aux sommets mais **près de la carte
elle-même**, que la grille ne contient pas. (5) Sous le v9 (−0,056 à −0,084) et sous La (−0,16 à −0,20). (6) 0,13 s (1 700
simulations). (7) Remplacerait la règle de lecture « log W ≥ log(1/α) » par un seuil simulé : écart au juge, sans garantie.
**Écartée.**

### Méthode 5 — même seuil, grille plus projection de la carte (Mc2)
(1) Méthode 4, en ajoutant à la grille le point de la classe La le plus proche de la carte (minimum de Σ_s KL(q(·|x_s) ‖
p_θ(·|x_s)) sur le plan ; calculé **avant** les tirages, d'après la carte, l'archive et le plan ; exact pour une copie :
écart médian 0 nat). (2) Pas de preuve (même marge que la méthode 4). (3) T1 0,047 ; T2 0,046 ; T4 0,056 ; T4b 0,036 ; **T3
(bord) : 0,070 [0,055 ; 0,088]**, au-dessus de α : ni la projection ni la grille ne couvrent les membres du bord, et 100
simulations par point laissent une erreur de quantile. (5) La plus faible de toutes : −0,29 à −0,35 sous La (le seuil calé
à la projection d'une vraie découverte est haut). (6) un peu plus que Mc. (7) Comme la méthode 4. **Écartée** (taille non tenue
au bord, puissance perdue).

### Méthode 6 — rééchantillonnage paramétrique sous le nul ajusté (Md)
(1) Statistique A1 ; seuil = quantile 0,95 de la statistique sous la loi de la classe La ajustée au maximum de vraisemblance
**sur les tirages frais eux-mêmes** (200 simulations). (2) Pas de preuve : le seuil dépend des tirages par l'ajustement ; la
validité ne vaudrait qu'à la limite, et pas au bord (le maximum de vraisemblance d'un monde du bord est biaisé). (3) T1 0,047 ;
T2 0,036 ; T4 0,034 ; T4b 0,054 ; **T3 : 0,102 [0,084 ; 0,122]**. (5) −0,13 à −0,22 sous le v9 ; −0,27 à −0,33 sous La.
(6) 0,11 s (avec l'ajustement La). (7) Écart au juge (le seuil dépend des tirages). **Écartée.**

### Méthode 7 — filtre « OU » avec partage du niveau
(1) Promue si La promeut au niveau α/2 ou si le v9 promeut au niveau α/2. (2) **Non valide** sur la classe du v9 (lemme B :
la branche La n'a pas de niveau sur les membres qu'elle omet). (3) **T6 : 0,939**. (5) +0,06 à +0,08 sur le v9, mais sous La
seul. (6) Somme des deux. (7) Sans objet. **Écartée.**

### Méthode 8 — filtre « ET » (La au niveau α, puis v9 au niveau α)
(1) Promue si les deux promeuvent. (2) Valide (taille ≤ celle du v9). (3) T6 : 0,000. (5) **Égale au v9, monde pour monde**
(gain 0 aux trois doses) : la classe La est dans celle du v9, donc toute promotion du v9 en est une de La. (6) Somme des deux.
(7) Aucun intérêt. Valide, sans gain.

### Méthode 9 — pari mixte entre dénominateurs (½ W_La + ½ W_v9)
(1) Richesse = moyenne des deux richesses ; promue si elle atteint 1/α à un instant de T. (2) Une moyenne de valeurs e est
une valeur e **si chacune l'est** sur la classe visée ; W_La ne l'est pas sur la classe du v9 : **non valide**. Et une moyenne
de deux valeurs e toutes deux valides sur la classe du v9 ne peut dépasser la meilleure qu'au prix d'un facteur 2 : pas de
gain sous le v9 par cette voie. (3) **T6 : 0,940**. (5) +0,07 à +0,10 sur le v9 (empruntés à La). (7) Sans objet. **Écartée.**

### Méthode 10 — élagage des membres certifié par la carte, avant les tirages (non mesurée)
(1) Retirer un membre P du maximum si, pour tout monde θ ∈ 𝒞_P, une borne calculée avant les tirages (de Chernoff, par
puissance λ ∈ (0, 1) du rapport q/p_φ(θ) contre un membre gardé φ(θ), normalisée en martingale puis bornée par Ville) garantit
P_θ(promotion) ≤ α. (2) **Valide si la borne est certifiée pour tout θ de 𝒞_P** : c'est un supremum non concave sur un
continuum de poids et de seuils, pour lequel je n'ai pas de certificat ; et le supremum est atteint près de la carte : pour
une découverte faible (là où le v9 perd sa puissance), la carte est proche de membres de 𝒞_P et la borne vaut ≈ 1, donc rien
ne s'élague là où il le faudrait. (3) à (6) non mesurés (aucun certificat à mesurer). (7) Sans objet. **Écartée** sur
l'argument, non sur une mesure.

### Méthode 11 — poids appris sur d'autres données indépendantes (autres cartes, générations passées)
(1) Ajuster les poids du nul sur des tirages indépendants de ceux de la carte, puis diviser par ce nul simple. (2) **Non
valide** : q / p_ŵ est une valeur e sous p_ŵ, pas sous le monde θ* ≠ ŵ ; pour une copie exacte (q = p_θ*),
E[q / p_ŵ] = Σ p_θ*² / p_ŵ ≥ 1 par instance (preuve du nul limité, § 8.2). C'est la façon « moitié » (A2) avec une autre
moitié : même mécanisme, mêmes taux attendus. Non jouée à part. **Écartée.**

### Méthode 12 — rapport de vraisemblance profilé avec un seuil certifié plus bas que log(1/α)
(1) Garder le dénominateur du v9, baisser le seuil. (2) Un seuil plus bas valide pour **toute** carte et tout monde de 𝒞
demande la loi de la statistique sous chaque θ : c'est la méthode 4 ou 5 appliquée à la statistique du v9, avec la même marge
hors d'atteinte ; un seuil propre à la carte, calé à la projection, échoue au bord (méthode 5). Aucun certificat. **Écartée.**

## 8. Artefact : les deux façons des fiches sur ce banc

**A1 — poids appris en ligne sans correction** (argon-p2-01 : descente exponentielle, départ uniforme, cellules de l'archive,
pas 0,2) : copie exacte promue **0,999** (T1), **1,000** (T2, T3, T4), **0,999** (T4b) ([R], `taux.A1`). **A2 — poids ajustés
sur la première moitié, valeur e sur la seconde** (argon-p1-01 : maximum de vraisemblance par cellule, poids séparés par
cellule, lecture à 125, 150, 175, 200) : **0,570** (T1), **0,202** (T2), **0,428** (T3), **0,227** (T4), **0,581** (T4b) ([R],
`taux.A2`). Les deux échouent nettement, sur des cartes qui sont des membres exacts du nul qu'elles prétendent couvrir, là où
les bras certifiés restent à 0 sur les mêmes tirages : **le banc voit le défaut.** Les chiffres sont du même ordre que ceux de
la preuve (96,5 % à 100 % et 64,9 %) et de la contre-lecture (98 % à 100 % et 37 % à 76 %), sur une autre famille de mondes.

## 9. Voies écartées sans essai, avec leur raison

- **Retirer des membres du nul selon les tirages** (choisir les coupures que suggèrent les issues fraîches) : rompt l'hypothèse
  de gel (H1 de la preuve) ; c'est la façon « moitié » en pire.
- **Partager α en somme entre membres** (style Bonferroni) : inutile, l'union demande le niveau α dans chaque membre (lemme B).
- **Tests par permutation ou conditionnels** : aucune échangeabilité des issues (les instances diffèrent) ; aucune statistique
  suffisante simple (un mélange n'est pas une famille exponentielle).
- **Mélange a priori au dénominateur** : non valide, la garantie tombe à α / π_P (`nul_v9.py`, docstring, point 5).
- **Pari à fraction au numérateur** (déjà dans `selection_pari.trajectoire_numerateur`) : utile aux cartes trop confiantes, ne
  touche pas la perte due au dénominateur ; hors de la question.
- **Seuils arrondis de la grammaire** (centièmes) : plus de seuils possibles que de valeurs observées, aucun gain.
- **Moins d'instants de lecture** : le seuil de Ville ne dépend pas du nombre d'instants ; aucun gain.

## 10. Ce que cela changerait à la conception scellée du juge (à nommer, non à trancher)

- Méthodes 1 à 3 : **une version neuve du nul** (classe plus petite) ; nœud du directeur, dépendant de la question de sens
  ouverte (une copie coupée hors de l'archive, ou par sous-population, est-elle une découverte ?) ; chacune demanderait sa
  propre validation scellée. Sur ce banc, le gain est de l'ordre de 0,04 à 0,14 en promotion ; le prix est de rouvrir les copies
  hors classe à 0,39 à 0,99.
- Méthodes 4 à 6 : un changement de la règle de lecture (seuil simulé) ; non proposées.
- Méthodes 7, 9, 11, 12 : non valides ; méthode 8 : sans gain ; méthode 10 : non certifiable en l'état.

## 11. Réserves

1. Banc simplifié (membres ordinaires et log-linéaires du v8 omis ; optimiseur différent du v9 ; un seul espace de mondes ;
   une seule famille de découvertes) : les taux absolus ne transfèrent pas au juge ; les comparaisons appariées sont plus sûres.
2. Restes de certificat du v9 jusqu'à 0,575 nat sur quelques évaluations (arrêt à 400 pas) : la puissance du v9 est un peu
   sous-estimée, donc les gains des méthodes 1 à 3 un peu surestimés.
3. 500 mondes par dose (et non 1 000), choix de temps ; v9 non calculé sur T1 à T5 (couvert par l'emboîtement, vérifié sans
   violation là où il est calculé).
4. Mc2 et Mc recalculé tirent leur calibrage d'un flux indépendant de celui du banc ; mondes et tirages frais identiques.
5. Coûts ([C]) mesurés sur des cœurs partagés et chargés : ordres de grandeur.
6. Références de méthode, à vérifier sur pièce, aucun chiffre repris : Ville (inégalité pour les surmartingales positives) ;
   Wasserman, Ramdas et Balakrishnan, « Universal inference » (PNAS, 2020) ; Grünwald, de Heide et Koolen, « Safe testing »
   (Journal of the Royal Statistical Society B, 2024) ; Wang et Ramdas (règle de Benjamini et Hochberg sur valeurs e, 2022).
