VERSION DE PYTHON : `python3 --version` ; AUCUN `-c`, AUCUN `-` APRÈS PYTHON3

AUCUNE COMMANDE DE LISTE : NI `ls`, NI `find`, NI `git ls-tree`, NI `git ls-files`, NI `git status`, NI `grep -r`, NI RECHERCHE SUR UN DOSSIER ENTIER, NI JOKER DANS UN CHEMIN. TOUT FICHIER S'OUVRE PAR SON CHEMIN COMPLET. UNE COMMANDE SIMPLE PAR APPEL : NI `&&`, NI `;`, NI BOUCLE. `git show` TOUJOURS REDIRIGÉ VERS UN FICHIER. AUCUNE RECHERCHE DE MOTIF LARGE.

# Mandat du rédacteur — additif des interrupteurs de l'orchestrateur v69, version 4 (corrections 1, 2, 3, 3 bis et 4 du contrôle de la v3) — v1

Pièce de travail (classe C). Donné par la session du compte organisme le 2026-11-20. Dossier : `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/orchestrateur-v69/` (noté V69).

## Qui

Un rédacteur neuf, modèle F. Tu signes « rédacteur neuf, modèle F ».

## Ce qui fait foi (vérifie chaque empreinte contre son compagnon)

- Le contrôle : `V69/controle-differentiel-additif-orchestrateur-v69-v2-v3-v1.md` (`12bbec8ded9c0e22eb257ebc03e193a7ec02d4cab2294c3fda036a5e904f7a4c`), **corrections 1, 2, 3, 3 bis et 4**, texte exact dans la pièce ; les points jugés « non exigé » ne se touchent pas. L'écart de la v3 (virgule changée en point) est accepté.
- La v3 : `V69/additif-interrupteurs-orchestrateur-v69-v3.md` (`f71e3a55…`). Le cadre v3 (`b1822613…`) n'appelle aucune correction : il ne change pas, aucune v4 du cadre.
- Le rapport du rédacteur de la v3 : `V69/rapport-redacteur-additif-orchestrateur-v69-v3-v1.md` (`4446464d…`) ; sa proposition de la correction 5 (§ 5) est jugée conforme et ne se réécrit pas.

## Ce que tu fais

1. Les cinq corrections **à la lettre**, par l'outil contre-lu (`python3 -B /home/user/controle-ia-travail/scripts/remplacer_texte_exact_v1.py`, empreinte commençant par `391db990`), un JSON écrit avec l'outil d'écriture de fichiers, sous le nom neuf `additif-interrupteurs-orchestrateur-v69-v4.md`. Tenue : titre, ligne de version, statut si la version y est nommée. Rien d'autre. Aucun allumage n'est accordé.
2. Différentiel `diff -u` v3 → v4 et rapport court `rapport-redacteur-additif-orchestrateur-v69-v4-v1.md` (remplacements, ancres comptées, tout écart).

Ton dossier : `/tmp/claude-0/-home-user-controle-ia-travail/227b647d-2ece-5654-bf04-8493b3ed2f19/scratchpad/redacteur-additif-orchestrateur-v69-v4/`. Chaque fichier rendu avec son compagnon (`env -C DOSSIER sha256sum F`, redirigé vers `DOSSIER/F.sha256`). Règle R-4067 ; vérifie chaque ancre par `grep -c -F -e` sur la cible avant l'appel.

## Interdits

Voir en tête. Jamais de heredoc ni de code en ligne passé à un interpréteur. Aucun lancement de l'orchestrateur, du lanceur ni de l'organisme. Aucune écriture dans le dépôt, aucun commit. Rien sous `archives-reponses-modeles/`, rien sous `/root/.claude/`. Jamais le nom d'une commande d'arrêt ou de recherche de processus par motif. Aucun appel à un fournisseur de modèles, aucune dépense. Aucun identifiant de modèle. Au premier refus de permission, de classifieur ou de garde : arrête-toi et dis-le.
