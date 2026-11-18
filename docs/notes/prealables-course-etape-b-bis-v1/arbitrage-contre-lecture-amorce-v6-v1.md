# Arbitrage des quatre contre-lectures de la chaîne de lancement version 6 de la course de l'étape B bis (apprentissage des sondes sur la tâche, T0.7) — v1

- **Arbitre** : sous-agent neuf. Je n'ai écrit aucune des pièces, ni aucune des quatre contre-lectures.
- **Date (UTC, `date -u`)** : 2026-11-18, de 04:50Z à 05:15Z environ. Processeur seulement. Aucune machine, aucune dépense,
  aucun appel au loueur, aucune valeur de clé lue, aucun commit, aucune poussée. Les rejeux tournent sans réseau
  (`unshare -n -r`), avec un `HOME` jetable dont la configuration de git ne signe pas, dans
  `/tmp/claude-0/-home-user-controle-ia-travail/8282ab93-0983-5813-b791-a7a522157dcd/scratchpad/cl-amorce-v6-arbitre/`. Le
  clone jetable a été effacé après usage ; les sorties de mesure sont gardées.
- **Pièces arbitrées, empreintes relues sur le disque** :
  - amorce version 6, `scripts/amorce_bbis_v6.sh` : `26f954e9e9783bf95a5149db9e848e1bd207dc8b027e6027d879363be2dfbbb5` ;
  - lanceur version 6, `scripts/lancer_bbis_v6.sh` : `3224ce14dc3fefe7cc46774072f65288a39c3fe760f325e311c5f948c45344b7` ;
  - essais, `tests/test_chaine_bbis_v6_v1.py` : `f36571bd7fb7f5693f8e45433f44c7826722b9baf995ce219038923d486b49ca` ;
  - brouillon 1 du troisième addendum, `brouillons/T0.7-etape-B-bis-v1/addendum-ecart-3-brouillon1.md` :
    `0056edaa66b20c2e5b40cfecf7ef9752834ae68c76db9e2cf4c3cc7efe75b58d`.
- **Rapports arbitrés**, tous sous `docs/notes/prealables-course-etape-b-bis-v1/`, chacun conforme à son compagnon :
  - angle « gardes », `contre-lecture-amorce-v6-gardes-v1.md` : `779ed714…f8db198` ;
  - angle « conformité au texte scellé », `contre-lecture-amorce-v6-conformite-v1.md` : `84abdb49…1668c7e` ;
  - angle « la course sur la vraie machine », `contre-lecture-amorce-v6-machine-v1.md` : `ddca4e7c…217e6945c` ;
  - angle « adverse », `contre-lecture-amorce-v6-adverse-v1.md` : `1e7bd8ef…13a563c7`.
- **Version de la contre-lecture « conformité »** : le commit `1e90d43d` portait une version périmée du rapport (empreinte
  `58a02d07…`). Le commit `c1d68248` et la tête portent la version scellée (`84abdb49…`). La version périmée ne fait pas foi.
- **Cloisonnement tenu** :
  - rien d'ouvert sous `diag/`, `runs/` ni `donnees/`, aucune branche de données ni de calcul ;
  - aucun résultat de 7a, de 7b, de T0.6, de l'étape B, de l'étape B bis ni du premier test boîte blanche bis ;
  - du registre partagé des sceaux, je n'ai lu que la clé et l'heure de la ligne du verdict de l'étape B ;
  - des deux journaux de répétition sur jouet (`docs/notes/g0-deux-semaines-v1/t07-module-v2/…`, données fabriquées), je n'ai
    lu que les lignes de code de réponse de l'arrêt.

## Verdict d'ensemble : « à corriger »

La chaîne version 6 fait ce que le brouillon annonce, et rien d'autre. Elle ne demande ni une amorce ni un lanceur neufs. Elle
n'est pourtant pas bonne pour le feu en l'état, pour deux raisons :

1. **Un bloquant de machine, confirmé** : rien n'écarte les hôtes à pilote de carte récent (séries 610, 615 et 620). Un tel
   hôte arrête l'amorce à la première minute et consomme la dernière course. Le 16 novembre, l'offre la moins chère était
   justement à pilote 615.
2. **Un bloquant de texte, confirmé** : le brouillon tait un écart à la section « Seuil » du texte scellé. Il faut un brouillon 2
   de l'addendum.

Les majeurs confirmés se lèvent tous de trois façons, sans code neuf :

- par le brouillon 2 ;
- par deux mesures scellées : le plancher d'essais au commit exact de la course, sous Python 3.13 et sous Python 3.11 ;
- par des gestes exécutables du feu version 4.

Un lanceur version 7 reste possible, mais il n'est pas exigé. Il demanderait sa propre contre-lecture, alors que l'échéance de la
ligne d'accord tombe le 22 novembre.

**Corrections exigées avant le feu** :

1. Écrire au feu l'hôte à pilote de série 595 ou 580, choisi par programme dans la sortie brute de la recherche d'offres.
2. Écrire un brouillon 2 de l'addendum, qui déclare l'écart à la clause « lue avant toute ouverture de données de 7b ».
3. Faire porter au brouillon 2 les sept autres corrections de texte : entropie, préséance, écart depuis la version 4, code hors
   de la fiche, accord, lecture de la liste d'arrêt, antériorité.
4. Comparer au feu, sur 64 caractères, les empreintes de l'amorce embarquée et du lanceur à l'addendum scellé et inscrit.
5. Remesurer le plancher au commit exact de la course, sous Python 3.13 **et** sous Python 3.11 : exactement 151 passés et 25
   sautés, sorties scellées.
6. Calculer l'échéance par commande, à 13 heures au plus.
7. Lire le journal de la machine dans les cinq minutes, sinon la détruire par son identifiant.
8. Reporter au feu version 4 les conditions du feu version 3 qu'il faut garder, et y corriger celles qui ont changé.
9. Faire trancher par la mère, avec citation au feu, le passage des deux clés à la machine.

Le détail suit.

## Tableau des points (bloquants et majeurs des quatre rapports, doublons fusionnés)

| n° | point | angle(s), gravité annoncée | statut de l'arbitre | gravité retenue | preuve de l'arbitre |
|---|---|---|---|---|---|
| 1 | Hôte à pilote récent non écarté : l'amorce ne lit que « CUDA Version: », or le pilote 615 affiche « CUDA UMD Version: 13.4 » | machine, bloquant | **confirmé** | bloquant (levé au feu) | (a) le bloc `cuda-du-pilote` extrait de l'amorce, joué sur une ligne au modèle du pilote 615.71.09, rend le code 1 (arrêt) ; sur « CUDA Version: 13.2 », il rend « 13.2 ». (b) Aucune occurrence de `driver` dans `src/controle_ia/t07bbis/registre_bbis_v2.py` ni dans le lanceur. (c) Le projet de feu version 3 (`projet-de-feu-v3-non-en-vigueur.md`, l. 39) ne pose que `cuda_max_good` ≥ 13.0. (d) La condition existe ailleurs : le troisième feu du 16 novembre exigeait la série 595 ou 580 (`registres/decisions.md`, R-3003, l. 2963). (e) Le même jour, « les offres moins chères étaient […] à pilote 615 » (R-3004, l. 2964). (f) L'arrêt réel est consigné dans `registres/arrets.md`, l. 133 (instance 60952525). |
| 2 | Écart à la section « Seuil » non déclaré : l'épreuve de niveau en vigueur a été jouée après l'ouverture des données de 7b | conformité, bloquant | **confirmé** | bloquant (texte seulement ; risque de fond nul) | (a) Texte scellé, `prereg/T0.7-etape-B-bis-v1.md`, l. 93 : épreuve « lue **avant toute ouverture de données de 7b** ». (b) Épreuve rejouée versée au commit `d75587c8` le 2026-11-17 à 11:03:40Z (`git log` du fichier de l'épreuve). (c) La relance du 16 novembre a tourné de 17:25Z à 21:35Z avec relecture des données de 7b (`registres/arrets.md`, l. 134-135). (d) Le brouillon, l. 24-25, dit ne toucher « aucune ligne » de « Seuil ». L'épreuve ne lit que des données fabriquées : seule la lettre est enfreinte. |
| 3 | Rien d'exécutable ne lie l'amorce et le lanceur qui partent aux empreintes que l'addendum rattache | gardes M1, adverse M1, conformité M7 ; majeur | **confirmé** | majeur | Rejoué dans le clone jetable : `MIN_ESSAIS=151` remplacé par `MIN_ESSAIS=1` dans l'amorce (empreinte devenue `8eaa02ce…`). Les deux essais de la commande de création passent quand même (2 passés) : la commande est imprimée, code 0. `grep` de `ADDENDUM`, `addenda` et `26f954e9` dans le lanceur : aucune occurrence. La seule empreinte calculée (l. 167) est coupée à 16 caractères, pour l'œil seulement. |
| 4 | Le plancher d'essais n'est pas une porte de la commande de création ; marge nulle | gardes M2, adverse M2 ; majeur | **confirmé** | majeur | La sous-commande `essais-du-commit` n'est appelée par aucune autre (`lancer_bbis_v6.sh`, l. 137-169 contre l. 170-186). Ma mesure à la tête `97da9246277cd8f1d76630dfe397a18d16696ecb` (la branche `main` a avancé trois fois pendant l'arbitrage) : « 151 passed, 25 skipped », code 0, 516 fichiers. Liste des fichiers identique à la preuve du développeur (`d48e74d3…`). Sorties : `mesure-tete-sortie.txt` `17b481c5…`, `mesure-tete/essais.txt` `e1f27773…`, dans le dossier jetable. |
| 5 | Plancher jamais mesuré sous le Python 3.11 de l'image | machine M3 ; majeur | **manque confirmé ; effet plausible, non tranché** | majeur | `/usr/bin/python3.11` est présent, sans numpy, torch ni pytest. Je n'ai pas pu installer de paquets (pas de réseau). Deux contre-lecteurs n'ont compilé la syntaxe que sous 3.11. La course du 16 novembre a joué ses essais sous 3.11 avec l'ancien jeu de 115 ; les essais du second addendum n'y ont jamais tourné. |
| 6 | Échéance de la minuterie non bornée côté session : l'essai local de l'amorce sort avant le contrôle de la fenêtre ; 24 h permises | machine M1, adverse M3 ; majeur | **confirmé** | majeur | Rejoué : amorce en essai local avec des échéances de 1, de maintenant − 1 h, de maintenant + 30 jours et de maintenant + 24 h. Code 0 dans les quatre cas (l. 131 avant l. 133). Le lanceur ne vérifie que la forme (l. 141). Calcul : 24 h × (1,40 + 0,08) USD/h ≈ 35,52 USD, au-dessus de la marge sous la coupure (39,50 − 5,99 ≈ 33,51 USD) ; 13 h × 1,48 ≈ 19,24 USD. Le projet de feu version 3 (l. 57) compte 18,20 USD, sans le stockage. |
| 7 | Les refus d'avant la minuterie quittent en code 2 sans minuterie ni demande d'arrêt | machine M2, adverse M4 (b), gardes mineur 7 ; majeur | **confirmé par le code ; relance en boucle plausible** | majeur | `amorce_bbis_v6.sh`, l. 116-138 : `exit 2` sans `fin_instance`. Le loueur a déjà relancé en boucle un conteneur sorti (`registres/arrets.md`, l. 120, instance 60671759 ; autre chaîne). La commande de création redécode et rejoue l'amorce à chaque démarrage du conteneur. |
| 8 | La garde neuve de la clé d'interface du conteneur pourrait arrêter une course saine si le loueur ne la pose pas dans ce mode de lancement | adverse M4 (a), gardes mineur 7 ; majeur | **réfuté pour l'essentiel** (preuve indirecte) ; reste la clé faite d'espaces (mineur) | mineur | Les machines de T0.6 sont lancées par `scripts/lancer_t06_v*.sh`, tous en mode `--entrypoint bash`. Leurs amorces `scripts/amorce_instance_t06_v*.sh` s'arrêtent et se détruisent par `CONTAINER_API_KEY`. Le registre des arrêts consigne 59623267 « arrêtée (« stopped ») par l'amorce » et 59598117 « détruite par la minuterie » (`registres/arrets.md`, l. 86-87). Ces deux gestes exigent la clé. Le risque résiduel est couvert par la lecture du journal du point 7. |
| 9 | Le texte de l'entropie (TA-3) laisse le texte en vigueur se contredire et garde au présent une prédiction sans appui | conformité M1 ; majeur | **confirmé** | majeur | Second addendum, l. 507-508 : « même entropie que la fiche […] » puis « l'entropie est celle que porte la ligne `CODE-BBIS` en vigueur, non retirée ; conséquence, prédite avant la course : mêmes sondes […] ». Après TA-3 viendrait « même entropie […] **non reprise** ». |
| 10 | L'en-tête du texte scellé dit que le code de la course (scripts de lancement compris) est cité par `CODE-BBIS` ; le brouillon n'a pas de règle de préséance | conformité M2 ; majeur | **confirmé** | majeur | Texte scellé, l. 5 (code « cité […] par la ligne `CODE-BBIS` ») et l. 227 (« Code neuf », dont `scripts/lancer_bbis_v1.sh` et son amorce). Brouillon, l. 21-23 : « Toute autre phrase de T, de A1 et de A2 fait foi telle quelle ». Le second addendum avait une telle règle (l. 23). |
| 11 | L'écart déclaré part de la version 5, jamais déclarée ; l'écart au texte va de la version 4 à la version 6 (plancher 148 → 151) | conformité M3 ; majeur | **confirmé** | majeur | `diff` des amorces 4 et 5 : seulement `MIN_ESSAIS=148` devenu `176` ; `diff` des lanceurs : 16 lignes, des noms seulement. Le passage à la version 5 est inscrit comme « recompte » (R-3074, `registres/decisions.md`, l. 3049), sans addendum. Le second addendum, l. 546, dit « liste le code v4 ». |
| 12 | La raison de TA-2 est fausse en général : le code hors de la fiche (les fichiers réutilisés de la l. 19 du texte scellé, `requirements-gpu.txt`) n'est gardé par rien au commit de la course | conformité M4 ; majeur | **confirmé** (état conforme à ce jour) | majeur | La fiche en vigueur ne cite, sous `src/`, que `src/controle_ia/t07bbis/` (63 fichiers ; aucun autre chemin de `src/`). `git diff --quiet 05cd22aa 97da9246 -- src requirements-gpu.txt pyproject.toml tests/conftest.py 'tests/test_t07bbis_*' 'tests/aide_t07bbis_*'` rend le code 0. Les onze empreintes relevées l. 19 sont égales au disque. Rien n'arrêterait un écart futur. |
| 13 | Qui accorde l'écart : le brouillon dit Lazar ; la décision d'autonomie dit la mère, pour une pièce libellée autrement | conformité M5 ; majeur | **confirmé** | majeur | GO-2026-11-18-04 (`registres/go.md`, l. 368) : « reste à accorder par Lazar sur pièce » ; c'est la **lecture de la mère**, non le verbatim de Lazar. R-3170 (8) (`registres/decisions.md`, l. 3262) : « accordé par la mère sous ce GO, sur pièce, seulement après contre-lecture […] rendue sans bloquant », pour « code neuf, fiche de code neuve, épreuve rejouée ». La version 6 n'écrit aucune fiche neuve. Le brouillon ne cite ni GO-2026-11-18-05 ni R-3170. |
| 14 | La liste d'arrêt accorde la course unique « sous ce texte et ses deux addenda », « sous le second addendum » | conformité M6 ; majeur | **confirmé** | majeur | Second addendum, l. 142 et l. 305, verbatim. |
| 15 | L'antériorité (§ 5) tait le verdict de l'étape B et la course du 16 novembre | conformité M8 ; majeur | **confirmé** | majeur | La ligne du verdict de l'étape B au registre des sceaux est datée 2026-11-17T11:20:08Z (clé et heure seulement). L'épreuve a été versée à 11:03:40Z et la fiche à 11:07:47Z (commit `c098fb51`). Niveau inchangé (0,99) : la règle de la liste d'arrêt, l. 180, n'est pas déclenchée, mais le brouillon ne l'écrit pas. |
| 16 | Le feu version 4 doit nommer plus que les six points du brouillon (§ 7, point 5) | machine M4 ; majeur | **confirmé** ; deux des sept points sont déjà au projet de feu version 3 et sont à reporter, non à ajouter | majeur | Voir le détail sous le tableau. |
| 17 | Hors pièces : la commande passe deux clés à la machine (jeton de la plateforme de modèles et jeton GitHub), alors que GO-2026-11-18-05 laisse à Lazar « le passage d'une clé à une machine » | adverse, limites | **plausible, non tranché** | à trancher par la mère avant le feu | La ligne de la décision d'autonomie le dit verbatim. GO-2026-11-14-09 ne nomme aucune clé. Les feux du 16 novembre ont passé ces deux mêmes clés sous GO-2026-11-14-09, avant la décision d'autonomie. |

**Détail du point 16** :

1. **Pilote** de série 595 ou 580 : à ajouter (point 1 du tableau).
2. **Échéance** calculée par commande et pire cas avec le stockage : à ajouter (point 6).
3. **Jeton GitHub de la machine**, pris de `CONTROLE_IA_GITHUB_TOKEN_2` par son nom (R-2829, R-2830, `registres/decisions.md`,
   l. 2789-2790) : à ajouter. Aucune occurrence de jeton dans le projet version 3.
4. **Crédit du loueur d'au moins 20 USD** : déjà au projet version 3 (l. 61-62). À reporter avec un relevé neuf : le dernier relevé
   inscrit est de 16,15 USD (`registres/depenses.md`, l. 489), sous le plancher.
5. **Outil du loueur réinstallé, option `-y` réprouvée** : déjà au projet version 3 (l. 93). À reporter : l'outil est absent de
   la session (`command -v vastai` ne rend rien).
6. **Plancher de 151 au lieu de 176** : à corriger. Le projet version 3 dit 176 aux l. 83, 94 et 107.
7. **`PYTHON_BBIS`** : à ajouter. Le `python3` du système de la session (3.13) n'a pas torch : faux refus, du côté sûr.
8. S'ajoute un point que le brouillon écrit lui-même mal : « seize caractères d'empreinte » doit devenir **64 caractères**.

**Mineurs des rapports.** Je ne les ai pas tous rejoués et je ne les classe pas plus haut, sauf deux que j'ai vérifiés :

- **Interpréteur de la garde « commit de la course »** (gardes, mineur 1) : il est lancé sans `-P` ni `-I` (`lancer_bbis_v6.sh`,
  l. 92). C'est sans effet si le lanceur est joué depuis la racine du dépôt, ce que le feu doit dire.
- **Signature des commits du dépôt jetable** (adverse, mineur 1) : elle produit un faux refus quand le réseau manque. C'est du côté
  sûr. Le feu joue le lanceur dans la session normale.

**Incidents de disque déclarés** par trois contre-lecteurs (vers 04:20Z, 04:31-04:35Z et vers 04:45Z), tous levés. La place libre
est de 15 Go à 05:08Z. La mère vérifie qu'aucune autre tâche n'a échoué en écriture dans ces fenêtres. Mon clone jetable a été
effacé.

## Corrections minimales

### A. Brouillon 2 du troisième addendum (texte seul ; à faire vérifier par un lecteur neuf, règle R2, puis à sceller et inscrire)

1. **Clause d'antériorité de l'épreuve** (point 2). Ajouter à la raison de TA-4 et TA-5 que l'épreuve `da9fa42b…` a été jouée le
   17 novembre et versée à 11:03:40Z. Elle vient donc après la course du 16 novembre, qui avait relu les données de 7b sans écrire
   de score. La clause « lue avant toute ouverture de données de 7b » n'est pas tenue à la lettre. L'épreuve ne lit que des
   données fabriquées, et le niveau décisif reste 0,99. Corriger aussi les l. 24-25 (« aucune ligne de « Seuil » »). Ajouter le
   point à l'accord demandé.
2. **Entropie** (point 9). Étendre l'« ancien » de TA-3 à tout le passage des l. 507-508 du second addendum. Écrire « entropie
   **changée** », citer les deux valeurs, et dire que la prédiction « mêmes sondes […] de l'ordre de 1 » a perdu son appui (réserve
   nommée au verdict, GO-2026-11-18-03 (1)). Revérifier l'unicité de l'« ancien » par programme et verser ce programme avec sa
   sortie (règle R6).
3. **Préséance** (point 10). Ajouter au § 0 : là où une phrase du texte scellé ou des deux addenda dit que le code de la course
   est cité par `CODE-BBIS`, cela vaut pour le code qui apprend, note et écrit (les 63 fichiers de la fiche), non pour le lanceur
   et l'amorce version 6, rattachés par le § 6 ; le troisième addendum fait foi.
4. **Écart depuis la version 4** (point 11). La version 5 (plancher 176) n'a été rattachée par aucun addendum (R-3074). L'écart
   net au texte va de la version 4 à la version 6, avec un plancher qui passe de 148 à 151. Joindre le `diff` de la version 4 à la
   version 6. Traiter « liste le code v4 » (second addendum, l. 546) et le complément orphelin « avec l'entropie ».
5. **Code hors de la fiche** (point 12). Corriger la raison de TA-2. Ajouter au § 4 que le code hors de la fiche (fichiers
   réutilisés de la l. 19 du texte scellé, `requirements-gpu.txt`, fichiers de la racine extraits par le motif `/*`) est pris au
   commit de la course sans garde. Le geste du feu B.4 le contrôle.
6. **Empreintes de la chaîne** (point 3). Ajouter au § 4 qu'aucune garde ne compare l'amorce et le lanceur version 6 aux
   empreintes du § 6. Ce contrôle est tenu par le feu (B.3). Remplacer « seize caractères » par « 64 caractères » au § 7.
7. **Accord** (point 13). Citer GO-2026-11-18-05 et R-3170 (8). Dire qui accorde, et sur quel texte. Nommer la pièce telle
   qu'elle est : chaîne hors de la fiche, aucune fiche neuve, TA-1 à TA-5, clause d'antériorité de l'épreuve, plafond de prix au
   lanceur. L'accord de la mère sous R-3170 (8) suppose une contre-lecture « sans bloquant ». Ce n'est pas le cas à ce jour :
   cela le devient quand le lecteur neuf du brouillon 2 n'en relève plus.
8. **Liste d'arrêt** (point 14). Déclarer, sans changer la phrase scellée, que « ses deux addenda » et « sous le second
   addendum » se lisent « sous le texte scellé, ses deux addenda et le présent addendum, qui ne touche aucune ligne de la liste
   d'arrêt ». Faire couvrir cette lecture.
9. **Antériorité** (point 15). Ajouter au § 5 :
   - l'heure du verdict de l'étape B (2026-11-17T11:20:08Z) ;
   - celles de l'épreuve (11:03:40Z) et de la fiche (11:07:47Z) ;
   - la course du 16 novembre ;
   - la phrase « niveau, seuils, cellules, grille, plis et adversaires inchangés : la règle de la liste d'arrêt, l. 180, n'est pas
     déclenchée ».
10. **Pilote** (point 1). Ajouter au § 4 que la garde d'offre ignore la version du pilote et que l'amorce ne lit pas « CUDA UMD
    Version: ». Le feu tient donc la condition de série 595 ou 580.

### B. Mesures et gestes avant le feu (sur processeur, sans dépense)

1. **Commit de la course fixé une fois**. La branche `main` avance de plusieurs commits par heure. Toutes les mesures qui suivent
   se font sur ce commit exact, qui doit porter l'addendum scellé et inscrit. La commande de création reçoit ce même commit.
2. **Plancher au commit exact, deux fois** (points 4 et 5). Jouer
   `PYTHON_BBIS=<interpréteur> bash scripts/lancer_bbis_v6.sh essais-du-commit RACINE COMMIT DOSSIER_NEUF` :
   - une fois avec `.venv` (Python 3.13) ;
   - une fois avec un environnement neuf `/usr/bin/python3.11 -m venv`, rempli de `requirements-cpu.txt` et de `requirements-donnees.txt` (le réseau des paquets
     est à la mère).
   Exiger les deux fois le code 0, **exactement** 151 passés et 25 sautés, et 516 fichiers d'une liste d'empreinte `d48e74d3…`.
   Sceller les deux sorties et les citer au feu. Tout écart arrête : on ne part pas.
3. **Empreintes de la chaîne** (point 3), dans le shell de lancement, avant la création :
   - `sha256sum scripts/amorce_bbis_v6.sh scripts/lancer_bbis_v6.sh`, comparé **en entier** au § 6 de l'addendum scellé ;
   - la ligne `ADDENDUM-ECART-3-BBIS` présente une fois au registre voisin, avec un fichier conforme à son compagnon ;
   - le base64 de la commande imprimée décodé (`… | base64 -d | sha256sum`) et comparé à `26f954e9e9783bf95a5149db9e848e1bd207dc8b027e6027d879363be2dfbbb5`.
   Un seul écart : arrêt, rien n'est créé. Sorties consignées.
4. **Code hors de la fiche** (point 12) : `git diff --quiet 05cd22aa <COMMIT> -- src requirements-gpu.txt pyproject.toml
   tests/conftest.py 'tests/test_t07bbis_*' 'tests/aide_t07bbis_*'` doit rendre le code 0. Comparer aussi à la l. 19 du texte
   scellé les empreintes des fichiers réutilisés, et `git ls-tree --name-only` de la racine à `05cd22aa`. Sortie consignée ;
   écart : arrêt.
5. **Passage des deux clés** (point 17) : la mère tranche et écrit sa lecture. Soit la course de GO-2026-11-14-09, dont l'amorce
   exige ces deux clés et que les feux du 16 novembre ont lancée avec elles, couvre ce passage ; soit c'est un nœud à porter à
   Lazar. Le feu cite la lecture retenue.

## Ce qui doit aller au feu version 4

Le feu version 4 remplace le projet version 3. Il reprend les conditions de celui-ci qui restent vraies, et ajoute ou corrige
ceci :

1. **Chaîne** : lanceur et amorce version 6, empreintes **entières** (`3224ce14…` et `26f954e9…`), comparées au § 6 de l'addendum
   scellé et inscrit (B.3). Lanceur joué depuis la racine du dépôt, avec `PYTHON_BBIS` posé (`.venv/bin/python`) pour
   `commande` et `essais-du-commit`.
2. **Commit de la course et branche de code `main`** : le commit exact de B.1, avec les deux mesures scellées du plancher (B.2),
   151 et 25, et la sortie du contrôle du code hors de la fiche (B.4).
3. **Offre** :
   - choisie par programme dans la sortie brute de la recherche d'offres (`offre-depuis-recherche`), jamais retapée ;
   - `driver_version` commençant par `595.` ou `580.`, recopié tel quel au registre des dépenses ; clé absente : arrêt. La
     série 595 est la seule éprouvée sur une vraie machine de cette course (595.91.07, instance 60953606) ;
   - `cuda_max_good` au moins 13.0, prix de carte au plus 1,40 USD/h (lanceur **et** opérateur), stockage au plus 0,08 USD/h,
     image `python:3.11-bookworm`.
4. **Échéance** :
   - calculée par commande au moment de la création, `ECH=$(( $(date +%s) + 46800 ))` (13 heures), et recopiée ;
   - refaite si la création attend plus d'une demi-heure après la commande ;
   - pire cas écrit avec le stockage : 13 h × 1,48 USD/h ≈ 19,24 USD ; cumul de la ligne au pire ≈ 25,2 USD sur la coupure de
     39,5 USD (coupure au reste de la ligne, ≈ 34 USD, en comptant les ≈ 5,99 USD déjà dépensés).
5. **Clés** : jeton GitHub de la machine `GH_TOKEN` pris de `CONTROLE_IA_GITHUB_TOKEN_2`, par son nom, dans le seul shell de
   lancement ; jeton de la plateforme de modèles par son nom ; lecture de la mère sur le passage des clés citée (B.5).
6. **Crédit** relevé dans l'heure qui précède la création, au moins 20 USD (dernier relevé inscrit : 16,15 USD) ; **outil du
   loueur** réinstallé, version inscrite, option `-y` réprouvée sur un cas sain.
7. **Lecture du journal dans les cinq minutes** qui suivent l'état « running ». Il faut y trouver :
   - la ligne « minuterie lancée » ;
   - la ligne « amorce v6 : empreinte » égale aux 64 caractères `26f954e9…dbbb5` ;
   - la ligne du pilote, « CUDA servie par le pilote : … ».
   À défaut, ou sur toute sortie de l'amorce avant la minuterie : destruction par l'identifiant avec `-y`, absence prouvée contre
   un témoin, compte rendu.
8. **Relances** : deux, la dernière course accordée. Une perte au démarrage la consomme : le feu le dit.
9. **Plancher** : 151, non 176, partout où le projet version 3 le nomme (l. 83, 94, 107).
10. **Réserves à écrire au feu** :
    - le plafond de prix tenu aussi par le lanceur, contre la lettre de GO-2026-11-18-03 (3) ;
    - l'image exigée par son nom, non par un condensé ;
    - l'amorce embarquée de 41 436 caractères en base64, taille jamais éprouvée chez le loueur ; le journal (point 7) la couvre.

Une vérification courte du brouillon 2 et du feu version 4 par un lecteur neuf, sur les seuls points ci-dessus, précède le
scellement de l'addendum, l'accord et le feu.
