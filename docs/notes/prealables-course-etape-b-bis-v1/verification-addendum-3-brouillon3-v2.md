# Vérification du brouillon 3 du troisième addendum d'écart de la course de l'étape B bis (apprentissage des sondes sur la tâche, T0.7) — v2

- **Version 2** : remplace la version 1 (`verification-addendum-3-brouillon3-v1.md`,
  `a0d1e80af29528a6598a1246f5d1c46b954fc5603de2c4a521cb2887d9fb772c`, gardée, règle R12), scellée une minute plus tôt par le même
  vérificateur avec un compte faux : « 19 blocs » de `diff` au lieu de 20. Seuls changent ce compte, le numéro de version et
  ce paragraphe ; le verdict et les points sont les mêmes.
- **Vérificateur** : sous-agent neuf (règle R2). Je n'ai écrit ni l'addendum, ni aucun de ses trois brouillons, ni les quatre
  contre-lectures de la chaîne de lancement version 6, ni leur arbitrage, ni la vérification du brouillon 2, ni aucune pièce de
  la chaîne.
- **Date (UTC, `date -u`)** : 2026-11-18, de 05:40Z à 05:50Z environ. Commit lu : `597157bbdb3ece1af7e7bd66eb294b6d559f2fce`
  (le brouillon 3, son dossier de preuve et la vérification du brouillon 2 n'y sont pas encore versés : lus sur le disque).
- **Pièce vérifiée** : `brouillons/T0.7-etape-B-bis-v1/addendum-ecart-3-brouillon3.md`,
  `858b7aca32f206e44beb2c07c38f0af279c28a26f3e476a69b905dce32c91895` (recalculée, égale à son compagnon).
- **Contre quoi** : la vérification du brouillon 2,
  `docs/notes/prealables-course-etape-b-bis-v1/verification-addendum-3-brouillon2-v1.md`
  (`c320d50e2a9f80f1c5a260dc71f8025790bd8149e853960d34d01ae7af33431b`, un majeur et sept mineurs) ; le brouillon 2
  (`a57895d42d002f99a1278e76c88ee9034a5fd12c31eb6711dde4ab90826f42e1`, intact) ; l'arbitrage
  `arbitrage-contre-lecture-amorce-v6-v1.md` (`688abea5965a872b646148538f979be9dfd90d687c8eb73185eb092bcac150e3`, lu en entier) et
  les quatre contre-lectures qu'il arbitre (« gardes » `779ed714…`, « conformité » `84abdb49…`, « machine » `ddca4e7c…`,
  « adverse » `1e7bd8ef…`, lues en entier, toutes conformes à leurs compagnons) ; `registres/decisions.md`, lignes R-3160,
  R-3170, R-3185, R-3188 ; `registres/go.md`, lignes GO-2026-11-18-03, -04, -05 ; le texte scellé
  `prereg/T0.7-etape-B-bis-v1.md` (`0ae6210f…`) aux l. 5, 93, 116, 180, 227 ; le second addendum (`18baeac3…`) aux l. 142, 305,
  500 à 509, 527, 546-547.
- **Cloisonnement tenu** : rien d'ouvert sous `diag/`, `runs/` ni `donnees/` ; aucune branche de données ni de calcul ; aucun
  résultat de 7a, de 7b, de T0.6, de l'étape B, de l'étape B bis ni du premier test boîte blanche bis. Du registre partagé des
  sceaux, je n'ai extrait par motif que la clé et l'heure de la ligne `VERDICT-T07-ETAPE-B`. De la ligne 482 du registre des
  dépenses, je n'ai extrait par motif que les dates, les montants et le cumul. Des deux fiches de code : l'entropie, le niveau
  retenu, le chemin de l'épreuve. Aucune dépense, aucun appel au loueur ni à l'hébergeur, aucune clé lue, aucun commit, aucune
  poussée. Aucun clone. Les quatre artefacts ont été joués sur des copies des six textes (quelques centaines de kilo-octets) dans
  `/tmp/claude-0/-home-user-controle-ia-travail/8282ab93-0983-5813-b791-a7a522157dcd/scratchpad/verif-b3/`, dossier supprimé.
  Seuls fichiers écrits dans le dépôt : ce rapport et son compagnon.

## Verdict : « scellable »

Le majeur et les sept mineurs de la vérification du brouillon 2 sont **tous levés**, chacun à l'endroit demandé, avec des
chiffres et des citations que j'ai revérifiés. La différence du brouillon 2 au brouillon 3 ne contient **rien d'autre** que ces
corrections et les changements de numéro. Aucun seuil, critère de lecture, hypothèse ni ligne de la liste d'arrêt n'est touché.
Toutes les empreintes sont exactes. Les cinq passages remplacés sont uniques. **Aucun bloquant, aucun majeur, aucune correction
exigée.**

Je laisse cinq remarques de forme, **non exigées** (un mot ou une ligne chacune). Aucune ne change le sens ni ne cache un écart.
Si la mère les porte au moment de sceller, elles se contrôlent par un simple `diff`, sans nouvelle vérification de fond.

## Les huit points de la vérification du brouillon 2, un par un

| point | demandé | fait ? | ma vérification |
|---|---|---|---|
| **M1** — tirage des plis internes et règle de la liste d'arrêt, l. 180 | réécrire la dernière phrase du § 5 ; déclarer la lecture ; reporter au § 1 et au § 7, point 2 | **oui** (§ 5, l. 327-337 ; § 1, l. 78-79 ; § 7, point 2) | Texte scellé, l. 116 : « une graine par clé (`bbis/interne/<pli>` […]) ; les plis externes prennent la graine `partition-taches` de 7b ». Texte scellé, l. 180 : citée mot pour mot par le brouillon. Code : `marche_v4.py`, l. 60 (`CLES_FIXES` avec `bbis/interne/e0` et `e1`), l. 287 (`Graines(int(entropie), reelle=reelle)`), l. 363 (plis externes par la graine de 7b) : exacts. Seconde ligne `CODE-BBIS` à 2026-11-17T11:05:29Z, après la marche du 16 novembre. Le brouillon ne tranche pas si GO-2026-11-18-03 (1) couvre la lecture : il le laisse à la mère, aux trois endroits, comme demandé. La phrase de plus sur « **plis** externes et internes » (second addendum, l. 509, sous « Inchangés ») reste dans le lieu que M1 nommait ; elle est juste. |
| **m1** — bloquant de machine | dire qu'il se lève au feu version 4 ; « l'accord ne vaut pas feu » | **oui** (§ 1, l. 73-75) | Renvoi au § 4, point 9, qui porte bien la condition de pilote de série 595 ou 580. |
| **m2** — plafond de prix au lanceur | le sortir de l'accord de la mère seul ; porté à Lazar ; réserve au verdict | **oui** (§ 1, l. 79-83 et l. 91-93 ; § 3, l. 276-277 ; § 7, point 2) | Les trois citations sont exactes à la lettre dans `registres/go.md` : « tout ce qu'un mot exprès de Lazar a déjà tranché autrement » (GO-2026-11-18-05) ; « tenu hors du code » et « le verdict dira que ce plafond tenait à un opérateur et non au code » (GO-2026-11-18-03 (3)). Le plafond ne figure plus dans la liste de ce que l'accord nomme. |
| **m3** — les deux autres membres de la l. 93 | nommer « avant toute marche » et « avant toute exécution » | **oui** (l. 236-239) | Texte scellé, l. 93 : les deux membres y sont. Le brouillon déclare plutôt trop que pas assez (remarque 3). |
| **m4** — « n'est plus dans le dépôt » | « est absente du dépôt (disque et index ; histoire non vérifiée) » ; retirer « non vérifié par moi » pour ce membre | **oui** (TA-4, « nouveau » ; raison, l. 226-228) | Revérifié (règle R11) : `registres/t07-etape-b-bis/epreuve-niveau-deux-plis-bbis-v1.json` absent du disque et de l'index ; `git log --all` sur son chemin ne rend rien ; dépôt local superficiel (142 commits). La première fiche cite bien ce chemin. « Non vérifié par moi » ne garde que la raison du changement d'entropie. |
| **m5** — préséance | « le code neuf que la fiche cite (63 fichiers) » | **oui** (§ 0, l. 53-54) | — |
| **m6** — heure du brouillon 2 | l'heure réelle | **oui** (en-tête, l. 19-20) | Le fichier du brouillon 2 porte 05:20 sur le disque. Voir la remarque 1 pour l'heure du brouillon 3. |
| **m7** — § 8, raison de TA-3, deux mineurs de la contre-lecture « conformité » | nommer les pièces au § 8 ; réécrire la phrase sur le niveau ; l'essai qui saute ; la coupure | **oui** (§ 8 ; l. 187-188 ; § 3, l. 268-271 et l. 253-256) | § 8 : les quatre contre-lectures, l'arbitrage, la vérification, GO-2026-11-18-05, R-3170, R-3188 et les deux différences de la version 4 à la version 6 y sont. Essai : `tests/test_t07bbis_second_addendum_v1.py`, l. 482-488, message « chaîne de T0.6 absente de ce clone » ; la preuve de la version 6 le montre bien sauté sur l'arbre extrait (`essais-arbre-extrait-candidat.txt`, l. 38) ; second addendum, l. 527 : « 34 essais » ; c'est bien le mineur m4 de la contre-lecture « conformité ». Coupure : registre des dépenses, l. 482, « cumul de la ligne ≈ 6,0 sur 40 (répétitions 0,749, première création 0,10) » et 5,14 ; 0,749 + 0,10 + 5,14 = 5,989 ; 40 − 5,99 ≈ 34. |

## Rien d'autre n'a bougé

`diff` du brouillon 2 au brouillon 3, rejoué : 20 blocs. La pièce versée
`preuve-addendum-3-brouillon3-v1/diff-brouillon2-brouillon3.txt` (`1b09050f…`) est égale à mon `diff -u`, hors les deux lignes
d'en-tête. Chaque bloc se rattache à l'un des huit points ou au changement de numéro :

- titre, paragraphe « Brouillon 3 », date, statut, lectures faites pour le brouillon 3 (en-tête) : numéro et m6 ;
- § 0 : les trois pièces de preuve du brouillon 3 à la place de celles du brouillon 2 ; m5 ;
- § 1 : « ce brouillon 3 » ; m1 ; M1 ; m2 (deux endroits) ;
- raison de TA-3 : m7 ; « nouveau » de TA-4 et raison : m4 ; clause d'antériorité : m3 ;
- § 3 : m7 (coupure ; essai qui saute) ; m2 ;
- § 5 : M1 ; § 7, point 2 : M1 et m2 ; § 8 : m7.

Les « anciens » de TA-1 à TA-5 et les « nouveaux » de TA-1, TA-2, TA-3 et TA-5 sont identiques à ceux du brouillon 2 ; seul le
« nouveau » de TA-4 change (m4). Les § 2 (hors les trois raisons citées), § 4 et § 6 sont inchangés.

## Le brouillon touche-t-il un seuil, un critère, une hypothèse ou la liste d'arrêt ?

**Non.** Par le programme versé, rejoué, et par un contrôle écrit de ma main, indépendant du programme :

- les cinq passages remplacés sont dans le second addendum seulement : le bloc « nouveau » de SA-8 (section « Code neuf » du
  texte scellé), le § 5 deux fois, le § 7 deux fois ;
- les 24 blocs SA autres que SA-8 sont inchangés, dont SA-4, SA-5, SA-15 et SA-19 ; les deux phrases de la liste d'arrêt
  (« sous ce texte et ses deux addenda », « sous le second addendum ») figurent une fois avant et une fois après ;
- le second addendum lu avec les cinq remplacements ne diffère de l'original que sur 12 lignes de `diff`, toutes dans ces
  passages ; il est égal, hors sa première ligne de commentaire, à la pièce de travail versée (`0f9c6765…`) ;
- le niveau décisif retenu est 0,99 dans les deux fiches.

Quatre lectures sont déclarées sans changer la lettre : la clause d'antériorité de « Seuil » (l. 93, trois membres) ; les deux
phrases de la liste d'arrêt (SA-5, SA-15) ; la préséance sur l'en-tête ; la règle de la l. 180 pour le tirage des plis internes,
avec la même lecture pour la l. 509 du second addendum. La quatrième est celle qui manquait au brouillon 2.

## Empreintes (toutes recalculées sur le disque)

- Les **20 empreintes de 64 caractères** du brouillon 3 : 19 correspondent chacune à un fichier présent (texte scellé, deux
  addenda, brouillons 1 et 2, arbitrage, vérification du brouillon 2, programme, sortie et pièce de travail du brouillon 3, deux
  différences de la version 4 à la version 6, amorces et lanceurs des versions 4 et 6, essais de la version 6, fiche en
  vigueur, épreuve rejouée). La vingtième, `641adeb5…9cbf`, est celle que la première fiche donne à l'épreuve absente.
- Les **empreintes courtes** : chacune est le début d'une empreinte de fichier présent (`ee362bb7`, `4b28535c`, `da9fa42b`,
  `688abea5`, `c320d50e`, `ca070374`, `83460ade`, `d48e74d3`, `8cbe0bc6`, `52d6f5c8`, `a3be1198`, `43298cc4`), d'un commit
  présent (`05cd22aa`, `8d88c812`, `03af21a3`, `d75587c8`, `c098fb51`), ou figure dans la première fiche (`641adeb5`).
- Compagnons : le brouillon 3, les quatre pièces du dossier `preuve-addendum-3-brouillon3-v1/`, les six du dossier
  `preuve-addendum-3-brouillon2-v1/`, les brouillons 1 et 2, et les dix notes du dossier des préalables sont conformes.
- Heures : commit `d75587c8` à 2026-11-17T11:03:40Z ; commit `c098fb51` à 11:07:47Z ; clé `VERDICT-T07-ETAPE-B` à
  2026-11-17T11:20:08Z. Les deux entropies sont celles des deux fiches.

## Unicité des « anciens » (programme versé, rejoué ; contrôle indépendant ; artefacts rejoués)

- `python brouillons/T0.7-etape-B-bis-v1/preuve-addendum-3-brouillon3-v1/controle-fragments-addendum-3-brouillon3-v1.py`, joué
  depuis la racine : **code 0, « CONFORME »**, sortie identique ligne pour ligne à la partie « cas sain » de la sortie versée
  (`d8760540…`) ; la pièce de travail existe et est identique, rien n'a été réécrit.
- Le programme ne diffère de celui du brouillon 2 que par le brouillon lu, l'empreinte exigée du brouillon 2, le nom de la pièce
  de travail et le mot « n'est plus dans le dépôt » dont l'absence est exigée (`diff` des deux programmes lu en entier).
- Contrôle de ma main : chaque « ancien » figure une fois dans le second addendum, zéro fois dans le texte scellé et dans le
  premier addendum ; aucun chevauchement.
- **Artefacts (règle R5), rejoués par moi sur des copies jetables**, tous refusés avec le code 1 : chevauchement de TA-2 et
  TA-5 ; « ancien » de TA-4 pris dans la liste d'arrêt (« recouvre les blocs ['SA-15'] ») ; « ancien » présent aussi dans le
  texte scellé (« trouvé 19 fois dans A2, 19 dans T, 7 dans A1 ») ; « n'est plus dans le dépôt » rétabli. Trois de ces quatre
  sont ceux de la sortie versée ; le troisième est de moi.
- **Limite du programme**, inchangée : il n'exige pas l'empreinte du brouillon 3 lui-même (c'est la pièce qu'il contrôle) ; pour
  un passage hors d'un bloc SA, il ne vérifie que le numéro de la section du second addendum (5 ou 7), ce qui suffit ici.

## Remarques de forme, non exigées

1. **Heure du brouillon 3 (en-tête, l. 20).** « de 05:30Z à 05:45Z environ » : le fichier porte 05:39 sur le disque, et la
   vérification du brouillon 2, dont il part, porte 05:33. C'est le défaut que m6 corrigeait pour le brouillon 2, en plus petit.
   À écrire avec la ligne de statut au scellement : « achevé à 05:39Z (heure du fichier sur le disque) ».
2. **Deux citations entre guillemets qui ne sont pas à la lettre.** L. 237 : « inscrit avec la ligne `CODE-BBIS`, avant toute
   marche » ; le texte scellé, l. 93, dit « inscrite ». L. 255-256 : « au reste de la ligne (≈ 34 USD) » ; GO-2026-11-18-03 et
   R-3170 (8) disent « au reste de la ligne GO-2026-11-14-09 (≈ 34 USD) ». Mettre « inscrite » et « […] ».
3. **Membre « avant toute marche » (l. 236-239).** Dans le texte scellé, ce membre est attaché au cas où le niveau passerait à
   99,5 %, cas qui ne s'est pas produit. Le brouillon le déclare « non tenu à la lettre » pour le niveau retenu, 0,99 : il
   déclare donc plus que la lettre n'exige. C'est du côté sûr ; je ne demande rien.
4. **§ 3, « plan d'analyse (plis, grille, […]) » sous « Inchangés » (l. 247).** La phrase est juste (la règle des plis ne change
   pas), mais elle garde le mot nu que M1 a fait préciser au § 5. Un renvoi suffirait : « plis : règle ; tirage des plis
   internes, voir § 5 ».
5. **Lecture de la l. 509 du second addendum.** Elle est déclarée au § 5, mais le § 1 et le § 7, point 2, ne nomment que la
   lecture de la l. 180. Le renvoi au § 5 la porte ; il serait plus net que l'accord de la mère nomme les deux.

Au scellement, comme pour le second addendum, la ligne de statut change (« version 1, scellée […] »), ainsi que les mentions
« L'accord n'est pas encore donné » (§ 1) et les points 1 et 2 du § 7, s'ils sont alors remplis. Ce sont des gestes de la mère,
hors de mon objet.

## Les deux questions laissées à la mère

- **GO-2026-11-18-03 (1) couvre-t-il déjà la lecture de M1 ?** Je ne tranche pas. Fait utile : la ligne ne nomme que « l'écart
  d'entropie des graines » ; elle ne nomme ni les plis, ni la règle de la l. 180, ni la l. 509 du second addendum. Le nouveau
  tirage des plis internes est une conséquence mécanique de cet écart (texte scellé, point 12), mais la lecture d'une règle de la
  liste d'arrêt n'y est pas écrite. Le plus sûr est que l'accord de la mère la nomme en propre et que son compte rendu à Lazar
  la cite.
- **Faut-il une vérification de plus avant l'accord ?** Celle-ci la tient. Si la mère scelle le brouillon 3 tel quel, ou avec
  les seules remarques 1, 2, 4 et 5 et la ligne de statut, un `diff` contre `858b7aca…` et un rejeu du programme suffisent.

## Limites

- Je n'ai pas relu les deux scripts de la version 6 ni rejoué leurs essais : les quatre contre-lectures et l'arbitrage l'ont
  fait. Je n'ai pas revérifié les § 4 et § 6 du brouillon, inchangés depuis le brouillon 2, au-delà de leurs empreintes.
- « N'a jamais tourné sur une machine » (§ 3, l. 269-270) : je m'appuie sur la contre-lecture « conformité » (mineur m4) et sur
  la contre-lecture adverse (limites) ; je ne l'ai pas prouvé moi-même.
- La raison du changement d'entropie reste non vérifiée, comme le brouillon le dit.
- Les mesures du plancher sous Python 3.13 et 3.11 et le feu version 4 (section B de l'arbitrage) ne sont pas dans mon objet.
