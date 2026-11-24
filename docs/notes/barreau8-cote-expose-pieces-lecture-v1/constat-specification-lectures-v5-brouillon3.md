# Constat sur le brouillon 3 de la spécification des lectures du dommage et de la diffusion sur la course v5

> EXPLORATOIRE, NON OPPOSABLE (R-522). Pièce de travail du côté exposé ; elle n'est jamais transmise au côté des moniteurs.

**Verdict : scellable en l'état.**

| Pièce | Fichier | Empreinte |
|---|---|---|
| Brouillon 3 (pièce constatée) | `specification-lectures-dommage-diffusion-course-v5-v1-brouillon3.md` | `acce24e76e17bffb2938616f2204d068a1f61d5e71938ce8a33e1e6a83a7407e` |
| Différences du brouillon 2 au brouillon 3 | `differences-specification-brouillon2-vers-3-v1.md` | `6aca9e888b1096311ffd0296b7133c1a6f37493de18178af80a0c47cd49cbde6` |
| Brouillon 2, resté intact | — | `5968aa37…` |

Les trois empreintes ont été recalculées. Le constat est fait par le même contre-lecteur, sous les mêmes interdits : aucune consigne privée, rien sous `docs/verdicts/`, aucune valeur des sorties de la course, aucun fichier du dépôt modifié.

## Les trois mineurs sont levés

### r1 — « clé seule écrite » dans deux lignes d'essais

Levé. Les lignes « décodage » et « fidélité » de la section 14 disent maintenant que la clé est imprimée sur la sortie d'erreur et que rien n'est écrit sur disque. L'essai vérifie qu'aucun fichier n'est créé.

### r2 — racine des registres

Levé.
- **Définition** : la racine des registres est le dossier parent du dossier `registres/` qui porte le fichier passé par `--registre-sondes`. Ce fichier doit être exactement `registres/sondes-iib-v1.md` ; tout autre nom, ou tout autre dossier, arrête la lecture.
- **Fonction d'ouverture** : `ouvrir(sorte_de_racine, …)` accepte trois racines nommées, chacune avec sa liste fermée.
- **Registre des décisions** : il est exigé dans ce même dossier `registres/`.
- **Essais** : ils sont ajoutés.
- **Script d'audit** : il n'ouvre rien sous la racine des registres.

### r3 — garde de l'audit de symétrie

Levé.
- Les quatre refus sont examinés dans l'ordre.
- Après la dernière ligne `DEFAUT`, il faut une ligne `DEFAUT-AUTORISE` qui porte un identifiant d'accord ouvrant une ligne de `registres/go.md` (première colonne de la table).
- Une ligne `SANS-DEFAUT`, où qu'elle soit, ne débloque rien.
- Les essais suivent : `DEFAUT` puis `SANS-DEFAUT` est refusé ; une autorisation placée avant le dernier défaut est refusée ; un identifiant absent du registre des accords est refusé.

## La liste des différences est complète

Le `diff` du brouillon 2 au brouillon 3 compte 29 blocs, le nombre annoncé. Chaque bloc correspond à une ligne de la liste des différences, et je n'ai trouvé aucun changement hors de cette liste.

La table de traitement de la contre-lecture 1 est gardée telle qu'au brouillon 2, et c'est déclaré. C'est le seul endroit où paraît encore le mot « recommandation ». Aucune option non retenue, aucun texte de rechange ni la mention « à trancher » ne subsiste ailleurs.

## Rien de faux n'est introduit

### Jetoniseur

Les quatre empreintes ont été recalculées par `git show e5677bbf2696e9364da7f4bf191abcc5de16eabc:jetoniseur/<fichier> | sha256sum`. Elles sont égales aux références :

| Fichier | Empreinte |
|---|---|
| `tokenizer.json` | `79e3e522…` |
| `tokenizer_config.json` | `177c7b61…` |
| `generation_config.json` | `189fb0c0…` |
| `config.json` | `29e4c210…` |

- **Branche** : le commit est orphelin, sans parent. Il est porté par `origin/jetoniseur/llama31-8b-instruct-0e9e39f2-v1`.
- **Contenu de l'arbre** : exactement ces quatre fichiers sous `jetoniseur/`, plus `LISEZMOI.md` et `empreintes-jetoniseur-v1.txt` à la racine de la branche, comme le dit la pièce. Je n'ai pas ouvert ces deux derniers.

### Mot rendu sur les nœuds

Les trois nœuds sont tranchés par leur option (a) : la part citée se lit sur tous les épisodes du maître ; la base « premier coût contre les suivants » est calculée et tenue du côté exposé ; les deux phrases sans phrase écrite d'avance gardent la phrase d'origine.

- **Accord** : il est cité sous `GO-2026-11-24-35`. Cet accord existe sur `origin/main` (ligne 913 de `registres/go.md`). Il autorise la mère à appliquer ses recommandations aux nœuds en attente, sauf pour une porte, une modification d'hypothèse ou de revendication, un contact externe ou une publication. Aucun des trois nœuds n'entre dans ces exceptions.
- **Ce que je n'ai pas vérifié** :
  - le message de 17:12Z lui-même ;
  - l'identifiant de session de la mère cité en tête, qui diffère de celui de la session du rédacteur.

  Le message doit être consigné par la mère au registre des décisions.

### Section 16

Elle ne porte plus qu'une option par nœud, et aucun choix ne dépend d'un résultat. Les limites des options retenues sont écrites. Les sept choix vont à Lazar pour information.

### Invariants

Le vocabulaire, la portée, les bases, les paires et la forme de l'extrait sont inchangés.

## Défauts restants

Aucun.
