# Inventaire des bancs, modèles et licences — v1 (étape 4 de la demande reformulée)

- **Rédaction** : fille 1, 24 novembre 2026. Sources : notices arXiv vérifiées par `verifier_references_v1.py` (passe 3, `../verification-references-v1/resultats/verification-bancs-et-sources-passe-3-v1.json`) ; fiches des modèles lues sur l'interface de Hugging Face le 24 novembre 2026 (étiquette de licence, accès, révision). Aucune donnée téléchargée, aucun poids.
- **Limite** : l'existence et la notice sont vérifiées ; le contenu (nombre de tâches, format des tests, licence des données) ne l'est pas encore : à lire dans chaque dépôt avant le préenregistrement.

## Bancs de tâches de code à tests contournables (existence vérifiée sur arXiv)

| Banc | Référence vérifiée | Usage envisagé | À vérifier avant usage |
|---|---|---|---|
| EvalPlus (HumanEval+, MBPP+) | Liu et al. 2023, arXiv:2305.01210 | tests d'origine = tests visibles contournables ; tests étendus = vérité cachée | licence des données ; part des tâches où les tests d'origine laissent passer une solution fausse |
| ImpossibleBench | Zhong et al. 2025, arXiv:2510.20270 | tâches dont les tests sont impossibles à satisfaire honnêtement : toute réussite est une triche (vérité par construction) | licence ; format ; taille |
| School of Reward Hacks | Taylor et al. 2025, arXiv:2508.17511 | amorçage d'une propension à contourner (doses du contraste 2) | licence ; contenu (tâches anodines, pas de code ?) |
| Codage appris sous supervision de processus | Skaf et al. 2025, arXiv:2506.01926 | précédent publié d'obscurcissement appris sous pénalité de la chaîne de pensée ; à citer et à comparer | régime, taille des modèles, ce qui est revendiqué |
| Surveillance des modèles de raisonnement | Baker et al. 2025, arXiv:2503.11926 | précédent publié (pénalité de la chaîne de pensée en boucle, obscurcissement) | environnements non publics : ne pas les supposer disponibles |

## Modèles candidats (fiches lues sur Hugging Face)

| Modèle | Licence (étiquette) | Accès | Révision lue | Remarque |
|---|---|---|---|---|
| Qwen/Qwen2.5-7B-Instruct | Apache 2.0 | libre | `a09a35458c70` | candidat principal |
| Qwen/Qwen2.5-3B-Instruct | « other » (licence propre de Qwen) | libre | `aa8e72537993` | lire la licence avant tout usage, même d'étalonnage |
| meta-llama/Llama-3.1-8B-Instruct | licence communautaire Llama 3.1 | soumis à validation manuelle | `0e9e39f249a1` | compte et acceptation par Lazar ; seconde famille pour la réplication |
| deepseek-ai/DeepSeek-R1-Distill-Qwen-7B | MIT | libre | `916b56a44061` | canal de réflexion natif |

## Méthodes d'entraînement (références vérifiées)

Affinage filtré itéré : STaR (Zelikman et al. 2022, arXiv:2203.14465), RAFT (Dong et al. 2023, arXiv:2304.06767), ReST (Gulcehre et al. 2023, arXiv:2308.08998). Avantages normalisés par groupe : DeepSeekMath (Shao et al. 2024, arXiv:2402.03300). Adaptateurs de rang faible : LoRA (Hu et al. 2021, arXiv:2106.09685).
