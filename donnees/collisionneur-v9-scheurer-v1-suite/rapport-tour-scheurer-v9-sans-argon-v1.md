# Rapport de la session fille — tour du collisionneur v9 sur Scheurer, variante sans Argon (GO-2026-11-03-07) — v1

Écrit le 3 novembre 2026 à 11:55 UTC (heure relevée par `date -u`). Ordre `docs/procedures/ordre-fille-tours-mentors-soir-v1.md`
(`b211ae27…`, `main` 8fdcdd33). Aucune cellule lue ; seuls statuts, modèles, catégories de refus et coûts du journal relevés.

## Déroulé (UTC)
- Branche `donnees/collisionneur-v9-scheurer-v1` à `f9fd47b7`, extraite par `git archive` ; 14 compagnons conformes ; lanceur
  `lancer-tour-scheurer-v9-sans-argon-v1.sh` `bd23fc0c…` égal ; port 8815 libre ; garde R12 au premier plan conforme.
- Départ 11:40:34 ; lanceur PID **7820** (`bash -c`, lu au processus) ; relais Kimi 8815 PID 7849. Contrôle ABDE conforme (modèle servi =
  demandé pour Fable, Opus, Kimi, Astra), 0,00195 USD. C absente acceptée au journal (variante déclarée).
- E3-T1 : A (Fable) OK 0,4358 ; **B (Opus) REFUS** (fin « refusal », catégorie « cyber »), 0,1597, 11:42:22 ; D (Kimi) OK 0,1911 ;
  E (Astra) OK 0,2091.
- **Arrêt en code 2** : « porte fermée après E3-T1 : ['E3-T1-conception-B'] non valides ; aucune suite sans décision de l'arbitre
  (--accepter-absence, ou nouveau run) ». Un refus est définitif dans un run (collisionneur v9). Relais Kimi arrêté par PID par le
  lanceur (7849 absent). Fin 11:54:44, code 2. Durée 14 min 10 s.
- `verifier` (sous-commande, avant scellement) : « tout tient » ; 3 cellules valides (E3-T1 A, D, E) ; sortie `verifier-scheurer-v9-sans-argon-v1.txt`.

## Dépense
Fable 0,4358 ; Opus 0,1597 ; Kimi 0,1911 ; Astra 0,2091 : **0,9957 USD** au journal ; contrôle 0,00195 ; relais Kimi : 2 appels,
0,191864 USD, aucun refus. Plafond 26 USD.

## Scellement
Compagnons posés pour tous les fichiers produits ; liste `EMPREINTES-tour-scheurer-v9-sans-argon-v1.txt` (76 lignes)
`9de99c7ebf741bfb206e3c4794e198fa33e2293017535be1f053ca17326ade74`, scellée. Versement : branche neuve
`donnees/collisionneur-v9-scheurer-v1-run` partie de `f9fd47b7`.

## Décision ouverte (session-depot ou arbitre)
Suite du même run avec `--accepter-absence E3-T1-conception-B` (B absente comme C), ou nouveau run, ou rien. Rien n'est relancé ici.
