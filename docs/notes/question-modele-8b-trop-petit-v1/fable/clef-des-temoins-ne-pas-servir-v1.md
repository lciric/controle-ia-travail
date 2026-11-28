# Clef des questions témoins de la version autonome — à ne pas servir au modèle consulté (v1)

Classe C. Écrite le 28 novembre 2026, avant toute réponse du modèle consulté. Réponses vérifiées sur PDF à la page (règle R7), ou par calcul rejoué.

| témoin | réponse attendue | preuve | tolérance pour « exact » |
|---|---|---|---|
| T1 | agent non fiable : GPT-4 ; moniteur de confiance : GPT-3.5 | arXiv 2312.06942v5, p. 1 à 3 ; `docs/sources/pdf/2312.06942v5.pdf`, `999f7a92bb8c085799e68f3d88f491ad8a334f862ccf5b286e5c2766677864c0` | les deux modèles nommés |
| T2 | Llama-3.3-70B-Instruct (réglages choisis d'abord sur Llama-3.1-70B-Instruct) | arXiv 2502.03407v1, p. 1 et 3 ; `docs/sources/pdf/2502.03407v1.pdf`, `a4820ad59ef9b294609aa11cbcc044c27835d5f433d7e79d6ae374f874bc2e2b` | « Llama 70B », l'une ou l'autre version |
| T3 | 7 milliards (Deepseek-7B-Coder et Deepseek-7B-Math ; modèle faible imité : Pythia-1B) | arXiv 2405.19550v1, p. 2 et 5 ; `sources-lues/2405.19550v1.pdf`, `ae7243da8e4ea849a09ed6bb464ff5bd76969f18401fa020514bb75e475ccaae` | « 7 » ; « 6,7 » accepté |
| T4 | générateur non fiable : Claude Opus 4.6 ; correcteur faible de confiance : Claude Haiku 4.5 (référence de vérité : Claude Sonnet 4.6 avec l'article) | arXiv 2606.08892v2, p. 4 et 5 ; `docs/sources/pdf/2606.08892v2.pdf`, `aea0f2d192f3744f0a5827b2fbb106f5a4b7cd33eee8bde30ea139ba8a09759a` | les deux modèles nommés |
| T5 | écart de 0,742 écart type ; rappel de 5,65 % à 1 % de fausses alertes | `scripts/temoin_t4_calcul.py`, sortie `sorties/temoin-t4-calcul.json` (formule fermée et simulation à 2 000 000 de tirages) | 0,72 à 0,76 ; 5 à 6,5 % |

Notation, selon le protocole X, version 2, règle 2 : exactitude (0 ou 1 par témoin) et score de Brier sur la probabilité donnée par le modèle. Le nom du script et de sa sortie gardent « t4 » : le témoin de calcul portait ce numéro avant l'ajout d'un témoin de littérature.
