# Essai des crochets de pilotage et d'ablation de `causal_lens.py` sur un Llama miniature — pièce 2 du § 6 du devis B-α v2 — v1

Écrit par la fille « Neuron Lens » (session `session_016QhUrtahFZo57fZUcRReVA`, branche `prep/neuron-lens-v1`) le 2026-11-15, sur
l'accord de la mère (R-2863). Aucune machine, aucune dépense. **Code voisin non exécuté dans le conteneur** (R-2710).

## 1. Ce que l'essai doit établir (texte gelé v6, § B.1 ; devis v2, m4)
« Essai écrit et contre-lu des crochets de pilotage et d'ablation de `causal_lens.py` sur un Llama miniature (norme de la cible non
nulle, pôle témoin différent du pôle) », à B0, avant le corpus et toute passe sur la carte.

## 2. Pièces
| fichier | rôle | où il tourne |
|---|---|---|
| `essai-crochets-causal_lens-llama-v1.py` | l'essai : le **vrai** `measure` corrigé (`a9d3bc8e…`) tourne de bout en bout sur un `LlamaForCausalLM` de 3 couches tiré au hasard ; ses cibles sont comparées à une référence calculée par un autre mécanisme | **machine louée, à B0** |
| `pre-essai-crochets-harnais-v1.py` | pré-essai de **notre** harnais : imite les deux mécanismes de `measure` (notre code, recopié de la lecture, non importé) et vérifie que les tolérances acceptent le cas sain et rejettent les artefacts | conteneur |
| `pre-essai-crochets-harnais-v1.txt` | sortie du pré-essai | — |

Commande sur la machine (dans l'arbre voisin à `849bfe16`, quatre correctifs appliqués) :
`NEURON_LENS_ROOT=$PWD NEURON_LENS_MODEL=meta-llama/Llama-3.1-8B-Instruct python -m pytest -q -rs <chemin>/essai-crochets-causal_lens-llama-v1.py`.
Aucun test sauté ; tout échec ou test sauté = arrêt de montage (rien n'est loué de plus : la machine est détruite selon la commande).

## 3. Montage
- Modèle : `LlamaConfig` (vocabulaire 96, largeur 32, 64 neurones par couche, 3 couches, 4 têtes, 2 têtes clé-valeur, `initializer_range`
  0,2 pour des effets bien au-dessus de l'arrondi float16), float32, processeur ; graine `SeedSequence(entropy=20261114, spawn_key=(2,))`
  (branche « B-α, essai des crochets », texte gelé § B.2) = 3015958266. Aucun poids téléchargé, aucun accès au Hub.
- Entrées de `measure` remplacées : modèle, tokeniseur, `catalog_top` (tables `acts` synthétiques : `act_top` > 0, quatre documents de
  tête par pôle dont le dernier sans tir, un tir en dernière position d'un document), `documents` (six documents de 18 à 40 jetons),
  `lens_docs` (trois contextes de 24 jetons), `CAUSAL` (dossier temporaire), `arch.is_gemma4` (faux) et `arch.cap` (identité : Llama
  n'a pas de plafonnement final ; la vraie fonction lirait la configuration sur le Hub). Arguments : 2 neurones par couche (tirage
  publié, graine 0), `cond_batch` 3 et `ctx_batch` 5 (lots incomplets essayés), `save_minutes` très grand.
- `measure` demande le bf16 (vérifié) ; le modèle miniature reste en float32 : l'essai porte sur les crochets, pas sur la précision.

## 4. Comparaisons (R5 : cas sain et artefacts)
- **Pilotage** : `measure` ajoute `s·α·W_down[:, n]` à la sortie de la couche à portes (crochet d'après), conditions en lot avec une
  ligne témoin non pilotée ; la référence ajoute `s·α` à l'activation du neurone `n` à l'entrée de `down_proj` (crochet d'avant),
  condition seule, logits du modèle complet. Cas sain : écart ≤ 2·10⁻³ de l'échelle, échelle > 10⁻⁴ (**norme de la cible non nulle**).
  Artefacts rejetés (écart > 2·10⁻² de l'échelle) : signe opposé, neurone voisin, autre couche, poussée à toutes les positions (sauf à la
  dernière couche, où elle est indiscernable par construction — trouvé au pré-essai, écart 0 — : rien ne mélange les positions après
  la dernière couche à portes ; l'essai vérifie que l'artefact est essayé à au moins une autre couche).
- **Ablation** : `measure` met à zéro l'entrée de `down_proj` au neurone et à la position, lignes propres et ablatées côte à côte,
  complétées à droite ; la référence met à zéro la sortie de `up_proj` au même endroit, document seul, sans complément. Cas sain :
  `ablate_pos`, `ablate_win`, `dlogp_next` (nan si aucun jeton suivant), documents et positions consignés, document sans tir sauté.
  Artefacts rejetés : position voisine, neurone voisin.
- **Pôle témoin différent du pôle** : les deux pôles d'un neurone donnent des cibles distinctes (pilotage et ablation) ; la dose 4×
  n'est pas la dose 1× ; toutes les cibles ont une norme non nulle (une ligne témoin pilotée, ou des lignes propres ablatées, les
  annuleraient) ; le fichier final n'a ni `seed`, ni `done`, ni fichier partiel restant.

## 5. Pré-essai fait dans le conteneur (notre code seul)
Sortie (`pre-essai-crochets-harnais-v1.txt`) : graine 3015958266 ; 0 échec sur 24 conditions de pilotage et 12 couples (couche, pôle)
d'ablation ; écart relatif maximal du cas sain **7,6·10⁻⁴** (tolérance 2·10⁻³) ; séparation minimale des artefacts **0,32** (seuil
2·10⁻²) ; une imitation fautive (signe opposé) est refusée. Environnement du conteneur : torch 2.14.1, transformers 5.18.0, les
versions du manifeste du volet A (`runs/20261114-165239-neuron-lens-volet-a/manifeste.json`). Ce pré-essai ne prouve rien du code
voisin : il montre seulement que le harnais distingue le sain de l'artefact aux tolérances choisies.

## 6. Statut
À contre-lire avec les autres pièces du § 6 (R-2863). Aucune tolérance ni aucun critère du texte gelé n'est touché.
