# Journal de la course B-α, commande v5 (GO-2026-11-14-06) — v3 (vivant pendant la course, scellé à la fin)

Commande jouée : `commande-b-alpha-v5.md` (`423b74b4…`, commit `6d336a6a`) ; feu écrit R-2904 (consignes de R-2887 et R-2892 ; point 9 :
l'écart de lot `--ctx-batch 16` est à reporter au rapport de la course, le fichier de résultats ne le consignant pas ; point 12 : pire cas
à l'arrêt dur ≈ 11,75 USD sur la ligne, accepté ; marge de mémoire recalculée par le lecteur ≈ 3,7 à 4,1 Gio, à vérifier sur la première
ligne « ablate L0 » ; nouvel échec par mémoire : destruction immédiate, aucune relance sans relecture). Heures : `date -u`.
**Écart de lot déclaré** : `measure --ctx-batch 16` (graine 0) et `measure --ctx-batch 16 --seed 1` (audit « trop beau », s'il est requis),
au lieu du défaut 64 (l. 379 de la copie) ; les défauts gelés des l. 374 à 377 sont inchangés (R-2901).

| heure (UTC) | étape | fait |
|---|---|---|
| 2026-11-15T12:05:5xZ | 1-3 | `show user` code 0 ; secrets présents ; suivi `verifier` code 0 ; `instances` : 58936096, 58936099, 58936100 (exited) ; **le témoin 60480302 n'existe plus** (autre session) : absence à prouver par `--non-vide`. Crédit 5,46 USD ; `can_pay`, `has_billing` vrais, `billing_failed` faux. |
| 2026-11-15T12:06:02Z | 4 | 26 offres ≤ 0,73. 57320184 (US-PA) 0,3628, trafic 0,039 USD/Go (≈ 1 USD pour ≈ 25 Go) ; 60779603 (VN) 0,373, trafic 0,052 ; 45449274 (CN) 0,389, écartée ; **60688995 (US-OR) 0,4547**, 32 cœurs, trafic 0,0039, stockage 0,2, fiabilité 0,9966 : **choisie** (moins chère trafic compris). |
| 2026-11-15T12:06:2xZ | 5-6 | Dépôt réduit v6 au commit source `90823b4b7a148ac7eaa23a50d814be272681010a` : commit réduit `8458961cd0ecddbabbdff78bedb5cf68ec26a73a`, 347 fichiers, **liste `0293f4e1…` = attendue**, paquet `6ab0b1db…` ; `course/neuron-lens-b-alpha-reduit-v6` poussée, tête = commit réduit ; `calcul/neuron-lens-b-alpha-v3` absente. RUN_ID `20261115-120622-neuron-lens-b-alpha`. |
| 2026-11-15T12:06:41Z | 7 | Préavis à la mère, création sans attendre : `{"success": true, "new_contract": 60783204}` ; **instance 60783204**. |
| 2026-11-15T12:06:5xZ | 8-10 | Prix lu **0,4950 USD/h** ; minuterie v4 **PID 551**, D = 78 531 s, échéance absolue **2026-11-16T09:55:47Z** ; garde v4 **PID 564**, plafond 12. |
| 2026-11-15T12:07:1xZ | 11 | Rappels 17:00Z, 21:18Z, 2026-11-16T05:34Z ; veille et suivi en tâche de fond. |
| 2026-11-15T12:06:54Z → 12:09:03Z | 12 | Commit réduit vérifié ; environnement en **112 s** ; carte RTX 4090 ; essais de nos modules passés ; course lancée. |
| 2026-11-15T12:09:03Z → 12:34:14Z | 12 | `preparer` ; `telecharger-tokeniseur` ; **`b0` passé en 41 s** (correctif (1) 7/7, graine 8/8, crochets 4/4, lentilles 13/13, B.3 35/35 ; aucun défaut (e)) ; `telecharger-poids` en 3 min 30, **clé retirée** (vérifiée par son nom) ; `corpus` en 15 min (2 min 31 à la relance : débit des jeux publics) ; **partie 2 sans écart** (tranche « chat » : 2 jetons de début dans 8 000 documents sur 8 000 ; les autres : 1) ; `fumee` en ≈ 3 min. |
| 2026-11-15T12:34:14Z → 13:40:21Z | 12 | `passe` complète en **66 min** ; `b3` rejoué. |
| 2026-11-15T13:40:21Z → 14:04:33Z | 12 | **`measure --ctx-batch 16`** (écart de lot déclaré, R-2901 : défaut publié 64, l. 379 de la copie ; défauts gelés des l. 374 à 377 inchangés ; le fichier de résultats ne consigne pas ce lot, il est consigné ici, R-2904 point 9) : pilotage des 32 couches en 514 s ; **« ablate L0 : 512 contexts, 29s »** à 13:49:34 : pas de mémoire épuisée ; ablation des 32 couches à ≈ 29 s chacune. |
| 2026-11-15T14:04:33Z → 14:10:58Z | 12 | `score` en ≈ 3 min ; **`grandeurs` faites** (garde de fidélité à `score` passée) ; `verdicts` faits, **aucun audit R4 requis** ; « fin : course terminee », état final poussé, `exclus=0`. |
| 2026-11-15T14:13:24Z | 15 | Préavis à la mère, `destroy instance 60783204 -y` ; **absence prouvée 14:13:32Z** (`--non-vide`, liste de 3 ; le témoin 60480302 n'existe plus). Minuterie PID 551, garde PID 564 et `sleep` orphelin PID 555 arrêtés par PID ; rappels supprimés ; veille et suivi arrêtés. |
| 2026-11-15T14:13:56Z | 14-15 | Résultats versés (`runs/` et `diag/20261115-120622-neuron-lens-b-alpha/`, 16 Mo), `verifier_resultat` 13 sur 13, compagnons de la partie 2, des grandeurs par pôle et du résumé de `score` conformes. Crédit 6,48 USD (rechargement automatique de 5 USD entre-temps). **Dépense de cette course ≈ 1,05 USD** (2 h 6 min 43 s à 0,4950 USD/h), plus ≈ 0,1 USD de trafic ; **ligne GO-2026-11-14-06 : ≈ 2,0 USD** sur 12 avec les deux courses précédentes. **Aucun résultat n'est lu par la fille** : la lecture revient à un lecteur neuf (devis v2, m8). |
