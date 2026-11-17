# Journal de la quatrième course de B-α (recourse de la lecture contre ablation, B-7, sur A100) — v1

Feu R-3056 de la mère (commande v8, `2df1dfdd…`, commit `3e2256ba`), ligne GO-2026-11-14-06, écart de carte GO-2026-11-17-04.
Écrit par la fille « Neuron Lens » le 2026-11-17. **Issue : machine qui ne démarre pas ; détruite ; rien calculé ; aucune mesure.**

| heure (UTC) | étape | fait |
|---|---|---|
| 01:10:5xZ | 1-3 | outil 1.11.0 ; `show user` code 0 ; secrets présents par leur longueur ; suivi `verifier` code 0 ; `instances` : 58936096, 58936099, 58936100 (arrêtées), 60988826 (en marche, autre session) : intouchables seulement. Crédit 6,446 USD ; `can_pay`, `has_billing` vrais, `billing_failed` faux. |
| 01:10:57Z | 4 | 4 offres A100 SXM4 ≤ 0,73 à la recherche ; **58627260** (Californie, 40 960 Mio) 0,3747, stockage 0,2 USD/Go/mois, trafic 0,0039 et 0,0026, 24 cœurs, 128 Go, CUDA 13.2, fiabilité 0,993 : choisie. |
| 01:11:0xZ | 5-6 | dépôt réduit v9 sur `3e2256ba` : liste `e3bcfb92…` (= essai à blanc), commit réduit `141ba080`, poussé sur `course/neuron-lens-b-alpha-reduit-v9` ; `calcul/neuron-lens-b-alpha-v6` absente ; RUN_ID `20261117-011123-neuron-lens-b-alpha`. |
| 01:11:46Z | 7 | préavis à la mère ; création : `new_contract` **60997517**. |
| 01:11:52Z | 8 | prix lu **0,415 USD/h** (≤ 0,73). |
| 01:12:04Z | 9-10 | minuterie v4 PID 29128, D = 66 345 s, échéance 19:37:31Z ; garde v4 PID 29140, plafond 8,5 ; rappels programmés ; veille. |
| 01:12 → 01:53Z | 13 | instance « loading », message du loueur « 3.12-bookworm: Pulling from library/python » sans changement pendant **41 min** ; `logs` : « No such container » ; aucune ligne de l'amorce, branche des résultats jamais créée. (Troisième course : démarrage en ≈ 2 min.) |
| 01:53:0xZ | 15 | préavis à la mère ; `vastai destroy instance 60997517 -y < /dev/null` code 0 ; `suivi_vast_v6 absente 60997517 --non-vide` code 0 ; minuterie et garde arrêtées par PID après lecture de leurs arguments, mortes ; rappels annulés ; veille arrêtée. |
| 01:53:40Z | — | crédit 6,308 USD (−0,138) ; temps facturable au prix lu ≤ 41 min 25 s × 0,415 = 0,29 USD : **dépense ≈ 0,14 à 0,29 USD** ; ligne GO-2026-11-14-06 ≈ 2,2 à 2,4 USD sur 12. |

Aucun résultat, aucune mesure, rien à lire. `HF_TOKEN` a été passé à la configuration de l'instance (jamais au conteneur, qui n'a pas
démarré) ; détruit avec elle. Une nouvelle création exige un feu neuf (R-3056 : « aucune relance sans feu neuf »).
