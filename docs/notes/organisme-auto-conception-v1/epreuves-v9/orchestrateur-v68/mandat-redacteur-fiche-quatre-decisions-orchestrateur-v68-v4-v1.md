VERSION DE PYTHON : `python3 --version` ; AUCUN `-c`, AUCUN `-` APRÈS PYTHON3

# Mandat du rédacteur — fiche des quatre décisions sur l'orchestrateur v68, version 4 — v1

Pièce de travail (classe C). Donné par la session du compte organisme le 2026-11-19 vers 23:58Z.

Tu écris la version 4 (`fiche-quatre-decisions-orchestrateur-v68-v4.md`) à partir de la version 3 (`fiche-quatre-decisions-orchestrateur-v68-v3.md`, `bff07f80…`, intacte, R12), limitée à **la seule correction C1** du contrôle `controle-differentiel-fiche-orchestrateur-v68-v3-v1.md` (même dossier, `93a95bf9…`), appliquée **à la lettre**, plus la tenue (titre, statut, heure, mandat cité, contrôle cité, une ligne de différentiel v3 → v4). Rien d'autre ne change. Applique avec `python3 -B scripts/remplacer_texte_exact_v1.py --cible F --remplacements R.json --sortie NOUVEAU`, en tirant le texte exact du contrôle par lecture du fichier. Produis le différentiel v3 → v4.

Rends dans ton bloc-notes seulement : la fiche v4, `differentiel-fiche-orchestrateur-v68-v3-v4.diff`, un rapport court, ton JSON. En-tête : « Auteur : rédacteur neuf, modèle F » ; aucun identifiant de modèle ; heure par `date -u`.

Interdits : jamais de heredoc ni de bloc de texte ou de code en ligne passé à un interpréteur, même vide ; une commande simple à la fois ; aucun lancement de l'orchestrateur ; aucun appel à un fournisseur de modèles, aucune dépense ; aucun commit, aucune poussée, aucune écriture dans le dépôt ; **aucune commande, même une empreinte, une liste ou une taille, sur un chemin sous `archives-reponses-modeles/`** ; jamais le nom d'une commande d'arrêt ou de recherche de processus par motif. Au premier refus d'un outil : arrête-toi et dis-le.
