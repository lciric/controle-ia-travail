# Addendum de relance au préenregistrement de l'idée 1.2 (tirages répartis par blocs avec arrêt anticipé) — v1

- **Texte auquel il s'ajoute** : `prereg/organisme-idee-1-2-tirages-repartis-arret-anticipe-v4.md`
  (`bdabf2bc9b2c9b78939660f7f7053576a145e165927cafd23e14a798d07d790e`), ci-dessous **[T]**, lignes citées « l. n ».
- **Addendum qu'il complète, sans le remplacer** : `prereg/organisme-idee-1-2-tirages-repartis-arret-anticipe-v4-addendum-empreintes-v1.md`
  (`1b96cf065cef40ed9e452611b107d9f40f598091c8a591f2397bf58e7c92beee`), ci-dessous **[AE]**.
- **Ce qui l'exige** : [T] l. 512, « exception, log W non fini | arrêt du run ; aucune lecture partielle ; relance seulement
  sous un texte ou un addendum neuf (R5) » ; [AE] l. 111-115, consigne d'opérateur : « **run invalide** ; relance seulement
  sous un texte ou un addendum neuf ([T] l. 512) ».
- **Rédacteur** : auteur neuf, sous-agent de la session mère ; il n'a écrit ni [T], ni [AE], ni le code, ni aucune de leurs
  relectures, ni aucune autre pièce de l'idée 1.2. **Date (UTC)** : 2026-11-16, de 11:47 à 12:13 (`date -u`) ; programme de
  l'annexe A joué de 12:06:35Z à 12:06:36Z. Dépôt lu sur `main`, tête `d4b81652d936d6d3fd620cd4260d367a0fa83805` ; aucun
  commit, aucune poussée.
- **Version : brouillon 2.** Corrections de la contre-lecture du tour 1 appliquées par un rédacteur neuf, sous-agent de la
  session mère, qui n'a écrit ni le brouillon 1, ni son rapport de contre-lecture, ni [T], ni [AE], ni le code : couples
  « ancien → nouveau » appliqués par le programme
  `docs/notes/organisme-idees-juge-v1/appliquer-corrections-addendum-relance-idee-1-2-v1-brouillon2.py` (scellé à côté)
  au brouillon 1 (`26aa0713419ecff1cbb2cd4240e17dfdc0aea9902e66e4f2c9020560ed50fdd3`) ; dépôt lu sur `main`, tête `60eee4e551fa8b3adc67278cbb5b9b6b4988ae81` ; heure du scellement
  2026-11-16T12:58:50Z (`date -u`) ; aucun commit, aucune poussée. Rien d'autre que ces corrections, cet en-tête et la section
  « Contre-lecture » n'a changé.
- **Statut et lieu** : rédigé comme brouillon 2, `docs/notes/organisme-idees-juge-v1/addendum-relance-idee-1-2-v1-brouillon2.md`,
  scellé par son compagnon comme pièce de travail (R6) ; il ne fait foi que dans sa recopie sous
  `prereg/organisme-idee-1-2-tirages-repartis-arret-anticipe-v4-addendum-relance-v1.md`, scellée après la contre-lecture
  (décision de la mère). R-2964 l'annonçait comme « addendum de relance v2 » : erreur de plume de la mère, reconnue par
  elle ; second addendum de [T], il est le premier de relance, d'où `-relance-v1` (R12), **nom confirmé par la mère**.
- **Sources des chiffres** : [T] ; [AE] ; les 34 fichiers gelés de [AE] § 1, égaux sur `main` (§ 4.1) ;
  `registres/decisions.md` (`7025e9857afd71a855a29aab3b1726865d3b246b148a3f5baaa6c54fdd05b3c3`) et `registres/go.md`
  (`b46dcde26612137d593100a135e698480034e0eef1f2a62c1d004bc71554b98a`), objets de `main` à la tête citée ; la sortie du
  programme de l'annexe A, programme et sortie recopiés en entier avec leurs empreintes. **Aucun chiffre n'est tiré du
  contenu d'un fichier du run invalide.**

## 1. Pièces complétées, non remplacées

- **[T] fait foi tel quel** : hypothèse, prédictions Q1 à Q9, métrique, seuils, plan d'analyse (banc, familles, bras,
  graines, étapes), comparaisons, critères de lecture, audit de symétrie, liste d'arrêt, coût.
- **[AE] fait foi tel quel** : les 34 fichiers gelés et leurs empreintes (§ 1) ; le lanceur et sa commande (l. 63-64) ; les
  écarts E-1 et E-2, acceptés par Lazar (`registres/go.md` l. 342, GO-2026-11-16-01, point 4 : « écarts E-1 et E-2
  acceptés, jeu sur processeur à lancer ») ; les lectures du texte (§ 3) ; les réserves (§ 4, dont la consigne du fils
  oisif, l. 106-115) ; la machine et la durée attendue (§ 5) ; les essais et mutations (§ 6) ; l'ordre avant le jeu (§ 7).
- **Cet addendum n'en change rien** : ni hypothèse, ni prédiction, ni métrique, ni seuil, ni bras, ni graine, ni étape, ni
  critère, ni ligne de la liste d'arrêt de [T] ; ni fichier gelé, ni empreinte, ni écart, ni réserve de [AE]. Il ajoute la
  qualification du run interrompu (§ 2), l'absence de lecture (§ 3), les conditions de la relance (§ 4), une consigne
  d'opérateur (§ 5) et le sort des fichiers du run invalide (§ 6). Si une phrase d'ici semblait contredire [T] ou [AE],
  [T] puis [AE] l'emportent.

## 2. Le run interrompu : cause, preuves, qualification

**Le run.** `20261116-002954-idee-1-2-tirages-repartis-v1`, lancé le 2026-11-16 à 00:29:50Z par la commande de [AE]
l. 63-64, depuis la copie propre `/home/user/jeu-idee-1-2-copie` au commit `2753ecf295f1226f3e284f14ef194022920b8cc8`,
processus parent de PID 5755 (R-2951, `registres/decisions.md` l. 2911).

**Cause déclarée** (R-2964, l. 2924) : redémarrage du conteneur vers 06:13Z (`/proc/uptime` : 60 s à 06:14:01Z), qui a tué
le jeu sans finir ; selon la mère, le conteneur a été repris pendant une période d'inactivité de la session.

**Preuves sur disque** (annexe A, sections [3] et [4]). Les fichiers ne sont pas ouverts : empreintes vérifiées par
`sha256sum -c` de leurs compagnons, lancé depuis leur dossier dans la copie (conformes tous trois) ; tailles et heures par
`stat`.

| fichier, sous `/home/user/jeu-idee-1-2-copie/` | octets | écrit le 16 novembre (UTC) | empreinte (compagnon) |
|---|---|---|---|
| `runs/20261116-002954-idee-1-2-tirages-repartis-v1/manifeste.json` | 9 489 | 00:38:05 | `93ee47caf273a8f0461afeb2b8e75fcd6587563b0fffb268e5d75b8caa0b44da` |
| `diag/organisme-idees-juge-v1/20261116-002954-idee-1-2-tirages-repartis-v1/controles-avant-jeu.json` | 10 076 | 00:53:28 | `4952a7e3a93ab66e0218048caec6bfe99be832ad063c1131cd6269fb515da7b7` |
| `diag/organisme-idees-juge-v1/20261116-002954-idee-1-2-tirages-repartis-v1/oracle.json` | 13 505 894 | 01:22:37 | `464bd7deb77904b65aec8f983cabafd42c45d82ea9c4457043ff668bcf1524ac` |

- Absents du dossier de sortie : `jeu.json`, `journal.json`, `arret.json`, `lecture-gelee-v2.json`.
- Journal `/home/user/jeu-idee-1-2.log` : 0 octet, dernière modification à 00:29:54Z.
- Copie : tête `2753ecf2…` ; `git status --porcelain --untracked-files=all` y rend exactement ces six fichiers (les trois
  et leurs compagnons), non suivis.
- Aujourd'hui, aucun processus de PID 5755 ; la machine a encore redémarré depuis, vers 11:24:01Z (`/proc/uptime` relevé à
  12:06:35Z, annexe A, [5]).

**Ce que le code gelé dit de cet état** (lecture du code seul ; lignes à l'annexe A, [6]) :

1. Le lanceur n'écrit le manifeste qu'après ses gardes d'avant jeu (`scripts/jouer_idee_1_2_v2.py` l. 133-152 : texte
   scellé et égal, arbre propre, aucune sortie antérieure, 34 fichiers égaux à [AE], copie du juge, constantes du texte,
   essais à code 0, mutations toutes tuées). Sa présence dit seulement qu'aucune de ces gardes n'a arrêté le lanceur.
2. `controles-avant-jeu.json` s'écrit après l'essai E1 et `oracle.json` après l'oracle (`execution_v2.py` l. 158 et 164) ;
   un échec de E1 arrête avant l'oracle (l. 160). Le run avait donc atteint la phase « jeu » (l. 168), qui n'écrit rien
   avant `jeu.json` (l. 176).
3. Dès l'entrée dans l'enchaînement (lanceur l. 160), toute exception, y compris celle que lève le signal TERM (l. 79), est
   attrapée (l. 162-163) et écrit `arret.json`. L'absence de ce fichier est compatible avec un arrêt que le lanceur ne
   peut pas intercepter (fin forcée du processus, arrêt de la machine), donc avec la cause déclarée ; elle n'exclut pas
   qu'une écriture du tout dernier instant n'ait pas atteint le disque.
4. **Limite de la preuve, déclarée.** L'état sur disque ne date pas la fin du processus : rien ne s'écrit entre
   `oracle.json` (01:22:37Z) et `jeu.json`. Il ne distingue pas un processus tué en plein jeu d'un parent resté bloqué
   par la mort d'un fils oisif en fin de phase ([AE] l. 106-115) puis tué avec le conteneur, ni d'une fin forcée plus tôt.
   Le redémarrage de ≈ 06:13Z est celui de la reprise de la session : il ne borne l'instant de l'arrêt que par le haut.
   D'après les seules heures de modification des fichiers de la machine (aucun n'est ouvert ; contre-lecture du tour 1,
   annexe B), la dernière sortie de tâche de fond de la session est écrite à 04:31:41Z, les journaux de la session
   s'arrêtent à 04:36:02Z, et plus rien n'est écrit sur le disque avant 06:13:16Z : le conteneur s'est très
   probablement arrêté vers 04:36Z, ≈ 4 h 06 min après le lancement ; la phase « jeu » durait alors depuis ≈ 3 h 13 min
   (4 h 50 min si l'arrêt n'était venu qu'à 06:13Z), pour 2,3 à 4,7 h attendues sur machine libre et davantage sous
   charge ([AE] l. 136-137). Le jeu n'avait vraisemblablement pas fini ; l'état sur disque ne permet pas de l'affirmer. **La qualification ne dépend pas de cette cause.**

**Qualification : run invalide.** [T] n'a pas de ligne propre à un arrêt imposé de l'extérieur. Cet addendum le range sous
la ligne la plus prudente, [T] l. 512 : arrêt du run, aucune lecture partielle, relance seulement sous un texte ou un
addendum neuf — comme [AE] l. 111-115 pour le parent bloqué, comme le lanceur pour tout arrêt (`execution_v1.py` l. 271,
règle recopiée dans `arret.json`), et comme R-2964. Aucun arrêt par une garde n'est consigné (ni `arret.json`, ni ligne au
journal du lanceur) ; le seul cas que l'état sur disque n'exclut pas est celui du parent bloqué de [AE] l. 106-115
(point 4). La relance n'est ni une reprise après un défaut constaté, ni une seconde tentative après un essai échoué :
aucun résultat n'a été lu (§ 3) et les tirages sont les mêmes (§ 4.2).

## 3. Aucune sortie n'a été lue

- **Par la mère** : « rien lu » (R-2964, l. 2924).
- **Par le rédacteur de ce brouillon** : les trois fichiers n'ont été lus que par `sha256sum -c` (leurs octets passent par
  le calcul de l'empreinte ; rien n'est affiché) ; seuls les noms, tailles et heures des deux dossiers du run ont été
  relevés (`ls`, `stat`), et la taille et l'heure du journal (`stat`). Rien d'autre n'a été ouvert ; rien n'a été lu ni
  écrit sous `diag/` ou `runs/` du dépôt principal. **Incident déclaré** : le `git status` du programme de l'annexe A,
  joué dans la copie sans `--no-optional-locks`, y a posé puis retiré un verrou d'index à 12:06:35Z (heure de
  modification du dossier `.git` de la copie) ; l'index (4 218 874 octets, 00:29:54Z) et l'arbre de travail n'ont pas
  changé. Tout rejeu de ce programme se fait avec `GIT_OPTIONAL_LOCKS=0` (rejeu du contre-lecteur à 12:21:47Z : même
  sortie, dossier `.git` inchangé).
- **Par le lecteur gelé** : impossible ; il refuse une sortie sans `journal.json` scellé, avant de rien charger
  (`lire_banc_tirages_repartis_v2.py` l. 64-69).
- **Limite, déclarée** : les heures d'accès ne prouvent rien. Le disque est monté `relatime` (annexe A, [4]) : la lecture
  que fait le scellement juste après l'écriture a fixé l'heure d'accès à l'instant de l'écriture, et `relatime` ne la met
  à jour que si l'accès précédent est antérieur à la dernière modification, ou ancien. L'absence de lecture repose sur les
  déclarations des agents et sur le code, non sur ces heures.
- **Règle désormais** : personne n'ouvre ces fichiers, ni avant ni après la relance ([T] l. 512, « aucune lecture
  partielle ») ; toute exception serait un écart à [T], donc un nœud de Lazar. Raison de plus : la relance refait les
  mêmes tirages (sous les conditions du § 4.2) ; hors du nom du run, de l'empreinte du manifeste et des durées, le
  contenu de `oracle.json` du run invalide est celui de l'oracle du run neuf ; l'ouvrir avant la lecture gelée du run
  neuf reviendrait à lire avant le scellement de sa sortie ([T] l. 514 : « run invalide »).

## 4. Conditions de la relance

**4.1 Mêmes fichiers gelés.** Vérifié par programme le 2026-11-16 à 12:06Z (annexe A, [1] et [2]) : les 34 lignes de [AE]
§ 1, extraites par l'expression même du lanceur, sont égales sur l'arbre du dépôt, sur les objets de `main` (tête
`d4b81652…`) et sur l'arbre de la copie du run invalide, **34 sur 34** dans les trois cas ; aucune différence entre
`2753ecf2…` et `main` sur ces chemins ; empreinte du bloc des 34 lignes, dans l'ordre de [AE] :
`b6e724a48fa3a57a28819c052ed68fcbd7ce95302283c0fbb5416b2b6fc239d2` ; [T] et [AE] égaux à leurs compagnons et aux objets de
`main` ; liste de la copie du juge égale à l'empreinte que cite [T]
(`0153e02d4522fe21eb1cf52985574eba38b5f260f7a3a08183d63589f29f32df`). Le lanceur refait ce contrôle au départ (l. 139) et
refuse toute différence ([T] l. 506 : « pas de jeu »). Si un fichier gelé change avant la relance, elle ne part pas sous
cet addendum.

**4.2 Mêmes graines, mêmes tirages (R3).** D'après le code gelé (annexe A, [6]) : la racine est l'entier de l'empreinte de
[T] (`banc_tirages_repartis_v1.py` l. 37 et 61-64 ; lanceur l. 145), la même pour tout run de [T] ; chaque tirage vient de
`SeedSequence(entropy=racine, spawn_key=clé)` (l. 67-74), avec les clés fixes de [T] l. 451-456 ; ni le nom du run (heure
du lancement, lanceur l. 132), ni le PID, ni le commit, ni l'addendum n'entrent dans la racine ou dans une clé ; le banc
de mutations et tout l'enchaînement reçoivent cette même racine (lanceur l. 146 et 160). **La relance refait donc
exactement les tirages du run invalide** — mondes, archives, cartes, plans, issues d'entraînement et fraîches,
permutations, hasard du placebo, oracle, jeu synthétique, rééchantillonnages — et n'offre aucune seconde chance sur un
autre tirage. « Exactement », au bit près, demande aussi le même code (4.1) et le même environnement numérique :

- interpréteur `/home/user/controle-ia-travail/.venv/bin/python` : Python 3.13.18, numpy 2.4.6, scipy 1.17.1 (et
  pytest 9.1.1) ; numpy et scipy y sont installés depuis le 2026-11-14 vers 13:43Z, avant le premier lancement (annexe A,
  [5]) ;
- le lanceur importe scipy (l. 48, par `lire_banc_tirages_repartis_v2.py` l. 23 et `lire_banc_tirages_repartis_v1.py`
  l. 20) et joue les essais par pytest ; des sept interpréteurs relevés sur la machine, ce seul-là porte numpy, scipy et
  pytest : le run invalide l'a employé, **par élimination** (son manifeste, qui consigne les versions, n'est pas ouvert) ;
- juste avant le lancement, l'opérateur joue
  `/home/user/controle-ia-travail/.venv/bin/python -I -c "import sys; from importlib import metadata as m; print(sys.version.split()[0], m.version('numpy'), m.version('scipy'))"`
  et doit lire `3.13.18 2.4.6 1.17.1` ; sinon, pas de relance sous cet addendum (une autre version de numpy peut changer
  des tirages de `Generator` ; les états de contrôle que relit le lecteur gelé ne portent que sur `SeedSequence`, non sur
  les lois tirées).

Les sorties ne seront pas identiques à l'octet à celles du run invalide : chacune porte le nom du run et l'empreinte du
manifeste (`execution_v1.py` l. 96), et l'oracle ses durées (`execution_v2.py` l. 116). Comparer les empreintes des deux
runs ne dirait donc rien ; comparer leurs contenus est interdit (§ 3).

**4.3 Run neuf, sous un nom neuf.** Le nom se forme au lancement, `AAAAMMJJ-HHMMSS-idee-1-2-tirages-repartis-v1` (lanceur
l. 132 ; `execution_v1.py` l. 32) ; la création du manifeste refuse un dossier existant (`src/controle_ia/manifeste.py`
l. 78) ; le lanceur refuse de partir si une sortie ou un manifeste de ce jeu existe déjà dans la copie (lanceur l. 135 ;
message, l. 74 : « relance seulement sous un texte ou un addendum neuf »).

**4.4 Copie propre neuve, à un commit noté.** Une copie locale neuve, détachée et propre, d'un commit de `main` qui porte
cet addendum scellé sous `prereg/`, sous un nom neuf (proposé : `/home/user/jeu-idee-1-2-relance-v1-copie`) ; **jamais**
`/home/user/jeu-idee-1-2-copie`, que le lanceur refuserait d'ailleurs (six fichiers non suivis, annexe A, [3] ;
`gardes.py` l. 100 ; lanceur l. 134-135). Avant le lancement, l'opérateur vérifie dans la copie neuve que cet addendum y est, égal à son
compagnon (`sha256sum -c` depuis `prereg/`) : le lanceur ne le contrôle pas (4.6). Le commit, l'empreinte de cet
addendum, la sortie du contrôle des versions (4.2) et l'espace libre sont notés au registre avant le lancement ; le
manifeste consigne le commit.
Journal sous un nom neuf (proposé : `/home/user/jeu-idee-1-2-relance-v1.log`), jamais l'ancien (R12).

**Espace disque (précaution d'opérateur, neuve).** Une copie neuve occupe ≈ 2,8 Go (arbre de travail ; les objets git
sont liés, non recopiés) et l'ancienne copie reste en place (§ 6) ; le disque offert à la session (≈ 39 Go) est passé
par ≈ 0,86 Go libre le 2026-11-16 à 12:39Z, puis ≈ 7,7 Go à 12:46Z, des dossiers de travail ayant été effacés
entre-temps (`df` ; contre-lecture du tour 1, annexe B). Avant de créer la copie, l'opérateur relève et consigne
l'espace libre ; s'il faut de la place, il la libère **ailleurs que dans `/home/user/jeu-idee-1-2-copie`** ; pas de
lancement si, la copie faite, il reste moins de 1 Go libre : un disque plein en cours de jeu lèverait une exception,
donc un run invalide de plus ([T] l. 512). Ce seuil est une précaution, non un critère.

**4.5 PID noté.** Le PID du processus parent est noté au registre dès le lancement ; tout arrêt se fait par ce seul PID
(R10 ; [AE] l. 112-115).

**4.6 Commande.** Celle de [AE] l. 63-64, depuis la racine de la copie neuve, l'interpréteur de 4.2 nommé par son chemin :

`/home/user/controle-ia-travail/.venv/bin/python -I -B scripts/jouer_idee_1_2_v2.py --addendum prereg/organisme-idee-1-2-tirages-repartis-arret-anticipe-v4-addendum-empreintes-v1.md`

(deux processus par défaut). L'argument `--addendum` reste [AE], l'addendum d'empreintes que contrôle le lanceur
(`execution_v1.py`, `verifier_addendum`). Le présent addendum n'en est pas un : il ne contient aucune ligne de la forme
que lit le lanceur (« empreinte, deux espaces, chemin ») ; passé par erreur, il serait refusé avant tout calcul (« fichiers
gelés absents de la liste » : pas de jeu). Le lien entre le run neuf et cet addendum est le commit de la copie, que le
manifeste consigne et qui porte cet addendum.

**4.7 Toutes les règles de [T] inchangées.** En particulier : la borne de 24 heures (l. 513) vaut pour le run neuf, comptée
depuis son propre lancement (horloge du lanceur, l. 130 ; `execution_v1.py` l. 29), et le temps du run invalide n'y entre
pas ; `nice -n 10` et deux processus au plus (l. 473 ; lanceur l. 83) ; oracle scellé avant le rejeu, sortie scellée avant
toute lecture (l. 472, 474 et 514) ; toutes les lignes de la liste d'arrêt (l. 506-515) ; processeur seul, aucune dépense
ni appel de modèle (l. 515 et 519). La consigne du fils oisif de [AE] l. 111-115 vaut telle quelle. Sorties recopiées
octet pour octet dans le dépôt et vérifiées par leurs compagnons avant toute lecture ([AE] l. 66-68) ; lecture gelée v2,
lecteur neuf (R13), audit de symétrie (R4) écrit avant le prononcé ([T] l. 475 ; [AE] § 7).

**4.8 Rapport.** Le rapport du run neuf nomme le run invalide (nom, cause, empreintes du § 2), sans aucun chiffre tiré de
lui, comme l'a été une course interrompue avant (R-1103, l. 1331 : seconde course « rapportée avec la course arrêtée »).

**4.9 Dépense, mot de Lazar, moment.** Aucune dépense ([T] l. 515 et 519). **La relance ne demande pas de mot nouveau
de Lazar (décision de la mère)** : elle ne dépense rien ; les seuls écarts au texte, E-1 et E-2, sont acceptés
(GO-2026-11-16-01, point 4 : « écarts E-1 et E-2 acceptés, jeu sur processeur à lancer », échéance 2026-11-22) ; la
relance sous un addendum neuf est ce que [T] l. 512 prescrit, et [T] ne demande pas de GO neuf (à la différence du texte
scellé d'A1-v3, course à dépense : R-1103) ; cet addendum ne déclare aucun écart. Ranger l'arrêt venu de l'extérieur
sous [T] l. 512 est une lecture du texte, faite du côté le plus strict (§ 2) ; Lazar la trouve au registre (R-2964,
R-2973) et dans le rapport du run neuf (4.8). Le moment du lancement relève de la mère (R-2964 : relance après l'étape 0
de l'idée 1.1 ; 4.10).

**4.10 Machine partagée avec le jeu de l'idée 1.1 (décision de la mère).** Le run neuf tournera en même temps que le jeu
de l'idée 1.1, sur la même machine à 4 processeurs logiques : deux processus de calcul pour l'idée 1.2 (4.6), trois au
plus pour l'idée 1.1 (son texte scellé, étape 3), tous à `nice -n 10`. [T] ne l'interdit pas (l. 473 : deux processus au
plus pour ce jeu) et [AE] § 5 décrivait déjà une machine partagée et chargée : ce n'est ni un écart ni un critère.
Conséquences :

- **tirages et calculs** : aucune ; ni la charge ni le nombre de processus n'entrent dans une graine (4.2) ; seules
  changent les durées consignées dans les sorties ;
- **durée** : jusqu'à cinq processus de calcul de même priorité pour quatre processeurs logiques, soit 4/5 d'un
  processeur chacun au mieux ; chaque phase de calcul prend alors au moins 1,25 fois sa durée sur machine libre (total
  ≈ 3 à 5,5 h selon [AE] l. 137, soit ≈ 3,75 à 6,9 h au moins). La durée dans cette configuration n'a pas été mesurée ; repère :
  ≈ 6 à 7,5 h sous la charge plus forte du jour des mesures de [AE] (charge moyenne de 10 à 13, l. 130-137) ;
- **borne de 24 heures** ([T] l. 513) : inchangée, comptée depuis le lancement du run neuf (4.7) ; sur le repère de
  7,5 h, la marge reste de trois fois environ. Si la borne était franchie, la garde arrêterait le run ([T] l. 513 :
  arrêt, run invalide), sans aucune lecture ;
- **consigne du fils oisif** ([AE] l. 111-115) : elle se lit avec ces durées ; TERM au parent, par son PID, seulement si
  `journal.json` n'est pas écrit à la durée attendue **et** si les processus du run n'emploient plus le processeur ;
- **ordre** : le run neuf ne part pas pendant l'étape 0 de l'idée 1.1, dont le chronométrage est sensible à la charge
  (R-2964 : relance après elle).

## 5. Consigne d'opérateur neuve : une tâche active pendant tout le jeu

- **Constat.** Le conteneur d'une session peut être repris pendant une période où elle n'a aucune tâche active ; la
  reprise tue tous ses processus, lanceur compris, sans `arret.json` (§ 2). Le conteneur de ce jeu a redémarré vers
  06:13Z (R-2964) et vers 11:24Z (annexe A, [5]) ; d'après les noms et les heures des journaux de la session (non
  ouverts ; contre-lecture du tour 1, annexe B), la session a tourné du 15 novembre 20:13:13Z au 16 novembre 04:36:02Z,
  de 06:13:17Z à 06:37:47Z, de 07:09:55Z à 07:14:53Z, puis depuis 11:24:08Z : trois reprises au moins depuis le
  lancement (causes de celles de 07:09Z et de 11:24Z non établies ici). Au lancement, la surveillance était tenue par
  une attente en arrière-plan de la mère (R-2951) ; d'après les heures et les tailles des sorties de tâches de fond de
  la session (non ouvertes), deux sorties de 10 octets sont écrites à 02:31:14Z et à 04:31:41Z, à deux heures d'écart,
  et aucune tâche de fond n'est armée ensuite (lecture : deux attentes menées jusqu'à la limite de l'outil, la seconde
  non réarmée) ; les journaux de la session s'arrêtent quatre minutes plus tard, à 04:36:02Z. Une session sans tâche
  active peut donc perdre son conteneur en quelques minutes. Précédent : A1-v3 (R-1103, l. 1331 : conteneur « repris après inactivité de sa session » ;
  règle d'alors : session active jusqu'à la fin, « attente en arrière-plan suivie par le harnais, réarmée avant son
  délai », « jamais par la seule relève horaire »).
- **Consigne.** La session qui tient le jeu — celle qui le lance, ou la session mère si un sous-agent le lance — garde une
  tâche active pendant tout le jeu : dès le lancement, elle arme une attente en arrière-plan suivie par le harnais, qui
  **se termine d'elle-même avant la limite de durée de l'outil**, que le parent ait fini ou non (par exemple
  `timeout <secondes> tail --pid=<PID> -f /dev/null`, la durée choisie sous cette limite : code 0, le parent a fini ;
  code 124, l'attente a expiré), et **la réarme à chaque fin**, dans le tour même où elle rend la main, tant que le
  parent vit. L'attente n'est jamais laissée jusqu'à la limite de l'outil, qui l'arrêterait ; faute de tâche active, le
  conteneur peut être repris (constat). Ni un rappel programmé ni une relève périodique ne la remplacent ; un sous-agent
  qui a fini ne la tient pas. La suite des attentes ne cesse qu'après la fin du parent (`journal.json` ou `arret.json`
  écrit, ou parent disparu).
- **Ce que la consigne n'exclut pas, déclaré** : la limite d'usage de la session (précédent : R-1463, l. 1421), une
  reprise imposée malgré une tâche active, une panne de la machine.
- **Seconde interruption.** Même règle : run invalide, aucune lecture partielle, relance seulement sous un texte ou un
  addendum neuf (un second addendum de relance), aux mêmes conditions ; ses fichiers suivent le § 6. Chaque relance refait
  les mêmes tirages (§ 4.2), et chaque run invalide est rapporté (§ 4.8).

## 6. Fichiers du run invalide

Trois fichiers, leurs compagnons (§ 2) et le journal vide. Deux voies ont été pesées ; **la mère a retenu la
voie (a)** (R-2973) : fichiers laissés scellés et non lus dans la copie jusqu'au prononcé du run neuf.

**(a) Les laisser scellés et non lus dans `/home/user/jeu-idee-1-2-copie`**, empreintes citées ici (§ 2) ; rien n'est
copié dans le dépôt.

- Pour : aucune exposition (jamais sur le dépôt distant ; aucun agent ne les ouvre en parcourant une branche) ; rien
  n'entre dans `main`, donc rien ne gêne la garde du lanceur (4.3) ; aucun geste ; les empreintes de cet addendum scellé
  fixent ce qui a existé, et aucun usage permis n'exige de les ouvrir (§ 3).
- Contre : ils ne vivent que sur le disque de cette machine ; ils ont survécu à trois redémarrages au moins (≈ 06:13Z, ≈ 07:09Z, ≈ 11:24Z ; § 5), mais
  un remplacement de la machine les effacerait, et seules leurs empreintes resteraient ; ni Lazar ni un auditeur hors de
  cette machine ne peut les revérifier ; la copie garde pour dépôt distant le dépôt principal, en lecture et en poussée
  (annexe A, [3]) : une commande git qui écrit, jouée par erreur dans la copie, pourrait les y porter ; la copie
  entière reste en place : ≈ 2,8 Go d'arbre de travail retenus sur un disque de ≈ 39 Go (4.4).

**(b) Les verser non lus sur une branche d'archive** (par exemple `donnees/idee-1-2-tirages-repartis-interrompu-v1`),
jamais fusionnée dans `main`. Précédent : les états interrompus d'A1-v3 (R-1105, l. 1333 ; R-1463, l. 1421).

- Pour : durables, visibles, revérifiables par leurs compagnons sans être ouverts ; conforme au précédent.
- Contre : exposition — le contenu de l'oracle est celui du run neuf (§ 3) ; sur le dépôt distant, toute session pourrait
  l'ouvrir avant la lecture gelée du run neuf, ce qui le contaminerait ([T] l. 514) ; versés par erreur dans `main`, ils
  feraient refuser au lanceur gelé toute relance faite depuis `main` (lanceur l. 135 ; message, l. 74) ; une poussée de
  plus sur le dépôt distant. Le précédent d'A1-v3 portait sur des courses à dépense, dont l'état interrompu n'était pas
  refait par la course suivante ; ici, la relance refait les tirages.

**Décision de la mère : voie (a)** (R-2973), sur la recommandation du rédacteur (confiance 0,65). Ces fichiers ne portent rien que la relance ne refasse, et personne ne doit les
lire : les garder hors du dépôt ne coûte rien ; les exposer ferait courir un risque réel, la lecture anticipée de l'oracle
du run neuf. Conditions : la copie `/home/user/jeu-idee-1-2-copie` n'est ni effacée, ni déplacée, ni modifiée (aucune
commande git qui écrit, aucun lancement ; toute commande git de lecture y est jouée avec `--no-optional-locks` ou
`GIT_OPTIONAL_LOCKS=0`, pour ne poser aucun verrou d'index) jusqu'au prononcé du run neuf ; ensuite, la garder ou l'effacer est une décision
de la mère, consignée ; sa perte par un remplacement de la machine est consignée quand on la constate, sans autre effet.
**Après le prononcé du run neuf**, la voie (b) reste ouverte si la mère veut une trace durable : le risque de
contamination est alors nul, et la règle « personne ne les ouvre » demeure.

## Contre-lecture

- **Contre-lecture 1** (R2) — lecteur neuf, sous-agent de la session mère (lettre du modèle : inscrite par la mère au
  registre), qui n'a écrit ni ce brouillon ni aucune pièce de l'idée 1.2 ; texte relu : brouillon 1,
  `docs/notes/organisme-idees-juge-v1/addendum-relance-idee-1-2-v1-brouillon1.md`,
  `26aa0713419ecff1cbb2cd4240e17dfdc0aea9902e66e4f2c9020560ed50fdd3` ; rapport :
  `docs/notes/organisme-idees-juge-v1/contre-lecture-addendum-relance-idee-1-2-tour1-v1.md`,
  `1b73554004a0cfc77b2448dc19f9d204bbe890382bbf19b91efbefa7a71a486f` (égal à son compagnon) ; programme de l'annexe A
  rejoué le 2026-11-16 à 12:21:47Z sur la tête `1332acb3` de `main` : même sortie, aux heures, à la tête, à la durée de
  marche de la machine et aux empreintes des registres près. Verdict : « corrections » (2 majeures, 11 mineures, en 17
  couples exigés ; 3 couples facultatifs ; remarques F4 à F10 sans couple) ; « la conception n'est pas en cause ».
- **Traitement** (brouillon 2) — chaque couple exigé est tiré du § 4 du rapport par programme ; chaque « ancien » figure
  une seule fois dans le brouillon 1 ; aucun chevauchement :
  - **M1** (§ 5, consigne : attente qui se termine d'elle-même avant la limite de l'outil, réarmée à chaque fin ; décision
    (vi) de la mère) : appliqué.
  - **M2** (4.10 neuf : jeu relancé en même temps que le jeu de l'idée 1.1 sur la même machine, conséquences sur la durée
    et sur la borne de 24 heures ; décision (v)) : appliqué.
  - **m1** (nom `…-addendum-relance-v1.md` confirmé, « v2 » de R-2964 erreur de plume ; décision (i)) : appliqué.
  - **m2** (pas de mot nouveau de Lazar, avec ses raisons ; décision (iv)) : appliqué.
  - **m3-a, m3-b, m3-c** (voie (a) retenue par la mère ; décision (ii)) : appliqués.
  - **m4** (instant de l'arrêt ≈ 04:36Z, non 06:13Z) : appliqué.
  - **m5** (trois reprises au moins ; sort de l'attente) : appliqué tel que proposé. La lecture « deux attentes menées
    jusqu'à la limite de l'outil, la seconde non réarmée » est celle du contre-lecteur, tirée des seules heures et tailles
    des fichiers ; le rédacteur du brouillon 2 ne l'a pas confirmée sur le journal de la mère, qu'il n'a pas lu ; elle
    concorde avec la décision (vi). Si le journal de la mère la dément, elle est corrigée avant la recopie sous `prereg/`,
    les heures, qui sont des faits, gardées.
  - **m6, m7-a, m7-b, m8, m9** : appliqués.
  - **m10** : appliqué en substance — cette section ; l'empreinte entière du rapport et le traitement y sont écrits
    directement, au lieu des mots que le « nouveau » du rapport laissait à la mère.
  - **m11-a, m11-b** (espace disque) : appliqués ; le seuil de 1 Go reste celui que propose le rapport, à fixer par la
    mère (rapport, § 6, point 4).
  - **f1, f2, f3** (facultatifs) : non appliqués ; le brouillon 2 est borné aux corrections exigées ; laissés à la mère.
  - **F4 à F10** (sans couple) : non appliqués ; laissés à la mère, F4 (comparaison des deux oracles après le prononcé)
    étant à trancher avant le scellement sous `prereg/` si elle la veut permise.
  - **Rapport, § 6, points 4, 5, 6 et 9** (variante de la voie (a) si la place manque ; déclaration symétrique dans
    l'addendum de l'idée 1.1 ; limite d'usage de la session ; lettre du modèle) : à la mère, hors de cette pièce.
  - **Rapport, § 6, point 7** : recompté par le programme sur le brouillon 2 : zéro ligne au format du lanceur.
- **Les six décisions de la mère, où elles sont écrites** : (i) nom du texte qui fera foi, en-tête (m1) ; (ii) voie (a),
  § 6 (m3) ; (iii) contrôle des versions de l'interpréteur avant le lancement, 4.2 (présent dès le brouillon 1,
  inchangé) ; (iv) aucun mot nouveau du directeur, 4.9 (m2) ; (v) jeu en même temps que celui de l'idée 1.1, 4.10 (M2) ;
  (vi) tâche active pendant tout le jeu, attente bornée réarmée à chaque fin, § 5 (M1).

## Annexe A — programme de vérification et sa sortie, recopiés en entier

Programme `verifier_relance_idee_1_2_v1.py` (`02d193c536eae1c534f2c2cffdefe1968587dbc7aac1fe45ff8b0987723ba8de`) et
sortie `sortie-verifier-relance-idee-1-2-v1.txt` (`a634334f8f1cbb538ff3f15ba1d34778a29e6c222723519e9187ff1eed798214`),
dossier de travail de la session ; lancé par `python3 -I -B` (interpréteur du système, aucune importation du paquet du
dépôt ni de numpy) le 2026-11-16 de 12:06:35Z à 12:06:36Z ; commandes légères seulement. Chaque bloc ci-dessous est le
fichier, octet pour octet, entre la ligne d'ouverture et la ligne de clôture.

Sortie :

```text
début (date -u) : 2026-11-16T12:06:35Z
tête de main : d4b81652d936d6d3fd620cd4260d367a0fa83805

[1] textes qui font foi (arbre du dépôt, compagnon, objet de main)
prereg/organisme-idee-1-2-tirages-repartis-arret-anticipe-v4.md : arbre bdabf2bc9b2c9b78939660f7f7053576a145e165927cafd23e14a798d07d790e ; compagnon égal ; objet de main égal
prereg/organisme-idee-1-2-tirages-repartis-arret-anticipe-v4-addendum-empreintes-v1.md : arbre 1b96cf065cef40ed9e452611b107d9f40f598091c8a591f2397bf58e7c92beee ; compagnon égal ; objet de main égal

[2] les 34 fichiers gelés de l'addendum d'empreintes v1
lignes au format du lanceur : 34 ; chemins distincts : 34
égales : arbre du dépôt 34/34 ; objets de main 34/34 ; arbre de la copie du run invalide 34/34
empreinte du bloc des 34 lignes, dans l'ordre de l'addendum : b6e724a48fa3a57a28819c052ed68fcbd7ce95302283c0fbb5416b2b6fc239d2
commit du run invalide 2753ecf2 ancêtre de main : oui
git diff 2753ecf2 → main sur les 34 chemins : aucune différence
liste de la copie du juge, objet de main : 0153e02d4522fe21eb1cf52985574eba38b5f260f7a3a08183d63589f29f32df

[3] copie du run invalide
HEAD de la copie : 2753ecf295f1226f3e284f14ef194022920b8cc8
lignes de `git status --porcelain --untracked-files=all` : 6
    ?? diag/organisme-idees-juge-v1/20261116-002954-idee-1-2-tirages-repartis-v1/controles-avant-jeu.json
    ?? diag/organisme-idees-juge-v1/20261116-002954-idee-1-2-tirages-repartis-v1/controles-avant-jeu.json.sha256
    ?? diag/organisme-idees-juge-v1/20261116-002954-idee-1-2-tirages-repartis-v1/oracle.json
    ?? diag/organisme-idees-juge-v1/20261116-002954-idee-1-2-tirages-repartis-v1/oracle.json.sha256
    ?? runs/20261116-002954-idee-1-2-tirages-repartis-v1/manifeste.json
    ?? runs/20261116-002954-idee-1-2-tirages-repartis-v1/manifeste.json.sha256
objets d'emprunt (alternates) : aucun
dépôt distant de la copie : origin	/home/user/controle-ia-travail (fetch)
dépôt distant de la copie : origin	/home/user/controle-ia-travail (push)

[4] fichiers du run invalide (empreintes par sha256sum -c depuis leur dossier ; tailles et heures par stat)
runs/20261116-002954-idee-1-2-tirages-repartis-v1/manifeste.json : sha256sum -c « manifeste.json: OK » (code 0) ; compagnon : 93ee47caf273a8f0461afeb2b8e75fcd6587563b0fffb268e5d75b8caa0b44da pour manifeste.json ; taille 9489 octets ; modification 2026-11-16 00:38:05.061519248 +0000 ; accès 2026-11-16 00:38:05.061611748 +0000
diag/organisme-idees-juge-v1/20261116-002954-idee-1-2-tirages-repartis-v1/controles-avant-jeu.json : sha256sum -c « controles-avant-jeu.json: OK » (code 0) ; compagnon : 4952a7e3a93ab66e0218048caec6bfe99be832ad063c1131cd6269fb515da7b7 pour controles-avant-jeu.json ; taille 10076 octets ; modification 2026-11-16 00:53:28.547248521 +0000 ; accès 2026-11-16 00:53:28.547432347 +0000
diag/organisme-idees-juge-v1/20261116-002954-idee-1-2-tirages-repartis-v1/oracle.json : sha256sum -c « oracle.json: OK » (code 0) ; compagnon : 464bd7deb77904b65aec8f983cabafd42c45d82ea9c4457043ff668bcf1524ac pour oracle.json ; taille 13505894 octets ; modification 2026-11-16 01:22:37.486751977 +0000 ; accès 2026-11-16 01:22:37.490751977 +0000
diag/organisme-idees-juge-v1/20261116-002954-idee-1-2-tirages-repartis-v1/jeu.json : absent
diag/organisme-idees-juge-v1/20261116-002954-idee-1-2-tirages-repartis-v1/journal.json : absent
diag/organisme-idees-juge-v1/20261116-002954-idee-1-2-tirages-repartis-v1/arret.json : absent
diag/organisme-idees-juge-v1/20261116-002954-idee-1-2-tirages-repartis-v1/lecture-gelee-v2.json : absent
options de montage de /home/user : rw,relatime,discard,no_prefetch_block_bitmaps,resv_strict,resuid=65534,resgid=65534
/home/user/jeu-idee-1-2.log : taille 0 octets ; modification 2026-11-16 00:29:54.090804109 +0000

[5] machine
/proc/uptime : 2554 s à 2026-11-16T12:06:35+00:00 ; démarrage ≈ 2026-11-16T11:24:01+00:00
processus 5755 : aucun
/usr/local/bin/python : 3.13.18 ; numpy 2.5.3 ; scipy absent ; pytest absent
/usr/bin/python3 : 3.13.18 ; numpy 2.5.3 ; scipy absent ; pytest absent
/usr/bin/python3.11 : 3.11.18 ; numpy absent ; scipy absent ; pytest absent
/usr/bin/python3.12 : 3.12.3 ; numpy absent ; scipy absent ; pytest absent
/usr/bin/python3.13 : 3.13.18 ; numpy 2.5.3 ; scipy absent ; pytest absent
/home/user/vastai-env/bin/python : 3.13.18 ; numpy absent ; scipy absent ; pytest absent
/home/user/controle-ia-travail/.venv/bin/python : 3.13.18 ; numpy 2.4.6 ; scipy 1.17.1 ; pytest 9.1.1
.venv/lib/python3.13/site-packages/numpy-2.4.6.dist-info : modification 2026-11-14 13:43:45.212955870 +0000
.venv/lib/python3.13/site-packages/scipy-1.17.1.dist-info : modification 2026-11-14 13:43:56.526310208 +0000

[6] lignes du code gelé (fichiers du § 2, objets de main égaux)
src/controle_ia/organisme_idees_juge/banc_tirages_repartis_v1.py l. 6 : `numpy.random.SeedSequence(entropy=racine, spawn_key=clé)`, famille 0 = N, 1 = T : monde `(f, g, 24)` ; archive
src/controle_ia/organisme_idees_juge/banc_tirages_repartis_v1.py l. 37 : EMPREINTE_PREREG = "bdabf2bc9b2c9b78939660f7f7053576a145e165927cafd23e14a798d07d790e"
src/controle_ia/organisme_idees_juge/banc_tirages_repartis_v1.py l. 61 : def racine_de(empreinte_hex: str) -> int:
src/controle_ia/organisme_idees_juge/banc_tirages_repartis_v1.py l. 64 : return int(empreinte_hex, 16)
src/controle_ia/organisme_idees_juge/banc_tirages_repartis_v1.py l. 67 : def generateur(racine: int, *cle: int) -> np.random.Generator:
src/controle_ia/organisme_idees_juge/banc_tirages_repartis_v1.py l. 70 : return np.random.default_rng(np.random.SeedSequence(entropy=racine, spawn_key=tuple(int(c) for c in cle)))
src/controle_ia/organisme_idees_juge/banc_tirages_repartis_v1.py l. 74 : return [int(x) for x in np.random.SeedSequence(entropy=racine, spawn_key=tuple(int(c) for c in cle)).generate_state(2)]
scripts/jouer_idee_1_2_v2.py l. 48 : from controle_ia.organisme_idees_juge import lire_banc_tirages_repartis_v2 as LB  # noqa: E402
scripts/jouer_idee_1_2_v2.py l. 74 : raise GardeArret(f"{quoi} de ce jeu existe déjà ({anciens}) : relance seulement sous un texte ou un addendum neuf")
scripts/jouer_idee_1_2_v2.py l. 79 : return signal.signal(signal.SIGTERM, lever_sur_term)
scripts/jouer_idee_1_2_v2.py l. 83 : os.nice(10)
scripts/jouer_idee_1_2_v2.py l. 130 : garde = X.GardeDuree(horloge=time.time)
scripts/jouer_idee_1_2_v2.py l. 132 : run_id = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S") + "-" + X.NOM_RUN
scripts/jouer_idee_1_2_v2.py l. 134 : exiger_depot_propre(RACINE_DEPOT)
scripts/jouer_idee_1_2_v2.py l. 135 : exiger_sortie_absente(RACINE_DEPOT, run_id)
scripts/jouer_idee_1_2_v2.py l. 139 : liste = X.verifier_addendum(RACINE_DEPOT, chemin_add)
scripts/jouer_idee_1_2_v2.py l. 144 : controles["essais"] = lancer_essais(RACINE_DEPOT)
scripts/jouer_idee_1_2_v2.py l. 145 : racine = B.racine_de(B.EMPREINTE_PREREG)
scripts/jouer_idee_1_2_v2.py l. 146 : rapport_mut = MU.banc(racine)
scripts/jouer_idee_1_2_v2.py l. 147 : MU.exiger_toutes_tuees(rapport_mut)
scripts/jouer_idee_1_2_v2.py l. 152 : chemin_m, _ = creer_manifeste(RACINE_DEPOT, run_id, config, ["racine-du-texte"], entropie=racine, decisif=True,
scripts/jouer_idee_1_2_v2.py l. 160 : res = X.executer(racine=racine, generations=generations, dossier_sortie=dossier, run_id=run_id, manifeste_sha=sha_m,
scripts/jouer_idee_1_2_v2.py l. 162 : except BaseException as e:
scripts/jouer_idee_1_2_v2.py l. 163 : print(f"ARRÊT : {X.consigner_arret(dossier, e, run_id, sha_m, journal)}", file=sys.stderr)
scripts/jouer_idee_1_2_v2.py l. 171 : garde = X.GardeDuree(horloge=time.time)
scripts/jouer_idee_1_2_v2.py l. 184 : run_id = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S") + "-miniature-" + X.NOM_RUN
scripts/jouer_idee_1_2_v2.py l. 189 : MU.exiger_toutes_tuees(rapport_mut)
scripts/jouer_idee_1_2_v2.py l. 210 : res = X.executer(racine=racine, generations=generations, dossier_sortie=dossier, run_id=run_id, manifeste_sha=sha_m,
scripts/jouer_idee_1_2_v2.py l. 212 : except BaseException as e:
scripts/jouer_idee_1_2_v2.py l. 213 : print(f"ARRÊT : {X.consigner_arret(dossier, e, run_id, sha_m, journal)}", file=sys.stderr)
src/controle_ia/organisme_idees_juge/lire_banc_tirages_repartis_v2.py l. 23 : from . import lire_banc_tirages_repartis_v1 as LB1
src/controle_ia/organisme_idees_juge/lire_banc_tirages_repartis_v1.py l. 20 : from scipy.stats import beta, binom, binomtest
src/controle_ia/organisme_idees_juge/execution_v1.py l. 29 : DUREE_MAX_S = 24 * 3600
src/controle_ia/organisme_idees_juge/execution_v1.py l. 31 : DOSSIER_DIAG = Path("diag") / "organisme-idees-juge-v1"
src/controle_ia/organisme_idees_juge/execution_v1.py l. 32 : NOM_RUN = "idee-1-2-tirages-repartis-v1"
src/controle_ia/organisme_idees_juge/execution_v1.py l. 96 : corps = {"run_id": run_id, "manifeste_sha256": manifeste_sha, "resultat": resultat}
src/controle_ia/organisme_idees_juge/execution_v1.py l. 271 : "regle": "arrêt du run ; aucune lecture partielle ; relance seulement sous un texte ou un addendum neuf (R5)"}
src/controle_ia/organisme_idees_juge/execution_v2.py l. 116 : table["duree_s"] = time.time() - t0
src/controle_ia/organisme_idees_juge/execution_v2.py l. 158 : _, sha_c = ecrire_scelle(dossier_sortie, "controles-avant-jeu", controles, run_id, manifeste_sha)
src/controle_ia/organisme_idees_juge/execution_v2.py l. 160 : if echecs:
src/controle_ia/organisme_idees_juge/execution_v2.py l. 162 : phase("oracle")
src/controle_ia/organisme_idees_juge/execution_v2.py l. 164 : chemin_o, sha_o = ecrire_scelle(dossier_sortie, "oracle", {"generations": tables}, run_id, manifeste_sha)
src/controle_ia/organisme_idees_juge/execution_v2.py l. 168 : phase("jeu")
src/controle_ia/organisme_idees_juge/execution_v2.py l. 176 : _, sha_j = ecrire_scelle(dossier_sortie, "jeu", {"generations": gens}, run_id, manifeste_sha)
src/controle_ia/organisme_idees_juge/execution_v2.py l. 183 : _, sha_jr = ecrire_scelle(dossier_sortie, "journal", journal, run_id, manifeste_sha)
src/controle_ia/organisme_idees_juge/lire_banc_tirages_repartis_v2.py l. 64 : if (dossier / "arret.json").exists():
src/controle_ia/organisme_idees_juge/lire_banc_tirages_repartis_v2.py l. 69 : raise GardeArret(f"journal absent ou non scellé : run incomplet, aucune lecture ({e})") from None
src/controle_ia/gardes.py l. 100 : statut = git("status", "--porcelain", "--untracked-files=all")
src/controle_ia/manifeste.py l. 78 : raise GardeArret(f"{dossier} existe déjà : R12 interdit d'écraser un run")

[7] lignes citées du texte [T] et de l'addendum [AE]
organisme-idee-1-2-tirages-repartis-arret-anticipe-v4.md l. 451 : Racine : entier de l'empreinte sha256 du texte qui fera foi. `numpy.random.SeedSequence(entropy=racine, spawn_key=…)`, famille
organisme-idee-1-2-tirages-repartis-arret-anticipe-v4.md l. 456 : mutations `(97, g)` (Métrique, réserve (a)). Manifeste du run (`src/controle_ia/manifeste.py`).
organisme-idee-1-2-tirages-repartis-arret-anticipe-v4.md l. 472 : 3. Oracle calculé et scellé pour toutes les générations, **avant** le rejeu des bras.
organisme-idee-1-2-tirages-repartis-arret-anticipe-v4.md l. 473 : 4. Jeu : 1 250 générations, `nice -n 10`, deux processus au plus.
organisme-idee-1-2-tirages-repartis-arret-anticipe-v4.md l. 474 : 5. Sortie scellée avant toute lecture, sous `diag/organisme-idees-juge-v1/`.
organisme-idee-1-2-tirages-repartis-arret-anticipe-v4.md l. 475 : 6. Lecture gelée, puis lecteur neuf (R13), audit de symétrie (R4) écrit avant le prononcé.
organisme-idee-1-2-tirages-repartis-arret-anticipe-v4.md l. 506 : | un fichier gelé diffère de l'addendum ; un essai échoue ; une mutation survit | pas de jeu |
organisme-idee-1-2-tirages-repartis-arret-anticipe-v4.md l. 512 : | exception, log W non fini | arrêt du run ; aucune lecture partielle ; relance seulement sous un texte ou un addendum neuf (R5) |
organisme-idee-1-2-tirages-repartis-arret-anticipe-v4.md l. 513 : | durée murale > 24 h | arrêt ; run invalide |
organisme-idee-1-2-tirages-repartis-arret-anticipe-v4.md l. 514 : | lecture avant scellement de la sortie, ou oracle calculé après le rejeu | run invalide |
organisme-idee-1-2-tirages-repartis-arret-anticipe-v4.md l. 515 : | toute dépense, instance payante ou appel de modèle | interdit (R-2851) |
organisme-idee-1-2-tirages-repartis-arret-anticipe-v4-addendum-empreintes-v1.md l. 63 : Lanceur du jeu : `scripts/jouer_idee_1_2_v2.py` (ligne ci-dessus), commande
organisme-idee-1-2-tirages-repartis-arret-anticipe-v4-addendum-empreintes-v1.md l. 64 : `python -I -B scripts/jouer_idee_1_2_v2.py --addendum prereg/organisme-idee-1-2-tirages-repartis-arret-anticipe-v4-addendum-empreintes-v1.md`
organisme-idee-1-2-tirages-repartis-arret-anticipe-v4-addendum-empreintes-v1.md l. 66 : scellement de la sortie. Le jeu peut être lancé depuis une copie propre, détachée, du commit qui porte cet addendum : le
organisme-idee-1-2-tirages-repartis-arret-anticipe-v4-addendum-empreintes-v1.md l. 67 : manifeste en consigne le commit ; ses sorties scellées sont recopiées octet pour octet dans le dépôt et vérifiées par leurs
organisme-idee-1-2-tirages-repartis-arret-anticipe-v4-addendum-empreintes-v1.md l. 68 : compagnons avant toute lecture.
organisme-idee-1-2-tirages-repartis-arret-anticipe-v4-addendum-empreintes-v1.md l. 106 : - **Réserve neuve ([RL], point 1) — mort d'un fils oisif.** Si un processus fils meurt alors qu'il **attend** une tâche (il
organisme-idee-1-2-tirages-repartis-arret-anticipe-v4-addendum-empreintes-v1.md l. 111 : lu (pas de `jeu.json` ; le lecteur v2 refuse sans `journal.json`) : échec du côté sûr. **Consigne d'opérateur** : si
organisme-idee-1-2-tirages-repartis-arret-anticipe-v4-addendum-empreintes-v1.md l. 112 : `journal.json` n'est pas écrit à la durée attendue (§ 5) et que les processus du run n'emploient plus le processeur,
organisme-idee-1-2-tirages-repartis-arret-anticipe-v4-addendum-empreintes-v1.md l. 113 : envoyer le signal TERM **au processus parent, par son PID** (`kill -TERM <PID>` ; jamais par motif de ligne de commande,
organisme-idee-1-2-tirages-repartis-arret-anticipe-v4-addendum-empreintes-v1.md l. 114 : R10) ; le lanceur lève alors `GardeArret` et écrit `arret.json` ([RL] : sortie en 9,6 s, aucun fils restant) ; **run
organisme-idee-1-2-tirages-repartis-arret-anticipe-v4-addendum-empreintes-v1.md l. 115 : invalide** ; relance seulement sous un texte ou un addendum neuf ([T] l. 512). Le PID du parent est noté au lancement.
organisme-idee-1-2-tirages-repartis-arret-anticipe-v4-addendum-empreintes-v1.md l. 137 : processus). **Total ≈ 3 à 5,5 h sur machine libre ; ≈ 6 à 7,5 h sous une charge comme celle du jour.** Borne dure 24 h

[8] registres à la tête de main
registres/decisions.md (objet de main d4b81652) : 7025e9857afd71a855a29aab3b1726865d3b246b148a3f5baaa6c54fdd05b3c3
   R-1103 : l. 1331
   R-1105 : l. 1333
   R-1463 : l. 1421
   R-2910 : l. 2870
   R-2951 : l. 2911
   R-2964 : l. 2924
registres/go.md (objet de main d4b81652) : b46dcde26612137d593100a135e698480034e0eef1f2a62c1d004bc71554b98a
   GO-2026-11-16-01 : l. 342

fin (date -u) : 2026-11-16T12:06:36Z
```

Programme :

```python
"""Vérifications de l'addendum de relance de l'idée 1.2 (brouillon 1). Commandes légères seulement : aucune importation du
paquet du dépôt, aucune importation de numpy, aucun essai, aucun jeu. N'ouvre aucun fichier du run invalide : ses trois
fichiers ne sont lus que par `sha256sum -c` de leurs compagnons, lancé depuis leur dossier dans la copie ; leurs noms,
tailles et heures viennent de `stat`. Aucune ligne de la sortie n'a la forme « empreinte, deux espaces, chemin »."""
import datetime
import hashlib
import re
import subprocess
from pathlib import Path

DEPOT = Path("/home/user/controle-ia-travail")
COPIE = Path("/home/user/jeu-idee-1-2-copie")
RUN = "20261116-002954-idee-1-2-tirages-repartis-v1"
TEXTE = "prereg/organisme-idee-1-2-tirages-repartis-arret-anticipe-v4.md"
ADD = "prereg/organisme-idee-1-2-tirages-repartis-arret-anticipe-v4-addendum-empreintes-v1.md"
COMMIT_RUN = "2753ecf295f1226f3e284f14ef194022920b8cc8"
MOTIF_LANCEUR = r"^([0-9a-f]{64})  (\S+)\s*$"     # expression de `execution_v1.verifier_addendum`


def sh(*cmd, cwd=None, check=True):
    return subprocess.run(list(cmd), cwd=cwd, capture_output=True, text=True, check=check)


def h(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def maintenant() -> str:
    return sh("date", "-u", "+%Y-%m-%dT%H:%M:%SZ").stdout.strip()


print("début (date -u) :", maintenant())
tete = sh("git", "-C", str(DEPOT), "rev-parse", "main").stdout.strip()
print("tête de main :", tete)

print("\n[1] textes qui font foi (arbre du dépôt, compagnon, objet de main)")
for f in (TEXTE, ADD):
    arbre = h((DEPOT / f).read_bytes())
    comp = (DEPOT / (f + ".sha256")).read_text().split()[0]
    obj = h(subprocess.run(["git", "-C", str(DEPOT), "show", f"main:{f}"], capture_output=True, check=True).stdout)
    print(f"{f} : arbre {arbre} ; compagnon {'égal' if comp == arbre else 'DIFFÈRE'} ; objet de main {'égal' if obj == arbre else 'DIFFÈRE'}")

print("\n[2] les 34 fichiers gelés de l'addendum d'empreintes v1")
lignes = re.findall(MOTIF_LANCEUR, (DEPOT / ADD).read_text(encoding="utf-8"), flags=re.M)
print("lignes au format du lanceur :", len(lignes), "; chemins distincts :", len({p for _, p in lignes}))
n_a = n_m = n_c = 0
for e, p in lignes:
    a = h((DEPOT / p).read_bytes()) == e
    m = h(subprocess.run(["git", "-C", str(DEPOT), "show", f"main:{p}"], capture_output=True, check=True).stdout) == e
    c = h((COPIE / p).read_bytes()) == e
    n_a, n_m, n_c = n_a + a, n_m + m, n_c + c
    if not (a and m and c):
        print("DIFFÈRE :", p, a, m, c)
print(f"égales : arbre du dépôt {n_a}/{len(lignes)} ; objets de main {n_m}/{len(lignes)} ; arbre de la copie du run invalide {n_c}/{len(lignes)}")
print("empreinte du bloc des 34 lignes, dans l'ordre de l'addendum :", h("".join(f"{e}  {p}\n" for e, p in lignes).encode()))
anc = sh("git", "-C", str(DEPOT), "merge-base", "--is-ancestor", COMMIT_RUN, "main", check=False).returncode
print("commit du run invalide", COMMIT_RUN[:8], "ancêtre de main :", "oui" if anc == 0 else "non")
d = sh("git", "-C", str(DEPOT), "diff", "--quiet", COMMIT_RUN, "main", "--", *[p for _, p in lignes], check=False).returncode
print("git diff", COMMIT_RUN[:8], "→ main sur les 34 chemins :", "aucune différence" if d == 0 else f"différences (code {d})")
liste_juge = "docs/notes/organisme-courbe-dose-reponse-v1/code-organisme-94bfd92/empreintes-copie-v1.txt"
print("liste de la copie du juge, objet de main :",
      h(subprocess.run(["git", "-C", str(DEPOT), "show", f"main:{liste_juge}"], capture_output=True, check=True).stdout))

print("\n[3] copie du run invalide")
print("HEAD de la copie :", sh("git", "-C", str(COPIE), "rev-parse", "HEAD").stdout.strip())
statut = sh("git", "-C", str(COPIE), "status", "--porcelain", "--untracked-files=all").stdout.splitlines()
print("lignes de `git status --porcelain --untracked-files=all` :", len(statut))
for s in statut:
    print("   ", s)
print("objets d'emprunt (alternates) :", "présents" if (COPIE / ".git/objects/info/alternates").exists() else "aucun")
for l in sh("git", "-C", str(COPIE), "remote", "-v").stdout.splitlines():
    print("dépôt distant de la copie :", l)

print("\n[4] fichiers du run invalide (empreintes par sha256sum -c depuis leur dossier ; tailles et heures par stat)")
dossiers = {COPIE / "runs" / RUN: ["manifeste.json"],
            COPIE / "diag/organisme-idees-juge-v1" / RUN: ["controles-avant-jeu.json", "oracle.json"]}
for dossier, noms in dossiers.items():
    for n in noms:
        r = sh("sha256sum", "-c", n + ".sha256", cwd=dossier, check=False)
        comp = (dossier / (n + ".sha256")).read_text().split()
        st = sh("stat", "-c", "%s|%y|%x", n, cwd=dossier).stdout.strip().split("|")
        rel = (dossier / n).relative_to(COPIE)
        print(f"{rel} : sha256sum -c « {r.stdout.strip()} » (code {r.returncode}) ; compagnon : {comp[0]} pour {comp[1]} ;"
              f" taille {st[0]} octets ; modification {st[1]} ; accès {st[2]}")
for n in ("jeu.json", "journal.json", "arret.json", "lecture-gelee-v2.json"):
    p = COPIE / "diag/organisme-idees-juge-v1" / RUN / n
    print(f"diag/organisme-idees-juge-v1/{RUN}/{n} :", "PRÉSENT" if p.exists() else "absent")
print("options de montage de /home/user :", sh("findmnt", "-no", "OPTIONS", "-T", "/home/user").stdout.strip())
st = sh("stat", "-c", "%s|%y", "/home/user/jeu-idee-1-2.log").stdout.strip().split("|")
print(f"/home/user/jeu-idee-1-2.log : taille {st[0]} octets ; modification {st[1]}")

print("\n[5] machine")
u = float(Path("/proc/uptime").read_text().split()[0])
t = datetime.datetime.now(datetime.timezone.utc)
print(f"/proc/uptime : {u:.0f} s à {t.isoformat(timespec='seconds')} ; démarrage ≈ {(t - datetime.timedelta(seconds=u)).isoformat(timespec='seconds')}")
ps = sh("ps", "-p", "5755", "-o", "pid=,lstart=,comm=", check=False)
print("processus 5755 :", ps.stdout.strip() or "aucun")
for py in ("/usr/local/bin/python", "/usr/bin/python3", "/usr/bin/python3.11", "/usr/bin/python3.12", "/usr/bin/python3.13",
           "/home/user/vastai-env/bin/python", str(DEPOT / ".venv/bin/python")):
    r = sh(py, "-I", "-c", "import sys\nfrom importlib import metadata as m\nv=[sys.version.split()[0]]\n"
           "for b in ('numpy','scipy','pytest'):\n    try: v.append(b+' '+m.version(b))\n    except m.PackageNotFoundError: v.append(b+' absent')\nprint(' ; '.join(v))",
           check=False)
    print(f"{py} : {r.stdout.strip()}")
for g in ("numpy-*.dist-info", "scipy-*.dist-info"):
    for p in sorted((DEPOT / ".venv/lib").glob(f"python*/site-packages/{g}")):
        print(f"{p.relative_to(DEPOT)} : modification {sh('stat', '-c', '%y', str(p)).stdout.strip()}")

print("\n[6] lignes du code gelé (fichiers du § 2, objets de main égaux)")
motifs = [
    ("src/controle_ia/organisme_idees_juge/banc_tirages_repartis_v1.py", r"^EMPREINTE_PREREG = |^def racine_de|return int\(empreinte_hex, 16\)|^def generateur|SeedSequence\(entropy=racine"),
    ("scripts/jouer_idee_1_2_v2.py", r"rapport_mut = MU\.banc\(racine\)|res = X\.executer\(racine=racine|run_id = datetime|exiger_depot_propre\(RACINE_DEPOT\)|exiger_sortie_absente\(RACINE_DEPOT|racine = B\.racine_de|creer_manifeste\(|except BaseException|consigner_arret\(dossier|relance seulement|lancer_essais\(RACINE|exiger_toutes_tuees|verifier_addendum\(RACINE|garde = X\.GardeDuree|os\.nice\(10\)|lire_banc_tirages_repartis_v2 as LB|signal\.SIGTERM, lever_sur_term"),
    ("src/controle_ia/organisme_idees_juge/lire_banc_tirages_repartis_v2.py", r"lire_banc_tirages_repartis_v1 as LB1"),
    ("src/controle_ia/organisme_idees_juge/lire_banc_tirages_repartis_v1.py", r"^from scipy"),
    ("src/controle_ia/organisme_idees_juge/execution_v1.py", r"^DUREE_MAX_S|^NOM_RUN|^DOSSIER_DIAG|corps = \{\"run_id\"|\"regle\": \"arrêt du run"),
    ("src/controle_ia/organisme_idees_juge/execution_v2.py", r"ecrire_scelle\(dossier_sortie, \"(controles-avant-jeu|oracle|jeu|journal)\"|table\[\"duree_s\"\]|^    if echecs:|phase\(\"(jeu|oracle)\"\)"),
    ("src/controle_ia/organisme_idees_juge/lire_banc_tirages_repartis_v2.py", r"arret\.json\"\)\.exists|journal absent ou non scell"),
    ("src/controle_ia/gardes.py", r"--untracked-files=all"),
    ("src/controle_ia/manifeste.py", r"R12 interdit d'écraser un run"),
]
for f, mo in motifs:
    for i, l in enumerate((DEPOT / f).read_text(encoding="utf-8").splitlines(), 1):
        if re.search(mo, l):
            print(f"{f} l. {i} : {l.strip()[:150]}")

print("\n[7] lignes citées du texte [T] et de l'addendum [AE]")
for f, nums in ((TEXTE, (451, 456, 472, 473, 474, 475, 506, 512, 513, 514, 515)),
                (ADD, (63, 64, 66, 67, 68, 106, 111, 112, 113, 114, 115, 137))):
    tl = (DEPOT / f).read_text(encoding="utf-8").splitlines()
    for n in nums:
        print(f"{Path(f).name} l. {n} : {tl[n - 1].strip()[:170]}")

print("\n[8] registres à la tête de main")
for f, cles in (("registres/decisions.md", ("| R-1103 ", "| R-1105 ", "| R-1463 ", "| R-2910 ", "| R-2951 ", "| R-2964 ")),
                ("registres/go.md", ("| GO-2026-11-16-01 ",))):
    b = subprocess.run(["git", "-C", str(DEPOT), "show", f"main:{f}"], capture_output=True, check=True).stdout
    tl = b.decode("utf-8").splitlines()
    print(f"{f} (objet de main {tete[:8]}) : {h(b)}")
    for c in cles:
        for i, l in enumerate(tl, 1):
            if l.startswith(c):
                print(f"   {c.strip('| ').strip()} : l. {i}")
print("\nfin (date -u) :", maintenant())
```
