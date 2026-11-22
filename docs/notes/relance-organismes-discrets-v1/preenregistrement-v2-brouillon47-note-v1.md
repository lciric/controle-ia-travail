# Note du brouillon 47 du texte neuf du bras A des organismes discrets — v1

- **Correcteur** : Claude Opus 5.5 (`claude-opus-5-5`), agent neuf, délégué par la session de relance. Règle suivie (décision de Lazar, GO-2026-11-21-84) : j'écris seulement les corrections, mot pour mot d'après les remarques déjà reçues ; je ne conçois rien.
- **Date** : 2026-11-22. Branche `claude/pensive-bardeen-1fv7hw`. Aucun réseau, aucune clé, aucune dépense, aucun commit.
- **Base** : brouillon 46, `prereg/T0.7-organismes-discrets-v-a-v2-brouillon46.md`, `b5e1031c9b92d7643815e9d18abec86f900fee0931eb6030839729b2f32c3fb9` (recalculée), 2 544 lignes.
- **Remarques portées** : contre-lecture 10, `docs/notes/relance-organismes-discrets-v1/contre-lecture-10-brouillon46-bras-a-v1.md`, `f711c9be09b8912adcb82d469a09f03e89b80ac67950cc2235e4d2cfebda1881` (recalculée) ; verdict « scellable après corrections », aucun bloquant, sept majeurs, neuf mineurs. Portés : M-1, M-2, M-4, M-5 et les mineurs. **Non portés** : M-3, M-6, M-7 (mandat).
- **Textes du mandat** recopiés tels quels : case « commit du code de l'instrument et de l'analyse » ; case « familles » ; fichier des règles qui fait foi et nom du programme de la file du juge (pour m-4).
- **Sortie** : brouillon 47, `prereg/T0.7-organismes-discrets-v-a-v2-brouillon47.md`, `f59f6b4ed2b1198c3781badf83692d593ed4ade0df5baa9f0e4ea8b1827a6cb9`, 2 546 lignes (deux lignes ajoutées, toutes deux après les règles).
- **Fichier des règles neuf** : `docs/notes/relance-organismes-discrets-v1/essais-admission-bras-a-v1/regles-admission-bras-a-v1-brouillon47.md`, `4ae135309e60a68c5fe07679787d23032db200cbb22e8c7a95a04de984978b77`.

## 1. Comment le brouillon 47 est fait

Par un programme, `docs/notes/relance-organismes-discrets-v1/brouillon47-corrections-v1/appliquer_corrections_brouillon47_v1.py` (`aca83838c88810a617fde4ede3da0eb60e48f3bb26684c020b3c3c0e3adc74fa`), lancé par `python3 -I … /home/user/controle-ia-travail`, sur le modèle du programme du brouillon 46. Il contrôle les empreintes de la contre-lecture 10, du brouillon 46, du fichier des règles du 46 et du programme `scripts/chef_essais_admission_bras_a_v12.py`. Il **lit les textes proposés dans le fichier de la contre-lecture** (textes entre guillemets des lignes 24, 25, 26, 36, 38, 48, 50, 53, 54, 63, 65, 67, 69 et 71), sans les recopier à la main, et vérifie le début et la fin de chaque extrait. Il fait 30 remplacements exacts, chacun sur un ancien trouvé une seule fois, et s'arrête sinon. Il refuse d'écrire si les lignes 542 à 550 changent, si leur empreinte jointe n'est pas `3d1f0afe82f5aeb3bf5dd757cb6d814e19c66b93a89a65b6f08677823e1b8f96`, si une autre ligne que 1, 3 et 522 change avant elles, s'il reste une marque ⟦ ⟧ ou si le fichier de sortie existe déjà (R12).

Fichier des règles : `docs/notes/relance-organismes-discrets-v1/brouillon47-corrections-v1/faire_regles_brouillon47_v1.py` (`037e700504c78fbbd774c5bc5c15ba54cba2120d268f661fc0f33342b67af6bb`), depuis le fichier du 46 (`fdc9254f…`, contrôlé) : seules changent la mention « définitif sur le brouillon 47 », l'empreinte et le chemin du texte en vigueur, et le nom du programme (`scripts/chef_essais_admission_bras_a_v6.py` → `scripts/chef_essais_admission_bras_a_v12.py`, qui porte bien une commande `regles`, relevé par recherche dans le programme). Il vérifie que les neuf lignes copiées (titre et huit règles) sont égales aux lignes 542 à 550 du brouillon 47, elles-mêmes égales à celles du 46, et qu'aucune ligne ne suit. Rendu : « règles égales : True ».

## 2. Chaque changement (ligne du 46 → ligne du 47)

| ligne 46 → 47 | correction portée | ce qui change |
|---|---|---|
| 1 → 1 | histoire | « BROUILLON 46 » → « BROUILLON 47 » |
| 3 → 3 | histoire ; M-2 | statut du 47 (corrections portées, cases remplies, M-3, M-6 et M-7 en attente, M-6 et M-7 au directeur) ; **déclaration des cases de 13.1 ouvertes** : « nœuds », « lecteurs et juge des ancres », « entropie », « renvoi de la base », « module des cinq moniteurs, côté habilité » ; puis « **État au brouillon 46, dépassé pour ce que le brouillon 47 change** : » devant le statut du 46, gardé |
| 522 → 522 | m-8 (3.4, demi-ligne) | après le relevé de `gemini-4-neon` : « ; température retirée d'avance pour `mistral-large-4-0` (GO-2026-11-21-86) » |
| 551 → 551 (neuve) | M-5 (3.4) | ligne neuve « - La sortie maximale que donne la règle 7 est confrontée… (8.4). », **après la règle 8** (ligne 550), non entre 7 et 8, pour que les règles ne bougent pas |
| 551 → 552 | M-4 (i) ; m-9 | parenthèse des deux étapes remplacée par le texte de M-4 (lots `ancre-plans-honnetes`, puis `ancre-couverture` ; `ancre-jumeaux` ; lots de la révision ; clé `ordr/{lot}`) ; « ceux de rang impair » → « les appels de rang impair » |
| 598 → 599 | m-2 | « presque jamais jugés « appariés spécifiques » » → « jugés « appariés spécifiques » au plus 10 % » ; « jamais jugé apparié » → « jugé apparié au plus 5 % » |
| 771 → 772 | m-7 | point d'insertion 2 de 6.3 : phrase de R3 ajoutée à la fin du point |
| 922 → 923 | m-3 (6.10) | « est à écrire, avec ses essais (13.1) » → « est écrit côté habilité (case de 13.1) » |
| 972 → 973 | m-3 (6.12, point 6) | « **Manque, à écrire avant scellement** (13.1) » → « **Écrit** (case « code de la base », 13.1) » |
| 1007 → 1008 | m-1 | ligne A8 : texte de m-1 ajouté à la fin de la condition |
| — → 1194 (neuve) | M-4 (iii) | ligne neuve de 8.4, « voie de service du juge », dernière ligne de la table |
| 1199 → 1201 | m-3 (8.4, sous la table) | « ligne de GO à inscrire, case « nœuds » » → « ligne de GO inscrite, case « nœuds » » |
| 1226 → 1228 | m-3 (8.7) | « encore à inscrire » → « GO-2026-11-20-19 (case « nœuds ») » |
| 1452 → 1454 | M-1 (section 13, étape 6) | étape 6 récrite au texte de M-1, « (R1) » gardé |
| 1460 → 1462 | m-3 (case « nœuds ») | « date d'envoi à Lazar à inscrire » → « date d'envoi à Lazar **À REMPLIR** » |
| 1462 → 1464 | mandat, point 4 ; m-5 | « **remplie, sauf un reste À REMPLIR** » → « **remplie** » ; phrase de la confrontation remplacée par le texte du mandat ; puis « ; une confrontation négative laisserait le rôle non pourvu par les règles 5 et 6 » ; la parenthèse « (brouillon 45 ; fiche des faits … information.) » gardée telle quelle |
| 1463 → 1465 | m-3 ; m-4 | « restent à inscrire ici » : état « fait » ajouté ; **fichier des règles qui fait foi au scellement** : celui du 46 (`fdc9254f…`, entier), programme nommé `…_v6.py` dans ce fichier, file du juge conduite par `…_v12.py` (`6aa04397…`, entier), déclaré ; liste (1) à (6) : état de chaque point ; « ligne de GO à inscrire » → « ligne de GO inscrite » |
| 1466 → 1468 | M-1 (case « entropie ») | deux remplacements, au texte de M-1 |
| 1471 → 1473 | m-6 | phrase de la troisième issue ajoutée après « ou « non vérifié : discrétion non lue » » |
| 1472 → 1474 | mandat, point 3 | « **À REMPLIR** : le commit, à inscrire… (GO-2026-11-19-24, point 1) » → « **remplie** : commit `2b9f8232…` (entier), branche…, inscrit par la session mère (…) » ; rien d'autre |
| 1483 → 1485 | M-4 (« même précision ») ; M-5 (13.2) | parenthèse du rang récrite avec les mots de M-4 ; texte de M-5 ajouté à la fin de la cellule |
| 2541 → 2543 | M-1 ; histoire | parenthèse de l'entrée remplacée au texte de M-1 ; « non faite. À inscrire … ; et, à part, » → « . **Contre-lecture 10 faite** : texte relu (chemin, empreinte entière) ; rapport (chemin, empreinte entière) ; contre-lecteur : agent neuf, Claude Opus 5.5 ; verdict « scellable après corrections », aucun bloquant, sept majeurs, neuf mineurs ; traitement … À inscrire ici avant scellement, à part : » ; la vérification habilitée reste à inscrire |

## 3. Ce qui n'est pas porté mot pour mot, déclaré

1. **M-2** : la contre-lecture ne propose aucun texte (« Elles doivent être ajoutées à la liste des cases ouvertes »). Le texte n'avait pas de liste ; la déclaration est écrite par le correcteur dans le statut (ligne 3), au plus court. La marque reste dans les deux cases.
2. **M-1, étape 6** : « même changement » sans phrase d'insertion ; le texte entre guillemets est mis à la place de l'ancienne étape, première lettre en capitale ; « (R1) » est gardé ; « (R2) » et « par un contre-lecteur d'un autre modèle que le rédacteur » disparaissent de l'étape (ils restent dans l'entrée « Contre-lecture 10 »).
3. **M-1, entrée « Contre-lecture 10 »** : la phrase neuve est suivie de l'inscription ; « : non faite. » devient « . **Contre-lecture 10 faite** : … », phrase du correcteur.
4. **M-4, ligne 552** : le texte proposé remplace la parenthèse ; la phrase garde ensuite « les appels, un item par appel, partent dans l'ordre tiré du lot (8.6) » et « à chacune des deux étapes », ce qui fait redite et ne compte pas les lots de la révision ; non corrigé, faute de texte proposé. **Ligne 1485** (« même précision ») : pas de texte proposé ; la parenthèse est récrite avec les mots de M-4, « ), chacun » devenant « ; chacun ».
5. **M-5** : placé **après la règle 8**, et non juste après la règle 7, pour que les lignes 542 à 550 ne bougent pas (mandat) ; ligne neuve de liste à puce. En 13.2, ajouté à la fin de la cellule « contenu », après un point. **Aucune ligne de 8.4 n'est ajoutée pour cette garde** : M-5 la dit « éprouvée … (8.4) » sans en donner la ligne.
6. **m-2** : « au plus 10 % » et « au plus 5 % » placés après le verbe ; ordre des mots du correcteur.
7. **m-3** : textes proposés seulement pour 6.10 et 6.12 (portés). Pour 8.4 sous la table, la case « lecteurs », 8.7 et la case « nœuds » : texte le plus court du correcteur (« inscrite », l'identifiant GO-2026-11-20-19 lu dans la case « nœuds », la marque). Pour les listes de la case « lecteurs », l'état de chaque point est écrit par le correcteur d'après la seule case : « fait » là où la case cite la pièce par chemin et empreinte ; **reste** pour la contre-lecture du devis (2) et le relevé de chaque vérification de clé par chemin et empreinte (3) ; à contre-lire. **Non porté** : le point du module (ligne 1475, restes (8) à (10)), que la contre-lecture renvoie au remplissage de cette case (« les clore au remplissage »).
8. **m-4** : pas de texte proposé ; fichier et programme donnés par le mandat. Le texte cite le fichier du **46** comme celui qui fait foi : le brouillon 47 ne peut pas citer le fichier du 47, qui porte son empreinte. **Tension laissée à la session** : la règle 8 dit que le fichier « cite l'empreinte du brouillon en vigueur » ; le fichier du 46 cite le 46, celui du 47 cite le 47 ; lequel le texte scellé citera reste à dire au scellement.
9. **m-5** : la phrase est celle que la contre-lecture cite de la vérification du brouillon 45, placée dans la case familles, au conditionnel, après la confrontation remplie.
10. **m-8** : demi-ligne du correcteur autour des mots cités (« température retirée d'avance ») ; la partie « au remplissage des champs exacts » n'est pas portée (case ouverte).
11. **m-1, m-6, m-7, m-9** : textes proposés, placés à la fin de la cellule, de la case ou du point visé.
12. **Histoire, « 46 » → « 47 » dans « Contre-lecture »** : lu comme l'inscription de la contre-lecture 10 ; les mentions d'histoire de cette section (« **Ajouté au brouillon 46** », « traitement : au brouillon 46 », « le brouillon 46 va à la contre-lecture 10 ») sont vraies et gardées.
13. **Non porté, hors mandat** : la ligne 1871 (table 14, R-11) dit encore « contre-lecture 10 à faire sur le texte aux cases remplies » ; M-1 ne la vise pas.

## 4. Diff contrôlé par programme contre le 46

`difflib.SequenceMatcher` (sans élagage) sur les lignes : 46, 2 545 éléments (2 544 lignes et une fin) ; 47, 2 547 ; 2 525 lignes égales ; 20 lignes du 46 changées ; 2 lignes ajoutées (551 et 1194 du 47). Blocs de `diff` : 1, 3, 522, 551 (→ 551 et 552), 598, 771, 922, 972, 1007, après 1192, 1199, 1226, 1452, 1460, 1462 et 1463, 1466, 1471 et 1472, 1483, 2541 — exactement les lignes de la partie 2. Avant la ligne 542, seules les lignes 1, 3 et 522 changent (vérifié par le programme). Validateur du dépôt (`controle_ia.prereg.problemes`) sur le 47 : un problème, « marqueur À REMPLIR restant hors des sections exigées », attendu ; celui de la contre-lecture 10 sans ses deux empreintes a disparu. La marque compte **sept occurrences sur cinq cases** : « nœuds » (2), « lecteurs et juge des ancres » (1), « entropie » (1), « renvoi de la base » (1), « module des cinq moniteurs » (2).

## 5. Les huit règles d'admission

Aux **lignes 542 à 550** du brouillon 47 (titre à la ligne 542, règles 1 à 8 aux lignes 543 à 550), égales caractère pour caractère à celles du 46 (comparaison de listes, et empreinte jointe `3d1f0afe…`) ; aucune ligne n'est ajoutée avant elles. Le fichier des règles du 47 les porte caractère pour caractère, vérifié par programme.

## 6. Lignes changées qui touchent la base « mots et coût » ou le verdict de discrétion (pour le lecteur habilité)

Numéros du brouillon 47 :
- **973** (6.12, point 6, la base) : programme d'extraction des six conditions dit « écrit (case « code de la base », 13.1) ».
- **1473** (case « renvoi de la base ») : troisième issue ajoutée (m-6).
- **923** (6.10, message des moniteurs à modèle de langue) : code du message dit écrit côté habilité.
- **1201** (8.4, sous la table, table des identifiants opaques des scores des moniteurs, écart à R9) : « ligne de GO inscrite ».
- **1228** (8.7, tenue du registre jusqu'au tirage de la table des identifiants opaques) : identifiant de la ligne du mot « go recos ».
- **1454** (section 13, étape 6, ordre du renvoi de la base après la contre-lecture 10) : étape récrite (M-1) ; la phrase d'ordre qui suit n'a pas changé.
- Indirect : **3** (le renvoi de la base nommé parmi les cases ouvertes) ; **1468** (entropie racine, dont dérivent aussi les graines des moniteurs : seul change ce qui borne la différence entre texte relu et texte scellé) ; **2543** (la vérification habilitée reste à inscrire).

Aucune autre ligne changée ne touche la base ni la discrétion.

## 7. Ce que j'ai ouvert

- **En entier** : CLAUDE.md (dans mes consignes) ; la contre-lecture 10 ; les deux programmes du brouillon 46 (`appliquer_corrections_brouillon46_v1.py`, `faire_regles_brouillon46_v1.py`) ; le fichier des règles du 46 et son compagnon ; le début de la note du brouillon 46 (forme).
- **Le brouillon 46** : par recherche de chaîne et par extraits autour des lignes visées (1, 3, 522, 551, 586 et 587, 594 à 646 pour la prédiction et les seuils, 748 à 786, 818 et 819, 922, 972, 1007, 1033, 1100 à 1203, 1226, 1441 à 1495 dont les cases 1460, 1462, 1463, 1466, 1471, 1472, 1483 en entier, 2528 à 2544).
- **Par programme** : empreintes de la contre-lecture 10, du 46, du fichier des règles du 46 et de `scripts/chef_essais_admission_bras_a_v12.py` ; recherche des sous-commandes de ce programme (`regles`) ; `controle_ia.prereg.problemes`.
- **Rien d'autre**. Aucun chemin cloisonné ouvert, listé, cherché ni empreinté ; la pièce des familles (`5e83cf07…`) est citée d'après le mandat, non ouverte. Les chemins sous `runs/` que le texte cite ne sont pas ouverts.
