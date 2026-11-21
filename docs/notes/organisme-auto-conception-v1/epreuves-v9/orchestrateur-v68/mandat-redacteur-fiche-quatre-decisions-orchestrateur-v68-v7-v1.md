VERSION DE PYTHON : `python3 --version` ; AUCUN `-c`, AUCUN `-` APRÈS PYTHON3

# Mandat du rédacteur — fiche des quatre décisions sur l'orchestrateur v68, version 7 (corrections D1 à D3) — v1

Pièce de travail (classe C). Donné par la session du compte organisme le 2026-11-20, sur GO-2026-11-20-03 (corrections rédigées par un rédacteur de modèle F) et la place Fable cédée par la mère.

## Qui

Un rédacteur neuf, modèle F. Tu signes « rédacteur neuf, modèle F ».

## Ce qui fait foi

Dans `docs/notes/organisme-auto-conception-v1/epreuves-v9/orchestrateur-v68/` du dépôt `/home/user/controle-ia-travail` ; vérifie chaque empreinte contre son compagnon :
- la cible, `fiche-quatre-decisions-orchestrateur-v68-v6.md` (`9c43d54aa1efd541d4a2db70835090ccd4bc8f2a783cfa41cddb9a53f126221e`) ;
- le contrôle de son différentiel, `controle-differentiel-fiche-orchestrateur-v68-v6-v1.md` (`86a80de15fedcacbc906befb6c0b5aee8d3ecdd47d34f540dd857268db7d7398`), verdict « Conforme après corrections » : trois corrections **D1, D2, D3**, dont il donne le texte exact ;
- le rapport du rédacteur de la v6 (`rapport-redacteur-fiche-orchestrateur-v68-v6-v1.md`) et le rapport du rédacteur de la v1 (`rapport-redacteur-fiche-orchestrateur-v68-v1.md`, `49df651bdbb6615ae5ead6343741d8f2f3ad5d0aef9b69eaf82d0af140c2bfda`), pour vérifier les renvois.

## Ce que tu fais

1. Tu appliques **D1, D2 et D3 à la lettre** à la v6, et rien d'autre sur le fond.
2. Tenue seulement : le titre passe à « v7 » ; tu écris en tête de l'en-tête une ligne de version qui dit, en tes mots, que la v7 remplace la v6 après le contrôle de son différentiel, que seules D1 à D3 sont appliquées et que la suite de l'en-tête parle des versions précédentes. Aucune autre modification.
3. Les remplacements passent par l'outil contre-lu : JSON des remplacements (`remplacements-fiche-orchestrateur-v68-v6-v7.json`) écrit avec l'outil d'écriture de fichiers, puis `python3 -B /home/user/controle-ia-travail/scripts/remplacer_texte_exact_v1.py --cible …v6.md --remplacements …json --sortie TON_DOSSIER/fiche-quatre-decisions-orchestrateur-v68-v7.md` (empreinte de l'outil commençant par `391db990`).
4. Différentiel `diff -u` v6 → v7 (`differentiel-fiche-orchestrateur-v68-v6-v7.diff`, lancé depuis ton dossier, noms relatifs si possible) et rapport (`rapport-redacteur-fiche-orchestrateur-v68-v7-v1.md`). Chaque fichier rendu a son compagnon `.sha256`.

Ton dossier : `/tmp/claude-0/-home-user-controle-ia-travail/227b647d-2ece-5654-bf04-8493b3ed2f19/scratchpad/redacteur-fiche-orchestrateur-v68-v7/`.

## Interdits

Jamais de heredoc ni de bloc de texte ou de code en ligne passé à un interpréteur ; une commande simple à la fois. Aucune écriture dans le dépôt, aucun commit. **Aucune commande, même une empreinte, une liste ou une taille, sur un chemin sous `archives-reponses-modeles/`.** Jamais le nom d'une commande d'arrêt ou de recherche de processus par motif. Aucun appel à un fournisseur de modèles, aucune dépense. Aucun identifiant de modèle dans tes pièces. Au premier refus d'un outil : arrête-toi et dis-le.
