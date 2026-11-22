# Addendum de la tranche de l'ajustement de nos lentilles — partie 2, premier relevé (B0, avant l'ajustement) — v2

Écrit par `controle_ia.neuron_lens.addendum_partie2_b_beta_v3` sur la machine (aucune pause humaine). Partie 1 :
`docs/notes/neuron-lens-v1/addendum-texte-gele-tranche-b-beta-v1-partie1-v3.md` (`bd8067dc…`). **Tout écart ci-dessous
arrête la course avant l'ajustement.**

- date : 2026-11-18T18:00:13Z ; instance : 
- commit réduit : 5e5cb65b4daf8726ebe1c4032a836b850de7ea2f ; commit source : fe0731ce71553301116a88680716653279f2a455 ; commit voisin : 849bfe1678e28becceb1e3864afe5fc8297d02e4 (arbre b22006e91067d517b758cf755246fd8d2f5c2ca4, correctifs appliqués sans commit)

## Écarts

Aucun.

## Modèle `meta-llama/Llama-3.1-8B-Instruct`, révision 0e9e39f249a16976918f6564b8830bc894c89659

| fichier | sha256 relevé | attendu (partie 1, § 2) |
|---|---|---|
| `config.json` | `29e4c210b0d6ac178b16b2a255a568bdb23b581e50ca1ef6a6d071dd85704e6e` | `29e4c210b0d6ac178b16b2a255a568bdb23b581e50ca1ef6a6d071dd85704e6e` |
| `generation_config.json` | `189fb0c0d7fd8a527db217c0a60a0e013f0394cd8800f9697a666a9e75e5f7fd` | `189fb0c0d7fd8a527db217c0a60a0e013f0394cd8800f9697a666a9e75e5f7fd` |
| `model-00001-of-00004.safetensors` | `2b1879f356aed350030bb40eb45ad362c89d9891096f79a3ab323d3ba5607668` | `2b1879f356aed350030bb40eb45ad362c89d9891096f79a3ab323d3ba5607668` |
| `model-00002-of-00004.safetensors` | `09d433f650646834a83c580877bd60c6d1f88f7755305c12576b5c7058f9af15` | `09d433f650646834a83c580877bd60c6d1f88f7755305c12576b5c7058f9af15` |
| `model-00003-of-00004.safetensors` | `fc1cdddd6bfa91128d6e94ee73d0ce62bfcdb7af29e978ddcab30c66ae9ea7fa` | `fc1cdddd6bfa91128d6e94ee73d0ce62bfcdb7af29e978ddcab30c66ae9ea7fa` |
| `model-00004-of-00004.safetensors` | `92ecfe1a2414458b4821ac8c13cf8cb70aed66b5eea8dc5ad9eeb4ff309d6d7b` | `92ecfe1a2414458b4821ac8c13cf8cb70aed66b5eea8dc5ad9eeb4ff309d6d7b` |
| `model.safetensors.index.json` | `146776fce3f6db1103aa6f249e65ee5544c5923ce6f971b092eee79aa6e5d37b` | `146776fce3f6db1103aa6f249e65ee5544c5923ce6f971b092eee79aa6e5d37b` |
| `special_tokens_map.json` | `6f38c73729248f6c127296386e3cdde96e254636cc58b4169d3fd32328d9a8ec` | `6f38c73729248f6c127296386e3cdde96e254636cc58b4169d3fd32328d9a8ec` |
| `tokenizer.json` | `79e3e522635f3171300913bb421464a87de6222182a0570b9b2ccba2a964b2b4` | `79e3e522635f3171300913bb421464a87de6222182a0570b9b2ccba2a964b2b4` |
| `tokenizer_config.json` | `177c7b61e616fecb84c17ce0591acb92c6c4d60e9ac5ababfb940ff23bbcd424` | `177c7b61e616fecb84c17ce0591acb92c6c4d60e9ac5ababfb940ff23bbcd424` |

## Lentilles de Neuronpedia, révision d2527c3cdbaa60dd4b65cbca1604921f044e989a

- `J` : `d5300a1575c0b5ad6e01b098c75adb072f3a6c246f184ce2fb35a3550fc8c68b` (attendu `d5300a1575c0b5ad6e01b098c75adb072f3a6c246f184ce2fb35a3550fc8c68b`)
- `npJpp` : `8bd04f482aed9c85e76e71ccb510907405500512193cdfcc34f4f31722056f7c` (attendu `8bd04f482aed9c85e76e71ccb510907405500512193cdfcc34f4f31722056f7c`)
- `npR` : `a63a1588f2cb61850c68131a5f13b74590f4fe137f67bf80c627547d2230d31c` (attendu `a63a1588f2cb61850c68131a5f13b74590f4fe137f67bf80c627547d2230d31c`)

## Corpus d'ajustement

- provenance écrite par `01_lens_corpus.py` : sha256 `16957c528c2f7765afe01b37318aae5365535f29dffdde8c5ce5c48ed1c2e77a` (publiée : `16957c528c2f7765afe01b37318aae5365535f29dffdde8c5ce5c48ed1c2e77a`)
- `dclm.jsonl` : sha256 `990849ad277204d343572f93f1361bfce961e2395ff16acfcf4b7115783bddc7`
- documents pleins de 128 jetons : 932 ; moitiés [466, 466] ; longueurs [128]
- `rows_sha256` : `a6afd972eeaa3566a28d07216efaf75624fda20293c5fab3b7af39277aaf93b3` ; moitiés `['4a31baecbac5481f71c22912f2a02927bea2877f2be6d82d58185d36c1b95e32', 'ef95a60c96032cdc9ea42a957eb4d0f10006d4d11fb751515f3c343eb435c3f9']`

## Versions

- datasets : 5.2.0
- drowse.ai : 6.1.4
- huggingface_hub : 1.33.0
- numpy : 2.4.6
- pyarrow : 26.0.1
- python : 3.12.16
- pyyaml : 6.0.3
- safetensors : 0.8.0
- tokenizers : 0.23.2
- torch : 2.14.1
- transformers : 5.18.0
- Drowse : version 6.1.4, roue `673ed2b4de653ad2ec22660b0191031ee2c7b4bacaf4cc2ea552f0436b9d8e03` (installée sans dépendances)

## Code voisin corrigé

- `data/corpus/act-chat-llama-3.1-8b-instruct.provenance.json` : `777aa068a008b38fc22c6758d283e33ac31e31d6c5ed2eed878f7d75050d231d`
- `neuron_lens/arch.py` : `877fa6b0a864d8ffe88d15789ea9fa913a7bc7a529c399b2e001911c4eccf964`
- `neuron_lens/lenses.py` : `2de7d6afe63bc398e17f4ff93ae7b7acdcc3a330e91c728df88bef338008b3e4`
- `scripts/06_activations.py` : `b97bf54b7c3b12f3ec1853000ba66cf5a6056c6c05b6400a8572a44e154cb902`
- `scripts/checks/causal_lens.py` : `a9d3bc8e8dde945c4ff0f4a229f30c78b35ee299a4fa1fe34fe75db35252141b`
- `scripts/checks/lens_compare.py` : `c974cc1aa58f81f4b77e63db7cf6905d1a3b6172652a3dc51bf6f0605bacc77a`

## Essais de B0

- `essai-06_activations-llama-v3.py` : code 0, « 7 passed in 4.87s »
- `essai-causal_lens-graine-v1.py` : code 0, « 8 passed in 3.80s »
- `essai-crochets-causal_lens-llama-v1.py` : code 0, « 4 passed in 5.10s »
- `essai-lens_compare-llama-v2.py` : code 0, « 10 passed in 4.18s »
- `essai-lenses-neuronpedia-v3.py` : code 0, « 13 passed in 1.38s »
- `essai-transport-llama-miniature-v3.py` : code 0, « 11 passed in 7.16s »
- `test_neuron_lens_controles_b_beta_v2.py` : code 0, « 29 passed in 1.62s »
- `test_neuron_lens_verdicts_b_beta_v4.py` : code 0, « 82 passed in 0.42s »
- `test_transport.py (dépôt, Qwen3 miniature)` : code 0, « 2 passed in 4.48s »
- artefact « saute » : code 0, « 10 passed, 1 skipped in 7.17s », vu en défaut : True
- artefact « signe » : code 1, « 2 failed, 9 passed in 8.91s », vu en défaut : True
