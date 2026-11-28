# Contre-lecture de l'additif 1 au versant honnête (v3) — Opus 5.5, v1

**Attestation** (2026-11-24, de 18:31Z à 18:40Z) : contre-lecteur neuf. Je n'ai lu aucun épisode, score, sortie de course, diagnostic, verdict ni lecture ; rien sous coffre/ ; aucune sortie d'étape 0. Dépôt non modifié.

**Verdict : scellable après corrections.**

Contrôles tenus :
1. L'ancienne ligne est égale à l'octet à la ligne 12 de la v3 (a505fa4e…), vérifié par `cmp`.
2. Les six empreintes recalculées sont égales. Le rapport v2 est sur la branche, après le commit ab094582.
3. La voie V2 est suivie : la v7 est contre-lue (« corrections vérifiées », diff limité à l'annoncé), avant toute donnée réelle, avec une entropie neuve.
4. Aucun seuil ni critère ne change. Les clés de tirage du code v6 et du code v7 sont identiques. Le code v7 refuse une table d'un autre commit (lignes 1694 et 1695) : les tables faites au commit 8e074634 ne peuvent pas resservir. Les deux phrases de l'auteur sont donc exactes.

## Défauts
1. **Moyen.** Le code lit le commit dans la copie de travail (lignes 1674 à 1676). Or la tête de la branche est déjà au-delà (passe v3 au commit 7bbb14cd2). Il faut écrire que l'étape 0 et la lecture tournent dans une copie dont la tête est ab094582. Sinon les tables sont refusées, ou bien la phrase « étape 0 du commit ab094582 » est invérifiable. La mère le constate sur le manifeste de l'étape 0.
2. **Faible.** La ligne V2 se déclenche sur un objet planté hors tolérance, pas sur un défaut trouvé à la contre-lecture. La raison doit dire que l'additif emprunte sa procédure.
3. **Faible.** La ligne 192 de la v3 dit : « le code v6 refuse toute lecture réelle sans ce fichier ». La portée doit dire que cette phrase se lit du code v7, qui garde ce refus (ligne 1986). Les errata et le fichier des réglages ne nomment ni le code v6 ni le commit 8e074634.
4. **Faible.** La première étape 0 a tourné sous l'entropie racine, contre le point 4 (« graines neuves »). Il faut le déclarer comme un écart, refermé parce que ses tables ne servent pas. L'entropie neuve et l'heure de la relance sont à vérifier par la mère au scellement.

## Qui a lu quoi
J'ai lu l'additif, la v3 (lignes 9 à 15, et par recherche les lignes 192, 204, 205, 238 et 378), les errata (par recherche), le fichier des réglages, le rapport v2 en entier et la contre-lecture (défauts). Dans le code v7, j'ai lu les seules lignes trouvées par recherche. J'ai vu des titres de commits et des noms de fichiers.
