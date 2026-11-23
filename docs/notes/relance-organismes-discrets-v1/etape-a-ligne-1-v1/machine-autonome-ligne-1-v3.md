# Ligne 1 de carte du bras A : machine autonome, sans SSH, version 3

- **Date (UTC)** : 2026-11-23. Rédacteur : Claude Opus 5.5, agent délégué par la session du bras A. Processeur seul : aucune dépense, aucune instance, aucune clé lue, aucun réseau hors git. Aucune commande de création n'a été jouée. La branche d'entrée n'est ni construite ni poussée : la session mère le fait au commit final.
- **Objet** : les corrections de la contre-lecture de la v2 (`contre-lecture-machine-autonome-ligne-1-v2.md`, `fe84a889…`, verdict « à corriger »). Les notes v1 et v2 et leurs pièces restent telles quelles (R12) ; tout ce qui n'est pas dit ici reste valable (`machine-autonome-ligne-1-v2.md`).
- **Versions** : amorce d'appel **v2**, amorce complète **v3**, construction **v3**, lanceur **v3**, essais **v3**, note **v3**. Toutes changent sur le fond.

## Pièces

| pièce | chemin | sha256 |
|---|---|---|
| amorce d'appel (onstart, < 2 500 octets, sans commentaire) | `scripts/amorce_appel_ligne_1_bras_a_v2.sh` | compagnon `.sha256` |
| amorce complète, portée par la branche d'entrée | `scripts/amorce_ligne_1_bras_a_v3.sh` | compagnon `.sha256` |
| construction de la branche d'entrée (58 fichiers) | `scripts/construire_branche_entree_ligne_1_bras_a_v3.py` | compagnon `.sha256` |
| lanceur de la session | `scripts/lanceur_machine_ligne_1_bras_a_v3.py` | compagnon `.sha256` |
| essais | `tests/test_amorce_ligne_1_bras_a_v3.py` | compagnon `.sha256` |

## 1. Amorce d'appel v2 : ce que fait chaque ligne (les commentaires vivent ici, pas dans le fichier)

Le fichier fait 2 484 octets : la limite d'environ 4 Ko du champ onstart laisse une marge. Dans l'ordre :
1. `[ -n "${BASH_VERSION:-}" ] || exec bash "$0" "$@"` : jouée par `sh` (dash), elle se reprend par bash (M1).
2. `set +x; set -u`. `APPEL_DEBUT_S` (heure de départ, transmise), `CLONE_FAIT=1` et `GIT_TERMINAL_PROMPT=0` sont exportés.
3. Une variable de jouet (`RACINE_AMORCE`, `AMORCE_DEPOT_URL`, `AMORCE_CURL`) hors du mode jouet est un arrêt.
4. La fonction `p` demande l'arrêt de l'instance : `PUT {"state": "stopped"}`, clé passée à `curl -K -` par l'entrée standard, sous `timeout 90`. **Si `curl` manque**, la demande passe par `python3 -I` (bibliothèque standard, `urllib`), avec l'adresse et la clé lues dans l'environnement par leur nom (B1).
5. La fonction `s` est l'arrêt de l'appel : elle journalise le motif, puis **redemande l'arrêt en boucle**, avec un délai croissant (1 à 10 fois 60 s, borné à 10 min), tant que le processus vit (M2). Sans identifiant numérique, aucun arrêt ne peut partir : elle sort (code 2). Jamais de destruction : rien n'est encore produit.
6. Si `git` ou `curl` manque : `apt-get update` puis `apt-get install -y git curl ca-certificates`, sans affichage (B1). Si `git` manque encore, c'est un arrêt.
7. Les cinq variables attendues sont exigées, et `CONTAINER_ID` doit être numérique.
8. Clone : `timeout 900 git -c credential.helper= -c credential.helper="$A" clone --depth 1 --no-checkout --branch <entrée>`. Le `--depth` implique une seule branche. L'aide est d'abord remise à vide, puis l'aide d'identification est donnée (m3). Ensuite la configuration du clone reçoit une aide vide puis l'aide d'identification, **puis** vient l'extraction (R-5101). Si le clone existe déjà, après un redémarrage, il n'est pas refait.
9. Le commit cloné doit être égal à `COMMIT_ENTREE`, puis l'amorce complète doit avoir l'empreinte `AMORCE_SHA256`. Enfin `exec bash` sur l'amorce complète.

## 2. Amorce complète v3 : les corrections

- **B1** : sans `curl`, les demandes au loueur (`PUT`, `DELETE`) passent par `python3` (bibliothèque standard). Un outil absent (`git`, `python3`, `sha256sum`, `timeout`, `setsid`…) ne termine plus le processus sans rien demander : c'est un **arrêt demandé**. Il ne reste aucune sortie de l'amorce complète sans demande d'arrêt ou de destruction, sauf deux cas : les refus d'arguments de jouet, avant tout, et l'identifiant illisible, où rien ne peut partir et la mère détruit.
- **M2** : `arreter` redemande l'arrêt en boucle, avec un délai croissant borné à 10 min, et relit l'état de l'instance par `GET` à chaque essai. Seuls `intended_status` et `actual_status` sont écrits, parce que la fiche porte les variables `-e`.
- **M3** : le secours passe à **25 min** après l'heure du plafond. `timeout` est mis sur chaque git réseau (clone 900 s, push 900 s, `ls-remote` 300 s) et sur chaque appel au loueur (90 s).
- **m2** : l'installation des paquets tourne sous `env -u GH_TOKEN -u HF_TOKEN -u CONTAINER_API_KEY`. Le téléchargement du modèle ne garde que `HF_TOKEN`, et la course aucun des trois.
- **m3** : `credential.helper` est remis à vide avant l'aide, au clone et dans les configurations du clone d'entrée et du dépôt de sortie. `GIT_TERMINAL_PROMPT=0` partout.
- **m4** : les étapes longues sont lancées par `setsid` (le PID est le numéro du groupe). La coupe envoie TERM puis KILL **au groupe** (`kill -- -PGID`). Les `bash -c` finissent par `exec`.
- **m5** : à la reprise, les états `fin`, `secours`, `destruction-demandee` et `arret-demande` d'un départ précédent sont effacés. Le secours est ainsi réarmé.
- **m10** : avant le scellement, tout fichier du versement de plus de 100 Mo est déplacé sous `hors-versement/` sur le disque de la machine, non poussé. Le manifeste le dit dans `manquants` (« plus de 100 Mo : non poussé, gardé sur le disque de la machine »).
- **m1, écart déclaré** : il n'y a pas de `set -e`. L'appel a `set -u`, l'amorce complète `set -uo pipefail`. Chaque commande qui compte est testée à la main, et chaque échec mène à un versement d'échec, un arrêt ou une destruction après preuve. Un `set -e` interromprait les chemins de repli (versement après un échec), d'où ce choix.

## 3. Construction v3 et lanceur v3

- **Construction** : elle porte l'amorce complète v3 (58 fichiers). Elle fait un `git fetch origin main` juste avant de prendre les quatre fichiers du guide à `origin/main` (m7) ; un fetch en échec est un refus. L'option `--sans-fetch` sert aux essais hors réseau.
- **Lanceur `creation`** : la commande imprimée porte `${GH_TOKEN:?}` et `${HF_TOKEN:?}` (m8) : un secret vide fait échouer la commande chez la mère, au lieu d'une machine qui démarre pour rien. Elle passe `--onstart scripts/amorce_appel_ligne_1_bras_a_v2.sh`, et `AMORCE_SHA256` est l'empreinte de l'amorce complète v3. La sortie de la commande de création est envoyée dans la sous-commande neuve `masquer` (`… 2>&1 | PYTHONPATH=src .venv/bin/python scripts/lanceur_machine_ligne_1_bras_a_v3.py masquer`).
- **m9** : les docstrings sont à jour.

## 4. « Nœud pour la mère » : le canal

La machine ne peut pas prévenir la mère quand la poussée échoue : le journal qui le dit reste sur le disque de la machine arrêtée. **La session mère (pas la machine) lit `etat` toutes les 15 minutes** pendant la vie de l'instance, et lit aussi `git ls-remote origin refs/heads/calcul/bras-a-ligne-1-v1`.
- Instance **arrêtée sans branche de sortie** : nœud pour la mère. Elle peut redémarrer l'instance (l'appel puis l'amorce reprennent sans rien relancer, repoussent, prouvent, puis **détruisent**), ou la détruire par l'identifiant après décision.
- Instance encore **en marche** après l'heure du plafond plus 25 min, sans versement prouvé : la mère la détruit par l'identifiant (R10).
- Au plus tard à l'échéance plus 30 min, une lecture de `etat` est faite quoi qu'il arrive.

## 5. Essais v3 (`tests/test_amorce_ligne_1_bras_a_v3.py`) : 41 passent, 1 sauté (le rejeu long)

Ils reprennent ceux de la v2 et en ajoutent six. Premier passage, sans l'essai de construction sur le vrai dépôt : 40 passent, 1 sauté. Cet essai-là n'est joué qu'une fois l'amorce v3 committée : il a été rejoué après le commit et passe (58 fichiers).
- **Reprise sous `sh`** : l'amorce d'appel jouée par dash se reprend par bash, puis arrête sur la variable absente.
- **Premier arrêt en échec (HTTP 500)** : l'appel redemande l'arrêt, et l'amorce complète aussi (poussée refusée), avec relecture de l'état et sans destruction.
- **Fichier trop gros** (seuil abaissé en jouet) : il reste sur le disque, le manifeste le dit, l'inventaire ne le porte pas.
- **Masquage** de la sortie de la commande de création.
- **Constantes de la v3** : secours à 25 min, `setsid`, `timeout`, aide vide, environnement sans secrets à l'installation, reprise par bash, `apt-get`, repli par python.
- Aucun secret dans les journaux, dans chaque scénario, comme en v2.
- **Non éprouvé ici** : l'installation par `apt-get` et le repli par `python3` vers l'adresse réelle du loueur (il faudrait du réseau ou un loueur simulé à cette adresse) ; le secours de 25 min (fil principal bloqué) ; le contenu réel de l'image ; la manière dont Vast joue l'onstart ; les droits réels de `CONTAINER_API_KEY`.

## 6. Ce qui reste à la session mère

1. Une contre-lecture courte de l'écart v2 → v3.
2. Construction et poussée de la branche d'entrée au commit final (`construire_branche_entree_ligne_1_bras_a_v3.py --pousser`, avec le fetch), puis `lanceur_machine_ligne_1_bras_a_v3.py creation --offre … --commit-entree …`. La création doit tomber **le 23 novembre UTC**, sinon il faut un nouveau constat et une nouvelle branche d'entrée.
3. La lecture de `etat` toutes les 15 minutes (section 4).
