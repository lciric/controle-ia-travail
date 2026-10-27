# Banque T0.5 complète — versement v2 : notations `e2` (couche 1 bis, partie (a))

- Remplace le LISEZMOI v1 (gardé, R12) pour ce qui manquait : **`e2`, passe 0, par les deux juges**, pour les 60 tâches du pilote et les 36 de la banque.
- Instance Vast.ai 58007778 (A100 SXM4 80 Go), sous GO-2026-10-27-07 ; commit extrait `65d78b55` de `prep/t05-complement-notations-v1` (module `noter_complement_t05`, code cité `f78a60b0`, arbre de code du pilote) ; 726 tests passés sur l'instance ; amorce finie en code 0 (2 runs sur 2).
- **Run 1** `20261027-203435-t05-complement-1-reel` (fiche `prereg/T0.5-complement-pilote-e2-v1.md`, `f2975b65…`) : run source `20261012-105125-t05-pilote-reel` ; `notations-8B-decisives.json` et `notations-3B-decisives.json` : **60 notations chacun, clés `juge-<juge>/<tâche>/e2/passe-0`**.
- **Run 2** `20261027-220146-t05-complement-2-reel` (fiche `prereg/T0.5-complement-banque-e2-v1.md`, `6e7ca833…`) : run source `20261027-153857-t05-pilote-reel` (ce versement, v1) ; **36 notations par juge, mêmes clés**.
- **Nom des fichiers** : `-decisives` est le nom demandé par conv-audit ; la chaîne, quand elle va jusqu'au bout, range `e2` dans `-descriptives`. **L'épisode et la passe se lisent sur la clé de chaque notation**, jamais sur le nom du fichier.
- Notes à champ `score` non nul (compte descriptif, rien n'est lu) : run 1, 8B 25 sur 60, 3B 6 sur 60 ; run 2, 8B 8 sur 36, 3B 5 sur 36. Les notes non entières restent absentes (jamais imputées ni redemandées).
- Traces de l'instance : `traces/t05-complement-20261027-225629-d23y/`.
- Dossiers des notations, pour conv-audit : `diag/20261027-203435-t05-complement-1-reel/` et `diag/20261027-220146-t05-complement-2-reel/` (manifestes sous `runs/`).
