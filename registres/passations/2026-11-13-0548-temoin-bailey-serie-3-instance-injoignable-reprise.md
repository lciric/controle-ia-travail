# Témoin de Bailey, troisième série — run principal interrompu (instance injoignable puis arrêtée) ; reprise (lecture 38) — 13 novembre 2026

Session `session_01XJ6MgnEhQMZteN9F8a1BST`. Ne se réécrit pas (R12). Aucune note de sonde ni de juge lue : seuls le
journal de la conduite, son bilan et des champs de l'inventaire Vast.

## Faits (journal `sortie-conduite-v11/conduite-v5.jsonl`, bilan `bilan-conduite-v5.json`, inventaire Vast à 05:46Z)
- Run principal lancé à 00:52:59Z (K = 72). Sondages de l'instance en échec à partir de 04:25:58Z ; 30 échecs
  consécutifs à 04:55:37Z ; la conduite a tenté l'arrêt par PID (veilleur 255), puis le transfert (« instance
  injoignable »), et n'a **pas** détruit : `detruite: false`, `transfert_complet: false`, aucune étape transférée ne fait
  foi (`reprise_requise` : mise en place, contrôle du juge, règle, pilote, principal) ; journal du chien de garde non
  transféré (`CalledProcessError`) ; alerte de la conduite : « reprise requise (`lanceur_v17 reprendre`) ; nœud ».
- Inventaire Vast : 60417353 `exited`, `intended_status: stopped`, `uptime_mins` ≈ 34,6 au moment de l'arrêt (le
  conteneur avait redémarré vers 04:21Z : coupure probable de l'hôte, non établie). Stockage seul facturé.
- D de la conduite à 04:55:56Z : 10,470 USD (compte prudent, B = 75).
- Nombre de tours complets du run principal : inconnu tant que les journaux ne sont pas transférés (≈ 9 à 10 attendus
  d'après la durée d'un tour du pilote ; non lu).

## Issue de la liste d'arrêt (texte l. 338, 371 ; addendum 2, lecture 38)
Interruption pendant le run principal : run tronqué, K′ = tours complets. Avant toute lecture et toute relance, la
**reprise** de la lecture 38 : redémarrage de l'instance arrêtée le temps du seul transfert (même GO), comparaison des
empreintes, scellement, destruction par identifiant ; aucune reprise du calcul. La session la lance (procédure scellée,
actée par Lazar, `6b1dc914…`) : poste Hetzner de reprise `runs/temoin-bailey-v1-20261111/poste-hetzner-reprise-v1.sh`
(empreinte au compagnon), qui exécute `lanceur_v17 reprendre --sortie <chemin absolu de sortie-conduite-v11>
--etiquette temoin-bailey-c6-89bd4d5cb025406c --go-id GO-2026-11-10-10`.

## Nœud pour Lazar (après la reprise)
Si K′ < 20 (attendu) : la liste d'arrêt prévoit **une seule relance entière** (« coupure de l'hôte », erreur technique
nommée), même graine, dossiers neufs, K recalculé sur le budget restant si ce K est ≥ 20. Elle demande une instance
neuve : la lecture de la condition 7 (addendum 4, § 6) ne vaut que pour une création avant 08:14Z le 13 novembre ;
la session ne crée donc aucune instance de relance sans le mot de Lazar. Les notes de la première exécution restent
scellées sans lecture jusqu'à la fin de la relance.
