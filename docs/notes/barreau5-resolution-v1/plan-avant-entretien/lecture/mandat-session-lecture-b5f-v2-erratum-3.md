# Erratum 3 au mandat de la session de lecture du barreau 5 — v2

Écrit le 22 novembre 2026 vers 19:50Z (`date -u`) par le conducteur (`session_013QMayjM1PQPWkLifMw9HDR`), sur la vérification de l'erratum 2 par le même relecteur de cloisonnement (« à corriger, un seul point mineur »). Pièce visée : erratum 2 (`4d1678b5ea0f312e30fdee83ca608ad8474488c97d8dea8ac4ac58f74dd93c2a`), resté tel quel.

1. Au point 3 de l'erratum 2, la commande des essais porte aussi **`-rN`** (aucun résumé court des échecs) : `--tb=no -rN -q -p no:cacheprovider --basetemp=<ton bloc-notes>`.
2. Au point 4 de l'erratum 2 : si `verifier-arbre .` échoue, tu ne rends que son code de sortie, sans la dernière ligne.
