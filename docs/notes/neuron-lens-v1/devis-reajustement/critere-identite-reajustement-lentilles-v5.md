# Critère d'identité du réajustement de nos lentilles R et S (lecture par lentille neuronale, Llama 3.1 8B Instruct) — v5 (à vérifier par le contre-lecteur de la v4, puis sceller avant toute création de machine)

- **Auteur** : le rédacteur, sous-agent lancé par la session `session_013QMaykLXtozHttcSQ4ke1s`, modèle **Claude Fable 5.2**
  (`claude-fable-5-2`), selon le mot de Lazar du 19 novembre (R-3735, section « Qui conçoit » des consignes permanentes, branche
  principale). Il n'a écrit ni les versions 1 à 4, ni le programme de comparaison, ni ses essais, ni les contre-lectures ; la v4 est
  d'un autre rédacteur sur le même modèle.
- **Origine, déclarée** : la v4 (`critere-identite-reajustement-lentilles-v4.md`,
  `60df6c539f8aa0a04d5eec0c5b47a421bb780dc5ab8d0251c80ebfb06c67ccfa`), dont les règles sont gardées ; elle reste archivée sans
  modification, comme les versions 1 à 3. Lus aussi, sur la branche principale : la contre-lecture de la v4 par un lecteur sur Claude
  Opus 5.5 (`docs/notes/neuron-lens-v1/contre-lecture-critere-et-devis-v4-v1.md`,
  `c61466fae8712769e498bfcabb24079bbc2934657e1899f005599e42a143ca3d`, commit `f113e756` : « pas avant », corrections E1 à E6,
  mineures m1 à m8) et la vérification du programme de comparaison v2 (`verification-programme-comparaison-v2-v1.md`,
  `8cd01e58bbdb724c12924595ba681ad726e22f273a74a108b4e24311bc98523b`, annexe) ; le programme de comparaison v3 et ses essais (§ 7).
- Heure (`date -u`) à l'écriture : 2026-11-19T11:09:09Z ; l'heure du scellement est celle du fichier compagnon. Pièce de **classe A**.
- Contexte : accord GO-2026-11-19-33 (pièce 3 du billet : la lecture des sondes avec nos lentilles, qui suppose le réajustement).
  Aucune ligne de calcul à ce jour : aucune lentille réajustée n'existe, ce critère est écrit avant de voir (R1). **Il prime sur toute
  phrase du devis** ; le devis v5 (`devis-reajustement-lentilles-b-beta-v5.md`) le cite.
- Reste à faire avant la création : vérification des corrections par le contre-lecteur de la v4 (R2, R-3735), scellement par la mère.

## 0. Différences avec la v4, et traitement de la contre-lecture
### 0.1 Différences avec la v4, chacune avec sa raison
**Aucun seuil n'est changé** (10⁻³, 10⁻⁹, 10⁻⁶, 0,10), ni les libellés des mentions, ni ce que chaque mention autorise.
| n° | différence | raison |
|---|---|---|
| 1 | **Le programme cité est la version 3**, et lui seul (§ 7). | Passage au programme v3, qui porte les contrôles H1 à H7 de la v4 ; remarque 5 de l'annexe de la vérification du programme v2 : ne citer que le programme en vigueur. |
| 2 | **Les contrôles hors programme H1 à H7 de la v4 disparaissent comme liste à la main.** H2, H3, H4, H5 et H7 sont des préalables ou des causes de suspension que le programme calcule ; H6 est le déclencheur (vi), rendu par le programme ; de H1, le programme verse les empreintes des pièces lues et le commit donné (§ 4, § 6). | Le programme v3 les vérifie lui-même, avec un essai par contrôle ; une règle appliquée par programme n'a plus à être tenue à la main. |
| 3 | **Liste fermée de ce qui reste à la main, K1 à K5** (§ 7) : ce que le programme ne fait pas. Elle ne peut que rendre « non comparable » ou suspendre. | Le programme enregistre le commit et les empreintes sans pouvoir dire qu'ils sont ceux de la branche poussée ; il ne rattache pas le lanceur neuf à sa course ; il ne lit ni le journal, ni la pièce du matériel, ni le lieu de rangement (sondes U1 à U4 du rédacteur, § 7). |
| 4 | **Préalables repris du programme v3** (§ 4) : fonction de calcul égale à une empreinte fixée par constante ; couches des matrices exactement 0 à 30 et des séries exactement 0 à 27, des deux côtés ; champ `etape` conforme à la lentille ; export neuf rattaché à la course neuve et différent de celui du 18 ; « même code » (bibliothèque des lentilles, précision, versions, contenu des correctifs). | Corrections F1 à F4 et mineure 1 de la vérification du programme v2, portées par le programme v3 ; corrections E1 et E2 et mineure m6 de la contre-lecture de la v4. |
| 5 | **La mention suspendue peut tomber à octets différents** : au deuxième palier, un écart sur `diffs` au-delà de 10⁻³ suspend la mention (§ 4). | C'était le contrôle H7 de la v4 ; le programme le rend sous le même libellé que l'anomalie à octets égaux. Le critère le dit pour que le libellé ne surprenne pas. |
| 6 | **La table des différences des deux manifestes est rendue par le programme, à tous les paliers**, sans critère (§ 6) ; ce qu'elle ne couvre pas (champs du haut du manifeste) est relevé à la main (K5). | Correction F5 de la vérification du programme v2 ; la v4 ne la demandait qu'à l'audit, donc pas au deuxième palier sans déclencheur (contre-lecture de la v4, § 6). |
| 7 | **Ce que l'audit peut conclure est écrit** : il ne fait jamais monter une mention ; sans contrôle manqué, la mention reste et le fait est écrit (§ 6). | Correction E3. |
| 8 | **Une phrase par lentille** quand une seule est au deuxième palier (ou au premier) ; « même code d'ajustement » ; la norme du plancher nommée (§ 5). | Correction E4 ; remarque 4 de l'annexe de la vérification du programme v2. |
| 9 | **Arrêt du programme sur une erreur** : vaut « non comparable », ou suspension à empreinte égale, et nœud de Lazar (§ 4). **Variante B, seconde course incomplète** : la lentille du deuxième palier reste sans mesure propre (§ 5). | Mineure m5 ; les sondes U11 à U14 du rédacteur montrent quatre arrêts sur erreur du programme v3. |
| 10 | Précisions de lettre : arrondi du plancher (§ 4) ; le zéro exact des séries de R n'exige rien de plus que l'égalité des matrices des moitiés (§ 4) ; nom du fichier au moment de l'écriture et lieu des tenseurs (§ 4) ; modèle de carte exigé le 18 (§ 2). | Mineures m1, m2, m3. |
| 11 | **Contrôle neuf, le seul que le rédacteur ajoute de lui-même : le manifeste neuf porte `depot_propre` vrai** (K2). | Le programme lit les correctifs et le critère lit le lanceur au commit que porte le manifeste : cela ne décrit le code qui a tourné que si l'arbre de la machine était propre. Le manifeste du 18 porte ce champ (vrai) ; le programme ne le lit pas (sonde U1). Il ne peut que suspendre ou rendre « non comparable ». |
| 12 | Deux nœuds proposés à Lazar (§ 9) : un essai court qui mesure l'écart d'un réajustement ; un croquis numérique de chaque matrice versé par la course neuve. | Remarques 6 et 7 de l'annexe de la vérification du programme v2 ; mineure m4. |
| 13 | Les sondes et tableaux d'historique de la v4 (§ 0, § 7 et § 9 de la v4) ne sont pas recopiés. | Ils décrivaient les défauts du programme v2, qui n'est plus cité ; ils restent dans la v4 archivée. |

### 0.2 Traitement de la contre-lecture de la v4 (`c61466fa…`)
| correction | traitement | où |
|---|---|---|
| E1, fonction de référence fixée et lanceurs rattachés (« H8 ») | **faite, autrement que par une ligne H8** : le texte de la fonction est comparé par le programme v3 à l'empreinte fixée `a5495c68…`, des deux côtés ; le lanceur neuf est rattaché à la main au commit du manifeste neuf (K2). **Refusé, un point** : exiger à la main l'empreinte du fichier du lanceur de référence (`582fd9ef…`). Raison : le programme ne lit de ce lanceur que le texte de la fonction, qui est fixé ; l'empreinte du fichier n'ajouterait aucune garde, et ce critère ne garde à la main que ce que le programme ne fait pas. L'empreinte reste citée au § 2. | § 4, § 7 |
| E2, couches des matrices 0 à 30 | **faite**, par le programme v3 (préalable). | § 4 |
| E3, ce que l'audit peut conclure | **faite**, texte repris ; « qui commence par H2 » devient « qui commence par K1 », H2 étant désormais un préalable du programme. | § 6 |
| E4, phrase par lentille, « même code d'ajustement », norme nommée | **faite** ; les phrases au singulier sont écrites en entier, en français et en anglais ; la phrase du premier palier reçoit aussi son singulier. | § 5 |
| E5, versions (clé d'un seul côté), pièces égales aux fichiers du commit, matériel à tous les paliers | **faite** : la clé d'un seul côté est un manqué dans le programme v3 (égalité des deux dictionnaires hors `plateforme` ; sonde U5) ; l'égalité aux fichiers du commit est K1 ; le matériel est K3, à tous les paliers. La part du devis est dans le devis v5. | § 4, § 7 |
| E6, fin de course | au devis v5 (§ 5, point 3) ; le critère en reprend une ligne : une lentille perdue avant sa copie reçoit le verdict « non réajustée ». | § 4 |
| m1, arrondi du plancher, ancre épinglée | **faite**. | § 4 |
| m2, H4 n'exige rien de plus que D1 | **faite**. | § 4 |
| m3, nom au moment de l'écriture, lieu des tenseurs, `H100_SXM` | **faite**, avec ce que le rédacteur a lu : le nom provisoire se déduit du nom final, et les sommes sont ramenées sur le processeur avant l'écriture. | § 2, § 4 |
| m4, remarques 6 et 7 de l'annexe | **faite** : nœuds proposés à Lazar. | § 9 ; devis v5, § 7 |
| m5, replis | **faite**. | § 4, § 5 |
| m6, champ `etape` | **faite**, par le programme v3 (préalable). | § 4 |
| m7, provenance des sondes et des essais rejoués | **faite par la seconde branche de la mineure** : les lignes « essais rejoués » et « sondes » de ce texte sont dites non opposables ; les fichiers sont hors dépôt, leur chemin est donné, la mère les verse si elle le veut. | § 7 |
| m8, stockage privé | au devis v5 (§ 5, point 9 ; décision 3). | — |

### 0.3 Annexe de la vérification du programme v2 (`8cd01e58…`)
Remarques 1, 2, 3 et 8 : déjà tenues dans la v4, gardées. Remarque 4 : différence n° 8. Remarque 5 : différence n° 1. Remarques 6 et 7 :
§ 9, nœuds proposés.

## 1. Ce que le critère décide
Les deux lentilles ajustées le 18 novembre (course `20261118-164930-neuron-lens-b-beta`, verdict « partiel » accepté par Lazar,
`lecture-b-beta/verdict-b-beta-v1.md`, `3a9b947e…`) ont été détruites avec la machine louée. Après un réajustement sur une autre
machine, trois questions se posent, et le critère les tient séparées :
1. **Identité** : les fichiers rangés sont-ils ceux qui ont été mesurés le 18 ? Seule une égalité d'octets y répond.
2. **Transport** : les mesures et le verdict du 18 décrivent-ils la lentille rangée ? Oui si l'identité est établie, non sinon.
3. **Parole** : qu'a-t-on le droit d'écrire, et de faire lire à cette lentille ? (§ 5.)
Ce qu'on appelle « la lentille » : pour R comme pour S, le **fichier d'ajustement** (sommes par couche, par cible et par moitié du
corpus). Pour R s'y ajoutent les trois exports qui en sont tirés (lentille entière, moitié paire, moitié impaire) : l'export est la
moyenne des sommes de la cible de sortie, et c'est lui qu'une lecture charge.

## 2. Références du 18 novembre
Branche `claude/brave-galileo-jhp684` (pièces absentes de la branche principale) ; les empreintes font foi, recalculées par le
rédacteur de la v5 le 19 novembre, égales aux valeurs ci-dessous. Dossier `diag/20261118-164930-neuron-lens-b-beta/` :
- `b-beta-ajustement-R.json` (`129c43b020854fd395cb0e969dd7f8956844417684e1e3a1099fee5e7f16d2ab`) : fichier d'ajustement de R
  `r-llama-3.1-8b-instruct-L32-dclm-T128.pt`, empreinte `31061d6c6c4b521c43d4710f9b660184b285467a065dadb5fc48e48c6d48c64c`,
  8 455 720 309 octets ; `diffs_float64`, 63 valeurs (32 pour la cible `mid`, 31 pour la cible `out`) ; `diffs` (simple précision) ;
  `meta` ; `n_docs` [466, 466] ; `next_doc` 932 ; `finies` vrai ; début 2026-11-18T18:03:15Z.
- `b-beta-ajustement-S.json` (`2dce646e32177941c02987a8ba3a0a67fd45d17f335e58ba9e321d3e0367c297`) : fichier
  `s-llama-3.1-8b-instruct-L32-dclm-T128.pt`, empreinte `aac70eef8f57b5d4423e5c8f8b2e77033b15077d95ef5a81894dbe3e0436e2b8`,
  8 589 938 049 octets ; 64 valeurs (32 et 32).
- `b-beta-export.json` (`17304c936792e4b79e9a47d78abf5bb6966310c36b92f387b3303b23891eedf1`) : pour R, `matrices_moities` (31 couches,
  deux empreintes par couche : moitié paire, moitié impaire) ; `valeurs.npR_notre_R` et `valeurs.identite_notre_R` (28 couches
  chacune, 0 à 27, calculées sur la lentille **entière**). **La lentille R entière n'a aucune empreinte par couche dans cette pièce** :
  ses fichiers exportés portent un identifiant de génération tiré à chaque export.
- Manifeste `runs/20261118-164930-neuron-lens-b-beta/manifeste.json` (`b90c15140074e9d41a3cf93e8bcaf55f80cc025d07d2d46432239d1c6b6e3444`) :
  commit du dépôt réduit `5e5cb65b4daf8726ebe1c4032a836b850de7ea2f` ; `config.commit_voisin` `849bfe1678e28becceb1e3864afe5fc8297d02e4` ;
  `config.drowse` (bibliothèque des lentilles : version 6.1.4, roue `673ed2b4…`) ; `config.precision` ; `config.correctifs` (cinq
  **chemins**, sans empreinte) ; `versions` (torch 2.14.1, numpy 2.4.6, transformers 5.18.0, safetensors 0.8.0, tokenizers 0.23.2,
  huggingface_hub 1.33.0, python 3.12.16).
- Fonction de calcul : `_split_half_64` de `src/controle_ia/neuron_lens/b_beta_lancer_v3.py` (fichier `582fd9ef322de2476b19eb4ce4868f99d7ea4ee52870edbaf316275bbd1dd1ea`, égal à celui du commit `5e5cb65b…` du dépôt réduit ; empreinte du
  texte de la fonction `a5495c68779bb67059cade18b3a92aaf7cf7fd0200f1770b038d8c5d0e62703c`, relevée par le rédacteur avec la fonction
  `empreinte_fonction` du programme ; **le programme v3 la porte en constante** et l'exige des deux lanceurs).
- **Non consignés le 18** : le modèle de carte (connu du registre des accords : H100 ; le filtre de la commande exigeait `H100_SXM`, selon le
  contre-lecteur de la v4, qui renvoie à l'en-tête du relevé de prix `90395583…`) et la version du pilote de la carte
  (réserve 2 du lecteur du verdict). Aucune pièce du 18 ne permet de les comparer.

## 3. Écart entre chemins de calcul (repère, hors critère)
Programme `ecart_chemins_calcul_v1.py` (`2084dae7…`), sortie `sortie-ecart-chemins-calcul-v1.txt` (`21d04198…`), sur les deux pièces
d'ajustement du § 2. Sur les **mêmes sommes**, la différence entre moitiés calculée en simple précision (`diffs`) s'écarte de celle en
double précision (`diffs_float64`) d'au plus 3,48 × 10⁻⁵ (R, cible `mid`, rang 2) et 5,86 × 10⁻⁵ (S, cible `out`, rang 26).
`diffs_float64` va de 3,53 × 10⁻³ à 0,1114 (R) et de 4,11 × 10⁻³ à 0,1046 (S) ; la valeur de R la plus proche de 0,10 est 0,100444
(cible `mid`, rang 2, **au-dessus** du seuil), à 4,4 × 10⁻⁴.
Cet écart est celui du calcul final en simple ou en double précision sur les mêmes sommes. Le critère compare deux valeurs en double
précision : cet écart n'y entre pas. **Il ne borne l'écart d'un réajustement ni par le bas ni par le haut ; aucune pièce ne mesure
l'écart d'un réajustement.**

## 4. Le critère, lentille par lentille
Chaque lentille est jugée seule ; cas mixte : chacune est rangée avec sa mention et reçoit sa propre phrase (§ 5). Les libellés entre
guillemets sont ceux que rend le programme de comparaison (§ 7) ; ils ne se reformulent pas.

### Procédure, dans cet ordre
0. **Lentille non réajustée** (course arrêtée avant elle, ou machine détruite par une garde avant sa copie : devis v5, § 5, point 3) :
   « R non réajustée » ou « S non réajustée » ; l'autre est jugée seule.
1. **Empreinte du nouveau fichier d'ajustement égale à celle du 18** → premier palier, sauf anomalie (mention 4 ci-dessous).
2. Sinon, **un préalable manqué** → « non comparable (traitée comme différente) ».
3. Sinon, **écart absolu maximal sur `diffs_float64` au plus 10⁻³** → deuxième palier, sauf si l'écart maximal sur `diffs` dépasse
   10⁻³ (mention suspendue) ; **au-delà de 10⁻³ sur `diffs_float64`** → « différente ».
4. Puis les **contrôles à la main** du § 7 (K1 à K5), dans les deux sens et à tous les paliers : l'un d'eux manqué rend « non
   comparable » (octets différents) ou suspend la mention (octets égaux), ou empêche le verdict tant qu'il n'est pas tenu (K1, K3, K4, K5) ; aucun ne peut faire monter
   une mention.
5. Puis la **relecture au lieu de rangement** : l'empreinte du fichier rangé, relue là où il est rangé, égale celle que la machine a
   calculée avant l'envoi ; sinon la mention est suspendue (elle décrirait un fichier qui n'existe plus).
6. Puis, si le programme rend au moins un déclencheur, l'**audit** du § 6, qui ne peut que suspendre.
Le résultat des points 1 à 3 est la **mention du programme** ; le résultat des points 0 à 6 est le **verdict d'identité**, prononcé par
la mère (§ 8). Seul le verdict d'identité s'écrit au lieu de rangement, à l'inventaire, dans un texte de lecture ou dans le billet.
**Arrêt du programme sur une erreur** (pièce illisible ou mal formée, toute exception) : aucune mention n'est rendue ; le verdict est
« non comparable (traitée comme différente) », ou « mention suspendue » si le résultat neuf porte l'empreinte du 18, et un nœud de
Lazar est ouvert ; le message d'erreur et la ligne de commande sont versés. Le programme n'est pas relancé sur des pièces retouchées.

### Les mentions
1. **Premier palier — « palier 1 — même lentille, octets identiques »** : l'empreinte du nouveau fichier d'ajustement est égale à la
   référence. Cela exige le **même nom de fichier au moment de l'écriture** qu'au 18 : le nom entre dans les octets écrits par
   `torch.save`, le dossier non (`essai_torch_save_nom_v1.py`, `1893d03e…`, sortie `3a2dbb16…` ; `essai_torch_save_octets_v1.py`,
   `4fdec19d…`, sortie `3a18c2c2…` ; essais sur processeur, torch 2.14.1). Le code voisin écrit sous un nom provisoire puis renomme ;
   ce nom provisoire se déduit du nom final (`path.with_suffix(".tmp")`, puis `os.replace`), donc le même nom final donne le même nom
   provisoire. Le lieu des tenseurs entre aussi dans l'archive : le code voisin ramène les sommes sur le processeur avant d'écrire
   (`v.cpu()`), ce qui est le cas que les essais couvrent. Ces trois lignes sont lues dans la copie de lecture du code voisin
   (`docs/sources/neuron-lens-lecture-20261113/depot-neuron-lens/scripts-02_fit.py.txt`, `309f4988…`, l. 161-166) ; **son égalité au
   commit `849bfe16…` de la course n'est pas vérifiée ici** (ce commit n'est pas dans le dépôt). Rien de cela n'est une condition du
   critère : le premier palier se lit sur l'empreinte, non sur ces raisons. Si le programme reçoit l'indication d'une reprise sur
   sauvegarde, il ajoute au libellé « ; reprise sur sauvegarde notée » ; si l'empreinte est égale, le premier palier est prononcé
   quand même, avec l'audit du § 6.
2. **Deuxième palier — « palier 2 — différences entre moitiés concordantes à 10⁻³ près ; octets différents ; matrices non
   comparables »** : tous les préalables tenus, et l'écart absolu maximal, en double précision et sans arrondi, entre les nouvelles
   `diffs_float64` (fonction `_split_half_64`, texte inchangé, calculée sur la machine à la fin de l'ajustement) et celles du 18, sur
   toutes les couches et cibles (R : 32 et 31 ; S : 32 et 32), est **au plus 10⁻³** ; et l'écart maximal sur `diffs` est lui aussi au
   plus 10⁻³.
3. **« différente »** : préalables tenus, écart sur `diffs_float64` au-delà de 10⁻³. **« non comparable (traitée comme
   différente) »** : un préalable manqué, octets différents.
4. **« mention suspendue : anomalie (nœud de Lazar) »**, dans deux cas.
   - **À empreinte égale**, l'un de ces faits : un préalable manqué (y compris la référence comparée à elle-même, qui n'est pas une
     course distincte) ; une taille différente ; un écart maximal sur `diffs_float64` supérieur à 10⁻⁹ (les mêmes sommes donnent la
     même valeur, à l'arrondi du calcul près) ; un écart maximal sur `diffs` supérieur à 10⁻⁶ (l'arrondi de la simple précision sur
     des valeurs d'au plus 0,12 est de l'ordre de 10⁻⁸) ; pour R, une empreinte de matrice des moitiés différente, ou **une des deux
     séries de R dont le plus grand changement n'est pas exactement zéro**. Le programme calcule les préalables et la table des écarts
     aussi au premier palier.
   - **À octets différents**, tous les préalables tenus et l'écart sur `diffs_float64` au plus 10⁻³, mais l'écart maximal sur `diffs`
     supérieur à 10⁻³ : `diffs` est la valeur que lisent les seuils de stabilité, elle ne peut pas s'écarter plus que la grandeur qui
     décide.
   S'y ajoutent les suspensions du contrôle K2, du point 5 de la procédure et de l'audit.

**Sur le zéro exact des séries de R au premier palier.** À octets égaux, les sommes sont les mêmes ; l'export est leur moyenne,
entrée par entrée ; chaque série est un maximum de valeurs absolues de différences, calculé en simple précision sur le processeur
(`ecart_max`, `src/controle_ia/neuron_lens/controles_b_beta_v2.py`, l. 139-143) : aucune réduction dont l'ordre dépende de la machine,
un maximum est exact. Les mêmes entrées donnent donc les mêmes nombres, et un changement non nul dit que la lentille entière exportée
n'est pas celle du 18, ou que l'ancre a changé. **Cette exigence n'ajoute rien de plus dur que l'égalité des empreintes des matrices
des moitiés**, qui suppose déjà un export reproductible au bit ; elle l'étend à la lentille entière, la seule qu'une lecture charge
et que rien d'autre ne trace. Les bornes de 10⁻⁹ et 10⁻⁶, elles, ne sont pas à zéro, parce que ces deux grandeurs passent par une
norme dont l'ordre de sommation dépend du processeur.

### Préalables du programme, tous exigés
Le programme les calcule tous avant de choisir une branche, à tous les paliers.
- **Forme et valeurs** : mêmes cibles et mêmes comptes de valeurs, séries non vides (`diffs_float64` et `diffs`) ; toutes les valeurs
  finies et numériques, des deux côtés ; `meta` présent et égal champ par champ ; `n_docs` [466, 466] et `next_doc` 932 des deux
  côtés ; même nom de fichier ; `finies` vrai des deux côtés ; champ `etape` égal à « ajustement-R » ou « ajustement-S » selon la
  lentille, des deux côtés.
- **Provenance** : empreintes des deux fichiers d'ajustement présentes et bien formées, tailles présentes ; pièces de référence
  (ajustement, manifeste et, pour R, export) d'empreintes égales à celles du § 2, **vérifiées par le programme sur les octets lus** ;
  course neuve distincte de celle du 18 (identifiant de course et heure de début différents) ; manifeste neuf d'empreinte égale à
  celle que porte le résultat neuf.
- **Même code** : champs `ajustement`, `correctifs`, `graines`, `modele`, `revision` et `corpus` de la configuration du manifeste
  présents et égaux à ceux du 18 ; même commit du code voisin ; texte de `_split_half_64` d'empreinte égale à la constante du § 2
  dans les deux lanceurs donnés ; `config.drowse` (bibliothèque des lentilles : version et empreinte de la roue) et
  `config.precision` présents et égaux ; `versions` : mêmes clés et mêmes valeurs des deux côtés, hors le champ `plateforme` (le noyau
  de l'hôte) — une clé présente d'un seul côté est un manqué ; chacun des fichiers de `config.correctifs`, lu dans le dépôt donné au
  programme au commit que porte chaque manifeste (`git show <commit>:<chemin>`), d'empreinte égale des deux côtés — un fichier
  illisible à l'un des commits est un manqué.
- **Pour R** : pièces d'export présentes et complètes des deux côtés (31 couches de matrices des moitiés, deux empreintes bien formées
  par couche ; 28 couches finies par série) ; couches des matrices exactement 0 à 30 et couches de chaque série exactement 0 à 27,
  des deux côtés ; export neuf de la course neuve (même identifiant de course et même empreinte de manifeste que le résultat
  d'ajustement neuf) et d'empreinte différente de l'export du 18.

### Ce que le deuxième palier voit, et ne voit pas
- **Aveugle par construction.** La grandeur vaut ‖moyenne paire − moyenne impaire‖ / ‖moyenne‖ : tout déplacement commun aux deux
  moitiés s'annule au numérateur. Elle dit si le bruit entre moitiés est retrouvé, pas si la lentille est au même endroit : une
  lentille déplacée de 13 % de sa norme à chaque couche, dans une direction commune aux deux moitiés, passe ce palier (contre-lecture
  de la v1, point 2). Or un effet de machine, de pilote ou de bibliothèque est justement commun aux deux moitiés. La mention ne dit
  ni « équivalente », ni « proche », ni « même lentille ».
- **Tolérance conventionnelle, déclarée telle, absolue.** La décision qui suit porte sur le seuil absolu de 0,10 ; une tolérance
  relative serait lâche là où la grandeur est grande, près de ce seuil. Repères, qui ne la justifient pas : ≈ 17 fois le plus grand
  écart entre chemins de calcul ; un centième du seuil de stabilité ; 0,9 % de la plus grande valeur ; 28 % (R) et 24 % (S) de la plus
  petite (aux couches les plus stables ce palier ne distingue presque rien) ; plus du double de la distance au seuil de la valeur de
  R la plus proche (4,4 × 10⁻⁴). Depuis la v4 (au deuxième palier, la variante A n'entre dans aucune lecture), cette tolérance ne décide plus que d'une chose : en variante B, si la
  lecture demande ou non un nœud de Lazar propre à l'identité (§ 5).
- **Pour R, deux séries rapportées sans critère** : l'écart maximal, entrée par entrée, de chaque matrice de la lentille entière à
  la lentille R publique (`npR_notre_R`) et à l'identité (`identite_notre_R`), couches 0 à 27. Le programme rend, pour chaque série,
  le changement par couche d'une course à l'autre, le plus grand changement en valeur absolue, la plus petite et la plus grande valeur
  du 18 (0,0694 à 0,6769 pour la première, 0,8015 à 2,1916 pour la seconde, lues dans la pièce `17304c93…`). Aucune tolérance : aucune
  pièce ne mesure leur variation d'un réajustement. **Leur sens exact : un plancher, jamais un plafond.** Si l'écart maximal d'une
  matrice à une ancre fixe change de δ, alors les deux matrices diffèrent d'au moins δ en une entrée (inégalité triangulaire) ; un
  changement nul ou petit ne borne rien par le haut. Les séries ne peuvent donc que **montrer** un déplacement, jamais l'exclure.
  Deux précisions de lettre : l'inégalité tient à l'arrondi de la simple précision près (au plus ≈ 3 × 10⁻⁷ ici, le calcul étant
  fait en `float32`, pour des écarts d'au plus 2,19) ; et elle suppose la même ancre aux deux courses — la lentille publique est
  épinglée par révision et vérifiée par empreinte dans le lanceur du 18 (relevé du contre-lecteur de la v4, non refait ici), le
  lanceur neuf doit garder ces lignes (devis v5, § 5, point 5), et toute différence du champ `lentilles` de la configuration
  paraît dans la table des différences des manifestes.
  Sont rapportés aussi : le compte des couches dont les empreintes des matrices des moitiés sont égales ; l'écart relatif maximal ;
  l'écart sur `diffs` ; toute valeur de `diffs` qui change de côté du seuil de stabilité de 0,10 ; la table des écarts par couche et
  par cible, avec leur signe.
- **Pour S, aucune grandeur sensible à la position n'existe dans les pièces du 18 : à écrire tel quel.** (L'écart maximal entre les
  sommes des deux moitiés, `ecarts_sommes`, versé le 18, est lui aussi une différence entre moitiés : il est aveugle de la même façon.)

## 5. Ce que chaque mention autorise
**Seul le premier palier établit l'identité.**

| verdict d'identité | identité | les mesures et le verdict du 18 décrivent la lentille rangée | lecture avec cette lentille |
|---|---|---|---|
| premier palier | établie | oui, avec leurs limites (verdict « partiel », couches stables du 18) | par un texte de lecture neuf et contre-lu, sous l'accord GO-2026-11-19-33 |
| deuxième palier, variante B (course rejouée **en entier**) | non établie | **non** ; ses mesures sont celles de la seconde course | seulement **après** la lecture de la seconde course par un lecteur neuf, dans les limites de cette lecture ; texte de lecture neuf et contre-lu, sous le même accord |
| deuxième palier, variante A (ajustement seul) | non établie | **non** ; elle n'a pour mesure à elle que sa différence entre moitiés (et, pour R, les deux séries) | **aucune sans nœud de Lazar** ; rangée avec sa mention |
| « différente », « non comparable », mention suspendue, lentille non réajustée | non établie | non | **aucune sans nœud de Lazar** ; rangée (si elle existe) avec sa mention |

- **Premier palier.** Phrase permise si **les deux** lentilles y sont : « Les fichiers d'ajustement réajustés sont identiques à l'octet à ceux du 18 novembre
  (empreintes …) ; les mesures du 18 novembre décrivent ces lentilles. » (*“The refitted fit files are byte-identical to those of
  18 November (hashes …); the 18 November measurements describe these lenses.”*) Si **une seule** lentille est au premier palier,
  la phrase est écrite pour elle seule : « Le fichier d'ajustement réajusté de la lentille [R | S] est identique à l'octet à celui
  du 18 novembre (empreinte …) ; les mesures du 18 novembre décrivent cette lentille. » (*“The refitted fit file of lens [R | S] is
  byte-identical to that of 18 November (hash …); the 18 November measurements describe this lens.”*) En variante B, la seconde course reste une seconde
  mesure de la même lentille, rapportée à côté selon son statut (devis v5, § 4).
- **Deuxième palier.** L'identité n'est pas établie et **le verdict du 18 ne se transporte pas** ; Lazar en est averti en ces termes
  dès le verdict d'identité, avant tout usage. **Mesures propres** : en variante B, celles de la seconde course, lues par un lecteur
  neuf sur un plan scellé ; en variante A, **aucune des mesures de la tranche du 18** (lecture contre pilotage, avance sur la lentille
  des logits, lecture côté entrée, accord du premier jeton entre moitiés, comparaison des deux codes, lecture contre ablation) : la
  lentille n'a à elle que la différence entre moitiés que son ajustement produit et, pour R, les deux séries ; le billet le dit.
  **Couches stables** : une couche n'est tenue pour stable que si `diffs` est au plus 0,10 **dans les deux ajustements** ; en
  variante B s'y ajoutent les limites que fixe la lecture de la seconde course.
  **Variante B, seconde course incomplète** (arrêtée après des ajustements copiés, avant la fin des mesures) : la lentille du
  deuxième palier reste sans mesure propre, comme en variante A ; elle est traitée comme en variante A (aucune lecture sans nœud de
  Lazar), et le billet le dit.
  Phrase permise si **les deux** lentilles sont au deuxième palier (les crochets se remplissent par les chiffres de la sortie du
  programme) : « Les deux lentilles mesurées le
  18 novembre ont été détruites avec la machine louée. Nous les avons réajustées avec le même code d'ajustement, le même corpus et les mêmes graines
  sur une autre machine. Les fichiers obtenus ne sont pas identiques à l'octet. Deux comparaisons restent possibles. La différence
  entre les deux moitiés du corpus, couche par couche, s'écarte d'au plus [écart mesuré] de celle du 18 novembre (tolérance fixée
  d'avance, par convention, à 10⁻³) ; cette grandeur ne voit pas un déplacement commun aux deux moitiés. Pour la lentille R seulement,
  l'écart maximal de chaque matrice à la lentille publique et à l'identité change d'au plus [valeur] et [valeur] d'une course à
  l'autre, pour des écarts qui valaient de [valeur] à [valeur] le 18 novembre ; aucun seuil n'était fixé d'avance pour ces deux
  séries, et ces changements sont un plancher, non un plafond, de l'écart maximal, entrée par entrée, entre les matrices des deux
  courses. Pour la lentille S,
  aucune comparaison de ce genre n'existe. Nous ne savons pas si les lentilles réajustées lisent comme celles du 18 novembre. Les
  mesures du 18 novembre [n'ont pas été refaites sur elles | ont été refaites sur elles et sont rapportées à côté]. »
  (*“The two lenses measured on 18 November were destroyed with the rented machine. We refitted them with the same fitting code, corpus and
  seeds on another machine. The files are not byte-identical. Two comparisons remain. The per-layer split-half difference deviates by
  at most [x] from the 18 November values (tolerance fixed in advance, by convention, at 10⁻³); this quantity is blind to any shift
  common to both halves. For lens R only, the largest entrywise gap of each matrix to the public lens and to the identity changes by
  at most [y] and [z] between the two runs, for gaps that ranged from [a] to [b] on 18 November; no threshold had been fixed in
  advance for these two series, and these changes are a lower bound, not an upper bound, on the largest entrywise gap between the matrices of the two
  runs. No such comparison exists for lens S. We cannot establish that the refitted lenses read like those measured on 18 November.
  The 18 November measurements [were not repeated on them | were repeated on them and are reported alongside].”*)
  Si **une seule** lentille est au deuxième palier, la phrase est écrite pour elle seule, au singulier, et l'autre reçoit la phrase
  de son propre verdict.
  Pour R seule : « La lentille R mesurée le 18 novembre a été détruite avec la machine louée. Nous l'avons réajustée avec le même
  code d'ajustement, le même corpus et les mêmes graines sur une autre machine. Le fichier obtenu n'est pas identique à l'octet. La
  différence entre les deux moitiés du corpus, couche par couche, s'écarte d'au plus [écart mesuré] de celle du 18 novembre
  (tolérance fixée d'avance, par convention, à 10⁻³) ; cette grandeur ne voit pas un déplacement commun aux deux moitiés. L'écart
  maximal de chaque matrice à la lentille publique et à l'identité change d'au plus [valeur] et [valeur] d'une course à l'autre,
  pour des écarts qui valaient de [valeur] à [valeur] le 18 novembre ; aucun seuil n'était fixé d'avance pour ces deux séries, et ces
  changements sont un plancher, non un plafond, de l'écart maximal, entrée par entrée, entre les matrices des deux courses. Nous ne
  savons pas si la lentille réajustée lit comme celle du 18 novembre. Les mesures du 18 novembre [n'ont pas été refaites sur elle |
  ont été refaites sur elle et sont rapportées à côté]. »
  (*“Lens R, measured on 18 November, was destroyed with the rented machine. We refitted it with the same fitting code, corpus and
  seeds on another machine. The file is not byte-identical. The per-layer split-half difference deviates by at most [x] from the
  18 November values (tolerance fixed in advance, by convention, at 10⁻³); this quantity is blind to any shift common to both
  halves. The largest entrywise gap of each matrix to the public lens and to the identity changes by at most [y] and [z] between
  the two runs, for gaps that ranged from [a] to [b] on 18 November; no threshold had been fixed in advance for these two series,
  and these changes are a lower bound, not an upper bound, on the largest entrywise gap between the matrices of the two runs. We
  cannot establish that the refitted lens reads like the one measured on 18 November. The 18 November measurements [were not
  repeated on it | were repeated on it and are reported alongside].”*)
  Pour S seule : la même phrase, « La lentille S… », où la phrase des deux séries (« L'écart maximal de chaque matrice… des deux
  courses. ») est remplacée par « Aucune autre comparaison n'existe pour cette lentille. » (*“No other comparison exists for this
  lens.”*)
  « Même code d'ajustement » dit le code qui ajuste (code voisin, correctifs, bibliothèque des lentilles, précision, versions), non
  le lanceur, qui a changé (devis v5, § 5, point 5). Au deuxième palier ces mots sont couverts : les préalables « même code » du
  programme (§ 4) et le contrôle K2 sont tenus, sans quoi le verdict serait « non comparable ».
  **Ces chiffres sont obligatoires**, quel que soit leur sens, dans toute
  phrase du billet et du texte de lecture qui cite la lentille R au deuxième palier, et dans l'avertissement à Lazar ; **aucun
  qualificatif** ne leur est attaché (« inchangé », « stable », « négligeable », « a bougé »), faute de seuil fixé d'avance.
  Phrases interdites : « nous avons réajusté à l'identique les lentilles jugées le 18 novembre » ; « la lentille réajustée est proche
  de l'originale », « équivalente », « la même à la précision numérique près » ; « le verdict “partiel” du 18 novembre vaut pour la
  lentille employée ici » ; « la distance à la lentille publique est inchangée », ou toute phrase qui tire des séries de R un appui à
  la proximité ; toute phrase qui prête à la lentille réajustée une mesure faite sur celle du 18. (*“We refitted the same lenses”;
  “the refitted lens is close/equivalent to the original”; “the 18 November verdict applies to the lens used here”.*)
- **Dans tous les cas** : tout usage dans une lecture passe par un texte de lecture neuf, contre-lu, qui recopie le verdict d'identité
  et les chiffres de la sortie ; le billet dit le palier obtenu, quel qu'il soit, et, si la lentille n'est pas lue, le dit en une
  phrase (aucun retrait silencieux de la pièce 3) ; le verdict d'identité est écrit dans un fichier compagnon au lieu de rangement et
  à l'inventaire.

## 6. Audit, le même dans les deux sens
**Déclencheurs, tous rendus par le programme** (champ `declencheurs` de sa sortie) : (i) premier palier obtenu ; (ii) écart maximal
exactement nul avec des octets différents ; (iii) « différente » ; (iv) « non comparable » ; (v) empreinte du fichier égale et une
cause d'anomalie du § 4 ; (vi) pour R, au deuxième palier, 31 matrices des moitiés égales sur 31, ou une série dont le plus grand
changement est exactement nul ; (vii) écart maximal sur `diffs` supérieur à 10⁻³ quand l'écart sur `diffs_float64` tient le deuxième
palier, ou supérieur à 10⁻⁶ au premier palier. **L'audit est dû dès que cette liste n'est pas vide** ; le champ `audit_requis` de la
sortie, que le programme ne pose que pour (vi), n'est pas ce qui en décide.
**Audit, fait par la mère ou par l'agent neuf du § 8, sans lire aucune mesure de la course.** Il dit, ligne par ligne, ce qui vient
du programme et ce qui est relevé à la main, avec chemin et empreinte :
- du programme : la liste des préalables, tenus ou non ; la table des écarts par couche et par cible, avec leur signe ; pour R, le
  compte des matrices égales et les deux séries ; les empreintes des pièces lues et le commit donné ; la table des différences des
  deux manifestes (`versions`, `commit`, champs de la configuration hors préalables), **que le programme rend à tous les paliers,
  sans critère** ;
- à la main : les contrôles K1 à K5, repris un à un, en commençant par K1 ; la provenance des deux côtés (l'empreinte neuve vient du
  fichier de la course neuve — identifiant, heure, taille — et est relue au lieu de rangement après la copie ; la référence est lue
  dans la pièce du 18 par son empreinte ; les deux ne sortent pas du même fichier).
**Ce que l'audit peut conclure.** Un contrôle manqué suspend la mention et ouvre un nœud de Lazar ; un audit sans contrôle manqué
laisse la mention telle que la procédure l'a rendue. **L'audit ne fait jamais monter une mention.** Pour le déclencheur (vi), s'il ne
trouve aucun contrôle manqué, la mention du programme reste, sans montée, et le verdict l'écrit en une phrase (« pour R, [31 matrices
des moitiés égales sur 31 | série … inchangée] malgré des octets d'ajustement différents ; audit sans contrôle manqué ») ; aucune
identité, de la lentille ni de son export, n'en est tirée. (Le cas n'est pas d'école : si seules les sommes de la cible `mid`
diffèrent d'une machine à l'autre, le fichier d'ajustement change d'octets alors que l'export de R, moyenne des sommes de la cible
`out`, peut être le même.)
L'audit est versé scellé avec le verdict d'identité. **Aucune relance pour obtenir un autre palier sans devis neuf et mot de Lazar.**

## 7. Programme, essais, et ce qui reste à la main
**Programme en vigueur, le seul que ce critère cite** : `src/controle_ia/neuron_lens/comparer_reajustement_v3.py`
(`c8fc62034f2e4e1c18e803c9108598c1d70b74b6c2eab61fef1eb653fdd89d3a`) ; essais `tests/test_neuron_lens_comparer_reajustement_v3.py`
(`5996a4150062c619a5a0e748d572ab8bdff108a8fb79d176821c0bd4300dc35e`). Empreintes recalculées par le rédacteur, égales à leur
compagnon. Pièce écrite par la session des lentilles, que le rédacteur cite sans la modifier. Il lit les deux résultats d'ajustement,
les deux manifestes, pour R les deux résultats d'export, le texte des deux lanceurs, et, dans le dépôt qu'on lui donne, les correctifs
aux deux commits des manifestes ; il vérifie les pièces de référence contre le § 2 ; il rend la mention, les déclencheurs (i) à (vii),
les préalables, la table des écarts, le compte des matrices égales, les séries de R, la table des différences des manifestes, les
empreintes des pièces lues et le commit de la branche de résultats qu'on lui donne ; il verse sa ligne de commande et refuse d'écraser
une sortie (R12). La tolérance (10⁻³), la borne de cohérence (10⁻⁹), les bornes sur `diffs` (10⁻⁶ et 10⁻³), le seuil de stabilité
(0,10) et les cinq empreintes de référence sont des constantes. Une valeur non finie, non numérique ou absente rend « non comparable »
(ou suspend le premier palier) avant tout maximum. Son en-tête et deux commentaires nomment le « critère v3 » ou « v4 et suivants » :
ce sont des étiquettes ; les règles qu'il calcule sont celles du § 4 de ce texte.
**Essais** : 123, sur les pièces du 18 lues par leurs empreintes vraies et sur des copies altérées en mémoire ou dans un dossier
temporaire (cas sains des deux paliers ; bords de la tolérance, signe gardé ; causes de suspension du premier palier, dont la série
de R qui change et la borne de 10⁻⁹ des deux côtés ; provenance ; forme ; exports de R ; un essai par contrôle porté de la v4 et par
sonde ; déclencheurs ; pièces de référence modifiées d'un octet ; ligne de commande). **Rejoués par le rédacteur le 2026-11-19 :
`123 passed`.** Ligne non opposable (aucune sortie versée) : elle se refait par
`PYTHONPATH=src .venv/bin/python -m pytest -q tests/test_neuron_lens_comparer_reajustement_v3.py`.

**Sondes du rédacteur sur le programme v3 non modifié** (copies en mémoire des pièces du 18 ; hors dépôt, donc **non opposables**
tant que la mère ne les verse pas : `/tmp/claude-0/-home-user-controle-ia-travail/ff3e16f4-e2c5-5d31-b08c-99762b9cded7/scratchpad/redacteur-fable-critere-v5/sondes/sondes_v3_v1.py`
et, dans le même dossier, `sortie-sondes-v3-v1.txt`). Elles fondent la liste K et la règle de l'arrêt sur erreur :
| sonde | cas, au deuxième palier | rendu par le programme | traité par |
|---|---|---|---|
| U1 | manifeste neuf avec `depot_propre` faux | deuxième palier, rien dans la sortie | K2 |
| U2, U3 | champs du haut du manifeste neuf changés (`graines`, `preenregistrement`, `commande`) | deuxième palier, rien dans la table des différences | K5 |
| U4 | commit de la branche de résultats quelconque (« n'importe quoi ») | recopié tel quel, sans contrôle | K1 |
| U5 | clé neuve dans `versions`, d'un seul côté | « non comparable », la clé paraît dans la table | préalable (rien à la main) |
| U6 | champ neuf dans la configuration du manifeste neuf | deuxième palier, le champ paraît dans la table, sans critère | rapporté |
| U11 à U14 | résultat ou manifeste neuf qui n'est pas un dictionnaire ; `versions` en liste ; `correctifs` mal formé | arrêt sur une erreur, aucune sortie | règle de l'arrêt sur erreur (§ 4) |
Le lanceur neuf, lui, n'est rattaché à sa course par rien dans le programme : lu dans le code, sans sonde (K2).

**Ce qui reste à la main — liste fermée, K1 à K5, appliquée par qui applique le critère (§ 8), avec chemin et empreinte, dans les deux
sens et à tous les paliers. Aucun de ces contrôles ne peut faire monter une mention.** Chacun dit pourquoi le programme ne le fait pas.
- **K1 — Le bon programme sur les bonnes pièces.** Avant le lancement : l'empreinte du programme est celle de ce paragraphe. Après :
  le commit que porte la sortie (`commit_resultats`) est celui de la branche de résultats poussée par la machine, lu sur le dépôt
  distant ; chaque empreinte de pièce neuve que porte la sortie (`pieces_lues` : résultat d'ajustement, manifeste, résultat d'export
  pour R) est égale à celle du fichier du même chemin à ce commit (`git show <commit>:<chemin> | sha256sum`). *Pourquoi à la main* :
  le programme recopie le commit qu'on lui donne et ne lit pas la branche. Manqué : pas de verdict ; la comparaison est refaite sur
  les bonnes pièces, sous un nom de sortie neuf, et la première sortie est versée aussi.
- **K2 — Le code qui a tourné est celui du manifeste.** Le manifeste neuf porte `depot_propre` vrai ; le lanceur neuf donné au
  programme (empreinte `lanceur_neuf` de la sortie) est égal au fichier du même chemin au commit que porte le manifeste neuf ; le dépôt
  donné au programme est le dépôt de travail, où les deux commits des manifestes sont lisibles. *Pourquoi à la main* : le programme
  ne lit pas `depot_propre` et ne rattache pas le lanceur au commit. Manqué : « non comparable » (octets différents) ou mention
  suspendue (octets égaux).
- **K3 — Matériel de la machine neuve.** Le modèle de carte, la version du pilote et les versions de la machine sont recopiés dans le
  verdict depuis la pièce du matériel que le lanceur neuf verse (devis v5, § 5, point 5 g), **à tous les paliers, sans vis-à-vis au
  18, où ils ne sont pas consignés : le verdict l'écrit**. *Pourquoi à la main* : cette pièce n'est pas une entrée du programme.
  Manqué (pièce absente) : pas de verdict, nœud de Lazar.
- **K4 — Reprise sur sauvegarde.** Le journal de la course neuve est lu ; l'indication donnée au programme (`--reprise`, champ
  `reprise` de la sortie) dit ce que le journal dit. *Pourquoi à la main* : le programme ne lit pas le journal. Manqué (indication
  contraire au journal) : la comparaison est refaite comme en K1 ; journal absent ou illisible : pas de verdict, nœud de Lazar.
- **K5 — Champs du manifeste que la table du programme ne couvre pas.** Les champs du haut des deux manifestes (`commande`, `cree_le`,
  `decisif`, `graines`, `preenregistrement`, `reserves`, `config_sha256`, et tout champ présent d'un seul côté) sont comparés et leurs
  différences recopiées dans le verdict, **sans critère** : une course neuve a d'office une autre commande et une autre heure.
  (`depot_propre` relève de K2 ; `run_id` et `commit` sont dans la sortie du programme.) *Pourquoi à la main* : la table du programme
  s'arrête à `versions`, `commit` et la configuration. Manqué (relevé non fait) : pas de verdict.
Restent aussi à la main, par nature : la relecture au lieu de rangement (§ 4, point 5), l'audit (§ 6), le verdict d'identité et
l'avertissement à Lazar (§ 5, § 8).

**Défauts du programme v3 relevés par le rédacteur, sans effet sur ce critère tel qu'il est écrit** (le programme reste à la session
des lentilles ; le rédacteur ne l'a pas modifié) : K1, K2 et K5 pourraient être portés par le programme (il a déjà le dépôt en
argument) ; le champ `audit_requis` n'est posé que pour (vi) ; quatre formes de pièce mal formée arrêtent le programme sur une erreur
au lieu de rendre « non comparable » ; le champ `etape` du résultat d'export neuf n'est pas lu ; l'empreinte du fichier du lanceur de
référence n'est pas versée dans `pieces_lues` ; des étiquettes nomment encore le critère v3. Une version neuve du programme
demanderait une version neuve, courte, de ce critère : ce n'est pas un préalable à la création.

## 8. Qui applique
- Les empreintes des fichiers d'ajustement sont calculées par programme sur la machine, avant l'envoi.
- La comparaison est lancée **par la mère ou par un agent neuf qu'elle lance**, jamais par la session des lentilles, **avant toute
  lecture d'une mesure de la nouvelle course**, avec le programme scellé du § 7 **dont l'empreinte est vérifiée avant le lancement**,
  sur les pièces **prises sur la branche de résultats poussée par la machine** (commit noté et donné au programme), jamais sur une
  copie remise par la session des lentilles ; pour R, les deux pièces d'export sont toujours fournies ; l'indication d'une reprise est
  lue au journal de la course.
- La même personne applique les contrôles K1 à K5 et le point 5 de la procédure (relecture au lieu de rangement), puis l'audit du
  § 6 si un déclencheur est levé.
- La ligne de commande, la sortie, les relevés à la main et l'audit sont versés scellés avec le verdict d'identité ; le verdict est
  écrit, scellé et rapporté à Lazar par la mère, avec, au deuxième palier, l'avertissement du § 5.

## 9. Deux nœuds proposés à Lazar (hors critère ; rien ici ne change une règle)
Tous deux viennent de l'annexe de la vérification du programme v2 (`8cd01e58…`, remarques 6 et 7) ; ils sont posés dans le devis v5
(§ 7, décisions 6 et 7), dans le format de décision.
1. **Mesurer l'écart d'un réajustement par un essai court, avant la course.** Le même ajustement sur quelques dizaines de documents,
   sur deux machines, puis la comparaison des empreintes et des différences entre moitiés. Ce serait la première mesure de ce que ce
   critère dit non mesuré (§ 3), et elle dirait si le premier palier est plausible. **C'est une dépense** : nœud de Lazar, sur devis.
   Si Lazar l'accorde et que la tolérance du deuxième palier devait en être revue, ce serait par une version neuve de ce critère,
   écrite et contre-lue avant la course entière, jamais après.
2. **Faire verser par la course neuve un croquis numérique de chaque matrice** de chaque lentille (projections sur des vecteurs tirés
   d'une graine fixée, normes par couche). Le 18 n'a laissé aucune grandeur qui compare deux matrices : c'est pourquoi le deuxième
   palier dit « matrices non comparables ». Le croquis ne change rien au verdict de cette course-ci (le 18 n'en a pas) ; il rendrait
   un réajustement **futur** comparable matrice par matrice. Sans dépense propre (quelques minutes de processeur en fin de course),
   mais c'est un ajout au lanceur neuf et aux pièces versées : Lazar tranche.

## 10. Ce que ce critère ne fait pas
Il ne dit pas si une lentille réajustée est **bonne** : seules des mesures faites sur elle le disent (variante B, ou une course de
mesure à part, sur devis). Il ne fixe pas le statut de la seconde mesure ni le plan de sa lecture (pièces à part, scellées avant la
création). Il ne décide d'aucun usage dans le programme : chaque expérience le dira dans son préenregistrement (R1).
