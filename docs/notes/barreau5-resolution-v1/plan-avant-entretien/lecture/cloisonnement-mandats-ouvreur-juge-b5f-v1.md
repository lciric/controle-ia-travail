# Relecture de cloisonnement des mandats de l'ouvreur et du lecteur du verdict du barreau 5 (« sabotage ou empreinte de l'adaptateur ») — v1

- Relecteur neuf : Claude Opus 5.5, agent sans autre rôle dans ce plan ; n'a ouvert que les six fichiers ci-dessous.
- Date (`date -u`) : Mon Nov 23 18:18:24 UTC 2026.
- Fichiers lus, empreintes vérifiées par `sha256sum` (toutes égales à celles données) :
  - `mandat-ouvreur-b5f-v2.md` : `3c3f1092c1935b3bc6adc165da6829d4571024c541e62b008fb7263c115bc3d6`
  - `mandat-ouvreur-b5f-v2-erratum-1.md` : `c9adf95d649b7c22e0ce092ca80046d2415b7eb53d1099f3a687467b06d7c60c`
  - `mandat-ouvreur-b5f-v2-erratum-2.md` : `e52cc340af3768de544ac8002ca38b24d36cfbe3e6d9e42f81bc257b2864b04e`
  - `mandat-juge-verdict-b5f-v2.md` : `17aafef2fc3d3f1ad619293d45d9fe7157acd2b6c0fc281dc5d6e43787b6ce6d`
  - `mandat-juge-verdict-b5f-v2-erratum-1.md` : `0e1b6cbba1736d3e4d33e517e21934ed946c71a97d2662e11f541a3c70fa587e`
  - `mandat-juge-verdict-b5f-v2-erratum-2.md` : `27af332622074081195fe5fdebb06c9d75a5aa7d8c83da4a4f086f01c9d7b64e`

**Verdict : à corriger.**

Aucune fuite de résultat dans le texte (point a) : pas de score, d'aire, de statistique d'adaptateur, de sens d'effet, d'issue, de valeur de table ou de sel, ni de coût. Les seules valeurs portées sont des empreintes (sel, engagement, code, textes) et des commits, qui ne redonnent rien. Plusieurs consignes, en revanche, peuvent faire voir des pièces porteuses ou non relues (point b). Deux errata s'accordent mal avec la pièce qu'ils corrigent ou avec l'autre mandat.

## Constats

### 1. Garde de place sans commande bornée : les noms de fichiers des arbres fermés s'affichent (ouvreur, pas 6 et 7) — majeur
- Citation : « Place : le total des tailles de `git ls-tree -r -l <SCORES_COMMIT> donnees/<RUN_ID>/lecture`, seul nombre affiché » ; au pas 7 : « même garde de place qu'au pas 6 ».
- Risque : aucune commande ne fait la somme. Une session qui joue `git ls-tree -r -l` voit tous les chemins de l'arbre fermé de la lecture (des noms par famille ou par nom opaque peuvent y être) et, au pas 7, tous les chemins de la branche de la formation (adaptateurs, relances, rejets, journaux par famille et membre). C'est exactement « des sorties d'outils dont les noms de fichiers peuvent parler ».
- Correction : un programme du bloc-notes, cité, qui lance `git ls-tree -r -l` en sous-processus, additionne la colonne des tailles et n'imprime que le total et l'espace libre (ou « tient » / « ne tient pas »). Interdire d'afficher la sortie brute de `ls-tree -r`.

### 2. Liste des noms sous `donnees/` affichée en entier (ouvreur, pas 6) — moyen
- Citation : « Liste `git -C <BN>/racine ls-tree --name-only <SCORES_COMMIT> donnees/` : exactement un nom de la forme `donnees/AAAAMMJJ-HHMMSS-b5f-lecture` […] ; les autres noms sont ignorés ».
- Risque : « ignorés » veut dire vus. Les autres dossiers de la branche des scores (autres courses, sorties d'essais) s'affichent avec leurs noms.
- Correction : un programme qui filtre la sortie sur le motif `^donnees/[0-9]{8}-[0-9]{6}-b5f-lecture$` et n'imprime que le nombre de noms retenus et, s'il y en a exactement un, ce nom. Rien des autres noms.

### 3. Pièce des sorties de la formation : non relue, lue sans commande bornée (ouvreur, § 3 point 6 et pas 8) — moyen
- Citations : « puis ses seuls titres (`grep -n '^#'`) ; puis la seule section qui nomme les couples » ; § 10 : « Les valeurs `3dff7bed…`, `41e51f99…04e6` […] viennent de la contre-lecture et du conducteur, non vérifiées par le rédacteur (branches fermées) ».
- Risque : c'est une pièce non relue mise dans « ce que tu lis ». Une pièce de sortie de formation peut porter des comptes d'adaptateurs retenus ou rejetés, des relances par famille ou des coûts. Ses titres eux-mêmes peuvent parler (par exemple « Adaptateurs rejetés »). La section est lue sans plage `sed -n 'D,Fp'` ni contrôle de début. Enfin, les suffixes recopiés en (b) (`-r1`) disent quelles familles ont été relancées, et le pas 9 le fait remonter (« si (b) porte des suffixes »).
- Correction : avant de servir le mandat, faire relire la pièce `41e51f99…` par un agent de cloisonnement (titres compris), qui donne la plage exacte de la section des couples et son premier mot. Le mandat écrit alors `sed -n 'D,Fp'` avec ce contrôle. À défaut, les 30 couples de (b) sont remis à l'ouvreur dans un fichier extrait et relu par un tiers, avec son empreinte.

### 4. Le filtre du registre affiche les lignes à clé en entier, contenu et référence compris (ouvreur, § 3 point 4 et pas 5 ; lecteur, § 3 point 4) — moyen
- Citation : « un filtre de programme qui n'affiche que les lignes de table à clé » ; clés : « `GO-RELANCE-FORMATION-B5F`, `SORTIES-FORMATION-B5F`, … ».
- Risque : la colonne de référence de `SORTIES-FORMATION-B5F` ou de `GO-RELANCE-FORMATION-B5F` peut porter un nombre d'adaptateurs rejetés ou relancés, une famille, ou un coût. Aucune relecture de ces lignes n'est citée. Pour l'ouvreur, ce serait une exclusion de fait.
- Correction : le filtre de l'ouvreur n'affiche que la clé, l'instant et le contenu (pas la référence), sauf pour `SORTIES-FORMATION-B5F`, dont il extrait seulement le commit à 40 signes par motif. Pour le lecteur, le risque est moindre (il lit le résultat), mais la même restriction est plus propre.

### 5. Versement, avant le verdict, de pièces dont le contenu n'est pas borné (ouvreur, pas 17 ; erratum 2, point 7) — moyen
- Citation : « tu ajoutes et commites […] `…/entrees/couts.json`, […] `preparer-v1.txt`, `ouvrir-v1-erreur.txt` » ; erratum 2 : « `traduction-table-b5f.json` […] Au pas 17, tu le verses avec le résultat ».
- Risque : `couts.json` porte les coûts des épisodes d'évaluation des adaptateurs tenus à l'écart. C'est une catégorie de résultat que la liste d'arrêt (point 8) tient hors de l'arbre de la lecture. Ces coûts sont poussés sur une branche que le conducteur et la mère peuvent récupérer avant le verdict. `preparer-v1.txt` mêle la sortie standard et la sortie d'erreur de `preparer` sans que le mandat dise ce qu'elles portent. `traduction-table-b5f.json` dit, famille par famille, quelles copies ont été relancées.
- Correction : retenir dans `<BN>/retenus/`, avec `formation.json` et `ouvrir-v1.json`, `couts.json`, `preparer-v1.txt` et `traduction-table-b5f.json` jusqu'à `VERDICT-B5F`, et ne verser d'abord que leurs empreintes dans l'inventaire. Autre voie : écrire, d'après les fonctions `preparer` et `_main` que l'ouvreur lit, ce que chacun imprime, et le justifier dans le mandat.

### 6. Motif de refus de `preparer` lu dans un journal non filtré (ouvreur, pas 12) — mineur
- Citation : « sortie standard et sortie d'erreur redirigées vers `<BN>/journal/preparer-v1.txt` […] Code 2 : arrêt, motif à la lettre ».
- Risque : rien ne dit comment le motif est lu. Un `cat` du journal afficherait tout ce que `preparer` a imprimé avant son refus.
- Correction : comme au pas 16, `grep '^REFUS' <BN>/journal/preparer-v1.txt`, une ligne, puis le masque du § 7.

### 7. Essais et vérification d'arbre : la consigne pousse à relancer en verbeux (ouvreur, pas 1 et 4) — mineur
- Citations : « `--tb=no -rN -q` […] Un essai rouge : arrêt, son nom seul au conducteur » ; « dont tu ne gardes que le code de sortie et la dernière ligne (`| tail -n 1`) […] en cas d'échec, le seul code de sortie ».
- Risque : `-rN` supprime le résumé, donc le nom de l'essai rouge n'apparaît pas. La session sera tentée de relancer avec `-v` ou sans `--tb=no`, ce qui afficherait des valeurs d'essai. Au pas 1, `tail -n 1` s'affiche avant que l'on sache s'il y a échec, et une dernière ligne d'échec peut nommer un fichier.
- Correction : au pas 4, `-rf --tb=no` (nom des essais en échec seulement, aucune trace), et interdire toute relance verbeuse. Au pas 1, rediriger la sortie vers le journal et n'afficher que le code de sortie, puis la dernière ligne seulement si le code est 0.

### 8. Pas 1 : « clone de la branche principale » non prescrit, et `CLAUDE.md` lu pousse vers d'autres pièces (ouvreur) — mineur
- Citation : « `cd docs && sha256sum -c sha256sums-lancement-v2.txt` dans ton clone de la branche principale ».
- Risque : le pas 2 ne clone que `BRANCHE_REGISTRE` (`--single-branch`). Le clone de `main` n'est décrit nulle part (chemin, commande), et c'est un arbre qui porte `registres/etat.md`, les passations et `diag/`. `CLAUDE.md`, que l'ouvreur lit, prescrit de lire `registres/etat.md`, la dernière passation et `registres/rappels.md`. L'écart est déclaré pour les deux premiers, mais pas pour `registres/rappels.md`.
- Correction : écrire la commande du clone de `main` (chemin absolu dans `<BN>`), ou jouer la vérification des empreintes sur la racine. Ajouter `registres/rappels.md` à « Jamais ouvert », ou dire qu'il est permis.

### 9. Le lecteur voit l'issue du programme avant d'appliquer lui-même les critères (lecteur, § 3 point 5, pas 2 à 5) — moyen
- Citation : « Le résultat scellé […] en entier » ; pas 4 : « Puis compare ton issue, son niveau et ses motifs à `g_issue` du résultat ».
- Risque : le résultat est lu en entier dès le pas 2, `g_issue` compris (issue, niveau, motifs, phrases, audit). L'application indépendante (pas 4) et le recompte (pas 5) se font donc ancrés sur l'issue déjà vue. C'est « un ordre qui laisse voir le verdict avant le moment prévu », et cela affaiblit le contrôle R4 que le mandat revendique.
- Correction : au pas 2, un programme du bloc-notes vérifie l'empreinte et extrait deux fichiers : le résultat sans `g_issue`, et `g_issue` à part, scellé et non ouvert. Le lecteur fait les pas 3 à 5 sur le premier, scelle son application et son recompte, puis seulement ouvre `g_issue` pour comparer.

### 10. Motif de refus remis « entier » au lecteur (lecteur, § 2 ; ouvreur, § 7 et nœud 4) — mineur
- Citation : « Si l'ouvreur a masqué un motif […], le motif entier peut t'être remis à part : il ne change rien à ton travail » ; ouvreur, nœud 4 : « le motif entier va au lecteur du verdict avec le résultat ».
- Risque : un motif masqué nomme à la fois un nom opaque et une famille ou un membre, c'est-à-dire une ligne de la table, que le lecteur ne doit jamais voir (§ 3). Il ne sert à rien : un refus ne donne pas de résultat, donc pas de verdict.
- Correction : retirer cette phrase du § 2 du lecteur. Dans le nœud 4 de l'ouvreur, proposer que le motif entier aille à Lazar seul.

### 11. Erratum 2 de l'ouvreur, point 9 : « Lecteur du verdict : aucun erratum », alors que le lecteur verra l'écart (accord des errata) — moyen
- Citation : « Son mandat […] ne lit que `resultat-lecture-b5f.json` […] Il n'en contrôle pas `a_garde_d_ouverture.code` » ; point 7 : `a_garde_d_ouverture.code` porte « égal hors des listes fermées de la v2 et de l'erratum », le commit v3, l'empreinte de l'erratum ; point 4 : une « ligne d'épinglage de l'erratum » au registre.
- Risque : le lecteur lit le résultat en entier et applique la liste d'arrêt (l. 345 à 361, dont le point 10, « programme d'une autre empreinte : aucune ouverture »), ainsi que la règle NI (« une garde de la liste d'arrêt a invalidé la lecture »). En voie (b), il verra le champ changé et l'ouverture passée par un lanceur neuf, sans que son mandat nomme l'écart 5 ni `GO-2026-11-22-147`. Il risque alors de s'arrêter en nœud, ou de prononcer NI à tort. Son filtre du registre peut aussi montrer la ligne d'épinglage, qui n'est pas dans sa liste attendue (pas 2). Enfin, son en-tête de verdict n'a pas de place prévue pour cet écart.
- Correction : un erratum 3 au mandat du lecteur. Il dit qu'en voie (b) le champ `a_garde_d_ouverture.code` porte la mention de l'erratum de chaîne (empreinte `01298f0f…`), accordée par `GO-2026-11-22-147` (écart 5). Il dit que ce n'est ni le point 10 de la liste d'arrêt ni une garde invalidante, pourvu que `programme_sha256` égale `ed0999df…`. Il nomme la ligne d'épinglage comme ligne attendue en (b). Il demande d'écrire l'écart dans l'en-tête du verdict.

### 12. Petits désaccords entre pièces — mineur
- (a) Ouvreur, pas 18 : « ils vont à la session du lecteur du verdict par le chemin et l'empreinte » ; erratum 2 du lecteur, point 1 : « ils restent dans la session de l'ouvreur ». Le sens est compatible, mais « vont à la session » peut se lire comme une copie des fichiers. Correction : dans un erratum de l'ouvreur, « seuls leurs chemins et empreintes sont remis au conducteur, pour le lecteur ; les fichiers ne quittent pas `<BN>/retenus/` ».
- (b) Erratum 2 de l'ouvreur, point 2, pas 4 : « tu rejoues de plus, dans `<BN>/code-v3`, `tests/test_ouverture_suffixes_v1.py`, avec les mêmes options ». Le `PYTHONPATH` (`<BN>/code-v3/src` ou celui de la racine) et `--basetemp` (un dossier neuf) ne sont pas dits. Correction : les écrire en entier.
- (c) Erratum 2 de l'ouvreur, point 8 : « Nœud 3 : l'accord est GO-2026-11-22-147 ». Le nœud 3 portait sur l'accord de la décision 2, l'essai des deux listes. Correction : confirmer que `GO-2026-11-22-147` couvre aussi l'essai des deux listes, et pas seulement la voie B et la variante.

## Ce qui est sain

- Aucun chiffre de résultat, aucune issue, aucune valeur de table ni de sel dans les six pièces. Les empreintes du sel (`1516230c…`) et de l'engagement (`553cb395…`) ne redonnent rien.
- Le sel n'est jamais affiché, copié ni versé (taille et empreinte seules). La table reste dans `/dev/shm`, n'est jamais versée, et n'est écrite que pour la liste admise. Le programme `table-b5f-v2.py` n'imprime que « égale » ou « différente » et un nombre de lignes. Aucune troisième liste n'est essayée.
- Les deux listes sont scellées avant le sel. La liste (a) est fixée sans lire la pièce de la formation.
- Les branches sont récupérées par leur nom entier, jamais par motif, et jamais extraites par `checkout`. Les arbres de la lecture et de la formation sont extraits par `git archive | tar -x`, sans `-v`, dans des dossiers neufs, et ne sont lus que par le programme figé.
- La sortie de `ouvrir` est redirigée et jamais affichée. Seul le code de sortie reste à l'écran. L'erratum 1 de l'ouvreur rappelle que le résultat poussé porte déjà l'issue.
- Le masque des noms opaques dans les motifs, les extractions bornées du texte scellé avec contrôle du premier mot, et la barrière des lignes 53 à 105 sont tenus des deux côtés. Pour le lecteur, la fenêtre est plus étroite (1 à 105 interdites).
- Les exclusions sont complètes (rédacteurs et contre-lecteurs des mandats compris). L'inscription « qui a lu quoi » précède tout geste, et chaque rôle n'a qu'un seul interlocuteur.
- Lecteur : sa matière est le seul résultat scellé. En cas de divergence, il ne choisit pas. Aucun chiffre ne figure dans son message. L'erratum 1 corrige bien le motif d'extraction de la ligne 226, et l'erratum 2 retire de façon cohérente la vérification des fichiers retenus (§ 2, pas 2, § 7, table D-6).
- Les errata 1 et 2 de l'ouvreur visent les bons pas (16 ; 6, 3, 4, 11, 11 bis, 12, 13, 15, 17). L'erratum 2 laisse la racine au code figé et ne lève le nœud 9 qu'en gardant la branche `…-lecture`.
