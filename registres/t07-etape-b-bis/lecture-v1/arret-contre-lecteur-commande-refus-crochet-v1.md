# Arrêt de la session de lecture de l'apprentissage des sondes sur la tâche (étape B bis de T0.7) — refus du crochet du dépôt chez le contre-lecteur de la commande de lecture, puis chez la conductrice — v1

Session conductrice `session_013QMayjNC5GKdDFTN87oAV5`, 2026-11-18, arrêt vers 23:10Z. Aucune mesure, aucun score, aucune aire, aucune issue n'a été lu par quiconque dans cette session. La commande de lecture (`registres/t07-etape-b-bis/lecture-v1/commande-lecture-bbis-v1.md`, `b308c9b12803ea58b470a7670881fc30274f0c93c04bc288d893146c6641e615`) n'a jamais été jouée ; sa première contre-lecture n'est **pas finie** : aucun rapport écrit ni scellé, aucune conclusion. À l'heure de l'arrêt : étape 0 non faite ; lecteur-opérateur et juge non lancés.

## Refus n° 1, mot pour mot (rendu par le contre-lecteur de la commande, sous-agent neuf, Opus 5.5)
`PreToolUse:Bash hook error: [command hook]: GARDE (registres/go, R10) — commande bloquée : R10 — arrêt par motif de ligne de commande interdit ; arrêter par PID ou identifiant d'instance`

Cause rendue par l'agent : une recherche en lecture seule dans le fichier du crochet lui-même (`.claude/hooks/garde_calcul.py`, précédée de l'affichage de `.claude/settings.json`), dont le motif de recherche portait deux noms de commandes d'arrêt de processus par motif ; le crochet l'a prise pour un tel arrêt. Rien n'a tourné ; l'agent n'a rien reformulé, découpé ni contourné ; il s'est arrêté.

## Refus n° 2, même texte mot pour mot (reçu par la conductrice)
En voulant écrire et sceller ce compte rendu par une commande de terminal dont le texte citait la cause du refus n° 1, donc ces mêmes deux noms. Rien n'a été écrit. La conductrice ne l'a pas rejoué ; elle a rendu les deux refus à la session mère par message (23:10Z) et s'est arrêtée.

## Suite accordée par la session mère (message du 2026-11-18 à 23:11:12Z ; R-3517 sur `main`)
Faux positif de la garde de l'arrêt de processus. La recherche refusée n'est refaite par personne. Un contre-lecteur neuf de la commande, d'un autre modèle que le préparateur, peut être lancé, son mandat interdisant tout nom de commande d'arrêt de processus par motif dans une ligne de commande et toute recherche de ces noms. Ce compte rendu est écrit en nommant la cause par une périphrase, sans recopier les deux mots, puis scellé. Avant la contre-lecture neuve, le préparateur écrit une commande version 2, sous un nom neuf, qui traite les cinq constats provisoires ci-dessous.

## Ce que le contre-lecteur avait établi avant l'arrêt (provisoire, non scellé par lui)
- Empreintes des dix pièces citées : conformes à leurs compagnons.
- Par les noms, à la tête `c049cd60…` de la branche de travail et au commit de `main` `4aefb5b1…` : dépôt non superficiel ; aucun fichier de lecture ou d'arrêt de l'étape B suivi à l'un ou l'autre commit (la fusion de `main` n'en apporte pas) ; journal des ouvertures absent des deux ; fichier d'issue de l'épreuve du signal planté et fichiers de registre cités suivis.
- Formes vérifiées contre le code, conformes : les quatre options du module ; la forme du nom du run ; l'enveloppe du résultat ; la commande de vérification des sceaux ; les recherches de l'antériorité ; les cinq points de la preuve d'entrée conjointe ; la ligne d'en-tête du journal ne porte pas la chaîne que le module compte comme une ouverture.

## Constats provisoires de l'agent sur la commande (non contre-lus ; entrées de la contre-lecture neuve)
1. **Contrôle manquant avant le lancement** : l'écriture du résultat crée un manifeste décisif, qui exige le préenregistrement scellé (sections, absence de marqueurs de gabarit, empreintes de la section « Contre-lecture ») ; ce contrôle s'exécute après le seuil — un échec consommerait la lecture. Il porte sur le texte scellé seul et peut être fait avant le lancement sans rien rejouer de la garde.
2. **Mode de lancement** : un lancement en arrière-plan depuis un appel d'outil peut ne pas survivre à l'appel (délai de l'outil), alors que la durée de la lecture est inconnue et qu'un processus arrêté après le seuil consomme la lecture ; il faut un lancement détaché de l'outil, identifiant de processus relevé, sortie dans un fichier.
3. **Arrêt avant le seuil** : aucun bloc n'extrait de la sortie gardée ce que l'opérateur doit rendre ; une trace d'erreur ou un refus des options n'impriment pas la ligne d'arrêt.
4. **Appels au distant** (récupération des branches nommées, lecture des têtes) : les règles communes disent « aucun appel à un service extérieur » ; permission à écrire dans le mandat de l'opérateur.
5. **Le constat de forme d'après lecture laisserait voir à la conductrice** si l'issue est « non lue » de fond ou « lecture faite » ; il doit aller au juge seul, la conductrice ne recevant que « écrit », le chemin et l'empreinte.

Non commencé par lui : fonctions d'ajout de ligne au registre propre et de journal ; chargement du code de la pièce « mots et coût » (arrêts possibles avant le seuil) ; notes de la contre-lecture du code ; points ouverts de la commande, dont le classement de l'inscription de la ligne `LECTURE-BBIS` sur une issue « non lue » de fond.

## Qui a lu quoi (depuis le premier compte rendu d'arrêt)
| agent | modèle | fichiers de résultat ouverts |
|---|---|---|
| conductrice | Fable 5.2 | aucun ; lignes bornées du registre des accords et du registre des décisions sur `main` (GO-56, 60, 61, 64 ; R-3512, R-3514 ; une ligne d'accord voisine, sans résultat, est apparue une fois dans une recherche) ; noms seuls des variables d'environnement de git |
| préparateur | Fable 5.2 | aucun ; rien joué sur le réel |
| rédacteur des addenda | Fable 5.2 | aucun |
| contre-lecteur des addenda | Opus 5.5 | aucun |
| développeur | Fable 5.2 | aucun ; rien joué sur le réel |
| contre-lecteur du code | Opus 5.5 | aucun ; rien joué sur le réel |
| contre-lecteur de la commande (premier) | Opus 5.5 | aucun ; arrêté par le refus |
| lecteur-opérateur, juge | — | non lancés |
