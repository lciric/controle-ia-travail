# Mandat du rédacteur — ligne 3 des épreuves v9, version 7 du préenregistrement (erratum) — v1

Pièce de travail (classe C). Donné par la session du compte organisme le 2026-11-19 vers 22:32Z, sur GO-2026-11-19-81.

## Ce que tu fais

Tu écris la version 7 du préenregistrement de la ligne 3 (`preenregistrement-ligne-3-votes-effectifs-juges-v7.md`), limitée aux **quatre corrections** de la vérification `verification-ligne-3-v6-v1.md` (même dossier, `cbaf44de…`), appliquées **à la lettre** avec ses textes exacts, et à la tenue de version (titre, statut, heure, mandat cité, vérification citée comme faite ; une section de différentiel v6 → v7). La version 6 (`b040d24c…`) reste intacte (R12). Le devis v6 (`34e87d90…`) est jugé propre : tu ne l'écris pas en version 7, sauf si un renvoi au fichier du préenregistrement l'exige ; dans ce cas, seulement ce renvoi.

Applique les remplacements par un programme Python écrit dans ton bloc-notes et lancé par son chemin, qui extrait les textes exacts de la vérification sans recopie à la main et s'arrête si un texte ancien n'est pas trouvé exactement une fois. Produis le différentiel v6 → v7.

## Ce que tu lis

`CLAUDE.md` ; la version 6, son rapport, son mandat ; la vérification `cbaf44de…` ; sur main, `registres/decisions.md` (R-3917, R-3934) pour la correction 4. Vérifie chaque empreinte avant de citer.

## Ce que tu rends

Dans ton bloc-notes seulement : la version 7, `differentiel-preenregistrement-ligne-3-v6-v7.diff`, `rapport-redacteur-ligne-3-v7-v1.md` (court) et ton programme. En-tête : « Auteur : rédacteur neuf, modèle F » ; aucun identifiant de modèle ; heure par `date -u`.

## Interdits

Aucun appel à un fournisseur de modèles, aucune dépense, aucune machine, aucun réseau sauf `git fetch`/`git show` du dépôt. Aucun commit, aucune poussée, aucune écriture dans le dépôt. Jamais de heredoc ni de bloc de texte en ligne passé à un interpréteur. Aucune valeur de clé. **Aucune commande, même une empreinte, une liste ou une taille, sur un chemin sous `archives-reponses-modeles/` ; tu n'ouvres aucune carte.** Jamais le nom d'une commande d'arrêt ou de recherche de processus par motif dans une commande. Au premier refus d'un outil : arrête-toi et dis-le.
