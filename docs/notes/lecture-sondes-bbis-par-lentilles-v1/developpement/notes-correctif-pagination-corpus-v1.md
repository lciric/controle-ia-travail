# Correctif de la pagination de l'arbre du corpus (première passe de la lecture des sondes par la lentille publique) — note du développeur — v1

Écrite le 2026-11-21 par le développeur neuf du correctif, sous le mandat scellé
`docs/notes/lecture-sondes-bbis-par-lentilles-v1/mandats/mandat-developpeur-correctif-pagination-corpus-v1.md`
(`c0c07faaaa36adb1f6d45f2066d337711d6fdc849d7fb916e3253f223f15b96f`, vérifiée ; commit `5fbb46fc`). Pièce de travail (classe C) ;
le code qu'elle décrit est de classe B et attend sa contre-lecture par un agent neuf d'un autre modèle. Base du travail : branche
`claude/brave-galileo-jhp684` au commit `5fbb46fc`. Aucune vue des données, aucune sortie de course lue, aucune requête vers l'hôte des
modèles et des jeux de données, aucune clé lue : tout est éprouvé sur des réponses fabriquées.

## Le défaut (tel que le mandat le relaie)

Au montage, avant tout téléchargement long, le code fait l'essai d'un octet sur « un fichier de chaque jeu de données du corpus des
jetons gardés » (texte de lecture v1 scellé, « Plan d'analyse », point 4). Pour trouver ce fichier, `cibles_corpus`
(`src/controle_ia/lentilles_sondes_bbis/montage_v1.py`, lignes 633 à 654) demande l'arbre récursif du jeu et y prend le plus petit
chemin d'un fichier de données. Or l'hôte sert cet arbre **par pages** (lien de la page suivante dans l'en-tête `Link`, relation
« next »), et `cibles_corpus` ne lit que la première. Pour le jeu de la tranche zh, la première page ne porte que des dossiers : arrêt
nommé « jeu de données de la tranche zh : aucun fichier de données dans l'arbre », alors que l'arbre en porte.

## Voie choisie : suivre les pages — voie (a) du mandat

- **Voie (b) écartée** (demander l'arbre du seul dossier des données) : le chemin du dossier ne se tire ni de la provenance ni du code
  voisin sans règle nouvelle. La provenance que le code lit ne porte que `repo` et `revision` ; la copie versée du script voisin
  `scripts-01_lens_corpus.py.txt` (dossier `docs/sources/neuron-lens-lecture-20261113/depot-neuron-lens/`) montre qu'une provenance
  n'y porte, pour le fichier, que son nom nu (`path.name`), pas son dossier ; le script du corpus d'activations n'est pas dans les
  copies versées. Écrire le dossier dans le code serait une règle neuve, propre à un jeu.
- **Voie (a) retenue**, la plus petite : même adresse de départ (`montage_v1.url_arbre`), mêmes extensions, même tri ; les pages sont
  suivies dans l'ordre où l'hôte les sert, jusqu'à la **première page qui porte un fichier de données** ; la cible est le plus petit
  chemin de cette page. Quand la première page porte un fichier, le résultat est celui de l'ancien code (essai d'égalité). Le texte
  n'exige qu'« un fichier » du jeu : aucune exigence du texte ne change.
- **Le transport** : `montage_v1` n'est pas touché. Le protocole `Transport` ne rend que des octets, sans en-tête ; la lecture d'une
  page avec son lien de suite est donc ajoutée dans le module neuf : `page_requests` passe par l'ouverture du transport réel
  (`TransportRequests._ouvrir`, appelée **sans clé**), lit le contenu et l'en-tête `Link` ; `lire_page` l'emploie pour le transport
  réel, emploie la méthode `page` d'un transport simulé qui en porte une, et **arrête** pour tout autre transport (lire la seule
  première page par `octets` referait le défaut en silence : aucun repli). Ce choix évite de changer, dans le lanceur, la ligne qui
  construit le transport : seul l'appel à `cibles_corpus` y change, comme le mandat le demande.

## Ce que le module neuf garde, et ses arrêts

| garde | arrêt nommé | cas sain | artefact |
|---|---|---|---|
| arbre fini sans fichier de données | la phrase de `montage_v1`, mot pour mot : « jeu de données de la tranche … : aucun fichier de données dans l'arbre : arrêt ; nœud » | fichier en deuxième page trouvé | arbre d'une et de trois pages de dossiers ; phrase comparée à celle de l'ancien code |
| le défaut lui-même | (ancien code) la même phrase | module neuf sur la même réponse paginée : fichier trouvé | `montage_v1.cibles_corpus` sur la même réponse : arrêt ; de même `lanceur_v7.monter` sur un monde des jouets à l'arbre paginé |
| borne du nombre de pages (`BORNE_PAGES` = 100 par jeu) | « plus de 100 pages d'arbre lues sans fichier de données (borne du nombre de pages) : arrêt avant tout téléchargement long ; nœud » | fichier à la page de rang égal à la borne : trouvé | pages sans fin : arrêt après exactement 100 pages ; fichier à la page de rang borne + 1 : arrêt |
| lien de page suivante hors de l'arbre du jeu demandé (autre hôte, hôte au nom prolongé, autre protocole, autre jeu, interface des modèles, adresse de fichier) | « le lien de la page suivante sort de l'arbre du jeu demandé : il n'est pas suivi : arrêt avant tout téléchargement long ; nœud » | lien du même jeu avec un curseur, ou avec la révision écrite autrement : suivi | six adresses fabriquées : arrêt, l'adresse proposée n'est jamais demandée ni citée |
| transport sans lecture de page | « transport sans lecture de page … : arrêt avant tout téléchargement long ; nœud » | transport simulé de la version 8 des jouets | transport simulé de la version 7 des jouets (octets seuls) : arrêt, aucune requête |
| requête refusée sur une page | la phrase de `montage_v1` : « essai d'un octet refusé (jeu de données de la tranche …) : … : arrêt avant tout téléchargement long ; nœud » | sans refus | refus de la première page (phrase égale à celle de l'ancien code) et de la deuxième ; transport réel sur session fabriquée : code 403, requête impossible, lecture interrompue |
| provenance absente ou illisible | la phrase de `montage_v1` | provenances présentes | provenance « chat » absente (phrase égale à celle de l'ancien code) ; provenance « code » illisible |
| la clé | — | — | aucune fonction du module ne reçoit la clé ; les en-têtes envoyés par le transport réel sont `{"Accept-Encoding": "identity"}` seulement ; les messages ne portent ni le texte d'une exception, ni un curseur ; le montage entier n'écrit la fausse clé dans aucun fichier |

Essai des essais (R5) : `outils/essai-des-essais-corpus-pagine-v1.py` défait douze lignes du module dans une copie jetable hors du
dépôt ; les douze défaites font tomber le fichier d'essais (`outils/sortie-essai-des-essais-corpus-pagine-v1.txt`).

## Le lanceur de la version 8

`lanceur_v8.py` est fabriqué de `lanceur_v7.py` (commit `cc7f4576`, `a5d6fc7b…`) par `outils/fabrique-lanceur-v8-v1.py`, par
remplacements exacts trouvés une fois chacun. Différences, toutes tenues par un essai (`difflib`) : sept lignes ajoutées à la
docstring d'en-tête (paragraphe « Version 8 ») ; une ligne d'import (`from . import corpus_pagine_v1 as cp`) ; la ligne des modules
(`corpus_pagine_v1` et `lanceur_v8` : quatorze modules, la fiche du code doit porter l'empreinte du module neuf, essai sain et deux
artefacts) ; l'appel `cp.cibles_corpus(voisin, transport)` à la place de `mo.cibles_corpus(voisin, transport)`. Aucune autre ligne.

Essais du lanceur de la version 7 rejoués contre la version 8 : l'outil de fabrique copie sous des noms neufs les dix fichiers qui
importent `lanceur_v7` (jouets compris), comme à chaque version précédente. Accords, tous dans l'outil : le transport simulé des
jouets reçoit une méthode `page` et une table `suites` ; dans le fichier des essais du lanceur, les deux essais qui comptaient
treize modules et comparaient la liste à celle de la version 4 en comptent quatorze ; dans le fichier de la garde du fichier
d'arrêt, les deux derniers essais (fabrique de la version 7 rejouée ; lignes retirées de la version 6 à la version 7) sont retirés
de la copie, leurs pareils pour la version 8 étant dans le fichier neuf. Aucun ancien fichier d'essais n'est réécrit.

## Dépendance

`requirements-cpu.txt` : ligne `requests==2.34.2` ajoutée (les autres lignes sont épinglées). C'est la dernière version publiée au
registre public des paquets le 2026-11-21, installée ici avec `urllib3` 2.8.0, `certifi` 2026.11.20, `idna` 3.20,
`charset-normalizer` 3.5.2. Je ne sais pas quelle version l'opérateur a employée (je ne lis aucune sortie de course) : voir le nœud 3.

## Environnement des essais

Python 3.13.18 ; torch 2.14.1 (roue pour processeur) ; numpy 2.4.6 ; scipy 1.17.1 ; pytest 9.1.1 ; transformers 5.18.0 ;
tokenizers 0.23.2 ; safetensors 0.8.0 ; huggingface_hub 1.33.0 ; matplotlib 3.11.2 ; requests 2.34.2. Environnement virtuel propre
à l'arbre de travail isolé ; rien n'a été installé dans l'environnement de l'autre développeur.

## Fichiers et empreintes (SHA-256)

Changé (un seul fichier existant) :

| fichier | empreinte |
|---|---|
| `requirements-cpu.txt` | `587cfe9221ebbebd39c508a7eb235656322f402f1d58676e054c87b486900fdf` |

Neufs — code :

| fichier | empreinte |
|---|---|
| `src/controle_ia/lentilles_sondes_bbis/corpus_pagine_v1.py` | `77fb4356cc18587873541dab6d9b4b55a108a13e06dd205ffe9b3fcae4305404` |
| `src/controle_ia/lentilles_sondes_bbis/lanceur_v8.py` | `0bba5d4e68fd193ded87426105252bdf554c7c93b9e422164916d1b6b7df57b3` |

Neufs — essais (le premier est écrit à la main ; les dix autres sont les copies écrites par l'outil de fabrique) :

| fichier | empreinte |
|---|---|
| `tests/test_lentilles_sondes_bbis_corpus_pagine_v1.py` | `87fd585e36802ab168f8d0c29053b944268d7179117f6915012844c6830ec7ff` |
| `tests/lentilles_sondes_bbis_jouets_v8.py` | `25d3af142138299df45dfd68d82891f252576e9532a5cadd4ca56079ada0e23b` |
| `tests/test_lentilles_sondes_bbis_addendum_concentration_v6.py` | `2270850d51970163c2ce469875cf9a2c304956a095f0ce2ce0f6eeecff473d3b` |
| `tests/test_lentilles_sondes_bbis_corrections_contre_lecture_v7.py` | `a01ca71467ca1e3648a8a619fb5123b2c0e1f35c0fd5d603838a847f94be5a7c` |
| `tests/test_lentilles_sondes_bbis_garde_egalite_v5.py` | `9748877480a69421366934d140ce9cdd4518d834d2a7597614b102524392f256` |
| `tests/test_lentilles_sondes_bbis_gardes_non_vues_v7.py` | `f7beb665af1795697e1b5d36122d3ffc91ac0c1ae82c5364b98ade090ced3e3b` |
| `tests/test_lentilles_sondes_bbis_montage_v8.py` | `1d469ca3ab6e4d555aa0c1908d209e53f0ed6c2c1bd3ab4298db8512045e9e45` |
| `tests/test_lentilles_sondes_bbis_procedure_v8.py` | `65c9c28075133c3734b4d13591348f4148fa39abfdc49174004653d320336c91` |
| `tests/test_lentilles_sondes_bbis_lanceur_v8_v1.py` | `7586aac8978e80b2dd622ff0a313b9672e18c6c5dfe2add1018ff8d09fdc9a8a` |
| `tests/test_lentilles_sondes_bbis_lanceur_v8_interruptions_v1.py` | `803cd6a1bae1400dde0b050e91d04a761d91554a93d5c5a1d0ba9a611af6e51f` |
| `tests/test_lentilles_sondes_bbis_lanceur_v8_garde_arret_present_v1.py` | `fbded7fc3edd55dd0a60f733ebbc53e319970d7c789df42026615b277e0119e1` |

Neufs — outils et leur sortie (dossier `docs/notes/lecture-sondes-bbis-par-lentilles-v1/developpement/outils/`, chacun scellé) :

| fichier | empreinte |
|---|---|
| `fabrique-lanceur-v8-v1.py` | `85db1533c3a162bb94eb1c3635ac7b414e4d711648760d0c9173692ec3c84588` |
| `essai-des-essais-corpus-pagine-v1.py` | `5f9ec6d3e321067fa85120fbaf729f2096b15787da954ff5e84f34965b63cc6c` |
| `sortie-essai-des-essais-corpus-pagine-v1.txt` | `5b1fc9ee4afb6f2380b423b74dc2d405e5cc7762aac1d89bc7393dcd9250c6eb` |

Non modifiés, pour repère : `montage_v1.py` `199e5e18b388db80cb42ca19af4dba577be057deb8124fd994c53159c34714c1` ;
`lanceur_v7.py` `a5d6fc7bd7abf2b191bc56cc7092e503e56362f4714a5f72a3e7d483a30fc4d9`.

## Essais (comptes seulement)

- **Fichier neuf du correctif** (`tests/test_lentilles_sondes_bbis_corpus_pagine_v1.py`) : 46 essais, 46 réussis, 0 échoué.
- **Paquet entier** (`tests/test_lentilles_sondes_bbis_*.py`, 61 fichiers, essais de l'autre développeur présents sur la branche
  compris), lancé en trois parts menées de front sur le code définitif (41 à 48 minutes chacune) : **2 463 essais ; 2 462 réussis,
  1 échoué** au premier passage. L'échec : dans la copie du fichier des essais du lanceur, l'essai de la fiche du code à la liste
  de modules de la version 4 attendait le refus sur l'empreinte du lanceur, et le refus tombe d'abord sur l'empreinte du module
  neuf (lue avant celle du lanceur). C'est la copie de l'essai qui était à accorder, pas le code : accord ajouté à l'outil de
  fabrique (l'essai vérifie les deux refus, l'un après l'autre), copie refabriquée. **Rejoué après l'accord** : ce fichier et le
  fichier neuf du correctif, 87 essais, 87 réussis. Bilan sur les fichiers définitifs : **2 463 essais, 2 463 réussis, 0 échoué**
  (2 462 du passage en trois parts, plus l'essai accordé rejoué). Aucun fichier de code n'a changé entre le passage et le rejeu.
- **Essai des essais** : 12 défaites du module, 12 vues, 0 inaperçue.
- **Non lancé** : le reste de la suite du dépôt (hors `tests/test_lentilles_sondes_bbis_*.py`) ; le correctif ne touche aucun
  module employé ailleurs.

## Nœuds et limites (rien de tranché par moi au-delà de ce que le mandat demande)

1. **La borne de 100 pages est un choix du développeur.** Le mandat demande une borne, sans valeur. À 1 000 entrées par page, 100
   pages couvrent 100 000 entrées avant le premier fichier de données. Je n'ai vu ni l'arbre réel ni sa taille : si le premier
   fichier de données du jeu de la tranche zh vient plus loin, l'arrêt nommé de la borne le dira, et la valeur se change par un
   paramètre (`borne`) ou par une version neuve du module.
2. **La forme réelle de l'en-tête `Link` n'a pas été observée** (aucune requête permise). Le module lit la forme standard
   (`<adresse>; rel="next"`, plusieurs liens séparés par des virgules, adresse relative ou absolue). La garde du lien exige que
   l'adresse proposée reste sur l'hôte de `montage_v1`, sous `/api/datasets/<jeu>/tree/` ; la révision et la requête du lien ne
   sont pas comparées, pour ne pas arrêter si l'hôte écrit la révision autrement dans son lien. Si l'hôte écrivait le nom du jeu
   autrement que la provenance, l'arrêt nommé « le lien de la page suivante sort de l'arbre du jeu demandé » le dirait.
3. **Version de `requests`** : épinglée à la dernière publiée ; à accorder à celle de la machine de l'opérateur si elle diffère.
4. **Le fichier choisi peut différer de celui que l'ancien code aurait pris sur un arbre entier** : l'ancien code triait toute la
   réponse (qu'il croyait entière) ; le module neuf prend le plus petit chemin de la première page qui porte un fichier de données.
   Le texte n'exige qu'un fichier du jeu ; lire toutes les pages pour trier l'arbre entier coûterait des dizaines de requêtes sans
   rien ajouter à l'essai d'un octet. Choix déclaré, à confirmer par le contre-lecteur.
5. **Page illisible comme JSON** : comme dans `montage_v1`, aucune garde propre (l'erreur de décodage remonte telle quelle) ; je n'ai
   pas ajouté d'arrêt nommé neuf, faute de règle dans le texte.
6. **La fiche du code** devra porter l'empreinte de `corpus_pagine_v1.py` et de `lanceur_v8.py` (quatorze modules) ; je n'écris pas
   la fiche et n'inscris aucune ligne de registre.
7. **Lignes de commit** : le mandat demande `Co-Authored-By: Claude <noreply@anthropic.com>` et aucun nom de modèle dans les
   commits ; je l'ai suivi.

## Refus d'outil (déclarés, non rejoués)

Trois refus du garde de l'arbre de travail isolé, tous de forme (« commande trop complexe pour vérifier qu'elle reste dans l'arbre
de travail »), chacun avec la consigne de découper en commandes simples : (1) la première commande, qui enchaînait `git fetch`,
`git checkout` et des lectures ; (2) une commande qui activait l'environnement virtuel par `. .venv/bin/activate` ; (3) une commande
qui écrivait un fichier par redirection puis le lançait. Aucune n'a été rejouée telle quelle ; j'ai suivi la consigne du garde
(commandes séparées, binaires de l'environnement virtuel appelés par leur chemin, fichiers écrits par l'outil d'écriture). Aucun
refus du crochet de calcul ni du classifieur.

## Expositions

Aucune. Lus : `CLAUDE.md` ; les deux mandats ; du texte de lecture v1 scellé (lu par `git show origin/main:…`, empreinte
`ca5066d7…` vérifiée) les titres de section et les lignes qui parlent d'octet, de corpus, d'arbre et de provenance (la ligne de
titre de la liste « Jamais ouverts » est sortie d'une recherche par mot, tronquée à 400 caractères : elle nomme un motif de chemin
de fichiers de scores, sans aucun contenu ; je n'ai pas ouvert la liste) ; `montage_v1.py`, `lanceur_v7.py`, `constantes_v1.py`
(lignes cherchées) ; les essais et jouets des versions 7 ; l'outil de fabrique de la version 7 ; des copies versées du code voisin,
les lignes cherchées par mot (`provenance`, `repo`, nom du jeu). Jamais lus : `diag/`, `runs/`, `docs/verdicts/`, branches
`calcul/*`, `donnees/*`, `verdict/*`, aucun `arret.json`, aucune sortie de course.
