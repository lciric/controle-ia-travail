# Complément 1 à la pièce de contrôle de la mère — avant les étapes 3 à 6 — v2 (relance après coupure de l'essai 1)

Écrit par la session mère le 2026-11-21T08:38:40Z (`date -u`), sous un nom neuf (R12) ; la pièce de contrôle v1 (a7f0b33e…) et le complément 1 v1 (379fa29e…) restent intacts ; ce complément prime sur le complément 1 v1 pour le dossier des sorties. Décisions R-4336 et R-4337. Accord : GO-2026-11-21-09.

## Constat de l'essai 1

- Lancé le 2026-11-21 vers 06:35Z par un agent neuf de l'organisme, en tâche de fond de l'outil ; coupé à 08:35:09Z par la limite de durée de l'outil (7 200 000 ms), pendant l'étape 4 (couche mécanique, bras 1 à 3, lecteur réglé pour l'héritage). Aucune ligne de sortie, aucun code de sortie, aucun des quatre manifestes, ni « fréquences gelées » ni « réglages gelés ». Ce n'est pas un arrêt nommé du programme : c'est une panne de l'appelant.
- Dossier de l'essai 1 : /home/user/palier-0b-racine/diag/heritage-palier-0b-v1/etapes-3-a-6 (environ 1,9 Go). Il reste intact jusqu'à son inventaire par programme et son versement scellé sur la branche recuperation/palier-0b-programme-1-essai-1-v1 (règle « récupérer ce qui est récupérable ») ; aucun nettoyage avant. L'étape 3 y est complète (manifeste, étiquettes, rapport d'audit, compagnons) ; rien n'en est lu par la mère.
- Fichiers gelés reçus : aucun. Le programme 1 rejoue tout depuis l'étape 3 : les graines sont dérivées du texte et de la pièce d'autorisation, inchangées.

## Relance (essai 2)

- Programme à lancer : lancer_etapes_3_5_6_v2.py, au chemin /home/user/palier-0b-racine/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/programme-3-5-6-v2/lancer_etapes_3_5_6_v2.py.
commit du programme lancer_etapes_3_5_6_v2.py : 8262c442332c9b79c58eb49c651f788c5397a7ef
empreinte du programme lancer_etapes_3_5_6_v2.py : 1f04cb463c2fca7d2d67bfa3a8045bd4c9592e4e93bb564000ec102421cfdb14
dossier des sorties des étapes 3 à 6 : /home/user/palier-0b-racine/diag/heritage-palier-0b-v1/etapes-3-a-6-essai-2
- Seul le dossier des sorties change par rapport au complément 1 v1 ; il n'existe pas avant le lancement, comme le programme l'exige. Le chemin ne porte aucune espace.
- Commande (texte v19, programme 1), dossier courant celui du code v6, interpréteur du dépôt, lancée DÉTACHÉE de l'outil, sortie standard et sortie d'erreur dans un journal, identifiant de processus écrit dans un fichier et suivi par ce seul identifiant (R10) :

```
env -C /home/user/palier-0b-racine/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/code-v6 PYTHONPATH=src /home/user/controle-ia-travail/.venv/bin/python -B /home/user/palier-0b-racine/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/programme-3-5-6-v2/lancer_etapes_3_5_6_v2.py /home/user/palier-0b-racine/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/preenregistrement-heritage-palier-0b-etage-processeur-v19.md /home/user/palier-0b-racine /home/user/palier-0b-racine/docs/notes/organisme-courbe-dose-reponse-v1/code-organisme-94bfd92/orchestrator /home/user/palier-0b-racine/diag/heritage-palier-0b-v1/etapes-3-a-6-essai-2
```

- À rendre à la mère après le lancement : l'identifiant de processus et le chemin du journal ; à la fin, les quatre empreintes des manifestes, les lignes « fréquences gelées : » et « réglages gelés : », le code de sortie ; à un arrêt, la cause et l'inventaire du dossier (R11), sans aucun geste avant.
