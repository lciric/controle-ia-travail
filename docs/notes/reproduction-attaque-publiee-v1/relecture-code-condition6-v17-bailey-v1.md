# Contre-lecture du code v17 (condition 6) — témoin « attaque publiée reproduite » (Bailey et collègues), v1

Contre-lecteur neuf (R2), n'ayant écrit aucun des fichiers lus. Date : 12 novembre 2026. Objet : commit `60d06b1f`
(`execution_v4.py`, `instance_v16.py`, `lanceur_v17.py`, essais `test_v17_*`, épreuve Hydra 1.3.2 hors essais).
Cloisons tenues : ni `donnees/bras-attaque*`, ni `donnees/mode-tenu-a-l-ecart*`, ni `docs/notes/bras-attaque/`, ni
`docs/notes/programme-et-4-familles-evasion/`, ni `registres/etat.md`, ni `registres/decisions.md`, ni aucun résultat ou
seuil de sonde ou de moniteur ; aucune variable d'environnement de secrets lue ; aucune commande réseau ; aucun fichier
existant modifié.

## Verdict

**Conforme après corrections** — une seule correction, hors du code exécuté : **C-1** (sceller l'épreuve hors essais et sa
sortie, R6). Le changement de code est celui annoncé et lui seul ; `runpy.run_path(..., run_name="__main__")` supprime la
cause établie (Hydra ne cherche plus `configs` comme ressource de paquet) sans changer la substitution du journaliseur,
les graines, le dossier courant, `sys.path`, `sys.argv`, le début exact de la sortie standard ni la propagation des
erreurs. Les autres constats sont des remarques.

Fichiers lus (empreintes SHA-256 au moment de la lecture) :

| Fichier | Empreinte |
|---|---|
| `src/controle_ia/temoin_bailey/execution_v4.py` | `560247ed8cd537ceb4558027de875233ef77da314057f764e8646b2abde65f3f` |
| `src/controle_ia/temoin_bailey/instance_v16.py` | `d9a56e878d091b210d7b96ceded756d24a37f8dea9ef579d489bdf24d524a597` |
| `src/controle_ia/temoin_bailey/lanceur_v17.py` | `acad9644093370b0ab74402eb52f3dff884b7b73284128bc30e035cf7d8ae541` |
| `tests/test_temoin_bailey_condition6_v17.py` | `6856b0b20d4a84b2375bea624fdbc8de9be47181aa706eb5b217926069526991` |
| `runs/temoin-bailey-v1-20261111/epreuve-hydra132-execution-v4-v1.py` | `17c3544d7354101f32db3114badb61396122f81256d605728eb9e00cd21a3522` |
| `runs/temoin-bailey-v1-20261111/epreuve-hydra132-execution-v4-sortie-v1.txt` | `7c204bd535e251342c088b89ce625b5b1f38d7fed363a3e291691030817fdd09` |
| `runs/temoin-bailey-v1-20261111/sortie-conduite-v9/pilote/transfert-1/erreur-demarrage-v1.txt` | `33599bfc6a36f53b52d777261e3373fc6b5a8fc7ff58b2c117fb2b5e452ba124` |

Code public lu (clone au commit `9c1f4b1a`, copie du bloc-notes de session) : `inference_time_experiments/train_harmful.py`,
`evaluate.py`, `obf_reps/utils.py`, `obf_reps/logging/__init__.py`, `obf_reps/data/__init__.py`, `obf_reps/models/hf.py`,
`obf_reps/metrics/__init__.py` (début de `ObfMetric`), `configs/config.yaml`, `configs/experiment/{default,z-jailbreak,
zf-iter-100-mlp}.yaml`. Hydra lu : 1.3.2 (environnement minimal du bloc-notes, version figée de l'instance) et 1.3.8
(`.venv` du dépôt).

## 1. Différentiels

- `execution_v3.py` → `execution_v4.py` : docstring (nouveau paragraphe v4, usage `-m …execution_v4`), `import runpy`
  (l. 44), et l. 116-118 : `script = racine / "train_harmful.py"` ; `sys.argv = [str(script), *over]` ;
  `runpy.run_path(str(script), run_name="__main__")` au lieu de `import train_harmful` ; `train_harmful.main()`. Rien
  d'autre : garde `TESTING` (l. 93-95), `WANDB_MODE` (l. 102), `os.chdir(racine)` (l. 104), `sys.path.insert(0, racine)`
  (l. 105), `set_seed` (l. 107-108), substitution du journaliseur (l. 110-114), `surcharges`, `configuration_attendue`
  identiques.
- `instance_v15.py` → `instance_v16.py` : docstring ; l. 222 `from .execution_v4 import configuration_attendue,
  surcharges` ; l. 792 commande de l'enfant `-m controle_ia.temoin_bailey.execution_v4`. Rien d'autre.
- `lanceur_v16.py` → `lanceur_v17.py` : docstring ; l. 271 import `instance_v16` ; l. 290-291 `INSTANCE_MODULE`
  (`instance_v16`) et `VEILLEUR_MODULE` (`lanceur_v17`) ; l. 305-310 commentaire et `CHEMINS_ARCHIVE` (`execution_v4.py`,
  `instance_v16.py`) ; l. 917 (docstring) et l. 1783 (message « reprise requise (`lanceur_v17 reprendre`) ») — ce dernier
  suit le changement de `VEILLEUR_MODULE`, annoncé. Rien d'autre.
- Fermeture de l'archive : imports internes de `instance_v16` → `gardes`, `analyse_v3`, `conventions_v3`, `execution_v4`,
  `journaliseur_v3`, `lecture_v8` ; de `execution_v4` → `conventions_v3`, `journaliseur_v3` ; de `lecture_v8` →
  `scellement`, `gardes`, `analyse_v3`, `conventions_v3`, `journaliseur_v3` ; de `journaliseur_v3` → `gardes`,
  `analyse_v3`, `conventions_v3`. Tous présents dans `CHEMINS_ARCHIVE` ; chacun est la dernière version présente dans
  `src/controle_ia/temoin_bailey/` (aucun module ancien envoyé). Aucun import dynamique (`importlib`, `__import__`) hors
  `importlib.metadata`.
- Chaînes exécutées : `grep` et l'essai `test_v17_aucune_reference_a_execution_v3_dans_le_code_execute` (arbre syntaxique,
  docstrings exceptées) ne trouvent `execution_v3`, `instance_v15` ni `lanceur_v16` que dans des docstrings.
  `runs/…/lancer-conduite-v10.py` (non suivi par git, hors périmètre) importe déjà `lanceur_v17`.

## 2. `runpy.run_path(..., run_name="__main__")` contre `python train_harmful.py`

- **Cause supprimée par construction.** Hydra (1.3.2, `hydra/_internal/utils.py` l. 44-59) prend le fichier appelant
  (`inspect.getfile`) quand `task_function.__module__` vaut `"__main__"`, et la configuration devient
  `file://<dossier du script>/configs` (l. 126-130). Avec `run_name="__main__"`, les fonctions du script ont
  `__module__ == "__main__"`. La trace de l'instance (`erreur-demarrage-v1.txt`) passe par
  `importlib_resources_config_source.py` (source « paquet »), branche qui n'est plus empruntée.
- **Journaliseur.** `train_harmful.py` n'importe que `Logger` (l. 18) ; le journaliseur est construit par
  `validate_and_create_experiment_config` dans `obf_reps/utils.py` (l. 48 `from obf_reps.logging import DummyLogger,
  WAndBLogger` ; l. 394-396 `WAndBLogger(log_file=…, username=…, metadata=…)`), nom global lu à l'appel ; `obf_reps.utils`
  est chargé par `execution_v4` avant `runpy` et réutilisé par le script (cache `sys.modules`). Aucun autre module public
  ne nomme `WAndBLogger` ni ne teste le type du journaliseur. `configs/experiment/z-jailbreak.yaml` met
  `logger: "WAndBLogger"` ; `JournaliseurLocal` a la signature de construction et les méthodes appelées (`log`,
  `create_table`, `log_to_table`, `log_table_name`). Substitution couverte.
- **Graines.** Inchangées : `transformers.set_seed(graine)` avant `runpy` ; puis le code public reprend
  `set_seed(config.seed)` dans `obf_reps/optimize/optimizers.py` l. 128 avec `experiment.seed` surchargé.
- **Dossier courant.** `os.chdir(racine)` avant `runpy` ; Hydra 1.3.2 ne change pas de dossier (`version_base=None` →
  base 1.3, `hydra/version.py` l. 74-75 ; `hydra/core/utils.py` l. 148-152 : `chdir` à faux). Les chemins relatifs
  publics (`./datasets/harmful_dataset/`) se résolvent sous `racine`, comme chez les auteurs.
- **`sys.path`.** `runpy.run_path` sur un fichier n'ajoute rien à `sys.path` ; `racine` est déjà en tête (l. 105), comme
  `python train_harmful.py` y met le dossier du script. `evaluate` (module local, `train_harmful.py` l. 15) se résout dans
  `racine`. Le dossier `datasets/` sans `__init__.py` dans `racine` reste une simple portion d'espace de noms : le paquet
  installé `datasets` (importé par `obf_reps/data/__init__.py` l. 15) l'emporte, comme chez les auteurs, et l'import a déjà
  réussi sur l'instance (la trace montre que la v3 a atteint `hydra.run`, donc tous les imports du script ont réussi).
- **`sys.argv`.** Fixé avant l'appel ; `runpy` (Python 3.11, `runpy.py` l. 96, `_ModifiedArgv0(fname)`) remet
  `sys.argv[0]` au même chemin pendant l'exécution et laisse `sys.argv[1:]` (les surcharges lues par Hydra) intact.
- **Début de la sortie standard.** Le premier énoncé du script est `print(OmegaConf.to_yaml(cfg))` ; aucun journal Hydra
  au niveau INFO avant l'appel ; aucun import n'a rien imprimé sur l'instance (sortie vide des deux pilotes). L'égalité
  exacte avec `configuration_attendue` est observée avec les vraies configurations publiques sous 1.3.2 et 1.3.8.
- **Erreurs.** Une exception de la fonction décorée remonte dans Hydra (`run_and_report`), qui écrit le message sur la
  sortie d'erreur et lève `SystemExit(1)` ; `runpy` ne l'attrape pas, `return 0` (l. 119) n'est pas atteint : code non
  nul, aucun repli silencieux (essai `test_v17_erreur_du_script_propagee_sans_repli`).
- **Effets propres à `runpy`, examinés un à un** : `__file__` vaut le chemin absolu du script (le code public ne lit
  jamais `__file__`) ; `sys.modules["__main__"]` est le module temporaire du script pendant l'exécution ; aucun objet
  défini dans le script n'est sérialisé (les `pickle.dump` de `train_harmful.py` l. 124 et `metric.save_probe` portent
  sur des classes de `obf_reps`) ; aucun `multiprocessing`, aucun `num_workers` (chargeurs à 0 processus) dans le code
  public ; aucun module public n'importe `train_harmful` ni `__main__` ; `hydra.job.name` reste `train_harmful` (journal
  `train_harmful.log` sous `hydra.run.dir`, hors du clone, vérifié par l'essai sain) ; `Path(__file__)` absent du code
  public.
- **Sonde du relecteur** (hors dépôt, `/tmp/claude-0/-home-user-controle-ia-travail/2cfa1854-671e-5aa7-83ff-79ac90ee7d37/scratchpad/relecteur-v17-sonde/scripts/sonde.py`,
  Hydra 1.3.2) : mini-clone de l'essai, script augmenté d'un `evaluate.py` local. Observé pendant l'exécution du script :
  dossier courant = `racine` ; `sys.path[0]` = `racine` ; `evaluate` chargé depuis `racine` ; graine 7 reçue par
  `set_seed` ; `__name__ == "__main__"`, `sys.modules["__main__"].__file__` = script ; `sys.argv[0]` = script ; code 0 ;
  journaliseur substitué.

## 3. Essais et épreuve

- `test_v17_*` : 8 réussis, 0 sauté (`TEMOIN_BAILEY_CONFIGS_PUBLIQUES` fourni), 4,9 s, Hydra 1.3.8 du `.venv`.
- Épreuve hors essais rejouée par le relecteur avec Hydra 1.3.2 (Python 3.11.18) : sortie identique ligne pour ligne à
  `epreuve-hydra132-execution-v4-sortie-v1.txt` (v4 : code 0, début exact, journaliseur substitué ; v3 : code 1, rien
  imprimé, journaliseur jamais construit ; configurations synthétiques et publiques).
- **R5 tenue** : même mini-clone, même commande, seule la voie change ; le cas sain passe, l'artefact (le chemin des
  pilotes du 12 novembre) tombe avant toute impression. L'épreuve distingue les deux chemins.

## Constats

- **C-1 — à corriger** — `runs/temoin-bailey-v1-20261111/epreuve-hydra132-execution-v4-v1.py` et
  `…-sortie-v1.txt` : aucun compagnon `.sha256` (R6), alors que les autres dépôts du dossier en ont. En outre, la première
  ligne de la sortie (date, Python, commit public, empreinte des configurations) n'est pas imprimée par le script : elle a
  été ajoutée à la main, et le script ne consigne ni l'interpréteur ni le chemin de l'installation Hydra 1.3.2 employés.
  Correction : sceller les deux fichiers tels quels ; si une v2 de l'épreuve est faite, lui faire imprimer elle-même
  `sys.executable`, `hydra.__file__` et le commit du dépôt.
- **C-2 — remarque** — `tests/test_temoin_bailey_condition6_v17.py` l. 3667-3705 (`MINI_SCRIPT`, `_mini_clone`) : les
  essais n'affirment ni le dossier courant, ni `sys.path[0]`, ni l'import d'un module local voisin du script (le cas de
  `evaluate`), ni la graine reçue par `set_seed` (le faux `transformers.GRAINES` est écrit mais jamais lu). La sonde du
  relecteur établit ces quatre points pour la v4 ; les ajouter au mini-script (une ligne sur la sortie d'erreur, quatre
  assertions) fermerait la régression.
- **C-3 — remarque** — l. 3764-3774 : l'essai avec les vraies configurations publiques est sauté sans
  `TEMOIN_BAILEY_CONFIGS_PUBLIQUES`, et la suite tourne sous Hydra 1.3.8 (`.venv`), l'instance sous 1.3.2. La version
  figée n'est éprouvée que par l'épreuve hors essais (C-1).
- **C-4 — remarque** — L'artefact sur processeur tombe avec « Primary config module 'configs' not found », l'instance
  avec `NotADirectoryError: MultiplexedPath only supports directories`. Les deux passent par la source « paquet » de Hydra ;
  la v4 ne l'emprunte plus (§ 2, premier point). L'épreuve prouve donc que la voie v3 tombe avant impression et que la v4
  passe, pas qu'elle reproduit à l'identique le mécanisme de l'instance — ce qui n'est pas nécessaire ici.
- **C-5 — remarque** — `hydra/_internal/utils.py` l. 29-47 (1.3.2) : si la variable `HYDRA_MAIN_MODULE` était définie
  dans l'environnement de l'enfant, Hydra reviendrait à la source « paquet ». Rien dans le code ne la pose ; non vérifié
  sur l'image de l'instance (le relecteur ne lit pas l'environnement).
- **C-6 — remarque** — `execution_v4.py`, `instance_v16.py`, `lanceur_v17.py` n'ont pas encore de compagnon `.sha256` ;
  la pratique du dépôt (commit `91238a73`) est de les sceller après la contre-lecture. À faire avant le manifeste qui
  citera le commit.

## Risques résiduels (entre l'impression de la configuration et la première ligne « MARK »)

Lecture du code public seulement, sans exécution du modèle ; aucune proposition sur ce qui sort de l'instance.

1. **Validation** (`obf_reps/utils.py` l. 207-222) : `model_path` doit exister sur l'instance ; `./datasets/
   harmful_dataset/` (relatif) doit contenir les six CSV dans le clone de l'instance.
2. **Journaliseur** (`journaliseur_v3.py` l. 160-174) : `TEMOIN_BAILEY_CONFIG` requise ; garde « dossier neuf » ; une
   `GardeArret` ici sort en code 1 par Hydra, après la configuration imprimée (la garde de démarrage passe, le message
   d'erreur de démarrage dépend alors de la condition de `ecrire_erreur_demarrage`).
3. **Chemins de sauvegarde** (`utils.py`, boucle des chemins `save_*`) : `FileExistsError` si
   `sondes/HIDHarmfulConceptDataModule/MLPMetric_ade_0.pkl` ou `params/…/model-params-MLPMetric_ade_0.pkl` existent ;
   dossier de travail neuf exigé par `executer`, donc improbable.
4. **Chargement du modèle** (`obf_reps/models/hf.py` l. 181-190) : `from_pretrained(path, device_map="cuda",
   torch_dtype=float16)` et tokeniseur depuis le chemin local ; mémoire graphique (≈ 16 Go pour 8 milliards de paramètres
   en demi-précision).
5. **Construction de la sonde MLP** (`obf_reps/metrics/__init__.py` l. 146-171) : représentations de tout le jeu
   d'entraînement du concept sur 32 couches, lot de 1, puis ajustement de la sonde et d'une analyse en composantes
   principales : long, et gros en mémoire (hôte ou carte) ; premier lieu probable d'épuisement mémoire ou de dépassement
   de l'échéance avant tout tour.
6. **Tour 0** (`train_harmful.py` l. 50-168) : évaluation du défenseur avec génération (`gen_len` 300, lot d'évaluation 16
   selon `zf-iter-100-mlp`) ; 2 époques d'attaque (`epochs: 2`) au lot de 1 ; sauvegarde de la sonde et des paramètres
   (`assert not path.exists()`) ; évaluation de l'attaquant avec `evaluate_behavior=True`, qui charge le juge StrongREJECT
   affiné (`obf_reps/data/__init__.py` l. 11 et l. 563-578 : cache Hugging Face, base à accès restreint, révisions gardées
   par `journaliseur_v3` l. 259-260) — second modèle en mémoire graphique ; figures `plot_lat_scan` (trois par exemple
   évalué) : `evaluate.py` l. 461 a son `plt.close("all")` commenté, mais `JournaliseurLocal.log_to_table` ferme chaque
   figure reçue (`journaliseur_v3.py` l. 238-239, `_fermer_figure` l. 76-81) ; puis réajustement de la sonde et ligne
   « MARK ».
7. **Journaux Hydra** : la configuration par défaut de Hydra envoie la journalisation sur la sortie standard ; toute ligne
   de journal arrive après la configuration (la garde ne compare que le début) et ne gêne la lecture des lignes « MARK »
   que si elle coupait une ligne, ce que la mise en tampon par ligne de `Surveillance` absorbe.

Aucun de ces points n'est introduit par la v4 : tous existaient sous `python train_harmful.py` et n'avaient jamais été
atteints, la v3 mourant avant l'impression.
