# Journal de la relance de la tranche B-α (GO-2026-11-14-06) — v2 (vivant pendant la course, scellé à la fin)

Commande jouée : `commande-b-alpha-v4.md` (`f54d5ec3…`, commit `541547fd`) ; feu écrit R-2892 (consignes de R-2887 : ≤ 0,73, P1, R1, R4,
préavis d'une ligne puis création sans attendre ; point 9 : préambule et étape 10 lus « préavis sans attente » ; point 6 : si les deux essais
qui lisent la copie d'origine échouent à B0, destruction immédiate, rapport, aucune relance sans relecture). Heures : `date -u`.

| heure (UTC) | étape | fait |
|---|---|---|
| 2026-11-15T10:19:3xZ | 1-2 | `show user` code 0 ; secrets présents (longueurs) ; suivi `verifier` code 0 ; `instances` : 58936096, 58936099, 58936100 (exited), **60480302 running (témoin)**. |
| 2026-11-15T10:19:52Z | 3 | Crédit 8,21 USD ; `can_pay`, `has_billing` vrais ; `billing_failed` faux. |
| 2026-11-15T10:19:53Z | 4 | 17 offres ≤ 0,73. Moins chère 45786456 (CN) 0,4028, écartée (accès au hub et à l'hébergeur de code) ; 47635080 (US-NJ) 0,4679, 16 cœurs tout juste ; **54329991 (US-UT) 0,4885**, 20 cœurs, 64 Go, CUDA 13.5, trafic 0,0039 USD/Go, stockage 0,267 : **choisie** (phase limitée par le processeur au volet A ; tables écrites par 16 processus). |
| 2026-11-15T10:20:1xZ | 5-6 | Dépôt réduit v5 au commit source `1ac4e1488bc95737d02985c60ecaf99220cbd912` : commit réduit `e6acd2b746f1095c855a09094cd9bc98474acec7`, 347 fichiers, **liste `0863f9c7…` = attendue**, paquet `11e5150e…` ; `course/neuron-lens-b-alpha-reduit-v5` poussée, tête = commit réduit ; `calcul/neuron-lens-b-alpha-v2` absente. RUN_ID `20261115-102017-neuron-lens-b-alpha`. |
| 2026-11-15T10:20:37Z | 7 | Préavis à la mère, création sans attendre (commits lus dans `rapport.json`) : `{"success": true, "new_contract": 60773264}` ; **instance 60773264**. |
| 2026-11-15T10:20:5xZ | 8 | Prix lu **0,5422 USD/h** (≤ 0,73 ; plus que les 0,4885 de la recherche : stockage de 150 Go compris). |
| 2026-11-15T10:21:08Z | 9-10 | Minuterie v4 **PID 606**, D = 71 673 s au prix lu, échéance absolue **2026-11-16T06:15:41Z** ; garde v4 **PID 620**, plafond 12. |
| 2026-11-15T10:21:2xZ | 11 | Rappels 15:14Z, 19:32Z, 2026-11-16T02:16Z ; veille et suivi en tâche de fond. |
| 2026-11-15T10:20:54Z → 10:22:13Z | 12 | Commit réduit vérifié ; environnement installé en **64 s** ; carte RTX 4090 ; essais de nos modules passés ; course lancée. |
| 2026-11-15T10:22:14Z → 10:28:54Z | 12 | `preparer` ; `telecharger-tokeniseur` ; **`b0` passé en 19 s** (correctif (1) 7/7 avec la copie d'origine, graine 8/8, crochets 4/4, lentilles 13/13, B.3 35/35 ; aucun défaut (e)) ; `telecharger-poids` en 72 s, **clé retirée** (vérifiée par son nom) ; `corpus` en 2 min 31 s ; **partie 2 sans écart** (tranche « chat » : 2 jetons de début dans 8 000 documents sur 8 000 ; `catalog.kept` 89 498) ; `fumee` en 67 s. |
| 2026-11-15T10:28:54Z → 11:29:50Z | 12 | `passe` complète en **61 min** (devis 1,0 à 1,4 h) ; `b3` rejoué. |
| 2026-11-15T11:29:51Z → 11:38:44Z | 12 | `measure` : pilotage des 32 couches fait (128 conditions par couche, 519 s) ; **échec dans l'ablation : CUDA out of memory** (24 Go ; 896 Mio demandés, 100 Mio libres ; lot `--ctx-batch 64` par défaut, soit 128 séquences par passe). Amorce : « fin : arret code 20 », état final poussé, `exclus=0`. |
| 2026-11-15T11:39:27Z | 15 | Préavis à la mère, `destroy instance 60773264 -y` ; **absence prouvée 11:39:34Z** (témoin 60480302). Minuterie PID 606, garde PID 620 et `sleep` orphelin PID 610 arrêtés par PID ; rappels supprimés ; veille et suivi arrêtés. |
| 2026-11-15T11:40:03Z | 14-15 | Résultats versés (`runs/` et `diag/20261115-102017-neuron-lens-b-alpha/`), `verifier_resultat` 10 sur 10. Crédit 5,74 USD (8,21 au départ ; la baisse comprend l'instance témoin d'une autre session, 1,17 USD/h). **Dépense de la relance ≈ 0,71 USD** (1 h 18 min 50 s à 0,5422), plus ≈ 0,1 USD de trafic ; **ligne GO-2026-11-14-06 : ≈ 0,85 USD** avec la première course. |
