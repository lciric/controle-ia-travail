<!-- Premier addendum lu avec SA-21 à SA-25 du second, produit par pieces/controle-fragments-second-addendum-v3.py ; pièce de travail, ne fait pas foi. -->
# Addendum d'écart déclaré au préenregistrement scellé de T0.7, étape B bis — contrôle carte-processeur de la sonde « attention », réserve R-PILE — v1

- **Auteur** : auteur neuf, sous-agent de la session mère (modèles notés sans identifiant). Il n'a écrit aucun fichier de l'étape
  B bis : ni le texte, ni ses brouillons, ni le code, ni les diagnostics, ni les contre-lectures.
- **Date (UTC)** : 2026-11-16, de 00:31 à 00:37 (`date -u`), brouillon 1 (`991ab560…`, gardé tel quel, R12).
- **Brouillon 2** : même auteur, 2026-11-16, de 00:50 à 00:50 (`date -u`) = brouillon 1 + les couples C1 à C5 et les mineurs
  m1 à m8 de `brouillons/T0.7-etape-B-bis-v1/contre-lecture-addendum-ecart-v1-brouillon1-v1.md`
  (`a5d0cc8a85cfd723d5b08258bd2515554b629667e27ad88981af3ff4bd3225c2`, « scellable après corrections » ; R-2956), appliqués par
  `brouillons/T0.7-etape-B-bis-v1/pieces/couples-addendum-ecart-v1-brouillon2-v1.py` ; les seize blocs du § 2 sont égaux à
  l'octet à ceux du brouillon 1 (vérifié par ce programme).
- **Version 1** : même auteur, 2026-11-16, de 00:53 à 00:53 (`date -u`) = brouillon 2 (`32d91c4c…`, gardé tel quel, R12) + les
  couples de `brouillons/T0.7-etape-B-bis-v1/pieces/couples-addendum-ecart-v1-version1-v1.py` (titre, date, statut, les deux
  marqueurs remplis, et les phrases du § 4 et du § 5 sur la quatrième passe) ; seize blocs égaux à l'octet à ceux du brouillon 2,
  donc du brouillon 1 (vérifié par ce programme).
- **Statut** : version 1, à sceller par la mère après la vérification éclair du différentiel brouillon 2 → cette version ;
  contre-lu au brouillon 1 (R2 ; R-2956) ; les points P1 et P1 bis du § 7 sont remplis (§ 4 et § 5). Il ne vaut addendum qu'après son scellement sous
  `prereg/` (fichier et compagnon `.sha256`) et l'inscription de sa ligne `ADDENDUM-ECART-1-BBIS` au registre voisin
  `registres/t07-etape-b-bis-v1-addenda-v1.md` et d'une ligne R- de `registres/decisions.md` (décision de la mère R-2955, § 7),
  **avant `CODE-BBIS`**. Texte qui fera foi : `prereg/T0.7-etape-B-bis-v1-addendum-ecart-v1.md` et son compagnon (R-2955, R-2956).
  Processeur seulement ; aucune machine, aucune dépense ; aucun résultat lu.

## 0. Texte scellé : il n'est pas remplacé

`prereg/T0.7-etape-B-bis-v1.md`, `0ae6210f954917fecff647f45a129961c0676517381becbffe1fd5ac7b90d9eb` (compagnon juste),
scellé le 2026-11-14 : ligne `| SCELLEMENT-BBIS | 2026-11-14T12:30:30Z | prereg/T0.7-etape-B-bis-v1.md | 0ae6210f… |` du
registre propre `registres/t07-etape-b-bis-v1.md` (R-2746). Il reste le texte cité, mot pour mot, par le code, la marche, la
lecture et le verdict. Cet addendum remplace, **dans ce texte et nulle part ailleurs**, les huit fragments du § 2 ; toute autre
phrase du texte scellé fait foi telle quelle ; « relance sous ce texte » (liste d'arrêt scellée, ligne 186) se lit
désormais « sous ce texte et cet addendum ». Les brouillons 4, 5 et 6 (`af612cbc…`, `99d88954…`,
`bf1be58e4be262b180e5ea952cafd7948942ff450614c901e97318500d874935`) restent des pièces de travail : ils ne font pas foi, et
leurs tableaux d'en-tête, leurs titres et leurs lignes de statut (dont la phrase fausse « non scellé » du brouillon 6, ligne 54 ;
majeur M1 de `contre-lecture-brouillon6-et-code-v3-v1.md`) ne sont pas repris.

## 1. Décision

Ligne `GO-2026-11-16-01` de `registres/go.md` (R-2950). Mot du directeur, verbatim, tel que la ligne le recopie :
« go recos sur les 6 décisions, on a dit go recos pendant l'autonomie ». Lecture écrite dans la même ligne, point (1) :
« **B bis** : les corrections au texte scellé `prereg/T0.7-etape-B-bis-v1.md` (`0ae6210f…`) sont portées par un **addendum
d'écart déclaré**, scellé à part au registre propre de B bis, le code v3 restant tel quel (R-2933, voie (ii)) ». « Au registre propre » est la formule de la mère, non le mot de
Lazar ; le registre propre n'admet que huit clés (§ 7) : inscription au registre voisin, R-2955, dit à Lazar (R-2956). La recommandation
acceptée est la voie (ii) du majeur M1 de `brouillons/T0.7-etape-B-bis-v1/code/contre-lecture-brouillon6-et-code-v3-v1.md`
(`35745eceffc3dd4ceeb75c5ec58701d34b44bad6480f5b60e6f2207a4418671a`), portée à Lazar par R-2933. Les décisions de la mère R-2917
et R-2919 sur ces couples, prises sur la prémisse fausse « texte non scellé », ne valaient que comme propositions (R-2933) ; elles
ne valent ici que par cette ligne. **Hors des dix-sept couples** (a1 à a5, b1, b2, c1 à c10) que R-2933 a portés à Lazar :
les ajouts m4 (premier écart) et m5 (deuxième écart), mineurs de la même contre-lecture ; m4 écrit ce que `marche_v3` fait
déjà, m5 étend R-PILE à la sonde d'ENC (la réserve s'écrit plus souvent, sans changer d'issue). **Dits à Lazar** par la mère,
dans la conversation, le 16 novembre vers 00:45 UTC, avant le scellement, avec l'affaiblissement du § 5, point 4 (« la sonde
lue à 300 époques n'est plus comparée à une référence d'une autre pile ») et le registre voisin du § 7 (R-2956). Aucun mot de
Lazar en retour sur ces points n'est consigné à la rédaction de ce brouillon, et aucun n'est revendiqué ici.

## 2. Les écarts

Source : le différentiel réel entre le texte scellé et le brouillon 6, plus les mineurs m4 et m5 de la contre-lecture du
brouillon 6 ; rien d'autre. Le texte scellé = brouillon 3 (`f104917f…`) + le couple mécanique du scellement
(`brouillons/T0.7-etape-B-bis-v1/pieces/couples-scellement-v1.py`, `4a42e3b7dc4ff9891df5c50881c99e9195ae4d0ff5169d810913c0712fcfe774`), qui touche les
lignes 5, 76, 93, 116 et 293 (vérifié par `diff`). Numéros de ligne : ceux du texte scellé (le brouillon 6 a 32 lignes de plus
après le titre : ligne scellée n = ligne n + 32 du brouillon 6). Chaque « ancien » figure une seule fois dans le texte scellé, chaque
« nouveau » une seule fois dans le brouillon 6 complété de m4 et m5 (vérifié par programme). Les citations sont exactes, au
caractère, dans les blocs. Les écarts sont nommés EC-1 à EC-8 pour ne pas être confondus avec les états E0 à
E6 du texte scellé.

### EC-1 — Plan d'analyse, point 5 (contrôle à la marche) (texte scellé, ligne 105)

Ancien :

```text
**contrôle à la marche** : un (cellule, pli) tiré par graine est réappris sur le processeur par `sondes.familles` ; écart relatif maximal des scores sur 256 actions tirées ≤ 10⁻⁴, sinon arrêt (erreur de chaîne).
```

Nouveau, qui fait foi :

```text
**contrôle à la marche** : un (cellule, pli) tiré par graine est réappris sur le processeur par `sondes.familles`, depuis le même départ (mêmes graines que la marche), à la couche et à la régularisation retenues pour ce couple, **dans les deux familles** (sous la variante (r1) : la linéaire seule) : la linéaire à 300 époques, l'attention à **3 époques** (`Reglages(epoques=3)`, les mêmes trois époques réapprises sur la carte) ; écart relatif maximal des scores sur 256 actions tirées ≤ 10⁻⁴ pour chacune, sinon arrêt (erreur de chaîne) ; la sonde « attention » de 300 époques du couple est réapprise une seconde fois sur la carte et doit être égale à la première au bit près (déterminisme), sinon arrêt. **Aucune issue « sans objet »** : une sonde apprise pour le contrôle en échec (perte ou paramètres non finis), à 3 ou à 300 époques, déterminisme compris, arrête (erreur de chaîne) ; le couple est tiré **à la fin de l'apprentissage, parmi les couples dont la sonde finale est finie**, dans le même ordre trié et avec la même graine (`bbis/egalite-carte`) ; aucun : arrêt (erreur de chaîne) ; après un arrêt de la garde de débit, aucun contrôle n'est joué (aucun score n'est écrit). Raison, écrite avant toute lecture : quand la sonde « attention » n'apprend rien ou presque, ses 300 époques amplifient les écarts d'arrondi entre deux piles de calcul au-delà de 10⁻⁴ (sans signal : 0,633 pour le paquet gelé contre lui-même sous un autre jeu d'instructions du processeur, 2,131·10⁻² entre la carte et le processeur à la répétition du 15 novembre ; signal faible : 4,0·10⁻²) ; avec un signal, non (au plus 1,9·10⁻⁵) ; à 3 époques, l'écart entre deux piles du processeur reste de 2,9·10⁻⁷ à 5,9·10⁻⁷ même sans signal (`brouillons/T0.7-etape-B-bis-v1/code/diagnostic-ecart-attention-carte-v1.md`, `5ecb9235…` ; `brouillons/T0.7-etape-B-bis-v1/code/diagnostic-stabilite-aires-attention-v1.md`, `dd67802d…`). **Répétition sur carte avant la course** (données synthétiques seulement ; mot de Lazar R-2802), **règle de lecture écrite avant la passe** : la passe ne compte que si chaque famille porte un écart numérique ≤ 10⁻⁴ (linéaire à 300 époques, attention à 3 époques) et l'égalité au bit près (déterminisme des deux familles et de l'attention du contrôle, lot reconstruit égal au premier) ; si l'écart de chaque famille est ≤ 10⁻⁵, la course part sans nœud ; entre 10⁻⁵ et 10⁻⁴, nœud écrit à la mère avant la course.
```

**Raison.** Sous le contrôle scellé, la sonde « attention » de 300 époques réapprise sur le processeur s'écarte de celle de la
carte bien au-delà de 10⁻⁴ dès qu'elle n'apprend rien ou presque, sans aucune erreur de chaîne : les 300 époques d'Adam amplifient
les écarts d'arrondi (paquet gelé contre lui-même sous un autre jeu d'instructions du processeur : 0,633 ; carte contre
processeur à la troisième passe de répétition : 2,131·10⁻² ; `brouillons/T0.7-etape-B-bis-v1/code/diagnostic-ecart-attention-carte-v1.md`,
`5ecb923525617e0a7d118ee57e712709e684a3a29e35a788ff4b9a173d175f37`, lignes 23, 39, 65 et 67 ; R-2869, R-2902). Le contrôle
scellé arrêterait donc à tort toute course dont le couple tiré porte une sonde « attention » sans signal. À 3 époques, l'écart
entre deux piles du processeur reste de 2,9·10⁻⁷ à 5,9·10⁻⁷ même sans signal (même rapport, ligne 163). Mesure des aires :
`brouillons/T0.7-etape-B-bis-v1/code/diagnostic-stabilite-aires-attention-v1.md`, `dd67802d181e4a367748836a4da0de9fe02c7f85eb33f60ea46027cd202cf85a`
(lignes 17 à 21). Couples a1 (`brouillons/T0.7-etape-B-bis-v1/pieces/couples-brouillon4-v1.py`,
`51135f43e1d921fa18cf20527295627d5550109807a274d8b2ffc67ba9f45012`), c1 à c4 (`brouillons/T0.7-etape-B-bis-v1/pieces/couples-brouillon6-v1.py`,
`b61ed1d32d5fef1b821eac4d6effe3b8d136f7498e126c5ef796fb05c0e03a57`) : arrêt sur sonde de contrôle en échec et tirage parmi les
sondes finales finies (voie (b) du majeur M2 de `brouillons/T0.7-etape-B-bis-v1/code/contre-lecture-brouillon5-et-code-v2-v1.md`,
`93b0724dd41b6c0bbfd2ace1ab47475bb3c0af86436361b0d184e5020c29af4e` : une perte non finie à 3 époques ne peut venir que
d'activations non finies, donc d'une erreur de chaîne ; R-2919) ; règle de lecture de la répétition écrite avant la passe (m3 et
m8 de la même contre-lecture ; la répétition elle-même est l'écart déjà accordé par R-2802). **Ajout m4** (phrase « après un arrêt
de la garde de débit, aucun contrôle n'est joué (aucun score n'est écrit) ») : mineur m4 de
`brouillons/T0.7-etape-B-bis-v1/code/contre-lecture-brouillon6-et-code-v3-v1.md`, `35745eceffc3dd4ceeb75c5ec58701d34b44bad6480f5b60e6f2207a4418671a` ;
il écrit ce que `marche_v3` fait déjà (même contre-lecture, § 3 et § 4, essai (a)). **Lecture déclarée** du bloc « nouveau » :
quand le réglage retenu du couple est linéaire, « la sonde « attention » de 300 époques du couple » est une sonde apprise sur la
carte au réglage « attention » de mêmes couche et régularisation, pour le seul contrôle ; ce n'est pas une sonde lue
(`src/controle_ia/t07bbis/validation_imbriquee_v3.py`, `71bffa5bf26c2b182bb81ebfb920c1246b6c9784b2332ff1304f0ff3c24890eb`,
docstring, lignes 9 à 22 ; § 5, point 4).

### EC-2 — Critères de lecture gelés, qualifications toujours écrites (réserve R-PILE) (texte scellé, ligne 155)

Ancien :

```text
**R-G3** (marque de la table A), audit R4 et ses motifs.
```

Nouveau, qui fait foi :

```text
**R-G3** (marque de la table A), **R-PILE** (écrite dès qu'une sonde finale lue, celle d'une source ou celle d'ENC, est de la famille « attention » : « sonde « attention » reproductible au bit près sur la même pile de calcul seulement (carte, pilote, versions de torch et de numpy) ; sur une autre pile, l'apprentissage peut rendre une autre sonde, surtout quand elle n'apprend rien » ; sur données synthétiques de la taille de la course, entre quatre piles de calcul du processeur (aucune carte), aires d'une sonde « attention » qui n'apprend rien (aire 0,46) d'étendue 0,0074, et d'étendue au plus 7,8·10⁻⁵ pour des sondes qui apprennent un signal (aires 0,56 à 0,98) ; `brouillons/T0.7-etape-B-bis-v1/code/diagnostic-stabilite-aires-attention-v1.md`, `dd67802d…`), audit R4 et ses motifs.
```

**Raison.** Le contrôle neuf ne compare plus la sonde « attention » de 300 époques lue à une référence calculée ailleurs :
elle n'est garantie qu'au bit près sur la même pile (déterminisme). La réserve dit cette limite à chaque lecture où une sonde
« attention » est lue. Chiffres (aires 0,46, étendue 0,0074 ; étendue au plus 7,8·10⁻⁵ pour des aires 0,56 à 0,98) :
`brouillons/T0.7-etape-B-bis-v1/code/diagnostic-stabilite-aires-attention-v1.md`, `dd67802d181e4a367748836a4da0de9fe02c7f85eb33f60ea46027cd202cf85a`,
lignes 17 à 21 et 102. Couples b1 (`couples-brouillon4-v1.py`, `51135f43…`) et c6 (`couples-brouillon6-v1.py`, `b61ed1d3…`).
**Ajout m5** (« celle d'une source ou celle d'ENC ») : mineur m5 de `contre-lecture-brouillon6-et-code-v3-v1.md` (`35745ece…`) ;
`lecture_v2.reserve_pile` compte déjà la sonde d'ENC (`src/controle_ia/t07bbis/lecture_v2.py`,
`154795f4ecfa3273a7a5cec91c6975cd34e558d14647bb8a1cb1ef4968972aca`, lignes 125 à 139) : le texte rejoint le code.

### EC-3 — Critères de lecture gelés, section D, point (7) (texte scellé, ligne 175)

Ancien :

```text
retient la condition « muette sur le jumeau ».
```

Nouveau, qui fait foi :

```text
retient la condition « muette sur le jumeau » ; (7) une aire de la famille « attention » est celle d'**une** sonde parmi celles que rendrait le même apprentissage sous d'autres arrondis (réserve R-PILE) : sur données synthétiques, la dispersion est négligeable quand la sonde apprend un signal, de l'ordre de 0,007 quand elle n'apprend rien ; sur de vraies activations, elle n'est pas mesurée.
```

**Raison.** Même limite que EC-2, dite dans « Ce que ces issues ne disent pas » ; chiffre 0,007 : la même pièce
(`dd67802d…`, ligne 17, étendue 0,0074). Couple b2 (`couples-brouillon4-v1.py`, `51135f43…`).

### EC-4 — Liste d'arrêt (contrôle carte-processeur) (texte scellé, ligne 186)

Ancien :

```text
- Contrôle carte-processeur de l'apprentissage au-delà de 10⁻⁴ : arrêt (erreur de chaîne) ;
```

Nouveau, qui fait foi :

```text
- Contrôle carte-processeur de l'apprentissage au-delà de 10⁻⁴ (linéaire à 300 époques, attention à 3 époques ; plan, point 5), sonde « attention » du couple non déterministe sur la carte, sonde apprise pour le contrôle en échec (perte ou paramètres non finis, à 3 ou à 300 époques), ou aucun couple à sonde finale finie : arrêt (erreur de chaîne) ;
```

**Raison.** La liste d'arrêt reprend, mot pour mot, les arrêts neufs de EC-1 (couples a2 et c5). La suite de la ligne scellée
(« correction du code sous un nom neuf, ligne `CODE-BBIS` remplacée une seule fois, relance sous ce texte ») est inchangée.

### EC-5 — Code neuf, module de validation imbriquée (texte scellé, ligne 227)

Ancien :

```text
`validation_imbriquee_v1` (plis, grille, sélection, sonde finale, nul de réétiquetage, ENC, garde de débit)
```

Nouveau, qui fait foi :

```text
`validation_imbriquee_v3` (plis, grille, sélection, sonde finale, nul de réétiquetage, ENC, garde de débit ; contrôle carte-processeur aux deux horizons du point 5, sans issue « sans objet », sur un couple tiré parmi les sondes finales finies, et déterminisme de la sonde « attention » du couple ; les v1 et v2 restent, R12)
```

**Raison.** Le contrôle de EC-1 est porté par un module à nom neuf (R12) ; `validation_imbriquee_v1` et `_v2` restent sans
changement. Couples a3 puis c7.

### EC-6 — Code neuf, module de lecture (texte scellé, ligne 227)

Ancien :

```text
`lecture_v1` (gardes, états, issue, phrases, réserves, audit R4 ;
```

Nouveau, qui fait foi :

```text
`lecture_v2` (la v1 reste, R12 ; gardes, états, issue, phrases, réserves dont R-PILE, point (7) de la section D, lecture du champ du contrôle carte-processeur, qui arrête la lecture s'il est « sans objet », absent ou non numérique ; audit R4 ;
```

**Raison.** R-PILE, le point (7) et la garde du champ du contrôle ne sont écrits par aucun code v1 (majeur M1 de
`contre-lecture-brouillon5-et-code-v2-v1.md`, `93b0724d…`) ; `lecture_v2` les porte, la v1 reste. Couple c8.

### EC-7 — Code neuf, lanceur et amorce de la course (texte scellé, ligne 227)

Ancien :

```text
scripts `scripts/lancer_bbis_v1.sh` et son amorce
```

Nouveau, qui fait foi :

```text
scripts `scripts/lancer_bbis_v3.sh` et son amorce `scripts/amorce_bbis_v3.sh` (marche `marche_v3`, qui appelle `validation_imbriquee_v3` ; les v1 et v2 restent, R12)
```

**Raison.** Noms v3 de la course (lanceur, amorce, marche) qui appellent `validation_imbriquee_v3`. Couples a5
(`pieces/couples-brouillon5-v1.py`, `8608d87c77f6380781667aecacd6b596ec242086106605038e921a2bc7619ffc`) puis c9.

### EC-8 — Code neuf, épreuves (égalité carte-processeur) (texte scellé, ligne 228)

Ancien :

```text
égalité carte-processeur ; garde de débit
```

Nouveau, qui fait foi :

```text
égalité carte-processeur (linéaire à 300 époques, attention à 3 époques ; artefacts : autre graine, poids altérés de 1 % ; déterminisme : cas sain et artefact ; sonde de contrôle en échec à 3 ou à 300 époques : arrêt ; couple tiré parmi les sondes finales finies : même couple et mêmes actions que la v1 si toutes sont finies, autre tirage si une ne l'est pas, aucun : arrêt ; R-PILE et champ du contrôle à la lecture : cas sain et artefacts) ; garde de débit
```

**Raison.** Chaque arrêt neuf a son cas sain et son artefact (R5). Couples a4 puis c10. Les épreuves existent et passent
(`contre-lecture-brouillon6-et-code-v3-v1.md`, `35745ece…`, § 4 et § 5 : 183 passés, 0 échec).

**Contrôle mécanique** (programme de l'auteur, hors du dépôt, rejoué sur les fichiers du commit `2dfb06db` de
`prep/t07bbis-code-v1`) : les huit remplacements appliqués au texte scellé donnent, ligne pour ligne, le brouillon 6 complété de
m4 et m5, sauf exactement les lignes 1 (titre), 22 (statut) et 5, 76, 93, 116, 293 (couple mécanique du scellement, que le
brouillon 6 n'a pas) : aucun autre fragment ne change. Rejoué par la contre-lecture du brouillon 1 (`a5d0cc8a…`, § 1 et annexe).
Les seize blocs du brouillon 2 sont ceux du brouillon 1 (`991ab560…`) à l'octet ; le même rejeu se fera sur la version scellée.

## 3. Ce qui ne change pas

Pour les huit écarts : **hypothèse, prédiction chiffrée et signe, métrique, seuil, niveaux de la règle (a) et épreuve de
niveau, puissance** : inchangés (aucune ligne de ces sections n'est touchée). **Plan d'analyse** : seul le contrôle à la marche
du point 5 change ; la grille de 18 réglages, les 300 époques et le pas 0,05 des sondes **apprises et lues**, le critère de choix
et ses ex aequo, la sonde finale, les planchers, le nul de réétiquetage, la notation, la garde de débit (11 h, facteur 1,2,
0,6 h) et les points 1 à 4 et 6 à 12 sont inchangés ; la tolérance 10⁻⁴ ne change pas. **Critères de lecture gelés** : aucun
état, aucune issue, aucun libellé ne change ; EC-2 et EC-3 ajoutent une réserve toujours écrite et un point à « ce que ces issues ne
disent pas ». **Liste d'arrêt** : seule la ligne du contrôle carte-processeur s'étend (EC-4). **Calcul et dépense** (40 USD,
`GO-2026-11-14-09`, une relance), calendrier, lignes de registre, données gardées : inchangés ; deux effets déclarés
sans changement de ces sections : le contrôle vient à la fin de l'apprentissage, donc un arrêt du contrôle coûte tout
l'apprentissage (§ 5, point 8), et il ajoute (second addendum) sur la carte, par famille de la marche, une sonde de 3 époques et au plus deux de 300 (la sonde finale du couple sert de première quand sa famille est retenue), et sur le processeur, par famille, une sonde de 3 époques, plus une linéaire de 300 époques pour l'information (`validation_imbriquee_v4`, docstring) ; la mesure de dispersion ajoute 730 apprentissages sur la carte (§ 6 du second addendum) ; le choix du réglage n'est pas modifié par cet addendum,
mais il peut dépendre de la pile (§ 5, point 6). EC-5 à EC-8 ne changent que des noms
de modules et la liste des épreuves.

## 4. Antériorité : aucun résultat de la course lu avant l'écart

- **Aucune course n'a eu lieu.** Le registre propre ne porte que `SCELLEMENT-BBIS` et `ABSENCE-B-BBIS` (relu à la
  rédaction) ; ni `CODE-BBIS`, ni `GO-BBIS`, sans lesquelles aucune création n'est permise (texte scellé, plan, point 2 ; garde
  `exiger_creation` de `src/controle_ia/t07bbis/registre_bbis_v1.py`, `c3b1848b3466a88a250aee2b58477c91ff5d660592c1a6cc695f8910005dcf1b`) ;
  aucune référence `donnees/t07-etape-b-bis*` dans les références locales du dépôt (relevé sans appel réseau, 2026-11-16) ;
  branche des données de la course absente du dépôt distant à 20:56 UTC le 15 novembre (contre-lecture du brouillon 6, § 3, ligne 183, par `git ls-remote`) ;
  absente encore à 2026-11-16T00:42:38Z (contre-lecture du brouillon 1 de cet addendum, `a5d0cc8a…`, § 3 : `git ls-remote
  --exit-code` de `refs/heads/donnees/t07-etape-b-bis-v1` et du motif `refs/heads/donnees/t07-etape-b-bis*` → code 2 ; témoin
  positif `refs/heads/prep/t07bbis-code-v1` → code 0) ; relevé de la mère au scellement : avec l'état de l'étape B, ci-dessous.
- **Seules des passes de répétition sur carte**, sur données synthétiques seulement, sans rien de 7a, 7b, T0.7 ni P3-bis, ont
  tourné : écart au texte scellé **déjà accordé** par R-2802 (mot de Lazar, verbatim : « Recommandation : (b), confiance 0,65 :
  go »). Passes : R-2844 (arrêt avant tout apprentissage, branche `calcul/t07bbis-repetition-v1`, `56f5b8b8`), R-2869 (troisième
  passe, arrêt en code 9 sur l'écart « attention » 2,131·10⁻², branche `calcul/t07bbis-repetition-v2`, `3528a2e8`, aucune aire).
  Le chiffre 2,131·10⁻² de EC-1 vient de cette passe synthétique, pas de la course. La quatrième passe (accordée par
  `GO-2026-11-16-01`, point (2)) : aucune référence `calcul/t07bbis-repetition-v4` dans les références locales à la rédaction du brouillon 1, ni à
  distance à 00:42:38Z ; la passe a tourné ensuite, sur données synthétiques seulement (machine 60858032, créée à
  00:35:00Z, détruite à 00:47:24Z, absence prouvée ; R-2953, R-2957) ; sa mesure : § 5, point 5 ;
  sa règle de lecture (EC-1, fin) était écrite avant elle, au brouillon 6, commit `6c346a03` du 2026-11-15T17:14:46Z.
- **Étape B de T0.7** : `ABSENCE-B-BBIS` (`registres/t07-etape-b-bis/ABSENCE-B-BBIS-v1.json`,
  `134ac847b89b7fb7beb3ccfb1d93aca6527a51107da2605da5ec504e426d9cfc`) l'établit au 14 novembre ; état relevé par la mère avant le
  scellement de cet addendum, le 2026-11-16T00:51:45Z (`date -u`), par la même méthode, par les noms seulement (`git ls-tree -r
  --name-only`, compte des chemins égaux au nom ou finissant par /nom, aucun fichier ouvert) : sur `main` au commit
  `120d8dc2440ba896a77d771c6e68b2ee27dafd4c`, `lecture-t07.json` 0 et `arret-etape-b.json` 0 ; sur `donnees/t07-etape-a-v1` au
  commit `0c176db582ec13705e8fb7cc2d281215e2766e42`, 0 et 0 : **absents, étape B non exécutée** ; à la même heure,
  `git ls-remote --exit-code origin refs/heads/donnees/t07-etape-b-bis-v1` rend le code 2 (branche de données de B bis
  absente) ; branches distantes dont le nom contient « t07 » : celles de `ABSENCE-B-BBIS`, plus `coffre/audit-fuites-t07-v1`,
  `prep/t07bbis-code-v1`, `calcul/t07bbis-repetition-v1`, `-v2` et `-v4` (point P1 du § 7). Les écarts portent sur la stabilité
  numérique d'une famille de sondes et ne lisent rien de l'étape B ; l'état est écrit par symétrie (R4).

## 5. Ce que le contrôle à 3 époques ne voit pas ; réserve R-PILE

Mesure : `brouillons/T0.7-etape-B-bis-v1/code/contre-lecture-brouillon5-et-code-v2-v1.md` (`93b0724d…`), § 3, 35 artefacts, largeur 1 024 au lieu de
4 096, côté « carte » joué sur le processeur. Il attrape 30 artefacts sur 35, toutes les erreurs de structure (couche, masque,
ordre, graine, famille, réglages d'Adam), avec un à cinq ordres de grandeur de marge ; cas sain 5,8·10⁻⁹ (sans signal) et
2,9·10⁻¹⁰ (avec). **Il ne voit pas** :
1. **toute erreur qui ne commence qu'après la troisième époque** (pas divisé par deux à partir de la quatrième : écart égal au cas
   sain) : aveugle par construction ; seuls l'identité du code de la boucle et le déterminisme la
   couvrent, sans comparaison directe ; **affaiblissement déclaré (second addendum)** : la linéaire à 300 époques, qui la couvrait, n'est plus un contrôle ; son écart carte-processeur n'est plus qu'une information, qui la signale sans la distinguer d'une amplification d'arrondi (§ 4 du second addendum) ;
2. une altération relative des poids sous ≈ 10⁻⁴ (le seuil lui-même ; biais décalé de 10⁻⁵ : non vu) et deux différences de
   formule d'effet sous le seuil (écart type à n − 1 degrés de liberté, 5,2·10⁻⁶ à 4,1·10⁻⁵ ; entrée en simple précision,
   3,4·10⁻⁸ à 7,8·10⁻⁷) ; le cinquième artefact non attrapé, actions et étiquettes permutées ensemble, n'est pas une erreur ;
3. une erreur en amont de l'apprentissage (relecture, couche, masque des séquences) qui toucherait la carte et le processeur de la
   même façon, à 3 époques comme à 300 : ce sont les gardes de la relecture qui la gardent, non ce contrôle ;
4. la sonde « attention » **lue** (300 époques) n'est plus comparée à une référence d'une autre pile : seul son déterminisme sur la
   carte est vérifié, et le déterminisme ne prouve pas la justesse (une erreur déterministe propre à la carte après la
   troisième époque passe les trois contrôles). **Second addendum** : la sonde **linéaire** lue (300 époques) n'est plus comparée non plus à une référence d'une autre pile ; seul son déterminisme sur la carte est vérifié, et son écart à 300 époques est écrit comme information : **affaiblissement déclaré**, de même forme que pour l'attention ; les sondes de 300 époques apprises pour le seul contrôle (famille non retenue du couple) ne sont pas des sondes lues ; les sondes « attention » des autres
   couples et celles d'ENC ne reçoivent aucun contrôle, comme au texte scellé. C'est un affaiblissement déclaré du contrôle scellé, accepté parce que ce dernier arrête sans erreur (EC-1) ;
5. jusqu'à la quatrième passe de répétition, rien n'avait été mesuré **sur carte** pour l'écart à 3 époques, l'égalité de deux
   lots construits sur la carte et le déterminisme à 300 époques (contre-lecture du brouillon 6, § 7). **Mesure de la quatrième
   passe** (données synthétiques seulement ; R-2953, R-2957 ; règle de lecture du premier écart) : branche
   `calcul/t07bbis-repetition-v4`, commit `75bc5b325c1668821f8626c5f415ea3e24c7feb6` (parent `ce470564`), fichier
   `traces/bbis-t07-repetition-v4/repetition-carte.json`, `cbcaeb5242583d99d11c2c02a8dbfa559a0a9551887f816f7a47e643e63a35a4`
   (par `git show`, recalculée par l'auteur) : code 0 ; essais sur la machine « 115 passed, 24 skipped »
   (`traces/bbis-t07-repetition-v4/essais.txt`, `6fc36ceb73b92ad652667f1fe29a9877a1f7e5674c15b375609c5237ec317409`) ; carte A100
   SXM4 80 Go, torch 2.14.1+cu130 ; fraction de la course 1,0 (640 actions, largeur 4 096) ; écart de la linéaire à 300 époques
   1,954·10⁻⁸, de l'attention à 3 époques 1,486·10⁻⁸ (256 actions, tolérance 10⁻⁴) — **requalifié (second addendum)** : 1,954·10⁻⁸ ne prouve le bon fonctionnement de la pile de la carte que sur un bruit gaussien isotrope indépendant en simple précision, où la sonde ajuste bien ; il ne dit rien des régimes qui ajustent mal, où la course du 16 novembre a donné 1,004 ; la linéaire à 3 époques n'a pas été mesurée sur carte ; déterminisme vrai pour les deux familles ;
   attention à 300 époques égale au bit près ; lot reconstruit égal au premier ; `lecture_de_la_passe` : compte, issue « la
   course part sans nœud » (seuil 10⁻⁵) ; mémoire de carte au plus 10 361 273 856 octets. **Ce que la passe ne prouve pas** :
   elle porte sur des données synthétiques sans signal apprenable, non sur les activations de 7b ; elle ne joue ni le tirage du
   couple en fin d'apprentissage (`ControleCarte.jouer`), ni `marche_v3`, ni `lecture_v2`, ni la relecture ; un seul jeu de
   réglages (couche 15, l2 = 10⁻³ au contrôle) ; elle ne dit rien d'une autre carte ni d'une autre pile. Le contrôle porte sur un seul couple tiré, comme au texte scellé ;
6. le réglage retenu peut dépendre de la pile : sans signal, l'étendue 0,0074 dépasse le seuil d'ex aequo 0,005 ; la
   famille, la couche ou la régularisation retenues, donc l'écriture même de R-PILE, peuvent changer d'une pile à l'autre
   (`diagnostic-stabilite-aires-attention-v1.md`, `dd67802d…`, lignes 24 et 106) ; l'état rapporté est celui de la carte de la
   course ;
7. les régimes mesurés sont ceux d'un bruit gaussien isotrope ; entre les aires 0,47 et 0,56, et pour un signal faible mêlé
   à une forte mémorisation, rien n'est mesuré (même pièce, ligne 108) ; l'horizon de 3 époques a été fixé sur ces trajectoires
   synthétiques (`diagnostic-ecart-attention-carte-v1.md`, `5ecb9235…`, lignes 161 à 169) ;
8. un couple dont la sonde finale est en échec n'est jamais contrôlé ; le contrôle vient à la fin de l'apprentissage : une
   erreur de chaîne coûte tout l'apprentissage (mineur m7 de la contre-lecture du brouillon 6 ; le pire cas du devis compte
   déjà une relance complète).

**R-PILE** (EC-2, EC-3 ; second addendum, SA-2, SA-3 et SA-10) : une aire de sonde, linéaire ou « attention », est celle d'**une**
sonde parmi celles que rendrait le même apprentissage sous d'autres arrondis ; sur données fabriquées, dispersion négligeable
quand la sonde apprend un signal, de l'ordre de 0,007 quand une sonde « attention » n'apprend rien, de 0,007 à 0,047 quand une
sonde linéaire ajuste mal ; **sur de vraies activations, elle est mesurée entre deux ordres de calcul de la carte, comme
information seulement, et non entre la carte et une autre pile**. La réserve ne change aucune issue ; elle borne ce que le
verdict peut dire d'une aire de sonde proche du hasard.

## 6. Rattachement du code v3 ; ce que le verdict cite

- Le code v3 reste tel quel. Il cite l'empreinte du **texte scellé** et lui seul : `src/controle_ia/t07bbis/commun_v1.py`
  (`9db2b40b15c9ca76f0c4bd4f29923cc06909b362de26a212bfc780133a4c9e33`), lignes 27 et 28, `TEXTE = "prereg/T0.7-etape-B-bis-v1.md"`,
  `TEXTE_SHA256 = "0ae6210f…"` ; `lecture_v2` (`154795f4…`) écrit `texte_sha256 = 0ae6210f…` (ligne 1124) et refuse toute ligne
  `SCELLEMENT-BBIS` d'un autre chemin ou d'une autre empreinte (ligne 1137). Ni la marche ni la lecture ne connaissent
  l'addendum ; l'amorce n'extrait que `/prereg/T0.7-etape-B-bis-v1.md*` : l'addendum ne monte pas sur l'instance, et n'a pas à y
  monter, car le code v3 fait déjà ce que les huit écarts écrivent (contre-lecture du brouillon 6, § 2 : `validation_imbriquee_v3`
  `71bffa5b…`, `marche_v3` `7009b34d…`, `lecture_v2` `154795f4…`, `scripts/amorce_bbis_v3.sh` `18e2f205…`,
  `scripts/lancer_bbis_v3.sh` `dc26ea01…`, conformes ; m4 et m5 écrivent au texte ce que le code fait).
- **Liste de la fiche `CODE-BBIS` v3** : `brouillons/T0.7-etape-B-bis-v1/code/fichiers-fiche-code-bbis-v3.txt`,
  `b8fb095bf44dc855868e1b48cef6005222af6888b00a9df2f60fccc36ded7d5d`, **103 chemins** (compté), dont les modules et scripts nommés
  par EC-5 à EC-7 ; l'addendum n'y figure pas (ce n'est pas du code).
- **Le verdict devra citer** : (a) le texte scellé, son empreinte et sa ligne `SCELLEMENT-BBIS` ; (b) cet addendum, son empreinte
  et sa ligne `ADDENDUM-ECART-1-BBIS` du registre voisin ; (c) la ligne `CODE-BBIS` (commit, fiche, entropie, épreuve de niveau) ; (d) lire les critères du texte
  scellé **modifiés par EC-1 à EC-4** — en particulier écrire R-PILE et le point (7) quand ils s'appliquent, et tenir pour arrêt
  chacun des cas de EC-4. Comme la sortie de `lecture_v2` ne porte que `0ae6210f…`, le lecteur neuf du verdict (R13) ajoute la
  citation de l'addendum à la main et vérifie que la lecture rendue porte R-PILE et le point (7) selon EC-2 et EC-3.
- **Recevabilité** : un verdict de B bis qui ne cite pas cet addendum, son empreinte et sa ligne n'est pas scellé ; la mère le
  vérifie avant de le soumettre à Lazar. L'addendum figure nommément dans la liste des fichiers donnés au lecteur du verdict
  (R13) et dans `registres/etat.md` ; la table conjointe et tout document qui cite une aire de B bis le citent aussi. Il
  n'entre pas dans la liste de la fiche `CODE-BBIS` (`marche_v3` vérifie chaque fichier de la fiche sur l'instance, où il
  n'est pas extrait).

## 7. Points ouverts avant le scellement

- **P1** — remplir le marqueur de l'état de l'étape B (§ 4) par l'état de l'étape B de T0.7 à l'heure du scellement,
  relevé par la mère par les noms seulement (`git ls-tree`), comme pour `ABSENCE-B-BBIS`.
- **P1 bis** — remplir le marqueur de la mesure de la quatrième passe (§ 5, point 5),
  puis rejouer le contrôle des seize blocs ; une vérification éclair par un lecteur neuf suffit (différentiel du brouillon 2 à
  la version scellée).
- **P2** — **lieu de la ligne de scellement (tranché, R-2955).** La ligne de décision dit « scellé à part au registre
  propre de B bis ». Or le texte scellé (« Lignes de registre », ligne 222) ne permet au registre propre que huit clés de marque
  `BBIS`, et le code v3 refuse toute autre clé de bonne forme qui s'y trouverait : `lecture_v2.lire_lignes`
  (`src/controle_ia/t07bbis/lecture_v2.py`, `154795f4…`, lignes 520 à 553 ; clés permises, ligne 513) rend « registre propre :
  clé … inconnue » et la lecture refuse ; `registre_bbis_v1` (`c3b1848b…`, lignes 42, 97 et 98) refuse de l'écrire et relit le
  registre propre de la même façon pour `CODE-BBIS` (lignes 212 à 215) ; le registre partagé est exclu (texte scellé, ligne 222 ;
  `t07/registre_v1.py`, `e50236574fbcd7e48ea3005eadc8bdb68d2c753d10028db7f2c365648a843cec`, lignes 136 à 148). Une ligne
  `ADDENDUM-…-BBIS` au registre propre rendrait donc la course illisible. **Décision de la mère (R-2955)** : registre voisin à nom neuf
  `registres/t07-etape-b-bis-v1-addenda-v1.md` (lu par aucun code ; nom hors des motifs d'extraction de l'amorce), clé
  `ADDENDUM-ECART-1-BBIS`, et ligne R- ; aucune ligne au registre propre ni au registre partagé ; une forme de clé que le code
  ignorerait est écartée (ce serait passer une garde par sa forme). Fichier scellé : `prereg/T0.7-etape-B-bis-v1-addendum-ecart-v1.md`.

## 8. Fichiers à donner au contre-lecteur (R2)

Lecture seule, sur la branche `prep/t07bbis-code-v1` (commit `2dfb06db` ou suivant) :
- cet addendum, son brouillon 1 et `contre-lecture-addendum-ecart-v1-brouillon1-v1.md` (`a5d0cc8a…`), avec le programme de
  couples du brouillon 2 ; `prereg/T0.7-etape-B-bis-v1.md` (`0ae6210f…`) ; `brouillons/T0.7-etape-B-bis-v1/T0.7-etape-B-bis-v1-brouillon3.md` et
  `-brouillon6.md` ; `brouillons/T0.7-etape-B-bis-v1/pieces/couples-scellement-v1.py`, `couples-brouillon4-v1.py`, `couples-brouillon5-v1.py`,
  `couples-brouillon6-v1.py` ;
- `brouillons/T0.7-etape-B-bis-v1/code/contre-lecture-brouillon5-et-code-v2-v1.md`, `contre-lecture-brouillon6-et-code-v3-v1.md`,
  `corrections-controle-attention-v1.md` (`45aeddba99a7a710a412ee048b42de589b771e17ea6a929f45ab3e74e40d91e5`),
  `corrections-controle-attention-v2.md` (`4e4fad18cff93589b6ba8b1a1a27bada52ed3f4c13a768e39c1a6f1d979a37ec`),
  `diagnostic-ecart-attention-carte-v1.md`, `diagnostic-stabilite-aires-attention-v1.md`, `fichiers-fiche-code-bbis-v3.txt` ;
- `src/controle_ia/t07bbis/commun_v1.py`, `validation_imbriquee_v3.py`, `marche_v3.py`, `lecture_v2.py` (lignes 100 à 140,
  505 à 553, 1120 à 1140), `registre_bbis_v1.py` (en-tête, lignes 40 à 100 et 205 à 220) ;
- dans le dépôt principal : `registres/t07-etape-b-bis-v1.md` ; `registres/go.md`, ligne `GO-2026-11-16-01` ;
  `registres/decisions.md`, lignes R-2746, R-2802, R-2844, R-2869, R-2902, R-2917, R-2919, R-2931, R-2933, R-2950, R-2953, R-2955, R-2956 (une à une, par
  `grep -n '^| R-NNNN '`).
- Questions à lui poser : chaque « ancien » est-il exact et à sa ligne, chaque « nouveau » exact ; le contrôle mécanique du § 2
  se rejoue-t-il ; reste-t-il un changement du brouillon 6 hors des huit écarts, ou un écart qui n'en vienne pas ; le § 5 est-il
  complet ; P2 est-il bien posé.
- Interdits : rien sous `diag/`, `donnees/`, `docs/verdicts/` ; aucune entrée de 7a ou 7b ; aucune valeur de clé ; ni `env`, ni
  `printenv` ; pas d'extraction entière d'un commit ; ni `pytest` ni git sous des variables `GIT_*` pointées ailleurs.
