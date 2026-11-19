# Contre-lecture de la différence brouillon 13 → brouillon 14 — lecture des sondes figées sur le saboteur à budget (barreau 8) et passe de recalcul de l'activité interne — v1

## En-tête

- Brouillon relu : `brouillons/barreau8-lecture-sondes-v1/prereg-lecture-sondes-barreau8-v1-brouillon14.md`, empreinte `5b503e28e6b81285a792575f878642bbd529888cc886e7cd4ddcf80257e39891` (vérifiée ; 442 lignes ; lu en entier une fois).
- Point de départ : brouillon 13, `7628ebfd8534bd44287e0a233a80339e6dde57db88fd0ada3df3c6a1b2305cd4` (vérifiée). Rapport précédent : `contre-lecture-brouillon13-v1.md`, `a723e7d91b8d4cf2c485598e24e49123359725f932b7b81b27e4e935a137575d` (vérifiée). Note du rédacteur : `differences-brouillon13-brouillon14-v1.md`, `f6be66c27d05575cc01a15c856db166a3cfe1bf83c0112501e0f90e54ef39afb` (vérifiée ; lue après ma propre différence, non crue). Rapport des deux codes et du troisième essai d'intégration : `docs/notes/barreau8-cote-moniteurs-sorties-v1/contre-lecture-codes-passe-v5-lecture-v4-integration-v1.md`, `c08e1ffb168454f44fb6f277423fe8e3d264ef24f2aa91d6e301cb5aa91cd1d4` (vérifiée).
- Contre-lecteur : Opus 5.5 (`claude-opus-5-5`), sous-agent neuf ; n'a écrit ni ce texte, ni aucune contre-lecture antérieure de ce texte, ni la note d'interface, ni aucune notice, ni aucun code. Ne connaît ni le sujet ni le mécanisme du saboteur ; le mode « coût » (seul) n'est connu que par le texte (I-10) : déclaré (décision N-054, point 3).
- Heures (`date -u`) : début 2026-11-19T04:53:17Z ; fin réelle : 2026-11-19T04:58:19Z.
- Aucun résultat du programme lu. Aucun code ni essai du barreau 8 ou du saboteur ouvert ; rien sous `registres/`, `diag/`, `runs/`, `donnees/`, `docs/verdicts/`, `scripts/`, `docs/notes/barreau8-iib-v1/`, `brouillons/ii-b-saboteur-budget-v1/` ; aucune branche ni historique git ; aucune recherche récursive. Aucun refus d'outil.

### Fichiers lus

| fichier | empreinte vérifiée | plage |
|---|---|---|
| brouillon 14 | `5b503e28…9891` | en entier |
| brouillon 13 | `7628ebfd…5cd4` | par `diff`, différence au mot près et reconstruction programmée (point 1) |
| `contre-lecture-brouillon13-v1.md` | `a723e7d9…575d` | en entier |
| `differences-brouillon13-brouillon14-v1.md` | `f6be66c2…ef39afb` | en entier |
| `contre-lecture-codes-passe-v5-lecture-v4-integration-v1.md` | `c08e1ffb…d4cd1d4` | en entier (74 lignes) ; rien d'autre de ce dossier |
| `src/controle_ia/prereg.py` | `3b2e3ee5…c306` (égale à la ligne 38 du texte) | en entier |
| `src/controle_ia/scellement.py` | `93beeb1c…94ef2` | empreinte seulement (outil de scellement de ce rapport) |
| `CLAUDE.md` | — | transmis en consignes |

Gabarit `prereg/gabarit-preregistrement-v1.md` : non ouvert (le validateur suffit au contrôle demandé).

Scripts et copies : `/tmp/claude-0/-home-user-controle-ia-travail/ccd98af0-e97a-5c3c-8902-30e463468b85/scratchpad/verif14/` (`wdiff.py`, `rebatir.py`, `rebatir2.py`, `renvois.py`, `controles.py`, `proc.py`, `gabarit.txt`).

## Point 1 — table des blocs de la différence

`diff brouillon13 brouillon14` : `1c1 3c3 5c5 7c7 24c24 97c97 168c168 191c191 224c224 227c227 276c276 289c289 324c324 390c390 415c415 440c440,441` — **conforme à l'annonce** (16 lignes changées, 1 ajoutée).

**Reconstruction par programme.** J'ai extrait du rapport `a723e7d9…` lui-même (lignes 136 et 137, motif « remplacer `…` par `…` ») les deux paires R-1 et R-2 ; chaque texte cherché paraît une fois dans le brouillon 13. Puis, sur le brouillon 13 ainsi corrigé, j'ai appliqué un par un, chaque texte cherché devant paraître exactement une fois, les remplacements déclarés : l'ajout (b) à (b-5), O-6, T-1, T-4 (règle mécanique), les trois alignements (c) (plan point 3, P1, liste d'arrêt 8), T-3 et T-2, l'ajout (a) à r5, le fait transmis en D-12 ; enfin les lignes d'en-tête 1, 3, 5, 7, 24 et les lignes 440-441 prises du brouillon 14 après contrôle mot à mot. **Le texte rebâti est égal au brouillon 14 (`True`) : aucun changement hors de ces points.**

| bloc | objet | changement (au mot près) | origine | verdict |
|---|---|---|---|---|
| 1c1, 3c3 | titre, statut | « 13 » → « 14 » | en-tête | juste |
| 5c5 | contre-lecteurs | « ; contre-lecteur du brouillon 13 : Opus 5.5 » | en-tête | juste |
| 7c7 | date | « ; brouillon 14 écrit entre 2026-11-19T04:49Z et 2026-11-19T04:51Z » | en-tête | juste (égal à la note des différences) |
| 24c24 | sources | passe « version 4 » → « version 5 » ; lecture « version 3 » → « version 4 ou suivante » (la phrase « c'est la ligne de registre de chaque code qui fait foi sur sa version » était déjà là) ; rapport du brouillon 13 et rapport d'intégration cités avec leurs empreintes | en-tête | juste ; deux empreintes vérifiées par moi ; observation O-4 |
| 97c97 | D-12, `run_id` | parenthèse « (plan, point 3) » étendue du fait transmis | fait transmis | juste (point 2) |
| 168c168 | plan, point 3 | « dans l'index » → « dans l'index de son fichier » | ajout (c) | juste |
| 191c191 | « Qui fait quoi » | phrase de R-2 | R-2 | mot pour mot |
| 224c224 | retour (b-2) | citation abrégée → phrase entière, marques de gras comprises | O-6 | juste ; vérifié par programme |
| 227c227 | retour (b-5) | phrase de R-1, puis retrait des deux phrases neuves | R-1, ajout (b) | R-1 mot pour mot ; (b) juste |
| 276c276 | garde r5 | « 2 560 actions, le champ `rang` de chaque ligne de l'index étant le rang de cette ligne dans le fichier, à partir de 0 » | ajout (a) | juste ; observation O-3 |
| 289c289 | garde P1 | « ou y paraît plus d'une fois, » → « ou paraît plus d'une fois dans l'index de son fichier, » | ajout (c) | juste |
| 324c324 | règle mécanique | T-4 (« dans l'index de son fichier ») ; T-1 (« sur toute entrée qui porte … dans l'index de chacun des trois fichiers de sondes et de planchers, ») | T-1, T-4 | mot pour mot |
| 390c390 | essai A0, chapeau | T-3 puis T-2, insérées après « jamais un score. » | T-3, T-2 | mot pour mot |
| 415c415 | liste d'arrêt, ligne 8 | « en double dans l'index » → « … de son fichier » | ajout (c) | juste |
| 440c440,441 | entrées 3 octies, 3 nonies | renvoi « cette différence est contre-lue par l'entrée 3 nonies » ; entrée 3 nonies ajoutée | en-tête | juste ; empreintes exactes |

## Point 2 — table R-1, R-2, O-6, T-1 à T-4, fait transmis, trois ajouts

| point | porté ? | où | juste, nécessaire, sans effet sur le fond ? |
|---|---|---|---|
| R-1 | mot pour mot (rebâti par programme depuis le rapport) ; le texte de remplacement est suivi, avant « tout le reste de l'essai », de l'ajout (b) | l. 227 | oui |
| R-2 | mot pour mot (rebâti par programme ; le texte de remplacement paraît une fois) | l. 191 | oui |
| O-6 | la phrase « **Pour les neuf sondes, … sur toutes les actions.** » paraît exactement deux fois : à sa place (l. 130, « Métrique ») et citée entre guillemets en (b-2) (l. 224), au caractère près, marques de gras comprises | l. 224 | oui ; l'application de (b-2) ne laisse plus de paire `****` |
| T-1 | mot pour mot (fragment du rapport, l. 62, retrouvé une fois) | l. 324 | oui ; la portée « trois fichiers » = léger, sondes neuves, planchers (table des identités ; clé `fichiers_sondes` de la trace) |
| T-2 | mot pour mot | l. 390 | oui, une fois l'ajout (a) fait |
| T-3 | mot pour mot | l. 390 | oui (cohérence plus bas) |
| T-4 | mot pour mot | l. 324 | oui ; même portée que les deux codes (rapport d'intégration, § 3 (e)) |
| fait transmis (`run_id`) | une parenthèse, dans D-12, déclarée « non vérifiable par le côté des moniteurs, et qui ne change rien à la règle » | l. 97 | oui : n'ajoute ni garde ni règle ; la source du nom de la trace (D-13, « écrits au manifeste et dans la trace ») est la même que celle que la parenthèse nomme ; ne demande au côté des moniteurs aucune lecture du manifeste. Clôt l'observation O-5 du rapport précédent |
| ajout (a), r5 | demi-phrase : `rang` = rang de la ligne dans le fichier, à partir de 0 | l. 276 | **nécessaire** : sans lui, T-2 (« la garde de réception r5 exige… ») serait fausse du texte (r5 du brouillon 13 ne le disait pas) ; **juste** : même définition que la liste fermée de l'index (l. 263) et que l'ordre des lignes des scores (l. 261) ; le code le fait déjà d'après le rapport d'intégration (§ 5, point 1) ; **sans effet sur le fond** : une condition de plus à une garde de réception, non une règle de lecture ; couverte par la liste d'arrêt, ligne 7 |
| ajout (b), (b-5) | les deux phrases T-3 et T-2 sont dites retirées sous l'option sans scores par jeton ; chaque phrase citée paraît, hors de (b-5), une fois et une seule (l. 390) | l. 227 | **nécessaire** : (b-5) retirait « jusqu'à "jamais un score." », les deux phrases qui suivent auraient renvoyé à une égalité retirée (même défaut que R-1) ; **juste** : sous (a), il n'y a plus d'égalité des deux chemins ; **sans effet** sous (b), option du scellement |
| ajout (c), trois endroits | « dans l'index de son fichier » au plan point 3, à P1 et à la liste d'arrêt 8 | l. 168, 289, 415 | **juste** : même portée que la règle mécanique et que les deux codes ; à P1 il remplace un « y » sans antécédent net ; **utile** (une seule règle, quatre fois dite pareil) ; **sans effet sur le fond**. Une cinquième phrase parle d'un nom unique sans « de son fichier » : observation O-1 |

## Point 3 — cohérence

- **T-3 contre la règle d'échec et le rejeu unique.** Le chapeau dit : « une seule inégalité fait échouer A0, sans rejeu » puis « Après une inégalité des deux chemins, ni (i), ni (ii), ni (iii) ne sont joués ». La règle d'échec (l. 394) : « A0 échoue si et seulement si l'égalité des deux chemins n'est pas tenue, ou si (a) …, ou (b) … » — l'inégalité suffit, (a) et (b) n'ont pas à être évalués. Le rejeu ne s'ouvre que « si (i) ou (iii) rend une sonde lue au-dessus », ce qui ne peut arriver s'ils ne sont pas joués. La limite déclarée (l. 396, sortie quand (ii) échoue) ne joue pas : (ii) n'a pas échoué, il n'est pas joué. La ligne L5 (l. 395, l. 373) suit. **Aucune contradiction.** Point laissé au code, sans effet sur l'issue : après la première inégalité, le contrôle de l'égalité des autres sondes lues est-il poursuivi pour écrire leur nombre d'actions inégales ? (observation O-5).
- **T-1, T-4 et la règle des sondes lues.** La portée complète est écrite une fois, dans la règle mécanique (l. 324) : finitude sur les neuf noms dans les trois index et sur toute candidate au plancher ; nom des couches 7 ou 23 en double dans l'index de son fichier. Les trois autres endroits (plan point 3, l. 168 ; P1, l. 289 ; liste d'arrêt 8, l. 415) disent la même chose pour le nom en double, et restent généraux pour la finitude (« un vecteur ou un biais d'une sonde ou d'une direction ») sans rien retirer ni ajouter. Même conséquence partout : arrêt de la passe (P1), refus de la lecture (plan point 3), jamais « sans objet ». **Règle unique, complète, sans contradiction.** Le code de la lecture doit encore chercher les neuf noms dans l'index du fichier des planchers (remarque C-1 du rapport d'intégration) : affaire du code, non du texte.
- **R-2.** Ce que la passe fait (écrire, découper, mesurer par P9, écrire compagnons et bordereau) est fait par « le code de la passe », hors de l'interdit. Ce que le côté exposé fait ensuite (copier, déposer en morceaux dans le dépôt, transmettre, calculer une empreinte) est exactement ce que R-2 excuse, sous la condition « sans en décoder le contenu ». Aucune voie pour voir un score n'est rouverte : l'exception ne couvre aucune opération qui décode un tableau ; l'interdit « ni n'en lit un score » reste entier. Le côté des moniteurs ne touche pas à cette phrase (il rebâtit et ouvre la livraison à la réception, comme avant).

## Point 4 — aucun changement de fond

Hypothèse (l. 100 à 108), prédictions B8-P1 à B8-P7 (l. 110 à 122), « Métrique » (l. 128 à 138), « Seuil » (l. 140 à 160), niveaux, règle du témoin-jumeau, conditions jugées, états, état agrégé, table des issues S1 à AU-b (l. 362 à 376) : **aucun bloc de la différence ne les touche (intacts)**. Bloc « Noms et champs, liste fermée » (du titre à « Fichiers non lus avant ») : **identique au caractère près** à celui du brouillon 13 (`True`, 5 551 caractères).

## Point 5 — lecture d'ensemble du brouillon 14 (texte qui sera scellé)

- **Ce que le texte dit de lui-même, une fois les deux remplacements faits.** Titre et statut « brouillon 14, texte soumis au scellement ; il n'est scellé que si son compagnon `.sha256` et la ligne `SCELLEMENT-SONDES-IIB` le disent » : vrai. Phrase des marqueurs (l. 53, « Au dernier brouillon, deux marqueurs restaient ouverts … F-3 et l'entrée « Contre-lecture 4 » ») : vraie (contrôlé : lignes 76 et 442). Liste des contre-lecteurs (l. 5) : arrêtée au brouillon 13, renvoyant à la section « Contre-lecture », où l'entrée 4 nommera celui du brouillon 14 : incomplet par construction, non faux (même forme qu'aux brouillons précédents). L'entrée 3 nonies dit « cette différence reste à contre-lire (entrée 4) » : vrai à l'écriture, et l'entrée 4 remplie y répond. Versions des codes : « passe version 5 », « lecture version 4 ou suivante », la ligne de registre de chaque code faisant foi : cohérent avec le rapport d'intégration (la lecture doit encore passer C-1 : « ou suivante » le couvre) ; observation O-4.
- **Options ouvertes après le scellement.** Recherche de « défaut », « échoit », « à trancher », « à confirmer », « provisoire », « peut être changé », « À FIXER » : chaque bloc de décision (l. 45, 145, 189, 213, 221, 314, 333, 341, 349) dit l'option sous laquelle le texte est scellé et « après le scellement, aucun défaut n'échoit ». Le « Défaut sous 48 heures » de la l. 341 est suivi de la même règle. Le seul « À FIXER » est le marqueur de F-3, rempli au scellement. **Aucune option ni aucun défaut ne joue après le scellement.**
- **Renvois.** Contrôle par programme (`renvois.py`) : chaque condition de départ D-1 à D-13, garde de la passe P0 à P10, garde de réception r1 à r8, ligne de la table des issues S1 à S5, L1 à L6, AU-a, AU-b, passage du retour (b-1) à (b-10), ligne 1 à 17 de la liste d'arrêt, déclencheur d1 à d4, point 1 à 10 du plan est **défini une fois et une seule** ; sortie « définitions multiples ou nulles : » vide. Tout identifiant de ces formes cité (96 identifiants distincts) est défini, à deux exceptions près, toutes deux antérieures à cette différence : `B8-P8`, `B8-P9` (l. 124, explicitement « du brouillon 3 », mémoire juste) ; `F-1` à `F-13` hors F-3 (l. 78, liste des champs fermés : c'est leur seule mention, déclarative) et `(F-7)` à la l. 108 (observation O-2). Renvois de la liste d'arrêt vérifiés au sens : ligne 3 (l. 97), 7 (l. 374), 10 (l. 228, 230), 13 (l. 96), 15 (l. 138, 249), 7 à 11 (l. 309) : chacune désigne la bonne ligne. **Aucun renvoi mort introduit par le brouillon 14.**

## Point 6 — validateur

`PYTHONPATH=src .venv/bin/python`, `prereg.problemes("…brouillon14.md")` : `['section vide ou à remplir : Contre-lecture']`.
Marqueurs « À REMPLIR » : exactement deux, lignes **76 et 442**. Ligne 76 **identique octet pour octet** à celle du brouillon 13 (`True`) : `| F-3 | entropie racine des graines | À REMPLIR — À FIXER : tirée par la session mère au scellement |`. Chaînes de la procédure, chacune une fois : `À REMPLIR — À FIXER : tirée par la session mère au scellement` ; `- **Contre-lecture 4 (finale, texte rempli)** — À REMPLIR :` ; `versée avec l'empreinte du texte scellé.` ; la ligne 442 commence et finit par les deux dernières ; le fichier finit par un saut de ligne. Entrée « Contre-lecture 3 nonies » : empreintes `7628ebfd8534bd44287e0a233a80339e6dde57db88fd0ada3df3c6a1b2305cd4` (brouillon 13) et `a723e7d91b8d4cf2c485598e24e49123359725f932b7b81b27e4e935a137575d` (rapport), exactes et distinctes ; motif `ENTREE` du validateur sur la section : `1, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4` (la neuvième « 3 » est la nonies) ; sur le texte rempli d'essai, aucune entrée ne manque de ses deux empreintes.

## Point 7 — essai de la procédure sur copies

Dossier `/tmp/claude-0/-home-user-controle-ia-travail/ccd98af0-e97a-5c3c-8902-30e463468b85/scratchpad/verif14/` (`proc.py`, `gabarit.txt`). Empreinte du brouillon 14 contrôlée avant copie. Entropie d'essai `123456789012345678901234567890123456789` ; ligne 442 remplacée entière par le gabarit ci-dessous, empreinte d'essai du rapport `222…2` (64 caractères) : deux empreintes distinctes.

| copie | `problemes` | `diff` avec le brouillon 14 |
|---|---|---|
| sain : entier seul + entrée 4 | `[]` | `['76c76', '442c442']` — exactement ces deux lignes ; ligne 76 : `| F-3 | entropie racine des graines | 123456789012345678901234567890123456789 |` ; aucun « À REMPLIR », aucun marqueur de gabarit |
| artefact : entropie laissée ouverte | `['marqueur À REMPLIR restant hors des sections exigées']` | — |
| artefact : entrée 4 sans l'empreinte du rapport | `['contre-lecture 4 sans ses deux empreintes (brouillon relu et rapport)']` | — |

## Remarques neuves

Aucune bloquante, aucune à corriger. Observations, sans correction exigée (aucune ne fait faire au code ou au lecteur autre chose que ce qui est voulu ; aucune ne rend le texte faux) :

- **O-1.** Règle mécanique, l. 324 : « elle porte le nom de la table, et ce nom ne paraît qu'une fois dans l'index ; sinon « sans objet » » — cinquième phrase sur un nom unique, sans « de son fichier ». Lecture unique tout de même : « l'index » y est celui de « l'entrée de l'index de rang k, dont le vecteur est sous la clé `s<k>_w` », et les deux codes cherchent dans l'index du fichier de la sonde (rapport d'intégration, § 3 (d)). Si la session mère voulait l'aligner (ce serait un changement de plus, donc un brouillon 15 et sa contre-lecture) : remplacer `et ce nom ne paraît qu'une fois dans l'index ; sinon` (paraît une fois, vérifié) par `et ce nom ne paraît qu'une fois dans l'index de son fichier ; sinon`. Je ne le demande pas.
- **O-2.** (Antérieure à cette différence.) « (F-7) », l. 108 : F-7 est dit « passé en condition de départ » (l. 78) sans dire laquelle ; c'est la puissance par fraction, D-10. Le lecteur s'y retrouve ; sans effet.
- **O-3.** Ajout (a) à r5 : la liste des artefacts de réception (l. 280) ne nomme pas « champ `rang` faux » ; R5 est tenue pour la garde r5 par ses autres artefacts, mais le contrôle de conformité peut vérifier que le code de la lecture éprouve ce cas.
- **O-4.** L. 24 : « passés depuis en version 5, sans changement des noms ni des formats de la livraison » s'appuie sur une comparaison des notices v3 et v1 ; pour les versions 4 et 5, l'appui est le rapport d'intégration (réception et lecture tenues de bout en bout), non une comparaison écrite. Sans effet : le bloc « Noms et champs » du texte fait foi, et la ligne de registre de chaque code fixe sa version.
- **O-5.** Après une inégalité des deux chemins, le texte ne dit pas si l'égalité est encore contrôlée pour les autres sondes lues (la sortie « écrit la sonde et le nombre d'actions inégales ») ; l'issue est L5 dans tous les cas.

## Procédure de remplissage mise à jour (pour la session qui scelle)

Elle vaut pour le brouillon 14, `5b503e28e6b81285a792575f878642bbd529888cc886e7cd4ddcf80257e39891`, scellé sans autre changement. Les chaînes ci-dessous sont uniques dans le brouillon 14 (vérifié).

1. Vérifier l'empreinte du brouillon 14 ; le copier, octet pour octet, au chemin de scellement choisi par la session mère (nom versionné neuf, R12), qu'elle inscrira à la ligne `SCELLEMENT-SONDES-IIB`.
2. Tirer l'entropie **une seule fois**, sans essai préalable : `PYTHONPATH=src .venv/bin/python -c "import numpy as np; print(np.random.SeedSequence().entropy)"` ; consigner **hors du texte**, avec le versement (étape 5), la commande, la version de numpy et l'heure UTC.
3. **Premier remplacement (ligne 76, cellule « état et raison » de F-3)** : remplacer la chaîne exacte
   `À REMPLIR — À FIXER : tirée par la session mère au scellement`
   par **l'entier décimal tiré, seul, sans séparateur** (aucun autre mot, aucune parenthèse, aucune espace insécable ; plan, point 5). La ligne devient `| F-3 | entropie racine des graines | <entier décimal> |`.
4. **Second remplacement (ligne 442)** : remplacer la ligne entière qui commence par `- **Contre-lecture 4 (finale, texte rempli)** — À REMPLIR :` et finit par `versée avec l'empreinte du texte scellé.` par cette seule ligne, où le **seul emplacement à remplir** est `<EMPREINTE DU RAPPORT>`, l'empreinte de ce rapport (`brouillons/barreau8-lecture-sondes-v1/contre-lecture-brouillon14-v1.md`), donnée dans le message qui le rend et dans son compagnon `contre-lecture-brouillon14-v1.md.sha256` (64 caractères hexadécimaux, sans chevrons dans le texte final) :
   `- **Contre-lecture 4 (finale, texte rempli)** — sous-agent neuf, modèle Claude Opus 5.5, qui n'a écrit ni ce texte, ni aucune contre-lecture antérieure de ce texte, ni la note d'interface, ni aucune notice, ni aucun code ; contre-lecture de la différence du brouillon 13 au brouillon 14 (remplacements R-1 et R-2, correction de forme O-6, phrases T-1 à T-4 du troisième essai d'intégration, fait transmis sur le nom de la course, trois ajouts du rédacteur) et lecture d'ensemble du texte soumis au scellement. Brouillon relu : `brouillons/barreau8-lecture-sondes-v1/prereg-lecture-sondes-barreau8-v1-brouillon14.md`, empreinte `5b503e28e6b81285a792575f878642bbd529888cc886e7cd4ddcf80257e39891`. Rapport : `brouillons/barreau8-lecture-sondes-v1/contre-lecture-brouillon14-v1.md`, empreinte `<EMPREINTE DU RAPPORT>`. Conclusion : « PRÊT : le brouillon 14 peut être scellé une fois l'entropie des graines versée et cette entrée de contre-lecture portée au texte, sans autre changement ». **Règle** : le texte scellé ne diffère du texte relu par cette contre-lecture que par cette entrée et par la cellule « état et raison » de F-3, où seule l'entropie tirée remplace le marqueur ; la session mère le vérifie par une comparaison faite par programme, versée avec l'empreinte du texte scellé.`
   (La ligne commence par `- **Contre-lecture 4` pour le motif du validateur, porte deux empreintes distinctes et aucun « À REMPLIR » ; essayée sur copie, point 7.)
5. Comparaison faite par programme (`diff`) entre le brouillon 14 et le texte rempli : **exactement `76c76` et `442c442`**, rien d'autre ; la verser avec l'empreinte du texte scellé et la provenance de l'entropie.
6. `prereg.problemes(<texte rempli>)` doit rendre `[]` ; essai de cette garde sur le cas sain (le texte rempli) et sur deux artefacts (entropie restée ouverte : attendu `['marqueur À REMPLIR restant hors des sections exigées']` ; entrée 4 sans l'empreinte du rapport : attendu `['contre-lecture 4 sans ses deux empreintes (brouillon relu et rapport)']`), versé (R5) ; puis `sceller_prereg` ; puis la ligne `SCELLEMENT-SONDES-IIB` ; l'heure de scellement consignée à côté de l'heure de la première sortie de la course (D-7).

## Conclusion

PRÊT : le brouillon 14 peut être scellé une fois l'entropie des graines versée et cette entrée de contre-lecture portée au texte, sans autre changement

R-1 et R-2 sont portés mot pour mot (rebâtis par programme depuis le rapport du brouillon 13) ; O-6 est corrigée au caractère près ; T-1 à T-4 sont portées mot pour mot, à leur place ; le fait transmis ne change aucune règle ; les trois ajouts du rédacteur sont justes, (a) et (b) nécessaires, (c) utile, aucun n'a d'effet sur le fond ; aucun renvoi mort, aucune option ouverte après le scellement. Le code de la lecture doit encore porter la correction C-1 du rapport d'intégration avant sa ligne de registre (affaire du contrôle de conformité).

## Refus d'outil

Aucun.

Fin réelle : 2026-11-19T04:58:19Z (dernier `date -u` avant le scellement de ce rapport).
