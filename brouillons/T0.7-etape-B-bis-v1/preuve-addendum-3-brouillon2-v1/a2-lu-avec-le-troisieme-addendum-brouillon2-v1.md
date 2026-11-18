<!-- A2 lu avec TA-1 à TA-5 du brouillon 2 du troisième addendum, produit par controle-fragments-addendum-3-brouillon2-v1.py ; pièce de travail, ne fait pas foi. -->
# Second addendum d'écart déclaré au préenregistrement scellé de T0.7, étape B bis — contrôle carte-processeur v4, réserve R-PILE étendue à la linéaire, mesure de dispersion entre deux ordres de calcul, nouvelle course — v1

- **Auteur** : rédacteur-développeur neuf (lettre de modèle A), sous-agent de la session mère. Il n'a écrit ni le texte scellé,
  ni ses brouillons, ni le premier addendum, ni le code v1 à v3, ni le diagnostic de l'arrêt, ni sa contre-lecture. Lecteur
  déclaré de T0.7 (exclu des lecteurs de P3-bis).
- **Date (UTC, `date -u`)** : de 2026-11-16T23:12Z à 2026-11-17T00:01Z (déclaration du rapport compagnon).
- **Brouillon 2** : rédacteur neuf des corrections (lettre de modèle A ; n'a écrit ni le brouillon 1, ni sa contre-lecture, ni le code ; lecteur déclaré de T0.7, exclu des lecteurs de P3-bis), de 2026-11-17T00:38Z à 2026-11-17T01:18Z (`date -u`, la seconde au scellement) = brouillon 1 (`a582e14dd22fd17e…`, gardé tel quel, R12) + les couples K1 à K7 de la contre-lecture du tour 1, appliqués au caractère par `pieces/couples-brouillon2-second-addendum-v1.py` ; hors de ces couples, seuls changent cet en-tête (titre, statut, cette ligne) et la section 11, ajoutée.
- **Brouillon 3** : rédacteur neuf de la correction du tour 2 (lettre de modèle A ; n'a écrit aucun des brouillons 1 et 2, ni leurs contre-lectures, ni le code ; lecteur déclaré de T0.7, exclu des lecteurs de P3-bis), de 2026-11-17T01:43Z à 2026-11-17T01:56Z (`date -u`, la seconde au scellement) = brouillon 2 (`ab66d5fa67a64067…`, gardé tel quel, R12) + le couple m1 de la contre-lecture du tour 2, appliqué au caractère par `pieces/couples-brouillon3-second-addendum-v1.py` ; hors de ce couple, seuls changent cet en-tête (titre, statut, cette ligne) et la section 11 (intertitre et note du tour 1, dont le texte est gardé tel quel ; tour 2 ajouté à la fin).
- **Statut** : **version 1, scellée sous `prereg/T0.7-etape-B-bis-v1-addendum-ecart-2-v1.md`.**
  Contre-lecture faite en trois tours (tours 1 et 2 par un lecteur C, tour 3 par un lecteur C ; tous neufs, R2) ;
  corrections exigées appliquées aux brouillons 2 et 3 ; verdict du tour 3 : scellable, aucune correction exigée.
  Ligne `ADDENDUM-ECART-2-BBIS` au registre `registres/t07-etape-b-bis-v1-addenda-v1.md`, **avant** la seconde ligne `CODE-BBIS`
  (condition de GO-2026-11-16-11). Processeur seulement ; aucune machine, aucune dépense ; aucun score, aucune donnée de 7a ou de 7b lus.

## 0. Textes qui font foi ; ce que cet addendum remplace

- Texte scellé `prereg/T0.7-etape-B-bis-v1.md`, `0ae6210f954917fecff647f45a129961c0676517381becbffe1fd5ac7b90d9eb` (« T »), ligne
  `SCELLEMENT-BBIS` du registre propre ; premier addendum `prereg/T0.7-etape-B-bis-v1-addendum-ecart-v1.md`,
  `f00eda8a9fb74516289a085350425d128bf5b1cf1dbc50eee32d8bbe749c78d7` (« A1 »), ligne `ADDENDUM-ECART-1-BBIS` du registre voisin.
  « T+1 » désigne T lu avec les huit remplacements EC-1 à EC-8 de A1.
- Cet addendum remplace, **dans T+1 et dans A1 et nulle part ailleurs**, les fragments SA-1 à SA-25 du § 2 (« SA » pour « second
  addendum », afin de ne confondre ces écarts ni avec EC-1 à EC-8 ni avec les états E0 à E6). Toute autre phrase de T et de A1
  fait foi telle quelle, à une exception : là où un bloc EC-1 à EC-8 de A1, ou un paragraphe de son § 3, de son § 5 ou de son § 6, dit autre chose qu'un fragment SA ou que le texte de ce § 2, le second addendum fait foi (les blocs EC de A1 restent lisibles comme l'histoire du premier écart, non comme le texte en vigueur). Chaque « ancien » figure **une seule fois** dans son document, chaque « nouveau » est cité au caractère ;
  le contrôle est fait par programme (`pieces/controle-fragments-second-addendum-v1.py`, sortie et texte en vigueur dans
  `pieces/`, § 9).

## 1. Décisions

- **GO-2026-11-16-11** (`registres/go.md`, R-3031), mot direct de Lazar, verbatim tel que la ligne le recopie : « c’est à toi de
  l’accorder. : go » (réponse à : « accepter un second addendum à B bis (contrôle carte-processeur v4) et une nouvelle course ? …
  Recommandation : (a), confiance 0,65 »). Lecture de la ligne : le contrôle « linéaire à 300 époques » est remplacé par carte
  contre processeur à 3 époques (tolérance 10⁻⁴), déterminisme au bit près à 300 époques sur la carte, écart à 300 époques écrit
  comme information ; affaiblissements déclarés ; R-PILE étendue à la linéaire ; **conditions** : second addendum contre-lu par un
  lecteur neuf et scellé avant que `CODE-BBIS` soit remplacée ; code v4 contre-lu ; une nouvelle course, une seule (« la relance
  unique du texte est consommée ; ce mot en accorde une de plus, une seule »), sous la ligne de dépense GO-2026-11-14-09 ; feu écrit
  de la mère avant toute location ; arrêt et destruction par identifiant (R10).
- **GO-2026-11-16-12** (R-3031), mot direct de Lazar, verbatim : « (ii) En plus, mesurer la dispersion des aires entre deux
  ordres de calcul. Avantage : on chiffre le risque. Inconvénient : un coût, que le brouillon chiffre : go ». Lecture de la ligne :
  réserve R-D tranchée par l'option (ii) : R-PILE étendue à la linéaire **et** une mesure d'information de la dispersion des aires
  des sondes entre deux ordres de calcul (deux piles), écrite ici avant le scellement, sans changer aucune issue, aucun état ni
  aucun seuil ; coût chiffré ici (§ 6) ; elle part sous GO-2026-11-14-09 si elle y tient avec la course, sinon nouveau mot de
  Lazar avant la course.
- **La relance** : le texte scellé ne permet qu'une relance (« une relance au plus », ligne GO-2026-11-14-09 ; liste d'arrêt :
  « une seconde relance est exclue ») ; elle a été **consommée** par le troisième feu (R-3003 : premier départ perdu sur la garde
  CUDA, relance au compteur 1), qui s'est arrêté sur le contrôle carte-processeur (R-3025). **La nouvelle course demande le mot
  de Lazar** : c'est GO-2026-11-16-11, et lui seul ; aucune autre course n'est permise par ce texte (SA-15).

## 2. Les écarts

### SA-1 — Plan, point 5, contrôle à la marche (document : T+1 ; remplace le « nouveau » de EC-1)

Ancien :

```text
**contrôle à la marche** : un (cellule, pli) tiré par graine est réappris sur le processeur par `sondes.familles`, depuis le même départ (mêmes graines que la marche), à la couche et à la régularisation retenues pour ce couple, **dans les deux familles** (sous la variante (r1) : la linéaire seule) : la linéaire à 300 époques, l'attention à **3 époques** (`Reglages(epoques=3)`, les mêmes trois époques réapprises sur la carte) ; écart relatif maximal des scores sur 256 actions tirées ≤ 10⁻⁴ pour chacune, sinon arrêt (erreur de chaîne) ; la sonde « attention » de 300 époques du couple est réapprise une seconde fois sur la carte et doit être égale à la première au bit près (déterminisme), sinon arrêt. **Aucune issue « sans objet »** : une sonde apprise pour le contrôle en échec (perte ou paramètres non finis), à 3 ou à 300 époques, déterminisme compris, arrête (erreur de chaîne) ; le couple est tiré **à la fin de l'apprentissage, parmi les couples dont la sonde finale est finie**, dans le même ordre trié et avec la même graine (`bbis/egalite-carte`) ; aucun : arrêt (erreur de chaîne) ; après un arrêt de la garde de débit, aucun contrôle n'est joué (aucun score n'est écrit). Raison, écrite avant toute lecture : quand la sonde « attention » n'apprend rien ou presque, ses 300 époques amplifient les écarts d'arrondi entre deux piles de calcul au-delà de 10⁻⁴ (sans signal : 0,633 pour le paquet gelé contre lui-même sous un autre jeu d'instructions du processeur, 2,131·10⁻² entre la carte et le processeur à la répétition du 15 novembre ; signal faible : 4,0·10⁻²) ; avec un signal, non (au plus 1,9·10⁻⁵) ; à 3 époques, l'écart entre deux piles du processeur reste de 2,9·10⁻⁷ à 5,9·10⁻⁷ même sans signal (`brouillons/T0.7-etape-B-bis-v1/code/diagnostic-ecart-attention-carte-v1.md`, `5ecb9235…` ; `brouillons/T0.7-etape-B-bis-v1/code/diagnostic-stabilite-aires-attention-v1.md`, `dd67802d…`). **Répétition sur carte avant la course** (données synthétiques seulement ; mot de Lazar R-2802), **règle de lecture écrite avant la passe** : la passe ne compte que si chaque famille porte un écart numérique ≤ 10⁻⁴ (linéaire à 300 époques, attention à 3 époques) et l'égalité au bit près (déterminisme des deux familles et de l'attention du contrôle, lot reconstruit égal au premier) ; si l'écart de chaque famille est ≤ 10⁻⁵, la course part sans nœud ; entre 10⁻⁵ et 10⁻⁴, nœud écrit à la mère avant la course.
```

Nouveau, qui fait foi :

```text
**contrôle à la marche** (second addendum) : à la fin de l'apprentissage, un (cellule, pli) est tiré par graine (`bbis/egalite-carte`) **parmi les couples dont la sonde finale est finie**, dans le même ordre trié ; aucun : arrêt (erreur de chaîne) ; à la couche et à la régularisation retenues pour ce couple, **dans les deux familles** (sous la variante (r1) : la linéaire seule) : la sonde apprise **3 époques** sur la carte (`Reglages(epoques=3)`, depuis le même départ, mêmes graines que la marche) est réapprise 3 époques sur le processeur par `sondes.familles` ; écart relatif maximal des scores sur 256 actions tirées ≤ 10⁻⁴ pour chacune, sinon arrêt (erreur de chaîne) ; la sonde de 300 époques de chaque famille (la sonde finale du couple si sa famille est retenue, sinon apprise sur la carte à ce réglage pour le seul contrôle) est réapprise une seconde fois sur la carte et doit être égale à la première au bit près (déterminisme), sinon arrêt ; **l'écart carte-processeur de la sonde linéaire à 300 époques est calculé et écrit comme information, sans arrêt** (il ne décide rien ; lecture : discriminant à double sens, § 4 du second addendum). **Aucune issue « sans objet »** : une sonde apprise pour le contrôle en échec (perte ou paramètres non finis), à 3 ou à 300 époques, déterminisme compris, arrête (erreur de chaîne) ; après un arrêt de la garde de débit, aucun contrôle n'est joué (aucun score n'est écrit). Après le contrôle, la **mesure de dispersion entre deux ordres de calcul** (« Métrique ») est jouée, puis les fichiers fermés sont écrits ; ses apprentissages sont des « apprentissages restants » de la garde de débit. Raison, écrite avant toute lecture d'un score : quand une sonde, linéaire ou « attention », ajuste mal, ses 300 époques d'Adam amplifient les écarts d'arrondi entre deux piles ou deux ordres de calcul au-delà de 10⁻⁴, sans aucune erreur de chaîne (linéaire, données fabriquées : 0,59 à 12,8, avec ou sans jetons presque identiques ; course du 16 novembre : 1,004) ; à 3 époques, l'écart reste au plus de l'ordre de 10⁻¹⁰ pour la linéaire et de 10⁻⁹ à 6·10⁻⁷ pour l'attention (`brouillons/T0.7-etape-B-bis-v1/diagnostic-carte-processeur-v1/rapport-diagnostic-carte-processeur-v1.md`, `1fefa0a9…` ; `contre-lecture-diagnostic-v1.md`, `0da982fb…` ; pour l'attention : `brouillons/T0.7-etape-B-bis-v1/code/diagnostic-ecart-attention-carte-v1.md`, `5ecb9235…`). **Répétition sur carte** : celle que ce point exigeait avant la course a été jouée et comptée (quatrième passe, R-2957 : linéaire à 300 époques 1,954·10⁻⁸, attention à 3 époques 1,486·10⁻⁸, déterminisme des deux familles, lot reconstruit égal au premier) ; aucune répétition neuve n'est exigée avant la course du second addendum (déclaré : la linéaire à 3 époques, le déterminisme de la linéaire dans le contrôle v4 et la mesure de dispersion n'ont tourné sur aucune carte avant elle).
```

**Raison.** Sous le contrôle de EC-1, la sonde linéaire de 300 époques réapprise sur le processeur s'est écartée de celle de la
carte de 1,004 (R-3025), sans erreur de chaîne trouvée au code (diagnostic, § 3 ; contre-lecture, § 2, point 1) ; l'écart d'ordre
1 se reproduit sans carte par le seul ordre des sommes, et à 3 époques il reste sous 10⁻¹⁰. **Caractérisation corrigée (réserve
R-A)** : le diagnostic écrivait (§ 1 et § 4) que, sans jetons presque identiques, « tout reste sous 10⁻¹⁰ » et que la linéaire
est « stable, comme la v3 l'avait supposé » ; c'est **faux en général** : la contre-lecture trouve l'amplification d'ordre 1
**sans aucune quasi-copie**, dans un régime anisotrope de bas rang où la sonde ajuste mal (écarts 0,59 ; 1,01 ; 1,34 ; 2,25 ;
4,51 à 300 époques, au plus 4·10⁻¹² à 3 époques ; perte finale 0,53 à 0,60 ; `contre-lecture-diagnostic-v1.md`, § 2, tableau ;
sortie `contre-lecture-sortie-essai-independant-v1.txt`, `ff5a6730…`), et ses quasi-copies à 40 % n'ont pas divergé. Les
quasi-copies ne sont donc ni nécessaires ni suffisantes ; la question « y a-t-il des jetons presque identiques dans les vraies
activations ? » n'est pas la bonne ; le mécanisme retenu est la **sensibilité de la fin de l'apprentissage aux arrondis dans les
régimes qui ajustent mal**. Le balayage préalable du diagnostic, aux sorties non gardées, n'est plus cité comme preuve (mineur M2
de la contre-lecture). Code : `validation_imbriquee_v4.controle_deux_horizons` (§ 7).

### SA-2 — Critères gelés, qualifications toujours écrites, réserve R-PILE (document : T+1 ; remplace le « nouveau » de EC-2)

Ancien :

```text
**R-G3** (marque de la table A), **R-PILE** (écrite dès qu'une sonde finale lue, celle d'une source ou celle d'ENC, est de la famille « attention » : « sonde « attention » reproductible au bit près sur la même pile de calcul seulement (carte, pilote, versions de torch et de numpy) ; sur une autre pile, l'apprentissage peut rendre une autre sonde, surtout quand elle n'apprend rien » ; sur données synthétiques de la taille de la course, entre quatre piles de calcul du processeur (aucune carte), aires d'une sonde « attention » qui n'apprend rien (aire 0,46) d'étendue 0,0074, et d'étendue au plus 7,8·10⁻⁵ pour des sondes qui apprennent un signal (aires 0,56 à 0,98) ; `brouillons/T0.7-etape-B-bis-v1/code/diagnostic-stabilite-aires-attention-v1.md`, `dd67802d…`), audit R4 et ses motifs.
```

Nouveau, qui fait foi :

```text
**R-G3** (marque de la table A), **R-PILE** (second addendum : écrite dès qu'une sonde finale lue, linéaire ou « attention », celle d'une source ou celle d'ENC, l'est : « sonde finale (linéaire ou « attention ») reproductible au bit près sur la même pile de calcul seulement (carte, pilote, versions de torch et de numpy) ; sur une autre pile ou dans un autre ordre de calcul, l'apprentissage peut rendre une autre sonde, surtout quand elle ajuste mal, et le réglage retenu peut changer (ex aequo à 0,005) », suivie des sondes lues par famille et du résumé de la mesure de dispersion entre deux ordres de calcul (écart absolu maximal des aires et sa cellule, nombre de plis dont le réglage retenu change, ou « mesure non faite » et son motif, ou « non lue », ou « aucune cellule calculable ») ; sur données fabriquées : aires d'une sonde « attention » qui n'apprend rien d'étendue 0,0074 entre quatre piles du processeur (`brouillons/T0.7-etape-B-bis-v1/code/diagnostic-stabilite-aires-attention-v1.md`, `dd67802d…`), aires d'une sonde linéaire qui ajuste mal différant de 0,007 à 0,047 entre deux ordres de calcul (`brouillons/T0.7-etape-B-bis-v1/diagnostic-carte-processeur-v1/contre-lecture-diagnostic-v1.md`, `0da982fb…`, § 2)), audit R4 et ses motifs.
```

**Raison.** Le contrôle v4 ne compare plus la sonde linéaire lue à une référence d'une autre pile (SA-22) : la limite de R-PILE
vaut désormais pour les deux familles (mot de Lazar, GO-2026-11-16-11 : « R-PILE étendue à la linéaire »). Comme toute sonde
finale lue est linéaire ou « attention », **R-PILE s'écrit à chaque lecture** où une sonde finale est lue. Le résumé de la mesure
(GO-2026-11-16-12) y est porté. Code : `lecture_v3.reserve_pile`, `phrase_dispersion` (la phrase entre guillemets est égale, au
caractère, à `RESERVES_FIXES["R-PILE"]` après « R-PILE : », vérifié par programme, § 9).

### SA-3 — Critères gelés, section D, point (7) (document : T+1 ; remplace le « nouveau » de EC-3)

Ancien :

```text
retient la condition « muette sur le jumeau » ; (7) une aire de la famille « attention » est celle d'**une** sonde parmi celles que rendrait le même apprentissage sous d'autres arrondis (réserve R-PILE) : sur données synthétiques, la dispersion est négligeable quand la sonde apprend un signal, de l'ordre de 0,007 quand elle n'apprend rien ; sur de vraies activations, elle n'est pas mesurée.
```

Nouveau, qui fait foi :

```text
retient la condition « muette sur le jumeau » ; (7) une aire de sonde, linéaire ou « attention », est celle d'**une** sonde parmi celles que rendrait le même apprentissage sous d'autres arrondis (réserve R-PILE) : sur données fabriquées, la dispersion va de négligeable, quand la sonde apprend un signal, à plusieurs centièmes quand elle ajuste mal (0,007 à 0,047 entre deux ordres de calcul) ; sur les vraies activations, elle est mesurée entre deux ordres de calcul de la carte, comme information seulement (« dispersion entre ordres de calcul ») ; elle n'est pas mesurée entre la carte et une autre pile.
```

**Raison.** Même limite que SA-2, dite dans « Ce que ces issues ne disent pas ». Chiffres : contre-lecture, § 2, point 3
(« les aires lues des deux piles diffèrent de 0,007 à 0,047 ») ; diagnostic, § 4 (0,02 à 0,04). Code : `lecture_v3.SECTION_D`
(égal au caractère, gras retiré, vérifié par programme).

### SA-4 — Liste d'arrêt, contrôle carte-processeur (document : T+1 ; remplace le « nouveau » de EC-4)

Ancien :

```text
- Contrôle carte-processeur de l'apprentissage au-delà de 10⁻⁴ (linéaire à 300 époques, attention à 3 époques ; plan, point 5), sonde « attention » du couple non déterministe sur la carte, sonde apprise pour le contrôle en échec (perte ou paramètres non finis, à 3 ou à 300 époques), ou aucun couple à sonde finale finie : arrêt (erreur de chaîne) ;
```

Nouveau, qui fait foi :

```text
- Contrôle carte-processeur de l'apprentissage au-delà de 10⁻⁴ (les deux familles à 3 époques ; plan, point 5), sonde de 300 époques d'une famille non déterministe sur la carte, sonde apprise pour le contrôle en échec (perte ou paramètres non finis, à 3 ou à 300 époques), ou aucun couple à sonde finale finie : arrêt (erreur de chaîne) ; l'écart de la linéaire à 300 époques n'arrête pas (information) ;
```

**Raison.** La liste d'arrêt reprend les arrêts de SA-1, mot pour mot.

### SA-5 — Liste d'arrêt, suite de la ligne du contrôle (document : T+1 ; fragment du texte scellé, ligne 186, que EC-4 laissait)

Ancien :

```text
correction du code sous un nom neuf, ligne `CODE-BBIS` remplacée une seule fois, relance sous ce texte.
```

Nouveau, qui fait foi :

```text
correction du code sous un nom neuf, ligne `CODE-BBIS` remplacée une seule fois (au registre propre : une seconde ligne `CODE-BBIS`, ajoutée après `GO-BBIS` et avant la création de la course qu'accorde GO-2026-11-16-11, strictement postérieure à la première, qui fait foi ; la première reste ; jamais une troisième), relance sous ce texte ; pour l'arrêt du 16 novembre (R-3025), la correction est celle du second addendum et la course qui suit est celle qu'accorde GO-2026-11-16-11, sous ce texte et ses deux addenda.
```

**Raison.** « Remplacée une seule fois » dans un registre où les lignes sont « ajoutées, jamais réécrites » se lit ici sans
ambiguïté : le code v1 à v3 refuse toute clé en double (`lecture_v1.lire_lignes`, `lecture_v2.lire_lignes` : « ligne CODE-BBIS
en double ou mal formée » ; `registre_bbis_v1.ajouter_ligne_propre` : « déjà présente ») ; sans cette lecture, la course
qu'accorde GO-2026-11-16-11 ne pourrait ni partir ni être lue. Code : `lecture_v3.lire_lignes` (`remplacables`),
`lecture_v3.exiger_ordre_propre`, `registre_bbis_v2.ajouter_ligne_propre`.

### SA-6 — Code neuf, module de validation imbriquée (document : T+1 ; remplace le « nouveau » de EC-5)

Ancien :

```text
`validation_imbriquee_v3` (plis, grille, sélection, sonde finale, nul de réétiquetage, ENC, garde de débit ; contrôle carte-processeur aux deux horizons du point 5, sans issue « sans objet », sur un couple tiré parmi les sondes finales finies, et déterminisme de la sonde « attention » du couple ; les v1 et v2 restent, R12)
```

Nouveau, qui fait foi :

```text
`validation_imbriquee_v4` (plis, grille, sélection, sonde finale, nul de réétiquetage, ENC, garde de débit ; contrôle carte-processeur des deux familles à 3 époques, déterminisme des deux familles à 300 époques, écart linéaire à 300 époques en information, sans issue « sans objet », sur un couple tiré parmi les sondes finales finies ; mesure de dispersion entre deux ordres de calcul ; les v1 à v3 restent, R12)
```

### SA-7 — Code neuf, module de lecture (document : T+1 ; remplace le « nouveau » de EC-6)

Ancien :

```text
`lecture_v2` (la v1 reste, R12 ; gardes, états, issue, phrases, réserves dont R-PILE, point (7) de la section D, lecture du champ du contrôle carte-processeur, qui arrête la lecture s'il est « sans objet », absent ou non numérique ; audit R4 ;
```

Nouveau, qui fait foi :

```text
`lecture_v3` (les v1 et v2 restent, R12 ; gardes, états, issue, phrases, réserves dont R-PILE étendue à la linéaire et le résumé de la mesure de dispersion, point (7) de la section D, lecture du champ du contrôle carte-processeur v4, qui arrête la lecture s'il est « sans objet », absent, non numérique, d'une autre version ou d'un autre horizon, ligne `CODE-BBIS` remplacée une seule fois ; audit R4 ;
```

### SA-8 — Code neuf, lanceur, amorce, marche (document : T+1 ; remplace le « nouveau » de EC-7)

Ancien :

```text
scripts `scripts/lancer_bbis_v3.sh` et son amorce `scripts/amorce_bbis_v3.sh` (marche `marche_v3`, qui appelle `validation_imbriquee_v3` ; les v1 et v2 restent, R12)
```

Nouveau, qui fait foi :

```text
scripts `scripts/lancer_bbis_v6.sh` et son amorce `scripts/amorce_bbis_v6.sh` (marche `marche_v4`, qui appelle `validation_imbriquee_v4` ; gardes de registre `registre_bbis_v2` ; branche de sortie `donnees/t07-etape-b-bis-v2` ; les v1 à v5 restent, R12 ; les v6 sont rattachées par le troisième addendum, non par la fiche de `CODE-BBIS`)
```

**Raison** (SA-6 à SA-8). Le contrôle de SA-1 et la mesure de SA-10 sont portés par des modules à noms neufs (R12) ; la v3 reste.
`registre_bbis_v2` est **neuf** (il ne figurait pas dans la demande) : sans lui, la seconde ligne `CODE-BBIS` ne peut être écrite
et la garde de création refuse la course (`exiger_creation` de la v1 : « une seconde relance est exclue » dès `RELANCES` = 2).
La branche de sortie change parce que `donnees/t07-etape-b-bis-v1` porte déjà les traces de la course arrêtée (l'amorce refuse
une branche présente : R12) ; voir SA-16.

### SA-9 — Code neuf, épreuves (document : T+1 ; remplace le « nouveau » de EC-8)

Ancien :

```text
égalité carte-processeur (linéaire à 300 époques, attention à 3 époques ; artefacts : autre graine, poids altérés de 1 % ; déterminisme : cas sain et artefact ; sonde de contrôle en échec à 3 ou à 300 époques : arrêt ; couple tiré parmi les sondes finales finies : même couple et mêmes actions que la v1 si toutes sont finies, autre tirage si une ne l'est pas, aucun : arrêt ; R-PILE et champ du contrôle à la lecture : cas sain et artefacts) ; garde de débit
```

Nouveau, qui fait foi :

```text
égalité carte-processeur (les deux familles à 3 époques ; artefacts : autre graine, poids altérés de 1 %, régularisation fausse, une étiquette inversée, lot d'autres données ; déterminisme de chaque famille : cas sain et artefact ; sonde de contrôle en échec à 3 ou à 300 époques : arrêt ; reproduction de l'arrêt du contrôle v3 sans erreur de chaîne, et cas sains qui passent malgré 300 époques divergentes, avec jetons presque identiques et en régime anisotrope sans quasi-copie ; couple tiré parmi les sondes finales finies : même couple et mêmes actions que la v1 si toutes sont finies, autre tirage si une ne l'est pas, aucun : arrêt ; R-PILE, champ du contrôle et discriminant à la lecture : cas sain et artefacts ; mesure de dispersion : ordre inverse joué, aucune aire écrite, échec d'une sonde, erreur d'exécution, garde, clés désalignées, compte des apprentissages ; ligne `CODE-BBIS` remplacée : lecture, ordre, écriture, garde de création) ; garde de débit
```

**Raison.** Chaque arrêt neuf a son cas sain et son artefact (R5) ; le cas sain du régime anisotrope est demandé par la réserve R-E.
Épreuves : `code/tests/test_t07bbis_second_addendum_v1.py` (34 essais, 34 passés, § 9).

### SA-10 — Métrique, mesure de dispersion entre deux ordres de calcul (document : T ; insertion avant le point « Non calculable »)

Ancien :

```text
- **Non calculable** : classe absente d'un pli ;
```

Nouveau, qui fait foi :

```text
- **Dispersion des aires entre deux ordres de calcul** (mesure d'information du second addendum ; GO-2026-11-16-12 ; réserve R-D) : « ordre 1 » = la sonde lue (plan, point 5). « Ordre 2 » = pour chaque source plafond (P-instruit, P-S25, P-S50, P-S75, P-S100) et chaque pli externe dont la sonde finale est apprise, la **recette entière de la sonde** (grille de 18 réglages × quatre plis internes, critère et ex aequo du point 5, sonde finale réapprise sur les 32 tâches) rejouée sur la même carte, **chaque lot d'apprentissage prenant ses actions dans l'ordre inverse** (étiquettes de même) ; mêmes plis, mêmes clés de graines (même départ), mêmes réglages, mêmes 300 époques et pas 0,05 : même problème, seul l'ordre des sommes change ; ni ENC, ni le plancher, ni le nul de réétiquetage ne sont rejoués. **Sur l'instance** : la sonde de l'ordre 2 est notée sur les mêmes actions que la sonde lue (tous les groupes que la sonde lue note) ; ses scores et ses poids sont écrits dans les fichiers fermés, son réglage retenu et son empreinte dans le fichier des sondes ; aucune aire n'est écrite (ses aires de validation interne servent au seul choix de son réglage, jamais écrites). **À la lecture**, sur processeur, pour chacune des dix cellules (plafond et transfert) : A₁ = aire du jeu décisif (positifs O de la cellule contre O[H], tâches du pli lu, moyenne des deux plis, comme « Aire d'une cellule ») par la sonde lue de la source, A₂ = la même par la sonde de l'ordre 2 de la même source ; **rapportés** : A₁, A₂, Δ = A₂ − A₁, les aires par pli, les réglages retenus des deux ordres par pli ; résumé : max |Δ| et sa cellule, nombre de plis comparés et nombre de plis dont le réglage retenu change. **Aucun intervalle, aucun niveau, aucun seuil, aucun état, aucune issue** : la mesure ne change aucune ligne de BB-P1 à BB-P12, aucune cellule, aucune phrase gelée hors de R-PILE ; elle est écrite dans le champ « dispersion entre ordres de calcul » de la lecture et résumée dans R-PILE. **Échecs** : sonde de l'ordre 2 en échec (perte ou paramètres non finis) → la source est « échec » pour la mesure, motif écrit, sans arrêt ; erreur d'exécution qui n'est pas une garde (mémoire de la carte, erreur de torch) → la mesure entière est « non faite », motif écrit, tableaux partiels retirés, la marche continue et écrit ses scores ; une garde (tâche du pli lu, signal d'arrêt, clés désalignées) arrête la marche comme ailleurs. **Ce qu'elle ne mesure pas** : l'écart à une autre pile (autre carte, autre pilote, processeur) ; une seule réalisation d'un second ordre, non une loi de la dispersion ; la dispersion d'ENC, du plancher ou du nul.
- **Non calculable** : classe absente d'un pli ;
```

**Raison.** Option (ii) de la réserve R-D, retenue par Lazar (GO-2026-11-16-12) : chiffrer, sur les vraies activations, la
dispersion que R-PILE ne fait que nommer, et le risque que l'ex aequo à 0,005 change le réglage retenu (contre-lecture, § 4).
« Deux ordres de calcul » est réalisé sur la même carte par l'ordre inverse des actions : c'est l'émulation qu'ont employée le
diagnostic (« permutée », écart 5,18 sur le jeu 2) et la contre-lecture (permutation des actions) ; elle ne demande aucune clé de
graine neuve (plan, point 12, inchangé) et aucune seconde carte. Code : `validation_imbriquee_v4.mesurer_dispersion`,
`apprendre_recette_ordre2` ; `lecture_v3.dispersion_ordres`.

### SA-11 — Plan, point 2, ordre des lignes (document : T)

Ancien :

```text
Puis `CODE-BBIS`, `GO-BBIS`, création, `SCORES-BBIS`, lecture,
```

Nouveau, qui fait foi :

```text
Puis `CODE-BBIS`, `GO-BBIS`, (second addendum : `CODE-BBIS` remplacée une seule fois, strictement après `GO-BBIS`), création, `SCORES-BBIS`, lecture,
```

### SA-12 — Plan, point 8, notation sur l'instance (document : T)

Ancien :

```text
scores d'action seulement (sonde, 800 directions, 100 sondes du nul de réétiquetage, ENC), écrits dans des fichiers **fermés**
```

Nouveau, qui fait foi :

```text
scores d'action seulement (sonde, 800 directions, 100 sondes du nul de réétiquetage, ENC, sonde de l'ordre 2 de la mesure de dispersion), écrits dans des fichiers **fermés**
```

### SA-13 — Plan, point 8, aires calculées sur l'instance (document : T)

Ancien :

```text
les seules aires calculées sur l'instance sont les aires de validation interne, sur les tâches d'apprentissage, pour le choix du réglage, jamais écrites ;
```

Nouveau, qui fait foi :

```text
les seules aires calculées sur l'instance sont les aires de validation interne, sur les tâches d'apprentissage, pour le choix du réglage (celui de la sonde et celui de la sonde de l'ordre 2), jamais écrites ;
```

### SA-14 — Plan, point 10 (d), ordre de la lecture (document : T)

Ancien :

```text
puis réserves RF, IT et descriptifs (DOM, DOM-H, SC, A_T, TE_instruit, capacité de mémorisation, taux à 1 %) ;
```

Nouveau, qui fait foi :

```text
puis réserves RF, IT et descriptifs (DOM, DOM-H, SC, A_T, TE_instruit, capacité de mémorisation, taux à 1 %) ; après toutes les cellules, la dispersion entre deux ordres de calcul (« Métrique », information) ;
```

### SA-15 — Liste d'arrêt, dépense, relance (document : T)

Ancien :

```text
; une seconde relance est exclue.
```

Nouveau, qui fait foi :

```text
; une seconde relance est exclue, hors la course unique accordée par GO-2026-11-16-11 sous le second addendum (compteur de relances à 2, feu écrit de la mère portant aussi ce numéro, ligne `CODE-BBIS` remplacée) ; toute autre course : exclue.
```

**Raison.** La relance unique est consommée (§ 1) ; seule GO-2026-11-16-11 permet la nouvelle course. Code :
`registre_bbis_v2.exiger_creation` (`RELANCES` ≤ 2 ; à 2, le feu doit porter GO-2026-11-16-11 et le registre deux lignes
`CODE-BBIS` ; la limite du samedi 21 novembre 12:00 UTC vaut pour toute relance).

### SA-16 — Données gardées, branche (document : T)

Ancien :

```text
(branche `donnees/t07-etape-b-bis-v1`, morceaux de moins de 95 Mo)
```

Nouveau, qui fait foi :

```text
(branche `donnees/t07-etape-b-bis-v2` pour la course du second addendum, `donnees/t07-etape-b-bis-v1` gardant, sans changement, les traces de la course arrêtée le 16 novembre ; morceaux de moins de 95 Mo)
```

### SA-17 — Données gardées, contenu des fichiers de scores (document : T)

Ancien :

```text
scores des actions d'apprentissage de la sonde finale et des sondes du nul)
```

Nouveau, qui fait foi :

```text
scores des actions d'apprentissage de la sonde finale et des sondes du nul ; scores et poids de la sonde de l'ordre 2, mesure de dispersion)
```

### SA-18 — Données gardées, fichier des sondes (document : T)

Ancien :

```text
(réglages retenus, empreintes des sondes et des deux premières directions, graines ; **aucune aire**)
```

Nouveau, qui fait foi :

```text
(réglages retenus, empreintes des sondes et des deux premières directions, graines, contrôle carte-processeur, réglage retenu et empreinte de la sonde de l'ordre 2 et résumé de la mesure de dispersion ; **aucune aire**)
```

### SA-19 — Liste d'arrêt, aire écrite sur l'instance (document : T)

Ancien :

```text
(hors du réglage retenu, écrit dans le fichier fermé des sondes)
```

Nouveau, qui fait foi :

```text
(hors des réglages retenus, celui de la sonde et celui de la sonde de l'ordre 2, écrits dans le fichier fermé des sondes)
```

### SA-20 — Calcul et dépense (document : T)

Ancien :

```text
; la ligne `GO-BBIS` du registre propre en recopie l'extrait.
```

Nouveau, qui fait foi :

```text
; la ligne `GO-BBIS` du registre propre en recopie l'extrait. Second addendum : la course qu'accorde GO-2026-11-16-11 (une seule) et la mesure de dispersion (GO-2026-11-16-12) partent sous cette même ligne (40 USD, coupure 39,5 USD, échéance 2026-11-22), avec le feu écrit de la mère portant GO-2026-11-14-09 et GO-2026-11-16-11 ; coût chiffré au § 6 du second addendum.
```

### SA-21 — Premier addendum, § 3, coût du contrôle (document : A1)

Ancien :

```text
il ajoute sur la carte au plus une linéaire de 300 époques, une attention de 3 époques et deux
de 300 (`validation_imbriquee_v3`, `71bffa5b…`, docstring, ligne 30)
```

Nouveau, qui fait foi :

```text
il ajoute (second addendum) sur la carte, par famille de la marche, une sonde de 3 époques et au plus deux de 300 (la sonde finale du couple sert de première quand sa famille est retenue), et sur le processeur, par famille, une sonde de 3 époques, plus une linéaire de 300 époques pour l'information (`validation_imbriquee_v4`, docstring) ; la mesure de dispersion ajoute 730 apprentissages sur la carte (§ 6 du second addendum)
```

### SA-22 — Premier addendum, § 5, point 1 (document : A1)

Ancien :

```text
seuls l'identité du code de la boucle, la linéaire à 300 époques et le déterminisme la
   couvrent, sans comparaison directe ;
```

Nouveau, qui fait foi :

```text
seuls l'identité du code de la boucle et le déterminisme la
   couvrent, sans comparaison directe ; **affaiblissement déclaré (second addendum)** : la linéaire à 300 époques, qui la couvrait, n'est plus un contrôle ; son écart carte-processeur n'est plus qu'une information, qui la signale sans la distinguer d'une amplification d'arrondi (§ 4 du second addendum) ;
```

### SA-23 — Premier addendum, § 5, point 4 (document : A1)

Ancien :

```text
Si le réglage retenu du couple tiré est linéaire, sa sonde lue est comparée
   comme au texte scellé et les sondes « attention » du contrôle ne sont pas des sondes lues ;
```

Nouveau, qui fait foi :

```text
**Second addendum** : la sonde **linéaire** lue (300 époques) n'est plus comparée non plus à une référence d'une autre pile ; seul son déterminisme sur la carte est vérifié, et son écart à 300 époques est écrit comme information : **affaiblissement déclaré**, de même forme que pour l'attention ; les sondes de 300 époques apprises pour le seul contrôle (famille non retenue du couple) ne sont pas des sondes lues ;
```

### SA-24 — Premier addendum, § 5, point 5 (document : A1)

Ancien :

```text
écart de la linéaire à 300 époques
   1,954·10⁻⁸, de l'attention à 3 époques 1,486·10⁻⁸ (256 actions, tolérance 10⁻⁴)
```

Nouveau, qui fait foi :

```text
écart de la linéaire à 300 époques
   1,954·10⁻⁸, de l'attention à 3 époques 1,486·10⁻⁸ (256 actions, tolérance 10⁻⁴) — **requalifié (second addendum)** : 1,954·10⁻⁸ ne prouve le bon fonctionnement de la pile de la carte que sur un bruit gaussien isotrope indépendant en simple précision, où la sonde ajuste bien ; il ne dit rien des régimes qui ajustent mal, où la course du 16 novembre a donné 1,004 ; la linéaire à 3 époques n'a pas été mesurée sur carte
```

### SA-25 — Premier addendum, § 5, paragraphe « R-PILE (EC-2, EC-3) » (document : A1)

Ancien :

```text
**R-PILE** (EC-2, EC-3) : une aire de la famille « attention » est celle d'**une** sonde parmi celles que rendrait le même
apprentissage sous d'autres arrondis ; sur données synthétiques, dispersion négligeable quand la sonde apprend un signal, de
l'ordre de 0,007 quand elle n'apprend rien ; **sur de vraies activations, elle n'est pas mesurée**. La réserve ne change aucune
issue ; elle borne ce que le verdict peut dire d'une aire « attention » proche du hasard.
```

Nouveau, qui fait foi :

```text
**R-PILE** (EC-2, EC-3 ; second addendum, SA-2, SA-3 et SA-10) : une aire de sonde, linéaire ou « attention », est celle d'**une**
sonde parmi celles que rendrait le même apprentissage sous d'autres arrondis ; sur données fabriquées, dispersion négligeable
quand la sonde apprend un signal, de l'ordre de 0,007 quand une sonde « attention » n'apprend rien, de 0,007 à 0,047 quand une
sonde linéaire ajuste mal ; **sur de vraies activations, elle est mesurée entre deux ordres de calcul de la carte, comme
information seulement, et non entre la carte et une autre pile**. La réserve ne change aucune issue ; elle borne ce que le
verdict peut dire d'une aire de sonde proche du hasard.
```

**Raison** (SA-21 à SA-25 ; réserve R-C de la contre-lecture). Ces paragraphes de A1 décrivent le contrôle de EC-1 ou l'état de la mesure ; laissés tels
quels, ils diraient faux sous le contrôle v4. **§ 6 de A1, lu avec le second addendum** (sans remplacement de fragment, déclaré) :
« le code v3 reste tel quel » vaut jusqu'à la ligne `CODE-BBIS` remplacée ; la course du second addendum cite le code v4 par la
fiche de cette ligne ; le code v4, comme le v3, cite l'empreinte du texte scellé et lui seul (`commun_v1.TEXTE_SHA256`, inchangé) ;
le verdict cite, en plus de (a) à (d) : le second addendum, son empreinte et sa ligne `ADDENDUM-ECART-2-BBIS`, et lit les critères
de T modifiés par EC-1 à EC-4 **puis** par SA-1 à SA-20 ; un verdict qui ne le cite pas n'est pas scellé (même règle que A1).

## 3. Affaiblissements déclarés

1. **Perte de la couverture « linéaire à 300 époques »** (A1, § 5, point 1 ; SA-22) : une erreur de chaîne qui ne commence
   qu'après la troisième époque (pas, réglage d'Adam ou mise à jour fausse au-delà de l'époque 3) n'est plus arrêtée par aucun
   contrôle comparatif : seuls l'identité du code de la boucle (même fonction aux deux horizons) et le déterminisme la couvrent,
   et le déterminisme ne prouve pas la justesse (une erreur déterministe propre à la carte passe). L'information à 300 époques
   la signale sans la séparer de l'amplification (§ 4).
2. **Perte de la comparaison de la sonde lue à une référence** (A1, § 5, point 4 ; SA-23) : la sonde linéaire lue de 300
   époques, comme déjà l'« attention », n'est plus comparée à une sonde apprise sur une autre pile ; seul son déterminisme l'est.
   Le couple contrôlé reste un seul couple tiré, comme au texte scellé ; les autres couples et ENC ne reçoivent aucun contrôle.
3. **Ce que la mesure de dispersion ne couvre pas** (SA-10) : la carte contre une autre pile ; ENC, plancher et nul ; une loi de
   la dispersion (une réalisation seulement).
4. Rien n'a été mesuré **sur carte** pour la linéaire à 3 époques, le déterminisme de la linéaire dans le contrôle v4 et la
   mesure (SA-1, fin) ; la quatrième passe n'a mesuré que la linéaire à 300 époques et l'attention à 3 époques (SA-24).

## 4. Discriminant à double sens (réserve R-B)

Écrit avant la course, il ne change aucun état ; il est rapporté par `lecture_v3.exiger_controle_carte` (`discriminant`).
- **Arrêt à 3 époques** (écart > 10⁻⁴), ou déterminisme faux à 300 époques : **erreur de chaîne au sens large** (entrée,
  structure, réglage, ou comportement de la pile non vu) ; l'amplification d'arrondi ne l'explique pas (à 3 époques, au plus de
  l'ordre de 10⁻¹⁰ pour la linéaire et de 6·10⁻⁷ pour l'attention sur les jeux fabriqués ; artefacts d'entrée : 10⁻² à 1).
- **Passage à 3 époques avec information à 300 époques au-dessus de 10⁻⁴** (ou non finie) : **amplification d'arrondi ou
  erreur de chaîne qui ne commence qu'après la troisième époque, indiscernables** par ce contrôle ; ce cas **ne réfute pas**
  une erreur tardive (contre-lecture, § 3).
- **Passage à 3 époques avec information au plus 10⁻⁴** : carte et processeur s'accordent aussi à 300 époques sur ce couple ;
  aucune amplification vue sur ce couple ; rien n'est dit des autres couples.

## 5. Ce qui ne change pas

**Inchangés, et dits tels** : hypothèse (HB-1 à HB-5, rivales) ; prédiction chiffrée et signe (BB-P1 à BB-P12) ; métrique (score
d'action par le maximum ou l'attention, jamais la moyenne ni la médiane ; aire ; intervalle ; plancher de 800 directions ; règle
(a) en deux plis ; nul de réétiquetage de 100 réétiquetages ; lecteurs du texte ; texte égal ; artefact ; DOM ; SC ; taux à 1 %),
hors l'ajout de SA-10 ; seuils ; niveaux (99 % décisif, 95 % réserves ; épreuve de niveau et niveau retenu 0,99 de la fiche
`code-bbis-v2.json`, `4b28535c…`, épreuve rejouée `da9fa42b…` (`registres/t07-etape-b-bis/epreuve-niveau-deux-plis-bbis-v2.json`) ; l'épreuve `641adeb5…` de la première fiche n'est plus dans le dépôt) ; **tolérance 10⁻⁴** ; **256 actions** de contrôle ; **tirage du
couple** (graine `bbis/egalite-carte`, ordre trié, parmi les sondes finales finies) ; **graines** (entropie **changée** : l'entropie est celle que porte la ligne `CODE-BBIS` en vigueur (lecture déclarée du point 12 de T, « tirée à l'inscription de `CODE-BBIS` »), soit `149084685129585384182032033013812122656` dans la fiche remplaçante `code-bbis-v2.json`, au lieu de `208082752394230630219821407440340422345` dans la fiche `code-bbis-v1.json` (écart couvert par GO-2026-11-18-03 (1) ; la prédiction écrite avant la course, « mêmes sondes, même couple de contrôle et mêmes actions que la course arrêtée, donc écart de la linéaire à 300 époques probablement de l'ordre de 1, discriminant « écart » », a perdu son appui : réserve nommée au verdict, GO-2026-11-18-03 (1) ; sans effet sur aucun état) : aucun score n'a été écrit ni lu ; aucune clé neuve ; la
mesure reprend les clés de la sonde) ; **plis** externes et internes ; **grille** de 18 réglages, critère et ex aequo à 0,005 ;
**300 époques et pas 0,05 des sondes lues** ; plancher ; nul ; notation ; **garde de débit** (11 h, facteur 1,2, 0,6 h, 20
premiers apprentissages entrelacés ; lecture déclarée : les 730 apprentissages de la mesure sont des « apprentissages restants ») ;
**budget** (40 USD, coupure 39,5 USD, ligne GO-2026-11-14-09) ; **échéance** (verdict scellé au plus tard le dimanche 22 novembre ;
limite de relance du samedi 21 novembre 12:00 UTC) ; états E0 à E6 et E6′, issues I0 à I6, suffixes T0 à T+, libellés du nœud
5, table conjointe C0 à C6 ; liste « Jamais » ; lignes de registre (huit clés, aucune neuve au registre propre).

## 6. Coût chiffré ; tient-il sous GO-2026-11-14-09 ?

Sources : course arrêtée du 16 novembre (R-3025 : marche de 17:58:00Z à 21:35:28Z, soit 3,62 h, pour 2 460 apprentissages ;
médiane des 20 premiers 2,23 s ; dépense ≈ 5,14 USD ; cumul ≈ 6,0 USD sur 40) ; prix relevé 1,2161 USD de l'heure (R-3011) ;
devis `devis-etape-b-bis-v3.md` (P1 : hôte deux fois plus lent, 1,40 USD de l'heure, 11,3 h, ≈ 18,8 USD).
- **Mesure de dispersion** : 5 sources × 2 plis × (18 × 4 + 1) = **730 apprentissages** (+ 30 % sur 2 460), plus leur notation
  (petite). Bas : 730 × 2,23 s ≈ **0,45 h** ; haut : 730 × 5,3 s (3,62 h ÷ 2 460, toute la marche comptée) ≈ **1,07 h** ; soit
  **≈ 0,55 à 1,30 USD** de carte, plus le disque (≤ 0,08 USD de l'heure : ≤ 0,09 USD). Pire cas (hôte deux fois plus lent, 1,40
  USD de l'heure) : 2,14 h ≈ **3,0 USD**.
- **Contrôle v4** : quelques secondes de plus sur la carte (une linéaire de 3 époques, une de 300) et une linéaire de 3 époques
  sur le processeur : négligeable.
- **Essais neufs sur l'instance** (34 essais ; au bloc-notes, sur 4 fils, 4 min 31 s avec les 17 de la v3 du contrôle, 7 min 50 s quand d'autres calculs tournaient) : ≈ 0,1 à 0,2 USD.
- **Course entière attendue** : 5,1 (course du 16 novembre) + 0,55 à 1,30 + 0,1 à 0,2 ≈ **5,8 à 6,6 USD** ; cumul après la course
  ≈ **11,8 à 12,6 USD sur 40**.
- **Pire cas** : la garde de débit arrête toute marche projetée au-delà de 11 h, mesure comprise (P1 : ≈ 18,8 USD), plus une
  instance gardée 12 h après un arrêt de débit (≤ 0,96 USD) : ≈ 19,8 USD ; cumul pire ≈ **25,8 USD ≤ 40** ; la coupure à 39,5 USD
  reste la garde de dépense.
- **Verdict** : **course plus mesure tiennent sous GO-2026-11-14-09** (cumul plus pire cas ≈ 25,8 ≤ 40 USD) ; **aucun nouveau
  mot de Lazar n'est requis pour la dépense** (GO-2026-11-16-12 : « sous la ligne GO-2026-11-14-09 s'il y tient avec la course »).
- **Hors devis** : une répétition à blanc sur carte n'est pas exigée (SA-1) ; si la mère ou Lazar la veulent quand même : ≈ 0,25 à
  0,5 USD (quatrième passe : 12 min, 0,247 USD), un script de répétition v4 à écrire, et un mot de Lazar sur sa ligne.

## 7. Rattachement du code

Code v4, dossier `brouillons/T0.7-etape-B-bis-v1/second-addendum-v2/code/` (miroir des chemins du dépôt, à verser sous `src/`,
`scripts/` et `tests/` par la mère, noms neufs, R12 ; aucun fichier existant modifié) : `validation_imbriquee_v4.py`,
`marche_v4.py`, `lecture_v3.py`, `registre_bbis_v2.py`, `scripts/lancer_bbis_v4.sh`, `scripts/amorce_bbis_v4.sh`, essais
`tests/test_t07bbis_second_addendum_v1.py` et aides `tests/aide_t07bbis_differentiels_v4.py`, `tests/aide_t07bbis_jeux_v4.py` ;
empreintes dans leurs compagnons ; différentiels : `diff-v3-v4.txt`. Le code v4 cite l'empreinte du texte scellé et lui seul ;
aucun addendum ne monte sur l'instance (l'amorce n'extrait que `/prereg/T0.7-etape-B-bis-v1.md*`) ; le lanceur et l'amorce v6 ne sont pas cités par la fiche de `CODE-BBIS` : ils sont rattachés par leurs empreintes, écrites au troisième addendum, et l'amorce écrit la sienne au journal de l'instance. La fiche remplaçante de
`CODE-BBIS` (nom proposé `registres/t07-etape-b-bis/code-bbis-v2.json`) liste au commit versé (`05cd22aa…`) 63 fichiers, dont le code v4 et, en plus, l'amorce et le lanceur v5 (écart déclaré à TA-1 ; les v6 sont rattachés par le troisième addendum, non par la fiche), avec l'entropie de la fiche remplaçante (`149084685129585384182032033013812122656`, changée, TA-3) et une épreuve de niveau rejouée sous cette entropie (`da9fa42bf95c9d6507b01d7bf69db2876a56c00d26b0cc58c15cd7893bfa5919`), au même niveau décisif retenu (0,99).

## 8. Antériorité : aucun score de la course lu avant l'écart

La course du 16 novembre n'a écrit aucun score (`scores_ecrits` faux ; R-3025). Ce brouillon n'a lu, sur la branche
`donnees/t07-etape-b-bis-v1`, que ce que le diagnostic et sa contre-lecture citent de `arret-marche-bbis.json`,
`manifeste.json` et `traces/bbis-t07-v1/*` (cause de l'arrêt, durées, versions), par leurs rapports ; il n'a ouvert ni
`relecture-bbis.json` ni aucun fichier de 7a, 7b, de l'étape B de T0.7, de T0.6, de P3-bis ni du bras d'attaque. Rien ne peut
avoir été choisi d'après un score.

## 9. Contrôle mécanique et pièces

`pieces/controle-fragments-second-addendum-v1.py` (programme de ce brouillon) : lit T, A1 et ce brouillon ; construit T+1 (EC-1 à
EC-8 de A1) ; pour chaque SA, vérifie que l'« ancien » figure une seule fois dans son document, applique les vingt-cinq
remplacements, écrit le texte en vigueur (`pieces/texte-en-vigueur-apres-second-addendum-v1.md`) et vérifie que la phrase de
R-PILE et le point (7) y sont égaux aux chaînes de `lecture_v3`. Sortie : `pieces/sortie-controle-fragments-second-addendum-v1.txt`.

## 10. Fichiers à donner au contre-lecteur (R2)

Lecture seule : ce brouillon ; `rapport-second-addendum-bbis-v1.md` ; le dossier `code/` et `diff-v3-v4.txt` ; `pieces/` ;
`essais/` ; `prereg/T0.7-etape-B-bis-v1.md` (`0ae6210f…`) ; `prereg/T0.7-etape-B-bis-v1-addendum-ecart-v1.md` (`f00eda8a…`) ;
`brouillons/T0.7-etape-B-bis-v1/diagnostic-carte-processeur-v1/` (rapport `1fefa0a9…`, contre-lecture `0da982fb…`,
`validation_imbriquee_v4.py` `ba127aa0…`, sorties) ; `src/controle_ia/t07bbis/` v1 à v3 (`validation_imbriquee_v3.py`,
`marche_v3.py`, `lecture_v2.py`, `registre_bbis_v1.py`, `apprentissage_carte_v1.py`, `commun_v1.py`) et `scripts/*_bbis_v3.sh` ;
`registres/go.md`, lignes GO-2026-11-14-09, GO-2026-11-16-11, GO-2026-11-16-12 ; `registres/decisions.md`, lignes R-2957,
R-3003, R-3011, R-3025, R-3030, R-3031 (une à une, `grep -n '^| R-NNNN '`) ; `registres/t07-etape-b-bis-v1.md`.
Questions : chaque « ancien » est-il exact et unique ; reste-t-il un fragment scellé touché sans être nommé ; la mesure est-elle
définie sans aucune issue ; le coût et le verdict de dépense sont-ils justes ; le code fait-il ce que le texte dit, et rien
d'autre. Interdits : rien sous `diag/`, `runs/`, `donnees/` ; jamais `relecture-bbis.json` ; aucune donnée de 7a ou 7b ; aucune
valeur de clé ; ni `env`, ni `printenv`.

## 11. Contre-lecture

### Tour 1 — rapport lu au brouillon 1, corrections dans le brouillon 2

Texte du brouillon 2, gardé tel quel : « ce brouillon », « ce brouillon 2 » et « de ma main » y désignent le brouillon 2 et son rédacteur.

- **Rapport** : `contre-lecture-second-addendum-bbis-tour1-v1.md` (ce dossier), tour 1, lu au brouillon 1 (`a582e14dd22fd17e716aaed8d475a3c1a7ceeff60d15c3a4644aa9bf0c6f4627`) ; empreinte du rapport
  `98a049d9f8b207eb336d04fc7e5a0b23bb5c066cd542bbc7719bd1e1b58fc120` (compagnon vérifié). Verdict du rapport :
  **corrections**, un majeur et cinq mineurs, aucun ne touchant l'hypothèse, les seuils, le budget ni une issue ; scellable une fois les couples
  de son § 6 appliqués et le contrôle mécanique rejoué, le code v4 étant contre-lu à part.
- **Réponse point par point** (chaque « ancien » vérifié unique dans le brouillon 1 et dans le texte courant ; chaque « ancien » et chaque
  « nouveau » vérifié égal, au caractère, au texte du rapport, par `pieces/couples-brouillon2-second-addendum-v1.py`) :
  - **M1** (blocs et paragraphes de A1 contredits sans règle de préséance) : **appliqué**. K1 : phrase de préséance au § 0 ; K2 :
    fragment SA-25 (paragraphe « R-PILE (EC-2, EC-3) » du § 5 de A1), ligne « Raison » de SA-21 à SA-25 ; comptes : « SA-1 à
    SA-25 » (§ 0) et « vingt-cinq » (§ 9) ; « 25 écarts SA lus » dans la sortie neuve du contrôle (ci-dessous).
  - **m1** (« avant toute création ») : **appliqué**, K3 (SA-5).
  - **m2** (ordre de 10⁻¹⁰ vrai de la linéaire, faux de l'attention) : **appliqué**, K4a (SA-1, « Nouveau ») et K4b (§ 4, premier cas).
  - **m3** (date et heures du brouillon 1) : **appliqué**, K5.
  - **m4** (entropie reprise, lecture du point 12 de T, prédiction écrite avant la course) : **appliqué**, K6 (§ 5).
  - **m5** (énumération des formes du résumé de la mesure) : **appliqué**, K7 (SA-2) ; la phrase gelée de R-PILE n'est pas touchée.
  - **Remarques facultatives R1 à R4** : aucune correction exigée par le rapport ; **non appliquées** (ce brouillon n'applique que les
    corrections exigées ; R1 demanderait en plus de changer `lecture_v3.SECTION_D`, donc de rouvrir la contre-lecture du code).
  - **Points pour la session mère** (§ 5 du rapport, points 1 à 6 : réponses aux trois questions du rédacteur, répétition à blanc
    recommandée sans être exigée, garde de débit pendant la mesure, ordre des gestes avant le feu, contre-lecture du code v4 encore due,
    incident du lecteur) : hors du texte de l'addendum, **non appliqués ici**, laissés à la mère.
- **Contrôle mécanique rejoué** sur ce brouillon 2 : `pieces/controle-fragments-second-addendum-v2.py` (copie de la v1, produite par le
  même programme de couples : seuls changent le nom du brouillon lu, les noms des deux pièces écrites et le compte « SA-21 à SA-25 »
  d'un commentaire) ; sortie `pieces/sortie-controle-fragments-second-addendum-v2.txt` : 25 écarts SA lus, chaque « ancien » unique dans
  son document, R-PILE et point (7) égaux aux chaînes de `lecture_v3`, **CONFORME**, code 0 ; texte en vigueur
  `pieces/texte-en-vigueur-apres-second-addendum-v2.md` ; premier addendum lu avec le second `pieces/premier-addendum-lu-avec-le-second-v2.md`.
  Les pièces v1 nommées au § 0 et au § 9 sont celles du brouillon 1, gardées telles quelles (R12) ; pour ce brouillon 2, les pièces v2 en tiennent lieu.
- **Essais rejoués** : le code du dossier `code/` n'est touché par aucun couple ; `essais/sortie-essais-second-addendum-v2.txt` (copie du bloc-notes : `git archive` de `af0adb14` réduit, plus `code/` ; mêmes deux fichiers d'essais que le brouillon 1) : première passe, 49 passés et 2 échecs, tous deux dus à la copie (dossiers `docs/sources/invites-*` retirés par erreur de ma main, garde « fichier absent sur disque ») ; ces deux essais, rejoués après ajout des dossiers : 2 passés ; au total, les 51 essais (34 neufs, 17 de la v3) passent, avec les mêmes valeurs des cas sains que la sortie du brouillon 1 (quasi-copies : 9,175·10⁻¹², 9,483·10⁻¹⁰, information 5,307 ; anisotrope : 3,088·10⁻¹², information 3,793). La suite entière sur un arbre de la forme de l'instance n'est pas rejouée (code inchangé).

### Tour 2 — rapport lu au brouillon 2, correction dans ce brouillon 3

- **Rapport** : `contre-lecture-second-addendum-bbis-tour2-v1.md` (ce dossier), tour 2, lu au brouillon 2
  (`ab66d5fa67a640679465581d48d9fc97a1da7d81c7b41b18e81865274c91f62c`) ; empreinte du rapport
  `f4843729df2528b864b77e370c6c8725e94adccbedb99ff096e14028783a9f4e` (compagnon vérifié). Verdict du rapport : **corrections**, une
  seule exigée (m1, mineure), aucun majeur ; scellable une fois m1 appliqué, aucun autre changement requis ; le code v4 reste à
  contre-lire à part.
- **Réponse point par point** (l'« ancien » de m1 vérifié unique dans le brouillon 2 et dans le texte courant, son « ancien » et son
  « nouveau » vérifiés présents, au caractère, dans le rapport, par `pieces/couples-brouillon3-second-addendum-v1.py`) :
  - **§ 2 et § 3 du rapport** (couples K1 à K7 du tour 1 appliqués au caractère ; contrôle mécanique, essais et épreuves rejoués par
    le lecteur, conformes ; code v4 inchangé) : constats, rien à appliquer.
  - **m1** (lettre de modèle du rédacteur du brouillon 2) : **appliqué**, au caractère, dans la ligne « Brouillon 2 » de l'en-tête
    (« lettre de modèle C » devient « lettre de modèle A »). Le rapport laissait le point à trancher par la mère, qui lance les
    rédacteurs ; la commande de ce tour, venue d'elle, dit les corrections écrites par le modèle A ; le rédacteur du brouillon 3 n'a
    pas d'autre source sur ce point et tient de la même commande la lettre de sa propre ligne.
  - **R1** (pièces v1 encore nommées au § 0 et au § 9) : remarque facultative, **non appliquée** : ce brouillon n'applique que la
    correction exigée et ne change que l'en-tête et cette section (pour ce brouillon 3, ce seraient d'ailleurs les pièces v3, non les
    v2) ; la lecture reste celle du tour 1 : les pièces v1 nommées au § 0 et au § 9 sont celles du brouillon 1, gardées telles quelles
    (R12) ; pour ce brouillon 3, les pièces v3 en tiennent lieu (ci-dessous).
  - **R2** (remarques R1 à R4 du tour 1 laissées non appliquées) : remarque facultative, rien à appliquer ; elles restent non
    appliquées.
  - **Points pour la session mère** (§ 5 du rapport, points 1 à 6 : m1 à trancher, scellement et ligne `ADDENDUM-ECART-2-BBIS` avant
    la seconde ligne `CODE-BBIS`, entropie reprise, gestes encore dus avant le feu, répétition à blanc, garde de débit pendant la
    mesure, incidents du lecteur) : hors du texte de l'addendum, **non appliqués ici**, laissés à la mère.
- **Contrôle mécanique rejoué après le couple** : `pieces/controle-fragments-second-addendum-v3.py` (copie de la v2, produite par le
  même programme de couples : seuls changent le nom du brouillon lu et les noms des deux pièces écrites, dans le code et dans leurs
  lignes de commentaire) ; sortie `pieces/sortie-controle-fragments-second-addendum-v3.txt` ; texte en vigueur
  `pieces/texte-en-vigueur-apres-second-addendum-v3.md` ; premier addendum lu avec le second
  `pieces/premier-addendum-lu-avec-le-second-v3.md`. Aucune ligne entre le titre du § 0 et celui de cette section ne change (aucun
  fragment SA, aucun chiffre, aucun seuil) : vérifié par le programme de couples, ces lignes sont égales, octet pour octet, à celles
  du brouillon 2.
- **Essais rejoués après le couple** : le code du dossier `code/` n'est touché par aucun couple ; mêmes deux fichiers d'essais que les
  brouillons 1 et 2 (34 essais neufs, 17 du contrôle v3) ; sortie `essais/sortie-essais-second-addendum-v3.txt`.
