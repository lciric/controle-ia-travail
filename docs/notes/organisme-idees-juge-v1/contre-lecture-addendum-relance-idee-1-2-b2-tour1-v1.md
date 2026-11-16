# Contre-lecture (brouillon 2, première lecture du lecteur C) de l'addendum de relance de l'idée 1.2 — v1

- **Pièce relue** : `docs/notes/organisme-idees-juge-v1/addendum-relance-idee-1-2-v1-brouillon2.md`
  (`ab55d5af5d70b340780c33b2bfe4dee15750095540af934530eb74531928d1df`, égale à son compagnon ; 644 lignes, lue en entier).
  Ci-dessous « la pièce » ; **[T]** et **[AE]** comme dans la pièce (`bdabf2bc…790e`, `1b96cf06…beee`, tous deux égaux à leurs
  compagnons sur disque et à `main`).
- **Lecteur** : modèle C, lecteur neuf (R2) ; je n'ai écrit ni la pièce, ni le brouillon 1, ni [T], ni [AE], ni le code, ni le
  rapport du tour 1 (modèle B). Rédacteur des brouillons : modèle A.
- **Dates (UTC, `date -u`)** : 2026-11-16, de 13:13:49Z à 13:22Z.
- **Dépôt** : `main` à la tête `2bf3ddb1` ; la pièce cite les têtes `d4b81652` et `60eee4e5`, toutes deux des commits existants.
- **Verdict : « corrections »** — 1 majeure (en 3 couples), 2 mineures (en 3 couples), plus des remarques facultatives.
  **La conception n'est pas en cause.** Les corrections du tour 1 sont appliquées fidèlement ; la majeure vient d'un fait
  postérieur au tour 1 (R-2979) que la pièce contredit.

## 1. Les corrections du tour 1 : appliquées fidèlement, rien d'autre

Moyens : `diff` brouillon 1 → brouillon 2 ; programme léger (interpréteur du système, `-I -B`) qui tire du § 4 du rapport du tour 1
(`1b73554004a0cfc77b2448dc19f9d204bbe890382bbf19b91efbefa7a71a486f`, égal à son compagnon) les 17 couples exigés, les applique
au brouillon 1 et compare le résultat au brouillon 2.

- Chaque « ancien » figure une fois dans le brouillon 1 (17 sur 17) ; chaque « nouveau » figure une fois dans le brouillon 2,
  sauf m10 (appliqué en substance, voir plus bas). Trois couples (M2, m7-a, m11-a) sont des insertions : leur « ancien »
  reste, comme prévu, dans le brouillon 2.
- Écart résiduel entre « brouillon 1 + les 16 couples + le couple de l'en-tête du rédacteur » et le brouillon 2 : exactement deux
  zones, l'en-tête (version, empreinte du brouillon 1, tête `60eee4e5`, heure 12:58:50Z) et la section « Contre-lecture ».
  Rien d'autre ne change : annexe A, § 1, 3, 4.1 à 4.8 hors couples, intacts. **Conforme.**
- m10 : le « nouveau » du rapport laissait des mots à la mère ; le rédacteur a écrit l'empreinte entière et le traitement.
  Les ajouts (« à la durée de marche de la machine près », « 17 couples exigés ; 3 facultatifs ; F4 à F10 ») reflètent le
  rapport du tour 1 (verdict, annexe A) ; je les ai relus : exacts.
- Les trois couples facultatifs (f1 à f3) et F4 à F10 ne sont pas appliqués, la section « Traitement » le dit ; pas une erreur.
- Annexe A : le programme (`02d193c5…a8de`) et la sortie (`a634334f…8214`) du dossier de travail de la mère, comparés par
  `sha256sum` et par inclusion exacte dans la pièce : **égaux, octet pour octet**. Compagnons du brouillon 2, du programme
  d'assemblage et du rapport du tour 1 : `sha256sum -c` OK.

## 2. Vérifications demandées

1. **Corrections du tour 1** : voir § 1. Conforme.
2. **Cause et qualification « run invalide »** : conformes. [T] l. 512 (« exception, log W non fini | arrêt du run ; aucune
   lecture partielle ; relance seulement sous un texte ou un addendum neuf (R5) ») et [AE] l. 111-115 sont cités exactement ;
   [T] n'a, par recherche de mots (interromp-, conteneur, redémarr-, relanc-, invalide), aucune ligne propre à un arrêt de
   l'extérieur : la pièce le dit et range sous la ligne la plus stricte, sans prétendre à un écart. Arithmétique vérifiée :
   00:29:50Z → 04:36Z = 4 h 06 ; 01:22:37Z → 04:36Z = 3 h 13 ; 01:22:37Z → 06:13Z = 4 h 50 ; « 2,3 à 4,7 h » = [AE] l. 136.
   La lecture de la nuit (journaux de session arrêtés à 04:36:02Z, deux sorties de 10 octets à 02:31:14Z et 04:31:41Z, soit
   2 h 00 min 27 s d'écart) concorde avec les relevés de l'annexe B du tour 1 ; je ne l'ai pas rouverte au-delà de ce rapport.
3. **« Mêmes tirages »** : confirmé par le code. La racine est `int(EMPREINTE_PREREG, 16)` (constante, `banc_tirages_repartis_v1.py`
   l. 37, 61-64) ; chaque tirage vient de `SeedSequence(entropy=racine, spawn_key=clé)` avec les clés fixes de [T] l. 451-456 ;
   le banc de mutations reçoit la même racine (lanceur l. 146) ; ses sources de hasard propres sont fixes (`default_rng(5)`,
   `sha256` d'un objet d'essai). Par recherche dans `banc_tirages_repartis_v1.py`, `rejeu_v1.py`, `execution_v1.py`,
   `execution_v2.py`, `mutations_v1.py` : aucun `default_rng()` sans graine, aucun module `random`, aucune lecture de PID ni
   d'horloge qui alimente un tirage ; l'horloge ne sert qu'aux durées et au nom du run. Nom du run (lanceur l. 132), PID,
   commit, addendum : absents des graines. Conséquence pour R3 : écrite (§ 2 et § 4.2 : « aucune seconde chance sur un
   autre tirage »). Réserve déjà déclarée par la pièce : « au bit près » demande la même version de numpy ; le contrôle des
   versions rend, rejoué par moi, `3.13.18 2.4.6 1.17.1` (conforme à l'annexe A, [5]). L'interpréteur du run invalide est
   inféré « par élimination » parmi sept relevés : la pièce le dit.
4. **Conditions de la relance** : conformes, sous réserve de la majeure M1 plus bas.
   - Mêmes fichiers gelés : la liste de [AE] compte 34 lignes au format du lanceur ; `gardes.py`, `scellement.py`, `manifeste.py`
     y figurent ; aucune modification de `gardes.py`, `manifeste.py`, `scellement.py`, `__init__.py` entre `2753ecf2` et `main`.
   - Copie propre neuve, commit noté, PID noté, commande de [AE] avec l'interpréteur nommé par son chemin (le lanceur emploie
     `sys.executable` pour ses essais : pas de dérive d'interpréteur) ; `--addendum` pointé sur [AE] ; la pièce ne contient
     **aucune** ligne au format du lanceur : `grep -cE '^[0-9a-f]{64}  \S+\s*$'` = 0 (rejoué), et le lanceur, passé cette pièce,
     refuserait (« fichiers gelés absents de la liste », `execution_v1.py` l. 112-114). Le lanceur ne contrôle pas la présence
     de l'addendum de relance dans la copie : la pièce le dit (4.4, 4.6) et exige la vérification de l'opérateur.
   - Borne de 24 heures : comptée depuis le lancement du run neuf, l'horloge du lanceur étant créée au début de `jeu_decisif`
     (l. 130), donc essais d'avant jeu compris ; la pièce l'écrit (4.7, 4.10).
   - Espace disque : `df` à 13:18Z = 7,3 Go disponibles (cohérent avec les relevés de la pièce) ; seuil de 1 Go après copie.
   - Tests du mécanisme d'attente (voir § 3) : `timeout … tail --pid=<PID> -f /dev/null` rend 124 à l'expiration, 0 à la fin du
     processus **et aussi 0 si le PID n'existe plus** ; la pièce l'a prévu (« la suite ne cesse qu'après la fin du parent :
     `journal.json` ou `arret.json` écrit, ou parent disparu »).
5. **Consigne d'opérateur et seconde interruption** : la consigne (M1 du tour 1, décision (vi)) est écrite avec ses limites
   déclarées (limite d'usage, reprise malgré une tâche active, panne). Une imprécision sur la portée de « seconde interruption » :
   voir m1.
6. **Sort des fichiers du run invalide** : voie (a) écrite comme décision de la mère (R-2973 : « retenue par la mère » vérifié
   par `grep`), avec ses conditions, y compris `GIT_OPTIONAL_LOCKS=0` pour toute lecture git dans la copie, et l'incident du
   verrou d'index déclaré (dossier `.git` de la copie : heure de modification 12:06:35Z, **inchangée à 13:16Z par `stat`**,
   donc rien d'autre ne l'a touché depuis). Conforme.
7. **Rien ne change un critère, un seuil, une graine ni le plan** : confirmé ; § 1 de la pièce, 4.7 et 4.9 le disent, et le
   différentiel n'y touche pas.
8. **Empreintes citées** : recalculées par `sha256sum` ou `git show … | sha256sum` — [T], [AE], brouillons 1 et 2, rapport du
   tour 1, programme et sortie de l'annexe A, `registres/decisions.md` (`7025e985…`) et `registres/go.md` (`b46dcde2…`) à la tête
   `d4b81652` : toutes **exactes**. Les têtes `d4b81652`, `60eee4e5`, `1332acb3`, `2753ecf2` existent. Aucun identifiant de modèle
   dans la pièce (recherche de mots sur les noms de modèles : vide). Section « Contre-lecture » remplie (rapport du tour 1,
   empreinte entière, verdict, réponse point par point) ; ses lignes « 17 couples, 3 facultatifs, F4 à F10 » sont exactes. Une
   ligne reste à écrire par la mère : mon propre tour (voir § 5).

## 3. Corrections exigées

Les couples « ancien → nouveau » sont exacts ; chaque « ancien » a été éprouvé comme figurant une seule fois dans le brouillon 2
(octets identiques, sans espace insécable).

### Majeure

**M1** — **la pièce fixe un ordre de lancement que R-2979 contredit** (§ 4.10 et § 4.9). R-2979 (`registres/decisions.md`,
2026-11-16 12:47Z) écrit que l'étape 0 v5 de l'idée 1.1 est lancée à 12:45:53Z sur « deux processus (le jeu de l'idée 1.2 doit
tourner à côté) », à `nice 10` ; la décision (v) de la mère dit la même chose (jeu de l'idée 1.2 en même temps que des travaux
de l'idée 1.1, dont l'étape 0 v5 ; le jeu de l'idée 1.1 « viendra ensuite »). La pièce, elle, écrit « le run neuf ne part pas
pendant l'étape 0 de l'idée 1.1 » (puce « ordre » de 4.10) et renvoie à R-2964 (4.9), qui disait « relance après l'étape 0 »
**avant** R-2979. Scellée ainsi, la pièce interdirait le lancement que la mère a prévu ; le passer serait un écart à un
addendum scellé (un nœud de Lazar). La pièce ne cite pas R-2979 et décrit 4.10 comme concurrence avec « le jeu de l'idée 1.1 »
seulement. Trois couples ; ils rendent l'ordre libre et laissent le choix du moment à la mère, sans l'orienter.

**M1-a** (4.10, premier alinéa)

Ancien :

```text
**4.10 Machine partagée avec le jeu de l'idée 1.1 (décision de la mère).** Le run neuf tournera en même temps que le jeu
de l'idée 1.1, sur la même machine à 4 processeurs logiques : deux processus de calcul pour l'idée 1.2 (4.6), trois au
plus pour l'idée 1.1 (son texte scellé, étape 3), tous à `nice -n 10`.
```

Nouveau :

```text
**4.10 Machine partagée avec les travaux de l'idée 1.1 (décision de la mère).** Le run neuf tournera en même temps que
des travaux de l'idée 1.1 (l'étape 0 v5, deux processus de calcul depuis 12:45:53Z, R-2979 ; puis son jeu), sur la même
machine à 4 processeurs logiques : deux processus de calcul pour l'idée 1.2 (4.6), deux pour l'étape 0 v5, trois au plus
pour le jeu de l'idée 1.1 (son texte scellé, étape 3), tous à `nice -n 10`.
```

**M1-b** (4.10, puce « ordre »)

Ancien :

```text
- **ordre** : le run neuf ne part pas pendant l'étape 0 de l'idée 1.1, dont le chronométrage est sensible à la charge
  (R-2964 : relance après elle).
```

Nouveau :

```text
- **ordre** : R-2964 prévoyait la relance après l'étape 0 de l'idée 1.1 ; R-2979 a ensuite lancé l'étape 0 v5 (12:45:53Z,
  deux processus de calcul) en notant que le jeu de l'idée 1.2 doit tourner à côté. Cet addendum permet les deux ordres et
  n'en impose aucun : le run neuf peut partir pendant l'étape 0 v5 (quatre processus de calcul pour quatre processeurs
  logiques, avant l'arrivée du jeu de l'idée 1.1) ou après elle ; le moment relève de la mère et se consigne au registre ;
  il n'entre dans aucune graine (4.2) ; l'effet de la charge sur l'étape 0 relève du texte de l'idée 1.1.
```

**M1-c** (4.9, dernière phrase)

Ancien :

```text
Le moment du lancement relève de la mère (R-2964 : relance après l'étape 0
de l'idée 1.1 ; 4.10).
```

Nouveau :

```text
Le moment du lancement relève de la mère (R-2964, R-2979 ; 4.10).
```

### Mineures

**m1** — **portée de « seconde interruption » (§ 5)**. La puce dit « Même règle » pour toute seconde interruption ; or la
pièce n'a bâti son raisonnement que pour un arrêt venu de l'extérieur, sans `arret.json` (§ 2, points 3 et 4 ; § 2, dernier
alinéa : « ni une reprise après un défaut constaté, ni une seconde tentative après un essai échoué »). Un arrêt consigné par
une garde du lanceur (essai qui échoue, exception de calcul, durée) est un autre cas : sa cause doit être établie d'abord, et si
un fichier gelé devait changer, il faut un addendum d'empreintes, non un second addendum de relance qui rejouerait un défaut
déterministe. Sans cette précision, « même règle » autorise à relancer à l'identique un jeu qui a échoué par défaut. Deux couples
(reprise de F6 du tour 1, non appliquée).

**m1-a**

Ancien :

```text
- **Seconde interruption.** Même règle
```

Nouveau :

```text
- **Seconde interruption** (arrêt venu de l'extérieur, sans `arret.json`)**.** Même règle
```

**m1-b**

Ancien :

```text
et chaque run invalide est rapporté (§ 4.8).
```

Nouveau :

```text
et chaque run invalide est rapporté (§ 4.8). Un arrêt consigné par le lanceur (`arret.json`) n'est pas une interruption au
  sens de ce paragraphe : il relève de [T] l. 512 avec sa cause établie d'abord (R4, R5), et d'un addendum d'empreintes neuf
  si un fichier gelé devait changer. Après une seconde interruption, une machine qui ne dépende pas de la session serait une
  dépense : devis et GO, à porter à Lazar.
```

**m2** — **« aucune tâche de fond n'est armée ensuite » dépasse ce que les heures montrent (§ 5, Constat)**. Les relevés
(annexe B du tour 1, [B3]) établissent qu'**aucune sortie de tâche de fond n'est écrite** entre 04:31:41Z et 06:20:55Z (après le
redémarrage) ; ils ne disent pas si une tâche était armée sans avoir fini (sa sortie n'est écrite qu'à sa fin). La lecture
« deux attentes menées jusqu'à la limite de l'outil, la seconde non réarmée » reste plausible (deux heures à 27 s près) et concorde
avec la décision (vi), mais elle est donnée dans la pièce comme un fait sur l'armement ; le rédacteur lui-même dit ne pas l'avoir
confirmée sur le journal de la mère (section « Contre-lecture », m5). À réécrire en ce que l'état sur disque établit.

Ancien :

```text
et aucune tâche de fond n'est armée ensuite (lecture : deux attentes menées jusqu'à la limite de l'outil, la seconde
  non réarmée)
```

Nouveau :

```text
et aucune autre sortie de tâche de fond n'est écrite avant 06:20:55Z, après le redémarrage (lecture, à confirmer sur le
  journal de la mère : deux attentes menées jusqu'à la limite de l'outil, soit deux heures chacune, la seconde non réarmée)
```

## 4. Remarques facultatives (non exigées ; la pièce peut être scellée sans)

- **f-1 — contrôle du zéro ligne sur la copie scellée.** Le lanceur ne refuserait plus l'addendum de relance passé par erreur
  si une ligne au format `empreinte  chemin` s'y glissait. À ajouter à la vérification d'opérateur de 4.4 :
  `grep -cE '^[0-9a-f]{64}  \S+\s*$'` sur la copie sous `prereg/` doit rendre 0 (rendu 0 sur le brouillon 2, rejoué).
- **f-2 — valeur de la durée d'attente.** § 5 : « la durée choisie sous cette limite » ne donne aucun chiffre ; les deux attentes
  de la nuit se sont arrêtées à 2 h pile. Proposer par exemple 1 h 30 donne une marge ; au choix de la mère.
- **f-3 — disque partagé.** 4.4 : le seuil de 1 Go après copie ne prend pas en compte les sorties et la copie du jeu de l'idée 1.1
  qui viendront sur le même disque (7,3 Go disponibles à 13:18Z) ; la précaution reste utile, à relever au lancement.
- **f-4 — annexe A.** Le docstring du programme dit « brouillon 1 » : exact (c'est le programme joué sur le brouillon 1) ; la
  sortie porte la tête `d4b81652` ; la vérification des 34 fichiers est de toute façon refaite par le lanceur.
- **f-5 — F4 à F10 du tour 1** : restent à la mère, comme la pièce le dit ; F5 (deux chaînes d'attentes décalées) est cohérente
  avec la consigne (vi) et sans coût.

## 5. Points pour la mère

1. **M1 d'abord** : décide l'ordre. R-2979 et la décision (v) font coexister le jeu de l'idée 1.2 et l'étape 0 v5 ; la pièce
   interdit cette coexistence. Les trois couples rendent l'ordre libre ; si tu veux au contraire l'ordre séquentiel (relance
   après l'étape 0 v5, ≈ 14:10Z), il faut alors garder la puce de la pièce **et** corriger R-2979 par une ligne neuve.
2. **m5 conditionnel dans la pièce** : la section « Contre-lecture » contient « si le journal de la mère la dément, elle est
   corrigée avant la recopie ». À trancher avant le scellement sous `prereg/` : lis ton journal du 16 novembre entre 02:30Z et
   04:40Z, puis retire la condition (couple m2).
3. **Ligne « Contre-lecture 2 »** à écrire : mon tour (modèle C, lecture entière du brouillon 2, ce rapport et son empreinte,
   verdict « corrections », 1 majeure, 2 mineures) ; et la mention du premier contre-lecteur du modèle B arrêté par une limite
   d'usage vers 13:05Z sans rapport (R-2973 attend la lettre du modèle de chaque lecteur : B pour le tour 1, C pour celui-ci).
4. **Lecture (iv), pas de mot nouveau du directeur** : cohérente avec [T] et [AE] ; elle repose sur une **lecture** de [T] l. 512
   (arrêt de l'extérieur rangé sous cette ligne). Si Lazar la contestait, ce serait un écart ; la pièce le dit au 4.9. Je la tiens
   pour défendable ; c'est ta décision, déjà prise.
5. **Disque et charge** : f-3 ; la machine à 4 cœurs porte déjà l'étape 0 v5 (2 processus), le pilote et les agents ; le plafond
   « cinq processus de calcul » de 4.10 suppose que le jeu de l'idée 1.1 ne part pas avant la fin de l'étape 0 v5.
6. **Recopie sous `prereg/`** : après correction, rejouer `sha256sum -c` du texte de relance et du compagnon, puis f-1 ; le
   lanceur ne contrôle pas la présence de l'addendum de relance : l'opérateur la contrôle (déjà exigé par 4.4).
7. **Limite d'usage de la session** : un jeu de ≈ 3,75 à 7,5 h dépasse la limite connue de la session (précédent R-1463, cinq
   heures) ; la pièce la déclare parmi ce que la consigne n'exclut pas ; rien ne la couvre ; à garder en tête pour le choix de
   la session qui lance.

## 6. Incidents et gestes de ma main

- **Un `git status --short` dans le dépôt principal** (vers 13:15Z), sans `--no-optional-locks` : verrou d'index facultatif posé puis
  retiré ; aucun effet relevé. Mes autres commandes git ont lu des objets (`rev-parse`, `cat-file`, `show`, `log`, `grep` de
  fichiers suivis) dans le dépôt principal ; **aucune commande git dans `/home/user/jeu-idee-1-2-copie`** : j'y ai seulement
  lancé `stat` sur son dossier `.git` (heure 12:06:35Z inchangée).
- **Aucun fichier du run invalide ouvert** ; leurs octets ne sont pas passés par mes commandes (je me suis fié aux empreintes
  de la pièce, pas rejouées).
- **Fichiers du dossier de travail de la mère** (`…/scratchpad/relance-1-2/`, programme et sortie de l'annexe A) : lus et
  comparés à la pièce, empreintes calculées ; rien d'autre n'y a été touché. **Dossiers d'autres agents du bloc-notes** : seuls
  leurs noms sont apparus dans le résultat d'un `find` ; non ouverts, non lus.
- **Commandes lourdes** : aucune. Légères : `diff`, `sha256sum`, petits programmes d'inclusion, `-I -B`, le contrôle des
  versions (une fois), `uptime`, `df`, essais de 2 s et 1 s de `timeout`/`tail --pid` (sur mon propre shell et un `sleep` de
  1 s à moi), `stat`. Fichiers de travail à moi dans mon dossier du bloc-notes (`chk.py`, `chk2.py`, `chk3.py`).
- **Rien d'autre** : aucun processus arrêté, aucun commit, aucune poussée, aucune valeur de clé, aucun appel réseau, aucun
  fichier existant modifié.
