# Contre-lecture neuve, par Claude Opus 5.5, du programme d'enchaînement de la lecture de la discrétion (version 3) et du programme de l'aire conditionnelle (version 1) — bras A des organismes discrets

Contre-lecteur neuf (n'a écrit ni le texte, ni le code, ni les essais, ni les notes), le 23 novembre 2026, sur processeur seul, sans réseau hors le poussage de cette note, sans dépense. Objet de la règle GO-2026-11-22-145 : les pièces écrites par Claude Opus 5.5 à la place de Claude Fable 5.2 sont contre-lues par un Opus neuf ; les deux programmes n'avaient eu jusqu'ici que des contre-lectures Sonnet. **Remarque** : 13.2 demande un contre-lecteur « d'un autre modèle » que le rédacteur ; le rédacteur des deux programmes est Claude Opus 5.5, comme moi : c'est la règle de GO-2026-11-22-145 qui fonde cette contre-lecture, non la lettre de 13.2.

## Pièces lues (empreintes recalculées)

| pièce | sha256 |
|---|---|
| texte scellé du bras A, `prereg/T0.7-organismes-discrets-v-a-v2-pour-scellement.md` — 3.5 (b), 6.3 (m) et (n), 6.9, 8.4 (par endroits), 8.7, case « commit du code » de 13.1, ligne « programme d'enchaînement » de 13.2 | `b4fbfb4e6cddfdc4775119a3e42a61045460ce8cee18a341834155ef1367a0cd` |
| enchaînement, `src/controle_ia/organismes_discrets/enchainement_discretion_bras_a_v3.py` | `05126df34a6f8c33a2ef94f8471d1eda96a69cde4534313b28392bd75e76410c` (égale à 13.1) |
| aire conditionnelle, `src/controle_ia/organismes_discrets/aire_conditionnelle_bras_a_v1.py` | `0f1e76409e07b7535b2e18bf312ff031164608a77b010a46d2dd847e45696df2` (égale à 13.1) |
| analyse, version 13 (signatures des trois fonctions composées et de la garde de sortie) | `a7ebf29f653d417a4f211f9809576a0e70b91ae7840759607c6f3cb7f84946cf` (égale à 13.1 et à la constante du programme) |
| `tests/test_enchainement_discretion_bras_a_v3.py` | `c5f5319c9275cf3ce08689d3618d8e64515a702004f132d0ef6147efecb54533` |
| `tests/test_aire_conditionnelle_bras_a_v1_par_enchainement_v3.py` | `e875477e72040350ca09cb2cd67a9dd9f6cd890c939a78539efc5ca156851213` |

Notes lues : note du code de l'enchaînement v2, note de l'aire conditionnelle v1, contre-lecture Sonnet de l'enchaînement v1 (`contre-lecture-enchainement-discretion-v1-v1.md`), contre-lecture Sonnet de l'aire conditionnelle (`contre-lecture-aire-conditionnelle-bras-a-v1.md`). Les chemins cloisonnés que cite le texte n'ont pas été suivis. Aucun fichier du dépôt n'a été modifié hors cette note ; scénarios et mutations sur copies de fichiers nommés, dans le bloc-notes de la session.

## Verdict : à corriger — aucun défaut bloquant ; deux défauts majeurs à trancher ou corriger avant l'épreuve de forme de bout en bout ; une branche majeure non éprouvée, que cette épreuve doit couvrir

Ce que 13.2 et 8.7 demandent est fait : constat de lancement par la commande du programme, dans la même exécution que la lecture ; étape (m) ; **versement du dossier de course entier — commit du seul dossier, poussage vérifié sur le distant — avant tout rendu**, et rien n'est rendu si le poussage échoue ; l'étape (n) ne part qu'après ; chaque pièce scellée ensuite (constat, acte de reprise, fichier des grandeurs, fichier d'arrêt) est versée avant la suivante ; le compte rendu porte la commande et l'empreinte de chaque programme joué, dont l'enchaînement lui-même et le programme de l'aire conditionnelle. Le programme de l'aire conditionnelle ne rend que les aires (3.5 (b)). Les défauts sont de procédure et de preuve, non de fuite.

## Conformité, point par point

| exigence | constat |
|---|---|
| constat de lancement par le programme, jamais à la main (13.2 ; conventions) | conforme : commande `sys.executable programme_du_constat …`, mode constat ou contrôle, ligne à huit champs exigée, versé avant la lecture ; malsain : rien ne part |
| étape (m) puis versement avant tout rendu (8.7) | conforme : fichier de l'étape (m) écrit par l'analyse, `del` des résultats, `verser(…, "étape (m)")`, puis seulement la relecture du fichier scellé pour le déclencheur « au moins une dose en C6 » ; `EchecDuVersement` est relancée telle quelle (premier `except`), la commande sort sur le code 7 sans compte rendu ; relancé, l'enchaînement pousse d'abord (versement d'ouverture) |
| étape (n) après le versement ; chaque pièce scellée versée avant la suivante | conforme : constat → versement ; (m) → versement ; acte de reprise → versement avant le lancement du programme ; fichier des grandeurs → versement ; arrêt → versement avant le rendu |
| empreinte au manifeste | conforme dans le compte rendu (`programmes` : neuf modules, programme du constat, enchaînement, programme de l'aire après vérification ; `commande` avec `-m MODULE`) ; rien n'est rendu sur un versement en échec ou une garde d'avant l'ouverture (le manifeste doit alors citer la commande par la session) |
| aire conditionnelle : « ne rend que les aires (valeur, intervalle, comptes), jamais une ligne du fichier » (3.5 (b)) | conforme : sortie standard à deux clés (`aires`, `cles`), chaque aire à dix champs passée par `exiger_sortie_de_l_aire_conditionnelle` dans le programme (par l'analyse) puis de nouveau dans l'enchaînement ; sur garde, une ligne d'erreur sans le message de l'analyse ; l'enchaînement ne garde que le nombre d'aires et l'empreinte du fichier des grandeurs, confronté aux aires rendues |
| cloisonnement | conforme : l'enchaînement ne nomme ni n'ouvre le fichier des scores par unité (chemin passé tel quel), le refuse sous le dossier de course ; garde statique v14 jouée sur `src` et `scripts` avant tout constat ; programme lancé depuis une copie de ses octets vérifiés |

## Essais rejoués

`python -m pytest -q tests/test_enchainement_discretion_bras_a_v3.py tests/test_aire_conditionnelle_bras_a_v1_par_enchainement_v3.py` : **101 réussis, 0 échec** (114 s).

## Défauts

### Bloquants

Aucun.

### Majeurs

**MA-1 — La liaison de l'entrée est écrite et versée dès l'ouverture, avant tout constat et toute lecture : une coquille de l'entrée découverte avant la lecture ne se corrige plus sous ce rang.** `lier_l_entree` est appelée avant le bloc `try`, puis versée avec l'ouverture ; toute exécution suivante dont les données diffèrent est refusée. **Scénario rejoué** (copie de l'essai de bout en bout) : première exécution avec des états de la base fautifs et un programme de l'aire introuvable → garde ordinaire, aucun constat, aucun fichier de l'étape (m) ; seconde exécution, coquille corrigée → « entrée de l'enchaînement changée depuis la liaison du rang 1 — refusé ». Rien n'a été lu, mais la seule issue est un rang neuf (configuration neuve, inscription). La liaison n'a de raison qu'entre (m) et (n) (D2 de la contre-lecture v1). Correction : sceller la liaison juste avant la lecture de l'étape (m), après le constat sain (elle part avec le versement de (m)), ou admettre son remplacement tant qu'aucune ouverture de lecture ni aucun fichier de l'étape (m) n'existe pour le rang ; essai sain et artefact. Parade sans code, si l'enchaînement reste gelé : faire contre-lire l'entrée scellée avant le premier lancement, et le dire au manifeste.

**MA-2 — « Remis après la ligne scellée de la table C » (3.5 (b), 6.9, 8.4, 13.2) n'est pas tenu par une exécution unique.** L'entrée scellée nomme le fichier des scores par unité avant l'étape (m), et l'enchaînement joue (m) puis (n) sans rendre la main : à suivre le chemin naturel, le fichier est sur l'instance d'analyse avant la table C. Rien ne l'ouvre avant (n) — la barrière « aucun agent n'ouvre » tient —, mais la lettre est contredite, et ni le code ni les notes n'en disent rien. **Scénario rejoué** : la lettre se tient en deux exécutions — la première sans le fichier : (m) jouée et versée, puis arrêt « garde ordinaire » du programme de l'aire, versé ; le fichier remis ; la seconde joue « étape (n) seule » et aboutit — au prix d'un arrêt versé qui n'en est pas un. À trancher (nœud : lecture du texte) : (a) lire « remis » comme « passé au programme de l'aire par l'enchaînement, après le versement de (m) », consigné comme lecture ; (b) écrire au manifeste la procédure en deux exécutions et la jouer à l'épreuve de forme ; (c) une version 4 avec un mode « étape (m) seule ». Recommandation : (b) sans code neuf, confiance 0,6.

**MA-3 — Non éprouvé : la branche des livraisons refaites.** Aucun essai de l'enchaînement ne joue une livraison refaite (ligne de GO, registre figé, acte de reprise) : ni la reprise de toute la lecture après un arrêt de (m), ni la reprise de l'étape (n) avec sortie d'origine — confrontation des liaisons des deux rangs, `ouvrir_la_reprise_de_l_etape_n`, versement de l'acte, **vrai programme lancé avec `--sortie-d-origine`**, confrontation au fichier des grandeurs de la livraison refaite. Seul le refus « reprise sans sortie d'origine » est essayé, `_a_jouer` remplacé. 8.7 exige de l'épreuve de forme « un arrêt à chaque étape et sa reprise » : c'est elle qui doit couvrir cette branche, avant toute dépense.

### Mineurs

- **mi-1 — Version annoncée fausse.** La v3 garde `VERSION = 2` et la description `(version 2)` : le compte rendu, donc le manifeste de course, porte `"version": 2` ; seule l'empreinte de `programmes.enchainement` distingue la v3. Docstrings périmées (enchaînement : « aucun programme du dépôt ne remplit encore ce contrat », garde v13, brouillon 55 ; aire : « enchaînement version 2 »). La différence v2→v3 est gelée et déclarée : à dire au manifeste plutôt qu'à corriger.
- **mi-2 — R5 : deux gardes du programme de l'aire sans artefact.** Le contrôle d'après import (module chargé = fichier vérifié, même empreinte) et le préfixe de cache vide n'ont aucun essai : mutants « contrôle d'après import retiré » et « préfixe de cache retiré » **survivent** aux essais (10 réussis chacun). Vérifié à la main que la défense tient : un `.pyc` malveillant posé dans `__pycache__` (horodatage et taille de la vraie source) n'est pas exécuté par le vrai programme, et l'est par le mutant. Les `__init__.py` des deux paquets, exécutés à l'import, ne sont pas vérifiés et la limite (a) ne les nomme pas. Même classement que D7 de la contre-lecture v1.
- **mi-3 — Échec d'import de l'analyse ou de ses dépendances : trace brute, code 1**, hors du contrat (0, 2, 3, 4, 8) ; l'enchaînement n'en rend rien (garde « arrêt sans aires »), aucune donnée n'est lue à ce moment : sans fuite.
- **mi-4 — Le versement committe en silence la destruction d'une pièce versée.** `git add -A` prend aussi les suppressions et retouches de fichiers suivis. Scénario rejoué : course aboutie, constat de lancement effacé, nouvelle exécution → le versement d'ouverture committe la suppression, l'issue est une garde ordinaire et le compte rendu n'en dit rien. 8.7 se contente de la trace de l'historique ; il est peu coûteux que le versement refuse, ou au moins nomme, toute suppression ou retouche d'un fichier déjà suivi du dossier de course.
- **mi-5 — Empreintes relevées, non confrontées.** L'enchaînement relève les empreintes sur disque des modules qu'il importe et prend celle du programme de l'aire dans son entrée ; il ne les confronte pas à 13.1. C'est la garde de procédure de 8.7 (contre-lecteur du manifeste) ; à noter qu'un `.pyc` substitué ferait mentir ce relevé, l'enchaînement n'ayant pas la défense du programme de l'aire.
- **mi-6 — Arrêt à l'étape (n) : la « livraison refusée » versée est la sortie de la lecture commune**, non le fichier des scores par unité, qui ne se verse pas par son contenu (13.2). Cohérent, mais à dire au manifeste : le fichier refusé n'est versé que par son empreinte (déclarée dans la sortie).

## Ce qui reste non éprouvé

1. La branche des livraisons refaites (MA-3), dont la reprise de l'étape (n) par le vrai programme.
2. La commande réelle de bout en bout sur le dépôt de travail, avec un distant réel : les essais emploient un dépôt nu local ; l'épreuve de forme (8.7) reste à faire.
3. Les codes 2 (arguments) et 8 (erreur inattendue) du vrai programme de l'aire ; un fichier des grandeurs écrit sans ligne rendue (programme tué entre les deux) : l'étape (n) ne se rejoue plus, l'enchaînement rend une garde — cas sans essai.
4. La procédure de remise du fichier après la table C (MA-2), à jouer à l'épreuve de forme sous la forme retenue.

## Ordre proposé

MA-2 (décision de lecture) et MA-1 (correction ou parade), puis l'épreuve de forme de bout en bout couvrant MA-3 et les points 2 à 4 ci-dessus ; les mineurs vont au manifeste de course (mi-1, mi-5, mi-6) ou à une version suivante (mi-2, mi-3, mi-4).
