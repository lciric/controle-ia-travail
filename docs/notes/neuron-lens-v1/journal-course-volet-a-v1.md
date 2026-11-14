# Journal de la course du volet A de « Neuron Lens » — v1 (commande v11, feu R-2782)

Session `session_016QhUrtahFZo57fZUcRReVA`, branche `prep/neuron-lens-v1`. Heures par `date -u`, dans la commande même.

| heure (UTC) | étape | fait |
|---|---|---|
| 2026-11-14T15:13:25Z | feu | Feu écrit de la mère lu (GO-2026-11-14-05, R-2782) ; vérifié à la source : `main` `b75f8c92`, ligne R-2782, note de vérification courte `a8224683…` (« conforme avec mineurs »). |
| avant 15:14 | M-1 | `garde_depense_v3.py` l.130, 137-143 : la garde écrit dans le fichier passé par `--journal` (ajout) ; l'étape 8 de la v11 passe `docs/notes/neuron-lens-v1/journal-depense-volet-a-v1.jsonl`, nom cité à l'étape 13 : conforme, rien à corriger. |
| 2026-11-14T15:14:04Z | 1 | `command -v vastai` = `/home/user/vastai-env/bin/vastai` ; `vastai show user --raw > /dev/null` : code 0. |
| 2026-11-14T15:14:14Z | 2 | Longueur du jeton ≥ 8 ; `suivi_vast_v4 verifier` : code 0 (« suivi prêt : liste de 4 instance(s) lue ») ; `suivi_vast_v4 instances` : code 0, 58936096, 58936099, 58936100 « exited », 60480302 « running » (témoin : 60480302). |
| 2026-11-14T15:14:23Z | 3 | **Crédit relevé : 6,68 USD (6.684615964066097) < 12 USD → ARRÊT** (commande v11, étape 3 ; feu R-2782). Aucune offre cherchée, aucune création, aucune dépense. Message à la mère. |
