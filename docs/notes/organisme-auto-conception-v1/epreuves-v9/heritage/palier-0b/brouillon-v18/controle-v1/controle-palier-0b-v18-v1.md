# Contrôle différentiel du brouillon de la version 18 — préenregistrement du palier 0b — v1

**BROUILLON EN ATTENTE DU MOT DE LAZAR. Rien n'est scellé ; la version 13 scellée reste le texte en vigueur.**

- **Auteur** : contre-lecteur neuf, modèle O, celui des versions 14 à 17. Je n'ai écrit aucune version du texte ni aucun programme. Pièce de travail (classe C).
- **Date** : 2026-11-20, `date -u` à 22:30Z.
- **Mandat** : l'en-tête du mandat `84b76af6…`, et le message de la session du compte organisme qui demande ce contrôle.
- **Conditions** :
  - ce que j'ai fait : un `git fetch origin main` ; un `git show origin/main:registres/decisions.md` redirigé vers `lecture-registre-origin-main.md`, copie de lecture, non rendue ; l'outil, sur des copies ;
  - ce que je n'ai pas fait : aucun lancement d'un programme ni du code ; aucune écriture dans l'arbre de travail du dépôt.
  - **Aucun refus de permission, de classifieur ni de garde.**

## Verdict : **À corriger**

Deux corrections de cohérence, aucune de fond (point 4 (c)). Tout le reste est conforme.

**Jeu** : `corrections-palier-0b-v18-v1.json`, deux remplacements.
- Chaque ancre est comptée une fois dans la v18 par `grep -c -F -e`.
- Sur une copie de la v18, l'outil rend « FAIT : 2 remplacement(s) », sortie `d54b6e5312c78b922c50ced5e4b8fcbaefa838b5b937110360cdbfcf3f806a33` ; c'est un essai, non une version.
- Sur cette copie, l'en-tête reste intact : une ligne au préfixe, `COMMIT_V6` une fois, aucun `` `<40 hex>` `` dans la ligne, bloc de 64 lignes égal à la table.

## 1. Rejeu

**Empreintes égales aux compagnons** :
- mandat (`7456ff27…`) ;
- dossier `brouillon-v18/` : v18, différentiel (`99af4cf3…`), rapport (`e6a106e3…`), jeux des passes 2 (`63ab55e8…`) et 3 (`2511f1dc…`), sorties des passes 1 et 2 ;
- mon jeu de la v17, versé (`23e4d150…`).

**Rejeu depuis la v17** (`3ac2bc59…`) :
- passe 1 (mon jeu) : 8 remplacements, sortie **`4dafc835…`**, égale à mon essai ;
- passe 2 : 3 remplacements, sortie `757ac43d…`, égale à la passe 2 versée ;
- passe 3 : 6 remplacements, sortie **`ae1e8f56c06c8153bb09fa8503f3136773615132d9ce95c6fb3775aecea29876`**, avec un `cmp` muet contre la v18.

## 2. Mes huit corrections

Contrôle par `neufs_intacts_v1.py`, sortie `sortie-neufs-intacts-v1.txt`.

- **X2 à X8** sont intactes, à l'octet.
- **X1** est retouchée par la passe 2 en deux lieux, comme le mandat le demande :
  - rang 1 : la phrase finale « … ce texte ne le fixe pas » est remplacée par R-4338 et le constat de fin du programme des étapes 8 et 9 ;
  - rang 2 : les gelés du complément 3 sont précisés.
- Le reste de X1 est intact. Restent notamment, chacune comptée une fois :
  - la citation de R-4337 ;
  - les quatre compléments ;
  - « aucun lancement ne le précède : il ne porte ni fichiers gelés ni constat de fin » ;
  - « La pièce elle-même garde ses lignes ».

Aucune correction n'est défaite.

## 3. R-4338

**Lecture sur `origin/main`** après `git fetch` : commit `c63541fdd3e2551258f1dbc2ea4973676abaddd0`, `decisions.md` `3d286667…`, l. 4476, sous l'heure 2026-11-20T22:23:29Z.

**Citation** : à la lettre. Le texte entre guillemets est compté une fois dans la v18. Le commit et l'empreinte du registre que la v18 inscrit sont ceux que je relève.

**Constat de fin du programme 8–9, au complément 4**, sous la forme de R-4338 (remarque 4, et en bref à « Ce que chacun rend ») :
- manifeste de l'étape 8 présent et vérifié par `tirages.verifier_manifeste` ;
- manifeste de l'étape 9 présent s'il y a des cases à confirmer ;
- lignes « étape 8 : » et « étape 9 : » à la sortie ;
- code de sortie nul.

**La phrase « non fixé »** est corrigée. C'était le seul lieu sur ce constat, et la recherche du rédacteur le confirme.

## 4. Les limites que le rapport déclare

**(a) Les gelés du complément 3 : utile, sans changement de sens.**
- X1 disait « les mêmes », ce qui laissait au lecteur de chercher « les mêmes que quoi ».
- La v18 dit « les mêmes qu'au complément 2, le fichier des fréquences et le fichier des réglages venus du programme des étapes 3 à 6 ». C'est la lettre de R-4338 (« au complément 3, les gelés sont ceux venus de 3–6 »), et le sens est inchangé. À garder.

**(b) « Quand il n'y a aucune case à confirmer, l'étape 9 n'écrit rien, et la ligne « étape 9 : » de la sortie le dit » : vrai.**
- Dans `code-v6/outils-dev/lancer_etapes_8_et_9_v1.py`, l. 41 à 46 : si `r9["manifeste"] is None`, le programme écrit « étape 9 : aucune case à confirmer ; rien n'est écrit ». Sinon, il écrit « étape 9 : <manifeste> <empreinte> <n> cases ».
- Le rapport du code v6 (point 6) et l'ordre des opérations, point 9, disent qu'`etape_9` n'écrit ni dossier ni manifeste quand il n'y a rien à confirmer.
- « Le programme des étapes 8 et 9 n'écrit aucun fichier d'arrêt » est vrai aussi : aucun fichier d'arrêt dans le programme, ni dans `etapes.py`, ni dans `tirages.py` du code v6.
- Un arrêt fait sortir le programme avec un code non nul, qu'il s'agisse d'une exception ou d'un `SystemExit` avec message. Le constat « code de sortie nul » est donc sûr.

**(c) Les deux phrases de « Version 14 » : contradiction à lever, deux corrections.** « À quelle ligne de la pièce de contrôle cette empreinte s'écrit, ce texte ne le fixe pas » (§ 3) et « À quelle ligne de sa table, et si le chemin de ce programme s'y écrit, ce texte ne le fixe pas » (§ 7, remarque 7) sont au présent.
- Aucune clause de version ne les range dans l'histoire : la tenue de la v16 nomme d'autres phrases, pas celles-ci.
- Or les versions 16 à 18 fixent cette ligne : libellé qui nomme le programme, ligne dans la pièce elle-même et au complément 3 (R-4336, R-4337, R-4338).
- Un lecteur qui tombe sur l'une de ces deux phrases lit le contraire de la règle. Ce texte, en pareil cas, ajoute un renvoi « Version N » au lieu même, comme pour la remarque 3 de « Version 9 ».
- Corrections **Y1** et **Y2** : un renvoi « Version 18 » à chaque lieu. Elles ne touchent aucune règle.

**(d) Les compléments 2 et 3 nommés par leur seul numéro : suffisant.**
- X1 écrit le chemin entier du complément 1 et la série « de … `-v1-complement-1.md` à `…-v1-complement-4.md` ».
- R-4337 numérote les quatre compléments. Le nom des compléments 2 et 3 s'en déduit sans ambiguïté.
- Les programmes ne lisent aucun complément. Rien à corriger.

## 5. Rien hors mandat ; ligne du commit ; empreintes

**Lieux** (`sortie-lieux-passe-2-v1.txt`, `sortie-lieux-passe-3-v1.txt`) :
- passe 2 : remarque 4 (deux lieux) et « Ce que chacun rend » ;
- passe 3 : titre, statut et ligne de version, date, « Contre-lecture » (deux lieux), alinéa « Version 18 ».

Les autres lignes retirées sont celles de mes huit corrections. **Rien hors mandat.**

**Ligne du commit** (`sortie-entete-v18-v1.txt`) :
- une seule ligne commence par « - Commit du code d'analyse : » ;
- `COMMIT_V6` y figure une fois, et aucun `` `<40 hex>` `` ;
- la table de 64 lignes est le premier bloc, égale à l'octet à `table-empreintes-code-v6.txt`.

**Lieux des empreintes** :
- `1f04cb46…` : 2 lieux (l. 107 et 407) ;
- `ed91813a…` : 2 lieux (l. 107 et 408) ;
- `67052a4b…` : 6 lieux (l. 20, 107, 342, 409, 1158 et 1220).

Le compte attendu est tenu : 2, 2 et 6. Les corrections Y1 et Y2 n'ajoutent aucune empreinte.

## 6. Les corrections

| n° | lieu de la v18 | objet |
|---|---|---|
| Y1 | annexe H, « Version 14 », § 3, fin | renvoi « Version 18 » : l'empreinte du programme 8–9 s'écrit dans la pièce et au complément 3, sous `empreinte du programme lancer_etapes_8_et_9_v1.py :` |
| Y2 | annexe H, « Version 14 », § 7, remarque 7 | renvoi « Version 18 » : ligne fixée, nom du programme dans le libellé ; chemin dans l'arbre lancé, celui de la règle de la remarque 2 de « Version 16 » |

## 7. Fichiers

Dossier : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/contre-lecture-palier-0b-v12/v18/`.

Rendus, chacun avec son compagnon :
- cette pièce ;
- `corrections-palier-0b-v18-v1.json` ;
- `sortie-neufs-intacts-v1.txt` ;
- `sortie-lieux-passe-2-v1.txt` et `sortie-lieux-passe-3-v1.txt` ;
- `sortie-entete-v18-v1.txt` et `sortie-entete-essai-v18-v1.txt`.

Programmes employés : ceux des contrôles précédents (`v14/lieux_v1.py`, `v14/entete_essais_v1.py`, `v17/neufs_intacts_v1.py`) et `deplier_jeu_v1.py`.

Fichiers de travail, non rendus :
- `rejeu-passe-1.md` à `rejeu-passe-3.md` et `essai-v18-corrige.md`, avec leurs journaux ;
- `passe-2-deplie.txt` ;
- `lecture-registre-origin-main.md`.

*Contre-lecteur neuf, modèle O.*
