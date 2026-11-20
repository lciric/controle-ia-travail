# Rapport du rédacteur — préenregistrement du palier 0b, brouillon v18 (compléments de la pièce de contrôle, R-4337 et R-4338) — v1

**BROUILLON, EN ATTENTE DU MOT DE LAZAR.** Rien n'est scellé ; la version 13 scellée reste le texte en vigueur ; la version 17 n'est pas touchée. Pièce de travail (classe C). 2026-11-20, journaux de l'outil : 22:24:45Z, 22:25:17Z et 22:26:10Z.

Dossier : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/redacteur-palier-0b-v18/`. Mandat : `mandat-redacteur-palier-0b-v18-complements-v1.md` (`7456ff27…`, égal à son compagnon).

## 1. Verdict

La version 18 est la version 17 (`3ac2bc59…`) plus **dix-sept remplacements exacts, en trois passes nommées**. **La sortie de la passe 1 est égale à l'essai du contrôleur (`4dafc835…`).** Une seule ligne commence par « - Commit du code d'analyse : » (compte : 1) ; le blanc `COMMIT_V6` reste, une seule fois ; aucun groupe de quarante chiffres hexadécimaux dans cette ligne (compte : 0) ; les 64 lignes de la table y sont, et la table reste le premier bloc de code après la ligne du commit (l. 9 à 74). L'écart de la garde 17 reste à Lazar, non tranché. Aucun refus de permission, de classifieur ni de garde.

## 2. Fichiers et empreintes

| fichier | empreinte SHA-256 |
|---|---|
| `preenregistrement-heritage-palier-0b-etage-processeur-v18.md` | `ae1e8f56c06c8153bb09fa8503f3136773615132d9ce95c6fb3775aecea29876` |
| `differentiel-palier-0b-v17-v18-v1.diff` (`diff -u`) | `99af4cf3dddf534691c06eb182ee60916122e03800a4952cb49f1915ad69bbe4` |
| `remplacements-passe-2-r-4338-v1.json` | `63ab55e801fbbd8c5f1834edb9573287e7cec004c104eb1760662a10daef6aef` |
| `remplacements-passe-3-tenue-v1.json` | `2511f1dcd8aafabb2aa01ff46e069c963e16c03148f4a071838b3c9e8e217787` |
| `passe-1-v17-plus-corrections-du-controle.md` | `4dafc835799d00ef705bd7b5d9ffc013a3dd9ba9838b398046fdbab6a36662f5` |
| `passe-2-plus-r-4338.md` | `757ac43d955b22989bfd15e284c0f11fbc7052a9d6819c0a4cd75d462525cf6c` |

Chacun a son compagnon ; les trois journaux de l'outil sont au dossier. Pièces reçues, recalculées et égales à leur compagnon : version 17, contrôle (`7f42dd73…`), jeu du contrôleur (`23e4d150…`).

## 3. Les trois passes

- **Passe 1 — le jeu X1 à X8 du contrôleur, tel quel** : 8 remplacements. **Les huit ancres ont été comptées par moi avant l'appel**, par `grep -c -F -e` sur la version 17 : huit fois « 1 ». Sortie `4dafc835…`, égale à son essai.
- **Passe 2 — R-4338** : 3 remplacements de ma main ; chaque ancre comptée à 1 sur la sortie de la passe 1.
  - **R-4338 citée à la lettre** (2026-11-20T22:23:29Z), relue sur `origin/main` au commit `c63541fdd3e2551258f1dbc2ea4973676abaddd0` après un `git fetch` ; elle est à la remarque 4 du § 2 de « Version 16 » (annexe H), à la place de la phrase de X1 qui disait le constat non fixé.
  - *Le constat de fin du programme 8–9, au complément 4* : manifeste de l'étape 8 présent et vérifié par `tirages.verifier_manifeste` ; manifeste de l'étape 9 présent s'il y a des cases à confirmer ; lignes « étape 8 : » et « étape 9 : » à la sortie ; code de sortie nul. Repris en bref à la section des programmes (« Ce que chacun rend »).
  - *La phrase « non fixé »* : un seul lieu (celui de X1), corrigé. Recherche des mots « ne le fixe pas », « n'est pas fixé », « non fixé » : aucun autre lieu ne porte sur ce constat.
  - *Les gelés du complément 3* : X1 disait « les mêmes » ; je l'ai rendu explicite — « les mêmes qu'au complément 2, le fichier des fréquences et le fichier des réglages venus du programme des étapes 3 à 6 (décision R-4338) ».
- **Passe 3 — tenue** : 6 remplacements (titre ; statut et ligne de version ; date ; section « Contre-lecture », deux lieux ; alinéa « Version 18 » de l'annexe H). Chaque ancre comptée à 1 sur la sortie de la passe 2.

**La pièce garde le commit et les trois empreintes, les compléments les répètent** : dit par X1 (remarque 4), et redit à l'alinéa « Version 18 » avec renvoi à R-4338.

## 4. Comptes

**Lieux des trois empreintes entières** (lignes de la version 18), inchangés en nombre depuis la version 17 :
- programme des étapes 3 à 6, `1f04cb46…` : 2 lieux (l. 107, l. 407) ;
- programme des étapes 6 bis et 7, `ed91813a…` : 2 lieux (l. 107, l. 408) ;
- programme des étapes 8 et 9, `67052a4b…` : 6 lieux (l. 20, 107, 342, 409, 1158, 1220).

**Noms `…-v1-complement-N`** :

| nom | occurrences | lieux |
|---|---|---|
| `…-v1-complement-1` | 3 | l. 1104, deux fois (la citation de R-4292, en abrégé, et le chemin entier de la phrase de la version 13) ; l. 1222 (X1, chemin entier) |
| `…-v1-complement-2` | 0 | — |
| `…-v1-complement-3` | 0 | — |
| `…-v1-complement-4` | 2 | l. 1104 (X2) ; l. 1222 (X1) |

Les compléments 2 et 3 ne sont nommés que par leur numéro (« le complément 2 », « le complément 3 ») ; X1 écrit « de `…-v1-complement-1.md` à `…-v1-complement-4.md` », ce qui donne leurs noms sans les écrire. Je ne les ai pas ajoutés : le mandat ne le demande pas.

## 5. Écarts et limites

- Le troisième remplacement de la passe 2 (les gelés du complément 3) précise une phrase de X1 que le contrôleur tenait déjà pour sans ambiguïté ; le mandat le permet « s'il reste une ambiguïté », et j'ai jugé que « les mêmes » gagnait à être dit. Si le contrôleur le juge superflu, il se retire sans rien changer d'autre.
- La phrase « Quand il n'y a aucune case à confirmer, l'étape 9 n'écrit rien, et la ligne « étape 9 : » de la sortie le dit » vient de ma lecture du programme des étapes 8 et 9 (lu pour la version 16), non de R-4338.
- Deux phrases de « Version 14 » (§ 3 et § 7, remarque 7) disent encore que la ligne de la pièce où s'écrit l'empreinte du programme 8–9 n'est pas fixée ; c'est de l'histoire, que les versions 16 à 18 règlent ailleurs ; je ne les ai pas touchées, hors mandat.
- La date de la ligne de date est celle de `date -u` (22:25Z) ; le journal de la passe 3 dit 22:26:10Z.
- Un `mkdir -p` de mon dossier ; un `git fetch origin main`, un `git show` redirigé, un `git rev-parse` ; des `grep -n -o` sur des fichiers nommés.
- Aucun lancement d'un programme, du code ni d'un essai ; aucun tirage ; aucune pièce d'autorisation ni de contrôle ; aucun appel à un fournisseur ; aucune dépense ; aucune écriture dans le dépôt.
- **À ne pas verser** : `lecture-registre-origin-main.md`.

Signé : rédacteur des v15 à v18, modèle F.
