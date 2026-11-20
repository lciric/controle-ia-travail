# Rapport du rédacteur — préenregistrement du palier 0b (étage sur processeur), version 11 : correction du contrôle de la version 10, renvois à R-4182, remarque 1 tranchée par Lazar — v1

- Auteur : rédacteur neuf, modèle F. Pièce de travail (classe C). Travail du 2026-11-20 ; `date -u` lu à 10:45Z ; heure de la version 11 au journal de l'outil : 10:47:54Z.
- Mandat : `P/mandat-redacteur-palier-0b-v11-v1.md` (`9426728cde7c375ac87ec4bdecd55d5e3831699de750c042a061ea60548fd15c`), vérifié par son compagnon avant tout autre geste.
- Conditions : processeur seul ; aucun tirage, aucun lancement du code du palier ; aucun appel à un fournisseur de modèles, aucune dépense ; aucune écriture dans l'arbre du dépôt, aucun commit. Un seul programme lancé, par son chemin : l'outil de remplacement. Aucune commande de liste, une commande simple par appel, aucun heredoc, aucun code en ligne. **Aucun refus de permission, de classifieur ni de garde.** Écarts : § 6.

P : `docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/`. Mon dossier : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/redacteur-palier-0b-v11/`.

## 1. Verdict

La version 11 est écrite par **24 remplacements exacts** sur la version 10 (`ac2deb4d…`), appliqués au premier appel, sans refus ni avertissement de l'outil : neuf à la lettre du contrôle de la version 10 (C1, six renvois à R-4182, NE-1, NE-2) et quinze du rédacteur. 14 lignes de la version 10 sont touchées : 1, 3, 6, 209, 357, 359, 429, 904, 912, 917, 934, 942, 947, 950. Aucune n'est dans « Hypothèse », « Prédiction », « Métrique », « Valeurs gelées », « Les six critères », « Critères de lecture gelés » ni « Liste d'arrêt ». Elle n'est **ni contre-lue ni scellable en l'état** : il reste le contrôle du différentiel, le code v5, sa vérification et l'erratum du commit. Une réserve demande un mot (§ 5, point 1).

## 2. Fichiers rendus (chacun avec son compagnon `.sha256`)

| fichier | empreinte SHA-256 |
|---|---|
| `preenregistrement-heritage-palier-0b-etage-processeur-v11.md` | `9faf31a3dd0278b562c62fbded81222b674f6c5df225006f9e0e8d610b720989` |
| `remplacements-preenregistrement-palier-0b-v10-v11.json` (24 remplacements) | dans son compagnon |
| `preenregistrement-heritage-palier-0b-etage-processeur-v11.md.journal-remplacements-v1.json` | dans son compagnon |
| `differentiel-preenregistrement-palier-0b-v10-v11.diff` (`diff -u`) | dans son compagnon |
| `rapport-redacteur-palier-0b-v11-v1.md` (ce rapport) | dans son compagnon |

Pièces de travail, sans compagnon : `go-main-6048bb22.md` (`registres/go.md` de `main` au commit `6048bb22c63f50be958f4f9525cb607c09c7cb30`) ; `go-main.md` (rendu par erreur d'une autre branche, § 6 ; non employé). La version 10 est intacte (compagnon revérifié après l'opération).

## 3. Sources vérifiées

Empreintes vérifiées par compagnon : mandat ; version 10 (`ac2deb4d…`, égale au mandat) ; rapport du rédacteur de la version 10 ; contrôle de la version 10 (`98975c9e…`, égale au mandat) et ses deux jeux d'essai ; contrôle de la version 9 ; outil (`391db990…`). Lus en entier : le mandat, le contrôle de la version 10, ses deux jeux, le contrôle de la version 9, le rapport du rédacteur de la version 10, l'outil. Lue en partie : la version 10 (lignes 1 à 7, 194 à 211, 355 à 359, 409 à 443, 895 à 950, et le voisinage de chaque mention de « remarque 1 », de « M + 2 σ₀ » et de « non tranché »).

**Ligne GO-2026-11-20-41** (ligne 572 de `registres/go.md` au commit `6048bb22…`) : colonne de la décision : « **Organisme, palier 0b, remarque 1 du contrôle v8→v9 : option (ii).** Le seuil d'arrêt de l'étape 3 des audits par dose est le plus grand de 0,55 et de la moyenne permutée + 2σ₀ (une exactitude au plus 0,55 n'arrête jamais) ; précise GO-2026-11-20-25 (1). À porter dans la v11 du préenregistrement du palier 0b. » ; mot cité : « Recommandation du contrôleur : (ii), confiance moyenne à haute. : go », égal au mot du mandat. La version 11 la cite ainsi en tête, sans les identifiants de session et d'événement de la colonne de source.

**Les neuf textes du contrôleur.** Repris de ses deux jeux ; chaque ligne de ses deux jeux se retrouve entière dans mon JSON (`grep -v -c -F -x -f` rend 0 pour chacun) ; les jeux avaient été comparés à sa pièce (§ 5 et § 7 du contrôle) à la lecture.

## 4. Les 24 remplacements

Chaque ancre comptée avant l'appel par `grep -c -F -e` : 1 pour les 24 ; l'outil confirme une occurrence chacune.

| rang | ligne v10 | objet | origine |
|---|---|---|---|
| 1 | 1 | titre : « v10 » devient « v11 » | rédacteur (tenue) |
| 2 | 3 | ligne de version : alinéa « Version 11 » (mandat, contrôle, ligne GO-41 citée, ce qui est porté, 24 remplacements, ce qui reste) ; « versions 9, 10 et 11 » ; la version 10 passe au passé | rédacteur (tenue ; remarque 1) |
| 3 | 3 | **texte 1** (renvoi à R-4182) | contrôle, § 5 |
| 4 | 3 | « ce texte ne la tranche pas » : dit de la version 10 ; version 11, tranchée | rédacteur (remarque 1) |
| 5 | 3 | « ne se scelle pas avant qu'elle soit tranchée » : elle l'est | rédacteur (remarque 1) |
| 6 | 6 | **NE-1** | contrôle, § 7 |
| 7 | 6 | date de la version 11 | rédacteur (tenue) |
| 8 | 209 | section « Seuil », tête des lectures de la forme : version 11, le plus grand de 0,55 et de M + 2 σ₀ | rédacteur (remarque 1) |
| 9 | 209 | section « Seuil », cas « au plus 0,55 mais au-dessus de M + 2 σ₀ » de la forme : pas d'arrêt, tenue | rédacteur (remarque 1) |
| 10 | 209 | règle de signalement, même cas : « non tranché, comme pour la forme (remarque 1) » devient « ni signalement ni mention : ce cas suit la forme » | rédacteur (remarque 1 ; **réserve, § 5, point 1**) |
| 11 | 357 | garde 25 : artefact neuf, forme plantée au plus 0,55 et au-dessus de M + 2 σ₀, aucun arrêt (« un code qui arrête sur une exactitude au plus 0,55 échoue ») ; le même pour le contenu | rédacteur (remarque 1 ; l'artefact manquait) |
| 12 | 357 | **C1** | contrôle, § 7 |
| 13 | 359 | **NE-2** | contrôle, § 7 |
| 14 | 429 | **texte 2** | contrôle, § 5 |
| 15 | 429 | « Contre-lecture » : alinéa « Version 11 » (contrôle de la version 10 fait, son verdict ; mot de Lazar ; ce qui reste) | rédacteur (tenue ; « Tenue de la version suivante » du contrôle) |
| 16 | 904 | remarque 1, titre : « tranchée par Lazar, GO-2026-11-20-41, option (ii) » | rédacteur (remarque 1) |
| 17 | 904 | remarque 1, fin : la version 10 au passé ; version 11, règle, ce que cela touche, ce qu'elle ne lit pas, report au signalement | rédacteur (remarque 1) |
| 18 | 912 | **texte 3** | contrôle, § 5 |
| 19 | 917 | **texte 4** | contrôle, § 5 |
| 20 | 934 | **texte 5** | contrôle, § 5 |
| 21 | 942 | code v5, point 1 : le seuil à coder | rédacteur (remarque 1) |
| 22 | 947 | code v5, point 6 : essai et défaut de banc « arrêt sur une exactitude au plus 0,55 » | rédacteur (remarque 1) |
| 23 | 950 | **texte 6** | contrôle, § 5 |
| 24 | 950 | « Ce qui revient à la mère » : les quatre remarques tranchées | rédacteur (remarque 1) |

**Lieux touchés pour la remarque 1, et pourquoi** : ligne de version (rangs 2, 4, 5 : elle disait la remarque posée et le texte non scellable avant son mot) ; section « Seuil » (8, 9 : le seuil et le cas ouvert ; 10 : le renvoi « non tranché (remarque 1) » du signalement) ; garde 25 (11 : l'artefact demandé manquait) ; « Contre-lecture » (15) ; remarque 1 de l'annexe H (16, 17) ; code v5 (21 : « attend son mot » ; 22 : essai et défaut) ; « Ce qui revient à la mère » (24).

## 5. Points où la lettre ne suffit pas — en remarque

1. **Le même cas dans la règle calibrée de signalement (rang 10 ; et la moitié « contenu » des rangs 11 et 22 ; une phrase des rangs 2 et 17).** La ligne GO-41 ne parle que du seuil d'arrêt, et le mandat dit de ne pas changer la règle de signalement ; mais il dit aussi de reprendre tout lieu qui dit la remarque 1 « non tranchée », et la version 10 écrivait ce cas « non tranché, comme pour la forme (remarque 1) ». Je n'ai pas pu le laisser tel quel sans que le texte dise ouverte une remarque fermée. J'ai écrit « ni signalement ni mention : ce cas suit la forme », en m'appuyant sur les mots « comme pour la forme » et sur l'annexe H, § 2 (« Le seuil y est le même que pour la forme »). Aucun seuil de la règle ne change. **C'est ma lecture, non la lettre du mot de Lazar : au contrôleur et à la mère de la confirmer ou de la retirer.** Le rang 10 est séparé ; les rangs 2, 11, 17 et 22 la répètent en une phrase chacun.
2. **« Tenue », « sans mention ».** La ligne dit « n'arrête jamais ». « Elle est tenue » vient du nom de l'option (ii), « la tenue prime », et de « au plus 0,55, tenue » des versions 7 et 8. « Sans mention » (garde 25, code v5 point 1) est mon mot : une exactitude de forme au plus 0,55 ne recevait de mention dans aucune version.
3. **Colonne du seuil de la table de l'étape 3.** Le point 1 du code v5 garde « la colonne du seuil de la table porte M + 2 σ₀ ». Quand M + 2 σ₀ est sous 0,55, le seuil d'arrêt est 0,55 : la colonne porte-t-elle M + 2 σ₀ ou le plus grand des deux ? Non touché, non tranché.
4. **Texte 1, commit de R-4182.** Porté mot pour mot, avec `ae64b9d3…`, le commit relu par le contrôleur. Son § 5 dit d'inscrire un autre commit « si la version qui les porte relit `main` à un autre commit » : je n'ai pas relu `registres/decisions.md` (le mandat ne demande que `go.md`), donc rien changé.
5. **Passages laissés, qui se lisent avec la remarque tranchée** : annexe H, § 1, « Mot de Lazar » et « Ce que cela touche » (l. 901, 903), qui disent la ligne GO-25 ; réserve 25 (l. 532, « avec M sous 0,5, c'est l'inverse » : sous l'option (ii) le seuil ne descend pas sous 0,55) ; « Points de la version 9 à vérifier » (l. 443) ; les phrases d'histoire des versions 9 et 10 de la ligne de version et de « Contre-lecture », couvertes par la clause de l'alinéa « Version 11 ».
6. **Heure.** La date dit « `date -u` à 10:45Z ; l'heure exacte est au journal » (10:47:54Z) : c'est la forme que NE-1 corrige pour la version 10 ; à reprendre de même si la mère le veut.

## 6. Écarts et à déclarer

- **`git fetch` relancé une fois.** Le premier a réussi (`main` à `74060b4f…`), mais une autre session a déplacé la référence de la dernière récupération avant mon `git show` : `FETCH_HEAD` désignait la branche `lot/compte-organisme-v1` (`92c677dc…`), et `go-main.md` en vient (319 lignes, sans aucune ligne du 20 novembre). Constaté par `git rev-parse` (deux fois) et par la lecture du fichier `.git/FETCH_HEAD`. Second `git fetch origin main` (`6048bb22…`), puis `git show` **par le commit explicite** et non par `FETCH_HEAD`, vers un nom neuf : écart à la lettre du mandat, pour ne pas relire une référence mouvante.
- Une recherche (`grep -n`) a rendu une sortie trop longue, que l'environnement a rangée de lui-même sous `/root/.claude/projects/…/tool-results/` ; je ne l'ai ni demandée ni relue.
- Statut inchangé (« brouillon corrigé, à faire contre-lire »), dit à la ligne de version ; pas de section « Version 11 » à l'annexe H ; pas de ligne « Fichiers à donner » pour le contrôle de la version 11.
- Non fait : relecture de la version 11 en entier après l'outil (contrôles internes de l'outil, journal, différentiel) ; validateur du gabarit. Mes ajouts ne portent aucun identifiant de modèle ni de session, et ne citent aucun travail publié.

## 7. Reste à faire, hors de mon mandat

Verser les fichiers ; contrôle du différentiel de la version 10 à la version 11 par le même contrôleur (en premier : § 5, point 1) ; code v5 et sa vérification ; erratum du commit ; scellement par la mère.

*Rédacteur neuf, modèle F.*
