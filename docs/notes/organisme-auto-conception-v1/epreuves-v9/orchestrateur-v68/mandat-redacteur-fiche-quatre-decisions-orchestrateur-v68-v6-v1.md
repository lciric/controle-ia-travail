VERSION DE PYTHON : `python3 --version` ; AUCUN `-c`, AUCUN `-` APRÈS PYTHON3

# Mandat du rédacteur — fiche des quatre décisions sur l'orchestrateur v68, version 6 (correction C2) — v1

Pièce de travail (classe C). Donné par la session du compte organisme le 2026-11-20, sur GO-2026-11-20-03 (« non je veux fable » : la correction est rédigée par un rédacteur de modèle F, pas recopiée par un autre modèle) et la place Fable cédée par la mère.

## Qui

Un rédacteur neuf, modèle F. Tu signes « rédacteur neuf, modèle F ».

## Ce qui fait foi

Dans `docs/notes/organisme-auto-conception-v1/epreuves-v9/orchestrateur-v68/` du dépôt `/home/user/controle-ia-travail` ; vérifie chaque empreinte contre son compagnon :
- la cible, `fiche-quatre-decisions-orchestrateur-v68-v4.md` (`7910e74b9952635df92d5cb7039b8a1e3ec024d4c74cf7724707a34ee79b1b48`) ;
- le contrôle de son différentiel, `controle-differentiel-fiche-orchestrateur-v68-v4-v1.md` (`e538fcb34df66299682a0648234644cd0b64fb04c5978ae3fd0ff22baf57e2f4`), verdict « Conforme après corrections », une seule correction : **C2**, dont il donne le texte exact ;
- la note `note-retrait-fiche-v5-recopie-mot-de-lazar-v1.md` (`abf9d404fb53b2dfb0c8e6b9ec3ded7e524ff9f21f83274ac87f0e968bf10c44`) : une v5 faite par recopie existe et est **retirée** ; tu ne pars pas d'elle, tu ne la cites que pour dire pourquoi la version suivante s'appelle v6 ;
- `note-interruption-fiche-v4-limite-fable-v1.md` et le mandat de la v4 (`mandat-redacteur-fiche-quatre-decisions-orchestrateur-v68-v4-v1.md`) pour le contexte.

## Ce que tu fais

1. Tu appliques **C2 à la lettre** à la v4, et rien d'autre sur le fond. Le contrôleur a relevé que, C2 appliquée, la phrase se lit « sont au rapport joint (rapport du rédacteur de la v3, … ; la v4 n'a pas de rapport de rédacteur, …) » : si tu juges que « au rapport joint » ne se lit plus juste, tu ne le changes pas ; tu le dis dans ton rapport, et le contre-lecteur tranchera.
2. Tenue seulement : le titre passe à « v6 » ; tu écris en tête de l'en-tête une ligne de version qui dit, en tes mots, que la v6 remplace la v4 après le contrôle de son différentiel, que seule C2 est appliquée, que la v5 (recopie, `c5694a88089f1cbc3c664e6396826d895142390e3497cfb40aedf44700b19882`) est retirée sur le mot de Lazar (GO-2026-11-20-03) et que la suite de l'en-tête parle de la v4. Aucune autre modification.
3. Les remplacements passent par l'outil contre-lu : écris le fichier JSON des remplacements (`remplacements-fiche-orchestrateur-v68-v4-v6.json`) avec l'outil d'écriture de fichiers, puis `python3 -B /home/user/controle-ia-travail/scripts/remplacer_texte_exact_v1.py --cible …v4.md --remplacements …json --sortie TON_DOSSIER/fiche-quatre-decisions-orchestrateur-v68-v6.md` (vérifie que l'empreinte de l'outil commence par `391db990`).
4. Tu calcules le différentiel `diff -u` v4 → v6 (`differentiel-fiche-orchestrateur-v68-v4-v6.diff`) et tu écris ton rapport (`rapport-redacteur-fiche-orchestrateur-v68-v6-v1.md`) : ce que tu as appliqué, empreintes, le point « au rapport joint ». Chaque fichier rendu a son compagnon `.sha256` (`sha256sum F > F.sha256` depuis ton dossier).

Ton dossier : `/tmp/claude-0/-home-user-controle-ia-travail/227b647d-2ece-5654-bf04-8493b3ed2f19/scratchpad/redacteur-fiche-orchestrateur-v68-v6/`.

## Interdits

Jamais de heredoc ni de bloc de texte ou de code en ligne passé à un interpréteur ; une commande simple à la fois. Aucune écriture dans le dépôt, aucun commit. **Aucune commande, même une empreinte, une liste ou une taille, sur un chemin sous `archives-reponses-modeles/`.** Jamais le nom d'une commande d'arrêt ou de recherche de processus par motif. Aucun appel à un fournisseur de modèles, aucune dépense. Aucun identifiant de modèle dans tes pièces. Au premier refus d'un outil : arrête-toi et dis-le.
