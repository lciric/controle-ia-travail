VERSION DE PYTHON : `python3 --version` ; AUCUN `-c`, AUCUN `-` APRÈS PYTHON3 SAUF `-B`

AUCUNE COMMANDE DE LISTE : NI `ls`, NI `find`, NI `git ls-tree`, NI `git ls-files`, NI `git status`, NI `git show --name-only`, NI `grep -r`, NI RECHERCHE SUR UN DOSSIER ENTIER, NI JOKER DANS UN CHEMIN. TOUT FICHIER S'OUVRE PAR SON CHEMIN COMPLET. UNE COMMANDE SIMPLE PAR APPEL : NI `&&`, NI `;`, NI BOUCLE, NI SUBSTITUTION DE PROCESSUS. TOUTE REDIRECTION VERS UN CHEMIN COMPLET DE TON DOSSIER.

# Mandat du rédacteur — préenregistrement du palier 0b, brouillon v19 (deux corrections de cohérence du contrôle de la v18) — BROUILLON, EN ATTENTE DU MOT DE LAZAR — v1

Pièce de travail (classe C), donnée par la session du compte organisme le 2026-11-20. Le contrôle de la v18 dit « À corriger » pour deux corrections de cohérence (Y1, Y2), sans effet sur aucune règle. Leur application relève de la routine : elle ne demande aucune décision neuve de la mère. **La v13 scellée (`d9591d5b…`) reste le texte en vigueur. La v18 n'est pas touchée. Rien n'est scellé avant le mot de Lazar.**

## Qui

Le rédacteur des v15 à v18 (modèle F). Tu signes « rédacteur des v15 à v19, modèle F ».

## Ce qui fait foi (vérifie chaque empreinte contre son compagnon)

Dossier P = `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/`.
- **Source** : la v18, `P/brouillon-v18/preenregistrement-heritage-palier-0b-etage-processeur-v18.md` (`ae1e8f56c06c8153bb09fa8503f3136773615132d9ce95c6fb3775aecea29876`).
- **Le contrôle de la v18** : `P/brouillon-v18/controle-v1/controle-palier-0b-v18-v1.md` (`e2aed461…`), et son jeu Y1–Y2 : `P/brouillon-v18/controle-v1/corrections-palier-0b-v18-v1.json` (`88e8b4fa…`).

## Ce que la v19 porte, et rien d'autre

Nom neuf : `preenregistrement-heritage-palier-0b-etage-processeur-v19.md`. Tu passes par l'outil contre-lu (`python3 -B /home/user/controle-ia-travail/scripts/remplacer_texte_exact_v1.py`, `391db990…`), en passes nommées. Avant chaque appel, tu comptes chaque ancre par `grep -c -F -e`.

- **Passe 1 — le jeu Y1–Y2 tel quel** sur la v18 ; la sortie doit être égale à l'essai du contrôleur (`d54b6e53…`). Sinon, arrête-toi et dis-le.
- **Passe 2 — tenue** : titre ; statut « BROUILLON, non scellé, en attente du mot de Lazar » ; date par `date -u` ; ligne de version ; section « Contre-lecture » ; alinéa « Version 19 » de l'annexe H, qui dit seulement que les deux phrases de « Version 14 » sont rangées par un renvoi.

Ensuite :
- le différentiel `diff -u` de v18 à v19 ;
- les comptes d'en-tête : une seule ligne « - Commit du code d'analyse : », `COMMIT_V6` en blanc, table de 64 lignes en premier bloc ;
- les lieux des trois empreintes entières des programmes ;
- un rapport court, `rapport-redacteur-palier-0b-v19-v1.md`.

Ton dossier : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/redacteur-palier-0b-v19/`. Chaque fichier a son compagnon.

## Interdits

Voir en tête. Jamais de heredoc ni de code en ligne passé à un interpréteur. Aucun lancement d'un programme ni du code, aucun essai, aucun tirage, aucune pièce d'autorisation ni de contrôle. Aucune écriture dans le dépôt, aucun commit. Rien sous `archives-reponses-modeles/`, rien sous `/root/.claude/`. Jamais le nom d'une commande d'arrêt ou de recherche de processus, même sans motif. Aucun appel à un fournisseur de modèles, aucune dépense, aucune publication d'artefact. Aucun identifiant de modèle. Au premier refus de permission, de classifieur ou de garde : arrête-toi et dis-le.
