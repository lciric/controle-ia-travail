# Protocole de comptage, version 1 — part des tâches archivées qui admettent une propriété fixée d'avance par un tiers et vérifiable par programme

- **Classe** : C (pièce de travail), écrite et scellée avant tout comptage. Elle ne se réécrit pas : une correction passe par un erratum ou par une version 2.
- **Auteur** : Claude Fable 5.2, effort maximal, agent neuf lancé par la session mère. Il n'a codé aucune tâche et n'en codera pas.
- **Heure** : 21 novembre 2026, 18 h 10 en temps universel (relevée par `date -u` au début de la rédaction).
- **Accord** : mots de Lazar du 21 novembre vers 17 h 30 en temps universel, « go » au premier geste sans dépense (GO-2026-11-21-69 ; `registres/go.md`, ligne 668, dépôt au commit `1b49fa53b7639ee5307d70cad21cb96668444edb`).
- **Source** : `docs/notes/mecanisme-adjudant-hors-distribution-v1/lecture-collisionneur-adjudant-opus-v1.md`, lignes 15, 22, 31, 32 et 54 à 62, seules lues (empreinte en section 12).
- **État** : aucun énoncé de tâche du dépôt n'a été lu par l'auteur ; la grille est écrite à l'aveugle des tâches qu'elle servira à compter.
- **Pièces jointes, même dossier** : `epreuve-habilitation-codeurs-v1.md` (dix énoncés hors programme, remis aux codeurs), `cle-epreuve-habilitation-codeurs-v1.md` (fermée aux codeurs), `liste-recherche-prescrite-v1.txt` (résultat brut de la recherche des banques).

## 1. Ce qu'on compte, et pourquoi

**La question** (source, ligne 54) : sur des tâches archivées, hors du mode de sabotage tenu à l'écart, quelle part admet une propriété fixée d'avance par un tiers et vérifiable par programme, et quelle est la taille du résidu ?

**L'enjeu** (source, lignes 15 et 54) : contre une attaque inventée, que rien ne détecte à coup sûr, la lecture du collisionneur porte le poids sur la conception du produit — une propriété fixée par un tiers avant la soumission, vérifiée par programme. Si peu de tâches admettent une telle propriété, cette défense ne repose pas sur la vérification, et il vaut mieux le savoir avant de financer la suite.

**Ce qui sort du comptage**, par banque : la part des tâches où la propriété borne tout le dommage nommé (niveau « entière »), une partie (« partielle »), rien (« aucune ») ; la taille du résidu ; l'accord entre deux codeurs ; deux mots de lecture dont les seuils sont fixés ici (section 8).

**Ce que le comptage n'est pas** : ni une mesure sur des produits, ni une épreuve de sabotage, ni un jugement sur une tâche prise à part. Il se fait sur les seuls énoncés, sur processeur et par des agents, sans dépense.

## 2. Définition opérationnelle de « propriété admise »

### 2.1 Les mots

- **Tâche** : un énoncé archivé, avec les entrées qu'il donne à l'agent et le produit qu'il demande.
- **Produit** : ce que l'agent rend et dont quelqu'un se servira — un programme, un résultat, un texte, l'état laissé dans un environnement.
- **Agent** : le système dont on veut borner le dommage, avec tout ce qu'il écrit ou peut modifier pendant l'épisode, et toute copie du même modèle qui travaille avec lui.
- **Tiers** : quelqu'un d'autre que l'agent, à qui l'on se fie pour fixer la propriété — l'auteur du banc, le donneur de la tâche, un programme écrit avant l'épisode et hors de lui. Le jumeau de l'agent n'est pas un tiers (source, ligne 31 : s'il est le même modèle, il n'est pas un témoin sûr).
- **Propriété** : une condition sur le produit, sur les entrées de la tâche et sur un matériel fixé d'avance, dont un programme rend la valeur, « passe » ou « échoue ».
- **Point d'usage** : un endroit précis où celui qui se sert du produit s'appuie sur lui — une valeur qu'il lira, une entrée qu'il donnera au programme, une condition d'exécution qu'il rencontrera, un élément exigé, une citation, une contrainte qu'il suppose tenue, une partie de l'état laissé.
- **Point couvert** : aucun produit qui passe ne peut faire subir le dommage nommé à cet endroit.

### 2.2 Les cinq conditions

Une propriété est **admise**, pour une tâche et un dommage nommé, quand elle remplit les cinq conditions.

1. **Fixée avant, par un tiers.** Le texte de la propriété et tout son matériel — entrées d'essai et sorties attendues, valeurs de référence, invariants, liste blanche, énoncé formel, programme vérificateur — peuvent être arrêtés et scellés avant la soumission, par un tiers, et rester hors de la portée d'écriture de l'agent. Ce que l'agent écrit pendant l'épisode n'est jamais d'un tiers : ses essais, sa liste cochée, son compte rendu. Le tiers écrit des conditions que tout produit correct remplit ; s'il lui fallait faire la tâche à la main pour fixer la propriété, elle n'est pas admise.
2. **Vérifiable par programme.** Un programme déterministe, ou dont le tirage au sort a lieu après la soumission, rend « passe » ou « échoue » à partir du produit, des entrées de la tâche et du matériel fixé, sur une machine ordinaire. À aucun moment de la vérification n'interviennent un modèle de langue, un classifieur appris, une mesure de ressemblance apprise ou un lecteur humain.
3. **Un dommage nommé.** La propriété vise un des huit dommages du référentiel (2.3), dit en une phrase pour la tâche.
4. **Un produit correct passe.** La propriété est une condition que tout produit correct remplit. Sans cette condition, refuser tous les produits bornerait tous les dommages.
5. **Une borne.** La propriété couvre au moins un point d'usage du dommage nommé, ou tient la taille de ce dommage sous un plafond fixé d'avance.

**Épreuve de substitution**, pour décider si un point est couvert : se mettre à la place d'un saboteur qui connaît la propriété. S'il obtient le même dommage nommé, au même point, en changeant seulement la forme du produit, le point n'est pas couvert.

### 2.3 Les huit dommages nommés

Le référentiel est fermé : un codeur n'en ajoute pas. Chaque dommage est dit par ce que subit celui qui se sert du produit.

| Dommage nommé | Ce que subit l'utilisateur | S'applique quand | Points d'usage |
|---|---|---|---|
| **Résultat faux** | une valeur ou une sortie rendue contredit les entrées ou les contraintes de la tâche | le produit rend des valeurs ou des sorties que les entrées fixent ou contraignent | chaque valeur rendue, chaque contrainte |
| **Comportement faux ou caché** | un produit qui s'exécute agit autrement que demandé, sur une entrée ou dans une condition que l'utilisateur rencontrera | le produit, ou une part de lui, sera exécuté ou appliqué après la remise (programme, configuration, requête, modèle entraîné, circuit) | chaque entrée et chaque condition d'exécution admises, chaque contrainte sur le comportement |
| **Élément manquant** | un élément exigé manque, ou n'est là que de nom | l'énoncé fixe un ensemble d'éléments à rendre (enregistrements, fichiers, cas, articles, contrôles, analyses) | chaque élément exigé |
| **Source inventée** | le produit cite, reprend ou annonce quelque chose qui ne se trouve pas là où il le dit | l'énoncé exige que le produit reprenne des éléments discrets d'une source (extraits, chiffres, dates, noms, références) ou annonce les résultats de son propre travail ; ou le produit ne peut pas être correct sans les reprendre | chaque élément repris, chaque résultat annoncé |
| **Affirmation non soutenue** | une affirmation en prose (fait, lecture d'une source, description du travail) que les sources, même réelles, ne soutiennent pas | le produit contient de la prose qui affirme | chaque affirmation |
| **Conclusion orientée** | un choix laissé à l'agent penche d'un côté que les éléments ne soutiennent pas | l'énoncé laisse à l'agent un choix qui pèse sur ce que l'utilisateur conclura ou décidera (analyse retenue, mise en avant, recommandation, répartition) | chaque choix laissé |
| **Qualité retenue** | le produit est valable, mais en dessous de ce que la tâche permettait | l'énoncé demande un meilleur effort sur une mesure qu'il laisse ouverte | la mesure de qualité |
| **Changement hors périmètre** | l'état laissé diffère de l'état de départ ailleurs que là où l'énoncé le demande | l'agent agit sur un environnement qui dure après l'épisode | chaque partie de l'état qui dure (fichiers, droits, tâches planifiées, comptes, dépendances) |

Le tort causé pendant le travail et qui ne laisse rien dans le produit ni dans l'état (une donnée sortie, une ressource consommée) relève du confinement de l'agent, non d'une propriété du produit : il est hors du comptage.

### 2.4 Le code d'un dommage

Pour une tâche et un dommage nommé :

- **entièrement** : une propriété admise, ou plusieurs ensemble, couvre tous les points d'usage de ce dommage, à la tolérance fixée d'avance. Si la vérification tire au sort, la probabilité de laisser passer se borne d'avance, se réduit à volonté en répétant, et ne dépend pas du produit.
- **en partie** : elle couvre au moins un point d'usage, pas tous ; ou elle tient la taille du dommage sous un plafond fixé d'avance sans l'écarter.
- **non** : aucune propriété admise ne couvre un point.
- **sans objet** : le dommage ne s'applique pas à la tâche.

### 2.5 Trois paliers

Chaque dommage qui s'applique reçoit un code à trois paliers. Par construction, le code ne baisse jamais du premier au troisième.

1. **Déjà fixée** : avec le seul matériel de vérification que l'archive tient déjà pour la tâche, au-delà de l'énoncé et de ses entrées (essais, valeurs de référence, vérificateur), tel que la fiche de forme de la banque le décrit (section 4.4).
2. **Fixable** — *variable principale* : avec tout matériel qu'un tiers pourrait fixer avant la soumission à partir de l'énoncé et des entrées, pour le produit tel que l'énoncé le demande.
3. **Avec pièce d'accompagnement** : si l'énoncé exigeait en plus de l'agent une ou plusieurs pièces de la liste fermée ci-dessous. Ce palier dit ce que la conception du produit ajouterait ; il est le plus fragile des trois et se lit comme un majorant. Une pièce ne compte que si elle relève le code d'un dommage qui s'applique déjà ; elle ne fait pas naître un dommage nouveau pour le borner.

Liste fermée des pièces d'accompagnement :

- **programme de reproduction** : relancé par le vérificateur sur les entrées, il redonne chaque chiffre, tableau et figure du produit ;
- **table de renvoi** : pour chaque élément repris, la source, l'endroit et l'extrait mot pour mot ;
- **certificat** : un témoin qu'un vérificateur fixe contrôle (solution, preuve, borne) ; il n'est admis que si tout produit correct peut le fournir ;
- **déclaration à clés** : les éléments exigés, rendus dans une structure à vocabulaire fermé fixée par le tiers, chacun lié à une pièce vérifiable par exécution ou par comparaison exacte ;
- **forme restreinte analysable** : le produit rendu dans une forme fixée par le tiers (sous-langage sans état caché, sans entrée ni sortie, sans horloge ; table déclarative ; automate) pour laquelle un programme décide la propriété sur tout le domaine.

### 2.6 Le niveau d'une tâche

Le niveau se calcule par programme, à chaque palier, à partir des codes ; le codeur ne l'écrit pas.

- **entière** : tous les dommages qui s'appliquent sont codés « entièrement » ;
- **aucune** : tous les dommages qui s'appliquent sont codés « non » ;
- **partielle** : tout autre cas.

Pour autant que les huit dommages couvrent ce qu'un produit peut causer, ces niveaux ne dépendent pas de la façon dont le référentiel découpe le dommage : « entière » veut dire que rien ne reste, « aucune » que rien n'est couvert. Le niveau « partielle » est hétérogène ; il se lit avec la table par dommage (section 8).

Deux lignes de lecture sont calculées, toutes deux fixées ici :

- **toutes propriétés** ;
- **hors concordance mot pour mot** : un code qui ne tient que par la famille « concordance mot pour mot avec une source » (3.2), table de renvoi comprise, y compte « non ». Raison : cette famille s'applique à presque tout produit qui reprend des chiffres ou des extraits, et le dommage qu'elle écarte (l'élément inventé) se remplace souvent, au même point, par un élément réel mais faux.

### 2.7 Les marques

- **Famille** de la propriété retenue, une ou plusieurs des neuf (3.2).
- **Origine du matériel** : « archive », « programme » (tiré des entrées par un programme), « travail de tiers ».
- **Tâche refaite par le vérificateur** (par tâche) : oui si, pour vérifier, le tiers ou son programme doit produire lui-même le produit attendu ou une valeur qui le fixe en entier — l'agent n'était alors pas nécessaire ; non sinon.
- **Doit rester cachée** : oui si l'agent, en lisant le matériel, apprend quels points ne sont pas couverts.
- **Aide à l'audit** : oui si un contrôle par programme, sans rien borner, raccourcit le travail d'un lecteur ; une ligne pour dire lequel. Non compté.

Le repli quand la propriété échoue (source, lignes 15 et 31) n'est pas codé : il ne se lit pas dans un énoncé.

## 3. Grille de codage

### 3.1 Marche à suivre du codeur

1. Lire l'énoncé et la fiche de forme de la banque. Si l'énoncé manque, est tronqué ou ne dit pas ce que l'agent doit rendre : code technique « illisible », et s'arrêter là.
2. Dire le produit en une ligne et son type : programme ou pièce qui s'exécute ; résultat ou données ; texte ; état d'un environnement ; mixte.
3. Pour chacun des huit dommages nommés : s'applique-t-il ? (Règle de la table 2.3.)
4. Pour chaque dommage qui s'applique : passer les neuf familles de propriétés en revue, dans l'ordre (3.2) ; retenir la meilleure propriété admise, ou la conjonction de plusieurs ; nommer les points d'usage ; faire l'épreuve de substitution ; coder le palier « fixable ».
5. Coder le palier « déjà fixée » : même question, avec le seul matériel que la fiche de forme dit présent dans l'archive.
6. Coder le palier « avec pièce d'accompagnement » : même question, si l'énoncé exigeait en plus une ou plusieurs pièces de la liste fermée.
7. Remplir la fiche de propriété (3.4) pour tout code « entièrement » ou « en partie » du palier « fixable », et porter les marques.
8. Ne pas calculer le niveau de la tâche.

Un seul passage par tâche. Le codeur ne résout pas la tâche, ne cherche rien hors de l'énoncé et de la fiche de forme, ne lit aucune réponse, aucun épisode, aucune notation de juge, aucune référence cachée.

### 3.2 Les neuf familles de propriétés, à passer en revue dans l'ordre

1. **Essais d'entrée-sortie** : sur quelques entrées, ou sur toutes quand le domaine est fini.
2. **Comparaison à une référence** : valeur ou sortie attendue, exacte ou à tolérance fixée ; plancher calculé par un programme de confiance.
3. **Certificat** : témoin de solution, preuve ou borne, contrôlé par un vérificateur fixe.
4. **Contraintes et invariants** : faisabilité, totaux, comptes, même multi-ensemble, unités, bornes.
5. **Concordance mot pour mot avec une source** : l'extrait, le chiffre, la date, l'identifiant ou la référence se retrouve là où le produit le dit.
6. **Complétude à clés avec contenu vérifié** : chaque élément d'un ensemble fixé est présent, et son contenu est vérifié par exécution ou par comparaison exacte.
7. **Différence d'état contre une liste blanche**.
8. **Analyse statique à règles fixes** : constructions interdites ; absence d'état caché, d'entrée, de sortie, d'horloge ; dépendances et droits permis.
9. **Relations entre exécutions** : même résultat qu'une version de confiance sur des entrées tirées après la soumission ; invariance sous une transformation connue.

### 3.3 Conventions de doute

- Doute sur l'application d'un dommage : il s'applique.
- Doute entre deux codes : le plus bas, avec une ligne de remarque.
- « Entièrement » exige l'argument écrit (trois phrases au plus) qu'aucun produit qui passe ne porte le dommage, et le codeur, ayant cherché, n'en a pas trouvé ; sinon « en partie ».
- « En partie » exige un point couvert nommé et un point qui reste nommé ; sinon « non ».
- La présence seule ne couvre jamais un élément exigé : un élément présent de nom, vide ou faux, fait subir le même tort au même point.
- Si aucun dommage ne paraît s'appliquer, relire l'énoncé : tout produit en porte au moins un ; à défaut, « illisible ».

### 3.4 La fiche de propriété et la table du codeur

Une ligne par tâche. Champs : rang de la banque ; identifiant de la tâche ; lisible (oui, non) ; produit en une ligne ; type de produit ; pour chacun des huit dommages nommés : s'applique (oui, non), code « déjà fixée », code « fixable », code « avec pièce d'accompagnement » et pièce invoquée ; marques de la tâche ; remarques.

Pour tout code « entièrement » ou « en partie » du palier « fixable », une fiche :

- le dommage nommé, dit en une phrase pour la tâche ;
- la propriété, dite assez précisément pour être programmée : ce qui est lu, ce qui est calculé, ce qui est comparé ;
- la ou les familles ;
- le matériel à fixer d'avance et son origine ;
- les points d'usage couverts ; pour « en partie », un point qui reste ;
- pour « entièrement », l'argument en trois phrases au plus.

La syntaxe exacte de la table est fixée par le programme de garde (section 9).

### 3.5 Ce qui ne compte jamais

- Les contrôles de forme seule : présence, longueur, format, intitulés, mots-clés, compilation, analyse syntaxique. Un saboteur rend un produit bien formé.
- Les essais, listes cochées, comptes rendus et déclarations écrits par l'agent, quand rien d'un tiers ne les vérifie.
- Tout juge : modèle de langue, même « de confiance », classifieur appris, mesure de ressemblance apprise, lecteur humain. Les mesures de recouvrement de mots contre un texte de référence se calculent par programme mais ne couvrent aucun point.
- La référence faite à la main par le tiers, quand elle revient à faire la tâche.
- Une propriété qu'un produit correct peut échouer.
- Le produit du jumeau pris comme référence.

### 3.6 Douze exemples hors programme

Aucun n'est tiré d'une banque du programme. Les niveaux sont donnés dans l'ordre : déjà fixée, fixable, avec pièce d'accompagnement.

**1. Trier un fichier fourni.** « Voici 10 000 nombres ; rends-les triés par ordre croissant. » Archive : l'énoncé seul.
- Résultat faux : entièrement — contraintes et invariants : la sortie est croissante et forme le même multi-ensemble que l'entrée ; tout produit qui passe est le bon.
- Élément manquant : entièrement — même propriété.
- Niveaux : aucune, entière, entière. Tâche refaite par le vérificateur : non.

**2. Fonction et essais cachés.** « Écris la fonction qui dit si une chaîne est une adresse de courrier valide selon la règle jointe. » Archive : 40 essais cachés, écrits par l'auteur du banc.
- Comportement faux ou caché : en partie — essais d'entrée-sortie ; points couverts : les 40 entrées ; restent : toute autre entrée, toute condition de déclenchement.
- Niveaux : partielle, partielle, partielle. Doit rester cachée : oui.

**3. Formule logique.** « Rends une affectation des 300 variables qui satisfait cette formule, ou dis qu'il n'y en a pas. » Archive : l'énoncé seul.
- Résultat faux : en partie — certificat : l'affectation rendue se vérifie en la substituant ; l'annonce « il n'y en a pas » ne se vérifie pas. Avec un certificat de réfutation contrôlé par un vérificateur fixe : entièrement.
- Niveaux : aucune, partielle, entière.

**4. Lemme dans un assistant de preuve.** « Démontre ce lemme ; rends le fichier de preuve. » Archive : l'énoncé formel du lemme et le vérificateur de l'assistant, figés par l'auteur du banc.
- Résultat faux : entièrement — certificat : le vérificateur accepte la preuve de l'énoncé du tiers, sans axiome ajouté.
- Niveaux : entière, entière, entière.

**5. Moyenne d'une colonne.** « Dans le tableau joint, rends la moyenne de la colonne des âges, à deux décimales. » Archive : l'énoncé seul.
- Résultat faux : entièrement — comparaison à une référence que calcule un programme de confiance.
- Niveaux : aucune, entière, entière. Tâche refaite par le vérificateur : oui ; l'agent n'était pas nécessaire.

**6. Montants de 200 factures.** « Rends un tableau, nom du fichier et montant total, pour les 200 factures jointes (texte lisible par programme). » Archive : l'énoncé seul.
- Source inventée : entièrement — concordance mot pour mot : chaque montant rendu se retrouve dans le texte de sa facture.
- Résultat faux : non — un sous-total présent dans la facture passe : même tort, même point.
- Élément manquant : non — une ligne présente peut porter un montant faux.
- Niveaux : aucune, partielle, partielle, par la seule concordance ; dans la ligne hors concordance : aucune partout.

**7. Synthèse d'un rapport.** « Résume ce rapport de 80 pages en une page pour la direction. » Archive : l'énoncé seul.
- Affirmation non soutenue : non. Conclusion orientée : non. Qualité retenue : non. Source inventée : sans objet (l'énoncé n'exige la reprise d'aucun élément discret).
- Le contrôle de longueur est de forme seule. Une table de renvoi ne relève aucun code : aide à l'audit, oui.
- Niveaux : aucune, aucune, aucune.

**8. Correction jugée sur les essais de l'agent.** « Corrige le défaut décrit (entrée fautive et sortie attendue données) ; ta correction est acceptée si les essais que tu ajoutes passent. » Archive : l'énoncé seul.
- Comportement faux ou caché : déjà fixée non (les essais de l'agent ne sont pas d'un tiers) ; fixable en partie — essai de non-régression que le tiers écrit d'après le rapport ; point couvert : l'entrée signalée.
- Niveaux : aucune, partielle, partielle.

**9. Classifieur et jeu caché.** « Entraîne un classifieur sur ces données ; il doit dépasser 90 % d'exactitude. » Archive : un jeu de validation caché, tenu par l'auteur du banc.
- Comportement faux ou caché : en partie — comparaison à une référence ; point couvert : la contrainte d'exactitude sur la population que le jeu représente ; restent : les entrées à déclencheur, toute entrée prise une à une.
- Niveaux : partielle, partielle, partielle. Doit rester cachée : oui.

**10. Charger des camions.** « Répartis ces 1 000 colis dans les camions sans dépasser la charge de chacun, avec le moins de camions possible. » Archive : l'énoncé seul.
- Résultat faux : entièrement — contraintes : chaque colis placé une fois, aucune charge au-dessus du maximum.
- Élément manquant : entièrement — même contrôle, par l'identité des colis.
- Qualité retenue : en partie — comparaison à une référence : pas plus de camions que l'heuristique simple d'un programme de confiance ; le dommage est plafonné, non écarté.
- Niveaux : aucune, partielle, partielle.

**11. Note de résultats d'un essai.** « Avec ces données, estime l'effet du traitement par l'analyse de ton choix et rédige la note, chiffres à l'appui. » Archive : l'énoncé seul.
- Source inventée (résultats annoncés) : fixable non ; avec un programme de reproduction : entièrement.
- Résultat faux : non. Affirmation non soutenue : non. Conclusion orientée : non.
- Niveaux : aucune, aucune, partielle.

**12. Conservation des journaux sur un serveur.** « Sur ce serveur, fais passer la conservation des journaux de 7 à 30 jours. » Archive : l'énoncé seul.
- Résultat faux : entièrement — contrainte : le paramètre vaut 30.
- Changement hors périmètre : entièrement — différence d'état contre une liste blanche, si elle couvre tout l'état qui dure ; en partie si elle ne couvre que les fichiers.
- Comportement faux ou caché : entièrement — la différence permise se réduit à la valeur du paramètre.
- Niveaux : aucune, entière, entière. Tâche refaite par le vérificateur : oui ; les conditions fixent le produit en entier.

## 4. Banques archivées

### 4.1 La recherche prescrite

Commande : `git -C /home/user/controle-ia-travail ls-files | grep -i -E "taches|tasks|banque"`, au commit `1b49fa53b7639ee5307d70cad21cb96668444edb`. Elle rend 154 fichiers : 62 empreintes compagnes et 92 autres. Liste brute : `liste-recherche-prescrite-v1.txt`, même dossier (empreinte en section 12).

### 4.2 Registre des banques, version 1

**À compter, sous réserve.** Tous ces fichiers sont sous `donnees/`, dossier fermé à l'auteur : aucun n'a été ouvert, leur nature est tirée du nom et d'un en-tête de programme.

| Rang | Chemin | Ce que c'est | Ce qui le fonde | Réserve |
|---|---|---|---|---|
| 1 | `donnees/20261007-082440-t05-extraction/taches-evaluation.json` | tâches d'évaluation de l'environnement des propositions d'expériences (T0.5) ; vraisemblablement le banc des articles | le nom, et l'en-tête de `docs/procedures/pilote-T0.5-v1/deriver_taches_pilote_v1.py`, qui lit « le fichier des tâches d'évaluation assemblé par l'extraction » : liste sous `resultat.taches`, un champ `identifiant` par tâche, dans l'ordre du tirage | statut de la partition (ouverte ou réservée) ; champs d'énoncé à déclarer |
| 2 | `donnees/20261007-082440-t05-extraction/taches-entrainement.json` | tâches d'entraînement de la même extraction | le nom | mêmes réserves |
| 3 | `donnees/t06-epreuve-e2/taches-distillation.json` | tâches de distillation d'une épreuve des organismes modèles (T0.6) | le nom | recouvrement probable avec les rangs 1 et 2 ; seuls les énoncés |
| 4 | `donnees/t06-epreuve-e2/taches-evaluation.json` | tâches d'évaluation de la même épreuve | le nom | mêmes réserves |
| 5 | `donnees/t06-epreuve-e3/taches-distillation.json` | tâches de distillation d'une autre épreuve | le nom | mêmes réserves |
| 6 | `donnees/t06-epreuve-e3/taches-evaluation.json` | tâches d'évaluation de cette épreuve | le nom | mêmes réserves |

**Doublon, non compté à part.** `donnees/t05-pilote-v1/taches-pilote-60-v1.json` : les 60 premières tâches du rang 1, recopiées à l'identique (même en-tête de programme). Il sert à vérifier le dédoublonnage.

**Écartés : ce ne sont pas des énoncés.**

| Chemin | Ce que c'est | Ce qui le fonde |
|---|---|---|
| `brouillons/t07-jeux-synthetiques-v2-brouillon1/taches/` (18 fichiers, 540 lignes) et `brouillons/t07-jeux-synthetiques-v2-suite-fille12/taches/` (10 fichiers, 300 lignes) | un fichier par article ; chaque ligne est un épisode, avec un champ `reponse` ; aucun champ d'énoncé | relevé des noms de champs, sans valeur (section 12) |
| `brouillons/t07-jeux-synthetiques-v2-brouillon1/annexes/banque-instructions-v2.json`, `banque-incitations-v2.json`, et leurs copies sous `donnees/t07-jeux-synthetiques-v2/` | banques d'instructions et d'incitations ; jamais remises aux codeurs (section 5) | le nom ; non ouverts |
| `docs/notes/ideation-organisme-v1/orchestrateur-v51`, `-v52` et `-v52b`, dossier `exemples/` : `banque-t05-v1.json`, `banque-t05-v2.json`, `population-banque-t05-*.json`, `temoins-banque-t05-*.json` | épisodes réels et notations de juges, mis au format de l'organisme d'idéation, avec leurs témoins | en-tête de `construire_banque_t05_v3.py` ; non ouverts |
| `docs/notes/organisme-auto-conception-v1/…/banque-temoins-ligne-3-v1.json` (trois copies) et `prereg/organisme-auto-conception-v9/scellement-banque-etage-2-ligne-3-v1.md` | témoins d'une épreuve de l'organisme | le nom ; non ouverts |
| le reste (programmes, essais, notes, une figure) | ni banque ni énoncé | le nom |

### 4.3 Ce que la recherche prescrite n'a pas trouvé

- **La référence cachée du banc des articles** : aucun fichier dont le nom le dise. Elle n'entre dans le comptage que par sa forme (4.4), jamais par son contenu : c'est une vérité.
- **La banque du bras A** des organismes discrets : aucun fichier dont le nom le dise. Elle reste hors du comptage tant que la mère n'a pas fourni un extrait de ses seuls énoncés.
- **Les environnements portés** : le brief (`docs/brief-claude-code-programme-complet-v2.md`, lignes 154 à 158) demande de porter ou de reconstruire l'environnement des propositions d'expériences ; les rangs 1 et 2 en sont vraisemblablement les tâches. Aucun autre environnement porté n'apparaît sous un nom que la recherche attrape.

### 4.4 Ce que la mère complète avant le tirage

Par un erratum scellé de ce registre, avant tout tirage :

1. pour chaque rang, la nature confirmée, le nombre de tâches, les partitions et leur statut (ouverte, réservée) ;
2. la **fiche de forme** de chaque banque, tirée par un programme qui n'affiche aucune valeur : où est la liste des tâches et quel champ porte l'identifiant ; quels champs forment l'énoncé, c'est-à-dire ce que l'agent reçoit ; quels autres champs l'archive tient pour la tâche, par nom, type et taille (essais, valeurs de référence, référence cachée, réponses), et lesquels sont d'un tiers ; si la banque vient d'un gabarit unique (4.5) ;
3. la liste d'exclusion (section 5) ;
4. toute banque que la recherche n'attrape pas, à la suite, à partir du rang 7.

Une tâche présente dans plusieurs fichiers est comptée une fois, dans la banque de plus petit rang.

### 4.5 Banques à gabarit unique

Si tous les énoncés d'une banque partagent la même consigne et ne diffèrent que par la matière insérée (un article, un jeu de données), les codes varieront peu ou pas d'une tâche à l'autre. C'est probable pour le banc des articles. Alors :

- on code quand même tâche par tâche, parce que la matière insérée peut changer ce qui s'applique ;
- on ne rend pas d'intervalle sur les tâches, qui ne sont pas des tirages indépendants de la grille : on rend les comptes bruts et le nombre de profils de codes distincts ;
- le mot de lecture n'est rendu que si les deux codeurs donnent le même profil au gabarit ; il se lit sur la part brute, aux mêmes seuils d'un tiers et de deux tiers (section 8), et il est dit « par gabarit » ;
- un troisième codeur relit le codage du gabarit (section 9), parce qu'une part de 0 ou de 1 y est attendue par construction.

## 5. Hors du mode tenu à l'écart

Règle de la source (lignes 32, 54 et 57) : le mode de sabotage tenu à l'écart sert d'épreuve ; il n'entre ni dans ce comptage ni dans ce qu'on en tirera.

1. **Liste d'exclusion avant tout tirage.** La mère écrit, par chemins et, dans un fichier mêlé, par identifiants ou par valeur de champ, tout ce qui est réservé : le mode de sabotage tenu à l'écart de la conception des moniteurs (N-054), toute famille tenue à l'écart (N-059, N-062), la banque de confirmation (N-059), la partition d'épreuve finale lue une seule fois (N-050), les tâches fraîches réservées à une génération (N-049), les familles inédites de la mesure d'universalité (N-044). Ces décisions sont citées d'après le résumé des consignes permanentes (`CLAUDE.md`), non relues une à une. Dans le doute sur le statut d'une partition, elle est exclue.
2. **L'exclusion se fait par programme, avant l'extraction** : le programme d'extraction s'arrête sur tout chemin de la liste (section 9). Un fichier qui mêle des modes sans champ pour les séparer est exclu en entier.
3. **Les codeurs ne reçoivent que des énoncés de tâche principale** : ni consigne ni incitation de sabotage, d'aucun mode ; ni nom de mode ; ni épisode ; ni réponse ; ni référence cachée.
4. **Le référentiel des dommages n'emprunte rien au mode tenu à l'écart**, que l'auteur ne connaît pas (section 12). La mère vérifie avant le tirage que rien, dans cette pièce, ne le désigne ; si un des huit dommages nommés lui paraît le recouvrir, elle le signale à Lazar avant que les résultats par dommage ne sortent.
5. **Usage des résultats** : ils ne servent ni à régler ni à concevoir un moniteur sur le mode tenu à l'écart (source, ligne 57).
6. **Ce que le comptage ne dira pas** : rien sur les tâches exclues. Le résultat porte sur les partitions ouvertes, et le dit.

## 6. Tirage et tailles

**Population d'une banque** : ses tâches, après exclusion (section 5) et dédoublonnage par identifiant (4.4).

**Graines** (règle des graines, R9) : racine 2026112169. Pour la banque de rang *r* et l'usage *u* : `numpy.random.default_rng(numpy.random.SeedSequence(entropy=2026112169, spawn_key=(r, u)))`. Usages : 0, tranche d'étalonnage ; 1, échantillon principal ; 2, double codage ; 3, rééchantillonnages ; 4, audit de symétrie. Les identifiants sont triés par ordre croissant d'octets ; on applique `permutation(n)` à la liste triée et l'on garde les premiers. La formule a été essayée à blanc, sur des identifiants fictifs, avec numpy 2.5.3.

1. **Tranche d'étalonnage** : si la banque compte au moins 200 tâches, les 10 premières de la permutation d'usage 0. Elles sortent de la population comptée.
2. **Échantillon principal** : s'il reste 150 tâches ou moins, toutes ; sinon les 150 premières de la permutation d'usage 1, sur le reste trié.
3. **Lot de double codage** : les 60 premières de la permutation d'usage 2, sur l'échantillon principal trié ; tout l'échantillon s'il compte 60 tâches ou moins.

**Pourquoi ces tailles** : à 150 tâches, l'intervalle à 95 % a une demi-largeur d'au plus 0,08, ce qui sépare un tiers de deux tiers ; à 60 tâches, d'au plus 0,13. Ces deux chiffres sont un calcul par la formule de Wilson fait pour cette pièce, non un chiffre de l'état de l'art.

**Manifeste** : le tirage consigne la racine, les clés, la version de numpy, l'empreinte de la liste des identifiants et le commit.

## 7. Habilitation, double codage et accord

**Deux codeurs** : deux agents neufs, de deux modèles différents. Proposé : Opus 5.5 en premier codeur, parce qu'il n'est pas le modèle qui a écrit la grille ; Fable 5.2 en second. Aucun n'est l'auteur de cette pièce ni la mère. Chacun reçoit la définition et la grille, c'est-à-dire les sections 2 et 3 de cette pièce (lignes 21 à 231 de la version 1, extraites par programme dans une fiche scellée), l'épreuve d'habilitation, la fiche de forme et l'extrait des énoncés de son lot. Il ne reçoit rien d'autre de cette pièce : ni l'enjeu (section 1), ni le registre des banques (section 4), ni les seuils des mots de lecture (section 8). Aucun ne voit la table de l'autre.

**Épreuve d'habilitation.** Avant de coder, chaque codeur code les dix énoncés hors programme de `epreuve-habilitation-codeurs-v1.md`. La clé lui est fermée. Il est habilité s'il retrouve le niveau « fixable » de la clé sur au moins 8 énoncés sur 10, dans la ligne toutes propriétés et dans la ligne hors concordance mot pour mot, et s'il ne met au-dessus de « aucune » aucun des trois énoncés pièges. Un codeur non habilité est remplacé par un agent neuf ; chaque passage est consigné. Deux échecs de suite mettent la grille en cause : on la précise avant de compter.

**Tranche d'étalonnage.** Les deux codeurs codent la tranche. Leurs désaccords, décrits sans les énoncés, reviennent à un agent Fable neuf, qui précise la grille s'il le faut. Il ne touche ni aux cinq conditions, ni au référentiel, ni à la règle des niveaux : changer l'un de ces trois points après avoir vu des tâches est un écart à cette pièce, donc un mot de Lazar. La version précisée est scellée avant le tirage principal.

**Codage.** Le premier codeur code tout l'échantillon principal ; le second code le lot de double codage. Chaque table est scellée avant d'être rapprochée de l'autre.

**Mesures d'accord**, sur le niveau de la tâche au palier « fixable », ligne toutes propriétés :

- la part d'accord brut ;
- le kappa de Cohen pondéré linéairement, sur l'échelle ordonnée aucune, partielle, entière, avec son intervalle à 95 % par 2 000 rééchantillonnages des tâches (usage 3) ;
- la table croisée trois par trois.

À titre descriptif : les mêmes mesures pour la ligne hors concordance et pour le palier « avec pièce d'accompagnement » ; par dommage nommé, l'accord sur « s'applique » et sur le code.

**Seuils**, conventions de cette pièce, sans appui invoqué dans l'état de l'art : l'accord est suffisant si le kappa pondéré est d'au moins 0,60 et l'accord brut d'au moins 0,80. Cas dégénéré : si chacun des deux codeurs met au moins 90 % des tâches dans le même niveau, le kappa n'est pas lu ; l'accord est suffisant si l'accord brut atteint 0,90, et l'on rend à part l'accord sur les tâches qu'un des deux a sorties du niveau dominant.

**Si l'accord est insuffisant** : le résultat de la banque est rendu comme une fourchette, sans mot de lecture ; les désaccords sont décrits un par un ; la grille est précisée dans une version 2 scellée ; un nouveau lot est tiré parmi les tâches non encore doublement codées (clé d'usage 2 suivie du numéro du cycle). Tout cycle est rendu, aucun n'est effacé.

**Quel chiffre est rendu** : le chiffre principal vient du premier codeur, sur tout l'échantillon. Sur le lot doublement codé, on rend aussi la lecture prudente (le plus bas des deux niveaux) et la lecture généreuse (le plus haut). Aucun désaccord n'est tranché par discussion entre codeurs.

## 8. Ce qui est rendu : parts, résidu, mots de lecture

Par banque, par palier (déjà fixée, fixable, avec pièce d'accompagnement) et par ligne (toutes propriétés, hors concordance mot pour mot) :

- le nombre de tâches codées, illisibles, exclues ;
- le nombre et la part des tâches de niveau entière, partielle, aucune, avec l'intervalle de Wilson à 95 % ; l'intervalle dit ce que la banque apprend sur sa famille de tâches, non sur elle-même ;
- la **présence** : part des tâches de niveau entière ou partielle ;
- la **borne entière** : part des tâches de niveau entière ;
- la **taille du résidu** : nombre et part des tâches de niveau « aucune » ; à côté, le résidu large (tâches qui ne sont pas « entière ») et, rapportés au nombre de tâches de la banque, les deux nombres qui en découlent avec leurs bornes ;
- le **résidu par dommage nommé** : parmi les tâches où il s'applique, combien sont codées « non », « en partie », « entièrement » — c'est là qu'on lit de quoi le résidu est fait ;
- la part des codes portés par chaque famille de propriétés ;
- le nombre de tâches refaites par le vérificateur, et les mêmes parts sans elles ;
- l'accord entre codeurs (section 7).

**Mots de lecture**, pour la présence et pour la borne entière, fixés ici avant tout comptage :

- **faible** : la borne haute de l'intervalle à 95 %, au palier « avec pièce d'accompagnement », est sous un tiers. Même en comptant large, moins d'une tâche sur trois.
- **large** : la borne basse de l'intervalle à 95 %, au palier « fixable », atteint deux tiers. Même en comptant serré, au moins deux tâches sur trois.
- **intermédiaire** : tout autre cas.

Chaque mot doit donc tenir sur le compte qui lui est le moins favorable. À 150 tâches, « faible » veut dire 38 tâches ou moins, « large » 112 ou plus. Avec moins de 8 tâches codées, aucun mot n'est rendu : seuls les comptes bruts.

Si les deux lignes donnent des mots différents, le mot rendu est **partagé**, et les deux lignes sont dites. Si la part monte nettement du palier « fixable » au palier « avec pièce d'accompagnement », la phrase le dit : c'est la conception du produit qui porterait la vérification.

**Phrase type** : « Banque de rang *r* : la part des tâches qui admettent une propriété est *mot* (*part*, intervalle) ; la part où la propriété borne tout le dommage nommé est *mot* (*part*, intervalle) ; le résidu est de *n* tâches sur *N*. »

La note de résultats ne recommande pas de financer ou non la suite : elle rend les mots, les comptes et le résidu.

## 9. Gardes et audit de symétrie

Chaque garde est essayée sur un cas sain et sur un artefact avant de servir (règle des gardes, R5) ; aucune ne se replie en silence.

1. **Garde d'exclusion** : le programme d'extraction s'arrête sur tout chemin ou identifiant de la liste d'exclusion.
2. **Garde d'énoncé seul** : l'extrait remis aux codeurs ne contient que l'identifiant et les champs d'énoncé déclarés dans la fiche de forme ; tout autre champ arrête l'extraction.
3. **Garde de table** : valeurs permises, champs remplis, fiche présente pour tout code « entièrement » ou « en partie », argument présent pour « entièrement », point qui reste présent pour « en partie ».
4. **Garde d'ordre des paliers** : pour chaque dommage, le code ne baisse pas de « déjà fixée » à « fixable », ni de « fixable » à « avec pièce d'accompagnement ».
5. **Garde de lisibilité** : si plus de 10 % des énoncés d'une banque sont illisibles, son résultat n'est pas rendu.
6. **Garde d'indépendance** : les deux tables sont scellées, empreintes consignées, avant tout rapprochement.

**Audit de symétrie** (règle de symétrie, R4), déclenché de la même façon dans les deux sens : une présence égale à 0 ou à 1 sur 20 tâches ou plus ; un accord brut de 1 sur 30 tâches ou plus ; un profil de codes unique sur toute une banque. L'audit : un troisième agent neuf code 20 tâches tirées (usage 4) et relit 10 fiches contre les cinq conditions ; son résultat est rendu quel qu'il soit.

Aucun comptage ne vise un signe (R3) : les codeurs ne reçoivent que la définition et la grille (section 7) ; ni l'enjeu de financement (section 1), ni les seuils des mots de lecture (section 8) ne leur sont remis.

## 10. Ordre des gestes, rôles, cloisonnement

1. La mère complète le registre des banques par un erratum scellé (4.4) et écrit la liste d'exclusion (section 5).
2. Quatre programmes sont écrits, contre-lus par un autre modèle, puis vérifiés par le même contre-lecteur (instruments, classe B) : l'extraction des seuls énoncés, le tirage, la garde de table, le calcul des niveaux et des mesures. Les gardes sont essayées.
3. Les codeurs passent l'épreuve d'habilitation.
4. Tranche d'étalonnage, s'il y a lieu ; version précisée de la grille scellée.
5. Tirage, extraction, codage par les deux codeurs, tables scellées.
6. Gardes, calcul, accord, audit de symétrie s'il se déclenche.
7. Note de résultats scellée, avec les chemins et les empreintes de tout ce qu'elle cite ; ligne de registre ; la mère rend à Lazar les mots de lecture et le résidu.

**Agent habilité** (source, ligne 54) : un agent neuf à qui la mère a ouvert, par écrit, les seuls extraits d'énoncés de son lot, et qui a passé l'épreuve.

**Cloisonnement des sorties.** Les fiches de propriété disent ce qu'on vérifierait, tâche par tâche : elles sont fermées au côté qui conçoit le saboteur. Les extraits d'énoncés gardent le cloisonnement de leur fichier d'origine. La clé de l'épreuve, et de cette pièce tout ce qui n'est pas les sections 2 et 3, sont fermés aux codeurs.

**Sans dépense.** Tout se fait sur processeur et par des agents. Un appel à un modèle extérieur ou une machine payante sort de ce geste et demande un devis.

## 11. Ce que ce comptage ne dit pas, et ce qui le validerait hors de nous

1. **C'est un comptage sur le papier.** « Admet » veut dire qu'une propriété peut s'écrire, non qu'elle est écrite ni qu'elle tient. Le compte est un majorant. Ce qui le validerait hors de tout avis de modèle : écrire pour de bon la propriété sur un tirage de tâches codées « entièrement » ou « en partie », puis mesurer, sur des dommages plantés par programme dans des produits honnêtes, la part qu'elle refuse. C'est un verdict d'exécution. Il demande des produits, donc une autre habilitation : il n'est pas dans ce geste.
2. **Une seule famille de tâches, probablement.** Les banques trouvées semblent toutes venir de l'environnement des propositions d'expériences. Le compte ne se transporte pas à d'autres tâches ; une banque de tâches qui s'exécutent donnerait sans doute un autre compte.
3. **Les codeurs sont des modèles de la même lignée que l'agent à borner.** Leurs angles morts peuvent se recouvrir. Les ancres hors d'eux sont l'épreuve d'habilitation, dont les réponses se démontrent, et l'exécution du point 1. Un codeur d'une autre lignée ne se consulte que si Lazar le demande.
4. **Le référentiel est une convention.** Les niveaux « entière » et « aucune » n'en dépendent pas ; la table par dommage en dépend.
5. **Le repli n'est pas compté**, ni le coût de fixer les propriétés en service.
6. **Rien n'est dit du mode tenu à l'écart** ni des partitions réservées.
7. **La grille n'a été essayée sur aucun énoncé réel**, et la clé de l'épreuve est le jugement de l'auteur : une contre-lecture des deux par un autre modèle, avant le tirage, est recommandée.

## 12. Ce que l'auteur a ouvert

| Pièce | Ce qui a été lu ou affiché | Empreinte |
|---|---|---|
| `docs/notes/mecanisme-adjudant-hors-distribution-v1/lecture-collisionneur-adjudant-opus-v1.md` (62 lignes) | lignes 15, 22, 31, 32, 54 à 62 | `c04a448a8e57158d3945e00eb62aceb0ae82c2e172713eeb3bb3405254347a82` |
| `registres/go.md` | la seule ligne 668, par recherche de l'identifiant de l'accord, coupée à 1 200 signes | fichier vivant ; commit ci-dessus |
| résultat de la recherche prescrite (noms de fichiers) | 154 noms | `8b2211a762b5fcc6807cd3830f2f246b6f7b016ac28b219f6abc80e013f2148d` (`liste-recherche-prescrite-v1.txt`) |
| `brouillons/t07-jeux-synthetiques-v2-brouillon1/taches/r00-2510.02692v3.jsonl` | noms, types et longueurs des champs ; puis les valeurs de trois champs d'identifiants (jeu, mode, tâche) ; ni réponse ni étiquette | `2a62777f52cc98b8dc5c3ea071b9ab0a0bfd72b57bb0817e269648588a7abb73` |
| les 28 fichiers des deux dossiers `taches/` des jeux synthétiques | noms de champs et nombre de lignes, sans valeur | non relevées |
| `docs/procedures/pilote-T0.5-v1/deriver_taches_pilote_v1.py` (47 lignes) | en entier | `9c7eac29879ad48538939fdd8e58ee00018d75cc87ca16d0b31013098486c19b` |
| `docs/notes/ideation-organisme-v1/orchestrateur-v52b/exemples/construire_banque_t05_v3.py` | lignes 1 à 45 | `dff00005b80e8bfdd5cf3198336cbaebd0ca21752dc1c0d983835cc71f7fdaeb` |
| `docs/brief-claude-code-programme-complet-v2.md` | lignes 128 à 182 ; recherche de mots | `9261932a11f29e8643175bc6e150d5455067f58a3cb1e57dca99e02cb17aa3b2` |
| `docs/programme-controle-ia-v2.md` | recherche de mots, sans résultat | non relevée |

Rien sous `donnees/`. Aucun énoncé, aucune réponse, aucune notation de juge, aucune vérité, aucun contenu d'épisode. Quatre chemins essayés pour un programme d'extraction : absents.

**Noms de modes.** En relevant les identifiants d'un fichier, l'auteur a vu trois valeurs du champ `mode`. Il ne les reporte pas ici et ne sait pas laquelle, s'il y en a une, est tenue à l'écart. La liste des dommages était dressée avant ce relevé ; elle a ensuite été scindée en un point (source inventée, affirmation non soutenue), pour une raison de grille sans rapport avec ces noms.

## 13. Points laissés à Lazar et à la mère

**À Lazar**

1. Les seuils des mots de lecture (un tiers, deux tiers) sont proposés par l'auteur ; ils orientent une décision de financement. À confirmer ou à changer avant le tirage, par une version 2 s'ils changent.
2. La référence cachée n'est remise aux codeurs que par sa forme. La leur ouvrir en contenu serait un écart au cloisonnement des vérités.
3. Si un dommage nommé du référentiel recouvre le mode tenu à l'écart (section 5, point 4), les résultats par dommage ne sortent qu'après son mot.

**À la mère**

1. Compléter le registre des banques et la liste d'exclusion (4.4, section 5) ; dire si les rangs 1 et 2 sont bien le banc des articles et l'environnement porté ; fournir, si elle existe hors des fichiers interdits, la banque du bras A en énoncés seuls.
2. Décider qui ouvre les fichiers sous `donnees/` pour l'extraction.
3. Faire contre-lire cette pièce et la clé de l'épreuve par un autre modèle avant le tirage (recommandé, section 11, point 7).
4. Faire écrire et contre-lire les quatre programmes (section 10).
