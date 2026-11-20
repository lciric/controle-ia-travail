# Contrôle de la condition (4) de la garde de recouvrement (ligne 3, étage 2) — v2

Pièce de travail (classe C), écrite le 2026-11-20, sous le même mandat : `mandat-controleur-condition-4-garde-recouvrement-v1.md`, empreinte `c7f395df0255f19f4a37aad18d5b0f2b7d1bc8afad5531d6da4f84840f08b726`, en-tête compris. Même contrôleur, modèle O, qui n'a écrit ni le générateur, ni le code d'appel, ni le texte de la ligne 3. Le contrôle v1 (`934d6bce…`), qui jugeait le programme v1, est gardé tel quel. Cette pièce juge le programme v2 :

- fichier : `generateur-v2/generer_temoins_ligne_3_v2.py`
- empreinte : a3a4e82f15afbabfb53a954e24ed9db709c5d8f2da5f907978e7612e3fddca65

## Verdict

Conforme

Les six points de la condition (4) sont tenus dans le code de la v2, à la lettre du texte v7, l. 257-263. Le défaut du point 5 relevé en v1 est corrigé. Ce verdict vaut pour ce programme seul, à l'empreinte ci-dessus, et pour la garde **entière** (94 cartes) ou pour le repli par le **premier** déclencheur. Il ne vaut pas pour le repli par le second déclencheur : voir la réserve B. Une réserve de procédure doit être portée à l'additif de code : voir la réserve A.

## Pièces (empreintes recalculées, égales à leur compagnon)

| pièce | sha256 |
|---|---|
| texte v7, l. 30 et 257-263 | `4e3680d9915ef6e2fa33010fc9b7b2ef5575d74e58e982bfabdbdbcc3e99d5a0` |
| `generer_temoins_ligne_3_v2.py`, lu en entier pour la garde (l. 1-420, 900-1402, 1760-1871) ; le reste par l'analyse statique | `a3a4e82f15afbabfb53a954e24ed9db709c5d8f2da5f907978e7612e3fddca65` |
| `rapport-developpeur-generateur-etage-2-v2.md`, en entier | `64254de51a5aab3553de23b0153bc116416aaf53fcabb53b306949f74f50ef32` |
| `differentiel-programme-v1-v2.diff`, dont l'empreinte a été vérifiée (je l'ai remplacé par la lecture directe des zones de la garde) | `87157eef682163bd95aaae6333757b4856c624eb392565f054ec71a3bb39ef46` |
| `table-empreintes-generateur-v2.txt` | `f763d167f9b6c7fda36d6dca4052c068e3b6e63f078b6b6525638b365ed97228` |
| `.gitignore` du dépôt de travail, lu pour savoir si `runs/` est suivi | — |
| mon analyse statique (`analyse_statique_v1.py`) ; sa sortie sur la v2 (`analyse-statique-sortie-v2.txt`), dans mon dossier | `a9f80807…` ; `c942b8c347fa349810bc067e55f6ddc230b66a47112eb99415eaaf0896409d54` |

Je n'ai lancé aucune commande sur un chemin sous `archives-reponses-modeles/` et je n'ai pas ouvert le fichier des cartes. Je n'ai lancé ni la garde, ni le générateur, ni ses essais. Aucun appel à un fournisseur ; aucune écriture dans le dépôt.

Les numéros de ligne qui suivent renvoient à `generer_temoins_ligne_3_v2.py` (empreinte `a3a4e82f…`).

## Points

### 1. Entrée unique — tenu

- **Constantes.** Chemin, empreinte et compte sont des constantes du code (l. 139-142), égales à la lettre au texte v7 (l. 258 et 30). Les sept cartes nommées (l. 143-144) sont égales à l'en-tête (l. 30).
- **Production.** Elle ne prend que ces constantes. Le constructeur nu de nature « production » refuse toute autre valeur (l. 921-923). Toute autre nature passe par `garde_chemins` (l. 925). `EntreeV2` passe par `garde_chemins` dès son constructeur (l. 951). Correction R3 de la v1 : faite.
- **Hors d'atteinte des arguments.** Aucune variable d'environnement n'est lue. La ligne de commande n'admet que la liste fermée `ARGUMENTS_GARDE` (l. 169-170 ; l. 1774-1787), qui ne contient aucune entrée de cartes. `__main__` ne passe aucune voie d'essai (l. 1870).
- **Ordre des vérifications.** Le fichier n'est ouvert qu'une fois (l. 941-944, appel l. 1334). L'empreinte est vérifiée sur les octets avant toute analyse (l. 1335-1337 : `EmpreinteCartesAutre`, ni garde ni repli). Le compte de 94 est vérifié (l. 1346-1347) avant toute comparaison (l. 1350-1356).
- **Aucun autre chemin de l'archive.** `garde_chemins` contrôle, avant toute ouverture, la banque, le journal, le manifeste du journal, la sortie, la pièce du (4) et la pièce du repli (l. 1284). La seconde entrée est une constante hors de l'archive.
- **Voie d'essai.** Elle ne peut pas atteindre le vrai fichier : `EntreeCartes.essai` (l. 934-939) et le constructeur (l. 925) passent tous deux par `garde_chemins`, qui contrôle la forme écrite puis le chemin réel (l. 385-403).

### 2. Retrait du champ `meta` — tenu, et suffisant au sens du texte

- `sans_meta` (l. 980-982) est le crochet `object_hook` de l'analyse JSON (l. 992). Chaque objet perd sa clé `meta` dès qu'il est construit, à toute profondeur, niveau du fichier compris. Seul l'analyseur voit la clé, le temps de construire l'objet. Aucune structure gardée en mémoire ne la porte.
- Une garde dure suit (l. 1005-1006).
- Avant ce retrait, seule l'empreinte des octets bruts est calculée (l. 1335), comme le texte l'exige.
- L'identifiant (l. 1007), le compte (l. 1346), les sept cartes du repli (l. 1344) et les bardeaux (l. 1351-1353) ne voient que des objets sans `meta`.
- La réserve du point 2 en v1 (forme réelle, `meta` imbriqué, `meta` au niveau du fichier) est levée. La lettre « le champ `meta` de chaque carte », l. 259, est tenue quelle que soit la forme.

### 3. Aucune écriture d'un bardeau ou d'un texte de carte — tenu

J'ai suivi chaque voie de sortie avec l'analyse statique : fichiers, journal, manifeste, rapport, sortie standard et d'erreur, sous-processus, exceptions, avertissements, `repr`.
- **Fichiers.** Le manifeste de la garde (l. 1327) et la ligne « ouverture » du journal (l. 1329) sont écrits avant l'ouverture (l. 1334). Après l'ouverture ne sortent que deux choses : la ligne « clôture » (l. 1374-1376), faite de la décision, de comptes et du lieu de l'exception ; et le rapport validé (l. 1387, via l. 1073-1075).
- **Bardeaux.** Ce sont des variables locales seulement (l. 1350-1357).
- **Sortie standard et sortie d'erreur.** La sortie standard ne reçoit que le rapport validé (l. 1815-1817) ou la sortie de secours (l. 1799 : décision, classe et lieu). Le geste `garde` n'écrit rien sur la sortie d'erreur.
- **Sous-processus.** Le seul est `git rev-parse`, sortie capturée (l. 374), avant l'ouverture.
- **Exceptions.** Toutes sont attrapées : l. 1362, 1377, 1388 dans la garde ; l. 1819 sur tout le geste `garde`, lecture des arguments et écriture sur la sortie standard comprises (l. 1807-1823) ; l. 1829-1833 pour la lecture du geste. `lieu_de` (l. 1025-1032) parcourt la trace par `walk_tb` sans lire le source. Il ne rend que la classe, `NOM_DU_PROGRAMME` et un numéro de ligne. La sortie de secours (l. 1790-1802) ne recalcule rien, écrit par `os.write` et avale tout échec. La correction R6 de la v1 est faite : aucune trace brute ne peut sortir du geste `garde`.
- **Avertissements.** Ils deviennent des exceptions dans le corps de la garde (l. 1278-1279).

### 4. Liste fermée des champs de sortie — tenu

- Les treize champs (l. 152-154) sont ceux de la l. 260. `valider_rapport_garde` (l. 1035-1070) refuse tout champ hors liste et contrôle la forme de chacun.
- Chaque écriture du rapport passe par elle : sur disque, l. 1074 avant 1075 ; en retour, l. 1394 (donc avant la sortie standard, l. 1816) ; sortie de secours, l. 1798.
- Le rapport de repli d'écriture garde désormais `nombre_de_rejeux` (l. 1392-1393).
- La sortie de secours ne porte que `decision` et `exception`, sous-ensemble de la liste. Elle ne sert que si rien d'autre n'est possible.

### 5. Compte des rejeux — tenu

- **Constantes.** Le journal et le manifeste de sa création sont des constantes (l. 161-163). `LieuDuJournal` de nature « production » refuse tout autre chemin (l. 1140-1147).
- **Aucun chemin libre.** La garde n'accepte que les arguments de `ARGUMENTS_GARDE` (l. 169, 1774-1787) : un `--journal-rejeux` est refusé (`ArgumentHorsListe`) avant toute ouverture. `creer-journal-rejeux` n'accepte aucun argument (l. 1838-1839). La voie d'essai `LieuDuJournal.essai` n'existe qu'en Python (l. 1153-1156).
- **Pas de recréation.** `creer_journal_rejeux` refuse si le manifeste ou son compagnon existe (l. 1164-1165). Le journal est créé en mode exclusif (l. 1167) : si le seul manifeste a disparu mais que le journal existe, la création échoue sans rien écrire.
- **Au lancement, avant l'ouverture,** la garde exige :
  - le manifeste de création scellé, c'est-à-dire compagnon égal, geste exact, nom du journal et nature (l. 1178-1189, appelé l. 1290) ;
  - puis le journal, lu en entier (l. 1291 ; absent : `JournalRejeuxAbsent` ; illisible : `JournalRejeuxIllisible`, l. 1082-1113).
- **Comptage.** La ligne « ouverture » est écrite avant l'ouverture (l. 1329), donc toute exécution qui ouvre le fichier est comptée, panne comprise. Le premier passage est au rang 1, rejeu 0 (l. 1328-1332).
- **Refus au sixième rejeu.** Il est prononcé avant l'ouverture, sans le mot de la mère (l. 1299-1301). Un même mot ne vaut qu'une fois (l. 1302-1303). Le mot est cité au manifeste (l. 1322).
- **Ce qui reste hors de portée du code :** la suppression ou la troncature du journal à la main, manifeste gardé ; la suppression des deux fichiers ; la perte du répertoire de travail. Voir la réserve A.

### 6. Chemin du repli — tenu pour la garde entière et pour le repli par le premier déclencheur ; voir la réserve B pour le second

- Ses deux déclencheurs sont des constantes (l. 147-148). Une cause hors de ces deux donne `ReplisHorsDeclencheur` (l. 1294-1296). La pièce du déclencheur est vérifiée par chemin et empreinte (l. 1297). Tout cela se passe avant l'ouverture.
- Les règles sont les mêmes que pour la garde entière :
  - même fichier, même ouverture, même empreinte (l. 1334-1337) ;
  - `meta` retiré à toute profondeur (l. 992) ;
  - sept cartes nommées, chacune trouvée une fois (l. 1013-1022, 1344) ;
  - même liste fermée, avec le repli au rapport (l. 1361, 1066-1070) et l'écart au manifeste (l. 1323-1325) ;
  - pièce du (4) à verdict exigée aussi sous le repli (l. 1293).
- Le compte de 94 n'est pas exigé sous le repli. C'est conforme à la lettre de la l. 263.
- Le compte des rejeux continue : même journal à constantes (point 5).

## Questions posées par la mère

### Emplacement des constantes du journal (`DEPOT/runs/ligne-3-etage-2-garde-de-recouvrement-v1/`)

Il convient, sous la réserve A.
- Il est hors de l'archive. Aucun composant ne commence par « coffre ». Il n'est pas sous les racines interdites (l. 175-176 : le dossier de course v9 sous `runs/` est un dossier frère, distinct).
- Il est hors du dossier du code.
- `runs/` n'est pas exclu par le `.gitignore` du dépôt : le journal et son manifeste peuvent être suivis par git.

**Réserve A (procédure, à écrire à l'additif de code).** Le compte ne survit à une session neuve ou à un clone neuf que si le journal et son manifeste sont **commis et poussés** :
- juste après `creer-journal-rejeux` ;
- puis après chaque passage de la garde, à la passation.

Sinon, un répertoire de travail neuf perd les deux fichiers. La garde refuse alors, ce qui est le sens prudent, mais `creer-journal-rejeux` serait de nouveau accepté et le compte repartirait de zéro. Le code ne peut pas l'empêcher sans état extérieur. Durcissement conseillé pour une version suivante, sans effet sur ce verdict : `creer_journal_rejeux` refuse si l'historique git connaît déjà le chemin du manifeste. Une troncature du journal à la main reste un geste délibéré ; l'historique git le rendrait visible.

### Lecture des pièces sous le repli par le second déclencheur

Le développeur lit ainsi les deux pièces :
- `--controle-4` : la pièce qui rend « Conforme » les autres points et le chemin du repli ;
- `--piece-repli` : la pièce « non conforme sur l'entrée ».

Cette lecture est cohérente avec la l. 263, qui demande deux constats distincts : le déclencheur, et le « conforme » sur le reste. Le code la tient mécaniquement (l. 1293, 1297).

**Réserve B, bloquante pour ce seul cas.** Le code ne distingue pas un « Conforme » limité au repli d'un « Conforme » qui vaut pour la garde entière. `exiger_controle_conforme` (l. 1192-1204) ne connaît pas `repli`. Une pièce écrite pour le seul repli (l'entrée y est jugée non conforme) laisserait donc tourner la garde entière si on la passait sans `--repli`. À l'inverse, si son auteur l'écrit honnêtement (« Conforme pour le repli »), elle ne passe pas la forme de la l. 167.

Avant tout usage du second déclencheur, il faut une version neuve, contre-lue :
- une ligne de portée exigée dans la pièce du (4) (garde entière, ou repli seulement) ;
- confrontée à `repli` ;
- la pièce du déclencheur, elle, lue pour son verdict « non conforme » sur un point propre à l'entrée.

Tant que cette version n'existe pas, le repli par le second déclencheur ne tourne pas. Le chemin à suivre est alors celui de la l. 263 : ni garde ni repli, la banque n'est pas scellée, la mère est saisie. Cette pièce ne déclenche pas ce cas, puisqu'elle rend l'entrée conforme.

## Remarques, non bloquantes

- **C1.** `exiger_controle_conforme` vérifie l'empreinte (l. 1195), puis relit le texte (l. 1197) : il reste une fenêtre entre les deux lectures. Conseil : lire les octets une fois, puis vérifier l'empreinte et le verdict sur ces mêmes octets.
- **C2.** Le geste `creer-journal-rejeux` laisse sortir une trace brute si le journal existe déjà (`FileExistsError`, qui n'est ni `Refus` ni `RefusGarde`, l. 1861). Ce n'est pas la garde, et aucune carte n'est en jeu.
- **C3.** Restent de la v1 : aucun verrou contre deux exécutions simultanées (le cas finit en refus, sens prudent) ; le lien physique ; la fenêtre entre la vérification d'un chemin et son ouverture ; la présence du fichier sur disque avant le premier passage (« (branche) », l. 30 et 258), à régler par la procédure, sans aucune commande sur ce chemin.
- **C4.** Je suis la recommandation du développeur (rapport v2, § 3) : retirer, dans une version suivante, les deux formes inutiles (liste, `{"fiches": [...]}`). Elles sont sans risque aujourd'hui.
- **C5.** La pièce du (4) n'est reconnue que par sa forme (l. 167-168, 1200-1204) : une pièce d'un autre auteur à la même forme passerait. Le chemin et l'empreinte de cette pièce-ci, au manifeste de la garde et à l'additif, en tiennent lieu.

Contrôleur de la condition (4), modèle O.
