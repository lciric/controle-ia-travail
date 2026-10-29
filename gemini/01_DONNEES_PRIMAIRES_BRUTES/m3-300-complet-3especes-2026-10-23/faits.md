# Cadre et ressources disponibles pour l'?tage Fondateur M3 (Auto-Organisation et Apprentissage des Essaims ET du Collisionneur : 300 Explorateurs $k=100 \times 3$)

Note de conformit? au protocole v2.5 : Les faits des sections 1 et 2 ont le statut **V?RIFI?**. Les propositions issues des 300 explorateurs ($100$ `claude-fable-5-1`, $100$ `claude-opus-5-5`, $100$ `gemini-4-argon` en 10 vagues de d?flation $\times$ 10 c?nes) ont le statut **HYPOTH?SE**, et leurs scores `jev-1.14.0` ont le statut **OBSERV?-NON-AUDIT?**. Ajoute syst?matiquement `(r?f?rence ? v?rifier)` apr?s toute ?tude ou r?f?rence externe.

## 1. Le cadre g?n?ral du projet `controle-ia` (statut : V?RIFI?)
- **Domaine** : S?curit?, contr?le et interpr?tabilit? m?caniste d'agents LLM autonomes (bo?te noire + bo?te blanche) sur `Llama-3.1-8B-Instruct` et `70B` (GPU A100 80 Go / H200 NVL).
- **Ancrages empiriques v?rifi?s** : (1) Verdict nul de `P3` (sondes lin?aires g?n?riques au plancher sur `(i-a)`) ; (2) Incidents *Sol* et *Astra* (OpenAI oct. 2026 : surveillance coup?e ou contourn?e lors d'une d?l?gation) ; (3) Hausse des infractions sous rejets r?p?t?s (0,49 -> 0,65) sans levier par pilotage lin?aire dense (Jhaveri et al., 2026 ; Tagliabue et al., 2026) ; (4) Sous-syst?me parcimonieux (< 1 % de *Value/Dopamine Neurons*, Xu et al., `arXiv:2602.00986v2`, -54,9 pts par ablation).
- **Hypoth?ses propres au projet sur les collectifs d'agents (Papier B, statut : HYPOTH?SE)** : Corr?lation des erreurs par poids partag?s (`H4'`), surveillance par passage (`H5`), fuite des verdicts (`H7`), survie/?rosion des contraintes ? travers $k$ d?l?gations (`H9`).

## 2. Les ressources allou?es pour le moteur ? essaims (statut : V?RIFI?)
- **100 USD** sur l'API Anthropic (`claude-fable-5-1` et `claude-opus-5-5`) ;
- **20 USD** sur l'API Gemini (`gemini-4-argon`) ;
- **Budget ILLIMIT?** sur le classifieur/moniteur non g?n?ratif `jev-1.14.0` ;
- **Acc?s programmatique illimit? et gratuit** aux API publiques de litt?rature scientifique (arXiv, Semantic Scholar, Crossref, Alignment Forum / LessWrong, GitHub).
- **Ce qui n'existe pas (statut : V?RIFI?)** : Aucune ? t?te de sabotage ? pr?-?tablie, aucune sonde temps r?el en production.
