# Corrections « CUDA de l'hôte » de l'étape B bis de T0.7, v1 — garde d'offre et contrôle d'amorce

**Déclaration** : rédigé sans vue des données de 7a, 7b, T0.7 ou P3-bis ; rien lu ni écrit sous `diag/`, `donnees/`,
`docs/verdicts/` ; aucun appel au service de location (aucune recherche réelle, aucune location, aucune dépense) ; aucune
machine ; `MIN_ESSAIS` (87), le code de mesure et les seuils de la course inchangés ; version de torch et `requirements-gpu.txt`
inchangés.

- **Date (UTC)** : 2026-11-15, vers 07:45.
- **Branche** : `prep/t07bbis-code-v1`, partie de `0f3d929b` ; code et ce rapport dans le commit suivant.
- **Fait nouveau** : répétition sur carte du 15 novembre, arrêt « ARRET : torch ne voit pas la carte » (code 2) après 118 s
  d'installation. Traces sur `calcul/t07bbis-repetition-v1` (`56f5b8b8`), `traces/bbis-t07-repetition-v1/` :
  `journal-repetition.txt`, `nvidia-smi.txt` (« NVIDIA A100-SXM4-80GB, 81920 MiB, 570.211.01 »), `pip-verbeux.txt`, lues par
  `git show`. Cause : le pilote 570.211.01 ne sert que CUDA 12.8, alors que la roue torch 2.14.1 de `requirements-gpu.txt` est
  construite pour CUDA 13.0 (le fichier le dit déjà, lignes 3 à 6). **Trou** : aucune garde d'offre de B bis (ni celle de la
  répétition, ni celle de la course) n'exigeait un hôte capable de CUDA 13.0.

## 1. Le champ de l'outil

`cuda_max_good` : version CUDA maximale servie par l'hôte dans la sortie de `vastai search offers --raw`. Vérifié sans appel :
(i) outil installé (`/home/user/vastai-env`, vastai 1.8.3) : `vastai/api/query.py` l. 117 (champ de recherche) et l. 169
(alias `cuda_vers` → `cuda_max_good`), `vastai/cli/display.py` l. 61 (colonne « CUDA »),
`vastai/cli/self_test/machine_diagnostics.py` l. 170 (lu sur l'offre) ; (ii) précédent du dépôt : garde R-1686 de T0.6
(`src/controle_ia/t06/session_v7.py`, `CUDA_MAX_GOOD_MIN = 13.0` et filtre `cuda_max_good>=13.0` ; `session_v8.py` l. 145 à 153,
même cause : « driver too old »). Aucune recherche réelle n'a été faite pour le confirmer aujourd'hui (voir § 4).

## 2. Changements, fichier par fichier

| fichier | différentiel résumé |
|---|---|
| `src/controle_ia/t07bbis/registre_bbis_v1.py` | `CUDA_MAX_GOOD_MIN = 13.0` ; `faute_cuda_hote(valeur)` : nombre JSON seulement (ni booléen ni texte), fini, au moins 13.0, sinon motif de refus ; `exiger_offre` (course) l'applique à la clé `cuda_max_good` de OFFRE.json ; clé absente → refus ; docstring et `__all__` à jour ; `import math`. |
| `scripts/repetition_carte_bbis_v1.py` | importe `CUDA_MAX_GOOD_MIN` et `faute_cuda_hote` du registre (une seule garde pour les deux) ; `offre_depuis_recherche` lit `cuda_max_good` sur l'offre de l'outil, refuse sous 13.0 ou si absente/illisible (aucun OFFRE.json écrit), et le recopie dans OFFRE.json ; `exiger_offre` (sous-commande `offre`) l'exige à son tour ; message « OFFRE ECRITE » porte « CUDA de l'hôte ». |
| `scripts/lancer_repetition_bbis_v1.sh` | commentaire d'usage seulement : commande de recherche écrite avec `cuda_max_good>=13.0` ; borne CUDA dans la description de `offre`. |
| `scripts/lancer_bbis_v1.sh` | commentaire d'usage seulement : borne `cuda_max_good` ≥ 13.0 de `offre` (clé recopiée telle quelle de la recherche) et commande de recherche avec le filtre. |
| `scripts/amorce_repetition_bbis_v1.sh` | bloc marqué `cuda-du-pilote` (`cuda_du_pilote`, `exiger_cuda_du_pilote`) ; `verifier_machine` capture l'en-tête de `nvidia-smi` (sans argument) dans `$X/nvidia-smi-entete.txt` ; appel `exiger_cuda_du_pilote` **après `preparer_depot` et avant `python3 -m venv` et l'installation** ; en-tête du fichier à jour. |
| `scripts/amorce_bbis_v1.sh` | même bloc `cuda-du-pilote`, texte identique (vérifié par essai) ; à l'étape 1 (machine), capture de l'en-tête et appel **avant le clonage, la sortie de 7b et l'installation** ; en-tête du fichier à jour. |
| `tests/test_t07bbis_registre_v1.py` | gabarits d'offre complétés de `cuda_max_good: 13.0` ; nouvel essai `test_garde_d_offre_cuda_servie_par_l_hote`. |
| `tests/test_t07bbis_chaine_instance_v1.py` | gabarit d'offre complété de `cuda_max_good: 13.0` (seul changement). |
| `tests/test_repetition_bbis_v1.py` | gabarits d'offre et `OFFRES` complétés ; faux `nvidia-smi` imprime un en-tête « CUDA Version: 13.0 » quand il est appelé sans argument, et l'essai de la machine vérifie la capture ; deux essais neufs (§ 3). |

Contrôle de l'amorce : lit « CUDA Version: M.m » dans l'en-tête de `nvidia-smi`, **une fois exactement**, forme `M.m` en chiffres ;
majeur < 13 → `arret "pilote trop ancien : CUDA 12.8 servie par le pilote < 13.0 … ; arrêt avant l'installation des paquets" 2` ;
absente, multiple, illisible, fichier vide ou absent → `arret "version CUDA servie par le pilote illisible … " 2`. Code 2, celui de
« torch ne voit pas la carte » (inchangé, toujours en place après l'installation). Rien n'est deviné depuis le numéro du pilote.

Commande de recherche (texte d'usage ; le filtre de l'outil est une aide, la garde locale décide) :
- répétition : `( umask 077; vastai search offers 'gpu_name=A100_SXM4 num_gpus=1 cpu_cores_effective>=16 cpu_ram>=128 disk_space>=60 reliability>0.98 cuda_max_good>=13.0' -o 'dph_total' --raw > RECHERCHE.json )` ;
- course : même forme, `disk_space>=150`, sans `reliability` (aucun filtre de fiabilité n'était écrit pour la course ; je n'en ajoute pas).

Cette commande **remplace**, pour la mère, celle du § 2 de `rapport-developpeur-repetition-carte-v2.md` (non réécrit, R12).

## 3. Essais (R5 : cas sain et artefact pour chaque garde)

- `test_garde_d_offre_cuda_servie_par_l_hote` (course) : 13.0 (borne incluse), 13.2 et 13 acceptés ; 12.8, 12.99, `None`, `"13.0"`
  (texte), `True`, NaN, infini, clé absente refusés ; sous-commande `offre` de `lancer_bbis_v1.sh` : saine → 0 ; 12.8 et clé
  absente → 2 ; filtre `cuda_max_good>=13.0` présent dans le texte d'usage.
- `test_offre_de_la_repetition_exige_cuda_13_de_l_hote` : `offre-depuis-recherche` à 13.0 → OFFRE.json écrit avec
  `cuda_max_good: 13.0`, puis `offre` → 0 ; 12.8, `"13.0"`, `null`, clé absente → 2 et aucun fichier écrit ; `offre` à 12.8, NaN,
  clé absente → 2 ; filtre présent dans le texte d'usage.
- `test_cuda_du_pilote_avant_l_installation_dans_les_deux_amorces` : bloc identique dans les deux amorces ; en-têtes sains 13.0,
  13.2, 14.1 → accepté ; en-tête de l'hôte des traces (pilote 570.211.01, « CUDA Version: 12.8 », reconstitué : les traces ne
  gardent que la ligne `--query-gpu`) → code 2, « pilote trop ancien : CUDA 12.8 » ; sortie `nvidia-smi.txt` des traces telle
  quelle (sans « CUDA Version ») → code 2, illisible ; en-tête double, vide, « 13.x », « 13 » sans mineur, fichier absent → code 2 ;
  ordre vérifié dans le texte (une seule occurrence de l'appel ; répétition : capture dans `verifier_machine`, puis
  `preparer_depot`, puis l'appel, puis `installer_paquets` ; course : capture, appel, puis clonage, `pip install`, contrôle torch).
- Mutations jouées à la main sur une copie jetable (non gardées) : seuil 12.0, clé absente tolérée, seuil de l'amorce de
  répétition à 12, contrôle de l'amorce de la course qui tolère l'illisible, appel retiré de l'amorce de la course : chacune fait
  échouer au moins un des essais neufs.

**Compte** (`PYTHONPATH=src python -m pytest -q -p no:cacheprovider tests/test_t07bbis_*.py tests/test_repetition_bbis_v1.py`) :
avant les ajouts, au commit `0f3d929b` avec le code corrigé mais les anciens gabarits : 5 échecs, 127 passés (132, comme attendu ;
les 5 échecs sont les gabarits d'offre sans `cuda_max_good`, refusés par la garde neuve, ce qui est voulu) ; après :
**135 passed, 4 warnings in 176.84s**. `tests/test_repetition_bbis_v1.py` rejoué seul après la dernière retouche (commentaire de
l'en-tête de l'amorce de répétition) : 25 passed. `MIN_ESSAIS` reste 87 (la course compte `tests/test_t07bbis_*.py` : un essai de
plus, au-dessus du minimum).

## 4. Points choisis, et ce qui reste non éprouvé

1. **Place du contrôle dans la répétition** : après le dépôt (quelques secondes de clonage partiel) et non à l'étape 1, pour que
   l'arrêt pousse ses traces (`SORTIE_LIBRE=1` posé par `preparer_depot`) ; toujours avant la création de l'environnement et
   l'installation. Dans la course, à l'étape 1 : les traces n'y partent qu'après l'étape 7 par construction, et les étapes 2 et 3
   (clonage, sortie de 7b) sont plus longues ; un arrêt à l'étape 1 n'y pousse donc aucune trace (comme « carte invisible »
   aujourd'hui) : la mère ne l'apprend que par le journal de l'instance.
2. **Forme stricte** de `cuda_max_good` : nombre JSON seulement ; un texte « 13.0 » est refusé (la T0.6 acceptait `float(texte)`).
   L'outil rend un nombre (T0.6, offres réelles à 13.2).
3. **Lecture par l'en-tête** de `nvidia-smi` plutôt que par le numéro du pilote : aucun tableau pilote → CUDA à tenir.
4. La course n'a pas de sous-commande `offre-depuis-recherche` : OFFRE.json de la course reste écrit par la mère, qui doit y
   recopier `cuda_max_good` tel quel ; je n'ai pas ajouté de construction par programme (correction minimale). À voir si la mère
   la veut.
5. **Non éprouvé** : forme réelle de l'en-tête de `nvidia-smi` sur un pilote 580 (texte reconstitué, conforme à la forme connue
   « … Driver Version: … CUDA Version: 13.0 … ») ; présence réelle de `cuda_max_good` dans une recherche du jour (non appelée) ;
   le filtre `cuda_max_good>=13.0` accepté par l'outil 1.11.0 de la mère (la T0.6 l'a employé) ; aucune passe sur carte.
6. **Fiche de `CODE-BBIS`** : pas encore écrite au registre propre ; `amorce_bbis_v1.sh`, `lancer_bbis_v1.sh` et
   `registre_bbis_v1.py` figurent dans `fichiers-fiche-code-bbis-v1.txt` : leurs empreintes changent, la fiche doit être écrite
   sur le nouveau commit. La commande de la répétition compare l'amorce du dossier à celle du commit : la passer avec le commit
   qui porte cette correction.
