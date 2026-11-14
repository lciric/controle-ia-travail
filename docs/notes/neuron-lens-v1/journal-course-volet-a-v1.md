# Journal de la course du volet A de « Neuron Lens » — v1 (commande v11, feu R-2782)

Session `session_016QhUrtahFZo57fZUcRReVA`, branche `prep/neuron-lens-v1`. Heures par `date -u`, dans la commande même.

| heure (UTC) | étape | fait |
|---|---|---|
| 2026-11-14T15:13:25Z | feu | Feu écrit de la mère lu (GO-2026-11-14-05, R-2782) ; vérifié à la source : `main` `b75f8c92`, ligne R-2782, note de vérification courte `a8224683…` (« conforme avec mineurs »). |
| avant 15:14 | M-1 | `garde_depense_v3.py` l.130, 137-143 : la garde écrit dans le fichier passé par `--journal` (ajout) ; l'étape 8 de la v11 passe `docs/notes/neuron-lens-v1/journal-depense-volet-a-v1.jsonl`, nom cité à l'étape 13 : conforme, rien à corriger. |
| 2026-11-14T15:14:04Z | 1 | `command -v vastai` = `/home/user/vastai-env/bin/vastai` ; `vastai show user --raw > /dev/null` : code 0. |
| 2026-11-14T15:14:14Z | 2 | Longueur du jeton ≥ 8 ; `suivi_vast_v4 verifier` : code 0 (« suivi prêt : liste de 4 instance(s) lue ») ; `suivi_vast_v4 instances` : code 0, 58936096, 58936099, 58936100 « exited », 60480302 « running » (témoin : 60480302). |
| 2026-11-14T15:14:23Z | 3 | **Crédit relevé : 6,68 USD (6.684615964066097) < 12 USD → ARRÊT** (commande v11, étape 3 ; feu R-2782). Aucune offre cherchée, aucune création, aucune dépense. Message à la mère. |
| 2026-11-14 (vers 16:27) | mot de Lazar | Verbatim, dans cette session : « vast se recharge seul go » (réponse à « c'est chez qui qu'il faut recharger ? ») : seuil de crédit de l'étape 3 levé (rechargement automatique) ; autres bornes du feu R-2782 inchangées ; mère prévenue avec le mot exact. |
| 2026-11-14T16:28:40Z | 1-2 | Outil `/home/user/vastai-env/bin/vastai`, `show user` code 0 ; jeton ≥ 8 ; `verifier` code 0 (4 instances, toutes d'autres sessions). |
| 2026-11-14T16:28:47Z | 3 | Crédit relevé : 5,11 USD (5.105585974066798), consigné sans seuil (mot de Lazar ; rechargement automatique). |
| 2026-11-14T16:28:58Z | 4 | 33 offres ; la moins chère : **54464717**, `dph_total` 0,4281 USD/h, 18 cœurs, 72 Go, disque 137,7 Go, CUDA 13.0, fiabilité 0,993, 894,7 Mb/s, Malaisie, vérifiée. |
| 2026-11-14T16:29:11Z | 5 | `course/neuron-lens-volet-a-reduit-v10` = `799a8a32` au distant ; `calcul/neuron-lens-volet-a-v1` absente. |
| 2026-11-14T16:29:29Z | 6 | Création sur l'offre 54464717 (commande v11 telle quelle ; `ISO_CREATION` 2026-11-14T16:29:29Z ; `RUN_ID` 20261114-162929-neuron-lens-volet-a). Sortie réduite : `{"success": false, "new_contract": 60669495}`, code 0. |
| 2026-11-14T16:29:37Z | 6 | `suivi_vast_v4 instance 60669495` : existe, `cur_state` et `intended_status` « stopped », `dph_total` 0,4489 USD/h ; la création a échoué (`success: false`) mais l'instance existe, à l'arrêt : cas « créée malgré tout » de l'étape 6 → arrêt, destruction par identifiant. Raison du refus non lue (sortie filtrée ; supposé : solde jugé insuffisant par le loueur pour démarrer). |
| 2026-11-14T16:29:55Z | arrêt | `vastai destroy instance 60669495` : code 0 ; mais `absente … --temoin 60480302` rend « PRÉSENTE » à 16:30:01 puis de 16:30:20 à 16:31:16 (6 relevés). |
| 2026-11-14T16:31:27Z | arrêt | Instance « loading », toujours « stopped » ; destruction relancée, sortie balayée puis lue : « Are you sure you want to destroy instance 60669495? … [y/N] » puis « Aborted. », **code 0**. **Défaut trouvé : l'outil 1.11.0 demande une confirmation, abandonne sans entrée et rend 0** (supposé jusqu'ici « aucune confirmation interactive », contre-lecture 11). |
| 2026-11-14T16:31:49Z | arrêt | `vastai destroy instance 60669495 -y` (option lue dans `--help`) : « destroying instance 60669495. », code 0. |
| 2026-11-14T16:31:56Z | arrêt | `absente 60669495 --temoin 60480302` : **absente**, liste de 4 lue sans erreur, témoin présent. Durée de vie ≈ 2 min 20 s (16:29:29 → 16:31:49), à l'arrêt ; coût borné par 0,4489 USD/h × 0,04 h ≈ 0,02 USD. |
| 2026-11-14T16:32:04Z | arrêt | Crédit 5,03 USD (5.029945674066539) ; la baisse depuis 16:28:47 (0,08 USD en 3 min 17 s) est surtout celle de 60480302 (1,17 USD/h). Minuterie et garde **jamais lancées** (étape 7 non atteinte) ; aucun PID. **Course arrêtée** : la minuterie v1 (l.29), la garde v3 (`_vast_detruire` l.119) et l'étape 13 appellent la destruction sans `-y` : toutes trois échoueraient sans bruit. Versions neuves, contre-lecture et nouveau feu exigés. |
