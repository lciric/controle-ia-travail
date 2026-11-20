# Passation de la session de formation du barreau 5 — 2026-11-20 16:05 UTC

Session `session_01QPDgKjCQYmTHUEjN63ThC8`. Fait suite à `passation-session-formation-2026-11-20-1450.md`. Mère : `session_01QPDgKgejkqwnuaJHJ31Ydo`. Lazar absent jusque vers 00:45Z ; autonomie de la mère (GO-2026-11-20-66). Aucun score, aucune sortie de marche lue.

## Fait depuis 14:50Z
- **Relances 1, 2, 3 et 4**, toutes sur la machine du loueur 144450 :
  - tombées à « ARRET : installation des paquets » : 1 à 14:59:36Z ; 2, 4 et 3 à 15:45-15:46Z, au plafond de 3600 s ;
  - aucune ligne « marche : début » ;
  - la 1 a écrit « versement final NON PROUVÉ » (15:13:32Z) ; 2, 3 et 4 ont écrit « versement final prouvé : 4 fichiers » (15:50-15:51Z), seulement traces-b5f/ ;
  - les quatre ont demandé « stopped » elles-mêmes ; toutes sont « stopped », aucune détruite.
- **Relance 1** : inventaire de son disque (ls, du ; aucune sortie de marche), versé sur `traces/barreau5-relance-1-premiere-tentative` @ 0ce9109d685edc5a818adaab0d7316a227d0e273, poussée prouvée.
- **Relances 2, 3 et 4** :
  - preuves vérifiées (inventaire final conforme ; `detruire` du lanceur joué en contrôle seul, rien détruit) ;
  - commits prouvés : 740c5c38…, fa7a6362…, 0af9679d… ;
  - branches de sortie copiées telles quelles sous `traces/barreau5-relance-<n>-premiere-tentative` (4fef6073…, b35dfe17…, 77fd59da…), poussée prouvée.
- **Additifs**, écrits par l'agent Fable, contre-lus et vérifiés par un contre-lecteur Opus neuf, scellés par la mère :
  - additif 2 v3 (R-4315), remplacé par la v6 (R-4318, 3562d5a1…) : recréation, une fois et sous le même nom « -x1 », de toute relance tombée avant sa marche ; machine 144450 exclue ; réserve de dépense ; mot unique de Lazar ;
  - additif 3 v2 (R-4322, d4f9c24c…) : suppression d'une branche de sortie qui ne porte que traces-b5f/, après copie prouvée.
  - « -x2 » est écarté : le code de lecture figé ne l'admet pas.
- **Essai de la suppression gardée** sur la branche jetable `formation-b5f/essai-suppression` :
  - tête fausse : refus par git ;
  - tête juste : refus HTTP 403 du dépôt distant, la session n'a pas le droit de supprimer une branche, rien réessayé ;
  - la branche d'essai reste ;
  - Lazar fera les suppressions dans l'interface de GitHub (R-4323).
- **Nettoyage du disque du conteneur** (plein à 97 %) : six arbres de travail de branches de sortie déjà poussées, retirés après contrôle (tête distante égale au commit local).
- **Relances 5 et 7** : en marche depuis 14:51 et 14:53Z.

## Reste
- **Mot unique de Lazar** (vers 00:45Z) : additifs 2 v6 et 3, exception à R12, destruction des quatre premières tentatives (61655405, 61655453, 61655547, 61655585), suppression par lui des branches …-instance-<2|3|4>-x1 et de la branche d'essai, recréation de 1, 2, 3 et 4 hors de la machine 144450, avant 2026-11-21T07:30:16Z.
- **Après son mot** :
  1. destruction par l'identifiant (`detruire` pour 2, 3 et 4 ; ligne directe pour 1, versement non prouvé) ;
  2. absence des branches vérifiée par ls-remote ;
  3. relevé des conditions et de la réserve (additif 2 v6, section 5) ;
  4. recréations par `creer_b5f_relance.sh`, avec un filtre de machine à ajouter (machine_id ≠ 144450) ;
  5. lignes d'engagement à la mère avant chaque création.
- **Veiller 5 et 7 jusqu'à leur fin** : preuve, destruction, vérification.

## Réserves
- La réserve de dépense pour quatre recréations est serrée : la quatrième est probablement un nœud au relevé.
- La branche d'essai `formation-b5f/essai-suppression` existe toujours ; Lazar la supprime avec les autres.

## Instances (16:05Z)
- En marche : 61655633 (relance 5), 61655818 (relance 7).
- Arrêtées, non détruites : 61655405, 61655453, 61655547, 61655585.
- Non touchées : 58936096, 58936099, 58936100 (intouchables) et 60988826 (témoin).
