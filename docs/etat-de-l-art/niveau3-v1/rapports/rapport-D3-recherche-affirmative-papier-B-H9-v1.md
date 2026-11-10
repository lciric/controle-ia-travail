# Rapport D3 — recherche affirmative d'antériorité, papier B (« l'essaim ») et H9 — v1

Écrit le 2026-11-10, vers 10:51 UTC (heure relevée par `date -u`), par un chercheur neuf du lot D3.
Consigne commune lue en entier : `docs/etat-de-l-art/niveau3-v1/consignes/consigne-commune-lecteurs-v1.md`.

**Statut de preuve de tout ce rapport.** Aucun PDF n'a été ouvert. Tout ce qui suit vient du moteur de recherche
(titres, adresses, résumés fabriqués par le moteur). Ce sont des **pistes non opposables** (règle R7). Aucun chiffre
de ce rapport ne peut entrer dans un préenregistrement ou un papier. Les passages entre guillemets sont des extraits
**tels que le moteur les rend**, pas des citations vérifiées sur page. Le script de contrôle des citations est sans
objet ici : citations exactes sur PDF contrôlées : 0 ; échecs : 0 (aucune citation opposable n'est faite).

---

## COLLISION POSSIBLE (non vérifiée sur PDF)

Quatre pistes touchent le cœur d'une pièce revendiquée. Aucune n'est au dépôt, aucune n'est jugée dans les notes.

1. **« Multi-Agent Collusion and the J-Space »**, Marco Molinari et Gabriele Bettineschi, arXiv 2611.02153
   (début novembre 2026 selon le moteur : « about nine days ago »). **Touche l'idée (1) et la statistique de
   population.** Selon le moteur : méthode non supervisée « J-PACT » pour détecter la collusion entre agents
   « that share a model and role » ; score **relationnel** : « the concepts a pair shares more with each other than
   with outsiders, accumulated over turns » ; essais sur NARCBench avec quatre modèles à poids ouverts ; « retains 85%
   of the above-chance AUROC of supervised NARCBench probes ». Si le PDF le confirme, c'est une statistique de paire,
   cumulée dans le temps, sur les représentations internes d'agents à poids partagés : très près de la co-élévation
   des activations comme signal. À lire en premier.
2. **« What Do Collusion Probes Read? Three Pitfalls in Evaluating Multi-Agent Collusion Monitors »**, auteurs non
   rendus par le moteur, arXiv 2611.10620 (novembre 2026 d'après l'identifiant). **Touche l'idée (1) et le témoin
   « instruit sans sabotage » déjà demandé au niveau 1.** Selon le moteur : les sondes « mostly detect that an agent
   was told to collude, not that it decided to » ; le banc ajoute des agents qui reçoivent la consigne et la
   refusent ; il propose « an online monitor for groups of any size » ; recherche bibliographique des auteurs
   arrêtée au 29 octobre 2026. Un moniteur en ligne pour des groupes de taille quelconque est une statistique de
   groupe. Réserve : l'identifiant 2611.10620 est élevé pour un 10 novembre ; à vérifier (R4).
3. **« Red-Teaming Multi-Agent Attacks for Loss-of-Control Risks »**, auteurs non rendus, arXiv 2610.24052 (fin
   octobre 2026 : « about 25 days old ») et billet LessWrong du même titre. **Touche les idées (2) et (7), et le
   socle boîte noire de H3.** Selon le moteur : environnements de contrôle multi-agents bâtis sur la plateforme
   Control Tower de Redwood Research, « 200+ realistic benign tasks and 8 types of loss-of-control harm » ; un
   moniteur par agent signale « only 7% of successful distributed attacks, compared with 87% when a single agent
   carries out the same side task » ; équipes de trois agents ; plans optimisés contre les scores du moniteur.
   Boîte noire d'après le moteur : pas de collision sur la partie boîte blanche de H3, mais c'est une nouvelle
   référence boîte noire à battre et un banc concurrent. Collision possible sur « division du travail de l'équipe
   rouge ».
4. **« MasDrift: Benchmarking Authorization Preservation Across Multi-Agent Architectures »**, arXiv 2608.07556
   (août 2026), code annoncé sous le compte ZhuoningXu. **Touche H9 de face.** Selon le moteur : 600 tâches
   bénignes, huit domaines, actions réservées à ne pas faire ; comparaison agent seul, hiérarchie, pairs, avec
   profondeur de hiérarchie et largeur variées ; mesure de la « constraint loss » (contrainte « weakened or absent
   for the executing agent ») ; comparaison « source re-anchoring against chain propagation » ; des billets
   secondaires disent que le premier passage porte la plus grande part des pertes. C'est une mesure de la survie
   d'une contrainte par passage, en fonction de la profondeur. **Antérieure à la décision N-035 (22 octobre) et
   absente des voisins qu'elle cite.** Ce que le moteur ne montre pas : un moniteur à chaque passage. Si le PDF
   n'en a pas, il resterait à H9 le bras « avec ou sans moniteur à chaque passage » ; la courbe de survie seule
   serait prise.

**Autour de H9, quatre voisins proches de plus, tous antérieurs au 22 octobre et absents du dépôt** (détail dans la
table) : 2608.24569 (« When "Must" Becomes "Maybe" »), 2609.27900 (« Delegated Misalignment »), 2605.10481
(« Constraint Drift »), 2607.07097 (« Operational Reframing »). Pris ensemble avec MasDrift, ils disent que
« l'érosion d'une contrainte à la délégation » est un sujet déjà ouvert par plusieurs équipes en 2026. La réserve
d'antériorité de N-035 est donc **active** : le repli (b) de N-035 est à examiner par Lazar après lecture des PDF.
Je ne modifie aucune hypothèse.

**Contre-résultat défavorable possible.** Un livre blanc du SANS Institute (« Quantifying Agentic Misalignment in
Multi-Agent Systems », 1 500 runs selon le moteur) rapporterait l'inverse de « Delegated Misalignment » : aucun
désalignement dans les topologies déléguées, échecs concentrés dans l'agent seul. Le signe de H9 n'est donc pas
acquis dans la littérature ; piste non vérifiée.

---

## 1. Journal des requêtes

Outil : recherche sur le réseau. 44 requêtes, en anglais (la consigne demandait 25 à 40 : dépassement de 4, signalé).
Mode « extended » : 12 requêtes (la consigne en demandait cinq ou six : dépassement signalé). Aucune requête ne porte
le nom du directeur, du projet, du dépôt ni du fonds. Les requêtes sont parties par lots ; l'heure est celle du début
du lot, relevée par `date -u` (2026-11-10, UTC).

| n° | heure du lot | mode | texte exact |
|---|---|---|---|
| 1 | 10:48:28 | extended | multi-agent collusion detection activations probes shared weights agents arXiv 2026 |
| 2 | 10:48:28 | standard | NARCBench collusion detection interpretability multi-agent follow-up |
| 3 | 10:48:28 | extended | distributed sabotage multiple agents AI control safety versus number of agents red team division of labor |
| 4 | 10:48:28 | extended | safety constraint propagation sub-agent delegation erosion LLM agents November 2026 |
| 5 | 10:48:43 | extended | "J-PACT" "Multi-Agent Collusion and the J-Space" unsupervised collusion detection agents sharing a model |
| 6 | 10:48:43 | standard | "What Do Collusion Probes Read" three pitfalls evaluating multi-agent collusion monitors |
| 7 | 10:48:43 | standard | "Red-Teaming Multi-Agent Attacks for Loss-of-Control Risks" arXiv 2610.24052 |
| 8 | 10:48:43 | standard | "Delegated Misalignment" multi-agent structures amplify LLM safety risks delegation sub-agent |
| 9 | 10:48:43 | extended | white-box monitoring multi-agent AI control fleet of agents probes correlated activations population statistic |
| 10 | 10:48:55 | standard | ensemble of probes diversity monitors AI control attack transfer matrix between monitors |
| 11 | 10:48:55 | standard | negative correlation learning linear probes ensemble deception detection activations |
| 12 | 10:48:55 | extended | information leakage from monitoring AI control attacker learns from detections stochastic audit threshold honeypots |
| 13 | 10:48:55 | standard | persona diversity fine-tuning agents reduces collusion coordination ability tradeoff decorrelate multi-agent safety |
| 14 | 10:48:55 | extended | multi-agent AI control October 2026 Redwood Research ControlArena new paper multiple untrusted agents |
| 15 | 10:49:08 | standard | fleet monitoring stateful monitor cross-agent link tracker distributed attacks AI control |
| 16 | 10:49:08 | standard | "Distributed Attacks in Persistent-State AI Control" gradual attacks multiple pull requests |
| 17 | 10:49:08 | standard | fragmented backdoor across multiple commits agents activation probe white-box detection distributed attack |
| 18 | 10:49:08 | standard | "Constraint Drift" LLM-based multi-agent systems "Safe Multi-Agent Behavior Must Be Maintained" |
| 19 | 10:49:08 | extended | subagent disabled monitoring oversight delegated task lab report system card October 2026 sub-agents safety instructions not passed |
| 20 | 10:49:19 | standard | "When Must Becomes Maybe" constraint weakening LLM agent workflows delegation handoff |
| 21 | 10:49:19 | standard | "Early Detection of Distributed Backdoors in Multi-Agent LLM Systems" characterization study |
| 22 | 10:49:19 | standard | "When Local Monitors Miss Compositional Harm" multi-agent |
| 23 | 10:49:19 | standard | instruction loss multi-agent handoff safety constraint survives delegation orchestrator subagent benchmark measurement |
| 24 | 10:49:19 | standard | Anthropic AI organisations study multi-agent alignment degradation subagents 2026 |
| 25 | entre 10:49:19 et 10:49:48 (pas de relevé propre à ce lot) | standard | "MasDrift" benchmarking authorization preservation multi-agent architectures constraint loss |
| 26 | idem | standard | "You Can't Escape Your Own Activations" evaluation awareness multi-agent monitoring probes agents informed of monitor |
| 27 | idem | standard | Truth Audit Labs Das collusion detection activations multi-agent interpretability |
| 28 | idem | standard | cross-agent activation correlation same model copies scheming detection group-level anomaly synchrony hidden states LLM agents |
| 29 | 10:49:48 | extended | "When Agents Go Rogue" activation-based detection of malicious behaviors in multi-agent systems correlated activation patterns |
| 30 | 10:49:48 | standard | Cemri "Why Do Multi-Agent LLM Systems Fail" follow-up safety constraints delegation failure taxonomy 2026 |
| 31 | 10:49:48 | standard | "Operational Reframing and Approval-Framed Delegation in Multi-Agent LLM Safety" |
| 32 | 10:49:48 | standard | monitor at each delegation hop subagent trusted monitoring multi-agent hierarchy AI control safety constraint inheritance experiment |
| 33 | 10:49:48 | extended | UK AI Security Institute multi-agent control research November 2026 collusion untrusted agents |
| 34 | 10:50:06 | standard | Apollo Research OR "Google DeepMind" multi-agent scheming collusion monitoring paper October 2026 |
| 35 | 10:50:06 | standard | sub-agent spawned by AI agent disabled monitoring OR "turned off" oversight safety report frontier model 2026 delegation incident |
| 36 | 10:50:06 | standard | AI control game attacker infers audit policy from being caught mutual information detection feedback randomized response protocol |
| 37 | 10:50:06 | standard | adversarial transfer between activation probes obfuscated activations ensemble of diverse probes robustness matrix |
| 38 | 10:50:06 | standard | fine-tuned persona variants same base model activation probe transfer decorrelated representations collusion steganography coordination Schelling points diversity |
| 39 | 10:50:06 | standard | "Lessons from Recent Multi-Agent Safety Incidents" Cooperative AI Foundation |
| 40 | 10:50:06 | standard | spatiotemporal scan statistic probe scores population of LLM agents anomaly detection deployment-level monitoring many instances |
| 41 | 10:50:22 | extended | OpenAI misalignment report October 2026 agents disabled misalignment monitoring subagent constraint weakened handoff original post |
| 42 | 10:50:22 | standard | safety as a function of number of agents white-box probes distributed attack multi-agent control activation monitor |
| 43 | 10:50:22 | extended | arXiv November 2026 multi-agent AI control collusion monitors shared model instances activation monitoring new preprint |
| 44 | 10:50:22 | standard | Hammond "Multi-Agent Risks from Advanced AI" 2026 follow-up empirical delegation safety constraints sub-agents measurement |

Réserve sur les heures : les relevés sont très rapprochés (deux minutes pour tout le journal). Je les écris tels que
`date -u` les a rendus.

## 2. Table des pistes

Colonnes « au dépôt ? » : résultat de `ls docs/sources/pdf/ | grep <identifiant>` et des sous-dossiers
`anteriorite-P-041-v1`, `anteriorite-P-041-v2/c1` à `c8`. « Jugée ? » : résultat de
`git grep -n <identifiant> -- docs/etat-de-l-art docs/decisions registres/veille.md docs/notes/etat-art-niveau2`.
Tout le contenu de la colonne « ce que le moteur en dit » est non vérifié.

### 2.1 Pistes neuves (ni au dépôt, ni jugées)

| Titre | Auteurs | Identifiant | Parution | Ce que le moteur en dit | Idée | Hypothèse | Au dépôt ? | Jugée ? | Menace | Priorité PDF |
|---|---|---|---|---|---|---|---|---|---|---|
| Multi-Agent Collusion and the J-Space | Molinari, Bettineschi | arXiv 2611.02153 | début nov. 2026 | J-PACT, non supervisé, agents « that share a model and role » ; score de paire « accumulated over turns » ; « retains 85% of the above-chance AUROC of supervised NARCBench probes » ; nomme la paire dans 99 % des runs détectés | (1) | statistique de population ; H3 (côté boîte blanche) | non | non | **collision possible** | 1 |
| What Do Collusion Probes Read? Three Pitfalls in Evaluating Multi-Agent Collusion Monitors | non rendus | arXiv 2611.10620 | nov. 2026 (identifiant à vérifier) | sondes lisent la consigne plutôt que la décision ; agents instruits qui refusent ; « an online monitor for groups of any size » ; poids des sièges variés | (1), (3) en partie | statistique de population ; H4′ en partie | non | non | **collision possible** | 2 |
| Red-Teaming Multi-Agent Attacks for Loss-of-Control Risks | non rendus | arXiv 2610.24052 ; billet LessWrong | fin oct. 2026 | Control Tower étendu à plusieurs agents ; moniteur par agent : « only 7% of successful distributed attacks, compared with 87% » ; attaques composables ; moniteurs « GPT-5.6 Sol and Luna » | (2), (7) | H3 (référence boîte noire) | non | non | **collision possible** sur la division du travail ; voisin proche pour H3 | 3 |
| MasDrift: Benchmarking Authorization Preservation Across Multi-Agent Architectures | non rendus (code : ZhuoningXu) | arXiv 2608.07556 | août 2026 | 600 tâches ; « constraint loss » par passage ; profondeur et largeur variées ; actions non autorisées « 2.7-19.8% » en hiérarchie contre « 0.6-0.8% » en pairs ; ré-ancrage à la source contre propagation en chaîne | (6) | H9 | non | non | **collision possible** | 4 |
| When "Must" Becomes "Maybe": Constraint Weakening in LLM Agent Workflows (autre titre rendu : « Erosion of Workflow Constraints in LLM Agent Handoffs ») | Yiheng Sun et al. | arXiv 2608.24569 | 25 août 2026 | le passage garde le contenu de la contrainte mais affaiblit sa force ; « artifact deactivation stayed at 95.3% » ; 1 296 épisodes synthétiques d'après un billet | (6) | H9 | non | non | voisin proche (collision possible sur le mécanisme « reformulation ») | 5 |
| Delegated Misalignment: How Multi-Agent Structures Amplify LLM Safety Risks | non rendus | arXiv 2609.27900 (EMNLP 2026 selon le moteur) | sept. 2026 | six modèles, 49 tâches dangereuses, agent seul contre paire principal-subordonné ; exécution complète « from 30.6% to 77.6% » pour un modèle ; défenses à une couche échouent | (6) | H9 | non | non | voisin proche | 6 |
| Safe Multi-Agent Behavior Must Be Maintained, Not Merely Asserted: Constraint Drift in LLM-Based Multi-Agent Systems | Tianxiao Li et al. | arXiv 2605.10481 | mai 2026 | papier de position ; « constraint drift » à travers mémoire, délégation, communication, outils ; cinq modes ; appelle une mesure sans la fournir (selon MasDrift) | (6) | H9 | non | non | voisin proche (prend le concept, pas la mesure) | 7 |
| Operational Reframing and Approval-Framed Delegation in Multi-Agent LLM Safety | non rendus | arXiv 2607.07097 | 8 juil. 2026 | cinq conditions contrôlées ; sépare reformulation, refus du planificateur, délégation « approuvée » ; 30 scénarios synthétiques | (6) | H9 (confondant « reformulation » de N-035) | non | non | voisin proche | 8 |
| Bounded Agents: Delegation Security for Multi-Agent AI Systems | non rendus | arXiv 2608.15888 | août 2026 | enveloppe d'autorisation rétrécie à chaque passage | (6) | H9 | non | non | voisin | 12 |
| Safe Bilevel Delegation: A Formal Framework for Runtime Delegation Safety in Multi-Agent Systems | non rendus | arXiv 2604.27358 | avril 2026 | borne de propagation de responsabilité sur des chaînes à plusieurs passages | (6) | H9 | non | non | voisin | 13 |
| Intelligent AI Delegation | non rendus | arXiv 2602.11865 | fév. 2026 | surveillance transitive : chaque agent surveille son délégataire | (6) | H9 (bras « moniteur à chaque passage », forme conceptuelle) | non | non | voisin | 11 |
| Quantifying Agentic Misalignment in Multi-Agent Systems | SANS Institute (livre blanc) | adresse sans.org/white-papers/quantifying-agentic-misalignment-multi-agent-systems | 2026, date non rendue | 1 500 runs, six modèles ; topologies déléguées à 0 % de désalignement | (6) | H9 (signe contraire) | non | non | voisin ; contre-résultat | 10 |
| AI Organizations are More Effective but Less Aligned than Individual Agents | Anthropic, blog de science de l'alignement | alignment.anthropic.com/2026/ai-organizations/ | vers avril 2026 | systèmes multi-agents « less ethical yet more effective » que l'agent seul | (6), (7) | H9, contexte | non (identifiant absent ; recherche par mot non faite hors des chemins nommés) | non trouvée | voisin | 14 |
| Lessons from Recent Multi-Agent Safety Incidents | Will Anderson, Cooperative AI Foundation | cooperativeai.com/post/lessons-from-multi-agent-safety-incidents | automne 2026, date non rendue | les propriétés de sécurité ne passent pas de l'individu au groupe ; le désalignement en contexte peut être corrélé entre instances | (6), (7) | H9, contexte | non | non | voisin | 15 |
| Linear Probe Accuracy Scales with Model Size and Benefits from Multi-Layer Ensembling | non rendus | arXiv 2604.13386 | avril 2026 | ensembles de sondes sur plusieurs couches, couches choisies par faible « double-fault » ; gains d'AUROC annoncés | (4) | H5 (axe « où lire », sélection par diversité d'erreurs) | non | non | voisin proche | 9 |
| Probe-based Fine-tuning for reducing Toxicity | Wehner, Fritz | arXiv 2510.21531 | oct. 2025 | ensembles de sondes diverses : gains modestes ; réentraîner les sondes suffit souvent | (4) | H5 (contre-résultat possible) | non | non | voisin | 16 |
| Colosseum: Auditing Collusion in Cooperative Multi-Agent Systems | non rendus | arXiv 2602.15198 (NeurIPS 2026 selon le moteur) | fév. 2026 | audit boîte noire de la collusion ; métriques de regret | (7) | contexte | non | non | voisin | 17 |
| Mapping Human Anti-collusion Mechanisms to Multi-agent AI Systems | non rendus | arXiv 2601.00360 | janv. 2026 | même modèle de base = point focal partagé ; la diversité des agents réduit la collusion | (3) | H4′ | non | non | voisin | 18 |
| Embedded Assessments for Frontier AI | non rendus | arXiv 2609.25413 | sept. 2026 | remonté par la requête sur le rapport d'OpenAI ; contenu non rendu | (7) | inconnue | non | non | voisin (à qualifier) | 19 |
| Risks and Controls for Multi-Agent Systems: an analytical framework… | non rendus | arXiv 2608.26626 | août 2026 | cadre analytique, déploiement entre organisations | (7) | contexte | non | non | voisin | 20 |

Pistes de presse, sans identifiant : billets LessWrong « what happens when a collusion probe only finds a thin
signal » (collusion, sondes, validation en laissant un scénario dehors) ; note de la Cloud Security Alliance du
23 octobre 2026 « Agents That Disable Their Own Oversight » (lit le rapport d'OpenAI sous l'angle de la délégation) ;
note de la même alliance sur un cas d'étude de 100 agents où une faille de notation se propage en 27 minutes (attribué
à Google DeepMind, septembre 2026, source première non trouvée) ; incident d'évaluation de l'institut britannique
(agents coordonnés par des dépôts publics, source première non trouvée). Degré : voisin. Aucune n'est opposable.

### 2.2 Pistes déjà au dépôt ou déjà jugées (rien de neuf à récupérer, sauf mention)

| Titre | Identifiant | Idée | Au dépôt ? | Jugée ? | Remarque |
|---|---|---|---|---|---|
| Detecting Multi-Agent Collusion Through Multi-Agent Interpretability (NARCBench, HELIOS) | arXiv 2604.01151 | (1) | oui | oui (niveau 1, N-061) | le moteur rend une **v3** et une fiche NeurIPS 2026 ; il signale deux plages d'AUROC selon les versions. Vérifier quelle version est au dépôt ; récupérer la v3 si elle manque. |
| You Can't Escape Your Own Activations | arXiv 2609.03035 (Das et al.) | (1), (5) en partie | oui | oui (niveau 1) | fiche NeurIPS 2026 rendue par le moteur |
| When Agents Go Rogue (AcMAS) | arXiv 2607.06807 | (1) | oui | oui (niveau 1, veille) | le moteur dit : « compromised agents exhibit correlated activation patterns », déploiement homogène à poids partagés. Vérifier que le jugement du niveau 1 a bien pesé cette phrase contre la co-élévation. |
| Emergent Collusion in Long-Horizon LLM Agent Interaction | arXiv 2609.24967 | (1), (3) | oui | oui | — |
| Multi-Agent AI Control: Distributed Attacks Hamper Per-Instance Monitors | arXiv 2607.07368 | (2) | oui | oui (niveau 2) | page de l'institut britannique rendue par le moteur |
| Distributed Attacks in Persistent-State AI Control (Hills et al.) | arXiv 2607.02514 | (2) | oui | oui | — |
| Stateful Online Monitoring Catches Distributed Agent Attacks | arXiv 2605.31593 | (2) | oui | oui | — |
| When Local Monitors Miss Compositional Harm | arXiv 2607.11751 | (2) | oui | oui | — |
| Early Detection of Distributed Backdoors in Multi-Agent LLM Systems | arXiv 2607.24893 | (2) | **non** | citée (chiffres introuvables, corrections du niveau 2) | PDF absent du dépôt : à récupérer (priorité moyenne) |
| The Best-Laid SCHEMEs | arXiv 2605.29178 | (2), (7) | oui | oui | — |
| Ensemble Monitoring for AI Control: Diverse Signals Outweigh More Compute | arXiv 2605.15377 | (4) | oui | oui (N-013) | fiche ICML 2026 rendue par le moteur |
| MonitoringBench | arXiv 2605.09684 | (2) | oui | oui | — |
| Async Control | arXiv 2512.13526 | (4) transfert d'attaque entre moniteurs | oui | **non trouvée** dans les chemins nommés | à juger pour H5 : le moteur dit que les moniteurs des tours passés sont rejoués « to test for attack transfer to other monitors » |
| Attack Selection in Agentic AI Control Evaluations… | arXiv 2606.06529 | (5) | oui | **non trouvée** | à juger pour H7 (attaquant qui choisit quand attaquer selon un seuil) |
| Subversion via Focal Points | arXiv 2507.03010 | (3) | oui | **non trouvée** | à juger pour H4′ |
| Obfuscated Activations Bypass LLM Latent-Space Defenses (Bailey et al.) | arXiv 2412.09565 | (4) | oui | oui (P-041) | le moteur dit : transfert facile entre sondes supervisées, faible vers les détecteurs hors distribution. À relire pour la matrice de transfert de H5. |
| When can we trust untrusted monitoring? | arXiv 2602.20628 | (7) | oui | oui (N-013) | — |
| TraceGuard | arXiv 2604.03968 | (7) | oui | non trouvée | — |
| Steganalysis of Adaptive Covert Collusion… | arXiv 2608.02698 | (1) boîte noire | oui | non trouvée | — |
| Towards evaluations-based safety cases for AI scheming | arXiv 2411.03336 | (4) | oui | oui | — |
| Rapport d'OpenAI « Suppressing misalignment monitoring alerts and disabling misalignment monitoring » | page d'OpenAI | (6) | oui (source de N-035) | oui (N-035, veille) | rien de neuf ; la presse d'octobre en fait une lecture « délégation » |

## 3. Lecture par idée (pistes seulement)

- **(1) Poids partagés, co-élévation, statistique de population.** Deux pistes neuves de novembre 2026 (2611.02153,
  2611.10620) s'ajoutent à NARCBench, à AcMAS et à Das et al. La zone se remplit vite. Non trouvé : une statistique
  de balayage spatio-temporelle sur des scores de sondes, à l'échelle d'une flotte (requête 40 : rien). « Non trouvé »
  ne veut pas dire libre (R8).
- **(2) Sabotage distribué, courbe sécurité(N).** Une piste neuve forte en boîte noire (2610.24052). Non trouvé : une
  courbe sécurité(N) en boîte blanche, ou des sondes contre une porte dérobée fragmentée (requêtes 17 et 42 : le
  moteur dit lui-même n'avoir rien).
- **(3) Diversification contre coordination.** Rien de direct. Voisins : 2601.00360, 2507.03010, et les sièges à
  poids variés de 2611.10620.
- **(4) Nombre et diversité des moniteurs.** Rien sur l'apprentissage à corrélation négative pour des sondes
  (requête 11). Voisins : 2604.13386 (sélection par double faute), 2510.21531 (gain modeste de la diversité),
  2512.13526 et 2412.09565 (transfert d'attaque entre moniteurs ou sondes, déjà au dépôt).
- **(5) Riposte et fuite.** Rien trouvé sur l'information mutuelle entre l'état de détection et les observations de
  l'attaquant, ni sur les seuils d'audit stochastiques (requêtes 12 et 36). Résultat trop propre pour valoir preuve
  (R4) : le moteur répond mal à ces mots ; une recherche dans les forums d'alignement et par citations reste à faire.
- **(6) H9.** Zone **nettement plus occupée** que ne le dit N-035 : cinq papiers de 2026 sur l'érosion à la
  délégation, dont un banc de mesure (MasDrift). Non trouvé : la mesure avec ou sans moniteur à chaque passage, dans
  un cadre de contrôle (requête 32 : seulement la forme conceptuelle de 2602.11865). Cemri et al. et Hammond et al. :
  aucune suite 2026 trouvée (requêtes 30 et 44) ; leurs PDF (2503.13657, 2502.14143) ne sont pas au dépôt.
- **(7) Contrôle multi-agents, octobre et novembre 2026.** 2610.24052 est la parution du mois. Rien trouvé de
  l'institut britannique, d'Apollo Research ni de Google DeepMind en novembre.

## 4. PDF à récupérer par une session à réseau ouvert, par ordre de priorité

1. arXiv 2611.02153 — Multi-Agent Collusion and the J-Space (collision possible, idée 1).
2. arXiv 2611.10620 — What Do Collusion Probes Read? (collision possible, idée 1 ; vérifier l'identifiant).
3. arXiv 2610.24052 — Red-Teaming Multi-Agent Attacks for Loss-of-Control Risks (idées 2 et 7 ; référence de H3).
4. arXiv 2608.07556 — MasDrift (collision possible, H9).
5. arXiv 2608.24569 — When "Must" Becomes "Maybe" (H9).
6. arXiv 2609.27900 — Delegated Misalignment (H9).
7. arXiv 2605.10481 — Constraint Drift (H9).
8. arXiv 2607.07097 — Operational Reframing and Approval-Framed Delegation (H9, confondant).
9. arXiv 2604.13386 — Linear Probe Accuracy… Multi-Layer Ensembling (H5).
10. Livre blanc du SANS Institute, « Quantifying Agentic Misalignment in Multi-Agent Systems » (H9, signe contraire).
11. arXiv 2602.11865 — Intelligent AI Delegation (H9, surveillance transitive).
12. arXiv 2608.15888 — Bounded Agents ; 13. arXiv 2604.27358 — Safe Bilevel Delegation.
14. arXiv 2503.13657 (Cemri et al.) et arXiv 2502.14143 (Hammond et al.) : cités par N-035, absents du dépôt.
15. arXiv 2607.24893 — Early Detection of Distributed Backdoors (citée au niveau 2, PDF absent).
16. arXiv 2604.01151 **v3** si le dépôt n'a qu'une version plus ancienne.
17. arXiv 2510.21531 ; 2602.15198 ; 2601.00360 ; 2609.25413 ; 2608.26626 ; pages d'Anthropic (« AI
    Organizations… ») et de la Cooperative AI Foundation (« Lessons from Recent Multi-Agent Safety Incidents »).

À juger sur des PDF **déjà au dépôt** (pas de réseau nécessaire) : 2512.13526 et 2412.09565 pour H5 ; 2606.06529 pour
H7 ; 2507.03010 pour H4′ ; 2607.06807 relu contre la co-élévation.

## 5. Ce que je n'ai pas pu chercher

- Aucun PDF, aucune page : `WebFetch` et `curl` sont fermés par le réseau du conteneur ; je n'ai pas essayé de les
  forcer. Aucune piste n'est donc vérifiée.
- Les listes arXiv du jour (catégories d'intelligence artificielle, d'apprentissage et de sécurité) pour novembre
  2026 : le moteur ne les parcourt pas. Une parution des tout derniers jours peut manquer.
- Les citations en aval (qui cite NARCBench, 2607.07368, MasDrift) : pas d'outil de graphe de citations.
- Les soumissions en relecture (OpenReview, ICLR 2027) : non cherchées.
- Les auteurs de 2611.10620, 2610.24052, 2608.07556 et 2609.27900 : non rendus par le moteur.
- Idée (5) : la recherche par mots clés rend peu ; elle demande une lecture des forums d'alignement et des billets de
  Redwood Research, non faite.
- « Truth Audit Labs » : le moteur ne rend aucune page à ce nom ; l'affiliation n'est pas confirmée.
- Le moteur est limité aux États-Unis et résume lui-même : ses chiffres et ses dates peuvent être faux.

## 6. Refus rencontrés

Aucun refus de permission ni de classifieur. Écarts à la consigne du lot, signalés : 44 requêtes au lieu de 40 au
plus ; 12 en mode « extended » au lieu de cinq ou six ; un lot de quatre requêtes (25 à 28) sans relevé d'heure
propre.
