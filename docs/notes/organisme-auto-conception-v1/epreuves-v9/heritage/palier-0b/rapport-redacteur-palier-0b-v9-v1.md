# Rapport du rédacteur — préenregistrement du palier 0b (étage sur processeur), version 9 : erratum après le code v4 — v1

- Auteur : rédacteur neuf, modèle F. Pièce de travail (classe C). Travail du 2026-11-20 ; `date -u` lu à 08:10Z en cours de travail ; heure de la version 9 au journal de l'outil : 08:18:55Z.
- Mandat : `docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/mandat-redacteur-palier-0b-v9-erratum-v1.md` (`6f5e4603194b820d266e381543532c4f167c4c1be2ec795ac2f8fc1395506f7c`), vérifié par son compagnon avant tout autre geste.
- Conditions : processeur seul ; aucun tirage, aucun étalonnage, aucun audit, aucun lancement du code de l'étage ; aucun appel à un fournisseur de modèles, aucune dépense ; aucune écriture dans l'arbre du dépôt, aucun commit. Réseau : un seul `git fetch origin main`, demandé par le mandat (il écrit `FETCH_HEAD` sous `.git/`), puis deux `git show` redirigés vers mon dossier. Un seul programme lancé, par son chemin : l'outil de remplacement (Python 3.13.18). Aucune commande de liste ; une commande simple par appel ; aucun heredoc, aucun code en ligne. Rien de lu sous `archives-reponses-modeles/` ni sous `/root/.claude/`. **Aucun refus de permission, de classifieur ni de garde.**

P : `docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/`. Mon dossier : `/tmp/claude-0/-home-user-controle-ia-travail/227b647d-2ece-5654-bf04-8493b3ed2f19/scratchpad/redacteur-palier-0b-v9/`.

## 1. Verdict

La version 9 est écrite par **28 remplacements exacts**, appliqués au premier appel, sans refus ni avertissement de l'outil : les neuf du contrôle de la version 8 (T1 à T9), à la lettre, et dix-neuf du rédacteur. Elle n'est **ni contre-lue ni scellable en l'état** : quatre points où la lettre du GO ou des décisions ne suffit pas sont écrits en remarque, avec une proposition, **sans être tranchés** ; elle demande un code v5 ; le commit inscrit en tête reste celui du code v3.

## 2. Fichiers rendus (chacun avec son compagnon `.sha256`)

| fichier | empreinte SHA-256 |
|---|---|
| `preenregistrement-heritage-palier-0b-etage-processeur-v9.md` (284 717 octets) | `0aacc4ea275e97812647ce0ce4723c9bd01d76f32a8f0c42462d00be2fe7bc2e` |
| `remplacements-preenregistrement-palier-0b-v8-v9.json` (28 remplacements) | `9351af5e2600fcc5a6debe272f89469deb58b8a15c33dff28a6c7613a0f68e21` |
| `preenregistrement-heritage-palier-0b-etage-processeur-v9.md.journal-remplacements-v1.json` | `701dae2528606330b82275c171a3f5c13f97a7942acd40160de64ed9c6487ab5` |
| `differentiel-preenregistrement-palier-0b-v8-v9.diff` (`diff -u` ; 15 lignes de la version 8 changées, 82 lignes côté version 9) | `74a81fabf2ac6f8bd22c045ea329ceebf6f18bd1107d8bd30c686a8305dc7a1e` |
| `rapport-redacteur-palier-0b-v9-v1.md` (ce rapport) | dans son compagnon |

Pièces de travail, non scellées, dans le même dossier : `go-main.md` (`ea02d0be4127136171eed347ea929f2e2c587c6c2fc1ecc17459e25f80ff968d`) et `decisions-main.md` (`5529afb83d5987b4032aee48d1bea8cb38cd51868e68ed8d51c2174d1b1a58ff`), rendus par `git show` au commit de `main` `e50ff62efe2b70a3db8525a8abf46c73110209e2`. La version 8 est intacte (compagnon revérifié après l'opération).

## 3. Sources vérifiées

Chaque empreinte vérifiée par son compagnon (`env -C DOSSIER sha256sum -c`) et égale à celle du mandat : la version 8 (`fd275af8…`) ; le contrôle de la version 8 (`a68a46a0a480dd9f6237a2fe1aae1a6e4716d478cb75c109c8033a87f645331a`) ; le rapport du rédacteur de la version 8 (`510266a587b21bbfa4a71afaeb95cf31e54c7ce2e934142dfde3b26ef059ee9b`) ; le rapport du développeur du code v4 (`2947c4f1…`) ; la vérification du code v4 (`183b17d2…`) ; l'outil (`391db990734dd36f7c827b8b6c77dc0de1bda324f671b65748ccfe68c56a53d6`, lu en entier).

Lu en entier : le mandat, le contrôle de la version 8, la vérification du code v4, le rapport du rédacteur de la version 8. Lu en partie : la version 8 (en-tête, section « Seuil », B2, B7 bis, B8, B9, ordre des opérations, critères de lecture, liste d'arrêt, « Contre-lecture », réserves 15 à 24, annexe H ; le reste non relu) ; le rapport du développeur du code v4 (§ 0 à § 8 et le début du § 9). Dans le code v4, deux recherches de mots (`audit.py`, `tirages.py`), rien de lancé.

## 4. Les 28 remplacements

Chaque ancre a été comptée avant l'appel par `grep -c -F -e` : résultat 1 pour les 28. Ce compte est un compte de lignes ; l'outil a ensuite confirmé une seule occurrence pour chacune.

| n° du JSON | lieu | objet | origine |
|---|---|---|---|
| 1 | titre | « v8 » devient « v9 » | rédacteur |
| 2 | ligne de version, statut | code v4 vérifié, code v5 à écrire | rédacteur |
| 3 | ligne de version | phrase « Version 9 » : ce qu'elle porte, les nœuds tranchés, le sens de « cette version » | rédacteur |
| 4 | ligne de date | **T1** | contrôle |
| 5 | ligne de date | date de la version 9 ; le `git fetch` | rédacteur |
| 6 | en-tête | ligne « Mandat de la version 9 », avec les citations de GO-2026-11-20-25, R-4123, R-4135, R-4150 | rédacteur |
| 7 | documents qui font foi | « pièces de la version 9 » | rédacteur |
| 8 | section « Seuil » | contenu et réunis des doses : renvoi à la règle calibrée de signalement | rédacteur (GO, point 2) |
| 9 | section « Seuil » | M défini ; lectures de la forme des doses au seuil M + 2 σ₀ | rédacteur (GO, point 1) |
| 10 | section « Seuil » | ce qui est rapporté ; règle calibrée de signalement | rédacteur (GO, point 2) |
| 11 | section « Seuil » | précisions des silences n° 1 à 5 | rédacteur |
| 12, 13 | garde 25 | artefact de la dose au nouveau seuil ; cinq artefacts de plus | rédacteur |
| 14 | B8 | pièce d'autorisation du verrou (R-4123) | rédacteur |
| 15 | B8 | fichier des étiquettes (silence n° 10) ; rôle « plis » | rédacteur |
| 16 | B7 | écart-type contrôlé par la note D8 (silence n° 9) | rédacteur |
| 17 | « Contre-lecture » | **T2** | contrôle |
| 18 | « Contre-lecture » | alinéa « Version 9 » | rédacteur |
| 19 | fichiers à donner | **T3** | contrôle |
| 20 | « Contre-lecture » | fichiers et points de la version 9 | rédacteur |
| 21 | réserve 23 | **T4** | contrôle |
| 22 | code v4, point 2 | **T5** | contrôle |
| 23, 24, 25 | annexe H | **T6, T7, T8** | contrôle |
| 26 | nœud 2, option (a) | **T9** | contrôle |
| 27 | réserves | réserve 25 (ce que l'on savait ; le 0,63 ; ce qui n'est pas recalculé) | rédacteur |
| 28 | fin de l'annexe H | section « Version 9 » : cinq points, quatre remarques, tenue, liste du code v5, ce qui n'est pas changé | rédacteur |

Les textes T1 à T9 sont ceux du § 5 du contrôle, sans retouche ; mes ajouts voisins sont dans des remplacements séparés (n° 5 et 18), pour que les neuf se contrôlent à l'octet.

## 5. Points où la lettre ne suffit pas — écrits en remarque, jamais tranchés

1. **Remarque 1 — la borne basse (GO, point 1).** Le GO fixe le seuil d'arrêt (moyenne permutée M + 2 σ₀) et ne dit pas ce que devient « au plus 0,55, tenue » quand M + 2 σ₀ tombe sous 0,55 (possible si M est sous 0,5 ; l'essai a vu 0,472). La section « Seuil » écrit les trois cas sûrs (arrêt au-dessus des deux ; tenue au-dessous des deux ; « non départagée » au-dessus de 0,55 et au plus au seuil) et nomme le quatrième « non tranché ». Propositions : (i) l'arrêt prime ; (ii) le plus grand de 0,55 et de M + 2 σ₀. Ma proposition : (ii), confiance moyenne. Le texte dit que l'étape 3 ne part pas avant le mot.
2. **Remarque 2 — la zone médiane du contenu et des réunis (GO, point 2).** Le GO ne dit pas si une exactitude de contenu ou réunie au-dessus de 0,55 et au plus au seuil lie l'étage payant, comme pour la forme. Le texte écrit ce qui est commun aux deux lectures (pas de signalement ; « non départagée » au compte rendu) et laisse la mention ouverte. Ma proposition : elle ne lie pas, confiance moyenne à haute (sinon les 20 à 25 % de R-4135 ne baissent pas).
3. **Remarque 3 — le jeu de la garde 27 (silence n° 8).** Le texte ne dit ni le proposeur, ni le nombre de sources, ni qui appelle `etape_4_jeu_de_la_garde_27`. Ma proposition : appelée par le lancement de l'étape 4, lecteur réglé pour la tenue au réglage de B2 (τ = 2), deux sources (trois en autre choix).
4. **Remarque 4 — le verrou D6 (R-4123).** La décision donne l'auteur, le lieu et les quatre champs ; le texte les écrit à la lettre du mandat. Elle ne dit pas ce que « scellée » exige par programme, d'où vient chaque « valeur attendue », la forme des champs, comment « sur `main` » se vérifie, ni ce que le manifeste inscrit à la place de la constante retirée. Une proposition pour chacun.

## 6. Choix de mots qui sont les miens, à contrôler

- **Le seuil du signalement calibré est M + 2 σ₀**, le même que pour la forme : je lis « règle calibrée étendue » comme la règle telle que le point (1) la laisse. Le GO ne l'écrit pas en toutes lettres.
- **Le nom du rôle « plis »** (silence n° 3) : valeur du rédacteur, dite telle dans le texte.
- **Cinq artefacts ajoutés à la garde 25** (valeurs plantées de A, de M et de σ₀), pour que les deux règles neuves aient leur cas sain et leur artefact (règle R5).
- **La réserve 25** et la phrase « l'étape 3 ne part pas avant qu'il le soit ».
- **Citations des registres** : à la lettre, mais avec des « […] » là où la ligne nomme qui écrit l'erratum, qui a vérifié le code, et la session d'où le mot est relu — le mandat interdit tout identifiant de modèle. Le texte le dit.

## 7. Écarts entre le mandat et les pièces, signalés

- Le mandat nomme « point 5 » de la vérification la liste des silences : elle est à son **§ 6** (le § 5 porte sur les sorties). Le texte cite le § 6.
- Le mandat attribue le mot sur le 0,63 à « R-4123, point 3 de la mère » : la ligne R-4123 lue sur `main` n'a pas de points numérotés et ne parle pas du 0,63 ; elle dit « Les constats du développeur vont à l'erratum ». J'ai écrit la phrase demandée (« un constat de l'essai, non une mesure du palier ; aucun seuil ne change ») sur la foi du mandat, à la réserve 25 et à l'annexe H.
- Le rapport du développeur donne deux écritures du nom du fichier des étiquettes ; le code v4 (`tirages.py`) tranche : nom du manifeste sans extension, suivi de `-etiquettes.txt`.

## 8. Ce que le code v5 devra changer

1. `audit.py`, lecture de la forme des audits des mondes par dose, et table de l'étape 3 : seuil d'arrêt M + 2 σ₀ au lieu de 0,55 + 2 σ₀ ; colonne du seuil ; cas de la remarque 1 après son mot.
2. `audit.py` : les six exactitudes de contenu et réunies des audits des mondes par dose lues par la règle calibrée de signalement, jamais un arrêt ; les quatre des audits de lois à la lettre ; mention de la zone médiane après la remarque 2.
3. Étape 3 (`mondes.py`, et `graines.py` si les rôles y sont tenus) : la graine des plis de la lecture observée dérivée par le code sous le rôle « plis », non plus reçue de l'appelant.
4. `graines.py`, `constantes.py`, manifeste (`tirages.py`) : le verrou avec la pièce d'autorisation, après la remarque 4 ; modules contrôlés contre la table du texte ; constante de l'empreinte de la version 6 retirée ; en-tête de `constantes.py` corrigé (silence n° 13).
5. Le jeu de la garde 27 : appelant, proposeur, nombre de sources, après la remarque 3.
6. Essais et banc : les artefacts neufs de la garde 25 ; défauts neufs (seuil resté à 0,55 + 2 σ₀ ; contenu des doses resté à la lettre ; signalement calibré qui arrête ; calibrage étendu aux audits de lois ; plis observés reçus de l'appelant ; chaque condition du verrou).
7. Sans changement : silences n° 1, 2, 4, 5, 9, 10 (le texte écrit ce que le code v4 fait déjà) ; n° 6, 7, 11, 12 non touchés.

Puis : vérification du code v5, erratum du commit refait et contre-lu.

## 9. Laissé tel quel, non fait

- **Laissés tels quels, nommés à l'annexe H (« Version 9 », point 6)** : le titre et le premier alinéa de l'annexe H ; ses deux tables de fin ; les nœuds 1 et 2 dans leurs mots d'avant les GO ; la ligne « Commit du code d'analyse » et la réserve 24 (code v4 « à venir ») ; l'ordre des opérations, point 2 ; les passages d'histoire qui disent encore « 0,55 + 2 σ₀ ».
- **Non traité, hors mandat** : le texte facultatif du § 6 du contrôle de la version 8 (action après un arrêt de l'étalonnage) ; les plis tirés par suite (non retenu par le GO).
- **Non recalculé** : les ordres de grandeur de la réserve 23 pour le seuil M + 2 σ₀ (dit à la réserve 25).
- **Non faits** : relecture de la version 9 en entier après l'outil (je m'appuie sur ses contrôles internes et sur le compte des lignes du différentiel) ; validateur du gabarit ; recherche des listes « Ne pas écrire » par programme. Mes ajouts ne citent aucun travail publié et ne portent aucun identifiant de modèle.

## 10. Reste à faire, hors de mon mandat

Verser les fichiers ; mots de la mère (et de Lazar si elle en juge ainsi) sur les remarques 1 à 4 ; contre-lecture de la version 9 par un sous-agent neuf (règle R2) ; code v5 et sa vérification ; erratum du commit ; scellement par la mère.

*Rédacteur neuf, modèle F.*
