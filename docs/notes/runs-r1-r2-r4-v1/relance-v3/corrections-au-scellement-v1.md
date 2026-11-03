# Addendum v3 de relance de R1 — retouches de session-depot au scellement, v1

Écrit le 3 novembre 2026 à 00:31 UTC (heure relevée par `date -u`). Brouillon 3 relu avant ces retouches :
`dcf51d015f4a195c7479b7ae504c06c2cb1154133a0e67759409eafdbb95e3d6` (commit `6de29976`). Texte seul ; code, scripts, essais,
configuration v5 et table v3 inchangés.

| Endroit | Retouche | Raison |
|---|---|---|
| « Liste d'arrêt », ligne « Récupération » | Ajout : session-depot apprend le scellement de la fiche de réception par un message de conv-audit au canal qui donne son chemin et son empreinte, vérifiée (compagnon `.sha256` égal) ; sans ce message, rien n'est récupéré. | Réserve du rédacteur sur C-1 de la concordance (`8482b4cd…`) : le texte ne disait pas comment session-depot l'apprend. |
| « Contre-lecture », « Traitement final par session-depot » | Marqueur « À REMPLIR » remplacé par le traitement final (relecture des différences des brouillons 2 et 3, empreinte du brouillon 3 relu, deux ajouts, aucun refus). | Exigé par le gabarit au scellement. |

`problemes()` après ces retouches : `[]`.
