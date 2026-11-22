# Journal — brouillons 4 de l'ordre de course et de la consigne du lecteur (T0.8)

Écrit par `brouillons/t08-texte-complet-fable-v1/faire-pieces-de-course-t08-brouillon4-v1.py`. Cause unique : le rendu du développeur de la chaîne de lancement, `docs/notes/t08-chaine-de-lancement-v1/rapport-chaine-de-lancement-t08-v2.md` (`47da96229401335b5b87b32111b4df1d56bb7da15a33c94fd21288d33aaf13b7`, branche `t08/chaine-de-lancement-v1`, commit `12eb328a6bf84960116e4b26bbad332f0df0f257`). « commandes » : ce que ce rapport donne ou demande ; « arrêts » : sa réserve 9 (messages d'arrêt qui portent un nombre) ; « renvoi » : renvoi d'un brouillon à l'autre. La consigne du juge de verdict reste au brouillon 3.

## `ordre-course-t08-v1-brouillon3.md` → `ordre-course-t08-v1-brouillon4.md`

| n° | cause | ancien (début) | nouveau (début) |
|---|---|---|---|
| 1 | renvoi | sur une machine louée — v1 — brouillon 3 | sur une machine louée — v1 — brouillon 4 |
| 2 | commandes | - **Statut** : **brouillon 3**, pièce de classe A, **non exécutable** : la chaîne de lancement n'existe pas en… | - **Statut** : **brouillon 4**, pièce de classe A : **le brouillon des commandes**. Il ajoute au brouillon 3 (… |
| 3 | commandes | ; le brouillon des commandes y portera les commandes exactes, quand la chaîne sera écrite et contre-lue. Aucun… | ; ce brouillon 4 y porte les commandes exactes. Aucune machine ne se crée tant qu'un préalable manque. |
| 4 | renvoi | les corrections des brouillons 2 et 3 sont à vérifier par le même contre-lecteur. | les brouillons 2 et 3 ont été vérifiés conformes par le même contre-lecteur (`prereg/contre-lectures/T0.8-piec… |
| 5 | commandes | leurs empreintes sont celles de cet ordre (brouillon des commandes) ¦ | leurs empreintes au commit `C` sont celles du rapport de contre-lecture de la chaîne ; l'essai du code aligné … |
| 6 | renvoi | Les commandes exactes sont au brouillon des commandes. | Les commandes exactes sont en section 13. |
| 7 | commandes | Un écart : c'est le quatrième arrêt de la section 7, et l'étape 10 bis. | Un écart : c'est le quatrième arrêt de la section 7, et l'étape 10 bis. **Fin en anomalie de taille** (rapport… |
| 8 | renvoi | sous sa consigne (`consigne-lecteur-t08-v1-brouillon3.md`) | sous sa consigne (`consigne-lecteur-t08-v1-brouillon4.md`) |
| 9 | renvoi | ## 12. À écrire au brouillon des commandes | ## 12. Ce qui était à écrire, et qui l'est en section 13 |
| 10 | commandes | l'identifiant de la session exécutante. | l'identifiant de la session exécutante (donné par la session mère). ⏎  ⏎ ## 13. Commandes exactes ⏎  ⏎ Source … |

Entrée : `6922ada9651f4bbcb9d9347dff105c003c136c702a63b79cc3e5a4f7ae6d01e8`. Sortie : `553be7d1ce6f0eb5090aa97e529f3d86189625122e60564516c773dc926e1d7d`. Opérations : 10.

## `consigne-lecteur-t08-v1-brouillon3.md` → `consigne-lecteur-t08-v1-brouillon4.md`

| n° | cause | ancien (début) | nouveau (début) |
|---|---|---|---|
| 1 | renvoi | jouer la lecture sur processeur — v1 — brouillon 3 | jouer la lecture sur processeur — v1 — brouillon 4 |
| 2 | commandes | - **Statut** : brouillon 3. Il inscrit au brouillon 2 | - **Statut** : brouillon 4, **le brouillon des commandes**. Il ajoute au brouillon 3 (`6a39a5d9aa1dc0e289494c0… |
| 3 | commandes | La commande exacte de la lecture vient au brouillon des commandes, quand l'entrée en ligne de commande exister… | Les commandes exactes sont au § 5 ; elles ne valent qu'au commit que cite `CODE-T08`, après la contre-lecture … |
| 4 | arrêts | les messages d'arrêt et les lignes de progression du programme, qui ne portent que des noms d'étape et d'état … | les lignes de progression du programme, qui ne portent que des noms d'étape et d'état, et ses messages d'arrêt… |
| 5 | commandes | Tu joues **une fois** la commande de la lecture (brouillon des commandes), | Tu écris la configuration de la lecture, puis tu joues **une fois** la commande de la lecture (les deux ci-des… |
| 6 | commandes | et s'arrête sur toute ligne de la liste d'arrêt. | et s'arrête sur toute ligne de la liste d'arrêt. ⏎  ⏎ - Configuration : `PYTHONPATH=src python3 -B scripts/ecr… |
| 7 | arrêts | Tu recopies le message d'arrêt tel quel et tu le rends à la session mère. | Tu ne recopies pas le message d'arrêt à la session mère, qui ne doit recevoir aucun nombre tiré des résultats … |
| 8 | commandes | brouillon des commandes : chemin du fichier d'échantillon | fichier `diag/<run de la lecture>/echantillon-audit-r4-t08.json`, dont le programme imprime le chemin et l'emp… |
| 9 | arrêts | - Tout message d'arrêt, tel quel ; tout refus d'outil ; | - Tout arrêt, par le chemin et l'empreinte de `arret-lecture-t08.json`, jamais par son texte ; tout refus d'ou… |

Entrée : `6a39a5d9aa1dc0e289494c0fea0828fdc8216f866f0358b08446605881c89cdf`. Sortie : `043e1a9eebbbf273499dce6e6c2190155f5367e9da9289b2490c9b443a632733`. Opérations : 9.

