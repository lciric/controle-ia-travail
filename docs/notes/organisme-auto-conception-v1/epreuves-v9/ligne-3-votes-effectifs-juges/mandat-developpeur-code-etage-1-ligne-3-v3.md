VERSION DE PYTHON : `python3 --version` ; AUCUN `-c`, AUCUN `-` APRÈS PYTHON3

# Mandat du développeur — code de l'étage 1 de la ligne 3, corrections de la contre-lecture (classe B) — v3

Pièce de travail (classe C). Donné par la session du compte organisme le 2026-11-20, sur GO-2026-11-20-01 et la lecture R-4024 de la mère (travaux sans Fable). Il garde l'objet et les interdits des mandats v1 et v2 (`mandat-developpeur-code-etage-1-ligne-3-v1.md`, `…-v2.md`, `0769bc95…`).

## Ce qui fait foi

- Le préenregistrement v7 de la ligne 3, sur main : `prereg/organisme-auto-conception-v9/preenregistrement-ligne-3-votes-effectifs-juges-v7.md` (`4e3680d9…`), lu par `git show origin/main:…` après `git fetch origin main`.
- La contre-lecture : `code-etage-1-v1/contre-lecture-v1/contre-lecture-code-etage-1-ligne-3-v1.md` (`3aed6849c76a4ed421207470e4a6b8a45fcecf6a8ef5325a5203c84fda2f85ff`), verdict « Conforme après corrections », corrections **C1, C2, C3** ; ses mutants (`mutants_cl.py`) et leur rapport (`rapport_ctrl_cl.json`), même dossier.
- Le code v1 : `code-etage-1-v1/` (banc `1d474cc9…`, essais `13b2b898…`, contrôle des défauts, rapport du développeur).

## Ce que tu fais

Une version 2 du code, sous des noms neufs (`…_v2.py`, R12) dans `code-etage-1-v2/` de ton bloc-notes, sans toucher au v1 :
- **C1** : essais sain et artefact qui épinglent chacune des règles de lecture et constantes listées par la contre-lecture ; les défauts correspondants ajoutés au contrôle des défauts réintroduits, rejoué ; viser que les 35 mutants de la contre-lecture soient vus, et dire lesquels ne le sont pas et pourquoi.
- **C2** : la taille d'étalonnage de la branche (2) suit la lettre du texte (« à partir de laquelle » : la branche tient à cette taille et à toutes les tailles plus grandes de la grille). Si tu lis le texte autrement, tu ne choisis pas : tu rends les deux grandeurs et tu le dis au rapport, comme question de texte.
- **C3** : l'essai sain de `verifier_autorisation` sur un additif valide ; des défauts visés sur cette fonction seule, sans aucune dérivation.
- Les deux silences relevés en plus par la contre-lecture (alarmes « à effet » comptées comme détections ; alarme sans mot calculé) et les points A à E sont des **questions de texte** : tu ne les tranches pas, tu les laisses au rapport.

Essais : `python3 -B -m pytest -q FICHIER` ; racine des essais 2026111930 seule ; aucune graine de 2026111931 à 2026111937 ; l'essai final « aucune graine décisive dérivée » reste vrai. Rapport : `code-etage-1-v2/rapport-developpeur-code-etage-1-ligne-3-v2.md`, avec un tableau de chaque fichier et son empreinte ; chaque fichier rendu a son compagnon `.sha256`.

Ton bloc-notes : `/tmp/claude-0/-home-user-controle-ia-travail/227b647d-2ece-5654-bf04-8493b3ed2f19/scratchpad/developpeur-etage-1-ligne-3-v3/`.

## Interdits

**Jamais de heredoc ni de bloc de texte ou de code en ligne passé à un interpréteur, même vide, même pour lire une version : un développeur de cette ligne a été arrêté pour cela.** Une commande simple à la fois. Aucun calcul décisif, aucun chronomètre à pleine taille. Aucun appel à un fournisseur de modèles, aucune dépense, aucune machine, aucun réseau sauf `git fetch`/`git show` du dépôt. Aucune écriture dans le dépôt, aucun commit, aucune poussée. **Aucune commande, même une empreinte, une liste ou une taille, sur un chemin sous `archives-reponses-modeles/`.** Jamais le nom d'une commande d'arrêt ou de recherche de processus par motif ; un calcul trop long s'arrête par l'outil de tâches. Aucun identifiant de modèle ; signe « développeur, modèle L′ ». Au premier refus d'un outil : arrête-toi et dis-le.
