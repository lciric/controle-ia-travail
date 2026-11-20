VERSION DE PYTHON : `python3 --version` ; AUCUN `-c`, AUCUN `-` APRÈS PYTHON3

AUCUNE COMMANDE DE LISTE : NI `ls`, NI `find`, NI `git ls-tree`, NI `git ls-files`, NI `git status`, NI `grep -r`, NI RECHERCHE SUR UN DOSSIER ENTIER, NI JOKER DANS UN CHEMIN. TOUT FICHIER S'OUVRE PAR SON CHEMIN COMPLET. UNE COMMANDE SIMPLE PAR APPEL : NI `&&`, NI `;`, NI BOUCLE. `git show` TOUJOURS REDIRIGÉ VERS UN FICHIER. AUCUNE RECHERCHE DE MOTIF LARGE.

# Mandat du rédacteur — préenregistrement court de la course « nouvelles attaques », version 3 (corrections L1 à L8) — v1

Pièce de travail (classe C). Donné par la session du compte organisme le 2026-11-20, sur l'accord de la mère. Dossier : `/home/user/controle-ia-travail/docs/notes/ideation-nouvelles-attaques-v1/preenregistrement-court-v2/` (noté P2).

## Qui

Un rédacteur neuf, modèle F. Tu signes « rédacteur neuf, modèle F ».

## Ce qui fait foi (vérifie chaque empreinte contre son compagnon)

- Le contrôle : `P2/controle-differentiel-preenregistrement-court-v1-v2-v1.md` (`7ab69293f34e06c4a74db3c56156ffd525c8db99e52ea9881348f9e0833f8862`), corrections **L1 à L8**, texte exact au § 5.
- La v2 : `P2/preenregistrement-court-course-nouvelles-attaques-v2.md` (`be4e3c4a…`).
- Sur main (relis par `fetch` puis `git show` redirigé) : GO-2026-11-20-22 (X = 8,35 USD ; juge sur Minuit, aiguilleur et espèce 4 sur Luc, espèce 3 sur Rigaud ; borne 415,21 USD) ; **R-4117**, qui dit que le contenu de GO-22 fait foi (« N2 (a) » de la fiche de la mère = option (b) du rapport v2) et que **K21 est acceptée par la mère** : c'est la ligne à citer pour L7.

## Ce que tu fais

1. L1 à L8 **à la lettre**, par l'outil contre-lu (`python3 -B /home/user/controle-ia-travail/scripts/remplacer_texte_exact_v1.py`, empreinte commençant par `391db990`), un JSON écrit avec l'outil d'écriture de fichiers, sous le nom neuf `preenregistrement-court-course-nouvelles-attaques-v3.md`. Pour L3, relis main et cite le commit relu et les empreintes des registres recalculées. Pour L7, cite R-4117. Pour L8, la section « Contre-lecture » reçoit les deux entrées avec leurs deux empreintes chacune, comme le contrôle les donne ; vérifie que le validateur l'accepte : `env -C /home/user/controle-ia-travail python3 -B -m controle_ia.prereg` avec `PYTHONPATH=src`, en lisant d'abord son aide (`--help`) pour la commande exacte de validation d'un fichier.
2. Pas de v3 du rapport (le contrôle recommande de ne pas en faire).
3. Différentiel `diff -u` v2 → v3 et rapport court `rapport-redacteur-corrections-preenregistrement-court-v3-v1.md`.

Ton dossier : `/tmp/claude-0/-home-user-controle-ia-travail/227b647d-2ece-5654-bf04-8493b3ed2f19/scratchpad/redacteur-preenregistrement-court-v3/`. Chaque fichier rendu avec son compagnon (`env -C DOSSIER sha256sum F`, redirigé vers `DOSSIER/F.sha256`). Règle R-4067 pour l'outil ; vérifie chaque ancre par `grep -c -F -e` sur la cible avant l'appel.

## Interdits

Voir en tête. Jamais de heredoc ni de code en ligne passé à un interpréteur. Aucune écriture dans le dépôt, aucun commit. Rien sous `archives-reponses-modeles/`, rien du coffre, rien sous `/root/.claude/`. Jamais le nom d'une commande d'arrêt ou de recherche de processus par motif. Aucun appel à un fournisseur de modèles, aucune dépense. **Aucune méthode d'attaque, aucun procédé, aucun détail opérant.** Aucun identifiant de modèle. Au premier refus de permission, de classifieur ou de garde : arrête-toi et dis-le.
