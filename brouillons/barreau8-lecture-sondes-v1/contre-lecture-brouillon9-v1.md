# Contre-lecture de la différence brouillon 8 → brouillon 9 — lecture des sondes figées sur le saboteur à budget (barreau 8) et passe de recalcul de l'activité interne — v1

## En-tête

- Brouillon relu : `brouillons/barreau8-lecture-sondes-v1/prereg-lecture-sondes-barreau8-v1-brouillon9.md`, empreinte `aca110b0635abf9e7e5a1bdd1dc66b94aaae40ad5c72a6e7d6127967f87f272d` (vérifiée ; 428 lignes).
- Point de départ : brouillon 8, `d8992b575a4e03fa6647b7d5af663596f80870925164b328adc0985c29f98b3a` (vérifiée). Rapport précédent : `contre-lecture-brouillon8-v1.md`, `94aaa09187c9631d2898ae50c8ccc7ec420ece9e71df5068a186aca516ad5e86` (vérifiée).
- Contre-lecteur : Opus 5.5 (`claude-opus-5-5`), sous-agent neuf : n'a écrit ni ce texte, ni aucune contre-lecture antérieure de ce texte, ni la note d'interface, ni la notice, ni la note des lacunes, ni aucun code ; ne connaît ni le sujet ni le mécanisme du saboteur. Le mode « coût » (seul) est connu par le texte et la note d'interface (question 10) : déclaré (décision N-054, point 3).
- Heures (`date -u`) : début 2026-11-19 02:03:09 UTC ; fin réelle 2026-11-19 02:11:10 UTC (dernier `date -u` avant le scellement de ce rapport).
- Aucun résultat du programme lu ; aucun code ni essai de `barreau8_moniteurs` ou `iib` ouvert ; aucun fichier de `registres/`, `diag/`, `runs/`, `donnees/`, `docs/verdicts/`, `scripts/` ; aucune branche ni historique git. Aucun refus d'outil.

### Fichiers lus, avec plages

| fichier | empreinte vérifiée | plage |
|---|---|---|
| brouillon 9 | `aca110b0…f272d` | en entier (1 à 428) |
| brouillon 8 | `d8992b57…98b3a` | par `diff` seulement (et sa ligne 75, par programme) |
| `differences-brouillon8-brouillon9-v1.md` | `748aea8b…77cd3` | en entier |
| `lacunes-texte-developpeur-lecture-v1.md` | `8f482f4d…5dc49` | en entier |
| `contre-lecture-brouillon8-v1.md` | `94aaa091…5e86` | lignes 1 à 12 et 66 à 115 (procédure, conclusion) |
| `docs/notes/barreau8-cote-moniteurs-sorties-v1/notice-passe-recalcul-v1.md` | `45da9b99…aa472` | lignes 84 à 104 (« Entrées attendues », fin : registre, bordereau du code, extrait ; puis « Livraison ») et 140 à 159 (« Écarts ou lacunes ») ; plus les lignes rendues par une recherche de `texte_scelle|accord_lecture|répét|76cdeace|extrait` (9, 16, 24, 54, 65, 76 à 78, 111, 112) : intitulés et table des entrées, sans mécanisme. Les lignes 84 à 88 sont hors des deux sections nommées par la consigne : lues parce que le texte (D-13) cite « notice de la passe, « Entrées attendues » » et que le point 4 de la consigne demande la comparaison à la notice ; déclaré |
| `docs/notes/barreau8-cote-moniteurs-entrees-v1/interface-passe-cote-moniteurs-v6.md` | `20c9ed6e480646b6bf3a5f6007be5f88b439c916763a618f3880634e92ad8ce1` | intitulés de sections ; ligne 89 (point (b) : empreinte des tâches d'évaluation) en extrait ; extraits des lignes 76 et 108 rendus par une recherche de motif (« iib », « extrait_cote ») pour vérifier les noms de fichiers ; aucun renvoi suivi, aucune pièce du point (e) ouverte |
| `src/controle_ia/prereg.py` | — | en entier |

## Point 1 — table des blocs de la différence (faite par programme)

`diff brouillon8 brouillon9` : 45 lignes retirées, 59 ajoutées, soit **45 lignes changées et 14 ajoutées** (23a24 : 1 ; 257a259,268 : 10 ; 293c304,306 : 1 → 3, soit 2 ; 413a427 : 1). Conforme à l'annonce.

| bloc (b8 → b9) | objet | point | verdict |
|---|---|---|---|
| 1c1, 3c3 | titre, statut « brouillon 9 » | hors des 32, déclaré | juste |
| 5c5 | contre-lecteur du brouillon 8 « désigné par la conductrice » | hors, déclaré | juste |
| 7c7 | date du brouillon 9 | hors, déclaré | juste |
| 23a24 | sources : notice et note des lacunes, empreintes | hors, déclaré | juste (empreintes exactes) |
| 85,86c86,87 | D-1, D-2 : lignes de code citent un bordereau | P-3, L-17 | juste |
| 89,90c90,91 | D-5 (mandats), D-6 (pièce de comparaison) | L-12 | juste, mot pour mot |
| 97c98 | D-13 : forme fermée de l'extrait du côté exposé | P-1 | juste ; égal à la notice et à la note des lacunes (point 4) |
| 117c118 | B8-P3 : « échec » si tâches différentes ou classes manquantes | L-8 | juste (précision, descriptive) |
| 131c132 | intervalle : classe vide = « échec » | L-8 | juste (précision) |
| 137c138 | sonde des couches 7 ou 23 d'une autre famille : écart, arrêt et refus | L-16 (et P-4) | juste ; durcissement déclaré (point 2) |
| 155c156 | aires « hors jugement » : intervalle, niveau, graine | L-5 | juste |
| 167,169c168,170 | plan 3 (règle des sondes à la réception), 4 (A0 étape de la commande), 5 (forme de F-3 ; `injection-adaptateurs`) | L-2, L-19, L-13, P-10 | juste |
| 175c176 | recette : round(f × 640) sans remise | L-11 | juste |
| 180,181c181,182 | recette : graines, contrôle du budget, deux issues rapportées | L-11 | juste |
| 209c210 | décision de taille : fichiers ajoutés, réserve P9 | hors, « phrase de taille » + ajout (c) | **à corriger** (R-2) |
| 237c238 | passe avant : lots sur actions notées ; ordre des conditions | P-13 | juste |
| 243c244 | liste des directions : sonde non conforme aux couches 7 et 23 arrête la passe | P-4, L-16 | juste |
| 255c256 | trace : `course`, taille des fichiers 1 à 4, trace d'arrêt | P-9 | juste |
| 257a259,268 | bloc « Noms et champs, liste fermée » et taille | P-11, L-1 ; ajout (c) | noms exacts ; **à corriger** (R-3) |
| 262c273 | r2 : compagnons, archives rebâties, somme des tailles | L-14, L-1 | juste |
| 264c275 | r4 : modules « exactement » ; adaptateur et dose ; état des sondes | hors (garde des modules), L-4, L-2 | juste |
| 268c279 | r8 : écart-type de population | L-15 | juste |
| 277,278c288,289 | P0 (bordereau, accord), P1 (extrait, tâches, arrêt des sondes) | P-3, P-1, P-2, P-4 | juste |
| 280c291 | P3 : clause (d), « (a) à (d) » | P-12 | juste |
| 284-287c295-298 | P7, P8, P9, P10 | P-7, P-5, P-6, P-8 | P7, P9, P10 justes ; **P8 bloquante** (R-1) |
| 293c304-306 | forme du registre ; conditions d'ordre ; deux bordereaux | L-17, L-18, P-3 ; ajout (a) | juste ; **mineure** (R-4) |
| 295c308 | refus mécanique contre le bordereau | P-3, L-17 | juste |
| 311c324 | règle mécanique : fichier absent = arrêt et refus | L-2, P-4 | juste (point 2) |
| 339c352 | chapeau de la table : S et A0 | L-9 | juste, mot pour mot |
| 345,346c358,359 | S3 lignes de mémoire ; S4 | L-3 ; ajout (b) | juste (point 2 pour S4) |
| 360c373 | réserve de dissimulation, « toute issue » | L-10 | juste (point 2) |
| 369c382 | A0 : graine de l'essai | L-6 | juste, mot pour mot |
| 371c384 | A0 (ii) : écart-type de population | L-6 | juste |
| 377,378c390,391 | audit : niveaux des déclencheurs ; contenu (1) | L-7 ; hors, déclaré | juste |
| 393c406 | liste d'arrêt, ligne 8 | L-2, P-4 | juste |
| 413a427 | entrée « Contre-lecture 3 quater » | hors, déclaré | juste (empreintes exactes, reconnue) |

Aucun changement ne tombe hors des 32 points et des changements déclarés par le rédacteur.

## Point 2 — aucun changement de fond ?

Sur la différence : aucune ligne ne touche l'énoncé de l'hypothèse, les prédictions B8-P1, B8-P2, B8-P4 à B8-P7, la métrique (score par le maximum, aire, 2 000 tirages, 800 directions, règle D), le seuil (borne basse strictement positive), le niveau (98,33 % ; 0,95), la règle de la sonde porteuse, les états U, J, N, Z, E, l'état agrégé, les lignes L1 à L6, AU-a, AU-b. Les précisions :

| précision | avis | cohérence des endroits |
|---|---|---|
| déclencheur d4 recalculé à 0,95 (et d2, d3 sur estimations ponctuelles) | **précision** : le brouillon 8 disait déjà « bornes au niveau 0,95 sauf d1 » ; d2 et d3 sont définis sur une aire et un quantile, l'estimation ponctuelle est leur lecture naturelle. Un déclencheur n'ouvre qu'un audit, le même dans les deux sens (R4) | « Seuil » (d1 à d4, inchangé) et audit (l. 390) : cohérents. « la graine du jeu » désigne la clé de la clause du jeu (`intervalle/…` ou `jumeau/…`) : lisible |
| classe vide → « échec » | **précision pure** : une classe vide donne 100 % de tirages à une seule classe, déjà « échec » par la règle des 1 % | « Métrique » (l. 132) et liste d'arrêt, ligne 9 : cohérents |
| réserve de la sonde de dissimulation à « toute issue » | **précision qui résout une contradiction** du brouillon 8 : « Hypothèse » (l. 106, inchangée) disait « un état U porté par elle seule à une condition jugée » ; les combinaisons disaient « L1 avec… ». Le brouillon 9 aligne les combinaisons sur la règle la plus ancienne. Réserve en tête, aucun état ni verdict changé | l. 106 et l. 373 : cohérents |
| recette de puissance (round(f × 640) sans remise ; deux issues ; graines filles) | **précision** : f vaut 1, ½, ¼, donc 640, 320, 160 exactement ; la règle de D-10 (« porteuse aux deux conditions », 80 %) ne change pas ; les deux issues de plus sont rapportées sans effet. Le mécanisme de dérivation d'une « séquence fille par (case, répétition, usage) » n'est pas écrit au niveau de l'appel (observation O-4) | plan 10 (l. 176, 181, 182) et D-10 : cohérents |
| fichier de sondes absent → arrêt de la passe et refus de la lecture | **précision qui tranche une contradiction** du brouillon 8 (règle mécanique : « sans objet » ; P1 et plan 3 : arrêt et refus) au plus strict ; sans donnée ; ne peut que rendre l'épreuve plus rare, jamais plus facile. Pour la sonde des couches 7 et 23 non conforme, le texte durcit au-delà de ce que le code de la passe fait selon la notice (« sans objet ») : déclaré au § 4 de la note des différences (à réaligner) | règle mécanique (l. 324), P1 (l. 289), plan 3 (l. 168), D-8, r4, liste d'arrêt 8, S3 : cohérents. Reste anodin : « Seuil », l. 143, « (échec, sans objet, absence) » — « absence » ne peut plus concerner une sonde décisive (O-3) |
| S4 « aucune action de `H` n'a de jeton noté » (non annoncé parmi les précisions) | **changement de verdict sur un cas extrême** : sous le brouillon 8, 640 actions `H` toutes vides auraient donné « échec » partout (E, L4, ou L5 par l'essai A0) ; sous le brouillon 9, « sans objet ». Les deux issues sont non informatives, la ligne S4 du brouillon 8 était inatteignable (r5), et rien n'est lu : acceptable avant toute donnée | S4 et r5 : cohérents |

Aucune précision n'est un changement de règle sur une issue informative.

## Point 3 — les 32 points

Notice de la passe (13) :

| n° | porté | où | avis |
|---|---|---|---|
| P-1 | oui | D-13 (l. 98), P1 | égal à la notice (« Entrées attendues ») et à la note des lacunes |
| P-2 | oui | P1 (l. 289) | empreinte `76cdeace…e67e` égale à la note d'interface, point (b) (ligne 89) |
| P-3 | oui | P0, D-1, l. 304 à 306, 308 | égal à la notice (registre, bordereau à sept clés et sous-clés) |
| P-4 | oui, durci | règle mécanique, P1, ligne 8, S3, l. 138, 244 | durcissement déclaré (point 2) ; code de la passe à réaligner |
| P-5 | oui, **défectueux** | P8 (l. 296) | **R-1, bloquante** : la phrase reprise de la notice refuse, à la lettre, des chemins de la liste fermée |
| P-6 | oui | P9 (l. 297) | juste |
| P-7 | oui | P7 (l. 295) | juste |
| P-8 | oui | P10 (l. 298) | juste |
| P-9 | oui | livraison 5 (l. 256), (5) (l. 265) | juste |
| P-10 | oui | plan 5 (l. 170) | juste |
| P-11 | oui | l. 259 à 266 | noms exacts ; R-3 (nom des tableaux bruts) |
| P-12 | oui | P3 (d) (l. 291) | mot pour mot |
| P-13 | oui | passe avant (l. 238) | mot pour mot |

Développeur de la lecture (19) :

| n° | porté | où | avis |
|---|---|---|---|
| L-1 | oui | l. 259 à 266 ; r2 | aux noms de la notice (qui prime : déclaré) |
| L-2 | oui, tranché au plus strict | plan 3, règle mécanique, r4, ligne 8 | point 2 |
| L-3 | oui | S3, S4 | point 2 (S4) |
| L-4 | oui | r4 | mot pour mot |
| L-5 | oui | l. 156 | mot pour mot |
| L-6 | oui | l. 382, 384 | mot pour mot |
| L-7 | oui | l. 390 | mot pour mot |
| L-8 | oui | l. 132, 118 | mot pour mot |
| L-9 | oui | l. 352 | mot pour mot, placé avant la table (sans effet) |
| L-10 | oui | l. 373 | mot pour mot |
| L-11 | oui | l. 176, 181, 182 | mot pour mot |
| L-12 | oui | D-5, D-6 | mot pour mot |
| L-13 | oui, hors de la cellule | plan 5 | cellule F-3 inchangée (point 5) |
| L-14 | oui | r2 | mot pour mot |
| L-15 | oui | r8 | mot pour mot |
| L-16 | oui | l. 138, 244, P1 | « refus » du développeur porté en « arrêt de la passe et refus de la lecture » : cohérent avec P-4 |
| L-17 | oui | l. 306, D-2 | juste |
| L-18 | oui | l. 305 | `LIVRAISON-PASSE-IIB` après `CODE-PASSE-IIB` : condition décidée par la session mère, déclarée |
| L-19 | oui | plan 4 (d) | juste |

## Point 3 bis et point 4 — noms et formats contre la notice et la note des lacunes

Comparaison faite par programme des éléments entre accents graves du bloc « Noms et champs » (l. 259 à 266) et de la section « Livraison » de la notice (l. 92 à 101). Différences : seulement des écritures (objet JSON littéral dans la notice, mêmes clés en prose dans le texte : `fichier`, `taille`, `sha256`, `morceaux` ; `nom`, `couche`, `empreinte`, `role` ; `nom`, `taille`, `sha256` ; `-c23` abrégé dans la notice, nom entier dans le texte ; `<sortie>/livraison/` contre `livraison/`). La règle `NaN` de la notice (point 1) est au texte l. 241. **Noms de fichiers, découpage (50 000 000 octets, `X.npz.morceau-000`, `X.npz.morceaux.json`), format des archives, clés `scores`, `directions`, `agregations`, `colonnes`, dix champs de l'index, clés de la trace (une à une), deux clés du bordereau : identiques au caractère près.** Une ambiguïté nouvelle : le nom des tableaux bruts (R-3).

- Registre : en-tête identique au caractère près à la note des lacunes (vérifié par programme) ; quatre colonnes, une ligne par clé, six clés, clé hors des six refusée : identiques ; conditions d'ordre : `CODE-PASSE-IIB` et `CODE-LECTURE-SONDES-IIB` strictement après le scellement, `ETATS-COURSE-IIB` strictement après le scellement, `LIVRAISON-PASSE-IIB` strictement après `CODE-PASSE-IIB` : présentes. Égal à la notice (l. 84).
- Bordereau du code de la passe : sept clés et sous-clés égales à la notice (l. 86). Bordereau de la lecture : six clés égales à la lacune 17.
- Extrait du côté exposé (D-13) : aucun élément de la note des lacunes absent du texte ; six clés, chaîne de `avertissement` identique, forme de `run_id`, treize noms de `versions`, quatre chemins relatifs, six clés des lignes, ordre : identiques ; « clés répétées refusées » est dans la notice (l. 88) ; « `dose_avant` et `empreinte` ne sont comparées à rien » : notice, mot pour mot.

## Point 5 — cellule de l'entropie

La ligne 76 du brouillon 9 est **identique octet pour octet** à la ligne 75 du brouillon 8 (`cmp`). La règle « entier décimal sans séparateur ; refus si l'entropie ne figure pas ainsi dans le texte scellé » est écrite au plan, point 5 (l. 170), hors de la cellule.

## Trois ajouts du rédacteur

- **(a) `LECTURE-SONDES-IIB` après les cinq autres** : accepté. Conséquence de l'ordre déjà écrit (la lecture exige les cinq autres avant de tourner et inscrit sa ligne à l'étape (h)) ; ne crée aucune condition nouvelle de départ. Formule voisine à rendre exacte : R-4.
- **(b) ligne de mémoire « aucune sonde lue »** : acceptée ; elle redit P1 et la règle mécanique, ne produit aucun verdict.
- **(c) réserve de 4 000 000 octets** : **le compte tient**, l'attribution est fausse à un endroit (R-2). Recompte de la liste fermée : morceaux 2 (scores par action : 98 672 640 octets de données + environ 429 000 octets de la liste des directions, mesurés sur 2 409 objets au nom le plus long du plancher de la tromperie, soit 1,98 morceau) + 2 (scores par jeton : 1,47) + 22 (couche 15 : 21,10) + 3 + 3 (couches 7 et 23 : 2,75 chacune) = **32** ; fichiers de plus : 5 descriptions des morceaux (quelques kilo-octets), 40 compagnons (environ 4 kilo-octets), en-têtes des archives (mesurés : 39 306 octets pour 161 entrées), liste des directions (environ 0,43 Mo, dans l'archive 1), index (2 560 lignes ; environ 0,5 à 1,3 Mo selon la longueur des identifiants de tâche, non connue), trace et bordereau (quelques dizaines de kilo-octets) : **de l'ordre de 1 à 2 Mo, sous 4 000 000** (estimation, non mesurée sur la livraison réelle). **Borne** : 1 502 781 440 + 4 000 000 = 1 506 781 440, sous 2 000 000 000 avec 493 218 560 octets de marge ; la garde P9 et la garde r2 la contrôlent sur les tailles réelles. Elle tient.

## Point 6 — validateur

`PYTHONPATH=src .venv/bin/python` → `problemes(brouillon 9)` : `['section vide ou à remplir : Contre-lecture']`.
Marqueurs « À REMPLIR » : exactement deux, lignes 76 et 428. Chaînes de la procédure, chacune une fois : `À REMPLIR — À FIXER : tirée par la session mère au scellement` (1) ; `- **Contre-lecture 4 (finale, texte rempli)** — À REMPLIR :` (1) ; `versée avec l'empreinte du texte scellé.` (1). Entrée « Contre-lecture 3 quater » : empreintes `d8992b575a4e03fa6647b7d5af663596f80870925164b328adc0985c29f98b3a` et `94aaa09187c9631d2898ae50c8ccc7ec420ece9e71df5068a186aca516ad5e86`, exactes, seules et distinctes ; reconnue par le motif (quatrième entrée « 3 ») ; sa conclusion « PRÊT » est celle du rapport (l. 113).

## Point 7 — essai de la procédure sur copies (script `verif9/essai.py`, dossier temporaire)

Entropie d'essai `123456789012345678901234567890123456789` ; entrée 4 au gabarit ci-dessous, empreintes d'essai `111…1` et `222…2` (64 caractères).

| copie | `problemes` | `diff` avec le brouillon 9 |
|---|---|---|
| sain : entier seul + entrée 4 | `[]` | `['76c76', '428c428']` — exactement ces deux lignes |
| artefact : entrée 4 sans l'empreinte du rapport | `['contre-lecture 4 sans ses deux empreintes (brouillon relu et rapport)']` | — |
| artefact : entropie laissée ouverte | `['marqueur À REMPLIR restant hors des sections exigées']` | — |

Essai des corrections R-1 à R-4 sur une copie (`verif9/corr.py`) : chaque texte cherché paraît une fois ; `diff` : `['210c210', '264c264', '296c296', '305c305']` ; `problemes` : `['section vide ou à remplir : Contre-lecture']` ; les deux chaînes de la procédure restent uniques, aux lignes 76 et 428.

## Remarques neuves

### R-1. Bloquante pour le scellement — garde P8 : la phrase refuse des chemins de sa propre liste fermée

- **Passage** : garde P8 (l. 296), « … et les fichiers du modèle ; tout autre fichier du dépôt ou d'un dossier d'entrée, et tout chemin dont un composant porte « iib », « ii-b », « consigne-privee » ou « extrait_cote_moniteurs », est refusé avant ouverture ».
- **Défaut** : le second membre (« et tout chemin dont un composant porte… ») n'est pas borné par « autre ». À la lettre, il refuse `ids-actions-iib-evaluation.npz` et `textes-actions-iib-evaluation.jsonl` (fichiers de P1, D-13), le registre propre `registres/sondes-iib-v1.md` (pièce de P0), et peut-être le nom de la course et le fichier de l'extrait. Le texte ne peut alors être tenu par aucun code : soit la passe s'arrête toujours (P8), soit le code s'écarte de la lettre et le contrôle de conformité doit l'écrire. Après le scellement, l'un ou l'autre est un écart, nœud de Lazar. La phrase vient telle quelle de la notice (écart 5) ; le code de la passe exempte sans doute la liste, ce que le texte doit dire.
- **TEXTE DE REMPLACEMENT** : remplacer `tout autre fichier du dépôt ou d'un dossier d'entrée, et tout chemin dont un composant porte « iib », « ii-b », « consigne-privee » ou « extrait_cote_moniteurs », est refusé avant ouverture` par `hors de cette liste, tout autre fichier du dépôt ou d'un dossier d'entrée, et tout chemin dont un composant porte « iib », « ii-b », « consigne-privee » ou « extrait_cote_moniteurs », est refusé avant ouverture ; un chemin de la liste fermée n'est jamais refusé par ce motif (les noms des fichiers de la course et du registre propre portent « iib »)`.

### R-2. À corriger — réserve de 4 000 000 octets attribuée à deux ensembles différents

- **Passages** : décision de taille (l. 210), « plus l'index, la trace, le bordereau, les fichiers de description des morceaux, les en-têtes des archives et les compagnons (moins de 0,01 Go ; la garde P9 leur réserve 4 000 000 octets) » ; garde P9 (l. 297) : « dont 4 000 000 réservés à la trace, au bordereau et à leurs compagnons (les fichiers 1 à 4 et leurs compagnons tiennent donc sous 1 996 000 000 octets) ».
- **Défaut** : P9 (reprise de la notice, écart 9) réserve les 4 000 000 octets à la trace, au bordereau et à leurs compagnons, l'index et les archives étant dans les fichiers 1 à 4 ; la ligne 210 dit que P9 les réserve à l'index, aux descriptions, aux en-têtes et aux compagnons. Le compte de la ligne 267 (une somme, non une règle) et la borne tiennent ; la règle est celle de P9 ; seule l'attribution est fausse.
- **TEXTE DE REMPLACEMENT** : remplacer `(moins de 0,01 Go ; la garde P9 leur réserve 4 000 000 octets)` par `(moins de 0,01 Go : compte au point « Taille des fichiers ajoutés par ces formes » ; la garde P9 réserve 4 000 000 octets à la trace, au bordereau et à leurs compagnons)`.

### R-3. À corriger — nom des tableaux d'activité brute : quel rang ?

- **Passage** : « Noms et champs », (4) (l. 264), « de nom `a` suivi du rang de l'action sur cinq chiffres (par exemple `a00016`) ».
- **Défaut** : le texte définit deux rangs : celui du tirage du sous-échantillon, dans la liste triée par le tri des chaînes de Python (l. 246), et le champ `rang` de l'index, dans l'ordre du fichier (l. 263). L'exemple `a00016` (multiple de 16) suggère le premier ; la note des différences (§ 4, passe, point 2) dit le second ; la notice écrit `a<rang sur cinq chiffres>` et définit `rang` dans l'index. Un code de la lecture qui prend l'autre rang lit le tableau d'une autre action : la garde r6 le refuserait (désalignement), mais le texte doit trancher.
- **TEXTE DE REMPLACEMENT** : remplacer `de nom `a` suivi du rang de l'action sur cinq chiffres (par exemple `a00016`)` par `de nom `a` suivi, sur cinq chiffres, de la valeur du champ `rang` de l'index (ordre du fichier des identifiants, non le rang dans le tri du sous-échantillon ; par exemple `a00016`)`.

### R-4. Mineure — « les cinq premières »

- **Passage** : conditions d'ordre (l. 305), « La passe exige les deux premières ; la lecture exige les cinq premières et refuse de tourner si une condition d'ordre manque. »
- **Défaut** : l'ordre de trois des clés dans le fichier n'est pas fixé ; « les cinq premières » se lit « les cinq premières de la liste écrite », non « les cinq premières lignes du fichier ».
- **TEXTE DE REMPLACEMENT** : remplacer `la lecture exige les cinq premières` par `la lecture exige les cinq autres clés`.

### Observations sans correction

- O-1. Durcissement de la sonde des couches 7 ou 23 non conforme (arrêt de toute la passe pour un bras descriptif) : coûteux si cela arrive, mais une sonde de nom attendu et de forme fausse signale un fichier faux ; acceptable. Le code de la passe est à réaligner (notice, écart 4 : « sans objet ») ; le contrôle de conformité le verra.
- O-2. r4, « l'état de chaque sonde dans la trace est celui que la règle mécanique rend à la réception » : la règle mécanique ne porte que sur les trois sondes décisives ; pour les six des couches 7 et 23, l'état attendu (« lue » ou « absente » selon le nom dans l'index) se déduit de la l. 244. Lisible ; le contrôle de conformité le relira.
- O-3. « Seuil », l. 143, « (échec, sans objet, absence) » : « absence » ne peut plus toucher une sonde décisive ; sans effet.
- O-4. Recette de puissance : « une séquence fille par (rang de la case, rang de la répétition, usage) » ne dit pas l'appel exact de `SeedSequence` ; sans donnée de la course et sans effet sur la règle de D-10 ; le contrôle de conformité fixera l'appel.
- O-5. « Tout fichier, toute clé ou tout champ hors de cette liste est un refus de la garde de réception (r2, r3, r4) » : une entrée de trop dans une archive n'est nommée par aucune des trois ; la phrase suffit à la rendre refusée.
- O-6. Le validateur ne contrôle pas que les deux empreintes de l'entrée 4 sont les bonnes : la session mère les contrôle.

## Procédure de remplissage mise à jour (pour la session qui scelle)

Elle vaut pour le brouillon 9, `aca110b0635abf9e7e5a1bdd1dc66b94aaae40ad5c72a6e7d6127967f87f272d`, et, mot pour mot, pour un brouillon 10 qui ne porterait que R-1 à R-4 (ces quatre remplacements gardent les lignes 76 et 428 : essai ci-dessus), en remplaçant le numéro, le chemin et l'empreinte du brouillon relu et le rapport par ceux de sa contre-lecture. Les chaînes ci-dessous sont uniques dans le brouillon 9 (vérifié).

1. Vérifier l'empreinte du brouillon relu ; le copier, octet pour octet, au chemin de scellement choisi par la session mère (nom versionné neuf, R12), qu'elle inscrira à la ligne `SCELLEMENT-SONDES-IIB`.
2. Tirer l'entropie **une seule fois**, sans essai préalable : `PYTHONPATH=src .venv/bin/python -c "import numpy as np; print(np.random.SeedSequence().entropy)"` ; consigner **hors du texte**, avec le versement (étape 5), la commande, la version de numpy et l'heure UTC.
3. **Premier remplacement (ligne 76, cellule « état et raison » de F-3)** : remplacer la chaîne exacte
   `À REMPLIR — À FIXER : tirée par la session mère au scellement`
   par **l'entier décimal tiré, seul, sans séparateur** (aucun autre mot, aucune parenthèse, aucune espace insécable ; plan, point 5). La ligne devient `| F-3 | entropie racine des graines | <entier décimal> |`.
4. **Second remplacement (ligne 428)** : remplacer la ligne entière qui commence par `- **Contre-lecture 4 (finale, texte rempli)** — À REMPLIR :` et finit par `versée avec l'empreinte du texte scellé.` par cette seule ligne, où `<EMPREINTE DU BROUILLON RELU>` est `aca110b0635abf9e7e5a1bdd1dc66b94aaae40ad5c72a6e7d6127967f87f272d` pour le brouillon 9 et `<EMPREINTE DU RAPPORT>` l'empreinte de ce rapport donnée dans le message qui le rend (et dans son compagnon `.sha256`) :
   `- **Contre-lecture 4 (finale, texte rempli)** — sous-agent neuf, modèle Claude Opus 5.5, qui n'a écrit ni ce texte, ni aucune contre-lecture antérieure de ce texte, ni la note d'interface ; vérification de la différence du brouillon 8 au brouillon 9. Brouillon relu : `brouillons/barreau8-lecture-sondes-v1/prereg-lecture-sondes-barreau8-v1-brouillon9.md`, empreinte `<EMPREINTE DU BROUILLON RELU>`. Rapport : `brouillons/barreau8-lecture-sondes-v1/contre-lecture-brouillon9-v1.md`, empreinte `<EMPREINTE DU RAPPORT>`. Conclusion : « PRÊT : le brouillon 9 peut être scellé une fois l'entropie des graines versée et cette entrée de contre-lecture portée au texte, sans autre changement ». **Règle** : le texte scellé ne diffère du texte relu par cette contre-lecture que par cette entrée et par la cellule « état et raison » de F-3, où seule l'entropie tirée remplace le marqueur ; la session mère le vérifie par une comparaison faite par programme, versée avec l'empreinte du texte scellé.`
   (la ligne commence par `- **Contre-lecture 4` pour le motif du validateur, porte deux empreintes distinctes et aucun « À REMPLIR » ; ne pas écrire de chevrons `<<…>>` dans le texte final ; la conclusion recopiée est celle du rapport qui fait foi pour le texte scellé : **ce rapport-ci conclut « PAS PRÊT »**, donc cette ligne ne s'emploie qu'avec le rapport de la contre-lecture du brouillon corrigé, à sa conclusion, à son chemin et à son empreinte).
5. Comparaison faite par programme (`diff`) entre le brouillon relu et le texte rempli : **exactement `76c76` et `428c428`**, rien d'autre ; la verser avec l'empreinte du texte scellé et la provenance de l'entropie.
6. `prereg.problemes(<texte rempli>)` doit rendre `[]` ; essai de cette garde sur le cas sain (le texte rempli) et sur un artefact (une copie où l'entropie reste ouverte : attendu `['marqueur À REMPLIR restant hors des sections exigées']`), versé (R5) ; puis `sceller_prereg` ; puis la ligne `SCELLEMENT-SONDES-IIB` ; l'heure de scellement consignée à côté de l'heure de la première sortie de la course (D-7).

## Conclusion

PAS PRÊT : (1) R-1, garde P8 (ligne 296), remplacement écrit ci-dessus ; (2) R-2, décision de taille (ligne 210), remplacement écrit ci-dessus ; (3) R-3, « Noms et champs », (4) (ligne 264), remplacement écrit ci-dessus ; (4) R-4, conditions d'ordre (ligne 305), remplacement écrit ci-dessus. Rien d'autre : les 32 points sont portés, les noms et formats sont ceux de la notice, aucune hypothèse, prédiction, métrique, seuil, niveau ni critère ne change, la cellule de F-3 est intacte, et les quatre remplacements gardent les lignes 76 et 428 (essai fait). La différence du brouillon 9 au brouillon corrigé est à contre-lire (quatre lignes), puis la procédure ci-dessus s'applique.
