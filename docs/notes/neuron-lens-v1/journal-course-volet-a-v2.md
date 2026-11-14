# Journal de la course du volet A de « Neuron Lens » — v2 (commande v14, feu R-2793)

Suite du journal v1 (`journal-course-volet-a-v1.md`, scellé : tentative du 14 novembre sur la v11, instance 60669495 créée à l'arrêt et
détruite). Session `session_016QhUrtahFZo57fZUcRReVA`, branche `prep/neuron-lens-v1`. Heures par `date -u`, dans la commande même.

**Consigne de la mère en cours de course** (message de 16:50:04Z, reprise dans le feu R-2793) : à chaque contrôle de suivi de l'étape 11,
le relevé de l'étape 3 est rejoué et journalisé ; si `credit` < 1 USD, `billing_failed` vrai ou `can_pay` faux → arrêt : récupération de
la branche des résultats (étapes 11-12), destruction selon l'étape 13 (`-y`, absence prouvée), arrêt de la minuterie et de la garde par
PID, message à la mère. Limite : sans ssh, seule la dernière poussée périodique (≤ 30 min) et l'état poussé sont sauvés.

| heure (UTC) | étape | fait |
|---|---|---|
| 2026-11-14T16:51:24Z | feu | Feu écrit R-2793 lu ; vérifié à la source (`main` `a1dd2dc2`, ligne R-2793, note `b6fdc937…`, « conforme avec mineurs », aucune condition bloquante ; v14 `14fe6383…` égale à l'empreinte du feu). |
| 2026-11-14T16:52:01Z | 1-2 | Outil `/home/user/vastai-env/bin/vastai`, `show user` code 0 ; jeton ≥ 8 ; `suivi_vast_v6 verifier` code 0 (5 instances : 58936096/099/100 « exited », 60480302 et **60670453** « running », toutes d'autres sessions, non touchées) ; témoin 60480302. |
| 2026-11-14T16:52:06Z | 3 | `credit` 4,48 USD, `can_pay` vrai, `has_billing` vrai, `billing_failed` faux, rechargement automatique 5 USD sous 5 USD : conforme (R-2788). |
| 2026-11-14T16:52:18Z | 4-5 | 33 offres ; la moins chère : **59572388**, 0,3747 USD/h, 24 cœurs, 64,3 Go (62,8 Gio), disque 1511,8 Go, CUDA 13.4, fiabilité 0,990, 776 Mb/s, New Jersey, vérifiée. `course/neuron-lens-volet-a-reduit-v10` = `799a8a32` ; `calcul/neuron-lens-volet-a-v1` absente. |
| 2026-11-14T16:52:39Z | 6 | Création (v14 telle quelle) ; `RUN_ID` 20261114-165239-neuron-lens-volet-a ; sortie : `{"success": true, "new_contract": 60671759}`, codes 0 0. **Instance 60671759.** |
| 2026-11-14T16:52:56Z | 6-7 | `dph_total` lu 0,3956 USD/h (stockage compris) > offre : **prix retenu 0,3956**. Minuterie v3 armée : durée 81883 s (90 % de 10 USD à 0,3956 USD/h), **PID 7134** (lu dans le fichier écrit par la minuterie ; `$!` différent), vivant et portant le script. |
| 2026-11-14T16:53:07Z | 8 | Garde v4 détachée : **PID 7178** (lu dans le fichier, après `exec`), vivante et portant `garde_depense_v4`, journal `journal-depense-volet-a-v1.jsonl`. |
| 2026-11-14T16:53:18Z | 9 | Rappel à 80 % (`trig_01PLQ22p…`, 2026-11-15T11:06:00Z) ; contrôle de suivi à 17:14Z (`trig_0147yKXD…`). |
| 2026-11-14T16:53:28Z | 10-11 | Instance « running » (« success, running python:3.12-bookworm ») ; journaux : `AMORCE … commit reduit verifie : 799a8a32… ; run_id=20261114-165239-neuron-lens-volet-a` (16:53:21Z), `pousse : commit verifie` (16:53:23Z) ; installation de l'environnement en cours. |
| 2026-11-14T16:54:32Z | mère | Lancement consigné en R-2795 ; **60670453 intouchable** (autre session), ajoutée à la liste (58936096, 58936099, 58936100, 60480302, 60599797, 60670453, `poste-temoin-bailey-*`) ; témoin d'absence : 60480302 ou 60670453. |
| 2026-11-14T17:14:43Z | 11 | Contrôle (réveil programmé) : instance « running » ; journaux : rien après `pousse : commit verifie` (16:53:23Z) — installation de l'environnement en cours (`pip -q` silencieux) ; état poussé « commit verifie », `exclus=0` ; relevé : `credit` 7,12 USD (rechargement automatique passé), `can_pay` vrai, `has_billing` vrai, `billing_failed` faux : consigne respectée. |
| 2026-11-14T17:14:57Z | incident | **Conteneur de la session redémarré à 17:14:27Z** (`uptime` 0 min ; fichiers conservés, processus tués) : minuterie PID 7134 et garde PID 7178 **mortes** depuis un moment inconnu entre 16:53 et 17:14 (limite déclarée de la v14). Journal de la minuterie : seule la ligne « armee » de 16:52:56Z. |
| 2026-11-14T17:15:13Z | 7 (reprise) | Minuterie v3 réarmée : durée restante 80548 s (même échéance absolue, comptée depuis 16:52:39Z), **PID 290**, vivante et portant le script. |
| 2026-11-14T17:15:15Z | 8 (reprise) | Garde v4 relancée : **PID 302**, vivante et portant `garde_depense_v4`. Veille en tâche de fond (contrôle des PID toutes les 5 min, 2 h au plus) pour garder la session active ; contrôle suivant programmé (~17:35Z). Mère prévenue. |
