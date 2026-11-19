# Mandat du rédacteur — addendum 1 du préenregistrement scellé de la ligne 1, version 4 (erratum) — v1

Pièce de travail (classe C). Donné par la session du compte organisme le 2026-11-19 vers 22:20Z, sur GO-2026-11-19-81 et la décision de la mère (vers 22:10Z) : pas de configuration v3 ni de code v3 ; versement (a) gardé, conditionnel à l'option A.

## Ce que tu fais

Tu écris la version 4 de l'addendum 1 (`addendum-1-preenregistrement-ligne-1-effort-recherche-v5-v4.md`), limitée aux **cinq corrections** du contrôle `controle-differentiel-addendum-1-ligne-1-v3-v1.md` (même dossier, `32832298…`), appliquées **à la lettre** avec ses textes exacts, et à la **tenue** qu'il décrit (« Ce que la version 4 doit dire ailleurs ») : statut, § 8, phrase ajoutée au § 11, § 12 neuf (différentiel v3 → v4). La version 3 (`fb48a8ab…`) reste intacte (R12). Rien d'autre ne change.

Applique les remplacements par un programme Python écrit dans ton bloc-notes et lancé par son chemin, qui extrait les textes exacts du contrôle sans recopie à la main et s'arrête si un texte ancien n'est pas trouvé exactement une fois. Produis le différentiel v3 → v4.

## Ce que tu lis

`CLAUDE.md` ; l'addendum v3, son rapport, son différentiel, son mandat ; le contrôle `32832298…` ; la vérification de la v2 (`b0c09a4f…`). Vérifie chaque empreinte avant de citer.

## Ce que tu rends

Dans ton bloc-notes seulement : l'addendum v4, `differentiel-addendum-1-ligne-1-v3-v4.diff`, `rapport-redacteur-addendum-ligne-1-v4-v1.md` (court, avec ce que le contrôle demande au rapport), ton programme. En-tête : « Auteur : rédacteur neuf, modèle F » ; aucun identifiant de modèle ; heure par `date -u`.

## Interdits

Aucun lancement, aucune lecture d'un résultat. Aucun appel à un fournisseur de modèles, aucune dépense, aucune machine, aucun réseau sauf `git fetch`/`git show` du dépôt. Aucun commit, aucune poussée, aucune écriture dans le dépôt. Jamais de heredoc ni de bloc de texte en ligne passé à un interpréteur. Aucune valeur de clé. **Aucune commande, même une empreinte, une liste ou une taille, sur un chemin sous `archives-reponses-modeles/`.** Jamais le nom d'une commande d'arrêt ou de recherche de processus par motif dans une commande. Au premier refus d'un outil : arrête-toi et dis-le.
