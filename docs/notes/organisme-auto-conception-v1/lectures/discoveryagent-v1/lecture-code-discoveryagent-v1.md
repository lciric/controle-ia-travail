# Lecture du code de DiscoveryAgent — v1

Lecteur neuf : Claude Opus 5.5, sur le mandat `mandat-lecteur-code-discoveryagent-v1.md` (sha256 129714fa4379345b90c167877b901a50a12a3f0d0c977bb0fbaf9d87fffc48db), 19 novembre 2026. Pièce de travail : une carte factuelle de ce que fait le code, sans recommandation ni jugement sur l'intérêt du système.

- **Code lu** : dépôt public DiscoveryAgent-code (licence MIT), copie locale `/home/user/owencqueen/discoveryagent-code`, commit `b510bb2c6c098620d76927c3a628bf8060658df4`, 123 fichiers suivis. Rien n'a été exécuté ni installé ; le dépôt a été traité comme une donnée.
- **Papier** : arXiv 2611.21950 v1 (40 pages) et son annexe (150 pages), lus dans `docs/sources/arxiv-2611.21950-v1/` (empreintes vérifiées contre leurs fichiers `.sha256`). Les numéros de page sont ceux du PDF ; ils coïncident avec les numéros imprimés, dans le papier comme dans l'annexe.
- **Reprise** : une première passe s'est arrêtée au premier refus de la garde de calcul (une commande de prise de notes citait un enchaînement d'arrêt de processus) ; la mère a repris le mandat avec des consignes d'écriture. Cette version est complète.

## 0. Conventions de citation et vérification

- Code, en ligne : `chemin:L1-L2` suivi de « extrait » ; l'extrait figure dans les lignes L1 à L2 du fichier au commit. Une référence sans extrait n'est contrôlée qu'en portée.
- Code, en bloc : une ligne « Source : `chemin:L1-L2` » suivie d'un bloc recopié mot pour mot.
- Papier et annexe : (papier p. N « extrait ») ou (annexe p. N « extrait ») ; l'extrait figure à la page N du texte extrait.
- Toutes ces citations sont relues par `outils-lecteur-code-v1/verifier_citations_v1.py`, qui contrôle aussi le registre de couverture et quinze recherches d'occurrences (`outils-lecteur-code-v1/controles-recherche-v1.json`, notées R01 à R15 ci-dessous) ; sa sortie est `outils-lecteur-code-v1/sortie-verification-citations-v1.txt` (bilan à la section 8).
- « Défaut du lanceur » désigne la valeur prise quand `scripts/run.py` est lancé sans la régler ; les classes de `config.py` portent d'autres défauts, rappelés quand ils diffèrent.

## 1. Couverture

- 123 fichiers suivis. **97 lus en entier** : tout `DiscoveryAgent/` (55 fichiers), `scripts/` (3), `configs/` (9), `tests/` (13), `claude_md_templates/` (1), `guides/` (1), `setup/` (2), `README.md`, `pyproject.toml`, `requirements.txt`, `.env.example`, `.gitignore`, `.python-version`, `LICENSE`, les trois `inputs/*/TASK_DESCRIPTION.md` et trois petits fichiers de `acs_agent/` (`__init__.py`, `__main__.py`, `tool_agent.py`).
- **26 parcourus** (permis par le mandat) : les 19 autres fichiers de `acs_agent/`, les six `inputs/*/README.txt` et `uv.lock`.
- Détail fichier par fichier (lignes, statut, rôle) : `registre-couverture-code-discoveryagent-v1.json`.

## 2. La carte du système, tirée du code

### 2.1 La boucle extérieure (tours, branches, modes, reprise)

- **Lanceur.** `scripts/run.py` lit la ligne de commande, puis un `config.json` de point de contrôle (reprise), puis un YAML, la ligne de commande gardant toujours la priorité (`DiscoveryAgent/utils/config_loader.py:142-144` « `if target_key in cli_override_keys:` »). Il crée le bac à sable `<dataset>/<analyse>_<horodatage>/`, charge `data/README.txt` comme description des données, la tâche éventuelle, construit les agents et lance `HypothesisBrancher` (`scripts/run.py:729-737` « `brancher = HypothesisBrancher(` »).
- **Tours.** `run_all_branches` boucle sur les tours d'une invocation : `DiscoveryAgent/hypothesis_brancher.py:536` « `end_round = start_round + self.num_rounds` », `DiscoveryAgent/hypothesis_brancher.py:575` « `for round_idx in range(start_round, end_round):` ». Défaut du lanceur : un tour par invocation (`scripts/run.py:858-859` « `args.num_rounds = 1` »).
- **Branches.** Une seule est possible : `DiscoveryAgent/hypothesis_brancher.py:115-116` « `raise NotImplementedError("Parallel workflow execution is not implemented yet")` » et `DiscoveryAgent/hypothesis_brancher.py:666` « `assert len(workflows) == 1, "Only one workflow is supported for now"` ».
- **Au début de chaque tour** : sauvegarde de `round_N/config.json` (`DiscoveryAgent/hypothesis_brancher.py:612-615` « `save_round_config_checkpoint(` ») ; à partir du deuxième tour d'une invocation, remise à zéro du workflow et injection de la mémoire accumulée comme rapport de fond (`DiscoveryAgent/hypothesis_brancher.py:649-656` « `workflow.background_report = accumulated_report` »).
- **Mode automatique.** Si le tour n'est ni exploratoire ni piloté, le workflow génère une hypothèse au début du tour (section 2.3) puis la fait tester par le directeur.
- **Mode piloté (« sélection humaine »).** Pas de génération : à partir du tour 1, le brancheur prend `round_{N-1}/selected_hypothesis.md` s'il existe (`DiscoveryAgent/hypothesis_brancher.py:676-681` « `f"round_{round_idx - 1}" / "selected_hypothesis.md"` »), et pour le premier tour le fichier donné par `--selected-hypothesis-file`. Le README décrit le geste humain : écrire ce fichier à la main puis relancer depuis le `config.json` du tour (`README.md:194-205` « `Write the hypothesis to test next, in plain Markdown, to` »). Le dépôt ne génère ni ne révise de candidats. Le statut de pause `paused_for_selection` est testé mais n'est produit nulle part (`DiscoveryAgent/hypothesis_brancher.py:822` « `if results.get('status') == 'paused_for_selection':` » ; `DiscoveryAgent/director_workflow.py:1232` « `'status': 'stopped_by_director' if director_requested_stop else 'completed'` » ; contrôle R06). En mode piloté sans fichier d'hypothèse et sans tour exploratoire, le directeur ne reçoit aucune hypothèse ni consigne de mode (`DiscoveryAgent/director_workflow.py:906-910` « `# Normal resume: hypothesis context should be in director state` »).
- **Tours exploratoires.** Les `num_exploration_rounds` premiers tours sont exploratoires, sauf si une hypothèse choisie existe : `DiscoveryAgent/hypothesis_brancher.py:719-723` « `not has_selected_hypothesis  # Don't explore if we have a selected hypothesis` ». En exploration, pas d'hypothèse ; le directeur reçoit l'invite d'exploration.
- **Fin de tour** : rapport final du directeur, sauvegarde de `round_report.md`, du journal, mise à jour de la mémoire puis `memory_report.md` (`DiscoveryAgent/hypothesis_brancher.py:796` « `self.results_memory.update_report(final_report, verbose=False)` »). Une exception marque le tour « failed » et la boucle continue (`DiscoveryAgent/hypothesis_brancher.py:870-878` « `'status': 'failed'` »). Hors mode piloté, un rapport consolidé est écrit à la fin (`DiscoveryAgent/hypothesis_brancher.py:890` « `if not is_human_selection and any(r['status'] == 'completed' for r in self.branch_results):` »).
- **Reprise.** Un tour est complet si `round_N/memory_report.md` existe (`DiscoveryAgent/hypothesis_brancher.py:244-246` « `memory_report = item / "memory_report.md"` ») ; on repart au tour suivant (`DiscoveryAgent/hypothesis_brancher.py:511-512` « `start_round = last_completed + 1` »). Un tour ayant `config.json` mais pas `memory_report.md` est incomplet (`DiscoveryAgent/hypothesis_brancher.py:292` « `if config_file.exists() and not memory_report.exists():` ») ; s'il est le tour attendu, le workflow est restauré depuis son dernier `query_NN/checkpoint.json` (`DiscoveryAgent/hypothesis_brancher.py:517` « `if incomplete_state and incomplete_state['round_num'] == start_round:` ») ; si la restauration échoue, départ neuf. Côté lanceur, la reprise réutilise l'espace de travail du `config.json` (`scripts/run.py:882` « `args.existing_codebase = args.working_directory` ») et recharge la mémoire : celle du tour s'il est complet, sinon celle du tour précédent (`scripts/run.py:139-155` « `required_report = checkpoints_dir / f"round_{previous_round}" / "memory_report.md"` »).
- **Mémoire à la reprise.** Le fichier `memory_report.md` entier, en-têtes compris, devient la mémoire (`scripts/run.py:537-538` « `background_report = load_background_report(args._resume_memory_report_path)` », `DiscoveryAgent/hypothesis_brancher.py:151-156` « `self.results_memory.current_report = seed_content` ») : la fonction qui extrairait la seule section « Accumulated Report » n'est jamais appelée (`DiscoveryAgent/hypothesis_brancher.py:215` « `def _extract_accumulated_report(raw_content: str) -> str:` » ; contrôle R08).
- **Message trompeur.** Le texte de pause conseille un drapeau `--resume` que l'analyseur d'arguments ne définit pas (`DiscoveryAgent/hypothesis_brancher.py:834` « `--resume --selected-hypothesis-file` »).
- **Code mort.** `generate_next_round_prompts` est définie sans être appelée (`DiscoveryAgent/hypothesis_brancher.py:459` « `def generate_next_round_prompts(` » ; contrôle R15).

### 2.2 La boucle intérieure (directeur, format d'un appel, budget, arrêt, compaction)

- **Construction du workflow** (`DirectorWorkflow.__init__`) : rapport de fond (2.3), agents outils, catalogue « Helper Agent i » ajouté à l'invite système du directeur (`DiscoveryAgent/hyp_agents/director_agent.py:271-272` « `# Helper Agents` »), conception du relecteur (2.5), gestionnaire de points de contrôle, dépôt git de l'espace de travail.
- **Une requête = un appel du directeur suivi d'un appel d'agent outil.** Boucle `DiscoveryAgent/director_workflow.py:917` « `while query_num <= self.max_queries:` ». Avant chaque appel, le compte des jetons de la conversation est demandé à l'API (`DiscoveryAgent/director_workflow.py:924` « `dir_tokens = self.director_agent.estimate_context_tokens()` »).
- **Ce que reçoit le directeur à chaque tour de parole** (`DiscoveryAgent/hyp_agents/director_agent.py:580-645`) : le rapport de la seule requête précédente, ou la description des données à la première requête (`DiscoveryAgent/hyp_agents/director_agent.py:584-587` « `turn_prompt += DATASET_DESCRIPTION_PROMPT.format(` ») ; une fois par tour, la mémoire accumulée (`DiscoveryAgent/hyp_agents/director_agent.py:589` « `if background_report and (not self.background_report_read):` ») et l'hypothèse ou la consigne d'exploration ; le budget restant (`DiscoveryAgent/hyp_agents/director_agent.py:621` « `queries left.` ») ; la critique du relecteur s'il y en a une ; la consigne d'arrêt si permise. Les rapports plus anciens restent dans la conversation persistante. La **tâche** (brief) n'est jamais transmise au directeur : `generate_query` n'a pas de paramètre pour elle et le fichier de l'agent directeur ne contient pas le mot `task_description` (contrôle R10), alors que son invite système annonce une tâche (`DiscoveryAgent/hyp_agents/director_agent.py:70` « `You will receive a research context (dataset description, task, and potentially a hypothesis or exploration directive)` »).
- **Format d'un appel.** Le directeur répond par une interprétation, une réflexion et une balise `<étiquette>requête</étiquette>` (`DiscoveryAgent/prompts/hyp_generation.py:67` « `**Thought**: [Your reasoning and plan for this step]` »). Le workflow prend la première balise trouvée n'importe où dans la sortie : `DiscoveryAgent/director_workflow.py:1000` « `xml_match = re.search(r'<(\w+)>([\s\S]*?)</\1>', query, re.DOTALL)` ». L'étiquette doit nommer un agent outil (`DiscoveryAgent/director_workflow.py:678` « `if tag not in self.agents:` »). La requête est écrite sur disque avant l'envoi (`DiscoveryAgent/director_workflow.py:686` « `persist_query_input(progress_round_dir, current_query_num_for_progress, query)` »).
- **Budget.** `num_queries` requêtes par tour (défaut du lanceur 5, `DiscoveryAgent/utils/arg_parsers.py:80` « `parser.add_argument("--num_queries", type=int, default=5,` ») et `num_rounds` tours par invocation. Une sortie sans balise ne consomme pas de requête : le directeur est relancé avec la consigne « SHORTER » jusqu'à trois fois (`DiscoveryAgent/director_workflow.py:284` « `max_tool_invocation_retries: int = 3,` », `DiscoveryAgent/director_workflow.py:1039` « `if tool_invocation_retry_count > self.max_tool_invocation_retries:` »), puis le tour s'arrête et passe au rapport. Les erreurs d'API surchargée ou 429/500/503 sont réessayées jusqu'à cinq fois, à 60 s d'intervalle (`DiscoveryAgent/hyp_agents/director_agent.py:356` « `max_retries: int = 5, wait_time: int = 60` »).
- **Signal d'arrêt.** Si permis, la sous-chaîne `<<STOP>>` dans la sortie du directeur arrête le tour : `DiscoveryAgent/director_workflow.py:986` « `if self.allow_director_to_stop and ("<<STOP>>" in query):` ». La consigne est dans l'invite système et répétée à chaque tour de parole (`DiscoveryAgent/hyp_agents/director_agent.py:203` « `You should do this by outputting <<STOP>> in your next query.` »).
- **Après chaque requête réussie** : point de contrôle de la requête (`DiscoveryAgent/director_workflow.py:1119` « `checkpoint_path = self.checkpoint_manager.save_checkpoint(query_num)` »), commit git (`DiscoveryAgent/director_workflow.py:1135-1136` « `commit_message = f"Query {query_num}"` »), rafraîchissement de la description en mode jeu croissant, puis éventuelle relecture (2.5).
- **Rapport de tour.** Le directeur écrit le rapport final dans sa conversation, sur l'invite à quatre sections (`DiscoveryAgent/hyp_agents/director_agent.py:698` « `Here is the cumulative report from all of your queries and analyses` ») ; en cas d'échec ou de refus, le rapport cumulé brut le remplace.
- **Compaction du contexte.** Réservée au fournisseur Anthropic et à un directeur dont le nom de modèle contient `claude-opus-4-6` : `DiscoveryAgent/hyp_agents/director_agent.py:305-309` « `and 'claude-opus-4-6' in self.llm_config.model_name` ». Elle est demandée à l'API (édition côté serveur) avec un déclencheur en jetons d'entrée : `DiscoveryAgent/hyp_agents/director_agent.py:380-386` « `"type": "compact_20260112",` ». Si la compaction est inactive et que l'API répond « prompt is too long », elle est activée au seuil minimal de 50 000 et l'appel est refait (`DiscoveryAgent/hyp_agents/director_agent.py:441-463` « `self.compaction_trigger_tokens = 50000` »). L'invite de résumé (`DiscoveryAgent/hyp_agents/director_agent.py:220-229`) est citée mot pour mot en section 4.
- **Remise à zéro entre tours** : conversations du directeur et de l'agent d'hypothèse vidées, rapports du tour vidés ; la mémoire (rapport de fond) et l'invite du relecteur sont gardées (`DiscoveryAgent/director_workflow.py:1789` « `# NOTE: background_report is intentionally NOT reset - it should persist across rounds` »).

### 2.3 La génération d'hypothèses

- **Quand.** Seulement en mode automatique, hors tour exploratoire et hors reprise en cours de tour : `DiscoveryAgent/director_workflow.py:840` « `skip_hypothesis_generation = mid_round_resuming or exploratory_mode or self.hypothesis_config.human_selection_mode` ».
- **Entrées.** Description des données, tâche si elle existe, mémoire accumulée (une fois) : `DiscoveryAgent/director_workflow.py:849-853` « `background_report=self.background_report,  # Consolidated knowledge` » ; `DiscoveryAgent/hyp_agents/hypothesis_gen_agent.py:301` « `prefix_prompt += DATASET_DESCRIPTION_TASK_DESCRIPTION_PROMPT.format(` ».
- **Rapport de fond de littérature.** Il est produit avant le premier tour dans `deep_research_background.md` du dossier des journaux (une requête à Perplexity, ou un résumé des PDF fournis par le modèle du directeur), réutilisé s'il existe (`DiscoveryAgent/director_workflow.py:357-359` « `self.background_report_path = Path(self.log_dir) / "deep_research_background.md"` »). L'agent d'hypothèse le lit (`DiscoveryAgent/hyp_agents/hypothesis_gen_agent.py:129-132` « `self.background_literature_content = f.read()` ») mais **aucune invite ne l'utilise** (contrôle R04 : trois occurrences, toutes dans le chargement).
- **Nombre de candidats.** Un seul, en un appel : `DiscoveryAgent/hyp_agents/hypothesis_gen_agent.py:354` « `hypothesis_prompt = prefix_prompt + HYPOTHESIS_GENERATION_PROMPT` ». L'invite système parle pourtant d'une liste soumise au choix d'un scientifique (`DiscoveryAgent/hyp_agents/hypothesis_gen_agent.py:36` « `You will be asked to generate a list of hypotheses` »).
- **Forme d'un candidat.** Deux champs : `DiscoveryAgent/prompts/hyp_generation.py:153-154` « `**Justification**: [Your justification for why this hypothesis is novel and impactful]` ». Pas de plan : le réglage `generate_plan` est stocké mais jamais lu (`DiscoveryAgent/hyp_agents/hypothesis_gen_agent.py:80` « `self.generate_plan = getattr(self.config, "generate_plan", False)` » ; contrôle R05).
- **Révision.** Aucune fonction de révision, de régénération ni de dialogue avec l'agent d'hypothèse dans le dépôt. L'hypothèse brute (texte complet) est passée au directeur dans l'invite de test (`DiscoveryAgent/hyp_agents/director_agent.py:597-611` « `turn_prompt += HYPOTHESIS_ORCHESTRATION_PROMPT.format(` ») et sauvegardée dans `query_00/hypothesis_000.md` (`DiscoveryAgent/checkpoint_manager.py:328` « `markdown_path = checkpoint_dir / "hypothesis_000.md"` »).

### 2.4 La mémoire empirique et la mémoire procédurale

**Mémoire empirique** (`DiscoveryAgent/memory/results_memory.py`), un seul modèle pour les trois agents (`DiscoveryAgent/memory/results_memory.py:417-419` « `self.refiner = RefinerAgent(llm_config)` »).

| Étape | Ce qu'elle reçoit | Ce qu'elle rend | Code |
|---|---|---|---|
| 0. Premier rapport | le rapport du tour | stocké tel quel, sans appel | `DiscoveryAgent/memory/results_memory.py:444-448` « `self.current_report = new_report` » |
| 1. Intégrateur | mémoire courante + rapport du tour | un rapport intégré à quatre sections, tout gardé | `DiscoveryAgent/memory/results_memory.py:459` « `integrated_report, integration_cost = self.integrator.integrate(` » |
| 2. Analyseur | le rapport intégré | un JSON de redondances (sections, raison, risque, informations à garder) ; JSON illisible = liste vide | `DiscoveryAgent/memory/results_memory.py:310-314` « `analysis_dict = {"redundancies": []}` » |
| 3. Raffineur | rapport intégré + toute l'analyse | le rapport raffiné, qui remplace la mémoire | `DiscoveryAgent/memory/results_memory.py:496` « `refined_report, refinement_cost = self.refiner.refine(` » |

- Le filtrage « seulement le risque faible » et la vérification des informations à garder ne sont demandés que par consigne : le code passe toute l'analyse au raffineur (`DiscoveryAgent/memory/results_memory.py:356` « `redundancy_analysis=json.dumps(redundancy_analysis, indent=2)` ») et ne contrôle pas le résultat. La consigne demande aussi d'élaguer au-delà des redondances (`DiscoveryAgent/memory/results_memory.py:161` « `4. Remove unnecessary verbosity and trim to essential results` »).
- La docstring développe ACE en « Atomic Context Extension » (`DiscoveryAgent/memory/results_memory.py:7` « `following the ACE (Atomic Context Extension) paper` »).
- La mémoire est injectée une fois par tour dans le directeur et dans l'agent d'hypothèse, sous le titre « Accumulated Knowledge from Previous Rounds » (`DiscoveryAgent/prompts/hyp_generation.py:120` « `## Accumulated Knowledge from Previous Rounds` »).

**Mémoire procédurale** : deux fichiers de l'espace de travail, tenus par deux sous-agents du SDK lancés par l'agent d'exécution quand `sub_agent_architecture` est vrai (vrai dans les six configurations).

- `documentation_agent` (DOCUMENTATION.md, détaillé) et `claude_md_agent` (CLAUDE.md, court) ont l'outil d'édition sans restriction de fichier : `DiscoveryAgent/prompts/cc_sub_agents.py:66` « `tools=["Read", "Edit", "Glob", "Grep"],` ». La limite à leur propre document n'est qu'une consigne, et seulement pour DOCUMENTATION.md : `DiscoveryAgent/prompts/claude_md_generator_command.py:173` « `CRITICAL: You are only allowed to edit DOCUMENTATION.md, but you may read any script or file in the directory.` ».
- Leurs invites sont transmises sans remplacer les marqueurs de chemin : `DiscoveryAgent/prompts/claude_md_generator_command.py:171` « `IMPORTANT: You must write the file to this exact location: {documentation_path}` » ; seul l'agent `execution_agent` reçoit une invite modifiée (`DiscoveryAgent/tool_agents/execution_agent_cc.py:1151-1159` « `modified_prompt = agent_def.prompt` »).
- L'agent d'exécution principal reçoit l'obligation de tenir ces deux fichiers (`DiscoveryAgent/prompts/execution_agent.py:44` « `You are REQUIRED to write ALL detailed code documentation` ») ; les sous-agents prennent le modèle de l'agent d'exécution (`DiscoveryAgent/tool_agents/execution_agent_cc.py:236` « `return "inherit"` »).
- La liste des outils permis de la session principale ne nomme pas l'outil de délégation (`DiscoveryAgent/tool_agents/execution_agent_cc.py:1220` « `allowed_tools = ["Read", "Write", "Edit", "Bash", "Glob", "Grep"]` ») ; l'effet de cette absence dépend du SDK et n'est pas lisible dans ce dépôt.

### 2.5 Le relecteur et le concepteur de relecture

- **Concepteur.** À chaque construction du workflow (chaque lancement ou reprise de `run.py`, et à nouveau lors d'une restauration en cours de tour), si `review_design` est vrai, un appel écrit l'invite système du relecteur à partir de la description des données et de la tâche : `DiscoveryAgent/director_workflow.py:453-462` « `generated_reviewer_prompt = review_designer.design_reviewer_prompt(` ». Cet appel est plafonné à 2 000 jetons (`DiscoveryAgent/meta_agents/review_designer.py:83` « `max_tokens: int = 2000,` »). Dans un même lancement de plusieurs tours, l'invite est conçue une fois et gardée.
- **Relecteur.** Une instance `OnePassLLM`, ou `BaseLLMWithSearch` (recherche web native, trois recherches au plus) si `review_search` est vrai (`DiscoveryAgent/director_workflow.py:489-497` « `self.review_optimization_llm = BaseLLMWithSearch(` »).
- **Ce qu'il reçoit** : la description des données, la mémoire accumulée et le rapport cumulé du tour (`DiscoveryAgent/director_workflow.py:1280-1292` « `And here is the most recent analysis. You should focus your critiques on these findings and approaches:` »).
- **Où va sa critique** : elle est jointe au prochain tour de parole du directeur (`DiscoveryAgent/hyp_agents/director_agent.py:631` « `Your work from the previous query was also fed into a reviewer agent` ») et ajoutée à `round_N/reviewer_logs/review_N.md`, qui ne garde que la sortie (`DiscoveryAgent/checkpoint_manager.py:683` « `review_content += "### Reviewer Output\n\n"` »). La même formule « reviewer agent » sert aussi à transmettre la consigne « SHORTER » après une sortie malformée.
- **Quand il se déclenche.** Seul chemin : `DiscoveryAgent/director_workflow.py:1149-1165` (contrôles R01 et R02). Pas après la dernière requête ; si `hold_reviews_in_exploratory_phase` est vrai, la décision passe par une fonction qui renvoie faux dès que `explicit_hypothesis_step` vaut None :

Source : `DiscoveryAgent/director_workflow.py:577-578`
```text
        if self.explicit_hypothesis_step is None:
            return False # We're not using explicit hypotheses
```

Source : `DiscoveryAgent/director_workflow.py:1155-1161`
```text
                if previous_query_num >= self.max_queries:
                    perform_review = False
                elif self.hold_reviews_in_exploratory_phase:
                    # Sets to true if frequency is met
                    perform_review = self._test_iteration_condition_with_warmup(previous_query_num, self.review_optimization_steps)
                elif (previous_query_num % self.review_optimization_steps == 0):
                    perform_review = True
```

- Le défaut du lanceur met `hold_reviews_in_exploratory_phase` à vrai (`DiscoveryAgent/utils/arg_parsers.py:163` « `parser.set_defaults(hold_reviews_in_exploratory_phase=True)` »), les six configurations aussi, et aucune ne fixe `explicit_hypothesis_step` (contrôle R03). **Avec les six configurations publiées, le relecteur n'est donc jamais appelé.** Il ne l'est qu'en ajoutant `--explicit_hypothesis_step` ou `--no-hold-reviews-in-exploratory-phase`. Le mécanisme de retenue ne lit pas le mode exploratoire du tour : il porte sur un pas de requête à l'intérieur du tour.
### 2.6 Les points de contrôle et la version du code

**Disposition du magasin** (pour une course `<analyse>_<horodatage>` sur le jeu `<dataset>`) :

```text
$DATA_PATH/LOGS/<dataset>/<analyse>_<horodatage>/
  discoveryagent.log, discoveryagent_actions.log     journal complet, journal des actions filtré
  deep_research_background.md                        rapport de fond (2.3)
  searches/round_N/                                   sorties brutes des recherches web et approfondies
  checkpoints/
    config.yaml                                       instantané des arguments résolus
    reviewer_prompt.md, reviewer_prompt.json          invite du relecteur (à la racine, voir plus bas)
    round_N/
      config.json                                     configuration de départ du tour
      query_00/checkpoint.json, hypothesis_000.md     hypothèse initiale (mode automatique)
      query_NN/checkpoint.json                        état complet après la requête NN
      query_NN/query_input_NN.md, query_report_NN.md  requête envoyée, rapport de l'agent outil
      query_NN/query_status.json, execution_log_NN.txt
      query_NN/execution_agent/tool_calls.jsonl, messages.jsonl, transcript.txt
      latest -> query_NN                              lien vers la dernière requête
      round_report.md, memory_report.md, round.log    rapport du tour, mémoire après intégration, journal
      live_round.log, round_activity.jsonl            journal en direct, événements (pour un frontal)
      reviewer_logs/review_N.md                       critiques du relecteur (sortie seule)
      selected_hypothesis.md                          écrit par le scientifique (mode piloté)
$DATA_PATH/<dataset>/<analyse>_<horodatage>/          espace de travail de l'agent d'exécution (dépôt git)
```

Appuis : `scripts/run.py:575` « `PARENT_LOG = os.path.join(DATA_DIR, "LOGS")` », `scripts/run.py:707` « `"config.yaml"` », `DiscoveryAgent/utils/logger.py:107` « `"discoveryagent.log"` », `DiscoveryAgent/director_workflow.py:714` « `searches_dir = str(Path(self.log_dir) / "searches" / f"round_{round_num}")` », `DiscoveryAgent/checkpoint_manager.py:99` « `return query_directory(self.checkpoint_base / f"round_{effective_round}", query_num)` », `DiscoveryAgent/utils/query_artifacts.py:22` « `return f"{query_num:02d}"` », `DiscoveryAgent/utils/query_artifacts.py:67-72` « `return f"query_{role}_{query_suffix(query_num)}.md"` », `DiscoveryAgent/tool_agents/execution_sdk_tracker.py:197-199` « `"tool_calls.jsonl"` », `DiscoveryAgent/utils/progress_recorder.py:62` « `"query_status.json"` », `DiscoveryAgent/utils/progress_recorder.py:133` « `"round_activity.jsonl"` », `DiscoveryAgent/utils/logger.py:240` « `log_path = round_dir / "live_round.log"` », `DiscoveryAgent/checkpoint_manager.py:852` « `latest_link.symlink_to(target)` ».

**Schéma exact d'un point de contrôle par requête** (`checkpoint.json`), d'après `DiscoveryAgent/checkpoint_manager.py:144-222` :

```text
checkpoint_version ("2.0"), timestamp, query_num,
workflow_state : dataset_description, task_description, max_queries, query_num, round_num,
                 results [ {query_num, query_raw, query_parsed, result, timestamp} ],
                 report (dernière requête seule), cumulative_report, images, image_counter,
                 review_history, generated_reviewer_prompt,
                 git_tracking, multiturn_hypothesis, review_search, review_design
agents : director_agent        {type, state, state_hash}
         hypothesis_gen_agent  {type, state, state_hash}
         hypothesis_agent      {type, state, state_hash}   même objet que le directeur, en double
         <étiquette de chaque agent outil> {type, state, state_hash}
validation : state_hashes {agent: sha256}, checkpoint_hash (sha256 du JSON trié), timestamp
```

- `state` du directeur : agent_type, messages (toute la conversation), system_prompt, conversation_length, background_report_read, target_hypothesis_read, exploratory_mode_prompted, estimated_tokens, llm_config (model_name, api_provider, temperature, frequency_penalty, api_key_hash), config_data, tool_agent_prompt, mcp_servers, compaction_enabled ; l'agent d'hypothèse a les mêmes champs sauf les trois derniers et les deux drapeaux de mode. Le champ `api_key_hash` vaut `hash()` de la clé d'API (`DiscoveryAgent/hyp_agents/director_agent.py:766` « `'api_key_hash': hash(self.llm_config.api_key) if self.llm_config.api_key else None` »).
- `state` de l'agent d'exécution : agent_type, execution_count, execution_context (les arguments de l'appel, dont l'objet workflow sérialisé en texte), working_directory, existing_files_count, config_info, claude_session_info (`DiscoveryAgent/tool_agents/execution_agent_cc.py:2202-2220`). Recherche web et approfondie : agent_type, config_agent_name, config_tag (`DiscoveryAgent/tool_agents/base.py:39-43` « `'config_tag': getattr(self.config, 'tag', None)` »).
- Le doublon de l'agent d'hypothèse hérité vient de `DiscoveryAgent/director_workflow.py:419` « `self.hypothesis_agent = self.director_agent` » ; chaque `save_state` du directeur et de l'agent d'hypothèse appelle l'API de compte de jetons, deux fois par agent (état puis empreinte : `DiscoveryAgent/checkpoint_manager.py:174-175` « `'state_hash': self._compute_state_hash(dir_agent.save_state())` »).
- La configuration complète de la course n'est pas dans le point de contrôle par requête (seulement les quatre drapeaux ci-dessus et max_queries) ; elle est dans `round_N/config.json`.

**Pièces écrites par tour** : `config.json` au début (`DiscoveryAgent/checkpoint_manager.py:483` « `config_path = save_dir / "config.json"` ») ; l'hypothèse initiale en mode automatique ; les pièces de chaque requête ; `round_report.md` (`DiscoveryAgent/checkpoint_manager.py:536` « `markdown_path = save_dir / "round_report.md"` ») ; `round.log` ; `memory_report.md` (`DiscoveryAgent/checkpoint_manager.py:589` « `markdown_path = save_dir / "memory_report.md"` ») ; les critiques du relecteur s'il y en a. L'invite du relecteur est écrite à la racine `checkpoints/` et non dans `round_N/` : elle est sauvegardée pendant la construction du workflow (seul appel, `DiscoveryAgent/director_workflow.py:515` ; contrôle R09), quand le numéro de tour vaut encore None (`DiscoveryAgent/director_workflow.py:499-502` « `round_num=self.round_num` »), ce qui choisit la racine (`DiscoveryAgent/checkpoint_manager.py:396-398` « `save_dir = self.checkpoint_base` ») ; elle est réécrite à chaque lancement. Le dépôt n'écrit pas de liste de candidats. Le rendu `query_NNN.md` prévu par le gestionnaire n'est jamais appelé (`DiscoveryAgent/checkpoint_manager.py:710` « `def _save_queries_and_reports_markdown(` » ; contrôle R07) : le rendu lisible d'une requête est la paire `query_input_NN.md` et `query_report_NN.md`.

**Version du code de l'espace de travail.** Dépôt git initialisé dans l'espace de travail si `git_tracking` est vrai ; après chaque requête réussie : `git add -A .` puis retrait de l'index des fichiers de plus de 50 Mo (`DiscoveryAgent/utils/git_version_control.py:39` « `"DISCOVERYAGENT_GIT_MAX_FILE_SIZE_MB", "50"` »), puis un commit dont le message suit ce schéma :

Source : `DiscoveryAgent/utils/git_version_control.py:350-351`
```text
        if round_num is not None:
            full_message = f"[Round {round_num}] {message} | {timestamp}"
```

Le message vaut donc `[Round N] Query Q | AAAA-MM-JJ hh:mm:ss`, auteur « DiscoveryAgent Workflow » si aucun n'est configuré (`DiscoveryAgent/utils/git_version_control.py:388` « `"DiscoveryAgent Workflow"` »). Aucun commit après le rapport de tour ni après la mémoire. Le dossier `reports/queryN/` où l'agent d'exécution écrit son rapport est supprimé après lecture, donc avant le commit (`DiscoveryAgent/tool_agents/execution_agent_cc.py:1988-1989` « `shutil.rmtree(report_dir)` »).

**Reprise et retour en arrière.** La reprise est décrite en 2.1 ; au niveau de la requête, voir 2.10. Le dépôt ne contient aucun outil de retour en arrière : `GitVersionControl` ne fait qu'init, add, commit, status et compte des commits ; la reprise prend toujours le plus haut tour complet trouvé dans `checkpoints/`, si bien qu'un retour à un tour antérieur suppose de retirer à la main les dossiers des tours suivants et de remettre l'espace de travail à un commit antérieur.

### 2.7 Les agents d'audit (ce que fait réellement le dépôt)

- **Il n'y a pas d'agent d'audit à outils dans le dépôt** : ni configuration en lecture seule, ni configuration avec exécution, ni harnais Codex. Seuls l'agent d'exécution et l'agent OpenTargets reçoivent une liste d'outils permis (contrôle R13).
- `scripts/utils/audit_run.py` enchaîne quatre étapes : découverte des `checkpoint.json`, extraction des paires requête-résultat, résumé de chaque paire par Claude Haiku 4.5, rapport Markdown (`scripts/utils/audit_run.py:283` « `summarizer = AuditSummarizer(model_name=args.model, max_concurrent=args.max_concurrent)` »). Le résumé est un appel sans outil, 1 024 jetons, sur un résultat tronqué à 10 000 caractères (`DiscoveryAgent/audit/summarizer.py:118` « `result=pair.result[:10000],  # Limit result length to avoid token limits` »). Le rapport est assemblé sans appel de modèle (`DiscoveryAgent/audit/report_generator.py`).
- **Lecteurs désaccordés des fichiers écrits par le flux.** L'extraction lit d'abord un « markdown » (`DiscoveryAgent/audit/data_extractor.py:66` « `# Try markdown first (easier to parse, more readable)` ») ; ce fichier est `query_report_NN.md` (`DiscoveryAgent/audit/checkpoint_discovery.py:182` « `markdown_path = query_dir / artifact_filename(query_num, "report")` »), mais les expressions cherchent l'ancien format (`DiscoveryAgent/audit/data_extractor.py:93` « `raw_query_match = re.search(` ») et une paire est rendue même vide, si bien que le JSON complet n'est lu qu'en l'absence de ce fichier. Les hypothèses sont cherchées dans `round_N/hypothesis_NNN.md` (`DiscoveryAgent/audit/data_extractor.py:266-267` « `hypothesis_file = checkpoint_dir / f"hypothesis_{pair.query_num:03d}.md"` ») alors que le flux écrit `round_N/query_00/hypothesis_000.md` ; les relectures dans `round_N/review_NNN.md` sous « Reviewer Input (Prompt) » (`DiscoveryAgent/audit/data_extractor.py:301` « `review_file = checkpoint_dir / f"review_{pair.query_num:03d}.md"` ») alors que le flux écrit `round_N/reviewer_logs/review_N.md`.
- Séparation lecture seule et exécution : sans objet dans ce dépôt (aucun agent d'audit) ; l'audit du dépôt lit les fichiers et n'écrit que son rapport.

### 2.8 L'agent d'exécution et son suivi

- **Une session neuve par requête** : la configuration fixe `execute_context_persistence` à faux (`DiscoveryAgent/tool_agents/execution_agent_cc.py:151` « `execute_context_persistence: bool = False` ») et chaque appel reconstruit la session (`DiscoveryAgent/tool_agents/execution_agent_cc.py:1639-1640` « `self.reset_conversation()` », `DiscoveryAgent/tool_agents/execution_agent_cc.py:2186-2189` « `self._init_claude_code_session()` »).
- **Options de session** : modèle de l'agent d'exécution ; outils permis lecture, écriture, édition, shell, plus recherche de fichiers et de contenu en mode sous-agents ; mode d'autorisation qui accepte les éditions (`DiscoveryAgent/tool_agents/execution_agent_cc.py:1230` « `"permission_mode": "acceptEdits",` ») ; plafond de tours seulement s'il est non nul (`DiscoveryAgent/tool_agents/execution_agent_cc.py:1244-1245` « `claude_options_kwargs["max_turns"] = self.max_turns_query_execution` »). Défaut du lanceur : aucun plafond (`DiscoveryAgent/utils/arg_parsers.py:82-84` « `0 (the default) lets it run until it finishes the task.` »).
- **Ce que reçoit l'agent** : l'invite système (orchestrateur à sous-agents dans les six configurations), la structure de code, les règles du bac à sable, puis, comme message, la description des données de la configuration (statique, non rafraîchie en mode jeu croissant) suivie de la requête du directeur (`DiscoveryAgent/tool_agents/execution_agent_cc.py:1529-1535` « `Here's a description of the dataset you're working with:` »).
- **Rapport rendu au directeur** : dans la même session, une seconde demande fait écrire un rapport dans `reports/query{N}/report.md`, relu puis supprimé (`DiscoveryAgent/tool_agents/execution_agent_cc.py:1947` « `expected_report_path = Path(self.working_directory) / "reports" / f"query{query_num}" / "report.md"` ») ; un seul réessai si le fichier manque (`DiscoveryAgent/tool_agents/execution_agent_cc.py:2006` « `Try to generate this report again` »), aucun si le modèle a refusé. La trace complète n'est pas transmise au directeur.
- **Vérification des fichiers** : après la requête, la liste des fichiers disparus depuis le démarrage est journalisée ; les fichiers modifiés ne sont pas vus (`DiscoveryAgent/tool_agents/execution_agent_cc.py:2148` « `missing_files = self.existing_files - current_files` »).
- **Compétences figées** (`--execution_skills_path`) : si des compétences sont déclarées, un crochet refuse tout outil tant que chacune n'a pas été chargée par son nom qualifié exact (`DiscoveryAgent/tool_agents/execution_agent_cc.py:686-694` « `Blocked substantive tool use until every configured execution skill is` »).
- **Suivi** : par requête, `execution_agent/tool_calls.jsonl` (entrée et sortie de chaque outil), `messages.jsonl` (chaque message du SDK), `transcript.txt` et un journal public `execution_log_NN.txt` plafonné à 8 Mio (`DiscoveryAgent/tool_agents/execution_sdk_tracker.py:27` « `EXECUTION_LOG_MAX_BYTES = 8 * 1024 * 1024` »), avec expurgation des secrets connus et des motifs de clé avant écriture.

### 2.9 Les quatre crochets de sécurité (`DiscoveryAgent/tool_agents/security/`)

Le dépôt dit lui-même que le SDK ignore une décision posée au premier niveau de la réponse d'un crochet :

Source : `DiscoveryAgent/tool_agents/security/sandbox_enforcement.py:124-130`
```text
    A prior version of this module returned ``{"permissionDecision": "deny",
    "permissionDecisionReason": reason}`` as *top-level* keys. Per the
    installed claude_agent_sdk's own type contract (``SyncHookJSONOutput`` /
    ``PreToolUseHookSpecificOutput`` in ``claude_agent_sdk/types.py``),
    ``permissionDecision`` is only recognized when nested under
    ``hookSpecificOutput``; a bare top-level ``permissionDecision`` key is not
    part of the schema and is silently dropped.
```

et l'essai du bac à sable le répète (`tests/test_sandbox_enforcement.py:6` « `top-level key is silently dropped.` »). Le format imbriqué n'apparaît que dans `sandbox_enforcement.py` et `url_blocker.py` (contrôle R14).

**1. Bac à sable** (`sandbox_enforcement.py`, agent d'exécution seulement, actif par défaut). Crochets avant outil sur Write, Edit, Read, Glob, Grep et Bash (`DiscoveryAgent/tool_agents/security/sandbox_enforcement.py:394-401` « `HookMatcher(matcher="Bash", hooks=[bash_hook]),` »), garde après outil sur Write et Edit.
- Écriture et édition directes : refusées si le chemin littéral ou le chemin résolu sort du bac (`DiscoveryAgent/tool_agents/security/sandbox_enforcement.py:307` « `if not _is_within(file_path, write_roots, strict=True):` »), avec mémoire de l'existence préalable de la cible (`DiscoveryAgent/tool_agents/security/sandbox_enforcement.py:315` « `"pre_existed": os.path.exists(abs_path),` »).
- Lecture et recherche : permises si le chemin littéral OU le chemin résolu est dans le bac ou dans une racine de lecture (`DiscoveryAgent/tool_agents/security/sandbox_enforcement.py:100-102` « `return literal_ok or real_ok` ») ; une recherche sans chemin est permise.
- Shell, motifs exacts du filtrage statique :

Source : `DiscoveryAgent/tool_agents/security/sandbox_enforcement.py:24-31`
```text
# Commands that destructively modify targets (all non-flag args are targets)
_DESTRUCTIVE_ALL_ARGS = {"rm", "rmdir", "mkdir", "touch", "chmod", "chown", "chgrp"}

# Commands where only the LAST non-flag arg is the write destination
_COPY_LIKE_COMMANDS = {"cp", "mv", "ln", "install"}

# Patterns for in-place edit flags
_INPLACE_EDIT_PATTERN = re.compile(r"\b(sed|perl|awk)\b.*\s-i\b")
```

Source : `DiscoveryAgent/tool_agents/security/sandbox_enforcement.py:42-48`
```text
_REDIRECT_PATTERN = re.compile(r"(>{1,2})\s*(\S+)")

# Pattern for tee command writing to a file
_TEE_PATTERN = re.compile(r"\btee\b(?:\s+-a)?\s+(\S+)")

# Read-oriented commands whose arguments are source paths
_READ_COMMANDS = {"cat", "head", "tail", "less", "more", "wc", "file", "stat", "md5sum", "sha256sum"}
```

  La commande est coupée sur `&&`, `||` et `;` (`DiscoveryAgent/tool_agents/security/sandbox_enforcement.py:159` « `segments = re.split(` »), les chemins relatifs résolus depuis la racine du bac (`DiscoveryAgent/tool_agents/security/sandbox_enforcement.py:374` « `cwd = tool_input.get("cwd") or sandbox_root` »), et un `cd` hors des racines est refusé (`DiscoveryAgent/tool_agents/security/sandbox_enforcement.py:238` « `cd_match = re.match(r"^cd\s+(.+)$", segment)` »).
- Garde après outil : si une écriture ou édition directe a abouti hors du bac, la cible est supprimée quand le crochet avant outil l'avait vue absente, gardée sinon (et aussi quand l'enregistrement manque), et la session est arrêtée (`DiscoveryAgent/tool_agents/security/sandbox_enforcement.py:459` « `pre_existed = record["pre_existed"] if record else True` », `DiscoveryAgent/tool_agents/security/sandbox_enforcement.py:492` « `"continue_": False,` »).
- Refus au double format, générique et imbriqué (`DiscoveryAgent/tool_agents/security/sandbox_enforcement.py:138-146` « `"permissionDecision": "deny",` »).
- **Trous visibles** : le tube `|` ne coupe pas la commande ; seule la destination de `cp`, `mv`, `ln`, `install` est contrôlée, pas la source ; les lectures par des commandes absentes de la liste (`grep`, `find`, `ls`, `python`, `awk` sans `-i`, `sort`…) ou par des jetons sans « / » ne sont pas filtrées ; les écritures faites par un programme lancé dans le shell (python, R, un script) ne sont vues par aucun crochet, ni avant ni après ; ni NotebookEdit ni WebFetch n'ont de crochet de bac ; la garde après outil ne couvre que Write et Edit ; le mode non strict des lectures accepte tout chemin dont le littéral est dans le bac, même s'il traverse un lien symbolique vers l'extérieur.

**2. Bloqueur d'URL** (`url_blocker.py`, agent d'exécution seulement, actif par défaut). Crochets avant outil sur Bash (texte de la commande) et WebFetch (adresse). Règles par défaut :

Source : `DiscoveryAgent/tool_agents/security/url_blocker.py:109-126`
```text
DEFAULT_BLOCKED_HOSTS: List[str] = [
    "marks.hms.harvard.edu",
]

DEFAULT_BLOCKED_URL_SUBSTRINGS: List[str] = [
    # ProteinGym mirrors on HuggingFace (URL form and SDK repo-id form)
    "huggingface.co/datasets/OATML-Markslab",
    "OATML-Markslab/ProteinGym",
    # ProteinGym mirrors on Zenodo (v1.0–v1.3)
    "zenodo.org/records/13932633",
    "zenodo.org/records/13936340",
    "zenodo.org/records/14997691",
    "zenodo.org/records/15293562",
    # GitHub release artifacts and raw blobs of the ProteinGym repo
    "github.com/OATML-Markslab/ProteinGym/releases",
    "github.com/OATML-Markslab/ProteinGym/raw",
    "raw.githubusercontent.com/OATML-Markslab/ProteinGym",
]
```

- Hôte : égalité ou sous-domaine ; sous-chaînes : sans casse, sur chaque URL extraite puis sur tout le texte de la commande (`DiscoveryAgent/tool_agents/security/url_blocker.py:98-101` « `folded_text = text.casefold()` »). Refus au double format.
- **Trous visibles**, dont le module convient en partie (`DiscoveryAgent/tool_agents/security/url_blocker.py:21-23` « `exfiltrate URL strings via base64, reroute through a proxy, or bounce off a` ») : une adresse écrite dans un fichier (outil Write) puis exécutée par `python fichier.py` n'apparaît pas dans le texte de la commande ; `git clone` du dépôt GitHub de ProteinGym n'est pas couvert (seuls `/releases` et `/raw`) ; les formes `zenodo.org/record/…` (singulier), `zenodo.org/api/records/…` et les DOI Zenodo ne sont pas couvertes ; les règles ne visent que ProteinGym ; aucun autre outil n'est inspecté ; les agents recensement et OpenTargets n'ont pas ce crochet.

**3. Protection d'écriture** (`write_protection.py`, agent OpenTargets seulement, protège le dossier des données OpenTargets). Mêmes motifs que le bac à sable (destructrices, copie, édition en place, redirection, `tee`) plus `cd` dans un chemin protégé (`DiscoveryAgent/tool_agents/security/write_protection.py:69-73` « `return f"Blocked: 'cd' into protected path {target}"` »), sur Write, Edit et Bash.
- Refus posé au premier niveau, sans `hookSpecificOutput` (`DiscoveryAgent/tool_agents/security/write_protection.py:158-161` « `"permissionDecision": "deny",` ») : selon le dépôt lui-même, ce format est ignoré par le SDK.
- Les chemins relatifs sont résolus contre le répertoire du processus Python quand l'outil ne donne pas de `cwd` (`DiscoveryAgent/tool_agents/security/write_protection.py:174` « `cwd = tool_input.get("cwd", None)` »), piège que le bac à sable décrit et corrige pour lui-même (`DiscoveryAgent/tool_agents/security/sandbox_enforcement.py:368-374` « Python process's cwd (the agent repo) and reject every relative »).
- Aucun essai ne l'éprouve. Mêmes trous de filtrage que le bac à sable.

**4. Protection des processus** (`kill_blocker.py`, outil Bash de l'agent d'exécution et de l'agent OpenTargets : `DiscoveryAgent/tool_agents/execution_agent_cc.py:1043` « `HookMatcher(matcher="Bash", hooks=[process_protection_hook]),` », `DiscoveryAgent/tool_agents/specialized/opentargets_agent.py:142` « `HookMatcher(matcher="Bash", hooks=[process_protection_hook]),` »). Motifs exacts, cherchés sans casse :

Source : `DiscoveryAgent/tool_agents/security/kill_blocker.py:17-27`
```text
    dangerous_patterns = [
        r"pkill\s+python", 
        r"killall\s+python", 
        r"kill\s+-\d+\s+-1", 
        r"kill\s+0",
        # Additive coverage for common variants that bypass the simpler patterns.
        r"\bpkill\b(?:\s+-\S+)*\s+(?:-\S+\s+)*python[0-9.]*\b",
        r"\bpkill\b(?:\s+-\S+)*\s+-f\s+['\"]?.*python[0-9.]*.*['\"]?",
        r"\bkillall\b(?:\s+-\S+)*\s+python[0-9.]*\b",
        r"\bpgrep\b(?:\s+-\S+)*\s+.*python[0-9.]*.*\|\s*xargs\s+kill(?:\s+-\d+)?\b",
    ]
```

Sur une correspondance, la commande n'est pas refusée mais réécrite :

Source : `DiscoveryAgent/tool_agents/security/kill_blocker.py:31-45`
```text
            # Deterministic Fix: Rewrite the command to exclude the agent's PID
            safe_command = (
                f"pgrep -f python | "
                f"awk '$1 != {agent_pid} && $1 != {parent_pid}' | "
                f"xargs -r kill -9"
            )
            
            return {
                "permissionDecision": "allow",
                "updatedInput": {**tool_input, "command": safe_command},
                "additionalContext": (
                    "NOTE: I intercepted a broad kill command. "
                    f"I have rewritten it to protect process PIDs {agent_pid} and {parent_pid}."
                )
            }
```

Seul refus :

Source : `DiscoveryAgent/tool_agents/security/kill_blocker.py:47-52`
```text
    # 2. Block specific destructive commands entirely
    if "rm -rf /" in command or "chmod -R 000" in command:
        return {
            "permissionDecision": "deny",
            "permissionDecisionReason": "This command is classified as high-risk for system stability."
        }
```

- Les deux identifiants protégés sont ceux du processus Python orchestrateur et de son parent (`DiscoveryAgent/tool_agents/security/kill_blocker.py:12-13` « `parent_pid = os.getppid()` »).
- **Trous visibles** : la réécriture vise tous les processus python de la machine sauf deux, ce qui est plus large que la commande d'origine pour les deux motifs généraux (`kill 0`, `kill -9 -1`) et pour les arrêts ciblés ; décisions posées au premier niveau, format que le dépôt dit ignoré, de sorte que la réécriture comme le refus dépendent de la lecture qu'en fait le SDK ; la sous-chaîne `rm -rf /` attrape toute suppression récursive d'un chemin absolu et manque `rm -fr /` ou `rm -r -f /` ; les variantes hors motifs passent (substitution `$(pgrep …)`, `kill -- -1`, `kill -s KILL -1`, arrêts par nom d'autres programmes) ; rien ne vise les commandes longues ; aucun essai.

### 2.10 Les refus du modèle et les appels partiels

- **Détection d'un refus** : `stop_reason == "refusal"` (`DiscoveryAgent/utils/llm_diagnostics.py:141` « `if getattr(response, "stop_reason", None) != "refusal":` »), traduit en avis « [REFUSAL] … » avec la catégorie et le conseil de relancer ; le directeur et l'agent d'hypothèse gardent le dernier avis (`DiscoveryAgent/hyp_agents/director_agent.py:433` « `self.last_refusal = refusal_notice(response)` »).
- **Directeur** : une sortie sans balise est d'abord testée comme refus (`DiscoveryAgent/director_workflow.py:1021` « `refusal = first_refusal(self.director_agent)` »). Refus : événement `model_refusal` et nouvel essai sans consigne (« Nothing was malformed »). Sortie malformée : nouvel essai avec la consigne « SHORTER ». Au-delà de trois réessais : arrêt du tour avec un événement `early_stopping`, puis rapport. Un refus du rapport final fait retomber sur le rapport cumulé.
- **Agent d'exécution** : une issue inutilisable est classée sans recopier son contenu (vide, réponse finale manquante, refus, rapport absent ou malformé, exception du SDK : `DiscoveryAgent/tool_agents/execution_agent_cc.py:210` « `if "refusal" in metadata or "refused" in metadata:` ») ; l'exception remonte et le tour échoue.
- **Appel partiel** : l'entrée de chaque requête est écrite avant l'envoi, le rapport dès qu'il existe, de façon atomique et idempotente (`DiscoveryAgent/utils/query_artifacts.py:91` « `query artifact already exists with different content` »). À la reprise en cours de tour, la première requête non terminée n'est pas redemandée au directeur : son rapport est rejoué s'il existe, sinon son entrée exacte est renvoyée à l'agent identifié par `query_status.json` ou par son journal d'exécution (`DiscoveryAgent/director_workflow.py:643` « `It never asks the Director to invent a replacement.` ») ; sans identité récupérable, la reprise échoue avant tout appel (`DiscoveryAgent/director_workflow.py:655` « `has persisted input but its helper identity cannot be recovered` »).
- Essais qui l'éprouvent : `tests/test_refusal_workflow.py` et `tests/test_partial_query_resume.py` (section 7).
## 3. Le papier contre le code

### 3.1 Table à trois colonnes (Méthodes 4.1 à 4.11, pages 25 à 31 ; notes 1 à 3, 12 à 17 et 41 à 45 de l'annexe)

| Mécanisme | Ce que dit le texte | Ce que fait le code | Écart |
|---|---|---|---|
| Deux boucles | (papier p. 25 « The system is built from two nested loops. ») | `DiscoveryAgent/hypothesis_brancher.py:575` « `for round_idx in range(start_round, end_round):` » ; `DiscoveryAgent/director_workflow.py:917` « `while query_num <= self.max_queries:` » | Aucun. |
| Mode autonome | (papier p. 25 « iterates until its budget is exhausted ») | `DiscoveryAgent/hypothesis_brancher.py:536` « `end_round = start_round + self.num_rounds` » | Aucun ; le budget de tours vaut par invocation du lanceur. |
| Entrées du directeur | (papier p. 25 « an LLM prompted with the dataset description, the current hypothesis, a catalog of available tool agents, and the report accumulated so far in the round ») | `DiscoveryAgent/hyp_agents/director_agent.py:580-587` « `turn_prompt += REPORT_MULTITURN_PROMPT.format(` » ; `DiscoveryAgent/hyp_agents/director_agent.py:271-272` « `# Helper Agents` » | Partiel : chaque tour de parole n'injecte que le rapport de la dernière requête (`DiscoveryAgent/director_workflow.py:1236-1237` « `self.report = f"` »), les précédents restent dans la conversation ; la mémoire est donnée aussi ; la tâche ne l'est jamais (R10). |
| Deux budgets | (papier p. 25 « a per-round query budget controls how deeply each hypothesis is pursued, and a round budget controls how many hypotheses are pursued in sequence ») | `DiscoveryAgent/utils/arg_parsers.py:80` « `"--num_queries", type=int, default=5` » ; `DiscoveryAgent/utils/arg_parsers.py:49` « `"--num_rounds", type=int, default=None` » | Aucun. |
| Format d'un appel | (papier p. 25 « natural-language rationale followed by a single tool agent invocation ») | `DiscoveryAgent/prompts/hyp_generation.py:65-71` « `<[helper agent tag]>` » ; `DiscoveryAgent/director_workflow.py:1000` « `re.search(r'<(\w+)>([\s\S]*?)</\1>', query, re.DOTALL)` » | Aucun ; seule la première balise de la sortie est exécutée. |
| Un agent par requête | (papier p. 25 « invokes exactly one tool agent per query ») | `DiscoveryAgent/hyp_agents/director_agent.py:75` « `You may only submit one query to one of the helper agents per step.` » | Aucun. |
| Arrêt anticipé | (papier p. 25 « output once it judges the hypothesis sufficiently explored ») | `DiscoveryAgent/director_workflow.py:986` « `if self.allow_director_to_stop and ("<<STOP>>" in query):` » | Aucun. |
| Restriction à l'hypothèse | (papier p. 25 « we restrict the director to executing only analyses explicitly related to the round's hypothesis and guidance ») | `DiscoveryAgent/hyp_agents/director_agent.py:112` « `Do NOT deviate from the hypothesis to explore tangential questions` » | Aucun (par consigne). |
| Compaction | (papier p. 26 « Once its estimated input length crosses a threshold, earlier turns are replaced by a model-generated summary ») | `DiscoveryAgent/hyp_agents/director_agent.py:380-386` « `"trigger": {"type": "input_tokens", "value": self.compaction_trigger_tokens},` » | Précision : faite par l'API, réservée à un directeur claude-opus-4-6 (`DiscoveryAgent/hyp_agents/director_agent.py:308` « `'claude-opus-4-6' in self.llm_config.model_name` »). |
| Repli sur débordement | (papier p. 26 « The same mechanism is triggered as a fallback when a context-overflow error is returned mid-query ») | `DiscoveryAgent/hyp_agents/director_agent.py:441-449` « `self.compaction_trigger_tokens = 50000` » | Aucun ; seulement quand la compaction est inactive, comme le précise la note 42. |
| Recherche web | (papier p. 26 « performs a single-shot search using the underlying model's native web-search capability ») | `DiscoveryAgent/tool_agents/single_search.py:79-83` « `"type": "web_search_20250305",` » | Aucun ; trois recherches au plus par appel. |
| Recherche approfondie | (papier p. 26 « returns a structured report with an executive summary, key findings, a methodology note, limitations, and a list of sources ») | `DiscoveryAgent/tool_agents/deep_research.py:19-27` « `"## Executive Summary\n"` » | Aucun sur la forme ; le plafond de sortie configuré n'est pas envoyé (`DiscoveryAgent/tool_agents/deep_research.py:94-97` « `"model": "sonar-deep-research",` ») ; une erreur revient au directeur comme texte (`DiscoveryAgent/tool_agents/deep_research.py:111` « `message = f"Error during deep research: {error}"` »). |
| Rapport de fond comme contexte | (papier p. 26 « provided as context during hypothesis generation ») | `DiscoveryAgent/hyp_agents/hypothesis_gen_agent.py:129-132` « `self.background_literature_content = f.read()` » | **Écart** : lu, jamais injecté dans une invite (R04). |
| Fond tiré de PDF fournis | (papier p. 26 « summarizes and synthesizes without drawing on outside sources ») | `DiscoveryAgent/director_workflow.py:88` « `Do not perform web search. Do not rely on outside knowledge.` » | Aucun pour la production ; même écart d'usage qu'à la ligne précédente. |
| Session autonome par appel | (papier p. 26 « Each invocation is a self-contained session ») | `DiscoveryAgent/tool_agents/execution_agent_cc.py:1639-1640` « `self.reset_conversation()` » | Aucun. |
| Résumé concis | (papier p. 26 « returns only a concise summary of what it did and found ») | `DiscoveryAgent/tool_agents/execution_agent_cc.py:1947` « `"report.md"` » | Aucun ; le fichier du rapport est ensuite supprimé de l'espace de travail. |
| Crochets avant outil | (papier p. 27 « pre-tool hooks constrain direct file operations and screen common shell access patterns ») | `DiscoveryAgent/tool_agents/security/sandbox_enforcement.py:394-401` « `HookMatcher(matcher="Write", hooks=[write_edit_hook]),` » | Aucun ; trous visibles en 2.9. |
| Garde après outil | (papier p. 27 « a post-tool guard terminates sessions after detected out-of-sandbox writes or edits ») | `DiscoveryAgent/tool_agents/security/sandbox_enforcement.py:491-494` « `"continue_": False,` » | Aucun. |
| Crochet d'URL | (papier p. 27 « a targeted URL hook blocks known ProteinGym result sources ») | `DiscoveryAgent/tool_agents/security/url_blocker.py:109-111` « `"marks.hms.harvard.edu",` » | Aucun. |
| Trois phases d'un tour | (papier p. 27 « a hypothesis is selected and used to condition the director ») | `DiscoveryAgent/hypothesis_brancher.py:731-734` « `exploratory_mode=is_exploratory_round` » ; `DiscoveryAgent/hypothesis_brancher.py:796` « `self.results_memory.update_report(final_report, verbose=False)` » | Aucun. |
| Remise à zéro entre tours | (papier p. 27 « Between rounds the in-round conversation is reset ») | `DiscoveryAgent/director_workflow.py:1801` « `self.director_agent.reset_conversation()` » ; `DiscoveryAgent/hypothesis_brancher.py:656` « `workflow.background_report = accumulated_report` » | Aucun. |
| Mode automatique | (papier p. 27 « proposes a single hypothesis—a statement with a justification grounded in the literature or in the accumulated memory, and an optional plan for testing it ») | `DiscoveryAgent/prompts/hyp_generation.py:151-154` « `**Hypothesis**: [Your hypothesis]` » | **Écart** : pas de plan (R05) ; la littérature du rapport de fond n'est pas fournie (R04), seule la mémoire l'est. |
| Mode pilotage | (papier p. 27 « the generated hypotheses are handed to a human scientist ») | `DiscoveryAgent/hypothesis_brancher.py:676-681` « `workflow.hypothesis_config.selected_hypothesis_file = str(prev_round_path)` » | **Écart** : aucun candidat généré ; le scientifique écrit `selected_hypothesis.md` à la main ; la branche de pause est morte (R06). |
| Tours exploratoires | (papier p. 27 « the first few rounds can be run in an exploratory mode ») | `DiscoveryAgent/hypothesis_brancher.py:719-723` « `round_idx < self.num_exploration_rounds and` » | Aucun dans le code ; les configurations s'écartent de la table 35 (dernière ligne). |
| Intégrateur | (papier p. 28 « An integrator merges the accumulated memory with the new report with completeness as its explicit objective ») | `DiscoveryAgent/memory/results_memory.py:34` « `Your goal is COMPLETENESS, not conciseness.` » | Aucun. |
| Analyseur | (papier p. 28 « assigns each a risk level (low, medium, or high) ») | `DiscoveryAgent/memory/results_memory.py:116-119` « `- LOW: Exact duplicates with no loss of information if merged` » | Aucun. |
| Raffineur | (papier p. 28 « A refiner applies only the low-risk consolidations, verifying that information flagged as critical is preserved ») | `DiscoveryAgent/memory/results_memory.py:151` « `Your task: Carefully consolidate ONLY the low-risk redundancies.` » | **Écart** : filtrage et vérification demandés par consigne, pas faits par le code ; la consigne demande aussi d'élaguer (2.4). |
| Injection de la mémoire | (papier p. 28 « This memory is injected into the director and the hypothesis-generation agent at the start of each round ») | `DiscoveryAgent/hyp_agents/director_agent.py:589` « `if background_report and (not self.background_report_read):` » ; `DiscoveryAgent/hyp_agents/hypothesis_gen_agent.py:311` « `if background_report and (not self.background_report_read):` » | Aucun. |
| Mémoire procédurale | (papier p. 28 « The active memory component is a short markdown file to orient the execution agent ») ; (papier p. 28 « The passive memory component is a longer documentation file that can be accessed on-demand ») | `DiscoveryAgent/prompts/cc_sub_agents.py:63-76` « `"claude_md_agent": AgentDefinition(` » | Aucun sur le principe ; voir la note 3 plus bas. |
| Relecture à fréquence configurable | (papier p. 28 « injects an automated reviewer into the research loop at a configurable query frequency ») | `DiscoveryAgent/director_workflow.py:1149` « `if (self.review_optimization_steps is not None):` » | **Écart** : avec les six configurations publiées, jamais déclenchée (2.5 ; R01 à R03). |
| Entrée du relecteur | (papier p. 28 « the round's cumulative report is passed to a reviewer LLM that produces a critique focused on novelty, rigor, and direction ») | `DiscoveryAgent/director_workflow.py:1292` « `{self.cumulative_report}` » | Aucun ; il reçoit aussi la description et la mémoire. |
| Retour au directeur | (papier p. 28 « the critique is fed back to the director as feedback that shapes the next query ») | `DiscoveryAgent/director_workflow.py:1165` « `feedback = self.get_feedback()` » ; `DiscoveryAgent/hyp_agents/director_agent.py:630-632` « `Use this feedback to improve your research.` » | Aucun. |
| Pas de relecture en exploration | (papier p. 28 « During exploratory rounds, we omit the reviewer ») | `DiscoveryAgent/director_workflow.py:577-578` « `if self.explicit_hypothesis_step is None:` » | **Écart** : la retenue ne lit pas le mode du tour ; telle que configurée, elle supprime toute relecture. |
| Relecteur avec recherche web | (papier p. 28 « The reviewer can optionally be granted web-search access ») | `DiscoveryAgent/tool_agents/base_llm_with_search.py:46-50` « `"max_uses": self.max_web_searches,` » | Aucun. |
| Concepteur de relecture | (papier p. 28 « generates a task-specific reviewer prompt at the start of each run ») | `DiscoveryAgent/director_workflow.py:459` « `generated_reviewer_prompt = review_designer.design_reviewer_prompt(` » | Aucun ; « chaque course » = chaque construction du workflow. |
| Invite du relecteur gardée | (papier p. 28 « The generated prompt is checkpointed with the rest of the run configuration ») | `DiscoveryAgent/checkpoint_manager.py:423` « `markdown_path = save_dir / "reviewer_prompt.md"` » ; `DiscoveryAgent/checkpoint_manager.py:156` « `'generated_reviewer_prompt': getattr(self.workflow, 'generated_reviewer_prompt', None),` » | Écart de lieu : à la racine `checkpoints/`, réécrite à chaque lancement (2.6). |
| Candidats proposés | (papier p. 29 « proposes a configurable set of candidate directions grounded in the evidence accumulated so far ») | aucun code ; une seule hypothèse : `DiscoveryAgent/hyp_agents/hypothesis_gen_agent.py:354` « `hypothesis_prompt = prefix_prompt + HYPOTHESIS_GENERATION_PROMPT` » | **Hors dépôt** (application de pilotage). |
| Révision des candidats | (papier p. 29 « 2) editing it directly, 3) asking the hypothesis-generation agent to revise or regenerate it from written feedback, or 4) replacing it with a custom hypothesis ») | aucun code | **Hors dépôt**. |
| Hypothèse choisie injectée | (papier p. 29 « with an explicit instruction to test the scientist-supplied hypothesis ») | `DiscoveryAgent/hyp_agents/director_agent.py:163-169` « `Consider their advice to be gold-standard.` » | Aucun. |
| Point de contrôle par requête | (papier p. 29 « each query has its own JSON checkpoint of the full workflow state ») | `DiscoveryAgent/checkpoint_manager.py:258` « `checkpoint_path = checkpoint_dir / "checkpoint.json"` » | Léger : la configuration de la course n'y figure que par quatre drapeaux (2.6). |
| Rendu lisible par requête | (papier p. 29 « together with a human-readable Markdown rendering of the query and its result ») | `DiscoveryAgent/utils/query_artifacts.py:72` « `return f"query_{role}_{query_suffix(query_num)}.md"` » | Aucun (deux fichiers : entrée et rapport). |
| Pièces par tour | (papier p. 29 « Each round additionally writes its starting configuration, its report before and after memory integration, its log, any generated reviewer prompt ») | `DiscoveryAgent/checkpoint_manager.py:536` « `"round_report.md"` » ; `DiscoveryAgent/checkpoint_manager.py:629` « `dest_log = save_dir / "round.log"` » | Écart : l'invite du relecteur n'est pas écrite par tour ; aucune liste de candidats n'est écrite par ce dépôt. |
| Commits par tour et requête | (papier p. 29 « changes are committed as the run proceeds with messages that tag each commit by round and query ») | `DiscoveryAgent/utils/git_version_control.py:351` « `full_message = f"[Round {round_num}] {message}` » | Aucun. |
| Reprise d'un tour incomplet | (papier p. 30 « an incomplete round instead restores the most recent query checkpoint ») | `DiscoveryAgent/hypothesis_brancher.py:556` « `restored_workflow = self._restore_workflow_from_checkpoint(` » | Aucun ; la reprise descend jusqu'à la requête interrompue (2.10). |
| Chaîne d'audit | (papier p. 30 « An audit pipeline consumes the per-query checkpoints and renders a run as a navigable ») | `scripts/utils/audit_run.py:198-215` « `discovery = CheckpointDiscovery(str(checkpoint_path))` » | Partiel : résumés par Haiku ; lecteurs désaccordés des fichiers écrits (2.7). |
| Auditeur en lecture seule | (papier p. 30 « Its tool allow-list contains only file reading, content search, globbing, and shell commands ») | aucun code (R13) | **Hors dépôt**. |
| Auditeur avec exécution | (papier p. 30 « The execution-enabled configuration additionally receives write and execute permissions ») | aucun code | **Hors dépôt**. |
| Agent recensement | (papier p. 31 « exposes three public-use data backends through a single search-then-download interface ») | `DiscoveryAgent/tool_agents/specialized/census_agent.py:124` « `result = self._run_coro(self._acs_agent.chat(query))` » ; `acs_agent/agent.py:128` « `MODEL = "claude-opus-4-6"` » | Aucun ; modèle codé en dur, 25 tours d'outils au plus (`acs_agent/agent.py:130` « `MAX_TOOL_ROUNDS = 25` »). |
| Agent OpenTargets | (papier p. 31 « a write-protection hook prevents it from modifying the shared source, and a process-control hook blocks long-running or destructive commands ») | `DiscoveryAgent/tool_agents/specialized/opentargets_agent.py:135-143` « `write_protection_hooks = create_write_protection_hook(` » | **Écart** : les deux crochets posent leur décision au premier niveau, format que le dépôt dit ignoré ; rien ne vise les commandes longues ; ni bac à sable ni bloqueur d'URL (2.9). |
| Modèles des composants | (papier p. 31 « components were configured with Claude Opus 4.6 ») | `configs/paper/dms_auto.yaml:8` « `director_model: "claude-opus-4-6"` » | Aucun (six configurations, section 5). |
| Exécution ProteinGym | (papier p. 31 « the ProteinGym configuration uses Sonnet 4.6 ») | `configs/paper/dms_steer.yaml:11` « `execution_model: "claude-opus-4-6"` » ; `configs/paper/dms_auto.yaml:11` « `execution_model: "claude-sonnet-4-6"` » | **Écart** pour DA-Steer : la configuration de départ dit Opus 4.6, comme la table 35 de l'annexe pour ses tours 0 à 7. |
| Plafonds de requêtes | (papier p. 31 « Query caps are 10 per round for StarEmbed, ProteinGym, and extragalactic astronomy, and 25 for economics and functional genomics ») | `configs/paper/acs_select.yaml:28` « `num_queries: 25` » ; `configs/paper/starembed_auto.yaml:25` « `num_queries: 10` » | Aucun. |
| Note 1 : chemins littéral et résolu | (annexe p. 2 « using both literal and symlink-resolved paths ») | `DiscoveryAgent/tool_agents/security/sandbox_enforcement.py:100-101` « `return literal_ok and real_ok` » | Aucun. |
| Note 1 : sessions fraîches | (annexe p. 2 « each query rebuilds a fresh session ») | `DiscoveryAgent/tool_agents/execution_agent_cc.py:2184-2188` « `self._init_claude_code_session()` » | Aucun. |
| Note 1 : rapport écrit puis relu | (annexe p. 2 « a short Markdown report of what it did and found to a report file, which is then read back and returned ») | `DiscoveryAgent/tool_agents/execution_agent_cc.py:77` « `output it into a file at {report_path}` » | Aucun. |
| Note 1 : cibles neuves supprimées | (annexe p. 2 « removes newly created external targets when their prior state is known ») | `DiscoveryAgent/tool_agents/security/sandbox_enforcement.py:474-479` « `shutil.rmtree(abs_path)` » | Aucun. |
| Note 1 : tours bornés | (annexe p. 2 « A bounded number of turns per session caps the work done within a single query ») | `DiscoveryAgent/tool_agents/execution_agent_cc.py:1244-1245` « `if self.max_turns_query_execution:` » | Le défaut du lanceur n'a pas de plafond (`DiscoveryAgent/utils/arg_parsers.py:82` « `"--execution_max_turns", type=int, default=0` ») ; les six configurations en fixent un (30 à 60). |
| Note 2 : premier rapport | (annexe p. 3 « The first round report initializes the empirical memory ») | `DiscoveryAgent/memory/results_memory.py:444-448` « `# First report - just store it` » | Aucun. |
| Note 2 : structure intégrée | (annexe p. 3 « organized as background, data characteristics, experiments and analyses, and discussion ») | `DiscoveryAgent/memory/results_memory.py:56-71` « `# Data Characteristics` » | Aucun ; le raffineur impose un premier titre différent (`DiscoveryAgent/memory/results_memory.py:168` « `# Background and Literature Review` »). |
| Note 2 : mémoire sauvegardée | (annexe p. 3 « saved in the round checkpoint as memory_report.md ») | `DiscoveryAgent/checkpoint_manager.py:589` « `"memory_report.md"` » | Aucun. |
| Note 2 : mémoire à la reprise | (annexe p. 3 « the latest completed memory report seeds the same memory manager ») | `DiscoveryAgent/hypothesis_brancher.py:156` « `self.results_memory.current_report = seed_content` » | Léger : le fichier entier, en-têtes compris (R08). |
| Note 2 : requêtes seules pour l'exécution | (annexe p. 3 « the execution agents receive only the specific queries dispatched by the director ») | `DiscoveryAgent/tool_agents/execution_agent_cc.py:1529-1535` « `Here's a description of the dataset you're working with:` » | Léger : l'agent reçoit aussi la description des données. |
| Note 3 : deux agents de documentation | (annexe p. 4 « A claude_md_agent revises CLAUDE.md ») | `DiscoveryAgent/prompts/cc_sub_agents.py:71-75` « `"claude_md_agent": AgentDefinition(` » | Aucun. |
| Note 3 : édition limitée | (annexe p. 4 « Both documentation agents read the shared workspace but can edit only their assigned document ») | `DiscoveryAgent/prompts/cc_sub_agents.py:74` « `tools=["Read", "Edit", "Glob", "Grep"],` » | **Écart** : limite par consigne seulement, et seulement pour DOCUMENTATION.md ; marqueurs de chemin non remplacés (2.4). |
| Note 12 : interface d'audit | (annexe p. 17 « it provided no file-writing, editing, or web-fetch tools ») | aucun code | **Hors dépôt**. |
| Notes 13 à 15 : banc des affirmations corrompues | (annexe p. 18 « we extracted exactly 50 claims ») | aucun code | **Hors dépôt**. |
| Note 16 : étude humaine | (annexe p. 21 « The study included eight participants, four in the Audit cohort and four in the Code cohort ») | aucun code | **Hors dépôt**. |
| Note 17 : outils filtrés | (annexe p. 22 « file globbing, content search, and shell commands ») | `DiscoveryAgent/tool_agents/security/sandbox_enforcement.py:394-401` « `HookMatcher(matcher="Grep", hooks=[search_hook]),` » | Aucun. |
| Note 17 : filtrage du shell | (annexe p. 22 « best-effort static screening of output redirection, tee, in-place edits, selected file-modifying commands, and common file-reading commands ») | `DiscoveryAgent/tool_agents/security/sandbox_enforcement.py:48` « `_READ_COMMANDS = {"cat", "head", "tail", "less", "more", "wc", "file", "stat", "md5sum", "sha256sum"}` » | Aucun ; trous visibles en 2.9. |
| Note 17 : double format de refus | (annexe p. 22 « returned through both the SDK's generic block response ») | `DiscoveryAgent/tool_agents/security/sandbox_enforcement.py:138-146` « `"decision": "block",` » | Aucun pour les crochets de fichiers ; ni la protection des processus ni la protection d'écriture n'ont ce format (R14). |
| Note 17 : protection des processus | (annexe p. 22 « screens a narrow set of broad process-killing and destructive command patterns ») | `DiscoveryAgent/tool_agents/security/kill_blocker.py:38-40` « `"permissionDecision": "allow",` » | **Écart** : réécrit la commande au lieu de la refuser ; décision au premier niveau (2.9). |
| Note 17 : adresses et texte | (annexe p. 22 « the hook extracts literal HTTP and HTTPS addresses and also scans the complete command text ») | `DiscoveryAgent/tool_agents/security/url_blocker.py:93-101` « `for url in _extract_urls(text):` » | Aucun. |
| Note 17 : règles par défaut | (annexe p. 22 « ProteinGym records 13932633, 13936340, 14997691, and ») | `DiscoveryAgent/tool_agents/security/url_blocker.py:118-121` « `"zenodo.org/records/15293562",` » | Aucun. |
| Note 17 : initialisation journalisée | (annexe p. 22 « session initialization records the active configuration in the action log ») | `DiscoveryAgent/tool_agents/execution_agent_cc.py:1124-1128` « `"url_blocker_init",` » | Aucun. |
| Note 17 : existence préalable | (annexe p. 22 « records whether an out-of-sandbox target existed before the attempted operation ») | `DiscoveryAgent/tool_agents/security/sandbox_enforcement.py:313-316` « `"pre_existed": os.path.exists(abs_path),` » | Aucun. |
| Note 17 : session arrêtée | (annexe p. 23 « terminates the execution session and records the event ») | `DiscoveryAgent/tool_agents/security/sandbox_enforcement.py:486-492` « `logger.log_action("sandbox_posttool_escape", reason)` » | Aucun. |
| Note 17 : retour en arrière | (annexe p. 23 « The outer loop identifies the highest completed round from its integrated memory report ») | `DiscoveryAgent/hypothesis_brancher.py:251-252` « `return max(completed_rounds)` » | Aucun ; le reste du retour en arrière (remise à un commit, élagage de l'historique, quarantaine) n'a pas d'outil dans le dépôt. |
| Note 41 : une hypothèse sans juge | (annexe p. 67 « passed directly to the director without a judge ») | `DiscoveryAgent/director_workflow.py:966` « `target_hypothesis=hypothesis_output,` » | Aucun. |
| Note 41 : modèle des sous-agents | (annexe p. 67 « agents inherit from it ») | `DiscoveryAgent/tool_agents/execution_agent_cc.py:236` « `return "inherit"` » | Aucun. |
| Note 41 : trois recherches web | (annexe p. 67 « a cap of three web searches per call ») | `DiscoveryAgent/utils/agent_config_builders.py:78` « `max_web_searches=3,` » | Aucun. |
| Note 41 : modèle de résumé désactivé | (annexe p. 67 « A report-summarization model exists but was disabled in every experiment reported here ») | `DiscoveryAgent/tool_agents/execution_agent_cc.py:64-66` « `Your job is to generate a concise summary of the agent's findings` » | Aucun : l'invite existe, sans chemin pour l'activer (R11). |
| Note 41 : seuil de compaction | (annexe p. 67 « configured to trigger at 150,000 estimated input tokens ») | `DiscoveryAgent/utils/arg_parsers.py:201` « `"--compaction_trigger_tokens", type=int, default=150000` » | Aucun ; la classe de `config.py` porte 190 000, inutilisé par le lanceur (`DiscoveryAgent/config.py:285` « `compaction_trigger_tokens: int = 190000` »). |
| Note 42 : condition | (annexe p. 68 « gated on an Anthropic Claude Opus 4.6 director and the per-run enable setting ») | `DiscoveryAgent/hyp_agents/director_agent.py:305-309` « `getattr(self.config, 'enable_compaction', False)` » | Aucun. |
| Note 42 : seuil minimal sur débordement | (annexe p. 68 « it enables compaction at the minimum 50,000-token threshold and retries the request ») | `DiscoveryAgent/hyp_agents/director_agent.py:449` « `self.compaction_trigger_tokens = 50000` » | Aucun. |
| Note 42 : ce que garde le résumé | (annexe p. 68 « (v) any data file paths or column names ») | `DiscoveryAgent/hyp_agents/director_agent.py:226` « `(5) any data file paths or column names referenced.` » | Aucun. |
| Note 43 : relectures comptées | (annexe p. 69 « Reviewer invocations are recorded per campaign in the action logs: 9 for StarEmbed, 42 for DA-Steer, 78 for economics, and 132 ») ; (annexe p. 70 « despite a configured review interval ») | `DiscoveryAgent/director_workflow.py:1157-1159` « `elif self.hold_reviews_in_exploratory_phase:` » | **Écart** : avec les configurations publiées, le code n'appelle jamais le relecteur. |
| Note 43 : fond au tour 0 | (annexe p. 70 « A round-0 deep-research background report was generated for every campaign ») | `configs/paper/dms_auto.yaml:14` « `generate_background_report: true` » | Aucun pour la génération ; non utilisé par les invites (R04). |
| Note 44 : états avec empreinte | (annexe p. 71 « the serialized state of the director, the hypothesis-generation agent, and the registered tool agents (each with an integrity hash) ») | `DiscoveryAgent/checkpoint_manager.py:199-206` « `'state_hash': self._compute_state_hash(agent_state)` » | Aucun ; le directeur figure deux fois (alias hérité). |
| Note 44 : plafond de taille | (annexe p. 71 « skipping files above a size cap ») | `DiscoveryAgent/utils/git_version_control.py:251-252` « `if abs_path.stat().st_size > self.max_stage_file_size_bytes:` » | Aucun (50 Mo). |
| Note 45 : candidats en un appel | (annexe p. 72 « the hypothesis-generation agent produces all candidates in one model call ») | aucun code | **Hors dépôt**. |
| Note 45 : exploration désactivée | (annexe p. 72 « The director workflow disables exploratory execution when a selection is present ») | `DiscoveryAgent/hypothesis_brancher.py:722` « `not has_selected_hypothesis` » | Aucun. |
| Note 45 : invite de sélection humaine | (annexe p. 72 « inserts the full text into a human-selection prompt on the first query ») | `DiscoveryAgent/hyp_agents/director_agent.py:599-602` « `TARGET_HYPOTHESIS_HUMAN_SELECTION_PROMPT.format(` » | Aucun. |
| Table 35 : tours exploratoires | (annexe p. 115 « Configured exploratory rounds ») | `configs/paper/acs_select.yaml:26` « `num_exploration_rounds: 0` » ; `configs/paper/gw_cd4_select.yaml:26` « `num_exploration_rounds: 0` » ; dms_steer sans la clé (R12) | **Écart** : la table dit 1 pour les six campagnes. |

### 3.2 Ce que le papier décrit et qui n'est pas dans ce dépôt

- **L'application de pilotage** : génération d'un ensemble de candidats en un appel, révision, régénération d'un candidat ou de l'ensemble, conversations sur les rapports, assistant de code et navigateur de points de contrôle en lecture seule, rôles d'accès (notes 12 et 45). Le README l'écarte (`README.md:274-281` « `The scientist steering web application` ») ; l'annexe parle d'une version locale publiée à part (annexe p. 72 « we have also released a local version »). Seules traces dans ce dépôt : des fichiers d'état « pour un frontal » (`DiscoveryAgent/utils/progress_recorder.py:4-5` « `round_activity.jsonl) for the frontend Round Monitor to consume.` ») et une disposition `code/` et `checkpoint/checkpoints/round_N/` attendue par les compétences figées (`DiscoveryAgent/tool_agents/execution_agent_cc.py:285-290` « `working_directory.name == "code"` »).
- **Les agents d'audit à outils**, en lecture seule et avec exécution, et le harnais Codex (4.9) ; le dépôt n'a qu'un script qui résume chaque requête par Haiku (2.7).
- **Le banc des affirmations corrompues** (notes 13 à 15) : extraction des 50 affirmations, catalogue de huit corruptions, auditeurs, notation, témoin sans trace.
- **L'étude humaine** (notes 16 et 49) : protocole, formulaires, appariement des erreurs.
- **Les traces des courses** : points de contrôle, espaces de travail et leur historique git, code, modèles et rapports produits par les agents (`README.md:277` « `Code, models and reports the execution agent produced during the campaigns.` ») ; les jeux de données, l'image de conteneur et l'environnement Slurm (`README.md:276` « `Datasets, API credentials, the HPC container image and Slurm environment.` ») ; les ressources de domaine (`README.md:280-281` « `Open Targets data and its loader package, the Dwarf` »).
- **Les opérations du retour en arrière après la fuite ProteinGym** (note 17 : remise à un commit, élagage de l'historique, quarantaine) : aucun outil.
- **L'étape d'agrégation de DA-Steer** (table 35, « agg. ») : aucun code.
- **Les scripts de reproduction et d'analyse des études de cas**, renvoyés au dépôt compagnon DiscoveryAgent-reproduction (`README.md:16-17` « `Case-study analysis code shown in the manuscript is maintained in the companion` »).

### 3.3 Ce que le code fait et que le papier ne dit pas

- La **tâche** (brief) n'atteint jamais le directeur ; elle n'atteint que l'agent d'hypothèse, le concepteur de relecture et le rapport consolidé (2.2).
- Le **relecteur** ne se déclenche pas avec les configurations publiées, à cause d'un réglage de retenue qui dépend d'un pas d'hypothèse explicite à l'intérieur du tour (2.5).
- Le **rapport de fond** de littérature est produit, payé (un appel Perplexity) et gardé dans les journaux, mais n'entre dans aucune invite (2.3).
- La **protection des processus** réécrit une commande d'arrêt large en un arrêt de tous les processus python sauf l'orchestrateur et son parent (2.9).
- Les **compétences figées** de l'agent d'exécution : instantané copié dans un greffon temporaire, tout outil refusé avant leur chargement exact, sous-agent `skills_agent`, préchargement en deux essais (`DiscoveryAgent/tool_agents/execution_agent_cc.py:837-877`).
- La **reprise au niveau de la requête interrompue**, sans régénération par le directeur (2.10).
- Le **dossier du rapport d'exécution est supprimé** après lecture, avant le commit (2.6).
- **Six appels de compte de jetons** à l'API par point de contrôle et un par tour de parole du directeur (section 6).
- Un **`hash()` de la clé d'API** dans chaque point de contrôle (2.6).
- L'**expurgation des secrets** et le plafond de 8 Mio du journal de l'agent d'exécution (2.8).
- La **vérification des fichiers disparus** après chaque requête, sans détection des fichiers modifiés (2.8).
- Le **délai par défaut des commandes shell** de l'agent : 10 minutes (`scripts/run.py:48` « `os.environ['BASH_DEFAULT_TIMEOUT_MS'] = '600000'` »), plafond 2 heures (`DiscoveryAgent/config.py:227` « `os.environ['BASH_MAX_TIMEOUT_MS'] = '7200000'  # 2 hours` »).
- Le **mode jeu croissant** : la liste des fichiers de `data/downloads` est réinjectée dans la description du directeur après chaque requête (`DiscoveryAgent/director_workflow.py:1146-1147` « `self._refresh_dataset_description()` »).
- La consigne de relance « SHORTER » est présentée au directeur comme une **critique du relecteur** (2.5).
- L'agent recensement garde sa **conversation d'un appel à l'autre** et a un modèle codé en dur (`acs_agent/agent.py:128` « `MODEL = "claude-opus-4-6"` »).
- Le **concepteur de relecture est rappelé à chaque lancement**, donc à chaque tour en mode piloté (un tour par lancement), et une fois de plus lors d'une restauration en cours de tour.
- Le README signale que le point de contrôle initial conservé de DA-Auto avait les drapeaux de sélection activés (`README.md:187-190` « `The retained initial checkpoint has selection flags enabled despite the` »).
<!-- FIN-PARTIE -->
