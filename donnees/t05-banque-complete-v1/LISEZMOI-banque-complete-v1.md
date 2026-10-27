# Banque T0.5 complète (« couche 1 bis », partie (b)) — versement v1

- Run `20261027-153857-t05-pilote-reel` (le nom vient de la chaîne du pilote, effet mécanique sans portée), fiche `prereg/T0.5-banque-complete-36-v1.md` (`61655f95…`), instance Vast.ai 57978233 (A100 SXM4 80 Go), sous GO-2026-10-27-07 ; commit extrait `41e61d88` (code du pilote, arbre gelé de `2660b07`) ; 689 tests passés sur l'instance.
- **Ce que contient le run** (dans `diag/20261027-153857-t05-pilote-reel/` et `runs/20261027-153857-t05-pilote-reel/`, scellés) : 108 épisodes (36 tâches × `e0`, `e1`, `e2`, tous à ensemble non vide), l'appariement, et les **notations décisives des deux juges** (`notations-8B-decisives.json`, `notations-3B-decisives.json` : `e0` passes 0 et 1, `e1` passe 0 ; 108 notations chacun). La chaîne s'est arrêtée à son échéance (15 000 s ; durée 15 209,8 s) pendant les **notations descriptives du 8B** (`e2` passe 0) : `arret.json`, étape « notations descriptives par 8B ». Issue prévue par la fiche (code 1, non un échec).
- **Ce qui manque** : `e2` passe 0, pour les deux juges (36 notations par juge) : run 2 du module de notation complémentaire (`prep/t05-complement-notations-v1`), avec les `e2` des 60 tâches du pilote (run 1).
- Origine de chaque tâche (évaluation retirée par N-019, entraînement) : `origines-taches-banque-v1.json`, à côté des tâches.
- Vecteurs par action : branche `donnees/t05/20261027-153857-t05-pilote-reel` (commit `c3eadf3b`, 26 629 366 octets).
- Rien n'est lu ici (production de données) ; les notes non entières restent absentes (jamais imputées).
