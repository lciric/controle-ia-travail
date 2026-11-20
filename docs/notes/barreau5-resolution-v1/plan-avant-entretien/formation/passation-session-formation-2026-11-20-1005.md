# Passation de la session de formation du barreau 5 — 2026-11-20 10:05 UTC

Session successeure (`session_01QPDgKjCQYmTHUEjN63ThC8`, autre compte), reprise vers 09:45Z sur le brief v1 (`brief-lancement-session-formation-v1.md`, sha256 9864a3d4ad8a84bed304d7692741b662a7f412b78a004a12a0c30392c3e9154b). Mandat v2 (83e5d7f8…), texte scellé (bdff244f…), plan de marche v1 (fbbc2191…), passation de 08:33Z (bf3762d1…) : empreintes vérifiées. Aucun score, aucune sortie de marche lue.

## Fait
- Environnements du bloc-notes : `venv-b5f` (exigences du dépôt, torch 2.14.1, numpy 2.4.6), `venv-vast` (vastai 1.11.2, paquet d'autorités du mandataire à la place du `cacert.pem` de certifi, original gardé à côté). Arbre de course détaché au commit 31fca83b0c26cd035fe9e660d123e690a41b6271.
- Instance 6 (61552174, `b5f-formation-v1-6`) trouvée « exited / stopped ». Lignes « B5F » de son journal : 08:53:25Z marche code 0, « FIN : marche menée au bout » ; 08:53:34Z « versement final prouvé : 53 fichiers … au commit 0a6af341244900da047ea850a966bf137dee279b de donnees/barreau5-familles-jumelles-v1-formation-instance-6 » ; 08:53:36Z fin, code 0, « stopped » demandé. Aucune ligne ARRET ni SIGNAL.
- Preuve : branche de sortie récupérée (tête 85a4942b, journal de fin ; commit prouvé ancêtre de la tête) ; `traces-b5f/inventaire-final.json` au commit prouvé, sha256 6d80070c2c7ec895a87b599e720fb3b12e93bc1fd1758d01481480a96bddcf88, égal à son compagnon.
- `detruire` du lanceur (GO_ID=GO-2026-11-19-86) accepté ; ligne jouée par l'identifiant à 10:01:46Z (joueur sha256 3935870a9786157766b2ef940dab6c503bd4ef22c31bac6c51741b0df2182245, garde vérifiée sur son texte ; sortie sha256 1be31252b72ec890f0c44751d67fad6800cff26ba31f4823446a5431c9238d5c) ; `verifier-destruction` (témoin 60988826) : « absence de l'instance 61552174 prouvée ».
- Dépense de l'instance 6 : ≈ 8,65 USD (7,39 h × 1,17 USD/h) plus le stockage arrêté jusqu'à 10:01Z. Crédit du compte à 10:02Z : 5,74 USD.
- L'ancienne mère (`session_01XJ6Mgr8BN6UanALsQatc5E`) est introuvable depuis ce compte ; rapport envoyé à 10:0xZ à la session `session_01QPDgKgejkqwnuaJHJ31Ydo`, présumée mère successeure (titre « New session », routine de reprise), avec demande de confirmation.

## Reste
- Instances 1, 2, 3, 4, 5, 7 : sur le seul signal de la mère (crédit rechargé), ordre 1, 2, 3, 4, 5, 7 ; fin des créations 2026-11-21T07:30:16Z.
- Ligne `SORTIES-FORMATION-B5F` : instance 6 proposée « donnees/barreau5-familles-jumelles-v1-formation-instance-6 @ 0a6af341244900da047ea850a966bf137dee279b ; inventaire sha256 6d80070c2c7ec895a87b599e720fb3b12e93bc1fd1758d01481480a96bddcf88 » ; ligne entière à la fin de toutes les instances et de toute relance.
- Sel, table, `ENGAGEMENT-B5F` : sur le seul mot exprès de la mère.
- Réunion des branches de données (question 5 du plan de marche) : non faite.

## Réserves
- Identité de la mère successeure non confirmée à l'écriture.
- Le cumul de la veille par la baisse du crédit surestimait la dépense propre (réserve de 08:33Z) ; le chiffre ci-dessus est heures × prix.

## Prochaine action
Attendre le mot de la mère. Au signal : relever le crédit, recherche d'offres (`outils/choisir_offre_b5f.py`), création dans l'ordre 1, 2, 3, 4, 5, 7 par fichier joueur, veille par instance.

## Programmes et instances en cours (10:05Z)
| Quoi | Identifiant | État |
|---|---|---|
| Instance de formation 6 | 61552174 | détruite 10:01:46Z, absence prouvée |
| Machines intouchables | 58936096, 58936099, 58936100 | exited, non touchées |
| Témoin | 60988826 | exited, non touché |
| Instances de formation à créer | 1, 2, 3, 4, 5, 7 | en attente du signal |
