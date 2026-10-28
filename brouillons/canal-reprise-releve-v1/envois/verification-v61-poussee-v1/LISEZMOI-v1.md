# Organisme v6.1 poussé par Gemini : vérification en isolation (v1)

Écrit le 25 octobre 2026, entre 15 h 25 et 15 h 45 UTC, par un sous-agent de vérification neuf. Je n'ai lancé aucune
commande git, ouvert aucun accès réseau, lancé aucun sous-agent. Seuls deux programmes ont tourné, en isolation : les
45 essais de l'organisme (deux fois, chaque fois sur sa propre copie) et l'outil `invariance_v1.py` (six fois). Tout le
reste est de la lecture : `diff`, `sha256sum`, analyses de l'arbre syntaxique par des outils qui lisent les fichiers
sans les exécuter, et ma propre transcription du contrôle de propreté. Aucun code de Gemini n'a été importé hors de
l'isolation. Rien n'a été écrit hors de `/var/tmp/verification-v61-poussee-v1/`. Les empreintes de toutes les pièces
sont dans `EMPREINTES-v1.txt`.

## Verdict

- **Aucun défaut bloquant. V6-01 est corrigé.** Les trois successeurs mutés que produisent les essais lient `ast`,
  `math` et `threading` au niveau du module, et n'ont aucun nom non lié. Le nouvel essai importe le `principal` d'un
  successeur muté dans un processus neuf, puis y fait tourner une génération, dont le journal ne contient aucune
  erreur. Le reste est conforme :
  - 45 essais passés ;
  - des relevés identiques sous les graines de hachage 0, 1 et 2, avec 28 appels en B et 29 en D, comme la v6 ;
  - 0 appel imbriqué sous `_VERROU` ;
  - les gardes C-01 à C-13 présentes ;
  - le contrat du noyau tenu par le code de l'organisme.
- **Non bloquant, mais à savoir.**
  - La borne de 1 s mise sur la validation est une attente, pas un arrêt : un fil qui dépasse continue de tourner.
  - Le fichier assemblé est exécuté une seconde fois, sans borne de temps et avec toutes les fonctions intégrées.
  - Le filtre de propreté tolère encore un écart de 0,01 sur l'optimum, ainsi que des transformations affines. Par le
    chemin du code brut, l'une d'elles fait franchir le seuil de fin de conception (0,78), sans rien changer à la
    calibration.
  - Parmi les neuf réserves : 4 sont partiellement levées (1, 3, 4, 7) et 2 ne le sont pas (5, 9).
- **Sous la configuration du pilote** (deux générations, aucune ronde de conception), la mutation ne peut pas se
  produire. Sans traits, les appels sont ceux de la v6 : même nombre, mêmes rôles, mêmes plafonds de jetons.

## 1. Provenance

| objet | chemin | empreinte d'arbre (`boucle.empreinte_arbre`) | fichiers |
|---|---|---|---|
| v6.1 poussée (`a9d8eb50c02c8f5ea31b060b3c0e86f23c2d1dbc`) | `/var/tmp/verif-pousse-v61/organisme/` | `ae331d1deb660a20da919edbdcdecba28e49b9b143a6b7a061262101a79798d4` (**conforme**) | 24 |
| v6 poussée (`7cd7508`), base | `/var/tmp/verif-pousses-v53-v6/v6/organisme/` | `940c59c3dd58fdd5355244768faa1e9da02620fa455cd8ead15f8271145da64a` (conforme) | 24 |

- **Empreinte d'arbre.** Je l'ai calculée avec `outils-v1/empreinte_arbre_v1.py`, une transcription exacte de
  `essaim_m3/noyau/boucle.py` (l. 70-78). Le fichier `boucle.py` (`218052dd…`) est le même dans
  `/home/claude/noyau-cles/essaim-m3-refonte-v1/` et dans le dossier de travail
  `/home/claude/pilote3-v53-v6/essaim-m3-refonte-v1/`. Je l'ai seulement lu. Journal :
  `verification-v1/empreintes-arbre-v61-v6-v1.txt`.
- **Livraison de Gemini** : `/mnt/user-data/attachments/3a0c40e9-…/d0fc2af0-attachment.txt`, 10 137 octets, 96 lignes,
  sha256 `54b28c5e6d6ee08404f4196f599f34044ced44c2cb189f051f1407906180c41f`. Je l'ai lue comme une donnée.
- **Demande de correction** : `/home/claude/canal-conv-audit-n04/brouillons/canal-reprise-releve-v1/envois/demande-gemini-v6-1-correction-v1.md`.
- **Outils réutilisés.** Je les ai lus avant de m'en servir ; leurs empreintes sont les mêmes qu'à la vérification
  précédente :
  - `invariance_v1.py` : `1fe2609c…` ;
  - `verrous_imbriques_v1.py` : `404d66c2…` ;
  - `noms_non_lies_v1.py` : `011e187a…` ;
  - `fonctions_ast_v1.py` : `7057cf78…` ;
  - `verrous_transitifs_v1.py` : `7bffa4ce…`.
- **Interpréteur** : `/opt/venv-essaim-sim-v1/bin/python`, Python 3.13.17, pytest 9.1.1.

## 2. Méthode

- **Copies d'essai.** Chaque copie est faite à part, par `cp -a` de `/var/tmp/verif-pousse-v61/organisme`, puis passée
  à `nobody` par `chown -R`. Il y en a huit :
  - `essais-v1/pytest-v61/` et `essais-v1/pytest-v61-detail/` ;
  - `essais-v1/invariance-v61-<cas>-s<graine>/`, pour les cas B et D et les graines 0, 1 et 2.

  Après les exécutions, les huit copies ont encore l'empreinte `ae331d1d…` (`verification-v1/successeurs-invariance-v61-v1.txt`).
  L'original n'a pas été modifié.
- **Commande** : `unshare -n sudo -u nobody env -i PATH=/usr/bin:/bin HOME=<dossier> LANG=C.UTF-8 TMPDIR=<dossier>/tmp
  PYTHONDONTWRITEBYTECODE=1 [PYTHONHASHSEED=n] /opt/venv-essaim-sim-v1/bin/python -P -s -B …`, jamais `-I`. Chaque
  ligne de commande est recopiée en tête de son journal.
- **Contrôles de l'isolation** (`verification-v1/sonde-isolation-v61-v1.log`) :
  - **graine de hachage** : deux lancements donnent la même valeur de `hash("a")` pour chaque graine, et les mêmes
    valeurs qu'à la vérification précédente (`4644417185603328019`, `-3012895188637184397`, `6352457989142756797`) ;
  - **réseau** : une connexion tentée dans l'espace de noms est refusée (`OSError` 101) ;
  - **écritures** : aucun fichier de `nobody` plus récent que le début de cette vérification n'existe hors de mon
    dossier, sous `/tmp`, `/var/tmp`, `/home`, `/root`, `/mnt/user-data` et `/opt/venv…`. Les dossiers `runs/`,
    `donnees/` et `diag/` ont été écartés de la recherche sans y entrer.
- **Analyses statiques.** Elles ont été lancées par `python -I` : elles ne font que lire et analyser le texte.

## 3. Fichiers (résultat 1)

- **Inventaire** : 24 fichiers. Les 6 fichiers annoncés changent ; les 18 autres sont identiques octet pour octet
  (`verification-v1/inventaire-v6-vers-v61-v1.txt`). Empreintes fichier par fichier :
  `verification-v1/sha256-fichiers-v6-poussee-v1.txt` et `sha256-fichiers-v61-poussee-v1.txt`.
- **Différences unifiées** : `verification-v1/diff-v6-vers-v61-<fichier>-v1.txt`.

| fichier | lignes ajoutées | lignes retirées | octets |
|---|---|---|---|
| `CONCEPTION.md` | 16 | 6 | 18 881 → 20 781 |
| `manifeste.json` | 2 | 2 | 427 → 486 (`6.1.0`, nom `organisme-gemini-m3-v6` inchangé) |
| `memoire_isvd.py` | 16 | 7 | 11 121 → 11 699 |
| `politique_endogene.py` | 183 | 75 | 7 055 → 10 920 |
| `principal.py` | 88 | 44 | 89 541 → 92 111 |
| `tests/test_auto_architecte_v6.py` | 105 | 20 | 5 041 → 9 910 |

Comparaison par arbre syntaxique (`verification-v1/fonctions-ast-v6-v61-v1.txt`) :
- **`principal.py`** : 32 fonctions inchangées, 7 changées. Ce sont `_entrainer_et_predire_sondes_traits`,
  `_executer_moisson`, `_calculer_score_bregman_tsallis`, `_synthetiser_mutation_politique_endogene`,
  `_propager_successeur`, `_traiter_tache` et `executer`. Côté constantes, `CODE_OBJECTIF_SONDE_BREGMAN_TSALLIS` devient
  `CODE_OBJECTIF_SONDE_SECOURS`.
- **`memoire_isvd.py`** : seule `mettre_a_jour_memoire_isvd` change.
- **`politique_endogene.py`** : il est réécrit. La liste noire `NOEUDS_INTERDITS` devient la liste blanche
  `NOEUDS_AUTORISES_BLANCS`.

## 4. Essais en isolation (résultat 2)

| exécution | résultat | temps | journal |
|---|---|---|---|
| `-q -p no:cacheprovider` | `45 passed in 4.88s`, code de sortie 0 | 5,18 s au mur | `verification-v1/pytest-v61-poussee-v1.log` |
| `-v --durations=0` (copie à part) | `45 passed in 5.07s`, code de sortie 0 | 5,31 s au mur | `verification-v1/pytest-v61-poussee-detail-v1.log` |

- **Répartition** : 34 essais hérités de la v5.2.1, 5 de la v5.3, 6 dans `test_auto_architecte_v6.py` (4 de la v6 et 2
  nouveaux). Les essais `test_c01` à `test_c13` passent tous.
- **Durées** : les plus lents sont `test_c06` (1,88 s) et `test_c05` (1,58 s) ; le nouvel essai en processus neuf prend
  0,13 s.
- **Gemini annonce 7,24 s** : c'est sa machine, l'écart est sans portée.

**Ce que fait réellement `test_v6_1_successeur_mute_s_importe_et_tourne_dans_processus_neuf`** (l. 112-167) :
1. Sous un faux noyau, il fait tourner une génération 1 dans le processus de pytest. L'historique y contient deux scores
   égaux (0,75), il y a donc stagnation, et l'architecte répond par un objet JSON (`alpha` 1,45, `poids_brier` 0,82).
   La mutation est acceptée.
2. Il lance un **processus neuf** (`sys.executable -B -c …`). Ce processus place le dossier du successeur en tête de
   `sys.path`, installe un faux `noyau_client` (`especes`, `budget`, `appeler`), importe `politique_endogene` puis
   `principal`, et vérifie `NOM_POLITIQUE == 'bregman_mutee_gen2'`. C'est bien le module muté qui est chargé.
3. Il appelle `principal.executer` pour une génération 2 (une tâche de test, aucune tâche d'entraînement). Il vérifie
   `n_taches_test_repondues == 1` et le code de sortie 0.

C'est conforme au critère d'acceptation : on importe le `principal` d'un successeur muté dans un processus neuf, en
plus de lire son texte. Trois limites :
- **Fonctions muettes.** Sans tâche d'entraînement, le processus neuf n'appelle jamais `recompense_interne` du
  successeur. Sans trait, il n'appelle pas non plus `code_objectif_sonde`.
- **Erreurs non contrôlées par l'essai.** L'essai ne regarde pas `bilan["erreurs"]`. J'ai donc lu le journal écrit par
  ce processus (`…/test_v6_1_successeur_mute_s_im0/travail_g2/journal_generation.json`) : 0 erreur, 2 appels, aucune
  mutation.
- **Un essai de la v6 affaibli.** Dans `test_v6_verificateur_proprete…`, l'assertion `"croissante" in msg_const`
  est retirée (différence l. 21-24), ce que Gemini ne dit pas. La portée est nulle, puisque le message rendu contient
  toujours « croissante ».

## 5. V6-01 : le successeur muté s'importe-t-il ? (résultat 3)

`noms_non_lies_v1.py` a été lancé sur l'original, sur les trois successeurs mutés produits par les essais, et sur le
`principal.py` d'un successeur. Journal : `verification-v1/noms-non-lies-successeurs-v61-v1.txt`. Les fichiers sont
sous `essais-v1/pytest-v61/tmp/pytest-of-nobody/pytest-0/`.

| fichier | sha256 | imports de niveau module | noms non liés |
|---|---|---|---|
| original `politique_endogene.py` | `da41dd9c…` | `math` (l. 1), `ast` (l. 56), `math` (l. 57), `threading` (l. 58) | aucun |
| `test_v6_auto_reecriture_effect0/travail_v6_mut/successeur/…` | `60a59bda…` | `math` (l. 1), `ast` (l. 52), `math` (l. 53), `threading` (l. 54) | aucun |
| `test_v6_1_successeur_mute_s_im0/travail_g1/successeur/…` | `6227829a…` | idem | aucun |
| `test_v6_1_successeur_mute_s_im0/travail_g2/successeur/…`, copie de la génération 2 | `6227829a…` | idem | aucun |
| `test_v5_3_phase_conception_ecr0/conception_c000/successeur/…` | `e12d277d…` | idem | aucun |
| `principal.py`, original et successeur | `5196029a…` | 9 imports, dont `politique_endogene` (l. 22) | aucun |

- **Le nom `ast` est lié, et tous les autres noms de niveau module aussi.** Dans les trois successeurs, la partie qui
  suit le marqueur est identique à celle de l'original. Différences entre l'original et chaque successeur muté :
  `verification-v1/diff-politique-originale-vers-successeur-essai-*-v61-v1.txt`. La mutation y change 8 lignes et en
  retire 12 : les constantes, l'objectif de sonde, les mots-clés de `ponderer_trace_memoire`, et `marge_sonde_decisive`,
  qui passe de 0,32 à 0,30.
- **La seconde ligne de défense** est dans `_propager_successeur` (l. 1492-1500). Avant d'écrire le fichier assemblé,
  l'organisme le compile, l'exécute, puis vérifie qu'il définit `verifier_et_valider_code_politique` et
  `recompense_interne`. En cas d'échec, l'erreur est consignée et l'original déjà copié reste en place. Un nom non lié
  comme celui de V6-01 y lèverait `NameError` et serait rattrapé.
- **Déterminisme.** Les deux exécutions de pytest, faites sans graine de hachage fixée, ont produit les mêmes trois
  fichiers mutés.

## 6. Reproductibilité (résultat 4)

`invariance_v1.py`, cas B et D, `PYTHONHASHSEED` = 0, 1 et 2. Journal : `verification-v1/invariance-v61-poussee-v1.log`.
Relevés : `verification-v1/releve-invariance-v61-<cas>-s<n>-v1.json`.

| cas | appels `appeler` | `budget()` / `especes()` | recherches / téléchargements | sha256 des 3 relevés | v6 (même outil) |
|---|---|---|---|---|---|
| B | 28 | 46 / 1 | 0 / 0 | `d10986838272ec3a…`, identique pour les trois | 28 appels, `84f355fc…` |
| D | 29 | 53 / 1 | 2 / 1 | `30381a7536756c4d…`, identique pour les trois | 29 appels, `d26a36c8…` |

**Ce qui change de la v6 à la v6.1** (`verification-v1/comparaison-invariance-v6-vers-v61-v1.txt`,
`differences-fichiers-v6-vers-v61-invariance-v1.txt`) :
- **Appels** : même nombre, même suite de rôles, d'espèces et de plafonds de jetons.
- **Consignes**
  - B : les 28 sont identiques.
  - D : une seule diffère, l'appel n° 24 (`moissonneur_formulation_requetes`). D'après le code, la v6 demandait
    « entre 4 et n » requêtes, avec n = max(4, min(10, recherches)), soit « entre 4 et 4 » ici. La v6.1 demande
    « entre 4 et 6 » (l. 736). Les requêtes du faux noyau étant fixes, les recherches et le téléchargement restent
    identiques.
- **Réponses** : `reponses_test.json` et `reponse-question.md` sont identiques.
- **Métrique proposée** : `valeur` passe de **0,195747 à 0,241719**, en B comme en D. La cause est la nouvelle
  `recompense_interne`.
- **Mémoire** (`memoire_isvd.json`) : 237 feuilles sur 300 diffèrent en B, et 236 sur 310 en D (Sigma, U et poids des
  exemplaires). Le `journal_ablations` est identique.
- **Journal de génération** : seule la version change.
- **Successeurs** : B `ea90ef35…`, D `dca3f858…`, identiques d'une graine à l'autre. `politique_endogene.py` y est
  recopié tel quel (`da41dd9c…`). Il n'y a pas de mutation, car l'historique n'a qu'une entrée et la phase n'est pas
  « conception ».

## 7. Verrous (résultat 5)

Journal : `verification-v1/verrous-v61-v1.txt`.
- **Appels imbriqués** : 0 dans `principal.py`, avec l'outil des appels directs comme avec celui des chaînes d'appels
  internes. Il n'y a aucun `acquire` ni `release` explicite.
- **Fonctions qui prennent `_VERROU`** : les six mêmes qu'en v6. Par chaîne d'appels, `_calculer_score_bregman_tsallis`
  et `_propager_successeur` s'y ajoutent, parce qu'elles consignent désormais leurs erreurs par `_consigner_erreur`.
  Aucune n'est appelée en tenant déjà le verrou.
- **Autres fichiers** : `memoire_isvd.py`, `politique_endogene.py` et `mitose_spectrale.py` ne prennent jamais
  `_VERROU`. Le fil de validation (§ 8) ne peut pas le prendre : il vit dans `principal`, que `politique_endogene`
  n'importe pas.

## 8. Gardes et contrat ; le fil d'exécution (résultat 6)

### 8.1. Gardes C-01 à C-13

Toutes sont présentes. Les fonctions qui les portent sont inchangées par l'arbre syntaxique, sauf C-03, portée par
`_traiter_tache`, et C-05, portée par `executer` :

| garde | constat, lignes de la v6.1 |
|---|---|
| C-01 | Aucun `.py` ni `.json` n'a de marque d'ordre d'octets ni de caractère de contrôle autre que LF (`verification-v1/c01-octets-v6-v61-v1.txt`). `CONCEPTION.md` garde 2 retours chariot (l. 104-105). |
| C-02, C-09 | `_parser_decision_tache` (l. 630) et `_extraire_json_candidat` (l. 595), inchangées. |
| C-03 | Les étiquettes sont lues dans chaque tâche (l. 1547), et la sonde prend `etiquettes[0]` et `etiquettes[1]` (l. 1581). |
| C-04 | `_selection_stratifiee` (l. 1035), inchangée. |
| C-05 | Le `try` d'`executer` couvre les l. 1753-1924, suivies d'`except Exception` (l. 1925) et du `finally` (l. 1927), qui écrit réponses, mémoire, métrique, journal et successeur. La mutation est appelée dans ce `try` (l. 1914) : une exception du vérificateur est rattrapée. Une attente ou un calcul qui ne finit pas ne l'est pas (§ 8.3). |
| C-06 | `_faut_basculer` (l. 1512), inchangée. |
| C-07 | `charger_connaissances_archive` (`memoire_isvd.py` l. 262), inchangée. Les nouveaux replis sont consignés (§ 9). |
| C-08 | `_confiance_finie` (l. 622), désormais appliquée aussi à l'exactitude et à la perte d'entraînement (l. 556-563). |
| C-10, C-11 | Le dossier `metrique/` est identique à la v6. |
| C-12 | 0 appel imbriqué (§ 7). |
| C-13 | `OUVERTURE_MOISSON` et `FERMETURE_MOISSON` (l. 25-26), `_sanitiser_donnee_externe` (l. 248, avec `replace("===", "= =")` l. 252) et `_bloc_moisson_borne` (l. 1054) sont inchangées. |

### 8.2. Contrat du noyau

Motifs recherchés dans les 24 fichiers (`verification-v1/motifs-v61-v1.txt`) : `subprocess`, `socket`, `os.system`,
`os.popen`, `urllib`, `requests`, `http`, `os.environ`, `getenv`, `environ`, `__import__`, `eval(`, `exec(`,
`compile(`, `open(`, `importlib`, `ctypes`, `multiprocessing`, `signal`, chemins absolus, `expanduser`.

Dans le code de l'organisme (hors `tests/`) :
- **Interdits** : ni `subprocess`, ni `socket`, ni `os.system`, ni `urllib`, ni `requests`, ni accès aux variables
  d'environnement. `http` n'apparaît que dans le contrôle d'hôte des téléchargements (l. 241).
- **Lectures de fichiers** : celles d'avant, à savoir l'archive (l. 297), le texte d'un téléchargement servi par le
  noyau (l. 414), la mémoire locale (l. 1725) et le propre `politique_endogene.py` de l'organisme (l. 1485, déjà en v6).
  Aucune lecture nouvelle hors du dossier de travail.
- **Écritures** : toutes sous `dossier_travail`, successeur compris (l. 1475-1508).
- **Exécution de code** : `exec` et `compile` paraissent deux fois, toutes deux nouvelles ou réécrites :
  - `politique_endogene.py` l. 235-236 : le candidat, dans le fil de validation ;
  - `principal.py` l. 1493-1495 : le fichier assemblé, dans le fil principal.

Dans les essais, `subprocess` ne sert qu'au nouvel essai (l. 4 et 160), ce qui est permis aux essais. Le contrat est
donc tenu, sous les réserves du § 8.3.

### 8.3. Le fil d'exécution (`threading`)

- **Où.** `politique_endogene.py` importe `threading` au niveau du module (l. 58, dans le bloc vérificateur). Le fil
  est créé dans `verifier_et_valider_code_politique` (l. 262-266). Ce n'est fait que lorsqu'une mutation est tentée
  (`principal.py` l. 1027), c'est-à-dire en conception, sous `autoriser_mutation_code`, ou en stagnation à partir de la
  génération 1.
- **Ce qu'il fait** (`_cible_validation`, l. 233-260). Il compile et exécute le candidat dans un espace réduit :
  14 fonctions intégrées, et un `__import__` qui ne rend qu'un objet `math` en lecture. Il vérifie ensuite les quatre
  fonctions, puis lance le contrôle de propreté, soit 404 évaluations de `recompense_interne`. Enfin, il appelle les
  trois autres fonctions.
- **Comment il est attendu.** Le fil est démon, et attendu par `join(1.0)`. S'il est encore vivant après 1 s, la
  validation rend « délai dépassé ».
- **Peut-il survivre ?** Un fil Python ne peut pas être arrêté. Au-delà du délai, il continue de tourner en
  arrière-plan, pendant la suite de la génération (`finally`, écritures, successeur), jusqu'à sa propre fin. Étant
  démon, il ne retient pas le processus : il ne survit pas à la fin de la génération, c'est-à-dire du processus lancé
  par le noyau.
- **Garde de temps.** Dans le cas ordinaire, l'attente est bien bornée à environ 1 s, puisque l'interpréteur alterne
  entre les fils. Ce n'est pas garanti pour une seule opération longue exécutée en code natif : elle garde le verrou
  global de l'interpréteur, et peut retarder le fil principal jusqu'à ce qu'elle finisse, donc retarder aussi
  `_temps_ok` et l'écriture du `finally`. Je ne l'ai pas éprouvé, et n'ai rien exécuté en ce sens.
- **Contrat.** Il n'est pas touché : `threading` appartient à la bibliothèque standard, et `principal.py` l'emploie
  déjà (l. 5 et 98, `_VERROU`). Il n'y a ni réseau, ni sous-processus, ni clé.

## 9. Les points 1 à 7 de la demande et les neuf réserves (résultat 7)

### 9.1. Les sept points du § 3 de la demande

| point | réponse de Gemini | constat |
|---|---|---|
| 1. La récompense change sans être annoncée | changé et annoncé | **Levé pour l'annonce** : `CONCEPTION.md` § 2.12, l. 143. La récompense change encore : 0,8 Brier + 0,2 divergence de Bregman-Tsallis normalisée (l. 10-20). La métrique passe de 0,195747 à 0,241719 sous le faux noyau. D'après ma transcription, la règle est propre (optimum à p, au pas de 1e-4 près). Le repli est consigné (l. 906-910) et repose sur Brier, qui est propre. |
| 2. Exécution sans borne | liste blanche et fil limité à 1 s | **Partiellement levé.** Il n'y a plus ni boucle ni récursion (§ 9.4). Mais 1 s est une borne d'attente, pas un arrêt (§ 8.3), et la seconde exécution, dans `_propager_successeur` (l. 1492-1497), n'a aucune borne. |
| 3. Deux replis silencieux | tous consignés | **Levé pour les deux replis cités** (l. 906-907 et l. 972-973). Les nouveaux replis sont aussi consignés : l. 495-501, 556-563, 1554-1555 ; `memoire_isvd.py` l. 109-111 et 185-189. Deux choses restent : un objet JSON sans les clés attendues donne toujours une mutation, avec les valeurs par défaut (l. 972-974 ; c'est consigné, pas refusé) ; et une valeur nulle de `seuils_routage()` reprend son défaut en silence (`or 0.78`, l. 1558-1562). |
| 4. Trois fonctions jamais appelées | branchées | **Levé.** `code_objectif_sonde` est appelée l. 495-501, mais seulement si des traits sont servis et que `entrainer` et `predire` existent (l. 466-470, 1787). `seuils_routage` est appelée l. 1553. `ponderer_trace_memoire` passe par `fn_ponderation` (l. 1961 ; `memoire_isvd.py` l. 183-185). `EXPOSANT_ALPHA` entre dans le calcul (l. 14 ; gabarit l. 989). Les plages de la consigne (l. 943-944) sont désormais celles du code (l. 969-971). |
| 5. La propreté n'est contrôlée qu'en 7 points | grille fine et ancrages | **Partiellement levé** (§ 9.3). |
| 6. Liste noire ; fichier final jamais validé | liste blanche ; fichier assemblé validé | **Partiellement levé.** La liste blanche est réelle (l. 60-110, 182-213). Le fichier assemblé est compilé et exécuté avant d'être écrit (l. 1492-1500). Il n'est pas passé au filtre, ce qui est normal, puisque le vérificateur importe `ast` et `threading`. Ce qui est garanti et ce qui ne l'est pas : § 9.4. |
| 7. Les neuf réserves | « toutes levées » | **Non** : voir le § 9.2. |

### 9.2. Les neuf réserves (§ 8 de la vérification précédente)

| n° | réserve | v6.1 |
|---|---|---|
| 1 | « Sans traits, flux identique à la v5.2.1 » est faux | **Partiellement levée.** La consigne de moisson redevient « entre 4 et 6 » (l. 736). Sans traits, les sondes ne sont plus appelées (l. 1787), et le `budget()` des sondes ne venait déjà qu'avec des traits (l. 466-472). Mais la récompense (l. 905) et la mémoire (`memoire_isvd.py` l. 142, 181-191) diffèrent toujours de la v5.2.1, donc la mémoire et la métrique aussi. Je n'ai pas comparé à la v5.2.1 en exécutant. |
| 2 | Perte de sonde non propre | **Levée.** `code_objectif_sonde()` rend 0,80 Brier + 0,20 log borné (l. 23-29), employé l. 519 ; le secours est la même formule (l. 45-50). |
| 3 | Vote de la sonde dès une exactitude de 0,60, quelle que soit la marge | **Partiellement levée.** Une marge minimale de 0,10 est exigée (l. 1582). Le seuil d'exactitude reste 0,60 (l. 1579). |
| 4 | « La sonde incertaine force l'arbitrage » : sans effet | **Partiellement levée.** Le déclencheur reste redondant dès deux castes (`len(castes) > 1`, l. 1624). L'effet nouveau : une sonde incertaine ou en désaccord interdit l'arrêt anticipé, qui exige en outre deux votes valides de modèles (l. 1629, 1654, 1657). |
| 5 | La garde d'exactitude porte sur l'exactitude d'entraînement | **Non levée.** Le code lit toujours `exactitude_entrainement` (l. 556-563, 1570-1579). La « documentation dans `CONCEPTION.md` » annoncée par Gemini est introuvable : j'ai lu le § 2.12 en entier et cherché par mots dans le fichier. |
| 6 | Il faut Δ > 0,005 pour « CONFIRME » | **Levée** : `delta_score > 0.0` (`memoire_isvd.py` l. 142). |
| 7 | Multi-familles détecté par mots-clés, bonus appliqué deux fois | **Partiellement levée.** Le bonus n'est plus appliqué qu'une fois : sur le poids (`memoire_isvd.py` l. 181-191), et plus sur l'énergie (l. 219-222). La détection reste faite par mots-clés, avec désormais trois jeux : `_detecter_confirmation_multi_familles` (l. 81, en repli), `ponderer_trace_memoire` initiale (`politique_endogene.py` l. 36-38) et celle du gabarit, plus étroite (`principal.py` l. 1010), qu'installe toute mutation. |
| 8 | Rondes de conception comptées à partir de 0 | **Levée.** Les l. 1986-1989 donnent `or 1`, la convergence à partir de la ronde 2, et la dernière ronde quand `r_idx >= R`, ce qui suit la numérotation de 1 à R du noyau. |
| 9 | Paramètre `erreurs` annoncé, absent du code | **Non levée.** La signature de `_entrainer_et_predire_sondes_traits` est inchangée (l. 460-465) ; les erreurs passent par `_consigner_erreur`. Sous ce numéro, Gemini répond à une autre réserve, celle des caractères de contrôle. |

**Caractères de contrôle de `CONCEPTION.md`** (réserve 4 du § 12 de la reconstitution) : **partiellement levée.** Sur
11 caractères de contrôle, 9 sont remplacés par des espaces, et 2 retours chariot restent (l. 104-105). Les mots
restent amputés de leur première lettre : « rxiv », « udget », « ichier », « ravail », « aches_entrainement »,
« ronque », « egles_induites ».

### 9.3. Le filtre de « propreté stricte » sur grille fine (`politique_endogene.py` l. 129-168)

**Méthode.** Je l'ai essayé par **ma transcription** (`outils-v1/proprete_regles_v2.py`), faite d'après la lecture des
lignes 129 à 168. Le code de Gemini n'est ni importé ni exécuté. Résultats : `verification-v1/proprete-regles-v61-v1.txt`.

**Ce que fait le contrôle** :
- 199 points, q de 0,005 à 0,995 ;
- valeurs comprises entre −1 et 1,05 ;
- monotonie stricte, d'au moins 1e-7 par pas ;
- |q*(p) − p| ≤ 0,0101 pour p = 0,05, 0,10, …, 0,95 ;
- trois ancrages : R(1 ; 0,999) et R(0 ; 0,001) dans [0,98 ; 1,005], R(y ; 0,5) dans [0,68 ; 0,82], R(1 ; 0,01) et
  R(0 ; 0,99) dans [−0,50 ; 0,15].

Je compare son verdict à l'optimum vrai, calculé au pas de 1e-4 pour p = 0,01 à 0,99. « Score de l'exemple » désigne
la moyenne obtenue pour deux vérifications : une juste à 0,85, une fausse à 0,70.

| règle | verdict (transcrit) | écart maximal de l'optimum | score de l'exemple |
|---|---|---|---|
| Brier, 1 − (y − q)² | accepte | 0 | 0,7438 |
| v6.1 initiale (α = 4/3, Brier 0,80) | accepte | 0 | 0,7449 |
| gabarit v6.1 aux coins (α 1,15 ou 1,85 ; Brier 0,60 ou 0,95) | accepte (les 4) | 0 | 0,7438 à 0,7469 |
| v6 initiale, 1 − (0,8 Brier + 0,2 log) | rejette (ancrage médian, 0,661) | 0 | 0,6584 |
| logarithmique bornée | rejette (bornes) | 0 | — |
| constante 0,99 ; linéaire | rejette | — | — |
| v5.3 interne ; sonde v5.3 prise comme récompense | rejette | 0,12 ; 0,10 | — |
| sur-confiante 1 − Brier + 0,10 (q − ½)² | **rejette** (comme Gemini l'annonce) | 0,05 | — |
| sur-confiante 1 − Brier + 0,30 (q − ½)² | rejette | 0,15 | — |
| Brier + 0,5 ; Brier × 5 ; Brier × 1e-5 | **rejette** (comme annoncé) | 0 | — |
| **sur-confiante très légère, 1 − Brier + 0,02 (q − ½)²** | **accepte** | **0,0099** (q* = 0,9796 pour p = 0,97) | 0,7454 |
| sous-confiante légère, 1 − Brier − 0,02 (q − ½)² | rejette (monotonie) | 0,0096 | — |
| **0,87 Brier + 0,13** (niveau relevé) | **accepte** | 0 | **0,7771** |
| **1,2 Brier − 0,2** (niveau abaissé) | **accepte** | 0 | 0,6925 |

**Balayage des transformations affines a·R + b** (a de 0,5 à 2 au pas de 0,02 ; b de −0,6 à 0,6 au pas de 0,01) :
- sur Brier, 39 sont acceptées, et le score de l'exemple va de **0,677 à 0,775** ;
- sur la règle initiale de la v6.1, 44 sont acceptées, et il va de **0,679 à 0,791** (avec a = 0,82, b = 0,18).

**Ce qui est garanti** (selon ma transcription) :
- sur la grille vérifiée, l'optimum est à moins de 0,01 de p ;
- le niveau et l'échelle sont tenus dans une bande ;
- les cas cités par la demande sont rejetés : sur-confiance de 0,10, Brier + 0,5, Brier × 5.

**Ce qui ne l'est pas** :
- une sur-confiance jusqu'à environ 0,01, par construction de la tolérance ;
- rien n'est contrôlé pour p > 0,95 ni entre les points de la grille ;
- une transformation affine acceptée déplace le score de l'exemple d'environ −0,07 à +0,05. Sur la règle initiale, elle
  **franchit le seuil de fin de conception de 0,78** (0,745 devient 0,791) sans aucun changement de calibration.

Ce dernier cas n'est possible que par le chemin du **code brut** (l. 961-963). Par le **gabarit**, la forme de la règle
est fixe, et le score de l'exemple ne varie que de 0,7438 à 0,7469 sur les plages permises. La v6 laissait, elle,
varier ce score de 0,552 à 0,722.

### 9.4. La liste blanche syntaxique (`politique_endogene.py` l. 171-213) : garanti et non garanti

Je n'ai pas cherché de contournement, et rien n'a été exécuté en ce sens.

**Garanti, à la lecture du filtre** :
- aucun nœud hors de la liste blanche, donc ni boucle, ni compréhension, ni `lambda`, ni classe, ni `try`, `with`,
  `raise`, `global`, `yield`, ni chaîne formatée, tranche ou argument nommé ;
- un seul import possible : `import math`, sans alias ;
- les appels se limitent aux 14 fonctions intégrées de la liste, aux 21 attributs permis de `math` et aux méthodes
  `lower` et `strip`. Tout appel à une fonction définie dans le candidat, ou par un autre nom, est refusé, ce qui exclut
  la récursion ;
- ni écriture d'attribut, ni attribut ou nom commençant par `__`, ni aucun des 24 noms interdits.

Conséquence : le nombre d'opérations du candidat est borné par la longueur de son texte (25 000 caractères au plus).
Je ne vois aucun moyen direct de lire ou d'écrire un fichier, d'ouvrir le réseau, de lancer un processus ou de
prendre un verrou.

**Non garanti** :
- **Le temps et la mémoire.** Le nombre d'opérations est borné, pas le coût de chacune : l'arithmétique sur entiers se
  fait en précision arbitraire, et la répétition d'une séquence peut être longue. Le délai de 1 s ne stoppe pas le
  fil (§ 8.3). Une boucle sans fin n'est plus possible, mais un calcul très long ou très gourmand en mémoire n'est pas
  exclu par construction.
- **La seconde exécution, dans `_propager_successeur`** (l. 1494-1495). Elle se fait dans `ns_entier = {}`, et Python
  y place alors toutes les fonctions intégrées. Elle a lieu dans le fil principal, pendant le `finally` d'`executer`,
  sans borne. Le candidat y est le code même qui a passé le filtre ; le reste est le vérificateur, qui est fixe.
- **Dans le successeur**, le module s'importe avec toutes les fonctions intégrées. Seules les contraintes de l'arbre
  syntaxique continuent de s'y appliquer.
- **Les types des seuils.** La validation contrôle que `seuils_routage()` rend un dictionnaire muni de la clé
  `seuil_confiance_caste1`, pas que ses valeurs soient des nombres. Une valeur non numérique ferait lever `float()`
  dans `_traiter_tache` (l. 1558-1562), hors du `try` des l. 1552-1556. Ce cas ne peut venir que du code brut.
- **Le repérage du vérificateur.** Il se fait par la première occurrence d'une ligne de commentaire (l. 1486-1488),
  que le filtre ne voit pas, puisque les commentaires ne figurent pas dans l'arbre syntaxique. C'est sans effet pour
  le gabarit.
- **Les erreurs d'analyse.** Autour de `ast.parse` (l. 175-178), seule `SyntaxError` est rattrapée. Une autre
  exception remonterait jusqu'à l'`except` d'`executer` (l. 1925). Elle serait alors consignée, et le `finally`
  s'exécuterait.

La seule barrière sûre reste le bac à sable du noyau : utilisateur dédié, réseau coupé, délai.

## 10. Sous la configuration du pilote : deux générations, aucune ronde de conception (résultat 8)

### 10.1. La mutation peut-elle se produire ?

**Non**, d'après la lecture ; ce n'est pas exécuté. `_synthetiser_mutation_politique_endogene` ne tente la mutation
qu'à trois conditions (l. 921-933). Aucune n'est remplie :
- **la phase « conception »** : il n'y a aucune ronde de conception ;
- **`autoriser_mutation_code`** : le noyau ne pose jamais cette clé (recherche dans `essaim_m3/` : absente) ;
- **deux scores à l'historique, à partir de la génération 1** :
  - en génération 0, la condition `generation >= 1` est fausse ;
  - en génération 1, l'historique est `archive.historique(lignee)` (`boucle.py` l. 630 ; `archive.py` l. 229-234) et
    ne contient que la ligne de la génération 0, relance comprise : une relance rejoue la génération 1 avec le même
    historique (`boucle.py` l. 802-807) ;
  - le bras gelé reçoit un historique vide (l. 630).

La fonction rend donc à la l. 933 sans aucun appel, et le candidat n'est jamais exécuté : il n'y a ni fil ni seconde
exécution.

### 10.2. Le nombre d'appels et le coût changent-ils par rapport à la v6 ?

- **Sans traits.** Rien ne change, ni le nombre d'appels, ni leurs rôles, ni leurs plafonds de jetons (§ 6 : 28 et 29
  appels, suites identiques). La raison : la sonde est absente (`etiq_sonde` est `None`), donc l'arrêt anticipé de la
  v6.1 (`votes_llm_valides >= 2`) équivaut à celui de la v6 (deux votes enregistrés), et les seuils lus dans
  `seuils_routage()` initial sont les valeurs que la v6 écrivait en dur (0,78 ; 0,32 ; 0,18 ; 0,35).
- **Avec des traits servis** (lecture, non exécuté). La v6.1 fait au moins autant d'appels par tâche que la v6, et plus
  dans trois cas :
  - quand la sonde est incertaine (marge sous 0,18) ou en désaccord avec la première caste : il n'y a plus d'arrêt
    anticipé, et toutes les castes supplémentaires sont appelées tant que `_peut_appeler` le permet ;
  - quand la première caste ne rend pas de vote valide, parce que le vote de la sonde ne compte plus parmi les deux
    votes exigés ;
  - quand la marge de la sonde est inférieure à 0,10, parce que la sonde ne vote plus.

  L'objectif de sonde envoyé à `entrainer` change aussi (§ 9.2, réserve 2). Le coût supplémentaire reste borné par
  `appels_max` et par la garde de temps.
- **La récompense** ne change pas le nombre d'appels d'une génération, puisqu'elle est calculée après les tâches. Elle
  change la mémoire et la métrique (§ 6). La mémoire entre dans les consignes de la génération 1, qui différeront de
  celles de la v6 ; avec un vrai modèle, les réponses, donc le routage, pourront différer aussi.
- **La moisson.** La consigne demande désormais 4 à 6 requêtes, contre 4 à n en v6, où n peut aller jusqu'à 10. Si le
  budget de recherches dépasse 6, la v6.1 peut donc en formuler, et peut-être en exécuter, moins que la v6. Sinon,
  rien ne change.

## 11. Écarts au rapport de Gemini

- **« Thread démon borné à 1.0 s », « terminaison en O(1) opérations »** : c'est une borne d'attente, pas un arrêt, et
  le nombre d'opérations est borné, pas leur coût (§ 8.3, § 9.4).
- **« Toutes [les réserves] levées »** : non. 4 sont levées (2, 6, 8, et l'annonce du point 1), 4 partiellement
  (1, 3, 4, 7) et 2 ne le sont pas (5, 9). La réserve 5 « documentée » est introuvable ; la réserve 9 est confondue
  avec une autre.
- **« CONCEPTION.md nettoyé de ses caractères de contrôle »** : seulement en partie (§ 9.2).
- **Un essai de la v6 affaibli**, sans que ce soit dit (§ 4).
- **La définition de la métrique** dit toujours « alpha=4/3 », même après une mutation à 1,45. C'est sans effet sur le
  calcul.

## 12. Réserves de cette vérification

1. **Garanties du filtre.** Elles sont établies par lecture et par l'analyse de l'arbre syntaxique ; aucun
   contournement n'a été cherché ni exécuté. Le comportement des fils et du verrou global de l'interpréteur relève des
   règles de CPython, et n'a pas été éprouvé ici.
2. **Propreté.** Les verdicts « accepte » et « rejette » du § 9.3 viennent de ma transcription, pas du code de Gemini.
3. **Couverture.** L'outil d'invariance ne déclenche ni les sondes (aucun trait) ni la mutation. Le chemin de la
   mutation n'est éprouvé que par les essais de Gemini, sous faux noyau, et par ma lecture des journaux qu'ils
   écrivent.
4. **Configuration du pilote.** Les conclusions du § 10 viennent de la lecture du noyau (`boucle.py` l. 614-630 et
   802-807, `archive.py` l. 229-234), sans exécution.
5. **Durée.** Le travail a été fait en une demi-heure environ. Je n'ai pas comparé à la v5.2.1 en exécutant (réserve 1).

C'est à toi de décider de la suite. Je n'ai rien préparé à ce sujet : ni préenregistrement, ni message à Gemini.

## 13. Contenu de ce dossier

- `LISEZMOI-v1.md` : ce rapport. `EMPREINTES-v1.txt` : sha256 de toutes les pièces et des outils réutilisés. Contrôle :
  `sha256sum -c EMPREINTES-v1.txt` depuis ce dossier.
- `verification-v1/` : inventaire, empreintes par fichier, différences, journaux de pytest, d'invariance, de verrous et
  d'isolation, relevés, comparaisons et analyses.
- `outils-v1/` : mes quatre outils, qui ne font que lire (`empreinte_arbre_v1.py`, `comparer_releves_v1.py`,
  `diff_json_v1.py`, `proprete_regles_v2.py`). Ils se lancent avec `python -I`.
- `essais-v1/` : les copies d'essai, propriété de `nobody`, avec leurs sorties. Elles sont hors des empreintes, sauf
  les relevés recopiés dans `verification-v1/`.
- `livrable-verification-v61-poussee-v1.zip` : tout ce qui précède, sauf `essais-v1/`.
