# Relevé des tests de la routine de reprise — session du compte organisme, 2026-11-20 — v1

Pièce de travail (classe C). Branche `lot/compte-organisme-v1`, environnement virtuel `.venv` du dépôt, `PYTHONPATH=src`. **Aucune conclusion** : à comparer au relevé de la mère sur `main` (les deux arbres n'ont pas d'histoire commune).

## Comment la suite a tourné

La suite entière (8 883 tests collectés) dépasse la limite de deux heures d'une tâche de fond : arrêtée à 78 %, sur `tests/test_t06_v10_scripts.py`. Ce fichier, rejoué seul, passe en entier (6 sur 6, 18 s) : il n'était pas bloqué. Les 81 fichiers suivants (liste `tests-restants-v1.txt`, ordre alphabétique) ont été joués à part (33 min).

## Comptes

| partie | passés | échoués | erreurs | sautés | échecs attendus |
|---|---|---|---|---|---|
| jusqu'à l'arrêt | 6 552 | 307 | 2 | 111 | — |
| `test_t06_v10_scripts.py` seul | 6 | 0 | 0 | 0 | — |
| 81 fichiers restants | 1 573 | 328 | 0 | 0 | 4 |
| **total** | **8 131** | **635** | **2** | **111** | **4** |

Total 8 883, égal au nombre collecté.

## Où sont les échecs

43 fichiers ; les comptes par fichier sont dans `echecs-par-fichier-v1.txt`. Les plus nombreux : lanceurs de la course d'auto-conception v3 à v9, amorces et minuteries de T0.6 (v4 à v13). Les messages lus (format court) sont des égalités non tenues et des lignes « AMORCE … DEMARRAGE … machine ?, commit … » : ces tests semblent dépendre de l'environnement (commit, machine, date, outils épinglés). C'est une supposition, non vérifiée.

## Ce qui n'est pas versé

Les sorties brutes de pytest ne sont pas versées : leurs noms de tests paramétrés portent des jetons factices que la garde des secrets refuse (20 correspondances au motif des jetons d'accès, toutes dans les paramètres de `tests/test_sonde_hote_durable_a1_v3_v10.py`). Elles restent dans le bloc-notes de la session.
