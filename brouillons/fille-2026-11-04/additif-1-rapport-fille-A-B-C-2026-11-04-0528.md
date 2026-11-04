# Additif 1 au rapport de la fille (b7231983…) — écrit le 2026-11-04 vers 05:30 UTC (date -u)
- Cause probable de l'arrêt de B : la session de la fille a été coupée par la limite d'usage des 5 heures vers 03:46 UTC (selon la mère ; remise à zéro 05:20), puis le conteneur a été repris (démarrage 05:22:53). Concorde avec les traces : dernier relevé de garde à 03:44:11Z, dernier appel au relais à 03:45:18Z, tous les processus disparus ensemble.
- Dépense de B lue au journal du relais (`relais-argon-journal-a1-v3-seconde.jsonl`, champ depense_cumulee_usd du dernier appel) : 48,49583 USD. Le registre de dépense de la sortie n'a pas été lu ; il est dans l'état scellé (fd66feb7…).
- Rien de la sortie de B n'a été lu.
