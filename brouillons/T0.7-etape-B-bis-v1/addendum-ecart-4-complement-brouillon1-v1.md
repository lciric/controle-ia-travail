# Complément au quatrième addendum d'écart déclaré au préenregistrement scellé de T0.7, étape B bis (apprentissage des sondes sur la tâche) — suite d'une issue « non lue » née d'un pur défaut de mise en place — brouillon 1

- **Auteur** : le rédacteur du quatrième addendum (sous-agent de la session conductrice de la lecture
  `session_013QMayjNC5GKdDFTN87oAV5`, modèle Fable 5.2). Il n'a écrit aucun code de l'étape B bis et n'écrit pas le module de
  lecture neuf ; il ne peut pas être le contre-lecteur de ce texte (R2) ; il ne sera ni lecteur-opérateur ni juge.
- **Date (UTC)** : 2026-11-18, après l'inscription de la ligne `ADDENDUM-ECART-4-BBIS` (2026-11-18T21:36:33Z) et de la ligne
  `GO-2026-11-18-60`. Heure exacte non relevée. Processeur seulement ; aucun commit, aucune poussée.
- **Statut** : **brouillon 1, non scellé, sans effet.** Il ne vaut qu'après contre-lecture par un lecteur neuf (R2), scellement
  sous `prereg/T0.7-etape-B-bis-v1-addendum-ecart-4-complement-v1.md`, et ligne `ADDENDUM-ECART-4-COMPLEMENT-BBIS` au registre
  voisin (§ 7). **Aucun code avant cela ; aucune lecture avant cela.**
- **Aucun résultat lu, rien d'exécuté sur les sorties, aucune garde jouée.** Lu et joué : § 5.

## 0. Textes qui font foi ; ce que ce complément remplace

- T, A1, A2, A3 : chemins et empreintes du § 0 du quatrième addendum. Quatrième addendum (« A4 »), scellé :
  `prereg/T0.7-etape-B-bis-v1-addendum-ecart-4-v1.md`, `5ef929eae8b070bc7f9d1934d487066ded34896df00dc8a9c70c91b44f0b30c4`
  (recalculée, égale au compagnon ; ligne `ADDENDUM-ECART-4-BBIS` du registre voisin, 2026-11-18T21:36:33Z). **A4 n'est pas
  réécrit (R12)** : ce complément s'y ajoute.
- Il remplace, **dans A4 et nulle part ailleurs**, les six fragments CQ-1 à CQ-6 du § 2 (« CQ » pour « complément au
  quatrième addendum »). CQ-3 porte sur le bloc « nouveau » de QA-4, c'est-à-dire sur la phrase de A2 telle que A4 la fait
  lire. Chaque « ancien » figure **une seule fois** dans A4 (compte d'occurrences par programme sur le texte scellé, retours de
  ligne compris) ; la chaîne « QA-1 à QA-3 » ne figure ni dans T, ni dans A1, A2, A3.
- Il ne touche **aucun énoncé ni aucune valeur** des sections « Hypothèse », « Prédiction », « Métrique », « Seuil »,
  « Critères de lecture gelés », « Puissance », « Données gardées ». **La phrase gelée de l'issue I0 ne change pas** (T, l. 143 :
  « Étape B bis non lue : [motif]. »). Ce qui change est **la suite** de cette issue dans un cas fermé (§ 2, la règle).
- **Préséance.** Là où A4 dit que la v4 du module de lecture est la v3 plus D1 à D6 « et rien d'autre », et que `main` ne
  change pas hors D6 (A4, § 6.1, § 6.2 essai 1, § 6.3), ce complément fait foi : la v4 porte une septième différence, D7.

## 1. Décision

- **GO-2026-11-18-60** (`registres/go.md` sur `main`, l. 424, seule ligne lue de ce fichier pour ce texte ; R-3449), texte de
  la ligne, mot pour mot : « **Lecture de l'étape B bis : une issue « non lue » née d'un pur défaut de mise en place ne consomme
  pas la lecture unique** (option a, R-3447), à une condition écrite dans le quatrième addendum et éprouvée (R5) : la garde
  prouve par programme qu'aucune donnée n'a été ouverte (aucun fichier de scores lu, aucune ligne d'ouverture au journal) ; la
  panne est corrigée, déclarée, puis la lecture relancée ; tout arrêt après une ouverture consomme la lecture. **Mot direct de
  Lazar dans la session mère**, verbatim « Ma recommandation. L’option a, confiance 0,7 : go ». »
- **« Écrite dans le quatrième addendum »** : A4 était scellé quand Lazar a tranché ; un texte scellé ne se réécrit pas (R12).
  La condition est donc écrite ici, dans un complément scellé et inscrit **avant le code** (message de la conductrice, donnée
  d'organisation). La mère dit si cette forme tient la lettre de la ligne (point ouvert 4).
- **Le point ouvert 4 de A4 est clos par cette décision** (CQ-1).
- **Symétrie (R4).** La règle élargit ce qui peut suivre un refus de la garde. Elle est décidée et écrite sans qu'aucune garde
  n'ait été jouée sur l'arbre de lecture et sans qu'aucune mesure n'ait été lue (§ 5) ; elle est fermée pour qu'un refus qui
  tient au fond ne puisse pas être rejoué.

## 2. Les faits, la règle, les écarts

### 2.0 Où le module ouvre des données, où il écrit au journal (`lecture_v3.py`, par simple lecture)

- **Bloc de la garde d'ouverture**, `lire`, l. 1235-1264. Dans l'ordre : lignes du registre propre (`lire_lignes`, l. 1236) ;
  lignes de lecture déjà inscrites (l. 1238-1240) ; registre partagé (l. 1241-1243) ; sceaux et antériorité à l'ouverture
  (`verifier_lignes`, l. 1244-1245) ; ordre des lignes (l. 1246) ; chemins de trois lignes (l. 1247-1252) ; antériorité de
  l'étape B (l. 1253) ; **construction de la liste blanche des entrées** (`GardeEntrees`, l. 1254) ; fichier d'issue de
  l'épreuve du signal planté (l. 1255-1260). Avant la l. 1254, le module n'a ouvert que les deux registres, les fichiers cités
  par leurs lignes pour en recalculer l'empreinte (`sceau_conforme`), et l'histoire git.
- **Première ouverture d'une sortie de la course** : `sondes-bbis.json`, l. 1270, après le bloc de la garde. **Fichiers de
  scores** : `charger_tableaux`, l. 1290 (définie l. 759-775), puis `sondes-bbis.npz` par `verifier_deux_premieres`, l. 1291.
  Toute ouverture d'une entrée passe par `GardeEntrees.exiger`, qui la consigne dans la liste `lus` (l. 538-547).
- **Journal des ouvertures** (`registres/t07-etape-b-bis-v1.md.ouvertures.md`) : une seule écriture, `main`, l. 1453, par
  `journaliser_ouverture`, **après** l'écriture du fichier de lecture (l. 1452) ; ligne de forme
  `| OUVERTURE-BBIS | date | lecture B bis (<run>) | empreinte du fichier de lecture |`.
- **Deux conséquences dans la v3**, que la règle doit regarder en face :
  1. **sur un refus de la garde, la v3 écrit quand même une ligne au journal** (`lire` rend l'issue I0, `main` écrit le
     fichier puis la ligne) : la condition « aucune ligne d'ouverture au journal » ne peut pas tenir sans changer cela ;
  2. **un arrêt du programme après une ouverture ne laisse aucune ligne au journal ni aucun fichier** (une `GardeArret` hors
     du bloc de la garde, ou l'arbre non propre au manifeste, l. 1454-1456 : code 2, rien d'écrit) : le journal seul ne dit
     pas qu'une ouverture a eu lieu.
- **Refus du bloc de la garde.** Seuls `RefusLecture` et `RefusRegistre` y sont rattrapés et rendus en I0 (l. 1261-1264). Les
  sceaux sont vérifiés par `t07.registre_v1.sceau_conforme` (l. 108-123), qui distingue quatre motifs : fichier absent ;
  compagnon absent ; compagnon différent du fichier ; fichier différent de l'empreinte du registre.

### La règle (la plus étroite qui suffit)

**Pur défaut de mise en place — définition fermée.** Un refus de la garde d'ouverture est un pur défaut de mise en place si,
et seulement si, **chacun** de ses motifs est l'un des trois suivants, relevés par programme à l'endroit où le refus est levé :

- **(M1) fichier non extrait** : un fichier cité par une ligne lue du registre propre ou du registre partagé est **absent du
  disque** de l'arbre de lecture, ou son compagnon `.sha256` est **absent du disque** ;
- **(M2) registre non extrait** : le registre propre ou le registre partagé est absent du disque de l'arbre de lecture ;
- **(M3) histoire git incomplète ou git en échec** : le dépôt de l'arbre de lecture est superficiel (`git rev-parse
  --is-shallow-repository` rend « true ») ; ou l'un des trois commits nommés par la preuve d'entrée conjointe de A4 est absent
  du dépôt ; ou une commande git de la garde rend un code de retour inattendu (ni 0, ni le 1 de « non ancêtre »).

**N'en sont pas, et gardent leur phrase gelée et leur suite (la lecture est consommée)** — liste non limitative, tout motif
hors de (M1) à (M3) étant « de fond » : une clé inconnue, une ligne exigée absente, en double ou mal formée ; une ligne de
lecture, de verdict ou de table conjointe déjà inscrite ; une ligne non strictement antérieure à l'ouverture ; **l'ordre des
lignes hors l'exception de QA-1**, et tout point (P1) à (P5) de la preuve d'entrée conjointe en défaut autrement que par un
objet git absent ; **une empreinte différente de celle consignée** (compagnon différent du fichier, fichier différent de
l'empreinte du registre) ; les chemins des lignes `SCELLEMENT-BBIS`, `RUN-CONFIRMATION-T06`, `SCORES-BBIS` ; **l'antériorité de
l'étape B** ; le commit du scellement introuvable dans un dépôt **non** superficiel ; une tête d'arbre qui ne descend pas du
commit de la course ; **l'issue de l'épreuve du signal planté autre que « vu »**, fichier illisible compris. Un refus qui
porte à la fois un motif de mise en place et un motif de fond est **de fond**.

**La condition « aucune donnée ouverte », prouvée par programme.** Sur un refus de pure mise en place, la garde joue la
**preuve d'aucune ouverture**, en trois points :

- **(O1) aucune entrée ouverte par cette exécution** : la liste blanche des entrées n'a pas été construite (le refus est levé
  avant la l. 1254 de la v3), ou sa liste `lus` est vide ;
- **(O2) la garde n'est pas passée** : le module n'a pas atteint le point où il imprime « garde passée » (D7, point (c)) ;
- **(O3) aucune ligne d'ouverture au journal** : le journal des ouvertures est absent du disque, ou présent sans aucune ligne
  dont la clé est `OUVERTURE-BBIS` (nombre de lignes et empreinte du journal relevés).

Elle est écrite par le programme de la garde dans une **pièce nommée, scellée** :
`diag/<run de lecture>/preuve-aucune-ouverture-bbis.json`, rattachée au manifeste du run comme le fichier de lecture, avec le
motif du refus, sa nature, les trois points et leurs relevés. **Un seul point en défaut : la preuve refuse, la lecture est
consommée**, et le module se comporte comme la v3 (ligne au journal comprise).

**La suite, quand la preuve passe.**
1. Le fichier de lecture écrit sur le refus (`diag/<run>/lecture-bbis.json`, issue I0, phrase gelée inchangée) et la pièce de
   preuve sont **gardés sous leur nom, jamais écrasés, jamais retirés** (R12). **Aucune ligne `LECTURE-BBIS` n'est inscrite**
   pour ce fichier ; **aucune ligne n'est écrite au journal des ouvertures**.
2. **La panne est corrigée** par le lecteur-opérateur, **sur l'arbre de lecture seulement** : histoire complète récupérée,
   fichier ou compagnon manquant extrait de sa branche. La correction ne change ni un registre, ni un texte scellé, ni le
   module rattaché, ni le contenu d'aucune entrée. Si elle le demandait, le défaut n'était pas de pure mise en place : arrêt,
   nœud.
3. **La panne est déclarée** par le lecteur-opérateur dans une pièce scellée,
   `registres/t07-etape-b-bis/lecture-v1/declaration-panne-mise-en-place-bbis-<n>-v1.md` (n = 1, 2, …) : motif du refus mot
   pour mot, chemins et empreintes du fichier de lecture gardé et de la pièce de preuve, ce qui a été corrigé et comment, nom
   du run de la relance. La conductrice la rend à la mère par chemin et empreinte ; **la mère l'inscrit au registre voisin**
   (clé `PANNE-MISE-EN-PLACE-BBIS-<n>`) **avant la relance**.
4. **La lecture est relancée** par la même commande, sous un **nom de run neuf** : le nom du run refusé suivi de
   `-relance<n>`. La garde est rejouée entière.
5. **Le verdict** cite chaque déclaration et chaque fichier gardé, et porte la réserve nommée **R-RELANCE** : « La lecture a
   été relancée [n] fois après un refus de la garde d'ouverture né d'un défaut de mise en place de l'arbre de lecture
   ([motifs]) ; à chaque fois, le programme a relevé qu'il n'avait ouvert aucune entrée et que le journal des ouvertures ne
   portait aucune ligne ; cette preuve ne voit pas une ouverture faite hors du module. »

**Tout arrêt après une ouverture consomme la lecture.** Dès que la garde est passée — ligne « garde passée » imprimée —, tout
arrêt, quelle qu'en soit la cause (garde d'arrêt de la lecture, erreur, arbre non propre au manifeste, processus tué),
**consomme la lecture** : aucune relance sous ce complément ; nœud de Lazar.

### CQ-1 — Point ouvert 4 de A4, clos (document : A4, § 7, point 4)

Ancien :

```text
Cet addendum ne déclare aucun écart sur ce point, et
   ce point **ne bloque pas le scellement**.
```

Nouveau, qui fait foi :

```text
Cet addendum ne déclare aucun écart sur ce point, et
   ce point **ne bloque pas le scellement**. **Clos après le scellement par GO-2026-11-18-60** (R-3449) : une issue « non lue » née d'un pur défaut de mise en place ne consomme pas la lecture, sous la règle fermée du complément au quatrième addendum (définition (M1) à (M3), preuve d'aucune ouverture (O1) à (O3) écrite par le programme, panne corrigée et déclarée, relance sous un nom de run neuf) ; tout arrêt après une ouverture consomme la lecture.
```

### CQ-2 — Nombre des différences du module (document : A4, § 6.1)

Ancien :

```text
plus les **six différences** ci-dessous, **et rien
d'autre**.
```

Nouveau, qui fait foi :

```text
plus les **sept différences** D1 à D6 ci-dessous et D7 du complément au quatrième addendum (§ 6), **et rien
d'autre**.
```

### CQ-3 — Code neuf, module de lecture (document : A4, bloc « nouveau » de QA-4, donc A2, SA-7, tel que A4 le fait lire)

Ancien :

```text
QA-1 à QA-3, et rien d'autre ;
```

Nouveau, qui fait foi :

```text
QA-1 à QA-3, et la suite d'un refus de pure mise en place que déclare le complément au quatrième addendum, et rien d'autre ;
```

### CQ-4 — Ce qui ne change pas dans `main` (document : A4, § 6.1, « Ne changent pas »)

Ancien :

```text
`main` hors D6 (codes de sortie, ce
qu'il imprime, écriture du fichier sur un refus de garde, journal des ouvertures)
```

Nouveau, qui fait foi :

```text
`main` hors D6 et D7 (hors D7 : codes de sortie, ce
qu'il imprime, écriture du fichier sur un refus de garde, journal des ouvertures)
```

### CQ-5 — Essai du différentiel (document : A4, § 6.2, essai 1)

Ancien :

```text
`lecture_v4.py` est `lecture_v3.py` plus D1 à D6 et rien d'autre
```

Nouveau, qui fait foi :

```text
`lecture_v4.py` est `lecture_v3.py` plus D1 à D7 et rien d'autre
```

### CQ-6 — Question au contre-lecteur du code (document : A4, § 6.3)

Ancien :

```text
la v4 est-elle la v3 plus D1 à D6 et rien d'autre
```

Nouveau, qui fait foi :

```text
la v4 est-elle la v3 plus D1 à D7 et rien d'autre
```

**Raison (CQ-2 à CQ-6).** La décision demande que « la garde prouve par programme » : il faut du code, donc une différence
de plus que A4 n'en comptait. La mention « la liste D2 à D6 » de D1 (docstring) se lit « D2 à D7 » par la préséance du § 0.

## 3. Ce qui ne change pas ; ce que le verdict cite

**Inchangés** : tout ce que le § 3 de A4 dit inchangé ; QA-1 à QA-4 ; D1 à D6 ; la preuve d'entrée conjointe ; la réserve
R-ORDRE ; la phrase gelée de I0 et toutes les autres ; le fait qu'un fichier de lecture est écrit et scellé sur tout refus de
la garde ; l'absence de tout mode « garde seule » (la garde s'exécute en tête de la lecture) ; le registre propre (aucune
ligne neuve, aucune clé neuve) ; la suite de tout refus **de fond** et de toute issue autre que I0 ; la ligne `LECTURE-BBIS`,
inscrite une seule fois, pour le fichier de la lecture qui compte.

**Le verdict cite** en plus : la ligne `ADDENDUM-ECART-4-COMPLEMENT-BBIS` ; s'il y a eu relance, les lignes
`PANNE-MISE-EN-PLACE-BBIS-<n>`, les fichiers gardés, et la réserve R-RELANCE. Sans relance, il ne porte pas cette réserve.

## 4. Ce que la preuve établit, et ce qu'elle n'établit pas

**Elle établit** que l'exécution qui a refusé n'a ouvert, par le module, aucune entrée de la liste blanche — ni sortie de la
course, ni fichier de 7b, ni fichier d'issue —, qu'elle n'a pas passé la garde, et que le journal des ouvertures ne portait
aucune ligne à cet instant.

**Elle n'établit pas** :
1. **qu'aucune donnée n'a été ouverte hors du module** : une lecture à l'œil, un autre programme, un autre agent lui
   échappent. Ce qui couvre cela est la table « qui a lu quoi » de la session, tenue par déclaration.
2. **qu'aucune exécution antérieure n'a ouvert des données puis s'est arrêtée sans trace** : dans la v3, un arrêt après une
   ouverture n'écrit ni fichier ni ligne au journal (§ 2.0). D7 y ajoute une ligne imprimée, « garde passée », avant toute
   ouverture : elle ne vit que dans la sortie de la commande, que le lecteur-opérateur garde et scelle à chaque lancement. La
   règle « tout arrêt après une ouverture consomme la lecture » tient donc au relevé de chaque lancement par l'opérateur, non
   à une trace que le programme retrouverait seul.
3. **que le journal n'a pas été retiré ou vidé** entre deux lancements : il est suivi par git dès qu'il est créé (A4, § 6.5,
   point 8) ; son histoire le dirait, la preuve ne la lit pas.
4. **Les arrêts du programme avant le passage de la garde, sans issue écrite** : registre propre absent ou fiche de code
   absente (l'entropie du manifeste ne peut pas être lue, `main`, l. 1449-1451), arbre non propre quand le fichier du refus
   s'écrit, clé de B bis dans le registre partagé, lecture demandée sur l'instance. Le programme s'arrête en code 2 : **ni
   fichier de lecture, ni pièce de preuve**. Ce complément **ne les couvre pas** : la décision parle d'une « issue « non lue » »
   et d'une preuve écrite par la garde ; ici il n'y a ni l'une ni l'autre (point ouvert 1). (M2), et (M1) quand le fichier
   manquant est la fiche de code, tombent dans ce cas avec le déroulement de la v3.
5. **Que la correction n'a touché que l'arbre de lecture** : c'est une déclaration de l'opérateur ; la garde rejouée entière à
   la relance (sceaux, empreintes, ordre, antériorités) est ce qui la contrôle.

## 5. Antériorité

- **Aucune mesure n'a été lue à ce jour**, par personne : appuis du § 5 de A4 (déclarations d'agents, non contre-lues), et
  message de la conductrice (donnée d'organisation). La garde d'ouverture n'a pas été jouée sur l'arbre de lecture ; le module
  de lecture neuf n'est pas écrit ; aucun refus de mise en place n'a eu lieu : la règle est écrite avant le premier cas.
- **Lu pour ce texte** : A4 scellé (§ 6.1, § 6.5, § 7 et l'en-tête) ; la ligne `GO-2026-11-18-60` de `registres/go.md` sur
  `main` ; les deux dernières lignes du registre voisin sur `main` ; `lecture_v3.py` (l. 505-680, 677-726, 759-806,
  1215-1464) ; `t07/registre_v1.py` (`sceau_conforme`, l. 108-123, et la classe `RefusRegistre`) ; `gardes.py` (classe
  `GardeArret`) ; `manifeste.py` (`ecrire_resultat`, l. 128-140, et lignes de l'arbre propre). **Joué** : des comptes
  d'occurrences sur le texte scellé de A4 ; `sha256sum` ; le scellement de ce fichier. **Aucun fichier sous `diag/`,
  `donnees/`, `runs/`, `docs/verdicts/` ; ni l'état, ni les décisions, ni les passations ; aucune garde appelée.**

## 6. Spécification de la différence D7 du module `lecture_v4`, et ses essais

Le module **n'est pas écrit**. D7 s'ajoute à D1 à D6 de A4 ; rien d'autre ne change.

**D7 — Suite d'un refus de pure mise en place.**

- **(a) Classe neuve `RefusMiseEnPlace(RefusLecture)`**, levée aux seuls endroits de (M1) à (M3) : dans `lire_lignes`
  (registre absent) ; dans `verifier_lignes` (fichier cité absent, compagnon absent — relevés **avant** l'appel de
  `sceau_conforme`, dont les deux autres motifs restent de fond) ; dans `anteriorite_etape_b` et `_git` (dépôt superficiel,
  code de retour inattendu) ; dans `preuve_entree_conjointe` (commit nommé absent, code de retour inattendu). Étant une
  `RefusLecture`, elle est rattrapée par le bloc de la garde et rendue en I0, phrase inchangée. Quand `verifier_lignes`
  rassemble plusieurs motifs, le refus n'est de mise en place que si **tous** le sont.
- **(b) Dans `lire`, à la branche du refus** : `res["garde"]` porte en plus `"nature"` (« mise en place » ou « fond ») ; pour
  « mise en place », `res["garde"]["aucune_ouverture"]` porte le rendu de la fonction neuve
  **`preuve_aucune_ouverture(racine, garde_entrees, passee) -> dict`**, qui relève (O1) à (O3) et rend `conforme` vrai ou
  faux avec les relevés ; elle ne lève rien pour un point en défaut.
- **(c) Dans `lire`, sitôt le bloc de la garde passé et avant la l. 1265 de la v3** : la ligne `BBIS LECTURE GARDE PASSEE`
  est imprimée (aucune valeur ; un état).
- **(d) Dans `main`, après l'écriture du fichier de lecture** : si la nature est « mise en place » **et** la preuve
  `conforme`, la pièce `preuve-aucune-ouverture-bbis` est écrite et scellée par `manifeste.ecrire_resultat` sous le manifeste
  du run, **aucune ligne n'est écrite au journal des ouvertures**, la ligne imprimée est
  `BBIS LECTURE NON CONSOMMEE <chemin du fichier de lecture> <empreinte> <chemin de la preuve> <empreinte>`, et le code de
  sortie est **3**. Dans tous les autres cas, `main` est celui de la v3 (ligne au journal, `BBIS LECTURE ECRITE`, code 0).
- **Aucun paramètre** de `lire` ni de `main` ne permet de déclarer une nature, de sauter la preuve, ni de taire la ligne
  « garde passée ».

**Essais exigés (R5), dans le fichier d'essais de A4, § 6.2, sur registres, dépôts git et arbres jouets seulement ; aucun
essai ne touche le registre réel, l'histoire réelle ni un fichier de résultat.**

1. **Cas sains** (un par motif) : fichier cité absent ; compagnon absent ; dépôt superficiel ; commit nommé absent → issue
   I0, nature « mise en place », preuve conforme, pièce écrite et scellée, **journal sans ligne**, code 3 ; puis, la panne
   corrigée sur l'arbre jouet, relance sous un nom de run neuf : la garde passe, la lecture jouet se déroule, le premier
   fichier et sa preuve sont intacts.
2. **Artefacts de la preuve** : journal portant déjà une ligne `OUVERTURE-BBIS` (O3) ; liste `lus` non vide (O1) ; garde
   passée (O2) → preuve non conforme, **pas de pièce « non consommée »**, ligne écrite au journal, code 0 comme la v3.
3. **Refus de fond**, chacun **sans relance possible** (nature « fond », ligne au journal, code 0) : empreinte d'un fichier
   cité différente de celle du registre ; compagnon différent du fichier ; ordre inversé hors l'exception ; point de la preuve
   d'entrée conjointe en défaut par contenu ; étape B antérieure au scellement ; issue de l'épreuve du signal planté autre que
   « vu » ; lecture déjà inscrite ; refus mêlant un motif de mise en place et un motif de fond.
4. **Arrêt après ouverture** : une garde d'arrêt déclenchée après le passage de la garde → la ligne « garde passée » a été
   imprimée, code 2, aucune pièce « non consommée ».
5. **R12** : relance sous le nom du run refusé → refus (le run existe).
6. **Différentiel** : la v4 est la v3 plus D1 à D7 et rien d'autre.

Contre-lecture du code et rattachement : ceux de A4, § 6.3, avec ce complément parmi les fichiers donnés ; la fiche de
rattachement porte aussi l'empreinte de ce complément scellé.

## 7. Ligne de registre proposée ; points ouverts

```text
| ADDENDUM-ECART-4-COMPLEMENT-BBIS | <heure UTC du scellement> | prereg/T0.7-etape-B-bis-v1-addendum-ecart-4-complement-v1.md | <sha256 du texte scellé> | GO-2026-11-18-60 ; R-3447 ; R-3449 ; complète ADDENDUM-ECART-4-BBIS 5ef929ea ; contre-lecture <rapport, empreinte> |
```

Au registre voisin, par la session mère, sur `main`, après le scellement, **avant** l'écriture du module.

**Points ouverts.**

1. **Arrêt du programme avant le passage de la garde, sans issue ni preuve écrites** (§ 4, point 4) : ni T, ni A4, ni la
   décision n'en disent la suite. Ce complément ne l'ouvre pas à la relance. À trancher par la mère ou Lazar ; la commande de
   lecture rend ce cas rare en contrôlant avant le lancement l'arbre propre, la présence des deux registres et de la fiche.
2. **Nombre de relances** : la décision n'en fixe pas ; ce texte non plus ; chacune est déclarée et inscrite.
3. **Clés neuves au registre voisin** (`ADDENDUM-ECART-4-COMPLEMENT-BBIS`, `PANNE-MISE-EN-PLACE-BBIS-<n>`) : à admettre par
   la mère, comme `RATTACHEMENT-LECTURE-V4-BBIS`.
4. **Lettre de la décision** : « écrite dans le quatrième addendum » est tenue ici par un complément scellé ; la mère dit si
   cela suffit.
5. **Code de sortie 3 et ligne imprimée « non consommée »** : états, non mesures ; la commande de lecture et le mandat du
   lecteur-opérateur doivent les connaître, ainsi que la ligne « garde passée ».
6. **Contre-lecture de ce brouillon** par un lecteur neuf (R2).

## 8. Fichiers à donner au contre-lecteur (R2)

Lecture seule : ce brouillon ; A4 scellé ; T (l. 114, 143, 192, 222) ; la ligne `GO-2026-11-18-60` de `registres/go.md` sur
`main`, seule ; `src/controle_ia/t07bbis/lecture_v3.py` (`GardeEntrees`, `lire_lignes`, `verifier_lignes`, `_git`,
`anteriorite_etape_b`, `charger_tableaux`, `lire`, `ecrire_lecture`, `main`) ; `src/controle_ia/t07/registre_v1.py`
(`sceau_conforme`) ; `src/controle_ia/t07bbis/registre_bbis_v1.py` (`journaliser_ouverture`) ; `src/controle_ia/manifeste.py`
(`creer_manifeste`, `ecrire_resultat`) ; le registre voisin.

Questions : chaque « ancien » est-il exact et unique dans A4 ; la définition (M1) à (M3) est-elle fermée et relevable par
programme, et laisse-t-elle passer un refus de fond ; les points (O1) à (O3) prouvent-ils ce que la décision demande, et le
§ 4 dit-il tout ce qu'ils ne prouvent pas ; D7 change-t-elle autre chose que la suite d'un refus de mise en place ; un refus
de fond peut-il être rendu rejouable par D7 ; la ligne « garde passée » est-elle bien imprimée avant toute ouverture d'une
sortie de la course.

Interdits : ceux du § 8 de A4.
