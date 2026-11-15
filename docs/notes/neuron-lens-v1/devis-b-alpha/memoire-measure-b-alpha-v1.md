# Mémoire de pointe de `measure` et des audits de B-α sur une RTX 4090, avec `--ctx-batch 16` — estimation v1

Écrite par la fille « Neuron Lens » le 2026-11-15, condition 1 de la décision R-2901 (option (a) : même carte, `measure --ctx-batch 16`,
même valeur pour l'audit « trop beau », écart de lot déclaré). Sources : `scripts/checks/causal_lens.py` (copie empreintée `befb7018…`,
`docs/sources/neuron-lens-v1-devis-20261113/reference-publiee/scripts-checks-causal_lens.py.txt` ; le correctif (3) ne touche pas la
mesure) ; configuration de Llama 3.1 8B Instruct (largeur 4 096, 14 336 neurones par couche, 32 couches, 32 têtes de requête, 8 de clé et
valeur, vocabulaire 128 256) ; journal de `measure` de la relance (`diag/20261115-102017-neuron-lens-b-alpha/journaux/measure.log`).

## 1. Ce que dit l'échec (mesuré)
« Tried to allocate 896.00 MiB. GPU 0 has a total capacity of 23.57 GiB of which 100.75 MiB is free. […] 21.07 GiB is allocated by
PyTorch, and 1.93 GiB is reserved by PyTorch but unallocated. » 896 MiB = 32 768 × 14 336 × 2 octets : **un tenseur intermédiaire de la
couche à portes** pour 32 768 jetons, soit 128 séquences (2 × `ctx_batch` 64, ligne propre et ligne ablatée) × 256 jetons (documents
coupés à 256 jetons par la passe, `06_activations.py` l. 88 ; `seqs = tokens[d][:pos + 1 + WINDOW]`, l. 218, donc au plus 256). Poids en
bf16 : ≈ 8,03 milliards de paramètres × 2 octets ≈ **14,96 GiB**. Part variable au moment de l'échec : 21,07 − 14,96 ≈ **6,1 GiB pour
32 768 jetons**, soit ≈ 0,19 MiB par jeton (activations des couches, tenseurs de la couche à portes, attention avec masque de
complément, sorties). Hors PyTorch : 23,46 − 21,07 − 1,93 ≈ 0,46 GiB (contexte CUDA).

## 2. Estimation par partie, à la même règle (linéaire en jetons par passe, calée sur l'échec)
| partie | lot | séquences × jetons par passe | jetons | part variable | alloué estimé | marge contre 23,57 GiB (avec 1,93 GiB réservés non alloués et 0,46 hors PyTorch) |
|---|---|---|---|---|---|---|
| pilotage (`cond_batch` 16, défaut, inchangé) | 16 conditions + 1 témoin, × 16 contextes | 272 × 64 | 17 408 | ≈ 3,2 GiB | ≈ 18,2 GiB | ≈ 3,0 GiB — **passé en vrai** (32 couches, 519 s) |
| pilotage : `lsm_chunks` (l. 90, 188) | 768 lignes × 128 256 en float32 | — | — | ≈ 0,9 GiB, libéré à chaque contexte | compris ci-dessus | — |
| ablation, défaut (`ctx_batch` 64) | 64 tâches × 2 lignes | 128 × 256 | 32 768 | ≈ 6,1 GiB | ≈ 21,1 GiB | **< 0 : échec observé** |
| **ablation, `ctx_batch` 16** | 16 tâches × 2 lignes | 32 × 256 | 8 192 | ≈ 1,5 GiB | ≈ **16,5 GiB** | ≈ **4,7 GiB** (≈ 6,6 GiB si les 1,93 GiB réservés sont rendus) |
| ablation, `ctx_batch` 32 (pour mémoire) | 32 × 2 | 64 × 256 | 16 384 | ≈ 3,1 GiB | ≈ 18,0 GiB | ≈ 3,2 GiB |

Contrôle indépendant de l'ordre de grandeur, à `ctx_batch` 16 : tenseurs de la couche à portes 4 × 8 192 × 14 336 × 2 o ≈ 0,9 GiB ;
poids d'attention s'ils sont matérialisés 32 × 32 × 256 × 256 × 2 o ≈ 0,13 GiB ; états cachés et sorties ≈ 0,2 GiB : ≈ 1,2 GiB, du même
ordre que les 1,5 GiB de la règle calée.

## 3. Les autres parties
- **Audit « trop beau »** : `measure --seed 1` avec les mêmes paramètres (et `--ctx-batch 16`) : mêmes pointes que ci-dessus.
- **`score`**, **grandeurs par pôle**, **audit « tout négatif »** (`score` sur Qwen3-8B) : **sur le processeur** (`score` : `mps` sinon `cpu`,
  l. 277 de la copie corrigée ; nos grandeurs : `cpu`) ; mémoire vive, de l'ordre de 10 Go au plus (projection de sortie en float32
  ≈ 2 GiB, trois lentilles en fp16 ≈ 3 GiB, fichier de `measure` ≈ 2 GiB pour Llama, 2,9 Go publié pour Qwen3-8B) contre 64 Go : sans
  objet pour la carte.
- **`06_activations.py`** (fumée et passe) : déjà passés en vrai à leurs défauts (`--batch-docs 32`), 61 min.
- **Aucune autre partie n'a de lot sur la carte** : `measure` n'a que `cond_batch` (pilotage, passé) et `ctx_batch` (ablation). Seul
  `--ctx-batch` est changé.

## 4. Écart déclaré
`--ctx-batch 16` au lieu du défaut 64 (l. 379 de la copie), dans `measure` et dans `measure --seed 1` de l'audit. Le texte gelé (l. 182-184)
fixe « ses défauts publiés (lignes 374 à 377 de la copie) » : `--per-layer`, `--contexts`, `--ctx-len`, `--top-contexts` ; `--ctx-batch`
n'en est pas. Il ne change que le nombre de tâches par passe ; chaque ligne est calculée seule (ligne propre et ligne ablatée côte à
côte, complément à droite sous masque d'attention, positions par défaut), donc les cibles sont les mêmes au bruit numérique du bf16 près
(forme du lot).

## 5. Réserve
L'estimation suppose la part variable linéaire en jetons par passe et le même schéma de réservation que pendant la relance ; elle
n'est pas mesurée à `ctx_batch` 16. Si l'ablation échouait encore par mémoire : destruction immédiate, rapport ; aucune relance sans mot de
la mère.
