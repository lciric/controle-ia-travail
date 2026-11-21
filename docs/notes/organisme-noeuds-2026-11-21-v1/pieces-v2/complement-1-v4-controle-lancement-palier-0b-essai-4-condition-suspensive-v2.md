# Complément 1 v4 à la pièce de contrôle du lancement du palier 0b (essai 4, à condition suspensive) — extraction v2

- Source : `docs/notes/organisme-noeuds-2026-11-21-v1/reponses-fable-noeuds-organisme-v2.md` (sha256 `4521273497513cb0de5eecdedfce4a6f088dd367b4e8675cc436d40d463af15e`), version 2 de la pièce du concepteur, écrite après la contre-lecture `contre-lecture-reponses-fable-noeuds-organisme-v1-opus-v1.md` (`e2e6296a8edfe04cc6f755564794e4df875fe1ac8187f3739c5250052cd17a3f`).
- Section : § 1.5.
- Remplace `pieces-v1/complement-1-v4-controle-lancement-palier-0b-essai-4-condition-suspensive-v1.md`, qui reste intact (règle R12). Constats portés : 3, 4 et 10.
- Statut : proposé par le concepteur après contre-lecture ; **pas encore retenu par la mère** (sa décision R-4573 portait sur la v1), ni vérifié par le contre-lecteur.
- Extrait à l'octet par programme le 2026-11-21T16:32:02Z (`date -u`), sans aucun changement ; conçu par Claude Fable 5.2.
- Note d'extraction : Texte assemblé, entier : la v1 ne donnait qu'une règle de dérivation. Il déclare un écart à la décision R-4337, qui est une décision de la mère : à elle de le recevoir.
- Note d'extraction : Commande qui produit le texte à sceller, jetons remplis, depuis la racine du dépôt (c'est celle du § 1.7 de la source) : `H=$(date -u +%Y-%m-%dT%H:%M:%SZ) ; E=$(sha256sum docs/notes/organisme-noeuds-2026-11-21-v1/reponses-fable-noeuds-organisme-v2.md | cut -d' ' -f1) ; sed -n '188,235p' docs/notes/organisme-noeuds-2026-11-21-v1/reponses-fable-noeuds-organisme-v2.md | sed "s/@HEURE@/$H/; s/@EMPREINTE-DE-LA-NOTE@/$E/" > docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/controle-lancement-palier-0b-par-la-mere-v1-complement-1-v4.md` ; le texte scellé ne porte plus aucune arobase. Les trois compléments se scellent ensemble, avec la même heure, avant le lancement de l'essai 3.
- Commande d'extraction et de contrôle à l'octet, depuis la racine du dépôt (aucune sortie attendue) : `sed -n '188,235p' docs/notes/organisme-noeuds-2026-11-21-v1/reponses-fable-noeuds-organisme-v2.md | cmp - <(sed -n '14,61p' docs/notes/organisme-noeuds-2026-11-21-v1/pieces-v2/complement-1-v4-controle-lancement-palier-0b-essai-4-condition-suspensive-v2.md)`.

<!-- lignes 188 à 235 de la source : texte entier du complément 1 v4, à l'octet -->

# Complément 1 à la pièce de contrôle de la mère — avant les étapes 3 à 6 — v4 (relance après une coupure de l'essai 3 par un redémarrage de la machine ; scellé d'avance, à condition suspensive)

Écrit par la session mère le @HEURE@ (`date -u`), avant le lancement de l'essai 3, sous un nom neuf (R12) ; la pièce de contrôle v1 (a7f0b33e…) et les compléments 1 v1 (379fa29e…), 1 v2 (502cbded…) et 1 v3 restent intacts ; si sa condition de validité est tenue, ce complément prime sur le complément 1 v3 pour le dossier des sorties et pour la tenue du lancement de l'essai 4. Décisions R-4336 et R-4337, avec l'écart déclaré plus bas. Accord : GO-2026-11-21-09. Texte conçu par le concepteur du programme : docs/notes/organisme-noeuds-2026-11-21-v1/reponses-fable-noeuds-organisme-v2.md (@EMPREINTE-DE-LA-NOTE@), § 1.5.

## Condition de validité de ce complément

Ce complément est scellé d'avance. Il ne vaut que si l'essai 3 a été coupé par un redémarrage de la machine, et l'organisme le constate par écrit, avant la relance, dans la pièce /home/user/journaux-palier-0b-essai-3-v1/constat-coupure-palier-0b-essai-3-v1.md, scellée (compagnon .sha256) et poussée sur la branche recuperation/palier-0b-programme-1-essai-3-v1, sur ces cinq points :
1. l'identifiant de démarrage de la machine diffère de celui écrit au lancement de l'essai 3 ;
2. le fichier /home/user/journaux-palier-0b-essai-3-v1/code-de-sortie.txt n'existe pas ;
3. aucun fichier dont le nom commence par « arret » n'existe, à aucune profondeur du dossier /home/user/palier-0b-racine/diag/heritage-palier-0b-v1/etapes-3-a-6-essai-3, et le journal /home/user/journaux-palier-0b-essai-3-v1/journal-essai-3.txt ne porte aucune trace d'exception (aucune ligne qui commence par « Traceback ») ;
4. le dossier de l'essai 3 est inventorié (noms, tailles, empreintes), l'inventaire est poussé sur la même branche de récupération, et le dossier reste intact, sauf libération permise au point 4 de la section « Avant le lancement » ;
5. la règle de départ de la section « Avant le lancement » (place projetée plus 4 Go) est tenue.
Si un seul point manque (processus absent sans redémarrage, code de sortie écrit, fichier d'arrêt, trace d'exception au journal, place insuffisante, aucune projection) : aucune relance ; inventaire, et retour à la mère. Après l'essai 5, aucune relance sans un mot neuf : trois coupures de suite sont un nœud.
Aucune de ces conditions ne lit une sortie du palier.

## Écart déclaré à la décision R-4337 (décision de la mère)

La décision R-4337 veut qu'un complément, écrit et scellé avant un lancement, porte le constat de fin du lancement précédent. Ce complément est scellé avant que l'essai 3 ait couru : il ne peut pas porter ce constat. Le constat de la coupure de l'essai 3 est écrit et scellé par l'organisme, sur les cinq points ci-dessus, avant la relance ; la mère le reprend, avec tous les essais, dans le complément qu'elle écrit après le dernier essai, et au registre. Motif : les envois de l'organisme vers la mère passent par un relais, et attendre son mot à chaque coupure coûte des heures. Le texte v19 (l. 466) demande un complément par lancement, écrit et scellé avant lui : c'est tenu.

## Avant le lancement

1. Versement de l'essai 3 (inventaire par programme : noms, tailles, empreintes ; branche recuperation/palier-0b-programme-1-essai-3-v1 poussée ; archive hors dépôt si la place le permet).
2. Mesure sur les noms et les heures de fichiers seulement, sur l'essai 3 : n, le nombre de dossiers de source présents sous etape-4/couche-mecanique/bras-1-a-3, à la profondeur proposeur, dose, source, sur 648 ; t3, l'heure de dernière modification de etape-3/manifeste.json ; s4, la taille du dossier etape-4 ; t_fin, l'heure de la dernière ligne « vivant » du journal /home/user/journaux-palier-0b-essai-3-v1/journal-de-tenue-essai-3.txt. Durée projetée de l'étape 4, borne basse (sans le jeu de la garde 27, ni les étapes 5 et 6) : (t_fin − t3) × 648 / (n − 1). Place projetée, borne basse au même titre : s4 × 648 / (n − 1). Si n ≤ 1, ou si le manifeste de l'étape 3 manque, l'essai 3 ne donne aucune projection. La projection retenue est celle de l'essai coupé qui a le plus grand n, parmi les essais 2 à 3, les nombres des essais précédents étant relus au manifeste de l'exécutant. Garde : si aucun de ces essais ne donne de projection : pas de départ, retour à la mère avec ce constat.
3. Règle de départ : départ si la place libre (octets libres du système de fichiers qui porte le dossier des sorties), après les libérations ci-dessous, dépasse la place projetée retenue d'au moins 4 Go ; sinon pas de départ, retour à la mère avec les deux nombres. La durée projetée ne retient pas le départ ; elle est rendue, avec la mention « relance entière peu sûre entre deux redémarrages » au-delà de quatre heures.
4. Libérations permises, dans cet ordre, chacune par un chemin écrit en toutes lettres, après vérification, consignée (R-4461, R-4463) : les caches ; le dossier de l'essai 1, branche de récupération poussée (cda576e5) et compagnon de l'archive revérifié ; les dossiers des essais 2 et 3, chacun après son versement, aux mêmes conditions ; l'arbre de travail arbre-prep-sorties, par git worktree remove, têtes revérifiées. L'archivage cède, jamais l'essai.

## Relance (essai 4)

- Programme à lancer : lancer_etapes_3_5_6_v2.py, au chemin /home/user/palier-0b-racine/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/programme-3-5-6-v2/lancer_etapes_3_5_6_v2.py.
commit du programme lancer_etapes_3_5_6_v2.py : 8262c442332c9b79c58eb49c651f788c5397a7ef
empreinte du programme lancer_etapes_3_5_6_v2.py : 1f04cb463c2fca7d2d67bfa3a8045bd4c9592e4e93bb564000ec102421cfdb14
dossier des sorties des étapes 3 à 6 : /home/user/palier-0b-racine/diag/heritage-palier-0b-v1/etapes-3-a-6-essai-4
- Seul le dossier des sorties change par rapport au complément 1 v3 ; il n'existe pas avant le lancement. La racine de l'arbre lancé ne bouge pas : ce complément se lit sur origin/main par git show redirigé.
- Commande (texte v19, programme 1), dossier courant celui du code v6, interpréteur du dépôt :

env -C /home/user/palier-0b-racine/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/code-v6 PYTHONPATH=src /home/user/controle-ia-travail/.venv/bin/python -B /home/user/palier-0b-racine/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/programme-3-5-6-v2/lancer_etapes_3_5_6_v2.py /home/user/palier-0b-racine/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/preenregistrement-heritage-palier-0b-etage-processeur-v19.md /home/user/palier-0b-racine /home/user/palier-0b-racine/docs/notes/organisme-courbe-dose-reponse-v1/code-organisme-94bfd92/orchestrator /home/user/palier-0b-racine/diag/heritage-palier-0b-v1/etapes-3-a-6-essai-4

## Tenue du lancement

- Dossier de tenue, hors dépôt et hors de tout dossier temporaire : /home/user/journaux-palier-0b-essai-4-v1/.
- Le lanceur est un fichier de ce dossier qui porte la commande ci-dessus, à l'octet, puis une ligne qui écrit son code de sortie dans code-de-sortie.txt. Il est lancé DÉTACHÉ de l'outil (setsid nohup), sortie standard et sortie d'erreur dans journal-essai-4.txt, entrée fermée. L'identifiant du processus, l'identifiant de démarrage de la machine (/proc/sys/kernel/random/boot_id) et l'heure du lancement sont écrits chacun dans un fichier ; le suivi se fait par ce seul identifiant (R10).
- Un gardien, lancé détaché lui aussi, écrit une ligne par minute dans journal-de-tenue-essai-4.txt : heure, identifiant de démarrage, processus « vivant » ou « absent », étape en cours, dossiers de source de l'étape 4 sur 648, étapes closes, présence d'un fichier d'arrêt (tout fichier dont le nom commence par « arret », à toute profondeur du dossier des sorties), octets occupés, octets libres. Il ne lit aucun contenu, ne supprime rien, n'arrête rien.
- Versement après chaque étape : dès que le manifeste d'une étape et son compagnon existent, le gardien écrit l'inventaire de cette étape (noms, tailles, empreintes) et son compagnon ; pour les étapes 3, 5 et 6, une archive hors dépôt et son compagnon ; pour l'étape 4, l'archive seulement si la place libre dépasse sa taille de 4 Go. La session pousse inventaires, compagnons, journal de tenue, lanceur et manifeste de l'exécutant sur la branche recuperation/palier-0b-programme-1-essai-4-v1 à son réveil suivant, puis à la fin. Aucune sortie n'est supprimée avant ce versement.
- Réveil de la session toutes les trente minutes, si l'outil le permet ; sinon à chaque reprise : elle lit le journal de tenue et rien d'autre.

## À rendre à la mère

Avant la relance, par le canal : le chemin et l'empreinte du constat de la coupure de l'essai 3. Après le lancement : les deux identifiants de processus, l'identifiant de démarrage, les chemins des deux journaux, n, t3, s4, t_fin et les deux projections retenues (bornes basses). À la fin : les quatre empreintes des manifestes, les lignes « fréquences gelées : » et « réglages gelés : », le code de sortie lu dans son fichier, l'égalité ou non des empreintes de l'étape 3 avec celles de l'essai 2. À un arrêt nommé du programme : la cause et l'inventaire du dossier (R11), sans aucun geste avant. À une coupure par redémarrage : voir le complément 1 v5.
