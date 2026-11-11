# Essai à blanc de l'installation du manifeste du témoin de Bailey, sur processeur — v1

Date : 11 novembre 2026 (UTC). Non scellé. Aucune dépense, aucune instance, aucun modèle téléchargé.

## Pièces
- Versions figées : `docs/notes/reproduction-attaque-publiee-v1/versions-figees-temoin-bailey-v1.json`
  (sha256 `e21bccf6eb99c9255f0069be7af2fe5d729bde9ab05db56811ccef1eddee06f9`, vérifiée), 166 paquets PyPI + 3 dépôts git.
- Code public : clone jetable du clone de référence, au commit `9c1f4b1a721fa3c43d00b8605ee7db4c84a55942`
  (arbre `c7cf686c…`), dans le dossier de travail de session (rien copié dans le dépôt).
- Installation reproduite à partir de `script_amorce` (`src/controle_ia/temoin_bailey/lanceur_v9.py`) : même liste
  `paquet==version` (paquets du champ `git` exclus) + `nom @ git+url@commit`, puis `pip install --no-deps -e
  <clone>/inference_time_experiments`. Python 3.11.18.

## Verdict
Les versions figées s'installent ensemble, sans aucun échec ni conflit. Le code public s'importe en entier, y compris
`Llama3SoftPrompted`, **à une condition près propre au processeur** : `sparsify` (EleutherAI, commit `42c06452`)
appelle `torch.cuda.is_bf16_supported()` à l'import, ce qui échoue sans carte. Sur une instance à carte, rien
d'attendu ; à surveiller si un pilote manque (même appel, même chute).

## Résultats
1. **Résolution complète** (manifeste exact, torch CUDA de PyPI compris, `pip --dry-run --ignore-installed`) :
   réussie, aucun conflit. Noms de distribution des dépôts git : `repe-0.1.4`, `eai-sparsify-1.3.3`,
   `strong_reject-0.0.1` (identiques aux clés du manifeste).
2. **Installation réelle** : les 169 exigences installées, code de sortie 0, aucune version refusée.
   **Aucune version à remplacer.**
3. **Imports** (`HF_HUB_OFFLINE=1`) :
   - sans retouche : `strong_reject.evaluate`, `hydra`, `peft` réussis ; `train_harmful`, `evaluate`,
     `obf_reps.utils`, `obf_reps.models.llama3`, `obf_reps.data` échouent tous sur
     `AssertionError: Torch not compiled with CUDA enabled` (chaîne : `obf_reps/__init__.py` → `obf_reps.metrics`
     → `from sparsify import Sae` → `sparsify/sparse_coder.py:208`, `torch.cuda.is_bf16_supported()` à la
     définition de la classe) ;
   - avec une retouche de diagnostic hors dépôt (`torch.cuda.is_bf16_supported` remplacé par `False` avant l'import,
     dans un `sitecustomize` du dossier de travail) : les huit imports et `Llama3SoftPrompted` réussis.
4. **Essai sauté** `test_essai_manquant_7_import_llama3_soft_prompted` (`tests/test_temoin_bailey_condition6_v3.py`),
   venv du manifeste, `TEMOIN_BAILEY_CLONE` = clone jetable : **encore sauté** sans retouche (sa raison affichée,
   « dépendances du clone absentes (joblib, …) », est désormais inexacte : la cause est l'absence de CUDA) ;
   **passé** avec la retouche. Fichier entier, sans retouche : 87 réussis, 1 sauté.
5. **Gardes de mise en place** (depuis le venv, `instance_v8`) :
   - `garde_depot_public` : passée (commit, arbre, aucun fichier suivi modifié après l'installation éditable) ;
   - `garde_empreintes_publiques` : passée ;
   - `garde_versions` : **tombée sur `torch`** seulement (installé `2.4.1+cpu`, attendu `2.4.1`) — conséquence de
     l'écart déclaré ci-dessous ; avec `torch` porté à `2.4.1+cpu` dans le dictionnaire, passée ;
   - `garde_commits_git` : passée (`repe` 5455d8a3…, `eai-sparsify` 42c06452…, `strong_reject` 7a551d5b…).
6. **Noms introuvables par `importlib.metadata.version`** : aucun. Les 166 noms du manifeste (casse et tirets
   compris : `GitPython`, `PyYAML`, `docstring_parser`, `typing_extensions`, etc.) sont tous trouvés.

## Écarts et réserves
- **torch processeur** : `torch==2.4.1` installé depuis `https://download.pytorch.org/whl/cpu` (version `2.4.1+cpu`) ;
  les paquets `nvidia-*` et `triton==3.0.0` installés quand même aux versions du manifeste (inertes ici).
- `pip` du venv mis à jour en 26.3 avant l'installation ; `script_amorce` ne le fait pas (pip fourni par
  `ensurepip` de Python 3.11.18). Résolution non essayée avec ce pip-là.
- `setuptools` n'est pas dans le manifeste : `wandb` le demande sans borne ; le venv avait 79.0.1, une résolution
  `--ignore-installed` tire 84.2.1 (postérieure au 11 février 2025). Sans effet constaté sur l'import.
- `pip check` : `obf-reps 0.0` déclare `ipykernel`, `ipywidgets`, `pre-commit`, `sparsify` non installés
  (installation `--no-deps` voulue ; `sparsify` est fourni comme module par la distribution `eai-sparsify`).
  Aucun n'a manqué à l'import.
- Premier essai avec torch CUDA de PyPI arrêté au téléchargement (débit passagèrement faible) ; repris avec torch
  processeur.

## Espace disque
Venv du manifeste : 5,4 Go ; dossier de travail entier : 5,5 Go (venv, venv de résolution, clone jetable).
