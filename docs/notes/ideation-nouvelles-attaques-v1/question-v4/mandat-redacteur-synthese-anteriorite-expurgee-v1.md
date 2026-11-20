VERSION DE PYTHON : `python3 --version` ; AUCUN `-c`, AUCUN `-` APRÈS PYTHON3

AUCUNE COMMANDE DE LISTE : NI `ls`, NI `find`, NI `git ls-tree`, NI `git ls-files`, NI `git status`, NI `git show --name-only`, NI `grep -r`, NI RECHERCHE SUR UN DOSSIER ENTIER, NI JOKER DANS UN CHEMIN. TOUT FICHIER S'OUVRE PAR SON CHEMIN COMPLET. UNE COMMANDE SIMPLE PAR APPEL : NI `&&`, NI `;`, NI BOUCLE. `git show` TOUJOURS REDIRIGÉ VERS UN FICHIER PAR `>`, SUR `origin/main`. AUCUNE RECHERCHE DE MOTIF LARGE.

# Mandat du rédacteur — synthèse d'antériorité servie, version expurgée pour la course « nouvelles attaques » — v1

Pièce de travail (classe C), donnée par la session du compte organisme le 2026-11-20, sur le mot du directeur (11:24Z, nœud 3 : « go reco ») : la synthèse d'antériorité servie aux espèces, `rapports/fille-ideation-1-v1/synthese-anteriorite-pilier-attaque-v2b.md` (sur main, `b828d800…`), porte le prénom du directeur (l. 258, 304), des identifiants de registre (R-…, N-…), des chemins du dépôt, une empreinte, des noms de fournisseurs ou de familles de modèles (l. 5, 258, 260, 266, 306, 309) et des noms de clés (l. 5, 212, 260). Une version neuve, expurgée, doit exister avant toute course. Ensuite : contre-lecture par un autre modèle, scellement par la mère.

## Qui

Un rédacteur neuf, modèle F, qui n'a écrit ni la synthèse, ni la question, ni l'ordre de course. Tu signes « rédacteur neuf, modèle F ».

## Ce qui fait foi

- La synthèse v2b, tirée de `origin/main` par `git -C /home/user/controle-ia-travail fetch origin main` puis `git … show origin/main:rapports/fille-ideation-1-v1/synthese-anteriorite-pilier-attaque-v2b.md > TON_DOSSIER/synthese-v2b.md` ; empreinte vérifiée (`b828d800…`, entière dans son compagnon sur main).
- Le relevé du contre-lecteur de la question v4 : `/home/user/controle-ia-travail/docs/notes/ideation-nouvelles-attaques-v1/question-v4/contre-lecture-v1/sortie-releve-motifs-synthese-anteriorite-v1.txt` et `…/contre-lecture-question-v4-v1.md` (remarque 9).
- L'outil `/home/user/controle-ia-travail/scripts/remplacer_texte_exact_v1.py` (`391db990…`).

## Ce que tu écris

1. `synthese-anteriorite-pilier-attaque-v3-servie.md` (nom neuf ; la v2b reste intacte), à partir de la v2b, par l'outil contre-lu, un JSON écrit avec l'outil d'écriture de fichiers, chaque ancre comptée par `grep -c -F -e` avant l'appel (R-4067). Elle porte, et rien d'autre : le prénom du directeur → « le directeur du programme » ; identifiants de registre, chemins du dépôt, empreintes, noms de clés retirés ou remplacés par une description neutre ; noms de fournisseurs et de familles de modèles remplacés par une désignation neutre (« un modèle d'une autre lignée », « espèce n ») sauf s'ils font partie d'une référence bibliographique publique (auteurs, titre) : dis-le cas par cas. **Aucune idée, aucune antériorité, aucune référence publique ne change de sens.**
2. Par un programme à toi (outil d'écriture de fichiers, lancé par son chemin), un relevé des motifs du contre-lecteur sur la v3 (prénom et nom du directeur, `session_`, `@`, `R-` et `N-` suivis de chiffres, `GO-20`, `lciric`, `github`, `controle-ia`, `docs/`, `prereg/`, `registres/`, `donnees/`, empreintes hexadécimales de 16 caractères et plus, `CLAUDE.md`, noms de clés en majuscules terminés par `_KEY` ou `_TOKEN`) : 0 attendu, sortie écrite.
3. Le différentiel `diff -u` v2b → v3, et un rapport court `rapport-redacteur-synthese-anteriorite-v3-servie-v1.md` (relevé avant, remplacements, relevé après, remarques).

Ton dossier : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/redacteur-synthese-anteriorite-v3/`. Chaque fichier rendu avec son compagnon (`env -C DOSSIER sha256sum F`, redirigé vers `DOSSIER/F.sha256`).

## Interdits

Voir en tête. **Aucune méthode d'attaque, aucun procédé, aucun détail opérant ; aucune recette** ; tu n'ajoutes rien au fond. Aucune valeur de clé. Aucune écriture dans le dépôt, aucun commit. Rien sous `archives-reponses-modeles/`, rien du coffre, rien sous `/root/.claude/`. Jamais de heredoc ni de code en ligne passé à un interpréteur. Aucun appel à un fournisseur de modèles, aucune dépense, aucune publication d'artefact. Aucun identifiant de modèle. Au premier refus de permission, de classifieur ou de garde : arrête-toi et dis-le.
