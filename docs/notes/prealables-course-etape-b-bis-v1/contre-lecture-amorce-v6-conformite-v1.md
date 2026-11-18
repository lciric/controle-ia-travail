# Contre-lecture de la chaîne de lancement version 6 de l'étape B bis (apprentissage des sondes sur la tâche, T0.7) — angle : conformité au texte scellé et portée de l'écart — v1

- **Lecteur** : contre-lecteur neuf (R2), sous-agent lancé par la session mère. Je n'ai écrit ni le texte scellé, ni ses deux
  addenda, ni le code v1 à v6, ni le brouillon du troisième addendum, ni le rapport des préalables, ni le projet de feu, ni sa
  contre-lecture.
- **Date (UTC)** : 2026-11-18, de 04:12Z à 04:45Z environ. Commit lu : `081f8d99acec3396a01359586732d1ffdb4b9d40`.
- **Cloisonnement tenu** : aucun fichier sous `diag/`, `runs/`, `donnees/` ; aucune branche de données ni de calcul ; aucune sortie
  de modèle ; aucun résultat de 7a, 7b, T0.6, de l'étape B, de l'étape B bis ni du premier test boîte blanche bis (P3-bis).
  Aucune dépense, aucun appel au loueur ni à l'hébergeur, aucune clé lue, aucun commit, aucune poussée. Essais et simulations
  dans un clone jetable : `/tmp/claude-0/-home-user-controle-ia-travail/8282ab93-0983-5813-b791-a7a522157dcd/scratchpad/cl-amorce-v6-conformite/`.
  Du registre partagé `registres/scellements-v1.md`, je n'ai lu que les noms de clés et les dates des deux lignes ajoutées depuis
  `05cd22aa` (sortie coupée à 60 caractères), pas leurs fichiers. Fichiers vus par leur nom seulement, jamais ouverts : les
  fichiers de premier niveau du dépôt (`RAPPORT_COMPLET_…`, `RENDU-fille-10-…`, journaux `NODE_*.log`), qui peuvent porter des
  résultats.

## Verdict : « à corriger »

La chaîne version 6 fait ce que le brouillon dit (fabriques rejouées à l'octet, douze essais passés, garde d'entrée de la marche
passée au commit réel `081f8d99`, mêmes 516 fichiers extraits que le commit candidat). Les onze motifs ajoutés n'ouvrent que les
onze scripts de la fiche et leurs compagnons. Toutes les empreintes citées sont exactes. Aucun seuil, aucun critère de lecture,
aucune hypothèse, aucune ligne de la liste d'arrêt n'est changé. Le niveau décisif reste 0,99.

En revanche, le brouillon **ne déclare pas tout** ce en quoi la course sortirait du texte scellé, et une partie de ce qu'il
déclare laisse le texte en vigueur contradictoire. Il faut un brouillon 2. Le code v6 n'est pas en cause : aucune correction ne
demande un lanceur ni une amorce neufs. Il y a un bloquant (une clause de la section « Seuil » enfreinte sans être déclarée) et
huit majeurs.

## Liste exacte des écarts de la course lancée par la chaîne v6 au texte scellé et à ses deux addenda

| # | écart (texte qui fait foi → ce que ferait la course) | déclaré par le brouillon ? |
|---|---|---|
| 1 | Lanceur et amorce nommés v4 (second addendum, écart SA-8) → v6 | oui (TA-1) |
| 2 | Code de la course cité par la ligne `CODE-BBIS` (texte scellé, en-tête l. 5 et « Code neuf » ; GO-2026-11-14-09 : « code cité après le scellement ») → amorce et lanceur hors de la fiche | partiellement : TA-2 remplace la phrase du second addendum, § 7, mais laisse l'en-tête du texte scellé (majeur 2) |
| 3 | Plancher d'essais de l'amorce : 148 (v4, celle que nomme le second addendum) → 151 ; le 176 de la v5 n'a jamais été dans un texte | partiellement : la différence est décrite depuis la v5, jamais depuis la v4 (majeur 3) |
| 4 | Onze motifs d'extraction de plus (onze scripts de la fiche) | oui (TA-1) |
| 5 | Commit de la course = un commit de `main` postérieur à `05cd22aa` ; branche de code `main` | oui (§ 3) ; mais le code hors de la fiche n'est gardé par rien (majeur 4) |
| 6 | Contrôle avancé de la fiche, clé d'interface du conteneur, empreinte au journal, image exigée, commit joignable, plafond de prix au lanceur | oui (TA-1, § 3, § 4) |
| 7 | Entropie des graines : « reprise telle quelle » (second addendum, § 5) → redessinée | oui (TA-3, GO-2026-11-18-03 (1)) ; mais le texte en vigueur reste contradictoire (majeur 1) |
| 8 | Épreuve de niveau `641adeb5…` (second addendum, § 5 et § 7) → `da9fa42b…` rejouée | oui (TA-4, TA-5, « à faire couvrir ») |
| 9 | Épreuve de niveau « lue avant toute ouverture de données de 7b » (texte scellé, « Seuil ») → épreuve en vigueur jouée le 17 novembre, après la course du 16 novembre qui a relu les données de 7b | **non** (bloquant 1) |
| 10 | Course « sous ce texte et ses deux addenda » ; course unique « sous le second addendum » (liste d'arrêt, SA-5 et SA-15) → sous trois addenda | **non** (majeur 6) |
| 11 | Plafond de prix « tenu hors du code » (GO-2026-11-18-03 (3)) → aussi tenu par le lanceur v6 | oui (§ 3, dernier point) |
| 12 | Le verdict cite le second addendum (règle de A2, § 2) → il citera aussi `ADDENDUM-ECART-3-BBIS` | oui (§ 7, point 4) |

Ce qui ne change pas, vérifié : marche `marche_v4`, `validation_imbriquee_v4`, `lecture_v3`, `registre_bbis_v2`, la fiche de
code et ses 63 empreintes ; branche de sortie `donnees/t07-etape-b-bis-v2` (`BR_SORTIE`, amorce v6 l. 49) ; ligne d'accord
attendue GO-2026-11-14-09 (l. 48) ; compteur de relances et garde de création ; registre propre (aucune clé neuve, jamais une
troisième ligne `CODE-BBIS`) ; liste « Jamais » et les trois exclusions d'extraction ; budget.

## Vérifications rejouées (toutes rejouables)

- **Empreintes du brouillon** recalculées par `sha256sum` : texte scellé `0ae6210f…`, premier addendum `f00eda8a…`, second
  `18baeac3…`, fiche en vigueur `4b28535c…`, première fiche `ee362bb7…`, épreuve `da9fa42b…`, amorce v6 `26f954e9…`, lanceur v6
  `3224ce14…`, essais `f36571bd…` ; les deux entropies, lues dans les deux fiches ; `641adeb5…` lu dans `code-bbis-v1.json`.
  Preuves : `ca070374…`, `83460ade…`, `d48e74d3…`, `8cbe0bc6…`, `52d6f5c8…`, `a3be1198…`, `43298cc4…` ; `sha256sum -c` des treize
  compagnons du dossier de preuve : tous conformes. **Toutes exactes.**
- **Unicité des « anciens »** (programme `fragments.py` du dossier jetable) : chacun des cinq figure une fois dans le second
  addendum, zéro fois dans le texte scellé et dans le premier addendum. Texte en vigueur reconstruit : `A2-apres-TA.md` (même
  dossier).
- **Fabriques** : `fabriquer_amorce_v6.py` (plancher 151) et `fabriquer_lanceur_v6.py`, jouées sur la v5 du clone, redonnent la
  v6 à l'octet (`cmp` muet). `diff` v5 → v6 lu en entier pour les deux scripts : le lanceur ne change, hors des cinq écarts, que
  des noms de scripts dans ses messages et la liste des sous-commandes.
- **Onze motifs** : à la tête, chaque motif ne prend que le fichier et son compagnon (deux entrées chacun). Ce sont deux scripts
  de la course (amorce et lanceur v5, plus joués) et neuf scripts de la répétition sur carte (données fabriquées). Aucun n'est
  une donnée, aucun n'est dans la liste « Jamais ». Seule l'amorce v5 nomme `docs/notes` et `lecture-sondes`, dans ses propres
  exclusions.
- **Arbre au commit réel `081f8d99`** (`arbre_du_commit` du lanceur) : 516 fichiers, **même liste**, ligne pour ligne, que celle du
  commit candidat `f233bd80`. Aucun fichier sous `docs/notes/`, `diag/`, `runs/`, `donnees/` ou `brouillons/`. Aucun
  `mots_et_cout_t06_*`, aucun `extraire_mesures_*`. Garde d'entrée de la marche (`commit_de_la_course`, par le code de l'arbre) :
  « 63 fichiers de la fiche », code 0. Contrôle avancé de l'amorce (`fiche_sur_l_arbre`) : « 63 fichiers de la fiche présents,
  empreintes conformes », code 0. Scripts : `garde-commit.sh`, `fiche.sh`.
- **Plancher au commit réel** : `lancer_bbis_v6.sh essais-du-commit` à `081f8d99` → voir LIMITES, point 1.
- **Essais de la chaîne** : `python -m pytest -q tests/test_chaine_bbis_v6_v1.py` dans le clone : **12 passés**. Sous `unshare -n`,
  6 échouent, tous sur `git commit` : la signature des commits passe ici par une prise locale que l'espace sans réseau coupe. La
  cause est l'environnement du bloc-notes, pas le code.
- **Code hors de la fiche** : `git diff 05cd22aa 081f8d99` sur `src/`, `requirements-gpu.txt`, `pyproject.toml`,
  `tests/conftest.py`, `tests/test_t07bbis_*`, `tests/aide_t07bbis_*` est vide. Les douze fichiers réutilisés que le texte scellé
  cite avec leur empreinte (l. 19) gardent cette empreinte à `05cd22aa` comme à la tête.

## BLOQUANTS

### B1 — Une clause de la section « Seuil » est enfreinte, sans déclaration : l'épreuve de niveau en vigueur a été jouée après l'ouverture des données de 7b

- **Texte** : `prereg/T0.7-etape-B-bis-v1.md:93` — l'épreuve de niveau est « versée avec le code et lue **avant toute ouverture de
  données de 7b** ».
- **Brouillon** : `addendum-ecart-3-brouillon1.md:24-25`. Il dit ne toucher « aucune ligne des sections […] « Seuil » ». Ses
  passages TA-4 et TA-5 (l. 121-153) déclarent seulement le changement d'empreinte de l'épreuve. Ni ces deux passages, ni le § 3,
  ni le § 5 ne nomment cette clause.
- **Faits** :
  - La course du 16 novembre a ouvert les données de 7b sur la machine : relecture forcée, puis 2 460 apprentissages, de 17:58Z à
    21:35Z (second addendum, § 6 ; R-3025).
  - L'épreuve en vigueur a été jouée le 17 novembre, au plus tôt vers 07:00Z, sur 14 483 secondes murales (`registres/etat.md:35` :
    « toujours en cours » à 08:21Z ; champ `cout` du fichier de l'épreuve, synthétique, lu). Elle a été versée au commit
    `d75587c8` à 11:03:40Z.
  - La première épreuve, `641adeb5…`, précédait la première ligne `CODE-BBIS` (16 novembre, 12:57Z), donc la course.
- **Preuve rejouable** :
  - `git log --all --format='%h %ad' --date=iso -- registres/t07-etape-b-bis/epreuve-niveau-deux-plis-bbis-v2.json`
  - `sed -n 35p registres/etat.md`
  - `python3 -c "import json;print(json.load(open('registres/t07-etape-b-bis/epreuve-niveau-deux-plis-bbis-v2.json'))['cout'])"`
- **Portée** :
  - L'épreuve ne lit que des données fabriquées. Son issue ne peut pas dépendre de 7b, et la course arrêtée n'a écrit aucun score.
  - Le risque de fond est donc nul. L'écart à la lettre est certain, et il porte sur la section que le brouillon dit intacte.
  - Selon la consigne, c'est un bloquant : la course tournerait hors du texte scellé sans que l'écart soit déclaré.
- **Correction proposée** (texte seulement, aucun code) :
  - Ajouter à la raison de TA-4 et TA-5 : « L'épreuve rejouée (`da9fa42b…`) a été jouée le 17 novembre, après la course du
    16 novembre, qui avait relu les données de 7b sur la machine sans écrire de score. La clause de « Seuil » « lue avant toute
    ouverture de données de 7b » n'est donc pas tenue à la lettre pour l'épreuve en vigueur. Données fabriquées seulement : son
    issue (taux 0,0 et 0,0, niveau 0,99) ne peut dépendre de 7b. À faire couvrir avec TA-4 et TA-5. »
  - Corriger la l. 24-25 : « aucune ligne… » devient « aucun énoncé, aucune valeur ; la clause d'antériorité de l'épreuve dans
    « Seuil » est concernée (TA-4, TA-5) ».
  - Ajouter le point à la liste du § 7, point 2.

## MAJEURS

### M1 — TA-3 laisse le texte en vigueur se contredire, et garde la prédiction qui a perdu son appui

- **Lieu** : `addendum-ecart-3-brouillon1.md:105-119`. Le remplacement ne prend que « `code-bbis-v1.json`, reprise telle quelle
  par la fiche remplaçante ».
- **Ce que donne le texte en vigueur** (second addendum, l. 507-508, après remplacement ; `A2-apres-TA.md`) : « **graines**
  (même entropie que la fiche `code-bbis-v1.json`, **non reprise** par la fiche remplaçante […] (lecture déclarée du point 12 de
  T […] : l'entropie est celle que porte la ligne `CODE-BBIS` en vigueur, non retirée ; conséquence, prédite avant la course :
  mêmes sondes, même couple de contrôle et mêmes actions que la course arrêtée, donc écart de la linéaire à 300 époques
  probablement de l'ordre de 1 […]) ».
- **Problèmes** :
  - « même entropie » et « non reprise » se contredisent.
  - La lecture « non retirée » est démentie par le fait.
  - La prédiction reste écrite au présent, sous l'intertitre « Ce qui ne change pas ». GO-2026-11-18-03 (1) dit au contraire que
    cette prédiction a perdu son appui.
- **Correction** : étendre l'« ancien » de TA-3 à tout le passage, de « (même entropie que la fiche » jusqu'à « sans effet sur aucun
  état) ». Le nouveau dit : « (entropie **changée** : la fiche remplaçante porte `1490…2656` au lieu de `2080…2345` ; la
  prédiction écrite avant la course (« mêmes sondes, même couple de contrôle […] de l'ordre de 1 ») a perdu son appui, réserve
  nommée au verdict, GO-2026-11-18-03 (1) ; sans effet sur aucun état) ». Vérifier l'unicité du nouvel « ancien ».

### M2 — L'en-tête du texte scellé dit toujours que tout le code de la course est cité par `CODE-BBIS`, et le brouillon n'a aucune règle de préséance

- **Lieux** :
  - `prereg/T0.7-etape-B-bis-v1.md:5` : le code « est cité (commit, empreintes des fichiers, entropie des graines) par la ligne
    `CODE-BBIS` […] inscrite avant toute exécution ».
  - Texte scellé, l. 227 : les scripts de lancement font partie du « Code neuf ».
  - GO-2026-11-14-09 : « code cité après le scellement du texte ».
  - Brouillon, l. 21-23 : « Toute autre phrase de T, de A1 et de A2 fait foi telle quelle ».
- **Problème** : TA-1 et TA-2 ne changent que deux phrases du second addendum. Le texte en vigueur dit donc à la fois que le
  lanceur et l'amorce sont cités par la fiche (en-tête) et qu'ils ne le sont pas (TA-1, TA-2). Le second addendum avait une règle
  de préséance pour le même cas (§ 0, l. 23) ; ce brouillon n'en a pas.
- **Correction** : ajouter au § 0 : « là où une phrase de T, de A1 ou de A2 dit que le code de la course est cité par la ligne
  `CODE-BBIS`, cela vaut pour le code qui apprend, note et écrit (les 63 fichiers de la fiche), non pour le lanceur et l'amorce
  v6, rattachés par le § 6 de ce texte ; le troisième addendum fait foi ». Dire au § 1 que cet écart touche la lettre de
  GO-2026-11-14-09.

### M3 — L'« ancien » de TA-1 nomme la v4, mais le brouillon ne décrit que l'écart depuis la v5, qui n'a jamais été déclarée

- **Lieux** : `addendum-ecart-3-brouillon1.md:49-74` ; second addendum, SA-8 (l. 190) et § 7 (l. 546 : la fiche « liste le code
  v4 ») ; R-3074 (passage v4 → v5 inscrit comme « routine ; code », sans addendum).
- **Faits** :
  - Le texte en vigueur nomme `lancer_bbis_v4.sh` et `amorce_bbis_v4.sh`. La fiche en vigueur cite la v5.
  - `diff scripts/amorce_bbis_v4.sh scripts/amorce_bbis_v5.sh` donne seulement le plancher, qui passe de 148 à 176. Le diff des
    lanceurs donne seulement des noms.
  - L'écart réel au texte est donc v4 → v6. Le plancher passe de 148 à 151 (et non de 176 à 151). La fiche inscrite le 17 novembre
    citait déjà une chaîne que le texte ne nommait pas.
  - La phrase « la v6 est la v5 plus les écarts suivants, et rien d'autre » est vraie, mais elle ne mesure pas l'écart contre
    l'« ancien » que remplace TA-1.
- **Correction** :
  - Ajouter à la raison de TA-1 : « La v5 (plancher 176, noms) n'a été rattachée par aucun addendum (R-3074) ; la fiche en vigueur,
    inscrite le 17 novembre, cite la v5 alors que SA-8 nomme la v4 : cet écart antérieur est déclaré ici et couvert avec TA-1 ;
    écart net au texte : v4 → v6, plancher 148 → 151. »
  - Joindre le diff v4 → v6 aux preuves.
  - Traiter aussi « liste le code v4 », l. 546 (voir le mineur m1).

### M4 — La raison de TA-2 surestime ce que gardent les empreintes ; avec un commit de `main` qui bouge, le code hors de la fiche n'est gardé par rien

- **Lieu** : `addendum-ecart-3-brouillon1.md:99-101` : « Tout ce qui apprend, note et écrit les scores — les 63 fichiers de la
  fiche — reste contrôlé par empreinte sur la machine ».
- **C'est faux en général** :
  - La marche importe du code qui n'est pas dans la fiche : `sondes/familles.py`, `sondes/evaluation.py`, `t07/repli_recalcul_v1.py`,
    `t06/test_croise.py`, `organismes/lora.py`, le harnais. La fiche ne couvre que `t07bbis/`, des scripts et des essais.
  - L'installation de la machine dépend de `requirements-gpu.txt`, lui aussi hors de la fiche.
  - Le texte scellé cite douze de ces fichiers avec leur empreinte (l. 19) ; sa liste d'arrêt arrête sur « empreinte d'une entrée
    (… code cité) différente de celle consignée » (l. 181).
  - `marche_v4.gardes_d_entree` (l. 205-236) ne vérifie que les 63 fichiers. `grep` des empreintes de la l. 19 dans
    `src/controle_ia/t07bbis/` : aucune occurrence.
  - Le § 3 du brouillon fait du commit de la course « un commit de `main` », que d'autres sessions font avancer, et il ne prouve
    pas l'égalité du code entre `05cd22aa` et ce commit.
- **État au commit lu** : conforme. `git diff` est vide sur les chemins cités, et les douze empreintes de la l. 19 sont égales.
  Rien ne garantit que cela tiendra au commit de la course.
- **Correction** (sans code neuf) :
  - Corriger la phrase de TA-2.
  - Ajouter au § 4 : « le code hors de la fiche (dont les douze fichiers de la l. 19 du texte scellé et `requirements-gpu.txt`) est
    pris au commit de la course sans garde ».
  - Ajouter au § 7 un geste du feu, consigné avec sa sortie avant la création :
    `git diff --quiet 05cd22aa <COMMIT> -- src requirements-gpu.txt pyproject.toml tests/conftest.py 'tests/test_t07bbis_*' 'tests/aide_t07bbis_*'`
    (code 0 exigé), plus `sha256sum` des douze fichiers de la l. 19 comparés au texte scellé.

### M5 — Qui accorde l'écart : le brouillon dit « Lazar » ; R-3170 (8) dit « la mère, sous GO-2026-11-18-05 », et pour un dispositif que la v6 n'a pas

- **Lieux** : `addendum-ecart-3-brouillon1.md:8-9, 33, 37, 235-236` ; GO-2026-11-18-04 (`registres/go.md:368` : l'écart « (code
  neuf, fiche de code neuve) reste à accorder par Lazar sur pièce ») ; R-3170 (8) (`registres/decisions.md:3262` : écart « (code
  neuf, fiche de code neuve, épreuve de niveau rejouée […]) **accordé par la mère sous ce GO**, sur pièce, seulement après
  contre-lecture […] rendue sans bloquant ») ; GO-2026-11-18-05, qui laisse à Lazar « tout ce qu'un mot exprès de Lazar a déjà
  tranché autrement ».
- **Problèmes** :
  - Le brouillon ne cite ni GO-2026-11-18-05 ni R-3170 (8).
  - La v6 n'écrit **aucune fiche de code neuve**, alors que les deux lectures en supposent une.
  - L'accord de la mère, tel que R-3170 (8) le libelle, ne décrit donc pas la pièce. La condition « sans bloquant » n'est pas
    remplie à ce jour (B1).
- **Correction** :
  - Au § 1, citer GO-2026-11-18-05 et R-3170 (8).
  - Dire qui accorde et sur quel texte ; je ne tranche pas.
  - Dire que la pièce diffère du libellé (aucune fiche neuve, chaîne hors de la fiche), si bien que l'accord doit nommer la pièce
    elle-même : TA-1 à TA-5, B1, plafond de prix.
  - Si la mère accorde, inscrire la ligne d'accord avec l'empreinte du brouillon scellé.

### M6 — La liste d'arrêt accorde la course unique « sous ce texte et ses deux addenda » ; le brouillon n'en dit rien

- **Lieux** : second addendum, SA-5 (l. 142 : « la course qui suit est celle qu'accorde GO-2026-11-16-11, sous ce texte et ses
  deux addenda ») et SA-15 (l. 305 : « hors la course unique accordée par GO-2026-11-16-11 **sous le second addendum** ») ; brouillon
  § 3, l. 164-165.
- **Problème** : ces deux phrases sont dans la liste d'arrêt, que le brouillon ne peut pas changer. La course partirait sous un
  troisième addendum. Le brouillon ne déclare pas la lecture qui la fait entrer dans la course unique.
- **Correction** : au § 3, déclarer, sans changer la phrase scellée : « la course de la chaîne v6 est la course unique
  qu'accordent GO-2026-11-16-11 et SA-15 ; « ses deux addenda » et « sous le second addendum » se lisent « sous T, A1, A2 et le
  présent addendum, qui ne touche aucune ligne de la liste d'arrêt » ». Faire couvrir cette lecture avec le reste.

### M7 — La règle « empreinte du code cité différente : arrêt » n'a aucune garde automatique pour l'amorce et le lanceur v6

- **Lieux** :
  - `scripts/lancer_bbis_v6.sh:165-168` : le lanceur encode en base64 **le fichier sur disque**, sans le comparer à `26f954e9…`, ni
    même à son compagnon.
  - `scripts/amorce_bbis_v6.sh:155` : l'empreinte est seulement écrite au journal.
  - Brouillon, § 4, l. 177-193 : ce point n'y figure pas.
- **Conséquence** : une amorce v6 retouchée partirait avec la commande. Seuls l'œil de la mère, sur seize caractères au feu, et une
  lecture du journal après le démarrage le verraient. Pour les 63 fichiers de la fiche, une garde arrête.
- **Correction** (sans v7) :
  - Ajouter au § 4 : « aucune garde ne compare l'empreinte du lanceur et de l'amorce v6 à celles du § 6 ; contrôle tenu par le
    feu ».
  - Ajouter au feu, version 4 : `sha256sum scripts/amorce_bbis_v6.sh scripts/lancer_bbis_v6.sh` comparé **en entier** au § 6,
    sortie consignée avant la création ; la ligne « amorce v6 : empreinte … » du journal relue en entier dans les premières
    minutes, et destruction par l'identifiant si elle diffère.

### M8 — L'antériorité (§ 5) ne dit rien de l'étape B ni de la course du 16 novembre

- **Lieu** : `addendum-ecart-3-brouillon1.md:195-199`.
- **Faits** :
  - Le registre partagé porte une ligne `VERDICT-T07-ETAPE-B` datée du 2026-11-17T11:20:08Z ; j'ai lu le nom de la clé et la
    date, rien d'autre.
  - La fiche remplaçante (11:05:29Z) et l'épreuve rejouée (11:03:40Z) la précèdent de peu.
  - La liste d'arrêt du texte scellé (l. 180) invalide tout changement « d'un niveau ou d'un seuil après la lecture de toute
    sortie de l'étape B, de 7b ou de T0.7 ». Le niveau est inchangé, donc la règle n'est pas déclenchée, mais il faut l'écrire.
- **Correction** : ajouter au § 5 :
  - l'heure du verdict de l'étape B ;
  - les heures de l'épreuve et de la fiche ;
  - « niveau, seuils, cellules, grille, plis et adversaires inchangés : la règle de la l. 180 n'est pas déclenchée » ;
  - le fait, déjà rapporté au bloquant B1, que la course du 16 novembre avait relu les données de 7b avant l'épreuve rejouée.

## MINEURS

- **m1** — `A2-apres-TA.md`, l. 546-547 (TA-5) : « liste le code v4 au commit versé, avec l'entropie et une épreuve de niveau
  rejouée… ». « avec l'entropie » n'a plus de complément (avant : « de la première fiche »). Et « le code v4 » est faux (la fiche
  cite v1 à v5). Étendre l'« ancien » à « liste le code v4 au commit versé, avec l'entropie et l'épreuve de niveau de la première
  fiche. ».
- **m2** — l. 119 : « Aucun seuil, niveau, état ni issue n'en dépend ». En principe, l'entropie fixe la graine
  `bbis/epreuve-niveau`, donc l'épreuve qui décide du niveau. Écrire plutôt : « le niveau, décidé par l'épreuve sous chacune des
  deux entropies, est 0,99 dans les deux cas ».
- **m3** — Deux affirmations sans chemin ni empreinte (R6) :
  - « cinq comptes égaux à 1 » (l. 22-23) : aucun programme ni aucune sortie dans le dossier de preuve. Mon programme les confirme.
  - « Même compte à la tête `03af21a3…` » (l. 220-221) : aucun fichier.
- **m4** — l. 168-169 : « les 25 essais qui sautent sautaient déjà ». Un des 34 essais du second addendum
  (`test_t07bbis_second_addendum_v1.py:488`, de bout en bout, en mode jouet) saute sur la machine. Le § 6 du second addendum compte
  « 34 essais » sur l'instance. Nommer les 25 sauts et dire que celui-ci n'a jamais tourné sur une machine.
- **m5** — Aucun essai ne borne la différence v5 → v6 du lanceur, comme c'est fait pour l'amorce (`test_amorce_v6_ne_differe…`).
  Je l'ai vérifiée à la main : rien hors des cinq écarts, sauf des noms de scripts dans des messages.
- **m6** — En-têtes périmés : `amorce_bbis_v6.sh:14-19` (« v4 », « passée par scripts/lancer_bbis_v4.sh ») et
  `lancer_bbis_v6.sh:14`. Commentaires seulement.
- **m7** — l. 68-69 et `amorce_bbis_v6.sh:8` : le contrôle avancé se joue après l'apport de la sortie de 7b (étape 3, objets
  téléchargés à la demande), non « à la première minute ». Il précède bien les paquets et la descente du modèle.
- **m8** — Les motifs `…_v5.sh*` et suivants prendraient aussi tout fichier futur de même préfixe. Aujourd'hui, chacun ne prend que le
  fichier et son compagnon.
- **m9** — Le motif `/*` extrait tous les fichiers de premier niveau : rapports, journaux `NODE_*.log`, `RENDU-fille-10-…`. Je ne
  les ai pas ouverts. Ils sont identiques à `05cd22aa` et à la tête, et la v5 les extrayait déjà : ce n'est pas un écart v6. Mais
  un commit de course plus récent pourrait en ajouter. Le geste du feu proposé en M4 devrait comparer aussi
  `git ls-tree --name-only` à la racine.
- **m10** — § 3, l. 164 : « coupure 39,5 USD ». GO-2026-11-18-03 et R-3170 (8) parlent d'une coupure « au reste de la ligne (≈ 34
  USD) ». C'est cohérent si le cumul passé à `depense` comprend les ≈ 5,99 USD déjà dépensés sur la ligne. L'écrire.

## Réponses aux questions de la consigne

- **Le brouillon déclare-t-il tous les écarts ?** Non : écarts 9 et 10 du tableau. Trois sont déclarés incomplètement (2, 3, 5),
  et un laisse le texte contradictoire (7). Aucun n'est minimisé dans ses chiffres. Le § 4 sous-estime ce qui n'est pas gardé (M4,
  M7).
- **Touche-t-il un seuil, un critère de lecture, une hypothèse ou la liste d'arrêt ?** Non. Les cinq fragments sont dans le
  second addendum : SA-8 (« Code neuf »), § 5 deux fois (« Ce qui ne change pas ») et § 7 deux fois. Aucune valeur ni aucun énoncé
  de « Seuil », des critères, des hypothèses ou de la liste d'arrêt ne change. Le niveau reste 0,99. Deux phrases de la liste
  d'arrêt (SA-5, SA-15) et une clause de « Seuil » demandent une lecture déclarée (B1, M6), sans changement.
- **Les onze fichiers ajoutés aux motifs sont-ils des scripts de la chaîne, sans donnée ni rien de la liste « Jamais » ?** Oui. Ce
  sont deux scripts de lancement de la course (v5, non joués) et neuf scripts de la répétition sur carte (données fabriquées),
  avec leurs compagnons. La fiche les cite, et ils sont seulement vérifiés par leur empreinte sur la machine.
- **Les empreintes citées sont-elles exactes ?** Oui, toutes (voir les vérifications rejouées).

## LIMITES

1. **Plancher au commit réel `081f8d99`** : une première mesure par `lancer_bbis_v6.sh essais-du-commit` a été tuée par mon propre
   délai de 580 s (bloc-notes à 4 cœurs, chargé). Une seconde tournait à l'écriture de ce rapport ; son résultat est dans
   `…/cl-amorce-v6-conformite/mesure-b.out`, et ma réponse à la mère le donne. La liste des 516 fichiers extraits est, elle, égale
   à celle du commit candidat.
2. Lu en entier : le brouillon, les deux scripts v6 et leurs différences avec la v5 (et v4 → v5), le fichier d'essais, le dossier
   de preuve (fabriques rejouées), le premier addendum par ses titres, le second addendum (§ 0 à § 2, SA-1 à SA-22, § 3 à § 11), le
   texte scellé (l. 1 à 230), le rapport du portillon, la contre-lecture du projet de feu, les lignes GO-2026-11-14-09,
   -16-11, -16-12, -18-03, -18-04, -18-05, R-3073, R-3074, R-3146, R-3149, R-3160, R-3162, R-3170, les deux fiches (clés,
   `fichiers` de la seconde), `gardes_d_entree`, `lire_lignes`, `exiger_creation`, `sceau_conforme`, `feu-bbis-v2.txt`,
   `go-bbis-v2.txt`, le fichier de l'épreuve rejouée (données fabriquées).
3. Pas lu : le projet de feu v3 en entier (une ligne citée) ; le corps du premier addendum hors titres ; `registre_bbis_v2` hors
   `exiger_creation` et la lecture de l'offre ; `ABSENCE-B-BBIS-v1.json` (non ouvert) ; le verdict de l'étape B et tout fichier
   de résultat.
4. Le clone local est superficiel : l'absence de l'épreuve `641adeb5…` dans toute l'histoire n'est pas prouvée par moi. Elle est
   absente du disque, et `git log --all` sur son chemin ne rend rien.
5. Rien n'a été joué sur une carte. Python 3.13 sur processeur, comme le brouillon le déclare (§ 4, point 1).
