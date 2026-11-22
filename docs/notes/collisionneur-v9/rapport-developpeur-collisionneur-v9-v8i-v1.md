# Collisionneur v9-v8i : rapport du développeur

Écrit à 2026-11-22T08:52:16Z (`date -u`). Classe B, Opus 5.5. Aucun réseau, aucune clé.

- `collisionneur_v9_v8i.py` (7c7aa713…), copie de la v8h (d9b41b11…, intacte) par `fabriquer_v8i_depuis_v8h_v1.py` ; essais `test_collisionneur_v9_v8i.py` : 388 passés, 11 sautés.
- Vérification de la v8h par le même contre-lecteur (`verification-corrections-collisionneur-v9-v8h-opus-v1.md`) : « à corriger », un bloquant (ponctuation interne au deuxième composant, jeton coupé par un caractère invisible, `+` ou `%`).

## Corrections
- **Jeton coupé** : le caractère qui suit le jeton doit être la fin du texte, un blanc ou une ponctuation de phrase (`, ; : ! ? ) ] } » " ' ’`) ; sinon, refus.
- **Forme des composants** : seulement des lettres et des chiffres, séparés par un seul `-`, `_` ou `.`.
- **Comparaison normalisée** : le nom et les entrées du dépôt sont comparés sans casse et sans caractère autre que lettre ou chiffre, avec et sans extension. Un nom qui est le début d'une entrée, ou l'inverse, est refusé à partir de six caractères (non-bloquant porté : `runs/collisionneur-protocole`).
- **Erreur du système de fichiers** : un essai la provoque ; elle est refusée.
- Les neuf contournements du contre-lecteur sont essayés : tous refusés, aucune écriture. Les faux positifs voulus restent admis (« des scripts/pipelines d'analyse »).
- **Mutations prises** : suivant, préfixe, erreur du système de fichiers, normalisation, forme des composants.
- **Incident de développement**, pris par les essais avant tout sceau : ma fonction de normalisation portait le nom d'une fonction de la v8d, qui l'écrasait. Elle est renommée `normaliser_nom`, et le programme de fabrication vérifie que les deux noms sont distincts.

Essai à blanc sur le tirage au hasard (lecture seule) : `['scripts/pipelines']`, acceptable. Reprise proposée : la même que dans le rapport de la v8h, mais sur la v8i.
