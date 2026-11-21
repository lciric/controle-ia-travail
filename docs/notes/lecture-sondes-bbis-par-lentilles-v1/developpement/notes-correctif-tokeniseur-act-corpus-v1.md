# Correctif du tokeniseur pour le script voisin du corpus des jetons gardés (première passe de la lecture des sondes par la lentille publique) — note du développeur — v1

Écrite le 2026-11-21 par le développeur neuf du correctif, sous le mandat scellé
`docs/notes/lecture-sondes-bbis-par-lentilles-v1/mandats/mandat-developpeur-correctif-tokeniseur-act-corpus-v1.md`
(`4420c6df06ff…`, vérifié par `controle_ia.scellement verifier`). Pièce de travail (classe C) ; le code qu'elle décrit est de
classe B et attend sa contre-lecture par un agent neuf d'un autre modèle. Base du travail : branche
`claude/brave-galileo-jhp684`. Aucune vue des données, aucune sortie de course lue, aucune requête vers l'hôte des modèles et
des jeux de données, aucune clé lue : tout est éprouvé sur un tokeniseur jouet, contre une porte simulée sur la machine.

## Le défaut (tel que le mandat le relaie, puis reproduit ici)

Le montage joue trois fois du code du voisin qui charge le tokeniseur : le script du corpus des jetons gardés
(`scripts/05_act_corpus.py`), **en ligne** parce qu'il lit les jeux de données ; puis le comptage des jetons et la liste des
jetons gardés, hors ligne. Aucun de ces enfants ne reçoit la clé (`montage_v1.environnement_enfant`). Le cache posé par
`montage_v1.poser_cache_tokeniseur` porte les quatre fichiers `.json` vérifiés (tokeniseur, sa configuration, ses jetons
spéciaux, la configuration du modèle).

Hors ligne, la bibliothèque de chargement ne lit que le cache : cela suffit, et l'essai hors ligne du montage le prouvait.
En ligne, la même bibliothèque (lecture du code installé, `transformers` 5.18.0, `utils/hub.py` et
`tokenization_utils_base.py`) :

1. résout la branche principale du dépôt en son commit par l'interface du dépôt, sans clé ;
2. pour ce commit, tient le cache pour complet **seulement** pour les fichiers qu'il porte ou qu'il marque absents
   (dossier `.no_exist/<commit>/` de la bibliothèque des téléchargements) ;
3. demande tout autre fichier de tokeniseur qu'elle connaît à l'hôte, qui répond par le refus du dépôt à porte (code 401)
   puisque l'enfant n'a pas la clé ; ce refus n'est pas rattrapé : le chargement s'arrête.

Le premier fichier ainsi demandé est `tokenizer.model` : c'est l'arrêt relayé (script du corpus, refus 401 sur
`tokenizer.model`, à la révision `0e9e39f2…`).

**Reproduit localement** (outil `outils/porte-locale-chargement-tokeniseur-v1.py`, sortie
`outils/sortie-porte-locale-chargement-tokeniseur-v1.txt`) : un enfant en ligne et sans clé charge un tokeniseur jouet posé
comme l'ancien cache, contre une porte simulée sur 127.0.0.1 dont l'interface répond sans clé et dont tout fichier est
refusé par le code 401 du dépôt à porte. Résultat : le même refus, sur `…/resolve/0e9e39f2…/tokenizer.model`.

## `tokenizer.model` existe-t-il à la racine du dépôt à cette révision ? — établi sur pièce versée : non

Pièce : `traces/hf-revisions-20261006-1645/hf-Llama-3.1-8B-Instruct.json`
(`ad6bed0351346a2d804310234ccd7629020239bc3bb9133d372eb3d83275d5c3`, égale à la ligne de `empreintes.sha256` du même
dossier), réponse brute de l'interface publique du dépôt, relevée sans clé le 2026-10-06. Son champ `sha` est la révision
épinglée (`0e9e39f249a16976918f6564b8830bc894c89659`) ; sa liste de fichiers porte dix-sept chemins, dont
`original/tokenizer.model` et **aucun `tokenizer.model` à la racine** ; elle ne porte ni `added_tokens.json` ni
`chat_template.jinja`. Les fichiers de la racine y sont ceux de `constantes_v1.PETITS_LLAMA` et `POIDS_LLAMA`, plus
`.gitattributes`, `README.md`, `generation_config.json`.

Cette pièce date de six semaines. Le code ne s'y fie donc pas : **au montage, l'absence est vérifiée sur l'arbre du dépôt lu
avec la clé** (voir « Les deux cas »).

## Voie choisie : marquer dans le cache l'absence connue — voie (a) du mandat

- **Voie (c) écartée** (poser `tokenizer.model` vérifié) : le fichier n'existe pas à la racine ; et s'il existait, le poser
  demanderait une taille et un identifiant de contenu que le texte ne fixe pas : règle neuve.
- **Voie (b) écartée** (jouer le script du corpus hors ligne pour le seul dépôt du modèle) : le mode hors ligne de la
  bibliothèque des téléchargements est une variable d'environnement du processus entier, qui couperait aussi la lecture des
  jeux de données ; le restreindre au dépôt du modèle demanderait de changer en mémoire le chargement du voisin (remplacer sa
  fonction `tokenizer`, ou forcer un argument de la bibliothèque) depuis un lanceur enveloppant : c'est toucher au voisin,
  et je ne peux pas lire le script du corpus (il n'est pas dans les copies versées) pour savoir ce qu'une telle enveloppe y
  changerait d'autre.
- **Voie (a) retenue**, la plus petite : les fichiers posés ne changent pas ; le cache reçoit en plus un fichier vide
  `.no_exist/<révision>/<nom>` pour chacun des trois noms que la bibliothèque demande et que le dépôt ne porte pas :
  `tokenizer.model`, `added_tokens.json`, `chat_template.jinja`. La clé ne passe à aucun enfant, rien n'est téléchargé de
  plus, le voisin n'est pas touché, le tokeniseur chargé est celui que les enfants hors ligne chargeaient déjà (mêmes
  quatre fichiers).

**Preuve locale de la voie**, aux versions de `requirements-cpu.txt` installées ici (même outil, même sortie) : avec le seul
marqueur de `tokenizer.model`, le refus se déplace sur `added_tokens.json` ; avec les trois marqueurs, le chargement en ligne
et sans clé réussit et **aucun fichier n'est demandé à l'hôte** (trois requêtes à l'interface du dépôt, toutes sans clé). Le
fichier d'essais rejoue ces cas (un marqueur retiré à la fois : refus sur ce nom).

### Les deux cas du mandat, traités par le code

`cache_tokeniseur_v2.poser_cache_tokeniseur` lit, par le transport du lanceur et **avec la clé**, l'arbre de la racine du
dépôt du modèle à la révision épinglée (même adresse que `montage_v1.sha256_par_interface`), avant d'écrire quoi que ce soit :

- **le fichier est absent** (cas établi sur pièce) : le marqueur est écrit ;
- **le fichier existe à la racine** : aucun marqueur n'est écrit ; arrêt nommé avant tout flux long, nœud (« … existe(nt) à la
  racine du dépôt du modèle à la révision du texte … »). La voie (c) demanderait alors une décision sur la taille et
  l'identifiant à épingler.

## Ce que le module neuf garde, et ses arrêts

| garde | arrêt nommé (début) | cas sain | artefact |
|---|---|---|---|
| le défaut lui-même | (bibliothèque) refus du dépôt à porte | cache neuf : chargement réel en ligne et sans clé réussi, aucun fichier demandé | ancien cache : refus sur `tokenizer.model` à la révision épinglée ; un marqueur retiré : refus sur ce nom (trois cas) |
| un nom à marquer existe à la racine | « … existe(nt) à la racine du dépôt du modèle … aucun marqueur d'absence n'est écrit » | arbre de racine sans ce nom ; `original/tokenizer.model` ne compte pas pour la racine | chacun des trois noms présent, comme fichier puis comme dossier ; de même par le montage entier |
| témoin de la lecture de l'arbre (chaque fichier posé y figure comme fichier) | « … posé(s) dans le cache mais absent(s) de l'arbre … » | arbre de racine complet | arbre vide ; un fichier posé manquant ; un fichier posé listé comme dossier ; arbre des jouets de la version 8 (poids seuls) par le montage entier |
| arbre refusé, illisible, de forme inattendue, en double, ou peut-être coupé (1 000 entrées ou plus) | « arbre des fichiers du modèle refusé / illisible / d'une forme inattendue / une entrée en double / il peut être coupé » | 999 entrées : lu | refus de l'hôte, clé absente, mauvaise clé ; octets non décodables, JSON cassé, quatre formes fausses ; 1 000 entrées ; doublon |
| noms de la racine seulement, sans doublon, jamais à la fois posés et marqués | « nom de fichier inattendu », « donné deux fois », « à la fois posé et marqué absent » | les quatre fichiers et les trois noms | sept noms faux (dossier, remontée, vide, point en tête, espace, non-texte) ; doublon ; `tokenizer.json` marqué absent |
| fichier posé d'une autre taille ou d'un autre identifiant que le texte (relu sur disque) | « … d'une autre taille ou d'un autre identifiant de contenu … » | pose saine : relevé égal aux valeurs attendues | identifiant attendu faux ; taille attendue fausse ; un octet changé à taille égale ; fichier allongé |
| l'instantané ne porte que les fichiers posés | « l'instantané ne porte pas exactement les fichiers posés » | pose saine | fichier manquant, de plus, dossier de plus, fichier remplacé par un lien |
| la branche principale du cache désigne la révision épinglée ; une seule branche, un seul instantané | « la branche principale n'y désigne pas la révision du texte », « une autre branche ou une autre révision » | pose saine | autre révision, saut de ligne final, branche absente, cache absent, autre branche, autre instantané ; chargement réel quand la porte rend un autre commit |
| marqueurs exactement ceux attendus, tous vides | « marqueurs d'absence ne sont pas exactement ceux attendus », « … n'est pas un fichier vide » | pose saine ; pose sans nom à marquer (aucun dossier) | manquant, de plus, autre révision, dossier absent, non vide, dossier, lien |
| rien n'est réécrit, rien n'est écrit avant les vérifications | « existe déjà dans le cache », « ne se répondent pas » | pose dans un cache neuf | seconde pose ; attendus incomplets ; après chaque arrêt d'avant la pose, le dossier du cache n'existe pas |
| la clé | — | — | le module n'importe ni réseau, ni processus, ni environnement, et n'appelle jamais la valeur de la clé ; les messages d'arrêt ne portent ni la fausse clé ni une autre ; aucune requête reçue par la porte ne porte d'en-tête de clé ; le montage entier n'écrit la fausse clé dans aucun fichier |

Essai des essais (R5) : `outils/essai-des-essais-cache-tokeniseur-v1.py` défait trente-deux lignes du module dans une copie
jetable hors du dépôt : les trente-deux défaites font tomber les essais du module (`outils/sortie-essai-des-essais-cache-tokeniseur-v1.txt`).

## Le lanceur de la version 9

`lanceur_v9.py` est fabriqué de `lanceur_v8.py` (`0bba5d4e…`) par `outils/fabrique-lanceur-v9-v1.py`, par remplacements exacts
trouvés une fois chacun. Différences, toutes tenues par un essai (`difflib`) : onze lignes ajoutées à la docstring d'en-tête
(paragraphe « Version 9 ») ; une ligne d'import (`from . import cache_tokeniseur_v2 as ct`) ; la liste des modules
(`cache_tokeniseur_v2` et `lanceur_v9` : quinze modules ; la fiche du code doit porter l'empreinte du module neuf, essai sain
et deux artefacts) ; la pose du cache par `ct.poser_cache_tokeniseur` à la place de `mo.poser_cache_tokeniseur` (trois lignes
retirées en tout, liste des modules comprise) ; après l'essai hors ligne du tokeniseur, **un second essai en ligne et sans
clé** (`essayer_tokeniseur_en_ligne`, journal `journal-essai-tokeniseur-en-ligne.txt`), puis la relecture du cache
(`ct.exiger_cache`) ; deux champs du rapport du montage (`cache_du_tokeniseur`, `essai_du_tokeniseur_en_ligne_sans_cle`) ;
deux gardes ajoutées à la liste du rapport. Aucune ligne de calcul n'est changée.

Pourquoi l'essai en ligne (voir le nœud 1) : l'arrêt relayé est tombé dans le script du corpus, donc après les flux de poids
et la lentille. L'essai en ligne fait, avant tout flux long, exactement le chargement que ce script fera, dans le même
environnement d'enfant (sans clé) ; s'il échoue (autre version de la bibliothèque sur la machine de la course, autre fichier
demandé, branche du dépôt déplacée), l'arrêt est nommé et ne coûte aucun flux.

Essais du lanceur de la version 8 rejoués contre la version 9 : l'outil de fabrique copie sous des noms neufs les dix
fichiers qui importent `lanceur_v8` (jouets compris), hors le fichier des essais du correctif de la pagination, propre à la
version 8. Accords, tous dans l'outil : l'arbre du dépôt du modèle des jouets liste aussi les petits fichiers et un dossier
(le témoin de la lecture de l'arbre l'exige) ; dans le fichier des essais du lanceur, les essais qui comptaient quatorze
modules en comptent quinze, l'essai de la fiche du code voit d'abord manquer le module neuf, et la comparaison des gardes du
rapport à celles de la version 4 se fait hors les deux gardes neuves (dont la présence et l'ordre sont vérifiés). Aucun
ancien fichier d'essais n'est réécrit.

## Environnement des essais

Python 3.13.18 ; torch 2.14.1 (roue pour processeur) ; numpy 2.4.6 ; scipy 1.17.1 ; pytest 9.1.1 ; transformers 5.18.0 ;
tokenizers 0.23.2 ; safetensors 0.8.0 ; huggingface_hub 1.33.0 (avec httpx 0.28.1, hf-xet 1.8.0) ; matplotlib 3.11.2 ;
requests 2.34.2. Environnement virtuel propre à l'arbre de travail isolé. `requirements-cpu.txt` n'est pas changé.

## Fichiers et empreintes (SHA-256)

Aucun fichier existant n'est changé.

Neufs — code :

| fichier | empreinte |
|---|---|
| `src/controle_ia/lentilles_sondes_bbis/cache_tokeniseur_v2.py` | `fb4069f71bd3e37fa1188ab3f733138a62223c6cd969b72f1e0f3c091a650f4a` |
| `src/controle_ia/lentilles_sondes_bbis/lanceur_v9.py` | `89d2e23b61ff2a6741aae20e6caca483df0d2c6f1d66235e9f3d20b772f4a065` |

Neufs — essais (le premier est écrit à la main ; les dix autres sont les copies écrites par l'outil de fabrique) :

| fichier | empreinte |
|---|---|
| `tests/test_lentilles_sondes_bbis_cache_tokeniseur_v2.py` | `9eb3f9853cb062d0ab84bff1e208399ac7a0576f12957ff7bdbfb8de785c7696` |
| `tests/lentilles_sondes_bbis_jouets_v9.py` | `9262e0389ab9326b636a2690b2140f4611269fe38bf24160de77563a55d83c2d` |
| `tests/test_lentilles_sondes_bbis_addendum_concentration_v7.py` | `9711e5f4786cc2cb679f97a91c591ebf7b6a2a363b6d9afeef6ae5817f78dcd0` |
| `tests/test_lentilles_sondes_bbis_corrections_contre_lecture_v8.py` | `2fcc1650b63fba4938b50501428967ec0ef01f81af308181b493b906d6f0df47` |
| `tests/test_lentilles_sondes_bbis_garde_egalite_v6.py` | `ca49c0e876bed22a88f2c6901f389feb8f03387ed154e8998e3271fba847d878` |
| `tests/test_lentilles_sondes_bbis_gardes_non_vues_v8.py` | `f00a1afb5184ca42d682537a9399378db93d3d62ea8b6cc68a95d584bbc10923` |
| `tests/test_lentilles_sondes_bbis_montage_v9.py` | `84f0dbe95a8986cb0deec60279b8e6f69d5e4d1ee2d351dbf50b0594000a1365` |
| `tests/test_lentilles_sondes_bbis_procedure_v9.py` | `1ee858c51efb5985323f5ee7cc37f3e1f55b7e9d2d030dd775a72be846727cc1` |
| `tests/test_lentilles_sondes_bbis_lanceur_v9_v1.py` | `bd8050b39a03a1ae587f23949922744d3817234ac072c4747f718f42adb36a06` |
| `tests/test_lentilles_sondes_bbis_lanceur_v9_interruptions_v1.py` | `203ef651b067ce312d124c728042753356fb262a54c6c2b8510f2646aa100ca4` |
| `tests/test_lentilles_sondes_bbis_lanceur_v9_garde_arret_present_v1.py` | `f39176bdb04b6b65d59cef587dd8ece755db381bd05b3a9e2cf2130a18dcc597` |

Neufs — outils et leurs sorties (dossier `docs/notes/lecture-sondes-bbis-par-lentilles-v1/developpement/outils/`, chacun scellé) :

| fichier | empreinte |
|---|---|
| `fabrique-lanceur-v9-v1.py` | `914251beb6ac76a2d5bae9a02f01353b2184059d2b7be32d8c121d3d731413e2` |
| `essai-des-essais-cache-tokeniseur-v1.py` | `565a100957eda5ba8bbf66009d8ff0623ba28cd9a941b0dab1643e353f966960` |
| `sortie-essai-des-essais-cache-tokeniseur-v1.txt` | `57fc63e1ac683b094c9dc4f00b8a835a2979d39d053fb8abc5bde2e2f2ac79b6` |
| `porte-locale-chargement-tokeniseur-v1.py` | `2a4ea93cebfb17176cad037e3282beaa8db3c3367942334f9af9231d2a392799` |
| `sortie-porte-locale-chargement-tokeniseur-v1.txt` | `0a40c93ca6a9f3d276c8266cdb8ae0d41f7a659416a165cab0ba98fe9a4527bb` |

Non modifiés, pour repère : `montage_v1.py` `199e5e18b388db80cb42ca19af4dba577be057deb8124fd994c53159c34714c1` ;
`lanceur_v8.py` `0bba5d4e68fd193ded87426105252bdf554c7c93b9e422164916d1b6b7df57b3` ;
`constantes_v1.py` `9c991d0e41d047bca25e146bc66b7b366301edd08bb4e1aad3709f3d016d2158`.

## Essais (comptes seulement)

- **Fichier neuf du correctif** (`tests/test_lentilles_sondes_bbis_cache_tokeniseur_v2.py`) : 72 essais, 72 réussis, 0 échoué
  (dont six qui jouent le vrai chargement dans un processus enfant contre la porte simulée).
- **Paquet entier** (`tests/test_lentilles_sondes_bbis_*.py`, 75 fichiers, essais de la seconde passe présents sur la branche
  compris), lancé en quatre parts menées de front sur les fichiers définitifs (38 à 46 minutes chacune) : **3 139 essais ;
  3 138 réussis, 1 échoué**.
- **L'échec n'est pas dans le correctif et ne vient pas de lui** : c'est un essai de la seconde passe,
  `test_lentilles_sondes_bbis_seconde_passe_lanceur_v1.py::test_cibles_du_corpus_jamais_celles_de_montage_v1_telles_quelles`.
  Il passe seul (rejoué : 1 réussi) et tombe quand un fichier d'essais chargé avant lui dans le même processus a déjà importé
  `corpus_pagine_v1` : l'essai masque le module dans la table des modules chargés, mais l'import relatif le retrouve comme
  attribut du paquet. Vérifié avec des fichiers d'avant ce correctif seulement (`…_montage_v8.py` puis ce fichier, ce seul
  essai choisi : 1 échoué) : la dépendance à l'ordre existait dès que `lanceur_v8` est entré sur la branche. Je n'ai pas
  touché à ce fichier (seconde passe) ; à reprendre par son développeur (retirer aussi l'attribut du paquet dans l'essai).
- **Essai des essais** : 32 défaites du module, 32 vues, 0 inaperçue.
- **Non lancé** : le reste de la suite du dépôt (hors `tests/test_lentilles_sondes_bbis_*.py`) ; le correctif ne touche aucun
  module employé ailleurs.

## Ce que la seconde passe devra reprendre (je n'ai touché à aucun de ses fichiers)

`lanceur_seconde_passe_v1.py` porte le même défaut, aux mêmes endroits : il pose le cache par
`mo.poser_cache_tokeniseur` (ligne 212), n'essaie le tokeniseur que hors ligne (`l7.essayer_tokeniseur_du_cache`, ligne 216),
puis joue `mo.calculer_jetons_gardes` (ligne 259), dont le script du corpus est en ligne et sans clé. Il s'arrêtera donc au
même point que la première passe. À reprendre, dans une version neuve de ce lanceur :

1. poser le cache par `cache_tokeniseur_v2.poser_cache_tokeniseur(transport, cle, hf_home, poses, attendus, depot, revision)`,
   avec `attendus = {nom: (taille, identifiant) du texte}` pour les fichiers posés ;
2. jouer l'essai en ligne et sans clé après l'essai hors ligne (la fonction est dans `lanceur_v9` ; la seconde passe importe
   aujourd'hui `lanceur_v7`), puis `cache_tokeniseur_v2.exiger_cache` ;
3. ajouter `cache_tokeniseur_v2` à sa liste de modules (fiche du code), et porter au rapport les deux champs neufs ;
4. ses jouets : l'arbre du dépôt du modèle doit lister les petits fichiers posés (accord fait ici pour les jouets de la
   version 9 ; ceux de la seconde passe sont à accorder de même).
Si la seconde passe réemploie un dossier de travail déjà monté par la première (même cache), rien n'est à reposer ; je ne sais
pas ce que son texte en dit et ne l'ai pas lu pour cela.

## Nœuds et limites (rien de tranché par moi au-delà de ce que le mandat demande)

1. **L'essai en ligne et sans clé est un ajout au-delà des marqueurs.** Il fait sortir, d'un enfant sans clé, les mêmes
   requêtes que le script du corpus fera plus tard (interface du dépôt du modèle : trois requêtes au relevé local). Je le
   crois dans l'objet du mandat (« seul ce point change » : le tokeniseur du script joué en ligne) et de même nature que
   l'essai hors ligne ajouté à la version 2, mais c'est une garde neuve du montage : à confirmer par le contre-lecteur. Il se
   retire sans toucher au reste (trois lignes du montage, la fonction, une garde de la liste).
2. **Je n'ai pas lu le script du corpus** (`scripts/05_act_corpus.py` n'est pas dans les copies versées ; je n'ai lu aucune
   sortie de course). Le correctif répare le chargement du tokeniseur par le catalogue du voisin, que le mandat désigne. Si ce
   script demande au dépôt à porte autre chose que le tokeniseur (la configuration du modèle est posée ; tout autre fichier ne
   l'est pas), il s'arrêtera de nouveau, plus loin, et ni les essais ni l'essai en ligne ne le voient.
3. **L'interface du dépôt à porte répond-elle sans clé ?** Je ne l'ai pas observé (aucune requête permise). Deux pièces le
   soutiennent : la trace du 2026-10-06 (réponse de l'interface « sans jeton », d'après son `LISEZMOI.md`) et la forme de
   l'arrêt relayé (le refus porte la révision épinglée, que seule une résolution réussie de la branche principale a pu
   donner à l'enfant, qui ne la reçoit de personne). Dans le monde contraire (interface à porte aussi), relevé localement, le
   chargement en ligne échoue autrement, avant `tokenizer.model`, marqueurs ou non : ce n'est pas le défaut relayé. L'essai en
   ligne du montage tranche sur la machine de la course.
4. **La voie tient tant que la branche principale du dépôt désigne la révision épinglée.** Si elle bouge, la bibliothèque
   en ligne ne lit plus le cache posé (essai de limite) : l'essai en ligne échoue, ou la relecture du cache nomme la cause
   (« la branche principale n'y désigne pas la révision du texte »). Il faudrait alors une autre voie (la voie (b), ou une
   révision passée au chargement du voisin) : décision à prendre, je n'ai rien préparé pour ce cas.
5. **La liste des trois noms tient aux versions épinglées** (`transformers` 5.18.0, `huggingface_hub` 1.33.0) et à la classe
   de tokeniseur que ces versions choisissent. Le tokeniseur jouet imite, de mémoire et sans lire les fichiers réels, ce
   qui compte ici de la configuration du tokeniseur réel (classe déclarée « rapide », gabarit de conversation dans la
   configuration) ; la classe choisie localement demande bien `tokenizer.model` le premier, comme l'arrêt relayé. Sur une
   autre version, ou si le fichier réel orientait la bibliothèque vers un quatrième nom, l'essai en ligne du montage
   l'arrête avant tout flux long, journal à l'appui.
6. **La borne de 1 000 entrées** pour l'arbre de la racine est un choix du développeur, repris de la taille de page relevée
   au correctif de la pagination ; la racine du dépôt porte quatorze fichiers et un dossier d'après la pièce versée. Le témoin (chaque fichier
   posé figure dans l'arbre) garde contre un arbre vide ou tronqué en deçà.
7. **Le lanceur lit l'arbre du dépôt du modèle deux fois** (ici, puis `montage_v1.sha256_par_interface`, inchangé) : une
   requête de plus, avec la clé, vers la même adresse.
8. **La relecture du cache après l'essai en ligne est stricte** (aucun fichier de plus dans l'instantané, marqueurs exacts).
   Localement, le chargement en ligne ne change rien au cache. Si la bibliothèque y écrivait autre chose sur la machine de la
   course, l'arrêt serait nommé, avant tout flux long. Le cache n'est pas relu après le script du corpus : la liste des jetons
   gardés y est déjà vérifiée par son nombre et son empreinte.
9. **La fiche du code** devra porter l'empreinte de `cache_tokeniseur_v2.py` et de `lanceur_v9.py` (quinze modules) ; je
   n'écris pas la fiche et n'inscris aucune ligne de registre.
10. **Lignes de commit** : le mandat demande `Co-Authored-By: Claude <noreply@anthropic.com>` et aucun nom de modèle dans
    les commits ; je l'ai suivi.

## Refus d'outil (déclarés, non rejoués)

Aucun refus du garde de l'arbre de travail isolé, du crochet de calcul ni du classifieur. Deux commandes d'attente ont
dépassé leur délai de dix minutes et sont passées en arrière-plan d'elles-mêmes (ce n'est pas un refus).

## Expositions

Aucune. Lus : `CLAUDE.md` ; le mandat du correctif, celui des deux passes, le mandat et la note du correctif de la
pagination ; du texte de lecture v1 scellé (lu par `git show origin/main:…`, empreinte `ca5066d7…` vérifiée) les lignes
sorties d'une recherche par mot (tokeniseur, cache, scripts du voisin, clé) et les passages du montage, de la table des
fichiers du modèle et du nœud de la clé (lignes 272 à 300, 396 à 436, 685 à 690) — la liste « Jamais ouverts » n'a pas été
ouverte ; `montage_v1.py`, `constantes_v1.py`, `lanceur_v8.py`, les lignes cherchées de `corpus_pagine_v1.py` ; les essais et
jouets de la version 8 ; l'outil de fabrique de la version 8 et l'outil d'essai des essais du correctif de la pagination ;
des copies versées du code voisin, le catalogue en entier, le fichier des dépendances, et les lignes cherchées par mot des
autres ; `requirements-cpu.txt` ; la trace versée `traces/hf-revisions-20261006-1645/` (son `LISEZMOI.md`, ses empreintes, et
du fichier du modèle les noms des champs, le champ `sha` et la liste des fichiers) ; de `lanceur_seconde_passe_v1.py` et
`montage_v2.py`, les lignes sorties d'une recherche par mot (pose du cache, essai du tokeniseur, jetons gardés), sans rien y
écrire. Une recherche du mot `tokenizer.model` dans le dépôt (hors `diag/`, `runs/`, `docs/verdicts/`) a rendu des **noms**
de fichiers, dont un fichier d'essais et deux fichiers de notes de la préparation de T0.7, deux archives de contre-lectures
de T0.4 et T0.5, une note de gabarit et un bloc-notes de passation : je n'en ai ouvert aucun. Jamais lus : `diag/`, `runs/`,
`docs/verdicts/`, branches `calcul/*`, `donnees/*`, `verdict/*`, aucun `arret.json`, aucune sortie de course, aucun fichier
de la seconde passe hors les lignes dites.
