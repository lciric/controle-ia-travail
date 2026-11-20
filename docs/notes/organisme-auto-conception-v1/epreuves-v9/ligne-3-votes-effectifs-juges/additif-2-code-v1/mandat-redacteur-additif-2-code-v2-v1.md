VERSION DE PYTHON : `python3 --version` ; AUCUN `-c`, AUCUN `-` APRÈS PYTHON3

AUCUNE COMMANDE DE LISTE : NI `ls`, NI `find`, NI `git ls-tree`, NI `git ls-files`, NI `git status`, NI `grep -r`, NI RECHERCHE SUR UN DOSSIER ENTIER, NI JOKER DANS UN CHEMIN. TOUT FICHIER S'OUVRE PAR SON CHEMIN COMPLET. UNE COMMANDE SIMPLE PAR APPEL : NI `&&`, NI `;`, NI BOUCLE. AUCUNE RECHERCHE DE MOTIF LARGE.

# Mandat du rédacteur — additif 2 (code) de la ligne 3, version 2 (corrections A, B, C) — v1

Pièce de travail (classe C). Donné par la session du compte organisme le 2026-11-20. Dossier : `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-3-votes-effectifs-juges/additif-2-code-v1/` (noté A2).

## Qui

Un rédacteur neuf, modèle F. Tu signes « rédacteur neuf, modèle F ».

## Ce qui fait foi (vérifie chaque empreinte contre son compagnon)

- La contre-lecture : `A2/contre-lecture-additif-2-code-ligne-3-v1.md` (`7cf5a2c99e678ab0c3a3580121ac1d2be388cfcbf22fc959958cd3ec2546fc41`), corrections **A** et **B** obligatoires, **C** facultative, texte exact dans la pièce.
- L'additif v1 : `A2/additif-2-code-preenregistrement-ligne-3-votes-effectifs-juges-v7-v1.md` (`65609405…`) et son rapport `A2/rapport-redacteur-additif-2-code-ligne-3-v1.md`.

## Ce que tu fais

1. A, B et C **à la lettre**, par l'outil contre-lu (`python3 -B /home/user/controle-ia-travail/scripts/remplacer_texte_exact_v1.py`, empreinte commençant par `391db990`), un JSON écrit avec l'outil d'écriture de fichiers, sous le nom neuf `additif-2-code-preenregistrement-ligne-3-votes-effectifs-juges-v7-v2.md`. Tenue : titre, ligne de version. Aucune autre modification ; rien de gelé ne change.
2. Différentiel `diff -u` v1 → v2 et rapport court `rapport-redacteur-additif-2-code-ligne-3-v2-v1.md`.

Ton dossier : `/tmp/claude-0/-home-user-controle-ia-travail/227b647d-2ece-5654-bf04-8493b3ed2f19/scratchpad/redacteur-additif-2-code-v2/`. Chaque fichier rendu avec son compagnon (`env -C DOSSIER sha256sum F`, redirigé vers `DOSSIER/F.sha256`). Règle R-4067 pour l'outil ; vérifie chaque ancre par `grep -c -F -e` sur la cible avant l'appel.

## Interdits

Voir en tête. Jamais de heredoc ni de code en ligne passé à un interpréteur. Aucun calcul de l'étage 1, aucun lancement du banc. Aucune écriture dans le dépôt, aucun commit. Rien sous `archives-reponses-modeles/`, rien sous `/root/.claude/`. Jamais le nom d'une commande d'arrêt ou de recherche de processus par motif. Aucun appel à un fournisseur de modèles, aucune dépense. Aucun identifiant de modèle. Au premier refus de permission, de classifieur ou de garde : arrête-toi et dis-le.
