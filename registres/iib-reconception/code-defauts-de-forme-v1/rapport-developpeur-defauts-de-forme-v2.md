# Rapport du développeur — trois défauts de forme des programmes de lancement de la course du saboteur à budget (version 2)

Date : 2026-11-19. Pièce d'instrument (classe B). Remplace le rapport en version 1 (`rapport-developpeur-defauts-de-forme-v1.md`, `bed307fa…28d5`, intact) après la contre-lecture `contre-lecture-code-lanceur-v2-cl1.md` (`06b261ac…0d49`, empreinte vérifiée) : verdict « autorisable après corrections », un bloquant, trois majeurs, huit mineurs. Rien poussé, rien dépensé, aucun appel au loueur de machines, aucun refus d'outil rencontré.

- Arbre de travail : `/tmp/claude-0/-home-user-controle-ia-travail/43943324-c96f-5191-9f95-633db6e7fd97/scratchpad/developpeur-forme/arbre`, branche locale `prep/iib-code-v5`.
- Commits (`git log --oneline origin/prep/iib-code-v4..HEAD`) : `e2c90f97` (version contre-lue), puis `806bce0f` (corrections de la contre-lecture).

## 1. Fichiers (aucun fichier antérieur à `e2c90f97` n'est modifié)

| Fichier | Empreinte à `806bce0f` | État |
|---|---|---|
| `scripts/lancer_iib_v2.sh` | `a0478ebe2c9b22571b912f6cc7a34c1a0d4f6b180a5d81986ac7bd9c49193929` | modifié (non scellé) |
| `src/controle_ia/iib/location_v1.py` | `6446a304357338ab5a3a4a92de9eb8c0225db86eeec91541ab95dd25b6b92db3` | **neuf** : lecture par programme des sorties du loueur (masquage, verdict de création, inventaire) ; bibliothèque standard seulement |
| `tests/test_iib_lanceur_forme_v2.py` | `3dc621480c1a006bc04ae9ab567402ff7a5da72f6ce3cbe1fdae7fbfd1792804` | modifié : 136 essais (57 avant) |
| `scripts/lancer_iib_v1.sh` | `3279e3dcc631519e574c2011f9f143d956d3b668c729a176cd8efc0e99dece8f` | intact (empreinte de l'ordre scellé, vérifiée par un essai) |

Le lanceur cherche `location_v1.py` à côté de lui, dans son propre arbre (`scripts/../src/controle_ia/iib/`), et non dans `IIB_DEPOT`. L'extraction réduite de l'ordre (`/scripts/ /src/`) le contient.

## 2. Corrections, remarque par remarque

### Bloquant 1 — destruction d'une autre machine
- **Lecture de l'identifiant créé** (`location_v1.py`, `verdict_creation`) : la réponse est analysée comme JSON strict, sans clé en double ; l'identifiant est la valeur de la clé `new_contract` du premier niveau. Le motif cherché dans tout le texte a disparu du lanceur.
- Refus (« création incertaine », code 4, **aucun identifiant consigné**) si : la réponse n'est pas du JSON (forme `repr` de Python comprise) ; ce n'est pas un objet ; la clé manque ; la valeur n'est pas un entier positif (chaîne, booléen, zéro, négatif, décimal) ; une clé est en double ; une autre valeur candidate existe (clé `new_contract` plus profonde, ou `new_contract: <chiffres>` cité dans un texte) ; `success` n'est pas vrai au premier niveau.
- Écart à ta consigne, à trancher (point 1 du § 5) : le contre-lecteur proposait d'accepter aussi la forme `repr` de Python ; ta consigne dit « analysée comme JSON », je refuse donc cette forme.
- **Gardes de la destruction, toutes avant le moindre appel de destruction** :
  - identifiant non vide, chiffres seuls, sans zéro de tête, égal à la dernière ligne `instance` de `lancement.txt` ;
  - identifiant hors de `IIB_INSTANCES_INTOUCHABLES` (identifiants séparés par des virgules ; liste vide permise, dite sur la sortie et dans `destruction.txt` ; liste illisible : refus) ;
  - l'inventaire d'avant doit montrer l'instance, avec une étiquette qui commence par celle que le lanceur a posée à la création (ligne neuve `etiquette` de `lancement.txt`, écrite par `creation` ; à défaut `offre.etiquette` de `config.json` ; elle-même doit commencer par `iib`). Sinon refus, code 2.

### Majeur 2 — un inventaire vide, illisible ou en erreur n'est jamais une preuve
- Instance absente de l'inventaire d'avant : **code 7**, « ABSENCE NON CONFIRMÉE », aucune commande envoyée, aucune ligne `destruction_verifiee`.
- Inventaire illisible ou appel en échec : code 4, avant comme après.
- « DÉTRUITE » (code 0, seule écriture de `destruction_verifiee`) exige : commande de destruction au code 0 ; puis **deux relectures consécutives** de l'inventaire, chacune avec un appel au code 0, analysable, où l'instance est absente **et où toutes les autres instances vues avant sont encore là**. Un inventaire revenu vide alors que le compte portait d'autres machines est dit « vide ou amputé », code 4.
- `IIB_DESTRUCTION_RELECTURES` doit valoir au moins 2.
- Un inventaire est illisible, et jamais lu comme vide, s'il est vide de texte, non JSON, un objet d'erreur, `null`, ou s'il porte une entrée sans identifiant entier ou un identifiant en double.

### Majeur 3 — inventaires versés aux traces
- **Les traces (`traces-location/`) ne gardent plus que les champs filtrés des seules instances du saboteur** : identifiant, étiquette, état (`actual_status`, `cur_state`, `intended_status`, `next_state`), prix (`dph_total`, `dph_base`, `storage_cost`, `storage_total_cost`), machine (`machine_id`, `host_id`, `gpu_name`, `num_gpus`, `disk_space`, `start_date`), plus le nombre d'instances du compte. **L'inventaire entier du compte n'est jamais conservé**, ni aux traces ni ailleurs.
- Le fichier de travail du dossier de session ne garde, pour chaque instance du compte, que l'identifiant, l'étiquette et l'état (ce qu'il faut à la règle « aucune instance iib » de la création).
- La sortie brute de l'inventaire va d'abord sur disque, droits restreints, puis est remplacée par cette forme réduite. Si elle est illisible, elle est gardée entière dans un fichier `….NON-MASQUE`, droits `600`, hors des traces.
- Le point 5 du § 5 de la version 1 (« à ne pas verser sans le filtre ») n'a plus lieu d'être : le filtre est fait par programme.

### Majeur 4 — masquage
- Par **analyse de la structure** quand la sortie est du JSON sans clé en double : toute valeur sous une clé dont le nom contient `key`, `token`, `secret`, `passw`, `credential`, `auth`, `jeton` ou `cookie` (casse indifférente, donc `jupyter_token`, `OPENAI_API_KEY`, `Db_PassWord`, `Authorization`) ; toute paire `["NOM", valeur]` dont le nom est de ce type ; puis les motifs dans chaque chaîne (affectations `NOM=valeur`, JSON échappé dans une chaîne, `Bearer …`).
- Par **motifs** sinon : champs nommés et paires entre guillemets doubles, simples ou doubles échappés ; valeurs nues ; affectations ; `Bearer`/`Basic` ; jetons à préfixe (`hf_`, `ghp_`, `github_pat_`, `sk-`, `xox…-`, `AKIA…`, jetons en trois parties).
- Valeurs des clés de l'environnement : forme brute et formes échappées en JSON (`\/`, `\uXXXX`).
- Le lanceur dit le mode (« structure » ou « motifs »), le nombre de remplacements, et que **le masquage n'est pas une garde des secrets**.
- **Si le masquage échoue** : la sortie est déjà sur disque (jamais dans un tube) ; elle est gardée entière sous le nom `….NON-MASQUE`, droits `600`, le lanceur le dit, rien n'est versé aux traces, et aucun champ de la réponse n'est imprimé (mineur 9).

### Mineurs
| Remarque | Correction |
|---|---|
| 5, 8 — traces écrasées | copie aux traces par création exclusive ; fichiers de travail à nom daté et unique (`mktemp`) ; la réponse de création porte le numéro de l'essai (`creation-brute-essai<n>.json`, refus si elle existe) ; plus de `destruction-sortie.txt` ni de `instances*.json` à nom fixe |
| 6 — « gardée » inexact | toute sortie va d'abord sur disque ; voir majeur 4 |
| 7 — sortie d'erreur des inventaires | gardée dans un fichier `.err` daté, masquée |
| 9 — extrait après un masquage en échec | plus imprimé |
| 10 — identifiant vide | test explicite, code 2 |
| 11 — garde d'état et de calendrier | état de l'inventaire exigé parmi `exited` et `stopped` (réglable par `IIB_DESTRUCTION_ETATS_ARRET`, dit au journal) ; `RAPATRIEMENT_VERIFIE=oui` exigé, sinon refus |
| 12 — essais | voir § 3 |

## 3. Essais (`tests/test_iib_lanceur_forme_v2.py`, 136 essais, faux outil de location seulement)

**Les sept attaques du contre-lecteur, reprises et tenues :**

| Attaque | Essai | Ce qui est tenu |
|---|---|---|
| 1 | `test_attaque_1_reponse_piegee_…` | code 4, « plusieurs valeurs candidates », aucune ligne `instance` ; destruction de l'autre machine refusée, aucun appel, machine encore à l'inventaire |
| 1, seconde ligne | `test_attaque_1_bis_…` | autre machine consignée par erreur : refus par l'étiquette (`a1-v4`), refus par la liste des intouchables |
| 2 | `test_attaque_2_inventaire_vide_par_erreur_…` | `[]`, `{"instances": null}`, `{"instances": []}` : code 7, aucune commande, aucune ligne vérifiée |
| 2, après | `test_attaque_2_bis_…` | inventaire revenu vide après la commande alors qu'une autre machine existait : code 4 |
| 3 | `test_attaque_3_…` | code 4, une seule commande ; inventaires illisibles gardés entiers, droits `600`, hors des traces |
| 4 | `test_attaque_4_identifiants_pieges` (8 cas), `test_attaque_4_bis_…` | zéro de tête, espace, saut de ligne, vide, `-1`, `0`, `+`, décimal : code 2, aucun appel ; deux lignes `instance` : seul le dernier identifiant |
| 5 | `test_attaque_5_…` | aucun fichier du dossier de session ne porte un secret d'une autre machine, ni son nom de variable, ni le jeton de bloc-notes du saboteur ; la trace égale exactement les champs filtrés de l'instance du saboteur |
| 6 | `test_attaque_6_…` | paire, jeton de bloc-notes, mot de passe imbriqué : absents de la copie, de l'original et de la sortie |
| 7 | `test_attaque_7_…` | après une seconde destruction, tous les fichiers de la première sont identiques octet pour octet (les deux journaux ne font que grandir) |

**Gardes neuves, cas sain et artefact :**
- rapatriement non attesté ou autre mot ; identifiant dans la liste ; liste illisible ; états illisibles : code 2, aucun appel (5 cas). Liste saine : dite, destruction faite, l'autre machine reste.
- inventaire : instance en marche, état absent, étiquette d'un autre chantier, sans étiquette, étiquette `iib` d'une autre course : code 2 sans appel de destruction (5 cas).
- étiquette de la création inconnue ; étiquette d'un autre chantier dans la configuration ; repli sain sur la configuration.
- appel d'inventaire en erreur : code 4, sortie d'erreur gardée, clé du loueur masquée.
- une seule relecture « absente » (inventaire qui clignote) : code 4 ; `IIB_DESTRUCTION_RELECTURES=1` refusé.
- compte à une seule instance, vide deux fois de suite : détruite (cas sain du même contrôle).
- **l'essai sain mord sur `-y`, dans la suite** : une copie du lanceur privée de l'option rend le code 6 sur le même faux outil.

**Lecture par programme, sans lanceur :**
- verdict de création : 19 formes de réponse (2 saines, 17 artefacts) ;
- masquage : 15 formes ouvertes (paires, clés nommées, échappées, forme Python, clé en double), valeur de l'environnement sous six formes échappées, et un cas sain où rien d'autre n'est retiré ;
- inventaire : 9 formes illisibles jamais lues comme vides ; trace jamais écrasée.

Les 25 essais de `tests/test_iib_scripts_v1.py` rejoués contre la version 2 passent toujours.

## 4. Sortie brute des essais ciblés

Fichier : `/tmp/claude-0/-home-user-controle-ia-travail/43943324-c96f-5191-9f95-633db6e7fd97/scratchpad/developpeur-forme/sortie-essais-cibles-v2.txt`.

```
$ PYTHONPATH=src python3 -m pytest -q --tb=line -rfE tests/test_iib_lanceur_forme_v2.py tests/test_iib_scripts_v1.py tests/test_iib_amorce_v1.py tests/test_iib_lanceur_v1.py
src/controle_ia/iib/lanceur_v1.py:40: in <module>
    import torch
E   ModuleNotFoundError: No module named 'torch'
ERROR tests/test_iib_lanceur_v1.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.49s

$ PYTHONPATH=src python3 -m pytest -q --tb=line -rfE tests/test_iib_lanceur_forme_v2.py tests/test_iib_scripts_v1.py tests/test_iib_amorce_v1.py
........................................................................ [ 35%]
........................................................................ [ 70%]
......................................................FFFF..             [100%]
FAILED tests/test_iib_amorce_v1.py::test_sain_progres_d_un_jeu_jouet_complet_du_lanceur_relaye_par_les_deux_motifs_de_l_amorce
FAILED tests/test_iib_amorce_v1.py::test_sain_progres_d_un_jeu_jouet_arrete_aux_epreuves_relaye_par_les_deux_motifs_de_l_amorce
FAILED tests/test_iib_amorce_v1.py::test_artefact_ancienne_forme_de_la_ligne_des_epreuves_retenue_par_le_relais[jouet0-aucun]
FAILED tests/test_iib_amorce_v1.py::test_artefact_ancienne_forme_de_la_ligne_des_epreuves_retenue_par_le_relais[jouet1-E-O6]
4 failed, 200 passed in 73.18s (0:01:13)      (les quatre échecs : ModuleNotFoundError: No module named 'torch')

$ PYTHONPATH=src python3 -m pytest -q tests/test_iib_lanceur_forme_v2.py
........................................................................ [ 52%]
................................................................         [100%]
136 passed in 37.55s
```

Le fichier d'attaques du contre-lecteur, lancé tel quel depuis mon arbre, n'a pas pu être collecté (`ModuleNotFoundError: No module named 'controle_ia.iib'` : il est rangé dans l'arbre principal, dont la branche n'a pas ce module). De plus son attaque 7 lit `destruction-sortie.txt`, fichier à nom fixe que la correction a retiré. Les sept attaques sont donc tenues par leur reprise dans ma suite, pas par le fichier d'origine.

## 5. Ce qui reste non éprouvé, et les points à trancher

**Non éprouvé (conditions avant tout emploi réel) :**
- a. `tests/test_iib_lanceur_v1.py` (non collecté) et quatre essais de `tests/test_iib_amorce_v1.py` : la bibliothèque `torch` manque dans mon conteneur. Code que je n'ai pas touché ; à rejouer sur un poste qui l'a.
- b. **L'option `-y` de l'outil réel**, et sa place après l'identifiant : connue par la seule ligne R-3722. À vérifier sur le poste de l'exécutante par l'aide de `destroy instance` de la version 1.8.3, avant tout emploi : c'est une condition, pas un détail.
- c. **La forme réelle des sorties du loueur** : réponse de création (est-elle du JSON pur sous `--raw` ? sinon toute création sera dite incertaine, code 4) ; inventaire (liste, ou autre enveloppe ?) ; nom et valeurs du champ d'état d'une instance arrêtée (`exited` et `stopped` sont une supposition) ; étiquette au champ `label`. Un écart rend des refus, jamais une destruction à tort.
- d. Délai réel entre la destruction et la disparition à l'inventaire (6 relectures à 10 secondes par défaut : choix à moi).
- e. Le masquage reste une liste de formes : un secret sous un nom neutre et sans préfixe connu passerait. La garde des secrets reste exigée avant tout versement.

**Points à trancher par la mère (liste exacte, six points) :**
1. Réponse de création sous la forme `repr` de Python : refusée (ta consigne), alors que le contre-lecteur proposait de l'accepter en second. À confirmer une fois la forme réelle connue (point c).
2. Journal de la surveillance : `journal-dernier.txt`, `journal-instance.txt` et le relevé brut `journal-brut.tmp` sont toujours remplacés à chaque relevé (20 000 lignes par minute). Seuls écrasements restants du lanceur, gardés par un essai. Les dater tous, ou garder ce régime ?
3. `IIB_DESTRUCTION_ETATS_ARRET` permet à l'exécutante d'élargir les états admis (par exemple si l'outil réel dit autre chose que `exited`). C'est une porte de sortie explicite et consignée au journal, mais c'est une porte : la garder, ou figer la liste ?
4. Chemin de l'outil portant une espace ou un caractère hors de `[A-Za-z0-9_./+-]` : refusé, même trouvé par le PATH (la version 1 l'aurait imprimé tel quel dans la commande).
5. `RAPATRIEMENT_VERIFIE=oui` est une attestation de l'exécutante, pas une preuve lue par le programme. Suffit-elle, ou faut-il une ligne écrite dans `lancement.txt` par une étape de rapatriement à programmer ?
6. Liste des essais joués dans l'instance (`scripts/tests-cibles-iib-v1.txt`, empreinte en dur dans l'amorce) : le fichier d'essais neuf n'y est pas. L'y mettre oblige à une amorce en version nouvelle et à un autre nombre attendu que 456.

## 6. Ce que la version 2 du lanceur oblige à changer dans l'ordre et dans la configuration

**Ce n'est pas une mise à jour de routine.** La liste des empreintes du code (`EMPREINTES_CODE_IIB`, 34 fichiers) est écrite dans la configuration scellée de la course et dans le § 11 de l'ordre scellé. La changer (37 fichiers : `scripts/lancer_iib_v2.sh`, `src/controle_ia/iib/location_v1.py`, `tests/test_iib_lanceur_forme_v2.py` en plus) touche **une pièce décisive** : il faut une configuration en version nouvelle et un ordre en version nouvelle, avec la chaîne complète (contre-lecture, scellement, mot de Lazar selon la classe A), sur un commit de lancement neuf. Rien de cela n'est fait ici ; l'ordre et la configuration scellés ne sont pas touchés.

Lignes de commande à changer dans l'ordre neuf (§ 5 de l'ordre) :

| Lieu | Ancien texte | Nouveau texte |
|---|---|---|
| consignes permanentes | « Commandes vérifiées contre `scripts/lancer_iib_v1.sh` … (`3279e3dc…ece8f`) » | même phrase pour `scripts/lancer_iib_v2.sh`, à son empreinte au commit de lancement neuf |
| étape 1, premier point | `vastai --version` → `1.8.3` ; sinon arrêt. | `VAST=/home/user/outil-vastai-v1/bin/vastai bash scripts/lancer_iib_v2.sh outil` → code 0, « OUTIL DE LOCATION VÉRIFIÉ … 1.8.3 … » ; sinon arrêt. **Plus : l'exécutante relève la sortie de l'aide de `destroy instance` de l'outil et y vérifie l'option `-y` ; absente → arrêt, message à la mère.** |
| étape 1, extraction du code | `--branch prep/iib-code-v4` ; `checkout --detach 836c7ccc…` | branche et commit de lancement neufs |
| étape 1, variables communes | `ENVI=(env -i PATH="$PATH" HOME="$HOME" …` | `ENVI=(env -i PATH="$PATH" HOME="$HOME" VAST=/home/user/outil-vastai-v1/bin/vastai IIB_INSTANCES_INTOUCHABLES=<les identifiants des machines des autres chantiers, relevés à l'inventaire de l'étape 1> …`. `IIB_DESTRUCTION_RELECTURES`, `IIB_DESTRUCTION_ATTENTE_S` et `IIB_DESTRUCTION_ETATS_ARRET` ne sont pas dans `ENVI` : les valeurs par défaut s'appliquent (6, 10 secondes, `exited stopped`), à écrire dans l'ordre. `RAPATRIEMENT_VERIFIE` n'y est pas non plus : il ne se pose qu'à l'étape 6. |
| étapes 1 à 3 | `"${ENVI[@]}" bash scripts/lancer_iib_v1.sh …` | `"${ENVI[@]}" bash scripts/lancer_iib_v2.sh …` (mêmes sous-commandes et arguments) |
| étape 2, commande imprimée | `GO_ID=… timeout -k 10 300 vastai create instance … > "…/creation-brute.json" 2>&1; bash …/scripts/lancer_iib_v1.sh apres-creation "…/creation-brute.json" $? "…"` | `GO_ID=… timeout -k 10 300 /home/user/outil-vastai-v1/bin/vastai create instance … > "…/creation-brute-essai<n>.json" 2>&1 </dev/null; VAST=/home/user/outil-vastai-v1/bin/vastai bash …/scripts/lancer_iib_v2.sh apres-creation "…/creation-brute-essai<n>.json" $? "…"` |
| étape 2, code 4 | « Code 4 : inventaire, aucune seconde création avant. » | ajouter : aucun identifiant n'est consigné ; la réponse est conservée, masquée, dans `traces-location/creation-brute-<date>.json` ; le code 4 vient aussi d'une réponse qui n'est pas du JSON ou qui porte plusieurs valeurs candidates ; l'écart de forme de R-3687 n'a plus lieu d'être |
| étapes 4 et 5, arrêt | `timeout -k 5 120 vastai stop instance <ID>` | `timeout -k 5 120 /home/user/outil-vastai-v1/bin/vastai stop instance <ID>` (imprimée par la surveillance) |
| étape 6 | `timeout -k 5 120 vastai destroy instance <ID>` … « Puis un seul `show instance <ID> --raw` (texte `{"instances": null}` ou code) et l'inventaire en champs filtrés. » | `"${ENVI[@]}" RAPATRIEMENT_VERIFIE=oui bash scripts/lancer_iib_v2.sh destruction <ID> "$W/iib-rejeu"`. **Les bornes de l'étape 6 restent écrites** : après le rapatriement vérifié (étape 5 sans écart, ou mot de la mère), au plus tard 48 heures après la fin, avant 2026-11-28T00:00:00Z, les deux rappels de la mère. `RAPATRIEMENT_VERIFIE=oui` ne se pose qu'alors. **Sort des codes** : 0, « DÉTRUITE », fin ; 6, instance encore là, elle coûte : message à la mère, aucune seconde commande sans son mot ; 7, instance absente de l'inventaire d'avant : ce n'est pas une preuve, message à la mère, inventaire en champs filtrés par l'exécutante ; 4, incertain : message à la mère, à relire ; 2, refus d'une garde : lire le message, ne rien forcer. |
| § 7, sorties et versement | — | `traces-location/` et `destruction.txt` versés **seulement après la garde des secrets** ; les inventaires n'y sont que sous la forme des champs filtrés de l'instance du saboteur ; tout fichier `….NON-MASQUE` et tout fichier de travail du dossier de session restent hors du versement |
| § 11 et configuration | 34 fichiers | 37 fichiers : pièce décisive, voir le premier alinéa de ce § |

Rien ne change dans l'amorce ni dans le nombre d'essais attendu dans l'instance (456), tant que la liste des essais ciblés reste la version 1 (point à trancher 6).
