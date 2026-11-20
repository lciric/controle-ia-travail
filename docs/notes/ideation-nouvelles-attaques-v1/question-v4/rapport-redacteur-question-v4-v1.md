# Rapport du rédacteur — question de la course « nouvelles attaques », v4 sans nom ni donnée interne dans ce qui peut être servi — v1

Pièce de travail (classe C), écrite le 2026-11-20 sur le mandat `docs/notes/ideation-nouvelles-attaques-v1/mandat-redacteur-question-v4-sans-donnees-internes-v1.md` (`50d8300be854c7487557e21cce1db7f1693bd6fc225b615295f446a0b5fd373c`, vérifiée contre son compagnon). Processeur seul : aucun appel à un fournisseur, aucune dépense, aucun lancement, aucune écriture dans le dépôt, aucun commit. Aucune méthode d'attaque, aucun procédé, aucun identifiant de modèle dans ce rapport ni dans la v4.

## 0. Verdict

1. La v4 est écrite : seize remplacements à texte exact par l'outil contre-lu, dont trois de tenue. Le prénom du directeur du programme n'y figure plus nulle part (compte à 0 sur le fichier entier, donc sur toute partie servie).
2. Aucune règle de fond n'est changée. Le § 4, « La question servie », est égal à l'octet à celui de la v3 : il ne portait aucune donnée interne.
3. **Ce que la v4 ne règle pas** : l'en-tête et le § 1 portent toujours des chemins du dépôt, des empreintes, des accords et un commit. La v4 n'est donc propre que si l'orchestrateur ne sert pas l'en-tête ni le § 1 (remarque 1, non tranchée).
4. **Autre texte servi à contrôler** : la synthèse d'antériorité que l'ordre de course cite comme pièce servie porte le prénom du directeur à deux lignes et des identifiants de registre (§ 4). Je n'y ai rien écrit.

## 1. Pièces lues et empreintes vérifiées

| pièce | chemin | empreinte | contrôle |
|---|---|---|---|
| question v3, scellée | `docs/notes/ideation-nouvelles-attaques-v1/conception-v3/question-course-nouvelles-attaques-v3.md` | `2cf2aae035beef43e999e3cd8b0fb7ba3808649b3cc8b29661c1244b0540415b` | recalculée ; égale à la copie de `main` tirée par `git show FETCH_HEAD:prereg/ideation-nouvelles-attaques-v1/question-course-nouvelles-attaques-v3.md` |
| ordre de course v3 | même dossier, `ordre-course-nouvelles-attaques-v3.md` | `b12cdc1292178d4c7fe80370439507efd1d04d07f47d0bc6315b8c429d329e22` | recalculée ; égale à celle que le préenregistrement court v6 cite |
| préenregistrement court v6 | `prereg/ideation-nouvelles-attaques-v1/preenregistrement-court-course-nouvelles-attaques-v6.md`, tiré de `main` | `7e240c8c9b059171e06b416d5cf8b14c6822978f84219ad2d9770a32f90f11c5` | recalculée sur la copie tirée |
| outil | `scripts/remplacer_texte_exact_v1.py` | `391db990734dd36f7c827b8b6c77dc0de1bda324f671b65748ccfe68c56a53d6` | recalculée |

Écart de lettre du mandat, sans effet : la copie de `main` de la question v3 n'est pas dans l'arbre de travail local ; je l'ai tirée de `FETCH_HEAD` dans mon dossier et comparée par empreinte. Le `git fetch origin main` a réussi du premier coup.

## 2. Quelle partie de la question est servie : ce que disent les textes

Les textes ne tranchent pas.

- Ordre de course v3, § 1 : « l'organisme reçoit la question scellée » ; § 4, « Pièces servies : la question scellée ; une pièce d'antériorité attestée « aucune recette » par la mère » ; § 3, sonde de refus : « chaque espèce reçoit la question ». Lecture possible : le fichier entier.
- Préenregistrement court v6, « Hypothèse », point 1 : « servie telle quelle (§ 4 de la question), avec ses cases et ses champs fermés (§ 5) » ; point 4 : « la question scellée ; une pièce d'antériorité […] ; une case ; et, aux générations 2 et 3, le registre entier des tentatives […]. Rien d'autre. » ; sonde de refus de l'espèce 6 : « la question scellée, telle qu'elle est servie, et rien d'autre : ni case, ni registre, ni pièce d'antériorité ». Lecture possible : le § 4, avec le § 5.
- Le véhicule (orchestrateur, lanceur, additif, configuration) reste à écrire : aucun code ne fixe aujourd'hui ce qui part.

J'ai donc traité comme « pouvant être servis » les § 2 à § 7 (les règles, la question, les cases, les champs), et comme « à ne pas servir » l'en-tête et le § 1 (provenance, empreintes, comparaison aux trois questions déjà scellées).

## 3. Relevé de la question v3, ligne par ligne

Aucun courriel, aucun identifiant de session, aucun nom de dépôt distant, aucun nom de famille dans la v3. Le nom de famille cherché est celui que porte le nom du dépôt distant ; le mandat ne le donne pas.

### 3.1 § 2 à § 7 (peuvent être servis)

| ligne v3 | § | donnée interne | ce que j'en fais | rang du remplacement |
|---|---|---|---|---|
| 24 | 2 | identifiants de registre « R-606, R-610, R-611 ; N-065, rôle 1 » | remplacés par « (ceux que nomme la règle d'antériorité entière) » ; la liste entière reste à l'ordre de course, § 9, source 2 bis | 4 |
| 29 | 2 | nom de règle du dépôt « règle R8 » | parenthèse retirée ; l'énoncé de la règle reste dans la phrase | 5 |
| 29 | 2 | nom de règle du dépôt « règle R7 » | parenthèse retirée ; l'énoncé reste | 6 |
| 29 | 2 | nom de règle du dépôt « règle R3 » | parenthèse retirée ; l'énoncé reste | 7 |
| 33 | 3 | **prénom du directeur** et identifiant « R-607 » | « mot de [prénom], R-607 : » devient « mot du directeur du programme : » ; la citation est gardée | 8 |
| 34 | 3 | identifiant « N-065, rôle 2 » | parenthèse retirée | 9 |
| 35 | 3 | identifiant « N-053, point 5 » | parenthèse retirée | 10 |
| 35 | 3 | accord « GO-2026-11-19-89 » | parenthèse retirée | 11 |
| 36 | 3 | **prénom du directeur** et identifiant « R-609 » | « que [prénom] décide (R-609). » devient « que le directeur du programme décide. » | 12 |
| 40 à 48 | 4 | aucune | rien ; égal à l'octet | — |
| 57 | 5 | nom de fichier du dépôt (les consignes permanentes) et « papiers A, B et C » | « , telles que ses consignes permanentes les résument » | 13 |
| 58 | 5 | identifiant « N-056 » | « décision du programme sur les bases boîte blanche » | 14 |
| 68 | 6 | chemin du dépôt (le dossier de données) | « aucune donnée du dossier de données du dépôt » | 15 |
| 72 | 7 | identifiant « R-611 » | parenthèse retirée | 16 |

Table des renvois retirés, pour le lecteur du dépôt (elle n'est pas dans la v4) : condition 1 du § 2 → R-606, R-610, R-611, N-065 rôle 1 ; zone vierge → règle R8 ; pièce lue sur PDF → règle R7 ; même rang → règle R3 ; niveau de l'idée → R-607 ; fiches comme matériau → N-065 rôle 2 ; aucun score de moniteur dans l'organisme → N-053 point 5 ; rien du juge aux proposeurs → GO-2026-11-19-89 ; reformulation après refus → R-609 ; source de l'axe « menace du programme » → le fichier des consignes permanentes, papiers A, B et C ; source de l'axe « étage de lecture » → N-056 ; revue de sécurité externe → R-611.

Gardé dans les § 2 à § 7, et pourquoi : les noms descriptifs de pièces internes (« questions v1 et v2 du pilier attaque », « question du coffre v2 », « ordre de course, § 4 et § 9 », « le coffre », « le portier », « la mère »). Ce ne sont ni des noms de personne, ni des identifiants, ni des chemins ; les retirer de la condition 1 du § 2 changerait la règle d'antériorité. À juger par le contre-lecteur (remarque 3).

### 3.2 En-tête et § 1 (à ne pas servir ; non récrits, hors la tenue)

| lignes v3 | ce qu'elles portent |
|---|---|
| 3 à 5 | empreintes de la v1, de la v2, de la contre-lecture et du contrôle du différentiel ; noms de ces fichiers |
| 6 | noms de règles du dépôt (R2, R1 et R3) |
| 7 | chemin du mandat, deux empreintes, accords GO-2026-11-19-94, -95, -96, chemin du registre des accords, nom de branche, commit, empreinte |
| 8 | noms des pièces sœurs, empreinte du devis |
| 14 à 16 | trois chemins du dépôt et trois empreintes (questions déjà scellées) |
| 18 | accord GO-2026-11-19-96 |

La tenue de la v4 y ajoute, à la phrase de version : l'empreinte de la v3, le chemin et l'empreinte de l'outil, le chemin et l'empreinte du mandat. Aucun prénom, aucun nom.

## 4. Ce que l'ordre de course et le préenregistrement court disent servir d'autre

| texte servi | où c'est dit | existe-t-il par un chemin cité ? | relevé |
|---|---|---|---|
| pièce d'antériorité attestée « aucune recette » par la mère | ordre, § 4 ; préenregistrement, « Hypothèse », point 4, et « Ce qui reste à écrire », point 6 | oui, comme candidate : `rapports/fille-ideation-1-v1/synthese-anteriorite-pilier-attaque-v2b.md` (`b828d800913c8960d04b6822de8f10fc51ee573c660c84f6658ea6ba68796b8d`, recalculée), « ou une version neuve » | relevé par motifs étroits, sans lire le texte : **prénom du directeur aux lignes 258 et 304** ; identifiants de registre aux lignes 27 (N-054, R-610), 94 (R-1795), 200 (R-610, N-054), 258, 302 et 303 (R-1821) ; chemin du dépôt aux lignes 116, 157 et 201 (l'état de l'art) ; une empreinte à la ligne 298. Rien écrit dans ce texte. Il ne peut pas être servi tel quel. |
| une case | préenregistrement, point 4 ; question, § 5 | non : le tirage reste à jouer et à sceller | les valeurs des axes (question, § 5) ne portent aucune donnée interne ; l'identifiant de case servi est à contrôler quand il existera |
| le registre des tentatives, générations 2 et 3 | ordre, § 5, option (a) ; préenregistrement, point 5 | non : produit en course | sa forme (champs fermés, nom, énoncé d'une ligne, classe, comptes) ne prévoit aucune donnée interne ; à contrôler par la garde du véhicule |
| consigne de rôle, préambule, titre de la section servie | ordre, § 2, points 3 et 4 (additif, configuration) ; préenregistrement, « Ce qui reste à écrire », point 1 | non : l'additif et la configuration restent à écrire | rien à relever ; à contrôler à leur écriture |
| sonde de refus (espèces 1 à 5 ; espèce 6) | ordre, § 3 ; préenregistrement, « Sonde de refus de l'espèce 6 » | non comme texte propre : elle porte « la question scellée, telle qu'elle est servie, et rien d'autre » | couverte par la question v4, sous la remarque 1 |
| témoins plantés | ordre, § 7 | non : la mère les écrit | servis au portier et aux juges, donc à contrôler aussi |

Le préenregistrement court v6 lui-même n'est pas servi. Il porte le prénom du directeur, des noms de clés et des accords ; c'est sans objet tant qu'il ne part dans aucune invite.

## 5. Contrôles faits

- Chaque texte ancien compté à 1 par `grep -c -F -e` sur la v3 avant l'appel (seize comptes à 1 ; cinq ancres resserrées et recomptées, pour que le texte neuf ne figure pas dans l'ancien, règle 5 de l'outil).
- Outil : « FAIT : 16 remplacement(s) », cible `2cf2aae0…`, sortie `47160d37de50cca412389fd539f9edf383ff64345513e51287ddcba5618d4654`.
- `grep -c -i -F` sur le prénom et le nom de famille, v4 entière : **0** (`sortie-grep-prenom-nom-question-v4-v1.txt`).
- Relevé par motifs sur la v4 : plus aucun identifiant de registre, nom de règle, empreinte, chemin ni nom de fichier après le § 1 ; ce qui reste est aux lignes 4 à 9 (en-tête) et 15 à 19 (§ 1).
- Différentiel `diff -u` relu en entier : seules les seize zones changent.

## 6. Remarques non tranchées

1. **Ne servir que la partie servie.** L'en-tête et la partie servie sont dans le même fichier. Trois manières, à trancher par la mère et le directeur du programme, puis par le mandat du véhicule : (a) l'additif fixe le titre de la première et de la dernière section servies, et l'orchestrateur n'envoie que les octets entre ces deux titres, avec une garde éprouvée sur un cas sain et sur un artefact, qui refuse le départ si le texte à envoyer porte un motif interdit (prénom, nom, identifiant de registre, empreinte, chemin) ; (b) la partie servie vit dans un fichier à part, scellé, que la question cite par son empreinte, et l'orchestrateur ne sert que ce fichier ; (c) le fichier entier est servi, et il faut alors une version de plus qui vide aussi l'en-tête et le § 1, au prix de la provenance (règle R6). L'ordre de course prévoit déjà « le titre de la section servie » à l'additif (§ 2, point 3), ce qui va vers (a).
2. **Quelle partie est la partie servie** (§ 4 seul ; § 4 et § 5 ; § 2 à § 7) n'est écrit nulle part sans ambiguïté. La v4 tient dans les trois cas.
3. **Noms descriptifs de pièces internes gardés** dans les § 2, § 3 et § 5 (« pilier attaque », « coffre », « ordre de course »). Je ne les tiens pas pour des données internes au sens du mandat ; un avis contraire demande de récrire la condition 1 du § 2, donc un mot sur une règle.
4. **Trois noms de règles du dépôt retirés** (§ 2). Ce ne sont pas des identifiants de registre ; je les ai retirés comme « autre donnée interne », l'énoncé de chaque règle restant dans la phrase. Si le contre-lecteur les veut gardés, trois remplacements tombent.
5. **« mot du directeur du programme »** : le mandat demande « le directeur du programme » ; après « de », la contraction donne « du ». La seconde occurrence est à la lettre.
6. **Le préenregistrement court v6 ne vaut que pour la question à l'empreinte `2cf2aae0…`** (son paragraphe « La question », et sa racine de graines, tirée de cette empreinte). Une question v4 scellée demande donc une version neuve du préenregistrement, et la racine des tirages change avec elle, sauf mot contraire. C'est un nœud ; je ne le tranche pas.
7. **L'ordre de course v3 et le rapport de conception citent la question v3** par son nom ; leurs renvois sont à porter par leurs propres versions ou par un erratum.
8. La ligne « Auteur » de la v4 reste celle de la v3 ; le rédacteur de la v4 est dit à la phrase de version, comme le fait le préenregistrement court.
9. La synthèse d'antériorité (§ 4) demande une version neuve, expurgée, avant d'être servie ; hors de ce mandat.

## 7. Fichiers rendus

Dossier : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/redacteur-question-v4/`. Chaque fichier a son compagnon `.sha256`.

- `question-course-nouvelles-attaques-v4.md` (`47160d37de50cca412389fd539f9edf383ff64345513e51287ddcba5618d4654`), son journal `question-course-nouvelles-attaques-v4.md.journal-remplacements-v1.json` ;
- `remplacements-question-v3-v4-v1.json` ;
- `differentiel-question-v3-v4-v1.diff` ;
- `sortie-grep-prenom-nom-question-v4-v1.txt` ;
- `rapport-redacteur-question-v4-v1.md` (ce rapport) ;
- copies tirées de `main`, pour contrôle : `tire-de-main-question-v3.md`, `tire-de-main-preenregistrement-court-v6.md`.

— rédacteur neuf, modèle F
