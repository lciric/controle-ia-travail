# Contre-lecture de la différence brouillon 10 → brouillon 11 — lecture des sondes figées sur le saboteur à budget (barreau 8) et passe de recalcul de l'activité interne — v1

## En-tête

- Brouillon relu : `brouillons/barreau8-lecture-sondes-v1/prereg-lecture-sondes-barreau8-v1-brouillon11.md`, empreinte `32c6da0125e3280e5b15316947f768da5025499613e9be8c97c0f2fb6e08fdf7` (vérifiée, égale à son compagnon ; 431 lignes, lu en entier une fois).
- Point de départ : brouillon 10, `1676078f73bb75a7f0ce68653918fdf58943038d1344179bd5c2c38a78065fc1` (vérifiée). Rapport précédent : `contre-lecture-brouillon10-v1.md`, `e4007fb10b7de2866830b0c87bf493295d407cff93d33087924e228c0ea7641c` (vérifiée). Note du rédacteur : `differences-brouillon10-brouillon11-v1.md`, `189526cb69734a3cc676c2ec6ec3a9d85a1c9d2b9c755556bcbda8d5f1381a8d` (vérifiée ; lue, non crue : toute la différence est refaite par programme).
- Contre-lecteur : Opus 5.5 (`claude-opus-5-5`), sous-agent neuf ; n'a écrit ni ce texte, ni aucune contre-lecture antérieure de ce texte, ni la note d'interface, ni aucune notice, ni aucun code. Ne connaît ni le sujet ni le mécanisme du saboteur ; le mode « coût » (seul) est connu par le texte (I-10), déclaré (décision N-054, point 3).
- Heures (`date -u`) : début 2026-11-19 03:09:51 UTC ; fin réelle 2026-11-19 03:32:22 UTC (dernier `date -u` avant l'écriture et le scellement de ce rapport).
- Aucun résultat du programme lu. Aucun code ni essai du barreau 8 ou du saboteur ouvert ; rien sous `registres/`, `diag/`, `runs/`, `donnees/`, `docs/verdicts/`, `scripts/`, `docs/notes/barreau8-iib-v1/` ; aucune branche ni historique git. Aucun refus d'outil.

### Fichiers lus

| fichier | empreinte vérifiée | plage |
|---|---|---|
| brouillon 11 | `32c6da01…fdf7` | en entier |
| brouillon 10 | `1676078f…65fc1` | par `diff` et par programme (ligne 76, bloc « Noms et champs », anciennes lignes 148 et 288) |
| `differences-brouillon10-brouillon11-v1.md` | `189526cb…1a8d` | en entier |
| `contre-lecture-brouillon10-v1.md` | `e4007fb1…641c` | en entier |
| `docs/notes/barreau8-cote-moniteurs-sorties-v1/contre-lecture-code-lecture-v1-v1.md` | `c5f12da0…cb85` | en entier |
| `docs/notes/barreau8-cote-moniteurs-sorties-v1/notice-passe-recalcul-v3.md` | `3071b909…165c9` | lignes 100 à 204 (« Livraison », « Codes de refus », machine, durée, essai à blanc, « Garde des chemins », traitement des remarques, « Phrases proposées », « État du texte », « Sur les essais ») |
| `docs/notes/barreau8-cote-moniteurs-sorties-v1/contre-lecture-code-passe-v2-v1.md` | `5f8de45c…b2c2` | lignes 98 à 167 (remarques 1 à 14, « Lacunes du texte ») |
| `docs/notes/barreau8-cote-moniteurs-sorties-v1/notice-passe-recalcul-v1.md` | `45da9b99…a472` (égale à celle de la ligne 24 du texte) | section « Livraison » seulement, comparée par programme à celle de la version 3, jamais affichée |
| `src/controle_ia/prereg.py` | `3b2e3ee5…c306` (égale à la ligne 38 du texte) | en entier |
| `src/controle_ia/sondes/evaluation.py`, `src/controle_ia/t07/plancher_v3.py` | — | recherche de motif (`quantile`, `integers`, `def`) pour conformer la simulation |

## Point 1 — table des blocs de la différence (faite par programme)

`diff brouillon10 brouillon11` : `1c1 3c3 5c5 7c7 24c24 89c89 91c91 96c96 98c98 148c148 169c169 191c191 288c288 290,292c290,292 296,298c296,298 306c306 324c324 387a388 411c412 427c428 428a430` — **conforme à l'annonce** (23 lignes changées, 2 ajoutées). Différence au caractère près faite par `git diff --no-index --word-diff` (fichiers hors du dépôt suivi, aucun historique lu).

| bloc | objet | changement exact | point des seize | verdict |
|---|---|---|---|---|
| 1c1, 3c3 | titre, statut | « 10 » → « 11 » | hors des seize, déclaré | juste |
| 5c5 | contre-lecteurs | ajout « ; contre-lecteur du brouillon 10 : désigné par la conductrice » | hors, déclaré | juste (le rapport `e4007fb1…` dit Opus 5.5 ; « désigné par la conductrice » n'est pas faux) |
| 7c7 | date | ajout « ; brouillon 11 écrit entre 2026-11-19T03:04Z et 2026-11-19T03:07Z » | hors, déclaré | juste |
| 24c24 | sources | « version 2 » → « version 3 » ; ajout « — section « Livraison » de la notice version 3 comparée par programme à celle de la version 1 : identique » ; ajout des trois sources avec empreintes | hors, déclaré | juste : empreintes exactes ; égalité des sections « Livraison » v1 et v3 **vérifiée par moi par programme : `True`** (5 481 caractères chacune) |
| 89c89 | D-4 | phrase T-2 ajoutée telle quelle | T-2 | juste |
| 91c91 | D-6 | phrase T-5 ajoutée telle quelle | T-5 | juste |
| 96c96 | D-11 | phrase T-4 complétée ; choix (a) du rédacteur | T-4 | **remarque N-1** |
| 98c98 | D-13 | « cet ordre » → « l'ordre `H`, `B50`, `B100`, `TJ100` » ; « lots strictement croissants … une ligne au plus par (condition, lot) ; des numéros de lot non contigus sont permis » | A-4 (et remarque 5 du code de la passe) | juste (même ordre qu'au brouillon 10, où « cet ordre » renvoyait à la liste des quatre noms) |
| 148c148 | clause (2) | « Un « échec » sur ce jeu donne en tête … » → « …, pour une sonde porteuse, … pour cette sonde, … ; pour une sonde qui n'est pas porteuse, l'échec est écrit dans la sortie, sans réserve en tête » | T-6 | juste (point 2) |
| 169c169 | plan, point 4 (h) | phrase T-1 ajoutée telle quelle + « Les cinq autres lignes du registre propre sont inscrites par la session mère. » | T-1 | juste (point 2) |
| 191c191 | « Qui fait quoi » | phrase 8 de la notice telle quelle | A-8 | juste |
| 288c288 | P0 | phrase 1 de la notice ; règle de T-2 étendue à la passe (« une ligne, et une seule, … a pour première cellule l'identifiant … cité par le bordereau du code, et porte l'empreinte du devis ; les autres lignes … ne comptent pas » ; brouillon 10 : « une ligne du registre des accords porte l'identifiant de l'accord et l'empreinte du devis ») | A-1 ; T-2 (extension déclarée) | juste ; l'extension resserre une garde de la passe sans toucher au fond ; conformité du code de la passe à vérifier (le rédacteur le dit, § E) |
| 290 (P2) | contrôles de plus | phrase 5 de la notice telle quelle | A-5 (remarque 7 du code de la passe) | juste ; observation O-2 |
| 291 (P3 (c)) | « au moins un identifiant et au plus 400 » | ajout de « moins un identifiant et au » | A-7, première moitié | juste |
| 292 (P4) | contrôles de plus | phrase 6 de la notice telle quelle | A-6 (remarque 14 du code de la passe) | juste ; cohérent avec I-5, I-7, r4 et S4 |
| 296 (P8) | lectures et écritures | phrase 2 de la notice, adaptée (déclaré) | A-2 (remarque 8 du code de la passe) | **remarque N-2** |
| 297 (P9) | place libre ; trace et bordereau mesurés | phrase 3 de la notice telle quelle | A-3 | juste (3 100 000 000 ≥ 2 000 000 000 + 1 055 129 600 + en-têtes) |
| 298 (P10) | limite déclarée | phrase 9 de la notice telle quelle | A-9 | juste |
| 306c306 | contrôle à l'ouverture des deux codes | ajout « ; le module lancé, que l'interpréteur nomme `__main__`, y compte sous le nom de son paquet » | A-1 (étendue aux deux codes, déclaré) | juste (la contre-lecture du code de la lecture dit que la lecture le fait déjà) |
| 324c324 | règle mécanique | « Recherche des directions : une seule règle… » ; choix (b) du rédacteur | T-7 ; A-7, seconde moitié | juste sur le fond ; **remarque N-3** (cohérence avec P1, plan point 3 et liste d'arrêt 8) |
| 387a388 | essai A0, limite déclarée | ligne ajoutée | T-3 | juste sous (R) ; question de plan (point 6) |
| 411c412 | liste d'arrêt, ligne 13 | parenthèse ajoutée (« la garde de réception, r1 à r8, n'est pas une lecture … ; condition de départ D-11 ») | T-4 | juste, sous réserve de N-1 |
| 427c428 | entrée « 3 quater » | « reste à contre-lire (entrée 4) » → « est contre-lue par l'entrée 3 quinquies » | hors, déclaré (observation O-1 du rapport précédent, texte de remplacement repris exactement) | juste |
| 428a430 | entrée « 3 sexies » | ligne insérée | hors, déclaré | juste (point 4) |

**Aucun changement hors des blocs annoncés** ; aucun bloc ne touche l'hypothèse, les prédictions B8-P1 à B8-P7, la métrique, le seuil, les niveaux, les états U, J, N, Z, E, l'état agrégé, la table des issues S1 à AU-b, les règles de décision, ni la cellule de F-3.

## Point 3 — les seize phrases, une ligne par point

Bloc « Noms et champs, liste fermée » (de `**Noms et champs, liste fermée**` jusqu'à `**Fichiers non lus avant**` exclu) : **identique au caractère près** à celui du brouillon 10 (comparaison par programme : `True`, 5 550 caractères).

| point | source | porté ? | contradiction ? |
|---|---|---|---|
| A-1 module lancé | notice v3, phrase 1 | oui, mot pour mot (P0) ; étendu aux deux codes (l. 306) | non |
| A-2 lectures / écritures | notice v3, phrase 2 | oui, réordonné, complété d'après « Garde des chemins » | **oui, une omission : l'index des invites publiées (N-2)** |
| A-3 place libre | notice v3, phrase 3 | oui, mot pour mot (P9) | non |
| A-4 lignes par lot | notice v3, phrase 4 | oui (D-13) | non |
| A-5 garde du modèle | notice v3, phrase 5 | oui, mot pour mot (P2) | non (O-2) |
| A-6 garde des adaptateurs | notice v3, phrase 6 | oui, mot pour mot (P4) | non |
| A-7 au moins un identifiant ; direction en trop | notice v3, phrase 7 | oui (P3 (c) ; règle (iv)) | non |
| A-8 essai à blanc | notice v3, phrase 8 | oui, mot pour mot | non |
| A-9 limite de P10 | notice v3, phrase 9 | oui, mot pour mot | non |
| T-1 inscription par la lecture | rapport du code de la lecture, l. 108 | oui, mot pour mot (plan, point 4 (h)) | non (point 2) |
| T-2 ligne d'accord | l. 109 | oui, mot pour mot (D-4) ; même règle à P0 | non |
| T-3 artefact positif | l. 110 | oui (phrase proposée portée), plus limite et réserve | non (sous (R)) |
| T-4 réception non lecture | l. 111 | oui (D-11, liste d'arrêt 13), complété | **oui : voie ouverte au code non vérifié (N-1)** |
| T-5 pièce de l'ordre | l. 112 | oui, mot pour mot (D-6) | non |
| T-6 portée de « non lisible » | l. 113 | oui, tranché pour les seules porteuses | non |
| T-7 règle unique | l. 114 ; remarque 8 | oui, complété | pas de contradiction, une incomplétude aux autres endroits (N-3) |

## Point 2 — aucun changement de fond ; avis sur les points demandés et sur les deux choix du rédacteur

- **T-6.** La ligne 148 du brouillon 10 était encadrée par « Si une sonde porteuse y est au-dessus » et « La sonde reste porteuse », et B8-P2 (l. 117) dit la réserve « écrite en tête du verdict si elle est porteuse ». Trancher pour les seules porteuses est la seule lecture cohérente avec ces deux passages ; l'issue n'entre dans aucun état ni aucune ligne de la table (la clause (2) « ne décide de rien », l. 149). L'expression « non lisible contre le témoin-jumeau » de L3 porte sur la clause (3) : autre objet, intacte. **Pas de changement de fond.**
- **T-1.** Cohérent partout : l. 305 disait déjà « inscrite par la lecture à sa dernière étape, postérieure aux cinq autres » ; la ligne ajoutée est en fin de fichier, conforme à « lignes ajoutées, jamais réécrites » (l. 304) ; les cinq autres : `SCELLEMENT-SONDES-IIB` (scellement par la session mère, l. 47 et 51), `LIVRAISON-PASSE-IIB` (l. 257, 302), `ETATS-COURSE-IIB` (D-12), `CODE-PASSE-IIB` et `CODE-LECTURE-SONDES-IIB` (sans inscripteur nommé au brouillon 10 ; la phrase nouvelle les attribue à la session mère, sans contradiction). Le refus « si une sortie `lecture-sondes-barreau8-v1.json` existe déjà sous `diag/` » est la seule mention de ce nom de fichier ; il rend mécanique « la lecture décisive se fait une seule fois ». **Pas de changement de fond.**
- **T-4 et choix (a) du rédacteur.** Le repère r8 (moyenne et écart-type des scores w·h + b des seules **directions de plancher** de la couche 15, sur des sous-échantillons tirés par rang sur les clés triées) mêle les quatre conditions : par le tri des chaînes, les clés `evaluation-B100…`, `-B50…`, `-H…`, `-TJ100…` se suivent par blocs de 640, et les rangs multiples de 16 (resp. 128) en prennent dans chaque bloc (environ 40, resp. 5 ou 6, par condition). Il ne porte aucun score de sonde et aucun contraste de condition : **il ne renseigne sur aucune condition.** En revanche, la phrase « sans attendre les autres conditions du plan, point 3 » dispense aussi la commande de réception de D-2 (ligne `CODE-LECTURE-SONDES-IIB` et égalité des empreintes des modules chargés), et la ligne 305 n'exige cette ligne de code qu'« avant toute lecture », ce que la réception n'est plus : **un code non contre-lu et non attesté peut ouvrir les fichiers d'activité au titre de la réception**, et rien du texte ne le refuse. C'est une voie par laquelle un score pourrait être vu avant la lecture. Remarque N-1, bloquante. Second défaut, de forme : « le seul nombre qu'elle écrit est le repère r8 » contredit les causes de refus naturelles (tailles en r2, comptes en r5) : à préciser dans la même phrase.
- **Choix (b) du rédacteur** (vecteur ou biais non fini, nom des couches 7 ou 23 en double : arrêt et refus, au lieu de « sans objet » ou « absente »). Le brouillon 10 ne disait rien de ces deux cas ; la règle comble un vide en durcissant, sur un objet d'intégrité de l'instrument (fichiers déjà fixés par empreinte, en pratique jamais non finis). Aucune hypothèse, aucun état, aucune issue décidable ne change. **Accepté.** Il manque seulement de le dire aux trois autres endroits où la règle est énumérée (N-3).
- **Règle unique des sondes lues (T-7).** Complète et sans choix pour (iv) : recherche par nom, ordre des numéros, unicité des 800 noms, aucune direction de plus, famille, couche et agrégation, et pour la dissimulation compte « toutes couches comptées » puis couche 15 exigée. Cohérence aux endroits qui en parlent : l. 138 (Métrique : sonde des couches 7 ou 23 non conforme → arrêt et refus) et l. 244 (liste des directions : nom manquant « absente », non conforme → arrêt) : cohérents ; l. 261 (ordre des colonnes « 0 à 799 », dissimulation « ordre de l'index ») : cohérente ; **l. 289 (P1), l. 168 (plan, point 3) et l. 407 (liste d'arrêt, ligne 8)** énumèrent les cas d'arrêt et de refus sans les deux cas nouveaux, alors que la l. 324 renvoie à « garde P1 » et « plan, point 3 » : incomplétude, non contradiction (N-3, mineure).
- **Choix de P0 (T-2 étendue à la passe).** Resserrement d'une garde de la passe ; pas de fond. Le code de la passe v3 n'a pas été écrit sous cette phrase : à vérifier par le contrôle de conformité (le rédacteur le dit, § E, point 1).

## Point 4 — validateur

`PYTHONPATH=src .venv/bin/python` → `prereg.problemes(brouillon 11)` : `['section vide ou à remplir : Contre-lecture']`.
Marqueurs « À REMPLIR » : exactement deux, lignes **76 et 431**. Ligne 76 du brouillon 11 **identique octet pour octet** à celle du brouillon 10 : `True`. Chaînes de la procédure, chacune une fois : `À REMPLIR — À FIXER : tirée par la session mère au scellement` (ligne 76) ; `- **Contre-lecture 4 (finale, texte rempli)** — À REMPLIR :` (ligne 431) ; `versée avec l'empreinte du texte scellé.` (ligne 431). Entrée « Contre-lecture 3 sexies » (l. 430) : empreintes `1676078f73bb75a7f0ce68653918fdf58943038d1344179bd5c2c38a78065fc1` et `e4007fb10b7de2866830b0c87bf493295d407cff93d33087924e228c0ea7641c`, exactes et distinctes ; reconnue par le motif `ENTREE` (entrées : `1, 2, 3, 3, 3, 3, 3, 3, 4`, la sixième « 3 » est la sexies) ; sa conclusion « PRÊT » est celle du rapport.

## Point 5 — essai de la procédure sur copies (script `verif11/proc.py`, dossier temporaire)

Entropie d'essai `123456789012345678901234567890123456789` ; ligne 431 remplacée entière par le gabarit ci-dessous, empreinte d'essai du rapport `222…2` (64 caractères) : deux empreintes distinctes.

| copie | `problemes` | `diff` avec le brouillon 11 |
|---|---|---|
| sain : entier seul + entrée 4 | `[]` | `['76c76', '431c431']` — exactement ces deux lignes ; ligne 76 : `| F-3 | entropie racine des graines | 123456789012345678901234567890123456789 |` |
| artefact : entropie laissée ouverte | `['marqueur À REMPLIR restant hors des sections exigées']` | — |
| artefact : entrée 4 sans l'empreinte du rapport | `['contre-lecture 4 sans ses deux empreintes (brouillon relu et rapport)']` | — |

## Remarques neuves

- **N-1. BLOQUANTE pour le scellement — la commande de réception seule n'exige pas le code attesté.** Passages : D-11 (l. 96) et conditions d'ordre (l. 305). Défaut : « sans attendre les autres conditions du plan, point 3 » dispense la réception de D-2 ; la ligne 305 n'exige `CODE-LECTURE-SONDES-IIB` qu'avant « toute lecture », et la réception n'en est plus une ; un code non contre-lu peut donc ouvrir les fichiers d'activité, et rien ne borne ce qu'il imprime. Le rédacteur demande en outre au code (§ E, point 6) de « n'exiger que la ligne `LIVRAISON-PASSE-IIB` ». Défaut corrigé par trois remplacements :
  - **TEXTE DE REMPLACEMENT 1 (l. 96).** Remplacer `le seul nombre qu'elle écrit est le repère r8, agrégat sur toutes les conditions confondues` par `hors des comptes, des tailles et des empreintes qu'une cause de refus peut porter, le seul nombre qu'elle écrit est le repère r8, agrégat sur toutes les conditions confondues`.
  - **TEXTE DE REMPLACEMENT 2 (l. 96).** Remplacer `La commande de réception seule peut être jouée par la conductrice du côté des moniteurs ou par le lecteur des sondes, dès que la ligne `LIVRAISON-PASSE-IIB` est inscrite, sans attendre les autres conditions du plan, point 3 ; elle n'écrit que « tenue », ou le refus et sa cause, et le repère r8` par `La commande de réception seule peut être jouée par la conductrice du côté des moniteurs ou par le lecteur des sondes, dès que les lignes `SCELLEMENT-SONDES-IIB`, `CODE-LECTURE-SONDES-IIB` et `LIVRAISON-PASSE-IIB` sont inscrites, sans attendre les autres conditions du plan, point 3 ; avant d'ouvrir quoi que ce soit de la livraison, elle exige, comme la lecture, ce texte scellé à l'empreinte de sa ligne et des modules chargés exactement ceux du bordereau du code de la lecture, aux mêmes empreintes (D-2), sinon elle refuse ; elle n'écrit que « tenue », ou le refus et sa cause, et le repère r8 ; aucune cause de refus ne porte un score d'action ou de jeton, ni un écart entre un score livré et un score recalculé`.
  - **TEXTE DE REMPLACEMENT 3 (l. 305).** Remplacer `` `CODE-LECTURE-SONDES-IIB` : strictement postérieure à `SCELLEMENT-SONDES-IIB`, **avant toute lecture**. `` par `` `CODE-LECTURE-SONDES-IIB` : strictement postérieure à `SCELLEMENT-SONDES-IIB`, **avant toute lecture et avant toute réception de la livraison**. ``
  (Chaque texte cherché paraît une fois dans le brouillon 11 : vérifié.)
- **N-2. À CORRIGER — la liste fermée des lectures de P8 n'a pas l'index des invites publiées.** Passage : P8 (l. 296). La notice v3 (« Garde des chemins », l. 159) dit que la passe lit, par chemin exact, « l'index des invites publiées et l'invite `H1-classification`, avec leurs compagnons » ; le texte ne nomme que l'invite, et dit « hors de cette liste, tout autre fichier du dépôt … est refusé avant ouverture ». Code et texte divergent donc d'un fichier (constat sur la notice seule ; je n'ai pas lu le code) ; après le scellement, ce serait un écart, nœud de Lazar. **TEXTE DE REMPLACEMENT** : remplacer `l'invite publiée de la recette de la question (6), `H1-classification` sous `docs/sources/invites-2606.08892-v1/`,` par `l'invite publiée de la recette de la question (6), `H1-classification`, et l'index des invites publiées, avec leurs compagnons, sous `docs/sources/invites-2606.08892-v1/`,`.
- **N-3. MINEURE — règle unique des sondes lues, trois énumérations à compléter.** Passages : P1 (l. 289), plan, point 3 (l. 168), liste d'arrêt, ligne 8 (l. 407). La l. 324 renvoie à « garde P1 » et à « plan, point 3 » pour les deux cas nouveaux, qui n'y figurent pas. **TEXTES DE REMPLACEMENT** : (a) remplacer `ou si une sonde des couches 7 ou 23 est trouvée sous son nom mais non conforme**)` par `ou si une sonde des couches 7 ou 23 est trouvée sous son nom mais non conforme, ou y paraît plus d'une fois, ou si un vecteur ou un biais d'une sonde ou d'une direction n'est pas fini**)` ; (b) remplacer `ou si l'état d'une sonde à la réception diffère de celui de la trace de la passe.` par `ou si l'état d'une sonde à la réception diffère de celui de la trace de la passe, ou si un vecteur ou un biais d'une sonde ou d'une direction n'est pas fini, ou si un nom de sonde des couches 7 ou 23 paraît plus d'une fois dans l'index.` ; (c) remplacer `| 8 | fichier de sonde ou de plancher absent, d'empreinte différente ou sans compagnon conforme ; état d'une sonde à la réception différent de celui de la trace |` par `| 8 | fichier de sonde ou de plancher absent, d'empreinte différente ou sans compagnon conforme ; état d'une sonde à la réception différent de celui de la trace ; vecteur ou biais non fini ; nom de sonde des couches 7 ou 23 en double dans l'index |`.

Observations, sans correction exigée :
- **O-1.** Ligne 5 : « contre-lecteur du brouillon 10 : désigné par la conductrice » ; le rapport `e4007fb1…` dit Opus 5.5. Rien de faux.
- **O-2.** P2 (l. 290) : « les quatre fichiers de configuration de la révision à leurs empreintes » — ces empreintes ne sont pas écrites dans le texte (seule celle de `tokenizer_config.json` l'est, P3 (b)) ; elles viennent de la note d'interface, que je n'ai pas lue. Le contrôle de conformité devra les rattacher à leur source.
- **O-3.** Le rédacteur ne déclare pas l'extension de la règle de T-2 à la passe comme un choix de sa main dans son message, mais il l'écrit au § B-2 de sa note : déclaré.

## Point 6 — question de plan : l'essai de la chaîne, artefact positif

### Raisonnement

- **Ce que la chaîne qui servira lit.** Chaque jeu décisif oppose les mêmes 64 tâches sous deux conditions : chaque bloc de tâche porte les deux classes, l'effet de tâche s'annule entre classes dans l'espérance, et le plancher de 800 directions ne monte que si l'adaptateur déplace l'activité. Sous (R), l'essai oppose deux moitiés de tâches **disjointes** : chaque bloc ne porte qu'une classe, l'effet de tâche entre tout entier dans la séparation, et le plancher sépare la moitié tirée. L'essai (R) éprouve donc une structure de données que la vraie lecture n'a pas ; (A) reproduit celle de la vraie lecture (deux classes dans chaque bloc), y compris la voie du rééchantillonnage par blocs où chaque tirage porte les deux classes.
- **L'essai peut-il encore échouer sur une chaîne cassée ?** Oui, et (A) en voit plus : (1) agrégation fausse (moyenne au lieu du maximum, qui dilue l'injection d'un jeton) : vue sous les deux formes ; (2) désalignement entre toutes les actions (essai (iii)) : vu sous les deux formes ; (3) **désalignement à l'intérieur d'un épisode** (scores décalés d'un pas, bornes des actions mal déduites des nombres de jetons notés) : **invisible sous (R)**, où toutes les actions d'une tâche portent la même étiquette, **vu sous (A)** ; (4) étiquettes fuyantes (étiquette tirée de quelque chose qui suit le score) : vues par (i) sous les deux formes. Sous (A), l'artefact positif ne peut plus échouer par le seul tirage des étiquettes : un échec y désigne la chaîne.
- **Essais (i) et (iii).** (ii) prend « les mêmes étiquettes que (i) » : (i) change avec. Sous (A), la sonde et les directions restent échangeables en (i) : le taux de faux « au-dessus » reste celui du rejeu écrit. (iii) peut rester tel quel (permutation entre toutes les actions de `H`) ; seule sa justification (« une permutation dans la tâche laisserait le décalage sous l'étiquette 1 ») tombe sous (A), où une permutation dans la tâche suffirait aussi : la permutation entre toutes les actions la contient.
- **Biais nouveau sous (A).** Rang du pas et longueur du contexte : cinq actions sur dix tirées au hasard dans chaque tâche équilibrent rang et longueur **en espérance** ; le déséquilibre de tirage est petit (écart-type du rang moyen de la classe 1 contre la classe 0 d'environ 0,96 dans une tâche, environ 0,12 sur 64 tâches) et touche la sonde et les 800 directions de la même façon (tous sont notés sur les mêmes étiquettes) : il ne peut pas fabriquer un « au-dessus » de la sonde seule. L'essai ne compare aucun prédicteur trivial (le texte ne le demande pas en A0). Un tirage par paires de pas consécutifs équilibrerait le rang à un demi-pas près ; inutile ici, non retenu.

### Simulation (données synthétiques seulement ; scripts dans `/tmp/claude-0/-home-user-controle-ia-travail/ccd98af0-e97a-5c3c-8902-30e463468b85/scratchpad/verif11/`)

Montage (`sim_a0.py`, `441a196b…97d6`) : 64 tâches × 10 actions de `H` ; score d'action = effet de tâche (écart-type σ fois celui du bruit, propre à chaque direction) + bruit normal réduit ; une sonde et 800 directions de plancher ; aire de Mann-Whitney regroupée sur toutes les paires ; 2 000 tirages par blocs de tâches (`integers(0, 64, 64)`, comme `intervalle_blocs`) ; D* = aire de la sonde − quantile 0,95 (linéaire, comme `np.quantile`) des 800 aires, sur le même tirage ; « au-dessus » si le quantile 0,833 % de D* est strictement positif ; artefact : score de chaque action étiquetée 1 porté à score + 2 s (équivaut à l'injection sur un jeton au maximum plus 2 s). Graines : `numpy.random.SeedSequence(20261119)` (puis 20261120, 20261121), une fille par (règle, σ, répétition), numpy 2.4.6. « Au-dessus » ici = la règle A0 du texte, qui ne demande pas l'interprétabilité.

Fréquence d'**échec de l'artefact positif (ii) sur une chaîne saine** (et marge : borne basse de D de l'artefact, minimum et moyenne) :

| montage | σ | (R) échecs | (R) borne basse min / moy | (A) échecs | (A) borne basse min / moy |
|---|---|---|---|---|---|
| tailles de la course, directions indépendantes, 25 rép. | 0 | 0/25 | 0,317 / 0,337 | 0/25 | 0,326 / 0,344 |
| idem | 0,5 | 0/25 | 0,249 / 0,289 | 0/25 | 0,322 / 0,346 |
| idem | 1 | 0/25 | 0,145 / 0,237 | 0/25 | 0,344 / 0,356 |
| idem | 2 | 0/25 | 0,139 / 0,182 | 0/25 | 0,345 / 0,357 |
| idem | 4 | 0/25 (et 0/50, `sim_R_fort.py`) | 0,051 / 0,146 (0,050 / 0,155) | 0/25 | 0,353 / 0,362 |
| idem, (R) seule | 8 | 0/50 | 0,012 / 0,153 | — | — |
| tailles de la course, **directions corrélées** (facteur de tâche commun, corrélation 0,9, poids aléatoire par direction ; `sim_correle.py`), 25 rép. | 2 | 0/25 | 0,103 / 0,179 | 0/25 | 0,343 / 0,356 |
| idem | 4 | **1/25** | **−0,072** / 0,152 | 0/25 | 0,352 / 0,360 |
| tailles réduites (20 tâches, 3 pas, 20 directions, 400 tirages ; `sim_petit.py`), 40 rép. | 1 | 18/40 | −0,104 / 0,016 | 0/40 | 0,028 / 0,170 |
| idem | 2 | 21/40 | −0,239 / −0,020 | 0/40 | 0,129 / 0,227 |
| idem | 4 | 27/40 | −0,256 / −0,064 | 0/40 | 0,213 / 0,263 |
| idem | 8 | 29/40 | −0,284 / −0,091 | 0/40 | 0,241 / 0,286 |

Le montage réduit reproduit le fait de la contre-lecture du code de la lecture (quantile 0,95 du plancher moyen 0,65 à 0,70, maximum 0,73 à 0,80 sous (R)). Quantile 0,95 moyen du plancher aux tailles de la course : sous (R) il monte avec σ (0,538 → 0,618 ; jusqu'à 0,710 avec directions corrélées) ; sous (A) il **descend** (0,537 → 0,510), l'effet de tâche fixant les paires entre tâches à un demi.

Chaînes cassées, tailles de la course, toutes cases ci-dessus (σ de 0 à 4, 25 rép.) : **sous (A)**, désalignement entre toutes les actions (iii) « au-dessus » 0/25, agrégation fausse 0/25, décalage d'un pas dans l'épisode 0/25 : **toujours vues**. Sous (R) : (iii) 0/25 et agrégation fausse 0/25, vues ; **décalage d'un pas dans l'épisode « au-dessus » 25/25 : jamais vu**. Cas sain (i) « au-dessus » : 0 dans toutes les cases, sous les deux formes.

Lecture : aux tailles de la course, (R) échoue rarement sur une chaîne saine (0 sur 300 répétitions à directions indépendantes ; 1 sur 25 avec un fort effet de tâche commun), mais sa marge tend vers zéro quand l'effet de tâche grandit, et un échec est alors indistinguable d'une chaîne cassée (la réserve en tête du brouillon 11 le dit) ; (A) garde une marge d'environ 0,35 quel que soit l'effet de tâche, et voit un défaut de plus. Les vraies données ne sont pas ce modèle (activité en 4 096 dimensions, directions tirées dans une même covariance) : l'ordre de grandeur, pas la valeur, est à retenir.

### Recommandation, au format décision

- **Décision** : quelle forme d'étiquetage l'essai de la chaîne de lecture (cas sain, artefact positif, alignement) emploie sur les épisodes honnêtes.
- **Enjeu** : un essai qui peut rendre « non concluant » (ligne L5) toute la lecture par le seul tirage, ou qui ne voit pas un désalignement à l'intérieur d'un épisode, n'éprouve pas la chaîne qui servira.
- **(R) garder l'étiquetage par moitié de tâches (brouillon 11)** — avantage : aucun texte à changer, aucun brouillon de plus ; échec rare aux tailles de la course dans ce modèle. Inconvénient : marge qui s'effondre avec l'effet de tâche (1 échec sur 25 sous directions corrélées) ; un échec ne distingue pas le tirage d'une chaîne cassée ; ne voit pas un décalage à l'intérieur d'un épisode ; structure de données (une classe par bloc) que la vraie lecture n'a pas.
- **(A) étiqueter cinq actions sur dix dans chaque tâche** — avantage : même structure que les jeux appariés de la lecture ; marge stable (borne basse d'environ 0,35) ; aucun échec sur chaîne saine sur 125 répétitions aux tailles de la course, 160 aux tailles réduites ; voit toutes les chaînes cassées simulées, dont le décalage dans l'épisode. Inconvénient : brouillon 12, sa contre-lecture, et un réalignement du code de la lecture (tirage des étiquettes) ; rang et longueur équilibrés en espérance seulement (sans effet sur la sonde seule).
- **Recommandation : (A)**, confiance 0,8. **Défaut sous 48 heures : (A)** si un brouillon 12 est de toute façon ouvert pour N-1 à N-3 ; sinon le défaut est (R) (état du texte).

### TEXTE DE REMPLACEMENT sous (A) (lignes 382 à 388 ; la ligne 387 est inchangée)

- **Ligne 382** : remplacer `(tâches étiquetées, jeton injecté, permutation)` par `(actions étiquetées, jeton injecté, permutation)`.
- **Ligne 383**, remplacer la ligne entière par :
  `- (i) **Cas sain.** Il n'y a qu'un épisode `H` par tâche (I-8) : **dans chaque tâche, cinq des dix actions de cet épisode reçoivent l'étiquette 1 et les cinq autres l'étiquette 0** (déclaré « apparié dans la tâche » : comme dans les jeux de la lecture, chaque tâche porte les deux classes). Tirage : le générateur neuf de la graine `sain/<sonde>` tire, tâche par tâche dans l'ordre du tri des chaînes de Python des identifiants de tâche, une permutation des rangs de pas 0 à 9 (`permutation(10)`) ; les rangs des cinq premières positions de la permutation reçoivent l'étiquette 1. Les étiquettes sont tirées sur les dix actions, avant le retrait des actions sans jeton noté, qui sortent ensuite des deux classes. Le score d'action de la sonde est le maximum, recalculé par le code de la lecture, de ses scores par jeton livrés. Aucune sonde ne doit être au-dessus.`
- **Ligne 384** : inchangée.
- **Ligne 385**, remplacer la ligne entière par :
  `- (iii) **Artefact d'alignement.** Sur les données de (ii), les clés d'action des scores par jeton de la sonde sont permutées **entre toutes les actions de `H`, toutes tâches confondues** (une permutation tirée par la graine `alignement/<sonde>`), les étiquettes restant en place : les scores injectés quittent les actions étiquetées 1, dans la tâche comme entre tâches. La sonde ne doit plus être au-dessus.`
- **Ligne 386** : inchangée (le rejeu reprend les mêmes formes sous les graines `sain-2/<sonde>`, `artefact-2/<sonde>`, `alignement-2/<sonde>`).
- **Ligne 387** : inchangée.
- **Ligne 388**, remplacer la ligne entière par :
  `- **Limite déclarée de l'essai.** Les étiquettes sont tirées au hasard dans chaque tâche : le rang du pas et la longueur du contexte sont équilibrés entre les deux classes en espérance seulement ; leur déséquilibre de tirage touche la sonde et les 800 directions de la même façon, et l'essai ne compare aucun prédicteur trivial. L'essai ne lit que `H` : un désalignement entre conditions n'est pas son objet. Quand l'artefact positif (ii) échoue, la sortie écrit pour chaque sonde l'aire de l'artefact et le quantile 0,95 du plancher sur le jeu de l'essai, sans autre effet ; un échec de (ii) n'ouvre aucun rejeu. Forme écartée, déclarée : l'étiquetage de tâches entières (brouillons 1 à 11), sous lequel des directions aléatoires séparent la moitié de tâches tirée quand l'activité dépend de la tâche (vu à tailles réduites par la contre-lecture du code de la lecture ; simulé par la contre-lecture du brouillon 11), et qui ne voit pas un décalage des scores à l'intérieur d'un épisode.`
- À la section « Seuil » ni ailleurs, rien d'autre ne change ; la note des différences du brouillon 12 citera ce rapport.

**Sous (R)** : le brouillon 11 est cohérent (règle inchangée, limite déclarée, sortie de diagnostic, réserve en tête) ; il ne demande sur ce point aucune correction. **Sous (A)** : il faudrait un brouillon 12 portant les remplacements ci-dessus, une contre-lecture de cette différence, et le réalignement du tirage des étiquettes dans le code de la lecture.

## Procédure de remplissage mise à jour (pour la session qui scelle)

Elle vaut pour le brouillon 11, `32c6da0125e3280e5b15316947f768da5025499613e9be8c97c0f2fb6e08fdf7`, **s'il est scellé sans autre changement** (par exemple sur le mot de Lazar écartant les remarques N-1 à N-3). Tout brouillon 12 déplace les lignes et demande sa propre procédure, écrite par son contre-lecteur. Les chaînes ci-dessous sont uniques dans le brouillon 11 (vérifié).

1. Vérifier l'empreinte du brouillon 11 ; le copier, octet pour octet, au chemin de scellement choisi par la session mère (nom versionné neuf, R12), qu'elle inscrira à la ligne `SCELLEMENT-SONDES-IIB`.
2. Tirer l'entropie **une seule fois**, sans essai préalable : `PYTHONPATH=src .venv/bin/python -c "import numpy as np; print(np.random.SeedSequence().entropy)"` ; consigner **hors du texte**, avec le versement (étape 5), la commande, la version de numpy et l'heure UTC.
3. **Premier remplacement (ligne 76, cellule « état et raison » de F-3)** : remplacer la chaîne exacte
   `À REMPLIR — À FIXER : tirée par la session mère au scellement`
   par **l'entier décimal tiré, seul, sans séparateur** (aucun autre mot, aucune parenthèse, aucune espace insécable ; plan, point 5). La ligne devient `| F-3 | entropie racine des graines | <entier décimal> |`.
4. **Second remplacement (ligne 431)** : remplacer la ligne entière qui commence par `- **Contre-lecture 4 (finale, texte rempli)** — À REMPLIR :` et finit par `versée avec l'empreinte du texte scellé.` par cette seule ligne, où `<EMPREINTE DU RAPPORT>` est l'empreinte de ce rapport, donnée dans le message qui le rend (et dans son compagnon `contre-lecture-brouillon11-v1.md.sha256`), et où la conclusion citée est celle que porte ce rapport au moment du scellement (si le brouillon 11 est scellé malgré la conclusion « PAS PRÊT », la session mère écrit à la place de la phrase « PRÊT … » : « PAS PRÊT, scellé sur le mot de Lazar (ligne d'accord citée) » et le versement le dit) :
   `- **Contre-lecture 4 (finale, texte rempli)** — sous-agent neuf, modèle Claude Opus 5.5, qui n'a écrit ni ce texte, ni aucune contre-lecture antérieure de ce texte, ni la note d'interface, ni aucun code ; vérification de la différence du brouillon 10 au brouillon 11. Brouillon relu : `brouillons/barreau8-lecture-sondes-v1/prereg-lecture-sondes-barreau8-v1-brouillon11.md`, empreinte `32c6da0125e3280e5b15316947f768da5025499613e9be8c97c0f2fb6e08fdf7`. Rapport : `brouillons/barreau8-lecture-sondes-v1/contre-lecture-brouillon11-v1.md`, empreinte `<EMPREINTE DU RAPPORT>`. Conclusion : « PRÊT : le brouillon 11 peut être scellé une fois l'entropie des graines versée et cette entrée de contre-lecture portée au texte, sans autre changement ». **Règle** : le texte scellé ne diffère du texte relu par cette contre-lecture que par cette entrée et par la cellule « état et raison » de F-3, où seule l'entropie tirée remplace le marqueur ; la session mère le vérifie par une comparaison faite par programme, versée avec l'empreinte du texte scellé.`
   (la ligne commence par `- **Contre-lecture 4` pour le motif du validateur, porte deux empreintes distinctes et aucun « À REMPLIR » ; un seul emplacement à remplir, `<EMPREINTE DU RAPPORT>`, sans chevrons dans le texte final.)
5. Comparaison faite par programme (`diff`) entre le brouillon 11 et le texte rempli : **exactement `76c76` et `431c431`**, rien d'autre ; la verser avec l'empreinte du texte scellé et la provenance de l'entropie.
6. `prereg.problemes(<texte rempli>)` doit rendre `[]` ; essai de cette garde sur le cas sain (le texte rempli) et sur deux artefacts (entropie restée ouverte : attendu `['marqueur À REMPLIR restant hors des sections exigées']` ; entrée 4 sans l'empreinte du rapport : attendu `['contre-lecture 4 sans ses deux empreintes (brouillon relu et rapport)']`), versé (R5) ; puis `sceller_prereg` ; puis la ligne `SCELLEMENT-SONDES-IIB` ; l'heure de scellement consignée à côté de l'heure de la première sortie de la course (D-7).

## Conclusion

PAS PRÊT : liste fermée des corrections, à porter en un brouillon 12 dont la différence est contre-lue avant le scellement :
1. N-1 (bloquante) : les trois textes de remplacement de N-1 (D-11, deux remplacements ; conditions d'ordre, ligne 305) ;
2. N-2 (à corriger) : le texte de remplacement de N-2 (P8, index des invites publiées) ;
3. N-3 (mineure) : les trois textes de remplacement (a), (b), (c) de N-3 (P1, plan point 3, liste d'arrêt ligne 8) ;
4. selon la décision de plan (point 6) : sous (A), les remplacements des lignes 382, 383, 385 et 388 ; sous (R), rien sur ce point ;
5. en-tête, date, liste des contre-lecteurs et entrée « Contre-lecture 3 septies » citant ce rapport, comme aux brouillons précédents.

## Refus d'outil

Aucun.
