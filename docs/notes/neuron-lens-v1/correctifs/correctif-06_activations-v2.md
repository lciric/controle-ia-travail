# Correctif daté de la passe d'activations du dépôt voisin pour Llama 3.1 8B Instruct — v2

Écrit par la session fille « Neuron Lens » (`session_01QPDgKfBxeeiM3BsxqJgSgf`, branche `prep/neuron-lens-v1`) le
2026-11-14 vers 10:05 UTC (`date -u`). **Remplace la v1** (`correctif-06_activations-v1.md`, `06_activations-llama-sans-qk-norm-v1.diff`,
`essai-06_activations-llama-v1.py`, archivés tels quels) après la contre-lecture 1
(`docs/notes/neuron-lens-v1/contre-lectures/contre-lecture-1-correctif-06-v1.md`). Aucune machine, aucune dépense ;
**code voisin non exécuté** (R-2685).

## 1. Objet
Dépôt `stdlogits/neuron-lens`, commit `849bfe1678e28becceb1e3864afe5fc8297d02e4` (MIT). Trois points d'arrêt de la passe
d'activations sur Llama 3.1, trouvés par lecture :
1. `scripts/06_activations.py` (`151d1196…`), `Collector.hooks`, ligne 287 : crochets sur `self_attn.q_norm` et `k_norm`, que
   Llama n'a pas → `AttributeError` dès la première couche.
2. `neuron_lens/arch.py` (`0f1e2262b5b13e5d68cf3e4ff139e756a92dbc1245781839a5d2bd41c992ce12`), `chat_open`, ligne 266 (appelé par la passe « first », ligne 396 de l'original de `06`, 401 du corrigé) : pour un
   tokeniseur à gabarit de dialogue sans `<|im_start|>` (Llama 3.1), `apply_chat_template(..., tokenize=True)[1]` ; dans
   `transformers` 5.18 (version lue par le contre-lecteur), la fonction rend un dictionnaire par défaut → `IndexError`
   probable, après toute la passe principale.
3. `06_activations.py`, `head_tables`, ligne 589 : `arch.lens(MODEL, "R_mid", R_FIT)` ; sans ajustement local, `R_FIT` vaut
   `"hub"` et la publication `stdlogits/rs-lenses` ne couvre que Qwen3-8B et Gemma 4 12B (arbre archivé du lecteur,
   `lentilles-stdlogits-rs-lenses-arbre.json`, `d2a7a076…` ; non relu par le contre-lecteur 2) → échec en fin de script (code de
   sortie non nul, ni `heads/acts.parquet` ni `docs.parquet`, après les tables des neurones). `causal_lens.py` ne lit
   `docs.parquet` que si le fichier d'état `data/acts/<modèle>.pt` n'est pas sur la machine (`catalog.flat_tokens`) : la mesure
   aurait pu tourner, mais sur une passe sortie en erreur.

## 2. Le correctif
Fichier : `docs/notes/neuron-lens-v1/correctifs/06_activations-llama-v2.diff` (deux fichiers, quatre blocs ; compagnon `.sha256`).
1. `hooks` : normes `q`, `k`, `v` lues par `getattr(…, None)` ; une norme absente ou `None` ne reçoit pas de crochet ; les
   statistiques QK (`q`, `q_r`, `q_m`, `k_r`, `k_m`) restent à zéro.
2. `collect` : si une couche n'a pas `q_norm` ou `k_norm` (même test que `hooks`), `meta["qk_norm"] = False`. **C'est une
   convention, pas une garde** : aucun script du dépôt ne lit cette clé (`08_reads.py` ne lit pas `meta` ; sa partie
   « têtes » s'arrêterait de toute façon sur `arch.qk` ; les scripts `scripts/checks/head_*.py` n'ont pas été lus). La clé
   n'est posée que pour un modèle sans ces normes : pour Qwen3 et Gemma 4, `meta` est inchangé (la reprise d'une passe, qui
   compare `meta`, n'est pas cassée).
3. `head_tables` : sans ajustement local et pour un modèle hors de la publication, la table des têtes est écrite **sans** la
   colonne `out_R_z` (message imprimé) au lieu d'échouer. Qwen3 et Gemma 4 : inchangé.
4. `arch.chat_open` : `return_dict=False` passé à `apply_chat_template`. Qwen3 prend l'autre branche (`<|im_start|>`) :
   inchangé.

Fichiers corrigés : `06_activations.py` `b97bf54b7c3b12f3ec1853000ba66cf5a6056c6c05b6400a8572a44e154cb902`, `arch.py`
`877fa6b0a864d8ffe88d15789ea9fa913a7bc7a529c399b2e001911c4eccf964`.

## 3. Prérequis de la passe sur Llama, hors du correctif
- étape 05 (corpus d'activations, tranches) et étape 03 (`data/token_counts-llama-3.1-8b-instruct.pt`, exigé par `kept()`) ;
- hors périmètre, signalé par le contre-lecteur : `05_act_corpus.py` ligne 76 — la tranche « chat » rendue par le gabarit de
  Llama contient déjà le jeton de début et `tok(text)` en ajoute un second. À constater en B0 (compte des jetons de début par
  document) ; tout correctif sera écrit, daté et contre-lu avant usage.
- la tranche B-α n'utilise ni la partie « têtes » de `08_reads.py`, ni la colonne `out_R_z`.

## 4. Ce qui a été vérifié sans exécuter le code voisin
- `git apply --check` de la différence v2 sur un clone propre au commit `849bfe16` : réussi ; `ast.parse` des deux fichiers
  corrigés (analyse syntaxique, aucune exécution) : réussie.
- Par lecture (contre-lecteur, `transformers` 5.18) : les autres pièces lues par les crochets existent dans Llama ; aucune
  division par une statistique QK laissée à zéro dans `06` ; comportement inchangé pour Qwen3.

**Non vérifié** : toute exécution. Identité de l'original avec la copie archivée du lecteur : vérifiée par l'autrice
(empreinte `151d1196…` des deux côtés), pas par le contre-lecteur.

## 5. Essai écrit (R5)
`essai-06_activations-llama-v2.py` : empreintes des fichiers essayés ; Llama miniature (crochets du mode principal sur un lot,
statistiques QK nulles, neurones et têtes comptés, 5 crochets par couche ; modes « first » et « rep ») ; Qwen3 miniature
**identique bit à bit** à l'original (non-régression, 7 crochets) ; `chat_open` sur un tokeniseur factice à gabarit de dialogue ;
artefact : l'original échoue sur Llama par `AttributeError` (ce test échoue au lieu d'être sauté si l'original n'est pas fourni).
Non couverts par l'essai : `collect()`, `neuron_tables`, `head_tables` ; ils le sont par la fumée `--docs 64` puis la passe
réelle de B-α (liste d'arrêt du texte gelé).

## 6. Traitement de la contre-lecture 1
| remarque | traitement |
|---|---|
| 1 `chat_open` | acceptée : bloc 4 |
| 2 `head_tables`, prérequis | acceptée : bloc 3 et § 3 |
| 3 rien d'autre dans `06` | notée ; `05_act_corpus.py` ligne 76 reportée au § 3 |
| 4 `hasattr` contre `None` | acceptée : même test dans `collect` et `hooks` |
| 5 marque sans lecteur | acceptée : dit tel quel au § 2 |
| 6 non-régression | acceptée : comparaison bit à bit |
| 7 empreintes, artefact sauté | acceptée |
| 8 « passe aboutie » | acceptée : périmètre de l'essai écrit exactement ; modes « first » et « rep » ajoutés |
| 9 limites | acceptée : en tête de l'essai |
| 10 compagnons `.sha256` | acceptée : posés au scellement |
| 11 « vérifié » | acceptée : § 4 |

## 7. Contre-lecture 2 (`docs/notes/neuron-lens-v1/contre-lectures/contre-lecture-2-correctifs-v2.md`, `50f6f7d5…`)
Relu : cette note à `1c3b8c9f…`, la différence `76b639a0…` (inchangée depuis), l'essai à `6d6c4c08…`. Verdict : « correct après
corrections mineures ». Retouches faites dans ce fichier et dans l'essai (fichiers non scellés à la relecture ; empreintes relues
ci-dessus) :

| remarque | traitement |
|---|---|
| 1 tableau du § 6 exact | constat |
| 2 blocs nouveaux corrects ; aucun lecteur de `out_R_z` dans `causal_lens.py` | constat ; fichiers non examinés (`08_reads.py`, `10_labels.py`, `12_release.py`, `neurons.py`, `weights.py`, `corpus.py`) notés |
| 3 motif surévalué | acceptée : § 1.3 réécrit |
| 4 numéro de ligne | acceptée : 396 (original), 401 (corrigé) |
| 5 liste en dur | acceptée : source citée, limite dite |
| 6 essai sans erreur trouvée | constat |
| 7a vrai tokeniseur | acceptée : `test_chat_open_vrai_tokeniseur` ajouté (B0) |
| 7b assertion recopiée | acceptée : commentée comme rappel |
