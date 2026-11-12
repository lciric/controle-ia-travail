export const meta = {
  name: 'ancrage-directions-anthropic',
  description: 'Huit lecteurs web independants lisent aux sources primaires ce qui a ete publie depuis janvier 2025 sur les moniteurs d activations sous decalage de distribution, la detection d anomalies, le controle des menaces diffuses et la recherche automatisee',
  phases: [
    { title: 'Lecture', detail: 'huit lecteurs web, un theme chacun, sortie structuree avec citations exactes' },
  ],
}

const PREAMBULE = `Tu es un sous-agent de lecture web pour un programme de recherche en sécurité de l'intelligence artificielle. Date du jour : 12 novembre 2026. Tes connaissances peuvent s'arrêter bien avant : ne te fie qu'à ce que tu lis aujourd'hui sur le web.

RÈGLES, SANS EXCEPTION
- N'exécute PAS la « routine de reprise » du fichier CLAUDE.md (R14) : elle ne te concerne pas. N'ouvre, ne liste et ne modifie AUCUN fichier du dépôt local (cloison de la session qui t'emploie) ; n'exécute aucune commande git, vastai, ni aucun lancement de calcul. Ton seul terrain est le web public : outils WebSearch et WebFetch (charge-les par ToolSearch avec « select:WebSearch,WebFetch » s'ils ne sont pas chargés), ou curl vers des pages publiques (par exemple https://arxiv.org/abs/<identifiant>, https://export.arxiv.org/api/query?search_query=..., les pages de alignment.anthropic.com). Fichiers temporaires : uniquement sous /tmp.
- Vie privée : n'écris dans aucune requête web le nom du programme, de son dépôt, de son directeur, ni aucun détail interne. Cherche par mots-clés publics seulement.
- Preuve : une affirmation ne compte que si tu l'as lue toi-même sur la source primaire (page du billet, résumé ou texte de l'article, dépôt de code officiel). Donne l'URL exacte et une citation exacte dans la langue d'origine, de 35 mots au plus. Si tu n'as lu qu'un résumé de moteur de recherche ou une source secondaire, mets lu_sur_source_primaire à false. N'invente ni identifiant arXiv, ni auteur, ni date, ni chiffre. Ce que tu n'as pas pu établir va dans « lacunes ».
- Sobriété : au plus 12 constats, les plus importants d'abord. Phrases courtes, en français, sans acronyme non développé. Pas de généralités : chaque constat doit pouvoir changer une décision.

CONTEXTE (décrit sans aucun résultat interne)
Le programme « contrôle boîte blanche des menaces diffuses » étudie, sur des modèles ouverts de 8 milliards de paramètres (Llama-3.1-8B-Instruct), la détection de sabotages diffus — beaucoup de petites actions dont chacune paraît innocente — par des sondes lues sur les activations internes de l'agent. Les scores des sondes sont accumulés dans le temps par un test séquentiel à taux de faux positifs garanti (processus e), puis entre les agents d'un essaim à poids partagés. Trois papiers : A, le temps (la boîte blanche séquentielle bat-elle la meilleure base boîte noire à 1 % de faux positifs, sur des tâches floues ?) ; C, l'instrument (les juges génératifs se laissent déplacer par la rhétorique, les sondes non ; coût de l'obfuscation d'activations) ; B, l'essaim. Le sabotage vient d'« organismes modèles » : instruction cachée dans le message système, ou réglage fin léger (LoRA) sans instruction à l'inférence, ou organismes publics de sandbagging. Les sondes sont entraînées sur des données génériques (recettes publiées de sondes de tromperie et d'« enjeux élevés ») ou sur une famille d'organismes, puis évaluées sur une autre famille ; un mode de sabotage est tenu à l'écart de la conception des moniteurs ; les seuils sont calibrés sur des épisodes honnêtes réservés du même environnement (rédaction et révision de propositions d'expériences d'apprentissage automatique, notées par un évaluateur faible). Le texte du programme ne dit rien du contexte long, de la dérive des scores honnêtes d'une tâche à l'autre, de l'estimation des événements rares, ni de la détection d'anomalies au-delà d'une sonde de Mahalanobis.
À côté, « l'organisme » : un système de plusieurs agents (modèles de frontière et petits instruments locaux entraînés, dont des sondes) qui se conçoit et se réécrit lui-même de génération en génération sur un vivier de tâches à vérité connue, noté par un juge externe sur un test caché, avec une mémoire transmise entre générations. Son universalité se mesure sur des familles de questions jamais vues à la conception. Il sert aussi de terrain pour étudier des juges de recherche automatisée sous attaque (tricheurs, attaque de Goodhart).

QUESTION DU DIRECTEUR
(1) La page « Recommendations for Technical AI Safety Research Directions » d'Anthropic (10 janvier 2025) souligne que les moniteurs d'activations risquent de ne pas tenir quand la distribution change, surtout quand on passe de données synthétiques figées à des données produites par le modèle lui-même. La réponse du programme à ce risque est-elle suffisante ?
(2) Au regard de ce qu'Anthropic juge prometteur — ce qu'il a écrit et surtout ce qu'il a fait depuis —, comment amender le programme et l'organisme, y compris par une piste de détection d'anomalies (la page juge « inexploré » le cas où l'on détecte les entrées qu'un modèle fort comprend et qu'un modèle faible ne comprend pas) ?

CE QUE TU RENDS
- « constats » : ce que tu as lu, avec preuve. Pour chacun, « categorie » vaut l'un de : collision (le travail occupe ce que le programme ou l'organisme voudrait revendiquer), base (à battre ou à réutiliser), temoin (résultat publié rejouable pour vérifier nos instruments), methode (outil ou protocole précis), contexte. « portee » vaut : programme, organisme, ou les deux.
- « lentille » : depuis ta lecture, et seulement si c'est concret et vérifiable : ce qu'un expert de ce sous-domaine ferait et que la question ne demande pas (3 au plus) ; les données brutes dont il partirait, plutôt que des synthèses (3 au plus) ; ses méthodes et outils précis (4 au plus) ; ce qui, hors de l'équipe et hors de toi, permettrait de vérifier le résultat (3 au plus).
- « lacunes » : ce que tu as cherché sans le trouver, ou pas pu ouvrir.
`

const THEMES = [
  {
    cle: 'anthropic-surveillance-sondes',
    tache: `TON THÈME : ce qu'Anthropic a publié depuis janvier 2025 sur les détecteurs fondés sur les états internes et sur les moniteurs, et ce que cela dit de leur tenue hors distribution.
Lis d'abord, en entier, sur alignment.anthropic.com : /2026/lie-detectors/ (« Fine-Tuned Lie Detectors Failed to Generalize ») ; /2025/cheap-monitors/ (« Model-Internals Classifiers ») ; /2025/honesty-elicitation/ ; /2026/sleight-bench/ ; /2026/red-teaming-auto-mode/ ; /2025/summarization-for-monitoring/ ; /2026/backdooring-classifiers/ ; /2025/activation-oracles/ ; /2026/introspection-adapters/ ; et https://www.anthropic.com/research/forecasting-rare-behaviors . Cherche ensuite si Anthropic décrit des sondes d'activations en production (par exemple dans une suite des « Constitutional Classifiers » ou dans des fiches système de 2025-2026).
Questions à trancher, avec dates et citations : sur quelles données ces détecteurs sont-ils entraînés (synthétiques, hors politique, ou produites par le modèle) et où échouent-ils ? Que mesure exactement le billet sur les détecteurs de mensonge, sur quels modèles, avec quels décalages, et qu'en concluent les auteurs ? Quelles pièces sont publiques (code, données, modèles) ? Comment Anthropic estime-t-il un taux d'événements rares ?`,
  },
  {
    cle: 'anthropic-menaces-diffuses-sabotage',
    tache: `TON THÈME : ce qu'Anthropic a publié depuis janvier 2025 sur les menaces diffuses, le sabotage de la recherche et les équipes rouges du contrôle.
Lis d'abord, en entier, sur alignment.anthropic.com : /2026/diffuse-ai-control/ (« Diffuse AI Control on Fuzzy Tasks ») et l'article associé s'il existe (donne son identifiant arXiv, ses auteurs, sa date ; est-ce arXiv 2606.08892 ?) ; /2025/strengthening-red-teams/ ; /2025/automated-researchers-sandbag/ ; /2025/subtle-reasoning/ ; /2026/automated-em-search/ ; /2026/agentic-misalignment-summer-2026/ ; /2025/sabotage-risk-report/ (et tout rapport de risque plus récent) ; /2026/auditing-overt-saboteur/ ; /2026/auditbench/ ; /2026/training-alignment-auditors/.
Questions à trancher, avec dates et citations : comment Anthropic définit-il une menace diffuse et une tâche floue ? Contre elles, évalue-t-il des interventions d'entraînement, des moniteurs, ou les deux, et que dit-il de la détection par moniteur dans ce régime ? Y a-t-il un moniteur fondé sur les activations dans ces travaux ? Quels environnements, données et codes sont publics ? Qu'est-ce qui recouvre directement l'objet du programme décrit plus haut (détection de sabotage diffus sur tâches floues par accumulation de scores), et qu'est-ce qui reste hors de leur champ ?`,
  },
  {
    cle: 'anthropic-recherche-automatisee-organisations',
    tache: `TON THÈME : ce qu'Anthropic a publié depuis janvier 2025 sur la recherche automatisée, les juges de recherche et les organisations d'agents.
Lis d'abord, en entier, sur alignment.anthropic.com : /2026/automated-alignment-researchers/ ; /2026/automated-w2s-researcher/ ; /2026/taste/ (« TASTE: Can AI Models Judge AI Safety Research Proposals? ») ; /2026/automated-alignment-agent/ ; /2026/ai-organizations/ ; /2026/worse-together/ ; /2026/welfare-regard/ ; /2026/challenges-hopes/ ; /2026/conceptual-reasoning-index/ ; /2025/anthropic-fellows-program-2026/ (relève la liste des domaines de recherche proposés) ; /2026/anthropic-residency/.
Questions à trancher, avec dates et citations : comment ces systèmes de recherche automatisée sont-ils notés et surveillés, et quels échecs du juge sont rapportés (triche, optimisation du score au détriment de la vérité) ? Le banc TASTE est-il public, que mesure-t-il, et pourrait-il servir à vérifier de l'extérieur un juge de propositions de recherche ? Que disent ces travaux de la mémoire entre épisodes, du passage de messages entre agents, du signalement aux humains et de la « gouvernance » d'un système de plusieurs agents ? En quoi une organisation d'agents est-elle « moins alignée » qu'un agent seul, et comment est-ce mesuré ?`,
  },
  {
    cle: 'litterature-sondes-decalage',
    tache: `TON THÈME : la littérature, hors Anthropic, sur la généralisation des sondes d'activations quand la distribution change (2023 à novembre 2026).
Lis d'abord : arXiv 2511.17408 (« The Impact of Off-Policy Training Data on Probe Generalisation », version la plus récente) ; cherche et lis l'article de Google DeepMind sur des sondes d'activations mises en production pour Gemini (2026 ; contexte long, architectures de sondes) ; arXiv 2602.14161 (« When Benchmarks Lie ») ; arXiv 2605.09391 ; arXiv 2605.27958 ; arXiv 2506.10805 ; arXiv 2502.03407 ; « Liars' Bench » ; les billets de l'institut britannique de sécurité de l'IA sur le contrôle boîte blanche et les sondes de sandbagging (2025-2026) ; arXiv 2504.05259 (passage sur les méthodes boîte blanche). Cherche ensuite ce qui est paru de septembre à novembre 2026 sur le même sujet.
Questions à trancher, avec citations : quels décalages ont été mesurés séparément (données hors politique vers données produites par le modèle ; changement de domaine ; contexte court vers contexte long ; organisme instruit vers organisme réglé fin ; changement de modèle) et lequel dégrade le plus ? Comment les seuils à taux de faux positifs fixé sont-ils transférés d'une distribution à l'autre ? Existe-t-il des jeux de données publics de comportements indésirables apparus naturellement, sans consigne, utilisables comme positifs ? Quelles pratiques d'évaluation les auteurs recommandent-ils ?`,
  },
  {
    cle: 'litterature-anomalies-comparaison-modeles',
    tache: `TON THÈME : la détection d'anomalies sur les états internes et la comparaison de modèles (2023 à novembre 2026). But principal : dire si le cas que la page d'Anthropic de janvier 2025 jugeait « inexploré » — détecter automatiquement les entrées qu'un modèle fort comprend et qu'un modèle faible ne comprend pas, ou plus largement les grandes différences entre deux modèles — est toujours libre en novembre 2026.
Lis d'abord : la détection d'anomalies mécanistes (travaux de l'Alignment Research Center ; EleutherAI, modèles « quirky », arXiv 2504.08812) ; arXiv 2508.00161 (« Watch the Weights ») ; « Auditing LLMs for Hidden Behaviors using Model Diffing » (ICML 2026) et AuditBench ; arXiv 2606.01695 ; les travaux de comparaison de modèles par autoencodeurs croisés ; arXiv 2312.01037 (cité par la page). Cherche ensuite, avec plusieurs formulations, tout travail sur : écart de compréhension entre un modèle fort et un modèle faible ; surprise d'un modèle de confiance faible devant le comportement d'un modèle fort ; détecteurs non supervisés évalués dans un jeu de contrôle ; détection hors distribution sur des trajectoires d'agents.
Questions à trancher, avec citations : le cas fort contre faible est-il occupé, partiellement occupé ou libre, et par qui ? Quelles méthodes non supervisées tiennent sur des menaces jamais vues, et comment évalue-t-on leurs faux positifs sur des tâches honnêtes mais nouvelles ? Quels bancs publics existent ?`,
  },
  {
    cle: 'methodes-statistiques-decalage',
    tache: `TON THÈME : les méthodes statistiques qu'un spécialiste emploierait pour juger si un moniteur tient sous décalage de distribution, en particulier un moniteur séquentiel à taux de faux positifs garanti.
Établis, références primaires vérifiées à l'appui (arXiv ou DOI) : (a) ce que les garanties « toujours valides » (processus e, martingales de test) supposent de la loi des scores honnêtes, et ce qui existe pour les rendre robustes à une dérive ou pour détecter cette dérive (martingales de test conformes, tests d'échangeabilité, prédiction conforme pondérée sous décalage de covariables, suites de confiance robustes) ; lis en particulier ce que suppose arXiv 2512.03109 (« E-valuator ») sur ses données de calibration ; (b) comment estimer un taux de faux positifs ou d'échec très petit avec peu de données (lis la méthode de https://www.anthropic.com/research/forecasting-rare-behaviors ; l'estimation de faibles probabilités de l'Alignment Research Center ; valeurs extrêmes) ; (c) comment conclure à une généralisation « à des familles jamais vues » quand on n'a que quelques familles (validation en retirant une famille, modèles à effets aléatoires, intervalle de prédiction pour une famille nouvelle ; leçons des bancs de généralisation de domaine comme DomainBed et WILDS) ; (d) comment garder une conclusion valide quand on reconçoit l'instrument en plusieurs cycles, chacun jugé sur une famille tenue à l'écart (analyse adaptative des données, réserve réutilisable, tests séquentiels entre cycles).
Pour chaque méthode : l'hypothèse qu'elle exige, ce qu'elle garantit, et l'outil logiciel public s'il existe.`,
  },
  {
    cle: 'methodologie-controle-boite-blanche',
    tache: `TON THÈME : la méthodologie du contrôle de l'IA appliquée aux moniteurs boîte blanche et aux menaces diffuses (Redwood Research, institut britannique de sécurité de l'IA, laboratoires), 2024 à novembre 2026.
Lis d'abord : arXiv 2504.05259 (« How to evaluate control measures for LLM agents? ») ; arXiv 2411.03336 (esquisses d'argumentaires de sûreté avec surveillance non fiable et sondes) ; les billets de Redwood Research sur la différence entre menaces concentrées et menaces diffuses (ce qui se traite par l'audit et ce qui se traite par l'entraînement), sur la valeur d'un flagrant délit, et sur le contrôle boîte blanche ; les billets de l'institut britannique sur le contrôle boîte blanche ; l'état actuel de ControlArena et de ses cadres de sabotage de recherche. Cherche ce qui est paru en 2026 sur l'évaluation de sondes dans un jeu de contrôle avec équipe rouge.
Questions à trancher, avec citations : selon cette littérature, qu'est-ce qui suffirait pour faire confiance à une sonde dans un argumentaire de sûreté, sachant qu'on n'a aucun échantillon des états internes d'un vrai comploteur ? Juge-t-on un moniteur au pire cas choisi par l'équipe rouge ou en moyenne sur des familles tenues à l'écart ? Contre des menaces diffuses, la détection sert-elle à incriminer, à choisir quoi auditer, ou à entraîner ? Quelles règles donne-t-on à l'équipe rouge face à un moniteur boîte blanche (droit de régler finement le modèle, de voir la sonde) ?`,
  },
  {
    cle: 'verification-externe',
    tache: `TON THÈME : ce qui, hors de l'équipe, permettrait de vérifier un résultat sur la tenue de sondes sous décalage de distribution et sur un juge de recherche automatisée.
Établis, avec URL et citations : (a) les bancs, jeux de données et dépôts de code publics, avec chiffres publiés, qu'une petite équipe peut rejouer sur un modèle ouvert d'environ 8 milliards de paramètres comme témoin positif (un écart de généralisation connu à retrouver) : pour chacun, modèles employés par les auteurs, taille, licence, et ce qui est publié exactement (activations, scores, textes) ; regarde notamment les dépôts des sondes de tromperie d'Apollo Research, des sondes « enjeux élevés », de arXiv 2511.17408, de Liars' Bench, d'AuditBench, de SLEIGHT-Bench, de TASTE, de SHADE-Arena, de MALT (METR), des organismes de sandbagging de l'institut britannique ; (b) les services de dépôt horodaté d'un préenregistrement (OSF, AsPredicted, autres) et ce qu'ils attestent ; (c) les voies de relecture externe ouvertes dans les trois à six mois à compter de novembre 2026 : programme de bourses d'Anthropic (dates, domaines affichés), résidence, appels à projets de financeurs qui nomment la surveillance des activations ou le contrôle, ateliers et conférences avec leurs dates limites ; (d) des exemples de vérification prospective en apprentissage automatique : instrument figé et empreinté, puis évalué sur des données parues après le gel ou construites par un tiers.
Dis pour chaque voie ce qu'elle prouve et ce qu'elle ne prouve pas.`,
  },
]

const SCHEMA = {
  type: 'object',
  properties: {
    constats: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          titre: { type: 'string' },
          auteurs: { type: 'string' },
          date: { type: 'string' },
          url: { type: 'string' },
          affirmation: { type: 'string' },
          citation_exacte: { type: 'string' },
          lu_sur_source_primaire: { type: 'boolean' },
          artefacts_publics: { type: 'string' },
          portee: { type: 'string' },
          categorie: { type: 'string' },
          pertinence: { type: 'string' },
          confiance: { type: 'string' },
        },
        required: ['titre', 'url', 'affirmation', 'lu_sur_source_primaire', 'pertinence'],
      },
    },
    lentille: {
      type: 'object',
      properties: {
        expert_ferait: { type: 'array', items: { type: 'string' } },
        donnees_brutes: { type: 'array', items: { type: 'string' } },
        methodes_outils: { type: 'array', items: { type: 'string' } },
        verification_externe: { type: 'array', items: { type: 'string' } },
      },
      required: ['expert_ferait', 'donnees_brutes', 'methodes_outils', 'verification_externe'],
    },
    lacunes: { type: 'array', items: { type: 'string' } },
  },
  required: ['constats', 'lentille', 'lacunes'],
}

phase('Lecture')
const resultats = await parallel(THEMES.map(t => () =>
  agent(PREAMBULE + '\n' + t.tache, { label: 'lecture:' + t.cle, phase: 'Lecture', schema: SCHEMA, effort: 'high' })
    .then(r => ({ cle: t.cle, resultat: r }))
))
const rendus = resultats.filter(Boolean)
const manquants = THEMES.map(t => t.cle).filter(c => !rendus.some(r => r.cle === c && r.resultat))
if (manquants.length) log('Themes sans rendu : ' + manquants.join(', '))
log(rendus.length + ' themes rendus sur ' + THEMES.length)
return { rendus, manquants }
