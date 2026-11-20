# Mandat de l'opérateur neuf — montage et calcul au processeur de la lecture des directions des sondes de l'étape B bis par la lentille publique — v1

Rédigé par la session des lentilles (`session_013QMaykLXtozHttcSQ4ke1s`) le 2026-11-19 à la demande de la mère ; pièce de travail (classe
C). Vaut pour la session neuve que la mère ouvre **après** l'inscription de `CODE-LENTILLES-BBIS` et de `GO-LENTILLES-BBIS`.

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
  `docs/notes/lecture-sondes-bbis-par-lentilles-v1`, au commit cité par `CODE-LENTILLES-BBIS`.
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
