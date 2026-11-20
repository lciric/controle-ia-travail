VERSION DE PYTHON : `python3 --version` ; AUCUN `-c`, AUCUN `-` APRÈS PYTHON3

AUCUNE COMMANDE DE LISTE : NI `ls`, NI `find`, NI `git ls-tree`, NI `git ls-files`, NI `git status`, NI `git show --name-only`, NI `grep -r`, NI RECHERCHE SUR UN DOSSIER ENTIER, NI JOKER DANS UN CHEMIN. TOUT FICHIER S'OUVRE PAR SON CHEMIN COMPLET, DONNÉ CI-DESSOUS OU PAR LA TABLE DES EMPREINTES DU RAPPORT DU CODE V4. UNE COMMANDE SIMPLE PAR APPEL : NI `&&`, NI `;`, NI BOUCLE. `git show` TOUJOURS REDIRIGÉ VERS UN FICHIER PAR `>`, SUR `origin/main` ET NON SUR `FETCH_HEAD`.

# Mandat du développeur — code de l'étage sur processeur du palier 0b, version 5 (préenregistrement v11) — v1

Pièce de travail (classe C), donnée par la session du compte organisme le 2026-11-20, sur GO-2026-11-20-25, GO-2026-11-20-41 et les décisions de la mère R-4123, R-4182 et R-4210 (NE-3 retenu). Pièce d'instrument (classe B) : contre-lue par un autre modèle, vérification des corrections par le même ; puis erratum du commit au texte, contre-lu, et scellement par la mère. Dossier P0B = `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/`.

## Qui

Un développeur neuf, modèle O, qui n'a écrit ni le texte, ni le code v1 à v4, ni leurs vérifications. Tu signes « développeur, modèle O ».

## Ce qui fait foi (vérifie chaque empreinte contre son compagnon, `env -C DOSSIER sha256sum -c F.sha256`)

- Le texte : `P0B/preenregistrement-heritage-palier-0b-etage-processeur-v11.md` (`9faf31a3dd0278b562c62fbded81222b674f6c5df225006f9e0e8d610b720989`), contrôlé « Conforme » (`P0B/controle-v11/controle-differentiel-palier-0b-v10-v11-v1.md`, `88c37d86…`). Sa liste **« Ce qui demande un code v5 »**, points 1 à 7, fait foi pour le périmètre, à la lettre ; la section « Seuil », la garde 25, la garde 27 et B8 pour le détail.
- **NE-3**, retenu par la mère (R-4210), à coder : à la table de l'étape 3, une colonne de plus porte le seuil d'arrêt, le plus grand de 0,55 et de M + 2 σ₀ (texte au § « Réserve 3 » du contrôle de la v11).
- Le code v4 : `P0B/code-v4/` (rapport `P0B/code-v4/rapport-developpeur-code-palier-0b-v4.md`, `2947c4f1…`, et sa table des empreintes), sa vérification `P0B/verification-code-palier-0b-v4-v1.md` (`183b17d2…`).
- Les contrôles v8 → v9, v9 → v10, v10 → v11 (`P0B/contre-lecture-v9/`, `P0B/controle-v10/`, `P0B/controle-v11/`) pour les essais et défauts recommandés (égalité A = M + 2 σ₀ ; plis observés tirés du générateur des permutations ; garde 27 à trois sources avec le défaut « source précédente au lieu de suivante » ; arrêt sur une exactitude au plus 0,55).

## Ce que tu fais

Le code v5 sous `code-v5/` de ton bloc-notes (même arborescence que `code-v4/`, copiée puis modifiée ; le v4 n'est pas touché) : chaque point 1 à 6 de la liste « Ce qui demande un code v5 » de la v11, et NE-3 ; rien d'autre (point 7 : sans changement). Chaque changement a un essai sain et un artefact (R5) et un défaut au banc des défauts (rejoué en entier) ; chaque fichier d'essais passe seul et en suite ; l'essai final « aucune graine décisive » passe ; les sorties du v4 qui ne relèvent pas d'une règle changée restent égales à l'octet (dis lesquelles changent, et pourquoi). Rapport `code-v5/rapport-developpeur-code-palier-0b-v5.md` avec table des empreintes, différentiels v4 → v5, et la liste exacte de ce que l'erratum du commit devra inscrire au texte. **Rien du texte n'est tranché par toi** : un silence se déclare, en remarque.

Ton bloc-notes : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/dev-palier-0b-v5/`. Chaque fichier rendu avec son compagnon (`env -C DOSSIER sha256sum F`, redirigé vers `DOSSIER/F.sha256`). Le dossier courant n'est pas gardé : `env -C DOSSIER commande`. Essais : `env -C DOSSIER /home/user/controle-ia-travail/.venv/bin/python -B -m pytest -q -p no:cacheprovider CHEMIN` avec `PYTHONPATH=src` ; calcul long en tâche de fond. Règle R-4067 pour l'outil de remplacement.

## Interdits

Voir en tête. **Jamais de heredoc ni de bloc de texte ou de code en ligne passé à un interpréteur, même vide.** Aucun tirage décisif, aucun étalonnage, aucun audit à pleine taille. Aucun appel à un fournisseur de modèles, aucune dépense, aucune machine, aucun réseau sauf `git fetch`/`git show` du dépôt (redirigé vers un fichier). Aucune écriture dans le dépôt, aucun commit. Rien sous `archives-reponses-modeles/`, rien sous `/root/.claude/`. Jamais le nom d'une commande d'arrêt ou de recherche de processus par motif. Aucune valeur de clé. Aucun identifiant de modèle. Au premier refus de permission, de classifieur ou de garde : arrête-toi et dis-le.
