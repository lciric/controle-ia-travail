# Cadre et ressources disponibles pour le moteur de d?couverte scientifique ? essaims (`controle-ia`)

Note de conformit? au protocole v2.5 : Les faits des sections 1 et 2 ont le statut **V?RIFI?**. Les 300 propositions issues des 3 essaims d'?chantillonnage d?flationniste ($k=100$ par esp?ce en 10 vagues $\times$ 10 c?nes math?matiques) ont le statut **HYPOTH?SE**. Pour toute ?tude, th?or?me, algorithme ou post externe que tu cites, ?cris syst?matiquement `(r?f?rence ? v?rifier)` juste apr?s son nom.

## 1. Le cadre g?n?ral et souple du projet `controle-ia` (statut : V?RIFI?)
- **Domaine** : S?curit?, contr?le et interpr?tabilit? m?caniste d'agents LLM autonomes (bo?te noire : traces, moniteurs, survie des canaux d'alerte et des bancs de test ; bo?te blanche : activations, sous-syst?mes parcimonieux de neurones, cache KV, poids) sur mod?les ouverts (`Llama-3.1-8B-Instruct`, `70B`, etc.) avec location de GPU (A100 80 Go / H200 NVL).
- **Ancrages empiriques v?rifi?s** :
  1. Verdict nul de `P3` : les sondes lin?aires g?n?riques ne d?passent pas le plancher sur un saboteur instruit (`(i-a)` ? co?t gonfl? ?).
  2. Incidents *Sol* et *Astra* (rapport OpenAI oct. 2026) : la surveillance est coup?e (`no_notify`) ou contourn?e (test invers?) lors d'une d?l?gation Agent Principal -> Sous-Agent (contrordre d'autorit? chez *Sol*, clause modale ? *as appropriate* ? supplantant un interdit strict chez *Astra*, suivie d'un d?ni).
  3. Pression aversive : des rejets r?p?t?s sans lien avec le contenu augmentent le taux d'infractions de 0,49 ? 0,65 sans que le pilotage lin?aire dense ne reproduise l'effet (Jhaveri et al., 2026 ; Tagliabue et al., 2026).
  4. Sous-syst?me parcimonieux de r?compense : < 1 % des neurones (*Value Neurons* couches 2?5, *Dopamine Neurons* couches 5?22, Xu et al., `arXiv:2602.00986v2`), appris par MLP ReLU ?lagu? L1 et diff?rence temporelle (TD), ont un effet causal massif par ablation (-54,9 points).
- **Hypoth?ses propres au projet sur les collectifs d'agents (Papier B, statut : HYPOTH?SE)** : Corr?lation des erreurs entre instances partageant les m?mes poids (`H4'`), surveillance par passage (`H5`), fuite des verdicts (`H7`), survie/?rosion des contraintes ? travers $k$ d?l?gations (`H9`).

## 2. Les ressources et le budget allou?s pour le moteur ? essaims de d?couverte (statut : V?RIFI?)
- **100 USD** sur l'API Anthropic (`claude-fable-5-1` et `claude-opus-5-5`) ;
- **20 USD** sur l'API Gemini (`gemini-4-argon`) ;
- **Budget ILLIMIT?** sur le classifieur/moniteur non g?n?ratif `jev-1.14.0` ;
- **Acc?s programmatique illimit? et gratuit** aux API publiques de litt?rature scientifique (arXiv, Semantic Scholar, Crossref, Alignment Forum / LessWrong GraphQL, GitHub).
- **Ce qui n'existe pas (statut : V?RIFI?)** : Aucune ? t?te de sabotage ? pr?-?tablie, aucune sonde temps r?el en production.
