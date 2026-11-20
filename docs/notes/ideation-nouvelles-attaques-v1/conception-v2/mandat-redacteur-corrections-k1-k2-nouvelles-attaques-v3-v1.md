VERSION DE PYTHON : `python3 --version` ; AUCUN `-c`, AUCUN `-` APRÈS PYTHON3

AUCUNE COMMANDE DE LISTE : NI `ls`, NI `find`, NI `git ls-tree`, NI `git ls-files`, NI `grep -r`, NI JOKER DANS UN CHEMIN. TOUT FICHIER S'OUVRE PAR SON CHEMIN COMPLET.

# Mandat du rédacteur — corrections K1 et K2 de la conception « nouvelles attaques » (pièces v3) — v1

Pièce de travail (classe C). Donné par la session du compte organisme le 2026-11-20. Dossier : `/home/user/controle-ia-travail/docs/notes/ideation-nouvelles-attaques-v1/conception-v2/` (noté V2).

## Qui

Un rédacteur neuf, modèle F. Tu signes « rédacteur neuf, modèle F ».

## Ce qui fait foi

- Le contrôle : `V2/controle-differentiel-conception-nouvelles-attaques-v1-v2-v1.md` (`3ab2b0eb620ce98f73fd7f3b92f0738ecae57ebd1b6f1209eb2e5de42aed1a3d`), verdict « Conforme après corrections » : **K1** (tenue, quatre remplacements) et **K2** (troisième classe d'issue « hors case », six remplacements), texte ancien et nouveau donnés. Le devis v2, son programme et sa sortie sont conformes tels quels : **tu n'y touches pas**.
- Les pièces visées : `V2/question-course-nouvelles-attaques-v2.md`, `V2/ordre-course-nouvelles-attaques-v2.md`, `V2/rapport-redacteur-conception-nouvelles-attaques-v2.md`.

## Ce que tu fais

1. K1 et K2 **à la lettre**, par l'outil contre-lu (`python3 -B /home/user/controle-ia-travail/scripts/remplacer_texte_exact_v1.py --cible … --remplacements … --sortie …`, empreinte commençant par `391db990`), un JSON de remplacements par pièce écrit avec l'outil d'écriture de fichiers, sous des noms neufs : `question-course-nouvelles-attaques-v3.md`, `ordre-course-nouvelles-attaques-v3.md`, `rapport-redacteur-conception-nouvelles-attaques-v3.md`.
2. Tenue : titres et ligne de version (« la v3 remplace la v2 après le contrôle de son différentiel ; seules K1 et K2 sont appliquées ; le devis reste en v2 »), et les renvois aux pièces sœurs. Aucune autre modification. **Aucune méthode d'attaque, aucun procédé, aucun détail opérant.**
3. Un différentiel `diff -u` v2 → v3 par pièce et un rapport court `rapport-redacteur-corrections-k1-k2-nouvelles-attaques-v3-v1.md`.

Ton dossier : `/tmp/claude-0/-home-user-controle-ia-travail/227b647d-2ece-5654-bf04-8493b3ed2f19/scratchpad/redacteur-nouvelles-attaques-v3/`. Chaque fichier rendu avec son compagnon (`env -C DOSSIER sha256sum F`, redirigé vers `DOSSIER/F.sha256`). Le dossier courant n'est pas gardé : `env -C DOSSIER commande`.

## Interdits

Aucune commande de liste (voir en tête). Jamais de heredoc ni de code en ligne passé à un interpréteur ; une commande simple à la fois. Aucune écriture dans le dépôt, aucun commit. Rien sous `archives-reponses-modeles/`, rien du coffre, rien sous `/root/.claude/`. Jamais le nom d'une commande d'arrêt ou de recherche de processus par motif. Aucun appel à un fournisseur de modèles, aucune dépense. Aucun identifiant de modèle. Au premier refus d'un outil ou d'un classifieur : arrête-toi et dis-le.
