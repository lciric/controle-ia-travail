# Contre-lecture du rapport v2 de la grille de la clause de repli — stabilité de rang du papier C — v1

Date : 2026-11-22. Contre-lecteur neuf : Claude Fable 5.2 (`session_013QMayitHYboVvfqWUdJqqe`), d'une autre lignée
que l'auteur du rapport (Opus 5.5) ; n'a écrit aucune version du préenregistrement du papier C, ni la liste finie, ni
aucun rapport de la grille. Mandat : message de lancement de la mère (`session_013QMayjbmQUdDuDs2S3i3XD`), vers
20:58Z. Pièce contre-lue : `registres/papier-c/grille-clause-de-repli-v2/rapport-grille-clause-de-repli-v2.md`
(`d3d59b087a34f5d92944c1704d422c7261875a54473a25dfd6577570b85f6f85`), branche `prep/papier-c-prereg-fable-v1`,
commit `66d1a86c4`. Données simulées seulement ; tout sur processeur ; aucune dépense, aucun sous-agent. **Ce
rapport porte les taux : il se rend à la mère seule ; le rédacteur du papier C ne l'ouvre pas.**

Dossier de cette contre-lecture : `registres/papier-c/contre-lecture-grille-v2/` (noté `./`). Dossier du rapport
contre-lu : `registres/papier-c/grille-clause-de-repli-v2/` (noté `G/`).

## 1. Avis par ligne

| ligne | avis | ce que le texte appelle l'issue | appui |
|---|---|---|---|
| C-P3a (stabilité du rang des trois juges d'une famille d'attaque à l'autre) | **clause passée** | issue 1 : la ligne garde son verdict, aux trois lectures | 144 cases sur 144 ; plus haut taux de fausses « établies » 0,049 (case 005), seuil 0,0638 ; aucune case au-dessus, aucune à moins de deux erreurs de Monte-Carlo du seuil |
| C-P3b (invariance du rang des juges d'un corpus à l'autre) | **clause passée**, marge mince | issue 1 : la ligne garde son verdict, aux trois lectures | 144 cases sur 144 ; plus haut taux 0,056 (case 097, jouée pour ce rapport), seuil 0,0638 ; aucune case au-dessus ; trois cases à moins de deux erreurs de Monte-Carlo du seuil (074, 093, 097) |
| C-P3c (invariance du rang des juges à l'attaquant) | **ligne rapportée sans verdict** | issue 2 : statistique et valeurs p écrites aux trois lectures, sans « établie » | bras « insertion » : 144 cases sur 144, 82 au-dessus de 0,0549, plus haut taux 0,107 (case 111) ; bras « contenu » : 108 sur 108, 50 au-dessus, plus haut taux 0,095 (case 003) |

**Sans attaque** (g = 0, 48 cases) : C-P3a au plus 0,049 ; C-P3b au plus 0,053 ; C-P3c au-dessus du seuil dans
42 cases sur 48 du bras « insertion » (toutes sauf les six de la compression homogène) et dans 36 cases sur 36 du
bras « contenu », à 0,076 au moins, soit plus de sept erreurs de Monte-Carlo au-dessus du seuil.

**Remarques : 0 bloquante, 1 majeure, 9 mineures.** Aucune correction du rapport n'est exigée avant qu'il soit
cité ; la majeure est une condition du texte qui reste à remplir au scellement, non un défaut du rapport. Les
constats de la section 1 du rapport v2 sont exacts : je les ai tous recalculés par un programme à moi, qui n'importe
aucun programme de l'agent.

**Ce que cet avis ne couvre pas.** Il vaut sous la lecture de la précision 37 du texte, gardée par la chaîne de
décision et non par un mot du directeur (GO-2026-11-22-125, « révisable par Lazar jusqu'au scellement ») : si le
directeur retient la lecture écartée, le texte demande de rejouer la grille. Il vaut sous la condition
d'appariement des témoins (remarque M-1). Je ne décide d'aucune version du texte.

## 2. Ce que j'ai vérifié, et comment

| point du mandat | constat | preuve |
|---|---|---|
| Couverture | C-P3a 144 / 144 ; C-P3b 144 / 144 ; C-P3c « insertion » 144 / 144, « contenu » 108 / 108. Chaque case présente une fois et une seule, en première passe, à l'effectif du texte (1 000 essais et 1 000 tirages ; 8 000 essais) ; aucune sortie hors liste ; la liste est le produit complet 8 × 3 × 2 × 3. 58 cases neuves pour C-P3a et C-P3b, 48 pour C-P3c, 86 + 96 = 182 reprises ; l'origine de chaque sortie est celle de la colonne « jouée » de la liste | `./controles/couverture_independante.py`, sortie `./controles/sortie-couverture-independante.txt` : « problemes : aucun » ; garde de l'agent rejouée (cas sain et quatre artefacts : conformes) |
| Reprises « à l'identique » | Les 182 sorties reprises sont identiques à l'octet aux sorties d'origine du 19 novembre (branche `claude/papier-c-preenregistrement-v1`, commit `48e08c72`), que j'ai extraites moi-même ; les trois programmes de v1, les quatre fichiers d'archive et la liste finie aussi ; listes d'empreintes de v1 conformes (`9ab5c8a8…`, `c5bc961a…`) ; rapport v1 `8d1616fc…` et sa contre-lecture `d0485a40…` conformes | `cmp` fichier par fichier, 182 sur 182 ; `sha256sum -c` |
| Trois programmes copiés sous nom neuf | Différences lues ligne à ligne (`diff`) : (1) `grille_commun_v2.py`, une seule ligne de calcul, le code de T dans l'identifiant de case ; (2) `grille_ab_v2.py`, compteurs seulement ; (3) `grille_c_v2.py`, règle « D₀ ≤ 0 compte non établie » et compteurs. Aucune ne tire de nombre au hasard : le flux de hasard est celui de v1. Le rapport les décrit exactement | section 3 ci-dessous |
| Graines | Sous la règle de v1, une case à 30 tâches aurait eu la graine de la case à 60 tâches de mêmes modèle, attaque et nombre de niveaux : vrai (lu au code). Sous v2 : 288 sorties, 288 graines distinctes ; chaque graine écrite dans une sortie est celle de la formule du rapport ; les 106 états de contrôle du manifeste du lot sont ceux que `numpy.random.SeedSequence` redonne | `./controles/couverture_independante.py` ; contrôle du manifeste (section 5) |
| Reproductibilité | **25 rejeux avec la graine de la case, 25 identiques** à la sortie versée, tous champs sauf la durée : 19 rejeux de cases neuves (11 pour C-P3a et C-P3b, dont la case 097 deux fois ; 8 pour C-P3c) et 6 de reprises (3 et 3), dont la case du plus haut taux de chaque ligne et de chaque bras (005, 097, 111, 003) et les trois cases de C-P3b proches du seuil | `./rejeu/`, `./rejeu-compteur-r/` ; section 4 |
| Calcul hors de `.venv` (numpy 2.5.3) | **Acceptable** (remarque m-6) : quatre cases rejouées sous numpy 2.4.6, taux identiques | `./rejeu-numpy-2.4.6/` |
| Manifestes hors de `runs/` | **Acceptable** (remarque m-7) : champs de R9 présents, graines vérifiées | section 5 |
| Appariement des témoins sur la configuration à sceller | **Non faisable aujourd'hui** : cette configuration n'existe pas encore (verrou 4 du texte). Contrôle indicatif fait : appariement identique sur les brouillons 2, 3, 4 et 5 de la configuration (remarque M-1) | `./controles/appariement_configs.py`, sortie `./controles/sortie-appariement-configs.txt` |
| Application de la clause | Seuil recalculé (0,063784 ; 0,054873) ; « strictement au-dessus » ; trois lectures jointes ; première passe seule ; pour C-P3c, les deux bras de la liste (trois niveaux du plaidoyer, gain lié au g de la case). Tables du rapport et annexe A égales à mes taux, case par case (144 lignes, 0 écart) ; tableaux par modèle des sections 6.1 et 6.2 recalculés : exacts | section 6 |

## 3. Les trois programmes

- **Identifiant de case.** v1 : `k × 10 + (0 si T = 45, sinon 1)`. v2 : `k × 10 + {45 : 0, 60 : 1, 30 : 2}`, erreur
  pour tout autre T. Pour 45 et 60 tâches l'identifiant est inchangé : les dix cases neuves du modèle d'erreur
  homogène 0,4 à 45 et 60 tâches ont donc la graine que v1 leur aurait donnée, et les reprises restent rejouables
  par v1 comme par v2. Le code 2 pour 30 tâches a été fixé avant qu'aucun taux à 30 tâches n'existe : il n'offre
  aucune prise à un choix d'après un résultat. La correction était nécessaire : sans elle, dans chacun des deux
  programmes, 48 paires de cases auraient partagé leur flux de hasard.
- **Règle « D₀ ≤ 0 chez un juge : non établie »** (règle (iii) de lecture du rapport). Codée dans `grille_c_v2.py`
  sur les lectures sans insertion déjà tirées, sans tirage neuf ; appliquée à tous les bras qui emploient D₀.
  Compté : 0 essai sur 48 × 8 000. Pour les 96 reprises, que v1 ne comptait pas, la borne du rapport est juste :
  D₀ est une moyenne gaussienne de moyenne 2 et d'écart type au plus √(2/45) = 0,211, soit 9,5 écarts types de 0.
- **Compteurs** (valeurs non finies ; égalités exactes). Tous à 0 dans les 106 cases neuves ; le compteur
  d'ex æquo de v1 est à 0 dans les 96 reprises de C-P3c. Les rangs ordinaux et le τ de forme a des programmes
  donnent donc ici ce que donnent les rangs moyens et le τ de forme b du texte (précision 8).
- **Gel.** Les programmes de calcul du versement de sûreté fait pendant le lot (commit `24f4b275`, 20:30:53Z, avant
  la fin de la première partie du lot) sont identiques à ceux du versement final : entre les deux commits, vingt
  fichiers ajoutés sous `programmes/`, `entrees/` et `archive/` (compagnons et programme de tables), aucun modifié.

## 4. Rejeu

Interpréteur `/usr/local/bin/python3` (python 3.13, numpy 2.5.3), quatre processus, programmes et archive copiés
hors du dépôt (empreintes égales). Reprises rejouées par les programmes de v1, cases neuves par ceux de v2.
Comparaison : tous les champs de la sortie, sauf `duree_s`.

| lot | cases | résultat |
|---|---|---|
| `./rejeu/` — C-P3c, neuves | 001, 019, 073, 091, 109, 133 (modèles E30, E40, K16, KH, MH sans attaque ; M616 à g = 0,10), k = 3, T = 30 | 6 identiques |
| `./rejeu/` — C-P3c, reprises | 111 (plus haut taux du bras « insertion »), 003 (plus haut taux du bras « contenu »), 065 | 3 identiques |
| `./rejeu/` — C-P3a et C-P3b, neuves | 097 (plus haut taux de C-P3b), 001, 022, 021, 023, 073, 121, 130 | 8 identiques |
| `./rejeu/` — C-P3a et C-P3b, reprises | 074 et 093 (proches du seuil pour C-P3b), 005 (plus haut taux de C-P3a) | 3 identiques |
| `./rejeu-compteur-r/` — rejeu complet avec un compteur ajouté (remarque m-1) | C-P3a et C-P3b : 097, 037, 142 ; C-P3c : 037, 127 | 5 identiques |

Soit 25 rejeux pour 24 sorties distinctes (la case 097 de C-P3a et C-P3b est rejouée deux fois, par deux voies) :
18 sorties neuves et 6 reprises, au-delà des dix et cinq demandées. Début 21:05:55Z, fin 21:13:54Z ; fichiers
d'erreurs vides. Les programmes rejoués sont ceux du versement (`./rejeu/empreintes-programmes-rejoues.txt`).

## 5. Calcul hors de `.venv`, manifestes hors de `runs/`

- **numpy 2.5.3 au lieu de 2.4.6.** La consigne ne cite `.venv` que pour le scellement. Les 182 sorties de v1
  portent numpy 2.5.3 : jouer les cases neuves sous la même version tient la grille entière sous une seule version,
  ce qui vaut mieux que deux. Essai de sensibilité : dans un environnement neuf à numpy 2.4.6, quatre cases rejouées
  (C-P3c : 133 neuve et 111 reprise ; C-P3a et C-P3b : 097 neuve et 074 reprise) donnent des sorties identiques
  hors durée et champ de version. L'écart E1 du rapport est sans effet sur un taux.
- **Manifestes sous `G/manifestes/`.** L'agent n'avait pas le droit d'écrire sous `runs/`, et la fonction du dépôt
  dérive les graines du nom des tâches, ce qui aurait rompu la règle de graines de v1 et donc la reprise des
  182 sorties. Les champs de R9 y sont (configuration et empreinte, versions, graines, commit, commande, réserve
  d'arbre non propre). Contrôlé : 106 graines, 106 clés distinctes, 106 états de contrôle exacts, clés égales à
  celles des sorties. Acceptable ; si la mère veut tenir la convention « un manifeste par run sous `runs/` », une
  ligne de renvoi au versement suffit, sans rien rejouer.

## 6. Application de la clause, ligne par ligne

Clause : un taux de « établie » strictement au-dessus de 0,05 + 2 × √(0,05 × 0,95 / R) dans au moins une case de la
liste, toutes lectures jointes, première passe seule, sans correction pour le nombre de cases.

- **C-P3a.** Les cinq plus hauts taux : 0,049 (005), 0,048 (001), 0,046 (132), 0,046 (129), 0,043 (096). Aucun à
  moins de deux erreurs de Monte-Carlo de 0,0638. La clause ne joue pas, et de loin.
- **C-P3b.** Les cinq plus hauts : 0,056 (097), 0,053 (074), 0,051 (093), 0,049 (080), 0,049 (075). Aucun
  au-dessus de 0,0638 : la clause ne joue pas, à la lettre. **Réserve (R4), que le rapport écrit déjà et que je
  confirme** : sous la compression seule, C-P3b est au niveau nominal. En prenant les taux observés pour les taux
  vrais, un rejeu indépendant des 144 cases donnerait en moyenne 0,4 dépassement, et au moins un dans environ un
  rejeu sur trois (C-P3a : un sur vingt). Ce calcul surestime un peu, puisqu'il part des cases les plus hautes. Il
  ne change rien à l'issue : le texte ne lit que la première passe, chaque case a été jouée une fois, et aucun
  rejeu ne lève ni ne crée un dépassement. Il dit seulement que « clause passée » pour C-P3b tient à la graine
  autant qu'au niveau, ce que le directeur doit savoir en lisant le constat. Mes deux rejeux de la case 097
  redonnent 0,056 exactement : ce sont la même graine, non une seconde passe.
- **C-P3c.** Sans attaque, tous les modèles où la lecture sans insertion porte une erreur passent le seuil dans les
  deux bras, entre 0,076 et 0,107. La cause est dans la définition de la statistique : les deux gains d'écart d'un
  même juge partagent la cellule S et D₀, donc deux des quatre évaluateurs ne sont pas indépendants et la valeur p
  exacte ne tient plus son niveau. Vérification d'ordre de grandeur, à la main : si deux des quatre évaluateurs
  étaient toujours d'accord, W ≥ 0,8125 aurait une probabilité de 5/36 = 0,139 au lieu de 0,0417 ; une liaison
  partielle donne des taux entre les deux, comme observé. Sous la compression homogène sans erreur sur la lecture
  sans insertion, rien ne passe (au plus 0,050), ce qui est cohérent avec ce mécanisme. La clause joue, sans
  dépendre des cases proches du seuil.

## 7. Remarques

### Majeure

**M-1 — Le contrôle de l'appariement des témoins sur la configuration à sceller reste à faire, au scellement.**
Le texte lie l'issue à ce contrôle : si l'appariement diffère sur les longueurs de la configuration à sceller et
que la liste n'est pas rejouée, l'issue 3 s'applique. L'agent ne l'a pas fait (limite L1 du rapport), et personne
ne peut le faire aujourd'hui : la configuration à sceller n'est pas écrite (verrou 4 du texte ; le brouillon 5 est
un premier jet non contre-lu). Contrôle indicatif, par un programme à moi qui ne lit que les longueurs :
l'appariement des seize témoins, pour les indices 1, 8, 16 et 1, 4, 8, 12, 16, est **identique** sur les
brouillons 2 (`77252564…`), 3 (`85173b22…`, celui de la grille), 4 (`6734fbd0…`) et 5 (`f8f21fec…`) ; les
longueurs des témoins et des formulations à ces indices y sont les mêmes. **À faire** : rejouer ce programme sur le
fichier scellé `prereg/papier-C-config-v1.json` le jour du scellement, et citer sa sortie à côté du constat (il
prend les fichiers en arguments et rend le code 1 si un appariement diffère ; essayé sur un cas sain et sur un
artefact, une longueur de témoin changée : « au moins un appariement diffère », code 1). Tant
que ni les témoins ni les formulations de ces indices ne changent de longueur, rien n'est à rejouer.

### Mineures

**m-1 — La précision 3 du texte n'est ni codée ni dite au rapport.** Le texte dit que si r̂ ≤ 0 la troisième
lecture n'est pas définie et que la statistique ne peut alors pas être « établie ». Les programmes bornent le
quotient ρ̂/r̂ à [0,05 ; 1] et continuent. La section 3 du rapport nomme trois règles du texte non codées par v1 ;
celle-ci est la quatrième. Mesuré par un rejeu complet avec un compteur, sans toucher au flux de hasard
(`./rejeu-compteur-r/`, sorties identiques aux sorties versées) : **0 cas** sur 18 000 000 de tirages et
66 000 estimations observées, dans cinq cases à 30 tâches choisies pour leur bruit (erreur 0,6, mélange, compression
hétérogène) ; plus petit r̂ observé : 0,62. Sens de l'écart, s'il se produisait : le programme compterait
« établie » là où le texte l'interdit, donc un taux plus haut que celui du texte ; pour C-P3a et C-P3b cela ne peut
que charger la clause, non la lever. Sans effet sur l'avis. Correction proposée : une phrase d'erratum au rapport.

**m-2 — Le compteur d'égalités de C-P3a et C-P3b ne regarde que les égalités entre juges d'une même famille.**
C'est ce qu'il faut pour le W de C-P3a ; le τ de C-P3b porte sur quinze valeurs, toutes familles confondues. Les
grandeurs sont continues : une égalité exacte entre deux familles a une probabilité nulle. Sans effet.

**m-3 — Dans les 182 reprises, les valeurs non finies ne sont pas comptées** (v1 ne les comptait pas). L'argument
du rapport tient : le dénominateur de la forme fermée est une somme de carrés, nulle seulement si toutes les
lectures sont égales. Les 106 cases neuves en comptent 0. Sans effet.

**m-4 — L'heure du gel du programme de tables n'est attestée que par le journal.** Ce programme n'est pas dans le
versement de sûreté de 20:30:53Z ; les programmes de calcul y sont. Sans effet : j'ai refait les tables sans lui.

**m-5 — « 198 sorties » de v1** (section 2 du rapport) : je compte 190 sorties de calcul (182 premières passes de
la liste, 6 cas d'effet, 2 secondes passes), 190 fichiers d'erreurs vides et 8 autres fichiers. Mot à préciser.

**m-6 — Calcul hors de `.venv`** : acceptable, voir section 5.

**m-7 — Manifestes hors de `runs/`** : acceptable, voir section 5. Détail : l'identifiant du lot porte l'heure
20:30:00 alors que le manifeste est créé à 20:28:35.

**m-8 — Lecture des taux de v1 avant l'écriture des programmes v2** (écart E3 du rapport) : inévitable, puisque la
consigne fait lire le rapport v1 ; les trois changements sont mécaniques et aucun ne dépend d'un taux. Acceptable.

**m-9 — La mesure du temps a joué trois cases de la liste sur une autre graine avant le lot** (passe 9). Ce ne
sont pas des passes au sens du texte : 400 et 40 essais, non l'effectif fixé. Je n'ai pas ouvert leurs taux.

### Corrections et suite

Aucune remarque bloquante n'est ouverte. Si la mère fait porter m-1 et m-5 par un erratum du rapport, je le
vérifie sur demande (même contre-lecteur, comme le texte l'exige) ; sans erratum, le rapport v2 est citable tel
quel, avec cette contre-lecture, et la condition M-1 se lève au scellement.

## 8. Symétrie (R3, R4)

Aucun taux n'était visé par cette contre-lecture ; j'ai cherché ce qui pouvait renverser chaque avis dans les deux
sens. Pour C-P3a et C-P3b, ce qui aurait pu créer un dépassement caché : une case manquante ou jouée deux fois, un
effectif réduit, une graine partagée, une règle du texte non codée qui baisserait les taux. Rien de tel : les
écarts au texte que j'ai trouvés (m-1, m-3) ne peuvent que monter les taux. Pour C-P3c, ce qui aurait pu créer un
faux dépassement : la règle sur D₀ mal codée, une égalité de rangs, un bras hors liste pris pour un bras de la
liste. Rien de tel non plus, et les dépassements sans attaque sont à plus de sept erreurs de Monte-Carlo.
L'absence de tout dépassement pour C-P3a et C-P3b n'est pas « trop propre » : la plupart des taux sont nettement
sous 0,05 parce que la conjonction de trois lectures est sévère ; elle l'est moins sous la compression seule, où
C-P3b frôle le seuil, ce que la section 6 dit.

## 9. Écarts de ma procédure

- La routine de reprise est faite en partie : empreintes de lancement conformes ; la vérification de l'arbre scellé
  rend 96 problèmes, tous hors des dossiers du papier C, donc hors de ce mandat (à la mère) ; ni l'inventaire des
  instances de calcul ni la suite d'essais complète du dépôt n'ont été faits (session sans calcul loué, économie
  d'usage demandée).
- La ligne GO-2026-11-22-125 n'est pas sur la branche de la pièce : lue sur `main` (commit `466bccd9`). Lecture
  incidente, par la même recherche, des lignes GO-2026-11-22-106, -114 et -118 ; et des titres et corps des
  demandes de fusion 72 à 76 du dépôt, en vérifiant l'usage avant d'ouvrir la mienne. Aucun résultat d'expérience.
- La liste « qui a lu quoi » v21 n'est pas sur ma branche : colonnes prises de la v19.
- Mes programmes de contrôle sont de classe C, non contre-lus ; ils sont versés pour être rejoués.

## 10. Ce que j'ai lu

`CLAUDE.md` ; liste « qui a lu quoi » v19 (puces de tête, en-tête du tableau, ligne 323) ; la consigne de l'agent
(`37ee2527…`) en entier ; le rapport v2 : sections 1 à 10 en entier, annexe A lignes 001 à 034 à l'écran et les
144 lignes par programme ; les programmes `grille_commun_v2.py`, `grille_ab_v2.py`, `grille_c_v2.py` en entier, les
différences avec v1, `lancer_v2.sh`, `mesure_temps_v2.sh` ; de l'archive, `commun_b5_v1.py` (lignes 1 à 140) et les
fonctions de rang de `t2_rang_temoins_partages_v1.py` ; le journal de l'agent ; le manifeste du lot (par
programme) ; la liste finie (sections 1 à 3 et 5, tête de la table, la table par programme) ; toutes les sorties,
par programme. Texte c5 (`0747f357…`) : verrou 4 (lignes 379 à 392), verrou 10 (474 à 494), bloc de la stabilité de
rang (937 à 1069), point 8 bis de la Métrique (1189 à 1200), précisions 3, 5, 8, 36 et 37 (jusqu'à la ligne 2143) ;
son erratum 1 (`78cc1127…`) en entier. Du 19 novembre : contre-lecture du rapport v1 (`d0485a40…`), sections 2, 4
et 9 et les remarques CG-08 et CG-10 ; rapport v1 : empreinte seulement ; sorties de v1 : comparées à l'octet.
Brouillons 2, 3, 4 et 5 de la configuration : longueurs seulement, par programme. **Non ouverts** : `diag/`,
`runs/`, `donnees/`, `docs/verdicts/` ; tout résultat d'expérience réelle ; les taux des sorties de la mesure du
temps ; le rejeu du rédacteur du 19 novembre ; les notes des deux juges du nœud H-1.

## 11. Pièces de cette contre-lecture

| pièce | chemin |
|---|---|
| contrôle indépendant de la couverture, des graines, des seuils et des taux | `./controles/couverture_independante.py`, `./controles/sortie-couverture-independante.txt` |
| contrôle de l'appariement sur quatre brouillons de la configuration (empreintes des fichiers lus dans la sortie) | `./controles/appariement_configs.py`, `./controles/sortie-appariement-configs.txt` |
| rejeu de 20 cases | `./rejeu/cases.txt`, `./rejeu/sorties/`, `./rejeu/sortie-comparaison.txt`, `./rejeu/empreintes-programmes-rejoues.txt` |
| rejeu de 5 cases avec le compteur de r̂ ≤ 0 | `./rejeu-compteur-r/compte_r.py`, `cases.txt`, `sorties/`, `compteurs/`, `sortie-comparaison.txt` |
| rejeu de 4 cases sous numpy 2.4.6 | `./rejeu-numpy-2.4.6/cases.txt`, `sorties/`, `sortie-comparaison.txt` |
| programmes de comparaison | `./controles/compare_rejeu.py`, `./controles/compare_numpy.py` |
| empreintes de toutes ces pièces | compagnons `.sha256` ; liste `./sha256sums-contre-lecture-grille-v2.txt` |
