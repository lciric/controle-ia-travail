# Passation du compte 4 — 2026-11-14T06:55:21Z

Écrite à 2026-11-14T06:55:21Z (heure relevée par `date -u`) par la session du compte 4 (`session_01Qi7Gr2uGzyVcw9VmDXgvEV`, modèle A), pendant l'autonomie accordée par Lazar jusqu'à 2026-11-14T10:49:43Z (C4-0023). Remplace pour la lecture la passation `registres-provisoires/passation-compte-4-2026-11-14-0559.md` (`f08f0f0f689b5aa175c05d2dc706201a92c6c1f98237e611e5b123f897bd9536`), gardée telle quelle. Brief `d56b336f…` ; plan `3b1bda25…`, lot « compte 4 ». Dernier journal : `registres-provisoires/compte-4-2026-11-14-v24.md` (`883adb6f910d7774b860deffac20a34e3e435685f242118eb5a0bec6adc36889`, C4-0065) ; le journal v11 se lit dans sa version sans identifiants (`…-v11-sans-identifiants.md`, C4-0056, point 3). Modèles notés « A » et « B » (R-2598). **Aucune dépense, aucune instance, aucune clé employée par ce compte.**

## Fait

- **Tâche 1, validité de l'adaptateur** : commit C7 `c2fab6cc7267b76228a75dc3e2e08bc7aa038961` rempli au brouillon 6 sur l'annonce de la mère (C4-0056) ; vérification courte (modèle B, ni lecteur de P3-bis ni de T0.7) : « candidat conforme », 0 bloquant, 0 majeur, 4 mineurs (rapport `prereg/contre-lectures/validite-adaptateur-preenregistrement-v1-brouillon6-verification-courte-v1.md`, `2c886d3e…`) ; **brouillon 7 (candidat)** `brouillons/validite-adaptateur-v1/validite-adaptateur-preenregistrement-v1-brouillon7.md` (`7e78909d7ca88e0834d277bcf2cad78112f28b23a75d2a07c0503c765062363d`), validateur `[]`, **rendu à la mère** (C4-0061).
- **Tâche 2, audit des fuites** : préparation rendue (C4-0015), auditeur non lancé.
- **Tâche 3, T0.8** : code citable au commit `453a71e1c6729d7ec5d43e3a4a0e3522dfd38579` (`prep/t08-code-compte4-v1`) ; mot de Lazar « go a pour T5-19 » recopié (C4-0054) ; brouillons 8 à 10 écrits et vérifiés (contre-lectures 6 et 7, modèle B : « conforme après corrections », puis « candidat conforme », aucun bloquant ni majeur) ; **brouillon 10 (candidat)** `brouillons/T0.8-bases-boite-noire-v0-v1-brouillon10.md` (`fb004b96bf7fd70d6fe4f1938cba8bcd1afa9a3261135b5ddea336a9e0c68ba1`), sept marqueurs dont `LIGNE_MOT_LAZAR_T5_19`, **rendu à la mère** (C4-0065).
- **Tâche 4, (ii-b)** : code au commit `3baecee7044f2f1701743dc307da9bdcb8fcf217` (`prep/iib-code-compte4-v1`, gelée pour `main`, C4-0056) ; contre-lecture 1 (`a375c699…`) : 1 bloquant, 6 majeurs, 11 mineurs ; **deux passes de corrections arrêtées par le classifieur** (C4-0052 : un refus ; C4-0063 : deux refus, dont un sur une commande en lecture seule), aucune correction faite ; **tâche arrêtée** par ce compte, aucune relance.

## Reste (décisions de la mère et de Lazar)

- **Tâche 1** : la mère confirme au registre VB6-01 (égalité du commit cité avec la ligne `CODE-T07` en vigueur) et VB6-03 (renvois de la notation des modèles), décide d'une relecture du différentiel du brouillon 6 au brouillon 7, puis scelle (`prereg/validite-adaptateur-v1.md`, ligne `SCELLEMENT-VADAPT`).
- **Tâche 3** : la mère remplit `LIGNE_MOT_LAZAR_T5_19` (inscription du mot, confirmation des trois points gardés plus stricts, sort de VT5-07) et les six autres marqueurs ; décide d'une relecture du différentiel du brouillon 9 au brouillon 10 ; ses points de T0.8 (C4-0056, point 6). **Point 7 de son message dépassé** : le mot de Lazar est donné (C4-0054).
- **Tâche 4** : voie pour les fragments de la consigne privée (CLIIBC-01) : décision de Lazar ; questions de C4-0052 et C4-0063 (outil qui importe le module jouet ; reprise, par qui, sur quelle consigne ; choix prévus du développeur) ; v4 de `tests/test_cibles_invisibles_v3.py` à l'intégration ; M7 non tranchée.

## Réserves

- Fragments de la consigne privée du maître de (ii-b) à la tête et dans l'historique de `prep/iib-code-compte4-v1` (`e70ab23e` à `3baecee7`) ; branche gelée.
- Trois refus du classifieur sur (ii-b), non contournés (C4-0052, C4-0063).
- Écarts de ce compte, déclarés : identifiants au journal v11 (version neuve sans eux faite) ; v1 de la vérification du brouillon 5 de T0.8 versée avec des identifiants ; consigne du développeur de (ii-b) sans le motif des secrets ; consigne des corrections de (ii-b) qui omettait `tests/test_iib_consigne_v1.py` ; heure « 05:5x » écrite à la main dans la passation de 05:59 (relevé : 05:58:15Z, C4-0053) ; liste des marqueurs de l'en-tête du brouillon 7 de T0.8 incomplète (corrigée au brouillon 8).
- **Qui a lu quoi** : consigne privée de (ii-b) lue en entier par le développeur du code de (ii-b) (modèle A) et par le contre-lecteur 1 de ce code (modèle B) : jamais lecteurs des sondes de (ii-b) ; les deux développeurs des corrections ne l'ont pas ouverte. Vérificateurs des brouillons 6 à 9 de T0.8 et du brouillon 6 de la validité (modèle B) : aucun fichier de T0.7, de P3-bis ni de (ii-b) ouvert, selon leurs consignes et leurs rapports. Lecteurs de T0.7 scellé : C4-0003, C4-0012.

## Prochaine action

Attendre la mère et Lazar ; rien n'est en cours.

## Agents et instances actifs

- Agents : **aucun** (tous rendus ou arrêtés ; le dernier développeur de (ii-b) arrêté par ce compte, C4-0063).
- Instances de calcul : **aucune** créée ni touchée par ce compte.
- Arbres : `/home/user/t08-code-compte4-v1` (tête `453a71e1`, propre) ; `/home/user/iib-code-compte4-v1` (tête `3baecee7`, propre, caches ignorés seulement). Branche du lot : `lot/compte-4-v1`.
