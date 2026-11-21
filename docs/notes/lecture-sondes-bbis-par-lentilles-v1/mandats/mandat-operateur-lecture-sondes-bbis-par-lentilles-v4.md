# Mandat de l'opérateur neuf — montage et calcul au processeur de la lecture des directions des sondes de l'étape B bis par la lentille publique — v4

Rédigé par la session des lentilles (`session_013QMaykLXtozHttcSQ4ke1s`) le 2026-11-19 à la demande de la mère ; pièce de travail (classe
C). Vaut pour la session neuve que la mère ouvre **après** l'inscription de `CODE-LENTILLES-BBIS` et de `GO-LENTILLES-BBIS`.

**Version 4** (session des lentilles, `session_01Qi7Gr3vedYVukbyqBbHd7z`, 2026-11-21). Elle remplace la v3 (`d24ab21e…`), qui reste archivée sans modification. Seul changement, après l'arrêt du montage de la deuxième course (code 3 : refus 401 du dépôt à porte sur `tokenizer.model`, demandé par le script voisin du corpus dans l'enfant sans clé), sous les mots de Lazar GO-2026-11-21-63 : **le lanceur est `lanceur_v9`** (code au commit `9e078c7f`, module neuf `cache_tokeniseur_v2` qui marque absents du cache les trois fichiers que le dépôt du modèle ne porte pas, puis essaie le chargement du tokeniseur en ligne et sans clé avant tout flux long ; fiche `docs/notes/lecture-sondes-bbis-par-lentilles-v1/fiche-code/fiche-code-lentilles-bbis-v3.json`, `31632853…` ; contre-lecture conforme `contre-lectures/contre-lecture-correctif-tokeniseur-act-corpus-v1.md`, `1e8c1704…`). Partout où la v3 ou la v2 disent `lanceur_v7` ou `lanceur_v8`, lis `lanceur_v9` ; la fiche est celle que cite la **dernière** ligne `CODE-LENTILLES-BBIS`. Un arrêt nommé de l'essai du tokeniseur (fichier présent dans l'arbre, révision qui a bougé, chargement en échec) tombe avant tout flux long : tu le rends à la mère par son nom, sans relancer. Course sous un identifiant neuf, donné par la mère ; tu n'ouvres rien des courses arrêtées. Tout le reste de la v3 vaut tel quel.

**Version 3** (session des lentilles, `session_01Qi7Gr3vedYVukbyqBbHd7z`, 2026-11-21). Elle remplace la v2 (`90f8befb…`), qui reste archivée sans modification. Seul changement, après l'arrêt de la première course sur « jeu de données de la tranche zh : aucun fichier de données dans l'arbre » (arbre du jeu paginé, première page seule lue), sous les mots de Lazar GO-2026-11-21-63 : **le lanceur est `lanceur_v8`** (code au commit `11f1cee7`, module neuf `corpus_pagine_v1` qui suit les pages de l'arbre ; fiche `docs/notes/lecture-sondes-bbis-par-lentilles-v1/fiche-code/fiche-code-lentilles-bbis-v2.json`, `63ab873b…` ; contre-lecture conforme `contre-lectures/contre-lecture-correctif-pagination-corpus-v1.md`, `8ba0f061…`). Partout où la v2 dit `lanceur_v7`, lis `lanceur_v8` ; partout où elle cite la fiche `a44c0e54…`, lis la fiche v2 que cite la **dernière** ligne `CODE-LENTILLES-BBIS`. Avant le montage, réinstalle `requirements-cpu.txt` (`requests` y est ajouté). Course sous un identifiant neuf, donné par la mère ; tu n'ouvres rien de la course arrêtée. Tout le reste de la v2 vaut tel quel.

**Version 2** (session des lentilles, `session_01QPDgKhLLz1oJQwPBeB5aFs`, 2026-11-21). Elle remplace la v1, qui reste archivée sans
modification. Ses changements, sur le mot de Lazar GO-2026-11-21-24 et après les contre-lectures du lanceur :
- **le lanceur** est `lanceur_v7` (code au commit `cc7f4576`, fiche définitive
  `docs/notes/lecture-sondes-bbis-par-lentilles-v1/fiche-code/fiche-code-lentilles-bbis-v1.json`, `a44c0e54…`), versé sur la branche
  principale par la mère ;
- **la consigne D** : ce que tu fais après un refus de la garde du fichier d'arrêt ;
- **le lancement détaché** : journal dans un fichier, identifiant de processus écrit ;
- **ce que tu vois d'un arrêt d'égalité** : son nom seulement.

## Qui tu es
L'**opérateur neuf** du texte scellé `prereg/lecture-sondes-bbis-par-lentilles-v1.md` (`ca5066d757df604cbf642db84f8a8fc56a0db8b6cc183f734842b7abdaf6d572`).
Tu n'as lu aucune sortie ni aucun score de l'apprentissage des sondes sur la tâche, ni des autres chaînes interdites ; tu n'es ni
l'auteur, ni le développeur, ni le lecteur de ce texte, ni le lecteur ou le juge d'aucun verdict qu'il nomme. Tu **lances** le montage
puis le calcul, et tu ne lis **que** les codes d'arrêt, les existences et les empreintes. **Tu n'ouvres aucune table.**

## Ta machine (nœud N9, option (a))
Le processeur du conteneur de **ta** session neuve, qui ne porte aucun dossier de course. **Aucune machine louée, aucune carte
graphique, aucune dépense** (0 USD ; la « Liste d'arrêt » arrête toute dépense).
- **Clone partiel** du dépôt de travail, **sans** `diag/`, `runs/`, `donnees/` ni `traces/` : la mère ouvre ta session avec une extraction
  partielle limitée à `src`, `tests`, `scripts`, `prereg`, `registres`, `docs/sources/neuron-lens-lecture-20261113`,
  `docs/notes/lecture-sondes-bbis-par-lentilles-v1`, au commit de la branche principale qui porte le code et la fiche citée par
  `CODE-LENTILLES-BBIS`. Tu vérifies l'empreinte de cette fiche contre la ligne avant tout lancement ; le lanceur le refait.
- Au démarrage, tu prouves l'absence de tout dossier de course : `find /home/user -maxdepth 4 \( -name diag -o -name runs -o -name donnees -o -name 'bbis-*' \) -print`
  doit ne rien rendre hors de ton dossier de travail neuf ; sinon arrêt et message à la mère.
- Les correctifs (2), (4) et (6) du code voisin sont extraits **un par un, par leur chemin** depuis la branche `claude/brave-galileo-jhp684`,
  dans le dossier `docs/notes/neuron-lens-v1/correctifs*/`, avec `git show <commit>:<chemin>`. Leurs empreintes sont comparées au texte
  scellé avant usage ; rien d'autre de cette branche n'est extrait.
- Relevés refaits au montage et versés au manifeste : fils, mémoire, disque libre (au moins 6 Go au départ, sinon arrêt) et versions.

## La clé de la plateforme de modèles (nœud N8, option (a)) — par son nom seulement
- Elle s'appelle **`HF_TOKEN`**. C'est une **variable d'environnement posée par la configuration de l'environnement infonuagique de ta
  session**, l'environnement que la mère choisit à l'ouverture. C'est la clé gardée par Lazar (mot du 2026-11-19, « garder la cle »).
- Tu ne la reçois **jamais** d'une autre session, ni par message, ni par fichier, ni par argument.
- Tu testes sa présence **sans l'imprimer**, par exemple `[ -n "${HF_TOKEN:-}" ] && echo "clé présente" || echo "clé absente"` ; jamais
  `env`, `printenv`, `set` ni `echo $HF_TOKEN`.
- Les bibliothèques de téléchargement la lisent d'elles-mêmes par son nom. Aucun mode de débogage : ni `HF_DEBUG`, ni
  `HF_HUB_VERBOSITY=debug`, ni journal « debug » de `urllib3`, `httpx` ou `requests`, ni `curl -v` ou `--trace`.
- Elle n'est écrite dans aucun fichier, journal ou manifeste. Le lanceur vérifie qu'aucune occurrence de sa valeur n'existe dans ce qu'il
  écrit.
- **Clé absente ou vide** : arrêt, nœud à la mère. C'est Lazar qui l'ajoute à la configuration de l'environnement, jamais une session.

## Ce que tu lis (autorisé)
- Le texte scellé, dont la « Liste d'arrêt » ;
- les lignes du registre propre `registres/lecture-sondes-bbis-par-lentilles-v1.md` ;
- dans `registres/t07-etape-b-bis-v1.md`, **les seules clés et heures nommées en E-3** : `SCORES-BBIS` avec son chemin et son empreinte,
  la présence de `VERDICT-BBIS` avec sa clé et son heure (jamais le fichier du verdict), `CODE-BBIS` avec sa clé, son heure, son chemin et
  son commit ;
- les codes d'arrêt, les existences de fichiers et les empreintes produits par le lanceur.

## Ce que tu ne lis jamais
- toute la liste « Jamais ouverts » du texte scellé ;
- les tables, les lectures et les phrases que le calcul écrit (`tables-lentilles-bbis.json`, `lectures-lentilles-bbis-NNN.npz`) : tu les
  verses sans les ouvrir ;
- E-1 et E-2 : ils ne sont ouverts **que par le programme**, et seulement après l'inscription de `VERDICT-BBIS`, par clone partiel sans
  contenus (`--filter=blob:none`) puis extraction de ces deux chemins et de leurs compagnons seulement.

## Le lanceur et sa conduite (v2)
- **Commande** : `PYTHONPATH=src python -m controle_ia.lentilles_sondes_bbis.lanceur_v9 <montage|calcul|recuperer|phrases> …`.
  L'aide de la commande (`--help`) donne les arguments. Aucun autre lanceur, aucune autre version.
- **Lancement détaché.** Les tâches de fond de ta session s'arrêtent à deux heures ; le calcul peut durer jusqu'à 6 h (arrêt à 8 h).
  Tu lances donc le montage et le calcul détachés de l'outil :
  - par `setsid nohup … > <journal> 2>&1 & echo $! > <fichier-pid>`, dans ton dossier de travail ;
  - le journal ne contient que ce que le lanceur imprime : des codes d'arrêt, des existences et des empreintes. Tu n'y ajoutes rien ;
  - tu surveilles l'avancement par l'existence du processus (`kill -0 <pid>`) et par la fin du journal. Ne lis le journal que pour un
    code d'arrêt ou un rendu final ;
  - tout arrêt se fait par cet identifiant de processus (R10).
- **Ce que tu vois d'un arrêt.** Un arrêt d'égalité au vingtième rang ou des directions nulles (`EgaliteDirectionLue`,
  `EgaliteNulleDecisive`) n'affiche que son nom, le chemin de `arret.json` et, le cas échéant, « fichier d'arrêt non écrit » ou
  « versement à l'arrêt en échec : rien n'est supprimé » (GO-2026-11-20-56 et GO-2026-11-21-06).
  - **Tu n'ouvres jamais `arret.json`.** Il porte le message entier, que seul un lecteur désigné par la mère lira. Tu le verses comme
    les autres fichiers, sans l'ouvrir, et tu rends à la mère son nom, son chemin et son empreinte.
- **Garde du fichier d'arrêt déjà présent** (GO-2026-11-21-06). Le calcul refuse de partir si un `arret.json` existe déjà au chemin où
  l'arrêt de la course serait écrit (`<sortie>/versement/<run>/calcul-interrompu/arret.json`).
  - **Consigne après un refus de cette garde** (nœud D, GO-2026-11-21-24) : ne supprime rien, ne déplace rien et ne renomme rien.
  - Pour relancer, prends un **identifiant de course neuf** ou un **dossier de sortie neuf**. Le montage est lié à l'identifiant de
    course : un identifiant neuf demande un montage neuf.
  - Ne relance jamais dans le même dossier de sortie après un arrêt.
  - Rends le refus à la mère avant toute relance.

## Ce que tu fais, dans l'ordre (plan d'analyse, points 1, 4 à 6 et 10)
1. **Vérifier les préalables** au registre propre : `SCELLEMENT-`, `GO-` et `CODE-LENTILLES-BBIS` présentes ; `SCORES-BBIS` présente
   une seule fois ; `VERDICT-BBIS` présente. Sinon, rien ne part.
2. **Lancer le montage** (point 4) : essais d'un octet par hôte avant tout flux long, poids lus en flux et vérifiés, lentille publique et
   sa provenance, 31 matrices, jetons gardés, code voisin et correctifs. Proposer à la mère la ligne `MONTAGE-LENTILLES-BBIS`
   (chemin et empreinte de `montage-lentilles-bbis.json`).
3. **Ouverture des entrées par le programme** : proposer la ligne `ENTREES-LENTILLES-BBIS`.
4. **Lancer le calcul** (points 5 et 6), sous l'horloge de 8 h ; garde du disque (moins de 1 Go : arrêt).
5. **Verser, sans ouvrir**, sur la branche `calcul/lentilles-sondes-bbis-v1` : morceaux de moins de 95 Mo, compagnons `.sha256`,
   manifeste (R9). Proposer à la mère la ligne `TABLES-LENTILLES-BBIS`.
6. **Nettoyer** (point 10) : supprimer, par chemin et dans le seul dossier de cette chaîne, les poids, la lentille, les tenseurs extraits
   et le corpus.
   - Règle de Lazar « récupérer ce qui est récupérable » : avant ce nettoyage, faire l'inventaire (noms, tailles, empreintes) de ce qui
     va être supprimé et le verser scellé.
   - Les fichiers que la licence interdit de garder (poids, lentille) ne sont pas versés ; leur empreinte l'est.
7. **Rendre à la mère** : codes d'arrêt, durées, empreintes, lignes de registre proposées.
   - Les lignes du registre propre sont inscrites par la mère.
   - La lecture humaine (point 8) revient à un **lecteur neuf**, qui n'est pas toi.

## Arrêts
- La « Liste d'arrêt » du texte scellé, entière.
- Tout refus d'une permission, du crochet ou du classifieur : ni rejoué, ni reformulé, ni contourné ; arrêt et message à la mère.
- Une exposition involontaire à une table ou à un fichier interdit : arrêt, déclaration écrite, nœud.
- Les arrêts se font par PID, jamais par motif de ligne de commande (R10).
- Avant de t'arrêter : passation dans `docs/notes/lecture-sondes-bbis-par-lentilles-v1/operation/`, scellée et poussée.
