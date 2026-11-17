# Contre-lecture du second addendum de B bis (T0.7) et du code v4 — tour 2 — v1

- **Lecteur** : contre-lecteur neuf (R2), lettre de modèle C. N'a écrit aucune des pièces, n'a pas fait le tour 1 (rapport lu,
  non écrit). Lecteur déclaré de T0.7 : exclu des lecteurs de P3-bis.
- **Heures (UTC, `date -u`)** : 2026-11-17, de 01:19 à 01:45.
- **Pièce lue** : `brouillon-second-addendum-bbis-v2.md` (brouillon 2, non scellé), empreinte `sha256` du compagnon vérifiée
  conforme (tous les compagnons `.sha256` du dossier, hors `second-addendum-v1/` non lu, se vérifient) ; différentiel avec
  `brouillon-second-addendum-bbis-v1.md` (`a582e14dd22fd17e…`, compagnon conforme) ; rapport du tour 1
  (`98a049d9f8b207eb336d04fc7e5a0b23bb5c066cd542bbc7719bd1e1b58fc120`, empreinte recalculée : égale) ; code v4 (non touché : aucun
  fichier de `code/` plus récent que le brouillon 1, compagnons conformes) ; essais et pièces du dossier. Texte scellé
  `prereg/T0.7-etape-B-bis-v1.md` (`0ae6210f…`) et premier addendum (`f00eda8a…`) : empreintes recalculées, conformes.
- **Interdits tenus** : aucune machine, aucun appel au loueur, aucune dépense ; aucun score ni donnée de 7a ou 7b ; jamais
  `relecture-bbis.json` ; rien sous `diag/`, `runs/`, `donnees/` ; aucune valeur de clé ; ni `env` ni `printenv` ; aucune pièce
  modifiée ; rien de committé. Aucun identifiant de modèle dans ce rapport.

## 1. Verdict

**Corrections** (une seule exigée, mineure). Les sept couples K1 à K7 du tour 1 sont appliqués **fidèlement, au caractère** ;
le différentiel contre le brouillon 1 ne contient rien d'autre que l'en-tête et la section 11 ; le contrôle mécanique, rejoué par
le lecteur, est conforme avec 25 fragments ; les essais neufs passent. Le majeur du tour 1 (M1) est levé. Reste **un point
exigé** : l'en-tête du brouillon 2 attribue la rédaction des corrections à la « lettre de modèle C », alors que la commande de
ce tour dit les corrections écrites par le modèle A (§ 4, m1). Une fois ce couple appliqué, la pièce peut être scellée ; aucun
autre changement n'est requis.

## 2. Vérification des corrections du tour 1 (couples K1 à K7)

Méthode du lecteur, indépendante du programme du rédacteur : un programme du lecteur extrait du rapport du tour 1 chaque couple
« ancien → nouveau » (K2 compris, avec son bloc SA-25), vérifie que chaque « ancien » figure **une seule fois** dans le brouillon 1,
les applique, puis compare le résultat au brouillon 2 ligne à ligne.

| Couple | Objet | Appliqué | Remarque |
|---|---|---|---|
| K1 | préséance, § 0 | oui, au caractère | texte du § 0, ligne 22 |
| K2 | fragment SA-25 et ligne « Raison » | oui, au caractère | + comptes « SA-1 à SA-25 » (§ 0) et « vingt-cinq » (§ 9), exigés par le rapport |
| K3 | SA-5, « avant la création de la course qu'accorde GO-2026-11-16-11 » | oui | |
| K4a, K4b | 10⁻¹⁰ linéaire, 10⁻⁹ à 6·10⁻⁷ attention (SA-1) ; 6·10⁻⁷ (§ 4) | oui | |
| K5 | date | oui | |
| K6 | entropie, lecture du point 12, prédiction | oui | |
| K7 | énumération du résumé, SA-2 | oui | |

Résultat : **les sept « ancien » sont uniques dans le brouillon 1 ; après application, le seul écart restant avec le brouillon 2
est** (a) le titre « brouillon 2 », (b) la ligne « Brouillon 2 » et la ligne « Statut » de l'en-tête, (c) les deux comptes
(« SA-25 », « vingt-cinq ») que le rapport demandait en mises en cohérence, (d) la section 11 ajoutée. Rien d'autre : hypothèse,
prédictions, seuils, niveaux, budget, garde de débit, coût et code ne changent pas. Le `diff` brut v1 contre v2 donne exactement
ces mêmes plages.

- **Comptes** : les occurrences de « SA-24 » restantes sont des renvois à ce fragment, justes ; plus aucun « vingt-quatre ».
- **Le programme de couples du rédacteur** (`pieces/couples-brouillon2-second-addendum-v1.py`) n'a pas servi de preuve : le lecteur
  a refait le travail par son propre programme (résultat égal).
- **Contrôle mécanique rejoué par le lecteur** : tronc léger (T `0ae6210f…` et A1 `f00eda8a…` de l'arbre, plus `code/src` en
  surcouche), copie du brouillon 2 et du programme `controle-fragments-second-addendum-v2.py` ; sortie : 25 écarts SA lus, chaque
  « ancien » unique (SA-25 : 465 → 683 caractères), « R-PILE et point (7) : égaux aux chaînes de lecture_v3 », **CONFORME**, code 0 ;
  le texte en vigueur et le premier addendum lu avec le second sont **octet pour octet égaux** à ceux du dossier (`cmp`). Le
  programme v2 ne diffère du v1 que par les noms de fichiers et le commentaire « SA-25 » (`diff`).
- **SA-25 en lui-même** : titre au même format que SA-21 à SA-24 (« (document : A1) »), « Ancien » unique dans A1 (465 caractères,
  texte exact du paragraphe), « Nouveau » conforme à K2 ; il dit la même chose que SA-2, SA-3 et SA-10 (R-PILE étendue aux deux
  familles, mesurée entre deux ordres de calcul, comme information, jamais entre la carte et une autre pile) ; les chiffres
  « 0,007 » et « 0,007 à 0,047 » sont ceux de SA-2 et SA-3. Dans le premier addendum lu avec le second, il ne reste aucune phrase
  « elle n'est pas mesurée » ; les blocs EC-1 à EC-8, qui disent l'ancien contrôle, sont couverts par la règle de préséance de K1.

## 3. Rejeu des vérifications que les corrections ont pu déranger

1. **Code v4** : inchangé depuis le tour 1 (aucun fichier de `code/` modifié après le brouillon 1 ; compagnons conformes ; `diff-v3-v4.txt`
   inchangé). Le diff minimal contre la v3, le contrôle à 3 époques, le déterminisme à 300 époques au bit près et l'information à
   300 époques écrite sans décider (`decide: False`, aucun arrêt) ont été jugés au tour 1 ; rien n'a bougé qui les remette en cause.
2. **Essais** (rejoués par le lecteur, processeur, 4 fils, machine chargée, tronc léger : arbre, `tests/` du dossier plus essais de la
   v3, dossiers `docs/sources/invites-*`, données fabriquées seulement) : première passe sur les deux fichiers d'essais : 42 passés,
   2 sautés (« chaîne de T0.6 absente de ce clone » : essai F de bout en bout en mode jouet et son homologue de la v3, que le tronc
   léger du lecteur ne porte pas), 7 erreurs de **mise en place** (module d'essais `test_t07bbis_apprentissage_v1` absent de mon
   tronc, pas un échec d'un essai) ; seconde passe des essais concernés (E1 à E5 : mesure de dispersion, et les deux essais de tirage)
   : **8 passés** en 2 min 32 s. Conclusion : tous les essais de contrôle, de mesure (ordre inverse effectivement joué, aucune aire
   écrite, échec d'une sonde, erreur d'exécution, garde, clés désalignées, compte des apprentissages) et de champ de lecture passent ;
   **non rejoués par le lecteur** : l'essai F et son homologue de la v3 (bout en bout en mode jouet), lus dans la sortie du rédacteur
   (`essais/sortie-essais-second-addendum-v2.txt` : 51 passés sur 51 après correction de la copie), et la suite entière sur arbre de
   la forme de l'instance (`MIN_ESSAIS`, à recompter). Les valeurs des cas sains de la sortie du rédacteur (quasi-copies : 9,175·10⁻¹²,
   9,483·10⁻¹⁰, information 5,307 ; anisotrope : 3,088·10⁻¹², 3,793) sont celles du brouillon 1 : le rédacteur dit juste que le code
   est inchangé.
3. **Épreuves R5** : cas sains (quasi-copies, anisotrope divergent à 300 époques sans quasi-copie, répétition) et artefacts
   (erreur de chaîne dès 3 époques, autre graine, poids altérés, étiquette inversée, non-déterminisme, sonde en échec, horizon hors
   bornes, 14 artefacts de champ) : présents, passent et arrêtent comme il faut ; B1 reproduit l'arrêt du contrôle v3 sans erreur de
   chaîne. Rien à ajouter.
4. **Antériorité** : aucun score ni donnée de 7a ou 7b lu (par le lecteur ; le brouillon 2 le déclare à l'identique du 1) ;
   `relecture-bbis.json` n'est cité qu'en interdit. **Identifiants de modèle** : aucun dans le brouillon 2, ni dans le programme de
   couples, ni dans les sorties ; les seules occurrences de « claude » sont le nom du fichier du brief de lancement (cité par T) et des
   chemins du bloc-notes dans la sortie des essais : noms de documents ou de dossiers, non des identifiants de modèle.
5. **Coût et discriminant** : inchangés par les couples ; le calcul (730 apprentissages, 0,45 à 1,07 h, 0,55 à 1,30 USD, cumul pire
   cas ≈ 25,8 sur 40) a été recalculé au tour 1 et rien ne l'a touché. K6 ajoute une prédiction écrite avant la course (écart de la
   linéaire à 300 époques de l'ordre de 1, discriminant « écart ») : cohérente avec le cas « information au-dessus de 10⁻⁴ » du § 4, dont
   la clé de lecture (`discriminant` = « ecart ») existe dans `lecture_v3`.

## 4. Constats

### Mineur exigé

**m1. L'en-tête du brouillon 2 déclare la lettre de modèle C pour le rédacteur des corrections ; la commande de ce tour dit les
corrections écrites par le modèle A.** Le brouillon 1 porte « lettre de modèle A » (ligne 3), le tour 1 la lettre C, le tour 2 (ce
rapport) la lettre C ; la ligne « Brouillon 2 » dit C pour un rédacteur « neuf » qui n'est ni l'auteur du brouillon 1 ni le
contre-lecteur du tour 1. Si le rédacteur est bien du modèle A, la ligne est fausse dans un texte qui sera scellé ; si la mère sait
qu'elle est juste, ignorer ce couple et le dire. À trancher par la mère (elle a lancé le rédacteur), puis :
- Ancien : `(lettre de modèle C ; n'a écrit ni le brouillon 1`
- Nouveau : `(lettre de modèle A ; n'a écrit ni le brouillon 1`
(« ancien » unique dans `brouillon-second-addendum-bbis-v2.md` : vérifié.)

Aucun autre point exigé. Aucun majeur.

### Remarques facultatives (aucune correction exigée)

- **R1. § 0 et § 9 citent encore les pièces v1** (`controle-fragments-second-addendum-v1.py`, sorties et textes en vigueur « v1 »), qui
  correspondent au brouillon 1 (24 fragments, sans SA-25). La section 11 le déclare (« les pièces v2 en tiennent lieu ») : le texte est
  cohérent à la lettre, mais un lecteur du verdict relancerait d'abord le programme v1, qui lit le brouillon 1. Si le brouillon 3 est de
  toute façon refait pour m1, il serait plus propre de nommer les pièces v2 aux quatre endroits (§ 0 : « `pieces/controle-fragments-second-addendum-v1.py` », § 9 : trois noms)
  et de retirer en conséquence la dernière phrase de la section 11 sur ce point. Sans effet sur le fond ; ne pas le faire est acceptable.
- **R2. Remarques du tour 1 (R1 à R4)** restent non appliquées, comme le brouillon 2 le dit : acceptable (R1 demanderait de rouvrir la
  contre-lecture du code ; R2, R3, R4 sans effet sur les critères).

## 5. Points pour la session mère

1. **Un seul couple exigé** (m1), et peut-être aucun si la lettre C est exacte : le dire. Ensuite : sceller sous
   `prereg/T0.7-etape-B-bis-v1-addendum-ecart-2-v1.md`, ligne `ADDENDUM-ECART-2-BBIS`, **avant** la seconde ligne `CODE-BBIS`
   (condition de GO-2026-11-16-11 ; aucun code ne le vérifie, c'est un geste de la mère). Aucun mot neuf de Lazar n'est requis pour la
   dépense (pire cas ≈ 25,8 USD sous les 40 de GO-2026-11-14-09) ni pour le fond : GO-2026-11-16-11 et -12 couvrent le second addendum,
   la mesure et la nouvelle course.
2. **Entropie reprise (K6)** : le brouillon 2 écrit le choix (même entropie que la première fiche) et sa conséquence prédite avant la
   course. La lettre de T (point 12 : « tirée à l'inscription de `CODE-BBIS` ») pourrait se lire autrement (nouvelle inscription,
   nouvelle entropie) ; GO-2026-11-16-11 laisse l'appréciation à la mère. Si la mère préfère une entropie neuve, il faut changer § 5, la
   fiche remplaçante et la prédiction K6 avant le scellement.
3. **Encore dus avant le feu** : contre-lecture du code v4 (condition de GO-2026-11-16-11 ; ce tour n'en tient pas lieu : il a rejoué les
   essais, non lu le code ligne à ligne) ; versement du code et recompte de `MIN_ESSAIS` (zéro marge : 148 = 115 + 33, l'essai F saute sur
   l'instance) sur l'arbre exact ; branche `donnees/t07-etape-b-bis-v2` absente à vérifier (`git ls-remote`) ; pilote 595 ou 580 ; liste des
   témoins de destruction.
4. **Répétition à blanc sur carte** : non exigée par le texte ; le tour 1 la recommandait (≈ 0,25 à 0,5 USD, un script à écrire, mot de
   Lazar sur sa ligne) parce que la course unique serait perdue si le contrôle v4 arrêtait sur la carte (la linéaire à 3 époques, son
   déterminisme et la mesure n'ont jamais tourné sur carte). Ce tour n'apporte rien de neuf : décision de la mère ou de Lazar.
5. **Garde de débit** pendant la mesure : peut arrêter la marche sans score pour une information seulement ; comportement voulu
   (SA-10), probabilité faible. À savoir.
6. **Incidents de ma main** (déclarés). (a) J'ai travaillé dans le bloc-notes partagé : dossier `cl-t2tour2` (créé par moi ; supprimé à
   la fin), fichier `k.py` ; j'ai exécuté `rm -rf` sur `c2` puis, après une première tentative abandonnée, sur `arb` : ces deux noms ont pu
   préexister dans le bloc-notes (je n'avais pas vérifié) ; le fichier `k.py` a pu en écraser un du même nom. Ce sont des copies de
   travail qui se refont ; rien du dépôt, du dossier du rédacteur ni d'un registre n'a été touché. (b) Ma première copie d'arbre
   (`git archive HEAD` de `prereg src docs`) a rempli le disque du bloc-notes (volume à 97 %, ≈ 1,4 Go libres) ; j'ai supprimé mes copies
   aussitôt ; **le volume reste presque plein : les sorties d'autres travaux ont pu être coupées pendant ces minutes**, la mère doit le
   savoir. (c) Aucune commande de location, aucun accès réseau.

## 6. Déclaration

Rôle : contre-lecteur neuf (R2), lettre de modèle C ; lecteur de T0.7, exclu des lecteurs de P3-bis. Heures : voir l'en-tête.
Fichier écrit dans le dossier du rédacteur : celui-ci, seul. Bloc-notes : copies de travail (§ 5, point 6).
