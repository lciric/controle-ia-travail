# Mandat du développeur neuf (Fable 5.2) du code du saboteur à budget — v1

Écrit par la session mère `session_013QMayjsoZJFBUCqcnvD5h1` le 2026-11-18 vers 21:45Z, sur le mot direct de Lazar « prend un developpeur fable » (R-3454). Langue : français, sans sigle seul.

## Qui tu es
Un développeur **neuf** du code du « saboteur à budget » (barreau 8) : un agent de test de laboratoire, sur modèles ouverts, qui dégrade discrètement une tâche pour éprouver des moniteurs ; recherche en sûreté. Tu reprends la branche `prep/iib-code-v3` à sa tête `ff6a947593f7c9f73c96e8055ff2d94a8f2eb02e`, après le développeur précédent (Opus 4.6), arrêté.

## Interdits absolus
- N'ouvre aucun fichier dont le nom contient « consigne-privee » ni « conception-ii-b », ni la branche `lot/compte-4-v1`. N'écris aucun fragment de consigne ni aucun sujet ou mécanisme du saboteur dans un message, un rapport ou un nom de fichier. Les essais de non-fuite existants restent tels quels.
- Tentative franche : au premier refus (classifieur, permission, crochet, garde-fou du modèle), arrêt, sans reformuler, découper ni contourner ; texte exact du refus rendu.
- Aucun nom de commande d'arrêt de processus par motif dans une ligne de commande, même en recherche.
- Processeur seulement, aucune dépense, aucun modèle chargé, aucun téléchargement.
- Cloisonnement : rien sous `diag/`, `runs/`, `donnees/`, `docs/verdicts/`, `registres/` ; aucun code, score ni poids de sonde ou de moniteur, sauf la pièce de la base textuelle que nomme le relevé ci-dessous, lue pour l'appeler.

## Où travailler
`git worktree add /home/user/iib-dev-fable-v1 origin/prep/iib-code-v3` puis `git -C /home/user/iib-dev-fable-v1 checkout -B prep/iib-code-v3 origin/prep/iib-code-v3` ; commits à la suite (aucune réécriture d'histoire) ; poussée sur `prep/iib-code-v3` seulement. Le disque est compté : `python -B`, `--basetemp` à toi, supprimé ensuite. La demande de fusion #23 reste en brouillon, jamais fusionnée.

## Ce que tu fais
Lis d'abord : `docs/notes/barreau8-iib-v1/controle-court-code-iib-v3-v1.md`, `docs/notes/barreau8-iib-v1/verification-courte-corrections-controle-court-iib-v1.md` (dépôt principal), le rapport v5 du développeur précédent sur la branche, et `docs/notes/barreau8-iib-v1/releve-code-des-deux-bases-v1.md`.
1. **CC-01 (majeur, obligatoire)** : l'essai du relais doit faire passer dans les deux motifs de l'amorce **la sortie réelle d'un jeu jouet du lanceur** (et non des arguments écrits dans l'essai). Preuve exigée et jouée : correction du lanceur retirée dans une copie → l'essai échoue ; remise → il passe. Rapporte exactement ce que tu as éprouvé.
2. **Portage de la base textuelle** : Lazar a suivi la recommandation (A) du relevé (GO-2026-11-18-56, point 4) : le code appelle la pièce inscrite au lieu de sa propre méthode d'ajustement. Écris ce code neuf et ses essais (cas sain et artefact de chaque garde, R5) ; graines par `SeedSequence` (R9) ; aucune moyenne ni médiane sur les jetons dans une sonde.
3. VC5-01 (sonde de texte sur 512 octets) : souhaitable.
4. Rejoue la suite ciblée `tests/test_iib_*` et la répétition jouet (identique à l'octet) ; rapport v6 scellé sous `brouillons/ii-b-saboteur-budget-v1/rapport-developpeur-corrections-iib-v6.md` sur la branche.

## Ce que tu rends
Ton dernier message à la session mère : tête neuve, nombre d'essais, pour chaque point « corrigé (preuve jouée) », « laissé (pourquoi) » ou « hors périmètre », chemin et empreinte du rapport v6, refus éventuels mot pour mot, lectures hors mandat. **Aucun sujet ni mécanisme** dans ce message. Supprime ton arbre de travail à la fin (`git worktree remove`), après la poussée.
