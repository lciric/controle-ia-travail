# Passation — session de formation du barreau 5 — 2026-11-21 (heure du nom, `date -u`)

Session sortante `session_01QPDgKjCQYmTHUEjN63ThC8`, rôle du point 7, premier tiret, du texte scellé du barreau 5. Mère : `session_01QPDgKgejkqwnuaJHJ31Ydo` (Lazar la passe sur un autre compte). Écrite sur la demande de la mère (message de 14:47Z). Aucun score, aucune sortie de marche lue, jamais.
Détail : `docs/notes/barreau5-resolution-v1/plan-avant-entretien/formation/passation-session-formation-2026-11-21-1455.md` et les passations antérieures du même dossier, sur la branche `formation-b5f/plan-de-marche-v1`.

## Fait
- **Toutes les marches de la formation sont menées au bout** (code 0), avec un versement final prouvé, et toutes leurs instances sont détruites par l'identifiant, absence prouvée (témoin 60988826) :

| copie lue | instance | marche | FIN (UTC) | commit prouvé | détruite (UTC) |
|---|---|---|---|---|---|
| 6 | 61552174 | 20261120-012937-b5f-formation-6 | 2026-11-20 08:53 | 0a6af341244900da047ea850a966bf137dee279b | 2026-11-20 10:01:46 |
| 7-x1 | 61655818 | 20261120-144552-b5f-formation-7-x1 | 2026-11-20 18:46:42 | 7714b0ac6a9a11cd2b1644a747bda0dcccec513a | 2026-11-20 18:55:56 |
| 5-x1 | 61655633 | 20261120-144431-b5f-formation-5-x1 | 2026-11-20 21:31:18 | e37790479d51c4f5fd7d68f11037254f15749de5 | 2026-11-20 21:32:47 |
| 2-x1 | 61761780 | 20261121-060152-b5f-formation-2-x1 | 2026-11-21 12:56:07 | 7b0e19b928d76c1f655dc512eea72440a570ebce | 2026-11-21 13:05:03 |
| 1-x1 | 61761129 | 20261121-055443-b5f-formation-1-x1 | 2026-11-21 13:07:00 | eb4b946c333be96515f3c36fa9537816259673ac | 2026-11-21 13:15:37 |
| 3-x1 | 61768944 | 20261121-071239-b5f-formation-3-x1 | 2026-11-21 14:16:23 | f74795a16c609eb00cc86c5043bf211805c428bb | 2026-11-21 14:27:28 |
| 4-x1 | 61770089 | 20261121-072248-b5f-formation-4-x1 | 2026-11-21 14:45:25 | 75814afec793814f44afff946344e94d46ea8f0e | 2026-11-21 14:48:13 |

- Premières copies de 1, 2, 3, 4, 5 et 7 (première vague, arrêtées au crédit nul) : disques inventoriés puis détruits le 20 novembre (GO-2026-11-20-51). Premières tentatives des relances 1 à 4 (machine 144450, tombées à l'installation des paquets) : traces copiées sous `traces/barreau5-relance-<n>-premiere-tentative`, instances détruites le 21 novembre à 05:53Z (GO-2026-11-21-01 ; écart sur l'inventaire de disque de 2, 3 et 4 accordé, GO-2026-11-21-03) ; leurs branches de sortie supprimées par Lazar.
- **Pièce des sorties** : `docs/notes/barreau5-resolution-v1/plan-avant-entretien/formation/sorties-formation-b5f-v1.md` (sha256 41e51f9970eda5f4351cac01a41a97296741d5f2ce5e62ba46d56e8af9fc04e6, commit 3dff7bed46ce62def89dddf835a372f6e2b23b72). **Ligne `SORTIES-FORMATION-B5F`** rédigée (texte exact : `versement-bloc-notes-session-formation-v9/b5f/ligne-sorties-formation-b5f-v1.txt`), contrôlée : registre de main plus la ligne, « ACCEPTÉ » par `relance-six-instances-v1/controler_registre_candidat_v1.py`. Envoyée à la mère par `registres/essaim/vers-mere/2026-11-21-1450-formation-b5f.md`.

## Ce qui tourne
- **Aucune instance de la formation.** Aucune instance étiquetée `b5f-formation-v1-<n>` chez le loueur (relevé de 14:48Z).
- Non touchées, hors de mon rôle : 58936096, 58936099, 58936100 (intouchables) ; 60988826 (témoin, ne se détruit pas).
- Aucune veille en cours.

## Reste
1. La mère inscrit `SORTIES-FORMATION-B5F` (forme à confirmer : pièce citée, 453 signes ; ou détail par instance, environ 1 100 signes) et réunit la branche de la formation : un seul dossier `donnees/<marche>` par instance (code de lecture figé, `_familles_formees`), les têtes des recréations pour 2, 3 et 4, jamais les traces des premières tentatives.
2. Réponse de la mère : qui écrit le code de l'additif 1 au devis (plafond de stockage de la machine de relecture à 0,12 USD/h ; commande v2 et lanceur v2) ; ma proposition : un agent Fable, contre-lu par Opus, commandé par la mère.
3. Sur le mot exprès de la mère seulement : sel, table, `ENGAGEMENT-B5F` (après `SORTIES-FORMATION-B5F` et la ligne de relance).
4. Ensuite, la relecture (coupure 21 USD) et la répétition générale (coupure 8 USD), selon le texte et l'additif 1 au devis.

## Dépenses
- Commun de la formation : **71,73 USD** sous le plafond de 200 USD (GO-2026-11-19-86) : première vague 18,59 ; stockage des premières tentatives 2,26 ; relances 5 et 7 : 7,93 et 4,97 ; premières tentatives des relances 1 à 4 : 0,70, 1,17, 1,17, 1,15 ; recréations 1 à 4 : 8,76, 8,54, 8,35, 8,13 (heures × prix, depuis le `start_date` du loueur).
- Crédit du loueur : 49,42 USD à 14:48Z. Entre 05:55Z et 14:48Z, il a baissé de 39,18 USD pour 33,78 USD d'heures × prix des recréations ; écart de 5,4 USD, sans doute des transferts réseau, non expliqué.
- Restent au devis : relecture 21 USD, répétition 8 USD.

## Réserves
- Inventaire de disque des premières tentatives des relances 2, 3 et 4 non fait avant destruction (mon erreur) ; écart accordé, GO-2026-11-21-03.
- Voie directe vers la mère refusée depuis 11:30Z (« elevated_session_untrusted_device ») ; canal en essaim depuis 14:00Z.
- La garde `detruire` suppose une référence locale fraîche de la branche de sortie : après une suppression puis recréation de branche, faire un fetch forcé (`+refs…`).
- Le registre propre a été réécrit une fois par la voie (c) (GO-2026-11-21-47) : toute clé inconnue du code figé s'écrit sous la table, sans barre de tête.

## Prochaine action
Relever `registres/essaim/vers-formation-b5f/` sur main (s'il existe) et les messages directs de la mère ; selon sa réponse, ajuster la forme de `SORTIES-FORMATION-B5F` (contrôle par le lecteur figé avant toute ligne de table) ; puis attendre son mot pour le sel, la table et l'engagement. Brief de reprise : `registres/passations/brief-lancement-formation-barreau5-v1.md`.
