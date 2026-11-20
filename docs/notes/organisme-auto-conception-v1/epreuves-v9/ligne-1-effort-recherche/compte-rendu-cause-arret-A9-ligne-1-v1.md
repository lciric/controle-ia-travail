# Compte rendu de cause — arrêt de la ligne 1 à l'étalonnage (garde A9) — v1

Pièce de travail (classe C). Lecteur de cause neuf : je n'ai écrit ni le préenregistrement de la ligne 1, ni son addendum, ni son erratum, ni le code du banc A. Mandat : `docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-1-effort-recherche/mandat-lecteur-cause-arret-A9-ligne-1-v1.md` (sha256 `372bcec5e64121a80ffc86352b8973a82bb44018cf274b4d0fbd74607f2a81ae`, vérifiée). Lancement permis par GO-2026-11-20-01 et la lecture R-4024 de la session mère (d'après le mot qui m'a lancé). Écrit le 2026-11-20 vers 00:40Z.

Rien n'a été rejoué, lancé ni réglé. Aucun journal de course d'étalonnage, aucune sortie de course n'a été ouvert. Aucun réglage n'est proposé.

## Verdict en bref

- **Déclencheur qui a tiré : la porte de prise (seconde branche de A9).** La borne basse de M1-nul du témoin T0, classe « beaucoup », vaut 0,0220, pour un seuil « strictement au-dessus de 0,05 ». La valeur (0,0292) et la borne haute (0,0366) sont aussi sous 0,05 : il ne s'agit pas d'un manque de précision, T0 *tient* le niveau sur ce banc.
- La première branche de A9 (force non atteinte en 10 pas) n'a **pas** tiré : les quatre forces sont atteintes en 3 à 8 pas.
- **Une seconde porte est aussi manquée, cachée par l'ordre du code : la porte des cartes jugées par appel (garde A15)**, écart de 0,1024 pour un seuil de 0,1. `exiger_portes` lève A9 avant de regarder A15. L'addendum scellé (§ 3) dit que sa conduite pour A15 vaut « dès que la sortie de l'étalonnage dit la porte A15 manquée, quelle que soit la garde levée en premier (A9 est levée avant A15) ». **La conduite du § 3 de l'addendum s'applique donc aussi.**
- Cause la mieux appuyée pour la prise : les lois fausses plantées sont très peu promues par le juge, chaque carte seule (au plus 1 % au seuil 1/0,05 sur la grille gelée), et ces rares promotions sont diluées dans les promotions des quatre lignées vraies, sur une quantité qui est la moyenne par course d'un rapport. Rien dans les pièces ne désigne une faute du code.

## 1. Pièces lues et empreintes vérifiées

Toutes les empreintes ont été recalculées par `sha256sum` et sont égales aux valeurs attendues.

| pièce | sha256 | lecture |
|---|---|---|
| mandat | `372bcec5e64121a80ffc86352b8973a82bb44018cf274b4d0fbd74607f2a81ae` | en entier |
| manifeste du versement `journaux-course-ligne1-v2-arret-A9-20261120/manifeste-depot-ligne1-v2.json` | `acc4192e65154ceb1dea72289abb4b30a1e75eaef5cde56c52933df363559dd4` (égale à son compagnon) | noms et empreintes des membres |
| morceau `journaux-banc-a-ligne1-v2-partie-001.tar` | `58dd2f9ce1592bb519b3253d0e1ef0919ee633fe2e53d8c622fb6bde9a03c48f` (égale au compagnon) | liste des membres ; trois membres extraits par leur nom |
| morceau `journaux-banc-a-ligne1-v2-partie-000.tar` | `5518d104f6027e0ddaba24ca914b3473f7ba9201dfbb75a2c662fb73d80781d0` (égale au compagnon) | liste des membres seulement (rien d'extrait) |
| `etalonnage/sortie-etalonnage-ligne1-v2.json` (extrait) | `99a9e765603fad5784ffda74af9d281d0726fd51e72a254f468c46592222ce76` | en entier, hors liste des empreintes des fichiers de course |
| `etalonnage/etape-forces.json` (extrait) | `f04be166b56f41816e63a8bcd0fccd184d27c99d6aba22ff2dcb8470a8eb07dd` | en entier |
| `etalonnage/etape-grille.json` (extrait) | `0e0367182b4ba8eb8ce29bff60dc8b8d7f306fd459b522b24eac2b6381238bc2` | en entier |
| préenregistrement scellé v5 (`git show origin/main:…`) | `523adfd75333d7f2e99a6fe4f868c7dc6982a67e51953734f40258d7a40fc0b9` | § 0, Hypothèse, Prédictions, Métrique, Seuil, Plan d'analyse (dont « Étalonnage » et « Audit du générateur »), table de lecture, « Liste d'arrêt », Réserves 1 à 9, différentiel v1 → v2 (une ligne) |
| addendum 1 scellé v4 (`main`) | `c29628a0dd209133545985cc334274462257314560c62c04259c5b31b1686e67` | en-tête, § 1 à § 9 |
| erratum 1 v3 scellé (`main`) | `ab98317d5e809d53eb5af88f17dd1f4e3683a16a1a21c699c9823538f84f1bd4` | en entier |
| `code/etalonnage_ligne1_v2.py` | `87c74c537a0750f81eacf54250615811c79450efa247448ac6f84f556c94b185` | en entier |
| `code/banc_ligne1_v1.py` | `ccc97ea2d0cee6d0e9ef08cb0e28699aab11fb424fef3f4f22676a30bbd549ba` | `charger_organisme`, `commit_organisme`, `Graines`, `parametres`, `juger`, `juger_banc`, monde planté, `variantes`, texte des cartes, étages amont, `jouer_course_pleine`, règles de promotion, `jouer_bras` |
| `code/configuration_ligne1_v2.json` | `81f58ce5ca0a492ef231fa175303a21dfb21383a096fa71911b917923cc34f15` | en entier |

Les empreintes du code et de la configuration sont aussi celles que la sortie scellée porte (`code.fichiers`, `configuration_sha256`) ; la sortie dit `arbre_propre: true`, commit `7b16f957a34e52e6eda59603611db926dbdd3195`.

**Deux pièces nommées par le mandat sont absentes** : le journal du lanceur et `journal-etalonner.log`. Elles ne sont ni dans le manifeste du versement, ni dans les deux morceaux (liste complète des membres relue : hors du dossier `etalonnage/courses/`, il n'y a que les trois fichiers extraits, leurs compagnons et `etat-lancement-ligne1-v2.json`), ni dans le dossier de la ligne 1, ni parmi les fichiers suivis par git (recherche par nom). L'addendum scellé (§ 9, point 5) demande pourtant que « le journal du lanceur, les journaux d'étape, le fichier des arrêts et les deux fichiers d'identifiants de processus » soient « versés à côté des morceaux, tels quels, chacun avec son compagnon `.sha256` ». **Écart du versement à l'addendum, constaté, non expliqué par les pièces que j'ai lues.** Je n'ai pas cherché ces fichiers hors du dépôt (le dossier source `/home/user/runs-banc-a-ligne1-v2` nommé par le manifeste n'est pas dans mon mandat).

## 2. Ce qui a tiré, d'après le code

`etalonner` (étalonnage v2) écrit et scelle la sortie, puis appelle `exiger_portes`, qui lève la garde de la **première** porte manquée dans cet ordre : A9 (prise), A15 (cartes jugées par appel), A8 (audit). La sortie scellée dit `prise.passee: false` et `cartes_jugees_par_appel.passee: false` ; l'exception levée est donc `GardeA9Etalonnage`, message « garde A9 : porte de prise manquée (banc sans prise) : arrêt, retour à la mère ». C'est une déduction par le code et la sortie : faute du journal du lanceur, je n'ai pas vu le message ni le code de sortie (le registre provisoire de la session dit « code 3, environ 584 s » ; la sortie dit `secondes: 584.0`).

La branche « force » de A9 ne peut pas avoir tiré : elle lève l'exception dans `dichotomie`, avant toute course, et écrit un fichier `etape-forces-echec-A9-NN.json`. Aucun fichier de ce nom n'est dans le versement ; `etape-forces.json` est scellé avec quatre forces ; 400 courses par classe ont été jouées (`etapes`, « courses », `jouees: 400`).

## 3. Quantités contre seuils, telles que la sortie scellée les écrit

### 3.1 Portes

| porte (garde) | quantité dans la sortie | seuil (préenregistrement, configuration) | état écrit |
|---|---|---|---|
| prise (A9) | M1-nul de T0, classe « beaucoup », 400 courses : valeur **0,029171**, borne basse **0,022012**, borne haute 0,036640, 10 000 rééchantillons | borne basse strictement au-dessus de α = 0,05 | `passee: false` |
| cartes jugées par appel (A15) | « beaucoup » **1,998906** ; « peu » **1,896458** ; écart **0,102448** | écart ≤ 0,1 | `passee: false` |
| audit du générateur (A8) | aucune aire tirée (`tire: []`), aucune nommée hors plage, dans les deux classes | intervalle tout entier hors de [0,45 ; 0,55] | `passee: true` |

Mesure rapportée sans porte : M1-nul de T0, classe « peu » : valeur 0,044086, bornes [0,034645 ; 0,054125]. Cartes indéterminées : 9,17 % (« beaucoup »), 5,16 % (« peu ») ; plafond 20 % non atteint (`en_tete` vide). Aucun partiel récupéré (`partiels_recuperes` vide). Seul T0 a été calculé (`bras_calcules: ["T0"]`).

### 3.2 Forces (A9, première branche) : toutes atteintes

Tolérance 0,03 autour de la cible, 1 600 jugements par pas, 10 pas au plus.

| cible | force retenue | pas | taux au dernier pas |
|---|---|---|---|
| 0,90 | 0,41875 | 3 | 0,896875 |
| 0,50 | 0,18828125 | 6 | 0,5 |
| 0,30 | 0,1421875 | 5 | 0,328125 |
| 0,15 | 0,1076171875 | 8 | 0,15 |

### 3.3 Grille des lois tranchantes : taux de fausse promotion d'une carte seule

4 000 jugements par couple, monde sans effet, seuil 1/0,05.

| s \ c | 0,60 | 0,75 | 0,90 |
|---|---|---|---|
| 1,0 | 0,00500 | 0,00325 | 0,00625 |
| 1,3 | 0,00275 | **0,01000** (retenu) | 0,00675 |
| 1,6 | 0,00325 | 0,00650 | 0,00825 |
| 1,9 | 0,00200 | 0,00325 | 0,00425 |

### 3.4 Porte A15 : décomposition par étage et par rôle (comptes de la sortie, course pleine)

19 200 appels par classe (400 courses × 8 lignées × 6 générations), soit 38 400 places de juge (quota 2). Cartes jugées : 38 379 (« beaucoup ») et 36 412 (« peu »). Écart en cartes : 1 967, soit 1 967 / 19 200 = 0,10245 par appel : c'est la quantité de la sortie. Ce calcul est le mien ; il retombe sur la valeur scellée.

Classe « peu » (4 800 réceptions par lignée) :

| rôle (lignées) | jugées | refus mémoire | refus « affinage » | manque, en cartes par appel |
|---|---|---|---|---|
| vraie forte (1) | 4 594 | 151 | 55 | 0,0107 |
| vraies faibles (3) | 13 480 | 823 | 97 | 0,0479 |
| fausses diffuses (2) | 9 352 | 132 | 116 | 0,0129 |
| fausses tranchantes (2) | 8 986 | 578 | 36 | 0,0320 |
| total | 36 412 | **1 684** | **304** | 0,1035 |

Classe « beaucoup » : manque de 21 cartes (0,0011 par appel), toutes sur les fausses tranchantes (9 597 jugées pour 9 600 places) ; refus mémoire / « affinage » / quota : vraie forte 4 603 / 1 374 / 18 023 ; vraies faibles 23 555 / 2 662 / 45 801 ; fausses diffuses 5 089 / 3 039 / 39 872 ; fausses tranchantes 17 388 / 635 / 29 980.

## 4. Causes plausibles de la prise manquée

Les ordres de grandeur ci-dessous sont des calculs de ma main sur les scalaires de la sortie, non opposables ; la sortie ne donne ni le nombre de promotions vraies ni le nombre de promotions fausses par course, et je n'ai ouvert aucune sortie de course.

### C1 — Les lois fausses plantées passent rarement le juge, chaque carte seule (cause principale)

- **Ce qui l'appuie.** Sur la grille gelée, faite pour « cherche[r] la loi fausse la plus dure pour le juge » (préenregistrement, « Étalonnage »), le meilleur couple promeut une carte seule à 1,0 % ; les douze couples vont de 0,2 % à 1,0 %, c'est-à-dire au plus un cinquième du plafond 0,05 de l'inégalité de Ville. Par course, les cartes fausses jugées sont environ 24 tranchantes et 24 diffuses (9 597 et 9 600 sur 400 courses, classe « beaucoup »). À 1 % par carte tranchante, et en comptant l'arrêt d'une lignée promue, une course n'a une fausse promotion qu'avec une probabilité de l'ordre de 0,1 à 0,2. Le § 0 du préenregistrement dit déjà que la recherche amont ne change pas cette probabilité, puisque les cartes sont jugées sur des tirages frais : le banc ne peut faire monter T0 que par ce taux de base.
- **Ce qui la contredit ou la borne.** Le taux par carte des fausses diffuses n'est mesuré nulle part dans la sortie. Le taux par carte des tranchantes *dans les courses* n'est pas écrit non plus : les étages amont (mémoire, quota, tri sur la tranche) y choisissent quelles cartes sont jugées, ce que la grille ne fait pas. Je n'ai pas lu `selection_pari` (loi des traits), donc je ne peux pas dire pourquoi la région « trait au-dessus de s » pèse si peu.
- **Renfort, d'après la grille elle-même.** Le couple retenu (0,0100) se tient au-dessus de ses voisins (0,00275 à 0,00675). À 4 000 jugements, l'écart-type binomial est d'environ 0,0016. Le maximum de douze estimations bruitées est biaisé vers le haut, si bien que le vrai taux du couple retenu est sans doute au plus 0,01. Cela pousse dans le sens de C1 et ne l'explique pas à lui seul.

### C2 — Les rares promotions fausses sont diluées dans les promotions vraies

- **Ce qui l'appuie.** Par course, M1-nul vaut V / (V + T), où V compte les promotions fausses et T les promotions vraies, avec au plus une promotion par lignée sous T0, donc T ≤ 4. Une course avec une seule fausse promotion et 2 à 4 vraies apporte 0,20 à 0,33. La moyenne observée, 0,029, suppose donc qu'environ une course sur dix porte une fausse promotion (déduction, non établie). Le sens de l'écart entre classes est celui qu'attend cette dilution : M1-nul de T0 vaut 0,044 en « peu » contre 0,029 en « beaucoup ». La part des cartes fausses pour l'oracle parmi les cartes jugées des mondes à effet est de 51 % en « peu » contre 24 % en « beaucoup » : en « beaucoup », le tri des 12 variantes sur la tranche envoie au juge de meilleures cartes vraies, donc plus de promotions vraies au dénominateur, alors que V ne dépend pas de la classe d'après le § 0.
- **Ce qui la contredit ou la borne.** La sortie ne sépare pas V et T. L'écart « peu » − « beaucoup » n'a pas d'intervalle apparié dans la sortie. Même en « peu », la borne basse (0,0346) reste sous 0,05 : la dilution plus faible ne suffit pas non plus.

### C3 — La quantité de la porte est exigeante par construction

- **Ce qui l'appuie.** La porte demande que la moyenne par course d'un rapport (0 quand rien n'est promu) ait sa borne basse au-dessus de 0,05 sur 400 courses. Avec des fausses promotions rares (C1) et diluées (C2), cette moyenne reste petite. Le différentiel v1 → v2 du préenregistrement montre que la porte a été durcie, de « 0,005 par carte tranchante » à « T0 dépasse sur 400 courses d'étalonnage » (correction 6 de la contre-lecture, « porte de prise trop basse »). La grille observée (meilleur couple à 0,01) aurait passé la porte v1. Je le dis comme description de la porte gelée, non comme suggestion.
- **Ce qui la contredit.** Rien dans les pièces : c'est la porte scellée, appliquée telle quelle par `porte_prise` (`borne_basse > alpha`).

### C4 — La prédiction P10 n'était pas étayée par un calcul

- **Ce qui l'appuie.** P10 annonçait « passée : taux attendu entre 0,06 et 0,15. Confiance 0,6 ». Les prédictions sont « écrites avant tout tirage, sans exploration préalable », et je n'ai trouvé dans les sections lues aucun calcul qui relie le taux par carte de la grille au taux par course de T0. La possibilité d'un banc sans prise était prévue (ligne 3 de la table de lecture, liste d'arrêt A9). La manquer n'est donc pas, en soi, une anomalie du banc.
- **Ce qui la contredit.** Rien ; c'est un constat sur l'origine de l'attente, pas un mécanisme.

### C5 — Faute du banc ou du code qui ferait sous-promouvoir T0 (hypothèse examinée, non appuyée)

- **Ce qui la contredit.** La règle T0 est `ev["promue"]` de l'évaluateur (`regle_seule`), sans autre filtre. Le même `juger_banc` a atteint les quatre cibles de force (0,15 à 0,90) : le juge promeut quand il doit. La sortie porte les empreintes des modules de l'organisme chargés, égales à celles de la configuration (garde A1). L'audit du générateur passe. Aucun partiel n'a été repris.
- **Ce qui la laisse ouverte.** Sans le journal du lanceur, je ne vois pas que la garde A6 (jugement identique à `juger_carte`) a tourné dans cette chaîne. La première dérivation de la racine des essais (2026111900, à 23:56:02.72Z) le suggère, sans le prouver. Une faute propre au jugement des cartes `si_sinon` *dans les courses* (et non sur la grille) n'est pas exclue par lecture ; rien ne l'indique.

### C6 — Effet des étages amont sur les cartes tranchantes jugées (non établi)

En « beaucoup », 17 388 des 57 600 réceptions tranchantes sont refusées par la mémoire, et les cartes jugées sont les deux premières, d'après le test de mort sur la tranche, parmi les survivantes. Par le § 0, ce tri ne donne aucun avantage sur les tirages frais. Qu'il abaisse ou non le taux par carte par rapport à la grille, la sortie ne le dit pas.

## 5. Porte A15, manquée aussi : causes plausibles (pour la conduite du § 3 de l'addendum)

- **Mécanisme connu, rappelé par l'addendum (§ 3).** En « peu », un appel de deux variantes dont une est refusée par la mémoire ou par la règle « affinage » n'envoie qu'une carte au juge. En « beaucoup », le quota de deux reste rempli. La sortie le montre : 1 684 refus mémoire et 304 refus « affinage » en « peu », contre un manque de 21 cartes en « beaucoup ».
- **Cause plausible du dépassement de l'attente (0,086, mesure de contre-lecture citée par l'addendum) : des forces étalonnées petites, qui font coïncider les mots arrondis.** Le texte d'une carte `transformee` écrit chaque poids et chaque biais multipliés par la puissance, à deux décimales. Avec des forces de 0,11 à 0,19, ces valeurs sont petites, s'arrondissent souvent aux mêmes chaînes et partagent des bardeaux. Ce qui l'appuie : dans les deux classes, le taux de refus mémoire par réception suit l'ordre inverse de la force. En « peu » : fausses diffuses (hypothèse de force 1,0) 1,4 % ; vraie forte (0,419) 3,1 % ; vraies faibles (0,108 à 0,188) 5,7 %. En « beaucoup » : 8,8 %, 16,0 % et 27,3 %. Les vraies faibles portent la plus grosse part du manque (0,0479 par appel). Ce qui la borne : je ne sais pas à quels paramètres la mesure de 0,086 a été faite. La configuration porte des forces d'essai 1,0 ; 0,6 ; 0,4 ; 0,25, soit 2,3 à 3,2 fois les forces étalonnées ; si la contre-lecture les a employées, le mécanisme expliquerait l'écart, mais je ne l'ai pas vérifié (pièce non lue, hors mandat). Les trois vraies faibles sont regroupées sous un même rôle dans la sortie, si bien que je ne peux pas montrer la pente force par force.
- **Part des fausses tranchantes** (0,0320 par appel en « peu », dont 578 refus mémoire). C'est la « conséquence connue » du texte scellé : deux cartes `si_sinon` de même seuil arrondi et de même issue partagent quatre bardeaux sur six. L'addendum note que la phrase du texte scellé est trop courte pour la classe « peu ».

## 6. Ce que je n'ai pas pu établir

1. **Le message et le code de sortie réellement levés** : le journal du lanceur et `journal-etalonner.log` manquent au versement (écart à l'addendum, § 9, point 5). L'exception A9 est déduite du code (`exiger_portes`) et de la sortie scellée.
2. **Le nombre de promotions fausses et vraies sous T0, par course et par rôle**, que la sortie ne porte pas. Les fractions de courses avec fausse promotion avancées en C1 et C2 sont des déductions sur des scalaires, non des mesures.
3. **Le taux de fausse promotion par carte des fausses diffuses**, et celui des tranchantes dans les courses (après mémoire, quota et tri).
4. **La loi des traits** (`selection_pari.tirer_instances`), non lue : je ne peux pas chiffrer pourquoi les paris de région restent sous 1 %.
5. **Les paramètres de la mesure de 0,086** (contre-lecture du code v1, citée par l'addendum), non lue.
6. **Si la garde A6 a tourné dans cette chaîne** (indice seulement : première dérivation de la racine des essais à l'ouverture).
7. **Pourquoi `organisme.commit_lu` vaut `null`** (commit attendu `a41b7b50…`). `commit_organisme` rend `None` quand `git rev-parse` échoue dans la racine de l'organisme. C'est une lacune de provenance (R9) sans lien visible avec la prise ; les empreintes des modules chargés sont, elles, portées et égales.

## 7. Observations hors cause, pour mémoire

- Premières dérivations des racines 2026111901 et 2026111903 : 2026-11-19T23:56:02.80Z, postérieures au scellement de l'addendum (22:25:03Z, registre cité par l'erratum). Je n'ai pas lu `etat-lancement-ligne1-v2.json` (non nommé par mon mandat). La racine décisive 2026111902 n'apparaît pas parmi les premières dérivations.
- Audit du générateur : la régression sur trois traits, étiquette d'effet, sort en partie de la plage par son intervalle dans les deux classes (« beaucoup » [0,4469 ; 0,4956], « peu » [0,4369 ; 0,4991]). Le code la marque `porte: false` (le texte scellé ne la met pas sous la porte pour l'étiquette d'effet), et sa valeur ponctuelle reste dans la plage. Aucun effet sur l'arrêt.

## 8. Refus, écarts de ma part

Aucun refus d'outil. Aucun écart aux interdits du mandat : pas de heredoc ni de code passé à un interpréteur, aucune commande sous `archives-reponses-modeles/`, rien d'exécuté du banc, aucune écriture dans le dépôt. Une recherche par nom de fichier sur l'index git du dépôt entier (`git ls-files` avec motifs) a listé, parmi d'autres, des chemins sous `archives-reponses-modeles/` : aucune commande n'a porté sur ces chemins ; je le signale par prudence.

— lecteur de cause, modèle O
