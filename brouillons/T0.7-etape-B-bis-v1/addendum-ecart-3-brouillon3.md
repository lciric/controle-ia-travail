# Troisième addendum d'écart déclaré au préenregistrement scellé de T0.7, étape B bis (apprentissage des sondes sur la tâche) — chaîne de lancement v6 de la course, entropie des graines et épreuve de niveau de la fiche de code en vigueur — brouillon 3

- **Auteur** : développeur neuf, sous-agent de la session mère. Il n'a écrit ni le texte scellé, ni ses brouillons, ni les deux
  addenda, ni le code v1 à v5, ni le projet de feu, ni sa contre-lecture, ni le rapport des préalables. Il a écrit les pièces que
  cet addendum rattache (amorce et lanceur v6, leurs essais) : il ne peut donc pas en être le contre-lecteur (R2).
- **Brouillon 2** : écrit par un autre sous-agent neuf de la session mère, qui n'a écrit ni le brouillon 1, ni les pièces v6, ni
  les quatre contre-lectures, ni leur arbitrage. Il part du brouillon 1 (`addendum-ecart-3-brouillon1.md`,
  `0056edaa66b20c2e5b40cfecf7ef9752834ae68c76db9e2cf4c3cc7efe75b58d`, gardé intact, R12) et porte les dix corrections de la
  section « A. Brouillon 2 du troisième addendum » de l'arbitrage des quatre contre-lectures
  (`docs/notes/prealables-course-etape-b-bis-v1/arbitrage-contre-lecture-amorce-v6-v1.md`,
  `688abea5965a872b646148538f979be9dfd90d687c8eb73185eb092bcac150e3`), et seulement elles.
- **Brouillon 3** : écrit par un troisième sous-agent neuf de la session mère, qui n'a écrit ni les brouillons 1 et 2, ni les
  pièces v6, ni les quatre contre-lectures, ni leur arbitrage, ni la vérification du brouillon 2. Il part du brouillon 2
  (`addendum-ecart-3-brouillon2.md`, `a57895d42d002f99a1278e76c88ee9034a5fd12c31eb6711dde4ab90826f42e1`, gardé intact, R12) et
  porte les corrections de la vérification du brouillon 2 par un lecteur neuf
  (`docs/notes/prealables-course-etape-b-bis-v1/verification-addendum-3-brouillon2-v1.md`,
  `c320d50e2a9f80f1c5a260dc71f8025790bd8149e853960d34d01ae7af33431b` ; « à corriger », aucun bloquant) : un majeur (M1) et sept
  mineurs (m1 à m7), et seulement elles.
- **Date (UTC, `date -u`)** : brouillon 1, 2026-11-18, de 03:40Z à 04:10Z environ ; brouillon 2, 2026-11-18, achevé à 05:20Z
  (heure du fichier sur le disque) ; brouillon 3, 2026-11-18, de 05:30Z à 05:45Z environ. Processeur seulement ; aucune machine,
  aucune dépense, aucun appel au loueur ni à l'hébergeur, aucun commit ni poussée.
- **Statut** : **brouillon 3, non scellé, non en vigueur.** Le brouillon 2 a été vérifié par un lecteur neuf (R2) sur les points
  de l'arbitrage ; ce brouillon 3 porte ses corrections. À accorder par la mère sous GO-2026-11-18-05, selon R-3170 (8), sur ce
  brouillon une fois vérifié sans bloquant (§ 1), puis à sceller sous `prereg/T0.7-etape-B-bis-v1-addendum-ecart-3-v1.md` avec une ligne `ADDENDUM-ECART-3-BBIS`
  au registre voisin `registres/t07-etape-b-bis-v1-addenda-v1.md`, **avant** toute création de machine.
- **Aucun résultat lu** : ni score, ni issue, ni verdict de contenu de 7a, 7b, T0.6, de l'étape B de T0.7, de l'étape B bis ou de
  P3-bis. Lus : du code, les textes scellés, des registres, les deux fiches de code (empreintes, commit, entropie, niveau). Pour le
  brouillon 2, en plus : de la ligne du verdict de l'étape B au registre des sceaux, la clé et l'heure seulement. Pour le
  brouillon 3, en plus : des lignes de code (`marche_v4.py`, l. 60, 287, 363 ; l'essai de bout en bout du second addendum,
  `tests/test_t07bbis_second_addendum_v1.py`, l. 482-488) et la ligne du 16 novembre du registre des dépenses (l. 482, montants
  et cumul).

## 0. Textes qui font foi ; ce que cet addendum remplace

- Texte scellé `prereg/T0.7-etape-B-bis-v1.md`, `0ae6210f954917fecff647f45a129961c0676517381becbffe1fd5ac7b90d9eb` (« T ») ;
  premier addendum `prereg/T0.7-etape-B-bis-v1-addendum-ecart-v1.md`, `f00eda8a9fb74516289a085350425d128bf5b1cf1dbc50eee32d8bbe749c78d7`
  (« A1 ») ; second addendum `prereg/T0.7-etape-B-bis-v1-addendum-ecart-2-v1.md`,
  `18baeac32d26ebf174c62d7a36caedeee1d5b80648c6743c21dc30d2747afd26` (« A2 »). « T+2 » désigne T lu avec A1 puis A2.
- Cet addendum remplace, **dans A2 et nulle part ailleurs**, les cinq fragments TA-1 à TA-5 du § 2 (« TA » pour « troisième
  addendum »). Toute autre phrase de T, de A1 et de A2 fait foi telle quelle, sous la règle de préséance ci-dessous. Chaque
  « ancien » figure **une seule fois** dans A2, aucune fois dans T ni dans A1, et deux « anciens » ne se chevauchent pas : vérifié
  par programme, `brouillons/T0.7-etape-B-bis-v1/preuve-addendum-3-brouillon3-v1/controle-fragments-addendum-3-brouillon3-v1.py`
  (`44eb82c809739b96ad11f77b0b764014ea5027e4fd33d19a9d92fca3e086723a`), sortie `sortie-controle-fragments-addendum-3-brouillon3-v1.txt` (`d8760540276d06bbbc37f7e267699ef7b8dbc57b9c4b053b0cf17a13802507c2`) et A2 lu avec
  les cinq remplacements `a2-lu-avec-le-troisieme-addendum-brouillon3-v1.md` (`0f9c67657e5af209cb5901566853cfe1f19f7abb4d092725d03d7d2d36bc7f67`, pièce de travail, ne fait pas
  foi), même dossier, compagnons posés (programme du brouillon 2 repris sous un nom neuf, R12, pour lire le brouillon 3).
- Il ne touche **aucun énoncé ni aucune valeur** des sections « Hypothèse », « Prédiction chiffrée et signe attendu »,
  « Métrique », « Seuil », « Plan d'analyse », « Critères de lecture gelés », « Liste d'arrêt », « Puissance », « Données
  gardées » de T+2. Une clause de « Seuil » est concernée sans être changée : l'épreuve de niveau « lue avant toute ouverture de
  données de 7b » (T, l. 93) n'est pas tenue à la lettre par l'épreuve en vigueur (raison de TA-4 et TA-5). Vérifié par le même
  programme : les cinq « anciens » sont dans A2, § 5 et § 7, et dans le bloc « nouveau » de SA-8, qui porte sur la section
  « Code neuf » de T ; aucun ne recouvre les blocs SA-5 et SA-15 de la liste d'arrêt.
- **Préséance.** Là où une phrase de T, de A1 ou de A2 dit que le code de la course est cité par la ligne `CODE-BBIS` (T, en-tête,
  l. 5 ; T, section « Code neuf », l. 227, qui nomme `scripts/lancer_bbis_v1.sh` et son amorce), cela vaut pour le code neuf
  que la fiche cite (63 fichiers), non pour le lanceur et l'amorce v6, rattachés par le § 6 de ce texte ; le
  troisième addendum fait foi.

## 1. Décisions

- **GO-2026-11-18-04** (`registres/go.md` ; R-3162), mot direct de Lazar, verbatim tel que la ligne le recopie : « go (a) pour
  l'amorce, go version complète recherche biblio » (option (a) de R-3160). Lecture de la ligne : écrire une amorce neuve
  (plancher d'essais juste, commit juste, fichiers extraits justes), la faire contre-lire par un agent neuf ; l'écart au
  dispositif scellé qu'elle suppose reste à accorder par Lazar sur pièce, avant le feu ; aucune dépense neuve (ligne
  GO-2026-11-14-09). Cette lecture est celle de la mère, non le verbatim de Lazar. **Cet addendum est cette pièce.** Qui
  l'accorde : voir le point suivant.
- **GO-2026-11-18-05** (`registres/go.md` ; R-3170), mot direct de Lazar, verbatim tel que la ligne le recopie : « lance autonomie
  24h go depenses go recos par defaut par anticipation » ; autonomie de la mère du 2026-11-18T04:01:34Z au 2026-11-19 à la même
  heure. **R-3170 (8)**, verbatim : l'écart au dispositif scellé que suppose l'amorce corrigée « (code neuf, fiche de code neuve,
  épreuve de niveau rejouée `da9fa42b…` au lieu de `641adeb5…`) sera **accordé par la mère sous ce GO, sur pièce**, seulement
  après contre-lecture de l'amorce par un agent neuf rendue sans bloquant, et inscrit avec ses empreintes ». **Qui accorde, et sur
  quel texte** : la mère, sous GO-2026-11-18-05, sur ce brouillon 3 une fois vérifié sans bloquant (R2), puis
  scellé et inscrit avec ses empreintes. La condition « sans bloquant » n'est pas remplie à ce jour : l'arbitrage des quatre
  contre-lectures (`688abea5…`) a confirmé deux bloquants, dont un de texte que ce brouillon lève ; elle le devient quand le
  lecteur neuf du brouillon 2 n'en relève plus (vérification `c320d50e…` : aucun bloquant) ; l'autre, de machine (pilote de
  carte récent), ne se lève pas par ce texte : il se lève au feu version 4, qui exige un pilote de série 595 ou 580 (§ 4,
  point 9) ; l'accord ne vaut pas feu. **La pièce diffère du libellé de R-3170 (8)** : la v6 n'écrit aucune fiche de code
  neuve. L'accord nomme donc la pièce telle qu'elle est : chaîne v6 hors de la fiche (TA-1, TA-2 et la préséance du § 0), aucune
  fiche neuve, entropie changée (TA-3), épreuve rejouée (TA-4, TA-5), clause d'antériorité de l'épreuve (§ 0 et raison de TA-4 et
  TA-5), lecture déclarée de la liste d'arrêt (§ 3), lecture déclarée de la règle de la liste d'arrêt de T, l. 180, pour le
  tirage des plis internes (§ 5 ; la mère écrit si GO-2026-11-18-03 (1) la couvre déjà). **Le plafond de prix au lanceur (§ 3)
  n'est pas couvert par l'accord de la mère seul** : GO-2026-11-18-05 laisse à Lazar « tout ce qu'un mot exprès de Lazar a déjà
  tranché autrement », et GO-2026-11-18-03 (3) en est un (« tenu hors du code » ; « le verdict dira que ce plafond tenait à un
  opérateur et non au code ») ; ce point est porté à Lazar par la mère dans son compte rendu, et reste en réserve au verdict tant
  que Lazar ne l'a pas dit. **L'accord n'est pas encore donné.**
- **GO-2026-11-18-03** (R-3149), mot direct de Lazar, verbatim : « go recos sur les trois décisions de l'étape B bis ». Point (1)
  de la ligne : l'écart d'entropie des graines est couvert ; le verdict portera en réserve nommée que la prédiction écrite avant
  la course qui s'appuyait sur la reprise de l'entropie a perdu son appui. **Cet addendum l'écrit dans le texte (TA-3).**
- **À faire couvrir, non couvert à ce jour** : l'épreuve de niveau rejouée (TA-4 et TA-5), relevée par la contre-lecture
  du projet de feu (`docs/notes/prealables-course-etape-b-bis-v1/contre-lecture-projet-de-feu-v3.md`, correction 1), et sa clause
  d'antériorité (T, « Seuil », l. 93 ; raison de TA-4 et TA-5). La ligne GO-2026-11-18-03 ne nomme que l'entropie ; R-3170 (8)
  nomme l'épreuve rejouée : l'accord de la mère du point précédent les couvre, s'il est donné.
- **Dit à Lazar ici, pour qu'il le refuse s'il le veut** : le lanceur v6 porte un plafond de prix (1,40 USD/h) alors que
  GO-2026-11-18-03 (3) le dit « tenu hors du code » ; voir § 3, dernier point. Porté à Lazar par la mère ; en réserve au verdict
  tant que Lazar ne l'a pas dit (point précédent).

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

**Écart net depuis la version 4.** L'« ancien » nomme la v4. La v5 (plancher 176 ; noms) n'a été rattachée par aucun addendum :
le passage de la v4 à la v5 est inscrit comme un recompte (R-3074). La fiche en vigueur, inscrite le 17 novembre, cite la v5
alors que SA-8 nomme la v4 ; cet écart antérieur est déclaré ici et couvert avec TA-1. L'écart net au texte va donc de la v4 à
la v6, avec un plancher d'essais qui passe de **148 à 151** (et non de 176 à 151) ; la v5 ne diffère de la v4 que par le
plancher (amorce) et par des noms de scripts (lanceur), si bien que les autres écarts sont ceux des deux listes ci-dessus.
`diff` de la v4 à la v6, joints : `preuve-addendum-3-brouillon2-v1/diff-amorce-v4-v6.txt`
(`752e95ae8b4773e1b4593c16e53d402d2cfc9952909468077bea7d0a7a4b37a8`) et `preuve-addendum-3-brouillon2-v1/diff-lanceur-v4-v6.txt`
(`c5203c51346fed949d07af1ef873f0e343c483ceabcba1059a13568a94dcf9ef`), entre `scripts/amorce_bbis_v4.sh`
(`099a5c0e5d504b43b68140da86b4d69d91ea42d1725e2dddca0fad2750764277`) et `scripts/amorce_bbis_v6.sh`, et entre
`scripts/lancer_bbis_v4.sh` (`457457c0e9d32a1c5d03765b03a8ab63a69cdbc2a5147d534d0889d5a159062a`) et `scripts/lancer_bbis_v6.sh`.
La phrase de A2, § 7, « liste le code v4 » est traitée par TA-5.

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
cite l'amorce et le lanceur v5. Elle ne peut pas être remplacée (TA-1). Les 63 fichiers de la fiche (22 sous
`src/controle_ia/t07bbis/`, seul chemin de `src/` qu'elle cite, 21 scripts et 20 essais) restent contrôlés par empreinte sur la machine, par la garde
d'entrée de la marche, inchangée. Ce qui échappe à la fiche n'est pas seulement ce qui lance (deux scripts, dont les empreintes
sont ici, § 6) : le code hors de la fiche — les fichiers réutilisés de la l. 19 du texte scellé, que la marche importe,
`requirements-gpu.txt`, les fichiers de la racine extraits par le motif `/*` — est pris au commit de la course sans garde (§ 4,
point 7).

### TA-3 — Entropie des graines (document : A2, § 5) — couvert par GO-2026-11-18-03 (1)

Ancien :

```text
(même entropie que la fiche
`code-bbis-v1.json`, reprise telle quelle par la fiche remplaçante (lecture déclarée du point 12 de T, « tirée à l'inscription de `CODE-BBIS` » : l'entropie est celle que porte la ligne `CODE-BBIS` en vigueur, non retirée ; conséquence, prédite avant la course : mêmes sondes, même couple de contrôle et mêmes actions que la course arrêtée, donc écart de la linéaire à 300 époques probablement de l'ordre de 1, discriminant « écart » ; sans effet sur aucun état)
```

Nouveau, qui fait foi :

```text
(entropie **changée** : l'entropie est celle que porte la ligne `CODE-BBIS` en vigueur (lecture déclarée du point 12 de T, « tirée à l'inscription de `CODE-BBIS` »), soit `149084685129585384182032033013812122656` dans la fiche remplaçante `code-bbis-v2.json`, au lieu de `208082752394230630219821407440340422345` dans la fiche `code-bbis-v1.json` (écart couvert par GO-2026-11-18-03 (1) ; la prédiction écrite avant la course, « mêmes sondes, même couple de contrôle et mêmes actions que la course arrêtée, donc écart de la linéaire à 300 époques probablement de l'ordre de 1, discriminant « écart » », a perdu son appui : réserve nommée au verdict, GO-2026-11-18-03 (1) ; sans effet sur aucun état)
```

**Raison.** Constat de R-3146, vérifié sur les deux fiches. La conséquence que A2 prédisait avant la course (« mêmes sondes, même
couple de contrôle et mêmes actions que la course arrêtée, donc écart de la linéaire à 300 époques probablement de l'ordre de
1 ») **perd son appui** : le verdict le dira en réserve nommée. Aucun seuil, état ni issue n'en dépend ; le niveau, décidé par
l'épreuve sous chacune des deux entropies, est 0,99 dans les deux cas. L'« ancien »
prend tout le passage des l. 507-508 de A2, de « (même entropie que la fiche » à « sans effet sur aucun état) », pour que le
texte en vigueur ne dise plus à la fois « même entropie » et « non reprise », ni la prédiction au présent sous « Ce qui ne change
pas ». Le « nouveau » garde le compte des parenthèses de l'« ancien » : la parenthèse ouverte avant « entropie » se ferme, comme
avant, après « la mesure reprend les clés de la sonde ».

### TA-4 — Épreuve de niveau (document : A2, § 5) — **à faire couvrir**

Ancien :

```text
`code-bbis-v1.json`, `ee362bb7…`, épreuve `641adeb5…`
```

Nouveau, qui fait foi :

```text
`code-bbis-v2.json`, `4b28535c…`, épreuve rejouée `da9fa42b…` (`registres/t07-etape-b-bis/epreuve-niveau-deux-plis-bbis-v2.json`) ; l'épreuve `641adeb5…` de la première fiche est absente du dépôt (disque et index ; histoire non vérifiée)
```

### TA-5 — Épreuve de niveau (document : A2, § 7) — **à faire couvrir**

Ancien :

```text
liste le code v4 au commit versé, avec l'entropie et
l'épreuve de niveau de la première fiche.
```

Nouveau, qui fait foi :

```text
liste au commit versé (`05cd22aa…`) 63 fichiers, dont le code v4 et, en plus, l'amorce et le lanceur v5 (écart déclaré à TA-1 ; les v6 sont rattachés par le troisième addendum, non par la fiche), avec l'entropie de la fiche remplaçante (`149084685129585384182032033013812122656`, changée, TA-3) et une épreuve de niveau rejouée sous cette entropie (`da9fa42bf95c9d6507b01d7bf69db2876a56c00d26b0cc58c15cd7893bfa5919`), au même niveau décisif retenu (0,99).
```

**Raison (TA-4, TA-5).** A2 épinglait par son empreinte l'épreuve de la première fiche (`641adeb57b8c271be60a89af2513805e591a63c7c0dde17883e4ace0d3f59cbf`).
La fiche en vigueur en porte une autre, rejouée ; `registre_bbis_v2.ecrire_fiche_code` exige d'ailleurs une épreuve jouée sous
l'entropie de la fiche, si bien que les deux écarts vont ensemble. Le niveau décisif retenu est 0,99 dans les deux fiches.
L'absence du fichier de la première épreuve (`registres/t07-etape-b-bis/epreuve-niveau-deux-plis-bbis-v1.json`, chemin que la
première fiche cite) est vérifiée sur le disque et dans l'index (R11) ; le dépôt local est superficiel : son histoire n'est pas
vérifiée. **Non vérifié par moi** : la raison du changement d'entropie. L'« ancien » de TA-5 s'étend à toute la phrase de A2, § 7 (l. 546-547), depuis « liste le code
v4 » : « le code v4 » était inexact (la fiche cite aussi l'amorce et le lanceur v5), et « avec l'entropie » restait sans
complément.

**Clause d'antériorité de l'épreuve (section « Seuil » de T, l. 93), écart déclaré.** T veut l'épreuve de niveau « versée avec le
code et lue **avant toute ouverture de données de 7b** ». L'épreuve rejouée `da9fa42b…` a été jouée le 17 novembre et versée au
commit `d75587c8` à 2026-11-17T11:03:40Z. Elle vient donc après la course du 16 novembre, dont la marche avait relu les données de
7b sur la machine, de 17:58Z à 21:35Z, sans écrire de score (A2, § 6 et § 8 ; R-3025). La clause « lue avant toute ouverture de
données de 7b » n'est pas tenue à la lettre pour l'épreuve en vigueur. Le même fait touche les deux autres membres de la même
ligne : le niveau « inscrit avec la ligne `CODE-BBIS`, avant toute marche », et l'épreuve citée par la ligne `CODE-BBIS`
« avant toute exécution » ; la seconde ligne `CODE-BBIS`, qui inscrit l'épreuve rejouée et son niveau (17 novembre, 11:05:29Z),
vient après la marche du 16 novembre, et ces deux membres ne sont pas non plus tenus à la lettre pour l'épreuve en vigueur.
L'épreuve ne lit que des données fabriquées : son issue ne
peut pas dépendre de 7b, et le niveau décisif reste 0,99. Ni l'énoncé ni aucune valeur de « Seuil » ne change. À faire couvrir
avec TA-4 et TA-5 (§ 1).

## 3. Ce qui ne change pas

**Inchangés, et dits tels** : hypothèses et rivales ; prédictions chiffrées et signes ; métrique ; seuils ; niveaux (99 %
décisif, 95 % réserves) et niveau décisif retenu (0,99) ; plan d'analyse (plis, grille, 300 époques, plancher, nul de
réétiquetage, notation, contrôle carte-processeur de A2, mesure de dispersion, garde de débit) ; critères de lecture gelés
(états, issues, suffixes, libellés, table conjointe, réserves) ; liste d'arrêt (dont « ligne `CODE-BBIS` remplacée une seule
fois » : aucune troisième ligne) ; liste « Jamais » et interdits d'extraction (`docs/notes/`, pièce « mots et coût »,
`extraire_mesures_epreuve_t06_v1.py`, `lecture-sondes-t06.json`) ; registre propre (aucune ligne neuve, aucune clé neuve) ;
fiche de code et ses 63 empreintes ; marche `marche_v4` et tout le code sous `src/` ; branche de sortie ; budget (40 USD, coupure
39,5 USD, ligne GO-2026-11-14-09 ; la coupure porte sur le cumul de la ligne, qui comprend les ≈ 5,99 USD déjà dépensés
(répétitions 0,749, créations du 16 novembre 0,10 et 5,14 ; « cumul de la ligne ≈ 6,0 sur 40 », `registres/depenses.md`,
l. 482) : c'est la coupure « au reste de la ligne (≈ 34
USD) » de GO-2026-11-18-03 et de R-3170 (8)) ; compteur de relances (2, GO-2026-11-16-11 : cette course est la course unique accordée,
jamais partie) ; échéance et limite de relance.

**Liste d'arrêt, lecture déclarée, sans changer la phrase scellée.** Deux phrases de la liste d'arrêt, portées par A2, accordent
la course unique « sous ce texte et ses deux addenda » (SA-5, A2 l. 142) et « sous le second addendum » (SA-15, A2 l. 305).
« ses deux addenda » et « sous le second addendum » se lisent « sous le texte scellé, ses deux addenda et le présent addendum,
qui ne touche aucune ligne de la liste d'arrêt ». La course de la chaîne v6 est la course unique qu'accordent GO-2026-11-16-11
et SA-15. Cette lecture est à faire couvrir avec le reste (§ 1).

**Changent, sans toucher une lecture** : le commit de la course (un commit de `main` qui porte les lignes d'inscription et la
fiche, au lieu de `05cd22aa…`, qui reste le commit **de la fiche**) et la branche de code passée à l'amorce (`main`) ; le
plancher d'essais de la machine (151 au lieu de 176 : les 25 essais qui sautent sautaient déjà, la v5 exigeait un compte que
la machine ne pouvait pas rendre ; l'un d'eux est l'essai de bout en bout du second addendum,
`tests/test_t07bbis_second_addendum_v1.py`, l. 482-488, qui saute sur la machine, « chaîne de T0.6 absente de ce clone », et n'a
jamais tourné sur une machine, alors que A2, l. 527, compte « 34 essais » neufs sur l'instance ; contre-lecture « conformité »,
mineur m4) ; onze scripts de plus sur le disque de la machine.

**Plafond de prix.** GO-2026-11-18-03 (3) : « tenu hors du code », parce que le code ne pouvait plus changer. Le lanceur v6,
puisqu'il existe, refuse une offre au-dessus de 1,40 USD/h de carte. Cela **s'ajoute** au plafond écrit au feu et au prix relu
après création, sans les remplacer ; le verdict dira que le plafond tenait au lanceur v6 (hors de la fiche de code) **et** à
l'opérateur. Si Lazar préfère la lettre de sa décision, il faut un lanceur v7 sans cette garde. Ce point n'est pas couvert par
l'accord de la mère seul : porté à Lazar, en réserve au verdict tant que Lazar ne l'a pas dit (§ 1).

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
7. **Code hors de la fiche** : le code hors de la fiche — les fichiers réutilisés de la l. 19 du texte scellé, que la marche
   importe ; `requirements-gpu.txt` ; les fichiers de la racine extraits par le motif `/*` — est pris au commit de la course sans
   garde : la garde d'entrée de la marche ne vérifie que les 63 fichiers de la fiche. Le geste du feu B.4 de l'arbitrage le
   contrôle : `git diff --quiet 05cd22aa <COMMIT> -- src requirements-gpu.txt pyproject.toml tests/conftest.py
   'tests/test_t07bbis_*' 'tests/aide_t07bbis_*'` doit rendre le code 0 ; les empreintes des fichiers réutilisés sont comparées
   à la l. 19 du texte scellé, et `git ls-tree --name-only` de la racine à celui de `05cd22aa` ; sortie consignée ; écart : arrêt.
8. **Empreintes de la chaîne** : aucune garde ne compare l'amorce et le lanceur v6 aux empreintes du § 6. Le lanceur encode
   l'amorce lue sur le disque sans la comparer et n'en imprime que seize caractères d'empreinte ; l'amorce écrit la sienne au
   journal sans la comparer. Ce contrôle est tenu par le feu (geste B.3 de l'arbitrage) : `sha256sum` des deux scripts comparé
   en entier, sur 64 caractères, au § 6 de l'addendum scellé et inscrit ; ligne `ADDENDUM-ECART-3-BBIS` présente une fois au
   registre voisin ; base64 de la commande imprimée décodé et comparé aux 64 caractères de l'amorce v6 ; un seul écart : arrêt,
   rien n'est créé.
9. **Pilote de la carte** : la garde d'offre ignore la version du pilote (`driver_version` n'est lu ni par `registre_bbis_v2` ni
   par le lanceur), et l'amorce ne lit que « CUDA Version: », non « CUDA UMD Version: », forme des pilotes récents (séries 610 à
   620 ; arrêt de l'instance 60952525 le 16 novembre, pilote 615.71.09, `registres/arrets.md`, l. 133). Le feu tient donc la
   condition : pilote de série 595 ou 580 (`driver_version` commençant par `595.` ou `580.`), offre choisie par programme dans
   la sortie brute de la recherche d'offres.

## 5. Antériorité : aucun score de la course lu avant l'écart

La chaîne v5 n'a créé aucune machine (R-3160 : arrêts trouvés avant toute dépense). La course du 16 novembre n'a écrit aucun
score (A2, § 8). Ce brouillon et les pièces v6 ont été écrits sans ouvrir aucun fichier sous `diag/`, `runs/` ou `donnees/`, ni
aucune branche de données. Rien ne peut avoir été choisi d'après un score.

- **Heures** : épreuve rejouée versée au commit `d75587c8` à 2026-11-17T11:03:40Z ; fiche remplaçante inscrite au registre propre
  à 11:05:29Z (seconde ligne `CODE-BBIS`) et versée au commit `c098fb51` à 11:07:47Z ; ligne du verdict de l'étape B de T0.7 au
  registre des sceaux (`registres/scellements-v1.md`, clé `VERDICT-T07-ETAPE-B`) à 2026-11-17T11:20:08Z, dont seules la clé et
  l'heure ont été lues. L'épreuve et la fiche précèdent ce verdict.
- **Course du 16 novembre** : la relance (instance 60953606, engagée à 17:25Z, arrêt écrit de la marche à 21:35Z ;
  `registres/arrets.md`, l. 134-135) a relu les données de 7b sur la machine, sa marche tournant de 17:58Z à 21:35Z (A2, § 6 ;
  R-3025), sans écrire de score, avant l'épreuve rejouée (clause d'antériorité, raison de TA-4 et TA-5).
- Niveau, seuils, cellules, grille, adversaires, règle de construction des plis et plis externes (graine `partition-taches` de
  7b ; T, l. 116, point 12 ; `src/controle_ia/t07bbis/marche_v4.py`, l. 363) inchangés. Le tirage des plis internes (clés
  `bbis/interne/e0`, `bbis/interne/e1` ; `marche_v4.py`, l. 60, et `Graines(int(entropie), reelle=reelle)`, l. 287) et tous les
  tirages que l'entropie graine changent avec elle (TA-3), après la marche du 16 novembre, qui avait lu les sorties de 7b sans
  écrire de score. **Lecture déclarée** : la règle de la liste d'arrêt, l. 180 (« Changement d'une cellule, d'un réglage de la
  grille, des plis, d'un adversaire, d'un niveau ou d'un seuil après la lecture de toute sortie de l'étape B, de 7b ou de T0.7 :
  lecture invalide, version neuve »), vise un changement de la règle des plis, non le tirage que T, point 12, attache à
  l'entropie de la ligne `CODE-BBIS` en vigueur ; elle n'est pas déclenchée. Même lecture pour « **plis** externes et internes »
  sous « Inchangés » de A2, § 5, l. 509 : la règle des plis et les plis externes, non le tirage des plis internes. Écart
  d'entropie couvert par GO-2026-11-18-03 (1) ; cette lecture est à faire couvrir avec le reste (§ 1) ; la mère écrit si
  GO-2026-11-18-03 (1) la couvre déjà.

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
2. Accord de la mère sous GO-2026-11-18-05, selon R-3170 (8), sur ce brouillon une fois vérifié sans bloquant (§ 1) : TA-1 et
   TA-2 (chaîne v6 hors de la fiche de code, aucune fiche neuve), TA-3 (entropie), TA-4 et TA-5 (épreuve de niveau rejouée), la
   clause d'antériorité de l'épreuve (§ 0, raison de TA-4 et TA-5), la lecture déclarée de la liste d'arrêt (§ 3) et la lecture
   déclarée de la règle de la l. 180 de T pour le tirage des plis internes (§ 5 ; la mère écrit si GO-2026-11-18-03 (1) la couvre
   déjà). Le plafond de prix porté par le lanceur n'est pas couvert par cet accord seul : porté à Lazar par la mère, en réserve
   au verdict tant que Lazar ne l'a pas dit (§ 1).
3. Les empreintes du § 6 se relisent au commit où la mère dépose les pièces ; le compte d'essais se remesure à ce commit.
4. Le verdict de l'étape B bis cite la ligne `ADDENDUM-ECART-3-BBIS`, comme les deux premières.
5. Le feu (version 4) nomme : amorce v6 et ses 64 caractères d'empreinte, lanceur v6, branche de code `main`, commit de la
   course, image, deux relances.

## 8. Fichiers à donner au contre-lecteur (R2)

Lecture seule : ce brouillon ; `scripts/amorce_bbis_v6.sh`, `scripts/lancer_bbis_v6.sh` et leurs différences avec la v5
(`diff scripts/amorce_bbis_v5.sh scripts/amorce_bbis_v6.sh`, de même pour le lanceur) et avec la v4
(`brouillons/T0.7-etape-B-bis-v1/preuve-addendum-3-brouillon2-v1/diff-amorce-v4-v6.txt` et `diff-lanceur-v4-v6.txt`) ;
`tests/test_chaine_bbis_v6_v1.py` ;
`brouillons/T0.7-etape-B-bis-v1/preuve-amorce-v6-v1/` ; T, A1, A2 ; `src/controle_ia/t07bbis/marche_v4.py` (garde d'entrée),
`lecture_v3.py` (`lire_lignes`), `registre_bbis_v2.py` ; `registres/t07-etape-b-bis-v1.md` et les deux fiches de code ;
`docs/notes/prealables-course-etape-b-bis-v1/` (rapport et contre-lecture du projet de feu ; les quatre contre-lectures de la
v6 ; leur arbitrage `arbitrage-contre-lecture-amorce-v6-v1.md`, `688abea5…` ; la vérification du brouillon 2,
`verification-addendum-3-brouillon2-v1.md`, `c320d50e…`) ; `registres/go.md`, lignes GO-2026-11-14-09, GO-2026-11-16-11,
GO-2026-11-18-03, GO-2026-11-18-04, GO-2026-11-18-05 ; `registres/decisions.md`, lignes R-3146, R-3149, R-3160, R-3162,
R-3170, R-3188. Questions : chaque « ancien » est-il exact et unique ; la v6 fait-elle ce que ce texte dit et rien d'autre ; une garde
neuve peut-elle arrêter une course saine sur la machine payée ; les onze motifs ouvrent-ils autre chose que les onze fichiers ;
reste-t-il un arrêt certain entre le démarrage et la marche. Interdits : rien sous `diag/`, `runs/`, `donnees/` ; aucune branche
de données ; aucune valeur de clé ; ni `env`, ni `printenv` ; aucune machine, aucun appel au loueur.
