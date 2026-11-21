# Passation de la session de formation du barreau 5 — 2026-11-21 07:40 UTC

Session `session_01QPDgKjCQYmTHUEjN63ThC8`. Fait suite à `passation-session-formation-2026-11-20-2135.md`. Mère : `session_01QPDgKgejkqwnuaJHJ31Ydo`. Aucun score, aucune sortie de marche lue.

## Fait depuis 21:35Z
- **Mot de Lazar GO-2026-11-21-01** (05:50Z, « g formation ») : additifs 2 v6 et 3 v2, exception à R12, destruction des quatre premières tentatives, recréation des relances 1 à 4 hors de la machine 144450 avant 07:30:16Z. Lu dans `registres/go.md` de `main`.
- **Destructions**, par l'identifiant, ordre 1, 2, 3, 4 : 61655405 (05:53:28Z, ligne directe, versement non prouvé), 61655453, 61655547, 61655585 (05:53:29 à 05:53:32Z, garde `detruire` acceptée sur les commits prouvés). Absence prouvée pour les quatre, témoin 60988826 présent.
- **Branches** : …-instance-2-x1, -3-x1, -4-x1 et `formation-b5f/essai-suppression` supprimées par Lazar ; absence relevée par ls-remote (code 2) à 05:58:36Z ; branches sans suffixe intactes.
- **Erreur de ma part, condition 2 des relances 2, 3 et 4** : leur inventaire de disque n'a pas été fait avant destruction (additif 2 v6, condition 2 ; additif 3 v2, ordre des gestes). Condition 2 tenue par trois autres preuves (journal sans « marche : début », inventaire final prouvé sans sortie, garde `detruire` acceptée) ; écart accordé par Lazar, GO-2026-11-21-03.
- **Erreur de ma part, outil de création** : le joueur de l'essai refusé de la relance 3 (06:05Z, offre 29019377 retirée par le loueur, « no_such_ask », rien créé) existait encore. L'outil refuse d'écraser un fichier, donc les offres acceptées par la garde entre 06:56Z et 07:11Z n'ont pas été jouées. Fichiers de l'essai renommés en « -essai1 », rien supprimé.
- **Recréations**, chacune après sa ligne d'engagement envoyée à la mère, réserve relevée ≤ 200 USD, `GO_ID=GO-2026-11-19-86`, commit de course 4bdf0d22… :

| n | instance | offre | machine | créée (UTC) | run | marche : début |
|---|---|---|---|---|---|---|
| 1 | 61761129 | 41153679 | 67802 | 05:55:07 | 20261121-055443-b5f-formation-1-x1 | 06:02:09 |
| 2 | 61761780 | 29296806 | 33686 | 06:02:07 | 20261121-060152-b5f-formation-2-x1 | 06:10:07 |
| 3 | 61768944 | 29019348 | 29089 | 07:12:59 | 20261121-071239-b5f-formation-3-x1 | 07:18:59 |
| 4 | 61770089 | 36602056 | 59032 | 07:23:14 | 20261121-072248-b5f-formation-4-x1 | 07:31:32 |

- **Commun** : 42,60 USD à 07:36Z ; crédit 82,73 USD.
- **Veille** : la configuration garde les premières tentatives sous « 1t » à « 4t », leurs heures fixes ; le commun fixe compte 2,26 USD de stockage des tentatives.

## Reste
- Veiller les quatre recréations jusqu'à leur fin (au plus tard le 22 novembre, 18:30:16Z). À chaque fin : branche `…-instance-<n>-x1`, commit prouvé lu dans le journal, inventaire au commit, garde `detruire` du lanceur d'`arbre-course-x1`, joueur éprouvé, destruction par l'identifiant, `verifier-destruction` (témoin 60988826).
- Ensuite : ligne `SORTIES-FORMATION-B5F`, contrôlée par programme, envoyée à la mère. Elle cite les têtes des branches des recréations pour 2, 3 et 4.

## Prochaine action
Relancer la veille si elle sort :

    cd $S && PAS_VEILLE_S=600 timeout 7000 python3 -I outils/veille_b5f_multi_x1.py b5f/veille-conf-x1.json b5f/veille-x1-etat.json b5f/veille-x1.txt

Codes de sortie : 10 étape, 20 arrêt, signal ou fin, 30 refus de la garde de dépense, 40 hors marche, 50 erreur du loueur.

## Instances (07:40Z)
- En marche : 61761129, 61761780, 61768944, 61770089.
- Non touchées : 58936096, 58936099, 58936100 (intouchables) et 60988826 (témoin).
