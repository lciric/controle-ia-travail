# Collisionneur v9-v8h : rapport du développeur

Écrit à 2026-11-22T08:45:36Z (`date -u`). Classe B, Opus 5.5, session des collisionneurs. Aucun réseau, aucune clé ; aucune reprise avant la vérification des corrections et le mot de la mère.

- `collisionneur_v9_v8h.py` (d9b41b11…), copie de la v8g (93f96e95…, intacte) par `fabriquer_v8h_depuis_v8g_v1.py` ; essais `test_collisionneur_v9_v8h.py` : 376 passés, 11 sautés.
- La contre-lecture de la v8g par un Opus neuf (`verification-collisionneur-v9-v8g-opus-v1.md`) conclut « à corriger ». Elle a démontré qu'un chemin réel suivi d'un point final (`scripts/depot_expurge.py.`) partait dans l'invite.
- **Correction au rapport de la v8g** : `docs/programme-controle-ia-v2.md` y est cité comme refusé parce que c'est un chemin réel. En fait, il est refusé par le motif `controle-ia`.

## Corrections
- **B1, liste blanche** (`chemin_hors_depot`). Le chemin doit commencer par `docs/`, `runs/` ou `scripts/`. Ponctuation finale retirée ; composants vides, `.` ou `..` refusés. Le refus vient dès que le deuxième composant nomme une entrée du dossier correspondant du dépôt : sans tenir compte de la casse, et avec ou sans extension. Refusés aussi : une racine du dépôt introuvable (`CLAUDE.md`) ou une erreur du système de fichiers. Les douze contournements du contre-lecteur et des cas voisins sont essayés : tous refusés, aucun octet neuf au journal.
- **B2** : `controler_acceptations`, en lecture seule, est appelée dans `principal` avant toute écriture (versements, composition, script, lignes, rejugements, absences). La journalisation reste à sa place.
- **Non-bloquants portés** : le bloc accepté est remplacé par un saut de ligne, ses voisins ne se recollent plus. `verifier` revalide chaque acceptation (cellule, empreinte, chemins) et signale une acceptation caduque. Les essais d'attaque du contre-lecteur sont repris.
- **Mutations prises** : contrôle d'existence retiré, retrait sans empreinte, contrôle avancé retiré, recollement, revalidation retirée.

## Essai à blanc sur le dossier réel (lecture seule)
`controler_acceptations` sur la conception de Neon du tirage au hasard rend `['scripts/pipelines']` : acceptable.

## Reprise proposée, après vérification et mot de la mère
Même dossier, v8h, `--reprise`, `--accepter-motif E3-T1-conception-F:chemin interne`, six espèces, plafond et ligne 50 USD (3,43 déjà comptés), GO-2026-11-22-33.
