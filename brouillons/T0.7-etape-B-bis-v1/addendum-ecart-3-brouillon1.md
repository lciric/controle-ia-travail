# Troisième addendum d'écart déclaré au préenregistrement scellé de T0.7, étape B bis (apprentissage des sondes sur la tâche) — chaîne de lancement v6 de la course, entropie des graines et épreuve de niveau de la fiche de code en vigueur — brouillon 1

- **Auteur** : développeur neuf, sous-agent de la session mère. Il n'a écrit ni le texte scellé, ni ses brouillons, ni les deux
  addenda, ni le code v1 à v5, ni le projet de feu, ni sa contre-lecture, ni le rapport des préalables. Il a écrit les pièces que
  cet addendum rattache (amorce et lanceur v6, leurs essais) : il ne peut donc pas en être le contre-lecteur (R2).
- **Date (UTC, `date -u`)** : 2026-11-18, de 03:40Z à 04:10Z environ. Processeur seulement ; aucune machine, aucune dépense, aucun
  appel au loueur ni à l'hébergeur, aucun commit ni poussée.
- **Statut** : **brouillon 1, non scellé, non en vigueur.** À contre-lire par un lecteur neuf (R2), puis à accorder par Lazar
  (GO-2026-11-18-04 : « l'écart au dispositif scellé qu'elle suppose […] reste à accorder par Lazar sur pièce, avant le feu »),
  puis à sceller sous `prereg/T0.7-etape-B-bis-v1-addendum-ecart-3-v1.md` avec une ligne `ADDENDUM-ECART-3-BBIS` au registre
  voisin `registres/t07-etape-b-bis-v1-addenda-v1.md`, **avant** toute création de machine.
- **Aucun résultat lu** : ni score, ni issue, ni verdict de contenu de 7a, 7b, T0.6, de l'étape B de T0.7, de l'étape B bis ou de
  P3-bis. Lus : du code, les textes scellés, des registres, les deux fiches de code (empreintes, commit, entropie, niveau).

## 0. Textes qui font foi ; ce que cet addendum remplace

- Texte scellé `prereg/T0.7-etape-B-bis-v1.md`, `0ae6210f954917fecff647f45a129961c0676517381becbffe1fd5ac7b90d9eb` (« T ») ;
  premier addendum `prereg/T0.7-etape-B-bis-v1-addendum-ecart-v1.md`, `f00eda8a9fb74516289a085350425d128bf5b1cf1dbc50eee32d8bbe749c78d7`
  (« A1 ») ; second addendum `prereg/T0.7-etape-B-bis-v1-addendum-ecart-2-v1.md`,
  `18baeac32d26ebf174c62d7a36caedeee1d5b80648c6743c21dc30d2747afd26` (« A2 »). « T+2 » désigne T lu avec A1 puis A2.
- Cet addendum remplace, **dans A2 et nulle part ailleurs**, les cinq fragments TA-1 à TA-5 du § 2 (« TA » pour « troisième
  addendum »). Toute autre phrase de T, de A1 et de A2 fait foi telle quelle. Chaque « ancien » figure **une seule fois** dans A2
  (vérifié par programme à la rédaction : cinq comptes égaux à 1).
- Il ne touche **aucune** ligne des sections « Hypothèse », « Prédiction chiffrée et signe attendu », « Métrique », « Seuil »,
  « Plan d'analyse », « Critères de lecture gelés », « Liste d'arrêt », « Puissance », « Données gardées » de T+2.

## 1. Décisions

- **GO-2026-11-18-04** (`registres/go.md` ; R-3162), mot direct de Lazar, verbatim tel que la ligne le recopie : « go (a) pour
  l'amorce, go version complète recherche biblio » (option (a) de R-3160). Lecture de la ligne : écrire une amorce neuve
  (plancher d'essais juste, commit juste, fichiers extraits justes), la faire contre-lire par un agent neuf ; l'écart au
  dispositif scellé qu'elle suppose reste à accorder par Lazar sur pièce, avant le feu ; aucune dépense neuve (ligne
  GO-2026-11-14-09). **Cet addendum est cette pièce.** Il couvre TA-1 et TA-2 ; **l'accord de Lazar sur eux n'est pas encore donné.**
- **GO-2026-11-18-03** (R-3149), mot direct de Lazar, verbatim : « go recos sur les trois décisions de l'étape B bis ». Point (1)
  de la ligne : l'écart d'entropie des graines est couvert ; le verdict portera en réserve nommée que la prédiction écrite avant
  la course qui s'appuyait sur la reprise de l'entropie a perdu son appui. **Cet addendum l'écrit dans le texte (TA-3).**
- **À faire couvrir par Lazar, non couvert à ce jour** : l'épreuve de niveau rejouée (TA-4 et TA-5), relevée par la contre-lecture
  du projet de feu (`docs/notes/prealables-course-etape-b-bis-v1/contre-lecture-projet-de-feu-v3.md`, correction 1). La ligne
  GO-2026-11-18-03 ne nomme que l'entropie.
- **Dit à Lazar ici, pour qu'il le refuse s'il le veut** : le lanceur v6 porte un plafond de prix (1,40 USD/h) alors que
  GO-2026-11-18-03 (3) le dit « tenu hors du code » ; voir § 3, dernier point.

## 2. Les écarts

### TA-1 — Code neuf, lanceur et amorce de la course (document : A2, bloc « nouveau » de SA-8)

Ancien :

```text
scripts `scripts/lancer_bbis_v4.sh` et son amorce `scripts/amorce_bbis_v4.sh` (marche `marche_v4`, qui appelle `validation_imbriquee_v4` ; gardes de registre `registre_bbis_v2` ; branche de sortie `donnees/t07-etape-b-bis-v2` ; les v1 à v3 restent, R12)
```

Nouveau, qui fait foi :

```text
scripts `scripts/lancer_bbis_v6.sh` et son amorce `scripts/amorce_bbis_v6.sh` (marche `marche_v4`, qui appelle `validation_imbriquee_v4` ; gardes de registre `registre_bbis_v2` ; branche de sortie `donnees/t07-etape-b-bis-v2` ; les v1 à v5 restent, R12 ; les v6 sont rattachées par le troisième addendum, non par la fiche de `CODE-BBIS`)
```

**Raison.** La chaîne v5 (celle que la fiche de code en vigueur cite), lancée en l'état, s'arrêtait trois fois après avoir payé
son démarrage (R-3160 ; `docs/notes/prealables-course-etape-b-bis-v1/rapport-portillon-et-pilote-v1.md`) : (1) plancher de 176
essais compté sur l'arbre complet, alors que l'arbre extrait sur la machine n'en permet que 151 ; (2) commit de la course
(`05cd22aa…`) sans les lignes d'inscription de la fiche de code et de l'accord de calcul, que le lanceur ne voyait pas parce qu'il
lisait le registre de la tête ; (3) onze des 63 fichiers de la fiche hors des motifs d'extraction. La v5 n'a lancé aucune course.
La v6 est la v5 plus les écarts suivants, **et rien d'autre** (différence vérifiée par essai, § 6) :

- *Amorce v6* (six écarts) : plancher d'essais fixé à **151**, compte mesuré sur l'arbre qu'elle extrait ; **onze motifs
  d'extraction de plus**, ceux des onze fichiers de la fiche et eux seuls (amorce et lanceur v5 ; amorces, lanceurs et scripts de
  la répétition v1 à v3) ; contrôle avancé du registre propre et de la fiche, dès la fin de l'extraction, avant l'installation
  des paquets et la descente du modèle ; clé d'interface du conteneur exigée avant d'armer la minuterie de destruction ;
  empreinte de l'amorce écrite au journal ; nom du lanceur dans un message.
- *Lanceur v6* (cinq écarts) : garde « commit de la course » (l'arbre que l'amorce extrairait au commit passé est reconstruit
  sans réseau, et la garde d'entrée de la marche y est rejouée par le code même de cet arbre, avant d'imprimer la commande de
  création) ; garde « commit joignable » (commit présent sur la branche de code du dépôt distant) ; sous-commande qui mesure le
  compte d'essais sur l'arbre extrait ; image de la machine exigée par son nom ; plafond de prix de l'offre.

**Choix pour le troisième arrêt, et pourquoi.** Deux voies : étendre les motifs aux onze fichiers, ou écrire une fiche de code
neuve qui ne cite que ce qui est extrait. La seconde est fermée par le dispositif lui-même : une troisième ligne `CODE-BBIS` est
refusée par la liste d'arrêt scellée (« ligne `CODE-BBIS` remplacée une seule fois »), par la garde d'entrée de la marche
(`lecture_v3.lire_lignes` : deux lignes au plus, « en double ou mal formée » au-delà), par `registre_bbis_v2.ajouter_ligne_propre`
et par la garde de création (exactement deux lignes pour la course accordée). Elle demanderait une marche, une lecture et un
registre neufs, donc un écart bien plus large, sur le code qui calcule. La première n'ajoute à l'arbre de la machine que des
scripts de la chaîne : aucune donnée, aucun résultat, rien de la liste « Jamais », rien sous `docs/notes/`. **Elle est retenue.**

### TA-2 — Rattachement du code (document : A2, § 7)

Ancien :

```text
l'addendum ne monte pas sur l'instance (l'amorce n'extrait que `/prereg/T0.7-etape-B-bis-v1.md*`)
```

Nouveau, qui fait foi :

```text
aucun addendum ne monte sur l'instance (l'amorce n'extrait que `/prereg/T0.7-etape-B-bis-v1.md*`) ; le lanceur et l'amorce v6 ne sont pas cités par la fiche de `CODE-BBIS` : ils sont rattachés par leurs empreintes, écrites au troisième addendum, et l'amorce écrit la sienne au journal de l'instance
```

**Raison.** La fiche en vigueur (`registres/t07-etape-b-bis/code-bbis-v2.json`, `4b28535c17fe450ff1c1ecc9164d91c4c8d03354e4f4137e324f2b04390be5bb`)
cite l'amorce et le lanceur v5. Elle ne peut pas être remplacée (TA-1). Tout ce qui apprend, note et écrit les scores — les 63
fichiers de la fiche — reste contrôlé par empreinte sur la machine, par la garde d'entrée de la marche, inchangée. Ce qui échappe
à la fiche est ce qui lance : deux scripts, dont les empreintes sont ici (§ 6).

### TA-3 — Entropie des graines (document : A2, § 5) — couvert par GO-2026-11-18-03 (1)

Ancien :

```text
`code-bbis-v1.json`, reprise telle quelle par la fiche remplaçante
```

Nouveau, qui fait foi :

```text
`code-bbis-v1.json`, **non reprise** par la fiche remplaçante, qui porte l'entropie `149084685129585384182032033013812122656` au lieu de `208082752394230630219821407440340422345` (écart couvert par GO-2026-11-18-03 ; réserve nommée au verdict)
```

**Raison.** Constat de R-3146, vérifié sur les deux fiches. La conséquence que A2 prédisait avant la course (« mêmes sondes, même
couple de contrôle et mêmes actions que la course arrêtée, donc écart de la linéaire à 300 époques probablement de l'ordre de
1 ») **perd son appui** : le verdict le dira en réserve nommée. Aucun seuil, niveau, état ni issue n'en dépend.

### TA-4 — Épreuve de niveau (document : A2, § 5) — **à faire couvrir**

Ancien :

```text
`code-bbis-v1.json`, `ee362bb7…`, épreuve `641adeb5…`
```

Nouveau, qui fait foi :

```text
`code-bbis-v2.json`, `4b28535c…`, épreuve rejouée `da9fa42b…` (`registres/t07-etape-b-bis/epreuve-niveau-deux-plis-bbis-v2.json`) ; l'épreuve `641adeb5…` de la première fiche n'est plus dans le dépôt
```

### TA-5 — Épreuve de niveau (document : A2, § 7) — **à faire couvrir**

Ancien :

```text
l'épreuve de niveau de la première fiche.
```

Nouveau, qui fait foi :

```text
une épreuve de niveau rejouée sous l'entropie de la fiche remplaçante (`da9fa42bf95c9d6507b01d7bf69db2876a56c00d26b0cc58c15cd7893bfa5919`), au même niveau décisif retenu (0,99).
```

**Raison (TA-4, TA-5).** A2 épinglait par son empreinte l'épreuve de la première fiche (`641adeb57b8c271be60a89af2513805e591a63c7c0dde17883e4ace0d3f59cbf`).
La fiche en vigueur en porte une autre, rejouée ; `registre_bbis_v2.ecrire_fiche_code` exige d'ailleurs une épreuve jouée sous
l'entropie de la fiche, si bien que les deux écarts vont ensemble. Le niveau décisif retenu est 0,99 dans les deux fiches. **Non
vérifié par moi** : l'absence du fichier de la première épreuve (constat de la contre-lecture du projet de feu, selon R11) et la
raison du changement d'entropie.

## 3. Ce qui ne change pas

**Inchangés, et dits tels** : hypothèses et rivales ; prédictions chiffrées et signes ; métrique ; seuils ; niveaux (99 %
décisif, 95 % réserves) et niveau décisif retenu (0,99) ; plan d'analyse (plis, grille, 300 époques, plancher, nul de
réétiquetage, notation, contrôle carte-processeur de A2, mesure de dispersion, garde de débit) ; critères de lecture gelés
(états, issues, suffixes, libellés, table conjointe, réserves) ; liste d'arrêt (dont « ligne `CODE-BBIS` remplacée une seule
fois » : aucune troisième ligne) ; liste « Jamais » et interdits d'extraction (`docs/notes/`, pièce « mots et coût »,
`extraire_mesures_epreuve_t06_v1.py`, `lecture-sondes-t06.json`) ; registre propre (aucune ligne neuve, aucune clé neuve) ;
fiche de code et ses 63 empreintes ; marche `marche_v4` et tout le code sous `src/` ; branche de sortie ; budget (40 USD, coupure
39,5 USD, ligne GO-2026-11-14-09) ; compteur de relances (2, GO-2026-11-16-11 : cette course est la course unique accordée,
jamais partie) ; échéance et limite de relance.

**Changent, sans toucher une lecture** : le commit de la course (un commit de `main` qui porte les lignes d'inscription et la
fiche, au lieu de `05cd22aa…`, qui reste le commit **de la fiche**) et la branche de code passée à l'amorce (`main`) ; le
plancher d'essais de la machine (151 au lieu de 176 : les 25 essais qui sautent sautaient déjà, la v5 exigeait un compte que
la machine ne pouvait pas rendre) ; onze scripts de plus sur le disque de la machine.

**Plafond de prix.** GO-2026-11-18-03 (3) : « tenu hors du code », parce que le code ne pouvait plus changer. Le lanceur v6,
puisqu'il existe, refuse une offre au-dessus de 1,40 USD/h de carte. Cela **s'ajoute** au plafond écrit au feu et au prix relu
après création, sans les remplacer ; le verdict dira que le plafond tenait au lanceur v6 (hors de la fiche de code) **et** à
l'opérateur. Si Lazar préfère la lettre de sa décision, il faut un lanceur v7 sans cette garde.

## 4. Ce que ces gardes ne voient pas

1. **Le plancher est mesuré sur une reproduction, pas sur la carte** : Python 3.13 et torch sur processeur ici, Python 3.11 et
   torch pour la carte sur la machine ; la sortie de 7b (étape 3 de l'amorce) n'est pas apportée dans la reproduction. Le
   rapport des préalables n'a trouvé aucun essai qui bifurque sur la carte. Un compte plus bas sur la machine arrêterait la
   course à l'étape 5, après l'installation des paquets.
2. **Le plancher vaut pour un commit** : 151 est mesuré au commit candidat fabriqué (§ 6). Il se remesure au commit réel de la
   course (`lancer_bbis_v6.sh essais-du-commit`), avant le feu. Un plancher est un minimum : un essai `tests/test_t07bbis_*`
   ajouté plus tard le laisse franchi.
3. **La garde « commit de la course » rejoue la garde d'entrée sur l'arbre extrait, sans la sortie de 7b** : elle ne voit ni
   une sortie de 7b incomplète, ni la ligne `RUN-CONFIRMATION-T06` du registre partagé (contrôlée plus loin par la marche), ni
   un fichier de la liste « Jamais » que la branche de 7b apporterait.
4. **Clé d'interface du conteneur** : présente ne veut pas dire valide. La minuterie reste « jamais jugée par un code de
   retour » ; la ligne « minuterie lancée » se lit au journal et la session détruit par l'identifiant.
5. **Image** : exigée par son nom (`python:3.11-bookworm`), non par un condensé ; le contenu servi sous ce nom peut changer.
6. **Le contrôle avancé de l'amorce** est écrit pour n'arrêter que là où la marche s'arrêterait (mêmes contrôles, moins
   l'ancêtre et les dates) ; il ne remplace pas la garde d'entrée, que la marche rejoue entière.

## 5. Antériorité : aucun score de la course lu avant l'écart

La chaîne v5 n'a créé aucune machine (R-3160 : arrêts trouvés avant toute dépense). La course du 16 novembre n'a écrit aucun
score (A2, § 8). Ce brouillon et les pièces v6 ont été écrits sans ouvrir aucun fichier sous `diag/`, `runs/` ou `donnees/`, ni
aucune branche de données. Rien ne peut avoir été choisi d'après un score.

## 6. Rattachement du code, preuve, empreintes

Pièces neuves (aucun fichier existant modifié, R12 ; compagnons `.sha256` posés) :

| pièce | empreinte |
|---|---|
| `scripts/amorce_bbis_v6.sh` | `26f954e9e9783bf95a5149db9e848e1bd207dc8b027e6027d879363be2dfbbb5` |
| `scripts/lancer_bbis_v6.sh` | `3224ce14dc3fefe7cc46774072f65288a39c3fe760f325e311c5f948c45344b7` |
| `tests/test_chaine_bbis_v6_v1.py` (12 essais, cas sain et artefact de chaque garde neuve) | `f36571bd7fb7f5693f8e45433f44c7826722b9baf995ce219038923d486b49ca` |

Le fichier d'essais ne s'appelle pas `test_t07bbis_*` exprès : l'amorce ne joue sur la machine que ce motif, et son compte
n'en dépend donc pas.

Preuve par simulation, dossier `brouillons/T0.7-etape-B-bis-v1/preuve-amorce-v6-v1/` (chaque fichier a son compagnon) : clone
jetable de `main` (tête `8d88c812…`), commit candidat fabriqué `f233bd80b0d29896d490e55222e4280125530f56` qui ajoute les trois
pièces et leurs compagnons, jamais poussé ; tout joué sans réseau (`unshare -n`).

- **Plancher** : `lancer_bbis_v6.sh essais-du-commit` au commit candidat : 516 fichiers sur l'arbre extrait ; ligne de compte
  « 151 passed, 25 skipped, 4 warnings », code 0 ; « 151 passés ≥ 151 » (`sortie-essais-du-commit.txt`, `ca070374…` ;
  `essais-arbre-extrait-candidat.txt`, `83460ade…` ; `fichiers-de-l-arbre-extrait-candidat.txt`, `d48e74d3…`). Même compte à
  la tête `03af21a3…`, mesure antérieure du même jour.
- **Contrôles d'entrée de la marche** sur cet arbre : `marche_v4.gardes_d_entree`, jouée par le code de l'arbre : 63 fichiers de
  la fiche, aucun arrêt (`garde-entree-candidat.txt`, `8cbe0bc6…`) ; outil indépendant du rapport des préalables : aucun absent, aucune
  empreinte autre, commit de la fiche `05cd22aa…` ancêtre (`garde-entree-candidat-outil-v1.json`) ; contrôle avancé de l'amorce :
  « 63 fichiers de la fiche présents, empreintes conformes » (`fiche-sur-l-arbre-candidat.txt`).
- **Pilote de la commande** (`commande`, offre fabriquée `52d6f5c8…`, `AMORCE_ESSAI_LOCAL=1`, deux relances, texte de
  `feu-bbis-v2.txt`) : **code 0**, sortie d'erreur vide, deux lignes imprimées, seize caractères d'empreinte `26f954e9e9783bf9`,
  le texte décodé de la commande est l'amorce v6 à l'octet, aucun dossier jetable laissé (`sortie-commande.txt`, `a3be1198…`).
  **Artefact** : même pilote avec l'ancien commit `05cd22aa…` → code 2, « ligne CODE-BBIS absente (exigée) ; ligne GO-BBIS
  absente (exigée) » (`sortie-commande-05cd22aa.txt`, `43298cc4…`).

## 7. Points ouverts avant le scellement

1. Contre-lecture par un lecteur neuf (R2), de ce texte et des deux scripts.
2. Accord de Lazar sur TA-1 et TA-2 (chaîne v6 hors de la fiche de code), sur TA-4 et TA-5 (épreuve de niveau rejouée), et sur
   le plafond de prix porté par le lanceur.
3. Les empreintes du § 6 se relisent au commit où la mère dépose les pièces ; le compte d'essais se remesure à ce commit.
4. Le verdict de l'étape B bis cite la ligne `ADDENDUM-ECART-3-BBIS`, comme les deux premières.
5. Le feu (version 4) nomme : amorce v6 et ses seize caractères d'empreinte, lanceur v6, branche de code `main`, commit de la
   course, image, deux relances.

## 8. Fichiers à donner au contre-lecteur (R2)

Lecture seule : ce brouillon ; `scripts/amorce_bbis_v6.sh`, `scripts/lancer_bbis_v6.sh` et leurs différences avec la v5
(`diff scripts/amorce_bbis_v5.sh scripts/amorce_bbis_v6.sh`, de même pour le lanceur) ; `tests/test_chaine_bbis_v6_v1.py` ;
`brouillons/T0.7-etape-B-bis-v1/preuve-amorce-v6-v1/` ; T, A1, A2 ; `src/controle_ia/t07bbis/marche_v4.py` (garde d'entrée),
`lecture_v3.py` (`lire_lignes`), `registre_bbis_v2.py` ; `registres/t07-etape-b-bis-v1.md` et les deux fiches de code ;
`docs/notes/prealables-course-etape-b-bis-v1/` (rapport et contre-lecture du projet de feu) ; `registres/go.md`, lignes
GO-2026-11-14-09, GO-2026-11-16-11, GO-2026-11-18-03, GO-2026-11-18-04 ; `registres/decisions.md`, lignes R-3146, R-3149, R-3160,
R-3162. Questions : chaque « ancien » est-il exact et unique ; la v6 fait-elle ce que ce texte dit et rien d'autre ; une garde
neuve peut-elle arrêter une course saine sur la machine payée ; les onze motifs ouvrent-ils autre chose que les onze fichiers ;
reste-t-il un arrêt certain entre le démarrage et la marche. Interdits : rien sous `diag/`, `runs/`, `donnees/` ; aucune branche
de données ; aucune valeur de clé ; ni `env`, ni `printenv` ; aucune machine, aucun appel au loueur.
