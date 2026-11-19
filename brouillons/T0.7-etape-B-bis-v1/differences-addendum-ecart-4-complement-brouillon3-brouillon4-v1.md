# Différences entre le brouillon 3, le brouillon 4 et le texte candidat du complément au quatrième addendum d'écart — apprentissage des sondes sur la tâche (étape B bis de T0.7) — v1

Écrit par le rédacteur du complément (sous-agent de la session conductrice de la lecture, modèle Fable 5.2), par le programme qui a porté les remplacements. Aucun fichier de résultat ouvert, aucune garde jouée.

## Pièces

- Brouillon 3 : `brouillons/T0.7-etape-B-bis-v1/addendum-ecart-4-complement-brouillon3-v1.md`, `d9affd94e094fc5ddb941542b5a2b04c14ca440af1fdd492e879fca8fa719abe` (inchangé, R12).
- Rapport de contre-lecture du brouillon 3 : `brouillons/T0.7-etape-B-bis-v1/contre-lecture-addendum-ecart-4-complement-brouillon3-v1.md`, `1b3fb66bb646792f09ba8a5707dcbe614d95455cd30effd185c7581335678cc8`.
- Brouillon 4 : `brouillons/T0.7-etape-B-bis-v1/addendum-ecart-4-complement-brouillon4-v1.md`, `3ce8447fe75f3903bb6953a2178c29ed1bd7885c4a511361501e756d6d3c9466`.
- Texte candidat, **non scellé**, **régénéré sous le même nom** à la demande de la conductrice : `prereg/T0.7-etape-B-bis-v1-addendum-ecart-4-complement-v1.md`, `a7dc8812dccf72a0bdcdd521c5671446a69674a32cf220a7f894fec64bf0d788`. Il remplace le texte candidat tiré du brouillon 3 (`dca3631a2f4e35fc7771a72488d979126e8e21ff9de2fbbb811420e999dc955d`), jamais scellé, qui n'existe plus sur le disque ; son contenu était le brouillon 3 hors l'en-tête.
- Fondements : d1, d2, d3 du rapport ; le nom du module final (R12 ; décision de la conductrice sous l'autonomie, accord de la mère du 2026-11-18 à 21:58:08Z, « d'accord pour (b) ») ; la garde des variables d'environnement de git (demande de la mère, même message : « Variables d'environnement de git : fais ajouter une garde au module final. Les commandes git de la preuve et de la garde tournent avec un environnement nettoyé des variables `GIT_*`, ou bien elles refusent de partir si l'une d'elles est posée, avec un essai sur le cas sain et sur l'artefact (une variable posée). Le contre-lecteur du code la vérifie. ») ; le statut des points ouverts ; l'en-tête.

## Compte des passages changés, par fondement

| fondement | passages |
|---|---|
| en-tête | 3 |
| nom du module (R12 ; décision de la conductrice, accord de la mère) | 10 |
| nom du module (R12 ; décision de la conductrice, accord de la mère) ; garde des variables de git (demande de la mère) | 4 |
| d3 | 2 |
| garde des variables de git (demande de la mère) | 3 |
| d2 | 1 |
| d1 | 2 |
| en-tête (contre-lectures citées) ; nom du module (R12 ; décision de la conductrice, accord de la mère) | 1 |
| statut | 1 |
| statut (table du rapport, point 6) | 1 |
| d1 (ce qui en découle) | 1 |
| d1 ; statut (table du rapport, point 7) | 1 |
| **total, brouillon 3 → brouillon 4** | **30** |

Passage changé sans fondement : **aucun**. Le bloc CQ-1 et les corrections c1 à c6 sont inchangés. Les anciens blocs CQ-2, CQ-4, CQ-5 et CQ-6 du brouillon 3 (six différences devenues sept dans la v4) sont retirés : la v4 garde six différences, les phrases du quatrième addendum redeviennent exactes ; les numéros CQ-2 à CQ-6 portent désormais le nom du module qui lit et le rattachement.

## A. Du brouillon 3 au brouillon 4

### A1 — titre — fondement : en-tête

Ancien :

````text
née d'un pur défaut de mise en place — brouillon 3
````

Nouveau :

````text
née d'un pur défaut de mise en place — brouillon 4
````

### A2 — en-tête, puce neuve « Brouillon 4 » — fondement : en-tête

Ancien :

````text
- **Date (UTC)** : brouillon 1, 2026-11-18, après l'inscription
````

Nouveau :

````text
- **Brouillon 4** : écrit par le même rédacteur, à la demande de la conductrice. Il part du brouillon 3
  (`brouillons/T0.7-etape-B-bis-v1/addendum-ecart-4-complement-brouillon3-v1.md`,
  `d9affd94e094fc5ddb941542b5a2b04c14ca440af1fdd492e879fca8fa719abe`, gardé intact, R12) et porte : les trois corrections
  mineures d1 à d3 de la contre-lecture du brouillon 3 par le même lecteur neuf d'un autre modèle (Opus 5.5 ;
  `brouillons/T0.7-etape-B-bis-v1/contre-lecture-addendum-ecart-4-complement-brouillon3-v1.md`,
  `1b3fb66bb646792f09ba8a5707dcbe614d95455cd30effd185c7581335678cc8` ; « scellable après corrections mineures », 0 majeur,
  3 mineurs, 7 notes) ; le statut des points ouverts selon sa table ; le **nom du module final**, `lecture_v5` (R12 ;
  décision de la conductrice sous l'autonomie, accord de la mère : § 1) ; la **garde des variables d'environnement de git**,
  différence D8 (demande de la mère : § 1) ; et rien d'autre. Lu en plus : ce rapport, en entier ; dans
  `src/controle_ia/t07bbis/lecture_v4.py`, `src/controle_ia/gardes.py` et `src/controle_ia/t07bbis/lien_mots_et_cout_v1.py`,
  les seules lignes qui lancent une commande git ; l'identifiant, l'heure, le titre et les noms de fichiers du commit
  `bb6f91f5b`.
- **Date (UTC)** : brouillon 1, 2026-11-18, après l'inscription
````

### A3 — en-tête, statut — fondement : en-tête

Ancien :

````text
- **Statut** : **brouillon 3, non scellé, sans effet.** Contre-lu au brouillon 1 par un lecteur neuf (R2).
````

Nouveau :

````text
- **Statut** : **brouillon 4, non scellé, sans effet.** Contre-lu aux brouillons 1 et 3 par un lecteur neuf (R2) ; les passages sur le nom du module et sur la garde des variables de git sont postérieurs à ces deux rapports.
````

### A4 — en-tête, statut, fin — fondement : nom du module (R12 ; décision de la conductrice, accord de la mère)

Ancien :

````text
**Aucun code avant cela ; aucune lecture avant cela.**
````

Nouveau :

````text
**Aucun code des différences D7 et D8 avant cela ; aucune lecture avant cela.**
````

### A5 — § 0, ce que le complément remplace — fondement : nom du module (R12 ; décision de la conductrice, accord de la mère)

Ancien :

````text
- Il remplace, **dans A4 et nulle part ailleurs**, les six fragments CQ-1 à CQ-6 du § 2 (« CQ » pour « complément au
  quatrième addendum »). CQ-3 porte sur le bloc « nouveau » de QA-4, c'est-à-dire sur la phrase de A2 telle que A4 la fait
  lire. Chaque « ancien » figure **une seule fois** dans A4 (compte d'occurrences par programme sur le texte scellé, retours de
  ligne compris) ; la chaîne « QA-1 à QA-3 » ne figure ni dans T, ni dans A1, A2, A3.
````

Nouveau :

````text
- Il remplace, **dans A4 et nulle part ailleurs**, les six fragments CQ-1 à CQ-6 du § 2 (« CQ » pour « complément au
  quatrième addendum »). CQ-3 porte sur le bloc « nouveau » de QA-4, c'est-à-dire sur la phrase de A2 telle que A4 la fait
  lire. Chaque « ancien » figure **une seule fois** dans A4 : il en est recopié à l'octet, retours de ligne compris, par le
  programme qui a écrit ce brouillon, lequel refuse un passage absent ou en double. Les chaînes `lecture_v4` et
  `RATTACHEMENT-LECTURE` ne figurent ni dans A1, ni dans A2, ni dans A3 ; `lecture_v4` figure dans T, l. 19 et l. 115, où
  elle nomme un fichier d'une autre étape (`src/controle_ia/t07/lecture_v4.py`), que rien ici ne touche.
````

### A6 — § 0, préséance — fondement : nom du module (R12 ; décision de la conductrice, accord de la mère)

Ancien :

````text
- **Préséance.** Là où A4 dit que la v4 du module de lecture est la v3 plus D1 à D6 « et rien d'autre », et que `main` ne
  change pas hors D6 (A4, § 6.1, § 6.2 essai 1, § 6.3), ce complément fait foi : la v4 porte une septième différence, D7.
````

Nouveau :

````text
- **Préséance.** Ce que A4 dit du module `lecture_v4` **lui-même** — copie de la v3 plus les six différences D1 à D6 « et
  rien d'autre », ses essais, son différentiel (A4, § 6.1, § 6.2) — reste vrai tel quel : ce module existe, à six
  différences, et n'est pas modifié. Là où A4 nomme `lecture_v4` comme **le module qui lit**, qui est lancé, dont
  l'empreinte est vérifiée ou qui est rattaché, et là où il nomme la clé `RATTACHEMENT-LECTURE-V4-BBIS` ou la fiche
  `rattachement-lecture-v4-bbis-v1.json`, ce complément fait foi : le module qui lit est **`lecture_v5`**, la clé est
  **`RATTACHEMENT-LECTURE-V5-BBIS`**, la fiche `rattachement-lecture-v5-bbis-v1.json`. Cinq de ces passages sont remplacés
  par les blocs CQ-2 à CQ-6 ; les autres se lisent de même par cette règle : A4, en-tête (statut, clé de rattachement) ;
  § 3 (« `lecture_v4` au lieu de `lecture_v3` », nom du module lancé et chaîne `commande` du manifeste) ; § 6.3 (fichiers
  donnés au contre-lecteur du code ; seconde mention de la clé) ; § 7, points 8 et 11.
````

### A7 — § 1, puces neuves : nom du module et garde des variables de git — fondement : nom du module (R12 ; décision de la conductrice, accord de la mère) ; garde des variables de git (demande de la mère)

Ancien :

````text
- **Symétrie (R4).** La règle élargit
````

Nouveau :

````text
- **Nom du module final : décision de la conductrice, qui n'est pas un mot de Lazar.** Fait rapporté par la conductrice,
  donnée d'organisation : le développeur a rendu et scellé `src/controle_ia/t07bbis/lecture_v4.py` dans son état à six
  différences (D1 à D6 de A4), empreinte `9bfca6269e34bb2a2ccd9b35c43c2af7b69e67b8bee45eab223cbd0a1c85f7ca`, commit
  `bb6f91f5b` de la branche `claude/lecture-verdict-etape-b-bis-v1`, avec ses essais
  `tests/test_lecture_bbis_v4_addendum_4_v1.py` (`97f4a69de29359ce24814997a0ff3e6815dad8333fcaffec606765a714eb6be2`) ; non
  rattaché, non contre-lu, jamais joué sur un fichier réel. Vérifié par le rédacteur : les deux empreintes sur le disque ;
  le commit, ancêtre de la tête de la branche de travail. On n'écrase jamais (R12) : le module qui porte une différence de
  plus prend un nom neuf, `lecture_v5.py`. **Décision de la conductrice sous l'autonomie, soumise à la mère** ; **accord de
  la mère** (message du 2026-11-18 à 21:58:08Z, mot pour mot : « d'accord pour (b) »). Écart déclaré : CQ-2 à CQ-6.
- **Garde des variables d'environnement de git : demande de la mère, qui n'est pas un mot de Lazar.** Même message de la
  mère, donnée d'organisation sous l'autonomie, mot pour mot : « Variables d'environnement de git : fais ajouter une garde au module final. Les commandes git de la preuve et de la garde tournent avec un environnement nettoyé des variables `GIT_*`, ou bien elles refusent de partir si l'une d'elles est posée, avec un essai sur le cas sain et sur l'artefact (une variable posée). Le contre-lecteur du code la vérifie. » Des deux formes que la mère laisse, **le refus est
  retenu, non le nettoyage** : aucun repli silencieux (R5). Elle est déclarée ici comme huitième différence, D8 (§ 6).
- **Symétrie (R4).** La règle élargit
````

### A8 — § 2, règle « Arrêt avant le seuil », preuve non faisable — fondement : d3

Ancien :

````text
**Si cette preuve ne peut pas être faite — un point en
défaut, une sortie non gardée, une sortie qui porte la ligne du seuil — il n'y a pas de
relance (la décision ne la permet que sur cette preuve) : nœud pour Lazar.**
````

Nouveau :

````text
**Une sortie non gardée, ou une sortie qui porte la ligne du
seuil : la lecture est consommée, aucune relance (point 3 de « La suite » ; GO-2026-11-18-64). Un point (A1) à (A3) en
défaut, ou une preuve qui ne peut pas être faite : aucune relance, nœud pour Lazar.**
````

### A9 — § 2, blocs CQ-2 à CQ-6 et leur raison — fondement : nom du module (R12 ; décision de la conductrice, accord de la mère)

Ancien :

````text
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
````

Nouveau :

````text
### CQ-2 — Module qui lit, règle de préséance de A4 (document : A4, § 0)

Ancien :

```text
le module est `lecture_v4`, rattaché par le § 6 de ce texte
```

Nouveau, qui fait foi :

```text
le module est `lecture_v5`, rattaché par le § 6 de ce texte et par le complément au quatrième addendum (`lecture_v4`, à six différences, reste et ne lit pas)
```

### CQ-3 — Code neuf, module de lecture (document : A4, bloc « nouveau » de QA-4, donc A2, SA-7, tel que A4 le fait lire)

Ancien :

```text
`lecture_v4` pour la lecture du point 10 du plan (les v1 à v3 restent, R12 ; la v4 est la v3 plus la lecture de l'ordre des lignes du registre propre que déclare le quatrième addendum, QA-1 à QA-3, et rien d'autre ; elle est rattachée par le quatrième addendum, non par la fiche de `CODE-BBIS` ;
```

Nouveau, qui fait foi :

```text
`lecture_v5` pour la lecture du point 10 du plan (les v1 à v4 restent, R12 ; la v4 est la v3 plus la lecture de l'ordre des lignes du registre propre que déclare le quatrième addendum, QA-1 à QA-3, et rien d'autre ; la v5 est la v4 plus la suite d'un pur défaut de mise en place et le refus sous variable d'environnement de git que déclare le complément au quatrième addendum, et rien d'autre ; la v5 est rattachée par le quatrième addendum et son complément, non par la fiche de `CODE-BBIS` ; la v4 n'est ni rattachée ni jouée pour la lecture ;
```

Le « nouveau » garde le compte des parenthèses de l'« ancien » : la parenthèse ouverte avant « les v1 » reste ouverte, fermée plus loin dans la phrase de A2.

### CQ-4 — Fiche de rattachement (document : A4, § 6.3)

Ancien :

```text
`registres/t07-etape-b-bis/rattachement-lecture-v4-bbis-v1.json` : empreinte de cet addendum scellé ;
  chemin et empreinte de `lecture_v4.py`, du fichier d'essais, du différentiel, de la sortie des essais, du rapport de
  contre-lecture du code ;
```

Nouveau, qui fait foi :

```text
`registres/t07-etape-b-bis/rattachement-lecture-v5-bbis-v1.json` : empreintes de cet addendum scellé et de son complément scellé ;
  chemins et empreintes de `lecture_v4.py` et de `lecture_v5.py`, du script de la preuve après coup, des fichiers d'essais, des différentiels, des sorties des essais, des rapports de
  contre-lecture du code ;
```

### CQ-5 — Clé de rattachement (document : A4, § 6.3)

Ancien :

```text
par une ligne de clé `RATTACHEMENT-LECTURE-V4-BBIS` (même format),
```

Nouveau, qui fait foi :

```text
par une ligne de clé `RATTACHEMENT-LECTURE-V5-BBIS` (même format),
```

### CQ-6 — Empreinte vérifiée au moment de lire (document : A4, § 6.3)

Ancien :

```text
`sha256sum` de `lecture_v4.py` comparé
  en entier, sur 64 caractères, à la fiche de rattachement inscrite ; les lignes `ADDENDUM-ECART-4-BBIS` et
  `RATTACHEMENT-LECTURE-V4-BBIS` présentes une fois chacune au registre voisin
```

Nouveau, qui fait foi :

```text
`sha256sum` de `lecture_v5.py` comparé
  en entier, sur 64 caractères, à la fiche de rattachement inscrite ; les lignes `ADDENDUM-ECART-4-BBIS`, `ADDENDUM-ECART-4-COMPLEMENT-BBIS` et
  `RATTACHEMENT-LECTURE-V5-BBIS` présentes une fois chacune au registre voisin
```

**Raison (CQ-2 à CQ-6).** Les décisions de Lazar demandent que « la garde prouve par programme » : il faut du code en plus
des six différences de A4. Le module à six différences est rendu et scellé sous le nom `lecture_v4.py` ; le changer
serait l'écraser (R12). Le code en plus va donc dans un module au nom neuf, `lecture_v5.py`, et c'est lui qui lit. La clé
`RATTACHEMENT-LECTURE-V4-BBIS` n'est pas inscrite à ce jour (donnée de la conductrice) : la clé `…-V5-…` la remplace, elle
ne s'y ajoute pas. **Ce que le brouillon 3 remplaçait et que ce brouillon ne remplace plus** : les phrases de A4 qui
comptent six différences pour la v4 (« plus les six différences », « `main` hors D6 », « plus D1 à D6 et rien d'autre »,
deux fois) ; elles redeviennent exactes telles que A4 les écrit, puisque la v4 garde ses six différences.
````

### A10 — § 3, « Inchangés » — fondement : nom du module (R12 ; décision de la conductrice, accord de la mère)

Ancien :

````text
QA-1 à QA-4 ; D1 à D6 ;
````

Nouveau :

````text
QA-1 à QA-3, et QA-4 hors le nom du module qui lit (CQ-3) ; D1 à D6
et le module `lecture_v4.py` tel qu'il est rendu, à l'octet ;
````

### A11 — § 4, point neuf 7 : ce que la garde des variables de git ne voit pas — fondement : garde des variables de git (demande de la mère)

Ancien :

````text
donc au relevé de l'opérateur ; hors du module, à la table « qui a lu quoi ».
````

Nouveau :

````text
donc au relevé de l'opérateur ; hors du module, à la table « qui a lu quoi ».
7. **La garde des variables de git (D8) ne voit que l'environnement du processus, au lancement.** Elle ne voit pas la
   configuration de git du dépôt, de l'utilisateur ou de la machine (fichiers de configuration, attributs, références de
   remplacement, greffes, dépôts de rechange), ni le programme `git` que le chemin de recherche désigne, ni les variables
   qui ne commencent pas par `GIT_`. Elle ne joue pas en mode jouet. Elle ne dit donc pas que git répond juste ; elle
   ferme une voie, celle d'une variable `GIT_*` qui ferait lire à git un autre dépôt, un autre index ou une autre
   configuration.
````

### A12 — § 5, état du code — fondement : nom du module (R12 ; décision de la conductrice, accord de la mère)

Ancien :

````text
le module
  de lecture neuf n'est pas écrit ;
````

Nouveau :

````text
le module
  `lecture_v4.py`, à six différences, est rendu et scellé, non rattaché, non contre-lu, jamais joué sur un fichier réel
  (donnée de la conductrice) ; `lecture_v5.py` n'est pas écrit ;
````

### A13 — § 6, titre — fondement : nom du module (R12 ; décision de la conductrice, accord de la mère) ; garde des variables de git (demande de la mère)

Ancien :

````text
## 6. Spécification de la différence D7 du module `lecture_v4`, et ses essais
````

Nouveau :

````text
## 6. Spécification des différences D7 et D8 du module `lecture_v5`, et leurs essais
````

### A14 — § 6, définition du module — fondement : nom du module (R12 ; décision de la conductrice, accord de la mère) ; garde des variables de git (demande de la mère)

Ancien :

````text
Le module **n'est pas écrit**. D7 s'ajoute à D1 à D6 de A4 ; rien d'autre ne change.
````

Nouveau :

````text
Le module `lecture_v5.py` **n'est pas écrit**. Fichier neuf `src/controle_ia/t07bbis/lecture_v5.py` : **copie à l'octet de
`lecture_v4.py`** (`9bfca6269e34bb2a2ccd9b35c43c2af7b69e67b8bee45eab223cbd0a1c85f7ca`), plus **D7**, **D8** et le **nom du
module** (dans `ecrire_lecture`, `commande="python -m controle_ia.t07bbis.lecture_v5"`, et dans les docstrings du module et
de `main`, comme D6 l'avait fait pour la v4 ; le docstring d'en-tête nomme ce complément et son empreinte scellée), **et
rien d'autre**. `lecture_v4.py` reste, à l'octet ; il n'est jamais rattaché ni joué pour la lecture. Aucun fichier existant
n'est modifié (R12). Les numéros de ligne cités ci-dessous sont ceux de la v3, comme dans le reste de ce texte.
````

### A15 — § 6, différence D8 — fondement : garde des variables de git (demande de la mère)

Ancien :

````text
ni de taire la ligne
  `BBIS LECTURE ENTREES OUVERTES`.
````

Nouveau :

````text
ni de taire la ligne
  `BBIS LECTURE ENTREES OUVERTES`.

**D8 — Refus si une variable d'environnement de git est posée.**

- **Forme retenue : le refus, sans nettoyage.** Fonction neuve `exiger_environnement_git_propre()` : si l'environnement du
  processus porte une variable dont le nom commence par `GIT_`, elle lève une `GardeArret` qui nomme ces variables par
  leur **nom seulement** (jamais une valeur, ni imprimée ni écrite). Elle ne retire ni ne change aucune variable.
- **Où elle est appelée** : en première instruction de `main`, avant `adaptateur_retenu`, avant toute commande git, toute
  lecture d'un registre et toute ouverture ; et en première instruction de `lire` quand `essai` est absent (lecture
  réelle). Effet : `BBIS LECTURE ARRET : …`, code 2, **rien d'écrit, aucune commande git lancée, rien d'ouvert**. Aucun
  paramètre de `lire` ni de `main` ne la désactive en lecture réelle. Elle ne joue pas en mode jouet.
- **Ce qu'elle couvre** : placée avant tout, elle vaut pour **toutes** les commandes git que le processus de la lecture
  lance, relevées par lecture du code : la preuve d'entrée conjointe (`preuve_entree_conjointe`) ; l'antériorité de
  l'étape B (`_git`, `anteriorite_etape_b`) ; le relevé du dépôt superficiel de D7 ; l'état du dépôt pour le manifeste
  (`gardes.etat_git`, par `manifeste.creer_manifeste`, appelé par `ecrire_lecture`) ; la lecture du code de la pièce
  « mots et coût » au commit cité (`lien_mots_et_cout_v1.octets_au_commit`), si la ligne `CODE-MOTS-ET-COUT-T06` fait
  charger cet adaptateur. Les deux derniers modules ne sont pas modifiés. La lecture n'appelle aucun contrôle
  d'ascendance de la fiche de code (`exiger_ancetre` n'est appelé que par la marche et la création).
- **Nature de l'arrêt** : rien n'est ouvert et rien n'est écrit ; c'est un arrêt avant le seuil, sans rien écrire, donc la
  voie de GO-2026-11-18-64 (preuve après coup), **fermée tant que Lazar n'a pas dit son mot sur le point ouvert 7**. La
  commande de lecture l'évite : elle lance le module dans un environnement d'où les variables `GIT_*` ont été retirées
  par un geste écrit, leurs noms relevés sans leurs valeurs dans la sortie gardée du lancement (point ouvert 9).
````

### A16 — § 6, fichier des essais — fondement : nom du module (R12 ; décision de la conductrice, accord de la mère)

Ancien :

````text
dans le fichier d'essais de A4, § 6.2, sur registres,
````

Nouveau :

````text
dans un fichier neuf, `tests/test_lecture_bbis_v5_complement_addendum_4_v1.py` (nom hors du motif
`test_t07bbis_*`, comme celui de A4, § 6.2), sur registres,
````

### A17 — § 6, essai 6 et essai neuf 7 — fondement : nom du module (R12 ; décision de la conductrice, accord de la mère) ; garde des variables de git (demande de la mère)

Ancien :

````text
6. **Différentiel** : la v4 est la v3 plus D1 à D7 et rien d'autre.
````

Nouveau :

````text
6. **Différentiel** : `lecture_v5.py` est `lecture_v4.py` (`9bfca626…`) plus D7, D8 et le nom du module, et rien d'autre,
   vérifié par programme ; le différentiel est versé à part, avec son empreinte. Les essais de A4, § 6.2, rendus avec la v4
   (`tests/test_lecture_bbis_v4_addendum_4_v1.py`), restent ceux de la v4 et ne sont pas modifiés.
7. **Garde des variables de git (D8)** : cas sain, aucune variable `GIT_*` → la fonction passe et la lecture jouet se
   déroule ; artefact, une variable `GIT_*` posée (par exemple `GIT_DIR`) → `main` s'arrête en code 2 **sans avoir lancé
   aucune commande git** (lancement de processus espionné), sans rien écrire, et le message porte le nom de la variable,
   non sa valeur ; même refus par `lire` en lecture réelle ; une variable d'un autre nom (par exemple `GITHUB_TOKEN`, qui
   ne commence pas par `GIT_`) ne refuse pas.
````

### A18 — § 6, contre-lecture du code et rattachement — fondement : nom du module (R12 ; décision de la conductrice, accord de la mère)

Ancien :

````text
Contre-lecture du code et rattachement : ceux de A4, § 6.3, avec ce complément parmi les fichiers donnés ; la fiche de
rattachement porte aussi l'empreinte de ce complément scellé.
````

Nouveau :

````text
Contre-lecture du code et rattachement : ceux de A4, § 6.3, lus avec CQ-4 à CQ-6. Le contre-lecteur du code reçoit en plus
ce complément scellé, `lecture_v4.py`, `lecture_v5.py`, les deux différentiels (de la v3 à la v4, de la v4 à la v5), les
deux fichiers d'essais et leurs sorties ; il vérifie les six différences de la v4, D7, D8 et le nom du module, et que rien
d'autre ne sépare la v5 de la v3. La fiche `registres/t07-etape-b-bis/rattachement-lecture-v5-bbis-v1.json` cite le
quatrième addendum, ce complément, les empreintes de `lecture_v4.py` et de `lecture_v5.py` et celle du script de la preuve
après coup ; la mère l'inscrit par la ligne `RATTACHEMENT-LECTURE-V5-BBIS`, après la contre-lecture du code rendue sans
bloquant et avant toute lecture.
````

### A19 — § 6, programme de la preuve après coup, même garde — fondement : garde des variables de git (demande de la mère)

Ancien :

````text
garde, ne décode aucun fichier de résultat.
````

Nouveau :

````text
garde, ne décode aucun fichier de résultat. **Il porte la même garde que D8** : une variable d'environnement dont le nom
commence par `GIT_` étant posée, il refuse de partir, avant toute commande git, sans rien écrire (cas sain et artefact
éprouvés sur jouets).
````

### A20 — § 6, programme de la preuve après coup, point (A2) — fondement : d2

Ancien :

````text
aucun fichier nommé `lecture-bbis.json`, aucun fichier nommé
   `preuve-aucune-ouverture-bbis.json` ;
````

Nouveau :

````text
aucun fichier nommé `lecture-bbis.json` ni
   `preuve-aucune-ouverture-bbis.json` hors de ceux que citent, par chemin et empreinte, les lignes
   `PANNE-MISE-EN-PLACE-BBIS-<n>` déjà inscrites, chacun à l'empreinte citée ;
````

### A21 — § 6, programme de la preuve après coup, point (A3), commit nommé — fondement : d1

Ancien :

````text
a les octets du même fichier à la tête de la branche des sorties de la course (empreintes
   comparées, compagnons compris) ; la liste des noms de ces dossiers est celle de cette tête,
````

Nouveau :

````text
a les octets du même fichier au commit `7322049dbbc10975ec1fa7dd54c10c8bc1ec4cf9` de la branche des
   sorties de la course (`donnees/t07-etape-b-bis-v2`, tête relevée par les règles communes de la lecture), où le script
   vérifie que `sondes-bbis.json` a l'empreinte de la ligne `SCORES-BBIS` (empreintes comparées, compagnons compris) ; la
   liste des noms de ces dossiers est celle de ce commit,
````

### A22 — § 6, programme de la preuve après coup, point (A3), lecture des mots — fondement : d1

Ancien :

````text
l'égalité est
   établie contre le commit des sorties auquel appartient le fichier que `SCORES-BBIS` cite (point ouvert 7).
````

Nouveau :

````text
l'égalité est
   établie contre ce commit, lié à la ligne `SCORES-BBIS` par l'empreinte de `sondes-bbis.json` ; c'est une lecture des
   mots « égales à celles de `SCORES-BBIS` », portée à Lazar (point ouvert 7).
````

### A23 — § 6, programme de la preuve après coup, issue — fondement : d3

Ancien :

````text
Non conforme, ou non faisable : nœud pour Lazar, aucune relance.
````

Nouveau :

````text
Une sortie absente ou portant la ligne du seuil : lecture consommée. Un point (A1) à
(A3) non conforme, ou non faisable : nœud pour Lazar, aucune relance.
````

### A24 — § 7, ligne de registre proposée — fondement : en-tête (contre-lectures citées) ; nom du module (R12 ; décision de la conductrice, accord de la mère)

Ancien :

````text
contre-lecture du brouillon 1 29c78e18 (scellable après corrections mineures, portées) |
````

Nouveau :

````text
contre-lectures 29c78e18 (brouillon 1) et 1b3fb66b (brouillon 3), scellable après corrections mineures, portées ; nom du module `lecture_v5` (décision de la conductrice, accord de la mère du 2026-11-18T21:58:08Z) ; module rattaché par RATTACHEMENT-LECTURE-V5-BBIS |
````

### A25 — § 7, moment de l'inscription — fondement : nom du module (R12 ; décision de la conductrice, accord de la mère)

Ancien :

````text
**avant** l'écriture du module.
````

Nouveau :

````text
**avant** l'écriture de `lecture_v5.py` et du script de
la preuve après coup.
````

### A26 — § 7, intitulé de la liste — fondement : statut

Ancien :

````text
**Points ouverts — statut après la contre-lecture du brouillon 1 et la décision GO-2026-11-18-64.**
````

Nouveau :

````text
**Points ouverts — statut après les contre-lectures des brouillons 1 et 3 et la décision GO-2026-11-18-64.**
````

### A27 — § 7, point ouvert 6 — fondement : statut (table du rapport, point 6)

Ancien :

````text
6. **Contre-lecture de ce brouillon** : faite au brouillon 1 par un lecteur neuf d'un autre modèle
   (`brouillons/T0.7-etape-B-bis-v1/contre-lecture-addendum-ecart-4-complement-brouillon1-v1.md`,
   `29c78e186ee602e8cad8079377c6eafdbd141ae46beb614c52277d55647e19ba`) : « scellable après corrections mineures », c1 à c6,
   portées ici. Les passages nés de GO-2026-11-18-64 (règle « Arrêt avant le seuil », absence de borne,
   programme de la preuve après coup) n'ont pas été contre-lus : ils sont postérieurs au rapport.
````

Nouveau :

````text
6. **Contre-lecture** : faite au brouillon 1
   (`brouillons/T0.7-etape-B-bis-v1/contre-lecture-addendum-ecart-4-complement-brouillon1-v1.md`,
   `29c78e186ee602e8cad8079377c6eafdbd141ae46beb614c52277d55647e19ba` ; c1 à c6, portées) et au brouillon 3
   (`brouillons/T0.7-etape-B-bis-v1/contre-lecture-addendum-ecart-4-complement-brouillon3-v1.md`,
   `1b3fb66bb646792f09ba8a5707dcbe614d95455cd30effd185c7581335678cc8` ; d1 à d3, portées ici), ce second rapport couvrant
   les passages nés de GO-2026-11-18-64. **Non contre-lus** : les passages sur le nom du module (CQ-2 à CQ-6, § 6) et sur
   la garde des variables de git (D8), postérieurs aux deux rapports.
````

### A28 — § 7, point ouvert 7, référence — fondement : d1 (ce qui en découle)

Ancien :

````text
(A3) compare les fichiers à la tête de la branche des sorties sans ouvrir `sondes-bbis.json`,
````

Nouveau :

````text
(A3) compare les fichiers au commit nommé de la branche des sorties sans ouvrir
   `sondes-bbis.json`,
````

### A29 — § 7, point ouvert 7, statut — fondement : d1 ; statut (table du rapport, point 7)

Ancien :

````text
La mère ou le contre-lecteur du script dit si cela tient les mots de la décision (« égales à
   celles de `SCORES-BBIS` »).
````

Nouveau :

````text
**Nœud de Lazar** : cette lecture remplace, pour les fichiers de scores et
   de sondes, les empreintes que consigne `sondes-bbis.json` par celles du commit des sorties lié à `SCORES-BBIS`. La
   voie de l'arrêt avant le seuil n'est pas employée avant son mot. Non bloquant pour le scellement : la voie de
   GO-2026-11-18-60 n'en dépend pas.
8. **Nom du module final** (`lecture_v5`, clé `RATTACHEMENT-LECTURE-V5-BBIS`) : décision de la conductrice sous
   l'autonomie, accord de la mère (§ 1) ; ce n'est pas un mot de Lazar. **Clos pour le scellement.**
9. **Garde des variables de git (D8)** : demandée par la mère (§ 1), forme du refus retenue par le rédacteur sur la
   recommandation de la conductrice. Deux suites à connaître : la commande de lecture doit retirer les variables `GIT_*`
   par un geste écrit avant le lancement (noms relevés, jamais les valeurs) ; un arrêt de D8 relève de la voie de
   l'arrêt avant le seuil, fermée jusqu'au mot de Lazar sur le point 7. Question d'organisation pour la mère.
````

### A30 — § 8, fichiers à donner au contre-lecteur — fondement : nom du module (R12 ; décision de la conductrice, accord de la mère)

Ancien :

````text
`src/controle_ia/t07bbis/lecture_v3.py` (`GardeEntrees`,
````

Nouveau :

````text
`src/controle_ia/t07bbis/lecture_v4.py` (lignes qui lancent une commande git) ;
`src/controle_ia/t07bbis/lecture_v3.py` (`GardeEntrees`,
````

## B. Du brouillon 4 au texte candidat (en-tête seulement)

### B1 — titre

Ancien :

````text
née d'un pur défaut de mise en place — brouillon 4
````

Nouveau :

````text
née d'un pur défaut de mise en place — version 1, scellée
````

### B2 — statut

Ancien :

````text
- **Statut** : **brouillon 4, non scellé, sans effet.** Contre-lu aux brouillons 1 et 3 par un lecteur neuf (R2) ; les passages sur le nom du module et sur la garde des variables de git sont postérieurs à ces deux rapports. Il ne vaut qu'après scellement
  sous `prereg/T0.7-etape-B-bis-v1-addendum-ecart-4-complement-v1.md`, et ligne `ADDENDUM-ECART-4-COMPLEMENT-BBIS` au registre
  voisin (§ 7). **Aucun code des différences D7 et D8 avant cela ; aucune lecture avant cela.**
````

Nouveau :

````text
- **Statut** : **version 1, scellée par la session conductrice de la lecture après vérification (l'heure du scellement est
  celle que porte la ligne `ADDENDUM-ECART-4-COMPLEMENT-BBIS` du registre voisin), en vigueur** pour la règle du § 2, les
  écarts CQ-1 à CQ-6, la préséance du § 0 et la spécification du § 6. **Accordés par Lazar** : la suite d'une issue « non
  lue » née d'un pur défaut de mise en place (GO-2026-11-18-60, R-3449) ; l'arrêt avant la première ouverture sans rien
  écrire, la preuve après coup et l'absence de limite du nombre de relances (GO-2026-11-18-64, R-3463). **Décidés sous
  l'autonomie, non par un mot de Lazar** : le nom du module final, `lecture_v5` (conductrice, accord de la mère), et la
  garde des variables d'environnement de git, D8 (demande de la mère). **Reste à Lazar** : le point ouvert 7 ; la voie de
  l'arrêt avant le seuil n'est pas employée avant son mot. Sur le brouillon 4
  (`brouillons/T0.7-etape-B-bis-v1/addendum-ecart-4-complement-brouillon4-v1.md`,
  `3ce8447fe75f3903bb6953a2178c29ed1bd7885c4a511361501e756d6d3c9466`), qui porte les corrections mineures des deux
  contre-lectures par un lecteur neuf d'un autre modèle (brouillon 1 :
  `29c78e186ee602e8cad8079377c6eafdbd141ae46beb614c52277d55647e19ba` ; brouillon 3 :
  `1b3fb66bb646792f09ba8a5707dcbe614d95455cd30effd185c7581335678cc8` ; « scellable après corrections mineures », aucun constat
  majeur) ; les passages sur le nom du module et sur la garde des variables de git sont postérieurs à ces rapports. Seules
  différences avec le brouillon 4 : le titre (« version 1, scellée ») et ce paragraphe de statut. Ligne
  `ADDENDUM-ECART-4-COMPLEMENT-BBIS` au registre voisin `registres/t07-etape-b-bis-v1-addenda-v1.md`, **avant** l'écriture
  de `lecture_v5.py` et **avant** toute lecture ; le scellement ne vaut pas lecture.
````
