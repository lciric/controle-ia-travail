# Notice d'emploi — code de la lecture des sondes du barreau 8, côté moniteurs — v1

Pour le lecteur neuf des sondes. Cette notice dit comment lancer le code, dans quel ordre, avec quelles entrées, ce qu'il refuse et ce qu'il rend. **Elle ne porte aucun résultat.** Le verdict n'est pas prononcé par ce code : il rend une sortie mécanique scellée (états, lignes déclenchées, réserves) que le juge neuf applique à la table des critères gelés.

## Pièces qui font foi

- Texte préenregistré, brouillon 9 : `brouillons/barreau8-lecture-sondes-v1/prereg-lecture-sondes-barreau8-v1-brouillon9.md`, empreinte `aca110b0635abf9e7e5a1bdd1dc66b94aaae40ad5c72a6e7d6127967f87f272d`. **Le texte scellé aura une autre empreinte** (il ne différera du brouillon 9 que par l'entropie des graines et une entrée de contre-lecture) : cette empreinte se lit sur la ligne `SCELLEMENT-SONDES-IIB` du registre propre et se porte au bordereau du code ; elle n'est jamais devinée, ni écrite ici.
- Note d'interface, version 6 : `docs/notes/barreau8-cote-moniteurs-entrees-v1/interface-passe-cote-moniteurs-v6.md`, empreinte `20c9ed6e480646b6bf3a5f6007be5f88b439c916763a618f3880634e92ad8ce1`.
- Formats de la livraison : bloc « Noms et champs, liste fermée » de la section de la passe du texte. La section « Livraison : liste fermée, noms, formats » de la notice de la passe (`docs/notes/barreau8-cote-moniteurs-sorties-v1/notice-passe-recalcul-v1.md`, `45da9b99be0a3f9dacbf0a98aae570982f1f8b4dfb000920a402ec202c9aa472`) a été lue pour comparaison ; le code de la passe n'a pas été lu.
- Code : `src/controle_ia/barreau8_moniteurs/lecture_sondes_v1.py` ; essais : `tests/test_barreau8_moniteurs_lecture_v1.py` (empreintes dans leurs compagnons `.sha256`).

## Ce que tu ne fais pas

Tu ne choisis aucune sonde, aucune couche, aucun seuil. Tu n'ouvres ni la consigne privée, ni la conception, ni le verdict du témoin positif planté (le code n'en contrôle que l'existence et l'empreinte). Tu ne relances pas la lecture : elle se fait une seule fois. Tu n'inscris pas toi-même les lignes de registre : le code les imprime, la session mère les inscrit.

## Ordre des commandes

Toutes se lancent de la racine du dépôt, avec `PYTHONPATH=src` et l'environnement `.venv`. Abréviation ci-dessous : `LECTURE` = `PYTHONPATH=src .venv/bin/python -m controle_ia.barreau8_moniteurs.lecture_sondes_v1`, `REG` = `registres/sondes-iib-v1.md`. Les trois fichiers de sondes sont passés par leur chemin sur ton disque :

- `--sondes-legeres` : `sondes-figees-legeres.npz` (empreinte `701f73bd…4e60`) ;
- `--planchers` : `planchers-figees-t07.npz` (empreinte `94ca013c…f224`) ;
- `--sondes-neuves` : `sondes-neuves-t07.npz` (empreinte `374ad473…bb79`, rebâti de ses neuf morceaux).

Chacun doit avoir son compagnon `.sha256` à côté de lui. Les empreintes entières sont celles de la table des identités du texte ; le code les porte en constantes.

### 0. Bordereau du code (une fois, par la session mère, après le scellement du texte)

```
LECTURE bordereau-code --racine . \
  --texte-scelle <chemin du texte scellé> \
  --rapport-conformite <chemin du rapport scellé du contrôle de conformité> \
  --notice docs/notes/barreau8-cote-moniteurs-sorties-v1/notice-lecture-sondes-v1.md \
  --accord-lecture GO-AAAA-MM-JJ-NN \
  --sortie <chemin du bordereau du code à écrire>
```

Écrit et scelle le bordereau du code de la lecture (six clés : `texte_scelle`, `modules`, `commit`, `rapport_conformite`, `notice`, `accord_lecture`), puis imprime la ligne `| CODE-LECTURE-SONDES-IIB | heure | chemin | empreinte |` prête à inscrire. Refus si le texte, le rapport ou la notice ne sont pas scellés, si un module chargé n'est pas, sous la racine, le fichier de même empreinte, ou si la sortie existe déjà.

### 1. Garde de réception de la livraison

```
LECTURE reception --racine . --registre REG \
  --sondes-legeres <…> --planchers <…> --sondes-neuves <…>
```

Exige au registre les lignes `SCELLEMENT-SONDES-IIB`, `CODE-PASSE-IIB`, `LIVRAISON-PASSE-IIB`. Joue r1 à r7 dans l'ordre et s'arrête au premier manque ; imprime « GARDE DE RÉCEPTION TENUE » et rien des scores. La commande `lecture` la rejoue de toute façon.

### 2. Contrôle de l'extrait des états

```
LECTURE etats --racine . --registre REG
```

Exige `SCELLEMENT-SONDES-IIB` et `ETATS-COURSE-IIB`. Imprime « EXTRAIT DES ÉTATS CONFORME » et aucune valeur.

### 3. Recette de la puissance et aires minimales détectables

```
LECTURE puissance --racine . --registre REG --entropie <F-3> --run-id AAAAMMJJ-HHMMSS-puissance-barreau8
```

Arbre de travail propre exigé (manifeste de run). Ne lit aucune donnée de la course. Écrit `runs/<run>/manifeste.json` et `diag/<run>/aires-minimales-detectables-barreau8-v1.json`, scellés ; à committer avant la lecture.

**Durée attendue, d'après le budget du texte (non mesurée ici)** : environ 12 secondes par répétition, soit environ 3,3 heures pour les cinq cases de f = 1 et environ 10 heures pour les quinze ; le budget est de douze heures sur quatre cœurs, sans carte. Le budget atteint, les cases non finies sont écrites « non calculée », rien d'autre ne change et le calcul n'est pas relancé. Si l'une des cinq cases de f = 1 manque, la lecture refuse (D-10) : fait à porter à la session mère.

### 4. Essai de la chaîne, puis lecture décisive : une seule commande

```
LECTURE lecture --racine . --registre REG \
  --sondes-legeres <…> --planchers <…> --sondes-neuves <…> \
  --entropie <F-3> --run-id AAAAMMJJ-HHMMSS-lecture-sondes-barreau8 \
  --registre-accords <registre des accords> \
  --puissance diag/<run de la recette>/aires-minimales-detectables-barreau8-v1.json \
  --mandat-lecteur <mandat scellé> --mandat-juge <mandat scellé> \
  --empreinte-liste-exclus <64 caractères> --empreinte-qui-a-lu-quoi <64 caractères> \
  --piece-ordre-scelle <pièce scellée de la comparaison de l'ordre>
```

**L'essai de la chaîne n'est pas une commande à part** : c'est une étape de celle-ci (plan, point 4, étape (d)) ; joué seul, il lirait des scores avant le manifeste. L'entropie est l'entier décimal du champ F-3 du texte scellé, sans séparateur. Arbre de travail propre exigé.

Déroulement : conditions de départ ; garde de réception ; manifeste de run avec la liste des sondes lues et toutes les graines ; conditions jugées ; essai de la chaîne ; lecture ; déclencheurs de l'audit ; sortie scellée. La commande imprime la ligne `| LECTURE-SONDES-IIB | heure | chemin | empreinte |` à inscrire ; cette ligne une fois inscrite, toute relance est refusée.

### 5. Audit de symétrie, seulement si un déclencheur a joué

```
LECTURE audit --racine . --registre REG \
  --sondes-legeres <…> --planchers <…> --sondes-neuves <…> \
  --sortie-lecture diag/<run de la lecture>/lecture-sondes-barreau8-v1.json
```

Partie mécanique de l'audit, pour l'auditeur neuf : rejoue la garde de réception, recalcule la lecture sous les mêmes graines et rend la liste fermée des défauts D1 à D4, puis la ligne AU-a ou AU-b. Refus si la sortie ne porte aucun déclencheur.

## Entrées attendues

| entrée | où | contrôle |
|---|---|---|
| registre propre | `registres/sondes-iib-v1.md` | lignes `\| CLÉ \| AAAA-MM-JJTHH:MM:SSZ \| chemin relatif \| sha256 \|`, quatre colonnes, une ligne par clé |
| texte scellé | chemin de la ligne `SCELLEMENT-SONDES-IIB` | scellé, conforme, à l'empreinte de la ligne ; porte l'entropie |
| bordereau du code de la lecture | chemin de la ligne `CODE-LECTURE-SONDES-IIB` | six clés ; modules chargés exactement ceux du bordereau |
| bordereau du code de la passe | chemin de la ligne `CODE-PASSE-IIB` | sept clés ; ses modules sont comparés à la trace |
| livraison de la passe | dossier du fichier cité par `LIVRAISON-PASSE-IIB` | garde de réception |
| extrait des états | chemin de la ligne `ETATS-COURSE-IIB` | forme fermée de la note version 6 |
| trois fichiers de sondes | options de la commande | empreintes entières de la table des identités, compagnon conforme |
| verdict du témoin positif planté et sa pièce d'issue | `docs/verdicts/verdict-P3-bis-v1.md` (`9b33c624…1e5c`), `docs/verdicts/verdict-P3-bis-v1-issue.json` (`c3a017ce…28d0`) | existence et empreinte seulement |
| aires minimales détectables | sortie de la commande `puissance` | scellée, même entropie, recette du texte, cinq cases de f = 1 |
| registre des accords | option | une ligne, et une seule, porte l'identifiant du bordereau du code |
| mandats du lecteur et du juge | options | scellés ; chacun cite les deux empreintes données |
| pièce de la comparaison de l'ordre scellé | option | scellée ; jamais ouverte |

**Livraison** (dossier `livraison/`, chaque fichier avec son compagnon) : `bordereau-livraison-passe-barreau8-v1.json` ; cinq archives en morceaux de 50 000 000 octets, chacune avec son fichier `….npz.morceaux.json` — `scores-par-action-passe-barreau8-v1.npz`, `scores-par-jeton-passe-barreau8-v1.npz`, `activite-brute-c7-…`, `activite-brute-c15-…`, `activite-brute-c23-passe-barreau8-v1.npz` ; `index-passe-barreau8-v1.jsonl` ; `trace-gardes-passe-barreau8-v1.json`. Les archives sont rebâties en mémoire : compter environ 1,5 Go de mémoire vive dans le pire cas.

## Conditions de départ vérifiées mécaniquement

Dans cet ordre ; au premier manque, refus, rien n'est ouvert plus avant.

1. Registre propre : les cinq lignes exigées, une par clé, quatre colonnes ; aucune clé hors des six ; chaque fichier cité présent, avec son compagnon, à l'empreinte de sa ligne ; chaque ligne antérieure à l'instant d'ouverture ; ordre par le rang et par l'heure, strictement — le scellement en premier ; code de la passe, code de la lecture et états après le scellement ; livraison après le code de la passe ; `LECTURE-SONDES-IIB` absente (sinon : lecture déjà faite).
2. Texte scellé conforme, à l'empreinte de la ligne ; l'entropie donnée y figure en décimal, sans séparateur.
3. Bordereau du code : six clés ; texte égal à celui de la ligne du scellement ; rapport et notice présents à leur empreinte ; modules `controle_ia` chargés exactement ceux du bordereau, aux mêmes empreintes.
4. Ligne d'accord de lecture (D-4).
5. Mandats (D-5) ; pièce de l'ordre scellé (D-6).
6. Témoin positif planté et pièce d'issue (D-9).
7. Aires minimales détectables (D-10).
8. Extrait des états (D-12).
9. Fichiers de sondes et de planchers (D-8), puis garde de réception r1 à r7 (D-11) ; r8 est descriptif.

## Sorties

- `runs/<run>/manifeste.json` : configuration et empreinte, versions, commit, liste des sondes lues, toutes les graines.
- `diag/<run>/lecture-sondes-barreau8-v1.json`, scellé. Il porte : le marquage ; l'en-tête (réserves, nom de la course, avertissement de l'extrait, contexte de la course sans effet sur le verdict, nombre d'actions sans jeton noté par condition, les quatre couples du repère de couche, les deux empreintes recopiées du mandat) ; l'état de chaque sonde ; les conditions jugées et leur cause ; l'essai de la chaîne, tirages compris ; les lignes du bras de production, chacune nommée ; l'état de chaque condition jugée et l'état agrégé ; les lignes déclenchées de la table des issues ; les lectures descriptives ; les lignes du **bras de diagnostic « moyenne », jamais en production**, qui n'entrent dans aucun état ; les déclencheurs de l'audit ; les aires minimales détectables.
- La ligne `LECTURE-SONDES-IIB`, imprimée.
- `diag/<run>/audit-mecanique-lecture-sondes-barreau8-v1.json` si l'audit est joué.

## Codes de refus

Code de sortie 2 : refus (« REFUS [code] … »), rien n'est ouvert plus avant, fait à porter à la session mère. Code 1 : arrêt d'une garde en cours de calcul. Code 0 : fait.

| code | sens |
|---|---|
| `[1]` | texte non scellé, non conforme, d'une autre empreinte, ou entropie absente du texte |
| `[4]` | verdict du témoin positif planté ou pièce d'issue absent ou d'empreinte différente |
| `[5]` | registre propre (ligne absente, répétée, mal formée, clé hors des six, ordre, empreinte, lecture déjà faite) ; bordereau du code ; modules chargés |
| `[7]` | garde de réception, cause autre ; action d'au moins un jeton noté sans score livré (ligne L6, de mémoire) |
| `[8]` | fichier de sondes ou de planchers absent, d'empreinte différente ou sans compagnon ; aucune sonde lue |
| `[15]` | sonde des couches 7 ou 23 non conforme ; audit demandé sans déclencheur |
| `[D-4]`, `[D-5]`, `[D-6]`, `[D-10]`, `[D-12]` | la condition de départ de ce nom |
| `[r1]` à `[r7]` | le point de la garde de réception de ce nom |

Un score infini, ou un score à une action sans jeton noté, arrête (liste d'arrêt, ligne 11).

## Ce qui n'a pas été éprouvé ici

- **La recette de puissance entière** (quinze cases, 200 répétitions, 800 directions, 2 000 tirages) : seule une grille réduite a tourné, avec l'étalonnage du décalage et le repli du budget. Sa durée n'est pas mesurée.
- **La garde de recalcul r6 aux tailles réelles** (largeur 4 096, 2 403 directions, 161 actions) : éprouvée à largeur 12 et 63 directions. Sa durée et sa mémoire réelles ne sont pas mesurées.
- **Les vrais fichiers de sondes** : aucun n'a été ouvert ; la règle mécanique est éprouvée sur des fichiers synthétiques écrits par le même écrivain (`ecrire_sondes`). Le fichier des sondes neuves pèse environ 430 Mo et se charge en entier.
- **Une vraie livraison** de la passe : la livraison d'essai est écrite par les essais, d'après le texte seul.
- La commande lancée par `python -m` : les essais appellent la fonction `main` ; le cas du module chargé sous le nom `__main__` est traité dans `modules_charges` mais n'a pas d'essai.

## Lectures strictes à connaître

- Le nom du bordereau de livraison doit être `bordereau-livraison-passe-barreau8-v1.json`.
- Les modules chargés sont tous les modules `controle_ia` du processus, fichiers `__init__.py` compris.
- Les deux libellés du tableau `agregations` ne sont pas fixés par le texte : le code exige deux chaînes non vides, sans les comparer.
- Le bordereau du code de la passe n'est lu que pour ses sept clés et ses modules ; son rapport, sa notice et son devis sont contrôlés par la passe.
