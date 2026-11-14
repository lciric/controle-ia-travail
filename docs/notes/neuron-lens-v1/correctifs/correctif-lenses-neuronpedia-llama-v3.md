# Lentilles publiques de Llama 3.1 8B Instruct dans `neuron_lens/lenses.py` — correctif v2, note et essai v3 (point 2 c)

Écrit par la session fille « Neuron Lens » (`session_01QPDgKfBxeeiM3BsxqJgSgf`) le 2026-11-14 vers 10:15 UTC (`date -u`) ; note et
essai v3 vers 10:27 UTC. **La différence ne change pas** (`lenses-neuronpedia-llama-v2.diff`, `616434bc98394c191e00ae02cb9342317e7fbdaea780d771224babc45c12a3bc`) ;
la note v2 (`ae20219e95f701d33d37a427a8b2d3fb14145e70c70c1bc7a2f83c4810707802`) et l'essai v2 sont archivés tels quels.
**Remplace la v1** (`correctif-lenses-neuronpedia-llama-v1.md`, `lenses-neuronpedia-llama-v1.diff`, archivés) après la contre-lecture 2
des correctifs (`docs/notes/neuron-lens-v1/contre-lectures/contre-lecture-2-correctifs-v2.md`, remarques 8 à 14). Aucune machine,
aucune dépense ; code voisin non exécuté (R-2685).

## Objet
Au commit `849bfe16`, `load_lens("J", modèle)` ne connaît que Qwen3-8B ; les lentilles J++ et R publiques de Neuronpedia n'ont aucune
entrée. La tranche B-α en a besoin (texte gelé : témoins J et J++, lentille R publique). Dans `causal_lens.py score`,
`lenses[s].get(layer)` rend `None` pour une couche absente, ce qui revient à la **lentille des logits sans aucun message** : tout
défaut de format doit donc arrêter, pas passer.

## Le correctif
`lenses-neuronpedia-llama-v2.diff` ; fichier corrigé `2de7d6afe63bc398e17f4ff93ae7b7acdcc3a330e91c728df88bef338008b3e4` :
- `NEURONPEDIA_FILES` : entrée `meta-llama/Llama-3.1-8B-Instruct` (J) ; `NEURONPEDIA_EXTRA` : `npJpp` (J++) et `npR` (R publique) ;
  à passer à `score --lenses logit,J,npJpp,npR` (le défaut `logit,hub` échouerait sur Llama) ;
- `NEURONPEDIA_SHA256` : empreintes de stockage des trois fichiers de Llama (arbre archivé du lecteur), **vérifiées sur le fichier du
  cache réellement lu**, avant `torch.load` ;
- `neuronpedia_lens` : refuse tout fichier qui n'est pas `{"J": {0..n−1: matrices carrées de même forme}}` (couche manquante,
  décalage, clé autre, indices non entiers) ; imprime les couches et les **autres clés** du fichier ;
- la lentille `J` de Llama passe aussi par ce contrôle ; **Qwen3-8B inchangé** (ancien chargement gardé) ;
- `npJpp` ou `npR` demandés pour un autre identifiant de modèle : `KeyError` explicite (au lieu d'une chute dans la fusion Drowse).
  `NEURON_LENS_MODEL` doit valoir l'identifiant exact `meta-llama/Llama-3.1-8B-Instruct` ;
- docstring de `load_lens` mise à jour.

## Conséquence pour la lecture (à porter au texte gelé)
Les trois fichiers font 31 matrices 4 096 × 4 096 (taille de l'arbre : 31 × 4 096² × 2 octets plus quelques kilo-octets) : la
couche 31 n'y est pas, par construction (même chose pour le fichier J de Qwen3-8B, 35 matrices pour 36 couches). À la couche 31,
`J`, `npJpp` et `npR` sont donc **exactement** la lentille des logits dans `score` : ce ne sont pas des mesures de lentille. Elles
entrent dans le centile commun aux couches (`pass`), comme dans la référence publiée, construite de même.

## À B0, avant toute lecture de résultat (liste d'arrêt du texte gelé)
- le correctif exige des couches **contiguës `0..n−1`** (n quelconque) ; n = 31 est lu sur la ligne imprimée pour chacun des trois
  fichiers, sinon arrêt ;
- lecture des `config.yaml` et `CREDIT.md` des trois dossiers : sens de la clé « couche l » (sortie de la couche l, comme le suppose
  le code voisin), nombre de documents ; toute autre convention = arrêt et écart écrit ;
- les autres clés imprimées sont consignées.

## Vérifié sans exécuter
`git apply --check` sur le clone au commit `849bfe16` : réussi ; `ast.parse` : réussi ; `hashlib` déjà importé par le fichier.

## Essai écrit (R5), non exécuté
`essai-lenses-neuronpedia-v3.py` : cas sain ; sept formats refusés (couche manquante, couches décalées, autre clé, formes mêlées,
indices non entiers, « J » vide, matrice non carrée) ; empreinte fausse refusée ; `npR` sur Qwen3 refusé ; `J` de Llama passe par la
garde, `J` de Qwen3 n'y passe pas ; cohérence des noms et des empreintes de Llama.

## Traitement de la contre-lecture 2 (correctif B)
| remarque | traitement |
|---|---|
| 8 J de Llama non contrôlée | acceptée (Qwen3 inchangé) |
| 9 couverture des couches | acceptée : contrôle `0..n−1`, formes égales ; « L31 = logits » écrit ci-dessus et au texte gelé ; `len(J) == 31` à B0 |
| 10 autres clés, sens des fichiers | acceptée : clés imprimées ; `config.yaml` et `CREDIT.md` lus à B0 avant toute lecture |
| 11 empreinte et révision | acceptée pour l'empreinte (dans `lenses.py`) ; révision du dépôt de Neuronpedia : inconnue de l'arbre archivé, l'empreinte la remplace |
| 12 identifiant exact | acceptée : `KeyError` explicite et note |
| 13 noms | constat, rien à faire |
| 14 docstring, essai | acceptée |

## Traitement de la contre-lecture 3 (`docs/notes/neuron-lens-v1/contre-lectures/contre-lecture-3-ciblee-v3.md`)
Verdict : différence et note « scellables en l'état » ; essai : deux compléments conseillés.

| remarque | traitement |
|---|---|
| 2 (texte) « couches `0..30` exigées » faux pour le code | acceptée : « contiguës `0..n−1` exigées ; n = 31 lu à B0 » (ci-dessus et au texte gelé) |
| 11a chemins de `J` non essayés, formats manquants | acceptée : essai v3 (sentinelles Llama et Qwen3 ; décalées, vide, non carrée) |
| 11b `torch.randn(..., dtype=float16)` | acceptée : `torch.randn(d, d).half()` |
| 12 constats sur le code | notés |
