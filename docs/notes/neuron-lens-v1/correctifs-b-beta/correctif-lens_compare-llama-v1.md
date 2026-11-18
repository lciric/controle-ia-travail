# Correctif (4) du dépôt voisin pour la tranche de l'ajustement de nos lentilles : `scripts/checks/lens_compare.py` sur Llama — v1 (note et essai)

Écrit le 2026-11-18 vers 04:30 UTC par la session `session_01XJ6MgmvmAAZ9h382ct8kHk`, en application du texte gelé de la tranche
(`docs/notes/neuron-lens-v1/texte-gele-tranche-b-beta-v1.md`, `f5d46860…`, « Plan d'analyse », P.2, correctif (4)). **Non contre-lu,
non scellé comme correctif employé** : il ne sert qu'après contre-lecture par un sous-agent neuf et scellement (texte gelé, liste
d'arrêt). Aucune machine, aucune dépense ; **code voisin non exécuté** dans le conteneur (R-2710) : seuls `git apply --check` sur la
copie de lecture au commit `849bfe16` et `ast.parse` du fichier corrigé ont été faits ; l'essai n'a été joué ici que sur ses contrôles
statiques (aucun module du voisin importé).

## 1. Objet (inventaire, `inventaire-code-voisin-llama-b-beta-v1.md`, `e1945920…`, table `lens_compare.py`)
Au commit `849bfe16`, `lens_compare.py` (`37b30e98c9771c03ed452ff0ff36b3667c382201fa726180497c03a2b9daf6cd`) écrit le modèle en dur
(`MODEL = "Qwen/Qwen3-8B"`, l. 29) pour le tokeniseur, les poids et les lentilles, alors que `kept()` (l. 46) suit `NEURON_LENS_MODEL` :
sur Llama, les jetons gardés de Llama s'appliqueraient aux lignes de `lm_head` de Qwen sans erreur. Le périphérique est `mps`, sinon le
processeur central (l. 39). Rien n'est écrit sur disque : l'accord du premier jeton n'est imprimé qu'à deux décimales (l. 78).

## 2. Le correctif
Fichier : `lens_compare-llama-v1.diff` (un fichier, cinq blocs). Empreinte de `lens_compare.py` corrigé :
`d083f94daab3bb02fd9e2cbf28e6495fb1aac60d0f001fe66a9d7f1c20480eeb`.
1. `MODEL` importé de `neuron_lens.catalog` (donc de `NEURON_LENS_MODEL`) à la place de la constante écrite en dur ;
2. `kept(MODEL)` explicite ;
3. périphérique `cuda` s'il existe, sinon `mps`, sinon le processeur central ;
4. argument `--json CHEMIN` : à chaque paire de lentilles et chaque couche, `top1_agree` et `top10_overlap` non arrondis (`.item()` des
   mêmes tenseurs que l'impression) et le nombre de lignes comparées (neurones × deux signes) ; écrit en fin de course ;
5. `import json`.
Rien d'autre ne change : définitions, demi-précision de `unembed`, impression, `--layers`, `--samples`, graine.

## 3. Essai (R5)
`essai-lens_compare-llama-v1.py`, à jouer sur la machine à B0 (`NEURON_LENS_MODEL=meta-llama/Llama-3.1-8B-Instruct`) :
- **contrôles statiques** : aucun « Qwen/Qwen3-8B » écrit en dur ; `MODEL` importé de `neuron_lens.catalog` ; chaque appel `kept(MODEL)` ;
  `cuda` présent ; `--json` présent ;
- **contrôle fonctionnel** : module chargé, `MODEL` égal au modèle attendu ; tokeniseur, poids, jetons gardés et lentilles remplacés par
  des doubles synthétiques (d = 8, 5 neurones, vocabulaire 20, deux lentilles) qui notent le modèle demandé ; `main()` joué avec
  `--json` ; exigé : chaque chargement demandé pour le modèle attendu, et l'accord écrit égal, à 10⁻¹² près, à l'accord recalculé par la
  fonction `read` du dépôt ; 10 lignes.
- **Cas sain** : le fichier corrigé (sortie 0). **Artefact** : le fichier publié échoue aux cinq contrôles statiques (sortie 1).
  Vérifié dans le conteneur, contrôles statiques seulement : corrigé `[]` ; publié, les cinq fautes.
