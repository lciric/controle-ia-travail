# Passation de la session de formation du barreau 5 — 2026-11-20 21:35 UTC

Session `session_01QPDgKjCQYmTHUEjN63ThC8`. Fait suite à `passation-session-formation-2026-11-20-1605.md`. Mère : `session_01QPDgKgejkqwnuaJHJ31Ydo`. Lazar absent jusque vers 00:45Z. Aucun score, aucune sortie de marche lue.

## Fait depuis 16:05Z
- **Relance 7** (61655818, marche 20261120-144552-b5f-formation-7-x1) : marche menée au bout, code 0, 18:46:42Z.
  - Versement final prouvé : 35 fichiers, commit 7714b0ac6a9a11cd2b1644a747bda0dcccec513a de `donnees/barreau5-familles-jumelles-v1-formation-instance-7-x1`.
  - Garde `detruire` du lanceur du commit de course acceptée ; détruite par l'identifiant à 18:55:56Z ; absence prouvée, témoin 60988826 présent.
  - Dépense : 5,12 USD (coupure 17).
- **Relance 5** (61655633, marche 20261120-144431-b5f-formation-5-x1) : marche menée au bout, code 0, 21:31:18Z.
  - Versement final prouvé : 53 fichiers, commit e37790479d51c4f5fd7d68f11037254f15749de5 de `donnees/barreau5-familles-jumelles-v1-formation-instance-5-x1`.
  - Garde acceptée ; détruite par l'identifiant à 21:32:47Z ; absence prouvée.
  - Dépense : 7,94 USD (coupure 26).
- **Commun** : 35,69 USD à 21:31Z, sous le plafond de 200 USD ; crédit 90,86 USD.
- **Ligne `SORTIES-FORMATION-B5F`** : non écrite. Elle suit la fin de toutes les instances et de toute relance (plan de marche, point 4), et cite pour 2, 3 et 4 la tête de la branche de la recréation (contre-lecture de l'additif 3). Erreur de ma part à 18:57Z, corrigée auprès de la mère à 21:35Z.

## Reste
- **Mot unique de Lazar** (vers 00:45Z) : additifs 2 v6 et 3, exception à R12, destruction des quatre premières tentatives (61655405, 61655453, 61655547, 61655585), suppression par lui des branches …-instance-<2|3|4>-x1 et de la branche d'essai, recréation de 1, 2, 3 et 4 hors de la machine 144450, avant 2026-11-21T07:30:16Z.
- **Après son mot** :
  1. destruction par l'identifiant (`detruire` pour 2, 3 et 4 ; ligne directe pour 1) ;
  2. absence des branches vérifiée par ls-remote ;
  3. relevé des conditions et de la réserve (additif 2 v6, section 5) ;
  4. ligne d'engagement à la mère avant chaque création ;
  5. recréations par `outils/creer_b5f_recreation.sh` (machine 144450 exclue, fichiers « -recre ») ;
  6. veille, preuve et destruction de chaque recréation ;
  7. ligne `SORTIES-FORMATION-B5F` envoyée à la mère, contrôlée par programme.

## Réserves
- La réserve de dépense pour quatre recréations est serrée : la quatrième est probablement un nœud au relevé.

## Instances (21:35Z)
- En marche : aucune.
- Arrêtées, non détruites : 61655405, 61655453, 61655547, 61655585.
- Non touchées : 58936096, 58936099, 58936100 (intouchables) et 60988826 (témoin).
- Détruites aujourd'hui : 61552174 (instance 6), les six premières copies, 61655818 (relance 7), 61655633 (relance 5).
