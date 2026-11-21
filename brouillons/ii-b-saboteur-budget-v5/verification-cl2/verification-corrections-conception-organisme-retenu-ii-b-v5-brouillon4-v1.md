EXPLORATOIRE, NON OPPOSABLE (R-522)

# Vérification des corrections — conception de l'organisme retenu du saboteur à budget, v5, brouillon 4

**Verdict : scellable après corrections.** Il reste une correction de texte, majeure mais petite, et cinq mineurs. Aucun bloquant.

- Mes cinq majeurs et mes douze mineurs sont tous traités. Neuf le sont entièrement, et la remarque M4 l'est dans les termes que la session a décidés.
- L'outil d'assemblage, rejoué sur le brouillon 3, redonne le brouillon 4 et la table de traitement **à l'octet**.
- La grille du passage neuf est déclarée avant son lancement.
- J'ai rejoué un point de ce passage avec mon propre code et ma propre entropie : il le retrouve.
- La table des nœuds rend le scellement presque mécanique. Une exception : sous l'option par défaut du nœud 7, une phrase de résultat promet une lecture que cette option ne fait pas (R1 ci-dessous).

**Correction de ma vérification précédente.** Le rédacteur a raison : j'avais interverti les dossiers des deux scripts de dépendance. La chaîne `simulation-chaine-oracle-revise-ii-b-v2.py` est dans `brouillons/ii-b-saboteur-budget-v2/`, et l'oracle couplé `simulation-oracle-couple-ii-b-v4.py` dans `brouillons/ii-b-saboteur-budget-v3/`. Je l'ai contrôlé sur disque. Les empreintes entières de l'annexe C sont conformes : `696b40b4…4156` et `b5893fc0…3f94`.

- **Pièce** : `brouillons/ii-b-saboteur-budget-v5/conception-organisme-retenu-ii-b-v5-brouillon4.md`, sha256 `1a11b635bf285b3e2ea3779da9226ba14cdde06fffe67907aeab95606a74a10f`, vérifiée. Complément 10 : `50c9691d…c3bd`, vérifié et lu.
- **Compagnons** : tous les fichiers du dossier v5 ont leur compagnon `.sha256`, et tous se vérifient.
- **Noté, sans plus** : le rédacteur dit avoir supprimé une copie de contrôle à lui (`table.check`) et laissé `/tmp/b4.check`, hors de son dossier d'écriture. Ce fichier existe : 162 664 octets, la taille du brouillon 4.
- Aucun refus d'outil. Je n'ai rien lu de la liste d'interdits de mon mandat. Je ne tranche aucun nœud.
- **Lexique** : [N] = oracle à contexte réécrit, couplé par moitié ; [P] = jumeau au contexte même de l'agent.

## 1. Mes remarques : traitées ?

| remarque | où | état |
|---|---|---|
| M1, liberté après l'étalonnage | 5.1 (point 5), 10.3 (étapes 1 et 2), 10.6, 15, 13 (`designation_v5`) | **traité** : quatrième issue « non calculable », écrite d'avance, sans thèse ni nombre de tours ; la coupe en échec mène à « ne part pas » en 10.3 comme en 15 ; plus aucun « arrêt, nœud » ; les deux sens de « non calculable » sont distingués ; les essais sont ajoutés |
| M2, nœuds ouverts et plafond de tours | table des nœuds, 10.2, 17 | **traité**, sauf une incohérence sous l'option par défaut du nœud 7 (R1) |
| M3, la page penche | 5.3, 5.5, 18 | **traité** : plage donnée par dispersion ; effet d'un texte qui porte un huitième du niveau ; paragraphe « cette page ne penche pas », juste |
| M4, validité du contrôle du premier coût | 6 bis.2, 13 | **traité selon la décision de la session** : risque écrit en clair, sans sixième donnée ; garde portée par `controle_premier_cout_v5`, avec un cas sain et un artefact bien choisis (différence de forme sans gonflement) |
| M5, pièces et compagnons | annexe C ; fichier des différences ; compagnons | **traité** : outil du brouillon 3 dit perdu ; section 9 déclarée ; dépendances citées avec leurs empreintes entières (dossiers justes, voir ma correction) ; outil du brouillon 4 rendu et rejoué à l'octet |
| m1 à m12 et le point (10) | 6 bis.1, 6 bis.3, 6 bis.5, 1.2 (e), 8, 5.4, 13, 10.6, 1.4, 17 | **traités**, tous. m5 l'est en gardant la loi normale et en disant le niveau réel : c'est acceptable, puisque la loi de Student ne corrige pas l'écart (1,5 % à 1,8 % contre 1,6 % à 1,9 %) |

## 2. Le passage neuf : « instrument planté pour la branche à contexte réécrit »

**Ordre déclaré.** Grille écrite à 16:22:45Z ; empreinte du script ajoutée et passage lancé à 16:24:03Z ; passage fini à 16:24:57Z. L'empreinte écrite dans la grille (`e4663f9e…b511`) est celle du script versé. Ces heures restent déclarées, mais elles sont cohérentes avec le dépôt : le complément 10 est versé à 16:20:16Z (`1e3aea82`), le passage à 16:34:54Z (`2498daef`).

**Ce que la grille fixe avant le lancement.** Les deux règles de lecture (« chance réelle » et recommandation), les rapportés (marge ôtée, loi de Student) et ce qui fait foi sont fixés d'avance. Les seuils ne sont pas rechoisis. La recommandation (a) découle bien de la règle 3 appliquée telle quelle : la condition 1 rend 0,0 % ; la condition 2 rend 86 % contre 83 %.

**Rejeu indépendant.** Mon code ne reprend rien du rédacteur. Il réutilise mes propres fonctions de chaîne de la vérification précédente et ajoute une copie plantée des mêmes épisodes honnêtes. Entropie neuve `234426861514902711970750797519789754527`, 1 000 étalonnages. Cellule (0,8 ; 0,05 ; 0,7), lecture « dès le moindre écart », oracle sain :

| grandeur | rédacteur (sortie, ligne 91 ; 300 étalonnages) | mon rejeu |
|---|---|---|
| épisodes acceptés sur 64 : honnêtes k_H ; régénérés k_R ; plantés k_P | 3,67 ; 15,24 ; 15,72 | 3,52 ; 15,16 ; 15,75 |
| excès lu par action : instrument régénéré m_R ; planté m_P | 0,463 ; 0,181 | 0,463 ; 0,180 |
| conditions de [N] remplies : régénéré ; planté | 0,363 ; 0,273 | 0,392 ; 0,287 |
| issue sous (b) : [N] / [P] / ne part pas | 0,273 / 0,670 / 0,057 | 0,287 / 0,679 / 0,034 |

Les écarts restent dans l'erreur d'échantillonnage (erreur type d'environ 0,027 sur 300 étalonnages).

## 3. La table des nœuds : le scellement est-il mécanique ?

Oui, à une exception près. Le texte courant porte les options par défaut. Pour chaque autre option, la section 17 écrit le texte qui la remplace, ou dit qu'il n'y a rien à changer. Le plafond de tours est donné par deux entrées scellées pour chaque option du nœud 7. Il ne peut pas l'être en nombre de tours avant que les durées soient mesurées, mais la formule est mécanique : aucune liberté.

**R1 (majeur) — Sous l'option (b) du nœud 7, qui est le défaut, une phrase promet une lecture que l'option ne fait pas (5.1, table des revendications ; 10.6, « lecture du dommage positive, [P] » ; 17, nœud 7 (b)).**
Sous l'option (b), l'oracle non nommé ne joue qu'à l'étalonnage et sur les épisodes acceptés du maître : 960 actions, et rien à l'évaluation (section 12 : 11 200 actions en tout, contre 16 640 sous (a)). Pourtant, sous l'issue [P], 5.1 dit « le niveau, lu par [N], est rapporté à côté », et 10.6 dit à propos de l'élève « le niveau, lu par l'autre oracle, est rapporté à côté ». L'option (c) traite ce cas ; l'option (b) ne le fait que pour le maître.
Correction, au choix du directeur dans le nœud 7, puisque l'option change ce que le résultat peut dire :
- soit 17, nœud 7 (b), *texte* : ajouter « (iii) sous l'issue [P], 5.1, case « ce que la lecture du dommage peut dire » : « le niveau, lu par [N], est rapporté à côté » devient « le niveau du maître, lu par [N] sur ses épisodes acceptés, est rapporté à côté ; celui de l'élève n'est pas lu » ; 10.6, phrase [P] de la lecture du dommage positive : « le niveau, lu par l'autre oracle, est rapporté à côté » devient « le niveau de l'élève n'est pas lu (nœud 7, option (b)) » » ;
- soit étendre l'option (b) à l'évaluation : 2 560 actions de plus, soit 3 520 au lieu de 960 ; changer en conséquence la table des nœuds et la section 12.

**Options « non prêtes », dont le choix reporterait le scellement d'un passage déclaré de plus** : 2 (c), 3 (b), 5 (b), 5 (c) et 6 (c). Elles sont bien marquées. Deux options sont offertes comme prêtes alors qu'elles ne le sont qu'en partie (m-a) :
- **4 (b)**, la marge ôtée : les conditions et les erreurs sont jouées, mais pas la part des courses parties qui aboutissent. Le texte le dit en 17, mais pas dans la table.
- **1 (c)**, la règle sur les épisodes acceptés : sa puissance au niveau 1/40 n'est pas citée pour 48 à 96 épisodes. Pour 96 épisodes, elle se lit dans la sortie existante (×2 vu 98,8 % des fois, sortie du contrôle du premier coût, ligne 292) ; pour 48, la grille ne la contient pas.

La 4 (c) (relever le plafond) reporte le scellement d'un devis, non d'un passage.

## 4. Aucune liberté après l'étalonnage ?

Oui, une fois R1 corrigée :
- les quatre issues sont écrites d'avance, et chacune nomme sa phrase ;
- la liste d'arrêt ne renvoie plus à une décision ;
- le second passage est refusé par le lanceur ;
- les nœuds 2, 4 et 7 deviennent des constantes de configuration ;
- le cas où la garde de validité déclare le contrôle non valide, sous le nœud 1 (b) ou (c), est écrit d'avance.

Une réserve mineure (m-b) : « toute reprise est une course neuve, sous devis neuf » (5.1 et 15). Une reprise décidée après avoir vu un étalonnage qui n'est pas parti est un chemin qui bifurque. Correction : ajouter « et l'issue de cet étalonnage est rapportée avec tout résultat de la reprise », comme l'en-tête le fait pour la première course.

## 5. Sondage de dix chiffres neufs (douze)

Sortie P = `brouillons/ii-b-saboteur-budget-v5/sortie-simulation-instrument-plante-branche-contexte-reecrit-ii-b-v1.txt`.

| # | chiffre du texte | où | sortie | conforme |
|---|---|---|---|---|
| 1 | k_H ; k_R ; k_P au point situé, « dès le moindre écart » : 4,7 ; 6,4 ; 9,5 | 5.2 bis | P l. 103 (4,65 ; 6,39 ; 9,51) | oui |
| 2 | m_R ; m_P : 0,63 ; 0,14 ; effet minimal détectable 0,14 | 5.2 bis | P l. 103 (0,625 ; 0,141 ; 0,138) | oui |
| 3 | conditions de [N] au point situé, régénéré : 0,0 % ; 0,0 % ; 0,7 % | 5.2 bis | P l. 103, 130, 157, colonne 17 | oui |
| 4 | causes d'échec sous (b), « dès le moindre écart » : 7 / 17 / 50 / 26 / 0 % | 5.2 bis | P l. 103, colonnes 33 à 37 | oui |
| 5 | issue sous (b) au point situé : 0,0 / 94 / 6 % | 5.2 bis | P l. 103, colonnes 24 à 26 | oui |
| 6 | conditions de [N] sur la grille, planté : 3,7 ; 8,3 ; 9,4 % | 5.2 bis, 0 | agrégat de P, l. 90 à 225 | oui |
| 7 | ancrage 0,7, dispersion 0,08 : (a) 24 ; 41 ; 40 % ; (b) 5 ; 15 ; 18 % | 5.2 bis | agrégat de P | oui |
| 8 | marge ôtée, régénéré, au point situé : 8 ; 26 ; 38 % | 5.2 bis, 17 | P l. 103, 130, 157, colonne 19 | oui |
| 9 | bascule contre le maître ancré sous (b) : 82 ; 69 ; 70 % | 10.4 ter | P l. 236, 239, 242 | oui |
| 10 | part à tort contre un excès tenu en niveau, (b) : 89 ; 85 ; 84 % ; (a) : 86 ; 81 ; 82 % | 10.4 ter | P l. 238, 241, 244 ; l. 229, 232, 235 | oui |
| 11 | marge ôtée : issue [N] à tort contre l'ancré 4 ; 13 ; 19 % (au pire 39 %) ; contre un excès tenu en niveau 7 ; 9 ; 15 % (au pire 61 %) | 17, nœud 4 | P l. 245, 248, 251 ; l. 247, 250, 253 | oui |
| 12 | texte à un huitième : pente de fuite 83 % à 88 % ; conditions 5 à 9 % (a), 3 à 8 % (b) | 5.2 bis | agrégat de P | oui |

Un écart d'arrondi seulement : le niveau de la pente de fuite sous la loi normale vaut 1,95 % sous la lecture « dès le moindre écart », écrit « 1,9 % ».

## 6. Restes

- **R1 (majeur)** : l'option (b) du nœud 7 et les phrases « niveau rapporté à côté » (section 3 ci-dessus).
- **m-a** : dans la table des nœuds, marquer 4 (b) « dimensionnée sauf l'aboutissement » et 1 (c) « puissance à 1/40 citée pour 96 épisodes seulement », en ajoutant ce chiffre (98,8 %).
- **m-b** : une reprise après « ne part pas » ou « non calculable » se rapporte avec l'étalonnage qui l'a précédée.
- **m-c** : 17, nœud 2 (b), point (iii) : la phrase de 10.6 « arrêt au tour de contrôle … pour k_R sur 64 à l'instrument » se lit aussi avec k_P sous l'issue [N].
- **m-d** : 17, nœud 7 : écrire ce que porte le coût fixe sous (b) et (c) (l'évaluation à un seul oracle), comme sous (a).
- **m-e** : `/tmp/b4.check`, écrit hors du dossier d'écriture du rédacteur, et la copie de contrôle supprimée : ce sont des écarts à son cadre, que le journal v7 déclare. Rien à corriger dans la pièce.

## 7. Fichiers rendus

Dossier `/tmp/claude-0/-home-user-controle-ia-travail/6e2b0069-d4f4-5fd1-be63-f516f6a3ee23/scratchpad/verificateur-brouillon3/`, chaque fichier avec son compagnon `.sha256` :
- ce texte ;
- `rejeu-assemblage-brouillon4-v1.md`, `rejeu-assemblage-table-de-traitement-v1.md` et `sortie-rejeu-assemblage-brouillon4-v1.txt` : l'outil d'assemblage relancé, avec des empreintes égales à celles des pièces versées ;
- `rejeu-instrument-plante-v1.py`, sa sortie et ses erreurs (vides).
