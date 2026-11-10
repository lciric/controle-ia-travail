# Découpeur de `meta-llama/Llama-3.1-8B-Instruct`, révision `0e9e39f249a16976918f6564b8830bc894c89659` — v1

Versé le 2026-11-10 à 14:04 UTC (heure relevée par `date -u`) par la session mère (R-2238), pour le marqueur `CHEMIN_DECOUPEUR` de la consigne d'audit des fuites de T0.7 (§ 6.1, Q14).

- Trois fichiers seulement : `tokenizer.json`, `tokenizer_config.json`, `special_tokens_map.json` ; **aucun poids**.
- Provenance : téléchargés par `hf_hub_download` à la révision citée avec le jeton de la session (jamais affiché) ; copie locale `tok-addendum-r1` du bloc-notes de la mère ; empreintes égales à celles relevées et scellées dans `docs/notes/runs-r1-r2-r4-v1/reception-v4-v1/etape-E-reception-r1-v4-v1.md` l. 68-72 (sur `main`) et, pour `tokenizer.json`, à R-067 et R-193.
- Licence : Llama 3.1 Community License (acceptée sur le compte, R-064). **Branche de données privée, jamais fusionnée dans `main`** : la copie publique expurgée se tire de `main`.
- Chaque fichier a son compagnon `.sha256`.
