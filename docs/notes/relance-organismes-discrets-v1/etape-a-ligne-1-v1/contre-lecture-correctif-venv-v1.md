# Contre-lecture du correctif du venv de la machine autonome de la ligne 1 du bras A, version 1

23 novembre 2026. Contre-lecteur neuf : un sous-agent qui n'a écrit ni la machine ni le correctif. Aucune dépense, aucune
instance, aucun réseau hors git. Chemins cloisonnés non ouverts.

## Verdict

**Bon pour le départ**, sous les réserves mineures R-a à R-e ci-dessous, dont aucune ne bloque : chaque cas qu'elles
visent finit en échec dit et versé, jamais en course fausse ni en repli silencieux.

## Ce qui a été lu et vérifié

- Échec réel (`diag/organismes-discrets-v-a-v2/ligne-1-echec-20261123T042528Z/`) : `installation.txt` porte le message
  du python patché par Debian (« ensurepip is not available … apt install python3.12-venv »), `journal-amorce.txt` dit
  « installation en échec » puis le versement. La cause annoncée (python 3.12 du système sans ensurepip) est celle que
  montrent les fichiers.
- Empreintes recalculées, toutes conformes : différences scellées `3ed84df4f8325385…` ; amorce complète v4
  `7f155ab60bbb945e…` ; amorce d'appel v3 `a8b0967a730de29d…` ; construction de la branche d'entrée v4
  `48b57327797f5878…` ; lanceur v5 `f54c69f88e7c9779…`.
- `diff -u` refait sur les quatre paires : les lignes ajoutées et retirées sont **identiques**, octet pour octet, à
  celles du fichier de différences scellé (100 lignes). Elles ne portent que sur :
  - le choix de l'interpréteur du venv, dans l'ordre annoncé : (a) `/opt/conda/bin/python3` si exécutable et
    `-m venv --help` passe ; (b) `python3` du chemin si `import ensurepip` passe ; (c) `apt-get update` puis
    `apt-get install -y -qq python3-venv python3.X-venv` (X lu sur `python3`, forme contrôlée), ensurepip revérifié,
    puis `python3` ;
  - l'exigence de Python 3.10 ou plus (`verifier_python`), l'interpréteur, `--version` et `sys.version_info` au journal ;
  - le contrôle de torch dans le venv (import, `torch.cuda.is_available()` par `assert`, versions de torch et de CUDA,
    nom de la carte), placé après l'installation des paquets et **avant** le téléchargement du modèle ;
  - les échecs dits et versés (« aucun interpréteur pour le venv », « Python du venv antérieur à 3.10 », « torch
    inutilisable », « apt-get en échec ») ; `choix-python.txt` et `controle-torch.txt` masqués et ajoutés au versement ;
  - deux variables de jouet neuves (`AMORCE_CONDA_PYTHON`, `JOUET_INSTALLATION`) ajoutées à la liste refusée hors jouet ;
    la branche de jouet de l'installation est un `elif` du `if [ "$JOUET" != 1 ]`, donc inatteignable hors jouet ;
  - chemins (`amorce_ligne_1_bras_a_v4.sh`, `amorce_appel_ligne_1_bras_a_v3.sh`, nom du lanceur), branches par défaut
    `entree/bras-a-ligne-1-v2` et `calcul/bras-a-ligne-1-v2` dans la construction et le lanceur ;
  - les en-têtes et la ligne de journal « amorce v4 ».
  Aucune autre différence.
- Secrets : `apt-get` et le contrôle de torch tournent sous `env -u GH_TOKEN -u HF_TOKEN -u CONTAINER_API_KEY`, comme
  l'installation de la v3.
- Amorce d'appel v3 : **2 484 octets**, sous le plafond de 2 500 (marge 16 octets, la même que la v2, seul le nom du
  fichier a changé, à longueur égale).
- `bash -n` passe sur `scripts/amorce_ligne_1_bras_a_v4.sh` et `scripts/amorce_appel_ligne_1_bras_a_v3.sh`.
- Essais : voir la section « Essais » en fin de note.

## Pièges connus sur cette image, examinés

1. **Venv créé par le python de conda, et pip.** Le python de conda embarque ensurepip ; le venv aura donc son pip
   (celui livré avec cet interpréteur). Sans `--system-site-packages`, le torch de l'image n'est pas vu : torch 2.14.1
   est réinstallé depuis PyPI par `requirements-gpu.txt` → `requirements-cpu.txt` (`torch==2.14.1`, roue visant CUDA
   13.0), ce qui est voulu (mêmes versions que sur processeur). Le pilote est déjà exigé à CUDA 13 ou plus avant ce
   point. Une bibliothèque CUDA de l'image qui masquerait celles de la roue (par `LD_LIBRARY_PATH`) serait prise par le
   contrôle de torch avant le téléchargement du modèle : c'est le rôle du contrôle.
2. **apt sans `DEBIAN_FRONTEND`.** Posé sur `apt-get install` (`DEBIAN_FRONTEND=noninteractive`), absent de
   `apt-get update`, qui n'en a pas besoin. Entrée standard sur `/dev/null`, `-y`, bornes de 600 et 900 secondes. Correct.
3. **Ordre `apt-get update` puis `install`.** Bon ordre (les listes d'apt sont d'ordinaire vidées dans ces images). Voir
   R-c pour la sévérité du `&&`.
4. **ensurepip sous Debian.** Sous Debian et Ubuntu, le module `ensurepip` vit dans `python3.X-venv` : le test
   `import ensurepip` discrimine bien les cas (b) et (c), et sa revérification après apt est juste. Sur l'image de
   l'échec (python 3.12, Ubuntu 24.04 vraisemblablement), `python3-venv` tire `python3.12-venv` ; le nom explicite est
   redondant mais sans mal.
5. **Python 3.10 et les versions épinglées.** Voir R-a.

## Réserves (mineures, aucune bloquante)

- **R-a — seuil de version trop bas.** `numpy==2.4.6` et `scipy==1.17.1` exigent Python 3.11 ou plus (à ma
  connaissance, non vérifié sur leurs fiches, hors réseau). Un interpréteur 3.10 passerait `verifier_python` puis
  échouerait à `pip install`, dit « installation des paquets en échec » et versé : pas de danger, diagnostic moins net.
  Correction possible à la prochaine version : exiger 3.11.
- **R-b — cas (a) sans contrôle d'ensurepip.** Le python de conda est retenu sur `-m venv --help` seul, qui ne prouve
  pas ensurepip. Le python de conda l'a d'ordinaire ; sinon le venv échoue, échec dit et versé, mais sans repli vers
  (b) ou (c). Correction possible : ajouter `-c 'import ensurepip'` au critère de (a).
- **R-c — `apt-get update` fatal.** `update && install` : un seul dépôt d'apt injoignable ou mal signé (piège connu des
  images bâties sur celles de NVIDIA, dont la clé du dépôt CUDA a déjà tourné) fait échouer `update` et donc (c), alors
  que l'installation depuis les dépôts d'Ubuntu aurait pu passer. Échec dit et versé, pas de danger. Correction
  possible : `update` non fatal (`;`), l'installation et la revérification d'ensurepip décidant seules.
- **R-d — défauts de branche des amorces restés en v1.** `amorce_appel_ligne_1_bras_a_v3.sh` (ligne 7) et
  `amorce_ligne_1_bras_a_v4.sh` (lignes 101–102) gardent `entree/bras-a-ligne-1-v1` et `calcul/bras-a-ligne-1-v1` comme
  défauts. Sans effet : le lanceur v5 passe toujours `-e BRANCHE_ENTREE=… -e BRANCHE_SORTIE=…` (v2), et l'appel refuse
  déjà une variable obligatoire absente. Si un jour ces défauts servaient, le clone de l'ancienne entrée n'aurait pas
  l'amorce v4 et l'appel échouerait bruyamment. L'étiquette de l'instance reste `bras-a-ligne-1-v1` (simple étiquette).
- **R-e — l'image réelle n'est pas éprouvée.** Déclaré par l'auteur. Le chemin effectivement pris sur
  `pytorch/pytorch:2.14.1-cuda13.0-cudnn9-runtime` ((a) si le conda existe et est lisible depuis l'amorce, sinon (c))
  ne se saura qu'au journal de la prochaine machine ; les trois issues sont couvertes, chacune finit en course ou en
  échec dit et versé.

## Essais

`PYTHONPATH=src python -m pytest -q tests/test_amorce_ligne_1_bras_a_v4.py tests/test_lanceur_machine_ligne_1_bras_a_v5.py`
(`.venv`, Python 3.13.18) : **75 réussis, 1 sauté** (le rejeu entier sur le modèle jouet, essai long, non demandé),
en 270 secondes. Les six essais neufs de la v4 couvrent les cas (a), (b), (c), apt en échec, version trop ancienne et
torch inutilisable, chacun avec de faux programmes ; deux autres couvrent le refus hors jouet des deux variables neuves.
