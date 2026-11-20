# Erratum 1 du rapport du développeur, collisionneur v9 v3

Écrit le 20 novembre 2026 par le même développeur (Claude Opus 5.5). Il suit la contre-lecture `contre-lecture-collisionneur-v9-v3-v1.md` (`9a9f0871b5b99c90371754b1afa42ff29f5a6b5915457483a3f6ca7328687fab`, Claude Fable 5.2, verdict « conforme après corrections »). Il corrige `rapport-developpeur-collisionneur-v9-v3.md` (`99bd3d48…`), qui n'est pas réécrit. Le script `collisionneur_v9_v3.py` (`850df311…`) ne change pas. Aucun appel réseau, aucun commit.

## C5 : phrase périmée du rapport

Le rapport disait : « `.git/info/exclude` contient `docs/notes/collisionneur-v9/*v3*` : les fichiers v3 n'apparaissent pas dans `git status` ».

Ce n'est plus vrai :
- cette exclusion n'est plus dans `.git/info/exclude` ;
- le commit `419719254` contient le script v3, ses essais, le rapport et la commande de reprise, chacun avec son sceau.

Vérifié par `git show --stat 419719254` et `git ls-files`.

## Corrections C1 à C4 appliquées, dans des pièces neuves

- **C1, C2, C3 : commande de reprise v2.** Fichier `commande-reprise-collisionneur-dopamine-v3-v2.txt`, construit à partir de la v1 par quatre remplacements à texte exact. La v1 est gardée telle quelle.
  - **C1** : clé `RR_ANTHROPIC_API_KEY_RIGAUD`, avec le commentaire de tête de la contre-lecture.
  - **C2** : contrôle par `python -m controle_ia.scellement verifier`. Rejoué depuis la racine du dépôt : `OK 850df3118073…`, code 0.
  - **C3** : règle « ne pas relancer l'étape 3 après un code 4 tombé sur une relance ».
- **Espace de travail d'Anthropic : la commande v2 ne le donne pas.** Ni `journal-lancement-mere.log` ni les registres (R-4257, ligne 551 de `registres/depenses.md`) ne donnent la ligne de commande du lancement de 12:24Z. Je n'ai donc aucune trace de `--nom-espace-anthropic` à ce lancement.
  - Si la mère sait que ce lancement le donnait, elle le redonne à l'étape 3 : `--nom-espace-anthropic RR_ANTHROPIC_WORKSPACE_ID`, comme le dit le commentaire de tête.
  - Si l'en-tête manque et qu'il était exigé, le premier comptage échoue (`COMPTE_IMPOSSIBLE`, code 8) et rien n'est envoyé.
- **C4 : essais complémentaires.** Fichier `test_collisionneur_v9_v3_complement_1.py`, repris à l'octet du bloc de la contre-lecture ; empreinte `58ddaa24acd62b7ce638cbfa058ce53d2423a4640c03b5b6aea2f137b4824534`, égale à l'attendue.
  - Le complément seul : 6 passés.
  - La suite v3 et le complément ensemble : 157 passés.
  - Les essais v2 sur la v2 : 117 passés.
- **Quatre retraits de C4**, faits sur des copies dans le bloc-notes, avec mes propres mutations. Chacun casse au moins un essai du complément, et aucun de la suite v3 seule :

| retrait | essais du complément en échec |
|---|---|
| comptage d'OpenAI envoyé à une adresse tierce | 2 |
| changement déclaré depuis une autre empreinte, admis | 1 |
| ligne non contrôlée à la relance | 1 |
| plafond non contrôlé à la relance | 1 |

Le contre-lecteur comptait 3 échecs pour le premier retrait. Ma mutation n'a pas la même forme : elle garde l'indicateur de boucle locale, et l'essai sain à la boucle locale passe donc encore.

## Ce qui reste à la mère

- **Crédit de la clé Rigaud.** La part d'Anthropic au pire est de 10,32 USD, selon la contre-lecture (C1). Il faut relire le crédit avant l'étape 3.
- **Changement de C3 dans le script.** La contre-lecture propose de ne pas repayer la première passe. Il n'est pas appliqué : le script v3 ne change pas. Il reviendrait à une version suivante.
- **Vérification par le même contre-lecteur** de ces corrections.
