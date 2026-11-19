# Commande de lecture de l'apprentissage des sondes sur la tâche (étape B bis de T0.7) — v4

Écrite le 2026-11-18 par le préparateur (sous-agent neuf, modèle Fable 5.2), sous `mandat-preparateur-lecture-bbis-v1.md` (`a6e027ce…`), son complément `complement-mandat-preparateur-lecture-bbis-v1.md` (`9a8b5515…`), son second complément `complement-2-mandat-preparateur-lecture-bbis-v1.md` (`8777bcf5…`) et les règles communes (`5f303a9c…`), compagnons vérifiés.

**Version 2.** La version 1 (`commande-lecture-bbis-v1.md`, `b308c9b12803ea58b470a7670881fc30274f0c93c04bc288d893146c6641e615`) reste, non jouée (R12). Cette version traite les cinq constats provisoires du premier contre-lecteur (`arret-contre-lecteur-commande-refus-crochet-v1.md`, `a903b87b…`) et les huit points du second complément ; chaque passage changé est dans `differences-commande-lecture-bbis-v1-v2.md`, avec son fondement. Tout le reste est le texte de la version 1, à l'octet.

**Version 3.** La version 2 (`commande-lecture-bbis-v2.md`, `4eea2d8a39c46ad2da27b7bd72852897a90eb122350ed55e5498eaaafc32b33d`) reste, non jouée (R12). Sa contre-lecture par un lecteur neuf d'un autre modèle (`contre-lecture-commande-lecture-bbis-v2.md`, `146b4d0483668df9fc6fb2661c4e4fad1425221a5061049e9731fb7128390925`) conclut « jouable après corrections mineures » : aucun constat majeur, sept mineurs. Cette version porte les remplacements m1 à m7 tels que le rapport les écrit, trois décisions d'organisation de la conductrice (sur m5, sur m6 et sur la note n3), et ce qui en découle strictement ; chaque passage changé est dans `differences-commande-lecture-bbis-v2-v3.md`, avec son fondement. Tout le reste est le texte de la version 2, à l'octet. **Cette version ne joue que le premier lancement.**

**Version 4 — forme en scripts.** La version 3 (`commande-lecture-bbis-v3.md`, `195207cf9180c0c667b9dd087f768278ee8ffafea8351a654b2899d32f3df0b3`) reste (R12). Le lecteur-opérateur l'a jouée jusqu'au § 1.2 compris ; au § 1.3, l'outil de terminal a refusé le bloc pour sa forme, et l'opérateur s'est arrêté. Rien n'a été lancé, rien n'est consommé. Sous le troisième complément du mandat (`complement-3-mandat-preparateur-lecture-bbis-v1.md`, accordé par la session mère, R-3540), cette version change **la forme seulement** : chaque bloc est un script versé et scellé sous `scripts/lecture-bbis-v4/`, lancé par une ligne unique en syntaxe simple. Aucun contrôle n'est changé, ajouté ni retiré, hors le rejeu écrit du relevé des têtes (§ 1.1). Aucun script ne supprime ni ne réécrit un fichier existant. `differences-commande-lecture-bbis-v3-v4.md` donne, pour chaque bloc de la version 3, le script qui le porte et la preuve de l'égalité de fond. Tout le reste est le texte de la version 3, à l'octet.

**Écrite par simple lecture.** Aucun script de cette commande n'a été joué, ni entier ni en partie : ni le module, ni sa garde, ni une de ses fonctions, ni le programme de la preuve après coup. Les scripts ont seulement passé un contrôle de syntaxe (`bash -n`), hors de toute exécution ; les trois fonctions neuves du fichier commun ont été essayées sur un dossier jouet. Les blocs des § 1.1 et § 1.2 ont tourné une fois sous leur forme de la version 3 ; les scripts qui les portent, non.

**Cette commande ne contient aucune garde rejouée à part** : la garde d'ouverture s'exécute en tête de la lecture, dans le module (complément au quatrième addendum, § 3 et § 6). Tout ce qui précède le lancement est fait de commandes `git` en lecture, de calculs d'empreintes et de comptes de lignes.

**Ce que le lecteur-opérateur ne fait jamais** : ouvrir à l'œil un fichier sous `diag/`, `donnees/`, `runs/`, `docs/verdicts/` ; afficher la sortie d'un lancement au-delà de ce que le § 5.2 demande ; afficher le constat de forme destiné au juge ; arrêter un processus ; relancer ; corriger ; pousser.

**Aucune commande d'arrêt de processus n'est écrite dans cette commande**, sous aucune forme. Une lecture lente mais vivante n'est jamais arrêtée.

## 0. Module de lecture en vigueur ; ce qui fait foi

- **Module qui lit** : `src/controle_ia/t07bbis/lecture_v5.py`, empreinte `dac9f8590784a2bf93d312128b09e89a7a21c04509700f3a3ee8c7a81a28064c`.
- **Ligne qui le fonde** : complément au quatrième addendum, CQ-3, bloc « Nouveau, qui fait foi » (`prereg/T0.7-etape-B-bis-v1-addendum-ecart-4-complement-v1.md`, l. 285) : « `lecture_v5` pour la lecture du point 10 du plan (les v1 à v4 restent, R12 ; […] la v5 est rattachée par le quatrième addendum et son complément, non par la fiche de `CODE-BBIS` ; la v4 n'est ni rattachée ni jouée pour la lecture ; ». Règle de préséance : même texte, § 0, et CQ-2.
- **Rattachement** : fiche `registres/t07-etape-b-bis/rattachement-lecture-v5-bbis-v1.json` (`cd14195d396a779da954619c9a3405741fe11e2f98bf4aae3767cb87a5036ca0`), ligne `RATTACHEMENT-LECTURE-V5-BBIS` du registre voisin. Le module n'est pas dans la fiche de code : une troisième ligne `CODE-BBIS` est interdite.
- **Fiche de code** (`registres/t07-etape-b-bis/code-bbis-v2.json`, `4b28535c…`) : elle reste en vigueur pour les 63 fichiers qu'elle cite, pour l'entropie des graines et pour le niveau décisif. Relevé au premier tour : les 63 empreintes sont égales sur le disque et au commit de la fiche `05cd22aa…`. La commande le revérifie dans l'arbre de lecture (§ 1.4).
- **Textes** : texte scellé `prereg/T0.7-etape-B-bis-v1.md` (`0ae6210f…`) ; addenda 1 (`f00eda8a…`), 2 (`18baeac3…`), 3 (`e5604cbd…`), 4 (`5ef929ea…`) et complément au quatrième (`12c90873…`) ; feu `registres/t07-etape-b-bis/feu-bbis-v7.txt`, § 12 et § 13.
- **Entropie et graines** (plan, point 12 ; troisième addendum, TA-3) : aucune n'est passée en argument. Le module lit l'entropie dans la fiche que cite la ligne `CODE-BBIS` en vigueur (`lecture_v5.py`, l. 1693-1695) et dérive une graine par clé `bbis/tirages/<ligne>`.

### Paramètres donnés par la conductrice au lancement

| nom | valeur |
|---|---|
| commit de `main` qui porte les inscriptions | `4aefb5b166b55a5ff7341454770a64caab923f52` |
| tête de la branche de travail après l'étape 0 (`TETE_TRAVAIL`) | donnée par la conductrice, 40 caractères ; **l'opérateur l'écrit dans un fichier, par l'outil d'écriture de fichiers** (ci-dessous) |
| numéro du lancement | `1`, **donné en argument simple** aux scripts des § 4.2 à § 5.5 ; cette version ne joue que le premier lancement (§ 5.3) et ses scripts refusent tout autre numéro |
| décision sur le risque de redémarrage | donnée par la conductrice au lancement du second temps |
| nom, sur le distant, de la branche de l'arbre de lecture | `claude/lecture-verdict-etape-b-bis-v1-arbre-de-lecture` (poussée par la conductrice, § 4.1) |

Relevé par les noms au commit `4aefb5b1…` (préparateur, `git show <commit>:<registre> | grep -c`) : les lignes `ADDENDUM-ECART-1-BBIS`, `-2-BBIS`, `-3-BBIS`, `ADDENDUM-ECART-4-BBIS`, `ADDENDUM-ECART-4-COMPLEMENT-BBIS` et `RATTACHEMENT-LECTURE-V5-BBIS` y figurent une fois chacune ; aucun fichier dont le nom commence par `lecture-t07` ou `arret-etape-b` n'y est suivi ; le commit de la course en est un ancêtre.

### État laissé par la version 3, et comment la lecture repart

État, par les noms (troisième complément du mandat ; je n'ai rien lu ni touché dans le dossier de travail de la version 3) :
- la fusion du commit de `main` `4aefb5b1…` et le journal du registre propre (ligne d'en-tête seule) sont faits et poussés : tête de la branche de travail `fd11004640544592885a218809b7f43415fb28f5` ;
- dossier de travail de la version 3, `…/scratchpad/lecture-bbis/` : son fichier de paramètres, trois relevés du § 1.1 (deux refusés, un conforme), l'arbre de lecture `arbre-de-lecture-v1` monté à `fd110046…` sur la branche locale `lecture/bbis-arbre-de-lecture-v1`, 32 entrées dans son index, aucun commit local ; l'intégrité de ces 32 fichiers n'est pas prouvée depuis un redémarrage de la machine ;
- rien n'a été lancé ; aucune preuve n'est écrite ; rien n'est poussé de l'arbre de lecture.

**Choix : un arbre de lecture neuf, sous un nom neuf, à la tête neuve ; l'ancien reste en place ; rien n'est supprimé.** Raisons :
- **La forme seule change.** Verser les scripts change la tête de la branche de travail. Avec un arbre neuf monté à cette tête, chaque contrôle de la version 3 qui cite `TETE_TRAVAIL` reste mot pour mot : tête de la branche de travail (§ 1.1), montage (§ 1.2), parent de la tête de l'arbre de lecture (§ 4.2). Reprendre l'ancien arbre aurait demandé deux têtes et des contrôles réécrits, et de sauter le § 1.2, dont la garde `neuf` refuse un arbre qui existe déjà.
- **Ce que les textes demandent est tenu.** Une tête qui descend du commit de la course et contient le commit de `main` qui porte les inscriptions (quatrième addendum, QA-1, point (P5), et § 4, point 2 ; premier complément du mandat, point 2) : vrai de la tête neuve, contrôlé aux § 1.1 et § 2. L'ancien arbre l'aurait tenu aussi : le module, les textes scellés, les registres et la fiche n'ont pas changé entre les deux têtes, ce que le § 1.4 vérifie par les empreintes. Le choix ne tient donc pas à une exigence des textes, mais à la forme et à la traçabilité.
- **Traçabilité.** Le manifeste de la lecture cite le commit de l'arbre où elle se joue (`manifeste.py`, l. 78-104 ; R9). Avec l'arbre neuf, l'ascendance de ce commit porte la commande et les scripts effectivement joués.
- **Intégrité.** L'arbre neuf est extrait à neuf des trois branches, puis contrôlé objet par objet (§ 1.3) ; l'index de l'ancien, d'intégrité non prouvée, ne sert pas.
- **Place.** 11 Go libres relevés par la conductrice ; l'arbre pèse environ 3,4 Go : il reste environ 7,6 Go. Les sorties de la lecture sont un manifeste, un fichier de lecture et une sortie imprimée, en texte. Cela tient ; le seuil de 6 Go du § 1.1 est gardé tel quel.

Noms neufs, et eux seuls : dossier de travail `…/scratchpad/lecture-bbis-v4/` ; arbre de lecture `arbre-de-lecture-v4` ; branche locale `lecture/bbis-arbre-de-lecture-v4`. Le nom de la branche sur le distant ne change pas : elle n'a jamais été poussée.

**Ce qui reste en place, et qu'aucun script ne lit ni ne touche** : le dossier de travail de la version 3, son arbre de lecture et sa branche locale. Cette branche pointe sur `fd110046…`, ancêtre de la tête de travail : elle n'ajoute aucun commit à ce que la garde parcourt. Leur retrait est une suppression : **je ne l'écris pas ; il reste à un humain**, quand il le voudra.

### Étape 0 — gestes de la conductrice, avant de lancer le lecteur-opérateur

La fusion et le journal sont faits : **ils ne sont pas rejoués**. Restent, chacun en une ligne simple :

1. verser et commiter, sur la branche de travail : cette commande, ses différences avec la version 3, le dossier `scripts/lecture-bbis-v4/` (scripts et compagnons), le troisième complément du mandat ; pousser la branche de travail ;
2. juste avant de lancer l'opérateur, la récupération complète du distant, en lecture seule (décision d'organisation sur m5) :

```bash
git -C /home/user/controle-ia-travail fetch origin
```

3. relever l'état et la tête, qui est `TETE_TRAVAIL` :

```bash
git -C /home/user/controle-ia-travail status --porcelain --untracked-files=all
```

```bash
git -C /home/user/controle-ia-travail rev-parse HEAD
```

- Le statut doit être vide : le § 1.1 exige l'arbre principal propre.
- **Récupération complète du distant : décision d'organisation de la conductrice** (constat m5 de la contre-lecture de la version 2). L'opérateur ne fait que la comparaison (§ 1.1) ; sa permission d'appel au distant reste celle des trois branches nommées et de la lecture des têtes. Si le § 1.1 relève une branche absente ou à une autre tête, parce que le distant a avancé depuis, on ne lance pas : la conductrice refait cette récupération, puis l'opérateur rejoue le § 1.1 (règle du § 1.1).
- La ligne d'en-tête du journal ne porte pas la chaîne que le module compte comme une ligne d'ouverture (`lecture_v5.py`, l. 1436) : ne pas la changer.
- Le journal est créé « avec sa seule ligne d'en-tête, commité avant la lecture » (quatrième addendum, § 6.5, point 8) : c'est fait.

### Scripts, fichier commun, fichier de la conductrice (premier geste du lecteur-opérateur)

**Chaque geste de l'opérateur est une ligne unique, en syntaxe simple** : `bash`, le chemin du script, et, des § 4.2 à § 5.5, l'argument `1`. Rien d'autre : ni accolade, ni redirection, ni tube, ni texte en ligne. L'opérateur ne recopie le contenu d'aucun script dans son terminal.

Les scripts sont sous `/home/user/controle-ia-travail/scripts/lecture-bbis-v4/`, chacun avec son compagnon ; leurs empreintes sont dans le fichier des différences. Chacun relit le fichier commun `commun.sh` (paramètres et fonctions : c'est le fichier des paramètres de la version 3), parce que l'état du terminal ne tient pas d'un appel à l'autre.

| paragraphe | script | qui le lance |
|---|---|---|
| § 1.1 | `1-1-depot-et-tetes.sh` | opérateur |
| § 1.2 | `1-2-montage-de-l-arbre.sh` | opérateur |
| § 1.3 | `1-3-entrees.sh` | opérateur |
| § 1.4 | `1-4-code-et-textes.sh` | opérateur |
| § 2 | `2-preuve-anteriorite-et-entree-conjointe.sh` | opérateur |
| § 4.1 | `4-1-commit-local.sh` | opérateur |
| § 4.1 | `4-1-conductrice-preuve-et-branche.sh` | **conductrice** |
| § 4.2 | `4-2-releve-avant-lancement.sh 1` | opérateur |
| § 5.1 | `5-1-lancement.sh 1` | opérateur |
| § 5.1 bis | `5-1-bis-attente.sh 1` | opérateur |
| § 5.2 | `5-2-releve-apres-lancement.sh 1` | opérateur |
| § 5.2 | `5-2-constat-de-forme-pour-le-juge.sh 1` | opérateur |
| § 5.2 | `5-2-motif-non-consommee.sh 1` | opérateur, état « non consommée » seulement |
| § 5.4 | `5-4-sorties-portees-et-ligne-de-lecture.sh 1` | opérateur |
| § 5.5 | `5-5-preuve-apres-coup-sur-ordre-ecrit.sh 1` | opérateur, **sur ordre écrit de la conductrice seulement** |

**Comment entrent les paramètres de la conductrice.**
- `TETE_TRAVAIL` : **par un fichier, que l'opérateur écrit par l'outil d'écriture de fichiers**, jamais par le terminal. Chemin : `/tmp/claude-0/-home-user-controle-ia-travail/1829cd11-38fd-5ef8-9688-6827f39023bc/scratchpad/lecture-bbis-v4/parametres-conductrice-v4.txt`. Contenu : une seule ligne, `TETE_TRAVAIL=` suivi des 40 caractères donnés par la conductrice. Le fichier commun lit cette ligne sans l'exécuter et s'arrête si le fichier manque, si la ligne n'y est pas une fois, ou si la valeur n'a pas la forme d'un identifiant de commit. C'est le premier geste de l'opérateur, et le seul fichier qu'il écrit à la main.
- Le numéro du lancement : **par argument simple**, `1`.
- La décision sur le risque de redémarrage : donnée par la conductrice au lancement du second temps ; elle n'entre dans aucun script.

**Deux temps.** Premier temps : § 1 à § 4.1 (mise en place, preuve relevée à part, commit local des entrées) ; l'opérateur rend la tête de l'arbre de lecture et s'arrête. La conductrice commite et pousse alors la pièce de la preuve sur la branche de travail, puis pousse la branche de l'arbre de lecture sous le nom ci-dessus (§ 4.1). Second temps, sur son message : § 4.2 à § 5.4.

**Règle pour tous les blocs d'avant le lancement** (§ 1 à § 4) : chacun finit par `CONCLUSION`. « ON NE LANCE PAS » veut dire : l'opérateur s'arrête, rend à la conductrice le chemin et l'empreinte du relevé et les lignes `DEFAUT`, et ne joue pas la suite. Ce ne sont pas des arrêts du programme de lecture : ils ne consomment rien, la lecture n'a pas été lancée. Les relevés ne portent que des noms, des empreintes, des identifiants de commit et des comptes.

## 1. Mise en place des fichiers

Les entrées de la liste blanche (plan, point 1) sont sur trois branches, relevées par les noms au premier tour :

| origine | branche locale de suivi | tête | ce qu'on en extrait |
|---|---|---|---|
| sorties de la course | `origin/donnees/t07-etape-b-bis-v2` | `7322049d…` (règles communes) | les 20 fichiers de `runs/`, `diag/`, `donnees/` du run `20261118-154143-bbis-t07-v1` (dix fichiers et leurs compagnons) |
| course de confirmation (7b) | `origin/calcul/t06-confirmation-7b-v1` | `55c3e3eb…` (feu, § 4) | cinq fichiers nommés et leurs compagnons ; **jamais** `lecture-sondes-t06.json` ni `resume.json`, qui sont sur cette branche et dans la liste « Jamais » |
| pièce « mots et coût » | `origin/verdict/t06-mots-et-cout-compte-3-v1` | aucune tête nommée par un texte ; le fichier est ancré par l'empreinte de la ligne `ISSUE-MOTS-ET-COUT-T06` | `issue-mots-et-cout-t06.json` et son compagnon |

Les fichiers cités par les lignes `VERDICT-P3BIS`, `CODE-MOTS-ET-COUT-T06` et `AUDIT-FUITES-T07` sont déjà suivis sur la branche de travail.

### 1.1 Dépôt à histoire complète, branches présentes, têtes

```bash
bash /home/user/controle-ia-travail/scripts/lecture-bbis-v4/1-1-depot-et-tetes.sh
```

- **Appels au distant permis au lecteur-opérateur, en lecture seule, et eux seuls** (second complément, point 4 ; la conductrice l'écrit aussi dans son mandat) : la récupération des trois branches nommées ci-dessus (`git fetch origin <branche>`), la lecture des têtes du distant (`git ls-remote --heads origin`), ici et au § 4.2. Ils n'écrivent rien sur le distant. Aucun autre appel à un service extérieur.
- Une branche du distant absente localement, ou dont la tête locale n'est pas celle du distant : la garde chercherait le premier ajout du fichier de lecture de l'étape B sur une histoire incomplète sans le savoir (`lecture_v5.py`, l. 862-871, `git log --all`). On ne lance pas ; la conductrice fait récupérer la branche.
- **Rejeu du relevé des têtes — seul contrôle que la version 4 touche** (troisième complément, condition 2). Le script écrit son relevé sous un nom numéroté, `releve-mise-en-place-<k>.txt`, où k est le plus petit numéro libre, à partir de 1 ; ses trois fichiers de travail portent le même numéro. Un relevé n'est jamais réécrit ni renommé : **le relevé refusé est gardé tel quel**. Pour rejouer, après que la conductrice a refait la récupération complète, l'opérateur relance la même ligne ; le script prend le numéro suivant. **Règle de lecture, sans autre cas : les scripts des § 1.2 et § 2 lisent le relevé de plus grand numéro, et lui seul ; s'il ne conclut pas « conforme », ils s'arrêtent, même si un relevé de numéro plus petit était conforme.** Les contrôles du relevé sont ceux de la version 3, à la lettre.
- Place : l'arbre de lecture pèse environ 3,5 Go. Moins de 6 Go libres : on ne monte pas, rendu à la conductrice.

### 1.2 Arbre de lecture monté, entrées extraites par chemins nommés

Arbre de travail séparé du dépôt à histoire complète (complément du mandat, point 2 ; montage admis par la session mère). Un clone local ne convient pas : il perdrait les branches de suivi que la garde parcourt.

```bash
bash /home/user/controle-ia-travail/scripts/lecture-bbis-v4/1-2-montage-de-l-arbre.sh
```

- `git checkout <branche> -- <chemin>` pose le fichier sur le disque et dans l'index sans l'afficher. Aucun dossier de la course de confirmation n'est extrait en entier.
- Un arrêt ici : l'opérateur ne retire rien, ne recommence pas, rend la ligne d'arrêt.

### 1.3 Entrées présentes, à l'empreinte des branches et des lignes de registre ; rien de la liste « Jamais »

```bash
bash /home/user/controle-ia-travail/scripts/lecture-bbis-v4/1-3-entrees.sh
```

- Les empreintes sont calculées sur le fichier entier ; aucun contenu n'est décodé ni affiché.
- Pourquoi ce contrôle : un fichier cité absent donnerait un refus de mise en place (code 3) ; un fichier de scores absent serait écrit « non calculable » sans arrêt (quatrième addendum, § 6.5, point 7) ; une empreinte autre donnerait un refus de fond, qui consomme la lecture.

### 1.4 Module, textes scellés, fiches, registre voisin

```bash
bash /home/user/controle-ia-travail/scripts/lecture-bbis-v4/1-4-code-et-textes.sh
```

- Un seul écart d'empreinte du module, d'un texte ou de la fiche, ou une ligne du registre voisin absente ou en double : on ne lance pas (quatrième addendum, § 6.3, tel que CQ-6 le fait lire : « un seul écart : arrêt, rien n'est lancé »).
- Le module ne vérifie pas sa propre empreinte : ce contrôle est celui-ci (quatrième addendum, § 4, point 7).

## 2. Preuve d'antériorité et preuve d'entrée conjointe, relevées à part

Ce que le plan, point 2, les addenda et le feu, § 12, demandent, par les noms et les commits seulement, dans l'arbre où la lecture se jouera, avec git dans l'environnement nettoyé du § 4 :

- (A) histoire complète ; tête de l'arbre qui descend du commit de la course et contient le commit de `main` qui porte les inscriptions ;
- (B) antériorité du scellement sur l'étape B : le premier commit, toutes références, qui ajoute `lecture-t07.json` ou `arret-etape-b.json`, s'il existe, a une date de commit strictement postérieure à celle du commit qui ajoute la ligne `SCELLEMENT-BBIS`. Ce sont les recherches mêmes de la garde (`lecture_v5.py`, l. 854-877), écrites ici en commandes ; le module n'est pas importé ;
- (C) ordre des lignes du registre propre : chaque couple de la chaîne en dates écrites strictement croissantes, hors le seul couple de l'accord de calcul et de la fiche remplaçante, égal à la seconde, que le quatrième addendum (QA-1) fait lire par la preuve d'entrée conjointe ;
- (D) preuve d'entrée conjointe, points (P1) à (P5) de QA-1 (quatrième addendum, § 6.4 : relevée par les seules commandes git en lecture de QA-1, écrite dans la même pièce scellée, avant de lancer le module) ;
- (E) ce que les addenda ajoutent : chaque ligne d'addendum ajoutée par un commit ancêtre de la tête ; les trois premières par un commit ancêtre du commit de la course ; la tête des sorties antérieure à la ligne `SCORES-BBIS`.

Pièce : `registres/t07-etape-b-bis/lecture-v1/preuve-anteriorite-et-entree-conjointe-bbis-v1.txt`, texte, une ligne par constat (`CONFORME` ou `DEFAUT`, avec les identifiants relevés), scellée par son compagnon. Écrite dans l'arbre principal, hors de l'arbre de lecture, pour que celui-ci reste propre.

**Ce qui vaut « on ne lance pas »** : une seule ligne `DEFAUT`. Un défaut de (A) est de mise en place : la conductrice fait corriger l'arbre, puis une pièce `-v2`. Un défaut de (B), (C), (D) ou (E) est un nœud : il annonce un refus de fond de la garde, qui consommerait la lecture ; rien n'est lancé, la conductrice le porte à la mère.

```bash
bash /home/user/controle-ia-travail/scripts/lecture-bbis-v4/2-preuve-anteriorite-et-entree-conjointe.sh
```

- Le bloc entre dans l'arbre de lecture (`cd "$ARBRE"`) : ses lectures de dates et ses comptes portent sur les registres de cet arbre ; la pièce est écrite dans l'arbre principal.
- Les faits attendus sont ceux du quatrième addendum, § 2.0 (F4 à F8), relevés à la source par son rédacteur et par son contre-lecteur.
- Ce relevé ne remplace pas la garde, que le module rejoue entière (quatrième addendum, § 6.4).

## 3. Journal du registre propre

- **Créé par la conductrice** à l'étape 0, avec sa seule ligne d'en-tête, commité sur la branche de travail avant le montage : il est donc dans l'arbre de lecture, suivi par git, sans aucune ligne d'ouverture. C'est l'état que le texte demande (texte scellé, l. 222 ; feu, § 12 ; quatrième addendum, § 6.5, point 8 ; complément, point (O3)).
- **Aucune fonction du code ne le crée à vide.** `registre_bbis_v1.journaliser_ouverture` (l. 113-119) y ajoute une ligne `| OUVERTURE-BBIS | date | lecture B bis (<run>) | empreinte du fichier de lecture |` ; `main` l'appelle une seule fois, après l'écriture du fichier de lecture (`lecture_v5.py`, l. 1708), et jamais sur une issue « non consommée ».
- L'opérateur ne l'écrit pas. Il relève son état au § 4.

## 4. Avant le lancement : arbre propre, environnement, git, versions

La garde d'ouverture n'a pas de commande à part : elle est le premier bloc de `lire` (`lecture_v5.py`, l. 1469-1503). Ce paragraphe écarte seulement ce qui ferait arrêter le programme **avant** sa garde, sans rien écrire : c'est l'état « arrêt avant le seuil », dont la conduite est au § 5.5.

### 4.1 Entrées commitées localement dans l'arbre de lecture

**Qui commite : le lecteur-opérateur, localement, sur la branche `lecture/bbis-arbre-de-lecture-v4` de l'arbre de lecture ; jamais sur `main` ni sur la branche de travail** (complément du mandat, point 2). Il ne pousse pas : la conductrice pousse cette branche sous un nom de la sienne (ci-dessous). Le manifeste de la lecture refuse un arbre non propre (`manifeste.py`, l. 81-83), et ce contrôle vient après le calcul.

```bash
bash /home/user/controle-ia-travail/scripts/lecture-bbis-v4/4-1-commit-local.sh
```

**Fin du premier temps.** L'opérateur rend cette tête à la conductrice et s'arrête.

**Gestes de la conductrice entre les deux temps, avant tout lancement.** D'abord, **décision d'organisation de la conductrice** (constat m6 de la contre-lecture de la version 2) : elle commite et pousse sur la branche de travail la pièce de la preuve d'antériorité et de la preuve d'entrée conjointe, avec son compagnon, pour que la preuve soit inscrite à part avant la lecture (feu, § 12). Ce commit ne touche pas l'arbre de lecture, dont le parent reste `TETE_TRAVAIL`. Ensuite (second complément, point 7) : elle pousse la branche locale de l'arbre de lecture sous un nom de sa branche, jamais `main`, pour que le manifeste de la lecture cite un commit joignable sur le distant :

```bash
bash /home/user/controle-ia-travail/scripts/lecture-bbis-v4/4-1-conductrice-preuve-et-branche.sh
```

- Cette branche porte les 32 fichiers d'entrée, déjà présents sur le distant sous leurs branches d'origine ; elle n'est jamais fusionnée dans la branche de travail ni dans `main`.
- Le § 4.2 vérifie, avant le lancement, que la tête de cette branche sur le distant est la tête de l'arbre de lecture ; sinon on ne lance pas.
- Une relance n'est pas jouée sur cette version (§ 5.3) ; la version écrite pour elle dira comment les commits locaux de plus sont poussés.

### Décision sur le risque de redémarrage : donnée par la conductrice au lancement du second temps

### 4.2 Relevé d'avant lancement

`N` est le numéro du lancement (1). Le nom du run de lecture est fixé ici, une fois : `<AAAAMMJJ-HHMMSS>-bbis-t07-lecture-v1` (forme exigée par `manifeste.py`, l. 26).

```bash
bash /home/user/controle-ia-travail/scripts/lecture-bbis-v4/4-2-releve-avant-lancement.sh 1
```

- **Contrôles d'après le seuil ramenés avant le lancement** (second complément, point 1). L'écriture du résultat crée un manifeste décisif après tout le calcul (`lecture_v5.ecrire_lecture`, l. 1635-1648 ; `manifeste.creer_manifeste`, l. 68-116) : un échec y consommerait la lecture. Par lecture de ces deux fonctions, ce qu'elles contrôlent sur des fichiers hors données, et où la commande le fait avant :
  - la forme du nom du run (`manifeste.py`, l. 26 et 74) et l'absence de son dossier (l. 76-77) : ici ;
  - l'arbre propre (l. 78-83) : ici, par git dans l'environnement nettoyé ;
  - **le préenregistrement scellé** (l. 85-96, `prereg.exiger_prereg_scelle`) : compagnon égal, huit sections exigées présentes et non vides, aucun marqueur « À REMPLIR », aucun marqueur de gabarit, deux empreintes par entrée de la section « Contre-lecture » (`prereg.py`, l. 37-76). La commande appelle **cette fonction du dépôt**, sur le texte scellé de l'arbre de lecture et sur lui seul. Elle n'est ni le module de lecture ni sa garde, n'ouvre aucune donnée et ne lance aucune commande git ;
  - l'entropie des graines (`manifeste.graines`, l. 37-49) et la fiche de code que `main` relit pour la trouver (`lecture_v5.py`, l. 1693-1695) : la commande appelle `registre_bbis_v1.lire_fiche_code` et `commun_v1.exiger_entropie` sur la fiche de code, qui n'est pas un fichier de résultat ; ce ne sont ni le module de lecture ni sa garde ;
  - l'écriture du dossier du run (l. 110-114) et du fichier de lecture (`manifeste.ecrire_resultat`, l. 128-139) : dossiers `runs` et `diag` ouverts à l'écriture, aucun fichier à ce nom ;
  - les versions des bibliothèques (`manifeste.versions`, l. 58-65) sont seulement consignées : elles ne peuvent pas refuser.
  Le module gelé de la partition des plis, que `lire` compare après le seuil (`adversaires_texte_v1.exiger_module_gele`), est déjà comparé au § 1.4. Ce qui reste après le seuil et ne peut pas être contrôlé avant sans ouvrir une donnée : les contrôles du contenu des entrées elles-mêmes (manifeste de la course de confirmation, audit des fuites, champ du contrôle carte-processeur, effectifs).
- Un échec d'un de ces contrôles vaut « on ne lance pas ».
- **S'il reste une variable dont le nom commence par `GIT_`, on ne lance pas** : le module s'arrêterait en première instruction (`lecture_v5.py`, l. 1674-1678), sans rien écrire : état « arrêt avant le seuil » (§ 5.5). L'opérateur n'ajoute pas un `-u` de son chef : il rend les noms à la conductrice.
- Si git ne répond pas dans l'environnement nettoyé : on ne lance pas (note n10 de la contre-lecture du code).
- **Si l'utilitaire de détachement manque, on ne lance pas** : l'opérateur ne le remplace par rien et rend le relevé. Relevé par le préparateur sur cette machine, par `command -v` : il est présent (`/usr/bin/setsid`, option `-f`), ainsi que les deux autres.
- Les valeurs des variables ne sont jamais imprimées : seuls leurs noms le sont.
- Les versions figées et les fils de calcul à 1 sont exigés par le contrôle d'égalité de la base « mots et coût » (tolérance 10⁻¹², `adversaires_texte_v1.py`, l. 68 ; fils : `lien_mots_et_cout_v1.py`, l. 123-129, arrêt sinon).

## 5. Lecture

### 5.1 Ligne de lancement

```bash
bash /home/user/controle-ia-travail/scripts/lecture-bbis-v4/5-1-lancement.sh 1
```

- **Module** : `controle_ia.t07bbis.lecture_v5`. **Arguments** : ceux de `main` (`lecture_v5.py`, l. 1682-1685), quatre, tous exigés ; `--adaptateur-mc` n'est pas passé : la ligne `CODE-MOTS-ET-COUT-T06` est inscrite avant l'échéance du 18 novembre à 12:00 UTC, le module charge de lui-même le code de la pièce (`adaptateur_retenu`, l. 1654-1665).
- **Environnement du module** : les onze variables retirées par `env -u`, `BBIS_INSTANCE` retirée, fils de calcul à 1, `PYTHONPATH` sur le code de l'arbre de lecture. La ligne exacte, valeurs développées, est celle du fichier `lancement-<N>.sh`, que l'opérateur copie sous `registres/t07-etape-b-bis/lecture-v1/lancement-lecture-bbis-<N>-v1.sh` et scelle au § 5.2. L'enveloppe (`bash`) garde l'environnement de la session ; seul le module tourne dans l'environnement nettoyé.
- **Lancement détaché de l'outil** (second complément, point 2) : l'enveloppe part dans une nouvelle session de processus (`setsid -f`), entrées et sorties coupées du terminal ; l'appel d'outil rend la main aussitôt. Le module n'est ni en arrière-plan d'un appel d'outil, ni sous un délai d'outil. L'opérateur ne lance pas ce bloc avec l'option d'arrière-plan de son outil.
- **Identifiant du processus** : celui du module de lecture, écrit par l'enveloppe dans `lancement-<N>.pid`. Le code de sortie est écrit dans `lancement-<N>.code` quand le module finit.
- **Sortie entière** (sortie et erreurs) dans `sortie-lancement-<N>.txt`. Les lignes `BBIS LECTURE ENTREES OUVERTES` et `BBIS LECTURE NON CONSOMMEE` ne vivent que là.
- **Durée** : le code ne la laisse pas estimer, et le module n'a jamais tourné sur les fichiers réels.
- **L'opérateur ne touche à rien dans l'arbre de lecture pendant la marche** : un fichier de plus rendrait l'arbre non propre au moment du manifeste, après le seuil.
- **Sorties attendues, dans l'arbre de lecture** : `runs/<run>/manifeste.json` et `diag/<run>/lecture-bbis.json`, chacun avec son compagnon, écrits et scellés par le module lui-même (`manifeste.creer_manifeste`, `manifeste.ecrire_resultat`) avant toute lecture humaine ; sur une issue « non consommée », en plus, `diag/<run>/preuve-aucune-ouverture-bbis.json` et son compagnon.

### 5.1 bis Attente, sans jamais arrêter le processus

L'opérateur relève l'état du processus par son identifiant, par des appels courts et espacés (toutes les dix minutes environ, sans attente longue dans un appel). Il n'y a aucun délai de garde.

```bash
bash /home/user/controle-ia-travail/scripts/lecture-bbis-v4/5-1-bis-attente.sh 1
```

- « vivant » : l'opérateur attend, quel que soit le temps écoulé. **Une lecture lente mais vivante n'est jamais arrêtée**, ni par lui, ni sur aucun motif ; s'il doute, il écrit à la conductrice et continue d'attendre.
- « fini » : § 5.2.
- « processus absent, code de sortie non écrit » deux relevés de suite, à une minute d'écart : le processus a disparu sans finir (machine redémarrée, par exemple). § 5.2, qui le traite comme un arrêt, avant ou après le seuil selon la sortie gardée.

### 5.2 Fin du lancement : sortie gardée et scellée

À jouer quand `lancement-<N>.code` existe, ou quand le processus est absent deux relevés de suite.

```bash
bash /home/user/controle-ia-travail/scripts/lecture-bbis-v4/5-2-releve-apres-lancement.sh 1
```

- **Ce relevé est ce que l'opérateur rend à la conductrice**, avec son chemin et son empreinte. Il ne porte que : le code de sortie, l'état, des noms, des empreintes.
- **État « écrit »** (second complément, point 5) : le relevé dit « écrit », le chemin, l'empreinte, le code de sortie, **et rien qui distingue une lecture faite d'une issue « non lue » de fond** : ni le compte de la ligne du seuil, ni le motif d'un refus, ni la taille du fichier, ni une clé du fichier. L'opérateur n'ajoute rien de tel dans son message.
- **Deux exceptions nécessaires**, parce qu'elles commandent une suite et ne portent aucune issue de mesure : l'état « non consommée » (code 3 et ligne `BBIS LECTURE NON CONSOMMEE`) et l'état « arrêt avant le seuil » sont rendus comme tels.
- **Arrêt avant le seuil** (second complément, point 3) : le relevé porte le code de sortie, les trois comptes de lignes, et les quarante dernières lignes de la sortie gardée, **si et seulement si** le compte de la ligne du seuil est zéro. Une trace d'erreur du programme ou un refus de ses options, qui n'impriment pas la ligne `BBIS LECTURE ARRET`, y sont donc compris. Si le compte du seuil n'est pas zéro, aucune ligne de la sortie n'est extraite.
- L'opérateur n'affiche jamais la sortie gardée elle-même. La sortie de **chaque** lancement est gardée et scellée, quel que soit le code (complément au quatrième addendum, « La suite », point 3 ; condition de la fiche de rattachement). La conductrice la commite sans l'ouvrir.

#### Constat de forme, pour le juge seul

À jouer dans les états « écrit » et « non consommée ». La pièce est écrite et scellée **sans être affichée** ; l'opérateur n'en rend que le chemin et l'empreinte ; **la conductrice ne l'ouvre pas** ; elle est donnée au juge. Elle ne porte aucune valeur de mesure : des présences de clés, les comptes de lignes de la sortie gardée, le motif d'un refus de la garde (noms de lignes, de fichiers et de commits), la liste des fichiers ouverts par la chaîne.

```bash
bash /home/user/controle-ia-travail/scripts/lecture-bbis-v4/5-2-constat-de-forme-pour-le-juge.sh 1
```

- Exception : dans l'état « non consommée », la conductrice et la mère ont besoin du motif du refus pour décider de la relance. L'opérateur le leur rend par une seule ligne, extraite de la pièce de preuve écrite par le module et non de ce constat, par le script `5-2-motif-non-consommee.sh` :

```bash
bash /home/user/controle-ia-travail/scripts/lecture-bbis-v4/5-2-motif-non-consommee.sh 1
```

  Le script porte la ligne de la version 3 (`grep -o` du champ « motif » de la pièce de preuve) et refuse de partir hors de l'état « non consommée ». Ce motif ne peut porter aucune mesure : rien n'a été ouvert.

### 5.3 Les suites, par code de sortie et par lignes imprimées

L'opérateur agit d'après la ligne `ETAT` du relevé du § 5.2, et d'elle seule.

| état du relevé | ce que c'est | ce que fait l'opérateur | ce qu'il rend à la conductrice |
|---|---|---|---|
| **écrit** (code 0, fichier de lecture écrit) | la lecture a eu lieu au sens du texte : lecture faite, ou issue « non lue » de fond écrite par le module avec sa phrase gelée ; dans les deux cas **la lecture est consommée** et le module a écrit sa ligne au journal | constat de forme pour le juge ; puis § 5.4, **le même geste dans tous les cas** : sorties portées, ligne `LECTURE-BBIS`, journal | « écrit », chemins, empreintes, code de sortie, la ligne ajoutée au registre propre ; rien d'autre |
| **non consommée** (code 3, ligne `BBIS LECTURE NON CONSOMMEE`, seuil à zéro) | issue « non lue » née d'un pur défaut de mise en place ; le module a écrit la pièce de preuve ; rien n'a été ouvert | constat de forme pour le juge ; **rien n'est inscrit ; arrêt** | l'état, les chemins et empreintes du relevé, le motif du refus |
| **arrêt avant le seuil** (ni code 0 ni code 3 ; seuil à zéro) | le programme s'est arrêté sans rien ouvrir ni rien écrire | **arrêt ; aucune relance** ; § 5.5 | le relevé, qui porte l'extrait de la sortie |
| **arrêt après le seuil** (ni code 0 ni code 3 ; seuil imprimé) | arrêt après la première ouverture d'une entrée | **lecture consommée ; arrêt ; nœud** | le relevé seul ; aucune ligne de la sortie |
| **non prévu** | code 0 ou 3 sans les fichiers ou les lignes attendus | arrêt ; nœud | le relevé seul |
| **sortie non gardée** (ni code 0 ni code 3 ; sortie du lancement absente ou non scellée) | rien ne prouve que le seuil n'a pas été franchi | **lecture consommée ; arrêt ; nœud** (complément au quatrième addendum, « La suite », point 3) | le relevé seul ; aucune ligne de la sortie |

- **État « non consommée » — ce que la conductrice et la mère décident ensuite**, selon « La suite » du complément au quatrième addendum : panne corrigée sur l'arbre de lecture seulement ; déclaration `registres/t07-etape-b-bis/lecture-v1/declaration-panne-mise-en-place-bbis-<n>-v1.md`, scellée, qui cite tous les lancements antérieurs et leurs sorties gardées ; ligne `PANNE-MISE-EN-PLACE-BBIS-<n>` inscrite par la mère au registre voisin avant la relance ; correction, fichier de lecture gardé, pièce de preuve, manifeste du run refusé et déclaration commités sur la branche de l'arbre de lecture, poussée de nouveau par la conductrice (§ 4.1) ; arbre vérifié propre ; relance sous le nom du run refusé suivi de `-relance<n>`. **Aucune relance n'est jouée sur cette version de la commande : une relance demande une version de la commande écrite et contre-lue pour elle** (décision d'organisation de la conductrice ; note n3 de la contre-lecture de la version 2 : après les commits de la correction et de la déclaration, les contrôles du § 4.2 sur le parent de la tête et sur les 32 entrées rendraient « on ne lance pas »). **L'opérateur ne fait rien de cela sans un mot de la conductrice** ; il ne corrige pas de son chef.
- **État « arrêt après le seuil »** : aucune relance sous aucun texte ; nœud de Lazar (complément au quatrième addendum, « Tout arrêt après une ouverture consomme la lecture »). Un processus disparu après le seuil en relève aussi.

### 5.4 État « écrit » : sorties portées, ligne `LECTURE-BBIS`, journal

Le module a déjà scellé ses sorties et écrit sa ligne au journal de l'arbre de lecture. L'opérateur porte les sorties, à l'octet, de l'arbre de lecture à l'arbre principal, puis ajoute la ligne au registre propre de l'arbre principal par la fonction du code (`registre_bbis_v2.ajouter_ligne_propre`, l. 95-120 : ligne ajoutée, jamais réécrite ; refus si la clé est déjà là, si le registre n'est pas le registre propre, ou si une clé de l'étape B bis est au registre partagé).

**Le geste est le même que le fichier porte une lecture faite ou une issue « non lue » de fond** : l'opérateur ne le sait pas et n'a pas à le savoir. Fondement : le plan, point 10 (f), fait suivre tout résultat écrit de la ligne `LECTURE-BBIS` ; le complément au quatrième addendum, § 3, la veut « inscrite une seule fois, pour le fichier de la lecture qui compte », et une lecture consommée est celle qui compte ; le second complément du mandat, point 5, veut que rien ne distingue les deux cas pour la conductrice.

```bash
bash /home/user/controle-ia-travail/scripts/lecture-bbis-v4/5-4-sorties-portees-et-ligne-de-lecture.sh 1
```

- **Format de la ligne** : celui du registre propre, `| LECTURE-BBIS | AAAA-MM-JJTHH:MM:SSZ | diag/<run>/lecture-bbis.json | sha256 |` (`t07/registre_v1.ecrire_ligne`, l. 318-322).
- Rien n'est écrit dans `registres/scellements-v1.md`.
- L'opérateur rend : « écrit » ; la ligne ajoutée (clé, heure, chemin, empreinte) ; la dernière ligne du journal (elle ne porte qu'une date, le nom du run et une empreinte) ; les chemins et empreintes des sorties et du constat de forme pour le juge ; l'identifiant du processus, le code de sortie (les heures de début et de fin sont dans le constat de forme, pour le juge seul). **Aucun chiffre de mesure, aucune issue, rien du constat de forme.** La liste des fichiers de résultat ouverts par la chaîne est dans le constat de forme, pour le juge ; à la conductrice, l'opérateur rend seulement : « à l'œil : aucun ; par la chaîne : liste dans le constat de forme ».
- L'arbre de lecture et sa branche locale ne sont pas retirés par l'opérateur.

### 5.5 État « arrêt avant le seuil » : conduite, et preuve après coup sur ordre écrit seulement

- **Statut de cette voie.** Le complément scellé au quatrième addendum (§ 7, point 7) la dit : « La voie de l'arrêt avant le seuil n'est pas employée avant son mot » — le mot de Lazar. **Toute relance par cette voie attend donc le mot de Lazar**, et non la seule confirmation de la session mère : l'application par anticipation que la mère avait annoncée ne remplace pas un texte scellé (message de la mère du 2026-11-18 à 23:36:15Z ; R-3530). La forme de la preuve après coup — comparaison des fichiers au commit épinglé des sorties `7322049dbbc10975ec1fa7dd54c10c8bc1ec4cf9`, après vérification de `sondes-bbis.json` contre la ligne `SCORES-BBIS`, sans décoder ce fichier — reste la forme recommandée et portée à Lazar ; **il ne l'a pas encore accordée**.
- **Conduite.** Sur un arrêt avant le seuil, l'opérateur **ne relance pas** et ne corrige rien. Il rend le relevé du § 5.2 et s'arrête. Il joue le programme de la preuve après coup **seulement sur ordre écrit de la conductrice** : le jouer n'emploie pas la voie, il relève un état ; relancer l'emploierait (classement de la contre-lecture de la version 2, point (g), N1 bis). Il rend la pièce (chemin, empreinte, la ligne imprimée par le programme, son code de sortie) et s'arrête de nouveau. La conductrice rend la pièce à la mère, qui la porte à Lazar. Aucune relance n'est jouée sur cette version de la commande (§ 5.3).
- **La ligne, à ne jouer que sur cet ordre écrit** (`scripts/preuve_aucune_ouverture_apres_coup_bbis_v1.py`, `b7bc7e5d87ba45a696ded6790e1354fd065467f838ef565efba2ff0746b05675`, cité par la fiche de rattachement ; usage : son en-tête, l. 35-37). Elle donne **toutes** les sorties gardées des lancements antérieurs, une paire chemin et empreinte par lancement :

```bash
bash /home/user/controle-ia-travail/scripts/lecture-bbis-v4/5-5-preuve-apres-coup-sur-ordre-ecrit.sh 1
```

- Le programme écrit et scelle lui-même sa pièce, dans l'arbre de lecture : `registres/t07-etape-b-bis/lecture-v1/preuve-aucune-ouverture-apres-coup-bbis-<N>-v1.json`. Il n'imprime que des chemins, des empreintes et des états ; il refuse de partir sous une variable `GIT_` (d'où l'environnement nettoyé).
- Code 0 : pièce conforme ; code 1 : pièce écrite, non conforme (« lecture consommée » ou « nœud », selon son classement) ; code 2 : rien d'écrit. Dans les trois cas l'opérateur rend et s'arrête ; il ne rejoue pas le programme.

## 6. Ce que la conductrice commite

Sur la branche de travail `claude/lecture-verdict-etape-b-bis-v1`. Le texte ne nomme aucune branche de données pour les sorties de la lecture (« Données gardées », l. 214 : « Lecture : `diag/<run-bbis-lecture>/lecture-bbis.json` […] chacun avec son compagnon ») : elles vont sur la branche de travail ; la mère porte les lignes de registre sur `main` par chemin et empreinte.

Avant le lancement de l'opérateur (étape 0) :
- la fusion du commit de `main` `4aefb5b1…` et `registres/t07-etape-b-bis-v1.md.ouvertures.md` (ligne d'en-tête) : déjà commités et poussés (tête `fd110046…`) ;
- `registres/t07-etape-b-bis/lecture-v1/commande-lecture-bbis-v4.md`, ses différences avec la version 3, le dossier `scripts/lecture-bbis-v4/` (seize fichiers et leurs compagnons), le troisième complément du mandat du préparateur, leurs compagnons (les versions 1 à 3 et leurs pièces restent, R12).

Entre les deux temps de l'opérateur (§ 4.1) : `registres/t07-etape-b-bis/lecture-v1/preuve-anteriorite-et-entree-conjointe-bbis-v1.txt` et son compagnon, commités et poussés sur la branche de travail (preuve « inscrite à part », avant la lecture : feu, § 12) ; puis la poussée de la branche de l'arbre de lecture sous le nom `claude/lecture-verdict-etape-b-bis-v1-arbre-de-lecture`, qui n'est pas un commit de la branche de travail.

Après, selon l'état (tous sous `registres/t07-etape-b-bis/lecture-v1/`, chacun avec son compagnon) :
- `releve-avant-lancement-lecture-bbis-<N>-v1.txt`, `lancement-lecture-bbis-<N>-v1.sh`, `sortie-lancement-lecture-bbis-<N>-v1.txt`, `releve-apres-lancement-lecture-bbis-<N>-v1.txt` ; la sortie gardée est commitée **sans être ouverte** ;
- `constat-forme-pour-le-juge-lecture-bbis-<N>-v1.txt`, commité **sans être ouvert**, donné au juge par son chemin et son empreinte ;
- état « écrit » : `runs/<run>/manifeste.json`, `diag/<run>/lecture-bbis.json`, leurs compagnons, commités sans être ouverts ; le registre propre (ligne `LECTURE-BBIS`) ; le journal (seconde ligne) ;
- état « non consommée » : les fichiers écrits par le module restent dans l'arbre de lecture, cités par chemin et empreinte dans le relevé, et sont commités sur la branche de l'arbre de lecture avant une relance (§ 5.3) ;
- état « arrêt avant le seuil », si la preuve après coup a été ordonnée : sa pièce reste dans l'arbre de lecture, de même ;
- les relevés de mise en place restent dans le dossier temporaire ; la conductrice peut les faire porter et sceller si elle les veut au dépôt.

Jamais commités sur la branche de travail : les 32 fichiers d'entrée de l'arbre de lecture. La branche locale `lecture/bbis-arbre-de-lecture-v4` n'y est jamais fusionnée, ni celle de la version 3, restée en place.

## 7. Points ouverts et écarts

### Ce que deviennent les onze points du premier rendu

1. **La garde refusait sur l'ordre des lignes** — tranché par Lazar (`GO-2026-11-18-56` (1)) : quatrième addendum, QA-1 ; exception fermée dans `lecture_v5.exiger_ordre_propre`. Réserve R-ORDRE au verdict.
2. **Histoire du registre propre non linéaire** — déclarée : quatrième addendum, QA-3 et § 2.0 (F4 à F7) ; entre dans R-ORDRE. Le relevé (C) du § 2 l'écrit.
3. **Garde non séparable de la lecture** — tranché : aucun mode « garde seule » (complément, § 3) ; un fichier est écrit sur tout refus (quatrième addendum, § 6.5, point 3) ; les suites sont celles de `GO-2026-11-18-60` et `-64` (§ 5.3, § 5.5). Voir N2 ci-dessous.
4. **Arbre propre exigé par le manifeste, après le calcul** — tranché : geste de la commande (quatrième addendum, § 6.5, point 4) ; l'opérateur commite localement (complément du mandat) ; la conductrice pousse la branche de l'arbre de lecture avant le lancement (second complément, point 7 ; § 4.1). Voir N3.
5. **Arbre de travail séparé plutôt que clone local** — tranché : complément du mandat, point 2 ; montage admis par la session mère.
6. **Entrées sur trois branches** — tenu par les § 1.2 et 1.3. La tête de la branche de la pièce « mots et coût » n'est nommée par aucun texte : le fichier est ancré par l'empreinte de sa ligne de registre.
7. **Fichier de scores absent rendu « non calculable » sans arrêt** — tranché par le texte (quatrième addendum, § 6.5, point 7) ; le § 1.3 contrôle chaque entrée avant le lancement.
8. **Journal** — tranché : quatrième addendum, § 6.5, point 8 ; créé à l'étape 0, en-tête seule.
9. **Environnement** — tenu : versions figées relevées, fils de calcul à 1 (§ 4.2, § 5.1). **Reste ouvert** : N5.
10. **`main` jamais joué en réel ; durée inconnue** — en partie levé : les essais neufs jouent le vrai `main` sur jouets (contre-lecture du code, note n9). Il reste que le module, sa garde et cette commande n'ont jamais tourné sur les fichiers réels (réserve de la fiche de rattachement) ; la durée reste inconnue.
11. **Branche des sorties de la lecture** — inchangé : le texte n'en nomme aucune ; branche de travail (§ 6).

### Points ouverts de cette commande

- **N1 — Des arrêts avant le seuil restent possibles malgré le § 4 ; réduit.** La table des modules gelés du code de la pièce « mots et coût » est désormais comparée avant le lancement, par empreinte (§ 1.4 ; constat m4 de la contre-lecture de la version 2). Restent, selon l'inventaire de ce rapport (note n8) : une erreur d'importation ou d'exécution du code de la pièce, le disque plein, un processus disparu ; aucun ne peut être exclu sans jouer le code. Un tel arrêt mène au § 5.5 : l'opérateur ne relance pas ; toute relance par cette voie attend le mot de Lazar. Classé par le rapport : question d'organisation.
- **N1 bis — Toute relance par la voie de l'arrêt avant le seuil attend le mot de Lazar** (complément au quatrième addendum, § 7, point 7 ; message de la mère du 2026-11-18 à 23:36:15Z, R-3530 ; contre-lecture de la version 2, point (g) : « nœud de Lazar si la voie doit servir à une relance »). La forme de la preuve après coup est recommandée et portée à Lazar, non encore accordée. Non bloquant pour le premier lancement.
- **N2 — Ligne `LECTURE-BBIS` inscrite dans tout état « écrit », issue « non lue » de fond comprise** (§ 5.4) : **tranché par le texte, dans le sens de la commande** (contre-lecture de la version 2, point (g) et note n1 : plan, point 10 (f), et point 2 ; quatrième addendum, § 7, point 4 ; complément au quatrième addendum, « La suite », point 1, et § 3). Ni question d'organisation, ni nœud.
- **N3 — Commit des entrées cité par le manifeste.** Tranché par le second complément, point 7 : la conductrice pousse la branche de l'arbre de lecture sous `claude/lecture-verdict-etape-b-bis-v1-arbre-de-lecture` avant le lancement ; le § 4.2 vérifie la tête du distant. Il reste que cette branche du distant porte une seconde fois, sous un autre nom, les 32 fichiers d'entrée, dont les fichiers fermés de scores.
- **N4 — Le mandat du lecteur-opérateur et cette commande ne s'accordent pas en plusieurs endroits** (à dire aussi dans son message de lancement : il ne fait pas la récupération complète du distant, que la conductrice fait à l'étape 0 ; il attend la fin du lancement sans attente fixe dans un appel de terminal, que son outil refuse — note n6 de la contre-lecture de la version 2), que le complément du mandat tranche : il « ne commite pas » (ici : un commit local dans l'arbre de lecture) ; il « crée » le journal (ici : la conductrice, à l'étape 0, lui en relève l'état) ; il joue « la garde » comme une étape (ici : elle est dans le module) ; les règles communes lui interdisent tout appel à un service extérieur (ici : la récupération des branches nommées et la lecture des têtes du distant, en lecture seule, § 1.1 et § 4.2, permises par le second complément, point 4, que la conductrice écrit dans son mandat) ; il est lancé en deux temps (§ 0). À dire dans son message de lancement.
- **N5 — Versions du run de la pièce « mots et coût » non comparées.** Son manifeste n'est pas dans la liste blanche du plan, point 1. Si les versions différaient, le contrôle d'égalité rendrait la base « non calculable » avec un nœud, sans arrêt du reste (liste d'arrêt, l. 193).
- **N6 — Verdict de l'épreuve du signal planté que cite son fichier d'issue, non contrôlé avant le lancement** : **tranché par le texte** (contre-lecture de la version 2, point (g)) : son nom ne se connaît qu'en ouvrant le fichier d'issue, que la chaîne seule ouvre ; un fichier absent ou illisible donne une issue « non lue » de fond (complément au quatrième addendum, « La règle ») ; l'arbre de lecture, propre, porte les fichiers suivis. Risque accepté par le texte ; aucune action.
- **N7 — Retrait des variables `GIT_`.** Les onze noms sont ceux que la contre-lecture du code relève sur cette machine ; je n'en ai lu aucune valeur. Si git, privé d'elles, refusait l'arbre de lecture, le § 4.2 le dit et on ne lance pas ; aucun texte ne dit quoi faire ensuite.
- **N11 — Forme en scripts.** Seize fichiers sous `scripts/lecture-bbis-v4/`, écrits par programme à partir des blocs de la version 3 ; aucun n'a été joué. Si l'outil de terminal refusait encore une ligne `bash <script>`, l'opérateur s'arrête et rend le texte du refus : il ne recopie pas le script.
- **N12 — Ce que la version 3 a laissé reste en place** : son dossier de travail, son arbre de lecture (3,4 Go) et sa branche locale. Aucun script ne les supprime ; leur retrait reste à un humain.
- **N13 — Le montage n'est pas rejouable** : si le § 1.2 s'arrêtait en cours (un redémarrage, par exemple), l'arbre `arbre-de-lecture-v4` existerait à moitié et sa garde `neuf` refuserait de le remonter. Aucun script ne le retire. Il faudrait un nom d'arbre neuf, donc une version de la commande, ou le geste d'un humain.
- **N14 — Deux ajouts au registre propre et à son journal, au § 5.4**, sont des lignes ajoutées en fin de fichier, voulues par le texte (« lignes ajoutées, jamais réécrites ») : ce ne sont pas des réécritures ; je les signale parce que la condition 3 du troisième complément parle de tout fichier existant.
- **N8 — Scripts écrits par simple lecture.** Aucun n'a été joué ; seule leur syntaxe est contrôlée. Une faute d'un bloc d'avant lancement arrête sans rien consommer. Le lancement détaché (`setsid -f`) n'a jamais été éprouvé avec ce module : si l'identifiant du processus n'est pas écrit à deux relevés de suite (§ 5.1 bis), l'opérateur ne relance pas et rend.
- **N9 — retiré.** Les lignes que le verdict cite (cinq lignes d'addenda, ligne de rattachement, réserve R-ORDRE) sont portées par le complément du mandat du juge, écrit par la conductrice.
- **N10 — Fusion de `main`.** Elle apporte dans l'arbre de lecture des fichiers d'autres chaînes que la lecture n'ouvre pas ; relevé par les noms : elle ne change ni le registre propre, ni le registre partagé pour ses cinq lignes lues, ni le module, ni la fiche de rattachement, ni un fichier sous `src/` déjà présent, et n'ajoute à `requirements-cpu.txt` que des lignes. Le § 1.4 le revérifie après coup par les empreintes.
