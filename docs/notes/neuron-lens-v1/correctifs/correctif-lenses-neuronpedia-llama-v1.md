# Entrées des lentilles publiques de Llama 3.1 8B Instruct dans `neuron_lens/lenses.py` — correctif v1 (point 2 c)

Écrit par la session fille « Neuron Lens » (`session_01QPDgKfBxeeiM3BsxqJgSgf`) le 2026-11-14 vers 09:55 UTC (`date -u`).
Aucune machine, aucune dépense ; **code voisin non exécuté** (R-2685). **Non contre-lu à ce jour** : à contre-lire avant B0.

## Objet
Au commit `849bfe16`, `load_lens("J", modèle)` lit le fichier de Neuronpedia du dictionnaire `NEURONPEDIA_FILES`, qui ne
connaît que Qwen3-8B ; les lentilles J++ et R publiques de Neuronpedia n'ont aucune entrée. La tranche B-α en a besoin
(texte gelé § 3.6 : témoins J et J++, lentille R publique).

## Le correctif
`docs/notes/neuron-lens-v1/correctifs/lenses-neuronpedia-llama-v1.diff` (compagnon `.sha256`) :
- entrée `meta-llama/Llama-3.1-8B-Instruct` dans `NEURONPEDIA_FILES` (lentille J) ;
- dictionnaire `NEURONPEDIA_EXTRA` : noms de lentille `npJpp` (J++) et `npR` (R publique) pour ce modèle (sans « + » ni
  « : », que `load_lens` interprète) ; à passer à `causal_lens.py score --lenses logit,J,npJpp,npR` ;
- `neuronpedia_lens` : charge le fichier et **refuse** tout format autre que `{"J": {entier: matrice carrée}}` (le format
  supposé, celui du fichier J que le code lit déjà) au lieu de le prendre pour acquis.

Chemins des fichiers : arbre archivé `docs/sources/neuron-lens-lecture-20261113/huggingface/lentilles-neuronpedia-jacobian-lens-arbre.json`
(`main`) ; empreintes de stockage gelées au texte gelé § 3.6. `hf_hub_download` ne compare pas ces empreintes : le script de
course de B0 calcule le SHA-256 de chaque fichier téléchargé et s'arrête à tout écart (liste d'arrêt du texte gelé).

## Vérifié sans exécuter
`git apply --check` sur un clone propre au commit `849bfe16` : réussi ; fichier corrigé
`20e48fb452309eb1611157ae1bf0fe36c67e8316eba1e4bd8dc79065244cb124`.

## Non vérifié
Le format réel des fichiers J++ et R de Neuronpedia (clés, couches couvertes, type des indices de couche) : en B0, par
lecture d'un fichier ; si le format diffère, le refus de `neuronpedia_lens` arrête la tranche et l'écart est écrit avant
toute lecture adaptée.
