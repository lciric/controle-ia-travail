# Mandat du développeur neuf — lanceur de la première passe, version 5 : messages d'arrêt cloisonnés — v1

Rédigé le 2026-11-20 par la session des lentilles. Classe B (instrument). Le développeur est un agent neuf sur Fable. Sa contre-lecture sera faite par un agent Opus 5.5, d'un autre modèle.

## Le mot qui fonde ce mandat

GO-2026-11-20-56, donné par Lazar dans la session mère vers 13:25Z, et relu par son identifiant dans `registres/go.md` sur la branche principale :

> **Lecture des sondes par lentilles** : le message entier d'un arrêt d'égalité ou des directions nulles va dans le fichier d'arrêt seulement ; la ligne de commande n'affiche que le nom de l'arrêt (recommandation du contre-lecteur, 7954d0fc…) ; lanceur neuf et liste de fichiers neuve dans la fiche du code.

## Ce qu'on te demande, et rien d'autre

Écrire `src/controle_ia/lentilles_sondes_bbis/lanceur_v5.py`. C'est `lanceur_v4.py` (`dc74be00…`) avec ce seul changement : quand le calcul s'arrête sur un **arrêt d'égalité au vingtième rang** (étage (i), directions lues) ou sur un **arrêt des directions nulles** (étage (ii)) :
1. le message entier, tel que l'addendum l'exige, est écrit **seulement** dans `arret.json` ;
2. la ligne de commande, c'est-à-dire la sortie d'erreur et la sortie standard, **n'affiche que le nom de l'arrêt** ;
3. aucun identifiant de jeton, aucune valeur, aucune borne de valeur p et aucun nom de statistique n'apparaît ailleurs que dans `arret.json`.

Tu peux ajouter le chemin de `arret.json` à côté du nom de l'arrêt : c'est une existence, que l'opérateur a le droit de lire. Les autres arrêts gardent leur comportement actuel ; ne les change pas.

Points à traiter et à dire dans ta note :
- **L'arrêt d'égalité doit toujours écrire son `arret.json`, même avant le départ du calcul.** Dans `lanceur_v4`, un arrêt levé avant `etat["parti"]` est relevé sans rien écrire. Si un arrêt d'égalité ou des directions nulles peut survenir avant le départ, il faut quand même que son message entier aille dans un `arret.json` et que la ligne de commande n'en montre que le nom. S'il ne peut pas survenir avant le départ, montre-le.
- **Le message enchaîné d'un échec du versement** (« versement à l'arrêt en échec ») reprend le message d'origine. Il ne doit pas faire sortir le message entier d'un arrêt d'égalité ou des directions nulles sur la ligne de commande.
- **Aucune trace d'exception non attrapée** ne doit porter ce message vers la sortie d'erreur.
- **Le nom de l'arrêt** est le nom de sa classe, ou un code fixe ; tu en écris la liste dans la note.

Fabrique `lanceur_v5` par un outil, comme `lanceur_v4` l'a été (`developpement/outils/fabrique-lanceur-v4-v1.py`) :
- l'outil s'appelle `outils/fabrique-lanceur-v5-v1.py` et part de `lanceur_v4.py` ;
- la différence doit être lisible en entier ;
- tu peux changer, dans `lanceur_v5`, les mots qui citent sa propre version et la liste `MODULES`, où `lanceur_v4` est remplacé par `lanceur_v5`.

Si l'arrêt d'égalité et l'arrêt des directions nulles sont levés dans `statistiques_v3.py`, ne touche pas ce module. Le tri entre message entier et nom se fait dans le lanceur.

## Essais (règle R5 : un cas sain et un artefact par garde)

Écris un fichier d'essais neuf, `tests/test_lentilles_sondes_bbis_lanceur_v5_v1.py`, au moins avec les cas suivants :
- pour chacun des deux arrêts, la ligne de commande (sortie d'erreur et sortie standard capturées) ne contient que le nom de l'arrêt, plus le chemin de `arret.json` si tu le donnes ;
- `arret.json` porte le message entier : les deux identifiants de jeton et la valeur commune pour l'étage (i) ; la borne basse et la borne haute de la valeur p pour l'étage (ii) ;
- l'artefact : une copie jetable du lanceur qui imprime le message entier doit faire tomber l'essai ;
- un autre arrêt, par exemple un registre sans la ligne de l'addendum, garde sa sortie actuelle ;
- un échec du versement, simulé, ne fait pas sortir le message entier ;
- le cas sain de bout en bout, sans arrêt, rend la même sortie que `lanceur_v4`.

Copie aussi, sous des noms neufs visant `lanceur_v5`, les fichiers d'essais existants qui importent `lanceur_v4`, pour que tout ce qui éprouvait `lanceur_v4` éprouve `lanceur_v5`. Ne réécris aucun fichier existant (règle R12).

Lance tous les essais du paquet avec `PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src python -m pytest -q -p no:cacheprovider tests/test_lentilles_sondes_bbis_*.py`. Ils prennent environ dix minutes. Rapporte le décompte et verse la sortie dans `developpement/sortie-essais-v5.txt`.

Ne lance pas la suite complète du dépôt.

## Pièces à écrire, toutes scellées (`python -m controle_ia.scellement sceller`)

Dans `docs/notes/lecture-sondes-bbis-par-lentilles-v1/developpement/` :
- `empreintes-code-v5.txt` : les treize modules de `lanceur_v5.MODULES` d'abord, dans cet ordre, puis les essais. C'est la liste de fichiers neuve de la fiche du code.
- `notes-lanceur-v5-v1.md` : ce qui change, la liste des noms d'arrêt, les points ci-dessus et leurs réponses, et ce qui reste ouvert.
- `outils/fabrique-lanceur-v5-v1.py`.
- `sortie-essais-v5.txt`.

## Ce que tu lis

**Sur la branche `claude/brave-galileo-jhp684`** :
- ce mandat ;
- `src/controle_ia/lentilles_sondes_bbis/` en entier ;
- les essais `tests/test_lentilles_sondes_bbis_*.py` et `tests/lentilles_sondes_bbis_jouets_*.py` ;
- dans `docs/notes/lecture-sondes-bbis-par-lentilles-v1/` :
  - `developpement/` : notes, empreintes, outils, sorties, et la passation `passation-developpeur-deux-passes-2026-11-20-etape-1-close-v1.md` ;
  - `contre-lectures/` : les deux rendus du contre-lecteur.

**Sur la branche principale**, par `git show origin/main:<chemin>`, en vérifiant chaque empreinte :
- `prereg/lecture-sondes-bbis-par-lentilles-v1-addendum-concentration-v1.md` (`7c738708…`), en entier ;
- dans `prereg/lecture-sondes-bbis-par-lentilles-v1.md` (`ca5066d7…`) : les sections « Liste d'arrêt », « Qui, quelle machine, quel coût » et « Code neuf » seulement.

## Ce que tu n'ouvres jamais

- La liste « Jamais ouverts » du texte de lecture v1 ou v2, et tout ce qu'elle nomme.
- Toute sortie, tout score, toute table, toute lecture et tout verdict de l'apprentissage des sondes sur la tâche (étape B bis), y compris la clé `VERDICT-BBIS` et la note de lecture réservée à Lazar.
- Toute table ou sortie de la lecture par la lentille publique.
- `diag/`, `runs/`, `donnees/`, `docs/verdicts/`.
- Les branches `donnees/*`, `calcul/*` et `verdict/*` : tu n'en extrais aucune et tu n'en lis rien. Si un `git fetch` en affiche les noms, déclare-le. Fais tes `fetch` par nom de branche.
- Tout fichier dont le nom contient « consigne-privee » ou « conception-ii-b », et `brouillons/ii-b-saboteur-budget-v1/`.
- P3, P3-bis, T0.6, T0.7 hors des textes cités, l'étape B, le bras d'attaque, le saboteur à budget.
- Tout registre de la branche principale, sauf une ligne de `registres/lecture-sondes-bbis-par-lentilles-v1.md` cherchée par son identifiant, si tu dois en voir la forme.
- Aucune clé ni aucun secret.

## Règles de travail

- Tu écris seulement sur la branche `claude/brave-galileo-jhp684`. Fais `git pull` avant de commencer. Pousse avec `git push -u origin claude/brave-galileo-jhp684`, en réessayant jusqu'à quatre fois en cas d'erreur réseau. Si le push est refusé, fais `git fetch origin claude/brave-galileo-jhp684 && git merge --no-edit FETCH_HEAD`, puis pousse.
- Les messages de commit finissent par :
  `Co-Authored-By: Claude Fable 5.2 <noreply@anthropic.com>`
  puis la ligne `Claude-Session: https://claude.ai/code/session_01QPDgKhLLz1oJQwPBeB5aFs`.
  Aucun identifiant de modèle ailleurs dans le message.
- Installe torch en version processeur depuis l'index de PyTorch, puis le reste de `requirements-cpu.txt` sans torch, dans un environnement du bloc-notes : `/tmp/claude-0/-home-user-controle-ia-travail/4c8fa2bf-6366-5665-a27b-6d403d9264f6/scratchpad/developpeur-lanceur-v5/`. N'installe pas torch depuis PyPI, qui tire les bibliothèques des cartes graphiques. Ne télécharge aucun modèle, aucune lentille, aucun corpus. Rien ne se lance, ne se loue ni ne se dépense.
- Passe `PYTHONDONTWRITEBYTECODE=1` à tous tes essais ; ne laisse aucun `__pycache__` sous un arbre scellé.
- Tu ne crées aucune règle neuve. Si un point est ambigu, écris-le dans la note et arrête-toi sur ce point, sans le trancher.
- Un refus d'outil n'est jamais rejoué, reformulé ni contourné ; tu le déclares.
- Tu ne touches pas à l'étape 2, la seconde passe, qui attend un autre mot.

## Forme du rendu (ton message final)

1. Verdict en une à trois lignes.
2. Commit et empreintes de chaque pièce.
3. Décompte des essais.
4. La liste des noms d'arrêt, et les réponses aux points à traiter.
5. Ce qui reste ouvert.
6. Expositions et refus d'outil.
7. La liste des fichiers à donner au contre-lecteur.
