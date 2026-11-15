# Lecture des `config.yaml` et `CREDIT.md` des trois lentilles de Neuronpedia pour Llama 3.1 8B Instruct — avant le feu de B-α — v1

Écrite par la fille « Neuron Lens » le 2026-11-15, pour la pièce 3 du § 6 du devis B-α v2 (partie 2 de l'addendum). Le texte gelé v6
(§ B.1 et liste d'arrêt, l. 416) demande, à B0, la lecture de ces fichiers ; arrêt si l'un « dit une autre convention que « clé l = sortie
de la couche l » ». Ces fichiers sont publics et petits : **lus ici, avant le feu**, pour que la machine n'ait qu'à vérifier l'égalité de
leurs empreintes (aucune lecture humaine pendant la course).

## Relevé
Téléchargés le 2026-11-15T08:28:50Z, sans clé, client générique, à la révision épinglée `d2527c3cdbaa60dd4b65cbca1604921f044e989a` de
`neuronpedia/jacobian-lens` (`…/resolve/<révision>/llama3.1-8b-it/<chemin>`) ; archivés sous
`docs/sources/neuron-lens-b-alpha-neuronpedia-config-20261115/` (compagnons `.sha256`). Empreinte git (« blob ») de chacun **égale** à celle
de l'arbre archivé de l'addendum (`docs/sources/neuron-lens-v2-addendum-20261114/neuronpedia-arbre-llama3.1-8b-it.json`) :

| fichier (sous `llama3.1-8b-it/`) | taille | empreinte git |
|---|---|---|
| `jlens/Salesforce-wikitext/config.yaml` | 2 871 | `0ae053cfdcf8909782d3ba55a25125d2d5db3015` |
| `jpp/Salesforce-wikitext/CREDIT.md` | 1 201 | `14fc7e775a0abf3dc1d5ba4af02784031a9e454f` |
| `jpp/Salesforce-wikitext/config.yaml` | 2 989 | `6bd6b47ddc1b7f680a72e6976f4280b29b7b9844` |
| `rlens/Salesforce-wikitext/CREDIT.md` | 1 130 | `d3724c2b5cd0daed4bd399e22e626f8f82f1d1fe` |
| `rlens/Salesforce-wikitext/config.yaml` | 2 999 | `01d952a6b357cfdf16e39e5cb58942cb1ddef57c` |

L'arbre n'a **pas** de `CREDIT.md` pour `jlens`.

## Lecture
- **J++ (`npJpp`)** et **R (`npR`)** : `lens.capture_point: "block_output"`, `source_layers_first: 0`, `source_layers_last: 30`,
  `n_source_layers: 31`, `target_layer: 31`, `skip_first: 16`, `n_prompts: 64` ; les `CREDIT.md` disent une conversion fp32 → fp16 « sans
  autre changement des matrices ». **Convention dite : la sortie du bloc l pour la clé l** — celle qu'exige le texte gelé.
- **J (`J`)** : la configuration est celle d'un ajustement (`fit_lens.py`, 1 000 invites demandées, **461 ajustées** :
  `results.prompts_fitted`) ; **elle ne nomme aucune convention** de capture (ni `capture_point`, ni couches sources), et il n'y a pas de
  `CREDIT.md`. Elle n'en dit donc **pas d'autre** : ce n'est pas le cas d'arrêt à la lettre. **Réserve déclarée**, pour le contre-lecteur :
  pour J, la convention ne repose que sur le contrôle de structure de B0 (31 couches contiguës `0..30`, `controle_lentille`) et sur la
  lecture du correctif (2) ; aucune phrase des fichiers de Neuronpedia ne la confirme.
- Nombres d'invites d'ajustement (texte gelé l. 190, « 461 ; 64 », niveau citation) : **retrouvés** (J : 461 ; J++ et R : 64).

## Ce que fait la machine à B0
Elle télécharge ces cinq fichiers à la même révision et exige l'**égalité des empreintes git** ci-dessus (partie 2 de l'addendum,
`addendum_partie2_b_alpha_v1.py`) ; tout écart = arrêt. La lecture de la convention n'est pas refaite sur la machine : elle est celle-ci,
contre-lue avant le feu.
