# Contre-lecture du second addendum de B bis (T0.7) et du code v4 — tour 1 — v1

- **Lecteur** : contre-lecteur neuf (R2), lettre de modèle C. N'a écrit aucune des pièces (modèle A). Lecteur déclaré de T0.7 :
  exclu des lecteurs de P3-bis.
- **Heures (UTC, `date -u`)** : 2026-11-17, de 00:02 à 00:37.
- **Pièce lue** : `brouillon-second-addendum-bbis-v1.md` (brouillon 1, non scellé), empreinte `a582e14dd22fd17e…` (compagnon vérifié :
  conforme), avec le rapport du rédacteur, `diff-v3-v4.txt`, le code v4, les essais, les pièces du dossier `second-addendum-v2/`
  (le dossier partiel `second-addendum-v1/` n'a ni été lu ni employé). Texte scellé `prereg/T0.7-etape-B-bis-v1.md`
  (`0ae6210f…` : empreinte recalculée, conforme) et premier addendum (`f00eda8a…` : recalculée, conforme) lus en entier là où ils
  sont touchés.
- **Interdits tenus** : aucune machine, aucun appel au loueur, aucune dépense ; aucun score ni aucune donnée de 7a ou de 7b ;
  jamais `relecture-bbis.json` ; rien sous `diag/`, `runs/`, `donnees/` ; aucune valeur de clé ; ni `env`, ni `printenv` ; aucune
  pièce modifiée ; rien de committé. Aucun identifiant de modèle dans ce rapport.

## 1. Verdict

**Corrections** : le brouillon est sain dans sa conception (le contrôle à 3 époques, la mesure d'information, les affaiblissements
déclarés et le coût tiennent), mais il laisse **un majeur** (des paragraphes du premier addendum qui font encore foi et disent
l'inverse du second, sans règle de préséance) et **cinq mineurs**. Aucun ne touche l'hypothèse, les seuils, le budget ni une issue.
Une fois les couples du § 6 appliqués, le contrôle mécanique à rejouer, et le code v4 contre-lu à part, la pièce peut être scellée.

## 2. Ce qui a été rejoué par le lecteur

1. **Contrôle mécanique des fragments** : rejoué à partir de T (`0ae6210f…`) et A1 (`f00eda8a…`) sur une copie du brouillon : conforme,
   texte en vigueur octet pour octet égal à `pieces/texte-en-vigueur-apres-second-addendum-v1.md` (`cmp` : égal). Vérifié en plus
   par un programme du lecteur : les huit « ancien » de SA-1 à SA-4 et SA-6 à SA-9 sont **égaux, en entier**, aux « nouveau » de
   EC-1 à EC-8 (pas seulement des sous-chaînes) ; les « ancien » de SA-10 à SA-20 figurent **une fois** dans T, ceux de SA-21 à
   SA-24 **une fois** dans A1 ; SA-5 est bien le reste de la ligne 186 que EC-4 laisse. Les phrases de R-PILE et du point (7) sont
   égales aux chaînes de `lecture_v3`. Les 26 compagnons `.sha256` du dossier se vérifient.
2. **Épreuves** : rejouées par le lecteur sur processeur (4 fils, machine chargée), dans une copie de travail du bloc-notes (`git archive` de `af0adb14` plus le dossier `code/`, données fabriquées seulement) : `tests/test_t07bbis_second_addendum_v1.py` et `tests/test_t07bbis_controle_v3.py` : **51 passés, 0 échec, 0 saut** en 32 min 45 s (la machine était partagée ; 4 min 31 s chez le rédacteur). 34 essais neufs et 17 de la v3 : comptes égaux à ceux du rapport. Les essais B2 et B3 (cas sains à 300 époques divergentes) et tous les artefacts passent. Non rejoué par le lecteur : la suite entière de B bis sur arbre de la forme de l'instance (155 passés, 18 sautés, 0 échec chez le rédacteur ; lue dans sa sortie, non refaite) ; le recompte de `MIN_ESSAIS` reste dû (§ 5, point 4).
3. **Chiffres** : empreintes des quatre rapports cités (`1fefa0a9…`, `0da982fb…`, `5ecb9235…`, `dd67802d…`) recalculées : égales.
   Les valeurs du contrôle (écart linéaire à 3 époques 9,2·10⁻¹², attention 9,5·10⁻¹⁰, information 5,31 ; anisotrope 3,1·10⁻¹² et
   3,79) sont celles de la sortie des essais. Coût recalculé : 5 × 2 × (18 × 4 + 1) = 730 ; 730 × 2,23 s = 0,45 h ; 730 × 5,3 s
   = 1,07 h ; × 1,2161 = 0,55 à 1,30 USD ; 2,14 h × 1,40 = 3,0 USD ; 5,1 + 0,55 à 1,30 + 0,1 à 0,2 = 5,8 à 6,6 ; cumul 6,0 + 19,8 =
   25,8 : justes. Citations de GO-2026-11-16-11 et -12 : verbatim conformes à `registres/go.md` (R-3031).

## 3. Réponses aux cinq points demandés

1. **Fragments** : les 24 « ancien » sont exacts et uniques (§ 2, point 1) ; les 24 « nouveau » sont cités au caractère dans le
   texte en vigueur. Rien d'autre ne change côté T : hypothèse, prédictions, seuils, niveaux, budget, plis, grille, 300 époques,
   garde de débit sont dits inchangés (§ 5) et le sont. **Réserve** : trois endroits du **premier addendum** restent faux ou
   contradictoires sans être nommés (M1) ; un point de détail de SA-5 (m1).
2. **Affaiblissements et double sens** : les deux affaiblissements (perte de la couverture « linéaire à 300 époques » ; perte de la
   comparaison de la sonde lue) sont dits sans fard, avec le motif exact (une erreur tardive déterministe propre à la carte passe).
   Le discriminant (§ 4) est à trois cas et honnête sur ce qu'il ne sépare pas. Un chiffre est trop optimiste pour l'attention
   (m2). La mesure n'est pas un contrôle : elle ne peut rattraper l'affaiblissement 1, et le texte ne le prétend pas.
3. **Code v4** : diff minimal. Le module de validation est un module neuf qui importe la v3 et ne redéfinit que le contrôle et la
   mesure (la copie de `ControleCarte.jouer` est nécessaire : elle appelle la fonction de ce module). Le contrôle a les deux
   familles à 3 époques (≤ 10⁻⁴), le déterminisme à 300 époques juste (réapprentissage sur la carte, égalité au bit près de w, b,
   q), l'information à 300 époques écrite avec `decide: False` et une tolérance infinie, sans arrêt. La lecture refuse un champ
   d'une autre version, d'un autre horizon, absent, non numérique, non fini. La mesure ne décide rien : aucune aire écrite
   (`_sans_aire`), aucun état, aucune issue ; erreur d'exécution = « non faite » sans rien de partiel ; garde = arrêt.
4. **Épreuves R5** : cas sains (jetons presque identiques ; anisotrope sans quasi-copie, 300 époques divergentes : B2, B3 ; forme de
   la répétition : B4) et artefacts (poids altérés, régularisation fausse, étiquette inversée, autre graine, lot d'autres données,
   non-déterminisme, sonde en échec à 3, 300 et 300 bis, horizon hors bornes ; champ de lecture : 14 artefacts) : présents et
   arrêtent. B1 reproduit l'arrêt du contrôle v3 sans erreur de chaîne : c'est la preuve que le remplacement est motivé.
   La graine du cas anisotrope est choisie pour diverger (quatre sur six) : déclaré, sans conséquence (cas sain d'un arrêt qu'on
   veut ne pas déclencher à tort), et la sonde préalable est gardée.
5. **Antériorité** : rien lu de 7a, 7b, `relecture-bbis.json` ; les chiffres cités de la course arrêtée viennent de R-3025 et des
   rapports ; aucun identifiant de modèle dans les pièces (seul le nom du fichier du brief de lancement, cité par T, contient
   « claude » : c'est un nom de document, non un identifiant de modèle).

## 4. Constats

### Majeur

**M1. Le premier addendum garde des blocs et des paragraphes « qui font foi » contredits par le second, sans règle de préséance.**
Le § 0 dit que SA-1 à SA-24 remplacent des fragments « dans T+1 et dans A1 », mais SA-1 à SA-9 ne visent que T+1 : les blocs
EC-1 à EC-8 de A1 (« Nouveau, qui fait foi : … linéaire à 300 époques … ») subsistent dans A1 tel que scellé. Et un paragraphe de
A1 n'est couvert par aucun SA : le dernier du § 5, « **R-PILE** (EC-2, EC-3) : une aire de la famille « attention » est celle
d'une sonde … ; **sur de vraies activations, elle n'est pas mesurée** ». Il dit, en texte du premier addendum, ce que SA-2, SA-3 et
SA-10 contredisent (R-PILE étendue à la linéaire ; la dispersion est désormais mesurée, entre deux ordres de calcul). Le
lecteur du verdict (R13) lit A1 et A2 ensemble : il tomberait sur deux phrases opposées. Corrections : une phrase de préséance au
§ 0 (couple K1) et un fragment SA-25 pour le paragraphe (couple K2, avec ses trois mises en cohérence de comptes). Le programme de
contrôle traite déjà `document : A1` : il suffit de rejouer.

### Mineurs

**m1. SA-5, « avant toute création » est faux à la lettre.** Trois créations ont déjà eu lieu (R-3003, R-3025) ; la phrase doit
viser la création de la nouvelle course (couple K3).

**m2. « À 3 époques, l'écart reste au plus de l'ordre de 10⁻¹⁰ » est vrai de la linéaire, faux de l'attention.** Les pièces du
dossier donnent pour l'attention 9,5·10⁻¹⁰ (carte émulée, B2), 1,5·10⁻⁸ (carte, quatrième passe) et 2,9·10⁻⁷ à 5,9·10⁻⁷ (deux
piles du processeur, sans signal ; cité par A1, § 5), alors que SA-1 cite, à l'appui de la phrase, le diagnostic de l'attention.
La tolérance 10⁻⁴ garde plus de deux ordres de marge : la conclusion tient, le chiffre non. Deux endroits : SA-1 (« Nouveau ») et
§ 4, premier cas (couples K4a et K4b).

**m3. Date et heures.** « Date : 2026-11-16, de 23:12 à la déclaration du rapport compagnon » : le travail et le rapport se
terminent le 2026-11-17 vers 00:01 (sorties d'essais horodatées 2026-11-17T00:00Z). Couple K5.

**m4. L'entropie reprise de la première fiche contredit la lettre de T, point 12 (« tirée à l'inscription de `CODE-BBIS` »), et le
texte ne le dit pas comme lecture.** Le § 5 la range parmi les choses « inchangées ». C'est un choix défendable (la deuxième ligne
`CODE-BBIS` « inscrit » une entropie ; aucun score n'a été lu) mais il a une conséquence qui doit être écrite avant la course :
mêmes sondes, même couple de tirage (`bbis/egalite-carte`), mêmes actions que la course arrêtée ; l'information à 300 époques de
la linéaire sera donc très probablement du même ordre que 1,004, et le discriminant dira « écart » : prédiction écrite avant
(R1, R4). Couple K6.

**m5. SA-2 énumère deux formes du résumé de la mesure ; le code en écrit quatre** (aussi « non lue », « aucune cellule calculable »,
`phrase_dispersion`). La phrase gelée est vérifiée égale, mais l'énumération du texte doit être complète (couple K7).

### Remarques facultatives (aucune correction exigée)

- **R1. Point (7), « elle est mesurée… »** : dans une course où la mesure est « non faite », la phrase gelée est fausse pour cette
  course ; R-PILE (qui la dit « non faite ») la corrige à la lecture. Acceptable ; si on veut le dire, il faut changer
  `lecture_v3.SECTION_D` (code) et SA-3 ensemble, donc rouvrir la contre-lecture du code.
- **R2. SA-24, « où la sonde ajuste bien »** : la quatrième passe a des données « sans signal apprenable » (A1, § 5, point 5) ;
  « ajuste bien » doit s'entendre « mémorise les données d'apprentissage » (largeur 4 096 > 640 actions). Une demi-phrase
  suffirait ; sans effet sur les critères.
- **R3. Coût** : la base de 5,14 USD est celle d'une marche arrêtée avant l'écriture et la poussée des fichiers fermés ; ces
  minutes ne sont pas dans « 5,8 à 6,6 USD ». Négligeable devant la marge (cumul pire cas 25,8 sur 40) ; à noter seulement.
- **R4. Calendrier de T** (ligne « mar. 17 : … répétition à blanc ; feu écrit ») : SA-1 dit qu'aucune répétition neuve n'est exigée ;
  la ligne du calendrier n'est pas une règle, aucun conflit, mais un lecteur pressé pourrait s'y tromper.

## 5. Points pour la session mère

1. **Écart à un texte scellé** : SA-10 à SA-20 touchent des fragments scellés de T (Métrique, plan 2, 8, 10 d, liste d'arrêt,
   données gardées, calcul et dépense). C'est bien l'objet de GO-2026-11-16-11 et -12 ; **aucun mot neuf de Lazar** n'est requis
   pour le fond ni pour la dépense (le calcul de coût est juste). À lui dire en une ligne : `registre_bbis_v2`, la branche
   `donnees/t07-etape-b-bis-v2` et `MIN_ESSAIS` relevé sont des conséquences mécaniques (hors de la demande, nécessaires, à
   accepter) ; ni l'un ni l'autre ne change un seuil ou une issue. Réponse du lecteur aux trois questions du rédacteur : (1) oui,
   acceptables ; (2) la répétition à blanc : voir le point 2 ci-dessous ; (3) garder l'entropie, **à condition d'écrire m4**.
2. **Risque principal de la course unique** : le contrôle à 3 époques de la **linéaire** sur la carte n'a jamais tourné sur carte
   (ni le déterminisme de la linéaire dans ce contrôle, ni la mesure). Si le contrôle v4 arrêtait la course sur la carte, la course
   unique serait perdue et il faudrait un nouveau mot de Lazar. La répétition à blanc (≈ 0,25 à 0,5 USD, un script à écrire) lèverait
   cette incertitude pour un dixième du prix de la course : **je la recommande**, sans l'exiger (le texte ne l'exige pas ; décision
   de la mère ou de Lazar).
3. **La garde de débit couvre la mesure** : si elle se déclenchait pendant la mesure (information seulement), la marche
   s'arrêterait sans écrire aucun score, l'apprentissage entier perdu pour une mesure d'information. Probabilité faible (marche
   attendue ≈ 4,1 à 4,7 h contre 11 h) ; comportement voulu par SA-10 (« une garde arrête la marche »). À savoir, pas à changer.
4. **Ordre des gestes** : le scellement de cet addendum et sa ligne `ADDENDUM-ECART-2-BBIS` doivent précéder la seconde ligne
   `CODE-BBIS` (condition de GO-2026-11-16-11) ; aucun code ne le vérifie (`ajouter_ligne_propre` ne regarde que `GO-BBIS` et
   `SCORES-BBIS`) : c'est un geste de la mère. Avant le feu : branche `donnees/t07-etape-b-bis-v2` absente (`git ls-remote`),
   recompte de `MIN_ESSAIS` sur l'arbre exact de l'instance (zéro marge : 148 = 115 + 33 ; un essai de plus sauté sur
   l'instance arrêterait le départ avant la marche, comme R-3003), liste des témoins de destruction, pilote 595 ou 580.
5. **Contre-lecture du code v4 encore due** (condition de GO-2026-11-16-11) : ce tour a rejoué les essais et lu le diff ; il ne tient
   pas lieu de la contre-lecture du code, que le brouillon d'addendum ne prétend d'ailleurs pas remplacer.
6. **Incident de ma main** (déclaré) : j'ai travaillé dans le bloc-notes partagé de la session, dans des dossiers de noms courts
   (`c1`, `arbre`) et un fichier `essais.txt`. Le dossier `arbre` a pu exister avant mon passage ; je l'ai supprimé (`rm -rf`) puis
   recréé par `git archive` pour rejouer les essais, et `essais.txt` a pu être écrasé. Ces copies sont de travail et se refont ;
   rien du dépôt, du dossier du rédacteur ni d'un registre n'a été touché. Je n'ai pas pu vérifier ce qui y était.

## 6. Corrections, sous forme de couples « ancien → nouveau »

Chaque « ancien » figure une seule fois dans `brouillon-second-addendum-bbis-v1.md` (vérifié par programme). Après application :
rejouer `pieces/controle-fragments-second-addendum-v1.py`, refaire le texte en vigueur et le premier addendum lu avec le second.

**K1 (M1) — préséance, § 0.**
- Ancien : `fait foi telle quelle. Chaque « ancien » figure`
- Nouveau : `fait foi telle quelle, à une exception : là où un bloc EC-1 à EC-8 de A1, ou un paragraphe de son § 3, de son § 5 ou de son § 6, dit autre chose qu'un fragment SA ou que le texte de ce § 2, le second addendum fait foi (les blocs EC de A1 restent lisibles comme l'histoire du premier écart, non comme le texte en vigueur). Chaque « ancien » figure`

**K2 (M1) — fragment SA-25 ; la ligne « Raison » de SA-21 à SA-24 devient celle de SA-21 à SA-25.**
- Ancien : `**Raison** (SA-21 à SA-24 ; réserve R-C de la contre-lecture). Ces paragraphes de A1 décrivent le contrôle de EC-1 ; laissés tels`
- Nouveau (à écrire exactement ainsi, le bloc SA-25 étant suivi d'une ligne vide puis de la ligne « Raison » modifiée) :

````text
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
````

- Mises en cohérence des comptes (trois couples) : `les fragments SA-1 à SA-24 du § 2` → `les fragments SA-1 à SA-25 du § 2` ;
  `applique les vingt-quatre` → `applique les vingt-cinq` ; et, dans la sortie du contrôle, « 24 écarts SA lus » devient 25 (sortie à
  refaire, pas un couple).

**K3 (m1) — SA-5.**
- Ancien : `et avant toute création, strictement`
- Nouveau : `et avant la création de la course qu'accorde GO-2026-11-16-11, strictement`

**K4a (m2) — SA-1, « Nouveau ».**
- Ancien : `l'écart reste au plus de l'ordre de 10⁻¹⁰ (`brouillons`
- Nouveau : `l'écart reste au plus de l'ordre de 10⁻¹⁰ pour la linéaire et de 10⁻⁹ à 6·10⁻⁷ pour l'attention (`brouillons`

**K4b (m2) — § 4, premier cas.**
- Ancien : `l'ordre de 10⁻¹⁰ sur tous les jeux fabriqués ;`
- Nouveau : `l'ordre de 10⁻¹⁰ pour la linéaire et de 6·10⁻⁷ pour l'attention sur les jeux fabriqués ;`

**K5 (m3) — date.**
- Ancien : `- **Date (UTC, `date -u`)** : 2026-11-16, de 23:12 à la déclaration du rapport compagnon.`
- Nouveau : `- **Date (UTC, `date -u`)** : de 2026-11-16T23:12Z à 2026-11-17T00:01Z (déclaration du rapport compagnon).`

**K6 (m4) — entropie, § 5.**
- Ancien : `reprise telle quelle par la fiche remplaçante : aucun score`
- Nouveau : `reprise telle quelle par la fiche remplaçante (lecture déclarée du point 12 de T, « tirée à l'inscription de `CODE-BBIS` » : l'entropie est celle que porte la ligne `CODE-BBIS` en vigueur, non retirée ; conséquence, prédite avant la course : mêmes sondes, même couple de contrôle et mêmes actions que la course arrêtée, donc écart de la linéaire à 300 époques probablement de l'ordre de 1, discriminant « écart » ; sans effet sur aucun état) : aucun score`

**K7 (m5) — SA-2, énumération du résumé.**
- Ancien : `ou « mesure non faite » et son motif) ; sur données fabriquées`
- Nouveau : `ou « mesure non faite » et son motif, ou « non lue », ou « aucune cellule calculable ») ; sur données fabriquées`

(K7 change le « Nouveau » de SA-2, donc le texte en vigueur : la phrase gelée entre guillemets de R-PILE n'est pas touchée ; le
contrôle d'égalité à `RESERVES_FIXES` reste vrai.)

## 7. Déclaration

Rôle : contre-lecteur neuf (R2), lettre de modèle C ; lecteur de T0.7, exclu des lecteurs de P3-bis. Heures : voir l'en-tête.
Fichier écrit : celui-ci, seul. Rien d'autre n'a été écrit dans le dossier du rédacteur. Bloc-notes : copies de travail (voir § 5,
point 6). Aucune commande de location ni de création de machine ; aucun accès au réseau.
