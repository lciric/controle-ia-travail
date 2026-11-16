# Préenregistrement — apprendre les poids du test de référence (« nul ») sans casser sa garantie : projection par blocs, nuls limités et règles de lecture, contre le nul v9, sur le banc B v2 — idée 1.1, version 2, brouillon 2

- Auteur : concepteur neuf, sous-agent de la session mère, auteur du brouillon 1 ; je n'ai écrit ni la contre-lecture du
  brouillon 1, ni la version 1, ni sa contre-lecture, ni la preuve,
  ni la synthèse, ni les rendus des cinq angles, ni leurs réfutations, ni le juge, ni les nuls v8 et v9, ni le
  préenregistrement de l'idée 1.2.
- Date (UTC) : 2026-11-15 ; brouillon 1 rédigé de 20:14 à 20:27, dépôt lu sur `main`, têtes `4b03f673` puis `9c3df628`
  ([CL2] m1) ; brouillon 2 rédigé de 20:40 à 20:45 (`date -u`), tête `3d7c5edd` ; aucun commit de ma part, aucune poussée,
  aucun appel réseau, aucun appel payant.
- Commit du code d'analyse : **aucun à ce jour**. Le code s'écrit après la contre-lecture de ce texte et le scellement de la
  version qui fera foi ; ses empreintes entrent dans un **addendum d'empreintes** scellé avant tout jeu, qui ne change rien
  d'autre.
- Documents qui font foi (chemin + empreinte entière, toutes recalculées le 15 novembre ; égales à leurs compagnons, ou, pour les
  modules de la copie `94bfd92`, à `empreintes-copie-v1.txt` ; `src/controle_ia/prereg.py` n'a pas de compagnon, son empreinte est
  calculée le 15 novembre) :
  - brouillon 1 de ce texte, gardé intact (R12) : `docs/notes/organisme-idees-juge-v1/organisme-idee-1-1-poids-du-nul-v2-brouillon1.md`
    (`916985cec9ba027effa9fdcf4bf70827424a838ed875358ae213dc1f60d30b55`) — **[B1]** ; sa contre-lecture (« scellable après
    corrections », six majeurs, quatorze mineurs) : `docs/notes/organisme-idees-juge-v1/contre-lecture-idee-1-1-v2-brouillon1-v1.md`
    (`d5e71f6c7ee41600a207255614685c303ecca68aecdf457291eaf9a6d6571c4b`) — **[CL2]** ;
  - seuils de l'annexe A, versés : `docs/notes/organisme-idees-juge-v1/organisme-idee-1-1-poids-du-nul-v2-outils/seuils_idee_1_1_v2_brouillon2.py`
    (`91fd1d11ec4b4ebeb19257209ea1d96a62d67e0f211c071ef0173a0ee044ecda`) et `…/sortie-seuils-idee-1-1-v2-brouillon2.txt`
    (`4e508c64f7cc5e352556fbba473cd6759e444b16f7739e0b4d8d0ad660b672f2`) ;
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

**Statut.** Brouillon 2 de la version 2, **scellé par empreinte seulement (R6) : il ne vaut pas préenregistrement au sens de
R1**. Il porte sur le brouillon 1 les six majeurs et les quatorze mineurs de [CL2] (réponses point par point : « Contre-lecture
2 ») et les précisions de la mère sur M3, M5 et M6 ; rien d'autre ne change. Il le deviendra sous un nom neuf, après le
contrôle du différentiel par un sous-agent neuf (R2) et scellement par `controle_ia.prereg.sceller_prereg`, puis recopie octet pour octet sous `prereg/` (comme
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
| banc | banc B v1 (19 lignes) | banc B v2 de [BANC-v2] (22 lignes, V5 comprise), plus sept lignes propres à ce texte (Q8, Q9a, Q9b, Hs, Hm, H7, Hg) |
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
moins un quart** de la puissance que le v9 perd contre le v8 sur de vraies découvertes (les 15 lignes V), **sans rouvrir aucune
copie de la classe du v9** — chaque cellule de copie de J9-P « tenue » (taux ≤ α) ; une carte membre y reste près de 1, pas au
plus 1 ([CL2] m12) — et en gardant sa taille α.

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
  W^reste contient le membre ordinaire `moyenne_glissante` de la bibliothèque, qui lit l'historique : sans effet sur la validité
  (minimum de deux statistiques valides chacune sur sa classe ; [CL2] m13). **Sous la forme « gel » de la garde, la carte jugée
  est la carte gelée, pas la carte soumise** ([CL2] M2).
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
ρ_X : part regagnée par le bras X (« Métrique »). **« Lignes informatives » veut toujours dire : parmi les 15 lignes V** (I ⊂ {V},
[CL2] M1) ; aucune ligne Q ou H n'entre dans ρ, dans un gain réuni ou dans la décomposition du prix.

| # | prédiction | signe | chiffre | ce qui la réfute | confiance |
|---|---|---|---|---|---|
| P1 | cellules fatales (carte membre exact de la classe d'un bras à maximum : 34 cellules) | nul | 0 promotion sur 1 000 ; log W maximal ≤ 10⁻⁶ | une seule promotion, ou un log W > 10⁻⁶ (défaut de code ou de certificat) | 0,97 |
| P2 | cellules de taille et copies des bras à projection (35 cellules ; pire cas Q8 compris) | sous α | taux ≤ 0,03 dans chaque cellule ; toutes « tenues » | une cellule « non tenue » (Holm) | 0,8 |
| P3 | dents : J8 promeut les copies Q2 à Q5 ; J9 et J9-P promeuvent la copie à deux niveaux Q6 ; A1 et A2 promeuvent les copies Q1 et Q2 | + | J8 ≥ 0,90 ; J9 ≥ 0,80 sur Q6 ; J9-P ≥ 0,60 sur Q6 (rapporté, sans seuil : même trou que le v9) ; A1 ≥ 0,90 ; A2 ≥ 0,30 | une borne basse sous son seuil (« Seuil ») ; pour J9-P sur Q6, un taux < 0,5 | 0,75 |
| P4 | copies rouvertes par les nuls limités : La et La-P promeuvent Q3, Q4, Q5 ; Ld promeut Q5 | + | La et La-P ≥ 0,85 ; Ld ≥ 0,60 | La ou La-P < 0,5 sur Q3 ou Q4 (à auditer) | 0,7 |
| P5 | prix du v9 sur ce banc : lignes V informatives | J9 < J8 | au moins 4 des 15 lignes V ; 2 ou 3 : prédiction « partielle » | moins de 2 | 0,65 |
| P6 | **principale** : part regagnée par J9-P | + | estimation ponctuelle de ρ_J9-P dans [0,25 ; 0,60] ; « regagne » (borne basse ≥ 0,25) | borne haute < 0,10 (« ne regagne pas ») | 0,45 pour « regagne » ; 0,8 pour une estimation > 0,10 |
| P7 | part recouvrée par La | + | borne basse de ρ_La ≥ 0,5 (ponctuelle 0,6 à 0,9) ; sur les lignes V5 informatives, La recouvre au plus 0,3 | borne haute < 0,25 | 0,55 |
| P8 | part recouvrée par Ld | + | ρ_Ld ≤ ρ_La **par construction** ; ponctuelle dans [0,35 ; 0,80] | borne haute < 0,25 | 0,5 |
| P9 | La-P contre La, même classe, lignes informatives réunies | + | gain apparié réuni de + 0,02 à + 0,10 | borne haute du gain réuni < 0 | 0,55 |
| P10 | J9-D contre J9 (jamais négatif, par construction) ; J9-D40 seul | + faible | gain réuni sur les lignes V : J9-D de + 0,010 à + 0,040 ; J9-D40 de + 0,005 à + 0,025 | gain réuni de J9-D < 0,005 | 0,6 |
| P11 | J9-P contre La, lignes informatives réunies | − ou 0 | écart réuni dans [− 0,11 ; + 0,03] | borne basse > 0 (bonne nouvelle : la classe du v9 sans prix) | 0,6 |
| P12 | garde P4 : carte hors grammaire H7 sans garde, **terme projeté seul** ; le même dans le juge complet (rapporté) ; avec garde par gel de l'historique ; cartes de la grammaire Hm et Hg sans garde ; Hs (aveugle par construction) | + ; + ; sous α ; sous α ; nul | H7, terme projeté sans garde ≥ 0,20 ; H7, juge complet sans garde ≥ 0,10 (confiance 0,5, sans seuil) ; avec gel ≤ 0,02 sur les quatre lignes ; Hm et Hg sans garde < 0,05 ; Hs sans garde ≤ α | H7, terme projeté : borne basse ≤ 0,05 (la garde n'est pas éprouvée) ; gel : cellule « non tenue » ; Hm ou Hg : borne basse > 0,05 (le trou est atteint par une carte de la grammaire) | 0,6 |
| P13 | protection d'une carte membre quand le monde est hors du nul (Q9a, Q9b) | nul | 0 promotion dans tous les bras ; pour J9-P et La-P, log W maximal ≤ 0,5 (prédiction seulement ; le seuil d'audit est 1,0 nat, « Seuil ») | une promotion (bras à maximum : défaut ; bras à projection : protection perdue) | 0,8 |
| P14 | écart du certificat du v9 : sensibilité J9⁺ | nul | J9 et J9⁺ diffèrent sur moins de 0,5 % des répétitions des lignes V ; le verdict de P6 est le même avec J9⁺ | verdict de P6 différent avec J9⁺ | 0,85 |

**D'où viennent ces chiffres** (exploratoires, autres bancs ; [SYN] § 4 et § 7) : gain de la projection à classe égale + 0,045 à
+ 0,185, part regagnée 0,41 à 0,82, **sans** membres log-linéaires, sur 100 à 200 mondes par dose ([PROJ] § 6) ; le gain de La
tombe d'un tiers à la moitié quand on garde les membres log-linéaires ([R-LIB] § 8) : d'où un intervalle prédit plus bas pour
J9-P ; lecture dense et rejet par famille + 0,020 à + 0,032 ([R-LIB] § 10) ; pire cas de la projection 35/2 120 ([R-PROJ]
§ 4.3) ; carte qui lit l'historique 904/2 000 pour le membre linéaire seul et 18/60 pour toutes les coupures, 0/2 000 pour le
réglage de Hm ([R-PROJ] § 5) ; aucun chiffre exploratoire n'existe pour Hg ni pour H7 dans le juge complet ;
J8 sur les copies : 0,986 et 0,972 dans la validation du v9 ([CL] § 1, audit `9086a420…`).

**Ce que serait chaque issue (R3).** P6 vraie : un candidat v10 existe **dans la classe du v9**, sous la garde P4 (meilleur
cas). P6 fausse et P7 vraie : un nul moins coûteux n'existe sur ce banc qu'en rétrécissant la classe (question de sens,
R-1768, R-1779). P6 et P7 fausses : le prix du v9 n'est repris par aucune voie de cette famille ; il reste « accepter le prix »
et, au mieux, les règles de lecture (P10). P5 fausse : le prix du v9 ne se reproduit pas sur ce banc, rien ne se lit sur la
principale. P12 fausse sur H7 (terme projeté) : le banc ne montre pas le défaut que la garde corrige. P12 fausse sur Hm ou Hg :
la garde est nécessaire dès la grammaire actuelle. P1, P2 ou P13 (bras à maximum) fausses : défaut de code ou de preuve.

## Métrique

- **Promotion d'une carte seule** (bras à huit instants) : il existe t ∈ T₈ = {25, 50, …, 200} avec log W_t ≥ log(1/α),
  α = 0,05 (règle de `nul_filles_v2.evaluer_v2`, sans marge des filles : cartes fraîches). Bras à 40 instants : « Bras ».
- **Taux d'une cellule** : promotions / 1 000 ; intervalle de Clopper-Pearson, bilatéral à 95 % pour le rapport, unilatéral à
  95 % pour les seuils.
- **Perte appariée du v9 sur une ligne ℓ** : δ₉(ℓ) = (1/R)·Σ_r (a_r − b_r), a_r = 1[J8 promeut], b_r = 1[J9 promeut]. Par
  monotonie ([PREUVE] § 6 (a)), b_r ≤ a_r.
- **Gain apparié d'un bras X sur un bras Y** : Δ_{X,Y}(ℓ) = (1/R)·Σ_r (x_r − y_r) ; test exact de McNemar par ligne (rapport).
  Δ_X = Δ_{X,J9}. **Gain réuni** sur un ensemble de lignes : moyenne des Δ(ℓ), lignes à poids égaux. **Deux pondérations, non
  interchangeables** ([CL2] m3) : ρ (chaque ligne pesée par sa perte δ₉) pour les trois primaires ; gain réuni (poids égaux) pour
  les secondaires seulement, sur un ensemble nommé : I pour La-P contre La et J9-P contre La ; les 15 lignes V pour J9-D et
  J9-D40 contre J9. Même rééchantillonnage (graines `(99, b)`), I recalculé de même.
- **Ligne informative** : ligne **parmi les 15 lignes V** (V1 à V5, trois doses) dont la borne basse unilatérale à 95 % de
  δ₉(ℓ) est ≥ 0,02, soit au moins 29 paires discordantes sur 1 000 (annexe A). I ⊂ {V} est fixé par J8 et J9 seuls. **Les
  lignes Q, Hs, Hm, Hg, H7 n'entrent jamais dans ρ, ni dans un gain réuni, ni dans la décomposition du prix** ([CL2] M1 : sur
  Q2 à Q5 et Q7, J8 promeut des copies et J9 non ; les compter ferait passer une promotion de copie pour de la puissance).
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
  d'un v9 exact est entre celle de J9 et celle de J9⁺. **Définition gelée** ([CL2] M4) : ρ⁺_X = Σ_{ℓ ∈ I⁺} (x − b⁺) /
  Σ_{ℓ ∈ I⁺} (a − b⁺), où b⁺ = 1[J9⁺ promeut] et I⁺ = lignes V informatives pour le couple (J8, J9⁺), recalculé dans chaque
  rééchantillon ; mêmes quantiles de Bonferroni. Les gains secondaires sont rapportés contre J9⁺ de la même façon. J9⁺ n'est
  pas un test valide : il ne sert que de comparateur.
- **Journal de la projection** (J9-P, La-P), par répétition : plus grand et médian c − 1 des certificats de bloc ; coût total
  Σ 25·log max(1, c) du processus retenu ; empreinte du tableau des poids projetés. Journal entier pour les 20 premières
  répétitions de chaque ligne.
- **Mesures descriptives** (aucun critère) : log W maximal et médian par cellule ; membre ou famille qui décide (minimum) ;
  `ecart_residuel` des membres par morceaux ; temps par évaluation ; strate « sans membres log-linéaires » (ci-dessous).
- Aucune moyenne ni médiane sur des jetons : il n'y en a pas ici.

## Seuil

- **Niveau du juge** : α = 0,05 ; n = 200 tirages frais ; marginale d'entraînement sur 100 instances (comme
  `a_blanc_v59.juger_carte`).
- **Cellules de taille** (57, comptées au « Plan d'analyse ») : test binomial exact, procédure de Holm au niveau 0,05 sur la
  famille des 57, dans chaque sens. « Tenue » si H₀ « taux ≥ α » est rejeté ; « non tenue » si H₀ « taux ≤ α » est rejeté ;
  sinon « non jugeable ». Au pas le plus strict (0,05/57) : tenue si ≤ 29 sur 1 000, non tenue si ≥ 74 ; au pas le moins
  strict : ≤ 38 et ≥ 63 (annexe A).
- **Cellules fatales** (34) : **toute** promotion, ou tout log W > 10⁻⁶, déclenche l'audit (une carte membre ne peut pas être
  promue par un bras à maximum, sous le pari plein). L'engagement de chaque bras est sans `fractions` (vérifié par un essai,
  [CL] m8). Pour J9-D, qui n'a pas de W unique, la quantité fatale est max sur t ∈ T₄₀ de log q(y_1..t) − V_m(t) pour le
  membre m qui contient la copie ; > 10⁻⁶ : audit ([CL2] m6).
- **Copies des bras à projection** (7 cellules, dans la famille des 57 ; et Q9a, Q9b) : en plus, **un seul seuil d'audit écrit**
  ([CL2] m5) : log W maximal d'une carte membre ≤ 1,0 nat ; au-dessus, audit de l'optimiseur (pas un « trou » : la validité ne dépend pas de ce seuil).
- **Dents** : borne basse de Clopper-Pearson unilatérale à 95 % **> 0,5** (au moins 527 sur 1 000) pour J8 sur Q2, Q3, Q4, Q5,
  pour J9 sur Q6 et pour A1 sur Q1 et Q2 ; **> 0,05** (au moins 63 sur 1 000) pour A2 sur Q1 et Q2 ([SYN] § 6, point 6 ; annexe A).
- **H7, deux quantités** ([CL2] M3) : **(i)** le **terme projeté seul**, min_F Σ_b log e_{F,b}, sans W^reste (« témoin de
  code ») ; sa dent sans garde : borne basse > 0,05 (au moins 63 sur 1 000) ; **(ii)** **J9-P-nu complet**, minimum avec W^reste,
  le numérateur Σ log q_s(y_s) étant calculé par le banc : **rapporté, sans seuil**. La cellule de Holm « J9-P avec gel » sur H7
  porte sur (i), qui majore la richesse de J9-P : « tenue » sur (i) vaut « tenue » pour J9-P.
- **Principale (J9-P)**, lue dans cet ordre, la première vraie l'emporte : 1. **« nuisible »** si la borne haute de ρ_J9-P
  < 0 ; 2. **« regagne »** si la borne basse ≥ 0,25 ; 3. **« ne regagne pas »** si la borne haute < 0,10 ; 4. sinon
  **« partiel »**. Au moins 2 lignes informatives sont exigées (sinon « sans objet »). Le seuil d'un quart est un jugement
  gelé : en dessous, le gain ne paierait pas ce que la voie change au juge (garde P4, optimiseur dans le résultat, audit
  « près de 1 »).
- **La, Ld** (seuils de [V1]) : « recouvre » si la borne basse de ρ_X ≥ 0,5 ; « ne recouvre pas » si la borne haute < 0,25 ;
  sinon « en partie ».
- **Secondaires**, intervalle percentile bilatéral à 95 % du gain réuni sur les lignes informatives, sans correction : La-P
  contre La ; J9-P contre La ; J9-D et J9-D40 contre J9 (sur les 15 lignes V). « Gain » si la borne basse > 0.
- **Garde P4** : « nécessaire, montrée sur le terme projeté » si le terme projeté sans garde passe la dent sur H7 **et** si J9-P
  avec gel est « tenu » sur Hs, Hm, Hg et H7. « Trou atteint par la grammaire » si la borne basse de J9-P-nu complet dépasse 0,05
  sur Hm ou sur Hg. Hs n'entre pas dans ce verdict (aveugle par construction, « Banc »).
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
| Q9b carte membre, monde hors du nul | monde de V1(0,50) | `melange`([S1, S2, S3, S4, uniforme fixe], poids de Dirichlet(1, …, 1) arrondis à six décimales et renormalisés), comme Q1 | idem |
| Hs carte de la grammaire qui lit l'historique | loi uniforme (`fixe`) | `sans_remise`, composition [70, 70, 70] | garde P4, réglage 0 de [R-PROJ] § 5 |
| Hm mélange de la grammaire qui lit l'historique | `melange`([S1, S2], [0,5 ; 0,5]) | `melange`([M, `sans_remise` [70, 70, 70]], [0,5 ; 0,5]) | garde P4, réglage 4 |
| Hg mélange de la grammaire à moyenne glissante | `melange`([S1, S2], [0,5 ; 0,5]) | `melange`([M, `moyenne_glissante` (3 issues, fenêtre 5, lissage 0,5)], [0,5 ; 0,5]) | garde P4, second type qui lit l'historique ([CL2] M3) ; jouée comme Hm |
| H7 carte écrite pour l'attaque, **hors grammaire** | `melange`([S1, S2], [0,5 ; 0,5]) | q_s(y) ∝ M_s(y)·exp(− 0,3·(nombre de y déjà vus dans le bloc − nombre attendu sous M)), plancher 10⁻¹², renormalisée (`carte_a_memoire`, genre « contre_exces_du_bloc », de `attaque_projection_v1.py`) | garde P4, réglage 7 ; témoin de code |

Q8 dépend du plan : la preuve est conditionnelle au plan, c'est le pire cas ; le monde ne lit que les instances, pas les
issues : il reste sans mémoire ; un monde réel ne le peut pas (dit). H7 ne passe pas par `valider_loi` : son terme projeté est
calculé par le module de projection, et son juge complet par le banc (numérateur du banc ; les membres ordinaires et
log-linéaires de W^reste ne dépendent pas de la carte) ; **je n'ai pas vérifié qu'elle s'écrit dans la grammaire** ([R-PROJ]
§ 5, limite (iii)). **Hs est aveugle sous J9-P-nu par construction** : son monde est uniforme, le membre ordinaire « uniforme »
est dans W^reste, et le minimum est borné par le rapport de la carte au monde, qui obéit à Ville. Hs éprouve W^reste, pas le
trou ([CL2] M3).

**Écart de montage** ([CL2] m11) : la bibliothèque est `BIBLIOTHEQUE_STANDARD` (juge v0, sans le membre « urne »). Le juge de
production v1 ajoute « urne », ou refuse au gel les cartes qui lisent l'historique (`cycle.py`, l. 318 à 327). Les lignes Hs,
Hm, Hg disent donc ce que ferait J9-P **sur le montage du banc**, pas en production.

**29 lignes × 1 000 répétitions** (réductions possibles seulement par la règle écrite au « Coût et durée »).

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
     projection de chacune des 26 partitions par trait et par bloc qu'une coupure induit (24 non triviales, plus 2 égales à la
     famille linéaire, [CL2] m8) : départ depuis la projection sans coupure du
     même bloc, **150 pas** (`IT_PROJ`, `IT_CHAUD` de `essai_projection_methodes_v1.py`, `29704896…`). Aucun autre critère
     d'arrêt ; double précision ; nombres de pas sous l'empreinte de l'addendum. Tout autre réglage est un écart.
   - *Gel et journal.* Pour une carte sans mémoire, **toutes** les projections et tous les certificats sont calculés au gel,
     avant le tirage des issues fraîches ; l'empreinte du journal est écrite dans l'enregistrement de la répétition avant que
     le générateur des issues fraîches soit créé (garde de code). Le module de projection ne reçoit jamais une issue du bloc
     qu'il projette (garde d'accès).
   - *Garde P4*, deux formes, toutes deux jouées sur Hs, Hm, Hg, H7 : **refus** — au gel, toute carte dont
     `selection_pari.types_de_la_loi(loi)` rencontre `TYPES_LISANT_L_HISTORIQUE` est refusée par le bras (comptée « refusée »,
     non promue) ; **gel de l'historique** — la loi de la carte est évaluée, au numérateur comme dans la projection, avec
     l'historique arrêté au début du bloc (ce qui change ce que la carte parie ; projections calculées au début de chaque
     bloc, sur les seules issues des blocs passés). **J9-P sans garde** (« J9-P-nu ») n'est joué que sur ces quatre lignes :
     projection et certificat calculés sur les lois que la carte a réalisées. Sur les 25 autres lignes, les cartes sont sans
     mémoire : la garde accepte tout et les trois formes coïncident (essai sain).
   - *Ce que le gel change* ([CL2] M2). Sous gel : (a) la projection du bloc b reçoit **exactement** les issues des blocs < b,
     et l'empreinte de son journal est écrite avant le tirage du bloc b (les issues fraîches sont tirées bloc par bloc, dans
     l'ordre, du même générateur) ; (b) le numérateur de W^reste est **la carte gelée** (même statistique que la projection) ;
     (c) **une promotion sous gel porte sur la carte gelée, pas sur la carte soumise** : elle ne vaut que comme contrôle de
     validité ; J9, sur les mêmes lignes, juge la carte réelle ; adopter cette forme serait une question de sens, pour le nœud.
     J9-P-nu, lui, lit par définition des lois qui dépendent des issues du bloc : c'est l'artefact voulu, déclaré, sur Hs, Hm,
     Hg, H7 seulement.
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
     c'est-à-dire par coupure c du plan gelé ; sa valeur à l'instant t est la borne (`bornes[sel]`) de la coupe que c induit sur
     les t premières instances ([CL2] m7 ; l'identité des coupes change d'un instant à l'autre, pas celle de c). Sans coût de
     plus : les bornes par coupe sont déjà calculées. Elle demande une copie renommée de `detail_morceaux_groupe` qui rend le certificat
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
   - **Ligne « carte qui lit l'historique »** : Hs, Hm, Hg, H7, par J9-P-nu, J9-P avec refus, J9-P avec gel, et, sur Hs, Hm et
     Hg, par J9, J9-D40 et J9-D (valides pour une carte prévisible, [PREUVE] H5). Témoin exact : le rapport de vraisemblance de la
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
| Hs, Hm, Hg | J9, J9-D40, J9-D, J9-P avec gel (carte gelée) | — | — | 4 + 4 + 4 |
| H7 | J9-P avec gel, terme projeté | — | — | 1 |
| Q9a, Q9b | aucun (monde hors du nul) | 6 + 6, **hors de la famille de Holm** | 2 + 2, rapportées | — |

Famille de Holm : 22 + 7 + 28 = **57 cellules** (53 au brouillon 1, recomptées exactes par [CL2] ; 4 de plus pour Hg).
Cellules fatales : 22 + 12 = **34**. Prédiction P2 : 7 + 28 = 35 cellules.

### Répétitions, appariement, ordre du gel

R = 1 000 par ligne. À chaque répétition : le banc tire l'archive, les paramètres de la ligne, 100 instances d'entraînement et
leurs issues, le plan de 200 instances ; **tous les bras construisent et gèlent** leur engagement (et, pour les bras à
projection, leur journal ; sous gel de l'historique, le journal du bloc b avant le tirage du bloc b) ; **ensuite seulement**
les 200 issues fraîches sont tirées du monde, bloc par bloc, d'un générateur distinct ; la
fonction qui bâtit un engagement ne reçoit aucune issue fraîche ([CL] m1). Chaque bras reçoit les mêmes issues, dans un
dictionnaire lié à **son** empreinte (montage de [V1], annexe B). Les mondes du banc ne lisent pas l'historique.

### Graines (R9)

Racine : l'entier de l'empreinte sha256 du texte qui fera foi. `numpy.random.default_rng(numpy.random.SeedSequence(entropy=racine,
spawn_key=…))`, numpy ≥ 1.25 : tout ce qui précède le gel `(i_ligne, r, 0)` ; issues fraîches `(i_ligne, r, 1)` ; essai
d'égalité E0 `(98, r)` ; rééchantillonnage `(99, b)` ; essais E9, EP, ED, mutations et chronométrage `(97, k)`, un k distinct par
essai, liste dans l'addendum ([CL2] m10). i_ligne de 0 à 28 dans l'ordre : Q1 à Q7, V1 à V5 (dose croissante), Q8, Q9a, Q9b,
Hs, Hm, H7, Hg. Manifeste du run (`src/controle_ia/manifeste.py`) : configuration et
empreinte, versions de Python, numpy et scipy, graines, commit, empreintes des fichiers gelés.

### Étapes

0. **Préalables et gel.** Préalables 1 et 2 levés (« Écarts, nœuds… »). Code écrit sous des noms neufs dans
   `src/controle_ia/organisme_idees_juge/` : nul limité, projection par blocs, lecture dense, témoins, banc, lecture gelée (la
   table des critères écrite en code). Essais : **cas sain et artefact pour chaque ligne de la liste d'arrêt et pour la garde
   P4** (R5). Banc de mutations, au moins : certificat de bloc retiré, optimiseur réduit à 3 pas (doit faire promouvoir Q8 ou
   une copie) ; projection calculée sur les issues du bloc ; garde P4 retirée (tuée par H7) ; blocs décalés des instants ;
   minimum sur les familles remplacé par un maximum ; projection sous gel recevant une issue du bloc courant ; W^reste oublié ; famille linéaire oubliée ; coupures de l'archive
   calculées sur les issues fraîches ; tirages différents d'un bras à l'autre ; issues fraîches tirées avant le gel ; rejet par
   famille lu à un instant hors de T₄₀ ; J9-D sans la réunion avec J9 ; seuil d'informativité choisi sur un bras neuf ; mauvais
   bras au numérateur de ρ ; I gardé fixe dans le rééchantillonnage ; **une ligne Q admise dans I** ([CL2] M1) ; ρ⁺ calculé
   sans recalculer I⁺. Toutes tuées pour la raison attendue. **Critère de mort écrit de la mutation « garde P4 retirée »**
   ([CL2] M3, mère) : sur 200 répétitions de H7 aux graines `(97, k)`, le **terme projeté** sans garde promeut au moins 20
   fois ; cas sain de la garde, sur les mêmes 200 répétitions : le terme projeté sous gel promeut au plus 2 fois (un test de
   niveau α ne garantit pas zéro ; exploratoire : 0 sur 13 000, [R-PROJ] § 5). Ce sont des essais du code, jamais lus comme
   résultat ; le juge complet n'entre pas dans ce critère. **Chronométrage** ([CL2] M5, mère) : temps de chaque bras mesuré sur
   20 répétitions d'essai aux graines `(97, k)`, sans lecture de promotion ; durée attendue calculée ; règle de réduction du
   « Coût et durée » appliquée s'il le faut ; temps, nombre de processus, durée attendue et réductions appliqués **inscrits à
   l'addendum**. Contre-lecture du
   code par un sous-agent neuf. **Addendum d'empreintes** scellé.
1. **Contrôles avant jeu** : empreintes conformes ; essais et mutations rejoués ; aucune sortie existante.
2. **Essais d'égalité**, non lus au-delà : **E0** (100 répétitions, archive A0, ligne Q1) : La ≡ J8 à 10⁻¹² nat ; **E9** : J9
   sans ses membres par morceaux (`nul_v9.sans_morceaux`) ≡ J8, valeur pour valeur ; **EP** ([CL2] m4) : sur 50 mondes de
   `essai_projection_commun_v1.py`, le module de projection sans W^reste, avec 𝔽 = famille linéaire, sous-population et coupures
   z_j > c du plan (comme `m3_toutes_coupures`), s'écarte d'au plus 10⁻⁹ nat sur chaque log e de bloc et sur le processus
   minimum ; l'optimiseur (`em_commun`, `_blocs_projection`) est repris octet pour octet, différentiel joint à l'addendum ; **ED** : aux huit
   instants de T₈, la trajectoire de l'engagement jumeau s'écarte de celle de J9 d'au plus 2·10⁻³ nat (deux appels du
   solveur, tolérance 10⁻³ chacun). Un essai manqué arrête tout.
3. **Jeu** : 29 lignes × 1 000 répétitions (sauf réduction inscrite à l'addendum), `nice -n 10`, trois processus au plus sur
   quatre cœurs ; gardes actives à chaque évaluation.
4. **Scellement de la sortie** avant toute lecture ; sortie sous `diag/organisme-idees-juge-v1/`.
5. **Lecture** : lecture gelée, puis lecteur neuf (R13) qui recalcule l'issue de façon indépendante ; audit de symétrie (R4)
   écrit avant le prononcé.
6. **Rapport** à la mère : issue, réserves, nœud. **Aucune adoption.**

### Comparaisons et corrections

Taille : Holm sur 57 cellules. Trois bras primaires (J9-P, La, Ld) : intervalles de ρ ajustés de Bonferroni, I ⊂ {V}. Secondaires et
lignes par lignes : rapportés sans correction ; aucun verdict d'adoption ne peut s'appuyer sur un secondaire seul. Contrôles
appariés : toutes les comparaisons sont sur les mêmes issues.

## Les neuf désaccords de la synthèse

[SYN] § 7 numérote huit désaccords ; l'« avertissement transversal » écrit dans le deuxième fait le neuvième (c'est le compte
de R-2924). Numérotation ci-dessous : celle à neuf ; entre parenthèses, le numéro dans [SYN].

| n° | désaccord | traitement | où |
|---|---|---|---|
| 1 (1) | garde P4 : « vraie au pari plein » ou fausse pour la grammaire du juge | **tranché par une mesure** : lignes Hm, Hg (grammaire, les deux types qui lisent l'historique), H7 (terme projeté : dent ; juge complet : rapporté), sans garde et avec les deux formes de garde ; Hs est aveugle par construction. **Réserve** : H7 est hors grammaire, non vérifiée comme écrivable ; le banc est sans le membre « urne » ; un résultat nul sur Hm et Hg ne montre pas qu'aucune carte de la grammaire n'atteint le trou ; le gabarit des proposeurs de la boucle réelle n'est pas examiné | P12 ; Seuil ; étage 7 |
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
| 3 | moins de 2 lignes informatives parmi les 15 lignes V | **« prix du v9 non reproduit sur ce banc »** (non concluant sur H-1.1 v2) ; les étages 6 à 8 restent lus |
| 4 | principale, dans l'ordre du Seuil ; puis la même lecture sur ρ⁺ (définition gelée de la « Métrique ») | « nuisible » / « regagne » / « ne regagne pas » / « partiel » ; si J9⁺ change le verdict : **« sensible au certificat »**, et c'est le moins favorable des deux qui est retenu |
| 5 | La, Ld | « recouvre » / « ne recouvre pas » / « en partie » ; ρ_Ld ≤ ρ_La par construction |
| 6 | secondaires : La-P contre La ; J9-P contre La ; J9-D40 et J9-D contre J9 | « gain » ou non, avec intervalle ; rapportés |
| 7 | garde P4 (Hs, Hm, Hg, H7) | « nécessaire, montrée sur le terme projeté » / « non éprouvée » (dent du terme projeté de H7 manquée) / « trou atteint par la grammaire » (Hm ou Hg, juge complet sans garde) ; J9-P-nu complet sur H7 : rapporté ; une cellule avec gel « non tenue » relève de l'étage 1 |
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
| une issue fraîche tirée avant le gel ; ou lue par la fonction qui bâtit un engagement ; ou, pour un bras à projection, une issue du bloc b (ou des blocs suivants) reçue par la projection ou le certificat du bloc b. **Exceptions déclarées, et elles seules** : sous gel, la projection du bloc b reçoit exactement les issues des blocs < b, et son empreinte est écrite avant le tirage du bloc b ; J9-P-nu sur Hs, Hm, Hg, H7 seulement | arrêt ; défaut |
| une carte qui lit l'historique arrive à J9-P ou à La-P sans passer par une forme de la garde P4, hors des bras « sans garde » déclarés | arrêt ; défaut |
| un engagement avec `fractions` | arrêt ; défaut (pari plein seulement) |
| un certificat de bloc non calculé, non fini, ou inférieur à 1 − 10⁻⁹ (impossible en théorie : la moyenne certifiée vaut 1 au point projeté, donc au moins 1 en un sommet) | arrêt ; défaut |
| une exception dans une évaluation ; un log W non fini | arrêt du run entier ; aucune lecture partielle ; relance seulement sous un texte ou un addendum neuf |
| monotonie violée : log W de J9, La ou Ld > log W de J8 + 10⁻⁶ à un instant | arrêt ; défaut de code |
| nichage violé : log W de La ou de Ld < log W de J9 − écart résiduel du membre limité − 10⁻⁶ ; ou log W de Ld > log W de La + écart résiduel de La + 10⁻⁶ | arrêt ; défaut de code, ou famille du v9 différente de [PREUVE] § 3 : audit, nœud |
| domination violée : J9 promeut et J9-D40 ou J9-D ne promeut pas | arrêt ; défaut de code |
| plus de 1 % des évaluations avec un écart résiduel > 2·10⁻³ nat | rapporté ; le run va à son terme |
| chronométrage de l'étape 0 absent de l'addendum ; ou durée attendue > 32 heures après toutes les réductions permises | pas de jeu ; texte neuf |
| une réduction de répétitions hors de la règle écrite, ou décidée après une lecture | run invalide |
| durée murale > 48 heures | arrêt ; run invalide, aucune lecture |
| une lecture avant le scellement de la sortie | run invalide |
| toute dépense, instance payante, appel réseau ou appel de modèle | interdit (R-2851) |

## Coût et durée

**Processeur seul, 0 dollar.** Machine de la session : 4 cœurs, partagée.

**Estimation actuelle** ([CL2] M5, mesure du contre-lecteur sur cette machine, code du v9 sur `94bfd92`, archive de 4 lois,
3 essais) : v9 0,9 à 2,2 s par évaluation à T₈ et 4,4 à 5,7 s à T₄₀ ; avec les autres bras, **7 à 9 s par répétition** ;
29 000 répétitions : environ 56 à 73 heures d'un cœur, **19 à 24 heures sur trois processus**, plus si la machine est chargée.
L'estimation du brouillon 1 (2,5 à 3 s, d'après la note `4d3a6d1c…`, autre montage) était trop basse d'un facteur 3 à 4.

**Chronométrage à l'étape 0, inscrit à l'addendum.** Temps de chaque bras mesuré sur 20 répétitions d'essai (graines
`(97, k)`), sans lecture de promotion. **Durée attendue** D = (somme, sur les lignes et les bras, du temps mesuré × nombre de
répétitions) / 3 processus. Le plan doit tenir sous **48 heures** murales : on exige **D ≤ 32 heures** (marge de moitié pour la
charge des autres sessions).

**Règle de réduction, écrite d'avance.** Si D > 32 heures, les réductions suivantes sont appliquées **dans cet ordre**, chacune
en entier, jusqu'à D ≤ 32 heures ; elles sont décidées sur le seul chronométrage, **avant tout jeu**, et inscrites à l'addendum :
1. strate descriptive « sans membres log-linéaires » supprimée ;
2. engagement jumeau à 40 instants (J9-D40, J9-D, J9-Dc) sur les 15 lignes V : 500 premières répétitions ;
3. le même : 250 premières répétitions ;
4. lignes Q9a et Q9b (protection, hors de Holm, rapportées) : 500 premières répétitions ;
5. La-P sur les 15 lignes V : 500 premières répétitions.
**Jamais réduits** : les 57 cellules de la famille de Holm et les cellules fatales (toutes à 1 000) ; J8, J9, J9-P, La, Ld sur
les 15 lignes V (principale et primaires) ; les dents. Un secondaire réduit est lu, apparié, sur ses seules premières
répétitions, avec son intervalle ; c'est dit au rapport. Si D > 32 heures après la réduction 5 : **pas de jeu, texte neuf**.
Aucune réduction après le début du jeu.

**Borne dure : 48 heures murales** (précision de la mère ; [CL2] proposait de garder 72 heures : non retenu). Écriture du code,
essais, mutations, contre-lectures : temps d'agents, sans dépense. Aucune machine louée.

## Écarts, nœuds et ce que l'essai ne décide pas

- **Préalable 1 (mère)** : [V9] vient du commit `a41b7b5` du dépôt tiers ; la copie du juge est au commit `94bfd92`. La
  compatibilité de `nul_v9.py` avec les modules `nul_filles_v2`, `nul_v8`, `selection_pari` et `outils` de `94bfd92` **n'est pas
  établie par empreinte** (les dépendances au commit `a41b7b5` ne sont pas au dépôt). `test_nul_v9.py`
  (`d42a50eb4ba9691e75e82fa4bc714a925615da80df22227fee730392015999b9`) charge, au niveau du module,
  `demonstrations/banc_tricheurs_v9.py`, absent des deux copies ([CL2] M6). **Je n'ai pas pu le verser** : l'objet `a41b7b5`
  n'est pas dans ce dépôt (`git cat-file` échoue), et le prendre au dépôt tiers demande un appel réseau, interdit ici ; je n'ai
  donc pas pu vérifier non plus qu'il est sur le `main` du dépôt tiers. La compatibilité s'établit, avant l'addendum, par :
  (a) la présence, dans les modules de `94bfd92`, des 16 noms que `nul_v9.py` emprunte (liste de [CL2], point 9 :
  `nf.InstantsInvalides`, `TYPES_AJUSTES`, `valeurs_ajustees` ; `nul_v8.NulV8Refuse`, `description`, `exiger_membres_ajustes`,
  `membres_archive_v8` ; `sp.Cache`, `EngagementModifie`, `TiragesNonLies`, `calibrer`, `plan_execution_de`, `trajectoire_loi`,
  `trajectoire_numerateur`, `trajectoires`, `verifier_plan_execution`), vérifiée par un essai ; (b) l'essai E9 ; (c) **les essais
  du v9 réécrits dans le banc**, sans `banc_tricheurs_v9.py` (K = 3, dimension 2, α = 0,05 écrits dans l'essai), d'après les
  classes de `test_nul_v9.py` qui n'emploient pas ce banc : `MembresNulV9` (cas sain ; membre absent, altéré ou en trop
  refusé par `exiger_membres_v9`) ; `CertificatMorceaux` (la valeur certifiée domine la vraisemblance de tout monde de la
  famille ; bruit propre au morceau non dominé ; seuil égal à une valeur observée ; référence indépendante par `scipy` sur
  petits échantillons ; valeur atteinte au départ non prise pour une borne ; valeur certifiée sous optimisation tronquée ;
  départ non admissible refusé) ; `EvaluateurV9` (identité avec `evaluer_v2` sans morceaux ; départage des membres ; monotonie
  v9 ≤ v8 sur les mêmes issues ; gardes d'engagement et de tirages ; membre inconnu refusé) ; et un essai du banc : copie
  `si_sinon` et copie par sous-population à log W ≤ 10⁻⁶ sous le v9. Si la mère verse plus tard `banc_tricheurs_v9.py` du commit
  `a41b7b5`, empreinté, les essais d'origine sont rejoués en plus. Sinon : pas de jeu. (Essai de fumée de [CL2], point 9 :
  compatibilité plausible, non établie.)
- **Préalable 2 (mère)** : une pièce « preuve, version 2 », scellée et contre-lue, qui porte les corrections p1 à p6 de [CL],
  le lemme de la projection par blocs **sous la garde P4**, et la preuve du rejet par famille. Ce texte emploie ces énoncés ;
  il ne les prouve pas.
- **Le banc** ne touche ni le juge de production, ni le v9, ni la boucle : aucun écart à une conception scellée. Différences
  de montage avec la production, comme [BANC-v2] : plan « ordre_naturel » ; issues fraîches tirées par le banc après le gel ;
  et, propre à ce texte : bibliothèque sans le membre « urne » (« Banc », [CL2] m11).
- **Ajouts au banc partagé** : les sept lignes Q8, Q9a, Q9b, Hs, Hm, H7, Hg sont propres à l'idée 1.1 ; le banc B v2 de l'idée 1.2
  n'est pas modifié.
- **Nœud de Lazar — adoption.** Adopter J9-P, La-P, La ou Ld ferait un nul v10 ; adopter J9-D40 change `instants_lecture` ;
  adopter J9-D change la règle de lecture et ne se branche pas sur e-BH. Chaque adoption est une modification du juge, avec
  sa validation scellée. **Ce plan n'en décide aucune.** Pour J9-P, l'adoption demanderait en plus ([R-PROJ] § 9) : la garde
  P4 dans le juge (rétrécissement de ce qu'il accepte aujourd'hui) ; la règle de marge des filles redéfinie ou laissée au
  maximum ; l'audit « près de 1 » ; l'optimiseur gelé sous l'empreinte ; le pari à fraction abandonné ou gelé par bloc.
- **Ne décide pas** : la question de sens (une copie par sous-population est-elle une découverte ?) ; la puissance sur les
  mondes riches à 8 traits (le nombre de coupures, donc de familles de J9-P, y grandit) ; le contrôle d'erreur entre
  générations et le branchement sur e-BH ; la réserve log-linéaire du v8 ; la projection à blocs plus petits que 25 ; les
  cartes à pari à fraction ; l'existence d'une carte de la grammaire qui atteint le trou de P4 au-delà de Hm et Hg ; le
  comportement de J9-P avec le membre « urne » ; toute
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
- **Contre-lecture 2** (R2, sur le brouillon 1 de la version 2) — sous-agent neuf, qui n'a écrit ni le brouillon, ni [SYN], ni
  les rendus des angles ; texte relu : `docs/notes/organisme-idees-juge-v1/organisme-idee-1-1-poids-du-nul-v2-brouillon1.md`,
  `916985cec9ba027effa9fdcf4bf70827424a838ed875358ae213dc1f60d30b55` ; rapport :
  `docs/notes/organisme-idees-juge-v1/contre-lecture-idee-1-1-v2-brouillon1-v1.md`,
  `d5e71f6c7ee41600a207255614685c303ecca68aecdf457291eaf9a6d6571c4b`. Verdict : « scellable après corrections » (6 majeurs,
  14 mineurs). **Traitement**, point par point :
  - M1 (I non restreint aux vraies découvertes) : **acceptée** — I ⊂ {15 lignes V} à la « Métrique », rappelé en tête des
    prédictions, à l'étage 3 et aux « Comparaisons » ; mutation « une ligne Q admise dans I ».
  - M2 (garde P4 et liste d'arrêt) : **acceptée** — ligne d'arrêt réécrite selon le rapport, avec ses deux exceptions
    déclarées ; issues tirées bloc par bloc ; numérateur de W^reste sous gel = la carte gelée ; « une promotion sous gel porte
    sur la carte gelée » écrit à la garantie et au bras 3 ; mutation « projection sous gel recevant une issue du bloc courant ».
  - M3 (témoin H7, mutation, Hs aveugle) : **acceptée**, avec les précisions de la mère — sur H7, terme projeté (dent, témoin
    de code) séparé du juge complet (rapporté, sans seuil) ; critère de mort écrit de la mutation « garde retirée » (au moins
    20 sur 200 sans garde) ; Hs dite aveugle ; ligne **Hg** ajoutée (Holm à 57, P2 à 35, seuils recalculés : inchangés).
    **Écart au rapport** : le cas sain sous gel est « au plus 2 sur 200 » et non « 0 fois » (un test de niveau α ne garantit
    pas zéro).
  - M4 (J9⁺ non défini) : **acceptée** — ρ⁺ et I⁺ définis selon le rapport ; mutation « ρ⁺ sans recalculer I⁺ ».
  - M5 (durée) : **acceptée**, avec les précisions de la mère — estimation refaite ; chronométrage à l'étape 0 inscrit à
    l'addendum ; exigence D ≤ 32 heures ; règle de réduction écrite d'avance ; trois processus. **Refusé en partie** : la borne
    dure passe à 48 heures (précision de la mère), au lieu des 72 heures que le rapport gardait ; et un dépassement après les
    réductions permises reste « texte neuf », comme le rapport le demande.
  - M6 (seconde route du préalable 1) : **acceptée par la voie « à défaut »** — le fichier manquant n'a pas pu être versé
    (commit absent de ce dépôt, appel réseau interdit) ; liste des 16 noms, essai E9 et liste écrite des essais du v9 réécrits.
  - m1 (en-tête) : **acceptée** (têtes, heures, compagnons). m2 (annexe A au dépôt) : **acceptée** — script et sortie versés
    avec leurs compagnons. m3 (deux pondérations) : **acceptée**. m4 (essai EP) : **acceptée** — forme du rapport, optimiseur
    repris octet pour octet. m5 (un seul seuil d'audit) : **acceptée**. m6 (quantité fatale de J9-D) : **acceptée**. m7
    (J9-Dc) : **acceptée**. m8 (« 26 partitions ») : **acceptée**. m9 (Q9b) : **acceptée**. m10 (graines des essais) :
    **acceptée**. m11 (montage sans « urne ») : **acceptée**. m12 (« sans rouvrir aucune copie ») : **acceptée**. m13
    (`moyenne_glissante` dans W^reste) : **acceptée**. m14 (cette entrée) : **acceptée**.
- **À venir** : contrôle du seul différentiel brouillon 1 → brouillon 2 par un sous-agent neuf. **Fichiers à lui donner
  explicitement** : ce texte ; [B1] ; [CL2] ; et, pour les points de fond, [R-PROJ] § 5, `selection_pari.py` et `cycle.py`
  (l. 312 à 330) de la copie `94bfd92`, `test_nul_v9.py`. Questions à trancher : compte de Holm à 57 ; règle de réduction
  (ordre, seuil de 32 heures, ce qui n'est jamais réduit) ; cas sain « au plus 2 sur 200 » ; liste des essais réécrits du v9 ;
  la ligne Hg telle qu'écrite (`valider_loi` l'accepte-t-elle avec ces champs). Puis scellement par `sceller_prereg` et recopie
  sous `prereg/`.

## Annexe A — seuils (compte seul, sans donnée, sans juge)

Script `docs/notes/organisme-idees-juge-v1/organisme-idee-1-1-poids-du-nul-v2-outils/seuils_idee_1_1_v2_brouillon2.py`
(`91fd1d11ec4b4ebeb19257209ea1d96a62d67e0f211c071ef0173a0ee044ecda`) et sortie `…/sortie-seuils-idee-1-1-v2-brouillon2.txt`
(`4e508c64f7cc5e352556fbba473cd6759e444b16f7739e0b4d8d0ad660b672f2`), versés avec leurs compagnons et recopiés en entier. Le
script du brouillon 1 (`d7408ee146824ce9150d8f644d750093ac75fe6a0e1bb60fef5d73373bce83f3`, recopié en entier dans [B1], rejoué à
l'octet par [CL2]) n'en diffère que par la famille de 57 cellules ajoutée et son titre :

```
taille, 53 cellules, niveau le plus strict (0,05/53) : tenue si <= 29 ; non tenue si >= 74
taille, 53 cellules, niveau le moins strict (0,05) : tenue si <= 38 ; non tenue si >= 63
taille, 57 cellules, niveau le plus strict (0,05/57) : tenue si <= 29 ; non tenue si >= 74
taille, 57 cellules, niveau le moins strict (0,05) : tenue si <= 38 ; non tenue si >= 63
borne basse unilatérale à 95 % > 0.5 : à partir de 527 sur 1000 (borne 0.5005)
borne basse unilatérale à 95 % > 0.05 : à partir de 63 sur 1000 (borne 0.0508)
borne basse unilatérale à 95 % >= 0.02 : à partir de 29 sur 1000 (borne 0.0208)
```

```python
"""Seuils du préenregistrement de l'idée 1.1, version 2, brouillon 2 (compte seul, sans donnée, sans juge).
(1) Cellules de taille : test binomial exact au taux 0,05 sur 1 000 répétitions, au niveau le plus strict de Holm
    (0,05/m) et au moins strict (0,05), pour m cellules.
(2) Dents : plus petit nombre de promotions sur 1 000 dont la borne basse de Clopper-Pearson unilatérale à 95 % dépasse
    0,5, puis 0,05.
(3) Ligne informative : plus petit nombre de paires discordantes sur 1 000 dont la même borne basse atteint 0,02."""
from scipy.stats import beta, binom

n = 1000
for m in (53, 57):
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
(`966dd9dc3fae61cbe1f10ee2a54f401ddf7af5041eeaacd81ad9f8b264661589`), section 6. Empreintes des quatre PDF recalculées par moi le 15
novembre, égales ; contenu non relu ; aucun chiffre n'en est tiré. Aucune revendication n'est faite ici.
