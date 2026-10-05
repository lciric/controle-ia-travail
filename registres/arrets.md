# Registre des arrêts

Processus et instances arrêtés par PID ou identifiant d'instance (R10) ; inventaire à chaque reprise et à chaque passation.

| date (UTC) | cible (PID ou identifiant) | raison | vérification après arrêt |
|---|---|---|---|
| 2026-10-04 03:30 | chaîne de sous-agents wrnktum5z (vérification des références) | budget de recherche web épuisé : poursuivre produirait des verdicts creux | arrêt confirmé par l'outil ; journal conservé |
| 2026-10-04 03:30 | chaîne de sous-agents wr6v7w6d4 (zones papier A et transverses) | idem | arrêt confirmé ; journal conservé |
| 2026-10-04 03:30 | chaîne de sous-agents wk1qdwe5t (zones papiers C et B) | idem | arrêt confirmé ; journal conservé |
| 2026-10-04 18:12 | instance Vast.ai **54183350** (validation de T0.4, H100 SXM ; `vastai stop instance 54183350`) | l'amorce échoue avant le clonage : GitHub refuse le jeton de l'instance (403, « Write access to repository not granted ») ; le conteneur relance l'amorce à chaque sortie (43 tentatives de 18:03:59 à 18:11:57) | état « exited », « stopped » à 18:14 ; journal archivé et scellé : `traces/t04-instance-54183350-20261004-181301/` ; non détruite : destruction soumise à Lazar (irréversible ; aucune donnée sur le disque) |
| 2026-10-05 08:31 | instance Vast.ai **54285455** (relancement de la validation de T0.4, A100 SXM4 ; `vastai stop instance 54285455`) | même échec avant le clonage : GitHub refuse toujours le jeton de l'instance (403, « Write access to repository not granted ») ; 10 tentatives de 08:29:31 à 08:31:17 ; la surveillance scellée a rendu la main sur « ÉCHEC D'AMORCE » | état « exited », « stopped » à 08:32 ; journal archivé et scellé : `traces/t04-instance-54285455-20261005-083202/` ; non détruite (sans données ; destruction soumise à Lazar, N-009) |

Instances de calcul : 54183350 (créée le 2026-10-04, arrêtée à 18:12 UTC) et 54285455 (créée le 2026-10-05, arrêtée à 08:31 UTC), toutes deux par leur identifiant ; aucune autre.
