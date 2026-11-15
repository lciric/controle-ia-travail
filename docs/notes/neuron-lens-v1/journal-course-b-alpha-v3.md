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
