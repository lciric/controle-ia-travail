# Rapport de la session fille — reprise du tour v9 sur Ibrahim Q1, sans Argon (GO-2026-11-03-06) — v1

Écrit le 3 novembre 2026 à 12:36 UTC (heure relevée par `date -u`). Mot de session-depot (≈ 12:24 UTC). Aucune cellule lue ; seuls
statuts, modèles et coûts relevés.

## Déroulé (UTC)
- Copie de `donnees/collisionneur-v9-ibrahim-q1-v1/` à `d60629fa` vers `donnees/collisionneur-v9-ibrahim-q1-v1-suite/` : 61 compagnons conformes.
- Barrage `barrage_reprise_ib_v1.py` (`dede2cdf…`, copie de `barrage_reprise_cw_v1.py` dont seules changent les listes) : 10 valides,
  absences de C consignées, à jouer E3-T3 D puis E. Lanceur `lancer-reprise-ibrahim-q1-v9-sans-argon-v1.sh` (`8f47a78d…`, copie de la
  reprise Colognese-Ward, `9f413bea…`), port 8818, clé Gemini factice (aucun appel à Argon), contrôle ABDE (v12).
- Épreuves sans clé ni appel conformes (sain jusqu'à « clé absente » ; refus : sans GO, GO absent, run manquant, compagnon cassé,
  cellule E3-T3-B retirée, contrôle déjà présent).
- Garde R12 au premier plan ; départ 12:25:38 ; barrage conforme ; contrôle ABDE conforme (0,002164 USD) ; `avant-reprise-v1.txt` scellé
  (`b7eadd59…`). `E3-T3-reponse-D` essai 2 (Kimi) : 12:25:52 → 12:34:58, OK, 0,2116 USD. `E3-T3-reponse-E` (Astra) : 12:34:58 → 12:36:22,
  OK, 0,4148 USD. Relais Kimi 8818 PID 16145 arrêté par PID par le lanceur (2 appels, 0,212654 USD, aucun refus). Fin 12:36:23, **code 0**.

## Dépense
Reprise : 0,6264 USD de cellules + 0,0022 de contrôle. Dossier (journal du collisionneur) : 5,7094 USD ; avec le pire cas de l'appel Kimi
en échec du tour (≈ 0,505) et les contrôles : ≈ 6,22 USD, sous le plafond de 27.

## Scellement et vérification
Avant toute lecture : compagnons neufs de `journal.jsonl`, `etat.md` et de tous les fichiers produits ; liste
`EMPREINTES-tour-ibrahim-q1-v9-reprise-v1.txt` (152 lignes) `68544772d0f7e4d19b7270cdad12db4c62ead91e16aa0a01dc5c2e4cc1538087`, scellée.
Vérification par la fonction `verifier()` chargée comme module : **12 cellules valides** (C absente, acceptée), « tout tient ».

## Déclaration
Deux appels de contrôle d'Astra seul (lettre E, `appel_controle_v12.py`, clé OpenAI seule, GO-2026-11-03-05), à 12:15:34 et 12:18:45 UTC,
0,00041 USD chacun, **hors lanceur**, faits sur le mot de session-depot pour constater la fin de la panne d'OpenAI (journal
`/home/user/controle-astra-v1/journal-sonde-astra-v1.log`).
