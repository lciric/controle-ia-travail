# Contre-lecture du correctif des gardes de la tentative 1 (classe B)

Pièce lue : branche `t08/correctif-gardes-tentative-1-v1`, commit 3c0f60f9f, enfant direct de bd32f9a5c. Contre-lecteur neuf, aucune dépense, rien sur `main`.

## Verdict : conforme avec mineures

## Vérifications
1. Différentiel bd32f9a5c vers 3c0f60f9f : six fichiers exactement (amorce et son `.sha256`, `entrees_v1.py` et son `.sha256` neuf, essai neuf et son `.sha256`). Les trois empreintes compagnon concordent (`sha256sum -c`). `bash -n` sur l'amorce : correct.
2. Objet de la garde conservé. Essai direct en clone partiel (`--filter=blob:none`) : `rev-list --all --objects --missing=allow-promisor` nomme encore tous les arbres et tout blob présent ; seuls les blobs absents (promis) disparaissent de la sortie. Un arbre manquant non promis (commit local dont l'arbre est supprimé) donne « fatal: unexpected missing tree », code 128, donc `GardeArret` : l'arrêt reste. La seconde passe (`log --all --root -m --name-only -z`) nomme `diag/resume.json` bien que son blob manque, sans téléchargement : même ensemble de références (`--all`) que la première, aucun contournement trouvé ; un fichier interdit dont le blob est absent est arrêté par cette passe (essai 2 du fichier d'essais).
3. Amorce : `rc=$?` dans le `|| {` suit bien la substitution. Simulation des codes 124, 137, 1 avec sortie, 2 sans sortie : le message d'arrêt est correct, le code de sortie et les lignes de journal et de refus sont inchangés ; une dernière ligne non vide reste prioritaire.
4. Essais : `tests/test_t08_garde_clone_partiel_v1.py` 3 réussis ; essais de la garde (`test_t08_entrees_rendu_v1.py`, `test_t08_gardes_corrections_v1.py`) 26 réussis. Mutation (drapeau retiré) : 2 essais sur 3 échouent (aucun blob téléchargé ; résumé de 7b), comme attendu.
5. git local 2.43.0 (celui de bookworm, image python:3.11-bookworm) : le drapeau `--missing=allow-promisor` y fonctionne avec `rev-list --objects`. Il existe depuis git 2.24 environ ; non vérifié sur la documentation en ligne (pas d'accès), mais l'essai local est probant.

## Défauts mineurs
1. Le troisième essai (`test_rev_list_par_defaut...`) teste git, non la garde : il ne tombe pas à la mutation. Sans gravité, il documente la cause.
2. `objets_git` renvoyé par la garde ne compte plus les blobs absents : sa signification change (affichée dans le journal, testée seulement `> 0`). À noter, non bloquant.
3. Le message « délai de 900 s dépassé » s'affiche aussi pour 137 (peut être une mémoire saturée) : formulation à nuancer, non bloquant.
4. Le correctif ne couvre que `rev-list` : la passe `log` et `cl.verifier` n'ont pas été mesurées à l'échelle (45 444 fichiers) ; `log` ne lit que les arbres (essai : zéro téléchargement), `cl.verifier` hors périmètre. Vérifier au prochain lancement le temps total des gardes.
