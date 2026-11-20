# Contrôle de la condition (4) de la garde de recouvrement (ligne 3, étage 2) — v3

Pièce de travail (classe C), écrite le 2026-11-20 sous le même mandat : `mandat-controleur-condition-4-garde-recouvrement-v1.md`, empreinte `c7f395df0255f19f4a37aad18d5b0f2b7d1bc8afad5531d6da4f84840f08b726`, en-tête compris. Même contrôleur, modèle O, qui n'a écrit ni le générateur, ni le code d'appel, ni le texte de la ligne 3. Les contrôles v1 (`934d6bce…`) et v2 (`f2066452…`) sont gardés tels quels.

Cette pièce juge le programme v3 : `generateur-v3/generer_temoins_ligne_3_v3.py`, empreinte f5de9c3c94be525d1ec48d3e7954135473894a298aafe908475f043934278ae0.

## Verdict

Conforme

Portée : garde entière

Les six points de la condition (4) sont tenus dans le code de la v3, à la lettre du texte v7, l. 257-263. L'ordre est tenu lui aussi : toutes les exigences passent avant l'unique ouverture du fichier des cartes. Cette pièce ne vaut que pour la garde **entière** (94 cartes, sans `--repli`), conformément à la règle « une pièce par portée ». Le code la refuse sous `--repli` (l. 1263-1265). Une garde sous le repli, par l'un ou l'autre déclencheur, demanderait une pièce distincte qui porte la portée « repli seul » ; je ne l'écris pas ici. La réserve A, une règle de procédure, reste à écrire à l'additif de code.

## Pièces (empreintes recalculées, égales à leur compagnon)

| pièce | sha256 |
|---|---|
| texte v7, l. 30 et 257-263 | `4e3680d9915ef6e2fa33010fc9b7b2ef5575d74e58e982bfabdbdbcc3e99d5a0` |
| `generer_temoins_ligne_3_v3.py`. Lu directement : l. 948-1103, 1163-1465, 1858-1946. Le reste par le différentiel et l'analyse statique. | `f5de9c3c94be525d1ec48d3e7954135473894a298aafe908475f043934278ae0` |
| `rapport-developpeur-generateur-etage-2-v3.md`, lu en entier | `f677bd08777442f58d4fc24d003bef1a7cd3339e4cf7e62d8abed1bb098f79ab` |
| `differentiel-programme-v2-v3.diff`, lu en entier ; les zones de la garde ont aussi été relues dans la v3 | `b88de2f0d751e8dd5cb1aa1dd672428142bdaec032e875b7179f240a7bca76de` |
| `table-empreintes-generateur-v3.txt` | `8e87f2bd51178a2f87ab9f296a7533864a1894df7c98740b0b6fe153fc79b412` |
| mon analyse statique (`analyse_statique_v1.py`) et sa sortie sur la v3 (`analyse-statique-sortie-v3.txt`), dans mon dossier | `a9f80807…` ; `a22990c6a3f5a00b981e242771d2bc4306c27a0376839d412ebfeda44d1cbf8e` |

Je n'ai lancé aucune commande sur un chemin sous `archives-reponses-modeles/`. Le fichier des cartes n'a pas été ouvert. Je n'ai lancé ni la garde, ni le générateur, ni ses essais. Aucun appel à un fournisseur, aucune écriture dans le dépôt.

Les numéros de ligne qui suivent renvoient à `generer_temoins_ligne_3_v3.py`.

## Ordre des exigences avant l'unique ouverture (`jouer_la_garde`, l. 1335-1463)

1. Les entrées sont construites sous `try` (l. 1347-1349).
2. `garde_chemins` passe sur la banque, le journal, le manifeste du journal, la sortie, la pièce du (4) et la pièce du repli (l. 1351).
3. La sortie doit être neuve (l. 1352-1356).
4. Le manifeste de création du journal, scellé, est exigé (l. 1357).
5. Le journal est lu ; absent ou illisible, c'est un refus (l. 1358).
6. Sous `--repli` seulement : la cause doit être l'un des deux déclencheurs (l. 1360-1362), puis la pièce du déclencheur est vérifiée par empreinte (l. 1363).
7. La pièce du (4) est exigée : verdict, empreinte du programme, portée confrontée à `repli` (l. 1364-1365).
8. Refus au sixième rejeu sans le mot de la mère (l. 1367-1371).
9. Lecture de la banque (l. 1372), puis de la seconde entrée par empreinte et compte (l. 1375).
10. Le manifeste de la garde est écrit (l. 1395).
11. La ligne « ouverture » est écrite au journal (l. 1397).
12. **Unique ouverture** du fichier des cartes (l. 1402).

Toutes les exigences sont donc vérifiées avant l'ouverture, cause et pièce du repli comprises, avant la pièce du (4).

## Points

### 1. Entrée unique — tenu

- **Constantes.** Le chemin, l'empreinte et le compte sont des constantes (l. 150-153), égales à la lettre au texte v7 (l. 258 et 30). Les sept cartes nommées (l. 154-155) sont égales à l'en-tête.
- **Constructeur de production.** De nature « production », il n'accepte que ces constantes (l. 957-959). Toute autre nature passe par `garde_chemins` (l. 961, 972). `EntreeV2` passe par `garde_chemins` dès son constructeur (l. 987).
- **Ligne de commande et environnement.** Les arguments forment une liste fermée (l. 185, 1842). Aucune variable d'environnement n'est lue. `__main__` ne transmet aucune voie d'essai (l. 1945).
- **Empreinte et compte.** L'empreinte est vérifiée sur les octets avant toute analyse (l. 1403-1405). Le compte de 94 est vérifié (l. 1414-1415) avant toute comparaison (l. 1418-1424).
- **Aucun autre chemin de l'archive.** `garde_chemins` passe sur tous les autres chemins (l. 1351). La voie d'essai ne peut pas atteindre le vrai fichier (l. 961, 972).

### 2. Retrait du champ `meta` — tenu, et suffisant

- Le crochet `object_hook` `sans_meta` (l. 1016-1018, 1028) retire `meta` à toute profondeur, niveau du fichier compris. Une garde dure suit (l. 1036-1037).
- Seule la forme réelle est admise (l. 1029-1035) : objet non vide ; clés de treize caractères ; valeurs objets portant un `contenu` objet. Toute autre forme donne `FormatCartesInconnu`, avant le compte et toute comparaison.
- Les sept cartes du repli sont prises par égalité exacte (l. 1047). Elles ne voient que des objets sans `meta`.

### 3. Aucune écriture d'un bardeau ou d'un texte de carte — tenu

- **Fichiers.** Le manifeste de la garde et la ligne « ouverture » sont écrits avant l'ouverture (l. 1395, 1397). Après l'ouverture ne sortent que la ligne « clôture » (l. 1442-1444 : décision, comptes, lieu) et le rapport validé (l. 1455). Les bardeaux restent dans des variables locales (l. 1418-1425).
- **Sortie standard.** Seulement le rapport validé (l. 1883-1885), ou la sortie de secours : décision, classe et lieu (l. 1858-1870).
- **Exceptions.** Toutes sont attrapées : l. 1430, 1445, 1456, et l. 1887 sur tout le geste `garde`. `lieu_de` (l. 1054-1061) parcourt la trace par `walk_tb`, sans lire le source, et ne rend que la classe, le programme et la ligne.
- **Avertissements.** Ils deviennent des exceptions (l. 1345-1346).
- **Geste `creer-journal-rejeux`.** Il ne touche jamais les cartes. Toute exception y est réduite à la classe et à la ligne, sur la sortie d'erreur, sans trace (l. 1906-1915). `git log` y est lancé avec sa sortie capturée et l'entrée fermée (l. 1198-1199).

### 4. Liste fermée des champs de sortie — tenu

- **La liste.** Treize champs (l. 163). `valider_rapport_garde` (l. 1064-1099) refuse tout champ hors liste et vérifie la forme de chaque valeur.
- **Validation avant toute écriture.** Sur disque, l. 1103 avant 1104. En retour, et donc avant la sortie standard, l. 1462. Dans la sortie de secours, l. 1866.
- **Rapport de repli d'écriture.** Il ne garde que la décision, l'empreinte du programme, le nombre de rejeux et l'exception (l. 1460-1461).

### 5. Compte des rejeux — tenu

- **Constantes.** Le journal et son manifeste de création sont des constantes (l. 172-174). `LieuDuJournal` de nature « production » exige ces constantes et le dépôt `DEPOT` (l. 1171-1173).
- **Aucun chemin libre.** Ni pour la garde (l. 185, 1842), ni pour la création (l. 1907-1908).
- **Création refusée** dans trois cas, tous avant toute écriture :
  - si le manifeste ou son compagnon existe (l. 1213-1214) ;
  - si l'historique git, toutes références, connaît déjà le manifeste (l. 1189-1204, 1215-1216 ; historique illisible : refus) ;
  - si le journal existe sans manifeste (l. 1217-1218).
  
  Le journal est ensuite créé en mode exclusif (l. 1220).
- **Au lancement.** Le manifeste scellé est exigé (l. 1231-1242), puis le journal, lu en entier (l. 1358) ; l'un ou l'autre absent ou illisible donne un refus avant l'ouverture.
- **Décompte.** La ligne « ouverture » est écrite avant l'ouverture (l. 1397) : toute exécution qui ouvre le fichier est donc comptée. Le premier passage est au rang 1, rejeu 0 (l. 1396-1400).
- **Refus au sixième rejeu** sans le mot de la mère, avant l'ouverture (l. 1367-1369). Un même mot ne vaut qu'une fois (l. 1370-1371).

### 6. Chemin du repli — tenu

- **Déclencheurs.** Seulement les deux constantes (l. 158). Toute autre cause donne `ReplisHorsDeclencheur`. La pièce du déclencheur est vérifiée par empreinte, avant la pièce du (4) et avant l'ouverture (l. 1360-1363).
- **Mêmes règles que la garde entière.**
  - Même fichier, même ouverture, même empreinte (l. 1402-1405).
  - `meta` retiré à toute profondeur (l. 1028).
  - Sept cartes nommées, chacune trouvée une fois par égalité exacte (l. 1043-1051, 1412).
  - Même liste fermée, avec le repli au rapport (l. 1429).
  - L'écart est porté au manifeste (l. 1391-1393).
  - Même journal : le compte continue.
- **Réserve B du contrôle v2 : levée.** La pièce du (4) doit porter une seule valeur de portée (l. 1260-1262). Cette valeur doit être « garde entière » sans `--repli` et « repli seul » avec `--repli` (l. 1263-1265). Une pièce écrite pour la garde entière ne peut donc pas servir sous le repli, et une pièce écrite pour le repli ne peut pas servir à la garde entière.
- **Lecture du développeur.** Sous le second déclencheur, il fait passer la pièce « repli seul » par `--controle-4` et la pièce du déclencheur par `--piece-repli`. Cette lecture est cohérente avec la l. 263. Elle vaut aussi sous le premier déclencheur : la garde n'y tourne qu'avec une pièce « repli seul » qui rend conformes les autres points et le chemin du repli.
- **Remarque C1 du contrôle v2 : levée.** Chaque pièce est lue une seule fois. L'empreinte est vérifiée sur ces octets, et ce sont ces mêmes octets qui sont analysés (l. 1250-1255, 1268-1279).

## Réserve et remarques

- **Réserve A (procédure, à écrire à l'additif de code).** Il faut commettre et pousser le journal et son manifeste juste après la création, puis après chaque passage, à la passation.
  - Le contrôle de l'historique (l. 1215) ne protège que ce qui a été commis. Il dépend aussi de la profondeur de l'historique local : un clone superficiel peut ne pas voir un commit ancien qui a retiré le manifeste.
  - Si le manifeste est présent dans l'arbre, la création est de toute façon refusée (l. 1213).
- **R-a.** La pièce du déclencheur du repli est vérifiée par son empreinte seulement, pas par son contenu. C'est inévitable pour le premier déclencheur (le refus écrit de la mère). Pour le second, la procédure doit nommer la pièce par chemin et empreinte au manifeste ; la garde l'y porte déjà (l. 1391-1393).
- **R-b.** Les lignes de verdict et de portée sont reconnues par des expressions où figurent « é » et « è » (l. 178, 182). Une pièce écrite sous une autre normalisation Unicode serait refusée : le défaut va dans le sens prudent.
- **R-c.** Restent des versions précédentes, sans effet sur le verdict : aucun verrou contre deux exécutions simultanées, avec un refus ensuite, ce qui va dans le sens prudent ; le lien physique ; la fenêtre entre la vérification d'un chemin et son ouverture ; la présence du fichier des cartes sur disque avant le premier passage, à régler par la procédure, sans aucune commande sur ce chemin.

Contrôleur de la condition (4), modèle O.
