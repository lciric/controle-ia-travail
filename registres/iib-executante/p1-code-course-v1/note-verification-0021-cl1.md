# Vérification courte du correctif 0021 — tirage sur la carte et tirage passé par l'ordre (cl1)

Date : 2026-11-22. Même contre-lecteur (Claude Opus 5.5), mêmes interdits. Rien poussé ni dépensé.

**Verdict : corrections levées, aucune régression. Le code est autorisable.**

## Application et essais rejoués

- Le correctif 0021, appliqué par `git am` dans le worktree neutre `scratchpad/cl-p1`, donne l'arbre `725f3d5884c3617065aa913d04e9b3eee0e2afac`, celui annoncé.
- Liste figée v6 : **296 passed**.
- Liste de la course en version 2, avec torch sur processeur : **311 passed, 1 skipped**. Le seul saut est l'essai marqué « carte ».

## Les corrections

**m1, levé.** Le second hachage `b` se tire maintenant de la base et du jeton sous des sels propres. Il ne dépend donc plus de `a` seul, et l'uniforme compte bien 53 bits. Un essai vérifie l'indépendance des deux hachages, avec son artefact.

Mon contrôle de la loi, rejoué sur le nouveau hachage, ne montre aucun écart :

| contrôle | résultat |
|---|---|
| khi-deux, graines aléatoires | p = 0,46 |
| khi-deux, pas successifs | p = 0,94 |
| khi-deux, graines consécutives | p = 0,43 |
| uniformité de u (Kolmogorov-Smirnov) | p = 0,84 |
| corrélation entre pas, entre jetons voisins | −0,002 |

**m2, levé.** La garde des logits ne juge plus que les lignes actives :
- un NaN sur une ligne finie n'arrête pas le lot ;
- un NaN sur une ligne active l'arrête.

Les deux cas ont leur essai.

**Garde du même tirage (`exiger_meme_tirage`).**
- Elle lit `resultat.tirage` dans le résumé scellé de l'étalonnage, après vérification de son sceau.
- Un résumé écrit avant le correctif 0020, qui n'a pas la clé, vaut « processeur ». C'est juste : ce code-là ne savait tirer que sur le processeur.
- Un tirage différent est refusé avant tout manifeste.
- Essais : un cas sain, des artefacts dans les deux sens, et la variable de l'ordre.

**`IIB_TIRAGE` dans les scripts.**
- Dans `lancer_iib_v3.sh`, le correctif ajoute exactement trois choses : une ligne d'en-tête, une ligne qui valide `IIB_TIRAGE` (toute autre valeur que « processeur » ou « carte » est un refus, code 2), et `-e IIB_TIRAGE=$TIRAGE` dans la commande de création. Rien d'autre ne change.
- Les deux amorces valident la variable et passent `--tirage` au lanceur.

## Constat du développeur sur trois points du lanceur de session

Les trois points sont **confirmés** sur le code. Un seul renvoi de ligne est à corriger.

1. **Plafond de la configuration plus dépense antérieure.**
   - Le constat est juste : `lancer_iib_v3.sh` l. 226 (lecture de `ANT`), l. 237 (`controles-explo`), l. 314 (dépense), et `session_v12.py` l. 77 (`if p + a > limite`).
   - Correction du renvoi : l'appel `go` de la création est à la **l. 283**, non à la l. 289.
   - La configuration porte 55 USD. Avec une ligne à 60 USD, toute dépense antérieure au-delà de 5 USD est refusée, et la course sur machine neuve ne peut donc pas partir sous GO-2026-11-21-70.
   - C'est une **garde de dépense** : la changer demande le mot de Lazar ou une ligne de GO neuve.
2. **Plafond de la ligne de GO lu sous la seule forme « N USD ».** Confirmé : `session_v3.py` l. 30 à 36 (`fullmatch`). La ligne de GO neuve devra écrire son plafond sous cette forme.
3. **Instance arrêtée qui bloque la création.**
   - Confirmé : `session_v2.py` l. 153 retient toute étiquette `iib…`, quel que soit son état.
   - Cela contredit l'en-tête de `session_v1.py` (l. 12 et 13), qui dit que les instances arrêtées ne bloquent pas.
   - La destruction de la machine de l'étalonnage, après le rapatriement vérifié, lève ce blocage.

## Restes pour l'ordre

- **Nombre d'essais attendus.** `TESTS_ATTENDUS=312` sur la machine de la course, avec la liste en version 2. L'essai « carte » s'y joue alors même que la course tire sur le processeur (la garde l'impose après un étalonnage sous « processeur »). Il faut accepter ce risque ou revenir à la liste en version 1.
- **Dépense.** Une ligne de GO neuve est nécessaire, ou un mot de Lazar sur la garde de dépense (point 1).
- **Instance de l'étalonnage.** La détruire avant la création (point 3).
- **Rappels.** Machine neuve (mot de Lazar), aucune création à partir du 2026-11-27T00:00Z, et un mot sur la première action « gardée ».
