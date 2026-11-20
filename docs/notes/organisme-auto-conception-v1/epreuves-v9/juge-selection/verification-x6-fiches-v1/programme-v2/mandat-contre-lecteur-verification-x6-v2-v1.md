VERSION DE PYTHON : `python3 --version` ; AUCUN `-c`, AUCUN `-` APRÈS PYTHON3

AUCUNE COMMANDE DE LISTE : NI `ls`, NI `find`, NI `git ls-tree`, NI `git ls-files`, NI `git status`, NI `grep -r`, NI RECHERCHE SUR UN DOSSIER ENTIER, NI JOKER DANS UN CHEMIN. TOUT FICHIER S'OUVRE PAR SON CHEMIN COMPLET. UNE COMMANDE SIMPLE PAR APPEL : NI `&&`, NI `;`, NI BOUCLE. `git show` TOUJOURS REDIRIGÉ VERS UN FICHIER. AUCUNE RECHERCHE DE MOTIF LARGE.

# Mandat du contre-lecteur — programme de vérification X6, version 2 — v1

Pièce de travail (classe C). Donné par la session du compte organisme le 2026-11-20. Tu es un agent neuf : tu n'as écrit ni le programme, ni ses essais, ni le mandat du développeur. Dossier : `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/juge-selection/verification-x6-fiches-v1/` (noté X6).

## Ce qui fait foi (vérifie chaque empreinte contre son compagnon)

- Le mandat du développeur : `X6/mandat-developpeur-verification-x6-fiches-v1.md` (contrat du programme : trois champs de sortie, empreintes avant décodage, aucun identifiant ni valeur affichés ou écrits, constantes gelées, aucune option d'essai en ligne de commande).
- Le compte rendu du jeu raté du v1 : `X6/compte-rendu-jeu-verification-x6-v1.md` (cause : le chemin `extraction.identifiants_par_classe.a_corriger` lu sous la clé racine `extraction`).
- Le v2 : `X6/programme-v2/verifier_x6_contre_fiches_v2.py` (`91833df0…`), `X6/programme-v2/essais_verifier_x6_contre_fiches_v2.py` (`ddc992d2…`), `X6/programme-v2/rapport-developpeur-verification-x6-v2.md` (`b7ad0d61…`).
- Pour comparaison : le v1 et sa contre-lecture dans `X6/` (`verifier_x6_contre_fiches_v1.py`, `contre-lecture-verification-x6-v1.md`).

## Ce que tu vérifies

1. Le chemin lu est bien `objet["extraction"]["identifiants_par_classe"]["a_corriger"]`, avec un refus propre à chaque niveau mal formé ; deux identifiants exactement, distincts.
2. L'ordre : sortie absente, puis empreintes des deux fichiers sur les octets avant tout décodage, puis extraction décodée et validée, puis cartes décodées (clés seulement). Un refus de l'extraction ne décode jamais les cartes.
3. Les constantes gelées sont inchangées par rapport au v1 ; le point d'entrée n'accepte que les constantes ; aucune option d'essai.
4. Aucun identifiant ni aucune valeur n'est écrit ou affiché, ni en cas de succès ni en cas de refus (lis chaque message de refus).
5. La sortie : trois champs exactement, compagnon `.sha256`, refus si la sortie ou son compagnon existe.
6. Les essais : lance-les par `env -C X6/programme-v2 python3 -B -m pytest -q -p no:cacheprovider essais_verifier_x6_contre_fiches_v2.py` (avec le chemin complet de X6) ; dis le nombre passé. Fais au moins trois mutations à la main sur une **copie** du programme dans ton dossier (par exemple : chemin à un niveau, ordre cartes avant extraction, identifiant dans un message de refus) et dis si un essai les attrape.
7. Que l'essai de « forme réelle » colle bien à ce que dit le compte rendu (clé racine `extraction`) ; tu n'ouvres pas l'extraction réelle.

Rends `contre-lecture-verification-x6-v2-v1.md` : verdict « Conforme » ou « À corriger » avec corrections numérotées, et la commande unique de jeu.

Ton dossier : `/tmp/claude-0/-home-user-controle-ia-travail/227b647d-2ece-5654-bf04-8493b3ed2f19/scratchpad/contre-lecture-verification-x6-v2/`. Chaque fichier rendu avec son compagnon (`env -C DOSSIER sha256sum F`, redirigé vers `DOSSIER/F.sha256`).

## Interdits

Voir en tête. **Tu ne touches ni au fichier des cartes, ni à l'extraction réelle, ni à aucun chemin sous `archives-reponses-modeles/`, par aucune commande, même une empreinte. Tu ne joues pas le programme sur les vrais fichiers.** Jamais de heredoc ni de code en ligne passé à un interpréteur. Aucune écriture dans le dépôt, aucun commit. Rien sous `/root/.claude/`. Jamais le nom d'une commande d'arrêt ou de recherche de processus par motif. Aucun appel à un fournisseur de modèles, aucune dépense. Aucun identifiant de modèle ; signe « contre-lecteur, modèle S ». Au premier refus de permission, de classifieur ou de garde : arrête-toi et dis-le.
