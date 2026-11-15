# Préenregistrement — tirages frais du juge répartis par blocs avec arrêt anticipé, contre la part fixe, à tirages totaux égaux, avec placebo — v1

- Auteur : concepteur neuf (modèle A au sens de R-2851), sous-agent de la session mère ; je n'ai écrit ni le relevé, ni les
  fiches, ni le juge.
- Date (UTC) : 2026-11-15, rédaction de 08:30 à 08:40 environ (`date -u` : 08:21 au début du dossier, 08:39 à la relecture) ;
  dépôt lu sur `main` ; aucun commit.
- Commit du code d'analyse : **aucun à ce jour** ; le code s'écrit après la contre-lecture et le scellement de la version qui
  fera foi ; ses empreintes entrent dans un **addendum d'empreintes** scellé avant tout jeu, qui ne change rien d'autre.
- Documents qui font foi (chemin + empreinte) :
  - banc B (espace, lois, archive A2, générateurs de lignes) : `docs/notes/organisme-idees-juge-v1/prereg-nul-par-morceaux-limite-v1.md`
    (`46ef2b92119ee5dff05727b90ca8bdd3ba57b52f9c1c75893750c792a2abc089`), section « Plan d'analyse », sous-section « Banc B » —
    ci-dessous **[BANC]** ; toute version neuve de ce texte qui change le banc oblige une version neuve de celui-ci ;
  - théorème 1 (domination de la richesse par une surmartingale, pour chaque membre du nul) :
    `docs/notes/organisme-idees-juge-v1/preuve-validite-nul-limite-v1.md` (`44f249409193778ccbaaa12b6c5e74d64434dfb87be77382d8bb9438459281b2`),
    § 4 — ci-dessous **[PREUVE]** ;
  - relevé, § 1.2 : `…/relecture-exploratoire-v2/releve-idees-reutilisables-v1.md` (`bd253b6c…`) ; fiches opus-p1-01 (n° 5) et
    argon-p1-05 (n° 4) de `sortie--fiches-validees.json` (`a9f9594e…`) ;
  - juge : copie `94bfd92` (`docs/notes/organisme-courbe-dose-reponse-v1/code-organisme-94bfd92/`, liste `0153e02d…`) :
    `pole/a_blanc_v59.py` (`606aa8b4…`, `juger_carte` : 200 tirages, 8 instants), `pole/nul_filles_v2.py` (`0ed9b4ad…`),
    `pole/nul_v8.py` (`cc452aaf…`), `pole/cycle.py` (`798f0390…`, `appliquer_multiplicite`, `instants_reguliers`),
    `pole/selection_pari.py` (`35992811…`) ;
  - recoupement J1 (`eecd98fa…`, § 6) et synthèse § 8 et § 9 (`5fd7e26f…`) ;
  - voisins publiés, PDF au dépôt : PACE, `docs/sources/pdf/2606.08106v1.pdf` (`779f49607688fd06226d4390ad6e0c4c8356ef75b87243fd734181cef700934f`) ;
    E-valuator, `docs/sources/pdf/2512.03109v2.pdf` (`b7a46e4cf781aec0c5730196b9f6a2ea1e42c3ec63f1e5260dff223dfafe3828`) ;
    Qu, Chen et Wang, `docs/sources/pdf/anteriorite-P-041-v2/c8/2609.27051.pdf` (`2a8ded0119a1db422aa548fdc3be80b2861f0548bc8166256be60572a2fddb03`) ;
  - registre : R-2851 (mot de Lazar) ; gabarit `prereg/gabarit-preregistrement-v1.md` (`8cad4371…`).

**Statut.** Version 1, **scellée par empreinte (R6), non contre-lue** : elle ne vaut pas préenregistrement (R1) avant la
contre-lecture par un sous-agent neuf d'un autre modèle (R2), les corrections portées sous un nom neuf, et le scellement par
`controle_ia.prereg.sceller_prereg`. **Aucun jeu avant.** Processeur seul, sans dépense (R-2851). Aucun résultat du banc
n'existe.

## Hypothèse

**Contexte.** Le juge de la boucle réelle donne à chaque carte une **part fixe** de 200 tirages frais lus à 8 instants
(`a_blanc_v59.juger_carte`). Une carte qui ne porte rien consomme autant qu'une carte porteuse d'une composante faible, qui
reste sous le seuil faute de tirages (à la course v67, deux lois plantées vraies sont restées sous le seuil de la règle e-BH
à 200 tirages : log W maximal 4,248 et 5,875 contre log(22/0,05) ≈ 6,087, verdict `docs/notes/organisme-boucle-reelle-v1/course-v67/verdict-course-v67-v1.md`,
`d79024328157aafc5c801b5b0a4a621a5c009f367d88b96bbbfaeaeef3753459`, § 4.2 — **déclaré** : lu avant d'écrire ce texte). L'idée 1.2
(fiche opus-p1-01, règle en neuf points ; argon-p1-05, point 1) : à tirages totaux égaux par génération, donner les tirages
par blocs, arrêter tôt les cartes dont la valeur e tombe très bas ou franchit le seuil, et passer les tirages libérés aux
cartes encore incertaines.

**H-1.2.** À nombre total de tirages frais égal par génération, sous le nul de production (v8), le juge à allocation par
blocs avec arrêt anticipé **couvre davantage de composantes vraies** que le juge à part fixe, **sans promouvoir davantage de
cartes fausses** au sens de l'oracle ; le gain dépasse celui d'un placebo qui répartit les tirages libérés au hasard, et celui
d'un juge à part fixe qui reçoit 25 % de tirages en plus.

**Hypothèses de travail.** (i) La validité ne dépend pas de la règle d'allocation (section « Garantie »). (ii) L'arrêt bas
libère une part notable du budget, parce que la plupart des cartes d'une génération ne portent rien (v67 : onze variantes
d'un même constat, faits du collisionneur, `d19b5400…`, § 2). (iii) Le gain, s'il existe, se place près du seuil de
détection (borne 5 du recoupement : l'arrêt optionnel « ne le déplace qu'en dépensant plus de tirages » — ici, des tirages
pris aux cartes qui n'en ont pas besoin).

**Renvois.** Recoupement J1 (« processus de valeurs e à arrêt optionnel », survivante) ; synthèse § 9, ordre 1 ; voie bon
marché « éliminations successives » approuvée par Lazar (N-045 v2, `c7b05e39…`, mots de 09:35) ; ce n'est **pas** une
revendication : le principe est publié (section « Garantie », voisins).

## Garantie de validité de l'arrêt optionnel et de l'allocation

**Cadre.** Une génération de m = 24 cartes. Chaque carte i a son engagement gelé : sa loi q_i, son plan de N_max = 800
instances, ses instants de lecture 𝒯 = {25, 50, …, 800}, le nul v8 de l'archive ; et son **propre flux** d'issues fraîches
y^(i)_1, y^(i)_2, …, d'une graine propre (dérivée de son empreinte en production, de la racine au banc). Le juge révèle les
issues **par blocs de 25** ; une **règle d'allocation** choisit, à chaque pas, quelle carte reçoit le bloc suivant ; elle ne lit
que les issues déjà révélées (et, pour le placebo, un hasard indépendant U). Hypothèse nulle (celle du juge, par carte
identique) : la loi du monde P* est dans la classe du nul v8 de l'archive.

**Lemme.** Pour chaque carte i, soit Λ^(i)_n = Π_{s ≤ n} q_i(y^(i)_s | ·) / P*(y^(i)_s | x^(i)_s) et N_i(k) le nombre d'issues
de i révélées après k pas. Si (C1) plans et instants sont gelés avant tout tirage, (C2) les flux des cartes sont indépendants
entre eux et de tout ce qui précède le gel, (C3) le monde ne lit pas l'historique, (C4) la règle d'allocation et d'arrêt est
mesurable par rapport aux issues révélées et à U, alors M_i(k) = Λ^(i)_{N_i(k)} est une surmartingale positive pour la
filtration globale G_k (toutes les issues révélées, toutes cartes, et U), avec M_i(0) = 1.

*Preuve.* Au pas k → k + 1, si i ne reçoit pas le bloc, M_i ne change pas. Si i le reçoit (décision G_k-mesurable), les 25 issues
neuves de i sont indépendantes de G_k (C2, C3) ; en conditionnant issue par issue dans l'ordre du plan, chaque facteur
q_i / P* a une espérance conditionnelle au plus 1 ([PREUVE], § 4, étape 3) ; d'où E[M_i(k+1) | G_k] ≤ M_i(k). ∎

**Théorème 2.** Sous C1 à C4 et les hypothèses du théorème 1 de [PREUVE] pour le nul v8 : (a) pour toute règle d'allocation et
d'arrêt écrite d'avance (part fixe, arrêt bas, arrêt haut, plafond, réallocation selon les valeurs e courantes, réallocation au
hasard), la valeur e finale de chaque carte, e_i = W^(i) lue au dernier instant révélé (ou arrêtée au premier instant où elle
atteint m/α), vérifie E[e_i] ≤ 1 ; (b) la règle de Benjamini et Hochberg sur ces valeurs e, m fixé avant toute issue, garde le
taux de fausses découvertes au plus α, **quelle que soit la dépendance que l'allocation crée entre cartes** ; (c) sous
l'hypothèse nulle, qui porte ici sur le monde et vaut pour toutes les cartes à la fois, ce taux est la probabilité d'au moins
une promotion dans la génération.

*Preuve.* (a) À chaque instant de lecture, W^(i) ≤ Λ^(i) ([PREUVE], théorème 1, étapes 1 et 2 : le maximum de vraisemblance
certifié du nul domine P* sur les issues révélées, **recalculé** à chaque instant sur toutes les issues reçues). Le dernier pas
où i est lu est un temps d'arrêt σ_i de G, borné (budget fini, plafond N_max) : E[e_i] ≤ E[M_i(σ_i)] ≤ M_i(0) = 1 (arrêt optionnel
d'une surmartingale positive ; inégalité de Ville pour la lecture continue). (b) La règle e-BH n'exige que E[e_i] ≤ 1 pour
chaque hypothèse nulle vraie, sous dépendance quelconque (Wang et Ramdas, 2022, citée par `cycle.py`). (c) Immédiat. ∎

**Ce que cela règle dans la critique.** La synthèse (§ 8) et le recoupement (J1) demandaient : surmartingale à chaque pas pour
toute loi du nul composite — **établi** (lemme, pour chaque P* de la classe) ; règle d'allocation scellée — **oui** ; ordre de
continuation « jamais selon les valeurs e » et dénominateur « à mélange de poids fixés d'avance, jamais recalibré sur les
issues » — **non nécessaires** : ce sont des conditions suffisantes, pas nécessaires. Le dénominateur du juge est déjà
recalibré sur ses tirages (`nul_v8.py`, docstring, point 4) et la domination W ≤ Λ tient trajectoire par trajectoire ; une
règle d'arrêt ou de continuation dépendante des données, écrite d'avance, est couverte par l'arrêt optionnel. **Divergence
argumentée avec la critique, à éprouver par le contre-lecteur.** Elle tranche la tension que le relevé signale (§ 1.2) en
faveur de la règle d'opus-p1-01.

**Réserves.** (i) C3 : pour un monde qui lit l'historique, les blocs révélés en ordre d'exécution secret demanderaient un
argument de plus ; les mondes du banc et des courses actuelles ne lisent pas l'historique. (ii) La réserve log-linéaire du v8
([PREUVE], H4) est héritée. (iii) Le rejeu tire d'avance les 800 issues de chaque carte ; il équivaut à une révélation à la
demande parce que la richesse à l'instant t ne dépend que des t premières issues (vérifié sur la copie `94bfd92`, [BANC],
annexe B : trajectoire d'un plan de 800 tronquée à 200 égale à celle d'un plan de 200) et parce que la règle ne lit que les
instants révélés (garde de code, liste d'arrêt). (iv) Les unités sont les cartes, non les groupes de doublons (la boucle
réelle n'en a pas) ; pour des groupes, la moyenne des surmartingales des membres en est une pour la même filtration : même
garantie, non éprouvée ici.

**Références.** Inégalité de Ville (Ville, 1939, « Étude critique de la notion de collectif ») ; inférence universelle
(Wasserman, Ramdas et Balakrishnan, PNAS, 2020, citée par `nul_v8.py`) ; règle e-BH (Wang et Ramdas, 2022, citée par
`cycle.py`) — références de méthode, PDF non versés, aucun chiffre n'en est tiré (R7). **Voisins publiés, lus sur PDF page 1** :
PACE (`779f4960…`, p. 1 : un candidat n'est accepté « only when a testing-by-betting e-process accumulates decisive evidence,
stopping early to save evaluations », avec une probabilité de fausse acceptation contrôlée « even under optional stopping (a
per-decision guarantee, not a run-level one) ») ; E-valuator (`b7a46e4c…`, p. 1 : test séquentiel « valid at every step ») ;
Qu, Chen et Wang (`2a8ded01…`, p. 1 : garantie sur les fausses découvertes « at every stopping time for any proposal policy »).
Aussi, liste de N-067, § 6 : Hegazy, Jordan et Dieuleveut, « Valid Stopping in Adaptive Generator–Verifier Loops », arXiv
2610.06432 (PDF sur une autre branche, empreinte `283d3e827032df04…` reprise de N-067, non lue par moi).

## Prédiction chiffrée et signe attendu

Écrites avant tout jeu, sans pilote. « Couverture » : part des générations de la famille T où au moins une carte porteuse est
retenue par la règle e-BH. Bras : section « Plan d'analyse ».

| # | prédiction | signe | chiffre | ce qui la réfute | confiance |
|---|---|---|---|---|---|
| Q1 | validité : famille N (monde dans la classe du nul) | sous α | part des générations avec au moins une promotion ≤ 0,02 dans **chacun** des cinq bras | une part « non tenue » (seuil) | 0,85 |
| Q2 | copies membres exactes de la classe : jamais promues, dans aucun bras ni aucune famille | nul | 0 | une seule promotion (défaut) | 0,97 |
| Q3 | **principale** : couverture A − couverture F, famille T, toutes cellules | + | ≥ + 0,05, borne basse > 0 ; gain surtout aux doses moyennes (≥ + 0,08 dans les quatre cellules moyennes réunies), ≤ + 0,05 aux doses faibles réunies | borne haute < + 0,02 (« pas de gain ») | 0,55 |
| Q4 | A contre F125 (part fixe de 250, total 1,25 fois plus grand) | ≥ 0 | couverture A ≥ couverture F125 (ponctuel) | borne haute de A − F125 < 0 (gain d'effectif seulement) | 0,5 |
| Q5 | A contre le placebo P | + | A − P ≥ + 0,02 (ponctuel) | borne haute de A − P ≤ 0 (pas d'effet du ciblage) | 0,55 |
| Q6 | fausses promotions au sens de l'oracle (famille T) | 0 ou + faible | moyenne par génération ≤ 0,10 dans chaque bras ; A − F : borne haute ≤ + 0,05 | borne basse de A − F > + 0,02 | 0,6 |
| Q7 | tirages économisés par l'arrêt seul (F-arrêt) | + | au moins 25 % du budget non consommé (famille T), pour une perte de couverture F − F-arrêt ≤ 0,02 | économie < 10 %, ou perte > 0,05 | 0,6 |
| Q8 | mécanisme : tirages moyens reçus par une carte porteuse sous A | + | ≥ 300 (contre 200 sous F) | < 230 | 0,55 |

**Ce que serait chaque issue.** Q3 vraie, Q4 et Q5 vraies : l'allocation apporte un gain de structure (meilleur cas). Q3 vraie,
Q4 fausse : le gain n'est qu'un gain d'effectif (cosmétique au sens de la fiche). Q3 fausse : l'allocation n'aide pas sur ce
banc ; Q7 dit alors seulement ce qu'épargne l'arrêt.

## Métrique

- **Génération** : un monde, son archive A2, m = 24 cartes, B = 24 × 200 = 4 800 tirages frais au total (sauf F125 : 6 000).
- **Promotion** : retenue par la règle e-BH (`cycle.appliquer_multiplicite`, m_fixe = 24, α = 0,05) sur les valeurs e finales
  des 24 cartes ; valeur e d'une carte : sa trajectoire lue jusqu'à son dernier instant révélé, arrêtée au premier instant où
  elle atteint m/α (log 480 ≈ 6,17), sinon sa dernière valeur.
- **Couverture C_X** (famille T) : part des générations où au moins une porteuse est promue ; intervalle de Clopper-Pearson à
  95 %. **Différence appariée** C_X − C_Y (mêmes générations, mêmes cartes, mêmes issues) : intervalle percentile à 95 % par
  rééchantillonnage des générations, 10 000 rééchantillons ; test exact de McNemar (rapport).
- **Fausses promotions FP_X** : nombre moyen, par génération, de cartes non porteuses promues (copies, fausses, nulles) ;
  différence appariée et intervalle de même construction. **Erreurs de décision** par génération : 1[non couverte] + nombre de
  fausses promotions (rapportées ensemble et séparément).
- **Validité** (famille N) : part des générations avec au moins une promotion ; Clopper-Pearson.
- **Tirages** : consommation D_X / B par génération (moyenne, quantiles) ; **économie** E_X = 1 − D_X / B ; tirages reçus par
  type de carte ; part des cartes arrêtées bas, haut, au plafond.
- Rapportés par cellule (type de composante × dose) et réunis.

## Seuil

- Juge : nul v8 de l'archive A2, bibliothèque et marginale d'entraînement comme `juger_carte` ; α = 0,05 ; m = 24 ; blocs de 25 ;
  instants = fins de blocs ; plafond N_max = 800 (4 fois la part fixe, fiche opus-p1-01, point 6).
- Arrêt bas : log W < log(1/20) après au moins 50 tirages (un quart de la part fixe, point 4) ; arrêt haut : log W ≥ log(m/α).
- **Validité** « tenue » si le test binomial exact de H₀ « part ≥ 0,05 » est rejeté au niveau 0,05/5 (Bonferroni sur les cinq
  bras) ; « non tenue » si H₀ « part ≤ 0,05 » est rejeté au même niveau ; sinon « non jugeable ».
- **Principale** : « gain » si la borne basse de C_A − C_F > 0, son estimation ≥ + 0,05 **et** la borne haute de FP_A − FP_F
  ≤ + 0,05 ; « pas de gain » si la borne haute de C_A − C_F < + 0,02 ; « nuisible » si la borne haute de C_A − C_F < 0 ou la
  borne basse de FP_A − FP_F > + 0,02 ; sinon « non tranché ».
- **Qualification d'un gain** : « d'effectif seulement » si la borne haute de C_A − C_F125 < 0 ; « sans effet de ciblage » si la
  borne haute de C_A − C_P ≤ 0 ; « de structure » si aucune des deux.
- **Zone utile** : si C_F (famille T, réunie) ≤ 0,05 ou ≥ 0,95, la principale est « hors de la zone utile » (non concluant).

## Plan d'analyse

**Cartes et mondes** (générateurs de [BANC], archive A2 ; graines ci-dessous). Composante tirée par génération : un type parmi
V1, V2, V3, V4 et une dose parmi les deux plus basses de sa grille ([BANC] : V1 {0,25 ; 0,50}, V2 et V3 {0,4 ; 0,8}, V4
{0,1 ; 0,2}) ; huit cellules.

- **Famille T** (600 générations, 75 par cellule) : monde M = S1 portant la composante (ligne V de [BANC]). 24 cartes :
  - 6 **porteuses** : M ; M à force × 0,5 ; M à force × 1,5 ; M avec la direction de la composante bruitée (bruit gaussien de
    0,3 fois sa norme, renormalisée) ; deux doublons de M (chaque poids des lois softmax de M + 0,01·N(0, 1)) ;
  - 6 **copies de la classe** : trois `melange` des lois d'archive (poids de Dirichlet) ; trois lois d'archive tempérées et
    inclinées (`transformee`, puissance U[0,7 ; 1,3], inclinaison N(0 ; 0,2²) par issue) — membres du nul v8 ;
  - 4 **copies par morceaux** hors de la classe du v8 : `si_sinon` sur chacune des deux coupures de l'archive (S1, S2) ;
    `par_sous_population` (S1, S2) ; `si_sinon` au signe d'un trait (S2, S1) ;
  - 6 **fausses** : S1 portant une composante de même type et de même dose, tirée indépendamment (quatre) ; M à composante de
    signe opposé (deux) ;
  - 2 **nulles** : softmax aléatoires.
- **Famille N** (500 générations) : monde M₀ = `melange` des lois d'archive (ligne Q1 de [BANC]), dans la classe du nul.
  24 cartes : 8 **voisines du monde** hors de la classe (M₀ où S1 est remplacée par softmax(W1 + 0,05·Δ, b1), Δ centrée ;
  dérive à peine négative, le cas le plus dur pour la continuation) ; 8 **membres exacts** (M₀ elle-même, autres mélanges,
  lois d'archive tempérées) ; 8 cartes des autres sortes de la famille T, bâties sur une composante que le monde ne porte pas.
- Chaque carte a son plan de 800 instances et ses 800 issues fraîches (flux propre), et une marginale d'entraînement sur 100
  instances ; ses richesses aux 32 instants 𝒯 sont calculées **une fois** par `nul_filles_v2.evaluer_v2` (nul v8,
  engagement à plan « ordre_naturel », tirages liés à son empreinte, montage de [BANC]) ; tous les bras **rejouent** ces mêmes
  trajectoires.

**Bras** (mêmes cartes, mêmes issues, même e-BH) :
- **F** (part fixe, témoin) : 200 tirages par carte, instants 25 à 200 ; valeur e arrêtée à m/α, sinon W₂₀₀ (règle actuelle).
- **F-arrêt** (arrêt seul) : F plus les arrêts bas et haut ; aucune réallocation ; mesure l'économie.
- **A** (allocation, fiche opus-p1-01 adaptée aux cartes et aux blocs de 25) : par tours ; à chaque tour, chaque carte
  **active** (ni arrêtée bas, ni arrêtée haut, ni au plafond) reçoit un bloc, dans l'ordre des indices décalé du numéro du tour,
  tant que le budget restant B − (tirages donnés) le permet. Les cartes arrêtées libèrent leur reste ; les tours continuent
  au-delà de 200 pour les actives jusqu'à épuisement du budget ou de cartes actives.
- **P** (placebo de la réallocation) : comme A jusqu'à ce que chaque carte ait reçu 200 tirages ou soit arrêtée ; ensuite,
  chaque bloc restant va à une carte **tirée au hasard** (graine indépendante des issues) parmi celles qui ne sont ni arrêtées
  haut ni au plafond, **arrêtées bas comprises** (elles reprennent).
- **F125** (témoin d'effectif) : 250 tirages par carte (10 blocs), total 6 000 ; valeur e comme F.

**Graines (R9).** Racine : entier de l'empreinte sha256 du texte qui fera foi. `numpy.random.SeedSequence(entropy=racine,
spawn_key=(famille, g, i))` pour la carte i de la génération g (famille 0 = N, 1 = T ; i = 24 pour le monde et l'archive) ;
`(famille, g, 1000)` pour le hasard du placebo ; `(99, b)` pour le rééchantillonnage. Manifeste du run (`src/controle_ia/manifeste.py`).

**Étapes.** 0. Code sous des noms neufs, `docs/notes/organisme-idees-juge-v1/code-v1/banc_tirages_repartis_v1.py` et
`lire_banc_tirages_repartis_v1.py` (lecture gelée), avec essais (R5 : cas sain et artefact par garde) et banc de mutations (au
moins : la règle lit un instant non révélé ; budget dépassé ; arrêt bas avant 50 tirages ; plafond ignoré ; hasard du placebo
tiré des issues ; m compté après coup ; flux d'issues partagé entre deux cartes) : toutes tuées pour la raison attendue ;
contre-lecture du code par un autre modèle ; addendum d'empreintes scellé. 1. Contrôles avant jeu. 2. **Essai E1** (50 cartes) :
la trajectoire d'un plan de 800 tronquée à t est égale à celle d'un plan de t, pour t = 200 et 400 ; sinon arrêt. 3. Jeu :
1 100 générations, `nice -n 10`, deux processus au plus. 4. Sortie scellée avant toute lecture, sous
`diag/organisme-idees-juge-v1/`. 5. Lecture gelée, puis lecteur neuf (R13), audit de symétrie (R4) écrit avant le prononcé.

**Comparaisons et corrections.** Une principale (A contre F, couverture, avec la condition sur les fausses promotions) ; deux
qualifications (A contre F125, A contre P) lues seulement si la principale rend « gain » ; validité : Bonferroni sur cinq bras.
Tout le reste (cellules, tirages par type, Q7, Q8) est rapporté sans critère supplémentaire.

## Critères de lecture gelés

| étage | observé | verdict |
|---|---|---|
| 1 | une validité « non tenue » dans un bras, ou une promotion d'un membre exact de la classe | **« garantie mise en défaut »** : défaut de code ou de preuve ; rien d'autre n'est lu ; audit ; nœud |
| 2 | C_F (famille T, réunie) ≤ 0,05 ou ≥ 0,95 | **« hors de la zone utile »** (non concluant) |
| 3 | principale | « gain » / « pas de gain » / « nuisible » / « non tranché » (seuils ci-dessus) |
| 4 | si « gain » : qualifications | « de structure » / « d'effectif seulement » / « sans effet de ciblage » |
| 5 | F-arrêt | économie et perte de couverture rapportées, avec intervalles (Q7) |

**Audit de symétrie (R4)**, écrit pour toute issue avant le prononcé : tirages reçus par type de carte (le mécanisme
attendu — les porteuses reçoivent les tirages libérés — se voit-il ?) ; cartes arrêtées bas puis porteuses (pertes par mauvaise
série initiale, piège nommé par la fiche) ; comparaison cellule par cellule ; « trop propre » (gain identique dans toutes les
cellules, aucune fausse promotion nulle part, toutes les prédictions vraies) : relecture écrite du code de rejeu.

## Liste d'arrêt

| condition | action |
|---|---|
| un fichier gelé diffère de l'addendum ; un essai échoue ; une mutation survit | pas de jeu |
| essai E1 : préfixe non égal | arrêt avant le jeu ; le rejeu n'est pas équivalent à une révélation à la demande |
| la règle d'un bras lit un instant au-delà des tirages qu'elle a donnés (garde d'accès du code) | arrêt ; défaut |
| tirages donnés > B (A, P, F-arrêt) ou > 6 000 (F125) dans une génération | arrêt ; défaut |
| exception, log W non fini | arrêt du run ; aucune lecture partielle ; relance seulement sous un texte ou un addendum neuf (R5) |
| durée murale > 24 h | arrêt ; run invalide |
| lecture avant scellement de la sortie | run invalide |
| toute dépense, instance payante ou appel de modèle | interdit (R-2851) |

## Coût

**Processeur seul, 0 dollar.** 1 100 générations × 24 cartes = 26 400 évaluations sous le nul v8 à 800 tirages et 32 instants,
à 0,12 à 0,20 s chacune (essai à blanc du 15 novembre, [BANC], annexe B) : 0,9 à 1,5 heure d'un cœur ; le rejeu des cinq bras
et le rééchantillonnage sont négligeables. Borne dure 24 heures. Écriture, essais, mutations, contre-lectures : temps d'agents.

## Écarts, nœuds et ce que l'essai ne décide pas

- **Le banc** ne touche ni le juge de production ni la boucle : aucun écart à une conception scellée.
- **Nœud de Lazar** : adopter l'allocation au juge changerait sa conception gelée (200 tirages et 8 instants par carte dans
  `juger_carte` et dans le texte scellé de la boucle réelle, `80fe4f03…` ; un budget de génération et un plafond de 800 en plus) :
  modification du juge, à décider sur le résultat, avec sa propre validation.
- **N-058** : l'allocation sélectionne des **cartes** sur leurs valeurs e, jamais des **agents** : compatible (« l'interdit porte
  sur la sélection d'agents, pas sur celle des fiches »). Garde : les tirages reçus ne seront jamais rapportés par proposeur ni
  servis à un choix de proposeurs.
- **Ne décide pas** : l'effet sur la découverte (une carte non proposée ne gagne rien, borne 1 du recoupement) ; les mondes riches
  à 8 traits ; les groupes de doublons ; le test de mort ; le gain en dollars (un tirage du monde planté coûte des
  millisecondes, fiche opus-p1-01, champ `perte_traduction` : l'intérêt réel est pour les domaines où un tirage est cher).

## Contre-lecture

Aucune à ce jour : ce texte v1 est le brouillon soumis à la contre-lecture (R2), par un sous-agent neuf d'un autre modèle que
l'auteur (modèle B, R-2851). **Fichiers à lui donner explicitement** : ce texte ; [BANC] (`46ef2b92…`) ; [PREUVE] (`44f24940…`) ;
de la copie `94bfd92` : `pole/a_blanc_v59.py`, `pole/nul_filles_v2.py`, `pole/cycle.py`, `pole/nul_v8.py`,
`pole/selection_pari.py` ; le relevé (`bd253b6c…`, § 1.2) ; les fiches n° 4 et 5 ; la synthèse § 8 et § 9 (`5fd7e26f…`) ; le
recoupement J1 et la borne 5 (`eecd98fa…`) ; les pages 1 des trois PDF voisins. À trancher en priorité : la divergence avec la
critique (section « Garantie », « Ce que cela règle ») ; l'équivalence du rejeu ; la composition des générations ; les seuils.

## Citations obligatoires (N-064, N-067)

POPPER (Huang et al., ICML 2025 ; `a3c4b370…`) ; Dwork et al., arXiv 1506.02629 (`dcfbb9aa…`) ; Blum et Hardt, « The Ladder »,
arXiv 1502.04585 (`957ef473…`) ; Co-Scientist (Gottweis et al., Nature 655, p. 487-496, 2026 ; `351f49d8…`) ; liste de
`docs/decisions/decision-N-067-v1.md`, section 6 (dont PACE, Qu, Chen et Wang, Hegazy, Jordan et Dieuleveut). Aucune
revendication n'est faite ici.
