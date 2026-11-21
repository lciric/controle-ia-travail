VERSION DE PYTHON : `python3 --version` ; AUCUN `-c`, AUCUN `-` APRÈS PYTHON3

# Mandat du rédacteur — fiche des quatre décisions sur l'orchestrateur v68, version 3 — v1

Pièce de travail (classe C). Donné par la session du compte organisme le 2026-11-19 vers 23:52Z, sur GO-2026-11-19-93.

## Ce que tu fais

Tu écris la version 3 de la fiche (`fiche-quatre-decisions-orchestrateur-v68-v3.md`) à partir de la version 2 (`fiche-quatre-decisions-orchestrateur-v68-v2.md`, `2b8e3815…`, intacte, R12), en appliquant **à la lettre** les dix corrections V1 à V10 de la vérification `verification-fiche-quatre-decisions-orchestrateur-v68-v2-v1.md` (même dossier, `34995283…`) ; la correction facultative V11 seulement si elle tient en un remplacement à texte exact donné. La correction principale : la divergence entre GO-2026-11-19-89 et la lecture de la garde acceptée par GO-76 point 2 (servir à la génération suivante les seules survivantes, sans verdict) est posée à Lazar **comme question**, au verdict et dans la phrase de la décision 2, au format de `CLAUDE.md`. Plus la tenue (titre, statut, heure, mandat cité, vérification citée, section de différentiel v2 → v3).

Applique les remplacements avec l'outil contre-lu `python3 -B scripts/remplacer_texte_exact_v1.py --cible F --remplacements R.json --sortie NOUVEAU` ; vérifie l'environnement, si besoin, par `python3 -B scripts/verifier_environnement_agent_v1.py`. Produis le différentiel v2 → v3.

## Ce que tu lis

`CLAUDE.md` ; la fiche v2, son rapport, son mandat ; la vérification `34995283…`. Vérifie chaque empreinte avant de citer.

## Ce que tu rends

Dans ton bloc-notes seulement : la fiche v3, `differentiel-fiche-orchestrateur-v68-v2-v3.diff`, `rapport-redacteur-fiche-orchestrateur-v68-v3-v1.md` (court), ton JSON de remplacements. En-tête : « Auteur : rédacteur neuf, modèle F » ; aucun identifiant de modèle ; heure par `date -u`.

## Interdits

Jamais de heredoc ni de bloc de texte ou de code en ligne passé à un interpréteur, même vide. Une commande simple à la fois. Aucun lancement de l'orchestrateur. Aucun appel à un fournisseur de modèles, aucune dépense, aucune machine, aucun réseau sauf `git fetch`/`git show` du dépôt. Aucun commit, aucune poussée, aucune écriture dans le dépôt. Aucune valeur de clé. **Aucune commande, même une empreinte, une liste ou une taille, sur un chemin sous `archives-reponses-modeles/`.** Jamais le nom d'une commande d'arrêt ou de recherche de processus par motif. Au premier refus d'un outil : arrête-toi et dis-le.
