# Rapport de la session fille — reprise du tour v9 sur Colognese et Ward Q2, sans Argon (GO-2026-11-03-08) — v1

Écrit le 3 novembre 2026 à 12:37 UTC (heure relevée par `date -u`). Mot de session-depot (≈ 12:15 UTC). Aucune cellule lue ; seuls
statuts, modèles et coûts relevés.

## Déroulé (UTC)
- Copie de `donnees/collisionneur-v9-colognese-ward-q2-v1/` à `5490f53c` vers `donnees/collisionneur-v9-colognese-ward-q2-v1-suite/` :
  52 compagnons conformes.
- Barrage `barrage_reprise_cw_v1.py` (`04f304a3…`, par la fonction `verifier()` chargée comme module) : 7 valides, absences de C
  consignées, à jouer E3-T2-critique-croisee-E puis E3-T3 A, B, D, E. Lanceur `lancer-reprise-colognese-ward-q2-v9-sans-argon-v1.sh`
  (`9f413bea…`), port 8817, clé Gemini factice (aucun appel à Argon), contrôle ABDE (v12), même commande `etage3` que le départ.
- Épreuves sans clé ni appel conformes (sain jusqu'à « clé absente » ; refus : sans GO, GO absent, run manquant, compagnon cassé,
  cellule E3-T2-B retirée, contrôle déjà présent).
- Garde R12 au premier plan ; départ 12:13:39 ; barrage conforme ; contrôle ABDE conforme (0,001924 USD) ; `avant-reprise-v1.txt` scellé
  (`c2344a52…`).
- Cellules : E3-T2-critique-croisee-E essai 2 (Astra) 12:14:00 → 12:17:50, OK, 0,3425 ; E3-T3-reponse-A (Fable) OK 1,1479 ;
  B (Opus) OK 0,5621 ; D (Kimi) OK 0,2381 ; E (Astra) 12:36:00 → 12:36:51, OK, 0,3653. Relais Kimi 8817 PID 12007 arrêté par PID par le
  lanceur (2 appels, 0,238826 USD, aucun refus). Fin 12:36:52, **code 0**. Durée 23 min 13 s.

## Dépense
Reprise : 2,6559 USD de cellules + 0,0019 de contrôle. Dossier (journal du collisionneur) : 5,4661 USD, sous le plafond de 27.

## Scellement et vérification
Avant toute lecture : compagnons neufs de `journal.jsonl`, `etat.md` et de tous les fichiers produits ; liste
`EMPREINTES-tour-colognese-ward-q2-v9-reprise-v1.txt` (152 lignes) `6c02684dead49bb78ceefd2bf811dbd87cb79efe633defd161faf2c56f2c5387`, scellée.
Vérification par la fonction `verifier()` : **12 cellules valides** (C absente, acceptée), « tout tient ».
