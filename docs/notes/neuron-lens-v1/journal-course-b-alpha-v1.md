# Journal de la course de la tranche B-α (GO-2026-11-14-06) — v1 (vivant pendant la course, scellé à la fin)

Commande jouée : `commande-b-alpha-v2.md` (`cf437d95…`, commit `1bb1ba17`) ; feu écrit R-2887 (consignes P1, prix lu ≤ 0,73, R1, R4,
création sur préavis sans attendre, R-2883). Heures : `date -u`.

| heure (UTC) | étape | fait |
|---|---|---|
| 2026-11-15T09:48:28Z | 1 | `vastai` 1.11.0 à /home/user/vastai-env/bin ; `show user` code 0. |
| 2026-11-15T09:48:3xZ | 2 | Secrets présents (longueurs seules) ; suivi v6 `verifier` code 0 ; `instances` code 0 : 58936096, 58936099, 58936100 (exited), **60480302 running (témoin)** ; aucune autre. |
| 2026-11-15T09:48:51Z | 3 | Crédit 8,97 USD ; `can_pay` vrai, `has_billing` vrai, `billing_failed` faux ; rechargement 5 USD sous 5 USD. |
| 2026-11-15T09:48:52Z | 4 | Recherche (filtre `dph_total<=0.73`) : 23 offres. Moins chère : 60747789 (VN) 0,3730, trafic 0,052 USD/Go, stockage 0,333 USD/Go/mois ; 45449268 (CN) 0,4028 ; **59118977 (JP) 0,4540**, trafic 0,0065 USD/Go, stockage 0,093, 24 cœurs, 128 Go, CUDA 13.4, fiabilité 0,9992. **Choix : 59118977** (écart déclaré à « la moins chère » : ≈ 20 Go à télécharger coûtent ≈ 1 USD de trafic sur 60747789 contre ≈ 0,13 sur 59118977, et son stockage de 150 Go ≈ 0,07 USD/h ; la Chine est écartée pour le risque d'accès au hub et à l'hébergeur de code). |
| 2026-11-15T09:5xZ | 5 | Dépôt réduit v4 au commit source `24baf09f19473f2cc809f85ab40e499fdd53c3c5` : commit réduit `e80e91ecbadc3af223ab713520cf730cca3a8c1c`, 347 fichiers (276 du voisin), **liste `6c1a9f6e…` = attendue**, paquet `ef1a6e8d…` ; branche `course/neuron-lens-b-alpha-reduit-v4` poussée, tête distante = commit réduit ; `calcul/neuron-lens-b-alpha-v1` absente. |
| 2026-11-15T09:49:40Z | 6 | RUN_ID = `20261115-094940-neuron-lens-b-alpha`. |
| 2026-11-15T09:50:0xZ | 7 | Préavis à la mère (offre, prix), puis création sans attendre (R-2887, 5) : commits lus par programme dans `rapport.json` (R1) ; `{"success": true, "new_contract": 60770175}` ; **instance 60770175**, création 2026-11-15T09:50:11Z. |
| 2026-11-15T09:50:2xZ | 8 | Prix lu sur l'instance : `dph_total` **0,4728 USD/h** ≤ 0,73 ; RTX 4090 ; « running ». |
| 2026-11-15T09:50:32Z | 9 | Minuterie v4 armée : **PID 823**, D = 82 216 s au prix lu (formule de la garde v4), échéance absolue **2026-11-16T08:40:48Z**. |
| 2026-11-15T09:50:4xZ | 10 | Garde v4 détachée : **PID 863**, plafond 12 (compte rendu 7,20 ; arrêt dur 10,80), prix 0,4728. |
| 2026-11-15T09:51Z | 11 | Rappels : 14:44Z (4,9 h), 19:02Z (9,2 h), 2026-11-16T04:06Z (80 % de D) ; veille en tâche de fond (5 min, 2 h, relancée à chaque contrôle). |
