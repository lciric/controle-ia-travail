VERSION DE PYTHON : `python3 --version` ; AUCUN `-c`, AUCUN `-` APRÈS PYTHON3

AUCUNE COMMANDE DE LISTE : NI `ls`, NI `find`, NI `git ls-tree`, NI `git ls-files`, NI `grep -r`, NI JOKER DANS UN CHEMIN. TOUT FICHIER S'OUVRE PAR SON CHEMIN COMPLET, DONNÉ CI-DESSOUS OU CITÉ DANS UNE PIÈCE.

# Mandat du rédacteur — corrections de la conception de la course « nouvelles attaques », pièces v2 — v1

Pièce de travail (classe C). Donné par la session du compte organisme le 2026-11-20. Ne part qu'à la place Fable rendue par la mère. Dossier : `/home/user/controle-ia-travail/docs/notes/ideation-nouvelles-attaques-v1/conception-v1/` (noté DOSSIER).

## Qui

Un rédacteur neuf, modèle F. Tu signes « rédacteur neuf, modèle F ».

## Ce qui fait foi

- La contre-lecture : `DOSSIER/contre-lecture-conception-nouvelles-attaques-v1.md` (`ae9d4ae44027476bee4821e72c4e9f9b12f39d10f3dc6749ae60ae61d07c1fed`), verdict « Conforme après corrections », **vingt et une corrections C1 à C21**, chacune avec son texte « ancien » et « nouveau ».
- Les pièces v1 : `DOSSIER/question-course-nouvelles-attaques-v1.md`, `DOSSIER/ordre-course-nouvelles-attaques-v1.md`, `DOSSIER/devis-course-nouvelles-attaques-v1.md`, `DOSSIER/calcul_devis_course_nouvelles_attaques_v1.py`, `DOSSIER/calcul-devis-course-nouvelles-attaques-v1.json`, `DOSSIER/rapport-redacteur-conception-nouvelles-attaques-v1.md`.
- Le mandat d'origine et son complément : `/home/user/controle-ia-travail/docs/notes/ideation-nouvelles-attaques-v1/mandat-redacteur-conception-course-nouvelles-attaques-v1.md` et `/home/user/controle-ia-travail/docs/notes/ideation-nouvelles-attaques-v1/complement-1-mandat-redacteur-conception-course-nouvelles-attaques-v1.md`.
- GO-2026-11-20-05, sur main (`git -C /home/user/controle-ia-travail show origin/main:registres/go.md` après `fetch`), et le mandat de l'additif de l'orchestrateur : `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/orchestrateur-v68/mandat-redacteur-additif-orchestrateur-v69-v1.md`, qui réserve les noms v69 (régime du palier 1) et v70 (lecture du registre) : **le véhicule de cette course prend un nom neuf, ni v69 ni v70**, ni « lanceur version 11 ».

## Ce que tu fais

1. Tu appliques C1 à C21 **à la lettre** par l'outil contre-lu, sous des noms neufs (R12) : `…-v2.md` pour la question, l'ordre, le devis ; si le calcul change (C17, C18), un programme `calcul_devis_course_nouvelles_attaques_v2.py` et sa sortie `…-v2.json`, joués deux fois et comparés à l'octet. Un fichier JSON de remplacements par pièce, écrit avec l'outil d'écriture de fichiers ; `python3 -B /home/user/controle-ia-travail/scripts/remplacer_texte_exact_v1.py --cible … --remplacements … --sortie …` (empreinte de l'outil commençant par `391db990`).
2. Là où la contre-lecture propose et te laisse la main (le nœud neuf qui remplace D2, sa recommandation), tu peux changer la recommandation en disant pourquoi ; rien d'autre sur le fond.
3. Tenue : titres et lignes de version (« la v2 remplace la v1 après la contre-lecture … »). Aucune autre modification. **Aucune méthode d'attaque, aucun procédé, aucun détail opérant.**
4. Un différentiel `diff -u` v1 → v2 par pièce, et un rapport `rapport-redacteur-corrections-nouvelles-attaques-v2-v1.md` : correction par correction, appliquée ou non et pourquoi ; empreintes ; décisions pour Lazar au format.

Ton dossier : `/tmp/claude-0/-home-user-controle-ia-travail/227b647d-2ece-5654-bf04-8493b3ed2f19/scratchpad/redacteur-nouvelles-attaques-v2/`. Chaque fichier rendu avec son compagnon (`env -C DOSSIER sha256sum F`, redirigé vers `DOSSIER/F.sha256`). Le dossier courant n'est pas gardé d'un appel à l'autre : `env -C DOSSIER commande`.

## Interdits

Aucune commande de liste (voir en tête). Jamais de heredoc ni de code en ligne passé à un interpréteur ; une commande simple à la fois. Aucune écriture dans le dépôt, aucun commit. Aucune commande, même une empreinte, sur un chemin sous `archives-reponses-modeles/`, ni rien du coffre hormis sa question. Jamais le nom d'une commande d'arrêt ou de recherche de processus par motif. Aucun appel à un fournisseur de modèles, aucune dépense. Aucun identifiant de modèle. Au premier refus d'un outil ou d'un classifieur : arrête-toi et dis-le.
