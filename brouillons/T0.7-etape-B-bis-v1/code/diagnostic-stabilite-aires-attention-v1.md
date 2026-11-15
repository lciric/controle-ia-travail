# Stabilité des scores et des aires des sondes « attention » sous les arrondis (étape B bis de T0.7), v1

**Déclaration** : réponse aux deux questions de la mère après le diagnostic consigné (R-2902) ; même développeur que
`diagnostic-ecart-attention-carte-v1.md` (`5ecb9235…`), qui n'a écrit aucun autre fichier de B bis ; **processeur seulement** ;
**données synthétiques seulement** (le jeu de la répétition, mêmes tirages, mêmes graines ; un jeu tenu à l'écart de même loi ;
des variantes déclarées du seul décalage du signal) ; aucune donnée ni sortie de 7a, 7b, T0.7 ou P3-bis ; rien sous `diag/`,
`donnees/`, `docs/verdicts/` ; aucune machine, aucune dépense ; ni le code (`src/`, `tests/`, `scripts/`) ni le texte de B bis
(brouillon 3, `f104917f…`) ne sont modifiés ; aucun brouillon 4 n'est écrit (les couples du § 6 sont une proposition).
**Date (UTC)** : 2026-11-15. Empreintes au § 8 ; tout chiffre renvoie à une sortie scellée.

## Réponse à la question 1, en cinq lignes

1. **Scores, sans signal** (jeu de la répétition ; les sondes n'apprennent rien qui se généralise, aire « attention » 0,46) :
   entre piles réelles, écart du contrôle **1,10 à 1,47**, écart absolu médian 0,17 à 0,23 (scores jusqu'à 6 environ),
   corrélation de rangs **0,978 à 0,988** ; un seul arrondi au premier pas : écart ≤ 1,1·10⁻⁶, rangs inchangés (1,000000) ;
   10⁻¹⁰ au premier pas : 0,045 à 0,44, rangs ≥ 0,998.
2. **Aires, sans signal** : 0,4608 à 0,4682 ; entre quatre piles, étendue **0,0074**, écart type 0,0030 (0,0015 sur les 13
   membres) ; un arrondi : 0 ; 10⁻¹⁰ au premier pas : étendue 0,0012. Linéaire (témoin) : 13 aires égales (0,5186).
3. **Avec un signal** (même jeu, seul le décalage des positifs change) : aires « attention » 0,558, 0,817, 0,983 ; entre quatre
   piles, étendue **7,8·10⁻⁵, 0, 0**, rangs 1,00000 ; écart du contrôle 3,2·10⁻⁵ à 4,0·10⁻² au signal faible (la seule
   réduction torch contre numpy dépasse 10⁻⁴), au plus 1,9·10⁻⁵ au décalage 4 et 1,5·10⁻⁹ au décalage 8.
4. **Devant le texte** : erreur type d'une aire sur ce jeu 0,005 à 0,023 ; seuil d'ex aequo 0,005 ; aire minimale détectable
   Q + 0,071 ; DD ≥ 0,036 : la dispersion est **négligeable dès que la sonde lit un signal** ; sans signal, 0,0074 dépasse le
   seuil d'ex aequo (le réglage retenu peut changer) mais touche une sonde au hasard (« non au-dessus ») : aucune lecture n'en
   dépend.
5. **Conséquences** : la mesure (c) n'est pas nécessaire (couples non proposés) ; la réserve R-PILE suffit ; l'arrêt de la
   répétition tient à un jeu **sans signal apprenable** (avec signal, le contrôle à 300 époques passerait entre piles du
   processeur) ; une cellule de la course sans signal ou à signal faible le referait : l'option 1 (3 époques) reste recommandée.

## 1. Protocole

- **Sondes** : réglage de la répétition (couche 15, l2 = 10⁻³, 300 époques, pas 0,05), familles « attention » et « linéaire »
  (témoin), apprises sur les 640 actions de la répétition.
- **Membres comparés** (13 par famille) : *piles réelles* — P0 paquet gelé (AVX-512, réduction numpy), P1 paquet gelé en AVX2, P2
  chemin v1 (réduction torch), sondes du premier diagnostic relues par leurs empreintes scellées ; S0 : le même calcul mené en
  colonne d'un produit matriciel (autre arithmétique des produits, autre pile, déclarée) ; *un seul arrondi au premier pas* —
  U1 à U5 : après le premier pas d'Adam, une coordonnée de w (tirée) remplacée par le flottant suivant ; *perturbation de la taille
  d'un écart de piles au premier pas* — R1 à R5 : après le premier pas, w ← w·(1 + 10⁻¹⁰·ξ), ξ gaussien (l'écart entre deux piles
  réelles après un pas est de 1,4·10⁻¹⁰ à 2,8·10⁻¹⁰, premier diagnostic, § 5). U et R sont des colonnes du même calcul que S0
  (perte moyenne par colonne, pénalité par colonne, Adam élément par élément : aucun couplage entre colonnes).
- **Jeu tenu à l'écart** : 640 actions (320 positives), 144 364 jetons, **même loi** que l'apprentissage (même direction u, relue et
  vérifiée par la première action de la répétition ; bruit et longueurs tirés sous la clé `bbis/repetition/tenu-a-l-ecart`). Les
  256 actions de contrôle de la répétition ne servent pas : leur direction u est autre.
- **Mesures** : par paire, écart du contrôle max |a − b| / max(|b|, 1), écart absolu médian des scores, corrélation de rangs de
  Spearman, écart d'aire (Mann-Whitney, `sondes.evaluation.aire_sous_courbe`) ; par groupe, étendue et écart type des aires ;
  erreur type d'échantillonnage de l'aire sur ce jeu (Hanley et McNeil), pour l'échelle.

## 2. Résultats sur le jeu de la répétition (`diagnostic-stabilite-aires-attention-v1-sortie.json`)

| paire | écart du contrôle | écart absolu médian | Spearman | écart d'aire |
|---|---|---|---|---|
| attention, P1 (AVX2) contre P0 | 1,10 | 0,170 | 0,9881 | −0,0074 |
| attention, P2 (réduction torch) contre P0 | 1,47 | 0,226 | 0,9782 | −0,0043 |
| attention, S0 (produit matriciel) contre P0 | 1,42 | 0,227 | 0,9789 | −0,0041 |
| attention, U1 à U5 (un arrondi) contre S0 | 3,9·10⁻⁷ à 1,1·10⁻⁶ | 1,3·10⁻⁸ à 3,9·10⁻⁸ | 1,000000 | 0 |
| attention, R1 à R5 (10⁻¹⁰ au premier pas) contre S0 | 0,045 à 0,44 | 8,0·10⁻⁴ à 0,072 | 0,9980 à 0,99998 | −0,0003 à −0,0012 |
| linéaire, P1, P2, S0 contre P0 | 1,4·10⁻¹² à 6,1·10⁻⁸ | ≤ 10⁻⁸ | 1,000000 | 0 |
| linéaire, U et R contre S0 | ≤ 2,1·10⁻⁸ | ≤ 4,4·10⁻⁹ | 1,000000 | 0 |

Aires « attention » : P0 0,4682 ; P1 0,4608 ; P2 0,4639 ; S0 et U1 à U5 0,4641 ; R1 à R5 0,4629 à 0,4638. **Dispersion** : piles
(P0, P1, P2, S0) étendue **0,0074**, écart type 0,0030 ; un arrondi : 0 ; 10⁻¹⁰ au premier pas : étendue 0,0012, écart type
0,0005 ; les 13 : étendue 0,0074, écart type 0,0015. Linéaire : les 13 aires égales (0,5186). Erreur type d'échantillonnage de
l'aire sur ce jeu : 0,0228.

**Limite qui domine la lecture** : sur ce jeu, **aucune sonde ne se généralise** (attention 0,46, linéaire 0,52 sur le jeu tenu à
l'écart ; perte d'apprentissage de l'attention 0,0018 : mémorisation). La dispersion ci-dessus est celle de sondes ajustées au
bruit. D'où la variante du § 3.

## 3. Variante à signal (même jeu, seul le décalage change ; déclarée)

Sur la direction dense u de la répétition, la sonde « attention » ne se généralise pas, même à décalage 1 ou 2 au calibrage
(aires 0,567 et 0,558), ni sur le premier axe à décalage 2 (0,529, `diagnostic-stabilite-aires-attention-signal-v2-sortie.json`) :
Adam avance chaque coordonnée au même pas, et sur 4 096 dimensions le bruit l'emporte tant que le signal par coordonnée est
faible. Le décalage est donc porté à 2, 4 et 8 sur la direction u (programme `diagnostic-stabilite-aires-attention-signal-v1.py`,
mêmes tirages, mêmes graines, mêmes longueurs ; au décalage 0,5, il redonne la sonde du premier diagnostic au bit près, essai) ;
membres : les quatre piles réelles P0 (gelé, AVX-512), P1 (gelé, AVX2), P2 (chemin v1, réduction torch), P3 (chemin v1, AVX2).

| décalage | aire « attention » (P0) | étendue des 4 aires | écart du contrôle P1 / P2 / P3 contre P0 | rangs | erreur type |
|---|---|---|---|---|---|
| 0,5 (répétition, § 2) | 0,468 | 0,0074 | 1,10 / 1,47 / — (S0 : 1,42) | 0,978 à 0,988 | 0,023 |
| 2 (signal faible) | 0,558 | 7,8·10⁻⁵ | 3,2·10⁻⁵ / 4,0·10⁻² / 4,0·10⁻² | 1,00000 | 0,023 |
| 4 | 0,817 | 0 | 5,1·10⁻⁸ / 1,2·10⁻⁸ / 1,9·10⁻⁵ | 1,00000 | 0,017 |
| 8 | 0,983 | 0 | 6,0·10⁻¹⁰ / 1,5·10⁻⁹ / 1,1·10⁻⁹ | 1,00000 | 0,005 |

Linéaire au décalage 4 (témoin) : aire 1,000 pour trois piles, écarts ≤ 1,4·10⁻¹³. (Au décalage 8, la marche de la linéaire a été
arrêtée avant tout apprentissage, par gain de temps ; aux décalages 2 et 8, la linéaire n'est pas rejouée.)

**Lecture** : l'instabilité aux arrondis de l'apprentissage « attention » est celle d'une sonde qui **mémorise le bruit** ; dès
qu'un signal se lit, les quatre piles rendent la même aire, et l'écart des scores tombe sous 10⁻⁴ (sauf, au signal faible,
l'écart de réduction torch contre numpy : 4,0·10⁻², quand l'écart des seuls noyaux reste à 3,2·10⁻⁵). Cela précise le premier
diagnostic sans le contredire : sur le jeu de la répétition (sans signal), aucune correction du code ne fait passer le contrôle ;
au signal faible, une réduction identique à celle du paquet gelé (numpy sur le processeur, puis transfert) suffirait peut-être
(écart des noyaux seuls 3,2·10⁻⁵ ici), sans garantie sur la carte.

## 4. La dispersion est-elle petite devant ce que le texte veut lire ?

Repères du brouillon 3 (`f104917f…`) : seuil d'ex aequo du choix du réglage **0,005** (plan, point 5, l. 105) ; aire minimale
détectable des cellules décisives **Q + 0,071 à 0,072** (« Puissance », l. 203) ; écart minimal à 99 % des différences appariées
**0,036 à 0,108** (l. 205) ; déplacement détectable des réserves à 95 % **≈ 0,554** contre 0,5 (l. 206). Erreur type d'une aire
sur le jeu tenu à l'écart (320 contre 320) : 0,005 à 0,023 selon l'aire.

- **Avec signal** (aires 0,56 à 0,98) : étendue ≤ 7,8·10⁻⁵, soit moins d'un soixantième du seuil d'ex aequo et environ un
  millième de l'aire minimale détectable : **négligeable** ; ni le choix du réglage, ni une borne, ni un état ne peuvent en
  dépendre, sauf à une coïncidence de l'ordre de 10⁻⁴.
- **Sans signal** (aire 0,46) : étendue 0,0074, écart type 0,0030 : un tiers de l'erreur type, un dixième de l'aire minimale
  détectable, mais **plus que le seuil d'ex aequo** : entre deux piles, le réglage retenu dans une cellule sans signal peut
  changer ; la lecture de cette cellule (« non au-dessus du plancher ») ne change pas.
- **Limite** : ces régimes sont ceux d'un bruit gaussien isotrope ; de vraies activations peuvent mêler un signal faible et une
  forte mémorisation (cas non mesuré ici) ; les sondes « attention » à aire voisine de 0,5 sont celles dont l'aire bouge.

## 5. Ce que coûterait sur la carte la mesure de stabilité (c)

La mesure (c) n'est pas proposée (dispersion négligeable là où elle compterait). Pour mémoire, son coût sur la carte, si Lazar
la voulait : pour chaque sonde finale et chaque sonde d'ENC dont le réglage retenu est « attention » (au plus 10 + 10), 7
réapprentissages sous des arithmétiques équivalentes disponibles sur la carte (réduction torch ou numpy × Adam multi-tenseurs ou un
tenseur à la fois × produit vecteur ou matrice à deux colonnes ; les variantes au premier pas sont écartées : un arrondi ne
change rien, et 10⁻¹⁰ sous-estime l'écart des piles, étendue 0,0012 contre 0,0074), soit au plus 140 apprentissages × 3,5 s
(durée d'un apprentissage « attention » sur la carte à la répétition, `repetition-carte.json`) ≈ 0,14 h, plus leur notation
(celle de 140 sondes de plus, à comparer aux 8 000 directions et 1 000 sondes du nul que le devis note en 0,2 à 0,4 h : ≤ 0,06 h) : **≈ 0,2 h
de carte, ≈ 0,2 à 0,3 USD** (1,09 à 1,40 USD de l'heure ; `devis-etape-b-bis-v3.md`), et 140 apprentissages de plus à la
garde de débit (2 460 → 2 600, + 6 %, ≈ 0,13 h projetées à la médiane de 2,77 s). Aucune dépense n'est engagée ici.

## 6. Couples « ancien / nouveau » proposés pour un brouillon 4 (question 2)

Vérifiés par `diagnostic-stabilite-aires-attention-v1-couples.py` (chaque « ancien » présent exactement une fois dans le brouillon 3
`f104917f…` ; couples appliqués en mémoire seulement ; texte qui en résulterait : `a7a0315b…`, non écrit ; sortie
`diagnostic-stabilite-aires-attention-v1-couples-sortie.txt`). Groupe (a) : option 1 ; groupe (b) : réserve R-PILE ; **(c)
non proposé** (§ 4). Le code (`validation_imbriquee_v2`, clés de graines) suivrait le mot de Lazar ; rien n'est écrit ici.

#### a1 plan, point 5

**Ancien** :

> **contrôle à la marche** : un (cellule, pli) tiré par graine est réappris sur le processeur par `sondes.familles` ; écart relatif maximal des scores sur 256 actions tirées ≤ 10⁻⁴, sinon arrêt (erreur de chaîne).

**Nouveau** :

> **contrôle à la marche** : un (cellule, pli) tiré par graine est réappris sur le processeur par `sondes.familles`, depuis le même départ (mêmes graines que la marche), à la couche et à la régularisation retenues pour ce couple, **dans les deux familles** : la linéaire à 300 époques, l'attention à **3 époques** (`Reglages(epoques=3)`, les mêmes trois époques réapprises sur la carte) ; écart relatif maximal des scores sur 256 actions tirées ≤ 10⁻⁴ pour chacune, sinon arrêt (erreur de chaîne) ; la sonde « attention » de 300 époques du couple est réapprise une seconde fois sur la carte et doit être égale à la première au bit près (déterminisme), sinon arrêt. Raison, écrite avant toute lecture : quand la sonde « attention » n'apprend rien ou presque, ses 300 époques amplifient les écarts d'arrondi entre deux piles de calcul au-delà de 10⁻⁴ (sans signal : 0,633 pour le paquet gelé contre lui-même sous un autre jeu d'instructions du processeur, 2,131·10⁻² entre la carte et le processeur à la répétition du 15 novembre ; signal faible : 4,0·10⁻²) ; avec un signal, non (au plus 1,9·10⁻⁵) ; à 3 époques, l'écart entre deux piles reste de 2,9·10⁻⁷ à 5,9·10⁻⁷ même sans signal (`brouillons/T0.7-etape-B-bis-v1/code/diagnostic-ecart-attention-carte-v1.md`, `5ecb9235…` ; `brouillons/T0.7-etape-B-bis-v1/code/diagnostic-stabilite-aires-attention-v1.md`).

#### a2 liste d'arrêt

**Ancien** :

> - Contrôle carte-processeur de l'apprentissage au-delà de 10⁻⁴ : arrêt (erreur de chaîne) ;

**Nouveau** :

> - Contrôle carte-processeur de l'apprentissage au-delà de 10⁻⁴ (linéaire à 300 époques, attention à 3 époques ; plan, point 5), ou sonde « attention » du couple non déterministe sur la carte : arrêt (erreur de chaîne) ;

#### a3 code neuf

**Ancien** :

> `validation_imbriquee_v1` (plis, grille, sélection, sonde finale, nul de réétiquetage, ENC, garde de débit)

**Nouveau** :

> `validation_imbriquee_v2` (plis, grille, sélection, sonde finale, nul de réétiquetage, ENC, garde de débit ; contrôle carte-processeur aux deux horizons du point 5 et déterminisme de la sonde « attention » du couple ; la v1 reste, R12)

#### a4 épreuves

**Ancien** :

> (activations décalées) ; égalité carte-processeur ; garde de débit

**Nouveau** :

> (activations décalées) ; égalité carte-processeur (linéaire à 300 époques, attention à 3 époques ; artefacts : autre graine, poids altérés de 1 % ; déterminisme : cas sain et artefact) ; garde de débit

#### b1 qualifications

**Ancien** :

> **R-G3** (marque de la table A), audit R4 et ses motifs.

**Nouveau** :

> **R-G3** (marque de la table A), **R-PILE** (écrite dès qu'une sonde finale lue est de la famille « attention » : « sonde « attention » reproductible au bit près sur la même pile de calcul seulement (carte, pilote, versions de torch et de numpy) ; sur une autre pile, l'apprentissage peut rendre une autre sonde, surtout quand elle n'apprend rien » ; sur données synthétiques de la taille de la course, entre quatre piles de calcul, aires d'une sonde « attention » qui n'apprend rien (aire 0,46) d'étendue 0,0074, et d'étendue au plus 7,8·10⁻⁵ pour des sondes qui apprennent un signal (aires 0,56 à 0,98) ; `brouillons/T0.7-etape-B-bis-v1/code/diagnostic-stabilite-aires-attention-v1.md`), audit R4 et ses motifs.

#### b2 section D

**Ancien** :

> (6) le libellé d'information (lettre de R-2716) ne dit pas « plafond tient » : seul le libellé « lecture dure », retenu, écarte de façon établie l'adaptateur seul et retient la condition « muette sur le jumeau ».

**Nouveau** :

> (6) le libellé d'information (lettre de R-2716) ne dit pas « plafond tient » : seul le libellé « lecture dure », retenu, écarte de façon établie l'adaptateur seul et retient la condition « muette sur le jumeau » ; (7) une aire de la famille « attention » est celle d'**une** sonde parmi celles que rendrait le même apprentissage sous d'autres arrondis (réserve R-PILE) : sur données synthétiques, la dispersion est négligeable quand la sonde apprend un signal, de l'ordre de 0,007 quand elle n'apprend rien ; sur de vraies activations, elle n'est pas mesurée.

## 7. Ce qui reste non éprouvé

- Rien n'est mesuré sur de vraies activations (interdit ici) ni sur la carte ; les régimes « sans signal » et « avec signal »
  sont synthétiques (bruit gaussien isotrope) ; un seul réglage (couche 15, l2 = 10⁻³) ; la stabilité du **choix** du réglage
  (aires de validation interne entre piles) n'est pas mesurée, seulement celle de la sonde à réglage fixé.
- Les colonnes S0, U, R sont une autre arithmétique que le paquet gelé (déclaré) ; la perturbation 10⁻¹⁰ au premier pas
  sous-estime l'effet des piles réelles (§ 2), elle n'en est pas un substitut.
- Aux décalages 2 et 8, la linéaire n'est pas rejouée ; au décalage 1, calibrage seul ; le jeu tenu à l'écart est unique
  (640 actions) : les écarts d'aire entre membres sont appariés, l'erreur type n'est donnée que pour l'échelle.

## 8. Fichiers et empreintes

Fichiers ajoutés dans `brouillons/T0.7-etape-B-bis-v1/code/`, chacun avec son compagnon `.sha256` (aucun fichier existant
modifié ; `src/`, `tests/`, `scripts/` et le brouillon 3 inchangés ; suite de B bis : 138 passés au dernier passage,
`essais-sortie-diagnostic-ecart-attention-v1.txt`, code inchangé depuis) :

| fichier | sha256 |
|---|---|
| `diagnostic-stabilite-aires-attention-v1.py` (colonnes (S0, U, R) et évaluation sur le jeu tenu à l'écart) | `e8a04efa94515901d7f86ae961d4a205a40e7c8cd7571a54434c1cb54be629a8` |
| `diagnostic-stabilite-aires-attention-v1-sortie.json` (§ 2 (empreintes de P0 à P2 vérifiées contre `2c7d9f23…`)) | `b05db392e7cd7abc5a2554813d57505e36cf2db0d4181aa467e0f3bd784d9b22` |
| `diagnostic-stabilite-aires-attention-signal-v1.py` (variante à signal dense) | `f2385651200ff428a181aa378796422beab7605f1c691c2779ce1ea1315ddb71` |
| `diagnostic-stabilite-aires-attention-signal-v1-sortie.json` (§ 3 (décalages 1, 2, 4, 8)) | `076be4a82c177bc44f577cf00a1cba9d4ec1738774e15a02616852a4a507cbd4` |
| `diagnostic-stabilite-aires-attention-signal-v2.py` (variante à signal sur un axe) | `fee59624d09187b4335e4055d66b6846319906ae02343ef3027dc719c703ae5c` |
| `diagnostic-stabilite-aires-attention-signal-v2-sortie.json` (§ 3 (calibrage sur l'axe)) | `cabb9370ae903e80e688fb2be65d154602a178fcc53bdba0f6e344c4e8e84060` |
| `diagnostic-stabilite-aires-attention-v1-couples.py` (§ 6 (vérification des couples, aucun texte écrit)) | `bd8d39482eadd954c985d19d475a319236bd417f7f1850ef7b6a34259c7f6d05` |
| `diagnostic-stabilite-aires-attention-v1-couples-sortie.txt` (§ 6) | `fd8fd0bf59cd168373a0fdd111b0bd5ec5354c72524b7bccc4facf4db1f669eb` |
| ce rapport | son compagnon `diagnostic-stabilite-aires-attention-v1.md.sha256` |

Paramètres des sondes (`.npz`) non versés : leurs empreintes sont dans les sorties. Durées : colonnes « attention » 31 min,
« linéaire » 12 min ; un apprentissage du paquet gelé 3 à 15 min selon la charge de cette machine partagée.
