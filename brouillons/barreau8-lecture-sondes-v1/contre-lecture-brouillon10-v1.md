# Contre-lecture de la différence brouillon 9 → brouillon 10 — lecture des sondes figées sur le saboteur à budget (barreau 8) et passe de recalcul de l'activité interne — v1

## En-tête

- Brouillon relu : `brouillons/barreau8-lecture-sondes-v1/prereg-lecture-sondes-barreau8-v1-brouillon10.md`, empreinte `1676078f73bb75a7f0ce68653918fdf58943038d1344179bd5c2c38a78065fc1` (vérifiée ; 429 lignes).
- Point de départ : brouillon 9, `aca110b0635abf9e7e5a1bdd1dc66b94aaae40ad5c72a6e7d6127967f87f272d` (vérifiée). Rapport précédent : `contre-lecture-brouillon9-v1.md`, `906bec723f0528c6055be8fbb2d88cc44d2be10a09aa9353d492ab4be7c55654` (vérifiée). Note des différences du rédacteur : `differences-brouillon9-brouillon10-v1.md`, `e325d55c44eebf48693ed70cd308ed6536ec46ba0c64151b82c35fd016ec545a` (vérifiée, non ouverte : je ne m'y suis pas fié, toute la différence est refaite par programme).
- Contre-lecteur : Opus 5.5 (`claude-opus-5-5`), sous-agent neuf : n'a écrit ni ce texte, ni aucune contre-lecture antérieure de ce texte, ni la note d'interface, ni la notice, ni la note des lacunes, ni aucun code ; ne connaît ni le sujet ni le mécanisme du saboteur. Le mode « coût » (seul) est connu par le texte (I-10) : déclaré (décision N-054, point 3).
- Heures (`date -u`) : début 2026-11-19 02:14:02 UTC ; fin réelle 2026-11-19 02:16:07 UTC (dernier `date -u` avant l'écriture et le scellement de ce rapport).
- Aucun résultat du programme lu ; aucun code ni essai de `barreau8_moniteurs` ou `iib` ouvert ; aucun fichier de `registres/`, `diag/`, `runs/`, `donnees/`, `docs/verdicts/`, `scripts/`, ni de `docs/notes/` ; aucune branche ni historique git. Aucun refus d'outil.

### Fichiers lus, avec plages

| fichier | empreinte vérifiée | plage |
|---|---|---|
| brouillon 10 | `1676078f…65fc1` | lignes 1 à 99 (en-tête, champs ouverts, conditions de départ, dont D-13), 185 à 311 (section « Passe » entière : décision de taille, ce que la passe calcule, livraison, « Noms et champs, liste fermée », réception, gardes P0 à P10 ; section « Code, registre et contrôle de conformité »), 395 à 429 (« Liste d'arrêt », « Contre-lecture ») ; ailleurs, lignes rendues par des recherches de motif (`rang`, libellés, `notice`, `P8`, `tableau brut`, `jamais en production` : l. 124, 137, 243, 254, 276) |
| brouillon 9 | `aca110b0…f272d` | par `diff` et par programme seulement (ligne 76 comparée octet pour octet) |
| `contre-lecture-brouillon9-v1.md` | `906bec72…5654` | en entier |
| `src/controle_ia/prereg.py` | — | en entier (76 lignes) |

## Point 1 — table des blocs de la différence (faite par programme)

`diff brouillon9 brouillon10` : `1c1 3c3 5c5 7c7 24c24 210c210 261c261 264c264 296c296 305c305 427a428` — conforme à l'annonce.

**Rebâti par programme** (`verif10/rebatir.py`, dossier temporaire) : brouillon 9 + les quatre remplacements R-1 à R-4 pris au caractère près dans le rapport précédent (chaque texte cherché paraît une fois dans le brouillon 9 ; chaque texte de remplacement paraît une fois dans le rapport et une fois dans le brouillon 10). `diff rebâti brouillon10` : `1c1 3c3 5c5 7c7 24c24 261c261 427a428` — **les lignes 210, 264, 296 et 305 du brouillon 10 sont identiques au rebâti** : R-1 à R-4 sont repris exactement, et rien d'autre ne change sur ces lignes. Différence au caractère près des lignes restantes (`verif10/mots.py`) :

| bloc | objet | changement exact (caractère près) | verdict |
|---|---|---|---|
| 1c1 | titre | `9` → `10` | juste |
| 3c3 | statut | `9` → `10` | juste |
| 5c5 | liste des contre-lecteurs | ajout de « ` ; contre-lecteur du brouillon 9 : Opus 5.5` » | juste (conforme à l'en-tête du rapport `906bec72…`) |
| 7c7 | date | ajout de « `; brouillon 10 écrit entre 2026-11-19T02:12Z et 2026-11-19T02:13Z ` » | juste |
| 24c24 | demi-phrase sur la version 2 du code de la passe | ajout de « ` (le code de la passe et sa notice sont passés depuis en version 2, sans changement des noms ni des formats de la livraison ; c'est la ligne de registre du code qui fait foi sur la version)` » | juste, sans contradiction (point 5) ; l'affirmation de fait n'est pas vérifiable sans lire la notice v2, hors de mon périmètre (observation O-3) |
| 210c210 | R-2 | égal au rebâti | juste |
| 261c261 | cinquième remplacement (libellés) | ajout, après « les deux libellés des cases », de « `, exactement `"maximum (production)"` pour la case 0 et `"moyenne (bras de diagnostic, jamais en production)"` pour la case 1 ; la lecture refuse si ces deux libellés ne sont pas exactement ceux-là, dans cet ordre` » ; rien d'autre de la ligne | juste (point 4) |
| 264c264 | R-3 | égal au rebâti | juste |
| 296c296 | R-1 | égal au rebâti | juste |
| 305c305 | R-4 | égal au rebâti | juste |
| 427a428 | entrée « Contre-lecture 3 quinquies » | ligne insérée | juste (point 6) ; crée un léger décalage avec la ligne 427, sans effet (observation O-1) |

Aucun changement hors des onze blocs annoncés ; aucun bloc ne touche l'hypothèse, les prédictions, la métrique, le seuil, le niveau, les états, les critères de lecture, la liste d'arrêt, ni la cellule de F-3.

**Contradictions cherchées** : la ligne 210 (R-2) est désormais égale à P9 (l. 297 : « dont 4 000 000 réservés à la trace, au bordereau et à leurs compagnons ») et renvoie au point de la ligne 267, qui existe sous ce nom exact (« Taille des fichiers ajoutés par ces formes ») ; la ligne 305 (R-4) : « les cinq autres clés » = les six clés de la ligne 302 moins `LECTURE-SONDES-IIB`, que la lecture inscrit elle-même : cohérent ; lignes 261, 264, 296 : points 2 à 4.

## Points 2 à 5 — R-1 à R-4 et le cinquième remplacement

| remplacement | repris exactement | effet vérifié | verdict |
|---|---|---|---|
| R-1, garde P8 (l. 296) | oui | « hors de cette liste » porte sur les deux membres (« tout autre fichier… » et « tout chemin dont un composant porte… ») ; la phrase finale l'écrit en clair. **Tout chemin hors de la liste fermée reste refusé** (premier membre, inchangé) ; **aucun chemin de la liste n'est plus refusé** par le motif. La liste fermée est définie dans la même parenthèse : pièces de P0 (texte scellé, registre propre, bordereau du code, modules, rapport de conformité, notice, devis, ligne d'accord), fichiers de P1 (extrait du côté exposé, les quatre fichiers de la course aux chemins de D-13 — identifiants, textes, deux adaptateurs —, tâches d'évaluation à l'empreinte `76cdeace…e67e`, fichiers de sondes et de planchers), l'invite publiée `H1-classification`, les fichiers du modèle. Le fichier d'oracle n'est pas parmi les quatre fichiers de D-13 (l. 98) : il reste refusé, comme la consigne privée. Lisibilité acceptable (observation O-4 sur les compagnons) | juste |
| R-2, décision de taille (l. 210) | oui | attribution désormais égale à P9 ; le compte (l. 267) et la borne inchangés | juste |
| R-3, tableaux d'activité brute (l. 264) | oui | `rang` est défini **une seule fois**, à l'index (l. 263 : « rang dans l'ordre du fichier, à partir de 0 ») ; la ligne 254 dit « rang dans l'ordre des clés », et la ligne 238 fixe « l'ordre des clés (partout dans ce texte : l'ordre du fichier des identifiants) » : même rang ; l. 261 (« Lignes dans l'ordre du fichier des identifiants (champ `rang` de l'index) ») et l. 264 l'emploient de la même façon ; le rang du tri du sous-échantillon (l. 246) ne sert qu'à l'appartenance, que la garde r5 recalcule sur l'index, et la ligne 264 l'écarte en clair. Aucun autre emploi du nom des tableaux bruts dans le texte | juste |
| R-4, conditions d'ordre (l. 305) | oui | « cinq autres clés » sans ambiguïté | juste |
| cinquième remplacement (l. 261) | — (demandé par la conductrice) | libellés écrits exactement `"maximum (production)"` (case 0) puis `"moyenne (bras de diagnostic, jamais en production)"` (case 1), dans cet ordre ; refus dit (« la lecture refuse si ces deux libellés ne sont pas exactement ceux-là, dans cet ordre ») ; cohérent avec l. 137 et 243 (« bras de diagnostic, jamais en production ») et avec la ligne 259 (toute clé hors liste : refus de la garde de réception) ; rien d'autre de la ligne n'a changé (différence au caractère près). L'égalité au code de la passe est dite vérifiée par la conductrice ; je ne l'ai pas vérifiée (code hors de mon périmètre) | juste |

**Point 5 — le texte scellé dit-il quelque chose de faux sur lui-même ?** Non, sur les lignes 1, 3, 5, 7 et 24 : le titre et le statut disent « brouillon 10 », que le texte scellé est (copie octet pour octet hors des deux cellules), et le statut subordonne le scellement au compagnon et à la ligne `SCELLEMENT-SONDES-IIB` ; la ligne 5 nomme les contre-lecteurs jusqu'au brouillon 9 et renvoie à la section « Contre-lecture », qui portera l'entrée 4 (même usage qu'au brouillon 9, observation O-2) ; la ligne 7 donne les heures d'écriture ; la ligne 24 cite la notice v1 par son empreinte comme pièce lue par le rédacteur et dit que la ligne de registre du code fait foi sur la version, ce que le texte tient ailleurs : le bordereau du code porte `notice` (`chemin`, `sha256`) sans empreinte fixée par le texte (l. 288, 306), et l'empreinte `45da9b99…a472` n'apparaît qu'à la ligne 24. La ligne 53 (« deux marqueurs restaient ouverts, et deux seulement ») reste vraie. Seul décalage relevé : ligne 427 (O-1).

## Point 6 — validateur

`PYTHONPATH=src .venv/bin/python` → `prereg.problemes(brouillon 10)` : `['section vide ou à remplir : Contre-lecture']`.
Marqueurs « À REMPLIR » : exactement deux, lignes **76 et 429**. Ligne 76 du brouillon 10 **identique octet pour octet** à la ligne 76 du brouillon 9 : `True`. Chaînes de la procédure, chacune une fois : `À REMPLIR — À FIXER : tirée par la session mère au scellement` (1, ligne 76) ; `- **Contre-lecture 4 (finale, texte rempli)** — À REMPLIR :` (1, ligne 429) ; `versée avec l'empreinte du texte scellé.` (1, ligne 429). Entrée « Contre-lecture 3 quinquies » (l. 428) : empreintes `aca110b0635abf9e7e5a1bdd1dc66b94aaae40ad5c72a6e7d6127967f87f272d` et `906bec723f0528c6055be8fbb2d88cc44d2be10a09aa9353d492ab4be7c55654`, exactes, seules et distinctes ; reconnue par le motif `ENTREE` (entrées reconnues : `1, 2, 3, 3, 3, 3, 3, 4` ; la cinquième « 3 » est la quinquies) ; sa conclusion « PAS PRÊT » sur quatre remplacements (R-1 bloquante, R-2 et R-3 à corriger, R-4 mineure) est celle du rapport (l. 215).

## Point 7 — essai de la procédure sur copies (script `verif10/proc.py`, dossier temporaire)

Entropie d'essai `123456789012345678901234567890123456789` ; entrée 4 au gabarit ci-dessous (empreinte du brouillon 10 écrite en clair), empreinte d'essai du rapport `222…2` (64 caractères) : deux empreintes distinctes.

| copie | `problemes` | `diff` avec le brouillon 10 |
|---|---|---|
| sain : entier seul + entrée 4 | `[]` | `['76c76', '429c429']` — exactement ces deux lignes ; ligne 76 : `| F-3 | entropie racine des graines | 123456789012345678901234567890123456789 |` |
| artefact : entrée 4 sans l'empreinte du rapport | `['contre-lecture 4 sans ses deux empreintes (brouillon relu et rapport)']` | — |
| artefact : entropie laissée ouverte | `['marqueur À REMPLIR restant hors des sections exigées']` | — |

## Remarques neuves

Aucune remarque bloquante ni à corriger. Observations, sans correction demandée (le texte peut être scellé tel quel) :

- **O-1. Mineure — ligne 427** (entrée « Contre-lecture 3 quater », inchangée) : « cette différence reste à contre-lire (entrée 4) ». La différence du brouillon 8 au brouillon 9 a été contre-lue par l'entrée 3 quinquies (l. 428), insérée juste en dessous ; l'entrée 4 vérifie la différence du brouillon 9 au brouillon 10. Le renvoi est daté du brouillon 9 et la ligne suivante dit ce qui s'est passé : aucune règle, aucun état, aucune lecture n'en dépend. Pas de correction (elle ouvrirait un brouillon 11 pour une phrase de provenance) ; si une version nouvelle est un jour écrite pour une autre raison : remplacer `cette différence reste à contre-lire (entrée 4)` par `cette différence est contre-lue par l'entrée 3 quinquies`.
- **O-2. Ligne 5** : le contre-lecteur du brouillon 10 n'y est pas nommé ; il l'est à l'entrée 4. Même usage qu'au brouillon 9 ; rien de faux.
- **O-3. Ligne 24** : « sans changement des noms ni des formats de la livraison » est une affirmation de fait sur la notice v2, que je n'ai pas lue (hors périmètre) ; le texte fixe lui-même les noms et formats (l. 259 à 267) et le code s'y aligne, et le contrôle de conformité la relira. De même pour l'égalité des libellés de la ligne 261 au code (dite vérifiée par la conductrice).
- **O-4. Garde P8** : les compagnons `.sha256` des fichiers de P1 ne sont pas nommés un à un dans la liste fermée ; P1 les exige (« toutes les entrées présentes avec un compagnon d'empreinte conforme ») : ils se lisent comme fichiers de P1. Les bibliothèques chargées hors du dépôt et des dossiers d'entrée ne sont pas visées par le refus (inchangé depuis le brouillon 9). Sans effet.
- **O-5. Ligne 261** : les guillemets droits entre accents graves sont les délimiteurs de chaîne JSON ; la lecture naturelle compare les chaînes sans eux.

## Procédure de remplissage mise à jour (pour la session qui scelle)

Elle vaut pour le brouillon 10, `1676078f73bb75a7f0ce68653918fdf58943038d1344179bd5c2c38a78065fc1`. Les chaînes ci-dessous sont uniques dans le brouillon 10 (vérifié).

1. Vérifier l'empreinte du brouillon 10 ; le copier, octet pour octet, au chemin de scellement choisi par la session mère (nom versionné neuf, R12), qu'elle inscrira à la ligne `SCELLEMENT-SONDES-IIB`.
2. Tirer l'entropie **une seule fois**, sans essai préalable : `PYTHONPATH=src .venv/bin/python -c "import numpy as np; print(np.random.SeedSequence().entropy)"` ; consigner **hors du texte**, avec le versement (étape 5), la commande, la version de numpy et l'heure UTC.
3. **Premier remplacement (ligne 76, cellule « état et raison » de F-3)** : remplacer la chaîne exacte
   `À REMPLIR — À FIXER : tirée par la session mère au scellement`
   par **l'entier décimal tiré, seul, sans séparateur** (aucun autre mot, aucune parenthèse, aucune espace insécable ; plan, point 5). La ligne devient `| F-3 | entropie racine des graines | <entier décimal> |`.
4. **Second remplacement (ligne 429)** : remplacer la ligne entière qui commence par `- **Contre-lecture 4 (finale, texte rempli)** — À REMPLIR :` et finit par `versée avec l'empreinte du texte scellé.` par cette seule ligne, où `<EMPREINTE DU RAPPORT>` est l'empreinte de ce rapport, donnée dans le message qui le rend (et dans son compagnon `contre-lecture-brouillon10-v1.md.sha256`) :
   `- **Contre-lecture 4 (finale, texte rempli)** — sous-agent neuf, modèle Claude Opus 5.5, qui n'a écrit ni ce texte, ni aucune contre-lecture antérieure de ce texte, ni la note d'interface ; vérification de la différence du brouillon 9 au brouillon 10. Brouillon relu : `brouillons/barreau8-lecture-sondes-v1/prereg-lecture-sondes-barreau8-v1-brouillon10.md`, empreinte `1676078f73bb75a7f0ce68653918fdf58943038d1344179bd5c2c38a78065fc1`. Rapport : `brouillons/barreau8-lecture-sondes-v1/contre-lecture-brouillon10-v1.md`, empreinte `<EMPREINTE DU RAPPORT>`. Conclusion : « PRÊT : le brouillon 10 peut être scellé une fois l'entropie des graines versée et cette entrée de contre-lecture portée au texte, sans autre changement ». **Règle** : le texte scellé ne diffère du texte relu par cette contre-lecture que par cette entrée et par la cellule « état et raison » de F-3, où seule l'entropie tirée remplace le marqueur ; la session mère le vérifie par une comparaison faite par programme, versée avec l'empreinte du texte scellé.`
   (la ligne commence par `- **Contre-lecture 4` pour le motif du validateur, porte deux empreintes distinctes et aucun « À REMPLIR » ; un seul emplacement à remplir, `<EMPREINTE DU RAPPORT>`, sans chevrons dans le texte final.)
5. Comparaison faite par programme (`diff`) entre le brouillon 10 et le texte rempli : **exactement `76c76` et `429c429`**, rien d'autre ; la verser avec l'empreinte du texte scellé et la provenance de l'entropie.
6. `prereg.problemes(<texte rempli>)` doit rendre `[]` ; essai de cette garde sur le cas sain (le texte rempli) et sur un artefact (une copie où l'entropie reste ouverte : attendu `['marqueur À REMPLIR restant hors des sections exigées']`), versé (R5) ; puis `sceller_prereg` ; puis la ligne `SCELLEMENT-SONDES-IIB` ; l'heure de scellement consignée à côté de l'heure de la première sortie de la course (D-7).

## Conclusion

PRÊT : le brouillon 10 peut être scellé une fois l'entropie des graines versée et cette entrée de contre-lecture portée au texte, sans autre changement
