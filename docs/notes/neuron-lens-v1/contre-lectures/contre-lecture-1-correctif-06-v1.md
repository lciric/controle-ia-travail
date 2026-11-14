# Contre-lecture 1 du correctif v1 de `06_activations.py` — rapport du contre-lecteur, recopié tel quel

Contre-lecteur : sous-agent neuf (« modèle B »), lancé le 2026-11-14 vers 09:52 UTC ; il ne l'a pas écrit. Pièces relues :
`correctif-06_activations-v1.md` (`36e369f5…`), `06_activations-llama-sans-qk-norm-v1.diff` (`2a67dd96…`),
`essai-06_activations-llama-v1.py` (`3575a397…`). Rapport rendu vers 09:56 UTC. Recopié sans modification de fond.

---

## 1) Empreintes vérifiées

- `correctif-06_activations-v1.md` : `36e369f5b57f18b9…f93039dd` — conforme.
- `06_activations-llama-sans-qk-norm-v1.diff` : `2a67dd969f70d74d…1fdb14` — conforme.
- `essai-06_activations-llama-v1.py` : `3575a397264b74f2…c51e6e` — conforme.
- Clone voisin : HEAD = `849bfe1678e28becceb1e3864afe5fc8297d02e4`, arbre propre ; `scripts/06_activations.py` = `151d1196…8035` (conforme à la note).
- Fichier corrigé de référence = `50d2b520…6bb1` (conforme à la note) ; son `diff` avec l'original ne contient que les deux blocs du correctif.
- `git apply --check` de la différence sur le clone : réussi. `ast.parse` du fichier corrigé et de l'essai : réussi.
- Rien n'a été exécuté (ni code voisin, ni essai). Sources lues de `transformers` : version 5.18.0 de l'environnement virtuel du dépôt (`.venv/lib/python3.13/site-packages/transformers`).

## 2) Verdict

**Correct après corrections** : la différence elle-même est juste et sans effet sur Qwen3, mais la passe complète sur Llama garde un point d'arrêt probable hors des crochets (remarque 1), et la note et l'essai annoncent plus qu'ils ne couvrent.

## 3) Remarques

**1. À corriger — bloquante pour la passe complète si la machine de B0 a un `transformers` qui se comporte comme 5.18.** `neuron_lens/arch.py` ligne 266 (`chat_open`), appelé par `06_activations.py` ligne 401 (passe « first »).
- Constat : Llama 3.1 a un gabarit de dialogue et pas de `<|im_start|>`, donc la branche prise est `tok.apply_chat_template([...], tokenize=True)[len(bos(tok))]`. Dans 5.18, `apply_chat_template` a `return_dict=True` par défaut et renvoie un `BatchEncoding` ; l'indice entier 1 lit `_encodings[1]`, alors qu'il n'y a qu'un encodage : `IndexError` attendu.
- Conséquence : l'arrêt tombe après toute la passe principale. L'état « main » est sauvegardé, donc la reprise ne refait pas la passe, mais le temps de machine est payé avant l'échec.
- Limite de ma lecture : je n'ai vu que 5.18 ; le voisin exige `transformers>=5` et je ne sais pas quelle version précise il a utilisée pour Gemma 4, qui prend la même branche.
- Correction proposée (seconde différence datée, ou ajout à celle-ci) :
  ```python
  tok.apply_chat_template([{"role": "user", "content": "a"}], tokenize=True, return_dict=False)[len(bos(tok))]
  ```
- À couvrir par l'essai avec le vrai tokeniseur de Llama à B0, ou par un `--docs N` de fumée, qui traverse « first » et « rep » sans écrire de tables.

**2. À corriger (note, prérequis) — `head_tables`, lignes 589-604, et `R_FIT`, ligne 96.**
- Constat : `head_tables` lit `arch.lens(MODEL, "R_mid", R_FIT)`. `arch.fits` ne rend les ajustements locaux que si les deux fichiers `r-llama-3.1-8b-instruct-L32-dclm.pt` et `s-…` existent dans `data/fits/` ; sinon il rend `("hub", "hub")` et télécharge `stdlogits/rs-lenses/llama-3.1-8b-instruct/r-lens/mid.pt`, qui n'existe vraisemblablement pas (la publication couvre Qwen3 et Gemma 4).
- Conséquence : l'arrêt tomberait après `neuron_tables` et avant l'écriture de `docs.parquet` (ligne 642, après `head_tables`).
- Autres prérequis non dits : `kept()` exige `data/token_counts-llama-3.1-8b-instruct.pt` (étape 03) et les tranches de l'étape 05.
- Correction : la note doit lister ces prérequis, ou dire que la tranche B-α s'arrête au fichier d'état et aux tables des neurones.

**3. Mineure — réponse à (a) pour le reste de `06_activations.py` : rien d'autre trouvé.**
- Crochets : `gate_proj`, `down_proj`, `input_layernorm`, `o_proj`, `self_attn` existent dans Llama. `LlamaAttention.forward` rend `(attn_output, attn_weights)` et l'attention « eager » rend bien les poids (5.18, lignes 213 et 281). `LlamaRMSNorm.variance_epsilon` existe, `rotary_emb.inv_freq` aussi (`arch.inv_freq`). `LlamaConfig.head_dim` est calculé quand il est absent, donc `layout_of` passe. `attn_norm` rend `None`, donc `attn_scale` rend `None`.
- Modes « first » et « rep » : `qk_norm`, `input_norm` et `attention` (hors « rep ») sortent tôt ; aucune pièce absente lue. `arch.bos` rend `[bos]` pour Llama, donc `first_pos = 1`, cohérent avec les documents de la passe principale, qui commencent par le jeton de début.
- Divisions : `06` ne divise aucune statistique QK. `sink`, `prev`, `self` sont divisés par `n_q`, qui est alimenté par `batch` et non par les normes, donc non nul. Les statistiques nulles (`q`, `q_r`, `q_m`, `k_r`, `k_m`) sont seulement sauvegardées.
- Hors périmètre, pour information : dans `05_act_corpus.py` ligne 76, le texte de dialogue rendu par le gabarit de Llama contient déjà le jeton de début, et `tok(text)` en ajoute un second ; la tranche « chat » aurait deux jetons de début.

**4. Mineure — réponse à (b) : comportement inchangé pour Qwen3, confirmé par lecture.**
- Mêmes crochets, même ordre (`q`, `k`, puis `v` s'il existe) ; 7 par couche pour Qwen3, 5 pour Llama. `Qwen3Attention` a `q_norm` et `k_norm` (5.18, lignes 237-238), donc `meta` est inchangé et la reprise n'est pas cassée.
- Incohérence sans cas réel : `hooks` teste « n'est pas `None` », `collect` teste `hasattr`. Une norme présente mais valant `None` serait sautée sans que la marque soit posée. Alignement proposé dans `collect` :
  ```python
  if any(getattr(layer.self_attn, n, None) is None for layer in model.layers for n in ("q_norm", "k_norm")):
      meta["qk_norm"] = False
  ```

**5. À corriger (note § 2.2) — la marque `meta["qk_norm"] = False` n'a aucun lecteur.**
- Constat : `08_reads.py` (lignes 200-232) ne lit pas `meta`. Sa partie « têtes » s'arrêterait de toute façon sur `arch.qk` (`q_norm.weight` absent des poids).
- La phrase « pour qu'aucune lecture des têtes ne prenne ces zéros pour des mesures » décrit une convention, pas une garde. Les scripts `scripts/checks/head_*.py` lisent aussi le fichier d'état et n'ont pas été examinés.
- Correction : le dire tel quel dans la note.

**6. À corriger — essai, test 2 : ce n'est pas une non-régression.**
- Constat : il vérifie « statistiques non nulles, 7 crochets », pas « identique à avant ». Ajouter une comparaison de l'original et du corrigé sur le même Qwen3 miniature (code proposé, repris dans l'essai v2 : `test_qwen3_identique_a_l_original`).

**7. À corriger — essai : rien n'assure que les fichiers essayés sont les bons, et l'artefact peut être sauté sans bruit.**
- Constat : sans `NEURON_LENS_ORIG`, le test de l'artefact (R5) est sauté ; `pytest -q` n'affiche qu'un « s ».
- Correction : vérifier les empreintes en tête des tests (original `151d1196…8035`, corrigé `50d2b520…6bb1`), et faire échouer le test de l'artefact à B0 au lieu de le sauter.

**8. À corriger — essai et note § 4 : « passe aboutie » dit plus que ce qui est essayé.**
- Constat : `one_pass` ne traverse que le mode « main » sur un lot. `collect()`, la ligne de la marque, les modes « first » et « rep », `chat_open`, `inv_freq` et les tables ne sont pas essayés. Le test 3 se réduit à une recherche de texte dans `inspect.getsource` et à une recopie de la condition.
- Correction : écrire dans la note « crochets du mode principal sur un lot », et ajouter les deux autres modes (code proposé, repris dans l'essai v2 : `test_llama_modes_first_et_rep`).

**9. Mineure — essai : pas d'erreur d'exécution trouvée à la lecture, sur 5.18.**
- Import du module : `R_FIT = arch.fits(MODEL)[0]` ne fait qu'un `AutoConfig.from_pretrained` sur le dossier local et un test d'existence ; aucun réseau, aucun dossier créé. `get_text_config()` rend la configuration elle-même. Les caches `functools` sont neufs après la purge de `sys.modules`, et de toute façon indexés par un chemin propre à chaque test.
- Configurations : `attn_implementation` est retiré des arguments par la classe de base (comme dans `tests/test_transport.py`). `LlamaConfig` et `Qwen3Config` ont `head_dim`.
- Comptes de crochets 5 et 7 : justes. `T = 24 > HEAD_FROM = 16` : 8 positions de têtes par document. Les empilements `topk(TOP=64)` ont 66 candidats (64 + B = 2) : suffisant.
- Formes : entrée de `q_norm` en `[B, T, têtes, hd]`, conforme à `qk_norm` ; index `int32` et `int64` acceptés par `index_add_`.
- Test de l'artefact : `hooks = col.hooks(stack)` est avant le `try`, donc l'`AttributeError` remonte intacte et `match="q_norm"` convient.
- Limites à écrire dans l'en-tête de l'essai : modèle miniature en `float32` (voie `bfloat16` de `count` non traversée) ; purge de `sys.modules` non défaite (lancer ce fichier seul) ; l'essai demande `pyarrow`, `safetensors`, `huggingface_hub` et Python 3.12 ou plus.

**10. À corriger — note § 2 : compagnons `.sha256` absents.** À poser au scellement (R6).

**11. Mineure — note § 1 et § 3 : ce qui est dit « vérifié ».**
- Confirmé : empreinte de l'original, empreinte du corrigé, `git apply --check`, `ast.parse`, ligne 287, branche « non Gemma » de `arch.py`, poids d'attention rendus par l'attention « eager », usage des statistiques QK dans `08_reads.py` lignes 222-232.
- Non vérifiable dans mon périmètre : l'identité avec la copie archivée `docs/sources/neuron-lens-lecture-20261113/…`.
- « Aucune autre lecture d'une pièce absente de Llama dans les crochets » : exact, mais limité aux crochets ; compléter avec les remarques 1 et 2.
- `mid_norm` est cité mais n'est pas utilisé par `06_activations.py` : sans conséquence.
- § 2.3 (« `v_norm` valant `None` désormais sauté ») : exact.
