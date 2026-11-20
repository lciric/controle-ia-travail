VERSION DE PYTHON : `python3 --version` ; AUCUN `-c`, AUCUN `-` APRÈS PYTHON3

AUCUNE COMMANDE DE LISTE : NI `ls`, NI `find`, NI `git ls-tree`, NI `git ls-files`, NI `git status`, NI `grep -r`, NI RECHERCHE SUR UN DOSSIER ENTIER, NI JOKER DANS UN CHEMIN. TOUT FICHIER S'OUVRE PAR SON CHEMIN COMPLET. UNE COMMANDE SIMPLE PAR APPEL : NI `&&`, NI `;`, NI BOUCLE. `git show` TOUJOURS REDIRIGÉ VERS UN FICHIER DE TON DOSSIER, JAMAIS À L'ÉCRAN.

# Mandat du développeur — code de l'étage 1 de la ligne 3, deux ajouts de l'additif 1 (code v3) — v4

Pièce de travail (classe C). Donné par la session du compte organisme le 2026-11-20. Il garde l'objet et les interdits des mandats v1 à v3 du développeur de la ligne 3. Dossier de la ligne : `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-3-votes-effectifs-juges/` (noté LIGNE).

## Ce qui fait foi

- L'additif 1 v2 : `LIGNE/additif-1-v2/additif-1-preenregistrement-ligne-3-votes-effectifs-juges-v7-v2.md` (`e1c1ee842219397a45b5a9a9336d05d873499b2a94bc8847f204b205141908b0`), contrôlé « Conforme » (`LIGNE/additif-1-v2/controle-differentiel-additif-1-ligne-3-v1-v2-v1.md`), **non encore scellé** ; section « Ce que le code doit changer », deux ajouts à l'alarme (silence 1 : la part (b) et les cinq comptes ; silence 2 : par m, comptes et deux clauses de P6, mots « P6 réfutée » / « P6 non réfutée », marqués comme aide, jamais pour la carte `fcbf4a2dd1a57`).
- Le préenregistrement v7 sur main (`4e3680d9…`), lu par `git show` redirigé.
- Le code v2 : `LIGNE/code-etage-1-v2/` (banc `ffc33083…`, essais `d90eb6f3…`, contrôle des défauts `1ead2775…`, rapport `995bd5f4…`) et sa vérification « Conforme » (`LIGNE/code-etage-1-v2/verification-corrections-code-etage-1-ligne-3-v1.md`).

## Ce que tu fais

Une version 3 du code sous des noms neufs (`…_v3.py`, R12) dans `code-etage-1-v3/` de ton bloc-notes, sans toucher au v2 : les deux ajouts, **après les tirages, sur les tableaux déjà tirés** ; aucun tirage, aucune graine, aucune constante, aucune mesure existante ne change (prouve-le : sur les essais, toutes les sorties existantes du v2 sont égales à l'octet en v3). Chaque ajout a un essai sain et un artefact (R5) ; défauts réintroduits pour chaque ajout, ajoutés au contrôle (R4), rejoué en entier. Essais : `python3 -B -m pytest -q -p no:cacheprovider CHEMIN` ; racine des essais 2026111930 seule ; l'essai final « aucune graine décisive dérivée » passe. Rapport `code-etage-1-v3/rapport-developpeur-code-etage-1-ligne-3-v3.md` avec table des empreintes et différentiels v2 → v3. Pour les remplacements dans un fichier, `python3 -B /home/user/controle-ia-travail/scripts/remplacer_texte_exact_v1.py` (R-4067 : si l'outil rejette une ancre, c'est un essai qui échoue ; JSON neuf, fautif gardé, incident déclaré).

Ton bloc-notes : `/tmp/claude-0/-home-user-controle-ia-travail/227b647d-2ece-5654-bf04-8493b3ed2f19/scratchpad/developpeur-etage-1-ligne-3-v4/`. Chaque fichier rendu avec son compagnon (`env -C DOSSIER sha256sum F`, redirigé vers `DOSSIER/F.sha256`). Le dossier courant n'est pas gardé : `env -C DOSSIER commande`.

## Interdits

Voir en tête. **Jamais de heredoc ni de bloc de texte ou de code en ligne passé à un interpréteur, même vide.** Aucun calcul décisif, aucun chronomètre à pleine taille. Aucun appel à un fournisseur de modèles, aucune dépense, aucune machine, aucun réseau sauf `git fetch`/`git show` du dépôt. Aucune écriture dans le dépôt, aucun commit. Rien sous `archives-reponses-modeles/`, rien sous `/root/.claude/`. Jamais le nom d'une commande d'arrêt ou de recherche de processus par motif ; un calcul long s'arrête par l'outil de tâches. Aucun identifiant de modèle ; signe « développeur, modèle L′ ». Au premier refus de permission, de classifieur ou de garde : arrête-toi et dis-le.
