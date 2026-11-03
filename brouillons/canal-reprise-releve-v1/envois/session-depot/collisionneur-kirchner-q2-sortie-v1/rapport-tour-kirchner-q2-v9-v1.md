# Rapport de la session fille — tour du collisionneur v9 sur Kirchner Q2 (GO-2026-11-03-04) — v1

Écrit le 3 novembre 2026 à 11:24 UTC (heure relevée par `date -u`). Ordre `docs/procedures/ordre-fille-collisionneur-kirchner-q2-v1.md`
(`9e553f68…`, `main` 0aecc10e). Aucune cellule lue ; seuls les statuts, modèles et coûts du journal ont été relevés.

## Déroulé (UTC)
- Sources : branche `donnees/collisionneur-v9-kirchner-q2-v1` à `16ec2e5a`, extraite par `git archive` ; 13 compagnons conformes ;
  LISEZMOI `291790aa…`, question `291f91f8…`, faits `cc202ecd…`, collisionneur `27e9ce40…`, lanceur `8c0d3812…` ; ports 8805 et 8812 libres.
- **Incident sans dépense (10:22:52)** : la commande du § 2 de l'ordre, telle qu'écrite, met toute la chaîne `&&` en arrière-plan ;
  `echo $! > lanceur-kirchner-q2-v9-v1.pid` s'est exécuté en parallèle et a créé ce fichier avant la garde R12, qui a refusé (exit 2) ;
  rien n'est parti. Fichier (contenu 1468) retiré du dossier, gardé hors du dépôt ; même commande relancée, garde jouée d'abord au premier plan.
- Départ 10:23:14 ; PID du lanceur **1546** (`bash -c`, lu au processus ; `$!` désignait `setsid`) ; relais Kimi 8812 PID 1583.
- Contrôle v10 : cinq espèces OK, modèle servi = modèle demandé ; 0,00279 USD.
- Cellules 1 à 13 OK (sous-tours 1 et 2 complets ; E3-T3 A, B, C). **`E3-T3-reponse-D`** (Kimi, essai 1, 11:16:14) : **ECHEC**, HTTP 502 du
  relais « amont coupé après envoi (dépense au pire cas) : ConnectionResetError » ; **arrêt du tour en code 5** (aucun autre modèle
  essayé ; `E3-T3-reponse-E` jamais lancée). Relais arrêté par PID par le lanceur (1583 absent, 8812 libre). Fin du lanceur 11:23:21,
  code 5 (`code-kirchner-q2-v9-v1.txt`). Durée : 1 h 00 min 7 s.
- `collisionneur_v9.py verifier run-kirchner-q2-e3-v1` (avant scellement) : « tout tient », **13 cellules valides** (attendu 15) ;
  non valides : `E3-T3-reponse-D`, `E3-T3-reponse-E`. Sortie : `verifier-kirchner-q2-v9-v1.txt`.

## Dépense
| Espèce | Journal du collisionneur (USD) |
|---|---|
| A Fable 5.1 | 3,8380 |
| B Opus 5.5 | 2,0519 |
| C Argon | 2,2334 |
| D Kimi (cellules réussies) | 0,3917 |
| E Astra | 0,9806 |
| **Total du dossier** | **9,4956** |
Relais Kimi : 4 appels, 0,99568 USD, dont **0,603056 au pire cas pour l'appel en échec** (non compté au journal du collisionneur) ;
contrôle 0,00279. Dépense estimée du tour : ≈ 10,10 USD (plafond 34, GO 35).

## Scellement
Compagnons posés pour tous les fichiers produits (journal compris) ; liste `EMPREINTES-tour-kirchner-q2-v9-v1.txt` (134 fichiers),
`71891883346518d3cd88e49850229586dce6816b51b837bb4cbdbd324325202e`, scellée. Versement : branche neuve `donnees/collisionneur-v9-kirchner-q2-v1-run`
partie de `16ec2e5a`.

## Suite possible
Les deux cellules manquantes (D essai 2, E essai 1) peuvent être jouées par une suite, comme le 3 novembre au matin (contrôle et
barrage sur D et E, sans Argon) : décision de session-depot.
