# Collisionneur v9-v8j : rapport du développeur

Écrit à 2026-11-22T08:55:59Z (`date -u`). Classe B, Opus 5.5. Aucun réseau, aucune clé.

- `collisionneur_v9_v8j.py` (d199a14b…), copie de la v8i (7c7aa713…, intacte) par `fabriquer_v8j_depuis_v8i_v1.py` ; essais `test_collisionneur_v9_v8j.py` : 393 passés, 11 sautés.
- La vérification de la v8i par le même contre-lecteur (`verification-corrections-collisionneur-v9-v8i-opus-v1.md`) conclut « à corriger », avec deux bloquants : un chemin réel imbriqué, et des homoglyphes ou des caractères pleine chasse. Treize mutations sont prises ; les trois qui survivent sont équivalentes.

## Corrections, au plus simple
- **Deux composants exactement** : un chemin accepté est de la forme `docs|runs|scripts/NOM`, sans aucun sous-chemin. Aucun chemin réel ne peut donc être imbriqué.
- **NOM en ASCII seul** : lettres et chiffres séparés par un seul `-`, `_` ou `.`. Ni homoglyphe ni pleine chasse.
- Les cinq cas du contre-lecteur sont essayés : tous refusés, aucune écriture. Un essai hérité est accordé : trois composants sont désormais refusés.

## Essai à blanc sur le tirage au hasard (lecture seule)
Le seul chemin trouvé est `['scripts/pipelines']`, acceptable. Reprise proposée, après vérification et mot de la mère : même dossier, v8j, `--reprise`, `--accepter-motif E3-T1-conception-F:chemin interne`, six espèces, plafond et ligne de 50 USD, GO-2026-11-22-33.
