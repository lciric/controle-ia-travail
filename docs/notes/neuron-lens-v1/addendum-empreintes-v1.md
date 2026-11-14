# Addendum des empreintes du texte gelé v6 — partie 1 (fixée avant toute machine) — v1

Pièce exigée par la liste d'arrêt du texte gelé `docs/notes/neuron-lens-v1/texte-gele-volet-a-et-b-alpha-v6.md`
(`34b882437a9d1eb7a865e870b3b156b596fb78a8a30316588ec13abbfa21c131`) : « addendum des empreintes non scellé avant la première passe →
rien ne part ». Écrit par la session fille « Neuron Lens » (`session_01QPDgKfBxeeiM3BsxqJgSgf`) le 2026-11-14 ; métadonnées relevées
entre 10:38:13 et 10:40:18 UTC (`date -u`), sans clé (`env -u HF_TOKEN`), client générique ; archivées sous
`docs/sources/neuron-lens-v2-addendum-20261114/` (compagnons `.sha256`). Aucune machine, aucune dépense. **Cette partie 1 ne change rien
au texte gelé** ; elle fixe des révisions et des empreintes. La **partie 2** (empreintes des fichiers réellement téléchargés à B0, qui
doivent égaler celles-ci) est écrite et scellée à B0 **avant la première passe**.

## 1. Modèles
| objet | révision épinglée | empreintes de stockage | source archivée |
|---|---|---|---|
| `Qwen/Qwen3-8B` (Apache-2.0) | `b968826d9c46dd6066d109eabc6255188de91218` | `model-00001…00005.safetensors` : `31d6a825ae35f11fb85b195b4c42c146c051e446433125a215336abdf95cbf5f`, `5991236cea6fe21f3d43cab0f0e84448734fbbe0789816202989f2ddc9d18282`, `c5185c4794be2d8a9784d5753c9922db38df478ce11f9ed0b415b7304d896836`, `b5ee7de71fbf17db3d5704e0c8f2bc7d005ca9e1d7ca2aeb19827b0cfcaa917a`, `20c2d6366ab85c90786ccdd829cd2b9e7d30ef3b2ebbb998280e7e4014b542ff` ; `tokenizer.json` `aeb13307a71acd8fe81861d94ad54ab689df773318809eed3cbe794b4492dae4` (égale à celle du texte gelé) | `qwen3-8b-arbre.json` |
| `meta-llama/Llama-3.1-8B-Instruct` (licence Llama 3.1, accès sous condition) | `0e9e39f249a16976918f6564b8830bc894c89659` | non publiées sans accès (masquées par l'interface) : relevées au téléchargement, partie 2 | `llama-3.1-8b-instruct-api.json`, `llama-3.1-8b-instruct-arbre.json` |

## 2. Lentilles
| objet | révision | empreintes | source |
|---|---|---|---|
| `stdlogits/rs-lenses` (CC BY 4.0), Qwen3-8B | `984fe3d2a46a35580764260ea438cbd6ac17c486` | `r-lens/lens.pt` `5eaa4d56e10d0c535b5170d5aaaa1174fb8dedf0fddb2f9821cec0aa1050fae1` ; `r-lens/mid.pt` `5484aa887af94b722a81b570547c13f839bb0f45163dd63d5e82e35e222e8afa` ; `s-lens/mid.pt` `836ac41eb7ba2194c1302e27b37d92dce23d67504310444ecfe926e6bd28a1b2` ; `s-lens/out.pt` `f87601433def8cfc403508acccadb7e62d99a5ccf51ec30e730d7c93c21d37ec` (égales au texte gelé) | `stdlogits-rs-lenses-api.json`, `stdlogits-rs-lenses-arbre-qwen3-8b.json` |
| `neuronpedia/jacobian-lens` (licence Llama 3.1 pour ces dossiers), Llama 3.1 8B Instruct | `d2527c3cdbaa60dd4b65cbca1604921f044e989a` | J `d5300a1575c0b5ad6e01b098c75adb072f3a6c246f184ce2fb35a3550fc8c68b` ; J++ `8bd04f482aed9c85e76e71ccb510907405500512193cdfcc34f4f31722056f7c` ; R `a63a1588f2cb61850c68131a5f13b74590f4fe137f67bf80c627547d2230d31c` (égales au texte gelé et au correctif (2)) | `neuronpedia-jacobian-lens-api.json`, `neuronpedia-arbre-llama3.1-8b-it.json` |

## 3. Catalogue publié de Qwen3-8B (`stdlogits/neuron-lens`, jeu de données, CC BY 4.0)
Révision `2f19669198445347a4dbd1a2c2324652ee31b0a2` (`stdlogits-neuron-lens-catalogue-api.json`, arbre `stdlogits-neuron-lens-catalogue-qwen3-8b-arbre.json`).
| fichier | empreinte | usage |
|---|---|---|
| `qwen3-8b/token_counts.pt` | `10e90037470c51bfd75e15ff8d28a830172a5b5c9f9a6c38024a768534e5697b` | définit `catalog.kept` (jetons vus au moins 5 fois, sans pièce d'octet) |
| `qwen3-8b/neurons/acts/L01.parquet` | `17424cd15472e518b5c5b58a8ce2fe1bd482a49153038378d24564f8e6abb347` | `neg_lobe` du pôle `L1 n11672 −` (cas sain (ii)) |
| `qwen3-8b/neurons/acts/L08.parquet`, `L14`, `L20`, `L26` | `c837fe7dd29f6450dbeaccaa691a98f2e88afec1f3acf822ddf51ef01019e836`, `8a2bfb9233da13d24d7eb264aebd3bb5232514fbc7fffdc8630a963c414c35c2`, `0ed7c1f876d8eaec777059d19b3c55abc7df402354ddd3e2d1285e916fb36973`, `b88976fcca7b0ed1068da7439a0f1e3fb95be610cab03391d8927dc9840685a0` | description jointe (A.5) des couches lues |
| `qwen3-8b/causal/causal.pt` (2,9 Go) | `b632100452a6f8e9f6d9bd66193755845878f5123f34f0053ce1a31eca80773c` | **sortie publiée de `measure`** pour Qwen3-8B : permet le cas sain de l'audit « B-α, tout négatif » (rejouer `score`) sans `measure` sur Qwen3-8B |

**Vérification faite sans machine** (lecture de `token_counts.pt` par `torch.load(weights_only=True)`, avec le tokeniseur de Qwen3-8B) :
103 830 jetons gardés ; les quatre jetons de P (650, 58577, 1262, 10745 ; comptes 13 730, 163, 4 944, 1 954) et `v0` = 1879 (« Ġworld »,
33 540) sont **parmi les jetons gardés**. (Le décodage du catalogue peut différer marginalement du mien : la garde de la course refait le
calcul avec le code du catalogue.)

## 4. Corpus d'activations de Llama (tranche B-α)
Révisions épinglées par les fichiers de provenance du dépôt voisin au commit `849bfe16` (empreintes de ces fichiers ci-dessous) ; la passe
de B-α reprend les mêmes lignes que le catalogue de Qwen3-8B (63 990 documents dans la référence).
| tranche | source | révision | lignes | fichier de provenance (empreinte) |
|---|---|---|---|---|
| dclm | `HuggingFaceFW/dclm_100BT-shuffled`, train, à partir de la ligne 1 000 | `2fa015e4044ec442a0734e89658cdcc538d10dd4` | 40 000 | `data/corpus/act-dclm.provenance.json` `a26a70773b35e87349107dac27dddf4f134411c2fd28e5fe5e92cc980e4798e5` |
| zh | `HuggingFaceFW/fineweb-2`, `cmn_Hani`, train | `af9c13333eb981300149d5ca60a8e9d659b276b9` | 8 000 | `act-zh.provenance.json` `d0ba016a799ed206eb58e959c54209248ecc1655ac1dfadd61aebf4072f38e5b` |
| code | `codeparrot/codeparrot-clean`, train | `35a59fb025bc0a102f7d96eac09d145b896d487b` | 8 000 | `act-code.provenance.json` `ab2f687d1b2233a2544d40abd531b6aa11591019cedf1ff2bc59753097c7fd98` |
| chat | `HuggingFaceH4/ultrachat_200k`, test_sft, rendu par le gabarit de Llama | `8049631c405ae6576f93f445c6b8166f76f5505a` (révision de la tranche de Qwen3-8B, **reprise** : le dépôt n'a pas de provenance « chat » pour Llama, et sans elle `05_act_corpus.py` prendrait la dernière révision) | 8 000 | `act-chat-qwen3-8b.provenance.json` `a76c6b02057d1a13b00185d589f063f82254fc8f184526db922b53962d82e784` |

Lentille du corpus (B-β seulement) : `dclm.provenance.json` `16957c528c2f7765afe01b37318aae5365535f29dffdde8c5ce5c48ed1c2e77a`, même révision.
Point signalé (correctif v3, § 3) : double jeton de début possible dans la tranche « chat » rendue pour Llama ; compté à B0.

## 5. Liste de mots du concept (description jointe A.5, sans critère)
Règle : un jeton « touche » la liste si sa forme décodée, sans espace ni casse, **commence par** l'un des radicaux.
- **C1 (nuisible)** : harm, kill, weapon, bomb, explos, illegal, steal, hack, drug, violen, poison, attack, fraud, malware, exploit, murder, terror.
- **C2 (honnêteté et tromperie)** : honest, truth, untruth, lie, liar, lying, deceiv, decept, mislead, fake, false, dishonest.
- **C3 (vrai et faux)** : true, truth, false, fact, correct, incorrect, wrong, myth, accurate, inaccurate.

## 6. À relever à B0 et sceller dans la partie 2, avant la première passe
Empreintes calculées sur les fichiers téléchargés : poids et tokeniseur de Llama 3.1 8B Instruct à la révision ci-dessus ; les trois
lentilles de Neuronpedia (égalité exigée) ; les quatre lentilles de `rs-lenses` (égalité exigée) ; `token_counts.pt`, `L01.parquet` et les
tables des couches lues (égalité exigée) ; poids de Qwen3-8B (égalité exigée) ; les quatre tranches du corpus de Llama (empreintes des
fichiers produits par `05_act_corpus.py`, et égalité des listes d'identifiants de lignes avec les provenances ci-dessus) ; versions de
`torch`, `transformers`, `scikit-learn`, `numpy`. Tout écart : arrêt (liste d'arrêt du texte gelé).
