# Rapport de la session fille — tour du collisionneur v9 sur Ibrahim Q1, variante sans Argon (GO-2026-11-03-06) — v1

Écrit le 3 novembre 2026 à 12:23 UTC (heure relevée par `date -u`). Ordre `docs/procedures/ordre-fille-tours-mentors-soir-v1.md`
(`b211ae27…`, `main` 8fdcdd33). Aucune cellule lue ; seuls statuts, modèles, type d'erreur et coûts relevés.

## Déroulé (UTC)
- Branche `donnees/collisionneur-v9-ibrahim-q1-v1` à `437c4d5e`, extraite par `git archive` ; 14 compagnons conformes ; lanceur
  `lancer-tour-ibrahim-q1-v9-sans-argon-v1.sh` `6293da64…` égal ; port 8814 libre ; garde R12 au premier plan conforme.
- Départ 11:40:33 ; lanceur PID **7803** (`bash -c`, lu au processus) ; relais Kimi 8814 PID 7846. Contrôle ABDE conforme, 0,00217 USD.
  C absente acceptée (variante déclarée).
- E3-T1 et E3-T2 : A, B, D, E OK ; E3-T3 : A, B OK ; **D (Kimi, essai 1, 12:16:09) : ECHEC**, HTTP 429 de Moonshot
  (`engine_overloaded_error`, « The engine is currently overloaded ») ; **arrêt en code 5** (aucun autre modèle ; E3-T3-reponse-E
  jamais lancée). Relais Kimi arrêté par PID par le lanceur. Fin 12:16:44, code 5. Durée 36 min 11 s.
- `verifier` (sous-commande, avant scellement) : « tout tient » ; **10 cellules valides** (E3-T1 et E3-T2 A, B, D, E ; E3-T3 A, B).

## Dépense
Fable 2,9228 ; Opus 1,2386 ; Kimi 0,3118 ; Astra 0,6098 : **5,0830 USD** au journal ; contrôle 0,00217 ; relais Kimi : 4 appels,
0,817196 USD (dont ≈ 0,505 au pire cas pour l'appel en échec, non compté au journal), aucun refus. Estimé ≈ 5,59 USD ; plafond 27.

## Scellement
Compagnons posés pour tous les fichiers produits ; liste `EMPREINTES-tour-ibrahim-q1-v9-sans-argon-v1.txt` (118 lignes)
`3fb35f9fb3bed76d55a38dc0a3a6047683e02fb06d9eb94c8b80f525397e3dad`, scellée. Versement : branche neuve
`donnees/collisionneur-v9-ibrahim-q1-v1-run` partie de `437c4d5e`.

## Suite possible (décision de session-depot)
Surcharge transitoire de Kimi : une suite du même run (E3-T3 D essai 2, puis E), sans Argon, sur le modèle des suites du 3 novembre.
