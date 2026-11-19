# Correctif (4) de `scripts/checks/lens_compare.py` (comparaison des lentilles neurone par neurone) sur Llama, et essai de l'estimateur sur un Llama miniature — v2 (note)

Écrit le 2026-11-18 vers 04:50 UTC par la session `session_01XJ6MgmvmAAZ9h382ct8kHk`. **Remplace la v1** (`correctif-lens_compare-llama-v1.md`,
`086e5a15…`, archivée), selon la contre-lecture par un agent neuf `contre-lecture-correctif-4-et-essai-llama-miniature-v1.md`
(`7444555b…` : les deux pièces « à corriger », 0 bloquante, 6 majeures, 12 mineures ; le diff v1 jugé juste). Pièce du texte gelé
`texte-gele-tranche-b-beta-v1.md` (`f5d46860…`, P.2). Aucune machine, aucune dépense ; **code voisin jamais exécuté ni importé dans le
conteneur** (R-2710) : `git apply --check` sur la copie de lecture au commit `849bfe16`, `ast.parse`, et les seules fonctions
`statiques` de l'essai jouées ici.

## 1. Le correctif, v2
`lens_compare-llama-v2.diff` : les cinq points de la v1 (modèle de `neuron_lens.catalog` ; `kept(MODEL)` ; `cuda` ; `--json` non
arrondi ; `import json`), plus **l'ouverture du fichier JSON en création exclusive** (`open(args.json, "x")` : un fichier de même nom
n'est jamais écrasé, R12 ; mineure 1). Fichier corrigé : `c974cc1aa58f81f4b77e63db7cf6905d1a3b6172652a3dc51bf6f0605bacc77a` (publié :
`37b30e98…`).
À la charge de notre code de course, non du correctif (mineures 2 et 3) : lire dans le JSON `model` (Llama exigé), `lenses`, les six
couches et `rows` = 28 672, sinon chaîne en défaut ; télécharger poids et tokeniseur à la révision épinglée puis travailler hors ligne.

## 2. Essai du correctif, v2 (`essai-lens_compare-llama-v2.py`, pytest, `NEURON_LENS_ROOT`)
- Empreinte du fichier essayé contrôlée (`c974cc1a…`) ; fichier publié lu par `git show HEAD:…`, empreinte `37b30e98…` contrôlée.
- **Contrôles statiques par l'arbre syntaxique** (six) : pas de « Qwen/Qwen3-8B » ; `MODEL` importé de `neuron_lens.catalog` ; `MODEL`
  jamais réaffecté ; chaque `kept(MODEL)` ; `cuda` dans l'affectation de `dev` (un commentaire ne suffit plus) ; `open(args.json, "x")`.
- **Contrôle fonctionnel discriminant** (majeures 1 et 3) : doubles à la graine 0, 7 neurones, 8 dimensions, vocabulaire 20, **jetons
  gardés = sous-ensemble désordonné de 14**, lentille A = identité, B = identité + 0,5 × tirage ; tous les appels des quatre
  chargements notés et exigés pour Llama ; recalcul par `read` du dépôt sur le même périphérique que le correctif ; exigés : accord
  recalculé strictement entre 0 et 1, accord **et recouvrement** écrits égaux au recalcul à 10⁻¹², 14 lignes. Valeurs attendues
  recalculées hors du voisin par l'autrice : accord 4/14 ; sans l'indexation par les jetons gardés, 7/14.
- **Artefacts (R5, majeure 2)** : le fichier publié échoue aux six contrôles statiques ; sept copies fautives du fichier corrigé
  doivent chacune échouer (modèle réaffecté ; valeur arrondie ; recouvrement faux ; jetons gardés non indexés ; `cuda` en commentaire
  seulement ; écrasement permis ; `kept()` sans modèle). Vérifié ici (statiques seuls) : quatre échouent aux contrôles statiques ; les
  trois autres (valeur arrondie, recouvrement faux, jetons gardés non indexés) sont laissées au contrôle fonctionnel, à jouer sur la
  machine.
- **Commande** (majeure 4) : `NEURON_LENS_ROOT=$PWD NEURON_LENS_MODEL=meta-llama/Llama-3.1-8B-Instruct python -m pytest -q -rs …` depuis
  la racine de l'arbre voisin ; l'essai ajoute la racine au chemin d'import. Doubles remplacés sur le module, jamais sur la classe de
  `transformers` ; dossier temporaire effacé.

## 3. Essai de l'estimateur sur un Llama miniature, v2 (`essai-transport-llama-miniature-v2.py`)
- **Première partie, prescrite par le texte gelé** : `tests/test_transport.py` recopié mot pour mot, Qwen3 remplacé par Llama
  (différence vérifiée : cinq lignes de modèle, le reste identique) ; comme dans le dépôt, il ne joue que la variante « réaliste »
  (mineure 9, déclarée).
- **Seconde partie, ajoutée** (majeures 5 et 6) — **déclarée à la mère comme ajout au texte gelé** (aucune tolérance ni règle changée ;
  un échec est un échec de l'essai de l'estimateur, garde (f)) : miniature de base ; variante aux traits de Llama 3.1 (`rope_parameters`
  « llama3 », base 500 000, facteur 8, longueur d'origine 8 192 ; `rms_norm_eps` 1e-5 ; 4 têtes de requête pour 1 tête de clés et
  valeurs, `head_dim` 4 pour qu'une fréquence soit touchée ; vérifié ici avec `transformers` 5.23.0, sans le voisin : la fréquence basse
  passe de 1,41·10⁻³ à 5,25·10⁻⁴) ; un contrôle que ces fréquences diffèrent bien du « default » ; **deux artefacts** qui doivent échouer
  à la même tolérance : estimation décalée de 10⁻³, estimation calculée sur un autre modèle.
- Attendu : 9 tests passent, aucun sauté. **Risque connu** (mineure 10) : jamais joué ; si la tolérance 10⁻⁴ ne tient pas sur Llama,
  c'est une chaîne en défaut (f), arrêt avant l'ajustement (rien d'autre n'est dépensé que le montage).
- **Hors de cet essai** (mineure 11) : le chemin réel en bf16 compilé, les documents de 128 jetons, `02_fit.py` lui-même : couverts par
  le banc et les gardes (g), (h), (q).
- `transformers` : version épinglée dans la commande, celle de la tranche des lentilles publiques si elle est ≥ 5.

## 4. Reprise de la contre-lecture
| point | traitement |
|---|---|
| majeure 1 (accord nul, essai non discriminant) | levée : doubles neufs, accord exigé entre 0 et 1 |
| majeure 2 (pas d'artefact fonctionnel) | levée : sept copies fautives |
| majeure 3 (jetons gardés non exercés ; recouvrement non contrôlé) | levée |
| majeure 4 (commande fragile) | levée : pytest et `NEURON_LENS_ROOT` |
| majeure 5 (essai du miniature sans artefact) | levée : deux artefacts |
| majeure 6 (aucun trait de Llama 3.1) | levée par un ajout déclaré |
| mineures 1 à 3 (écrasement ; modèle non posé ; révision) | 1 levée dans le diff ; 2 et 3 à la charge de notre code et de la commande |
| mineure 4 (champs du JSON) | non retenue (liste fermée du texte gelé) |
| mineures 5 à 8 (empreintes ; arbre syntaxique ; double sur la classe ; sortie non versée) | levées ; sortie des contrôles statiques ci-dessus ; `__pycache__` effacé |
| mineures 9 à 12 (variante de base ; nom en clair ; risque ; hors champ) | levées |
