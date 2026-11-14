# Correctif daté de `scripts/06_activations.py` (dépôt voisin `stdlogits/neuron-lens`) pour Llama 3.1 8B Instruct — v1

Écrit par la session fille « Neuron Lens » (`session_01QPDgKfBxeeiM3BsxqJgSgf`, branche `prep/neuron-lens-v1`) le
2026-11-14, première version de la différence à 09:50 UTC (`date -u`). Aucune machine, aucune dépense.

## 1. Objet
Au commit `849bfe1678e28becceb1e3864afe5fc8297d02e4` (licence MIT), `scripts/06_activations.py`
(empreinte `151d11963d5c43d6593d2482cc4510bddc825b3bc66696be121dc60b8b488035`, identique à la copie archivée du lecteur
`docs/sources/neuron-lens-lecture-20261113/depot-neuron-lens/scripts-06_activations.py.txt` sur `main`) pose, dans
`Collector.hooks` (ligne 287), un crochet sur `self_attn.q_norm` et `self_attn.k_norm` sans garde. Llama 3.1 n'a pas ces
normes : la passe d'activations s'arrêterait sur `AttributeError` dès la première couche.

## 2. Le correctif
Fichier : `docs/notes/neuron-lens-v1/correctifs/06_activations-llama-sans-qk-norm-v1.diff` (empreinte au compagnon `.sha256`).

1. `Collector.hooks` : les normes `q`, `k`, `v` sont lues par `getattr(…, None)` ; une norme absente ne reçoit pas de crochet.
   Les statistiques QK (`q`, `q_r`, `q_m`, `k_r`, `k_m`) restent alors à zéro ; elles ne servent qu'à la partie « têtes » de
   `08_reads.py`, **hors périmètre** (plan v1 § 2 ; `arch.qk` exige de toute façon ces normes).
2. `collect` : si une couche n'a pas `q_norm` et `k_norm`, la passe est marquée `meta["qk_norm"] = False`, pour qu'aucune
   lecture des têtes ne prenne ces zéros pour des mesures. La clé n'est posée que dans ce cas : **pour Qwen3 et Gemma 4,
   `meta` est inchangé** (la reprise d'une passe existante, qui compare `meta`, n'est pas cassée).
3. Pour Qwen3 : mêmes crochets, dans le même ordre (`q`, `k`, puis `v` s'il existe) ; comportement identique. Seule
   différence de comportement possible : un `v_norm` présent mais valant `None` est désormais sauté au lieu de faire échouer
   la passe (cas qui n'existe ni dans Qwen3 ni dans Llama).

Ce qui reste hors du correctif et n'est pas requis par la tranche B-α : `08_reads.py` partie « têtes » ; `arch.qk`.

## 3. Ce qui a été vérifié sans exécuter le code voisin
- `git apply --check` de la différence sur un clone propre au commit `849bfe16` : réussi.
- Analyse syntaxique du fichier corrigé par `ast.parse` (aucune exécution) : réussie ; empreinte du fichier corrigé
  `50d2b52090add67429ac7ea9479dda878e75ce9266e2a44a1bdd8744fdcf6bb1`.
- Lecture : `neuron_lens/arch.py` (`layout_of`, `attn_norm`, `mid_norm`, `head_write`, `attn_scale`) traite Llama par la
  branche « non Gemma » ; `Collector.attention` lit les poids d'attention (`out[1]`), rendus par l'attention « eager » de
  Llama ; aucune autre lecture d'une pièce absente de Llama dans les crochets.

**Non vérifié** : l'exécution. L'essai écrit (`essai-06_activations-llama-v1.py`) n'a pas été lancé (refus du classifieur du
13 novembre, non contourné ; R-2685). Il passe à l'étape B0, sur la machine louée, après la ligne de GO, le feu de la mère et
la règle de Lazar sur l'exécution du code voisin. Tant qu'il n'a pas réussi, la passe d'activations de B-α ne part pas.

## 4. Essai écrit (R5 : cas sain et artefact)
`essai-06_activations-llama-v1.py` (pytest, modèles miniatures aléatoires, processeur, aucun poids téléchargé) :
Llama miniature corrigé (passe aboutie, statistiques QK nulles, neurones et têtes comptés, 5 crochets par couche) ; Qwen3
miniature (non-régression : statistiques QK non nulles, 7 crochets par couche) ; marque `qk_norm` ; artefact : le script
original échoue sur le Llama miniature par `AttributeError` sur `q_norm`.

## 5. Contre-lecture
À remplir : sous-agent neuf d'un autre modèle que l'autrice, rapport et traitement des remarques.
