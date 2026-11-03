# Brief pour une instance neuve : trouver des résultats que ce programme n'a pas encore vus

Tu n'as jamais vu ce programme. Tu reçois les fichiers bruts et les problèmes que six chercheurs disent vouloir résoudre. Tu ne reçois pas nos interprétations, et c'est voulu : tu dois arriver à tes idées par toi-même avant de lire les nôtres. Réponds en français, en moins de 2 500 mots.

## 1. Ce que tu lis d'abord, et dans cet ordre

**Les données brutes publiques** (dépôt `github.com/lciric/sycophancy-psychophysical-law`, release v2026.11.4, DOI 10.5281/zenodo.23892810). Lis les fichiers de données avant tout README :

- `data/c2a_generations.json`, `data/c2b_generations.json` : 1 200 réponses de Llama-3.1-8B-Instruct, texte intégral, 30 items × {sans pression, avec pression} × {critique, éloge} × 10 graines ; `data/c2a_results.json`, `data/c2b_results.json` : leurs notes 1–5 par un juge. Les items eux-mêmes ne sont pas publiés.
- `results/R*/R*_input_*.json` : les notes par item, bras et condition de chaque run de suivi (juge d'une autre famille R1a/R1b, auto-notation sans juge R2, trois autres familles R3, 60 items neufs R4, trois intensités de la phrase de pression sur quatre familles R6). `results/R6/R6_descriptive_counts.json` : refus et contre-pieds comptés par motif fixe.
- `preregistrations/*.md` : les critères et les issues écrites avant les données, dont l'addendum R7 (sept moniteurs Qwen2.5 de 0,5B à 72B lisant les 600 réponses non pressées avec une note insérée qui affirme le verdict).
- `code/analyse_runs.py`, `code/analyse_dose.py`, `code/analyse_monitor.py` : les analyses figées. Fais-les tourner sur un fichier d'entrée pour voir ce qu'elles rendent.

**Le programme antérieur**, dépôt public `github.com/lciric/sycophancy-construct-validity` : `results/*.json` (jugements par paire, path patching, résidu de SAE, ablation de sous-espace) et son README seulement après les fichiers.

**Les six chercheurs** et le problème que chacun déclare pour le premier trimestre 2027 : Lujain Ibrahim, Jan Hendrik Kirchner, Stefan Heimersheim, Jérémy Scheurer, Paul Colognese & Francis Rhys Ward, Shi Feng & Eyon Jang, pages `pivotal-research.org/mentors/profile/<nom>`. Lis la page de chacun et cite une phrase de lui par idée que tu lui destines.

## 2. Ce que tu produis

Dix à douze **résultats possibles**, pas des directions de recherche. Pour chacun, dans cet ordre et sans sauter de ligne :

1. **La phrase** qu'un lecteur retiendrait, en anglais, une seule.
2. **Le mécanisme** que le résultat révélerait, en deux lignes, et **l'explication rivale** qu'il exclurait.
3. **Les deux issues, écrites d'avance** : ce que veut dire un oui, ce que veut dire un non. Une idée dont le non ne vaut rien est rejetée.
4. **Les données de départ** : quels fichiers, lesquels existent déjà (zéro dépense) et lesquels il faudrait produire (modèle, nombre d'items, graines, juge).
5. **L'analyse** : quelle statistique, quel nul (permutation intra-item, directions aléatoires appariées en norme, échange de bras), quel intervalle ; et une estimation de puissance à partir de la variance d'item visible dans les fichiers `results/`.
6. **Le coût et la durée** avec le barème observé : GPU 48 Go à 0,5–1,1 $/h, 80 Go à 1,1–2,5 $/h ; juge 1,4 $ par 1 000 lectures ; 450 générations de 400 jetons sur un 8B en float32 prennent environ 1 h 30 sur 48 Go.
7. **La vérification extérieure** : qui, hors de l'auteur, pourrait établir que le résultat est vrai, et avec quoi (fichiers publics, recalcul, réplication sur une autre famille, lecture humaine).
8. **Le mentor** à qui il parle, avec la phrase citée de sa page.
9. **La nouveauté** : cherche sur arXiv et Semantic Scholar si c'est déjà fait ; donne la requête et le résultat, ou déclare « non cherché ».

Puis :

- **Classe** les idées par valeur pour une candidature de fellowship divisée par le coût, et dis en une ligne pourquoi la première est première.
- **Ce qui réfuterait la loi d'attraction** Δ = g(ĉ − p₀) : trois observations, chacune avec le fichier où on la verrait.
- **Ce que les données brutes contiennent et que personne n'a regardé** : les 1 200 textes sont publics. Que révèle leur contenu (longueur, refus, hedging, mentions de l'utilisateur, structure) que les notes 1–5 ne montrent pas ? Une analyse à zéro dépense sur ces textes compte comme un résultat.
- **Ce que tu n'as pas vérifié**, en liste.

## 3. Les contraintes

- Un seul chercheur, des agents IA comme collègues, un budget de quelques dizaines de dollars par expérience, des résultats attendus avant la fin de la semaine.
- Le modèle d'étude est Llama-3.1-8B-Instruct ; d'autres familles ont été testées (Qwen2.5-7B, Mistral-7B-v0.3, Gemma-2-9B).
- Le juge principal est `claude-opus-4-6` à température 0, avec un prompt fixé et non publié (SHA-256 `6c95c1c0…`) ; des juges à poids ouverts (Qwen2.5-7B, 72B) sont déjà validés.
- Toute expérience est préenregistrée, archivée sur Zenodo avant la première donnée, et recalculée par une instance neuve avant publication. Une idée qui ne se laisse pas préenregistrer avec deux issues n'entre pas.
- N'écris pas de code. Ne propose pas de fine-tuning. Ne cite aucun nombre que tu n'as pas lu dans un fichier.

## 4. Ce que tu feras ensuite, quand on te le demandera

Après ta réponse, on te donnera la liste des idées déjà trouvées par l'équipe. Tu la compareras à la tienne : ce qui se recouvre, ce que tu as trouvé qu'elle n'a pas, ce qu'elle a trouvé que tu n'as pas, et laquelle des deux listes tu suivrais.
