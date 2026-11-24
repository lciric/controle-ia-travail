# Seconde vérification des corrections des projets de mandats du lecteur des sondes, du juge et de l'auditeur (lecture des sondes sur le saboteur à budget, barreau 8), version 3, brouillon 3 — v1

Pièce de travail, écrite le 2026-11-24 entre 16:38Z et 16:50Z par le contre-lecteur des projets de mandats du barreau 8 (sous-agent Opus 5.5 de la conductrice du côté des moniteurs, session `session_01Qi7Gr6acCdYGKsotBtUNvE`), auteur de `verification-corrections-mandats-v3-v1.md` (`544f07b02070bbd5cd46264e899eb8d3e31e9e4c3e58017106915fee3ac1e15a`). C'est une vérification courte : mes cinq remarques sont-elles faites et justes, les deux ajouts du rédacteur sont-ils justes, et le passage du brouillon 2 au brouillon 3 ne touche-t-il rien d'autre ? Pièces (commit `5a1ab22b4`), empreintes égales à leurs compagnons :

| pièce | empreinte |
|---|---|
| `projet-mandat-lecteur-sondes-v3-brouillon3.md` | `e92f33455286260e94130c315e00d3c07394ae8b61bf4d365bb8bf80269232fb` |
| `projet-mandat-juge-lecture-sondes-v3-brouillon3.md` | `9ae1baad53a195d16fc2acf56b7d5b1c64cb106e3d8b22c554ab8358f380057a` |
| `projet-mandat-auditeur-lecture-sondes-v3-brouillon3.md` | `66a5fb61d810df41cc88d2c98493e289ef6a837fe28f635ed4508c232990c1cd` |
| `corrections-verification-mandats-v3-v1.md` | `aeba3d1d21d7de748b02f90f83f13e1d0f1cfef05c7bcb44779e1c558e1b6f51` |

Brouillons 2 de comparaison : lecteur `119e6040…0c3a`, juge `b368e2ea…5b60`, auditeur `336e9958…9b75`.

## Verdict

**Conforme.** Les cinq remarques sont faites et justes ; les deux ajouts sont justes ; la différence entre les brouillons 2 et 3, faite par programme (`diff`), ne touche que les lieux de ces remarques, des deux ajouts, des en-têtes et des sections « Ce qui change ». Aucune remarque restante.

## Remarque par remarque

| remarque | état | constat |
|---|---|---|
| V-1, contrôle du déclenchement de l'audit | faite, juste | juge (ligne 15) et auditeur (ligne 19) : `['declencheurs_de_l_audit'].get('audit_de_symetrie_declenche') is True`, égal au texte proposé ; phrase « clé absente sous les lignes S1, S3, S4 et L5 : le contrôle rend alors « False » » ajoutée (juge, ligne 18 ; auditeur, ligne 22) ; juge, étape 4 (ligne 111) : « clé absente […] : vaut faux ». Plus aucune occurrence de la forme `['audit_de_symetrie_declenche']` dans les trois brouillons 3 (décompte par programme). Essai fait au tour précédent, même commande, sur une sortie factice sans la clé : « False » |
| V-2, verrou atomique et refus visible | faite, juste | lecteur, étapes 1 (ligne 164) et 3 (ligne 182) ; auditeur, étape 3 (ligne 124) : `mkdir <DOSSIER_JOURNAL>/<n>-<nom>.verrou && { setsid nohup bash -c '…' < /dev/null > /dev/null 2>&1 & } && echo LANCE || echo "RIEN N'EST LANCÉ"`, contenu de `bash -c '…'` identique, caractère pour caractère, à celui des brouillons 2 (constaté sur le `diff`) ; règles récrites (lecteur, ligne 120 ; auditeur, ligne 139) ; plus aucun `test ! -e … .pid` (le seul `test ! -e` restant est le contrôle de la référence boîte noire, lecteur, ligne 148). Forme éprouvée au tour précédent : premier lancement « LANCE », second « RIEN N'EST LANCÉ », rien de lancé |
| V-3, appel d'attente | faite, juste | lecteur, ligne 125 ; auditeur, ligne 127 : « relance alors **l'appel d'attente**, jamais l'étape » |
| V-4, relance décidée par la mère | faite, juste | lecteur, ligne 17 ; auditeur, ligne 24 : contrôle par `kill -0` sur l'ancien `.pid`, versement de l'ancien journal (inventaire scellé), renommage `<DOSSIER_JOURNAL>-tentative-<k>`, jamais d'effacement, même mandat |
| V-5, relecture arrêtée | faite, juste | auditeur, lignes 154 et 155, avant « Relecture inégale » : la chaîne « relecture arrêtée : voir le défaut D3 » (égale au code, ligne 2717) donne l'issue AU-a par le défaut D3, non une relecture inégale |

## Les deux ajouts du rédacteur

1. **`.code` lu quand le `.pid` manque** (lecteur, lignes 167 et 185 ; auditeur, ligne 127). Juste. Essai fait (bloc-notes, commande factice) : `cd` intérieur vers une racine absente → « LANCE » imprimé, aucun `.pid`, `.code` à 99, conformément au contenu de `bash -c` (`cd … || { echo 99 > ….code; exit 1; }`). La lecture du `.code` suivie d'un arrêt et d'un report est la bonne conduite ; le verrou reste en place, et une nouvelle tentative passe par la procédure de V-4.
2. **Inventaire du journal par `find <DOSSIER_JOURNAL> -type f | sort`** (lecteur, ligne 193 ; auditeur, ligne 172). Juste et nécessaire : le verrou est un dossier, et `sha256sum` sur un dossier échouerait. L'essai montre que `find … -type f` ne rend que les fichiers. Comme avant, la commande n'imprime que tailles et empreintes, sans ouvrir de contenu.

## Différence du brouillon 2 au brouillon 3 (par programme)

`diff` de chaque brouillon 2 avec son brouillon 3 :
- **lecteur** : blocs `1c1`, `3c3`, `5c5`, `7,14c7,11` (titre, en-tête, section « Ce qui change »), `19a17` (V-4), `121,122c119,120` (règles du lancement, V-2), `127c125` (V-3), `166c164` et `169c167` (étape 1 : V-2 et premier ajout), `184c182` et `187c185` (étape 3 : V-2 et premier ajout), `195c193` (second ajout) ;
- **juge** : blocs `1c1`, `3c3`, `5c5`, `7,12c7,8` (titre, en-tête, section « Ce qui change »), `19c15` et `22c18` (V-1), `115c111` (V-1, étape 4) ;
- **auditeur** : blocs `1c1`, `3c3`, `5c5`, `7,12c7,12` (titre, en-tête, section « Ce qui change »), `19c19` et `22c22` (V-1), `23a24` (V-4), `120c121`, `123c124` et `138c139` (V-2), `126c127` (V-2, V-3 et premier ajout), `152a154,155` (V-5), `169c172` (second ajout).

Rien d'autre ne change : ni les champs, ni les empreintes, ni les interdits, ni les consignes du dépôt, ni les étapes du juge hors de l'étape 4, ni la table des issues, ni les phrases de tête. La syntaxe des cinq lignes de lancement et de contrôle des brouillons 3, chevrons remplacés par des valeurs factices, passe `bash -n`.

## Ce que ce vérificateur a lu (pour le registre « qui a lu quoi »)

- Le relevé `corrections-verification-mandats-v3-v1.md` ; les `diff` des trois brouillons 2 aux trois brouillons 3 (gardés dans mon bloc-notes) ; des décomptes et recherches par programme dans les trois brouillons 3.
- Essai dans mon bloc-notes (`…/scratchpad/essai-99/`), commande factice ; aucun code de la lecture lancé ; aucun fichier du dépôt modifié ; aucun processus restant.
- `git log` des trois derniers commits (titres), `git status`, empreintes des pièces.
- **Non lus** : rien sous `diag/`, `donnees/`, `runs/`, `versement/`, `coffre/`, `docs/verdicts/` ; aucune pièce de la course, aucun ordre, aucune note d'interface ; aucun registre sous `registres/`.
