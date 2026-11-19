VERSION DE PYTHON : `python3 --version` ; AUCUN `-c`, AUCUN `-` APRÈS PYTHON3

# Mandat du rédacteur — palier 0b, préenregistrement version 6 (erratum) — v1

Pièce de travail (classe C). Donné par la session du compte organisme le 2026-11-20 vers 00:05Z, sur GO-2026-11-19-84 et -93.

## Ce que tu fais

Tu écris la version 6 (`preenregistrement-heritage-palier-0b-etage-processeur-v6.md`) à partir de la version 5 (`6230d6c3…`, intacte, R12), limitée aux **sept remplacements exacts** de la relecture `heritage/palier-0b/relecture-preenregistrement-palier-0b-v5-v1.md` (`8faf3940…`), appliqués **à la lettre**, plus une ligne à l'annexe G qui les inscrit, et la tenue (titre, statut, heure, mandat cité, relecture citée). Rien d'autre ne change.

Applique-les avec l'outil contre-lu `python3 -B scripts/remplacer_texte_exact_v1.py --cible F --remplacements R.json --sortie NOUVEAU`, en tirant les textes exacts de la relecture par lecture du fichier. Produis le différentiel v5 → v6.

## Ce que tu rends

Dans ton bloc-notes seulement : la version 6, `differentiel-preenregistrement-palier-0b-v5-v6.diff`, un rapport court, ton JSON. En-tête : « Auteur : rédacteur neuf, modèle F » ; aucun identifiant de modèle ; heure par `date -u`.

## Interdits

Jamais de heredoc ni de bloc de texte ou de code en ligne passé à un interpréteur, même vide. Une commande simple à la fois ; pour l'environnement, `python3 -B scripts/verifier_environnement_agent_v1.py`. Aucun tirage, aucun lancement du code versé. Aucun appel à un fournisseur de modèles, aucune dépense, aucune machine, aucun réseau sauf `git fetch`/`git show` du dépôt. Aucun commit, aucune poussée, aucune écriture dans le dépôt. **Aucune commande, même une empreinte, une liste ou une taille, sur un chemin sous `archives-reponses-modeles/`.** Jamais le nom d'une commande d'arrêt ou de recherche de processus par motif. Au premier refus d'un outil : arrête-toi et dis-le.
