# Complément 1 v3 à la pièce de contrôle du lancement du palier 0b (essai 3) — extraction v1

- Source : `docs/notes/organisme-noeuds-2026-11-21-v1/reponses-fable-noeuds-organisme-v1.md` (sha256 `dd4e1ccc53dbe142a4a64ae054114dd17feec20f07eb9d050d9de714ac3ed587`), sur main.
- Section : § 1.4 (texte du complément 1 v3, à sceller par la mère).
- Retenu par la mère, décision de routine, R-4573.
- Extrait à l'octet par programme le 2026-11-21T14:48:35Z (`date -u`), sans aucun changement ; conçu par Claude Fable 5.2.
- Note d'extraction : Les crochets sont laissés tels que la pièce les donne (« Les crochets sont à remplir par la mère », § 1.4) : l'heure d'écriture de cette extraction est celle ci-dessus, l'empreinte de la pièce est celle ci-dessus.

<!-- lignes 87 à 125 de la source : texte du complément 1 v3, à l'octet -->

# Complément 1 à la pièce de contrôle de la mère — avant les étapes 3 à 6 — v3 (relance après la coupure de l'essai 2 par un redémarrage de la machine)

Écrit par la session mère le [heure relevée par `date -u`], sous un nom neuf (R12) ; la pièce de contrôle v1 (a7f0b33e…), le complément 1 v1 (379fa29e…) et le complément 1 v2 (502cbded…) restent intacts ; ce complément prime sur le complément 1 v2 pour le dossier des sorties et pour la tenue du lancement. Décisions R-4336 et R-4337. Accord : GO-2026-11-21-09. Texte conçu par le concepteur du programme : docs/notes/organisme-noeuds-2026-11-21-v1/reponses-fable-noeuds-organisme-v1.md ([empreinte]), § 1.

## Constat de l'essai 2

- Lancé détaché à 08:42:45Z (processus 16809, R-4460) ; tué par le redémarrage de la machine vers 10:49:37Z, pendant l'étape 4 ; il écrivait encore après 10:45Z. Aucune ligne au journal : le programme n'écrit ses lignes qu'à sa fin. Ni « fréquences gelées » ni « réglages gelés », aucun code de sortie. Ce n'est pas un arrêt nommé du programme : c'est une panne de la machine.
- Dossier de l'essai 2 : /home/user/palier-0b-racine/diag/heritage-palier-0b-v1/etapes-3-a-6-essai-2 (environ 3,6 Go). Il reste intact jusqu'à son inventaire par programme et son versement scellé sur la branche recuperation/palier-0b-programme-1-essai-2-v1 ; rien n'en est lu par la mère.
- Fichiers gelés reçus : aucun. Le programme 1 rejoue tout depuis l'étape 3 : les graines sont dérivées du texte et de la pièce d'autorisation, inchangées.

## Avant le lancement

1. Versement de l'essai 2 (inventaire par programme : noms, tailles, empreintes ; branche poussée ; archive hors dépôt si la place le permet).
2. Mesure sur les noms et les heures de fichiers seulement : n, le nombre de dossiers de source présents sous etape-4/couche-mecanique/bras-1-a-3 de l'essai 2, à la profondeur proposeur, dose, source, sur 648 ; t3, l'heure de dernière modification du manifeste de son étape 3 ; s4, la taille de son dossier etape-4. Durée projetée de l'étape 4 : (10:49:37Z − t3) × 648 / (n − 1). Place projetée : s4 × 648 / (n − 1).
3. Règle de départ : départ si la place libre, après les libérations ci-dessous, dépasse la place projetée d'au moins 4 Go ; sinon pas de départ, retour à la mère avec les deux nombres. La durée projetée ne retient pas le départ ; elle est rendue.
4. Libérations permises, dans cet ordre, chacune par un chemin écrit en toutes lettres, après vérification, consignée (R-4461, R-4463) : les caches ; le dossier de l'essai 1, branche de récupération poussée (cda576e5) et compagnon de l'archive revérifié ; le dossier de l'essai 2, après son versement, aux mêmes conditions ; l'arbre de travail arbre-prep-sorties, par git worktree remove, têtes revérifiées. L'archivage cède, jamais l'essai.

## Relance (essai 3)

- Programme à lancer : lancer_etapes_3_5_6_v2.py, au chemin /home/user/palier-0b-racine/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/programme-3-5-6-v2/lancer_etapes_3_5_6_v2.py.
commit du programme lancer_etapes_3_5_6_v2.py : 8262c442332c9b79c58eb49c651f788c5397a7ef
empreinte du programme lancer_etapes_3_5_6_v2.py : 1f04cb463c2fca7d2d67bfa3a8045bd4c9592e4e93bb564000ec102421cfdb14
dossier des sorties des étapes 3 à 6 : /home/user/palier-0b-racine/diag/heritage-palier-0b-v1/etapes-3-a-6-essai-3
- Seul le dossier des sorties change par rapport au complément 1 v2 ; il n'existe pas avant le lancement. La racine de l'arbre lancé ne bouge pas : ce complément se lit sur origin/main par git show redirigé.
- Commande (texte v19, programme 1), dossier courant celui du code v6, interpréteur du dépôt :

env -C /home/user/palier-0b-racine/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/code-v6 PYTHONPATH=src /home/user/controle-ia-travail/.venv/bin/python -B /home/user/palier-0b-racine/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/programme-3-5-6-v2/lancer_etapes_3_5_6_v2.py /home/user/palier-0b-racine/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/preenregistrement-heritage-palier-0b-etage-processeur-v19.md /home/user/palier-0b-racine /home/user/palier-0b-racine/docs/notes/organisme-courbe-dose-reponse-v1/code-organisme-94bfd92/orchestrator /home/user/palier-0b-racine/diag/heritage-palier-0b-v1/etapes-3-a-6-essai-3

## Tenue du lancement

- Dossier de tenue, hors dépôt et hors de tout dossier temporaire : /home/user/journaux-palier-0b-essai-3-v1/.
- Le lanceur est un fichier de ce dossier qui porte la commande ci-dessus, à l'octet, puis une ligne qui écrit son code de sortie dans code-de-sortie.txt. Il est lancé DÉTACHÉ de l'outil (setsid nohup), sortie standard et sortie d'erreur dans journal-essai-3.txt, entrée fermée. L'identifiant du processus, l'identifiant de démarrage de la machine (/proc/sys/kernel/random/boot_id) et l'heure du lancement sont écrits chacun dans un fichier ; le suivi se fait par ce seul identifiant (R10).
- Un gardien, lancé détaché lui aussi, écrit une ligne par minute dans journal-de-tenue-essai-3.txt : heure, identifiant de démarrage, processus vivant ou absent, étape en cours, dossiers de source de l'étape 4 sur 648, étapes closes, présence d'un fichier d'arrêt, octets occupés, octets libres. Il ne lit aucun contenu, ne supprime rien, n'arrête rien.
- Versement après chaque étape : dès que le manifeste d'une étape et son compagnon existent, le gardien écrit l'inventaire de cette étape (noms, tailles, empreintes) et son compagnon ; pour les étapes 3, 5 et 6, une archive hors dépôt et son compagnon ; pour l'étape 4, l'archive seulement si la place libre dépasse sa taille de 4 Go. La session pousse inventaires, compagnons, journal de tenue, lanceur et manifeste de l'exécutant sur la branche recuperation/palier-0b-programme-1-essai-3-v1 à son réveil suivant, puis à la fin. Aucune sortie n'est supprimée avant ce versement.
- Réveil de la session toutes les trente minutes, si l'outil le permet ; sinon à chaque reprise : elle lit le journal de tenue et rien d'autre.

## À rendre à la mère

Après le lancement : les deux identifiants de processus, l'identifiant de démarrage, les chemins des deux journaux, n, t3, s4 et les deux projections. À la fin : les quatre empreintes des manifestes, les lignes « fréquences gelées : » et « réglages gelés : », le code de sortie lu dans son fichier, l'égalité ou non des empreintes de l'étape 3 avec celles de l'essai 2. À un arrêt nommé du programme : la cause et l'inventaire du dossier (R11), sans aucun geste avant. À une coupure par redémarrage : voir le complément 1 v4.
