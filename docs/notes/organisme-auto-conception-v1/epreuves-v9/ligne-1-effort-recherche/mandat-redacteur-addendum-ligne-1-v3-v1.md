# Mandat du rédacteur — addendum 1 du préenregistrement scellé de la ligne 1, version 3 (erratum) — v1

Pièce de travail (classe C). Donné par la session du compte organisme le 2026-11-19 vers 22:10Z, sur GO-2026-11-19-81 (main, commit `d4449d327`).

## Ce que tu fais

Tu écris la version 3 de l'addendum 1 (`addendum-1-preenregistrement-ligne-1-effort-recherche-v5-v3.md`), limitée aux **quatre corrections** de la vérification `verification-addendum-1-ligne-1-v2-v1.md` (même dossier, `b0c09a4f…`), appliquées **à la lettre** avec les textes exacts de sa section 6. La version 2 (`b5d76973…`) reste intacte (R12). Rien d'autre ne change, sauf la tenue nécessaire (titre et phrase de version, heure, mandat cité, vérification citée comme faite), déclarée dans le rapport.

1. § 5.4 : retirer l'en-tête de table en double ; remplacer les deux « À PORTER par la mère » des attestations par les deux textes exacts de la vérification (attestations `7565e0ba…` et `56d7e2f6…`, commit `6f0957a7…`).
2. § 5.4, « État de ces conditions » : la puce sur (iii) et (v) dit les deux conditions tenues, cite leurs sources et recopie la limite des 18 passes de mutation.
3. § 6 : la phrase ajoutée après « L'étalonnage ne part pas avant le scellement de cet addendum. » (ni `tout`, ni étape à la main, ni étalonnage seul avant le mot de Lazar exigé par GO-2026-11-19-81 ; tant que la décision 4 n'est pas tranchée, rien ne part ; si ce mot vient après l'étalonnage, il ne porte que sur « toutes les portes passées, empreintes conformes »).
4. § 7, réserve 6 : le programme de l'audit de symétrie est écrit, contre-lu et porté au registre avant le lancement de la course décisive, et son empreinte figure dans le mot de Lazar de GO-2026-11-19-81.

Applique les remplacements par un petit programme Python écrit dans ton bloc-notes et lancé par son chemin (chaque texte ancien trouvé une seule fois), puis produis le différentiel v2 → v3.

## Ce que tu lis

`CLAUDE.md` ; l'addendum v2, son rapport, son mandat ; la vérification `b0c09a4f…` ; les deux attestations sous `code-v2/`. Vérifie chaque empreinte avant de citer.

## Ce que tu rends

Dans ton bloc-notes seulement : l'addendum v3, `differentiel-addendum-1-ligne-1-v2-v3.diff`, `rapport-redacteur-addendum-ligne-1-v3-v1.md` (court), et ton programme de remplacement. En-tête : « Auteur : rédacteur neuf, modèle F » ; aucun identifiant de modèle ; heure par `date -u`.

## Interdits

Aucun lancement, aucune lecture d'un résultat. Aucun appel à un fournisseur de modèles, aucune dépense, aucune machine, aucun réseau sauf `git fetch`/`git show` du dépôt. Aucun commit, aucune poussée, aucune écriture dans le dépôt. Jamais de heredoc ni de bloc de texte en ligne passé à un interpréteur. Aucune valeur de clé. **Aucune commande, même une empreinte, une liste ou une taille, sur un chemin sous `archives-reponses-modeles/`.** Jamais le nom d'une commande d'arrêt ou de recherche de processus par motif dans une commande. Au premier refus d'un outil : arrête-toi et dis-le.
