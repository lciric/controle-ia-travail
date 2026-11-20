VERSION DE PYTHON : `python3 --version` ; AUCUN `-c`, AUCUN `-` APRÈS PYTHON3

AUCUNE COMMANDE DE LISTE : NI `ls`, NI `find`, NI `git ls-tree`, NI `git ls-files`, NI `git status`, NI `grep -r`, NI RECHERCHE SUR UN DOSSIER ENTIER, NI JOKER DANS UN CHEMIN. TOUT FICHIER S'OUVRE PAR SON CHEMIN COMPLET. UNE COMMANDE SIMPLE PAR APPEL : NI `&&`, NI `;`, NI BOUCLE. `git show` TOUJOURS REDIRIGÉ VERS UN FICHIER. AUCUNE RECHERCHE DE MOTIF LARGE.

# Mandat de l'exécutant — second et unique jeu du programme de vérification X6, version 2 — v1

Pièce de travail (classe C). Donnée par la session du compte organisme le 2026-11-20, sur GO-2026-11-20-23 (« go a », R-4114) et la lecture de la mère (R-4122 : ce GO vise ce seul fichier ; second jeu unique par un agent neuf, mêmes sorties, même arrêt). Tu es un agent neuf : tu n'as écrit ni le programme, ni ses essais, ni sa contre-lecture, et tu n'as pas joué le v1.

## Ce qui fait foi (vérifie chaque empreinte contre son compagnon, par `sha256sum -c` lancé avec `env -C` dans le dossier)

Dossier P = `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/juge-selection/verification-x6-fiches-v1/programme-v2/`.
- Le programme : `P/verifier_x6_contre_fiches_v2.py`, empreinte exacte `91833df0e8e2ef54a7536d5fa1d23a6ac77e065cfb8e0da34979581243b44de5`.
- Sa contre-lecture « Conforme » : `P/contre-lecture-verification-x6-v2-v1.md` (`5aa144b8…`).
- Le compte rendu du jeu raté du v1 : `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/juge-selection/verification-x6-fiches-v1/compte-rendu-jeu-verification-x6-v1.md`.

## Ce que tu fais, dans cet ordre

1. `python3 -B /home/user/controle-ia-travail/scripts/verifier_environnement_agent_v1.py`.
2. Copie le programme dans ton dossier : `cp P/verifier_x6_contre_fiches_v2.py TON_DOSSIER/programme/` (dossier à créer par `mkdir -p`), puis vérifie l'empreinte de la copie (exactement la valeur ci-dessus ; sinon arrête-toi).
3. L'extraction : `git -C /home/user/controle-ia-travail fetch origin main`, puis `git -C /home/user/controle-ia-travail show origin/main:docs/notes/organisme-auto-conception-v9-mere/juge-selection-x6-v1/sortie-extraction-x6-v2.json`, redirigé vers `TON_DOSSIER/entree/sortie-extraction-x6-v2.json`. **Tu ne l'ouvres pas.** Le programme vérifie lui-même son empreinte.
4. Le fichier des cartes : `/home/user/controle-ia-travail/archives-reponses-modeles/auto-conception-course-v9-2026-11-19-v1/course-v9-sortie/sortie/generation-1/fiches.json`. Le seul geste permis sur ce chemin avant le jeu est `test -f CHEMIN` (une commande, ce seul chemin). S'il n'existe pas : tu t'arrêtes, sans jouer, et tu le dis. **Tu ne l'ouvres, ne le copies, ne le hashes pas toi-même.** Aucun autre chemin sous `archives-reponses-modeles/`.
5. Le jeu, **une seule fois**, jamais relancé, quel qu'en soit le résultat : `env -C TON_DOSSIER/programme python3 -B verifier_x6_contre_fiches_v2.py --fiches CHEMIN_DES_CARTES --extraction TON_DOSSIER/entree/sortie-extraction-x6-v2.json --sortie TON_DOSSIER/sortie/resultat-verification-x6-v2.json` (chemins absolus ; `mkdir -p TON_DOSSIER/sortie` avant). Note la sortie écran et le code de retour.
6. Si « FAIT » : `env -C TON_DOSSIER/sortie sha256sum -c resultat-verification-x6-v2.json.sha256`, puis lis le résultat (trois champs : `nombre_de_cles`, `retenues_presentes`, `empreintes`). **Si `nombre_de_cles` ne vaut pas 94, ou si une retenue est présente : tu le dis en tête de ton compte rendu et tu ne fais rien d'autre.**

Rends un compte rendu `compte-rendu-second-jeu-verification-x6-v1.md` dans ton dossier, avec son compagnon (`env -C DOSSIER sha256sum F`, redirigé vers `DOSSIER/F.sha256`) : heure (`date -u`), commandes exactes, codes de retour, sortie écran, les trois champs du résultat recopiés tels quels. Jamais un identifiant ni une valeur de carte.

Ton dossier : `/tmp/claude-0/-home-user-controle-ia-travail/227b647d-2ece-5654-bf04-8493b3ed2f19/scratchpad/second-jeu-verification-x6/`.

## Interdits

Voir en tête. Jamais de heredoc ni de code en ligne passé à un interpréteur. Aucune écriture dans le dépôt, aucun commit. Rien sous `/root/.claude/`. Jamais le nom d'une commande d'arrêt ou de recherche de processus par motif. Aucun appel à un fournisseur de modèles, aucune dépense. Aucun identifiant de modèle ; signe « exécutant neuf, modèle S ». Au premier refus de permission, de classifieur ou de garde : arrête-toi et dis-le.
