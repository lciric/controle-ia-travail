# Contre-lecture des deux instruments de la mère pour le juge de sélection — v1

Contre-lecteur neuf, Claude Fable 5.2 (`claude-fable-5-2`), 20 novembre 2026. Pièce de travail (contre-lecture d'instruments, classe B). Mandat : `mandat-contre-lecteur-fable-instruments-mere-v1.md` (`da74088f…283b9e`, empreinte vérifiée).

## Verdicts

- **Pièce 1, la garde de la graphie de `lignee_reconnue` : à corriger** (deux couples courts, A et B ci-dessous). Aucun chemin trouvé par lequel une valeur fautive sort avec le code 0 : la garde ferme bien. Les deux corrections portent sur un code de sortie faux sans rapport écrit, et sur un identifiant recopié sans contrôle de forme.
- **Pièce 2, l'extraction du cas X6 : le programme v2 est conforme** ; **la règle de R-4097 est à compléter avant le scellement du manifeste**. Rien de ce que j'ai lu ne contredit la liste X6 (2 fiches « à corriger ») ni `cartes_attendues` = 94. Mais trois points ne sont pas établis par les pièces lues, dont un indice matériel que le code lu par la mère n'est pas exactement celui qui a écrit le journal (voir « Ce qui menace le manifeste »).

## Empreintes vérifiées par `sha256sum`

Garde `5aceb2ab…4f8a61` ; essais de la garde `e9d18366…89b592` ; extraction v1 `e2da19df…bacb19` ; extraction v2 `004fc6b7…ad9dddb` ; essais v1 `39d282ee…11431b` ; essais v2 `0d721e7e…f3a127` ; contre-lecture Sonnet `88ed7ece…83a162` ; vérification Sonnet `e08ecda8…586b98` ; sortie v1 `a13699aa…7f9f3b` ; sortie v2 `f5c7cc1c…3659eb`. Toutes conformes au mandat ou aux pièces qui les citent.

Non vérifiées par empreinte, faute de pouvoir le faire en commande simple sans écrire un fichier : le programme d'assemblage scellé (`2f5640da…`) et le code de l'aiguilleur (`a856cdaa…`). Le commit de l'orchestrateur est bien `a41b7b50f7c64ce488c120bb89ad3d25fb1dd1cb` (`git rev-parse FETCH_HEAD`). Du programme d'assemblage, je n'ai lu que `valider_lecture` (l. 158 à 230) et `valider_liste_veto` (l. 233 à 245) ; un aperçu de la fin du fichier (les options de la ligne de commande) est apparu dans le résultat tronqué d'un premier `git show`, je ne l'ai pas cherché.

## Pièce 1 — la garde de `lignee_reconnue`

### Question 1 — refuse-t-elle toute valeur hors des clés de `familles` et de « aucune » ?

Oui, dans les cartes et dans les veto d'une lecture (l. 63 à 65 : texte exigé, puis appartenance exacte à l'ensemble des clés, sans rognage ni casse : « Opus », « prop-opus  » avec espace, « Aucune », valeur absente, nulle ou numérique sont refusées). Oui pour la lignée du lecteur (l. 53), avec le défaut A. La table lue est la même que celle que l'assemblage consulte (`manifeste["familles"]`).

Défaut A. Si `lignee` est une liste ou un objet, `lecture["lignee"] not in permis` lève `TypeError`, que `principal` ne rattrape pas : le programme sort par une trace, code 1 (et non 2), sans écrire de rapport ; un rapport plus ancien laissé au même chemin de sortie pourrait être pris pour le sien. La trace ne montre aucune valeur.

Limites, à déclarer et non à corriger ici :
- La garde ne prend qu'une lecture (objet à clés `lignee`, `cartes`, `veto`). Les listes de veto du juge, passées à l'assemblage par une option à part et validées par la même `valider_liste_veto`, portent elles aussi `lignee_reconnue` et ne passent pas par cette garde : une liste nue y sort en code 2. Je n'ai pas lu le reste de l'assemblage pour savoir comment ces valeurs sont comptées. À trancher par la mère : soit la garde reçoit un second mode pour ces listes, soit le manifeste dit qu'elles ne sont pas gardées.
- La garde ne lit pas `lignee_reconnue_declaree` du manifeste. Si cette clé est fausse, les cartes n'ont pas de `lignee_reconnue` et la garde les refuse toutes (code 1) : fermeture bruyante, sans danger, mais à savoir.
- Une lecture à zéro carte sort « conforme » ; l'assemblage la refuse ensuite. Sans danger.

### Question 2 — peut-elle écrire une note, une phrase, une raison ou la valeur fautive ?

La valeur fautive : non. Elle n'est jamais copiée ; le rapport ne porte que l'identifiant de l'entrée, et un booléen pour la lignée du lecteur. Une note ou une raison : non, ces clés ne sont jamais lues. Les motifs d'erreur (`JSONDecodeError`, `UnicodeDecodeError`, `OSError`, `Malforme`) ne portent qu'une position, un octet, un chemin, un nom de clé ou un rang.

Une phrase : oui, par un seul chemin, le défaut B. La valeur de `id` est recopiée telle quelle dès qu'elle est un texte non vide (l. 59 à 65). Une lecture mal formée dont le champ `id` porterait une phrase la ferait entrer dans le rapport. Le programme d'extraction X6 de la mère borne déjà ses identifiants par un motif ; la garde doit faire de même.

### Question 3 — codes de sortie

Essais rejoués par la commande du mandat : **9 réussis**. Par `principal` : code 0 sur un cas sain, code 1 sur une graphie fautive de carte, code 2 sur un JSON cassé. Les artefacts de veto, de lignée du lecteur, d'identifiant absent et de manifeste mal formé sont éprouvés sur les fonctions, pas sur le code de sortie ; acceptable, le code découle de `issue`. Manquent : l'artefact du défaut A, et un manifeste mal formé passé par `principal`.

### Corrections (fichier, avant, après)

Fichier : `garde_lignee_reconnue_v1.py` (nouvelle version, nouveau nom, R12).

Couple A, l. 53 :
- avant : `    refus = {"lignee_du_lecteur": lecture["lignee"] not in permis, "cartes": [], "veto": []}`
- après : `    refus = {"lignee_du_lecteur": not (isinstance(lecture["lignee"], str) and lecture["lignee"] in permis), "cartes": [], "veto": []}`

Couple B, en deux endroits :
- avant, l. 21 à 27 : `import argparse` / `import json` / `import sys` … `AUCUNE = "aucune"`
- après : ajouter `import re` parmi les imports, et sous `AUCUNE = "aucune"` la ligne `MOTIF_ID = re.compile(r"[A-Za-z0-9._:/-]{1,120}")`
- avant, l. 60 : `            if not (isinstance(ident, str) and ident.strip()):`
- après : `            if not (isinstance(ident, str) and MOTIF_ID.fullmatch(ident)):`

Si les identifiants réels des cartes ne tiennent pas dans ce motif, la garde sortira en code 1 avec des entrées « sans identifiant » : bruyant, et le motif se règle alors sur leur forme, sans la deviner.

Fichier : `essais_garde_lignee_reconnue_v1.py` (nouvelle version). Ajouter trois essais :
- lignée du lecteur en liste (`lignee=["prop-fable"]`) : `controler` rend `lignee_du_lecteur` vrai et `issue` « refusee », sans exception ;
- identifiant en phrase (`{"id": "une phrase avec des espaces", "lignee_reconnue": "Opus"}`) : `entrees_sans_identifiant` vaut 1 et « phrase » est absent de `json.dumps(r)` ;
- par `principal`, un manifeste `{"familles": {}}` : code 2 et `issue` « mal_formee ».

## Pièce 2 — l'extraction du cas X6 (contre-lecture après coup)

### Question 1 — le programme v2 pouvait-il écrire autre chose ?

Non, à une précision près que la liste du mandat omet : il écrit aussi **les valeurs de `classe`** (comme clés des comptes), bornées par le motif `^[a-z_]{1,40}$`. Le reste : version, commit et suffixe reçus en argument, nombre de fichiers, chemin, empreinte, taille, noms de clés des objets à `classe`, comptes, identifiants bornés par `^[A-Za-z0-9._:/-]{1,120}$`, doublons. Ni `categorie`, ni `contenu`, ni aucun texte libre : un identifiant ou une classe hors motif arrête le programme (codes 4 et 5) sans être écrit. Au code 3, la « forme » ne rend que des noms de clés, des types et des longueurs.

Réserves mineures, sans effet sur ce qui a été joué :
- `MOTIF_ID.match` et `MOTIF_CLASSE.match` avec `$` laissent passer un saut de ligne final ; `fullmatch` serait exact.
- Un `id` non textuel fait retomber sur la clé parente (déjà relevé par l'agent Sonnet) ; visible dans `source_identifiant`. Au passage réel : clé 2, parent 0, donc sans objet.
- Un échec de `git` (`CalledProcessError`) ou un JSON trop profond pour l'analyseur ne sont pas rattrapés : trace, code 1, pas de rapport.
- Le programme ne rend pas les deux comptes de tête du journal (`passeports`, `refus_aiguilleur`), qui sont des entiers et auraient recoupé le « 94 ».

Sortie v2, lue par ses seules lignes de champs et de comptes (aucun identifiant affiché ni recopié) : issue « conforme », 1 fichier, 957 octets, journal `e2ba2a33…95df`, 2 objets à `classe`, `a_corriger` = 2, source de l'identifiant : clé 2, parent 0, aucun doublon, 8 noms de clés. Conforme au rapport de l'agent Sonnet. Essais v2 rejoués (données fabriquées seulement) : **16 réussis**.

### Question 2 — le passage de la v1 à la v2 ne dépend-il que d'un nom de clé ?

Oui. `diff` des deux programmes : en-tête, `VERSION`, `ident` ajouté à `CLES_ID`, décodage des noms du commit avec `errors="replace"`. La sortie v1 (arrêt par le code 4) ne contient que des noms de clés, trois comptes, le chemin, l'empreinte et la taille ; `ident` y figure comme nom de clé. Aucune valeur du journal n'a pu guider la v2.

### Question 3 — la règle de R-4097 est-elle juste au regard du code de l'aiguilleur ?

Sur la logique du code lu, oui : dans `Aiguilleur.classer`, chaque appel qui rend la main finit soit par un passeport (classe `niveau_methode`), soit par une entrée ajoutée au journal sous « retenues » (toute autre classe ; un refus ou une réponse illisible sont retenus sous la classe `concret` avec `refus_aiguilleur` vrai). Les deux issues s'excluent pour un appel donné.

Trois choses que ce code n'établit pas :

1. **Le code lu n'est pas exactement celui qui a écrit le journal.** Au commit `a41b7b50…`, chaque entrée retenue porte neuf clés, dont `passe`. Le journal réel n'en porte que huit : `categorie`, `classe`, `contenu`, `empreinte`, `fournisseur`, `ident`, `origine`, `refus_aiguilleur` (sorties v1 et v2). `passe` manque. La course a donc tourné avec une autre version de l'aiguilleur. La règle est sans doute la même, mais R-4097 cite un code qui n'est pas prouvé être celui de la course.
2. **« Hors des 94 cartes à passeport » ne découle pas du seul aiguilleur.** Les passeports sont rangés par identifiant. L'arithmétique 96 = 94 + 2 montre que les 94 passeports ont 94 identifiants distincts, pas que les 2 identifiants retenus en sont absents : une fiche retenue puis représentée sous le même identifiant et passée donnerait les mêmes comptes. Et que les 94 fiches à passeport soient bien les 94 cartes offertes au choix relève de l'orchestrateur, que je n'ai pas lu. Le « 96 appels, 94 passeports » ne vient d'aucune pièce que j'ai lue.
3. **Le journal lu est celui de la seule première génération** (voir question 4).

### Question 4 — une fiche retenue pouvait-elle échapper au programme ?

Dans le fichier lu : non. Toute entrée de « retenues » porte une clé `classe`, refus et réponses illisibles compris (classés `concret`) ; le programme parcourt tout le JSON et s'arrête si un identifiant ou une classe est illisible. Zéro `concret` au passage réel, donc zéro refus retenu dans ce journal.

Hors du fichier lu : oui, par quatre voies que le programme ne voit pas.
- Le suffixe joué est `/generation-1/aiguillage/journal-aiguillage.json`. Le journal d'une autre génération, s'il existe, n'est ni lu ni compté : l'exigence « exactement un fichier » ne porte que sur ce suffixe.
- Chaque `Aiguilleur` exige un dossier de journal neuf, et `sceller_journal` accepte un autre nom de fichier : un second aiguilleur (la garde du proposeur Kimi, un étalonnage) écrirait ailleurs.
- Le journal n'existe sur disque qu'après `sceller_journal` : avant, les retenues ne vivent qu'en mémoire. Une étape interrompue avant ce scellement ne laisse aucun journal.
- `git show --name-only` ne liste que les fichiers changés par le commit donné : un journal versé par un autre commit échappe.

## Ce qui menace le manifeste

Rien ne contredit X6 = 2 fiches ni `cartes_attendues` = 94 ; trois contrôles manquent pour les tenir, tous par programme et sans lire une carte :

1. **Version de l'aiguilleur.** Retrouver dans le manifeste de la course le commit de l'orchestrateur réellement exécuté, relire `classer` et `sceller_journal` à ce commit, et corriger la référence de R-4097 par un erratum.
2. **Tous les journaux.** Compter, dans le commit de versement, les noms qui finissent par `/aiguillage/journal-aiguillage.json` sans le segment de génération (le programme v2 le fait tel quel avec ce suffixe plus court : code 0 s'il n'y en a qu'un, code 2 sinon, et il n'écrit alors que le nombre). C'est un second passage sur le dossier cloisonné : il lui faut le mot de Lazar, comme le premier.
3. **Intersection vide, écrite dans le manifeste.** Le programme qui bâtit le manifeste doit vérifier que les 2 identifiants de `hors_choix` sont absents des identifiants des 94 cartes, et s'arrêter sinon. Si l'un d'eux y figurait, `cartes_attendues` vaudrait 94 moins ce nombre, comme l'écrivait la table d'origine.

Pour la garde : ne pas l'employer avant les couples A et B ; décider du sort des listes de veto du juge.

## Ce que je n'ai pas fait

Rien ouvert sous `archives-reponses-modeles/`, aucune carte, aucune lecture, aucune transcription ; extraction non rejouée ; fichier partiel de la contre-lecture Sonnet de la garde non lu ; rien d'autre lu du dépôt de l'orchestrateur ; aucun identifiant de carte recopié ; aucun refus d'outil rencontré.
