# Inventaire des réglages de Llama dans le code voisin (lecture par lentille neuronale, tranche de l'ajustement de nos lentilles) — v1

Rendu verbatim d'un sous-agent neuf (lecture seule ; code voisin `stdlogits/neuron-lens` au commit
`849bfe1678e28becceb1e3864afe5fc8297d02e4`, jamais exécuté ni importé), commandé par la session
`session_01XJ6MgmvmAAZ9h382ct8kHk` le 2026-11-18 vers 04:00 UTC pour le brouillon 2 du texte gelé de la tranche (contre-lecture du
brouillon 1, M-5). Marques du sous-agent : **V** vérifié sur pièce, **D** déduit. Écart déclaré par lui : une lecture des fichiers de
provenance JSON par `python3 -I -c "json.load(...)"`. Les points repris par le texte gelé sont vérifiés par l'autrice sur pièce là où ils
fixent une règle ; les autres restent au niveau de ce rendu.

---

Inventaire en lecture seule de la copie de Neuron Lens au commit `849bfe1678e28becceb1e3864afe5fc8297d02e4`. J'ai vérifié le commit avec `git rev-parse HEAD`, et l'arbre est propre (`git status` vide).

Résumé :
- **Sept ruptures nettes sur Llama** :
- `lens_compare.py` a le modèle Qwen écrit en dur.
- `lens_compare.py` a la couche 32 dans ses couches par défaut.
- `score` ignore le processeur graphique.
- `02_fit.py` a pour défauts le modèle `Qwen/Qwen3-0.6B` et 12 documents.
- `05_act_corpus.py` a pour défaut 4 000 lignes de DCLM au lieu de 40 000.
- Les options `--parts` par défaut de `08_reads.py` et de `reads_at_firings.py` lancent aussi la partie « têtes », qui échoue sur Llama.
- **Plusieurs replis silencieux** : surtout la reprise de `02_fit.py`, qui ne compare pas l'empreinte du corpus, et l'usage sans contrôle d'un ajustement partiel.
- **Aucun correctif existant ne touche 01, 02, 03, 04, 07, 08, `lens_compare` ni `reads_at_firings`.**

Écart à ta consigne : en plus de cat, sed et grep, j'ai lu une fois les fichiers de provenance JSON avec `python3 -I -c "json.load(...)"`. Aucun code du dépôt n'a été exécuté ni importé.

Marques : **V** = vérifié sur pièce ; **D** = déduit (comportement de transformers, du tokeniseur de Llama ou de Drowse non lu ici). Les numéros de ligne sont ceux du commit épinglé ; je les ai recalculés là où j'avais concaténé plusieurs fichiers.

Abréviation des tableaux : `<stem>` = `llama-3.1-8b-instruct`.

---

## `neuron_lens/catalog.py`, `paths.py`, `corpus.py`, `arch.py` (modules communs)

| ligne(s) | constat | effet sur Llama ou nos mesures | couvert ? | correctif proposé (minimal) |
|---|---|---|---|---|
| catalog 32 | `MODEL = os.environ.get("NEURON_LENS_MODEL", "Qwen/Qwen3-8B")`, lu à l'import (V). | Lu par 03, 05, 06, 07, 08, `causal_lens`, `reads_at_firings`, `corpus.act_file` et `catalog.kept`. Non lu par 01, 02, 04, ni par `lens_compare` (modèle en dur, voir plus bas). Il faut l'identifiant exact, sinon `load_fits` refuse (lenses 104-106). | partiel (le correctif des lentilles le dit) | Poser `NEURON_LENS_MODEL=meta-llama/Llama-3.1-8B-Instruct` avant chaque étape. |
| corpus 8, 12-19 | Ligne de document : `tok(text[:chars])["input_ids"][:seq_len]` avec `chars = max(4000, 8*seq_len)` (V). Jetons spéciaux du tokeniseur par défaut, donc le jeton de début est ajouté pour Llama (D). | La longueur compte le jeton de début. Une ligne d'ajustement de 128 jetons = 1 jeton de début + 127 de texte, contre 128 de texte pour Qwen. Coupe à 4 000 caractères pour 128 et 256 jetons, à 4 096 pour 512. | non | Rien à corriger ; à rapporter. |
| corpus 22-34 | `lens_docs` : sans `full`, prend les `n` premières lignes, puis retire celles de moins de `min_len` jetons. Avec `full`, saute les lignes de moins de `seq_len` jetons et garde les `n` premières assez longues (V). | Le nombre de documents peut être inférieur à `n` **sans message** dans les deux modes. | non | Assertion `len(rows) == n` dans les appelants, ou impression de l'écart. |
| corpus 37-45 | `act_file("chat")` → `act-chat-<stem>.jsonl` ; les autres tranches → `act-<tranche>.jsonl`, communes à tous les modèles (V). | Les tranches web, chinois et code sont réécrites par 05 quel que soit le modèle. | la provenance « chat » l'est | — |
| corpus 48-60 | `act_docs` : ordre des tranches dclm, zh, code, chat ; `line` = rang dans le fichier de la tranche ; lignes de moins de `min_len` retirées (V). | Le rang d'un document dans le corpus d'activations n'est pas la ligne : la correspondance passe par `docs.parquet`. | — | — |
| catalog 125-134 | `kept()` = jetons comptés au moins 5 fois dans `data/token_counts-<stem>.pt` (écrit par 03), moins ceux dont le décodage contient « � » (V). Aucun retrait des jetons spéciaux. | Pour Llama, le jeton de début (présent dans chaque document, deux fois dans « chat ») et les jetons du gabarit (`<|start_header_id|>`, `<|end_header_id|>`, `<|eot_id|>`) entrent dans les listes de lecture, dans les pilotes de 07 et dans les jetons de déclenchement (D). Qwen n'a pas de jeton de début. | non (le double jeton de début est seulement signalé, correctif de 06 v3 § 3) | À décider : soit constater (compte et rang du jeton de début dans les listes), soit retirer `tok.bos_token_id` de `kept()`, ce qui serait un écart à la publication. |
| arch 299-303 | `fits()` cherche `data/fits/r-<stem>-L32-dclm.pt` **et** `s-<stem>-L32-dclm.pt`. Si l'un des deux manque, renvoie `("hub","hub")` (V). | Si un seul fichier existe, ou si les noms portent `-T128` ou `-s0of2`, tout bascule sur `stdlogits/rs-lenses`, qui n'a pas Llama. Échec bruyant à la lecture (erreur 404) dans 08 et `reads_at_firings`. Pour 06 corrigé, la table des têtes est écrite sans `out_R_z`. | correctif de 06 v3 (bloc 3), pour 06 seulement | Ligne imprimée « ajustements lus : … » ; arrêt si `hub` pour un modèle hors publication. |
| arch 288-296, lenses 95-116 | `arch.lens` puis `load_fits` contrôlent la lentille, `layers == model_layers` et le modèle. Ils ne contrôlent **pas** `next_doc == docs` (V). | Un ajustement interrompu (par ex. 400 documents sur 1 000) est utilisé tel quel par 04, 08 et `reads_at_firings`, sans message. | non | Dans `load_fits`, refuser si `saved["next_doc"] < saved["meta"]["docs"]`, ou l'imprimer. |
| arch 171-176 | `bands(32)` donne des quarts : (0,7) (8,15) (16,23) (24,31) (V). | Bandes des résumés de `reads_at_firings` et de 08. | — | — |
| arch 256-267 | `bos` et `chat_open` (V). | Utilisés par 06 seulement. | correctif de 06 v3 (bloc 4) | — |

## `scripts/01_lens_corpus.py`

| ligne(s) | constat | effet | couvert ? | correctif |
|---|---|---|---|---|
| 21, 27-28 | Jeu `HuggingFaceFW/dclm_100BT-shuffled`, `--docs` par défaut 1000, `--revision` par défaut None (V). | Passer `--docs 1000`, qui est aussi le défaut. | — | — |
| 31-34 | La révision vient de `--revision`, sinon de `data/corpus/dclm.provenance.json` (suivi dans git : `2fa015e4044ec442a0734e89658cdcc538d10dd4`, lignes `[0,1000]`, 1 000 identifiants), sinon de la **dernière** révision du jeu (V). | Si le fichier de provenance a disparu, on prend la dernière révision sans message. | non | Passer `--revision 2fa015e4044ec442a0734e89658cdcc538d10dd4` explicitement. |
| 37-40 | Lignes `[0, docs)` du flux, **sans** filtre des textes vides (V). | `dclm.jsonl` ligne i = ligne i du flux. | — | — |
| 41-49 | Écrit `data/corpus/dclm.jsonl` et **réécrit** `dclm.provenance.json`, qui est suivi dans git (V). | Comparer à `git show 849bfe16:data/corpus/dclm.provenance.json` (identifiants). | non | Contrôle après la passe : `git diff` vide sur la provenance. |

## `scripts/02_fit.py`

| ligne(s) | constat | effet | couvert ? | correctif |
|---|---|---|---|---|
| 194 | `--model` par défaut `Qwen/Qwen3-0.6B` ; `NEURON_LENS_MODEL` non lu (V). | Passer `--model meta-llama/Llama-3.1-8B-Instruct`. La même chaîne exacte que `NEURON_LENS_MODEL` est exigée plus loin (lenses 104, Drowse). | non | Passer l'argument. |
| 203 | `--docs` par défaut **12** (V). | Passer `--docs 1000`. | non | — |
| 204-205 | `--seq-len` 128 ; `--full-length` = ne garder que les documents d'au moins `seq_len` jetons, les `--docs` premiers (corpus 29-30), et ajouter le suffixe `-T128` au nom (55-56) (V). | Avec `--full-length`, `arch.fits` ne trouve plus le fichier et bascule sur « hub ». Avec un `dclm.jsonl` de 1 000 lignes, on a moins de 1 000 documents sans message. | non | Ne pas passer `--full-length`. |
| 207-213 | `--dim-batch` 256, `--targets` (R : out,mid ; S : mid,out ; transport 45), `--device auto` (cuda sinon cpu), `--dtype auto` (bf16 sur cuda), `--acc-device auto`, `--shard 0/1`, `--save-minutes` 10 (V). | Passer `--save-minutes 60`. Un `--shard n>1` ajoute `-s{i}of{n}` (58-59), ce que `arch.fits` ne lit pas, et aucun script n'écrit un ajustement fusionné. | non | `--shard 0/1` seulement. |
| 69-72 | Sur cuda en bf16 : `torch.set_float32_matmul_precision("high")`, donc produits fp32 en TF32 (V). | Précision des sommes : à consigner au manifeste. | — | — |
| 132 | `lens_docs(..., args.docs, args.seq_len, SKIP_FIRST + 2 = 18, full)` (V). | Le minimum de 18 jetons compte le jeton de début. Positions valides `[16, T−1)` (transport 90-93), donc le jeton de début et 15 jetons de texte sont exclus pour Llama, contre 16 jetons de texte pour Qwen (D pour le jeton de début). | non | À rapporter. |
| 173 | Moitié = `i % 2`, où i est le **rang parmi les documents retenus**, pas la ligne du flux (V). | Si un document court est retiré, les moitiés ne suivent plus la parité des lignes de DCLM. | — | À rapporter (les 1 000 documents de Qwen étaient tous retenus : « 500-document halves », design.md). |
| 149-159 | Reprise : comparaison de `meta` **hors** `("docs", "rows_sha256", "dim_batch")` (151). Les anciennes clés absentes prennent leur ancien défaut (152). Toute autre différence (modèle, couches, corpus par nom, seq_len, full_length, cibles, shard, dtype, règles) provoque `SystemExit` (V). | **Un corpus changé sous le même nom reprend sans message** au document `next_doc`, en mélangeant les deux corpus. À la sauvegarde suivante, `meta` est **réécrit** avec la nouvelle empreinte : la trace de l'ancienne est perdue (161-166). | non | Refuser si `rows_sha256` diffère sur le préfixe déjà ajusté (empreinte de `rows[:next_doc]` enregistrée), ou au minimum imprimer les deux empreintes. |
| 168-180 | Sauvegarde toutes les `save_minutes` et au dernier document (V). | Si la liste `mine` est vide (reprise sans rien à faire), aucune écriture. | — | — |
| 185-188 | Écart entre moitiés imprimé par couche avec `{x:.2f}` (V). | Arrondi à 2 décimales. | — | Recalcul : voir la liste « mesures de stabilité ». |
| 225-236 | `--detach` écrit dans `logs/fit_r.log` ou `fit_s.log` en ajout (V). | Le même journal sert à toutes les relances. | — | — |
| layers 502-582 (V), rules 105-123 (V) | Le chemin de Llama passe : pas de q/k-norm (`getattr(..., None)`, layers 251-253), pas de fenêtre glissante, `rotary_emb` du modèle (mise à l'échelle llama3 prise en charge par transformers : D), `at.scaling`, `num_key_value_groups`, aucun biais (check 478-490), SiLU. | Aucun arrêt attendu (D : attributs de `LlamaAttention` dans transformers 5 non lus ici). | — | Fumée `--docs 4` avant la vraie passe (nom de fichier distinct, sinon reprise). |
| rules 96 | `_check_norm` tire `torch.randn` **sans graine** (V). | Simple contrôle à tolérance 1e-2, sans effet sur les sommes. | — | — |

## `neuron_lens/transport.py`

| ligne(s) | constat | effet | couvert ? | correctif |
|---|---|---|---|---|
| 44 | `SKIP_FIRST = 16` (V). | Voir 02. | — | — |
| 192-223, 256-258 | R : la cible `out` couvre les couches 0..n−2. L'estimation de la couche `layer` est rangée en `out[layer−1]` (220-222). La cible `mid` couvre 0..n−1 (V). | Llama : `out` = couches 0..30 ; la couche 31 est l'identité par définition (sortie finale). | — | — |
| 64-72 | `split_half` = ‖a/n0 − b/n1‖_F / ‖(a+b)/(n0+n1)‖_F par couche, NaN si une moitié est vide (V). | Formule de stabilité. | — | — |

## `scripts/03_token_counts.py`

| ligne(s) | constat | effet | couvert ? | correctif |
|---|---|---|---|---|
| 24 | `--slices` par défaut `dclm,zh,code,chat` (V). | Lit `act-chat-<stem>.jsonl`, donc 05 doit précéder. | — | — |
| 26, 32 | Tokeniseur de `MODEL`. `tok(json.loads(line)["text"])` sur le **texte entier**, sans coupe à 4 000 caractères ; jetons spéciaux ajoutés (V). | Compte le jeton de début une fois par document (D), deux fois dans « chat » (D). Une ligne vide ferait échouer (pas de `strip`). | double jeton signalé, non corrigé | À constater (compte du jeton 128000). |
| 29, 33 | Vecteur de taille `len(tok)` = 128 256 pour Llama (D), égale à la taille de `lm_head` (V pour l'usage `[:nv]` de `score`). | — | — | — |
| 37 | Écrit `data/token_counts-<stem>.pt` (`arch.counts_path`) (V). | Lu par `kept()` (06, 07, 08, `lens_compare`, `reads_at_firings`) et par `score` (ligne 278). **Si 03 est relancé après 06** (texte « chat » re-rendu, date du gabarit), `kept()` diffère de celui de 06 sans message. | correctif de provenance « chat » v2 : empreinte de `kept` (`cd8a6c23…`) | Comparer l'empreinte de `kept()` à celle de la passe de 06 avant 07, 08 et `reads_at_firings`. |

## `scripts/04_export_rlens.py` et `neuron_lens/lenses.py` (export et chargement)

| ligne(s) | constat | effet | couvert ? | correctif |
|---|---|---|---|---|
| 04 : 20-22 | `fits` (positionnel), `--name` obligatoire, `--half 0/1`, défaut None (V). | `… r-<stem>-L32-dclm.pt --name dclm-llama` ; moitiés : `--name dclm-llama-even --half 0` et `--name dclm-llama-odd --half 1`. | — | — |
| 04 : 24 ; lenses 95-116 | `load_fits(fits, "R")` sans `model_id`, donc pas de contrôle du modèle à l'export. Pas de contrôle de complétude (voir arch). Plusieurs fichiers sont additionnés (V). | — | non | Voir `load_fits`. |
| lenses 119-142 | `save_drowse_lens` : `n_prompts` = documents de la moitié ; `corpus_sha256` = empreinte du corpus **entier**, même pour une moitié ; `split_half` seulement si `half` est None ; modèle = `meta["model"]` (V). | La provenance d'une moitié porte l'empreinte du tout. Le dossier est `data/lenses/<name>/` (Drowse y écrit `local/r` : paths 7-9, AGENTS) (V pour le dossier, D pour le format interne). | non | À consigner. |
| 04 : 28-31 | Imprime l'écart entre moitiés de l'ajustement **entier**, même avec `--half`, en `.2f` (V). | — | — | — |
| pyproject | `drowse = ["drowse.ai>=6.0.0"]`, extra optionnel. Pas de fichier de verrou dans le dépôt (V). | Version résolue à l'installation, donc non figée. Le comportement de `load_local_lens` (correspondance de l'identifiant de modèle, type de `.jacobians`, couche 31 absente ou identité) n'a pas été lu (D). | non | Épingler une version exacte et consigner son empreinte ; lire `drowse.lens.store` et `jlens` sur la machine. |
| lenses 37-45, 90-92 | `R:<nom>` → `merge([load_r_lens(model, nom)])`. Si Drowse ne trouve rien, `FileNotFoundError` (V). `merge` rend `JacobianLens(jac.get("out"), mid=…)`, donc `.jacobians` = la cible `out` (D). | `R:dclm-llama` exige `data/lenses/dclm-llama/`, écrit par 04, et le même identifiant de modèle que celui de 02. | non | — |
| lenses 85-89 | `fit:<stem>[@mid]` lit directement `data/fits/<stem>.pt` (deux moitiés, sans Drowse) (V). | Autre voie que `R:` pour la lentille entière ; pas de moitiés. | — | — |
| lenses 81-84 | `J` : Qwen seulement au commit. | — | **oui** : correctif des lentilles de Neuronpedia v2 (`J`, `npJpp`, `npR`, garde de format) | — |

## `scripts/05_act_corpus.py`

| ligne(s) | constat | effet | couvert ? | correctif |
|---|---|---|---|---|
| 52 | `--docs` par défaut `dclm=4000,zh=1000,code=1000,chat=1000` (V). La publication a 40 000 / 8 000 / 8 000 / 8 000 (provenances suivies : `n` = 40000, 8000, 8000, 8000) (V). | Passer `--docs dclm=40000,zh=8000,code=8000,chat=8000`. | **oui**, argument écrit dans le correctif de provenance « chat » v2 | — |
| 33, 68, 70-72 | `DCLM_SKIP = 1000` **écrit en dur**. L'indice `i` du flux compte toutes les lignes, vides comprises (V). | Indépendant du `--docs` de 01 : si 01 prend plus de 1 000 lignes, chevauchement sans message. | non | Assertion `DCLM_SKIP == provenance["rows"][1]` de `dclm.provenance.json`. |
| 60-66 | Révision : `act-<tranche>.provenance.json` s'il existe (suivis pour dclm, zh et code ; pour « chat », par modèle). Sinon, pour dclm, `dclm.provenance.json`. Sinon la **dernière** révision (V). | Sans le fichier « chat » de Llama, on prendrait la dernière révision. | **oui** : correctif de provenance « chat » | — |
| 76-77 | « chat » : `apply_chat_template(messages, tokenize=False)` si `tok.chat_template` (V). Le texte commence par `<|begin_of_text|>` et contient l'en-tête système « Cutting Knowledge Date … Today Date … » (D, gabarit non lu ici). | Double jeton de début (via `_rows`) ; une vingtaine de jetons d'en-tête identiques dans chaque conversation, avant le dialogue (D). | signalé (correctif de 06 v3 § 3, provenance « chat » v2), non corrigé | À constater ; voir 07. |
| 81 | Lignes vides écartées (`text.strip()`) ; `strip_header` du code peut tout retirer (V). | Voir la formule des lignes de DCLM. | — | — |
| 85-91 | **Réécrit** les fichiers JSONL et les provenances, dont celles suivies dans git (V). | Comparer avec `git show` avant la passe. | **oui** (ordre écrit dans le correctif de provenance) | — |

## `scripts/07_drivers.py`

| ligne(s) | constat | effet | couvert ? | correctif |
|---|---|---|---|---|
| 74-75 | `--batch` 64 ; `--device` cuda sinon mps (V). | — | — | — |
| 46-48, 51-57 | Documents : pour dclm 4, code 2, chat 2, `lens_docs(act_file, tok, 4k, 128, 128)[:k]`, donc parmi les 4k premières lignes celles d'au moins 128 jetons. Sans `full`, au plus 4k lignes regardées. Coupe à `AT+1+AFTER` = 41 jetons. Le jeton remplacé est à la position 24 (V). | Si moins de k lignes ont 128 jetons, D (nombre de documents) diminue **sans message**. Pour Llama, dans les 2 documents « chat », la position 24 tombe dans l'en-tête du gabarit (`<|start_header_id|>user…`, D), alors qu'elle tombe dans le message chez Qwen. Les pilotes de Llama ne sont donc pas mesurés dans le même cadre. | non | Assertion `len(rows) == k` ; décider pour « chat » (constater ou décaler AT), écart à écrire. |
| 60-63 | `randperm` avec la graine 0 : ordre de balayage, départage des égalités (V). | — | — | — |
| 80, 115 | `attn_implementation="eager"`, `out[1]` = poids d'attention (D pour `LlamaAttention` dans transformers 5). | Têtes seulement. | — | — |
| 62, 129-130 | Jetons balayés = `kept()`, qui contient le jeton de début pour Llama (D). | Jeton de début inséré en position 24 : activations possiblement massives, donc risque de dominer les listes de pilotes (D). | non | À constater (rang du jeton 128000 dans `drivers_ids`). |
| 138-147 | Écrit `data/catalog/<stem>/neurons/drivers/LXX.parquet` et `heads/drivers.parquet` (V). | Lu sans condition par `reads_at_firings` (146). | — | — |

## `scripts/08_reads.py` (neurones)

| ligne(s) | constat | effet | couvert ? | correctif |
|---|---|---|---|---|
| 311-313 | `--parts` par défaut `neurons,heads` ; `--layers` a-b (tout par défaut) ; `--device` mps sinon cuda (V). | Passer `--parts neurons` : la partie « têtes » échoue sur Llama à `arch.qk` (poids `q_norm` absents, donc `KeyError` dans `weights.tensors`) (V pour le code, D pour l'échec). | non (le correctif de 06 v3 § 2 le dit) | — |
| 94 | `R_FIT, S_FIT = arch.fits(MODEL)` à l'import (V). | Exige les deux ajustements au nom exact ; sinon « hub » puis 404 (bruyant). Ajustement partiel accepté sans message. | non | Voir arch et `load_fits`. |
| 116-117 | Quatre `arch.lens` : chacun recharge le fichier entier (V). | Mémoire vive d'environ 10 Go au pic par appel (D) ; aucune incidence sur le résultat. | — | — |
| 126 | `lobe_signs` lit `neurons/acts/LXX.parquet` (`neg_lobe`), écrit par 06 (V). | Dépendance à 06. | — | — |
| 137, 145 | Couche 31 : `J_out[31]` n'existe pas, d'où `None`, c'est-à-dire la lentille des logits (identité, exacte par définition) (V). | — | — | — |
| readout 12-14 | `rms_norm_columns(eps=1e-6)` écrit en dur ; Llama a `rms_norm_eps = 1e-5` (D pour la valeur de la configuration) (V pour le code). | Sans effet sur les rangs ni sur les corrélations par ligne. Effet possible sur les probabilités `_val` et sur les z inter-colonnes (`*_z`, et `mean_z` de `reads_at_firings`) si ‖J w‖²/d est comparable à 1e-6 (D, ampleur non évaluée). | non | Option : passer `text_config(MODEL).rms_norm_eps` ; écart à la publication, à décider. |
| 109, 115 | Désenchâssement et plongements des jetons gardés en fp16 (V). | — | — | — |

## `scripts/checks/lens_compare.py`

| ligne(s) | constat | effet | couvert ? | correctif |
|---|---|---|---|---|
| **29** | `MODEL = "Qwen/Qwen3-8B"` **en dur** : tokeniseur (41), poids (45), lentilles (50) (V). En revanche `kept()` (46) suit `NEURON_LENS_MODEL` (V). | Avec la variable sur Llama : identifiants gardés de Llama appliqués aux 151 936 lignes de `lm_head` de Qwen, sans erreur (indices < 151 936), et d = 4 096 des deux côtés. `R:…` échoue probablement dans Drowse (D), `fit:` échoue (contrôle du modèle) ; mais `logit` et `J` donneraient un résultat **faux sans message**. | non | `from neuron_lens.catalog import MODEL` à la place de la ligne 29. |
| 35 | `--layers` par défaut `2,8,14,20,26,32` (V). | La couche 32 n'existe pas, d'où `KeyError` dans `tensors` (V pour le code). La couche 31 avec `R:` donne `m[31]`, sans doute `KeyError` (cible `out` 0..30 ; D selon le type Drowse). | non | Passer `--layers` explicitement, dans 0..30. |
| 34 | `--lenses` par défaut `logit,J,R:dclm` (V). | Passer `R:dclm-llama-even,R:dclm-llama-odd` (plus d'autres au besoin). | — | — |
| 39 | Périphérique : mps sinon **cpu** (V). | Sur la machine louée : processeur central, avec produits fp16 (readout 40). Lent (plusieurs heures possibles, D). | non | `torch.device("cuda" if torch.cuda.is_available() else …)`. |
| 46-47, 58 ; readout 23-44 | `read(sgn*wd, unembed[kept] fp16, gamma, J)`, k = 10 : pour chaque neurone (colonne brute de `W_down`) et chaque signe, les 10 premiers jetons parmi `kept()` (V). | Définition de l'accord : ligne 75, part des 2f lignes (neurones × 2 signes, **pas** les pôles du catalogue ni les lobes) dont le premier jeton est le même ; ligne 76-77, recouvrement moyen des 10 premiers / 10. `kept()` vient de 03. | — | — |
| 57 | `m[layer]` sur la lentille Drowse (cible `out`) (V pour l'appel, D pour le type). | — | — | — |
| 40, 79, 43 | `random.seed(--seed=0)` ; tirage seulement si `--samples > 0` ; `KNOWN` = neurones de Qwen (V). | Garder `--samples 0`. | — | — |
| 60-78 | Rien n'est écrit : sortie standard seulement, `.2f` ou `.3f` (V). | Pas de recalcul non arrondi sans relance. | — | Rediriger la sortie et la sceller ; option : écrire les fractions brutes. |

## `scripts/checks/causal_lens.py` (`score`, et `measure` pour les contextes)

| ligne(s) | constat | effet | couvert ? | correctif |
|---|---|---|---|---|
| 381 | `--lenses` par défaut `logit,hub` hors Qwen (V). | Passer `--lenses logit,J,npJpp,npR,R:dclm-llama`. | `npJpp` et `npR` : oui (correctif des lentilles de Neuronpedia) ; `R:dclm-llama` : non (Drowse et 04) | — |
| 271 | Lit `data/causal/<stem>-causal.pt` (V). | — | **oui** : correctif de graine (`causal_path`, garde de la graine) | — |
| **277** | Périphérique : mps sinon **cpu**. `--device` est **ignoré** par `score` (V). | Calcul en fp32 sur processeur central ; correct mais lent. | non | Lire `args.device`. |
| 274, 278 | `nv = len(tok)` ; masque = `counts[:nv] >= 5`, qui **n'est pas** `kept()` (jetons « � » non retirés) (V). | Ensemble de jetons différent de celui de 08 et de `lens_compare` ; jeton de début compris pour Llama (D). | non | À consigner. |
| 284 ; lenses 37-45 | `R:dclm-llama` → Drowse, dossier `data/lenses/dclm-llama/` (V). Les moitiés se notent aussi : `R:dclm-llama-even,R:dclm-llama-odd` (exemple de la ligne 39) (V). | — | — | — |
| 303 | `lenses[s].get(layer)` : couche absente → `None`, c'est-à-dire la lentille des logits, **sans message** (V). Couche 31 : R s'arrête à 30, donc logits = identité exacte pour R (V pour l'intention, D pour le type Drowse). | Toute couche manquante d'un format inattendu passe pour des logits. | partiel (la garde du correctif des lentilles couvre `J`, `npJpp` et `npR`, pas `R:`) | Arrêt si `get(layer)` est None pour `layer < 31`. |
| 286, 296-299 | Neurones aléatoires reconstruits avec `random.Random(0)`. Témoin = pioche voisine (`roll(1)`) dans le groupe aléatoire (V). | — | graine : oui | — |
| 309-316 | n par (couche, cible, lentille) = pôles aléatoires gardés : pilotage, les 2 × `per_layer` (64) pôles moins les lignes nulles ; ablation, les pôles avec au moins un contexte déclenché. n n'est ni imprimé ni écrit (V). | — | non | Imprimer `k.sum()`. |
| 325 | Seuil = quantile 0,99 du témoin, regroupé sur **toutes** les couches, par (cible, lentille) (V). | À la couche 31, `J`, `npJpp` et `npR` valent les logits et entrent dans le regroupement. | dit dans le correctif des lentilles | — |
| 360-368 | Résumé `data/summary/causal_lens_[<tag>_]<stem>.{log,json}` **écrasé** à chaque appel de même étiquette ; JSON arrondi à 4 décimales (362, 367) ; journal à 2 décimales ; r par pôle non sauvé (V). | Pas de recalcul non arrondi sans relance (déterministe, processeur central). | non | `--tag` distinct par appel. |
| measure 122 | Contextes de pilotage : `lens_docs(act-dclm.jsonl, tok, 64, 64, 64)[:16]` (V). | Moins de 16 contextes possible sans message ; `meta["contexts"]` le garde. | — | — |

## `scripts/checks/reads_at_firings.py` (neurones)

| ligne(s) | constat | effet | couvert ? | correctif |
|---|---|---|---|---|
| 273-274 | `--parts` par défaut `neurons,heads` ; `--device` mps sinon cuda (V). | Passer `--parts neurons` : les têtes exigent `data/heads/<stem>-token-z.pt`, écrit par la partie « têtes » de 08 (impossible sur Llama). | non | — |
| 67 | `arch.fits` à l'import, comme 08 (V). | — | non | — |
| 277 | Lit sans condition `data/acts/<stem>.pt` (état de 06 : `top`, `tokens`, `doc_start`) (V). | Dépendance à 06. | — | — |
| 143, 146 | Lit sans condition `neurons/acts/LXX.parquet` (`act_top`, `cur_mode`, `next_mode`) et **`neurons/drivers/LXX.parquet`** (`drivers_ids`) (V). | 07 est obligatoire, même pour les tests autres que `read_R`. **08 n'est pas lu** par la partie « neurones » : les lectures sont recalculées depuis les lentilles. | — | — |
| 280-281, 286 | Fusionne un `data/checks/reads_at_firings-<stem>.pt` et un résumé JSON existants. Avec `--parts neurons`, d'anciennes entrées « têtes » sont gardées et réimprimées (V). | Contenu périmé possible sans message. | non | Partir de dictionnaires vides, ou imprimer ce qui est repris. |
| 162-168, 84-107 | Définition de `read_S`, voir la liste séparée ci-dessous (V). | — | — | — |
| 133, 149 | Un seul générateur avec la graine 0 pour toutes les couches, tiré dans l'ordre des couches (V). `randperm` n'exclut pas les points fixes : environ un pôle par moitié est « apparié à lui-même » (V). | — | — | À consigner. |
| 152, 159 | Couche 31 : `J_out` absent, donc logits (identité) pour `write_R` et `write_orth_R` (V). | — | — | — |
| 289-291 | JSON en flottants complets ; journal `.2f` ; valeurs q par pôle dans `data/checks/…pt` ; z moyens par pôle non sauvés (V). | — | — | — |

**Définition de `read_S`** (lignes 162-168, 84-107, 174-181, V) :
- Direction : `c = read_rows(â, b̂, lobe)`, soit â ± b̂, ou ∓b̂ sur le lobe négatif (lobe lu dans la colonne `neg_lobe` des tables `acts`). Covecteur `cs = c @ K_mid[L]`, normé.
- Table : plongements des jetons gardés, centrés, en fp16. Score du jeton v = ĉs · (e_v − ē).
- z par jeton : moyenne et écart-type sur les 2f pôles, silencieux compris.
- **Numérateur** : somme des z sur les déclenchements utilisables (`val > 0` parmi les 64 premiers documents, et jeton sous le déclenchement dans `kept`). **Dénominateur** : leur nombre. NaN si moins de 3.
- Paire mal appariée : vecteur du pôle `perm[i]` sur les jetons du pôle i, permutation tirée séparément pour les pôles + et pour les pôles −.
- p = (1 + #{nul ≥ stat}) / (1 + #nul), avec le nul = tous les appariés non NaN, silencieux compris.
- **Benjamini-Hochberg** : par couche et par test, sur les pôles non NaN et non silencieux (`act_top` ≥ 0,05) ; q = 1 pour les autres.
- Part rapportée = q ≤ 0,05 sur **les 2f pôles** (silencieux et NaN comptés comme échecs). `_net` = part au-dessus du quantile 0,99 du nul, moins la même part pour le nul, silencieux exclus des deux.

---

## Replis silencieux
1. `02_fit.py` 151-166 : la reprise ignore `rows_sha256`, `docs` et `dim_batch`. Un corpus changé sous le même nom est mélangé, puis l'empreinte est réécrite. (V)
2. `load_fits` (lenses 95-116) et `arch.fits` : un ajustement **incomplet** (`next_doc < docs`) est exporté et lu sans message. (V)
3. `arch.fits` (arch 299-303) : un des deux fichiers absent, ou un suffixe `-T`/`-s`, fait passer à « hub ». Bruyant dans 08 et `reads_at_firings` (404), mais 06 rééxécuté écrirait la table des têtes sans `out_R_z`. (V, couvert pour 06)
4. `causal_lens.py score` 303 : couche absente d'une lentille → lentille des logits. (V)
5. `lens_compare.py` 29 : modèle Qwen en dur avec `kept()` de Llama ; résultat faux sans erreur pour `logit` et `J`. (V)
6. `corpus.lens_docs` (22-34) et ses appelants (02 ligne 132, 07 ligne 56, `measure` ligne 122) : moins de documents que demandé, sans message. (V)
7. 01 lignes 31-34 et 05 lignes 60-66 : provenance absente → dernière révision du jeu. (V)
8. 05 ligne 33 : `DCLM_SKIP = 1000` fixe, quel que soit le `--docs` de 01. (V)
9. `reads_at_firings` 280-286 : anciennes entrées « têtes » reprises. (V)
10. `score` 277 et `lens_compare` 39 : processeur central choisi sur une machine cuda, `--device` ignoré (lenteur seulement). (V)
11. 03 relancé après 06 : `kept()` change sans contrôle. (D)
12. `rules._check_norm` (96) : tirage sans graine (contrôle seulement). (V)

## Dépendances d'ordre entre étapes
- 01 → 02 (`data/corpus/dclm.jsonl`). La provenance de 01 ne sert à 05 que si `act-dclm.provenance.json` manque (il est suivi dans git).
- 02 (R **et** S, noms `r-<stem>-L32-dclm.pt` et `s-<stem>-L32-dclm.pt`, sans `--full-length` ni `--shard`) → 04, 08, `reads_at_firings`. Une relance de 06 après 02 utiliserait aussi l'ajustement local.
- 05 (avec la provenance « chat » de Llama déposée) → 03 → 06 → 07 → `reads_at_firings`.
- 03 → 06, 07, 08, `lens_compare` (oui, `kept()` exige `data/token_counts-<stem>.pt`) et `score` (ligne 278).
- 06 → 08 (`neg_lobe`), `measure`, `reads_at_firings` (état `.pt` et tables `acts`).
- 07 → `reads_at_firings` (lu sans condition).
- 08 → seulement la partie « têtes » de `reads_at_firings`. La partie « neurones » n'en dépend pas (le docstring de `reads_at_firings` dit « after 07 and 08 »).
- 04 (`--name dclm-llama`, `dclm-llama-even --half 0`, `dclm-llama-odd --half 1`, Drowse installé) → `lens_compare` et `score`.
- `measure` → `score`.

## Mesures de stabilité et recalcul non arrondi
- Imprimées en `.2f` : 02 lignes 185-188 et 04 lignes 28-31.
- Recalcul sans arrondi depuis `data/fits/<…>.pt` : `Accumulator.from_state(saved["state"]).split_half(cible)`, avec la formule de transport 64-72 (sommes par moitié et `n_docs`).
- L'export entier transmet aussi `split_half` à Drowse (lenses 135-136 ; format non lu) ; les moitiés n'en portent pas.
- `lens_compare` n'écrit rien.

## Lignes de DCLM (révision `2fa015e4044ec442a0734e89658cdcc538d10dd4`, flux `train`)
- **Corpus d'ajustement** : `dclm.jsonl` ligne i = ligne i du flux, pour i ∈ [0, 1000) (01, lignes 37-40). Documents ajustés = ces lignes, sauf celles de moins de 18 jetons (jeton de début compris), coupées à `text[:4000]` et à 128 jetons. Moitié = rang parmi les documents retenus, modulo 2.
- **Corpus d'activations** (05, lignes 68-83) : `act-dclm.jsonl` ligne j = r_j, le j-ième indice (j à partir de 0) de {i ≥ 1000 : `text_i.strip()` non vide}, pour j ∈ [0, N), avec N = 40 000 (`--docs dclm=40000`). **Si aucun texte n'est vide, r_j = 1000 + j, soit les lignes [1000, 41000).** Le contrôle se fait par la liste `ids` de la provenance (40 000 identifiants ; le premier est `<urn:uuid:786a455d-…>`).
- **Passe d'activations (06)** : ces lignes, sauf celles de moins de 9 jetons, coupées à 256 jetons.
- **Contextes de `measure`** : les 16 premières lignes j ∈ [0, 64) qui ont au moins 64 jetons, coupées à 64.
- **Pilotes (07)** : les 4 premières lignes j ∈ [0, 16) qui ont au moins 128 jetons.
- **Déclenchements les plus forts de `reads_at_firings` et ablations de `measure`** : les documents de toutes les tranches. Pour DCLM, l'indice de document donne (tranche 0, ligne j) par `docs.parquet`, puis la ligne du flux r_j.

Fichiers lus : `/home/user/stdlogits/neuron-lens/` (scripts nommés, `neuron_lens/*.py` concernés, `pyproject.toml`, provenances de `data/corpus/`) et les cinq notes de correctifs dans `/home/user/carnet/nl/docs/notes/neuron-lens-v1/correctifs/`.
