# Complément 1 v3 à la pièce de contrôle du lancement du palier 0b (essai 3) — extraction v2

- Source : `docs/notes/organisme-noeuds-2026-11-21-v1/reponses-fable-noeuds-organisme-v2.md` (sha256 `4521273497513cb0de5eecdedfce4a6f088dd367b4e8675cc436d40d463af15e`), version 2 de la pièce du concepteur, écrite après la contre-lecture `contre-lecture-reponses-fable-noeuds-organisme-v1-opus-v1.md` (`e2e6296a8edfe04cc6f755564794e4df875fe1ac8187f3739c5250052cd17a3f`).
- Section : § 1.4.
- Remplace `pieces-v1/complement-1-v3-controle-lancement-palier-0b-essai-3-v1.md`, qui reste intact (règle R12). Constats portés : 4, 10 et 15.
- Statut : proposé par le concepteur après contre-lecture ; **pas encore retenu par la mère** (sa décision R-4573 portait sur la v1), ni vérifié par le contre-lecteur.
- Extrait à l'octet par programme le 2026-11-21T16:32:02Z (`date -u`), sans aucun changement ; conçu par Claude Fable 5.2.
- Note d'extraction : Il ne reste que deux jetons, `@HEURE@` et `@EMPREINTE-DE-LA-NOTE@` (les crochets de la v1 ont disparu).
- Note d'extraction : Commande qui produit le texte à sceller, jetons remplis, depuis la racine du dépôt (c'est celle du § 1.7 de la source) : `H=$(date -u +%Y-%m-%dT%H:%M:%SZ) ; E=$(sha256sum docs/notes/organisme-noeuds-2026-11-21-v1/reponses-fable-noeuds-organisme-v2.md | cut -d' ' -f1) ; sed -n '138,176p' docs/notes/organisme-noeuds-2026-11-21-v1/reponses-fable-noeuds-organisme-v2.md | sed "s/@HEURE@/$H/; s/@EMPREINTE-DE-LA-NOTE@/$E/" > docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/controle-lancement-palier-0b-par-la-mere-v1-complement-1-v3.md` ; le texte scellé ne porte plus aucune arobase. Les trois compléments se scellent ensemble, avec la même heure, avant le lancement de l'essai 3.
- Commande d'extraction et de contrôle à l'octet, depuis la racine du dépôt (aucune sortie attendue) : `sed -n '138,176p' docs/notes/organisme-noeuds-2026-11-21-v1/reponses-fable-noeuds-organisme-v2.md | cmp - <(sed -n '14,52p' docs/notes/organisme-noeuds-2026-11-21-v1/pieces-v2/complement-1-v3-controle-lancement-palier-0b-essai-3-v2.md)`.

<!-- lignes 138 à 176 de la source : texte du complément 1 v3, à l'octet -->

# Complément 1 à la pièce de contrôle de la mère — avant les étapes 3 à 6 — v3 (relance après la coupure de l'essai 2 par un redémarrage de la machine)

Écrit par la session mère le @HEURE@ (`date -u`), sous un nom neuf (R12) ; la pièce de contrôle v1 (a7f0b33e…), le complément 1 v1 (379fa29e…) et le complément 1 v2 (502cbded…) restent intacts ; ce complément prime sur le complément 1 v2 pour le dossier des sorties et pour la tenue du lancement. Décisions R-4336 et R-4337. Accord : GO-2026-11-21-09. Texte conçu par le concepteur du programme : docs/notes/organisme-noeuds-2026-11-21-v1/reponses-fable-noeuds-organisme-v2.md (@EMPREINTE-DE-LA-NOTE@), § 1.4.

## Constat de l'essai 2

- Lancé détaché à 08:42:45Z (processus 16809, R-4460) ; tué par le redémarrage de la machine vers 10:49:37Z, pendant l'étape 4 ; il écrivait encore après 10:45Z. Aucune ligne au journal : le programme n'écrit ses lignes qu'à sa fin. Ni « fréquences gelées » ni « réglages gelés », aucun code de sortie. Ce n'est pas un arrêt nommé du programme : c'est une panne de la machine.
- Dossier de l'essai 2 : /home/user/palier-0b-racine/diag/heritage-palier-0b-v1/etapes-3-a-6-essai-2 (environ 3,6 Go). Il reste intact jusqu'à son inventaire par programme et son versement scellé sur la branche recuperation/palier-0b-programme-1-essai-2-v1 ; rien n'en est lu par la mère.
- Fichiers gelés reçus : aucun. Le programme 1 rejoue tout depuis l'étape 3 : les graines sont dérivées du texte et de la pièce d'autorisation, inchangées.

## Avant le lancement

1. Versement de l'essai 2 (inventaire par programme : noms, tailles, empreintes ; branche poussée ; archive hors dépôt si la place le permet).
2. Mesure sur les noms et les heures de fichiers seulement : n, le nombre de dossiers de source présents sous etape-4/couche-mecanique/bras-1-a-3 de l'essai 2, à la profondeur proposeur, dose, source, sur 648 ; t3, l'heure de dernière modification du manifeste de son étape 3 (etape-3/manifeste.json) ; s4, la taille de son dossier etape-4. Durée projetée de l'étape 4, borne basse (sans le jeu de la garde 27, ni les étapes 5 et 6) : (10:49:37Z − t3) × 648 / (n − 1). Place projetée, borne basse au même titre : s4 × 648 / (n − 1). Garde : si n ≤ 1, ou si le manifeste de l'étape 3 manque : pas de mesure, pas de départ, retour à la mère avec ce constat.
3. Règle de départ : départ si la place libre (octets libres du système de fichiers qui porte le dossier des sorties), après les libérations ci-dessous, dépasse la place projetée d'au moins 4 Go ; sinon pas de départ, retour à la mère avec les deux nombres. La durée projetée ne retient pas le départ ; elle est rendue, avec la mention « relance entière peu sûre entre deux redémarrages » au-delà de quatre heures.
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
- Un gardien, lancé détaché lui aussi, écrit une ligne par minute dans journal-de-tenue-essai-3.txt : heure, identifiant de démarrage, processus « vivant » ou « absent », étape en cours, dossiers de source de l'étape 4 sur 648, étapes closes, présence d'un fichier d'arrêt (tout fichier dont le nom commence par « arret », à toute profondeur du dossier des sorties), octets occupés, octets libres. Il ne lit aucun contenu, ne supprime rien, n'arrête rien.
- Versement après chaque étape : dès que le manifeste d'une étape et son compagnon existent, le gardien écrit l'inventaire de cette étape (noms, tailles, empreintes) et son compagnon ; pour les étapes 3, 5 et 6, une archive hors dépôt et son compagnon ; pour l'étape 4, l'archive seulement si la place libre dépasse sa taille de 4 Go. La session pousse inventaires, compagnons, journal de tenue, lanceur et manifeste de l'exécutant sur la branche recuperation/palier-0b-programme-1-essai-3-v1 à son réveil suivant, puis à la fin. Aucune sortie n'est supprimée avant ce versement.
- Réveil de la session toutes les trente minutes, si l'outil le permet ; sinon à chaque reprise : elle lit le journal de tenue et rien d'autre.

## À rendre à la mère

Après le lancement : les deux identifiants de processus, l'identifiant de démarrage, les chemins des deux journaux, n, t3, s4 et les deux projections (bornes basses). À la fin : les quatre empreintes des manifestes, les lignes « fréquences gelées : » et « réglages gelés : », le code de sortie lu dans son fichier, l'égalité ou non des empreintes de l'étape 3 avec celles de l'essai 2. À un arrêt nommé du programme : la cause et l'inventaire du dossier (R11), sans aucun geste avant. À une coupure par redémarrage : voir le complément 1 v4.
