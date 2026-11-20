# Rapport du rédacteur — préenregistrement du palier 0b, brouillon v17 (corrections du contrôle de la v16 et choix de la mère) — v1

**BROUILLON, EN ATTENTE DU MOT DE LAZAR.** Rien n'est scellé ; la version 13 scellée reste le texte en vigueur ; la version 16 n'est pas touchée. Pièce de travail (classe C). 2026-11-20, journaux de l'outil : 22:13:08Z, 22:14:38Z et 22:15:42Z.

Dossier : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/redacteur-palier-0b-v17/`. Mandat : `mandat-redacteur-palier-0b-v17-corrections-v1.md` (`b7900ceb…`, égal à son compagnon).

## 1. Verdict

La version 17 est la version 16 (`c37bdb2f…`) plus **vingt-huit remplacements exacts, en trois passes nommées**. **La sortie de la passe 1 est égale à l'essai du contrôleur (`ee5ff013…`).** Une seule ligne commence par « - Commit du code d'analyse : » (compte : 1) ; le blanc `COMMIT_V6` reste, une seule fois ; aucun groupe de quarante chiffres hexadécimaux dans cette ligne (compte : 0) ; les 64 lignes de la table y sont, et la table reste le premier bloc de code après la ligne du commit (l. 9 à 74). L'écart de la garde 17 reste à Lazar, non tranché. Aucun refus de permission, de classifieur ni de garde.

## 2. Fichiers et empreintes

| fichier | empreinte SHA-256 |
|---|---|
| `preenregistrement-heritage-palier-0b-etage-processeur-v17.md` | `3ac2bc59dd421375db9ce8ea492998e285f118adacbcfb03109cc14d5339ab4d` |
| `differentiel-palier-0b-v16-v17-v1.diff` (`diff -u`) | `f68ca480e491494f79ee09df0a602029e04192f3ee4f5c1a5989aa838b3ce673` |
| `remplacements-passe-2-choix-de-la-mere-v1.json` | `f8b365709aaaec7b4340cbf0be4af2ee77a6e4755b9346a7121c19d734886361` |
| `remplacements-passe-3-tenue-v1.json` | `a6627bcd469fa0fc49c6154eb7bdf61a4029bc8f41f53ca86b522a35a9e4ccb8` |
| `passe-1-v16-plus-corrections-du-controle.md` | `ee5ff01398149875259ce580aab768f75410d5641eb70c851354d9a34451ce2c` |
| `passe-2-plus-choix-de-la-mere.md` | `b7632ea298779956a83946ed7c1f638546fe206b5264de46a7bb631af781f6d1` |

Chacun a son compagnon ; les trois journaux de l'outil sont au dossier. Pièces reçues, recalculées et égales à leur compagnon : version 16, contrôle (`6e772a5d…`), jeu du contrôleur (`7f98449b…`).

## 3. Les trois passes

- **Passe 1 — le jeu du contrôleur tel quel** : 11 remplacements (A1 à A4, B, C, D, E, K1 à K3). Sortie `ee5ff013…`, égale à son essai.
- **Passe 2 — les trois choix de la mère** : 11 remplacements de ma main. Chaque ancre comptée à 1 sur la sortie de la passe 1.
  - **R-4336 citée à la lettre** (2026-11-20T22:12:01Z), relue sur `origin/main` au commit `433c3cd972b194eb111adbdddca73c75e6945be9` après un `git fetch` ; elle est à la fin du § 2 de « Version 16 » (annexe H).
  - *Choix 1, constat de fin sans arrêt* : la forme du contrôleur, déjà portée par sa correction C ; renvoi à R-4336 à la remarque 3, et une phrase à la section des programmes (« Ce que chacun rend »).
  - *Choix 2, libellés avec le nom du programme* : la phrase de la remarque 4 qui nommait la forme sans le nom est réécrite, ainsi que celle qui la reprenait ; la forme avec le nom est aussi inscrite à la section des programmes. Après la passe, les mots « commit du programme » et « empreinte du programme » entre guillemets ne figurent plus au texte (compte : 0).
  - *Choix 3, compléments numérotés* : remarque 4 ; section des programmes, deux lieux ; alinéa « Version 13 » corrigé ; citation de R-4296 annotée.
- **Passe 3 — tenue** : 6 remplacements (titre ; statut et ligne de version ; date ; section « Contre-lecture », deux lieux ; alinéa « Version 17 » de l'annexe H). Chaque ancre comptée à 1 sur la sortie de la passe 2.

**Lieux où le « complément 1 » était réservé à la règle n° 8** : trois. Deux dans l'alinéa « Version 13 » de la remarque 5 de « Version 12 » — la citation de R-4292 et la phrase du rédacteur de la version 13 qui la suit — et un en tête, la citation de R-4296. Les deux citations restent à la lettre ; une phrase de la version 17 les corrige à chaque lieu.

**Lieux des trois empreintes entières** (lignes de la version 17) :
- programme des étapes 3 à 6, `1f04cb46…` : 2 lieux (l. 107, l. 407) ;
- programme des étapes 6 bis et 7, `ed91813a…` : 2 lieux (l. 107, l. 408) ;
- programme des étapes 8 et 9, `67052a4b…` : 6 lieux (l. 20, 107, 342, 409, 1154, 1216), dont un de plus qu'à la version 16 : la règle de la remarque 2, du jeu du contrôleur.

## 4. Écarts et limites

- **Les onze ancres du jeu du contrôleur n'ont pas été recomptées par moi avant la passe 1** : le contrôleur les dit comptées à 1, l'outil exige une occurrence unique et a rendu « FAIT », et la sortie est égale à son essai. Les dix-sept autres ancres l'ont été.
- **R-4336 dit l'ordre des compléments, non leur nom.** Le texte garde la forme de nom de R-4292 sans l'écrire pour chaque numéro ; il ne dit ni combien de compléments la mère écrit, ni ce que chacun regroupe. Dit à l'alinéa « Version 17 », non tranché.
- La remarque 4 énumère ce qui vient avant le complément de la règle n° 8 (fichiers gelés, constats, contrôle de l'empreinte du programme 8–9, dossiers) : c'est la liste du contrôleur (son § 7), reprise sans fixer d'ordre entre eux.
- Les mots « réponse du 2026-11-20, 22:03Z » des corrections du contrôleur restent : je n'ai pas lu cette réponse, seulement R-4335 et R-4336.
- La date de la ligne de date est celle de `date -u` (22:14Z) ; le journal de la passe 3 dit 22:15:42Z.
- Un `mkdir -p` de mon dossier ; un `git fetch origin main`, un `git show` redirigé, un `git rev-parse` ; des `grep -n -o` sur des fichiers nommés.
- Aucun lancement d'un programme, du code ni d'un essai ; aucun tirage ; aucune pièce d'autorisation ni de contrôle ; aucun appel à un fournisseur ; aucune dépense ; aucune écriture dans le dépôt.
- **À ne pas verser** : `lecture-registre-origin-main.md`, copie de lecture du registre.

Signé : rédacteur des v15 à v17, modèle F.
