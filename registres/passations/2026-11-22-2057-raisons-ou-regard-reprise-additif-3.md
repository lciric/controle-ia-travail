# Additif 3 à la passation de reprise « Raisons ou regard ? » — 2026-11-22T20:57:06Z

- Lot d'Astra (décisions 273 et 274 du chantier ; GO-2026-11-22-108, -111, -116) parti par tranches à 18:53Z : module exp1_lots_par_tranches.py (contre-lu par Sonnet, corrections vérifiées, 17 essais), plan 49 × 16 requêtes, ligne 70 USD.
- ARRÊTÉ à la tranche 22 : compte OpenAI de la clé injectée par le relais à sa limite de facturation (HTTP 400 billing_hard_limit_reached, rejet net, rien créé). 21 tranches relevées (336 requêtes sur 780), 14,53 USD réels. Commit abfd021 (raisons-ou-regard-travail, claude/stoic-mayer-51otyy).
- Sorties versées dans Sirmium/rr-resultats (hors_git/exp1_ter/2026-11-22-astra-tranches/).
- Incidents : le conteneur a redémaré deux fois pendant l'inactivité de la session (processus détachés tués) ; reprise sans renvoi ; conduite ensuite en tâche suivie.
- Écart de cloisonnement déclaré : 80 premiers caractères d'une invite système affichés par mégarde en inspectant la forme d'une requête (17:5xZ).
- Prochaine action (Lazar) : recharger le compte OpenAI puis relancer sur le même accord (« faux échec », la tranche 22 repart après une décision datée de renvoi, le code l'exige après un rejet net) ; ou décider d'assembler le lot arrêté (21 tranches), ce que le module ne fait pas après un rejet sans décision.
- Instances : aucune machine louée ; aucun processus d'envoi vivant.
