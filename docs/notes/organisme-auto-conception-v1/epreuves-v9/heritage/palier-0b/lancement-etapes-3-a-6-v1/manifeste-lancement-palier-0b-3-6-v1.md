# Manifeste du lancement du palier 0b, étapes 3 à 6 (v1)

Agent du lancement du palier 0b, étapes 3 à 6. Programme sur processeur seulement, aucun appel de modèle, aucune dépense. GO-2026-11-21-09.

## Heures (UTC)
- Début de session (`date -u`) : Sat Nov 21 06:34:41 UTC 2026
- Lancement en tâche de fond : juste après les vérifications, vers 06:35 UTC
- Fin (`date -u` à la notification) : Sat Nov 21 08:35:09 UTC 2026
- Durée : environ 2 h 00 min, soit le délai accordé de 7 200 000 ms

## Vérifications du point 1
- `git -C /home/user/palier-0b-racine rev-parse HEAD` → `d7f949acd9ac92e998e57663d2cc741de93f18c3` : conforme.
- `git -C /home/user/palier-0b-racine status --porcelain` → sortie vide : conforme.
- `test -e /home/user/palier-0b-racine/diag/heritage-palier-0b-v1/etapes-3-a-6` → l'outil n'a affiché aucun code de sortie (ni 0, ni 1), deux fois. Contrôle sur disque (R11) : `stat` sur ce chemin → code 1, « No such file or directory ». Dossier absent : conforme.

## Commande exacte (lancée en tâche de fond, délai de 7 200 000 ms)
```
env -C /home/user/palier-0b-racine/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/code-v6 PYTHONPATH=src /home/user/controle-ia-travail/.venv/bin/python -B /home/user/palier-0b-racine/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/programme-3-5-6-v2/lancer_etapes_3_5_6_v2.py /home/user/palier-0b-racine/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/preenregistrement-heritage-palier-0b-etage-processeur-v19.md /home/user/palier-0b-racine /home/user/palier-0b-racine/docs/notes/organisme-courbe-dose-reponse-v1/code-organisme-94bfd92/orchestrator /home/user/palier-0b-racine/diag/heritage-palier-0b-v1/etapes-3-a-6 > /tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/lancement-palier-0b-3-6/sortie-standard.txt 2> /tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/lancement-palier-0b-3-6/sortie-erreur.txt
```

## Code de sortie
Aucun code de sortie rendu. La notification indique l'état « killed » : l'outil a arrêté la commande quand elle a atteint son délai de tâche de fond (7 200 000 ms, le maximum permis). Le programme n'a pas fini de lui-même. Il n'a pas été relancé.
Je n'ai pas vérifié qu'aucun processus du programme ne tourne encore : la consigne interdit les commandes de recherche de processus.

## Cause
Aucune cause imprimée par le programme : les deux fichiers de sortie sont vides (0 octet).
- sortie-standard.txt : e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 (empreinte d'un fichier vide)
- sortie-erreur.txt : e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 (empreinte d'un fichier vide)
Cause constatée : arrêt par la limite de durée de l'outil, en cours d'exécution, sans aucune sortie émise.

## Inventaire du dossier de sortie (R11)
`find /home/user/palier-0b-racine/diag/heritage-palier-0b-v1/etapes-3-a-6 -type f` : le dossier existe et contient un très grand nombre de fichiers. La liste dépasse 64 Mo de chemins. L'outil n'a gardé que les 64 premiers Mo, dans un fichier sous `/root/.claude/`, que la consigne m'interdit de lire. Je n'ai donc ni le nombre de fichiers ni la liste complète.
Les premiers chemins vus montrent que le programme était à l'étape 4 au moins, couche mécanique, sous `etape-4/couche-mecanique/bras-1-a-3/sourd-paie/0.25/3/` : fichiers `bras-2/registre.jsonl`, `bras-2/registre.jsonl.sceaux`, `mondes/s3-finale/servi/D00.csv` à `D15.csv`, etc. Ces chemins sont listés dans l'ordre de `find`, pas dans l'ordre d'écriture. Ils ne disent donc pas jusqu'où le programme est allé.
Une empreinte par fichier, un appel par fichier, n'est pas faisable à cette échelle et n'a pas été faite. Aucun autre geste n'a été fait sur ce dossier : rien de supprimé, rien de déplacé.

## Lignes relevées
Aucune : ni les lignes « étape N : manifeste », ni « fréquences gelées : », ni « réglages gelés : ». La sortie standard est vide.
