# Sauvegarde de l'autonomie du 31 octobre 2026 (13:15 UTC) — session-depot, instance 2

Copie mécanique, pour reprise si le conteneur est perdu (consigne de Lazar, 13:12 UTC : « passation maintenant pour reprendre exactement au même point »).
`donnees/` est ignoré par git sur `main` ; les sorties d'Argon seul sont hors dépôt ; les outils étaient dans le dossier temporaire.

- `donnees/collisionneur-noeuds-v1/` : run v10 arrêté (question périmée, n° 293), scripts v1 à v3, journaux.
- `donnees/collisionneur-dml1-v1/` : run D-ML-1 **en cours au moment de la copie** (tour 3), état partiel.
- `donnees/collisionneur-protocelles-v1/` : tour 2 arrêté à 13:12 UTC (erreur de la synthèse du tour 1, n° 299).
- `argon-seul/` : réponses d'Argon seul A, B, C (et questions envoyées, avec empreintes).
- `outils/` : surveillance du canal (`surveiller-canal-v1.sh`), assembleur des faits des nœuds v1 et balayage.

Empreintes de chaque fichier : `EMPREINTES-sauvegarde.txt`. Recherche de fuite des trois clés faite avant le commit : aucune occurrence.
Pour reprendre un run : recopier son dossier sous `donnees/` sur `main`, puis lancer un script « suite » neuf (R12) ; le collisionneur saute les cellules valides.
