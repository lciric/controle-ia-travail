# Journal du versement des pièces du papier C — version 1

Date : 2026-11-19. Pièce de travail (classe C). Dossier : `/tmp/claude-0/-home-user-controle-ia-travail/ea38fd7e-2b5a-5aae-9611-af6160a314d6/scratchpad/bloc-notes/versement`.

## Déroulé
1. Empreinte du texte dépouillé et des deux archives vérifiées. Relevé par programme des chemins et des empreintes (`outils/releve.py`, `outils/releve-brut.tsv`).
2. Index des empreintes : dossiers `papier-C/` et `voisins-C/` des archives, sans extraction (`outils/index-archives.tsv`) ; arbre du dépôt hors `diag/`, `runs/`, `donnees/`, `docs/verdicts/` (`outils/index-depot.txt`) ; recherche des seules empreintes citées dans le reste des archives (`outils/correspondances-hors-papier-C.tsv`). Croisement : `outils/croisement.tsv`.
3. Plan de versement (`outils/plan.py`, `outils/plan.tsv`), extraction par membres nommés sous `extraction/`, copie dans `arbre/` avec compagnons, empreintes et tailles recontrôlées (`outils/extraire_copier.py`). 161 pièces.
4. Première tentative de réémission des mesures de conception en version 2 : `scipy` absent de la machine, pas d'environnement au dépôt. Une commande de ce rédacteur, interrompue par cette absence, a laissé un compagnon vide hors de l'arbre (voir « Reste »).
5. Refus de permission (texte exact plus bas) sur une commande de suppression de ce compagnon vide. Arrêt et compte rendu, comme le mandat l'exigeait.
6. Reprise sur mot de la session mère : aucune suppression ; environnement local `venv/` (python 3.13.18, numpy 2.5.5, scipy 1.18.1, installés par `pip install numpy scipy` depuis le registre de paquets ; manifeste `outils/manifeste-environnement-mesures-v2.txt`) ; version 1 rejouée, identique octet pour octet à la sortie de l'archive ; version 2 émise dans l'arbre (`outils/faire_v2.py`) : deux lignes ajoutées, aucun chiffre changé.
7. Liste des PDF cités par les notes (`outils/pdf_manquants.py`, `outils/pdf-cites.tsv`) ; table écrite par programme (`outils/ecrire_table.py`).

## Reste, non supprimé
- `mesures-v2-non-relancees/mesures_conception_papier_c_v2.py.sha256` : fichier vide (0 octet), créé par une commande ratée ; hors de l'arbre de versement ; sans valeur ; laissé en place sur consigne (aucune suppression).
- `outils/controle-partie2-kendall-numpy-seul.txt` et `outils/v1-partie2.txt` : restes de la même commande ratée ; sans valeur.
- `outils/rejeu-mesures-v1.txt` : sortie du rejeu de la version 1 dans l'environnement local (identique à l'archive).

## Texte exact du refus de permission
> Permission for this command was denied by a built-in Claude Code safety check, not by the user. The check stops removals that can delete far more than intended: a system, home or workspace directory, or a target it cannot resolve, such as a shell variable that, if unset or empty, turns this into `rm -rf /` or `rm -rf /*`. Only a person may approve such a removal, and no person did (the permission prompt timed out, or none was shown). The command was NOT run; do not claim it succeeded. Do not work around the check by splitting, scripting, or re-issuing the removal through another tool or shell: the check exists because a removal like this can destroy the user's data, and getting past it would not make it safe. If the text below suggests a safe rewrite, run that instead; it goes through the same check. Otherwise finish the rest of the task without this removal, tell the user what you wanted to delete and why, and leave the removal to them. What was flagged: Dangerous rm operation detected in `rm -f $D/*.sha256`. The target '$D/*.sha256' is a shell variable expansion: when $D is unset or empty it becomes `/`, `/*` or a top-level path. This requires explicit approval and cannot be auto-allowed by permission rules.
>
> This check does not fire on a target that cannot expand to the filesystem root: rewrite it as `"${D:?}"/*.sha256`, which makes the shell stop with an error instead of running rm when $D is unset or empty, or use a literal absolute path.

La commande refusée n'a rien exécuté. Aucune suppression n'a été faite, ni avant ni après.

## Interdits tenus
Rien d'ouvert sous `diag/`, `runs/`, `donnees/`, `docs/verdicts/` ; aucun nom à « consigne-privee » ni « conception-ii-b » dans les listes des archives ; aucune modification du dépôt ; seul accès au réseau : l'installation de numpy et de scipy depuis le registre de paquets, sur mot de la session mère ; aucun autre agent, aucun modèle extérieur, aucune suite d'essais.
