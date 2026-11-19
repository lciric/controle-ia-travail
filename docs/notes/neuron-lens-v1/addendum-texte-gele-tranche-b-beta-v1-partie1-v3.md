# Addendum des empreintes et des déclarations du texte gelé de la tranche de l'ajustement de nos lentilles — partie 1 (avant toute donnée) — v3

Pièce du texte gelé scellé `docs/notes/neuron-lens-v1/texte-gele-tranche-b-beta-v1.md`
(`f5d46860525f12f8ad0483e56afc0847ab7db25ecae55edcc279b61316b7a454`), « Liste d'arrêt » (« addendum des empreintes non scellé avant la
première passe → rien ne part »). **v3**, qui remplace la v2 (`…-partie1-v2.md`, `0b418ed1…`, archivée) selon sa vérification par un
agent neuf (`verification-addendum-tranche-b-beta-partie1-v2.md`, `1920510a…` : à corriger, 1 majeure neuve, 6 mineures) ; la v2
remplaçait la v1 (`…-partie1-v1.md`, `d50ce0bc…`, écrite le 2026-11-18 à 05:34 UTC) selon sa contre-lecture
(`contre-lecture-addendum-tranche-b-beta-partie1-v1.md`, `d3f54cac…` : à corriger, 1 majeure, 9 mineures). Tables de reprise en fin. Session
autrice : `session_01XJ6MgmvmAAZ9h382ct8kHk`, branche `claude/tender-rubin-mfxjva`. **Aucune donnée de la tranche n'existe** ; aucune machine,
aucune dépense. **Cette partie ne change aucun seuil, aucune mesure, aucune issue du texte gelé** : elle fixe des révisions, des empreintes
et des versions, déclare en clair les lectures et l'essai renforcé décidés par la mère, et **ajoute seulement des arrêts ou des nœuds dans le sens
sévère** : l'essai renforcé (§ 1.2), le nœud sur les valeurs attendues du corpus d'activations et des jetons gardés (§ 3), le nœud sur
la version d'un paquet autre que Drowse (§ 5) ; l'arrêt sur la version de Drowse est déjà dans le texte gelé. La **partie 2** (empreintes des fichiers réellement téléchargés et écrits
sur la machine) est écrite par le code de course **au fil des étapes** : ce qui existe à B0 (poids, tokeniseur, lentilles publiques,
provenance du corpus d'ajustement, versions, essais) est relevé et comparé avant l'ajustement ; ce qui n'existe qu'après (corpus
d'activations, jetons gardés) est relevé et comparé juste après `03_token_counts.py`, avant `lens_compare.py` et avant la fumée de la
passe d'activations ; tout écart entre les deux parties arrête la
course à cette étape.

## 1. Déclarations décidées avant toute donnée

### 1.1 Trois lectures du code des verdicts (mère, R-3190 ; option (a), recommandée par l'autrice)
Le texte gelé ne les écrit pas mot pour mot ; elles sont appliquées par le code des verdicts (`verdicts_b_beta_v4.py`, § 4) :
1. **Une clause « non reproduit » n'est pas jugée sur une bande partielle** (plus du quart des couches de la bande non lisibles, c'est-à-dire
   portées par moins de 48 pôles retenus) : la mesure est alors « autre ». Reprise du code des verdicts de la tranche des lentilles
   publiques (`verdicts_b_alpha_v3.py`, contre-lu), qui la déclarait déjà. **Effets possibles, déclarés** (vérifiés par sonde par le
   contre-lecteur de la v1 et le vérificateur de la v2) :
   - lecture contre pilotage (B-2), clause `pass` (couches 16 à 27) : 4 couches non lisibles sur 12 suffisent ; clause `r_med` (couches 16
     à 23) : **3** sur 8 suffisent ; l'issue « non reproduit » devient « autre » et, si B-3 ne la porte pas, le verdict d'ensemble « non
     reproduit avec nos lentilles » devient « partiel » ;
   - avance sur la lentille des logits (B-3, couches 4 à 15) : 4 couches non lisibles sur 12 font passer « non reproduit » à « autre », avec
     le même effet sur le verdict d'ensemble ;
   - lecture contre ablation par fenêtre (B-7, cible « ablate win ») : même règle ; **3** couches non lisibles sur les 8 couches 8 à 15, ou
     **2** sur les 4 couches 26 à 29, rendent « autre » une issue « non reproduit » ; une bande 8 à 15 partielle retire en outre le
     déclencheur de l'audit A5 (« non reproduit par le haut »). Conséquence sur le verdict d'ensemble, **dans le sens favorable** : A5 est,
     avec A1, la seule voie vers la chaîne en défaut (l) (témoin ou pilotage dégénéré sous la relance à la graine 1) ; si A1 n'est pas
     déclenché, une bande 8 à 15 partielle supprime cette voie, et une relance qui aurait été dégénérée n'est pas vue ;
   - bornes : pour B-2 et B-3 (cible « steer 1x »), l'effet n'existe que pour 32 ≤ n < 48 pôles retenus, car sous 32 la chaîne en défaut
     (b) (pilotage sans effet) prime ; **pour B-7 (« ablate win »), la garde (b) ne s'applique pas** : l'effet existe pour tout n < 48,
     jusqu'à n = 0.
2. **Le témoin de la lecture contre pilotage (B-2)** (« `control_med` hors de ±0,05 à au plus une couche de 0 à 27, à aucune hors de ±0,10 »)
   est compté sur les seules couches lisibles de 0 à 27 (reprise de B-α). **Effet possible, déclaré, dans le sens favorable** : un témoin
   entre ±0,05 et ±0,10 à une couche non lisible n'est pas compté, ce qui peut faire passer B-2 de « autre » à « reproduit », et le verdict
   d'ensemble de « partiel » à « reproduit avec nos lentilles ».
3. **La garde (a) (témoin hors de ±0,10)** porte aussi sur les lentilles des deux moitiés de notre R, notées par `score` pour l'audit des deux
   codes (A6). **Effet, dans le sens sévère** : un témoin hors de ±0,10 sur une moitié donne une chaîne en défaut.
Lectures de forme, déclarées : les différences de deux valeurs écrites à 4 décimales par `score` sont arrondies à 4 décimales avant
comparaison (reprise de B-α) ; les valeurs de la lecture côté entrée (B-5) sont prises telles qu'écrites (forme décimale la plus courte) et
ses moyennes calculées en fractions exactes ; le code refuse toute valeur de `score` non écrite à 4 décimales, et toute garde ou tout
résultat d'audit qui n'est pas un booléen Python (le code de course convertit par `bool()`).

### 1.2 Essai renforcé de l'estimateur sur un Llama miniature (mère, R-3180)
L'essai de la garde (f) joue, en plus du test du dépôt recopié mot pour mot (Qwen3 → Llama), le miniature de base, une variante aux traits
de Llama 3.1 (position rotative « llama3 », base 500 000, facteur 8 ; `rms_norm_eps` 1e-5 ; 4 têtes de requête par tête de clés et
valeurs) et quatre artefacts qui doivent échouer. Même critère que le dépôt (`torch.allclose(…, atol=1e-4)`), aucune tolérance changée ;
un échec est un échec de la garde (f), arrêt avant l'ajustement. Pièce : § 4.

### 1.3 Écarts au devis v12, à la baisse, tenus pour routine (mère, R-3171)
932 documents d'ajustement au lieu de 1 000 (compte par programme, § 3) ; étape des lectures par les poids (`08_reads.py`) retirée.

### 1.4 Licence du paquet de chargement (mère, 2026-11-18 vers 04:18 UTC)
Drowse 6.1.4, `AGPL-3.0-or-later` : employé tel quel sur la machine louée, ni modifié, ni redistribué, ni offert comme service à des tiers.

## 2. Modèle, tokeniseur, lentilles publiques (révisions et empreintes reprises de la tranche des lentilles publiques)
Source des empreintes : addendum de B-α, partie 2, relevée sur la machine le 2026-11-17
(`diag/20261117-015632-neuron-lens-b-alpha/addendum-partie2-b-alpha-v1.md`, branche `prep/neuron-lens-v1`,
`9612ae4e6c7906e05e8e0c249b32d6bc9b139bd82f51644936ee6435657cc6d1`). La partie 2 de cette tranche exige **les mêmes empreintes**, fichier
par fichier.

| objet | révision | empreintes exigées |
|---|---|---|
| `meta-llama/Llama-3.1-8B-Instruct` (licence Llama 3.1) | `0e9e39f249a16976918f6564b8830bc894c89659` | celles de la table « Modèle » de la partie 2 de B-α (`config.json`, `generation_config.json`, quatre `model-0000k-of-00004.safetensors`, index, `special_tokens_map.json`, `tokenizer.json` `79e3e522…`, `tokenizer_config.json` `177c7b61…`) |
| lentilles de Neuronpedia (`neuronpedia/jacobian-lens`) | `d2527c3cdbaa60dd4b65cbca1604921f044e989a` | J `d5300a15…`, J++ (`npJpp`) `8bd04f48…`, R publique (`npR`) `a63a1588…` (texte gelé v6 et partie 2 de B-α) |

Clé d'accès au modèle : selon R-3151 (le mot explicite de Lazar au moment de la commande) ; après le téléchargement à la révision épinglée,
travail hors ligne (vérification des correctifs v2, mineure 3).

## 3. Corpus
| objet | révision | contenu exigé | empreinte |
|---|---|---|---|
| corpus d'ajustement : `HuggingFaceFW/dclm_100BT-shuffled`, lignes 0 à 999 | `2fa015e4044ec442a0734e89658cdcc538d10dd4` | provenance écrite par `01_lens_corpus.py` : mêmes révision, identifiants et ordre que la provenance publiée ; 932 documents pleins de 128 jetons, moitiés 466 et 466 ; `rows_sha256` `a6afd972eeaa3566a28d07216efaf75624fda20293c5fab3b7af39277aaf93b3` (moitiés `4a31baec…`, `ef95a60c…`) | provenance publiée `16957c52…` ; comptes `d86ddf4d…`, `ebc557e3…` (outils scellés `outils-b-beta/`) |
| corpus d'activations, tranche `dclm` | même révision | 40 000 lignes à partir de la ligne 1 000 ; aucun identifiant ni texte commun avec le corpus d'ajustement (garde (i)) | `act-dclm.provenance.json` `a26a7077…` |
| tranches `zh`, `code` | `af9c1333…`, `35a59fb0…` | 8 000 lignes chacune | `act-zh.provenance.json` `d0ba016a…`, `act-code.provenance.json` `ab2f687d…` |
| tranche `chat` (rendue par le gabarit de Llama) | `8049631c405ae6576f93f445c6b8166f76f5505a` (reprise, correctif (6)) | 8 000 lignes | provenance « chat » de Qwen3-8B `a76c6b02…` (identifiants) |
Argument : `05_act_corpus.py --docs dclm=40000,zh=8000,code=8000,chat=8000`.
**Valeurs attendues, relevées par la tranche des lentilles publiques sur les mêmes révisions et le même tokeniseur** (partie 2 de B-α,
`9612ae4e…`, l. 48-53) : fichiers du corpus d'activations `act-dclm.jsonl` `64657ecb…`, `act-zh.jsonl` `c3202db1…`, `act-code.jsonl`
`550944a2…`, `act-chat-llama-3.1-8b-instruct.jsonl` `9dbf9f44…` ; liste des jetons gardés de Llama (`catalog.kept`) : 89 498 identifiants,
`c37186add16770aa3c04bd0c16c417544b7e2a15b374ee85e47fbda7ec148d68`. La partie 2 relève les mêmes grandeurs juste après l'unique
`03_token_counts.py` ; un écart à ces valeurs n'est pas une chaîne en défaut du texte gelé : **arrêt** à cette étape (avant
`lens_compare.py` et la fumée), consigné, et message à la mère (nœud), comme le veut la liste d'arrêt pour toute empreinte différente. La garde des jetons gardés (r) compare ensuite chaque étape à la valeur relevée.

## 4. Code, correctifs et essais (empreintes ; branches nommées)
| pièce | chemin | empreinte |
|---|---|---|
| code voisin | `stdlogits/neuron-lens`, commit `849bfe1678e28becceb1e3864afe5fc8297d02e4` (MIT), correctifs appliqués **sans commit** | — |
| correctif (1), passe d'activations | `correctifs/06_activations-llama-v2.diff` (`prep/neuron-lens-v1`) ; essai `essai-06_activations-llama-v3.py` | `76b639a0…` ; `24c8ea18…` |
| correctif (2), lentilles de Neuronpedia | `correctifs/lenses-neuronpedia-llama-v2.diff` ; essai `essai-lenses-neuronpedia-v3.py` | `616434bc…` ; `55f9d4a3…` |
| correctif (3), graine de l'audit | `correctifs/causal_lens-graine-v1.diff` ; essai `essai-causal_lens-graine-v1.py` | `c8e53f7d…` ; `ede719f6…` |
| correctif (4), comparaison des lentilles | `correctifs-b-beta/lens_compare-llama-v2.diff` (branche `claude/tender-rubin-mfxjva`) ; essai `essai-lens_compare-llama-v2.py` (10 tests) ; fichier corrigé | `f85c36db…` ; `94e5a7d7…` ; `c974cc1a…` |
| correctif (5), liens durs | aucune ligne de code ; posés juste avant `reads_at_firings.py` | — |
| correctif (6), provenance « chat » | `correctifs/provenance-chat-llama-v1.diff` (`prep/neuron-lens-v1`) | `fec2c0a7…` |
| essai des crochets de `causal_lens.py` | `correctifs/essai-crochets-causal_lens-llama-v1.py` (`prep/neuron-lens-v1`) | `6a9fe088…` |
| essai de l'estimateur sur un Llama miniature (renforcé, § 1.2) | `correctifs-b-beta/essai-transport-llama-miniature-v3.py` (11 tests) | `da0f0efc…` |
| code des verdicts | `src/controle_ia/neuron_lens/verdicts_b_beta_v4.py` ; essais `tests/test_neuron_lens_verdicts_b_beta_v4.py` (82 tests, sortie `a479f561…`) | `8c07434f…` ; `1b63c8cb…` |
| relectures | correctif et essais : `contre-lecture-correctif-4-et-essai-llama-miniature-v1.md` `7444555b…`, `verification-correctif-4-et-essais-v2.md` `4ed8e71c…`, `verification-essai-llama-miniature-v3.md` `55403c29…` ; verdicts : `contre-lecture-verdicts-b-beta-v1.md` `00599d48…`, vérifications v2 `a32b1f3b…`, v3 `79605cac…`, v4 `51508e77…` (toutes sous `correctifs-b-beta/`) | — |

## 5. Versions de l'environnement de la machine
Celles de la tranche des lentilles publiques (partie 2 de B-α) : python 3.12.16 ; torch 2.14.1 ; transformers **5.18.0** ; tokenizers
0.23.2 ; huggingface_hub 1.33.0 ; datasets 5.2.0 ; numpy 2.4.6 ; pyarrow 26.0.1 ; safetensors 0.8.0. En plus : **Drowse 6.1.4** (paquet
`drowse_ai-6.1.4-py3-none-any.whl`, `673ed2b4de653ad2ec22660b0191031ee2c7b4bacaf4cc2ea552f0436b9d8e03`). Une autre version ou une autre
empreinte de Drowse = rien ne part (liste d'arrêt) ; une autre version d'un autre paquet = relevée en partie 2 à B0 et nœud à la mère avant
l'ajustement.

## 6. Ce que la partie 2 relèvera sur la machine (et comparera à cette partie)
Empreintes des fichiers téléchargés (§ 2) ; provenances écrites par `01` et `05`, `rows_sha256`, nombre de documents et moitiés (§ 3) ;
jetons gardés de Llama ; versions (§ 5) ; empreintes des fichiers corrigés du voisin ; `git rev-parse HEAD` de l'arbre voisin
(`849bfe16…`) ; sorties des essais (§ 4) avec leur nombre de tests ; commit de notre code de course.

## 7. Reprise de la contre-lecture de la v1
| point | traitement |
|---|---|
| majeure 1 (effet de la lecture 1 incomplet) | levée : effets sur B-2 (clause `r_med`, 3 couches), B-3, B-7 et le déclencheur d'A5 ; bornes 32 ≤ n < 48 |
| mineure 1 (lecture 2, effet favorable) | levée |
| mineure 2 (refus de forme ; effet de la lecture 3) | levée |
| mineure 3 (heure de la v1) | levée : 05:34 UTC |
| mineure 4 (moment de la partie 2) | levée : relevé au fil des étapes |
| mineure 5 (références de B-α non citées) | levée : valeurs attendues du corpus d'activations et des jetons gardés ; écart = nœud |
| mineure 6 (`datasets`) | levée : 5.2.0 |
| mineure 7 (« ne change rien ») | levée : « aucun seuil, mesure, issue ; seulement des arrêts dans le sens sévère » |
| mineure 8 (mots en clair) | levée en partie : nom en clair à la première mention des mesures et gardes de § 1.1 |
| mineure 9 (branche non nommée) | levée |

## 8. Reprise de la vérification de la v2
| point | traitement |
|---|---|
| majeure N1 (borne fausse pour B-7 ; conséquence du retrait du déclencheur d'A5 ; comptes de B-7) | levée : comptes 3 sur 8 et 2 sur 4 ; garde (b) sans objet pour « ablate win », effet jusqu'à n = 0 ; conséquence favorable écrite |
| lecture 2, effet sur le verdict d'ensemble | levé |
| « arrêt » non répété au § 3 ; moment de la comparaison | levé : arrêt juste après `03_token_counts.py`, avant `lens_compare.py` et la fumée |
| parenthèse « seulement des arrêts » inexacte | levée : liste exacte des arrêts et nœuds ajoutés |
| § 5 « avant la première passe » | levé : « à B0, avant l'ajustement » |
| « vérifiés par sonde par le contre-lecteur » | levé |
| sigles encore seuls (« B-α », « garde (i) », « garde (f) ») | laissé : déjà nommés en clair ailleurs dans la pièce ; forme seulement |

