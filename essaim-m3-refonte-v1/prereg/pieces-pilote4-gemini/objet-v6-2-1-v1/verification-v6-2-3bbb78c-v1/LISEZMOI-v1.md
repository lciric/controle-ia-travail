# Organisme v6.2 poussé par Gemini : vérification en isolation (v1)

- **Début** : 2026-10-25 22:58:00 UTC (lu sur `date -u` au lancement).
- **Écriture de ce rapport** : 2026-10-25 23:21:12 UTC (lue sur `date -u` au moment de l'écrire).

Sous-agent de vérification neuf. Commandes git : trois extractions `git -C /home/claude/canal-conv-audit-n04 archive <commit>
organisme | tar -x -C <dossier neuf>` (passées par `tee` pour garder l'archive), pour `fedb065`, `a9d8eb5` (la v6.1) et,
sur l'instruction reçue en cours de travail, `3bbb78c` ; aucune autre. Aucun accès réseau, aucun sous-agent, aucune clé
rencontrée. Rien n'a été écrit hors de `/var/tmp/verification-v62-poussee-v1/`. Les programmes de Gemini n'ont tourné
qu'en isolation : essais (pytest) et `invariance_v1.py`. Tout le reste est lecture, `diff`, `sha256sum`, analyses de
l'arbre syntaxique et mes transcriptions. Empreintes de toutes les pièces : `EMPREINTES-v1.txt`.

**Objet.** Le brief désignait `fedb065`. À 23:09 UTC, le coordinateur a fait savoir que la v6.2 livrée est `3bbb78c`, fils
unique de `fedb065`, avec un rapport de livraison. **Le verdict, les treize points et les points 4 à 6 portent sur
`3bbb78c`.** Ce que j'avais établi sur `fedb065` est gardé comme état intermédiaire (§ 1.3).

## Verdict

- **`3bbb78c` : aucun défaut bloquant.**
  - **Essais** : 53 sur 53 passent en isolation, deux fois (4,87 s et 4,83 s).
  - **V6-01 reste corrigé** : le successeur muté s'importe et fait tourner une génération dans un processus neuf, sans
    erreur ; aucun nom non lié.
  - **Le reste est conforme** :
    - relevés identiques sous les graines de hachage 0, 1 et 2 ;
    - 28 appels en B et 29 en D, même suite que la v6.1 et que la v5.2.1 ;
    - 0 appel imbriqué sous `_VERROU` ;
    - les gardes C-01 à C-13 présentes ;
    - le contrat du noyau tenu.
- **« Levée intégrale des 13 points » n'est pas exact.** 7 points sont levés (1, 2, 6, 8, 11, 12, 13) et 6 le sont en
  partie (3, 4, 5, 7, 9, 10). Aucun n'est resté tel quel.
  - Le coût d'une opération n'est toujours pas borné. Quatre candidats très coûteux passent le filtre statique (ma
    transcription). Or la validation tourne désormais dans le fil principal, sans aucune borne de temps.
  - Le contrôle de propreté accepte encore une règle impropre qui cache un bonus entre les points qu'il lit (ma
    transcription).
  - Ces deux cas ne passent que par le chemin du code brut. Par le gabarit, la forme de la règle est fixe.
- **`fedb065`, l'état intermédiaire, avait un défaut bloquant** (V62-01). Ses essais ne passaient pas tous : 7 échecs
  sur 53, dont 4 parmi les 45 de la v6.1, l'essai de V6-01 compris.
  - **La cause** : le nouveau contrôle par différences finies (pas de 1e-5) rejetait toute règle arrondie à 8 décimales.
    Cela touchait la règle initiale de Gemini et toute mutation par gabarit (0 sur 120 sur la plage du gabarit, d'après
    ma transcription). Aucune mutation par gabarit ne pouvait donc être acceptée.
  - `3bbb78c` corrige ce défaut : il retire l'arrondi et élargit les bornes, ce qui n'est pas annoncé (§ 1.3).
- **Le rapport de livraison** :
  - **Exact** : la provenance, le nombre d'essais (53 = 34 + 5 + 14) et les essais nommés, qui existent tous.
  - **Inexact** :
    - « LEVÉ » pour les six points partiels ;
    - le « bornage strict du coût unitaire » ;
    - 12 des 26 références de lignes citées ; 8 sont exactes et 6 approchées, à 5 lignes près.
  - **Non dit** : l'échec des essais de `fedb065`, l'élargissement des bornes et deux attentes d'essais ajustées entre
    `fedb065` et `3bbb78c` (§ 8).
  - Ce sont des constats, pas des défauts bloquants.
- **Sous la configuration du pilote 4** (lecture seule) :
  - la mutation est tentée à chaque ronde de conception : 1 appel d'architecte, désormais accepté par le gabarit, comme
    en v6.1 ;
  - le critère de fin de conception est inchangé ;
  - les appels par ronde et par génération sont ceux de la v6.1.

## 1. Provenance (résultat 1)

### 1.1. Objets

L'empreinte d'arbre est calculée par `outils-v1/empreinte_arbre_v1.py`, transcription exacte de `boucle.empreinte_arbre`.
Le commit est lu dans l'en-tête que `git archive` écrit dans l'archive (`comment`). La date est celle des fichiers de
l'archive.

| objet | commit (en-tête de l'archive) | date des fichiers | empreinte d'arbre | fichiers |
|---|---|---|---|---|
| **v6.2 livrée** | `3bbb78c1991baf17feb421529fa1957be7edec59` | 2026-10-25 22:57:18 UTC | **`3b2d8d5a9af75b5457579c847d4ea9510f9da92818805123ed037f7c8436c946`** | 24 |
| v6.2 intermédiaire | `fedb06525610c05945f8496c2058c21a15256fca` | 2026-10-25 21:35:06 UTC | `d02c2907c8eaafb5c9c6768d739b415bfe3d9733a4342b8a16ad77eb19fdb252` | 24 |
| v6.1, base | `a9d8eb50c02c8f5ea31b060b3c0e86f23c2d1dbc` | 2026-10-25 15:20:33 UTC | `ae331d1deb660a20da919edbdcdecba28e49b9b143a6b7a061262101a79798d4` (conforme) | 24 |

- **La v6.1 extraite** est identique, fichier par fichier, à celle de la vérification précédente (même liste de sha256).
- **Journaux** : `verification-v1/empreintes-arbre-*.txt`, `en-tetes-archives-v1.txt`, `sha256-fichiers-*.txt`.
- **Ce que je n'ai pas vérifié**, faute d'autre commande git :
  - le lien de parenté (« un seul commit », « fils unique ») ;
  - la tête distante de la branche.

  Ce que je constate est cohérent avec les deux : de `fedb065` à `3bbb78c`, 4 fichiers changent, pour 12 lignes
  ajoutées et 13 retirées, ce qui est exactement ce qu'annonce le coordinateur.

### 1.2. Ce qui change

- **Inventaire.** Les 24 fichiers sont présents dans les trois arbres ; aucun n'est ajouté ni retiré. De la v6.1 à
  `3bbb78c`, les 6 mêmes fichiers changent, comme annoncé. Les 18 autres sont identiques octet pour octet
  (`inventaire-v61-vers-v62-v1.txt`).
- **Fichiers changés, de la v6.1 à `3bbb78c`** (`diff-v61-vers-3bbb78c-*-v1.txt`) :

  | fichier | ajoutées | retirées | octets |
  |---|---|---|---|
  | `CONCEPTION.md` | 13 | 7 | 20 781 → 22 423 |
  | `manifeste.json` | 2 | 2 | 486 → 541 (`6.2.0`, nom inchangé) |
  | `memoire_isvd.py` | 6 | 2 | 11 699 → 11 797 |
  | `politique_endogene.py` | 94 | 112 | 10 920 → 12 632 |
  | `principal.py` | 128 | 48 | 92 111 → 96 483 |
  | `tests/test_auto_architecte_v6.py` | 195 | 3 | 9 910 → 20 237 |

- **Comparaison par arbre syntaxique** (`fonctions-ast-v61-3bbb78c-v1.txt`) :
  - **`principal.py`** : 33 fonctions inchangées, 6 changées et 2 ajoutées.
    - Changées : `_entrainer_et_predire_sondes_traits`, `_synthetiser_mutation_politique_endogene`,
      `_propager_successeur`, `_traiter_tache`, `executer` et `executer._une`.
    - Ajoutées : `_noter_err` et `_lire_seuil_verifie`.
    - Seule la constante `VERSION` change.
  - **`memoire_isvd.py`** : `_detecter_confirmation_multi_familles` change ; deux tuples de mots-clés sont ajoutés.
  - **`politique_endogene.py`** :
    - 5 fonctions changent, dont `recompense_interne`, qui n'est plus arrondie ;
    - la fonction interne `_cible_validation`, c'est-à-dire le fil, est retirée ;
    - trois constantes sont ajoutées.

### 1.3. État intermédiaire `fedb065`, et ce qu'apporte `3bbb78c`

**Sur `fedb065`, les essais ne passaient pas tous.** Deux exécutions isolées, chacune sur sa copie
(`pytest-v62-poussee-v1.log`, `pytest-v62-poussee-detail-v1.log`), donnent **7 échecs et 46 réussites**, code de sortie 1.

| essai en échec sur `fedb065` | origine | cause |
|---|---|---|
| `test_v6_verificateur_proprete_stricte…` | v6 | la règle initiale est rejetée par son propre contrôle : « Savage violée en p=0.01 (g'=-0.000205, g''=-101.0) » |
| `test_v6_1_filtre_rejette_boucles…` | v6.1 | la sur-confiance de 0,10 est rejetée par la borne 1,005 (valeur 1,006), et non avec le message « propreté stricte » attendu |
| `test_v6_auto_reecriture_effective…` | v6 | mutation rejetée : « Savage violée en p=0.04 » |
| `test_v6_1_successeur_mute_s_importe_et_tourne_dans_processus_neuf` | v6.1 (V6-01) | mutation rejetée dès la première étape (l. 140) : le successeur muté n'existe pas |
| `test_v6_2_point_02_03_04…` | nouveau | 3 appels pour `t_incertain`, alors que l'essai en attend 2 |
| `test_v6_2_point_06…` | nouveau | `ModuleNotFoundError: noyau_client` : l'essai recharge `principal` sans faux noyau |
| `test_v6_2_point_01_et_11…` | nouveau | les mots amputés sont toujours dans `CONCEPTION.md` |

**La cause des quatre premiers échecs : l'arrondi.** Ma transcription du contrôle (`outils-v1/proprete_regles_v3.py`,
`verification-v1/proprete-regles-v62-v1.txt`) donne les mêmes valeurs que les essais de Gemini :
- la règle initiale arrondie à 8 décimales est rejetée ;
- la même règle sans l'arrondi est acceptée ;
- le gabarit arrondi, comme le code de `fedb065`, est rejeté sur toute sa plage : **0 sur 120** (α de 1,15 à 1,85, poids
  de Brier de 0,60 à 0,95) ;
- sans l'arrondi, il est accepté sur toute sa plage : 120 sur 120.

Pourquoi : un arrondi à 1e-8, divisé par h² = 1e-10, fait un bruit de l'ordre de 100 sur g'', et de l'ordre de 5e-4 sur
g', contre un seuil de 1,5e-4. Sous `fedb065`, aucune mutation par gabarit ne pouvait donc être acceptée. Je l'appelle
**V62-01**. Le message du commit (« levée intégrale ») ne le disait pas.

**Ce que change `3bbb78c`** (`diff-fedb065-vers-3bbb78c-*-v1.txt`), en 4 fichiers :
- **`politique_endogene.py`** :
  - l. 23 : `round(…, 8)` devient `float(…)` ;
  - l. 110-111 : **les bornes passent de [−1 ; 1,005] à [−10 ; 10]**, ce que ni le message du commit ni la livraison ne
    disent.
- **`principal.py`** l. 1039 : même retrait de l'arrondi dans le gabarit.
- **`CONCEPTION.md`** : les sept mots amputés sont rétablis (§ 2.10).
- **Essais** (il s'agit de deux essais nouveaux, aucun des 45) :
  - l. 299 : l'attente de `t_incertain` passe de 2 à 3 appels, ce qui aligne l'essai sur le comportement du code ;
  - l. 318 : `importlib.reload(principal)` est retiré de l'essai du point 6.

## 2. Méthode

La méthode est celle de la vérification de la v6.1.

- **Copies.** Chaque exécution a sa copie, faite par `cp -a` de l'arbre extrait, puis passée à `nobody` par `chown -R`.
  Les copies sont sous `essais-v1/`.
- **Commande** : `unshare -n sudo -u nobody env -i PATH=/usr/bin:/bin HOME=<copie> LANG=C.UTF-8 TMPDIR=<copie>/tmp
  PYTHONDONTWRITEBYTECODE=1 [PYTHONHASHSEED=n] /opt/venv-essaim-sim-v1/bin/python -P -s -B …`, jamais `-I`. Chaque ligne
  de commande est recopiée en tête de son journal.
- **Contrôles de l'isolation** (`sonde-isolation-v62-v1.log`) :
  - **graine de hachage** : pour chaque graine, deux lancements donnent la même valeur de `hash("a")`, et les mêmes
    valeurs qu'aux vérifications précédentes (`4644417185603328019`, `-3012895188637184397`, `6352457989142756797`) ;
  - **réseau** : une connexion tentée dans l'espace de noms est refusée (`OSError` 101) ;
  - **utilisateur** : uid 65534, c'est-à-dire `nobody` ;
  - **écritures** : aucun fichier de `nobody` plus récent que 22:58:00 UTC n'existe hors de mon dossier, sous `/tmp`,
    `/var/tmp`, `/home`, `/root`, `/mnt/user-data` et `/opt/venv…`. Les dossiers `runs/`, `donnees/` et `diag/` ont été
    écartés sans y entrer.
- **Analyses statiques** : lancées par `python -I`, sur mes outils ou ceux des vérifications précédentes, lus avant usage.
  Les empreintes de ces derniers sont conformes à `/var/tmp/verification-v61-poussee-v1/EMPREINTES-v1.txt`.
- **Interpréteur** : Python 3.13.17, pytest 9.1.1.

## 3. Essais en isolation (résultat 2)

| objet | exécution | résultat | temps | journal |
|---|---|---|---|---|
| `3bbb78c` | `-q -p no:cacheprovider` | **`53 passed in 4.87s`**, code de sortie 0 | 5,08 s au mur | `pytest-3bbb78c-v1.log` |
| `3bbb78c` | `-v --durations=0` (copie à part) | `53 passed in 4.83s`, code de sortie 0 | 5,00 s au mur | `pytest-3bbb78c-detail-v1.log` |
| `3bbb78c` | essai du point 6, **lancé seul** | **1 échec** (`ModuleNotFoundError: noyau_client`) | 0,37 s | `pytest-3bbb78c-point06-seul-v1.log` |
| `fedb065` | `-q` puis `-v` | 7 échecs, 46 réussites (§ 1.3) | 6,69 s et 5,11 s | `pytest-v62-poussee-*.log` |

- **Répartition** : 34 essais hérités de la v5.2.1, 5 de la v5.3, 14 dans `test_auto_architecte_v6.py` (les 6 de la v6.1
  et 8 nouveaux). C'est la répartition qu'annonce la livraison.
- **Les 45 de la v6.1 sont présents, et aucun n'est affaibli.**
  - 39 sont dans des fichiers identiques octet pour octet à ceux de la v6.1.
  - Dans `test_auto_architecte_v6.py`, la seule différence qui touche les 6 anciens est l'assertion `"croissante" in
    msg_const`, **rétablie** (l. 20-21). Sous `3bbb78c`, elle est atteinte, et l'essai passe.
- **Durées** : les plus longues sont `test_c06` (1,86 s) et `test_c05` (1,57 s) ; l'essai de V6-01 prend 0,09 s.
- **Gemini annonce 17,55 s** : c'est sa machine, l'écart est sans portée.
- **L'essai du point 6 dépend de l'ordre.** Lancé seul, il échoue : il importe `principal` sans faux noyau, et ne passe
  que si un essai précédent a laissé `principal` importé. C'est sans portée sur le code, mais l'essai est fragile.

## 4. Les treize points de la demande, sur `3bbb78c` (résultat 3)

Les lignes sont celles de `3bbb78c`. Le critère est celui de la demande : un point est levé quand le fait décrit n'est
plus vrai du code. Un choix gardé sans raisons ne compte pas comme levé.

| point | constat sur `3bbb78c` | essai (Gemini) ou preuve (moi) | verdict |
|---|---|---|---|
| **1.** Réserve 1, « sans traits, flux identique à la v5.2.1 » | L'affirmation est remplacée par un énoncé exact : `CONCEPTION.md` § 2.13.1, l. 152, seul passage du fichier qui parle de la v5.2.1. Sans traits, mêmes appels, mêmes consignes et mêmes réponses ; la mémoire et la métrique diffèrent. | L'essai cité (`point_01_et_11`) ne contrôle que les octets et les mots de `CONCEPTION.md`, **pas le flux**. **Ma preuve** : `comparaison-invariance-v61-v521-vers-3bbb78c-v1.txt`. En B et D, mêmes appels que les relevés existants de la v5.2.1 (rôle, espèce, plafond, empreinte de chaque consigne), même `reponses_test.json` ; la mémoire et la métrique diffèrent. Cela vaut pour une génération (contexte de génération 1), sous faux noyau. | **Levé** (énoncé conforme ; sans essai de Gemini qui le montre) |
| **2.** Réserve 3, seuil d'exactitude de la sonde à 0,60 | Le seuil est lu dans `seuils_routage()["seuil_exactitude_sonde"]` (0,65 ; `politique_endogene.py` l. 47, `principal.py` l. 1632), puis appliqué l. 1653 à l'exactitude de validation quand elle existe (l. 1948). La marge minimale de 0,10 reste exigée (l. 1656). | `point_02_03_04` : la sonde (validation 1,0) vote sur `t_clair` et `t_neutre`, pas sur `t_incertain` (marge 0,04). **Aucune sonde n'est placée entre 0,60 et 0,65** : le seuil lui-même n'est pas éprouvé. | **Levé** (essai indirect) |
| **3.** Réserve 4, arbitrage redondant dès deux castes | Avec une sonde qui vote, `len(castes) > 1` est retiré (l. 1698-1699). **Sans sonde, il reste** (l. 1700-1701) : `besoin_arbitrage = (conf_c1 < seuil_c1) or (len(castes) > 1)`, toujours vrai dès deux castes. C'est le cas du pilote 4. `CONCEPTION.md` § 2.13.3 le restreint à « lorsqu'une sonde est active », sans raisons. | `point_02_03_04` : `t_neutre` (marge 0,22) n'appelle qu'une caste ; `t_incertain` en appelle 3. Le cas sans sonde n'est pas essayé ; il est conservé à l'identique (mes relevés). | **Partiellement levé** (choix gardé sans raisons : Lazar décide) |
| **4.** Réserve 5, garde sur l'exactitude d'entraînement, documentation absente | Un pli de validation stratifié (25 %, au moins 2 tâches) est tenu à l'écart d'`entrainer` dès 4 tâches (l. 524-535). L'exactitude est calculée par `predire` (l. 587-607) et passée au routage (l. 1948). C'est documenté (§ 2.13.2). **Repli silencieux sur l'exactitude d'entraînement** (l. 609) quand la famille a moins de 4 tâches, ou quand `predire` ne rend pas « OK » ou aucune probabilité valable. Seule l'exception est consignée (l. 606-607). | `point_02_03_04` : la spécification d'entraînement porte 2 tâches sur 4, et `exactitudes_validation` vaut 1,0. L'essai ne distingue pas laquelle des deux exactitudes la garde lit : l'entraînement donne 0,99, la validation 1,0, toutes deux au-dessus de 0,65. | **Partiellement levé** |
| **5.** Réserve 7, trois jeux de mots-clés | Les trois jeux ont désormais le même contenu (5 + 5 mots) : constantes de `memoire_isvd.py` (l. 81-82, employées l. 87-88), littéraux de `ponderer_trace_memoire` initiale (`politique_endogene.py` l. 38-39 ; les constantes l. 9-10 n'y servent pas) et littéraux du gabarit (`principal.py` l. 1054-1055). **La détection reste faite par mots-clés**, en trois copies. | `point_05` : égalité des constantes ; les 25 paires détectées par `_detecter_confirmation_multi_familles` et par la pondération initiale. Le gabarit n'est pas essayé, mais il est lu identique. | **Partiellement levé** |
| **6.** Réserve 9, paramètre `erreurs` | `erreurs: list = None` (l. 466) ; `_noter_err` consigne et ajoute (l. 468-471) ; `executer` passe `erreurs=erreurs` (l. 1870). | `point_06` passe dans la suite, mais échoue lancé seul (§ 3). | **Levé** |
| **7.** Point 2 v6.1, une borne d'attente et une seconde exécution sans borne | Il n'y a plus de fil ni de `join` : `threading` n'est plus importé par `politique_endogene.py`. La seconde exécution est remplacée par un contrôle de l'arbre syntaxique : `ast.parse`, imports `ast` et `math`, cinq fonctions (l. 1539-1550). Mais la validation (`exec` du candidat et appels de propreté, l. 225-250) tourne désormais **dans le fil principal, sans aucune borne de temps**. Une opération longue n'y retarde plus le fil principal : elle le bloque. | `point_07_10` contrôle l'absence de `threading.Thread` et de `exec(`, et rejette **un seul** exposant constant (`9999 ** 99`). **Ma transcription** du filtre statique (`filtre-statique-v62-transcrit-v1.txt`) laisse passer `n ** n ** n`, `9999 ** (4 ** 4 ** 4)`, quatorze `** 4` imbriqués et `'a' * 10000 * 10000 * 10000`. Rien n'en a été exécuté. | **Partiellement levé** |
| **8.** Point 3 v6.1, JSON incomplet accepté, `or 0.78` silencieux | Un JSON sans `alpha`, `poids_brier` ou `seuil_confiance_caste1` finis est refusé, et le refus consigné (l. 1011-1014). Le repli de `_lire_seuil_verifie` est consigné quand une clé est absente, non finie ou hors de [0,05 ; 0,95] (l. 1586-1594, appelée l. 1631-1636) ; un retour qui n'est pas un dictionnaire est consigné aussi (l. 1617-1620). | `point_08` : JSON sans `alpha`, d'où `cle_json_manquante_ou_invalide:alpha` ; seuil 0,0, d'où 0,78 avec l'erreur consignée. | **Levé** |
| **9.** Point 5 v6.1, propreté : sur-confiance légère et transformations affines | **Ma transcription** (`proprete_regles_v4.py`, `proprete-regles-3bbb78c-v1.txt`) : la sur-confiance de 0,02 et celle de 0,10 sont rejetées par la condition de Savage. Des transformations affines, seule l'identité est acceptée (ancrages exacts) ; le gabarit est accepté à 120 sur 120, avec un score de l'exemple de 0,7438 à 0,7469. p est contrôlé jusqu'à 0,99. **Entre les points lus, rien n'est contrôlé** : une règle de Brier avec +0,01 pour y = 1 sur ]0,0151 ; 0,0199[ est **acceptée**, alors que son optimum vrai pour p = 0,012 est q* = 0,0151. Elle passe aussi le filtre statique (70 nœuds). Bornes élargies à [−10 ; 10], non annoncé. | `point_09` : 0,02 rejetée (« propreté stricte ») ; les trois transformations affines du rapport sont rejetées. | **Partiellement levé** (le reste ne passe que par le code brut) |
| **10.** Point 6 v6.1, ce que la liste blanche ne garantit pas (§ 9.4 du rapport v6.1) | **Levés** : erreurs d'analyse (`except Exception`, l. 157), types et bornes des seuils (l. 243-250 et `_lire_seuil_verifie`), seconde exécution (point 7). **Non levés** : le coût d'une opération (point 7 ; ajout de 800 nœuds au plus, constantes ≤ 10 000, chaînes ≤ 450, exposant **constant** ≤ 4), et le successeur, qui s'importe avec toutes les fonctions intégrées (c'est inhérent). **Changé** : le bloc du vérificateur est repéré par la première occurrence du texte `"\nimport ast\nimport math\n"` (l. 1532), qui peut aussi figurer dans une chaîne d'un candidat. Je n'ai pas cherché à l'exploiter. | `point_07_10` (voir 7). | **Partiellement levé** |
| **11.** `CONCEPTION.md` : retours chariot, mots amputés | 0 caractère de contrôle autre que LF, 0 marque d'ordre d'octets (`c01-octets-3bbb78c-v1.txt`). Les sept mots sont rétablis, entre accents graves. | `point_01_et_11` passe. | **Levé** |
| **12.** Assertion `"croissante"` retirée | Rétablie (essais l. 20-21) et atteinte. | `test_v6_verificateur_proprete…` passe. | **Levé** |
| **13.** « alpha=4/3 » dans la définition de la métrique | La définition interpole `politique=` et `alpha=` depuis le module actif (l. 2084-2091). Sous faux noyau : « politique=bregman_tsallis_propre_v6_2_initiale, alpha=1.333333 ». | `point_13` (α mis à 1,45 par l'essai). | **Levé** |

## 5. V6-01, reproductibilité, verrous, gardes, contrat (résultat 4)

### 5.1. V6-01 reste corrigé

Journal : `noms-non-lies-successeurs-3bbb78c-v1.txt`.

- **L'essai `test_v6_1_successeur_mute_s_importe_et_tourne_dans_processus_neuf` passe.** J'ai lu les journaux qu'il
  écrit :
  - **génération 1** : mutation acceptée (`validation_stricte_ok`), 0 erreur, 3 appels, dont 1 d'architecte ;
  - **génération 2**, dans un processus neuf, avec le successeur muté (`NOM_POLITIQUE = bregman_mutee_gen2`) : 0 erreur,
    2 appels, 1 tâche répondue.
- **Aucun nom non lié.** Les successeurs mutés produits par les essais (deux contenus : `11ca1a56…`, en générations 1 et
  2, et `47967ec7…`) lient `math` (l. 1), `ast` (l. 53) et `math` (l. 54). Il en va de même pour l'original (`8e8b58ea…`), pour les 29 successeurs
  recopiés à l'identique et pour `principal.py`.
- **La seconde ligne de défense a changé de nature.** Ce n'est plus une exécution du fichier assemblé, mais un contrôle
  de l'arbre syntaxique (l. 1539-1550) : imports et définitions de niveau module. Un nom non lié dans le corps d'une
  fonction n'y serait pas vu. C'est l'essai en processus neuf qui couvre ce cas.
- **Sous `fedb065`**, cet essai échouait avant l'assemblage. J'ai donc reconstruit le fichier par ma transcription de
  l'assemblage (`outils-v1/assembler_successeur_v1.py`, sans exécuter de code de Gemini), puis je l'ai importé dans un
  processus neuf isolé : il s'importe, et ses noms sont liés. Mais son propre vérificateur le rejetait, au titre de
  V62-01 (`v6-01-successeur-transcrit-v62-v1.txt`).

### 5.2. Reproductibilité : cas B et D, graines de hachage 0, 1 et 2

L'outil est `invariance_v1.py`, lu avant usage, d'empreinte `1fe2609c…`. Journal : `invariance-3bbb78c-v1.log`.

| cas | appels | `budget()` / `especes()` | recherches / téléchargements | sha256 des 3 relevés |
|---|---|---|---|---|
| B | 28 | 46 / 1 | 0 / 0 | `139c903665f8a05b…`, identique pour les trois, et identique sous `fedb065` |
| D | 29 | 53 / 1 | 2 / 1 | `423c5a3fc905530d…`, identique pour les trois, et identique sous `fedb065` |

**Par rapport à la v6.1** (relevés de référence refaits en isolation, mêmes empreintes qu'à la vérification
précédente : `d1098683…`, `30381a75…`) :
- **appels** : même nombre ; même suite de rôles, d'espèces et de plafonds ; même empreinte pour chaque consigne ;
- **identiques** : `memoire_isvd.json`, `reponses_test.json` et `reponse-question.md` ;
- **la métrique** a la même valeur ; seule sa définition change (point 13) ;
- **le journal de génération** ne change que par la version et par un champ nouveau, `sonde_incertaine_ou_discorde`
  (faux), sur 3 tâches.

Le retrait de l'arrondi ne change aucun fichier de sortie, ici, entre `fedb065` et `3bbb78c`.

### 5.3. Verrous

Journal : `verrous-3bbb78c-v1.txt`.
- 0 appel imbriqué, avec l'outil des appels directs comme avec celui des chaînes d'appels internes. Il n'y a aucun
  `acquire` ni `release` explicite.
- Les six mêmes fonctions qu'en v6.1 prennent `_VERROU`. `_lire_seuil_verifie` et `_noter_err` le prennent par
  `_consigner_erreur`, et ne sont jamais appelées en le tenant.
- `politique_endogene.py`, `memoire_isvd.py` et `mitose_spectrale.py` ne le prennent jamais.

### 5.4. Gardes C-01 à C-13

Les 13 essais `test_c01` à `test_c13` passent. Les fonctions qui portent les gardes sont inchangées par l'arbre
syntaxique, sauf `_traiter_tache` (C-03) et `executer` (C-05) :
- **C-01** : aucune marque d'ordre d'octets ni caractère de contrôle autre que LF dans les `.py`, `.json` et `.md`.
  `CONCEPTION.md` est désormais propre.
- **C-03** : les étiquettes sont lues dans chaque tâche (l. 1611), et la sonde prend `etiquettes[0]` ou `etiquettes[1]`
  (l. 1655).
- **C-05** : le `try` d'`executer` commence l. 1830 ; `except Exception` est l. 2003 et `finally` l. 2005, qui écrit
  mémoire, métrique, journal et successeur. La mutation est appelée dans le `try` (l. 1992).
- **C-02 et C-09** (`_parser_decision_tache` l. 674, `_extraire_json_candidat` l. 639), **C-04** (`_selection_stratifiee`
  l. 1081), **C-06** (`_faut_basculer` l. 1565), **C-07** (`charger_connaissances_archive`, `memoire_isvd.py` l. 266) et
  **C-08** (`_confiance_finie` l. 666) : inchangées.
- **C-10 et C-11** : le dossier `metrique/` est identique.
- **C-12** : § 5.3.
- **C-13** : les constantes d'ouverture et de fermeture (l. 26-27), `_sanitiser_donnee_externe` (l. 249, avec le
  remplacement de « === » l. 253) et `_bloc_moisson_borne` (l. 1100) sont inchangées.

### 5.5. Contrat du noyau

Motifs : `motifs-3bbb78c-v1.txt` et `motifs-v62-v1.txt`.
- **Aucun interdit.** Ni sous-processus, ni réseau, ni variable d'environnement, ni `importlib`, `ctypes` ou
  `multiprocessing` dans le code de l'organisme. Ces mots ne paraissent que dans la liste `NOMS_INTERDITS` (l. 69-73).
- **`exec` et `compile`** ne restent qu'à `politique_endogene.py` l. 226-227 (validation du candidat). `principal.py`
  n'en contient plus.
- **Lectures et écritures** : les mêmes qu'en v6.1, aux lignes décalées (archive l. 298, téléchargement servi l. 415,
  mémoire locale l. 1802, propre `politique_endogene.py` l. 1531). Toutes les écritures se font sous `dossier_travail`,
  successeur compris (l. 1551-1558).
- **Dans les essais**, `subprocess` ne sert qu'à l'essai de V6-01 (l. 4 et 160), ce qui est permis aux essais.

## 6. Sous la configuration du pilote 4 (résultat 5)

C'est une lecture du code de `3bbb78c`, sans exécution hors des essais. La configuration : jusqu'à 6 rondes de
conception à 3 USD au plus, puis 4 générations notées, aucun entraînement (`--entrainements-max 0`).

- **Sans traits ni entraînement, les sondes ne tournent pas.** `_entrainer_et_predire_sondes_traits` rend « inactif »
  (l. 474 sans traits, l. 481 quand `entrainements_restants` vaut 0). Le routage prend donc la branche sans sonde
  (l. 1700-1701), qui est celle de la v6.1.
- **La mutation est tentée à chaque ronde de conception.**
  - **Où et à quelles conditions** : `_synthetiser_mutation_politique_endogene` est appelée dans le `try` d'`executer`
    (l. 1992). Elle tente la mutation si `phase == "conception"` (l. 976), puis si `_peut_appeler` le permet (l. 979).
  - **L'appel** : un appel d'architecte (l. 992-999), plafonné par `_plafond_tokens_effectif(contexte, 8192)`, avec une
    consigne identique à la v6.1 (v6.1 l. 938-946 = l. 982-990).
  - **L'issue** :
    - un JSON complet passe par le gabarit, et il est **accepté**, comme en v6.1 (120 sur 120 sur la plage, d'après ma
      transcription) ; le successeur est muté (l. 2139, dans le `finally`) ;
    - **ce qui change par rapport à la v6.1** : un JSON incomplet est refusé, alors que la v6.1 mutait avec des valeurs
      par défaut ;
    - sous `fedb065`, toute mutation par gabarit aurait été refusée (V62-01).
  - **En génération**, la condition est inchangée : génération ≥ 1 et stagnation (l. 970-977, § 7).
- **Le critère de fin de conception** (l. 2063-2068) est celui de la v6.1. La conception s'arrête à la première de ces
  conditions :
  - un score interne d'au moins 0,78 avec au moins deux exemplaires ;
  - à partir de la ronde 2, un score d'au moins 0,65 ;
  - la dernière ronde permise.

  La règle initiale n'étant plus arrondie, le score interne diffère de celui de la v6.1 de moins de 5e-9. Une décision ne
  pourrait en changer qu'à égalité exacte.
- **Appels par ronde et par génération : ceux de la v6.1**, d'après la lecture. Sans sonde, le flux par tâche est
  identique (§ 5.2), et la mutation ajoute toujours un appel, dans les mêmes conditions.
  - Une mutation acceptée change les seuils du successeur, dont `seuil_confiance_caste1`. Mais sans sonde, et dès deux
    castes, `besoin_arbitrage` est toujours vrai (l. 1701). Avec une seule caste, il n'y a pas d'arbitrage (l. 1703). Le
    nombre d'appels n'en dépend donc pas.
  - La validation n'a plus de borne de temps. Pour un candidat du gabarit, elle ne dure que quelques millisecondes.
- **Les comptes de la simulation** (v6.1 : 7 appels en c001, 124 en g003) **ne se lisent pas dans les essais de Gemini.**
  Le seul essai de conception (`test_v5_3_phase_conception…`) fait 4 appels : 2 de calibrage, 1 d'induction et 1
  d'architecte, dont la mutation est refusée, faute de clé `alpha` dans la réponse du faux noyau. L'essai de V6-01 fait
  3 appels en génération 1, dont 1 de mutation acceptée, puis 2 en génération 2.

## 7. Lignes que cite le préenregistrement du pilote 4 (résultat 6)

Journal : `lignes-preenregistrement-pilote4-v61-vers-3bbb78c-v1.txt`. Toutes ces lignes ont le même texte qu'en v6.1, à
leur nouvelle place :

| citation (v6.1) | `3bbb78c` | comportement |
|---|---|---|
| `principal.py` l. 1985-1990, fin de conception | **l. 2063-2068** | inchangé |
| l. 926-933, mutation et stagnation | **l. 970-977** | texte inchangé ; un JSON incomplet est désormais refusé (l. 1011-1014) |
| l. 1927 puis 1950, `finally`, puis mise à jour de la mémoire | **l. 2005, puis 2028** (bloc v6.1 l. 1927-1960 = l. 2005-2038) | appel inchangé ; la pondération reçue (l. 2039) compte désormais aussi « laboratoire » comme mot d'évaluation (point 5) |
| l. 740, exemple de format | **l. 784** (bloc v6.1 l. 733-741 = l. 777-785) | inchangé |
| l. 86-95, dix requêtes de réserve | **l. 87-96** | inchangées |
| `memoire_isvd.py` l. 236-244, six dernières entrées, celle du même numéro retirée | **l. 240-248** | inchangé |
| `memoire_isvd.py` l. 114-117, score de g0 à g001 | **l. 118-121** | inchangé |
| `memoire_isvd.py` l. 125-127, meilleur ancêtre | **l. 129-131** | inchangé |
| `mitose_spectrale.py` l. 75 et 117, stagnation | **l. 75 et 117** (fichier identique) | inchangé |

Les mêmes correspondances valent pour `fedb065`, dont `principal.py` et `memoire_isvd.py` ont les mêmes numéros de ligne.

## 8. Le rapport de livraison confronté au code de `3bbb78c`

**La pièce.** `/var/tmp/fournis-verification-v62/livraison-gemini-v6-2-recue-2026-10-25-2309-v1.txt` : 12 689 octets,
fins de ligne CRLF, sha256 `e9471860…` (son compagnon `.sha256` est conforme). Je l'ai lue comme une donnée.

**Ce qui est exact** :
- **Provenance.** La sortie de `git ls-remote` qu'il cite, `3bbb78c1991baf17feb421529fa1957be7edec59
  refs/heads/canal/gemini-organisme-v6-2`, est cohérente avec l'en-tête de l'archive et avec le relevé du coordinateur.
  Je ne l'ai pas refaite.
- **Essais.** 53 = 34 + 5 + 14, les fichiers hérités inchangés octet pour octet, l'assertion du point 12 rétablie, les
  6 fichiers changés et les 18 inchangés.

**Ce qui est inexact ou non dit** :
- **« LEVÉ » pour les 13 points** : 6 ne le sont qu'en partie (§ 4).
- **« bornage strict du coût unitaire de chaque nœud »** (points 7 et 10) : c'est inexact (point 7).
- **Ce que la livraison ne dit pas** :
  - les 7 échecs de `fedb065` ;
  - l'élargissement des bornes de [−1 ; 1,005] à [−10 ; 10] (l. 110-111) ;
  - l'attente de `t_incertain` passée de 2 à 3 appels ;
  - le retrait de `importlib.reload` (§ 1.3).
- **Point 1** :
  - le rapport situe le changement aux « § 2.11 et § 2.13.1 », mais le § 2.11 n'a pas changé ;
  - il parle des « consignes de la génération 0 », là où `CONCEPTION.md` dit « première génération » ; mon relevé porte
    sur une génération, en contexte de génération 1.
- **Point 3** : il est dit « LEVÉ » alors que la livraison elle-même le restreint à « lorsque la sonde est active ».

**Lignes citées** (`lignes-citees-livraison-vs-3bbb78c-v1.txt`). Sur 26 références : 8 exactes, 6 approchées (à 5 lignes
près) et 12 fausses.

| point | référence citée | lignes réelles | |
|---|---|---|---|
| 2 | `politique_endogene.py` l. 44-53 ; `principal.py` l. 1637 et 1656 | 44-52 ; 1632 et 1656 | exacte ; fausse (l. 1637 est vide) ; exacte |
| 3 | l. 1697-1700 | 1698-1701 | approchée |
| 4 | l. 512-522 et 569-589 ; `executer` l. 1882 | 524-535 et 587-609 ; 1948 | fausse ; fausse ; fausse |
| 5 | `memoire_isvd.py` l. 7-8 et 83-88 ; `politique_endogene.py` l. 9-10 et 36-41 ; gabarit l. 1054-1059 | 81-82 et 85-89 ; exactes ; 1054-1057 | fausse ; approchée ; exacte ; exacte ; exacte |
| 6 | l. 461-467 et 1829 | 461-467 et 1870 | exacte ; fausse |
| 7 | l. 1528-1545 | 1530-1551 | approchée |
| 8 | l. 1007-1011 ; `_lire_seuil_verifie` l. 1572-1580, appelée l. 1636-1641 | 1011-1014 ; 1586-1594 ; 1631-1636 | approchée ; fausse ; approchée |
| 9 | l. 114-169 ; `recompense_interne` l. 22 | 95-148 ; 23 | fausse ; approchée |
| 10 | l. 172-275 ; `principal.py` l. 1522-1525 | 151-253 (le fichier a 253 lignes) ; 1532 | fausse ; fausse |
| 1 et 11 | `CONCEPTION.md` § 2.11 et § 2.13.1 | § 2.13.1, l. 152 ; § 2.11 inchangé | fausse ; exacte |
| 12 | essais l. 20-21 | 20-21 | exacte |
| 13 | l. 2033-2040 | 2084-2091 | fausse |

Les neuf essais nommés existent, et passent dans la suite. Ce qu'ils montrent pour chaque point est au § 4.

## 9. Réserves de cette vérification

1. **Ce qui repose sur mes transcriptions.**
   - **Propreté, filtre statique, assemblage du successeur** : les verdicts « accepte », « passe » et « rejet » de ces
     pages viennent de mes transcriptions, pas du code de Gemini. Elles redonnent exactement les messages des essais de
     Gemini sur `fedb065`.
   - **Rien n'a été exécuté** pour éprouver le coût des candidats lourds, ni le bonus caché : ils ont seulement été
     analysés.
2. **Ce qui ne vient que de la lecture.** Le comportement sous le pilote 4 (§ 6) vient de la lecture de l'organisme. Je
   n'ai relu du noyau que la transcription de l'empreinte d'arbre. Ce que le noyau met dans `historique` pendant la
   conception n'est pas revérifié ici.
3. **Ce que je n'ai pas revérifié moi-même.**
   - **Provenance distante** : la tête de branche et la parenté des commits viennent du coordinateur et du rapport ; je
     n'avais que l'extraction.
   - **v5.2.1** : la comparaison du point 1 se fait avec des relevés existants (`/var/tmp/essai-v521-inv/`), que je n'ai
     pas régénérés.
4. **Durée.** Environ vingt-cinq minutes jusqu'à l'écriture, objet changé en cours de route (message reçu après 23:09
   UTC). Les deux transcriptions de propreté (v3 pour
   `fedb065`, v4 pour `3bbb78c`) sont gardées toutes deux.

Je n'ai rien préparé d'autre : ni préenregistrement, ni message à Gemini. La suite est ta décision.

## 10. Contenu de ce dossier

- `LISEZMOI-v1.md` est ce rapport, et `EMPREINTES-v1.txt` contient le sha256 de chaque pièce, des outils et des entrées
  lues. Contrôle : `sha256sum -c EMPREINTES-v1.txt` depuis ce dossier.
- `verification-v1/` : journaux d'essais, d'invariance et d'isolation, relevés, différences, inventaires, analyses.
- `outils-v1/` : mes outils, qui ne font que lire et se lancent par `python -I`. Ce sont `empreinte_arbre_v1.py`,
  `comparer_releves_v1.py`, `diff_json_v1.py` et `proprete_regles_v2.py`, recopiés de la vérification v6.1, puis
  `proprete_regles_v3.py`, `proprete_regles_v4.py`, `filtre_statique_v62_transcrit_v1.py` et
  `assembler_successeur_v1.py`, qui sont nouveaux.
- `archives-v1/` : les trois archives extraites (`.tar`). `extraction-*` : les arbres extraits. `essais-v1/` : les copies
  d'essai, propriété de `nobody`. Ces trois dossiers sont hors du zip, et leurs empreintes sont dans `EMPREINTES-v1.txt`.
- `livrable-verification-v62-poussee-v1.zip` : `LISEZMOI-v1.md`, `EMPREINTES-v1.txt`, `verification-v1/` et `outils-v1/`.
