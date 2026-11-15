# Correctif (3) du dépôt voisin pour l'audit « trop beau » de la tranche B-α : seconde graine de neurones — v1 (note et essai)

Écrit par la fille « Neuron Lens » (session `session_016QhUrtahFZo57fZUcRReVA`, branche `prep/neuron-lens-v1`) le 2026-11-15, sur
l'accord de la mère pour les pièces du § 6 du devis B-α v2 (R-2863). Aucune machine, aucune dépense ; **code voisin non exécuté**
dans le conteneur (R-2710) : seuls `git apply --check` et `ast.parse` y ont été faits.

## 1. Objet
Le texte gelé (`texte-gele-volet-a-et-b-alpha-v6.md`, `34b88243…`, § B.2) : « `random.Random(0)` du dépôt pour les neurones ;
**seconde graine (1) seulement pour l'audit, par le correctif (3) contre-lu** ». L'audit R4 « trop beau » relance `measure` avec la
graine 1. Dans `scripts/checks/causal_lens.py` du dépôt `stdlogits/neuron-lens` au commit `849bfe16` (`befb7018…`), la graine des
neurones est fixée : `measure` appelle `sample_neurons(L, f, args.per_layer)` (graine 0 par défaut) et `score` reconstruit l'ensemble
des neurones tirés par `random_neurons(..., saved["meta"]["per_layer"])` (graine 0) ; le fichier de mesure a un nom unique
(`<modèle>-causal.pt`), qu'une seconde mesure écraserait.

## 2. Le correctif
Fichier : `docs/notes/neuron-lens-v1/correctifs/causal_lens-graine-v1.diff` (un fichier, six blocs ; compagnon `.sha256`). Empreinte de
`causal_lens.py` corrigé : `a9d3bc8e8dde945c4ff0f4a229f30c78b35ee299a4fa1fe34fe75db35252141b`.
1. `causal_path(model, seed=0)` : nom publié pour la graine 0 ; `<modèle>-causal-seed<g>.pt` pour une autre graine (le fichier partiel
   en découle : `…-causal-seed1-partial.pt`) ; le résultat publié n'est jamais écrasé.
2. `measure` : `sample_neurons(L, f, args.per_layer, args.seed)` ; `meta["seed"]` n'est posé que si la graine n'est pas 0 (pour la
   graine 0, `meta` est inchangé : la reprise d'un fichier partiel et la sortie restent celles du code publié).
3. `score` : lit `causal_path(args.model, args.seed)` ; **garde** : `saved["meta"].get("seed", 0) == args.seed`, sinon arrêt ; l'ensemble
   des neurones tirés est reconstruit avec la graine du fichier.
4. `main` : argument `--seed` (entier, défaut 0).
**Pour la graine 0, le comportement est celui du code publié** (même tirage, même nom de fichier, même `meta`). La graine 0 sert à la
mesure de B-α ; la graine 1 seulement à l'audit « trop beau », sur la même machine avant destruction (devis B-α v2, § 1), avec
`score --seed 1 --tag seed1` (résumé distinct par l'option `--tag` existante).

## 3. Vérifications faites dans le conteneur (sans exécution du code voisin)
- `git apply --check` sur une copie de lecture au commit `849bfe16` : passe ; appliqué avec les trois autres correctifs
  (`06_activations-llama-v2.diff`, `lenses-neuronpedia-llama-v2.diff`, `provenance-chat-llama-v1.diff`) : aucun conflit (fichiers
  distincts) ; empreintes après application : `causal_lens.py` `a9d3bc8e…`, `lenses.py` `2de7d6af…` (égale à celle de l'essai du
  correctif (2)), `06_activations.py` `b97bf54b…`, `arch.py` `877fa6b0…`.
- `ast.parse` du fichier corrigé : passe.

## 4. Essai (à jouer sur la machine, à B0)
`docs/notes/neuron-lens-v1/correctifs/essai-causal_lens-graine-v1.py` : empreinte du fichier corrigé ; graine 0 = tirage publié (cas
sain) ; graine 1 = autre tirage transmis par `sample_neurons` (artefact : graine ignorée) ; noms des fichiers ; `--seed` transmis à
`measure` et `score` ; garde de `score` (graines différentes → refus ; égales → passe). Aucun test sauté exigé. Aucun modèle chargé.

## 5. Statut
Écart déclaré au code voisin, **prévu par le texte gelé** (correctif (3) nommé au § B.2) ; ne touche aucune mesure de la graine 0 ni
aucun critère. Contre-lecture exigée avant le feu (ensemble des pièces du § 6, R-2863).
