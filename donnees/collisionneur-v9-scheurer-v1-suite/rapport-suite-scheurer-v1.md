# Rapport de la session fille — suite du tour v9 sur Scheurer, sans Argon ni Opus (GO-2026-11-03-07) — v1

Écrit le 3 novembre 2026 à 13:37 UTC (heure relevée par `date -u`). Décision de Lazar « (a) Continuer sans l'espèce qui a refusé »
(conv-audit n° 421), ordre de session-depot ≈ 13:10 UTC. Aucune cellule lue ; seuls statuts, modèles et coûts relevés.

## Déroulé (UTC)
- Copie de `donnees/collisionneur-v9-scheurer-v1/` à `b733fe22` vers `donnees/collisionneur-v9-scheurer-v1-suite/` : 40 compagnons conformes.
- Barrage `barrage_suite_scheurer_v1.py` (`c5a913e3…`) : 3 valides (E3-T1 A, D, E) ; C consignée ; E3-T1-conception-B au statut REFUS
  (catégorie « cyber », la seule) ; E3-T2-B et E3-T3-B jamais lancées ; à jouer E3-T2 et E3-T3 de A, D, E.
- Lanceur `lancer-suite-scheurer-v9-sans-argon-v1.sh` (`42c1dc49…`, copie de la reprise Colognese-Ward), port 8819, clé Gemini factice,
  contrôle sur A, D, E (`appel_controle_v12.py`, 0,001812 USD, conforme).
- **Écart déclaré** : `--accepter-absence` donné aux trois cellules de B, y compris **E3-T1-conception-B**, non nommée dans l'ordre : sans
  ce drapeau, `lancer_etage` du collisionneur voit le statut REFUS et referme la porte (code 2) avant tout appel ; avec lui, la cellule
  est sautée (« absence acceptée par l'arbitre, non relancée ») et **n'est jamais rejouée** (R-486). Aucun appel à Opus ni à Argon.
- Épreuves sans clé ni appel conformes (sain jusqu'à « clé absente » ; refus : sans GO, GO absent, run manquant, compagnon cassé,
  cellule E3-T1-D retirée, contrôle déjà présent).
- Garde R12 au premier plan ; départ 13:10:25 ; `avant-suite-v1.txt` scellé (`dea8848c…`). Cellules : E3-T2 A (Fable) OK 1,0973 ;
  D (Kimi) OK 0,1379 ; E (Astra) OK 0,3128 ; E3-T3 A (Fable) OK 0,8932 ; D (Kimi) OK 0,1784 ; E (Astra) OK 0,3769. Relais Kimi 8819
  PID 19901 arrêté par PID par le lanceur (3 appels, 0,317122 USD, aucun refus). Fin 13:37:26, **code 0**. Durée 27 min 1 s.

## Dépense
Suite : 2,9965 USD de cellules + 0,0018 de contrôle. Dossier (journal du collisionneur) : 3,9922 USD, sous le plafond de 26.

## Scellement et vérification
Avant toute lecture : compagnons neufs de `journal.jsonl`, `etat.md` et de tous les fichiers produits ; liste
`EMPREINTES-tour-scheurer-v9-suite-v1.txt` (134 lignes) `9ff6a3e285d57584c5b82c49855a6ba42baf8dc41790b1ada0c8dccf25b27113`, scellée.
Vérification par la fonction `verifier()` : **9 cellules valides** (trois espèces A, D, E sur trois sous-tours ; B absente après son
refus, C absente), « tout tient ».
