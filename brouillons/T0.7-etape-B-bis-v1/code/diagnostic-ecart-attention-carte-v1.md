# Diagnostic de l'écart carte-processeur de la famille « attention » (répétition sur carte de l'étape B bis, 15 novembre), v1

**Déclaration** : rédigé par un développeur neuf, qui n'a écrit aucun fichier de l'étape B bis ; sans vue des données de 7b ;
aucune sortie de 7a, 7b, T0.7 ou P3-bis lue ; rien lu ni écrit sous `diag/`, `donnees/`, `docs/verdicts/` ; aucune entrée de 7a
ou 7b ; aucune machine, aucun appel payant, aucune dépense ; **processeur seulement**, sur les **données synthétiques de la
répétition** (mêmes tirages, mêmes graines) ; aucune aire calculée.

- **Date (UTC)** : 2026-11-15. **Branche** : `prep/t07bbis-code-v1`, partie de `95cfada6`.
- **Traces lues** : branche `calcul/t07bbis-repetition-v2`, commit `3528a2e8` (parent `95cfada6`),
  `traces/bbis-t07-repetition-v1/` (`repetition-carte.json`, `carte.txt`, `carte-resume.txt`, `journal-repetition.txt`,
  `essais.txt`, `nvidia-smi*.txt`, `pip-freeze.txt`).
- **Pièces de ce diagnostic** (même dossier, chacune avec son compagnon `.sha256`) : scripts
  `diagnostic-ecart-attention-carte-v1.py` et `diagnostic-trajectoires-attention-carte-v1.py` ; sorties
  `diagnostic-ecart-attention-carte-v1-sortie.json` et `diagnostic-trajectoires-attention-carte-v1-sortie.json` ; sortie des
  essais `essais-sortie-diagnostic-ecart-attention-v1.txt`. Empreintes au § 10. Tout chiffre ci-dessous renvoie à ces sorties.

## Verdict

1. **Cause établie (sur processeur)** : ce n'est pas une erreur de chaîne. L'apprentissage « attention » tel que le texte le
   fixe (300 époques d'Adam, pas 0,05, requête q sans pénalité, 640 actions, 4 096 dimensions) **amplifie les écarts d'arrondi
   entre deux piles de calcul** : 10⁻¹⁰ après le premier pas, 10⁻⁴ entre les pas 11 et 21, de l'ordre de 1 vers le pas 50, puis
   0,6 à 1,1 à la fin ; la carte et le processeur ne calculent pas les mêmes arrondis (2,1·10⁻² à la répétition). Le paquet gelé
   lui-même, sur cette machine, sous un autre jeu d'instructions du processeur, s'écarte de lui-même de **0,633** ; la famille
   « linéaire » reste à 10⁻¹² (processeur) et 2·10⁻⁸ (carte).
2. Pistes (a) tirage sur l'appareil, (b) ordre des lots, (c) simple précision, noyau rapide d'attention : **écartées par les
   faits** ; (d) amplification par l'optimiseur et (e) chemins de calcul différents : **ensemble, la cause**.
3. **Aucune correction du code sous le texte ne peut faire passer ce contrôle** : la seule voie serait une arithmétique
   presque identique au bit près à celle du paquet gelé sur le processeur de l'instance (écart sous 10⁻¹⁴ environ au premier
   pas, § 5), que même ce paquet ne tient pas d'un jeu d'instructions à l'autre. **Nœud de Lazar** (§ 7) ; aucun `apprentissage_carte_v2` n'est écrit ; `src/` et `tests/` sont
   inchangés ; une quatrième passe sous le code actuel redonnerait l'arrêt.

## 1. Faits de départ (traces de la répétition)

- `repetition-carte.json` : code 9, état « controle » ; environnement de la carte : A100-SXM4-80GB, pilote 595.91.07, torch
  `2.14.1+cu130`, CUDA 13.0, numpy 2.4.6, algorithmes déterministes vrais, TF32 coupé, cuDNN déterministe, un fil ; 640 actions,
  143 231 jetons, 4 096 dimensions ; réglages `lineaire-c15-l2_0.001` et `attention-c15-l2_0.001` contrôlés ; déterminisme sur la
  carte vrai pour les deux familles (paramètres égaux au bit près entre deux apprentissages).
- Contrôle carte-processeur : « linéaire » écart relatif maximal **1,9539e-08** (256 actions, tolérance 10⁻⁴) ; « attention »
  **2,131e-02** > 10⁻⁴, refus « erreur de chaîne » ; durée du réapprentissage de l'attention sur le processeur : 387,9 s.
- Versions de la carte et de cette machine : mêmes torch (2.14.1) et numpy (2.4.6) (`pip-freeze.txt`) ; cette machine :
  processeur Intel à AVX-512, torch lié à MKL 2024.2 (`torch.__config__.show()`).

## 2. Les pistes, par la lecture du code et par les faits

| piste | ce que dit le code | fait mesuré (processeur) | verdict |
|---|---|---|---|
| (a) départ tiré sur l'appareil | `t07bbis/apprentissage_carte_v1.py` l. 94-95 : `torch.manual_seed(graine)` puis `torch.randn(d, dtype=torch.float64) * 0.01` **sans appareil** (générateur du processeur), porté ensuite sur l'appareil (l. 101) ; `sondes/familles.py` l. 192 et 209 : même tirage, même générateur ; aucun `set_default_device` ni `set_default_dtype` dans `src/` ni `scripts/` | sous-commande `tirage` : q0 relevé à l'appel de `torch.randn` dans les deux chemins : processeur, double précision, générateur par défaut, **égal au bit près** (`q0_egal_au_bit_v1_gele` : vrai) ; un autre générateur à graine égale (Philox) donnerait 8,177 (ordre de grandeur sans rapport avec 2,1·10⁻²) | **écartée** |
| (b) ordre des lots, permutations sur l'appareil | apprentissage **par lot entier** : chaque époque lit tout `lot.X` (`apprentissage_carte_v1.py` l. 106-115 ; `familles.py` l. 213-225) ; aucun mélange, aucun lot ; les actions de contrôle sont tirées par numpy (`scripts/repetition_carte_bbis_v1.py` l. 333, 388 ; course : `validation_imbriquee_v1.py` l. 422) | sans objet : aucun tirage sur l'appareil | **écartée** (rien à tirer) |
| (c) simple précision, noyau rapide d'attention | `LotCarte` en double précision (l. 56), w, b, q, cible en double (l. 95-105), agrégation au type des scores (l. 73) ; attention écrite à la main (`scatter_reduce`, `exp`, `index_add`, l. 71-81) ; aucun `scaled_dot_product_attention` | recensement de **toutes** les sorties des opérations de torch du chemin v1 pendant deux époques (mode de fonctions de torch) : toutes en double précision, sauf les compteurs de pas d'Adam (scalaires de valeur entière 0, 1, 2, en simple précision : `state['step']`, aucun calcul) | **écartée** |
| (d) optimiseur qui amplifie | Adam, 300 époques, pas 0,05 ; pénalité sur w seulement (q libre) ; agrégation softmax sur environ 224 jetons | § 3 à § 5 : écarts d'arrondi amplifiés jusqu'à 0,6 à 1,1 ; un seul arrondi croît d'environ ×1,5 par pas jusqu'au pas 37 environ, puis se contracte (2 à 3·10⁻⁶ à la fin) ; deux piles réelles : 10⁻¹⁰ au premier pas, au-delà de 10⁻⁴ entre les pas 11 et 21 | **cause** (avec (e)) |
| (e) chemins de calcul différents | réduction (moyenne, écart type) par torch sur l'appareil dans v1 (l. 61-64) contre numpy dans le paquet gelé (`familles.py` l. 152-155, sommes séquentielles) ; sur la carte, produits par cuBLAS et non MKL, `index_add` et `exp` de la carte ; Adam « multi-tenseurs » par défaut sur la carte, « un tenseur à la fois » sur le processeur (`torch/optim/optimizer.py`, `_default_to_fused_or_foreach`) : mêmes formules, autres arrondis | § 3 : chacun de ces écarts d'arrondi suffit, amplifié par (d) | **cause** (avec (d)) |

## 3. Mesures au lot entier de la répétition, sur processeur

Sous-commandes `apprendre` et `comparer` ; mêmes données, mêmes graines, réglage l2 = 10⁻³, couche 15, 300 époques, pas 0,05 ;
quatre fils, algorithmes déterministes ; mesure du contrôle : max |a − b| / max(|b|, 1) sur les scores des 256 actions de
contrôle (boucle du harnais), comme `controle_carte_processeur`. Le paquet gelé est appelé tel quel ; seules ses deux fonctions
de réduction sont remplacées, dans le processus du diagnostic, par des répliques économes en mémoire (le lot entier dépasse la
mémoire de cette machine par les copies transitoires) : **égales au bit près** aux originales à 200 actions (45 742 jetons ;
moyenne, écart type, jetons réduits, indices : sous-commande `repliques`), et la référence pas à pas (§ 4) rend le paquet gelé au
bit près pour les deux familles (`reference_pas_a_pas_egale_au_paquet_gele`).

| comparaison | ce qui diffère | attention | linéaire |
|---|---|---|---|
| **carte** contre processeur (la répétition, `repetition-carte.json`) | tout : réduction, noyaux, Adam | **2,131e-02** | 1,954e-08 |
| chemin v1 sur processeur contre paquet gelé | la réduction seule (torch contre numpy) | **1,088** | 4,300e-12 |
| paquet gelé contre lui-même, autre jeu d'instructions (AVX2 contre AVX-512 : `ATEN_CPU_CAPABILITY=avx2`, `MKL_ENABLE_INSTRUCTIONS=AVX2`, relu `AVX2`) | les noyaux seuls (jetons réduits identiques) | **0,633** | 9,193e-13 |
| paquet gelé, q0 d'un autre générateur à graine égale (simulation de (a)) | le départ entier | 8,177 | — |

Échelle : scores des actions de contrôle jusqu'à 5,91 (attention) et 3,68 (linéaire) en valeur absolue ; max |q| = 1,149. Écart
relatif des paramètres (attention, v1 contre gelé) : 0,136 sur w, 0,026 sur q.

**Lecture** : pour l'attention, deux piles qui ne diffèrent que par l'arrondi rendent deux sondes différentes (écart 0,6 à 1,1
sur cette machine ; 2·10⁻² entre la carte et le processeur de la répétition) ; pour la linéaire, le même écart d'arrondi reste
à 10⁻¹² (10⁻⁸ entre carte et processeur). Le contrôle mesure donc, pour l'attention, la sensibilité de l'apprentissage aux
arrondis, et non la justesse de la chaîne. Le paquet gelé ne tient pas lui-même la tolérance d'un jeu d'instructions à l'autre :
aucune mise en œuvre sur la carte ne peut la tenir à coup sûr.

## 4. Pas à pas : une perturbation d'un seul arrondi (sous-commande `pas-a-pas`)

Trajectoires menées en pas égal sur les mêmes jetons réduits : référence A (le calcul du paquet gelé opération par opération,
égal au paquet au bit près) ; « pas » : pas d'Adam remplacé par le flottant suivant (0,05 → 0,05000000000000001) ; « q0 » : q0[0]
remplacé par le flottant suivant. (Une perturbation de w0 est écartée : w0 = 0 rend tous les scores égaux à la première époque,
et tout w0[0] ≠ 0 rompt l'égalité du maximum : ce n'est pas un arrondi.) Écart du contrôle aux époques relevées (après le pas de
l'époque ; « pas faits » = indice de l'époque + 1) :

| pas faits | attention, « pas » | attention, « q0 » | linéaire, « pas » |
|---|---|---|---|
| 1 | 6,1e-16 | 1,3e-15 | 1,2e-15 |
| 2 | 2,0e-13 | 1,3e-13 | 8,9e-16 |
| 6 | 1,2e-11 | 2,2e-11 | 1,0e-15 |
| 11 | 1,8e-10 | 3,5e-10 | 1,2e-15 |
| 21 | 3,0e-08 | 3,7e-08 | 2,3e-15 |
| 31 | 9,1e-07 | 1,3e-06 | 3,4e-15 |
| 51 | **9,6e-06** | 5,3e-06 | 1,3e-14 |
| 101 | 3,4e-06 | 2,7e-06 | 4,2e-14 |
| 201 | 3,0e-06 | 2,4e-06 | 3,8e-13 |
| 300 | 2,9e-06 | 2,1e-06 | 7,0e-13 |

**Lecture** (écart pas à pas demandé pour (d)) : chez l'attention, un seul arrondi croît d'environ ×1,5 par pas entre les pas
4 et 37 (de 1,7·10⁻¹² à 1,7·10⁻⁶ sur les sorties d'action du lot), puis plafonne entre 10⁻⁶ et 10⁻⁵ et décroît un peu ; il
reste sous 10⁻⁴ (2 à 3·10⁻⁶ à la fin). Chez la linéaire, rien ne croît (10⁻¹⁵ à 10⁻¹²). L'apprentissage de l'attention a donc une
**phase d'instabilité transitoire** (jusqu'au pas 50 environ) suivie d'une contraction : ce n'est pas un chaos sans borne ; un
écart final de 10⁻² à 1 demande un écart de départ bien plus grand qu'un arrondi : c'est ce que montre le § 5.

## 5. Trajectoires sous deux piles d'arrondis réelles, pas par pas (second script)

`diagnostic-trajectoires-attention-carte-v1.py`, sous-commande `trajectoire` : le calcul du paquet gelé, opération par opération,
mené seul dans un processus ; scores des 256 actions de contrôle relevés aux mêmes époques ; validation : la sonde de chaque
trajectoire à sa dernière époque est **égale au bit près** à celle de l'apprentissage correspondant du § 3 (paquet gelé, paquet
gelé en AVX2, chemin v1). Écart du contrôle :

| pas faits | AVX2 contre AVX-512 (même code gelé, jetons réduits identiques) | réduction torch contre numpy (chemin v1 contre paquet gelé) |
|---|---|---|
| 1 | 1,4e-10 | 2,8e-10 |
| 2 | 3,9e-08 | 7,8e-08 |
| 3 | 2,9e-07 | 5,9e-07 |
| 4 | 5,0e-07 | 1,0e-06 |
| 6 | 1,8e-06 | 3,6e-06 |
| 11 | 4,4e-05 | 8,7e-05 |
| 21 | **5,8e-03** | **1,2e-02** |
| 31 | 0,157 | 0,312 |
| 51 | 1,94 | 3,08 |
| 101 | 0,625 | 0,981 |
| 300 | **0,633** | **1,088** |

**Lecture** : deux piles réelles s'écartent dès le **premier pas** de 10⁻¹⁰, soit cinq ordres de grandeur de plus qu'un arrondi
sur un paramètre (6·10⁻¹⁶ au § 4) ; la même croissance (environ ×1,4 à ×1,9 par pas entre les pas 11 et 31) les porte au-delà de
10⁻⁴ entre les pas 11 et 21 et jusqu'à l'ordre de 1 au pas 51 ; la contraction finale les laisse à 0,6 et 1,1. Explication
probable du premier pas, **non mesurée** : le premier pas d'Adam divise chaque gradient par sa racine carrée moyenne plus 10⁻⁸ ;
pour les coordonnées de gradient petites, issues de sommes de 143 231 termes qui se compensent, l'écart relatif d'arrondi entre
deux piles est grand et passe dans le pas. La répétition sur carte (2,1·10⁻² à la fin) est du même ordre que ces deux piles du
processeur ; rien n'indique qu'une pile carte, quelle qu'elle soit, s'écarte de la pile processeur de moins de 10⁻¹⁴ au premier
pas, ce qu'il faudrait pour finir sous 10⁻⁴.

## 6. Correction : aucune sous le texte

- Ce que le code v1 fait déjà de ce que demandait la commande : tout tirage sur le processeur (q0 par le générateur du
  processeur après `torch.manual_seed`, puis transfert ; un tirage par `numpy.random.SeedSequence` rendrait un **autre** q0 que
  le paquet gelé, donc un échec sûr du contrôle : il ne faut pas le faire) ; double précision partout (recensement) ; aucun noyau
  rapide d'attention.
- Ce qui reste et qu'aucun code ne retire : les arrondis des noyaux de la carte (cuBLAS, `exp`, `index_add`, Adam
  multi-tenseurs) diffèrent de ceux du processeur ; or le § 3 montre que des écarts de cette nature (AVX2 contre AVX-512, à jetons
  réduits identiques : 0,633) suffisent à séparer les trajectoires. Une version qui reprendrait la réduction du paquet gelé
  (numpy sur le processeur, puis transfert) retirerait l'écart de réduction mais pas celui des noyaux ; elle **ne réparerait pas
  l'arrêt** : elle n'est pas écrite.
- Les seules corrections qui feraient passer le contrôle changent ce que le texte décrit (le contrôle, l'apprentissage de la
  famille, ou l'appareil) : **nœud de Lazar**, arrêt ici comme la commande le demande. Ni la tolérance, ni la grille, ni la
  famille, ni les seuils, ni `MIN_ESSAIS` ne sont touchés.

## 7. Décision demandée à Lazar (nœud : pas de défaut)

**Décision** : comment rendre jouable le contrôle carte-processeur de B bis pour la famille « attention », que le texte actuel
ne peut pas passer pour une raison de conditionnement et non d'erreur de chaîne.

**Enjeu** : sous le brouillon 3, toute marche dont le couple (cellule, pli) tiré retient un réglage « attention » s'arrête
(code 9), et la relance unique redonne le même arrêt ; la course du mercredi 18 et le verdict du dimanche 22 en dépendent. Le texte
n'est pas encore scellé (`SCELLEMENT-BBIS` prévu lundi 16) : un brouillon 4 peut porter la décision.

**Options** :
1. **Contrôle à horizon court pour l'attention**, au même seuil 10⁻⁴ : la carte et le processeur (paquet gelé,
   `Reglages(epoques=k)`) réapprennent le couple tiré pendant k époques depuis le même départ ; k fixé maintenant, sur ces
   trajectoires synthétiques (§ 5), avec marge : **k = 3** (2,9·10⁻⁷ et 5,9·10⁻⁷ entre deux piles du processeur, marge de plus de
   deux ordres de grandeur ; k = 11 n'en a plus : 4,4·10⁻⁵ et 8,7·10⁻⁵) ; la linéaire garde le contrôle à 300 époques ; le
   déterminisme au bit près sur la carte à 300 époques reste exigé. Avantage : attrape les erreurs de chaîne (données, graine,
   formule, réglage) sans dépendre de la phase d'instabilité ; une ligne du texte, peu de code (`controle_carte_processeur` prend
   déjà `epoques`). Inconvénient :
   la sonde de 300 époques de l'attention n'est pas comparée elle-même ; k est choisi sur données synthétiques ; le pouvoir de
   détection à 3 époques (par exemple d'un calcul en simple précision) n'est pas mesuré ici.
2. **Contrôle sur la seule famille linéaire** (si le couple tiré retient l'attention, une sonde linéaire du même couple, au
   réglage linéaire le mieux classé, est contrôlée à sa place). Avantage : passe sur la carte (1,95·10⁻⁸ mesuré) et vérifie le
   tronc commun (lot, réduction, perte, Adam, produits). Inconvénient : le code propre à l'attention (q, softmax, `index_add`) n'est jamais comparé sur la carte.
3. **Variante (r1) pour toute la course** (famille linéaire seule). Avantage : contrôle sûr. Inconvénient : retire l'attention
   de la grille, ce qui change ce que B bis éprouve ; non recommandé.

**Recommandation** : l'option 1, avec la linéaire contrôlée à 300 époques comme aujourd'hui ; confiance moyenne : les écarts de
la carte peuvent dépasser ceux des deux piles du processeur (pour la linéaire, 2·10⁻⁸ sur la carte contre 10⁻¹² ici), d'où une
marge d'au moins deux ordres de grandeur sur k, à confirmer par la quatrième passe (§ 9). **Réserve à écrire quelle que soit
l'option** : les sondes « attention » de B bis ne sont reproductibles qu'au bit près sur la même pile (carte, pilote, torch) ;
sur une autre pile, l'apprentissage rendrait une autre sonde (ici, écart du contrôle jusqu'à 1,09 sur des scores d'au plus
5,9 en valeur absolue).

## 8. Essais

- **Suite de B bis** (`tests/test_t07bbis_*.py` et `tests/test_repetition_bbis_v1.py`) : **138 passés**, 0 échec, 0 sauté
  (même compte qu'avant ; aucun fichier de `src/` ni de `tests/` modifié) ; sortie : `essais-sortie-diagnostic-ecart-attention-v1.txt`.
- **Essais du diagnostic** (dans ses sorties) : répliques de réduction égales au bit près aux originales (cas sain) ; référence
  pas à pas égale au paquet gelé au bit près (deux familles) ; trajectoires égales, à leur dernière époque, aux sondes des
  apprentissages correspondants (§ 5) ; q0 égal au bit près entre les deux chemins ; artefacts : autre générateur (8,177),
  autre jeu d'instructions (0,633), autre réduction (1,088) — chacun refusé par la tolérance du contrôle. Le contrôle lui-même
  garde ses essais sain et artefact (`test_controle_carte_processeur_sain_et_artefact`, inchangé).
- Pas d'essai « appareil à flux aléatoire différent » ajouté : le chemin v1 ne tire rien sur l'appareil (piste (a)), et
  l'« ancien chemin » n'échouerait pas à cet essai ; il ne prouverait rien.

## 9. Ce qui reste non éprouvé sans carte, et ce qu'une quatrième passe devrait montrer

- **Non éprouvé** : la part de chaque noyau de la carte dans l'écart (réduction sur la carte, cuBLAS, `exp`, `index_add`, Adam
  multi-tenseurs) ; la courbe époque par époque entre la carte et le processeur ; le comportement de l'attention sur de vraies
  activations (mieux ou moins bien conditionnées que ce bruit gaussien : non mesurable ici sans les données, interdites).
- **Sous le code et le texte actuels**, une quatrième passe redonnerait l'arrêt : l'apprentissage sur la carte est déterministe
  au bit près (même sonde), et la référence sur le processeur ne dépend que du processeur de l'instance ; l'écart resterait très
  probablement au-delà de 10⁻⁴ (2,1·10⁻² à la troisième passe ; 0,6 à 1,1 entre deux piles du processeur ici). **Elle ne vaut pas
  d'être payée.**
- **Si l'option 1 est retenue**, la quatrième passe (même jeu synthétique) devrait montrer : linéaire à 300 époques ≤ 10⁻⁴
  (≈ 2·10⁻⁸ attendu) ; attention à 3 époques ≤ 10⁻⁴ avec marge (de l'ordre de 10⁻⁷ attendu si la carte s'écarte du
  processeur comme deux piles du processeur entre elles) ; déterminisme vrai. Pour confirmer le mécanisme sur la carte
  (si une ligne de dépense le permet), elle écrirait aussi l'écart carte-processeur aux époques relevées (petit au début, en
  croissance jusqu'au pas 50 environ, au-delà de 10⁻⁴ dès les pas 11 à 21, comme au § 5) et l'écart de la carte à elle-même
  sous un pas d'Adam d'un arrondi (≈ 10⁻⁶ attendu, sous 10⁻⁴, comme au § 4).

## 10. Fichiers et empreintes

Fichiers ajoutés dans `brouillons/T0.7-etape-B-bis-v1/code/` (aucun fichier existant modifié ; `src/`, `tests/`, `scripts/`
inchangés), chacun avec son compagnon `.sha256` :

| fichier | sha256 |
|---|---|
| `diagnostic-ecart-attention-carte-v1.py` (apprentissages, pas à pas, comparaison) | `0c3226fc8ce439922bf5edeb5ae52afee23c368ab2798699e2bcc7f37ec7d52f` |
| `diagnostic-ecart-attention-carte-v1-sortie.json` (§ 2 à § 4) | `2c7d9f2377604fde7c017d70b046a495512f6484e3d1582dde7d7e4786b4be88` |
| `diagnostic-trajectoires-attention-carte-v1.py` (trajectoires ; empreinte relue dans sa sortie) | `8da0cb895bb49ef873440e758e462d55ccab729675724cf941bd5158f4f2708a` |
| `diagnostic-trajectoires-attention-carte-v1-sortie.json` (§ 5) | `8f7cfd5d77228ea25d826a73c0bee7db0802be42bc0f1752f5f10ca69531c768` |
| `essais-sortie-diagnostic-ecart-attention-v1.txt` (§ 8) | `56b2be854b17e667cad548d1bd67bec84aa06f804740d50a0b82dc274337e13c` |
| ce rapport | son compagnon `diagnostic-ecart-attention-carte-v1.md.sha256` |

Rejeu (processeur, environ 2 h 30 sur cette machine partagée, 4 fils, mémoire de pointe ≈ 7 Go) : pour chaque sous-commande,
`PY=.venv/bin/python ; $PY -I SCRIPT SOUS-COMMANDE SORTIE.json [options]` dans un dossier de travail ; les jeux d'instructions par
`env ATEN_CPU_CAPABILITY=avx2 MKL_ENABLE_INSTRUCTIONS=AVX2` ; puis `comparer`. Les paramètres des sondes (`.npz`) ne sont pas
versés : leurs empreintes sont dans les sorties (`empreinte_parametres`).
