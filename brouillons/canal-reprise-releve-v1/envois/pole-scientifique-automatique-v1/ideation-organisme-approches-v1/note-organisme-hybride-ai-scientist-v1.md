# Organisme hybride avec un cadre « AI scientist » existant : inventaire, architecture, protocole de comparaison, devis — note de conception avec recommandation (v1)

Lignée conv-audit (sous-agent neuf, modèle Claude Fable 5.1), 29 octobre 2026, relevé `date -u` **11:44 UTC** (début de rédaction ; heure de fin au pied). Mot de Lazar
(29 octobre, 12:33 heure de Paris) : « on peut aussi créer en parallèle un organisme hybride intégrant un AI scientist existant qui propose et expérimente et teste, en
plus du nôtre, et on compare les deux ; les expériences sur carte restent sur devis et GO : go ». Ce « go » fixe le **principe** (un hybride en parallèle, comparé au
nôtre) ; la note propose **comment** : quel cadre, quelle entrée dans le pôle, quel protocole, quel devis. **Proposer avec recommandation** ; défaut sous 48 heures en § 5.

**Déclaration de méthode.** Processeur seul ; aucune session réelle, aucune dépense, aucune commande `git`, aucun fichier existant modifié, rien de scellé ; aucune lecture
de `donnees/`, des traces, du bras d'attaque, du mode tenu à l'écart ni des consignes de P3 ; niveau méthode (aucun contenu d'attaque). L'inventaire vient de **pages web
secondaires** (fiches de projets, billets, résumés) et de deux README lus par le relais de lecture ; les dépôts GitHub et les PDF arXiv n'étaient **pas accessibles** depuis
ce bac à sable (liste blanche du relais) : tout chiffre ci-dessous est **RAPPORTÉ par une page**, jamais vérifié sur PDF empreinté (R7), donc non opposable ; ce qui n'est
dit par aucune page est marqué SUPPOSÉ.

**Fichiers lus (sha256, douze premiers caractères)** : `conception-pole-scientifique-v1.md` `a4f94148c9c5` ; `orchestrateur-pole-v7/LISEZMOI-orchestrateur-pole-v7-v46.md`
`3c9c1527f81d` ; `note-tour-c-outils-clotures-v1.md` `ad33007204aa` ; `question-mere-course-v1/question-course-2-fusion-v0.md` `97cf7306b0f1` ;
`integration-proposeurs-ia-v1.md` `974b2dbe17b7` (§ 1, 3, 6, 7 : N-053, prises, quarantaine) ; `registres/decisions.md` `e0e968e99b79` (lignes R-338, R-366, R-369,
R-370, R-448 : N-053 points 4 et 5, mesures jamais servies aux juges) ; `pole/relais_reel.py` `1b90b020287e` et `pole/relais.py` `b5a76343e458` (en-tête, `variables_agent`,
chemins permis) ; `CLAUDE.md` `a2aabda8a181`.

## Verdict

Recommandation : **(c) — les deux, (b) d'abord** : donner à notre organisme sa boucle d'exécution légère (fiche gelée → script → exécution sur processeur sur la tranche
exploratoire scellée → éliminée ou survivante au seuil gelé), **en empruntant la forme de la boucle « garde ou reviens en arrière » d'`autoresearch`** ; en parallèle,
préparer l'**hybride (a) avec Agentic Scientist v3 (Sakana, Apache-2.0, agent Claude Code par défaut)** sous notre bac à sable, relié au relais, et le comparer à notre
organisme par le protocole préenregistré du § 3 à partir de la **course 3**. Confiance **0,6**. Deux constats fondent l'ordre : (1) le relais ne parle que l'interface
`/v1/messages` d'Anthropic (`relais_reel.py`, `CHEMINS_PERMIS`), ce qui élimine d'emblée tous les cadres qui n'appellent Claude que par OpenAI, Bedrock ou Gemini ; (2) une
comparaison « hybride contre organisme » n'a de sens que si **les deux exécutent** : sans (b), elle mesurerait « avoir un exécuteur », pas « le cadre ».

## 1. Inventaire des cadres « AI scientist » ouverts

Critère d'entrée : le cadre **propose, code, exécute, teste et écrit** (au moins quatre des cinq). Contrainte d'installabilité chez nous : réseau **par le relais seulement**
(`ANTHROPIC_BASE_URL` vers le relais local, jeton factice à la place de la clé, `relais.variables_agent`), donc le cadre doit appeler Claude par l'interface Messages
d'Anthropic ou par Claude Code ; aucune clé chez l'agent ; processeur seul (carte sur GO) ; aucun service tiers obligatoire (Modal, Semantic Scholar, arXiv en direct).

| cadre | auteurs, organisation, année | licence | modèles appelés | ce qu'il exécute, matériel | garde-fous propres | résultats publiés | statut |
|---|---|---|---|---|---|---|---|
| **Agentic Scientist v3** (« AI-Scientist-v3 ») | Sakana AI, 15 octobre 2026, arXiv 2610.18933 | Apache-2.0 | enveloppe des **agents de code** : `claude` (défaut), `codex`, `cursor`, `opencode`, `gemini`, `pi` ; modèles cités : Claude Opus, GPT, DeepSeek, Kimi | six phases, chacune dans **son conteneur Docker** sur un instantané local ; agents à **« full tool permissions »** (mode « yolo ») ; exemple **processeur seul** (`examples/circpack`) ; tâches d'entraînement (GRPO, Brax) sur carte | rédaction de tâche → évaluateur et grille, puis **« seals the evaluation assets »** ; évaluation finale rescorée dans un environnement scellé ; lignes de base et ablations automatiques ; avertissement du README : conteneurs, identifiants au strict nécessaire, injections possibles par les fichiers de tâche ou les papiers | papier ALIFE 2026 (oral) co-découvert, avec forte édition humaine ; 70 campagnes sur 5 tâches ; corrélation 0,44 entre performance et notes de relecteurs ; un raccourci trouvé par un agent sur une grille implicite | vu sur pages (runtimewire, explainx, alphasignal) ; README non lu : SUPPOSÉ pour les détails Docker |
| **The AI Scientist-v2** | Sakana AI, 2025, arXiv 2504.08066 ; Nature, 2 octobre 2026 (« Towards end-to-end automation of AI research ») | « AI Scientist Source Code License » (dérivée RAIL, obligation de divulguer l'usage de l'IA) | OpenAI (o1, o3-mini, gpt-4o), Gemini via interface OpenAI, **Claude via AWS Bedrock seulement** ; Semantic Scholar facultatif | idéation, **recherche arborescente** d'expériences, rédaction, relecture ; **Linux avec carte NVIDIA et CUDA exigés** | avertissement « This codebase will execute LLM-written code », conteneur recommandé ; relecteur automatique (précision équilibrée 69 %, RAPPORTÉ) | papier d'atelier accepté ICLR 2025 (notes 6, 7, 6), retiré par engagement ; ≈ 15 à 20 USD par run d'expériences, ≈ 5 USD de rédaction (README) | README vu ; **non installable** chez nous (carte exigée, Claude par Bedrock) |
| **Agent Laboratory** | S. Schmidgall et al., 2025, arXiv 2501.04227 (EMNLP Findings) | MIT | **OpenAI et DeepSeek seulement** (o1, gpt-4o, o3-mini, deepseek-chat) | revue de littérature (arXiv, HuggingFace), expérimentation (`mlesolver.py`, Python local), rédaction LaTeX ; processeur possible | aucun avertissement de sécurité ; mode copilote | rapports ; aucun coût chiffré | README vu ; **non installable sans adaptateur** de modèle (pas d'Anthropic) et sans couper la revue en ligne |
| **AI-Researcher** | HKUDS (Université de Hong Kong), 2025, arXiv 2505.18705 | **aucune licence déclarée** (tous droits réservés par défaut) | Claude, OpenAI, DeepSeek, Gemini, Groq… | cycle complet ; image Docker ; « multiple GPUs are recommended » | aucun décrit | suite de bancs ; ≈ 5 850 étoiles | fiche vue ; **exclu** (licence absente, cartes) |
| **Denario** | AstroPilot-AI (Villanueva-Domingo, Villaescusa-Navarro, Bolliet), 1.0.1 du 4 novembre 2025, arXiv 2510.26887 | GPLv3 | non précisé sur la page (agents AG2 et LangGraph, dorsal `cmbagent`) : Anthropic par LangChain **SUPPOSÉ** | idée, méthode, calculs et figures (`get_results`), papier LaTeX ; Docker optionnel ; processeur plausible | aucun décrit | un papier entièrement généré accepté à « Open Conference of AI Agents for Science 2025 » | fiche PyPI vue ; installable **sous réserve** (routage du modèle à vérifier) |
| **AIDE** | WecoAI (Jiang, Schmidt et al.), 2024-2025, arXiv 2502.13138 | MIT | OpenAI, **Anthropic**, Gemini, tout modèle local « qui parle l'interface OpenAI » ; modèle de retour par défaut gpt-4o (à changer) | **arbre de scripts Python** exécutés localement, métrique définie par l'utilisateur, 20 pas par défaut ; Docker optionnel ; processeur | aucun bac à sable ; clé passée en clair dans l'exemple Docker | 4 × plus de médailles que le meilleur agent linéaire sur MLE-Bench (RAPPORTÉ) | README vu ; **installable** (petit code) ; c'est un exécuteur, pas un proposeur d'hypothèses |
| **Curie** | P. T. J. Kon et al., 2025, arXiv 2502.16069 | Apache-2.0 | clés de fournisseurs (liste non vue) | génère et exécute le code d'expériences ; Docker recommandé ; modules de rigueur intra-agent, inter-agent, connaissance d'expérience | modules de vérification « procedural reliability and reproducibility » | banc de 46 questions (SUPPOSÉ, non vu) ; 370 étoiles, dernier commit septembre 2025 | fiche vue ; installable **sous réserve** (modèles non vus) |
| **CodeScientist** | P. Jansen, Ai2, 31 mars 2025, arXiv 2503.22708 | Apache-2.0 | OpenAI, Anthropic | code Python dans des **conteneurs Modal.com** (service externe obligatoire) ; bibliothèque de blocs de code vérifiés | environnement contrôlé ; relecture humaine exigée | ≈ 50 expériences, 19 découvertes candidates, 6 validées par experts | page vue ; **non installable** (Modal = réseau hors relais) |
| **DeepScientist** | Weng et al., Westlake University, 30 septembre 2025, arXiv 2509.26603 (ICLR 2026) | MIT « avec addenda » ; module « Analyze & Report » **non publié** | Gemini 2.5 Pro (cœur), Claude Opus 4 par Claude Code (code) | optimisation bayésienne sur des idées, Claude Code exécute ; ≈ 5 000 idées, ≈ 1 100 validées, > 20 000 heures de carte, ≈ 100 000 USD | supervision humaine exigée ; le module de rapport est retenu pour éviter des papiers crédibles non vérifiés | +183,7 %, +1,9 %, +7,9 % sur trois tâches (auto-rapporté) | page vue ; **exclu** (échelle, Gemini au cœur, code partiel) |
| **autoresearch** | A. Karpathy, 7-8 mars 2026 | MIT | agent de code au choix (non précisé par la page ; Claude Code SUPPOSÉ) | script de ≈ 630 lignes : l'agent lit `train.py`, le modifie, lance un run **à budget fixe (≈ 5 minutes sur une carte)**, lit `val_bpb`, **garde ou revient en arrière**, recommence ; tourne aussi sur processeur (un run sur Mac Mini : 26 échecs sur 35) | budget fixe, retour arrière ; aucune garde contre la contamination du jeu de validation (soulevée par un utilisateur) | 126 expériences en une nuit (0,9979 → 0,9697) ; ≈ 700 modifications en deux jours | page vue ; **installable** ; c'est la forme de boucle la plus simple à emprunter pour (b) |
| **data-to-paper** | Technion, Kishony lab, 2024, arXiv 2404.17605 (NEJM AI) | MIT | « especially GPT4 » (OpenAI) | code d'analyse de données local ; manuscrits « data-chained » : **chaque nombre remonte à la ligne de code** qui l'a produit ; autonome ou guidé | garde-fous remplaçant les paquets statistiques ; filigrane « AI-created » ; « NOT error-proof » | quatre cas d'étude | README vu ; non installable sans adaptateur de modèle ; sa **traçabilité nombre → code** est à emprunter (R6) |
| Kosmos | Edison Scientific, 5 novembre 2025, arXiv 2511.02824 | **service fermé** (plateforme) | non nommés | ≈ 200 déroulés, ≈ 42 000 lignes de code, ≈ 1 500 papiers par run de 12 heures | chaque affirmation citée ; 79,4 % d'affirmations exactes (102 évaluées) | rapports sur la plateforme | hors périmètre (fermé) ; réimplémentations non officielles : non évaluées |

**Réellement installables et exécutables sous notre bac à sable** (réseau par relais, Claude par `ANTHROPIC_BASE_URL`, processeur) : **Agentic Scientist v3** (par Claude
Code, dont notre kit est déjà l'enveloppe ; Docker à remplacer par notre bac à sable `bwrap` : SUPPOSÉ faisable, le cadre lançant lui-même `claude`), **AIDE** et
**autoresearch** (petits codes, exécution locale). Sous réserve : Denario, Curie. Exclus : AI-Scientist-v2, Agent Laboratory, AI-Researcher, CodeScientist, DeepScientist,
Kosmos, data-to-paper (pour les raisons de la colonne « statut »). Un papier de banc (Ravideshik et Kejriwal, arXiv 2607.28631) compare AI Scientist v1, v2,
CycleResearcher et data-to-paper sur **les mêmes 15 propositions** avec trois juges modèles : coût par papier 9 à 26 USD, 10 à 88 minutes ; à retenir comme antériorité du
protocole du § 3 et comme mise en garde (juges modèles divergents, référence commerciale prégénérée, aucun test formel).

## 2. Architecture de l'hybride : un cadre tiers entre dans le pôle sans toucher aux garanties

**Position.** Le cadre tiers est un **proposeur-expérimentateur enfichable** de plus, branché par l'`AdaptateurCommandeExterne` (consigne sur l'entrée standard, une ligne
JSON en sortie) comme Argon ; il n'est **jamais** orchestrateur, juge, vérificateur ni auteur de témoins. Le noyau v46 (dossier fermé, liste blanche, caviardage valeur par
valeur, plafonds, journal du crochet) reste le seul maître des entrées et des sorties.

**Mêmes entrées.** La question de la course 2 (texte I : axes 1 à 5 et 7 ; texte II exclu du premier hybride : la session « hypothèses fragiles » ne reçoit aucun cadre
qui exécute du code tant que la revue de sécurité du § 4 n'est pas passée), le même préambule, le même format de fiche à onze champs, le même index du dossier fermé
(copie vérifiée, empreintes, aucun PDF), les mêmes listes fermées, les mêmes plafonds en dollars, en demandes de lecture et en délai ; la moisson passe par **notre**
protocole (v47), jamais par la recherche en ligne du cadre.

**Ses expériences.** Le cadre ne touche aux données qu'au travers d'un **sas de gel** : avant toute exécution, il doit rendre une **fiche de test courte** (hypothèse,
prédiction chiffrée et signée, métrique, nul, seuil, plan d'analyse, liste d'arrêt) que le noyau scelle (R1) ; seulement alors le noyau copie dans son dossier la **tranche
exploratoire scellée** (scores et traits de P3 déjà payés, sorties des lentilles, simulateur figé ; jamais de textes, jamais `donnees/`). Exécution **sur processeur**
dans le bac à sable (aucun réseau, écriture dans le seul dossier de l'expérience, temps et mémoire bornés) ; toute expérience sur carte est une fiche de devis séparée,
**sur GO**. Chez Agentic Scientist v3, le sas se place entre sa phase « rédaction de tâche » (qui produit évaluateur et grille, puis les scelle) et ses phases
d'expérimentation : on garde son scellement, on y ajoute le nôtre, et son « évaluation finale scellée » est rejouée par **notre vérificateur** d'une autre lignée.

**Ses sorties.** Fiches, code, nombres, artefacts : scellés par le noyau à la sortie, empreintés, caviardés ; les fiches sont **traduites** dans le gabarit à onze champs
par un agent neuf d'une autre lignée (perte à la traduction mesurée, comme pour les proposeurs publiés, `integration-proposeurs-ia-v1.md` § 2), anonymisées, et lues par
**notre juge figé** en **une seule lecture**, mêlées aux fiches de notre organisme et aux témoins plantés (N-053 : jamais de sélection sur le verdict ; aucune note de juge
ni de surveillant ne revient au cadre, ni à aucun agent, ni à aucun entraînement). Les mesures de lecture et de coût vont au manifeste de fin seulement (R-448).

**Garde de sûreté.** Niveau méthode partout : aucun mode, aucune recette ; garde lexicale et quarantaine (lecture humaine avant tout bras rapporté, N-053 point 5) sur
les sorties du cadre comme sur les nôtres ; un cadre qui produit un contenu d'attaque est arrêté et sa sortie va en quarantaine sans lecture par la défense.

**Ce qui est retiré ou bridé dans le cadre** : (1) **auto-modification** : le cadre peut modifier *son* code d'expérience dans son dossier (c'est sa boucle), jamais son
orchestrateur, ni le sas, ni le noyau — copie du cadre réempreintée après chaque session, copie altérée = incident ; (2) **réseau** : aucun, hors le relais ; recherche
bibliographique, Semantic Scholar, arXiv, HuggingFace, suivi d'expériences (W&B) désactivés ou remplacés par la moisson du noyau ; (3) **exécution arbitraire** : le mode
« full tool permissions » est remplacé par notre crochet `PreToolUse` (outils de fichiers sur la racine de l'expérience, `Bash` dans `bwrap` sans réseau), ce qui suppose
d'injecter nos réglages dans le `claude` que le cadre lance (une enveloppe du binaire : code neuf, R5) ; (4) **écriture de papier** : gardée comme artefact local, scellée,
**jamais envoyée** (aucune soumission, aucun dépôt, aucune relecture automatique qui compte) ; (5) **relecteur ou juge interne** du cadre : retiré de toute sélection
(c'est la source d'inflation documentée : expérimentateur et relecteur de la même lignée) ; s'il reste comme signal d'affinage sur la partie de développement, il est
déclaré au manifeste comme variable de la comparaison.

## 3. Protocole de comparaison préenregistré : notre organisme contre l'hybride

**Mêmes entrées, mêmes plafonds** (§ 2) ; les deux bras tournent sur la même course, la même génération, le même dossier fermé, le même tirage de témoins ; l'ordre de
lecture des fiches par les juges est tiré au sort après scellement. Préenregistrement scellé avant toute lecture (R1), contre-lu par un sous-agent neuf (R2).

**Métriques gelées** (par bras et par course) : **M1** part de fiches éligibles (porte K1, K3, K4, K5 puis note max(avantage, originalité) ≥ 2, médiane des trois juges) ;
**M2** part des fiches éligibles dont la **prédiction chiffrée a été mise à l'épreuve de son test de mort** sur la tranche exploratoire (préenregistrement court scellé,
exécution par le bras, rejouée par un vérificateur neuf d'une autre lignée ; compte « survit / éliminée / indécise », jamais le signe ni l'ampleur comme mérite, R3) ;
**M3** part des antériorités citées vérifiées sur PDF empreinté, page citée (sous-agent neuf ; recherche adverse chez un autre fournisseur) ; **M4** coût par fiche éligible
(dollars du journal du relais, jetons, lectures de cache) ; **M5** temps mural par fiche et par course. Métrique de validité du lot : les témoins plantés (vrai, jumeau,
faux-antériorité, faux-falsifiabilité) ; un lot où un témoin « notable » n'est pas classé notable est **invalide** pour les deux bras (pas pour un seul).

**Verdict** par un sous-agent neuf (R13), ni auteur du préenregistrement, ni de l'analyse, ni d'aucun des deux bras, appliquant les règles gelées : « **l'hybride apporte** »
si, sur l'ensemble des courses, M2(hybride) − M2(organisme) ≥ +0,25 **et** M1 non inférieure de plus de 0,10 **et** M3 non inférieure de plus de 0,10 ; « **n'apporte
pas** » si M2 ≤ celle de l'organisme et M4 ≥ 1,5 × celle de l'organisme, ou si M1 ou M3 inférieure de plus de 0,25 ; « **non concluant** » sinon (défaut). Aucune
sélection sur le verdict : le verdict ne choisit ni les fiches qui passent en génération suivante (c'est la porte d'éligibilité, identique pour les deux bras) ni le bras
qui continue (c'est un nœud de Lazar) ; aucune métrique n'est servie aux juges.

**Taille et puissance** (calcul sur deux proportions, test bilatéral au seuil 0,05, puissance 0,8, SUPPOSÉ sur les tailles de fiches de la v46 : ≈ 8 fiches par bras et
par course). Une course (8 contre 8) ne détecte qu'un écart de proportion ≥ 0,5 : le verdict attendu est « non concluant ». **Trois courses** (≈ 24 fiches par bras)
détectent un écart ≈ 0,4 (0,5 contre 0,9 : ≈ 15 fiches par bras suffisent ; 0,5 contre 0,75 : ≈ 45 par bras, hors de portée). D'où : la comparaison est jouée sur
**trois courses au moins** (générations 1 à 3 de la course 2), métrique principale M2, M1 et M3 en garde, et le verdict n'est prononcé qu'au terme des trois ; un verdict
intermédiaire est interdit.

**Risques et parades.** *Contamination par un fournisseur* : le cadre tourne derrière notre relais vers Anthropic, le même fournisseur que nos agents ; s'il appelait un
autre fournisseur, nos pièces caviardées y partiraient (cas déjà tranché pour Argon, n° 119) ; aucune recherche en ligne : ce que le cadre « lit sur le web » est nul par
construction. *Fuite de pièces* : rien ne sort du bac à sable ; copie du dossier fermé réempreintée ; aucune écriture hors du dossier de l'expérience. *Juge qui reconnaît
le style* : traduction des fiches des deux bras dans le même gabarit par un agent tiers, en français, même longueur cible ; **épreuve d'anonymat** préenregistrée : un
agent neuf, sans accès aux juges, devine le bras de chaque fiche anonymisée ; s'il dépasse 0,7 d'exactitude, le lot est marqué « distinguable » et la comparaison
rapportée avec cette réserve (R4 : un écart trop net déclenche le même audit qu'un écart nul). *Comparaison asymétrique* : si notre organisme n'a pas d'exécuteur (b), M2 ne
mesure que l'existence d'un exécuteur ; d'où l'ordre (b) puis (a). *Cadre qui triche sur sa propre évaluation* (raccourci documenté chez Sakana, modification du code de
délai rapportée pour la v1 — SUPPOSÉ, non vérifié sur PDF) : la rejouée par un vérificateur d'une autre lignée et le gel avant lecture sont les seules parades ; un test
rejoué qui ne redonne pas le verdict compte « éliminée ».

## 4. Devis d'ordre de grandeur (SUPPOSÉ, à chiffrer par session-depot) et nœuds pour Lazar

- **Jetons.** Bras hybride par course : un proposeur de plus au barème Opus 5.5 (4 / 20 USD par million) sur la consigne de passe 1 (≈ 188 000 jetons) et ses tours
  d'outils avec cache : ≈ 2,5 à 7 USD par passe (note du tour (c), § 4 : × 2 à × 2,5 avec cache, × 20 sans) ; phases d'expérimentation du cadre (une dizaine de sessions
  Claude Code courtes par fiche de test, 8 fiches) : ≈ 15 à 40 USD par course (repère : 15 à 20 USD par run d'expériences chez AI-Scientist-v2, 26 USD par papier dans le
  banc 2607.28631, RAPPORTÉ) ; traducteur de fiches, vérificateur rejouant, épreuve d'anonymat, sous-agent de verdict : ≈ 5 à 15 USD ; juges : les 8 fiches de plus
  n'ajoutent que ≈ 10 000 jetons par juge. **Total hybride ≈ 30 à 70 USD par course**, trois courses ≈ 90 à 210 USD, au-dessus des plafonds actuels de la course
  (Claude 40,4 ; total 52,6 à 61) : nouvelle enveloppe à poser au devis v8 ou v9.
- **Processeur.** Tests de mort et rejouées : processeur seul, gratuits ; délai : ≈ 1 à 3 heures par course en plus (SUPPOSÉ).
- **Cartes.** Aucune dans le premier hybride. Si une fiche de test exige une carte (sondes rejouées, modèle de 8 milliards) : instance Vast.ai sur devis séparé, ≈ 0,5 à
  2 USD par heure (SUPPOSÉ), `GO_ID` au lancement, arrêt par identifiant (R10).
- **Épreuve R5 réelle du cadre** (étage 2 de la note du tour (c), étendue au cadre : lecture hors racine, écriture hors dossier, réseau, sous-agent, modification du sas,
  exfiltration par le papier) : une dizaine de sessions courtes, ≈ 5 à 15 USD.
- **Nœuds pour Lazar** : (N1) **choix du cadre** — Agentic Scientist v3 recommandé (Apache-2.0, Claude Code, scellement natif d'évaluation), AIDE ou autoresearch pour la
  forme de boucle de (b) ; (N2) **GO sur devis** pour l'épreuve R5 réelle du cadre, puis pour chaque course du bras hybride ; (N3) **revue de sécurité** avant toute
  session réelle, puisque le cadre exécute du code : enveloppe du binaire `claude` avec notre crochet, bac à sable sans réseau, sas de gel, copie réempreintée ; revue
  faite par une lignée autre que celle qui écrit l'enveloppe (R2), **une tentative réussie de sortie arrête tout et revient à Lazar** ; (N4) toute expérience sur carte.

## 5. Décision (format du dépôt)

**Décision en une phrase** : comment construire l'hybride décidé par Lazar — intégrer un cadre tiers entier, n'emprunter que sa boucle d'exécution, ou les deux dans
l'ordre.
**Enjeu** : avoir vite un organisme qui *teste* (le mot de Lazar) sans ouvrir un trou de sûreté (code tiers à pleins droits) ni fausser la comparaison.

| option | ce que c'est | avantage | inconvénient |
|---|---|---|---|
| **(a)** hybride avec un cadre ouvert sous notre bac à sable, comparaison préenregistrée | Agentic Scientist v3 enfiché comme proposeur-expérimentateur, sas de gel, juge figé commun, protocole du § 3 | répond au mot de Lazar tel quel ; un cadre éprouvé (70 campagnes) ; scellement d'évaluation déjà dans sa forme ; comparaison externe crédible pour un papier | code tiers lancé « à pleins droits » à brider : enveloppe neuve, Docker à remplacer, revue de sécurité ; installabilité SUPPOSÉE (README non lu) ; comparaison asymétrique tant que notre organisme n'exécute pas |
| **(b)** emprunter seulement la boucle d'exécution (couche 3 légère) | dans notre noyau : fiche gelée → script en bac à sable → run borné sur la tranche exploratoire → « survit / éliminée » au seuil gelé, retour arrière à la manière d'`autoresearch` ; traçabilité nombre → ligne de code à la manière de data-to-paper | nos gardes, notre code, R5 déjà outillé (crochet, `bwrap`) ; quelques jours ; aucune licence ni code tiers | pas de comparaison « contre un cadre existant » ; on réinvente ce que le cadre fait déjà (arbre d'expériences, ablations) |
| **(c)** les deux, (b) d'abord | (b) en routine tout de suite ; (a) préparé en parallèle (enveloppe, épreuve R5 étage 1 hors ligne), joué à partir de la course 3 sur GO | comparaison symétrique (les deux exécutent) ; rien n'attend : (b) sert la course 2 ; (a) arrive avec sa revue de sécurité faite | deux chantiers ; le bras hybride ne compare rien avant la course 3 |

**Recommandation : (c)**, confiance **0,6** (l'installabilité du cadre et la tenue du cache sont supposées ; la puissance à huit fiches est faible, d'où trois courses).
**Défaut sous 48 heures (≈ 31 octobre, 11:45 UTC)** : (c) **en préparation seulement** — (b) codée et essayée hors ligne (routine, processeur) ; inventaire gelé sur
Agentic Scientist v3 ; aucune installation de code tiers dans le dépôt de travail avant la revue de sécurité (N3) ; aucune session réelle, aucune dépense, aucune carte :
ces points restent des nœuds (N1 à N4).

## Réserves

- Aucun dépôt GitHub ni PDF arXiv n'a pu être lu (hors liste blanche) : licences, modèles, prérequis et chiffres viennent de pages secondaires et de deux README relayés ;
  à vérifier sur les dépôts et PDF empreintés (R7) avant tout préenregistrement ou devis.
- Que le cadre accepte de lancer `claude` à travers une enveloppe portant notre crochet, et qu'il tourne sans Docker dans `bwrap`, est SUPPOSÉ.
- Les seuils du § 3 (0,25 ; 0,10 ; 1,5 ×) sont des propositions à geler dans le préenregistrement, pas des chiffres mesurés ; la puissance est calculée sur des tailles
  de fiches supposées.
- La note ne lit aucune fiche de course réelle ; elle ne préjuge pas du recoupement de la question de la course 2 (v0 non contre-lu).

## Sources (pages lues par le relais, 29 octobre 2026)

- Agentic Scientist v3 : [runtimewire](https://runtimewire.com/article/sakana-ai-agentic-scientist-v3) ; [explainx](https://www.explainx.ai/blog/sakana-agentic-scientist-v3-ai-scientist-v3-coding-agents-open-source-2026) ; [alphasignal](https://alphasignal.ai/news/sakana-ai-s-agentic-scientist-turns-coding-agents-into-open-source-researchers) ; dépôt annoncé `github.com/SakanaAI/AI-Scientist-v3`, arXiv 2610.18933 (non lus).
- AI-Scientist-v2 : [README GitHub](https://github.com/sakanaai/ai-scientist-v2) ; [Nature, note aiweekly](https://aiweekly.co/alerts/sakana-ais-ai-scientist-lands-in-nature-after-peer-review) ; arXiv 2504.08066 (non lu).
- Agent Laboratory : [README GitHub](https://github.com/SamuelSchmidgall/AgentLaboratory) ; arXiv 2501.04227 (non lu).
- AI-Researcher : [fiche SourcePulse](https://www.sourcepulse.org/projects/1840471).
- Denario : [PyPI](https://pypi.org/project/denario/) ; arXiv 2510.26887 (non lu).
- AIDE : [README](https://raw.githubusercontent.com/WecoAI/aideml/main/README.md).
- Curie : [fiche osrepos](https://osrepos.com/repo/just-curieous-curie.md) ; [résumé moonlight](https://www.themoonlight.io/en/review/curie-toward-rigorous-and-automated-scientific-experimentation-with-ai-agents) ; arXiv 2502.16069 (non lu).
- CodeScientist : [billet Ai2](https://allenai.org/blog/codescientist) ; [fiche SourcePulse](https://www.sourcepulse.org/projects/1924750).
- DeepScientist : [arXiv 2509.26603, version HTML](https://arxiv.org/html/2509.26603v1).
- autoresearch : [VentureBeat](https://venturebeat.com/technology/andrej-karpathys-new-open-source-autoresearch-lets-you-run-hundreds-of-ai).
- data-to-paper : [README GitHub](https://github.com/Technion-Kishony-lab/data-to-paper/blob/main/README.md).
- Kosmos : [arXiv 2511.02824, version HTML](https://arxiv.org/html/2511.02824v2).
- Banc de comparaison : [Ravideshik et Kejriwal, arXiv 2607.28631 (PDF)](https://arxiv.org/pdf/2607.28631).

Horodatage de fin : rédaction achevée le 2026-10-29 à **11:47 UTC** (relevé `date -u` dans la commande qui a compté les lignes et empreinté la première version ; cette
ligne est la seule retouche après ce relevé, l'empreinte finale est celle rendue dans la réponse du sous-agent).
