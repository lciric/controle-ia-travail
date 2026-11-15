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
