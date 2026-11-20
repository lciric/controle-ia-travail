# Contrôle différentiel du brouillon de la version 17 — préenregistrement du palier 0b — v1

**BROUILLON EN ATTENTE DU MOT DE LAZAR. Rien n'est scellé ; la version 13 scellée reste le texte en vigueur.**

- **Auteur** : contre-lecteur neuf, modèle O, celui des versions 14 à 16. Je n'ai écrit aucune version du texte ni aucun programme. Pièce de travail (classe C), 2026-11-20.
- **Mandat** : l'en-tête du mandat `84b76af6…`, et deux messages de la session du compte organisme. Le premier demande les points 1 à 6. Le second ajoute un point 7 : la règle de la mère de 22:17Z, R-4337.
- **Conditions** :
  - ce que j'ai fait : un `git fetch origin main` ; un `git show origin/main:registres/decisions.md` redirigé vers `lecture-registre-origin-main.md`, copie de lecture, non rendue ; l'outil sur des copies ;
  - ce que je n'ai pas fait : aucun lancement d'un programme ni du code, aucune écriture dans l'arbre de travail du dépôt.
  - **Aucun refus de permission, de classifieur ni de garde.**

## Verdict : **À corriger** — pour la règle de la mère R-4337 seulement

1. **Points 1 à 6 : conformes.** La v17 porte fidèlement mes onze corrections et les trois choix de R-4336. Rien n'est hors mandat. La ligne du commit et la table sont intactes.
2. **Point 7 : huit corrections.** La v17 a été écrite avant R-4337. Elle laisse ouverts le nombre et le contenu des compléments, et elle ne fixe aucun ordre entre ce qui précède la règle n° 8. R-4337 les fixe : le texte doit le dire.
   - Jeu : `corrections-palier-0b-v17-v1.json`. Chaque ancre est comptée une fois par `grep -c -F -e` dans la v17 (huit comptes à 1).
   - Sur une copie de la v17, l'outil rend « FAIT : 8 remplacement(s) », sortie `4dafc835799d00ef705bd7b5d9ffc013a3dd9ba9838b398046fdbab6a36662f5`. C'est un essai, à appliquer à la v17 pour faire une v18.
   - Sur cette copie : une ligne au préfixe, `COMMIT_V6` une fois, aucun `` `<40 hex>` `` dans la ligne, bloc de 64 lignes égal à la table (`sortie-entete-essai-v17-v1.txt`).

## 1. Rejeu des trois passes

Les empreintes sont égales aux compagnons :
- mandat (`b7900ceb…`) ;
- dossier `brouillon-v17/` : v17, différentiel (`f68ca480…`), rapport (`1f9a7093…`), jeux des passes 2 (`f8b36570…`) et 3 (`a6627bcd…`), sorties des passes 1 et 2 ;
- mon jeu versé sous `brouillon-v16/controle-v1/` (`7f98449b…`).

Rejeu depuis la v16 (`c37bdb2f…`) :
- **passe 1** (mon jeu) : 11 remplacements, sortie **`ee5ff013…`**, égale à mon essai ;
- **passe 2** : 11 remplacements, sortie `b7632ea2…`, égale à la passe 2 versée ;
- **passe 3** : 6 remplacements, sortie **`3ac2bc59dd421375db9ce8ea492998e285f118adacbcfb03109cc14d5339ab4d`**. `cmp` avec la v17 : muet.

## 2. Mes onze corrections dans la v17

Contrôle par `neufs_intacts_v1.py`, sortie `sortie-neufs-intacts-v1.txt`.

- **Intactes, à l'octet** : neuf sur onze — A1 à A4, B, E, K1 à K3.
- **C** (remarque 3) : la passe 2, rang 8, ajoute à son titre la mention de R-4336, point 1. Le corps est intact ; la règle et les noms réels des fichiers d'arrêt sont comptés une fois.
- **D** (remarque 4) : la passe 2, rangs 1 à 3, en réécrit trois phrases, comme le mandat le demande.
  - Les mots qui laissaient ouverte la forme sans le nom sont retirés.
  - La forme avec le nom du programme et ses trois exemples restent.
  - La phrase « Ce texte ne dit pas sous quel nom … » est remplacée par la numérotation des compléments.

Aucune passe ne défait une correction.

## 3. Les trois choix de la mère (R-4336)

R-4336 a été relue sur `origin/main` (`33b504fb…`, l. 4474, 2026-11-20T22:12:01Z). Elle est citée à la lettre dans la v17 : le texte entre guillemets y est compté une fois.

- **(1) Constat de fin dans ma forme** : porté. Remarque 3, avec renvoi à R-4336, et une phrase à « Ce que chacun rend ».
- **(2) Seule la forme avec le nom** : portée à la remarque 4 et à « La pièce de contrôle — Sa forme ». Aucune alternative ne reste.
- **(3) Compléments numérotés dans l'ordre d'écriture, la règle n° 8 en dernier** : porté à la remarque 4 et à « Quand elle est écrite ».
- **Trois lieux du « complément 1 »** :
  - la citation de R-4292 et la phrase de la version 13, dans l'alinéa « Version 13 » de la remarque 5 de « Version 12 » ;
  - la citation de R-4296, en tête.

  Les citations restent à la lettre, et une phrase de la version 17 les corrige. Aucun autre lieu : « à son complément » (annexe H, « Version 14 », § 7, remarque 7) est de l'histoire et ne dit pas un numéro.

## 4. Rien hors mandat (passes 2 et 3)

Lieux (`sortie-lieux-passe-2-v1.txt`, `sortie-lieux-passe-3-v1.txt`) :
- **passe 2** : remarques 3 et 4 ; section des programmes, l. 460, 464, 465, 466 ; alinéa « Version 13 », l. 1096 ; citation de R-4296, l. 78 ; R-4336 citée après la remarque 8 ;
- **passe 3** : titre, statut et ligne de version, date, « Contre-lecture » (deux lieux), alinéa « Version 17 ».

Les autres lignes retirées sont celles de mes onze corrections. Rien d'autre.

## 5. Ligne du commit et empreintes

- **Ligne du commit** (`sortie-entete-v17-v1.txt`) :
  - une seule ligne commence par « - Commit du code d'analyse : » ;
  - `COMMIT_V6` figure une fois ;
  - la ligne ne porte aucun `` `<40 hex>` `` ;
  - la table de 64 lignes est le premier bloc qui la suit, égale à l'octet à `table-empreintes-code-v6.txt`.
- **Lieux des empreintes** (`grep -n -o`) :
  - `1f04cb46…` : 2 lieux, l. 107 et 407 ;
  - `ed91813a…` : 2 lieux, l. 107 et 408 ;
  - `67052a4b…` : 6 lieux, l. 20, 107, 342, 409, 1154 et 1216.

  C'est conforme : 2, 2 et 6.

## 6. Les limites du rapport

Le rapport laisse ouverts le nombre des compléments, leur contenu et l'ordre de ce qui précède la règle n° 8.
- **Avant R-4337**, j'aurais conclu qu'une remarque suffisait : aucun critère, seuil ni graine n'en dépend, et la mère en répond.
- **Depuis R-4337**, la mère a tranché : un texte qui laisse ouvert ce qu'une décision inscrite fixe est incomplet. **À corriger** (point 7).

La v17 dit en outre deux choses que R-4337 rend inexactes :
- « Viennent avant lui, dans l'ordre où la mère les écrit : les fichiers gelés …, les constats …, le contrôle de l'empreinte … et les dossiers … » : la règle range tout cela par lancement, non par nature ;
- « il ne dit ni combien de compléments la mère écrit, ni ce que chacun regroupe ».

## 7. La règle de la mère R-4337

R-4337 est inscrite. Relue sur `origin/main` après `git fetch` : commit `33b504fb0c14cf668a1f92f8a0cd32765a137334`, `decisions.md` `0b014106…`, l. 4475, 2026-11-20T22:17:39Z. Elle dit, à la lettre :

« Palier 0b, compléments de la pièce de contrôle : un par lancement, écrit et scellé avant lui, portant les gelés reçus du lancement précédent, le constat de fin de ce lancement (R-4336), l'empreinte et le commit du programme à lancer, nommé dans le libellé, et son dossier de sortie : complément 1 avant 3–6, 2 avant 6 bis–7, 3 avant 8–9 ; complément 4 après 8–9, pour la règle n° 8 et le constat de fin. V17 (3ac2bc59…) en contrôle. »

**Les huit corrections :**

| n° | lieu de la v17 | objet |
|---|---|---|
| X1 | annexe H, « Version 16 », § 2, remarque 4, phrase « Viennent avant lui … » | R-4337 citée à la lettre ; les quatre compléments, nommés, et ce que chacun porte |
| X2 | alinéa « Version 13 » de la remarque 5 de « Version 12 » | « vient en dernier : c'est le complément 4 » |
| X3 | remarque 2 | le contrôle de l'empreinte du programme 8–9 va au complément 3 |
| X4 | remarque 3 | les constats vont au complément 2, après le programme 3–6, et au complément 3, après le programme 6 bis–7 |
| X5 | remarque 5 | les dossiers vont au complément 2 (étapes 6 bis et 7) et au complément 3 (étapes 8 et 9) |
| X6 | section des programmes, « Quand elle est écrite » | un par lancement, le 1, le 2, le 3, puis le 4 |
| X7 | alinéa « Version 17 », limite | « ne disait … ; la décision R-4337 le fixe depuis » |
| X8 | citation de R-4296, annotation de la version 17 | le complément 4 |

Contenu de X1, pour chaque complément :
- (1) le complément 1, avant les étapes 3 à 6 : commit et empreinte du programme 3–6, son dossier ;
- (2) le complément 2, avant les étapes 6 bis et 7 : gelés, constat du programme 3–6, commit et empreinte du programme 6 bis–7, son dossier ;
- (3) le complément 3, avant les étapes 8 et 9 : gelés, constat du programme 6 bis–7, commit et empreinte du programme 8–9 et leur contrôle à la main, les deux dossiers ;
- (4) le complément 4, après les étapes 8 et 9 : la règle n° 8, puis le constat de fin du programme 8–9.

**Cohérence avec ce que la v17 dit déjà, quatre points :**
- **Le complément 1** n'a pas de lancement avant lui. X1 le dit sans ambiguïté : « aucun lancement ne le précède : il ne porte ni fichiers gelés ni constat de fin ».
- **La pièce elle-même garde ses lignes.** C'est une contrainte du code, non une décision nouvelle. Les programmes 1 et 2 ne lisent que la pièce, à son chemin (`CHEMIN_PIECE_DE_CONTROLE = …-par-la-mere-v1.md`), et y cherchent le commit et leur empreinte (programme 2, l. 47-48 et 62-76 ; de même au programme 1, l. 60 et 104-…). Une empreinte écrite seulement dans un complément ferait arrêter le programme. X1 le dit : le commit et les trois empreintes restent dans la pièce, et chaque complément les répète pour son lancement. Cela s'accorde avec ce que la v17 dit de la pièce (« le commit du code v6 ; l'empreinte de chacun des trois programmes »).
- **Les gelés du complément 3.** Le programme 6 bis–7 ne rend aucun fichier gelé (« rien n'en passe au programme 3 »). Je lis « les gelés reçus du lancement précédent » comme les mêmes fichiers, que le programme 6 bis–7 a reçus, et X1 le dit. Recommandation : confirmer cette lecture. Confiance élevée.
- **Le constat de fin du programme 8–9** (complément 4). R-4336 (1) nomme les fichiers d'arrêt et les lignes de sortie des deux premiers programmes seulement. Le programme 8–9 lui-même n'écrit aucun fichier d'arrêt : un arrêt des fonctions du code v6 qu'il appelle se propage jusqu'à lui. À sa sortie, il écrit « étape 8 : <manifeste> <empreinte> … » puis « étape 9 : … », ou « aucune case à confirmer ». X1 dit que ce constat n'est pas fixé. Recommandation pour la mère, confiance moyenne à haute, sans la mettre au jeu faute de sa lettre :
  - le manifeste de l'étape 8 présent et vérifié par `tirages.verifier_manifeste` ;
  - celui de l'étape 9 présent s'il y a des cases à confirmer ;
  - les lignes « étape 8 : » et « étape 9 : » à la sortie, et un code de sortie nul.

## 8. Fichiers

Dossier : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/contre-lecture-palier-0b-v12/v17/`.

Avec compagnons :
- cette pièce ;
- `corrections-palier-0b-v17-v1.json` ;
- `neufs_intacts_v1.py` et `sortie-neufs-intacts-v1.txt` ;
- `sortie-lieux-passe-2-v1.txt`, `sortie-lieux-passe-3-v1.txt` ;
- `sortie-entete-v17-v1.txt`, `sortie-entete-essai-v17-v1.txt`.

Fichiers de travail, non rendus :
- `rejeu-passe-1.md` à `rejeu-passe-3.md`, `essai-v17-corrige.md` et leurs journaux ;
- `passe-2-deplie.txt` ;
- `lecture-registre-origin-main.md`.

*Contre-lecteur neuf, modèle O.*
