# Mandat du rédacteur — fiche des quatre décisions sur l'orchestrateur v68, version 2 — v1

Pièce de travail (classe C). Donné par la session du compte organisme le 2026-11-19 vers 23:33Z, sur GO-2026-11-19-93 (reprise) et l'ordre de file accepté par la mère.

## Ce que tu fais

Tu écris la version 2 de la fiche (`fiche-quatre-decisions-orchestrateur-v68-v2.md`) à partir de la version 1 (`fiche-quatre-decisions-orchestrateur-v68-v1.md`, `52741f65…`, intacte, R12), en appliquant les **dix-neuf corrections à la fiche** de la contre-lecture `contre-lecture-fiche-quatre-decisions-orchestrateur-v68-v1.md` (même dossier, `af90dae4…`), **à la lettre quand elle donne un texte exact**, et ses trois corrections au rapport dans un rapport v2. Tu revois en plus, comme rédacteur, la **recommandation de la décision 4** (machine jetable), puisque la contre-lecture montre que le précédent invoqué (course v67) est celui de l'autre option : dis ta recommandation revue, sa confiance et sa raison.

Tiens compte des décisions de Lazar prises depuis la v1 : GO-2026-11-19-89 (rien du juge servi aux proposeurs dans les courses qui comptent ; la note servie n'existe que comme bras d'attaque déclaré) ; GO-2026-11-19-81 et -85 (ligne 1) ; GO-2026-11-19-76 et -77 (héritage). Si une décision de la fiche est déjà tranchée par l'une d'elles, dis-le et retire-la des décisions ouvertes.

Pour tout remplacement de texte, utilise l'outil contre-lu `python3 -B scripts/remplacer_texte_exact_v1.py --cible F --remplacements R.json --sortie NOUVEAU` (empreinte `391db990…`) ; il refuse un ancien absent ou multiple, ou un neuf recréé par jonction : élargis alors le contexte. Produis le différentiel v1 → v2.

## Ce que tu lis

`CLAUDE.md` ; la fiche v1, son rapport, son mandat ; la contre-lecture `af90dae4…` ; les pièces qu'elle cite (dont `docs/notes/organisme-boucle-reelle-v1/course-v67/verdict-course-v67-v1.md` et `registres/depenses.md` sur main) ; sur main, `registres/go.md` (GO-2026-11-19-55 à -93). Vérifie chaque empreinte avant de citer.

## Ce que tu rends

Dans ton bloc-notes seulement : la fiche v2, `differentiel-fiche-orchestrateur-v68-v1-v2.diff`, `rapport-redacteur-fiche-orchestrateur-v68-v2-v1.md`, ton JSON de remplacements. En-tête : « Auteur : rédacteur neuf, modèle F » ; aucun identifiant de modèle ; heure par `date -u`.

## Interdits

VERSION DE PYTHON : `python3 --version` ; AUCUN `-c`, AUCUN `-` APRÈS PYTHON3. Jamais de heredoc ni de bloc de texte ou de code en ligne passé à un interpréteur. Aucun lancement de l'orchestrateur. Aucun appel à un fournisseur de modèles, aucune dépense, aucune machine, aucun réseau sauf `git fetch`/`git show` du dépôt. Aucun commit, aucune poussée, aucune écriture dans le dépôt. Aucune valeur de clé. **Aucune commande, même une empreinte, une liste ou une taille, sur un chemin sous `archives-reponses-modeles/`.** Jamais le nom d'une commande d'arrêt ou de recherche de processus par motif dans une commande. Au premier refus d'un outil : arrête-toi et dis-le.
