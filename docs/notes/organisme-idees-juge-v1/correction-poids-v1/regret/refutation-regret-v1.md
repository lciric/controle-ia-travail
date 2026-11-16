# Réfutation — poids du nul appris en ligne, corrigés par une borne de regret — v1

- **Statut** : mise au point exploratoire, **aucune revendication**. Toutes les issues sont rapportées de la même façon.
  Aucun essai ne visait un signe. Rien n'est adopté ici.
- **Auteur de cette pièce** : réfutateur neuf, sous-agent, d'un autre modèle que l'auteur des méthodes. Je n'ai écrit aucune
  des pièces citées.
- **Pièce réfutée** : `methodes-regret-v1.md` (`fac20a285737517f31ececd8062b38b93b25b8349813bd120311e42e93c990c4`), ses
  cinq programmes et ses dix sorties (même dossier). Aucun de ces fichiers n'a été modifié.
- **Date** : 2026-11-15 (UTC). Dépôt lu sur `main` (tête `108c0bd1`). Aucun commit, aucun appel réseau, aucun appel payant,
  rien sous `diag/` ni `donnees/`.
- **Calcul** : processeur seul, Python 3.13.18, numpy 2.4.6, scipy 1.17.1, `.venv/bin/python -I -B`, 3 processus, machine
  partagée. Chaque simulation a tenu en dix minutes (la plus longue des miennes : 253 s ; le plus long rejeu : 387 s).

## 0. Le verdict en huit lignes

1. **Les sept verdicts de l'auteur tiennent.** Je n'ai trouvé ni pas faux dans une preuve, ni contre-exemple, ni chiffre non
   retrouvé. Sa conclusion tient aussi : dans cet angle, aucune méthode ne regagne la puissance perdue du nul v9.
2. **Rejeu** : ses dix sorties sont retrouvées à l'identique, champs de durée exclus (neuf par ses programmes lancés tels
   quels, une par tranches).
3. **Mon attaque** (programme à moi, 12 cas, 2 000 mondes par cas, arrêt aux instants du juge) : les méthodes dites valides
   (R1, R2) et le maximum certifié promeuvent **0 monde sur 2 000 dans chacun des 12 cas**, avec ou sans les membres
   ordinaires du juge. Borne haute de l'intervalle à 95 % : 0,0018, sous le niveau 0,05.
4. **Artefact** : les deux façons des fiches échouent aussi dans mon banc. En ligne sans correction : 33,5 % à 100 % des
   copies promues quand rien ne masque. Moitié : 10 % à 54 % dans dix cas sur douze.
5. **Puissance** : dans mon banc, aux doses 0,1 ; 0,2 ; 0,35, le maximum certifié promeut 0,8 % ; 22,6 % ; 63,8 % des vraies
   découvertes ; R1 en promeut 0 % ; 0 % ; 0,4 % ; R2 aucune. R1 ne promeut aucun monde que le maximum ne promeut pas.
6. **Ce que je corrige dans son rendu** (sans changer un verdict) : (i) le mélange exact n'est pas « hors de portée » avec
   deux lois connues : je le calcule exactement ; (ii) l'erreur de son estimateur du mélange est plus grande qu'il ne le
   dit : de −2,54 à +2,74 nats en dimension 4 et 5, contre −0,20 à +0,38 mesurés par lui en dimension 2 ; (iii) la
   constante calibrée (R5) n'a pas besoin d'être « proche de la borne » : 12,25 nats suffisent sur mes cas, contre 19,7 et
   23,5 ; elle reste pourtant sous le maximum en puissance.
7. **R5, écartée par lui sans essai, est ici essayée** : calibrée sur les copies intérieures seulement, elle promeut 35,6 % à
   98,5 % des copies dans cinq autres cas ; calibrée sur le pire cas simulé, elle promeut 0 % ; 0,5 % ; 21,4 % des découvertes,
   contre 0,8 % ; 22,6 % ; 63,8 % pour le maximum. Le rejet est fondé.
8. **Réserve principale** : banc réduit (comme le sien), deux lois connues dans onze cas sur douze ; les théorèmes ne
   dépendent pas du banc, les chiffres si.

## 1. Ce que j'ai lu et vérifié (empreintes recalculées, égales aux compagnons `.sha256`)

| pièce | empreinte |
|---|---|
| `docs/notes/organisme-idees-juge-v1/preuve-validite-nul-limite-v1.md` | `44f249409193778ccbaaa12b6c5e74d64434dfb87be77382d8bb9438459281b2` |
| `docs/notes/organisme-idees-juge-v1/prereg-nul-par-morceaux-limite-v1.md` | `46ef2b92119ee5dff05727b90ca8bdd3ba57b52f9c1c75893750c792a2abc089` |
| `docs/notes/organisme-idees-juge-v1/contre-lecture-prereg-nul-limite-et-preuve-v1.md` | `763fc6e29cd80868dcdb1d848eafdc928a39fca7244fa16eb0ac721ec705014e` |
| `docs/notes/organisme-conception-propre-v1/relecture-exploratoire-v2/releve-idees-reutilisables-v1.md` (section 1.1) | `bd253b6c68f6baada0e61b5381f029b52838ca34aa092502e55253c662451c6c` |
| `runs/course-ideation-conception-propre-v1/20261113-235541-course-ideation-conception-propre-v1-g1/copies/sortie--fiches-validees.json` (fiches argon-p1-01, argon-p2-01, opus-p1-05, fable-p1-05 : n° 0, 14, 9, 13) | `a9f9594e2dc3a7a553c54577202817758e3f7ef231445f1a48d500fc647389d5` |
| `docs/verdicts/verdict-validation-nul-v9-v1.md` (seul fichier ouvert de ce dossier, par son chemin exact) | `1407e460367754bb9f76b37174f3a21585970864eb9beaa2699494d90125c1ea` |
| `docs/notes/organisme-idees-juge-v1/copie-nul-v9-a41b7b5/orchestrator/pole/nul_v9.py` (lu, jamais exécuté) | `7ae450df2482246122bf9fbcf0fa5ef30b4a7e4c6f0d09531e83af048e46ee95` |
| `docs/notes/organisme-courbe-dose-reponse-v1/code-organisme-94bfd92/orchestrator/pole/selection_pari.py` (lu) | `359928110d757cd54cc0d2773910c7360895b68cac5d17e0e4b4e9933ef306bc` |
| `…/pole/nul_v8.py` (lu) | `cc452aafd17121a7c0ec42829eea47063ffee1f6cdf7f642e264d528f976b888` |
| `…/pole/nul_filles_v2.py` (lu) | `0ed9b4adbcddc4ad77a1c97d5cbd5706f14926e9c47fe96ce2bab3221a138910` |
| `…/pole/a_blanc_v59.py` (lu) | `606aa8b4fcc38786b38cf2954da46533eed9384232a56100d22ff30b8ce0826c` |

Les seize fichiers de l'auteur (note, cinq programmes, dix sorties) ont les empreintes de son rendu et de leurs compagnons.
Ce que « puissance perdue » veut dire, lu dans le verdict : le v9 tient sa taille sur les 18 lignes fatales, mais perd
0,105 de puissance appariée contre le v8 sur la ligne I02 (0,381 contre 0,486), au-delà de la marge 0,05.

Du code du juge, j'ai retenu trois choses que le banc de l'auteur ne reprend pas toutes : la promotion se lit à huit
instants fixés (`nul_filles_v2.evaluer_v2`) ; la marginale d'entraînement est lissée à 0,5 (`controles_pari._frequences`) ;
la bibliothèque ordinaire contient une **marginale ajustée sur les issues mêmes** (`selection_pari.BIBLIOTHEQUE_STANDARD`,
type `marginale_mv`), que son banc omet. Mon banc la garde. Cette omission ne change aucun de ses verdicts (section 9).

## 2. Les preuves, pas à pas (point a)

**Théorème 1 (validité d'une correction par regret).** (1) D_t ≥ sup_Θ ℓ_t ≥ ℓ_t(θ*) : c'est l'hypothèse (H3). (2) Donc
W_t ≤ Λ_t = q(y_1..t)/P*(y_1..t). (3) Sous P*, chaque facteur de Λ a pour espérance conditionnelle la somme des q(y | passé)
sur les issues possibles, au plus 1 : Λ est une surmartingale positive de départ 1. (4) Inégalité de Ville, et les instants
lus sont parmi 1..n. **Aucun pas faux.** Deux remarques : l'hypothèse (H2) ne sert pas, seule (H3) sert ; prendre le
maximum avec d'autres membres ne fait que baisser W.

**Théorème 2 (domination).** Immédiat : on prend le supremum sur les membres. Sa portée est celle que dit l'auteur : il ne
parle que des dénominateurs qui dominent chaque membre sur chaque suite.

**R1, borne ε.** Pas (a) : le maximum existe (polytope compact). Pas (b) : S_ε a pour mesure ε^d. Je l'ai vérifié par
tirages, pour le membre linéaire (d = 4) et le membre par morceaux (d = 5), avec quatre centres (deux sommets, un bord, un
point intérieur) et ε = 0,3 ; 0,5 ; 0,8 : 24 contrôles de 4 millions de tirages, plus grand écart 2,05 écarts types
(`controle_preuve_regret_v1.json`, champ `R1_pas_b_mesure_de_S_epsilon`). Ce contrôle éprouve aussi le paramétrage de la
mesure uniforme (masse des lois certaines de loi Bêta, jacobien σ^{C(J−1)}), que je retrouve par le calcul. Pas (c) : la
loi est affine et positive en θ. Pas (d) et (e) : algèbre ; ε = d/(t + d) donne bien R(t, d). **Aucun pas faux.**

La borne est presque atteinte. Quand la suite n'est explicable que par une loi certaine δ_k (issue constante, lois connues au
plancher), le mélange vaut exactement 1/C(t + d, d). Le regret exact y est log C(t + d, d) : 18,06 nats contre une borne de
19,69 (d = 4), et 21,78 contre 23,51 (d = 5), à 200 tirages. L'écart minimal sur les huit instants est de 1,56 et 1,65 nat
(`attaque-sorties/attaque_regret_v1--bornes.json`, champ `table_borne_epsilon_contre_pire_regret_exact`). Sur 404 suites
défavorables ou extrêmes à mélange exact (3 232 contrôles), aucun dépassement ; la part de la borne atteinte monte à 0,918.
À 200 tirages, on ne gagnerait donc pas plus de 1,6 nat (d = 4) ou 1,7 nat (d = 5) en resserrant la constante de ce
mélange.

**R2, borne de Hedge.** Pas (a) convexité : juste. Pas (b) : chaque composante du gradient est dans [−G, 0], parce que la
prédiction lissée vaut au moins (γ/m)·x_j. Pas (c) : inégalité de Hedge pour des pertes d'étendue G, puis minimum d'une forme
linéaire sur le simplexe atteint en un sommet. Pas (d) : le lissage coûte log(1/(1 − γ)) par tirage. Somme sur les morceaux :
la borne énoncée. **Aucun pas faux.** Contrôles : 600 suites aléatoires et extrêmes, quatre lissages et quatre pas, aucune
composante hors de [−G, 0], aucun dépassement de l'inégalité, part de la borne atteinte 0,80 au plus
(`controle_preuve_regret_v1.json`, champ `R2_pas_b_et_c`). Je retrouve ses réglages et ses bornes par une autre
minimisation : 196,49 nats (un morceau, η = 0,0377, γ = 0,426) et 227,96 nats (deux morceaux) ; il écrit 196,5 et 228,0.
Son programme écrête l'exposant à 50 ; avec le lissage, l'exposant vaut au plus η·G, soit 0,25 (un morceau) et 0,36 (deux
morceaux) : l'écrêtage ne joue jamais.

**R3.** Identité : avec B_t = V_t − Σ log p̂_s, le dénominateur est V_t, le maximum certifié lui-même. Rien à prouver. La
remarque sur la correction minimax est une identité aussi.

**R4.** Avec M partitions et un a priori uniforme : log Σ_P (1/M)·e^{a_P} + log M = log Σ_P e^{a_P} ≥ max_P a_P. Juste. Une
précision : son énoncé met un seul R(t, d) hors de la somme ; il faut alors la plus grande dimension des partitions (R croît
avec d). Avec une seule partition, R4 est R1.

## 3. Rejeu des programmes de l'auteur (point b)

Ses programmes refusent d'écraser leurs sorties. Je les ai donc copiés à l'octet dans un dossier de travail hors du dépôt
(empreintes des copies égales aux empreintes scellées), puis lancés tels quels. Résultat (`rejeu_regret_v1.json`) :

| sortie de l'auteur | voie | résultat |
|---|---|---|
| `essai_regret_bornes_v1.json` | programme lancé tel quel | identique hors durées |
| `essai_regret_taille_v1--interieur_lineaire.json`, `--sommet_L1`, `--bord_L2_delta`, `--morceaux_archive`, `--poids_extremes_morceaux` (1 000 mondes chacun) | programme lancé tel quel | identiques hors durées |
| `essai_regret_taille_v1--morceaux_hors_archive.json` (500 mondes, structure v9 réduite) | programme lancé tel quel | identique hors durées |
| `essai_regret_puissance_v1--d0.1.json`, `--d0.2.json` (500 mondes) | programme lancé tel quel | identiques hors durées |
| `essai_regret_puissance_v1--d0.35.json` (500 mondes) | par tranches | lignes, comptes appariés, médianes, écart de certificat : identiques |

La dose 0,35 lancée telle quelle n'a pas tenu en dix minutes sur la machine partagée : je l'ai arrêtée à 379 s, par son
identifiant de processus, sans sortie. Je l'ai rejouée en deux tranches de 250 mondes (178 s et 152 s) : mon outil
`rejeu_regret_v1.py` appelle **sa** fonction de jugement (`essai_regret_juge_v1.juger`), avec ses graines, puis refait
l'agrégat de son programme. Les 500 mondes rendent ses chiffres au compte près.

Tous les chiffres de son rendu sont donc retrouvés : les taux de taille (0 pour les méthodes corrigées ; 72,9 % à 99,9 % en
ligne sans correction ; 9,9 % à 30,0 % pour la moitié), les bornes (19,69 ; 23,51 ; 196,5 ; 228,0), la puissance (maximum
certifié v9 réduit 0,4 % ; 10,0 % ; 55,6 % ; nul limité 1,4 % ; 18,2 % ; 68,8 % ; R1 au plus 0,2 %), les comptes appariés
(2, 50 et 278 mondes que R1 manque ; aucun monde promu par R1 seul), l'erreur de l'estimateur en dimension 2 (−0,20 à +0,38).
Sa remarque sur le programme de taille modifié pendant le cas « bord » est sans effet : le cas « bord » rejoué avec le
programme final rend sa sortie.

## 4. Mon attaque (point c)

### 4.1 Le banc (`attaque_regret_v1.py`, écrit sans recopier le sien)

Niveau du juge recopié en réduit : 3 issues, 2 traits gaussiens, 200 tirages, lecture aux instants 25, 50, …, 200, niveau
0,05, promotion si log W ≥ log 20 **à l'un des instants** (arrêt optionnel), plancher 10⁻¹². Archive : une loi softmax et
une loi si/sinon dont la coupure (trait et seuil tirés) est la coupure de l'archive. Membres ordinaires gardés : uniforme,
marginale ajustée sur les issues mêmes, marginale d'entraînement, chaque loi connue seule.

Trois choses diffèrent de son banc, par choix :
- **le mélange uniforme est calculé exactement** avec deux lois connues (11 cas sur 12, et la puissance). À proportions
  entre lois connues fixées, l'intégrale sur le bruit aveugle est une somme finie de termes positifs (polynômes symétriques
  élémentaires, moments de Dirichlet). L'intégrale restante porte sur un polynôme de degré au plus t : une quadrature de
  Gauss-Legendre à 101 nœuds (membre linéaire) ou sur une grille d'environ 2 500 nœuds (membre par morceaux) est exacte.
  Trois recoupements scellés : la forme close au sommet (suite « issue constante, lois au plancher » : 18,0648 nats
  calculés, log C(204, 4) = 18,065) ; le même calcul en précision étendue (écart 1,1·10⁻¹³ nat, trois mondes par cas) ;
  et l'estimateur de l'auteur, sans biais sur le mélange, dont l'écart médian à mon calcul va de −0,024 à −0,002 nat
  (section 9, point 2) ;
- **deux régimes de lecture** : « membre seul » (le dénominateur ne contient que le membre ajusté qui contient le monde :
  rien ne masque, c'est le plus sévère) et « avec ordinaires » (comme le juge) ;
- **le maximum** est cherché sur les sommets du polytope ; je garde la valeur atteinte (borne basse du maximum) et le
  certificat (borne haute). Écart médian 10⁻⁴ nat ; plus grand écart 1,68 nat sur un monde à poids très creux (il coûte de
  la puissance au maximum, jamais de la validité).

Graines : `numpy.random.SeedSequence(2026111577, spawn_key=(partie, cas, monde))`, écrites dans chaque sortie.

### 4.2 Taille : 12 cas, 2 000 mondes chacun

Les douze cas : (1) copie intérieure du membre linéaire, poids tirés uniformément ; (2) poids très creux (Dirichlet 0,15) ;
(3) bord : une loi connue et une loi certaine ; (4) sommet : loi certaine δ_k ; (5) sommet : une loi connue seule ; (6) six
lois connues (dimension 8) ; (7) peu de tirages : 40, lus tous les 5 ; (8) copie par morceaux sur la coupure de l'archive
(une loi de chaque côté) ; (9) par morceaux, point tiré uniformément dans le polytope ; (10) par morceaux, poids 0,96 et
0,02, bruit commun 0,02 ; (11) copie par morceaux coupée **hors** de l'archive, jugée par le membre de sa coupure ;
(12) monde intérieur et carte qui n'est **pas** une copie (loi du monde à la puissance 1,3, surconfiante).

Nombre de mondes promus sur 2 000, [intervalle de Clopper-Pearson à 95 %]. Source : `attaque_regret_v1.json`, champ
`resume_taille…`, et les douze fichiers `attaque-sorties/attaque_regret_v1--taille--<cas>.json`.

**Régime « membre seul ».**

| cas | maximum certifié | R1 | R2 | en ligne, mélange | en ligne, gradient 0,05 | en ligne, gradient 0,2 | moitié |
|---|---|---|---|---|---|---|---|
| 1 intérieur | 0 | 0 | 0 | 1 834 [0,904 ; 0,929] | 1 903 [0,941 ; 0,961] | 2 000 [0,998 ; 1,000] | 565 [0,263 ; 0,303] |
| 2 poids creux | 0 | 0 | 0 | 1 981 [0,985 ; 0,994] | 1 989 [0,990 ; 0,997] | 2 000 [0,998 ; 1,000] | 429 [0,197 ; 0,233] |
| 3 bord | 0 | 0 | 0 | 1 995 [0,994 ; 0,999] | 1 999 [0,997 ; 1,000] | 1 998 [0,996 ; 1,000] | 209 [0,091 ; 0,119] |
| 4 sommet δ_k | 0 | 0 | 0 | 2 000 [0,998 ; 1,000] | 2 000 [0,998 ; 1,000] | 2 000 [0,998 ; 1,000] | 0 |
| 5 sommet loi seule | 0 | 0 | 0 | 1 998 [0,996 ; 1,000] | 2 000 [0,998 ; 1,000] | 2 000 [0,998 ; 1,000] | 108 [0,044 ; 0,065] |
| 6 six lois | 0 | 0 | 0 | 1 660 [0,813 ; 0,846] | 1 715 [0,841 ; 0,873] | 2 000 [0,998 ; 1,000] | 883 [0,420 ; 0,464] |
| 7 quarante tirages | 0 | 0 | 0 | 670 [0,314 ; 0,356] | 867 [0,412 ; 0,456] | 1 646 [0,806 ; 0,839] | 629 [0,294 ; 0,335] |
| 8 morceaux, archive | 0 | 0 | 0 | 1 997 [0,996 ; 1,000] | 2 000 [0,998 ; 1,000] | 2 000 [0,998 ; 1,000] | 339 [0,153 ; 0,187] |
| 9 morceaux, intérieur | 0 | 0 | 0 | 1 798 [0,885 ; 0,912] | 1 906 [0,943 ; 0,962] | 2 000 [0,998 ; 1,000] | 1 082 [0,519 ; 0,563] |
| 10 morceaux, poids extrêmes | 0 | 0 | 0 | 1 996 [0,995 ; 0,999] | 2 000 [0,998 ; 1,000] | 2 000 [0,998 ; 1,000] | 592 [0,276 ; 0,317] |
| 11 morceaux, hors archive | 0 | 0 | 0 | 1 999 [0,997 ; 1,000] | 2 000 [0,998 ; 1,000] | 2 000 [0,998 ; 1,000] | 377 [0,172 ; 0,206] |
| 12 carte surconfiante | 0 | 0 | 0 | 1 474 [0,717 ; 0,756] | 1 631 [0,798 ; 0,832] | 1 998 [0,996 ; 1,000] | 472 [0,218 ; 0,255] |

**Régime « avec ordinaires ».**

| cas | maximum certifié | R1 | R2 | en ligne, mélange | en ligne, gradient 0,05 | en ligne, gradient 0,2 | moitié |
|---|---|---|---|---|---|---|---|
| 1 intérieur | 0 | 0 | 0 | 1 265 [0,611 ; 0,654] | 1 305 [0,631 ; 0,673] | 1 368 [0,663 ; 0,704] | 271 [0,121 ; 0,151] |
| 2 poids creux | 0 | 0 | 0 | 1 051 [0,503 ; 0,548] | 1 059 [0,507 ; 0,552] | 1 063 [0,509 ; 0,554] | 166 [0,071 ; 0,096] |
| 3 bord | 0 | 0 | 0 | 1 963 [0,975 ; 0,987] | 1 967 [0,977 ; 0,989] | 1 964 [0,975 ; 0,987] | 189 [0,082 ; 0,108] |
| 4 sommet δ_k | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 5 sommet loi seule | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 6 six lois | 0 | 0 | 0 | 1 378 [0,668 ; 0,709] | 1 432 [0,696 ; 0,736] | 1 632 [0,798 ; 0,833] | 481 [0,222 ; 0,260] |
| 7 quarante tirages | 0 | 0 | 0 | 187 [0,081 ; 0,107] | 233 [0,103 ; 0,131] | 349 [0,158 ; 0,192] | 28 [0,009 ; 0,020] |
| 8 morceaux, archive | 0 | 0 | 0 | 1 978 [0,983 ; 0,993] | 1 981 [0,985 ; 0,994] | 1 981 [0,985 ; 0,994] | 326 [0,147 ; 0,180] |
| 9 morceaux, intérieur | 0 | 0 | 0 | 1 516 [0,739 ; 0,777] | 1 604 [0,784 ; 0,819] | 1 676 [0,821 ; 0,854] | 668 [0,313 ; 0,355] |
| 10 morceaux, poids extrêmes | 0 | 0 | 0 | 1 986 [0,988 ; 0,996] | 1 990 [0,991 ; 0,998] | 1 990 [0,991 ; 0,998] | 576 [0,268 ; 0,308] |
| 11 morceaux, hors archive | 0 | 0 | 0 | 1 996 [0,995 ; 0,999] | 1 997 [0,996 ; 1,000] | 1 997 [0,996 ; 1,000] | 374 [0,170 ; 0,205] |
| 12 carte surconfiante | 0 | 0 | 0 | 949 [0,452 ; 0,497] | 1 057 [0,506 ; 0,551] | 1 246 [0,601 ; 0,644] | 211 [0,092 ; 0,120] |

Pour chaque 0 sur 2 000, l'intervalle est [0 ; 0,0018] : la borne haute est sous le niveau 0,05 dans les 72 cellules des
trois premières colonnes.

### 4.3 Marges : à quelle distance la borne est du maximum

Regret effectif = maximum atteint − log mélange. Marge de R1 = log mélange + R(t, d) − maximum atteint, minimum sur les huit
instants : le théorème la veut positive. Source : les mêmes sorties, champs `regret_effectif_nats…`, `marge_R1…`,
`marge_R2…`.

| cas | dimension | borne au dernier instant | regret au dernier instant : médiane ; 95 % ; maximum | marge de R1 : minimum ; médiane | marge de R2 : minimum | plus grand log W de R1 |
|---|---|---|---|---|---|---|
| 1 intérieur | 4 | 19,688 | 6,173 ; 8,171 ; 11,610 | 2,375 ; 8,363 | 38,279 | −5,439 |
| 2 poids creux | 4 | 19,688 | 9,303 ; 14,621 ; 17,754 | 1,876 ; 6,558 | 34,886 | −1,933 |
| 3 bord | 4 | 19,688 | 9,579 ; 11,675 ; 12,892 | 4,506 ; 7,101 | 44,829 | −4,889 |
| 4 sommet δ_k | 4 | 19,688 | 17,252 ; 17,580 ; 17,846 | 1,783 ; 2,337 | 34,260 | −1,783 |
| 5 sommet loi seule | 4 | 19,688 | 10,884 ; 13,391 ; 15,090 | 3,546 ; 6,340 | 44,984 | −3,546 |
| 6 six lois | 8 | 33,909 | 7,278 ; 9,818 ; 14,395 | 8,762 ; 14,634 | 65,303 | −12,082 |
| 7 quarante tirages | 4 | 13,404 | 3,867 ; 5,876 ; 10,603 | 1,677 ; 4,233 | 10,529 | −2,835 |
| 8 morceaux, archive | 5 | 23,506 | 12,224 ; 14,915 ; 17,690 | 4,430 ; 8,138 | 52,566 | −4,430 |
| 9 morceaux, intérieur | 5 | 23,506 | 6,703 ; 8,839 ; 12,001 | 3,014 ; 10,045 | 47,122 | −5,674 |
| 10 morceaux, poids extrêmes | 5 | 23,506 | 10,814 ; 13,379 ; 15,813 | 4,229 ; 8,566 | 53,238 | −4,932 |
| 11 morceaux, hors archive | 5 | 23,506 | 12,218 ; 15,053 ; 16,774 | 4,701 ; 8,153 | 54,377 | −4,701 |
| 12 carte surconfiante | 4 | 19,688 | 6,181 ; 8,083 ; 11,692 | 2,860 ; 8,363 | 40,954 | −5,011 |

**Aucune marge négative**, ni pour R1 ni pour R2, sur les 24 000 mondes de taille (huit instants chacun) ; ni pour R1 sur
les 3 000 mondes de puissance (marge d'au moins 5,13 nats). La marge de R1 est la plus petite au sommet δ_k, aux poids très
creux et avec peu de tirages : 1,68 à 1,88 nat. En médiane, elle vaut 2,3 nats au sommet δ_k, 4,2 avec quarante tirages, et
6,3 à 14,6 nats ailleurs : c'est ce que R1 perd sur le maximum. Le cas 12 montre que la taille tient aussi pour une carte qui
n'est pas une copie : le plus grand log W du maximum certifié y est 2,27, sous le seuil 3,00.

Le cas 6 (six lois) est le seul où mon mélange est estimé : 1 200 nœuds d'importance sur les proportions, le reste intégré
exactement. Erreur contre une référence à 12 000 nœuds, sur 15 mondes : −0,38 à +0,34 nat. La marge y est d'au moins
8,76 nats : le compte 0 sur 2 000 n'en dépend pas.

**Des zéros partout : trop propre ?** Non. Pour une copie d'un membre, le maximum donne W ≤ 1 à chaque instant, et R1 est
encore en dessous de la marge : zéro promotion est ce que les théorèmes annoncent. Ce qui montre que le banc a des dents,
ce sont les colonnes de l'artefact (même mondes, mêmes tirages), et le cas 12, où le maximum certifié monte à 2,27 sans
passer le seuil.

### 4.4 La copie coupée hors de l'archive, vue par un nul limité à la coupure de l'archive

Hors de la classe, par construction ; 500 mondes, régime « avec ordinaires » ; descriptif. Maximum certifié sur la structure
« linéaire + coupure de l'archive » : 496 sur 500 promues [0,980 ; 0,998]. R1 sur la même structure : 374 [0,708 ; 0,785].
R2 : 0. Moitié : 485. L'auteur trouve 98,0 %, 78,6 %, 0 et 97,8 % : même tableau. Ce n'est pas un défaut de validité ; c'est
le trou que rouvre le nul limité (preuve, section 7).

## 5. L'artefact (point d)

Dans son banc (rejeu) : en ligne sans correction, 72,9 % à 99,9 % des copies promues dans quatre cas ; moitié, 9,9 % à
30,0 %, bornes basses de 0,081 à 0,272, toutes au-dessus de 0,05 ; rien au sommet « L1 seule ».

Dans le mien :
- **en ligne sans correction** (argon-p2-01 ; trois variantes). Membre seul : borne basse au-dessus de 0,05 dans les 12 cas
  pour chaque variante ; le plus petit taux est 33,5 % (quarante tirages, mélange). Avec ordinaires : au-dessus de 0,05 dans
  10 cas sur 12 ; 0 sur 2 000 aux deux sommets ;
- **moitié** (argon-p1-01). Membre seul : borne basse au-dessus de 0,05 dans 10 cas sur 12 (10,5 % à 54,1 %) ; 5,4 %
  [0,044 ; 0,065] au sommet « loi seule » (non tranché) ; 0 au sommet δ_k. Avec ordinaires : au-dessus de 0,05 dans 9 cas
  sur 12 (8,3 % à 33,4 %) ; **1,4 % [0,009 ; 0,020] avec quarante tirages** (pas d'excès dans ce cas) ; 0 aux deux
  sommets. La lecture au seul dernier instant donne les mêmes conclusions (colonne `A2-moitie-lecture-finale` des sorties) :
  l'échec ne vient pas des lectures répétées.

Deux précisions sur son rendu. (i) Il écrit qu'« un seul cas ne voit rien » : la copie d'un sommet. C'est un masquage, pas
une validité : sans membre ordinaire pour couvrir le sommet, l'artefact en ligne promeut 1 998 à 2 000 copies sur 2 000
(cas 4 et 5, membre seul). (ii) Mon gradient exponentié n'écrête pas l'exposant (le sien l'écrête à 50). Au pas 0,2, il
s'effondre : la prédiction tombe au plancher et la médiane de log W est 1 530 sur les copies intérieures (membre seul).
Cela aggrave l'échec, sans le créer : au pas 0,05 et pour le mélange bayésien, l'échec est le même.

L'échec des deux façons est donc réel, dans deux bancs indépendants. Il n'est pas un défaut de son banc.

## 6. La puissance, et la loyauté de la comparaison (point e)

**Loyauté, lue dans son code.** Dans `essai_regret_juge_v1.juger`, toutes les méthodes reçoivent le même numérateur (`lq`),
les mêmes issues, les mêmes instants, le même seuil (`bc.SEUIL`) ; seul le dénominateur change. La moitié lit quatre
instants au lieu de huit : c'est la méthode, pas un biais. Deux choses jouent **contre** le maximum, pas pour lui : son
certificat est lâche (écart jusqu'à 1,22 nat à la dose 0,35), et le mélange de R1 est estimé avec un biais vers le bas, ce
qui grossit W. La ligne `R1-BORNE-v9r` retire l'écart du certificat et promeut les mêmes mondes que le maximum (2, 50, 278) :
la comparaison est loyale.

**Dans mon banc** (1 000 mondes par dose, et non 2 000, pour tenir le temps ; monde = (1 − dose)·(½ L1 + ½ L2) + dose·loi
neuve ; structure : ordinaires, membre linéaire, membre par morceaux sur la coupure de l'archive ; mélange exact ; mêmes
tirages, mêmes instants, même seuil pour toutes). Source : `attaque-sorties/attaque_regret_v1--puissance--d<dose>.json`.

| méthode | dose 0,1 | dose 0,2 | dose 0,35 |
|---|---|---|---|
| maximum certifié | 8 [0,003 ; 0,016] | 226 [0,200 ; 0,253] | 638 [0,607 ; 0,668] |
| R1 (mélange exact + borne) | 0 [0 ; 0,004] | 0 | 4 [0,001 ; 0,010] |
| R2 | 0 | 0 | 0 |
| (artefact) en ligne, gradient 0,2 / moitié | 992 / 257 | 986 / 433 | 986 / 649 |

Mondes promus par R1 et non par le maximum certifié : 0 aux trois doses. Mondes promus par le maximum et non par R1 : 8,
226, 634. Surcoût de R1 sur le maximum certifié à 200 tirages : médiane 16,8 à 17,3 nats, minimum 12,8. Les chiffres de
l'auteur (0,4 % ; 10,0 % ; 55,6 % pour le v9 réduit, 1,4 % ; 18,2 % ; 68,8 % pour le nul limité, 0,2 % au plus pour R1) sont
du même ordre que les miens pour la structure limitée ; l'ordre des méthodes est le même.

## 7. Les méthodes dites non valides : l'échec est-il réel ?

**R0-a et R0-b** : oui, section 5.

**R5 (constante calibrée par simulation), écartée par l'auteur sans essai.** Je l'ai essayée, en une passe, à partir des
mêmes mondes. Deux formes : dénominateur = log mélange + c (constante), ou log mélange + κ·R(t, d). Calibration : plus
petite valeur d'une grille (pas 0,25 nat, ou 0,01) pour laquelle le taux simulé de promotion est au plus 0,05. Source :
`attaque_regret_v1.json`, champ `lecture_constante_calibree_R5`.

| cas | c qu'il faut, membre seul | c qu'il faut, avec ordinaires |
|---|---|---|
| 1 intérieur | 4,00 | 3,50 |
| 9 morceaux, intérieur | 4,25 | 4,00 |
| 2 poids creux | 11,00 | 7,25 |
| 3 bord | 8,50 | 8,50 |
| 10 morceaux, poids extrêmes | 9,25 | 9,25 |
| 5 sommet loi seule | 10,50 | 0 (masqué) |
| 8 morceaux, archive | 12,00 | 12,00 |
| 11 morceaux, hors archive | 12,25 | 12,25 |
| 4 sommet δ_k | 14,75 | 0 (masqué) |

- **Calibrée sur les copies intérieures seulement** (c = 3,5 avec ordinaires), elle promeut 35,6 % des copies à poids
  creux, 89,05 % des copies du bord, et 97,65 % ; 92,95 % ; 98,5 % des copies par morceaux des cas 8, 10 et 11. Une
  simulation de la taille sur un seul type de monde ne garantit rien.
- **Calibrée sur le pire cas simulé** (c = 12,25 avec ordinaires ; taux au plus 3,85 % dans les douze cas), sa puissance est
  0,0 % ; 0,5 % ; 21,4 % aux trois doses, contre 0,8 % ; 22,6 % ; 63,8 % pour le maximum certifié. Avec κ = 0,52 : 0,0 % ;
  0,5 % ; 22,5 %. Elle fait mieux que R1 et moins bien que le maximum.
- **Pourquoi, en une phrase.** Pour une copie, la promotion a lieu quand le regret du mélange contre le vrai membre dépasse
  c + log 20. Ce regret est grand aux sommets et sur les faces (9 à 17 nats en médiane ici) et petit à l'intérieur (6 à
  7). La constante doit couvrir les sommets ; à l'intérieur elle est alors plus grande que le regret, donc le dénominateur est
  au-dessus du maximum. Au sommet δ_k, le regret ne dépend d'aucun aléa (toutes les issues valent k) : la copie est promue
  avec probabilité 1 dès que c est sous le regret moins log 20.

Son rejet est donc fondé, et il l'est même sans l'argument de garantie : calibrée sur le pire de mes douze cas, R5 ne rend
pas la puissance perdue. Une de ses phrases est à corriger : la constante utile ne reste pas « proche de la borne »
(12,25 nats contre 19,7 et 23,5) ; c'est à l'intérieur du polytope qu'elle est trop grande, pas partout.

## 8. Verdict par méthode

« Tient » : ce que l'auteur dit de la méthode (valide ou non, dominée ou non, ses chiffres) résiste aux épreuves (a) à (e).
« Ne tient pas » : un pas faux, un contre-exemple ou un chiffre non retrouvé. « Indéterminé » : ni l'un ni l'autre.

| méthode (verdict de l'auteur) | mon verdict | raison, chiffre |
|---|---|---|
| R0-a, en ligne sans correction (non valide) | **tient** | rejeu identique (72,9 % à 99,9 %) ; mon banc : 33,5 % à 100 % des copies promues, membre seul, 12 cas sur 12 ; l'échec est réel |
| R0-b, moitié (non valide) | **tient** | rejeu identique (9,9 % à 30,0 %) ; mon banc : 8,3 % à 33,4 % avec ordinaires dans 9 cas sur 12 ; pas d'excès avec quarante tirages (1,4 %) ni aux sommets |
| R1, mélange uniforme + borne ε (valide, dominée) | **tient** | preuve sans pas faux ; 0 sur 2 000 dans 12 cas et 2 régimes (borne haute 0,0018) ; marge minimale 1,68 nat, jamais négative ; puissance 0 % ; 0 % ; 0,4 % contre 0,8 % ; 22,6 % ; 63,8 % ; aucun monde promu par elle seule. Réserve : c'est établi pour le mélange **exact** ; pour sa version estimée, voir section 9, point 2 |
| R2, gradient lissé + borne de Hedge (valide, inutilisable) | **tient** | preuve sans pas faux ; 0 sur 2 000 partout ; marge d'au moins 10,5 nats (quarante tirages) et 34,3 nats (200 tirages) ; bornes 196,49 et 227,96 nats retrouvées ; puissance 0 |
| R3, borne dépendante des données (valide, égale au maximum) | **tient** | identité ; rejeu : `R1-BORNE-v9r` et `MAX-v9r` promeuvent les mêmes mondes (2, 50, 278). Le plafond `R1-BORNE-v9r` emploie la valeur atteinte : ce n'est pas un dénominateur valide, c'est une borne de puissance, et il le dit |
| R4, mélange sur les découpages + log(1/π_min) (valide, dominée par R1) | **tient** | inégalité vérifiée à la main ; sa richesse est au plus celle de R1 sur chaque suite, donc l'attaque de R1 la couvre (avec un seul membre, R4 est R1) ; aucun essai séparé, ni chez lui ni chez moi |
| R5, constante calibrée (non valide en garantie, écartée) | **tient** | essayée ici : calibrée sur l'intérieur, 35,6 % à 98,5 % de copies promues dans cinq autres cas ; calibrée sur le pire cas simulé (12,25 nats), puissance 0,0 % ; 0,5 % ; 21,4 % contre 0,8 % ; 22,6 % ; 63,8 % |

La conclusion d'ensemble de l'auteur tient : une correction certifiée met le dénominateur au-dessus du maximum sur chaque
suite, donc ne rend jamais de puissance ; la constante non certifiée n'en rend pas non plus sur mon banc. Ce qui reste est
hors de cet angle, comme il le dit : réduire la classe du nul, ou une valeur e qui ne domine pas suite par suite.

## 9. Ce que je corrige ou précise dans le rendu de l'auteur (aucun verdict ne change)

1. **« Mélange exact hors de portée (t^d monômes) »** : vrai pour la somme sur les monômes, faux pour le mélange lui-même
   quand il y a deux lois connues. Je le calcule exactement par une autre voie (section 4.1). Coût mesuré, toutes méthodes
   comprises : 0,02 à 0,07 s par carte pour le membre linéaire, 0,20 à 0,38 s pour le membre par morceaux (champ
   `duree_par_monde_s_moyenne` des sorties de taille). Avec plus de lois connues, la quadrature exacte croît vite (une
   dimension de plus par loi et par morceau) : à six lois, je l'estime moi aussi.
2. **Erreur de son estimateur du mélange** : il la mesure en dimension 2 seulement (−0,20 à +0,38 nat). Je l'ai mesurée dans
   les dimensions de son banc, avec ses fonctions appelées comme dans son programme, contre mon mélange exact, sur mes
   mondes : 8 cas, 200 mondes, 8 instants (`attaque-sorties/attaque_regret_v1--estimateur.json`). Dimension 4 : de −2,54 à
   +1,10 nat. Dimension 5 : de −1,40 à +2,74 nats. Médiane proche de 0 (−0,06 à 0,00 à 200 tirages). Aucun des 12 800
   calculs ne met « mélange estimé + borne » sous le maximum atteint, parce que les grandes erreurs ne sont pas tombées sur
   les petites marges. Mais la plus grande sous-estimation (2,54 nats) dépasse la plus petite marge (1,78 nat au sommet
   δ_k, où son erreur reste entre −0,20 et +0,17) : la validité de la version **estimée** n'est pas établie. Sa réserve 2
   est donc plus lourde qu'écrit. Sans effet sur la décision : R1 est dominée de toute façon.
3. **R5, « c utile resterait proche de la borne »** : mesuré, 12,25 nats contre 19,7 et 23,5 (section 7).
4. **Son banc omet la marginale ajustée** du juge (section 1). Pour le maximum, sans effet : le membre linéaire la contient.
   Pour l'artefact, elle masque un cas de plus (la copie de δ_k).
5. **R0-a, « regret positif et croissant »** : il l'est en espérance, pas sur chaque suite. Sans effet.
6. **R1, « la borne est 2 à 3 fois le regret subi »** : chiffre de la dimension 2. En dimension 4, le rapport va de 3,2
   (intérieur, médiane) à 1,1 (sommet δ_k) : c'est aux sommets que la borne est serrée.
7. **R4** : avec des partitions de dimensions différentes, le terme R(t, d) hors de la somme doit prendre la plus grande.

## 10. Réserves de cette réfutation

1. **Banc réduit**, comme celui de l'auteur : deux lois connues (six dans un cas), membres tempérés et inclinés omis,
   moyennes glissantes omises, pas de partition par sous-population, pari plein. Les membres par morceaux n'ont qu'une
   coupure fixée d'avance ; le vrai v9 parcourt tout seuil réel. Pour la taille, c'est sans effet (ajouter des membres ne
   fait que baisser W) ; pour la puissance, mes chiffres valent pour la structure limitée, pas pour le v9.
2. **Puissance sur 1 000 mondes par dose** dans mon banc, **estimateur sur 200 mondes par cas**, **structure hors classe sur
   500 mondes** : réduits pour tenir dix minutes par simulation. La taille, elle, est sur 2 000 mondes par cas.
3. **Rejeu de la dose 0,35 par tranches** : sa fonction de jugement est la sienne, l'agrégat est refait par moi sur le
   modèle de son programme. Les neuf autres sorties sont rejouées par ses programmes mêmes.
4. **R4 n'a pas d'essai séparé** ; son verdict repose sur une inégalité de deux lignes et sur l'attaque de R1.
5. **R5** : ma calibration ne voit que mes douze cas ; « pire cas simulé » n'est pas « pire cas ». C'est l'objection même
   de l'auteur, et elle vaut pour mon essai.
6. Mon exposé de la quadrature exacte et mes contrôles ne sont **pas contre-lus**.
7. Arrêts faits pendant le travail, tous par identifiant de processus : un pilote de lancement en attente (aucune partie
   lancée), et le rejeu direct de la dose 0,35 (section 3). Aucun fichier n'a été écrasé.

## 11. Fichiers (dossier `docs/notes/organisme-idees-juge-v1/correction-poids-v1/regret/`, chacun scellé par un compagnon `.sha256`)

| fichier | rôle | empreinte |
|---|---|---|
| `attaque_regret_v1.py` | programme d'attaque (banc, mélange exact, lecture) | `739c2a5dfa5c5b2c269a99f5a0b76cb8ec5c3dcb0debb8458d95f65241d547f8` |
| `attaque_regret_v1.json` | sortie rassemblée : résumé de taille, lecture de R5, les 17 sorties partielles et leurs empreintes | `571ba83be185733234a96b07f6b6d198c5e3d9c18ef751123aff637b3e4e8339` |
| `rejeu_regret_v1.py` | outil de rejeu et de comparaison | `adaafc8e6b4085ddecd6284c63ce84d64e216be2e2274d1480e7f55b08b1b82f` |
| `rejeu_regret_v1.json` | comparaison des rejeux aux sorties scellées de l'auteur | `7ad7cb26214fa291a643f1603451cfe840081c57767afaf7d2b2dbf8bc5d31b9` |
| `controle_preuve_regret_v1.py` | contrôles des pas des preuves de R1 et R2 | `3b4a0975192a127c26b71a181d02d2c31ac6fc2d6e0b55a6079057cf4e1e3bd6` |
| `controle_preuve_regret_v1.json` | sortie des contrôles | `93a7a43c631fcdb3a20a14f6ac0f48c40253473ca0e468dcd835bc9baea702d1` |
| `attaque-sorties/attaque_regret_v1--bornes.json` | sortie partielle de l'attaque | `c9e065b0a3bc93045dbc40bdb2b5ada70107a8e58347d21158c4c839a0f672d6` |
| `attaque-sorties/attaque_regret_v1--estimateur.json` | sortie partielle de l'attaque | `b02f370e127c595a90a0a96a1ff90ce36884fb4a9c048c255e1b3235f13251ba` |
| `attaque-sorties/attaque_regret_v1--puissance--d0.1.json` | sortie partielle de l'attaque | `2967428434cf4a58e301427f1df36114d597b0d7bd8a68f76b6e95e13e062eec` |
| `attaque-sorties/attaque_regret_v1--puissance--d0.2.json` | sortie partielle de l'attaque | `b77c5869898427b63ff21b8b12ecf0b4fa1c297c127f2ddad87a55e37629fe10` |
| `attaque-sorties/attaque_regret_v1--puissance--d0.35.json` | sortie partielle de l'attaque | `bcbaa76b15f142116dffca5b542a6cb3a90b7d8f8c90722e976878997ea0469d` |
| `attaque-sorties/attaque_regret_v1--taille--lin_bord.json` | sortie partielle de l'attaque | `16a18e3b2d4258dac8d36d48ea30f152b125961453197f36516f21dd3211dc78` |
| `attaque-sorties/attaque_regret_v1--taille--lin_carte_surconfiante.json` | sortie partielle de l'attaque | `6f33a14a82b95bf675fabf3d21fc9c6a02bc4eb58f3c0d6b2726bc70e04519a5` |
| `attaque-sorties/attaque_regret_v1--taille--lin_interieur.json` | sortie partielle de l'attaque | `4f1f089d5708ec8f22e6cc26fd5ab8f54062358428f617b6c246ccb5f13edffc` |
| `attaque-sorties/attaque_regret_v1--taille--lin_peu_tirages.json` | sortie partielle de l'attaque | `daac8e3a63c06870a8a726e338b7c0dc29bac3c2f057ca81dd20c36f1bb4e965` |
| `attaque-sorties/attaque_regret_v1--taille--lin_poids_extremes.json` | sortie partielle de l'attaque | `dc7bd47f2b117c8b9c15feb87fe028f78b3206135c08531969037a27f45bd9bf` |
| `attaque-sorties/attaque_regret_v1--taille--lin_six_lois.json` | sortie partielle de l'attaque | `a09c0f3ddf145c102e22b68909b930176401aede90b87ae13c0fad0aebc2e103` |
| `attaque-sorties/attaque_regret_v1--taille--lin_sommet_delta.json` | sortie partielle de l'attaque | `cb37172ca9eab7efa773f3fd6899b8d2c51ff55ea783cb79a2cf04ffe79b214b` |
| `attaque-sorties/attaque_regret_v1--taille--lin_sommet_loi.json` | sortie partielle de l'attaque | `078b71d3b3e3bdd4d1bb57ee6654248589488523605168df88d9cbc3e9474ab0` |
| `attaque-sorties/attaque_regret_v1--taille--mor_hors_archive.json` | sortie partielle de l'attaque | `b2ce90c2e57945df91051d51409b44e5cf303c821e14c077599b78b14d1f3f7d` |
| `attaque-sorties/attaque_regret_v1--taille--mor_interieur.json` | sortie partielle de l'attaque | `07bc09f3289812eeae75fb2fc1109ea820c06bb98587206520c484cc76f4a860` |
| `attaque-sorties/attaque_regret_v1--taille--mor_poids_extremes.json` | sortie partielle de l'attaque | `5e2e1cfc1497f3fdab8d399589e81c99840dbd72912f416599a541f576f12c88` |
| `attaque-sorties/attaque_regret_v1--taille--mor_sommet.json` | sortie partielle de l'attaque | `c2faa44bab1cedddc177ada6f916b127e13a2098a2bcfbb683b56e7897a51e6d` |
| `rejeu-sorties/rejeu_regret_v1--d0.35--0-250.json` | mondes rejoués de la dose 0,35 (fonction de jugement de l'auteur) | `cbdadbf099af29ea176728e624ccd13678f07c41672cd2f6851a1003ceb31097` |
| `rejeu-sorties/rejeu_regret_v1--d0.35--250-500.json` | mondes rejoués de la dose 0,35 (fonction de jugement de l'auteur) | `1501fe58dac157ea7afe7ed9a7c3f5af5f3057981662c95060e7c31bed75ff0e` |

Les programmes n'ont pas changé depuis leurs essais. Les empreintes des 17 sorties partielles sont aussi dans
`attaque_regret_v1.json` (champ `parties`).

## Références (à vérifier sur pièce ; aucun chiffre n'en est repris)

Inégalité de Ville ; inégalité de Hedge (Freund et Schapire) ; portefeuille universel (Cover) ; quadrature de
Gauss-Legendre ; intervalle de Clopper-Pearson. Les preuves relues sont celles que l'auteur écrit dans sa note ; mes calculs
n'emploient aucun résultat chiffré de ces textes.
