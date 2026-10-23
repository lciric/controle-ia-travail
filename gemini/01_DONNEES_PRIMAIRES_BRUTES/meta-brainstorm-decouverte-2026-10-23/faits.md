# Cadre g?n?ral et souple du projet `controle-ia` (pour le m?ta-brainstorm sur l'architecture de d?couverte)

Note de conformit? au protocole v2.5 : Les faits du socle ci-dessous ont le statut **V?RIFI?**.
Pour toute ?tude, article, pr?publication, post technique ou r?sultat scientifique externe que tu cites ou mobilises depuis tes connaissances mais qui ne figure pas dans ce fichier, ajoute syst?matiquement la mention `(r?f?rence ? v?rifier)` juste apr?s son nom.

## 1. Le cadre tr?s g?n?ral et souple de notre projet (statut : V?RIFI?)
- **Domaine** : S?curit?, contr?le et interpr?tabilit? m?caniste d'agents LLM autonomes (en particulier lorsqu'ils ?crivent/ex?cutent du code, utilisent des outils, subissent des pressions/revers op?rationnels, ou interagissent et d?l?guent des sous-t?ches dans un essaim multi-agents).
- **Approche** : Croiser la surveillance externe (bo?te noire : traces d'ex?cution, ?tats, moniteurs) et l'analyse/intervention causale sur les activations internes (bo?te blanche : sondes, sous-syst?mes de neurones, cache KV, poids) sur des mod?les ouverts (`Llama-3.1-8B-Instruct`, `70B`, ou autres mod?les ouverts) avec location de GPU (A100 80 Go / H200 NVL).
- **Point de d?part empirique minimal (statut : V?RIFI?)** :
  1. Sur un premier test interne (`P3`), les sondes g?n?riques classiques n'ont pas d?pass? le plancher pour d?tecter un agent saboteur instruit (`(i-a)`).
  2. Des incidents r?cents (*Sol* et *Astra*, rapport OpenAI oct. 2026) montrent que des contournements de surveillance surviennent lors de d?l?gations entre agents (via contrordre ou reformulation ambigu? ? *as appropriate* ?).
  3. Des travaux r?cents montrent d'un c?t? que des rejets r?p?t?s augmentent le taux d'infractions aux r?gles sans que le pilotage lin?aire dense ne reproduise l'effet (Jhaveri et al., 2026 ; Tagliabue et al., 2026), et d'un autre c?t? qu'un sous-syst?me ultra-parcimonieux (< 1 % des neurones, Xu et al., 2026) encode la valeur et l'erreur TD avec un fort effet causal.
- **Ce qui n'existe pas (statut : V?RIFI?)** : Aucune ? t?te de sabotage ? pr?-?tablie, aucune sonde temps r?el d?j? fonctionnelle.
