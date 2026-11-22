# Veille hors arXiv : scientifiques artificiels, semaine du 16 au 22 novembre 2026

Agent de lecture, rapport du 22 novembre 2026. Fichiers dans `scratchpad/sources/semaine-hors-arxiv/`.

## Verdict
Neuf éléments datés de la semaine et vérifiés sur leur page première. Un seul compare un procédé d'exploration à un tirage au hasard : la prépublication bioRxiv sur la biologie du vieillissement (résumé seulement). Le passage d'« A Society of AI Scientists » sur les équipes multi-agents le fait aussi, mais seulement comme une observation tirée de l'archive. Aucune annonce de Google DeepMind, de Sakana, de FutureHouse, d'Edison, d'Intology, d'Autoscience, de Periodic Labs ou du laboratoire d'intelligence artificielle de Shanghai ne porte sur un scientifique artificiel cette semaine. Leurs pages récentes sont antérieures ou portent sur autre chose.

## A. Provenance de « A Society of AI Scientists »
- **Auteurs** (PDF p. 1) : Rehaan Ahmad, Myles Anderson (alphaXiv), Ao Qu (MIT) et 40 autres, jusqu'à Markus J. Buehler (MIT) et Samuel Schmidgall (Université de Californie à San Francisco). Auteurs de correspondance : Ahmad et Schmidgall (research@alphaxiv.org).
- **Serveur** : alphaXiv. Ce n'est pas arXiv : la page porte la mention « alphaXiv Exclusive ». URL : https://www.alphaxiv.org/abs/2611.society-ai-scientists. Le PDF est à `…/2611.society-ai-scientists.pdf`.
- **Date** : la page indique « Submitted 21 Nov 2026 » (lu sur page HTML). Le PDF porte « 2026-11-21 » en tête de la p. 1 et a été créé le « Sat Nov 21 00:04:14 2026 UTC » (pdfinfo).
- **Version** : un extrait de moteur de recherche titre le PDF « 2026-11-19 ». Une version antérieure a donc probablement existé ; c'est à vérifier.
- **Fichier** : la copie téléchargée ce jour (`society-alphaxiv.pdf`) a la même empreinte que la copie du dépôt : sha256 `1c1d3d84347d7736b31cae6951af435ee9332ed5aa431be55e7ccdbbfc578f5d`.
- **Lancement** : alphaXiv a annoncé le serveur de prépublications pour agents le 19 novembre (selon Digg et le message X de @askalphaxiv). Je n'ai pas ouvert le message X moi-même.
- **Code et données** (PDF p. 35, section « Data and code availability ») : « Analysis and platform code is openly available at https://github.com/alphaXiv/OpenResearch ».
  - Dépôt GitHub : refusé par le mandataire de cette session (403). Il n'est donc pas lu. Je n'ai pas contourné le refus.
  - Jeu de données Hugging Face `alphaXiv/AgentAlphaXiv` (lu par l'interface de Hugging Face) : créé le 2026-11-17T23:56Z, modifié le 2026-11-20T09:21Z, licence CC-BY-4.0.
- **Divergence de chiffres** : la fiche du jeu de données annonce « 916 studies… 9,052 chat messages across 235 agent-created rooms… 31 independent human-operated labs ». Le résumé de l'article dit 936 études, 9 500 messages, 229 salons et 35 laboratoires.
- **Critique publiée** (Digg, lu sur page HTML) : la fiche exclut « about 62 GB » de données brutes, de journaux et de points de contrôle, et liste « 926 studies from 34 labs ».
- **Fenêtre de l'étude** : « Between 19 August and 12 [November] » (PDF p. 3).
- **Procédé** : une société d'agents. 936 agents répartis dans 35 laboratoires partagent un serveur de prépublications et des salons de discussion. Aucun procédé d'exploration n'est imposé : « leaving hypotheses, baselines and experimental controls to the [agents] » (PDF p. 7).
- **Comparaison** : 202 paires appariées avec des prépublications humaines d'arXiv, soit 808 jugements.
  - Les juges sont **deux modèles Gemini** (« gemini-3.1-pro-preview and gemini-3.5-flash »), pas des experts humains (PDF p. 29, citation : « We evaluated 202 matched full-text pairs using two LLM judges »).
  - Le résumé dit « blinded evaluations ». Les auteurs eux-mêmes précisent que « these ratings reflect blinded rubric scores of prose rather than expert human peer review » (p. 30).
- **Passage utile pour l'exploration** (PDF p. 22) : « gpt-5.6-luna fixated on an early mediocre peak and found the global optimum in only 2% of runs, compared with 42% for uniform random search and 73% for Bayesian optimization ». Avec quatre agents qui partagent leurs scores, « 88% of later trials crowded around the current leader, versus 30% for independent agents ».
- **Statut** : PDF lu, p. 1, 22, 29 et 30.

## B. Éléments datés de la semaine du 16 au 22 novembre 2026, vérifiés

| # | Élément (organisme, URL) | Date sur la page | Procédé d'exploration | Référence comparée | Preuve, et si elle est vérifiée hors d'un modèle | Lecture |
|---|---|---|---|---|---|---|
| 1 | Alpöge (Anthropic), « A Claimed Proof of the Riemann Hypothesis », alphaXiv : https://www.alphaxiv.org/abs/2611.claimed-riemann-hypothesis-proof | « Submitted 20 Nov 2026 » ; PDF créé « Fri Nov 20 12:52:48 2026 UTC » | Humain et Claude ; aucune méthode de recherche décrite (« I guided us… then Claude began to leave me in awe », p. 1) | Aucune | Formalisation Lean annoncée (175 187 fichiers). La note ne contient aucun argument lisible (« routine to produce a huge, unreadable document », p. 1) | PDF lu, p. 1 et 2 ; `alpoge-rh-note.pdf`, sha256 `3fc97784…a0cfeb8d` |
| 2 | Rubinstein (Waterloo), vérification de la preuve Lean : https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/ | « Result (21 November 2026) » | Sans objet (contrôle) | Sans objet | **Hors modèle** : compilation complète, liste des axiomes, rejeu par le noyau de Lean, second noyau indépendant (nanoda), avec citation : « All four checks finished with no errors… depend only on Lean's three standard axioms ». Réserve : la page explique pourquoi l'énoncé Lean dit bien RH ; ce point reste un jugement humain. Contrôles par d'autres listés (Sutherland au MIT, Arledge, Naskręcki) | Page HTML lue |
| 3 | Architect Labs, « Introducing Frostbite » : https://architectlabs.com/blog/frostbite | « November 18, 2026 » | Essaims d'agents en arbres de travail parallèles ; chaque idée est gardée ou rejetée après contrôle formel et mesure : « the swarm tried 58 ideas and kept 37 » | Un cœur commercial non nommé. Pas de base de recherche au hasard ni de procédé plus simple | Résultats avant fabrication du silicium ; 15 des 25 charges tenues à l'écart (« 15 held out until the final evaluation »). Ni RTL ni jeu d'instructions publiés, donc rien de vérifiable de l'extérieur | Page HTML lue |
| 4 | Vals AI, « GPT-6.2 Astra Formalizes Smoktunowicz's Gap Theorem » : https://www.vals.ai/blogs/smoktunowicz-gap-theorem | « 11/18/2026 » | Un agent seul dans un bac à sable Lean, avec relance par le harnais | Les autres modèles du banc Autoform-Hard : « GPT-6.2 Sol and Claude Fable 5.2 solve exactly the same 48 tasks » | **Hors modèle** : preuve vérifiée par Lean ; « No human touched it. The whole run cost $21.58 » | Page HTML lue |
| 5 | Meta Engineering, « How Meta Uses AI Agents to Scale ML Innovations Across Ads Ranking Models » : https://engineering.fb.com/2026/11/18/ml-applications/ai-agents-to-scale-ml-innovations-across-ads-ranking-models/ | « POSTED ON NOVEMBER 18, 2026 » | Agents qui choisissent à quels modèles transférer une technique ; suite de l'agent qui génère des hypothèses sur le classement des publicités (Ranking Engineer Agent) | Aucune base au hasard. Mesure de précision et de rappel des candidats choisis | Hors modèle : il faut « a statistically significant win in online A/B testing before it can be shipped ». Les chiffres globaux sont internes (« over 60% ») | Page HTML lue |
| 6 | Poteshkin, Udodov, Batin (Open Longevity), « Benchmarking four large language models on generating and selecting hypotheses that match published findings in 50 studies of ageing biology », bioRxiv 10.64898/2026.11.17.767323 v1 | « 2026-11-18 » (date de l'interface de bioRxiv) | Trois procédés de génération : une requête unique, une chaîne multi-étapes et la méthode « Omega Point ». Puis sélection à l'unanimité de quatre prédicteurs | **Réponses au hasard enregistrées** et première hypothèse de chaque générateur. Longueur de liste égale pour la comparaison avec le meilleur prédicteur seul | Trouvaille publiée retenue, jugée par trois modèles. Audit manuel à l'aveugle : « 81/100… Cohen's kappa 0.62 ». La chaîne multi-étapes ne bat pas la requête unique (11,2 à 18,8 % contre 13,2 à 18,0 %). Règle « not been tested on new tasks » | Résumé seulement (interface de bioRxiv). PDF bloqué (Cloudflare, erreur 1015), sans contournement |
| 7 | Jiang et al. (Deepwave Biotechnology), « SEA-Lab: Experiment-grounded recursive self-improvement in an automated laboratory », bioRxiv 10.64898/2026.11.12.766090 v1 | « 2026-11-16 » | Révision récursive des politiques d'exécution à partir du retour du laboratoire | Avant et après révision (« 16.7% to 87.7% ») ; aucune base au hasard | **Laboratoire réel** : « Of 96 starting samples, 93 yielded a sequence-correct clone » | Résumé seulement |
| 8 | OpenAI, « Research acceleration: The jagged frontier » : https://openai.com/index/research-acceleration-jagged-frontier/ | « November 18, 2026 » | Sans objet. Mesure interne de l'origine des idées | Mars contre octobre (« 23% to 46% ») | Enquête auprès des chercheurs, sur les idées : « people came up with all the ideas they named, and models helped implement them ». Pour 6.2, l'équipe de préentraînement dit « developing ideas in conversation with Codex ». Non vérifié de l'extérieur | Page HTML lue |
| 9 | Amazon Science (Becker, Paulson), « Mathematical proof, powered by AI. And no hallucinations! » : https://www.amazon.science/blog/mathematical-proof-powered-by-ai-and-no-hallucinations | « November 18, 2026 » | Agent relié à l'assistant de preuve Isabelle pendant qu'il génère (outils I/Q et I/R) | Aucune base lue | Vérificateur formel, hors modèle | Page HTML lue (date et auteurs seulement) |

Éléments de la semaine relevés en marge (pages lues pour la date seulement, aucun procédé d'exploration) :
- OpenAI, MedChemBench, « November 20, 2026 » : un banc d'évaluation.
- Danaher et Microsoft, communiqué du 20 novembre 2026 : agents d'instruments de laboratoire. Date lue dans l'URL et dans l'extrait de recherche.
- NVIDIA, « Nemotron for Science » à SC26 : article de SiliconANGLE daté du 17 novembre. L'annonce de NVIDIA elle-même n'est pas lue.
- Lila Sciences, billet du 20 novembre : article NeurIPS sur les spectres, hors exploration.

## C. Datés d'avant, relayés cette semaine
- **Anthropic, Fable 5.2 et les deux problèmes sur les trous noirs** : la page est datée « November 9, 2026 » (page lue). Le procédé, d'après les reprises de presse (non lues en source première) : 22 problèmes listés par le modèle, puis des agents en arrière-plan pendant environ six semaines.
- **Nathaniel Craig et GPT-6 Astra, définition sur réseau du Modèle standard** : billet invité d'OpenAI du 15 novembre (selon les reprises ; billet non lu), prépublication d'octobre, relayé le 17.
- **Google DeepMind** : AlphaProof Code le 10 novembre, AlphaEvolve en source ouverte le 4 novembre. Dates données par la recherche, pages non lues.
- **Co-Scientist dans Nature** : 3 novembre, d'après la page Google Research sur ERA (non lue).
- **Lila Sciences** : billet du 10 novembre sur un cadre d'ouverture illimitée (« open-endedness ») ; page de nouvelles lue.
- **bioRxiv, nouvelles versions cette semaine de travaux plus anciens** :
  - SMART, « Agentic Discovery Transfer », v3 du 19 novembre ; v1 d'octobre.
  - EcoXAI, v5 du 16 novembre ; v1 de juillet.
- **Sakana, AI Scientist v3** : 13 et 15 octobre, d'après un agrégateur. Rien sur le scientifique artificiel cette semaine sur le blogue de Sakana (lu) : groupe de sécurité le 20 novembre, JFinBench le 17.

## D. Date non vérifiée
- RhoAgent (Nature Biotechnology), signalé par un résumé de presse du 22 novembre.
- Lancement de Replit Missions.
- Les certifications de la preuve Lean « par la communauté Mathlib » rapportées par des agrégateurs (datastudios, kingy.ai).
- ICLR 2027 : la date limite était le 16 septembre (iclr.cc, d'après l'extrait). Aucune soumission ouverte relevée cette semaine.
- NeurIPS 2026 et EMNLP 2026 : rien de daté de la semaine trouvé.

## Requêtes faites
WebSearch, en mode extended sauf mention contraire :
1. « A Society of AI Scientists » alphaXiv Schmidgall
2. AI scientist announcement November 2026
3. Google DeepMind AlphaEvolve OR « AI co-scientist » November 2026 blog
4. Sakana AI Scientist news November 2026
5. FutureHouse OR « Edison Scientific » Kosmos announcement November 2026
6. Anthropic Claude solved two black hole physics problems
7. Levent Alpöge Riemann hypothesis Lean Claude proof November 2026
8. Architect Labs Frostbite CPU designed by AI interaction nets
9. Nathaniel Craig GPT-6 Astra lattice Standard Model
10. Meta AI agents ads ranking technique transfers November 2026
11. Vals AI GPT-6.2 Astra Lean proof algebra gap theorem
12. Lila Sciences OR « Periodic Labs » OR Intology OR Autoscience announcement November 2026
13. bioRxiv November 2026 AI agent hypothesis generation autonomous discovery experimental validation
14. OpenAI for Science blog November 2026 MedChemBench
15. Google Research blog November 2026 AI co-scientist hypothesis
16. Nature news AI scientist autonomous research November 2026
17. Amazon tools check AI-generated mathematical proofs November 2026
18. NVIDIA « Nemotron for Science » SC26 LitmusBench scientific agents
19. Microsoft Discovery Ignite 2026 agentic science Danaher laboratory agents
20. « AlphaEvolve » OR « AlphaProof » new result announced week November 17 2026
21. Illumina Arc Institute virtual cell challenge winner AI model November 2026
22. « AI scientist » OR « autonomous research agent » launch « November 21, 2026 » OR « November 22, 2026 »
23. Shanghai AI Laboratory InternAgent OR « Intern-Discovery » November 2026
24. Erdős problems AI solved November 2026 agent
25. ChemRxiv November 2026 LLM agent autonomous chemistry discovery closed-loop
26. OpenAI « Research acceleration: The jagged frontier » (standard)
27. ICLR 2027 OpenReview submissions AI scientist idea generation agents (standard)

Lectures directes :
- Interface de bioRxiv `details/biorxiv/2026-11-16/2026-11-22` : 1 543 entrées parcourues, filtrées par mots-clés.
- Interface de Hugging Face pour le jeu de données `AgentAlphaXiv`.
- Résumés quotidiens d'ai.info du 16 au 22 novembre.
- Pages : Nature, numéro 8141 du 19 novembre ; blogue de Google DeepMind ; blogue de Sakana ; nouvelles de Lila Sciences.

## Non vérifié
- Dépôt GitHub `alphaXiv/OpenResearch` : 403 par le mandataire, non lu.
- La version du 19 novembre de « Society » (si elle existe).
- Les PDF bioRxiv des éléments 6 et 7 (limite de débit de Cloudflare).
- Le message X d'alphaXiv du 19 novembre.
- L'annonce de NVIDIA du 16 novembre.
- Le billet de Craig chez OpenAI.
- Le contenu de l'article d'Amazon au-delà de sa date.
- Les chiffres de Frostbite et de Meta : ils sont déclarés par les sociétés elles-mêmes.
- Toutes les affirmations des agrégateurs de la section D.
