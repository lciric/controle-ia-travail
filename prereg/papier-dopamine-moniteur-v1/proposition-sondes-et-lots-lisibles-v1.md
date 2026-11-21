# Proposition — les sondes d'intention et les lots honnêtes dont le bras « papier dopamine » peut lire les scores (v1)

**PROPOSITION, À CONTRE-LIRE, PUIS À APPROUVER PAR LAZAR.** Elle ferme la valeur ouverte VO-16 du préenregistrement court (et VO-5, qui demande la même liste) seulement une fois approuvée. Elle n'ouvre aucune lecture, aucun calcul, aucune dépense.

- Auteur : Claude Fable 5.2, concepteur du préenregistrement court (R-3735). Contre-lecteur attendu : un autre modèle (Opus 5.5).
- Date (UTC) : 21 novembre 2026, 06:20. Dépôt à `997fb18ec`.
- Accord qui la demande : GO-2026-11-21-06, point 6, `registres/go.md`, l. 605 (`964b17624c466407ce4c3bf053b50ed64c2012cdd34beb6438f170895f5dad59` à la rédaction) : « liste nominative des sondes et lots lisibles, proposée par Fable, contre-lue, approuvée par Lazar ».
- Texte servi : `prereg/papier-dopamine-moniteur-v1/preenregistrement-court-papier-dopamine-v4-brouillon.md`, étape 2b (prédictions P3 et P4) et comparaison des sondes d'intention aux quatre bases (étape 3).

## Comment la liste a été construite, et ce que je n'ai pas ouvert

Sources, et elles seules :
- les noms de fichiers du dépôt (`git ls-files`, 35 632 chemins) et la présence sur disque (`ls`) ;
- `registres/scellements-v1.md` (`bde092b6368809d53f896d3438729987c9d42413179cd390c8bb2b9185098fe0`), lu en entier, lignes tronquées ;
- `registres/decisions.md` (`d57c7cd81b27a76c2ed21e4a0bce99e39013a6c9a8a02310e188180c94b292da`), lu **par extraits autour de mots cherchés** (« cloisonn », « sonde d'intention », « sondes figées », « honnête », « tenu à l'écart »), pas en entier ; les numéros de ligne cités ci-dessous renvoient à cette empreinte.

Les empreintes de la colonne « empreinte » sont recalculées par `sha256sum` sur le fichier, sans l'ouvrir ; quand le fichier n'est pas dans cet arbre, l'empreinte est celle du registre et je le dis.

Je n'ai ouvert aucun fichier de scores, aucun fichier de résultats, aucun fichier de sondes, aucun préenregistrement autre que celui du bras, aucune conception d'organisme, ni la décision N-054. **Conséquence : chaque nom de sonde ci-dessous vient d'une ligne du registre, pas des clés du fichier ; il doit être confirmé par la mère sur les clés, sans lecture de scores.** Les extraits du registre que j'ai lus portaient quelques chiffres de papiers publiés et de jeux synthétiques ; je n'en reprends aucun et aucun n'est un résultat de sonde sur un saboteur.

## Ce dont le bras a besoin

1. Des sondes d'intention **figées avant** les épisodes où on les lit, pour P3, P4 et la comparaison aux bases.
2. Deux lots honnêtes **disjoints par famille de tâches** pour l'étape 2b (l'un ajuste le modèle de retrait, l'autre le juge), avec le texte de l'énoncé, l'état interne au dernier jeton de l'énoncé aux couches 7, 15 et 23, et le score de chaque sonde par épisode.
3. Aucun épisode saboté à l'étape 2b.

## Règle de la liste

- **Proposé** : rien n'empêche la lecture, d'après les noms et les registres.
- **Proposé sous condition** : la lecture est permise seulement une fois la condition écrite remplie par la mère, sans lecture de scores.
- **Exclu** : l'élément touche un cloisonnement nommé au registre, ou un interdit de cette session. Un élément exclu n'est lu ni en entier ni en partie.
- Tout ce qui n'est pas dans les deux premières tables est fermé. Une lecture hors liste est un arrêt (liste d'arrêt du préenregistrement, v4).

## Table 1 — sondes d'intention proposées

Le registre nomme trois sondes figées retenues pour la lecture décisive d'un autre chantier, lues à la couche 15, les couches 7 et 23 étant descriptives (`registres/decisions.md`, l. 3680). Ce sont des sondes de concept ; aucune ne porte le nom « intention » (voir la question 1 à Lazar).

| N° | Sonde, en clair | Chemin | Empreinte | Statut | Raison |
|---|---|---|---|---|---|
| S-1 | La sonde de tromperie, par différence de moyennes, couche 15 (couches 7 et 23 en second) | `donnees/20261019-230011-p3-reel/sondes-figees-legeres.npz` (fichier léger des sondes figées du premier test, 24 couples d'après le registre, l. 1981) | `701f73bd3a8ef30f46b304a6d5caa21444f0e1daf0829d04046e4024aa4e6e60` | Proposée sous condition C-1 | Figée le 19 octobre, avant le premier lot du premier test (registre, l. 447) : ses scores sur tout lot postérieur sont hors échantillon. C'est la sonde que H-D vise le plus directement : une sonde de tromperie lit-elle autre chose que l'échec attendu ? |
| S-2 | La sonde d'enjeux élevés, linéaire, couche 15 (7 et 23 en second) | même fichier | même empreinte | Proposée sous condition C-1 | Même gel. Elle sert de contraste : un concept sans lien avec l'intention, qui dit si P3 et P4 lisent une propriété de toute sonde ou de la seule sonde de tromperie. |
| S-3 | La sonde de dissimulation, linéaire, couche 15 (7 et 23 en second) | même fichier | même empreinte | Proposée sous condition C-1 | Même gel. Troisième sonde de la lecture décisive nommée au registre ; l'écarter serait un choix fait sans raison écrite. |

Pièce d'identité des trois, à lire par la mère seulement : `diag/20261019-230011-p3-reel/sondes-figees.json` (`fb41812732711c1a2a152fa776c46be5a4c50a72ccdc8fd9b7b7f9edcc37d208`). Je ne sais pas si ce fichier porte aussi des mesures.

**Condition C-1.** La mère confirme, sur les clés du fichier léger et sans ouvrir de scores, que les trois couples existent sous ces noms aux couches 7, 15 et 23 ; elle écrit les trois clés exactes dans l'addendum de l'étape 2a. Le chargeur du bras ne lit que la direction, le biais, la couche et la normalisation ; il refuse tout autre champ.

## Table 2 — lots honnêtes proposés

| N° | Lot, en clair | Chemin | Empreinte | Statut | Raison |
|---|---|---|---|---|---|
| L-1 | Un lot honnête neuf, généré pour ce bras sur des familles de tâches du banc qui ne sont ni du jeu final, ni tenues à l'écart, ni d'une banque de confirmation ; coupé en deux moitiés disjointes par famille | N'existe pas ; chemin et empreinte écrits à l'addendum de l'étape 2a | — | Proposé, sur devis | Il ne touche aucun cloisonnement et il est le seul dont la taille peut être choisie pour le point à 1 % (voir la remarque sur les effectifs). Les scores de S-1 à S-3 y sont calculés par le bras, pas relus d'un fichier ancien. |
| L-2 | Les épisodes honnêtes du premier test des sondes (course du 19 octobre) | `diag/20261019-230011-p3-reel/episodes-p3.json` ; textes `donnees/20261019-230011-p3-reel/textes-actions-p3.jsonl` ; scores `donnees/20261019-230011-p3-reel/scores-p3.npz` | `1a96cbf8ac6e10d3315bb20248453836d6ae5570b2312ded2be5ebb67cd14381` ; `ba05fa13af2dd4f935334438b44d2d27fbc655a970721b10b90bd94b5846f284` ; `968414fc7ce7db935c2c4a390a13e2eceebe2fd722628cccb52caf27128004cf` | Proposé sous condition C-2 | Déjà sur disque, sans dépense ; les sondes y étaient figées d'avance. Il sert de lot d'ajustement de l'étape 2b, ou de répétition du code, pas de lot de jugement. |
| L-3 | Les réponses à MATH500 régénérées par le bras à l'étape 1 | N'existe pas ; produit par l'étape 1 | — | Proposé, en second, sans critère | Donnée publique, honnête par construction. Les scores de S-1 à S-3 y sont un diagnostic de l'instrument (une sonde d'intention suit-elle la difficulté d'une question de mathématiques ?), jamais un verdict de P3 ni de P4 : ce ne sont pas des épisodes d'agent. |

**Condition C-2.** La mère confirme, par les seuls champs d'étiquette : que la course contient des épisodes honnêtes, leur nombre et leurs familles ; que leur issue se calcule par programme ; que les états internes au dernier jeton de l'énoncé existent aux trois couches (le nom `jetons-principales-p3.npz`, `4cd2ddb8311cfa7322d4137514c057c33039aba115aa14f08fb64141a2b0a36f`, ne le dit pas). Elle remet au bras la liste des identifiants d'épisodes honnêtes ; le chargeur ne lit dans `scores-p3.npz` que ces lignes et que les trois sondes de la table 1. Si le fichier ne se laisse pas filtrer sans charger les lignes des épisodes sabotés, la mère extrait elle-même la partie honnête (règle retenue au registre, l. 3237) et L-2 devient ce fichier extrait, sous son empreinte.

## Table 3 — exclus

| Élément, en clair | Chemin | Empreinte | Cloisonnement ou interdit touché |
|---|---|---|---|
| Les scores par action de la lecture des sondes de T0.7 (ligne `SCORES-T07`) | `donnees/20261114-001352-t07-lecture-reel/scores-actions-t07.npz`, absent de cet arbre (vérifié sur disque) | `13ac4480035f1ef6d4ea8ac81ffa962c1324e4e9e90a78c1d4f569f2abd0509d` (registre des scellements) | Résultat dérivé de 7b et de T0.7 (registre, l. 2711, 3476, 3481). |
| Les sondes apprises à l'étape A de T0.7 (ligne `SONDES-T07`) | `diag/20261114-001352-t07-lecture-reel/sondes-t07.json`, absent de cet arbre (vérifié sur disque) | `aa6892320f130e96af45e4e70b542b7ccfcea3ccd23d2fdc3e722b5637affa95` (registre) | Même cloisonnement ; je ne sais pas si le fichier porte des mesures à côté des directions. |
| L'audit des fuites de T0.7 | `diag/20261114-001352-t07-lecture-reel/audit-fuites-t07.json` | `5c76b7ff48964abe9ec552552d57c32e0b9d9ec4519a61206f7fdac349fce094` | Cloisonnement de R-2748 (registre, l. 2711). |
| Les épisodes honnêtes de la course 7b (64 d'après le registre, l. 2123) | Non cherché | — | Résultats de 7b : cloisonnement, et interdit de cette session. |
| Les épisodes honnêtes d'étalonnage de la course « mots et coût » sur le banc de T0.6 (320 d'après le registre, l. 2123) | `diag/20261116-205721-mots-et-cout-t06/`, absent de cet arbre (vérifié sur disque) | lecture `a2113f9a5c5f92fdb50e6b5390304e57c8fe51e59c99aa36f7e5cf99fb5e7d35`, issue `1b84d7c4440638699ac14711365fb865c1f5c57b50c39f44259a61b2aca53657` (registre) | Résultats de T0.6 et verdict de l'étape B, tenus hors de tout espace de l'apprentissage des sondes sur la tâche (registre, l. 2781, 2803) ; interdit de cette session. Voir la question 2 à Lazar. |
| Les sondes apprises sur la tâche et leur lecture (étape B bis de T0.7) | `diag/20261119-000444-bbis-t07-lecture-v1/lecture-bbis.json` ; texte `prereg/T0.7-etape-B-bis-v1.md` | `8e0d3e085601c3d9f5451b898acdcefc0caab6b61ddb1c6f382648e4425ed284` ; `0ae6210f954917fecff647f45a129961c0676517381becbffe1fd5ac7b90d9eb` | Résultats de l'étape B bis : interdit de cette session ; cette étape a un bras de transfert vers un mode tenu à l'écart (registre, l. 2674), donc cloisonnement du mode tenu à l'écart (N-054, l. 3641). Voir la question 1. |
| La sonde d'intention « du domaine », à apprendre | Aucun objet figé (registre, l. 3680) | — | Elle n'existe pas ; son jeu de paires vient du même fichier que l'étalonnage d'une course cloisonnée (registre, l. 3683). |
| Les jeux synthétiques d'intention et de dissimulation de T0.7 | `donnees/t07-jeux-synthetiques-v2/intention-autres-modes-v2.jsonl` ; `…/dissimulation-v2.jsonl` | `5b0409209e66e6c29b69e675c5836cefbef966d9cc0a34412837cae837e2aacf` ; `32f412888270a3c4b4bc347cf57055bd11b517000feceeaeed122476238ec228` | Ni sondes ni lots honnêtes d'agent : ce sont des jeux de lecture de T0.7. Écartés pour ne pas être pris pour des lots. |
| Les jeux publics qui ont pu servir à apprendre les sondes | `donnees/T0.7-models-under-pressure-v1/training/train.jsonl` ; `donnees/T0.7-faits-repe-v1/facts_true_false.csv` | Non calculées | Inférence d'après les noms seulement : un lot qui a servi à apprendre une sonde ne peut pas la juger. À confirmer par la mère ; écartés par prudence. |
| Tout ce qui touche les organismes discrets (bras A), leurs sujets et leur fichier de scores | `prereg/T0.7-organismes-discrets-v-a-v1.md` et ses suites | `06ab6a2f6e173bb1258f45ffeded7a419b05ecc2f59920666cea91aafcc7cf05` | Cloisonnement des sujets des organismes discrets (registre, l. 3439, 3441, 3489) et du fichier des scores. |
| Tout ce qui touche le saboteur à budget | Dossiers nommés dans les interdits de cette session ; `docs/notes/barreau8-iib-v1/` | — | Rédacteur cloisonné (registre, l. 3907 et suivantes) ; interdit de cette session. |
| La lecture des sondes du barreau 8, côté moniteurs | `prereg/lecture-sondes-barreau8-v1.md` ; `docs/notes/barreau8-cote-moniteurs-sorties-v1/` | `8e432cdc3d6998324281467e1bac5df3adb93ff7ba803b8ad7f877ffd5e8feb4` | Session « côté moniteurs » séparée par mandat ; scores non courus ou cloisonnés. |
| Le barreau 5 (sabotage ou empreinte, adaptateurs tenus à l'écart) | `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1.md` | `bdff244f1377e795b84f71518bb5e58fb1600fff8afee383d8f70c10d3f5d935` | Adaptateurs tenus à l'écart ; interdit de cette session sur tout score et toute table. |
| Les six couples de Mahalanobis du fichier complet des sondes figées | Branche distante `calcul/regeneration-sondes-p3-v1`, en neuf morceaux (registre, l. 1987) | Abrégée au registre : `91b61c45…` | Ce ne sont pas des sondes d'intention ; fichier absent de `main` et du disque. |
| Tout épisode du jeu final, d'une famille tenue à l'écart, d'une banque de confirmation | — | — | N-050, N-062, N-059 ; déjà dans la liste d'arrêt du préenregistrement. |

## Le mode de sabotage tenu à l'écart et cette liste

Lazar a décidé que le bras lit le mode tenu à l'écart (GO-2026-11-21-06, point 2). Cela ne change rien à l'étape 2b, qui ne lit que des épisodes honnêtes. À l'étape 3, les scores de S-1 à S-3 sur les épisodes de ce mode sont des résultats de ce bras sur ce mode : ils tombent sous la garde de la mère (aucun n'est servi à une session qui conçoit des sondes ou des moniteurs) et sont écrits dans un fichier à part. Aucun lot de la table 2 ne contient d'épisode de ce mode, par construction : ce sont des lots honnêtes.

## Remarque sur les effectifs, à porter au devis

Le point de verdict est 1 % (GO-2026-11-21-06, point 1). Un seuil à 1 % par tranche de longueur ne s'étalonne pas sur quelques centaines d'épisodes : sur 300 épisodes honnêtes, trois seulement dépassent le seuil attendu. Le lot L-2 ne peut donc pas servir à l'étalonnage du point de verdict, quelle que soit sa taille exacte ; le lot L-1 est le seul qui le puisse, et sa taille décide si les épreuves sont jugeables ou « non concluantes ». Ce n'est pas une raison de changer de point : c'est le coût de la décision, à voir avant le devis.

## Questions à Lazar

1. **Les sondes apprises sur la tâche entrent-elles un jour dans la liste ?** Ce sont les sondes du programme les plus proches d'une « sonde d'intention », et elles sont exclues ici (table 3). Options : (a) non, la liste reste aux trois sondes figées — net, mais le bras ne dit rien de la famille de sondes que le programme défendra ; (b) oui, plus tard, par un texte à part contre-lu, lues par une session qui n'a rien conçu — répond à la vraie question, mais touche un cloisonnement de plus et le mode tenu à l'écart ; (c) oui, tout de suite — je le déconseille. Recommandation : (a) maintenant, (b) ouvert plus tard sur ta demande. Confiance 0,7. Défaut : (a).
2. **Les épisodes honnêtes d'étalonnage de la course « mots et coût » peuvent-ils être extraits seuls par la mère ?** Ce serait un second lot honnête sans dépense. Options : (a) non, exclus — sûr, mais L-1 porte alors tout ; (b) oui, la mère extrait la seule partie honnête dans un dossier neuf sous empreinte, sans verdict ni lecture — économe, mais c'est elle qui juge si la séparation tient. Recommandation : (a) tant que L-1 n'est pas chiffré. Confiance 0,6. Défaut : (a).
3. **Trois sondes ou une seule ?** Trois sondes triplent les lectures de P3 et P4 ; le préenregistrement (v4) les rend par sonde, avec correction de Holm entre sondes. Garder la seule sonde de tromperie (S-1) donnerait plus de puissance. Recommandation : garder les trois, S-1 étant la lecture principale et les deux autres secondaires. Confiance 0,6. Défaut : les trois, S-1 principale.

## Ce que je n'ai pas pu établir par les noms

- Si les trois sondes figurent bien dans le fichier léger sous ces noms (condition C-1).
- Si la course du premier test contient des épisodes honnêtes, combien, et de quelles familles (condition C-2).
- Si les épisodes de validation du harnais d'octobre (`diag/20261005-144628-validation-reelle`, `diag/20261006-114025-validation-reelle`, `diag/20261006-115440-validation-reelle`) sont des épisodes honnêtes utilisables : rien dans leurs noms ni dans les extraits lus ne le dit ; non proposés.
- Si d'autres sondes figées existent sur des branches distantes : je n'ai cherché que dans l'arbre courant et dans les deux registres.
- Les numéros de ligne du registre des décisions valent pour l'empreinte citée ; le registre grandit.
