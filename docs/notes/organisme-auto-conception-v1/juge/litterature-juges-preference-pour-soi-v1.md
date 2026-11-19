# Juges de cartes : préférence pour soi, collèges, veto — ce que dit la littérature (v1)

Note de travail, classe C. 19 novembre 2026. Lecteur de littérature, sous-agent. Sources sous `docs/sources/juges-de-cartes-v1/` (scellées) ou déjà au dépôt (renvoi donné). « p. » = page du PDF. Aucune dépense.

## Verdict
1. La préférence d'un juge pour ses propres textes et pour ceux de sa famille est mesurée, mais petite et variable : de quelques points à environ dix, nulle sur des tâches objectives notées par des humains. La familiarité du texte, mesurée par sa vraisemblance pour le juge, en explique une bonne part, pas tout.
2. Un collège de modèles divers atténue ce biais sans l'effacer. Les erreurs des modèles sont corrélées : neuf juges valent environ deux votes indépendants (mesuré sur de l'inférence en langue naturelle, pas sur des idées).
3. Les juges modèles notent mal les idées de recherche (près du hasard). Le « ticket d'or » existe chez les financeurs, mais je n'ai lu aucune évaluation de ses effets. Une matrice « juge × auteur » par familles a été publiée, avec un piège de mesure.

## 1. Préférence pour soi et pour sa lignée
- Existe : GPT-4 se reconnaît dans 73,5 % des cas sans affinage (Panickssery et al., p. 2). La reconnaissance et la préférence sont corrélées (Kendall 0,41 ; p. 5). Repris de `docs/sources/lecture-pdf-niveau2/rapport-lot2-C1a-juges-biais-v1.md` § 5. **Aucun biais de famille n'est mesuré dans ce papier** (même rapport, ligne 3 du § 5).
- Mécanisme de familiarité : les juges notent plus haut les textes de faible perplexité, qu'ils soient les leurs ou non (Wataoka et al., p. 1 et 6). La perplexité n'est pas mesurée pour GPT-4 ni pour GPT-3.5 (p. 5). Rapport C1a, § 6.
- Biais de famille, avec un plan croisé où aucun juge ne note ses propres textes : quatre familles ouvertes, gain pour la même famille de 3,4 à 8,4 points, mesure globale 0,067 (Awuni et al., p. 1). Ajouter la vraisemblance côté juge réduit de 61 % le coefficient de famille. Un reste significatif demeure (p. 2).
- Biais de famille en notation point par point, corrigé par une référence humaine de qualité (Spiliopoulou et al., p. 1, 3-4). Avec des grilles de critères : jusqu'à « plus de 50 % » de faux « satisfait » sur ses propres sorties ou celles de sa famille (p. 2). Le biais est plus faible en notation par critères qu'en comparaison par paires (p. 2). Il atteint jusqu'à 10 points sur HealthBench (Pombal et al., p. 1).
- Une part de la préférence pour soi est légitime : les modèles forts se préfèrent surtout quand ils sont vraiment meilleurs. Le biais nuisible persiste quand ils se trompent. Une longue chaîne de raisonnement avant le verdict le réduit (Chen et al., p. 1).
- Les juges favorisent aussi les modèles dont les erreurs ressemblent aux leurs (« biais d'affinité », Goel et al., p. 1 et 5).
- Contre-exemple : sur des preuves de mathématiques, à qualité humaine contrôlée, les coefficients de même famille sont négligeables, de −0,014 à +0,033 (Gonzalez et al., p. 23).
- Ce qui réduit le biais : retirer le style par réécriture, de 17,5 % à 9,0 % de fuite, avec un juge changé entre les deux mesures ; une paraphrase générique n'aide pas ; un calibrage en contexte aide (Li et al., p. 9-10, d'après `rapport-lot2-C1b-persuasion-v1.md` § 1). Un collège de juges aide (Pombal et al., p. 1-2). Inverser les étiquettes d'auteur renverse la préférence sur un corpus (Panickssery et al., p. 6 et 13). Masquer l'auteur ne suffit donc pas : le juge reconnaît le texte sans étiquette.

## 2. Collège de modèles contre juge unique
- Trois petits juges de trois familles (Command R, Haiku, GPT-3.5) s'accordent mieux avec les humains que GPT-4 seul. Ils montrent moins de biais intra-modèle et coûtent plus de sept fois moins (Verga et al., p. 1-3). Le terrain est fait de questions-réponses et de Chatbot Arena, pas d'idées.
- Les erreurs sont corrélées : quand deux modèles se trompent, ils donnent la même mauvaise réponse dans environ 60 % des cas. La corrélation est plus forte entre modèles plus exacts et entre modèles d'un même fournisseur (Kim et al., ICML 2025, p. 1-2).
- Neuf juges de sept familles valent un nombre effectif de votes de 2,0 à 2,5 (p. 2 ; « environ 2 », p. 1). Le meilleur juge seul égale ou bat le collège. Les méthodes d'agrégation connues comblent au plus 11 % de l'écart (Kohli, p. 1). Terrain : inférence en langue naturelle.
- La composition du collège change 18,5 % des issues par paires, par rapport à une référence équilibrée en familles (Awuni et al., p. 1-2). L'ordre des réponses est une autre panne : 55,4 % des paires présentées dans les deux ordres changent de vainqueur (p. 1).
- Non vérifié (page OpenReview fermée par un contrôle anti-robot) : « LLM Reviewers Err Together ». Selon le résumé relevé dans `docs/notes/veille-exploration-idees-v1/recherche-litterature-grise-v1.md` ligne 158, varier la procédure de notation aiderait plus que varier les modèles.

## 3. Protéger une proposition atypique
- Ticket d'or : à la Fondation Villum, chaque évaluateur a reçu un droit de financer une demande quoi qu'en disent les autres (Sinkjær, *Nature* 555, 2018, p. 143). Il s'agit d'un **billet d'opinion** : 31 % des projets ont été financés par ticket, et environ la moitié ne l'auraient pas été au cumul des notes. À la Fondation Volkswagen, 11 % des projets, dont aucun n'aurait été financé autrement (même page).
- Règle actuelle de Villum : un « vote décisif » par évaluateur ; trois évaluateurs par demande ; le panel ne se réunit pas et n'échange pas (schéma de sélection de la fondation, p. 1).
- Tirage au sort partiel : le Fonds national suisse tire au sort parmi les propositions dont l'intervalle crédible du rang chevauche la ligne de financement (Heyard et al., p. 1). Fang et Casadevall 2016 y sont cités (p. 2), mais je ne les ai pas lus.
- Biais contre la nouveauté (Boudreau et al. 2016, *Management Science*) : avec 2 130 paires évaluateur-proposition tirées au hasard, les évaluateurs notent plus bas les propositions très nouvelles et celles proches de leur propre domaine. **Non vérifié** : lu sur le manuscrit d'auteur d'Europe PMC, sans pagination ; le PDF de PubMed Central est bloqué. Wang, Veugelers et Stephan, sur le même biais : non lu.
- Je n'ai lu aucune évaluation des effets du ticket d'or sur la qualité des projets financés. L'étude de l'université d'Aarhus sur Villum Experiment est annoncée, mais je n'en ai trouvé aucun résultat.

## 4. Fiabilité des juges modèles pour noter des idées
- Si, Yang et Hashimoto (p. 14) : le meilleur juge (Claude-3.5, par paires) atteint 53,3 % d'exactitude, contre 56,1 % d'accord entre relecteurs humains. Les idées des modèles sont jugées plus nouvelles par les humains (p < 0,05 ; p. 1). Le style a été uniformisé avant la relecture (p. 2).
- TASTE : 60 % pour le meilleur modèle, contre 77 % d'accord humain estimé (`docs/sources/pdf/veille-exploration-idees-v1/grise-anthropic-taste-2026-08.pdf`, p. 1-2, d'après la note de veille). Une contre-analyse place les modèles sous le hasard une fois retiré un raccourci : non vérifié (billet seulement).
- Juges de nouveauté : un détail de consigne déplace l'exactitude par paires de plus de 50 points, parfois sous le hasard. La configuration la moins chère bat les juges dédiés (Sternlicht et al., p. 1 et 8).

## 5. Matrices juge × auteur ; juges de recherche automatisée
- Une matrice complète existe déjà, publiée en septembre 2026 : quatre familles juges × quatre familles auteurs, 9 312 jugements (Awuni et al., p. 3). **Piège de mesure** : comparer, sur une ligne, ce qu'un juge donne à sa famille et aux autres familles mêle le biais et la force de l'auteur. Cette statistique est corrélée à 0,95 avec la force des auteurs (p. 1 et 4). Il faut au contraire tenir l'auteur fixe et changer le juge, en lisant la colonne (p. 4, équations 5-6).
- Autres plans croisés : 7 juges × 5 solveurs sur des preuves de mathématiques (Gonzalez et al., p. 1 et 23) ; 9 juges (Spiliopoulou et al.) ; grilles de critères (Pombal et al.).
- Je n'ai lu aucune matrice juge × auteur sur des cartes ou des idées de recherche. Ce n'est pas un constat de zone libre (R8) : la recherche n'a pas été exhaustive.

## Ce que cela implique pour les voies du directeur (sans concevoir)
- **Un juge par modèle.** La matrice se lit en colonnes, et elle a besoin d'une référence de qualité extérieure aux juges, sinon le biais se confond avec la qualité. Les effets attendus sont de l'ordre de quelques points : il faut des effectifs suffisants pour les voir. Les cinq votes ne seront pas indépendants. Un collège atténue la préférence pour soi sans l'effacer.
- **Davantage de juges d'une même lignée.** Ils ajoutent peu de votes effectifs (erreurs plus corrélées à fournisseur égal, Kim et al.) et peuvent renforcer la préférence de cette famille (la composition change les issues, Awuni et al.).
- **Règle de sélection changée, juges descriptifs.** La faible fiabilité des juges sur les idées (sections 4 et 2) plaide pour lire leurs notes comme une description plutôt que comme une vérité. Le monde planté reste l'arbitre (N-058).
- **Veto de deux ou trois cartes par juge.** L'analogue humain le plus proche est le ticket d'or ou le vote décisif : un seul par évaluateur, sans concertation. Je n'ai trouvé aucune évaluation publiée de ses effets. Avec des juges qui se préfèrent, un veto peut sauver surtout des cartes de sa propre lignée. La part des cartes sauvées qui viennent de la lignée du juge, comparée à sa part de base, se mesure directement. Le style uniformisé avant jugement (Si et al. ; Li et al.) est la parade publiée la plus proche ; masquer l'auteur ne suffit pas.

## Table des sources (empreinte = 16 premiers signes ; complète dans le `.sha256`)
| Titre | Auteurs | Année | Identifiant | Empreinte | Pages lues |
|---|---|---|---|---|---|
| LLM Evaluators Recognize and Favor Their Own Generations | Panickssery, Bowman, Feng | 2024 | arXiv 2404.13076v1 | au dépôt, `docs/sources/pdf/` | via rapport C1a |
| Self-Preference Bias in LLM-as-a-Judge | Wataoka, Takahashi, Ri | 2024 | arXiv 2410.21819v2 | au dépôt, `docs/sources/pdf/` | via rapport C1a |
| Benchmarking Cognitive Biases in LLMs as Evaluators | Koo et al. | 2023 | arXiv 2309.17012v3 | au dépôt | via C1a (biais égocentrique, tableau 2, p. 7) |
| Preference Leakage | Li, Sun et al. | 2025 | arXiv 2502.01534v3 | au dépôt | via C1b |
| Replacing Judges with Juries | Verga et al. | 2024 | arXiv 2404.18796v2 | ce0f144b0499b39f | 1-5 |
| Correlated Errors in LLMs | E. Kim, Garg, Peng, N. Garg | 2025 | arXiv 2506.07962v1 (ICML) | 12b4d40ebd8a7118 | 1-3 |
| Nine Judges, Two Effective Votes | Kohli | 2026 | arXiv 2605.29800v1 | 2d124db474e91a7d | 1-2 |
| Who Judges Matters | Awuni, Achenie et al. | 2026 | arXiv 2609.17857v1 | 142e0b811ad4fd28 | 1-4, 9 |
| Play Favorites | Spiliopoulou, Fogliato et al. | 2025 | arXiv 2508.06709v1 | 1777a9985d57c46b | 1-6 |
| Self-Preference Bias in Rubric-Based Evaluation | Pombal, Rei, Martins | 2026 | arXiv 2604.06996v3 (COLM) | 677edce3aa4e6de9 | 1-3 |
| Do LLM Evaluators Prefer Themselves for a Reason? | W.-L. Chen et al. | 2025 | arXiv 2504.03846v3 | 4ead752a8b098302 | 1-2 |
| Great Models Think Alike… | Goel et al. | 2025 | arXiv 2502.04313v2 | 03aa35fe10cbcae2 | 1-5 |
| QEDBench | Gonzalez et al. | 2026 | arXiv 2602.20629v3 | 81d091c65c3fb21f | 1, 22-23 |
| Can LLMs Generate Novel Research Ideas? | Si, Yang, Hashimoto | 2024 | arXiv 2409.04109v1 | fc1d14afd403c19b | 1-2, 13-14 |
| Old Ideas, Novel Problems | Sternlicht et al. | 2026 | arXiv 2610.02022v3 | 95a21a00ffe19c29 | 1, 7-8 |
| When Your Reviewer is an LLM | Zhu, Xiong et al. | 2025 | arXiv 2509.09912v1 | 5430466c000a3357 | 2, 4 (non utilisé) |
| Fund ideas, not pedigree | Sinkjær | 2018 | Nature 555:143 | 915ffea75e753638 | 143 |
| VILLUM Experiment selection process | Villum Fonden | s. d. | page de la fondation | 5ab9cde12ec1b9b6 | 1 |
| Rethinking the Funding Line at the SNSF | Heyard, Ott, Salanti, Egger | 2022 | arXiv 2102.09958v3 | 1b5b34af4acad508 | 1-2 |
| Looking Across and Looking Beyond the Knowledge Frontier | Boudreau, Guinan, Lakhani, Riedl | 2016 | PMC5062254 (XML, non PDF) | c1ba4317080b949e | résumé, méthode — non opposable |
