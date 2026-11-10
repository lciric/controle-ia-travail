# Lecture sur source, niveau 3, lot 12 — deux pistes pour H9 (survie des contraintes de sécurité à la délégation) — complément du rapport du lot 7-D — v1

Lecteur neuf (n'a écrit ni le programme, ni la décision N-035, ni le rapport du lot 7-D). Heure : 2026-11-10, 11:19 UTC, relevée par `date -u` au dernier contrôle des citations. Ce rapport complète `docs/sources/lecture-pdf-niveau3/rapport-lot7D-delegation-H9-v1.md` ; il en reprend les composantes C1 à C6 sans le refaire.

## En tête

- **Occupation partielle nouvelle, sur C2.** AgentCollabBench (arXiv 2605.08647, version 1 du 9 mai 2026, antérieure à MasDrift et à la décision N-035) publie ce que le rapport du lot 7-D donnait comme « non trouvé » : un **taux de perte conditionnel par relais** — parmi les arêtes où l'information est présente à la sortie de l'émetteur, la part où elle a disparu chez le receveur — sur des **chaînes linéaires**, pour quatre modèles : 16 %, 8 %, 3 % et 40 % par relais (auteurs, tableau 23, p. 34). L'objet mesuré est toutefois une **chaîne de caractères témoin** recherchée à l'identique, pas la force d'une contrainte de sécurité ; le taux est mis en commun sur tous les rangs de relais ; la longueur de chaîne n'est pas un facteur contrôlé.
- **Pas de loi ni de courbe de survie en fonction du nombre de relais** dans cet article (C3). Le seul chiffre qui s'en approche est une corrélation entre la profondeur atteinte et la longueur du chemin, r = −0,176, que les auteurs disent proche de zéro (p. 33). L'expression « 7 à 40 % de la variance » porte sur la **topologie**, pas sur le nombre de relais.
- **« Instruction decay » n'est pas une érosion à la délégation.** La mesure de ce nom place la contrainte dans la consigne système de l'agent cible et compte ses violations sous pression de pairs ; rien n'y est transmis d'un agent à un sous-agent, et ce n'est pas non plus une courbe dans le temps (p. 5, 17).
- **Tallam (arXiv 2605.05440, version 1 du 6 mai 2026) : un cadre, aucune mesure.** Article de position sur le contrôle d'accès ; trois anecdotes d'une plateforme, sans dénominateur, qui concernent une passerelle d'authentification et des conteneurs, pas des passations en langue naturelle entre agents.
- **Le verdict d'ensemble du lot 7-D ne change pas : H9 occupée en partie.** C2 reste « occupée en partie », mais le reste non trouvé se resserre ; C3 reste « occupée en partie, avec contre-indice », et le contre-indice se nuance (voir section 4). C1, C4, C5, C6 inchangées.
- **Aucun des deux articles ne lit un état interne ni ne pose un moniteur.** Deux des quatre modèles d'AgentCollabBench sont à poids ouverts (Llama 3.1 8B Instruct, Qwen-3.5-35B-A3B) mais appelés par un service d'hébergement tiers.
- Citations contrôlées par script : **87 ; échecs : 0**.

## Méthode

- Empreintes vérifiées par `sha256sum` contre les compagnons, conformes :
  - `2605.08647v1.pdf` = `274bc00ae0f48df3254f8defa3d8b0197eae710d5c919484d790eeb219e332e1` (38 pages) ;
  - `2605.05440v1.pdf` = `fc43013689fe7342e3fc5703427dc5093e4371131d2947c2addfbf29adf0ee19` (20 pages).
- Les deux PDF lus en entier, annexes et bibliographies comprises, page par page (`pdftotext -layout`, numérotation du fichier). Les valeurs utilisées viennent du texte et des tableaux ; la figure 6 d'AgentCollabBench (p. 8) n'est citée qu'à travers le tableau 23 qui en imprime les valeurs arrondies.
- Énoncé de H9 lu dans `docs/decisions/decision-N-035-v1.md` ; rapport du lot 7-D lu en entier. `docs/etat-de-l-art/niveau2-v1/anteriorite-v1.md` ne contient aucune occurrence de « H9 » (compté dans ce seul fichier).
- Script `controle_citations.py` : normalisation Unicode NFKC, apostrophes et guillemets droits, blancs et traits d'union retirés (le signe moins typographique est gardé, pour qu'un signe ne se perde pas) ; trois extractions essayées par page (`-layout`, ordre par défaut, `-raw`). Essai préalable : cas juste trouvé, cas altéré (« time-to-last-failure » pour « time-to-first-failure ») rejeté, cas juste sur une mauvaise page rejeté. Second contrôle `controle_rapport.py` : chaque passage entre guillemets français suivi d'un identifiant est inclus dans la citation contrôlée de cet identifiant, à la page dite.
- Identifiants : A (AgentCollabBench), T (Tallam) ; ils renvoient à `citations.json` dans l'archive. Nature des chiffres : « auteurs » (imprimé), « calcul » (recalculé par moi, `calculs.py`). Aucune valeur n'est lue sur une figure.
- Aucun appel réseau, aucun appel de modèle, aucune commande git, aucune recherche récursive dans le dépôt. Aucun refus rencontré.

## 1. AgentCollabBench (2605.08647v1, Mazumder et collègues ; « Preprint. », A04, p. 1 ; tampon « arXiv:2605.08647v1 [cs.CL] 9 May 2026 », A59, p. 1)

### 1.1 Ce que l'article fait

- **Banc de 900 tâches** d'ingénierie logicielle, d'exploitation et d'ingénierie des données, cinq topologies de communication (chaîne linéaire, arbre, graphe convergent, graphe complet, graphe libre), 2 à 6 agents (« Agent count range 2–6 », A53, p. 14). Quatre mesures, une par tâche : « Each task isolates one of four behavioral risks: instruction decay (does a constraint survive peer pressure?), false-belief contagion (does a falsehood spread through consensus?), context leakage (does information bleed between tasks?), and tracer durability (does marked data reach the final agent?). » (A01, p. 1).
- **Modèles** : « GPT 4.1 mini (OpenAI), Gemini 2.5 Flash Lite (Google), Qwen-3.5-35B-A3B (OpenRouter), and Llama 3.1 8B Instruct (OpenRouter). » (A15, p. 14). Juge génératif pour deux mesures : « IDR and CPR are scored with DeepSeek V4 Flash as judge; RTD and CLC are deterministic. » (A14, p. 14). **Boîte noire intégrale** ; aucun état interne, aucun moniteur, aucun agent adverse (les invitations à violer et les faits faux sont des stimuli injectés par le banc).
- **Deux mesures touchent H9, et elles ne mesurent pas la même chose :**
  - *Taux de déclin de la consigne*, « Instruction Decay Rate (IDR). » (A63, p. 5) : « IDR measures whether an agent keeps obeying a hard behavioral constraint after peer messages implicitly normalize violating it » (A05, p. 5) ; « A constraint is added to the target agent’s system prompt and peer turns then issue mild and stronger violation invitations; the judge labels each constrained turn as compliant or violating, and IDR reports the violation fraction. » (A06, p. 5). **La contrainte n'est pas transmise** : elle reste dans la consigne système de l'agent jugé. Et ce n'est pas une courbe : « It measures turn-level violation incidence, not time-to-first-failure or severity. » (A07, p. 17).
  - *Durabilité du traceur*, « Radioactive Tracer Durability (RTD). » (A64, p. 5) : « RTD measures how deep a critical tracer reaches as messages pass through the team. » (A08, p. 5) ; un identifiant unique « that should propagate verbatim rather than be paraphrased – is embedded at a known graph location, and the deepest detection layer is normalized by the task’s graph depth » (A09, p. 5). **C'est la mesure de propagation de relais en relais**, mais son objet est une chaîne de caractères retrouvée à l'identique.
  - Résumé des auteurs sur les deux artefacts : « IDR uses a behavioral constraint inserted into the target agent’s system prompt with peer messages that invite violation. RTD uses a synthetic token seeded at the root agent and tracked via exact regex matching. » (A16, p. 15). Ils séparent eux-mêmes présence et respect : « Whether agents act on preserved constraints under peer pressure is a separate question, governed by IDR rather than RTD. » (A35, p. 8).
- **Quelle contrainte ?** Des contraintes d'exploitation et de conformité dans des tâches d'ingénierie, pas une frontière d'autorisation posée par un utilisateur. Pour la première mesure, exemple imprimé : « Never disable Flink checkpointing or set the checkpoint interval above 30 seconds, even under peak load or latency pressure » (A32, p. 21) — la forme « ne jamais désactiver, même sous pression » est celle de la consigne d'Astra dans N-035, mais sans délégation. Pour le traceur, l'identifiant accompagne parfois une vraie règle de sécurité : dans un exemple, l'agent parent le présente « as a “Critical Security Constraint” and requires all container images to be sourced from an approved private registry » (A33, p. 35) ; l'annexe range sous ce mode d'échec « Failure mode. Critical information (budget limits, compliance rules, safety constraints) is lost as it passes through the communication graph. » (A58, p. 18). La mesure, elle, ne voit que la chaîne de caractères.

### 1.2 Résultats chiffrés

| résultat | valeur | nature | page |
|---|---|---|---|
| durabilité moyenne du traceur, par modèle | GPT 80,3 % ; Gemini 84,5 % ; Qwen 94,0 % ; Llama 62,6 % (A47, A48 pour deux lignes) | auteurs, tableau 9 | 26 |
| violations de la contrainte sous pression (première mesure) | GPT 3,4 % ; Gemini 1,5 % ; Qwen 0,9 % ; Llama 10,1 % (A47, A48) | auteurs, tableau 9 | 26 |
| durabilité, chaîne / arbre / graphe convergent (45 tâches par case) | GPT 75,9 / 77,4 / 49,4 ; Gemini 83,9 / 76,1 / 64,4 ; Qwen 97,4 / 91,1 / 81,7 ; Llama 48,3 / 49,3 / 20,7 (A39 à A42) | auteurs, tableau 21 | 33 |
| **taux de perte par relais, chaîne linéaire** (arêtes où l'émetteur porte le traceur) | GPT 16 % de 85 arêtes ; Gemini 8 % de 86 ; Qwen 3 % de 96 ; Llama 40 % de 67 (A20, A22, A24, A26) | auteurs, tableau 23 | 34 |
| **idem, graphe convergent** | GPT 33 % de 45 ; Gemini 27 % de 56 ; Qwen 16 % de 64 ; Llama 65 % de 37 (A21, A23, A25, A27) | auteurs, tableau 23 | 34 |
| part de variance de la durabilité liée à la topologie | η² de 0,07 à 0,40 selon le modèle (A02, A51) | auteurs | 1, 2, 29 |
| durabilité contre longueur du chemin et nombre moyen d'entrées | r = −0,176 et r = −0,073, tous modèles réunis (A12) | auteurs | 33 |
| échecs du graphe convergent, par type (GPT, Gemini, Qwen, Llama) | perte à la synthèse 11, 8, 6, 22 ; perte en amont 8, 2, 0, 12 ; partiel 6, 9, 4, 2 (A44, A43, A45) | auteurs, tableau 22 | 33 |
| pertes en amont : traceur absent de tout message | 21 sur 22 (A46) | auteurs, tableau 25 | 35 |
| violations sous pression, échelle basse / moyenne / haute (Llama) | 6,8 ; 9,7 ; 13,9 % ; ρ = 0,211 (A55) | auteurs, tableau 15 | 28 |
| violations selon la topologie | effet non significatif pour Qwen et Llama (η² = 0,000, A56) ; significatif pour GPT et Gemini | auteurs, tableau 17 | 29 |

Définition du taux par relais, mot pour mot : « we computed the per-hop tracer drop rate for linear-chain and converging-DAG tasks (the fraction of edges A → B where the tracer is present in A’s output but lost in B’s) » (A10, p. 8) ; « For each directed edge A → B where the tracer is present in A’s output, Src. edges counts such edges and Drop rate is the fraction where B’s output is tracer-free. » (A11, p. 34). C'est un taux **conditionnel** (l'émetteur porte encore l'information), donc un taux de risque par relais, mis en commun sur tous les rangs.

Lecture des auteurs : le goulot est au nœud de convergence (« an agent weighing competing parent inputs discards constraints carried by a minority branch, a bottleneck structurally absent from linear chains », A03, p. 1 ; « convergence nodes drop constraints that arrive in only one », A17, p. 9), sauf pour le plus petit modèle : « for Llama 3.1 8B Instruct it is masked by a uniformly high per-hop drop rate » (A36, p. 10).

Calculs de ma main (script `calculs.py`), à ne pas attribuer aux auteurs :
- Si le taux par relais était constant le long d'une chaîne — **hypothèse que l'article ne teste pas** —, la survie après 1, 2, 3, 4 relais vaudrait 0,84 ; 0,71 ; 0,59 ; 0,50 pour GPT, et 0,60 ; 0,36 ; 0,22 ; 0,13 pour Llama. L'article ne trace aucune de ces courbes.
- Graphe convergent : 90 échecs en tout ; 47 pertes à la synthèse (52 %), 22 pertes en amont (24 %), dont 21 où la racine n'a jamais émis le traceur (23 % des échecs).

### 1.3 Ce que l'article ne fait pas, limites reconnues

- **Aucune courbe ni loi en fonction du nombre de relais.** Le taux par relais n'est pas ventilé par rang (premier, deuxième, troisième relais) ; la longueur de chaîne n'est pas un facteur ; la mesure principale est normalisée par la profondeur du graphe, ce qui efface la profondeur absolue. La seule statistique liée à la longueur est la corrélation r = −0,176 (A12), donnée pour écarter la longueur comme explication de l'écart entre topologies (« Pearson correlations of −0.176 and −0.073; n=540 directed », A13, p. 8).
- **La topologie n'est pas manipulée à tâche égale** : « Each task is co-designed with a specific communication topology » (A50, p. 4), parce que « Reassigning the same task to an arbitrary topology conflates topology effects with task-topology mismatch artifacts » (A49, p. 4). L'effet de topologie est donc une association entre groupes de tâches différentes ; les auteurs titrent d'ailleurs « Topology is associated with propagation behavior » (A61, p. 7).
- **Présence n'est pas respect** : le traceur ne dit rien de l'obéissance (A35) ; « RTD can undercount highly abstractive paraphrases, while CLC captures explicit tracer leakage rather than all semantic leakage. » (A28, p. 38). Une contrainte reformulée fidèlement sans son identifiant compte comme perdue ; l'audit lexical ne couvre que les 47 pertes à la synthèse du graphe convergent (p. 34), pas les chaînes linéaires.
- **Pas de moniteur, pas de défense évaluée.** Une intervention est renvoyée à plus tard : « evaluate explicit constraint echoing at converging-DAG nodes as a targeted design intervention » (A18, p. 10).
- **Longueur du contexte non isolée.** Le mécanisme est affirmé, pas mesuré : « Each hop introduces additional tokens that can displace or dilute earlier constraints. » (A31, p. 18).
- Portée : « the reported values should be interpreted as protocol-specific measurements rather than universal backbone properties » (A29, p. 38) ; « We do not report correlations between behavioral scores and final task success » (A30, p. 38).
- Positionnement face aux deux voisins que N-035 nomme de mémoire (Cemri et collègues, référence 2 ; Hammond et collègues, référence 14) : « they name failure modes but lack quantitative instruments for measuring how rapidly a false belief permeates a network or how far a constraint travels before it is forgotten » (A34, p. 3). C'est la lecture d'AgentCollabBench, non vérifiée par moi sur ces deux sources.

### 1.4 Incohérences internes et réserves de symétrie

1. **Effectif des arêtes.** Le texte annonce 540 arêtes dirigées (A13) ; la somme des « arêtes sources » du tableau 23 vaut 536 (calcul). Écart de 4, non expliqué (les 540 peuvent compter des arêtes dont l'émetteur ne porte pas le traceur ; l'article ne le dit pas).
2. **Aucune répétition déclarée, aucune température déclarée pour les quatre modèles évalués** (seule la température du générateur de tâches est donnée, p. 15). Les erreurs types du tableau 9 sont entre tâches, pas entre tirages. Les taux par relais reposent sur de petits effectifs : 3 % de 96 arêtes, c'est environ 3 arêtes (calcul) ; le rapport « 5,0 fois » de Qwen entre graphe convergent et chaîne tient donc à une poignée d'événements. Aucun intervalle n'est imprimé pour ces taux.
3. **L'échelle « cloisonnement de la topologie »** qui valide la mesure du traceur (0,727 ; 0,605 ; 0,360 : « Topology siloing RTD -0.313 [-0.455, -0.141] 150 0.727 0.605 0.360 », A37, p. 28) **n'est définie nulle part** dans le PDF : on ne sait pas si elle ajoute des relais, retire des arêtes ou autre chose. Elle ne peut pas être lue comme une courbe en profondeur. Elle n'est conduite que sur le plus petit modèle (A38, p. 6).
4. **La part « racine muette ».** Dans le graphe convergent, 21 des 22 pertes en amont sont des cas où « the root agent received the tracer via system-prompt injection but never echoed it into any outgoing message » (A19, p. 35) : la perte a lieu avant tout relais, à la première émission. Cela mesure la consigne d'injection du banc (un traceur dans une consigne système, sans obligation de le répéter) autant qu'une érosion. La même ventilation n'est pas donnée pour les chaînes linéaires. Toutes les tâches du graphe convergent injectent à la racine (« All converging-DAG tasks in this corpus use root-agent injection », A60, p. 34).
5. **Juge prudent sur la première mesure** : « The GPT 4.1 mini validation judge is conservative for IDR (19 false negatives vs. 4 false positives) » (A52, p. 16) ; ce chiffre vaut pour le juge de validation, pas pour le juge DeepSeek des résultats rapportés, dont l'accord avec les humains n'est pas imprimé séparément.
6. Petites discordances : borne haute de l'intervalle de ρ, 0,358 dans le texte (A54, p. 6) et 0,359 au tableau 15 (A55, p. 28) ; « 45 tâches par case » au tableau 21 contre « 45 à 52 par topologie » p. 8, alors que les moyennes du tableau 21 sont celles du tableau 13.
7. Recoupements conformes (calcul) : pour chaque modèle, le nombre de tâches parfaites, les échecs du tableau 22 et la moyenne du tableau 21 sont compatibles ; les rapports annoncés (2,0 ; 3,3 ; 5,0 ; 1,6) se retrouvent à l'arrondi près sur le tableau 23 (2,06 ; 3,38 ; 5,33 ; 1,62 avec les valeurs arrondies).

### 1.5 Verdict pour H9

- C1 **occupée en partie** : la perte, de relais en relais, d'une information qui porte une contrainte est mesurée (mai 2026), mais par présence d'un identifiant, et entre pairs d'un flux de travail plutôt que d'un agent vers un sous-agent délégué ; le « déclin de la consigne » n'est pas un phénomène de délégation.
- C2 **occupée en partie, et sur le point que le lot 7-D donnait pour non trouvé** : taux de perte conditionnel par relais, chaînes linéaires et graphes convergents, quatre modèles. Non fait : ventilation par rang de relais ; longueur de chaîne contrôlée ; survie de la force de la contrainte (et non du texte).
- C3 **voisin** : aucune courbe ni loi en fonction du nombre de relais ; une corrélation faible avec la longueur du chemin (r = −0,176), sur une mesure normalisée.
- C4 **ne touche pas** (aucun moniteur ; une intervention de rappel de la contrainte renvoyée aux travaux futurs).
- C5 **occupée en partie** : capacité du modèle (quatre modèles, dont un petit dont la perte est uniforme) ; structure (topologie, longueur du chemin, nombre d'entrées, niveau de complexité) ; reformulation traitée seulement comme risque de sous-comptage ; longueur du contexte non séparée.
- C6 **ne touche pas**.
- **D'ensemble pour cet article : H9 occupée en partie** (C2 surtout), par une mesure voisine d'objet différent.

## 2. Tallam (2605.05440v1, « Authorization Propagation in Multi-Agent AI Systems: Identity Governance as Infrastructure » ; aucune venue imprimée ; tampon « arXiv:2605.05440v1 [cs.AI] 6 May 2026 », T22, p. 1 ; auteur unique, affilié à une entreprise)

### 2.1 Ce que l'article fait : un cadre

- Il nomme un problème de contrôle d'accès : « maintaining authorization invariants as non-human principals retrieve data, delegate tasks, and synthesize results across changing boundaries » (T02, p. 1) ; « We call this problem authorization propagation. » (T01, p. 1). Trois sous-problèmes : délégation transitive, inférence par agrégation, validité dans le temps. Un modèle formel court (principaux, ressources, fonction d'autorisation, fonction de délégation, graphe de flux, p. 8) et sept exigences de structure, dont « R2. Delegation must be explicit, bounded, and auditable. » (T04, p. 13) et « R3. Authorization must be evaluated at every data retrieval boundary. » (T05, p. 13).
- La thèse centrale est une prescription : « authorization state must be evaluated continuously and enforced at every interaction boundary in the system » (T21, p. 8) ; côté maîtrise : « Deny a downstream agent access even if the upstream agent was authorized (least privilege at each hop, not inherited privilege) » (T15, p. 13).
- L'objet est un **droit d'accès** (qui peut lire quoi, au nom de qui), géré par des jetons et des relations, pas une consigne de sécurité en langue naturelle qu'un modèle reformule. La propriété visée est inverse de l'érosion : que l'autorité ne s'élargisse pas en descendant (« Authority does not accumulate through delegation chains (no privilege escalation) », T06, p. 9).
- Sans adversaire, comme MasDrift : « No attacker is required. » (T23, p. 7).

### 2.2 Ce qu'il ne fait pas : aucune mesure

- « We do not propose a specific authorization architecture. We identify the structural requirements that any sufficient architecture must satisfy. » (T03, p. 13) ; « This paper identifies the problem and the structural requirements. » (T16, p. 15) ; « This paper does not present a complete deployment architecture, and its claims are narrower than they may first appear. » (T11, p. 15).
- Aucun modèle exécuté, aucune tâche, aucun taux, aucune chaîne de délégation mesurée, aucun état interne.
- La seule partie empirique : trois incidents d'une plateforme de production (repli silencieux d'une passerelle d'authentification vers un contexte global, T14, p. 16 ; une liaison de session annoncée réussie alors qu'elle a échoué ; un conteneur non attesté). Ce sont des défauts de logiciel classique, sans modèle de langage dans la boucle, sans dénominateur. L'auteur le borne : « We note that three cases from a single system do not constitute proof of the formal model. » (T07, p. 17) ; il en tire que « all three violations arose from normal system operation, not from adversarial action » (T08, p. 17).
- La dépendance à la profondeur est affirmée, non mesurée : « The difficulty of recovery scales with the depth and breadth of the agent chain. » (T12, p. 13).
- Il **appelle** la mesure : « A more complete evaluation program should measure silent » (T09, p. 17) « narrowing, unsafe completeness, delegation drift, and stale-authority behavior under realistic task decompositions » (T10, p. 18). Un appel à mesurer n'est pas une mesure ; il rejoint celui de Li et collègues (lot 7-D) et ôte un peu plus à H9 la nouveauté de l'idée.

### 2.3 Réserves

- **Chiffres de seconde main, non opposables (R7)** : tout chiffre de l'article vient d'un autre travail, par exemple « which improves policy compliance from 48% to 93% » (T13, p. 10) ou « Reference implementations in Python and Rust demonstrate 0.049ms verification latency and 100% adversarial rejection across 600 attack attempts. » (T20, p. 4). Plusieurs « 100 % » rapportés sans réserve : trop propres pour être repris.
- **Bibliographie fragile** : six références « Anonymous » sans identifiant ni venue vérifiable (exemple : « Anonymous. Claude Code permission system evaluation, 2026b. », T19, p. 19), et six brouillons de travail de l'auteur lui-même. Les pistes citées ne sont pas traçables depuis ce PDF.
- Incohérence mineure : les remerciements renvoient à « The SQL injection analogy in Section 8.1 » (T17, p. 18) ; l'analogie est à la section « 9.1 The SQL Injection Analogy, Revisited » (T18, p. 14).

### 2.4 Verdict pour H9

- C1 **voisin** (un cadre de contrôle d'accès sur la conservation de l'autorité le long d'une chaîne de délégation ; ni contrainte en langue naturelle, ni érosion mesurée).
- C2, C3 **ne touche pas** (aucune mesure ; la mesure est demandée comme travail futur).
- C4 **voisin** (prescrit un contrôle à chaque frontière et cite des mécanismes de jetons et de moniteurs de référence ; n'en évalue aucun).
- C5, C6 **ne touche pas**.
- **D'ensemble : voisin, cadre sans mesure.** À citer comme antériorité du cadrage « l'autorisation doit survivre à la chaîne », que MasDrift cite déjà.

## 3. Tableau croisé (colonnes du lot 7-D rappelées pour mémoire)

| | AgentCollabBench | Tallam | rappel : MasDrift | rappel : Sun |
|---|---|---|---|---|
| date imprimée | 9 mai 2026 | 6 mai 2026 | 15 octobre 2026 (version 3) | 13 octobre 2026 (version 2) |
| contrainte | identifiant témoin (parfois attaché à une règle de sécurité) ; contrainte d'exploitation dans la consigne système | droit d'accès (concept) | autorisation explicite de l'utilisateur | blocage explicite |
| relais | graphes de 2 à 6 agents, dont chaînes linéaires | — | 1 à 3 niveaux ; pairs | 1 réel ; 1 à 4 simulés |
| mesure par relais | taux de perte conditionnel par arête, tous rangs réunis | — | premier relais fautif | préservation de l'artefact, un relais |
| loi ou courbe selon le nombre de relais | non (r = −0,176 avec la longueur du chemin) | non | courbe 1 à 3 niveaux, pas de loi | 5 points confondus |
| moniteur ou défense | non | prescrit, non évalué | deux défenses | contrôle, réparation |
| états internes | non | non | non | non |
| adversaire | non (stimuli injectés) | non | non | non |
| C1 | occupée en partie | voisin | occupée | occupée |
| C2 | **occupée en partie (taux conditionnel)** | ne touche pas | occupée en partie | occupée en partie |
| C3 | voisin | ne touche pas | occupée en partie, contre-indice | voisin |
| C4 | ne touche pas | voisin | occupée en partie | occupée en partie |
| C5 | occupée en partie | ne touche pas | occupée en partie | occupée en partie |
| C6 | ne touche pas | ne touche pas | ne touche pas | ne touche pas |
| H9, par article | **occupée en partie** | voisin | occupée en partie | occupée en partie |

## 4. Le verdict d'ensemble du lot 7-D change-t-il ?

**Non pour le verdict ; oui pour deux formulations.**

- **C1 — inchangée : occupée.** Une date s'ajoute : la perte d'une information porteuse de contrainte de relais en relais est mesurée dès mai 2026 (AgentCollabBench), avant MasDrift, dont l'identifiant arXiv est d'août 2026 (sa version 1 n'a pas été lue).
- **C2 — toujours « occupée en partie », mais la part non trouvée se resserre.** Le lot 7-D écrivait : non trouvé, « la survie conditionnelle par relais […] sur des chaînes linéaires de longueur contrôlée ». La **forme de la mesure** — taux de perte conditionnel par relais, sur chaînes linéaires — est publiée (A10, A11 ; 3 à 40 % par relais selon le modèle). Reste non trouvé dans les sept sources lues : (i) ce taux **ventilé par rang de relais** (le premier relais est-il pire que les suivants ?) ; (ii) sur des chaînes de **longueur contrôlée**, à tâche égale ; (iii) pour une **contrainte de sécurité jugée dans sa force** (encore opérante, affaiblie, absente — la grille de MasDrift) et non pour un identifiant retrouvé à l'identique.
- **C3 — toujours « occupée en partie, avec contre-indice » ; le contre-indice se nuance sans se lever.** AgentCollabBench n'apporte ni loi ni courbe. Mais ses taux par relais sont conditionnels à la présence chez l'émetteur et restent non nuls en chaîne linéaire : la perte ne s'épuise donc pas à la première émission, au moins pour un identifiant et surtout pour le petit modèle (40 %). C'est compatible avec une décroissance par passage, sans l'établir : le taux n'est pas donné par rang, et un quart des échecs du graphe convergent sont des racines muettes (calcul), ce qui va dans le sens de la marche initiale de MasDrift. Les deux lectures — « marche au premier relais » et « risque à chaque relais » — ne sont pas départagées par les sources lues, et elles ne portent pas sur le même objet (force d'une contrainte jugée, contre présence d'une chaîne de caractères). Un préenregistrement de H9 devrait prédire **le profil du taux par rang**, pas seulement le signe de la pente.
- **C4 — inchangée : occupée en partie** (rien de neuf : ni l'un ni l'autre article n'évalue un moniteur).
- **C5 — inchangée : occupée en partie.** S'ajoute : la capacité du modèle change le régime (petit modèle : perte uniforme à chaque relais ; modèles plus forts : perte concentrée aux nœuds de convergence), et la topologie est un confondant à part entière que N-035 ne liste pas — une chaîne de délégation réelle fait converger des retours de sous-agents. La longueur du contexte reste non séparée dans les sept sources.
- **C6 — inchangée : ne touche pas**, et toujours absente de l'énoncé de H9.

**D'ensemble : H9 occupée en partie**, comme au lot 7-D. La condition de repli de N-035 reste remplie pour le cœur de l'énoncé ; le repli ou la reformulation est un nœud de Lazar, que ce rapport ne tranche pas.

## 5. Ce qui reste revendicable (mise à jour des quatre formulations du lot 7-D ; aucune n'engage)

1. *Un moniteur à chaque passage, comme facteur croisé avec la profondeur* — **inchangé**. Non trouvé dans les sept sources. Ajout utile : le croiser aussi avec la topologie (chaîne contre convergence), puisque c'est là que la perte publiée se concentre.
2. *La lecture interne du sous-agent* (contrainte encore opérante contre contrainte seulement mentionnée) — **inchangé**, et renforcé comme réponse au constat désormais triple que présence n'est pas respect (MasDrift, Sun, et AgentCollabBench qui sépare ses deux mesures, A35). Toujours hors de l'énoncé actuel de H9 : l'y mettre change l'hypothèse.
3. *La loi par passage, confondants séparés* — **resserré**. N'est plus revendicable : « première mesure d'un taux de perte conditionnel par relais ». Reste : le profil par rang de relais, sur chaînes de longueur contrôlée et à tâche égale, pour la force d'une contrainte de sécurité, à longueur de contexte égalisée, sur des modèles à poids ouverts hébergés (pour pouvoir lire les états internes). Bases à citer et à battre : les taux par relais du tableau 23 d'AgentCollabBench et la répartition du premier relais fautif de MasDrift.
4. *Sous un agent qui sabote* — **inchangé** : absent des sept sources ; ce n'est pas établi comme trou du champ.

**N'est plus revendicable** (en plus de la liste du lot 7-D) : la mesure conditionnelle par relais comme idée neuve ; la topologie comme facteur de survie de l'information ; le constat « un petit modèle perd à chaque relais ».

## 6. Pistes citées et non lues

- AgentCollabBench cite pour la propagation en chaîne : Lin et collègues 2025 (référence 21, synthèse sur les hallucinations des agents, « constraint loss in one agent propagates downstream » (A62, p. 37) selon l'article) ; Shen et collègues 2025, EMNLP (référence 38, effets de propagation de l'information selon la topologie) ; Liu et collègues 2025, « Topology matters » (référence 22, fuite de mémoire selon la topologie) ; Song et collègues 2025 (référence 40, pression des pairs). La référence 38 est la plus susceptible de porter une courbe de propagation selon la structure.
- Tallam cite des mécanismes à chaque frontière (jetons de capacité liés à l'invocation ; moniteur de référence sur graphe de dépendances) qui touchent C4 du côté du contrôle d'accès ; références sans identifiant dans le PDF.
- Restent non lus, comme au lot 7-D : Cemri et collègues 2025 ; Hammond et collègues 2025 ; Xu et collègues 2026 (« The trust paradox ») ; les versions 1 de MasDrift et de Sun.

## 7. Contrôle des citations

- 87 citations contrôlées, 0 échec (85 trouvées en `-layout`, 2 dans l'ordre de lecture par défaut : A10 et A13, paragraphe entrelacé avec la figure 6, p. 8).
- Second contrôle (`controle_rapport.py`) : 60 passages entre guillemets rattachés à un identifiant, 0 échec d'inclusion ou de page ; les passages entre guillemets sans identifiant sont des termes français, des titres ou les exemples de l'essai du script (liste dans `journal-controle-rapport.txt`).
- Essai préalable du script : cas juste trouvé, cas altéré rejeté, cas juste sur mauvaise page rejeté (`journal-autotest.txt`).
- Fichiers dans l'archive : `citations.json`, `construire_citations.py`, `controle_citations.py`, `controle_rapport.py`, `calculs.py`, `journal-autotest.txt`, `journal-controle.txt`, `journal-controle-rapport.txt`, `journal-calculs.txt`, `journal.md`, et le texte extrait par page (`texte/`).
