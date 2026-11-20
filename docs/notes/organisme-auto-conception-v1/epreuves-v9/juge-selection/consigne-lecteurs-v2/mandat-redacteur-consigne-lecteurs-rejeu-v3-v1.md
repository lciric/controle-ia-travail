VERSION DE PYTHON : `python3 --version` ; AUCUN `-c`, AUCUN `-` APRÈS PYTHON3

AUCUNE COMMANDE DE LISTE : NI `ls`, NI `find`, NI `git ls-tree`, NI `git ls-files`, NI `git status`, NI `grep -r`, NI RECHERCHE SUR UN DOSSIER ENTIER, NI JOKER DANS UN CHEMIN. TOUT FICHIER S'OUVRE PAR SON CHEMIN COMPLET. UNE COMMANDE SIMPLE PAR APPEL : NI `&&`, NI `;`, NI BOUCLE. `git show` TOUJOURS REDIRIGÉ VERS UN FICHIER. AUCUNE RECHERCHE DE MOTIF LARGE.

# Mandat du rédacteur — consigne des lecteurs du rejeu, version 3 (garde nommée, retouche du § 4) — v1

Pièce de travail (classe C). Donné par la session du compte organisme le 2026-11-20, sur l'accord de la mère (garde de `lignee_reconnue` scellée en v2 ; retouche facultative du contrôle acceptée). Dossier : `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/juge-selection/consigne-lecteurs-v2/` (noté C2).

## Qui

Un rédacteur neuf, modèle F. Tu signes « rédacteur neuf, modèle F ».

## Ce qui fait foi (vérifie chaque empreinte)

- La consigne v2 : `C2/consigne-lecteurs-rejeu-criteres-v7-v2.md` (`1e5479be…`) et son contrôle `C2/controle-differentiel-consigne-lecteurs-v1-v2-v1.md` (`e5c21791…`), qui donne la retouche facultative du § 4 (« le programme d'assemblage ne voit pas » à la place de « le programme ne voit pas »).
- La garde scellée de la mère, sur main : `git -C /home/user/controle-ia-travail fetch origin main`, puis `git -C /home/user/controle-ia-travail show origin/main:docs/notes/organisme-auto-conception-v9-mere/juge-selection-manifeste-v1/garde_lignee_reconnue_v2.py`, redirigé vers ton dossier (empreinte `635e9160…`) ; tu en lis seulement l'en-tête pour la nommer juste.

## Ce que tu fais

Par l'outil contre-lu (`python3 -B /home/user/controle-ia-travail/scripts/remplacer_texte_exact_v1.py`, empreinte commençant par `391db990`), un JSON écrit avec l'outil d'écriture de fichiers, sous le nom neuf `consigne-lecteurs-rejeu-criteres-v7-v3.md` : au § 4, la phrase de garde nomme la pièce (chemin et empreinte) ; la retouche facultative du contrôle, à la lettre ; tenue : titre, ligne de version. Aucune autre modification. Différentiel `diff -u` v2 → v3 et rapport court `rapport-redacteur-consigne-lecteurs-rejeu-v3-v1.md`.

Ton dossier : `/tmp/claude-0/-home-user-controle-ia-travail/227b647d-2ece-5654-bf04-8493b3ed2f19/scratchpad/redacteur-consigne-lecteurs-rejeu-v3/`. Chaque fichier rendu avec son compagnon (`env -C DOSSIER sha256sum F`, redirigé vers `DOSSIER/F.sha256`). Règle R-4067 ; vérifie chaque ancre par `grep -c -F -e` sur la cible avant l'appel.

## Interdits

Voir en tête. Jamais de heredoc ni de code en ligne passé à un interpréteur. Aucune carte. Aucune écriture dans le dépôt, aucun commit. Rien sous `archives-reponses-modeles/`, rien sous `/root/.claude/`. Jamais le nom d'une commande d'arrêt ou de recherche de processus par motif. Aucun appel à un fournisseur de modèles, aucune dépense. Au premier refus de permission, de classifieur ou de garde : arrête-toi et dis-le.
