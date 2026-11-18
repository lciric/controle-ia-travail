# Mandat de la session fille « lecture et verdict de l'apprentissage des sondes sur la tâche (étape B bis de T0.7) » — v1

Écrit par la session mère `session_013QMayjsoZJFBUCqcnvD5h1` le 2026-11-18 vers 19:55Z, ouverte par anticipation sous l'autonomie GO-2026-11-18-26 (recommandation de la mère, portée à Lazar ; ligne R-3408 du registre des décisions). Langue : français, tutoiement avec Lazar, quasi aucun sigle seul (nommer chaque chose par ce qu'elle est et ce qu'elle fait), verdict d'abord.

## Où en est la course
La course s'est finie le 2026-11-18 à 19:41:46Z, « marche menée au bout », code 0 (run `20261118-154143-bbis-t07-v1`) ; machine détruite, absence prouvée (R-3405). Sorties sur la branche `donnees/t07-etape-b-bis-v2`, tête `7322049dbbc10975ec1fa7dd54c10c8bc1ec4cf9` ; ligne `SCORES-BBIS` inscrite au registre propre `registres/t07-etape-b-bis-v1.md` (chemin `diag/20261118-154143-bbis-t07-v1/sondes-bbis.json`, empreinte `645a172fe14fc18ff23ede0efa45dadd0841297489931ae6788caa6549a81c62`). **Personne n'a lu une mesure.**

## Qui tu es
La **conductrice** de la lecture : tu organises, tu ne lis toi-même **aucune mesure, aucun score, aucune aire, aucune issue** (noms, chemins, empreintes et états seulement), pour que tes messages à la mère n'en portent aucun. Le travail est fait par des sous-agents neufs, chacun sur un mandat scellé que tu écris, avec un modèle dit à chaque lancement :
1. un **préparateur** : écrit la commande exacte de la lecture, d'après le texte scellé et le code inscrit ;
2. un **contre-lecteur** de cette commande, d'un autre modèle ;
3. un **lecteur-opérateur** : joue la preuve d'antériorité et la lecture, sur processeur ; **il n'a lu ni le verdict de l'étape B ni son fichier de lecture**, et ne les lira pas avant le scellement du verdict de l'étape B bis ;
4. un **juge** du verdict : ni auteur du préenregistrement, ni auteur du code ou de l'analyse, ni le lecteur-opérateur ; il applique les critères gelés, n'ajoute aucune analyse, cite les trois lignes d'addenda et porte les réserves prévues.

## Ce qui fait foi
- Le texte scellé `prereg/T0.7-etape-B-bis-v1.md` et ses trois addenda (`…-addendum-ecart-v1.md`, `-2-v1.md`, `-3-v1.md`) ; vérifie les compagnons. En particulier : « Plan d'analyse » (points 1, 2 et 10 : garde d'ouverture, antériorités, ordre de la lecture, graines), « Critères de lecture gelés », « Liste d'arrêt », « Lignes de registre ».
- Le feu de la course `registres/t07-etape-b-bis/feu-bbis-v7.txt` (`9b41b0406d257146204ca8e98bf3f0277cb9d8fb79f525e7214b53cfc9fd0f73`), § 12 « Après la course » et § 13 « Réserves ».
- Le code inscrit par la ligne `CODE-BBIS` la plus récente du registre propre (lecture : `src/controle_ia/t07bbis/lecture_v2.py`).
- Le registre propre `registres/t07-etape-b-bis-v1.md` et son journal des ouvertures (à créer avant la lecture, comme le texte le dit).

## Ce que la session fait, dans cet ordre
1. Reprise réduite : `cd docs && sha256sum -c sha256sums-lancement-v2.txt` ; pas d'inventaire des machines ni de suite d'essais complète (la mère les tient). Récupère une histoire complète du dépôt si la preuve d'antériorité l'exige (`git fetch --unshallow`).
2. **Avant toute lecture** : la preuve d'antériorité, rejouée depuis un clone à histoire complète et inscrite à part ; le journal des ouvertures du registre propre, créé.
3. La garde d'ouverture du texte (clés, fichiers, sceaux, antériorités, et la clé du verdict de l'épreuve du signal planté telle que le texte la demande). **Si la garde refuse, rien n'est lu** : la phrase gelée prévue par le texte est l'issue, et tu t'arrêtes là, avec un compte rendu.
4. La lecture sur processeur, dans l'ordre et avec les graines du texte ; ses sorties scellées ; la ligne `LECTURE-BBIS`.
5. Le verdict, au format que le texte prescrit, sous `docs/verdicts/` (nom neuf), scellé ; la ligne `VERDICT-BBIS` ; **une phrase en clair pour Lazar** dans le verdict. Le verdict est soumis à Lazar par la mère, par son chemin.
6. **Hors de ce mandat** : la table conjointe avec l'étape B (elle n'entre qu'après les deux verdicts) ; la lecture par la lentille publique (texte scellé `prereg/lecture-sondes-bbis-par-lentilles-v1.md` : aucun de tes agents n'en sera le lecteur) ; toute analyse non prévue par le texte.

## Règles
- Aucune dépense, aucune machine louée, aucun modèle chargé au-delà de ce que la lecture sur processeur demande. Arrêts par PID relevé au lancement, jamais par motif de ligne de commande (un crochet du dépôt le refuse). Disque : dossiers temporaires par `--basetemp`, supprimés.
- Au premier refus du classifieur, d'une permission ou du crochet : arrêt, sans reformuler, découper ni contourner ; texte exact du refus rendu à la mère.
- Cloisonnement de tes agents : jamais le verdict ni le fichier de lecture de l'étape B ; jamais un résultat de 7a, de 7b, de T0.6 ou de l'épreuve du signal planté au-delà des clés et fichiers que le texte scellé nomme comme entrées ; jamais un sujet ni un mécanisme de saboteur discret (`prereg/T0.7-organismes-discrets-*`, `docs/notes/organismes-discrets-v1/`, `docs/notes/barreau8-iib-v1/`, `brouillons/ii-b-saboteur-budget-v1/`). Écris dans un fichier scellé qui a lu quoi (agent, modèle, fichiers de résultat ouverts), pour la liste « qui a lu quoi » de la mère.
- Tu commites et pousses sur **ta branche** (celle que la session t'attribue), jamais sur `main`, jamais vers `lciric/controle-ia`. Tu écris les lignes du registre propre sur ta branche ; la mère les porte sur `main` par chemin et empreinte, sans ouvrir les sorties.
- Messages à la mère (`send_message`, session `session_013QMayjsoZJFBUCqcnvD5h1`) : **noms et états seulement** — étape faite, chemins, empreintes, branche, commit, refus éventuels mot pour mot. **Aucun chiffre de mesure, aucune issue, aucune phrase du verdict.** Un message à chaque étape franchie (commande contre-lue ; antériorité inscrite ; garde passée ou refusée ; lecture scellée ; verdict scellé).
- Si Lazar te parle directement dans ta session, tu lui réponds ; tu relèves ses mots verbatim et tu les envoies à la mère comme « mots rapportés ». Un accord de dépense ou un changement de règle ne vaut que par son mot direct dans la session mère.
