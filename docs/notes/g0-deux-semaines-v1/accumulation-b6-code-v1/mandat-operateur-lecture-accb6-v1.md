# Mandat de l'opérateur de la lecture du barreau 6 (accumulation sur l'épisode) — v1

Écrit par la session mère `session_013QMayjsoZJFBUCqcnvD5h1` le 2026-11-18 vers 16:25Z, sous GO-2026-11-18-30 (mot de Lazar : « go; prépare ce qu'il faut ») et R-3310. Langue : français, sans sigle seul.

## Qui tu es
Un **opérateur neuf**, sous-agent de la session mère : tu n'as écrit ni le texte du barreau 6, ni son code, ni T0.6, T0.7, P3-bis ; tu n'as lu aucun résultat de ces travaux. **Tu ne lis aucun résultat** : ton rôle est de faire tourner la lecture préenregistrée, pas de la lire. Le verdict sera prononcé ensuite par un autre agent neuf.

## Texte qui fait foi
`prereg/accumulation-barreau6-v1.md` (scellé, R-2343 ; empreinte `2e2dddc60667cd5c670a37a656e896cc210e59ac92be37211bbb1680fc1a4b22` à vérifier, et son compagnon). Lis-le **en entier** : sa procédure de lancement (sections « Plan d'analyse », « Liste d'arrêt », « Lignes de registre », « Code ») prime sur ce mandat. Registre propre : `registres/accumulation-b6-v1.md` (ligne `SCELLEMENT-ACCB6`). Fiche de code : `registres/code-accb6/CODE-ACCB6-v1.json` (`1957d087…`, commit du code `282e295ec8e825b9c045bd30ebfdac3cbe55496f`). Le code est fusionné dans `main` (commit `5e10f33d`, pas 1 fait par la mère).

## Ce que tu fais, dans l'ordre (arrêt au premier écart, compte rendu)
1. **Arbre de travail séparé** : `git worktree add /home/user/accb6-racine-v1 <tête de main>` (n'écris jamais d'entrée ni de sortie dans `/home/user/controle-ia-travail` lui-même). Ce dossier est RACINE.
2. **Essais** : la suite d'essais que le texte exige avant la lecture (pas 4 du texte, essais de T0.7 dans l'arbre fusionné ; environ 50 minutes), depuis RACINE, environnement `/home/user/controle-ia-travail/.venv` (`PYTHONPATH=src`). Code de sortie et ligne de compte recopiés ; tout échec : arrêt.
3. **Entrées scellées réunies sous RACINE, sans être lues** : les fichiers que le texte et la garde exigent (scores de l'étape A de T0.7, mesures de 7b, sondes, notation et lecture de T0.7, manifestes des runs, fichiers cités par les lignes partagées), **extraits par leur chemin seul** des branches qui les portent (`git show <branche>:<chemin> > <fichier>` ou `git archive` d'un chemin précis ; ces branches sont des copies complètes du dépôt : n'en extrais que les chemins nommés). Branches candidates, d'après leurs noms : `origin/donnees/t07-etape-a-v1`, `origin/calcul/t06-confirmation-7b-v1` (et celles que les lignes du registre des scellements désignent). Chaque fichier : empreinte calculée par `sha256sum` (commande simple, sans boucle) et comparée **sur 64 caractères** à la ligne du registre qui le scelle et à son compagnon `.sha256`. **N'ouvre aucun de ces fichiers** (ni `cat`, ni `head`, ni `python -c 'print(...)'`, ni `jq`) : seules les empreintes et les tailles s'affichent.
4. **Comparaison des 17 empreintes** de fichiers hors paquet que le texte fait contrôler au lancement : écrite dans un fichier de RACINE avant le lancement, et recopiée au compte rendu.
5. **Lancement unique** : `PYTHONPATH=src python -m controle_ia.accumulation_b6.lecture_v1 lire RACINE` depuis RACINE (ou la forme exacte que le texte prescrit), **sortie standard détournée vers un fichier que personne n'ouvre**, sortie d'erreur lue. Codes : 0 = lecture écrite et scellée ; 2 = refus de la garde (nœud) ; 3 = arrêt. **Aucune relance** après un code 3 ; après un code 2, compte rendu et arrêt (la mère décide).
6. **Rien d'autre** : ne lis ni la sortie standard, ni `diag/<…accb6-lecture>/lecture-accb6.json`, ni le contenu de la ligne `LECTURE-ACCB6` au-delà de son chemin et de son empreinte. Ne commite pas, ne pousse pas, n'écris rien dans le dépôt principal.

## Règles fermes
- Arrêt au premier refus d'une permission, du crochet de garde ou du classifieur : aucun rejeu, aucune reformulation, aucun contournement ; compte rendu d'une ligne.
- Cloisonnement : aucun résultat, aucune issue, aucun score de 7a, 7b, T0.6, T0.7, de la base « mots et coût », de l'étape B, de l'étape B bis, de P3-bis ; rien sous `docs/verdicts/` ; aucune recherche récursive dans le dépôt. Si tu ouvres par erreur un contenu interdit : arrête et déclare-le.
- Aucune dépense (processeur seulement).

## Compte rendu final (ton dernier message, court)
Code de chaque étape ; empreintes des entrées (comparaison sur 64 caractères : conformes ou non) ; sortie de la suite d'essais (ligne de compte) ; code de la lecture ; chemins et empreintes des sorties écrites par le programme (fichier de lecture, fichier de sortie standard non ouvert, ligne `LECTURE-ACCB6` : chemin du registre et empreinte du registre après écriture) ; tout écart ; toute lecture faite hors de ce mandat.
