# Rapport du développeur — trois défauts de forme des programmes de lancement de la course du saboteur à budget (version 1)

Date : 2026-11-19. Pièce d'instrument (classe B), à contre-lire par un autre modèle. Rien poussé, rien dépensé, aucun appel au loueur de machines.

- Arbre de travail : `/tmp/claude-0/-home-user-controle-ia-travail/43943324-c96f-5191-9f95-633db6e7fd97/scratchpad/developpeur-forme/arbre`
- Branche : `prep/iib-code-v5`, partie de `origin/prep/iib-code-v4` (commit de lancement `836c7ccc`).
- Commit : `e2c90f97` (un seul ; `git log --oneline origin/prep/iib-code-v4..HEAD`).
- Lu dans l'arbre principal : `CLAUDE.md`, les trois lignes R-3683, R-3687 et R-3722 de `registres/decisions.md`, et les sections 5 et 6 de l'ordre scellé. Aucun chemin interdit n'a été ouvert.

## 1. Fichiers créés (aucun fichier existant n'est modifié)

| Fichier | Empreinte | Rôle |
|---|---|---|
| `scripts/lancer_iib_v2.sh` | `cc0518ae08fac1bd705a17afe4af621b254908dffe6fbcc0f52591affe1473be` | lanceur de session, version 2 (copie de la version 1, plus les trois corrections) |
| `tests/test_iib_lanceur_forme_v2.py` | `f65f67a8f31cb1cf5107b958d48cdd95fb9b0c03445df9ff2efca8dc895d0d5d` | essais à blanc, faux outil de location écrit dans le fichier |

Choix de forme (R12) : `scripts/lancer_iib_v1.sh` n'a pas de compagnon `.sha256`, mais son empreinte (`3279e3dc…ece8f`) est citée par l'ordre scellé et par la configuration de la course. Je ne l'ai donc pas réécrit : la version 2 est un fichier neuf, la version 1 est intacte (un essai le vérifie par son empreinte). L'amorce de l'instance (`scripts/amorce_instance_iib_v1.sh`) et `src/controle_ia/iib/session_v1.py` ne sont pas touchés : aucun des trois défauts ne s'y trouve (l'amorce se détruit par l'interface du loueur, sans l'outil en ligne de commande).

## 2. Ce que fait chaque correction

### Défaut 1 — chemin de l'outil de location (R-3683)
- La version 1 lisait déjà une variable `VAST`, mais ne faisait que `command -v`, ne disait rien, et la commande imprimée appelait `apres-creation` sans la transmettre.
- Version 2, fonction `resoudre_outil` : avec `VAST`, le chemin doit contenir un `/`, être un fichier, être exécutable, et `--version` doit rendre le code 0 et un texte ; il est rendu absolu. Sinon refus, code 2, avec la raison (« n'existe pas », « n'est pas exécutable », « ne rend pas sa version », « n'est pas un chemin »).
- Sans `VAST` : recherche de `vastai` dans le PATH, refus s'il est introuvable, comme la version 1. La version est demandée et consignée ; si elle n'est pas rendue, le lanceur écrit « non rendue » et continue (comportement de la version 1 gardé).
- Le lanceur dit lequel il emploie : sur la sortie (« outil de location employé : chemin (version ; trouvé par) »), dans `lancement.txt` (lignes `outil_location`, `outil_location_version`), dans `surveillance.txt` et dans `destruction.txt`.
- Le chemin absolu est écrit dans toutes les commandes imprimées : création, appel de `apres-creation` (`VAST=<chemin> bash …/lancer_iib_v2.sh apres-creation …`), rang suivant, arrêt.
- Sous-commande neuve `outil` : vérifie l'outil, ne crée rien (peut remplacer le `vastai --version` de l'étape 1 de l'ordre).
- Écart à signaler : un chemin qui porte un caractère hors de `[A-Za-z0-9_./+-]` (une espace, par exemple) est refusé dans les deux cas, parce qu'il casserait la commande imprimée. La version 1 l'aurait imprimé tel quel.

### Défaut 2 — réponse brute du loueur effacée (R-3687)
- La ligne `rm -f -- "$F"` est retirée. `apres-creation` conserve la réponse avant toute lecture et tout verdict, dans les trois issues (créée, offre refusée, création incertaine).
- Copie datée : `DOSSIER/traces-location/creation-brute-<AAAAMMJJTHHMMSSZ>.json`, avec son compagnon `.sha256` ; jamais d'écrasement (suffixe `-1`, `-2` si le nom existe). La ligne `reponse_creation <chemin> <empreinte> masques=<n>` va dans `lancement.txt`.
- Masquage par programme avant conservation, et le lanceur le dit avec le nombre de remplacements : valeurs des clés de l'environnement (`HF_TOKEN`, `GH_TOKEN`, les deux jetons GitHub, `VAST_API_KEY`, `CONTAINER_API_KEY`) ; motifs de jeton (`hf_…`, `ghp_…`, `github_pat_…`) ; `Bearer …` ; champs JSON et affectations dont le nom porte clé, jeton, secret ou mot de passe.
- Le fichier d'origine est remplacé par sa forme masquée (seuls les secrets en sont retirés). Si le masquage échoue, il est laissé tel quel et le lanceur écrit « NON MASQUÉ : ne pas le verser avant la garde des secrets ».
- Le lanceur imprime aussi les champs `success`, `new_contract`, `error`, `msg`, tronqués à 300 caractères et masqués (ce que l'exécutante a fait à la main le 19 novembre).
- Étendu aux autres sorties de la location : inventaires, liste des offres et sortie de la destruction sont versés au même dossier, avec empreinte. Une sortie dont le masquage échoue est gardée sous un nom daté au lieu d'être supprimée (la version 1 faisait `rm -f` sur ces fichiers temporaires).
- Seul `rm` restant : les deux fichiers de tâches des contrôles (`reserve.json`, `evaluation.json`), qui ne sont pas des sorties de la location ; inchangé.

### Défaut 3 — destruction sans option de confirmation (R-3722)
- La version 1 n'avait pas de commande de destruction : l'ordre la donnait à la main. Sous-commande neuve : `destruction ID DOSSIER`.
- Refus avant tout appel (code 2) : identifiant qui n'est pas fait de chiffres seuls (étiquette, motif), identifiant différent de la ligne `instance` de `lancement.txt` (R10), outil introuvable.
- Inventaire d'avant : illisible → aucune destruction, code 4 ; identifiant déjà absent → aucune commande envoyée, code 0, dit.
- Commande : `timeout -k 5 120 <outil> destroy instance <ID> -y`, entrée standard fermée, une seule fois, jamais de second essai.
- Preuve : l'inventaire est relu (6 fois au plus, 10 secondes d'écart ; réglable par `IIB_DESTRUCTION_RELECTURES` et `IIB_DESTRUCTION_ATTENTE_S`).
- Codes : 0, commande au code 0 et identifiant absent ; 6, identifiant encore à l'inventaire (le message distingue commande réussie et commande en échec) ; 4, inventaire illisible après, ou commande en échec alors que l'identifiant est absent. Aucun repli : ni arrêt, ni seconde commande.
- Journal : `destruction.txt`, et `destruction_verifiee` dans `lancement.txt` seulement au code 0.

## 3. Ce que chaque essai prouve (`tests/test_iib_lanceur_forme_v2.py`, 57 essais)

Le faux outil de location rend une version, une réponse de création choisie par l'essai, un inventaire, et **exige `-y`** pour détruire : sans l'option il demande une confirmation sur l'entrée standard et échoue.

| Essai | Cas | Ce qu'il prouve |
|---|---|---|
| `test_la_v1_citee_par_l_ordre_scelle_est_intacte` | sain | l'empreinte de la version 1 est celle de l'ordre scellé |
| `test_outil_sain_chemin_explicite_hors_du_path` | sain | outil hors du PATH accepté par `VAST`, chemin et version dits, seuls appels : `--version` |
| `test_outil_sain_chemin_relatif_rendu_absolu` | sain | un lien est résolu en chemin absolu |
| `test_outil_artefacts_refus_clair` (6 cas) | artefact | absent, non exécutable, muet sur sa version, nom nu, dossier, chemin à espace : code 2 et raison, pour `outil`, `destruction` et `surveillance` ; aucun appel au-delà de `--version` |
| `test_outil_sans_variable_recherche_dans_le_path_comme_la_v1` | les deux | sans variable : refus si absent du PATH ; trouvé dans le PATH ; version non rendue acceptée et dite |
| `test_surveillance_dit_l_outil_dans_son_journal_et_imprime_son_chemin` | sain | `surveillance.txt` nomme l'outil ; la commande d'arrêt porte le chemin absolu et l'identifiant |
| `test_creation_de_bout_en_bout_avec_un_outil_hors_du_path` | les deux | sans variable ni outil dans le PATH : refus, aucune commande imprimée ; avec `VAST` : la commande imprimée porte le chemin absolu deux fois, passe la garde de calcul, et, exécutée telle quelle sans `VAST` dans l'environnement, rend « CRÉÉE », réponse conservée et jetons masqués |
| `test_apres_creation_sain_creee_reponse_conservee` | sain | code 0, copie datée identique, empreinte tenue, 0 masque, aucun appel au loueur |
| `test_apres_creation_artefact_reponse_sans_identifiant_lisible_reste_sur_disque` | artefact | le cas du 19 novembre : code 4, réponse sur disque (original et copie), cause lisible (« 402 », « lacks credit »), cinq secrets absents du fichier et de la sortie |
| `test_apres_creation_artefact_code_non_nul_et_identifiant_present_incertain_conserve` | artefact | code 4, réponse conservée |
| `test_apres_creation_offre_refusee_reponse_conservee_et_rang_suivant_en_v2` | sain | code 5, réponse et inventaire conservés, commande du rang suivant en version 2 avec `VAST` |
| `test_apres_creation_deux_reponses_deux_copies_aucune_ecrasee` | artefact | deux réponses, deux copies distinctes |
| `test_apres_creation_artefacts_reponse_absente_et_masquage_en_echec` | artefact | réponse absente : dit, code 4 ; sans `python3` : original intact, « NON MASQUÉ » dit, aucune copie |
| `test_le_programme_ne_supprime_aucune_sortie_de_la_location` | garde de forme | le seul `rm` de la version 2 porte sur les deux fichiers de tâches ; la version 1 portait bien `rm -f -- "$F"` |
| `test_le_faux_outil_exige_la_confirmation` | artefact | sans `-y`, le faux outil échoue sur la confirmation et l'instance reste (défaut du 19 novembre rejoué) |
| `test_destruction_sain_option_y_par_identifiant_et_absence_verifiee` | sain | une seule commande `destroy instance <ID> -y`, encadrée par deux inventaires ; l'autre instance reste ; journal et traces à empreinte tenue |
| `test_destruction_artefacts_echec_dit_sans_repli` (3 cas) | artefact | code 0 sans effet → 6 ; commande en échec → 6 ; échec mais instance retirée → 4 ; jamais « DÉTRUITE », une seule commande, ni arrêt ni création ; clé du loueur masquée dans la sortie gardée |
| `test_destruction_artefact_inventaire_illisible_avant_aucune_destruction` | artefact | code 4, aucune commande de destruction |
| `test_destruction_artefact_inventaire_illisible_apres_incertain` | artefact | code 4, absence « non établie » |
| `test_destruction_instance_deja_absente_aucune_commande` | sain | `{"instances": null}` : code 0, aucune commande |
| `test_destruction_artefacts_jamais_une_autre_instance_ni_un_motif` (4 cas) | artefact | autre identifiant, étiquette, motif, deux identifiants : code 2, aucun appel |
| 25 essais repris de `tests/test_iib_scripts_v1.py` | non-régression | garde de GO, contrôles, création, surveillance : même verdict avec la version 2 qu'avec la version 1 |

Joué à la main en plus (hors suite, dossier `demo/` de mes notes) : une copie de la version 2 privée de `-y` rend « DESTRUCTION EN ÉCHEC », code 6, sur le même faux outil — l'essai sain mord bien sur l'option.

## 4. Sortie brute des essais ciblés

Fichier : `/tmp/claude-0/-home-user-controle-ia-travail/43943324-c96f-5191-9f95-633db6e7fd97/scratchpad/developpeur-forme/sortie-essais-cibles-v1.txt`.

```
$ PYTHONPATH=src python3 -m pytest -q --tb=line -rfE tests/test_iib_scripts_v1.py tests/test_iib_amorce_v1.py tests/test_iib_lanceur_v1.py tests/test_iib_lanceur_forme_v2.py
tests/test_iib_lanceur_v1.py:16: in <module>
    from controle_ia.iib import lanceur_v1 as la
src/controle_ia/iib/lanceur_v1.py:40: in <module>
    import torch
E   ModuleNotFoundError: No module named 'torch'
ERROR tests/test_iib_lanceur_v1.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.26s

$ PYTHONPATH=src python3 -m pytest -q --tb=line -rfE tests/test_iib_scripts_v1.py tests/test_iib_amorce_v1.py tests/test_iib_lanceur_forme_v2.py
E   ModuleNotFoundError: No module named 'torch'   (quatre fois, src/controle_ia/iib/lanceur_v1.py:40)
FAILED tests/test_iib_amorce_v1.py::test_sain_progres_d_un_jeu_jouet_complet_du_lanceur_relaye_par_les_deux_motifs_de_l_amorce
FAILED tests/test_iib_amorce_v1.py::test_sain_progres_d_un_jeu_jouet_arrete_aux_epreuves_relaye_par_les_deux_motifs_de_l_amorce
FAILED tests/test_iib_amorce_v1.py::test_artefact_ancienne_forme_de_la_ligne_des_epreuves_retenue_par_le_relais[jouet0-aucun]
FAILED tests/test_iib_amorce_v1.py::test_artefact_ancienne_forme_de_la_ligne_des_epreuves_retenue_par_le_relais[jouet1-E-O6]
4 failed, 121 passed in 44.72s

$ PYTHONPATH=src python3 -m pytest -q tests/test_iib_lanceur_forme_v2.py
.........................................................                [100%]
57 passed in 20.88s
```

## 5. Ce que je n'ai pas pu éprouver

1. **`tests/test_iib_lanceur_v1.py` n'est pas collecté et quatre essais de `tests/test_iib_amorce_v1.py` échouent** : la bibliothèque `torch` n'est pas installée dans mon conteneur. Ces essais portent sur le lanceur de la course dans l'instance (`src/controle_ia/iib/lanceur_v1.py`) et sur l'amorce, que je n'ai pas touchés. À rejouer sur un poste qui a `torch`.
2. **L'option `-y` de l'outil réel** : je ne l'ai vérifiée sur aucune source. Elle vient de la ligne R-3722 (« écart de forme accepté : option `-y` »). L'outil n'est pas installé dans mon conteneur et tout appel m'était interdit. À vérifier sur le poste de l'exécutante avant emploi : `destroy instance --help` de la version 1.8.3 doit montrer `-y`, et sa place (après l'identifiant, comme je l'ai écrit) doit être acceptée.
3. **La forme réelle des réponses du loueur** : réponse de création du 19 novembre (effacée, jamais lue), sortie de `destroy`, forme de l'inventaire après destruction. Mes essais emploient des formes factices. Le lecteur d'inventaire accepte une liste et `{"instances": liste ou null}` ; toute autre forme est dite illisible (code 4), sans conclusion.
4. **Le masquage** ne couvre que les clés connues de l'environnement et les motifs listés au § 2. Un secret d'une autre forme passerait : la garde des secrets avant tout commit reste nécessaire. À l'inverse, un champ dont le nom porte « key » ou « token » sans être un secret serait masqué (perte d'information possible sur ce seul champ).
5. **Les inventaires versés aux traces** portent tout l'inventaire du compte (les autres machines comprises), comme `instances.json` en version 1. À ne pas verser sans le filtre des champs.
6. **Délai réel entre la destruction et la disparition à l'inventaire** : inconnu ; les 6 relectures à 10 secondes sont un choix à moi.
7. **Non traité** : en surveillance, `journal-dernier.txt` est toujours remplacé à chaque relevé (20 000 lignes par minute ; `journal-instance.txt` en garde une copie). Je n'ai pas daté chaque relevé, pour la place. À trancher si la règle « aucune sortie supprimée » doit s'y appliquer.
8. **Liste des essais joués dans l'instance** (`scripts/tests-cibles-iib-v1.txt`, empreinte en dur dans l'amorce) : je n'y ai pas ajouté le fichier d'essais neuf. Il éprouve le poste de l'exécutante, pas l'instance, et l'ajouter obligerait à une amorce en version nouvelle et à un autre nombre d'essais attendu (456).

## 6. Lignes de l'ordre scellé à changer dans un ordre en version nouvelle

L'ordre `brouillons/ii-b-saboteur-budget-v1/ordre-exploratoire-ii-b-v1.md` est scellé : je ne l'ai pas touché. Si la version 2 du lanceur est retenue, voici les lignes de commande à changer (§ 5), et celles qui en dépendent.

| Lieu | Ancien texte | Nouveau texte |
|---|---|---|
| § 5, consignes permanentes | « Commandes vérifiées contre `scripts/lancer_iib_v1.sh` … (`3279e3dc…ece8f`) » | même phrase pour `scripts/lancer_iib_v2.sh`, avec son empreinte au commit de lancement neuf (à `e2c90f97` : `cc0518ae…73be`) |
| § 5, étape 1, premier point | `vastai --version` → `1.8.3` ; sinon arrêt. | `VAST=/home/user/outil-vastai-v1/bin/vastai bash scripts/lancer_iib_v2.sh outil` → code 0, « OUTIL DE LOCATION VÉRIFIÉ … version : … 1.8.3 … » ; sinon arrêt. (Se joue après l'extraction du code ; l'export du PATH de R-3683 n'est plus nécessaire.) |
| § 5, étape 1, extraction du code | `--branch prep/iib-code-v4` ; `checkout --detach 836c7ccc…` | la branche et le commit de lancement neufs |
| § 5, étape 1, variables communes | `ENVI=(env -i PATH="$PATH" HOME="$HOME" …` | `ENVI=(env -i PATH="$PATH" HOME="$HOME" VAST=/home/user/outil-vastai-v1/bin/vastai …` (le reste inchangé, sauf `IIB_BRANCHE_CODE`) |
| § 5, étapes 1 à 3, toutes les commandes | `"${ENVI[@]}" bash scripts/lancer_iib_v1.sh …` | `"${ENVI[@]}" bash scripts/lancer_iib_v2.sh …` (mêmes sous-commandes, mêmes arguments) |
| § 5, étape 2, forme de la commande imprimée | `GO_ID=… timeout -k 10 300 vastai create instance … > "…/creation-brute.json" 2>&1; bash …/scripts/lancer_iib_v1.sh apres-creation "…/creation-brute.json" $? "…"` | `GO_ID=… timeout -k 10 300 /home/user/outil-vastai-v1/bin/vastai create instance … > "…/creation-brute.json" 2>&1 </dev/null; VAST=/home/user/outil-vastai-v1/bin/vastai bash …/scripts/lancer_iib_v2.sh apres-creation "…/creation-brute.json" $? "…"` |
| § 5, étape 2, code 4 | « Code 4 : inventaire, aucune seconde création avant. » | ajouter : la réponse brute est conservée, masquée, dans `"$W/iib-rejeu"/traces-location/creation-brute-<date>.json` avec son empreinte ; l'écart de forme de R-3687 (commande coupée en deux, copie à la main) n'a plus lieu d'être |
| § 5, étape 4 et étape 5, commande d'arrêt | `timeout -k 5 120 vastai stop instance <ID>` (imprimée par la surveillance) | `timeout -k 5 120 /home/user/outil-vastai-v1/bin/vastai stop instance <ID>` (imprimée par la surveillance, chemin absolu) |
| § 5, étape 6 | `timeout -k 5 120 vastai destroy instance <ID>` … « Puis un seul `show instance <ID> --raw` (texte `{"instances": null}` ou code) et l'inventaire en champs filtrés. » | `"${ENVI[@]}" bash scripts/lancer_iib_v2.sh destruction <ID> "$W/iib-rejeu"` → code 0, « DÉTRUITE : instance <ID> absente de l'inventaire … » ; code 6 ou 4 : message à la mère, aucune seconde commande. Le lanceur passe `destroy instance <ID> -y` et relit lui-même l'inventaire ; l'inventaire en champs filtrés de l'exécutante reste. |
| § 11, bloc « Valeur de `EMPREINTES_CODE_IIB` » (et la clé du même nom de la configuration de la course) | 34 fichiers | ajouter `scripts/lancer_iib_v2.sh` et `tests/test_iib_lanceur_forme_v2.py` avec leurs empreintes au commit de lancement neuf (36 fichiers) ; la configuration est scellée, donc configuration en version nouvelle |
| § 7, sorties et versement | — | ajouter `traces-location/` et `destruction.txt` du dossier de session à ce que l'exécutante verse, après la garde des secrets |

Rien ne change dans l'amorce ni dans le nombre d'essais attendu dans l'instance (456), tant que la liste des essais ciblés reste la version 1.
