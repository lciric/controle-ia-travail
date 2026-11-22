# Huit prépublications sur l'originalité des idées produites par des modèles (août à novembre 2026) — lecture sur PDF

Fichiers dans `/tmp/claude-0/-home-user-controle-ia-travail/7225ef84-cf06-5367-97a0-6c2a4e600e2b/scratchpad/sources/recent-idees/`. Dates de dépôt vérifiées sur les pages arxiv.org/abs. Les pages données sont celles du fichier PDF (égales aux numéros imprimés, sauf mention). Statut de tout ce qui suit : « lu sur PDF, p. N », sauf mention contraire.

| Fichier | sha256 |
|---|---|
| 2611.12184.pdf | d0643e1c74648486d14d3b42f78a000cee7445dfd7966fcee9b4fe08514bdd1d |
| 2609.33936.pdf | ee607c2533055c4f51adcf688377b29a27bf30aef427b99cf4946f936730d37d |
| 2608.19437.pdf | 451f9e68d530e4eaff9e3ab42d21fbc065db377faac33fcce9513669f89d866b |
| 2610.36511.pdf | 5af0af20c9f7104ef574c9531c470fe635274a233e8296ab7c5c649977e83a85 |
| 2609.35706.pdf | 7474df187ab80493efcd16f1ff7b8199ba54b8b34bd4a989591e6c3f8d5a36c9 |
| 2608.03233.pdf | 2d8f5b89ab31aee789f271b436d9f533ec5d46d1875a81f06c7091bfb68bbe7a |
| 2611.15835.pdf | a0951584b2342896f0de5fc1f8498358de780cdb1e5dbc20818ac8cf4190f6b5 |
| 2607.22375.pdf | ee61f63cfa0a67f716a144d4df1d40ceca9ee54e0b35d3796f58bbd639aad8ca |

---

## 1. Xu, Zou, Erdogan, Ye, Lu, Zou (Stanford), « Blind Variation, Selective Retention: Improving Creative Idea Generation in AI Scientists », arXiv 2611.12184, déposé le 9 novembre 2026 (v1), https://arxiv.org/pdf/2611.12184

- **Ce qui est retiré.** Claude Opus 5 résume l'énoncé complet S de la tâche en quatre contextes I plus ou moins informatifs. La quantité d'information se mesure en bits (« V-usable information ») : écart de log-vraisemblance de S avec et sans I, moyenné sur trois petits modèles (Qwen3-8B, Gemma-3-4B, Llama-3.1-8B) (p. 3, p. 24, p. 26). Exemple pour la tâche des gènes à variation spatiale, à 11,2 bits : « the samples sit on a 2-D lattice, and the goal is to rank features by how much of their variation is organized across the lattice rather than noise » (p. 33). Le domaine de la tâche, le jeu de données, la mesure et la référence sont donc masqués **au seul stade de l'idée**. L'implémentation, elle, reçoit l'énoncé complet (p. 3). Le gabarit d'idée demande en plus « ONE real paper from the field {field} » (p. 32) : il impose un champ scientifique, donc une composante de recherche dans un autre domaine (ce point est mon constat, il n'est pas commenté par les auteurs).
- **Les cinq proposeurs** : DeepSeek-V4-Flash, DeepSeek-V4-Pro, GLM-5.3 Flash, GLM-5.2, Kimi-K3, tous avec raisonnement et recherche OpenAlex (p. 4).
- **Les douze tâches** (p. 4, tableau 3 p. 25) :
  - biologie unicellulaire : communication cellulaire, projection d'étiquettes, prédiction de perturbation, gènes à variation spatiale ;
  - trajectoires Cassini et Voyager 2 ;
  - détection d'anomalies et calibration (MLS-Bench) ;
  - deux tâches de lois d'échelle (SLD-Bench) ;
  - prévision d'activité neuronale ZAPBench à 16 et 32 pas.
- **Qui juge.**
  - Originalité = rareté au sein du lot : 1 − log|g(c)|/log n, où les groupes g d'idées équivalentes sont formés **par un modèle**, GPT-5.6-Sol. Les auteurs le disent : « originality refers specifically to generative rarity … rather than novelty relative to the scientific literature » (p. 3, p. 25).
  - Utilité = **programme exécuté** par l'évaluateur du banc, normalisée par la meilleure amélioration observée (p. 3).
  - Non-évidence = **modèle** GPT-5.6-Luna, qui note v entre 0 et 1 (p. 3, p. 26).
  - Validation humaine (cinq chercheurs de niveau doctorat) :
    - groupement : 84 % des paires réunies par le modèle sont jugées équivalentes (IC [0,74 ; 0,92]) ; 73 % des paires séparées sont jugées distinctes (IC [0,61 ; 0,82]) ;
    - non-évidence : corrélation r = 0,56 avec le score automatique ; sur des propositions qui battent toutes la référence, la limitation d'information obtient 3,64 contre 2,97 pour le raisonnement par analogie (écart 0,67, IC [0,33 ; 0,99], p = 0,0006) (p. 9-10). Les résumés montrés aux experts sont réécrits par Claude Opus 5 (p. 33).
- **Chiffres, tableau 1 (p. 5).** 112 propositions par tâche et par modèle ; « All methods share the same proposer models, candidate budget, and reasoning configuration » : **budget égal en nombre de candidats**.

  | Méthode | Créativité | Utilité | Originalité | Non-évidence |
  |---|---|---|---|---|
  | Information limitée | 0,530 ± 0,043 | 0,571 ± 0,041 | 0,955 | 0,713 |
  | Même invite, énoncé complet | 0,462 | 0,524 | 0,926 | 0,609 |
  | Analogie | 0,429 | 0,508 | 0,914 | 0,492 |
  | Recherche dans d'autres domaines | 0,369 | 0,531 | 0,871 | 0,263 |
  | Sans consigne de domaine | 0,117 | 0,530 | 0,598 | 0,104 |

  La créativité et l'utilité de ce tableau sont celles du premier centile. L'écart d'utilité entre la limitation d'information et l'analogie (0,571 contre 0,508) est d'environ une erreur type. La figure 2 (p. 5) montre la baisse avec le nombre de bits, sans valeurs lisibles dans le texte.
- **Le tri appris.**
  - Modèle Qwen3.5-9B-Base entièrement affiné avec une tête de score. La perte est par paires et oppose les 5 % les plus utiles au reste (p. 7, p. 26).
  - Entraînement sur 40 733 propositions **déjà exécutées, sur les mêmes tâches** ; test sur 5 783 (p. 7).
  - En écartant 50 % des candidats, il garde 79 % des 5 % meilleurs en créativité et 82 % des 5 % meilleurs en utilité (p. 7). Il fait mieux que quatre juges sans exemples, que l'apprentissage en contexte (pas meilleur que les juges sans exemples) et qu'une régression affinée (figure 3, p. 7).
- **Effet sur des résultats exécutés** : la méthode est insérée dans SimpleTES avec Kimi-K3, quatre trajectoires, 40 propositions par itération, 10 itérations (p. 8).
  - Score final plus haut sur les cinq tâches (figure 4), atteint avec moins de vérifications.
  - Meilleurs programmes (tableau 2, p. 8) : gènes spatiaux 0,918 contre 0,906 pour SimpleTES et 0,853 pour SPARK-X ; anomalies 0,679 contre 0,629 et 0,491 (Isolation Forest) ; lois d'échelle R² 0,967 contre 0,940.
  - L'ablation (p. 9) porte sur deux tâches seulement.
- **Ce que l'article ne montre pas.**
  - Aucune section des limites (vérifié par recherche du mot).
  - Aucune répétition de graine signalée pour les courses SimpleTES ; un écart de 0,012 sur une seule course n'est pas éprouvé.
  - Le coût des 40 733 exécutions qui nourrissent le tri n'entre pas dans le budget comparé.
  - L'originalité n'est pas mesurée contre la littérature.
  - La non-évidence est jugée par un modèle, l'expertise humaine ne donnant qu'une corrélation modérée.
  - Le gain du tri est mesuré sur la distribution d'entraînement (mêmes tâches) : aucune tâche inédite.

## 2. Schaeffer, Miranda, Kazdan, Chudnovsky, Koyejo (Stanford), « How Strong Is the Evidence for the Artificial Hivemind? … », arXiv 2609.33936, déposé le 27 septembre 2026, https://arxiv.org/pdf/2609.33936

- **Objet** : réexamen de Jiang et al. 2025 (« Artificial Hivemind »). Trois résultats sont visés (p. 1).
- **(1) L'exemple phare (« Write a metaphor involving time », deux groupes).**
  - Nouvelle collecte de 9 000 réponses : 15 modèles de Google, Anthropic et OpenAI, 12 sujets fixés d'avance (p. 4).
  - La projection en deux dimensions ne capte que 25 à 41 % de la variance (p. 4).
  - Un mélange de von Mises-Fisher choisit 22 à 41 groupes, jamais deux (p. 5-6). Sur les données originales (43 modèles, 2 150 réponses), il en choisit K = 42 et 44 (p. 6).
  - Étiquettes du « véhicule » posées **par un modèle** (Claude Fable 5) : « river » 80,5 %, nombre effectif 6,23 ; 1,86 sur les réponses à une seule métaphore (p. 7). Sur les données originales : « river » 90,2 %, la famille « weaver » 3,3 % (p. 8).
  - « Time » est classé 1er sur 12 sujets du côté le moins divers (p. 8).
- **(2) Le nul trop facile** : des réponses à des invites différentes (cosinus médian d'environ 0,11 ; le seuil de 0,8 en est au 99,95e centile) (p. 9).
  - Nul plus exigeant : des réponses à la même invite qui expriment des idées réellement différentes. Médiane 0,723 par groupement géométrique sur 50 invites, 0,703 par étiquettes d'un modèle sur 15 invites (tableau 2, p. 9).
  - Au-dessus de 0,8, on trouve 20 % des paires (étiquettes) et 32 % (groupement). Au-dessus de 0,7, 54 % et 61 % (p. 10).
  - **Effet résiduel** : les paires de même invite de l'article original dépassent 0,8 « roughly two to three times as often », soit un rapport de 1,9 (groupement) et 3,1 (étiquettes) (p. 10). Le chiffre comparé est celui de l'original sous échantillonnage min-p (61,2 % au-dessus de 0,8).
  - Les statistiques restantes n'ont aucun nul. Le compte de modèles distincts (environ 8 sur 50) se situe entre 1 et environ 21,9 (p. 11).
- **(3) Le remède par l'entraînement** : inférence jugée sans appui (p. 12).
  - Cinq reformulations de l'invite fixées d'avance dépassent la référence dans 79,6 à 91,7 % des 108 cases. Le rapport de participation passe de 13,8 à 44,8 (p. 13).
  - Mais le nombre effectif d'idées ne bouge pas significativement (3,34 contre 3,99 ; p de signe ≥ 0,39) et la part non classable monte de 0,20 à 0,39-0,45 (p. 14).
- **Conclusion des auteurs** : « We do not resolve whether the Artificial Hivemind is real. We show that the published evidence does not establish it » (p. 1).
- **Limites dites** (p. 15) : réplication conceptuelle, avec un écart d'époque des modèles ; pas de nul humain (le pilote humain a été écarté, soupçon de réponses générées, p. 10) ; une diversité d'enchâssement n'est pas une créativité ; la qualité sous reformulation n'est pas mesurée.
- **Ce qu'il ne montre pas** : que les modèles sont divers. Le texte : « We do not claim model responses are diverse » (p. 8). Une concentration réelle subsiste, avec 80 à 90 % de « river ».

## 3. Patel, Crossman, Aggarwal, Wenger (Duke), « Are LLMs becoming similarly creative? Evidence from three years of models », arXiv 2608.19437, déposé le 19 août 2026, https://arxiv.org/pdf/2608.19437

- **Mesure** : distance cosinus (enchâssement all-MiniLM-L6-v2) entre réponses de modèles de fournisseurs différents à la même invite.
  - Jeux : la tâche des usages alternatifs, avec 10 objets, chaque liste enchâssée d'un bloc ; et 100 invites Infinity-Chat.
  - Une seule réponse par modèle et par invite, température 1 (p. 4).
  - Régression des moindres carrés sur 9 tranches de dates de sortie ; 1 000 rééchantillonnages, un modèle par famille (p. 4).
- **Modèles** : 68, sortis de mars 2023 à juillet 2026, 12 fournisseurs (p. 3-4).
- **Tendance** (tableau 1, p. 6) :

  | Jeu | Pente par tranche | IC 95 % | Évolution |
  |---|---|---|---|
  | Usages alternatifs | −0,01385 | [−0,01695 ; −0,01044] | d'environ 0,50 à moins de 0,40 |
  | Infinity-Chat | −0,00167 | [−0,00267 ; −0,00074] | d'environ 0,34 à un peu plus de 0,32 |

  Pentes négatives dans les 1 000 rééchantillonnages (p. 5).
- **Limites dites** : « preliminary » (résumé, p. 1) ; distillation et données partagées non contrôlées ; une seule réponse par modèle (« only a point estimate ») ; rôle de l'utilisateur ignoré ; robustesse au libellé, à l'échantillonnage et à la longueur « would also help rule out confounders » (p. 6).
- **Ce qu'il ne montre pas** :
  - aucun nul de type Schaeffer (idées différentes à la même invite) ;
  - aucun contrôle de longueur ni de style ;
  - aucune mesure du contenu des idées ;
  - les paires partagent des modèles, sans correction de dépendance (mon constat) ;
  - l'association avec la date n'est pas causale, ce que les auteurs disent eux-mêmes (p. 4).

## 4. Liu, Zhao, Xie, Zhai (Illinois), « Do AI Scientists Know What's New? », arXiv 2610.36511, déposé le 27 octobre 2026, https://arxiv.org/pdf/2610.36511

- **Cadre à vérité temporelle** : date de coupure T = mars 2026 ; tous les juges sont antérieurs à T (Sonnet 4.6) (p. 5). Quatre jeux, 1 060 propositions :
  - **déjà faites** : 100 papiers vedettes d'ICML 2026, déguisés à 4 degrés, 380 retenus ; pool de 20 papiers ; au plus 2 % de 6-grammes communs ;
  - **contestées par des relecteurs** : 160 revues ICLR 2022-23 ;
  - **réalisées ensuite par des humains** : 400 idées tirées de 3 000 générées par Sonnet 4.6 à partir de 30 papiers de NeurIPS 2025, étiquetées **par un modèle** (Opus 4.6) contre les papiers citants postérieurs à T ;
  - **hybrides** : 100 (p. 5-6).
- **Contrôles existants** (tableau 1, p. 7, juge Sonnet 4.6) :

  | Contrôle | Déguisements rejetés (sur 380) | Fausses alertes sur les idées réalisées ensuite |
  |---|---|---|
  | Si et al. | 380 | 96,0 % |
  | AI Scientist v1 | 380 | 51,8 % |
  | AI-Scientist-v2 | 362 | 39,2 % |
  | ResearchAgent | 338 | 98,5 % |
  | CoI-Agent | 368 | 3,8 % |
  | ARC | 85 | 0 % |
  | ScholarEval | 0 | 0 % |

  Conclusion de l'article : « checks with high rejection rates on non-novel work also tend to have high false alarms » (p. 1).
- **Module proposé (ClaimNov)** : il découpe la proposition en affirmations typées, retrouve les affirmations proches (embeddings), juge l'implication avec gpt-4o-mini, puis rend le verdict avec Sonnet 4.6 (p. 3-4).
  - 367 déguisements sur 380 rejetés, la source nommée 366 fois ; 1,5 % de fausses alertes ; J = +0,95 (p. 7).
  - Sans le profil par affirmation, les fausses alertes montent de 1,5 % à 11,8 % (p. 7).
  - Rejette 3 % des propositions acceptées à ICLR (p. 7-8).
  - Garde 91 hybrides sur 100, contre 76 pour CoI-Agent (p. 8).
  - CoI-Agent est « statistically level » avec ClaimNov sur le tableau 1, une fois les tests groupés par source (p. 6).
- **Limites dites** (p. 9) :
  - les idées réalisées ensuite sont étiquetées par un modèle ;
  - les déguisements et les idées viennent du même modèle que le juge (Sonnet 4.6), « a known source of possible bias » ;
  - pools fermés de 20 papiers ;
  - IA seulement ;
  - la vérité temporelle se périme.
- **Contre-indice à retenir** : l'audit humain de 45 idées « réalisées ensuite » n'en confirme que **28 comme nouvelles** par rapport au pool (annexe F.1, p. 20). Les « fausses alertes » des concurrents comptent donc en partie des rejets justifiés. Les règles de verdict ont été calibrées sur des items pilotes (tableau 38, p. 26).

## 5. Kargupta, Cucerzan, Mahajan, Herring, Han, White, Jauhar (Illinois, Microsoft), « Reinforcing Agentic Creativity in Scientific Ideation with Night Science », arXiv 2609.35706, déposé le 28 septembre 2026, https://arxiv.org/pdf/2609.35706

- **Référence à la « science de nuit »** : Yanai et Lercher, Genome Biology 2019, et Stent 1988 (p. 2, p. 13). **François Jacob n'est pas cité** (recherche du nom : aucune occurrence). La référence Stent 1988 s'intitule « The statue within: An autobiography », Science 239, mais le nom de Jacob n'y figure pas.
- **Ce qui est entraîné.**
  - Qwen3-8B-Base et Qwen3-14B-Base, par GRPO (p. 6), avec cinq actions : chercher, débattre, « étincelle » (renverser une hypothèse), écrire, arrêter. Chaque action a des niveaux de créativité décrits en langage naturel (tableau 1, p. 5).
  - La récompense est la moyenne de précédence, faisabilité et pertinence, notées **par un modèle** (GPT-4.1 dans la chaîne de récompense, p. 5-6).
  - Données : 4 414 titres de bourses NSF pour l'entraînement, 491 pour le test ; seul le titre est donné (p. 6).
- **Qui juge**, et ce sont des modèles :
  - « impact de citation prédit » : SciJudge, **un modèle de 30 milliards de paramètres** qui prédit l'impact relatif (82,7 % d'exactitude annoncée) ;
  - originalité : **GPT-5.1** en comparaison par paires ;
  - diversité : catégories posées par **GPT-5.4-mini** (p. 7).
  - Les références comparées sont des propositions **reconstruites par GPT-5.1** à partir des résultats des bourses (p. 6). Le juge d'originalité est donc le même modèle que l'auteur de la référence.
- **Gains** (tableau 3, p. 8 ; intervalles p. 14) :

  | Comparaison | Taux de victoire (citations) | Taux de victoire (originalité) |
  |---|---|---|
  | Modèle entraîné 8B contre la référence | 29,89 % [25,77 ; 34,35] | 56,32 % |
  | Qwen3-8B sans exemple contre la référence | 0,46 % | 2,53 % |
  | Modèle entraîné 14B contre la référence | 33,18 % | 68,68 % |

  - Étendue des paradigmes : de 0,738 à 0,943, soit +27,8 %. Types de contribution : de 0,370 à 0,425, soit +14,9 %.
  - Contre la même chaîne avec la seule température, en apprentissage par renforcement : +36,50 points d'originalité (p. 8).
- **Validation hors modèle** : deux annotateurs sur 33 comparaisons, 15 en commun.
  - Accord humain-modèle : 76,7 % (46/60) pour l'impact, 72,4 % « (43/60) » pour l'originalité. Or 43/60 vaut 71,7 % : incohérence interne (p. 25).
  - Aucune mesure de citations réelles ni d'exécution.
- **Ce qu'il ne montre pas** :
  - un gain jugé hors des modèles d'OpenAI ;
  - l'absence d'exploitation de la récompense (la précédence récompensée ressemble à l'originalité évaluée) ;
  - une originalité vérifiée.
  - Aucune section des limites dans le corps. Les baselines « sans exemple » partent de presque zéro.

## 6. Shen, de Sousa, Barcelos, Guo, Zhu (Queen's University, Institut fédéral de Goiás, Conseil national de recherches du Canada), « On the Diversity of Analogy Making in Large Language Models », arXiv 2608.03233, déposé le 4 août 2026, https://arxiv.org/pdf/2608.03233

- **Dispositif** : 10 modèles. Cinq fermés : GPT-5.2, Grok-4.5, Gemini 2.5 Pro, Gemini 3.1 Pro, Claude 4.6 Sonnet. Cinq ouverts, d'environ 8 milliards de paramètres, limités à 100 jetons de sortie. Trois jeux : AnaloBench, Metaphoric Analogies, MUNCH (1 000 extraits). K = 10 générations par item (p. 3-4).
- **Mesure de l'homogénéité des domaines.**
  - Distance cosinus moyenne (MiniLM).
  - Groupement des domaines cibles par **un modèle** (GPT-4o-mini) ; accord humain de 95 % sur 10 % des données (p. 5).
  - Qualité jugée par GPT-4o-mini (p. 4).
- **Chiffres.**
  - Diversité intra-sortie au mieux 0,49 (Gemini 3.1 Pro, invite de diversité) ; au plus 0,63 sur les seuls domaines (p. 4).
  - Environ **deux groupes de domaines pour 10 analogies demandées « distinctes »** : 3,5 pour Grok-4.5, moins de 2 pour Qwen3-8B (p. 5).
  - Score MAUVE entre modèles de 0,72 (Grok contre Gemini 3.1) (p. 5).
- **Compromis.**
  - Mistral-7B : invite de base, qualité 4,32, diversité 0,33, 1,97 groupes ; top-k, qualité 4,21, diversité 0,53, 2,27 groupes (p. 6).
  - Phi-4-mini : qualité 4,28 en base, 3,80 avec top-nσ, la méthode la plus diverse (p. 7).
  - « No outstanding method » ; classements instables selon le modèle (p. 6).
- **Ce qu'il ne montre pas** :
  - aucune base humaine ;
  - qualité jugée par un seul petit modèle ;
  - sortie tronquée à 100 jetons pour les modèles ouverts ;
  - pas d'idéation scientifique proprement dite ;
  - l'explication par les couches reste « potential » (p. 8) ;
  - aucune section des limites.

## 7. Li, Hays, Ramdas, Raghavan (MIT, Stanford selon l'en-tête), « Controlling the Probability of Unknown Unknowns in Pre-Deployment Testing of AI Systems », arXiv 2611.15835, déposé le 11 novembre 2026, https://arxiv.org/pdf/2611.15835

- **Grandeur bornée.** R_t = P(fail(A_{t+1})·unseen(A_{t+1}, H_t) = 1 | F_t), la probabilité que la prochaine sortie montre un mode de défaillance jamais vu ; but : P(R_T < ε) ≥ 1 − α au temps d'arrêt T (p. 6).
- **Lien avec Good et Turing, explicite** : « a sequential variant of the missing-mass estimation problem which gave rise to the classic Good-Turing estimator (Good, 1953) » (p. 1). La généralisation : la nouveauté peut dépendre de l'historique, et n'est donc pas une taxonomie fixe (p. 5, note 1).
- **Suite et règle d'arrêt.**
  - Processus de pari : mélange de « départs retardés » E_{s:t}, pondérés en (i+1)⁻¹ log(i+1)⁻², et mélange uniforme sur λ ∈ [0,1].
  - Borne supérieure U_t(α) obtenue par inversion ; arrêt dès que U_t(α) < ε (algorithme 1, p. 8).
  - Théorème 3.2 : couverture simultanée ≥ 1 − α (p. 9). Théorème 3.3 : arrêt presque sûr, délai en O(log) après la descente sous γ < ε (p. 10). Théorème 3.4 : bornes inférieures montrant ce délai optimal à une constante près (p. 10-11).
- **Hypothèses.**
  - Entrées **tirées indépendamment d'une loi P fixe** (p. 4-5).
  - Espace des sorties dénombrable (p. 7).
  - Monotonie de la fonction « unseen » (p. 5).
  - Extensions : (a) loi d'échantillonnage différente de P, mais **rapport des propensions connu et borné** (p. 12-13) ; (b) étiqueteur imparfait, par un modèle, corrigé par des audits sur vérité terrain, chaque vraie défaillance gardant une probabilité d'audit minorée (p. 13).
- **Résultats** (SWE-Chat, 5 001 sessions) :
  - défaillances posées **par un modèle** (GPT-5.6 Sol), 538 catégories par groupement (p. 14-15) ;
  - masse manquante vraie d'environ 0,15 au départ, sous 0,1 vers 3 000 tirages ;
  - borne plus serrée que les deux bornes de Good et Turing ; couverture empirique de 0,973 (p. 15-16) ;
  - sur une loi synthétique défavorable, couverture de 0,9587 (p. 16) ;
  - à ε = 0,1, la voie par inférence assistée de prédictions demande 896 étiquettes vraies contre 3 045, au prix de 8 943 sessions (p. 14).
- **Limites dites** : tout dépend des définitions de « fail » et « unseen » ; insensible au coût d'une défaillance rare et grave (p. 16) ; en tension avec la validité de terrain (p. 15).
- **Ce qu'il ne montre pas** : rien sur un système qui s'adapte au test ou sur un adversaire. La garantie suppose un système et une loi fixes. Les tirages sont faits avec remise dans un ensemble fini, donc indépendants par construction.

## 8. Gumma, Majumder, Sinhahajari, Poria (Nanyang Technological University), « IDEAgent: Agentic Quality-Diversity Search for Research Idea Generation », arXiv 2607.22375, v1 du 24 juillet 2026, v2 du 20 octobre 2026 (hors de la fenêtre « août à novembre » pour la v1), https://arxiv.org/pdf/2607.22375

- **Procédé d'archive** : quatre stocks (p. 4).
  - Les acceptées (capacité 10).
  - Une file de réparation.
  - Les historiques, c'est-à-dire les parents remplacés.
  - La mémoire des rejets, en résumés.
  - Chaque graine est jugée sur la non-évidence, la clarté, la faisabilité et la solidité (5 tirages), puis comparée à l'archive. Elle est réparée une fois si elle échoue de peu, ou raffinée ; l'enfant ne remplace son parent que s'il ne perd pas en non-évidence.
  - Pas de grille MAP-Elites (p. 3).
- **Juges.**
  - Internes : gemini-3.1-pro et gemini-3.5-flash. Proposeur : gpt-5.6-sol.
  - Externes : claude-sonnet-5 et claude-opus-4.7, moyennés (p. 7). Leur accord en kappa est de 0,27 à 0,60 (tableau 3, p. 9).
  - Humains : **deux auteurs**, à l'aveugle, 25 paires (p. 15).
- **Référence et budget** : même nombre de graines (B = 10) pour toutes les méthodes (p. 7), mais pas le même nombre d'appels.
  - Coût par sujet réussi : 22,00 $ contre 35,52 $ et 130,56 $ selon le seuil (p. 17).
  - Avec une ligne sans mémoire portée à 50 générations, la méthode garde un « Yield » 2,06 et 2,46 fois plus haut (p. 17).
- **Chiffres** (tableau 1, p. 8).
  - « Yield » au seuil 7 : 1,094 contre 0,281 pour la ligne inspirée de NOVA, soit le facteur 3,89.
  - Au moins 2 idées qualifiées sur 8 sujets sur 32, contre 1 sur 32.
  - Humains : préférée dans 69,6 % des paires (p < 0,05), aucune rubrique significative seule (p. 15, 17).
  - Algorithmes exécutés : meilleur score 106,2 contre 93,5 sur AlphaResearch et 56,4 contre 45,1 sur ALE-Bench ; mais la diversité y reste jugée par un modèle (tableau 4, p. 11).
- **Limites dites** : juges modèles ; hyperparamètres non optimisés ; informatique et intelligence artificielle seulement ; « not to claim SoTA » (p. 14-15).

---

## Tableau de synthèse

| Article | Originalité jugée par | Validation hors modèle | Budget égal | Résultat principal |
|---|---|---|---|---|
| Variation aveugle (2611.12184) | modèle (rareté intra-lot ; non-évidence GPT) | utilité exécutée ; 5 experts | oui en candidats ; le tri coûte 40 733 exécutions non comptées | moins d'information → plus d'originalité et de non-évidence ; gain exécuté faible, sans répétition |
| Réexamen du « Hivemind » (2609.33936) | enchâssements + étiquettes Claude | aucune base humaine | sans objet | 20-32 % de paires d'idées différentes déjà au-dessus de 0,8 ; effet résiduel ×1,9-3,1 |
| Tendance sur trois ans (2608.19437) | enchâssements MiniLM | aucune | sans objet | pente négative, faible sur Infinity-Chat ; préliminaire |
| Contrôles de nouveauté (2610.36511) | modèles (Sonnet, gpt-4o-mini) | audit humain partiel : 28/45 seulement confirmées | oui (même juge) | compromis rejet/fausses alertes ; ClaimNov 97 % / 1,5 % |
| Science de nuit (2609.35706) | GPT-5.1, SciJudge, GPT-5.4-mini | 2 annotateurs, 33 paires | non précisé | +27,8 % d'étendue, jugée uniquement par des modèles |
| Analogies (2608.03233) | GPT-4o-mini, MiniLM | 10 % des groupes par des humains | sans objet | environ 2 domaines sur 10 analogies ; diversité contre qualité |
| Inconnus inconnus (2611.15835) | sans objet (statistique démontrée) | théorèmes + simulation | sans objet | borne valide à tout instant, tirages indépendants d'une loi fixe |
| IDEAgent (2607.22375) | Gemini en interne, Claude en externe | 2 auteurs, 25 paires ; algorithmes exécutés | même nombre de graines, pas d'appels | « Yield » ×3,89 face à la ligne inspirée de NOVA |

## Lecture d'ensemble (six lignes)

(a) Ce qui fait monter l'originalité **vérifiée**. Seul l'article sur la variation aveugle relie une manipulation (masquer la tâche au stade de l'idée) à des scores exécutés. L'originalité y reste une rareté jugée par un modèle, et le gain exécuté n'est pas répété. Les gains de la science de nuit et d'IDEAgent sont jugés par des modèles, avec des contrôles humains minces.

(b) La convergence existe sous forme de concentration : 80 à 90 % de « river », environ deux domaines d'analogie sur dix. Mais les seuils de cosinus en exagèrent l'ampleur (Schaeffer), la tendance temporelle reste préliminaire, et aucune étude n'a de base humaine appariée.

(c) La reconnaissance de la nouveauté : les contrôles existants échangent rejet contre fausses alertes. ClaimNov fait mieux sur une vérité fabriquée et jugée par le même modèle, dont l'audit humain ne confirme que 62 % des « nouvelles ». L'article de Li et al. donne une borne valide de nouveauté des défaillances, mais seulement pour des tirages indépendants d'une loi fixe.

## Non vérifié

- Valeurs chiffrées de la figure 2 de 2611.12184 (pourcentages de baisse de 0 à 140 bits) : illisibles dans le texte extrait.
- Annexes de 2611.15835 au-delà de la p. 19 et figure 3 (temps d'arrêt contre l'oracle) : non lues en détail.
- Annexes de 2609.33936 au-delà de la p. 16 : non lues.
- Tableaux 13 et 23 de 2610.36511 : seulement survolés.
- Affiliations de 2611.15835 : l'en-tête attribue « 1 MIT » et « 2 Stanford ». Ramdas est habituellement à Carnegie Mellon (de mémoire, à vérifier) ; l'en-tête du PDF est rapporté tel quel.
- Lien entre Stent 1988 et François Jacob : de mémoire, à vérifier ; le PDF ne nomme pas Jacob.
