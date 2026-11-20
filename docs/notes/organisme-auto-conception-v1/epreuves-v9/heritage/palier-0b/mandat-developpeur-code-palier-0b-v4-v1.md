VERSION DE PYTHON : `python3 --version` ; AUCUN `-c`, AUCUN `-` APRÈS PYTHON3

AUCUNE COMMANDE DE LISTE : NI `ls`, NI `find`, NI `git ls-tree`, NI `git ls-files`, NI `git status`, NI `grep -r`, NI RECHERCHE SUR UN DOSSIER ENTIER, NI JOKER DANS UN CHEMIN. TOUT FICHIER S'OUVRE PAR SON CHEMIN COMPLET, DONNÉ CI-DESSOUS OU PAR LA TABLE DU RAPPORT DU CODE V3. UNE COMMANDE SIMPLE PAR APPEL : NI `&&`, NI `;`, NI BOUCLE.

# Mandat du développeur — code de l'étage sur processeur du palier 0b, version 4 (préenregistrement v8) — v1

Pièce de travail (classe C). Donné par la session du compte organisme le 2026-11-20, sur GO-2026-11-20-11 (R-4083 : palier 0b v8, nœud 1 (a), nœud 2 (a) limité aux trois audits par dose, dose 0,25 du jeu de la garde 27 (a)). Code par un développeur de modèle L′ ; il garde l'objet et les interdits des mandats v2 et v3. Dossier : `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/` (noté P0B).

## Ce qui fait foi

- Le texte : `P0B/preenregistrement-heritage-palier-0b-etage-processeur-v8.md` (`fd275af81704997f2844e4ee9fdb68c5401658335221ea0768f70e3cdac9586c`), contrôlé (`P0B/controle-differentiel-palier-0b-v8-v1.md`, `a68a46a0…`, tenue seulement, dont la correction T5 du point 2 du code v4) ; sa liste « Ce qui demande un code v4 » (annexe H et rapport `P0B/rapport-redacteur-palier-0b-v8-v1.md`) fait foi pour le périmètre.
- Le code v3 : `P0B/code-v3/` (rapport `5e3fa3e8…`, table des empreintes), sa vérification `P0B/code-v3/verification-v1/verification-corrections-code-palier-0b-v3-v1.md`.
- Les contrôles de la v7 et de la v8 (`P0B/controle-differentiel-palier-0b-v7-v1.md`, `1211fed3…`, § 10 ; et le précédent), pour les remarques sur le code (exactitude « non calculée » qui arrête ; jeu de la garde 27 hors de l'étape 4 ; fuite possible entre mondes frères, à rapporter).

## Ce que tu fais

Le code v4 sous `code-v4/` de ton bloc-notes (même arborescence que `code-v3/`) : chaque point de la liste « Ce qui demande un code v4 » de la v8, dont
- `audit.py` et l'étape 3 : longueur de forme sur le texte aux nombres remplacés par leur jeton, longueur brute au contenu (nœud 1) ; σ₀ par 1 000 permutations et la règle calibrée pour les trois seuls audits par dose, les deux audits de lois à la lettre de la v6 (nœud 2) ; arrêt sur un pli privé d'une classe (D9) ; arrêt sur une exactitude non calculable ;
- `graines.py` et `constantes.py` : le verrou (D6), avec le fichier d'autorisation tel que la v8 le définit, ou un arrêt motivé si la v8 ne le définit pas assez ;
- `etalonnage.py` : D8 ; `tirages.py` : la liste des étiquettes dans un fichier scellé (choix 12) ;
- le jeu de la garde 27 : où il se joue, à la dose 0,25 fixée par une constante.
Chaque changement a un essai sain et un artefact (R5) et un défaut au banc (`mutations_v3.py`, rejoué en entier) ; chaque fichier d'essais passe seul et en suite ; l'essai final « aucune graine décisive » passe ; les sorties du v3 qui ne relèvent pas d'une règle changée restent égales à l'octet (dis lesquelles changent, et pourquoi). Rapport `code-v4/rapport-developpeur-code-palier-0b-v4.md` avec table des empreintes et différentiels v3 → v4. Rien de la v8 n'est tranché par toi : un silence du texte se déclare.

Ton bloc-notes : `/tmp/claude-0/-home-user-controle-ia-travail/227b647d-2ece-5654-bf04-8493b3ed2f19/scratchpad/dev-palier-0b-v4/`. Chaque fichier rendu avec son compagnon (`env -C DOSSIER sha256sum F`, redirigé vers `DOSSIER/F.sha256`). Le dossier courant n'est pas gardé : `env -C DOSSIER commande`. Essais : `python3 -B -m pytest -q -p no:cacheprovider CHEMIN` avec `PYTHONPATH=src` ; calcul long en tâche de fond. Règle R-4067 pour l'outil de remplacement.

## Interdits

Voir en tête. **Jamais de heredoc ni de bloc de texte ou de code en ligne passé à un interpréteur, même vide.** Aucun tirage décisif, aucun étalonnage, aucun audit à pleine taille. Aucun appel à un fournisseur de modèles, aucune dépense, aucune machine, aucun réseau sauf `git fetch`/`git show` du dépôt (redirigé vers un fichier). Aucune écriture dans le dépôt, aucun commit. Rien sous `archives-reponses-modeles/`, rien sous `/root/.claude/`. Jamais le nom d'une commande d'arrêt ou de recherche de processus par motif. Aucune valeur de clé. Aucun identifiant de modèle ; signe « développeur, modèle L′ ». Au premier refus de permission, de classifieur ou de garde : arrête-toi et dis-le.
