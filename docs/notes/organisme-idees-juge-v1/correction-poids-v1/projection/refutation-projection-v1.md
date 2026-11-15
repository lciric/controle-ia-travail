# Réfutation — angle « projection d'information inverse (numéraire) » — v1

**Statut.** Mise au point exploratoire, **aucune revendication**. Toutes les issues sont rapportées à l'identique : ce
qui tient est dit avec son chiffre, ce qui ne tient pas aussi. Aucun essai ne vise un signe. Rien n'est adopté : toute
suite est une décision de Lazar.

- **Auteur de cette note** : réfutateur neuf, sous-agent de la session mère, d'un autre modèle que l'auteur de la
  méthode ; je n'ai écrit aucune des pièces citées.
- **Pièce attaquée** : `methodes-projection-v1.md` (`681eb7f5c75b9599ddb7508b575f1824fb126fa781409104e08115d106e51f2e`),
  ses sept programmes et ses sorties, même dossier. Aucun fichier de l'auteur n'est modifié.
- **Date** : 2026-11-15, de 15:58 à 18:20 UTC environ. Dépôt lu sur `main`, aucun commit, aucun appel réseau ni payant,
  rien sous `diag/` ni `donnees/`.
- **Calculs** : Python 3.13.18, numpy 2.4.6, processeur seul, machine partagée et très chargée (charge de 5 à 24 sur
  4 cœurs) ; chaque simulation bornée à dix minutes ; réductions dites en section 11.
- **Mes fichiers** : `attaque_projection_v1.py` (programme), `sortie-attaque-projection-v1.json` (toutes mes sorties,
  120 pièces fusionnées), cette note. Empreintes en section 12.
- Toute référence de la littérature est **à vérifier sur pièce** ; aucun chiffre n'en est repris.

## 0. En bref

1. **La preuve tient.** Lemme 1, lemme 2, proposition 3, théorème 4 : aucun pas faux. Vérifié aussi par le calcul : le
   plus grand logarithme d'espérance d'une valeur e de bloc, cherché sur tout le polytope, n'a jamais dépassé 0 sur
   2 304 essais ; une énumération complète à peu de tirages donne une probabilité exacte de promotion de 0,479 pour
   α = 0,5, de 0,192 pour 0,25 et de 0,069 pour 0,1.
2. **Le rejeu est identique.** 900 mondes de taille, 270 de puissance et tout l'essai « tirages » rejoués avec ses
   programmes : mêmes promotions, monde par monde ; ses deux fichiers fusionnés régénérés à l'octet près.
3. **Mon attaque ne casse aucune méthode dans sa classe.** Douze méthodes réécrites, 16 cas, dont le pire cas (monde
   égal à la projection de la carte) que l'auteur n'avait pas : au plus 1,7 % de promotions (35/2 120, borne haute
   2,3 %) ; en amplifiant (200 000 mondes par cas), au plus 1,8 % en moyenne et 3,25 % pour le pire engagement ; mon M3
   complet : 0,36 % à 0,63 % ; le M3 de l'auteur sur mes mondes : 3/500. L'espérance exacte de chaque bloc est restée au
   plus 1 sur 161 810 couples (méthode, monde).
4. **Une hypothèse est fausse pour le juge, et le lemme en dépend.** P4 dit que la loi de la carte ne lit pas les
   issues du bloc jugé, « vrai au pari plein ». Or la grammaire du juge a deux lois qui lisent l'historique, et la
   preuve du juge actuel les couvre. Avec une telle carte, la méthode par blocs n'est plus valide : espérance exacte
   1,33 sur un exemple à deux tirages ; à l'échelle du juge, **10,3 %** de fausses promotions pour M1 avec la loi
   « sans remise » de la grammaire dans un monde uniforme (206/2 000 ; dans le juge complet, le membre ordinaire
   « uniforme » couvrirait ce monde-là), et **45 %** avec une carte écrite pour l'attaque (904/2 000) dans un monde que
   seul le membre linéaire couvre ; M3 tombe aussi (19/60 avec le code de l'auteur). Geler l'historique au début du
   bloc rétablit la validité (0/13 000). **Toute adoption demande une garde que l'auteur n'a pas écrite** (section 5).
5. **L'artefact est confirmé.** Les deux façons des fiches promeuvent la copie exacte dans 41 % à 100 % de mes mondes
   selon le cas (58 % à 100 % à 200 tirages ; 56,6 % à 100 % dans les siens), et leur espérance exacte dépasse 1 sur
   chacun de mes 4 020 mondes de contrôle.
6. **La puissance annoncée est rejouée, et la comparaison est loyale** : mêmes tirages, mêmes instants, même seuil ; sa
   référence « façon v9 » est au maximum de vraisemblance à 0,004 nat près (18 mondes recalculés). L'ampleur des gains
   ne se transpose pas au vrai juge (il le dit), et elle dépend du soin de l'optimiseur.
7. **Verdicts** (section 10) : les treize méthodes dites valides **tiennent** (M1 à M9, et P2 dans son cas d'école),
   sous la garde du point 4 pour les dix qui travaillent par blocs ; A1, A2 et P1 **ne tiennent pas**, comme l'auteur
   le dit, et leur échec est réel.

## 1. Pièces lues, empreintes vérifiées

Toutes les empreintes ci-dessous sont recalculées (sha256) et égales à leur compagnon, ou, pour les quatre fichiers du
dossier de copie `code-organisme-94bfd92` qui n'ont pas de compagnon propre, à la ligne de `empreintes-copie-v1.txt`
(lui-même égal à son compagnon).

| pièce | sha256 |
|---|---|
| `docs/notes/organisme-idees-juge-v1/preuve-validite-nul-limite-v1.md` | `44f249409193778ccbaaa12b6c5e74d64434dfb87be77382d8bb9438459281b2` |
| `docs/notes/organisme-idees-juge-v1/prereg-nul-par-morceaux-limite-v1.md` | `46ef2b92119ee5dff05727b90ca8bdd3ba57b52f9c1c75893750c792a2abc089` |
| `docs/notes/organisme-idees-juge-v1/contre-lecture-prereg-nul-limite-et-preuve-v1.md` | `763fc6e29cd80868dcdb1d848eafdc928a39fca7244fa16eb0ac721ec705014e` |
| `…/copie-nul-v9-a41b7b5/orchestrator/pole/nul_v9.py` (lu, jamais exécuté) | `7ae450df2482246122bf9fbcf0fa5ef30b4a7e4c6f0d09531e83af048e46ee95` |
| `…/code-organisme-94bfd92/orchestrator/pole/selection_pari.py` (lu) | `359928110d757cd54cc0d2773910c7360895b68cac5d17e0e4b4e9933ef306bc` |
| `…/code-organisme-94bfd92/orchestrator/pole/nul_v8.py` (lu) | `cc452aafd17121a7c0ec42829eea47063ffee1f6cdf7f642e264d528f976b888` |
| `…/code-organisme-94bfd92/orchestrator/pole/nul_filles_v2.py` (lu) | `0ed9b4adbcddc4ad77a1c97d5cbd5706f14926e9c47fe96ce2bab3221a138910` |
| `…/code-organisme-94bfd92/orchestrator/pole/a_blanc_v59.py` (lu) | `606aa8b4fcc38786b38cf2954da46533eed9384232a56100d22ff30b8ce0826c` |
| `…/code-organisme-94bfd92/orchestrator/pole/cycle.py` (lu : lignes 295 à 330) | `798f039042e3ee1f18df5c566f5a0ddee5dac5c98225c8ce621e267174c8ee18` |
| `docs/notes/organisme-conception-propre-v1/relecture-exploratoire-v2/releve-idees-reutilisables-v1.md` (§ 1.1) | `bd253b6c68f6baada0e61b5381f029b52838ca34aa092502e55253c662451c6c` |
| `runs/course-ideation-conception-propre-v1/20261113-235541-course-ideation-conception-propre-v1-g1/copies/sortie--fiches-validees.json` (fiches argon-p1-01, argon-p2-01, opus-p1-05, fable-p1-05) | `a9f9594e2dc3a7a553c54577202817758e3f7ef231445f1a48d500fc647389d5` |
| `docs/verdicts/verdict-validation-nul-v9-v1.md` (seul fichier ouvert de ce dossier, par son chemin exact) | `1407e460367754bb9f76b37174f3a21585970864eb9beaa2699494d90125c1ea` |

Dossier de l'auteur : les 54 fichiers du rendu (10 à la racine, 44 dans `sorties/`) ont une empreinte égale à leur
compagnon et à celle que le rendu annonce ; aucun n'a été modifié.

« Puissance perdue », par le verdict lu : le v9 tient sa taille (18 lignes fatales sur 18) mais perd contre le v8
apparié 105 promotions sur 1 000 sur la ligne I02 (0,381 contre 0,486), au-delà de la marge de 0,05 ; trois autres pertes
(0,038 à 0,046) ne sont pas jugeables.

## 2. (a) La preuve, suivie pas à pas

Je reprends les énoncés de `methodes-projection-v1.md`, section 3, avec ses notations.

**Lemme 1 (valeur e de bloc).** Aucun pas faux.
1. *Espérance = produit.* Sachant le passé, φ et q sont fixés (P3, P4) et les issues du bloc sont indépendantes sous un
   même θ (P2). Donc E_θ[Π_s r_s(y_s)] = Π_s m_s(θ), avec m_s(θ) = Σ_y P_θ(y | x_s)·r_s(y). Juste. Ce pas emploie P4 :
   voir la section 5, où je montre ce qui arrive quand P4 manque.
2. *Moyennes.* Π m_s ≤ ((1/b)·Σ m_s)^b pour des m_s ≥ 0. Juste.
3. *Sommets.* (1/b)·Σ_s m_s(θ) est affine en θ ; son maximum sur le polytope est pris en un sommet. Juste. J'ai vérifié
   la liste des sommets des deux familles. « Bruit commun » : le polytope {π_c ≥ 0, ρ ≥ 0, Σ_j π_{c,j} + Σ_k ρ_k = 1 pour
   chaque cellule c} est l'enveloppe de deux pièces, le produit des simplexes des cellules (ρ = 0) et le simplexe du
   bruit (π = 0) ; ses sommets sont « une loi connue par cellule » et « une loi certaine δ_k ». « Bruit par cellule » :
   produit de simplexes, sommets « une composante par cellule ». Le code calcule bien ces maximums
   (`certificat_commun` : somme sur les cellules du maximum sur j, comparée au maximum sur k ; `certificat_cellule` :
   somme sur les cellules du maximum sur les composantes).
4. *Division.* E ≤ (c / max(1, c))^b ≤ 1. Juste.

Deux remarques. Le lemme ne demande ni que φ soit dans la famille, ni qu'elle somme à 1 : le plancher numérique
(10⁻³⁰⁰) ne coûte donc pas la validité. Et la borne est atteinte : au bloc de taille 1 elle est une égalité, et pour une
projection exacte le monde « égal à la projection » donne une espérance égale à 1 (contrôle X1, section 4.2).

**Lemme 2 (certificat égal à 1 à la projection).** Juste : condition d'optimalité d'une fonction convexe sur un convexe,
puis θ = φ*. Il faut P_φ* > 0 là où q > 0 ; c'est vrai ici (lois softmax strictement positives).

**Proposition 3.** Juste (inégalité de Jensen sur la loi jointe « instance uniforme dans le bloc, issue tirée de q »).
Elle dit que la projection est le meilleur choix **parmi les valeurs e de cette forme** (une loi φ, certificat par la
moyenne), pas parmi toutes les valeurs e ; l'auteur le dit (numéraire non calculable).

**Théorème 4.** Juste : la richesse de la famille du monde est une surmartingale positive aux fins de bloc ; le minimum
sur les familles reste dessous ; inégalité de Ville sur huit instants. Le nombre de familles n'entre pas dans la borne.
Même chose pour la valeur arrêtée de la règle e-BH.

**Méthodes dérivées.** M4 (borne de l'union sur huit horizons fixes) : juste. M5 : juste, et W ≤ 1 trajectoire par
trajectoire (les lois certaines sont des sommets). M6 : juste pour la classe dite (loi du monde dans l'enveloppe des
lois connues et de l'uniforme à chaque instance, ou monde de la famille linéaire). M7, M7b, M8 : justes (φ ne lit que
le passé). M9 : juste (numérateur gelé par bloc, moyenne de surmartingales).

**Ce que j'ai trouvé en lisant.**
- **Écart 1, important pour le juge, sans effet sur le banc de l'auteur.** L'hypothèse P4 est écrite « q_s ne dépend
  que de x_s et des issues des blocs précédents (pari plein : vrai) ». La parenthèse est fausse pour le juge. Sa
  grammaire a deux types de loi qui lisent l'historique des issues (`selection_pari.TYPES_LISANT_L_HISTORIQUE` :
  « sans_remise », « moyenne_glissante ») ; `valider_loi` les accepte, donc le gardien de `a_blanc_v59` aussi ;
  `cycle.py` (lignes 319 à 326) ne les refuse au gel que dans une configuration (juge v1 sans le membre « urne »). La
  preuve du juge actuel les couvre (hypothèse H5 de la preuve du nul limité : q peut lire les issues passées). La
  méthode par blocs ne les couvre pas : section 5, contre-exemple chiffré.
- **Écart 2, mineur.** Le texte de M6 écrit le certificat par pas comme un maximum sur les lois connues seulement ; le
  code y met aussi l'uniforme (`_pas_a_pas`, maximum sur toutes les colonnes). Le code est juste, le texte est incomplet.
- **Écart 3, de portée.** Pour une copie exacte, la projection de la carte est la carte : chaque facteur vaut 1 et la
  richesse vaut 1 à l'erreur de l'optimiseur près. « 0 promotion sur 1 000 copies » ne mesure donc presque rien pour les
  méthodes de projection (M1 à M4, M2b, M2c, M9). Le cas qui mord est une carte hors du nul dans un monde du nul ;
  l'auteur n'en a joué que deux (T10, T12). J'ai ajouté le pire cas : un monde égal à la projection de la carte
  (sections 4.3 et 4.4).

## 3. (b) Rejeu des programmes de l'auteur

Ses programmes sont relancés tels quels (`python -I`, ses graines), sorties dans mon bac à sable, hors du dépôt. La
comparaison monde par monde est faite par `attaque_projection_v1.py rejeu` et consignée dans ma sortie (pièce
`rejeu.json`).

| essai | ce qui est rejoué | comparaison |
|---|---|---|
| taille | les 100 premiers mondes de chacun des 9 cas joués (900 mondes sur 7 500) | 14 400 couples (méthode, monde) : promotions toutes égales, plus grand log W égal à 4 décimales partout |
| puissance | les 30 premiers mondes de chacune des 9 lignes (270 mondes sur 1 500) | 4 320 couples (bras, monde) : promotions toutes égales |
| lois connues par tirages | tout (2 000 mondes par case) | résultats identiques |
| fusion | les deux fichiers fusionnés | régénérés à l'octet près |

Les chiffres du texte de l'auteur (table de l'artefact, table de puissance, comparaisons appariées, parts regagnées,
table des tirages) sont relus contre ses sorties fusionnées : égaux.

**Les trois cas qu'il avait programmés sans les jouer**, joués ici avec son programme et ses graines (peu de mondes :
la machine était très chargée) :

| cas | mondes | méthodes valides dont le monde est dans la classe | trous attendus | artefact |
|---|---|---|---|---|
| T02, une loi connue seule | 40 | 0/40 pour les douze | — | A1 40/40 ; A2 19/40 (fin), 21/40 (instants) |
| T07, copie par sous-population | 40 | M3 0/40, M5 0/40, M6 0/40 | M1, M2, M2b, M2c, M4, M9 : 40/40 ; M7 7/40 ; M7b 24/40 ; M8 0/40 | A1 40/40 ; A2 40/40 |
| T11, monde linéaire, carte trop confiante | 60 | 0/60 pour les douze (plus grand log W : 2,81 pour M4, lu à 5,08) | — | A1 42/60 et 55/60 ; A2 41/60 (fin), 44/60 (instants) |

Rien dans le rejeu ne contredit le rendu.

## 4. (c) Mon attaque

### 4.1 Le banc (programme `attaque_projection_v1.py`, écrit sans recopier celui de l'auteur)

- **Juge réécrit** : plan de 200 instances (2 traits gaussiens, 2 sous-populations), 3 issues, 8 instants de lecture
  (25, 50, …, 200), α = 0,05, pari plein ; **la promotion compte dès que la richesse passe 20 à l'un des huit instants**
  (M4 : seuil 160, comme l'auteur le définit).
- **Archive** : J − 2 lois softmax, puis deux lois si/sinon dont les seuils (A sur un trait, B sur l'autre) sont les
  coupures de l'archive ; J = 4, ou 12 pour « beaucoup de composantes ». « Peu de tirages » : 40 instances, 8 blocs de 5.
- **Optimiseur** : le mien (espérance-maximisation, avec un pas allongé gardé seulement s'il améliore la valeur), 20 à
  60 pas. Le certificat rend tout état valide ; moins de pas ne coûte que de la puissance. Les certificats sont
  recalculés par mes propres formules.
- **Méthodes** : M1, M2, M2b, M2c, M3, M4, M5, M6, M7, M7b, M8, M9 et les deux artefacts A1, A2, toutes réécrites. M5 est
  calculée exactement (la projection d'une loi sur le simplexe entier est elle-même : richesse égale à 1). Pour M3,
  trois mesures : mon M3 complet (402 familles) ; la « borne » (le processus de la seule vraie famille du monde, qui
  majore M3 trajectoire par trajectoire et coûte peu) ; et le code de l'auteur appelé sur mes mondes.
- **Contrôle exact en plus du comptage.** Pour chaque monde et chaque bloc, je calcule l'espérance exacte de la valeur e
  du bloc sous la loi du monde, sachant le passé réalisé : Π_s Σ_y M_s(y)·q_s(y)/φ_s(y), divisé par le certificat. Le
  lemme 1 dit qu'elle est au plus 1 quand le monde est dans la classe. C'est une vérification sans aléa de la propriété
  de surmartingale, bloc par bloc.
- **Cas** (monde, carte). Copies exactes : membre linéaire à poids de Dirichlet (`copie_lin`) ; poids extrêmes 0,999 et
  0,001 (`copie_extreme`) ; une loi connue seule, au bord du simplexe (`copie_bord_loi`) ; copie par morceaux sur la
  coupure A de l'archive (`copie_coupure_archive`), sur un seuil hors de l'archive (`copie_coupure_hors`), par
  sous-population (`copie_sous_pop`), avec bruit commun (`copie_coupure_bruit`), à deux niveaux (`copie_deux_niveaux`).
  Cartes hors du nul dans un monde du nul : carte trop confiante (`surconfiante`), carte neuve dans un monde coupé
  (`carte_neuve_monde_coupure`), carte très tranchée sans lien avec le monde (`audacieuse`). **Pire cas**, absent du banc
  de l'auteur : la carte est une loi neuve (une loi de l'archive déplacée d'une dose 0,3, 0,6 ou 1,0) et le monde est
  **la projection de cette carte sur la famille** — sur tout le plan (`pire_lin`, `pire_f4`, `pire_coupure_hors`,
  `pire_sous_pop`) ou bloc par bloc (`pire_bloc_lin`, `pire_bloc_f4` : l'espérance de chaque bloc vaut alors exactement
  1, la richesse est une vraie martingale, c'est le monde qui approche le plus la borne de Ville).
- **Graines** : `numpy.random.SeedSequence(entropy=2026111517, spawn_key=(tâche, cas, r, …))`, écrites dans la sortie.
- **Deux façons de compter.** « Mondes » : un engagement neuf (plan, archive, carte, monde) et un jeu d'issues par monde.
  « Amplification » : 100 engagements, 2 000 jeux d'issues chacun (200 000 mondes par cas). Elle est permise parce que
  les projections ne lisent pas les issues, et parce que la garantie est conditionnelle à l'engagement ; l'intervalle est
  alors calculé sur les 100 engagements.

### 4.2 Contrôles exacts

- **X1 — borne du lemme 1.** 2 304 essais (blocs de 1, 2, 5 et 25 ; 2, 4 ou 12 lois connues ; 1, 2 ou 4 cellules ; les
  deux familles ; φ de quatre sortes : projection, projection arrêtée après 3 pas, poids au hasard, poids au bord du
  simplexe ; cartes douces, tranchées ou presque certaines). Pour chacun, je cherche le plus grand logarithme
  d'espérance de la valeur e du bloc sur tout le polytope des poids (fonction concave, espérance-maximisation, plus les
  sommets). Résultat : **jamais au-dessus de 0** ; égal à 0 pour la projection menée à terme (la borne est atteinte),
  de −3·10⁻² à −15,5 pour les autres φ au bloc de 25.
- **X2 — énumération complète, peu de tirages.** Deux issues, 4 blocs de 3, les 4 096 suites possibles ; richesse =
  minimum de trois familles (linéaire et deux coupures) ; 150 engagements par niveau ; mondes : la projection par bloc
  sur chaque famille (pire cas) et deux membres linéaires au hasard. Plus grande **probabilité exacte** de promotion :
  0,4785 pour α = 0,5 ; 0,1921 pour α = 0,25 ; 0,0686 pour α = 0,1. Plus grande espérance exacte de la valeur arrêtée :
  1,000000. La borne de Ville est tenue, et presque atteinte : la méthode n'a pas de marge cachée.

### 4.3 Taille, monde par monde (un engagement neuf et un jeu d'issues par monde)

Promues / mondes. En italique : le monde est hors de la classe de la méthode (« trou », mesuré, sans garantie). Case
vide : non calculé. Source : `sortie-attaque-projection-v1.json`, champ `taille_par_cas`.

| cas | M1 | M2 | M2b | M3 (borne : vraie famille) | M4 | M5 | M6 | M2c | M7 | M7b | M8 | M9 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| copie exacte, membre linéaire | 0/2020 | 0/2020 | 0/2020 | 0/2020 | 0/2020 | 0/2020 | 0/2020 | 0/2020 | 0/2020 | 0/2020 | 0/2020 | 0/2020 |
| poids extrêmes (0,999 et 0,001) | 0/3000 | 0/3000 | 0/3000 | 0/3000 |  | 0/1000 | 0/1000 | 0/1000 | 0/1000 | 0/1000 | 0/1000 |  |
| bord du simplexe (une loi connue seule) | 0/3000 | 0/3000 | 0/3000 | 0/3000 |  | 0/1000 | 0/1000 | 0/1000 | 0/1000 | 0/1000 | 0/1000 |  |
| beaucoup de composantes (12 lois connues) | 0/3000 | 0/3000 | 0/3000 | 0/3000 |  | 0/1000 | 0/1000 | 0/1000 | 0/1000 | 0/1000 | 0/1000 |  |
| peu de tirages (40, blocs de 5), copie | 0/2000 | 0/2000 | 0/2000 | 0/2000 |  | 0/2000 | 0/2000 | 0/2000 | 0/2000 | 0/2000 | 0/2000 |  |
| copie par morceaux, coupure de l'archive | *trou 1954/2000* | 0/2000 | 0/2000 | 0/2000 |  | 0/2000 | 0/2000 | 0/2000 | 0/2000 | 0/2000 | 0/2000 |  |
| copie par morceaux, seuil hors archive | *trou 1983/2050* | *trou 1820/2050* | *trou 1856/2050* | 0/2050 |  | 0/2000 | 0/2000 | *trou 1740/2000* | *trou 33/2000* | *trou 251/2000* | *trou 27/2000* |  |
| copie par sous-population | *trou 99/100* | *trou 99/100* | *trou 99/100* | 0/100 |  | 0/100 | 0/100 | *trou 99/100* | *trou 10/100* | *trou 59/100* | *trou 10/100* |  |
| copie par morceaux avec bruit commun | *trou 88/100* | 0/100 | 0/100 | 0/100 |  | 0/100 | *trou 11/100* | 0/100 | 0/100 | 0/100 | 0/100 |  |
| copie à deux niveaux | *trou 100/100* | 0/100 | *trou 97/100* |  |  | 0/100 | 0/100 | 0/100 | 0/100 | 0/100 | 0/100 |  |
| **pire cas**, famille linéaire, par bloc, dose 0,6 | 35/2120 | 26/2120 | 21/2120 | 35/2120 | *trou 0/120* | 0/2120 | 4/2120 | 17/2120 | 0/2120 | 0/2120 | 0/2120 | 0/120 |
| **pire cas**, peu de tirages (40), dose 1,0 | 15/1000 | 7/1000 | 4/1000 | 15/1000 |  | 0/1000 | 6/1000 | 3/1000 | 0/1000 | 0/1000 | 0/1000 |  |
| **pire cas**, seuil hors archive, dose 0,6 | *trou 13/500* | *trou 7/500* | *trou 8/500* | 7/500 |  |  |  |  |  |  |  |  |
| **pire cas**, quatre cellules, dose 0,6 |  |  |  |  | 4/2000 |  |  |  |  |  |  | 16/2000 |
| carte trop confiante, monde linéaire | 0/100 | 0/100 | 0/100 | 0/100 |  | 0/100 | 0/100 | 0/100 | 0/100 | 0/100 | 0/100 |  |
| carte neuve, monde coupé sur l'archive | *trou 2/100* | 0/100 | 0/100 | 0/100 |  | 0/100 | 0/100 | 0/100 | 0/100 | 0/100 | 0/100 |  |

Par méthode, sur les seuls cas où le monde est dans sa classe :

| méthode | promues / mondes | cas le plus chargé, intervalle à 95 % | espérance exacte d'un bloc au-dessus de 1 |
|---|---|---|---|
| M1 | 50/16 240 | pire cas linéaire : 35/2 120 [0,0115 ; 0,0229] ; à 40 tirages : 15/1 000 [0,0084 ; 0,0246] | jamais |
| M2 | 33/18 540 | 26/2 120 [0,0080 ; 0,0179] | jamais |
| M2b | 25/18 440 | 21/2 120 [0,0061 ; 0,0151] | jamais |
| M3, borne par la vraie famille | 57/21 090 | 35/2 120 [0,0115 ; 0,0229] ; seuil hors archive : 7/500 [0,0056 ; 0,0286] | jamais |
| M4 | 4/4 020 | pire cas à quatre cellules : 4/2 000 [0,0006 ; 0,0051] | jamais |
| M5 | 0/14 640 | richesse égale à 1, par calcul | jamais |
| M6 | 10/14 540 | à 40 tirages : 6/1 000 [0,0022 ; 0,0130] | jamais |
| M2c | 20/12 540 | 17/2 120 [0,0047 ; 0,0128] | jamais |
| M7 | 0/12 540 | plus grand log W d'une copie : 2,59 (seuil 3,00) | jamais |
| M7b | 0/12 540 | plus grand log W d'une copie : 2,07 | jamais |
| M8 | 0/12 540 | plus grand log W d'une copie : 1,48 | jamais |
| M9 | 16/4 140 | pire cas à quatre cellules : 16/2 000 [0,0046 ; 0,0130] | jamais |

Lecture.
- **Aucune borne haute ne passe α = 0,05.** Les plus hautes (0,036) viennent de cas à 100 mondes sans promotion ; là
  où il y a des promotions, la plus haute est 0,0286 (7/500), et 0,0229 sur les cas à 2 000 mondes.
- **Le contrôle exact tient sur chaque monde** : sur 161 810 couples (méthode, monde) dans la classe, l'espérance exacte
  d'une valeur e de bloc sous le monde n'a jamais dépassé 1 (à 10⁻⁹ près). Hors classe elle dépasse 1 dans presque tous
  les mondes (par exemple M1 sur une copie par morceaux : 2 000 mondes sur 2 000), comme attendu.
- **Les copies exactes ne disent presque rien** pour les projections (écart 3, section 2) : la richesse d'une copie
  reste près de 1. Elle s'en écarte quand l'optimiseur est arrêté tôt (jusqu'à 1,07 en logarithme pour M1 et 1,69 pour
  M2 avec 20 pas, sur une loi au bord du simplexe) : valide, mais la règle d'audit « une carte membre ne dépasse jamais
  1 » ne vaut plus telle quelle. Pour M7, M7b et M8 la richesse d'une copie est un vrai pari (jusqu'à 2,59).
- **Le pire cas mord** : 1,0 % à 1,7 % de promotions dans la classe, contre 0 chez l'auteur. C'est le régime normal
  d'une valeur e serrée ; cela reste sous α.
- **Les trous déclarés par l'auteur sont retrouvés** : M1 laisse passer la copie par morceaux (97,7 %), M2, M2b et M2c
  la copie à un seuil hors de l'archive (87 % à 91 %), M2b la copie à deux niveaux (97/100), M6 la copie avec bruit
  commun (11/100 ; lui : 41/500).

### 4.4 Amplification : 100 engagements, 2 000 jeux d'issues chacun

Taux moyen de promotion et intervalle à 95 % calculé sur les engagements ; « pic » : plus grand taux d'un engagement
(2 000 tirages) ; « nets » : engagements dont la borne basse de Clopper-Pearson dépasse α. Mon M3 est ici le M3
complet (402 familles).

| cas | méthode dans la classe | promues / mondes | taux moyen [intervalle] | pic | nets |
|---|---|---|---|---|---|
| pire cas linéaire par bloc, dose 0,6 (60 pas) | M1 | 3 357/200 000 | 0,0168 [0,0158 ; 0,0178] | 0,0325 | 0 |
| | M2 | 2 819/200 000 | 0,0141 [0,0129 ; 0,0153] | 0,0305 | 0 |
| | M2b | 2 239/200 000 | 0,0112 [0,0100 ; 0,0124] | 0,0325 | 0 |
| | M3 | 1 057/200 000 | 0,0053 [0,0043 ; 0,0063] | 0,0220 | 0 |
| le même, optimiseur poussé à 300 pas (60 engagements) | M1 | 2 040/120 000 | 0,0170 [0,0157 ; 0,0184] | 0,0325 | 0 |
| | M2 | 1 756/120 000 | 0,0146 [0,0131 ; 0,0162] | 0,0305 | 0 |
| | M2b | 1 400/120 000 | 0,0117 [0,0101 ; 0,0132] | 0,0325 | 0 |
| | M3 | 707/120 000 | 0,0059 [0,0045 ; 0,0073] | 0,0220 | 0 |
| pire cas linéaire par bloc, dose 0,3 | M1 | 3 100/200 000 | 0,0155 [0,0141 ; 0,0170] | 0,0305 | 0 |
| | M3 | 719/200 000 | 0,0036 [0,0028 ; 0,0044] | 0,0170 | 0 |
| pire cas linéaire, un seul membre, dose 0,6 | M1 | 3 222/200 000 | 0,0161 [0,0150 ; 0,0173] | 0,0280 | 0 |
| | M2 | 2 606/200 000 | 0,0130 [0,0118 ; 0,0142] | 0,0270 | 0 |
| | M2b | 2 020/200 000 | 0,0101 [0,0089 ; 0,0113] | 0,0255 | 0 |
| | M3 | 973/200 000 | 0,0049 [0,0039 ; 0,0058] | 0,0225 | 0 |
| pire cas, seuil hors archive, dose 0,6 (60 pas) | M3 | 1 257/200 000 | 0,0063 [0,0055 ; 0,0071] | 0,0180 | 0 |
| | M3, borne | 3 464/200 000 | 0,0173 [0,0163 ; 0,0183] | 0,0270 | 0 |
| le même, 300 pas (60 engagements) | M3 | 717/120 000 | 0,0060 [0,0052 ; 0,0068] | 0,0180 | 0 |
| pire cas, sous-population, dose 0,6 | M3 | 845/200 000 | 0,0042 [0,0034 ; 0,0051] | 0,0185 | 0 |
| pire cas, quatre cellules par bloc, dose 0,6 | M2 | 3 526/200 000 | 0,0176 [0,0166 ; 0,0187] | 0,0285 | 0 |
| pire cas, quatre cellules, un seul membre | M2 | 3 031/200 000 | 0,0152 [0,0140 ; 0,0163] | 0,0280 | 0 |
| carte trop confiante, monde linéaire | M1 | 949/200 000 | 0,0047 [0,0037 ; 0,0058] | 0,0215 | 0 |
| | M3 | 54/200 000 | 0,0003 [0,0001 ; 0,0004] | 0,0040 | 0 |
| carte neuve, monde coupé sur l'archive | M2 | 191/200 000 | 0,0010 [0,0004 ; 0,0015] | 0,0170 | 0 |
| | M3 | 81/200 000 | 0,0004 [0,0002 ; 0,0007] | 0,0075 | 0 |
| carte très tranchée, monde linéaire | M1 | 19/200 000 | 0,0001 | 0,0030 | 0 |

Lecture. Dans la classe, le taux moyen ne dépasse pas 1,8 % et aucun engagement n'est nettement au-dessus de α (pic
3,25 %). Le nombre de pas de l'optimiseur ne change pas la lecture (60 ou 300 pas : 1,68 % et 1,70 % pour M1). Hors
classe, la même mesure voit les trous : dans le monde à quatre cellules, M1 monte à 14,5 % en moyenne (pic 74,6 %,
54 engagements nets), M2b à 4,1 % (22 nets), M3 à 1,9 % (5 nets) ; dans le monde coupé hors archive, M1 a 13 engagements
nets et M2 en a 3.

### 4.5 Le code de l'auteur sur mes mondes

| mes mondes | ce que j'appelle | résultat |
|---|---|---|
| pire cas, seuil hors archive (dans la classe de M3) | son `m3_toutes_coupures` | **3/500 [0,0012 ; 0,0174]** |
| copie par morceaux, seuil hors archive | son M3 et mon M3 complet, mêmes mondes | 0/50 et 0/50 ; écart de log W au plus 0,80 |
| pire cas linéaire par bloc | ses M1, M2, M2b, M2c, M6, M7, M7b, M8, M9 | 2, 3, 0, 1, 0, 0, 0, 0, 0 sur 120 (mes écritures, mêmes mondes : 2, 2, 0, 1, 0, 0, 0, 0, 0) |
| copie exacte, membre linéaire | ses onze méthodes hors M3 | 0/20 chacune |
| les deux précédents | ses A1 et A2 | A1 : mêmes trajectoires que les miennes (écart 0,000) ; A2 : 17 et 17 sur 20, 48 et 49 sur 120 |

Lecture. Son code tient sa taille sur mes mondes. Avec 120 mondes, 2 ou 3 promotions ne donnent pas un intervalle sous
α à elles seules (borne haute 0,059 pour 2/120, 0,071 pour 3/120) ; les taux observés (1,7 % et 2,5 %) sont ceux de mes
écritures sur 2 120 mondes (1,7 % et 1,2 %). Les richesses des deux codes diffèrent parfois de plus d'un nat (jusqu'à
2,8 pour M2) : écart d'optimiseur, les deux restant valides. Son M3 dépasse ma « borne » de plus de 0,05 nat dans 19
mondes sur 500 (au plus 1,5 nat) : ma borne est calculée avec 50 pas seulement et paie un certificat plus lourd ; elle
majore mon M3 (0 dépassement sur les 50 mondes où j'ai calculé les deux), pas le sien.

## 5. Le contre-exemple : une carte qui lit l'historique du bloc (hypothèse P4)

**Ce que dit l'auteur.** P4 : « q_s ne dépend que de x_s et des issues des blocs précédents (pari plein : vrai) ».

**Ce que fait le juge.** La loi d'une carte est évaluée par `selection_pari.proba(loi, instance, historique, t)`, qui
reçoit les issues passées. Deux types de la grammaire les lisent : « sans_remise » (p_k ∝ c_k − nombre de k déjà vus)
et « moyenne_glissante ». `valider_loi` les accepte. Le juge actuel reste valide avec elles : son numérateur est un
produit de lois prévisibles et son dénominateur majore la vraisemblance du monde (hypothèse H5 de la preuve du nul
limité). La méthode par blocs, elle, calcule sa projection et son certificat sur les lois q_s du bloc. Si ces lois
dépendent des issues du bloc, le pas 1 du lemme 1 tombe : la loi φ du bloc n'est plus fixée avant ses issues.

**Calcul exact (deux issues, un bloc de deux tirages, nul = les lois constantes).** Carte : pile ou face au premier
tirage, puis « l'autre issue, sûrement ». Projection sur les lois réalisées : la moyenne des deux lois de la carte ;
certificat égal à 1. Sous un monde pile ou face de probabilité p (membre du nul), l'espérance exacte de la valeur e du
bloc vaut **1,3333 pour p = 0,5**, 1,12 pour p = 0,3 et 0,48 pour p = 0,1. Au-dessus de 1 : ce n'est plus une valeur e.

**À l'échelle du juge** (200 tirages, 8 blocs de 25, 3 issues, 4 lois connues ; projection et certificat de chaque bloc
calculés sur les lois que la carte a réalisées ; neuf réglages, tous rapportés ; l'ordre des essais est dit en
section 11). « Blocs » : méthode M1,
mon écriture. « Témoin vrai » : rapport de vraisemblance de la carte au monde, une martingale exacte, lu aux mêmes
instants. « Témoin gelé » : la même carte, mais son historique n'est relu qu'au début de chaque bloc (P4 rétablie).

| n° | monde (membre du nul) | carte | blocs : promues / mondes [intervalle à 95 %] | moyenne de la valeur e du premier bloc (± erreur type) | témoin vrai | témoin gelé |
|---|---|---|---|---|---|---|
| 0 | loi uniforme | « sans_remise », composition 70 / 70 / 70 | **206/2 000 [0,090 ; 0,117]** | 1,118 ± 0,002 | 0/2 000 | 0/2 000 |
| 1 | loi uniforme | « sans_remise », 100 / 100 / 100 | 0/1 000 [0 ; 0,004] | 1,078 ± 0,002 | 0/1 000 | 0/1 000 |
| 2 | loi uniforme | « sans_remise », 200 / 200 / 200 | 0/1 000 [0 ; 0,004] | 1,030 ± 0,001 | 0/1 000 | 0/1 000 |
| 3 | ½·L_1 + ½·L_2 | mélange à parts égales du monde et de « sans_remise » (100) | 0/1 000 [0 ; 0,004] | 1,017 ± 0,001 | 15/1 000 | 0/1 000 |
| 4 | ½·L_1 + ½·L_2 | mélange à parts égales du monde et de « sans_remise » (70) | 0/2 000 [0 ; 0,002] | 1,031 ± 0,001 | 26/2 000 | 0/2 000 |
| 5 | ½·L_1 + ½·L_2 | ¾ du monde, ¼ de « sans_remise » (70) | 0/1 000 [0 ; 0,004] | 1,011 ± 0,001 | 16/1 000 | 0/1 000 |
| 6 | ½·L_1 + ½·L_2 | monde incliné contre l'excès du bloc, force 0,1 | **420/2 000 [0,192 ; 0,229]** | 1,33 ± 0,01 | 7/2 000 | 0/2 000 |
| 7 | ½·L_1 + ½·L_2 | monde incliné contre l'excès du bloc, force 0,3 | **904/2 000 [0,430 ; 0,474]** | 2,13 ± 0,04 | 59/2 000 | 0/2 000 |
| 8 | ½·L_1 + ½·L_2 | monde incliné contre l'excès du bloc, force 1,0 | **75/1 000 [0,059 ; 0,093]** | 3,26 ± 0,55 | 22/1 000 | 0/1 000 |

« Incliné contre l'excès du bloc » : q_s(y) ∝ M_s(y)·exp(−force·(nombre de y déjà vus dans le bloc − nombre attendu)).

**Les autres méthodes par blocs, et le code de l'auteur**, sur les 60 premiers mondes des réglages 0 et 7 (mêmes lois
réalisées) :

| réglage | M1 (moi) | M2 (moi) | M2b (moi) | M3 (moi) | M1 (code de l'auteur) | M2 (code de l'auteur) | M3 (code de l'auteur) |
|---|---|---|---|---|---|---|---|
| 0 | 6/60 | 3/60 | 3/60 | 1/60 | 7/60 | 5/60 | 4/60 |
| 7 | 31/60 | 29/60 | 23/60 | 18/60 [0,19 ; 0,43] | 32/60 | 29/60 | 19/60 [0,20 ; 0,45] |

**Lecture.**
- Dans les neuf réglages, la moyenne de la valeur e du premier bloc dépasse 1 (de 1,011 à 3,26, à plus de quatre
  erreurs types). Avec une carte qui lit l'historique du bloc, la valeur de bloc n'est pas une valeur e.
- Le taux de promotion dépasse α dans quatre réglages sur neuf : 10,3 % avec une loi de la grammaire même du juge
  (« sans_remise ») dans un monde uniforme ; 21 %, 45 % et 7,5 % avec une carte écrite pour l'attaque dans un monde que
  seul le membre linéaire couvre. M3, avec ses 402 familles, tombe aussi : 18 sur 60 dans mon écriture, 19 sur 60 dans le
  code de l'auteur.
- Le témoin gelé ne promeut rien (0 sur 13 000) : geler l'historique au début du bloc rétablit la validité.
- **Limites de ce contre-exemple, dites.** (i) Dans le juge complet, le monde uniforme est aussi couvert par le membre
  ordinaire « uniforme », que la proposition de l'auteur garde (minimum des deux richesses) : le réglage 0 seul ne
  ferait donc pas promouvoir. (ii) Les mélanges de « sans_remise » (réglages 3 à 5, écrits dans la grammaire) cassent
  l'espérance (1,011 à 1,031) mais n'ont promu aucune carte sur 4 000 mondes. (iii) La carte des réglages 6 à 8 est
  faite pour l'attaque ; je n'ai pas vérifié qu'elle s'écrit dans la grammaire, ni si le gabarit des proposeurs de la
  boucle réelle permet les deux types qui lisent l'historique. (iv) L'auteur n'a pas essayé de carte à mémoire : son banc
  ne pouvait pas voir ce trou.
- **Conséquence.** Les méthodes par blocs (M1, M2, M2b, M2c, M3, M4, M7, M7b, M8, M9) ne valent que pour une carte
  dont la loi ne lit pas les issues du bloc jugé (M4 : de tout l'horizon). Ce n'est pas acquis au pari plein. Il faut
  une garde écrite, que la section 9 de l'auteur n'a pas : refuser au gel toute carte dont la loi contient un type de
  `TYPES_LISANT_L_HISTORIQUE`, ou n'évaluer sa loi qu'avec l'historique arrêté au début du bloc (ce qui change ce que
  la carte parie). C'est un rétrécissement de ce que le juge accepte aujourd'hui : décision de Lazar. M5 et la partie
  pas à pas de M6 ne sont pas touchées (blocs d'une instance).

## 6. (d) L'artefact : les deux façons des fiches échouent, dans son banc et dans le mien

- **Dans son banc** (rejeu, section 3) : chiffres retrouvés à l'identique sur les mondes rejoués ; la table de la
  section 5 de son texte est égale à sa sortie fusionnée (A1 de 933/1 000 à 1 000/1 000 ; A2 lu à 200 de 283/500 à
  814/1 000).
- **Dans le mien** (mes écritures de A1 et de A2, mes mondes ; copies exactes d'un membre de la famille des fiches) :

| cas | A1, pas 0,05 | A1, pas 0,2 | A2, lu à la fin | A2, lu aux instants de la seconde moitié |
|---|---|---|---|---|
| copie d'un membre linéaire | 1 880/2 020 [0,919 ; 0,941] | 2 020/2 020 | 1 662/2 020 [0,805 ; 0,839] | 1 715/2 020 |
| copie par morceaux, coupure de l'archive | 2 000/2 000 | 2 000/2 000 | 1 166/2 000 [0,561 ; 0,605] | 1 200/2 000 |
| poids extrêmes | 1 000/1 000 | 1 000/1 000 | 595/1 000 [0,564 ; 0,626] | 612/1 000 |
| une loi connue seule | 1 000/1 000 | 1 000/1 000 | 594/1 000 [0,563 ; 0,625] | 622/1 000 |
| 12 lois connues | 756/1 000 [0,728 ; 0,782] | 993/1 000 | 865/1 000 | 881/1 000 |
| 40 tirages seulement | 818/2 000 [0,387 ; 0,431] | 1 206/2 000 | 1 777/2 000 | 1 800/2 000 |
| copie à deux niveaux | 100/100 | 100/100 | 53/100 [0,428 ; 0,631] | 56/100 |
| copie par morceaux avec bruit commun | 99/100 | 100/100 | 79/100 | 85/100 |

  Et pour une carte hors classe dans un monde de la classe : carte trop confiante, 32/100 et 71/100 (A1), 47/100 (A2) ;
  carte neuve dans un monde coupé, 15/100 et 10/100 (A1), 5/100 (A2).
- **Preuve sans aléa.** Sur chacun des 4 020 mondes des deux premières lignes, l'espérance exacte du rapport, sachant
  le passé réalisé, est au-dessus de 1 : pour A2, E[W final | première moitié] ; pour A1, la somme le long de la
  trajectoire des logarithmes d'espérance de chaque facteur. Les mêmes quantités, pour les méthodes certifiées, ne
  dépassent jamais 1.
- **Même code, même défaut vu.** Sur 140 de mes mondes, mon A1 et le sien donnent la même trajectoire (écart 0,000 :
  c'est la formule de la fiche) ; mon A2 et le sien promeuvent 17 et 17 copies sur 20, puis 49 et 48 cartes sur 120
  (un monde d'écart, optimiseurs différents).
- Les deux façons sont donc bien non valides, et l'échec ne vient pas de son banc. Copie exacte promue : 65 % à 100 %
  dans la pièce d'origine, 56,6 % à 100 % chez lui, 41 % à 100 % chez moi (le plus bas, 41 %, est A1 au petit pas avec
  40 tirages seulement ; à 200 tirages et 1 000 mondes au moins, 58 % à 100 %). Toutes les bornes basses sont loin
  au-dessus de α.

## 7. (e) Puissance annoncée et loyauté de la comparaison

- **Rejeu.** Les 30 premiers mondes de chacune des 9 lignes de puissance, rejoués avec le programme de l'auteur : mêmes
  promotions, bras par bras (section 3). Les taux, les différences appariées et les intervalles du texte sont ceux de
  `sortie-puissance-v1.json`, relus : M3 contre R9 de +0,045 à +0,185, tous les intervalles de Wald au-dessus de 0 ; part
  de la perte regagnée de 0,41 à 0,82 ; M3 contre R8 de −0,200 à −0,020 ; M1 contre R8 de +0,030 à +0,105 ; M2b contre RLa
  de +0,035 à +0,160.
- **Mêmes tirages, mêmes instants, même seuil : oui.** Lu dans `essai_projection_puissance_v1.py` (`un_monde`) et
  `essai_projection_methodes_v1.py` (`references`) : un seul dictionnaire de monde par répétition, donc la même carte et
  les mêmes 200 issues pour tous les bras ; lecture aux 8 instants pour tous ; seuil log 20 pour tous, sauf M4 lu à
  log 160 par construction. La référence R9 parcourt bien la classe du v9 (linéaire, sous-population, toute coupure
  d'un trait) : la même que M3.
- **La référence n'est ni handicapée ni vraiment avantagée.** L'auteur écrit que ses références sont « avantagées »
  parce qu'il prend la valeur atteinte par son optimiseur. J'ai recalculé, sur 18 de ses mondes (V1 dose 0,5 : 10 ;
  V3 dose 0,8 : 4 ; V4 dose 0,2 : 4 ; ses graines), le maximum de vraisemblance de la classe du v9 à chaque instant,
  par mon optimiseur, avec la valeur atteinte et la borne certifiée par l'écart de Frank-Wolfe (la formule de
  `nul_v9._certificats`, réécrite). Son dénominateur ne dépasse ma borne certifiée dans aucun des 18 mondes (plus grand
  dépassement : 7·10⁻¹⁵). Ma valeur atteinte dépasse la sienne d'au plus 0,0038 nat, et la sienne dépasse la mienne
  d'au plus 0,0011 nat. Sa référence est donc au maximum, à quelques millièmes de nat près : la comparaison au
  « maximum certifié » est loyale, et « l'avantage » qu'il déclare est négligeable. Sur ces 18 mondes : R9 de l'auteur
  10 promues, mon maximum atteint 10, mon maximum certifié 10 ; M3 de l'auteur 12, mon M3 12.
- **Mon M3 et le sien** diffèrent d'au plus 0,66 nat sur ces mondes, avec les mêmes promotions. Les deux sont valides ;
  l'écart vient des optimiseurs (une projection moins aboutie paie 25·log c par bloc). C'est assez pour déplacer une
  promotion à la marge : l'ampleur des gains dépend du soin de l'optimiseur.
- **Ce que le rejeu ne dit pas.** (i) L'ampleur ne se transpose pas : sur ce banc R9 perd jusqu'à 0,37 contre R8, alors
  que le verdict du v9 donne 0,105 au plus sur son banc ; l'auteur le dit. (ii) Le gain de la projection a un prix que
  la table de puissance ne montre pas : la garantie ne couvre plus les cartes qui lisent l'historique (section 5), et la
  propriété « une carte membre a une richesse au plus 1, tirage par tirage » (remarque (ii) du théorème 1 de la preuve
  du nul limité, règle d'audit du préenregistrement) devient « proche de 1 » : la richesse d'une copie exacte est montée
  jusqu'à 0,25 en logarithme dans son banc pour M3, et jusqu'à 1,07 dans le mien pour M1 quand l'optimiseur est arrêté
  tôt. (iii) Je n'ai pas refait la puissance sur un banc à moi : la charge de la machine ne l'a pas permis.

## 8. Lois connues seulement par tirages (P1, P2)

Cas d'école de l'auteur, réécrit (deux lois sur trois issues, nul = le segment qui les joint, carte = copie d'un vrai
membre, 2 000 mondes par taille m, blocs de 25, 8 instants). Copies promues :

| m tirages par loi | rayon de la boule | vraies lois | « comme si exact » (P1) | certificat robuste (P2) | mondes où les deux boules contiennent la vraie loi |
|---|---|---|---|---|---|
| 50 | 0,53 | 0/2 000 | **395/2 000 [0,180 ; 0,216]** | 0/2 000 | 2 000/2 000 |
| 200 | 0,27 | 0/2 000 | 68/2 000 [0,027 ; 0,043] | 0/2 000 | 2 000/2 000 |
| 1 000 | 0,12 | 0/2 000 | 0/2 000 | 0/2 000 | 2 000/2 000 |

- **P1 : l'échec est réel**, pas un défaut de son banc. Avec les vraies lois, les mêmes mondes ne promeuvent rien ;
  avec les lois estimées prises pour exactes, 19,8 % des copies passent à m = 50 (lui : 21,5 %). À m = 200 mon taux
  (3,4 %) est sous α, comme le sien (3,1 %) : la faute se voit aux petits m.
- **P2 : le calcul tient.** La majoration Σ L·f ≤ Σ L̂·f + (ε/2)·(max f − min f) est juste (L − L̂ est de somme nulle
  et de norme 1 au plus ε). Dans aucun des 6 000 mondes le certificat robuste n'est passé sous le vrai certificat. Les
  boules ont contenu la vraie loi dans tous les mondes (la borne de concentration employée est donc large ici). La
  garantie α + δ reste suspendue à cette borne (Weissman et autres, 2003, **à vérifier sur pièce**), que je n'ai pas
  vérifiée sur pièce. Cas d'école seulement : rien pour des lois qui dépendent de traits ; l'auteur le dit.
- Réduction dite : m = 5 000 non joué (charge de la machine).

## 9. Ce que l'adoption changerait et que la section 9 de l'auteur ne dit pas

1. **La garde sur les cartes qui lisent l'historique** (section 5). Sans elle, la garantie du juge rétrécit en silence.
   La section 9, point 8, prévoit de refuser un φ qui lirait une issue du bloc ; il faut la même garde sur q.
2. **La règle de marge des filles.** `nul_filles_v2.evaluer_v2` (et `nul_v9.evaluer_sur_issues`) calcule le gain moyen
   contre la meilleure « enveloppe », c'est-à-dire la vraisemblance maximale des membres ajustés aux n tirages. Si le
   membre linéaire et les membres par morceaux passent au produit de blocs, cette valeur n'existe plus pour eux : la
   règle est à redéfinir (ou le maximum à garder pour elle seule).
3. **La règle d'audit « une carte membre ne dépasse jamais 1 »** (preuve du nul limité, remarque (ii) du théorème 1)
   devient « reste près de 1 » ; l'écart dépend des pas de l'optimiseur (0,05 à 1,7 en logarithme dans mes essais). Il
   faut un seuil d'audit écrit, et le nombre de pas gelé.
4. **L'optimiseur entre dans le résultat.** Deux écritures valides de la même méthode donnent des richesses qui
   diffèrent parfois de plus d'un nat. La règle d'arrêt de l'optimiseur doit être gelée sous l'empreinte, et le
   certificat journalisé (l'auteur le prévoit, point 4).

## 10. Verdict par méthode

« Garde P4 » : la méthode ne vaut que si la loi de la carte ne lit pas les issues du bloc jugé (section 5) ; sans cette
garde écrite dans le juge, je ne la tiens pas pour branchable. Les chiffres sont ceux de mes écritures sur mes mondes,
dans la classe de la méthode, sauf mention.

| méthode | verdict | raison et chiffre |
|---|---|---|
| **M3** — projection par blocs, toutes les coupures du plan | **tient**, sous la garde P4 | Preuve sans pas faux ; rejeu identique. Borne par la vraie famille : 57/21 090 ; pire cas 35/2 120 [0,0115 ; 0,0229]. Mon M3 complet, amplifié : 0,36 % à 0,63 %, pic d'un engagement 2,25 %. Code de l'auteur sur mes mondes du pire cas : 3/500 [0,0012 ; 0,0174]. Puissance rejouée, référence loyale. **Contre-exemple hors hypothèse** : carte qui lit l'historique, 18/60 (moi) et 19/60 (son code). Le trou « deux niveaux » est celui du v9, comme dit. |
| **M1** — projection sur le membre linéaire | **tient**, sous la garde P4 | 50/16 240 ; pire cas 35/2 120 [0,0115 ; 0,0229] ; amplifié 1,7 %, pic 3,25 %. Son code : 2/120 au pire cas, 0/20 sur des copies. Contre-exemple hors hypothèse : 904/2 000 (45 %). |
| **M2** — partition à quatre cellules, bruit commun | **tient**, sous la garde P4 | 33/18 540 ; pire cas 26/2 120 [0,0080 ; 0,0179] ; amplifié 1,4 % à 1,8 %, pic 3,05 %. Son code : 3/120. Trou hors archive retrouvé (88,8 %). |
| **M2b** — minimum sur linéaire, A, B | **tient**, sous la garde P4 | 25/18 440 ; pire cas 21/2 120 [0,0061 ; 0,0151]. Son code : 0/120. Trous retrouvés (hors archive 90,5 % ; deux niveaux 97/100). |
| **M4** — horizon fixe, seuil de Bonferroni | **tient**, sous la garde P4 étendue à tout l'horizon | 4/4 020 ; pire cas à quatre cellules 4/2 000 [0,0006 ; 0,0051]. Attaque partielle : deux cas à 2 000 mondes (copie, pire cas), pas les autres. |
| **M5** — pas à pas avec lois certaines | **tient** (valide, sans puissance) | Richesse au plus 1 trajectoire par trajectoire, par calcul ; 0/14 640 ; son code 0/140. Pas de garde à ajouter (blocs d'une instance). |
| **M6** — pas à pas sur l'enveloppe, minimum avec M1 | **tient** pour la classe dite ; garde P4 pour sa partie M1 | 10/14 540 ; au plus 6/1 000 [0,0022 ; 0,0130]. Trou « bruit commun » retrouvé : 11/100 (lui : 41/500). Texte incomplet sur le certificat (l'uniforme manque), code juste. |
| **M2c** — projection sur la famille des fiches | **tient**, sous la garde P4 | 20/12 540 ; pire cas 17/2 120 [0,0047 ; 0,0128]. Son code : 1/120. |
| **M7** — poids appris sur le passé, certifiés | **tient** (valide, sans puissance), sous la garde P4 | 0/12 540 ; plus grand log W d'une copie 2,59 sous le seuil 3,00 ; espérance exacte de bloc jamais au-dessus de 1. |
| **M7b** — M7 mêlé à la projection | **tient**, sous la garde P4 | 0/12 540 ; plus grand log W d'une copie 2,07. |
| **M8** — moitié, certifiée par bloc | **tient**, sous la garde P4 | 0/12 540 ; plus grand log W d'une copie 1,48. |
| **M9** — fraction gelée par bloc | **tient**, sous la garde P4 | 16/4 140 ; pire cas à quatre cellules 16/2 000 [0,0046 ; 0,0130]. Attaque partielle, comme M4. |
| **A1** — poids en ligne, sans correction | **ne tient pas** (l'auteur a raison) | Copie exacte promue : 1 880/2 020 et 2 020/2 020 ; l'échec est réel, vu dans mon banc et dans le sien, et l'espérance exacte dépasse 1 sur chaque monde. |
| **A2** — moitié, sans correction | **ne tient pas** (l'auteur a raison) | Copie exacte promue : 1 662/2 020 [0,805 ; 0,839] lue à la fin ; 1 166/2 000 sur une copie par morceaux ; espérance exacte au-dessus de 1 sur chaque monde. |
| **P1** — lois par tirages, certificat « comme si exact » | **ne tient pas** (l'auteur a raison) | 395/2 000 [0,180 ; 0,216] à 50 tirages par loi ; 0/2 000 avec les vraies lois sur les mêmes mondes. |
| **P2** — lois par tirages, certificat robuste | **tient** dans le cas d'école, sous la borne de concentration non vérifiée sur pièce | 0/6 000 ; certificat robuste jamais sous le vrai ; boules couvrantes 6 000/6 000. |

Aucun rejet à tort : je n'ai trouvé aucune méthode que l'auteur dit non valide et qui serait valide.

## 11. Ce que je n'ai pas fait, et les réductions (toutes dites)

- **Charge de la machine.** La charge est montée à 24 sur 4 cœurs ; mes simulations ont eu par moments moins d'un
  dixième de cœur chacune. Tranches arrêtées ou hors délai, sans sortie et non comptées : la première file (tranches
  trop longues), une tranche « poids extrêmes », deux tranches légères du pire cas hors archive (remplacées par
  l'amplification), l'essai « tirages » en un seul appel (rejoué par taille m), m = 5 000.
- **« Au moins 2 000 mondes par cas »** : tenu, par mes écritures, pour M1, M2, M2b et la borne de M3 sur les sept
  cas demandés (copie exacte, poids extrêmes, bord du simplexe, beaucoup de composantes, peu de tirages, copie par
  morceaux sur une coupure de l'archive et hors d'elle) et sur le pire cas linéaire. Pour M5, M6, M2c, M7, M7b, M8 :
  2 000 mondes sur quatre de ces cas et sur le pire cas, 1 000 sur les trois autres (poids extrêmes, bord, 12 lois).
  Pour M4 et M9 : 2 000 mondes sur deux cas seulement (copie exacte, pire cas à quatre cellules). Cas secondaires
  (sous-population, bruit commun, deux niveaux, carte trop confiante, carte neuve) : 100 mondes, complétés par
  l'amplification pour M1 à M3.
- **Mon M3 complet** n'est joué monde par monde que sur 50 mondes ; le reste vient de l'amplification (100 ou
  60 engagements, 2 000 jeux d'issues chacun), dont l'intervalle est calculé sur les engagements. Le code de l'auteur
  pour M3 est joué sur 500 + 50 de mes mondes, pas 2 000.
- **Code de l'auteur sur mes mondes, toutes méthodes** : 140 mondes seulement (2 secondes par monde).
- **Nombre de pas de l'optimiseur** : 20 pas pour les copies jouées en fin de session, 50 ou 60 ailleurs, 300 pour un
  contrôle. Moins de pas rend mes écritures un peu plus prudentes ; le contrôle à 300 pas ne change pas les taux.
- **Puissance** : rejouée (270 mondes), référence encadrée (18 mondes), **non refaite sur un banc à moi**.
- **Rejeu** : 12 % des mondes de taille, 18 % des mondes de puissance ; cas non joués par l'auteur : 40 à 60 mondes.
- **Contre-exemple de la section 5** : les neuf réglages ont d'abord été essayés à petite échelle (30 à 150 mondes)
  avant les courses rapportées ; les réglages 6 à 8 ont été ajoutés après le premier essai des réglages 0 à 5. Les
  neuf sont rapportés. La carte des réglages 6 à 8 n'est pas vérifiée comme écrivable dans la grammaire.
- **Programme** : des sous-commandes et des options ont été ajoutées en cours de session (amplification, rejeu,
  contrôle, tranches). Les fonctions de calcul de la taille n'ont pas changé depuis la première tranche gardée ; une
  tranche rejouée avec la version scellée donne les mêmes comptes pour ses quinze méthodes (pièce `controle.json`).
- **Non regardé** : le vrai code du v9 n'est pas exécuté (règle des dossiers de copie) ; les membres ordinaires et
  log-linéaires du juge ne sont pas au banc ; la borne de concentration de P2 n'est pas vérifiée sur pièce.

## 12. Fichiers et empreintes (sha256 ; chacun scellé par un compagnon `.sha256`)

Dossier `docs/notes/organisme-idees-juge-v1/correction-poids-v1/projection/` :

| fichier | sha256 |
|---|---|
| `attaque_projection_v1.py` | `c6161399704d5d6eac1743c364caa08a4f4da9fb2bb2d710b0357235cf8a4257` |
| `sortie-attaque-projection-v1.json` | `07e9e8dbfe3930d6e6421ff76ecffb47f681acd0fcd684bab7247522090da686` |
| `refutation-projection-v1.md` (cette note) | dans son compagnon |

La sortie réunit 120 pièces (champ `pieces`) : 90 tranches de taille, 9 réglages « mémoire », 12 amplifications
(dont 2 à 300 pas), 3 essais « tirages », 3 encadrements de la référence, le contrôle exact, le rejeu, le contrôle de
non-régression. Le nom de chaque pièce donne sa commande (cas, tranche, options) ; chaque pièce porte ses graines et
ses réglages. Le champ `taille_par_cas` somme les tranches par cas. Les sorties rejouées des programmes de l'auteur
sont restées dans mon bac à sable ; leur comparaison est dans la pièce `rejeu.json`.

Pour rejouer une tranche : `python -I attaque_projection_v1.py taille CAS R0 R1 SORTIE.json` avec les options du nom
de la pièce (par exemple `--n 40 --J 4 --it 50 --sans-m4-m9`), une simulation par appel, sous dix minutes.

