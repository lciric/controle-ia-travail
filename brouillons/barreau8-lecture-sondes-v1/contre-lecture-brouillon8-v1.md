# Contre-lecture de la différence brouillon 7 → brouillon 8 — lecture des sondes figées sur le saboteur à budget (barreau 8) — v1

## En-tête

- Brouillon relu : `brouillons/barreau8-lecture-sondes-v1/prereg-lecture-sondes-barreau8-v1-brouillon8.md`, empreinte `d8992b575a4e03fa6647b7d5af663596f80870925164b328adc0985c29f98b3a` (vérifiée, égale à celle donnée et à son compagnon ; 414 lignes).
- Point de départ : brouillon 7, `8749b51816fca87987c3e163fd0b5e872164812f19287f102f95ad92c7fcf337` (vérifiée). Rapport de la contre-lecture précédente : `contre-lecture-brouillon7-v1.md`, `b62ec7795e8495ed693a3fd8dd2cdbb43219bfb73afb5d735e219d80dfd6194e` (vérifiée). Note des différences du rédacteur : `27d6653de4eb0326d513f755706b3e5282455e38738f7252edfc7e1bd60d7242` (vérifiée ; non ouverte, je ne m'y suis pas fié).
- Contre-lecteur : Opus 5.5 (`claude-opus-5-5`), neuf : n'a écrit aucun brouillon ni aucune contre-lecture antérieure de ce texte, ni la note d'interface ; ne connaît ni le sujet ni le mécanisme du saboteur.
- Heures (`date -u`) : début 2026-11-19 01:26:48 UTC ; fin : voir la dernière ligne.

### Fichiers lus, avec plages

| fichier | plage |
|---|---|
| `…/prereg-lecture-sondes-barreau8-v1-brouillon8.md` | lignes 1 à 80 ; 212 à 232 ; 382 à 414 (sections « Liste d'arrêt » et « Contre-lecture » entières) ; ligne 169 ; lignes rendues par la différence et par une recherche de motif dans ce seul fichier (« non scellé », « ce brouillon », « entropie », « F-3 », « À REMPLIR », « marqueur », « Contre-lecture 4 », « dernière contre-lecture », « texte relu ») |
| `…/prereg-lecture-sondes-barreau8-v1-brouillon7.md` | par la différence seulement |
| `…/contre-lecture-brouillon7-v1.md` | entier (152 lignes) |
| `src/controle_ia/prereg.py` | entier (76 lignes), `3b2e3ee5…c306`, égale à la citation du texte |
| `CLAUDE.md` | donné en contexte |

Rien d'autre : aucun fichier du dossier du saboteur, de `registres/`, `diag/`, `runs/`, `donnees/`, `docs/verdicts/`, `scripts/` ; aucun historique git ; aucun fichier d'un autre agent du dossier temporaire. Lecture incidente : la ligne 90 du brouillon 8 (rendue par la recherche de « marqueur ») parle du remplissage d'un marqueur dans l'ordre de la course ; sans valeur ni résultat.

## Différence faite par programme

`diff brouillon7 brouillon8` : `1c1`, `3c3`, `5c5`, `7c7`, `52c52`, `231c231`, `280c280`, `387c387`, `413c413,414`. Soit neuf lignes du brouillon 7 changées (1, 3, 5, 7, 52, 231, 280, 387, 413) et une ligne ajoutée (la 413 du brouillon 8, entrée « Contre-lecture 3 ter »). Conforme à l'annonce.

Contrôle exact : j'ai rebâti le brouillon 8 à partir du brouillon 7 en appliquant, chacun sur une occurrence unique, les textes de remplacement du rapport de la contre-lecture du brouillon 7 (M-1 à M-4), plus le changement de la liste des contre-lecteurs (ligne 5), la ligne de date (ligne 7) et l'insertion de l'entrée 3 ter : **le résultat est égal au brouillon 8, ligne pour ligne** (`True`). Aucun autre caractère n'a changé.

## Table des lignes changées

| ligne (br. 7 → br. 8) | remarque | texte de remplacement repris exactement ? | contradiction créée ? |
|---|---|---|---|
| 1 → 1 | M-4 (titre) | oui : « brouillon 7 » → « brouillon 8 » | non |
| 3 → 3 | M-4 (statut) | oui, mot pour mot | non ; la phrase reste vraie dans le texte scellé |
| 5 → 5 | hors remarque, annoncé (liste des contre-lecteurs) | « 1, 3, 4 et 6 » → « 1, 3, 4, 6 et 7 » | non ; juste (entrée 3 ter) |
| 7 → 7 | hors remarque, annoncé (date) | ajout « ; brouillon 8 écrit entre 2026-11-19T01:24Z et 2026-11-19T01:25Z » | non ; heure de modification du fichier 01:25:37Z, cohérente |
| 52 → 52 | M-4 (marqueurs) | oui, mot pour mot | non ; vraie dans le texte scellé |
| 231 → 231 | M-3 ((b-10)) | oui, mot pour mot | non ; cohérente avec le bloc (l. 214 à 220) : sous (a), (b) « non retenue », (a) « appliquée », règle « scellé sous (a) » |
| 280 → 280 | M-2 (fichier absent) | oui, mot pour mot | non |
| 387 → 387 | M-1 (liste d'arrêt, ligne 2) | oui, mot pour mot | non (point M-1 ci-dessous ; une réserve de lecture, R-1) |
| 413 → 414 | M-1 (« Règle » de l'entrée 4) | oui, mot pour mot ; le reste de la ligne inchangé | non |
| — → 413 | hors remarque, annoncé (entrée « Contre-lecture 3 ter ») | — | non ; faits exacts (point 6) |

**Aucun changement sans remarque hors des trois annoncés (lignes 5, 7, 413 nouvelle).**

## Table M-1 à M-4

| remarque | appliquée ? | avis |
|---|---|---|
| M-1 (bloquante) | **oui, mot pour mot, aux deux lieux** | La ligne 2 de la liste d'arrêt et la « Règle » de l'entrée 4 permettent exactement deux différences entre le texte relu (le brouillon 8) et le texte scellé : l'entrée « Contre-lecture 4 (finale, texte rempli) » elle-même et la cellule « état et raison » de F-3 ; rien d'autre. Les deux formulations disent la même chose (« ailleurs que dans cette entrée et dans la cellule… » ; « que par cette entrée et par la cellule… »), et toutes deux exigent la comparaison faite par programme. Dans la ligne 2, « cette entrée » renvoie sans ambiguïté à l'entrée 4 nommée plus tôt dans la même cellule. Réserve de lecture R-1 ci-dessous, réglée par la procédure sans toucher au texte |
| M-2 | oui, mot pour mot | — |
| M-3 | oui, mot pour mot | — |
| M-4 | oui, mot pour mot (lignes 1, 3, 52) | Lu comme texte scellé : le titre dit « brouillon 8 » (vrai : texte d'origine) ; le statut dit « texte soumis au scellement ; il n'est scellé que si son compagnon `.sha256` et la ligne `SCELLEMENT-SONDES-IIB` le disent » (vrai) ; la ligne 52 dit « Au dernier brouillon, deux marqueurs restaient ouverts… ils sont remplis au scellement » (vrai). Aucun « non scellé » sur ce texte (le seul, ligne 19, vise l'ordre de la course) ; « ce brouillon » (lignes 6, 35) désigne des états anciens, vrais. Ligne 5 : « contre-lecteurs des brouillons 1, 3, 4, 6 et 7 : Opus 5.5 » ne nomme pas le contre-lecteur du brouillon 8 : **incomplète, non fausse** (elle renvoie à la section « Contre-lecture », où l'entrée 4 le nommera) ; la règle de M-1 interdit d'y toucher, et aucune phrase ne resterait fausse : aucun remplacement exigé |

## Sorties exactes du validateur

`PYTHONPATH=src .venv/bin/python` → `prereg.problemes('brouillons/barreau8-lecture-sondes-v1/prereg-lecture-sondes-barreau8-v1-brouillon8.md')` :

`['section vide ou à remplir : Contre-lecture']`

- Marqueurs « À REMPLIR » : **exactement deux**, ligne 75 (F-3) et ligne 414 (entrée 4).
- Chaîne `À REMPLIR — À FIXER : tirée par la session mère au scellement` : **une occurrence** (ligne 75).
- Début de ligne `- **Contre-lecture 4 (finale, texte rempli)** — À REMPLIR :` : **une occurrence** (ligne 414).
- Entrées reconnues par le motif du validateur dans la section : `['1', '2', '3', '3', '3', '4']` (3, 3 bis, 3 ter lues comme trois entrées « 3 », chacune sur son segment).

## Point 6 — entrée « Contre-lecture 3 ter »

Elle porte `8749b51816fca87987c3e163fd0b5e872164812f19287f102f95ad92c7fcf337` (brouillon 7, exacte) et `b62ec7795e8495ed693a3fd8dd2cdbb43219bfb73afb5d735e219d80dfd6194e` (rapport, exacte) ; ce sont ses deux seules empreintes, distinctes. Le validateur la reconnaît (troisième entrée « 3 ») et ne rend aucun message sur elle. Ses faits sont ceux du rapport : « PAS PRÊT » sur une liste fermée, N-1 à N-11 appliquées, sans changement hors remarque, M-1 bloquante, M-2 à M-4 mineures.

## Point 5 — essai de la procédure, sur copies (dossier temporaire, script `verif8/essai.py`)

Entropie d'essai `123456789012345678901234567890123456789` ; entrée 4 d'essai au gabarit ci-dessous, empreintes d'essai `111…1` (brouillon relu) et `222…2` (rapport), 64 caractères chacune.

| copie | `problemes` | `diff` avec le brouillon 8 |
|---|---|---|
| entropie (entier seul) + entrée 4 | `[]` | `75c75`, `414c414` — exactement ces deux lignes |
| entropie (entier et provenance entre parenthèses) + entrée 4 | `[]` | `75c75`, `414c414` |
| artefact : entrée 4 sans l'empreinte du rapport | `['contre-lecture 4 sans ses deux empreintes (brouillon relu et rapport)']` | — |
| artefact : entropie laissée ouverte, entrée 4 remplie | `['marqueur À REMPLIR restant hors des sections exigées']` | — |
| artefact : entrée 4 avec la même empreinte deux fois | `['contre-lecture 4 sans ses deux empreintes (brouillon relu et rapport)']` | — |

Les deux artefacts demandés sont refusés ; le cas sain passe.

## Remarques neuves

### R-1. Mineure, réglée par la procédure, aucun changement du texte — « seule l'entropie tirée remplace le marqueur »

- **Passages** : liste d'arrêt, ligne 2 (l. 387) ; « Règle » de l'entrée 4 (l. 414).
- **Défaut** : la procédure du rapport précédent remplaçait le marqueur par l'entier **suivi d'une parenthèse de provenance** (commande, version de numpy, heure). Lue à la lettre, la règle dit que **seule l'entropie** remplace le marqueur : la parenthèse serait un ajout hors de ce que la règle permet, et un lecteur strict pourrait dire que le texte scellé viole sa propre liste d'arrêt à sa naissance.
- **Règlement (dans la procédure, pas dans le texte)** : la cellule reçoit **l'entier décimal seul** ; la provenance (commande, version de numpy, heure UTC) est consignée hors du texte, avec la comparaison faite par programme et l'empreinte du texte scellé (ce qui satisfait la phrase de la ligne 50 « chaque valeur versée l'est avec son chemin et son empreinte » au sens du versement). Le validateur accepte les deux formes (essai ci-dessus) ; seule la forme « entier seul » est conforme à la lettre de la règle.

### Observations sans correction

- L'entrée 4, dans son texte d'attente, décrit une vérification « champ par champ (chaque valeur contre sa source) » du texte rempli ; la présente contre-lecture porte sur le brouillon 8 avant le versement de l'entropie, qui n'a pas de source vérifiable à l'avance. C'est l'économie voulue par M-1 : la ligne qui remplace l'entrée dit ce qui a été fait, et la comparaison faite par programme de la session mère tient lieu du contrôle du versement.
- Le validateur ne vérifie pas que les deux empreintes de l'entrée 4 sont les bonnes ; même remarque que le rapport précédent : la session mère les contrôle.

## Procédure de remplissage mise à jour (pour la session qui scelle)

Elle vaut pour le brouillon 8, `d8992b575a4e03fa6647b7d5af663596f80870925164b328adc0985c29f98b3a` ; les deux chaînes ci-dessous y sont uniques (vérifié).

1. Vérifier l'empreinte du brouillon 8 ; le copier, octet pour octet, au chemin de scellement choisi par la session mère (nom versionné neuf, R12), qu'elle inscrira à la ligne `SCELLEMENT-SONDES-IIB`.
2. Tirer l'entropie **une seule fois**, sans essai préalable : `PYTHONPATH=src .venv/bin/python -c "import numpy as np; print(np.random.SeedSequence().entropy)"` ; consigner **hors du texte**, avec le versement (étape 6), la commande, la version de numpy et l'heure UTC.
3. **Premier remplacement (ligne 75, cellule « état et raison » de F-3)** : remplacer la chaîne exacte
   `À REMPLIR — À FIXER : tirée par la session mère au scellement`
   par **l'entier décimal tiré, seul** (aucun autre mot, aucune parenthèse ; R-1). La ligne devient `| F-3 | entropie racine des graines | <entier décimal> |`.
4. **Second remplacement (ligne 414)** : remplacer la ligne entière qui commence par `- **Contre-lecture 4 (finale, texte rempli)** — À REMPLIR :` et finit par `versée avec l'empreinte du texte scellé.` par cette seule ligne, où `<EMPREINTE DU RAPPORT>` est l'empreinte de ce rapport donnée dans le message qui le rend (et dans son compagnon `.sha256`) :
   `- **Contre-lecture 4 (finale, texte rempli)** — sous-agent neuf, modèle Claude Opus 5.5, qui n'a écrit ni ce texte, ni aucune contre-lecture antérieure de ce texte, ni la note d'interface ; vérification de la différence du brouillon 7 au brouillon 8. Brouillon relu : `brouillons/barreau8-lecture-sondes-v1/prereg-lecture-sondes-barreau8-v1-brouillon8.md`, empreinte `d8992b575a4e03fa6647b7d5af663596f80870925164b328adc0985c29f98b3a`. Rapport : `brouillons/barreau8-lecture-sondes-v1/contre-lecture-brouillon8-v1.md`, empreinte `<EMPREINTE DU RAPPORT>`. Conclusion : « PRÊT : le brouillon 8 peut être scellé une fois l'entropie des graines versée et cette entrée de contre-lecture portée au texte, sans autre changement ». **Règle** : le texte scellé ne diffère du texte relu par cette contre-lecture que par cette entrée et par la cellule « état et raison » de F-3, où seule l'entropie tirée remplace le marqueur ; la session mère le vérifie par une comparaison faite par programme, versée avec l'empreinte du texte scellé.`
   (la ligne commence par `- **Contre-lecture 4` pour le motif du validateur, porte deux empreintes distinctes et aucun « À REMPLIR » ; ne pas écrire de chevrons `<<…>>` dans le texte final).
5. Comparaison faite par programme (`diff`) entre le brouillon 8 et le texte rempli : **exactement `75c75` et `414c414`**, rien d'autre ; la verser avec l'empreinte du texte scellé et la provenance de l'entropie.
6. `prereg.problemes(<texte rempli>)` doit rendre `[]` ; essai de cette garde sur le cas sain (le texte rempli) et sur un artefact (une copie où l'entropie reste ouverte : attendu `['marqueur À REMPLIR restant hors des sections exigées']`), versé (ligne 50, R5) ; puis `sceller_prereg` ; puis la ligne `SCELLEMENT-SONDES-IIB` ; l'heure de scellement consignée à côté de l'heure de la première sortie de la course (D-7).

## Conclusion

PRÊT : le brouillon 8 peut être scellé une fois l'entropie des graines versée et cette entrée de contre-lecture portée au texte, sans autre changement

M-1 à M-4 appliquées mot pour mot ; aucun changement hors remarque autre que les trois annoncés (liste des contre-lecteurs, date, entrée 3 ter), tous justes ; aucune contradiction créée ; une réserve de lecture (R-1) réglée par la procédure : l'entropie entre seule dans la cellule de F-3.

**Aucun refus d'outil.**

Fin : 2026-11-19 01:29:07 UTC.
