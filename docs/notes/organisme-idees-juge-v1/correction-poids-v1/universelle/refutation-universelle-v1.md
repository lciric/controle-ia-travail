# Réfutation — angle « inférence universelle bien faite » (correction des poids du nul) — v1

**Statut.** Mise au point exploratoire, **aucune revendication**. Aucun préenregistrement : rien ici n'est une expérience
décisive. Toutes les issues sont rapportées à l'identique. Aucun essai ne vise un signe.

- Réfutateur : sous-agent neuf de la session mère, d'un autre modèle que l'auteur ; je n'ai écrit aucune des pièces citées.
- Date : 2026-11-15, de 14:36 à 15:58 UTC (`date -u`) ; dépôt lu sur `main`, tête `a3b7883a`. Aucun commit, aucune
  poussée, aucun appel réseau, aucun appel payant. Aucun fichier de l'auteur n'est modifié.
- Calculs : Python 3.13.18, numpy 2.4.6, scipy 1.17.1 (`.venv/bin/python -I -B`), processeur seul, 2 ou 3 processus par
  lancement, machine partagée (charge de 9 à 13). Chaque lancement a tenu en moins de dix minutes (le plus long : 473 s).
- Pièce réfutée : `methodes-universelle-v1.md` (`324e1243f4d508f5ebb26ff67cb490e9e56e1cdd7c25dc1d45ab2d009b6fa2c4`) et les
  27 autres fichiers du rendu de l'auteur, même dossier.

## 0. Verdict en tête

**Aucune méthode dite valide n'est réfutée.** Les six tiennent leur taille sous l'attaque la plus dure que j'ai su
construire : taux de fausse promotion de 4,0 % à 4,7 %, bornes hautes à 95 % de 4,2 % à 4,9 %, pour un niveau de 5 %.
La borne est donc approchée, pas dépassée. Les quatre méthodes dites non valides le sont bien : leur échec est réel dans
le banc de l'auteur (rejeu exact) et dans le mien. Tous les lots rejoués redonnent les sorties scellées, monde par monde.

**Trois affirmations du rendu ne tiennent pas telles quelles** (aucune ne touche la validité d'une méthode) :
1. « La lecture dense ne peut que promouvoir plus » : faux. Les instants 10, 20, …, 200 ne contiennent pas 25, 75, 125,
   175. Contre-exemple calculé : 158 mondes sur 4 000 où le juge promeut et la lecture dense non ; et 6 mondes sur 3 600
   dans mon banc de puissance, sans construction. La correction est simple : lire l'union des deux jeux d'instants.
2. « Le prix du v9 vient surtout de la liberté des poids par morceau, moins de la recherche des coupures » : non établi.
   La base de ses mondes de puissance est elle-même une copie par morceaux que le v8 ne couvre pas : le v8 la promeut
   dans 17,3 % des mondes sans aucune composante neuve. Sur une base sans coupure, son propre banc donne des parts égales :
   v8 → limité −0,100 / −0,100 / −0,047 ; limité → v9 −0,090 / −0,103 / −0,057.
3. « Les variantes valides tiennent leur taille : 0 promotion sur 400 à 1 000 mondes » : vrai, mais sans portée. Pour une
   copie exacte, ces méthodes rendent W ≤ 1 par construction ; ce 0 ne teste ni le pas de Ville ni le compte β + (α − β).
   Mon attaque (cartes qui ne sont pas des copies) fait ce test, et trois variantes fausses de contrôle y sont vues.

**Un constat de portée.** Le « v9 du banc » (neuf déciles par trait) n'est pas le v9 : il promeut 50,8 %
[48,6 % ; 53,0 %] des copies par morceaux coupées entre deux déciles, que le vrai v9 couvre. L'auteur déclare la grille ;
il ne mesure pas ce trou. Les puissances « contre le v9 » se lisent donc contre une référence plus petite que le juge.

| méthode (nom du rendu) | dit par l'auteur | verdict | raison | chiffre |
|---|---|---|---|---|
| Référence : maximum certifié sur tous les tirages | valide | **tient** | preuve sans pas faux ; rejeu exact ; certificat de son code jamais en défaut ; attaque sous α | pire taux 1 857/40 000 = 0,0464 [0,0444 ; 0,0485] ; copies 0/2 000 dans 8 cas |
| Fiche argon-p2-01 : poids appris en ligne | non valide | **ne tient pas** (échec réel) | rejeu exact de ses 955 à 1 000 promotions sur 1 000 ; même échec dans mon banc | copies promues : 0,709 à 1,000 (pas 0,05), 0,880 à 1,000 (pas 0,2), 2 000 mondes par cas |
| Fiche argon-p1-01 : poids ajustés sur la première moitié | non valide | **ne tient pas** (échec réel) | rejeu exact de ses 97, 148, 360, 435 sur 1 000 ; même échec dans mon banc | copies promues : 0,106 à 0,642 dans les six cas de sa classe |
| Moitié jugée | valide | **tient** | théorème appliqué à la seconde moitié ; attaque sous α ; perte de puissance rejouée | pire taux 1 839/40 000 = 0,0460 [0,0439 ; 0,0481] |
| Découpes croisées, moyenne des valeurs e | valide | **tient** | lemme C juste ; attaque sous α ; la variante « maximum des deux parts » est vue fausse | pire taux 1 806/40 000 = 0,0452 [0,0431 ; 0,0472] |
| Sous-échantillonnage, quatre moitiés | valide | **tient** | lemme C juste ; attaque sous α | pire taux 1 783/40 000 = 0,0446 [0,0426 ; 0,0466] |
| Région de confiance apprise sur D1 | valide | **tient** | lemme D juste ; attaque sous α ; la variante « seuil 1/α » est vue fausse ; perte de puissance de structure (section 8.2) | pire taux 1 617/40 000 = 0,0404 [0,0385 ; 0,0424] |
| Lecture dense du v9 | valide | **tient**, avec une correction | valide (Ville) ; gain rejoué ; mais elle ne contient pas la lecture du juge (point 1 ci-dessus) | pire taux 1 860/40 000 = 0,0465 [0,0445 ; 0,0486] |
| Dénominateur pénalisé vers le bas | non valide | **ne tient pas** (échec réel) | un nat : défaut **mesuré** ici, là où l'auteur le démontrait seulement ; complexité : rejeu exact | un nat : 1 197/10 000 = 0,120 [0,113 ; 0,126] ; complexité : 300/300 dans 8 cas |
| Mélange a priori des membres | non valide | **ne tient pas** (échec réel) | rejeu exact de ses 179, 543, 330 sur 1 000 ; même échec dans mon banc | copies promues : 0,110 ; 0,337 ; 0,467 (300 mondes par cas) |

Lecture du mot « ne tient pas » pour une méthode que l'auteur dit non valide : la méthode ne tient pas, donc son rejet
par l'auteur est juste. Aucun rejet à tort n'est trouvé.

## 1. Ce que j'ai lu et vérifié (empreintes recalculées le 15 novembre, égales à leurs compagnons)

| pièce | chemin | sha256 |
|---|---|---|
| preuve de validité du nul limité | `docs/notes/organisme-idees-juge-v1/preuve-validite-nul-limite-v1.md` | `44f249409193778ccbaaa12b6c5e74d64434dfb87be77382d8bb9438459281b2` |
| préenregistrement de l'idée 1.1 | `docs/notes/organisme-idees-juge-v1/prereg-nul-par-morceaux-limite-v1.md` | `46ef2b92119ee5dff05727b90ca8bdd3ba57b52f9c1c75893750c792a2abc089` |
| contre-lecture | `docs/notes/organisme-idees-juge-v1/contre-lecture-prereg-nul-limite-et-preuve-v1.md` | `763fc6e29cd80868dcdb1d848eafdc928a39fca7244fa16eb0ac721ec705014e` |
| nul v9 (copie, lue, jamais exécutée ni importée) | `docs/notes/organisme-idees-juge-v1/copie-nul-v9-a41b7b5/orchestrator/pole/nul_v9.py` | `7ae450df2482246122bf9fbcf0fa5ef30b4a7e4c6f0d09531e83af048e46ee95` |
| pari, tirages frais | `docs/notes/organisme-courbe-dose-reponse-v1/code-organisme-94bfd92/orchestrator/pole/selection_pari.py` | `359928110d757cd54cc0d2773910c7360895b68cac5d17e0e4b4e9933ef306bc` |
| nul v8 | `…/code-organisme-94bfd92/orchestrator/pole/nul_v8.py` | `cc452aafd17121a7c0ec42829eea47063ffee1f6cdf7f642e264d528f976b888` |
| membres ajustés, certificat, instants | `…/code-organisme-94bfd92/orchestrator/pole/nul_filles_v2.py` | `0ed9b4adbcddc4ad77a1c97d5cbd5706f14926e9c47fe96ce2bab3221a138910` |
| jugement d'une carte fraîche | `…/code-organisme-94bfd92/orchestrator/pole/a_blanc_v59.py` | `606aa8b4fcc38786b38cf2954da46533eed9384232a56100d22ff30b8ce0826c` |
| relevé, section 1.1 | `docs/notes/organisme-conception-propre-v1/relecture-exploratoire-v2/releve-idees-reutilisables-v1.md` | `bd253b6c68f6baada0e61b5381f029b52838ca34aa092502e55253c662451c6c` |
| fiches argon-p1-01 (n° 0), opus-p1-05 (n° 9), fable-p1-05 (n° 13), argon-p2-01 (n° 14) | `runs/course-ideation-conception-propre-v1/20261113-235541-course-ideation-conception-propre-v1-g1/copies/sortie--fiches-validees.json` | `a9f9594e2dc3a7a553c54577202817758e3f7ef231445f1a48d500fc647389d5` |
| verdict de la validation du v9 (ouvert par son chemin exact ; seul fichier lu dans ce dossier) | `docs/verdicts/verdict-validation-nul-v9-v1.md` | `1407e460367754bb9f76b37174f3a21585970864eb9beaa2699494d90125c1ea` |
| note de l'auteur | `…/correction-poids-v1/universelle/methodes-universelle-v1.md` | `324e1243f4d508f5ebb26ff67cb490e9e56e1cdd7c25dc1d45ab2d009b6fa2c4` |
| banc de l'auteur | `…/universelle/banc_universelle_v1.py` | `68381bc5de78d928af29c6fae5084145f420911eca91873de9d929d6ebc6cb12` |

Les 49 fichiers du dossier de l'auteur ont une empreinte égale à leur compagnon ; les 28 empreintes de son rendu sont
celles des fichiers. Ses tables (sections 5.1 à 5.3 de sa note) sont égales, cellule par cellule, aux comptes de ses
sorties. Les quatre fiches disent bien ce qu'il leur prête (champ `demande_organisme` lu en entier).

Ce que « puissance perdue » veut dire dans le verdict du 8 novembre : les 18 lignes fatales sont tenues ; la perte
appariée de puissance du v9 contre le v8 dépasse la marge sur une ligne (interaction faible hors de l'archive). Je ne
reprends aucun chiffre de ce verdict dans mes essais.

Le juge, tel que le code le calcule (`a_blanc_v59.juger_carte`, `nul_v9.evaluer_sur_issues`) : 200 tirages frais, huit
instants lus (25, 50, …, 200), promotion si log W_t ≥ log(1/α) à l'un d'eux, α = 0,05 ; le dénominateur est le maximum
des membres, chacun avec son certificat. Le banc de l'auteur et le mien reprennent ces réglages.

## 2. Les preuves, suivies pas à pas (point a)

Je n'ai trouvé aucun pas faux dans les quatre lemmes. Je donne pour chacun ce que j'ai vérifié, et sa portée exacte.
Le seul énoncé faux est une phrase de la remarque sur la lecture dense.

**Lemme A (le maximum est le plus petit dénominateur qui domine).** Vrai : le supremum est le plus petit majorant, point
par point. Portée : le lemme parle d'un dénominateur unique par instant, qui domine tous les membres à cet instant. Il ne
dit rien d'une règle qui rejette chaque famille du nul à son propre instant (section 8.1), ni d'une valeur e qui ne
domine pas trajectoire par trajectoire (la projection inverse, que l'auteur nomme lui-même). La phrase « le seul gain
valide est la lecture dense » se lit donc « parmi ce que j'ai joué » ; l'auteur écrit d'ailleurs « je n'ai trouvé aucune
façon ».

**Lemme B (un dénominateur qui est une loi de probabilité promeut les copies).** Vrai : Σ P²/D ≥ (Σ P)²/Σ D = 1
(Cauchy-Schwarz) et E[log W] est une divergence de Kullback-Leibler, donc positive (Gibbs). Portée : E[W] ≥ 1 dit que W
n'est pas une valeur e ; cela ne suffit pas à dire que le test au seuil 1/α dépasse α. Le dépassement est une mesure, pas
une conséquence du lemme ; elle est faite (rejeu exact de ses lots, et mon banc, section 5). Pour le mélange a priori
tel qu'il le code (mélange des maxima certifiés des 21 partitions), le dénominateur n'est pas une loi normalisée ;
l'auteur le dit et borne par W ≤ 21·Λ : juste.

**Lemme C (moyenne de valeurs e de parts fixées d'avance).** Vrai. Chaque Λ^b est une martingale positive de départ 1
pour la filtration de tous les tirages (facteur 1 hors de la part) ; une moyenne à poids fixes de martingales sous la
même loi en est une ; l'inégalité de Ville borne tous les instants. La condition « parts fixées avant les issues » est
nécessaire et tenue dans son code (graine scindée de celle du monde, `sous_ensembles`). Le lemme vaut aussi pour un
numérateur prévisible (pari à fraction du juge). La moyenne est nécessaire : avec le maximum des deux parts à la place,
la garantie tombe à 2·α, et mon attaque le voit (section 4.4).

**Lemme D (région de confiance apprise sur une part).** Vrai. (1) P(θ* ∉ C) ≤ β, par Markov sur q(D1)/L_θ*(D1), dont
l'espérance est au plus 1. (2) Sur {θ* ∈ C}, le terme ajouté λ·[log L_θ*(D1) − log q(D1) + log(1/β)] est positif, donc
chaque B_λ majore log L_θ*(D0) ; le maximum pondéré est concave et son certificat est exact (∇f·x = somme des poids ;
vérifié dans son code, `Solveur._gradients`, et par mon recoupement). (3) Λ sur D0 est une martingale, indépendante de D1
quand la carte est gelée : Ville au niveau α − β. (4) Somme : α. Le compte « β, puis α − β » est celui qu'il faut : une
lecture au seuil 1/α au lieu de 1/(α − β) donnerait α + β. Mon attaque sépare les deux : 2,1 % contre 6,8 % sur la même
carte (section 4.4).

**Remarque sur la lecture dense.** La validité est juste : le pas 4 de la preuve du nul limité borne tous les instants
de 1 à n dès que D_t ne lit que les t premières issues. La seconde moitié de la phrase est fausse : « lire à chaque
dizaine de tirages au lieu de chaque vingt-cinquaine […] ne peut que promouvoir plus ». Les instants denses de son code
(`INSTANTS_DENSES = range(10, 201, 10)`) ne contiennent pas 25, 75, 125 et 175. **Contre-exemple calculé**
(`contre_exemple_lecture_dense_v1.py`) : monde tranchant (section 4.3), carte qui parie au tirage 23 (gain de
probabilité 1/22) puis au tirage 27. À l'instant 25 la richesse vaut 22 si le premier pari est gagné : le juge promeut.
À l'instant 20 rien n'est parié ; à l'instant 30 le second pari est presque toujours perdu. Sur 4 000 mondes : juge
164 promotions, lecture dense 6 ; **158 mondes promus par le juge et pas par la lecture dense**, 0 dans l'autre sens ;
premier monde contre-exemple : r = 31 (`sortie-contre-exemple-lecture-dense-v1.json`). Sans construction, mon banc de
puissance en trouve aussi : 6 mondes sur 3 600 (5 à la dose 0,40 et 1 à la dose 0,55, base par morceaux), contre 51 dans
l'autre sens. Sur les 900 mondes de l'auteur il n'y en a aucun : son « (2/0, 8/0, 0/0) » est exact, sa généralisation
ne l'est pas. Correction : lire l'union des instants (ou tous les cinq tirages) ; alors seulement la lecture dense
contient celle du juge.

**Lecture de fond, que je partage.** La condition H4 (domination de la vraisemblance du vrai membre sur la part jugée)
est suffisante, non nécessaire ; les deux façons des fiches la violent, et les bancs montrent qu'elles perdent en plus
la taille.

## 3. Rejeu des programmes de l'auteur (point b)

`rejeu_universelle_v1.py` lance ses scripts tels quels, avec ses graines, en écrivant hors du dépôt, puis compare aux
sorties scellées. Même clé ⇒ même monde : un rejeu sur les R' premiers mondes se compare au début des chaînes « promue »
et « log_w_max ». Résultat : **26 étapes, 134 lignes (étape, méthode), 0 monde en désaccord, tous les comptes des rejeux
complets égaux, plus grand écart de log W maximal 0,0**. Détail dans `sortie-rejeu-universelle-v1.json`.

| lots de l'auteur | rejeu | résultat |
|---|---|---|
| puissance, lots « a » et « b », trois doses (dix et trois méthodes) | complet, 300 mondes par lot | identique monde par monde ; v9 0,080 / 0,493 / 0,800 et toutes les autres lignes de sa table 5.2 |
| puissance, grille fine, dose 0,25 | complet, 200 mondes | identique : v8 78, limité 31, v9 15, confiance 4 |
| taille « interieur » (premier lot, sans détail par monde), neuf méthodes | complet, 1 000 mondes | comptes égaux (v8 209, fiches 955 / 999 / 435, mélange 0, complexité 1 000), log W maximal et médian égaux |
| taille, les deux fiches, cinq autres cas | complet, 1 000 mondes par cas | identique monde par monde (par exemple sommet : 1 000 / 1 000 / 97 ; bruite : 993 / 999 / 360) |
| taille, lots « a », cinq cas, neuf méthodes | 250 premiers mondes sur 1 000 | identique monde par monde |
| taille, lots « b », cinq cas, quatre variantes à découpe | 150 premiers mondes sur 600 ou 400 | identique monde par monde |
| taille « interieur », quatre variantes à découpe | 150 premiers mondes | 0 promotion, log W maximal négatif (sa sortie n'a pas de détail par monde à comparer) |
| lecture dense, « interieur » et « sommet » | 200 premiers mondes sur 1 000 | identique monde par monde |
| appariements (`essai_universelle_appariement_v1.py`) | complet | sortie identique à l'octet (`662874bd…`) |
| coût (`essai_universelle_cout_v1.py`) | complet, autre charge machine | mêmes ordres : v9 0,170 s ; rapports au v9 : dense 1,7 ; moitié jugée 0,7 ; croisées 1,4 ; sous-échantillons 2,8 ; confiance 1,8 (lui : 1,6 ; 0,7 ; 1,3 ; 2,5 ; 1,7) |

Limites : les lots de taille « a » et « b » sont rejoués sur une part des mondes pour tenir dix minutes par lancement ;
le pilote qui a placé ses doses n'a pas de script gardé (il le dit) et ne se rejoue pas.

Recoupement de plus, par un autre solveur : mon calcul du v9 sur ses 900 mondes de puissance (maxima encadrés à
10⁻⁴ nat, section 8.1) redonne ses promotions monde par monde (24, 148, 240 ; 0 désaccord), et sa lecture dense à la
dose 0,40 (156 ; 0 désaccord).

## 4. Mon attaque (point c)

### 4.1 Le programme

`attaque_universelle_v1.py`, écrit sans recopier le banc de l'auteur. Ce qui diffère :
- **le calcul du maximum** : tout point du polytope d'une famille est un mélange de ses sommets (« une loi connue par
  morceau », « bruit aveugle seul sur une issue ») ; le maximum devient celui d'un mélange sur un simplexe, monté par
  espérance-maximisation avec un pas extrapolé. Pour tout point admissible, je garde la valeur atteinte (borne basse du
  maximum) et le certificat (borne haute, écart de Frank-Wolfe). Auto-essai : sur 120 problèmes tirés au hasard,
  comparés à un optimum calculé à part (méthode SLSQP de scipy, six départs), la référence n'est jamais au-dessus de mon
  certificat, et l'encadrement fait au plus 10⁻⁷ nat de large ;
- **la décision par encadrement** : la statistique d'une méthode décroît quand un maximum du nul monte. Avec les
  certificats elle donne ce que la méthode rend ; avec les valeurs atteintes elle borne ce que tout certificat valide
  pourrait rendre. Promotion si la première passe le seuil à un instant lu ; refus certain si la seconde reste dessous à
  tous les instants ; sinon on itère (plafond : 600 cycles). **Aucun cas indécis au plafond** dans toute l'attaque ;
- **le point du vrai membre** : quand le monde est un membre connu du nul, sa propre vraisemblance est une valeur
  atteinte ; elle tranche d'emblée la plupart des mondes. Ce n'est pas la preuve qu'on suppose : c'est « un maximum vaut
  au moins la valeur en un point ». Vérifié en clair, en refaisant les décisions sans ce point : **0 décision différente**
  (60 mondes par cas souple pour les cartes adverses, 800 mondes par cas tranchant, six méthodes) ; et pour les copies,
  30 mondes par cas résolus sans ce point : log W certifié maximal ≤ 0, borne haute au plus 10⁻⁴ nat ;
- **les mondes et les cartes** : lois connues souples qui dépendent des deux traits et de la sous-population ; membres
  défavorables ; cartes qui ne sont pas des copies.

Les six méthodes dites valides sont réécrites d'après les énoncés de la note (sections 4.1, 4.4 à 4.8), avec les réglages
de l'auteur (α = 0,05 ; β = 0,025 ; multiplicateurs 0 ; 0,25 ; 1 ; 4 ; 16 ; quatre moitiés ; classe « v9 du banc » :
aucune coupure, coupure de l'archive, sous-population, neuf déciles par trait). Arrêt optionnel partout : la promotion
compte si la statistique passe le seuil à l'un des instants lus. En tout : 248 000 mondes de taille, 4 800 de puissance.
Graines : `SeedSequence(entropy=2026111571, spawn_key=(indice du cas, r))` pour la taille, `2026111572` pour la
puissance, scindées en (monde, issues, parts) ; écrites dans la sortie.

### 4.2 Pourquoi les copies ne suffisent pas

Pour une copie exacte d'un membre, toute méthode dont le dénominateur vaut au moins la vraisemblance de ce membre rend
W ≤ 1 : c'est une identité, pas une mesure. Le « 0 promotion sur 400 à 1 000 mondes » de l'auteur pour ses variantes
valides teste le certificat et le code ; il ne teste ni le pas de Ville ni le compte β + (α − β). Une méthode dont la
garantie serait α·e ou 2·α y rendrait aussi 0 (l'auteur le dit pour la pénalité d'un nat seulement). J'ai donc joué des
cartes qui ne sont pas des copies, dans des mondes du nul :
- **copie** (pour le contrôle du code et pour l'artefact) ;
- **surconfiante** : loi du monde élevée à la puissance 1,5 puis normalisée ;
- **loterie** : copie de la loi du monde, sauf en un ou deux tirages où toute la masse va sur une issue de probabilité
  proche de 1/M. Si le pari est gagné, le rapport de vraisemblance simple est multiplié par M ; sinon il tombe à zéro.
  C'est la carte qui approche la borne de Ville.

### 4.3 Membres défavorables, lois souples (2 000 mondes par cas)

Cas : membre intérieur sur la coupure de l'archive ; sommet (une loi connue de chaque côté de la coupure de l'archive) ;
poids extrêmes (0,992 / 0,004 / 0,004, bruit 1 % concentré) ; beaucoup de composantes (sept lois connues) ; peu de
tirages (48 tirages, instants 6 à 48) ; copie par morceaux sur un seuil de la grille ; par sous-population ; membre
sans coupure. Chaque cellule : promotions sur mondes, [borne haute à 95 %], carte la pire.

| cas | copie exacte, les six méthodes | maximum certifié (v9) | lecture dense | moitié jugée | découpes croisées | sous-échantillons | région de confiance |
|---|---|---|---|---|---|---|---|
| interieur | 0/2000 | 0 | 0 | 1/2000 [0,0028] loterie, 2de moitié | 0 | 0 | 0 |
| sommet_archive | 0/2000 | 32/2000 [0,0225] surconfiante | 49/2000 [0,0323] surconfiante | 24/2000 [0,0178] loterie, 2de moitié | 23/2000 [0,0172] surconfiante | 19/2000 [0,0148] surconfiante | 9/2000 [0,0085] surconfiante |
| poids_extremes | 0/2000 | 25/2000 [0,0184] loterie, 2de moitié | 28/2000 [0,0202] loterie, 2de moitié | 32/2000 [0,0225] loterie, 2de moitié | 4/2000 [0,0051] surconfiante | 3/2000 [0,0044] surconfiante | 4/2000 [0,0051] loterie, 2de moitié |
| beaucoup_de_composantes | 0/2000 | 0 | 0 | 0 | 0 | 0 | 0 |
| peu_de_tirages | 0/2000 | 15/1981 [0,0125] loterie, début | 15/1981 [0,0125] loterie, début | 4/1986 [0,0052] loterie, 2de moitié | 1/1986 [0,0028] loterie, 2de moitié | 0 | 1/1986 [0,0028] loterie, 2de moitié |
| morceaux_sur_grille | 0/2000 | 41/2000 [0,0277] loterie, début | 63/2000 [0,0401] surconfiante | 22/2000 [0,0166] loterie, 2de moitié | 24/2000 [0,0178] surconfiante | 21/2000 [0,0160] surconfiante | 15/2000 [0,0123] surconfiante |
| sous_population | 0/2000 | 46/2000 [0,0306] loterie, début | 59/2000 [0,0379] surconfiante | 34/2000 [0,0237] loterie, 2de moitié | 28/2000 [0,0202] surconfiante | 18/2000 [0,0142] surconfiante | 13/2000 [0,0111] surconfiante |
| sans_coupure | 0/2000 | 0 | 0 | 0 | 0 | 0 | 0 |

Lecture : toutes les bornes hautes sont sous α (la plus haute : 0,0401). Les membres intérieurs ne laissent rien
passer : le maximum du nul y dépasse la vraisemblance du vrai membre de plusieurs nats. Les sommets sont les membres
défavorables : le maximum y tombe souvent sur le vrai membre, et la valeur e du juge égale alors le rapport simple.

**Copie par morceaux hors de l'archive et hors de la grille** (`morceaux_hors_grille`, 2 000 mondes, copie exacte,
résolution complète). Ce monde est dans la classe du vrai v9 (tout seuil réel) et hors de la classe du banc. Copies
promues : v8 1 954 (0,977) ; nul limité 1 855 (0,928) ; **v9 du banc 1 016 (0,508 [0,486 ; 0,530])** ; lecture dense
1 042 ; moitié jugée 378 (0,189) ; croisées 525 ; sous-échantillons 557 ; confiance 529. Ce n'est pas une erreur de
taille des méthodes (aucune garantie hors de la classe) : c'est la mesure de l'écart entre le v9 du banc et le v9. Une
classe à grille de déciles (variante (a) du relevé, fiche opus-p1-05) laisse passer la moitié des copies coupées entre
deux déciles, à 200 tirages, dans ce banc.

### 4.4 L'attaque la plus dure : mondes « tranchants » et loteries (40 000 mondes par cas)

Construction. Trois lois connues presque certaines (une issue à 0,9996, les autres à 0,0002), sauf en un ou deux tirages
« tendres » où toutes les lois connues donnent la même loi : l'issue 2 y a la probabilité p. Le monde est un sommet du
nul (une loi connue partout, ou une de chaque côté de la coupure de l'archive, moitié-moitié). Dans un tel monde le
maximum du nul tombe presque toujours sur le vrai membre : la valeur e du juge égale le rapport de vraisemblance simple.
La carte mise tout sur l'issue 2 aux tirages tendres, placés pour la méthode visée (premier bloc ; premier bloc de la
seconde moitié ; un tirage pair et un impair ; un tirage commun aux quatre moitiés ; un dans D1 et un dans le deuxième
bloc de D0). C'est un pire cas : la carte connaît le plan et la loi du monde. Le théorème le couvre (il est conditionnel
au plan). Ce n'est pas une attaque praticable du juge réel, où le plan vient d'une graine que la carte ne voit pas :
c'est une mesure de la marge.

| cas (méthode visée, probabilité de gain) | paris gagnés | rapport simple aux huit instants | maximum certifié (v9) | lecture dense | moitié jugée | découpes croisées | sous-échantillons | région de confiance |
|---|---|---|---|---|---|---|---|---|
| tranchant_v9 (1/22) | 1877 | 1877 (0,0469) | **1857 (0,0464 [0,0444 ; 0,0485])** | **1860 (0,0465 [0,0445 ; 0,0486])** | 0 | 0 | 127 | 0 |
| tranchant_moitie (1/22) | 1852 | 1852 (0,0463) | 1769 (0,0442) | 1777 (0,0444) | **1839 (0,0460 [0,0439 ; 0,0481])** | 0 | 115 | 0 |
| tranchant_croisee (deux paris à 1/42) | 1826 | 17 | 17 | 17 | 0 | **1806 (0,0452 [0,0431 ; 0,0472])** | 489 | 16 |
| tranchant_sous_echantillons (1/22 ou moins) | 1819 | 1819 (0,0455) | 1802 (0,0450) | 1807 (0,0452) | 0 | 0 | **1783 (0,0446 [0,0426 ; 0,0466])** | 0 |
| tranchant_confiance (1/52 dans D1, 1/41 dans D0) | 1681 | 747 | 725 | 728 | 927 | 734 | 745 | **1617 (0,0404 [0,0385 ; 0,0424])** |

Lecture. Chaque méthode valide atteint entre 4,0 % et 4,7 % sous sa carte, et jamais plus que la part des paris gagnés,
dont la probabilité est fixée par construction sous 5 %. Les six bornes hautes à 95 % sont sous α (0,0424 à 0,0486).
Il n'y a donc **aucune marge** : tout relâchement du dénominateur ou du seuil casse la garantie. C'est ce que montrent
les dents.

**Dents (variantes volontairement fausses, 10 000 mondes par cas).**

| variante fausse | carte | variante | méthode valide sur la même carte |
|---|---|---|---|
| pénalité d'un nat (garantie α·e) | un pari à 1/8 | **1 197 (0,120 [0,113 ; 0,126])** | v9 : 0 |
| découpes croisées par le maximum des deux parts (garantie 2·α) | deux paris à 1/22 | **895 (0,090 [0,084 ; 0,095])** | croisées, moyenne : 19 (0,0019) |
| région de confiance lue au seuil 1/α (garantie α + β) | 1/52 dans D1, 1/20,5 dans D0 | **683 (0,068 [0,063 ; 0,073])** | région de confiance : 206 (0,021) |

Les trois bornes basses sont au-dessus de α : l'attaque voit une erreur de compte quand il y en a une, et n'en voit pas
dans les méthodes de l'auteur. La première ligne **mesure** le défaut de la pénalité d'un nat, que l'auteur déclarait
« démontré, pas mesuré » (son angle mort). Elle se voit aussi sans construction : 130/2 000 (0,065 [0,055 ; 0,077]) sous
la carte surconfiante du cas `sous_population`.

### 4.5 Le code de l'auteur sous la même attaque

`recoupement_universelle_v1.py`, mode « tranchant » : mes mondes tranchants et mes cartes (2 500 mondes par cas, mes
graines), jugés par **ses** fonctions et ses réglages. Son code n'est joué que là où un pari est gagné, et sur 40 mondes
témoins par cas : 757 mondes jugés par les deux codes. **Ses décisions sont les miennes dans les 757 mondes, pour les six
méthodes** ; aucun témoin promu ; son log W ne dépasse jamais ma borne haute.

| cas | promotions de son code sur 2 500 | taux [intervalle à 95 %] |
|---|---|---|
| tranchant_v9, maximum certifié | 112 | 0,0448 [0,0370 ; 0,0537] |
| tranchant_moitie, moitié jugée | 134 | 0,0536 [0,0451 ; 0,0632] |
| tranchant_croisee, découpes croisées | 110 | 0,0440 [0,0363 ; 0,0528] |
| tranchant_sous_echantillons | 108 | 0,0432 [0,0356 ; 0,0519] |
| tranchant_confiance, région de confiance | 95 | 0,0380 [0,0309 ; 0,0463] |

Je le dis sans l'adoucir : à 2 500 mondes, quatre bornes hautes dépassent α, et le taux de la moitié jugée est à 5,36 %.
Ces 2 500 mondes ne suffisent donc pas, seuls, à conclure pour son code. Ce qui conclut : (1) toute promotion y est un
pari gagné, et la probabilité de gain est 1/22 par construction (136 gains sur ces 2 500 premiers mondes là où 113,6
sont attendus, soit 2,1 écarts-types ; 1 852 sur les 40 000 mondes du même cas, pour 1 818,2 attendus) ; (2) ses
décisions sont celles de mon code monde par monde, et mon code donne 0,0460 [0,0439 ; 0,0481] sur 40 000.

### 4.6 Ce que l'attaque ne couvre pas

Les réglages de l'auteur seuls (un seul β, une seule découpe 100/100, quatre moitiés) ; des mondes à 2 traits et
3 issues ; la classe du banc, pas celle du vrai v9 ; aucun membre log-linéaire ; une carte gelée (pas de pari à
fraction). Les mondes tranchants sont des tables sur le plan, pas des lois de la grammaire du juge.

## 5. L'artefact : les deux façons des fiches (point d)

**Dans le banc de l'auteur** (rejeu complet, 1 000 mondes par cas, identique monde par monde) : poids appris en ligne,
pas 0,05 : 955 / 1 000 / 1 000 / 993 (interieur, sommet, extreme, bruite) ; pas 0,2 : 999 / 1 000 / 1 000 / 999 ; poids
ajustés sur une moitié : 435 / 97 / 148 / 360. Sur les mêmes mondes, v9 et nul limité : 0.

**Dans mon banc** (copie exacte, 2 000 mondes par cas ; 300 pour les deux dernières colonnes) :

| cas | en ligne, pas 0,05 | en ligne, pas 0,2 | moitié | mélange a priori | pénalité de complexité |
|---|---|---|---|---|---|
| interieur | 1892 (0,946 [0,935 ; 0,956]) | 1998 (0,999) | 876 (0,438 [0,416 ; 0,460]) | 0/300 | 300/300 |
| sommet_archive | 2000 (1,000) | 2000 (1,000) | 212 (0,106 [0,093 ; 0,120]) | 33/300 (0,110 [0,077 ; 0,151]) | 300/300 |
| poids_extremes | 2000 (1,000) | 2000 (1,000) | 296 (0,148 [0,133 ; 0,164]) | 0/300 | 300/300 |
| beaucoup_de_composantes | 1702 (0,851 [0,835 ; 0,866]) | 1997 (0,999) | 1285 (0,642 [0,621 ; 0,664]) | 0/300 | 300/300 |
| peu_de_tirages | 1418 (0,709 [0,689 ; 0,729]) | 1761 (0,880) | 540 (0,270 [0,251 ; 0,290]) | 0/300 | 300/300 |
| sans_coupure | 1817 (0,908 [0,895 ; 0,921]) | 1999 (1,000) | 873 (0,436 [0,415 ; 0,459]) | 0/300 | 300/300 |
| morceaux_sur_grille (hors de la classe des fiches) | 2000 | 2000 | 1784 (0,892) | 101/300 (0,337 [0,283 ; 0,393]) | 300/300 |
| sous_population (hors de la classe des fiches) | 2000 | 2000 | 1979 (0,990) | 140/300 (0,467 [0,409 ; 0,525]) | 300/300 |

Toutes les bornes basses des deux fiches sont au-dessus de α dans les six cas de leur classe. L'échec est réel, pas un
défaut de son banc : autre programme, autres lois, autres mondes, mêmes ordres de grandeur (moitié : 0,438 ici contre
0,435 chez lui pour le membre intérieur ; 0,106 contre 0,097 au sommet ; 0,148 contre 0,148 aux poids extrêmes).

Deux précisions, sans effet sur les verdicts :
- **mélange a priori** : l'auteur joue une variante plus douce que la lettre de fable-p1-05 (il mélange les maxima des
  21 familles). Son échec y tient à 21 > 20 : une copie y atteint au plus log 21 = 3,04 pour un seuil de 3,00. La lettre
  de la fiche (mélange à poids fixes d'un nombre fini de lois) échoue plus fort : pour la copie de la loi i, W tend vers
  1/π_i quand les tirages séparent les lois. Le rejet est juste dans les deux lectures ;
- **pénalité de complexité** : 300/300 partout chez moi, 1 000/1 000 chez lui (rejeu exact pour « interieur »).

## 6. Puissance et loyauté de la comparaison (point e)

**Rejeu.** Les six lots de puissance et le lot à grille fine sont rejoués en entier : identiques (section 3). Les
appariements sont recalculés à l'octet.

**Loyauté.** Vérifiée dans le code (`evaluer`, `un_monde`) : toutes les méthodes d'un lot jugent le même monde et les
mêmes tirages ; le v9 est identique monde par monde entre les lots « a » et « b » (rejeu : 0 désaccord). Instants : huit
pour le v9, les croisées et les sous-échantillons ; les tirages 125, 150, 175, 200 pour la moitié jugée et la région de
confiance (quatre des huit instants du juge) ; seuil log 20 partout, log 40 pour la région de confiance (c'est la
méthode). Un certificat plus lâche pour une méthode que pour une autre aurait pu fausser la comparaison : sur 90 mondes
de puissance recoupés par mon solveur, aucune décision ne change, pour aucune des huit méthodes (section 7).

**Banc indépendant** (le mien, 600 mondes par cellule, mêmes tirages, mêmes instants, même seuil ; taux de promotion) :

| base du monde | dose | v8 | limité | v9 du banc | lecture dense | moitié jugée | croisées | sous-échantillons | confiance |
|---|---|---|---|---|---|---|---|---|---|
| par morceaux (comme l'auteur) | 0 | 0,185 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| par morceaux | 0,25 | 0,388 | 0,170 | 0,092 | 0,103 | 0,007 | 0,013 | 0,012 | 0,012 |
| par morceaux | 0,40 | 0,687 | 0,552 | 0,430 | 0,443 | 0,150 | 0,192 | 0,207 | 0,220 |
| par morceaux | 0,55 | 0,875 | 0,823 | 0,748 | 0,755 | 0,447 | 0,573 | 0,578 | 0,605 |
| sans coupure | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| sans coupure | 0,25 | 0,263 | 0,157 | 0,067 | 0,073 | 0,003 | 0,007 | 0,007 | 0,007 |
| sans coupure | 0,40 | 0,665 | 0,567 | 0,422 | 0,443 | 0,147 | 0,200 | 0,182 | 0,238 |
| sans coupure | 0,55 | 0,888 | 0,840 | 0,743 | 0,758 | 0,433 | 0,552 | 0,588 | 0,573 |

Lecture. L'ordre de l'auteur est retrouvé par un autre programme et d'autres mondes : v8 > limité > v9 ≈ lecture dense >
confiance ≳ sous-échantillons ≳ croisées > moitié jugée. Les quatre variantes à découpe perdent nettement contre le v9
(à la dose 0,40, base par morceaux : promues par le v9 seul 172, 152, 140, 128 ; par la variante seule 4, 9, 6, 2).
Ses chiffres (0,080 / 0,493 / 0,800 pour le v9 ; 0,013 / 0,277 / 0,650 pour la confiance) sont dans les mêmes ordres.
**Sa conclusion principale tient** : aucune des façons valides jouées ne regagne la puissance perdue.

**D'où vient le prix : la lecture de l'auteur ne tient pas.** Il lit « v8 → limité : −0,25 / −0,12 / −0,06 » comme le
prix de la liberté des poids par morceau, et « limité → v9 : −0,05 / −0,11 / −0,05 » comme celui de la recherche des
coupures. Or la base de ses mondes de puissance est un membre « intérieur » : des poids différents de chaque côté de la
coupure de l'archive. Cette base est hors de la classe du v8. `prix_par_morceau_v1.py` rejoue **son** banc (ses
fonctions, son solveur, ses graines, son archive, son plan, sa loi neuve) en changeant la base seule ; avec sa base, les
300 mondes par dose sont les siens et ses comptes sont retrouvés (115 / 39 / 24 ; 217 / 181 / 148 ; 273 / 254 / 240).

| banc de l'auteur, 300 mondes par dose | dose 0 | dose 0,25 | dose 0,40 | dose 0,55 |
|---|---|---|---|---|
| base de l'auteur : v8 / limité / v9 | 0,173 / 0 / 0 | 0,383 / 0,130 / 0,080 | 0,723 / 0,603 / 0,493 | 0,910 / 0,847 / 0,800 |
| base sans coupure : v8 / limité / v9 | 0 / 0 / 0 | 0,260 / 0,160 / 0,070 | 0,690 / 0,590 / 0,487 | 0,890 / 0,843 / 0,787 |
| base sans coupure : écart v8 → limité (mondes perdus) | 0 | −0,100 (30) | −0,100 (30) | −0,047 (14) |
| base sans coupure : écart limité → v9 (mondes perdus) | 0 | −0,090 (27) | −0,103 (31) | −0,057 (17) |

Lecture. Avec sa base, le v8 promeut 17,3 % des mondes **sans aucune composante neuve** (dose 0 ; 18,5 % dans mon banc ;
20,9 % dans son propre cas de taille « interieur »). Son écart « v8 → limité » de −0,25 à la dose 0,25 contient donc une
part qui n'est pas une puissance perdue : c'est la fermeture d'une fausse promotion. Sur une base que toutes les classes
contiennent, les deux parts du prix sont égales à l'incertitude près (30 contre 27 mondes, 30 contre 31, 14 contre 17).
Mon banc dit la même chose, avec une part « recherche des coupures » plutôt plus grande (v8 → limité : −0,107 / −0,098 /
−0,048 ; limité → v9 : −0,090 / −0,145 / −0,097). Conséquence pour le nœud du nul limité : sur ces bancs, un nul limité
à la coupure de l'archive regagnerait à peu près la moitié de l'écart entre le v9 du banc et le v8 (47 % à 55 % dans son
banc, 46 % à 67 % dans le mien, base sans coupure), et non la petite part que sa lecture lui laisse (0,05 sur 0,30 à la
dose 0,25).
Réserve : le v9 du banc n'a que 20 partitions à coupure ; le vrai v9 en parcourt bien plus (section 4.3), et sa part
« recherche » est donc sous-estimée ici comme chez l'auteur.

**Lecture dense.** Gain rejoué à l'identique chez lui : +2, +8, 0 mondes sur 300. Dans mon banc : gain net +0,012 /
+0,013 / +0,007 (base par morceaux) et +0,007 / +0,022 / +0,015 (base sans coupure), avec 6 mondes perdus sur 3 600
(section 2). Faible dans les deux bancs.

## 7. Le solveur de l'auteur, recoupé par le mien

`recoupement_universelle_v1.py`, modes « puissance » et « taille » : sur ses mondes (ses graines), ses log W par
méthode et par instant sont comparés à mon encadrement des mêmes maxima (mêmes tirages, mêmes partitions, mêmes
questions ; mon encadrement fait au plus 0,0015 nat de large).

| mondes de l'auteur | lignes (monde, méthode) | son certificat en défaut | largeur de son certificat : médiane ; plus grande | décisions différentes |
|---|---|---|---|---|
| puissance, 30 par dose | 720 | **0** | 0,002 nat ; 0,46 nat | **0** |
| taille, 18 par cas, six cas | 864 | **0** | 0,001 nat ; 4,09 nat | **0** |

Lecture. « En défaut » voudrait dire que son dénominateur est sous une vraisemblance qu'un membre du nul atteint
(hypothèse H4 rompue) : cela n'arrive jamais. Son certificat est parfois lâche : jusqu'à 0,46 nat sur ses mondes de
puissance, et jusqu'à 4,1 nats sur des copies au sommet ou aux poids extrêmes (400 pas ne suffisent pas au bord du
simplexe). C'est ce qu'il rapporte comme « excès de monotonie jusqu'à 0,82 nat ». Cela coûte de la puissance à la
méthode concernée, jamais de la validité ; sur les 90 mondes de puissance recoupés, aucune promotion n'en dépend.

## 8. Deux constats hors verdict (exploratoires, aucune revendication)

### 8.1 Une piste que le lemme A ne ferme pas : un instant de rejet par famille

Le nul est une union de familles. Règle : promouvoir si, pour **chaque** famille F, il existe un instant lu s_F avec
log q(y_1..s_F) − V_F(s_F) ≥ log(1/α). La statistique est min_F max_s au lieu de max_s min_F pour le juge ; elle vaut
toujours au moins celle du juge. Validité en trois lignes : si le monde est le membre θ* de F*, la promotion exige un
instant s avec log q − V_F*(s) ≥ log(1/α), donc Λ_s ≥ 1/α à un instant lu ; par Ville, la probabilité en est au plus α.
Le choix de s_F après les tirages est permis, puisque Ville borne tous les instants à la fois.
Mesure (`piste_instant_par_famille_v1.py`, maxima par famille encadrés à 10⁻⁴ nat, sans élagage) :
- puissance, sur les 900 mondes de l'auteur : la règle promeut 24, 150, 241 mondes ; le v9 24, 148, 240. **Gain : 0, +2,
  +1 monde sur 300.** Avec les vingt instants denses, dose 0,40 : 157 contre 156 ;
- taille : copies de l'auteur (« interieur », « sommet », « grille », 150 mondes chacun) : 0 promotion, statistique
  certifiée ≤ 0 ; mondes tranchants avec loterie (4 000 mondes par cas) : mêmes promotions que le v9 (178 et 203),
  jamais sans que le rapport simple passe.
Lecture : valide, gratuite en calcul, gain négligeable sur ce banc. Réserve : c'est un test de niveau α pour la carte
seule ; ce n'est pas une valeur e (le maximum courant d'une martingale n'en est pas une), donc elle ne se branche pas
telle quelle sur la règle e-BH du juge. Je la nomme pour que la liste des options soit complète, je ne la propose pas.

### 8.2 Pourquoi la région de confiance perd : presque dominée par le v9, quel que soit β

Notons a(θ) = log L_θ(D0 jusqu'à t), b(θ) = log L_θ(D1), A0 et A1 les mêmes quantités pour la carte. Si la région de
confiance promeut à l'instant t de D0, alors pour tout θ : b(θ) ≤ A1 − log(1/β) ou a(θ) ≤ A0 − log(1/(α − β)). Donc
a(θ) + b(θ) ≤ A0 + A1 − log(1/α) pour tout θ, dès que le maximum du nul ne dépasse pas la carte de plus de log(α/β) nats
sur D0 et de plus de log(α/(α − β)) nats sur D1. Dans ce cas **le v9 promeut aussi**, à l'instant 100 + t. Avec
β = α/2 : dès que la valeur e du v9 restreinte à chaque moitié vaut au moins 1/2. La région de confiance ne peut donc
battre le v9 que dans les mondes où le nul surajuste une moitié de plus de log 2 par rapport à la carte, tout en étant
rejeté 40 fois sur l'autre : des moitiés très déséquilibrées. Données : chez l'auteur, 1 monde sur 900 promu par la
confiance seule (131 par le v9 seul) ; dans mon banc, 12 sur 3 600 (520 par le v9 seul). Changer β ou la découpe déplace
les deux marges sans supprimer l'implication. Un renversement demanderait un surajustement joint du nul de plus de
4,4 nats environ, plus deux fois le surajustement restreint : possible seulement pour une classe bien plus riche que
celle du banc. La suggestion de l'auteur (« à réessayer seulement sur un banc où le prix des coupures domine ») est
cohérente avec cela ; rien ici ne dit que ce banc existe.

## 9. Écarts, limites, ce que je n'ai pas fait

- **Dix minutes par simulation** : tenu. Lancement le plus long : 473 s (code de l'auteur sous l'attaque tranchante) ;
  rejeu le plus long : 439 s. Pour tenir, les lots de taille de l'auteur sont rejoués sur 250 ou 150 mondes (dit en
  section 3), et son code n'est jugé sous mon attaque que sur 2 500 mondes par cas (dit en section 4.5).
- **Un arrêt par identifiant de processus** (2384) : une file d'attente de lancements, arrêtée avant tout calcul pour
  scinder un lancement qui aurait dépassé dix minutes (une dose par lancement ensuite).
- **Contrôles en clair sur sous-échantillons** seulement (30, 60 ou 800 mondes par cas) ; ailleurs la décision s'appuie
  sur le point du vrai membre (section 4.1).
- **Le juge réel n'est pas joué.** Aucun fichier des dossiers de copie n'est exécuté ni importé ; la famille du nul est
  réécrite d'après la lecture de `nul_v9.py` (l. 19 à 25). Le banc, le mien comme le sien, n'a ni membre log-linéaire, ni
  toutes les coupures, ni pari à fraction.
- **Réglages** : je n'ai joué que les réglages de l'auteur pour ses méthodes (β = 0,025, découpe 100/100, quatre
  moitiés, multiplicateurs jusqu'à 16). La section 8.2 dit pourquoi d'autres β ne changeraient pas le sens.
- **Fluctuation dite** : les 2 500 à 4 000 premiers mondes du cas `tranchant_moitie` portent plus de paris gagnés
  qu'attendu (2,1 à 2,3 écarts-types) ; les 36 000 suivants sont à 4,56 % pour 4,55 % attendus.
- **Aucune référence lue sur PDF** ; Ville, Wasserman, Ramdas et Balakrishnan, Berger et Boos, Grünwald, de Heide et
  Koolen ne sont cités que comme noms de méthodes, **à vérifier sur pièce** ; aucun chiffre n'en vient.
- **Rien n'est adopté, rien n'est proposé au juge.** Les nœuds restent ceux que l'auteur nomme ; j'y ajoute une
  correction (lecture dense : union des instants) et une réserve de lecture (origine du prix).

## 10. Fichiers écrits (même dossier ; chaque fichier a son compagnon `.sha256`)

| fichier | rôle | sha256 |
|---|---|---|
| `attaque_universelle_v1.py` | mon programme d'attaque (taille, puissance, auto-essai) | `704161540cb9c12fb084183161839fcf5de1b0e8b8f93e36a65f311246fda817` |
| `sortie-attaque-universelle-v1.json` | sa sortie (26 parties) | `e678e9a6e802a6d63e23f07a11b5845f97582b1b354a723ee260a627f94d41c7` |
| `rejeu_universelle_v1.py` | rejeu des scripts de l'auteur et comparaison | `d65a08a9d0985b1a5083640cfb974624e5425b2a031a4c4247f3122c2ea91bdb` |
| `sortie-rejeu-universelle-v1.json` | 26 étapes comparées | `0f67c21bb4ef77488062a87cc503e4819c2a8428b672233937ad05ab2c385d63` |
| `sortie-rejeu-cout-universelle-v1.json` | rejeu de son script de coût | `12cdc5d93b5030719205a1de35b1c894847f2ba32bec086b9865d19637c5fff9` |
| `recoupement_universelle_v1.py` | son solveur recoupé par le mien ; son code sous mon attaque | `713e85cad98101f9b4b636dcf7edd80dc318a5a768848affb391aa1247841639` |
| `sortie-recoupement-puissance-universelle-v1.json` | | `d029c73127454c126bcf1508bfe7be5d0cc6f4eb3828a02ccb639ee4b549847e` |
| `sortie-recoupement-taille-universelle-v1.json` | | `0f9dc90981008490e1cab793bd39d4de65edd60ac5d87a4e0e6c8248d6f64213` |
| `sortie-recoupement-tranchant-universelle-v1.json` | | `db8024c5cbdb2dbccccc903336e90b6d39b48ab904f98627accbeaae76eb2b74` |
| `prix_par_morceau_v1.py` | son banc, base du monde changée seule | `a38f8c09582a1cb7f3e0c56c54533b9dc95a3422233491d2ce9f9c4539905942` |
| `sortie-prix-par-morceau-0.25-v1.json` | | `7277fc342f4488203737ab91d2f131c319493149075e70036a9cd097503161d9` |
| `sortie-prix-par-morceau-0.40-v1.json` | | `f2e2ee9ebed85958949c8d1b7c07deb5b8c42bca88345dc0438536d1366c8b11` |
| `sortie-prix-par-morceau-0.55-v1.json` | | `8a6eb31d736ca16fbab07fdebb6c9baea8f31b3856eab524538bd7989ea87e88` |
| `sortie-prix-par-morceau-0.0-v1.json` | | `686668011ded5c60a0a6d5a94d98da44c2a2a6a209b02d5b4198c08e6c61e685` |
| `contre_exemple_lecture_dense_v1.py` | contre-exemple de la section 2 | `21c94abecb1480736016bbceb35d0e0741a746321b1e94eb9aab929c96ce1d7d` |
| `sortie-contre-exemple-lecture-dense-v1.json` | | `b8db1e70a76eaa4fbc8e84430fed728ca2ed42035da588a5b617a9971a1748cc` |
| `piste_instant_par_famille_v1.py` | mesure de la section 8.1 | `4445df5afbae217a4c0cc144358a518ff236d1c1d5d685ff5f37cdb1edcf3c02` |
| `sortie-piste-instant-par-famille-puissance-0.25-v1.json` | | `bf267580b8bd931439c9fcad17e156322f50a38d3c338eeca4413fa2e40234cd` |
| `sortie-piste-instant-par-famille-puissance-0.40-v1.json` | | `c3ffa575ded187e727a121b8cdf1aaff0d4af78c1b026b7aac357087663b0ef9` |
| `sortie-piste-instant-par-famille-puissance-0.55-v1.json` | | `3440b92d1037db071037732082362a7d6fcb014d0e884ce597337f2ec3594d61` |
| `sortie-piste-instant-par-famille-taille-v1.json` | | `e4bbbcacfe9eed0a5db269b1d7da701b52d0494a3aadb87b5b0515a8b91d0700` |

L'empreinte de `attaque_universelle_v1.py` est celle notée au lancement des essais et celle que porte sa sortie
(`empreinte_programme`). Les sorties intermédiaires des rejeux (une par étape) sont restées hors du dépôt ; leurs
empreintes sont dans `sortie-rejeu-universelle-v1.json` (`empreinte_rejeu`).

## Citations obligatoires (N-064, N-067)

POPPER (Huang et al., ICML 2025), `docs/sources/pdf/huang-2025-icml-pmlr-267-popper-automated-hypothesis-validation-agentic-sequential-falsifications.pdf` ;
Dwork et al., arXiv 1506.02629 (2015) ; Blum et Hardt, « The Ladder », arXiv 1502.04585 (2015) ; Co-Scientist (Gottweis
et al., Nature 655, p. 487-496, 2026) ; Qu, Chen et Wang, « Propose, Don't Judge », arXiv 2609.27051 — chemins et
empreintes dans la preuve du nul limité. Aucun PDF relu ici, aucun chiffre repris. Aucune revendication.
