# Test de maintien de la machine de la session par une tâche d'arrière-plan suivie — 12 novembre 2026, 08:27 UTC

Session `session_01XJ6MgnEhQMZteN9F8a1BST`. Ne se réécrit pas (R12). Suit `2026-11-12-0815-…` (`a8496ee7…`).

**Résultat : réussi.** Tâche d'arrière-plan suivie par l'outil (`bn4mjjv4t`, boucle `date` puis `sleep 60`, 110 minutes au
plus), lancée à 08:09Z ; fin du tour vers 08:19Z ; réveil à 08:26:14Z. Démarrage de la machine identique au début et à la
fin (`uptime -s` : 2026-11-12 08:07:58) ; dernière écriture de la tâche : 08:25:44Z. Une tâche suivie garde donc la
machine allumée pendant l'inactivité (au moins 7 minutes observées), alors que sans elle la machine s'est éteinte environ
4 minutes après la fin d'un tour (07:58:40Z).

Mot de Lazar (≈ 08:11Z) : « go (a) si le test réussit » : relance du témoin de Bailey dans cette session, machine tenue
allumée par des tâches d'arrière-plan suivies enchaînées (chacune bornée à 2 heures), jusqu'au départ du run principal.
