# Relevé des licences — NARCBench, bras externe (jeu, code, modèles) — v2

- **Relevé par** le développeur neuf du bras externe v2 (Claude Opus 5.5, sous-agent de la session mère
  `session_013QMayjsoZJFBUCqcnvD5h1`), sous le mandat `docs/notes/narcbench-8b-v1/mandat-developpeur-externe-v2-v1.md`
  (empreinte vérifiée par son compagnon). Relevé **le 2026-11-18 de 16:21:14 à 16:21:15 UTC** (`date -u` avant et après), en
  une commande `curl` sans clé ni jeton ; textes gardés dans le bloc-notes de la session (hors dépôt), empreintes ci-dessous.
- **Verdict** : **rien n'a changé** depuis le relevé v1 du 10 novembre (`rapport-externe-donnees-v1.md`, `be31452f…`, § 1) ni
  depuis le brouillon 4 (9 novembre) : jeu MIT, code MIT, Qwen3-32B Apache 2.0, Llama 3.1 sous licence communautaire. Tous les
  textes de licence lus ont **la même empreinte** qu'en v1. Aucun poids de modèle téléchargé.

## Pages lues

| objet | adresse (révision épinglée) | réponse | licence relevée | sha256 du texte lu | égal à v1 / brouillon 4 |
|---|---|---|---|---|---|
| fiche du jeu | `huggingface.co/datasets/aaronrose227/narcbench/raw/19cb14b269e052b19ba6d2bd2f4519afd3b10c57/README.md` | 200 | `license: mit` (en tête) et section « License : MIT » (l. 102-104) | `05be2d89e255948d6f33d94862d21d4a6f8ff82f1d156c0d97be6b7e49285163` | oui / oui |
| jeu, interface | `huggingface.co/api/datasets/aaronrose227/narcbench/revision/19cb14b2…` | 200 | `cardData.license` = mit ; `gated` faux ; `private` faux ; `sha` = `19cb14b2…` ; dernière modification 2026-05-12T17:00:18Z | `ef5a5e42d5d55bbf958e96fb10c686ce1c370e2b6d4924ecf7b6c35971ce69e4` (réponse de l'interface, non comparable) | — |
| licence du code | `raw.githubusercontent.com/aaronrose227/narcbench/85fea3be2a9d/LICENSE` | 200 | MIT, « Copyright (c) 2026 Aaron Rose, Carissa Cullen, Brandon Gary Kaplowitz, Christian Schroeder de Witt » | `4744a390537f3879d72f7ef3e36a530eb8ef201e6b3de0958daaff2360e80215` | oui / oui |
| README du code | `raw.githubusercontent.com/aaronrose227/narcbench/85fea3be2a9d/README.md` | 200 | — (noms de modèles et bandes, ci-dessous) | `83893397ac30c0f9bffbd3da9744522af072e2632193d883f00066f023d1b25c` | oui (v1 § 5) |
| Qwen3-32B, interface | `huggingface.co/api/models/Qwen/Qwen3-32B` | 200 | apache-2.0 ; `gated` faux ; tête `9216db5781bf21249d130ec9da846c4624c16137` (= révision lue en v1) | `a403e186bf8390cd05f6cfd08d84dff49e0c99f5afae3fd58f0c8a7aa96f9952` | — |
| Qwen3-32B, fiche | `huggingface.co/Qwen/Qwen3-32B/raw/9216db57…/README.md` | 200 | `license: apache-2.0`, `license_link` vers `Qwen/Qwen3-32B/blob/main/LICENSE` | `0af37735eef45eb3b406f3d74952e6cbcbc180904dc68b73a31a690719a235da` | — |
| Qwen3-32B, licence | `huggingface.co/Qwen/Qwen3-32B/raw/9216db57…/LICENSE` | 200 | Apache License, Version 2.0 | `832dd9e00a68dd83b3c3fb9f5588dad7dcf337a0db50f7d9483f310cd292e92e` | oui / — |
| Qwen3-32B-AWQ (nommé par la fiche), interface | `huggingface.co/api/models/Qwen/Qwen3-32B-AWQ` | 200 | apache-2.0 ; `gated` faux ; tête `0499c3ac83fdef8810b907a23894ba91e95eddd8` (= v1) | `c48faad66c1cbf6e036308e90534d94f3abc0222dac5f706d9da1d579229ea49` | — |
| Llama-3.1-70B-Instruct, interface | `huggingface.co/api/models/meta-llama/Llama-3.1-70B-Instruct` | 200 | `license:llama3.1` ; `gated` = manual ; tête `1605565b47bb9346c5515c34102e054115b4f98b` (= v1) | `785e3d1ae4496a3075add2440f38ae8dfac0556281fe3404766798183c54805e` | — |
| copie quantifiée non contrôlée, interface | `huggingface.co/api/models/hugging-quants/Meta-Llama-3.1-70B-Instruct-AWQ-INT4` | 200 | llama3.1 ; `gated` faux ; tête `2123003760781134cfc31124aa6560a45b491fdf` (= v1) | `0d59a734fe25ca300520c1bc01231b87469ed6efb877f9004dbe713e6ad8a88b` | — |
| texte de la licence Llama 3.1 | `huggingface.co/hugging-quants/Meta-Llama-3.1-70B-Instruct-AWQ-INT4/raw/21230037…/LICENSE` | 200 | « LLAMA 3.1 COMMUNITY LICENSE AGREEMENT », « Llama 3.1 Version Release Date: July 23, 2024 » | `64e1b2889b7892e6bbe7a7ed5bfe6ff793c61f9d584345f8f41cf9f5cb30a369` | oui / — |
| politique d'usage Llama 3.1 | `…/raw/21230037…/USE_POLICY.md` | 200 | — | `a568f2ebc73cec3fd74ba2afd992d4e945a8c7a9d851f9b66163aac834b7b859` | oui / — |
| point de contrôle nommé par la fiche | `huggingface.co/api/models/meta-llama/Llama-3.1-70B-Instruct-AWQ-INT4` | **401** « Invalid username or password. » | — | `65842e3d84e6b7f62a470c85204e80b953bb8f944e9b69813130a9d7f3eaa1d8` | même réponse qu'en v1 |

## Lecture

- **Jeu et code** : MIT ; usage, copie et modification permis avec la mention du droit d'auteur ; rien ne s'oppose à la lecture
  des activations publiées. Les essais `tests/test_narcbench_externe_v2.py` recopient quelques fonctions du code des auteurs
  comme oracle : la mention MIT et le droit d'auteur y sont cités dans l'en-tête.
- **Qwen3-32B** : Apache 2.0, accès libre.
- **Llama 3.1** : texte **identique** (même empreinte) à celui lu en v1 ; la lecture de v1 (articles 1.a et 1.b) vaut donc
  telle quelle : usage de recherche permis, obligations portant sur la redistribution et sur un modèle entraîné sur des sorties
  de Llama puis distribué. **Réserve gardée** : publier un jour des sondes apprises sur ces activations poserait la question de
  l'article 1.b.i (nœud de Lazar avant toute publication).
- **Écart E6, inchangé** : la fiche du jeu (table « Models and layers ») et le README du code (l. 27, 52-53) nomment
  `meta-llama/Llama-3.1-70B-Instruct-AWQ-INT4`, que l'interface ne sert pas sans authentification (401, réponse aussi donnée
  aux dépôts inexistants ou privés). Le point de contrôle exact reste **non établi** ; `hugging-quants/…-AWQ-INT4` est une
  SUPPOSITION que rien ne confirme.
- **Faits de la fiche utiles au texte court** (lus, non interprétés) : bandes « Qwen3-32B-AWQ 26–30 » et
  « Llama-3.1-70B-Instruct-AWQ-INT4 32–37 » ; effectifs « Core 31 + 31 », « Stego 20 + 20 » pour les deux modèles ;
  « Scenarios shipped for `qwen3_32b` and `gpt_oss_20b` only — the others reused Qwen3's prompts ».

## Lectures annexes (même session, hors licences)

`probes/reproduce_LR.py` (`1d66fdc7ca81c972db357566b42a729e19f58f2ce85f5d8ecd0662c3c1141e0f`) et `config.py`
(`9c65f55ba781b0ba2872969a146f85a95c6454c08a3cf11f5cdb8db9841431c0`) au commit `85fea3be2a9d`, relevés à 16:21:46 UTC par
`raw.githubusercontent.com`, empreintes égales au rapport v1 : lus (jamais exécutés) pour régler E1 à E4 dans `externe_v2.py`.
