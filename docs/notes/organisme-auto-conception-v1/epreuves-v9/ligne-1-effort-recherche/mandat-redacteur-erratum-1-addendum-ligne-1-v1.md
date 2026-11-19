# Mandat du rédacteur — erratum 1 à l'addendum 1 scellé de la ligne 1 — v1

Pièce de travail (classe C). Donné par la session du compte organisme le 2026-11-19 vers 22:28Z, sur le mot de la mère (vers 22:25Z) : un texte ne peut pas porter sa propre empreinte ; la copie scellée reste identique à l'octet ; les places « À PORTER » se remplissent par un erratum.

## Ce que tu fais

Tu écris l'erratum 1 (`erratum-1-addendum-1-preenregistrement-ligne-1-effort-recherche-v5-v4-v1.md`) à l'addendum 1 scellé : `prereg/organisme-auto-conception-v9/addendum-1-preenregistrement-ligne-1-effort-recherche-v5-v4.md` sur main, sha256 `c29628a0dd209133545985cc334274462257314560c62c04259c5b31b1686e67`, clé `ADDENDUM-1-ORGANISME-V9-LIGNE-1`, scellé à `2026-11-19T22:25:03Z` (registre `registres/scellements-v1.md` et R-3980 sur main, commits `061aeff58` et `3f64028f1`). L'addendum n'est pas réécrit.

L'erratum **ne fait que remplir** les places « À PORTER » de l'addendum, chacune citée par sa section et son texte exact, avec la valeur qui la remplit :
- § 8 : le contrôle du différentiel v3 → v4 (`docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-1-effort-recherche/controle-differentiel-addendum-1-ligne-1-v4-v1.md`, `def81ef33381acd6bbd10926c79f025743cd16de17b0e35621706a262e1bb2c2`, commit `991e4229` de `lot/compte-organisme-v1`, verdict « Scellable tel quel ») ;
- § 6 : chemin, empreinte, commit et heure du scellement, lus dans la ligne du registre des scellements et dans R-3980 sur main ;
- toute autre place « À PORTER » que tu trouves : nomme-la ; remplis-la si sa valeur est écrite dans une pièce versée et vérifiable, sinon dis qu'elle reste ouverte et ce qui la remplira.

Une seule phrase de plus est permise : celle que le contrôle v4 propose pour le § 9, point 5 (« le journal du lanceur sert en complément au contrôle du § 6, dont la source d'heure est le fichier d'état du lanceur, versé par l'empaquetage. »), écrite comme précision de lecture, non comme changement de règle.

L'erratum dit en tête qu'il ne change ni hypothèse, ni prédiction, ni seuil, ni critère, ni garde, ni liste d'arrêt, ni décision de Lazar.

## Ce que tu lis

`CLAUDE.md` ; l'addendum scellé (sur main, par `git show`) ; `registres/scellements-v1.md` et `registres/decisions.md` (R-3980, R-3981) sur main ; le contrôle v4 ; les pièces citées dans les places à remplir. Vérifie chaque empreinte avant de citer.

## Ce que tu rends

Dans ton bloc-notes seulement : l'erratum et un rapport court. En-tête : « Auteur : rédacteur neuf, modèle F » ; aucun identifiant de modèle ; heure par `date -u`.

## Interdits

Aucun lancement. Aucun appel à un fournisseur de modèles, aucune dépense, aucune machine, aucun réseau sauf `git fetch`/`git show` du dépôt. Aucun commit, aucune poussée, aucune écriture dans le dépôt. Jamais de heredoc ni de bloc de texte en ligne passé à un interpréteur. Aucune valeur de clé. **Aucune commande, même une empreinte, une liste ou une taille, sur un chemin sous `archives-reponses-modeles/`.** Jamais le nom d'une commande d'arrêt ou de recherche de processus par motif dans une commande. Au premier refus d'un outil : arrête-toi et dis-le.
