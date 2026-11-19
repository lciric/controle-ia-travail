VERSION DE PYTHON : `python3 --version` ; AUCUN `-c`, AUCUN `-` APRÈS PYTHON3

# Mandat du développeur — programme de vérification de l'environnement des agents (classe B) — v1

Pièce de travail (classe C). Donné par la session du compte organisme le 2026-11-19 vers 23:33Z, sur GO-2026-11-19-93, mesure (b) (main ; mot de Lazar vers 23:29Z).

## Pourquoi

Quatre refus d'outil ce jour, dont trois pour le même geste : des agents composent des commandes groupées de vérification et y glissent du code en ligne passé à l'interpréteur (`python3 -c`, `python3 -`, heredoc), ce que le classifieur refuse. Ce programme donne aux agents, dans un fichier qu'ils lancent par son chemin, tout ce qu'ils vérifient d'ordinaire au début d'un travail.

## Ce que tu écris

Dans ton bloc-notes, en reproduisant l'arborescence du dépôt : `scripts/verifier_environnement_agent_v1.py`, bibliothèque standard seulement, et ses essais `tests/test_verifier_environnement_agent_v1.py`.

Appel : `python3 -B scripts/verifier_environnement_agent_v1.py [--empreintes FICHIER_LISTE] [--modules numpy,pytest,...] [--depot CHEMIN] [--sortie FICHIER_JSON]`.

Il rend, en JSON (sur la sortie standard et, si demandé, dans un fichier neuf, jamais écrasé, avec compagnon `.sha256`) :
- version de Python, chemin de l'interpréteur, plateforme ;
- pour chaque module demandé : présent ou absent, et sa version s'il l'expose (import protégé ; aucun module tiers exigé par le programme lui-même) ;
- pour une liste de fichiers (un chemin par ligne, avec en option l'empreinte attendue) : existence, taille, sha256, égalité à l'empreinte attendue ; **refus de lire tout chemin qui contient le segment `archives-reponses-modeles`**, sans le toucher, avec un message clair ;
- dans un dépôt git donné : la tête (`git rev-parse HEAD`), la branche, et si l'arbre est propre (`git status --porcelain`), par appel de `git` avec une liste d'arguments fixe (aucun shell, aucune chaîne composée) ; le programme ne lance aucun autre processus que `git` ;
- l'heure UTC.

Codes de retour : 0 si tout est lu ; 3 si une empreinte attendue diffère ; 2 sur entrée invalide ou chemin refusé. Aucun réseau, aucune écriture hors du fichier de sortie et de son compagnon.

## Essais exigés

Un cas sain et un artefact pour chaque refus et chaque écart (R5), dont : chemin sous `archives-reponses-modeles` refusé sans accès ; empreinte différente, code 3 ; sortie existante refusée ; module absent rapporté sans erreur ; dépôt non git rapporté. Contrôle « trop beau » (R4) : défauts réintroduits un par un dans une copie, vus. Lance-les depuis ton bloc-notes (`PYTHONDONTWRITEBYTECODE=1 python3 -B -m pytest -q CHEMIN`).

Rapport court : `scripts/rapport-developpeur-verifier-environnement-agent-v1.md`.

## Interdits

Jamais de heredoc ni de bloc de texte ou de code en ligne passé à un interpréteur. Écris tes fichiers avec l'outil d'écriture ; pour modifier un fichier, `python3 -B scripts/remplacer_texte_exact_v1.py`. Aucune commande, même une empreinte, une liste ou une taille, sur un chemin sous `archives-reponses-modeles/`. Jamais le nom d'une commande d'arrêt ou de recherche de processus par motif dans une commande. Aucun commit, aucune poussée, aucun appel à un fournisseur de modèles, aucune dépense. Aucun identifiant de modèle ; signe « développeur, modèle L′ ». Au premier refus d'un outil : arrête-toi et dis-le.
