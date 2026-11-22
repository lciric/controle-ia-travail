# Passation de la session de lecture du barreau 5 — 2026-11-22, 22:20Z

Session `session_013QMayiuN339pSspJBRTwYL` (Opus 5.5), fille du conducteur `session_013QMayjM1PQPWkLifMw9HDR` ; mère en poste `session_013QMayjbmQUdDuDs2S3i3XD`. Passation intermédiaire : la session reste en attente. Écarts à R14 déclarés : ni `registres/etat.md`, ni passations, ni `registres/decisions.md` lus (mandat, § 9, point 10) ; `registres/etat.md` reste à la mère.

## Fait
- Phase 1 : plan de marche `plan-de-marche-session-lecture-b5f-v1.md` (`88c8cf8a…`), erratum 1 (`7920172e…`), erratum 2 (`3659365f…`), sur `lecture-b5f/plan-de-marche-v1`.
- **Répétition générale** : instance 62036317 (`b5f-repetition-v1`, offre 29019346, 1,1833 USD de l'heure), créée à 20:43:41Z ; marche 20261122-204222-b5f-repetition menée au bout (21:54:58Z) ; versement final prouvé au commit `c5c77d5b351cf2c24e4440700d1eb3ca534670d1` de `donnees/barreau5-familles-jumelles-v1-repetition` (inventaire final `3f44f1be…`, 397 fichiers ; manifeste, inventaire et garde des activations présents) ; détruite par son identifiant à 22:10:10Z, absence prouvée (témoin 58936096) ; dépense ≈ 1,71 USD au plus (coupure 8). Un refus de garde à « detruire », dû à mon nommage de l'inventaire, corrigé sur mot du conducteur (erratum 2, point 1).
- **Relecture décisive** : ligne d'engagement inscrite à 22:12:24Z (coupure 14 USD, GO-2026-11-22-133, garde `une_sur_dix`) ; instance 62047649 (`b5f-lecture-v1`, offre 29019282, 1,22 USD de l'heure), créée à 22:13:15Z après « config », « verifier » et « commande » v2 sans refus ; **tombée avant la marche** à 22:13:48Z : « ARRET : commit des entrées f6e2072dc4cce95059e7590ae4e39cc4881729fc introuvable ». Cause : le clone partiel des entrées dans l'amorce figée (l. 362-364) ne garde pas son aide d'identification pour le téléchargement différé (« could not read Username for 'https://github.com' », « could not fetch … from promisor remote ») ; le commit des entrées existe et reste la tête de sa branche. Aucun score produit ; trois fichiers de traces prouvés au commit `254f92804c0c4efecdab15ca162fd88bf28bad7b` (inventaire final `cae5107f…`, copie versée sur ma branche au commit `3a802872…`) ; détruite sur mot de la mère (écart déclaré : versement final non prouvé) à 22:17:14Z, absence prouvée (témoin 58936096) ; dépense ≈ 0,08 USD.
- Lignes rédigées et transmises : deux lignes d'engagement, deux lignes d'arrêt (versées par la mère).

## Reste
- Relance de la relecture décisive : erratum de chaîne de l'amorce (en conception), nom de la branche de sortie (`donnees/barreau5-familles-jumelles-v1-lecture` existe désormais : l'amorce figée la refuserait, R12), mot de Lazar. Rien n'est relancé avant.
- `SCORES-B5F` : non écrite ; aucune ligne à clé de clôture n'existe.

## Réserves
- La clé propre à l'instance de la répétition a été affichée une fois dans ma sortie d'outil ; retirée du fichier, transmise nulle part (erratum 2, point 2).
- Le coût d'une instance est tenu par heures × `dph_total` plus sortie facturée ; la baisse du crédit, partagé, n'est relevée que pour mémoire.

## Phrase de la mère, reportée telle quelle
« Toute relecture rejouée commence par reproduire le dixième gardé ; sa tolérance est fixée par le préenregistrement de ce rejeu, scellé avant toute lecture de ses sorties ; à défaut d'égalité au bit près sur une même machine, l'écart toléré est écrit et justifié avant le rejeu. »

## Prochaine action
Attendre le mot du conducteur ou de la mère (erratum de chaîne, branche de sortie, mot de Lazar). À la relance : arbres de travail du bloc-notes à refaire si le conteneur a été repris (plan, § 3.1, et erratum 1, § 2), commit de la marche et commit de commande éventuellement neufs, à vérifier comme en phase 1.

## Instances actives
Aucune à moi. Chez le loueur, à 22:17Z : 58936096, 58936099, 58936100, 60988826, arrêtées, intouchables.
