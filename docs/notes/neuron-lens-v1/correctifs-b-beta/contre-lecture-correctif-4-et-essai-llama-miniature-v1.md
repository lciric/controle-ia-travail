# Contre-lecture du correctif (4) de `lens_compare.py` et de l'essai de l'estimateur sur un Llama miniature — v1

Date : 2026-11-18, 04:35 UTC (`date -u`). Auteur : **contre-lecteur neuf** (R2), qui n'a écrit aucune des pièces lues.
Aucun fichier modifié hors ce rapport ; rien de committé ; rien lu sous `registres/` ni `diag/`.

## Pièces et empreintes vérifiées (`sha256sum` contre chaque compagnon : toutes égales)

| pièce | empreinte |
|---|---|
| `lens_compare-llama-v1.diff` (le correctif) | `1a13091329ddd9662a1b8d656844e0231717e5800ea1344b8b3b716ae6fc4243` |
| `correctif-lens_compare-llama-v1.md` (sa note) | `086e5a156e5ab66caeafd229adca47593e194d7862bde90594c244f76b63e697` |
| `essai-lens_compare-llama-v1.py` (son essai) | `5a72d24aac5a25543670ae9bbecb112e31dfbd3f55ab9545b679ac9b7b566eed` |
| `essai-transport-llama-miniature-v1.py` (essai de l'estimateur sur un Llama miniature) | `328f87f2225799630bd0b7b7d7ba53232ef92762070ee95115076eef7d8bd96d` |
| référence : `../texte-gele-tranche-b-beta-v1.md` | `f5d46860525f12f8ad0483e56afc0847ab7db25ecae55edcc279b61316b7a454` |
| contexte : `../inventaire-code-voisin-llama-b-beta-v1.md` | `e1945920…` (début vérifié) |
| dépôt voisin, lecture seule | commit `849bfe1678e28becceb1e3864afe5fc8297d02e4`, arbre propre avant et après |

## Ce que j'ai lu ou fait

- **Lu** : les quatre pièces ; le texte gelé (mesure de l'accord du premier jeton, gardes (d), (f), (r), P.2, P.3, P.4, P.5, P.6) ;
  la table `lens_compare.py` de l'inventaire ; dans le voisin, sans rien exécuter ni importer : `scripts/checks/lens_compare.py`,
  `neuron_lens/catalog.py`, `readout.py`, `weights.py`, `lenses.py`, `rules.py`, `transport.py`, `layers.py` (primal, attention,
  contrôles), `tests/test_transport.py`, `pyproject.toml`, l'en-tête de `scripts/02_fit.py` ; les essais de la tranche précédente
  (branche `prep/neuron-lens-v1`) pour comparer les conventions.
- **Fait sur le voisin** : `git apply --check` du correctif (accepté) ; rien d'autre.
- **Fait hors du voisin**, dans un dossier de travail jetable : copie du seul `lens_compare.py`, correctif appliqué par `patch`,
  empreinte et `ast.parse` du fichier corrigé ; appel de la seule fonction `statiques` de l'essai sur le fichier publié, le fichier
  corrigé et sept copies fautives de mon cru ; **recalcul indépendant**, par mon propre code écrit d'après la lecture de
  `readout.read` (aucun import du voisin), de l'accord que l'essai compare ; avec `torch 2.15.0` (processeur) et
  `transformers 5.23.0` installés pour l'occasion, **sans le voisin** : construction des deux Llama miniatures de l'essai, noms des
  modules, type de sortie des blocs, et passage de la force brute de l'essai (crochets recopiés) sans les règles du voisin.
- **Non fait** (règle stricte) : le contrôle fonctionnel de l'essai de `lens_compare`, et l'essai du Llama miniature, n'ont jamais
  tourné — ni chez l'autrice, ni ici.

## Verdicts

- **Pièce 1 — correctif (4) de `lens_compare.py`, sa note et son essai : « à corriger ».** Le correctif lui-même (le diff) est juste
  et **employable tel quel** : aucun constat bloquant ni majeur sur lui. C'est son **essai** qui est à corriger : son contrôle
  fonctionnel compare zéro à zéro et n'a pas d'artefact.
- **Pièce 2 — essai de l'estimateur sur un Llama miniature : « à corriger ».** La recopie est fidèle et la configuration est valide ;
  il manque l'artefact prévu par le texte gelé, et le miniature ne porte aucun des traits propres à Llama 3.1.

Comptes : **0 bloquante, 6 majeures, 12 mineures.**

## Ce qui est vérifié et juste (sans constat)

- Le correctif s'applique sur le commit épinglé. Le fichier publié a bien l'empreinte `37b30e98…` ; le fichier corrigé a bien
  l'empreinte `d083f94d…` annoncée par la note ; il se lit par `ast.parse`. Cinq blocs, comme annoncé.
- Il fait ce que P.2 (4) et la note disent, et rien d'autre : `MODEL` importé de `neuron_lens.catalog` ; `kept(MODEL)` ;
  périphérique `cuda`, sinon `mps`, sinon processeur central ; argument `--json` ; `import json`. Définitions (l. 72-78 du publié),
  demi-précision de `unembed`, impressions, `--layers`, `--samples`, graine : inchangés. Sans `--json`, sur une machine sans carte,
  le comportement est celui du publié.
- L'import de `MODEL` est sûr : `catalog` est déjà importé par le fichier publié (pour `kept`), donc aucun ordre d'import nouveau ;
  la variable `NEURON_LENS_MODEL` est lue une fois, à l'import, donc avant `main()`. `kept(MODEL)` et `kept()` rendent la même liste.
- `cuda` est compatible avec la suite : `read` rend des tenseurs sur le processeur central (`readout.py` l. 42-43), donc la
  comparaison des premiers jetons, `fmt` et son `.cpu()` ne changent pas ; `torch.linalg.svd` porte sur la matrice de la lentille
  telle que chargée (sur le processeur central pour les fichiers lus avec `map_location="cpu"`), comme dans le publié ; `gamma`,
  `W_down` et `unembed` sont tous portés sur le même périphérique.
- Le fichier JSON reçoit `top1.item()` et `overlap.item()`, c'est-à-dire les **mêmes tenseurs** que la ligne imprimée, non arrondis
  (précision simple). La précision simple suffit aux règles du texte gelé : avec 28 672 pôles, les seuils 0,80 et 0,60 ne tombent
  sur aucun compte entier (22 937,6 et 17 203,2), et l'accord « égal à 1 » de l'audit de stabilité est exact (somme de 28 672 uns).
- Essai de `lens_compare`, contrôles statiques : rejoués ici — fichier corrigé `[]`, fichier publié les cinq fautes. Les signatures
  des doubles (`tensors(modèle, noms)`, `kept(modèle)`, `load_lens(spéc, modèle)`, `from_pretrained(modèle)`) sont celles des appels
  de `lens_compare.py` ; les lentilles en dictionnaire `{couche: matrice}` conviennent à `m[layer]` ; avec `--samples 0`, ni `KNOWN`
  ni le tokeniseur ne servent. Sur une machine à carte, l'essai et `lens_compare` calculent tous deux sur `cuda` : même périphérique.
- Essai du Llama miniature : le `diff -u` contre `tests/test_transport.py` ne contient **que** la description, l'import, les deux
  noms de classe (quatre lignes) et un commentaire ; `run_with`, `exact`, `exact_from` et le test sont identiques au mot près ;
  tolérance `atol = 1e-4` et graines `torch.manual_seed(0)` et `(1)` inchangées, comme le texte gelé l'écrit.
- Configuration Llama valide sous `transformers 5.23.0` : `head_dim=8` accepté (4 têtes × 8 = 32 pour une largeur de 16, comme le
  Qwen3 du dépôt), attention « eager » prise, aucun biais (`attention_bias` et `mlp_bias` faux), position rotative par défaut.
  `LlamaModel` a bien `embed_tokens`, `layers`, `norm`, `rotary_emb` ; chaque bloc a `self_attn`, `mlp`, `input_layernorm`,
  `post_attention_layernorm` ; la sortie d'un bloc est un tenseur `[1, T, d]`, comme les crochets le supposent ; la force brute de
  l'essai tourne (dérivée finie, nulle vers la dernière position). Les sept poids de normes sont bien tirés dans [0,3 ; 2,0].
- Les règles du voisin couvrent Llama, à la lecture : normes d'entrée et d'après attention (`rules.py` l. 38, `variance_epsilon`
  présent), couche à portes à trois projections et activation `SiLUActivation` (l. 59), attention ordinaire non modifiée
  (`is_gated` faux : 32 ≠ 64) ; `layers.check` ne refuse rien (aucun biais, attention causale) ; l'absence de normes de requêtes et
  de clés est prévue (`layers.py` l. 251-253) ; les tables de position rotative viennent du module du modèle (l. 545).

## Constats

| rang | pièce | constat vérifié | correction proposée |
|---|---|---|---|
| majeure | essai de `lens_compare` | **Le contrôle fonctionnel compare 0 à 0.** Avec les doubles de l'essai (lentille A = identité, lentille B tirée au hasard, 5 neurones, 20 jetons), mon recalcul indépendant donne un accord du premier jeton de **0,0** (les dix pôles en désaccord), en demi-précision comme en précision simple. Un fichier JSON qui écrirait 0 par défaut, une valeur arrondie, ou un calcul fait ailleurs passerait donc. (Recalcul par mon code, non par `read` du voisin : à confirmer sur la machine.) | Prendre B proche de A et un nombre de pôles qui ne tombe pas sur deux décimales : par exemple B = identité + 0,5 × tirage, 7 neurones (accord recalculé ici : 6/14 = 0,4286). Exiger dans l'essai `0 < accord < 1`. |
| majeure | essai de `lens_compare` | **Le contrôle fonctionnel n'a pas d'artefact** (R5). Le seul artefact est le fichier publié, qui s'arrête aux contrôles statiques : le contrôle fonctionnel n'est jamais joué sur un cas qui doit échouer. Sur sept copies fautives du fichier corrigé, les contrôles statiques n'en voient aucune ; à la lecture, le contrôle fonctionnel n'en verrait que deux (modèle réaffecté ; tokeniseur de Qwen) et laisserait passer : valeur arrondie écrite, recouvrement faux, `unembed` en précision simple, `cuda` présent seulement en commentaire, indexation par les jetons gardés retirée. | Ajouter à l'essai des artefacts fonctionnels faits par remplacement de texte dans une copie du fichier corrigé (au moins : valeur arrondie à deux décimales ; indexation `[keep]` retirée ; recouvrement mis à 0), chacun attendu en échec ; sortie 0 seulement si le cas sain passe **et** si chaque artefact échoue. |
| majeure | essai de `lens_compare` | **Les jetons gardés ne sont pas exercés, le recouvrement n'est pas contrôlé.** Le double de `kept` rend tous les jetons (`arange(20)`) : l'indexation des lignes de `lm_head` par les jetons gardés — le défaut même que le correctif répare — est sans effet dans l'essai. `top10_overlap`, écrit par le correctif et rapporté par le texte gelé, n'est pas comparé. | Rendre un sous-ensemble strict et désordonné (par exemple 14 jetons sur 20) et recalculer avec lui ; comparer aussi `top10_overlap` ; exiger que les quatre chargements (`tensors`, `kept`, `lens`, `tok`) aient tous été vus, et noter tous les appels plutôt que le premier (`setdefault`). |
| majeure | essai de `lens_compare` | **Commande prescrite fragile.** `python -I essai… CHEMIN` retire le dossier courant, le dossier du script et `PYTHONPATH` du chemin d'import : `from neuron_lens.readout import read` ne marche que si le voisin est installé dans l'environnement (`pip install -e .`). Les essais de la tranche précédente passaient par `NEURON_LENS_ROOT=$PWD python -m pytest`. Un échec d'import à B0 serait un essai en échec (garde (d)). | Soit ajouter la racine au chemin dans l'essai (comme les essais précédents, par `NEURON_LENS_ROOT`), soit écrire dans la note que le voisin doit être installé, et le vérifier dans la commande de montage avant l'essai. |
| majeure | essai du Llama miniature | **Aucun artefact** (R5 ; texte gelé, P.4, branches des gardes). Le texte gelé attend, pour l'essai de l'estimateur contre la force brute (garde (f)), « un Llama miniature dont une matrice estimée est perturbée de 10⁻³ », et pour les essais (garde (d)) « un estimateur faussé (signe d'un terme inversé dans une copie de l'essai) ». La pièce n'offre ni ce cas ni une prise pour le jouer. | Ajouter une pièce (ou un second test dans le même fichier, sans toucher au test recopié) qui perturbe de 10⁻³ une matrice estimée et exige que la même comparaison, à la même tolérance, échoue ; la sceller avec l'essai. Écrire le nombre de tests attendus (2 réussis, 0 sauté) et l'option `-rs` dans la commande. |
| majeure | essai du Llama miniature | **Le miniature ne porte aucun trait propre à Llama 3.1.** Il ne diffère du Qwen3 miniature que par la classe et l'absence de normes de requêtes et de clés. Le vrai modèle a : position rotative mise à l'échelle « llama3 » (facteur 8, base 500 000 — lu sur un miroir public de la configuration, l'original étant sous licence), `rms_norm_eps = 1e-5`, quatre têtes de requête par tête de clés et valeurs, produit têtes × `head_dim` égal à la largeur. À la lecture, le risque est faible (les tables de position viennent du module du modèle), mais l'essai ne le montre pas. Vérifié ici : `LlamaConfig` accepte cette mise à l'échelle sur un miniature et change bien les fréquences. | Ajouter une troisième variante « fidèle » (mêmes dimensions, `rope_parameters` de Llama 3.1, `rms_norm_eps=1e-5`, 8 têtes dont 2 de clés et valeurs), en plus des deux prescrites. C'est un ajout au texte gelé, non un changement : à déclarer ; si la mère y voit un écart au texte scellé, c'est un nœud pour Lazar. |
| mineure | correctif | Le fichier JSON est ouvert en écriture simple : un fichier de même nom serait écrasé sans message (R12). | Ouvrir en création exclusive (`"x"`), ou nom neuf imposé par la commande. |
| mineure | correctif | Si `NEURON_LENS_MODEL` n'est pas posée, tout retombe sur Qwen3 sans message (défaut du voisin, `catalog.py` l. 32). Le correctif rend l'ensemble cohérent et écrit `model` dans le JSON, ce qui permet le contrôle. | Notre code des verdicts doit lire dans le JSON `model` (Llama attendu), `lenses`, les six couches et `rows` = 28 672, et s'arrêter sinon. |
| mineure | correctif (hors de son périmètre) | `tensors(MODEL, …)` et `AutoTokenizer.from_pretrained(MODEL)` ne passent aucune révision : c'est la branche principale du dépôt de poids qui est lue, non la révision épinglée, sauf cache seul. Comportement publié, inchangé. | À tenir par la commande de montage (mode hors ligne après téléchargement à la révision épinglée), non par le correctif. |
| mineure | correctif | Le JSON n'écrit ni le compte entier de pôles d'accord, ni le nombre de jetons gardés, ni le périphérique. Non exigé par P.2 (liste fermée) ; la garde des jetons gardés reste à la charge de notre code. | Facultatif : rien, ou une nouvelle version du texte si l'on veut ces champs. |
| mineure | essai de `lens_compare` | L'empreinte du fichier essayé n'est pas contrôlée (`d083f94d…` pour le corrigé, `37b30e98…` pour le publié), alors que les essais précédents le faisaient. La note ne dit pas comment garder le fichier publié pour l'artefact, ni que l'attendu est « sortie 1 avec exactement les cinq fautes ». | Contrôler les deux empreintes ; écrire la commande des deux passages et leur attendu. |
| mineure | essai de `lens_compare` | Contrôles statiques par recherche de texte : `torch.cuda.is_available()` dans un commentaire suffit ; `MODEL` réaffecté après l'import n'est pas vu (le contrôle fonctionnel le voit). | Chercher par l'arbre syntaxique : affectation de `dev`, absence d'affectation à `MODEL`. |
| mineure | essai de `lens_compare` | `AutoTokenizer.from_pretrained` est remplacé sur la classe de `transformers` elle-même, sans remise en état ; le dossier temporaire n'est pas effacé ; le recalcul choisit « `cuda` sinon processeur central » alors que le correctif choisit « `cuda`, `mps`, processeur central » (écart seulement sur une machine `mps`). | Remplacer `m.AutoTokenizer` par un objet double ; reprendre le même choix de périphérique que le correctif. |
| mineure | note du correctif | La vérification statique « corrigé `[]`, publié cinq fautes » n'a pas de sortie versée (R6). Un dossier `__pycache__` est resté à côté des pièces (ignoré par git, non committé). | Verser la sortie avec son compagnon ; effacer `__pycache__`. |
| mineure | essai du Llama miniature | Ambiguïté de lecture du texte gelé : « aux mêmes dimensions (… 2 têtes de requête et 1 de clés et valeurs …), puis dans la variante réaliste ». Comme dans le dépôt, le test ne joue que la variante réaliste ; le miniature de base n'est jamais comparé. Conforme à « mot pour mot ». | Le déclarer dans une note ; ou jouer aussi le miniature de base (ajout). |
| mineure | essai du Llama miniature | Pas de note compagne ; la description nomme la garde par sa lettre avant son nom en clair (« Essai de la garde (f) ») ; la version de `transformers` n'est pas écrite (le voisin demande `>= 5`). | Une note courte ; « essai de l'estimateur contre la force brute sur un Llama miniature (garde (f)) » ; version épinglée dans la commande. |
| mineure | essai du Llama miniature | Jamais joué nulle part : rien ne dit que la tolérance 10⁻⁴ tient sur un Llama miniature (attention sans normes de requêtes et de clés). Un échec numérique à B0 serait une chaîne en défaut. | Le dire dans la note comme risque connu ; aucune tolérance ne change (texte gelé). |
| mineure | essai du Llama miniature | Ce que l'essai ne couvre pas, comme celui du dépôt : le chemin réel de l'ajustement en bf16 sur carte avec pas compilés ; les documents de 128 jetons ; le script `02_fit.py` lui-même (moitiés, reprise, export). | À rappeler dans la note : couverts par le banc et par les gardes de l'ajustement, non par cet essai. |

## Non vérifiable ici

- Le contrôle fonctionnel de l'essai de `lens_compare` et l'essai du Llama miniature : jamais exécutés (règle stricte). L'accord nul
  du premier constat vient de mon recalcul, non de `read`.
- Le comportement sur `cuda` : produit en demi-précision, égalités exactes entre logits en demi-précision et leur départage par
  `topk` (il peut différer de celui de `mps`, périphérique du publié), mémoire, durée des dix-huit décompositions sur le processeur.
- Le type et le périphérique des matrices rendues par Drowse pour les lentilles `R:` (lu par l'autrice, non par moi).
- La configuration officielle de Llama 3.1 (dépôt sous licence) : lue sur un miroir public seulement.
- La version de `transformers` et le mode d'installation du voisin sur la machine.
