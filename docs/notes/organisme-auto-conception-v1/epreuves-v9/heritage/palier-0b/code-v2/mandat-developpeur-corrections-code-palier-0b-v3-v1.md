VERSION DE PYTHON : `python3 --version` ; AUCUN `-c`, AUCUN `-` APRÈS PYTHON3

AUCUNE COMMANDE DE LISTE : NI `ls`, NI `find`, NI `git ls-tree`, NI `git ls-files`, NI `git status`, NI `grep -r`, NI RECHERCHE SUR UN DOSSIER ENTIER, NI JOKER DANS UN CHEMIN. TOUT FICHIER S'OUVRE PAR SON CHEMIN COMPLET, DONNÉ CI-DESSOUS OU PAR LA TABLE DU § 7 DU RAPPORT DU CODE V2. UNE COMMANDE SIMPLE PAR APPEL : NI `&&`, NI `;`, NI BOUCLE.

# Mandat du développeur — corrections C1 à C3 du code de l'étage sur processeur du palier 0b (code v3) — v1

Pièce de travail (classe C). Donné par la session du compte organisme le 2026-11-20. Code par un développeur de modèle L′ ; il garde l'objet et les interdits du mandat v2 (`/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/mandat-developpeur-code-palier-0b-v2.md`, `024e94e5…`). Dossier du code v2 : `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/code-v2/` (noté V2).

## Ce qui fait foi

- Le préenregistrement v6 : `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/preenregistrement-heritage-palier-0b-etage-processeur-v6.md` (`4aee136b…`).
- La contre-lecture : `V2/contre-lecture-v1/contre-lecture-code-palier-0b-v2-v1.md` (`3778fb395dae1e2003ce8236f93c77cfbd6bc78c355417bf0b40e0b5e694c5e5`), verdict « Conforme après corrections » : **C1** (essai « aucune graine décisive » qui échoue lancé seul), **C2** (bras 4b sans vérification d'empreinte de la copie étrangère servie : empreinte, artefact, entrée au banc des défauts), **C3** (`Mondes.__init__` plus exigeant que `frequences.strates_requises` : aligner). Les notes D4 à D9 : tu peux traiter celles qui ne touchent que le code et ne changent aucun résultat (déclare-le) ; les autres restent pour l'erratum.
- Le code v2 et son rapport : `V2/rapport-developpeur-code-palier-0b-v2.md` (`ca61bf7e…`), `V2/src/`, `V2/tests/`, `V2/outils-dev/`.

## Ce que tu fais

1. Copie le code v2 dans ton bloc-notes (`cp -r V2/src BLOC/src`, de même `tests` et `outils-dev`), applique C1, C2, C3 ; R12 : les fichiers changés gardent leur nom de module (le paquet est versionné par son dossier), et le dossier rendu est `code-v3/`.
2. Essais : `python3 -B -m pytest -q -p no:cacheprovider CHEMIN` avec `PYTHONPATH=src`, chaque fichier lancé seul **et** la suite entière ; le fichier « aucune graine décisive » passe dans les deux cas. Le banc des défauts (`outils-dev/mutations_v1.py`, en version neuve `mutations_v2.py` avec l'entrée de C2) rejoué en entier ; dis combien sont vus. Un calcul long en tâche de fond, arrêté au besoin par l'outil de tâches.
3. Rapport `code-v3/rapport-developpeur-code-palier-0b-v3.md` : correction par correction, différentiel par fichier (`diff -u`), essais, défauts vus, table des empreintes ; aucun écart au texte tranché (les trois écarts B7 bis, présentation, doses par paires vont à l'erratum).

Ton bloc-notes : `/tmp/claude-0/-home-user-controle-ia-travail/227b647d-2ece-5654-bf04-8493b3ed2f19/scratchpad/dev-palier-0b-v3/`. Chaque fichier rendu avec son compagnon (`env -C DOSSIER sha256sum F`, redirigé vers `DOSSIER/F.sha256`). Le dossier courant n'est pas gardé : `env -C DOSSIER commande`.

## Interdits

Voir en tête. **Jamais de heredoc ni de bloc de texte ou de code en ligne passé à un interpréteur, même vide.** Aucun tirage décisif, aucun étalonnage, aucun audit à pleine taille. Aucun appel à un fournisseur de modèles, aucune dépense, aucune machine, aucun réseau sauf `git fetch`/`git show` du dépôt (redirigé vers un fichier). Aucune écriture dans le dépôt, aucun commit. Rien sous `archives-reponses-modeles/`, rien sous `/root/.claude/`. Jamais le nom d'une commande d'arrêt ou de recherche de processus par motif. Aucune valeur de clé. Aucun identifiant de modèle ; signe « développeur, modèle L′ ». Au premier refus d'un outil : arrête-toi et dis-le.
