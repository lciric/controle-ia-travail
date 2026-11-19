# Notice d'emploi — code de la lecture des sondes du barreau 8, côté moniteurs — v5

Pour le lecteur neuf des sondes. Cette notice dit comment lancer le code, dans quel ordre, avec quelles entrées, ce qu'il refuse et ce qu'il rend. **Elle ne porte aucun résultat.** Le verdict n'est pas prononcé par ce code : il rend une sortie mécanique scellée (états, lignes déclenchées, réserves) que le juge neuf applique à la table des critères gelés. Elle remplace les notices v1 à v4, qui restent scellées à côté des versions 1 à 4 du code.

## Pièces qui font foi

- Texte préenregistré, **brouillon 13, spécification suivie par ce code** : `brouillons/barreau8-lecture-sondes-v1/prereg-lecture-sondes-barreau8-v1-brouillon13.md`, empreinte `7628ebfd8534bd44287e0a233a80339e6dde57db88fd0ada3df3c6a1b2305cd4`. **Le texte scellé aura une autre empreinte** : elle se lit sur la ligne `SCELLEMENT-SONDES-IIB` du registre propre et se porte au bordereau du code ; elle n'est jamais devinée, ni écrite ici. Si le texte scellé diffère du brouillon 13 ailleurs que par l'entropie et les entrées de contre-lecture, le code est à réaligner avant sa ligne de registre.
- Note d'interface, version 6 : `docs/notes/barreau8-cote-moniteurs-entrees-v1/interface-passe-cote-moniteurs-v6.md`, empreinte `20c9ed6e480646b6bf3a5f6007be5f88b439c916763a618f3880634e92ad8ce1`.
- Contre-lecture des versions courantes et troisième essai d'intégration (lecture version 4, passe version 5) : `docs/notes/barreau8-cote-moniteurs-sorties-v1/contre-lecture-codes-passe-v5-lecture-v4-integration-v1.md`, empreinte `c08e1ffb168454f44fb6f277423fe8e3d264ef24f2aa91d6e301cb5aa91cd1d4`.
- Contre-lecture de la version 3 du code et second essai d'intégration avec le code de la passe : `docs/notes/barreau8-cote-moniteurs-sorties-v1/contre-lecture-code-lecture-v3-integration-v1.md`, empreinte `c07e50324925f0d4e47ec09e6342737b9de477f0bd8a83e7df69a44cef210228`.
- Contre-lecture de la version 1 du code : `docs/notes/barreau8-cote-moniteurs-sorties-v1/contre-lecture-code-lecture-v1-v1.md`, empreinte `c5f12da08cce4ad086f8a8a3cbe317da2afe8b4800c8d4174c720d3a7146cb85`. Les durées et la mémoire données plus bas en viennent.
- Code : `src/controle_ia/barreau8_moniteurs/lecture_sondes_v5.py` ; essais : `tests/test_barreau8_moniteurs_lecture_v5.py` (empreintes dans leurs compagnons `.sha256`).

## Ce que tu ne fais pas

Tu ne choisis aucune sonde, aucune couche, aucun seuil. Tu n'ouvres ni la consigne privée, ni la conception, ni le verdict du témoin positif planté (le code n'en contrôle que l'existence et l'empreinte). Tu ne relances pas la lecture : elle se fait une seule fois, et le code refuse toute seconde lecture. Tu n'inscris aucune ligne de registre à la main : **la commande de lecture inscrit elle-même sa ligne `LECTURE-SONDES-IIB`** ; les cinq autres lignes sont inscrites par la session mère.

## Où poser les entrées

- **La livraison de la passe** : dans un dossier sous la racine du dépôt qui ne contient que la livraison et ses compagnons `.sha256` (rien d'autre : ni fichier de git, ni `.gitkeep`, ni archive entière). Le bordereau s'y nomme `bordereau-livraison-passe-barreau8-v1.json` ; c'est son chemin que cite la ligne `LIVRAISON-PASSE-IIB`.
- **L'extrait des états** : `docs/notes/barreau8-cote-moniteurs-entrees-v1/etats-lectures-iib-v1.json`, avec son compagnon ; c'est le chemin de la ligne `ETATS-COURSE-IIB`.
- **Arbre de travail propre** : les commandes `puissance` et `lecture` écrivent un manifeste de run et refusent un arbre git non propre. La livraison, l'extrait, le registre propre, les bordereaux et la sortie de la recette doivent donc être committés (ou ignorés par git) avant la lecture.
- **Les mandats et la pièce de comparaison de l'ordre scellé** : leurs chemins te sont donnés par la session mère. Le mandat du lecteur doit citer trois empreintes : la liste des exclus, le registre « qui a lu quoi », la pièce de comparaison de l'ordre.
- **Le registre des accords** : `registres/go.md`, passé par `--registre-accords`.

## Ordre des commandes

Toutes se lancent de la racine du dépôt. Abréviations : `LECTURE` = `PYTHONPATH=src .venv/bin/python -m controle_ia.barreau8_moniteurs.lecture_sondes_v5`, `REG` = `registres/sondes-iib-v1.md`. Les trois fichiers de sondes sont passés par leur chemin sur ton disque, chacun avec son compagnon `.sha256` :

- `--sondes-legeres` : `sondes-figees-legeres.npz` (empreinte `701f73bd…4e60`) ;
- `--planchers` : `planchers-figees-t07.npz` (empreinte `94ca013c…f224`) ;
- `--sondes-neuves` : `sondes-neuves-t07.npz` (empreinte `374ad473…bb79`, rebâti de ses neuf morceaux).

### 0. Bordereau du code (une fois, par la session mère, après le scellement du texte)

```
LECTURE modules
LECTURE bordereau-code --racine . \
  --texte-scelle <chemin du texte scellé> \
  --rapport-conformite <chemin du rapport scellé du contrôle de conformité> \
  --notice docs/notes/barreau8-cote-moniteurs-sorties-v1/notice-lecture-sondes-v5.md \
  --accord-lecture GO-AAAA-MM-JJ-NN \
  --sortie <chemin du bordereau du code à écrire>
```

`modules` imprime les modules `controle_ia` chargés et leurs empreintes (dix-sept, fichiers `__init__.py` compris ; le module lancé, que l'interpréteur nomme `__main__`, y figure sous le nom de son paquet). `bordereau-code` écrit et scelle le bordereau (six clés : `texte_scelle`, `modules`, `commit`, `rapport_conformite`, `notice`, `accord_lecture`) et imprime la ligne `| CODE-LECTURE-SONDES-IIB | heure | chemin | empreinte |` que la session mère inscrit. **Le bordereau doit être écrit par la même forme de lancement que la lecture** (`python -m`), pour que les mêmes modules soient chargés.

### 1. Garde de réception de la livraison

```
LECTURE reception --racine . --registre REG \
  --sondes-legeres <…> --planchers <…> --sondes-neuves <…>
```

Peut être jouée par la conductrice du côté des moniteurs ou par le lecteur, dès que les quatre lignes du scellement, du code de la passe, du code de la lecture et de la livraison sont inscrites, sans attendre les autres conditions. Elle ne reçoit pas l'entropie et ne contrôle pas la cellule F-3 ; elle ne lit pas l'extrait des états et ne compare donc pas le nom de la course. **Avant d'ouvrir quoi que ce soit de la livraison**, elle exige le code attesté comme la lecture : le texte scellé à l'empreinte de sa ligne, et les modules chargés exactement ceux du bordereau du code de la lecture. Ce n'est pas une lecture au sens de la liste d'arrêt : elle ne calcule aucune aire et n'imprime aucun score. Elle écrit « GARDE DE RÉCEPTION TENUE », ou le refus et sa cause, et les quatre couples du repère de couche (r8). Aucune cause de refus ne porte un score ni un écart de score : un recalcul qui ne se reproduit pas nomme la garde, l'action et la direction, rien de plus. La commande `lecture` la rejoue.

**Durée et mémoire, d'après la contre-lecture de la version 1 (estimées, non mesurées aux tailles réelles)** : 3 à 5 minutes ; pic de 2,5 à 3 Go de mémoire vive (les cinq archives sont rebâties en mémoire, et le fichier des sondes neuves, environ 430 Mo, est chargé en entier). Prévoir une machine avec au moins 4 Go libres.

### 2. Contrôle de l'extrait des états

```
LECTURE etats --racine . --registre REG
```

Imprime « EXTRAIT DES ÉTATS CONFORME » et aucune valeur.

### 3. Recette de la puissance et aires minimales détectables

```
LECTURE puissance --racine . --registre REG --entropie <F-3> --run-id AAAAMMJJ-HHMMSS-puissance-barreau8
```

Ne lit aucune donnée de la course. Écrit `runs/<run>/manifeste.json` et `diag/<run>/aires-minimales-detectables-barreau8-v1.json`, scellés ; à committer avant la lecture.

**Durée** : la contre-lecture a mesuré 5,7 secondes par répétition sur ce dépôt (quatre cœurs), soit, par extrapolation, environ 1,6 heure pour les cinq cases de f = 1 et environ 4,8 heures pour les quinze. Le budget du texte est de douze heures. Le budget atteint, les cases non finies sont écrites « non calculée », rien d'autre ne change et le calcul n'est pas relancé. Si l'une des cinq cases de f = 1 manque, la lecture refuse (D-10).

### 4. Essai de la chaîne, puis lecture décisive : une seule commande, une seule fois

```
LECTURE lecture --racine . --registre REG \
  --sondes-legeres <…> --planchers <…> --sondes-neuves <…> \
  --entropie <F-3> --run-id AAAAMMJJ-HHMMSS-lecture-sondes-barreau8 \
  --registre-accords registres/go.md \
  --puissance diag/<run de la recette>/aires-minimales-detectables-barreau8-v1.json \
  --mandat-lecteur <mandat scellé> --mandat-juge <mandat scellé> \
  --empreinte-liste-exclus <64 caractères> --empreinte-qui-a-lu-quoi <64 caractères> \
  --piece-ordre-scelle <pièce scellée de la comparaison de l'ordre>
```

**L'essai de la chaîne n'est pas une commande à part** : c'est une étape de celle-ci ; joué seul, il lirait des scores avant le manifeste. Sa forme est celle du brouillon 13. D'abord l'égalité des deux chemins : pour chaque sonde lue et chaque action honnête notée, le score d'action lu dans le tableau livré par la fonction même de la lecture décisive doit être égal, sans tolérance, au maximum recalculé des scores par jeton, sur des bornes que l'essai déduit lui-même de l'index ; une seule inégalité fait échouer l'essai, sans rejeu, et la sortie n'écrit que la sonde et le nombre d'actions inégales. Puis, dans chaque tâche, cinq des dix actions de l'épisode honnête reçoivent l'étiquette 1 (étiquetage apparié dans la tâche), tirées avant le retrait des actions sans jeton noté. Une tâche réduite à une classe après ce retrait n'est pas une cause d'échec : la sortie la nomme, avec la classe qui lui reste. L'entropie est l'entier de la cellule F-3 du texte scellé, écrit seul, en décimal, sans séparateur.

Déroulement : conditions de départ ; garde de réception ; manifeste de run ; conditions jugées ; essai de la chaîne ; lecture ; déclencheurs de l'audit ; sortie scellée ; **inscription de la ligne `LECTURE-SONDES-IIB` en fin de registre propre**, dans le même processus. Si l'inscription échoue, la commande s'arrête bruyamment (code 2) en nommant la sortie, qui reste écrite et scellée : la ligne est alors à inscrire par la session mère, et rien n'est relancé.

La lecture elle-même prend quelques minutes de plus que la réception (une soixantaine de comparaisons au plancher).

### 5. Audit de symétrie, seulement si un déclencheur a joué

```
LECTURE audit --racine . --registre REG \
  --sondes-legeres <…> --planchers <…> --sondes-neuves <…>
```

Pour l'auditeur neuf. Lit la sortie citée par la ligne `LECTURE-SONDES-IIB` ; contrôle les modules chargés contre le bordereau du code ; rejoue la garde de réception ; recalcule la lecture sous les mêmes graines ; rend la liste fermée des défauts D1 à D4 et la ligne AU-a ou AU-b, dans `diag/<run de la lecture>/audit-mecanique-lecture-sondes-barreau8-v1.json`, scellé. **Un recalcul r6 ou r7 qui ne se reproduit pas n'est pas un refus : c'est le défaut D2, écrit, issue AU-a.** Refus si la sortie ne porte aucun déclencheur. L'audit s'ouvre au moins une seconde après l'inscription de la ligne `LECTURE-SONDES-IIB`.

## Entrées attendues

| entrée | où | contrôle |
|---|---|---|
| registre propre | `registres/sondes-iib-v1.md` | lignes `\| CLÉ \| AAAA-MM-JJTHH:MM:SSZ \| chemin relatif \| sha256 \|`, quatre colonnes, une ligne par clé |
| texte scellé | chemin de la ligne `SCELLEMENT-SONDES-IIB` | scellé, conforme, à l'empreinte de la ligne ; sa cellule F-3 égale à l'entropie donnée |
| bordereau du code de la lecture | chemin de la ligne `CODE-LECTURE-SONDES-IIB` | six clés ; modules chargés exactement ceux du bordereau |
| bordereau du code de la passe | chemin de la ligne `CODE-PASSE-IIB` | sept clés ; noms et empreintes de ses modules comparés à la trace ; son champ de chemin n'est pas comparé |
| livraison de la passe | dossier du fichier cité par `LIVRAISON-PASSE-IIB` | garde de réception |
| extrait des états | chemin de la ligne `ETATS-COURSE-IIB` | forme fermée de la note version 6 |
| trois fichiers de sondes | options de la commande | empreintes entières de la table des identités, compagnon conforme |
| verdict du témoin positif planté et sa pièce d'issue | `docs/verdicts/verdict-P3-bis-v1.md` (`9b33c624…1e5c`), `docs/verdicts/verdict-P3-bis-v1-issue.json` (`c3a017ce…28d0`) | existence et empreinte seulement |
| aires minimales détectables | sortie de la commande `puissance` | scellée, même entropie, recette du texte, cinq cases de f = 1 |
| registre des accords | `registres/go.md` | une ligne, et une seule, dont la première cellule est l'identifiant du bordereau du code |
| mandats du lecteur et du juge | options | scellés ; chacun cite les deux empreintes données |
| pièce de la comparaison de l'ordre scellé | option | scellée ; jamais ouverte ; son empreinte est citée par le mandat du lecteur |

**Livraison** : `bordereau-livraison-passe-barreau8-v1.json` ; cinq archives en morceaux de 50 000 000 octets, chacune avec son fichier `….npz.morceaux.json` — `scores-par-action-passe-barreau8-v1.npz`, `scores-par-jeton-passe-barreau8-v1.npz`, `activite-brute-c7-…`, `activite-brute-c15-…`, `activite-brute-c23-passe-barreau8-v1.npz` ; `index-passe-barreau8-v1.jsonl` ; `trace-gardes-passe-barreau8-v1.json`. Les deux libellés des cases d'agrégation sont exigés à la lettre, dans cet ordre : `"maximum (production)"`, `"moyenne (bras de diagnostic, jamais en production)"`.

## Conditions de départ vérifiées mécaniquement

Dans cet ordre ; au premier manque, refus, rien n'est ouvert plus avant.

1. Aucune sortie `lecture-sondes-barreau8-v1.json` sous `diag/`.
2. Registre propre : les cinq lignes exigées, une par clé, quatre colonnes ; aucune clé hors des six ; chaque fichier cité présent, avec son compagnon, à l'empreinte de sa ligne ; chaque ligne antérieure à l'instant d'ouverture ; ordre par le rang et par l'heure, strictement — le scellement en premier ; code de la passe, code de la lecture et états après le scellement ; livraison après le code de la passe ; `LECTURE-SONDES-IIB` absente.
3. Texte scellé conforme, à l'empreinte de la ligne ; cellule F-3 égale à l'entropie donnée.
4. Bordereau du code : six clés ; texte égal à celui de la ligne du scellement ; rapport et notice présents à leur empreinte ; modules `controle_ia` chargés exactement ceux du bordereau, aux mêmes empreintes.
5. Ligne d'accord de lecture (D-4).
6. Mandats (D-5) ; pièce de l'ordre scellé, à l'empreinte citée par le mandat du lecteur (D-6).
7. Témoin positif planté et pièce d'issue (D-9).
8. Aires minimales détectables (D-10).
9. Extrait des états (D-12).
10. Fichiers de sondes et de planchers (D-8), puis garde de réception r1 à r7 (D-11) ; r8 est descriptif.
11. Nom de la course : celui de la trace de la passe égal à `run_id` de l'extrait des états (liste d'arrêt, ligne 3).

## Sorties

- `runs/<run>/manifeste.json` : configuration et empreinte, versions, commit, liste des sondes lues, les graines de la lecture et celle de la recette de puissance (les clés de la passe sont consignées par la passe).
- `diag/<run>/lecture-sondes-barreau8-v1.json`, scellé. Il porte : le marquage ; l'en-tête (réserves, nom de la course, avertissement de l'extrait, contexte de la course sans effet sur le verdict, nombre d'actions sans jeton noté par condition, nom de la course et commit de lancement selon la trace, les quatre couples du repère de couche, les deux empreintes recopiées du mandat) ; l'état de chaque sonde ; les conditions jugées et leur cause ; l'essai de la chaîne, tirages compris ; les lignes du bras de production ; l'état de chaque condition jugée et l'état agrégé ; les lignes déclenchées de la table des issues ; les lectures descriptives ; les lignes du **bras de diagnostic « moyenne », jamais en production**, qui n'entrent dans aucun état ; les déclencheurs de l'audit ; les aires minimales détectables. Chaque ligne porte le nom de son bras.
- Quand l'artefact positif de l'essai de la chaîne échoue : pour chaque sonde, l'aire de l'artefact et le quantile 0,95 du plancher sur le jeu de l'essai, sans autre effet (ligne L5).
- La ligne `LECTURE-SONDES-IIB`, inscrite au registre propre et imprimée.
- `diag/<run>/audit-mecanique-lecture-sondes-barreau8-v1.json` si l'audit est joué.

## Codes de refus

Code de sortie 2 : refus (« REFUS [code] … »), fait à porter à la session mère. Code 1 : arrêt d'une garde en cours de calcul. Code 0 : fait.

| code | sens |
|---|---|
| `[1]` | texte non scellé, non conforme, d'une autre empreinte, ou cellule F-3 différente de l'entropie donnée |
| `[3]` | nom de la course de la trace de la passe différent de `run_id` de l'extrait des états |
| `[4]` | verdict du témoin positif planté ou pièce d'issue absent ou d'empreinte différente |
| `[5]` | registre propre (ligne absente, répétée, mal formée, clé hors des six, ordre, empreinte) ; lecture déjà faite ou sortie déjà présente ; bordereau du code ; modules chargés ; inscription de la ligne échouée |
| `[7]` | garde de réception, cause autre ; action d'au moins un jeton noté sans score livré (ligne L6, de mémoire) |
| `[8]` | fichier de sondes ou de planchers absent, d'empreinte différente ou sans compagnon ; vecteur ou biais non fini ; aucune sonde lue |
| `[15]` | sonde des couches 7 ou 23 non conforme ou de nom en double ; audit demandé sans déclencheur |
| `[D-4]`, `[D-5]`, `[D-6]`, `[D-10]`, `[D-12]` | la condition de départ de ce nom |
| `[r1]` à `[r7]` | le point de la garde de réception de ce nom |

Un score infini, ou un score à une action sans jeton noté, arrête (liste d'arrêt, ligne 11).

## Ce qui a été éprouvé, et ce qui ne l'a pas été

**Éprouvé par le troisième essai d'intégration** (lecture version 4 et passe version 5, sur jouet ; la version 5 de la lecture n'en diffère que par la portée du contrôle de finitude et ne l'a pas refait) :

- une livraison écrite par le code de la passe est reçue par la garde de réception ; l'extrait des états est contrôlé ; la recette de puissance réduite tourne ;
- la lecture est jouée de bout en bout ; elle inscrit elle-même sa ligne `LECTURE-SONDES-IIB`, dernière du registre ; une seconde lecture est refusée ;
- un nom de course différent entre la trace et l'extrait des états fait refuser la lecture, sans sortie écrite ;
- l'égalité des deux chemins tient ; une tâche réduite à une classe est nommée, sans échec ;
- l'audit est ouvert par sa commande, sur une livraison fabriquée par les montages de mes essais (déclencheur d'aire haute, issue sans défaut).

Les commandes y ont été jouées par une enveloppe qui appelle la fonction `main` avec un cadre réduit : les tailles du texte (morceaux de 50 000 000 octets, 64 tâches, largeur 4 096, identités des vrais fichiers) sont en dur dans la ligne de commande, et aucune option ne les change.

**Non éprouvé** :

- **Les tailles réelles.** La vraie commande `python -m … reception` passe le registre, le texte scellé et les modules chargés, puis refuse la livraison jouet sur la taille de ses morceaux, comme attendu. Restent non mesurés : la garde de recalcul r6 (largeur 4 096, 2 403 directions, 161 actions), la lecture à 2 560 actions, l'essai de la chaîne à 64 tâches et 800 directions (éprouvé ici à 24 tâches de dix actions et 30 directions, avec et sans effet de tâche). Durée et mémoire sont des estimations de la contre-lecture.
- **La recette de puissance entière** : seule une grille réduite a tourné.
- **Les vrais fichiers de sondes** : aucun n'a été ouvert. Risques connus : un nom des couches 7 ou 23 du fichier léger qui ne serait pas une sonde linéaire par jeton agrégée par le maximum ferait refuser (`[15]`) ; un vecteur ou un biais non fini, dans une entrée au nom de l'une des neuf sondes nommées (cherchée dans l'index de chacun des trois fichiers) ou dans une direction candidate au plancher, aussi (`[8]`).
- **Le vrai registre des accords** : la ligne d'accord de lecture doit avoir pour première cellule l'identifiant seul, sans mise en forme, et être la seule ainsi ; sinon refus (`[D-4]`). Rien n'est exigé des autres lignes : d'anciens identifiants en double ne gênent pas.
- **Limite de l'égalité des deux chemins** : un champ `rang` faux mais cohérent dans l'index déplacerait les deux chemins ensemble et ne serait pas vu par l'essai ; c'est la garde r5 qui exige que le rang soit le rang dans le fichier.
