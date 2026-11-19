# Contre-lecture de la différence brouillon 12 → brouillon 13 — lecture des sondes figées sur le saboteur à budget (barreau 8) et passe de recalcul de l'activité interne — v1

## En-tête

- Brouillon relu : `brouillons/barreau8-lecture-sondes-v1/prereg-lecture-sondes-barreau8-v1-brouillon13.md`, empreinte `7628ebfd8534bd44287e0a233a80339e6dde57db88fd0ada3df3c6a1b2305cd4` (vérifiée, égale à son compagnon ; 441 lignes ; lu en entier une fois).
- Point de départ : brouillon 12, `467c2e8ba627554e454bba09dd640c3d10c5f25ed73cd7d25fcf7e491013bd5a` (vérifiée). Rapport précédent : `contre-lecture-brouillon12-v1.md`, `715cef034f1a50f604bda49b204b9117502fc228b4b111f465097a17904e2f0d` (vérifiée). Note du rédacteur : `differences-brouillon12-brouillon13-v1.md`, `7191e508b5c485080f0fd4eef99ff8f117b75252fdbb66e286f5cb8017c45d19` (vérifiée ; lue après ma propre différence, non crue).
- Contre-lecteur : Opus 5.5 (`claude-opus-5-5`), sous-agent neuf ; n'a écrit ni ce texte, ni aucune contre-lecture antérieure de ce texte, ni la note d'interface, ni aucune notice, ni aucun code. Ne connaît ni le sujet ni le mécanisme du saboteur ; le mode « coût » (seul) n'est connu que par le texte (I-10) : déclaré (décision N-054, point 3).
- Heures (`date -u`) : début 2026-11-19T04:28:32Z ; fin réelle : 2026-11-19T04:36:05Z.
- Aucun résultat du programme lu. Aucun code ni essai du barreau 8 ou du saboteur ouvert ; rien sous `registres/`, `diag/`, `runs/`, `donnees/`, `docs/verdicts/`, `scripts/`, `docs/notes/barreau8-iib-v1/`, `brouillons/ii-b-saboteur-budget-v1/` ; aucune branche ni historique git ; aucune recherche récursive. Aucun refus d'outil.

### Fichiers lus

| fichier | empreinte vérifiée | plage |
|---|---|---|
| brouillon 13 | `7628ebfd…5cd4` | en entier |
| brouillon 12 | `467c2e8b…bd5a` | par `diff`, par différence au mot près et par reconstruction programmée (point 1) |
| `contre-lecture-brouillon12-v1.md` | `715cef03…2f0d` | en entier |
| `differences-brouillon12-brouillon13-v1.md` | `7191e508…5d19` | en entier |
| `docs/notes/barreau8-cote-moniteurs-sorties-v1/contre-lecture-code-lecture-v3-integration-v1.md` | `c07e5032…0228` | titres, puis lignes 60 à 91 (point 4 « l'essai de la chaîne », point 5 « lacunes », remarques N-1 à N-5, conclusion) ; rien d'autre de ce dossier |
| `src/controle_ia/prereg.py` | `3b2e3ee5…c306` (égale à la ligne 38 du texte) | en entier |
| `src/controle_ia/scellement.py` | `93beeb1c…94ef2` | empreinte seulement (outil de scellement de ce rapport) |
| `CLAUDE.md` | — | transmis en consignes |

## Point 1 — table des blocs de la différence

`diff brouillon12 brouillon13` : `1c1 3c3 5c5 7c7 24c24 89c89 96,97c96,97 132c132 168c168 191c191 227c227 275c275 288c288 324c324 390,391c390,391 393,394c393,394 396c396 410c410 439c439,440` — **conforme à l'annonce** (22 lignes changées, 1 ajoutée).

**Reconstruction par programme.** J'ai extrait du rapport `715cef03…` lui-même (lignes 167 à 175, motif « remplacer `…` par `…` ») les neuf paires de remplacement de M-1 (a), (b), (c), m-2, m-3, m-4, m-5 (deux) et m-6 ; chaque texte cherché paraît une fois dans le brouillon 12, chaque texte de remplacement paraît une fois dans le brouillon 13. Appliquées au brouillon 12, il ne reste, entre ce texte rebâti et le brouillon 13, que les lignes 1, 3, 5, 7, 24, 89, 96-97, 168, 275, 288, 324, 391, 410 et 439-440 : **les lignes 132, 191, 227, 390, 393, 394 et 396 sont égales au caractère près ; M-1 (a), (b), (c) (qui porte m-1) et m-2 à m-6 sont portés mot pour mot.** Les phrases du rapport d'intégration ont ensuite été extraites de ce rapport par programme (lignes 65, 68 à 73) et cherchées dans le brouillon 13 (table du point 2).

| bloc | objet | changement | origine | verdict |
|---|---|---|---|---|
| 1c1, 3c3 | titre, statut | « 12 » → « 13 » | en-tête | juste |
| 5c5 | contre-lecteurs | « ; contre-lecteur du brouillon 12 : Opus 5.5 » | en-tête | juste |
| 7c7 | date | « ; brouillon 13 écrit entre 04:24Z et 04:26Z » | en-tête | juste |
| 24c24 | sources | code de la passe « version 4 », de la lecture « version 3 » ; rapport du brouillon 12, rapport d'intégration et notice de la passe v4 cités avec leurs empreintes | en-tête | juste ; les deux premières empreintes vérifiées par moi ; la troisième (`66f1e6c1…06db`) non vérifiée (fichier hors de ma liste) |
| 89c89 | D-4 | phrase de la première cellule | phrase 5.6 | mot pour mot (point final absorbé par la cellule) |
| 96c96 | D-11 | quatre lignes et leur raison ; entropie et cellule de F-3 | phrases 5.1, 5.2 | mot pour mot |
| 97c97 | D-12, `run_id` | « comparée à rien » remplacée : comparée au seul nom de la course de la trace, refus de la lecture s'ils diffèrent | O-1, demandé par la conductrice | juste (point 3) |
| 132c132 | « Métrique », intervalle | blocs d'un jeu | m-3 | mot pour mot |
| 168c168 | plan, point 3 | refus si le nom de la course de la trace diffère de `run_id` de l'extrait | O-1 | juste (point 3) |
| 191c191 | « Qui fait quoi » | nul n'ouvre les fichiers 1, 2 et 4 du côté exposé | m-6 | mot pour mot ; remarque R-2 |
| 227c227 | retour (b-5) | marques de gras ; retrait de l'égalité et de sa clause d'échec | m-5, M-1 (c) | mot pour mot ; **incomplet après B-1** : remarque R-1 |
| 275c275 | garde r4 | « type seulement » : la garde de réception contrôle le type, la lecture exige l'égalité | O-1 | juste (point 3) |
| 288c288 | P0 | phrase de la première cellule | phrase 5.6 | mot pour mot |
| 324c324 | règle mécanique des sondes lues | clé et nom ; « une direction de plus » ; finitude | phrases 5.5, 5.4 (adaptée), 5.3 | juste ; observation O-1 |
| 390c390 | chapeau de l'essai | égalité des deux chemins ; générateur nommé | M-1 (a), m-1 | mot pour mot |
| 391c391 | essai (i) | tâche réduite à une classe | phrase du point 4 (adaptée) | juste (point 2) |
| 393c393 | essai (iii) | permutation fixée | m-2 | mot pour mot |
| 394c394 | règle d'échec | égalité des deux chemins | M-1 (b) | mot pour mot |
| 396c396 | limite déclarée | | m-4 | mot pour mot |
| 410c410 | liste d'arrêt, ligne 3 | `run_id` de l'extrait différent du nom de la course de la trace | O-1 | juste |
| 439c439,440 | entrées 3 septies et 3 octies | renvoi corrigé (« contre-lue par l'entrée 3 octies ») ; entrée ajoutée | en-tête | juste ; empreintes exactes |

**Aucun changement hors de ces blocs.**

## Point 2 (de la commande, 1) — table M-1, m-1 à m-6, O-1, phrases d'intégration

| point | porté ? | où | contradiction ? |
|---|---|---|---|
| M-1 (a) | mot pour mot | l. 390 | non |
| M-1 (b) | mot pour mot | l. 394 | non |
| M-1 (c) | mot pour mot | l. 227 | non ; mais le retour ne couvre pas la phrase ajoutée par B-1 (R-1) |
| m-1 | mot pour mot (dans M-1 (a)) | l. 390 | non |
| m-2 | mot pour mot | l. 393 | non |
| m-3 | mot pour mot | l. 132 | non |
| m-4 | mot pour mot | l. 396 | non |
| m-5 | mot pour mot (deux remplacements) | l. 227 | non |
| m-6 | mot pour mot | l. 191 | non ; lecture littérale de « ouvrir » (R-2) |
| O-1 (observation devenue ajout) | quatre endroits : D-12 (l. 97), plan point 3 (l. 168), r4 (l. 275), liste d'arrêt 3 (l. 410) ; « comparée à rien » n'existe plus ; « type seulement » ne reste qu'à r4, réécrit | — | non (point 3) |
| phrase du point 4 (tâche réduite à une classe) | portée avec **deux** adaptations : (i) fin « l'essai n'échoue que par l'égalité des deux chemins non tenue, (a) ou (b) », déclarée et juste ; (ii) renvoi « (elle reste un bloc : « Métrique », « Intervalle ») », déclaré dans la note des différences (B-1) mais non dans la commande ; juste, il ne fait que renvoyer à m-3 | l. 391 | non |
| 5.1 (quatre lignes, avec la raison) | mot pour mot | l. 96 | non (point 4) |
| 5.2 (ni entropie, ni cellule de F-3) | mot pour mot (point final absorbé par la cellule) | l. 96 | non |
| 5.3 (finitude) | mot pour mot | l. 324 | non ; observation O-1 |
| 5.4 (« une direction de plus ») | mot pour mot, précédée de « Pour la tromperie et les enjeux élevés : » (« Une » devient « une ») | l. 324 | non : juste, la dissimulation n'a pas de préfixe de nom dans le texte (table des identités : « les 800 entrées de l'index de famille « plancher » ») et garde sa règle « 800 entrées, toutes couches comptées » |
| 5.5 (clé et nom de la sonde décisive) | mot pour mot | l. 324 | non |
| 5.6 (première cellule) | mot pour mot, aux deux endroits | l. 89 (D-4), l. 288 (P0) | non ; observation O-2 |

## Point 3 (de la commande, 2) — l'essai de la chaîne, lignes 390 à 396, lu comme un tout

**(a) L'égalité des deux chemins.**
- *Ce qui est comparé* : pour chaque sonde lue (les trois sondes décisives que la règle mécanique rend « lues ») et chaque action de `H` d'au moins un jeton noté, la valeur du tableau des scores par action livré (fichier 1, `scores`), **case 0** (`"maximum (production)"`), colonne de la sonde (rôle « sonde » dans `directions`), ligne désignée par la clé, **lue par la fonction même de la lecture décisive** — contre le maximum, recalculé par l'essai, du segment de la colonne de la sonde du tableau des scores par jeton (fichier 2), segment borné par les sommes cumulées de `jetons_notes` dans l'ordre de `rang`.
- *Bornes* : entièrement définies. La l. 262 dit que les bornes d'une action sont les sommes cumulées de `jetons_notes` ; la l. 245, que les actions sont dans l'ordre de l'index, les jetons dans l'ordre de l'action, et qu'une action sans jeton noté n'a aucune ligne (sa contribution à la somme est nulle) ; la l. 263, que `rang` est le rang dans l'ordre du fichier, égal à l'ordre des lignes de l'index. Les sommes portent sur **toutes** les lignes de l'index (toutes conditions), non sur les seules actions de `H` : c'est la seule lecture compatible avec la l. 262 ; observation O-3.
- *« Exacte » est-il possible ?* Oui. Le maximum ne fait aucun arrondi : il choisit un des nombres. La l. 245 exige que « le maximum et la moyenne du tableau des scores par action sont calculés à partir de ces mêmes nombres » (les scores par jeton stockés), en `float64`, une seule fois sur la carte ; les copies vers le disque et le format `npz` sans compression sont exactes. La seule différence possible au bit près serait un zéro de signe opposé (`-0.0` contre `0.0`), que l'égalité numérique tient pour égaux ; « égal, sans tolérance » se lit en égalité de nombres, comme à r7. Aucune raison qu'un bit diffère si le texte est suivi ; s'il ne l'est pas (scores par jeton recalculés une seconde fois sur la carte), r7 refuse déjà la livraison.
- *Inégalité* : échec de A0, sans rejeu ; la sortie écrit la sonde et le nombre d'actions inégales, jamais un score ; puis ligne L5 (l. 395). Cohérent.

**(b) Double emploi ou contradiction avec r7 ?** Ni l'un ni l'autre ; les deux se complètent et r7 passe d'abord.
- *r7 voit, A0 non* : les 2 560 actions, les quatre conditions, les neuf sondes (couches 7 et 23 comprises), la moyenne ; un défaut de la **livraison** (tableaux incohérents entre eux). Elle passe par les fonctions de la garde de réception, non par celle de la lecture décisive.
- *A0 voit, r7 non* : un défaut du **code de la lecture décisive** dans son accès au tableau des scores par action — colonne fausse (une direction de plancher prise pour la sonde, une autre sonde), case 1 lue pour la case 0, association fausse des lignes aux clés — sur `H` et les trois sondes lues.
- *Ni l'un ni l'autre* : un accès faux aux colonnes **de plancher** par la lecture décisive (r6 les compare au brut avec ses propres fonctions, A0 ne compare que la sonde), et un accès faux propre à une autre condition que `H` (l'essai ne lit que `H`, limite déjà déclarée l. 396). Tenu par le contrôle de conformité seul ; observation O-4.
- Comme r7 refuse toute livraison où les deux tableaux ne s'accordent pas, une inégalité de A0 ne peut venir que du code de la lecture : l'échec (L5, « chaîne de lecture non validée ») est le bon nom.

**(c) Règle d'échec unique ?** Oui. Elle est écrite une fois, l. 394 (« si et seulement si l'égalité des deux chemins n'est pas tenue, ou si (a) …, ou (b) … ») ; les l. 390 (« une seule inégalité fait échouer A0, sans rejeu ») et 391 (« l'essai n'échoue que par l'égalité des deux chemins non tenue, (a) ou (b) ») la redisent sans rien ajouter ; la règle des blocs (l. 132) ne crée aucune cause d'échec propre à l'essai : une tâche à une classe reste un bloc ; seule la garde « plus de 1 % de tirages à une classe » peut rendre un « échec », qui n'est une cause de A0 que par (b) (artefact (ii) non au-dessus) — c'est ce que dit « n'échoue que par … (a) ou (b) ». La l. 395 (« A0 échoue au sens ci-dessus … : ligne L5 ») et la ligne L5 de la table s'accordent. La remarque N-1 du rapport d'intégration (cause d'échec ajoutée par le code) est fermée côté texte.

**(d) Reste-t-il un choix au code ?** Non, hors de deux points sans effet sur l'issue : la fonction et l'ordre du tirage du jeton injecté (sans effet : porter n'importe quel jeton au maximum plus 2 s donne le même maximum ; le rééchantillonnage reçoit la graine entière « telle quelle », donc ne dépend pas du nombre de tirages consommés) ; et le sens de « rang » en (iii), où « l'action de rang k » ne peut désigner que la position k dans la liste des n actions de `H` (les éléments de `permutation(n)` vont de 0 à n − 1 ; le champ `rang` de l'index va jusqu'à 2 559) : lecture unique. Ordre des tâches, générateur (`numpy.random.default_rng(graine)`, un seul par essai, tâche par tâche dans l'ordre du tri des chaînes de Python), `permutation(10)`, moment du retrait (après le tirage des étiquettes), liste et fonction de la permutation de (iii) : écrits.

**(e) Retour à l'option sans scores par jeton.** **Incomplet.** Le passage (b-5) retire la phrase de l'égalité et la clause « l'égalité des deux chemins n'est pas tenue, ou si » de la règle d'échec, mais pas la fin de la phrase ajoutée en (i) par l'adaptation (i) de B-1 : sous (a), le texte dirait encore « l'essai n'échoue que par l'égalité des deux chemins non tenue, (a) ou (b) », qui renvoie à une règle retirée. Le reste du retour s'applique (chaque chaîne citée paraît une fois, marques de gras comprises). Remarque R-1.

## Point 4 (de la commande, 3) — le refus sur le nom de la course

- *Quatre endroits, cohérents* : D-12 (l. 97 : `run_id` « n'est comparée qu'au nom de la course porté par la trace de la passe, à l'ouverture de la lecture, qui refuse de tourner s'ils diffèrent (plan, point 3) ») ; plan, point 3 (l. 168, refus et raison) ; r4 (l. 275 : la garde de réception ne contrôle que le type des deux valeurs ; l'égalité est exigée à l'ouverture de la lecture, où trace et extrait sont lus ensemble) ; liste d'arrêt, ligne 3 (l. 410 : la lecture refuse, fait porté à la session mère). Ce que disent encore la l. 97 (« elle n'entre dans aucune règle de lecture ») et la l. 154 (« sans effet sur le verdict ») reste vrai : c'est une condition d'ouverture, non une règle de lecture.
- *Mêmes sources ?* D'après le texte : le nom de la trace vient de l'extrait du côté exposé (D-13 : `run_id`, forme `AAAAMMJJ-HHMMSS-…`, « écrits au manifeste et dans la trace » ; trace, l. 256 et clé `course`, l. 265) ; celui de l'extrait des états est écrit par le programme du côté exposé (D-12), chaîne libre d'au plus 200 caractères. Le texte ne dit pas que ce programme écrit le même nom de la course, au caractère près : il le suppose (titre « nom de la course (extrait des états) »). Si les deux sont bien le nom de la course, le refus ne joue que sur une vraie confusion de courses — ce qu'il doit faire. S'ils différaient d'écriture pour une même course, le refus ne serait levable que par un écart (une seule ligne `ETATS-COURSE-IIB`, l. 304) : risque de blocage, non de mauvaise lecture. Observation O-5 : à confirmer auprès du côté exposé avant le scellement ; aucun changement de texte exigé.
- *Réception seule* : elle ne lit pas l'extrait ; r4 n'y contrôle que le type ; l'égalité est explicitement portée par « l'ouverture de la lecture ». Dispense sans contradiction.

## Point 5 (de la commande, 4) — les autres phrases

- **Réception seule.** Les quatre lignes exigées (`SCELLEMENT-SONDES-IIB`, `CODE-PASSE-IIB`, `CODE-LECTURE-SONDES-IIB`, `LIVRAISON-PASSE-IIB`) et la raison de la deuxième (r4 compare la trace au bordereau de `CODE-PASSE-IIB`) s'accordent avec les conditions d'ordre (l. 305 : `LIVRAISON-PASSE-IIB` après `CODE-PASSE-IIB` ; `CODE-LECTURE-SONDES-IIB` « avant toute lecture et avant toute réception de la livraison ») ; ce que le brouillon 12 exigeait (texte scellé, modules exactement ceux du bordereau du code de la lecture, avant d'ouvrir quoi que ce soit) est gardé tel quel. « Ni entropie ni cellule de F-3 » : cohérent avec le plan, point 5 (seuls la lecture et la recette de puissance reçoivent l'entropie) ; la réception ne tire aucune graine.
- **Finitude.** Portée exacte (toute entrée au nom de l'une des neuf sondes, toute candidate au plancher, avant toute autre condition, que la sonde soit ensuite lue ou non) ; cohérente avec P1, le plan point 3 et la liste d'arrêt 8 (arrêt et refus, jamais « sans objet »). « Avant toute autre condition » ne peut s'entendre qu'après la présence et l'empreinte du fichier, que `lire_sondes` contrôle en le lisant : observation O-1 (aucun effet sur l'issue : les deux causes arrêtent).
- **« Une direction de plus »** : règle unique pour la tromperie et les enjeux élevés (tout nom au préfixe, hors des 800 noms sans zéro de tête, quelles que soient famille et couche), plus large que l'exemple de la phrase précédente (« un nom `<préfixe>-plancher-<k>` hors de 0 à 799 ») qu'elle complète sans le contredire ; la dissimulation garde « 800 entrées de famille « plancher », toutes couches comptées ». Les deux côtés appliquent la même règle (l. 324, « une seule règle, pour la passe et pour la lecture »).
- **Clé et nom de la sonde décisive** : la sonde est l'entrée de rang k sous la clé `s<k>_w` de la table, portant le nom de la table, nom unique dans l'index ; sinon « sans objet ». Cohérent avec la condition (ii) et avec la liste d'arrêt 8 (un nom des couches 7 ou 23 en double arrête ; un nom décisif en double rend « sans objet »). Le code de la passe est à aligner (note des différences, D, passe 1) : c'est au contrôle de conformité.
- **Première cellule** : même phrase en D-4 et P0, règle « une ligne et une seule » gardée ; cohérente. Observation O-2.
- **« Du côté exposé, nul n'ouvre les fichiers de scores »** : compatible avec ce que la passe fait elle-même (écrire, découper, mesurer par P9, écrire les compagnons et le bordereau : « autre que le code de la passe »). Mais le transport (la livraison « passe par le dépôt, en morceaux », l. 194) et toute vérification d'empreinte par l'exécutante font ouvrir ces fichiers par un programme qui n'est pas le code de la passe ; la convention du texte (plan, point 3 ; D-6 : contrôler l'existence et l'empreinte n'est pas « ouvrir ») l'excuse par analogie seulement. Remarque R-2.

## Point 6 (de la commande, 5) — aucun changement de fond

Hypothèse (l. 100 à 108), prédictions B8-P1 à B8-P7 (l. 110 à 126), « Métrique » hors de l'ajout m-3 (qui décrit le comportement de `intervalle_blocs` sans changer de calcul), « Seuil », niveaux, règle du témoin-jumeau, états, état agrégé, table des issues S1 à AU-b (l. 360 à 376) : **intacts** (aucun bloc de la différence ne les touche). Le refus sur le nom de la course ajoute une condition d'ouverture et une ligne à la liste d'arrêt 3, sans toucher une règle de lecture. Bloc « Noms et champs, liste fermée » (du titre à « Fichiers non lus avant ») : **identique au caractère près** à celui du brouillon 12 (`True`, 5 551 caractères).

## Point 7 (de la commande, 6) — validateur

`PYTHONPATH=src .venv/bin/python` → `prereg.problemes("…brouillon13.md")` : `['section vide ou à remplir : Contre-lecture']`.
Marqueurs « À REMPLIR » : exactement deux, lignes **76 et 441**. Ligne 76 **identique octet pour octet** à celle du brouillon 12 (`True`) : `| F-3 | entropie racine des graines | À REMPLIR — À FIXER : tirée par la session mère au scellement |`. Chaînes de la procédure, chacune une fois : `À REMPLIR — À FIXER : tirée par la session mère au scellement` ; `- **Contre-lecture 4 (finale, texte rempli)** — À REMPLIR :` ; `versée avec l'empreinte du texte scellé.`. Entrée « Contre-lecture 3 octies » : empreintes `467c2e8ba627554e454bba09dd640c3d10c5f25ed73cd7d25fcf7e491013bd5a` (brouillon 12) et `715cef034f1a50f604bda49b204b9117502fc228b4b111f465097a17904e2f0d` (rapport), exactes et distinctes ; motif `ENTREE` du validateur sur le texte rempli d'essai : `1, 2, 3, 3, 3, 3, 3, 3, 3, 3, 4` (la huitième « 3 » est l'octies) ; aucune entrée ne manque de ses deux empreintes.

## Point 8 (de la commande, 7) — essai de la procédure sur copies

Dossier temporaire `/tmp/claude-0/-home-user-controle-ia-travail/ccd98af0-e97a-5c3c-8902-30e463468b85/scratchpad/verif13/` (scripts `proc.py`, `gabarit.txt`). Entropie d'essai `123456789012345678901234567890123456789` ; ligne 441 remplacée entière par le gabarit de la procédure ci-dessous, empreinte d'essai du rapport `222…2` (64 caractères) : deux empreintes distinctes.

| copie | `problemes` | `diff` avec le brouillon 13 |
|---|---|---|
| sain : entier seul + entrée 4 | `[]` | `['76c76', '441c441']` — exactement ces deux lignes ; ligne 76 : `| F-3 | entropie racine des graines | 123456789012345678901234567890123456789 |` |
| artefact : entropie laissée ouverte | `['marqueur À REMPLIR restant hors des sections exigées']` | — |
| artefact : entrée 4 sans l'empreinte du rapport | `['contre-lecture 4 sans ses deux empreintes (brouillon relu et rapport)']` | — |

Les deux remplacements de la conclusion (R-1, R-2), appliqués ensemble à une copie (`remplacements.py`) : chaque texte cherché paraît une fois ; aucun saut de ligne ajouté ; validateur `['section vide ou à remplir : Contre-lecture']` ; marqueurs aux lignes 76 et 441.

## Remarques neuves

- **R-1. À CORRIGER — le retour à l'option sans scores par jeton n'est plus complet.** Passage : (b-5), l. 227 ; phrase visée, essai (i), l. 391. Défaut : l'adaptation (i) de B-1 a ajouté en (i) « l'essai n'échoue que par l'égalité des deux chemins non tenue, (a) ou (b) » ; (b-5) retire l'égalité et sa clause d'échec, non cette fin de phrase ; sous (a), le texte renverrait à une règle retirée, et le retour dit « mécanique » ne le serait plus. Défaut si non corrigé : un passage à (a) avant le scellement laisserait une contradiction (que la contre-lecture prévue de ce passage aurait à voir) ; sous (b), aucun effet. **TEXTE DE REMPLACEMENT** (le texte cherché paraît une fois, vérifié) : remplacer `est retiré de la règle d'échec ; tout le reste de l'essai` par `est retiré de la règle d'échec ; en (i), « l'essai n'échoue que par l'égalité des deux chemins non tenue, (a) ou (b) » devient « l'essai n'échoue que par (a) ou (b) » ; tout le reste de l'essai`.
- **R-2. MINEURE — « ouvrir », du côté exposé, pris à la lettre, interdit le transport.** Passage : « Qui fait quoi », l. 191 (texte de m-6). Défaut : le dépôt des morceaux, leur copie et toute vérification d'empreinte par l'exécutante sont faits par des programmes autres que le code de la passe, qui ouvrent ces fichiers ; seule l'analogie avec le plan, point 3, les excuse. Défaut si non corrigé : un écart déclarable à la livraison, ou une hésitation de l'exécutante. **TEXTE DE REMPLACEMENT** (le texte cherché paraît une fois, vérifié) : remplacer `n'ouvre les fichiers 1, 2 et 4 de la livraison ni n'en lit un score, avant comme après leur envoi.` par `n'ouvre les fichiers 1, 2 et 4 de la livraison ni n'en lit un score, avant comme après leur envoi ; les copier, les déposer, les transmettre et en calculer l'empreinte, sans en décoder le contenu, n'est pas les ouvrir au sens de cette phrase (comme une pièce dont seules l'existence et l'empreinte sont contrôlées n'est pas ouverte : plan, point 3).`

Observations, sans correction exigée :
- **O-1.** Finitude « avant toute autre condition » : elle ne peut venir qu'après la présence et l'empreinte entière du fichier (contrôlées par `lire_sondes` en le lisant) ; les deux causes arrêtent la passe et font refuser la lecture : seule la cause écrite peut différer.
- **O-2.** Première cellule de la ligne d'accord : une cellule de tableau porte des espaces de bord ; les deux codes les retirent (rapport d'intégration, 5.6), lecture naturelle de « l'identifiant seul ». Risque signalé par ce rapport, que je reprends : si le vrai registre des accords met ses identifiants en gras ou entre accents graves, la passe et la lecture refuseront, et le changement serait un écart après le scellement ; la session mère peut le vérifier avant.
- **O-3.** Bornes de l'égalité des deux chemins : sommes cumulées sur toutes les lignes de l'index (l. 262), non sur les seules actions de `H` ; seule lecture compatible, à relire au contrôle de conformité.
- **O-4.** L'accès de la lecture décisive aux colonnes de plancher, et aux lignes des conditions autres que `H`, n'est éprouvé ni par A0 ni par r6 ou r7 (qui passent par leurs propres fonctions) : tenu par le contrôle de conformité seul.
- **O-5.** `run_id` de l'extrait des états : le texte suppose, sans le dire, qu'il est écrit au caractère près comme le `run_id` de l'extrait du côté exposé (D-13) ; à confirmer par la session mère auprès du côté exposé avant le scellement ; sinon un refus non levable sans écart.
- **O-6.** (Antérieur à cette différence.) Le retour (b-2) cite « Pour les neuf sondes, les scores par jeton sont livrés aussi … sur toutes les actions. » sans les marques de gras qui l'entourent (l. 130) ; son application laisserait une paire `****` vide, sans effet sur le sens.

## Procédure de remplissage mise à jour (pour la session qui scelle)

Elle vaut pour le brouillon 13, `7628ebfd8534bd44287e0a233a80339e6dde57db88fd0ada3df3c6a1b2305cd4`, s'il est scellé sans autre changement (sur le mot de la session mère ou de Lazar écartant R-1 et R-2 ; la conclusion citée devient alors celle que dit l'étape 4). Un brouillon 14 qui porterait R-1, R-2, son en-tête et une entrée « Contre-lecture 3 nonies » déplacerait l'entrée 4 à la ligne 442 : sa procédure est à revérifier par son contre-lecteur. Les chaînes ci-dessous sont uniques dans le brouillon 13 (vérifié).

1. Vérifier l'empreinte du brouillon 13 ; le copier, octet pour octet, au chemin de scellement choisi par la session mère (nom versionné neuf, R12), qu'elle inscrira à la ligne `SCELLEMENT-SONDES-IIB`.
2. Tirer l'entropie **une seule fois**, sans essai préalable : `PYTHONPATH=src .venv/bin/python -c "import numpy as np; print(np.random.SeedSequence().entropy)"` ; consigner **hors du texte**, avec le versement (étape 5), la commande, la version de numpy et l'heure UTC.
3. **Premier remplacement (ligne 76, cellule « état et raison » de F-3)** : remplacer la chaîne exacte
   `À REMPLIR — À FIXER : tirée par la session mère au scellement`
   par **l'entier décimal tiré, seul, sans séparateur** (aucun autre mot, aucune parenthèse, aucune espace insécable ; plan, point 5). La ligne devient `| F-3 | entropie racine des graines | <entier décimal> |`.
4. **Second remplacement (ligne 441)** : remplacer la ligne entière qui commence par `- **Contre-lecture 4 (finale, texte rempli)** — À REMPLIR :` et finit par `versée avec l'empreinte du texte scellé.` par cette seule ligne, où le **seul emplacement à remplir** est `<EMPREINTE DU RAPPORT>`, l'empreinte de ce rapport (`brouillons/barreau8-lecture-sondes-v1/contre-lecture-brouillon13-v1.md`), donnée dans le message qui le rend et dans son compagnon `contre-lecture-brouillon13-v1.md.sha256` (sans chevrons dans le texte final). Ce rapport conclut « PAS PRÊT » : si le brouillon 13 est scellé tel quel, la session mère écrit, à la place de la phrase entre guillemets qui suit « Conclusion : », « PAS PRÊT, R-1 et R-2 écartées, scellé sur le mot de Lazar (ligne d'accord citée) », et le versement le dit :
   `- **Contre-lecture 4 (finale, texte rempli)** — sous-agent neuf, modèle Claude Opus 5.5, qui n'a écrit ni ce texte, ni aucune contre-lecture antérieure de ce texte, ni la note d'interface, ni aucune notice, ni aucun code ; contre-lecture de la différence du brouillon 12 au brouillon 13 (dont l'égalité des deux chemins de l'essai de la chaîne, le refus sur le nom de la course et les phrases du second essai d'intégration). Brouillon relu : `brouillons/barreau8-lecture-sondes-v1/prereg-lecture-sondes-barreau8-v1-brouillon13.md`, empreinte `7628ebfd8534bd44287e0a233a80339e6dde57db88fd0ada3df3c6a1b2305cd4`. Rapport : `brouillons/barreau8-lecture-sondes-v1/contre-lecture-brouillon13-v1.md`, empreinte `<EMPREINTE DU RAPPORT>`. Conclusion : « PRÊT : le brouillon 13 peut être scellé une fois l'entropie des graines versée et cette entrée de contre-lecture portée au texte, sans autre changement ». **Règle** : le texte scellé ne diffère du texte relu par cette contre-lecture que par cette entrée et par la cellule « état et raison » de F-3, où seule l'entropie tirée remplace le marqueur ; la session mère le vérifie par une comparaison faite par programme, versée avec l'empreinte du texte scellé.`
   (La ligne commence par `- **Contre-lecture 4` pour le motif du validateur, porte deux empreintes distinctes et aucun « À REMPLIR » ; essayée sur copie, point 8.)
5. Comparaison faite par programme (`diff`) entre le brouillon 13 et le texte rempli : **exactement `76c76` et `441c441`**, rien d'autre ; la verser avec l'empreinte du texte scellé et la provenance de l'entropie.
6. `prereg.problemes(<texte rempli>)` doit rendre `[]` ; essai de cette garde sur le cas sain (le texte rempli) et sur deux artefacts (entropie restée ouverte : attendu `['marqueur À REMPLIR restant hors des sections exigées']` ; entrée 4 sans l'empreinte du rapport : attendu `['contre-lecture 4 sans ses deux empreintes (brouillon relu et rapport)']`), versé (R5) ; puis `sceller_prereg` ; puis la ligne `SCELLEMENT-SONDES-IIB` ; l'heure de scellement consignée à côté de l'heure de la première sortie de la course (D-7).

## Conclusion

PAS PRÊT : liste fermée des corrections, à porter en un brouillon 14 dont la différence est contre-lue avant le scellement :
1. R-1 (à corriger) : le retour (b-5) couvre la fin de phrase ajoutée en (i) (l. 227) ;
2. R-2 (mineure) : « ouvrir », du côté exposé, n'interdit pas la copie, le dépôt et l'empreinte (l. 191) ;
3. en-tête, date, liste des contre-lecteurs et entrée « Contre-lecture 3 nonies » citant ce rapport, comme aux brouillons précédents.

Tout le reste de la différence est porté exactement : M-1 (a), (b), (c), m-1 à m-6 mot pour mot (rebâtis par programme), les phrases du second essai d'intégration avec leurs adaptations justes, le refus sur le nom de la course cohérent à ses quatre endroits, aucun changement de fond. Si la session mère ou Lazar écartent R-1 et R-2, le brouillon 13 est scellable par la procédure ci-dessus, avec la mention « PAS PRÊT, R-1 et R-2 écartées, scellé sur le mot de Lazar ».

## Refus d'outil

Aucun.

Fin réelle : 2026-11-19T04:36:05Z (dernier `date -u` avant le scellement de ce rapport).
