VERSION DE PYTHON : `python3 --version` ; AUCUN `-c`, AUCUN `-` APRÈS PYTHON3

AUCUNE COMMANDE DE LISTE : NI `ls`, NI `find`, NI `git ls-tree`, NI `git ls-files`, NI `git status`, NI `grep -r`, NI RECHERCHE SUR UN DOSSIER ENTIER, NI JOKER DANS UN CHEMIN. TOUT FICHIER S'OUVRE PAR SON CHEMIN COMPLET. UNE COMMANDE SIMPLE PAR APPEL : NI `&&`, NI `;`, NI BOUCLE. `git show` TOUJOURS REDIRIGÉ VERS UN FICHIER DE TON DOSSIER, JAMAIS À L'ÉCRAN.

# Mandat du rédacteur — corrections 1 à 6 de l'additif 1 de la ligne 3 (additif v2) — v1

Pièce de travail (classe C). Donné par la session du compte organisme le 2026-11-20. Dossier : `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-3-votes-effectifs-juges/additif-1-v1/` (noté A1).

## Qui

Un rédacteur neuf, modèle F. Tu signes « rédacteur neuf, modèle F ».

## Ce qui fait foi

- La contre-lecture : `A1/contre-lecture-additif-1-ligne-3-v1.md` (`f12200ae427da3f3f70d549ac4dfef4feeb805b2279c7a24bf36e86f563d3955`), verdict « Conforme après corrections », **six corrections de texte**, texte ancien et nouveau donnés ; son jugement du point B (question de conception, non un nœud ; l'option (b) presque gratuite en calcul, à dire).
- Les pièces : `A1/additif-1-preenregistrement-ligne-3-votes-effectifs-juges-v7-v1.md` (`27ecd5d5…`), `A1/rapport-redacteur-additif-1-ligne-3-v1.md` (`6c273e5e…`).

## Ce que tu fais

1. Les six corrections **à la lettre**, par l'outil contre-lu (`python3 -B /home/user/controle-ia-travail/scripts/remplacer_texte_exact_v1.py`, empreinte commençant par `391db990`), un JSON par pièce écrit avec l'outil d'écriture de fichiers, sous des noms neufs : `additif-1-preenregistrement-ligne-3-votes-effectifs-juges-v7-v2.md`, `rapport-redacteur-additif-1-ligne-3-v2.md`.
2. Tenue : titres et ligne de version ; dans le rapport, le point B suit le jugement de la contre-lecture (question de conception ; l'option (b) presque gratuite en calcul). Aucune autre modification ; aucun critère gelé ne change.
3. Différentiels `diff -u` v1 → v2 et rapport court `rapport-redacteur-corrections-additif-1-ligne-3-v2-v1.md`.

Ton dossier : `/tmp/claude-0/-home-user-controle-ia-travail/227b647d-2ece-5654-bf04-8493b3ed2f19/scratchpad/redacteur-additif-1-ligne-3-v2/`. Chaque fichier rendu avec son compagnon (`env -C DOSSIER sha256sum F`, redirigé vers `DOSSIER/F.sha256`). Le dossier courant n'est pas gardé : `env -C DOSSIER commande`.

## Interdits

Voir en tête. Jamais de heredoc ni de code en ligne passé à un interpréteur. Aucun calcul de l'étage 1, aucun tirage. Aucune écriture dans le dépôt, aucun commit. Rien sous `archives-reponses-modeles/`, rien sous `/root/.claude/`. Jamais le nom d'une commande d'arrêt ou de recherche de processus par motif. Aucun appel à un fournisseur de modèles, aucune dépense. Aucun identifiant de modèle. Au premier refus d'un outil ou d'un classifieur : arrête-toi et dis-le.
