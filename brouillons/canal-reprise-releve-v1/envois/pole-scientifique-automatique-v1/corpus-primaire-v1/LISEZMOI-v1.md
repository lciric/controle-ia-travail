# LISEZMOI — corpus primaire v1

Date : 28 octobre 2026. Produit par l'instance de contrôle des conversations (sous-agent), sur décision de Lazar du 28 octobre 2026, 22 h 47 (heure de Paris).

## 1. Ce que c'est

Des extraits de texte, scellés, des papiers des occupants, à servir aux proposeurs et aux juges de la course d'idéation en plus des rapports d'antériorité. Un extrait garde, dans l'ordre : le titre, les auteurs, l'année, l'identifiant, l'empreinte du PDF, le résumé, l'introduction, la méthode, les limites ou la conclusion, avec le numéro de page du PDF en `[p.N]` au début de chaque passage. Les bibliographies, annexes et figures illisibles sont coupées. Chaque extrait fait au plus 25 000 caractères.

Un extrait n'est pas une vérification : tout chiffre repris dans un préenregistrement ou un papier doit citer la page `[p.N]` et être relu sur le PDF empreinté (règle R7). Les notes de coupe et de retrait, entre crochets, sont de la main de l'instance, pas du papier.

## 2. Choix des dix papiers

Critère : occupants principaux les plus cités par les onze rapports (sept questions, question-pont, classement motivé v2, rapport de co-évolution, rapport d'universalité), puis les alertes ; PDF présent dans `docs/sources/pdf/` et empreinte vérifiée par `sha256sum -c` (les dix : OK, lancé le 28 octobre 2026). Les occupants les plus cités n'ont pas de PDF (SafeCoEvo 6 rapports, Storf 5, AgentSafeEvo 4, EvoDefense 4) : ils sont dans `manquants-v1.md`.

## 3. Papiers choisis (présents, extraits)

| Identifiant (version du PDF) | Titre (tel qu'écrit dans le PDF) | Auteurs | Année | Rapports qui le citent (par identifiant / par identifiant ou nom) | Rôle | Pages gardées | Caractères |
|---|---|---|---|---|---|---|---|
| arXiv:2610.12445v1 | Caught in the Act: Probes Effectively Detect Sabotage and Catch Unverbalized Deception | Hollinsworth, Spies, Diriba, Gleave, Cundy | 2026 | 5 / 5 | Occupant principal des sondes boîte blanche (Q6, Q7, Qpont) ; alerte « Telling FIBS » tranchée : le titre du PDF est « Caught in the Act », FIBS est le nom du jeu de données. | 1-10 | 24892 |
| arXiv:2606.08892v2 | Diffuse AI Control on Fuzzy Tasks | Terekhov, Gulcehre, Hebbar, Benton | 2026 | 3 / 3 | Occupant principal des menaces diffuses (Q4) : défense optimisée par équipe rouge ; l'argument « la surveillance est moins prometteuse » est cité, non démontré. | 1-9 | 24667 |
| arXiv:2607.02514v2 | Distributed Attacks in Persistent-State AI Control | Hills, Caspary, Cooper Stickland | 2026 | 3 / 3 | Occupant principal Q3 et Q4 : attaques graduelles, moniteur à état. | 1-10 | 24941 |
| arXiv:2607.07368v1 | Multi-Agent AI Control: Distributed Attacks Hamper Per-Instance Monitors (cité par les rapports sous le nom de Makins et al. ; premier auteur du PDF : Angelini) | Angelini, Makins, Shams, Phuong | 2026 | 3 / 3 | Occupant principal Q4 : attaques réparties sur un, trois ou neuf agents ; part inexpliquée d'environ 40 %. | 1-6, 8, 10-14 | 24742 |
| arXiv:2605.09684v1 | MonitoringBench: Semi-Automated Red-Teaming for Agent Monitoring | Jotautaitė, Martinez, Matthews, Tracy | 2026 | 3 / 5 | Occupant principal de la co-évolution et des moniteurs figés (Q1, Q6) ; trois axes de taxonomie. | 1-9 | 24551 |
| arXiv:2602.14161v2 | When Benchmarks Lie: Evaluating Malicious Prompt Classifiers Under True Distribution Shift | Fomin | 2026 | 3 / 3 | Q6 et universalité des métriques : évaluation en laissant un jeu de données de côté, écart de 8,0 à 16,5 points avec la validation croisée. | 1-11 | 24567 |
| arXiv:2605.16626v2 | SLEIGHT-Bench: A Benchmark of Evasion Attacks Against Agent Monitors | Najt, Toft, Tracy, Roger, Benton | 2026 | 2 / 2 | Alerte 2 (Q3) : onze classes d'angles morts des moniteurs ; le titre du PDF diffère de celui du billet cité par les rapports. | 1-4, 6-10 | 24333 |
| arXiv:2412.09565v2 | Obfuscated Activations Bypass LLM Latent-Space Defenses | Bailey, Serrano, Sheshadri, et al. | 2025 | 2 / 2 | Q7 : attaques d'obfuscation contre les sondes, entraînement adversarial de la défense sur plus de 70 époques. | 1-7, 11-13, 28-30 | 24098 |
| arXiv:2601.20022v2 | Quickest Change Detection in Discrete-Time in Presence of a Covert Adversary | Ramtin, Nain, Towsley | 2026 | 2 / 2 | Q4 : ancrage formel du « lemme du plafond d'horizon » ; théorie hors langage naturel. | 1-12 | 23840 |
| arXiv:2510.09462v2 | Adaptive Attacks on Trusted Monitors Subvert AI Control Protocols | Terekhov, Panfilov, Dzenhaliou, Gulcehre, Andriushchenko, Prabhu, Geiping | 2025 (v2 2026) | 1 / 2 | Q7 et co-évolution : injection d'invite dans les sorties du modèle non fiable ; moniteurs figés à base de grand modèle de langage. | 1-10 | 24747 |

Somme des caractères servis : **245378** (dix extraits ; moyenne 24537).

Fichiers : `extrait-IDENTIFIANT-v1.md` (identifiant sans le numéro de version ; la version du PDF est dans l'en-tête) et, pour chacun, son empreinte compagnon `extrait-IDENTIFIANT-v1.md.sha256`.

## 4. Autres occupants (liste complète des identifiants cités par au moins deux rapports)

Nombre par identifiant arXiv sur onze rapports. « Présent » : PDF dans le dépôt, non extrait faute de place (au plus dix papiers). « Absent » : voir `manquants-v1.md`.

| Identifiant | Titre ou nom | Premier auteur ou équipe | Année (d'après l'identifiant) | Rapports | PDF |
|---|---|---|---|---|---|
| 2609.36580 | SafeCoEvo | non donné par les rapports | 2026 | 6 | absent |
| 2603.00829 | Storf et al. (STRIDE, Gloom) | Storf | 2026 | 5 | absent |
| 2610.19422 | AgentSafeEvo | non donné | 2026 | 4 | absent |
| 2605.31140 | EvoDefense | non donné | 2026 | 4 | absent |
| 2605.13411 | EvoSafety | non donné | 2026 | 3 | absent |
| 2602.01539 | MAGIC | non donné | 2026 | 3 | absent |
| 2601.19726 | RvB | non donné | 2026 | 3 | absent |
| 2609.17560 | Promotion certifiée par e-processus | non donné | 2026 | 2 | absent |
| 2609.32267 | Promotion certifiée par e-processus | non donné | 2026 | 2 | absent |
| 2609.25848 | Optimizing the Score, Losing Sight of the Task | non donné | 2026 | 2 | absent |
| 2606.27091 | Inherited Circuits, Learned Semantics | Fetterman | 2026 | 2 | absent |
| 2509.17778 | Détection de rupture avec adversaire furtif, temps continu | Ramtin, Nain, Towsley | 2025 | 2 | absent |
| 2603.19461 | HyperAgents | Zhang, Clune, Foerster, Jiang et al. | 2026 | 2 | absent |
| 2609.19799 | Evolution or Illusion? | IBM | 2026 | 2 | absent |
| 2602.01425 | Building Better Deception Probes Using Targeted Instruction Pairs | Natarajan et al. | 2026 | 2 | absent |
| 2110.08514 | Analyzing Dynamic Adversarial Training Data in the Limit | Wallace et al. | 2021 | 2 | absent |
| 1912.06321 | Sim2Real Predictivity | Kadian et al. | 2019 | 2 | absent |
| 2511.17408 | The Impact of Off-Policy Training Data on Probe Generalisation | Kirch et al. | 2025 | 2 | absent |
| 2411.17693 | Adaptive Deployment of Untrusted LLMs Reduces Distributed Threats | Wen, Hebbar, Larson et al. | 2024 | 2 | présent (v1, 44 p.) |
| 2512.07810 | Auditing Games for Sandbagging | Taylor et al. | 2025 | 2 | présent (v1, 77 p.) |
| 2606.07054 | TRACE : raisonnement sur trajectoires par agrégation d'indices entre étapes | Mittapalli et al. | 2026 | 2 | présent (v1, 18 p.) |
| 2607.19321 | ResearchArena : sabotage et surveillance en recherche automatisée | Libon, Rank et al. | 2026 | 2 | présent (v2, 50 p.) |
| 2506.14261 | RL-Obfuscation : les modèles apprennent-ils à échapper aux moniteurs de l'espace latent ? | Gupta, Jenner | 2025 | 2 | présent (v4, 24 p.) |
| 2601.11516 | Building Production-Ready Probes For Gemini | Kramár et al. (Google DeepMind) | 2026 | 2 | présent (v4, 40 p.) |
| 2507.12691 | Benchmarking Deception Probes via Black-to-White Performance Boosts | Parrack, Attubato, Heimersheim | 2025 | 2 | présent (v3, 39 p.) |

Les dix papiers choisis (section 3) complètent cette liste. Papiers cités une seule fois et sans PDF : 2608.01388 (Zhang, Q3) et 1908.08016 (Kang et al., universalité des métriques) ; Gualandi, Maggio, Papadopoulos (MED 2022) n'a pas d'identifiant arXiv. Tous trois sont dans `manquants-v1.md`.

Les sept PDF présents sans extrait (Wen, Taylor, TRACE, ResearchArena, RL-Obfuscation, Kramár, Parrack) sont les premiers à extraire si la limite de dix papiers est levée.

## 5. Commande d'extraction et méthode

Texte du PDF par `pdftotext` (poppler), deux modes : `pdftotext FICHIER.pdf -` (flux de lecture, utilisé pour les paragraphes) et `pdftotext -layout FICHIER.pdf -` (mise en page, utilisé pour les tableaux et pour les colonnes entremêlées). Les pages sont séparées par les sauts de page du texte. Exception : `2510.09462v2` contient 72 sauts de page pour 52 pages réelles (les légendes de figure en créent) ; son texte a donc été extrait page par page (`pdftotext [-layout] -f N -l N FICHIER.pdf -`) pour que `[p.N]` soit la vraie page du PDF.

Assemblage : lignes rejointes en paragraphes ; coupures de mots en fin de ligne recollées seulement si le mot recomposé existe ailleurs dans le document ; coupes par ancres textuelles (jamais de reformulation) ; chaque coupe est marquée `[COUPÉ]` et chaque retrait de sûreté `[RETIRÉ POUR SÛRETÉ, p.N : raison]`. Les scripts d'assemblage sont restés dans le dossier temporaire de la session et ne sont pas livrés ; la fidélité se revérifie en cherchant une phrase de l'extrait dans la page citée.

Contrôle de fidélité fait avant le scellement : 1 336 phrases d'au moins 70 caractères, prises dans les dix extraits, ont été cherchées dans le texte de la page citée (espaces et césures normalisés, deux modes d'extraction) ; 1 283 retrouvées. Les 53 autres sont des notes de coupe ou de retrait de l'instance, des jonctions de coupe, ou des lignes de tableau reconstituées (césure non recollée). Je les ai relues une à une.

## 6. Retraits de sûreté (niveau méthode seulement)

Règle appliquée : seulement la classe d'attaque et le protocole d'évaluation ; jamais de recette, de consigne d'attaque ni d'exemple d'instruction de sabotage ou d'injection. Les en-têtes de chaque extrait détaillent les retraits ; en résumé :

- arXiv:2610.12445 : rien (aucune recette d'attaque : le papier entraîne des sondes de détection et évalue sur des environnements existants). Les annexes (transcriptions, invites) ne sont pas reprises.
- arXiv:2606.08892 : p.2 (figure 1 : exemple d'instruction de sabotage), p.6 (fragments d'instructions de sabotage cités et stratégie contre le détecteur), p.8 (instruction d'attaque intégrale de l'équipe rouge) ; annexes non reprises (elles contiennent les invites complètes). Seules les classes d'attaque et le protocole d'évaluation sont gardés.
- arXiv:2607.02514 : p.4 (consigne de cadrage donnée à l'agent attaquant), p.5 (exemples de tâches d'utilisateur servant de couverture), p.6 (figure 3 et paragraphes : exemple complet d'attaque graduelle par exfiltration, avec extrait de code), tableau 1 de p.3 ; annexes non reprises (elles contiennent les invites d'attaque et les séquences). Gardés : classes d'attaque (graduelle, positionnelle), protocole d'évaluation, moniteurs, résultats, limites.
- arXiv:2607.07368 : p.2 (texte de la figure 1 : exemple détaillé de chaîne d'attaque répartie, avec ses habillages de couverture), p.4 (clause sur l'incitation des agents à tenter les attaques) ; annexes non reprises (elles contiennent des cas d'attaque et les invites). Gardés : classes d'attaque (répartie sur 1, 3, 9 agents, avec ou sans planificateur), protocole d'évaluation, moniteurs, résultats, limites.
- arXiv:2605.09684 : p.3 (exemples d'attaque par niveau, avec mécanismes concrets), p.5 (exemple de tâche secondaire dissimulée par un cadrage anodin), p.8 (deux exemples concrets d'évasion et leur comparaison). Les annexes (taxonomie détaillée, invites de construction des attaques, exemples d'attaques non détectées) ne sont pas reprises. Gardés : classes (trois axes de la taxonomie), protocole de construction et d'évaluation, taux de détection, limites.
- arXiv:2602.14161 : rien (la figure 2, qui montrait des exemples de requêtes, n'est pas reprise).
- arXiv:2605.16626 : p.4 à p.6 : détail des 11 catégories d'angles morts et de leur mode d'exploitation (§3.3), colonne « Examples » du tableau 1, phrase de construction d'une transcription d'attaque (§3.2)  ; annexes non reprises (elles contiennent les invites des moniteurs et les transcriptions). Gardés : noms et définitions des classes, taux de détection, protocole d'évaluation, limites.
- arXiv:2412.09565 : p.1 (légende de la figure 0 : requête nuisible donnée en illustration), p.29 (paragraphe sur l'optimiseur et les réglages qui rendent les attaques par invite réussies) ; sections de construction détaillée des attaques non reprises. Gardés : définition de l'attaque d'obfuscation (classe), protocole d'évaluation (rappel à 1 % de faux positifs), entraînement adversarial des sondes sur plus de 70 époques, leçons et limites.
- arXiv:2601.20022 : rien (article théorique : aucune recette d'attaque). Les démonstrations des propositions sont omises par économie de place, les énoncés et hypothèses sont gardés.
- arXiv:2510.09462 : p.4 recette de construction des injections visant le moniteur ; p.5 paragraphe sur l'obtention d'une injection « sans exemple » ; p.8 figure 7 (exemple d'injection complète) et description de son fonctionnement ; annexes E (invites système de la politique d'attaque) et F (exemples d'attaques) non reprises. Gardés : classe d'attaque (injection d'invite dans les sorties du modèle non fiable, adaptative, connaissant le protocole et le moniteur), protocoles de contrôle, protocole d'évaluation, résultats chiffrés, discussion, limites.

Rien n'a été retiré pour Ramtin et al., Fomin et Hollinsworth et al. (théorie, évaluation de classificateurs et de sondes). Une recherche de motifs de commandes d'attaque (curl, wget, /etc/, sudo, base64, formules d'injection) sur les dix extraits ne trouve que des noms de classes de tâches (par exemple « élévation de privilèges ») dans MonitoringBench.

## 7. Réserves (ce que les papiers disent, comparé à ce que disent les rapports)

Chaque point est vérifié sur le PDF, page citée.

- SLEIGHT-Bench (2605.16626) : le titre du PDF n'est pas celui du billet cité par les rapports (« Finding Blind Spots in AI Monitors ») ; les catégories d'angles morts sont en partie établies après coup (p.3) ; les invites ciblées sont évaluées sur le même jeu (p.8) ; 20 attaques sur 40 ne sont jamais attrapées (p.7).
- Bailey et al. (2412.09565) : le PDF est la version 2 de février 2025 et ne mentionne pas ICLR 2026 (les rapports en parlent : non vérifiable ici) ; l'entraînement adversarial dure plus de 70 époques sans signe d'amélioration du défenseur (p.13).
- Terekhov et al., menaces diffuses (2606.08892) : l'argument « la surveillance est moins prometteuse » est cité de Hebbar, Gasteiger et Gan, non démontré par les auteurs (p.2) ; la défense est évaluée par une nouvelle optimisation de l'équipe rouge, pas sur des familles d'attaque tenues à l'écart (p.7).
- Terekhov et al., attaques adaptatives (2510.09462) : le PDF est la version 2 de mars 2026, sans mention d'ICLR (le rapport Q7 écrit « ICLR 2026 » : non vérifiable ici) ; tout le comportement subversif est induit par invite et peut être sous-élicité (p.10) .
- Hills et al. (2607.02514) et Angelini, Makins et al. (2607.07368) : les chiffres des rapports sont confirmés (Hills : détection de 87 % à 54 % et de 93 % à 47 % ; Makins : part inexpliquée de 38 % et 43 % sur p.8, taux de fausses alarmes de 3,6 % et 7,8 % sur p.12).
- Ramtin, Nain, Towsley (2601.20022) : théorie à observations indépendantes et de même loi, procédure CUSUM, adversaire qui connaît le paramètre γ ; les conditions (6) et (7) ne sont pas générales (p.8) ; proposition 3.3 et corollaire 3.1 (délai de détection en Θ(γ) quand γD = Θ(1), p.8-9) ; proposition 3.4 (dommage en Θ(γ^(1−ρ)), p.10). Aucun lien avec les modèles de langage ; le lien avec le lemme du programme reste une inférence.
- Hollinsworth et al. (2610.12445) : le moniteur boîte noire de comparaison (Opus 5.5) refuse 2 638 des 5 014 étapes positives, et un refus compte comme soupçon maximal (p.7) ; sondes 0,979 à 0,984 contre 0,960 sur 14 scénarios de SHADE-Arena sur 25 (p.6-7) ; sonde mal classée sur l'organisme math-sandbagger (63 %, p.9) et sur le niveau gratuit de l'organisme bird-labs (75 %, rappel de 2 %, p.9) ; la définition de « mensonge » est étroite (fausseté sue, p.2).
- MonitoringBench (2605.09684) : les auteurs demandent que le papier et le jeu de données soient exclus des corpus d'entraînement de modèles (p.9). Cet extrait est servi en lecture seule aux proposeurs et aux juges et ne doit entrer dans aucun entraînement. Un taux de fausses alarmes de 1 % par action se compose en 6,7 % à 17,4 % par trajectoire (p.7) : les taux d'attrapage par étape et par trajectoire ne sont pas comparables.
- Fomin (2602.14161) : l'écart de 8,0 à 16,5 points est mesuré sur des jeux de requêtes malveillantes (injection, évasion), pas sur des trajectoires d'agents ; l'auteur écrit lui-même que la méthode ne mesure pas la robustesse adverse (p.11).

Texte difficile à lire : les figures de Terekhov et al. (2510.09462) ont des polices encodées (texte brouillé, légendes gardées) ; les formules de Ramtin et al. et de Fomin sont extraites en texte linéaire, parfois dans le désordre ; les tableaux de Fomin, de Hills et de Makins sont reconstitués en mode mise en page (les chiffres sont ceux du PDF, la grille est approximative).

## 8. Contrôle avant scellement (règle R5)

- `LC_ALL=C.utf8 wc -m extrait-*-v1.md` : tous les extraits à 25 000 caractères ou moins (maximum 24941).
- Recherche (`grep -nE`) des trois motifs de clé d'accès fixés par le brief dans tous les fichiers du dossier : aucune ligne trouvée.
- `sha256sum -c *.sha256` dans ce dossier : tous OK (résultat repris dans la réponse de l'instance).
- Aucune lecture sous `donnees/`, aucun accès au réseau, aucune clé lue, aucune instance payante, aucun fichier existant modifié.

## 9. Fichiers du dossier

- 10 extraits `extrait-*-v1.md` et leurs 10 empreintes `.sha256` ;
- `manquants-v1.md` et son empreinte ;
- ce fichier et son empreinte.
