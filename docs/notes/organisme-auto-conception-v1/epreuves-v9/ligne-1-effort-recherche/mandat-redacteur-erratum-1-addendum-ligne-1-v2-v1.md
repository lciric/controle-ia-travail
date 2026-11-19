# Mandat du rédacteur — erratum 1 à l'addendum scellé de la ligne 1, version 2 — v1

Pièce de travail (classe C). Donné par la session du compte organisme le 2026-11-19 vers 22:45Z.

## Ce que tu fais

Tu écris la version 2 de l'erratum 1 (`erratum-1-addendum-1-preenregistrement-ligne-1-effort-recherche-v5-v4-v2.md`), limitée aux **deux corrections** de la relecture `relecture-erratum-1-addendum-ligne-1-v1.md` (même dossier, `48f14f5c…`), appliquées **à la lettre** avec ses textes exacts, et à la tenue (titre, version, heure, mandat cité, relecture citée). La version 1 (`a370cf6a…`) reste intacte (R12). Rien d'autre ne change.

Applique les remplacements par un programme Python écrit dans ton bloc-notes et lancé par son chemin, qui extrait les textes exacts de la relecture et s'arrête si un texte ancien n'est pas trouvé exactement une fois. Produis le différentiel v1 → v2.

## Ce que tu lis

`CLAUDE.md` ; l'erratum v1, son rapport, son mandat ; la relecture `48f14f5c…`. Vérifie chaque empreinte avant de citer.

## Ce que tu rends

Dans ton bloc-notes seulement : l'erratum v2, `differentiel-erratum-1-addendum-ligne-1-v1-v2.diff`, un rapport court et ton programme. En-tête : « Auteur : rédacteur neuf, modèle F » ; aucun identifiant de modèle ; heure par `date -u`.

## Interdits

Aucun lancement. Aucun appel à un fournisseur de modèles, aucune dépense, aucune machine, aucun réseau sauf `git fetch`/`git show` du dépôt. Aucun commit, aucune poussée, aucune écriture dans le dépôt. Jamais de heredoc ni de bloc de texte en ligne passé à un interpréteur. Aucune valeur de clé. **Aucune commande, même une empreinte, une liste ou une taille, sur un chemin sous `archives-reponses-modeles/`.** Jamais le nom d'une commande d'arrêt ou de recherche de processus par motif dans une commande. Au premier refus d'un outil : arrête-toi et dis-le.
