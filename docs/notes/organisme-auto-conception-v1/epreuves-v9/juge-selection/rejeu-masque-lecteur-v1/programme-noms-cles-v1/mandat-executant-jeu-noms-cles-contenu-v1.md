VERSION DE PYTHON : `python3 --version` ; AUCUN `-c`, AUCUN `-` APRÈS PYTHON3

AUCUNE COMMANDE DE LISTE : NI `ls`, NI `find`, NI `git ls-tree`, NI `git ls-files`, NI `git status`, NI `git show --name-only`, NI `grep -r`, NI RECHERCHE SUR UN DOSSIER ENTIER, NI JOKER DANS UN CHEMIN. TOUT FICHIER S'OUVRE PAR SON CHEMIN COMPLET. UNE COMMANDE SIMPLE PAR APPEL : NI `&&`, NI `;`, NI `|`, NI BOUCLE, NI `echo` APRÈS UNE COMMANDE. `git show` TOUJOURS REDIRIGÉ VERS UN FICHIER (redirection du shell `>`, jamais `--output=`). AUCUNE RECHERCHE DE MOTIF LARGE.

# Mandat de l'exécutant — jeu unique du programme des noms de clés de `contenu` — v1

Pièce de travail (classe C), donnée par la session du compte organisme le 2026-11-20, sur **GO-2026-11-20-28** (`registres/go.md` sur main, ligne 559) : « Un agent neuf, qui ne lit aucune carte, lit par un programme contre-lu les seuls noms de clés de `contenu` du seul fichier `fiches.json` de la course v9 (ba65c411…, sous `archives-reponses-modeles/`). Le programme ne rend que les noms hors des dix champs, avec le nombre de cartes qui portent chacun, sans valeur ni identifiant. […] Quatrième exception bornée à la règle de ce dossier. » Programme contre-lu « Conforme » (`contre-lecture-noms-cles-contenu-v1.md`, `88bec845…`).

## Qui

Un agent neuf : tu n'as écrit ni le programme, ni ses essais, ni sa contre-lecture, ni le masque. Tu signes « exécutant neuf, modèle S ».

## Les gestes, un par appel, dans cet ordre, chacun une seule fois

PROG = `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/juge-selection/rejeu-masque-lecteur-v1/programme-noms-cles-v1`. JEU = `/tmp/claude-0/-home-user-controle-ia-travail/227b647d-2ece-5654-bf04-8493b3ed2f19/scratchpad/jeu-noms-cles-contenu-v1` (à créer par `mkdir -p`). CARTES = `/home/user/controle-ia-travail/archives-reponses-modeles/auto-conception-course-v9-2026-11-19-v1/course-v9-sortie/sortie/generation-1/fiches.json` (le seul chemin permis).

1. `env -C PROG sha256sum -c mandat-executant-jeu-noms-cles-contenu-v1.md.sha256` (ce mandat), puis `env -C PROG sha256sum -c noms_cles_contenu_hors_champs_v1.py.sha256` : l'empreinte doit valoir `26eeaa798e14c716bbe4bd0c323e797e60470459d9a13b804ccacb07ea121120` ; sinon arrête-toi.
2. `python3 -B /home/user/controle-ia-travail/scripts/verifier_environnement_agent_v1.py`.
3. `git -C /home/user/controle-ia-travail fetch origin main`, puis `git -C /home/user/controle-ia-travail show origin/main:prereg/organisme-auto-conception-v9/juge-selection/rejeu-v1/configuration-a-masque-v1.json > JEU/configuration-a-masque-v1.json`, puis `sha256sum JEU/configuration-a-masque-v1.json` : doit valoir `8a8548d1444bfe3ab85396b3913c2d1b018a32541e9a283bd3f9b517a6332ce4` ; sinon arrête-toi. Tu ne l'ouvres pas.
4. `test -f CARTES` : le seul geste permis sur ce chemin hors du programme. Code non nul : arrête-toi sans jouer.
5. **Le jeu, une seule fois, jamais relancé** : `python3 -B PROG/noms_cles_contenu_hors_champs_v1.py --fiches CARTES --configuration JEU/configuration-a-masque-v1.json --sortie JEU/noms-cles-contenu-hors-champs-v1.json` (chemins absolus). Note la sortie écran telle quelle et le code de retour (par le retour de l'outil, sans rien ajouter à la commande).
6. Si « FAIT » : `env -C JEU sha256sum -c noms-cles-contenu-hors-champs-v1.json.sha256`, puis lis le fichier de sortie (trois champs : `cles_hors_champs`, `nombre_de_cartes`, `empreintes`). Si « REFUS » : rien d'autre, tu rends.

Rends `compte-rendu-jeu-noms-cles-contenu-v1.md` dans JEU, avec son compagnon (`env -C JEU sha256sum F`, redirigé vers `JEU/F.sha256`) : heure (`date -u`), commandes exactes, codes de retour, sortie écran, les trois champs du résultat recopiés tels quels. Aucune valeur ni aucun identifiant de carte ne peut y figurer (le programme n'en rend pas).

## Interdits

Voir en tête. Aucun autre chemin sous `archives-reponses-modeles/`. Tu n'ouvres, ne copies ni ne hashes toi-même le fichier des cartes. Jamais de heredoc ni de code en ligne passé à un interpréteur. Aucune écriture dans le dépôt, aucun commit. Rien sous `/root/.claude/`. Jamais le nom d'une commande d'arrêt ou de recherche de processus par motif. Aucun appel à un fournisseur de modèles, aucune dépense. Aucun identifiant de modèle. Au premier refus de permission, de classifieur ou de garde : arrête-toi et dis-le.
