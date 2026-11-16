# Vérification éclair (R2) du différentiel brouillon 2 → version 1 de l'addendum d'écart de T0.7, étape B bis — v1

- **Lecteur** : sous-agent neuf de la session mère (modèle noté sans identifiant). Je n'ai écrit aucun fichier de l'étape B bis.
- **Heure (UTC, `date -u`)** : rapport écrit à 2026-11-16T00:58:50Z ; lecture depuis 00:54:37Z.
- **Pièces** (branche `prep/t07bbis-code-v1`, commit `7683e2e7`, tête distante égale à 00:55:25Z ; empreintes recalculées,
  compagnons justes) : brouillon 1 `991ab56066c229c2a04cfa0489e6cbe0f2b11a717587d305fdcfb65ea1582efe` ; brouillon 2
  `32d91c4c6ec74ec52400e327c4196c0cc201c493c80aaa69592592ef2610b416` ; version 1
  `f00eda8a9fb74516289a085350425d128bf5b1cf1dbc50eee32d8bbe749c78d7` ; contre-lecture du brouillon 1
  `a5d0cc8a85cfd723d5b08258bd2515554b629667e27ad88981af3ff4bd3225c2` ; programmes de couples
  `d8394a1727cdd9588ddbcc1199d926f8a3884273bf2e0e9186cab763f3477ca4` (brouillon 2) et
  `7778e697e27c2696fb63adec71f55bfbe369067b914c90c7ea21122490c2be7a` (version 1) ; texte scellé
  `0ae6210f954917fecff647f45a129961c0676517381becbffe1fd5ac7b90d9eb` ; brouillon 6 `bf1be58e…`.
- Processeur seulement ; aucune machine, aucun appel payant ; rien ouvert sous `diag/`, `donnees/`, `docs/verdicts/` ; aucune
  entrée de 7a ou 7b ; ni `env` ni `printenv` ; ni clone ni extraction entière ; aucun `pytest` ; rien committé ; rien inscrit.

## Verdict

**Scellable tel quel** (`f00eda8a…`). Les six points demandés tiennent ; aucune correction n'est exigée. Quatre mineurs de
rédaction, dont l'intitulé du § 7 ; des couples exacts sont donnés **à titre facultatif** (les appliquer change l'empreinte et
demande de rejouer le contrôle des seize blocs ; ne pas les appliquer ne trompe pas le lecteur du verdict, voir point 6).

## 1. Brouillon 1 → brouillon 2

- **Rejeu** : copie du seul brouillon 1 dans un sous-dossier neuf du bloc-notes, programme copié à part, lancé par `python -I` :
  code 0 ; sortie **égale à l'octet** au brouillon 2 du dépôt (`cmp`, `32d91c4c…`). Le différentiel est donc exactement la
  liste du programme : C2 (22 lignes) puis 26 couples ; 35 régions de lignes (compte par `difflib`, programme à moi).
- **C1 à C5 et m1 à m8 appliqués** : quatorze fragments des couples de la contre-lecture (C1 début, phrase de C2, C3 § 1, C3 P2
  en deux parts, C3 § 6, C4 point 4, points 6, 7, 8, artefact, C5, m1, m2) figurent chacun une fois dans la contre-lecture et
  une fois dans le brouillon 2, aux blancs près (programme à moi). C2 : hors des blocs, plus aucun « E1 » à « E8 » nu ; seule
  mention restante, « états E0 à E6 du texte scellé », voulue. m3 et m4 (§ 3), m5 (§ 4), m6 (raison de EC-1, bloc intouché),
  m7 (§ 8), m8 : lus dans le programme et dans le texte.
- **Ce qui dépasse la lettre des couples, relevé un à un, sans objection** : (a) forme du brouillon (titre, date, statut) ;
  (b) C1 : le marqueur du message à Lazar proposé par la contre-lecture est remplacé par la forme de la mère (« vers 00:45
  UTC », R-2956, registre voisin ajouté) et par la phrase « Aucun mot de Lazar en retour … n'est revendiqué » : plus prudent
  que le couple ; (c) C3 : nom de la clé `ADDENDUM-ECART-1-BBIS` et phrase « Texte qui fera foi », conformes à R-2956 ;
  (d) m7 : R-2953 et R-2956 ajoutées en plus de R-2955 ; (e) deux marqueurs posés (§ 4 et § 5) et P1, P1 bis réécrits sans le
  nom du marqueur : mise en œuvre de m5 et m8. Aucun changement de fond hors de la contre-lecture.

## 2. Brouillon 2 → version 1

- **Rejeu** de même (copie du seul brouillon 2, `python -I`) : code 0 ; sortie **égale à l'octet** à la version 1 (`f00eda8a…`).
- Six couples, cinq régions de lignes : titre (ligne 1), ligne « Version 1 » ajoutée et statut (lignes 11 à 16), phrase du § 4
  sur la passe (lignes 262 et 263), marqueur de l'état de l'étape B rempli (lignes 266 à 273), point 5 du § 5 et marqueur de la
  mesure rempli (lignes 295 à 308). Rien d'autre.
- **Plus aucun marqueur** : zéro « << » et zéro « >> » dans la version 1 ; ni « ANCIEN-P2-RETIRE ».

## 3. Blocs et contrôle mécanique (programme à moi, `python -I`)

- Seize blocs dans chacune des trois pièces (32 clôtures, toutes « text ») ; ceux de la version 1 sont **égaux à l'octet** à
  ceux du brouillon 1 ; étiquettes dans l'ordre « Ancien », « Nouveau, qui fait foi », huit fois.
- Chaque « ancien » : une fois dans le texte scellé ; chaque « nouveau » : zéro fois dans le texte scellé, une fois dans le
  brouillon 6 complété de m4 et m5 (chaque « ancien » de m4 et m5 : une fois dans le brouillon 6).
- Texte scellé + huit remplacements, comparé ligne à ligne au brouillon 6 complété (deux voies : `difflib`, puis retrait des
  lignes 2 à 33 du brouillon 6 et comparaison directe, 294 lignes contre 294) : seules diffèrent les lignes **1, 5, 22, 76, 93,
  116, 293** (titre, statut, couple mécanique). Conforme à la phrase du § 2 de l'addendum.

## 4. Valeurs des deux marqueurs

**État de l'étape B, par les noms seulement** (relevé à 2026-11-16T00:55:23Z à 00:55:25Z) :

| référence | commit | chemins | `lecture-t07.json` | `arret-etape-b.json` | témoin positif `CLAUDE.md` |
|---|---|---|---|---|---|
| `refs/remotes/origin/main` | `120d8dc2440ba896a77d771c6e68b2ee27dafd4c` | 26 337 | 0 | 0 | 1 |
| `refs/remotes/origin/donnees/t07-etape-a-v1` | `0c176db582ec13705e8fb7cc2d281215e2766e42` | 23 278 | 0 | 0 | 1 |

- Compte des chemins égaux au nom ou finissant par « / » + le nom ; aucun fichier ouvert. Les deux commits sont ceux du texte ;
  `git ls-remote` rend les mêmes têtes à distance à la même heure. En plus (hors demande) : même compte, 0, sur la tête locale
  non poussée de `main` du dépôt principal (`35ff87cf`).
- `git ls-remote --exit-code origin refs/heads/donnees/t07-etape-b-bis-v1` : **code 2** ; motif `…t07-etape-b-bis*` : code 2 ;
  témoin positif (quatre références existantes) : code 0.
- Branches distantes dont le nom contient « t07 » : dix-sept ; les douze de `ABSENCE-B-BBIS`
  (`registres/t07-etape-b-bis/ABSENCE-B-BBIS-v1.json`, `134ac847…`, recalculée) plus `coffre/audit-fuites-t07-v1`,
  `prep/t07bbis-code-v1`, `calcul/t07bbis-repetition-v1`, `-v2`, `-v4` : **égal au texte**.
- Variables `GIT_*` : voir « Incidents ».

**Mesure de la quatrième passe** (`git show refs/remotes/origin/calcul/t07bbis-repetition-v4:traces/bbis-t07-repetition-v4/repetition-carte.json`,
3 423 octets, empreinte recalculée `cbcaeb5242583d99d11c2c02a8dbfa559a0a9551887f816f7a47e643e63a35a4` ; commit
`75bc5b325c1668821f8626c5f415ea3e24c7feb6`, parent `ce470564…`, daté 2026-11-16T00:46:42Z ; `"donnees": "synthétiques seulement"`,
`"aucune_aire": true`) :

| valeur citée au § 5, point 5 | valeur du fichier | accord |
|---|---|---|
| code 0 | `code` 0, `etat` « reussie » | oui |
| « 115 passed, 24 skipped » ; `essais.txt` `6fc36ceb…` | dernière ligne de `essais.txt`, empreinte recalculée égale | oui |
| carte A100 SXM4 80 Go ; torch 2.14.1+cu130 | « NVIDIA A100-SXM4-80GB » ; « 2.14.1+cu130 » | oui |
| fraction 1,0 ; 640 actions ; largeur 4 096 | 1.0 ; 640 ; 4096 | oui |
| linéaire, 300 époques : 1,954·10⁻⁸ | 1.9539638351773192e-08, `epoques` 300 | oui |
| attention, 3 époques : 1,486·10⁻⁸ | 1.4862957808947641e-08, `epoques` 3 | oui |
| 256 actions ; tolérance 10⁻⁴ | 256 ; 0.0001 (les deux familles) | oui |
| déterminisme vrai pour les deux familles | `deterministe` : vrai, vrai | oui |
| attention à 300 époques égale au bit près | `egal_au_bit` vrai, écart 0.0, `epoques` 300 | oui |
| lot reconstruit égal au premier | `egal_au_premier` vrai | oui |
| `lecture_de_la_passe` : compte, « la course part sans nœud », seuil 10⁻⁵ | vrai ; même chaîne ; 1e-05 | oui |
| mémoire de carte au plus 10 361 273 856 octets | 10361273856 | oui |
| couche 15, l2 = 10⁻³ au contrôle | `controle_parametres` : 15 ; 0.001 | oui |

- § 4 : machine 60858032, « créée à 00:35:00Z, détruite à 00:47:24Z, absence prouvée » : `registres/depenses.md`, ligne 476
  (00:35:00Z → 00:47:24Z), `registres/arrets.md`, ligne 129, R-2957. R-2953, citée, ne dit que « 00:35 UTC » : la seconde
  vient de la ligne de dépense, non citée (mineur, sans couple).

## 5. Ce que la passe ne prouve pas ; étendue de l'accord du directeur

- **Dit, et juste** : données synthétiques, non les activations de 7b ; ni le tirage du couple (`ControleCarte.jouer`), ni
  `marche_v3`, ni `lecture_v2`, ni la relecture ; un seul jeu de réglages ; rien d'une autre carte ni d'une autre pile.
  Concorde avec R-2957 (« ne prouve ni le tirage en fin d'apprentissage, ni la marche, ni la lecture ») et avec le script de
  la passe (`scripts/repetition_carte_bbis_v3.py` de la branche de la passe, `355b3133…` : il appelle
  `controle_deux_horizons` directement ; aucune mention de `ControleCarte`, de `marche_v3` ni de `lecture_v2`).
- **« sans signal apprenable »** : le générateur du script plante un léger décalage des positifs (0,5 le long d'une direction,
  sur le premier quart des jetons) et sa docstring dit « la sonde apprend quelque chose ». La formule de l'addendum est pourtant
  sourcée : `code/diagnostic-stabilite-aires-attention-v1.md` (`dd67802d…`), lignes 13 et 27 (« jeu de la répétition ; les
  sondes n'apprennent rien qui se généralise, aire « attention » 0,46 » ; « sans signal apprenable »). Juste, mais la source
  n'est pas citée à cet endroit : mineur, couple facultatif F3.
- **Accord du directeur, pas plus large qu'il n'est** : le § 1 recopie le mot verbatim de la ligne `GO-2026-11-16-01`
  (`registres/go.md`, ligne 342 : « go recos sur les 6 décisions, on a dit go recos pendant l'autonomie ») ; il distingue la
  lecture de la mère du mot de Lazar (« Au registre propre » : formule de la mère) ; il dit que m4 et m5 sont **hors** des
  dix-sept couples portés par R-2933 ; il dit qu'ils ont été « dits à Lazar », avec l'affaiblissement et le registre voisin,
  et qu'**aucun mot de Lazar en retour n'est consigné ni revendiqué**. Vérifié : `registres/go.md` ne porte au 16 novembre que
  les lignes -01 et -02, aucune sur m4, m5, l'affaiblissement ou le registre voisin ; R-2955 et R-2956 disent « décision de la
  mère » et « dit à Lazar par la mère » ; le registre voisin est partout attribué à la mère (statut, § 1, § 7). La quatrième
  passe est rattachée au point (2) de la ligne et à R-2953, R-2957 ; le fichier de la passe porte `GO-2026-11-14-09` et
  R-2802 pour la dépense et l'écart, comme le texte.
- Réserve que le texte porte déjà et que je répète : m4, m5, l'affaiblissement du § 5, point 4, et le registre voisin sont
  scellés **sur le dire de la mère à Lazar, sans mot de Lazar en retour**. « vers 00:45 UTC » : R-2956 écrit « à 00:4x UTC » ;
  je n'ai pas d'autre source de la minute (la conversation ne m'est pas donnée).

## 6. Identifiants de modèle ; § 7

- **Aucun identifiant de modèle** dans la version 1 (recherche sans casse de neuf noms de familles et de fournisseurs : seuls
  des fragments d'empreintes hexadécimales répondent). L'auteur est « noté sans identifiant ».
- **§ 7, « Points ouverts avant le scellement »** : l'intitulé et l'impératif de P1 et P1 bis (« remplir le marqueur ») sont
  périmés dans un texte sans marqueur. **Pas trompeur sur le fond** pour le lecteur du verdict : le statut (lignes 15 et 16)
  dit « les points P1 et P1 bis du § 7 sont remplis (§ 4 et § 5) », P2 porte « tranché, R-2955 », le § 4 renvoie au « point P1
  du § 7 » avec la valeur. **Un couple de plus n'est pas exigé** ; F1 est offert si la mère préfère un texte sans ambiguïté.

## Mineurs et couples facultatifs (sur la version 1 ; chaque « ancien » y figure une fois, vérifié)

- **F1 — ligne 349.** Ancien : « ## 7. Points ouverts avant le scellement ». Nouveau : « ## 7. Points ouverts au brouillon 1,
  remplis (P1, P1 bis : § 4 et § 5) ou tranché (P2 : R-2955) avant le scellement ».
- **F2 — ligne 49.** Ancien : « n'est consigné à la rédaction de ce brouillon, et aucun ». Nouveau : « n'est consigné à la
  rédaction de cette version, et aucun ». (« ce brouillon » est resté du brouillon 2 ; l'énoncé reste vrai à 00:55 UTC.)
- **F3 — ligne 306.** Ancien : « elle porte sur des données synthétiques sans signal apprenable, non sur les activations de
  7b ; ». Nouveau : « elle porte sur des données synthétiques sans signal apprenable (décalage planté faible, rien qui se
  généralise : `diagnostic-stabilite-aires-attention-v1.md`, `dd67802d…`, lignes 13 et 27), non sur les activations de 7b ; ».
- Sans couple : ligne 228, « le même rejeu se fera sur la version scellée » (fait : lignes 13 et 14, et ce rapport) ; § 8,
  liste des lignes R- sans R-2957, que les § 4 et § 5 citent ; « créée à 00:35:00Z » sourcée par la ligne de dépense, non
  par R-2953.
- Si un de ces couples est appliqué : nom neuf ou empreinte neuve (R12), rejeu du contrôle des seize blocs ; ce rapport ne vaut
  que pour `f00eda8a…`.

## Ce que je n'ai pas vérifié

- Aucun essai rejoué (`pytest` interdit) : « 115 passed, 24 skipped » et « 183 passés » sont lus, non refaits.
- Le dire à Lazar (heure, contenu) : connu par R-2955 et R-2956 seulement.
- Les pièces citées par les § 0, § 2 (raisons), § 5 (points 1 à 3) et § 6 : couvertes par la contre-lecture du brouillon 1, non
  relues ici ; du diagnostic de stabilité, deux lignes seulement.
- La destruction de la machine : lue aux registres, aucun inventaire fait par moi.
- Les références locales suivies valent à l'heure du relevé ; je n'ai fait aucun `git fetch`.

## Incidents de ma main

- **Variables `GIT_*`** : la consigne demandait « sans variable `GIT_*` ». Onze noms sont présents dans l'environnement de
  l'outil (relevés par leur nom seul, `compgen -v`, aucune valeur affichée) : `GIT_ASKPASS`, `GIT_CONFIG_COUNT`,
  `GIT_CONFIG_KEY_0` à `_2`, `GIT_CONFIG_VALUE_0` à `_2`, `GIT_EDITOR`, `GIT_SSL_CAINFO`, `GIT_TERMINAL_PROMPT`. Aucune
  ne déplace le dépôt (ni `GIT_DIR`, ni `GIT_WORK_TREE`, ni `GIT_INDEX_FILE`, ni `GIT_OBJECT_DIRECTORY`, ni
  `GIT_NAMESPACE`). Je ne les ai pas retirées (réglages du relais réseau de la session) ; les commandes git ont donc tourné
  avec elles.
- Lu hors de la liste donnée, sans résultat de course : `registres/t07-etape-b-bis/ABSENCE-B-BBIS-v1.json` (liste des
  branches) ; `registres/depenses.md` ligne 476, `registres/arrets.md` ligne 129, `registres/etat.md` lignes 3 et 5 (600
  premiers caractères, pour la machine 60858032) ; sur la branche de la passe, par `git show` d'un fichier à la fois : les
  trois dernières lignes de `essais.txt`, des lignes du script `scripts/repetition_carte_bbis_v3.py` (générateur synthétique,
  appels) et une ligne de `scripts/amorce_repetition_bbis_v3.sh` ; la liste des noms de `traces/bbis-t07-repetition-v4/` ;
  lignes 13 et 27 du diagnostic de stabilité. R-2953 et R-2957 lues en entier.
- Une recherche du motif de date dans `registres/go.md` a rendu, en plus des deux lignes voulues, les 200 premiers caractères
  de dix-huit lignes de GO des 2 et 7 novembre, sans rapport, dont certaines nomment des modèles d'autres tâches ; vus, non
  repris.
- Deux recherches larges de noms (« lecture-t07 », « arret-etape-b » en sous-chaîne) ont rendu six noms de notes de
  contre-lecture sous `docs/notes/` par référence : des noms seulement, aucun n'est un des deux fichiers comptés.
- Trois sorties trop longues (version 1 entière, contre-lecture entière, deux fois) ont été rangées par l'outil dans des
  fichiers de résultats hors du dépôt ; relues ensuite par tranches.
- J'ai d'abord tenu « sans signal apprenable » pour une erreur (docstring du générateur) avant de trouver sa source au
  diagnostic ; laissé visible au point 5.
- Écritures : ce rapport, son compagnon, et le sous-dossier neuf `verif-eclair-addendum-v1` du bloc-notes (copies, deux
  rejeux, trois programmes à moi, une liste de noms). Aucun fichier existant modifié.
