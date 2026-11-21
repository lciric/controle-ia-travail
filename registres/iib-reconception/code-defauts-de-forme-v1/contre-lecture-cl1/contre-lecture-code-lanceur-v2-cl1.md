# Contre-lecture du lanceur de session du saboteur à budget, version 2 — contre-lecteur 1

Pièce d'instrument (classe B). Commit lu : `e2c90f97`, branche locale `prep/iib-code-v5`. Fichiers : `scripts/lancer_iib_v2.sh` et `tests/test_iib_lanceur_forme_v2.py`, comparés à `scripts/lancer_iib_v1.sh`. Rien n'a été modifié dans l'arbre. Aucun appel au loueur : seul le faux outil des essais a été employé. La garde de calcul n'a pas été lue (consigne de la mère après un refus de la garde, rapporté à part).

## Verdict : **autorisable après corrections** (un bloquant, trois majeurs)

Les trois corrections font, dans leur cas nominal, ce qu'elles disent :
- le chemin de l'outil est vérifié, dit et refusé clairement ;
- la ligne qui effaçait la réponse brute a disparu ;
- la destruction passe `-y`, ne vise que l'identifiant consigné et relit l'inventaire.

En revanche, la sous-commande neuve de destruction donne une capacité irréversible, et cette capacité repose sur une lecture fragile de la réponse du loueur. Un de mes essais d'attaque **détruit une machine d'un autre chantier** (remarque 1). Par ailleurs, les traces versées gardent des secrets en clair dans des formes courantes (remarques 3 et 4).

Essais ciblés rejoués dans l'arbre : `PYTHONPATH=src python3 -m pytest -q tests/test_iib_lanceur_forme_v2.py tests/test_iib_scripts_v1.py` → **103 passed in 90.37s**.

## Remarques

### Bloquant

**1. Une réponse piégée fait consigner, puis détruire, une machine d'un autre chantier.**
- Où : `scripts/lancer_iib_v2.sh`, l. 313 (lecture de l'identifiant), l. 316-318 (consignation) et l. 378-380 (seule garde de la destruction).
- Ce qui ne va pas : `ID` est le premier motif `new_contract: <chiffres>` trouvé n'importe où dans la réponse, `msg` compris. Il est écrit dans `lancement.txt`. La destruction ne vérifie ensuite que l'égalité avec cette ligne.
- Preuve (essai d'attaque 1) : la réponse `{"msg": "previous new_contract: 58936096 released", "success": true, "new_contract": 777777}` donne « CRÉÉE : instance 58936096 ». Ensuite, `destruction 58936096` rend « DÉTRUITE », code 0, et l'inventaire ne garde plus que l'instance du saboteur. Or l'ordre parle de cinq machines intouchables.
- En version 1, le même défaut de lecture existait, mais aucune commande de destruction n'en dépendait.
- Correction :
  - (a) lire la réponse par programme (JSON, puis forme `repr` de Python), clé `new_contract` au premier niveau seulement ; refuser, avec le code 4, si plusieurs valeurs sont trouvées ;
  - (b) dans `destruction`, avant `destroy`, exiger que l'entrée de l'inventaire d'avant pour cet identifiant porte une étiquette qui commence par `iib` (la même règle que la création) ; refuser sinon, code 2, sans appel ;
  - (c) un essai d'attaque pour (a) et pour (b).

### Majeurs

**2. Un inventaire vide par erreur vaut preuve : code 0 et `destruction_verifiee … deja_absente`.**
- Où : l. 148-153 et 389-393.
- Ce qui ne va pas : une liste vide, ou `{"instances": null}`, rendue alors que l'instance existe donne « DÉJÀ ABSENTE », code 0, et la ligne `destruction_verifiee` est écrite. Aucune commande n'est envoyée et l'instance continue de coûter. Une liste vide peut venir d'une erreur du compte, d'une clé d'un autre compte ou d'un filtre.
- Preuve : essai d'attaque 2.
- Correction : « déjà absente » doit rendre un code propre et non 0 (par exemple 7, « absence non confirmée, aucune commande envoyée »), sans écrire `destruction_verifiee`. On peut aussi exiger, pour conclure à l'absence d'avant, un inventaire non vide qui porte au moins une autre machine connue, ou un second appel ciblé sur l'identifiant. Le code 0 ne doit venir qu'après une commande au code 0 suivie d'une absence relue.

**3. Les inventaires versés aux traces gardent en clair les secrets des autres machines.**
- Où : l. 133-140 (`vast_masque` ne passe que par `masquer`, l. 68-75, qui ne remplace que les valeurs des clés de l'environnement local) ; l. 263, 323, 386 et 405.
- Ce qui ne va pas : l'inventaire du compte porte les variables d'environnement et les jetons des autres machines (`extra_env`, jeton de bloc-notes). Ces valeurs sont inconnues de l'environnement local, donc non masquées. Or elles sont maintenant copiées et empreintées dans `traces-location/`, que le § 6 du rapport propose de verser.
- Preuve : essai d'attaque 5, deux traces sur deux portent le secret et le jeton en clair.
- Correction : ne conserver de l'inventaire que les champs filtrés de l'identifiant créé (`id`, `label`, `actual_status`, `machine_id`, prix), ou passer l'inventaire entier par `masquer_reponse`. Le rapport doit cesser de proposer le versement de l'inventaire entier.

**4. Le masquage de la réponse de création ne voit pas les secrets en paires.**
- Où : l. 110-116.
- Ce qui ne va pas : le motif des champs nommés exige `"NOM": "valeur"` ou `NOM=valeur`. La forme en paires `[["MY_API_KEY", "secret"]]`, qui est celle d'`extra_env`, passe. Un secret écrit avec des caractères échappés en JSON (`\/`, `\u…`) échappe aussi au remplacement des valeurs de l'environnement.
- Preuve : essai d'attaque 6, secret en clair dans la copie empreintée.
- Correction :
  - ajouter le motif `["NOM", "valeur"]` ;
  - remplacer aussi la forme échappée en JSON de chaque valeur de l'environnement ;
  - dire dans la sortie que le masquage n'est pas une garde des secrets (la garde des secrets reste exigée avant tout versement : l'écrire dans l'ordre, ce que le rapport dit déjà en § 5 point 4).

### Mineurs

5. **Dossier écrasé à chaque destruction, contrairement à R12** (l. 398, `mv -f` vers `destruction-sortie.txt` ; l. 138, `mv -f` des inventaires ; l. 289, `: > "$NBM"`, et le nom fixe `creation-brute-masquee.tmp`). Une seconde destruction écrase la sortie de la première dans le dossier de session (essai d'attaque 7). Les copies datées de `traces-location/` survivent, donc rien n'est perdu tant que `conserver` réussit ; si elle échoue, l'écrasement perd la trace. Correction : noms datés, ou `mv -n` avec refus.
6. **« Gardée, jamais supprimée » est inexact quand le masquage échoue** (l. 137, 357-358 et 395-399). Si la commande Python de masquage échoue, le flux brut est perdu dans le tube : le fichier « gardé » est vide ou partiel. Correction : écrire d'abord la sortie brute dans un fichier temporaire, sur un disque local et non versé, puis masquer depuis ce fichier ; ou bien dire honnêtement « sortie perdue ».
7. **La sortie d'erreur des appels d'inventaire est jetée** (l. 135, `2>/dev/null`). Quand l'inventaire est illisible, sa cause est perdue, contre R-3661. Correction : rediriger vers un fichier `.err` daté, masqué.
8. **Copie de trace exposée à une course entre deux lancements** (l. 127-128) : le test `-e`, puis `cp` sans `-n`, peut écraser une trace si deux sous-commandes tournent dans la même seconde (surveillance en tâche de fond). Correction : `cp -n`, puis vérifier l'empreinte, ce qui est déjà fait.
9. **Extrait des champs du chemin d'échec** (l. 302-308) : si le masquage a échoué, l'extrait est lu dans l'original non masqué et ne passe que par `masquer` (valeurs de l'environnement). Les 300 caractères de `msg` peuvent porter un secret d'une autre forme. Correction : ne pas imprimer l'extrait quand le masquage a échoué.
10. **Identifiant vide : code 1 et message brut de bash** (l. 377, `${2:?}`), alors que l'usage annonce 2. Aucun appel n'est fait, donc c'est sans danger. Correction : test explicite, code 2.
11. **Aucune garde de calendrier sur la destruction.** Rien n'empêche d'appeler `destruction` avant le rapatriement vérifié ou avant le mot de la mère (ordre, § 5 étapes 5 et 6 ; R-3722 : « destruction seulement après le diagnostic scellé »). Correction minimale : exiger une ligne `rapatriement_verifie` (ou `mot_mere …`) dans `lancement.txt`, ou un argument explicite ; à défaut, l'écrire en tête de l'étape 6 de l'ordre neuf.
12. **Essais, à renforcer.**
    - Les essais de masquage n'éprouvent que les formes pour lesquelles les motifs ont été écrits ; ils sont donc biaisés vers le succès (R4).
    - `test_le_faux_outil_exige_la_confirmation` n'éprouve que le faux outil, pas le lanceur. La preuve que l'essai sain mord sur `-y` n'existe qu'en démonstration à la main, hors de la suite : à verser dans la suite, avec une copie du lanceur privée de `-y`.
    - `test_le_programme_ne_supprime_aucune_sortie_de_la_location` est une garde textuelle : elle ne voit ni `mv -f` ni `>` qui écrasent (remarque 5).
    - Ajouter mes attaques 1 à 6 comme artefacts.

### Régressions par rapport à la version 1

Aucune trouvée. Le `diff` ne montre que des ajouts et des remplacements localisés :
- la garde de calcul reste sur la commande imprimée (l. 278), avec `GO_ID` exigé (l. 160) ;
- les refus, les codes 2, 3, 4 et 5 et l'interdit des variables du mandataire sont inchangés ;
- `command -v "$VAST"` est remplacé par `resoudre_outil`.

Seul écart de comportement, dit par le développeur : un `VAST` donné comme nom nu (`VAST=vastai`) est maintenant refusé.

## Rapport du développeur, § 5 et § 6

- **Pas de « quatre points à trancher ».** Le § 5 compte huit points, dont un seul est dit « à trancher » (le point 7).
  - Point 2 (option `-y` non vérifiée sur l'outil réel) : à vérifier sur le poste de l'exécutante avant tout emploi, par `destroy instance --help` de la version 1.8.3 ; c'est une condition, pas un détail.
  - Point 4 : juste, mais sous-estimé (remarque 4).
  - Point 5 : juste, et aggravé par la version 2, qui multiplie les copies (remarque 3).
  - Point 7 : à trancher par la mère.
- **§ 6, ce qu'il faut ajouter :**
  - (a) Le changement de `EMPREINTES_CODE_IIB` et de la configuration scellée de la course (36 fichiers) touche une pièce décisive. Il s'agit d'un ordre et d'une configuration en version nouvelle, avec contre-lecture complète, et non d'une ligne de routine : le dire.
  - (b) L'étape 6 doit garder ses bornes (rapatriement vérifié, mot de la mère, 48 heures, 2026-11-28T00:00Z) et dire le sort des codes 6, 4 et du « déjà absente » (remarque 2).
  - (c) Le § 7 ne doit verser `traces-location/` qu'après la garde des secrets et sans les inventaires entiers (remarque 3).
  - (d) `IIB_DESTRUCTION_RELECTURES` et `IIB_DESTRUCTION_ATTENTE_S` ne sont pas dans `ENVI` : les valeurs par défaut s'appliquent, à dire.
  - (e) Le § 5, étape 1, doit faire relever par l'exécutante la sortie de `destroy instance --help` (point 2 ci-dessus).

## Sorties brutes

Essais ciblés (dans l'arbre) :
```
........................................................................ [ 69%]
...............................                                          [100%]
103 passed in 90.37s (0:01:30)
```

Essais d'attaque : `test_attaques_lanceur_v2_cl1.py` (ce dossier). Chaque essai affirme le comportement sûr : un échec signale un défaut. Sortie complète : `sortie-essais-attaque-cl1.txt`. Extrait :
```
APRES-CREATION : 0 CRÉÉE : instance 58936096 (...) | consigné : ['instance 58936096']
DESTRUCTION de l'autre : 0 DÉTRUITE : instance 58936096 absente de l'inventaire (relecture 1/2) ; commande de destruction rendue avec le code 0 | inventaire : [61414494]
INVENTAIRE VIDE : 0 ... INSTANCE 61414494 DÉJÀ ABSENTE DE L'INVENTAIRE : aucune commande de destruction envoyée
ERREUR APRES DESTRUCTION : 4 DESTRUCTION INCERTAINE : commande de destruction rendue avec le code 1, inventaire illisible (...) : l'absence de l'instance 61414494 n'est pas établie   [tenu]
IDENTIFIANT '061414494' -> 2 ; '61414494 ' -> 2 ; '61414494\n' -> 2 ; '' -> 1   [aucun appel ; code 1 pour le vide]
TRACES D'INVENTAIRE AVEC SECRET EN CLAIR : ['instances-apres-destruction-…json', 'instances-avant-destruction-…json']
SECRET EN PAIRE DANS LA COPIE : True
destruction-sortie.txt, 1re puis 2e : 'failed with error 500 ; Authorization: B' -> 'destroying instance 61414494.\n' | copies datées : 2
6 failed, 1 passed in 14.43s
```
