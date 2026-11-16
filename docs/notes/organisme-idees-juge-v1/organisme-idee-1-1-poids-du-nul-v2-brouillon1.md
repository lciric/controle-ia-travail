# Préenregistrement — apprendre les poids du test de référence (« nul ») sans casser sa garantie : projection par blocs, nuls limités et règles de lecture, contre le nul v9, sur le banc B v2 — idée 1.1, version 2, brouillon 1

- Auteur : concepteur neuf, sous-agent de la session mère ; je n'ai écrit ni la version 1, ni sa contre-lecture, ni la preuve,
  ni la synthèse, ni les rendus des cinq angles, ni leurs réfutations, ni le juge, ni les nuls v8 et v9, ni le
  préenregistrement de l'idée 1.2.
- Date (UTC) : 2026-11-15, rédaction de 20:14 à 20:28 (`date -u`) ; dépôt lu sur `main`, tête `4b03f673` ; aucun commit, aucune
  poussée, aucun appel réseau, aucun appel payant.
- Commit du code d'analyse : **aucun à ce jour**. Le code s'écrit après la contre-lecture de ce texte et le scellement de la
  version qui fera foi ; ses empreintes entrent dans un **addendum d'empreintes** scellé avant tout jeu, qui ne change rien
  d'autre.
- Documents qui font foi (chemin + empreinte entière, toutes recalculées le 15 novembre et égales à leurs compagnons) :
  - synthèse de la course de conception : `docs/notes/organisme-idees-juge-v1/correction-poids-v1/synthese-correction-poids-du-nul-v1.md`
    (`48e46c10b163e0cb7d49a7d9c1f09bde2e7c4ac488467739e5b6e8a45c0941b4`) — ci-dessous **[SYN]** ;
  - angle « projection » : `…/correction-poids-v1/projection/methodes-projection-v1.md`
    (`681eb7f5c75b9599ddb7508b575f1824fb126fa781409104e08115d106e51f2e`) — **[PROJ]** ; sa réfutation
    `…/projection/refutation-projection-v1.md` (`7bfaa88eae7485c973ab6d07271324eca4da4b0bf1404aa1e7e2afce00f5d5e4`) — **[R-PROJ]** ;
    programmes cités : `…/projection/essai_projection_commun_v1.py` (`1f4ada977b6cdb96378f3c913df0119bcf6fc333981217ecbbb3583b38f2ca54`),
    `…/projection/essai_projection_methodes_v1.py` (`29704896ec641feff607d42c2636c456e372a2a9f4deb589efd4b8256c8b4105`),
    `…/projection/attaque_projection_v1.py` (`c6161399704d5d6eac1743c364caa08a4f4da9fb2bb2d710b0357235cf8a4257`) ;
  - angle « toute autre voie », réfutation : `…/correction-poids-v1/libre/refutation-libre-v1.md`
    (`8ee42bd6ba74f7326f9f1540db5538bee1373f9a6e6bfa8143ef62ea9f58318b`) — **[R-LIB]** ; angle « inférence universelle »,
    réfutation : `…/correction-poids-v1/universelle/refutation-universelle-v1.md`
    (`f1f03b19f034579ccfa41a360bdc33a7e09d9c48ed456ff375f6b86ba033af84`) — **[R-UNI]** ; angle « ensemble de confiance »,
    réfutation : `…/correction-poids-v1/confiance/refutation-confiance-v1.md`
    (`04028cf3707aef6b74e1bbbcb5bf6ce6c1492b2f405fbf662f3177d1dae81020`) — **[R-CONF]** ; angle « borne de regret », réfutation :
    `…/correction-poids-v1/regret/refutation-regret-v1.md` (`ca3fad0cb6e388818be2af851ed181bf9e21469af62a88c386331aa9185045f4`) — **[R-REG]** ;
  - version 1 de ce préenregistrement, gardée intacte (R12) : `docs/notes/organisme-idees-juge-v1/prereg-nul-par-morceaux-limite-v1.md`
    (`46ef2b92119ee5dff05727b90ca8bdd3ba57b52f9c1c75893750c792a2abc089`) — **[V1]** ; sa contre-lecture
    `docs/notes/organisme-idees-juge-v1/contre-lecture-prereg-nul-limite-et-preuve-v1.md`
    (`763fc6e29cd80868dcdb1d848eafdc928a39fca7244fa16eb0ac721ec705014e`) — **[CL]** ;
  - preuve de validité du nul limité : `docs/notes/organisme-idees-juge-v1/preuve-validite-nul-limite-v1.md`
    (`44f249409193778ccbaaa12b6c5e74d64434dfb87be77382d8bb9438459281b2`) — **[PREUVE]** ;
  - banc B v2, défini par le préenregistrement scellé de l'idée 1.2 :
    `prereg/organisme-idee-1-2-tirages-repartis-arret-anticipe-v4.md`
    (`bdabf2bc9b2c9b78939660f7f7053576a145e165927cafd23e14a798d07d790e`), section « Plan d'analyse », « Banc B v2 » — **[BANC-v2]** ;
    son code déjà au dépôt : `src/controle_ia/organisme_idees_juge/juge_v1.py`
    (`853595cb44260eaaf16bf003f7a7b8155a3785e08c424573fcdaf40a6d1c487e`), `…/lois_v1.py`
    (`bf7e1f3e6cdbbebed681cf115e6d7e8031e670ffb14d82910d707a09f5b0e1fb`) ;
  - nul v9, copie empreintée : `docs/notes/organisme-idees-juge-v1/copie-nul-v9-a41b7b5/orchestrator/pole/nul_v9.py`
    (`7ae450df2482246122bf9fbcf0fa5ef30b4a7e4c6f0d09531e83af048e46ee95`) — **[V9]** ;
  - juge, copie `94bfd92` : liste `docs/notes/organisme-courbe-dose-reponse-v1/code-organisme-94bfd92/empreintes-copie-v1.txt`
    (`0153e02d4522fe21eb1cf52985574eba38b5f260f7a3a08183d63589f29f32df`) ; sous `…/orchestrator/pole/` : `selection_pari.py`
    (`359928110d757cd54cc0d2773910c7360895b68cac5d17e0e4b4e9933ef306bc`), `nul_filles_v2.py`
    (`0ed9b4adbcddc4ad77a1c97d5cbd5706f14926e9c47fe96ce2bab3221a138910`), `nul_v8.py`
    (`cc452aafd17121a7c0ec42829eea47063ffee1f6cdf7f642e264d528f976b888`), `cycle.py`
    (`798f039042e3ee1f18df5c566f5a0ddee5dac5c98225c8ce621e267174c8ee18`), `a_blanc_v59.py`
    (`606aa8b4fcc38786b38cf2954da46533eed9384232a56100d22ff30b8ce0826c`) ;
  - verdict de la validation du v9 : `docs/verdicts/verdict-validation-nul-v9-v1.md`
    (`1407e460367754bb9f76b37174f3a21585970864eb9beaa2699494d90125c1ea`) ; note de la brèche W2 (temps mesurés du v9) :
    `docs/notes/ideation-organisme-v1/breche-w2-v1/note-breche-w2-v1.md`
    (`4d3a6d1c84b8f4790ff9635f974da840ec577c62b31a8cfb1a73ded1440da404`) ;
  - relevé d'idées, § 1.1 : `docs/notes/organisme-conception-propre-v1/relecture-exploratoire-v2/releve-idees-reutilisables-v1.md`
    (`bd253b6c68f6baada0e61b5381f029b52838ca34aa092502e55253c662451c6c`) ; fiches n° 0 (poids ajustés sur une moitié) et n° 14
    (poids appris en ligne) de `sortie--fiches-validees.json` (`a9f9594e2dc3a7a553c54577202817758e3f7ef231445f1a48d500fc647389d5`,
    empreinte reprise de [SYN] § 2 ; fichier non rouvert par moi) ;
  - registre : R-1779 (nœud « accepter le prix du v9 ou chercher un nul moins coûteux »), R-2851 (processeur, sans dépense),
    R-2874 (copie du v9), R-2875 (ligne V5 ; « on n'abandonne pas » les poids appris), R-2881 (banc B v2), R-2924 (synthèse) ;
  - gabarit `prereg/gabarit-preregistrement-v1.md` (`8cad43714b562e28238a92200d6315b1769d8bdf7e9f0a8d72dfe2bc9b37700e`) ;
    validateur `src/controle_ia/prereg.py` (`3b2e3ee56463f30ffd3c549e7fe480fea574c707581bcf30098bf38f4980c306`).

**Statut.** Brouillon 1 de la version 2, **scellé par empreinte seulement (R6), non contre-lu : il ne vaut pas
préenregistrement au sens de R1**. Il le deviendra sous un nom neuf, après contre-lecture par un sous-agent neuf (R2),
corrections, et scellement par `controle_ia.prereg.sceller_prereg`, puis recopie octet pour octet sous `prereg/` (comme
l'idée 1.2, R-2881). **Aucun jeu avant.** Processeur seul, sans dépense (R-2851). Aucun résultat de ce banc n'existe.

**Ce texte n'adopte rien.** Chaque bras neuf est un **candidat** à une version neuve du nul (« v10 ») ou de la règle de
lecture. Le jeu ne branche aucune voie dans le juge. Tout résultat favorable ouvre un nœud : **adopter une voie dans le juge
est réservé à Lazar**, avec sa propre validation scellée.

**Déclaration (R1, R3).** Les prédictions ci-dessous sont écrites **après** lecture des résultats exploratoires de la course de
conception ([SYN]), obtenus sur d'autres bancs, simplifiés, sans le code du v9 ; **sans pilote sur ce banc**. Les chiffres
exploratoires cités servent à placer les prédictions ; aucun n'est un résultat de ce plan.

## Ce qui change de la version 1 à la version 2

| objet | version 1 ([V1]) | version 2 |
|---|---|---|
| question | un nul limité aux coupures de l'archive recouvre-t-il la perte du v9 ? | la même, plus : peut-on **apprendre les poids du nul** sans rétrécir la classe du v9 (projection par blocs), et que rendent deux règles de lecture ? |
| banc | banc B v1 (19 lignes) | banc B v2 de [BANC-v2] (22 lignes, V5 comprise), plus six lignes propres à ce texte (Q8, Q9a, Q9b, Hs, Hm, H7) |
| bras | J8, J9, La, La2, Ld | J8, J9 ; La, Ld ; J9-P ; La-P ; J9-D40, J9-D (et J9-Dc, descriptif) ; témoins A1, A2 ; ligne « carte qui lit l'historique » avec et sans garde. **La2 retiré** (hors des bras recommandés par [SYN] § 6 ; la copie à deux niveaux Q6 reste, comme dent) |
| principale | part recouvrée par La | part regagnée par **J9-P** (classe du v9 gardée) ; La et Ld restent lues, avec leurs seuils de [V1] |
| corrections de [CL] | — | M1 à M4 et m1 à m9 portées (section « Contre-lecture ») |

## Hypothèse

**Contexte.** Le nul v9 ferme le trou « par morceaux » du v8 et le paie en puissance : perte appariée de 0,105 sur la ligne
d'interaction faible I02, borne de Clopper-Pearson unilatérale à 95 % [0,0894 ; 0,1223], au-delà de la marge de 0,05
(verdict `1407e460…`, l. 12 et 31). Le nœud R-1779 demande s'il existe un nul moins coûteux. Les fiches n° 0 et n° 14
proposaient d'**apprendre les poids** du nul sur les tirages ; ces deux façons ne sont pas valides ([PREUVE] § 8 ; [CL] § 4 ;
[SYN] § 5 : la loi devinée ne majore pas la vraisemblance du vrai membre). La course de conception ([SYN] § 1) rend trois
familles de voies valides : (i) la **projection par blocs** — les poids du nul sont calculés à partir de la loi de la carte,
gelés avant chaque bloc de 25 tirages, et la valeur e du bloc est divisée par un certificat exact ([PROJ] § 3, lemmes 1 et 2,
théorème 4) —, valide **seulement si la loi de la carte ne lit pas les issues du bloc jugé** (garde P4, [R-PROJ] § 5) ;
(ii) les **nuls plus petits** (La, Ld), valides sur leur classe seulement ; (iii) deux **règles de lecture** du v9 (40 instants ;
rejet de chaque famille à son propre instant, [R-LIB] § 10, [R-UNI] § 8.1).

**H-1.1 v2 (principale).** Sur le banc B v2, avec le **code original du v9** et **tous les membres du v8 gardés dans tous les
bras** (membres ordinaires et log-linéaires compris), la projection par blocs sur la classe du v9 (bras **J9-P**) **regagne au
moins un quart** de la puissance que le v9 perd contre le v8 sur de vraies découvertes, **sans rouvrir aucune copie de la
classe du v9** et en gardant sa taille α.

**Sous-hypothèses de travail** (chacune lue à part) :
- **H-a (garantie).** Chaque bras garde une taille au plus α sur sa classe : J8, J9, La, Ld par [PREUVE], théorème 1 ; J9-P et
  La-P par [PROJ], théorème 4, sous la garde P4 ; J9-D40 et J9-D par l'inégalité de Ville ([R-LIB] § 10 ; [R-UNI] § 8.1).
- **H-b (prix du v9 sur ce banc).** Le v9 perd de la puissance contre le v8 sur une partie des lignes de vraies découvertes.
- **H-c (question de départ).** Un nul limité aux coupures de l'archive (La) recouvre au moins la moitié de cette perte ; il le
  paie en laissant passer les copies coupées ailleurs. Ld (La plus sous-population et signe de chaque trait) recouvre moins.
- **H-d (projection à classe égale).** La projection gagne sur sa référence de même classe : J9-P sur J9, La-P sur La.
- **H-e (règles de lecture).** Lire le v9 à 40 instants et rejeter chaque famille à son propre instant ne fait jamais perdre une
  promotion (par construction) et en gagne peu.
- **H-f (garde P4).** Sans la garde, une carte qui lit l'historique du bloc fausse la taille de J9-P ; avec elle, non.

**Renvois.** Organisme d'idéation, second terrain du papier C et atelier d'idées (N-065) ; clause de N-067 sur le juge au nul
formé des lois connues ; nœud R-1779. **Aucune revendication n'est faite ici.**

## Garantie de chaque bras, et ce qu'elle ne couvre pas

- **J8, J9, La, Ld** : maximum de vraisemblance certifié sur les tirages mêmes ; [PREUVE], théorème 1, avec les corrections p1 à
  p6 de [CL] § 2.2 (tolérance du code 10⁻³ nat ; instants ; pari plein ; e-BH ; La2 ; statut). Sous le pari plein, une carte
  membre de la classe a W_t ≤ 1 à chaque instant.
- **J9-P, La-P** : produit de valeurs e de blocs ([PROJ] § 3). Hypothèses P1 à P6 de [PROJ] ; **P4 n'est pas acquise au pari
  plein** dans la grammaire du juge ([R-PROJ] § 5 : `selection_pari.TYPES_LISANT_L_HISTORIQUE` = « sans_remise »,
  « moyenne_glissante »). La richesse est une surmartingale **aux fins de bloc** seulement ; les blocs sont les intervalles
  entre les huit instants du juge. Une carte membre reste « près de 1 », plus « au plus 1 » ([R-PROJ] § 4.3 et § 9, point 3).
- **J9-D40** : la même valeur e que J9, lue tous les 5 tirages ; valide par Ville sur tous les instants ([PREUVE], pas 4 ;
  [CL] p2). Sa valeur arrêtée reste une valeur e.
- **J9-D** : chaque famille du nul doit être rejetée à au moins un instant lu, pas forcément le même. Valide comme test de
  niveau α **pour la carte seule** ([R-UNI] § 8.1, preuve en trois lignes). **Ce n'est pas une valeur e** : le bras **ne se
  branche pas tel quel sur la règle e-BH** du juge ; ce branchement serait un nœud à part, non traité ici.
- **Réserves communes.** Mondes sans mémoire seulement ; réserve log-linéaire du v8 héritée ([PREUVE], H4) ; la preuve du rejet
  par famille n'est pas contre-lue par un tiers ([SYN] § 7) ; les lemmes de [PROJ] ont été suivis par le réfutateur et par le
  rédacteur de [SYN], mais **aucune pièce « preuve, version 2 » n'est scellée** : préalable 2. Références de méthode non relues
  sur PDF, aucun chiffre n'en est tiré (R7) : inégalité de Ville ; inférence universelle ; numéraire et projection
  d'information inverse ; « Safe testing » ; règle e-BH ([SYN] § 7, liste entière).

## Prédiction chiffrée et signe attendu

Cellule = (ligne, bras) ; taux = part des 1 000 répétitions où la carte seule est promue. Bras et lignes : « Plan d'analyse ».
ρ_X : part regagnée par le bras X (« Métrique »).

| # | prédiction | signe | chiffre | ce qui la réfute | confiance |
|---|---|---|---|---|---|
| P1 | cellules fatales (carte membre exact de la classe d'un bras à maximum : 34 cellules) | nul | 0 promotion sur 1 000 ; log W maximal ≤ 10⁻⁶ | une seule promotion, ou un log W > 10⁻⁶ (défaut de code ou de certificat) | 0,97 |
| P2 | cellules de taille et copies des bras à projection (31 cellules ; pire cas Q8 compris) | sous α | taux ≤ 0,03 dans chaque cellule ; toutes « tenues » | une cellule « non tenue » (Holm) | 0,8 |
| P3 | dents : J8 promeut les copies Q2 à Q5 ; J9 et J9-P promeuvent la copie à deux niveaux Q6 ; A1 et A2 promeuvent les copies Q1 et Q2 | + | J8 ≥ 0,90 ; J9 ≥ 0,80 sur Q6 ; J9-P ≥ 0,60 sur Q6 (rapporté, sans seuil : même trou que le v9) ; A1 ≥ 0,90 ; A2 ≥ 0,30 | une borne basse sous son seuil (« Seuil ») ; pour J9-P sur Q6, un taux < 0,5 | 0,75 |
| P4 | copies rouvertes par les nuls limités : La et La-P promeuvent Q3, Q4, Q5 ; Ld promeut Q5 | + | La et La-P ≥ 0,85 ; Ld ≥ 0,60 | La ou La-P < 0,5 sur Q3 ou Q4 (à auditer) | 0,7 |
| P5 | prix du v9 sur ce banc : lignes V informatives | J9 < J8 | au moins 4 des 15 lignes V ; 2 ou 3 : prédiction « partielle » | moins de 2 | 0,65 |
| P6 | **principale** : part regagnée par J9-P | + | estimation ponctuelle de ρ_J9-P dans [0,25 ; 0,60] ; « regagne » (borne basse ≥ 0,25) | borne haute < 0,10 (« ne regagne pas ») | 0,45 pour « regagne » ; 0,8 pour une estimation > 0,10 |
| P7 | part recouvrée par La | + | borne basse de ρ_La ≥ 0,5 (ponctuelle 0,6 à 0,9) ; sur les lignes V5 informatives, La recouvre au plus 0,3 | borne haute < 0,25 | 0,55 |
| P8 | part recouvrée par Ld | + | ρ_Ld ≤ ρ_La **par construction** ; ponctuelle dans [0,35 ; 0,80] | borne haute < 0,25 | 0,5 |
| P9 | La-P contre La, même classe, lignes informatives réunies | + | gain apparié réuni de + 0,02 à + 0,10 | borne haute du gain réuni < 0 | 0,55 |
| P10 | J9-D contre J9 (jamais négatif, par construction) ; J9-D40 seul | + faible | gain réuni sur les lignes V : J9-D de + 0,010 à + 0,040 ; J9-D40 de + 0,005 à + 0,025 | gain réuni de J9-D < 0,005 | 0,6 |
| P11 | J9-P contre La, lignes informatives réunies | − ou 0 | écart réuni dans [− 0,11 ; + 0,03] | borne basse > 0 (bonne nouvelle : la classe du v9 sans prix) | 0,6 |
| P12 | garde P4 : carte hors grammaire H7 sans garde ; avec garde par gel de l'historique ; cartes de la grammaire Hs et Hm sans garde | + ; sous α ; sous α | H7 sans garde ≥ 0,20 ; avec gel ≤ 0,02 sur les trois lignes ; Hs et Hm sans garde < 0,05 | H7 sans garde : borne basse ≤ 0,05 (la garde n'est pas éprouvée) ; gel : cellule « non tenue » ; Hs ou Hm : borne basse > 0,05 (le trou est atteint par une carte de la grammaire) | 0,6 |
| P13 | protection d'une carte membre quand le monde est hors du nul (Q9a, Q9b) | nul | 0 promotion dans tous les bras ; pour J9-P et La-P, log W maximal ≤ 0,5 | une promotion (bras à maximum : défaut ; bras à projection : protection perdue) | 0,8 |
| P14 | écart du certificat du v9 : sensibilité J9⁺ | nul | J9 et J9⁺ diffèrent sur moins de 0,5 % des répétitions des lignes V ; le verdict de P6 est le même avec J9⁺ | verdict de P6 différent avec J9⁺ | 0,85 |

**D'où viennent ces chiffres** (exploratoires, autres bancs ; [SYN] § 4 et § 7) : gain de la projection à classe égale + 0,045 à
+ 0,185, part regagnée 0,41 à 0,82, **sans** membres log-linéaires, sur 100 à 200 mondes par dose ([PROJ] § 6) ; le gain de La
tombe d'un tiers à la moitié quand on garde les membres log-linéaires ([R-LIB] § 8) : d'où un intervalle prédit plus bas pour
J9-P ; lecture dense et rejet par famille + 0,020 à + 0,032 ([R-LIB] § 10) ; pire cas de la projection 35/2 120 ([R-PROJ]
§ 4.3) ; carte qui lit l'historique 904/2 000 pour le membre linéaire seul et 18/60 pour toutes les coupures ([R-PROJ] § 5) ;
J8 sur les copies : 0,986 et 0,972 dans la validation du v9 ([CL] § 1, audit `9086a420…`).

**Ce que serait chaque issue (R3).** P6 vraie : un candidat v10 existe **dans la classe du v9**, sous la garde P4 (meilleur
cas). P6 fausse et P7 vraie : un nul moins coûteux n'existe sur ce banc qu'en rétrécissant la classe (question de sens,
R-1768, R-1779). P6 et P7 fausses : le prix du v9 n'est repris par aucune voie de cette famille ; il reste « accepter le prix »
et, au mieux, les règles de lecture (P10). P5 fausse : le prix du v9 ne se reproduit pas sur ce banc, rien ne se lit sur la
principale. P12 fausse sur H7 : le banc ne montre pas le défaut que la garde corrige. P12 fausse sur Hs ou Hm : la garde est
nécessaire dès la grammaire actuelle. P1, P2 ou P13 (bras à maximum) fausses : défaut de code ou de preuve.

## Métrique

- **Promotion d'une carte seule** (bras à huit instants) : il existe t ∈ T₈ = {25, 50, …, 200} avec log W_t ≥ log(1/α),
  α = 0,05 (règle de `nul_filles_v2.evaluer_v2`, sans marge des filles : cartes fraîches). Bras à 40 instants : « Bras ».
- **Taux d'une cellule** : promotions / 1 000 ; intervalle de Clopper-Pearson, bilatéral à 95 % pour le rapport, unilatéral à
  95 % pour les seuils.
- **Perte appariée du v9 sur une ligne ℓ** : δ₉(ℓ) = (1/R)·Σ_r (a_r − b_r), a_r = 1[J8 promeut], b_r = 1[J9 promeut]. Par
  monotonie ([PREUVE] § 6 (a)), b_r ≤ a_r.
- **Gain apparié d'un bras X sur un bras Y** : Δ_{X,Y}(ℓ) = (1/R)·Σ_r (x_r − y_r) ; test exact de McNemar par ligne (rapport).
  Δ_X = Δ_{X,J9}. **Gain réuni** sur un ensemble de lignes : moyenne des Δ(ℓ), lignes à poids égaux.
- **Ligne informative** : borne basse unilatérale à 95 % de δ₉(ℓ) ≥ 0,02, soit au moins 29 paires discordantes sur 1 000
  (annexe A). L'ensemble I est fixé par J8 et J9 seuls.
- **Part regagnée** : ρ_X = Σ_{ℓ ∈ I} Δ_X(ℓ) / Σ_{ℓ ∈ I} δ₉(ℓ), **V5 comprise** ([CL] M1). Intervalle par rééchantillonnage des
  répétitions dans chaque ligne (vecteurs appariés de tous les bras), 10 000 rééchantillons ; **I est recalculé dans chaque
  rééchantillon** ([CL] m4) ; un rééchantillon à moins de 2 lignes informatives est écarté et compté. Trois bras primaires
  (J9-P, La, Ld) : quantiles 0,833 % et 99,167 % (Bonferroni). Rapportée aussi par strate : « structure sur une partition du
  bras » et « structure hors des partitions du bras » ([CL] M1).
- **Décomposition du prix du v9** (descriptive) : 1 − ρ_La = part du prix déjà payée en passant de J8 à La (poids libres par
  morceau sur deux partitions fixées) ; ρ_La − ρ_Ld = part des trois partitions déclarées ; ρ_Ld = part de la recherche sur
  tous les seuils. Avec les intervalles du rééchantillonnage.
- **Promotions de copies** (fausses ou non selon la question de sens, ouverte : R-1768, R-1779 ; [CL] m3) : taux des cellules
  Q2 à Q6 pour les bras dont la classe ne contient pas le monde.
- **Sensibilité J9⁺** : promotions recalculées quand la valeur certifiée de chaque membre par morceaux est remplacée par sa
  meilleure valeur **atteinte** (`detail_morceaux_groupe`, champ `atteinte`). Le vrai maximum est entre les deux : la richesse
  d'un v9 exact est entre celle de J9 et celle de J9⁺. Tout gain d'un bras est rapporté contre J9 **et** contre J9⁺.
- **Journal de la projection** (J9-P, La-P), par répétition : plus grand et médian c − 1 des certificats de bloc ; coût total
  Σ 25·log max(1, c) du processus retenu ; empreinte du tableau des poids projetés. Journal entier pour les 20 premières
  répétitions de chaque ligne.
- **Mesures descriptives** (aucun critère) : log W maximal et médian par cellule ; membre ou famille qui décide (minimum) ;
  `ecart_residuel` des membres par morceaux ; temps par évaluation ; strate « sans membres log-linéaires » (ci-dessous).
- Aucune moyenne ni médiane sur des jetons : il n'y en a pas ici.

## Seuil

- **Niveau du juge** : α = 0,05 ; n = 200 tirages frais ; marginale d'entraînement sur 100 instances (comme
  `a_blanc_v59.juger_carte`).
- **Cellules de taille** (53, comptées au « Plan d'analyse ») : test binomial exact, procédure de Holm au niveau 0,05 sur la
  famille des 53, dans chaque sens. « Tenue » si H₀ « taux ≥ α » est rejeté ; « non tenue » si H₀ « taux ≤ α » est rejeté ;
  sinon « non jugeable ». Au pas le plus strict (0,05/53) : tenue si ≤ 29 sur 1 000, non tenue si ≥ 74 ; au pas le moins
  strict : ≤ 38 et ≥ 63 (annexe A).
- **Cellules fatales** (34) : **toute** promotion, ou tout log W > 10⁻⁶, déclenche l'audit (une carte membre ne peut pas être
  promue par un bras à maximum, sous le pari plein). L'engagement de chaque bras est sans `fractions` (vérifié par un essai,
  [CL] m8).
- **Copies des bras à projection** (7 cellules, dans la famille des 53) : en plus, **seuil d'audit écrit** : log W maximal d'une
  carte membre ≤ 1,0 nat ; au-dessus, audit de l'optimiseur (pas un « trou » : la validité ne dépend pas de ce seuil).
- **Dents** : borne basse de Clopper-Pearson unilatérale à 95 % **> 0,5** (au moins 527 sur 1 000) pour J8 sur Q2, Q3, Q4, Q5,
  pour J9 sur Q6 et pour A1 sur Q1 et Q2 ; **> 0,05** (au moins 63 sur 1 000) pour A2 sur Q1 et Q2 et pour J9-P sans garde sur
  H7 ([SYN] § 6, point 6 ; annexe A).
- **Principale (J9-P)**, lue dans cet ordre, la première vraie l'emporte : 1. **« nuisible »** si la borne haute de ρ_J9-P
  < 0 ; 2. **« regagne »** si la borne basse ≥ 0,25 ; 3. **« ne regagne pas »** si la borne haute < 0,10 ; 4. sinon
  **« partiel »**. Au moins 2 lignes informatives sont exigées (sinon « sans objet »). Le seuil d'un quart est un jugement
  gelé : en dessous, le gain ne paierait pas ce que la voie change au juge (garde P4, optimiseur dans le résultat, audit
  « près de 1 »).
- **La, Ld** (seuils de [V1]) : « recouvre » si la borne basse de ρ_X ≥ 0,5 ; « ne recouvre pas » si la borne haute < 0,25 ;
  sinon « en partie ».
- **Secondaires**, intervalle percentile bilatéral à 95 % du gain réuni sur les lignes informatives, sans correction : La-P
  contre La ; J9-P contre La ; J9-D et J9-D40 contre J9 (sur les 15 lignes V). « Gain » si la borne basse > 0.
- **Garde P4** : « nécessaire, montrée » si J9-P sans garde passe la dent sur H7 **et** si J9-P avec gel est « tenu » sur Hs,
  Hm et H7. « Trou atteint par la grammaire » si la borne basse de J9-P sans garde dépasse 0,05 sur Hs ou sur Hm.
- **Tolérances numériques** : constantes du code du v9 inchangées (`TOLERANCE_GROUPE` = 10⁻³ nat, `PALIERS_MU`,
  `PAS_MAX_PAR_PALIER` ; [CL] M4) ; nichage vérifié à l'écart résiduel du membre + 10⁻⁶ nat ; monotonie à 10⁻⁶ nat.

## Plan d'analyse

### Banc

**Le banc B v2 de [BANC-v2], repris tel quel** pour l'espace (3 issues, 2 traits, 2 sous-populations), les instances, les lois
softmax aléatoires, l'archive A2 (S1, S2 softmax ; S3, S4 `si_sinon` sur les coupures de l'archive, |s| ≥ 0,3), les 22 lignes
Q1 à Q7 et V1 à V5 à trois doses, et le gel des engagements **avant** les issues fraîches. Ce que [BANC-v2] ne répète pas
(C_decl = {sous-population ; z₀ > 0 ; z₁ > 0}, archive A0 = {S1, S2}, colonne « classes qui contiennent M ») reste celui de
[V1], « Banc B ». Le code des lois est celui de `lois_v1.py` ; l'accès au juge celui de `juge_v1.py` (vérification des
empreintes de la copie avant tout import).

**Proximité avec le vrai juge** (désaccord 8, plus bas). J8 est calculé par le code du juge de la copie `94bfd92`
(`nul_filles_v2.evaluer_v2`, `nul_v8.membres_archive_v8`). J9 par le **code original** [V9] : bibliothèque =
`BIBLIOTHEQUE_STANDARD` + marginale d'entraînement + `nul_v9.membres_archive_v9(archive, None, 3, 2)` ; engagement par
`nf.construire_engagement_v2("fiche", loi, instances, 3, 0,05, bibliothèque, 0, None, instants, plan_execution="ordre_naturel")` ;
évaluation par `nul_v9.evaluer_v9` ([CL] M2). **Aucune grille de seuils ne remplace le v9** : toutes les coupures réelles sont
parcourues par son code. Les membres ordinaires et log-linéaires du v8 sont dans **tous** les bras ([SYN] § 6, point 2).
[V9] est chargé comme module `pole.nul_v9` au-dessus du paquet `pole` de la copie `94bfd92` (préalable 1).

**Lignes ajoutées par ce texte** (propres à l'idée 1.1 ; elles ne changent rien au banc partagé) :

| ligne | monde M | carte Q | rôle |
|---|---|---|---|
| Q8 pire cas de la projection | la projection d'information inverse de Q sur la famille linéaire de l'archive, calculée sur les 200 instances du plan (600 pas, comme `projection_globale` de `attaque_projection_v1.py`), écrite en `melange`([S1, S2, S3, S4, loi fixe], poids arrondis à six décimales et renormalisés) : membre de toutes les classes | softmax(W1 + 0,6·Δ, b1), Δ ~ N(0, 1) centrée par colonne (forme de V1, dose 0,6) | taille, là où la valeur e de bloc est serrée ([R-PROJ] § 4.3) |
| Q9a carte membre, monde hors du nul | monde de V1(0,50) | S1 | protection d'une carte membre (désaccord 9) |
| Q9b carte membre, monde hors du nul | monde de V1(0,50) | `melange` des lois de l'archive, poids de Dirichlet(1, …, 1) | idem |
| Hs carte de la grammaire qui lit l'historique | loi uniforme (`fixe`) | `sans_remise`, composition [70, 70, 70] | garde P4, réglage 0 de [R-PROJ] § 5 |
| Hm mélange de la grammaire qui lit l'historique | `melange`([S1, S2], [0,5 ; 0,5]) | `melange`([M, `sans_remise` [70, 70, 70]], [0,5 ; 0,5]) | garde P4, réglage 4 |
| H7 carte écrite pour l'attaque, **hors grammaire** | `melange`([S1, S2], [0,5 ; 0,5]) | q_s(y) ∝ M_s(y)·exp(− 0,3·(nombre de y déjà vus dans le bloc − nombre attendu sous M)), plancher 10⁻¹², renormalisée (`carte_a_memoire`, genre « contre_exces_du_bloc », de `attaque_projection_v1.py`) | garde P4, réglage 7 ; témoin de code |

Q8 dépend du plan : la preuve est conditionnelle au plan, c'est le pire cas ; un monde réel ne le peut pas (dit). H7 ne passe
pas par `valider_loi` : elle n'est jugée que par le module de projection et par le rapport exact au monde ; **je n'ai pas
vérifié qu'elle s'écrit dans la grammaire** ([R-PROJ] § 5, limite (iii)).

**28 lignes × 1 000 répétitions.**

### Bras (mêmes plans, mêmes issues fraîches pour tous)

1. **J8** et **J9** — références, définies ci-dessus. **J9⁺** n'est pas un bras : c'est la lecture de sensibilité de la
   « Métrique ».
2. **La** et **Ld** — nuls limités de [PREUVE] § 3 : La = v8 plus les deux partitions à seuil **fixé** de l'archive ; Ld = La
   plus la sous-population et le signe de chaque trait. Module du v9 **copié sous un nom neuf** (R12), avec **quatre
   changements déclarés, et eux seuls** ([CL] M2) : (1) un type de partition « seuil_fixe » ajouté à `_coupes` (une seule
   coupe {z ≤ s} | {z > s}) ; (2) `membres_morceaux` prend la liste des partitions en paramètre ; (3) la garde
   `exiger_membres_v9` vérifie cette liste ; (4) noms des membres. Solveur, constantes et `evaluer_sur_issues` inchangés, octet
   pour octet (différentiel joint à l'addendum). Par construction : W^La ≤ W^J8 ; log W^La ≥ log W^J9 − écart résiduel ;
   W^Ld ≤ W^La à l'écart résiduel près ([CL] p5, M3).
3. **J9-P — projection par blocs sur la classe du v9** (M3 de [PROJ] § 4). Module neuf.
   - *Richesse.* log W_t = min( log W^reste_t ; min_{F ∈ 𝔽₉} Σ_{b ≤ t/25} log e_{F,b} ), t ∈ T₈. W^reste : la richesse du juge
     sur la bibliothèque du v9 **privée** des membres de type `ajuste_lineaire` et `ajuste_morceaux` (membres ordinaires et
     log-linéaires, calculés par le code du juge, inchangé). 𝔽₉ : la famille linéaire de l'archive ; la sous-population ;
     pour chaque trait j et chaque valeur distincte c de z_j **sur les 200 instances du plan gelé**, la coupure {z_j ≤ c} |
     {z_j > c} — au plus 402 familles, liste fixée par le plan, avant les tirages.
   - *Valeur e d'un bloc.* Blocs B_1 à B_8 = les huit intervalles de 25 instances entre instants du juge. Pour la famille F et
     le bloc b : φ = poids projetés ; r_s(y) = q_s(y) / P_φ(y | x_s) ; **certificat** c = max sur les sommets v de F (une loi
     connue par cellule et bruit nul, ou une loi certaine commune) de (1/25)·Σ_{s ∈ B} Σ_y P_v(y | x_s)·r_s(y), calculé
     exactement ; e_{F,b} = Π_{s ∈ B} r_s(y_s) / max(1, c)²⁵. **Pari plein seulement** (un engagement avec `fractions` est
     refusé).
   - *Optimiseur gelé.* Espérance-maximisation pondérée par q_s(y), paramétrage et accélération avec garde de `em_commun`
     (`essai_projection_commun_v1.py`, `1f4ada97…`). Projection sans coupure du bloc : départ au centre, **300 pas** ;
     projection de chacune des 26 partitions qu'une coupure induit dans un bloc : départ depuis la projection sans coupure du
     même bloc, **150 pas** (`IT_PROJ`, `IT_CHAUD` de `essai_projection_methodes_v1.py`, `29704896…`). Aucun autre critère
     d'arrêt ; double précision ; nombres de pas sous l'empreinte de l'addendum. Tout autre réglage est un écart.
   - *Gel et journal.* Pour une carte sans mémoire, **toutes** les projections et tous les certificats sont calculés au gel,
     avant le tirage des issues fraîches ; l'empreinte du journal est écrite dans l'enregistrement de la répétition avant que
     le générateur des issues fraîches soit créé (garde de code). Le module de projection ne reçoit jamais une issue du bloc
     qu'il projette (garde d'accès).
   - *Garde P4*, deux formes, toutes deux jouées sur Hs, Hm, H7 : **refus** — au gel, toute carte dont
     `selection_pari.types_de_la_loi(loi)` rencontre `TYPES_LISANT_L_HISTORIQUE` est refusée par le bras (comptée « refusée »,
     non promue) ; **gel de l'historique** — la loi de la carte est évaluée, au numérateur comme dans la projection, avec
     l'historique arrêté au début du bloc (ce qui change ce que la carte parie ; projections calculées au début de chaque
     bloc, sur les seules issues des blocs passés). **J9-P sans garde** (« J9-P-nu ») n'est joué que sur ces trois lignes :
     projection et certificat calculés sur les lois que la carte a réalisées. Sur les 25 autres lignes, les cartes sont sans
     mémoire : la garde accepte tout et les trois formes coïncident (essai sain).
   - *Marge des filles* : laissée au maximum de vraisemblance ; hors de ce banc (cartes fraîches, pas de `delta0`).
4. **La-P — projection de La** (M2b) : comme J9-P, avec 𝔽 = {famille linéaire ; coupure A de l'archive ; coupure B}. Même
   classe que La. Sépare ce que rend la projection de ce que rend la restriction de classe.
5. **J9-D40** et **J9-D** — règles de lecture du v9, même classe, même dénominateur. Un **engagement jumeau** à 40 instants
   T₄₀ = {5, 10, …, 200} (T₈ ⊂ T₄₀), même plan, mêmes issues, évalué par le code du v9.
   - **J9-D40** promeut si J9 promeut, **ou** s'il existe t ∈ T₄₀ avec log W_t ≥ log(1/α).
   - **J9-D** promeut si J9-D40 promeut, **ou** si, pour **chaque** membre m de la bibliothèque (membres ordinaires par
     `selection_pari.trajectoires`, membres ajustés par `nul_v9.valeurs_ajustees_v9`), il existe un instant t_m ∈ T₄₀ avec
     log q(y_1..t_m) − V_m(t_m) ≥ log(1/α). « Famille » = membre nommé de la bibliothèque : c'est la règle telle que le code
     du juge peut la lire **sans rien changer au v9**. La réunion des trois événements reste dans l'événement de Ville du
     monde : le niveau α est gardé, et « J9 promeut ⇒ J9-D40 promeut ⇒ J9-D promeut » vaut par construction.
   - **J9-Dc** (descriptif, aucun critère) : la même règle, famille par famille au sens fin — une famille par seuil réel,
     c'est-à-dire par coupure du plan gelé. Elle demande une copie renommée de `detail_morceaux_groupe` qui rend le certificat
     de **chaque** coupe (changement déclaré, différentiel lu par le contre-lecteur du code) ; s'il n'est pas jugé sûr, J9-Dc
     est retiré et le retrait est rapporté.
   - **Rappel** : J9-D et J9-Dc ne sont pas des valeurs e et **ne se branchent pas tels quels sur la règle e-BH**.
6. **Témoins** (dents du banc, sans verdict sur le juge ; R5) :
   - **A1** — fiche n° 14 sans correction : poids par cellule (quatre cellules des deux coupures de l'archive ; lois connues et
     lois certaines), descente exponentielle de pas 0,05 après chaque tirage, dénominateur = loi prédictive courante
     (`a1_en_ligne`) ; richesse = numérateur de la carte sur ce seul dénominateur.
   - **A2** — fiche n° 0 sans correction : poids ajustés au maximum de vraisemblance sur les tirages 1 à 100 (300 pas), rapport
     sur les tirages 101 à 200, lu à 200 (`a2_moitie`).
   - A1 et A2 sont lus sur Q1 et Q2 (copies exactes d'un membre de leur famille) ; rapportés sur les autres lignes.
   - **Ligne « carte qui lit l'historique »** : Hs, Hm, H7, par J9-P-nu, J9-P avec refus, J9-P avec gel, et, sur Hs et Hm,
     par J9, J9-D40 et J9-D (valides pour une carte prévisible, [PREUVE] H5). Témoin exact : le rapport de vraisemblance de la
     carte au monde, lu aux mêmes instants.
7. **Strate descriptive « sans membres log-linéaires »** : J8, J9, La et J9-P rejoués sans les membres `ajuste_log`, sur les 250
   premières répétitions des 15 lignes V. Sert seulement à situer ce banc par rapport aux chiffres exploratoires. Aucun critère.

**Bras non joués** : ceux de [SYN] § 6 (« bras à ne pas jouer »), pour les raisons qui y sont écrites ; et La2.

### Cellules (comptes)

Classe de chaque bras : J8 — v8 ; J9, J9-P, J9-D40, J9-D — v9 ; La, La-P — v8 plus les deux coupures de l'archive ; Ld — La
plus les partitions déclarées.

| ligne | monde dans la classe de | cellules fatales (bras à maximum, carte membre) | copies (bras à projection) | cellules de taille (carte hors classe) |
|---|---|---|---|---|
| Q1 | tous | 6 | 2 | — |
| Q2 | tous sauf J8 | 5 | 2 | — |
| Q3, Q4 | J9, Ld, J9-P, J9-D40, J9-D | 4 + 4 | 1 + 1 | — |
| Q5 | J9, J9-P, J9-D40, J9-D | 3 | 1 | — |
| Q7 | tous sauf J8 | — | — | 7 |
| Q8 | tous | — | — | 8 |
| Hs, Hm | J9, J9-D40, J9-D, J9-P avec gel | — | — | 4 + 4 |
| H7 | J9-P avec gel | — | — | 1 |
| Q9a, Q9b | aucun (monde hors du nul) | 6 + 6, **hors de la famille de Holm** | 2 + 2, rapportées | — |

Famille de Holm : 22 + 7 + 24 = **53 cellules**. Cellules fatales : 22 + 12 = **34**. Prédiction P2 : 7 + 24 = 31 cellules.

### Répétitions, appariement, ordre du gel

R = 1 000 par ligne. À chaque répétition : le banc tire l'archive, les paramètres de la ligne, 100 instances d'entraînement et
leurs issues, le plan de 200 instances ; **tous les bras construisent et gèlent** leur engagement (et, pour les bras à
projection, leur journal) ; **ensuite seulement** les 200 issues fraîches sont tirées du monde, d'un générateur distinct ; la
fonction qui bâtit un engagement ne reçoit aucune issue fraîche ([CL] m1). Chaque bras reçoit les mêmes issues, dans un
dictionnaire lié à **son** empreinte (montage de [V1], annexe B). Les mondes du banc ne lisent pas l'historique.

### Graines (R9)

Racine : l'entier de l'empreinte sha256 du texte qui fera foi. `numpy.random.default_rng(numpy.random.SeedSequence(entropy=racine,
spawn_key=…))`, numpy ≥ 1.25 : tout ce qui précède le gel `(i_ligne, r, 0)` ; issues fraîches `(i_ligne, r, 1)` ; essai
d'égalité E0 `(98, r)` ; rééchantillonnage `(99, b)` ; essais et mutations `(97, k)`. i_ligne de 0 à 27 dans l'ordre : Q1 à Q7,
V1 à V5 (dose croissante), Q8, Q9a, Q9b, Hs, Hm, H7. Manifeste du run (`src/controle_ia/manifeste.py`) : configuration et
empreinte, versions de Python, numpy et scipy, graines, commit, empreintes des fichiers gelés.

### Étapes

0. **Préalables et gel.** Préalables 1 et 2 levés (« Écarts, nœuds… »). Code écrit sous des noms neufs dans
   `src/controle_ia/organisme_idees_juge/` : nul limité, projection par blocs, lecture dense, témoins, banc, lecture gelée (la
   table des critères écrite en code). Essais : **cas sain et artefact pour chaque ligne de la liste d'arrêt et pour la garde
   P4** (R5). Banc de mutations, au moins : certificat de bloc retiré, optimiseur réduit à 3 pas (doit faire promouvoir Q8 ou
   une copie) ; projection calculée sur les issues du bloc ; garde P4 retirée (tuée par H7) ; blocs décalés des instants ;
   minimum sur les familles remplacé par un maximum ; W^reste oublié ; famille linéaire oubliée ; coupures de l'archive
   calculées sur les issues fraîches ; tirages différents d'un bras à l'autre ; issues fraîches tirées avant le gel ; rejet par
   famille lu à un instant hors de T₄₀ ; J9-D sans la réunion avec J9 ; seuil d'informativité choisi sur un bras neuf ; mauvais
   bras au numérateur de ρ ; I gardé fixe dans le rééchantillonnage. Toutes tuées pour la raison attendue. Contre-lecture du
   code par un sous-agent neuf. **Addendum d'empreintes** scellé.
1. **Contrôles avant jeu** : empreintes conformes ; essais et mutations rejoués ; aucune sortie existante.
2. **Essais d'égalité**, non lus au-delà : **E0** (100 répétitions, archive A0, ligne Q1) : La ≡ J8 à 10⁻¹² nat ; **E9** : J9
   sans ses membres par morceaux (`nul_v9.sans_morceaux`) ≡ J8, valeur pour valeur ; **EP** : sur 50 mondes, le module de
   projection réduit aux familles linéaires en leurs poids reproduit `m3_toutes_coupures` à 10⁻⁹ nat ; **ED** : aux huit
   instants de T₈, la trajectoire de l'engagement jumeau s'écarte de celle de J9 d'au plus 2·10⁻³ nat (deux appels du
   solveur, tolérance 10⁻³ chacun). Un essai manqué arrête tout.
3. **Jeu** : 28 lignes × 1 000 répétitions, `nice -n 10`, deux processus au plus ; gardes actives à chaque évaluation.
4. **Scellement de la sortie** avant toute lecture ; sortie sous `diag/organisme-idees-juge-v1/`.
5. **Lecture** : lecture gelée, puis lecteur neuf (R13) qui recalcule l'issue de façon indépendante ; audit de symétrie (R4)
   écrit avant le prononcé.
6. **Rapport** à la mère : issue, réserves, nœud. **Aucune adoption.**

### Comparaisons et corrections

Taille : Holm sur 53 cellules. Trois bras primaires (J9-P, La, Ld) : intervalles de ρ ajustés de Bonferroni. Secondaires et
lignes par lignes : rapportés sans correction ; aucun verdict d'adoption ne peut s'appuyer sur un secondaire seul. Contrôles
appariés : toutes les comparaisons sont sur les mêmes issues.

## Les neuf désaccords de la synthèse

[SYN] § 7 numérote huit désaccords ; l'« avertissement transversal » écrit dans le deuxième fait le neuvième (c'est le compte
de R-2924). Numérotation ci-dessous : celle à neuf ; entre parenthèses, le numéro dans [SYN].

| n° | désaccord | traitement | où |
|---|---|---|---|
| 1 (1) | garde P4 : « vraie au pari plein » ou fausse pour la grammaire du juge | **tranché par une mesure** : lignes Hs, Hm, H7, sans garde et avec les deux formes de garde. **Réserve** : H7 est hors grammaire, non vérifiée comme écrivable ; un résultat nul sur Hs et Hm ne montre pas qu'aucune carte de la grammaire n'atteint le trou ; le gabarit des proposeurs de la boucle réelle n'est pas examiné | P12 ; Seuil ; étage 7 |
| 2 (2) | gain de l'ensemble de confiance coupé sur l'entraînement : 14 %, 42 %, 55 % ou 0 %, 0 %, − 7 % | **réserve** : bras non joué ([SYN] § 6 : aucun gain à maxima serrés, protection d'une carte membre perdue). La démonstration du réfutateur n'est pas contre-lue ; ce plan ne la confirme ni ne l'infirme | — |
| 3 (2, avertissement) | un banc qui sous-optimise le maximum fabrique un faux gain | **tranché par une mesure** : J9 est le code du v9 lui-même, à valeur certifiée ; `ecart_residuel` rapporté ; sensibilité J9⁺ sur tous les gains ; P14 | Métrique ; étage 4 |
| 4 (3) | origine du prix du v9 : liberté des poids par morceau, ou parts égales | **tranché par une mesure descriptive** sur ce banc : décomposition 1 − ρ_La, ρ_La − ρ_Ld, ρ_Ld. Sans verdict | Métrique ; étage 8 |
| 5 (4) | « aucune méthode valide plus puissante » | **tranché par une mesure** : J9-D40 et J9-D contre J9, même classe (P10) ; et J9-P contre J9 (P6) | étages 4 et 6 |
| 6 (5) | seuil simulé « grille plus projection » : non valide ou indéterminé | **réserve** : non joué, aucune preuve, puissance la plus basse ([SYN] § 4.5). Reste « non établi » | — |
| 7 (6) | erreur de l'estimateur du mélange du portefeuille universel | **réserve** : non joué ; voie dominée par le maximum (théorème, [SYN] § 4.4) ; sans effet sur ce plan | — |
| 8 (7) | le « v9 du banc » à grille de déciles n'est pas le v9 | **tranché par construction et par mesure** : aucune grille ; code original du v9, toutes les coupures réelles ; les cellules fatales de Q5 (coupure hors de l'archive, entre deux valeurs quelconques) l'éprouvent pour J9, J9-D40, J9-D, et la copie de Q5 pour J9-P | Banc ; P1, P2 |
| 9 (8) | perte de la protection « une carte membre n'est jamais promue » quand le monde est hors du nul | **réserve** pour les cinq bras à ensemble de confiance (non joués). **Mesure** de la même protection pour les bras joués : Q9a, Q9b (P13) | étage 8 |

## Critères de lecture gelés

Lecture dans cet ordre ; un étage non franchi arrête la lecture des suivants, sauf mention.

| étage | observé | verdict |
|---|---|---|
| 1 | une cellule de taille « non tenue » (Holm) ; **ou** une promotion ou un log W > 10⁻⁶ sur une cellule fatale ; **ou** un nichage ou une monotonie violés | **« trou »** : défaut de code, de certificat ou de preuve ; rien d'autre n'est lu ; audit écrit ; nœud |
| 1 bis | une cellule « non jugeable » pour un bras | **« validité non établie »** pour ce bras : ses lectures de puissance sont rapportées sous cette réserve ; **aucune adoption ne peut s'en réclamer** |
| 2 | dents non tenues : J8 sur Q2 à Q5, J9 sur Q6, A1 ou A2 sur Q1 ou Q2 | **« banc sans dents »** (non concluant). La dent de H7 est lue à l'étage 7 seulement |
| 3 | moins de 2 lignes informatives | **« prix du v9 non reproduit sur ce banc »** (non concluant sur H-1.1 v2) ; les étages 6 à 8 restent lus |
| 4 | principale, dans l'ordre du Seuil ; puis la même lecture avec J9⁺ | « nuisible » / « regagne » / « ne regagne pas » / « partiel » ; si J9⁺ change le verdict : **« sensible au certificat »**, et c'est le moins favorable des deux qui est retenu |
| 5 | La, Ld | « recouvre » / « ne recouvre pas » / « en partie » ; ρ_Ld ≤ ρ_La par construction |
| 6 | secondaires : La-P contre La ; J9-P contre La ; J9-D40 et J9-D contre J9 | « gain » ou non, avec intervalle ; rapportés |
| 7 | garde P4 (Hs, Hm, H7) | « nécessaire, montrée » / « non éprouvée » (dent de H7 manquée) / « trou atteint par la grammaire » (Hs ou Hm) ; une cellule avec gel « non tenue » relève de l'étage 1 |
| 8 | copies rouvertes par La, Ld, La-P ; protection Q9a, Q9b ; décomposition du prix ; strate sans membres log-linéaires | rapportés, sans verdict |

**Issue rendue pour le nœud R-1779** (si les étages 1 à 3 sont franchis) :
- **(A)** « J9-P regagne » : un candidat v10 **de même classe que le v9** existe sur ce banc, sous la garde P4. À valider à part.
- **(B)** J9-P ne « regagne » pas, « La recouvre » : un nul moins coûteux n'existe sur ce banc qu'en rétrécissant la classe ;
  la décision dépend de la question de sens (R-1768, R-1779), ouverte. Si « Ld recouvre » aussi, le dire.
- **(C)** J9-P « ne regagne pas » et ni La ni Ld ne recouvrent : aucune voie de cette famille ne reprend le prix ; restent
  « accepter le prix » et, au mieux, la règle de lecture (étage 6).
- **(D)** autre combinaison : « non tranché », avec les estimations.
- **Dans tous les cas : rien n'est adopté.** L'issue ouvre un nœud ; la décision est à Lazar.

**Audit de symétrie (R4)**, écrit avant le prononcé, pour **toute** issue : membre ou famille qui décide, par cellule ;
distribution des certificats de bloc et de leur coût ; distribution des écarts résiduels ; comptes des vérifications de nichage
et de monotonie ; décomposition de ρ ligne par ligne et par strate ; répétitions où J9-P promeut et J8 non (possible : aucun
ordre entre eux ; à lire une à une si plus de 1 %). **« Trop propre »** : une part regagnée ≥ 0,95 ou ≤ 0,05 sur toutes les
lignes ; toutes les prédictions vraies ; aucune promotion dans aucune cellule de taille de J9-P alors que le pire cas Q8 en
attend ; gain de J9-P identique sur toutes les lignes. **« Tout négatif »** : J9-P égal à J9 répétition pour répétition ;
certificats tous égaux à 1 au dernier chiffre ; J9-D40 égal à J9 partout. Dans les deux cas : même relecture écrite du code
d'évaluation.

## Liste d'arrêt

Chaque ligne a son essai sain et son artefact (R5 ; [CL] m7). Aucun repli silencieux.

| condition | action |
|---|---|
| préalable 1 ou 2 non levé | pas de jeu |
| copie de `nul_v9.py` d'empreinte ≠ `7ae450df…`, ou un module de la copie `94bfd92` non conforme à sa liste | pas de jeu |
| un fichier gelé diffère de l'addendum ; un essai échoue ; une mutation survit | pas de jeu |
| essai E0, E9, EP ou ED manqué | arrêt avant le jeu ; défaut |
| une issue fraîche tirée avant le gel, ou lue par la fonction qui bâtit un engagement ou un journal de projection | arrêt ; défaut |
| le module de projection lit une issue du bloc qu'il projette (garde d'accès) | arrêt ; défaut |
| une carte qui lit l'historique arrive à J9-P ou à La-P sans passer par une forme de la garde P4, hors des bras « sans garde » déclarés | arrêt ; défaut |
| un engagement avec `fractions` | arrêt ; défaut (pari plein seulement) |
| un certificat de bloc non calculé, non fini, ou inférieur à 1 − 10⁻⁹ (impossible en théorie : la moyenne certifiée vaut 1 au point projeté, donc au moins 1 en un sommet) | arrêt ; défaut |
| une exception dans une évaluation ; un log W non fini | arrêt du run entier ; aucune lecture partielle ; relance seulement sous un texte ou un addendum neuf |
| monotonie violée : log W de J9, La ou Ld > log W de J8 + 10⁻⁶ à un instant | arrêt ; défaut de code |
| nichage violé : log W de La ou de Ld < log W de J9 − écart résiduel du membre limité − 10⁻⁶ ; ou log W de Ld > log W de La + écart résiduel de La + 10⁻⁶ | arrêt ; défaut de code, ou famille du v9 différente de [PREUVE] § 3 : audit, nœud |
| domination violée : J9 promeut et J9-D40 ou J9-D ne promeut pas | arrêt ; défaut de code |
| plus de 1 % des évaluations avec un écart résiduel > 2·10⁻³ nat | rapporté ; le run va à son terme |
| durée murale > 72 heures | arrêt ; run invalide, aucune lecture |
| une lecture avant le scellement de la sortie | run invalide |
| toute dépense, instance payante, appel réseau ou appel de modèle | interdit (R-2851) |

## Coût et durée

**Processeur seul, 0 dollar.** Temps par évaluation, **estimés, non mesurés sur ce banc** : J8 0,02 à 0,03 s ([V1], annexe B) ;
J9 0,25 à 0,29 s par évaluation appariée v8 et v9 (note `4d3a6d1c…`, l. 44) ; La, Ld 0,05 à 0,3 s (estimation) ; projection
sur toutes les coupures 0,46 à 0,53 s, sur les coupures de l'archive 0,08 à 0,09 s ([PROJ] § 8, machine chargée) ; v9 à 40
instants : environ 4,6 fois le nombre de coupes de la lecture à 8 instants (Σ t sur T₄₀ = 4 100 contre 900 sur T₈), soit
1,2 à 1,4 s (estimation). Par répétition : 2,5 à 3 s pour tous les bras ; 28 000 répétitions : **20 à 25 heures d'un cœur,
10 à 15 heures sur deux processus** ; strate sans membres log-linéaires, rééchantillonnages, essais : 2 heures de plus au
plus. Machine partagée à 4 cœurs : la durée peut doubler. Borne dure : 72 heures. Écriture du code, essais, mutations,
contre-lectures : temps d'agents, sans dépense. Aucune machine louée.

## Écarts, nœuds et ce que l'essai ne décide pas

- **Préalable 1 (mère)** : [V9] vient du commit `a41b7b5` du dépôt tiers ; la copie du juge est au commit `94bfd92`. La
  compatibilité de `nul_v9.py` avec les modules `nul_filles_v2`, `nul_v8`, `selection_pari` et `outils` de `94bfd92` **n'est pas
  établie par empreinte** (les dépendances au commit `a41b7b5` ne sont pas au dépôt). Elle s'établit par l'essai E9 et par les
  essais de `test_nul_v9.py` (`d42a50eb4ba9691e75e82fa4bc714a925615da80df22227fee730392015999b9`) rejoués par import depuis le
  banc ; ou par le versement des dépendances au même commit, décision de la mère. Sinon : pas de jeu.
- **Préalable 2 (mère)** : une pièce « preuve, version 2 », scellée et contre-lue, qui porte les corrections p1 à p6 de [CL],
  le lemme de la projection par blocs **sous la garde P4**, et la preuve du rejet par famille. Ce texte emploie ces énoncés ;
  il ne les prouve pas.
- **Le banc** ne touche ni le juge de production, ni le v9, ni la boucle : aucun écart à une conception scellée. Différences
  de montage avec la production, comme [BANC-v2] : plan « ordre_naturel » ; issues fraîches tirées par le banc après le gel.
- **Ajouts au banc partagé** : les six lignes Q8, Q9a, Q9b, Hs, Hm, H7 sont propres à l'idée 1.1 ; le banc B v2 de l'idée 1.2
  n'est pas modifié.
- **Nœud de Lazar — adoption.** Adopter J9-P, La-P, La ou Ld ferait un nul v10 ; adopter J9-D40 change `instants_lecture` ;
  adopter J9-D change la règle de lecture et ne se branche pas sur e-BH. Chaque adoption est une modification du juge, avec
  sa validation scellée. **Ce plan n'en décide aucune.** Pour J9-P, l'adoption demanderait en plus ([R-PROJ] § 9) : la garde
  P4 dans le juge (rétrécissement de ce qu'il accepte aujourd'hui) ; la règle de marge des filles redéfinie ou laissée au
  maximum ; l'audit « près de 1 » ; l'optimiseur gelé sous l'empreinte ; le pari à fraction abandonné ou gelé par bloc.
- **Ne décide pas** : la question de sens (une copie par sous-population est-elle une découverte ?) ; la puissance sur les
  mondes riches à 8 traits (le nombre de coupures, donc de familles de J9-P, y grandit) ; le contrôle d'erreur entre
  générations et le branchement sur e-BH ; la réserve log-linéaire du v8 ; la projection à blocs plus petits que 25 ; les
  cartes à pari à fraction ; l'existence d'une carte de la grammaire qui atteint le trou de P4 au-delà de Hs et Hm ; toute
  revendication publique (clause de N-067).

## Contre-lecture

- **Contre-lecture 1** (R2, sur la version 1) — sous-agent neuf, qui n'a écrit ni [V1] ni [PREUVE] ; texte relu : version 1,
  `docs/notes/organisme-idees-juge-v1/prereg-nul-par-morceaux-limite-v1.md`,
  `46ef2b92119ee5dff05727b90ca8bdd3ba57b52f9c1c75893750c792a2abc089` ; rapport :
  `docs/notes/organisme-idees-juge-v1/contre-lecture-prereg-nul-limite-et-preuve-v1.md`,
  `763fc6e29cd80868dcdb1d848eafdc928a39fca7244fa16eb0ac721ec705014e`. Verdict : « scellable après corrections » (4 majeurs,
  9 mineurs). **Traitement**, remarque par remarque :
  - M1 (aucune découverte posée sur une coupure de l'archive) : **acceptée** — ligne V5 du banc B v2 (R-2875) ; ρ sur toutes les
    lignes informatives, V5 comprise ; strates ; prédiction propre à V5 (P7).
  - M2 (changements au code du v9 ; entrée de J9) : **acceptée** — changements déclarés du bras 2 ; entrée de J9 écrite au
    « Banc ». Le type « croisement » n'est pas ajouté : La2 est retiré.
  - M3 (P8 non réfutable ; gardes de nichage) : **acceptée** — P8 de [V1] disparaît avec La2 ; ρ_Ld ≤ ρ_La écrit comme fait de
    construction (P8, étage 5) ; garde de nichage de Ld sur La ajoutée à la liste d'arrêt.
  - M4 (tolérances) : **acceptée** — constantes du code inchangées ; nichage à l'écart résiduel ; seuil de 2·10⁻³ nat.
  - m1 (ordre du gel) : **acceptée**. m2 (coupure proche du signe) : **acceptée** par le banc B v2 (|s| ≥ 0,3). m3 (« promotions
    de copies ») : **acceptée**. m4 (I recalculé dans chaque rééchantillon) : **acceptée**. m5 (P5 entre 2 et 3 lignes) :
    **acceptée**. m6 (graines de E0) : **acceptée**. m7 (essai sain et artefact pour chaque garde) : **acceptée**. m8 (audit borné
    au pari plein) : **acceptée**. m9 (empreintes entières dans cette section) : **acceptée**.
  - p1 à p6 (preuve) : **acceptées pour ce texte**, qui emploie les énoncés corrigés ; leur report dans la preuve est le
    préalable 2.
- **À venir** : contre-lecture de ce brouillon 1 par un sous-agent neuf, qui n'a écrit ni ce texte, ni [SYN], ni les rendus des
  angles. **Fichiers à lui donner explicitement** : ce texte ; [SYN] ; [PROJ] et [R-PROJ] ; [R-LIB] (§ 8 et § 10) ; [R-UNI]
  (§ 8.1) ; [V1] et [CL] ; [PREUVE] ; [BANC-v2] ; [V9] ; `selection_pari.py`, `nul_filles_v2.py`, `nul_v8.py` de la copie
  `94bfd92` ; `essai_projection_commun_v1.py`, `essai_projection_methodes_v1.py`, `attaque_projection_v1.py`. Questions à
  trancher : compte des cellules ; validité de la réunion qui définit J9-D40 et J9-D ; « famille » = membre nommé ; forme
  « gel de l'historique » de la garde ; seuil d'un quart de la principale ; ligne Q8 bâtie sur le plan ; traitement des neuf
  désaccords ; durée. Chaque remarque recevra un traitement écrit dans la version suivante.

## Annexe A — seuils (compte seul, sans donnée, sans juge)

Script (`d7408ee146824ce9150d8f644d750093ac75fe6a0e1bb60fef5d73373bce83f3`) et sortie
(`7907a1c9e75858c0c3c46f29019eaa675b292620d5cd685c74c84d8768cc2051`), dossier de travail de la session, recopiés en entier :

```
taille, 53 cellules, niveau le plus strict (0,05/53) : tenue si <= 29 ; non tenue si >= 74
taille, 53 cellules, niveau le moins strict (0,05) : tenue si <= 38 ; non tenue si >= 63
borne basse unilatérale à 95 % > 0.5 : à partir de 527 sur 1000 (borne 0.5005)
borne basse unilatérale à 95 % > 0.05 : à partir de 63 sur 1000 (borne 0.0508)
borne basse unilatérale à 95 % >= 0.02 : à partir de 29 sur 1000 (borne 0.0208)
```

```python
"""Seuils du préenregistrement de l'idée 1.1, version 2 (compte seul, sans donnée, sans juge).
(1) Cellules de taille : test binomial exact au taux 0,05 sur 1 000 répétitions, au niveau le plus strict de Holm
    (0,05/m) et au moins strict (0,05), pour m cellules.
(2) Dents : plus petit nombre de promotions sur 1 000 dont la borne basse de Clopper-Pearson unilatérale à 95 % dépasse
    0,5, puis 0,05.
(3) Ligne informative : plus petit nombre de paires discordantes sur 1 000 dont la même borne basse atteint 0,02."""
from scipy.stats import beta, binom

n = 1000
for m in (53,):
    for nom, lv in (("le plus strict (0,05/%d)" % m, 0.05 / m), ("le moins strict (0,05)", 0.05)):
        kt = max(k for k in range(n + 1) if binom.cdf(k, n, 0.05) <= lv)
        knt = min(k for k in range(n + 1) if binom.sf(k - 1, n, 0.05) <= lv)
        print(f"taille, {m} cellules, niveau {nom} : tenue si <= {kt} ; non tenue si >= {knt}")


def borne_basse(k):
    return 0.0 if k == 0 else float(beta.ppf(0.05, k, n - k + 1))


for seuil, strict in ((0.5, True), (0.05, True), (0.02, False)):
    k = min(k for k in range(n + 1) if (borne_basse(k) > seuil if strict else borne_basse(k) >= seuil))
    print(f"borne basse unilatérale à 95 % {'>' if strict else '>='} {seuil} : à partir de {k} sur {n} (borne {borne_basse(k):.4f})")
```

## Citations obligatoires (N-064, N-067)

POPPER (Huang et al., ICML 2025 ; `docs/sources/pdf/huang-2025-icml-pmlr-267-popper-automated-hypothesis-validation-agentic-sequential-falsifications.pdf`,
`a3c4b3701543a84a74602ae46a624b955e201bb83baeea2c219213a0e65b4998`) ; Dwork et al., arXiv 1506.02629
(`docs/sources/pdf/anteriorite-P-041-v2/c8/1506.02629.pdf`, `dcfbb9aa401c62949123be2d74787c4f9cca48597f18860760ef1580ddb4bc71`) ;
Blum et Hardt, « The Ladder », arXiv 1502.04585 (`…/c8/1502.04585.pdf`, `957ef4739df371a0a778360f0db4252a62f7c85abcd8343f581cd6250b1d31fe`) ;
Co-Scientist (Gottweis et al., Nature 655, p. 487-496, 2026 ;
`docs/sources/co-scientist-v1/gottweis-2026-nature-655-487-accelerating-scientific-discovery-with-co-scientist.pdf`,
`351f49d89d2f4f4ed84eed4225c09cc95470c41aa3becd0aa3e06b3bd8ba54c3`) ; liste de `docs/decisions/decision-N-067-v1.md`
(`966dd9dc3fae61cbe1f10ee2a54f401ddf7af5041eeaacd81ad9f8b264661589`), section 6. Empreintes reprises de [BANC-v2] ; PDF non
rouverts par moi ; aucun chiffre n'en est tiré. Aucune revendication n'est faite ici.
