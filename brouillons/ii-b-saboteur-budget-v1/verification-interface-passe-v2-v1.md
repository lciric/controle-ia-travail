# Vérification courte de la note d'interface v2 de la passe de recalcul, côté exposé — saboteur à budget, barreau 8 — v1

> **CÔTÉ EXPOSÉ.** Ce rapport recopie, dans ses couples, des passages de la note et du programme vérifiés, et nomme des pièces du côté exposé : il n'est **jamais montré au côté moniteurs**. Seule la note corrigée l'est.

- **Verdict : transmissible après ces couples** — quinze couples exacts, à appliquer dans l'ordre : trois sur la note (W-01 à W-03), neuf sur le programme de l'extrait (E-01 à E-09, qui en font une version 2 sous nom neuf, R12), trois sur ses essais (T-01 à T-03, version 2 sous nom neuf). Chaque « avant » est présent une seule fois dans sa pièce, à la ligne dite, vérifié par programme au moment de son application.
  - Le rejeu de la v2 depuis la v1 est exact à l'octet ; les quatorze couples de la vérification de la v1 sont appliqués tels que le rapport les donne, et rien d'autre ne change hors des quatre ajouts déclarés.
  - Des quatre ajouts, trois ne portent ni mécanisme, ni fragment de la consigne privée, ni réglage. Le quatrième, le point d'en-tête « Version 2 », n'en porte pas dans son texte, mais il **renvoie** par chemin et empreinte à trois pièces qui portent les passages retirés par la vérification de la v1, dont deux hors des exclusions du point (e) (W-01, W-03).
  - La section « Livraison » est cohérente avec la décision de la mère ; une phrase du point (e), venue d'un couple de la v1, la contredit et contredit le point (4) de la décision (W-02).
  - Le programme de l'extrait ne laisse passer, par construction, que les clés permises au premier niveau et dans les lignes d'état ; **ni les clés de `versions` ni les valeurs des lignes d'état ne sont bornées** : deux artefacts passent. Au code revu, rien ne fuit en pratique ; les couples E et T rendent la garantie vraie par construction.
- **Pièces vérifiées**, branche `claude/iib-executante-v1`, commit `d02870e0929aecc47a2ee5f31b7aaacb977c3c80` ; chaque empreinte recalculée sur `git show` par nom explicite, égale au préfixe donné par le mandat et au compagnon `.sha256` du même commit :
  - `docs/notes/barreau8-iib-v1/interface-passe-cote-moniteurs-v1.md` : `4fddb6c616de813f040353fc26fb2465aba101020222d08e904447bffa90b8db` ;
  - `docs/notes/barreau8-iib-v1/interface-passe-cote-moniteurs-v2.md` : `3262010b2493e7c1131d72f70deb3905f335d8c4a1d1f2b14428e1737bb9cce6` ;
  - `docs/notes/barreau8-iib-v1/differences-interface-v1-vers-v2.md` : `59e602a1f0ca9657d9243d8a84720faf27742894b75b9456727d4510edb5da10` ;
  - `docs/notes/barreau8-iib-v1/appliquer-couples-interface-v2.py` : `c5ac40abf7376dfd98550a95d75546b011a2be7d8ca2af6718c90079747fe1f0` ;
  - `docs/notes/barreau8-iib-v1/ajouts-interface-v2.json` : `a8afd2ecb7c25024c736705988fdab463b0e1684ecfea0f16c85dc65c3c547a5` ;
  - `scripts/extrait_iib_cote_moniteurs_v1.py` : `e6172629ff71d6bf8486982e22b522ebd9f204f146dae3d935b634659d2e9ebd` ;
  - `tests/test_extrait_cote_moniteurs_v1.py` : `29561a4ca49564b910baca3c60fcf0b73be252c176aceb0d9dd0c55151dcc87b`.
- **Sur `main`** (`5b4b396f5ce47a8566291a32cae4956e603fd538`), recalculées et égales : le rapport de vérification de la v1, `brouillons/ii-b-saboteur-budget-v1/verification-interface-passe-v1.md` (`ae5c03531564b0a4f9c0606b03db9e56661cb6babdee56ea6cecb1444482beef`) ; la conception finale, `brouillons/ii-b-saboteur-budget-v1/conception-ii-b-v1.md` (`77f1cc99a766190f31d0fa78226f8b74afda3345355701cfd222ee4fdc2aeb8c`), lue en entier.
- **Vérificateur** : sous-agent neuf de la session mère `session_013QMayjsoZJFBUCqcnvD5h1` (Claude Opus 5.5), côté exposé, second vérificateur de cette différence (le premier a été coupé par un redémarrage ; aucun fichier `verification-interface-passe-v2-*.md` n'existait à l'écriture). Il n'a écrit ni la note, ni la conception, ni l'ordre, ni le code, ni le rapport de la v1 ; il est exclu, à compter de cette vérification, de tout rôle côté sondes du barreau 8. Écrit le 2026-11-19 vers 00:30 UTC (`date -u` : 00:28:17 au début de l'écriture).
- **Lu, pour les points 1 à 4** : les sept pièces ci-dessus, le rapport de la v1 et la conception ; au commit `d02870e0`, les modules généraux qu'appelle le programme de l'extrait : `src/controle_ia/manifeste.py` (l. 24-26 et 55-117 : `BIBLIOTHEQUES`, `versions`, `creer_manifeste`), `src/controle_ia/scellement.py` (l. 55-90 : `sceller`, `verifier`), `src/controle_ia/gardes.py` (l. 15-17), `tests/conftest.py`, `pyproject.toml` (réglages de `pytest`).
- **Lectures hors des pièces nommées** :
  - pour le point 4, la seule ligne R-3558 de `registres/decisions.md` sur `main` (l. 3696), que le mandat cite ;
  - pour le point 3 (ce que révèlent les « états par lot »), au commit du code revu `ec3b0329cd59db676007bd6c9ea3f0c36cf3ce95`, par `git show` et recherche de lignes : `src/controle_ia/iib/lanceur_v1.py` l. 66-68 (table des adaptateurs) et l. 380-432 (boucle de l'évaluation et écriture de `episodes-iib.json`) ; `src/controle_ia/t06/identite.py` l. 20-55 ; `src/controle_ia/organismes/lora.py` l. 123-128 ; recherche de `etats_par_lot`, `creer_manifeste` et `versions` dans `src/controle_ia/iib/` (lignes trouvées : `bases_textuelles_v1.py` l. 198 et 204 ; `lanceur_v1.py` l. 3, 46, 241, 385, 400, 428) ;
  - **par accident d'une première recherche trop large** sur `scripts/` au même commit, des lignes isolées d'appel au manifeste ou à `versions` dans des scripts sans rapport avec cette vérification : `essai_fermeture_p3bis_v1.py` (l. 59, 179), `etape0_idee_1_1_v1.py` à `_v5.py` (l. 70 à 73), `extraire_garde_equivalence_t06_v1.py` (l. 281), `fabrique_factice_mots_et_cout_t06_v1.py` (l. 108), `jouer_idee_1_1_v1.py` à `_v5.py` (l. 39 à 43, 139 à 149), `jouer_idee_1_2_v1.py` et `_v2.py` (l. 41-42, 131, 148-152, 174, 198), `mots_et_cout_t06_v1.py` (l. 1565), `mots_et_cout_t06_v3.py` (l. 1593) et **`repetition_jouet_t07_v2.py` (l. 6, 35, 37 : enveloppe du lanceur de la répétition jouet des sondes autour de `creer_manifeste`)** ; ce sont des lignes d'appel, sans sonde, couche ni résultat ; la dernière touche au côté sondes et est déclarée pour la liste « qui a lu quoi » ;
  - par leurs noms seuls : le contenu du dossier `docs/notes/barreau8-iib-v1/` sur `main` et au commit `d02870e0` ; les autres fichiers de la branche de l'exécutante (`registres/iib-executante/…`, journal et journaux à blanc), vus par `git diff --name-only` ; le dossier non suivi `runs/20261119-001744-formulation-g1/` vu par `git status` ; les noms du dossier `brouillons/ii-b-saboteur-budget-v1/` (dont ceux qui contiennent « consigne-privee ») ;
  - une recherche sur le disque local d'une copie de `tokenizer.json` (aucune trouvée).
- **Non ouverts** : aucun fichier dont le nom contient « consigne-privee » ; ni la branche `lot/compte-4-v1`, ni l'enveloppe de la huitième tâche, ni `diag/`, `runs/`, `donnees/`, `docs/verdicts/` ; ni l'ordre, ni le devis, ni le préenregistrement et la configuration des sondes de T0.7 cités par la note ; aucun des autres fichiers du dossier `docs/notes/barreau8-iib-v1/` ; rien d'autre du code revu que les lignes dites.
- **Écart du vérificateur, déclaré** : mon premier calcul d'empreintes a pris ses fichiers **par joker** (`*.md`, `*.py`, `*.json`) dans mon dossier du bloc-notes où je venais d'extraire les sept pièces, une à une, par leur nom ; les jokers n'y couvraient que ces sept fichiers. Toutes les empreintes de ce rapport ont été recalculées ensuite par noms explicites, sur `git show`.
- **Refus** : aucun (ni classifieur, ni permission, ni crochet).

## 1. Rejeu de la v2 depuis la v1 (point 1)

- **Programme de l'exécutante**, joué tel quel (`python3 -I -B appliquer-couples-interface-v2.py <rapport v1> <note v1> <ajouts> <sortie>`, depuis un dossier vide du bloc-notes) : les quatorze couples puis les quatre ajouts s'appliquent ; la sortie a l'empreinte `3262010b2493e7c1131d72f70deb3905f335d8c4a1d1f2b14428e1737bb9cce6`, égale octet pour octet à la v2 du commit (`cmp`).
- **Contre-épreuve indépendante** (programme à moi, sans les expressions régulières de l'exécutante) : les couples sont relus ligne à ligne dans le rapport de la v1 ; chaque « avant » est présent une fois dans la v1, à la ligne annoncée par le rapport (20, 32, 41, 43, 46, 50, 56, 62, 65, 69, 80, 91, 98, 102) ; chaque « après » est présent une fois dans la v2 ; aucun « avant » ne reste dans la v2, sauf V-09 et V-10, dont l'« après » contient l'« avant » (ajout en fin de ligne).
- **Rien d'autre ne change** : la v2 recomposée en remplaçant, aux positions de la v1, les dix-huit « avant » (quatorze couples, quatre ajouts ; aucun chevauchement, tous présents dans la v1 d'origine) par leurs « après » est égale à la v2 (même empreinte `3262010b…`).
- **Liste des différences** : le différentiel de `differences-interface-v1-vers-v2.md` est égal, ligne pour ligne, à `diff -u` recalculé sur les deux fichiers (en-têtes de date mis à part).
- **Écart de compte, sans portée** : le point d'en-tête de la v2 annonce « trois ajouts » ; la liste des différences et `ajouts-interface-v2.json` en comptent quatre (le titre passé en v2). W-01 aligne le texte.

## 2. Les quatre ajouts hors couples, lus contre la conception (point 2)

| ajout | ligne de la v2 | mécanisme, consigne privée, réglage ? | jugement |
|---|---|---|---|
| titre « — v2 » | 1 | aucun | sans défaut |
| phrase de l'empreinte git du jetoniseur | 20 | aucun : empreinte d'un fichier public du modèle de base | sans défaut quant au mécanisme ; fait non vérifié ici (section 6, remarque 2) |
| section « Livraison au côté moniteurs » | 10-14 | aucun : qui conduit la passe, son périmètre (2 560 actions de l'évaluation, déjà dites à la question (8)), ce que reçoit le côté moniteurs ; rien de la sélection des épisodes, de l'oracle, de la règle, des tours, de la distillation ni de la consigne | sans défaut ; cohérente avec R-3558 (section 4) |
| point d'en-tête « Version 2 » | 6 | **aucun dans son texte** ; mais il **renvoie**, par chemin et empreinte, à la v1 « gardée intacte », au rapport de vérification de la v1 et à la liste des différences, « même dossier » | **défaut de renvoi** : W-01 et W-03 |

**Pourquoi le point d'en-tête est un défaut.** La conception tient pour le cœur de la construction la fabrication des données de l'élève (sections 0, 1, 3 et 4) et pour des réglages du saboteur les effectifs des tours (section 4). Or :
- la **v1** porte encore les deux passages que les couples V-03 (fabrication de l'organisme, rattachement du témoin-jumeau à l'oracle) et V-07 (effectifs des phases hors évaluation, dont le nombre maximal de tours) ont retirés, ainsi que les renvois au paquet du saboteur et au manifeste, au résumé et aux fiches que V-01, V-04, V-05 et V-11 ont fermés ;
- la **liste des différences** les recopie toutes, lignes « − » du différentiel ;
- le **rapport de la v1** les recopie dans ses couples et en commente le sens.
Le rapport de la v1 est dans `brouillons/ii-b-saboteur-budget-v1/`, déjà fermé par le point (e). **La v1 et la liste des différences sont dans `docs/notes/barreau8-iib-v1/`, que le point (e) ne ferme pas** : le point d'en-tête y mène le côté moniteurs, ce que la vérification de la v1 traitait comme un défaut de même rang qu'un passage de mécanisme (son § 1 : « des renvois qui mènent le côté moniteurs à des fichiers ou à du code qui le portent en entier »). W-01 retire les renvois et garde, en clair, ce qui a changé ; W-03 ferme les pièces par leur nom au point (e). La provenance de la v2 reste entière du côté exposé (liste des différences, programme, ajouts, ce rapport).

## 3. Programme de l'extrait (point 3)

**Ce qu'il écrit** : six clés fixes au premier niveau (`avertissement`, `run_id`, `commit_lancement`, `versions`, `fichiers_de_la_passe`, `etats_par_lot_evaluation`). Il lit le manifeste, le résumé et les fiches d'épisodes, chacun vérifié contre son compagnon, mais n'en recopie que : la clé `versions` du manifeste ; les empreintes des quatre fichiers de la passe, prises dans `resultat.empreintes` du résumé et recalculées sur disque et contre leurs compagnons ; les lignes `etats_par_lot`, réduites à six clés. Ni la configuration, ni son empreinte, ni les graines, ni la commande, ni les comptes du résumé, ni les fiches, ni l'oracle ne sont recopiés. Le commit de lancement doit égaler celui du manifeste ; la sortie n'écrase rien (ni le fichier, ni un compagnon existant).

**Ce que révèlent les « états par lot de l'évaluation »** (code revu, `lanceur_v1.py` l. 383-401, seul endroit où ces lignes sont écrites) : condition (H, B50, B100, TJ100), numéro du lot dans la condition, nom de l'adaptateur chargé (`eleve` ou `temoin-jumeau`), dose relue sur les modules avant et après le lot, empreinte sha256 des tenseurs de l'adaptateur chargé (`identite.etat_adaptateurs` → `lora.empreinte_adaptateurs`). La table condition → adaptateur → dose est celle de la question (5) de la note. **Rien de la fabrication de l'organisme** : ni phase hors évaluation, ni compte d'épisodes, ni coût, ni oracle. La clé `versions` vient de `manifeste.versions()` : interpréteur, chaîne de plateforme, versions des bibliothèques listées.

**Essais joués** (copie de l'arbre du commit dans le bloc-notes, `PYTHONPATH=src python -B -m pytest -q -p no:cacheprovider --basetemp=<bloc-notes>/basetemp-essais/v1 tests/test_extrait_cote_moniteurs_v1.py`) : **9 réussis**.

**Artefacts du vérificateur** (bloc-notes, non versés) :
- une clé de plus dans `versions` (nom et valeur arbitraires) : **acceptée et recopiée** ;
- une ligne d'état aux six clés permises, mais à valeurs imbriquées (un dictionnaire de comptes dans `lot`, une liste dans `adaptateur`, une chaîne dans une dose, un dictionnaire dans `empreinte`) : **acceptée et recopiée** ;
- `run_id` du manifeste discordant, liste d'états vide, compagnon faux d'un fichier de la passe, compagnon de sortie déjà présent : refusés ; empreinte imprimée égale au compagnon écrit.

**Jugement.** Au premier niveau et pour les clés des lignes d'état, le filtre est par construction. Pour les **clés de `versions`** et les **valeurs des lignes d'état**, la garantie repose sur le producteur, non sur l'extrait. Au code revu, le producteur n'écrit que des scalaires et `manifeste.versions()` que des versions : rien ne fuit en pratique. Les couples E-01 à E-09 bornent les clés de `versions` à celles de `manifeste.versions()` et fixent le type et la valeur de chaque champ d'état (adaptateur et dose de la condition, lot entier positif, empreinte de 64 caractères hexadécimaux), sans imprimer aucune valeur refusée ; E-01, E-08 et E-09 portent le nom de la version 2. T-01 à T-03 adaptent le cas sain à la table de la question (5) et ajoutent huit artefacts.

**Contrôle des couples à blanc** : appliqués sur copies, les « avant » présents une fois chacun ; la v1 du programme et de ses essais restant en place (R12), `pytest` sur les deux versions donne **26 réussis** (9 de la v1, 17 de la v2, dont les 8 artefacts neufs refusés) ; les clés réelles de `manifeste.versions()` dans cet environnement sont toutes permises. Aperçus à blanc (bloc-notes, non versés) : programme v2 `645248bb7ea012ceb701f9405c75f6941bd8335bec44862ea77908a46d7ea63c` ; essais v2 `8befae14bb0d7cbddd5a2adc78bdfd38ce5cbc3e99432c043a46af007dca44e0`.

**Nom des essais v2** : `tests/test_iib_extrait_cote_moniteurs_v2.py`, pour que la règle du point (e) sur les essais `test_iib_*` les couvre ; les essais v1, dont le nom ne commence pas ainsi, sont nommés par W-03. Leur jeu factice porte des noms de clés (« acceptes », « tours », « effectifs », « couts », condition « maitre_iib ») qui n'ajoutent rien aux noms de fichiers que le point (e) donne déjà, mais qui n'ont pas à être lus par le côté moniteurs.

## 4. Section « Livraison » et décision de la mère (point 4)

R-3558 (registre des décisions, l. 3696), points (1), (2) et (4) :
- **(2) passe bornée à l'évaluation, conduite par l'exécutante, avec le code du développeur du côté moniteurs** : la section le dit (« Qui conduit la passe », « bornée aux 2 560 actions de l'évaluation », « joue, sans le modifier, le code que le développeur du côté moniteurs écrira ») ;
- **(2) le côté moniteurs ne lit jamais la configuration ni le manifeste ; il ne reçoit que les fichiers d'activité scellés** et, selon le mandat, la note et l'extrait : la section le dit (« rien d'autre de la course : ni la configuration, ni le manifeste, ni le résumé, ni les fiches d'épisodes, ni aucun fichier de `donnees/<run>/`, `diag/<run>/` ou `runs/<run>/` » ; « les seuls textes qui les accompagnent sont cette note et l'extrait ») ;
- **(1) l'extrait remplace tout accès au manifeste, au résumé et aux fiches** : cohérent avec le point (b) et avec le programme ;
- **(4) aucune sortie d'une lecture de la course avant le scellement du texte du côté moniteurs** : la section le respecte (les sorties des lectures sont sous `diag/<run>/`) ; **mais le point (e), ligne 105, venu du couple V-13 de la v1, dit que la phrase de la sortie de la lecture (1) « peut être transmise par le côté exposé »** : cela contredit la section et le point (4). W-02 aligne le point (e) sur la section.

Laissé tel quel : la dernière phrase du point (b) (« ne sont pas ouverts par le côté moniteurs », pour le seul manifeste, le résumé et les fiches) est plus étroite que la section, sans la contredire ; la section, placée avant les questions et le point (b), ferme le reste. La phrase « les questions (1) à (8) et les points (b) à (e) disent au développeur ce que son code doit lire et rebâtir » est juste : (9) à (12) ne servent pas au code de la passe.

## 5. Couples exacts (avant → après), à appliquer dans l'ordre

Chaque bloc est à l'octet, entre deux lignes `~~~~` ; un saut de ligne dans un bloc est un saut de ligne de la pièce ; aucun bloc ne finit par un saut de ligne. La ligne dite est celle de la pièce au moment où le couple s'applique, couples précédents de la même pièce compris (E-03, E-04, E-05 et E-06 ajoutent des lignes).

### 5.1 Note v2 (`3262010b…`) → version suivante de la note

Aperçu à blanc de la note après W-01 à W-03 (bloc-notes, non versé) : `477815d1b48fc681ae4d403f81cf6f6fcff5750611e74f784db802013eed05f1`.

### W-01 — ligne 6

avant :

~~~~
- **Version 2** (2026-11-19, UTC) : version 1 (`interface-passe-cote-moniteurs-v1.md`, `4fddb6c616de813f040353fc26fb2465aba101020222d08e904447bffa90b8db`, gardée intacte, R12) + les quatorze couples V-01 à V-14 du rapport de vérification du côté exposé (`brouillons/ii-b-saboteur-budget-v1/verification-interface-passe-v1.md`, `ae5c03531564b0a4f9c0606b03db9e56661cb6babdee56ea6cecb1444482beef`), appliqués par programme dans l'ordre, chaque « avant » présent une seule fois ; plus trois ajouts déclarés de l'exécutante : ce point d'en-tête, la phrase de l'empreinte git (question 1, remarque du rapport, § 3) et la section « Livraison au côté moniteurs » (décision d'organisation de la mère, message du 2026-11-19 vers 00:12Z). Liste des différences : `differences-interface-v1-vers-v2.md`, même dossier.
~~~~

après :

~~~~
- **Version 2** (2026-11-19, UTC) : remplace la version 1 de cette note, après vérification du côté exposé. Ajouts de l'exécutante hors des couples de cette vérification : le titre, ce point d'en-tête, la phrase de l'empreinte git (question 1) et la section « Livraison au côté moniteurs » (décision d'organisation de la mère, message du 2026-11-19 vers 00:12Z). La version 1, la liste des différences, les pièces qui ont fait cette version et les rapports de vérification restent du côté exposé, qui tient la provenance de cette version (point (e)).
~~~~

### W-02 — ligne 105

avant :

~~~~
la sortie de la lecture (1) (sa seule phrase peut être transmise par le côté exposé)
~~~~

après :

~~~~
la sortie de la lecture (1) et sa phrase (aucune sortie ni phrase d'une lecture de la course n'est transmise au côté moniteurs : section « Livraison » ; R1)
~~~~

### W-03 — ligne 106

avant :

~~~~
les contre-lectures, contrôles courts et vérifications du code, de l'ordre et du devis, et les journaux de l'exécutante ; la branche gelée `prep/iib-code-v2`.
~~~~

après :

~~~~
les contre-lectures, contrôles courts et vérifications du code, de l'ordre, du devis et de cette note, et les journaux de l'exécutante ; dans le dossier de cette note, la version 1 de la note (`interface-passe-cote-moniteurs-v1.md`) et les pièces qui ont fait la version 2 (`differences-interface-v1-vers-v2.md`, `appliquer-couples-interface-v2.py`, `ajouts-interface-v2.json`), qui portent les passages retirés ou y mènent ; les essais du programme de l'extrait (`tests/test_extrait_cote_moniteurs_v1.py` et ses versions suivantes) ; la branche gelée `prep/iib-code-v2`.
~~~~

### 5.2 Programme de l'extrait v1 (`e6172629…`) → `scripts/extrait_iib_cote_moniteurs_v2.py`

### E-01 — ligne 1

avant :

~~~~
"""Extrait de la course du saboteur à budget pour le côté moniteurs, v1 (vérification de la note d'interface, couple V-11).
~~~~

après :

~~~~
"""Extrait de la course du saboteur à budget pour le côté moniteurs, v2 (v1 + couples E-01 à E-09 de la vérification de la note v2).
~~~~

### E-02 — ligne 4

avant :

~~~~
- les versions relevées au manifeste (clé `versions`, rien d'autre du manifeste) ;
~~~~

après :

~~~~
- les versions relevées au manifeste (clé `versions`, réduite aux clés de `manifeste.versions()` ; toute autre clé : refus) ;
~~~~

### E-03 — ligne 8

avant :

~~~~
- les lignes `etats_par_lot` de l'évaluation, réduites à six clés permises (toute autre clé : refus).
~~~~

après :

~~~~
- les lignes `etats_par_lot` de l'évaluation, réduites à six clés permises, chaque valeur de type et de valeur permis
  (adaptateur et dose de la condition, lot entier, empreinte hexadécimale ; toute autre clé ou valeur : refus).
~~~~

### E-04 — ligne 26

avant :

~~~~
from controle_ia.gardes import GardeArret
~~~~

après :

~~~~
from controle_ia.gardes import GardeArret
from controle_ia.manifeste import BIBLIOTHEQUES
~~~~

### E-05 — ligne 34

avant :

~~~~
CLES_ETAT = ("adaptateur", "condition", "dose_apres", "dose_avant", "empreinte", "lot")
~~~~

après :

~~~~
CLES_ETAT = ("adaptateur", "condition", "dose_apres", "dose_avant", "empreinte", "lot")
CLES_VERSIONS = frozenset(("python", "plateforme") + tuple(BIBLIOTHEQUES))
ADAPTATEUR_ET_DOSE = {"H": ("eleve", 0.0), "B50": ("eleve", 0.5), "B100": ("eleve", 1.0), "TJ100": ("temoin-jumeau", 1.0)}
~~~~

### E-06 — ligne 64

avant :

~~~~
        raise GardeArret("manifeste : versions absentes ou mal formées")
~~~~

après :

~~~~
        raise GardeArret("manifeste : versions absentes ou mal formées")
    if not set(versions) <= CLES_VERSIONS:
        raise GardeArret(f"manifeste : versions, {len(set(versions) - CLES_VERSIONS)} clé(s) hors de manifeste.versions()")
~~~~

### E-07 — ligne 94

avant :

~~~~
            raise GardeArret(f"etats_par_lot[{i}] : condition {l['condition']!r} hors de l'évaluation")
~~~~

après :

~~~~
            raise GardeArret(f"etats_par_lot[{i}] : condition {l['condition']!r} hors de l'évaluation")
        adaptateur, dose = ADAPTATEUR_ET_DOSE[l["condition"]]
        if (l["adaptateur"] != adaptateur or type(l["lot"]) is not int or l["lot"] < 1
                or any(type(l[k]) is not float or l[k] != dose for k in ("dose_avant", "dose_apres"))
                or not isinstance(l["empreinte"], str) or not re.fullmatch(r"[0-9a-f]{64}", l["empreinte"])):
            raise GardeArret(f"etats_par_lot[{i}] : valeur hors permis (adaptateur et dose de la condition, lot entier, empreinte)")
~~~~

### E-08 — ligne 106

avant :

~~~~
p = argparse.ArgumentParser(prog="extrait_iib_cote_moniteurs_v1")
~~~~

après :

~~~~
p = argparse.ArgumentParser(prog="extrait_iib_cote_moniteurs_v2")
~~~~

### E-09 — ligne 12

avant :

~~~~
    PYTHONPATH=src python scripts/extrait_iib_cote_moniteurs_v1.py --racine .
~~~~

après :

~~~~
    PYTHONPATH=src python scripts/extrait_iib_cote_moniteurs_v2.py --racine .
~~~~

### 5.3 Essais v1 (`29561a4c…`) → `tests/test_iib_extrait_cote_moniteurs_v2.py`

### T-01 — ligne 11

avant :

~~~~
"scripts" / "extrait_iib_cote_moniteurs_v1.py"
~~~~

après :

~~~~
"scripts" / "extrait_iib_cote_moniteurs_v2.py"
~~~~

### T-02 — ligne 38-39

avant :

~~~~
        etats = [{"condition": c, "lot": 1, "adaptateur": "eleve", "dose_avant": 0.5, "dose_apres": 0.5, "empreinte": "e" * 64}
                 for c in ex.CONDITIONS]
~~~~

après :

~~~~
        etats = [{"condition": c, "lot": 1, "adaptateur": ex.ADAPTATEUR_ET_DOSE[c][0], "dose_avant": ex.ADAPTATEUR_ET_DOSE[c][1],
                  "dose_apres": ex.ADAPTATEUR_ET_DOSE[c][1], "empreinte": "e" * 64} for c in ex.CONDITIONS]
~~~~

### T-03 — ligne 98

avant :

~~~~
def test_artefact_pas_d_ecrasement(tmp_path):
~~~~

après :

~~~~
@pytest.mark.parametrize("ecart", [
    {"lot": {"tours": 7}}, {"lot": 1.0}, {"adaptateur": "temoin-jumeau"}, {"dose_avant": 0.5}, {"dose_apres": 1},
    {"empreinte": "e"}, {"empreinte": {"k": 1}},
])
def test_artefact_valeur_d_etat_hors_permis(tmp_path, ecart):
    ligne = {"condition": "H", "lot": 1, "adaptateur": "eleve", "dose_avant": 0.0, "dose_apres": 0.0, "empreinte": "e" * 64}
    _course(tmp_path, etats=[{**ligne, **ecart}])
    assert _jouer(tmp_path, tmp_path / "x.json") == 1


def test_artefact_versions_cle_hors_permis(tmp_path):
    _course(tmp_path)
    p = tmp_path / "runs" / RUN / "manifeste.json"
    m = json.loads(p.read_text())
    m["versions"]["regle"] = "jamais copiée"
    p.write_text(json.dumps(m))
    (tmp_path / "runs" / RUN / "manifeste.json.sha256").unlink()
    sceller(p)
    s = tmp_path / "x.json"
    assert _jouer(tmp_path, s) == 1
    assert not s.exists()


def test_artefact_pas_d_ecrasement(tmp_path):
~~~~

## 6. Remarques à la mère (sans couple)

1. **Le dossier de la note.** `docs/notes/barreau8-iib-v1/` mêle, d'après les seuls noms, des pièces du côté exposé (mandats des développeurs du code du saboteur, du rédacteur de l'ordre et des contre-lectures ; contre-lectures, contrôles courts et vérifications du code, de l'ordre et du devis ; chemin critique des saboteurs discrets ; nœuds du repli de deuxième ligne) et des pièces dont le nom touche aux sondes (identités des fichiers de sondes). Le point (e) ne ferme, par son texte, que les contre-lectures, contrôles et vérifications ; **les mandats ne sont pas nommés**, et un mandat de développeur porte d'ordinaire la spécification du code. Je n'ai ouvert aucune de ces pièces : le classement par nom est à confirmer par la mère. Recommandation : transmettre la note hors de ce dossier (copie à l'identique, même empreinte, sous un chemin du côté moniteurs), et ajouter au point (e), dans la version suivante, une règle sur ce dossier qui en excepte les seules pièces écrites pour le côté moniteurs. Confiance : moyenne (je ne connais pas le contenu de ces pièces).
2. **Phrase de l'empreinte git** (ajout de la ligne 20) : non vérifiée ici, faute de copie locale du fichier et sans appel réseau. Elle n'est vraie que si l'hébergeur garde ce fichier en git ordinaire, où l'étiquette rendue est l'empreinte git du contenu ; si le fichier était tenu par le stockage des gros fichiers, l'étiquette serait son empreinte sha256 et l'égalité annoncée serait impossible. Aucune portée sur le mécanisme.
3. **Version suivante de la note** : son point d'en-tête ne doit pas réintroduire de chemin ni d'empreinte vers les pièces de fabrication ; la liste de ses différences et ce rapport restent du côté exposé.
4. **Écart du vérificateur** : empreintes d'abord calculées par joker sur mon bloc-notes, puis recalculées par noms explicites (en-tête). Lignes d'appel de `scripts/repetition_jouet_t07_v2.py`, vues par accident : à inscrire, si la mère le juge utile, à la liste « qui a lu quoi » (je suis déjà exclu du côté sondes).

## 7. Moyens de contrôle

Tout est dans le bloc-notes de cette session, non versé : pièces extraites par `git show` ; sortie du rejeu de l'exécutante ; contre-épreuve indépendante ; différentiel recalculé ; copie de l'arbre du commit pour les essais ; artefacts du vérificateur ; programmes qui appliquent à blanc les couples W, E et T et qui ont tiré de la note et du programme les blocs de la section 5, puis relecture de ce rapport par un programme qui en extrait les blocs et les rejoue sur les pièces d'origine.
