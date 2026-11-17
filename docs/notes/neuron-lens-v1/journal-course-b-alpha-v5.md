# Journal de la cinquième course de B-α (recourse de la lecture contre ablation, B-7, sur A100, seconde tentative) — v1

Feu neuf : mot direct de Lazar dans la session de la fille, « go », le 2026-11-17 vers 01:55 UTC, à la demande de feu neuf après
l'échec de la quatrième course (`journal-course-b-alpha-v4.md`, `d7f0d25f…`) ; commande v8 (`2df1dfdd…`), consignes de R-3056, plus deux
règles : aucune ligne de l'amorce en 20 min = destruction ; une seule tentative. Ligne GO-2026-11-14-06 ; écart de carte GO-2026-11-17-04.
Écrit par la fille « Neuron Lens » le 2026-11-17. **Issue : course terminée, deux séries (lots 16 et 64), aucun audit requis ; détruite ;
aucune mesure lue par la fille.**

| heure (UTC) | étape | fait |
|---|---|---|
| 01:56:01Z | 1-4 | suivi `verifier` code 0 ; `instances` : intouchables seulement ; crédit 6,300 USD, `can_pay`, `has_billing` vrais, `billing_failed` faux ; 3 offres ≤ 0,73 : 58627262 (même prix, lieu et fiche que l'échec : écartée), **56423175** (Alberta, 39 936 Mio, 0,5228, 32 cœurs, 128 Go, CUDA 13.4, fiabilité 0,995) choisie, 59897131. |
| 01:56:32Z | 5-7 | même dépôt réduit v9 (`141ba080`, liste `e3bcfb92…`) ; `calcul/neuron-lens-b-alpha-v6` absente ; RUN_ID `20261117-015632-neuron-lens-b-alpha` ; préavis à la mère ; création : **61001440**. |
| 01:57Z | 8-11 | prix lu **0,6033 USD/h** ; minuterie v4 PID 910 (D = 45 630 s, échéance ≈ 14:37Z) ; garde v4 PID 922 (plafond 8,5) ; rappels ; veille. |
| 01:57:52Z | 12 | amorce v7 : commit vérifié ; **carte (nvidia-smi) : NVIDIA A100-SXM4-40GB** ; installation de l'environnement (règle des 20 min tenue). |
| 02:11Z | 13 | `b0` poussé et lu (contrôle de montage) : essais 7/7, 8/8, 4/4, 13/13, B.3 35/35, aucun arrêt ni défaut (e) sur J, npJpp, npR. |
| 02:21Z | 13 | partie 2 sans écart ; tranche « chat » : 2 jetons de début dans 8 000 documents sur 8 000 ; les autres : 1. |
| 02:21 → 03:15Z | 12 | `fumee` ; `passe` complète (≈ 54 min) ; `b3`. |
| 03:15 → 03:36Z | 12 | `measure` (lot 16), `score`, `grandeurs`, `verdicts` ; aucun audit requis ; `bascule-lot64`. |
| 03:36 → 03:57Z | 12 | **`measure-lot64` (lot 64) passée en mémoire** ; `score-lot64`, `grandeurs-lot64`, `verdicts-lot64` ; aucun audit requis ; « fin : course terminee » à 03:57:15Z ; une relance du conteneur reconnue par l'entrée idempotente (« etat final deja atteint ; attente sans calcul »). |
| 03:58Z | 14 | état poussé final, `exclus=0` ; branche des résultats `ea814779` ; `verifier_resultat` **18 sur 18** ; compagnons **29 sur 29** ; copiés dans `prep/neuron-lens-v1` (`runs/20261117-015632-neuron-lens-b-alpha`, `diag/20261117-015632-neuron-lens-b-alpha`). **Aucun résultat de mesure lu par la fille.** |
| 03:58:32Z | 15 | préavis à la mère ; `vastai destroy instance 61001440 -y < /dev/null` code 0 ; `absente 61001440 --non-vide` code 0 ; minuterie et garde arrêtées par PID après lecture de leurs arguments, mortes ; rappels annulés ; veille arrêtée. |
| 03:58Z | — | location 2 h 2 min à 0,6033 USD/h ≈ **1,23 USD**, plus le trafic (faible). Crédit 6,300 → 9,718 USD : un rechargement automatique de 5 USD a eu lieu entre-temps (seuil 5 USD) ; au crédit, ≈ 1,58 USD, ce qui compte aussi la fin de la quatrième course. **Ligne GO-2026-11-14-06 : ≈ 3,4 à 4,0 USD sur 12.** |

`HF_TOKEN` : passé à la configuration de l'instance, retiré de la course après `telecharger-poids` (vérifié par l'amorce, par son nom),
détruit avec l'instance ; **révocation recommandée** (cinquième passage à une machine louée). Les fichiers bruts de `measure`
(`-causal.pt`, `-causal-lot16.pt`) sont restés sur l'instance et sont perdus avec elle (addendum v3, § 6).
