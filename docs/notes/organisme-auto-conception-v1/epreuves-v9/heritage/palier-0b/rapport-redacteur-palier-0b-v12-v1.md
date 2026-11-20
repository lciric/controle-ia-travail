# Rapport du rédacteur — préenregistrement du palier 0b, version 12 (erratum du commit après le code v5) — v1

- Auteur : rédacteur neuf, modèle F. Je n'ai écrit aucune version de ce préenregistrement, aucun code, aucune vérification. Pièce de travail (classe C) rendant une pièce décisive (classe A), à faire contre-lire.
- Date : 2026-11-20 ; `date -u` à 14:00Z en cours de travail ; heure du journal de l'outil : 14:06:34Z.
- Mandat : `P/mandat-redacteur-palier-0b-v12-erratum-du-commit-v1.md` (`1485b861c8f3670ecb94703a694641ceeb50117abd605f576848f9248db7fd73`), empreinte recalculée avant tout geste, égale à celle du compagnon. P = `docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/`.
- Conditions : processeur seul ; aucun lancement du code du palier, aucun tirage, aucun appel à un fournisseur de modèles, aucune dépense, aucune écriture dans le dépôt, aucun commit, aucune publication ; rien sous `archives-reponses-modeles/` ni sous `/root/.claude/` ; aucun heredoc, aucun code en ligne ; une commande simple par appel. **Aucun refus de permission, de classifieur ni de garde.**

## 0. Résultat

- **Version 12** : `preenregistrement-heritage-palier-0b-etage-processeur-v12.md`, empreinte `a4234028486ce0d6cfe24d15e991e0bf03bd6e56397395f4b3cb53fa86d5d398` (1 004 lignes ; la v11 en a 952).
- **Outil** : `scripts/remplacer_texte_exact_v1.py` (`391db990…`), un seul appel, réussi au premier essai : « FAIT : 42 remplacement(s) », aucun avertissement. Fichier des remplacements : `remplacements-palier-0b-v11-v12-v1.json` (`7e85da7064cfb23800a5240ab8f9455c42df5833e2c4cf439f548b2ab5b9338f`), écrit avec l'outil d'écriture de fichiers. Journal : `…-v12.md.journal-remplacements-v1.json` (`06f5d162b25f2226264aa68b749f9b123e1f9294892239aa6846a44a94faaf3c`).
- **Différentiel** `diff -u` v11 → v12 : `differentiel-palier-0b-v11-v12-v1.diff`, empreinte `97c639f2e4e6e0b3431baf06cfc4408fb7f33d501fed178fbca34be18ca466a5` (252 lignes).
- **Lignes qui commencent par « - Commit du code d'analyse : »** dans la v12 : **1** (`grep -c -e "^- Commit du code d'analyse : "`) ; lignes qui contiennent ce préfixe (`grep -c -F -e`) : **1**. Dans la v11 : 1.
- **Table** : le bloc qui suit cette ligne (lignes 10 à 67 de la v12, entre les deux lignes « ``` ») compte 58 lignes ; retrait de deux espaces ôté, il est égal à l'octet à `P/table-empreintes-code-v5.txt` (`56bddae7…`, `cmp` muet), elle-même égale à l'octet au bloc du § 11 du rapport du code v5 (lignes 1999 à 2056, `cmp` muet). La forme à deux espaces de retrait est celle de la v11, que le vérificateur du code v5 a lue par le verrou ; j'ai lu la fonction `lire_en_tete_du_texte` : elle retire les blancs de bord de chaque ligne du bloc.

## 1. Vérifications faites avant d'écrire

- Empreintes recalculées et égales à leur compagnon : v11 (`9faf31a3…`), contrôle v10 → v11 (`88c37d86…`), rapport du code v5 (`a2966a3c…`), table extraite (`56bddae7…`), vérification du code v5 (`0e2c46bb…`), outil (`391db990…`).
- `git fetch origin main` réussi ; `git merge-base --is-ancestor e308b84d68a85416fab1a80b0c116858d24b85a5 origin/main` : code de sortie 0 ; `git rev-parse origin/main` rend ce même commit (il est la tête de `main`). Le rapport du code v5 relu à ce commit a l'empreinte `a2966a3c…`.
- `registres/go.md` (`766a63e7…`) et `registres/decisions.md` (`ed74b95e…`) lus par `git show origin/main:… >` : ligne `GO-2026-11-20-25` (l. 556), R-4285 (l. 4423), R-4210 (l. 4348), citées à la lettre dans la v12, le nom de famille de modèle que porte R-4285 étant omis et marqué « […] ».

## 2. Les 42 remplacements (rang dans le JSON ; chaque ancre comptée une fois par `grep -c -F -e` dans la v11 avant l'appel)

| rang | lieu | objet |
|---|---|---|
| 1 | titre | v11 → v12 |
| 2 | ligne de version | statut ; alinéa « Version 12 » ; la version 11 dite au passé |
| 3 | ligne de version | « il reste le contrôle… » : dit de la version 11, contrôle fait |
| 4 | ligne de version | l'erratum du commit est refait |
| 5 | ligne de date | **NE-4**, à la lettre du contrôle v10 → v11 |
| 6 | ligne de date | date et conditions de la version 12 |
| 7 | ligne « Commit du code d'analyse » | commit `e308b84d…` de `main`, forme que le verrou lit, table des 58 fichiers annoncée |
| 8 à 22 | bloc de la table | quinze lignes : deux ajouts de lignes (sorties et bancs v3 et v4), douze empreintes changées, la ligne `statistique` suivie de la ligne neuve `verrou` |
| 23 | en-tête | mandat de la version 12 ; R-4285 et R-4210 citées |
| 24 | documents qui font foi | pièces de la version 12 |
| 25 | section « Seuil » | colonne du seuil d'arrêt (NE-3, silence n° 9) |
| 26 | section « Seuil » | mots et clé de la zone médiane (silence n° 10, ajout (b)) |
| 27 | section « Seuil » | ordre de dérivation, plis puis permutation (silence n° 11) |
| 28 | B7 bis | `etapes.lancer_etape_4`, dossiers, paramètres, clés rendues (silence n° 12, ajout (b)) |
| 29 | B8 | le verrou tel que le code v5 l'écrit (silences n° 1 à 8) ; précisions n° 2 et n° 7 ; décisions de la mère sur les n° 8, 14, 15 ; n° 16 en remarque |
| 30 | B9, garde 27 | ce que la garde compare (silence n° 13 et sa précision) |
| 31 | ordre des opérations, point 2 | ce qui est fait, ce qui reste |
| 32 | section « Contre-lecture » | alinéa « Version 12 » |
| 33 | section « Contre-lecture » | fichiers à donner et points à vérifier pour la version 12 |
| 34 | annexe C | fichier d'essais du verrou, comptes d'essais, banc |
| 35 | réserve 24 | commit du code v5 ; ce que je n'ai pas fait |
| 36 | réserve 25 | « reste celui du code v3 » dit des versions 9 à 11 |
| 37 | annexe H, « Erratum du commit » | inscription refaite |
| 38 | annexe H, remarque 4 | renvoi à B8, « Version 12 » |
| 39 | annexe H, « Version 9 », § 6 | les trois lieux « tels quels » sont mis à jour |
| 40 | annexe H, « Ce qui demande un code v5 » | fait par le code v5, vérifié |
| 41 | annexe H, code v5, point 1 | **NE-3**, à la lettre du contrôle v10 → v11 |
| 42 | fin du texte | section neuve « Version 12 » : table des neuf points, décisions de la mère, remarque 5, ajouts et précisions, tenue, ce qui n'est pas changé |

Deux sont à la lettre du contrôle de la version 11 (rangs 5 et 41), quinze refont la table (8 à 22), vingt-cinq sont de moi. Les 43 comptes (les 42 ancres, et le préfixe de la ligne du commit) valent tous 1.

## 3. Points où la lettre ne suffit pas (en remarque ; aucun n'est tranché)

1. **Où s'écrivent les contrôles des silences n° 14 et n° 15** (remarque 5 de la v12, annexe H). Le mandat dit la racine et le texte « fixés dans la pièce d'autorisation de ces étapes » et le contrôle « sur main » écrit « dans la pièce d'autorisation ». Or la pièce du verrou, telle que le code v5 la lit, porte exactement quatre lignes et toute autre ligne la fait refuser. Pièce du verrou ou pièce à part : la v12 écrit les mots du mandat et pose la question, sans trancher.
2. **Silence n° 8, « à la ligne « Commit du code d'analyse » de la pièce d'autorisation »** : la pièce n'a pas de ligne de ce nom, mais un champ `commit du code`, que le verrou tient égal à la ligne « Commit du code d'analyse » du texte. J'ai écrit : « au commit du code de la pièce d'autorisation, que le verrou tient égal à celui de la ligne… ». À confirmer.
3. **« Comme pour la portée 200 »** (mandat, n° 8) : je n'ai trouvé ces mots ni dans la v11, ni dans `go.md`, ni dans `decisions.md` (trois comptes à 0). Je ne les ai pas écrits dans la v12.
4. **NE-4** : porté (rang 5). R-4285 ne le demande pas et ne cite aucune décision par son numéro ; mais R-4210, que le rapport du code v5 cite (en-tête et § 6, point 3), dit « NE-3 […] et NE-4 (heure de la v11) : oui, avec l'erratum du commit ». J'ai lu « décision citée » comme couvrant R-4210. Si la mère l'entend autrement, le rang 5 se retire seul (et les mentions de NE-4 aux rangs 2, 32, 33 et 42).
5. **Le détail des décisions sur les n° 8, 14 et 15** (« à la main », `git merge-base --is-ancestor`, « de ces étapes ») vient du mandat, non de la lettre de R-4285, plus courte ; la v12 le dit (« le mandat de la version 12 détaille ce qu'elle dit en abrégé »).
6. **« Le contre-lecteur du code »** : le texte (« Ce qui demande un code v5 ») dit le code v5 vérifié par lui ; la vérification est signée d'un vérificateur neuf, modèle S. La v12 le dit sans changer la phrase reprise.
7. **Les trois remarques du § 7 du rapport du code v5** (dont le constat des essais) ne sont pas portées : le mandat ne les met pas dans ce que la v12 porte. La v12 le dit.
8. **Forme de la date de la version 12** : « `date -u` à 14:00Z en cours de travail ; l'heure exacte est au journal de l'outil » — la forme que NE-4 corrige pour la version 11, l'heure du journal (14:06:34Z) n'étant connue qu'après l'appel. Tenue possible à la prochaine version.
9. **Comptes d'essais et de banc de l'annexe C** (107 ; 113) : repris du rapport du code v5 et de sa vérification, non rejoués.
10. **Statut** : « erratum du commit après le code v5, à faire contre-lire » est de ma plume.

## 4. Écarts et gestes à déclarer

- Un des trois `git show` porte sur le commit `e308b84d…` et non sur le nom `origin/main` (relecture du rapport du code v5 « au commit », que le mandat demande) ; c'est le même commit que la tête d'`origin/main`.
- Une commande a échoué sans rien changer : un `grep -P` de recherche d'espaces insécables, refusé par la locale ; refait avec `env LC_ALL=C.UTF-8` (compte 0 : la v11 n'a ni espace insécable, ni apostrophe courbe, ni tabulation, ni retour chariot).
- Le compte des lignes « qui commencent par » emploie `grep -c -e "^…"` (sans `-F`, pour l'ancre de début de ligne), en plus du `grep -c -F -e`.
- **Lu de la v11** (par une copie pliée à 1 800 colonnes, de lecture seule) : l'en-tête entier, la section « Seuil », B7 bis, B8, B9, l'ordre des opérations, la liste d'arrêt, la section « Contre-lecture », l'annexe C, l'annexe D, les réserves, et de l'annexe H : « Ce qui demande un code v4 », « Erratum du commit », la table de la version 7 et toute la « Version 9 ». Le reste n'a pas été lu ; l'outil garantit qu'il est repris à l'octet.
- Du code v5, lu sans rien lancer : `lire_en_tete_du_texte` et trois constantes.
- Aucun identifiant de modèle ni de session dans le JSON (recherche de mots : 0).

## 5. Fichiers de mon dossier

`/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/redacteur-palier-0b-v12/` :
- `preenregistrement-heritage-palier-0b-etage-processeur-v12.md`, son compagnon, son journal et le compagnon du journal (écrits par l'outil) ;
- `remplacements-palier-0b-v11-v12-v1.json` et son compagnon ;
- `differentiel-palier-0b-v11-v12-v1.diff` et son compagnon ;
- ce rapport et son compagnon ;
- fichiers de travail, non rendus : `go-main.md`, `decisions-main.md`, `rapport-code-v5-au-commit.md`, `v11-plie-lecture-seule.txt`, `table-du-rapport-section-11.txt`, `bloc-de-la-v12-sans-retrait.txt`.

*Rédacteur neuf, modèle F.*
