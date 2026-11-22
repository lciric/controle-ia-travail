# Note du brouillon 46 du texte neuf du bras A des organismes discrets — v1

- **Correcteur** : Claude Opus 5.5 (`claude-opus-5-5`), agent neuf, délégué par la session de relance. Règle suivie (décision de Lazar, GO-2026-11-21-84) : j'écris seulement les corrections, mot pour mot d'après les remarques déjà reçues ; je ne conçois rien.
- **Date** : 2026-11-22. Branche `claude/pensive-bardeen-1fv7hw`. Aucun réseau, aucune clé, aucune dépense, aucun commit.
- **Base** : brouillon 45, `prereg/T0.7-organismes-discrets-v-a-v2-brouillon45.md`, `4588944f9658a7ddb563296821392404be96241ba41027b7d15df72194eb6b4d` (recalculée), 2 543 lignes.
- **Remarques portées** : vérification du brouillon 45, `docs/notes/relance-organismes-discrets-v1/verification-brouillon45-bras-a-v1.md`, `6ab0def272f0f0d48423bcd4aa9a1f81c8753d34ee5d4d512a65e214740bfac0` (recalculée) ; verdict « engageable après corrections », cinq corrections, neuf mineurs.
- **Sortie** : brouillon 46, `prereg/T0.7-organismes-discrets-v-a-v2-brouillon46.md`, `b5e1031c9b92d7643815e9d18abec86f900fee0931eb6030839729b2f32c3fb9`, 2 544 lignes.
- **Fichier des règles neuf** : `docs/notes/relance-organismes-discrets-v1/essais-admission-bras-a-v1/regles-admission-bras-a-v1-brouillon46.md`, `fdc9254fc2294343e1ff1d5d527ac8b24a466f084ff38d674013580321eb31d2`.

## 1. Comment le brouillon 46 est fait

Par un programme, `docs/notes/relance-organismes-discrets-v1/brouillon46-corrections-v1/appliquer_corrections_brouillon46_v1.py` (`941a29419a86776438da1c96d19a7c829715449bd5422bbcb7c79a2aa703a913`), lancé par `python3 -I … /home/user/controle-ia-travail`. Il contrôle l'empreinte de la vérification et celle du brouillon 45. Il **lit les textes proposés dans le fichier de la vérification** (citations des lignes 44, 50 à 52, 60 et 66 ; textes entre guillemets des lignes 46, 62, 70, 71, 81, 126, 127 et 128), sans les recopier à la main. Il fait 17 remplacements exacts, chacun sur un ancien trouvé une seule fois, et s'arrête sinon. Il refuse d'écrire si les lignes 542 à 550 changent, si leur empreinte jointe n'est pas `3d1f0afe…`, s'il reste une marque ⟦ ⟧ ou si le fichier de sortie existe déjà (R12).

## 2. Chaque changement (ligne du 45 → ligne du 46)

| ligne 45 → 46 | correction portée | ce qui change |
|---|---|---|
| 1 → 1 | histoire | « BROUILLON 45 » → « BROUILLON 46 » |
| 3 → 3 | histoire ; information pour Lazar (partie 3, (b)) | « **Statut : brouillon 45** » → « **Statut : brouillon 46** » ; ajout d'une phrase d'histoire (corrections C-1 à C-5 et mineurs m-2 à m-7 de la vérification du brouillon 45, mot pour mot, par GO-2026-11-21-84 ; aucune règle, aucun seuil, aucune issue ni aucune prédiction ne change ; huit règles aux lignes 542 à 550) ; ajout de **l'information pour Lazar**, à la phrase proposée, mot pour mot ; puis « **État au brouillon 45, dépassé pour ce que le brouillon 46 change** : », devant le paragraphe du 45 inchangé |
| 3 → 3 | m-2 | « Il ne modifie ni les brouillons 1 à 41, » → « … 1 à 44, » ; « inscrite comme contre-lecture 9 (R2 ; » → « inscrite comme contre-lecture 9 (au brouillon 45 : contre-lecture 10) (R2 ; » |
| 9 → 9 | C-5 (ligne 9) | « versée par la session, qui en inscrit le chemin et l'empreinte (brouillon 45 : » → « versée par la session (note du rédacteur du brouillon 45 : `…/sortie/relecture-fable-api.md`, `a4e1712a…` ; mandat : `…/brouillon45-par-api-v1/mandat-redacteur-fable-api-brouillon45-v1.md`, `213ad3db…` ; brouillon 45 : » (texte de la vérification, chemins et empreintes entiers comme elle les donne) |
| 518 → 518 | m-3 | « mineurs m-1 à m-8) » → « mineurs m-1 à m-9) » |
| 551 → 551 | C-1, avec m-6 | la parenthèse « (brouillon 45 ; vérification du brouillon 44, m-2 : sous la décision de la session principale … n'étant pas donnés au rédacteur) » est remplacée par le texte proposé, mot pour mot (« session mère » ; exemption du seul contrôle « réflexion plus 16 000 jetons de texte » ; sonde envoyée ; avenant 2, version 3, section 6, chemin et `9d4b8a08…` ; GO-2026-11-22-03 qui remplace GO-2026-11-21-88 ; « si bien que ce point garde son objet ») |
| 551 → 551 | m-5 | ajout, à la suite, d'une phrase : « à l'essai, la file du juge est partie au régime prudent, imposé par la configuration sur décision de la session mère, alors que les deux sondes étaient « comprises » (rapport technique `7bb8cc95…`) : ce point relève du devis, non de ce texte, et le régime prudent est le plus strict (brouillon 46 ; vérification du brouillon 45, m-5) » |
| 551 → 551 | C-3 (ligne 551) | « dans chaque file du juge à la course, les appels partent dans l'ordre de ses items ; » → le texte proposé, mot pour mot (deux étapes (d) et (e′), deux lots, ordre tiré du lot (8.6), rang compté à partir de 1 par lot, tableau sans nommer d'item, écrit avant que le lot de (e′) existe), suivi de « ; » |
| 1462 → 1462 | C-4 | « , ce qui est dit ici sans être tranché) » → « . Ce n'est pas un écart : … C'est dit à Lazar comme une information.) », texte proposé mot pour mot |
| 1463 → 1463 | C-2 | « reste À REMPLIR, pour ce que la fiche ne donne pas : la sortie maximale … les champs exacts de chaque service** (brouillons 40, 41 et 45) » → « reste À REMPLIR : les champs exacts de chaque service** (brouillons 40, 41 et 45 ; brouillon 46 : vérification du brouillon 45, C-2). Le reste est transcrit des pièces citées, compteurs seulement : » puis les deux puces proposées, mot pour mot, mises à la suite (Mistral Large 4 : 12 652 ; 51 200 ; 24 sur 24 ; 104,9661 USD ; `api.eu.mistral.ai` ; `mistral-large-4-0` — `gemini-4-neon` : 8 sur 8 ; 0,1131545 et 0,2578845 USD) |
| 1483 → 1483 | C-3 (ligne 1483) | ajout de « (rang compté dans chaque lot du juge, étapes (d) et (e′), dans l'ordre tiré du lot) » après « le même partage par rang qu'à l'essai d'admission » |
| 2513 → 2513 | m-4 | « aucune fiche n'est ajoutée » → « aucune section de jugement n'est touchée ; treize lignes de table sont ajoutées » |
| 2518 → 2518 | C-1 (ligne m-2 de 14.57) | traitement remplacé par le texte proposé : « **ajouté** au point (3) : l'exemption ne vise que le contrôle « réflexion plus 16 000 » ; la sonde est envoyée et rend « comprise » sur chaque clé ; l'avenant 2, version 3 (`9d4b8a08…`), est cité » |
| — → 2528 | m-7 | ligne neuve de la table de 14.57 : le fichier des règles du premier envoi cite toujours les lignes 529 à 537 et le brouillon 44, ce qui est juste par la règle 8 ; les mêmes règles sont désormais aux lignes 542 à 550 |
| 2540 → 2541 | histoire (« Contre-lecture ») | ajout, en fin de ligne : « **Ajouté au brouillon 46** : la vérification du brouillon 45. » |
| 2541 → 2542 | C-5 (ligne 2541) | « le chemin et l'empreinte du rapport entier, son auteur et son verdict sont à inscrire par la session » → texte proposé, mot pour mot (rapport du 44, `be7b0453…` entier ; agent neuf, Claude Opus 5.5 ; « engageable », aucune correction, neuf mineurs) |
| 2541 → 2542 | C-5 (« inscrire ensuite la présente vérification ») ; histoire | ajout de « **vérification du brouillon 45** (faite) : brouillon vérifié …45.md, `4588944f…` (entière) ; rapport …verification-brouillon45-bras-a-v1.md, `6ab0def2…` (entière) ; vérificateur : agent neuf, Claude Opus 5.5 ; verdict « engageable après corrections », cinq corrections, neuf mineurs ; traitement : au brouillon 46, mot pour mot (statut) » ; « le brouillon 45 va à la contre-lecture 10 » → « le brouillon 46 va à la contre-lecture 10 » |

Mineurs sans changement : m-1 (accepté par la vérification), m-6 (porté par le texte de C-1), m-8 (sans effet), m-9 (information inchangée, déjà dite).

## 3. Ce qui n'est pas porté mot pour mot, déclaré

1. **C-1, ligne de table pour l'avenant 2 : non ajoutée.** La table des documents est aux lignes 206 à 218, avant les huit règles ; une ligne de plus déplacerait leurs numéros, ce que le mandat interdit. L'avenant 2 est cité au point (3) (ligne 551) par son chemin et `9d4b8a08…`, et dans la ligne m-2 de 14.57. Empreinte entière, telle que la vérification la donne : `9d4b8a08fbeec8568f03aafe5f882b0631cbd0fef501641f99303591d4d103e3`. À décider par la session.
2. **Points finaux retirés.** Le texte de C-1, celui de C-3 (ligne 551) et la seconde puce de C-2 finissent par un point. Dans le 46, ils sont suivis de « ; (4) », de « ; ceux de rang impair » et de « — **état au 22 novembre** ». J'ai retiré ce seul point final. Pour C-3, « ceux de rang impair » suit désormais une phrase sur le tableau. La lecture reste « les appels de rang impair », mais la grammaire en est moins nette : à voir par la contre-lecture.
3. **C-2 dans une case de table.** Les puces sont mises à la suite, séparées par « ; », et non sur des lignes à part. Le gras de la case est fermé après « chaque service », avant les gras des puces. La marque « (brouillons 40, 41 et 45 ; brouillon 46 : vérification du brouillon 45, C-2) » est un ajout du correcteur. La phrase « saine voulant dire, en 3.4, … » reste, comme la vérification le permet.
4. **C-4 : ligne 518 non touchée par C-4.** La parenthèse que vise le texte proposé n'est qu'à la ligne 1462. La ligne 518 dit seulement que la confrontation n'est pas faite, ce qui reste vrai. Elle ne change que par m-3.
5. **C-5, ligne 9.** Le texte proposé prend la place de « , qui en inscrit le chemin et l'empreinte », entre parenthèses, devant « brouillon 45 : … ». Le « …/ » du chemin du mandat est gardé tel que la vérification l'écrit.
6. **C-5, « inscrire la présente vérification de la même façon ».** Elle est inscrite à la ligne 2542, dans la même forme que les vérifications 42 et 43. Aucune section 14.58 n'est écrite : le traitement est dit « au brouillon 46, mot pour mot (statut) », avec la ligne m-7 en 14.57.
7. **m-5 : la vérification ne donne pas de texte.** La phrase est la plus courte que j'ai pu écrire avec ce qu'elle dit. Je l'ai placée à la fin du point (3). Elle cite le rapport technique du juge, `7bb8cc95…` (le même que dans C-2), comme la vérification dit « d'après le rapport technique ».
8. **m-2 pris à la lettre.** J'ai écrit « 1 à 44 » et « (au brouillon 45 : contre-lecture 10) », comme proposé pour le 45. Pour le 46, « 1 à 45 » serait complet. Ce n'est pas faux, puisque le 46 ne modifie pas le 45, mais c'est incomplet. À décider par la session.
9. **m-4 à la lettre.** « treize lignes de table » est l'en-tête de 14.57 et porte sur le brouillon 45.
10. **Lignes non touchées, faute de remarque** : 5 (« Auteur »), 6 (« Date »), la liste des notes de la ligne 9 (la note présente n'y est pas inscrite) et 10 (« Documents qui font foi »). Elles ne disent rien du 46.
11. **Fichier des règles.** Le modèle exact du brouillon 44 nomme `scripts/chef_essais_admission_bras_a_v6.py` comme programme qui applique les règles, et je l'ai gardé. Le brouillon 45 nomme `scripts/chef_essais_admission_bras_a_v12.py` (`6aa04397…`) comme le programme qui a conduit la file du juge. Je n'ai rien conçu pour trancher : à voir par la session.

## 4. Diff contrôlé par programme contre le 45

- `diff` 45 → 46 : `1c1 3c3 9c9 518c518 551c551 1462,1463c1462,1463 1483c1483 2513c2513 2518c2518 2527a2528 2540,2541c2541,2542`. Le texte passe de 2 544 à 2 545 éléments par `split("\n")`, soit 2 543 à 2 544 lignes.
- La comparaison au signe (`difflib`) ligne à ligne, avec le décalage d'une ligne après la ligne 2527, montre que rien d'autre ne bouge. Elle donne exactement les changements de la table de la partie 2.
- Parité des `**` et équilibre des « » : aucun écart sur les lignes changées.
- Validateur du dépôt (`controle_ia.prereg.problemes`) : le 45 et le 46 donnent les deux mêmes problèmes (« marqueur À REMPLIR restant hors des sections exigées » ; « contre-lecture 10 sans ses deux empreintes »). « À REMPLIR » compte 8 occurrences dans l'un et l'autre.
- Marques ⟦ ⟧ : 0.

## 5. Les huit règles d'admission

- Dans le brouillon 46, elles sont aux **lignes 542 à 550** : le titre à la ligne 542, les règles 1 à 8 aux lignes 543 à 550.
- Elles sont égales, caractère pour caractère, aux lignes 542 à 550 du 45 (`r45[541:550] == r46[541:550]`, vrai). Leur empreinte jointe est `3d1f0afe82f5aeb3bf5dd757cb6d814e19c66b93a89a65b6f08677823e1b8f96`, la même qu'aux brouillons 43 à 45.
- Aucune ligne n'est ajoutée avant elles.
- Le fichier des règles neuf est fait par `docs/notes/relance-organismes-discrets-v1/brouillon46-corrections-v1/faire_regles_brouillon46_v1.py` (`7cac96d18b8d97a1de0e744833c958444083904e075865fdfe1b35ebc89f6c85`).
  - Il est tiré du gabarit, contrôlé sur son compagnon, et la ligne d'état « gabarit » en est ôtée.
  - Le programme vérifie qu'il est égal au fichier du brouillon 44 (`cd0e384c…`), à quatre valeurs près : le titre, l'empreinte du texte en vigueur (`b5e1031c…`), le chemin du texte, et les lignes 542 à 550 (deux fois).
  - Il vérifie aussi que ses neuf lignes de règles sont égales, caractère pour caractère, aux lignes 542 à 550 du 46 : vrai.

## 6. Ce que j'ai ouvert

- **En entier** : CLAUDE.md (dans mes consignes) ; la vérification du brouillon 45 ; le gabarit du fichier des règles et le fichier des règles du brouillon 44 (par `diff` et `cat -A`).
- **En partie, par programme** : le brouillon 45, aux lignes 1, 3, 5, 6, 9 et 10 (débuts, et autour des occurrences de « 45 »), 204 à 220 (aperçu), 518, 551, 1462, 1463 et 1483, et 2505 à 2544, ainsi que par recherche de chaînes ; `src/controle_ia/prereg.py` (signature de `problemes`). Le brouillon 46 a été affiché autour des changements.
- **Non suivi** : les chemins cloisonnés que citent le 45 et la vérification. Je n'ai ouvert, listé, cherché ni empreinté aucun chemin interdit. Les empreintes abrégées des pièces citées (`9d4b8a08…`, `7bb8cc95…`, `74106c3e…`, `98581778…`, `a4e1712a…`, `213ad3db…`, `be7b0453…`) sont prises dans la vérification, sans recalcul.
- **Aucun** réseau, clé, appel de modèle, sous-agent ni commit.
