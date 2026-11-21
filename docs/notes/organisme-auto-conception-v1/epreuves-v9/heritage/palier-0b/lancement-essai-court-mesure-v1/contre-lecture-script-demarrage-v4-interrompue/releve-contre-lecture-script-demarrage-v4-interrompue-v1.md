# Relevé de la contre-lecture S courte du script de démarrage v4 — interrompue au premier refus — v1

Pièce de travail (classe C), recopiée par la session du compte organisme le 2026-11-21 vers 23:56Z depuis le rapport de fin de l'agent, sans rien changer sur le fond. Pièces visées : script v4 `d20e90e1…`, amorce v4 `39236834…`, fabricant v4 `12a49965…`, rapport de l'auteur `1dc07929…` (commit `6bf7a515`). L'agent a contrôlé les quatre empreintes : toutes OK.

## Verdict : incomplet, arrêté au premier refus
Aucun des cinq points n'a été joué. La pièce de l'agent n'est pas écrite, et ses dossiers d'outils et de tables sont vides. Aucun processus n'a été lancé ou arrêté ; aucun commit ; aucune dépense ; l'environnement n'a été ni listé ni affiché.

## Refus, cité mot pour mot
L'appel refusé était une lecture dans des dossiers voisins, non nommés dans le mandat : la liste de `auteur-lanceur-v4/` et de `auteur-lanceur-v3-gardien-v4/`, enchaînée avec l'affichage de trois outils du banc. Réponse de l'outil :

> Permission for this action was denied by the Claude Code auto mode classifier. Reason: [Unauthorized Access]. If you have other tasks that don't depend on this action, continue working on those. […]

L'agent n'a ni reformulé ni découpé. Il cherchait ces pièces parce que le fabricant les relit à des chemins écrits en dur (variable `P`) : sans elles, il ne peut pas jouer le point 5. La session ne fait pas cette lecture à sa place.

## Constats de lecture, non éprouvés (de l'agent)
1. **R2, un chemin reste ouvert, et la course de l'auteur ne le visait pas.** La course de l'auteur (`essais-outils/course-amorce.sh`) remplace le fichier de la charge. Or la v4 copie ce fichier dans `$CHARGE.script.XXXXXX/s.sh`, puis hache cette copie. Remplacer la charge mène donc au pire au refus 18, comme le montrent les 18 refus de la course. Un processus du même compte peut trouver la copie par motif de nom, et un dossier 700 ne protège pas du même compte. Il peut alors remplacer `s.sh` entre le hachage (ligne 15 de l'amorce) et la lecture (ligne 17). La fenêtre est plus étroite qu'en v3, mais elle reste ouverte. À jouer : une course dirigée sur la copie privée, au moins 300 exécutions.
2. **R1** : un descendant qui ouvre sa propre session (nouveau `setsid`) et dont le père meurt n'est plus atteint par aucun des trois critères (chaîne des parents, session, groupe). Il survivrait à l'arrêt.
3. **R3** : la fenêtre de −5 s à +2 s autour de l'heure de lancement écrite, au code 5, permet de prendre pour le programme un étranger qui reprendrait son identifiant dans ces 7 s. Elle n'est atteignable que si l'identifiant est recyclé en moins de 7 s ; à chiffrer par l'épreuve.
4. **R4** : la ligne 12 de l'amorce est juste à la lecture ; un `E_SCRIPT` faux rend 18 à la ligne 15.
5. L'extraction de la charge (ligne 10) précède le contrôle de `E_SCRIPT` (ligne 12) : un `E_SCRIPT` absent laisse une charge à demi extraite, et une reprise rend 20. L'auteur le note lui-même.

## Écart déclaré par l'agent
Il n'a rendu ni sa pièce ni son « Relevé de méthode » : sans rien avoir joué, il aurait dû les remplir sans épreuve.
